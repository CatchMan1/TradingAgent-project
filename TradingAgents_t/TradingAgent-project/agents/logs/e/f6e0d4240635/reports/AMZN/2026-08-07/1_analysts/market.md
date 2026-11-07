# AMZN — Technical & Trend Analysis
**As of 2026-08-07 (verified market snapshot)** | Last close: **$274.48**

---

## 1. Indicator Selection & Rationale

I selected **8 complementary indicators** spanning trend, momentum, volatility and volume — deliberately avoiding same-family redundancy (e.g., I did not stack RSI + stochastic, nor all three MACD components, since histogram sign fully encodes the MACD/signal crossover):

| # | Indicator | Value (2026-08-07) | Why it fits this market context |
|---|---|---|---|
| 1 | **close_10_ema** | 263.35 | AMZN just printed a violent 3-session, earnings-driven re-rating. A fast EMA is needed to define the immediate trend and the first "line in the sand" for the new regime. |
| 2 | **close_50_sma** | 247.51 | Medium-term trend/support. It has just inflected upward — essential for confirming the breakout is repairing trend, not just a news spike. |
| 3 | **close_200_sma** | 236.54 | Long-term regime benchmark; price is 16% above it, which frames how *extended* the move is. |
| 4 | **macd** | 7.58 | Captures the momentum regime shift from deeply negative (July downtrend) to strongly positive. |
| 5 | **macdh** | 4.09 | Histogram exposes *rate of change* of that momentum — critical right now because it is rolling over while price chops. |
| 6 | **rsi** | 64.21 | The move went from RSI 33.3 (7/29, near-oversold) to 72.2 (8/3, overbought) in three sessions. RSI quantifies whether the digestion has cooled the froth. |
| 7 | **atr** | 9.33 | Volatility roughly +35% post-gap. Position sizing and stop distance must be ATR-scaled, not fixed-percentage. |
| 8 | **vwma** | 256.04 | Volume-weighted cost basis: tells us where the marginal buyer is positioned and whether overhead supply exists. |

*Supplementary context (pulled and cross-checked, not part of the core 8): Bollinger middle 251.59 / upper 287.33 / lower 215.86.*

**Data-integrity flag:** The snapshot reports `mfi = 0.4754`. Read as a 0–1 normalized series that is ~47.5 (neutral money flow), which conflicts with the visibly strong up-volume on 7/30–8/3. Because the scale is ambiguous, **I am not using MFI in the conclusion.** I also confirm `split = 1.0` and `dividend = 0.0` on every row, so no corporate-action distortion exists in this series.

---

## 2. The Dominant Fact: A 15% Earnings Gap Re-Rated AMZN

Everything in the current technical picture flows from three sessions:

| Date | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|
| 2026-07-29 | 229.32 | 232.82 | 226.16 | **226.65** | 44.96M |
| 2026-07-30 | 233.35 | 239.82 | 231.06 | **235.50** | 101.84M |
| 2026-07-31 | **265.00** | 273.23 | 262.01 | **271.58** | 129.05M |
| 2026-08-03 | 278.29 | **287.20** | 278.00 | **284.02** | 90.83M |

- **7/31 day return: +15.3%** (235.50 → 271.58), with an opening gap from 235.50 to 265.00.
- **Low 226.65 (7/29) → high 287.20 (8/3) = +26.7% in three sessions.**
- **287.20 is the highest print of 2026** in the data set (prior 2026 intraday high was 278.56 on 2026-05-05). **284.02 on 8/3 was the highest close of 2026** (prior best close 274.99 on 2026-05-06).
- Volume confirms participation: 101.8M and 129.1M versus a 20-session average of **50.1M** (computed from the OHLCV rows).

This is a **repricing event, not a drift**. The technical question is no longer "is it bullish" but "is it holding the gap?"

---

## 3. Trend Structure: Bullish, But Extended

