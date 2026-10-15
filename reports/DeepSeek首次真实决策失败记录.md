# DeepSeek 首次真实决策运行记录

## 运行结论

本次 DeepSeek 调用实际上已经完成。失败并非发生在模型调用或数据读取阶段，而是发生在最终结果转换为小组回测 CSV 的阶段。

本次运行信息：

- 股票：AAPL
- 决策日期：2024-01-02
- 模型：DeepSeek Flash
- 分析师：Market、Fundamentals
- LLM 调用次数：14 次
- 输入 token：130,469
- 输出 token：46,421
- 总耗时：272.785 秒，约 4 分 33 秒
- 最终经理评级：`Underweight`
- 最终运行状态：`failed`
- 决策 CSV：未生成
- API 费用：已经产生

## 终端提示说明

运行过程中出现：

```text
Research Manager: structured-output invocation failed (structured output returned no parsed result); retrying once as free text
```

这表示 Research Manager 的结构化输出没有成功解析，程序随后自动改用普通文本重试。该步骤已经完成，不是本次运行最终失败的原因。

最终错误为：

```text
A run failed: ValueError: Unsupported/absent final rating; Overweight/Underweight/REVIEW require explicit upstream policy
```

## 失败原因

官方 TradingAgents v0.6.0 支持五档评级：

```text
Buy
Overweight
Hold
Underweight
Sell
```

小组项目的 `signals.py` 目前只接受三档回测动作：

```text
BUY
HOLD
SELL
```

本次 Portfolio Manager 返回了：

```text
Underweight
```

由于小组适配器没有预先定义 `Overweight` 和 `Underweight` 应如何映射到 `BUY/HOLD/SELL`，程序主动拒绝写入决策 CSV。这属于官方五档评级与小组三档回测接口之间的协议不一致，并非 DeepSeek 调用失败。

## 已保存的运行结果

虽然 CSV 没有生成，但完整模型结果已经保存。

完整状态文件：

```text
agents/logs/results/AAPL/TradingAgentsStrategy_logs/full_states_log_2024-01-02.json
```

最终经理决定与记忆记录：

```text
agents/logs/memory/trading_memory.md
```

运行统计和错误记录：

```text
agents/logs/runs.jsonl
```

因此，在确定评级映射规则后，原则上可以利用已经保存的完整状态恢复这条决策，不需要再次调用 DeepSeek。

## 需要小组确定的实验规则

在继续批量实验前，小组必须统一确定：

```text
Overweight  → BUY、HOLD 或其他动作
Underweight → SELL、HOLD 或其他动作
```

一种适用于二元持仓回测的映射方式是：

```text
Buy         → BUY
Overweight  → BUY
Hold        → HOLD
Underweight → SELL
Sell        → SELL
```

另一种较保守的映射是：

```text
Buy         → BUY
Overweight  → HOLD
Hold        → HOLD
Underweight → HOLD
Sell        → SELL
```

第二种方案存在语义问题：当前回测中的 `HOLD` 表示保持上一期仓位，而 `Underweight` 通常表示降低仓位，两者并不完全相同。因此，映射方式必须在观察更多实验结果之前固定，并在实验协议和报告中明确说明。

## Token 日志字段问题

本次 `runs.jsonl` 同时记录了：

```json
"input_tokens": 0,
"output_tokens": 0,
"tokens_in": 130469,
"tokens_out": 46421
```

实际 token 数量是：

```text
tokens_in  = 130469
tokens_out = 46421
```

`input_tokens` 和 `output_tokens` 是初始化字段，但没有被实际统计结果覆盖。C 角色后续汇总成本时，应暂时读取 `tokens_in` 和 `tokens_out`，或由工程负责人统一日志字段。

## 后续处理建议

1. 暂时不要重复运行同一条付费命令。
2. 向小组报告五档评级与三档动作接口不兼容的问题。
3. 在全组统一映射规则后修改 `signals.from_final_state()` 及相关测试。
4. 使用已经保存的完整状态恢复本次 AAPL 决策，避免重复产生 API 费用。
5. 修复并验证后，再开始 20 次成本试跑或季度批量实验。
6. 在适配器修复前不要运行完整批量任务，否则所有返回 `Overweight` 或 `Underweight` 的单元都会失败，但仍会产生费用。
