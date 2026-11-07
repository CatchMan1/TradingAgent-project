# AAPL — Point-in-Time Technical Report (as of 2024-01-05)

**Ticker under analysis:** `AAPL` (Apple Inc.)
**Last visible session:** Friday, 2024-01-05 — data resolved from the verified snapshot.

---

## 1. Executive Summary

`AAPL` is in a **short-term downtrend inside an intact long-term uptrend**, arriving at the most consequential technical junction visible in the retrieved data. A fast, high-volume four-session decline (–5.89% from the 2023-12-29 close of 192.53 to 181.18) has:

1. Pushed price **below the 10 EMA (187.81), the 50 SMA (187.40), the Bollinger middle (192.64) and even below the Bollinger lower band (182.32)**.
2. Driven **RSI to 28.79** — the first sub-30 reading in the ~two-month indicator window retrieved.
3. Flipped **MACD below its signal line and below zero** (MACD –1.346 vs signal 0.699; histogram –2.045, the most negative print in the window).
4. Left price **resting almost exactly on the rising 200 SMA at 180.02**, with today's low at 180.17.

The setup is therefore **oversold-but-not-yet-stabilized**: momentum is still deteriorating, yet the reward/risk for initiating new short exposure *at* the 200 SMA, with RSI < 30, is poor. The trade is to react to the 180.02 support test, not to anticipate its outcome.

---

## 2. Verified Price Structure (source of truth: 2024-01-05 snapshot)

| Field | Value |
|---|---|
| Open | 181.99 |
| High | 182.76 |
| Low | 180.17 |
| **Close** | **181.18** |
| Volume | 62,379,700 |

**Recent close sequence (from snapshot):** 197.57 (12-15) → 195.89 → 196.94 → 194.83 → 194.68 → 193.60 → 193.05 → 193.15 → 193.58 → 192.53 (12-29) → **185.64 (01-02) → 184.25 (01-03) → 181.91 (01-04) → 181.18 (01-05)**

Key mechanical facts, all directly from tool output:

- **Unfilled gap:** the 2024-01-02 session opened at 187.15 against a 192.53 prior close (–2.79% gap) and printed a high of 188.44. Price has not traded back into **187.15–188.44** since. This is an open overhead gap.
- **Failed December breakout:** the highest print in the retrieved history is **199.62 on 2023-12-14** (close 198.11). From that high to today's low of 180.17 is **–9.74%**; close-to-close (198.11 → 181.18) is **–8.55%**.
- **Decelerating downside impulse:** daily closes have fallen –3.58%, –0.75%, –1.27% and **–0.40%** over 01-02 → 01-05, while today's session still made a *lower low* (180.17 vs 180.88). Deceleration of the decline with a lower low is an early exhaustion cue, **not** a reversal signal.
- **Volume confirms distribution:** the four down sessions transacted 82.49M + 58.41M + 71.98M + 62.38M = **275.3M shares**, versus 153.7M across the four prior sessions (12-26 → 12-29) — roughly **1.8× the volume** on the decline. 01-02's 82.49M is the heaviest session since 2023-12-15 (128.54M). Sellers, not drift, moved this tape.

---

## 3. Selected Indicators (8) and Why They Fit This Market Context

This is a **trend-breakdown-into-support** context, so the set is built around three questions: (a) where is the trend broken, (b) how stretched is momentum, (c) where is the risk boundary.

