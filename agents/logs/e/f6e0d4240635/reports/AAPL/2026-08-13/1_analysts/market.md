# AAPL — Multi-Timeframe Technical Report
**As of close 2026-08-13 | Reference price: $305.26**

---

## 1. Verified Data Anchor (source of truth)

From the verified snapshot for 2026-08-13:

| Field | Value |
|---|---|
| Open / High / Low / Close | 304.21 / 306.00 / 302.05 / **305.26** |
| Volume | 40,349,300 |
| 50-SMA | 309.277 |
| 200-SMA | 280.298 |
| 10-EMA | 310.243 |
| MACD / Signal / Hist | -2.186 / 0.849 / **-3.035** |
| RSI(14) | 43.04 |
| Bollinger (mid / UB / LB) | 319.819 / 346.139 / 293.499 |
| ATR | 8.220 |
| VWMA | 315.806 |
| MFI | 0.5015 |

The full OHLCV pull and the snapshot agree on every row I checked (e.g., 07-31 close 308.91, 08-13 close 305.26), so there is **no tool conflict to flag**. The Bollinger midpoint I computed from the upper/lower bands ((346.139+293.499)/2 = 319.819) matches the snapshot exactly. Note the snapshot's MFI value of 0.5015 is on a 0–1 scale, i.e. ~50.2 on the conventional 0–100 scale — neutral, and not a reading I rely on below.

One data nuance: the 2026-08-10 row carries a **$0.27 dividend** (ex-date). The -5.07 point decline that session (313.33 → 308.26) is therefore overwhelmingly price action, not the dividend; do not attribute the drop to the payout.

---

## 2. Why these eight indicators

The market context is **a high-volume trend break inside a still-intact long-term uptrend** — the hardest kind of tape, because trend-following and mean-reversion signals point in opposite directions. I chose indicators that separate those two questions rather than blend them:

1. **close_200_sma** – defines whether the primary trend is still up (strategic anchor).
2. **close_50_sma** – the level price just lost; the battleground for the medium-term trend.
3. **close_10_ema** – short-term momentum and the fastest objective trigger.
4. **macd** – regime change via the zero-line cross (more decisive here than a signal-line cross, which already happened).
5. **rsi** – measures how much downside energy is spent; also documents the negative divergence into the July top.
6. **boll_ub** – marks the stretched July extreme (346.68 on 07-23/24) that now sits as a ceiling.
7. **boll_lb** – defines the downside envelope; currently dominant because volatility is expanding downward.
8. **atr** – mandatory here: post-gap volatility is elevated, so stop distance and size must scale.

**Deliberately excluded:** `macds`/`macdh` (derivable from `macd`; the snapshot already gives them), `boll` middle (implied by the two bands; used for %B), and `vwma` — I reference VWMA below only as a cross-check from the verified snapshot rather than as one of the eight selections.

---

## 3. Three timeframes, three different answers

### Long-term (200-SMA): still bullish, unambiguously
- Price 305.26 vs 200-SMA **280.298** → **+8.90% above**.
- The 200-SMA is rising every session (267.20 on 06-15 → 280.30 on 08-13), roughly +13 points in two months.
- 50-SMA (309.28) is **28.98 points (10.3%) above** the 200-SMA — a healthy golden-cross configuration with a wide spread, i.e., the primary uptrend has not been structurally damaged.
- **Implication:** shorting this is counter-trend at the primary degree. Any bearish trade is a swing trade, not a position trade.

### Medium-term (50-SMA): the trend has flattened and price is underneath it
- Price is **below** the 50-SMA by 4.02 points (**-1.30%**).
- The 50-SMA has stopped rising: peak 309.786 (08-07) → 309.700 → 309.557 → 309.476 → **309.277** (08-13). It is curling over, not yet falling hard. This is the classic "medium-term trend rolling from up to sideways."
- The break was driven by a single session: 07-30 close 333.43 → **07-31 open 304.81, low 300.00, close 308.91 on 132.49M shares**. Every close since 07-31 (308.91, 303.42, 309.38, 311.00, 312.41, 313.33, 308.26, 304.91, 302.25, 305.26) has been **below** the 50-SMA. That is ten consecutive closes on the wrong side — a persistent loss, not a one-day wick.

### Short-term (10-EMA): downtrend, but decelerating
- Price is 4.98 below the 10-EMA (**-1.61%**). The 10-EMA has collapsed from 331.31 (07-30) to 310.24 (08-13).
- Crucially, the *rate* of decline is slowing. Daily changes in the 10-EMA: -1.554 (08-10), -1.881 (08-11), -2.022 (08-12), **-1.107 (08-13)**. The slope is losing force.
- The last eight sessions form a **range of roughly 300.5–316.3** (08-12 low 300.57 to 08-06 high 316.29) — a base, but a base *below* the 50-SMA, which makes it neutral-to-distributive until proven otherwise.

---

## 4. Momentum: negative, but not capitulating

