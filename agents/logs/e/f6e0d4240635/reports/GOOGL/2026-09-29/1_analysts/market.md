# GOOGL — Alphabet Inc. | Technical & Tactical Review
**Analysis date: 2026-09-29 (Tuesday close)** | Price basis: 340.92 USD

---

## 1. Data integrity check (done before any claims)

The `get_verified_market_snapshot` (2026-09-29) and the individual indicator series agree to 4+ decimals on every overlapping value:

| Field | Snapshot | Indicator series | Status |
|---|---|---|---|
| Close | 340.92 | 340.92 (CSV) | Match |
| close_50_sma | 343.9886 | 343.9886 | Match |
| close_200_sma | 338.4388 | 338.4388 | Match |
| close_10_ema | 343.5616 | 343.5616 | Match |
| macd / macds | -0.2945 / -0.3015 | -0.2945 / -0.3015 | Match |
| rsi | 47.3609 | 47.3609 | Match |
| boll / ub / lb | 342.0605 / 354.6468 / 329.4742 | 342.0605 / 354.6468 / 329.4742 | Match |
| atr | 8.2086 | 8.2086 | Match |
| vwma | 345.4203 | 345.4203 | Match |

No conflicts found. Latest session: **O 341.95 / H 342.84 / L 338.02 / C 340.92 / V 21.07M**. Note a cash dividend of **0.22** went ex on **2026-09-04**, so price changes across that date include a small mechanical adjustment.

---

## 2. Where price sits in the structure

**Three timeframes, three different answers — this is the core of the setup.**

**Long term (bullish, intact).** Price is **+0.73% above a rising 200-day SMA (338.44)**, which itself has climbed from 315.61 on 2026-07-01 to 338.44 today (+7.2%). On a 12-month basis GOOGL is up **+39.7%** (244.05 → 340.92), and the 50-day remains above the 200-day (a golden-cross structure). The primary trend has not broken.

**Medium term (deteriorating).** The 50-day SMA is **falling**: 358.74 (2026-07-31) → 343.99 (2026-09-29), a 4.1% decline in two months. Price has closed **below the 50-day for five consecutive sessions** (9/23 through 9/29), and the 50/200 gap has compressed to just **5.55 points** from roughly 43 points on 2026-07-01. That convergence is the single most important structural observation in this report: the cushion between the two averages has almost disappeared.

**Short term (bearish/neutral).** Price is **-0.77% below the 10-EMA (343.56)** with three straight closes beneath it, **-0.89% below the 50-SMA**, and **-1.30% below the VWMA (345.42)**. Price is effectively **sandwiched between the 200-day (338.44, below) and the 50-day (343.99, above)** — a 5.5-point decision zone.

**The bigger pattern is a contracting range, not a trend.** Lower highs: 408.61 (2026-05-18 intraday) → 386.76 (2026-05-01) → 380.52 (2026-08-04) → 364.17 (2026-09-22) → 350.00 (2026-09-23). Higher lows: 314.90 (2026-07-23) → 327.74 (2026-09-10) → 337.45 (2026-09-23). The May close peak of 402.62 leaves price **-15.3% below its 52-week closing high** and **-16.6% below the 408.61 intraday high**. Meanwhile the last three months are net negative: 353.65 (2026-06-29) → 340.92 = **-3.6%**.

---

## 3. Indicator-by-indicator read

**Bollinger Bands (20,2): middle 342.06 | upper 354.65 | lower 329.47.**
Price at 340.92 sits just under the midline with **%B ≈ 0.455** — dead center of the distribution. Total band width is **25.17 points (7.36% of the midline)**, and it has **widened roughly 24% since 2026-09-14** (width then 20.27). This is *not* a squeeze setup; volatility has expanded, so "coiled spring breakout" logic does not apply here. Use the bands as objective targets: **354.65 upside**, **329.47 downside**. Distance from spot: +4.03% / -3.36%.

**MACD (line -0.2945, signal -0.3015, histogram +0.0070).**
A bullish crossover technically printed today, but treat it with heavy skepticism:
- Both lines are **still below zero**.
- The histogram is **+0.007** — statistically indistinguishable from zero.
- The MACD line has **collapsed from +1.076 (2026-09-22) to -0.2945 in five sessions.** The "cross" happened because the signal line fell faster (-0.877 → -0.302), not because the MACD line turned up.

This is **momentum decay, not momentum reversal.** A real bullish confirmation needs the MACD line back above zero *and* the histogram expanding beyond ~+0.30.

