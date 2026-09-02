"""COMPASS as a ``Compressor``: evidence-grounded requirement-state compaction.

At every compaction boundary k the compressor emits one artifact, the checkpoint C_k:

    Q_k = Extract_alpha(delta tau_k)             adapter extracts bounded events (build.py); the raw
                                                 observation is destroyed after Apply
    G_k = Apply(G_{k-1}, Q_k), size(G_k) <= B_G  private graph under a byte budget (build.py)
    N_k = Verify_G(Note_phi(N_{k-1}, Q_k, u))    one LLM call, verified against the graph (note.py)
    C_k = Render_B(N_k, Fold(G_k | N_k))         |C_k| <= summary_frac * B (render.py)

State lives in the graph, which persists across boundaries in this object, keyed by the exact
handover text it produced (the episode loop hands that text back as ``prev_summary``). When
``prev_summary`` is unknown (a different compressor's summary, e.g. in the shared-cohort
verifier) it is kept as a legacy node and the graph is rebuilt from the turns at hand.

Method names accepted by ``make_compass`` are listed in ``VARIANTS`` below, grouped as
main method / ablations / variants / legacy. The helpers that used to live here are now in
``note.py`` (requirement-state note), ``externalize.py`` (+ExternalMemory) and
``requirements.py`` (frontier engine); they are re-exported for existing importers.
"""
from __future__ import annotations

import hashlib

from jinja2 import Template

from ..harness.compressors import Compressor, clip_turns
from ..harness.llm import LLM
from ..harness.prompt import count_tokens, load_prompt
from .build import GRAPH_BUDGET_CHARS, OBS_KEEP_CHARS, Graph
from .externalize import mem_setup_code, mem_value, worth_saving
from .flow import attach_to_frontier, narrate, prune_evidence, render_flow_to_budget
from .note import (
    ground_note,
    parse_requirements,
    progress_note,
    splice_requirements,
    strip_requirements,
)
from .refine import refine_graph
from .render import live_variable_line, render_to_budget
from .requirements import ReqGraph, frontier_update

__all__ = [
    "VARIANTS",
    "CompassCompressor",
    "frontier_update",
    "ground_note",
    "make_compass",
    "mem_setup_code",
    "mem_value",
    "parse_requirements",
    "progress_note",
    "splice_requirements",
    "strip_requirements",
]


def _h(text: str | None) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()


