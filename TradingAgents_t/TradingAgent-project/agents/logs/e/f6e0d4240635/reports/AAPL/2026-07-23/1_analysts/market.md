# AAPL (Apple Inc.) — Technical Analysis Report
**Analysis date: 2026-07-23 (latest settled session) | Last close: $321.66**

Data reconciliation note: the OHLCV pull from `get_stock_data` (139 rows, 2026-01-01 → 2026-07-23) and the `get_verified_market_snapshot` (2026-07-23) agree row-for-row, including the 2026-07-23 bar (O 321.73 / H 323.30 / L 319.35 / C 321.66 / V 40.84M). No discrepancy to flag; all exact levels below come from the verified snapshot.

---

## 1. Market context: a parabolic July advance now in its first meaningful pause

The dominant feature of the tape is the sequence that began on **2026-06-25**: a violent −6.1% day (close 275.15, volume 107.0M) followed by a 261.8M-share reversal session on 2026-06-26 (close 283.78, low 274.21). From the 2026-06-26 low of **274.21** to the 2026-07-17 high of **334.99**, AAPL gained **+22.2% in 15 sessions**. The advance then stalled:

| Date | Close | Volume |
|---|---|---|
| 2026-07-16 | 333.26 | 62.97M |
| 2026-07-17 | **333.74** (cycle closing high) | 63.41M |
| 2026-07-20 | 326.59 | 53.47M |
| 2026-07-21 | 327.74 | 41.34M |
| 2026-07-22 | 325.89 | 38.76M |
| 2026-07-23 | **321.66** | 40.84M |

That is **−3.62% from the 2026-07-17 close** — but the internal quality of that pullback is the single most important read in this report: **volume has contracted on every down day** (63.4M → 53.5M → 41.3M → 38.8M → 40.8M). Distribution-driven tops almost never look like that; this pattern is consistent with supply drying up into a consolidation rather than institutional liquidation. Context: the year opened at 271.01 (2026-01-02) and printed a 2026 low close of **246.70 on 2026-01-20**, so the primary trend for the year remains decisively upward.

---

## 2. Why these 8 indicators were selected

The context is a **strongly trending, high-volatility instrument at a short-term momentum inflection** — not a range-bound or mean-reverting setup. So the selection pairs trend-structure anchors with momentum-deceleration detectors and a volatility/volume reality check:

| # | Indicator | Role in this specific setup |
|---|---|---|
| 1 | `close_200_sma` | Strategic regime filter — is the bull intact? |
| 2 | `close_50_sma` | Medium-term trend + first structural support / trailing stop reference |
| 3 | `close_10_ema` | Detects the *short-term* momentum loss that the 50/200 cannot see |
| 4 | `macd` | Trend-momentum impulse; confirms/corrects the MA read |
| 5 | `macdh` | Rate-of-change of momentum — the earliest warning at a fresh high |
| 6 | `rsi` | Overbought/oversold + divergence detection (needed here because RSI already hit 79.8 and 32.2 in the last 8 weeks) |
| 7 | `atr` | Position sizing and stop placement — mandatory given ATR is elevated and the stock moves ~$8/day |
| 8 | `vwma` | Confirms whether the July advance is volume-backed, and gives the true breakeven of the marginal buyer |

*Supplementary (reviewed, not counted):* the Bollinger envelope (`boll` 311.49 / `boll_ub` 346.68 / `boll_lb` 276.31) — used only to quantify statistical extension and bandwidth. Redundancy was deliberately avoided (no stochrsi alongside RSI, no second MACD variant).

---

## 3. Trend structure: bull market intact, but stretched

**Verified values (2026-07-23):** 10 EMA 322.655 | 50 SMA 305.467 | 200 SMA 275.599 | Close 321.66

- **Price is +5.30% above the 50 SMA and +16.93% above the 200 SMA.** Both averages are rising with a positive and *widening* slope: the 50 SMA climbed 271.72 (2026-05-26) → 305.47 (2026-07-23), i.e. +$33.75 in two months. The 50-minus-200 spread has widened from **+9.73 (2026-05-26)** to **+29.87 (2026-07-23)** — the golden-cross configuration is strengthening, not decaying. There is no death-cross risk anywhere in the visible window.
- **The 50 SMA is rising ~$0.60–$0.70 per session** (304.89 → 305.47 in one day). That mechanical drift will place it near 311–312 within 10 sessions — meaning price closing toward the Bollinger midline (311.49) would still not break the primary trend.
- **The warning is at the fast end.** The close (321.66) is **below the 10 EMA (322.66) for the first time since the 2026-07-01 breakout leg**, and the 10 EMA itself has flattened hard: 319.73 (7/17) → 320.98 → 322.21 → 322.88 → **322.66** (7/23). A flattening 10 EMA after a +22% run is the classic signature of a trend transitioning from impulse to digestion.

