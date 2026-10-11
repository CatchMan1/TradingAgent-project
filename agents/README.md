# A：工程与 Agent 开发

这是预留开发入口，目前尚未实现或接入 LLM。数据与回测已经可运行，不能把规则基线当作真实 Agent 输出。

建议在本目录实现：

- `run_agents.py`：单日／单股票入口，接入官方 TradingAgents 和模型配置。
- `batch_run.py`：按股票和模拟交易日批量运行；重试失败任务并保存日志。
- `logs/`：逐次运行的模型、提示词版本、阶段结果、token、耗时与错误。本地生成，不提交密钥和完整运行日志。

这些文件名是协作约定，不是已经存在的实现。外部项目依赖只登记在根目录 requirements.txt，不提交虚拟环境。

## 输入与输出

从项目根目录读取 `config.json` 与 `data/`。在每个模拟日期调用根目录 `data.py` 的 `data_asof()`，不能把全时期行情或财报直接传给模型。历史新闻尚未取得，不用近期新闻冒充历史新闻。

最终经理的真实决策写入 `data/decisions/agent.csv`，字段为：

```text
ticker,decision_time,information_cutoff,action,strategy_version,source
```

`source=portfolio_manager`；`action` 为 BUY／SELL／HOLD。中间分析师、Trader 或辩论的意见保存在日志中，不作为最终仓位。`signals.from_final_state()` 可从官方最终经理结果适配动作，`signals.validate_decisions()` 检查日期、版本和信息截止时间。完整格式与时间约定见[主 README](../README.md#agent-csv-接口)。

C 负责实际实验调度与成本记录；B 负责最终 CSV 校验和收益评价；D 的优化方案确定后由 A 接入。按 plan.md 先复现，后优化。
