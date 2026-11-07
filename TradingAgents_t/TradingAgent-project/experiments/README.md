# C：实验运行、成本与结果记录

本目录保存 Role C 的固定清单、断点调度器、运行台账与 token 台账。调度器调用
`agents.run_agents.run_one()`，不另写 Agent 或回测收益逻辑。

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

## Role C manifest 调度器

固定 cell 清单位于 `experiment_manifest.csv`。调度器逐行调用现有
`agents.run_agents.run_one()`，不会复制 Agent 或回测逻辑。每个策略使用短哈希日志目录，
避免 Windows 路径长度问题，同时隔离 reports、完整状态、checkpoint、memory 和新闻缓存。

免费检查全部 manifest cell：

```powershell
python -X utf8 -m experiments.run_experiments --dry-run
```

真实串行运行／断点续跑：

```powershell
python -X utf8 -m experiments.run_experiments
```

已成功写入策略 CSV 的 cell 会被跳过；失败 cell 会保留原始日志并在下次运行时重试。
每次尝试后都会重建 `runs.csv` 与 `costs.csv`。本地日志没有 DeepSeek 缓存命中分类或
账单金额，因此成本表先保存 token，价格和美元金额留空，待供应商账单核对后填写。

## 2024 Q1：六轮断点运行

正式清单为 `manifests/repro_2024q1_v1.csv`，共 186 个 cell，固定拆成六轮，
每轮新增 31 个。`--round N` 使用累计前缀，因此中断后重复同一命令会跳过成功 cell，
只续跑未完成或失败的 cell：

```powershell
python -X utf8 -m experiments.run_experiments --manifest experiments\manifests\repro_2024q1_v1.csv --round 1 --rounds 6
python -X utf8 -m experiments.run_experiments --manifest experiments\manifests\repro_2024q1_v1.csv --round 2 --rounds 6
python -X utf8 -m experiments.run_experiments --manifest experiments\manifests\repro_2024q1_v1.csv --round 3 --rounds 6
python -X utf8 -m experiments.run_experiments --manifest experiments\manifests\repro_2024q1_v1.csv --round 4 --rounds 6
python -X utf8 -m experiments.run_experiments --manifest experiments\manifests\repro_2024q1_v1.csv --round 5 --rounds 6
python -X utf8 -m experiments.run_experiments --manifest experiments\manifests\repro_2024q1_v1.csv --round 6 --rounds 6
```

六轮累计边界依次为 31、62、93、124、155、186。2024 Q1 固定使用
`market,fundamentals`，不启用 news analyst，也不会请求 Finnhub。不要为了重试而修改
`strategy_version`；换版本名会创建另一套 CSV、日志和 checkpoint，失去原断点。

DeepSeek 请求由 `TRADINGAGENTS_LLM_TIMEOUT_SECONDS` 限制单次等待时间，
`TRADINGAGENTS_LLM_MAX_RETRIES` 控制 SDK 级重试。失败 cell 的图 checkpoint 会保留，
下次使用同一清单和同一策略版本时从未完成节点继续。

## 2026年7月至10月：三分析师主实验

正式清单为 `manifests/main_2026jul_oct_v1.csv`。日期包含2026-06-30种子日，
随后为2026-07-01至2026-10-09的NYSE交易日，共72个日期、3只股票、216个cell。
分析师固定为 `market,news,fundamentals`；其中news analyst使用Finnhub公司新闻，
时间窗口限制为决策日前7天至前1天。行情与财务仍使用本地point-in-time数据。

六轮累计命令：

```powershell
python -X utf8 -u -m experiments.run_experiments --manifest experiments\manifests\main_2026jul_oct_v1.csv --round 1 --rounds 6
python -X utf8 -u -m experiments.run_experiments --manifest experiments\manifests\main_2026jul_oct_v1.csv --round 2 --rounds 6
python -X utf8 -u -m experiments.run_experiments --manifest experiments\manifests\main_2026jul_oct_v1.csv --round 3 --rounds 6
python -X utf8 -u -m experiments.run_experiments --manifest experiments\manifests\main_2026jul_oct_v1.csv --round 4 --rounds 6
python -X utf8 -u -m experiments.run_experiments --manifest experiments\manifests\main_2026jul_oct_v1.csv --round 5 --rounds 6
python -X utf8 -u -m experiments.run_experiments --manifest experiments\manifests\main_2026jul_oct_v1.csv --round 6 --rounds 6
```

累计边界依次为36、72、108、144、180、216。重复同一轮命令会跳过已写入正式
决策CSV的cell，并利用同一策略日志目录中的checkpoint续跑失败或中断的cell。
不要修改清单中的strategy_version，否则会被视为另一套实验。
