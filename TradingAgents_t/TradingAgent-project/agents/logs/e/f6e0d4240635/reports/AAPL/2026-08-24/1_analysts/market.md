# AAPL — Technical Analysis Report
**Analysis date: 2026-08-24 | Verified close: $310.34**

---

## 1. Data Integrity & Verified Snapshot Check

Before any interpretation, I reconciled the two data sources:

- `get_stock_data` and `get_verified_market_snapshot` **agree exactly** on the 2026-08-24 row: **Open 311.47 / High 313.36 / Low 309.97 / Close 310.34 / Volume 34,673,600**.
- All indicator values cited below are taken from the verified snapshot (latest visible session) and cross-checked against the indicator time series. **No conflicts found.**
- **One flagged anomaly:** the snapshot's `mfi` reads **0.576508**, which is on a 0–1 normalized scale rather than the conventional 0–100 MFI scale. Because the scale is ambiguous, I have **excluded MFI from all conclusions** rather than mis-citing it as "neutral money flow."
- Corporate actions in the window: dividends of $0.26 (2026-02-09), $0.27 (2026-05-11), $0.27 (2026-08-10); no splits. The total-return index (315.85) sits above the raw close (310.34), consistent with dividend accrual.

**Verified indicator panel (2026-08-24):**

| Indicator | Value | Read |
|---|---|---|
| Close | 310.34 | — |
| 50-SMA | 310.50 | Price **$0.16 below** (−0.05%) |
| 200-SMA | 281.70 | Price **+10.17% above** |
| 10-EMA | 310.35 | Price essentially **at** it (−0.003%) |
| MACD (12,26) | −1.488 | Negative regime |
| MACD Signal | −1.253 | MACD below signal |
| MACD Histogram | −0.235 | Negative but collapsing toward zero |
| RSI (14) | 48.23 | Neutral, mid-range |
| Bollinger Mid (20) | 313.01 | Price below basis |
| Bollinger Upper | 335.14 | — |
| Bollinger Lower | 290.88 | — |
| ATR (14) | 7.37 | 2.38% of price |
| VWMA | 309.15 | Price +0.39% above |

---

## 2. Indicator Selection & Why These Eight

I selected **eight complementary indicators** across five categories, deliberately avoiding redundancy:

| # | Indicator | Why it is the right tool *for this specific market context* |
|---|---|---|
| 1 | **close_50_sma** | The single most important line right now: price is pinned within $0.16 of it, and the line has gone **flat** — the precise signature of a trend stall after a distribution event. This is the medium-term regime arbiter. |
| 2 | **close_200_sma** | Separates a *pullback inside an uptrend* from a *trend reversal*. It is rising ~0.2 pts/session and sits 10.2% below price, keeping the structural bull case alive. Non-negotiable for strategic context. |
| 3 | **close_10_ema** | Because price has collapsed onto this fast average after a 4-week drift, the 10-EMA is the cleanest short-term inflection gauge and the natural first trigger line for entries. Unlike the 50-SMA, it responds within days. |
| 4 | **macd** | Confirms the *regime shift*: MACD crossed below zero on 2026-08-11 and remains negative. This is the objective evidence that the July impulse ended, not just paused. |
| 5 | **macdh** | The highest-information indicator on the board right now. It has improved for **13 straight sessions**, from −3.634 to −0.235 — quantifying decelerating downside momentum and flagging an imminent signal crossover. |
| 6 | **rsi** | At 48.23 it answers a critical question: *is there a mean-reversion edge?* No. It is neither oversold (30) nor overbought (70), so no contrarian fuel exists in either direction — it rules out two tempting but unsupported trades. |
| 7 | **atr** | Contracting from 9.87 → 7.37. This is the risk-management backbone: stop placement and position sizing must scale to 2.38% daily range, not to the 3.2% range that prevailed on 2026-07-31. |
| 8 | **vwma** | The only indicator that fuses price and volume. It tells us whether the *volume-weighted* participant is in profit or loss. VWMA has flattened at ~309, and price is just above it — a subtle but important shift from the one-way decline of July. |

**Deliberately excluded:**
- **Bollinger Bands (boll/boll_ub/boll_lb)** — I read them as a *supporting overlay* (values above) rather than counting them among the eight, because the **20-SMA middle band duplicates the 10-EMA/50-SMA trend cluster**, and band width is a volatility measure that **ATR already covers**. Adding all three would have consumed three of eight slots for redundant information.
- **macds** — the signal line's information is fully expressed through `macd` + `macdh`; selecting it separately would be redundant.
- **mfi** — scale anomaly (see §1).

