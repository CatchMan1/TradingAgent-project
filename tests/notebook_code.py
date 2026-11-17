"""Expose the same backtest functions used by both notebooks."""
import backtest

namespace = vars(backtest)
signals = backtest.signals
