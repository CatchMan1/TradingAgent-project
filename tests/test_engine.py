import numpy as np
import pandas as pd
import pytest
from notebook_code import namespace


def prices(opens, splits=None, dividends=None):
    n = len(opens)
    return pd.DataFrame(dict(date=pd.bdate_range("2024-01-02", periods=n).strftime("%Y-%m-%d"),
                             open=opens, close=opens, high=opens, low=opens, volume=[10000]*n,
                             split=splits or [1]*n, dividend=dividends or [0]*n))


def decisions(actions):
    days = ["2023-12-29"] + list(pd.bdate_range("2024-01-02", periods=len(actions)-1).strftime("%Y-%m-%d"))
    return pd.DataFrame(dict(session=days, action=actions))


def test_position_return_and_turnover_cost_include_initial_entry():
    nav, ret = namespace["cal_net_values"]([1, 1, 0], [.1, -.1, .2], fee=.001, nav_mode="additive")
    np.testing.assert_allclose(ret, [.099, -.1, -.001])
    np.testing.assert_allclose(nav, [1.099, .999, .998])


def test_compound_and_log_input_use_same_long_only_cost_formula():
    function = namespace["cal_net_values"]
    nav, ret = function([0, 1, 0], [.1, .2, -.1], fee=.01, nav_mode="compound")
    np.testing.assert_allclose(ret, [0, .19, -.01])
    np.testing.assert_allclose(nav, np.cumprod([1, 1.19, .99]))
    log_nav, log_ret = function([0, 1, 0], np.log1p([.1, .2, -.1]), fee=.01,
                               return_type="log", nav_mode="compound")
    np.testing.assert_allclose(log_nav, nav)
    np.testing.assert_allclose(log_ret, ret)
    with pytest.raises(AssertionError, match="0/1"):
        function([1, -1], [.1, .2])


def test_initial_position_avoids_duplicate_boundary_entry_cost():
    _, ret = namespace["cal_net_values"]([1, 0], [0, 0], fee=.01, initial_position=1)
    np.testing.assert_allclose(ret, [0, -.01])


def test_signal_maps_to_next_open_and_unknown_last_return_is_dropped():
    function = namespace.get("prepare_backtest")
    assert callable(function)
    df = function(prices([100., 200., 220.]), decisions(["HOLD", "BUY", "HOLD", "SELL"]))
    assert df.position.tolist() == [0, 1]
    assert df.signal_session.tolist() == ["2023-12-29", "2024-01-02"]
    np.testing.assert_allclose(df.pct, [1., .1])
    assert df.return_end.iloc[-1] == pd.Timestamp("2024-01-04T09:30:00-05:00")
    _, ret = namespace["cal_net_values"](df.position, df.pct, fee=0)
    np.testing.assert_allclose(ret, [0, .1])


def test_split_and_dividend_are_in_forward_asset_return():
    function = namespace.get("prepare_backtest")
    assert callable(function)
    df = function(prices([100., 49., 50.], splits=[1, 2, 1], dividends=[0, 1, 0]),
                  decisions(["BUY", "HOLD", "HOLD", "HOLD"]))
    np.testing.assert_allclose(df.pct, [0., 50/49-1])


def test_first_loss_is_in_drawdown_and_population_sharpe():
    assert namespace["calculate_mdd"]([.9, .8]) == pytest.approx((-.2, 1))
    assert namespace["calculate_sharpe"]([.1, .2], periods=4) == pytest.approx(6.)
    assert np.isnan(namespace["calculate_sharpe"]([0., 0.]))


def test_all_strategies_including_agent_share_evaluation_path():
    """新增 Agent 与规则策略走相同入口，比较表不能只保留焦点策略。"""
    import json
    from data import ROOT
    notebook = json.loads((ROOT / "analysis.ipynb").read_text())
    index = pd.date_range("2024-01-02", periods=2, tz="America/New_York")
    base = pd.DataFrame({"pct": [.1, -.1], "return_end": index + pd.Timedelta(days=1)}, index=index)
    frames = {("AAPL", "test", key): base.assign(position=position) for key, position in {
        "buy_hold": [1., 1.], "sma": [0., 1.], "macd": [1., 0.], "agent": [0., 0.],
    }.items()}
    scope = dict(namespace, cfg={"commission_bps": 5, "slippage_bps": 5,
                                 "annualization": 252, "risk_free_rate": 0.},
                 position_tables=frames, strategy_names={key[2]: key[2].upper() for key in frames},
                 RETURN_TYPE="simple", NAV_MODE="additive")
    cell = next(c for c in notebook["cells"] if "strategy-evaluation" in c.get("metadata", {}).get("tags", []))
    exec("".join(cell["source"]), scope)
    assert scope["metrics_table"].index.tolist() == list(frames)
    np.testing.assert_allclose(scope["metrics_table"].cumulative_return, [-.001, -.101, .098, 0.])
    assert scope["metrics_table"].strategy_name.tolist() == [key[2].upper() for key in frames]
    assert "net_values" not in base  # 每个策略独立计算，不污染共同行情。


def test_independent_test_restarts_nav_but_full_period_keeps_boundary_return():
    index = pd.DatetimeIndex(["2026-05-28 09:30", "2026-05-29 09:30", "2026-06-01 09:30"],
                             tz="America/New_York")
    frame = pd.DataFrame({
        "date": ["2026-05-28", "2026-05-29", "2026-06-01"],
        "pct": [.1, .2, .3], "position": [1., 1., 1.],
        "return_end": pd.DatetimeIndex(["2026-05-29 09:30", "2026-06-01 09:30", "2026-06-02 09:30"],
                                       tz="America/New_York"),
    }, index=index)
    select, run = namespace["select_period"], namespace["run_backtest"]
    train = run(select(frame, "2024-01-01", "2026-05-31"), .001)
    test = run(select(frame, "2026-06-01", "2026-10-09"), .001)
    full = run(select(frame, "2024-01-01", "2026-10-09"), .001)
    assert train.net_values.iloc[-1] == pytest.approx(1.099)
    assert test.net_values.iloc[-1] == pytest.approx(1.299)
    assert full.net_values.iloc[-1] == pytest.approx(1.599)
    assert full.cost.sum() == pytest.approx(.001)
    assert test.cost.sum() == pytest.approx(.001)