class CompassCompressor(Compressor):
    name = "compass_v2"

    def __init__(self, llm: LLM | None, budget: int = 4096, *, summary_budget: int | None = None,
                 use_llm: bool = True, hide_sections: tuple[str, ...] = (), det_needs: bool = True,
                 adapter: str = "codeact", summary_frac: float = 0.4, flow: bool = False,
                 narrate: bool = False, proj: bool = False, mem: bool = False,
                 narrative: bool = False, narrative_tokens: int = 450, nar_prompts: str = "progress",
                 frontier: bool = False, needs_extract: bool = False, frontier_after: int = 0):
        super().__init__(llm, budget)
        self.summary_budget = summary_budget or max(600, int(budget * summary_frac))
        self.flow = flow
        self.narrate = narrate and llm is not None
        self.use_llm = use_llm and llm is not None    # legacy v2 intent layer (refine.py); off in the main method
        self.hide_sections = tuple(hide_sections)
        self.det_needs = det_needs
        self.adapter = adapter
        self._graphs: dict[str, dict] = {}
        self.last_extra: dict | None = None
        self.proj = proj      # field-wise value projection + fill-to-budget
        self.mem = mem        # +ExternalMemory: externalize full observations into the session (_mem)
        self.last_setup_code: str | None = None
        self.narrative = narrative and llm is not None   # requirement-state note above the evidence layer
        self.narrative_tokens = narrative_tokens
        self.nar_prompts = nar_prompts
        self.frontier_mode = frontier and llm is not None
        # plan state costs a decompose + ops call and note budget at every boundary; on short
        # episodes that never pays for itself, so it can be switched on only once the episode
        # has already survived ``frontier_after`` compactions
        self.frontier_after = frontier_after
        self.needs_extract = needs_extract

    def compress(self, task: str, prev_summary: str | None, turns: list[dict]) -> str:
        key = _h(prev_summary)
        if prev_summary and key in self._graphs:
            g = Graph.from_dict(self._graphs[key])
            rebuilt = False
        else:
            g = Graph(task)
            g.call_prefix = "apis." if self.adapter == "codeact" else ""
            # externalization / projection need the raw observation after Apply; the bounded main
            # method does not, and holds the private graph under B_G = GRAPH_BUDGET_CHARS
            g.obs_keep = 0 if (self.mem or self.proj) else OBS_KEEP_CHARS
            g.graph_budget = 0 if (self.mem or self.proj) else GRAPH_BUDGET_CHARS
            g.legacy_summary = prev_summary
            rebuilt = prev_summary is not None
        rg = (ReqGraph.from_dict(g.req_graph)
              if (self.frontier_mode and len(g.bytes_log) >= self.frontier_after) else None)
        req_tree = rg.render() if rg is not None else ""
        if self.needs_extract and rg is not None:
            g.extract_specs = [f for spec in rg.frontier_needs() for f in spec["fields"]]
        # --- Q_k, G_k: bounded extraction and Apply -------------------------------------------
        new_ids = []
        for t in clip_turns(turns):
            if f"s{t['step']}" in g.steps:
                continue
            s = g.add_turn(t, self.adapter)
            new_ids.append(s["id"])
        new_turns = [t for t in clip_turns(turns) if f"s{t['step']}" in new_ids]
        stats: dict = {}
        if self.use_llm and new_ids:
            try:
                stats = refine_graph(g, new_ids, self.llm)
            except Exception as e:  # noqa: BLE001
                stats = {"error": str(e)[:200]}
                g.log.append({"drop": "refine_call_failed", "err": str(e)[:200]})
        if self.det_needs:
            g.augment_needs(new_ids[-3:])
        # --- optional requirement frontier (v4 line) ------------------------------------------
        req_stats: dict = {}
        if rg is not None and new_ids:
            try:
                req_stats = frontier_update(rg, task, g, self.llm, new_turns)
            except Exception as e:  # noqa: BLE001
                req_stats = {"error": str(e)[:200]}
                g.log.append({"drop": "frontier_update_failed", "err": str(e)[:200]})
            g.req_graph = rg.to_dict()
            g.protect_steps = {e for n in rg.frontier() for e in n["evidence"]} | \
                              {e for n in rg.frontier() for a in rg.ancestors(n) for e in a["evidence"]}
            g.protect_infos = set(rg.needed_infos(g.infos))
            req_tree = rg.render()
        # --- N_k: requirement-state note, verified against the graph -------------------------
        note_tokens = 0
        if self.narrative and new_ids:
            try:
                g.narrative = progress_note(self.llm, task, g.narrative, new_turns,
                                            self.narrative_tokens, self.nar_prompts)
            except Exception as e:  # noqa: BLE001
                g.log.append({"drop": "narrative_call_failed", "err": str(e)[:200]})
            if g.narrative and self.nar_prompts == "progress5":
                g.narrative, ng = ground_note(g.narrative, g)
                stats["note_downgraded"] = ng
                # V^requirement: the note's clauses become nodes with SUPPORTS edges to the cited
                # steps; the rendered requirement section is regenerated from the nodes
                g.requirements = parse_requirements(g.narrative, g)
                g.narrative = splice_requirements(g.narrative, g.requirements)
            note_tokens = count_tokens(g.narrative or "")
        budget_stats = g.enforce_budget()
        self.last_setup_code = None
        if self.mem:
            saved = {sid: g.steps[sid]["observation"] for sid in new_ids if worth_saving(g.steps[sid])}
            if saved:
                g.mem_keys.extend(k for k in saved if k not in g.mem_keys)
                self.last_setup_code = mem_setup_code(saved)
        # --- C_k: render to budget ------------------------------------------------------------
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
            # the requirement graph renders the requirement section; the note keeps its
            # handled / not-yet-done / next-steps content
            head = req_tree.strip()
            if g.narrative:
                body = strip_requirements(g.narrative) if head else g.narrative.strip()
                head = (head + "\n\n" + body) if (head and body) else (head or body)
            if head:
                note_tokens = count_tokens(head)
            text, level = render_to_budget(g, max(400, self.summary_budget - note_tokens), new_ids[-3:],
                                           proj=self.proj, fill=self.proj)
            if head:
                text = ("PROGRESS NOTE (written at the last compaction; advisory -- before completing the task, "
                        "check its remaining items against the exact evidence below"
                        + ("; do only what the task asks -- no extra modifications, and pass an answer to "
                           "complete_task only if the task asks for one"
                           if (rg is not None or self.nar_prompts in ("progress4", "progress5")) else "")
                        + ")\n") + head + "\n\n" + text
        degraded = False
        if level == 4 and self.llm is not None and self.use_llm:
            user = Template(load_prompt("openclaw_first.jinja")).render(history=text)
            try:
                text = self.llm.chat([{"role": "system", "content": load_prompt("openclaw_system.jinja")},
                                     {"role": "user", "content": user}], tag="fallback").strip()
                text += "\n\n" + live_variable_line(g)
                degraded = True
            except Exception:  # noqa: BLE001, S110
                pass
        if self.hide_sections:
            text = _drop_sections(text, self.hide_sections)
        self._graphs[_h(text)] = g.to_dict()
        self.last_extra = {"level": level, "degraded": degraded, "rebuilt_from_legacy": rebuilt,
                           "n_steps": len(g.steps), "n_intents": len(g.intents), "n_infos": len(g.infos),
                           "n_facts": len(g.facts), "summary_tokens": count_tokens(text),
                           "attached": attached, "pruned_steps": pruned,
                           "refine": stats, "drops": g.log[-10:],
                           "graph_bytes": budget_stats["after"], "graph_evicted": budget_stats["evicted"],
                           "n_requirements": len(g.requirements),
                           "req": req_stats, "frontier": (len(rg.frontier()) if rg is not None else None),
                           "protected": [len(g.protect_steps), len(g.protect_infos)]}
        return text

    def render_context(self, summary: str) -> str:
        head = ("\n\n<history_summary>\nThe conversation so far was compacted into this plan-graph checkpoint. "
                "Variables listed as LIVE are still defined in the Python session.\n")
        if self.mem:
            head += ("Results marked _mem['sN'] are saved in the Python session as parsed objects (list/dict or text): "
                     "use them directly instead of calling the API again.\n")
        return head + f"{summary}\n</history_summary>\n\n"


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


