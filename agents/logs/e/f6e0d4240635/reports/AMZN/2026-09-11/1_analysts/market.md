# AMZN — Multi-Timeframe Technical Report
**As of close 2026-09-11 | Last price: $256.78**

---

## 1. Executive summary

AMZN is in a **medium- and long-term uptrend that is being digested by a six-week short-term corrective downtrend**. The stock has not broken its primary structure — price sits above a rising 50-day SMA, which sits above a rising 200-day SMA — but momentum, volume-weighted pricing, and the pattern of lower highs/lower lows since the August 3 peak all argue that the correction is **not yet conclusively finished**.

The 2026-09-11 session was constructive: a +1.94% close (+$4.89) that finished at 81.8% of the day's range and reclaimed the 50-day SMA. However, that bounce occurred on **26.72M shares, roughly 84% of the ~31.9M-share simple average of the prior 22 sessions**, so it lacks the volume confirmation that would make it a high-conviction reversal signal. The tactical bias is therefore **neutral-to-cautiously-constructive: wait for confirmation rather than chase**.

**Verdict: HOLD / wait-for-trigger. Bullish above ~$259 on volume; bearish below ~$251.**

---

## 2. Price structure and the post-gap consolidation

### 2.1 The event-driven gap still defines the map
On 2026-07-30 AMZN closed $235.50. On 2026-07-31 it opened $265.00 and closed $271.58 — a **+15.32% one-day move on 129.05M shares**, roughly 4x the recent volume baseline. The unfilled gap runs from the 07-30 high of **$239.82** to the 07-31 open of **$265.00**. Six weeks later, the gap remains entirely unfilled, which is itself evidence that the repricing has held. (The dataset does not label the catalyst; the analysis treats it purely as a volume-confirmed repricing event.)

The post-gap high was **$287.20 (intraday) / $284.02 (close) on 2026-08-03**, on 90.83M shares. From that peak:
- Close-to-close: $284.02 → $256.78 = **−9.59%**
- High-to-Sep-10-low: $287.20 → $249.58 = **−13.10%**

### 2.2 Lower highs, lower lows — but decelerating
The correction has produced a **consistent sequence of lower lows**:

| Swing | Low | Date |
|---|---|---|
| 1 | $270.73 | 2026-08-05 |
| 2 | $262.42 | 2026-08-14 |
| 3 | $257.73 | 2026-08-18 |
| 4 | $257.04 | 2026-08-21 |
| 5 | $251.93 | 2026-09-01 |
| 6 | **$249.58** | **2026-09-10** |

Lower highs are present but **not perfectly monotonic**: $287.20 (08-03) → $280.14 (08-10) → $266.40 (08-19) → $267.56 (08-28, a marginal higher high) → $261.12 (09-04) → $257.59 (09-11). The 08-28 pop failed, which keeps the descending-highs framework intact.

### 2.3 Fibonacci confluence at the September low
Measured on the full post-gap impulse (intraday low $226.16 on 2026-07-29 to high $287.20 on 2026-08-03, range $61.04):
- **61.8% retracement ≈ $249.48** — the 2026-09-10 low was **$249.58**, an almost exact tag.
- **50% retracement ≈ $256.68** — the 2026-09-11 close was **$256.78**, essentially sitting on it.

This is arithmetic derived from the tool's OHLC data, not a vendor-computed level, and it is *not* proof of a bottom. But the coincidence of the corrective low with the 61.8% retracement, followed by a strong-bodied reversal day, is a legitimate reason to treat $249.5–$250 as the near-term line that matters.

### 2.4 Gap-fill and resistance micro-structure
- 2026-08-31 low: $257.12; 2026-09-01 open: $254.83, high $255.82 → a **downside gap zone of $255.82–$257.12**.
- On 2026-09-11 AMZN traded $253.14–$257.59, **fully covering that gap zone**, and closed at $256.78 inside it.
- That overhead gap fill plus the VWMA ($257.95), Bollinger mid-band ($258.96), and the 09-03 high ($259.50) creates a **dense resistance cluster in the $257.9–$259.5 area**.

---

## 3. Indicator-by-indicator read

**Selected set (8): `close_10_ema`, `close_50_sma`, `close_200_sma`, `macd`, `macds`, `rsi`, `atr`, `vwma`.** Bollinger levels from the verified snapshot are used as corroborating context. Rationale: three time horizons of trend (10-day, 50-day, 200-day), two momentum-regime signals (MACD line and signal), one mean-reversion/divergence gauge (RSI), one volatility/risk-sizing input (ATR), and one volume-weighted conviction gauge (VWMA). No two indicators in this set measure the same thing, and none are redundant oscillators.

