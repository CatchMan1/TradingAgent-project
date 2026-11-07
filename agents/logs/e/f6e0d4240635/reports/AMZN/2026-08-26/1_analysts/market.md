# AMZN — Multi-Timeframe Technical Assessment
**Analysis date: 2026-08-26 | Verified close: $260.28**

---

## 1. Data integrity note

I cross-checked every indicator series from `get_indicators` against `get_verified_market_snapshot` for 2026-08-26. **All twelve values match to the decimal** (50 SMA 250.8754, 200 SMA 238.5303, 10 EMA 261.9666, MACD 2.4348, Signal 3.8996, Histogram −1.4648, RSI 50.8766, Bollinger mid 266.1040 / upper 286.6093 / lower 245.5987, ATR 6.8206, VWMA 265.5298). No conflicts to flag on price or technicals.

One anomaly worth flagging: the snapshot reports **MFI = 0.362862**, which is inconsistent with a standard 0–100 money-flow scale and cannot be reliably interpreted. I excluded MFI from the analysis rather than invent a conversion.

---

## 2. The dominant context: a post-earnings impulse that is now coiling

The single most important structural fact in this dataset is the **July 30–August 3 repricing**:

| Date | Close | Volume | Note |
|---|---|---|---|
| 2026-07-29 | $226.65 | 44.96M | 2026 summer low close |
| 2026-07-30 | $235.50 | 101.84M | earnings-day surge, high 239.82 |
| 2026-07-31 | $271.58 | 129.05M | gap up: open 265.00, high 273.23 |
| 2026-08-03 | $284.02 | 90.83M | high **287.20** — highest print in dataset |

That is **+25.3% from the 2026-07-29 close to the 2026-08-03 close in three sessions**, on roughly 3–4× normal volume. Since then AMZN has given back part of it: **$284.02 → $260.28 = −8.4%**, but the retreat has been orderly, on *shrinking* volume.

Two derived references from tool closes:
- **38.2% retracement of the 226.65→284.02 advance = $262.10** — already lost on 2026-08-13.
- **50% retracement = $255.34**; **61.8% = $248.57**.
- The unfilled gap spans **$239.82 (07-30 high) → $265.00 (07-31 open)**. Price re-entered the gap on 2026-08-13 (low 264.71) and has not reclaimed $265.00 since. Notably, a *full* gap fill (~$239.82) would land almost exactly on the **200 SMA at $238.53**.

---

## 3. Trend structure: bullish across medium/long term, corrective short term

**Long term (200 SMA) — constructive.** 200 SMA = **238.530**, up every single session in the window (235.01 on 07-31 → 238.53 on 08-26). Price sits **+9.12% above** it.

**Medium term (50 SMA) — constructive and inflecting up.** 50 SMA = **250.875**, having bottomed at 246.384 on 2026-07-30 and risen for 18 consecutive sessions. Price is **+3.75% above** it. The **50/200 spread is +5.18%** (12.35 points) and widening — a persistent golden-cross regime, not a fresh one.

**Short term (10 EMA) — negative.** 10 EMA = **261.967**; price is **−0.65% below** it. The 10 EMA peaked at 267.18 on 2026-08-12 and has rolled over modestly. It is flattening rather than plunging, which matters: the pullback is losing force.

**Synthesis:** this is a textbook *bullish-trend correction*, not a trend break. The violated averages are all short-horizon; the rising 50 and 200 SMA lines sit 3.8% and 9.1% below.

---

## 4. Momentum: the impulse has fully decayed, and is now flat-lining

**MACD (2.4348) vs Signal (3.8996) vs Histogram (−1.4648)**
- MACD peaked at **8.4324 on 2026-08-11** and has fallen **−71%** to 2.4348. It remains **above zero**, so the regime is still net-positive momentum, merely decelerating.
- The bearish crossover occurred **2026-08-17** (histogram −0.3097), the histogram bottomed at **−1.538 on 2026-08-21**, and the last four readings are **−1.472 → −1.460 → −1.465**. That is *stabilization*, not fresh deterioration. A histogram that stops making lower lows while price holds a flat base is the classic precondition for a re-cross, but it is **not yet a signal** — it needs a close back above ~266 to validate.

**RSI 50.88 — a clean reset with no divergence.**
RSI went from **72.23 on 2026-08-03** (genuinely overbought) to **49.74 on 2026-08-21**, and is now 50.88. Comparing price peaks and RSI peaks through August (284.02/72.23 on 08-03; 278.09/65.87 on 08-10; 265.84/55.64 on 08-19) shows **lower highs in both series — a correlated decline, not a bearish divergence**. The key implication: RSI at 50.9 is *neutral with room in either direction*; it is neither a buy-the-dip oversold reading nor an exhaustion top. It offers no edge by itself right now, which is itself informative — it argues against chasing.