**Verdict on structure:** medium/long-term bullish, short-term neutral-to-corrective. This is a *pullback within an uptrend*, not a trend reversal — yet.

---

## 4. Momentum: decelerating sharply, but from a very high level

**MACD 8.107 | Signal 7.312 | Histogram 0.795**

The MACD line remains deeply positive (peaked at **8.927 on 2026-07-21**, the highest reading in the visible window) and has *not* crossed below its signal line — the crossover condition for a formal momentum sell signal is not met. But the histogram is contracting at an accelerating pace:

- 2026-07-17: **+3.337** (histogram peak)
- 2026-07-20: +2.724
- 2026-07-21: +2.214
- 2026-07-22: +1.599
- 2026-07-23: **+0.795**

That is a **76% collapse in the histogram in four sessions** while price fell only 3.6%. Two readings follow: (a) momentum is bleeding faster than price, which historically front-runs further price consolidation or a deeper shakeout; (b) at +0.795 the histogram is within **~1–2 sessions of a zero-line cross**, which is the objective, mechanical trigger to watch. Note also that MACD printed a clean bearish-to-bullish flip on **2026-07-02** (histogram −1.251 → +0.261) that was highly reliable — the current reading is the mirror-image setup forming on the other side.

**RSI 58.11** — down from **71.65 (2026-07-17)**, i.e. RSI exited overbought in a straight line. For reference, the last two RSI extremes in this dataset were **79.79 on 2026-05-28** (followed by a −9.8% slide to 2026-06-09) and **32.20 on 2026-06-25** (followed by the +22% rally). Critically, RSI at 58 is **not** oversold and **not** broken — it sits in the neutral-bullish band where strong uptrends routinely reset before continuing. A drop below ~45–47 would be the first evidence that this is more than a reset.

**Momentum divergence to watch:** price made its high on 2026-07-17 (333.74) while RSI made its high on 2026-07-17 (71.65) — no classic divergence on that print. The deterioration is contained in the MACD histogram, not in a price/RSI divergence. That makes this a *momentum-fade*, not yet a *distribution top*.

---

## 5. Volatility and statistical extension

**ATR 7.918 (≈2.46% of close)** — up from 5.57 on 2026-05-29 and 8.74 at the 2026-07-02 peak. Volatility has roughly doubled since May. Practical implications:
- A "normal" AAPL day is now a **±$8 move**. Intraday noise of $4–5 must not be treated as signal.
- A standard 1.5×ATR stop from 321.66 is **$11.88**, i.e. ~$309.8 — which conveniently sits just under the Bollinger midline (311.49) and above the 50 SMA (305.47). Position sizing off a fixed dollar risk should therefore assume roughly 2.5% risk per share at 1×ATR.

**Bollinger envelope:** middle 311.49, upper **346.68**, lower **276.31**. Bandwidth is an extreme **22.6%** of the 20-day mean — a direct artifact of the June crash + July spike. Price at 321.66 sits at **%B ≈ 0.64** (upper half, but far from the upper band). Two consequences: (1) the bands are too wide to generate meaningful touch signals right now; (2) the **311.49 midline is the statistically natural mean-reversion target** for this pullback, and it coincides almost exactly with where the rising 50 SMA will be in ~10 sessions. That convergence (~311) is the highest-conviction support cluster on the chart.

---

## 6. Volume validation — the most bullish evidence in the report

**VWMA 321.376 | Close 321.66 | VWMA slope: aggressively rising**

- The VWMA has climbed from **288.84 (2026-06-30)** to **321.38 (2026-07-23)** — a $32.5 rise in 17 sessions. That is volume-weighted proof that the bulk of July's transacted shares changed hands at progressively higher prices. This is accumulation, not a low-volume drift.
- **The close (321.66) is $0.29 above the VWMA (321.38)** — essentially pinned to it. This is the single most actionable line on the chart: the volume-weighted breakeven of the entire July buying cohort.
- Caveat per the indicator's own limitation: the **2026-06-26 volume of 261.8M** (vs. a ~40–60M norm) is almost certainly an index-rebalance or event-driven print and does skew the VWMA window. But because it's now ~19 sessions old, it is rolling out of the calculation, and the VWMA's *upward* slope is being driven by July's elevated, orderly volume (61–75M on the up-days of 2026-07-02, 07-15, 07-16, 07-17) — not by the outlier.

**Interpretation:** a close decisively below 321.38 (i.e. below ~320, and certainly below the 2026-07-23 low of 319.35) would flip the marginal July buyer into a loss and materially raise the odds of a fast slide to 311–314. Holding above it keeps the breakout structure fully valid.

---

## 7. Actionable levels — all derived from verified tool output

