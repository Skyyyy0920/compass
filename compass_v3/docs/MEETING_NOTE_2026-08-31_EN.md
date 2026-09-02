# COMPASS — progress report, 2026-08-31

Previous report: 2026-08-26. This week's work was to **converge the method into a protocol that survives scrutiny** — three review rounds from the senior collaborator, each of which changed something substantive — and to re-run every experiment at a reportable standard. All runs use open-weight models served by Ollama Cloud (DeepSeek-V4-Flash unless stated), AppWorld `test_normal`, window B = 4096, last turn preserved, 50-step cap; OfficeBench uses its 95 non-image test episodes. Code and all artifacts are in the repository (§8).

---

## 1. Headline

**Under a strict bounded protocol — after compaction the agent sees only a checkpoint of at most 0.4·B plus the last raw turn — compaction at a 4096-token window no longer costs task success: AppWorld-168 scores 80.4 / 81.5 = 81.0 over two runs, matching full context at 81.0, and beats natural-language compaction (OpenClaw) by +6.3 ± 2.7 paired per task.** Claims are scoped to CodeAct-style / structure-rich tool-use agents.

---

## 2. The method, as it now stands: evidence-grounded requirement-state compaction

Every compaction boundary does three things and emits exactly one artifact, the checkpoint — there is no environment-side memory channel:

```
Q_k = Extract_α(Δτ_k)                      # adapter extracts bounded events; the raw observation is then destroyed
G_k = Apply(G_{k-1}, Q_k),  size(G_k) ≤ B_G    # private graph updated incrementally under a byte budget
N_k = Verify_G(Note_φ(N_{k-1}, Q_k, u))    # one LLM call writes the requirement-state note; the graph then verifies it
C_k = Render_B(N_k, Fold(G_k | N_k))       # |C_k| ≤ 0.4·B
```

1. **Deterministic evidence layer** (no LLM): call forms with the `apis.` prefix, API signatures and per-app API listings, live variables with provenance, and observed results deduplicated by call signature. Ablations put essentially all of the gain here (removing it: boundary +1.02\*).
2. **Bounded private state**: after Apply only a 600-character observation excerpt survives; the parsed observation and the full text are dropped. The serialized graph is held under B_G = 64k characters, evicting oldest evidence first. Measured over 914 boundaries: mean 37.5k, p95 65k, 99 boundaries evicted — **with no loss in performance**.
3. **Requirement-state layer**: the instruction is decomposed into requirement nodes quoting verbatim spans (checked), optionally with an expected count. A status must cite the evidence steps supporting it, and the compressor verifies that those steps exist and succeeded, otherwise it is rewritten as NOT DONE (unverified) — so `DONE(c) ⇒ ∃e ∈ G_k: SUPPORTS(e, c) ∧ outcome(e) = ok` holds by construction. Two behavioural rules ride along: do only what the task asks, and pass an answer to `complete_task` only when one is requested.

---

## 3. Main results

### 3.1 AppWorld `test_normal`, 168 tasks

| Method | Runs | Mean | long-52 / other-116 | Pass² | Paired |
|---|---|---|---|---|---|
| Full context | 81.0 / 81.0 | 81.0 | 69.2 / 86.2 | 74.4 | – |
| OpenClaw | 69.0 / 78.0 / 76.8 | 74.6 ± 2.8 | 59.0 / 81.6 | 55.4 (P³) | – |
| **COMPASS (main)** | **80.4 / 81.5** | **81.0** | 68.3 / 86.6 | 73.2 | vs OpenClaw **+6.3 ± 2.7**; vs full +0.0 ± 2.9 |
| Hermes | 70.8 | | | | |
| ACON-UT | 66.7 | | | | |
| FIFO | 49.4 | | | | |
| COMPASS v2 (one week ago) | 65.5 | | 38.5 / 77.6 | | |

Repeat runs of the same configuration move by up to nine points (OpenClaw 69 → 78), so every comparison is reported as a multi-run mean ± SE plus a per-task paired difference.

### 3.2 Boundary level (Trace protocol, 109 boundaries, paired Δ@5 vs OpenClaw; negative = fewer blocked/repeated actions)

Main method **−0.56\***; the deterministic evidence layer alone −0.38\*; COMPASS v2 −0.21; OpenClaw 0.

### 3.3 Other settings

- 30-task subset: main method 96.7 (full 83.3, OpenClaw 73.3) — note this subset varies by about ±13 points between runs.
- OfficeBench (no Python session, note channel only): 78.9 at B = 2048 (OpenClaw 74.7, v2 77.9) and 78.9 at B = 4096 (OpenClaw 82.1).
- Budget sweep (30 tasks, OpenClaw / COMPASS): 66.7 / 66.7 at 2048, 73.3 / 83.3 at 4096, 86.7 / 86.7 at 8192 — the advantage sits at the middle budget.

---

## 4. The three review rounds and what we did

