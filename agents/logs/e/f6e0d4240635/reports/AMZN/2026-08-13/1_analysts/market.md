# AMZN — Technical Analysis Report (as of close 2026-08-13)

## 1. Verified market state (source of truth)

The verified snapshot and the OHLCV CSV agree exactly on the latest session, so there is no data conflict to flag.

| Field | 2026-08-13 value |
|---|---|
| Open / High / Low / Close | 267.24 / 269.58 / 264.71 / **265.13** |
| Volume | 32,170,200 |
| Split / Dividend | 1.0 / 0.0 (price series = total-return series) |
| 10 EMA | 266.81 |
| 50 SMA | 247.914 |
| 200 SMA | 237.524 |
| RSI(14) | 55.41 |
| MACD / Signal / Histogram | 7.372 / 6.119 / **1.2525** |
| Bollinger mid / upper / lower | 255.749 / 294.762 / 216.735 |
| ATR(14) | 8.543 (3.22% of close) |
| VWMA | 261.986 |

**Indicators selected (8, chosen for non-redundancy):** `close_10_ema`, `close_50_sma`, `close_200_sma`, `macd`, `macdh`, `rsi`, `atr`, `vwma`. Bollinger bands (`boll`, `boll_ub`, `boll_lb`) were also retrieved and are used as a supplementary volatility-confirmation check rather than as a primary signal. (The snapshot also reports an `mfi` field of 0.5236; the scale is ambiguous — 0.52 as a 0–1 ratio implies neutral flow, which is consistent with my RSI read, so I weight it as neutral and do not build conclusions on it.)

---

## 2. The dominant fact: a violent post-catalyst regime shift on 2026-07-31

Every indicator on the board is still distorted by one event, and any analysis that ignores it will be wrong.

- **2026-07-30 close:** 235.50 (volume 101.8M — already elevated vs. ~35–45M typical).
- **2026-07-31:** opened at 265.00, closed at **271.58**, high 273.23, low 262.01, volume **129.05M**. That is a close-to-close gain of **+15.32%** and an opening gap of **+12.51%** from the prior close.
- **2026-08-03:** closed **284.02** (intraday high **287.20**), volume 90.83M — a new **closing high and intraday high for the entire 2025-12-01 → 2026-08-13 window** (prior bests were 274.99 close on 2026-05-06 and 278.56 intraday on 2026-05-05).
- Impulse measured from the 2026-07-30 close (235.50) to the 2026-08-03 close (284.02) = **+48.52 points, +20.6% in two sessions.**

The critical structural read: **the gap has not been filled at all.** The 7/31 low of 262.01 remains the floor, and the 8/13 low of 264.71 sits above it. This is an unfilled, high-volume breakaway gap — historically a strong *tendency* (not a guarantee) to act as support, and a hard invalidation zone if breached.

---

## 3. Trend structure: bullish stack intact, but the first crack has appeared

**Stacking is textbook bullish** as of 8/13: 10 EMA (266.81) > 50 SMA (247.91) > 200 SMA (237.52), with price (265.13) above both the 50 and 200 SMAs.

- **Price vs. 50 SMA:** +6.95% above (265.13 vs 247.914).
- **Price vs. 200 SMA:** +11.62% above (265.13 vs 237.524).
- **Price vs. 10 EMA:** **−0.63% (below).** 8/13 is the **first close below the 10 EMA since 2026-07-30** — i.e., the first break of short-term trend control since the gap. That is the single most important near-term signal on the board.

**Slope detail that matters:**
- The 50 SMA bottomed at 246.384 on 2026-07-30 and has risen to 247.914 (+1.53, +0.62%) over 10 sessions. It was in a *downtrend* all of June–July (255.50 on 6/15 → 246.38 on 7/30), so this is a **fresh, but shallow, inflection up** — the 50 SMA has not yet "caught up" to price, leaving a wide 6.95% air pocket.
- The 200 SMA is rising faster than the 50 SMA: 234.755 (7/30) → 237.524 (8/13), **+2.77 points in 10 sessions**, because the low Feb–Mar prices are rolling off the window. Consequence: the 50>200 spread is **narrowing slightly** (11.63 points on 7/30 → 10.39 on 8/13), and the price-vs-200-SMA cushion will compress mechanically over coming weeks even if price goes sideways. Note the 50 SMA has been above the 200 SMA throughout the visible period — **this is a long-standing bullish alignment, not a fresh golden cross**; do not trade it as a new signal.

