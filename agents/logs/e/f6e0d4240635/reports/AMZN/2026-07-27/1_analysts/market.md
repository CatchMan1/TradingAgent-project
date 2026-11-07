# AMZN — Technical Analysis Report (as of 2026-07-27)

## 0. Data provenance & cross-check

All exact price/indicator claims below come from the **verified market snapshot for 2026-07-27** and the cached indicator series. I re-pulled every indicator independently via `get_indicators`; the values matched the snapshot exactly (e.g., RSI 36.953222 both ways, MACD −2.301281 both ways, 50-SMA 248.448401 both ways). **No discrepancies to flag.** The snapshot additionally reports an MFI field of 0.3628 — this appears to be a 0–1 normalized scale (i.e., ≈36.3), which corroborates the weak-money-flow read from RSI rather than contradicting it; I do not use it as a primary signal.

**Latest verified session (2026-07-27):** Open 235.67 / High 235.89 / Low 230.99 / **Close 231.39** / Volume 34,999,500.

| Indicator | Value (2026-07-27) | Price vs indicator |
|---|---|---|
| close_10_ema | 240.373 | Price −3.74% below |
| close_50_sma | 248.448 | Price −6.87% below |
| close_200_sma | 234.636 | Price −1.38% below |
| macd | −2.301 | Below zero |
| macds | −0.849 | MACD below signal |
| macdh | −1.452 | Negative & widening |
| rsi | 36.95 | Weak, not yet oversold |
| boll / boll_ub / boll_lb | 243.771 / 256.022 / 231.520 | Price marginally **below lower band** |
| atr | 7.056 | ≈3.05% of price |
| vwma | 244.616 | Price −5.41% below |

---

## 1. Why these 8 indicators (complementary, non-redundant)

The market context here is **a failed recovery inside a wider range that is now breaking down** — a regime where trend confirmation and mean-reversion risk both matter. My selection covers each distinct information channel once:

1. **close_200_sma** — the strategic trend arbiter. Price just lost a *rising* 200-SMA; this is the single most consequential fact in the dataset.
2. **close_50_sma** — medium-term trend/supply zone. Catches the rolling-over of the "golden cross" structure and defined the July rejection zone.
3. **close_10_ema** — short-term momentum for entry timing; unlike the SMAs it flags the speed of the July collapse.
4. **macd** — momentum regime change (zero-line crossover).
5. **macds** — needed to date the *bearish crossover* (Jul 22→23) and to size how far momentum has deteriorated.
6. **rsi** — independent, bounded oscillator to test whether the decline is stretched (divergence/oversold) or merely trending. Deliberately chosen *instead of* adding StochRSI/MFI-class oscillators, which would duplicate it.
7. **boll + boll_ub/boll_lb** — volatility-scaled levels. Captures the squeeze→breakdown dynamic and gives a statistically anchored lower-band level.
8. **atr** — the only pure risk-sizing input; converts all the above into stops and position size.
9. **vwma** — volume-confirmation. Distinguishes "decline on distribution" from "decline on apathy"; redundant with a plain MA but not with SMAs since it weights by turnover.

Deliberately excluded: `boll_ub`/`boll_lb` are used as components of the Bollinger read rather than separate convictions; no second oscillator, no second volume average.

---

## 2. Trend structure: the 200-SMA break is the headline

**Long-term (200-SMA).** The 200-SMA is **still rising** — from 231.27 on 2026-05-28 to 234.64 on 2026-07-27 (+0.06 to +0.14 per session). But price has now posted **three consecutive closes below it**:

- 2026-07-23: close 233.66 vs 200-SMA 234.53
- 2026-07-24: close 232.11 vs 200-SMA 234.59
- 2026-07-27: close 231.39 vs 200-SMA 234.64

Throughout June and early July, price was comfortably above this line (e.g., 2026-06-15 close 246.02 vs 200-SMA 232.59; 2026-07-15 close 254.96). A loss of a **rising** 200-SMA after a multi-month advance is a materially different signal than losing a flat one: it means the average itself is still climbing while price falls, so the gap can widen mechanically. The bearish read is confirmed, not marginal — but it is only 3 sessions old, and a reclaim above ≈234.6 would neutralize it.