---

## 5. Volatility: a genuine squeeze — the most actionable signal in the dataset

**ATR has collapsed to 6.8206** (2.62% of price), from **9.9827 on 2026-08-05** (3.66%) — a **−31.7% contraction in three weeks**. Recent realized daily ranges confirm the compression is ongoing rather than stale: 2026-08-24 range 4.27, 08-25 range 4.06, 08-26 range 3.81 — all well *below* the 6.82 ATR.

Bollinger corroboration (from tool output, used as cross-reference rather than a primary selection since ATR already measures the same risk):
- **Bandwidth collapsed from 29.6% (2026-08-19: upper 296.99 / lower 220.47, mid 258.73) to 15.4% (2026-08-26: upper 286.61 / lower 245.60, mid 266.10)** — a **~48% narrowing in five sessions**.
- The mechanism is striking: the **upper band is falling** (296.99 → 286.61) while the **lower band is rising violently** (220.47 → 245.60). Both bands are converging on price. That is a textbook volatility coil, and it typically resolves in a directional expansion.

**Price vs. the Bollinger frame:** close 260.28 is **−2.19% below** the mid (266.10) and well above the lower band (245.60). Mid-band is rising (254.99 on 08-12 → 266.10 on 08-26), so the *mean* is still climbing even as price sits beneath it.

**Structure of the coil:** consecutive swing highs — 287.20 (08-03), 282.79 (08-05), 280.14 (08-10), 278.84 (08-11), 273.46 (08-12), 269.58 (08-13), 266.40 (08-19), 263.89 (08-25), 262.05 (08-26) — form a clean **descending ceiling**. Swing lows — 267.10 (08-12), 262.42 (08-14), 258.34 (08-17), 257.73 (08-18), **257.04 (08-21)**, 259.05 (08-24), 258.24 (08-26) — form a **flat floor near 257–259**. The last five closes (260.11, 258.63, 262.07, 261.06, 260.28) span just **3.44 points = 1.3%**. This is a tightening apex, and it resolves soon.

---

## 6. Volume: distribution risk is being *priced out*, not confirmed

**VWMA = 265.530**, and price is **−1.98% below it**. This is the most underrated bearish tell in the file: the volume-weighted cost basis of recent sessions sits 5.25 points *above* spot, meaning **the marginal buyer since the gap is underwater**, and 265–266 is a supply zone. VWMA peaked at 272.05 on 08-20 and is now rolling down.

But the crucial nuance is the **volume profile**, which is bullish-leaning:
- Pullback average volume (08-12 → 08-26, 11 sessions): **≈31.0M/day**. The markup sessions were 129.05M (07-31) and 90.83M (08-03) — the reversal-down has occurred on **roughly one quarter of the markup's volume**.
- **2026-08-26 volume was 21.53M — the lowest single-day volume in the entire 163-row dataset** (prior dataset low ~25.3M on 2026-04-06). Declining price on record-low volume is more consistent with seller exhaustion and pre-breakout coiling than with active distribution.
- Caveat: 2026-06-26 printed **248.37M** (an outlier, likely an index/rebalance event) and 2026-02-06 printed **179.21M** during the February collapse — volume spikes in this name can be mechanical, so treat single-day prints with skepticism.

---

## 7. The critical price zone: 265–266

Three independent measures converge there:
- **VWMA: 265.530**
- **Bollinger mid (20 SMA): 266.104**
- **2026-07-31 gap open: 265.00**
- (10 EMA at 261.967 sits just below, adding a minor layer at ~262)

A close **above 266.10** would simultaneously (a) reclaim the volume-weighted cost basis, (b) reclaim the 20-period mean, (c) put price back above the earnings-gap origin, and (d) very likely flip the MACD histogram. That is the highest-quality long trigger available. Until then, rallies into 261–266 are counter-trend.

Support ladder below: **257.04** (08-21 swing low) → **255.34** (50% retracement) → **250.875** (rising 50 SMA) → **245.599** (Bollinger lower band, rising fast) → **238.53** (200 SMA, coincident with the full gap-fill and the 61.8% retracement at 248.57 acting as an intermediate shelf).

---

## 8. Actionable playbook

**Bias:** constructive/neutral-to-bullish on the medium term; tactically *wait* — the squeeze is unresolved and neither side has paid yet. Chasing either direction inside 257–266 is a low-expectancy trade.

**Long setup (preferred, needs confirmation):**
- Trigger: daily close **> 266.10** (ideally on volume > 40M, i.e. above the ~31M pullback average).
- Level-1 target: **272.27–274.48** (2026-08-11/08-12 closes) → Level-2: **284.02** (08-03 close) → Level-3: **287.20** (08-03 high).
- Invalidation: close back below **261.97** (10 EMA), hard stop below **257.04**.
- Stop distance ≈ 9.1 points from a 266.10 trigger = **1.34 × ATR** — a reasonable, volatility-scaled risk.