**Short-term structure has turned down:** after the 8/3 peak the sequence of intraday lows is 273.60 (8/10) → 271.36 (8/11) → 267.10 (8/12) → 264.71 (8/13) — four consecutive lower lows and lower highs. From the 8/3 close of 284.02 to the 8/13 close of 265.13, AMZN is **−6.65%**. That is a controlled pullback inside a still-intact uptrend, not yet a trend reversal.

---

## 4. Momentum: decaying, but still net positive

**MACD (12/26/9):** The line crossed above signal on **2026-08-04** (line 4.809 vs signal 0.225) after being deeply negative (line −3.751 on 7/29). It peaked at **8.432 on 8/11** and has eased to 7.372. The signal line (6.119) is still rising. So the *crossover regime* remains bullish.

**MACD histogram is the warning light:** it topped at **4.619 on 8/5** and has fallen for **six consecutive sessions**: 4.619 → 4.361 → 4.090 → 3.904 → 3.171 → 2.179 → **1.253**. That is a **−73% collapse in momentum thrust in six sessions**. Read carefully: positive-but-shrinking histogram = uptrend losing power, not uptrend reversing. A histogram cross below zero (currently 1.25 above it) would be the mechanical confirmation that the post-earnings impulse has exhausted.

**RSI(14):** Peaked at **72.23 on 2026-08-03** (overbought), and has cooled to **55.41** — a 16.8-point round trip. This is *textbook* post-gap digestion and is genuinely constructive: RSI has reset to neutral **without price giving back more than 6.65%**, which means the pullback is being absorbed by time rather than by price. RSI is now mid-range, giving room to run in either direction with no edge from overbought/oversold. Note the pre-gap oversold print of **33.31 on 2026-07-29** — that was the launching pad.

**Divergence check:** none confirmed. A bearish divergence requires a *lower price high* paired with a *higher RSI high*; price has made a lower high (284.02 → 278.09) but RSI has also made a lower high (72.23 → 65.87 on 8/10). That is **trend-consistent deterioration, not divergence.**

---

## 5. Volatility: massively expanded, now beginning to contract

- **ATR(14):** 6.892 on 2026-07-29 → **9.983 peak on 2026-08-05** → **8.543 on 8/13**. That is a **+45% expansion** off the pre-gap base and then a **−14% contraction** off the peak. This is the classic post-catalyst volatility hump rolling over.
- **ATR as % of price: 3.22%.** Position sizing must be cut relative to the pre-gap norm (~2.9% on 7/29, ~3.1% on 7/14). A "normal" 1-ATR daily swing here is ~$8.50, so a stop inside ~$5 will be noise-stopped.
- **Bollinger bandwidth is extreme:** (294.762 − 216.735) / 255.749 = **30.5%**. The bands are exploding outward (upper 264.20 on 7/31 → 294.76 on 8/13) purely because the 20-day standard deviation now contains the gap. **Do not read the +10.05% distance below the upper band as "oversold"** — the band itself is an artifact of the shock. The practically useful Bollinger fact is that the **middle band (20 SMA) is at 255.75 and rising ~$1.6/session**, which is the natural mean-reversion target if this pullback deepens.
- The 8/13 session itself was a **narrow-range day**: range of 4.87 = 0.57× ATR (1.84% of close), closing in the lower third. Combined with decelerating down-closes (−2.09% on 8/11, −1.83% on 8/12, **−0.80% on 8/13**), this is a **volatility contraction / seller exhaustion footprint** at the 38.2% retracement — a potential pause point, not yet a confirmed turn.

---

## 6. Volume and participation: the pullback is happening on *drying* volume (constructive)

