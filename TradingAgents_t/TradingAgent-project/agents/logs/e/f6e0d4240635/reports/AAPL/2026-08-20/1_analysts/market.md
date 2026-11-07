# AAPL — Multi-Timeframe Technical Analysis
**Analysis date: 2026-08-20 | Reference ticker: AAPL (Apple Inc.) | Last close: 311.30**

---

## 1. Data integrity check (verified snapshot vs. tool outputs)

I cross-checked the `get_stock_data` pull against `get_verified_market_snapshot` for 2026-08-20. **No discrepancies found** — the frozen row matches exactly:

| Field | Verified value (2026-08-20) |
|---|---|
| Open | 317.46 |
| High | 320.28 |
| Low | 310.65 |
| Close | **311.30** |
| Volume | 40,959,200 |
| Split / Dividend | 1.0 / 0.00 |

All indicator values produced by `get_indicators` reconcile to the snapshot values (RSI 48.9254, MACD −1.5608, MACD signal −1.0994, histogram −0.4614, 50SMA 309.8526, 200SMA 281.3000, 10EMA 310.5745, ATR 7.8075, VWMA 308.4148). All levels below are quoted directly from tool rows.

Note on the session itself: AAPL opened at 317.46, printed a high of 320.28, then sold off to close at 311.30 — **only 0.65 above the session low (310.65)** and 2.80% below the intraday high. That is a bearish intraday reversal bar, and it matters because of where it occurred (see §3).

---

## 2. Trend hierarchy: long-term bullish, intermediate flat, short-term unresolved

The three selected moving averages are deliberately chosen to disentangle three different horizons, and right now they tell three different stories:

**Primary (200-day): intact uptrend.** close_200_sma = **281.30**, rising monotonically across the whole window (272.76 on 2026-07-13 → 281.30 on 2026-08-20, a gain of ~8.54 points in 26 sessions, or roughly +0.166/day). Price at 311.30 sits **+10.67% above** the 200-day. Nothing in the tool data challenges the primary uptrend; the 50-day (309.85) remains far above the 200-day (281.30), so the golden-cross configuration established earlier in 2026 is still in force.

**Intermediate (50-day): flat, i.e., consolidation.** This is the single most diagnostic number in the report. close_50_sma progression:

| Date | close_50_sma |
|---|---|
| 2026-07-29 | 308.59 |
| 2026-07-31 | 309.50 |
| 2026-08-10 | 309.70 |
| 2026-08-17 | 309.08 |
| 2026-08-19 | 309.44 |
| 2026-08-20 | **309.85** |

The 50-day has moved only **+0.35 points in 15 sessions** and actually *fell* between 08-07 (309.79) and 08-17 (309.08). Contrast that with July, when it was climbing ~0.75–1.0 points *per day* (298.71 on 07-13 → 309.30 on 07-30). A flat 50-day after a steep advance is the mechanical fingerprint of a sideways base, not of a new downtrend — a downtrend would require the average to roll over, which it has not.

**Short-term (10-day EMA): momentum has stalled at the average.** close_10_ema = **310.57**. Its path is the cleanest description of the last month: it peaked at 331.31 on 07-30, collapsed to 308.76 on 08-17, and has ticked back up for three straight sessions (308.99 → 310.41 → 310.57). Price closing at 311.30 is **barely +0.23% above** the 10-EMA.

**The compression signal:** 10-EMA (310.57), 50-SMA (309.85), and VWMA (308.41) are now bunched into a **2.16-point band** — roughly 0.7% of price, or about **0.28 ATR**. When three independent averages from three different construction methods (exponential, simple, volume-weighted) converge this tightly, the market is coiling. That resolution — up or down — is likely to be the next meaningful directional move, and today's close sits *on top* of that cluster rather than decisively above or below it.

---

## 3. Where price actually is: inside the lower edge of an unfilled earnings gap

This is the most actionable structural fact in the dataset, and it is often missed by simple moving-average analysis.

