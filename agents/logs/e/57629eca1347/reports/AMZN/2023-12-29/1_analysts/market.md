# AMZN — Technical Analysis Report
**As of close 2023-12-29 · Instrument: AMZN (Amazon.com, Inc.)**

---

## 1. Verified data snapshot (source of truth)

From `get_verified_market_snapshot` (2023-12-29), the latest session:

| Field | Value |
|---|---|
| Open | 153.10 |
| High | 153.89 |
| Low | 151.03 |
| **Close** | **151.94** |
| Volume | 39,823,200 |
| 10 EMA | 152.1536 |
| 50 SMA | 143.0456 |
| 200 SMA | 127.7338 |
| MACD | 2.7820 |
| MACD Signal | 2.9230 |
| MACD Histogram | −0.1410 |
| RSI(14) | 59.01 |
| Bollinger Mid (20 SMA) | 149.824 |
| Bollinger Upper (2σ) | 156.6614 |
| Bollinger Lower (2σ) | 142.9866 |
| ATR | 2.8095 |
| VWMA | 150.7008 |

**Data-integrity notes (important for anyone reconciling numbers):**
- The frozen OHLCV series from `get_stock_data` matches the snapshot row-for-row on 2023-12-29 (close 151.94, volume 39.82M). No discrepancy between the two tools.
- Every indicator value from `get_indicators` matches the snapshot exactly (RSI 59.0123, MACD 2.7820, MACD-H −0.1410, ATR 2.8095, VWMA 150.7008, 50SMA 143.0456, 200SMA 127.7338, 10EMA 152.1536, bands 156.6614 / 142.9866). No conflicts to flag.
- ⚠️ **Quirk in the source data:** closes on 2023-09-26, 09-27 and 09-28 are identical (125.9800033569336) despite different OHLC ranges. That is almost certainly a vendor artifact, not three flat sessions. It sits outside the 50/200-day windows' most recent portion but is *inside* the 200-day window, so treat the 200-SMA as marginally less precise than the faster indicators.
- 2023-12-29 is the final session of the calendar year; the trailing week's volume (25–40M) is holiday-thinned relative to early December (40–58M, with 110M on the 12-15 quad-witching session). Volume conclusions below are therefore provisional.

---

## 2. Indicator selection and why

Eight complementary indicators were selected, deliberately spanning trend, momentum, volatility and volume, with redundancy removed:

1. **close_200_sma** — the strategic trend anchor and the line that defines whether this is a bull or bear tape.
2. **close_50_sma** — the medium-term trend and the "pullback magnet" that has been the operative support rail all autumn.
3. **close_10_ema** — the only fast average included; needed to time entries because the 50/200 lag badly at turning points.
4. **macd** — captures the medium-term momentum impulse and its cross of the signal line.
5. **macdh** — the histogram is the *rate-of-change* of momentum; it is the single best early-warning tool for a fade at a high, which is precisely the situation on 12-29. (Signal line used from the same MACD family rather than as a 9th slot.)
6. **rsi** — independent, price-normalised momentum/overbought gauge that is not built from EMA differences, so it is not redundant with MACD.
7. **atr** — required for stop placement and position sizing; AMZN's volatility is compressing, which changes the correct stop distance.
8. **vwma** — the only volume-integrated price measure here; it tells us whether the buyers moving size are paying up or fading.

*Deliberately excluded:* `boll`/`boll_ub`/`boll_lb` were computed and are quoted as supplementary context, but they overlap heavily with the 20-SMA/ATR information already captured; `macds` would be redundant with `macdh`; stochastic-type oscillators would duplicate RSI.

---

## 3. Primary trend: structurally bullish, and not marginally so

AMZN closed 2023 at **151.94**, which is:

- **+6.22%** above the 50 SMA (143.0456)
- **+18.95%** above the 200 SMA (127.7338)
- **+23.76%** above the 2023-06-01 close of 122.77

The moving-average stack is fully ordered and rising: **price (151.94) > 50 SMA (143.05) > 200 SMA (127.73)**. The 50 SMA sits **12.0% above** the 200 SMA — a wide positive spread indicating the golden-cross structure has been intact and *widening*, not merely holding. Both averages are still climbing with positive slope: the 50 SMA added **+4.15 points** between 2023-12-15 (138.8954) and 2023-12-29 (143.0456), while the 200 SMA added **+2.68** over the same ten sessions (125.0503 → 127.7338). Rising long averages beneath price is the least ambiguous bullish configuration available.

Two unfilled earnings gaps anchor this uptrend and are worth respecting:
- **2023-08-04:** open 141.06 vs prior close 128.91 (a ~9.4% gap); the subsequent low on 2023-08-18 was 131.15 — the gap was never filled.
- **2023-10-27:** close 127.74 vs prior close 119.57 (a ~6.8% gap); no post-gap print has come near 119.57. The lowest close since is 133.09 (2023-10-31).

