# 多空辩论模块与 AAPL 月度实验

本模块接入原有 TradingAgents 工作流，不使用先前的冻结报告实验入口。

## 开关与默认值

- 独立入口：`python -m agents.debate_agent`。
- 默认开启多轮，每方三次发言：多1 → 空1 → 多2 → 空2 → 多3 → 空3。
- `--no-multi-round` 关闭后，每方一次：多1 → 空1。即使同时传入 `--rounds 5`，关闭状态仍执行一轮。
- `--rounds N` 设置开启时的正整数轮数。
- 一轮是多空各发言一次，不是总共一次；三轮总计六次研究员发言。

第一位多头看分析师报告，不虚构尚未出现的空方意见。后续双方读取累计辩论历史和上一位对手观点。最后一位空头发言结束后，研究经理接收全部发言，随后仍由交易员、三类风险角色和组合经理完成原来的决策流程。没有新增评委，也不在第三轮之前提前终止。

只改变研究辩论轮数。技术、新闻、基本面分析师保留；情绪分析模块关闭；风险讨论固定一轮，即激进、保守、中性各一次。最终决策仍沿用原始评级及 BUY/SELL/HOLD 接口，不增加比例仓位或卖空。

该入口的显式设置覆盖旧环境变量中的研究/风险轮数，避免实验串组。未通过本入口或未向 `run_one` 传入 `debate_options` 的旧调用，保持原来行为。

## 离线预检（不会调用 API）

在项目根目录执行：

```bash
python -m agents.debate_agent --ticker AAPL --date 2026-09-01
python -m agents.debate_agent --ticker AAPL --date 2026-09-01 --no-multi-round
python -m pytest tests/test_debate_module.py -q
```

默认执行的是本地日期/数据预检，显示模块开关、实际配置轮数、预期发言数，不生成真实模型决策。离线工作流测试使用假模型，禁止网络连接，验证原始图结构与角色节点的路由和历史传递；不代表验证真实 LLM 辩论质量或收益。

只有明确加上 `--live` 才可能调用模型和新闻 API。AAPL 2026 年 9 月的一轮/三轮对照已获用户授权并完成，结果保存在 `results/debate_aapl_sep2026_paired/`。

## 保存与核验

三轮开关组默认策略名 `ta-debate-on-r3-v1`；关闭组 `ta-debate-off-r1-v1`。日志分别写入 `agents/logs/modules/<策略名>/`，决策写入 `data/decisions/<策略名>.csv`，不覆盖历史实验。

运行日志记录模块设置、预期研究发言数和实际研究/风险发言数。实际计数不符时失败，不写决策 CSV。模型调用、token 和耗时沿用现有运行日志统计；离线测试本身不产生付费模型调用。

三轮相比一轮正常增加四次研究员调用。模型重试、工具查询等可能增加实际调用和费用，因此不能把这个差值当成固定账单金额。已完成实验的费用、余额及失败补跑记录见上述结果目录。

## 结合当前账户的比例仓位实验（2026-11-15 完成）

独立入口 `python -m experiments.position_month`。`--prepare` 只核验和冻结本地输入；`--live --budget 4` 才调用 DeepSeek；`--evaluate` 只重算结果。结果独立保存于 `results/position_aapl_sep2026/`，不覆盖原始两组实验。

复用每个日期的三个分析师报告及按时间顺序排列的完整一轮/三轮多空辩论。程序逐日提供真实账户的股数、现金、成本、浮动/已实现盈亏及最近交易。研究经理重新生成当前目标仓位，取值 0–1，占总账户资产比例。`keep_shares` 保留股数、比例自然漂移；`rebalance` 在次日开盘按目标比例及成交费用计算订单。成本不作为回本或补仓的机械触发条件。条件性的后续加减仓不提前执行。

旧研究经理、交易员、风险经理和组合经理结论不进入新提示词。新方案不新增大模型风险审核，由程序校验仓位范围、现金、输出格式及费用。没有新增情绪分析、卖空、杠杆或外部证据。因决策角色、账户输入及执行方式同时改变，与旧结果的差异不能单独归因于比例输出。

两组各 21 个日期，42 次模型调用，零失败。一轮净收益 0.5854%、最大回撤 0.6034%；三轮净收益 0.2230%、最大回撤 0.4006%。平均执行后仓位分别 15.5406% 和 9.6055%。初始资金 100,000 美元，9 月 1 日开盘起，10 月 1 日开盘强制清仓估值，每笔成交费用 10 bps；API 成本单独以人民币统计，不扣入美元净值。Token 估算费用 1.4641 元，实际查询余额及扣费延迟说明见 `billing_summary.json`。