**Resistance**
- **$326.59–$327.74** — the 2026-07-20/07-21 close cluster; first reclaim needed to neutralize the pullback.
- **$333.74 close / $334.99 high (2026-07-17)** — the confirmed cycle high; a close above 334.99 is the clean breakout trigger.
- **$346.68** — Bollinger upper band (a statistical ceiling, not a proven level).

**Support**
- **$321.38** — VWMA (immediate bull/bear line).
- **$319.35** — 2026-07-23 session low.
- **$317.32–$314.86** — the unfilled gap zone from the 2026-07-15 breakout (07-14 close 314.86; 07-15 low 317.32). This is the highest-quality structural support because it is a gap, not an opinion.
- **$311.49** — Bollinger midline, converging with the rising 50 SMA by mid-August.
- **$305.47** — 50 SMA; a close below here invalidates the medium-term structure.
- **$275.60** — 200 SMA (strategic; ~14% below spot — not a near-term factor).

---

## 8. Scenarios and execution plan

**Scenario A — Constructive consolidation (highest probability given declining-volume pullback + intact 50/200 structure).** AAPL holds 319–321, RSI bases in the high 40s/low 50s, MACD histogram flattens above zero, and price reclaims 327.74. Entry on a close above **327.74** with a stop at **321.00** (below VWMA/7-23 low) targets **333.74–334.99**, then 346.68. Risk ≈ $6.7/share (~1× ATR), reward ≈ $7–13.

**Scenario B — Deeper mean reversion (triggered by a close below 319.35).** Expect a slide into the **314.86–311.49** zone (gap fill + Bollinger midline). This is a *buy* zone for the primary trend, not a short-term trend break — but only with confirmation (RSI stabilizing above ~45 and volume contracting on the flush).

**Scenario C — Trend damage (requires a close below 305.47 on expanding volume).** That would mark the first lower break of the 50 SMA since April and shift the stance to neutral/defensive. Nothing in the current verified data supports this as likely — the 50 SMA is rising ~$0.65/day and price is still 5.3% above it.

**What to monitor in the next 1–3 sessions (in priority order):**
1. Whether MACD histogram crosses zero (~1–2 sessions away at the current rate of decay) — the mechanical signal.
2. Whether the 10 EMA (322.66) is reclaimed — the fastest repair of short-term momentum.
3. Whether VWMA at 321.38 holds on a *closing* basis.
4. Daily volume: any down-day above ~70M would break the "quiet pullback" thesis and materially raise the odds of Scenario B/C.

---

## Key points summary

| Dimension | Indicator | Verified value (2026-07-23) | Signal | Conviction |
|---|---|---|---|---|
| Long-term trend | `close_200_sma` | 275.599 (rising) | Bull regime; price +16.9% above | High |
| Medium-term trend | `close_50_sma` | 305.467 (rising ~$0.65/day) | Uptrend intact; price +5.3% above | High |
| Short-term trend | `close_10_ema` | 322.655 (flattening) | **Price closed below it — first loss of fast momentum since 2026-07-01** | Medium |
| Trend momentum | `macd` | 8.107 vs signal 7.312 | Still bullish; no bearish cross yet | Medium-high |
| Momentum rate-of-change | `macdh` | +0.795 (from +3.337 on 07-17) | **−76% in 4 sessions; near zero-cross** | High (bearish watch) |
| Overbought/oversold | `rsi` | 58.11 (from 71.65 on 07-17) | Reset from overbought; neutral-bullish | Medium |
| Volatility / risk | `atr` | 7.918 (≈2.46% of price) | Elevated; size positions for ±$8 days | High |
| Volume confirmation | `vwma` | 321.376 | Close pinned $0.29 above it = pivotal; July advance is volume-backed | High |
| *Supplementary* | `boll` / `boll_ub` / `boll_lb` | 311.49 / 346.68 / 276.31 | %B ≈ 0.64; 22.6% bandwidth too wide for touch signals; 311.49 = mean-reversion magnet | Medium |
| Price structure | — | Close 321.66; cycle high 333.74 / high 334.99 (07-17); 07-23 low 319.35 | −3.62% from cycle close high on **declining** volume | High |
| Actionable plan | — | Trigger >327.74 → 333.74/334.99/346.68; invalidation <314.86–311.49 zone; structural break <305.47 | Long bias, staged entries, 1–1.5× ATR stops | Medium-high |

**Bottom line for AAPL:** the primary trend is emphatically bullish — 50 SMA above a rising 200 SMA with the spread widening, price 5.3% above the 50 SMA, and a volume-weighted average that has surged $32 in 17 sessions. But the *impulse* is over for now: price lost the 10 EMA, RSI reset from 71.7 to 58.1, and the MACD histogram has bled 76% in four sessions. The declining-volume character of the pullback argues for treating 319–314.86 as an accumulation window rather than an exit, while a MACD-histogram zero cross plus a close below 319.35 would justify patience over aggression.