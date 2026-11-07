# AMZN — Multi-Timeframe Technical & Tactical Report
**As of the verified session: 2026-09-09** | Close **$252.40**

---

## 1. Data integrity anchor (source of truth)

The verified snapshot and the raw OHLCV feed agree exactly on the 2026-09-09 row, and every indicator value returned by `get_indicators` matches the snapshot to full precision (10-EMA 257.589837, 50-SMA 254.680199, 200-SMA 239.4435, MACD −0.420808, Signal 0.906699, Histogram −1.327507, RSI 44.06238, Bollinger mid 260.147499, ATR 6.470983, VWMA 258.726144). **No discrepancies to flag.**

| 2026-09-09 | Value |
|---|---|
| Open | 253.12 |
| High | 254.69 |
| Low | 250.65 |
| **Close** | **252.40** |
| Volume | 33,055,500 |
| Session range | 4.04 (1.60%) |
| Close location in range | 43% from low (lower half) |

---

## 2. Indicators selected (8) and why

| Category | Indicator | Rationale for this specific setup |
|---|---|---|
| Trend (short) | **close_10_ema** | The pullback is only 15 sessions old; a fast EMA is needed to time whether the down-drift is still accelerating or flattening. |
| Trend (medium) | **close_50_sma** | AMZN is testing this line for the first time since the late-July breakout — the single most decision-relevant level on the chart. |
| Trend (long) | **close_200_sma** | Establishes whether this is a pullback inside an uptrend or the start of a trend reversal; also anchors the "gap-top" confluence near $239–240. |
| Momentum | **macd** | A trend/momentum oscillator that just produced a zero-line cross — separates a routine pullback from a momentum regime change. |
| Momentum | **rsi** | Checks whether selling is exhausted (oversold) or has room; also used for price/RSI divergence. |
| Volatility / mean | **boll** (with upper/lower from snapshot) | 20-day mean is the mean-reversion target and the lower band is the immediate decision line (price is 0.1% above it). |
| Volatility / risk | **atr** | Required for stop placement and position sizing at a moment when realized volatility is compressing fast. |
| Volume | **vwma** | Confirms whether the average *dollar-weighted* participant is in profit or underwater — the cleanest read on overhead supply. |

