# AMZN — Multi-Timeframe Technical Report (as of close 2026-08-21)

**Last verified session:** 2026-08-21 — O 260.74 / H 261.09 / L 257.04 / **C 258.63** / Vol 35.72M
`get_stock_data` and `get_verified_market_snapshot` agree exactly on this row and on all indicator values cited below — no discrepancy to flag.

---

## 1. Market Context: What AMZN Is Actually Doing

AMZN is in a **post-event digestion phase inside an intact intermediate uptrend**. The tape has three distinct regimes that matter for indicator selection:

1. **June–July 2026: declining/choppy base.** Price oscillated 226–256, bottoming at a close of **226.65 on 2026-07-29** (intraday low 226.16), while the 50-SMA drifted *down* from 256.64 (06-17) to 246.38 (07-30).
2. **2026-07-30 → 2026-08-03: violent re-rating.** Volume exploded to **101.8M on 07-30** (close 235.50) and then **129.1M on 07-31**, when price gapped and closed at **271.58**. Follow-through on **08-03** to a close of **284.02** and the swing high of **287.20** (volume 90.8M). That is **+20.6% in two sessions** on close-to-close data (235.50 → 284.02).
3. **2026-08-04 → 2026-08-21: orderly retracement.** Fourteen sessions of lower highs (287.20 → 280.14 on 08-10 → 266.40 on 08-19) and lower lows, taking price to **258.63**, i.e. **−8.9% off the 08-03 close** (284.02) and **−9.9% off the intraday high** (287.20).

The critical nuance: **the 07-31 gap-day low of 262.01 has been lost.** Closes on 08-17 (261.31), 08-18 (259.45), 08-20 (260.11) and 08-21 (258.63) are all *below* it. Every buyer who chased the gap is now underwater on a volume-weighted basis. That is the single most important bearish tell in this chart, and it is why VWMA matters here.

---

## 2. Selected Indicators (8) and Why

| # | Indicator | Current (2026-08-21) | Why it earns a slot |
|---|---|---|---|
| 1 | **close_10_ema** | 262.75 | Fastest read on the post-gap momentum roll-over; price below it = short-term sellers in control |
| 2 | **close_50_sma** | 249.73 | Medium-term trend + dynamic support; just turned up after 3 months of decline |
| 3 | **close_200_sma** | 238.33 | Long-term regime filter; steeply rising, confirms bull structure |
| 4 | **macd** | 3.461 | Still positive → this is a momentum *deceleration*, not yet a trend reversal |
| 5 | **macds** | 4.999 | Provides the crossover event date (08-17) and confirms histogram expansion |
| 6 | **rsi** | 49.74 | Confirms the overbought reset from 72.23 (08-03) without capitulation |
| 7 | **atr** | 7.482 | Essential for stop sizing in a post-gap regime where volatility is 25% off its peak |
| 8 | **vwma** | 269.19 | The only indicator that tells us the *volume-weighted* cost basis of the gap buyers |

**Deliberately excluded / de-emphasized:** Bollinger bands. The verified snapshot shows **boll 261.38, boll_ub 295.34, boll_lb 227.42** — a band width of ~68 points, or **26% of price**. The 07-31 gap mechanically blew out the standard deviation, so the upper/lower bands carry almost no signal right now (the 08-03 high of 287.20 never even tagged the 295.34 upper band). The **Bollinger middle (20-SMA) at 261.38** is still useful as a plain short-term pivot and is referenced below. I also excluded a second momentum oscillator (e.g. stochastics) as redundant with RSI, and excluded `mfi` because the snapshot returns it in a non-standard normalized form (0.207) that I cannot validate.

---

## 3. Detailed Indicator Readings

### 3.1 Short-term trend — 10 EMA (262.75): bearish
- The 10-EMA peaked at **267.18 on 08-12** and has fallen for seven consecutive sessions to 262.75.
- Close of **258.63 is 1.57% below it** — the sixth consecutive close beneath the 10-EMA. Price has not closed above it since 08-10 (278.09).
- The 10-EMA is *still* 5.1% above the 50-SMA, so the short-term average has a long way to fall before structure breaks. Signals a **pullback, not a breakdown**.

