# 四个独立改进方向：团队交接包

此包是 **原项目的源码覆盖层（overlay）**，不是重新实现的 TradingAgents 框架。每个方向目录都放实际源码，保留原路径，便于同学分别修改后接回原代码。共享文件只有一份，见 `manifest.json`。不需要把四个优化同时打开。

基线仓库：https://github.com/CatchMan1/TradingAgent-project
基线提交：`f2fcee2f8d0c37698e9eca05c4caae4f44cfccb9`。

## 四个分工目录

- `01_position/`：完整原流程 + 目标总仓位 [0,1]。研究经理建议、交易员提案、三方风险审核、最终经理授权；不是早期只有研究经理的方案。
- `02_sentiment/`：在原来的市场、新闻、基本面报告旁加历史新闻情绪报告。原始角色提示词不改，不增加强制全仓规则、不缩短风险审核。
- `03_short/`：离散 −1/0/+1，包含显式做空审批与减持直接改做空两个不同实验；不启用比例仓位或情绪。
- `04_debate/`：默认三轮，关闭恢复一轮；每轮多空双方各发言一次，不搜集新证据，风险讨论仍为原来一轮。

## 五分钟接入

使用 Python 3.11+。建议从交接基线新建分支，避免覆盖同学的工作：

```bash
git clone https://github.com/CatchMan1/TradingAgent-project.git trading-team
cd trading-team
git switch -c my-optimization f2fcee2f8d0c37698e9eca05c4caae4f44cfccb9
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r /path/to/four_directions/requirements-extra.txt
python /path/to/four_directions/install.py --destination .
python /path/to/four_directions/install.py --destination . --apply
```

第一次只预览；加 `--apply` 才写入，并备份被覆盖文件到 `handoff-backups/`。脚本先核验全部文件的 SHA-256。**安装所有方向的源码是为了满足现有跨文件依赖，不表示运行时同时启用它们。** 不在原始工作副本上直接执行安装；合并到不同版本时先审查预览和差异。

## 离线测试（不调用 API）

安装后在原项目根目录执行：

```bash
python -m pytest tests/test_debate_module.py tests/test_debate_month.py tests/test_historical_sentiment.py tests/test_full_position_pipeline.py tests/test_short_only.py tests/test_optimizations.py tests/test_position_month.py -k 'not replay_old_binary_decisions_matches_original_engine' -q
```

排除的一个参数化测试依赖未随包提供的历史一轮/三轮完整模型输出，不能用缺失数据冒充复现成功。其他测试使用模拟模型、合成行情或模拟余额。

包中还提供三只股票的紧凑价格/评级夹具，能复现七至九月及十月部分的做空实验，无需原始报告：

```bash
python /path/to/four_directions/03_short/replay.py --ticker AAPL --output /tmp/replay-aapl
python /path/to/four_directions/03_short/replay.py --ticker AMZN --output /tmp/replay-amzn
python /path/to/four_directions/03_short/replay.py --ticker GOOGL --output /tmp/replay-googl
```

每只股票复核 5 个区间 × 3 种策略，导出逐日交易及指标；历史预期指标只用于回归测试，不输入决策。

## 实验边界与协作方式

1. 先保持其他三个方向关闭，各自与原版做对照；共享行情、信号日、成交时点和费用。
2. 先改所属目录下 `overlay/` 的源码，再接回原项目相同路径。最终合并时共享文件只维护一份；跨目录依赖见各目录 README。
3. 现有代码提供单模块实验入口，**没有验证四模块任意组合都兼容**。例如比例输出限制 [0,1]，不能直接用于负仓位；情绪流水线当前固定一轮辩论。组合前要明确接口并新增测试。
4. `shared` 中旧版 `position_month`、`position_other_stocks` 目前仍提供费用、缓存、预算等被新流程引用的函数；旧实验入口不作为推荐方案。`compact_risk_position` 与 `run_optimizations` 仅为历史回归测试保留，不能当成最终实验入口。
5. 所有真实模型调用都是推理/回测，不是更新模型参数的训练。历史月度 runner 依赖本地完整报告、新闻快照和记忆存档；本包不包含这些大型/账户相关日志，不能声称解压后可直接重跑付费整月实验。
6. API 密钥自行配置 `.env`；永远不要提交。需要 token 估算时设置 `DEEPSEEK_TOKENIZER_PATH` 指向供应商 tokenizer.json，默认 `data/tokenizers/deepseek/tokenizer.json`。成本单价要按运行时价格校验，旧估算不保证当前准确。
7. 缓存需同时校验输入/提示词/账户/模型配置；上游报告可复用，下游收到新证据或新持仓时不能盲目复用旧决策。

## 本包内容与版本

仅含源码、测试、接入说明、三只股票价格/离散评级夹具。无密钥、余额、完整提示词调用日志或原始新闻正文。`manifest.json` 记录每个覆盖文件、归属目录、原项目目标路径及哈希。附带的 archive/zip 与 GitHub 分支用于交接，原实验工作目录保留不动。

## 重新打包

修改 overlay 文件后，在 `manifest.json` 更新对应 SHA-256，并重新运行测试；然后执行 `python build_zip.py`，生成上一层的 `TradingAgent-four-directions.zip`。中文图表需要系统安装 Noto Sans CJK SC 等中文字体，缺字体不影响数值回测。
