# Role C 新对话交接与执行指南

> 项目根目录：`D:\97039\Documents\pycharm_workspace\MSBD5018\TradingAgents_t`
>
> 本文用于把项目交给一个全新的对话。不要把 API Key 写入本文、Git、截图或聊天消息。

## 1. 可直接复制到新对话的提示词

```text
你现在负责 MSBD5018 TradingAgents 小组项目的 Role C（实验负责人）。

完整项目根目录为：
D:\97039\Documents\pycharm_workspace\MSBD5018\TradingAgents_t

其中：
- TradingAgents：在官方 TradingAgents v0.6.0 基础上修改的框架源码，已经加入 Finnhub 公司新闻 vendor。
- TradingAgent-project：课程项目、冻结数据、Agent 运行入口、回测和实验目录。
- ROLE_C_HANDOFF.md：已核实的项目状态、Role C 职责、重要文件说明、完整流程和 PowerShell 命令。

请先完整读取 ROLE_C_HANDOFF.md、TradingAgent-project/plan.md、README.md、experiments/README.md、agents/README.md 和 agents/FINNHUB_NEWS.md，再检查实际文件，不要仅凭文档假设功能存在。

工作原则：
1. 你是 Role C，只负责实验设计、调度、运行记录、token/费用汇总和结果交付；不要另写一套回测公式。
2. 先修复本机环境路径并运行免费测试；任何 DeepSeek 付费调用前必须先告诉我预计运行数量和风险，并取得我的明确确认。
3. 不泄露或复述 API Key。发现已暴露的 Key，应建议轮换。
4. 保留原始日志、模型输出和失败记录；不能为了结果好看修改决策。
5. 不覆盖不同实验版本的 CSV；每个实验必须使用唯一 strategy_version。
6. 当前确认的回测周期是 2026-07-01 至 2026-10-09（本地三只股票数据的共同截止日）。如果全组还需要从其中划分开发段和最终留出段，必须在付费批量运行前书面冻结；最终留出段只允许运行一次。
7. 先识别当前阻塞项，再实现 experiments/run_experiments.py、runs.csv 和 costs.csv；实现后运行测试。
8. 当前 CLI 尚没有明确的“单 Agent 模式”开关，Notebook 默认又要求完整长区间决策。不能把“只选一个分析师”擅自当作单 Agent，也不能用不完整 CSV 强行回测；先与 A/B/D 固定定义和评测口径。

请先给出：当前状态核查、阻塞项、拟修改文件和无费用验证方案。未经我确认，不执行真实 LLM 批量实验。
```

## 2. 已核实的当前状态（2026-11-02）

### 已完成

- 两个项目已按正确形式并列放置：`TradingAgents/` 与 `TradingAgent-project/`。
- Finnhub 实现文件、路由、日期窗口、配置、新闻分析师工具链和测试均已接入。
- Finnhub 专项测试：`22 passed`。
- 课程项目测试：`61 passed`（测试时临时把框架目录加入了 `PYTHONPATH`）。
- 官方框架全量测试：`1280 passed, 1 failed, 4 skipped, 1 deselected`。唯一失败是 Windows 下临时目录位于用户目录内导致的隔离断言，不是 Finnhub 或业务功能失败。
- `data/sources.json` 状态为 `complete`，本地价格和财报数据具备运行条件。
- 已有三条免费基线：Buy and Hold、SMA、MACD。

### 尚未完成或必须先处理

- `TradingAgent-project/.env` 不存在，需要从 `.env.example` 创建并由用户本人填写两个不同的 Key。
- conda 环境中的 editable install 仍指向已经不存在的旧路径：
  `...\TradingAgents-Team-Package-2026-10-12\TradingAgents`。
  必须将当前 `TradingAgents_t\TradingAgents` 重新安装到环境。
