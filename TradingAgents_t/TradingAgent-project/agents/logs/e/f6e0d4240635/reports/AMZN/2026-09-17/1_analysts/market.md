# AMZN — Multi-Timeframe Technical Report
**As of:** 2026-09-17 (Thursday close) · **Last price:** $251.19

---

## 1. Data Integrity Check

I pulled the full 252-session OHLCV history (2025-09-17 → 2026-09-17) and the verified snapshot for 2026-09-17. **No discrepancies found.** The snapshot's latest row matches the raw CSV exactly:

| Field | Verified value |
|---|---|
| Open | 251.07 |
| High | 252.73 |
| Low | 249.24 |
| Close | **251.19** |
| Volume | 30,438,800 |
| 50 SMA | 255.7064 |
| 200 SMA | 240.2016 |
| 10 EMA | 252.7308 |
| MACD / Signal / Hist | −2.2863 / −1.0200 / −1.2662 |
| RSI (14) | 45.3945 |
| Bollinger (20,2) mid / upper / lower | 256.4535 / 266.2868 / 246.6202 |
| ATR (14) | 6.1742 |
| VWMA | 255.2109 |

All figures below are drawn from these two tool outputs. Derived percentages are simple arithmetic on those verified closes.

---

## 2. Executive Summary — The Verdict

**Primary trend: UP. Intermediate trend: CORRECTING. Short-term trend: DOWN, with the first tentative stabilization signal on 2026-09-17.**

AMZN is in a classic **post-earnings-gap digestion phase**. The stock gapped violently higher on 2026-07-31 (Jul 30 close 235.50 → Jul 31 close 271.58, **+15.32%**, on 129.05M shares), peaked at a close of **284.02 on 2026-08-03** (intraday 287.20), and has since bled lower in a well-ordered staircase of lower highs and lower lows. The 2026-09-16 close of **245.96** was the lowest close since 2026-07-29 — i.e., the entire post-earnings advance from the gap-day low (262.01) has now been fully retraced, and price is sitting roughly 41% of the way down into the unfilled gap zone (235.50 → 262.01).

**However**, the *structural* bull case is intact:
- The **200 SMA at 240.20 is rising** (+1.52 points over the last 14 sessions, ~+0.11/day), and price is still **+4.57% above it**.
- The **50 SMA (255.71) sits +6.46% above the 200 SMA**, and that spread has remained positive across the entire 90-session window I examined.
- Rebound day 2026-09-17 closed at 251.19, **+2.13% off the prior close**, with a higher low (249.24 vs 244.30).

**Net:** This is a *pullback inside an uptrend*, not a trend reversal — but the short-term tape is still bearish and the bounce is unconfirmed. I would not call a bottom until AMZN closes back above the **255.2–256.5 cluster** (VWMA 255.21 / 50 SMA 255.71 / Bollinger mid 256.45).

---

## 3. Trend Structure

### 3.1 Long-Term (200 SMA) — Intact and Rising
- 200 SMA: **240.2016**, up from 238.6797 on 2026-08-28 and 232.8377 on 2026-06-22.
- Price sits **+4.57%** above it. The 200 SMA has not been tested on a closing basis since the February 2026 bottoming sequence (closing low 198.79 on 2026-02-13), and it has been climbing monotonically for four straight months.
- This is the single most important line on the chart: a daily close below ~240 would convert the current "pullback" into a structural trend break.

### 3.2 Medium-Term (50 SMA) — Rising, But Now Acting as Resistance
- 50 SMA: **255.7064**, up from 246.3842 on 2026-07-30 — a sharp upward inflection caused by the earnings gap rolling through the lookback window. It is currently rising roughly **+0.2 points per session** (252.41 on 2026-09-01 → 255.71 on 2026-09-17).
- Price is **−1.77% below** it. Because the 50 SMA is still rising while price stagnates, **the distance to reclaim is widening, not shrinking** — a genuine headwind. A flat price through month-end would leave the 50 SMA near ~258, requiring a larger rally to repair the chart.
- 50 SMA > 200 SMA (+6.46%) keeps the golden-cross structure valid, but the *price*-vs-50 SMA relationship is the bearish component.