### 3.1 Trend structure — `close_10_ema`, `close_50_sma`, `close_200_sma`
| Metric | Value | Price vs. level |
|---|---|---|
| 10 EMA | **$256.59** | +$0.19 (+0.07%) |
| 50 SMA | **$255.25** | +$1.53 (+0.60%) |
| 200 SMA | **$239.80** | +$16.98 (+7.08%) |

- **50 vs. 200 SMA:** $255.25 vs. $239.80 = a **+$15.46 (6.44%) golden-cross spread**, with both averages rising. The 200 SMA has climbed every session in the window, from $233.47 (07-13) to $239.80. The 50 SMA bottomed at $246.38 on 07-30 and has risen to $255.25 — a **positive-slope medium-term trend**.
- **But the short-term average is the problem:** the 10 EMA is essentially *at* price ($256.59), meaning no short-term trend edge exists. It has been declining from $267.18 (08-12) all the way through, and 2026-09-11 produced its **first uptick since 08-12** ($256.5535 → $256.5947). That is an early stabilization tell, not a trend reversal.
- The **10 EMA ($256.59) is below the 50 SMA ($255.25)?** No — it is $1.34 above it, but the gap has collapsed from over $19 in mid-August. Short-term momentum has flattened to the medium-term average: a classic coiling condition.

### 3.2 Momentum regime — `macd`, `macds`
| Date | MACD | Signal | Histogram |
|---|---|---|---|
| 08-11 (peak) | +8.432 | +5.261 | +3.171 |
| 08-17 | +5.830 | +6.140 | −0.310 |
| 09-04 | +0.339 | +1.519 | −1.180 |
| 09-08 | +0.118 | +1.239 | −1.120 |
| 09-09 | **−0.421** | +0.907 | −1.327 |
| 09-10 | −0.879 | +0.550 | −1.429 |
| **09-11** | **−0.838** | **+0.272** | **−1.110** |

Two distinct bearish events have already occurred:
1. **Bearish crossover on 2026-08-17** — MACD ($5.830) fell below the signal ($6.140) and has stayed below it for 19 consecutive sessions.
2. **Zero-line break on 2026-09-09** — MACD crossed from +0.118 to −0.421, meaning short-term momentum is now below its own trend baseline, not merely decelerating.

The one offset: on 09-11 the MACD line **rose for the first time since 08-11** (−0.879 → −0.838), and the histogram narrowed from −1.429 to −1.110. That is deceleration of the selloff, consistent with the price reversal, but the MACD is still negative and below signal — **the momentum regime remains bearish**.

