import pytest

from tradingagents.llm_clients.factory import _coerce_timeout, build_llm_kwargs


@pytest.mark.parametrize(("value", "expected"), [(120, 120.0), ("30", 30.0), (2.5, 2.5)])
def test_timeout_is_validated_and_forwarded(value, expected):
    assert _coerce_timeout(value) == expected
    assert build_llm_kwargs({"llm_provider": "deepseek", "llm_timeout": value})["timeout"] == expected


@pytest.mark.parametrize("value", [0, -1, "bad", True])
def test_invalid_timeout_is_rejected(value):
    with pytest.raises(ValueError):
        _coerce_timeout(value)
