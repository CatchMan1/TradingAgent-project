# AAPL — Technical Analysis Report, as of 2026-10-01

## 1. Bottom line

AAPL (Apple Inc.) closed at **330.32** on 2026-10-01, roughly **3.2% below its 52-week closing high of 341.07 (2026-09-25)** and **4.3% below the 52-week intraday high of 345.34 (2026-09-22)**. The dominant structure is still a **rising intermediate/long-term uptrend** (price > 50 SMA > 200 SMA, both averages sloping up), but the **short-term tape has rolled into a corrective phase**: price is below its 10 EMA (333.70), below its 20-day Bollinger mid-band (331.62), below VWMA (335.30), and MACD has just printed a bearish signal-line crossover (histogram negative since 2026-09-29).

This is best classified as **a healthy pullback inside an intact uptrend, not yet a trend break** — the pullback has occurred on *declining* volume, ATR has been compressing, and RSI at 51.4 is neutral rather than broken. The tactical problem is that price is sitting in a **no-man's zone** (331–336) where the short-term averages are overhead resistance while the 50 SMA (322.18) sits 2.5% below. The decision point is clean: **reclaim 333.70–335.30 = continuation; lose 322.18 = deeper correction toward 316.8–310.**

---

## 2. Verified data baseline (source of truth)

Per `get_verified_market_snapshot` for 2026-10-01 (identical to the final row of the OHLCV pull — **no discrepancy to flag**):

| Field | Value |
|---|---|
| Open / High / Low / Close | 330.00 / 332.48 / 325.81 / **330.32** |
| Volume | 36,306,300 |
| 10 EMA | 333.6998 |
| 50 SMA | 322.1756 |
| 200 SMA | 288.8607 |
| MACD / Signal / Histogram | 4.0834 / 5.0733 / **−0.9900** |
| RSI(14) | 51.4331 |
| Bollinger mid / upper / lower | 331.6210 / 346.4133 / 316.8287 |
| ATR(14) | 7.2515 |
| VWMA | 335.3003 |

Derived arithmetic from these values: price is **−1.01% vs 10 EMA**, **+2.53% vs 50 SMA**, **+14.35% vs 200 SMA**, **−1.49% vs VWMA**, **−0.39% vs Bollinger mid**, **−4.87% below the upper band**, **+4.08% above the lower band**. ATR equals **2.20% of price**; Bollinger bandwidth is **29.58 points = 8.92% of the mid-band**.

---

## 3. Trend structure across three timeframes

**Long-term (200 SMA) — bullish and improving.**
The 200 SMA has risen every session in the window: **278.24 (2026-08-03) → 288.86 (2026-10-01)**, a slope of roughly **+0.26 points/session**. Price is 14.35% above it. The 50 SMA sits 11.5% above the 200 SMA, and that spread has *widened* slightly over the last two months (309.52 − 278.24 = 31.28 on 2026-08-03 vs 322.18 − 288.86 = 33.31 on 2026-10-01). A widening 50/200 spread indicates the golden-cross structure is strengthening, not maturing into a flattening top.

**Intermediate (50 SMA) — bullish, steady, and now the key line in the sand.**
The 50 SMA has advanced monotonically from **309.52 (2026-08-03) to 322.18 (2026-10-01)**, i.e. roughly **+0.31 points/session**, with no inflections. On 2026-09-25 price closed at 341.07, **6.0% above** the then-50 SMA (321.83); today that extension has compressed to **2.5%**. That compression is exactly what a normal mean-reversion pullback looks like — it relieves extension without damaging structure.

**Short-term (10 EMA) — bearish flip.**
The 10 EMA rose from **309.46 (2026-08-14) to a peak of 335.96 (2026-09-28)**, then turned down to 333.70. Price closed **below** it on 2026-09-29 (close 329.40 vs EMA 334.77), the first such close since 2026-09-09, and has stayed below for three consecutive sessions. The 10 EMA is now declining (−2.26 points from its 9/28 peak), confirming a short-term momentum shift.

**Event risk embedded in the tape.** This name has produced repeated single-session air pockets in the observed window, all verifiable from the OHLCV rows:
- 2026-02-12: 275.50 → **261.73 (−5.00%)**
- 2026-06-25: 293.08 → **275.15 (−6.12%)** on 107.0M shares
- 2026-07-31: 333.43 → **308.91 (−7.36%)**, opening at 304.81 (−8.58% gap) on 132.5M shares

