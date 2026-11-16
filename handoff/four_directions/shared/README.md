# 共享接入层

- run_agents.py：原入口增加 DebateOptions 接入，关闭恢复一轮。
- trading_graph.py、finnhub/news.py：冻结历史记忆/新闻的回放支持。
- optimization_engine.py：多空成交、费用、收益与回撤。
- position_month.py、position_other_stocks.py：新实验仍复用的缓存/费用/预算基础设施；原旧仓位实验入口不是最终流程。
- fixed_position_comparison.py：已有结果评估工具。
- compact_risk_position.py、run_optimizations.py：仅保留旧接口以运行现有回归测试，不推荐用作当前实验入口。

安装器一次放入所有依赖，运行时用各模块接口分别启用。下一步可把旧 runner 中的通用工具抽成专用客户端模块；这次保持已验证接口，避免整理代码时改变模型行为。

兼容现有 GitHub main：随包提供 single_agent.py（旧报告读取/证据适配工具依赖）、local_data_vendor.py 和 signals.py。这里不把单 agent 作为第五个优化方向启用。
