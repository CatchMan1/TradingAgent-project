# AMZN — Multi-Indicator Technical Analysis
**As of close 2024-01-10 | Reference price: $153.73 | Verified snapshot + frozen OHLCV history (2023-06-01 → 2024-01-10)**

---

## 1. Verified data check (source-of-truth first)

The `get_verified_market_snapshot` (2024-01-10) and the `get_stock_data` CSV agree row-for-row — **no discrepancy to flag**.

| Item | Value (2024-01-10) |
|---|---|
| Open | 152.06 |
| High | 154.42 |
| Low | 151.88 |
| **Close** | **153.73** |
| Volume | 44.42 M |
| Split / Dividend | 1.0 / 0.0 (no adjustment noise) |

Supporting verified indicator readings on the same session:

| Indicator | Value | Read |
|---|---|---|
| close_50_sma | 146.346 | Price 5.0% above; rising |
| close_200_sma | 129.482 | Price 18.7% above; rising |
| close_10_ema | 150.279 | Price 2.3% above; just turned up |
| macd | 1.1525 | Positive, rebuilding |
| macds | 1.5419 | Still above MACD line |
| macdh | −0.3894 | Negative but improving 3 sessions straight |
| rsi | 60.43 | Bullish, not overbought |
| boll (20 SMA) | 150.7715 | Price above midline |
| boll_ub | 156.813 | First upside target |
| boll_lb | 144.730 | ~Recent swing low |
| atr | 3.048 | 1.98% of price |
| vwma | 150.632 | Price above volume-weighted avg |
| mfi | 0.485 | Neutral money flow (not confirming a breakout yet) |

---

## 2. The dominant structural story: a sharp V-shaped recovery inside an intact uptrend

The tape is best described as **a violent four-session dip that was fully repaired, with price closing at the highest level since 2023-12-21**.

Chronology (all from verified rows):

1. **Plateau / double top area, mid-to-late December.** Close peaks: 154.07 (12-18), 153.79 (12-19), 153.84 (12-21). Intraday peaks: 154.85 (12-18), 155.12 (12-19), **155.63 (12-20)**. Price then went flat-to-lower: 153.42 (12-22), 153.41 (12-26), 153.34 (12-27), 153.38 (12-28), 151.94 (12-29).
2. **Breakdown into year-end / new year.** 149.93 (01-02), 148.47 (01-03), **144.57 (01-04) with an intraday low of 144.05** and volume of 56.04 M (the heaviest of the last three weeks excluding the 12-15 rebalance print of 110.09 M). Close-to-close from 12-29 to 01-04: **−7.36 points, ≈ −4.85%**.
3. **Rebound.** 145.24 (01-05, low 144.53 — a second test of the same zone), then **149.10 (01-08, +2.66%)**, **151.37 (01-09, +1.52%)**, **153.73 (01-10, +1.56%, high 154.42)**. From the 01-04 close of 144.57 to 153.73 = **+9.16 points, ≈ +6.34% in four sessions**; from the 01-04 intraday low of 144.05 to the 01-10 high of 154.42 = **+10.37 points, ≈ +7.2%**.

**Why the dip looks corrective, not distributive:**
- The 01-04 close (144.57) finished *above* the 50-day SMA (144.3024) even though the intraday low (144.05) pierced it by ~0.25 — a textbook **test-and-reclaim of the 50-day** on a closing basis.
- The 01-04 close never violated the Bollinger lower band (143.397 that day); the 01-05 low (144.53) held above the band (143.552). **No downside band-break = volatility-contained pullback.**
- RSI bottomed at **40.23 (01-04)** — it never reached the 30 oversold threshold, which is exactly what a trend pullback (rather than a trend reversal) looks like.

**Where price now sits:** 153.73 is above the 12-22/12-28 congestion (153.3–153.4) and just below the December supply shelf. The immediate ceiling is the **154.42–155.63** band (01-10 high, 12-18/12-19/12-20 highs).

---

## 3. Trend architecture: bullish stack, all three averages rising

