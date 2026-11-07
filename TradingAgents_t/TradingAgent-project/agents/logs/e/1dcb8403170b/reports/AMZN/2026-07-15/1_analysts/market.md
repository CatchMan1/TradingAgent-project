# AMZN — Multi-Indicator Technical Analysis (as of 2026-07-15)

## Data integrity note
The `get_stock_data` OHLCV series and the `get_verified_market_snapshot` agree exactly on the latest session: **2026-07-15 close of $254.96 (open $249.75, high $256.48, low $249.75, volume 45.24M)**. All indicator values below are taken from the verified snapshot (source of truth); the time-series pulls from `get_indicators` match the snapshot's latest values. No conflicts to flag.

---

## 1. Market context / price structure
AMZN has just completed a **V-shaped recovery from a June correction**. The stock bottomed at a close of **$227.01 on 2026-06-25** (intraday low $225.55) and has climbed to $254.96 by 2026-07-15 — a gain of roughly **+12.3% in about three weeks**. Two features of that low are notable and tool-supported:
- **2026-06-26 traded 248.4M shares** — a dramatic volume spike versus the ~30–70M typical of surrounding sessions — consistent with capitulation/absorption at the low.
- The recovery accelerated into the latest session: 2026-07-15 rose **+$7.47 (+3.02%)** from the 2026-07-14 close of $247.49, printing the highest close since early June (last close above it was $256.52 on 2026-06-02).

Broader context: the stock's 2026 swing high was the **$278.56 intraday print on 2026-05-05**, so at $254.96 AMZN remains ~8.5% below that peak, i.e., still in a recovery/repair phase rather than at new highs. Earlier in the year there was a sharp **earnings-type gap down on 2026-02-05/06** (close fell from $232.99 on 2026-02-04 to $210.32 on 2026-02-06 on 179.2M shares), from which the stock spent Q1–Q2 rebuilding.

---

## 2. Selected indicators and rationale
I chose **8 complementary indicators** spanning trend (three timeframes), momentum, breakout/volatility, and risk:

| # | Indicator | Role in this read |
|---|-----------|-------------------|
| 1 | **close_10_ema** | Short-term momentum / responsive entry timing |
| 2 | **close_50_sma** | Medium-term trend & immediate dynamic support |
| 3 | **close_200_sma** | Long-term trend benchmark (golden-cross context) |
| 4 | **macd** | Momentum regime shift (zero-line & crossover) |
| 5 | **macds** | Signal line to confirm the MACD crossover |
| 6 | **rsi** | Overbought/oversold & momentum strength |
| 7 | **boll_ub** | Breakout zone / overbought stretch marker |
| 8 | **atr** | Volatility-based stop & position sizing |

I deliberately avoided stacking redundant oscillators (RSI alone, not RSI+stochrsi) and used VWMA, MFI, and the Bollinger middle/lower bands as **supplementary confirmation** in the narrative rather than as primary selections.

---

## 3. Trend analysis (moving averages)

**Bullish alignment, freshly reclaimed.**
- **Price $254.96 > 50-SMA $253.10 > 200-SMA $233.79** — a full bullish stack. The 50-SMA sits ~$19.3 above the 200-SMA, so the long-term "golden-cross" structure is intact.
- **Price just reclaimed the 50-SMA** on 2026-07-15 (first decisive close above it since early June). However, note the 50-SMA has been *declining* (from $256.64 on 2026-06-17 to $253.10 now) as the May highs roll off the window — so the trend is in the very early stages of turning back up, not yet confirmed by the medium-term average itself.
- **10-EMA $246.40**, rising steadily (from $236.70 on 2026-06-26) and **well below price** — confirming accelerating short-term momentum. Price is ~$8.6 above it, which is a stretched short-term reading.
- **200-SMA $233.79**, gently rising (+~1.2 pts over the month) — the long-term uptrend remains intact and provides a deep-value reference far below.

**Read:** Trend is turning constructive across all three horizons, but the fastest read (price far above the 10-EMA) argues the move is extended near-term.

---

## 4. Momentum analysis (MACD & RSI)

**MACD — genuine regime shift:**
- The **MACD histogram turned positive on 2026-07-01 ($+0.47)** and has expanded to **$+2.12 by 2026-07-15** — strengthening bullish momentum.
- The MACD line crossed above its signal line around that 2026-07-01 turn (line −5.06 vs signal −5.53) and has now **crossed above zero** ($+0.26 on 2026-07-15 vs signal −1.86) — the first positive MACD print in the visible window. A zero-line cross is a meaningful confirmation that momentum has flipped from bearish to bullish, not just a bounce.

**RSI — recovering with room:**
- RSI climbed from **33.6 on 2026-06-25** to **60.14 on 2026-07-15**. This is a clean recovery out of near-oversold territory.
- At 60.1, RSI is **not yet overbought (70)** — meaning there is still head-room before the classic overbought trigger. In a strengthening uptrend, RSI can push into the 65–70 zone.

