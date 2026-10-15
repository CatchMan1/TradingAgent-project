"""Probe official Yahoo retrieval paths; no LLM or paid service calls."""
from datetime import datetime, timezone
from pathlib import Path
import json
import yfinance as yf

out = Path(__file__).resolve().parent
yf.set_tz_cache_location('/private/tmp/trading-yfinance-news-cache-v170')
results = []
print('yfinance_version', yf.__version__, flush=True)
for ticker in ['AAPL', 'GOOGL', 'AMZN']:
    item = {'ticker': ticker}
    for label in ['primary', 'fallback']:
        try:
            if label == 'primary':
                feed = yf.Ticker(ticker).get_news(count=50)
            else:
                feed = [a for a in yf.Search(ticker, news_count=50).news or []
                        if ticker in [t.upper() for t in a.get('relatedTickers') or []]]
            (out/f'{ticker}-v170-{label}.json').write_text(json.dumps(feed, ensure_ascii=False))
            dates = []
            for article in feed:
                c = article.get('content')
                if isinstance(c, dict):
                    d = c.get('pubDate')
                else:
                    t = article.get('providerPublishTime')
                    d = datetime.fromtimestamp(t, tz=timezone.utc).isoformat() if t else None
                if d:
                    dates.append(d)
            item[label] = {
                'returned': len(feed), 'dated': len(dates),
                'earliest': min(dates) if dates else None,
                'latest': max(dates) if dates else None,
                'july_august_2026': sum('2026-07-01' <= d[:10] <= '2026-08-31' for d in dates),
                'august_september_2026': sum('2026-08-01' <= d[:10] <= '2026-09-30' for d in dates),
            }
        except Exception as exc:
            item[label] = {'error_type': type(exc).__name__, 'error': str(exc)[:300]}
    results.append(item)
    print(json.dumps(item, ensure_ascii=False), flush=True)
(out/'locked-version-summary.json').write_text(json.dumps({
    'checked_on': '2026-10-15', 'yfinance_version': yf.__version__, 'results': results,
}, ensure_ascii=False, indent=2))