Unfilled gaps of that size that survive months of trading are genuine demand footprints. The structural low of the observable period is the **2023-10-26 close of 119.57 (intraday low 118.35)**; from that close AMZN is **+27.07%**.

---

## 4. Medium-term context: a bottoming base followed by a textbook advance

Reading the actual sequence rather than the endpoints:

- **June–early August:** a 120–136 range, i.e. a base (June 1 close 122.77 → June 22 close 130.15).
- **Aug 4 earnings gap** to 139.57, then a high-level consolidation from 130 to 145 through August–September (September high close 144.85 on 09-13).
- **Late September–October correction:** a slide to the **October 26 low of 118.35 / close 119.57**, a −18% drawdown from the September 144.85 close.
- **Oct 27 onward:** an earnings-gap recovery followed by an unusually orderly, low-volatility ascending channel. There the stock climbed from the 133.09 close (10-31) to the **154.07 close on 2023-12-18**, with pullbacks repeatedly arrested in the 143–147 zone.

That is a "higher low → higher high" sequence with shrinking pullback depth. The medium-term trend is not in question.

---

## 5. Short-term: the tape is stalling at the top of a two-week range

This is where the nuance lives, and where the 8-indicator set earns its keep.

**Price action since the 12-18 breakout:**
- 12-18: **154.07** close (gap up from 149.97), high 154.85
- 12-19: 153.79 (high **155.12**)
- 12-20: 152.12 (high **155.63** ← period high)
- 12-21: 153.84
- 12-22: 153.42
- 12-26: 153.41
- 12-27: 153.34
- 12-28: 153.38
- **12-29: 151.94 (open 153.10, high 153.89, low 151.03, close near the low)**

Six consecutive sessions (12-19 through 12-28) closed inside a tight **153.34–153.84** band — a 0.5-point compression. The 12-29 candle broke that shelf and closed **below the 10 EMA (152.1536)** for the first time since 2023-12-11 (close 145.89 vs EMA 146.09). That is a short-term loss of control by buyers, though by only ~0.21 points — a marginal, not decisive, break.

**MACD family (the key evidence of deceleration):**
- MACD line peaked at **3.886 on 2023-11-27**, faded to **2.263 on 2023-12-14**, re-accelerated on the 12-18 gap to **3.136 (12-22)**, and has now rolled to **2.782 (12-29)**.
- The **histogram crossed from +0.031 (12-28) to −0.141 (12-29)** — a fresh bearish MACD/signal crossover.
- Critically, the MACD line is still **above zero (2.78 vs signal 2.92)**. This is a *momentum fade within an uptrend*, not a trend reversal. It is the same pattern (histogram rolling negative while MACD stays elevated) that appeared on 2023-11-30 → 2023-12-14 — and that fade resolved into a new leg up after the 12-18 gap. So the signal has a recent precedent for being a pause rather than a top.

**RSI:** 59.01, down from 68.05 (12-18) and 63.94 (12-28). RSI has now spent two months oscillating between roughly 54.5 (12-06) and 68.1 (12-18) — a *bullish regime* band that never touched 70 (no overbought excess to unwind) and never broke 50 (no momentum failure). The 12-29 drop is a reset, not a breakdown. Note the mild negative divergence: the 12-20 push to 155.63 printed RSI 62.67 versus 68.05 on the 12-18 push to 154.85. Higher high in price, lower high in momentum — a caution flag, but a shallow one, and it was already resolved downward by the 12-29 decline.

**VWMA — the diagnostic I weight most heavily here:** VWMA is **150.7008**, only **+0.82%** below the close. That gap has collapsed:
- 2023-11-20: close 146.13 vs VWMA 141.71 → price **+3.1%** above
- 2023-12-13: close 148.84 vs VWMA 146.47 → **+1.6%**
- 2023-12-29: close 151.94 vs VWMA 150.70 → **+0.82%**

Two readings, both valid: (a) VWMA has climbed sharply (145.31 on 12-04 → 150.70 on 12-29), which means *the bulk of traded volume is occurring at rising prices* — accumulation, not distribution; but (b) price is now almost sitting on its volume-weighted cost basis, meaning buyers at recent volume have essentially zero cushion. **VWMA at 150.70 is the single most important near-term line on the chart.** Holding it keeps the "quiet advance" thesis intact; losing it on heavy volume converts 150–155 into a supply shelf.

---

## 6. Volatility and risk management

**ATR is compressing hard: 3.7295 (2023-11-16) → 3.4460 (12-18) → 2.8095 (12-29)** — a **−24.7%** contraction over six weeks, and the lowest ATR in the sample. At 2.8095, one ATR equals **1.85%** of the 151.94 close.

