# 01 比例仓位

主要改动：`overlay/agents/position_full_pipeline.py`（提示词扩展、校验 schema、原六阶段调用）、`overlay/experiments/position_account.py`（股数、成本、现金、已实现/未实现盈亏）、`overlay/experiments/full_position_pair.py`（带账户上下文的客户端和历史实验）。

接口：`run_pipeline(state, llm_for_stage)`；客户端在最终经理阶段提供经过校验的 `SizedPortfolioDecision`。最终输出包含 `execution_action=rebalance` + `target_weight_now∈[0,1]`，或 `keep_shares` + `null`。Hold 必须保持股数。`Account.snapshot()` 是实际持仓来源，`execute_interval()` 按次日开盘执行目标总仓位，不在昨日比例上继续乘折扣。

接入：原分析报告和一轮多空辩论生成 state → `full_position_pair.initial_state(frozen, account_snapshot)` → 原研究/交易员/三风险角色/最终经理 → 执行 final_position。原 rating 继续保留；实际交易读目标比例。

关闭方式：使用原图和原来的 PortfolioDecision/二元执行路径，不使用 SizedPortfolioDecision 或 SIZING_RULES。风险审核不缩短；其他模块关闭。共享依赖 `optimization_engine.rebalance` 和旧 position helper 仅提供记账/缓存/费用工具。

优化建议：修改 SIZING_RULES 或方案比较方式，不强迫最低仓位；测试当前0.2→目标0.35、清仓、Hold股数不变以及未知次日价格不进入输入。`test_full_position_pipeline.py`、`test_position_month.py` 覆盖这些约束。