- **200-day SMA: 129.482**, up from 127.983 on 01-02 (+1.50 in six sessions). Slope is positive and steepening; price is **18.7% above** it. The strategic trend is unambiguously up, and this average has not been touched since the October 2023 lows (price low in the dataset: 118.35 on 2023-10-26) — a very wide cushion.
- **50-day SMA: 146.346**, up from 143.476 on 01-02 (+2.87 in six sessions, ~0.48/session), and rising in an almost unbroken line from 133.16 on 2023-11-13. The **50 > 200 configuration is firmly intact**; the gap is **16.86 points (≈13.0% of the 50-day)**, i.e., a well-established golden-cross regime, not a fresh, fragile one.
- **10-day EMA: 150.279** — this is the key short-term tell. It topped at 152.20 (12-28), sagged to **149.099 (01-05) and 149.099 (01-08)**, then **hooked back up to 149.512 (01-09) and 150.279 (01-10)**. Note the detail on 01-08: price closed at exactly 149.10, i.e., **right on the 10 EMA** — the pivot point of the recovery — before gapping away on 01-09/01-10.

**Alignment:** Close (153.73) > 10 EMA (150.28) > 50 SMA (146.35) > 200 SMA (129.48). This is the cleanest possible bullish stack, and critically, **price has re-taken the 10 EMA**, which is the precondition for the short-term leg to be considered "live" again.

**Breadth of the trend (context):** the stock rose from 122.77 (2023-06-01) to 153.73 — a **+25.2%** advance over the sample — with the largest single air-pocket being the 2023-09-21 to 2023-10-26 slide (144.85 → 119.57 close, i.e., −17.4%), which was subsequently reversed. The 200-day has been rising through all of it. The current pullback (−4.85% from 12-29 to 01-04) is small relative to that history, which supports treating it as noise within trend.

---

## 4. Momentum: MACD is turning up from below the signal — crossover is the next trigger

The MACD complex is the most informative part of the current tape:

| Date | MACD | Signal | Histogram |
|---|---|---|---|
| 12-22 | 3.136 | 2.873 | +0.263 |
| 12-28 | 2.989 | 2.958 | +0.031 |
| 12-29 | 2.782 | 2.923 | −0.141 |
| 01-02 | 2.428 | 2.824 | −0.396 |
| 01-03 | 2.006 | 2.660 | −0.655 |
| 01-04 | 1.341 | 2.396 | −1.055 |
| 01-05 | 0.859 | 2.089 | **−1.230 (low)** |
| 01-08 | 0.779 | 1.827 | −1.048 |
| 01-09 | 0.888 | 1.639 | −0.751 |
| **01-10** | **1.153** | **1.542** | **−0.389** |

Three observations:

1. **The histogram has improved for three consecutive sessions** (−1.230 → −1.048 → −0.751 → −0.389), i.e., the *rate of deterioration has reversed*. This is the classic precursor to a bullish MACD/signal cross.
2. **The MACD line never went negative.** It bottomed at 0.779 on 01-08 and is now 1.153. A MACD line that stays above zero through a correction means the intermediate-term momentum regime was never lost — unlike a true trend break, where MACD typically dives through zero.
3. **The gap to a cross is now small:** MACD 1.153 vs signal 1.542, a 0.389 spread. At the recent closing rate of progress (~0.20–0.28/session on the MACD line, with the signal line falling ~0.10–0.20/session), a **bullish crossover is plausible within roughly 1–3 sessions** *if* price holds above ~151.8. If price stalls, the histogram can re-flatten and this becomes a lower-high momentum structure instead.

**RSI: 60.43** — up from 40.23 (01-04), 42.13 (01-05), 51.67 (01-08), 56.24 (01-09). Three things matter here:
- The recovery from 40 to 60 in four sessions shows **demand returned fast** and confirms the MACD histogram turn.
- RSI is **not overbought** (below 70); the December peak RSI was only **68.05 (12-18)** — so this instrument has been setting *lower* RSI peaks while setting *higher* price highs in mid-December, a mild negative divergence that was arguably what the pullback purged.
- Now RSI is making a **higher low (40.23) versus the September-October sequence**, and pushing back into the 60s without exhaustion. That leaves room to 70 before momentum becomes a headwind.