### 3.2 Medium-term trend — 50 SMA (249.73): bullish, and freshly turning up
- Sequence: 256.64 (06-17) → **trough 246.38 (07-30)** → **249.73 (08-21)**, rising for **16 consecutive sessions**.
- Price is **+3.57% above** the 50-SMA. The 50-SMA is rising ~0.21 points/day, so a flat price for two more weeks would let it "catch up" to ~252-253 — a natural magnet.
- **Important caveat:** the 50/200 spread has been *narrowing* since mid-June (50−200 = 23.93 on 06-17 → 11.63 on 07-30 → **11.40** on 08-21). The golden-cross structure is intact and the spread is wide, but the widening phase has ended. Long-term trend = up; medium-term trend = up but decelerating.

### 3.3 Long-term trend — 200 SMA (238.33): hard bullish
- Rising monotonically from 230.77 (05-26) to 238.33, gaining ~0.22/day.
- Price is **+8.52% above** the 200-SMA. This is the structural cushion: a full retest of the 200-SMA would require a −7.9% move and would also mean filling the entire 07-31 gap.
- 50-SMA (249.73) > 200-SMA (238.33) with both rising = textbook golden-cross bull configuration. **No death-cross risk in any near-term scenario.**

### 3.4 Momentum — MACD (3.461) vs Signal (4.999), Histogram −1.538: bearish crossover confirmed
- MACD line topped at **8.432 on 08-11** and has declined five straight sessions to 3.461 (−59% from the peak).
- Signal line peaked at **6.217 on 08-14**; the **bearish crossover occurred on 2026-08-17** (histogram flipped from +0.392 on 08-14 to −0.310 on 08-17).
- Histogram has expanded negatively every session since: −0.310 (08-17) → −0.908 → −0.882 → −1.237 → **−1.538 (08-21)**. **Selling momentum is still accelerating, not decelerating.**
- Crucially, **MACD remains above zero (3.461)**. This is a *corrective* signal inside a bull trend. A zero-line cross would be the genuine regime-change warning; at the recent ~0.5-0.6/session decay rate that is roughly 5-7 sessions away *if* the decay continues linearly (it usually does not — deceleration typically flattens the line first).

### 3.5 Momentum breadth — RSI (49.74): neutral, no divergence, no extreme
- RSI path: **33.31 (07-29) → 72.23 (08-03, overbought at the swing high) → 49.74 (08-21)**. A near-perfect momentum round-trip.
- The decline has been orderly (65.87 on 08-10, 60.97, 57.06, 55.41, 53.49, 52.43, 50.93, then the 08-19 bounce to 55.64, then 50.92, 49.74). **No positive divergence has formed** — RSI has simply tracked price lower, which means no evidence yet of downside exhaustion.
- RSI at ~50 with price below the 10-EMA and a negative MACD histogram argues for **more chop/grind rather than an immediate V-bottom**. Historically RSI in the mid-40s would coincide with the 250-251 area.

### 3.6 Volatility — ATR (7.482): contracting, which is constructive
- ATR spiked to **9.98 on 08-05** (post-gap) from **6.89 on 07-29** (pre-gap), and has now bled down to **7.482** — a **25% contraction** from the peak, but still **+8.6% above** the pre-gap level.
- Interpretation: the market is *absorbing* the re-rating, not panicking. The current 5-day range (257.04–266.40 = 9.36 points) is only ~1.25× ATR — a tight, controlled flag.
- Consequences: (a) stops must be wider than pre-July norms; (b) with ATR falling, the same dollar risk buys more shares than it did two weeks ago; (c) a volatility expansion out of this contraction (either direction) is the next tradeable event.

