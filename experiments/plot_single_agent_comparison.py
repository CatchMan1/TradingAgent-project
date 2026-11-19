"""Validate and visualize the archived single-agent experiment; no API calls.

python -m experiments.plot_single_agent_comparison
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "results/single_vs_multi_AAPL_GOOGL_AMZN"
DEFAULT_OUTPUT = ROOT / "results/single_agent_comparison"
TICKERS = ("AAPL", "GOOGL", "AMZN")
STYLES = {
    "single_agent": ("Single Agent", "#9467bd", "--"),
    "agent": ("Multi Agent", "#1f77b4", "-"),
    "buy_hold": ("Buy and Hold", "#737373", ":"),
}


def load_results(source):
    """Fail closed on inconsistent metrics, daily ledgers, or backtest settings."""
    source = Path(source)
    run = json.loads((source / "run.json").read_text())
    if (run["return_type"], run["nav_mode"], run["fee"], run["exclude_periods"]) != (
        "simple", "additive", 0.001, []
    ) or run["periods"] != {"agent_period": ["2026-07-01", "2026-10-09"]}:
        raise ValueError("This report requires the archived full-period additive protocol")
    metrics = pd.read_csv(source / "metrics.csv")
    if metrics.duplicated(["ticker", "period", "strategy"]).any():
        raise ValueError("Duplicate strategy metrics")
    expected = {(t, s) for t in TICKERS for s in (*STYLES, "sma", "macd")}
    if set(zip(metrics.ticker, metrics.strategy)) != expected or len(metrics) != 15:
        raise ValueError("Expected three stocks and five strategies per stock")
    if not metrics.period.eq("agent_period").all():
        raise ValueError("Unexpected evaluation period")
    curves, rows = {}, []
    for ticker in TICKERS:
        for strategy in STYLES:
            row = metrics.loc[metrics.ticker.eq(ticker) & metrics.strategy.eq(strategy)].iloc[0]
            daily = pd.read_csv(source / ticker / "agent_period" / strategy / "daily.csv")
            values = 1.0 + daily.strategy_ret.cumsum().to_numpy()
            peak = np.maximum.accumulate(np.r_[1.0, values])[1:]
            drawdown = values / peak - 1.0
            end = pd.to_datetime(daily.return_end, utc=True).dt.tz_convert("America/New_York").dt.tz_localize(None)
            if (len(daily) != 70 or int(row.return_intervals) != 70
                    or not end.is_monotonic_increasing or end.duplicated().any()
                    or end.min() < pd.Timestamp("2026-07-01")
                    or end.max() >= pd.Timestamp("2026-10-10")
                    or not np.isfinite(daily.strategy_ret).all()
                    or not np.allclose(values, daily.net_values, rtol=0, atol=1e-10)
                    or not np.allclose(drawdown, daily.drawdown, rtol=0, atol=1e-10)
                    or not np.isclose(values[-1] - 1, row.cumulative_return, rtol=0, atol=1e-10)
                    or not np.isclose(drawdown.min(), row.max_drawdown, rtol=0, atol=1e-10)
                    or not np.isclose(daily.cost.sum(), row.cost_sum, rtol=0, atol=1e-10)):
                raise ValueError(f"Daily ledger does not reconcile: {ticker}/{strategy}")
            # Returns belong at their END timestamp, with initial NAV=1 at the first open.
            initial = pd.to_datetime(daily.DateTime.iloc[0], utc=True).tz_convert("America/New_York").tz_localize(None)
            curves[ticker, strategy] = (pd.DatetimeIndex([initial, *end]),
                                        np.r_[1.0, values], np.r_[0.0, drawdown])
            rows.append(dict(ticker=ticker, strategy=strategy,
                             strategy_name=STYLES[strategy][0],
                             return_pct=100 * row.cumulative_return,
                             max_drawdown_pct=-100 * row.max_drawdown,
                             sharpe=row.sharpe, turnover=row.turnover_sum,
                             trading_cost_pct=100 * row.cost_sum, return_intervals=70))
    return pd.DataFrame(rows), curves


def build_report(source=DEFAULT_INPUT, output=DEFAULT_OUTPUT):
    source, output = Path(source).resolve(), Path(output).resolve()
    if source == output or source in output.parents:
        raise ValueError("Keep generated presentation files separate from archived results")
    summary, curves = load_results(source)
    os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "single-agent-chart-cache"))
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib.ticker import PercentFormatter

    output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "svg.fonttype": "none"})
    summary.to_csv(output / "comparison_metrics.csv", index=False, lineterminator="\n")
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.5))
    x, width = np.arange(3), 0.24
    for i, (strategy, (label, color, _)) in enumerate(STYLES.items()):
        selected = summary.loc[summary.strategy.eq(strategy)].set_index("ticker").loc[list(TICKERS)]
        for axis, field in zip(axes, ("return_pct", "max_drawdown_pct")):
            bars = axis.bar(x + (i - 1) * width, selected[field], width,
                            label=label, color=color, zorder=3)
            axis.bar_label(bars, labels=[f"{v:+.2f}" if field == "return_pct" else f"{v:.2f}"
                                       for v in selected[field]], padding=4, fontsize=9)
    for axis in axes:
        axis.set_xticks(x, TICKERS)
        axis.set_xlabel("Stock (separate backtests)")
        axis.grid(axis="y", alpha=0.18, zorder=0)
        axis.axhline(0, color="black", linewidth=0.7)
        axis.margins(y=0.22)
    axes[0].set(title="Net cumulative return | higher is better", ylabel="Return (%)")
    axes[1].set(title="Maximum drawdown | lower is better", ylabel="Loss from peak (%)")
    axes[0].set_ylim(-29, 31)
    axes[1].set_ylim(0, 35)
    fig.suptitle("Single Agent vs Multi Agent vs Buy and Hold", fontsize=16, y=0.98)
    fig.legend(*axes[0].get_legend_handles_labels(), loc="upper center",
               bbox_to_anchor=(0.5, 0.91), ncol=3, frameon=False)
    fig.text(0.5, 0.025, "2026-07-01 to 2026-10-09 | DeepSeek Flash | additive NAV | 10 bps per unit turnover\n"
             "Source: archived metrics.csv and daily ledgers; API fees excluded; no event dates removed.",
             ha="center", fontsize=9, color="#555555")
    fig.subplots_adjust(top=0.76, bottom=0.21, left=0.07, right=0.98, wspace=0.23)
    for ext in ("png", "svg"):
        fig.savefig(output / f"returns_drawdown_comparison.{ext}", dpi=200, facecolor="white")
        if ext == "svg":
            path = output / f"returns_drawdown_comparison.{ext}"
            path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")
    plt.close(fig)

    fig, axes = plt.subplots(2, 3, figsize=(15, 7.3), sharex="col", sharey="row")
    for col, ticker in enumerate(TICKERS):
        for strategy, (label, color, linestyle) in STYLES.items():
            dates, nav, dd = curves[ticker, strategy]
            axes[0, col].plot(dates, nav, label=label, color=color, linestyle=linestyle, linewidth=2)
            axes[1, col].plot(dates, dd, color=color, linestyle=linestyle, linewidth=1.6)
        axes[0, col].set_title(ticker, fontsize=13, fontweight="bold")
        axes[0, col].axhline(1, color="black", linewidth=0.6)
        axes[1, col].axhline(0, color="black", linewidth=0.6)
        axes[1, col].yaxis.set_major_formatter(PercentFormatter(1))
        axes[1, col].xaxis.set_major_locator(mdates.MonthLocator())
        axes[1, col].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
        axes[1, col].set_xlabel("Return interval end date (New York)")
        for axis in axes[:, col]:
            axis.grid(alpha=0.18)
    axes[0, 0].set_ylabel("Additive NAV (initial value = 1)")
    axes[1, 0].set_ylabel("Drawdown from running peak (%)")
    fig.suptitle("How performance and risk evolved across the three stocks", fontsize=16, y=0.98)
    fig.legend(*axes[0, 0].get_legend_handles_labels(), loc="upper center",
               bbox_to_anchor=(0.5, 0.94), ncol=3, frameon=False)
    fig.text(0.5, 0.025, "Source: archived daily ledgers, 2026-07-01 to 2026-10-09. "
             "70 open-to-open returns per stock; initial NAV and all transaction costs retained.",
             ha="center", fontsize=9, color="#555555")
    fig.subplots_adjust(top=0.84, bottom=0.13, left=0.065, right=0.985, hspace=0.23, wspace=0.10)
    for ext in ("png", "svg"):
        fig.savefig(output / f"equity_drawdown_three_stocks.{ext}", dpi=200, facecolor="white")
        if ext == "svg":
            path = output / f"equity_drawdown_three_stocks.{ext}"
            path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")
    plt.close(fig)

    notes = ["基于同一 DeepSeek Flash 的三股历史对照，每股72条信号、70个收益区间；含2026-06-30种子日。",
             "多Agent为技术、基本面、新闻三分析师，共11个决策角色；单Agent一次性综合原始证据。",
             "单Agent读取参考实验中当日已结算的历史记忆：同股最多5条、跨股3条；不是自身独立交易形成的记忆。",
             "输入由归档重建，旧版实际工具查询和记忆提示词未逐次保存，不声称输入逐字一致。",
             "BUY目标持仓1、SELL目标持仓0、HOLD延续；次日开盘执行，10bps换手成本，采用加法净值。",
             "215条首次格式成功、1条缺括号离线恢复；原始响应和HOLD动作保留，无额外修复模型调用。",
             "本实验没有运行GPT-6.1 Sol；图中不混入后续情绪、辩论或仓位优化实验。"]
    findings = []
    for ticker in TICKERS:
        group = summary.loc[summary.ticker.eq(ticker)].set_index("strategy")
        single, multi, hold = (group.loc[s] for s in STYLES)
        findings.append(f"{ticker}：单Agent收益{single.return_pct:+.2f}%、最大回撤{single.max_drawdown_pct:.2f}%；"
                        f"多Agent收益{multi.return_pct:+.2f}%、最大回撤{multi.max_drawdown_pct:.2f}%；"
                        f"买入持有收益{hold.return_pct:+.2f}%、最大回撤{hold.max_drawdown_pct:.2f}%。")
    conclusion = "本窗口内多Agent在三股上的收益和最大回撤均优于单Agent；多Agent仅在AAPL跑赢买入持有。样本有限，不能推广为普遍结论，也不能把差异完全归因于协作机制。"
    costs = json.loads((ROOT / "experiments/googl_amzn_single_live_20261109/cost_summary.json").read_text())
    billing = (f"单Agent216次已记录逻辑调用，输入{costs['input_tokens']:,}、输出{costs['output_tokens']:,} token（输出已含推理）。"
               f"返回usage计价{float(costs['usage_priced_cost_cny']):.2f}元；"
               "2026-11-09账户累计减少19.47元，与usage计价约0.23元差额未核销。"
               "这不是当前余额；不包含既有多Agent和共享记忆的成本，API费用不扣进图中交易收益。")
    report = "# 单Agent与多Agent实验结果\n\n" + conclusion + "\n\n"
    report += "![收益和最大回撤对比](returns_drawdown_comparison.png)\n\n"
    report += "\n".join("- " + t for t in findings) + "\n\n"
    report += "![三股净值与回撤走势](equity_drawdown_three_stocks.png)\n\n"
    report += "## 实验口径与限制\n\n" + "\n".join("- " + n for n in notes) + "\n\n"
    report += "## 新增模型调用成本\n\n" + billing + "\n\n"
    report += "## 代码与复现\n\n" + "周晓杨负责单Agent方案、预算与整合，Codex辅助实现、执行及结果整理。\n\n"
    report += "仅从归档生成本页和图表，无需密钥，也不调用模型：\n\n```bash\npython -m experiments.plot_single_agent_comparison\n```\n\n"
    report += "从已有信号重新运行完整Notebook回测（无模型调用），再画图：\n\n```bash\npython -m experiments.compare_single_agent --tickers AAPL,GOOGL,AMZN\npython -m experiments.plot_single_agent_comparison\n```\n\n"
    report += "- [单Agent代码](../../agents/single_agent.py)\n- [实验协议](../../experiments/single_agent_protocol.json)\n"
    report += "- [绘图与校验代码](../../experiments/plot_single_agent_comparison.py)\n- [统一Notebook](../../analysis.ipynb)\n"
    report += "- [216条单Agent信号](../../data/decisions/deepseek-flash-single-shared-memory-2026jul-oct-v1.csv)\n"
    report += "- [全部五策略原始指标](../single_vs_multi_AAPL_GOOGL_AMZN/metrics.csv)\n"
    report += "- [三方法汇总CSV](comparison_metrics.csv)\n- [离线HTML报告](index.html)\n- [来源哈希与校验](provenance.json)\n"
    (output / "README.md").write_text(report, encoding="utf-8")
    table = summary[["ticker", "strategy_name", "return_pct", "max_drawdown_pct", "sharpe"]].copy()
    table.columns = ["股票", "方法", "收益 (%)", "最大回撤 (%)", "Sharpe"]
    svg = []
    for name in ("returns_drawdown_comparison", "equity_drawdown_three_stocks"):
        text = (output / f"{name}.svg").read_text()
        svg.append(text[text.index("<svg"):])
    page = '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    page += '<title>单Agent与多Agent实验结果</title><style>body{font:16px/1.7 system-ui,sans-serif;max-width:1200px;margin:32px auto;padding:0 24px;color:#222}h1{font-size:28px}h2{margin-top:32px}svg{width:100%;height:auto}table{border-collapse:collapse;width:100%}th,td{padding:8px 12px;border-bottom:1px solid #ddd;text-align:right}th:first-child,td:first-child{text-align:left}.note{color:#555}a{color:#145f95}</style>'
    page += '<h1>单Agent与多Agent实验结果</h1><p class="note">2026-07-01—10-09 · AAPL / GOOGL / AMZN · DeepSeek Flash · 归档结果整理于2026-11-19</p>'
    page += '<p>' + html.escape(conclusion) + '</p><h2>收益与最大回撤</h2>' + svg[0]
    page += '<h2>完整期间净值与回撤</h2>' + svg[1] + '<h2>可核对指标</h2>'
    page += table.to_html(index=False, border=0, float_format=lambda v: f"{v:.2f}")
    page += '<h2>实验口径与限制</h2><ul>' + ''.join('<li>' + html.escape(n) + '</li>' for n in notes) + '</ul>'
    page += '<h2>费用</h2><p>' + html.escape(billing) + '</p><p><a href="README.md">实验说明与代码入口</a> · <a href="comparison_metrics.csv">下载指标CSV</a></p></html>'
    (output / "index.html").write_text(page, encoding="utf-8")
    signal_file = ROOT / "data/decisions/deepseek-flash-single-shared-memory-2026jul-oct-v1.csv"
    signals = pd.read_csv(signal_file)
    if (len(signals) != 216 or signals.duplicated(["ticker", "information_cutoff"]).any()
            or signals.groupby("ticker").size().to_dict() != dict.fromkeys(TICKERS, 72)
            or not signals.source.eq("single_agent").all()
            or not signals.action.isin(["BUY", "SELL", "HOLD"]).all()):
        raise ValueError("Expected 216 unique, valid archived single-agent decisions")
    files = [source / "metrics.csv", source / "run.json", signal_file,
             ROOT / "experiments/single_agent_protocol.json",
             ROOT / "experiments/googl_amzn_single_live_20261109/cost_summary.json"] + [
        source / t / "agent_period" / s / "daily.csv" for t in TICKERS for s in STYLES]
    provenance = {"report_date": "2026-11-19", "model_calls": 0,
                  "validated_single_agent_decision_rows": 216,
                  "validated_daily_ledgers": 9, "return_intervals_per_ledger": 70,
                  "nav_reconciled": True, "drawdown_reconciled": True,
                  "performance_endpoint_is_return_end": True,
                  "metric_rows_in_source": 15, "metric_rows_in_overview": 9,
                  "drawdown_overview_sign": "positive loss magnitude; lower is better",
                  "source_hashes": {str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p):
                                    hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    (output / "provenance.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n")
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    print(build_report(args.input_dir, args.output_dir))


if __name__ == "__main__":
    main()
