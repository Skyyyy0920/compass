"""Deterministic rendering of the graph into the handover, with a fold ladder.

Level 0  everything: done intents with their evidence one-liners and produced
         values, all live variables with value hints, facts, warnings
Level 1  done subtrees folded to one line each (macro nodes, keeping produced
         values that something ahead needs); live variables limited to those
         needed by open intents or consumed recently
Level 2  frontier only: open intents, their needs, facts; done work as a bare
         list of API names already executed
Level 3  caller falls back to an LLM shrink of the level-2 text (degraded).

The DONE section carries the executed API names so the agent can see what was
already called (the refetch guard v1 lacked).
"""
from __future__ import annotations

from ..harness.prompt import count_tokens
from .build import Graph, Info, Intent, compact_step_view


def _short(text: str | None, n: int) -> str:
    t = (text or "").strip()
    return t if len(t) <= n else t[:n] + "..."


def _status_mark(s: str) -> str:
    return {"done": "[x]", "blocked": "[!]", "invalidated": "[-]", "active": "[>]", "pending": "[ ]"}[s]


def _tree(g: Graph) -> list[tuple[Intent, int]]:
    roots = [it for it in g.intents.values() if it.parent is None or it.parent not in g.intents]
    out: list[tuple[Intent, int]] = []

    def walk(it: Intent, depth: int):
        out.append((it, depth))
        for c in it.children:
            if c in g.intents:
                walk(g.intents[c], depth + 1)
    for r in sorted(roots, key=lambda x: x.order):
        walk(r, 0)
    return out


def _subtree_done(g: Graph, it: Intent) -> bool:
    if it.status not in ("done", "invalidated"):
        return False
    return all(_subtree_done(g, g.intents[c]) for c in it.children if c in g.intents)


def _executed_apis(g: Graph, step_ids: list[str]) -> list[str]:
    out = []
    for s in step_ids:
        st = g.steps.get(s)
        if st and st["status"] == "ok":
            out.extend(st["api_names"])
    return list(dict.fromkeys(out))