Interpretation: this is a low-volatility, orderly advance — historically a healthy signature — but the 12-29 wide-body down day (range 151.03–153.89, i.e. **1.88%**, ~1.02 ATR) is a *volatility-expansion* candle following a compressed six-session shelf. Compressed volatility tends to resolve directionally rather than persist, and the resolution direction is now ambiguous.

**Position-sizing consequences:**
- A 2×ATR stop from a 151.94 entry is **~5.62 points**, or 3.7% of price. For a 1% account risk, that permits a position size of roughly 17.8% of equity *per 1% risk unit*.
- Because ATR has fallen, the *dollar* stop is tighter than it was in November — this flatters backtests but also means the stop is more likely to be hit by noise. A stop inside 1.5 ATR (≈4.2 pts) at 147.7 sits almost exactly on the 12-19/12-20 congestion, which is a poor place to hide a stop.

---

## 7. Bollinger context (supplementary)

- Mid (20 SMA) **149.824**, Upper **156.661**, Lower **142.987** → total width **13.675**, or **9.13%** of the mid.
- The expansion has been **one-sided upward**: between 2023-12-12 and 2023-12-29 the upper band rose from **148.777 → 156.661 (+5.3%)** while the lower band was essentially flat (**143.083 → 142.987**). A band walking up with a stationary lower band is the classic signature of a strong-trend "ride the band" phase, not of a mean-reverting range.
- AMZN actually closed **above** the upper band on 2023-12-18 (close 154.07 vs UB 151.37) — a genuine breakout signal in trend-following terms. Price is now back inside the bands at 151.94, i.e. the breakout has normalised. The **mid-band at 149.824** is the natural first retracement target and coincides with the 12-18 session low of 150.05 and the VWMA at 150.70. That cluster (**149.82–150.70**) is the most consequential support zone in the market right now.
- The upper band at **156.661** is rising ~0.4–0.6/day and is the dynamic ceiling on any breakout attempt.

---

## 8. Key levels (all derived from tool output)

**Resistance**
| Level | Source |
|---|---|
| **155.63** | 2023-12-20 intraday high — the period high |
| 155.12 | 2023-12-19 intraday high |
| **156.66** | Bollinger Upper (rising) — the breakout trigger zone |
| 154.85 / 154.07 | 2023-12-18 high / close (breakout pivot) |
| 153.84–153.89 | 12-21 close / 12-29 high — the failed shelf |

**Support**
| Level | Source |
|---|---|
| **150.70** | VWMA — the volume-weighted cost basis (first line of defence) |
| **149.82** | Bollinger Mid / 20 SMA |
| 150.05–151.03 | 2023-12-18 low / 2023-12-29 low |
| **147.4–147.9** | 2023-12-12 close (147.48), 12-08 close (147.42), 11-27 close (147.73) — congestion shelf |
| **143.0–143.6** | **50 SMA 143.046 + Bollinger Lower 142.987** (near-perfect confluence) + 2023-12-11 low 143.64 |
| 127.73 | 200 SMA — strategic line, far below (a −16% move would be needed) |

The **143.0 zone is the highest-quality reference in the entire chart**: the 50 SMA and the lower Bollinger band have converged within 6 cents of each other, and it has already been tested intraday on 2023-12-11 (low 143.64). A close below that zone would break both the medium-term trend rail and the lower volatility envelope simultaneously.

---

## 9. Actionable assessment

**Bias: constructively bullish on the primary trend; neutral-to-defensive for the next 1–3 weeks.** The evidence does not support a "top is in" call (MACD above zero, price above all three MAs, RSI in a healthy 59 regime, unfilled demand gaps below), and it does not support chasing (fresh negative MACD histogram, close below 10 EMA, price only 0.8% above VWMA, first close beneath the six-session shelf).

**Scenario A — base case (~50%): one-to-three week digestion, then continuation.**
Price mean-reverts into the **149.8–150.7** cluster (Bollinger mid + VWMA), holds, and rebuilds. The trigger for re-engagement: a close back above the **10 EMA (~152.15)** with the MACD histogram turning positive again — the same sequence that preceded the 12-18 gap. A decisive close above **155.63** with volume back above ~50M opens **156.66 (upper band)** and then a measured extension.

**Scenario B — bullish acceleration (~20%).** Year-end/January-seasonality plus a fresh record high on volume >50M. Note that 2023-12-29 volume of 39.8M is not a demand spike; a breakout on sub-45M volume should be treated as suspect.