---

## 5. Volatility & breakout analysis (Bollinger, ATR)

**Bollinger — squeeze resolving upward, price at the upper band:**
- Bands contracted sharply from mid-June (upper $280.04 / lower $232.64 on 2026-06-15, width ~$47) to now (upper **$254.80** / lower **$227.95**, width ~$26.9) — a classic **volatility squeeze**.
- On 2026-07-15, price ($254.96) **closed right at / marginally above the upper band ($254.80)** — %B ≈ 1.01. This is a **breakout signal** (squeeze resolving higher), but also flags short-term overbought tension. Watch whether price "walks the band" (continuation) or reverts toward the **middle band ($241.38)**.
- The middle band bottomed near $239.68 on 2026-07-08 and is now curling up — consistent with an emerging upswing.

**ATR — volatility compressing (good for risk control):**
- ATR is **$7.48 (~2.9% of price)**, down from $8.59 on 2026-06-29. Compressing volatility during an advance is constructive.
- Practical sizing: 1.5× ATR ≈ **$11.2**, 2× ATR ≈ **$15.0**.

---

## 6. Volume confirmation (supplementary)

- **VWMA $238.81** (rising from a ~$236.5 base) sits well below price — the uptrend is **volume-supported**, and VWMA turning up signals accumulation.
- **MFI ≈ 76.6** — above 70, indicating strong but **overbought** money-flow. This is the main cross-check caution: near-term money flow is hot.

---

## 7. Actionable insights

**Bull case (trend continuation):**
- Reclaimed 50-SMA + rising 10-EMA, MACD zero-cross with expanding histogram, and a Bollinger squeeze resolving upward = momentum is genuinely turning.
- A **daily close above $256.48 (today's high) / clearing the $257–261 early-June congestion** would validate the breakout, opening a path toward the **$275–278 May highs**.
- Trend/momentum traders: entry on a break-and-hold above ~$256.5 with volume; stop below the **10-EMA ~$246** (or ~2× ATR ≈ $15 → ~$240).

**Caution / pullback case:**
- Price is stretched (≈$8.6 above the 10-EMA), riding/exceeding the upper Bollinger band, RSI ~60 rising fast, and MFI ~76.6 overbought — a **short-term pullback or consolidation is a live risk**.
- The 50-SMA is still slightly declining, so the medium-term trend is not yet re-verified.
- Retest/dip buyers: better risk-adjusted entries on a pullback into **$246–248** (10-EMA / prior breakout shelf), with the **Bollinger mid $241.38** and **VWMA $238.81** as the next supports.

**Key levels (all tool-derived):**
- **Resistance:** $256.48 (today's high) → $254.80 (upper Bollinger) → $257–261 (early-June congestion).
- **Support 1:** $253.10 (50-SMA, immediate). **Support 2:** $246.40 (10-EMA). **Support 3:** $241.38 (Boll mid) / $238.81 (VWMA). **Deep support:** $233.79 (200-SMA).

**Net stance:** Constructive/leaning bullish on momentum and trend repair, but **do not chase into the upper band at RSI 60** — prefer breakout confirmation above $256.5 or a disciplined dip-buy near the 10-EMA ($246) with stops sized off ATR ($7.48).

---

## 8. Summary table

| Dimension | Indicator | Latest value (2026-07-15) | Signal | Interpretation |
|-----------|-----------|---------------------------|--------|----------------|
| Short-term trend | close_10_ema | 246.40 (rising) | Bullish | Price ~$8.6 above; short-term extended |
| Medium-term trend | close_50_sma | 253.10 (slightly falling) | Bullish (reclaimed) | Price just back above it; 50-SMA still rolling over |
| Long-term trend | close_200_sma | 233.79 (rising) | Bullish | Golden-cross intact; deep support |
| Momentum | macd | +0.26 | Bullish | First zero-line cross; regime shift |
| Momentum confirm | macds | −1.86 | Bullish | MACD above signal; upward slope |
| Momentum | rsi | 60.14 | Neutral-Bullish | Recovering, room to 70 |
| Breakout/volatility | boll_ub | 254.80 | Breakout (stretched) | Price at/exceeds upper band; %B ≈1.01 |
| Risk/volatility | atr | 7.48 (~2.9%) | — | Compressing; 2×ATR stop ≈ $15 |
| Volume (supp.) | vwma | 238.81 (rising) | Bullish | Uptrend volume-confirmed |
| Money flow (supp.) | mfi | 76.6 | Caution | Overbought (>70) |

**Bottom line:** AMZN is in a strong short-term recovery with bullish momentum (MACD zero-cross, expanding histogram, RSI 60) and an intact long-term uptrend (50>200 SMA). The immediate risk is that price is stretched against the upper Bollinger band with overbought money flow (MFI 76.6), favoring either a breakout confirmation above **$256.5** or a disciplined dip-buy near the **10-EMA ($246)** rather than chasing at current levels.