- `experiments/` 目前只有 README，没有 Role C 的实验调度器、`runs.csv` 或 `costs.csv`。
- 当前新目录没有真实付费实验日志：`agents/logs/` 尚无正式结果。
- 当前决策目录只有基线 CSV，没有完整 TradingAgents 决策 CSV。
- CLI 支持选择分析师，但没有已经定义并验证的“单 Agent 模式”。该实验需要全组先定义，并由 A/D 提供相应实现或配置。
- 当前 Notebook 的既有配置会验证更早种子日直至 2026-10-09 的完整决策序列；仅有 2026-07-01 至 2026-10-09 的实验 CSV 仍不能直接套用旧配置。B 必须把正式回测周期冻结为本轮区间，并同步校验入口，不能绕过覆盖检查。
- 用户现已确认本轮回测周期为 2026-07-01 至 2026-10-09。本地 AAPL、GOOGL、AMZN 行情均截止于 2026-10-09；若要求覆盖 10 月剩余交易日，应先由 B 补充并验证数据。
- `runs.jsonl` 当前只提供每个决策的总 input/output token，不提供可靠的分阶段 token，也没有 DeepSeek 缓存命中/未命中 token。精确费用应优先使用供应商账单；若要按阶段或缓存类别计费，需要在正式实验前补充统计。
- 首次三分析师 smoke v1 在 2026-11-02 因 DeepSeek thinking 模式拒绝人工构造的新闻 tool-call 历史而失败；没有决策 CSV 或可恢复完整状态，但已产生 101,571 input token、16,134 output token，必须计入失败成本。框架随后改为把预取的 Finnhub 冻结证据直接交给新闻分析师，不再生成工具历史。smoke v2 已真实成功：AAPL、2026-07-01、HOLD，10 次 LLM 调用，86,259 input token、36,692 output token、247.619 秒；CSV、运行日志和完整报告均已落盘。Research Manager 的结构化输出首次解析失败后自动自由文本重试，未影响最终成功，但应作为额外调用与成本事件记录。

## 3. Role C 的职责与交付物

Role C 负责：

1. 与全组冻结实验协议：股票、日期、分析师组合、模型、轮数、温度、策略版本、回测口径和最终留出期。
2. 先运行 20 个付费决策的小规模 pilot，统计成功率、LLM 调用数、token、耗时、失败类型和实际费用。
3. 运行论文复现、完整系统、单 Agent、分析师消融、优化开发段和最终留出段。
4. 让所有实验使用同一份冻结行情/财报、同一手续费与回测公式。
5. 保存每次运行的原始日志、报告、最终经理 CSV 和版本信息。
6. 生成 `experiments/runs.csv` 与 `experiments/costs.csv`，把成本和决策文件交给 B/D。
7. 失败运行也要登记；已经付费但只在 CSV 适配阶段失败时，优先离线恢复，不能重复付费。
8. 最终留出期只运行一次，不根据留出结果重新调参。

Role C 不负责：重新实现收益公式、人工修改模型决策、替代 A 修框架主流程、替代 B 改回测口径、替代 D 选择优化方向。

### 最终应提交

- `experiments/run_experiments.py`：读取冻结实验清单，调用现有 batch runner，支持断点续跑，不能重新实现 Agent 或回测。
- `experiments/experiment_manifest.csv`：每个实验版本、日期、股票、分析师与状态。
- `experiments/runs.csv`：每个 `(strategy_version, ticker, trade_date)` 一行。
- `experiments/costs.csv`：token、耗时、计费依据、估算/账单成本和价格日期。
- `data/decisions/<唯一策略版本>.csv`：每个实验一份，不互相覆盖。
- `agents/logs/runs.jsonl`、reports、results：原始证据。
- 给 B 的已校验决策文件；给 D 的指标、成本和失败清单。

建议 `runs.csv` 至少包含：

```text
run_id,strategy_version,ticker,trade_date,analysts,model_provider,quick_model,deep_model,status,llm_calls,tool_calls,input_tokens,output_tokens,elapsed_seconds,action,final_rating,error_type,error,decision_file,log_file,code_commit,data_snapshot_sha256
```

建议 `costs.csv` 至少包含：

```text
run_id,provider,model,input_tokens,cache_hit_input_tokens,cache_miss_input_tokens,output_tokens,input_price_usd_per_million,cache_hit_price_usd_per_million,output_price_usd_per_million,estimated_cost_usd,billed_cost_usd,price_effective_date,price_source,currency,notes
```

若日志没有缓存 token 或账单金额，对应字段留空并把金额标记为 `estimated`，不能称为实际费用。

## 4. 项目结构与重要文件

