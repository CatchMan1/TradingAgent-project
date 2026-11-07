# GOOGL (Alphabet Inc.) — Technical Analysis Report
**As of trading date 2026-07-14 (verified snapshot source of truth)**

## 1. Selected Indicators & Rationale
I chose 8 complementary, non-redundant indicators spanning trend, momentum, volatility, and volume:

| Indicator | Category | Why it fits this context |
|---|---|---|
| **close_200_sma** | Long-term trend | Anchor for the multi-month uptrend and golden-cross structure |
| **close_50_sma** | Medium-term trend | Currently the key overhead level; shows the medium trend rolling over |
| **close_10_ema** | Short-term momentum | Times the recent bounce and detects momentum shifts |
| **macd** | Momentum | Measures the depth/recovery of the correction |
| **macds** | Momentum (signal) | Confirms the recent bullish crossover / whether it holds |
| **rsi** | Momentum | Gauges overbought/oversold within the consolidation |
| **atr** | Volatility | Elevated-volatility regime; stop-loss & position sizing |
| **vwma** | Volume | Volume-weighted trend confirmation of accumulation/distribution |

Bollinger values (boll/boll_ub/boll_lb) are also referenced as supplementary context from the verified snapshot; they are not double-counted in the core 8.

---

## 2. Price Context & Trend Structure
**Latest session (2026-07-14):** Open 351.20, High 360.16, Low 351.09, **Close 359.51**, Volume 18.26M. This was a bullish reversal candle — opened near the session low, closed near the high, recovering +7.00 pts (+2.0%) from the prior close of 352.51 after a two-day dip.

**The bigger picture:** GOOGL staged a strong V-shaped recovery off the March 2026 low (~273.50 close on 2026-03-30), rallied to a closing peak of **402.62 on 2026-05-13** (intraday high 408.61 on 2026-05-18), then corrected. The correction bottomed at a close of **337.39 on 2026-06-26** (intraday low 330.20) — a **−16.2% drawdown** from the May close high. From that low, price has recovered **+6.6%** to today's 359.51, but remains below the May peak.

**Multi-timeframe trend read:**
- **Long-term (bullish):** Price (359.51) sits **+12.4% above the 200 SMA (319.98)**, which is rising steadily (from 291.3 on 2026-05-15 to 320.0 today). The **50 SMA (372.29) remains above the 200 SMA**, preserving the golden-cross / bullish structural backdrop.
- **Medium-term (corrective):** Price is **−3.4% below the 50 SMA (372.29)**. Critically, the 50 SMA has flattened and just begun to roll over (peaked at ~372.80 on 2026-07-13, now 372.29). This is the signature of a mid-term consolidation/rollover after the May peak.
- **Short-term (stabilizing/recovering):** Price closed **just above the 10 EMA (358.25, +0.35%)** and **above the VWMA (350.76, +2.5%)**, and above the Bollinger middle (357.61). The 10 EMA bottomed near 352.0 (2026-06-26) and has flattened near 358–360. Short-term momentum has clearly stabilized versus the June slide.

**Summary:** A structurally bullish long-term chart that is in a medium-term digestion phase; the short-term tape is attempting to turn back up but has not yet reclaimed the pivotal 50 SMA.

---

## 3. Momentum Analysis
**MACD (line −1.93 / signal −2.63 / histogram +0.70):** MACD bottomed at −7.35 on 2026-06-26 and has recovered sharply to −1.93. The MACD line crossed **above** the signal line around **2026-07-02** (histogram flipped positive) — a classic early-recovery buy signal. **Caveat:** both MACD and signal remain **below zero**, so this is a bullish crossover *inside bearish territory* (a repair signal, not yet a confirmed trend). The histogram has also begun to **fade** (from ~+1.31 around 2026-07-06 to +0.70 today), meaning the recovery thrust is losing a little steam — it needs a fresh push to stay valid.

**RSI (49.35):** Neutral. RSI recovered from an early-June trough of **33.27 (2026-06-26)** to as high as **54.0 (2026-07-07)** and has eased back to 49.35. It is dead-center — no overbought/oversold signal, consistent with a two-way range. There is room to run in either direction before RSI reaches an extreme (70/30), so RSI is currently a *neutral filter*, not a trigger.

**Volume (VWMA 350.76):** Price sits above the volume-weighted average, so buyers hold a modest edge on a volume basis. However, VWMA has been flat at ~350–352 since late June, confirming a **consolidation base** rather than a decisive breakout. Note the **capitulation-style volume spike of 114.7M on 2026-06-26** (the correction low) — a potential seller-exhaustion event. Recent up-days, by contrast, are on lighter volume (~15–26M), which is a **mild caution** — the bounce lacks strong volume conviction.

---