# evidence layer only (no v2 intent layer) + the verified requirement-state note
_MAIN = {"use_llm": False, "narrative": True, "nar_prompts": "progress5", "narrative_tokens": 450}

VARIANTS: dict[str, dict] = {
    # ---- main method: bounded evidence-grounded requirement-state compaction -------------------
    "compass_det_nar5": dict(_MAIN),

    # ---- ablations of the main method ----------------------------------------------------------
    "compass_det": {"use_llm": False},                                    # evidence layer only, no note
    "compass_det_nar4": {**_MAIN, "nar_prompts": "progress4", "narrative_tokens": 420},  # note grounded by prompt only
    "compass_det_nar3": {**_MAIN, "nar_prompts": "progress3", "narrative_tokens": 420},  # note without requirement list
    "compass_det_nar2": {**_MAIN, "nar_prompts": "progress2", "narrative_tokens": 350},  # note with a constraints section (rejected)
    "compass_det_nar": {"use_llm": False, "narrative": True},             # first OpenClaw-style note (done/next)
    "compass_wide": {"summary_frac": 0.6},                                # larger handover budget

    # ---- variants ------------------------------------------------------------------------------
    "compass_det_mem_nar5": {**_MAIN, "mem": True},                       # +ExternalMemory (session holds observations)
    "compass_frontier": {**_MAIN, "frontier": True},                      # + executable requirement frontier
    "compass_frontier_ex": {**_MAIN, "frontier": True, "needs_extract": True},  # + needs-conditioned field extraction
    "compass_frontier_late": {**_MAIN, "frontier": True, "frontier_after": 2},  # frontier only after 2 compactions
    "compass_frontier_noteless": {"use_llm": False, "frontier": True},    # first wiring: tree replaced the note
    "compass_generic": {"adapter": "generic"},                            # adapter tiers (Generic <= Schema <= CodeAct)
    "compass_schema": {"adapter": "schema"},
    "compass_codeaware": {},

    # ---- legacy: v2 (LLM intent layer) and v3 (flow graph / projection / externalization) lines;
    #      negative results, kept so the recorded artifacts stay reproducible -------------------
    "compass_v2": {},
    "compass_nospec": {"hide_sections": ("API DOCS ALREADY READ",)},
    "compass_novars": {"hide_sections": ("LIVE VARIABLES",)},
    "compass_nodone": {"hide_sections": ("CALL FORMS THAT", "API DOCS ALREADY READ", "RESULTS ALREADY")},
    "compass_noplan": {"hide_sections": ("PLAN (", "NEXT", "CONSTRAINTS", "FACTS")},
    "compass_llmneeds": {"det_needs": False},
    "compass_v3": {"flow": True},
    "compass_v3_det": {"flow": True, "use_llm": False},
    "compass_v3_nl": {"flow": True, "narrate": True},
    "compass_proj": {"proj": True},
    "compass_mem": {"mem": True},
    "compass_pm": {"proj": True, "mem": True},
    "compass_det_proj": {"use_llm": False, "proj": True},
    "compass_det_mem": {"use_llm": False, "mem": True},
    "compass_det_pm": {"use_llm": False, "proj": True, "mem": True},
    "compass_det_mem_nar": {"use_llm": False, "mem": True, "narrative": True},
    "compass_det_mem_nar2": {**_MAIN, "mem": True, "nar_prompts": "progress2", "narrative_tokens": 350},
    "compass_det_mem_nar3": {**_MAIN, "mem": True, "nar_prompts": "progress3", "narrative_tokens": 420},
    "compass_det_mem_nar4": {**_MAIN, "mem": True, "nar_prompts": "progress4", "narrative_tokens": 420},
}


def make_compass(method: str, llm: LLM, budget: int) -> CompassCompressor:
    if method not in VARIANTS:
        raise ValueError(f"unknown compass variant {method}; known: {sorted(VARIANTS)}")
    kw = dict(VARIANTS[method])
    # the model is always passed: use_llm only governs the intent/plan layer; the narrative and the
    # level-4 fallback check their own switches
    c = CompassCompressor(llm, budget, **kw)
    c.name = method
    return c
