# AMZN — Multi-Timeframe Technical Report (as of 2024-02-07 close)

## 1. Executive summary

AMZN closed at **$170.53** on 2024-02-07 (O 169.48 / H 170.88 / L 168.94, volume 47.17M). The stock is in a **confirmed, mature uptrend that was re-accelerated by a single-session repricing event on 2024-02-02** (+7.87% close-to-close, from 159.28 to 171.81, on 117.22M shares ≈ **2.33× the trailing-20-session average of ~50.2M**). The last three sessions (Feb 5–7) are a **tight, low-volatility consolidation directly beneath the post-gap high of 172.50 and the upper Bollinger band at 171.67**.

The trend structure is unambiguously bullish on every timeframe I can verify:
- Price **+11.45% above the 50-SMA** ($153.01) and **+26.39% above the 200-SMA** ($134.93), with the 50-SMA **13.40% above** the 200-SMA and both averages rising every session in the visible window.
- Short-term momentum is re-accelerating: **MACD +4.80 vs signal +3.49**, histogram **+1.31** (positive since the 2024-01-12 bullish crossover).
- **RSI 69.62** — strong-trend territory, just under the 70 threshold, with **no bearish divergence** visible.

The main risk is not trend direction but **extension**: the close sits **3.69% above the 10-EMA ($164.46)**, **5.40% above the volume-weighted average ($161.79)**, and at the **95.5% percentile of the Bollinger range** (see §7). This is a "hold, don't chase at market" configuration; the asymmetry improves either on a confirmed break of 172.50 or on a controlled pullback into 167.33–164.46.

---

## 2. Data-integrity check (verified snapshot is the source of truth)

`get_verified_market_snapshot` for 2024-02-07 returned values **fully consistent** with `get_stock_data` and `get_indicators` — no discrepancies to flag:

| Metric | Snapshot (2024-02-07) | Indicator tool | Match |
|---|---|---|---|
| Close | 170.529999 | 170.529999 | ✅ |
| 50-SMA | 153.0130 | 153.012999 | ✅ |
| 200-SMA | 134.9281 | 134.9281 | ✅ |
| 10-EMA | 164.4602 | 164.460156 | ✅ |
| MACD / Signal / Hist | 4.7993 / 3.4886 / 1.3107 | 4.799302 / 3.488589 | ✅ |
| RSI | 69.6243 | 69.624288 | ✅ |
| ATR | 3.7009 | 3.700941 | ✅ |
| VWMA | 161.7894 | 161.789430 | ✅ |
| Bollinger (mid/UB/LB) | 158.916 / 171.670 / 146.162 | not selected | supplementary |

**One formatting caveat to flag rather than reconcile:** the snapshot prints MFI as **0.6855**, which is the 0–100 scale expressed as a fraction (≈**68.55**). I read it as "strong but near-overbought money flow," not as a near-zero reading. All other values are internally consistent.

---

## 3. Why these 8 indicators (complementary, non-redundant)

| Indicator | Role in this specific setup | Why not redundant |
|---|---|---|
| **close_200_sma** | Strategic trend anchor; confirms the bull regime and how stretched it is (26.4% above) | Slowest, non-overlapping information: regime, not timing |
| **close_50_sma** | Intermediate trend & the trailing risk line (153.01) | Captures the "trend break" threshold that 200-SMA would report far too late |
| **close_10_ema** | Timeliness: measures the *extension* problem and marks first support (164.46) | Fastest average; the only one that flags short-term over-extension |
| **macd** | Momentum regime and thrust (+4.80, highest in 40-session window) | Trend/rate-of-change of EMAs, distinct from price averages |
| **macds** | Crossover trigger; defines when momentum actually turned (2024-01-12) | Converts MACD into an actionable signal rather than a level |
| **rsi** | Overbought/oversold + divergence surveillance in a parabolic move | Normalized oscillator; MACD cannot tell you "this is a 70 print" |
| **atr** | Position sizing and stop placement after a volatility regime change (2.94 → 3.88 → 3.70) | Risk dimension; no other selected indicator is scale-free volatility |
| **vwma** | Confirms the move is volume-backed (161.79 vs close 170.53) | Price-averaged *with volume*; SMA/EMA ignore volume entirely |

Deliberately excluded: `boll`, `boll_ub`, `boll_lb` (their values come from the verified snapshot and are used in §7 — selecting them would have consumed 3 of 8 slots for one concept), and `macdh` (derivable from macd − macds, which I compute directly).