```text
TradingAgents_t/
├── TradingAgents/                         修改后的官方框架
│   ├── tradingagents/
│   │   ├── agents/analysts/               market/news/fundamentals 等分析师
│   │   ├── agents/tools.py                Agent 可调用工具；约束新闻日期窗口
│   │   ├── dataflows/router.py            数据工具到 vendor 的路由
│   │   ├── dataflows/date_window.py       Finnhub D-7 至 D-1 日期计算
│   │   ├── dataflows/vendors/finnhub/
│   │   │   ├── __init__.py                导出 Finnhub vendor
│   │   │   └── news.py                    鉴权、请求、重试、过滤、去重、缓存、快照
│   │   ├── default_config.py              框架默认模型/vendor/新闻选项
│   │   └── graph/analyst_execution.py     分析师及工具执行计划
│   ├── cli/stats_handler.py               汇总每次决策总调用数和总 token
│   └── tests/test_finnhub_news.py          Finnhub 模拟测试，不产生费用
│
└── TradingAgent-project/                  课程项目
    ├── plan.md                             A/B/C/D 分工和周计划
    ├── config.json                         股票、日期、成本与回测参数
    ├── data.py                             行情/财报读取及时间截面
    ├── signals.py                          最终评级映射、CSV 读取和严格校验
    ├── settings.py                         配置、哈希和可选冻结工具
    ├── analysis.ipynb                      唯一正式回测实现和结果导出
    ├── agents/
    │   ├── check_env.py                    环境、Key、vendor 与本地数据检查
    │   ├── run_agents.py                   单个决策、日志、token、最终 CSV
    │   ├── batch_run.py                    串行批量运行及断点续跑
    │   ├── recover_decision.py             离线恢复已付费但适配失败的决策
    │   ├── local_data_vendor.py            将冻结行情/财报注册给框架
    │   ├── FINNHUB_NEWS.md                 Finnhub 接入规则和修改清单
    │   └── logs/                           运行后产生原始日志、报告和状态
    ├── data/
    │   ├── prices/                         AAPL/GOOGL/AMZN 行情
    │   ├── financials/                     历史财报及披露时间
    │   ├── raw/                            原始数据证据
    │   ├── decisions/                      基线与 Agent 最终决策 CSV
    │   └── sources.json                    数据完整性状态
    ├── experiments/                        Role C 工作目录（目前待开发）
    ├── reports/                            Role D 工作目录
    └── tests/                              课程项目与 Finnhub 入口测试
```

## 5. PyCharm 中的一次性环境设置

这些命令应在 **PyCharm 下方的 Terminal（PowerShell）** 执行，不是在 Python Console 中执行。PyCharm 项目应打开外层 `TradingAgents_t`，解释器选择：

```text
D:\Anaconda3\envs\msbd5018\python.exe
```

### 5.1 重新安装当前框架并安装课程依赖

```powershell
$ROOT = "D:\97039\Documents\pycharm_workspace\MSBD5018\TradingAgents_t"
$PY = "D:\Anaconda3\envs\msbd5018\python.exe"

Set-Location "$ROOT\TradingAgents"
& $PY -m pip install -e .

Set-Location "$ROOT\TradingAgent-project"
& $PY -m pip install -r requirements.txt
```

不要把项目复制进 conda 环境。`pip install -e .` 只是在环境中登记当前源码路径，源码仍保留在项目目录。

### 5.2 创建并编辑 `.env`

```powershell
Set-Location "$ROOT\TradingAgent-project"
Copy-Item -LiteralPath ".env.example" -Destination ".env"
```

随后在 PyCharm 中打开 `TradingAgent-project\.env`，分别填写：

```dotenv
DEEPSEEK_API_KEY=新的DeepSeek密钥
FINNHUB_API_KEY=新的Finnhub密钥
```

两者不是同一个服务，也不能混填。曾在聊天或截图中暴露过的 Key 应先到供应商后台撤销并重新生成。

### 5.3 免费环境检查与测试

```powershell
Set-Location "$ROOT\TradingAgent-project"
& $PY -X utf8 -m agents.check_env
& $PY -X utf8 -m pytest -q

Set-Location "$ROOT\TradingAgents"
& $PY -X utf8 -m pytest -q tests\test_finnhub_news.py
```

