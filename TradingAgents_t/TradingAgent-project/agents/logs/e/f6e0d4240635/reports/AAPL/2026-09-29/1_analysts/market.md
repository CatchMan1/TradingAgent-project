# AAPL — Technical Analysis Report
**As of close 2026-09-29 | Verified snapshot source of truth**

---

## 1. Executive Summary

AAPL remains in a **structurally intact, long-term uptrend** that is currently going through a **short-term corrective phase**. The 2026-09-29 session was the weakest in weeks: a -2.66% decline to **$329.40** on a **gap-down open ($336.97)** and a **close near the session low ($328.70)**. This broke a six-session shelf at $334–$335 and produced the **first negative MACD histogram reading since 2026-08-25**, a fresh bearish momentum cross.

Critically, this is a pullback **inside** a bull structure, not a trend break:
- Close is **+2.3% above the 50-day SMA ($321.98)** and **+14.2% above the 200-day SMA ($288.33)**, both rising.
- The 50-day SMA sits **11.7% above** the 200-day SMA — a wide, healthy bullish separation.
- The pullback has occurred **without volume expansion** (38.5M vs. an approximate 20-day average of ~42.5M derived from the OHLCV rows), and RSI has reset to neutral (50.9) rather than collapsing into oversold.

**Net read: bullish primary trend, deteriorating short-term momentum, unresolved 1–2 week direction. The burden of proof has shifted to the bulls to reclaim $334.8–$336.**

*Data integrity note: `get_stock_data` and `get_verified_market_snapshot` agree exactly on the 2026-09-29 row (O 336.97 / H 337.09 / L 328.70 / C 329.40 / V 38,478,000). No discrepancy to flag.*

---

## 2. Verified Market State (2026-09-29)

| Metric | Value |
|---|---|
| Close | **$329.40** |
| Open / High / Low | $336.97 / $337.09 / $328.70 |
| Day change | **-$9.00 (-2.66%)** from $338.40 |
| Volume | 38,478,000 |
| 10 EMA | $334.77 |
| 50 SMA | $321.98 |
| 200 SMA | $288.33 |
| MACD / Signal / Hist | 5.188 / 5.471 / **-0.283** |
| RSI(14) | **50.88** |
| ATR(14) | **$7.04 (2.14% of price)** |
| VWMA | $333.99 |
| Bollinger Mid / Upper / Lower | $330.96 / $346.27 / $315.65 |

---

## 3. Structural Trend: Bullish, But Price Is Extended

The medium- and long-term trend structure is unambiguously constructive.

- **200 SMA = $288.33**, rising every session in the sample: $280.67 on 2026-08-17 → $288.33 on 2026-09-29 (+2.7% in ~30 sessions). Slow, steady accumulation trend.
- **50 SMA = $321.98**, also rising monotonically over the same window ($309.08 → $321.98, +4.2%). The 50 SMA has been above the 200 SMA throughout — the golden-cross regime is well established, and the gap is still widening (+11.7%).
- Trough-to-peak in the data window: **$246.63 (2026-03-30) → $345.34 (2026-09-22 intraday) = +40.0%**. The February–March correction ($278 → $246.63) was fully recovered and exceeded.

The caveat: at $329.40 the stock is still **2.3% above the 50 SMA** after a five-session decline. That is not yet a true mean-reversion test — it is a *partial* reset. Historically in this dataset, deeper pullbacks have reached the 50 SMA or below (e.g., the July 31 drop took price from $333.43 to $308.91, below the then-50 SMA).

**Implication:** The 50 SMA at **$321.98** is the single most important medium-term line in the sand. A daily close below it would convert "pullback" into "trend damage."

---

## 4. Short-Term Momentum: Clear Deterioration

### 10 EMA — lost
The 10 EMA rose from $308.76 (2026-08-17) to a peak of **$335.96 (2026-09-28)** and has now rolled to $334.77. Price closed **$5.37 (1.60%) below it**. The 10 EMA is flattening/turning — the first time since the September advance began. Short-term trend bias is now neutral-to-down.

### MACD — fresh bearish crossover
- MACD line peaked at **6.248 on 2026-09-22** and has fallen to **5.188** on 2026-09-29.
- Signal line is **5.471**; histogram flipped from **+0.537 (9/28)** to **-0.283 (9/29)**.
- This is the **first negative histogram since 2026-08-25** — a clean, fresh bearish crossover, not a stale one.

**Important nuance — momentum divergence preceded the drop:** MACD histogram made successively lower highs while price made higher highs:

| Date | Price High | MACD Hist |
|---|---|---|
| 2026-09-03 | $330.81 | +2.028 |
| 2026-09-17 | $338.34 | +1.686 |
| 2026-09-22 | $345.34 | +1.544 |

The *rate of change* of the uptrend was already decaying for three weeks before the 9/29 break. This raises the odds that the -2.66% day is a **momentum resolution**, not a random noise event.

---

## 5. RSI: Neutral, Not Oversold — Room to Fall