- 5-session average volume (8/7–8/13) = **32.7M**. 20-session average (7/17–8/13) = **48.8M**. Ratio = **0.67**.
- Post-gap volume has bled off steadily: 129.05M (7/31) → 90.83M → 69.75M → 45.12M → 30.67M → 33.86M → 35.73M → 31.90M → 29.94M → 32.17M.
- **Interpretation:** the −6.65% pullback from 284.02 is occurring on roughly one-third of the volume that drove the breakout. That is the profile of **profit-taking/digestion, not institutional distribution**. If this were distribution, the down days (8/12, 8/13 at 29.9M and 32.2M) would be expanding above the 20-day average.
- **VWMA at 261.986 and rising** (250.17 on 8/3 → 261.99 on 8/13) because the gap's heavy volume is being weighted in. Price at 265.13 is only **+1.20% above VWMA** — much closer than to the 50 SMA (+6.95%). **VWMA ≈ 262.0 is the most immediate volume-validated support**, and it lines up almost exactly with the unfilled gap floor at 262.01. That confluence is the highest-quality support on the chart.
- Caveat: the 6/26 volume of **248.4M** is a 5x outlier versus everything around it (Russell/index reconstitution-type flow, date-specific). It distorts any multi-week volume average; I have deliberately excluded it from the 5/20-session comparisons above.

---

## 7. Confluence map — where the decisions actually are

**Retracement grid of the 7/30→8/3 impulse (235.50 → 284.02, +48.52 pts), computed arithmetically:**

| Retracement | Level | Notes |
|---|---|---|
| 23.6% | 272.57 | Already lost on 8/11 close (272.27) |
| **38.2%** | **265.48** | **Current close 265.13 — price is sitting on it; 8/13 low 264.71** |
| 50.0% | 259.76 | Overlaps VWMA 261.99 / gap floor 262.01 zone |
| 61.8% | 254.03 | Overlaps Bollinger middle / 20 SMA 255.75 |

**Resistance:**
1. **266.81** — 10 EMA (now overhead; first thing bulls must reclaim)
2. **269.58 / 272.27** — 8/13 high and 8/11 close (the most recent lower high)
3. **273.60–278.09** — cluster of 8/10–8/11 highs and 8/10 close
4. **284.02 close / 287.20 intraday high** — the post-gap peak and window high; the breakout retest target

**Support:**
1. **264.71** — 8/13 low
2. **261.99 / 262.01** — VWMA + unfilled gap floor (**highest-confluence zone**)
3. **255.75** — 20 SMA / Bollinger middle, rising ~$1.6/day
4. **247.91** — 50 SMA (the line in the sand for the medium-term trend)
5. **237.52** — 200 SMA (long-term regime)

---

## 8. Actionable plan

**Base case (primary): bullish continuation after digestion.** The 8/13 narrow-range day at the 38.2% retracement, on volume 33% below the 20-day average, with RSI reset to 55 and MACD still above signal, argues that this is digestion. Three tactical routes:

**(a) Pullback accumulation (preferred risk/reward).** Scale in **262–265**. Stop **below 254** (beneath the 50% retracement, the 61.8% level at 254.03, and roughly 1.5× ATR from current price at 252.3 — a true confluence invalidation). First target **272.3**, second **284.0**. At entry 264 vs stop 254 that is ~2.0:1 to the 284 target. *Risk:* if 255.75 (20 SMA) breaks decisively, the thesis degrades to "failed breakout" and the 50 SMA at 247.9 becomes the next magnet.

**(b) Breakout confirmation (cleaner signal, worse price).** Wait for a **close above 266.81 (10 EMA)** and then a **close above 272.27 (8/11 lower high)** — that re-establishes the higher-high sequence and clears the 6-session momentum decay. Add on the reclaim, stop under 262 (gap floor/VWMA). This avoids catching a falling knife but forfeits ~2.7% of the move.

**(c) Stand aside** if you require MACD histogram confirmation: the histogram has bled from 4.62 to 1.25 in six sessions. A fresh histogram *expansion* upward (or a re-cross of the MACD line above the 8/11 high of 8.43) is the cleanest "digestion complete" signal.

**Invalidation logic, in order of severity:**
1. Close below **266.81 (10 EMA)** → already true; short-term momentum is negative. Reduces conviction, does not break the trend.
2. Close below **261.99 (VWMA) / 262.01 (gap floor)** → the gap starts to fill; the breakout is impaired. Cut position size at minimum.
3. Close below **255.75 (20 SMA)** → mean reversion has become trend damage.
4. Close below **247.91 (50 SMA)** → medium-term uptrend broken; a full gap fill toward 235.50 becomes the operative risk. This is the **−6.4%** scenario from here and would erase the entire +15.3% post-earnings move.

