# COMPASS 进度汇报（2026-08-31）

上一次汇报 2026-08-26。这一周的主线是：**把方法收敛成一个可辩护的协议**（经过师兄三轮评审，每一轮都改了实质内容），并把所有实验重跑到可报告的口径。全部实验用开源模型（Ollama Cloud，deepseek-v4-flash 为主），AppWorld test_normal，窗口 B=4096，保留最后一轮，50 步上限；OfficeBench 95 个非图像 episode。代码与全部产物已推到仓库（见 §8）。

---

## 1. 一句话结论

**在严格的 bounded 协议下（压缩后 agent 只能看到 ≤0.4·B 的 checkpoint 和最后一轮原文），COMPASS 让 4096 窗口的压缩不再损失任务成功率：AppWorld-168 两次 80.4 / 81.5 = 81.0，与 full context 的 81.0 持平，逐题配对显著优于自然语言压缩 OpenClaw（+6.3 ± 2.7）。** 主张范围限定为 CodeAct / 结构丰富的 tool-use agent。

---

## 2. 方法定稿：evidence-grounded requirement-state compaction

每个压缩边界做三件事，产物只有一个 checkpoint（没有环境侧记忆通道）：

```
Q_k = Extract_α(Δτ_k)                     # adapter 确定性提取有界事件；原始 observation 随后销毁
G_k = Apply(G_{k-1}, Q_k),  size(G_k) ≤ B_G   # 私有图增量更新，受字节预算约束
N_k = Verify_G(Note_φ(N_{k-1}, Q_k, u))   # 一次 LLM 调用写需求状态笔记，再由图核验
C_k = Render_B(N_k, Fold(G_k | N_k))      # |C_k| ≤ 0.4·B
```

1. **确定性证据层**（无 LLM）：调用形式（带 `apis.` 前缀）、API 签名与应用 API 名单、活变量与来源、按调用签名去重的结果摘录。消融显示收益几乎全在这一层（去掉 → boundary +1.02\*）。
2. **有界私有状态**：Apply 之后只保留 600 字符观测摘录，解析结果与原文全部丢弃；序列化图受 B_G = 64k 字符约束，超出按最旧证据逐级驱逐。实测 914 个边界：均值 37.5k、p95 65k，99 个边界发生驱逐，**性能不变**。
3. **需求状态层**：任务指令逐字拆成 requirement 节点（span 校验、可带 expect 计数），状态必须引用支持它的证据步骤，压缩器核验"该步骤存在且执行成功"，否则降级为 NOT DONE (unverified)——`DONE(c) ⇒ ∃e∈G_k: SUPPORTS(e,c) ∧ outcome(e)=ok` 由构造保证。另有两条行为规则：只做任务要求的事；任务没要答案就不要传 `answer`。

---

## 3. 主结果

### 3.1 AppWorld test_normal 168 题

| 方法 | 各次 Acc | 均值 | 长 52 / 其余 116 | Pass² | 逐题配对 |
|---|---|---|---|---|---|
| Full context | 81.0 / 81.0 | 81.0 | 69.2 / 86.2 | 74.4 | – |
| OpenClaw | 69.0 / 78.0 / 76.8 | 74.6 ± 2.8 | 59.0 / 81.6 | 55.4（P³） | – |
| **COMPASS（主方法）** | **80.4 / 81.5** | **81.0** | 68.3 / 86.6 | 73.2 | vs OpenClaw **+6.3 ± 2.7**；vs full +0.0 ± 2.9 |
| Hermes | 70.8 | | | | |
| ACON-UT | 66.7 | | | | |
| FIFO | 49.4 | | | | |
| COMPASS v2（一周前） | 65.5 | | 38.5 / 77.6 | | |

同配置重复运行波动可达 9 点（OpenClaw 69→78），所有对比一律用多次均值 ± SE 与逐题配对。

### 3.2 Boundary 级（Trace 协议，109 边界，配对 Δ@k5 vs OpenClaw，负=更少阻塞/重取）

主方法 **−0.56\***；去掉需求笔记的纯证据层 −0.38\*；COMPASS v2 −0.21；OpenClaw 0。

### 3.3 其他设置

- 30 题：主方法 96.7（full 83.3、OpenClaw 73.3）——注意该子集运行间方差约 ±13 点。
- OfficeBench（无 Python 会话，只用笔记通道）：@2048 **78.9**（OpenClaw 74.7、v2 77.9）、@4096 78.9（OpenClaw 82.1）。
- 预算扫描（30 题）：B=2048 66.7/66.7，B=4096 73.3/83.3，B=8192 86.7/86.7——优势集中在中等预算。

---

## 4. 三轮评审与我们的处理

| 轮次 | 评审意见 | 处理 | 证据 |
|---|---|---|---|
| 一 | `_mem`（把完整 observation 外置到 agent 的 Python 会话）改变了环境转移，baseline 没有同样接口，不能算 context compression | 从主方法移除，降为变体 `+ExternalMemory`；补 `openclaw_mem` 公平对照 | bounded 81.5 ≥ +ExtMem 80.7；给 OpenClaw 同样接口只 +2.2 ± 2.9（不显著）→ **增益不来自外部记忆** |
| 二 | 私有图没有预算、原始 observation 实际仍在图里；"grounded"只是 prompt 指令；已经不是 graph planning，claim 也过宽 | 加 B_G 预算与物理删除；状态改为程序核验；形式化为 requirement graph；claim 限定 CodeAct | 加预算后性能不变（81.0）；核验版 boundary −0.56\* |
| 三 | 有 planning 但没有闭环：Next Steps 没有编译成 frontier，信息没有按未来需求挂载 | 实现 requirement 引擎（一次性分解 + 四个受校验的局部算子 + 可执行 frontier + NEEDED_BY 保护 + 按需字段提取），做三臂配对消融 | 见 §5 |

