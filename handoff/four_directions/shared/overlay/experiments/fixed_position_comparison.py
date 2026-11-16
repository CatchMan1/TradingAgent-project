"""Offline exposure controls. No model clients or network dependencies."""
from pathlib import Path
import hashlib
import json
import os
os.environ.setdefault('MPLCONFIGDIR', str(__import__('pathlib').Path(__import__('tempfile').gettempdir()) / 'trading-matplotlib'))
import numpy as np
import pandas as pd
from experiments.position_account import Account, execute_interval, metrics

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'results/position_aapl_sep2026'
OUT = SOURCE/'fixed_position_controls'

def read(path):
    return json.loads(path.read_text())

def decision(weight):
    return dict(action='keep_shares' if weight is None else 'rebalance', target_weight_now=weight,
                **{k:'Offline benchmark' for k in ['rationale','why_change_from_current','increase_condition','reduce_condition']})

def simulate(prices, dates, targets):
    account = Account()
    indices = {r.date:i for i,r in prices.iterrows()}
    return [execute_interval(account, decision(w), day, prices.iloc[indices[day]+1],
                prices.iloc[indices[day]+2], terminal=j==len(dates)-1)
            for j,(day,w) in enumerate(zip(dates, targets, strict=True))]

def main():
    OUT.mkdir(exist_ok=True)
    protocol=read(SOURCE/'protocol.json')
    path=ROOT/'data/prices/AAPL.csv'
    assert hashlib.sha256(path.read_bytes()).hexdigest()==protocol['data_sha256']['prices']
    prices=pd.read_csv(path); dates=protocol['signal_dates']; n=len(dates)
    results={}; ledgers={}
    def add(key, targets, **metadata):
        rows=simulate(prices,dates,targets)
        ledgers[key]=rows
        results[key]=dict(**metadata,**metrics(rows))
        pd.DataFrame(rows).to_csv(OUT/f'{key}.csv',index=False)
        return results[key]
    for w in [.10,.15,.30,.50,.70,1.]:
        add(f'passive_{int(w*100)}',[w]+[None]*(n-1),initial_weight=w,kind='initial allocation, hold shares')
        add(f'daily_{int(w*100)}',[w]*n,target_weight=w,kind='daily constant-weight rebalance')
    attribution={}
    for rounds in [1,3]:
        old=pd.read_csv(SOURCE/f'trades_r{rounds}.csv')
        targets=[None if pd.isna(w) else float(w) for w in old.target_weight]
        a=add(f'actual_r{rounds}',targets,kind='saved manager decisions')
        replay=pd.DataFrame(ledgers[f'actual_r{rounds}'])
        for col in ['equity','actual_weight','trading_cost','shares_after_execution']:
            np.testing.assert_allclose(replay[col],old[col],rtol=1e-11,atol=1e-8)
        # Retrospective diagnostic matching; not an ex-ante investable policy.
        lo,hi=0.,1.
        for _ in range(50):
            mid=(lo+hi)/2
            exposure=metrics(simulate(prices,dates,[mid]+[None]*(n-1)))['mean_exposure']
            if exposure<a['mean_exposure']:lo=mid
            else:hi=mid
        w=(lo+hi)/2
        b=add(f'matched_passive_r{rounds}',[w]+[None]*(n-1),initial_weight=w,kind='ex-post matched mean execution weight')
        assert abs(a['mean_exposure']-b['mean_exposure'])<1e-12
        c=add(f'matched_daily_r{rounds}',[a['mean_exposure']]*n,target_weight=a['mean_exposure'],kind='ex-post matched daily weight')
        gap=a['final_equity']-b['final_equity']
        extra_fee=a['trading_cost']-b['trading_cost']
        attribution[f'r{rounds}']=dict(net_pnl_difference_usd=gap,
            net_return_difference_percentage_points=gap/1000,
            extra_fees_usd=extra_fee,
            price_and_dividend_pnl_difference_usd=gap+extra_fee,
            daily_control_return_difference_percentage_points=100*(a['total_return']-c['total_return']))
    np.testing.assert_allclose([r['equity'] for r in ledgers['actual_r1']],
                               [r['equity'] for r in ledgers['passive_15']],atol=1e-8)
    hold=read(ROOT/'results/debate_aapl_sep2026_paired/buy_hold_comparison.json')['strategies']['Buy & Hold']
    assert abs(results['passive_100']['total_return']-hold['total_return'])<1e-12
    report=dict(api_calls=0,api_cost_cny=0,execution_start='2026-09-01',liquidation='2026-10-01 open',
        initial_cash=100000,fee_bps=10,cash_interest=0,
        exposure_definition='Arithmetic mean of 21 post-trade opening equity weights; not time/volatility-weighted.',
        limitations=['Matched controls use realized monthly exposure for retrospective diagnosis only.',
          'One stock/month; matched average exposure does not imply matched risk.',
          'Same saved market data and fee/execution assumptions as original; no new data verification.'],
        metrics=results,attribution=attribution,validation='Both actual trajectories replayed; one-round equals passive 15%; 100% equals prior Buy & Hold; mean exposures matched to 1e-12.')
    (OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    pd.DataFrame(results).T.to_csv(OUT/'metrics.csv',index_label='strategy')
    plot(results,ledgers)
    print(json.dumps(dict(metrics=results,attribution=attribution),ensure_ascii=False,indent=2))

def plot(results,ledgers):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    font=font_manager.FontProperties(family=['Noto Sans CJK SC','Microsoft YaHei','STHeiti','DejaVu Sans'])
    plt.rcParams.update({'font.family':font.get_name(),'axes.unicode_minus':False,'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(1,3,figsize=(17,6.5),gridspec_kw={'width_ratios':[1.1,1,1]})
    weights=[10,15,30,50,70,100]
    ax=axes[0]
    bars=ax.bar(range(6),[results[f'passive_{w}']['total_return']*100 for w in weights],color='#8699A5')
    for bar,w in zip(bars,weights):
        ax.text(bar.get_x()+bar.get_width()/2,bar.get_height()+.06,f'{bar.get_height():.3f}%',ha='center',fontsize=10)
    ax.set_xticks(range(6),[f'{w}%' for w in weights]);ax.set_ylim(0,4.5)
    ax.set_xlabel('月初投入比例（之后保持股数）');ax.set_ylabel('整月净收益（%）');ax.set_title('仓位增大，收益随之增大',loc='left')
    for ax,r in zip(axes[1:],[1,3]):
        for key,label,color,ls in [(f'matched_passive_r{r}','同平均仓位：买入持有','#617D8B','--'),(f'matched_daily_r{r}','同平均仓位：每日再平衡','#A6AEB4',':'),(f'actual_r{r}','实际经理决策','#D17A32','-')]:
            nav=np.r_[0,[row['equity']/1000-100 for row in ledgers[key]]]
            ax.plot(range(len(nav)),nav,label=f'{label} {nav[-1]:.3f}%',color=color,ls=ls,lw=2.2)
        ax.set_title(f'{r} 轮｜匹配平均仓位 {results[f"actual_r{r}"]["mean_exposure"]:.2%}',loc='left')
        ax.set_xlabel('估值序号（0 = 初始，21 = 清仓）');ax.set_ylabel('累计净收益（%）')
        ax.legend(fontsize=8,frameon=False,loc='upper left')
    bounds=[ax.get_ylim() for ax in axes[1:]]
    for ax in axes[1:]:ax.set_ylim(min(v[0] for v in bounds),max(v[1] for v in bounds)+.12)
    for ax in axes:ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True)
    fig.suptitle('AAPL 2026 年 9 月｜低仓位与动态调仓的效果分开看',fontsize=21,x=.06,ha='left',y=.97)
    fig.subplots_adjust(left=.06,right=.98,top=.80,bottom=.25,wspace=.30)
    fig.text(.06,.13,'统一口径：初始 $100,000；9 月 1 日开盘开始，10 月 1 日开盘清仓；交易费用 0.10%；现金不计息。',fontsize=10)
    fig.text(.06,.08,'同平均仓位为事后归因对照；匹配 21 个开盘成交后仓位的算术平均值，不代表风险完全相同。全部使用已有数据，API 费用 ¥0。',fontsize=9)
    fig.savefig(OUT/'fixed_position_comparison.png',dpi=180)
    fig.savefig(OUT/'fixed_position_comparison.pdf')
    plt.close(fig)

if __name__=='__main__':main()