### 3.3 Short-Term (10 EMA) — Downtrend Decelerating
- 10 EMA: **252.7308**, down from a peak of 267.1837 on 2026-08-12. Price is **−0.61% below** it.
- Critically, the 10 EMA's **slope is flattening**: 256.0393 (09-14) → 254.6540 (09-15) → 253.0732 (09-16) → 252.7308 (09-17). Each daily decline is smaller than the last. That is the mechanical signature of downside momentum exhausting.
- 10 EMA < 50 SMA confirms the short-term trend is still down; 10 EMA >> 200 SMA confirms it is a counter-trend dip, not a bear regime.

### 3.4 Swing Sequence — A Textbook Descending Channel

| Swing highs (close basis) | Swing lows (intraday) |
|---|---|
| 284.02 — 2026-08-03 | 262.01 — 2026-07-31 |
| 278.09 — 2026-08-10 | 267.10 — 2026-08-12 |
| 265.84 — 2026-08-19 | 258.34 — 2026-08-17 |
| 266.43 — 2026-08-28 *(minor exception)* | 255.02 — 2026-08-27 |
| 258.90 — 2026-09-03 | 251.93 — 2026-09-01 |
| 256.78 — 2026-09-11 | **244.30 — 2026-09-16** |
| 255.95 — 2026-09-14 | 249.24 — 2026-09-17 *(higher low)* |

The sequence of lower highs is unbroken on closes (with one marginal 0.6-point overshoot on 2026-08-28), and the sequence of lower lows was strictly unbroken until 2026-09-17 printed **249.24**, the first higher low since the decline began. That is a one-day signal, not a trend change — but it is the first piece of evidence supporting the long side.

---

## 4. Momentum

### 4.1 MACD — Bearish, But the Histogram Is Rolling Over
- MACD line: **−2.2863**; signal: **−1.0200**; histogram: **−1.2662**.
- The MACD line peaked at **+8.4324 on 2026-08-11** and has fallen monotonically since. It **crossed below zero on 2026-09-09** (from +0.1182 on 09-08 to −0.4208) — a standard trend-following sell trigger.
- The MACD line crossed below its signal back on **2026-08-17** (histogram −0.3097) and has stayed negative for 22 consecutive sessions.
- **The nuance that matters:** the histogram has stopped making lower lows. It bottomed at −1.6831 on 2026-08-27, improved to −1.1800 by 2026-09-04, and after oscillating near −1.1 to −1.5 has ticked **up from −1.5387 (09-16) to −1.2662 (09-17)**. That is early downside-momentum exhaustion — the first necessary (not sufficient) condition for a low.
- Watch for a histogram contraction toward zero followed by a MACD/signal bull cross; that would be the confirmation trigger around/above the 255–256 zone.

### 4.2 RSI — Neutral-Low, No Washout
- RSI (14): **45.3945**, up from **39.4467 on 2026-09-16** and 41.4171 on 2026-09-15.
- RSI peaked at **72.2316 on 2026-08-03** — a genuine overbought reading at the exact price top (close 284.02). That is a clean, tool-supported peak-timing coincidence.
- Since 2026-08-11, RSI has **not once exceeded 60** (best reading: 55.85 on 08-28). That persistent inability to regain the momentum midline is the clearest evidence of distribution rather than accumulation.
- **Important caveat:** RSI bottomed at ~39.4, never reaching the 30 oversold threshold. The pullback therefore has *not* produced a washout. Historically that means either (a) the correction needs more time/price, or (b) this is a shallow, trend-continuation dip. RSI 45 leaves room in both directions — no edge from this indicator alone.
- Note the 08-03 top (RSI 72.2) vs the 08-10 lower close high (278.09, RSI 65.9): consistent with fading momentum, though not a formal price-higher/RSI-lower divergence since price never exceeded 284.02.

---

## 5. Volatility and Bollinger Structure