**Medium-term (50-SMA).** The 50-SMA peaked at **257.100 on 2026-06-18** and has declined every session since, reaching **248.448** — a monotonic 26-session slide. Price is 6.87% below it. The July rebound tested it and failed: the **only** close above the 50-SMA in the rebound was 2026-07-15 (254.96 vs 253.10), and price immediately reverted (07-16 close 249.89 vs 252.66; 07-16 intraday high 258.08 with a close 8+ points lower). That is textbook failed-reclaim behavior at a declining medium-term average.

The **50/200 relationship is still bullish (248.45 > 234.64, a +13.8 point spread)** — the golden cross is intact. But the spread has compressed from its June peak and is compressing roughly 0.6–0.7 points per session. At the current slope a death cross would need price to stay depressed for weeks; **a death cross is a risk, not a current condition.** Treat it as a *strategic* warning, not a trigger.

**Short-term (10-EMA).** 240.373, and falling fast: 247.60 (07-20) → 247.09 (07-22) → 244.65 (07-23) → 242.37 (07-24) → 240.37 (07-27). Price has been below it since 07-23. The 10-EMA is 3.74% above spot, which quantifies how violent the last three sessions were.

**Sequence of lower highs (verified data points):**
278.56 (05-05 high) → 274.75 (05-29) → 266.63 (06-01) → 258.08 (07-16) → 252.89 (07-20). The July spike high (258.08) *did* exceed June's high (249.71 on 06-29), so this is not a clean stair-step — it is a **range (roughly 225.6–258.1) with a bearish short-term resolution inside it.** That distinction matters for targets: we are mid-range, not at the bottom of a completed topping pattern.

**Recent close sequence (the breakdown in numbers):**
254.96 → 249.89 → 247.23 → 249.99 → 247.55 → 244.85 → **233.66** → 232.11 → 231.39.
The **2026-07-23 candle is the event**: it gapped down from a 244.85 close to a 236.26 open (−3.5%), ran to 238.35, and closed at 233.66 on **47.47M shares** versus a ~41.8M average over the prior 20 sessions (~1.14×). From the 07-15 close of 254.96 to 231.39 is **−9.24% in eight sessions**; from the 07-22 close to 231.39 is **−5.50% in three.**

---

## 3. Momentum: MACD has flipped regimes; RSI says "weak, not washed out"

**MACD family.** The MACD line was positive and *improving* through mid-July (0.260 on 07-15, 0.824 on 07-20), then failed:
- **Zero-line cross:** MACD went negative on **2026-07-23** (−0.530 from +0.559 on 07-22).
- **Signal cross:** histogram flipped negative on **2026-07-23** (−0.297 from +0.717), i.e., MACD crossed *below* its signal in the same session as the zero-line cross.
- **Current:** MACD −2.301, signal −0.849, histogram **−1.452 and widening** (07-24: −1.014; 07-27: −1.452).

A simultaneous zero-line and signal-line breakdown, with a widening negative histogram, is the highest-confidence momentum configuration in the bearish toolkit. There is **no bullish divergence** visible — the histogram low in late June (−0.101 on 06-30, with price near 227–232) was *higher* than nothing comparable; the July histogram peak (+2.124 on 07-15) is now being fully unwound, which means the July rally's momentum impulse has been erased rather than merely paused.

**RSI.** 36.95, down from **60.14 on 2026-07-15** — a ~23-point collapse in eight sessions. Context for calibration: RSI bottomed at **32.46 on 2026-06-10** and **33.63 on 2026-06-25** during the June decline and both times the stock subsequently recovered. So **RSI 37 is weak but has not yet reached the level (≈32–34) where the two prior 2026 pullbacks found buyers.** Two implications:

- For **trend-followers**: momentum is confirming, not diverging — no reason to fade the move yet.
- For **counter-trend buyers**: you are early. The June precedent says RSI in the 32–34 zone (with price near the 225–228 support shelf) was the better asymmetry. Waiting for RSI ~32–34 or a bullish RSI divergence would be more disciplined than buying 37.

---

## 4. Volatility and mean reversion: a squeeze that broke down, and a marginal lower-band breach

**Bollinger structure.** The band width compressed dramatically: on 2026-06-12 the bands spanned 233.83–280.67 (width 46.84, **18.2%** of the 257.25 middle line). By 2026-07-27 they span 231.52–256.02 (width 24.50, **10.05%** of the 243.77 middle). That is a **classic volatility squeeze** — and it resolved **downward** on 2026-07-23, not upward. Squeeze-then-breakdown direction is the more reliable read of what the market chose.

Critically, **the 2026-07-27 close of 231.39 is fractionally below the lower band of 231.520** (the first close below the lower band in the visible window; 07-24's close of 232.11 was still above its band at 231.85). Two caveats:
1. In a confirmed downtrend, price can **ride the lower band** for multiple sessions — the lower band is a *statistical* stretched condition, not a buy signal.
2. The breach is *marginal* (0.13 points, ~0.06%), which is more consistent with "trend pressing the envelope" than with a violent capitulation spike.

Note also that the middle band (243.77, a 20-SMA) has **turned back up** in July (239.68 on 07-08 → 243.77 on 07-27) while price fell away from it — a divergence that will resolve either by a snap-back rally toward 243.8 or by the middle band rolling back down. Price falling while the 20-SMA rises is the mechanical setup for a **mean-reversion bounce attempt**, but only after the down-move stops making new lows.

**ATR.** 7.056, ≈**3.05% of price**. ATR has actually *contracted* from the June/July peaks (8.59 on 06-29; 8.41 on 07-01) — the recent decline, despite being sharp in point terms, occurred on **declining realized range**, i.e., a steady bleed rather than a volatility explosion. Practical use:
- 1 ATR below 231.39 = **224.33** (conveniently just under the June low of 225.55).
- 1.5 ATR = 10.6 points; 2 ATR = 14.1 points.
- Stop placement should be **≥1.5 ATR** to avoid noise stop-outs; a 1-ATR stop at 224.3 is too tight given the July 23 gap proves this name can gap 3.5% overnight.

**Event-gap risk is not captured by ATR.** Verified precedent in this dataset: 2026-02-05 closed 222.69, then 2026-02-06 opened at **202.70** (low 200.31) on **179.2M shares** — an ~9% overnight gap. The 2026-07-23 gap (−3.5% at the open) is a smaller cousin. Any stop logic must assume the gap can jump the stop; size positions on gap risk, not just ATR.

---

## 5. Volume: distribution on the break, apathy on the follow-through

**VWMA** (244.616) is **above** spot by 5.41% and has **rolled over** from its 07-22 peak of 247.032 (07-20: 245.58; 07-23: 246.23; 07-24: 245.52; 07-27: 244.62). Reading: the volume-weighted average price paid by recent participants is ~244.6, and the market is now 13+ points below it — **recent buyers as a cohort are underwater.** That is a supply overhang: rallies into 243–245 will meet motivated sellers trying to get out near flat.

VWMA vs the 50-SMA (248.45): VWMA sits *below* the 50-SMA, meaning recent turnover has concentrated at lower prices than the simple average — consistent with **distribution into the July rally** rather than accumulation.

**Volume detail on the decline:**
- 2026-07-23: 47.47M (breakdown day; ~1.14× the ~41.8M 20-session average) — real distribution.
- 2026-07-24: 35.02M and 2026-07-27: 35.00M (~0.84× average) — **declining volume on further decline.**

Interpretation is genuinely two-sided and I will not overclaim: light-volume drift-down *can* mean seller exhaustion (bullish for a bounce), but it equally means **no capitulation flush and no demand**, which usually precedes continuation. The decisive tell is what happens at the 231.5/230.9 area: a high-volume reversal candle there = exhaustion; a high-volume close below 225.55 = continuation confirmed.

One data hygiene note: **2026-06-26 volume of 248.4M** is a massive outlier (index-rebalance-type flow) and should be excluded from any average-volume calculation or it will distort every read.

---

## 6. Key levels (all derived from verified data)

| Level | Value | Source / significance |
|---|---|---|
| **Resistance 4** | 256.0–258.1 | Boll upper band 256.02 (07-27); 07-16 high 258.08 |
| **Resistance 3** | 248.4 | 50-SMA (declining); July's failed-reclaim zone |
| **Resistance 2** | 243.8–244.9 | Boll middle 243.77; VWMA 244.62; **07-22 close 244.85 = top of the unfilled 07-23 gap** |
| **Resistance 1** | 234.6–240.4 | 200-SMA 234.64 (must reclaim); 10-EMA 240.37 |
| **Spot** | **231.39** | Close 2026-07-27 |
| **Support 1** | 230.99–232.24 | 07-27 low 230.99; Boll lower band 231.52; 06-22 low 232.24 |
| **Support 2** | 225.55–227.01 | 06-25 low 225.55 / close 227.01 — **the line in the sand** |
| **Support 3** | 219.6–223.8 | 04-08 low 219.62 / 04-08 open 223.79 — the unfilled April gap shelf |
| **Support 4** | 196.00–200.31 | 02-17 low 196.00; 02-06 low 200.31 |

**Context for scale:** 2026 YTD close-to-close is +2.16% (226.50 on 01-02 → 231.39). From the 2026 high close of **274.99 (05-06)**, AMZN is **−15.9%**. So this is a stock that has given back most of its yearly gain and is retesting the lower half of a six-month range — not a broken secular uptrend, but a damaged intermediate one.

---

## 7. Actionable scenarios

### Scenario A — Trend-continuation short / underweight (highest-probability base case)
**Logic:** 200-SMA lost on a rising average; MACD zero + signal cross with widening histogram; price below 10-EMA, 50-SMA, VWMA, and the lower Bollinger band; failed 50-SMA reclaim; recent buyers underwater at 244.6.
**Trigger/entry zone:** rallies into **240–245** (10-EMA → VWMA/Boll middle, and the unfilled gap fill at 244.85) rather than chasing at 231 after a −5.5% three-day slide.
**Targets:** 227.0/225.55 first; if that fails on volume, 219.6–223.8.
**Invalidation:** a **daily close back above 234.64 (200-SMA)** weakens the thesis; two consecutive closes above **248.45 (50-SMA)** kills it.
**Stop:** ≥1.5 ATR ≈ 10.6 points above entry; note gap risk (Feb 6 precedent: ~9% overnight).

### Scenario B — Mean-reversion long (tactical, counter-trend)
**Logic:** first close below the lower Bollinger band; RSI 36.95 falling toward the 32–34 zone where the June 10 and June 25 lows formed; 20-period middle band still rising; volume fading on the decline.
**Conditions to require before entry (do not front-run):** a close back **inside** the bands (above 231.52) and preferably above 07-27's high of 235.89; or RSI ≤34 with a higher low in price above 225.55.
**Targets:** 240.4 (10-EMA) → 243.8–244.6 (Boll middle/VWMA) → gap fill 244.85.
**Stop:** below **225.55** (below the June low) or 1.5 ATR, whichever is tighter given entry.
**Caution:** buying now is buying at RSI 37 *with* MACD accelerating negative and below a rising 200-SMA. The asymmetry improves materially at 227 or on an RSI divergence.

### Scenario C — Regime repair (bullish, requires patience)
**Sequence needed:** reclaim 234.64 (200-SMA) → clear 240.37 (10-EMA) → close above 248.45 (50-SMA) → break 258.08 (07-16 high). Only after that does the range resolve upward, with 256.02 (upper band) and 265.9–274.99 (April–May highs) as references.
**Why to wait:** the July attempt already produced one close above the 50-SMA (07-15) that failed within a session.

### Risk sizing note
At ATR 7.06 (3.05%), a 1%-of-equity risk per trade implies a position size of roughly **0.14% of equity per $1 of stop distance** — i.e., with a 1.5 ATR stop (10.6 points), position size ≈ (1% × equity) / 10.6 per share. Halve that if holding through any scheduled catalyst, because the Feb 6 and Jul 23 gaps show stops are not respected overnight.

---

## 8. Nuanced conclusion

AMZN is at a genuine inflection, not a comfortable trend. The **weight of evidence is bearish on the intermediate horizon** (below rising 200-SMA, 50-SMA declining 26 straight sessions, MACD double-cross with widening histogram, price below VWMA and the lower Bollinger band, failed 50-SMA reclaim on 07-15, lower-high sequence since 05-05), but there are three honest counterweights that argue against aggressive shorting right here: **(1)** RSI 36.95 is not yet at the 32–34 zone that marked the June 10 and June 25 lows; **(2)** price is fractionally *below* the lower Bollinger band — statistically stretched, where bounces begin; **(3)** volume has faded to 0.84× average on the last two down days, i.e., no capitulation, which leaves Scenario B live. The technically cleanest approach is **not to chase at 231.4**: be a seller into 240–245 supply, or a buyer only with confirmation (close back inside the bands / RSI ≤34 with a higher low) and a hard stop under 225.55. The single level that reframes everything is **234.64**.

---

## 9. Summary table

| Dimension | Reading (2026-07-27) | Signal | Key evidence |
|---|---|---|---|
| Price | 231.39 close; low 230.99; vol 35.00M | — | Verified snapshot |
| Long-term trend | Below **rising** 200-SMA 234.64 | **Bearish** | 3 straight closes below (233.66, 232.11, 231.39 vs 234.53/234.59/234.64) |
| Medium-term trend | 50-SMA 248.45, declining 26 sessions from 257.10 (06-18) | **Bearish** | Price −6.87%; only 07-15 closed above it, then failed |
| Golden/death cross | 50-SMA > 200-SMA by 13.8 pts | Still bullish, eroding | Spread compressing ~0.6–0.7 pts/session; death cross = risk, not event |
| Short-term momentum | 10-EMA 240.37, falling 7 pts in 5 sessions | **Bearish** | Price −3.74% below |
| MACD | −2.301 / signal −0.849 / hist −1.452 | **Bearish, strengthening** | Zero & signal crosses both on 07-23; hist widening |
| RSI | 36.95 (from 60.14 on 07-15) | Weak; **not oversold** | June lows were 32.46 (06-10) and 33.63 (06-25) |
| Bollinger | 243.77 mid / 256.02 upper / 231.52 lower | Stretched; squeeze broke down | Close 231.39 just below lower band; width 18.2%→10.05% |
| ATR | 7.056 (3.05%) | Elevated but contracting | Peaked 8.59 (06-29); gap risk exceeds ATR (Feb 6: 222.69→202.70 open) |
| VWMA | 244.616, rolling over from 247.03 | **Bearish supply overhang** | Price −5.41%; cohort of buyers underwater |
| Volume character | 47.47M on 07-23 break, 35.0M after | Distribution, then apathy | ~1.14× then ~0.84× 20-session avg (~41.8M); 06-26 248M excluded as outlier |
| Structural range | 225.55 (06-25 low) – 258.08 (07-16 high) | Mid/low range | Lower highs since 278.56 (05-05); higher low not yet broken |
| YTD / drawdown | +2.16% YTD; −15.9% from 274.99 (05-06) | Damaged intermediate uptrend | 226.50 (01-02) → 231.39 |
| Primary pivots | Res: 234.64 / 240.37 / 243.8–244.9 / 248.45 / 256–258 · Sup: 231.0–232.2 / 225.55–227.0 / 219.6–223.8 | — | Each level traced to a dated print |
| Bias | **Bearish intermediate, tactically stretched** | Sell rallies; don't chase | Base case A; Scenario B needs confirmation |