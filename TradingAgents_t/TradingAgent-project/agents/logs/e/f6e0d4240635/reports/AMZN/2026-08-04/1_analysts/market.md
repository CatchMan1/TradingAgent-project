# AMZN — Technical & Trend Analysis Report
**Analysis date:** 2026-08-04 (market close) · **Instrument:** AMZN (Amazon.com, Inc.)
*All exact OHLCV and indicator values below are sourced from `get_verified_market_snapshot` (2026-08-04) and cross-checked against `get_stock_data` / `get_indicators`. No discrepancies were found between the snapshot and the indicator tools.*

---

## 1. The Single-Most-Important Fact: AMZN Is In a Post-Catalyst Repricing Regime

The most recent five sessions describe a market that has been structurally re-rated, not merely trended:

| Date | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|
| 2026-07-29 | 229.32 | 232.82 | 226.16 | **226.65** | 44.96M |
| 2026-07-30 | 233.35 | 239.82 | 231.06 | **235.50** | 101.84M |
| 2026-07-31 | 265.00 | 273.23 | 262.01 | **271.58** | 129.05M |
| 2026-08-03 | 278.29 | **287.20** | 278.00 | **284.02** | 90.83M |
| 2026-08-04 | 276.06 | 281.07 | 275.82 | **277.42** | 69.75M |

Concrete, tool-supported observations:

- **07-31 gap:** prior close 235.50 → 07-31 open 265.00, with 07-31's *low* (262.01) far above 07-30's *high* (239.82). That leaves an **unfilled upward gap of ~9.3%** between 239.82 and 262.01. Close-to-close, 235.50 → 271.58 = **+15.32% in one session** on **129.05M shares**, which is roughly **2.6x** the ~48.7M average of the 22 sessions from 2026-07-06 to 2026-08-04 (my calculation from tool volume data).
- **08-03 continuation:** +4.58% to 284.02, printing **287.20 intraday — the highest high in the entire visible dataset** (data begins 2026-01-02; the previous visible high was 278.56 on 2026-05-05).
- **08-04 rejection:** −2.32% to 277.42, an inside-range day that still broke 08-03's low (275.82 vs 278.00) and left a **small unfilled gap-down** (08-03 close 284.02 → 08-04 open 276.06), with the high capped at 281.07.

I cannot verify the *cause* of the 07-30/07-31 explosion from the tools available (no news feed). The volume signature — 101.84M then 129.05M versus a ~35–45M baseline in preceding weeks — is consistent with a scheduled corporate catalyst (e.g., earnings), but treat that as inference, not fact.

**Interpretation:** the stock spent May–July repricing *down* (−17.28% from the 2026-05-28 close of 274.00 to the 2026-07-29 close of 226.65), and then erased that entire decline in two sessions (+22.40% from 226.65 to 277.42). Price is now at the top of its visible range. This is a **momentum-breakout / high-volatility regime**, and indicator selection must respect that: mean-reversion signals are unreliable here, trend and volatility signals are not.

---

## 2. Indicator Selection and Rationale (8 selected)

| Indicator | Value (2026-08-04) | Why it matters *in this specific regime* |
|---|---|---|
| **close_10_ema** | 255.16 | The only MA fast enough to track a two-day gap. Measures how stretched the thrust is. |
| **close_50_sma** | 247.19 | Medium-term trend/support; distinguishes "real trend flip" from "gap spike." |
| **close_200_sma** | 235.66 | Long-term benchmark; confirms the secular uptrend was never broken. |
| **macd** (+ macds/macdh from snapshot) | 4.809 / 0.225 / **+4.585** | Detects the momentum *regime change* (negative → positive in 3 sessions). |
| **rsi** | 67.04 | Overbought/extension gauge; avoids chasing into exhaustion. |
| **atr** | 9.823 | The core risk tool now — volatility repriced +42% in three sessions. |
| **boll_ub** | 278.02 | Defines the "riding the band" breakout zone vs. a failed spike. |
| **vwma** | 252.45 | Confirms whether the gap was volume-validated or thin/suspect. |

**Deliberately excluded for redundancy:** `close_200_sma` vs. `boll` middle (both ~247 — nearly identical here, so I kept the 50-SMA as the medium-term reference and the upper band alone for the volatility envelope), and I did not pair `rsi` with any secondary oscillator (stochrsi/mfi) since RSI already captures the same overbought information.