- **ATR (14): 6.1742**, equal to **2.46% of price**. ATR has compressed persistently from **9.9478 on 2026-08-03** to today — a ~38% contraction in realized volatility.
- This is classic post-gap volatility collapse: the market has absorbed the earnings information and the daily ranges are narrowing. Volatility compression is direction-neutral but **precedes expansion**, so a range resolution is likely within the next 2–4 weeks.
- Bollinger (20,2): mid **256.4535**, upper **266.2868**, lower **246.6202**. Bandwidth = **7.67% of the midline** — a moderately tight envelope that is still narrowing.
- Price at 251.19 is:
  - **−2.05% below** the midline (bearish bias)
  - **+1.85% above** the lower band (not oversold)
  - **−5.67% below** the upper band
- **The 2026-09-16 close of 245.96 was below the *current* lower band (246.62)** and the 2026-09-17 close snapped back inside the envelope. A one-day band pierce followed by an inside close, combined with a higher low, is a mild mean-reversion buy signal — but with a single session of confirmation it is exactly that: mild.

---

## 6. Volume and Participation

- **VWMA: 255.2109**, and price is **−1.58% below it**. The volume-weighted average transaction price of the recent window sits *above* the current price, meaning the marginal recent buyer is underwater. Declining VWMA (272.05 on 2026-08-20 → 255.21 today) alongside declining price is textbook **distribution / lack of bid**.
- The VWMA also completes a **resistance cluster at 255.2–256.5**: VWMA 255.21, 50 SMA 255.71, Bollinger mid 256.45. Three independent methods converge within 1.25 points. That is the level that matters.
- **Volume character during the pullback has been benign, not panicked:** the last 20 sessions average ~31.67M shares; 2026-09-17 traded 30.44M (~96% of that average). There has been no high-volume capitulation day since the gap. That argues against a violent flush lower and supports a grind/consolidation resolution.
- **Volume caveat on the bounce:** the 2026-09-17 up day (30.44M) traded *lighter* than the 2026-09-16 down day (33.49M). Up-day volume below down-day volume is a weak-quality rally — a reason not to chase the bounce.
- **Event-risk calibration:** the two largest volume prints in the 252-session file are 2026-02-06 (179.21M, close −5.55% from 222.69 to 210.32, intraday −10.05%) and 2026-07-31 (129.05M, +15.32%). AMZN's earnings gaps dwarf its 2.46% ATR. Any position held through a report is an event trade, not a technical trade — size accordingly.

---

## 7. Key Levels (All Derived from Tool-Supplied Prices)

| Level | Price | Source | Significance |
|---|---|---|---|
| Resistance 5 | 266.29–267.56 | Boll upper 266.2868; 2026-08-28 high 267.56 | Range top / target zone |
| Resistance 4 | 258.90–261.12 | 2026-09-03 close 258.90; 2026-09-04 high 261.12 | Prior breakdown shelf |
| **Resistance 3 (pivot)** | **255.21–256.45** | VWMA 255.2109 / 50 SMA 255.7064 / Boll mid 256.4535 | **Bull/bear line. Reclaim = trend repair** |
| Resistance 2 | 252.73 | 10 EMA | Immediate intraday resistance |
| Resistance 1 | 252.73 (session high) | 2026-09-17 high 252.73 | Today's high — coincident with 10 EMA |
| **Spot** | **251.19** | 2026-09-17 close | — |
| Support 1 | 249.24 | 2026-09-17 low | First higher low |
| Support 2 | 247.22 | 2026-09-15 low | Shelf |
| Support 3 | 246.62 | Boll lower band | Envelope floor |
| **Support 4 (critical)** | **244.30** | 2026-09-16 low | Swing low; break = downtrend extension |
| Support 5 | 240.20 | 200 SMA | **Structural bull/bear line** |
| Support 6 | 235.50–238.0 | 2026-07-30 close / gap origin | Gap-fill completion zone |

---

## 8. Scenarios and Triggers

**Base case (≈45% subjective odds) — Range consolidation 244–262.** ATR compression, mixed momentum, and converging moving averages point to a 2–4 week base. Trade the edges, not the middle. The most likely path is a retest of 246–249 followed by another attempt at 255–257.