| # | Indicator | Latest value (2024-01-05) | Why it is included here |
|---|---|---|---|
| 1 | **close_200_sma** | **180.02** | The single most important level on the chart today: price (181.18) is +0.65% above it and today's low (180.17) is 0.15 above it. It defines the long-term trend and the line-in-the-sand for trend followers. |
| 2 | **close_50_sma** | **187.40** | Confirms the medium-term trend has broken and coincides almost exactly with the unfilled gap zone / 10 EMA — a high-confluence reclaim target. |
| 3 | **close_10_ema** | **187.81** | Fastest trend proxy; shows the short-term trend has rolled over and is shedding ~1.6 points/session. Stacked with the 50 SMA inside the gap zone. |
| 4 | **macd** | **–1.346** | Measures the momentum regime shift; crossed below its signal on 2023-12-20 and below zero on 2024-01-04. |
| 5 | **macdh** | **–2.045** | Non-redundant companion to MACD: shows the *acceleration* of bearish momentum (–0.867 on 12-29 → –2.045 on 01-05), i.e. the decline is still steepening, and it is the cleanest place to look for an eventual bullish divergence. |
| 6 | **rsi** | **28.79** | Quantifies the oversold extreme (first sub-30 print in the window); the primary input for mean-reversion risk and for spotting divergence. |
| 7 | **boll_lb** | **182.32** | Price closed **below** the lower band (181.18), a statistical stretch; paired with band width, it measures how far the rubber band is extended. |
| 8 | **atr** | **2.97 (1.64% of close)** | Converts all of the above into position sizing and stop placement; ATR has expanded from 2.57 (12-29) to 2.97, confirming the volatility regime shift. |

**Deliberately excluded (redundancy control):**
- **macds** — mathematically embedded in `macd` and `macdh`; the histogram already encodes the crossover.
- **stochrsi** — highly correlated with `rsi`; would double-count oversold.
- **boll / boll_ub** — the middle band and upper band are still used as *context* (192.64 / 202.95 from the verified snapshot), but the lower band is the actionable one in a downside stretch; selecting all three would be triple-counting one volatility construct.
- **vwma** — used as supporting evidence only (191.21, i.e. price is 5.25% below the volume-weighted average price, confirming the average holder of recent volume is underwater), since the raw volume series already carries the distribution evidence.
- **MFI** — see **Data caveat** in §8: the snapshot's MFI value of 0.0967 is implausible on a 0–100 bounded oscillator and should not be used.

---

## 4. Trend Analysis

### 4.1 The long-term trend is intact but being tested in real time
The 200 SMA is at **180.02 and rising** (~+0.11/session: 179.49 on 12-29 → 180.02 on 01-05). The 50 SMA at **187.40** sits **7.38 points (4.1%) above** the 200 SMA, so the medium/long-term "golden-cross" configuration remains in force. However, the 50 SMA is now **above price**, meaning the intermediate trend has already flipped down against the long-term trend. That divergence — price below 50 SMA but above 200 SMA — is the definition of a **trend correction inside a bull leg**, and it is a notoriously poor zone for fresh directional bets because both sides have a live thesis.

An important anchor: today's close of 181.18 is essentially back to the **2023-06-01 close of 180.09**. Seven months of advance have been surrendered in four sessions, which is precisely why the 200 SMA is sitting where it is — it is not an arbitrary line, it is the mean of the entire 2023 base.

### 4.2 The short-term trend is unambiguously down and still steepening in momentum
- The **10 EMA (187.81)** is 6.63 points (3.53%) above price and falling fast: 192.40 (01-02) → 190.92 → 189.28 → **187.81**. Price has closed below it for four consecutive sessions.
- **MACD (–1.346)** crossed below the signal line on **2023-12-20** and crossed the zero line on **2024-01-04**. The histogram has been negative since 12-19 with only a brief 12-13 → 12-18 positive blip, and it is now at its most negative value in the entire window (–2.045). There is **no momentum divergence yet**: MACD and price are making new lows together.
- **VWMA (191.21)** is 10.03 points (5.25%) above price and rolling over — buyers on volume are trapped above.

### 4.3 Volatility: a squeeze that resolved to the downside
The Bollinger construct tells a clean story. On **2023-12-29** the bands were compressed to a width of just **9.03 points** (upper 198.82, lower 189.80) — a genuine volatility squeeze. On **2024-01-05** the width is **20.63 points** (upper 202.95, lower 182.32), a **10.71% bandwidth**, more than double. Realized volatility exploded as the squeeze broke *downward*. Note that the **upper band rose from 198.82 to 202.95** while price collapsed — that is pure volatility expansion, not bullishness, and it is a trap for anyone reading band direction naively.

ATR confirms it: 2.57 (12-29) → 3.01 (01-02) → 2.97 (01-05). Volatility has re-based roughly 16% higher, which means **the same dollar stop that worked in December is now too tight**.

