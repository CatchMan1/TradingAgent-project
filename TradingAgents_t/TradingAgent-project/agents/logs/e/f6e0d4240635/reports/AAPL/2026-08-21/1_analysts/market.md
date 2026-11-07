# AAPL — Technical Analysis Report
**As of the close of 2026-08-21 | Last price: $309.35**

---

## 1. Executive Summary — The One-Line Stance

AAPL is in a **long-term uptrend that has been interrupted by an intermediate-term distribution event**. The stock remains ~9.9% above its rising 200-day SMA, but it is trading *below* the 10 EMA, the 50 SMA, and the Bollinger midline, with MACD below both zero and its signal line. Price is currently pinned in a **decision zone between $307 and $310.7** — the lower lip of an unfilled July 31 gap and the 50-day/10-day average cluster. This is a "prove it" setup: neither a clean continuation long nor a confirmed breakdown short.

**Bias: Neutral / range-bound with a constructive tilt.** Bearish momentum is decelerating (MACD histogram improved for four straight sessions), but no bullish trigger has fired.

---

## 2. Verified Data Baseline (source of truth: snapshot 2026-08-21)

| Field | Value |
|---|---|
| Open / High / Low / Close | 312.05 / 312.38 / 307.01 / **309.35** |
| Volume | 46,876,800 |
| 10 EMA | 310.352 |
| 50 SMA | 310.208 |
| 200 SMA | 281.502 |
| MACD / Signal / Histogram | −1.574 / −1.194 / **−0.380** |
| RSI(14) | 47.28 |
| Bollinger Mid / Upper / Lower | 314.339 / 338.856 / 289.821 |
| ATR(14) | 7.633 |
| VWMA | 308.804 |

*Data caveat: the snapshot's `mfi` field returns 0.598805, a scaling (0–1 vs 0–100) I cannot reconcile confidently. I have excluded MFI from the signal set rather than misattribute a "neutral" reading to it.*

---

## 3. Indicator Selection — 8 Chosen, and Why

The governing context is **"post-shock consolidation inside a bull trend."** That demands a mix of (a) trend anchors at two horizons, (b) momentum oscillators that can distinguish *deceleration* from *reversal*, (c) a volatility metric for stop placement, and (d) a volume-weighted price to judge where real positioning sits.

| # | Indicator | Role in this specific context |
|---|---|---|
| 1 | **close_200_sma** (281.50) | Defines whether the July damage broke the primary trend. It did not — this is the bull-market anchor and the deepest reference support. |
| 2 | **close_50_sma** (310.21) | The contested line. Price crossed below it and is now oscillating around it; the 50 SMA has flattened (309.08 on 08-17 → 310.21 on 08-21) — a trend *stall*, not a rollover. |
| 3 | **close_10_ema** (310.35) | Fastest read on whether the three-day August bounce (08-18→08-19) has any follow-through. It does not so far: price closed below it. |
| 4 | **macd** (−1.574) | Confirms momentum regime shift: MACD went from +9.61 (07-29) to negative territory on 08-11 — a structural change, not noise. |
| 5 | **macds** (−1.194) | Signal line defines the *trigger*: a reclaim of −1.19 is the first mechanical evidence of repair. |
| 6 | **rsi** (47.28) | Best available evidence of the July bearish divergence and of whether August selling reached exhaustion (it bottomed at 40.22, never oversold). |
| 7 | **atr** (7.633) | Volatility is mean-reverting post-shock (9.87 on 07-31 → 7.63). Necessary for non-arbitrary stop distance and position sizing. |
| 8 | **vwma** (308.80) | The volume-weighted cost basis of recent buyers. Price sitting a hair *above* it (+0.18%) tells us the marginal, volume-backed holder is roughly at breakeven — a pivotal level. |

*Supplementary (from snapshot, used as an overlay rather than core signals): Bollinger bands — the midline at 314.34 is the nearest real resistance shelf, and the envelope (289.82–338.86) quantifies how wide the post-gap distribution is.*

