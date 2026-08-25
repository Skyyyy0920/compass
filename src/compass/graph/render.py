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
from .build import Graph, Intent, compact_step_view


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
                L.append(line)
                continue
            if it.note and it.status in ("blocked", "active", "invalidated"):
                line += f"  -- {it.note}"
            if it.needs and it.status not in ("done", "invalidated"):
                names = [g.infos[n].name for n in it.needs if n in g.infos]
                if names:
                    line += f"  needs: {', '.join(names)}"
            L.append(line)
            if level == 0 and it.status == "done":
                for e in it.evidence[-3:]:
                    if e in g.steps and e not in shown_evidence:
                        shown_evidence.add(e)
                        L.append(f"{ind}    - {compact_step_view(g.steps[e], 70)}")

    all_ok_apis = _executed_apis(g, sorted(g.steps, key=lambda s: int(s[1:])))
    if all_ok_apis and level <= 2:
        L += ["", "APIS ALREADY CALLED SUCCESSFULLY (do not re-read docs or re-login unless needed)",
              ", ".join(all_ok_apis[:40])]

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

    other = [f for f in g.facts if f["kind"] != "constraint"]
    if other:
        L += ["", "FACTS"] + [f"- {f['text']}" for f in other[-15:]]

    warn = [g.steps[s] for s in g.steps if g.steps[s]["status"] == "blocked"]
    if warn and level <= 2:
        L += ["", "WARNINGS (errors seen; avoid repeating)"]
        for s in warn[-5:]:
            L.append(f"- {s['id']} {s['error_class']}: {compact_step_view(s, 120).split('->', 1)[-1].strip()}")

    front = g.frontier()
    if front:
        L += ["", "NEXT"]
        for it in front[:5]:
            needs = ", ".join(g.infos[n].name for n in it.needs if n in g.infos)
            L.append(f"- {it.id} {it.description}" + (f" (needs {needs})" if needs else ""))
    return "\n".join(L)


def render_to_budget(g: Graph, budget: int, recent_ids: list[str]) -> tuple[str, int]:
    for level in (0, 1, 2):
        text = render(g, level, recent_ids)
        if count_tokens(text) <= budget:
            return text, level
    return render(g, 2, recent_ids), 3