**RSI = 43.04.** Context matters more than the level:
- July peak **71.65 (07-17)** — overbought.
- Collapsed to **40.34 (08-03)** after the gap, bounced to 47.58 (08-07), faded to **40.22 (08-12)**, and ticked up to 43.04.
- So RSI has now made a **lower low in momentum (40.22 on 08-12 vs 40.34 on 08-03) while price made a roughly similar-to-higher low** (302.25 close vs 303.42 close). That's a marginal *positive* divergence worth monitoring, not a signal on its own.
- 43 is **not oversold**. There is room for another leg down before RSI reaches 30. Anyone buying this dip is buying "neutral momentum," not "washed-out momentum."

**Documented negative divergence into the top** (fully supported by tool output):
- RSI made a **lower high**: 71.65 on 07-17 vs 68.90 on 07-28.
- Price made a **higher high**: 333.74 close on 07-17 vs 340.08 close on 07-28.
- That is a textbook bearish momentum divergence that preceded the 07-31 break — evidence the break was a *resolution* of deteriorating internals rather than a random shock.

**MACD = -2.186, Signal = 0.849, Histogram = -3.035.** This is the cleanest bearish fact in the set:
- MACD crossed **below zero between 08-10 (+0.072) and 08-11 (-0.827)** and kept falling to -2.186. Zero-line crosses are regime markers, not noise.
- The signal line (0.849) is still *positive* and above the MACD line — the histogram is deeply negative at -3.035. Both lines are headed down; the bearish crossover is already complete.
- Nuance: the MACD's daily decline is decelerating — -0.899 (08-10→08-11), -0.907 (08-11→08-12), **-0.451 (08-12→08-13)**. Momentum is still negative but no longer accelerating. Because I only have same-day signal values, I will not claim the histogram is narrowing day-over-day; the MACD deltas merely make that the leading hypothesis.

---

## 5. Volatility structure: an unusually lopsided Bollinger envelope

- Bollinger upper **346.139**, lower **293.499**, mid **319.819**. Bandwidth is **16.46% of the midpoint** — very wide (normal for this instrument is materially tighter), reflecting the 07-31 gap.
- The envelope is behaving asymmetrically: the **upper band has been essentially flat (346.34 → 346.14) since 07-29**, while the **lower band has collapsed from 304.16 (07-30) to 293.50 (08-13)**. That downward migration means realized volatility is being generated on the downside.
- **Position in the band (%B) = 0.223.** Price sits ~22% of the way up from the lower band and **4.55% below the 20-day midpoint (319.82)**. The midpoint is overhead resistance and a magnet — the market is trading in the lower third of its own range.
- **ATR = 8.220**, down from a post-gap peak of 9.872 (07-31), and up from 8.06 (07-30). ATR is **2.69% of price**. Translation: one average day is ±8.2 points, and a normal two-day adverse excursion is ~16 points. Any stop tighter than ~1.5×ATR (≈12 points) in this tape is a coin flip.

**Actionable risk math:** 2×ATR = **16.44 points**. On a $100k notional account risking 1% ($1,000), a 2×ATR stop implies roughly **61 shares** (~$18.6k exposure). The elevated ATR argues for *smaller* size, not tighter stops.

---

## 6. Volume / participation: sellers spent, buyers not yet committed

- **07-31 volume = 132,489,100**, versus a **22-session average (07-15 → 08-13) of ≈55.1M** — approximately **2.4×** normal. This was a genuine distribution/repricing event, not a thin drift.
- Volume has since **dried up**: the last five sessions (08-07, 08-10, 08-11, 08-12, 08-13) average **≈39.7M**, roughly **28% below** the 22-session average. That pattern — climactic volume, then contraction while price holds a range — is consistent with *seller exhaustion*, but it is equally consistent with *absence of demand*. It is not yet a buy signal.
- **VWMA = 315.806** (from verified snapshot). Price is **3.34% below** the volume-weighted average price of the recent window. This is important: the bulk of recent volume transacted above current price, so the **average recent participant is underwater**, and 315.81–316.29 is where supply is likely to appear.
- Precedent worth noting, factually: the 06-25/06-26 episode also saw a violent high-volume flush (107.0M then **261.8M** shares; close 293.08 → 275.15 → 283.78). Price subsequently rallied from the 06-26 close of 283.78 to **340.08 on 07-28 (+19.8%)**. High-volume flushes in this name have resolved higher — but that is history, not a prediction, and the current setup differs: this time price is *below* the 50-SMA, whereas in late June it was above it.

---

## 7. Levels map (all from tool output, with dates)

**Resistance (overhead, in order):**
| Level | Source |
|---|---|
| 309.28 | 50-SMA (2026-08-13) |
| 310.24 | 10-EMA (2026-08-13) |
| 310.69 | 07-31 high — bottom edge of the unfilled gap |
| 313.33 / 314.81 | 08-07 close / 08-07 high |
| 315.81 | VWMA |
| 316.29 / 316.53 | 08-06 high / 07-09 high |
| 319.82 | Bollinger mid (20-day) |
| 329.59 → 310.69 | **Unfilled gap zone** (07-30 low to 07-31 high); price has retraced **none** of it |