---

## 4. Primary Trend: Intact, But the Slope Has Flattened

- **12-month price path:** 224.90 (2025-08-21) → 309.35 (2026-08-21) = **+37.6%** price return (total-return index 228.05 → 314.85).
- **200 SMA at 281.50 is rising monotonically** — from 268.49 (2026-06-22) to 281.50 (2026-08-21), roughly +0.2/day with no down-tick in the sample. Price is **9.9% above it**.
- **Golden-cross structure intact:** 50 SMA (310.21) sits **28.71 points above** the 200 SMA — a wide, healthy spread that would take sustained weakness to close.

**Interpretation:** The primary trend has not been violated. Anything short of a weekly close below ~$289–$300 is a counter-trend dip within an uptrend. That framing matters for position bias: shorting strength here is fighting the 200-day, while buying blindly ignores that the *intermediate* trend has already turned down.

---

## 5. The Regime Break: 2026-07-31 Gap — The Most Important Event on the Chart

This is the technical fact that reorganizes everything else:

| Session | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|
| 2026-07-30 | 333.10 | 334.75 | 329.59 | 333.43 | 74.8M |
| **2026-07-31** | **304.81** | **310.69** | **300.00** | **308.91** | **132.5M** |

- Close-to-close: **−7.36%** in a single session.
- Volume at 132.5M vs a computed 20-session average of ~53M — roughly **2.5x normal**. High-volume downside gaps are a distribution signature, not a shakeout.
- **The gap is unfilled.** The void spans **$310.69 → $329.59** (6.1% of price). The highest print since the break is 320.28 (2026-08-20), i.e. the market has retraced only ~half of the gap and failed.
- **Peak-to-now drawdown:** from the 340.08 close on 2026-07-28, AAPL is **−9.03%**; from the 344.57 intraday high (07-29), **−10.2%**.

**Why this matters right now:** the closing price of 309.35 is *directly beneath the gap's lower lip at 310.69*. The single most consequential short-term level on the chart is not a round number — it is 310.7.

---

## 6. Intermediate Trend: Base-Building, With a Failed Breakout

Post-gap behavior has been a **$300–$320 range** (August low 300.57 on 08-12; high 320.28 on 08-20 — a 6.4% band):

- **08-12** close 302.25, RSI 40.22 → the low of the consolidation.
- **08-17 → 08-19**: 305.59 → 310.03 → 316.83, a genuinely strong three-day push (+3.7% from 08-17) on 50.5M volume (08-19).
- **08-20**: opened 317.46, tagged **320.28**, closed **311.30** — a rejection day that gave back the bulk of the gain.
- **08-21**: 312.05 open → 307.01 low → 309.35 close, near the session low, on 46.9M.

**The 50 SMA's message:** it rose from 289.47 (06-22) to a peak of 309.79 (08-07), then *flatlined* between 309.08 and 310.21 for ten sessions while price whipsawed around it. A flattening 50 SMA beneath a broken price is the classic signature of **trend transition into range**. The fact that price reclaimed it intraday on 08-18/08-19 but closed below it on 08-21 is a failure to convert.

**Net for August:** month-to-date, 308.91 (07-31) → 309.35 (08-21) = **+0.14%**. Two weeks of heavy two-way action and no net progress — the definition of consolidation.

---

## 7. Short-Term Momentum: Decelerating Bearishness, No Cross Yet

**10 EMA (310.35):** collapsed from 331.31 (07-30) to a trough of 308.76 (08-17), then flattened (308.99 → 310.41 → 310.57 → 310.35). Price at 309.35 is **−0.32% below it**. The 10 EMA has stopped falling — a necessary but not sufficient condition for a bottom.

**MACD — the nuanced read:**