---

## 5. 第三轮的三臂消融（52 长任务，同 cohort，指标不止 accuracy）

| 臂 | acc | 跑满 50 步 | 提前完成 | refetch/题 | boundary Δ@k5 |
|---|---|---|---|---|---|
| (a) 主方法（冻结基线，2 次） | **65.4 / 71.2**（68.3） | 9 / 9 | 10 / 7 | 5.1 / 4.8 | **−0.56\*** |
| (b) + 可执行 frontier | 61.5 | 11 | 9 | 6.3 | −0.50\* |
| (b') + 完成守卫 | 59.6 | 12 | 8 | 6.7 | – |
| **(c) + 需求条件化字段提取** | **63.5** | 10 | 11 | 6.2 | – |
| 需求树**替代**笔记（第一版接线） | 55.8 | 19 | 3 | 7.9 | −0.31\* |
| OpenClaw（4 次） | 55.3 ± 3.6 | – | – | – | 0 |

**结论**：
1. frontier 机制本身有效——相对"树替代笔记"的第一版，步数耗尽 19→11、refetch 7.9→6.3、boundary −0.31→−0.50、长任务 55.8→63.5，**明显高于 OpenClaw**。
2. **但没有超过冻结基线**（63.5 vs 68.3；boundary −0.50 vs −0.56）。原因是主方法的已核验笔记本身就带覆盖计数与未完成清单，frontier 想补的信息大部分已在其中，而它每个边界要多花两次 LLM 调用与一部分笔记预算。
3. arm (c) 是 frontier 里最强的一环：**用 plan 决定从大 observation 提升哪些字段确有价值**（61.5→63.5），与基线较差那次仅差 1 题。
4. 完成守卫无增益（59.6 vs 61.5，一题之差）：agent 提前完成不是因为"不知道还差多少"。
5. 短任务上 frontier 是净成本（30 题 83.3×3；改成"两次压缩后才启用"回到 86.7）。

---

## 6. 本周修掉的四个真实缺陷（都有前后数据）

1. **渲染缺前缀**：checkpoint 把调用写成 `venmo.login(...)`，agent 照抄 → 压缩后 73 次 `NameError: name 'venmo'`；加 `apis.` 前缀后 **0 次**。
2. **变体接线错误**：frontier 臂漏了 narrative 开关，跑成"树替代笔记"而非叠加 → 长任务 55.8、boundary −0.31；修正后 61.5 / −0.50。
3. **需求树滞后**：状态只在边界更新，短任务里永远停在 NOT_STARTED 且与轨迹矛盾 → 改为单调下界语义（只声明"至少已确认完成什么"）。
4. **预算驱逐 O(n²)**：`enforce_budget` 每个候选都整图 JSON 序列化，字段提取模式下 5.7s/边界且降不到预算（101k > 65k），导致一个长任务实验 50 分钟零产出 → 改为按估算逐级驱逐 + 末级丢弃最旧未保护结果：**0.03s/边界，稳定在 65.6k**。

---

## 7. 明确的负结果（都做过配对实验，不再重试）

v3 流程图（信息挂到计划节点，最好 −0.04 n.s.）；结构化 checkpoint 的自然语言改写（+0.30）；字段级投影按"更多字段"实现（行变长、折叠更粗）；结构化 LLM 计划层（boundary +0.25，任务级无增益）；未 grounding 的 Done 列表（短任务提前完成）；让模型写"约束栏"（写入 "presumably…" 之类推断，30 题 70.0）；完成守卫；需求树替代笔记。

---

## 8. 代码与文档

- Draft PR：`GuanghuiMin/compass` #2（`Skyyyy0920:compass-v3-pr` → `main`，全部代码在 `compass_v3/` 子目录，v1 文件未动）
- 完整历史分支：`Skyyyy0920/compass` 的 `compass-v3-requirement-state`
- 阅读顺序：`compass_v3/README.md` → `docs/METHOD_v3.2_requirement_state_compaction.md`（方法 + 完整结果 + 三轮评审回应，§7 是 frontier 消融）→ `docs/PLAN.md`（§3.5–3.17、§4.1–4.8 全过程与负结果）
- 单测 17 项；`scripts/report_ablation.py` 输出 accuracy 之外的指标（遗漏需求、重复副作用、提前完成、压缩后 refetch/blocked、图与上下文大小）

---

## 9. 下一步（需要决定优先级）

1. **唯一未验证的关键杠杆**：把 `NEEDED_BY` 用作**删除**准则（frontier 不需要的证据直接丢弃），目前它只用于保护与排序。arm (c) 的正向信号说明"plan 决定保留什么"这条链条有效，删除准则是它最后一步。
2. **成本核算**：frontier 每边界多两次 LLM 调用（长任务约 6 次边界 = 12 次），当前收益不抵成本，需纳入论文口径。
3. **补齐跨模型**：glm-5.2 / kimi 上目前只有 +ExternalMemory 变体的数字，bounded 主方法待跑；OfficeBench 的核验版待跑。
4. **论文**：Overleaf §4/§5b 仍是 `_mem` 版本的表述，需要改成 bounded 框架（红色追加已推送到 `main`，但要重写这两节）。
5. **外部对照**：BCG（belief/confidence-based context）接到同一 AppWorld agent，或至少做 BCG-style 消融，与 frontier-conditioned 选择对比。
6. **GPT 实验**：尚未启动，按既定规则需要先确认预算（OpenClaw vs 主方法各 168 ×2，约 $250–300）。
