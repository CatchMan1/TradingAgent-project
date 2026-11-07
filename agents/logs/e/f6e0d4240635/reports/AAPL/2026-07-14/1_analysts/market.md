# AAPL — Technical Analysis Report (as of 2026-07-14)

## 1. Verified Market Snapshot (source of truth)

Per the verified snapshot for **AAPL on 2026-07-14**:

| Field | Value |
|---|---|
| Open | 313.76 |
| High | 316.19 |
| Low | 311.91 |
| **Close** | **314.86** |
| Volume | 36,336,800 |
| 50-SMA | 299.58 |
| 200-SMA | 273.08 |
| 10-EMA | 309.68 |
| MACD / Signal / Hist | 5.474 / 3.145 / 2.329 |
| RSI (14) | 61.45 |
| Bollinger Mid / Upper / Lower | 300.37 / 325.61 / 275.14 |
| ATR | 7.90 |
| VWMA | 294.60 |

All OHLCV and indicator values below are drawn from this verified snapshot and the point-in-time indicator series; where I compute a derived figure (e.g., a percentage move, %B), the dates and raw prices used are shown.

## 2. Selected Indicators & Rationale

I selected **8 complementary indicators** spanning trend, momentum, volatility, and volume — deliberately avoiding redundancy (e.g., I use MACD rather than stacking RSI + StochRSI):

1. **close_50_sma** — medium-term trend and dynamic support.
2. **close_200_sma** — long-term trend confirmation / golden-cross structure.
3. **close_10_ema** — short-term momentum and near-term entry timing.
4. **macd** — momentum regime and crossover timing (referencing its signal/histogram data I also have).
5. **rsi** — overbought/oversold and momentum divergence checks.
6. **boll_ub** — breakout/overbought envelope (read with the mid 300.37 and lower 275.14 bands).
7. **atr** — volatility-scaled stop placement and position sizing.
8. **vwma** — volume-weighted trend confirmation (important given the huge late-June volume event).

## 3. Trend Analysis

**Structure is unambiguously bullish and in textbook alignment.** As of 2026-07-14, price (314.86) sits above every selected moving average:

- Price **> 10-EMA (309.68) > 50-SMA (299.58) > 200-SMA (273.08)** — a fully stacked, "perfect order" uptrend.

- **Price vs 50-SMA:** +15.28 points, i.e. roughly **+5.1%** above the 50-SMA. The 50-SMA has risen every session from **280.14 on 2026-06-04 to 299.58 on 2026-07-14**, confirming a rising medium-term trend.
- **Price vs 200-SMA:** +41.78 points, roughly **+15.3%** above the 200-SMA. The 200-SMA is also rising (264.81 on 2026-06-04 → 273.08 on 2026-07-14). The 50-SMA sitting well above a rising 200-SMA reflects a durable **golden-cross regime**, and the gap is widening (bullish trend acceleration).
- **Price vs VWMA (294.60):** +20.26 points (**~+6.9%**). Price leading a rising VWMA confirms the uptrend is volume-supported rather than a thin drift.

**Medium-term trajectory:** The stock bottomed at a close of **246.63 (2026-03-30)** and rallied through the spring, peaking at a close of **315.20 (2026-06-02)**. A corrective pullback followed to a close of **275.15 on 2026-06-25** (with the intraday low 273.75 that day), after which it has rallied hard again — **+15.3% from the 275.15 close (6/25) to the 317.31 close (7/13)** — printing the **highest close in the entire provided window (back to Dec 2025)**. So AAPL is trading at the top of its sampled range, not recovering from a drawdown.

## 4. Momentum Analysis

- **MACD has just completed a fresh bullish crossover and re-acceleration.** The MACD line fell negative in late June — crossing below zero at **-1.59 on 2026-06-25**, bottoming near **-2.92 on 2026-06-29** — then turned up. The MACD line crossed back above its signal line around **2026-07-07/07-08** (MACD 0.878 vs signal -0.582 on 7/6 → MACD 2.96 vs signal 0.529 on 7/8). It now reads **MACD 5.474 vs signal 3.145, histogram +2.329 and expanding**, a clean bullish momentum confirmation.
- **RSI(14) at 61.45** — constructive but **not overbought**. RSI recovered from a near-oversold **32.20 on 2026-06-25** to a local peak of **64.16 on 2026-07-13**, now easing to 61.45 with the 7/14 pullback. Trading in the 55–65 zone during an uptrend is characteristic of healthy momentum with room before the 70 overbought threshold. There is no bearish divergence flagged by the series (RSI made a higher high into 7/13 alongside price).

## 5. Volatility & Band Analysis