预期分别为课程测试 `61 passed`、Finnhub 测试 `22 passed`。官方框架全量测试可选；当前 Windows 上有一个与临时目录位置有关的隔离断言失败，不影响本项目业务测试。

确认环境实际导入的是新路径：

```powershell
Set-Location "$ROOT\TradingAgent-project"
& $PY -X utf8 -c "import tradingagents; print(tradingagents.__file__)"
```

输出必须位于 `TradingAgents_t\TradingAgents\tradingagents`，不能是旧包路径。

## 6. 完整实验流程

### 阶段 0：全组冻结协议，尚不付费

先由 A/B/C/D 书面确认：

- 股票：AAPL、GOOGL、AMZN。
- 复现期：2024-01-01 至 2024-03-29。
- 本轮回测周期：2026-07-01 至 2026-10-09；批处理还会自动加入 2026-06-30 的种子决策。
- 是否在该周期内部划分开发段与最终留出段，以及分界日期；该选择必须在查看结果前冻结。
- 模型、temperature=0、最大辩论轮数、最大风险轮数。
- 每个实验的 analysts 和唯一 `strategy_version`。
- 2024 年 Finnhub 免费历史不足，因此复现实验是否正式固定为 `market,fundamentals`。
- 首个正式版本采用三个分析师：`market,news,fundamentals`。Finnhub 是 `news` 分析师的数据供应商，不是第四个分析师；命令中必须写 `fundamentals`（复数），不是 `foundamental`。
- 后续“单 Agent”的严格定义。它不能自动等同于只启用一个分析师。
- 部分日期 CSV 如何进入 B 的回测；不得绕过 `signals.py` 的覆盖校验。
- DeepSeek 费用的取值日期和官方来源。

推荐实验矩阵（最终以全组冻结版本为准）：

| 实验 | analysts | 日期 | 备注 |
|---|---|---|---|
| 2024 复现 | market,fundamentals | 2024-01-01—03-29 | 不伪造历史新闻 |
| 首个三分析师完整系统 | market,news,fundamentals | 2026-07-01—10-09 | news 使用 Finnhub；共 216 个含种子决策的 cell |
| 去掉 market | news,fundamentals | 同上 | 分析师消融 |
| 去掉 news | market,fundamentals | 同上 | 分析师消融 |
| 去掉 fundamentals | market,news | 同上 | 分析师消融 |
| 单 Agent | 待全组定义 | 同上 | 当前 CLI 未实现明确模式 |
| 优化版开发段 | 冻结后填写 | 待全组从周期内划分 | 只用于调参 |
| 优化版最终段 | 冻结后填写 | 待全组冻结 | 只跑一次 |

### 阶段 1：免费 dry-run

```powershell
Set-Location "$ROOT\TradingAgent-project"
& $PY -X utf8 -m agents.run_agents `
  --ticker AAPL `
  --date 2026-07-01 `
  --analysts market,news,fundamentals `
  --strategy-version dry-run-full-v1 `
  --dry-run
```

它只验证交易日和本地价格/财报，不调用 Finnhub 或 DeepSeek。检查 `agents/logs/runs.jsonl` 中状态为 `dry_run`。

### 阶段 2：一次真实付费 smoke test

以下命令会产生费用，必须先得到用户确认：

```powershell
Set-Location "$ROOT\TradingAgent-project"
& $PY -X utf8 -m agents.run_agents `
  --ticker AAPL `
  --date 2026-07-01 `
  --analysts market,news,fundamentals `
  --strategy-version ta-v0.6.0-deepseek-flash-full-smoke-v1 `
  --output "data/decisions/ta-v0.6.0-deepseek-flash-full-smoke-v1.csv"
```

成功后必须同时检查：最终 CSV 行、`agents/logs/runs.jsonl`、reports、完整状态、Finnhub 快照哈希、token 和耗时。若失败，也必须保留失败日志和已消耗 token。

### 阶段 3：固定的 20 决策 pilot

正式运行前先在 `experiments/experiment_manifest.csv` 固定 20 个 `(ticker, trade_date)`，覆盖三只股票和开发段不同日期，不根据结果临时更换样本。使用独立策略版本 `pilot-v1`。完成后输出：

- 成功/失败/恢复数量。
- 每决策和总计的 input/output token。
- 平均、中位数、P90 耗时。
- LLM/tool 调用数。
- 估算费用与供应商账单费用。
- 失败原因和是否可安全断点续跑。