---

## 5. Volatility: compressed bands, price in the upper half, ATR still modest

- **Bollinger midline (20 SMA): 150.7715**; **upper 156.813**; **lower 144.730**.
- Bandwidth = (156.813 − 144.730) / 150.7715 = **8.02%** — a narrow-to-moderate envelope. The upper band has been essentially flat since 12-29 (156.66 → 156.81), meaning the recent sell-off *compressed* rather than expanded volatility.
- Position within the bands: (153.73 − 144.73) / (156.81 − 144.73) = **~74% of band height**. Price is in the upper quartile — bullish positioning without a band ride.
- **ATR: 3.048**, or **1.98%** of the close. ATR has drifted down from 3.446 (12-18) to 2.806 (12-28) and back up to 3.048 — i.e., **volatility contraction through the pullback, mild expansion on the recovery**. That pattern (rising price + rising ATR off a low) is more consistent with accumulation than with a breakdown.
- **Practical ATR bands:** 1×ATR below 153.73 = 150.68 (coincides almost exactly with the 10 EMA at 150.28 and Bollinger midline at 150.77 — a genuinely *confluent* risk line). 2×ATR below = 147.63, which sits just above the 50-day SMA (146.35). An ATR-based stop below the pivot cluster is therefore ~$150.5, and a structural stop below the 50-day is ~$146.0.

---

## 6. Volume: the one genuinely mixed signal

| Metric | Value |
|---|---|
| 01-10 volume | 44.42 M |
| 20-session average (12-12 → 01-10, computed from returned rows) | ≈47.2 M |
| 01-04 sell-off volume | 56.04 M (above average) |
| 01-08 / 01-09 / 01-10 rebound volume | 46.76 / 43.81 / 44.42 M (average-to-light) |
| VWMA (verified) | 150.632 |

Interpretation:
- **VWMA at 150.632 with price 2.1% above it** confirms the volume-weighted participant is in profit and that the trend, net of volume, is up.
- **But VWMA has been creeping down** — 151.248 (01-03) → 150.978 (01-04) → 150.878 (01-05) → 150.929 (01-08) → 150.666 (01-09) → 150.632 (01-10) — while price rallied. That is the signature of **a rebound running on lighter volume than the decline that preceded it**. The 01-10 advance came on 44.42 M, ~94% of the 20-day average and well below the 56+ M prints seen on 12-15, 12-18 and 01-04.
- **MFI = 0.485** (neutral) reinforces this: money flow is neither confirming nor rejecting. A true breakout through 154.42–155.63 should be accompanied by MFI pushing up and volume > ~50 M; absent that, treat a break as lower-quality.

**Verdict on volume: neutral-to-slightly-negative confirmation.** This is the single reason not to be maximally aggressive on the long side right here.

---

## 7. Confluence map — actionable levels

