# AMZN — Technical Research Note
**As of close 2026-09-29 | Last price: $246.67**

---

## 1. Data integrity check (verified snapshot)

| Item | Verified value (2026-09-29) |
|---|---|
| Open / High / Low / Close | 246.71 / 248.84 / 245.14 / **246.67** |
| Volume | 33,730,400 |
| 10-EMA | 250.167 |
| 50-SMA | 256.087 |
| 200-SMA | 241.013 |
| MACD / Signal / Histogram | −2.560 / −1.903 / −0.657 |
| RSI(14) | 41.93 |
| Bollinger mid / upper / lower | 252.637 / 261.036 / 244.238 |
| ATR | 5.600 |
| VWMA | 251.342 |

The `get_stock_data` series and the verified snapshot agree exactly on the 2026-09-29 OHLCV row, and every indicator value returned by the indicator tool matches the snapshot to the displayed precision. **No discrepancies to flag on price or indicator data.**

One flag: the snapshot also returns `mfi = 0.441`. A money-flow index of 0.44 on a 0–100 scale would imply extreme oversold, which is inconsistent with RSI at 41.9 and price only ~1% above the lower Bollinger band. This looks like a 0–1 scaled artifact rather than a true MFI reading. **I have excluded it** from the analysis rather than reconciling it.

---

## 2. Trend structure: three timeframes, three different answers

This is the central nuance of the setup — AMZN is in a **rising long-term trend, a deteriorating medium-term trend, and a short-term downside drift that is now coiling**.

**Long-term (200-SMA) — intact uptrend.** The 200-SMA sits at **241.01** and is rising steadily (~+0.07/day over the last week, ~+2.4 points over the past month). Price at 246.67 is **+2.35% above it**. The 50-SMA (256.09) remains above the 200-SMA by **15.07 points (~6.3%)**, so the golden-cross configuration is intact. Nothing in the long-term data says "trend broken."

**Medium-term (50-SMA) — has rolled over.** The 50-SMA rose from 246.38 on 2026-07-30 all the way to a local peak of **256.29 on 2026-09-23**, and has since ticked down to **256.09**. That is the first sustained flattening/decline in the 50-SMA in this window. Price is **−3.68% below it**, and has closed below the 50-SMA continuously since 2026-09-22. A bearish 10/50 configuration (10-EMA 250.17 < 50-SMA 256.09) reinforces that the medium-term impulse is down.

**Short-term (10-EMA) — bearish, price pinned below.** The 10-EMA at **250.17** has been falling since 2026-08-11 (267.16) and price is **−1.40% below it**. Critically, the 10-EMA and the VWMA (251.34) are converging with the Bollinger mid (252.64) into a single overhead shelf.

**Price structure — textbook lower highs and lower lows since the 2026-08-03 peak:**

- Swing highs: 284.02 (Aug 3) → 278.09 (Aug 10) → 266.43 (Aug 28) → 258.90 (Sep 3) → 259.49 intraday (Sep 21)
- Swing lows: 257.73 (Aug 18) → 255.02 (Aug 27) → 249.58 (Sep 10) → 244.30 (Sep 16) → 244.73 (Sep 28)

From the 2026-08-03 close of **284.02**, AMZN is **−13.15%**. On a closing basis the low so far is **245.96 (2026-09-16)**, and the last two sessions carved marginally higher lows (244.73 on Sep 28, 245.14 on Sep 29 versus 244.30 on Sep 16). That is a *very* early, unconfirmed stabilization — not a reversal.

---

## 3. The earnings gap is the spine of this chart

On 2026-07-30 AMZN closed **235.50**; on 2026-07-31 it opened **265.00** and closed **271.58** — a **+15.32% gap on 129.05M shares**, roughly 3.8x the ~34M recent average. It extended to the **284.02 close / 287.20 intraday high on 2026-08-03**, which is the 2026 high.

The unfilled gap zone is **239.82 (Jul 30 high) to 265.00 (Jul 31 open)**. At 246.67 the stock is **inside the lower third of that gap** and **below the gap midpoint of 252.41**. Measured against the full 2026-07-29 low close (226.65) → 2026-08-03 high (284.02) impulse of 57.37 points:

- 50% retracement: **255.34** (already lost)
- 61.8% retracement: **248.57** (already lost on a closing basis)
- 78.6% retracement: **238.93** (not yet tested)

In other words, **more than 61.8% of the post-earnings impulse has been given back**, but the gap itself remains technically open. That is the definition of a *failed follow-through* rather than a *broken trend* — the distinction matters for how you trade it.