当前 `batch_run.py` 按完整区间运行，不适合任意 20-cell 清单；Role C 应实现 manifest 调度器逐项调用 `agents.run_agents.run_one()`，并复用现有日志/CSV写入逻辑，不复制 Agent 主流程。

### 阶段 4：正式批量实验

2024 复现示例（付费）：

```powershell
Set-Location "$ROOT\TradingAgent-project"
& $PY -X utf8 -m agents.batch_run `
  --start 2024-01-01 `
  --end 2024-03-29 `
  --tickers AAPL,GOOGL,AMZN `
  --analysts market,fundamentals `
  --strategy-version ta-v0.6.0-deepseek-flash-market-fundamentals-repro-v1 `
  --output "data/decisions/ta-v0.6.0-deepseek-flash-market-fundamentals-repro-v1.csv"
```

2026 年 7 月至 10 月三分析师完整系统（付费，共 216 个含种子决策的 cell；必须先完成 smoke test 和 20-cell pilot，不能直接启动）：

```powershell
& $PY -X utf8 -m agents.batch_run `
  --start 2026-07-01 `
  --end 2026-10-09 `
  --tickers AAPL,GOOGL,AMZN `
  --analysts market,news,fundamentals `
  --strategy-version ta-v0.6.0-deepseek-flash-market-news-fundamentals-2026jul-oct-v1 `
  --output "data/decisions/ta-v0.6.0-deepseek-flash-market-news-fundamentals-2026jul-oct-v1.csv"
```

消融实验必须各用不同策略版本和不同 CSV。重新执行完全相同的命令会跳过成功 cell、重试失败 cell；不要并行运行，因为 checkpoint、日志和 CSV 是共享的。

如果全组另行划分最终留出段，对应命令只能在方案、代码、参数和 strategy version 全部冻结后生成并运行一次。运行前保存代码哈希、实验清单哈希和数据快照。

### 阶段 5：决策校验与回测

每个决策文件先通过 `signals.load_decisions()` 与 `validate_decisions()`。不要仅凭能打开 CSV 就认为合格。当前 Notebook 对长区间完整覆盖有严格要求，因此：

1. 先由 B 确认正式实验配置和区间校验入口。
2. 不改变收益公式；所有策略共用 `analysis.ipynb` 中的回测函数。
3. 每个策略分别运行回测并保存 `results/metrics.csv`、月收益、逐期收益和 `run.json`。
4. 将收益、夏普、最大回撤、换手与成本合并成最终比较表。

### 阶段 6：成本汇总

解析 `agents/logs/runs.jsonl` 时：

- `input_tokens/output_tokens` 与 `tokens_in/tokens_out` 是同一组总数，不能重复相加。
- `failed` 运行可能已经产生费用，必须纳入。
- `dry_run` 与 `recovered` 的新增 token 为 0；恢复记录不能再次计算原调用费用。
- 当前日志只按决策汇总，不能声称是分阶段成本。
- DeepSeek 价格会变化。正式汇总时查询官方当日价格/账单，保存价格来源、有效日期、缓存命中规则和币种。
- 最终报告同时给出总费用、每成功决策费用、每实验版本费用、失败浪费费用和 token 分布。

## 7. 完成判定清单

- [ ] 当前框架已重新 editable 安装，导入路径正确。
- [ ] `.env` 存在，两个 Key 分属正确服务且未泄露。
- [ ] `agents.check_env` 通过。
- [ ] 课程测试 61 passed，Finnhub 测试 22 passed。
- [ ] 协议、单 Agent 定义和回测区间由全组冻结。
- [ ] dry-run 通过。
- [ ] 1 次真实 smoke test 成功并保存全部证据。
- [ ] 20 决策 pilot 完成，成本和失败率已审核。
- [ ] `run_experiments.py`、manifest、runs.csv、costs.csv 完成并有测试。
- [ ] 复现、完整系统和消融实验均使用唯一 strategy version。
- [ ] 决策 CSV 完整通过 B 的校验。
- [ ] 所有版本使用同一回测公式和成本口径。
- [ ] 最终留出段仅运行一次。
- [ ] 原始日志、决策、结果表和代码/数据哈希均已归档。

