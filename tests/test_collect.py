import pandas as pd
import pytest
from data import normalize_sec, collect_news


def test_sec_join_on_accession_acceptance_not_fiscal_end():
    facts={"facts":{"us-gaap":{"Assets":{"units":{"USD":[dict(accn="1",end="2023-12-31",val=100,form="10-K",filed="2024-02-01")]}}}}}
    filings=pd.DataFrame([dict(accessionNumber="1",acceptanceDateTime="2024-02-01T21:05:00Z")])
    f=normalize_sec(facts,filings,"2023-01-01")
    assert f.accepted_at.tolist()==["2024-02-01T21:05:00+00:00"]
    filings.loc[0,"acceptanceDateTime"]=""
    with pytest.raises(ValueError,match="acceptance"):
        normalize_sec(facts,filings,"2023-01-01")


def test_news_unavailable_is_error_not_empty_dataset():
    with pytest.raises(ValueError,match="historical news"):
        collect_news()


def test_curl_transport_records_raw_errors_and_never_disables_tls(tmp_path,monkeypatch):
    import subprocess
    from data import Fetcher
    from data import DataFolder
    def denied(cmd,**kwargs):
        assert "--insecure" not in cmd and "-k" not in cmd
        return subprocess.CompletedProcess(cmd,0,b'{"error":"denied"}\n403',b'')
    monkeypatch.setattr(subprocess,"run",denied)
    s=DataFolder(tmp_path)
    f=Fetcher(s,transport="curl")
    with pytest.raises(ValueError,match="HTTP 403"):
        f.json("https://data.sec.gov/a.json","raw/a.json")
    assert (s.path/"raw/a.json").read_bytes()==b'{"error":"denied"}'


@pytest.mark.parametrize("bad",["nonfinite","conflicting"])
def test_sec_rejects_unusable_numeric_facts(bad):
    item=dict(accn="1",end="2023-12-31",val=100,form="10-K",filed="2024-02-01")
    items=[item]
    if bad=="nonfinite": item["val"]=float("nan")
    else: items.append({**item,"val":80})
    facts={"facts":{"us-gaap":{"Assets":{"units":{"USD":items}}}}}
    filings=pd.DataFrame([dict(accessionNumber="1",acceptanceDateTime="2024-02-01T21:05:00Z")])
    with pytest.raises(ValueError): normalize_sec(facts,filings,"2023-01-01")