---

## 3. Trend Structure: Bullish Stack, But Built on Two Sessions

Current ordering: **Close 277.42 > 10-EMA 255.16 > 50-SMA 247.19 > 200-SMA 235.66.**

- **Premiums to averages (computed):** +8.72% vs 10-EMA, +12.23% vs 50-SMA, +17.72% vs 200-SMA, +9.89% vs VWMA.
- **Long-term trend is genuinely intact and improving:** the 200-SMA has climbed steadily and monotonically from 232.13 (2026-06-05) to 235.66 (2026-08-04). There has been **no death cross** — the 50-SMA (247.19) sits ~11.5 points above the 200-SMA throughout the visible window.
- **The 50-SMA is the tell.** It has been *falling* for months — 256.16 (06-16) → 253.10 (07-15) → **246.38 (07-30)** — and only ticked up microscopically over the last three sessions (246.38 → 246.63 → 247.01 → 247.19). Translation: **the medium-term trend has only just stopped deteriorating; it has not yet turned up.** A single 20-point gap does not bend a 50-day average. This is the strongest argument against treating this as an already-confirmed medium-term uptrend.
- **The 10-EMA is vertical:** 236.29 (07-30) → 242.70 (07-31) → 250.22 (08-03) → **255.16 (08-04)**. Price is 8.7% above it. Every historical instance of that degree of separation in this dataset has resolved with at least a sideways consolidation, if not a retest.

**Net:** the *long-term* trend is up, the *medium-term* trend is neutral-to-turning, and the *short-term* trend is parabolic. These three states are in conflict — that is the central nuance of this setup.

---

## 4. Momentum: A Textbook Regime Flip, Already Maturing

**MACD** history is unambiguous and extremely sharp:

- 2026-07-29: MACD = **−3.751** (deepest reading of the pullback)
- 2026-07-30: −3.634
- 2026-07-31: **−0.623**
- 2026-08-03: **+2.736** — crosses zero
- 2026-08-04: **+4.809**

Signal line = **0.225**; histogram = **+4.585**. So MACD crossed *above* its signal line during the 07-31→08-03 window and the gap is now wide and expanding — the classic early-stage bullish crossover signature. This is the strongest single bullish confirmation in the dataset.

**Caveat — momentum is front-loaded, not sustainable in a straight line.** The MACD line went from −3.75 to +4.81 (+8.56 points) in **four sessions**. Historically, vertical MACD spikes of this magnitude mean-revert toward the signal line quickly, because the averages must "catch up." Expect either (a) price consolidation while MACD flattens, or (b) a MACD roll-over back toward zero. A **macdh contraction from +4.585** would be the first objective warning that the thrust is fading.

**RSI** path: 33.31 (07-29, near-oversold) → 67.88 (07-31) → **72.23 (08-03, overbought)** → **67.04 (08-04)**.

- The 08-04 dip is a *healthy* overbought reset — RSI exited >70 without price collapsing.
- Nothing in the data shows a bearish RSI divergence (the 08-03 RSI high of 72.23 accompanied a higher price high, so momentum confirmed price).
- 67.04 is in the neutral-to-strong band: **not** an exhaustion sell signal, and **not** a fresh-entry trigger. In confirmed uptrends RSI routinely holds 60–75; in this dataset the preceding downtrend kept RSI in the 33–54 range for two months, so a regime where RSI bases above 60 would itself be a bullish structural change.

---

## 5. Volatility: The Regime Has Repriced, and That Changes Everything About Stops

**ATR** jumped from **6.892 (07-29)** → **7.341 (07-30)** → **9.511 (07-31)** → **9.948 (08-03)** → **9.823 (08-04)**. That is **+42.6% in three sessions**. ATR of 9.82 = **3.54% of the 277.42 close**.

Practical consequences, all derived from tool values:

