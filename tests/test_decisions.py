import pandas as pd
import pytest
from signals import validate_decisions, from_final_state, load_decisions


def rows():
    return pd.DataFrame([dict(ticker="AAPL",decision_time=d+"T16:30:00-05:00",information_cutoff=d+"T16:00:00-05:00",action="BUY",strategy_version="v1",source="portfolio_manager") for d in ["2023-12-29","2024-01-02","2024-01-03"]])


def test_complete_agent_decisions_and_roundtrip(tmp_path):
    d = rows()
    for suffix in ["csv", "jsonl"]:
        p = tmp_path / ("d."+suffix)
        if suffix == "csv": d.to_csv(p,index=False)
        else: d.to_json(p,orient="records",lines=True)
        got = validate_decisions(load_decisions(p),"AAPL","2024-01-02","2024-01-03")
        assert got.action.tolist() == ["BUY"]*3


@pytest.mark.parametrize("kind",["duplicate","missing","action","future","naive","version","source","late","before_close"])
def test_reject_invalid_decisions(kind):
    d=rows()
    if kind=="duplicate": d=pd.concat([d,d.iloc[[0]]])
    if kind=="missing": d=d.iloc[:-1]
    if kind=="action": d.loc[0,"action"]="Overweight"
    if kind=="future": d.loc[0,"information_cutoff"]="2023-12-29T17:00:00-05:00"
    if kind=="naive": d.loc[0,"decision_time"]="2023-12-29 16:30"
    if kind=="version": d.loc[0,"strategy_version"]=""
    if kind=="source": d.loc[0,"source"]="trader"
    if kind=="late": d.loc[0,"decision_time"]="2023-12-30T10:00:00-05:00"
    if kind=="before_close": d.loc[0,"decision_time"]="2023-12-29T15:00:00-05:00"
    with pytest.raises(ValueError): validate_decisions(d,"AAPL","2024-01-02","2024-01-03")


def test_final_manager_five_tier_to_binary_position_mapping():
    assert from_final_state({"final_rating":"Buy","final_trade_decision":"**Rating**: Buy"})=="BUY"
    assert from_final_state({"final_trade_decision":"**Rating**: Hold"})=="HOLD"
    assert from_final_state({"final_rating":"Overweight","final_trade_decision":"**Rating**: Overweight"})=="BUY"
    assert from_final_state({"final_rating":"Underweight","final_trade_decision":"**Rating**: Underweight"})=="SELL"
    for s in [{"trader_investment_plan":"BUY"},{"final_rating":"REVIEW","final_trade_decision":"x"},{"final_rating":"Buy","final_trade_decision":"**Rating**: Sell"}]:
        with pytest.raises(ValueError): from_final_state(s)


def test_early_close_cutoff_is_13_not_regular_16():
    d=rows()
    for i,day in enumerate(["2024-07-02","2024-07-03","2024-07-05"]):
        d.loc[i,"decision_time"]=day+"T16:30:00-04:00"
        d.loc[i,"information_cutoff"]=day+("T13:00:00-04:00" if i==1 else "T16:00:00-04:00")
    assert len(validate_decisions(d,"AAPL","2024-07-03","2024-07-05"))==3
    d.loc[1,"information_cutoff"]="2024-07-03T16:00:00-04:00"
    with pytest.raises(ValueError): validate_decisions(d,"AAPL","2024-07-03","2024-07-05")


def test_single_agent_preserves_binary_targets_in_chronological_order():
    from agents_single import validate_single_agent

    decisions = pd.DataFrame({
        "ticker": "AAPL",
        "signal_date": ["2023-12-29", "2024-01-02", "2024-01-03"],
        "target_weight": [1, 1, 0],
    })
    validated = validate_single_agent(decisions.iloc[::-1], "AAPL")
    assert validated.signal_date.tolist() == ["2023-12-29", "2024-01-02", "2024-01-03"]
    assert validated.target_weight.tolist() == [1, 1, 0]


@pytest.mark.parametrize("weight", [-1, 0.5, 2, "", "NaN", "HOLD"])
def test_single_agent_rejects_nonbinary_and_missing_weights(weight):
    from agents_single import validate_single_agent

    decisions = pd.DataFrame({"ticker": ["AAPL"], "signal_date": ["2024-01-02"], "target_weight": [weight]})
    with pytest.raises(ValueError, match="target_weight"):
        validate_single_agent(decisions, "AAPL")
