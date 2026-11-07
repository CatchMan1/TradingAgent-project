# AAPL — Technical Analysis Report
**As of the close of 2026-07-21 | Verified reference price: $327.74**

---

## 1. Data integrity check (done first)

I pulled the full OHLCV series (`get_stock_data`, 2025-12-01 → 2026-07-21, 159 rows) and then the deterministic verification snapshot for 2026-07-21. **All overlapping rows match exactly** — no discrepancy between the two sources. Every exact price, band, and indicator value quoted below is taken from the verified snapshot, which is the source of truth. Where I quote historical comparisons, the date and price come directly from the frozen CSV.

**Latest verified session (2026-07-21):**

| Field | Value |
|---|---|
| Open | 323.13 |
| High | 329.60 |
| Low | 322.22 |
| **Close** | **327.74** |
| Volume | 41,338,900 |
| Prior close (2026-07-20) | 326.59 |

---

## 2. Indicator selection and why (8 chosen)

| # | Indicator | Verified value (2026-07-21) | Why it earns a slot |
|---|---|---|---|
| 1 | `close_10_ema` | 322.21 | Short-term trend/momentum arbiter; defines the pullback-entry shelf in a fast tape |
| 2 | `close_50_sma` | 304.24 | Medium-term trend spine and the first real structural support below price |
| 3 | `close_200_sma` | 274.94 | Long-term regime filter; confirms the primary bull structure |
| 4 | `macd` | 8.927 | Trend/momentum crossover engine (currently above signal) |
| 5 | `macdh` | 2.214 | Momentum **acceleration** — the key read on whether the July thrust is fading |
| 6 | `rsi` | 64.54 | Overbought/oversold and, critically, medium-term divergence detection |
| 7 | `boll_ub` / `boll_lb` (with `boll` middle 308.48) | 344.09 / 272.87 | Volatility envelope: shows extreme band width (event-driven regime) and %B position |
| 8 | `atr` | 8.206 | Position sizing and stop placement; ATR has expanded ~41% since late May |
| — | `vwma` | 317.27 | Volume-weighted confirmation — separates real accumulation from drift |

