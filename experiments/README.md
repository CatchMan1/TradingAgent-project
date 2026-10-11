# C：实验运行、成本与结果记录

这是预留入口，当前没有真实 Agent 实验结果。建议在本目录编写 `run_experiments.py`，调用 A 的 `agents/batch_run.py`，不要另写回测收益公式。

## 实验流程

1. 确认实验日期和策略版本；`plan.md` 的论文复现／主实验与当前 Notebook 的演示日期不同，正式运行前先与全组统一 config.json。
2. 先运行少量真实决策，记录调用次数、token、耗时、错误和实际费用。
3. 按计划运行完整系统、单 Agent 和分析师消融，每个版本分别保留完整决策 CSV，例如 `data/decisions/full_system.csv`、`single_agent.csv`。不能覆盖成同一文件而丢失版本。
4. 在 analysis.ipynb 的 AGENT_CSV 中指定对应文件，运行 B 的回测流程。所有版本用同一行情、日期、费用和仓位规则。
5. 将汇总成本与运行记录交给 D，收益指标从 `results/metrics.csv` 取得。

建议的记录文件（待开发／真实运行后生成）：

| 文件 | 内容 |
|---|---|
| `runs.csv` | run_id、strategy_version、ticker、日期范围、模型、提示词版本、状态、决策文件路径 |
| `costs.csv` | run_id、decision_time、ticker、stage、input_tokens、output_tokens、actual_cost_usd、latency_seconds |

实际计费数据来自供应商或调用日志；不能用示例数字当作实验结果。运行日志放 `agents/logs/`；最终经理决策放 `data/decisions/`。大型输出通过单独数据包／Release 交接。

当前免费基线已有三条：Buy and Hold、SMA、MACD；plan.md 提及四条，第四条尚未实现，不将其标记为已完成。最终留出期在参数定稿后按计划只评一次。