### 3.7 Volume — VWMA (269.19): strongly bearish for the gap cohort
- VWMA climbed every session from 245.72 (07-31) to a peak of **272.05 on 08-20**, then ticked down to 269.19 on 08-21. That is the volume-weighted average price of the whole post-gap period.
- Price at 258.63 is **4.07% below VWMA**. Anyone who bought the 129M-share and 91M-share volume days (07-31 and 08-03) is at a loss — that is a supply overhang on every rally into 265-274.
- **Offsetting positive:** the pullback itself has been on *shrinking* volume. Volume by day: 129.1M (07-31) → 90.8M (08-03) → 69.7M → 45.1M → **30.7M (08-06, period low)** → 33.9M / 35.7M / 31.9M / 29.9M / 32.2M / 27.3M / 43.9M / 33.2M / 35.8M / 28.4M / **35.7M (08-21)**. Declining volume on a declining price is the signature of **orderly distribution/consolidation rather than institutional dumping** — but it equally means **no volume-backed demand has appeared yet**.

---

## 4. Price Structure & Levels (all derived from tool data)

**Rally leg used for retracement:** 07-29 close 226.65 → 08-03 high 287.20 (range 60.55)
- 38.2% = **264.07** — already lost
- 50.0% = **256.93** — current price (258.63) is holding just above it
- 61.8% = **249.78** — effectively coincides with the 50-SMA (249.73)

**Resistance stack (descending relevance):**
1. **261.09** — 08-21 session high
2. **261.38** — Bollinger middle / 20-day basis
3. **262.75** — 10-EMA (the first real reclaim test)
4. **266.40 / 265.84** — 08-19 high and close (the failed bounce)
5. **269.19** — VWMA
6. **271.58–273.23** — 07-31 gap-day close/high, plus the 272.27–274.48 congestion of 08-07/08-10/08-11
7. **280.14 / 287.20** — August highs
8. **295.34** — Bollinger upper (not realistically in play)