### 4.4 Momentum: oversold, but with no divergence and no confirmation
RSI path: 51.06 (12-29) → **35.37 (01-02)** → 33.16 → 29.78 → **28.79 (01-05)**. RSI crossed into oversold (<30) on 2024-01-04 and is now the weakest reading in the retrieved window. Critically:

- Price made a **lower low** today (180.17 vs 180.88) and RSI made a **lower low** (28.79 vs 29.78). **No bullish divergence exists as of this snapshot.** Any divergence-based long thesis is premature.
- The *rate* of RSI decline is decelerating (–15.7 pts on 01-02, then –2.2, –3.4, –1.0). Combined with the shrinking daily close-to-close losses (–0.40% today), this is consistent with **selling pressure exhausting near the 200 SMA** — but exhaustion ≠ reversal.

---

## 5. Key Levels (all values traced to tool output)

| Role | Zone | Evidence |
|---|---|---|
| **Resistance 3** | **192.6 – 194.7** | Bollinger mid 192.64; December congestion closes 192.53–194.71 |
| **Resistance 2** | **191.21** | VWMA (volume-weighted average price of the recent tape) |
| **Resistance 1 (pivot)** | **187.15 – 188.44** | Unfilled 01-02 gap (open 187.15, high 188.44) **+** 50 SMA 187.40 **+** 10 EMA 187.81 — a triple confluence |
| **Near-term pivot** | **183.4 – 185.9** | 01-03 low 183.43 / 01-03 high 185.88 |
| **Support 1 (critical)** | **180.02 – 180.17** | Rising 200 SMA 180.02 **+** today's low 180.17 (0.15 apart) |
| **Support 2** | **177.5 – 179.2** | Early-November congestion (11-02 close 177.57; 11-06 close 179.23) |
| **Support 3 (measured)** | **~174.1** | 180.02 minus 2×ATR (2×2.97 = 5.94); also the 2023-08-17 low 173.48 / close 174.00 |

---

## 6. Actionable Playbook

### Scenario A — 200 SMA holds (base case for a tactically *neutral-to-long* trade, not a call on the trend)
Trigger requires **evidence**, not hope. Wait for either:
1. A session that holds above **180.02** on **contracting volume** (< the 62–82M of the down leg), followed by a close **back above 183.43** (01-03 low, proving the last lower-low structure failed); or
2. A close above **182.32** (Bollinger lower band) that recaptures the band, with `macdh` narrowing two sessions in a row.

