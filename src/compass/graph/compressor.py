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
import re

from jinja2 import Template

from ..harness.compressors import Compressor, clip_turns, turns_to_text
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
                 narrate: bool = False, proj: bool = False, mem: bool = False,
                 narrative: bool = False, narrative_tokens: int = 450, nar_prompts: str = "progress"):
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
        self.proj = proj      # field-wise value projection + fill-to-budget
        self.mem = mem        # externalize full observations into the session (_mem) and cite the keys
        self.last_setup_code: str | None = None
        self.narrative = narrative and llm is not None   # OpenClaw-style progress note above the evidence layer
        self.narrative_tokens = narrative_tokens
        self.nar_prompts = nar_prompts

    def compress(self, task: str, prev_summary: str | None, turns: list[dict]) -> str:
        key = _h(prev_summary)
        if prev_summary and key in self._graphs:
            g = Graph.from_dict(self._graphs[key])
            rebuilt = False
        else:
            g = Graph(task)
            g.call_prefix = "apis." if self.adapter == "codeact" else ""
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
        note_tokens = 0
        if self.narrative and new_ids:
            try:
                g.narrative = progress_note(self.llm, task, g.narrative, [t for t in clip_turns(turns)
                                                                       if f"s{t['step']}" in new_ids],
                                            self.narrative_tokens, self.nar_prompts)
            except Exception as e:  # noqa: BLE001
                g.log.append({"drop": "narrative_call_failed", "err": str(e)[:200]})
            if g.narrative and self.nar_prompts == "progress5":
                g.narrative, ng = ground_note(g.narrative, g)
                stats["note_downgraded"] = ng
            note_tokens = count_tokens(g.narrative or "")
        self.last_setup_code = None
        if self.mem:
            saved = {sid: g.steps[sid]["observation"] for sid in new_ids if _worth_saving(g.steps[sid])}
            if saved:
                g.mem_keys.extend(k for k in saved if k not in g.mem_keys)
                self.last_setup_code = mem_setup_code(saved)
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
            text, level = render_to_budget(g, max(400, self.summary_budget - note_tokens), new_ids[-3:],
                                           proj=self.proj, fill=self.proj)
            if g.narrative:
                text = ("PROGRESS NOTE (written at the last compaction; advisory -- before completing the task, "
                        "check its remaining items against the exact evidence below"
                        + ("; do only what the task asks -- no extra modifications, and pass an answer to "
                           "complete_task only if the task asks for one" if self.nar_prompts in ("progress4", "progress5") else "")
                        + ")\n") + g.narrative.strip() + "\n\n" + text
        degraded = False
        if level == 4 and self.llm is not None and self.use_llm:
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
        head = ("\n\n<history_summary>\nThe conversation so far was compacted into this plan-graph checkpoint. "
                "Variables listed as LIVE are still defined in the Python session.\n")
        if self.mem:
            head += ("Results marked _mem['sN'] are saved in the Python session as parsed objects (list/dict or text): "
                     "use them directly instead of calling the API again.\n")
        return head + f"{summary}\n</history_summary>\n\n"



def progress_note(llm: LLM, task: str, prev: str | None, turns: list[dict], max_tokens: int,
                  prompts: str = "progress") -> str:
    """OpenClaw-style progress note (done / in progress / blocked / decisions / next), incrementally
    updated; the evidence layer is rendered separately, so the note is told not to repeat values."""
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


STEP_ID_RE = re.compile(r"\bs\d+\b")
STATUS_RE = re.compile(r"(?<!NOT )(?<!NOT_)\b(DONE|PARTIAL)\b")


def ground_note(note: str, g) -> tuple[str, int]:
    """Requirement-state grounding by construction: a DONE / PARTIAL status survives only if the
    line cites step ids that exist in the graph and executed without error; otherwise the status
    is rewritten as NOT DONE (unverified). Returns the note and the number of downgraded lines."""
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


def _worth_saving(step: dict) -> bool:
    obs = (step.get("observation") or "").strip()
    return bool(step.get("api_names")) and step.get("status") == "ok" and len(obs) > 40 \
        and obs != "Execution successful."


def mem_value(obs: str, limit: int = 20000):
    from compass.graph.project import parse
    obj = parse(obs) if len(obs) <= limit else None
    return obj if obj is not None else obs[:limit]


def mem_setup_code(saved: dict[str, str], limit: int = 20000) -> str:
    """Code executed in the agent's Python session at the boundary: it stores the full observations
    of the absorbed steps under their step ids. Nothing is sent to the model; the checkpoint only
    cites the keys."""
    # JSON observations are stored parsed (list/dict), so the agent can index them the way it
    # indexes an API result; anything else is stored as the text that was printed
    items = ", ".join(f"{k!r}: {mem_value(v, limit)!r}" for k, v in saved.items())
    return "try:\n    _mem\nexcept NameError:\n    _mem = {}\n_mem.update({" + items + "})"


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
    # beyond v3: keep fields not characters (proj), and let the session hold the full observations (mem)
    "compass_proj": {"proj": True},
    "compass_mem": {"mem": True},
    "compass_pm": {"proj": True, "mem": True},
    "compass_det_proj": {"use_llm": False, "proj": True},
    "compass_det_mem": {"use_llm": False, "mem": True},
    "compass_det_pm": {"use_llm": False, "proj": True, "mem": True},
    # progress narrative (OpenClaw-style done/in-progress/next) on top of the evidence layer
    "compass_det_nar": {"use_llm": False, "narrative": True},
    "compass_det_mem_nar": {"use_llm": False, "mem": True, "narrative": True},
    "compass_det_mem_nar2": {"use_llm": False, "mem": True, "narrative": True, "nar_prompts": "progress2",
                             "narrative_tokens": 350},
    "compass_det_nar2": {"use_llm": False, "narrative": True, "nar_prompts": "progress2", "narrative_tokens": 350},
    "compass_det_mem_nar4": {"use_llm": False, "mem": True, "narrative": True, "nar_prompts": "progress4",
                             "narrative_tokens": 420},
    "compass_det_nar4": {"use_llm": False, "narrative": True, "nar_prompts": "progress4", "narrative_tokens": 420},
    "compass_det_nar5": {"use_llm": False, "narrative": True, "nar_prompts": "progress5", "narrative_tokens": 450},
    "compass_det_mem_nar5": {"use_llm": False, "mem": True, "narrative": True, "nar_prompts": "progress5",
                             "narrative_tokens": 450},
    "compass_det_mem_nar3": {"use_llm": False, "mem": True, "narrative": True, "nar_prompts": "progress3",
                             "narrative_tokens": 420},
    "compass_det_nar3": {"use_llm": False, "narrative": True, "nar_prompts": "progress3", "narrative_tokens": 420},
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