**Verified snapshot:** 50SMA 247.51 · 200SMA 236.54 · 10EMA 263.35 · VWMA 256.04 · Close 274.48

- Price is **+10.90% above the 50SMA**, **+16.04% above the 200SMA**, **+4.23% above the 10EMA**, and **+7.21% above the VWMA**.
- **50SMA > 200SMA** (spread of 10.97, i.e. the 50SMA sits 4.64% above the 200SMA) — a golden-cross configuration in place.
- **The 50SMA has bottomed and is turning up.** Its series declined steadily from 254.60 (7/08) to a trough of **246.38 (7/30)**, then rose to **247.51 (8/07)** for five consecutive up-days. This is the single most constructive structural signal: the medium-term average stopped falling precisely as the gap occurred.
- **The 200SMA is rising monotonically**: 233.17 (7/08) → 236.54 (8/07), roughly +1.4% over a month. Long-term trend is intact and healthy.

**Nuance — the extension risk is real.** At +16% above the 200SMA, AMZN is stretched versus its own long-run anchor. Historically (and conceptually) this is a zone where the stock becomes vulnerable to sharp mean-reversion if the broad tape wobbles. Note also the 2026 path: close 226.50 on 2026-01-02 → 274.48 now is **+21.2% YTD**, *and* the stock fell from 246.29 (1/08) to a 196.00 low (2/17) — a **-20.4% drawdown** — before rallying **+46.5% off that low** to 287.20. This is a high-beta, high-amplitude name; the current extension should be respected, not ignored.

---

## 4. Momentum: Strong, But Decelerating (The Key Watch Item)

**RSI (verified 64.21):**
- 33.31 (7/29) → 67.88 (7/31) → **72.23 (8/03, peak)** → 67.04 (8/04) → 63.49 (8/05) → 63.20 (8/06) → **64.21 (8/07)**
- The breakout drove RSI into overbought (72.2) but **it has since reset to the mid-60s without price collapsing**. That is the healthy form of an overbought reset: froth burned off by time, not by price.
- RSI at 64 leaves meaningful headroom before 70–80, so there is no mechanical overbought ceiling blocking a continuation attempt.
- **No bearish divergence yet.** RSI's lower high (72.2 → 64.2) is *accompanied* by a lower price high (284.02 → 274.48) — consistent, not divergent. A divergence would only appear if price retests 284–287 and RSI fails to exceed 72.

**MACD (verified 7.58, signal 3.49, histogram 4.09):**
- MACD line: **-3.75 (7/29) → -0.62 (7/31) → +7.58 (8/07)** — a ~11.3-point swing in six sessions.
- **Bullish MACD/signal crossover occurred on 2026-07-31** (MACD -0.62 crossed above signal -1.84). The signal line only crossed zero on 8/04 (0.22), meaning the crossover is now confirmed from below — a structurally stronger configuration.
- **Caution: the histogram has now contracted for three consecutive sessions: 4.62 (8/05) → 4.58 (8/04→8/05 peak) → 4.36 (8/06) → 4.09 (8/07).** Momentum is still strongly positive in absolute terms but the *second derivative* has turned negative. Combined with falling volume, this is textbook **consolidation/flag formation rather than distribution** — but it does mean the easy money of the gap follow-through has been made.

---

## 5. Volatility: Post-Gap Expansion Is Now Deflating

**ATR (verified 9.33):**
- 6.89 (7/29) → **9.51 (7/31)** → 9.95 (8/03, peak) → 9.33 (8/07). Volatility expanded ~44% at the peak and is now easing for three sessions.
- At **3.40% of the last close**, ATR is elevated. Any stop tighter than ~1 ATR (≈$9.3) is at high risk of noise-triggering.

