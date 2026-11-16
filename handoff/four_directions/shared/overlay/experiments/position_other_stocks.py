"""Reuse archived single-round research with the unchanged active sizing policy."""
import argparse
import json
import re
from dotenv import load_dotenv
from tokenizers import Tokenizer
from experiments import position_month as base
import pandas as pd

ARCHIVE=base.ROOT/'agents/logs/e/f6e0d4240635'

def prepare(ticker, month="sep2026"):
    base.OUT=base.ROOT/f'results/position_active_{ticker.lower()}_{month}'
    # Read the exact completed AAPL policy, changing only the ticker.
    base.SYSTEM=(base.ROOT/'results/position_active_aapl_sep2026/system_prompt.txt').read_text().replace('AAPL',ticker)
    if month == 'sep2026':
        start,end='2026-09-01','2026-09-30'
    elif month == 'aug2026':
        start,end='2026-08-01','2026-08-31'
    else:raise ValueError('Unsupported month')
    prices=pd.read_csv(base.ROOT/f'data/prices/{ticker}.csv')
    indices=prices.index[(prices.date>=start)&(prices.date<=end)].tolist()
    assert indices and indices[0]>0 and indices[-1]+1<len(prices)
    days=[str(prices.iloc[i-1].date) for i in indices]
    tok=Tokenizer.from_file(str(base.TOKENIZER));sources={};tokens=0
    for day in days:
        path=ARCHIVE/f'results/{ticker}/TradingAgentsStrategy_logs/full_states_log_{day}.json'
        state=base.read(path);history=state['investment_debate_state']['history']
        assert state['run_settings']['max_debate_rounds']==1
        assert len(re.findall(r'(?m)^Bull Analyst:',history))==len(re.findall(r'(?m)^Bear Analyst:',history))==1
        assert state['company_of_interest']==ticker and state['trade_date']==day
        context=dict(ticker=ticker,signal_date=day,market_report=state['market_report'],
                     fundamentals_report=state['fundamentals_report'],news_report=state['news_report'],debate_history=history)
        assert all(context.values())
        target=base.OUT/'inputs'/f'r1_{day}.json'
        if target.exists():assert base.read(target)==context
        base.save(target,context)
        sources[f'r1_{day}']=dict(source_state_sha256=base.digest(path),context_sha256=base.digest(target))
        tokens+=len(tok.encode(base.SYSTEM+'\n'+json.dumps(context,ensure_ascii=False),add_special_tokens=False).ids)+3664
    p=dict(ticker=ticker,start=start,end=end,signal_dates=days,rounds=[1],initial_cash=100000.,fee_bps=10.,
        include_previous_decisions=True,model='deepseek-flash',thinking='enabled',reasoning_effort='high',max_tokens=8192,
        system_prompt_sha256=base.sha_text(base.SYSTEM),sources=sources,
        data_sha256={name:base.digest(base.ROOT/f'data/{name}/{ticker}.csv') for name in ['prices','financials']},
        estimated_input_tokens_with_account_reserve=tokens,offpeak_estimated_cny_at_8192_output_per_call=(tokens+len(days)*8192*4)/1e6,
        architecture='Frozen archived three analyst reports and one complete bull/bear round; active account-aware manager with last five decisions; next-open execution.',
        limitation='Upstream reports reused from original archived run, not the fresh AAPL paired-run batch; no causal cross-stock comparison of debate quality.')
    if (base.OUT/'protocol.json').exists():assert base.read(base.OUT/'protocol.json')==p
    base.save(base.OUT/'protocol.json',p);(base.OUT/'system_prompt.txt').write_text(base.SYSTEM)
    return p

class IndependentSpendGuard(base.SpendGuard):
    """Per-run budget; account-wide decreases may include concurrent stock runs."""
    def acquire(self, identity, reserve):
        with self.lock:
            current=base.balance()
            room=min(self.cap-self.charged_estimate,current['cny']-1.)-sum(self.inflight.values())
            base.save(base.OUT/'balance_latest.json',{**current,'account_decrease_cny':self.initial-current['cny'],
                'token_or_failure_reserve_cny':self.charged_estimate,'cap_cny':self.cap,
                'budget_scope':'local ledger; account balance availability checked separately'})
            if room<reserve:raise base.SpendStop('Insufficient per-run or account budget reserve')
            self.inflight[identity]=reserve

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--ticker',choices=['AAPL','GOOGL','AMZN'],required=True)
    parser.add_argument('--month',choices=['sep2026','aug2026'],default='sep2026')
    parser.add_argument('--live',action='store_true');parser.add_argument('--budget',type=float,default=2.)
    args=parser.parse_args();p=prepare(args.ticker,args.month)
    print(json.dumps({k:p[k] for k in ['ticker','estimated_input_tokens_with_account_reserve','offpeak_estimated_cny_at_8192_output_per_call']}),flush=True)
    if not args.live:return
    from tradingagents.dataflows.files import locked
    load_dotenv(base.ROOT/'.env',override=False)
    with locked(base.OUT/'run',wait=False) as acquired:
        if not acquired:raise RuntimeError('Already running')
        guard=IndependentSpendGuard(args.budget)
        try:base.run_arm(1,p,guard)
        finally:
            base.save(base.OUT/'balance_end.json',base.balance())
            print(json.dumps(base.evaluate(),ensure_ascii=False),flush=True)

if __name__=='__main__':main()
