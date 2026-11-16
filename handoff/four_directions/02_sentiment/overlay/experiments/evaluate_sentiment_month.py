"""Offline audit and viewer: sentiment run versus the archived original strategy."""
import json
import argparse
from datetime import datetime
from html import escape
import os
os.environ.setdefault('MPLCONFIGDIR',str(__import__('pathlib').Path(__import__('tempfile').gettempdir()) / 'trading-matplotlib'))
import numpy as np
import pandas as pd
from agents.historical_sentiment import summarize,NewsSentimentBatch
from experiments.run_sentiment_month import ARCHIVED_OUT as OUT,base
from experiments.fixed_position_comparison import simulate,metrics

def main():
    global OUT
    ap=argparse.ArgumentParser();ap.add_argument('--original-prompts',action='store_true');args=ap.parse_args()
    if args.original_prompts:
        from experiments.run_sentiment_month import OUT as corrected_out
        OUT=corrected_out
    p=base.util.read(OUT/'protocol.json');days=p['signal_dates'];rows={};reports={};audited=0
    prices=pd.read_csv(base.ROOT/'data/prices/AAPL.csv')
    assert base.util.digest(base.ROOT/'data/prices/AAPL.csv')==p['prices_sha256']
    for arm in ['sentiment']:
        targets=[];reports[arm]=[]
        for day in days:
            f=OUT/'inputs'/f'{day}.json';assert base.util.digest(f)==p['input_hashes'][day]
            payload=base.util.read(f);d=base.util.read(OUT/'decisions'/f'{arm}_{day}.json')
            assert d['trade_date']==day and d['company_of_interest']=='AAPL'
            assert d['investment_debate_state']['count']==2 and d['risk_debate_state']['count']==3
            for key,value in payload['reports'].items():assert d[key]==value
            if arm=='baseline':assert d['sentiment_report']==''
            else:
                sentiment=json.loads(d['sentiment_report'])
                assert summarize(payload['bundle'],NewsSentimentBatch(items=sentiment['items']))==sentiment
                if args.original_prompts:
                    reuse=base.util.read(OUT/'reuse'/f'{day}.json')
                    source=__import__('pathlib').Path(reuse['source'])
                    assert base.util.digest(source)==reuse['source_sha256']
                    assert json.loads(base.util.read(source)['sentiment_report'])==sentiment
            for stage in (['sentiment'] if arm=='sentiment' else [])+['bull','bear','research','trader','aggressive','conservative','neutral','portfolio']:
                identity=f'{arm}_{day}_{stage}';prompt=base.util.read(OUT/'prompts'/f'{identity}.json');call=base.util.read(OUT/'calls'/f'{identity}.json')
                assert base.util.sha_text(json.dumps(prompt,sort_keys=True,ensure_ascii=False))==call['prompt_sha256']
                recovery=call.get('recovery')
                if isinstance(recovery,dict) and 'old_id' in recovery:
                    rawpath=OUT/'responses'/f"{identity}_{call['call_id']}.json"
                    assert base.util.digest(rawpath)==recovery['raw_response_sha256']
                    original=json.loads(base.util.read(rawpath)['choices'][0]['message']['content'])
                    changed=0
                    for item in original['items']:
                        if item['article_id']==recovery['old_id']:
                            item['article_id']=recovery['new_id'];changed+=1
                    assert changed==1 and original==json.loads(call['content'])
                audited+=1
            targets.append({'Buy':1.,'Overweight':1.,'Hold':None,'Underweight':0.,'Sell':0.}[d['final_rating']]);reports[arm].append(d)
        rows[arm]=simulate(prices,days,targets)
        saved=pd.read_csv(OUT/f'trades_{arm}.csv')
        for col in ['equity','actual_weight','trading_cost']:
            np.testing.assert_allclose(saved[col],[r[col] for r in rows[arm]],rtol=1e-11,atol=1e-8)
    rows['buy_hold']=simulate(prices,days,[1.]+[None]*(len(days)-1))
    archive=base.ROOT/'results/full_pipeline_position_2026aug_sep/comparisons/AAPL_08/original_binary_trades.csv'
    rows['baseline']=pd.read_csv(archive).to_dict('records')
    reports['baseline']=[base.util.read(base.ARCHIVE/f'results/AAPL/TradingAgentsStrategy_logs/full_states_log_{day}.json') for day in days]
    calls=[json.loads(x) for x in (OUT/'api_calls.jsonl').read_text().splitlines()]
    start=base.util.read(OUT/'balance_start.json');end=base.util.read(OUT/'balance_end.json')
    result=dict(metrics={k:metrics(v) for k,v in rows.items()},verified_days=len(days),verified_stages=audited,
        billing=dict(calls=len(calls),failures=sum(x['status']!='success' for x in calls),estimated_cny=sum(x.get('estimated_cny',0) for x in calls),
        by_arm={a:sum(x.get('estimated_cny',0) for x in calls if x['cell'].startswith(a+'_')) for a in p['arms']},balance=end),
        elapsed_minutes=(datetime.fromisoformat(end['queried_at_utc'])-datetime.fromisoformat(start['queried_at_utc'])).total_seconds()/60,
        rating_changes=sum(a['final_rating']!=b['final_rating'] for a,b in zip(reports['baseline'],reports['sentiment'])),
        exposure_changes=sum(abs(a['actual_weight']-b['actual_weight'])>1e-6 for a,b in zip(rows['baseline'],rows['sentiment'])),
        limitation=('Original native model client and full original risk prompts; only added sentiment report. Separate stochastic invocation batch, historical archived baseline, retrospective news, one stock-month.' if args.original_prompts else 'Historical superseded run: extra binary execution mandate and compact risk review confound sentiment attribution.'))
    folder=OUT/'comparison';folder.mkdir(exist_ok=True);base.util.save(folder/'report.json',result)
    plot(folder,rows,result);viewer(folder,days,rows,reports,result)
    print(json.dumps(result,ensure_ascii=False,indent=2))