| Date | MACD | Signal | Histogram |
|---|---|---|---|
| 07-29 | +9.609 | +8.437 | +1.172 |
| 08-11 | −0.827 | +2.444 | −3.271 |
| 08-17 | −2.676 | −0.385 | **−2.290** (trough) |
| 08-18 | −2.459 | −0.800 | −1.659 |
| 08-19 | −1.719 | −0.984 | −0.735 |
| 08-20 | −1.561 | −1.099 | −0.461 |
| **08-21** | **−1.574** | **−1.194** | **−0.380** |

The histogram has contracted for **four consecutive sessions** (−2.29 → −0.38), which is real evidence of selling exhaustion. **But flag the nuance:** on 08-21 the MACD *line itself* ticked down (−1.561 → −1.574) while the signal fell faster (−1.099 → −1.194). Part of the improvement is the signal line catching down to the MACD, not the MACD rising. A genuine bullish crossover requires MACD > −1.19 — achievable within a few sessions if price holds above ~$308, but it is **not yet in hand.**

**RSI (47.28):** textbook neutral. Critically, it **never reached oversold** during the entire post-gap decline (trough 40.22 on 08-12). That means the correction has been *orderly* rather than capitulative — which is usually neutral-to-positive medium term, but it also means no washed-out springboard has formed.

**Bearish divergence (verified):** price closed at **333.74 on 07-17** with **RSI 71.65**; it then made a **higher high of 340.08 on 07-28** while RSI printed a **lower 68.90**. Price up, momentum down — a classic bearish divergence that resolved into the 07-31 gap. This is the strongest cautionary evidence that 340 may be an intermediate top rather than a pause.

---

## 8. Volatility & the Bollinger Envelope

- **ATR 7.633** = **2.47% of price**. It peaked at 9.872 on 07-31 (post-gap) and has compressed to 7.63, though still above the pre-shock ~8.0 baseline read. **Volatility is normalizing but has not fully reset.**
- **Bollinger:** mid 314.339, upper 338.856, lower 289.821 → **bandwidth 49.03 pts = 15.6% of the midline.** That is an extremely wide envelope; the 2σ bands are currently useless as reversal triggers but excellent as a *range map*.
- **Price position within the bands:** (309.35 − 289.82) / (338.86 − 289.82) = **39.8%** — lower-middle of the envelope. No mean-reversion signal at either extreme.
- **Band dynamic:** the upper band is falling fast (347.26 on 08-12 → 338.86) while the lower band has flattened (295.18 → 289.82, then flat for four sessions). This is the envelope "closing in from above" — the signature of a volatility contraction building toward a range resolution.

**Practical consequence:** with ATR at 7.63, a 1.5×ATR stop is ~11.5 points and a 2×ATR stop is ~15.3 points. Any stop tighter than ~1 ATR (±7.6) inside this range will be noise-stopped; the 08-19→08-21 swing alone was 13.3 points (320.28 → 307.01).

---

## 9. Volume & Participation — Where Real Positioning Sits

**VWMA at 308.804 vs close 309.35 → price is +0.18% above it.** The VWMA series has *flattened* (307.765 on 08-19 → 308.415 → 308.804) after a persistent decline from 329.58 (07-30). Read: **the volume-weighted cost basis of recent buyers is ~$308.8, essentially at the market.** Holders are at breakeven, which typically produces a decision point — either support (reluctance to sell at breakeven) or supply (relief selling on any bounce). The fact that price is holding marginally *above* it is a mild point for the bulls.

**Volume character since the shock:**
- 132.5M (07-31, capitulation) → 75.1M (08-03) → decaying to **28.2M on 08-14** (the lowest of the sequence) → **50.5M on 08-19's rally** → 41.0M / 46.9M on the two down days. Selling pressure has visibly dried up versus the shock week; the 08-19 up-move attracted the best relative participation since the break. Volume on 08-21 (46.9M) was ~0.88x my computed ~53M 20-session average — unremarkable, i.e., **the pullback was not distribution-heavy.**
- Notable historical volume events for context (not current signals): 261.8M on 2026-06-26, 144.6M on 2025-12-19, 163.7M on 2025-09-19 — all consistent with index/rebalance or event dates rather than technical breakouts.