---

## 3. The Dominant Structural Fact: A Violent Regime Break on 2026-07-31

Everything in the current tape is downstream of one session.

- **2026-07-28:** AAPL closed at **340.08**, its highest close in the data window (intraday high **344.57** on 2026-07-29).
- **2026-07-31:** The stock gapped from a 333.43 close to a **304.81 open**, printed a low of **300.00**, and closed **308.91** — a **−7.35% single-session decline** on **132,489,100 shares**, roughly 2.5–3× the typical 40–55M share day.
- That gap remains **structurally unfilled**: the void spans roughly **310.69 (07-31 high) to 329.59 (07-30 low)**.

This is not a routine pullback. It is a **volume-confirmed distribution event** that converted a strong uptrend into a range. The significance: **price at 310.34 is sitting on the bottom lip of that gap, right where the 50-SMA (310.50) also sits.** Two independent references converge at the same price — that is an unusually meaningful pivot.

**Note a precedent worth flagging (fact, not forecast):** the previous high-volume shock — **2026-06-25, −6.11% to 275.15 on 107M shares** — was followed by a full recovery to **340.08 by 2026-07-28** (+19.8% from the 06-26 close of 283.78). Two capitulation-type days in ten weeks, one bought aggressively, is a genuine ambiguity rather than a clean bullish or bearish setup.

---

## 4. Trend Analysis: Three Timeframes, Three Different Answers

This is the central tension of the report — and it is why any single-timeframe conclusion here is wrong.

### Long-term (200-SMA): intact uptrend
The 200-SMA has risen monotonically from **253.92 (2026-04-27) to 281.70 (2026-08-24)**, a slope of roughly +0.2 points per session. Price sits **10.17% above it**. The 50-SMA (310.50) remains **28.80 points / 10.22% above** the 200-SMA — a wide, still-constructive "golden cross" configuration. For context, closes rose from **246.70 (2026-01-20)** to **340.08 (2026-07-28)**, a **+37.85%** advance. Nothing in the long-term structure has broken.

### Medium-term (50-SMA): stalled, and now the battleground
The 50-SMA climbed from **260.26 (2026-04-27)** to a peak of **309.79 (2026-08-07)**, then **flattened**: it dipped to **309.08 (2026-08-17)** and has crept back to **310.50**. A flattening 50-SMA after a vertical advance means **the average participant's cost basis has converged with price** — the market is at equilibrium, not trending. Price closing **$0.16 below** this line is not materially bearish, but the *coincidence* of price, 10-EMA, 50-SMA, and gap bottom inside a ~1.4-point band (309.15–310.69) is the definition of a decision point.

### Short-term (10-EMA): stabilizing after a controlled descent
The 10-EMA peaked at **331.31 (2026-07-30)**, fell for 13 consecutive sessions to **308.76 (2026-08-17)**, then turned **flat-to-up** (308.99 → 310.41 → 310.57 → 310.35 → 310.35). Price closing exactly at the 10-EMA is a **short-term equilibrium**, not a trend. The prior downtrend in this average has been arrested.

**Verdict:** long-term bullish, medium-term **neutral/compressed**, short-term **neutral but stabilizing**. This is a **coiled market**, not a trending one.

---

## 5. Momentum: The Most Constructive Signal on the Board

### MACD histogram — 13 consecutive sessions of improvement
| Date | Histogram | MACD |
|---|---|---|
| 2026-08-05 | **−3.634** (trough) | +2.089 |
| 2026-08-17 | −2.290 | −2.676 |
| 2026-08-20 | −0.461 | −1.561 |
| 2026-08-21 | −0.380 | −1.574 |
| **2026-08-24** | **−0.235** | **−1.488** |

The negative histogram has contracted by **93.5%** from its 08-05 trough. The recent pace of improvement is **+0.274 → +0.081 → +0.145** per session. At that rate, a **MACD/signal bullish crossover is likely within ~2–4 sessions** if the tape merely holds sideways.

**The critical caveat:** MACD is still **−1.488, below its −1.253 signal line, and below zero** (it crossed zero on **2026-08-11**). A signal crossover off a below-zero MACD is a **momentum-repair signal, not a trend signal**. It argues for "the decline is over," not "the advance has resumed." Traders who treat that crossover as a buy trigger without price confirmation are buying into a downtrend's echo.

