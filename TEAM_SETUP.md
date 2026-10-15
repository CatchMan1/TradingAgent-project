# 组员环境安装与运行

## 从GitHub的side分支开始

本仓库不内嵌上游TradingAgents副本。首次安装时，两个仓库放在同一个父目录，固定上游版本后在同一虚拟环境安装：

```bash
git clone --branch side https://github.com/CatchMan1/TradingAgent-project.git
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents
git checkout 1394a3f72aa4393e1a98f51b382434c4b4c2d972
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
cd ../TradingAgent-project
python -m pip install -r requirements.txt
cp .env.example .env
```

随后按README从data-v1 Release下载并校验数据包，再执行下方验证。四分析师是研究目标；当前默认仅启用技术和基本面，正式新闻/情绪流程须先完成数据验收。下文保留原团队压缩包安装方式。

## 从原团队包开始

压缩包包含两个并列目录：

```text
TradingAgents-Team-Package-2026-10-12/
├── TradingAgents/          官方框架，固定为 v0.6.0
└── TradingAgent-project/   A/B 项目代码及冻结数据
```

包内不包含 API Key、`.env`、虚拟环境、Git 历史和个人运行日志。

## macOS / Linux 安装

```bash
cd TradingAgents-Team-Package-2026-10-12/TradingAgents
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .

cd ../TradingAgent-project
python -m pip install -r requirements.txt
cp .env.example .env
```

如果是 macOS arm64 且使用 Python 3.12，可用已验证的精确版本快照覆盖依赖版本：

```bash
python -m pip install -r requirements-lock-macos-arm64-py312.txt
```

在 `.env` 中填写自己的 Key：

```text
DEEPSEEK_API_KEY=自己的Key
```

不要在群聊中发送 Key，也不要提交 `.env`。

## 验证

```bash
python -m pytest -q
python -m agents.check_env
python -m agents.run_agents --ticker AAPL --date 2024-01-02 --dry-run
```

`check_env` 需要有效的 DeepSeek Key；dry-run 不调用模型、不产生费用。

## 第一次真实运行

```bash
python -m agents.run_agents \
  --ticker AAPL \
  --date 2024-01-02 \
  --strategy-version ta-v0.6.0-deepseek-flash-market-fundamentals-v1 \
  --output data/decisions/ta-v0.6.0-deepseek-flash-market-fundamentals-v1.csv
```

确认单次结果、token、耗时和日志正常后，才运行批量实验。完整顺序见 `agents/README.md`。