Redundancy avoided: I did **not** stack `rsi` with a stochastics-type oscillator, and I used `macdh` rather than also pulling `macds` (the signal line is exactly derivable: 8.927 − 2.214 = **6.713**, which matches the snapshot's `macds` of 6.7129).

---

## 3. The dominant narrative: a violent V-recovery into a fresh record high, now consolidating

AAPL's last six months are a textbook **high-volatility, high-beta trend** that has repeatedly shaken out weak hands and then gone higher:

1. **January washout** — close 271.86 (2025-12-31) → **246.70 (2026-01-20)**, the intraday low that day was **243.42**, the lowest print in the dataset.
2. **February failure** — rally to a 280.91 high (2026-02-06), then a **single-session gap-down on 2026-02-12**: close 275.50 → **261.73 (−5.0%)**, next day's low 255.45.
3. **March basing** — a long chop between roughly 246 and 267, with the dataset's **lowest close at 246.63 on 2026-03-30**.
4. **May–June leg up** — 246.63 → **315.20 close on 2026-06-02**, with a 317.40 intraday high on 2026-06-08.
5. **June shakeout** — 2026-06-25: close 293.08 → **275.15 (−6.1%)** on **107.0M** shares, low 273.75; the next session (2026-06-26) traded **261.8M** shares — by far the largest volume in the entire dataset, characteristic of a capitulation/rebalance event.
6. **July recovery to new highs** — from that 273.75 low, a **+19.7% run to 327.74**, including a **+4.02% breakout day on 2026-07-15** (close 314.86 → 327.50 on 61.0M shares) that cleared the June high zone, then 333.26 (07-16) and a record close of **333.74 on 2026-07-17** (intraday high 334.99).

So the current price is **1.8% below the record close** and **2.2% below the record intraday high**, having just absorbed a sharp two-day wobble.

---

## 4. Layer-by-layer read

### 4.1 Trend structure — unambiguously bullish, but stretched
- **Price (327.74) > 10 EMA (322.21) > 50 SMA (304.24) > 200 SMA (274.94).** Perfect bullish stacking, no exceptions.
- **50 SMA vs 200 SMA:** 304.24 vs 274.94 — the medium-term average sits **10.7% above** the long-term average. The golden-cross regime is deeply entrenched and both averages are still **rising**: 50 SMA from 291.15 (2026-06-25) to 304.24; 200 SMA from 269.21 (2026-06-25) to 274.94.
- **But the extension is large:** price is **+7.7% above the 50 SMA** and **+19.2% above the 200 SMA**. Historically in this dataset that is the upper end of the stretch — on 2026-05-28, when price closed 312.51 with the 50 SMA at ~274.04, the extension was ~14%; the June shakeout promptly cut it back. This is a *sizing* caution, not a direction caution.
- **10 EMA slope is flattening:** its daily increments went from +3.70 (07-15) → +3.11 (07-16) → +3.11 (07-17) → +1.25 (07-20) → **+1.23 (07-21)**. The short-term trend is intact but decelerating — consistent with a pause rather than a reversal so far.

### 4.2 Momentum — positive and re-acceleration risk now the key variable
- **MACD 8.927 vs signal 6.713**, above signal since the **2026-07-02** re-cross (histogram flipped from −1.25 on 07-01 to +0.26 on 07-02). The MACD line itself went **−2.92 (2026-06-29) → +8.93 (2026-07-21)**, one of the sharpest momentum inflections in the six-month history.
- **The warning flag:** the histogram **peaked at 3.337 on 2026-07-17** and has since contracted to 2.724 (07-20) then **2.214 (07-21)**. Two consecutive declines = momentum *deceleration* inside an intact uptrend. This is the classic "trend fine, thrust fading" configuration for a 1–3 week consolidation.
- **RSI 64.54**, down from **71.65 on 2026-07-17**. It is not overbought, and there is room to run to the 70s before the trend gets frothy again.
- **Medium-term bearish RSI divergence worth watching:** the **2026-05-28 close of 312.51 carried an RSI of 79.79**, whereas the **higher 2026-07-17 close of 333.74 carried RSI of only 71.65**. Higher price, lower momentum — a genuine negative divergence over an ~7-week window. It has not resolved into a decline (price is higher still), but it argues that each further push upward is being bought with less force.

### 4.3 Volatility — expanded, and that changes everything about position sizing
- **ATR 8.206**, i.e. **2.50% of price** per day. The ATR path: ~5.57 (2026-05-29) → 7.88 (06-25) → **8.74 peak (2026-07-02)** → 8.21 now. Volatility has expanded ~47% from the late-May calm and has *not* mean-reverted despite the price making new highs.
- **Bollinger envelope is exceptionally wide:** upper **344.09**, middle **308.48**, lower **272.87** → total width ~**$71.2 or 23.1% of the middle band**. The upper band has risen from 312.31 (07-02) to 344.09 (07-21) — bands are fanning outward, the signature of a trending, volatile regime rather than a squeeze.
- **%B (position in band):** (327.74 − 272.87) / (344.09 − 272.87) = **0.77**. Upper-quartile of the envelope. Note the important subtlety: on 2026-07-17, the close of 333.74 was still **$5.46 below** the upper band (339.20); price has **not** been "riding the band" or tagging the upper extreme, so a reach toward 344 is not mechanically excluded.
- Practical translation: **1 ATR ≈ $8.21, 2 ATR ≈ $16.41.** Any stop tighter than ~$8 simply gets taken out by normal noise in this regime.

### 4.4 Volume — the strongest bullish tell in the report
- **VWMA 317.27 vs close 327.74.** Price above the volume-weighted average = buyers on high-volume days are in profit and in control.
- The VWMA has turned up sharply at exactly the right moment: 292.83 (07-09) → 296.42 (07-15) → 300.72 (07-16) → **310.27 (07-17)** → 314.02 (07-20) → **317.27 (07-21)**. The gap between price and VWMA has narrowed to a modest **+3.3%**, meaning the recent rally is *volume-supported*, not a thin drift.
- **Breakout volume profile:** the 2026-07-15 breakout came on **61.0M**, followed by **63.0M (07-16)** and **63.4M (07-17)** — expanding volume into higher prices. The subsequent pullback volume **contracted** to 53.5M (07-20) and **41.3M (07-21)**, roughly 21% below the trailing 3-day breakout average. Declining volume on a pullback inside an uptrend is the bullish signature; distribution would have shown heavy volume on the down days.

### 4.5 Candlestick micro-structure of the last three sessions
- **2026-07-20:** gapped open at 333.51, high 333.71, low 323.68, **closed 326.59** — a wide-range down day closing near the low (a short-term distribution/outside-bar failure at the highs).
- **2026-07-21:** opened 323.13 (below the prior day's low), low 322.22, high 329.60, **closed 327.74** — i.e. it **recovered above the prior close and closed in the upper half of the range** on lower volume. That is a constructive absorption of the 07-20 supply.
- Net: a **near-term range of 322.22 – 334.99** has formed. Which side breaks first is the tactical trigger.

---

## 5. Actionable plan

### Bias: **constructive / trend-following long**, with a tactical allowance for a 1–2 week consolidation because the MACD histogram has rolled over and price is 7.7% extended above the 50 SMA.

**Scenario A — Continuation (base case, ~60%).**
Trigger: a daily close **above 333.74** (the 07-17 record close) with volume ≥ ~60M.
- Entry: on the break, or on a reclaim of 330 intraday.
- First target: **344.09** — the rising Bollinger upper band (a moving target; re-read it each session).
- Invalidation: daily close back below **322.21** (10 EMA).
- ATR-based stop: entry − 1.5×ATR ≈ **−$12.3**.

**Scenario B — Pullback to buy (preferred risk/reward, ~30%).**
The higher-probability *entry* is not the breakout; it is the dip.
- **Tier 1 zone: 322.22 – 324** (07-21 low and 10 EMA). Shallow, aggressive accumulation.
- **Tier 2 zone: 308.50 – 313.40** — this is a confluence of the **Bollinger middle band at 308.48**, the **50 SMA at 304.24**, and the June price congestion (June closes 310.26 on 06-03, 311.23 on 06-04, 313.39 on 07-08). A retest here that holds would be a textbook "breakout-and-retest" long with the 50 SMA as the floor.
- Stop for Tier 2: daily close **below 304.24** (50 SMA), because a break there would also break the 20-day mean and negate the immediate uptrend.
- Position sizing: with ATR at 8.21 (2.50% of price), a 1% portfolio risk budget implies a position no larger than ~**risk_budget / (1.5 × 8.21)** — i.e. size to ATR, not to a fixed share count.

**Scenario C — Trend damage (~10%).**
Signals that would flip the bias: (a) daily close below the **50 SMA at 304.24**; (b) MACD crossing **below signal** (requires MACD to fall from 8.93 toward 6.71); (c) RSI losing **50**; (d) VWMA turning down. A close below **304** would shift the tactical thesis to neutral and put the 200 SMA at **274.94** back in play as the strategic reference.

### Risk-management specifics (from verified levels)
| Parameter | Level | Source |
|---|---|---|
| Immediate resistance | 329.60 → **334.99** | 07-21 high; 07-17 intraday high |
| Record close | **333.74** | 2026-07-17 |
| Upside magnet | **344.09** | Bollinger upper band |
| First support | **322.21 / 322.22** | 10 EMA / 07-21 low |
| Trend shelf | **304.24** | 50 SMA |
| Confluence support | **308.48** | Bollinger middle |
| Structural floor | **274.94** | 200 SMA |
| June capitulation low | **273.75** | 2026-06-25 |
| Daily 1 ATR | **$8.21 (2.50%)** | 2026-07-21 |

### What to watch in the next 5–10 sessions
1. **MACD histogram** — does 2.21 stabilise and re-expand above 3.34, or keep bleeding toward zero? This is the single cleanest tiebreaker.
2. **Volume on the next up-day** — needs to return above ~60M to validate continuation.
3. **RSI holding 60+** — a break of 60 while price is making highs would confirm the medium-term divergence (79.79 on 05-28 vs 71.65 on 07-17 vs 64.54 now) is resolving bearishly.
4. **The 322.22 – 334.99 range** — resolution direction is the tactical trade.

---

## 6. Caveats
- The dataset begins 2025-12-01, so "record high" here means the highest print **within this visible window**, not a verified all-time high. I make no claim beyond the frozen data.
- No fundamental, earnings, or news data is available from these tools. The two anomalous sessions — **2026-02-12 (−5.0%)** and **2026-06-25 (−6.1%, 107M shares)** with **261.8M** shares the following day — are flagged as event-triggered volatility. Such gaps can recur without warning and are not predictable from technicals.
- Bollinger bands and moving averages are recomputed each session; the 344.09 target will drift with volatility.

---

## 7. Summary table

| Dimension | Evidence (verified 2026-07-21) | Read | Action |
|---|---|---|---|
| **Price structure** | 327.74 close; 322.22–334.99 last 3 sessions | Consolidation under record close 333.74 | Range trade until resolution |
| **Short-term trend** | 10 EMA 322.21, still rising (+1.23/day) but decelerating | Intact, losing thrust | Hold longs; trail stop under 322 |
| **Medium-term trend** | 50 SMA 304.24, up from 291.15 since 06-25 | Bullish | Buy dips toward 308–313 |
| **Long-term trend** | 200 SMA 274.94; 50 SMA is 10.7% above it | Deeply entrenched golden cross | Strategic long bias |
| **Extension** | Price +7.7% vs 50 SMA, +19.2% vs 200 SMA | Stretched | Size down; prefer pullbacks over chases |
| **MACD** | 8.927 vs signal 6.713; bullish cross since 07-02 | Positive | Trend-follow |
| **MACD hist** | Peaked 3.337 (07-17) → 2.214 (07-21) | Decelerating | Await re-expansion before adding |
| **RSI** | 64.54 (from 71.65 on 07-17); 79.79 at 05-28 | Neutral-bullish; medium-term negative divergence | Not a sell, but a "don't add aggressively" |
| **Bollinger** | UB 344.09 / mid 308.48 / LB 272.87; width 23.1%; %B 0.77 | Wide, fanning = event regime; price inside bands | Target 344; expect 308 retest risk |
| **ATR** | 8.206 = 2.50% of price, +47% since 05-29 | Elevated | Stops ≥ 1.5×ATR; reduce size |
| **VWMA** | 317.27, rising sharply; price +3.3% above | Accumulation confirmed | Bullish confirmation |
| **Volume** | Breakout 61–63M (07-15/16/17); pullback 41–53M (07-20/21) | Healthy contraction | Supports continuation |
| **Bias** | All four trend layers aligned up; momentum cooling | **Bullish, tactically paused** | Long bias; buy 322 or 308–313; invalidation 304 |
| **Key risk** | RSI divergence + 2 consecutive histogram declines + 7.7% SMA extension | Consolidation or deeper mean-reversion | Respect the 304 break as a regime change |