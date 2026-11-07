# 数据下载与本地目录

数据作为独立压缩包发布，不直接存入 Git 提交。下载 [data-v1 Release](https://github.com/CatchMan1/TradingAgent-project/releases/tag/data-v1) 的 `trading-data.zip` 和 `trading-data.zip.sha256`，放到项目根目录：

```bash
shasum -a 256 -c trading-data.zip.sha256
unzip -n trading-data.zip
```

压缩包内自带 `data/` 前缀；解压后应直接得到 `data/prices/`、`data/financials/`、`data/raw/`、`data/decisions/` 和 `data/sources.json`，不要解压成 `data/data/`。`-n` 避免覆盖已有文件，更新数据时先备份并与组员协调。

`raw/` 保留原始 Yahoo／SEC 响应，`sources.json` 记录来源和校验值。当前包包含真实行情和 SEC 财报，以及免费规则生成的基线信号；不含真实 Agent 决策或历史新闻。压缩只改变存储方式，不改变来源与使用条件。

重新打包：在项目根目录运行 `python package_data.py`，生成 `dist/trading-data.zip` 与校验文件，再上传到新的 GitHub Release。密钥、个人 SEC 联系方式、本地环境和回测 results/ 不进入数据包。