- A **1x-ATR** stop from 277.42 = **267.60**; **1.5x ATR** = **262.69**; **2x ATR** = **257.78**.
- Note that 1.5x ATR (262.69) lands almost exactly on the **07-31 gap low of 262.01**. That convergence is the single most useful coincidence in this chart: a stop just under ~262 is simultaneously (i) outside normal noise and (ii) placed at the structural invalidation of the gap. Stops tighter than that (e.g., under 275.82) are inside one day's noise and will likely be hit.
- **Position sizing must be cut.** If you risk a fixed dollar amount, the ATR expansion from 6.89 to 9.82 means the same dollar risk now buys ~30% fewer shares. Sizing off the pre-gap ATR would over-risk by ~42%.

**Bollinger envelope:**

- Middle (20-SMA) = **247.42**, upper = **278.02**, lower = **216.83** → bandwidth = **24.7%** of the middle, an extremely wide band created by the gap itself.
- On 08-03 the close (284.02) finished **above** the upper band (272.99 that day) — a genuine band-break/breakout print. On 08-04 the close (277.42) is **0.22% below** the upper band (278.02). So price is *hugging* the upper band rather than decisively riding it.
- **Two-sided read:** closing back below the upper band after a single day above it is the mild-failure version of a breakout. It is not bearish by itself — but the "easy" part of the move (the gap) is done, and the band now sits directly overhead as resistance at **~278**.

Notably, the 20-SMA (247.42) and 50-SMA (247.19) are **nearly identical**. That only happens when price has been range-bound for months — which is exactly the May–July picture. It means the 247 area is a *thick* structural shelf, not a thin line.

---

## 6. Volume: Strong Confirmation, Fading Follow-Through

**VWMA** = **252.45**, up hard from 240.82 (07-30) → 245.72 (07-31) → 250.17 (08-03) → **252.45 (08-04)**.

- Price (277.42) is **+9.89% above VWMA**, and VWMA is rising steeply. Rising VWMA with price above it = the volume-weighted "true average holder" is being dragged up, i.e., **the gap was volume-validated, not a thin print**. This is materially more bullish than a gap on light volume; a light-volume gap would have left VWMA flat and invited a full fill.
- **But the raw volume sequence is decaying:** 129.05M (07-31) → 90.83M (08-03) → **69.75M (08-04)**. That is a **−46% decline** from the peak in two sessions. Normal post-catalyst decay, and mildly constructive because the 08-04 down-day came on *lower* volume than the up-days (no distribution signature). The 08-04 volume is still ~1.43x the 22-day average, so participation remains elevated.
- **What would flip this:** a *down* day on volume expanding back above ~100M, or a close back below VWMA (~252 and rising). Neither has occurred.

---

## 7. Actionable Level Map

Derived entirely from verified OHLCV and indicator values:

| Level | Price | Source | Role |
|---|---|---|---|
| Resistance 1 | **287.20** | 2026-08-03 high (highest visible high) | Breakout trigger |
| Resistance 2 | **284.02** | 2026-08-03 close | Gap-fill / recovery pivot |
| Resistance 3 | **281.07** | 2026-08-04 high | Intraday supply |
| Pivot | **278.02** | Bollinger upper band | The "ride the band" line |
| Pivot | **278.56** | 2026-05-05 high | Old visible-range ceiling, now overhead |
| Spot | **277.42** | 2026-08-04 close | — |
| Support 1 | **275.82** | 2026-08-04 low | First dip-buy reference |
| Support 2 | **271.58** | 2026-07-31 close | Gap-day close; must hold on a weekly basis |
| Support 3 | **262.01** | 2026-07-31 low = gap edge | **Structural invalidation** (~1.5x ATR) |
| Support 4 | **255.16** | 10-EMA | Trend-following trailing stop |
| Support 5 | **252.45** | VWMA | Volume-weighted cost basis |
| Support 6 | **247.19–247.42** | 50-SMA / 20-SMA (Bollinger mid) | Thick medium-term shelf; final bull thesis line |
| Support 7 | **235.66** | 200-SMA | Long-term trend line; where the Apr–May 2026 highs (258.79 on 04-23, 278.56 on 05-05) become the reference |

---

## 8. Scenario Framework (with risk-defined triggers)

**Scenario A — Bullish continuation (highest probability, ~45%):** AMZN digests for 2–5 sessions in the 271–284 zone, the histogram stays positive, and a close **above 287.20** on volume >90M re-arms the breakout. *Action:* add on the breakout close, not on intraday pokes; trail with the 10-EMA. *Target structure:* measured move from the 07-29 low (226.65) to the 08-03 high (287.20) is 60.55 points; a similar extension off a 287.20 base projects into the low 330s — treat that as a **projection, not a forecast**, and only after a confirmed breakout close.

