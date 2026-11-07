# AAPL — Technical Analysis Report
**Analysis date:** 2026-08-05 · **Last verified close:** 311.00 · **Vendor:** B-project point-in-time (frozen rows ≤ 2026-08-05)

---

## 1. Data integrity check

I cross-checked `get_stock_data` against `get_verified_market_snapshot` for every overlapping session. **No discrepancy was found** — the 2026-08-05 row is identical in both sources (O 309.36 / H 311.71 / L 305.67 / C 311.00, volume 49,438,800), and all indicator values below reconcile with the snapshot line:

`close_50_sma 309.6542 · close_200_sma 278.8567 · close_10_ema 318.7297 · macd 2.0892 · macds 5.7230 · macdh −3.6338 · rsi 45.8378 · boll 323.7215 · boll_ub 345.8031 · boll_lb 301.6399 · atr 9.5082 · vwma 322.2765 · mfi 0.4651`

Per instructions, all exact price/indicator claims below are taken from the verified snapshot or from the indicator series that match it.

---

## 2. The defining event: a violent, unfilled event gap on 2026-07-31

The dominant fact in this dataset is the session of **2026-07-31**:

| Field | 2026-07-30 | 2026-07-31 | Change |
|---|---|---|---|
| Close | 333.43 | 308.91 | −24.52 (−7.35%) |
| Open | 333.10 | 304.81 | gap of −28.62 (−8.58%) vs prior close |
| High / Low | 334.75 / 329.59 | 310.69 / 300.00 | — |
| Volume | 74.8M | 132.5M | 1.77× prior day |

*Cause is not verifiable from the tool output* — I will not assert one. The signature (overnight gap, 1.8× volume, entire prior-session range left unfilled) is the classic footprint of a **company-specific scheduled event**, and it is worth confirming against the news calendar before sizing any position. What matters technically is what the price structure says next, because the market has spent four sessions telling us.

**The gap zone (329.59 – 333.74) is still completely unfilled.** No session since has traded above 311.80. That unfilled block is the single most important overhead supply shelf on the chart, and it is where trapped longs from July are positioned.

A useful in-sample precedent: **2026-06-25** printed a similar event gap (close 293.08 → 275.15, −6.12%, 107.0M shares, followed by 261.8M on 06-26). AAPL then spent roughly six weeks recovering to the 340.08 close of 2026-07-28. Event gaps in this name have been *repaired, not fatal* — but they have taken weeks, not days.

---

## 3. Trend structure: intermediate trend intact, short-term trend broken

### ✔ Long-term (200 SMA) — firmly bullish, and the reason not to be structurally bearish
- **close_200_sma = 278.86**, rising steadily every session (270.03 on 06-30 → 273.43 on 07-15 → 278.86 on 08-05, i.e. **+3.27% over ~5 weeks**).
- Price is **+11.52% above** the 200 SMA. This is a *wide* cushion, not a marginal one.
- **50 SMA (309.65) sits 30.80 points / 11.05% above the 200 SMA** — the golden-cross configuration remains fully intact and is not remotely threatened at current prices.

### ⚠ Intermediate (50 SMA) — flattening, and price is knife-edging it
- **close_50_sma = 309.65**; close 311.00 = **+0.44% above**.
- Slope has decelerated hard: 306.99 (07-27) → 309.30 (07-30) → 309.50 (07-31) → 309.52 (08-03) → 309.61 (08-04) → 309.65 (08-05). That is **+0.11 points over five sessions** — effectively flat.
- Interpretation: the 50 SMA has stopped rising *with* price and is now a static line. A flat 50 SMA being tested from above is a decision point, not a trend. **Holding it is the bare minimum required for the bullish case.**

### ✘ Short-term (10 EMA) — broken, and it is the active ceiling
- **close_10_ema = 318.73**; close 311.00 = **−2.43% below**.
- The 10 EMA rolled over decisively: 331.31 (07-30) → 327.24 (07-31) → 322.91 (08-03) → 320.45 (08-04) → 318.73 (08-05). Down ~12.6 points (−3.8%) in four sessions and still falling.
- Price has not closed above the 10 EMA since 2026-07-30. **The short-term trend is down until proven otherwise.**

### ✘ Volume-weighted trend — the tell
- **vwma = 322.28** vs close 311.00 → price is **−3.50% below** the volume-weighted average price of the recent window.
- VWMA rolled from 329.58 (07-30) to 322.28 (08-05). When spot sits *below* VWMA, the volume-weighted marginal buyer is **underwater** — that is textbook distribution, and it explains why every rally attempt has met supply.

