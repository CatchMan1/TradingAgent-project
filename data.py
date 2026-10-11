"""行情、财报、历史可见数据和固定数据目录；不包含回测逻辑。"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"


# 数据来源记录

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(obj):
    return json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False).encode()


def read_sources(data_dir=DATA_DIR):
    record = json.loads((Path(data_dir) / "sources.json").read_text())
    if record.get("status") != "complete":
        raise ValueError("Data collection incomplete or failed; inspect sources.json")
    return record


def data_hash(data_dir=DATA_DIR):
    """冻结时核对实际行情/财报内容，不需要快照编号。"""
    folder = Path(data_dir)
    files = sorted(list(folder.glob("prices/*.csv")) + list(folder.glob("financials/*.csv")))
    if not files:
        raise ValueError("No market/financial data to freeze")
    note = folder / "sources.json"
    if note.exists():
        files.append(note)
    return digest(b"".join(str(p.relative_to(folder)).encode() + p.read_bytes() for p in files))


class DataFolder:
    """采集时写入固定路径，并保留一份来源说明；不创建批次目录。"""
    def __init__(self, base=DATA_DIR):
        self.path = Path(base)
        self.path.mkdir(parents=True, exist_ok=True)
        note = self.path / "sources.json"
        self.sources = json.loads(note.read_text()) if note.exists() else {"files": {}, "limitations": []}
        self.sources.pop("error", None)
        self.sources["status"] = "collecting"

    def write_bytes(self, name, content, source, **metadata):
        path = (self.path / name).resolve()
        if not path.is_relative_to(self.path.resolve()):
            raise ValueError("Data path escapes folder")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        self.sources["files"][name] = dict(source=source, fetched_at=utcnow(), sha256=digest(content), **metadata)

    def write_json(self, name, obj, source, **metadata):
        self.write_bytes(name, json_bytes(obj), source, **metadata)

    def write_frame(self, name, frame, source, **metadata):
        self.write_bytes(name, frame.to_csv(index=False).encode(), source, rows=len(frame), **metadata)

    def finish(self, status="complete"):
        self.sources["status"] = status
        self.sources["updated_at"] = utcnow()
        (self.path / "sources.json").write_bytes(json_bytes(self.sources))

# 交易日历、数据整理与历史过滤

"""Strict market validation and point-in-time views. No gap filling."""
from functools import lru_cache
import numpy as np
import pandas as pd
import exchange_calendars as xcals


@lru_cache(maxsize=64)
def schedule(start, end):
    cal = xcals.get_calendar("XNYS", start=pd.Timestamp(start)-pd.Timedelta(days=10), end=pd.Timestamp(end)+pd.Timedelta(days=10))
    s = cal.schedule.loc[start:end, ["open", "close"]].copy()
    s.index = s.index.tz_localize(None).normalize() if s.index.tz is not None else s.index.normalize()
    return s


def aware(value):
    if value is None or pd.isna(value):
        raise ValueError("Missing timestamp; timezone required")
    t = pd.Timestamp(value)
    if pd.isna(t) or t.tzinfo is None:
        raise ValueError(f"Timestamp needs explicit timezone: {value}")
    return t.tz_convert("UTC")


def validate_prices(p, start, end):
    required = ["date", "open", "high", "low", "close", "volume", "split", "dividend"]
    if not set(required).issubset(p.columns):
        raise ValueError(f"Missing price columns: {set(required)-set(p.columns)}")
    p = p.copy()
    dates = pd.to_datetime(p.date, format="%Y-%m-%d", errors="raise")
    if dates.duplicated().any() or not dates.is_monotonic_increasing:
        raise ValueError("Duplicate or unsorted price dates")
    if not dates.equals(dates.dt.normalize()):
        raise ValueError("Prices must have session dates")
    expected = schedule(start,end).index
    actual = pd.DatetimeIndex(dates)
    if not actual.equals(expected):
        raise ValueError(f"Price sessions mismatch: missing={expected.difference(actual).strftime('%Y-%m-%d').tolist()}, extra={actual.difference(expected).strftime('%Y-%m-%d').tolist()}")
    if len(p) == 0:
        raise ValueError("Empty prices")
    nums = p[required[1:]].apply(pd.to_numeric, errors="raise")
    if not np.isfinite(nums.to_numpy()).all():
        raise ValueError("Non-finite prices/actions")
    if (nums[["open","high","low","close","split"]] <= 0).any().any() or (nums[["volume","dividend"]] < 0).any().any():
        raise ValueError("Invalid prices/actions")
    if (nums.high < nums[["open","low","close"]].max(axis=1)-1e-7).any() or (nums.low > nums[["open","high","close"]].min(axis=1)+1e-7).any():
        raise ValueError("Invalid OHLC range")
    p[required[1:]] = nums
    p["date"] = dates.dt.strftime("%Y-%m-%d")
    return p.reset_index(drop=True)


def normalize_yahoo(payload):
    chart = payload.get("chart", {})
    if chart.get("error") or not chart.get("result"):
        raise ValueError(f"Yahoo error: {chart.get('error')}")
    r = chart["result"][0]
    if r["meta"].get("exchangeTimezoneName") != "America/New_York" or r["meta"].get("currency") != "USD":
        raise ValueError("Yahoo exchange timezone/currency mismatch")
    q = r["indicators"]["quote"][0]
    p = pd.DataFrame({k:q[k] for k in ["open","high","low","close","volume"]},dtype=float)
    p.insert(0,"date",pd.to_datetime(r["timestamp"],unit="s",utc=True).tz_convert("America/New_York").strftime("%Y-%m-%d"))
    p["split"], p["dividend"] = 1., 0.
    events = r.get("events", {})
    # Yahoo OHLC (even auto_adjust=False) and dividends use split-adjusted
    # share units. Undo subsequent splits to recover actual historical units.
    splits = []
    for v in events.get("splits",{}).values():
        d = pd.Timestamp(v["date"],unit="s",tz="UTC").tz_convert("America/New_York").strftime("%Y-%m-%d")
        ratio = float(v["numerator"])/float(v["denominator"])
        if not np.isfinite(ratio) or ratio <= 0 or d not in set(p.date):
            raise ValueError("Invalid/unmatched Yahoo split event")
        splits.append((d,ratio))
        p.loc[p.date == d,"split"] *= ratio
    for v in events.get("dividends",{}).values():
        d = pd.Timestamp(v["date"],unit="s",tz="UTC").tz_convert("America/New_York").strftime("%Y-%m-%d")
        if d not in set(p.date):
            raise ValueError("Unmatched Yahoo dividend event")
        p.loc[p.date == d,"dividend"] += float(v["amount"])
    for d,ratio in splits:
        before = p.date < d
        p.loc[before,["open","high","low","close","dividend"]] *= ratio
        p.loc[before,"volume"] /= ratio
    return p


def facts_asof(facts, cutoff):
    c = aware(cutoff)
    if facts.empty:
        return facts.copy()
    times = facts.accepted_at.map(aware)
    f = facts.loc[times <= c].copy()
    # Preserve each fiscal span/tag/unit separately; select latest public vintage.
    keys = ["taxonomy","tag","unit","start","end"]
    f["accepted_at"] = times.loc[f.index]
    return f.sort_values(["accepted_at","accn"]).drop_duplicates(keys,keep="last").reset_index(drop=True)


def news_asof(news, cutoff, start=None):
    times = news.published_at.map(aware)
    mask = times <= aware(cutoff)
    if start is not None:
        mask &= times >= aware(start)
    return news.loc[mask].copy().reset_index(drop=True)


def total_return_index(p):
    """Forward-only series in current share units; no future action adjustment."""
    p = p.copy()
    growth = (p.close + p.dividend)*p.split/p.close.shift(1)
    growth.iloc[0] = 1.
    return growth.cumprod()*float(p.close.iloc[0])

# Yahoo / SEC 采集

"""Direct Yahoo chart and SEC EDGAR collectors. No vendor fallback."""
import os
import re
import subprocess
import time
from pathlib import Path
import pandas as pd
import numpy as np
import requests

CIKS = {"AAPL": "0000320193", "GOOGL": "0001652044", "AMZN": "0001018724"}


class Fetcher:
    def __init__(self,folder,user_agent="TradingAgentsQuantBacktest/1.0",transport="requests"):
        self.folder=folder
        if transport not in ["requests","curl"]: raise ValueError("Unknown HTTP transport")
        self.transport=transport
        self.session=requests.Session()
        self.session.headers.update({"User-Agent":user_agent,"Accept":"application/json"})
        self.last_request=0.

    def get(self,url,name):
        # Below SEC's 10 req/s limit; do not retry/fallback silently.
        time.sleep(max(0.,.15-(time.monotonic()-self.last_request)))
        self.last_request=time.monotonic()
        try:
            if self.transport=="requests":
                r=self.session.get(url,timeout=(10,45))
            else:
                command=["curl","--silent","--show-error","--location","--max-time","60","--user-agent",self.session.headers["User-Agent"],"--header","Accept: application/json","--write-out","\n%{http_code}",url]
                response=subprocess.run(command,capture_output=True,timeout=65,check=False)
                if response.returncode:
                    raise ValueError(f"curl transport failed ({response.returncode}): {response.stderr.decode(errors='replace')}")
                body,status=response.stdout.rsplit(b"\n",1)
                r=requests.Response()
                r.status_code=int(status)
                r._content=body
                r.encoding="utf-8"
        except requests.RequestException as e:
            raise ValueError(f"Network failed for {url}: {type(e).__name__}: {e}") from e
        self.folder.write_bytes(name,r.content,url,status_code=r.status_code,content_type=r.headers.get("Content-Type"),transport=self.transport)
        if r.status_code!=200: raise ValueError(f"HTTP {r.status_code} for {url}; raw response retained; no fallback")
        return r

    def json(self,url,name):
        r=self.get(url,name)
        try: return r.json()
        except requests.exceptions.JSONDecodeError as e: raise ValueError(f"Non-JSON response: {url}") from e


def collect_prices(cfg,folder,transport="requests"):
    f=Fetcher(folder,transport=transport)
    start=cfg["warmup_start"]
    end=cfg["splits"]["test"][1]
    # Request through retrieval day to undo ALL subsequent split adjustments,
    # including actions after the configured evaluation end. Never evaluate them.
    retrieval_day=pd.Timestamp.now(tz="America/New_York").strftime("%Y-%m-%d")
    fetch_end=max(end,retrieval_day)
    p1=int(pd.Timestamp(start,tz="America/New_York").timestamp())
    p2=int((pd.Timestamp(fetch_end,tz="America/New_York")+pd.DateOffset(days=1)).timestamp())
    for ticker in cfg["tickers"]:
        url=f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?period1={p1}&period2={p2}&interval=1d&events=div%2Csplits&includeAdjustedClose=true"
        raw=f.json(url,f"raw/yahoo/{ticker}.json")
        p=normalize_yahoo(raw)
        p=p.loc[(p.date>=start)&(p.date<=end)]
        p=validate_prices(p,start,end)
        folder.write_frame(f"prices/{ticker}.csv",p,url,price_basis="actual_historical_share_units",dividend_basis="actual_historical_share_units",validation_start=start,validation_end=end)
    folder.sources["price_window"]=[start,end]
    folder.sources["limitations"].extend(["Yahoo historical bars are retrospective vendor data, not archived as first published; revisions remain possible.","Yahoo dividends provide ex-dates but no complete historical pay-date schedule; return assumptions are documented in analysis.ipynb."])


def normalize_sec(facts,filings,earliest):
    if "accessionNumber" not in filings or "acceptanceDateTime" not in filings: raise ValueError("SEC missing acceptance metadata")
    versions={}
    for _,r in filings.iterrows():
        acc=r.accessionNumber
        val=r.acceptanceDateTime
        if not isinstance(val,str) or not val.strip(): continue
        t=aware(val)
        if acc in versions and versions[acc]!=t: raise ValueError("Conflicting SEC acceptance times")
        versions[acc]=t
    records=[]
    for taxonomy,tags in facts["facts"].items():
        for tag,detail in tags.items():
            for unit,items in detail.get("units",{}).items():
                for item in items:
                    if item.get("form") not in ["10-K","10-K/A","10-Q","10-Q/A"]: continue
                    # Retain a two-year prehistory for the first as-of view.
                    if item.get("filed","")<earliest: continue
                    acc=item["accn"]
                    if acc not in versions: raise ValueError(f"SEC acceptance timestamp unavailable: {acc}; filed date cannot substitute")
                    records.append(dict(taxonomy=taxonomy,tag=tag,unit=unit,start=item.get("start",""),end=item["end"],val=item["val"],accn=acc,form=item["form"],filed=item["filed"],accepted_at=versions[acc].isoformat()))
    if not records: raise ValueError("SEC no eligible historical facts")
    frame=pd.DataFrame(records).drop_duplicates().reset_index(drop=True)
    frame["val"]=pd.to_numeric(frame.val,errors="raise")
    if not np.isfinite(frame.val.to_numpy(dtype=float)).all(): raise ValueError("SEC non-finite fact values")
    keys=["taxonomy","tag","unit","start","end","accn"]
    if frame.duplicated(keys).any(): raise ValueError("SEC conflicting values in the same filing/span")
    return frame


def collect_sec(cfg,folder,user_agent=None,transport="requests"):
    ua=user_agent or os.environ.get("SEC_EDGAR_USER_AGENT")
    # A local contact file is intentionally excluded from version control.
    contact=ROOT/".sec_user_agent"
    if not ua and contact.exists(): ua=contact.read_text().strip()
    if not ua or not re.search(r"[^\s@]+@[^\s@]+\.[^\s@]+",ua):
        raise ValueError("SEC requires SEC_EDGAR_USER_AGENT='Name email@example.com'")
    f=Fetcher(folder,ua,transport)
    earliest=(pd.Timestamp(cfg["warmup_start"])-pd.DateOffset(years=2)).strftime("%Y-%m-%d")
    for ticker in cfg["tickers"]:
        cik=CIKS[ticker]
        url=f"https://data.sec.gov/submissions/CIK{cik}.json"
        submissions=f.json(url,f"raw/sec/{ticker}/submissions.json")
        if ticker not in submissions.get("tickers",[]): raise ValueError(f"SEC CIK/ticker mismatch for {ticker}")
        frames=[pd.DataFrame(submissions["filings"]["recent"])]
        for file in submissions["filings"].get("files",[]):
            if file["filingTo"]<earliest: continue
            name=file["name"]
            if not re.fullmatch(r"CIK\d+-submissions-\d+\.json",name): raise ValueError("Unexpected SEC history filename")
            frames.append(pd.DataFrame(f.json(f"https://data.sec.gov/submissions/{name}",f"raw/sec/{ticker}/{name}")))
        filings=pd.concat(frames,ignore_index=True).drop_duplicates("accessionNumber")
        if "acceptanceDateTime" not in filings: filings["acceptanceDateTime"]=""
        relevant=filings.form.isin(["10-K","10-K/A","10-Q","10-Q/A"]) & (filings.filingDate>=earliest)
        for idx,row in filings.loc[relevant].iterrows():
            if isinstance(row.acceptanceDateTime,str) and row.acceptanceDateTime.strip(): continue
            # Older submissions shards may lack acceptanceDateTime. Read the
            # original SGML header; never invent midnight or use period-end.
            acc=row.accessionNumber
            compact=acc.replace("-","")
            header_url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{compact}/{acc}.txt"
            body=f.get(header_url,f"raw/sec/{ticker}/{acc}.txt").text
            match=re.search(r"<ACCEPTANCE-DATETIME>(\d{14})",body)
            if not match: raise ValueError(f"SEC acceptance header missing: {acc}")
            timestamp=pd.to_datetime(match[1],format="%Y%m%d%H%M%S")
            filings.loc[idx,"acceptanceDateTime"]=timestamp.tz_localize("America/New_York",ambiguous="raise",nonexistent="raise").tz_convert("UTC").isoformat()
        facts_url=f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
        facts=f.json(facts_url,f"raw/sec/{ticker}/companyfacts.json")
        if int(facts["cik"])!=int(cik): raise ValueError("SEC facts CIK mismatch")
        normalized=normalize_sec(facts,filings,earliest)
        folder.write_frame(f"financials/{ticker}.csv",normalized,facts_url,earliest_filing=earliest)
        folder.write_frame(f"raw/filings/{ticker}.csv",filings.loc[relevant],url)
    folder.sources["limitations"].append("SEC companyfacts contains standardized entity-wide XBRL facts, not every custom tag or full statement. Actual EDGAR acceptance timestamps define availability; possible dissemination delay is not archived.")


def collect_news():
    raise ValueError("No authorized historical news source: Yahoo is a recent sample; Alpha Vantage NEWS_SENTIMENT is premium. Supply a licensed timestamped archive/API before collecting; no empty substitute or paid call made.")


def collect(cfg, kind="prices", transport="requests", overwrite=False):
    """显式采集到 data/；已有数据需 overwrite=True 才更新。"""
    if kind not in ["prices", "sec", "free", "news"]:
        raise ValueError("Unknown data kind")
    if kind == "news":
        collect_news()
    selected = (["prices"] if kind == "prices" else ["financials"] if kind == "sec"
                else ["prices", "financials"])
    if not overwrite and any((DATA_DIR / name / f"{ticker}.csv").exists()
                             for name in selected for ticker in cfg["tickers"]):
        raise ValueError("Data already exists; use cached files or explicitly set overwrite=True")
    folder = DataFolder(DATA_DIR)
    folder.sources["news_status"] = "blocked_no_authorized_historical_source"
    # 采集失败时拒绝将部分更新的数据当作完整数据使用。
    folder.finish("collecting")
    try:
        if kind in ["prices", "free"]:
            collect_prices(cfg, folder, transport)
        if kind in ["sec", "free"]:
            collect_sec(cfg, folder, transport=transport)
        folder.finish()
    except Exception as error:
        folder.sources["error"] = dict(type=type(error).__name__, message=str(error), at=utcnow())
        folder.finish("failed")
        raise ValueError(f"Collection failed; inspect data/sources.json: {error}") from error
    return DATA_DIR


def read_prices(ticker, cfg, end=None, data_dir=DATA_DIR):
    """读取固定行情文件，验证完整覆盖后截断实验结束日。"""
    sources = read_sources(data_dir)
    first, last = sources["price_window"]
    frame = pd.read_csv(Path(data_dir) / f"prices/{ticker}.csv")
    frame = validate_prices(frame, first, last)
    if first > cfg["warmup_start"] or last < (end or cfg["splits"]["test"][1]):
        raise ValueError("Price coverage insufficient")
    return frame if end is None else frame.loc[frame.date <= end].copy()


def data_asof(ticker, kind, cutoff, data_dir=DATA_DIR):
    """给 Agent 提供截至 cutoff 已公开的数据，不能直接使用整份历史表。"""
    sources = read_sources(data_dir)
    if kind not in ["prices", "financials", "news"]:
        raise ValueError("kind must be prices / financials / news")
    path = Path(data_dir) / kind / f"{ticker}.csv"
    if not path.exists():
        raise ValueError(f"Missing {kind}/{ticker}.csv; no empty substitute")
    frame = pd.read_csv(path, keep_default_na=False)
    if kind == "financials":
        return facts_asof(frame, cutoff)
    if kind == "news":
        return news_asof(frame, cutoff)
    first, last = sources["price_window"]
    frame = validate_prices(frame, first, last)
    closes = schedule(first, last).close
    visible = closes.loc[closes <= aware(cutoff)].index.strftime("%Y-%m-%d")
    frame = frame.loc[frame.date.isin(visible)].copy()
    if frame.empty:
        raise ValueError("No completed daily bar at cutoff")
    frame["technical_total_return_index"] = total_return_index(frame)
    return frame
