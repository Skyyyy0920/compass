"""Requirement-state note: one LLM call per boundary, verified against the private graph.

    N_k = Verify_G(Note_phi(N_{k-1}, Q_k, u))

``progress_note`` is the model call (prompt family ``progress5`` for the main method); the
remaining functions are the deterministic verifier and the requirement-node bookkeeping:

- ``ground_note``: a DONE / PARTIAL status survives only if the line cites step ids that exist
  in the graph and executed without error, otherwise it is rewritten as NOT DONE (unverified).
  This is what makes ``DONE(c) => exists e in G_k: SUPPORTS(e, c) and outcome(e) = ok`` hold
  by construction rather than by prompt instruction.
- ``parse_requirements`` / ``splice_requirements``: the verified clauses become requirement
  nodes with SUPPORTS edges, and the note's requirement section is regenerated from them.
- ``strip_requirements``: used when a requirement graph (``requirements.py``) renders that
  section instead of the note.
"""
from __future__ import annotations

import re

from jinja2 import Template

from ..harness.compressors import turns_to_text
from ..harness.llm import LLM
from ..harness.prompt import count_tokens, load_prompt

STEP_ID_RE = re.compile(r"\bs\d+\b")
STATUS_RE = re.compile(r"(?<!NOT )(?<!NOT_)\b(DONE|PARTIAL)\b")
REQ_RE = re.compile(r'^\s*-\s*"(?P<text>[^"]{3,}?)"\s*(?:--|-|:)\s*(?P<status>DONE|PARTIAL|NOT DONE)(?P<rest>.*)$')


def progress_note(llm: LLM, task: str, prev: str | None, turns: list[dict], max_tokens: int,
                  prompts: str = "progress") -> str:
    """Progress note (handled / not yet done / next), incrementally updated from the previous
    note and the new turns; the evidence layer is rendered separately, so the note is told not
    to repeat values."""
    hist = turns_to_text(turns)
    tpl = f"{prompts}_update.jinja" if prev else f"{prompts}_first.jinja"
    user = Template(load_prompt(tpl)).render(history=hist, prev_summary=prev or "", task=task)
    out = llm.chat([{"role": "system", "content": load_prompt("openclaw_system.jinja")},
                    {"role": "user", "content": user}], tag="narrative").strip()
    if count_tokens(out) > max_tokens:
        lines, kept = out.splitlines(), []
        for ln in lines:
            kept.append(ln)
            if count_tokens("\n".join(kept)) > max_tokens:
                kept.pop()
                break
        out = "\n".join(kept)
    return out


def ground_note(note: str, g) -> tuple[str, int]:
    """Verify every DONE / PARTIAL line against the graph. Returns the note and the number of
    lines downgraded to NOT DONE (unverified)."""
    out, n = [], 0
    for line in note.splitlines():
        if STATUS_RE.search(line) and not line.lstrip().startswith("#"):
            ids = STEP_ID_RE.findall(line)
            ok = bool(ids) and all(i in g.steps and g.steps[i].get("status") == "ok" for i in ids)
            if not ok:
                line = STATUS_RE.sub("NOT DONE (unverified)", line, count=1)
                n += 1
        out.append(line)
    return "\n".join(out), n


def parse_requirements(note: str, g) -> list[dict]:
    """Requirement nodes from the verified note: one per quoted instruction clause, with the
    status the verifier left and SUPPORTS edges to the cited steps (only steps that exist)."""
    reqs = []
    for line in note.splitlines():
        m = REQ_RE.match(line)
        if not m:
            continue
        ids = [i for i in STEP_ID_RE.findall(m.group("rest")) if i in g.steps]
        status = m.group("status")
        if status != "NOT DONE" and not ids:
            status = "NOT DONE"
        detail = re.sub(r"\[[^\]]*\]", "", m.group("rest")).strip(" ,;()")
        reqs.append({"id": f"r{len(reqs) + 1}", "text": m.group("text"), "status": status,
                     "detail": detail[:120], "supports": ids})
    return reqs


def splice_requirements(note: str, reqs: list[dict]) -> str:
    """Regenerate the requirement section of the note from the requirement nodes."""
    if not reqs:
        return note
    lines = note.splitlines()
    out, i, replaced = [], 0, False
    while i < len(lines):
        line = lines[i]
        if not replaced and line.startswith("## ") and "requirement" in line.lower():
            out.append("## Task requirements (quoted from the instruction) and verified status")
            for r in reqs:
                sup = f" [{', '.join(r['supports'])}]" if r["supports"] else ""
                det = f" ({r['detail']})" if r["detail"] else ""
                out.append(f"- {r['id']}: \"{r['text']}\" -- {r['status']}{det}{sup}")
            i += 1
            while i < len(lines) and not lines[i].startswith("## "):
                i += 1
            replaced = True
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def strip_requirements(note: str) -> str:
    """Drop the note's own requirement section: the requirement graph renders it instead."""
    out, skip = [], False
    for line in (note or "").splitlines():
        if line.startswith("## "):
            skip = "requirement" in line.lower()
        if not skip:
            out.append(line)
    return "\n".join(out).strip()