| Round | Objection | Response | Evidence |
|---|---|---|---|
| 1 | `_mem` (externalizing full observations into the agent's Python session) changes the environment transition and the baseline had no such interface, so it cannot be reported as context compression | Removed from the main method, kept as the `+ExternalMemory` variant; added `openclaw_mem` as a fairness control | bounded 81.5 ≥ +ExtMem 80.7; giving OpenClaw the same interface buys only +2.2 ± 2.9 (n.s.) → **the gain does not come from external memory** |
| 2 | The private graph had no budget and still held raw observations; "grounded" was a prompt instruction, not a guarantee; this is no longer graph planning and the claim is too broad | Added B_G and physical deletion; statuses are now verified programmatically; formalized as a requirement graph; claims scoped to CodeAct | Adding the budget left performance unchanged (81.0); the verified variant scores −0.56\* at boundary level |
| 3 | There is planning but no closed loop: Next Steps were never compiled into a frontier and information was not attached to future needs | Built the requirement engine (one-time decomposition, four validated local operators, executable frontier, NEEDED_BY protection, needs-conditioned extraction) and ran the three-arm ablation | §5 |

---

## 5. The three-arm ablation (52 long tasks, same cohort, metrics beyond accuracy)

| Arm | acc | step-exhausted | premature completion | refetch/ep | boundary Δ@5 |
|---|---|---|---|---|---|
| (a) main method (frozen baseline, 2 runs) | **65.4 / 71.2** (68.3) | 9 / 9 | 10 / 7 | 5.1 / 4.8 | **−0.56\*** |
| (b) + executable frontier | 61.5 | 11 | 9 | 6.3 | −0.50\* |
| (b') + completion guard | 59.6 | 12 | 8 | 6.7 | – |
| **(c) + needs-conditioned field extraction** | **63.5** | 10 | 11 | 6.2 | – |
| requirement tree **replacing** the note (first wiring) | 55.8 | 19 | 3 | 7.9 | −0.31\* |
| OpenClaw (4 runs) | 55.3 ± 3.6 | – | – | – | 0 |

Reading:
1. The frontier machinery works on its own terms — against the first wiring it cuts step exhaustion 19 → 11, refetches 7.9 → 6.3, boundary burden −0.31 → −0.50, and lifts long tasks 55.8 → 63.5, **clearly above OpenClaw**.
2. **It does not beat the frozen baseline** (63.5 vs 68.3; −0.50 vs −0.56). The verified note already carries coverage counts and an explicit not-yet-done list, so most of what the frontier adds is information the agent already had, while it costs two extra LLM calls and part of the note budget at every boundary.
3. Arm (c) is the strongest piece of the frontier line: **letting the plan decide which fields to lift out of a large observation is genuinely useful** (61.5 → 63.5), landing within one task of the weaker baseline run.
4. The completion guard buys nothing (59.6 vs 61.5, one task): premature completion is not caused by the agent not knowing how much is left.
5. On short tasks the frontier is a net cost (30 tasks: 83.3 three times; gating it to switch on only after two compactions recovers 86.7).

---

## 6. Four real defects fixed this week (each with before/after numbers)

1. **Missing prefix in the rendering**: the checkpoint spelled calls as `venmo.login(...)`, the agent copied them, and 73 post-compaction `NameError: name 'venmo'` followed; with the `apis.` prefix, **zero**.
2. **Variant wiring**: the frontier arm omitted the narrative flag and therefore shipped the tree *instead of* the note — long tasks 55.8, boundary −0.31; after the fix 61.5 / −0.50.
3. **Stale requirement tree**: statuses only advance at boundaries, so on short tasks the tree stayed at NOT_STARTED and contradicted the trajectory. Statuses now render as a monotone lower bound ("at least N of M confirmed done").
4. **Budget eviction was O(n²)**: `enforce_budget` serialized the whole graph for every candidate — 5.7 s per boundary with field extraction, and it still ended 50% over budget (101k vs 65k), which stalled one long-task run for 50 minutes with zero output. Eviction now works against a calibrated size estimate and can drop the oldest unprotected results: **0.03 s per boundary, graph held at 65.6k**.

---

## 7. Negative results (all paired experiments; not worth retrying)

The v3 flow graph that attached information to plan nodes (best −0.04, n.s.); narrating the structured checkpoint in natural language (+0.30); field-wise projection implemented as "more fields" (longer lines, coarser folding); the structured LLM plan layer (boundary +0.25, no task-level gain); ungrounded Done lists (premature completion on short tasks); letting the model write a constraints section (it imports inferences such as "presumably…"; 30 tasks 70.0); the completion guard; the requirement tree replacing the note.

---

## 8. Code and documents

- Draft PR: `GuanghuiMin/compass` #2 (`Skyyyy0920:compass-v3-pr` → `main`; all code under `compass_v3/`, the v1 files untouched)
- Full history branch: `compass-v3-requirement-state` on `Skyyyy0920/compass`
- Reading order: `compass_v3/README.md` → `docs/METHOD_v3.2_requirement_state_compaction.md` (method, full results, responses to all three review rounds; §7 is the frontier ablation) → `docs/PLAN.md` (§3.5–3.17, §4.1–4.8: the whole trajectory including negative results)
- 17 unit tests; `scripts/report_ablation.py` reports the metrics beyond accuracy (open requirements at completion, duplicated side effects, premature completion, post-compaction refetch/blocked, graph and context size)

---

## 9. Next steps (priorities to decide)

1. **The one untested lever**: use `NEEDED_BY` as a *deletion* criterion — drop the evidence the frontier does not need — rather than only for protection and ordering. Arm (c)'s positive signal says the "plan decides what to keep" link is real, and deletion is its last step.
2. **Cost accounting**: the frontier spends two extra LLM calls per boundary (about six boundaries per long task, so twelve calls); at present the benefit does not cover the cost, and the paper's accounting must say so.
3. **Fill in the cross-model evidence**: GLM-5.2 and Kimi currently only have `+ExternalMemory` numbers; the bounded main method still needs to be run there, as does the verified variant on OfficeBench.
4. **Paper**: §4 and §5b on Overleaf still describe the `_mem` version and need rewriting into the bounded framing (the red additions are pushed to `main`, but those two sections must change).
5. **External comparison**: connect BCG (belief/confidence-based context) to the same AppWorld agent, or at least run a BCG-style ablation, against frontier-conditioned selection.
6. **GPT runs**: not started; per the standing rule the budget needs approval first (OpenClaw vs the main method, 168 tasks × 2 each, roughly $250–300).
