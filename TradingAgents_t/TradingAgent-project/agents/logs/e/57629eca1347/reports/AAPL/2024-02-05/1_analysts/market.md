# AAPL — Technical & Trend Assessment (as of Monday, 2024-02-05)

**All price/indicator figures below are taken from the verified snapshot for 2024-02-05 or from the indicator history computed on the frozen OHLCV series. % figures are my arithmetic on those tool values.**

---

## 1. Market Context: Broadly Bullish, Medium-Term Deteriorating, Short-Term Choppy

AAPL closed at **187.68** on 2024-02-05 (open 188.15, high 189.25, low 185.84, volume 69.67M). The structure is best described as a **long-term uptrend that has lost its medium-term impulse and is now oscillating in a corrective range**. Three facts anchor this:

1. **The 200-day SMA is rising and firmly below price.** close_200_sma = **182.59**, up from 176.10 on 2023-12-07 (+3.7% over ~2 months). Price is **+2.79% above** it.
2. **The 50-day SMA has rolled over and price is below it.** close_50_sma = **190.59**, which peaked at **190.93 on 2024-01-30** and has ticked down for four consecutive sessions. Price is **−1.53% below** the 50-SMA.
3. **The 50/200 relationship is still bullish (golden-cross configuration).** The 50-SMA exceeds the 200-SMA by **~8.00 points (4.4%)**. That spread is *narrowing* (the 50 is falling while the 200 keeps rising), which is the classic early signature of a trend transition rather than a confirmed reversal.

So: the primary trend (200-SMA) is intact, the intermediate trend (50-SMA) has turned neutral-to-down, and the short-term swing structure is a lower-highs sequence off the late-January peak.

---

## 2. Selected Indicators and Why

| # | Indicator | Role in this specific setup |
|---|---|---|
| 1 | **close_200_sma** (182.59) | Defines the strategic regime. Distinguishes "pullback inside an uptrend" from "trend break." |
| 2 | **close_50_sma** (190.59) | Captures the medium-term inflection; its rollover on 2024-01-30 is the single most important structural change. |
| 3 | **close_10_ema** (188.38) | Short-term timing/execution line — shows whether the bounce has genuine short-term momentum. |
| 4 | **macd** (−0.448) | Measures mid-cycle momentum; identifies the regime shift from the January impulse. |
| 5 | **macds** (−0.050) | Needed to date the crossover and to judge whether the bearish cross is fresh (fragile) or mature. |
| 6 | **rsi** (47.30) | Momentum oscillator to gauge whether the January bounce ever reached impulse strength (it did not). |
| 7 | **atr** (3.57) | Position sizing and stop placement — critical here because volatility has expanded post-2024-02-01. |
| 8 | **vwma** (189.18) | Volume-weighted confirmation: are buyers or sellers "winning" on a dollar-weighted basis? |

