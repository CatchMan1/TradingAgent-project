"""Short-only overlay: frozen original full chain, approve shorts only on exit dates."""
import argparse,json,os
from concurrent.futures import ThreadPoolExecutor,as_completed
from pydantic import BaseModel,ConfigDict,Field
from tokenizers import Tokenizer
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
from experiments import full_position_pair as base
from experiments.optimization_engine import simulate

OUT=base.ROOT/'results/short_only_aapl_aug2026'
class ShortReview(BaseModel):
    model_config=ConfigDict(extra='forbid',strict=True)
    open_short: bool
    rationale: str=Field(min_length=1)
    downside_evidence: str
    upside_risk: str
    exit_condition: str

RULES='''You are the final Portfolio Manager evaluating ONLY the new optional short-selling feature. All supplied analyst, research, trader and full risk reports and the original final decision are frozen; do not rewrite them. No sentiment module or fractional sizing is enabled. The original recommendation exits or avoids a long position. Decide whether the existing evidence additionally justifies opening a short now, as opposed to staying in cash. Underweight/Sell is NOT automatically a short thesis. Missing bullish confirmation, expensive valuation alone, or merely wishing to reduce long risk does not prove an affirmative downside trade. Weigh evidence both for a short and against it; approve only if the evidence supports it, without inventing probabilities or news. A rejection preserves the original strategy unchanged. A short approval means one fixed unit: short notional equal to account net equity at next open, no leverage beyond that, no partial positions. Borrow cost assumption 3% annualized; short owes dividends; rising price loses money. This is an unconditional next-open decision, not a future trigger or limit order. On a later date without a new short approval the position is covered (or reversed if the original decision is long). Explain evidence, squeeze/upside risk and invalidation; no external tools. Output the requested JSON in concise Chinese, rationale under 250 Chinese characters.'''
class Client(base.StageClient):
    def messages(self,prompt,schema):
        return [dict(role='system',content=RULES+'\nJSON schema:\n'+json.dumps(schema.model_json_schema())),dict(role='user',content=prompt)]
    def request_options(self):return dict(max_tokens=2000,extra_body={'thinking':{'type':'disabled'}})

def prepare():
    OUT.mkdir(exist_ok=True)
    days=base.util.read(base.ROOT/'results/full_pipeline_position_2026aug_sep/protocol.json')
    # Use the already audited original August signal calendar.
    days=base.util.read(base.ROOT/'results/sentiment_aapl_aug2026_original_prompts/protocol.json')['signal_dates']
    hashes={};ratings={}
    for day in days:
        source=base.ARCHIVE/f'results/AAPL/TradingAgentsStrategy_logs/full_states_log_{day}.json';s=base.util.read(source)
        assert s['run_settings']['max_debate_rounds']==1 and not s.get('sentiment_report')
        ratings[day]=s['final_rating'];hashes[day]=base.util.digest(source)
        payload={k:s[k] for k in ['company_of_interest','trade_date','market_report','news_report','fundamentals_report','investment_plan','trader_investment_plan','final_trade_decision','final_rating']}
        payload['bull_bear_debate']=s['investment_debate_state']['history'];payload['full_risk_debate']=s['risk_debate_state']['history']
        target=OUT/'inputs'/f'{day}.json'
        if target.exists():assert base.util.read(target)==payload
        base.util.save(target,payload)
    protocol=dict(days=days,ratings=ratings,original_source_hashes=hashes,rules=RULES,borrow_apr=.03,fee_bps=10,maintenance_margin=.30,model='deepseek-flash',scope='short-only final-manager overlay on original exit dates; all upstream decisions frozen',limitations='Assumed borrow availability and 3% annual cost, no intraday margin/locate/slippage model. One stock-month, not a live tradability claim.',prices_sha256=base.util.digest(base.ROOT/'data/prices/AAPL.csv'))
    if (OUT/'protocol.json').exists():assert base.util.read(OUT/'protocol.json')==protocol
    base.util.save(OUT/'protocol.json',protocol);return protocol

def one(day,guard):
    payload=base.util.read(OUT/'inputs'/f'{day}.json')
    with OpenAI(api_key=os.environ['DEEPSEEK_API_KEY'],base_url='https://api.deepseek.com',max_retries=0,timeout=120) as api:
        c=Client(api,guard,Tokenizer.from_file(str(base.util.TOKENIZER)),day,{},'short_review')
        result=c.call(json.dumps(payload,ensure_ascii=False),ShortReview)
        base.util.save(OUT/'decisions'/f'{day}.json',result.model_dump());print('COMPLETE',day,'SHORT' if result.open_short else 'ORIGINAL',flush=True)

def evaluate(p):
    prices=pd.read_csv(base.ROOT/'data/prices/AAPL.csv');assert base.util.digest(base.ROOT/'data/prices/AAPL.csv')==p['prices_sha256']
    authorizations={d:base.util.read(OUT/'decisions'/f'{d}.json')['open_short'] if r in {'Sell','Underweight'} else False for d,r in p['ratings'].items()}
    off,offm=simulate(prices,p['ratings'],'2026-08-01','2026-08-31')
    on,onm=simulate(prices,p['ratings'],'2026-08-01','2026-08-31',short=True,short_authorizations=authorizations,borrow_apr=p['borrow_apr'])
    archived=pd.read_csv(base.ROOT/'results/full_pipeline_position_2026aug_sep/comparisons/AAPL_08/original_binary_trades.csv')
    import numpy as np
    np.testing.assert_allclose(off.equity,archived.equity,rtol=1e-10)
    bh,bhm=simulate(prices,{d:'Buy' if i==0 else 'Hold' for i,d in enumerate(p['days'])},'2026-08-01','2026-08-31')
    for name,frame in [('original',off),('short_enabled',on),('buy_hold',bh)]:frame.to_csv(OUT/f'{name}.csv',index=False)
    ledger=[json.loads(x) for x in (OUT/'api_calls.jsonl').read_text().splitlines()]
    report=dict(metrics=dict(original=offm,short_enabled=onm,buy_hold=bhm),short_dates=[d for d,v in authorizations.items() if v],api_calls=len(ledger),api_estimated_cny=sum(x.get('estimated_cny',0) for x in ledger),balance=base.util.read(OUT/'balance_end.json'),baseline_parity_verified=True,limitations=p['limitations'])
    base.util.save(OUT/'report.json',report);print(json.dumps(report,ensure_ascii=False,indent=2))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--live',action='store_true');ap.add_argument('--evaluate',action='store_true');args=ap.parse_args();p=prepare()
    pending=[d for d,r in p['ratings'].items() if r in {'Underweight','Sell'}]
    print('Short review dates',len(pending),'upstream API calls 0',flush=True)
    if args.evaluate:evaluate(p);return
    if not args.live:return
    base.OUT=OUT;base.util.OUT=OUT;load_dotenv(base.ROOT/'.env');guard=base.IndependentSpendGuard(2.);failures=[]
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures={pool.submit(one,d,guard):d for d in pending}
        for f in as_completed(futures):
            try:f.result()
            except Exception as e:failures.append(dict(day=futures[f],error=str(e)));print('FAILED',failures[-1],flush=True)
    base.util.save(OUT/'failures.json',failures);base.util.save(OUT/'balance_end.json',base.util.balance())
    if failures:raise SystemExit(1)
    evaluate(p)
if __name__=='__main__':main()
