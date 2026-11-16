"""Audit and compare a complete original-flow fractional arm with its archive baseline."""
import argparse
import json
import os
os.environ.setdefault('MPLCONFIGDIR',str(__import__('pathlib').Path(__import__('tempfile').gettempdir()) / 'trading-matplotlib'))
import numpy as np
import pandas as pd
from experiments.full_position_pair import ROOT,OUT,ARCHIVE,util
from experiments.fixed_position_comparison import simulate,metrics
from agents.position_full_pipeline import STAGES,SizedPortfolioDecision,SIZING_RULES

def evaluate(group):
    protocol=util.read(OUT/'protocol.json');g=protocol['groups'][group];ticker=g['ticker'];days=g['signal_dates'];n=len(days)
    prices=pd.read_csv(ROOT/f'data/prices/{ticker}.csv');assert util.digest(ROOT/f'data/prices/{ticker}.csv')==g['prices_sha256']
    original=[];new=[];ratings=[];stage_ids=[]
    for day in days:
        cell=f'{group}_{day}';frozen=util.read(OUT/'inputs'/f'{cell}.json')
        assert util.digest(OUT/'inputs'/f'{cell}.json')==g['sources'][day]['input_sha256']
        assert util.digest(ARCHIVE/f'results/{ticker}/TradingAgentsStrategy_logs/full_states_log_{day}.json')==g['sources'][day]['archive_sha256']
        d=util.read(OUT/'decisions'/f'{cell}.json');final=SizedPortfolioDecision.model_validate(d['final'])
        new.append(final.target_weight_now)
        original.append({'Buy':1.,'Overweight':1.,'Hold':None,'Underweight':0.,'Sell':0.}[frozen['original_rating']])
        ratings.append(dict(day=day,old=frozen['original_rating'],new=final.rating.value,target=final.target_weight_now))
        for stage,_ in STAGES:
            identity=f'{cell}_{stage}';stage_ids.append(identity)
            prompt=util.read(OUT/'prompts'/f'{identity}.json');saved=util.read(OUT/'calls'/f'{identity}.json')
            assert util.sha_text(json.dumps(prompt,sort_keys=True,ensure_ascii=False))==saved['prompt_sha256']
            assert SIZING_RULES in prompt[0]['content']
            assert json.dumps(d['account_before'],ensure_ascii=False) in prompt[0]['content']
        risk=util.read(OUT/'stages'/f'{cell}_neutral.json')['risk_debate_state']
        assert risk['count']==3
        pm_prompt=str(util.read(OUT/'prompts'/f'{cell}_portfolio.json'))
        for label in ['Aggressive Analyst:','Conservative Analyst:','Neutral Analyst:']:assert label in pm_prompt
    rows=simulate(prices,days,new);saved=pd.read_csv(OUT/f'trades_{group}.csv');assert len(saved)==n
    for col in ['equity','actual_weight','trading_cost']:np.testing.assert_allclose(saved[col],[r[col] for r in rows],rtol=1e-11,atol=1e-8)
    oldrows=simulate(prices,days,original);hold=simulate(prices,days,[1.]+[None]*(n-1))
    result=dict(group=group,metrics={'原版全仓买卖':metrics(oldrows),'完整流程比例买卖':metrics(rows),'Buy & Hold':metrics(hold)},
        daily_ratings=ratings,verified_days=n,verified_downstream_stages=len(stage_ids),
        limitation=protocol['limitation'],comparison='Same archived analyst reports, one-round bull/bear debate and original six downstream role functions. New arm adds real account context and continuous final execution target; archived baseline is not freshly rerun.')
    calls=[json.loads(s) for s in (OUT/'api_calls.jsonl').read_text().splitlines()]
    ours=[r for r in calls if r['cell'].startswith(group+'_')]
    result['billing']=dict(selected_group_calls=len(ours),selected_group_failures=sum(r['status']!='success' for r in ours),
        selected_group_estimated_cny=sum(r.get('estimated_cny',0) for r in ours),
        other_group_recorded_estimated_cny=sum(r.get('estimated_cny',0) for r in calls if r not in ours),
        note='Interrupted in-flight calls before scope reduction may incur delayed charges absent from completed-call ledger.')
    folder=OUT/'comparisons'/group;folder.mkdir(parents=True,exist_ok=True)
    util.save(folder/'report.json',result);pd.DataFrame(result['metrics']).T.to_csv(folder/'metrics.csv')
    pd.DataFrame(oldrows).to_csv(folder/'original_binary_trades.csv',index=False)
    plot(folder,g,result,oldrows,rows,hold)
    print(json.dumps({k:v for k,v in result.items() if k!='daily_ratings'},ensure_ascii=False,indent=2))
    return result

def plot(folder,g,result,oldrows,rows,hold):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    font=font_manager.FontProperties(family=['Noto Sans CJK SC','Microsoft YaHei','STHeiti','DejaVu Sans'])
    plt.rcParams.update({'font.family':font.get_name(),'axes.unicode_minus':False,'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(2,1,figsize=(12,8.5),gridspec_kw={'height_ratios':[2,1]},sharex=True)
    for ledger,label,color,ls in [(oldrows,'原版全仓买卖','#287398','-'),(rows,'完整流程比例买卖','#C87532','-'),(hold,'Buy & Hold','#ABB2B8','--')]:
        nav=np.r_[0,[r['equity']/1000-100 for r in ledger]]
        axes[0].plot(range(len(nav)),nav,color=color,ls=ls,lw=2,label=f"{label} {result['metrics'][label]['total_return']:+.2%}")
        if label!='Buy & Hold':axes[1].step(range(1,len(ledger)+1),[r['actual_weight']*100 for r in ledger],color=color,where='post',lw=2,label=label)
    axes[0].set_ylabel('累计净收益（%）');axes[1].set_ylabel('成交后仓位（%）');axes[1].set_ylim(-3,103)
    axes[1].set_xlabel('交易期序号（最后一期包含次月首个开盘清仓）')
    for ax in axes:ax.grid(axis='y',alpha=.2);ax.legend(frameon=False)
    fig.suptitle(f"{g['ticker']} 2026 年 {int(g['month'])} 月｜完整流程：全仓买卖 vs 比例买卖",fontsize=20)
    fig.subplots_adjust(left=.09,right=.97,top=.9,bottom=.19,hspace=.15)
    fig.text(.09,.10,'两者均含研究经理 → 交易员 → 激进／保守／中立风险审核 → 最终组合经理；复用相同原版分析与一轮辩论。',fontsize=9.5)
    fig.text(.09,.065,'初始 $100,000；次日开盘执行，成交手续费 0.10%；原版使用归档决策，新版重新调用模型，并非同批次随机对照。',fontsize=9.5)
    fig.savefig(folder/'comparison.png',dpi=180);fig.savefig(folder/'comparison.pdf');plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--group',default='AAPL_08');evaluate(p.parse_args().group)