Any stop-loss plan based on ATR alone will not protect against this magnitude of overnight gap. That is a structural risk-management fact of this instrument, not a prediction.

---

## 4. Indicator-by-indicator read (the eight selected)

### 4.1 close_10_ema — 333.70 (price below, −1.01%)
Short-term momentum has flipped from tailwind to headwind. The relevant sequence: price was above the 10 EMA continuously from 2026-09-10 through 2026-09-28, and lost it on 2026-09-29. **Reclaiming 333.70 on a closing basis is the first requirement for any bullish re-engagement.**

### 4.2 close_50_sma — 322.18 (price above, +2.53%)
The primary trend filter and the most important level on the chart right now. Rising at ~0.31/day, it is a moving objective rather than a fixed floor: by 2026-10-09 it would be near ~324.6 if the slope holds. A close below it would be the first intermediate-term warning since the spring.

### 4.3 close_200_sma — 288.86 (price above, +14.35%)
Strategic bull market benchmark. Rising steadily, no death-cross threat (50 SMA is 11.5% above it). This is not the operative risk level for a swing trade; it is the confirmation that the *strategic* bias remains long.

### 4.4 macd — 4.083 (positive, but falling from 6.248 on 2026-09-22)
Still above zero, so the intermediate momentum regime is positive. But it has rolled over for six consecutive sessions and is decelerating at roughly 0.3–0.6 points/day. At that pace, a **zero-line test** is plausible within roughly two to three weeks. A zero-line break would mark a genuine regime change, not just a pullback.

### 4.5 macds — 5.073 (MACD crossed below signal)
The crossover occurred on **2026-09-29** (histogram −0.283), and the gap has widened to **−0.990** today. Importantly, this was *preceded* by a momentum divergence: the histogram peak was **+2.028 on 2026-09-03** (close 328.21) but only **+1.686 on 2026-09-17** and **+0.803 on 2026-09-25** (close 341.07) — price made a materially higher high (341.07 vs 328.21) while the histogram made a lower high. Momentum was already fading before price rolled over. That is a textbook warning sequence, and it argues the current pullback has more basis than a one-day headline flush.

### 4.6 rsi — 51.43 (neutral; was 66.88 on 2026-09-22)
A fast, orderly unwind: **66.88 (9/22) → 61.32 (9/24) → 65.67 (9/25) → 61.79 (9/28) → 50.88 (9/29) → 51.43 (10/1)**. Two things matter here:
1. RSI **never reached 70** during the September advance (peak 66.88), so there is no classic overbought exhaustion to work off. This supports the "digestion" interpretation.
2. At 51.43, RSI has roughly **20 points of downside room to the 30 threshold** and 19 points of upside room to 70. It is a genuinely two-sided reading — a neutral zone, not a signal.

### 4.7 atr — 7.2515 (2.20% of price; declining)
ATR fell from **9.83 (2026-08-03) to 6.83 (2026-09-28)** before ticking up to 7.25. The September rally occurred *with falling ATR* — an orderly, low-chop advance rather than a volatile blow-off. Now ATR is stabilizing near the low end of its 2-month range.
**Risk-management translation:** 1× ATR ≈ 7.25 points; 1.5× ≈ 10.9 points (3.3%); 2× ≈ 14.5 points (4.4%).

### 4.8 vwma — 335.30 (price below, −1.49%)
This is the most actionable volume signal today. The volume-weighted cost basis of the recent window sits **above** spot, meaning the marginal buyer of the last several weeks is slightly underwater. VWMA rose from **307.76 (2026-08-19) to 335.34 (2026-09-30)** and has now **flattened** (335.34 → 335.30). Flattening VWMA plus price below it = buyers losing the initiative.
**Uses:** a reclaim of 335.30 with expanding volume is a high-quality long trigger; conversely, rallies that stall *at* 335.30 are shorts-into-strength setups within an uptrend.