### RSI: no edge, which is itself information
RSI fell from **71.65 (2026-07-17, overbought)** to a low of **40.22 (2026-08-12)**, bounced to **53.85 (2026-08-19)**, and has faded back to **48.23**.

Three observations:
1. **RSI never broke 30** during the entire post-07-31 decline. The correction was **orderly, not capitulative** — which is consistent with distribution rather than panic, and means no washout low has been registered.
2. The **53.85 → 48.23 fade** over three sessions (08-19 to 08-24) shows the bounce **lost momentum before reaching 60**. Bulls have not taken control.
3. At 48.23, RSI is a **coin flip**. There is no oversold bounce trade and no overbought fade trade available.

---

## 6. Volatility & Volume: Compression Into a Squeeze

### Volatility is collapsing — resolution is being set up
- **ATR: 9.87 (2026-07-31) → 8.96 (08-07) → 7.86 (08-14) → 7.37 (2026-08-24)**, the lowest reading since 2026-06-25 (7.88). That is a **−25% contraction in 17 sessions**.
- **Bollinger bandwidth: 20.34% (07-24) → 16.21% (08-12) → 14.14% (2026-08-24).** The upper band has fallen from **346.02 (08-07)** to **335.14**, while the lower band has *risen* from **289.77 (08-20)** to **290.88**. Both bands converging on a falling midline (324.37 → 313.01) = textbook coil.
- Price is at **%b = 0.44** — the lower-middle of the band, with **no proximity to either extreme**.

Compressed ATR + compressed bandwidth after a 7% shock means **the market is loading a directional move**. It does **not** tell us the direction. That is precisely why the level map in §7 matters more than the momentum readings.

### Volume: drying up — constructive and cautionary simultaneously
| Date | Close | Volume |
|---|---|---|
| 2026-07-31 | 308.91 | **132,489,100** (shock) |
| 2026-08-18 | 310.03 | 53,424,500 |
| 2026-08-19 | 316.83 | 50,505,600 |
| 2026-08-20 | 311.30 | 40,959,200 |
| 2026-08-21 | 309.35 | 46,876,800 |
| **2026-08-24** | **310.34** | **34,673,600** |

The 10-session average volume is ~41M versus 68–75M in the first week of August. **Volume has roughly halved.**

