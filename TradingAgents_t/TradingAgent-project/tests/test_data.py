import pandas as pd
import pytest
from data import validate_prices, normalize_yahoo, facts_asof, news_asof, schedule


def test_calendar_actual_sessions_and_early_close():
    s = schedule("2024-07-03", "2024-07-05")
    assert list(s.index.strftime("%Y-%m-%d")) == ["2024-07-03", "2024-07-05"]
    assert s.iloc[0].close.tz_convert("America/New_York").hour == 13


def test_missing_trading_day_is_error():
    p = pd.DataFrame({"date": ["2024-01-02"], "open": [10.], "high": [11.], "low": [9.], "close": [10.], "volume": [10.], "split": [1.], "dividend": [0.]})
    with pytest.raises(ValueError, match="sessions"):
        validate_prices(p, "2024-01-02", "2024-01-03")
    p.loc[0, "open"] = float("nan")
    with pytest.raises(ValueError):
        validate_prices(p, "2024-01-02", "2024-01-02")


def test_yahoo_split_adjusted_ohlc_restored_to_traded_price():
    ts = [int(pd.Timestamp(d, tz="America/New_York").timestamp()) for d in ["2024-01-02 09:30", "2024-01-03 09:30"]]
    payload = {"chart": {"error": None, "result": [{"meta": {"exchangeTimezoneName": "America/New_York", "currency": "USD"}, "timestamp": ts, "indicators": {"quote": [{"open": [50., 51.], "high": [50., 51.], "low": [50., 51.], "close": [50., 51.], "volume": [200., 200.]}]}, "events": {"splits": {str(ts[1]): {"date": ts[1], "numerator": 2., "denominator": 1.}}, "dividends": {str(ts[0]): {"date": ts[0], "amount": .5}}}}]}}
    p = normalize_yahoo(payload)
    assert p.open.tolist() == [100., 51.]
    assert p.volume.tolist() == [100., 200.]
    assert p.dividend.tolist() == [1., 0.]
    assert p.split.tolist() == [1., 2.]


def test_filing_restatement_visible_only_after_acceptance():
    f = pd.DataFrame([dict(taxonomy="us-gaap", tag="Assets", unit="USD", start="", end="2023-12-31", val=100, accepted_at="2024-02-01T21:05:00Z", accn="a"), dict(taxonomy="us-gaap", tag="Assets", unit="USD", start="", end="2023-12-31", val=80, accepted_at="2024-03-01T20:00:00Z", accn="b")])
    assert facts_asof(f, "2024-02-01T21:00:00Z").empty
    assert facts_asof(f, "2024-02-02T21:00:00Z").val.tolist() == [100]
    assert facts_asof(f, "2024-03-01T21:00:00Z").val.tolist() == [80]
    f.loc[0, "accepted_at"] = "2024-02-01"
    with pytest.raises(ValueError, match="timezone"):
        facts_asof(f, "2024-03-01T21:00:00Z")


def test_news_future_and_unknown_time_rejected():
    n = pd.DataFrame({"published_at": ["2024-01-02T20:00:00Z", "2024-01-02T22:00:00Z"], "title": ["past", "future"]})
    assert news_asof(n, "2024-01-02T21:00:00Z").title.tolist() == ["past"]
    n.loc[0, "published_at"] = None
    with pytest.raises(ValueError):
        news_asof(n, "2024-01-02T21:00:00Z")


def test_integer_yahoo_volume_handles_reverse_split():
    ts=[1704205800,1704292200]
    raw={"chart":{"result":[{"meta":{"exchangeTimezoneName":"America/New_York","currency":"USD"},"timestamp":ts,"indicators":{"quote":[dict(open=[100.,110.],high=[100.,110.],low=[100.,110.],close=[100.,110.],volume=[201,200])]},"events":{"splits":{"x":dict(date=ts[1],numerator=1,denominator=10)}}}],"error":None}}
    p=normalize_yahoo(raw)
    assert p.open.tolist()==[10.,110.]
    assert p.volume.tolist()==[2010.,200.]