**Bollinger (verified): middle 251.59 · upper 287.33 · lower 215.86**
- **Bandwidth = 28.4% of the middle band** — an extremely wide envelope, a direct artifact of the gap.
- Price at 274.48 sits at **%B ≈ 0.82** (82% of the way from lower to upper band): in the upper quintile, **but not hugging the upper band**. That combination — strong but not at the extreme — typically precedes either a breakout continuation or a band-contraction chop.
- The bands are still *diverging*: upper rising 264.20 (7/31) → 287.33 (8/07) while the lower falls 223.51 → 215.86 (the pre-gap 196–210 zone rolling into the 20-day window). **Do not read the low lower band as "oversold support" — it is a stale-data artifact of the gap.** The actionable band level is the upper band at **287.33**, which nearly coincides with the 8/03 high of **287.20** — a powerful double-capping confluence.

---

## 6. Volume: Healthy Drying-Up, Not Distribution

Post-gap volume decay: **129.05M → 90.83M → 69.75M → 45.12M → 30.67M → 33.86M**.

- Latest volume **33.86M is 0.68× the 20-session average of 50.06M**, and 0.85× the 39.97M average of the 17 non-earnings sessions.
- Tight range (270.73–282.79 over the four sessions since 8/03) on contracting volume = **no evidence of institutional supply**. This is the footprint of a bullish consolidation.
- **VWMA at 256.04**, with price 7.2% above it: the volume-weighted cost of recent buyers sits far below market. This is supportive (no trapped sellers overhead until ~256) but also means the 256–262 corridor is **thinly-supported, air-pocket territory** if the gap starts to fill.
- **Actionable volume rule:** a break of 287.20 needs volume back above ~50M (1× 20-day avg) to be trusted. A break of 270.73 on expansion would signal the first genuine distribution.

---

## 7. Actionable Level Map (all levels derived from tool output)

**Resistance**
| Level | Source |
|---|---|
| **287.20–287.33** | 8/03 high **+** Bollinger upper band — the decisive confluence |
| 281.07 / 282.79 | 8/04 and 8/05 highs — first supply shelf |
| 278.31 | 8/07 high (immediate intraday cap) |

**Support**
| Level | Source |
|---|---|
| 272.75 / 271.06 / 270.73 | 8/07, 8/06, 8/05 lows — immediate pivot floor |
| **265.00** | 7/31 gap-day *open* (institutional repricing line) |
| **263.35** | Rising 10EMA — sits just above the gap open |
| **262.01** | 7/31 gap-day *low* — **the breakout's invalidation line** |
| 256.04 / 256.93 | VWMA **and** 50% retracement of the 226.65→287.20 leg (confluence) |
| 251.59 | Bollinger middle |
| 247.51 | 50SMA — the final trend line of defence |

**Asymmetry note:** the gap zone between 262.01 and 265.00 is the true battleground. Price has *not* closed below 262.01 since 7/30, so it is untested but structurally critical.

---

## 8. Trading Plan

**Bias: Constructive/long, with a "buy the pullback, don't chase the high" discipline.**

1. **Continuation trigger (breakout):** A daily close above **287.20 on volume > ~50M** reasserts the trend. Do **not** pre-position into 287 — that is where the upper Bollinger band caps and where the histogram is decelerating.
2. **Preferred entry zone (pullback):** **263–266** (10EMA 263.35 + gap open 265.00). This is the highest-quality risk/reward: buying the retest of the institutional repricing line while the 10EMA rises into it.
3. **Second entry zone:** **256–257** (VWMA + 50% gap-retrace confluence). Only if the tape grants it; this would be a deeper reset while the 50SMA (247.51) still holds below.
4. **Stop discipline (ATR-scaled):** ATR 9.33 means:
 - Aggressive swing stop: below **262.01** (gap low) ≈ 4.5% risk from 274.48.
 - Structural stop: below **256.0** (VWMA/50% retrace) ≈ 6.7% risk.
 - If long from the 263–266 zone, place the stop ~1.5 ATR below entry, i.e. roughly **250–252** (the Bollinger middle), not a hair under the entry.
