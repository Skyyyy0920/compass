"""COMPASS v2 as a ``Compressor``.

State lives in the graph, which persists across boundaries in this object,
keyed by the exact handover text it produced (the episode loop hands that text
back as ``prev_summary``). When ``prev_summary`` is unknown (a different
compressor's summary, e.g. in the shared-cohort verifier) it is kept as a
legacy node and the graph is rebuilt from the turns at hand.

Variants (method names accepted by ``make_compass``):
  compass_v2      hybrid: deterministic graph + LLM refine   (the method)
  compass_det     deterministic only, no LLM call            (ablation A1)
  compass_nodone  hybrid but the executed-API section hidden (ablation A5)
"""
from __future__ import annotations

import hashlib

from jinja2 import Template

from ..harness.compressors import Compressor, clip_turns
from ..harness.llm import LLM
from ..harness.prompt import count_tokens, load_prompt
from .build import Graph
from .refine import refine_graph
from .flow import attach_to_frontier, narrate, prune_evidence, render_flow_to_budget
from .render import live_variable_line, render_to_budget


def _h(text: str | None) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()


class CompassCompressor(Compressor):
    name = "compass_v2"

    def __init__(self, llm: LLM | None, budget: int = 4096, *, summary_budget: int | None = None,
                 use_llm: bool = True, hide_sections: tuple[str, ...] = (), det_needs: bool = True,
                 adapter: str = "codeact", summary_frac: float = 0.4, flow: bool = False,
                 narrate: bool = False):
        super().__init__(llm, budget)
        self.summary_budget = summary_budget or max(600, int(budget * summary_frac))
        self.flow = flow
        self.narrate = narrate and llm is not None
        self.use_llm = use_llm and llm is not None
        self.hide_sections = tuple(hide_sections)
        self.det_needs = det_needs
        self.adapter = adapter
        self._graphs: dict[str, dict] = {}
        self.last_extra: dict | None = None

    def compress(self, task: str, prev_summary: str | None, turns: list[dict]) -> str:
        key = _h(prev_summary)
        if prev_summary and key in self._graphs:
            g = Graph.from_dict(self._graphs[key])
            rebuilt = False
        else:
            g = Graph(task)
            g.legacy_summary = prev_summary
            rebuilt = prev_summary is not None
        new_ids = []
        for t in clip_turns(turns):
            if f"s{t['step']}" in g.steps:
                continue
            s = g.add_turn(t, self.adapter)
            new_ids.append(s["id"])
        stats: dict = {}
        if self.use_llm and new_ids:
            try:
                stats = refine_graph(g, new_ids, self.llm)
            except Exception as e:  # noqa: BLE001
                stats = {"error": str(e)[:200]}
                g.log.append({"drop": "refine_call_failed", "err": str(e)[:200]})
        if self.det_needs:
            g.augment_needs(new_ids[-3:])
        attached = pruned = 0
        if self.flow:
            attached = attach_to_frontier(g, new_ids[-3:])
            pruned = prune_evidence(g, new_ids[-3:])
            text, level = render_flow_to_budget(g, self.summary_budget, new_ids[-3:])
            if self.narrate:
                structured = text
                try:
                    text = narrate(structured, self.llm, self.summary_budget)
                    if count_tokens(text) > self.summary_budget * 1.2:
                        text = structured
                except Exception:  # noqa: BLE001
                    text = structured
        else:
            text, level = render_to_budget(g, self.summary_budget, new_ids[-3:])
        degraded = False
        if level == 4 and self.llm is not None:
            user = Template(load_prompt("openclaw_first.jinja")).render(history=text)
            try:
                text = self.llm.chat([{"role": "system", "content": load_prompt("openclaw_system.jinja")},
                                     {"role": "user", "content": user}], tag="fallback").strip()
                text += "\n\n" + live_variable_line(g)
                degraded = True
            except Exception:  # noqa: BLE001
                pass
        if self.hide_sections:
            text = _drop_sections(text, self.hide_sections)
        self._graphs[_h(text)] = g.to_dict()
        self.last_extra = {"level": level, "degraded": degraded, "rebuilt_from_legacy": rebuilt,
                           "n_steps": len(g.steps), "n_intents": len(g.intents), "n_infos": len(g.infos),
                           "n_facts": len(g.facts), "summary_tokens": count_tokens(text),
                           "attached": attached, "pruned_steps": pruned,
                           "refine": stats, "drops": g.log[-10:]}
        return text

    def render_context(self, summary: str) -> str:
        return ("\n\n<history_summary>\nThe conversation so far was compacted into this plan-graph checkpoint. "
                "Variables listed as LIVE are still defined in the Python session.\n"
                f"{summary}\n</history_summary>\n\n")


def _drop_sections(text: str, headers: tuple[str, ...]) -> str:
    """Remove rendered sections whose header line starts with one of ``headers``.
    A section ends at the next blank line."""
    out, skip = [], False
    for line in text.splitlines():
        if any(line.startswith(h) for h in headers):
            skip = True
            continue
        if skip and line.strip() == "":
            skip = False
        if not skip:
            out.append(line)
    return "\n".join(out)


VARIANTS = {
    "compass_v2": {},                                                     # the method
    "compass_det": {"use_llm": False},                                    # A1 deterministic only
    "compass_nospec": {"hide_sections": ("API DOCS ALREADY READ",)},      # A3 no API signatures
    "compass_novars": {"hide_sections": ("LIVE VARIABLES",)},             # A4 no live variables
    "compass_nodone": {"hide_sections": ("CALL FORMS THAT", "API DOCS ALREADY READ", "RESULTS ALREADY")},  # A5 no history
    "compass_noplan": {"hide_sections": ("PLAN (", "NEXT", "CONSTRAINTS", "FACTS")},        # A2 no intent layer
    "compass_llmneeds": {"det_needs": False},                             # A4b LLM-only needs
    # adapter tiers (paper: Generic <= Schema-aware <= Domain-specific); compass_v2 == codeact
    "compass_v3": {"flow": True},            # flow graph: attach-to-node, prune evidence, plan-first render
    "compass_v3_det": {"flow": True, "use_llm": False},
    "compass_v3_nl": {"flow": True, "narrate": True},   # same content, narrated by the LLM as the final surface
    "compass_generic": {"adapter": "generic"},
    "compass_schema": {"adapter": "schema"},
    "compass_codeaware": {},
    "compass_wide": {"summary_frac": 0.6},                                 # A6b larger handover budget
}


def make_compass(method: str, llm: LLM, budget: int) -> CompassCompressor:
    if method not in VARIANTS:
        raise ValueError(f"unknown compass variant {method}; known: {sorted(VARIANTS)}")
    kw = dict(VARIANTS[method])
    c = CompassCompressor(None if kw.pop("use_llm", True) is False else llm, budget, **kw,
                          **({"use_llm": False} if VARIANTS[method].get("use_llm") is False else {}))
    c.name = method
    return c