For contrast, the prior earnings event gapped the other way: 2026-02-05 close 222.69 → 2026-02-06 close 210.32 (**−5.55%**, 179.2M shares), followed by a multi-week base at 197–217. The stock's sensitivity to these events is large and two-sided.

---

## 4. Momentum: weak, deteriorating, but not exhausted

**RSI(14) = 41.93.** This is weak-neutral — below the 50 midline but **nowhere near the 30 oversold threshold**. Important context: RSI peaked at **72.23 on 2026-08-03** (confirming the overbought top) and has traced a lower-high sequence since. The September range is 39.45 (Sep 16) to 52.69 (Sep 21). Two observations:

1. RSI has **not** broken below 39 in September, whereas it hit **33.31 on 2026-07-29** before the earnings gap. Momentum damage is milder this time.
2. There is a **nascent non-confirmation**: price made a marginally higher closing low (246.15 on Sep 28 vs 245.96 on Sep 16) while RSI rose from 39.45 to 41.24 — a very shallow positive divergence. It is too small to trade on its own and needs a price trigger.

**MACD = −2.560, Signal = −1.903, Histogram = −0.657.** The MACD line crossed below zero on 2026-09-09 and has been below its signal since 2026-09-15. The important detail is the **failed bullish crossover**: the histogram compressed to −0.245 (Sep 21) and **−0.057 (Sep 22)** — within a hair of flipping positive — then re-expanded to −0.657 by Sep 29. That is a textbook momentum failure, and it lines up precisely with the failed price reclaim of the 50-SMA on Sep 21–22 (close 258.45, then 254.98, then 249.27). Two independent tools telling the same story strengthens the signal.

For perspective, the MACD line is at −2.56 versus −3.75 (2026-07-29) and −5.06 (2026-07-01). So momentum is negative but **not at an extreme**, leaving room for further downside before a mean-reversion setup becomes compelling.

---

## 5. Volatility: a genuine squeeze sitting on a decision point

This is the most actionable part of the setup.

- **ATR = 5.600**, or **2.27% of price**. ATR has collapsed from 9.95 (2026-08-03) and 9.51 (2026-07-31) to the lowest reading in the 60-session window.
- **Bollinger bandwidth = (261.036 − 244.238) / 252.637 = 6.65%.** On 2026-08-19 the bandwidth was ~29.6% (bands 220.47–296.99). Bandwidth has compressed by roughly **78%** in six weeks.

Compression of this magnitude is a **coiled-spring condition**: it raises the probability of a range expansion but says nothing definitive about direction. Direction must be taken from the trend/momentum context, which currently leans lower (price below 10-EMA, 50-SMA and VWMA; MACD negative and re-widening). Mechanically, a close outside the bands projects roughly one bandwidth beyond the break (≈227.4 below / ≈277.8 above) — treat that as a heuristic maximum, not a forecast; a 2×ATR move (≈11.2 points) is the more realistic near-term expectation.

Note also the **exhaustion signature at the top**: on 2026-08-03 AMZN closed at 284.02 versus an upper band of 272.99 — an ~11-point close *above* the band. It never closed above the upper band again. That is a classic blow-off extension, and it is the origin of the current downtrend.

---

## 6. Volume and participation: sellers in control, but no capitulation

- **VWMA = 251.342**, and price is **−1.86% below it**. On a volume-weighted basis the average holder of the last ~20 sessions is underwater — a bearish confirmation, and the reason 251.3 belongs in the resistance shelf.
- Volume behavior during the decline is **distributional, not panicked**: 52.27M on 2026-09-18 (price +2.3%), then 42.98M (Sep 21 up), 41.98M (Sep 22 down), 44.21M (Sep 23 down, −2.24%). Down days are being done on equal-or-heavier volume than up days.
- The 20-session average volume is ~**33.9M**; 2026-09-29 traded 33.73M — dead average. There is **no volume climax / capitulation bar** that typically marks a durable low.
- The Aug–Sep fade occurred on **declining** volume after the 90.8M (Aug 3) and 129.1M (Jul 31) events. Falling volume into falling price is ambiguous: it can signal a low-energy pullback (bullish) or simple absence of demand (bearish). Price location resolves it — and price is below every short-term average.

---

## 7. The level map

