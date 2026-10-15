# A：工程与 Agent 接入

A 的输出不是另一套回测。A 负责把固定版本的官方 TradingAgents 跑成真实的最终经理决策，并写成 B 已经定义的 CSV 接口；B 继续负责收益、换手、夏普和最大回撤。

## 1. 环境

本项目使用官方仓库的固定版本：`TradingAgents` v0.6.0，commit `1394a3f72aa4393e1a98f51b382434c4b4c2d972`。官方代码已经在同级目录 `../TradingAgents` 建好虚拟环境时，可以直接复用：

```bash
cd /path/to/TradingAgent-project
../TradingAgents/.venv/bin/pip install -r requirements.txt
cp .env.example .env
# 编辑 .env，只填本机的 DEEPSEEK_API_KEY
```

如果使用别的环境，必须先安装官方仓库本身：

```bash
cd /path/to/TradingAgents
git checkout 1394a3f72aa4393e1a98f51b382434c4b4c2d972
python -m pip install -e .
cd /path/to/TradingAgent-project
python -m pip install -r requirements.txt
```

运行前需要把 B 的独立数据包解压到本仓库的 `data/`，并确认 `data/sources.json` 的状态为 `complete`。没有它，A 会在 API 调用前停止，不会用当前 Yahoo 数据替代历史截面。

检查环境：

```bash
../TradingAgents/.venv/bin/python -m agents.check_env
```

## 2. 单个决策

默认只使用 `market,fundamentals`。B 仓库明确记录了目前没有合格的历史新闻档案，因此默认不启用 `news` 或 `social`，避免把今天的新闻倒灌到历史日期。若全组以后取得授权的历史新闻，再单独固定数据源和 strategy version。

```bash
../TradingAgents/.venv/bin/python -m agents.run_agents \
  --ticker AAPL \
  --date 2024-01-02 \
  --strategy-version ta-v0.6.0-deepseek-flash-market-fundamentals-v1 \
  --output data/decisions/ta-v0.6.0-deepseek-flash-market-fundamentals-v1.csv
```

程序会先调用 B 的 `data_asof()` 检查价格和财报截面，再把这两个本地数据源注册成 TradingAgents 的 vendor。每次成功运行会生成：

- B 接口需要的最终经理 CSV 行：只接受 `BUY`、`SELL`、`HOLD`。
- `agents/logs/runs.jsonl`：模型、分析师、日期、数据截面哈希、LLM/tool 调用数、输入/输出 token、耗时和错误。
- `agents/logs/reports/<ticker>/<date>/`：完整报告和 HTML。
- `agents/logs/results/`：官方 graph 的完整状态文件。

最终经理是唯一的回测输入。五档评级按 B 的二元仓位协议固定映射：Buy/Overweight → BUY，Hold → HOLD，Underweight/Sell → SELL。原始评级保留在运行日志中；这不表示能够回测实际的超配或低配权重。Trader、bull/bear debate、risk analysts 的内容只留在报告和状态日志，不能直接转成仓位。

## 3. 批量运行与断点续跑

下面的命令覆盖指定区间内每个 NYSE 交易日，并自动加入区间开始前的 seed session；这正是 B 的 `validate_decisions()` 要求的格式：

```bash
../TradingAgents/.venv/bin/python -m agents.batch_run \
  --start 2024-01-01 \
  --end 2024-03-29 \
  --tickers AAPL,GOOGL,AMZN \
  --strategy-version ta-v0.6.0-deepseek-flash-market-fundamentals-v1
```

批处理是串行的，原因是官方 memory/checkpoint 和本地 CSV/JSONL 都是共享文件；串行可以避免两个日期互相覆盖状态。每个 cell 成功写 CSV 后才算完成；失败的 cell 只写错误日志。重新执行同一条命令会跳过已经成功的 `(ticker, date, strategy_version)`，只重试失败项。

主实验也用同一个入口，但应使用新的 `strategy_version`，不要覆盖论文复现结果：

```bash
../TradingAgents/.venv/bin/python -m agents.batch_run \
  --start 2026-07-01 \
  --end 2026-08-31 \
  --strategy-version ta-v0.6.0-deepseek-flash-market-fundamentals-main-v1
```

## 4. 交给 B 和 C

完成一段区间后，先用 B 的校验，而不是直接打开 Notebook：

```bash
../TradingAgents/.venv/bin/python - <<'PY'
from signals import load_decisions, validate_decisions
from settings import load_config

cfg = load_config()
path = "data/decisions/ta-v0.6.0-deepseek-flash-market-fundamentals-v1.csv"
for ticker in cfg["tickers"]:
    decisions = validate_decisions(load_decisions(path), ticker, "2024-01-01", "2024-03-29")
    print(ticker, len(decisions), decisions.action.value_counts().to_dict())
PY
```

C 可以直接读取 `agents/logs/runs.jsonl` 汇总实际 token 和耗时。`input_tokens`/`output_tokens` 与 `tokens_in`/`tokens_out` 记录相同的实际统计；失败的付费运行也记录已产生的 token。`actual_cost_usd` 不在 A 中臆造；需要按 DeepSeek 当日价格表由 C 根据 token 账单计算，并记录价格日期。`status=recovered` 的离线恢复记录 token 为 0，原始调用费用只算一次。

## 5. 恢复已付费但适配失败的决策

若官方完整状态已保存、`runs.jsonl` 有对应的评级适配失败记录，可以离线恢复 CSV，不再次调用模型：

```bash
python -m agents.recover_decision --ticker AAPL --date 2024-01-02 \
  --strategy-version ta-v0.6.0-deepseek-flash-market-fundamentals-v1
```

入口核对状态中的股票和日期、失败日志中的策略版本和错误类型；已有相同决策时拒绝重复写入。恢复记录含原状态文件哈希和原始评级。若日志或状态文件缺失，应先找回真实文件，不用报告文字重建决策。

## 6. 复现边界

“温度为 0”只降低部分模型的采样波动，不能保证 LLM 字节级重复；DeepSeek 的 thinking 模式也可能忽略 temperature。每个 run 必须保留模型 ID、代码 commit、strategy version 和 B 数据截面哈希。论文复现必须先固定日期、股票、分析师和模型，再开始主实验，不能一边看测试结果一边改设置。
