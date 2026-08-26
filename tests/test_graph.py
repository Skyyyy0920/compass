"""Deterministic-layer tests: parsing, dataflow, grounding, rendering budget."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from compass.eval.signatures import canon, is_error, sigs  # noqa: E402
from compass.graph.build import Graph  # noqa: E402
from compass.graph.parse import defs_uses, error_class  # noqa: E402
from compass.graph.render import render_to_budget  # noqa: E402
from compass.harness.prompt import count_tokens  # noqa: E402

ERR = "Execution failed. Traceback:\n  File \"<python-input>\", line 1\nNameError: name 'tok' is not defined"


def test_sigs_canonical():
    assert sigs("apis.venmo.add_friend(user_email=e, access_token=t)") == ["venmo.add_friend(access_token=t,user_email=e)"]
    assert canon("b=2, a=1") == "a=1,b=2"
    assert is_error(ERR) and not is_error("[]")


def test_defs_uses_and_loop_vars():
    code = ("tok = apis.venmo.login(username=u, password=p)['access_token']\n"
            "for f in friends:\n    print(f, tok)\n"
            "def helper(x):\n    return x + tok\n")
    defs, uses, ok = defs_uses(code)
    assert ok
    assert defs == ["tok", "helper"]
    assert "f" not in defs and "f" not in uses
    assert set(uses) == {"u", "p", "friends"}


def test_extract_code_strips_model_markup():
    from compass.harness.episode import extract_code
    assert extract_code("\n\n<｜DSML｜python>\nprint(1)\n</｜DSML｜python>") == "print(1)"
    assert extract_code("```python\nx = 1\n```") == "x = 1"
    # ACON semantics: think *tags* are removed, their content is kept
    assert extract_code("<think>hmm</think>\nprint(2)") == "hmm\nprint(2)"


def test_error_class():
    assert error_class(ERR) == "name_error"
    assert error_class("No code available to execute.") == "no_code"
    assert error_class("[]") is None


def test_graph_dataflow_and_supersede():
    g = Graph("goal")
    g.add_turn({"step": 1, "code": "a = apis.x.y()\nprint(a)", "observation": "[1, 2]"})
    g.add_turn({"step": 2, "code": "b = len(a)", "observation": "Execution successful."})
    g.add_turn({"step": 3, "code": "a = 5", "observation": "Execution successful."})
    a1 = next(i for i in g.infos.values() if i.name == "a" and i.producer == "s1")
    assert a1.source_api == "x.y" and a1.consumers == ["s2"] and a1.superseded
    assert g.steps["s2"]["consumes"] == [a1.id]
    live = {i.name for i in g.live_infos()}
    assert "a" in live and "b" in live


def test_status_grounding():
    g = Graph("goal")
    g.add_turn({"step": 1, "code": "x = apis.a.b()", "observation": ERR})
    g.add_turn({"step": 2, "code": "x = apis.a.b()", "observation": "{\"ok\": true}"})
    it = g.add_intent("do the thing")
    assert g.set_status(it.id, "done", ["s1"]) and it.status == "active"      # no ok evidence -> downgraded
    assert g.set_status(it.id, "done", ["s2"]) and it.status == "done"
    assert g.set_status(it.id, "blocked", ["s2"]) and it.status == "active"   # no error evidence
    assert g.set_status(it.id, "blocked", ["s1"]) and it.status == "blocked"
    assert g.add_intent("child of missing", parent="c99") is None
    assert g.log[-1]["drop"] == "intent_parent_missing"


def test_fact_dedup_and_citation():
    g = Graph("goal")
    g.add_turn({"step": 1, "code": "print(1)", "observation": "1"})
    assert g.add_fact("Friends are contacts with relationship 'friend'.", "constraint") is None   # no citation
    assert g.add_fact("Friends are contacts with relationship 'friend'.", "constraint", ["s1"]) is not None
    assert g.add_fact("friends are contacts with relationship friend", "constraint", ["s1"]) is None  # duplicate
    assert len(g.facts) == 1


def test_adapter_tiers():
    turn = {"step": 1, "code": "tok = apis.venmo.login(username=u, password=p)\nprint(tok)",
            "observation": "Execution failed. Traceback:\n  x\nNameError: name 'u' is not defined"}
    g = Graph("goal")
    s = g.add_turn(turn, "generic")
    assert s["status"] == "unknown" and s["call_forms"] == [] and s["defs"] == []
    g2 = Graph("goal")
    s2 = g2.add_turn(turn, "schema")
    assert s2["status"] == "blocked" and s2["call_forms"] == ["venmo.login(username, password)"] and s2["defs"] == []
    g3 = Graph("goal")
    s3 = g3.add_turn(turn, "codeact")
    assert s3["defs"] == ["tok"] and set(s3["uses"]) == {"u", "p"}


def test_render_within_budget():
    g = Graph("Reset friends on venmo")
    big = "[" + ", ".join(f'{{"contact_id": {i}, "email": "u{i}@x.com"}}' for i in range(400)) + "]"
    for k in range(1, 30):
        g.add_turn({"step": k, "code": f"v{k} = apis.phone.search_contacts(page_index={k})\nprint(v{k})",
                    "observation": big})
    root = g.add_intent("sync friends")
    for k in range(1, 10):
        c = g.add_intent(f"sub {k}", parent=root.id)
        g.set_status(c.id, "done", [f"s{k}"])
    text, level = render_to_budget(g, 500, ["s29"])
    assert level in (1, 2, 3)
    if level < 3:
        assert count_tokens(text) <= 500
    assert "GOAL" in text and "PLAN" in text