### 4.9 Bollinger envelope (secondary cross-check, not counted in the core eight)
Snapshot: mid 331.62, upper 346.41, lower 316.83.
- **A squeeze resolved into a trend.** Bandwidth compressed to **15.43 points (≈5.0% of the mid-band) on 2026-08-27** (upper 317.04 / lower 301.61), then expanded to **33.50 points (≈10.2%) by 2026-09-25** (346.15 / 312.65). Price ran from 314.58 (8/27 close) to 341.07 (9/25 close) during that expansion — a classic squeeze-then-expansion.
- **Expansion is now contracting again:** 33.50 → **29.58 points (8.92%)**. Volatility is re-condensing, which typically precedes the next directional expansion. Direction is *not* yet determined by the bands; the trigger is a close outside 316.83 / 346.41, or more practically outside the nearer 322–336 decision range.
- Note the internal tension worth flagging: **ATR (14-day true range) is falling while Bollinger width (20-day standard deviation) expanded.** This is consistent with a persistent directional trend (price traveled far from its mean) combined with compressed daily ranges — not a contradiction, but it means ATR-based stops are currently *tighter* than band-based stops imply.

---

## 5. Volume and participation

- 2026-10-01 volume of **36.3M** is unremarkable and below the elevated prints during the September advance (**70.0M on 2026-09-10**, **50.7M on 2026-09-11**).
- The 2026-09-29 down day (−2.66%, close 329.40 from 338.40) traded **38.5M** — a *below-trend* decline. There is no volume climax to date on this pullback, which argues against institutional distribution.
- The standout volume anomaly is **86.6M on 2026-09-18** (close 336.13) — more than double any adjacent session. It sits inside the 331–341 congestion zone and represents a large block of supply that must be absorbed on any retest of the highs.
- **Interpretation:** the pullback is *so far* an absence-of-buyers move, not a rush-for-the-exits move. That is the single strongest argument for the constructive base case. It becomes a bear argument the moment a close below 322.18 arrives on >50M shares.

---

## 6. Key levels — all values traceable to tool output

| Level | Value | Source / basis | Role |
|---|---|---|---|
| Upper Bollinger | 346.41 | Snapshot 2026-10-01 | Outer resistance / volatility cap |
| 52-wk intraday high | 345.34 | 2026-09-22 high | Breakout target |
| 52-wk closing high | 341.07 | 2026-09-25 close | Prior high / resistance |
| VWMA | 335.30 | Tool output 2026-10-01 | Overhead supply / long trigger |
| 10 EMA | 333.70 | Tool output 2026-10-01 | First resistance |
| Bollinger mid | 331.62 | Snapshot 2026-10-01 | Immediate pivot |
| **Last close** | **330.32** | 2026-10-01 | — |
| **50 SMA** | **322.18** | Tool output 2026-10-01 | **Primary trend line** |
| Lower Bollinger | 316.83 | Snapshot 2026-10-01 | Volatility floor |
| Sept lows | 314.90 / 309.90 | 2026-09-08 / 2026-09-09 lows | Structure support |
| July gap floor | 304.81 / 300.00 | 2026-07-31 open / low | Major support |

**Measured retracement of the 2026-09-09 → 2026-09-25 advance (closing basis: 315.34 → 341.07, range 25.73 points):**
- 38.2% = **331.24** (current close 330.32 is essentially *at* this level)
- 50.0% = **328.21**
- 61.8% = **325.17**

**Measured retracement of the wider swing (2026-09-09 low 309.90 → 2026-09-22 high 345.34, range 35.44):** 38.2% = **331.80**; 50% = **327.62**; 61.8% = **323.44** — which brackets the 50 SMA at 322.18.

This is a genuinely useful confluence: the 38.2% retracement (331.2–331.8), the Bollinger mid (331.62) and the broken 10 EMA (333.70) form a tight **331–334 resistance shelf**, while the 50 SMA (322.18) and the 61.8% retracement (323.44) form a tight **322–323 support shelf**. Price is in the lower third of its own decision range.

**Gap context (important nuance):** the 2026-07-30 close was 333.43 and the 2026-07-31 open was 304.81, creating a gap zone roughly **304.81–333.43**. Price closed above the top of that gap (333.43) on **2026-09-17 (337.00)** after failing just below it on 9/14–9/16 (333.08, 331.34, 332.41). Today's 330.32 means price has **slipped back inside the upper portion of that old gap zone** — the breakout above the gap has not been decisively defended. Clearing 333.43–335.30 again would be a meaningful re-assertion.

