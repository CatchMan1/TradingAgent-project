# 优先核验TradingAgents官方已有新闻来源

2026-10-15用户明确：不必换GDELT，先检查官方接口能否满足历史实验。暂不更改实验日期或切换数据源。

## 代码确认与底层路径实测分开记录

包内v0.6.0的news_data默认为yfinance，新闻工具可选Alpha Vantage。官方Yahoo路径先调用yf.Ticker(ticker).get_news(count=...)；主feed为空才调用yf.Search(ticker,news_count=...)，按relatedTickers保留该股票新闻，最后本地按日期过滤。

本次Python3.12临时环境中yfinance为1.2.2，直接测试相同底层获取路径，不加载完整TradingAgents/LLM运行时，也不调用付费模型。主feed对AAPL/GOOGL/AMZN请求各50条，均返回空列表。其后按官方备用方式测试Search：

- AAPL：49条，日期2026-10-14至2026-10-15；没有2026年7—8月或8—9月新闻。
- GOOGL：按股票标签筛选后0条；这不代表谷歌没有新闻。
- AMZN：50条，日期2026-10-14至2026-10-15；没有2026年7—8月或8—9月新闻。

原响应和汇总保存在同目录。当前返回结果支持“本次默认Yahoo路径没有取得目标历史期样本”，不支持“Yahoo所有产品均不能查历史”或“任意其他环境都会为空”的推论。get_news公开函数仅有count/tab参数；TradingAgents外围的start_date/end_date主要用于过滤返回feed，不能当作Yahoo服务端历史归档检索的证明。

## Alpha Vantage状态

### 团队锁定版本复核

初步环境的yfinance 1.2.2低于团队要求，故又在临时环境安装并实测锁定的1.7.0。locked-version-summary.json及*-v170-*.json记录复核结果：三股主feed仍为空；备用Search的AAPL为49条、AMZN为50条，均只覆盖2026-10-14至15日；GOOGL按股票标签筛选后0条。目标7—8月及8—9月样本均未取得。结论以1.7.0复核为准，仍只限定本次环境和官方所用的底层获取路径，不是完整LLM工作流验收。check_yahoo.py可在获准联网环境复现。

### 授权和覆盖尚未实测

官方适配器已有NEWS_SENTIMENT请求，支持time_from/time_to，供应商文档标注premium。初步核验时未配置密钥；后续用户提供密钥，已仅保存至Git忽略的本地.env（权限0600，未跟踪）。没有在报告或日志中记录密钥值。

2026-10-15使用该凭据向官方端点请求AAPL、2026-07-01至07-02历史新闻，HTTP 200但正文只有Information，明确提示NEWS_SENTIMENT需要Premium，没有返回feed。证据为alpha-historical-probe.json与alpha-historical-summary.json（不含密钥）。因此该次凭据下没有取得历史新闻，不能称覆盖已验收；也不能据此判定密钥无效。未购买订阅。

下一步优先由B确认团队是否已有具备NEWS_SENTIMENT历史权限的账号，提供符合时间/文本/覆盖要求的样本；A复用现有适配器完成本地缓存和模拟收盘时点过滤。若官方路径可用，就不引入GDELT。只有官方历史数据/预算无法满足时，再评估其他来源。

## 即使用官方来源也需要处理

官方适配器已做部分响应解析和格式化，因此无需全部重写；课程可复现实验仍需统一去重、时区与实际收盘截止、缺失/失败/截断标记、原始响应及文本哈希保存。所有条件读取同一冻结新闻包，避免不同运行时间抓到不同结果。

尤其是现有Alpha适配器time_to会扩展到当日结束，项目正式允许信息截止却是收盘，不能直接把日期过滤视为已满足收盘过滤。情绪角色现有StockTwits/Reddit实时抓取路径仍须按用户决定改为新闻文本情绪，不可仅增加news analyst后就声称四角色历史输入合格。

来源：包内TradingAgents/tradingagents/dataflows/vendors/yahoo/news.py、alpha_vantage/news.py、default_config.py与本次底层响应；https://ranaroussi.github.io/yfinance/reference/api/yfinance.Ticker.get_news.html ；https://www.alphavantage.co/documentation/#news-sentiment 。
