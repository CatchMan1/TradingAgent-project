# AMZN — Multi-Timeframe Technical Assessment (as of 2024-01-23 close)

**Data provenance note:** All exact price/indicator values below come from the `get_verified_market_snapshot` call for 2024-01-23, which returned the latest visible row: **O 154.85 / H 156.21 / L 153.93 / C 156.02 / V 37,986,000**. The individual `get_indicators` calls returned identical values to the snapshot for every overlapping field (e.g., 50-SMA 148.9522, RSI 61.5129, ATR 2.9460, upper band 158.4784) — **no discrepancy to flag** between tools.

---

## 1. Verdict in one paragraph

AMZN is in a **confirmed, orderly uptrend on all three timeframes** (short via 10-EMA, medium via 50-SMA, long via 200-SMA) and printed its **highest close in the ~7-month sample** on 2024-01-23 (156.02). However, the advance is **not accelerating**: both MACD and RSI are *lower* now than they were at the late-December price peak, which is a mild negative momentum divergence. Combined with **declining volume into the new high** and price sitting in the upper quartile of a slightly widening Bollinger channel, the tape reads as **trend-intact but flow-light** — a "hold/trail, buy dips" rather than "chase breakouts aggressively" posture.

---

## 2. Price structure and trend

**Short-term (days):** 10-EMA = **153.6932**, rising from 152.2597 (2024-01-18) to 153.6932 (2024-01-23). Price at 156.02 sits **+1.51% above** the 10-EMA, and the EMA slope has re-steepened after flattening during the 2024-01-11 → 2024-01-17 dip (EMA 152.045 → 151.984 → 152.260). That re-steepening is the cleanest short-term confirmation that the mid-January wobble was absorbed.

**Medium-term (weeks/months):** 50-SMA = **148.9522**, up **+7.24 points over the last 18 sessions** (141.7154 on 2023-12-26 → 148.9522 on 2024-01-23, ≈ +0.40/day, roughly +0.27%/day). This is a steep, persistent medium-term slope — not a lagging flatline. Price is **+4.75% above** the 50-SMA.

**Long-term:** 200-SMA = **131.6117**, rising ≈ +0.26/day (126.858 on 2023-12-26). Price is **+18.5% above** it. The 50-SMA sits **13.2% above** the 200-SMA — a wide, mature bullish separation consistent with a long-running uptrend, but also a reminder that mean-reversion risk to the long-term anchor is large if the trend breaks.

**Measured path (tool-verified closes):**
- Cycle low close **119.57 on 2023-10-26** (intraday low 118.35) → **156.02 on 2024-01-23** = **+30.5%**.
- September–October drawdown: **144.85 (2023-09-13) → 119.57 (2023-10-26) = −17.5%**, then a V-shaped recovery.
- Early-January dip: **153.79 (2023-12-19) → 144.57 (2024-01-04)** = **−6.0%**, with intraday low 144.05 on 2024-01-04.
- Recovery: **144.57 (2024-01-04) → 155.18 (2024-01-11)** = **+7.3%**, then a shallow pullback to **151.71 (2024-01-17)** = **−2.2%**, then a push to **156.02 (2024-01-23)**.

The structural read: **higher lows on the swing sequence** (119.57 → 144.05 intraday → 149.91 intraday on 2024-01-17) and **higher highs on closes** (144.85 → 154.07 → 155.18 → 156.02). Note that the 2024-01-23 close exceeds the prior window-high close of 155.18 (2024-01-11), but the **intraday high of 156.21 is still below the 2024-01-11 intraday high of 157.17** — i.e., a close-breakout that has not yet been confirmed on an intraday basis. That is the single most important unresolved detail in the chart.

---

## 3. Momentum