---

## 4. Long-term trend: intact bull market, structurally healthy

- **200-SMA $134.93**, rising monotonically from 123.94 (2023-12-11) to 134.93 (2024-02-07) — a slope of roughly **+0.73% per month** in the average itself. A rising 200-SMA over a two-month window with price above it is the definition of a structural uptrend.
- **50-SMA $153.01**, rising from 137.16 (2023-12-11) to 153.01 — a much steeper **+1.93% per month** in the average. The 50-SMA has been **above the 200-SMA on every session in the visible window** (137.16 > 123.94 on 2023-12-11; 153.01 > 134.93 now), and the spread has **widened from 10.7% to 13.4%** of the 200-SMA. Expansion of that spread means the intermediate trend is *outperforming* its own long-term baseline — bullish, but also the mechanism by which "stretched" conditions build.
- **Context for the 26.4% premium to the 200-SMA:** the last time price was meaningfully below the 200-SMA in this dataset was late October 2023 (close 119.57 on 2023-10-26, low 118.35). The stock has therefore spent ~3.5 months re-rating upward. This is strength, but it lowers the margin of safety for late entries: a routine mean-reversion to the 50-SMA would be a **−10.3%** move without breaking the trend.

---

## 5. Intermediate trend & momentum: the January reset, then re-acceleration

The MACD series tells a clean three-act story that is directly supported by the tool output:

1. **Momentum peak and decay (late Dec → 2024-01-08).** MACD 2.78 on 2023-12-29, already *below* its signal (2.92) — i.e., a bearish crossover had occurred before that date — then decayed to **0.779 on 2024-01-08**, with the histogram at roughly **−1.05**. Price obliged: close fell from 153.41 (2023-12-26) to **144.57 (2024-01-04)**, a −5.8% drawdown.
2. **Bullish re-cross (2024-01-12).** MACD 1.643 crossed above signal 1.549 — the first bullish crossover in the window. Price confirmed with higher lows: 149.10 (01-08) → 151.37 (01-09) → 153.73 (01-10) → 155.18 (01-11).
3. **Thrust (2024-02-02 onward).** MACD jumped from 2.450 (02-01) to 3.465 (02-02) to **4.799 (02-07)**, the highest reading in the 40-session window, with the signal lagging at 3.489.

**Important nuance — the thrust is *decelerating*, not failing.** The histogram reads: 0.166 (02-01) → 0.944 (02-02) → 1.264 (02-05) → 1.298 (02-06) → **1.311 (02-07)**. The increments are shrinking each day (0.778 → 0.320 → 0.034 → 0.013). Translation: **the post-gap impulse is maturing into a consolidation**. This is typical and not bearish, but it means the next directional resolution likely requires a fresh trigger rather than continued momentum drift. Any *negative* histogram print (MACD crossing back below ~3.49) would be the first objective warning that the gap is being digested rather than built upon.

The **10-EMA at 164.46 is rising aggressively** (152.26 on 01-18 → 164.46 on 02-07) and is now **7.48% above the 50-SMA** — a wide but not extreme fast/slow spread, confirming a "fresh leg up" rather than a late-stage blow-off.

---

## 6. RSI: strong, technically overbought, but *not* diverging

- RSI **69.62** on 2024-02-07; the 40-session high was **73.78 on 2024-02-02** (the gap day). It printed **70.41 on 2024-01-29** and then reset hard to **53.10 on 2024-01-31** — a 17-point momentum flush on a −3.8% two-day price drop. That reset is *constructive*: it burned off overbought conditions before the gap, which is why the current 69.62 is not as extended as it looks.
- **No bearish divergence.** Price's highest close (171.81 on 02-02) coincided with RSI's highest reading (73.78). The subsequent three sessions produced marginally lower closes (171.81 → 170.31 → 169.15 → 170.53) with RSI easing to 68–70 — mild cooling, not divergence.
- **Interpretation:** in a strong trend RSI often parks in the 60–75 band and *stays* there. The correct read is "trend intact, do not fight it," not "sell because RSI > 70." A **sustained loss of the 60 level** (as on 2024-01-31, 53.10) has been the more reliable cooling signal in this window than the 70 threshold itself.

---

## 7. Volatility & Bollinger structure: post-gap volatility decay

