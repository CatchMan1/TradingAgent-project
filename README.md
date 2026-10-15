# TradingAgents：数据与量化回测

课程项目流程：**共享 data/ → 组员 Agent → 最终经理 CSV → analysis.ipynb → 收益风险与图表**。

真实 Yahoo 行情、公司行动与 SEC 财报已取得，免费基线已有 Notebook 输出。A 已交付官方 TradingAgents 接入代码；首次真实 DeepSeek 运行据成员记录完成模型调用，但因评级适配失败未生成决策 CSV，原始状态与日志尚未随包交付。历史新闻仍待合格来源，正式批量实验尚未完成。

最新交付与验收状态见 [项目进度（2026-10-15）](PROGRESS.md)，首次运行详情见 [DeepSeek 失败记录](reports/DeepSeek首次真实决策失败记录.md)。

## 小组分工与开发位置

按 [plan.md](plan.md) 的四人分工，本仓库已实现 B 的数据与回测，以及 A 的官方 TradingAgents 接入、批量运行和日志。C 的实验汇总和 D 的结果分析仍待交付；已收录首次付费运行的文字记录，尚无可回测的真实 Agent CSV。

| 角色 | 职责 | 开发位置 | 交付给其他组员 |
|---|---|---|---|
| A：工程 | 环境、Agent 接入、批量运行、日志 | [agents/](agents/README.md)、`agents/run_agents.py`、`agents/batch_run.py` | 最终经理 CSV → data/decisions/；阶段日志 → agents/logs/ |
| B：数据 | 数据源、历史过滤、回测、收益与风险指标 | [data.py](data.py)、[signals.py](signals.py)、[analysis.ipynb](analysis.ipynb)、[config.json](config.json) | 共享数据包；results/metrics.csv、逐期收益与图表 |
| C：实验 | 实验调度、消融、运行记录、token 与费用 | [experiments/](experiments/README.md)，建议实现 run_experiments.py | runs.csv、costs.csv；各策略版本的真实决策 CSV |
| D：分析 | 错误分析、选优化方向、报告与展示 | [reports/](reports/README.md)，建议维护 analysis.md、cases.csv、report.tex | 失败案例、优化方案、最终报告与 slides |

数据流：**B 共享数据 → A 生成真实经理决策 → C 按实验版本运行并记成本 → B 回测 → D 分析**。各组员在自己的目录开发；新增 Python 依赖统一加到根目录 requirements.txt，模型密钥放本地环境变量，不能提交。

计划日期与当前演示范围分开：plan.md 提出 2024 年 1–3 月复现、2026 年 7–8 月主实验；当前 Notebook 展示更长的训练／测试基线。正式论文实验前由全组统一 config.json 的日期与留出方案。计划提到四条免费基线，目前实际实现三条；历史新闻、真实 Agent 的付费运行、C 的实际费用汇总与优化仍待完成。

## 目录与运行

```text
analysis.ipynb       唯一回测实现，逐格检查数据、信号、仓位、收益与指标
 data.py             数据采集、整理、历史截止时间过滤
 signals.py          最终经理 CSV/JSONL 读取、适配、校验
 settings.py         参数校验、代码哈希与可选冻结工具
 config.json         默认实验日期、成本、指标窗口
 requirements.txt    conda 环境内安装的依赖
 package_data.py     将本地 data/ 打包为独立 Release 附件
 plan.md             小组计划与分工依据
 agents/             A 的 Agent 单次／批量运行、冻结数据 vendor 与环境检查
 experiments/        C 的实验与成本记录入口（待开发）
 reports/            D 的分析与报告入口；含首次真实运行失败记录
 tests/              关键小样本测试，复用 Notebook 中的公式
 data/
   prices/           AAPL、GOOGL、AMZN 日频行情（各 946 行）
   financials/       三只股票的历史财报事实与实际公开时间
   decisions/        组员 Agent CSV 与各区间生成的基线信号 CSV
   raw/              Yahoo/SEC 原始响应、申报与接受时间依据
   sources.json      来源、原始采集时间、数据说明
 results/            本次实验结果，每次运行更新同名文件
```

## 从 GitHub 开始运行

```bash
git clone https://github.com/CatchMan1/TradingAgent-project.git
cd TradingAgent-project
conda activate py311_env
python -m pip install -r requirements.txt
```