AAPL closed at **333.43 on 2026-07-30** and then gapped down on **2026-07-31**, opening at 304.81, printing a low of **300.00**, and closing at **308.91** on **132,489,100 shares** — the largest volume in the visible dataset apart from 2026-06-26. That is a one-day decline of **−7.35%** on roughly 2.5× normal volume.

The 07-30 *low* was 329.59 and the 07-31 *high* was 310.69, so the true unfilled gap zone is approximately **310.69 → 329.59**. (Note there was no dividend on 07-31, so this gap is not a distribution artifact.)

Since then:

| Date | Close | High | Volume | Comment |
|---|---|---|---|---|
| 2026-07-31 | 308.91 | 310.69 | 132.49M | Gap day; sets gap edge |
| 2026-08-03 | 303.42 | 311.80 | 75.05M | Base low attempt |
| 2026-08-12 | 302.25 | 305.66 | 41.66M | Retest of base at low volume |
| 2026-08-14 | 305.93 | 307.49 | 28.23M | Lowest volume in the visible window |
| 2026-08-18 | 310.03 | 311.49 | 53.42M | Reclaims gap edge |
| 2026-08-19 | 316.83 | 319.28 | 50.51M | Pushes into gap |
| 2026-08-20 | **311.30** | **320.28** | 40.96M | **Rejected from 320; closes back at gap edge** |

**Interpretation:** the 08-18/08-19 rally pushed AAPL back *inside* the unfilled gap for two sessions, reaching 320.28 on 08-20 — and then failed, closing almost exactly at the gap's lower boundary (310.69). The close of 311.30 is **0.61 points above that boundary**. That is a razor-thin hold on the single most important pivot in the chart:

- **Hold and reclaim 316–320 →** the gap-fill trade is live toward 329.59 (07-30 low) and 333.43 (07-30 close).
- **Lose 310.69 →** price is back inside the 300.00–310.69 post-gap base, and the 08-18/08-19 advance becomes an unsuccessful retest.

---

## 4. Momentum: downside momentum is decaying, but the trend signal is still net negative

**MACD (selected: `macd` + `macdh`)** is the most nuanced part of the picture and deserves careful reading rather than a binary crossover call.

The MACD line peaked at **9.61 on 07-29**, collapsed with the gap, and crossed below zero on **2026-08-11** (−0.83). It has been negative for eight consecutive sessions and stands at **−1.5608** versus a signal line of **−1.0994** — i.e., still in a bearish configuration (MACD below signal, both below zero).

**But the histogram is telling the opposite story on a shorter horizon.** macdh progression:

| Date | macdh | |
|---|---|---|
| 2026-08-12 | −3.3429 | trough |
| 2026-08-13 | −3.0352 | |
| 2026-08-14 | −2.6482 | |
| 2026-08-17 | −2.2903 | |
| 2026-08-18 | −1.6590 | |
| 2026-08-19 | −0.7351 | |
| 2026-08-20 | **−0.4614** | 6th consecutive improvement |

That is a **six-session sequence of shrinking bearish bars** — the histogram has contracted by 86% from its 08-12 trough. Mechanically, the MACD line and signal line are converging rapidly and a bullish crossover looks imminent (on a histogram pace of ~+0.35/day, the cross could occur within roughly one to two sessions). **This is a positive-momentum divergence between the histogram and the price action**, and it is the strongest short-term argument for the bull case.

**The caveat that must be stated plainly:** a MACD crossover that occurs *below the zero line* is a counter-trend signal. It argues for a bounce or base, not for a new uptrend. To upgrade the signal from "bounce" to "trend," I need the MACD line itself to cross above zero (currently −1.56, so ~1.56 points of travel required).

**RSI (selected: `rsi`)** at **48.93** is neutral and, importantly, **shows no bullish divergence**. Checking the obvious candidates against tool data:

- 08-03 close 303.42 → RSI 40.34
- 08-12 close 302.25 → RSI 40.22 (price slightly *lower*, RSI essentially identical — no divergence)
- 08-19 close 316.83 → RSI 53.85
- 08-20 close 311.30 → RSI 48.93