### 3.3 Mean reversion — `rsi`
- **RSI = 48.91**, up from 43.62 on 09-10 and 44.06 on 09-09. Dead-center neutral.
- The only overbought reading was **72.23 on 2026-08-03**, which correctly marked the post-gap peak; RSI has since bled to the high-40s without ever reaching oversold (<30).
- The 09-09/09-10 double dip at 44.06 / 43.62 followed by a 5.3-point jump is a **mild positive divergence in the making** (price made a lower low at $249.58 vs. $251.93 on 09-01, while RSI's low, 43.62, was barely below the 09-01 reading of 46.33). Not yet a valid divergence signal — RSI is not oversold — but it supports the "selling pressure is fading" case.
- Key tell: **RSI reclaiming 50** would align with price clearing the $257.9–$259 cluster.

### 3.4 Volume-weighted conviction — `vwma`
- **VWMA = $257.95**, and the close ($256.78) is **$1.17 (−0.46%) below it**. The volume-weighted holder base over the window is slightly underwater — a mild headwind, not a rout.
- VWMA has fallen from **$272.05 (08-20)** to $257.95, reflecting the lower volume-weighted transacting level. Critically, the *rate* of decline is flattening: −1.55 (09-08), −0.84 (09-09), −0.57 (09-10), −0.21 (09-11). That is **seller exhaustion in the volume-weighted series**.
- **Volume quality of the bounce is the weak link.** 09-11 volume of 26.72M is ~84% of the ~31.9M 22-session simple average. By contrast, the 09-01 down day (31.70M) and 09-09 down day (33.06M) both traded *above* that average, while 09-03 and 09-04 up days (26.89M, 30.75M) were average or lighter. Distribution days are outnumbering accumulation days — this is why the low-volume reversal needs follow-through.

### 3.5 Risk and volatility — `atr`
- **ATR = $6.22**, or **2.42% of price**.
- ATR has collapsed from **$9.95 (08-03)** and $7.24 (09-01) to $6.22 — a **~37% volatility contraction from the post-gap peak**. This is consistent with a maturing consolidation, and it means:
  - A 1-ATR daily move is ~$6.20; a 2-ATR move is ~$12.45.
  - Stop distances should be at least 1.0–1.5 ATR to avoid noise-level stops.
  - Contracting ATR inside a range often precedes an expansion move — the breakout/breakdown trigger matters more than the day-to-day chop.

### 3.6 Corroborating context — Bollinger bands (verified snapshot)
- Middle: **$258.96** (falling from $267.14 on 08-27), Upper: **$266.66**, Lower: **$251.26**.
- Bandwidth ≈ **5.95% of the mid-band** — narrow, consistent with the ATR contraction.
- Price ($256.78) sits in the **lower half** of the band, below the mid-band. The 09-10 low ($249.58) pierced below the current lower band ($251.26) and was reclaimed the next day — a short-term "stretch and snap-back," but one that needs a close above the mid-band to become a genuine band-based reversal.

---

## 4. The evidence balance sheet

| Bullish evidence | Bearish evidence |
|---|---|
| Price above rising 50 SMA (+0.60%) and rising 200 SMA (+7.08%); golden-cross spread 6.44% | Price below 20-day mid-band ($258.96) and VWMA ($257.95) |
| 50 SMA slope positive (+$2.84 since 09-01) | MACD below zero since 09-09 and below signal since 08-17 |
| 09-11 reversal closed at 81.8% of day's range, +1.94% | Unbroken sequence of lower lows since 08-05 |
| 09-10 low $249.58 ≈ 61.8% retrace ($249.48) of post-gap impulse | Volume on the bounce (26.7M) below the ~31.9M recent average; up-days lighter than down-days |
| 10 EMA and MACD line both ticked up on 09-11 for the first time since 08-11/08-12 | Overhead resistance cluster $257.9–$259.5 (VWMA, mid-band, gap-fill, 09-03 high) |
| RSI recovering from 43.6 to 48.9; potential nascent higher low in RSI | RSI not oversold and no confirmed divergence |
| ATR contraction (−37% from peak) suggests a resolving range | Short-term trend (10 EMA flat/declining) has no edge |

**Net:** the primary trend is up, the intermediate trend is corrective, and the short-term tape is at an inflection point with a slight upward tilt after 09-11 — but without conviction.

---

## 5. Actionable plan

### 5.1 Key levels
| Level | Price | Source |
|---|---|---|
| Resistance 4 | $266.66 | Bollinger upper band |
| Resistance 3 | $261.12 | 2026-09-04 high |
| **Resistance cluster** | **$257.95–$259.50** | VWMA $257.95, Bollinger mid $258.96, 2026-09-03 high $259.50, filled 09-01 gap |
| **Pivot / last close** | **$256.78** | 2026-09-11 close |
| Support 1 | $255.25 | 50-day SMA |
| Support 2 | $253.14 | 2026-09-11 low |
| Support 3 | $251.26 | Bollinger lower band |
| **Critical support** | **$249.48–$249.58** | 2026-09-10 low / 61.8% retracement |
| **Structural floor** | **$239.80–$239.82** | 200-day SMA $239.80 + unfilled gap top (2026-07-30 high) $239.82 |

The **$239.80–$239.82 confluence is the most important level on the chart**: a rising 200-day SMA and the lower edge of the unfilled earnings gap sit within two cents of each other.

### 5.2 Scenario A — Bullish confirmation (preferred)
- **Trigger:** daily close **above $258.96–$259.50** on volume **≥ ~32M** (at least the recent average), ideally with MACD back above its signal line.
- **Staged adds:** $261.12 (09-04 high), then $266.66 (upper band) / $267.56 (08-28 high).
- **Stop:** below $253.14 (09-11 low) for a tight trade, or below $251.26 (lower band) for a swing position.
- **R:R at trigger (~$259.10 entry, $251.26 stop):** risk ~$7.84; reward to $266.66 ~$7.56 → **~0.96:1** — poor. Chasing the breakout at the band is not attractive. Reward improves materially only if the $267.56 high gives way toward the $284/$287.20 post-gap peak zone.

### 5.3 Scenario B — Pullback buy (better asymmetry)
- **Setup:** a retest of **$252–$254** (09-11 low to lower band) that holds and closes back above $255.25.
- **Entry:** ~$253.50. **Stop:** $247.45 (1.5 × ATR = $9.34 below entry, just under the $249.58 low). **Target:** $266.66.
- **R:R:** risk $6.05, reward $13.16 → **~2.2:1**. This is the higher-quality long because it leans on the 09-10 low and the 61.8% retracement rather than on a low-volume momentum chase.

### 5.4 Scenario C — Bearish continuation
- **Trigger:** daily close **below $251.26**, confirming the lower band and the 09-10 low as failed support.
- **Measured objectives:** $249.48 first, then the **$239.80–$239.82 structural confluence** (a further ~4.7% below the trigger).
- **Invalidation:** a close back above $258.96.

### 5.5 Position sizing example (ATR-based)
With ATR at $6.22, a standard 1.5-ATR stop is **~$9.33**. On a $100,000 account risking 1% ($1,000):
- Shares = $1,000 ÷ $9.33 ≈ **107 shares**
- Notional at $256.78 ≈ **$27,470** (~27% of equity)
- Volatility-adjusted: the position should be reduced if ATR expands back toward the $9–10 post-gap level, and can be increased if ATR compresses below ~$5.50 alongside a confirmed breakout.

---

## 6. What to watch over the next 3–10 sessions

1. **Does volume expand above ~32M on an up day?** This is the single most important missing piece. Without it, 09-11 is a low-conviction bounce.
2. **Can price close above $258.96 (mid-band) and hold it for 2 sessions?** That would flip the short-term trend from "below the 20-day benchmark" to "above."
3. **Does the MACD line cross back above its signal ($0.272)?** The line is at −$0.838; a cross would require roughly a $1.11 rally in the MACD line — achievable in 3–5 sessions if price holds above $258–260.
4. **Does RSI close above 50?** Currently 48.91, moving in tandem with the $258 level.
5. **Does the 10 EMA ($256.59) turn up decisively?** The 09-11 tick (+$0.04) is the first sign; a second consecutive rise would confirm.
6. **Watch $249.58.** Any close below it reopens the path to the 200 SMA/gap confluence at $239.80–$239.82.

---

## 7. Data verification note

All OHLCV and indicator values in this report come from `get_verified_market_snapshot` (2026-09-11), and the independently retrieved indicator series agree exactly with the snapshot: `close_10_ema` 256.594684, `close_50_sma` 255.252799, `close_200_sma` 239.7977, `macd` −0.837920, `macds` 0.272060, `rsi` 48.913551, `boll` 258.960499, `atr` 6.2235, `vwma` 257.952689. **No discrepancy found.** All Fibonacci levels, percentage changes, averages, and R:R figures above are arithmetic derived from the tool's own price rows and are labeled as such; no external data, news catalysts, or unobserved support/resistance tests have been assumed.

---

## 8. Key points summary

| Dimension | Reading | Evidence (2026-09-11) | Interpretation | Action |
|---|---|---|---|---|
| **Primary trend** | Up | Close $256.78 > 50 SMA $255.25 > 200 SMA $239.80; 50/200 spread +6.44%, both rising | Bullish structure intact | Do not short the primary trend |
| **Intermediate trend** | Corrective | −9.59% from $284.02 close (08-03); six lower lows since 08-05 | Correction, not yet a reversal | Wait for a higher low |
| **Short-term trend** | Flat/coiling | 10 EMA $256.59 ≈ price; first uptick since 08-12 | Inflection point | Needs 2–3 sessions to confirm |
| **Momentum** | Bearish, decelerating | MACD −0.838 vs signal +0.272; hist −1.110 (from −1.429) | Sell signal intact, pressure easing | No momentum buy signal yet |
| **Mean reversion** | Neutral | RSI 48.91 (from 43.62) | Room in both directions | RSI > 50 = bullish tell |
| **Volume** | Weak confirmation | 26.72M vs ~31.9M 22-day average; down days heavier than up days | Bounce lacks conviction | Require ≥32M on breakout |
| **Volume-weighted price** | Mild headwind | Close $256.78 < VWMA $257.95 | Average buyer slightly underwater | Reclaim $257.95 first |
| **Volatility** | Contracting | ATR $6.22 = 2.42%; down 37% from $9.95 (08-03); band width 5.95% | Range resolving imminent | Size positions off 1.5×ATR ≈ $9.33 |
| **Resistance** | Dense | $257.95–$259.50 cluster (VWMA, mid-band, gap fill, 09-03 high) | Breakout gate | Long only on close > $258.96 with volume |
| **Critical support** | $249.48–$249.58 | 09-10 low + 61.8% retracement | Correction's line in the sand | Long stop below $247.45 |
| **Structural floor** | $239.80–$239.82 | 200 SMA + unfilled gap top | Major confluence | Bearish target if $251.26 fails |
| **Best risk/reward** | Pullback long | Entry ~$253.50, stop $247.45, target $266.66 ≈ 2.2:1 | Superior to chasing $259 | Wait for retest |
| **Overall stance** | **Neutral / Hold** | Uptrend + bearish short-term momentum + low-volume bounce | Confirmation-dependent | Buy >$259 on volume or $252–254 with a hold; avoid the middle |