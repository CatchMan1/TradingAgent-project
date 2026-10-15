# GDELT新闻接口与实验日期可行性核对

核对日期：2026-10-15。未改变正式实验日期、配置或proposal；用户提出8—10月作为候选，本次仅核查可行性。

## 当前证据

GDELT官方数据页说明数据库免费开放。DOC 2.0官方文档说明默认搜索最近三个月，STARTDATETIME/ENDDATETIME也受滚动窗口约束，ArticleList最多250条。因此最近窗口接口不等于完整历史档案；旧数据可研究GKG等档案路径，但工作量不同。GDELT自身免费不代表BigQuery计算、新闻原站内容或DeepSeek调用免费。

本次无Key调用DOC API，分别尝试2026-07-01与2026-08-01各一天的Apple查询，两次均HTTP 429。原响应保存在july_boundary.txt及august_sample.txt：要求请求间隔至少5秒，并建议高流量用户考虑ngrams。没有取得正常article样本，不能把本次测试作为日期覆盖、字段完整性或三股数据已可用的证明。两次查询参数相同，均为query=(Apple OR AAPL) sourcelang:english，mode=artlist，format=json，maxrecords=5，sort=datedesc；仅startdatetime/enddatetime不同。

用户右侧打开的趋势简报介绍页，也出现在429响应的推荐链接中；该页本身不是历史新闻接口或付费订阅的证明。右侧聊天正文没有成功读取，本次不转述其中内容。

## 日期含义

现在是10月15日，完整10月尚未发生。按项目XNYS交易日历：8月21天，9月21天，10月全月计划22天；8—10月完整共64天，需等10月30日收盘后才具备全部历史行情。

候选优先级：8月3日—9月30日共42天，都是完整历史区间；若要利用当前全部已缓存行情，可考虑8月3日—10月9日共49天。选哪一个须先验证新闻覆盖，再固定开发/留出边界并修订协议，不能先按容易盈利选窗口。团队行情目前只缓存到10月9日，延长至10月14日或之后需补行情。

若每个决策回看7天新闻，还需覆盖种子决策日及其7天历史。8月3日首个交易日对应7月31日种子决策，至少准备到7月24日的新闻。滚动窗口会继续移动，应尽快冻结数据，而不是每次模型实验重新联网查询；用历史档案途径时也要验证相同信息时间规则。

## 接入工作

不只是提供GDELT网址。B负责查询拆分、公司实体匹配、URL/标题去重、时间标准化、公开/收录时点证据、每日覆盖统计和原始响应归档；A负责本地get_news/get_global_news适配、按模拟收盘过滤、确定性选取最多10条、限流重试与缓存、新闻角色和新闻情绪角色读取同一冻结包。仅标题足够时明确称为标题级新闻输入；不要暗示DOC ArticleList给出了全文或自动生成摘要。

缺新闻、查询失败、被截断与不相关结果须区分。ArticleList满250条时要按日期细分，不能把被截断结果当完整覆盖。情绪角色按先前用户决定只分析冻结新闻，不能继续调用当日StockTwits/Reddit。单Agent读取完全相同原始证据，保证对照成立。

## 原项目接什么

论文第5.2节列出Bloomberg、Yahoo、EODHD、FinnHub、Reddit等来源，没有证明只接一个免费接口即可复现数据。

团队包固定v0.6.0的default_config.py中news_data默认yfinance；router.py中的get_news/get_global_news可选yfinance或alpha_vantage。Yahoo实现先取近期feed再做日期过滤，不能因为传入历史起止日期就视为完整历史检索。Alpha Vantage实现调用NEWS_SENTIMENT并传time_from/time_to；官方当前标注premium。

同版本sentiment_analyst.py预先抓新闻、StockTwits、Reddit，再放进提示词；其注释明确近期社交feed不是历史point-in-time档案。现有项目agents/local_data_vendor.py只注册行情/技术/财报等工具，未注册get_news/get_global_news；news和social接入仍需开发。新闻分析师另有宏观/预测市场工具，正式历史评测中要禁用未冻结的实时检索，或提供同口径的历史缓存。

## 来源

- https://gdeltproject.org/data.html
- https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/
- https://www.alphavantage.co/documentation/#news-sentiment
- https://arxiv.org/html/2412.20138#S5.SS2
- 团队包TradingAgents/tradingagents/default_config.py、dataflows/router.py、dataflows/vendors/yahoo/news.py、dataflows/vendors/alpha_vantage/news.py、agents/analysts/sentiment_analyst.py及项目agents/local_data_vendor.py。