---

## 10. Key Levels — A Confluence Map

### Resistance (overhead, in order)
| Level | Source | Significance |
|---|---|---|
| **310.21** | 50 SMA | First line; price closed 0.28% below |
| **310.35** | 10 EMA | Overlapping cluster with the 50 SMA |
| **310.69** | 07-31 gap high | **The pivot.** Reclaiming this reopens the void above |
| **312.38 / 314.34** | 08-21 high / Bollinger mid | First real supply shelf |
| **316.29–316.83** | 08-06 high / 08-19 close | Prior reaction high |
| **319.28–320.28** | 08-19 high / 08-20 high | Range top; the ceiling that failed |
| **329.59** | 07-30 low | Bottom of the unfilled gap's upper structure |
| **338.86 / 340.08** | Boll upper / 07-28 peak close | Full gap fill / prior high |

### Support (below, in order)
| Level | Source | Significance |
|---|---|---|
| **308.80** | VWMA | Volume-weighted breakeven; price barely above |
| **307.01** | 08-21 low | Immediate invalidation for a bounce attempt |
| **305.59–305.93** | 08-17 / 08-14 closes | Last higher-low shelf before the range floor |
| **300.57–302.25** | 08-12 low/close | Range floor; also 07-31 low 300.00 |
| **289.82** | Bollinger lower | Deeper mean-reversion target |
| **281.50** | 200 SMA | Primary trend line — a break here changes the thesis entirely |

---

## 11. Actionable Scenarios With Explicit Triggers