5. **Position sizing:** size so that 1.5 × ATR (≈$14, ~5.1% of price) adverse excursion is within your per-trade risk budget. With ATR up 35% post-gap, the same dollar risk now requires a **~26% smaller position** than in late July.
6. **Exit/invalidation:** a daily close below **262.01** breaks the breakout structure and targets **256 → 251.59 → 247.51**. A close below the **50SMA (247.51)** would flip the medium-term trend and put the 200SMA (236.54) in play.

---

## 9. Honest Caveats / What Would Change the Read

- **Extension:** +16% above the 200SMA and +10.9% above the 50SMA means mean-reversion risk is asymmetric on any macro shock.
- **Momentum decay:** three consecutive sessions of MACD-histogram contraction plus 0.68× average volume can resolve either way. It's a coil, not a verdict.
- **Gap fragility:** gaps of this magnitude (15.3% on 7/31) statistically tend to be partially retested. Watch 262.01/265.00.
- I make **no claim of historical validation** for these levels — they are derived from the specific dated rows cited above, and no "bounce off support" is asserted anywhere in this report. The one genuine multi-point confluence I can evidence is 287.20 (8/03 high) vs 287.33 (upper band), and 256.04 (VWMA) vs 256.93 (computed 50% retracement).
- **Flagged discrepancy:** `mfi = 0.4754` from the snapshot is not interpretable on a 0–100 scale convention and conflicts with observed up-volume strength; excluded from conclusions.

---

## Key Points Summary

| Dimension | Verified Reading (2026-08-07) | Interpretation | Actionable Implication |
|---|---|---|---|
| Close | **$274.48** (O 272.87 / H 278.31 / L 272.75) | Consolidating 3.4% below the 8/03 record close of 284.02 | Range 270.73–282.79 is the active coil |
| Trend (short) | 10EMA **263.35**, +4.23% below price | Rising fast; supports the new regime | First dynamic support; aligns with gap open 265.00 |
| Trend (medium) | 50SMA **247.51**, +10.90% below price | **Inflected up** from 246.38 trough on 7/30 | Trend repair confirmed; 50SMA is final defence |
| Trend (long) | 200SMA **236.54**, +16.04% below price | Rising, but price is **extended** | Bullish but mean-reversion risk elevated |
| Golden cross | 50SMA − 200SMA = **+10.97** | Bullish alignment intact | Favours dip-buying over shorting |
| MACD | **7.58** vs signal **3.49** | Bullish crossover 7/31, confirmed above zero 8/04 | Trend momentum positive |
| MACD Histogram | **4.09**, down from 4.62 (8/05) | 3 sessions of contraction | Consolidation, not reversal — no chase |
| RSI | **64.21** (peak 72.23 on 8/03) | Overbought reset via time, not price | Room to 70+; no divergence yet |
| Bollinger | Mid **251.59** / UB **287.33** / LB **215.86** | %B ≈ 0.82; bandwidth 28.4% (extreme) | **287.20–287.33 is the cap**; expect band contraction |
| ATR | **9.33** (3.40% of price) | +35% post-gap, now easing | Stops ≥1.5 ATR; cut size ~26% |
| VWMA | **256.04**, +7.21% below price | Recent buyers in profit; thin air below 262 | 256 zone = VWMA + 50% gap retrace confluence |
| Volume | **33.86M** = 0.68× 20-day avg (50.06M) | Drying up on a tight range | Healthy — but breakouts need ≥50M |
| Key event | 7/31 gap: 235.50 → 265.00 open → 271.58 close (**+15.3%**) | Repricing, not drift | 262.01 = invalidation; 265.00 = institutional line |
| Invalidation | Daily close **< 262.01** | Breakout structure fails | Targets 256.04 → 251.59 → 247.51 |
| Continuation | Daily close **> 287.20 on >50M volume** | New leg higher | Only then add; don't pre-position |
| Data flag | `mfi = 0.4754` (scale ambiguous) | Conflicts with up-volume evidence | Excluded from conclusions |