14 项离线测试覆盖成本、费用、部分加减仓、持股不变、拆股分红、无未来信息、预算防护，以及重放旧决策与原回测引擎逐日净值一致。`validation.json` 记录全部 42 个账户状态、提示词、源文件哈希与成交记录的重放核验。`position_comparison.png/pdf` 提供五组对比。

### Return-aware one-round sizing rerun (2026-11-15)

`experiments/position_active_month.py` reuses the frozen one-round analyst/debate inputs and sequential account engine in a separate output directory, `results/position_active_aapl_sep2026`. The research manager remains the sole model deciding target exposure; no separate sizing manager was added. The new mandate weighs idle-cash opportunity cost, explicitly evaluates meaningful additions when evidence is bullish, permits zero exposure under material risk, and supplies the last five dated decisions so add/cut conditions can be checked instead of silently moved. No forced minimum allocation is enforced.

Offline preparation: `python -m experiments.position_active_month`. Authorized live run: `python -m experiments.position_active_month --live --budget 2`. Offline validation/plot: `python -m experiments.evaluate_active_position`. Previous experiments and prompts remain preserved. Base runner defaults remain both arms with no previous-decision payload; the new arm opts in. Fifteen account/runner tests pass, including history opt-in and no future-valuation leakage.

The 21-day run completed with 21 successful calls, zero failures, and usage-estimated API cost CNY 0.74704232. Executed target changes: Sep 1 40%, Sep 2 60%, Sep 9 48%, Sep 11 70%; otherwise shares held. Net return 1.3232%, maximum drawdown 2.3701%, mean opening post-trade exposure 64.8702%. Old sizing returned 0.5854%; full Buy & Hold returned 3.8995%. A passive initial allocation of 63.9190% matches the new strategy's mean exposure and returns 2.4934% with 2.5274% drawdown. Thus greater participation improved raw return versus the old sizing policy, but the new timing still underperformed matched-exposure passive holding by 1.1702 percentage points.

The prompt was revised after inspecting September results; this is in-sample iteration, not independent validation or model-weight training. Matching realized average exposure is a retrospective diagnostic, not an ex-ante trading rule. Fee and next-open execution conventions are unchanged. Provider balance deductions can lag usage-based costs; timestamped balance snapshots are saved separately.

### GOOGL / AMZN active sizing extension (2026-11-15)

The three-round direction is set aside. `experiments/position_other_stocks.py` reuses 21 existing September states per stock from `agents/logs/e/f6e0d4240635`, verifying one bull and one bear speech and the archived one-round setting. Only ticker names are changed in the exact completed AAPL active sizing system prompt. Current account and the last five dated decisions are supplied as before. The base account runner now selects its price file using the protocol ticker (AAPL remains the fallback); 17 offline tests pass, including non-AAPL selection.

Run preparation with `python -m experiments.position_other_stocks --ticker GOOGL` (or AMZN). The authorized live command adds `--live --budget 2`; each arm ran separately with a CNY 2 cap. Both completed 21 successful calls with no retries/failures. GOOGL usage-estimated cost CNY 0.7614962; AMZN CNY 0.8481122; combined CNY 1.6096084. The final account balance snapshot was CNY 25.94 at 2026-11-15 19:13:08 Beijing time; provider settlement can lag usage costs.

`python -m experiments.evaluate_other_positions` replays all daily account trajectories, verifies evidence hashes and the actual account/history included in each prompt, and writes independent stock results and combined figures under `results/position_active_other_stocks_sep2026/`.

GOOGL active return -0.3747%, drawdown 3.0099%, mean exposure 36.7739%; full Buy & Hold +4.2586%, drawdown 5.9882%; matched-mean-exposure passive +1.5490%, drawdown 2.2648%. AMZN active return -1.9797%, drawdown 2.8670%, mean exposure 28.4630%; full Buy & Hold -1.4609%, drawdown 5.0372%; matched passive -0.4193%, drawdown 1.4618%. Active management underperformed both passive comparisons for both stocks; smaller drawdown than full exposure does not demonstrate useful timing.

