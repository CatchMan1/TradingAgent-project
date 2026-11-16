# 04 多轮多空辩论

主要改动：`overlay/agents/debate_config.py`、`debate_agent.py`，以及 shared 中 run_agents 的配置接入。底层沿用原框架循环，不复制一套模型角色。

`DebateOptions(enabled=True, rounds=3)` 默认三轮；`enabled=False` 生效轮数为1。一轮是多头与空头各一次，因此三轮共六次研究发言。风险讨论保持原来一轮（三风险角色）。只增加辩论次数，不重新搜证。

安装后在原项目根目录预览（不会产生付费调用）：

```bash
python -m agents.debate_agent --ticker AAPL --date 2026-08-03
python -m agents.debate_agent --ticker AAPL --date 2026-08-03 --no-multi-round
```

显式加 `--live` 才执行模型/数据 API。整月旧 runner `experiments/debate_month.py` 还依赖原始报告、行情、冻结新闻和记忆数据；本包不附带全部历史调用记录。

测试：`tests/test_debate_module.py` 检查真实图路由、轮数与关开一致性，`tests/test_debate_month.py` 检查预算和冻结数据接入。不要同时开启比例/情绪/做空，以免无法归因轮数的效果。