- RSI = **50.88**, down **10.9 points in a single session** from 61.79.
- The September rally topped out at **66.88 (2026-09-22)** — notably, RSI **never reached 70**. AAPL was never technically overbought on this leg, which argues *against* the idea that this is an exhaustion top driven by froth.
- **No bearish RSI divergence** at the 9/22 high: RSI 65.39 (9/17) → 66.88 (9/22) confirmed the higher price high.
- In this dataset, pullback lows have seen RSI settle in the **low-to-mid 40s** (e.g., 43.41 on 2026-08-17 during the August base, with price near $305). RSI at 50.9 is **only halfway** through a typical reset.

**Implication:** There is a realistic path to further downside without any oversold cushion. RSI in the 40–45 zone near $315–$322 would be the higher-quality "buy the dip" setup.

---

## 6. Volatility & Bollinger Context

- **ATR = $7.04 (2.14% of price)**, up modestly from $6.83 on 9/28 but down from the local peak of $8.05 on 9/11. Volatility is **normalizing, not spiking** — consistent with an orderly pullback.
- The 9/29 range was **$8.39 (1.19 ATR)**, with the close in the bottom ~8% of the range — a weak, seller-controlled close.
- **Bollinger Bands:** Mid $330.96, Upper $346.27, Lower $315.65. Price closed **just below the mid-band (-0.47%)** after riding the upper half through September. The upper band at $346.27 essentially caps the 9/22 high of $345.34 — the band contained the advance. Bandwidth is wide (~9.3% of mid), so a move to the lower band is a $15 slide, not a crash.

**ATR-derived levels:**
- 1.5 ATR below close: **$318.85**
- 2.0 ATR below close: **$315.33** — coincidentally almost exactly the lower Bollinger Band ($315.65)

---

## 7. Volume: The Most Constructive Datapoint

- 9/29 volume **38.48M** vs. approximate 20-day average **~42.5M** → roughly **0.9x average**. A -2.66% break on *below-average* volume is **not characteristic of institutional distribution**.
- VWMA = **$333.99**; price is **1.39% below** it. This means the average dollar-weighted buyer of the recent volume profile is underwater. That creates overhead supply on rallies toward $334–$336 — a real resistance cluster.
- For reference, genuine heavy-volume events in this dataset were: **86.59M on 9/18** (likely expiration-related), **70.01M on 9/10** (an up day, +3.6%, constructive accumulation), and **132.49M on 7/31** (a -7.4% shock day).
- **Event-risk warning:** this stock has produced two -5%+ single-session gaps in the last four months — **2026-06-25 (-6.1%, 107.0M shares)** and **2026-07-31 (-7.4%, 132.5M shares)**. ATR understates this tail risk. Size positions for gap risk, not just daily ATR.

---

## 8. Key Levels & Scenarios

### Resistance
| Level | Source |
|---|---|
| $330.96 | Bollinger mid-band (just overhead) |
| $333.99 | VWMA — recent buyers' breakeven |
| $334.77 | 10 EMA — first momentum reclaim |
| $337.0–$338.4 | 9/28 close & 9/29 gap origin |
| $341.07 | 9/25 close |
| **$345.34 / $346.27** | 9/22 swing high / Bollinger upper |

### Support
| Level | Source |
|---|---|
| **$321.98** | **50 SMA — primary medium-term support** |
| $317.86 | 9/4 low |
| $315.65 | Bollinger lower band |
| $315.33 | 2 ATR below close |
| $314.90 | 9/8 low |
| **$309.90** | 9/9 low — September base |
| $300.57 | 8/12 low — August base |

### Scenario A — Bullish repair (needs confirmation)
A close back above **$334.77 (10 EMA)** and, better, **$336–$338**, with volume above ~42.5M would re-establish the 10 EMA and neutralize the MACD cross. Target retest of $345.34 / $346.27. This scenario is supported by the intact 50>200 structure and the lack of volume on the selloff.

### Scenario B — Deeper mean reversion (currently the path of least resistance)
Failure to reclaim $334.8 keeps pressure toward **$322 (50 SMA)**. A decisive close below $322 opens **$315–$317** (lower band + 2 ATR + 9/8 low). A close below $314.9 would put the **$309.90** September low in play.

### Scenario C — Trend damage
A weekly close below **$310** would break the September base and put the 200 SMA at $288.33 in scope. Low probability given the slope of the long-term average, but it is the defined invalidation of the bull thesis.

---

## 9. Actionable Positioning Guidance

**For existing holders (trend-following):**
- Hold. The primary trend is intact. Use **$321.50–$322.00** (just under the 50 SMA) as a tactical trailing stop, or **$315.30 (2 ATR)** for wider swing tolerance. Do not use stops tighter than 1 ATR ($7) — daily noise alone is ~2%.
- Do **not** add here. The risk/reward at $329 is poor: ~$5 to first resistance ($334.8) versus ~$8 to support ($322). Wait for either a reclaim of $335 or a test of $322/$315.