**Resistance (in order of importance):**
1. **248.84** — 2026-09-29 high (immediate)
2. **250.17** — 10-EMA
3. **251.34** — VWMA
4. **252.41** — 50% retracement of the Jul 29→Aug 3 impulse / midpoint of the Jul 31 gap
5. **252.64** — Bollinger mid — *items 2–5 form a dense 250.2–252.6 shelf*
6. **256.09** — 50-SMA (the regime line)
7. **258.45–259.49** — Sep 21/22 closing high and intraday high (failed-breakout pivot)
8. **262.65** — Aug 14 close; **266.43** — Aug 28 close
9. **284.02 / 287.20** — 2026 closing/intraday high

**Support:**
1. **244.24–245.14** — lower Bollinger band plus the Sep 16/28/29 lows (244.30 / 244.73 / 245.14)
2. **241.01** — 200-SMA (rising)
3. **239.82** — Jul 30 high / top of the unfilled gap
4. **238.93** — 78.6% retracement of the Jul 29→Aug 3 impulse
5. **235.50** — Jul 30 close (pre-gap)
6. **231.4–233.7** — late-July closing congestion

**The key confluence:** **238.9–241.0** is where the rising 200-SMA, the gap top and the 78.6% retracement all sit within ~2 points of each other. That is the highest-quality structural support on the chart, and it is only **2.3–3.2% below spot**.

---

## 8. Scenarios and actionable plans

The stock is in a **1.06-ATR-wide coil** (244.24 → 250.17). The professional play here is *not* to guess direction mid-coil; it is to define the triggers at the edges and let the market pay you for patience.

| Scenario | Trigger (daily close) | Invalidation | First target | Second target | Notes |
|---|---|---|---|---|---|
| **A. Coil break down (base case, trend-aligned)** | Close **< 244.24** on volume > ~40M | Close back **> 250.2** | 241.0 (200-SMA) | 239.8 → 238.9 (gap top / 78.6%) | MACD, VWMA, 50-SMA slope all already point this way. Poor R:R chasing at 246.7; better to short the retest of 250–252.6. |
| **B. Shelf rejection short (best R:R)** | Rally into **250.2–252.6**, rejection candle | Close **> 253.7** | 245.0 | 244.2 → 241.0 | Risk ~2.7 pts, reward ~7 pts ≈ **2.5R**. Aligns with 10-EMA + VWMA + Boll mid + gap midpoint. |
| **C. Confluence flush buy** | Flush into **241–244.3** with a reversal close / volume spike | Close **< 239.8** | 250.2 | 252.6 → 256.1 | Buying the 200-SMA against a rising long-term trend. Risk ~3.5–4 pts, reward ~9–12 pts ≈ **2.5–3R**. |
| **D. Trend-repair breakout long** | Close **> 252.64**, ideally **> 256.09** (50-SMA) | Close **< 247.5** | 259.5 | 262.6 → 266.4 | The failed Sep 21 breakout is the cautionary precedent — demand above-average volume (>40M) before trusting it. |
| **E. Structural breakdown** | Close **< 239.8** (gap top) | Close **> 244.3** | 235.5 | 231.4–233.7 | Would confirm the Jul 31 earnings breakout fully failed; medium-term trend flips down. |

**Risk management notes.** ATR is 5.60 (2.27%), so a stop inside ~4 points is inside daily noise. Size from the stop, not from conviction: for a 1%-of-equity risk budget, a 2×ATR (≈11.2 pt) stop implies roughly one-third of the dollar exposure that a 0.5×ATR stop would allow. If the 241.0 area is your invalidation, your true risk per share is ~6 points (2.4%), not 2.7.

**Event risk is the dominant unmodeled variable.** The data tools provide no earnings date, but AMZN's two most recent reports produced gaps of **−5.55% (Feb 6)** and **+15.32% (Jul 31)** with 3–5x normal volume. Any position carried through the next quarterly report is a volatility bet, not a technical trade. The current squeeze is exactly what you would expect *before* such an event — which is another reason the coil may not resolve purely on technicals.

---

## 9. Why these eight indicators

The market context is **a mature uptrend that has lost its medium-term momentum and is compressing into a decision point**, so the selection is deliberately stacked toward *trend regime* and *trigger definition* rather than toward redundant oscillators.