| Measure | 2024-02-07 value | Context |
|---|---|---|
| ATR | **3.70** | 2.94 on 01-29 → 3.88 on 02-02 → 3.84 → **3.70** (contracting) |
| ATR as % of close | **2.17%** | vs ~1.9% pre-earnings (2.94–3.0 ATR) |
| Bollinger mid (20-SMA) | **158.92** | Rising; close is +7.31% above it |
| Bollinger upper | **171.67** | Close is **0.67% below it** |
| Bollinger lower | **146.16** | — |
| Band width | **16.05%** of mid | Wide (inflated by the Feb-2 gap) |
| %B position | **≈95.5%** | Price in the top 5% of the band envelope |

Two things matter here:
1. **The ATR spike-and-decay pattern is textbook post-catalyst behavior.** ATR expanded from 2.94 → 3.88 (a 32% jump) as the gap printed, and has since contracted for three straight sessions. Volatility contraction *inside* a high-level range is usually a coil, with resolution direction dictated by the level that breaks.
2. **Price has NOT closed above the upper Bollinger band.** Despite a 9.0% overnight open (155.20 prior close → 169.19 open on 02-02) and an intraday high of **172.50** that day, the close (171.81) and every close since have stayed **inside** the band, because the bands widened to absorb the move. This is a subtle but genuine warning that the immediate upside is being "priced in" rather than "riding the band." A close **above 171.67 with expanding volume** would be a materially stronger signal than the current pattern.

---

## 8. Volume confirmation: VWMA says the rally is real; participation says it's pausing

- **VWMA $161.79** vs close **$170.53** → price is **5.40% above** the volume-weighted average. VWMA has risen for nine consecutive sessions it is visible (150.93 on 01-08 → 161.79), meaning **the marginal dollar traded has been getting progressively more expensive** — genuine demand, not a thin drift. Note the VWMA sits **$8.78 above the 50-SMA**, another way of saying recent volume-weighted buying happened far above the trailing baseline.
- **Volume sequence after the gap: 117.22M (02-02) → 55.08M (02-05) → 42.51M (02-06) → 47.17M (02-07).** Declining volume on a flat-to-slightly-lower price is **constructive consolidation** (no distribution signature). But it also means the 172.50 breakout, if it comes, needs volume to re-expand — I'd want **>60M** (above the ~50.2M trailing average) to treat it as valid rather than a liquidity-thin fake-out.
- **MFI ≈68.55** (snapshot value 0.6855, fractional) corroborates: money flow is strongly positive and approaching overbought, consistent with the RSI/VWMA read rather than contradicting it.

---

## 9. Concrete levels (all derived from tool output)

**Resistance**
- **170.88** — 2024-02-07 high (immediate intraday ceiling)
- **171.67** — Bollinger upper band
- **172.50** — 2024-02-02 high = the post-gap swing high; **the pivot for the next leg**

**Support**
- **168.94** — 2024-02-07 low
- **167.33** — 2024-02-02 low = **the most important near-term level**; the unfilled gap (159.76 Feb-1 high → 167.33 Feb-2 low) sits directly below it
- **164.46** — 10-EMA
- **161.26 / 161.73** — pre-gap close (01-29) and high (01-30)
- **158.92** — Bollinger mid / 20-SMA
- **153.01** — 50-SMA (trend-break line)
- **146.16** — Bollinger lower band; **144.05** — 2024-01-04 low (January swing low)

Mechanical volatility envelopes off the 170.53 close (using ATR 3.70 — **projections, not forecasts**): 1×ATR = 166.83 / 174.23; 2×ATR = 163.13 / 177.93.

---

## 10. Actionable plan

**Bias: constructive/long, but execute on levels, not at market.**

1. **Breakout continuation (primary trigger).** A daily close **above 172.50** with volume **>60M** justifies adding exposure. Logical invalidation: **close below 167.33** (−2.9% from the 02-07 close) or below the 1×ATR line at 166.83. That gives roughly a 1.2%–3.0% risk band per unit against an open-ended trend continuation — acceptable R:R because the trend and momentum regimes are both bullish.
2. **Pullback accumulation (preferred risk/reward).** The gap zone **167.33–164.46** (Feb-2 low to 10-EMA) is the highest-quality demand shelf. Buying there with a stop below **163.13** (close − 2×ATR) risks ~1.0%–2.6% while keeping the position aligned with a rising 10-EMA. Do not pre-position for this level; let price arrive with contracting volume.
3. **Core trend hold.** As long as the close is above the **50-SMA (153.01)** and MACD (4.80) is above signal (3.49), the structural trend is intact — trailing stops can reasonably sit beneath 10-EMA (164.46) for tactical longs, and beneath the 50-SMA for strategic positions.
4. **Sizing.** ATR is **2.17% of price**, so the same dollar risk buys ~15% fewer shares than it did a month ago (2.94/170 vs 3.70/170 ≈ 1.73% vs 2.17%). Cut notional to keep risk-per-trade constant; for a 0.5%–1.0% equity risk budget, position size ≈ (0.0075 × equity) / 3.70 per share.
5. **Do NOT add on a lower-high failure at 171.67–172.50.** A rejection there with the MACD histogram rolling over (currently 1.31 and flattening) sets up a re-test of 167.33, and a close below 164.46 would shift the tactical bias to neutral.