RSI recovered from a 40.2–40.3 floor to 53.85 and then failed at ~54. That 54 failure is meaningful: in the July uptrend, RSI spent extended time between 61 and 72 (71.65 on 07-17). The inability to reclaim even the mid-50s on a two-day advance is a sign that the buyers are working off oversold conditions rather than reasserting trend control. RSI is not oversold (no <30 reading, and the lowest print in the entire window was 40.22), so there is no "washed-out" floor to lean on either. **48.93 is genuinely two-sided — it supports neither a strong buy nor a strong sell.**

---

## 5. Volatility and the Bollinger envelope (supplementary overlay)

`atr` is selected because this instrument has demonstrated two >6% single-day gap events in five weeks (2026-06-25: −6.10%, and 2026-07-31: −7.35%). Average-based trend tools are structurally blind to that risk; ATR is not.

**ATR = 7.8075**, or **2.51% of the 311.30 close.** The trajectory is informative:

| Date | atr |
|---|---|
| 2026-07-29 | 8.02 |
| 2026-07-31 | 9.87 (post-gap spike) |
| 2026-08-12 | 8.55 |
| 2026-08-17 | 7.64 |
| 2026-08-20 | **7.81** |

Volatility has **normalized and slightly re-expanded** (7.64 on 08-17 → 7.81 on 08-20). The 08-19–08-20 sessions (19.68-point and 9.63-point daily ranges) pushed ATR off its low. This is a useful tell: the base was built during a volatility contraction (08-14's 5.19-point range, ATR falling to 7.64), and volatility is now expanding *with price pressing the top of the base*. Range expansion at a range boundary usually resolves the range.

**Bollinger envelope (values used as a contextual overlay, not as a core signal — see §9).** On 2026-08-20: middle **315.52**, upper **341.28**, lower **289.77**.

- Band width = 51.51 points = **16.33% of the middle band** — a wide envelope, consistent with post-gap elevated realized volatility.
- Position within the bands (%B) = **0.418**, i.e., price sits in the **lower-middle half** of the envelope, below the 20-day mean of 315.52.
- The middle band has been **falling steadily** (324.37 on 07-31 → 315.52 on 08-20) as the late-July highs roll out of the 20-day window. The upper band is also rolling down (347.26 on 08-12 → 341.28 on 08-20) while the lower band has turned down (295.18 on 08-12 → 289.77 on 08-20).

**Concrete reading:** the 20-day mean (315.52) is *above* the 10-EMA (310.57), the 50-SMA (309.85), and the VWMA (308.41). That is a subtle but real negative: on a 20-day horizon, the average price paid is higher than the current price, meaning recent buyers are, on aggregate, under water. **315.52 is therefore the first genuine resistance on any rebound**, and today's rejection came in *above* it (at 320.28) before failing back below.

---

## 6. Volume: the advance lacked conviction, and today's decline lacked urgency

The selected `vwma` (308.41) is the key volume-integrated trend measure, and it has one subtle positive worth flagging.

**VWMA trend:** it fell for ten consecutive sessions — from **329.58 on 07-30** to **307.76 on 08-19** — then **rose for the first time on 08-20 (308.41)**. That is a genuine inflection in the volume-weighted average price, and it tells us the 08-19 advance came with enough volume-weighted participation to pull the metric up. Price (311.30) now sits **+0.94% above VWMA**, which is a modestly constructive reading: on a volume-weighted basis, the average buyer over the window is slightly in profit.

**But volume quality on the rally was mediocre.** Using the 20 most recent sessions in the tool data, average volume is approximately **53.0M shares** (my own computation from the tool's rows):

| Session | Volume | vs ~53.0M 20-day avg | Direction |
|---|---|---|---|
| 2026-08-12 | 41.66M | 79% | down |
| 2026-08-13 | 40.35M | 76% | up |
| 2026-08-14 | 28.23M | **53%** | up (lowest in window) |
| 2026-08-18 | 53.42M | 101% | up |
| 2026-08-19 | 50.51M | 95% | up |
| 2026-08-20 | 40.96M | 77% | down |

Two observations. First, the **declining volume into 08-14 (28.23M, the lowest reading in the entire visible history)** marked classic selling exhaustion — sellers ran out of supply, which is what allowed the subsequent lift. That is constructive and supports the base thesis.

Second, and more cautionary: **the 08-18/08-19 push back into the gap happened on merely average volume (101% and 95% of the 20-day mean), not on expanding volume.** A genuine gap-fill/reclaim breakout would typically show 130–150%+ of average volume. Combined with the fact that 08-20's decline came on *lighter* volume (77%) than the advance, the honest read is: **neither side is showing conviction.** The 08-20 rejection from 320.28 is therefore best interpreted as a low-conviction failure rather than aggressive distribution — but the 08-19 breakout was equally low-conviction, which is why it failed.

One minor calendar note: the tool data shows dividend events of 0.26 (2026-02-09), 0.27 (2026-05-11), and 0.27 (2026-08-10). The 2026-08-10 ex-date falls inside the recent consolidation window and may have contributed trivially to downward pressure, but at ~0.09% it is not a material driver. Next ex-date would be expected in the November quarter, outside this window.

---

## 7. Key levels (all derived directly from tool rows)

**Resistance (ascending):**

| Level | Source | Distance from 311.30 |
|---|---|---|
| 311.80 | 2026-08-03 high | +0.16% |
| 315.52 | Bollinger middle / 20-day mean | +1.36% |
| 316.29 | 2026-08-06 high | +1.60% |
| 316.83 | 2026-08-19 close | +1.78% |
| **320.28** | **2026-08-20 high — the rejection level** | **+2.89%** |
| 323.68 | 2026-07-20 low | +3.98% |
| **329.59** | **2026-07-30 low — full gap-fill target** | **+5.88%** |
| 333.43 | 2026-07-30 close (pre-gap) | +7.11% |
| 340.08 | 2026-07-28 close — highest close in dataset | +9.24% |
| 341.28 | Bollinger upper band | +9.63% |
| 344.57 | 2026-07-29 high — highest high in dataset | +10.68% |

**Support (descending):**

| Level | Source | Distance from 311.30 |
|---|---|---|
| 310.69 | 2026-07-31 high — **gap lower edge, today's pivot** | **−0.20%** |
| 308.41 | VWMA | −0.93% |
| 309.85 | close_50_sma | −0.47% |
| 305.59 | 2026-08-17 close | −1.83% |
| 302.05 | 2026-08-13 low | −2.97% |
| 300.57 | 2026-08-12 low | −3.45% |
| **300.00** | **2026-07-31 low — base floor** | **−3.63%** |
| 289.77 | Bollinger lower band | −6.92% |
| 281.30 | close_200_sma | −9.64% |

---

## 8. Actionable scenarios

### Scenario A — Gap-fill continuation (bullish; probability weighted moderate)
**Trigger:** a daily close **above 320.28** (the 08-20 high) *with volume ≥ 65M* (≥125% of the 20-day average), ideally accompanied by the MACD line crossing above its signal line (imminent) and then above zero.
**Rationale:** the base 300.00–320.28 has now been built over 15 sessions; a decisive break ends it. The unfilled gap at 310.69–329.59 has a mechanical gravitational pull, and the MACD histogram's six-session improvement supports the setup.
**Targets:** 329.59 (+5.88%) first, 333.43 (+7.11%) second. A close above 333.43 would put the 340.08/344.57 highs back in play.
**Invalidation:** a close back below 310.69.

### Scenario B — Range trade (neutral; currently the highest-probability path)
**Setup:** the 300.00–320.28 range (6.76% wide) is well defined by four separate lows (300.00, 301.32, 300.57, 302.05) and highs (311.80, 316.29, 319.28, 320.28) in the tool data.
**Execution:** accumulate in the **302–306** zone (1.0–1.2 ATR below current, above the base floor), target **316–320** (the Bollinger middle and rejection zone), with a hard stop **below 300.00**. At an entry of 305 with a stop at 299, risk is 6 points against ~12 points of upside — roughly 2:1.
**Why not buy here at 311.30?** The reward/risk is poor: −3.63% to the base floor versus +5.88% to the first real target, approximately 1.6:1, while price sits directly *under* the 315.52–320.28 resistance stack and *at* a freshly rejected level.

### Scenario C — Base failure (bearish)
**Trigger:** a decisive close **below 300.00** (the 07-31 gap low) on expanding volume.
**Implication:** the entire 15-session base is broken, the 08-18/08-19 advance is confirmed as a failed retest, and the MACD improvement is invalidated.
**Targets:** **289.77** (Bollinger lower band, −6.92%), then **281.30** (200-day SMA, −9.64%). Note that the 200-day is still rising, so a move to that level would be a deep mean-reversion event rather than a trend-break of the primary uptrend.

### Risk sizing
With ATR at **7.8075 (2.51%)**, a 1.5-ATR stop from the current price is **311.30 − 11.71 = 299.59** — which lands almost exactly on the 300.00 base floor. That is unusually clean confluence: **a 1.5-ATR stop and the structural invalidation level agree.** For a 1% portfolio risk budget per trade, position size ≈ risk$ ÷ (1.5 × 7.81). Because of the demonstrated gap risk (two >6% single-day gaps in five weeks), I would size positions assuming stops can be **skipped entirely** — i.e., use roughly half the position size that the ATR math alone would suggest.

---

## 9. Why these 8 indicators were selected

| Indicator | Role in this specific market context |
|---|---|
| **close_200_sma** (281.30) | Establishes the primary trend, which is clearly intact (+10.67% above, rising ~0.166/day). Prevents overreacting to a consolidation. |
| **close_50_sma** (309.85) | The most diagnostic single line: flat for 15 sessions (+0.35 pts) after rising ~1/day in July — mathematically confirms consolidation over decline. |
| **close_10_ema** (310.57) | Captures the short-term inflection (trough 308.76 on 08-17 → 310.57) and shows the 10/50/VWMA compression to a 2.16-point cluster. |
| **macd** (−1.5608) | Confirms the trend signal is still net negative (below signal *and* below zero since 08-11) — prevents confusing a bounce with a reversal. |
| **macdh** (−0.4614) | The most actionable momentum datum: six consecutive sessions of contraction from −3.34, an 86% reduction, indicating an imminent bullish crossover. |
| **rsi** (48.93) | Genuinely neutral with a failed 54 test and, critically, **no bullish divergence** — an honest negative that tempers the MACD histogram signal. |
| **atr** (7.8075) | Essential given two >6% gap events in five weeks; sets stops (1.5 ATR ≈ the 300 floor) and position size. |
| **vwma** (308.41) | Confirms volume-integrated price and provided the one genuinely new positive on 08-20 — its first uptick after ten declining sessions. |

**Deliberately excluded for redundancy:** `macds` (fully implied by macd and macdh), `boll`/`boll_ub`/`boll_lb` as *core* signals (the middle band is a 20-SMA, largely duplicating the 50-SMA's message; I used the band values only as a volatility envelope and resistance/support reference in §5 and §7), and `mfi`/`stochrsi`-type oscillators (highly correlated with RSI in a range-bound tape, adding noise rather than information).

---

## 10. Bottom line

AAPL is a **structurally healthy stock in a medium-term consolidation, sitting exactly on the pivot that will decide the next move.** The primary uptrend is unbroken (price +10.67% above a rising 200-day at 281.30, 50-day above 200-day). But the intermediate trend has gone flat — the 50-day has moved 0.35 points in 15 sessions — and the short-term picture is a **failed breakout**: price pushed into the lower edge of the unfilled 310.69–329.59 gap on 08-19/08-20, tagged 320.28, and closed back at 311.30, just 0.61 above the gap boundary.

The bullish case rests on three concrete, tool-supported facts: (1) the MACD histogram has improved for six straight sessions, shrinking 86% from −3.34 to −0.46, putting a crossover within a session or two; (2) selling volume dried up to 28.23M on 08-14 (53% of the 20-day average), marking exhaustion; and (3) VWMA turned up on 08-20 for the first time in ten sessions.

The bearish case is equally concrete: (1) RSI failed at 53.85 and fell to 48.93 with **no bullish divergence** anywhere in the base; (2) price is below the 315.52 20-day mean, below the Bollinger middle, and below the entire 316–320 resistance stack; (3) the 08-18/08-19 advance came on ordinary volume (101% and 95% of average), not breakout volume; and (4) the MACD crossover, when it comes, will occur **below the zero line** — a counter-trend signal.

**Net judgment: neutral-to-cautiously-constructive, with the trade defined by 310.69 on the downside and 320.28 on the upside.** I would not initiate at 311.30 — the setup is too close to resistance with a freshly rejected high overhead. The better expressions are either (a) buy the 302–306 zone with a sub-300 stop for a move back to 316–320, or (b) wait for a confirmed close above 320.28 on ≥65M volume and buy the break with a 310.69 stop for the 329.59/333.43 gap fill. A close below 300.00 should be treated as a full base failure and a reason to stand aside, not to average down.

---

## Summary Table

| Dimension | Reading (2026-08-20) | Signal | Key evidence |
|---|---|---|---|
| **Last close** | 311.30 (O 317.46 / H 320.28 / L 310.65) | Bearish reversal bar | Closed 0.65 above low, 2.80% below high |
| **Volume (08-20)** | 40.96M vs ~53.0M 20-day avg (77%) | Neutral-positive | Decline on light volume = low urgency |
| **Primary trend (200-SMA)** | 281.30, rising +0.166/day; price +10.67% above | **Bullish** | Golden-cross config intact |
| **Intermediate trend (50-SMA)** | 309.85; flat, +0.35 pts in 15 sessions | **Consolidation** | Was rising ~1.0/day in July |
| **Short-term (10-EMA)** | 310.57; trough 308.76 → 3-session uptick | Mildly bullish | Price +0.23% above |
| **MA compression** | 10EMA/50SMA/VWMA within 2.16 pts (0.28 ATR) | Coiling | Three methods converged — resolution likely |
| **MACD line** | −1.5608 vs signal −1.0994; below zero since 08-11 | **Bearish** | 8 sessions negative |
| **MACD histogram** | −0.4614; 6 straight improvements from −3.3429 | **Bullish (counter-trend)** | 86% contraction → crossover imminent |
| **RSI** | 48.93; failed at 53.85; floor 40.22 | **Neutral, no divergence** | No bullish div.: 08-03 303.42/40.34 vs 08-12 302.25/40.22 |
| **ATR** | 7.8075 (2.51% of price); 7.64 → 7.81 | Expanding off lows | 1.5 ATR stop = 299.59 ≈ 300 base floor |
| **VWMA** | 308.41; first uptick after 10 declining sessions | Mildly bullish | Price +0.94% above |
| **Bollinger (overlay)** | Mid 315.52 / Upper 341.28 / Lower 289.77; %B = 0.418 | Bearish positioning | Below 20-day mean; width 16.33% |
| **Critical pivot** | 310.69 (07-31 high = gap lower edge) | Close is +0.61 above | Gap zone 310.69–329.59 unfilled |
| **Upside trigger** | Close > 320.28 on ≥65M volume | Bullish | Targets 329.59 (+5.88%), 333.43 (+7.11%) |
| **Downside trigger** | Close < 300.00 | Bearish | Targets 289.77 (−6.92%), 281.30 (−9.64%) |
| **Reward/risk at 311.30** | ~1.6:1 to first target | Unfavorable | Better entry at 302–306 (≈2:1) |
| **Preferred action** | **Wait / range-trade 302–306 with sub-300 stop** | **Neutral** | Do not initiate at the rejection level |

*All prices, indicator values, and volume figures above are taken directly from `get_stock_data`, `get_indicators`, and `get_verified_market_snapshot` outputs for AAPL dated on or before 2026-08-20. The ~53.0M 20-day average volume is my own arithmetic over the tool's 20 most recent rows. No support/resistance "bounce" claims are made beyond the raw high/low prints cited.*