- **close_10_ema** — the immediate ceiling (250.17) and the top of the coil; fastest read on short-term momentum.
- **close_50_sma** — the single most important line on the chart (256.09). It defines bull/bear regime, it has just rolled over, and it was the level of the failed 2026-09-21 breakout.
- **close_200_sma** — the rising long-term anchor (241.01) and the structural support that keeps this a "pullback" rather than a "top."
- **macd** — trend/momentum level; captures the loss of the post-earnings impulse.
- **macds** — the crossover timing line; the Sep 21–22 near-crossover that failed is the cleanest momentum signal in the dataset.
- **rsi** — overbought/oversold and divergence; confirms the Aug 3 exhaustion (72.2) and shows there is *no* oversold cushion yet at 41.9.
- **atr** — volatility regime and stop placement; the collapse to 5.60 is both the squeeze evidence and the position-sizing input.
- **vwma** — volume-weighted confirmation (251.34); identifies where the marginal buyer is trapped and adds an independent, non-redundant read on the 250–252.6 shelf.

Deliberately excluded: Bollinger upper/lower and the MACD histogram overlap heavily with ATR/RSI and the MACD pair respectively — I used them as *confirmation* of the squeeze and the failed crossover, not as separate decision inputs. No stochastic-family oscillator was included because RSI already covers the overbought/oversold axis.

---

## 10. Bottom line

AMZN is **not broken, but it is not healthy either**. The long-term structure (rising 200-SMA, 50>200) remains constructive and price is still 2.35% above the long-term anchor. Everything shorter than that is bearish: a −13.15% decline from 284.02 with a clean lower-high/lower-low sequence, price below the 10-EMA, 50-SMA and VWMA, a failed reclaim of the 50-SMA on 2026-09-21, and a MACD that has just re-widened to the downside after nearly crossing up.

At the same time, **ATR and Bollinger bandwidth are at six-week lows**, price is holding a 244.2–245.1 shelf with three marginally higher lows, and RSI at 41.9 is stabilizing rather than collapsing. The honest read is **"coiled and leaning lower, sitting on the last defensible support zone above the 200-SMA."**

The tradable asymmetry lives at the **241–244.3 confluence** (buy zone, stop under 239.8) and at the **250.2–252.6 shelf** (sell/trim zone, stop above 253.7). Mid-range at 246.67, with 2.4% to the first real support and 1.4% to the first real resistance, the risk/reward is poor in both directions — which is precisely why the edge is in waiting for one of those two edges to be tested rather than acting on today's close.

---

## 11. Key points summary

| Indicator | Value (2026-09-29) | Signal | Key level / actionable implication |
|---|---|---|---|
| **Price (close)** | 246.67 | Below 10-EMA, 50-SMA, VWMA; above 200-SMA | Coil between 244.24 and 250.17; −13.15% from 284.02 (Aug 3) |
| **close_10_ema** | 250.167 | Bearish (price −1.40%) | First resistance; top of the coil. Break above opens 252.6 |
| **close_50_sma** | 256.087 | Bearish (price −3.68%); slope just turned down | Regime line. Failed reclaim on Sep 21; needs a close >256.09 to repair |
| **close_200_sma** | 241.013 | Bullish (price +2.35%); rising ~+0.07/day | Major confluence support with 239.82 gap top and 238.93 (78.6% retrace) |
| **MACD** | −2.560 | Bearish; negative since Sep 9, not yet extreme | Room to −3.75 (Jul 29) before an oversold read |
| **MACD signal** | −1.903 | Bearish; MACD below signal since Sep 15 | Failed crossover: histogram nearly crossed (+→−) on Sep 22 |
| **RSI(14)** | 41.93 | Weak-neutral; no oversold cushion | Peaked 72.23 at Aug 3 top; shallow positive divergence vs Sep 16 |
| **ATR** | 5.600 (2.27%) | Low volatility / squeeze | Lowest in 60 sessions; 1×ATR stop ≈ 241.1 (aligns with 200-SMA) |
| **VWMA** | 251.342 | Bearish (price −1.86%) | Confirms 250.2–252.6 resistance shelf; volume-weighted buyer is trapped |
| **Bollinger mid / upper / lower** | 252.637 / 261.036 / 244.238 | Squeeze; bandwidth 6.65% (vs ~29.6% on Aug 19) | Break of 244.24 or 261.04 likely to expand range; 244.24 is the trigger level |
| **Gap (Jul 30 high → Jul 31 open)** | 239.82 → 265.00 | Unfilled; price in lower third | Gap midpoint 252.41 reinforces resistance; 239.82 is the structural line in the sand |
| **Volume** | 33.73M (20-day avg ~33.9M) | Distribution on down days; no capitulation | Want >40M to validate a breakdown or a genuine breakout |

*All price and indicator figures above are taken from the verified 2026-09-29 snapshot and the indicator tool output for AMZN; no fundamental, news, or index-level data was available to these tools and none has been assumed.*