没有 py311_env 时，可先创建 Python 3.11 的 conda 环境。随后下载 [独立数据包 data-v1](https://github.com/CatchMan1/TradingAgent-project/releases/tag/data-v1) 中的两个附件到仓库根目录：

```bash
shasum -a 256 -c trading-data.zip.sha256
unzip -n trading-data.zip
python -m pytest -q
```

代码与数据分开发布；直接克隆只得到代码、说明和已执行的 Notebook 展示。下载数据包并解压后才能重新跑回测或完整检查。数据包保留行情、SEC 财报、来源与原始响应、规则信号；不含真实 Agent 输出或历史新闻。

打开 `analysis.ipynb`，选择 py311_env，重启内核后 Run All。默认一次评价 AAPL、GOOGL、AMZN，不再选择单个 SPLIT。参数仅保留股票列表 `TICKERS`、真实 Agent 文件 `AGENT_CSV`、展示名称 `AGENT_NAME`、`RETURN_TYPE` 和 `NAV_MODE`；日期、成本和指标窗口集中在 config.json。表格直接返回变量，不用 display/HTML。

## Notebook 流程与回测范围

完整行情 → 训练／测试切分 → 信号先保存 CSV → 读取并映射 0/1 仓位 → 分范围回测 → 策略比较与导出。

每只股票分别展示：

| 范围 | 日期 | 净值与仓位 |
|---|---|---|
| train：纯训练 | 2024-01-01～2026-05-31 | 初始净值 1，独立从空仓建仓 |
| test：纯测试 | 2026-06-01～2026-10-09 | 初始净值 1，独立从空仓建仓 |
| train_test：训练＋测试 | 2024-01-01～2026-10-09 | 连续计算，边界不重置 |

原验证期已并入测试期。默认加载所有股票到测试结束日，2023 年只用于指标预热。三种基线 Buy and Hold、SMA Trend (20/50)、MACD Trend (12/26/9) 同时比较；真实 Agent CSV 接入后自动加入 TradingAgents。

训练、测试独立范围只保留收益终点在本段的区间，训练收益不得跨入测试。完整期间保留跨边界的真实持有收益，所以全时段结果不是两个独立结果的简单相加。末行没有下一开盘，收益保留 NaN 后剔除，不补零。

## 只做多与收益公式

BUY 对应仓位 1，SELL 对应仓位 0，HOLD 延续之前的仓位；没有历史 BUY 时 HOLD 对应空仓。`signal` 和 `position` 都只含 0/1，不再用负数动作编码。仓位变化可能为 −1，表示从持有卖出为空仓。

```python
position_changes = np.diff(np.r_[0.0, position])
strategy_ret = position * asset_ret - abs(position_changes) * fee
net_values = 1 + strategy_ret.cumsum()       # additive，默认
# net_values = (1 + strategy_ret).cumprod()  # compound，可选
```

收盘后决策在下一交易日开盘执行，持有到下一开盘。DateTime 是本期开盘，return_end 是下一交易日开盘；资产简单收益为 `(next_open + next_dividend) * next_split / open - 1`，拆股分红直接进入总收益率。历史 `simple_ret / log_ret` 用于观察特征，未来 `pct` 只用于评价，不重复 shift。

`cal_net_values` 保留简单函数入口，拒绝 0/1 以外仓位。对数输入先还原为简单资产收益，再乘仓位、扣比例费用。手续费和滑点默认各 5 bps，合计 fee=0.001。初始建仓扣费，重复 BUY／HOLD 不扣额外换手费；不强制末日平仓。

纯测试的第一期目标仓位由边界前已经可见的决策确定；HOLD 可沿用此前目标，但独立回测从空仓重建，按实际目标扣初始建仓费。训练＋测试则连续持仓，不重复扣费。没有现金、股数或订单撮合模型。

日收益按 return_end 归属，加法模式求和、复利模式复合，月收益使用相同口径。夏普使用日收益、rf/252 和 ddof=0，零波动为空。回撤为净值／历史峰值−1，包含初始净值 1。

## 策略接口与结果

基线信号分别保存为 `data/decisions/baseline_{股票}_train_test.csv`，覆盖种子日到测试末日。修改文件后从读取 CSV 单元格继续运行，以免重新生成覆盖。

统一接口为 `decision_tables[(股票, 策略ID)]` 和 `strategy_names[策略ID]`。新增策略先保存、读取并校验 CSV，再加入这两个字典，共用 `prepare_backtest → select_period → run_backtest → evaluate_backtest`。不为 Agent 复制另一套收益公式。

`results/metrics.csv` 汇总股票／范围／策略的指标，`monthly_returns.csv` 汇总对应月收益。各股票目录保存三个范围的净值回撤图；`results/{股票}/{范围}/{策略}/` 保存逐期收益和仓位变化，各策略完整决策保存在股票目录。run.json 记录股票、日期范围、策略名称、收益口径、费率与来源哈希。重新运行更新生成结果。

## Agent CSV 接口

每行最终经理决策，必需字段：

```text
ticker,decision_time,information_cutoff,action,strategy_version,source
```

source 必须为 portfolio_manager；action 只接受 BUY/SELL/HOLD。时间带时区，决策在当日收盘后、当地午夜前；信息截止不晚于当日实际收盘。同一股票同一区间使用统一策略版本。文件必须覆盖 TICKERS 中的每只股票。每只股票必须包含“训练前最后交易日种子决策 + 训练到测试末日的每日决策（含末日）”。缺失、重复、非法动作、错误来源和未来信息直接报错；不需要 snapshot_id，额外列不覆盖计算字段。

组员返回的文件例如 `data/decisions/agent.csv`，UTF-8 编码，首行为字段名：

```csv
ticker,decision_time,information_cutoff,action,strategy_version,source
AAPL,2023-12-29T16:30:00-05:00,2023-12-29T16:00:00-05:00,BUY,agent-v1,portfolio_manager
GOOGL,2023-12-29T16:30:00-05:00,2023-12-29T16:00:00-05:00,HOLD,agent-v1,portfolio_manager
AMZN,2023-12-29T16:30:00-05:00,2023-12-29T16:00:00-05:00,BUY,agent-v1,portfolio_manager
AAPL,2024-01-02T16:30:00-05:00,2024-01-02T16:00:00-05:00,HOLD,agent-v1,portfolio_manager
GOOGL,2024-01-02T16:30:00-05:00,2024-01-02T16:00:00-05:00,BUY,agent-v1,portfolio_manager
AMZN,2024-01-02T16:30:00-05:00,2024-01-02T16:00:00-05:00,SELL,agent-v1,portfolio_manager
```

**这些动作仅用于说明格式，不是真实 Agent 输出，也不是可直接运行的完整文件。** 实际文件要从种子日覆盖到测试末日 2026-10-09，不能用示例动作替代 Agent 的真实结果。Notebook 会校验完整交易日序列，缺失决策不会补作 HOLD。

| 字段 | 组员填写内容 |
|---|---|
| ticker | `AAPL`、`GOOGL` 或 `AMZN` |
| decision_time | 该模拟交易日的最终经理决策时间，必须带时区；LLM 实际运行时间可另列记录 |
| information_cutoff | 本次允许使用信息的截止时间，不晚于该交易日实际收盘 |
| action | 最终经理的 `BUY`、`SELL` 或 `HOLD`，不填 1/-1/0 或中间分析师意见 |
| strategy_version | 同一次实验统一的策略版本，如 `agent-v1`；修改模型、提示词或策略时更新版本 |
| source | 固定填写 `portfolio_manager` |

上例种子日 2023-12-29 的 BUY 在 2024-01-02 开盘执行；2024-01-02 的动作在 2024-01-03 开盘执行。每只股票每天都要有一行，明确 HOLD 也要返回，不能省略。末日及映射到最后未知收益区间的决策保留在输入文件中，不计额外换手费用。

时间建议用 `America/New_York` 生成带时区的 ISO 8601 字符串：冬令时为 `-05:00`，夏令时为 `-04:00`。不要全年固定同一偏移。提前收市日的信息截止也要提前，例如 2024-07-03 应为 `2024-07-03T13:00:00-04:00`；实际时间可从 `data.schedule()` 的 `close` 列取得。

CSV 放 data/decisions/，设置 `AGENT_CSV=ROOT/"data/decisions/agent.csv"`，即可将真实 Agent 加入全部股票、全部范围的比较；`AGENT_NAME` 设置展示名称。文件应覆盖完整训练和测试期间，同一实验保持统一策略版本。未提供文件时只评价规则基线。

`signals.from_final_state()` 只读取最终 Portfolio Manager 评级。由于本回测只有全仓与空仓，固定映射为 Buy/Overweight → BUY、Hold → HOLD、Underweight/Sell → SELL。Overweight 和 Underweight 在这里不代表真实权重大小；日志保留原始 `final_rating`，报告必须说明这一二元化假设。REVIEW、冲突评级与仅有中间意见的结果仍直接报错。组员负责 Agent，不在本项目中投票或融合分析师意见。

## 样本外解释与核对

默认直接展示训练、测试与全时段结果，不再要求通过冻结开关才能加载测试数据。训练结果用于诊断，测试结果不应反向用于选择指标窗口、模型或提示词；训练＋测试仅用于观察连续表现。未来若接入学习模型，只在训练集拟合，再应用到测试集。

settings.py 的 freeze/check_evaluation 是可选实验冻结工具，Notebook 默认流程不调用。旧 frozen.json 对修改后的日期和源码不再有效。

检查覆盖信号延迟、只做多限制、HOLD 延续、首笔换手、简单／对数输入、加法／复利、拆股分红，以及训练／测试收益边界。

## 参考与限制

官方参考 commit：`1394a3f72aa4393e1a98f51b382434c4b4c2d972`，v0.6.0；[固定代码](https://github.com/TauricResearch/TradingAgents/tree/1394a3f72aa4393e1a98f51b382434c4b4c2d972)。propagate 返回 final_state 与 signal；最终经理写 final_rating/final_trade_decision，Trader 的动作属于中间意见。官方行情路径的复权/补缺口行为不用于本项目撮合。

数据参考：[SEC API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)、[SEC 开发者说明](https://www.sec.gov/about/developer-resources)、[Alpha Vantage 新闻](https://www.alphavantage.co/documentation/#news-sentiment)。SEC 使用实际 acceptance 时间，旧分片缺时间则读取原始申报 header，同来源下仍无法核实就报错。

历史新闻未取得，Yahoo 近期样本不覆盖实验，Alpha Vantage 对应接口为付费，未调用。SEC companyfacts 不保证全部自定义标签或完整财报。供应商可能修订历史数据，保存原始响应也不能证明当年首次发布原貌。

当代 LLM 可能已知道历史事件；输入时间过滤无法消除预训练知识风险。组员应记录模型、提示词、运行时间，隔离未来记忆与检索。比例收益模型不模拟税款、分红真实支付延迟或成交容量。人工数据仅用于测试。
