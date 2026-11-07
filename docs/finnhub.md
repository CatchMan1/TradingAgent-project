# Finnhub 历史公司新闻接入

运行入口统一在项目根目录；执行 `python -m pip install -r requirements.txt` 安装本地 `framework/` 和课程依赖。

根目录 `.env` 中填写 `DEEPSEEK_API_KEY`、`FINNHUB_API_KEY`，并设置 `TRADINGAGENTS_ANALYSTS=market,news,fundamentals`、`TRADINGAGENTS_NEWS_VENDOR=finnhub`。命令行 `--analysts` 优先。

```bash
python -m agents.check_env
python -m agents.run_agents --ticker AAPL --date 2026-07-01 --analysts market,news,fundamentals --output data/decisions/example-v1.csv --strategy-version example-v1
```

真实调用会产生模型费用；`--dry-run` 仅检查日期与本地行情/财报。新闻分析师、vendor 和专项测试源码位于 `framework/`。

## 数据和时间规则

- 接口：[Finnhub Company News](https://finnhub.io/docs/api/company-news)，GET `https://finnhub.io/api/v1/company-news`；传 `symbol/from/to`，通过 `X-Finnhub-Token` 请求头鉴权。
- 交易日 D，允许使用 **纽约时间 D−7 00:00（含）到 D 00:00（不含）** 的新闻。前 1—7 天是日历日，包含周末。D=2026-07-01 时可用 06-24—06-30。模型缩小窗口时仍强制取该范围的交集；完全越界、倒置或非法日期不发请求。
- API 查询使用包围上述区间的 UTC 日期，然后按 Unix 发布时间精确过滤。纽约 06-30 深夜的新闻可能带 07-01 UTC 时间戳，应保留；纽约 07-01 凌晨新闻应排除。
- 默认提供最多 20 条去重后的最新新闻，包含标题、摘要、来源、UTC 发布时间和 URL；记录过滤后数量及实际提供数量。不是新闻全文，也不保证供应商完整覆盖所有事件。
- 无数据时明确报告 Finnhub 在窗口内没有返回可用记录，不能推断世界上没有相关新闻。非法响应、认证失败、限流和网络错误不会伪装成“无新闻”。
- 公司新闻模式在 LLM 启动前由应用读取完整冻结快照，并把新闻作为普通证据直接交给模型。该模式不向模型开放工具，也不把人工生成的 tool call/ToolMessage 写入对话历史，以兼容 DeepSeek thinking 模式。全局新闻、实时预测市场和额外宏观接口不进入此模式。
- 免费档文档说明提供近一年历史公司新闻；截至 2026-10-22，2026 年 7—8 月在该区间内，2024 年复现不在。实际可用性取决于账户权限和供应商覆盖。

## 缓存和审计

真实运行首先检查本地价格/财报和 Finnhub Key，再在任何 LLM 调用前预取新闻。认证或请求失败则本次 cell 停止，仅记录失败，不生成猜测决策。成功的空列表可以继续分析并明确标记证据不足。

`agents/logs/cache/finnhub/<查询哈希>.json` 保存接口原始记录、股票、窗口、时区、API 查询参数和抓取时间；不保存 Key。相同股票、完整窗口和时区复用缓存。不同窗口单独缓存，不承诺相邻日期只请求一次。只缓存已完成的历史日期，失败不缓存；损坏的缓存会报错，不自动替换。

预取后把缓存路径和 SHA256 固定到本次 graph 配置。新闻分析师只读取这一份完整快照，不重新联网；内容变动将报错。`agents/logs/runs.jsonl` 的 `data_snapshot.sources.news` 记录路径、SHA256、日期、时区、抓取时间、API 返回数、可用去重数、无效时间戳数及条数上限。保存缓存与日志供组内复用；不要在实验中途删除或刷新它们。

请求之间至少间隔 1.1 秒，网络错误、429、5xx 最多请求 3 次；401/403 立即报错。此限速只覆盖当前 Python 进程，继续使用现有串行批处理，避免多个进程共享 Key 超限。

早期协议的开发段为 2026-07-01—08-05、留出段为 08-06—08-31；当前第一版回测已统一为 2026-07-01—10-09 的完整信号期间，不按早期开发/留出方案切段。批处理会加入开始日期前一交易日作为 seed；开发段 seed 为 06-30，因此完整新闻下载最早需覆盖 06-23。测试段第一天也允许读取此前已发表的新闻，但不能读取测试结果调参。本改动不自动运行实验、不改动 B 的日期配置。供应商事后修订摘要仍是历史数据的局限，发布时间过滤不能证明内容的历史原貌。
