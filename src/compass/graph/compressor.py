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
from .render import render_to_budget


def _h(text: str | None) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()


class CompassCompressor(Compressor):
    name = "compass_v2"

    def __init__(self, llm: LLM | None, budget: int = 4096, *, summary_budget: int | None = None,
                 use_llm: bool = True, hide_done: bool = False):
        super().__init__(llm, budget)
        self.summary_budget = summary_budget or max(600, budget // 3)
        self.use_llm = use_llm and llm is not None
        self.hide_done = hide_done
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
            s = g.add_turn(t)
            new_ids.append(s["id"])
        stats: dict = {}
        if self.use_llm and new_ids:
            try:
                stats = refine_graph(g, new_ids, self.llm)
            except Exception as e:  # noqa: BLE001
                stats = {"error": str(e)[:200]}
                g.log.append({"drop": "refine_call_failed", "err": str(e)[:200]})
        text, level = render_to_budget(g, self.summary_budget, new_ids[-3:])
        degraded = False
        if level == 3 and self.llm is not None:
            user = Template(load_prompt("openclaw_first.jinja")).render(history=text)
            try:
                text = self.llm.chat([{"role": "system", "content": load_prompt("openclaw_system.jinja")},
                                     {"role": "user", "content": user}], tag="fallback").strip()
                degraded = True
            except Exception:  # noqa: BLE001
                pass
        if self.hide_done:
            lines, out, skip = text.splitlines(), [], False
            for l in lines:
                if l.startswith("APIS ALREADY CALLED"):
                    skip = True
                    continue
                if skip:
                    skip = False
                    continue
                out.append(l)
            text = "\n".join(out)
        self._graphs[_h(text)] = g.to_dict()
        self.last_extra = {"level": level, "degraded": degraded, "rebuilt_from_legacy": rebuilt,
                           "n_steps": len(g.steps), "n_intents": len(g.intents), "n_infos": len(g.infos),
                           "n_facts": len(g.facts), "summary_tokens": count_tokens(text),
                           "refine": stats, "drops": g.log[-10:]}
        return text

    def render_context(self, summary: str) -> str:
        return ("\n\n<history_summary>\nThe conversation so far was compacted into this plan-graph checkpoint. "
                "Variables listed as LIVE are still defined in the Python session.\n"
                f"{summary}\n</history_summary>\n\n")


def make_compass(method: str, llm: LLM, budget: int) -> CompassCompressor:
    if method == "compass_v2":
        c = CompassCompressor(llm, budget)
    elif method == "compass_det":
        c = CompassCompressor(None, budget, use_llm=False)
    elif method == "compass_nodone":
        c = CompassCompressor(llm, budget, hide_done=True)
    else:
        raise ValueError(f"unknown compass variant {method}")
    c.name = method
    return c
