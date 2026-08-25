"""The three-layer text-attributed action graph.

Layers
  Step    s<t>   one action-observation, fully deterministic (parse.py)
  Info    i<n>   a value the run holds: a runtime variable, an API result, a
                 constraint or a fact. PRODUCES / CONSUMES edges come from the
                 AST def/use analysis, so they are exact for CodeAct agents.
  Intent  c<n>   a plan item (goal decomposition). Intents are proposed by a
                 small LLM call (refine.py) and validated here; their status is
                 grounded in step evidence, never merely declared.

The graph is a plain data structure: every mutation goes through a method that
keeps it legal (no dangling references, parents exist, no cycles), so an LLM
proposal can only ever add legal structure or be dropped item by item.
"""
from __future__ import annotations

import ast
import json
import re
from dataclasses import asdict, dataclass, field

from .parse import parse_step

STATUSES = ("pending", "active", "done", "blocked", "invalidated")


@dataclass
class Info:
    id: str
    kind: str                      # runtime_reference | api_result | fact | constraint | failure
    name: str                      # variable name or short label
    producer: str | None = None    # step id
    source_api: str | None = None  # app.api that produced it (if known)
    value_hint: str | None = None  # short canonical excerpt of the value
    description: str | None = None
    consumers: list[str] = field(default_factory=list)   # step ids that read it
    needed_by: list[str] = field(default_factory=list)   # intent ids predicted to need it
    superseded: bool = False       # a later def rebound the same name


@dataclass
class Intent:
    id: str
    description: str
    parent: str | None = None
    children: list[str] = field(default_factory=list)
    status: str = "pending"
    evidence: list[str] = field(default_factory=list)    # step ids
    needs: list[str] = field(default_factory=list)       # info ids
    produces: list[str] = field(default_factory=list)    # info ids
    note: str | None = None                              # short LLM note (e.g. why blocked)
    order: int = 0


