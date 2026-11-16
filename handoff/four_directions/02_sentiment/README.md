# 02 情绪分析

主要改动：`overlay/agents/historical_sentiment.py`；`original_sentiment_client.py` 是原生模型客户端适配，保留结构化失败后的原版文本回退。`run_sentiment_month.py` 是最后使用原提示词的历史实验版本。

接口：`prepare_articles(snapshot, day)` → `NewsSentimentBatch` → `summarize(bundle, result)` → `sentiment_report`。`run_sentiment_pipeline(state, bundle, llm_for_stage, enabled=True)` 在辩论前追加报告，再运行原一轮多空辩论及完整后续链。`enabled=False` 不请求情绪模型，报告为空；原市场/新闻/基本面报告不重写。

评分−2到2是文本情绪，不是仓位或上涨概率。按纽约时区筛选历史新闻、去重、校验引文；空数据标为 unavailable，不假装中性。历史抓取不能证明文章没有后续修改。

不要使用早期 sentiment paired 版本的强制全仓/清仓提示词或紧凑风险规则。最终版本 COMMON/RISK_RULES 为空；通过客户端保留原版提示词。复用原版 STAGES 定义不意味着启用比例仓位：本模块直接调用原工厂，不使用比例模块的 run_pipeline 或 SIZING_RULES。

接入新数据时改 prepare_articles 的数据适配层，保持 bundle 的 article_id、发布时间与引文约束。测试：`tests/test_historical_sentiment.py`。