**Scenario C — deeper retracement (~30%).** A close below **150.70 (VWMA)** on above-average volume shifts the burden of proof. Targets then become the **147.4–147.9** shelf, then the **143.0 confluence** (50 SMA + lower band). Losing 143.0 on a weekly closing basis would mark the first genuine break of the autumn uptrend in the tool data.

**Execution notes:**
- Do not initiate at 153–155. Reward-to-risk is poor there: the nearest resistance (155.63) is only ~+2.4% away while the nearest structural support (149.82) is −1.4% away, and the MACD histogram has just turned negative.
- Preferred entry zones: **150.05–150.70** (aggressive) or **147.4–147.9** (conservative). Stop below **146.9** (beneath the congestion shelf and ≈1.6 ATR) for the aggressive entry; below **142.5** for a swing position.
- Trimming/stop-management: with ATR at 2.81, a trailing stop of 2×ATR (≈5.6 pts) under the highest close would currently sit near **148.5**, which is tighter than the support structure — consider 2.5×ATR (≈7.0 pts) to clear the 147.4 shelf.
- Confirmation checklist for adding: (1) MACD histogram back above zero, (2) RSI reclaiming 62–65, (3) close > VWMA, (4) volume expansion above ~45M.

**Risks / caveats that reduce confidence in the above:**
1. The final-week volume sample is holiday-distorted (25–40M vs a 40–58M December norm); the 12-29 down day may be noise rather than distribution.
2. The RSI divergence at the 12-20 high is shallow and already partly discharged — it should not be over-weighted as a reversal signal.
3. The 200-SMA calculation window contains the 2023-09-26/27/28 flat-close data artifact, so the 127.73 level and the "+18.95% above 200 SMA" figure carry a small error band.
4. No historical validation of "bounces" off the cited levels is claimed here — the levels above are confluence zones derived from indicator values and dated price clusters, not proven reaction points, with the single exception of 2023-12-11's intraday low of 143.64 near the 143.0 zone.

---

## 10. Summary table

| Dimension | Reading (2023-12-29) | Evidence | Interpretation | Action |
|---|---|---|---|---|
| **Primary trend** | Strong up | Close 151.94 > 50SMA 143.05 > 200SMA 127.73; 50SMA +12.0% over 200SMA; both rising (50SMA +4.15, 200SMA +2.68 over 10 sessions) | Bull structure intact and widening | Strategic long bias |
| **Medium-term** | Up, staircase | Higher lows from 2023-10-26 close 119.57 (−18% low vs Sept); +27.07% off that close; unfilled gaps 08-04 and 10-27 | Accumulation, not distribution | Buy dips, not breakouts |
| **Short-term** | Stalling | 6 sessions pinned 153.34–153.84; 12-29 close 151.94 broke shelf and closed below 10EMA 152.15; low 151.03 | Loss of short-term control, marginal | No new entry at 153–155 |
| **Momentum (MACD)** | Decelerating | MACD 2.782 vs signal 2.923; histogram +0.031 → −0.141 (fresh bearish cross); MACD still >0 | Fade within uptrend (matches 11-30→12-14 precedent) | Wait for histogram to turn positive |
| **Momentum (RSI)** | Neutral-healthy | 59.01; down from 68.05 (12-18); 2-month regime 54.5–68.1, never >70 | Reset, not exhaustion; room to run | RSI <55 with price holding 149.8 = add zone |
| **Volatility** | Compressing then expanding | ATR 2.8095, −24.7% from 3.7295 (11-16); 12-29 range 1.88% ≈ 1.02 ATR | Coiled; directional resolution pending | 2×ATR stop ≈5.6 pts (3.7%) |
| **Bands** | Upper-band ride, normalised | UB 148.78→156.66 while LB 143.08→142.99 (one-sided expansion); 12-18 close 154.07 > UB 151.37 | Trend strength, now mean-reverting | Mid-band 149.82 = first target |
| **Volume** | Support thinning | VWMA 150.7008, price only +0.82% above (was +3.1% on 11-20); volume 25–40M vs 40–58M earlier in Dec | Buyers in control but without cushion | Close < 150.70 = reduce |
| **Nearest resistance** | 155.12 / 155.63 / 156.66 | 12-19 & 12-20 highs; Bollinger UB | ~2.4–3.1% upside to first test | Breakout needs vol >45–50M |
| **Nearest support** | 150.70 / 149.82 / 147.4–147.9 / 143.0 | VWMA; Boll mid; Dec congestion closes; 50SMA+BollLB confluence | 143.0 is the highest-quality rail | 143.0 close break = trend damage |
| **Net stance** | **HOLD / accumulate on weakness** | Trend + RSI supportive; MACD-H, 10EMA break and VWMA proximity argue patience | Bullish trend, extended short-term | Buy 150.0–150.7 or 147.4–147.9; stop 146.9 (aggressive) |