**Bullish repair (≈30%) — Reclaim of 256.5 on volume.** Requires a daily close above 256.45 (Bollinger mid) with volume > 35M (above the ~31.7M 20-day average). Confirmation sequence: MACD histogram turns positive, RSI pushes above 55, VWMA flattens. Targets 258.90 → 266.29 → 267.56. A close above 267.56 breaks the sequence of lower highs and reopens the 278–284 zone.

**Bearish continuation (≈25%) — Loss of 244.30.** A daily close under 244.30 targets the 200 SMA at 240.20, then the 235.50 gap origin. A close below 240.20 would be the first structural break since early 2026 and would flip the medium-term bias to neutral/bearish, with 232–234 (the June 2026 congestion) as the next reference.

**Invalidation of the bearish short-term case:** two consecutive closes above 256.5 with expanding volume.

---

## 9. Actionable Plans

### A. Confirmation Long (preferred)
- **Trigger:** daily close > **256.50**, volume > 35M
- **Stop:** **246.90** (below the 2026-09-15 low 247.22, ~1.6 ATR)
- **Targets:** T1 266.29 (Boll upper) = **+0.9R**; T2 267.56 = **+1.1R**; T3 278.09 (2026-08-10 close) = **+2.1R**
- **Read:** Honest assessment — the first two targets offer poor R:R because the stop is wide relative to the nearby resistance. This setup only earns its keep if you hold a partial for the 278 retest. Better risk-adjusted alternative: **take T1 on half and trail the remainder with a 1.5-ATR (≈9.3 pt) stop.**

### B. Mean-Reversion Long at Support (better R:R, lower probability of fill)
- **Trigger:** limit near **246.50–247.50** (Boll lower band 246.62 / 2026-09-15 low 247.22) with a reversal candle
- **Stop:** **243.50** (below the 2026-09-16 low 244.30)
- **Target:** 255.20–256.45 cluster = **+2.7 to +3.0R**
- **Invalidation:** any close below 244.30 before fill — stand down and switch to Plan D.

### C. Counter-Trend Fade at the Cluster (tactical, small size)
- **Trigger:** rejection candle in **255.70–257.60** (50 SMA 255.71 / Sep 11 high 257.59) with RSI failing to exceed 55
- **Stop:** **259.60** (above the 2026-09-03 close 258.90)
- **Targets:** 246.62 (Boll lower) = **+2.3R**; 244.30 = **+2.9R**
- **Caveat:** this is shorting into a rising 200 SMA with 50 SMA > 200 SMA. It is a tactical trade only — half normal size, and take profits rather than holding for a breakdown.

### D. Breakdown Short
- **Trigger:** daily close < **244.30**
- **Stop:** **248.60** (back above the 2026-09-15 low)
- **Targets:** 240.20 (200 SMA) = **+1.0R**; 235.50 = **+2.1R**

### Risk Sizing Notes
- ATR 6.17 = 2.46% of price. With a 1% account risk budget, position size = 1% ÷ (stop distance %) — e.g., Plan A's 3.8% stop implies ~26% of a full position per 1% risk unit.
- **Do not size off ATR into an earnings date.** The 2026-07-31 gap was +15.32% and the 2026-02-06 gap was −5.55% (−10.05% intraday). Use half or less of ATR-implied size if a report falls inside the holding period.

---

## 10. What Would Change My View

| To Bullish | To Bearish |
|---|---|
| Two closes > 256.45 with volume > 35M | Close < 244.30 |
| MACD histogram turns positive | MACD line < −3.0 with histogram re-expanding |
| RSI > 55 and holding | RSI < 35 with price making lower lows |
| 10 EMA turns up and price holds above VWMA | VWMA rolls decisively under the 50 SMA |
| Close > 267.56 (breaks lower-high sequence) | Close < 240.20 (200 SMA) |

---

## 11. Why These Eight Indicators