**Short setup (counter-trend, tactical only):**
- Trigger: daily close **< 257.04** (breaks the flat floor and the 38.2% retracement structure).
- Targets: **250.88** (50 SMA) → **245.60** (lower band). A sustained break of 250.88 would be the first genuine medium-term trend damage and would open the gap-fill toward 238.53.
- Invalidation: close back above **262.10**.

**Risk management specifics:**
- ATR = **6.82 (2.62%)** → 1.5×ATR stop ≈ 10.2 pts; 2×ATR ≈ 13.6 pts.
- **Sizing caution:** mechanical ATR-based sizing will size *up* here precisely because volatility is compressed — right before a coil resolution that could expand range sharply. Use a volatility floor (e.g., size as if ATR were the ~9.5–10.0 seen on 2026-08-05) or reduce gross exposure until the range breaks.
- Event risk is asymmetric: the July 31 repricing proves this name gaps 13–15% on catalysts. Being short into an unresolved coil with a 200 SMA rising underneath carries gap risk.

---

## 9. Key takeaways

1. **Trend is up, momentum is not.** Price is above a rising 50 SMA (+3.75%) and 200 SMA (+9.12%), but below the 10 EMA, 20 SMA, and VWMA — a corrective pause inside a bull structure.
2. **MACD above zero but halved** (−71% from the 08-11 peak); bearish histogram since 08-17 is **flattening**, an early but unconfirmed turn signal.
3. **RSI 50.9 = pure no-man's-land.** No oversold edge, no overbought risk, no divergence.
4. **Volatility squeeze is the trade.** ATR −31.7% and Bollinger bandwidth −48% in five sessions; five closes inside 1.3%. Expansion is imminent; direction is not yet determined.
5. **265–266 is the fulcrum** (VWMA + 20 SMA + gap open). Above = long. Below **257.04** = short. Between = no trade.
6. **Volume argues for the bulls** — record-low 21.5M on 2026-08-26, pullback volume ~31M vs. 129M/91M on the markup.

---

## 10. Summary table

| Dimension | Indicator (selected) | 2026-08-26 Reading | Signal | Interpretation / Level |
|---|---|---|---|---|
| Short-term trend | `close_10_ema` | 261.967 | Bearish | Price −0.65% below; EMA flattening, not plunging. Reclaim = first sign of life |
| Medium-term trend | `close_50_sma` | 250.875 | **Bullish** | +3.75% above; rising 18 straight sessions from 246.384 (07-30). First major support |
| Long-term trend | `close_200_sma` | 238.530 | **Bullish** | +9.12% above; 50/200 spread +5.18% and widening. Full gap-fill ≈ 200 SMA |
| Momentum regime | `macd` | 2.4348 | Weakening but positive | Above zero, yet −71% from 8.4324 (08-11 peak) |
| Momentum timing | `macdh` | −1.4648 | Bearish, decelerating | Negative since 08-17; bottomed −1.538 (08-21), now flat → re-cross watch |
| Momentum level | `rsi` | 50.88 | Neutral | Down from 72.23 (08-03) to 49.74 (08-21); no divergence; no edge |
| Volatility / risk | `atr` | 6.8206 (2.62%) | **Squeeze** | −31.7% from 9.9827 (08-05). 1.5×ATR stop ≈ 10.2 pts |
| Volume conviction | `vwma` | 265.530 | Bearish (mild) | Price −1.98% below volume-weighted cost → overhead supply at 265–266 |
| *Cross-check* | Bollinger mid / UB / LB | 266.104 / 286.609 / 245.599 | Squeeze | Bandwidth 15.4% vs 29.6% on 08-19; lower band up from 220.47 |
| *Cross-check* | Volume | 21.53M | Bullish | **Lowest daily print in the 163-row dataset**; pullback avg ≈31M vs. 91–129M on markup |
| **Resistance** | — | 265.00 / 266.10 / 272.3–274.5 / 284.02 / 287.20 | — | 265–266 = VWMA + 20 SMA + gap open confluence |
| **Support** | — | 257.04 / 255.34 / 250.88 / 245.60 / 238.53 | — | 257.04 = flat floor; 250.88 = 50 SMA; 238.53 = 200 SMA |
| **Trigger — Long** | — | Close > 266.10, volume > 40M | — | Invalid below 261.97; stop < 257.04 |
| **Trigger — Short** | — | Close < 257.04 | — | Targets 250.88 → 245.60; invalid above 262.10 |

*All price levels and indicator values above are taken from, or arithmeticically derived from, the verified 2026-08-26 snapshot and the corresponding indicator series. Retracement levels are my own calculations from tool-supplied closes. No claim of historical support/resistance "bounces" is made — levels are reference points, not validated pivots.*