Original archived final-rating binary decisions were also replayed over precisely this month: GOOGL +0.2603%, AMZN +1.9520%. These include the old trader/risk/portfolio workflow and are not a pure sizing-format ablation. Upstream reports were generated in the original archive batch rather than the newer AAPL paired batch; avoid causal cross-stock or model-version claims. All controls use the same next-open execution, 10-bps fees, independent $100,000 accounts, no cash interest, and final Oct 1 open liquidation. Matched exposure remains an ex-post diagnostic.

### August three-stock replication (2026-11-15)

User requested the same one-round active sizing policy for all three stocks in August. The frozen September system prompt was reused exactly except ticker substitution; no changes based on August performance were made. `experiments/position_other_stocks.py --ticker AAPL --month aug2026` (or GOOGL/AMZN) prepares inputs; authorized runs append `--live --budget 2`. Each stock executes 21 sessions Aug 3–Aug 31 using July 31–Aug 28 signal reports, with final liquidation Sept 1 open. Each starts with independent $100,000 cash, 10-bps turnover costs, and no cash interest. All archived states contain exactly one bull and one bear speech. Source files and exact prompts remain saved separately from September.

Concurrent jobs use per-run ledger budget accounting, not account-wide balance declines that may include other stock jobs; actual account availability and failed-call reserves are still checked. Eighteen offline tests pass, including this budget isolation. Three jobs finished with 63 successes, zero failures/retries. Usage-estimated total CNY 2.60793168: AAPL 0.87475156, GOOGL 0.86548856, AMZN 0.86769156. Latest balance CNY 23.86 at Nov 15 19:23:19 Beijing time; settlement can lag usage.

`python -m experiments.evaluate_august_positions` verifies full replay, evidence hashes, prompt identity, historical decision payloads and exact period boundaries, and writes `results/position_active_three_stocks_aug2026/`.

Net returns, active / full Buy & Hold / matched-exposure passive: AAPL +0.1613% / +2.2729% / +0.7603%; GOOGL -3.7278% / -8.2423% / -3.3702%; AMZN -4.7807% / -8.6130% / -3.6659%. Active maximum drawdowns are 1.4577%, 5.9809%, 5.6535%; matched passive drawdowns are 1.0593%, 5.2266%, 4.1086%. All active arms underperform matched passive on both net return and drawdown. Smaller losses than full exposure for GOOGL/AMZN do not establish timing value.

Archived original binary final decisions replayed on the same period return +2.8146%, -3.3270%, +0.8572% respectively. They include the old downstream trader/risk/portfolio stages, so this is not a pure numeric-output ablation. August is a retrospective cross-period test, not a preregistered untouched holdout; training-data contamination cannot be excluded and the stocks are not independent experimental replicates.

### Restored original downstream flow: fractional output only

The earlier `position_*` manager-only experiments are exploratory workflow changes, **not valid evidence for a position-sizing-only ablation of the original project**. The original six downstream role implementations remain byte-identical to Git HEAD (verification saved under `results/full_pipeline_position_2026aug_sep/original_agent_code_verification.json`).

`agents/position_full_pipeline.py` is an opt-in adapter around those original factories, retaining Research Manager → Trader → Aggressive → Conservative → Neutral → Portfolio Manager. It supplies authoritative signal-day account state, clarifies total-account fraction/next-open execution semantics, and extends the final PortfolioDecision with execution_action and a finite [0,1] target or null for keep_shares. Research/Trader sizing suggestions remain subject to risk review and final Portfolio Manager approval. The previous aggressive-allocation mandate and five-day decision-history prompt are not used. Three-round debate, new sentiment and short modules are disabled; original archived one-round evidence and point-in-time historical memory are reused.

The user narrowed execution to AAPL August after the initial six-group batch began. That batch was terminated; 18 completed calls (four useful to AAPL August) were recorded before termination. Other partial outputs are preserved and not continued. Interrupted in-flight requests may have charged without a completed local ledger entry. Subsequent execution is restricted to `python -m experiments.full_position_pair --group AAPL_08 --live --budget 5`, using prompt/account hashes to reuse completed stages. Default maximum output is 8192; truncated responses are rejected and retried with additional capacity up to 16384, with all known usage charged to the ledger. Invalid structured final decisions fail closed. A shared budget guard applies to the entire experiment ledger.