---

## 11. Risks and what would invalidate the read

- **Extension risk (highest-probability risk).** 26.4% above the 200-SMA, 11.5% above the 50-SMA, 3.7% above the 10-EMA, 95.5% of the Bollinger range. A −10.3% reversion to the 50-SMA would be a *normal* event that leaves the primary trend technically intact.
- **Gap-fill risk.** The 159.76–167.33 gap is unfilled. A close under 167.33 opens a mechanical vacuum toward 161.26–158.92. This is the single most concrete bearish trigger available.
- **Momentum deceleration.** MACD histogram increments are collapsing (0.778 → 0.320 → 0.034 → 0.013). If the histogram prints negative, the 01-12 bullish crossover is effectively spent and the setup reverts to "range 164–172."
- **Volume fade.** Breakout attempts on <50M shares have not yet been tested in this window; treat sub-50M breaks of 172.50 with skepticism.
- **Event-catalyst footnote.** The 2024-02-02 gap (+9.0% open, 2.33× volume) is *consistent with* an earnings-type catalyst; the dataset itself does not label the cause. Treat that attribution as inference while treating the price/volume facts as verified.
- **Caveat on historical claims:** I have not asserted any support/resistance *bounce* history beyond the raw touch points listed in §9, nor any exact percentage move that isn't computed directly from the returned OHLC rows above.

---

## 12. Summary table

| Dimension | Reading (2024-02-07) | Signal | Actionable use |
|---|---|---|---|
| Close | **170.53** (O 169.48 / H 170.88 / L 168.94) | Neutral-positive, coiling under highs | Reference for all levels |
| 200-SMA | **134.93**, rising; price +26.39% | Bull regime, stretched | Strategic long bias retained |
| 50-SMA | **153.01**, rising; +11.45% below price | Intermediate uptrend intact | Strategic stop / trend-break line |
| 50 vs 200 | +13.40% spread, widening | Healthy but late-cycle | Watch for spread compression as an early warning |
| 10-EMA | **164.46**, +3.69% below price | Short-term over-extension | First dynamic support; pullback entry zone |
| MACD | **4.80** (highest in 40 sessions) | Strong bullish thrust | Confirms trend |
| MACD signal | **3.49**; hist **+1.31** | Bullish since 2024-01-12; hist flattening | Warning if hist turns negative |
| RSI | **69.62** (peak 73.78 on 02-02; flushed to 53.10 on 01-31) | Strong, mild overbought, **no divergence** | Hold trend; RSI <60 = cooling signal |
| ATR | **3.70** = **2.17%** of price (from 2.94 on 01-29) | Post-catalyst volatility decay | Size positions on 3.70; 1×ATR = 166.83/174.23 |
| Bollinger | Mid **158.92**, UB **171.67**, LB **146.16**, %B ≈95.5% | Upper-band test, not yet a band ride | Close >171.67 on volume = valid breakout |
| VWMA | **161.79**, +5.40% below price | Volume-backed demand confirmed | Reinforces that dips were bought |
| Volume | 117.22M (02-02) → 47.17M (02-07); 20d avg ≈50.2M | Healthy consolidation, no distribution | Need >60M to validate a 172.50 break |
| Key resistance | **170.88 / 171.67 / 172.50** | Pivot cluster | Break = add; rejection = range |
| Key support | **167.33 / 164.46 / 161.26 / 158.92 / 153.01** | Tiered demand | Buy 167.33–164.46; trip-wire <161.26 |
| **Overall verdict** | **Bullish trend, bullish momentum, extended price** | **Hold core long; add on >172.50 breakout or 167.33–164.46 pullback; stop under 163.13 (tactical) / 153.01 (strategic)** | Favor level-based execution over market orders |