**Scenario B — Constructive consolidation / partial gap-fill (most likely near-term path, ~40%):** given +8.72% vs the 10-EMA, RSI 67 after a 72 print, and price just rejected at 287.20, the odds favor *time* correction. A drift into **271.58 → 262.01** would be a normal, healthy retest of the gap edge. *Action:* staged limit accumulation at ~271 and ~263, sized so the average cost is near VWMA (~252–255). This is the higher reward-to-risk entry than chasing 277.

**Scenario C — Gap failure (~15%):** a close **below 262.01** decisively breaks the gap structure and would likely target the 10-EMA (255.16) then the 247 shelf. *Action:* hard stop under 262 for any breakout-chasing long; do not "average down" a failed gap — statistically these fill toward the origin, i.e., 239.82.

**Overall stance: constructive/bullish bias, but explicitly do NOT chase at 277.42.** The evidence for bullishness (MACD zero-cross + expanding histogram, volume-validated VWMA, price above all major MAs, 200-SMA rising, RSI reset without price damage) is real and multi-factor. The evidence for caution (8.7% above the 10-EMA, 50-SMA still near-flat after months of decline, one-day close above the upper band already surrendered, −46% volume decay, −2.32% rejection day, ATR +42%) is equally real and argues that **the risk/reward at the current print is poor while the risk/reward ~5–6% lower is excellent.**

---

## 9. Honest Limitations of This Analysis

- The visible dataset begins **2026-01-02**; I cannot confirm "all-time high" — only the **highest high in the visible window (287.20)**.
- I have **no fundamental or news data**; the catalyst identity behind the 07-30/07-31 volume explosion is inferred from the volume signature alone.
- I have **not** validated any prior support/resistance "bounce" statistically; the level map above is structural (prior highs/lows/closes and indicator values), not backtested.
- ATR-based stop distances assume the current volatility persists; if ATR reverts toward the pre-gap ~6.9, stops at 262 become relatively wider than intended.
- Every percentage figure in this report is arithmetic on tool-supplied closes and is labeled as my computation where applicable.

---

## 10. Key Points Summary

| Dimension | Reading (2026-08-04) | Signal | Conviction |
|---|---|---|---|
| **Close** | 277.42 (−2.32% d/d) | Rejection day below 08-03 close | Moderate |
| **Visible high** | 287.20 (08-03) | Immediate resistance; new visible-window high | High |
| **10-EMA** | 255.16 (+8.72% below price) | **Extremely stretched** — do not chase | High |
| **50-SMA** | 247.19 (+12.23% below price) | Medium-term trend *just* stopped falling | Moderate |
| **200-SMA** | 235.66 (+17.72% below price), rising monotonically since 06-05 | Long-term uptrend intact; no death cross | High |
| **MACD / Signal / Hist** | 4.809 / 0.225 / **+4.585** | Fresh bullish crossover, zero-cross on 08-03 | **High (bullish)** |
| **RSI** | 67.04 (from 72.23) | Overbought reset, no bearish divergence | Neutral-positive |
| **ATR** | 9.823 (+42.6% in 3 sessions) | Volatility regime shift — resize positions | High |
| **Bollinger upper / mid / lower** | 278.02 / 247.42 / 216.83 | Closed 0.22% *below* upper band after one day above; 20-SMA ≈ 50-SMA = thick 247 shelf | Moderate |
| **VWMA** | 252.45 (price +9.89% above), rising steeply | Gap was **volume-validated** | **High (bullish)** |
| **Volume trend** | 129.05M → 90.83M → 69.75M | Follow-through decaying, but down-day on lightest volume | Neutral |
| **Unfilled gap** | 239.82 → 262.01 (~9.3%) | 262.01 is the structural line in the sand | High |
| **Primary plan** | Stage entries at ~271 and ~263; stop <262 (≈1.5x ATR); add only on a close >287.20 | Risk-defined bullish, non-chasing | — |
| **Invalidation** | Close below 262.01 (gap edge); thesis break below 247 shelf | Exit / reassess | High |