**RSI(14): 47.36.** Neutral, no oversold condition, no usable divergence. The sequence of RSI highs is 58.80 (9/21) → 55.26 (9/22) → 49.72 (9/25) → 47.36 (9/29) — a clean cooling pattern that matches price. Critically, RSI at 47 means there is **room to fall without any oversold support**, and room to rise without being overbought. RSI is confirming the range, not signaling a turn.

**ATR(14): 8.21 points = 2.41% of spot.** This is the volatility anchor for everything else. ATR spiked to **9.15 on 2026-09-23** (the -3.8% session) and has since eased back to 8.21 — realized volatility is normalizing. Practical implications: 1.5×ATR = **12.31 pts**, 2×ATR = **16.42 pts**; daily noise of ±2.4% should be expected and stops tighter than ~1 ATR (8.2 pts) will be noise-stopped.

**VWMA: 345.42 — the most useful bearish tell on the board.** Price is **1.3% below** the volume-weighted average, and the VWMA is *rising* (339.39 on 9/11 → 345.42 today) while price *falls*. That divergence means the heavy-volume sessions were **up-days at higher prices that have since been given back**:
- 2026-09-18: 47.63M shares, close 349.54 (faded from a 359.44 high)
- 2026-09-21: 30.46M shares, close 354.97
- 2026-09-22: 29.79M shares, close 351.16 (rejected from 364.17)
- 2026-09-23: 35.58M shares, close 337.83 (near the low)

That is a textbook **failed-breakout / distribution cluster**: buyers paid up on volume near 350–357, and those positions are now underwater. This creates **overhead supply at 344–355**, which is exactly where the 50-SMA and VWMA sit. A rally into that zone should be treated as a *test*, not a breakout, until volume proves otherwise.

**Volume context:** the 20-session average is **25.99M** (computed from the CSV). Today's 21.07M is **~19% below average** — the bounce off the 9/23 low is happening on **declining volume**, which is characteristic of a corrective bounce rather than accumulation.

---

## 4. Key levels (all derived from verified rows)

| Level | Price | Source / date |
|---|---|---|
| Supply / failed high | 364.17 | 2026-09-22 intraday high |
| Supply | 359.44 / 354.97 | 9/18 high, 9/21 close |
| Bollinger upper | 354.65 | 2026-09-29 |
| Resistance cluster | 350.00–351.16 | 9/23 high, 9/22 close |
| **First resistance** | **343.99 / 345.42** | 50-SMA / VWMA |
| Spot | 340.92 | 2026-09-29 close |
| **First support** | **338.44** | 200-SMA |
| Support | 337.45 | 2026-09-23 low |
| Support | 330.65–329.47 | 9/9 close, Bollinger lower |
| Critical support | 327.74 | 2026-09-10 low (September low) |
| Structural support | 317.69 / 314.90 | 7/23–7/24 closes, July low |

**The 200-day has been tested three times in three weeks and has not been abandoned:** closes below it occurred on 9/9 (330.65 vs 336.40) and 9/10 (332.60 vs 336.62), were reversed on 9/11 (338.50 vs 336.81), and a marginal 0.12-point breach on 9/23 (337.83 vs 337.95) was reversed the next session. That is observable behavior from the data — it does not guarantee the next test holds, but it establishes 336–338.4 as the line in the sand.

---

## 5. Actionable scenarios

**Base case — range-bound chop (highest probability given RSI 47, MACD ≈0, %B 0.455).** Price oscillates between 337.5 and 350.0. Low-conviction environment; the edge is in *not* paying up in the middle of the range. Avoid initiating at 341 — that is no-man's-land with 5 points to support and 5 points to resistance.

**Bearish trigger — daily close below 337.40 (9/23 low) and below the 200-day.**
That would break the higher-lows sequence and confirm the failed 9/22 breakout. Targets: **330.65 → 329.47 (lower band) → 327.74**. Stop reference: 343.50 (above the 50-SMA/VWMA shelf), ≈6.1 points ≈ **1.7:1 R:R** to the 327.74 target. A close below 327.74 opens the July gap zone at **317.69 / 314.90** and would likely coincide with a 50/200 death cross.

**Bullish trigger — daily close above 345.50 (VWMA) on volume >30M (>15% above the 26M average).**
Volume is the non-negotiable condition, because 344–355 is trapped supply. Confirmation sequence: 349.54–351.16 → 354.65 (upper band) → **364.17**. A close above 364.17 breaks the entire sequence of lower highs and re-opens **380.52 (8/4 high)**. Stop: 1×ATR below entry (~8.2 pts), or below 343.5 for a tighter, higher-risk-of-noise version.