**Deliberately excluded:** `boll`/`boll_ub`/`boll_lb` (used only as secondary context below — the 50-SMA and 10-EMA already cover dynamic mean-reversion levels, so adding a third mean would be redundant), `macdh` (the MACD/signal pair already encodes the same information), and `mfi` (the snapshot's raw value of 0.5209 is on an unnormalized 0–1 scale, so it is not directly comparable to a 0–100 threshold — I chose not to build a claim on it).

---

## 3. Indicator-by-Indicator Evidence

### 3.1 Moving average stack — bearish short-term, bullish long-term (compression)
- Price **187.68** vs 10-EMA **188.38** vs Bollinger mid **188.48** vs VWMA **189.18** vs 50-SMA **190.59** vs 200-SMA **182.59**.
- Price sits **below every short/medium-term average** and **above only the 200-SMA**. That is a textbook corrective profile inside a primary uptrend.
- The **10-EMA is falling** (peak 191.41 on 2024-01-29 → 188.38 on 2024-02-05), but the gap between close and 10-EMA has **narrowed from −1.27 (Feb 1) to −0.70 (Feb 5)** — downside momentum is decelerating rather than accelerating.
- **Stack order is not clean:** 10-EMA (188.38) is *below* the 50-SMA (190.59) but *above* the 200-SMA. This "tangled" stack is the mathematical signature of a range, not of a trending market — which is why moving-average crossover signals have been unreliable here (see MACD section).

### 3.2 MACD — fresh bearish crossover, but whipsaw-prone
- macd: **−0.4478** | macds: **−0.0504** | macdh: **−0.3974**.
- The MACD line **peaked at +0.951 on 2024-01-26** and has fallen monotonically to −0.448 — a **1.40-point collapse in seven sessions**.
- The **bearish crossover occurred between 2024-01-31 (MACD +0.091 vs signal +0.235) and 2024-02-01 (MACD −0.138 vs signal +0.160)**. That is a *very fresh* cross — only four sessions old.
- Histogram: −0.143 (Jan 31) → −0.298 → −0.445 → **−0.397 (Feb 5)**. The histogram has stopped making lower lows, i.e. the *rate* of deterioration is easing. This is consistent with a pause/bounce attempt, not a fresh breakdown impulse.
- **Whipsaw warning — this is important:** the *bullish* crossover that this bearish cross just reversed happened only on **2024-01-19** (MACD −1.026 vs signal −1.228). That bullish phase lasted roughly **8–9 trading days**. Before that, the MACD spent 2024-01-04 through 2024-01-18 negative and deeply oversold (minimum −1.926 on Jan 17). A MACD that produced a full bull-to-bear flip in under two weeks is a **low-quality signal generator in the current regime** and must be filtered by price structure.

### 3.3 RSI — neutral, and revealingly so
- RSI **47.30** — dead center of the range.
- The more informative facts are the *extremes it failed to reach*: RSI bottomed at **28.79 on 2024-01-05** (oversold), then rallied for over two weeks but **topped out at only 62.62 on 2024-01-23**. It never reached 70.
- **Interpretation:** the January advance was a *mean-reversion recovery*, not a new momentum impulse. Sellers were never forced out. This raises the odds that the 2024-01-24 high (196.38) is a lower-high cap rather than a stepping stone.
- Current RSI 47.3 with price below the 50-SMA means there is **no oversold cushion**; there is room to fall to ~35 without any "cheap" signal firing (as happened on 2024-01-02–01-05).

### 3.4 ATR — volatility expanding; size down
- ATR **3.574**, up from **2.575 on 2023-12-29** (+39% over ~5 weeks) and from 3.130 on 2024-01-29.
- ATR = **1.90% of the close**. The **2024-02-02 session alone ranged 179.25–187.33 = 8.08 points, roughly 2.25× that day's ATR** — an outlier expansion day.
- Practical consequence: stops tighter than ~1 ATR (≈3.6 points) are statistically likely to be noise-stopped. A 1.5×ATR stop is ≈**5.36 points**.

### 3.5 VWMA — sellers hold the volume-weighted edge
- VWMA **189.18** vs close **187.68** → price is **−0.79% below** the volume-weighted average.
- VWMA has **flattened**: 185.25 (Jan 18) → 189.40 (Jan 30) → **189.18 (Feb 5)**. The January accumulation impulse has stalled out; the volume-weighted "true cost basis" of recent buyers is now *above* spot, i.e. recent buyers are underwater and are latent supply on rallies into 189.1–189.4.
- **Volume anomaly worth flagging:** 2024-02-02 volume was **102.55M**, versus a ~**57.5M** average over the prior 20 sessions (my calculation from the CSV) — roughly **1.8×**. That day opened at 179.86, printed a low of 179.25, and closed at 185.85: a **large-volume, long-lower-wick reversal session** that recovered ~6.6 points off the low. 2024-02-05 followed with 69.67M and a close above the prior close (187.68 > 185.85). *Constructively*, that looks like demand absorbing a catalyst-driven flush (the gap coincides with Apple's fiscal-Q1 report cycle — event context, not a tool-derived claim).

### 3.6 Bollinger context (secondary, from the verified snapshot)
- Middle **188.48** | Upper **196.46** | Lower **180.50** | width **15.96 pts = 8.47%** of the midpoint.
- Bands are **compressing**: on 2024-01-08 width was **21.50 pts (11.19%)**. Upper band has fallen 202.95 → 196.46 while the lower band has risen 178.19 → 180.50.
- Price is **just below the middle band** — mild bearish bias *within* a contracting range. A squeeze of this magnitude typically resolves in a directional expansion; the resolution level, not the oscillator, should drive the trade.

---

## 4. Key Levels (all derived from tool data)

**Resistance (ascending):**
1. **188.38–188.48** — 10-EMA + Bollinger middle (immediate; will be tested first)
2. **189.18–189.25** — VWMA + 2024-02-05 high (the real gate)
3. **190.59** — 50-SMA (the trend-repair line)
4. **191.73–191.95** — 2024-01-29 close / 2024-01-19 high
5. **194.50–196.46** — Jan 23–25 congestion + Bollinger upper band
6. **198.11 / 199.62** — 2023-12-14 close / high (highest in the visible series)

**Support (descending):**
1. **185.84–185.85** — 2024-02-05 low / 2024-02-02 close
2. **184.35–184.40** — 2024-01-31 low and close
3. **182.59** — 200-SMA (strategic line in the sand)
4. **180.17–180.50** — 2024-01-05 low / 2024-01-17 low (180.30) / Bollinger lower band (180.50) → a genuine confluence shelf
5. **179.25** — 2024-02-02 low (the flush low; a break invalidates the absorption thesis)

---

## 5. Actionable Framework

**Bias: NEUTRAL-to-CAUTIOUSLY-BEARISH on the 1–3 week horizon; structurally BULLISH on the 3–6 month horizon.** The 200-SMA and rising long-term average argue against aggressive shorting; the 50-SMA rollover, sub-70 RSI ceiling, and fresh MACD cross argue against chasing longs at 187.7.

**Scenario A — Base case (≈45%): continued chop between 184.3 and 190.6.**
Confirmation: price holds 185.84–184.35, MACD histogram stays flat-to-slightly-negative, ATR stays ~3.5. Action: **no directional position**; treat 188.4–190.6 as a place to trim/reduce longs and 184.3–185.8 as a scale-in zone only for investors with a 200-SMA-based thesis.

**Scenario B — Bullish repair (≈30%): reclaim of 189.2–190.6.**
Triggers: two consecutive closes **above the VWMA (189.18) and then the 50-SMA (190.59)**, with the 10-EMA turning back up and the MACD histogram crossing back above zero. Action: **long with entry on the retest of 188.4–189.2, stop below 185.80 (−1.6% to −1.9%)**, first target 191.7–192.0, second target 194.5–196.4. Note the reward/risk at spot is poor (≈0.85:1 to the 50-SMA), which is precisely why waiting for the reclaim rather than buying the print is the higher-expectancy approach.

**Scenario C — Trend break (≈25%): loss of 184.35 and then 182.59.**
Triggers: a **daily close below 182.59 (200-SMA)**, MACD making a new low below −0.72 (the Jan 17 trough on the histogram was −0.73; MACD itself −1.93), and expansion back above ~4.0 ATR. Action: short with stop above 186.5 (1×ATR) or above 188.4 for a wider leash; targets 180.5 (Bollinger lower) and 179.25. A close below 180.17–179.25 would target **176.10**. **Caveat: this would be a short into a rising 6-month 200-SMA — reduce size accordingly.**

**Execution rules dictated by this specific tape:**
- **Stop distance minimum: 1×ATR = 3.57 pts (1.90%).** Preferred 1.5×ATR = 5.36 pts. Do not use stops tighter than ~1.8 pts — the 2024-02-02 session alone spanned 8.08 points.
- **Halve normal position size** relative to a trending regime: ATR is +39% from 2023-12-29 while the moving-average stack is tangled. Two whipsaw MACD crossovers in three weeks is a regime filter telling you to size down, not to add.
- **Do not fade the 189.2–190.6 band without confirmation.** The VWMA + 50-SMA + Bollinger-mid cluster is dense; a single intraday spike through it is noise, a close above it is a signal.
- **Watch 2024-02-02's 102.55M-volume session as the reference "capitulation candle."** As long as 179.25 holds, the absorption read stands; a close below 179.25 invalidates the entire constructive case and effectively completes the Bollinger squeeze to the downside.

---

## 6. Summary Table

| Dimension | Reading (2024-02-05) | Signal | Evidence / Notes |
|---|---|---|---|
| Close | **187.68** | — | O 188.15 / H 189.25 / L 185.84 / Vol 69.67M |
| close_200_sma | **182.59** (rising from 176.10 on 2023-12-07) | **Bullish (primary)** | Price +2.79% above; intact long-term uptrend |
| close_50_sma | **190.59** (peak 190.93 on 2024-01-30, now 4 sessions down) | **Bearish (intermediate)** | Price −1.53% below; gold cross intact but spread narrowing to ~8.00 pts |
| close_10_ema | **188.38** (peak 191.41 on 2024-01-29) | **Bearish, decelerating** | Gap to price narrowed −1.27 → −0.70 in 2 sessions |
| macd / macds | **−0.4478 / −0.0504** | **Bearish, fresh** | Bearish cross on/around 2024-02-01; MACD fell 1.40 pts from its 2024-01-26 peak (+0.951) |
| macdh | **−0.3974** (from −0.4449) | Slightly improving | 4th negative bar but no longer making lower lows |
| rsi | **47.30** | **Neutral** | Jan bounce capped at 62.62 (2024-01-23); never overbought → weak impulse |
| atr | **3.574** (1.90% of price; +39% vs 2023-12-29) | **Volatility expanding** | 2024-02-02 range 8.08 pts = ~2.25× ATR |
| vwma | **189.18** (flattening from 189.40 on 2024-01-30) | **Bearish (mild)** | Price −0.79% below; volume-weighted sellers retain edge |
| Bollinger (context) | Mid **188.48** / UB **196.46** / LB **180.50**; width **8.47%** vs **11.19%** on 2024-01-08 | **Squeeze / Range** | Contracting range; resolution likely directional |
| Volume (context) | **102.55M on 2024-02-02** (~1.8× the ~57.5M 20-session avg) | **Constructive** | Long lower wick, low 179.25, close 185.85; demand absorbed the flush |
| Key resistance | **188.4 → 189.2 → 190.6 → 191.9 → 196.4** | — | 10EMA/Boll-mid → VWMA/Feb-5 high → 50SMA → Jan-19 high → Jan congestion/Boll-UB |
| Key support | **185.85 → 184.35 → 182.59 → 180.2–180.5 → 179.25** | — | Feb-5 low → Jan-31 low → 200SMA → Jan lows/Boll-LB confluence → flush low |
| Net stance | **Neutral-to-cautious-bearish (short term); bullish (long term)** | — | Prefer fade-and-wait over chasing; halve size until ATR contracts or the 50-SMA is reclaimed |

**Disclaimer:** These are technical observations from a point-in-time frozen dataset, not a recommendation to transact. No claim of historical strategy validation is made — the January MACD bull/bear flip in ~9 sessions is cited specifically as evidence that crossover signals in this regime have been unreliable.