| Level | Price | Source / basis |
|---|---|---|
| Upside cap #1 | **155.63** | 12-20 intraday high (highest in dataset since 2023) |
| Upside cap #2 | **154.85 / 155.12** | 12-18 / 12-19 highs |
| Immediate hurdle | **154.42** | 01-10 high (today's rejection point) |
| **Spot** | **153.73** | 01-10 close |
| Band target | **156.81** | Bollinger upper (2σ) |
| First support (pivot) | **150.28 – 150.77** | 10 EMA 150.28 / Bollinger mid 150.77 / VWMA 150.63 / 1 ATR 150.68 — four-way confluence |
| Rebound-integrity line | **149.10** | 01-08 close = 10 EMA pivot low |
| Trend support | **146.35** | 50-day SMA; 2 ATR = 147.63 |
| Structural floor | **144.05 – 144.73** | 01-04 low / 01-05 low 144.53 / Bollinger lower 144.73 |
| Long-term floor | **129.48** | 200-day SMA (not in play) |

---

## 8. Trading plan (scenario-based, with explicit triggers)

**Scenario A — Breakout continuation (primary, ~55% weight).**
Trigger: a **daily close above 154.42**, ideally above **155.63**, on volume ≥ ~50 M with MFI rising and MACD crossing above its signal. Targets in sequence: 156.81 (Bollinger upper), then extension toward the round-number 160 zone (flag: psychological level, not a tool-derived measurement). Entry/risk: stops at ~150.5 (below the 150.28–150.77 confluence) implies risk of ~$4.00–4.50 or ~2.6–2.9% — roughly 1.4 ATR — with an initial 1R of ~$2.4 to the upper band. **Position size off ATR:** with ATR = 3.05 (~2% of price), a 1%-of-equity risk budget implies a position of ~0.33× the notional you could carry in a low-volatility name — i.e., size down, not up.

**Scenario B — Choppy digestion below the December shelf (base case for the next 1–2 weeks, ~30% weight).**
Price stalls between 150.3 and 155.6, MACD crosses but flattens, RSI oscillates 50–65. Trade the range: buy the 150.3–151.0 confluence, sell/trim into 154.4–155.6. This is the scenario the *light volume* argues for.

**Scenario C — Failed rebound / lower high (~15% weight).**
Trigger: a close back below **149.10** (the 01-08 pivot) which would also break the 10 EMA and re-open the 146.35 (50 SMA) / 144.05–144.73 zone. Note the bearish tell to watch for: MACD making a **lower high** (failing around 1.5–2.0) while price makes a lower high below 155.63 — that would convert the current constructive setup into a distribution pattern. Hard invalidation of the bullish thesis: a **close below 146.35**, which would be the first close under the 50-day SMA since the October 2023 low.

**Cross-scenario risk management:** volatility is *low* right now (ATR 3.05 vs 3.45 on 12-18). Tight ATR stops in a compressed-band regime are vulnerable to whipsaw; a stop inside 1 ATR of the 150.5 pivot is likely to be hit by noise alone. Prefer close-based stops over intraday stops.

---

## 9. Why these eight indicators (and what each adds that the others don't)

| # | Indicator | Role in this specific setup |
|---|---|---|
| 1 | **close_200_sma** | Establishes the strategic regime. At 129.48 and rising, with price 18.7% above, it rules out "bear market rally" interpretations and means no strategic-level risk is in play. |
| 2 | **close_50_sma** | The medium-term trend and the exact line that was tested and reclaimed on 01-04 (low 144.05 vs SMA 144.30, close 144.57). Also the hard invalidation level. |
| 3 | **close_10_ema** | The pivot of the current recovery (149.10 on 01-05/01-08 → 150.28 now). It is the fastest objective arbiter of whether the rebound is still alive. |
| 4 | **macd** | Stays positive (1.15) through the whole pullback, proving the momentum regime was not lost; its approach to the signal line is the next event trigger. |
| 5 | **macdh** | Adds *rate-of-change* information the MACD line alone hides: three straight sessions of improvement (−1.23 → −0.39) is a leading cross-detection signal. Chosen instead of `macds` to avoid the near-perfect redundancy of line-vs-signal pairs. |
| 6 | **rsi** | Confirms the dip was a 40-handle pullback, not a 30-handle breakdown, and shows the current 60.4 leaves headroom before overbought. Also the tool for spotting the December lower-high divergence. |
| 7 | **atr** | Purely for risk: 3.05 (1.98%) sizes positions and anchors stops at 150.68 / 147.63, which happen to align with structural levels — validating the confluence. |
| 8 | **vwma** | The only volume-integrated price measure selected; at 150.63 it confirms participation *and* reveals the subtle negative (VWMA drifting down while price rises = light-volume rebound). |

**Deliberately excluded:** `boll`/`boll_ub`/`boll_lb` (used as context values from the verified snapshot but overlapping heavily with the 20-day midline already implied by the 50/10 averages and ATR), and `mfi` (useful, but it currently reads neutral at 0.485 and would be the ninth indicator; it is folded in as a confirmation filter rather than a primary input).

---

## 10. Bottom line

AMZN is in a **confirmed, mature uptrend** (price > 10 EMA > 50 SMA > 200 SMA, all rising; 50-day 13% above the 200-day) that just absorbed a **−4.85% pullback** without breaking a single structural level on a closing basis. Momentum has clearly turned back up — MACD histogram improving three sessions in a row, MACD line positive throughout, RSI 40 → 60 in four sessions — and price closed 2024-01-10 at **153.73, the highest close since 2023-12-21**, right beneath the **154.42–155.63** December supply shelf.

The two things keeping this from being a high-conviction breakout signal are (a) **volume that is running below average on the advance (44.42 M vs ~47.2 M 20-day average, VWMA drifting lower)** and (b) **MACD still below its signal (1.15 vs 1.54)**. Both are *timing* issues, not *direction* issues. The trade is to be long-biased but add on **confirmation** — a close above 154.42–155.63 with volume expansion and an MACD cross — while defining risk at the four-way confluence of **150.28–150.77**, with 149.10 as the "rebound is failing" line and 146.35 as the thesis-invalidation line. Do not chase into the shelf on light volume.

---

## Key Points Summary

| Dimension | Reading (2024-01-10) | Signal | Evidence |
|---|---|---|---|
| **Last close** | 153.73 (H 154.42 / L 151.88) | Bullish | Highest close since 2023-12-21; closed in upper 71% of the day's range |
| **Long-term trend** | 200 SMA = 129.48, rising | **Strong bull** | Price 18.7% above; +1.50 in 6 sessions |
| **Medium trend** | 50 SMA = 146.35, rising | **Bull** | Price 5.0% above; 50 SMA 13.0% above 200 SMA (mature golden cross) |
| **Short-term** | 10 EMA = 150.28, hooking up | **Bull** | Reclaimed after testing 149.10 on 01-05/01-08 |
| **Pullback depth** | 12-29 → 01-04: 151.94 → 144.57 | Corrective | ≈−4.85%; 50 SMA pierced intraday (144.05 vs 144.30) but held on close |
| **Recovery** | 01-04 → 01-10: 144.57 → 153.73 | **Strong** | ≈+6.34% in 4 sessions; +7.2% from the 144.05 low |
| **MACD** | 1.153 vs signal 1.542; hist −0.389 | Improving / pre-cross | Hist 3 straight improvements from −1.230 (01-05); MACD never went negative |
| **RSI** | 60.43 | Bullish, not extended | Rose from 40.23 (01-04); December RSI peak only 68.05 |
| **Bollinger** | Mid 150.77 / UB 156.81 / LB 144.73 | Upper half, compressed | ~74% of band height; bandwidth 8.0%; no lower-band break on 01-04 |
| **ATR** | 3.048 (1.98% of price) | Moderate / compressing | 1×ATR = 150.68 (aligned with 10 EMA); 2×ATR = 147.63 (near 50 SMA) |
| **Volume / VWMA** | VWMA 150.63; 01-10 vol 44.42 M vs ~47.2 M avg | **Mixed — the caveat** | Rebound volume < 01-04 sell-off volume (56.04 M); VWMA drifting down |
| **MFI** | 0.485 | Neutral | No money-flow confirmation yet |
| **Immediate resistance** | 154.42 → 154.85/155.12 → 155.63 | Key hurdle | Dec highs; upper band 156.81 beyond |
| **Immediate support** | 150.28–150.77 (4-way confluence) | Pivot | 10 EMA / Bollinger mid / VWMA / 1×ATR |
| **Invalidation** | 149.10 (soft) / 146.35 (hard) | Risk lines | 01-08 pivot; 50-day SMA |
| **Primary plan** | Long bias; add on close >154.42–155.63 with volume >50 M + MACD cross | Constructive | Targets 156.81 then 160 zone; stops below 150.5 on a close basis |

*Note: "next earnings" is a known catalyst — AMZN has historically reported fiscal Q4 results in early February; confirm the actual scheduled date before sizing positions around it. All price/indicator figures above are taken from the verified market snapshot and frozen OHLCV rows; percentage and average-volume figures are arithmetic derived from those rows.*