**Synthesis:** three timeframes disagree. Long-term up (200 SMA), intermediate flat (50 SMA), short-term down (10 EMA + VWMA). That is a **corrective pullback inside a primary uptrend** — not yet a trend reversal, but no longer a healthy uptrend either.

---

## 4. Momentum: the most important nuance in this report

### MACD system — bearish crossover, and momentum is *still deteriorating*
| Date | MACD | Signal | Histogram |
|---|---|---|---|
| 2026-07-17 | 8.815 | 5.478 | +3.337 (peak) |
| 2026-07-29 | 9.609 (peak) | 8.437 | +1.172 |
| 2026-07-30 | 9.241 | 8.598 | +0.643 |
| 2026-07-31 | 6.891 | 8.256 | **−1.365 (crossover)** |
| 2026-08-03 | 4.534 | 7.512 | −2.978 |
| 2026-08-04 | 3.110 | 6.631 | −3.521 |
| 2026-08-05 | **2.089** | **5.723** | **−3.634** |

Two facts that must be read together:

1. **The MACD line is still above zero (2.09)**, so this is a *momentum reset within an uptrend*, not a confirmed trend-failure signal. The zero-line cross (a much more serious event) is actually still ~2 points away — but the MACD line fell 7.5 points in four sessions, so do not be complacent.
2. **The histogram is still widening negative on 2026-08-05 (−3.634 vs −3.521)** *even though price rose* (309.38 → 311.00). This is the critical caveat: **the three-day bounce has zero momentum confirmation.** The MACD line is falling faster than the signal line. Historically in this dataset that pattern resolves with either a final flush or several more sessions of basing before a durable low — it rarely marks the bottom on day three.

### RSI — neutralized, and a confirmed bearish divergence preceded the drop
- **rsi = 45.84** (snapshot), up from 44.68 (08-04) and 40.34 (08-03, the lowest reading since 39.90 on 06-29).
- **Bearish divergence (documented):** price closed at a *higher* high on 2026-07-28 (340.08) versus 2026-07-17 (333.74), while RSI made a *lower* high — 68.90 vs 71.65. That non-confirmation preceded the −7.35% air-pocket by two sessions.
- RSI never reached true overbought (>70 only on 07-16/07-17 at 71.43/71.65), so this was a grind-up that exhausted on momentum, not on a blow-off.
- At 45.84, RSI is **neutral, in the lower-middle half of its range** — there is plenty of room in *both* directions. RSI is not offering a mean-reversion buy signal, and it is not yet oversold. It is simply *not blocking* either side.

### The divergence to watch: RSI up, MACD histogram down
RSI is repairing (40.3 → 45.8) while MACD momentum is degrading. When these two disagree on a three-day bounce, **treat the bounce as unconfirmed and let price structure decide.** A close above the 10 EMA would resolve it bullishly; a failure at 311–312 with the histogram still widening would resolve it bearishly.

---

## 5. Volatility and bands: the floor is real, but the regime has shifted

### ATR — a higher-volatility regime, and position sizing must change
- **atr = 9.51** vs 8.06 on 07-30 → **+18.0% in four sessions.**
- ATR as % of price = **3.06%** (vs ~2.4% through mid-July). Expect wider intraday ranges; a "normal" 1.5×ATR day is now ~14 points.

### Bollinger structure (snapshot)
- Middle **323.72** · Upper **345.80** · Lower **301.64** → bandwidth **44.16 = 13.6% of the middle** (very wide; volatility already expanded).
- **%B = (311.00 − 301.64) / (345.80 − 301.64) = 0.21** — price sits in the **bottom quintile** of the band.
- The lower band **rose** from 276.31 (07-23) to 304.16 (07-30) and has now **turned down slightly** (301.64 on 08-05). That inflection is the band "catching" the new price range — consistent with a volatility expansion that is beginning to stabilize rather than accelerate.
- The price **closed below the middle band (323.72) on every session since 07-31**, and the middle band is now stacked almost exactly on the VWMA (322.28). That 322–324 confluence is the first real overhead wall.

### The 300–302.5 floor is the strongest technical feature on the chart
Three consecutive sessions held a tight low cluster:
- 2026-07-31 low **300.00**
- 2026-08-03 low **302.56**
- 2026-08-04 low **301.32**
- and **boll_lb = 301.64** sits inside that cluster.

Price has now bounced **+3.67% off 300.00** (to 311.00). This is a *single-episode* support test, not a validated historical level — I am explicitly **not** claiming a repeated historical bounce, because the tool data shows only this one test. But the confluence of a round number, the lower Bollinger band, and three defended sessions makes 300–302.5 the line that defines the risk.

---

## 6. Volume: the bounce is losing conviction