**Pullback-buy (best risk/reward, requires patience).** Wait for a flush into **331–329.5** (lower band + 9/9 close zone). Entry ~331, stop **326.50** (below the 9/10 low of 327.74, ~0.55 ATR of buffer), target **342.00 / 345.40**. Risk 4.5, reward 11–14 → **2.4:1 to 3.1:1**. This is the only setup on the board with clearly favorable asymmetry.

**Do-not-do:** buying the current 340.92 print. Risk to 337.4 is 3.5 points; reward to 345.4 is 4.5 points, and the trade sits directly in the path of the VWMA supply shelf. R:R < 1.3 with negative short-term momentum.

---

## 6. Risk management math (ATR-based)

- ATR = 8.21 (2.41%). Typical 5-day range ≈ 8.21 × √5 ≈ **18.4 points (±2.7%)** — plan for that much noise.
- Stops: minimum **1 ATR (8.21)**, preferably **1.5 ATR (12.31)** for swing positions.
- Sizing example: $100,000 account, 1% risk ($1,000), stop 12.31 pts → **81 shares** (~$27,600 notional, 27.6% of capital). At a 6.1-point tactical stop (bearish trigger) the same $1,000 risk allows 164 shares (~$55,900 notional) — note how tighter stops quietly double position size and gap risk.
- Because band width is **7.36%** and ATR 2.41%, overnight gap risk is material; consider half-size into the late-October reporting window (Alphabet's Q3 report typically lands in that period — **confirm the official date before sizing around it**).

**What invalidates the bearish/neutral read:** a volume-backed close above 345.42, followed by a hold of the 50-SMA at 344 for 2–3 sessions. **What invalidates the bullish/neutral read:** a close below 337.40 that is *not* reversed within two sessions, especially if the 50-SMA crosses below the 200-SMA.

---

## 7. Summary table

| # | Indicator | Value (2026-09-29) | Signal | Interpretation | Actionable level |
|---|---|---|---|---|---|
| 1 | Close | 340.92 | Neutral | Between 200-SMA and 50-SMA; mid-range | Range 337.4–350.0 |
| 2 | close_50_sma | 343.99 (falling from 358.74 on 7/31) | Bearish | 5 straight closes below it; acting as resistance | Reclaim >344 needed |
| 3 | close_200_sma | 338.44 (rising from 315.61 on 7/1) | Bullish | Primary uptrend intact; tested 9/9, 9/10, 9/23 and reclaimed | Close <337.4 = warning |
| 4 | close_10_ema | 343.56 | Bearish | Price below for 3 sessions; short-term rollover | >343.6 to neutralize |
| 5 | macd / macds | -0.2945 / -0.3015 (hist +0.007) | Weak bullish cross | Both lines <0; MACD fell from +1.076 (9/22) — decay not reversal | Needs hist >+0.30 |
| 6 | rsi | 47.36 | Neutral | Mid-range, no divergence, no oversold cushion | <40 = washout zone |
| 7 | boll / ub / lb | 342.06 / 354.65 / 329.47 | Neutral, wide | %B 0.455; width 7.36%, widened ~24% since 9/14 | Targets 354.65 / 329.47 |
| 8 | atr | 8.21 (2.41%) | Risk gauge | Cooling from 9.15 on 9/23 | Stops 8.2–12.3 pts |
| 9 | vwma | 345.42 (rising) | Bearish | Price 1.3% below; 9/18–9/22 volume trapped at 350–357 | Overhead supply 344–355 |
| 10 | Volume (20d avg) | 25.99M vs 21.07M today | Bearish tilt | Bounce off 9/23 low on ~19% below-average volume | >30M needed to trust upside |

**Bottom line:** GOOGL is a **long-term uptrend inside a three-month distribution range**, currently in the lower half of a 337–350 box with short-term momentum negative but not extreme. The 200-day at **338.44** is the pivotal level; the **344–345.4** VWMA/50-SMA shelf is the ceiling. The favorable trade is *not* here at 340.92 — it is either a patient buy at **331/329.5 with a 326.5 stop** (≈2.4–3.1:1), a volume-confirmed breakout above **345.50** targeting 354.65/364.17, or a break of **337.40** targeting 330.65/327.74. Until one of those triggers, small size and patience beat activity.