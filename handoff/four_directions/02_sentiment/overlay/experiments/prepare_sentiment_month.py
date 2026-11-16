"""Offline frozen news preparation; no API clients or network fallback."""
import json
from pathlib import PureWindowsPath
from agents.historical_sentiment import prepare_articles,PROMPT,NewsSentimentBatch
from agents.single_agent import reference_record
from experiments.full_position_pair import ROOT,ARCHIVE
from experiments import position_month as util
from tokenizers import Tokenizer
import pandas as pd

def main():
    out=ROOT/'results/sentiment_aapl_aug2026_offline';out.mkdir(exist_ok=True)
    prices=pd.read_csv(ROOT/'data/prices/AAPL.csv');indices=prices.index[prices.date.str.startswith('2026-08-')]
    tok=Tokenizer.from_file(str(util.TOKENIZER));coverage=[]
    for i in indices:
        day=str(prices.iloc[i-1].date);record=reference_record('AAPL',day,ARCHIVE)
        meta=record['data_snapshot']['sources']['news'];source=ARCHIVE/'cache/finnhub'/PureWindowsPath(meta['path']).name
        if util.digest(source)!=meta['sha256']:raise ValueError('Archived source hash mismatch')
        snapshot=util.read(source)
        if snapshot['symbol']!='AAPL':raise ValueError('Wrong ticker')
        bundle=prepare_articles(snapshot,day)
        bundle['source_path']=str(source);bundle['source_sha256']=util.digest(source)
        payload=PROMPT+json.dumps(bundle,ensure_ascii=False)+json.dumps(NewsSentimentBatch.model_json_schema())
        n=len(tok.encode(payload,add_special_tokens=False).ids)
        path=out/'inputs'/f'{day}.json'
        if path.exists() and util.read(path)!=bundle:raise ValueError('Frozen input changed')
        util.save(path,bundle)
        coverage.append(dict(day=day,articles=len(bundle['articles']),eligible=bundle['eligible_unique_count'],estimated_input_tokens=n,excluded=bundle['excluded']))
    result=dict(ticker='AAPL',month='2026-08',days=coverage,total_article_appearances=sum(x['articles'] for x in coverage),
        unique_articles=len({a['article_id'] for x in coverage for a in util.read(out/'inputs'/f"{x['day']}.json")['articles']}),
        sentiment_input_tokens=sum(x['estimated_input_tokens'] for x in coverage),
        experiment=dict(debate_rounds=1,fractional_position=False,short_selling=False,baseline='fresh same downstream settings; sentiment disabled',treatment='same reports and settings; sentiment enabled before fresh debate',risk='identical settings in both arms'),
        status='Offline evidence preparation only; no model outputs, no backtest results, no API cost')
    util.save(out/'coverage.json',result);print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
