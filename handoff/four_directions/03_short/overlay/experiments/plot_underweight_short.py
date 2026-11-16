"""Offline archived-signal comparison; no API calls."""
import json,hashlib,argparse
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as md
from matplotlib.font_manager import FontProperties
from experiments.optimization_engine import simulate
parser=argparse.ArgumentParser();parser.add_argument('--ticker',choices=['AAPL','AMZN','GOOGL'],default='AAPL');T=parser.parse_args().ticker
R=Path(__file__).resolve().parents[1];O=R/f'results/underweight_short_{T.lower()}_jul_oct2026';O.mkdir(exist_ok=True)
A=R/f'agents/logs/e/f6e0d4240635/results/{T}/TradingAgentsStrategy_logs'
ratings={}; hashes={}
for f in sorted(A.glob('full_states_log_*.json')):
 s=json.loads(f.read_text());assert s['run_settings']['max_debate_rounds']==1 and not s.get('sentiment_report');ratings[f.stem[-10:]]=s['final_rating'];hashes[f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
p=pd.read_csv(R/f'data/prices/{T}.csv').sort_values('date').reset_index(drop=True)
plt.rcParams.update({'axes.unicode_minus':False,'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
from matplotlib import font_manager
for candidate in ['Noto Sans CJK SC','Microsoft YaHei','PingFang SC','STHeiti','SimHei']:
 if candidate in {f.name for f in font_manager.fontManager.ttflist}:
  plt.rcParams['font.family']=candidate;break
names=['原版：减持清仓','减持改为满仓做空','买入并持有'];colors=['#2864ad','#cf5c36','#7c8794'];keys=['original','underweight_short','buy_hold'];frames={};periods={}
for k,start,end in [('07','2026-07-01','2026-07-31'),('08','2026-08-01','2026-08-31'),('09','2026-09-01','2026-09-30'),('10','2026-10-01',p.iloc[-2].date),('combined','2026-07-01',p.iloc[-2].date)]:
 ix=p.index[(p.date>=start)&(p.date<=end)];days=[p.iloc[i-1].date for i in ix];assert all(d in ratings for d in days)
 mapped={d:'Sell' if r=='Underweight' else r for d,r in ratings.items()};bh={d:'Buy' if i==0 else 'Hold' for i,d in enumerate(days)};frames[k]=[];metrics={}
 for name,rs,short in zip(keys,[ratings,mapped,bh],[False,True,False]):
  f,m=simulate(p,rs,start,end,short=short);f['original_rating']=f.signal_date.map(ratings);f.to_csv(O/f'{k}_{name}.csv',index=False);frames[k].append(f);metrics[name]=m
 periods[k]={'start':frames[k][0].execution_date.iloc[0],'last_execution':frames[k][0].execution_date.iloc[-1],'liquidation':frames[k][0].valuation_date.iloc[-1],'partial':k=='10','underweight_signals':sum(ratings[d]=='Underweight' for d in days),'metrics':metrics}
report={'source':str(A),'source_hashes':hashes,'prices_sha256':hashlib.sha256((R/f'data/prices/{T}.csv').read_bytes()).hexdigest(),'new_api_calls':0,'api_cost_cny':0,'assumptions':{'fee_bps':10,'borrow_apr':.03,'initial_cash':100000,'hold':'Preserve shares including shorts','execution':'Prior session signal, next open execution; liquidate next open after final execution','limitations':'Assumes available borrowing; no intraday margin, recall, slippage, cash interest. October partial.'},'periods':periods};(O/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
def lines(ax,k):
 for f,n,c in zip(frames[k],names,colors):ax.plot(pd.to_datetime([f.execution_date.iloc[0],*f.valuation_date]),np.r_[0,(f.equity.to_numpy()/100000-1)*100],label=n,color=c,lw=2)
 ax.axhline(0,color='#bbbbbb',lw=.6);ax.set_ylabel('累计净收益（%）');ax.set_xlabel('估值日期（2026年）');ax.grid(alpha=.16);ax.xaxis.set_major_formatter(md.DateFormatter('%m-%d'))
fig,axes=plt.subplots(2,2,figsize=(15,10))
for ax,k,title in zip(axes.flat,['07','08','09','10'],['7月','8月','9月','10月部分：10/1–10/8交易，10/9结算']):
 lines(ax,k);ms=periods[k]['metrics'];ax.set_title(title+'\n原版 {:+.2f}% | 做空 {:+.2f}% | 持有 {:+.2f}%'.format(*[ms[n]['total_return']*100 for n in keys]),fontsize=12)
h,l=axes[0,0].get_legend_handles_labels();fig.legend(h,l,loc='upper center',bbox_to_anchor=(.5,.945),ncol=3,frameon=False);fig.suptitle(T+'｜每月独立回测：Underweight 改为满仓做空',fontsize=19,y=.985)
fig.text(.06,.025,'每月从10万美元现金开始；Hold延续现有多头或空头。单边交易费0.1%，借券年费3%，含股息补偿。\n来源：原版存档决策＋项目行情；次日开盘执行，月末下一交易日开盘平仓；十月不是整月。',fontsize=10,color='#555555');fig.tight_layout(rect=(0,.075,1,.90));fig.savefig(O/'monthly_comparison.png',dpi=160);plt.close(fig)
fig,(ax,dd)=plt.subplots(2,1,figsize=(15,9),gridspec_kw={'height_ratios':[2,1]});lines(ax,'combined');ax.legend(frameon=False,ncol=3);ax.set_title(T+'｜连续账户：2026/7/1—10/9估值（十月不完整）',fontsize=18)
for f,n,c in zip(frames['combined'],names,colors):
 v=np.r_[100000,f.equity];dd.plot(pd.to_datetime([f.execution_date.iloc[0],*f.valuation_date]),(v/np.maximum.accumulate(v)-1)*100,label=n,color=c,lw=1.7)
dd.set_ylabel('回撤（%）');dd.set_xlabel('估值日期（2026年）');dd.xaxis.set_major_formatter(md.DateFormatter('%m-%d'));dd.grid(alpha=.16)
fig.text(.06,.02,'连续账户不按月重置或强制平仓；不能用独立月度收益直接相加替代。原版历史报告不变，仅改减持交易映射。\n来源：原版存档＋项目行情。交易费0.1%，借券年费3%；API调用0次。未模拟盘中强平、借券召回和滑点。',fontsize=10,color='#555555');fig.tight_layout(rect=(0,.08,1,1));fig.savefig(O/'continuous_comparison.png',dpi=160);plt.close(fig)
rows=''
for k,q in periods.items():
 label={'07':'7月','08':'8月','09':'9月','10':'10月（部分）','combined':'连续账户'}[k]
 rows+='<tr><th>'+label+'</th>'+''.join(f'<td>{q["metrics"][n]["total_return"]:+.2%}<br><small>最大回撤 {abs(q["metrics"][n]["max_drawdown"]):.2%}</small></td>' for n in keys)+f'<td><a href="{k}_underweight_short.csv">逐日交易</a></td></tr>'
html=('''<!doctype html><meta charset="utf-8"><title>AAPL 减持改做空</title><style>body{font:16px system-ui;max-width:1300px;margin:40px auto;padding:0 24px;color:#243040}img{width:100%}table{border-collapse:collapse;width:100%}td,th{padding:14px;text-align:left;border-bottom:1px solid #ddd}small,p{color:#566272}a{color:#2864ad}</style><h1>AAPL：原版减持改为满仓做空</h1><p>2026年7—9月完整；10月仅10月1—8日交易、10月9日开盘结算。未调用API。</p><img src="monthly_comparison.png"><table><tr><th>区间</th><th>原版</th><th>减持→做空</th><th>买入并持有</th><th>明细</th></tr>'''+rows+'''</table><img src="continuous_comparison.png"><p>每月独立账户与连续账户分别计算。Underweight→−100%；Buy/Overweight→+100%；Hold保持现有股数，包括空头。原始报告未重写，无情绪模块、无比例仓位。</p><p>10万美元初始资金；单边交易费0.1%；借券年费3%；计入股息补偿。假设借券可用，不模拟盘中强平、借券召回及滑点。</p><a href="report.json">完整指标及来源哈希</a>''')
(O/'comparison.html').write_text(html.replace('AAPL',T))
print(json.dumps({k:{n:{x:round(m[x]*100,3) for x in ['total_return','max_drawdown']} for n,m in q['metrics'].items()} for k,q in periods.items()},ensure_ascii=False,indent=2))