class Graph:
    def __init__(self, goal: str):
        self.goal = goal
        self.steps: dict[str, dict] = {}
        self.infos: dict[str, Info] = {}
        self.intents: dict[str, Intent] = {}
        self.facts: list[dict] = []             # {id, kind, text, steps}
        self.step_intent: dict[str, str] = {}   # REALIZES
        self.legacy_summary: str | None = None  # a non-graph previous summary, kept verbatim-ish
        self._n_info = 0
        self._n_intent = 0
        self._n_fact = 0
        self.log: list[dict] = []               # dropped proposals, for diagnostics

    # ------------------------------------------------------------------ steps / infos
    def _latest_info_for(self, name: str) -> Info | None:
        cands = [i for i in self.infos.values() if i.kind == "runtime_reference" and i.name == name and not i.superseded]
        return cands[-1] if cands else None

    def add_turn(self, turn: dict) -> dict:
        s = parse_step(turn)
        sid = f"s{s['step']}"
        s["id"] = sid
        s["produces"] = []
        s["consumes"] = []
        self.steps[sid] = s
        # CONSUMES: free loads bound by an earlier cell
        for name in s["uses"]:
            info = self._latest_info_for(name)
            if info is not None:
                info.consumers.append(sid)
                s["consumes"].append(info.id)
        # PRODUCES: module-level defs
        api_by_var = _assigned_api_calls(s["code"])
        literals = _literal_assignments(s["code"])
        for name in s["defs"]:
            prev = self._latest_info_for(name)
            if prev is not None:
                prev.superseded = True
            self._n_info += 1
            info = Info(id=f"i{self._n_info}", kind="runtime_reference", name=name, producer=sid,
                        source_api=api_by_var.get(name),
                        value_hint=literals.get(name) or _value_hint(s, name))
            self.infos[info.id] = info
            s["produces"].append(info.id)
        # API documentation read by the agent -> api_spec / api_list infos (deduped by name)
        for spec in s.get("api_specs", []):
            name = spec.split("(", 1)[0]
            old = next((i for i in self.infos.values() if i.kind == "api_spec" and i.name == name), None)
            if old is not None:
                old.value_hint, old.producer = spec, sid
                continue
            self._n_info += 1
            self.infos[f"i{self._n_info}"] = Info(id=f"i{self._n_info}", kind="api_spec", name=name, producer=sid,
                                                  source_api="api_docs.show_api_doc", value_hint=spec)
            s["produces"].append(f"i{self._n_info}")
        for app, names in (s.get("api_lists") or {}).items():
            old = next((i for i in self.infos.values() if i.kind == "api_list" and i.name == app), None)
            hint = ", ".join(names[:60])
            if s.get("api_list_truncated"):
                hint += " ... (listing was TRUNCATED by the output limit: more APIs exist; " \
                        "query api_docs.show_api_doc for specific names or use page_limit/keywords)"
            if old is not None:
                old.value_hint, old.producer = hint, sid
                continue
            self._n_info += 1
            self.infos[f"i{self._n_info}"] = Info(id=f"i{self._n_info}", kind="api_list", name=app, producer=sid,
                                                  source_api="api_docs.show_api_descriptions", value_hint=hint)
            s["produces"].append(f"i{self._n_info}")
        # api results not bound to a variable but printed (non-doc calls) -> api_result info
        if s["status"] == "ok" and s["api_names"] and not s["defs"] and not s.get("api_specs") and not s.get("api_lists"):
            for api in s["api_names"]:
                self._n_info += 1
                obs = s["observation"]
                info = Info(id=f"i{self._n_info}", kind="api_result", name=api, producer=sid, source_api=api,
                            value_hint=_excerpt(obs, SMALL_VALUE_CHARS if len(obs) <= SMALL_VALUE_CHARS else 240))
                self.infos[info.id] = info
                s["produces"].append(info.id)
        return s

    # ------------------------------------------------------------------ intents
    def add_intent(self, description: str, parent: str | None = None, iid: str | None = None) -> Intent | None:
        if parent is not None and parent not in self.intents:
            self.log.append({"drop": "intent_parent_missing", "parent": parent, "desc": description})
            return None
        if iid is None or iid in self.intents or not re.fullmatch(r"c\d+", iid):
            self._n_intent += 1
            iid = f"c{self._n_intent}"
        else:
            self._n_intent = max(self._n_intent, int(iid[1:]))
        it = Intent(id=iid, description=description.strip()[:300], parent=parent, order=len(self.intents))
        self.intents[iid] = it
        if parent:
            self.intents[parent].children.append(iid)
        return it

    def set_status(self, iid: str, status: str, evidence: list[str], note: str | None = None) -> bool:
        """Grounded status update. ``done`` and ``blocked`` need step evidence."""
        it = self.intents.get(iid)
        if it is None or status not in STATUSES:
            self.log.append({"drop": "bad_status", "intent": iid, "status": status})
            return False
        ev = [e for e in evidence if e in self.steps]
        if status == "done":
            ok = [e for e in ev if self.steps[e]["status"] == "ok"]
            if not ok:
                self.log.append({"drop": "done_without_ok_evidence", "intent": iid})
                status = "active" if it.status in ("pending", "active") else it.status
                ev = ev or it.evidence
        if status == "blocked":
            bad = [e for e in ev if self.steps[e]["status"] == "blocked"]
            if not bad:
                self.log.append({"drop": "blocked_without_error_evidence", "intent": iid})
                status = "active"
        if self.ungrounded_negative(note):
            # "no API exists" style conclusions need a complete API listing as evidence
            self.log.append({"drop": "ungrounded_negative_status", "intent": iid, "note": (note or "")[:80]})
            if status in ("blocked", "invalidated"):
                status = "active"
            note = "guessed API names failed; the API listing seen was incomplete -- look for other APIs"
        it.status = status
        it.evidence = list(dict.fromkeys(it.evidence + ev))
        if note:
            it.note = note[:200]
        return True

    def set_realizes(self, sid: str, iid: str) -> bool:
        if sid in self.steps and iid in self.intents:
            self.step_intent[sid] = iid
            if sid not in self.intents[iid].evidence:
                self.intents[iid].evidence.append(sid)
            return True
        self.log.append({"drop": "bad_realizes", "step": sid, "intent": iid})
        return False

    def set_needs(self, iid: str, info_ids: list[str]) -> None:
        it = self.intents.get(iid)
        if it is None:
            return
        for i in info_ids:
            if i in self.infos and i not in it.needs:
                it.needs.append(i)
                self.infos[i].needed_by.append(iid)

    def augment_needs(self, recent_ids: list[str]) -> int:
        """Deterministic NEEDS: every open intent is assumed to need the current
        credentials/tokens, everything consumed by the recent steps, and every
        variable consumed by two or more distinct steps so far (reused state)."""
        open_intents = [it for it in self.frontier()]
        if not open_intents:
            return 0
        cand = []
        recent = set(recent_ids)
        for i in self.infos.values():
            if i.kind != "runtime_reference" or i.superseded:
                continue
            n = i.name.lower()
            if re.search(r"token|password|login|session|auth|cred", n):
                cand.append(i.id)
            elif any(c in recent for c in i.consumers):
                cand.append(i.id)
            elif len(set(i.consumers)) >= 2:
                cand.append(i.id)
        added = 0
        for it in open_intents:
            before = len(it.needs)
            self.set_needs(it.id, cand)
            added += len(it.needs) - before
        return added

    NEGATIVE = re.compile(r"\b(no|not|cannot|can't|missing|unavailable|does not exist|doesn't exist|impossible|"
                          r"unsupported|lack|absent|none)\b", re.I)

    def complete_listing_seen(self, text: str = "") -> bool:
        """True if the app(s) the text talks about had a complete (untruncated)
        API listing observed. With no app named, any complete per-app listing counts."""
        complete, apps = set(), set()
        for st in self.steps.values():
            for app in (st.get("api_lists") or {}):
                if app == "apps":
                    apps.update(st["api_lists"][app])
                    continue
                apps.add(app)
                if not st.get("api_list_truncated"):
                    complete.add(app)
        named = {a for a in apps if re.search(rf"\b{re.escape(a)}\b", text, re.I)}
        if named:
            return named <= complete
        return bool(complete)

    def ungrounded_negative(self, text: str | None) -> bool:
        return bool(text) and bool(self.NEGATIVE.search(text)) \
            and bool(re.search(r"\bapi|endpoint|function|feature|way to|capabilit", text, re.I)) \
            and not self.complete_listing_seen(text)

    def add_fact(self, text: str, kind: str = "fact", steps: list[str] | None = None) -> dict | None:
        if self.ungrounded_negative(text):
            self.log.append({"drop": "ungrounded_negative_fact", "text": text[:100]})
            return None
        norm = re.sub(r"\W+", " ", text.lower()).strip()
        for f in self.facts:
            if re.sub(r"\W+", " ", f["text"].lower()).strip() == norm:
                return None
        self._n_fact += 1
        f = {"id": f"f{self._n_fact}", "kind": kind if kind in ("fact", "constraint", "failure") else "fact",
             "text": text.strip()[:300], "steps": [s for s in (steps or []) if s in self.steps]}
        self.facts.append(f)
        return f

    # ------------------------------------------------------------------ derived
    def frontier(self) -> list[Intent]:
        """Unresolved intents not represented by unresolved children."""
        out = []
        for it in sorted(self.intents.values(), key=lambda x: x.order):
            if it.status in ("done", "invalidated"):
                continue
            if it.children and any(self.intents[c].status not in ("done", "invalidated") for c in it.children):
                continue
            out.append(it)
        return out

    def live_infos(self, recent_steps: int = 3) -> list[Info]:
        """Infos something ahead can still use: needed by an open intent, consumed
        recently, or a current (non-superseded) runtime binding."""
        open_intents = {it.id for it in self.intents.values() if it.status not in ("done", "invalidated")}
        last = sorted(self.steps, key=lambda s: int(s[1:]))[-recent_steps:]
        out = []
        for i in self.infos.values():
            if i.kind == "runtime_reference" and i.superseded:
                continue
            if any(n in open_intents for n in i.needed_by) or any(c in last for c in i.consumers):
                out.append(i)
            elif i.kind == "runtime_reference":
                out.append(i)
        return out

    def to_dict(self) -> dict:
        return {"goal": self.goal, "steps": self.steps, "infos": {k: asdict(v) for k, v in self.infos.items()},
                "intents": {k: asdict(v) for k, v in self.intents.items()}, "facts": self.facts,
                "step_intent": self.step_intent, "legacy_summary": self.legacy_summary,
                "counters": [self._n_info, self._n_intent, self._n_fact], "log": self.log}

    @classmethod
    def from_dict(cls, d: dict) -> "Graph":
        g = cls(d["goal"])
        g.steps = d["steps"]
        g.infos = {k: Info(**v) for k, v in d["infos"].items()}
        g.intents = {k: Intent(**v) for k, v in d["intents"].items()}
        g.facts = d["facts"]
        g.step_intent = d["step_intent"]
        g.legacy_summary = d.get("legacy_summary")
        g._n_info, g._n_intent, g._n_fact = d["counters"]
        g.log = d.get("log", [])
        return g