## 4. Volatility & Risk
**ATR (10.31, ~2.87% of price):** Volatility remains **elevated** but is **declining** — ATR peaked at 12.25 (2026-06-29) and has eased to 10.31. It was ~9.3–9.5 in late May, so we are still in an above-normal volatility regime driven by the June selloff.

**Bollinger (middle 357.61 / upper 376.69 / lower 338.54):** Bandwidth is wide (~10.7% of the middle band), reflecting the elevated volatility. Price (359.51) sits just above the middle band — the upper half of the envelope, but well inside the bands (not a breakout, not oversold). 

**Risk-management implications:**
- A 1.5×ATR stop ≈ **~15.5 points**; a 1×ATR stop ≈ ~10.3 points. For swing longs from ~359, a stop below the VWMA/support cluster at ~**350** (≈ −9 pts, ~0.9×ATR) or, for more room, below ~338 (−6%).
- Position sizing should account for ~2.9% daily average range.

---

## 5. Key Levels & Actionable Scenarios
**Resistance (overhead):**
1. **372.29** — 50 SMA (primary medium-term hurdle; flattening).
2. **373.16** — 2026-07-07 swing high.
3. **376.0–376.69** — June 16 high + Bollinger upper band (confluence).
4. **~400–403** — May closing highs (full recovery zone).

**Support (below):**
1. **357.6–358.3** — Bollinger middle + 10 EMA (price is riding this now).
2. **350.8** — VWMA + round 350 (the consolidation floor; the level buyers defended on 2026-07-14 from a 351.09 low).
3. **338.5–340** — Bollinger lower band + late-June closing lows (337–346).
4. **330.2** — 2026-06-26 intraday capitulation low (major structural support).

**Scenarios:**
- **Bullish (recovery continuation):** A daily close **above the 50 SMA (~372)** on expanding volume would confirm the MACD repair and open 376 → 400. Watch for volume to confirm (recent rallies have been light).
- **Range (base case):** Choppy **350–372** consolidation. Range traders: buy the 350–352 VWMA floor, sell/take profit near the 50 SMA.
- **Bearish (failed bounce):** A decisive break **below 350 (VWMA)** would invalidate the base and target 338–340, then 330. The fading MACD histogram and light-volume bounce are the early warning signs to monitor here.

---

## 6. Trading Stance
- **Bias: cautiously constructive within a neutral-to-corrective range.** The long-term uptrend (price >> rising 200 SMA, 50>200) is intact, and short-term momentum has repaired (MACD bullish cross, price back above the 10 EMA/VWMA/Boll middle).
- **But confirmation is incomplete:** price is still below the 50 SMA, MACD remains sub-zero with a shrinking histogram, RSI is neutral, and the bounce is on light volume.
- **Practical approach:** Treat **350** as the bull/bear line for the near term and **372 (50 SMA)** as the upside trigger. Add on a volume-backed close above 372; defend/stop below 350; remain neutral in between.

---

## 7. Key Metrics Summary

| Metric | Value (2026-07-14) | Signal / Interpretation |
|---|---|---|
| Close | 359.51 | Reversal day; +2.0% off prior close |
| 200 SMA | 319.98 (rising) | Bullish — price +12.4% above |
| 50 SMA | 372.29 (flattening/rolling) | Bearish/corrective — price −3.4% below; key resistance |
| 10 EMA | 358.25 | Price just above — short-term stabilizing |
| MACD / Signal | −1.93 / −2.63 | Bullish crossover (hist +0.70) but sub-zero |
| MACD Histogram | +0.70 (fading from ~1.31) | Recovery thrust losing momentum |
| RSI | 49.35 | Neutral — no overbought/oversold |
| ATR | 10.31 (~2.87%) | Elevated but declining volatility |
| Bollinger Mid / UB / LB | 357.61 / 376.69 / 338.54 | Price in upper half, inside bands; wide bandwidth |
| VWMA | 350.76 | Price above; flat → consolidation base |
| Resistance | 372.3 / 373.2 / 376.7 / ~400 | 50 SMA → July high → Boll UB/Jun high → May peak |
| Support | 357.6 / 350.8 / 338.5 / 330.2 | Boll mid+10EMA / VWMA / Boll LB+Jun lows / Jun intraday low |
| Volume note | 114.7M on 2026-06-26 | Capitulation spike at low; light volume on bounce |
| Structural backdrop | 50 SMA > 200 SMA | Golden-cross / long-term uptrend intact |

**Discrepancy check:** The standalone indicator pulls and the verified snapshot agree on all values (close 359.51, 50 SMA 372.29, 200 SMA 319.98, 10 EMA 358.25, MACD −1.93/−2.63, RSI 49.35, ATR 10.31, VWMA 350.76). No conflicts to flag.

*This is a technical analysis for informational purposes, not investment advice. Levels are derived from the tool data above; always confirm with live data and manage risk.*