Deliberately excluded: `macds`/`macdh` (derivable from the snapshot's signal and histogram without a separate call), `boll_ub`/`boll_lb` (values supplied by the verified snapshot, so the middle band is the only missing piece), and stochastics/MFI (redundant with RSI in a directional, non-choppy tape).

---

## 3. Trend structure: long-term up, medium-term cracking, short-term down

**Long-term (200-day): intact and rising.**
- 200-SMA **$239.44**, up from $233.47 on 2026-07-13 and $238.33 on 2026-08-21 — a steady, monotonic rise.
- Price is **+5.41%** above it. The primary trend is still bullish.

**Medium-term (50-day): bullish alignment, but price has just broken it.**
- 50-SMA **$254.68**, above the 200-SMA by **$15.24 (+6.36%)** — a widening bullish spread.
- However, AMZN closed at $252.40, i.e. **0.90% below the 50-SMA**. Checking the daily series, this is the **first close below the 50-day SMA since 2026-07-31**, the session of the huge breakout gap. That is a meaningful medium-term warning even though the average itself is still rising (+$3.02 over the last eight sessions, ≈ +$0.38/day). A rising 50-SMA being lost from above is a classic "first crack" configuration, not yet a trend break.

**Short-term (10-day EMA): clearly bearish.**
- 10-EMA **$257.59**, price **2.01%** below it.
- The 10-EMA has rolled from $267.18 (2026-08-12) to $257.59, and price has printed **three consecutive lower session highs**: 261.12 (9/4) → 257.99 (9/8) → 254.69 (9/9). That is a textbook descending short-term channel.

**Structural context (why this is a pullback, not a reversal — yet):**
- The sequence of major swing lows in the dataset is rising: $196.00 (2026-02-17) → $199.34 (2026-03-27) → $226.65 (2026-07-29 close basis). The current low of $250.65 is far above all of them.
- The 2026-08-03 close of $284.02 was the highest close in the visible dataset; the 2026-08-03 intraday high was **$287.20**. From that high, AMZN is **−12.12%** (from the $284.02 close: **−11.13%**).
- The rally leg itself was enormous: from the 2026-02-17 intraday low ($196.00) to the 2026-08-03 high ($287.20) is **+46.5%**. A 12% give-back inside a 46% advance is normal digestion, *unless* key structure fails.

**Critical nuance — the July 31 gap:** On 2026-07-30 AMZN closed $235.50 (volume 101.8M); on 2026-07-31 it opened $265.00 and closed $271.58 on 129.1M shares (**+15.32%**). The unfilled gap between the 7/30 high ($239.82) and the 7/31 open ($265.00) is roughly **$25 wide**. That gap ceiling at **~$239.82 coincides almost exactly with the rising 200-SMA at $239.44**. This is the strongest technical confluence on the chart and the line in the sand for the medium-term trend.

---

## 4. Momentum: two independent bearish confirmations, no divergence

**MACD — fresh zero-line cross.**
- MACD line **−0.4208** vs signal **+0.9067**, histogram **−1.3275**.
- The MACD line peaked at **+8.43 on 2026-08-11** and has collapsed **8.85 points in 19 sessions**, crossing below zero on 2026-09-09 (from +0.118 on 9/8). Price is now below the signal line *and* below zero — two separate bearish conditions.
- Important context: the last negative MACD reading (2026-07-23 to 07-30, bottoming at −3.75) was resolved by the event-driven gap. That is **not** a repeatable pattern; do not treat the prior negative-MACD episode as a bullish precedent.

**RSI — weaker than the prior two dips, but not oversold.**
- RSI **44.06**, down from **55.85 on 2026-08-28** (−11.8 points in eight sessions).
- The August pullback troughs were **50.93 (8/18)** and **47.23 (8/27)**. The current reading of 44.06 is **below both**, i.e., momentum is deteriorating *faster* than it did on the earlier dips.
- There is **no bullish divergence**: price made a lower low (250.65 vs 251.93 on 9/1) and RSI made a lower low too. Price and momentum agree — this is confirmation of downside momentum, not a reversal signal.
- RSI remains 14 points above the 30 threshold, so there is mechanical room for further downside before an oversold bounce becomes statistically likely.

---

## 5. Volatility and Bollinger position: compressed drift, coiling for expansion

- Bollinger middle (20-SMA) **$260.15**; upper **$268.18**; lower **$252.12**.
- Price at $252.40 sits **$0.28 (0.11%) above the lower band** — **%B ≈ 0.02**, i.e., in the bottom ~2% of the band. This is a "band test," not yet a band break.
- Band width: **$16.06 = 6.17% of the middle band** — a comparatively tight envelope.
- ATR **$6.47 = 2.56% of price**, down from **$9.98 on 2026-08-05 (−35%)**. The 9/9 session range of $4.04 was only 0.62× ATR.
- **Interpretation:** the decline from $284 to $252 has been a *low-volatility drift*, not a high-volatility liquidation. That is usually a sign of orderly profit-taking/absence of bids rather than panic supply — but compressed ATR also raises the odds of a **range-expansion move** soon, with direction decided by the $250.65 / $257.6 resolution.
- **The mean is falling away from the price:** the 20-SMA dropped from $267.14 (8/27) to $260.15 (9/9), ≈ **−$0.7/session**. Mechanically, if price stays near $252, the 20-SMA converges on the 50-SMA ($254.68) within roughly **7–10 sessions** (this is a linear extrapolation of the recent slope, not a prediction). Two implications: (a) do **not** anchor a long target at $260.15 — it is moving down toward you; (b) a 20-SMA/50-SMA bearish cross is approaching.

---

## 6. Volume: orderly, but the average buyer is underwater

- 2026-09-09 volume **33.06M** vs an approximate 20-session average of **32.4M** (+1.9%) and a 5-session average of **28.6M** (+15.5%). No capitulation, but a mild uptick in activity on a down day that closed near the lows.
- Compare with the 2026-07-31 event volume of **129.1M** (~4× today's average) and the 2026-02-06 sell-off volume of **179.2M**. Today's tape is quiet by comparison — the pullback lacks the signature of institutional distribution so far.
- **VWMA $258.73**, i.e., **2.45% above spot** and above both the 50-SMA and the 10-EMA. The volume-weighted average transaction price of the recent window is higher than the current price: **the average recent buyer is underwater**. VWMA has fallen from $272.05 (8/20) to $258.73 — a steady slide that confirms sellers have controlled the tape for three weeks.
- The high-volume price node from mid/late August sits roughly **$262–$272** (e.g., 8/19 close $265.84 on 35.8M; 8/28 close $266.43 on 49.5M). That entire shelf is now **overhead supply** — every rally into it meets trapped longs.

---

## 7. Reference levels (all derived from tool data; none are "validated" historical pivots)

**Resistance — a dense cluster just overhead:**
| Level | Source |
|---|---|
| **$254.68** | 50-SMA (immediate pivot) |
| **$257.59** | 10-EMA |
| **$258.73** | VWMA |
| **$260.15** | Bollinger middle (falling ≈ $0.7/day) |
| $261.12 | 2026-09-04 high |
| $266.40 / $267.56 | 2026-08-19 / 2026-08-28 highs |
| $268.18 | Bollinger upper |

Anything between **$254.7 and $260.2** is a four-layer supply band. A close above $260.15 would be the first genuine repair signal.

**Support:**
| Level | Source |
|---|---|
| **$252.12** | Bollinger lower band |
| **$250.65** | 2026-09-09 low (the trigger line) |
| $250.00 | Round-number / psychological |
| $248.00 | 2026-07-16 low |
| **$243.59–$244.18** | 2026-07-14 / 07-17 lows (mid-July congestion) |
| **$239.44–$239.82** | 200-SMA + 2026-07-30 high (gap top) — strongest confluence |
| $235.50 | 2026-07-30 close |
| $226.65 | 2026-07-29 close (July low; primary-trend invalidation) |

---

## 8. Scenarios, triggers, and trade plans

*Subjective weights, not statistical probabilities.*

### Base case (~50%): range digestion, $248–$260
Momentum is bearish but volatility is compressing, volume is average, and price is sitting on the lower Bollinger band while still 5.4% above a rising 200-SMA. The most likely path is continued chop that digests August's excess. **No trade is the right trade here** — shorting the lower band and buying a fresh MACD zero-cross are both low-quality entries.

### Bearish continuation (~30%): break of $250.65 → $244–248 → $239–240
- **Trigger:** a daily close below **$250.65** accompanied by volume ≥ 40M (i.e., >20% above the 20-day average).
- **First target:** $248.00 (7/16 low), then **$243.6–$244.2**.
- **Stretch target:** **$239.4–$240.0** (200-SMA + gap top).
- **Execution note — do not chase:** at $252.4 with ATR $6.47, a stop above the 50-SMA ($255.8) is only 0.5 ATR away and will be noise-hit. The better risk/reward is to **sell a bounce into $257.5–$258.7** (10-EMA/VWMA), stop at **$260.60** (just above the falling 20-SMA), first target $252, second $246.5 — roughly **2.5:1 to 4:1** reward/risk depending on the fill.

### Bullish repair (~20%): reclaim $257.6–$260.2
- **Trigger:** a daily close above **$258.73** (VWMA), ideally on volume > 4-day average, then follow-through above **$260.15**.
- **Target:** $266.40–$267.56 (August highs), then the $268.18 upper band.
- **Invalidation:** a close back below $254.68 after the reclaim.
- **Note:** this is a counter-MACD trade. Size it smaller than a trend-aligned position and treat it as tactical.

### Highest-quality strategic entry (patient): $239–$244
If the pullback extends into the **200-SMA / gap-top confluence**, that is where the long-term trend, the unfilled gap, and the psychological $240 level align. A bullish reversal candle there (e.g., a close back above the prior day's high) with a stop below **$235.50** (7/30 close) offers a multi-week swing entry with the 200-SMA as support rather than overhead. This zone is **−5.0% to −3.3%** from spot, so there is no need to pre-position.

---

## 9. Risk management specifics

- **1 ATR = $6.47 = 2.56%** of price. A 1-ATR stop on a full-notional position is a 2.56% account hit; size so that 1 ATR ≈ 0.5–1.0% of equity → notional exposure of roughly **20–39% of equity** for a single 1-ATR-stop trade.
- **Gap risk is not in the ATR.** The 2026-07-31 session gapped +$25.18 from the prior high and closed +15.32%; the 2026-02-06 session fell −9.72% (232.99 → 210.32) on 179M shares. Both are event-style repricings. Reduce size or use defined-risk options ahead of scheduled catalysts.
- **Invalidation discipline:** the bearish thesis dies on a close above $260.15; the bullish thesis (pullback-within-uptrend) dies on a close below $226.65.

---

## 10. Monitoring checklist for the next 5–10 sessions

1. **Daily close vs $250.65** — the fresh leg low. Below = bear case active.
2. **Daily close vs $254.68** — reclaiming the 50-SMA quickly would neutralize today's break.
3. **MACD histogram (−1.3275)** — needs to stop making lower lows *before* price bottoms; watch for the histogram turning up while price holds $250–252 (early positive divergence).
4. **RSI 44.06** — a push back above 50 signals momentum repair; a break below 40 with a new price low signals continuation.
5. **VWMA slope ($258.73, falling since $272.05 on 8/20)** — flattening = supply being absorbed; continued decline = rallies remain sellable.
6. **20-SMA ($260.15) vs 50-SMA ($254.68)** — an approaching bearish cross (≈7–10 sessions if the current slopes persist).
7. **Volume on down days** — >40M would mark genuine distribution versus the current orderly drift.

---

## 11. Bottom line

AMZN is in a **short-term downtrend inside a still-intact long-term uptrend**. The bearish evidence is concrete and mutually reinforcing: first close below the 50-SMA since 2026-07-31, price 2.0% below the 10-EMA and 2.5% below the VWMA, a fresh MACD zero-line cross with a −1.33 histogram, RSI at 44.06 below both August troughs with no divergence, lower session highs for three straight days, and a fresh leg low at $250.65. The mitigating evidence is equally concrete: a rising 200-SMA 5.4% below price, a rising 50-SMA still $15 above the 200-SMA, ATR compressed 35% from its August peak (orderly, not panicked, selling), volume merely average, and price only $0.28 above the lower Bollinger band. **The tape is at an inflection, not in freefall.** The highest-expectancy actions are to (a) stand aside at the band, (b) sell strength into $257.5–$260.6 if it comes, or (c) buy a controlled break of $250.65 only after it stabilizes, with $239–$244 reserved as the highest-confluence strategic long zone.

---

## Key-points summary table

| Dimension | Indicator / Level | Latest reading (2026-09-09) | Signal | Actionable implication |
|---|---|---|---|---|
| Price | Close | $252.40 | Near session low, −11.13% from 8/3 close | Fresh leg low; lowest close since 7/30 |
| Short-term trend | 10-EMA | $257.59 | **Bearish** (price −2.01%) | Resistance on any bounce; descending highs 9/4→9/9 |
| Medium-term trend | 50-SMA | $254.68 | **Bearish break** (price −0.90%) | First close below since 7/31; reclaim needed to neutralize |
| Long-term trend | 200-SMA | $239.44 (rising) | **Bullish** (price +5.41%) | Primary uptrend intact; $239–240 is major confluence |
| Trend alignment | 50-SMA vs 200-SMA | +$15.24 (+6.36%) | **Bullish** | Golden-cross structure still widening |
| Momentum | MACD / Signal / Hist | −0.4208 / 0.9067 / −1.3275 | **Bearish** | Fresh zero-line cross; 8.85-pt collapse from 8/11 peak |
| Momentum | RSI | 44.06 | **Bearish, not oversold** | Below 8/27 trough (47.23); no divergence; room to 30 |
| Volatility | Bollinger mid / lower / upper | $260.15 / $252.12 / $268.18 | Price at lower band (%B ≈ 0.02) | Band test, not break; mid band falling ~$0.7/day |
| Volatility | ATR | $6.47 (2.56% of price) | **Compressing** (−35% from 8/5) | Use $6.47 for stops; expect range expansion soon |
| Volume | VWMA | $258.73 | **Bearish** (price −2.45%) | Average recent buyer underwater; overhead supply $262–272 |
| Volume | 9/9 volume | 33.06M vs ~32.4M 20-day avg | Neutral (no capitulation) | Orderly drift; >40M on a down day would change the read |
| Support | Key levels | $252.12 / $250.65 / $248.00 / $243.6–244.2 / $239.4–240.0 | — | $250.65 = bear trigger; $239–240 = strategic long zone |
| Resistance | Key cluster | $254.68 / $257.59 / $258.73 / $260.15 | — | Sell-zone for tactical shorts; close >$260.15 = repair |
| **Verdict** | — | — | **Short-term bearish / long-term bullish** | **Stand aside at the band; sell rallies into $257.5–260.6; buy $239–244 on stabilization** |