**MACD:** line **1.8647**, signal **1.6658**, histogram **+0.1990**.
- Bearish crossover occurred into the January dip (line fell to a trough of **0.7788 on 2024-01-08**, below the signal's 1.8269 that day).
- **Bullish re-cross on 2024-01-12** (line 1.6430 vs signal 1.5493, histogram +0.0937).
- Histogram briefly flickered **negative on 2024-01-17 (−0.0392) and 2024-01-18 (−0.0119)** — a soft, whipsaw-prone cross — then re-expanded to **+0.1090 / +0.1288 / +0.1990** on 2024-01-19/22/23.
- **Critical nuance:** MACD was **3.1186 on 2023-12-26** when AMZN closed 153.41; it is **1.8647 today** with price 1.7% higher. That is a **negative momentum divergence** — the second price advance carries materially less thrust than the December one. It does not invalidate the trend, but it argues against anticipating a vertical continuation.
- MACD has also just **reclaimed roughly its December mid-range** and is rising for the fifth consecutive session; direction is bullish even though magnitude is unimpressive.

**RSI:** **61.51**, in the bullish-but-not-overbought band. The 30-session range is **40.23 (2024-01-04) → 64.09 (2023-12-26)**, so RSI never reached 70 at any point in this window — the advance has been *grind*, not *froth*. Two consequences: (a) there is **headroom to ~70 without a mechanical overbought trigger**; (b) the same divergence appears here — RSI 61.5 at a higher price vs 64.1 at a lower price on 2023-12-26. RSI structure (higher lows: 40.2 → 42.1 → 51.7 → 60.4, and the 2024-01-17 dip holding 53.7 vs 40.2 on 2024-01-04) supports dip-buying over shorting.

---

## 4. Volatility and Bollinger positioning

- **Bollinger:** middle **152.1105**, upper **158.4784**, lower **145.7426**. Band width = **12.7358** (≈ **8.2% of spot**).
- Price is **+2.57% above the middle band** and **1.58% below the upper band**. **%B ≈ 0.81** — upper quartile of the channel, i.e., a bullish-regime location but *not* band-riding and *not* a stretch extreme.
- The upper band has crept from 155.4825 (2023-12-26) to 158.4784 — bands are **mildly expanding**, consistent with a trending rather than coiling market. The lower band at 145.7426 sits almost exactly on the **2024-01-04 intraday low of 144.05** region, giving a convenient volatility-defined downside envelope.
- **ATR = 2.9460**, i.e., **1.89% of price**. ATR peaked at **3.1196 on 2024-01-11** (post-dip expansion) and has since cooled to 2.95 — **volatility is contracting while price makes new highs**, which is the classic signature of a controlled, low-panic advance (and also the signature of thin participation; see volume).

**Risk arithmetic off the verified ATR:**
| Stop basis | Distance | Stop level from 156.02 |
|---|---|---|
| 1.0 × ATR | 2.95 | ≈ 153.07 |
| 1.5 × ATR | 4.42 | ≈ 151.60 |
| 2.0 × ATR | 5.89 | ≈ 150.13 |
| 2.5 × ATR | 7.37 | ≈ 148.65 (≈ 50-SMA 148.95) |

Note how **1.5×ATR (≈151.60) coincides almost exactly with VWMA 151.6183**, and **2.5×ATR (≈148.65) coincides almost exactly with the 50-SMA 148.9522**. Those are high-confluence invalidation levels, not arbitrary numbers.

---

## 5. Volume and participation

- **VWMA = 151.6183**, rising (149.5448 on 2023-12-26 → 151.6183 now). Price is **+2.90% above VWMA**.
- VWMA (151.62) sits **above the 50-SMA (148.95)** by ~1.8%, which means **the volume-weighted average price is higher than the simple average** — heavier dollar participation has occurred at the higher end of the range. That is a genuinely constructive flow signal and the reason I kept VWMA in the suite.
- **Caveat:** 2024-01-23 volume of **37.99M** is about **8% below the ~41M average of the last 20 sessions** I can reconstruct from the tool rows, and the new closing high came on the **second-lowest volume of the last six sessions** (2024-01-18 37.85M, 2024-01-23 37.99M). A breakout on contracting volume is a **lower-quality breakout** — it raises the odds of a retest of the 152–154 shelf before continuation.
- The highest recent volume prints were event-like, not trend-like: **110.09M on 2023-12-15**, 62.51M on 2023-12-18, 56.04M on 2024-01-04 (the down day). The lack of a 50M+ up-volume day since 2024-01-19 (51.65M) at the highs is a yellow flag rather than a red one.
- Snapshot MFI reads **0.6459** (≈ **64.6** on a 0–100 scale; the field is stored as a fraction). Money-flow is constructive and *not* overbought — consistent with RSI 61.5 and supportive of the "grind, not froth" characterization. Flagging the unit convention explicitly so no one misreads 0.6459 as a raw index level.

---

## 6. Actionable levels (all tool-derived)

**Resistance**
1. **156.21** — 2024-01-23 intraday high (immediate trigger).
2. **157.17** — 2024-01-11 intraday high; the level that would confirm the close-breakout on an intraday basis.
3. **158.48** — upper Bollinger band; statistically where a low-volume breakout stalls.

**Support**
1. **153.69** — 10-EMA (first, shallow pullback zone).
2. **154.85 / 155.12** — 2023-12-18 / 2023-12-19 highs; the prior breakout shelf now acting as the first retest zone (the 2024-01-23 open of 154.85 landed right here).
3. **152.11** — Bollinger middle / 20-SMA basis.
4. **151.62** — VWMA; also ≈ 1.5×ATR below spot.
5. **149.91** — 2024-01-17 intraday low (the most recent higher low).
6. **148.95** — 50-SMA; the medium-term trend line in the sand.
7. **145.74 / 144.05** — lower Bollinger band and 2024-01-04 intraday low; the structural-breakdown zone.

---

## 7. Scenario planning

**Base case (highest probability given the evidence): range-digestion between ~152 and ~157, then resolution higher.** Justification: 10-EMA > 50-SMA > 200-SMA with all three rising, price above VWMA, RSI 61.5, MACD histogram re-expanding, but volume declining and momentum divergence present. Expect a retest of 153.7–154.9 before another attempt at 157.17.

**Bull continuation:** A **daily close above 157.17 on volume ≥ ~45–50M** (i.e., above the 20-session average and in line with the 2024-01-19 and 2024-01-11 up-days) would confirm the intraday breakout and neutralize the volume objection. Next statistical objective is the **upper band 158.48**, with extension measured off the ~8.2% channel width.

**Bear/repair:** A close **below 151.62 (VWMA)** would break the volume-weighted support and put **149.91** in play; a close **below 148.95 (50-SMA)** would be the first objective medium-term trend damage in this leg and would shift the bias to neutral. Below **145.74/144.05** the multi-month structure is broken and the 200-SMA at 131.61 becomes the relevant long-term reference.

**Trade construction consistent with the above (illustrative, not a guarantee):**
- **Preferred entry:** pullback into **152.0–153.7** (Bollinger middle/10-EMA cluster), i.e., buying the trend where risk is tight.
- **Stop:** **~151.5** for a tactical long (≈1.5×ATR, at VWMA) or **~148.6–149.0** for a swing long (≈2.5×ATR, at the 50-SMA). Use the wider stop with smaller size, not the reverse.
- **Sizing math:** a tactical stop at 151.60 from 156.02 is 4.42 points = **2.83%**; risking 1% of equity implies a position of roughly **35% of equity notional**. With the swing stop at 148.95, risk is 4.53% and the 1%-risk position shrinks to ~22%.
- **Management:** given the MACD/RSI divergence and light volume, **trail stops under the 10-EMA rather than adding at the highs**; take partials into 157.2–158.5.
- **Do not short this configuration** on the divergence alone: every trend filter in the suite is bullish and RSI has yet to print 70 anywhere in the 30-session window — divergences in strong trends are timing signals, not reversal signals.
- **Event-risk caveat:** the ATR of 2.95 (1.9%) does **not** embed the gap risk of the upcoming quarterly report, whose date is not present in the tool data. Halve normal size into any unverified binary event; a 2×ATR-implied gap is ~4% and earnings gaps in this name have historically exceeded that (a general statement, not a verified figure from these tools).

---

## 8. Why these eight indicators (and why not others)

| Indicator | Value (2024-01-23) | Why it earns a slot |
|---|---|---|
| **close_10_ema** | 153.6932 | Fastest read on whether the mid-Jan dip is fully absorbed; sets the trailing-stop ladder. |
| **close_50_sma** | 148.9522 | The operative medium-term trend/support; its +0.40/day slope confirms trend *quality*, not just direction. |
| **close_200_sma** | 131.6117 | Strategic anchor — confirms the 50/200 bullish stack and size-of-reversion risk (+18.5% stretch). |
| **macd** | 1.8647 | Detects the January re-cross and, crucially, the lower-high vs December that flags fading thrust. |
| **macds** | 1.6658 | Required to date the 2024-01-12 re-cross and the 2024-01-17/18 histogram flicker. |
| **rsi** | 61.51 | Independent (non-EMA) momentum check; shows no overbought ceiling consumed, and confirms the same divergence. |
| **boll_ub** | 158.4784 | Defines the statistical ceiling and a breakout-vs-fade decision line; pairs with middle 152.11 / lower 145.74 for %B ≈ 0.81. |
| **atr** | 2.9460 | Converts volatility into stop distance and position size — the two stops above land on VWMA and the 50-SMA by coincidence of ATR, which is exactly why it's needed. |
| **vwma** | 151.6183 | The *only* volume-integrated price measure in the suite; it is why the light-volume breakout objection is quantifiable rather than vague. |

**Deliberately excluded:** `macdh` (its information is fully contained in the macd/macds pair I already have — reported above as +0.1990 for free), `boll` and `boll_lb` (the middle and lower bands are derivable/known: 152.1105 and 145.7426 — I cite them but did not spend dedicated slots), and `close_50_sma`/`close_200_sma` redundancy is avoided by using them for *different* jobs (entry structure vs long-term stretch). I also avoided stacking a second momentum oscillator (e.g., stochastic) alongside RSI, per the no-redundancy rule; MFI from the snapshot supplies the volume-weighted-oscillator angle instead.

---

## 9. Key points summary

| Dimension | Reading | Signal | Confidence |
|---|---|---|---|
| Trend, short (10-EMA 153.69) | Price +1.51% above; EMA re-steepening since 2024-01-18 | Bullish | High |
| Trend, medium (50-SMA 148.95) | Price +4.75% above; slope ≈ +0.40/day over 18 sessions | Bullish | High |
| Trend, long (200-SMA 131.61) | Price +18.5% above; 50>200 by 13.2% | Bullish / mature | High |
| Momentum (MACD 1.8647 / signal 1.6658) | Re-crossed 2024-01-12; histogram +0.199 and expanding | Bullish, modest | Medium |
| Momentum divergence | MACD 3.12 (2023-12-26) vs 1.86 now at higher price; RSI 64.1 vs 61.5 | Negative divergence | Medium |
| RSI 61.51 | 30-session range 40.2–64.1; never ≥70 | Bullish, not stretched | High |
| Bollinger (%B ≈ 0.81; upper 158.48) | Upper quartile, bands mildly expanding, not band-riding | Bullish, room limited | High |
| Volatility (ATR 2.9460 = 1.89%) | Cooling from 3.12 (2024-01-11) | Constructive but gap-blind | High |
| Volume (VWMA 151.62; 37.99M) | Price +2.90% above VWMA; volume ~8% below 20-session avg | Constructive structure, weak confirmation | Medium |
| Money flow (MFI ≈ 64.6) | Fraction field 0.6459; elevated, not overbought | Supportive | Medium |
| Immediate resistance | 156.21 → 157.17 → 158.48 | Breakout trigger zone | — |
| Immediate support | 153.69 → 152.11 → 151.62 → 149.91 → 148.95 | Dip-buy ladder / invalidation | — |
| Stance | **Long bias; buy 152–154 pullbacks, trail under 10-EMA, don't chase 156+ on light volume** | — | — |