- **Bollinger position:** Price (314.86) sits between the mid-band (300.37) and upper band (325.61). Approximate **%B ≈ 0.79** ((314.86−275.14)/(325.61−275.14)) — in the **upper third of the band**, consistent with an uptrend pushing toward the upper envelope without yet piercing it.
- **Bands are expanding upward:** The upper band has lifted from **312.68 (2026-07-01) to 325.61 (2026-07-14)**, while the lower band is roughly flat (**277.09 → 275.14**). This upward "unfolding" of the bands signals volatility expanding in the direction of the trend — typically a continuation, not exhaustion, signal — but it also means price is closer to stretched territory (the upper band at 325.61 is ~**+3.4%** above the current close).
- **ATR = 7.90**, down slightly from the July peak of **8.74 on 2026-07-02**. Volatility remains elevated (the June 25–26 shakeout pushed ATR from ~7.0 to ~8.2) but is now gently contracting — a sign the post-pullback rally is steadying.

## 6. Volume Analysis

- **VWMA (294.60) is rising** and price is comfortably above it, confirming buyers are in control on a volume-weighted basis.
- **The standout event:** volume exploded to **107.0M on 2026-06-25** and **261.8M on 2026-06-26** (versus a typical 35–75M). That late-June spike coincides with the sharp low at 275.15 (6/25) followed by an immediate bounce — consistent with a capitulation/rebalancing flush that marked the swing low rather than the start of a downtrend. Since then, volumes have normalized.
- **The 7/14 pullback came on lighter volume (36.3M)** versus the prior up-days (e.g., 48.1M on 7/9, 43.3M on 7/13) — a mild, low-conviction dip rather than distribution.

## 7. Actionable Insights

**Primary bias: constructive/long, trend-following.** All trend and momentum evidence aligns bullishly. This favors buying pullbacks rather than chasing strength into the upper band.

- **Entry zones (dip-buying):** The nearest dynamic support is the **10-EMA at ~309.68**; a pullback holding that level keeps the short-term trend intact. A deeper but still constructive zone is the **confluence around 299–300** where the **50-SMA (299.58)** and **Bollinger mid-band (300.37)** sit together — a high-quality support cluster.
- **Resistance/upside targets:** The **7/13 high of 323.45** and the **upper Bollinger band at 325.61** form the immediate ceiling. A decisive close above ~325.6 on rising volume would signal a breakout extension.
- **Stop placement (volatility-scaled):** With ATR at 7.90, a swing stop of roughly **1.5× ATR (~$12)** below entry is reasonable. Structurally, a close back below the **50-SMA/300 zone** would invalidate the current bullish structure and warrant standing aside.
- **Momentum triggers to watch:** Keep the position while **MACD histogram stays positive/expanding** and **RSI holds above ~50**. A MACD signal-line cross back down, or RSI failure below 50, would be the first warning of momentum decay. RSI pushing above ~70 into the upper band would argue for trimming rather than adding.

**Key risk:** Price is at the top of its range and in the upper band with elevated (though moderating) volatility; the 7/14 session showed the first down-close (−0.77% from 317.31 to 314.86) on the new high. This is a "buy dips, don't chase" environment, not a breakout-chase one, until 325+ is cleared on volume.

## 8. Key Levels & Signals Summary

| Dimension | Selected Indicator | Reading (2026-07-14) | Interpretation | Actionable Level |
|---|---|---|---|---|
| Medium trend | close_50_sma | 299.58 (rising) | Uptrend; price +5.1% above | Dynamic support ~299–300 |
| Long trend | close_200_sma | 273.08 (rising) | Golden-cross regime; price +15.3% | Strategic bull confirmation |
| Short momentum | close_10_ema | 309.68 (rising) | Near-term trend intact; price +1.7% | First pullback support ~310 |
| Momentum | macd | 5.474 (hist +2.329, expanding) | Fresh bullish crossover, re-accelerating | Bullish while hist > 0 |
| Momentum strength | rsi | 61.45 | Constructive, not overbought | Watch 70 (overbought) / 50 (decay) |
| Volatility band | boll_ub | 325.61 (expanding up) | Price in upper band, %B ≈ 0.79 | Breakout trigger >325.6 |
| Volatility/risk | atr | 7.90 (moderating) | Elevated but cooling | Stop ≈ 1.5×ATR (~$12) |
| Volume trend | vwma | 294.60 (rising) | Volume-confirmed uptrend; price +6.9% | Confirmation support |
| Structure | Price | 314.86 (7/14 close) | New-high territory, first minor down day | Range high 323.45; support 309.7 / 300 |

**Bottom line:** AAPL is in a strong, volume-confirmed, fully-stacked uptrend trading at the top of its range. Momentum (MACD crossover, RSI ~61 with room to run) supports continuation, but the upper-band positioning and elevated ATR argue for disciplined dip-buying at the 10-EMA (~310) or 50-SMA/mid-band confluence (~300) with stops managed around ATR-based levels, rather than chasing into 325.