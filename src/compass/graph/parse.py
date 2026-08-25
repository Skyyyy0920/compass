"""Deterministic step parsing (the evidence layer).

One CodeAct turn -> one Step record. Nothing here calls a model, so this layer
never refuses and never drifts. Extracted per step:

  comments        the agent's chain-of-thought, i.e. ``# ...`` lines and any
                  separate reasoning text
  api_sigs        ``app.api(canon args)`` (Trace-compatible)
  api_names       ``app.api``
  defs / uses     module-level names bound in the cell / free names read that
                  were bound by an earlier cell (Python AST; regex fallback)
  status          ok | blocked   (AppWorld's own error contract)
  error_class     coarse traceback class for blocked steps
  printed         structured values recovered from the observation (JSON, ids,
                  emails, tokens, counts)
"""
from __future__ import annotations

import ast
import builtins
import json
import re

from ..eval.signatures import is_error, sigs
from ..harness.prompt import count_tokens

APINAME = re.compile(r"apis\.(\w+)\.(\w+)\(")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
TOKENISH = re.compile(r"['\"]?(access_token|token)['\"]?\s*[:=]\s*['\"]([A-Za-z0-9._\-]{8,})['\"]")
IDFIELD = re.compile(r"\"(\w*?(?:_id|id))\":\s*(\d+|\"[^\"]+\")")
TRACEBACK_LAST = re.compile(r"\n(\w+(?:Error|Exception))\b[:\s]")


def comments_of(code: str, reasoning: str | None = None) -> list[str]:
    out = []
    if reasoning and reasoning.strip():
        out.extend(l.strip() for l in reasoning.strip().splitlines() if l.strip())
    for line in (code or "").splitlines():
        s = line.strip()
        if s.startswith("#"):
            s = s.lstrip("#").strip()
            if s:
                out.append(s)
    return out


class _Vars(ast.NodeVisitor):
    def __init__(self):
        self.defs: list[str] = []
        self.loads: list[str] = []
        self.loop_vars: list[str] = []
        self._in_loop_target = False

    def _bind(self, target):
        if isinstance(target, ast.Name):
            (self.loop_vars if self._in_loop_target else self.defs).append(target.id)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for e in target.elts:
                self._bind(e)
        elif isinstance(target, ast.Starred):
            self._bind(target.value)

    def visit_Assign(self, n):
        for t in n.targets:
            self._bind(t)
        self.generic_visit(n)

    def visit_AugAssign(self, n):
        self._bind(n.target)
        self.generic_visit(n)

    def visit_AnnAssign(self, n):
        self._bind(n.target)
        self.generic_visit(n)

    def visit_For(self, n):
        self._in_loop_target = True
        self._bind(n.target)
        self._in_loop_target = False
        self.generic_visit(n)

    def visit_With(self, n):
        for it in n.items:
            if it.optional_vars is not None:
                self._bind(it.optional_vars)
        self.generic_visit(n)

    def visit_FunctionDef(self, n):
        self.defs.append(n.name)
        for d in n.decorator_list:
            self.visit(d)

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_ClassDef(self, n):
        self.defs.append(n.name)

    def visit_Import(self, n):
        for a in n.names:
            self.defs.append((a.asname or a.name).split(".")[0])

    def visit_ImportFrom(self, n):
        for a in n.names:
            self.defs.append(a.asname or a.name)

    def visit_Name(self, n):
        if isinstance(n.ctx, ast.Load):
            self.loads.append(n.id)
        self.generic_visit(n)

    def visit_comprehension(self, n):
        self.visit(n.iter)
        for i in n.ifs:
            self.visit(i)


_BUILTIN = set(dir(builtins)) | {"apis", "datetime", "json", "re", "time", "math", "collections", "timedelta"}


def defs_uses(code: str) -> tuple[list[str], list[str], bool]:
    """(defs, free loads, parsed_ok). Free loads exclude names the cell itself binds."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        defs = re.findall(r"^\s*([A-Za-z_]\w*)\s*=[^=]", code, flags=re.MULTILINE)
        uses = [n for n in set(re.findall(r"\b([A-Za-z_]\w*)\b", code)) if n not in defs]
        return list(dict.fromkeys(defs)), [u for u in uses if u not in _BUILTIN], False
    v = _Vars()
    v.visit(tree)
    loops = set(v.loop_vars)
    defs = [d for d in dict.fromkeys(v.defs) if d not in loops]
    dset = set(defs) | loops
    uses = [n for n in dict.fromkeys(v.loads) if n not in dset and n not in _BUILTIN]
    return defs, uses, True


def error_class(observation: str) -> str | None:
    if not is_error(observation):
        return None
    if observation.strip() == "No code available to execute.":
        return "no_code"
    m = TRACEBACK_LAST.findall(observation)
    name = m[-1] if m else None
    if "Number of requests exceeded" in observation:
        return "request_limit"
    if "timed out" in observation:
        return "timeout"
    if name == "NameError":
        return "name_error"
    if name in ("KeyError", "TypeError", "IndexError", "AttributeError", "ValueError"):
        return "data_shape"
    if "401" in observation or "Unauthorized" in observation:
        return "auth"
    if "422" in observation or "400" in observation or "Invalid" in observation:
        return "bad_argument"
    if "404" in observation or "not found" in observation.lower():
        return "not_found"
    if name == "SyntaxError":
        return "syntax"
    return name or "other"


def printed_values(observation: str) -> dict:
    """Cheap structured recovery from the observation text."""
    out: dict = {}
    text = observation or ""
    try:
        parsed = json.loads(text)
        out["json"] = parsed
        if isinstance(parsed, list):
            out["n_items"] = len(parsed)
    except Exception:  # noqa: BLE001
        pass
    emails = list(dict.fromkeys(EMAIL.findall(text)))
    if emails:
        out["emails"] = emails[:50]
    toks = [t[1] for t in TOKENISH.findall(text)]
    if toks:
        out["tokens"] = toks[:5]
    ids = IDFIELD.findall(text)
    if ids:
        agg: dict[str, list] = {}
        for k, v in ids:
            agg.setdefault(k, [])
            if v not in agg[k] and len(agg[k]) < 50:
                agg[k].append(v)
        out["ids"] = agg
    m = re.fullmatch(r"\s*(\d+)\s*", text)
    if m:
        out["scalar"] = int(m.group(1))
    return out


def parse_step(turn: dict) -> dict:
    code = turn.get("code") or ""
    obs = turn.get("observation") or ""
    defs, uses, ok = defs_uses(code)
    return {
        "step": turn["step"],
        "code": code,
        "observation": obs,
        "comments": comments_of(code, turn.get("reasoning")),
        "api_sigs": sigs(code),
        "api_names": list(dict.fromkeys(f"{a}.{b}" for a, b in APINAME.findall(code))),
        "defs": defs,
        "uses": uses,
        "ast_ok": ok,
        "status": "blocked" if is_error(obs) else "ok",
        "error_class": error_class(obs),
        "printed": printed_values(obs),
        "obs_tokens": count_tokens(obs[:4000]),
    }