**For new buyers:**
- Preferred entry zone: **$318–$322**, ideally with RSI in the low-to-mid 40s and declining volume (a classic uptrend pullback signature).
- Secondary aggressive trigger: a **volume-backed reclaim of $335** (volume > ~42.5M), targeting $345+.
- Avoid initiating in the $329–$334 no-man's land where both the 10 EMA and VWMA sit directly overhead.

**For short-term traders:**
- The 9/29 close below the $334.3–$335.5 shelf with a negative MACD histogram favors **short-side tactical setups** with stops above $336.5 and targets $322 / $318.
- But note: the below-average volume on the decline weakens conviction. Take profits near the 50 SMA rather than holding for a breakdown.

**Position sizing:** With ATR at 2.14% of price, a 1% account risk per trade implies roughly a **0.47x notional position** using a 1-ATR stop — and gap risk (two -6% to -7% days in 4 months) argues for halving that.

---

## 10. Indicator Selection Rationale

| Indicator | Why selected | What it contributes |
|---|---|---|
| **close_200_sma** | Long-term regime filter | Confirms the bull market (+14.2% above, rising) — prevents overreacting to a short-term dip |
| **close_50_sma** | Medium-term trend + dynamic support | Defines the pullback's first real test at $321.98 and the line between "dip" and "damage" |
| **close_10_ema** | Fast trend/momentum | Captures the exact point momentum was lost ($334.77) and provides the first reclaim trigger |
| **macd** | Trend momentum | Shows the September impulse peaking at 6.25 and rolling over |
| **macdh** | Crossover timing + divergence | The fresh -0.283 flip plus the lower-high sequence (2.03→1.69→1.54) was the early warning |
| **rsi** | Overbought/oversold & divergence | Establishes that there was **no** overbought extreme and **no** bearish divergence — a reset, not exhaustion |
| **atr** | Volatility / risk sizing | $7.04 ATR sets stops ($315.33 = 2 ATR) and position size; sized for a 2.1% daily range |
| **vwma** | Volume-price confirmation | Price below $333.99 VWMA = overhead supply from recent buyers, and volume analysis shows the selloff lacked conviction |

*Deliberately excluded:* Bollinger upper/lower and raw volume indicators as "selected" signals to avoid redundancy with ATR (volatility) and VWMA (volume). The Bollinger values from the verified snapshot are used above as corroborating context only — notably the lower band at $315.65 converging almost exactly with the 2-ATR level, which strengthens that support zone. StochRSI was excluded as redundant with RSI.

---

## 11. Key Points Summary

| Dimension | Reading (2026-09-29) | Interpretation | Action |
|---|---|---|---|
| **Long-term trend** | Close $329.40 vs 200 SMA $288.33 (+14.2%) | Strong, rising bull regime | Stay structurally long |
| **Medium-term trend** | Close vs 50 SMA $321.98 (+2.3%); 50>200 by 11.7% | Intact, but support is close | Hold, stop under $322 |
| **Short-term trend** | Close $5.37 below 10 EMA $334.77 | Momentum lost | No new buys at $329 |
| **MACD** | 5.188 < signal 5.471; hist **-0.283** | **Fresh bearish cross** (first since 8/25) | Favors patience / tactical short |
| **MACD divergence** | Hist lower highs 2.03→1.69→1.54 into 9/22 price high | Impulse was fading pre-drop | Confirms corrective risk |
| **RSI** | **50.88**, -10.9 pts in one day; Sept peak only 66.9 | Neutral, no oversold cushion | Wait for 40–45 for better entry |
| **ATR** | $7.04 (2.14%) | Normal volatility, no spike | Stops ≥1 ATR; size for gaps |
| **VWMA** | $333.99 — price 1.39% below | Recent buyers underwater | $334–$336 is overhead supply |
| **Volume** | 38.48M ≈ 0.9x 20-day avg | Decline lacked conviction | Mildly constructive, not decisive |
| **Bollinger** | Mid $330.96 / Up $346.27 / Low $315.65 | Price just below mid-band | $315.65–$315.33 confluence support |
| **Immediate resistance** | $334.77 → $338.4 → $345.34/$346.27 | Reclaim needed to repair | Buy trigger >$335 on volume |
| **Immediate support** | $321.98 → $315.65 → $309.90 → $300.57 | Layered shelf | Buy zone $318–$322 |
| **Base case** | Pullback within uptrend; 1–2 weeks of digestion | Neutral near-term, bullish medium-term | Hold; add lower or on reclaim |

**Bottom line:** AAPL's bull market is not broken, but its September impulse is. The evidence — a lost 10 EMA, a fresh negative MACD histogram after a three-week momentum divergence, a weak close near the session low, and price below VWMA — points to **further digestion toward $322, with $315–$317 as the deeper target**. Two factors argue against aggressive bearishness: the selloff came on below-average volume, and RSI never reached overbought, so this is more likely a **reset than a reversal**. The cleanest risk/reward is to let price come to the **$318–$322 zone** or to buy a **confirmed reclaim of $335 on above-average volume** — not to commit at $329.40.