---

## 7. Scenarios and triggers

**Bull continuation (base case, ~50–55% weight):** Price holds 328–330, bases for a few sessions, and reclaims the 331.62 mid-band followed by 333.70 (10 EMA) and 335.30 (VWMA). MACD histogram stops falling and curls back toward zero. ATR stays near 7. *Trigger:* daily close >335.30 on volume >50M. *Path:* 337.00 → 341.07 → 345.34/346.41.

**Extended consolidation (meaningful probability, ~25–30%):** Price chops between the 50 SMA (322.18) and the 10 EMA (333.70) for two to four weeks, letting the 50 SMA catch up and RSI reset to the mid-40s. This is the *most consistent* read with the low-ATR, low-volume pullback: it would rebuild a platform under 341 rather than break the trend. Watch for bandwidth to contract further (a second squeeze) before the next expansion.

**Trend deterioration (~20%):** A daily close below 322.18, confirmed by >50M volume, opens 316.83 (lower band) and then 314.90/309.90 (September lows). A break of 309.90 would invalidate the entire September structure and expose 304.81–300.00 (July gap floor). A MACD zero-line cross would corroborate this scenario.

**Note on probabilities:** these are judgments, not statistical outputs. No backtested hit rates are available from the tool data, so they should be treated as relative weighting, not precision.

---

## 8. Actionable plan

**For existing long-term holders:** The strategic trend is intact (price +14.35% above a rising 200 SMA; 50 SMA 11.5% above 200 SMA and widening). No action is required on the trend signal. A sensible mechanical trail is **2× ATR ≈ 14.5 points below the high**, or a closing stop under the 50 SMA (322.18), accepting that this sits fairly close to spot (2.5% away) and will be triggered by ordinary noise if used intraday — use *closing* basis.

**For swing traders looking to add (two asymmetric setups):**
1. *Momentum re-entry:* wait for a **daily close above 335.30 (VWMA)** with volume >50M. Stop 1.5× ATR (≈10.9) at ~324.4, i.e. below the 50 SMA. Targets 341.07 then 345.34. Reward/risk ≈ 0.5:1 to first target — thin.
2. *Pullback entry (better asymmetry):* scale in at **322–325** (50 SMA + 61.8% retracement), stop on a close below **316.83** (lower band), targets 331.6 / 335.3. Reward/risk ≈ 1.2:1 to 2.3:1. This is the preferred structure *if* the pullback extends.

**For those wanting to hedge or trade short-term weakness:** a close below **322.18** activates the short/hedge case, with 316.83 and 309.90 as objectives and a stop back above 331.6. Do not initiate shorts in the 330–333 zone: it is mid-range with the 50 SMA rising underneath.

**What NOT to do:** chase in the **331–336** band. Price is below VWMA and the 10 EMA but above the 50 SMA — both long and short setups have poor location there.

**Sizing discipline:** with ATR at 2.20% of price the *daily* risk is modest, but the observed single-session gaps of **−5.0% (2026-02-12), −6.1% (2026-06-25), −7.4% (2026-07-31)** mean overnight risk is materially larger than ATR implies. Size positions so a 7–8% adverse gap is survivable, and prefer defined-risk options structures around known catalysts.

**Calendar note:** the last ex-dividend in the series was **2026-08-10 ($0.27)** following 2026-05-11 ($0.27), 2026-02-09 ($0.26) and 2025-11-10 ($0.26) — a quarterly cadence that implies the next ex-date is likely in early November 2026, outside the immediate trading window.

---

## 9. What would change this read

| Observation | Would flip the read to… |
|---|---|
| Daily close >335.30 (VWMA) with volume >50M and MACD histogram turning back up | Bullish continuation, add exposure |
| Daily close below 322.18 (50 SMA) on >50M volume | Intermediate trend warning, reduce |
| MACD line crossing below zero | Confirmed regime change, not a pullback |
| RSI <40 while price holds >322 | Deep reset within uptrend — high-quality entry |
| Bandwidth compressing below ~6% again | Pre-breakout coil; wait for direction |
| Close below 309.90 (September low) | September structure invalid; 304.81–300 in play |

---

