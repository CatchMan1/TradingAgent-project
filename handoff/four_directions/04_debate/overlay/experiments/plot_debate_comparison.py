"""Offline figure: paired debate experiment versus matched buy-and-hold."""
import os
os.environ.setdefault('MPLCONFIGDIR', str(__import__('pathlib').Path(__import__('tempfile').gettempdir()) / 'trading-matplotlib'))
import hashlib
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import font_manager
import numpy as np
import pandas as pd
from experiments.optimization_engine import simulate

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/debate_aapl_sep2026_paired'

def main():
    protocol = json.loads((OUT / 'protocol.json').read_text())
    report = json.loads((OUT / 'report.json').read_text())
    assert not report['missing'], 'Complete both arms before plotting'
    price_path = ROOT / 'data/prices/AAPL.csv'
    assert hashlib.sha256(price_path.read_bytes()).hexdigest() == protocol['data_sha256']['prices']
    prices = pd.read_csv(price_path)
    days = protocol['signal_dates']
    ratings = {day: ('Buy' if i == 0 else 'Hold') for i, day in enumerate(days)}
    hold, hold_metrics = simulate(prices, ratings, protocol['start'], protocol['end'],
                                  fee_bps=protocol['fee_bps'], initial_cash=protocol['initial_cash'])
    frames = [hold, pd.read_csv(OUT / 'trades_r1.csv'), pd.read_csv(OUT / 'trades_r3.csv')]
    metrics = [hold_metrics, *report['metrics']]
    labels = ['Buy & Hold', '一轮辩论', '三轮辩论']
    colors = ['#667580', '#126B91', '#CE7831']
    dates = pd.to_datetime([protocol['start'], *hold.valuation_date])
    for f, m in zip(frames, metrics):
        assert f.valuation_date.tolist() == hold.valuation_date.tolist()
        assert np.isclose(f.equity.iloc[-1] / protocol['initial_cash'] - 1, m['total_return'])
    font = font_manager.FontProperties(family=['Noto Sans CJK SC','Microsoft YaHei','STHeiti','DejaVu Sans'])
    plt.rcParams.update({'font.family': font.get_name(), 'axes.unicode_minus': False,
                         'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False,
                         'axes.spines.left': False, 'axes.edgecolor': '#D7DCE0',
                         'text.color': '#202D36', 'axes.labelcolor': '#46545F',
                         'xtick.color': '#62717A', 'ytick.color': '#62717A'})
    fig = plt.figure(figsize=(13.6, 9.5), facecolor='white')
    grid = fig.add_gridspec(2, 2, height_ratios=[2.3, 1], left=.075, right=.955,
                           top=.84, bottom=.18, hspace=.50, wspace=.28)
    ax = fig.add_subplot(grid[0, :])
    for f, m, label, color in zip(frames, metrics, labels, colors):
        nav = np.r_[100., f.equity.to_numpy() / protocol['initial_cash'] * 100]
        ax.plot(dates, nav, lw=2.6, color=color, label=f"{label}  {m['total_return']:+.2%}")
        ax.scatter(dates[-1], nav[-1], s=32, color=color, zorder=4)
    ax.axhline(100, color='#AAB4BB', lw=.8, linestyle='--')
    ax.grid(axis='y', color='#E8ECEF', lw=.8)
    ax.set_axisbelow(True)
    ax.set_ylabel('账户净值（初始 = 100）', labelpad=10)
    ax.set_xlabel('估值日期（开盘价）', labelpad=8)
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.TU))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    ax.set_xlim(dates[0] - pd.Timedelta(days=.5), dates[-1] + pd.Timedelta(days=1))
    ax.legend(frameon=False, loc='upper left', ncol=3, fontsize=10.5)
    ax.tick_params(length=0)
    for col, (key, title, negate) in enumerate([
        ('total_return', '区间净收益（%，越高越好）', False),
        ('max_drawdown', '最大回撤幅度（%，越低越好）', True),
    ]):
        sub = fig.add_subplot(grid[1, col])
        vals = [m[key] * (-100 if negate else 100) for m in metrics]
        sub.bar(labels, vals, color=colors, width=.5, zorder=3)
        sub.axhline(0, color='#AAB4BB', lw=.8)
        sub.grid(axis='y', color='#E8ECEF')
        sub.set_title(title, loc='left', fontsize=12, pad=17)
        sub.set_ylabel('%')
        sub.set_ylim(min(0, min(vals)) - .15, max(vals) * 1.30 + .1)
        sub.tick_params(length=0)
        for i, value in enumerate(vals):
            sub.annotate(f'{value:+.2f}%' if not negate else f'{value:.2f}%',
                         (i, value), xytext=(0, 6), textcoords='offset points',
                         ha='center', fontsize=12, fontweight='bold')
    fig.text(.075, .945, 'AAPL｜买入持有与辩论轮数对照', fontsize=23, weight='bold')
    fig.text(.075, .902, '2026 年 9 月 · 21 个交易日 · 同一初始资金与成交费用', fontsize=12, color='#62717A')
    fig.text(.075, .105, '口径：初始资金 $100,000；9 月 1 日开盘开始，10 月 1 日开盘清仓估值；每次成交收取 0.10% 费用。', fontsize=10)
    fig.text(.075, .078, 'Buy & Hold 首日买入后持有至期末；辩论策略按前一交易日信号执行。曲线已扣交易费用，不扣 API 费用。', fontsize=10)
    fig.text(.075, .051, '来源：本项目冻结行情与一轮 / 三轮实测决策。仅单股单月的一次实验，结果不代表普遍表现。', fontsize=9.5, color='#62717A')
    fig.savefig(OUT / 'buy_hold_debate_comparison.png', dpi=180, facecolor='white')
    fig.savefig(OUT / 'buy_hold_debate_comparison.pdf', facecolor='white')
    plt.close(fig)
    (OUT / 'buy_hold_comparison.json').write_text(json.dumps({
        'method': 'Same simulator, dates, initial cash, and 10 bps turnover fee; buy first session and hold to terminal liquidation.',
        'strategies': {label: m for label, m in zip(labels, metrics)},
        'valuation_dates': [d.strftime('%Y-%m-%d') for d in dates],
        'normalized_nav': {label: [100., *(f.equity / protocol['initial_cash'] * 100).tolist()]
                           for label, f in zip(labels, frames)},
    }, ensure_ascii=False, indent=2))
    print(json.dumps({label: m for label, m in zip(labels, metrics)}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