- **Bullish read:** selling pressure is exhausting; no further distribution is occurring; VWMA has stopped falling (**307.76 → 308.41 → 308.80 → 309.15** over four sessions) after collapsing from **329.58 (07-30)**. Flattening VWMA = the volume-weighted holder has stopped losing ground.
- **Bearish read:** **declining volume on an attempted rally** (08-19's +4.82% run from 302.25 came on 50.5M, *below* the 07-31 shock but not expansionary) is the classic absence of accumulation. Price is only **+0.39% above VWMA (309.15)** — barely profitable for the average buyer. If that flips, the marginal holder is underwater and becomes supply.

**Net:** the low-volume drift is neutral-to-mildly-constructive, but it is **not confirmation**. A breakout must arrive with volume expansion (>50M, ideally >60M) to be trusted.

---

## 7. The Level Map (all levels derived from verified OHLC rows)

### Overhead — layered, and the reason the 08-19/08-20 rally failed
| Level | Price | Derivation |
|---|---|---|
| **Gap bottom / 50-SMA** | **310.50 – 310.69** | 50-SMA 310.50; 2026-07-31 high 310.69 |
| 10-EMA | 310.35 | Immediate pivot, price at it |
| Intraday capping | 313.36 | 2026-08-24 high |
| **Bounce high / first resistance** | **316.83 – 319.28** | 2026-08-19 close 316.83, high 319.28 |
| **Failed 50% retrace** | **320.04 – 320.28** | 50% of 340.08→300.00 = 320.04; 2026-08-20 high **320.28** — tagged and rejected, closed 311.30 |
| 61.8% retrace | 324.77 | Of the 07-28→07-31 range |
| **Unfilled gap / supply** | **329.59 – 333.43** | 2026-07-30 low 329.59; 2026-07-30 close 333.43 |
| Bull invalidation target | 340.08 | 2026-07-28 record close |
| Bollinger Upper | 335.14 | 2σ above 20-SMA |

**The single most important bearish evidence in this report:** on **2026-08-20** the stock printed a high of **320.28** — essentially the exact 50% retracement of the crash (320.04) — and closed **311.30 (−1.75%)**. That is a **precise rejection at the midpoint of the breakdown leg**, and it is where supply has declared itself.

### Downside — a real, multi-tested floor
| Level | Price | Derivation |
|---|---|---|
| VWMA | 309.15 | Volume-weighted cost basis; must hold |
| Prior lows | 307.01 | 2026-08-21 low |
| First support shelf | 304.30 – 305.74 | 2026-08-14 low 304.30; 2026-08-18 low 305.74 |
| **Tested floor** | **300.57 – 302.94** | 2026-08-12 low 300.57; 2026-08-03 low 302.56; 2026-08-04 low 301.32; 2026-08-17 low 302.94 |
| **Line in the sand** | **300.00** | 2026-07-31 crash low — the origin of the entire range |
| Bollinger Lower | 290.88 | 2σ below 20-SMA |
| Strategic support | 281.70 | 200-SMA (currently −9.2% away) |

The **300.00–302.94 zone has absorbed four separate tests** (08-03, 08-04, 08-12, 08-17) without a close beneath it. That is genuine absorption, and it is where the structural stop belongs.

**Range definition:** AAPL has spent 17 sessions boxed between **300.00 and 320.28** — a **6.8% range**. Price at 310.34 sits almost exactly at the midpoint (310.14). The market is **perfectly balanced**.

---

## 8. Actionable Playbook

### Scenario A — Bullish resolution (needs confirmation)
**Trigger:** Daily close **above 316.83** (08-19 close), with volume **> 55M**, ideally accompanied by the MACD/signal crossover.
**Why it would matter:** reclaiming 316.83 puts price above the 50-SMA, above VWMA, above the 10-EMA, and inside the gap — flipping the median cost basis from resistance to support.
**Path:** 320.04 (50% retrace) → **329.59–333.43** (gap fill). A full gap fill implies roughly **+6.2% to +7.5%** from 310.34.
**Invalidation of the bullish case:** a close back below **309.15 (VWMA)** after the breakout.

### Scenario B — Bearish resolution
**Trigger:** Daily close **below 300.57**, decisively below the **300.00** crash low on **expanding** volume.
**Why it would matter:** it would break the four-times-tested floor and confirm the 07-31 gap as a genuine structural break rather than an overreaction. The 50-SMA would then be rolling over with price beneath it.
**Path:** **290.88** (Bollinger lower) is the first objective, roughly **−6.3%** from 310.34. The 200-SMA at 281.70 is a strategic magnet, **−9.2%** away, but would require sustained deterioration.

### Scenario C — Continued coil (highest-probability near-term, given compressed ATR)
**Range:** 302.94 – 320.28.
**Trade construction:** buy the 302–305 shelf / sell the 316–320 zone, **only** with Bollinger band or ATR extremes as a filter, and **only with small size** — because bandwidth at 14.1% and ATR at 7.37 mean the range is narrow relative to the cost of a stop.

### Risk management (ATR-calibrated)
- ATR = **7.37 (2.38% of price)**. Do **not** reuse July-era stop distances; volatility is 25% lower.
- **Swing long from ~311:** a 1.5× ATR stop sits near **300.0** (−3.5%), conveniently aligned with the structural floor. Risk ≈ **$11/share**; size positions off that, not off a fixed dollar amount.
- **Breakout long above 316.83:** stop at **2× ATR ≈ 302.1**, or tighter at **309.15 (VWMA)** for a higher-probability-but-wider-stop trade-off.
- **Short below 300:** stop back above **310.50 (50-SMA)**, risk ≈ 3.5%.
- Expected daily drift is only ~2.4%; taking profits at 1× ATR (7.4 pts) from entry is a reasonable discipline inside the range.

---

## 9. Nuances, Tensions, and Honest Limitations

1. **The indicator set is internally contradictory — by design.** Trend (200-SMA, rising) says buy; momentum regime (MACD < 0, price < 50-SMA and < Bollinger mid) says the trend has paused; momentum *rate of change* (histogram +93.5%, flattening VWMA) says the pause is ending; RSI says no edge. **The honest conclusion is that the direction of the squeeze's resolution is unresolved.** A trader acting on any single indicator here is over-reading noise.
2. **A below-zero MACD crossover ≠ a buy signal.** If the crossover fires in the next 2–4 sessions while MACD remains near −1.5, treat it as permission to *stop being bearish*, not as permission to be aggressively long.
3. **The 320.28 rejection is the strongest single piece of evidence in the dataset.** Any bullish thesis must explain why that rejection fails on the second attempt. The answer must involve **volume** — the 08-19 attempt came on 50.5M while the 07-31 distribution came on 132.5M. Until volume expands, the short side has the better evidence at 316–320.
4. **No RSI divergence.** I looked specifically for a bullish divergence at the 08-12 low and did not find a clean one — RSI made a low of 40.22 vs the 06-25 low of 32.20 while price made a *higher* low. That is a mild positive, but it is not a validated divergence pattern and I am not claiming one.
5. **The 06-25 precedent is a fact, not a template.** The 06-25 shock (−6.11% on 107M) recovered fully by 07-28. Similar setup ≠ similar outcome; I am flagging the ambiguity, not predicting a repeat.
6. **Volume figures around 2026-06-26 (261,775,500) are an outlier** — an order of magnitude above normal, consistent with an index/rebalance event. I excluded it from all average-volume reasoning so it does not distort the "volume is drying up" conclusion.
7. **Data window constraint:** the price history begins 2025-12-01. The "200-SMA at 281.70" is a valid computation on available rows, but I cannot verify behavior beyond this window, and I have made no claims about levels outside it.
8. **No fundamental or macro input** is available from these tools. The 07-31 gap is unexplained by the data — earnings, guidance, or a sector event would all be consistent with a −7.35% gap on 132M shares. Anyone trading this should identify the catalyst before committing directionally.

---

## 10. Summary Table

| Dimension | Verdict | Key Evidence (verified 2026-08-24) |
|---|---|---|
| **Long-term trend** | **Bullish, intact** | 200-SMA rising 253.92 (04-27) → **281.70**; price **+10.17%** above it |
| **Medium-term trend** | **Stalled / flattening** | 50-SMA flat at **310.50**; price **$0.16 below** it; peaked 309.79 on 08-07, dipped to 309.08 on 08-17 |
| **Short-term trend** | **Neutral equilibrium** | 10-EMA **310.35** ≈ close 310.34; 13-session slide in the EMA has stopped |
| **Momentum regime** | **Bearish but repairing** | MACD **−1.488** < signal **−1.253**, below zero since 08-11 |
| **Momentum velocity** | **Constructive** | Histogram **−3.634 (08-05) → −0.235 (08-24)**; 13 up-sessions; crossover likely 2–4 sessions |
| **Overbought/oversold** | **No edge** | RSI **48.23**; never broke 30 during the decline; failed at 53.85 on 08-19 |
| **Volatility** | **Compressing → squeeze** | ATR **9.87 → 7.37**; Bollinger bandwidth **20.34% → 14.14%**; %b = 0.44 |
| **Volume** | **Drying up (ambiguous)** | 08-24: **34.67M** vs 07-31 shock **132.49M**; 10-day avg ~41M |
| **Volume-weighted cost** | **Mildly constructive** | VWMA **309.15**, flattening 4 sessions; price **+0.39%** above |
| **Range** | **300.00 – 320.28** (17 sessions) | Price at midpoint 310.14 |
| **Key resistance** | **316.83 → 320.04 → 329.59–333.43** | 08-20 high **320.28** = exact 50% retrace; supply rejection closed 311.30 |
| **Key support** | **309.15 → 302.94 → 300.00** | 300.00–302.94 tested four times (08-03, 08-04, 08-12, 08-17) |
| **Bull trigger** | Close **>316.83** on **>55M** volume | Opens 320.04, then gap fill to 329.59–333.43 (+6.2% to +7.5%) |
| **Bear trigger** | Close **<300.57**, ideally <300.00 | Opens 290.88 (−6.3%), then 200-SMA 281.70 (−9.2%) |
| **Risk unit** | **ATR 7.37 = 2.38%** | 1.5× ATR stop ≈ $11; align with 300.0 floor for longs from ~311 |
| **Bottom line (AAPL)** | **Neutral / coiled. Do not chase. Wait for a volume-confirmed break of 316.83 or 300.57.** | Trend intact long-term, but medium-term unresolved; the 08-20 rejection at 320.28 gives the short side the edge at 316–320 until volume proves otherwise |