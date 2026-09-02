"""+ExternalMemory variant: hand the full observations of absorbed steps back to the agent's
Python session as ``_mem['sN']`` and let the checkpoint cite the keys.

This is *not* part of the bounded main method (it changes the environment transition and the
baselines have no such interface); it is kept as a variant, with ``openclaw_mem`` in
``harness/compressors.py`` as the fairness control that gives OpenClaw the same channel.
"""
from __future__ import annotations


def worth_saving(step: dict) -> bool:
    obs = (step.get("observation") or "").strip()
    return bool(step.get("api_names")) and step.get("status") == "ok" and len(obs) > 40 \
        and obs != "Execution successful."


def mem_value(obs: str, limit: int = 20000):
    from .project import parse
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