def render(g: Graph, level: int, recent_ids: list[str]) -> str:
    L: list[str] = ["GOAL", g.goal.strip()]
    if g.legacy_summary and level <= 1:
        L += ["", "EARLIER SUMMARY (pre-graph)", g.legacy_summary.strip()[:1500]]
    facts = [f for f in g.facts if f["kind"] == "constraint"]
    if facts:
        L += ["", "CONSTRAINTS"] + [f"- {f['text']}" for f in facts]

    tree = _tree(g)
    if tree:
        L += ["", "PLAN (status: [x] done  [>] active  [ ] pending  [!] blocked  [-] invalidated)"]
        skip_under: set[str] = set()
        shown_evidence: set[str] = set()
        for it, depth in tree:
            if it.parent in skip_under:
                skip_under.add(it.id)
                continue
            ind = "  " * depth
            line = f"{ind}{_status_mark(it.status)} {it.id} {it.description}"
            if it.status in ("done", "invalidated") and level >= 1 and _subtree_done(g, it):
                skip_under.add(it.id)
                apis = _executed_apis(g, it.evidence)
                if apis and level <= 2:
                    line += f"  (executed: {', '.join(apis[:6])})"
                prod = g.produced_by_intent(it)
                if prod and it.status == "done":
                    line += "  -> " + "; ".join(f"{i.name} = {_short(i.value_hint, 60 if level <= 2 else 30)}" for i in prod)
                L.append(line)
                continue
            if it.note and it.status in ("blocked", "active", "invalidated"):
                line += f"  -- {it.note}" + ("  [agent's own conclusion; re-verify]" if it.status == "invalidated" else "")
            if it.needs and it.status not in ("done", "invalidated"):
                names = [g.infos[n].name for n in it.needs if n in g.infos]
                if names:
                    line += f"  needs: {', '.join(names[:6])}" + (" ..." if len(names) > 6 else "")
            L.append(line)
            if level == 0 and it.status == "done":
                for e in it.evidence[-3:]:
                    if e in g.steps and e not in shown_evidence:
                        shown_evidence.add(e)
                        L.append(f"{ind}    - {compact_step_view(g.steps[e], 70)}")
                prod = g.produced_by_intent(it)
                if prod:
                    L.append(f"{ind}    -> " + "; ".join(f"{i.name} = {_short(i.value_hint, 80)}" for i in prod))

    if g.calls_ok and level <= 2:
        L += ["", "CALL FORMS THAT WORKED (exact argument names; reuse them, do not re-login)"]
        L += [f"- {f}" for f in list(g.calls_ok)[-30:]]
    if g.calls_failed and level <= 2:
        L += ["", "CALL FORMS THAT FAILED (do not repeat as written)"]
        L += [f"- {f} -> {e}" for f, e in list(g.calls_failed.items())[-8:]]
    lists = [i for i in g.infos.values() if i.kind == "api_list" and i.name != "apps"]
    specs = [i for i in g.infos.values() if i.kind == "api_spec"]
    if lists or specs:
        L += ["", "API DOCS ALREADY READ (exact signatures; do not call api_docs again for these)"]
        if level <= 2:
            for i in lists[-6:]:
                hint = i.value_hint or ""
                if level == 2 and len(hint) > 300:
                    hint = hint[:300] + " ... (more; listing shortened here)"
                L.append(f"- {i.name} apis: {hint}")
        for i in specs[-(25 if level <= 1 else 12):]:
            L.append(f"- {_short(i.value_hint, 220 if level <= 1 else 150)}")

    if level <= 1:
        infos = g.live_infos(recent_steps=3 if level == 1 else 8)
        if level == 1:
            open_intents = {it.id for it in g.intents.values() if it.status not in ("done", "invalidated")}
            recent = set(recent_ids)
            infos = [i for i in infos if any(n in open_intents for n in i.needed_by)
                     or any(c in recent for c in i.consumers) or i.source_api or i.name.endswith("token")]
        rt = [i for i in infos if i.kind == "runtime_reference"]
        if rt:
            L += ["", "LIVE VARIABLES (still bound in the Python session; reuse them, do not recompute)"]
            for i in rt[-40:]:
                src = f" = {i.source_api}(...)" if i.source_api else ""
                hint = f" -> {i.value_hint}" if i.value_hint else ""
                L.append(f"- {i.name}{src}{hint}")
    else:
        rt = [i for i in g.live_infos(recent_steps=2) if i.kind == "runtime_reference"]
        if rt:
            L += ["", "LIVE VARIABLES: " + ", ".join(i.name for i in rt[-30:])]
        # plan-conditioned floor: whatever the frontier needs keeps its value even at the
        # coarsest levels (folding must not drop what the next computation consumes)
        needed: list[Info] = []
        for it in g.frontier():
            for n in it.needs:
                i = g.infos.get(n)
                if i and i.value_hint and i.kind == "runtime_reference" and not i.superseded and i not in needed:
                    needed.append(i)
        recent = set(recent_ids)
        for i in g.infos.values():
            if i.kind == "runtime_reference" and not i.superseded and i.value_hint and i not in needed \
                    and any(c in recent for c in i.consumers):
                needed.append(i)
        if needed:
            L += ["", "VALUES THE NEXT STEPS NEED (still bound; reuse instead of recomputing)"]
            for i in needed[-12:]:
                L.append(f"- {i.name} = {_short(i.value_hint, 160)}")

    results = [i for i in g.infos.values() if i.kind == "api_result" and i.value_hint]
    if results and level <= 2:
        keep, chars = (20, 160) if level <= 1 else (12, 90)
        L += ["", "RESULTS ALREADY OBSERVED (printed, not stored in a variable; do not call again)"]
        for i in results[-keep:]:
            L.append(f"- {_short(i.name, 90)} -> {_short(i.value_hint, chars)}")

    other = [f for f in g.facts if f["kind"] != "constraint"]
    if other:
        L += ["", "FACTS"] + [f"- {f['text']}" for f in other[-15:]]

    generic = all(st["status"] == "unknown" for st in g.steps.values()) and g.steps
    if generic and level <= 2:
        # generic adapter: no outcome or schema; keep the raw record of what was executed
        recent = sorted(g.steps, key=lambda s: int(s[1:]))[-12:]
        L += ["", "ACTIONS ALREADY EXECUTED (most recent; tool -> observation excerpt)"]
        for s in recent:
            st = g.steps[s]
            L.append(f"- {s} {','.join(st['api_names'][:3]) or 'code'} -> {_short(st['observation'], 100)}")
    warn = [g.steps[s] for s in g.steps if g.steps[s]["status"] == "blocked" and not g.steps[s].get("call_forms")]
    if warn and level <= 2:
        L += ["", "WARNINGS (non-API errors seen; avoid repeating)"]
        for s in warn[-4:]:
            L.append(f"- {s['id']} {s['error_class']}: {s.get('error_line') or ''}")

    front = g.frontier()
    if front:
        L += ["", "NEXT"]
        for it in front[:5]:
            needs = ", ".join(g.infos[n].name for n in it.needs if n in g.infos)
            L.append(f"- {it.id} {it.description}" + (f" (needs {needs})" if needs else ""))
    return "\n".join(L)


def live_variable_line(g: Graph) -> str:
    rt = [i for i in g.live_infos(recent_steps=2) if i.kind == "runtime_reference"]
    return "LIVE VARIABLES (still bound in the Python session): " + ", ".join(i.name for i in rt[-40:]) if rt else ""


def render_to_budget(g: Graph, budget: int, recent_ids: list[str]) -> tuple[str, int]:
    """Levels 0-3 are deterministic folds; 4 means 'still over budget, caller degrades'."""
    for level in (0, 1, 2, 3):
        text = render(g, level, recent_ids)
        if count_tokens(text) <= budget:
            return text, level
    return render(g, 3, recent_ids), 4