| Date | Close | Volume |
|---|---|---|
| 2026-07-30 | 333.43 | 74.8M |
| 2026-07-31 | 308.91 | **132.5M** (capitulation) |
| 2026-08-03 | 303.42 | 75.1M |
| 2026-08-04 | 309.38 | 68.0M |
| 2026-08-05 | 311.00 | **49.4M** (lowest since 07-23's 40.8M) |

Average volume of the last 10 sessions ≈ **64.6M** vs ≈ **48.3M** for the prior 10 — a **~34% expansion** driven almost entirely by the event itself (computed from the provided rows).

**The bearish read:** the rally from 303.42 → 311.00 occurred on *declining* volume (75.1M → 68.0M → 49.4M). Rallies that shrink into resistance are typically supply-dominated. This aligns with spot trading below VWMA (322.28) and with the still-widening MACD histogram.

**The bullish counter-read:** post-capitulation volume dry-up *can* mark a low. If a session arrives with a close > 311.80 **on above-average volume**, the dry-up was accumulation rather than indifference. That is the confirmation trigger.

**MFI = 0.465** (below neutral 0.50) corroborates: money flow is mildly negative, not panicked.

---

## 7. Actionable levels

Given ATR = 9.51, treat any level within ±0.5×ATR (~4.75 points) as a **zone**, not a line.

**Support**
| Zone | Source | Significance |
|---|---|---|
| **305.67 – 309.65** | 08-05 low (305.67) + rising-then-flat 50 SMA (309.65) | Must hold for the bounce thesis; the 50 SMA is the pivot |
| **300.00 – 302.56** | 07-31 low 300.00, 08-03 low 302.56, 08-04 low 301.32, boll_lb 301.64 | **Primary risk line.** Confluence of round number + lower band |
| **275.15 – 278.86** | 200 SMA (278.86) + 06-25 close (275.15) / 06-25 low (273.75) | Structural bull-market line; a close below ends the primary uptrend |

**Resistance**
| Zone | Source | Significance |
|---|---|---|
| **311.71 – 311.80** | 08-03 high 311.80, 08-05 high 311.71 | Immediate lid; price closed 311.00, right underneath |
| **318.73** | 10 EMA | **The trend-repair trigger.** First close above = short-term downtrend broken |
| **322.28 – 323.72** | VWMA 322.28 + Bollinger middle 323.72 | Heavy confluence; where underwater buyers sell |
| **329.59 – 333.74** | 07-30 low 329.59 → 07-30 close 333.43 (gap zone) | **Unfilled gap; the real test of whether the event is digested** |
| **344.57** | 07-29 high (window high) | Prior swing high / full recovery |

---

## 8. Scenarios and trades

**Scenario A — Constructive base (needs confirmation):** Close > **318.73 (10 EMA)** on volume > ~65M. Targets 322–324 first, then 329.6–333.7 gap fill. Invalidation: close back below 305.67.
**Scenario B — Range/two-way chop (base case given mixed signals):** Price oscillates 302–319, digesting the gap while the flat 50 SMA catches up. Best handled by *not* trading the middle; buy 303–306 / sell 317–319, or stand aside.
**Scenario C — Trend break (needs 300 to fail):** Close below **300.00** opens 290s and puts 278.86 (200 SMA) in play. The MACD histogram's continued widening is the leading warning for this branch.

**Suggested risk framework**
- Long entry zones: (i) 305–307 on a hold of the 50 SMA; or (ii) **breakout > 311.80 with volume**.
- Stops: 1×ATR ≈ 9.5; 1.5×ATR ≈ 14.3. A long at 311 with a stop at 300.00 risks **11.0 points ≈ 1.16×ATR** — defensible. Stop below 299.5 invalidates Scenario A entirely.
- Position size using ATR% = 3.06%: a 1×ATR stop on a 1% portfolio risk implies roughly **1/3 the notional exposure** you'd take in a 1% ATR regime.
- **Do not add to longs while MACD histogram makes new lows** (−3.634 on 08-05). That is the single cleanest veto in this setup.
- Small housekeeping note: the data shows dividends of 0.26 on 2025-11-10, 0.26 on 2026-02-09 and 0.27 on 2026-05-11 — a quarterly cadence implying a possible **mid-August ex-dividend** (~0.09% at current price). Immaterial to the thesis, but relevant for tight option/dividend-assignment positioning.

---

## 9. Why these eight indicators

| Indicator | Value (2026-08-05) | Why it earns a slot here |
|---|---|---|
| **close_10_ema** | 318.73 | The active short-term trend line and the specific level that must be reclaimed; it *is* the current resistance |
| **close_50_sma** | 309.65 | Price is knife-edging it (+0.44%) after its slope went flat — the immediate decision line between Scenario A and C |
| **close_200_sma** | 278.86 | Long-term regime anchor; +11.5% cushion proves this is a correction, not a bear market, and provides the deepest support reference |
| **macd** | 2.089 (signal 5.723) | Confirms the bearish crossover on 07-31 and — critically — that the line remains above zero, i.e. momentum reset, not trend failure |
| **macdh** | −3.634 | The single best veto signal: still widening negative through a 3-day price bounce, meaning the bounce is unconfirmed |
| **rsi** | 45.84 | Neutralizes both extremes and documents the 07-17→07-28 bearish divergence (71.65 → 68.90) that flagged the breakdown; complements MACD timing |
| **atr** | 9.51 (+18% in 4 sessions) | Volatility regime has changed; it sets every stop and position size quoted above and explains the 300→311 range width |
| **vwma** | 322.28 | Price −3.50% below VWMA = volume-weighted buyers are underwater = distribution. Not redundant with the SMAs because it weights *volume*, explaining why rallies keep failing |
| *Bollinger (supplementary)* | mid 323.72 / ub 345.80 / lb 301.64 | Used as an overlay only: the 301.64 lower band corroborates the 300–302.5 floor, and the middle band at 323.72 stacks with VWMA |

Deliberately excluded: `boll_lb`/`boll_ub` as standalone picks (subsumed by the VWMA/ATR volatility read), and `mfi` (0.465, directionally redundant with RSI and VWMA here).

---

## 10. Bottom line

AAPL is in a **corrective phase within an intact primary uptrend**, sitting exactly on the fence. The bullish evidence is genuine: price is **+11.5% above a rising 200 SMA**, the 50-over-200 spread is **+11.05%**, RSI at **45.84** has room to run, and a **300.00–302.56 floor** was defended three times with the lower Bollinger band at **301.64** underneath it. The bearish evidence is equally genuine: price is **−2.4% below a falling 10 EMA**, **−3.5% below VWMA (322.28)**, below the Bollinger middle (**323.72**), with a **MACD histogram that widened to −3.63 on the very day price rallied**, an **unfilled 329.59–333.74 gap**, and a bounce on **shrinking volume (75.1M → 68.0M → 49.4M)**.

The correct posture is **disciplined patience, not conviction**. The 300–302.5 zone defines the risk; the 10 EMA at 318.73 defines the repair. Until one of them resolves, this is a two-way tape where the 50 SMA at 309.65 is the fulcrum — and it is flat, which means the market has not decided either.

---

### Summary Table

| Dimension | Reading | Signal | Key Level(s) |
|---|---|---|---|
| Primary trend (200 SMA) | 278.86, rising +3.27% in 5 wks; price +11.52% above | **Bullish** | Support 275.15–278.86 |
| Intermediate trend (50 SMA) | 309.65, flat (+0.11 over 5 sessions); price +0.44% above | **Neutral / decision point** | Fulcrum 309.65 |
| Short-term trend (10 EMA) | 318.73, falling −12.6 pts in 4 sessions; price −2.43% | **Bearish** | Repair trigger 318.73 |
| Volume-weighted trend (VWMA) | 322.28; price −3.50% → buyers underwater | **Bearish (distribution)** | Wall 322.28–323.72 |
| MACD | 2.089 vs signal 5.723; bearish cross 07-31; still >0 | **Bearish, but not trend-failure** | Zero line 2.1 pts below |
| MACD histogram | −3.634, widening (was −3.521) despite price up | **Bearish veto — bounce unconfirmed** | Turn positive = first real tell |
| RSI | 45.84 (from 40.34); bearish divergence 07-17→07-28 (71.65→68.90) | **Neutral** | 40 floor / 55 for momentum |
| Bollinger | mid 323.72, ub 345.80, lb 301.64; %B = 0.21 | **Lower-quartile, wide bands** | 301.64 corroborates floor |
| ATR | 9.51 = 3.06% of price, +18% in 4 sessions | **Volatility regime shift** | 1×ATR 9.5 / 1.5×ATR 14.3 |
| Volume | Jul-31 capitulation 132.5M; bounce on 75.1→68.0→49.4M | **Bearish (weak demand)** | >65M needed to confirm upside |
| Unfilled gap | 329.59 – 333.74 (07-30 low → 07-31 open) | **Overhead supply shelf** | First target on Scenario A |
| **Net verdict** | Corrective pullback inside a primary uptrend; momentum not yet repaired | **Neutral / wait** | Risk line **300.00**; trigger **318.73** |