| Indicator | Why it earns a slot |
|---|---|
| **close_200_sma** | The only line separating a correction from a bear market; and it is *rising*, which is the core of the bull case |
| **close_50_sma** | The intermediate trend and, at 255.71, actual overhead resistance — the pivot of the whole setup |
| **close_10_ema** | Detects the short-term slope change (flattening since 09-14) that longer averages cannot show |
| **macd** | Confirms the 09-09 zero-line cross and dates the momentum regime change |
| **macdh** | The single most useful leading tell right now — contraction from −1.68 to −1.27 while price made new lows |
| **rsi** | Independent momentum scale; establishes that the 08-03 top was genuinely overbought and that no washout has occurred |
| **atr** | Sizes every stop/target and quantifies the 38% volatility compression that signals an impending range resolution |
| **vwma** | Adds volume-weighted conviction; at 255.21 it confirms the resistance cluster *and* shows recent buyers are underwater |

**Deliberately omitted:** Bollinger upper/lower bands were *not* selected as separate indicator calls (their verified values are quoted from the snapshot for context) because the 20-SMA midline largely duplicates the 50 SMA's resistance message. I also skipped MFI/stochastic-style oscillators — they would be redundant with RSI in an environment where the key question is trend repair, not oscillator divergence.

---

## 12. Summary Table

| Dimension | Reading (2026-09-17) | Interpretation | Actionable Implication |
|---|---|---|---|
| **Close** | 251.19 (+2.13% d/d) | Rebound after 4.21% 3-session drop | Bounce, not yet a reversal |
| **Primary trend (200 SMA)** | 240.2016, rising; price +4.57% above | Bullish, intact | Structural longs valid ≥240 |
| **Intermediate (50 SMA)** | 255.7064, rising; price −1.77% below | Resistance overhead | 255.71 is the pivot |
| **Short-term (10 EMA)** | 252.7308; price −0.61% below; slope flattening | Downtrend decelerating | Watch for 10 EMA reclaim |
| **MACD** | −2.2863 / signal −1.0200 / hist −1.2662 | Bearish regime, momentum fading | Zero-line cross 09-09 remains in force |
| **RSI** | 45.3945 (from 39.4467) | Neutral-low, no washout | No edge; needs >55 to confirm |
| **Bollinger** | Mid 256.4535 / UB 266.2868 / LB 246.6202 (width 7.67%) | Compressing range; price below mid | 246.6–256.5 is the operative box |
| **ATR** | 6.1742 (2.46% of price), down from 9.9478 | Volatility contraction | Expect expansion; size stops off ATR |
| **VWMA** | 255.2109; price −1.58% below | Recent buyers underwater | Confirms 255–256 supply |
| **Volume** | 30.44M vs ~31.67M 20-day avg; up-day < prior down-day | Weak-quality bounce | Demand volume > 35M to trust a breakout |
| **Swing structure** | Lower highs 284.02→255.95; lower lows 267.10→244.30, first higher low 249.24 | Downtrend with a nascent bottoming attempt | 244.30 = invalidation; 256.5 = repair |
| **Base case (45%)** | 244–262 consolidation | Post-gap digestion | Trade the edges |
| **Bull case (30%)** | Close > 256.5 on volume | Trend repair | Targets 258.90 / 266.29 / 267.56 |
| **Bear case (25%)** | Close < 244.30 | Downtrend extension | Targets 240.20 / 235.50 |
| **Preferred trade** | Confirmation long > 256.50, stop 246.90 | Better R:R at 246.5–247.5 support, stop 243.50 | Do not chase the 09-17 bounce |

**Bottom line:** AMZN is a bull-market pullback that has not yet finished proving itself. The evidence — rising 200 SMA, 50 > 200, MACD histogram contracting, ATR compressing, first higher low — argues for patience rather than panic. But price below the 10 EMA, 50 SMA, VWMA, and Bollinger midline, combined with a sub-60 RSI ceiling since 2026-08-11 and a lighter-volume bounce, means the burden of proof sits with the buyers. **Let 256.5 print before turning constructive; let 244.3 break before turning outright bearish.**