`python -m experiments.evaluate_full_position --group AAPL_08` verifies all six stage outputs per day, frozen input hashes, final risk count, exact prompt/account hashes and replayed trades. It compares to archived original full-pipeline final ratings using the original binary execution mapping over identical dates/fees. This restores architecture, but archived baseline versus new model sampling still has run-date/stochastic/backend differences; it is not a freshly randomized paired comparison. The 26 offline tests include final-manager authority over earlier recommendations, all risk arguments reaching the final manager, numeric validation, historical account isolation, caching and longer-capacity truncation retry.

AAPL August completed on 2026-11-15: 21 days and 126 validated downstream stages, with 139 recorded calls including 13 unsuccessful attempts. The final self-imposed cost guard was raised to CNY 5.50 to finish the already-authorized AAPL group; no other group was resumed. Recorded AAPL cost CNY 4.75177660, other stopped groups CNY 0.34688632; latest provider balance CNY 17.90 at 20:46:42 Beijing time. Interrupted requests/settlement timing mean usage estimates need not exactly equal balance changes.

Verified net return / maximum drawdown / mean post-trade exposure: archived original binary +2.8146% / 2.6601% / 28.5714%; restored full-flow fractional -0.3925% / 0.4156% / 3.6184%; Buy & Hold +2.2729% / 3.1367% / 99.9337%. Starting with USD 100,000, final equities are 102,814.56 / 99,607.49 / 102,272.89. All include 10 bps transaction costs; August execution sessions are August 3–31 with terminal liquidation at September 1 open. The fractional arm was very lightly invested and failed to improve return in this month; lower absolute drawdown alone does not establish better timing or sizing. Results and audited chart: results/full_pipeline_position_2026aug_sep/comparisons/AAPL_08/.

### Daily total-target reassessment (offline change after AAPL August review)

The user requested four additional sizing requirements: independently re-evaluate total exposure daily rather than recursively discounting yesterday's small position; weigh cash opportunity cost alongside downside loss; justify the selected fraction against concrete higher/lower alternatives; explain the economic purpose of tiny positions and allow explicit liquidation. These requirements are now passed to all six downstream roles through SIZING_RULES. Existing explanation fields carry the rationale; the final portfolio manager retains sole execution authority. Keeping shares still uses null, not zero, and reassessment does not force daily trading. No allocation floor, new module, or original role-code change is introduced. This is a prompt requirement, not a mathematical guarantee of sound reasoning.

Existing AAPL August outputs and comparison remain historical results of the previous prompt. This change was tested offline only; no paid model calls or new performance claims. Future live experiments must use a separate output directory and protocol so changed prompt hashes cannot mix with the completed run.

### Compact risk review rerun (AAPL August)

User-authorized speed experiment: `python -m experiments.compact_risk_position --group AAPL_08 --live --budget 5.5`. Separate output directory `results/full_position_compact_risk_aapl_aug2026` protects the previous run. It incorporates the four new total-target sizing requirements. All six original role factories remain in sequence. Only the three risk clients use bounded, explicitly marked head/tail source excerpts, a bounded trader plan, and each prior risk view once. Full account context is retained. Risk output requests at most 450 Chinese characters, hard token cap 1200, thinking disabled; other stages preserve full evidence and thinking. This deliberately changes risk information/compute, so performance changes cannot be attributed solely to sizing instructions. Truncated responses fail validation rather than executing partial decisions. Per-call elapsed_seconds and usage are saved. 27 offline tests pass, including compression, preservation of account/opponent views, and unchanged full-evidence final-manager input.

Compact-risk AAPL August completed: 21 audited days / 126 successful stages, 128 calls with two final-manager retries (one length, one JSON validation), no risk-stage failures. Recorded API cost CNY 1.71749204 vs prior CNY 4.75177660 (63.86% lower); provider balance CNY 16.28 at 21:28:28 Beijing time, settlement may lag. End-to-end balance-snapshot interval about 24 minutes; recorded API request time 1390.93 seconds. Risk reviews average 2.97 seconds, mean input 3708 tokens vs 23780 before, output including reasoning 352 vs 5908 before. Prior run has no comparable per-call elapsed records, so no precise speedup percentage is claimed.

New net return -0.06496%, maximum drawdown 0.34685%, mean exposure 3.89838%, final equity USD 99,935.04 (fees USD 29.96). Previous sizing -0.39251%, original binary +2.81456%. Executed target path 15% → 10% → 6% → 3% → 2%, otherwise keep shares. Faster/cheaper review did not fix low exposure. Both sizing policy and risk computation changed, so outcome differences cannot isolate either cause. Offline audit, updated daily output viewer and three-strategy chart are saved under comparisons/AAPL_08/.