# ---------------------------------------------------------------------- helpers
def _assigned_api_calls(code: str) -> dict[str, str]:
    """{var: 'app.api'} for ``var = apis.app.api(...)`` (possibly nested in an expression)."""
    out: dict[str, str] = {}
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            src = ast.unparse(node.value)
            m = re.search(r"apis\.(\w+)\.(\w+)\(", src)
            if m:
                out[node.targets[0].id] = f"{m.group(1)}.{m.group(2)}"
    return out


def _literal_assignments(code: str) -> dict[str, str]:
    """{var: repr(literal)} for ``var = <constant or short literal container>``."""
    out: dict[str, str] = {}
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return out
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            v = node.value
            if isinstance(v, ast.Constant) or (isinstance(v, (ast.List, ast.Tuple, ast.Dict, ast.Set))
                                               and len(ast.unparse(v)) <= 120):
                out[node.targets[0].id] = ast.unparse(v)[:120]
    return out


def _value_hint(step: dict, name: str) -> str | None:
    """A short value excerpt when the cell printed this variable (or only this one)."""
    code, obs = step["code"], step["observation"]
    if step["status"] != "ok" or not obs.strip() or obs.strip() == "Execution successful.":
        return None
    p = step["printed"]
    if (name.endswith("token") or name.endswith("login")) and p.get("tokens"):
        return "access_token " + p["tokens"][0][:10] + "..."
    printed = re.findall(r"print\(([^)]*)\)", code)
    hits = [pp for pp in printed if re.search(rf"\b{re.escape(name)}\b", pp)]
    if hits or (len(step["defs"]) == 1 and printed):
        # small structured results (credential lists, profiles, short id lists) are kept whole:
        # an excerpt of them is exactly what makes the agent re-fetch
        return _excerpt(obs, SMALL_VALUE_CHARS if len(obs) <= SMALL_VALUE_CHARS else 120)
    return None


SMALL_VALUE_CHARS = 900


def _excerpt(text: str, n: int) -> str:
    t = re.sub(r"\s+", " ", (text or "").strip())
    return t if len(t) <= n else t[:n] + "..."


def compact_step_view(s: dict, obs_chars: int = 160) -> str:
    """One-line evidence view of a step for LLM prompts and DONE sections."""
    tag = "OK " if s["status"] == "ok" else f"ERR:{s['error_class']}"
    apis = ",".join(s["api_names"][:4]) or "-"
    defs = ",".join(s["defs"][:6]) or "-"
    com = (" | " + s["comments"][0][:80]) if s["comments"] else ""
    return f"{s['id']} [{tag}] apis={apis} defs={defs}{com} -> {_excerpt(s['observation'], obs_chars)}"


def dumps(g: Graph) -> str:
    return json.dumps(g.to_dict(), ensure_ascii=False)