**Stop and size discipline:** with ATR at 8.54 (3.22% of price), a 1×ATR stop is 258.6 and 1.5×ATR is 252.3. Size positions so that a 1.5–2.0× ATR adverse excursion is survivable; do not use pre-gap (sub-$7 ATR) sizing.

---

## 9. Risks and honest limitations

- **Single-catalyst dependence.** The trend from 7/31 onward rests on one event. Every bullish reading above is downstream of that gap. If it was an overreaction, the 235.50–246.00 region (the entire gap air pocket) is a vacuum with essentially no traded support.
- **The 50 SMA is 6.95% below price.** The medium-term trend line has not validated the new price level yet. Pullbacks to it would look violent (−6.5% from here) but would be *normal* mean reversion.
- **Unexplained index-level anomalies.** Two volume spikes in the window (248.4M on 2026-06-26, and the 101.8M pre-earnings print on 2026-07-30) are event-driven and not indicative of trend conviction. I have not built any conclusion on them.
- **No fundamental/earnings data in the toolset.** I can describe the price/volume reaction on 7/31–8/3 but cannot verify *why* it happened. Treat the gap as an unexplained volatility event whose directional edge should be confirmed by the technical structure, not assumed.
- **What I am explicitly *not* claiming:** I am not asserting any "historical support/resistance bounce" — no level in this report has been tested more than twice in the visible data. The 225.55/226.16 double low (6/25 and 7/29 lows) is the only genuine multi-touch base in the window, and it is 15% below current price — relevant only as the structural origin of this advance, not as a tradeable level today.

---

## 10. Summary table

| Dimension | Reading (2026-08-13) | Signal | Evidence |
|---|---|---|---|
| **Long-term trend** | Price 265.13 vs 200 SMA 237.524 (**+11.62%**) | **Bullish** | 200 SMA rising 234.76→237.52 in 10 sessions |
| **Medium-term trend** | Price vs 50 SMA 247.914 (**+6.95%**) | **Bullish but extended** | 50 SMA inflected up from 246.38 (7/30) after a 9-point June–July decline |
| **Short-term trend** | Price vs 10 EMA 266.81 (**−0.63%**) | **Bearish (first break)** | First close below 10 EMA since 7/30; 4 lower lows since 8/10 |
| **Momentum (MACD)** | MACD 7.372 > Signal 6.119 | **Bullish, fading** | Crossed up 8/4; MACD line peaked 8.432 on 8/11 |
| **Momentum (histogram)** | 1.2525, down 6 straight sessions from 4.619 (8/5) | **Warning** | −73% thrust decay; still >0 so no reversal confirmed |
| **Momentum (RSI)** | 55.41, from 72.23 (8/3) | **Neutral / reset** | Overbought fully unwound without price damage; no divergence |
| **Volatility** | ATR 8.543 (3.22%); Bollinger width 30.5% | **Elevated, contracting** | ATR peak 9.983 (8/5), −14% since; 8/13 range 0.57× ATR |
| **Participation** | 5d vol 32.7M vs 20d 48.8M (0.67×) | **Constructive** | Pullback on ~1/3 of breakout volume = digestion, not distribution |
| **Volume-weighted price** | VWMA 261.986; price +1.20% | **Support nearby** | Coincides with unfilled gap floor 262.01 |
| **Key resistance** | 266.81 → 272.27 → 284.02 / 287.20 | — | 10 EMA, 8/11 lower high, post-gap peak / window high |
| **Key support** | 264.71 → 261.99 → 255.75 → 247.91 → 237.52 | — | 8/13 low, VWMA/gap floor, 20 SMA, 50 SMA, 200 SMA |
| **Primary bias** | **Uptrend intact; short-term digestion inside an unfilled breakaway gap** | **Bullish, conditional** | Accumulate 262–265, stop <254, targets 272.3 / 284.0 |
| **Invalidation** | Close <261.99 impairs breakout; close <247.91 breaks medium-term trend | — | Full gap-fill risk → 235.50 (−11%) |