def plot(folder,rows,result):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    font=font_manager.FontProperties(family=['Noto Sans CJK SC','Microsoft YaHei','STHeiti','DejaVu Sans'])
    plt.rcParams.update({'font.family':font.get_name(),'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(2,1,figsize=(12,8),sharex=True,gridspec_kw={'height_ratios':[2,1]})
    names={'baseline':'原版历史策略（无情绪）','sentiment':'本次实验：加入情绪','archive':'原版历史结果（参考）','buy_hold':'Buy & Hold'}
    for key,color,style in [('baseline','#287398','-'),('sentiment','#C87532','-'),('archive','#808080','--'),('buy_hold','#B8BDC0',':')]:
        if key not in rows:continue
        ledger=rows[key];nav=np.r_[0,[r['equity']/1000-100 for r in ledger]]
        axes[0].plot(range(len(nav)),nav,color=color,ls=style,lw=2,label=f"{names[key]} {result['metrics'][key]['total_return']:+.2%}")
        if key in ['baseline','sentiment']:axes[1].step(range(1,len(ledger)+1),[r['actual_weight']*100 for r in ledger],where='post',color=color,lw=2,label=names[key])
    axes[0].set_ylabel('累计净收益（%）');axes[1].set_ylabel('成交后仓位（%）');axes[1].set_xlabel('交易期序号（末期包含 9 月 1 日开盘清仓）')
    for ax in axes:ax.grid(axis='y',alpha=.2);ax.legend(frameon=False,fontsize=10)
    fig.suptitle('AAPL 2026 年八月｜加入新闻情绪与原版历史结果比较',fontsize=20)
    fig.subplots_adjust(left=.09,right=.97,top=.90,bottom=.19,hspace=.15)
    fig.text(.09,.10,('均为原始完整风险审核、一轮辩论、全仓买卖；只新增情绪报告；手续费 0.10%。' if OUT.name.endswith('original_prompts') else '历史实验含额外执行提示词及简短风险审核；不能归因于情绪；手续费 0.10%。'),fontsize=10)
    fig.text(.09,.065,'复用历史分析报告；新闻情绪来自归档标题与摘要。单个股票月份、模型随机性，不能据此外推。',fontsize=10)
    fig.savefig(folder/'comparison.png',dpi=180);fig.savefig(folder/'comparison.pdf');plt.close(fig)

def viewer(folder,days,rows,reports,result):
    names={'baseline':'原版历史策略（无情绪）','sentiment':'加入情绪（本次实验）','archive':'原版历史结果（参考）','buy_hold':'Buy & Hold'}
    metricrows=''.join('<tr><td>'+names[k]+'</td>'+''.join(f'<td>{v:.2%}</td>' for v in [m['total_return'],abs(m['max_drawdown']),m['mean_exposure']])+'</tr>' for k,m in result['metrics'].items())
    labels={'Buy':'买入','Overweight':'增持','Hold':'持有','Underweight':'减持','Sell':'卖出'}
    entries=[]
    for i,day in enumerate(days):
        a,b=reports['baseline'][i],reports['sentiment'][i];s=json.loads(b['sentiment_report']);ra,rb=rows['baseline'][i],rows['sentiment'][i]
        cells=[day,ra['execution_date'],labels[a['final_rating']],f"{ra['actual_weight']:.0%}",s['band'],str(s['score']),labels[b['final_rating']],f"{rb['actual_weight']:.0%}"]
        entries.append('<tr>'+''.join('<td>'+escape(c)+'</td>' for c in cells)+'</tr><tr><td colspan="8"><details><summary>查看情绪证据与双方最终报告</summary><h3>情绪报告</h3><pre>'+escape(json.dumps(s,ensure_ascii=False,indent=2))+'</pre><h3>原版历史策略：最终经理报告</h3><pre>'+escape(a['final_trade_decision'])+'</pre><h3>加入情绪：最终经理报告</h3><pre>'+escape(b['final_trade_decision'])+'</pre></details></td></tr>')
    text='''<!DOCTYPE html><html lang="zh"><meta charset="utf-8"><title>AAPL 八月情绪模块对照</title><style>body{font:15px/1.7 system-ui;color:#243444;background:#fafbfc;max-width:1250px;margin:32px auto;padding:0 24px}table{border-collapse:collapse;width:100%;background:white}th,td{padding:10px;text-align:left;border-bottom:1px solid #dbe2e8}th{background:#eaf0f5}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:13px/1.7 system-ui}summary{cursor:pointer;color:#315b7d}img{width:100%}</style><h1>AAPL 八月份：新闻情绪模块独立对照</h1><p>比较原版历史结果与本次情绪组，均采用一轮辩论、完整决策链和全仓买卖；本次采用简短风险审核，运行批次也不同，因此不能单独归因于情绪。新增对照组已停止，其不完整结果不纳入收益比较。新闻情绪是已有新闻的显式解读，不是独立的新消息来源。新闻归档为事后获取，不能证明历史文本从未修订；本实验不是模型参数训练。</p><table><tr><th>策略</th><th>净收益</th><th>最大回撤</th><th>平均仓位</th></tr>'''+metricrows+'</table><img src="comparison.png"><p>原版执行：买入／增持→满仓，减持／卖出→空仓，持有→保留股数。每日信号于下一交易日开盘执行；9 月 1 日统一清仓为回测结算规则。</p><table><tr>'+''.join('<th>'+x+'</th>' for x in ['信号日','成交日','对照评级','对照仓位','情绪方向','情绪分数[-1,1]','情绪组评级','情绪组仓位'])+'</tr>'+''.join(entries)+'</table><p>费用与核验记录：</p><pre>'+escape(json.dumps({k:v for k,v in result.items() if k!='metrics'},ensure_ascii=False,indent=2))+'</pre></html>'
    if OUT.name.endswith('original_prompts'):
        text=text.replace('本次采用简短风险审核，运行批次也不同，因此不能单独归因于情绪。新增对照组已停止，其不完整结果不纳入收益比较。','本次使用原始完整风险审核、原生模型客户端与原角色提示词，只新增已校验的情绪报告；没有额外的满仓／清仓决策约束。历史对照与本次仍是不同随机运行批次。')
    (folder/'daily_outputs.html').write_text(text)
if __name__=='__main__':main()