**Support stack:**
1. **257.04** — 08-21 low (the immediate line in the sand)
2. **256.93** — 50% retracement (confluence with #1)
3. **250.16–250.87** — early-July congestion and 08-04 area closes
4. **249.73–249.78** — 50-SMA + 61.8% retracement (the key structural zone)
5. **242.70–245.72** — 07-31 intraday low (262.01?) no — 07-31 low is 262.01; the lower structural shelf is the **240.82 VWMA turn of 07-30** and the **239.82 07-30 high** (the unfilled gap's upper edge)
6. **238.33** — 200-SMA; **227.42** — Bollinger lower

The gap between **239.82 (07-30 high) and 262.01 (07-31 low)** remains entirely unfilled — a 22-point vacuum. Price is currently sitting in the lower third of the *post*-gap range, inside 3.1% of the gap's upper edge, but the vacuum below is real and thin.

---

## 5. Actionable Interpretation

**Bias: NEUTRAL-to-CONSTRUCTIVE intermediate term; SHORT-TERM DOWN.** The burden of proof has shifted. Three of the eight indicators (10-EMA, MACD cross, VWMA) are outright bearish; two (50-SMA, 200-SMA) are outright bullish; three (RSI, ATR, Bollinger middle) are neutral/ambiguous. That is a market in **digestion**, and the correct posture is patient rather than directional.

**Scenario A — Bullish resolution (preferred if the 50-SMA holds):**
- Trigger: a daily close **above 266.40** (clearing the 08-19 high) with volume **>50M** (i.e., above the ~30-36M pullback norm). That would reclaim the 10-EMA *and* the VWMA, and would flip MACD back up.
- Targets: 271.58–274.48 first, then 280.14, then 287.20.
- Invalidation/re-entry logic: a touch of **249.7–251.0** (50-SMA) that reverses intraday with a higher low is an *add* zone, not a stop-out, because it aligns 61.8% retracement with a rising 50-SMA and still leaves price 4.8% above the 200-SMA.

**Scenario B — Bearish continuation:**
- Trigger: daily close **below 256.93** (simultaneously breaks the 08-21 low at 257.04 and the 50% retracement) on expanding volume. That would set up a test of 250-251 (50-SMA), and MACD would likely be closing in on its zero line.
- If 249.73 breaks decisively, the next magnet is 240-242 and the unfilled gap's upper edge at 239.82 — a further **7.3%** below current price from 258.63. This is the fat-tail risk that the 200-SMA alone will not protect against.

**Risk management using ATR (7.482):**
- For a long entered near 259 with a stop below 256.93, that is a ~2.1-point (0.8× ATR) stop — **too tight** for this volatility regime. A 1.5× ATR stop from 259 is ~247.8, which sits just under the 50-SMA and is the more survivable placement.
- With ATR down 25% from the 08-05 peak, position size can be **~30% larger** than at peak post-gap volatility for the same dollar risk, but the still-elevated level (+8.6% vs pre-gap) argues for keeping gross exposure below pre-July norms.
- Expect a daily range of roughly ±7.5 points (±2.9%) as the base case; a close outside 257.04–266.40 with volume expansion is the next directional cue.

**What would change the read:**
- Bullish flip: MACD histogram turning back positive (a second crossover), or price closing above 269.19 VWMA.
- Bearish flip: MACD crossing below zero, or RSI closing below ~45 concurrently with a close under 256.93.
- Regime risk: any move back into the 239.82–262.01 gap would be a full retracement of the re-rating and would signal the 07-31 event was fully priced out.

---

## 6. Summary Table

| Dimension | Reading (2026-08-21) | Evidence from tool output | Implication |
|---|---|---|---|
| **Last close** | 258.63 | O 260.74 / H 261.09 / L 257.04; Vol 35.72M | Sitting on 50% retracement of the post-gap leg |
| **10-EMA** | **262.75** — price 1.57% below | 7 straight declines from 267.18 (08-12); 6 closes below | Short-term trend = down |
| **50-SMA** | **249.73** — price 3.57% above | Rose 16 straight sessions from trough 246.38 (07-30) | Medium-term trend = up; support ~250 |
| **200-SMA** | **238.33** — price 8.52% above | Monotonic rise from 230.77 (05-26) | Long-term bull intact; deep cushion |
| **50/200 spread** | 11.40 (was 23.93 on 06-17) | Golden cross intact but no longer widening | Bull trend decelerating |
| **MACD / Signal** | **3.461 / 4.999** | Bearish cross on 2026-08-17; MACD −59% from 8.432 peak (08-11) | Momentum negative, but still >0 |
| **MACD histogram** | **−1.538** | −0.31 → −0.91 → −0.88 → −1.24 → −1.54 since 08-17 | Downside momentum still expanding |
| **RSI** | **49.74** | 72.23 (08-03) → 49.74; no divergence | Neutral; overbought reset complete |
| **ATR** | **7.482** | Peak 9.98 (08-05), pre-gap 6.89 (07-29) | Volatility contracting — orderly, not panicked |
| **VWMA** | **269.19** — price 4.07% below | Peaked 272.05 (08-20) | Gap buyers underwater = supply at 265-274 |
| **Bollinger mid / ub / lb** | 261.38 / 295.34 / 227.42 | Band width ≈ 26% of price | Bands distorted by gap; only mid (261.38) usable |
| **Volume pattern** | 129.1M & 90.8M on the gap; 27-44M since | 08-06 low 30.7M; 08-21 35.7M | Low-volume pullback = no capitulation, no demand |
| **Broken level** | 07-31 gap-day low **262.01** lost | 4 of last 5 closes beneath it | Key warning: post-gap longs are at a loss |
| **Key trigger — bull** | Close > **266.40** on >50M volume | 08-19 high 266.40 | Opens 271.6 / 280.1 / 287.2 |
| **Key trigger — bear** | Close < **256.93** | = 08-21 low 257.04 + 50% retrace | Opens 249.7 (50-SMA), then 239.8 |
| **ATR stop guidance** | 1.5× ATR ≈ 11.2 points | ATR 7.482 | Long from ~259 → stop ~247.8 (below 50-SMA) |
| **Overall stance** | Neutral / short-term down, intermediate up | 3 bearish, 2 bullish, 3 neutral indicators | Wait for resolution of 257.04–266.40; do not chase |