**Support (below, in order):**
| Level | Source |
|---|---|
| 302.05 | 08-13 low |
| 300.57 | 08-12 low |
| 300.00 | **07-31 low — the pivotal level** |
| 293.50 | Bollinger lower band (2026-08-13) |
| 280.30 | 200-SMA (2026-08-13) |
| 275.15 / 273.75 | 06-25 close / 06-25 low |

The 300.00–302.05 shelf has been touched on 07-31 (low 300.00), 08-03 (low 302.56), 08-12 (low 300.57), and 08-13 (low 302.05). Four tests, holding so far. **300 is the line that separates "correction" from "trend change."**

---

## 8. Actionable scenarios

**Regime verdict: neutral-to-bearish short term, bullish long term — a "reduce, don't reverse" tape.** Price is below the 50-SMA, 10-EMA and VWMA, MACD is below zero, and RSI has room to fall. But price is 8.9% above a rising 200-SMA and 4.0% above the lower Bollinger band, so downside is not open-ended.

**Scenario A — Base breakout (long, tactical).**
- Trigger: **daily close above 310.30** (clears both the 10-EMA 310.24 and 50-SMA 309.28), confirmed by volume **>55M** (i.e., back above the 22-session average).
- Targets: **313.4 → 315.8 (VWMA) → 319.8 (Boll mid)**. A close above 319.8 opens the 329.6–310.7 gap fill.
- Stop: **close below 299.50** (under the 07-31 low). From a 310.3 entry that's ~10.8 points ≈ **1.3×ATR** — acceptable but tight; a 2×ATR stop (≈16.4) implies a 294 stop, just above the lower band.
- Rationale chain: volume contraction + 10-EMA slope flattening + marginal RSI higher low all support a bounce attempt; the moving-average cluster gives a clean, low-cost invalidation.

**Scenario B — Range fade (short-avoidance / trim zone).**
- The 309–316 zone is where the underwater volume sits. If price rallies into **313–316 without volume expansion**, that is a **reduce/hedge** zone, not a chase zone. Confirmation of failure: MACD histogram stays negative while price makes a higher high.

**Scenario C — Breakdown (short, counter-trend, small size).**
- Trigger: **daily close below 299.50** with volume **>55M**.
- Targets: **293.5 (lower band) → 280.3 (200-SMA)**.
- Stop: back above **305.5** (reclaim of today's close) or 310.3 for a wider stop.
- Caveat: this fights a rising 200-SMA; keep size at half normal and treat it as a swing, not a position.

**Scenario D — Do nothing (explicitly valid).** Between 300 and 309 the risk/reward is poor in both directions: no trend confirmation up (below 50-SMA), no breakdown trigger down (holding 300). The 40M-share volume suggests the market agrees — waiting for the range to resolve at 300 or 310.3 is the highest-expectancy choice.

**Invalidation watch-list:**
- **Bullish repair** requires: close >310.3 *and* MACD back above zero *and* price reclaiming VWMA 315.8.
- **Bearish escalation** requires: close <300.0 on >55M volume, which would put the 200-SMA at 280.30 (~-8.1% from here) in play.
- **Neutrality persists** while RSI stays in 40–50 and price stays inside 300–313.

---

## 9. Key points summary

| Dimension | Reading (2026-08-13) | Interpretation | Actionable level |
|---|---|---|---|
| Primary trend (200-SMA) | 280.30, rising; price +8.90% above | Bullish, undamaged | Trend-break risk only below 280.30 |
| Medium trend (50-SMA) | 309.28, curling over (peak 309.79 on 08-07); price -1.30% below | Weakening; 10 straight closes below | Reclaim >310.30 needed |
| Short trend (10-EMA) | 310.24, falling but decelerating (-2.02 → -1.11/day) | Downtrend losing force | Trigger level 310.30 |
| MACD | -2.19 / signal 0.85 / hist -3.04; zero-cross on 08-11 | Bearish regime, decelerating | Back above 0 = repair |
| RSI | 43.04 (from 71.65 on 07-17; 40.22 on 08-12) | Neutral, NOT oversold; bearish divergence into top | 30 = capitulation, 50 = repair |
| Bollinger | UB 346.14 / mid 319.82 / LB 293.50; %B = 0.22; width 16.5% | Price in lower third; overhead mid | 319.82 resistance, 293.50 target |
| ATR | 8.22 (2.69% of price) | Elevated post-gap volatility | 2×ATR stop ≈ 16.4 pts; size down |
| Volume | 07-31: 132.5M ≈2.4× avg; last 5 sessions ≈39.7M (-28%) | Climactic sell, then demand vacuum | Confirmation needs >55M |
| VWMA (snapshot cross-check) | 315.81; price -3.34% below | Recent buyers underwater; supply overhead | 313–316 = distribution zone |
| Structure | Base 300.00–316.29; unfilled gap 310.69–329.59 | Correction within uptrend, unresolved | 300.00 = trend line in the sand |
| Stance | Neutral-to-bearish tactical / bullish strategic | Reduce, don't reverse | Buy trigger >310.30, sell trigger <299.50 |

*This is technical analysis based solely on the frozen data and indicator values retrieved above, not investment advice. Volatility is elevated (ATR 2.7% of price); position sizing should reflect that.*