## 10. Why these eight indicators

The selection is deliberately **one-per-job** with no duplicated signal:

- **close_200_sma + close_50_sma** establish strategic and intermediate trend direction and give the 50/200 spread (11.5% and widening) — the "is the trend intact?" question. They are not redundant because they answer different horizons and their *relationship* is itself the signal.
- **close_10_ema** is the only fast average included, used strictly to time the short-term flip (it broke on 2026-09-29). Adding a second fast average would be redundant.
- **macd + macds** are taken as a pair because the crossover is what matters here; the histogram divergence (2.028 on 9/3 vs 0.803 on 9/25) is the most informative single detail in the whole dataset and cannot be read from RSI or price alone.
- **rsi** adds a bounded oscillator that MACD cannot provide — it quantifies *how much* room is left (51.4 = neutral) and confirms there was never an overbought extreme.
- **atr** is included purely for executable risk sizing (stops, position size, gap awareness), not for direction.
- **vwma** is the only volume-weighted measure selected; it integrates participation with price and produces the actionable 335.30 reclaim level, something a plain SMA cannot do. (Raw volume analysis is done qualitatively from the OHLCV rows instead of adding a second volume indicator.)
- **Bollinger bands** were used as a secondary volatility-envelope cross-check (squeeze→expansion→re-contraction) but are excluded from the core eight because the volatility job is already covered by ATR; including both as primary signals would double-count volatility.

---

## 11. Key points summary

| Area | Signal / Value (2026-10-01) | Read | Actionable use |
|---|---|---|---|
| Price | Close 330.32; O 330.00 / H 332.48 / L 325.81; vol 36.31M | −3.2% from 52-wk closing high 341.07 (9/25); −4.3% from intraday high 345.34 (9/22) | Mid-range; avoid chasing 331–336 |
| Long-term trend | 200 SMA 288.86, rising ~0.26/day | Bullish; price +14.35% above | Strategic long bias intact |
| Intermediate trend | 50 SMA 322.18, rising ~0.31/day | Bullish; price +2.53% above; extension compressed from 6.0% (9/25) | **Primary invalidation level** |
| Short-term trend | 10 EMA 333.70, now declining | Bearish flip; first close below on 9/29 | Reclaim needed to re-engage long |
| MACD | 4.083 vs signal 5.073; hist −0.990 | Bearish cross 9/29; still positive above zero | Zero-line test is the regime-change watch |
| Momentum divergence | Histogram 2.028 (9/3) → 0.803 (9/25) while price rose 328.21 → 341.07 | Slowing momentum preceded the drop | Supports "digestion, not breakout" near term |
| RSI | 51.43 (peak 66.88 on 9/22; never >70) | Neutral, two-sided; no exhaustion | Room to reset to 40 without breaking trend |
| ATR | 7.2515 = 2.20% of price, down from 9.83 (8/3) | Low, orderly volatility | 1.5×ATR ≈ 10.9 pt stop; 2×ATR ≈ 14.5 pt |
| VWMA | 335.30; price 1.49% below; slope flattened | Recent volume-weighted buyers underwater | Close >335.30 on >50M = long trigger |
| Bollinger | Mid 331.62 / UB 346.41 / LB 316.83; width 8.92% | Squeeze (5.0% on 8/27) → expansion (10.2% on 9/25) → re-contracting | Direction unresolved; 322–336 is the decision box |
| Volume | 36.31M vs 70.0M (9/10) and 86.6M (9/18) | Pullback on below-trend volume | No distribution signal yet |
| Retracement confluence | 38.2% = 331.2–331.8; 50% = 327.6–328.2; 61.8% = 323.4–325.2 | Price at 38.2%; 50 SMA overlaps 61.8% | 322–325 = highest-quality long zone |
| Primary trade | Wait for either 322–325 hold or close >335.30 | Asymmetry favors the pullback entry | Stop <316.83 or <322.18 on closing basis |
| Gap risk | −5.0% (2/12), −6.1% (6/25), −7.4% (7/31) | Overnight risk >> ATR | Reduce size / use defined-risk structures |

*This report is technical analysis of the supplied price data, not investment advice. All levels and percentages above are computed from the tool-returned OHLCV and indicator series dated 2026-10-01 or earlier.*