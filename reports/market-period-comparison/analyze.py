"""Compare the proposed periods using cached prices; makes no model/API calls."""
from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
PERIODS = {
    '2024 Q1': ('2024-01-01', '2024-03-31'),
    '2026 Jul-Aug': ('2026-07-01', '2026-08-31'),
    '2026 development': ('2026-07-01', '2026-08-05'),
    '2026 holdout': ('2026-08-06', '2026-08-31'),
}

def tri(p):
    growth = (p.close + p.dividend) * p.split / p.close.shift(1)
    growth.iloc[0] = 1.
    return growth.cumprod() * p.close.iloc[0]

def read_stock(ticker, sources):
    p = ROOT / f'data/prices/{ticker}.csv'
    expected = sources['files'][f'prices/{ticker}.csv']['sha256']
    assert hashlib.sha256(p.read_bytes()).hexdigest() == expected
    return pd.read_csv(p)

def read_etf(ticker):
    raw = json.loads((OUT / f'{ticker}-yahoo.json').read_text())['chart']['result'][0]
    dates = pd.to_datetime(raw['timestamp'], unit='s', utc=True).tz_convert('America/New_York').strftime('%Y-%m-%d')
    frame = pd.DataFrame(raw['indicators']['quote'][0])
    frame['date'], frame['dividend'], frame['split'] = dates, 0., 1.
    for event in raw.get('events', {}).get('dividends', {}).values():
        d = pd.Timestamp(event['date'], unit='s', tz='UTC').tz_convert('America/New_York').strftime('%Y-%m-%d')
        frame.loc[frame.date == d, 'dividend'] += event['amount']
    assert not raw.get('events', {}).get('splits'), 'Review ETF split handling'
    return frame.dropna(subset=['close']).reset_index(drop=True)

def metrics(ticker, label, x):
    r = x.ret.to_numpy()
    nav = np.r_[1., np.cumprod(1+r)]
    return {
        'ticker': ticker, 'period': label, 'first_session': x.date.iloc[0],
        'last_session': x.date.iloc[-1], 'sessions': len(x),
        'total_return_pct': (nav[-1]-1)*100,
        'annualized_volatility_pct': np.std(r, ddof=0)*np.sqrt(252)*100,
        'max_drawdown_pct': (nav/np.maximum.accumulate(nav)-1).min()*100,
        'positive_day_pct': np.mean(r>0)*100,
        'largest_daily_gain_pct': max(r)*100,
        'largest_daily_loss_pct': min(r)*100,
        'trend_efficiency': abs(np.log(nav[-1]))/np.abs(np.log1p(r)).sum(),
    }, nav

def main():
    sources = json.loads((ROOT/'data/sources.json').read_text())
    frames = {t: read_stock(t, sources) for t in ['AAPL','GOOGL','AMZN']}
    frames.update({t: read_etf(t) for t in ['SPY','QQQ']})
    rows, curves = [], {}
    for ticker, p in frames.items():
        p['tri'] = tri(p)
        p['ret'] = p.tri.pct_change()
        assert p.date.is_unique and p.date.is_monotonic_increasing
        for label, (a,b) in PERIODS.items():
            x = p.loc[p.date.between(a,b)]
            assert len(x) == {'2024 Q1':61,'2026 Jul-Aug':43,'2026 development':25,'2026 holdout':18}[label]
            row, nav = metrics(ticker, label, x)
            rows.append(row); curves[ticker,label] = nav
        # Sensitivity: equal number of trading sessions, without changing formal dates.
        x = p.loc[p.date.between('2024-01-01','2024-03-31')].head(43)
        row, _ = metrics(ticker, '2024 first 43 sessions', x); rows.append(row)
    table = pd.DataFrame(rows)
    table.to_csv(OUT/'period_metrics.csv', index=False)
    (OUT/'period_metrics.json').write_text(table.to_json(orient='records', force_ascii=False, indent=2))
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
    fig, axes = plt.subplots(2,3, figsize=(15,8.2), constrained_layout=True)
    for ax, ticker in zip(axes.flat, ['AAPL','GOOGL','AMZN','SPY','QQQ']):
        for label, color, ls in [('2024 Q1','#265DAB','-'),('2026 Jul-Aug','#AD5B15','--')]:
            nav = curves[ticker,label]*100
            ret = table.loc[(table.ticker==ticker)&(table.period==label),'total_return_pct'].iloc[0]
            ax.plot(np.arange(len(nav)),nav,label=f'{label}: {ret:+.2f}%',color=color,ls=ls,lw=2)
        ax.axhline(100,color='0.65',lw=.7)
        ax.set_title(ticker,loc='left',fontweight='bold')
        ax.set_xlabel('Trading sessions from window start (day 0 = prior close)')
        ax.set_ylabel('Gross total-return index (start = 100)')
        ax.grid(axis='y',color='0.9',lw=.7);ax.legend(frameon=False,fontsize=9)
        ax.spines[['top','right']].set_visible(False)
    axes[1,2].axis('off')
    axes[1,2].text(0, .95,
        'Comparison conventions\n\n'
        '2024 Q1: 61 sessions\n2026 Jul-Aug: 43 sessions\n\n'
        'Close-to-close total returns, including dividends.\n'
        'Starting point: last close before each window.\n'
        'No trading fees or API cost.\n\n'
        'Sources: team Yahoo price cache (3 stocks);\n'
        'Yahoo chart API (SPY / QQQ).\n'
        'Comparison compiled: 2026-10-15.\n\n'
        'Descriptive market diagnostics only;\nnot Agent strategy performance.',va='top',fontsize=11,linespacing=1.45)
    fig.suptitle('The proposed windows have different stock-level trends and risk',fontsize=16,fontweight='bold')
    fig.savefig(OUT/'period-comparison.png',dpi=170)
    plt.close(fig)
    provenance = {'as_of':'2026-10-15','team_sources_manifest':'data/sources.json',
        'conventions':'Prior-session close to period-end close; forward-only dividend total return; no fees; vol sqrt(252), ddof=0; peak includes starting capital.',
        'yahoo_etf_urls': {t:f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1=1703808000&period2=1791777600&interval=1d&events=div%2Csplits&includeAdjustedClose=true' for t in ['SPY','QQQ']},
        'input_sha256': {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [*(ROOT/f'data/prices/{t}.csv' for t in ['AAPL','GOOGL','AMZN']),*(OUT/f'{t}-yahoo.json' for t in ['SPY','QQQ'])]}}
    (OUT/'provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2))
    print(table[['ticker','period','sessions','total_return_pct','annualized_volatility_pct','max_drawdown_pct']].round(2).to_string(index=False))

if __name__=='__main__':
    main()