### Scenario A — Bullish repair (probability-weighted as the higher-quality setup)
**Trigger:** a daily close **above $312.40** (clears 08-21's high and the 310.2–310.7 cluster decisively), confirmed by MACD crossing above its signal (−1.19) and RSI pushing through 55.
- **First target:** 316.3–316.8. **Second:** 319.3–320.3. **Stretch:** 329.6 (gap fill).
- **Entry logic:** prefer buying the *reclaim of 314.34 (Boll mid)* on above-average volume over anticipating it — the 08-20 rejection at 320.28 shows how quickly this market punishes front-running.
- **Stop:** below 305.5 (≈1.6× ATR from a 314 entry) or 1.5× ATR trailing (≈11.5 pts).
- **Risk note:** the 07-31 distribution candle means the first push into 316–320 should be assumed to be sold until proven otherwise.

### Scenario B — Range continuation (base case)
**Trigger:** price continues oscillating between 300 and 320 with ATR compressing further.
- **Tactic:** fade extremes, not the middle. Buy 302–305 with a stop under 299.5; trim into 316–320. Do **not** add size in the 309–311 no-man's-land where the averages, gap lip, and VWMA all collide.

### Scenario C — Breakdown
**Trigger:** a daily close **below $305.59** (08-17 close) with volume above ~60M, and especially below 300.57–302.25.
- **Targets:** 289.82 (Boll lower), then 281.50 (200 SMA).
- **Confirmation required:** MACD making a fresh low below −2.68, RSI breaking 40.22 (its August trough).
- **Stop:** above 312.4 (back inside the cluster).

### Position-sizing math (uses only verified ATR)
ATR = 7.633 → 1 ATR ≈ 2.47% of price. For a $10,000 risk budget:
- 1.5×ATR stop (11.45/share) → ~873 shares notional ≈ $270k exposure.
- 2×ATR stop (15.27/share) → ~655 shares ≈ $203k exposure.
Given the unfilled gap and event-driven volatility (07-31 was a 7.4% one-day move), I would size to the **2×ATR** column and no tighter.

---

## 12. Divergences, Inconsistencies, and Honest Caveats

1. **Signal conflict, stated plainly:** The *trend* signals (price vs 200 SMA, 50>200 spread) are bullish; the *momentum* signals (price below 10 EMA/50 SMA/Boll mid, MACD < 0 and < signal, RSI < 50) are bearish. This is definitionally a range/transition market. Anyone claiming a clean directional read here is overselling their confidence.
2. **No tool output supports a claim of a "support bounce."** The August lows at 300.57/302.25 were *followed* by a rally, but I have no evidence of repeated tests-and-holds at a single level; treat 300–302 as a zone, not a proven floor.
3. **Bullish-divergence counterpoint:** while July showed a bearish RSI divergence into the top, August has not yet produced a *bullish* divergence at the lows (RSI bottomed at 40.22 on 08-12 with price at its low — coincident, not divergent). The oscillator has room to go lower without conflicting with price.
4. **Gap behavior is unverified beyond observation.** The 310.69–329.59 void exists as arithmetic from the 07-30/07-31 rows. Its future *fill* is a scenario, not a forecast.
5. **MFI excluded** (scale ambiguity at 0.5988). **No fundamental/newsflow data was retrieved**, so any event explanation for the 07-31 gap is outside what these tools support — I have deliberately not invented one.
6. **All percentage figures above are computed directly from tool rows** and are tied to the stated dates; none are rounded-in generalities.

---

## 13. Summary Table

| Dimension | Reading (2026-08-21) | Evidence | Implication |
|---|---|---|---|
| **Primary trend** | Bullish, intact | Close 309.35 vs 200 SMA 281.50 (+9.9%), 200 SMA rising every session from 268.49 (06-22) | Dips are counter-trend; thesis only breaks <281.50 |
| **Intermediate trend** | Transition / range | 50 SMA flat for 10 sessions (309.08–310.21); price −0.28% below it | Trend stall, not rollover; range $300–$320 |
| **Short-term trend** | Weak, stabilizing | Close below 10 EMA (310.35) and Boll mid (314.34); 10 EMA has flattened | No momentum buy signal; watch for reclaim |
| **Regime event** | 07-31 distribution gap | 333.43 → 308.91 (−7.36%) on 132.5M vs ~53M avg; gap 310.69–329.59 unfilled | Major supply overhead; caps upside until reclaimed |
| **Momentum (MACD)** | Negative but decelerating | MACD −1.574 < signal −1.194; histogram −2.290 (08-17) → −0.380 (08-21) | Exhaustion building; **no** crossover yet |
| **Momentum (RSI)** | Neutral | 47.28; trough 40.22 (08-12), peak 53.85 (08-19); July bearish divergence 71.65→68.90 vs 333.74→340.08 | No oversold springboard, no overbought headwind |
| **Volatility** | Elevated, contracting | ATR 7.633 (2.47% of price) vs 9.872 (07-31); Boll width 49.03 (15.6% of mid) | Size to 2×ATR (~15.3 pts); expect range resolution |
| **Participation** | Balanced at cost basis | Close 309.35 vs VWMA 308.80 (+0.18%); VWMA flat 3 sessions | Marginal buyer at breakeven = pivot point |
| **Immediate pivot** | **$310.69** (gap lip) + 310.2–310.4 (50 SMA/10 EMA) | Confluence of three references | Decisive close above = Scenario A; rejection = range |
| **Bull trigger** | Close > 312.40, then >314.34 | MACD > −1.19 + RSI >55 as confirmation | Targets 316.8 → 320.3 → 329.6 |
| **Bear trigger** | Close < 305.59, then < 300.57 | Needs volume >60M + MACD < −2.68 + RSI <40.22 | Targets 289.82 → 281.50 |
| **Preferred action** | **Wait/selective** | Conflicting trend vs momentum; price at ATR-defined no-man's-land | Trade the edges of 300–320; avoid the 309–311 middle |
| **Overall stance** | Neutral-to-constructive | Long-term structure up, intermediate structure damaged | Longs need 314.34 reclaim; avoid shorts against a rising 200 SMA |