- **Entry:** 183.4–184.0 on the reclaim.
- **Stop:** **179.85** (below the 200 SMA and below today's low) → risk ≈ 3.6 points ≈ **1.2 ATR**.
- **First target:** 187.15–188.44 (gap fill / 50 SMA / 10 EMA) ≈ **+2.3R**. Beyond that, 191.21 (VWMA).
- **Sizing:** risk 1.0% of equity ÷ 3.6 points per share.

### Scenario B — 200 SMA fails (trend continuation)
Trigger: a **close below 180.02** (not an intraday wick) with volume **≥ ~70M** (i.e. at or above the 01-04 level), and `macdh` making a fresh low.

- **Entry:** on the close-through or the first failure-retest of 180 from below.
- **Stop:** **183.1** (~1 ATR above the break) for a tight version, or 184.0 above the 01-04 high (183.09) for a swing version.
- **Target:** **174.1** (2×ATR extension, confluent with the August 2023 173.5–174.0 zone) → roughly **2:1** reward/risk on the swing version.
- **Sizing:** risk 1.0% of equity ÷ stop distance in points. With ATR at 2.97 (1.64% of price), a 1.5-ATR stop is 4.46 points — position size in shares = (0.01 × equity) ÷ 4.46.

### What to *avoid*
- **Do not short at 181.18 with RSI 28.79 and the 200 SMA immediately beneath.** The distance to the first meaningful invalidation (183.1) is larger than the distance to support (180.02), which is negative expectancy on a chase.
- **Do not buy solely because RSI < 30.** Oversold in a confirmed downtrend with an accelerating negative `macdh` (–2.045, still expanding) and no divergence has repeatedly been a "catch the knife" condition. The RSI print is a *risk-management* input, not an entry trigger.

### Invalidation of the bearish read (watch these)
1. A daily close **above 187.15–188.44** (gap filled + 50 SMA + 10 EMA reclaimed) with `macdh` rising.
2. A **bullish RSI divergence**: price undercutting 180.17 while RSI holds above 28.79.
3. `macdh` printing a **shallower negative value** for two consecutive sessions (momentum trough).

---

## 7. Summary Table

| Dimension | Reading (2024-01-05) | Signal | Interpretation / Use |
|---|---|---|---|
| Close | **181.18** (O 181.99, H 182.76, L 180.17) | — | 4th straight down session; smallest loss (–0.40%) of the sequence |
| Volume | 62.38M (down-leg avg ~68.8M vs ~38.4M pre-drop) | **Bearish** | ~1.8× volume on decline = distribution, not drift |
| close_200_sma | **180.02** (rising) | **Critical support** | Price +0.65% above; today's low 180.17 is 0.15 above it — the whole thesis pivots here |
| close_50_sma | **187.40** (price –3.32% below) | **Bearish** | Medium-term trend broken; sits inside the unfilled gap zone |
| close_10_ema | **187.81** (price –3.53% below), falling ~1.6/session | **Bearish** | Short-term trend firmly down |
| Golden-cross status | 50 SMA is 4.1% **above** 200 SMA | **Bullish (structural)** | Long-term uptrend technically intact; correction, not a confirmed reversal |
| macd | **–1.346** (signal 0.699) | **Bearish** | Signal cross 2023-12-20; zero-line cross 2024-01-04 |
| macdh | **–2.045** (worst in window) | **Bearish, expanding** | Momentum still steepening — no divergence yet |
| rsi | **28.79** (oversold since 01-04) | **Oversold** | Lowest in window; lower-low RSI with lower-low price = no divergence |
| boll / boll_ub / boll_lb | 192.64 / 202.95 / **182.32** | **Stretched** | Close is 0.63% *below* lower band; bandwidth blew out from 9.03 (12-29) to 20.63 |
| vwma | 191.21 (price –5.25%) | **Bearish** | Recent volume-weighted buyer is underwater |
| atr | **2.97** (1.64% of close), up from 2.57 | **Rising risk** | Use 1.5–2×ATR (4.5–5.9 pts) stops; reduce position size vs December |
| Unfilled gap | **187.15 – 188.44** (from 01-02) | **Overhead magnet** | Confluent with 50 SMA 187.40 and 10 EMA 187.81 |
| **Net stance** | **Oversold within an intact long-term uptrend, at critical support** | **Neutral / tactical** | Wait for either a reclaim of 183.43 → 187–188 or a volume close below 180.02; do not chase either direction inside 180–184 |

---

## 8. Data Caveats & Discrepancy Flag

- **Consistency check:** every indicator value from `get_indicators` matches the verified snapshot exactly for 2024-01-05 (50 SMA 187.3978, 200 SMA 180.01515, 10 EMA 187.807199, MACD –1.345788, signal 0.698936, histogram –2.044724, RSI 28.794487, Bollinger 192.637001 / 202.951007 / 182.322995, ATR 2.967694, VWMA 191.211054). **No discrepancy between tools.**
- **Flagged anomaly:** the snapshot also returns **`mfi` = 0.0967**. Money Flow Index is bounded 0–100, so a value near zero is not interpretable as "extreme oversold" — it is almost certainly a broken/negative-flow-edge computation. **This value is excluded from the analysis above** and should not be used to reinforce the oversold case.
- All percentage moves, level confluences and ATR multiples above are arithmetic on tool-provided OHLCV and indicator values on the dates cited. No support/resistance "bounce" is claimed as historical validation — the 180.02/180.17 relationship is a *juxtaposition of two tool-reported numbers*, not a verified reaction.
- Adjusted-price note: the series carries dividends of 0.24 on 2023-08-11 and 2023-11-10; the `technical_total_return_index` (182.19 on 01-05) differs slightly from the close (181.18), so return figures quoted here are **price returns**, close-to-close.