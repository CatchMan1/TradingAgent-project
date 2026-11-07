# AMZN — Multi-Factor Technical Assessment (as of 2024-01-03 close)

## 1. Verified data check (source of truth)

I pulled 149 sessions of OHLCV (2023-06-01 → 2024-01-03) and cross-checked against the verified market snapshot for 2024-01-03. **No discrepancies found** — the two sources agree exactly on the latest row and on every indicator value used below.

| 2024-01-03 | Value |
|---|---|
| Open / High / Low / Close | 149.20 / 151.05 / 148.33 / **148.47** |
| Volume | 49,425,500 |
| Day range | 2.72 pts (1.83% of close) |
| Close location in day range | 5% from the low (weak close) |

One data caveat: the snapshot also returns `mfi = 0.5525`, which is not on a 0–100 scale. I have **excluded** it rather than interpret an ambiguous number.

---

## 2. Bottom line

AMZN remains in a **well-established primary uptrend** (price +15.8% above a rising 200-SMA, +3.1% above a rising 50-SMA), but it is in the **maturation/mean-reversion phase of a December breakout that has now been almost entirely retraced**. Three independent short-term bearish signals are firing simultaneously:

1. Price has lost the 10-EMA, the VWMA, and the Bollinger middle band.
2. MACD crossed below its signal line on 2023-12-29 and the histogram is expanding negative (−0.14 → −0.40 → −0.65).
3. RSI collapsed from 68.1 (12-18) to 48.9 in 11 sessions, and three straight sessions of rising volume accompanied the decline.

This is a **bullish-regime pullback, not a regime break** — the MACD line is still above zero (2.01), and price sits ~4 points above the confluence of the rising 50-SMA (143.94) and the lower Bollinger band (143.84). The trade is therefore about *where* the pullback stops, not *whether* the uptrend exists.

---

## 3. Trend structure across timeframes

**Long-term (strategic): intact and strong.**
- close_200_sma = 128.23, rising every session in the sample (118.50 on 2023-11-06 → 128.23 on 2024-01-03, ≈+0.127/day).
- close_50_sma = 143.94, also rising monotonically (132.51 → 143.94, ≈+0.43/day over the last 20 sessions).
- 50-SMA sits **12.25% above** the 200-SMA — a wide, positively-sloped golden-cross configuration. No death-cross risk anywhere on the horizon.

**Medium-term: also intact, but the cushion is thinning.**
- Price is +3.15% above the 50-SMA. That is a **normal but not generous** cushion; in mid-December price was +10% above it (154.07 vs 139.42 on 12-18).
- The 50-SMA is rising into price quickly. A purely sideways tape would resolve this compression within roughly 5–7 sessions as the average climbs into the 145s.

**Short-term: broken.**
- close_10_ema = 151.15, and price closed **1.78% below** it. The 10-EMA, which had been rising since early December, has now **flattened to declining**: 152.20 (12-28) → 152.15 → 151.75 → 151.15.
- Sequence of closes: 153.38 (12-28) → 151.94 (12-29) → 149.93 (01-02) → **148.47 (01-03)**. Three consecutive lower closes, two consecutive unfilled gap-downs (01-02 opened 151.54 vs prior close 151.94; 01-03 opened 149.20 vs prior close 149.93).

**The most important structural observation:** the December breakout has been **fully round-tripped**. Price closed at 146.13 on 2023-11-20, peaked at 154.07 on 2023-12-18 (+5.4%), and is now at 148.47 — only **+1.60%** versus that mid-November level. The current price is sitting precisely at the **top of the November consolidation range** (Nov highs: 147.26 on 11-14, 149.26 on 11-27). That makes 148–150 a genuine decision shelf, not an arbitrary number.

Drawdown metrics (all tool-derived):
- From the 2023-12-18 peak close (154.07): **−3.63%**
- From the 2023-12-20 intraday peak (155.63): **−4.60%**
- 3-session change (12-28 → 01-03): **−3.20%**
- Since 2023-12-29 (151.94): **−2.28%**
- 20-session change (2023-12-05 close 146.88): still **+1.08%**

---

## 4. Momentum: deterioration is orderly but accelerating

**MACD (macd = 2.006, macds = 2.660, derived histogram = −0.655):**
- The bearish crossover occurred on **2023-12-29** (histogram flipped from +0.031 on 12-28 to −0.141 on 12-29).
- The histogram is **expanding negative at an increasing rate**: −0.141 → −0.396 → −0.655. That is the signature of *momentum acceleration to the downside*, not yet exhaustion.
- Critically, **the MACD line is still positive**. At the current rate of decline (−0.36 to −0.42/day over the last three sessions), a mechanical zero-line cross would land around 5–6 sessions out (approx. 2024-01-10/11). This is a straight-line extrapolation, not a forecast, but it defines the window in which this must stabilize.
- The MACD actually *peaked at 3.136 on 2023-12-22* while price peaked on 12-18 — a lagging-momentum rollover typical of late-stage advances.

**RSI (48.92):**
- Path: 68.05 (12-18) → 67.28 → 62.67 → 65.31 → 64.12 → 64.09 → 63.86 → 63.94 → 59.01 (12-29) → 52.89 (01-02) → **48.92 (01-03)**.
- RSI has moved from the *edge* of overbought to dead-neutral in 11 sessions. It is **not oversold** — there is roughly 9 points of room to 40 and 19 points to 30.
- Mild bearish divergence: on 12-19/12-20 the stock printed higher intraday highs (155.12, 155.63) than 12-18's 154.85, while RSI made lower highs (67.28, 62.67) and *closes* failed to exceed 154.07. Momentum was already thinning at the highs.

**Interpretation:** nothing here is capitulation. This is a controlled de-risking. But the fact that RSI fell ~19 points while price fell only ~3.6% tells you the December rally was **over-owned and momentum-dependent**, which is exactly the condition in which pullbacks overshoot.

---

## 5. Volatility and Bollinger structure

| Band | 2024-01-03 | 2023-12-28 | 2023-12-18 |
|---|---|---|---|
| boll (20-SMA) | 150.15 | 149.53 | 147.09 |
| boll_ub | 156.46 | 156.49 | 151.37 |
| boll_lb | 143.84 | 142.58 | 142.81 |
| Bandwidth (ub−lb) | 12.62 (8.40% of mid) | 13.91 (9.13%) | 8.56 (5.82%) |
| %B | **0.367** | 0.655 | — |

- **Band expansion then topping.** Bandwidth went from 5.82% (12-18) to a peak of 9.13% (12-28/29) — a full volatility expansion — and is now contracting slightly (8.40%) as price rolls back inside. Contracting bandwidth *after* a directional impulse with price falling toward the mid-band is a textbook sign of trend maturation.
- **The upper-band ride failed.** On 2023-12-18 and 12-19, AMZN closed *above* the upper band (154.07 vs 151.37; 153.79 vs 152.67). By 12-20 it was back inside, and the upper band has since flattened (156.67 → 156.46). Failed band-rides at 2σ frequently precede a rotation toward the opposite band.
- **%B = 0.367** — price is in the lower third of the channel, dropping fast from 0.655 three sessions ago. The middle band at 150.15 is now overhead resistance rather than support.
- **ATR = 2.881 (1.94% of price)**, down from 3.446 on 12-18 and 3.383 on 12-07. Volatility contracted *while price made highs*, then the price broke down. ATR is a reactive measure, so expect it to tick back up if the decline continues — which is why ATR-based stops set today may be slightly too tight tomorrow.

**ATR-anchored levels:** 1×ATR below close = 145.59; 2×ATR below = 142.71.

---

## 6. Volume and participation

- Latest volume 49.43M vs a 20-session average of ≈46.99M (computed from the returned rows) → **≈+5% above average**.
- The last five sessions read **31.4M → 27.1M → 39.8M → 47.3M → 49.4M**: three consecutive sessions of rising volume on falling price. That is distribution-style behavior, though at modest magnitude — nothing climactic (no 1.5–2× average reversal print).
- Context on the December rally: 12-15 traded **110.1M** (likely an event-driven quarterly expiry / index-rebalance print) and 12-18 traded 62.5M on the 154.07 close. But from 12-21 through 12-28 volume collapsed to 25–36M while price stalled at the highs. **The advance exhausted on declining participation; the decline is now arriving on rising participation.** That is the single most bearish volume-information read in this dataset.
- **VWMA = 151.25** vs close 148.47. Price is **1.84% below** its volume-weighted average price — meaning the marginal buyer over the recent window is underwater. VWMA has been *above* price since 2024-01-02 and is now declining. This clusters with the 10-EMA (151.15) and the full-session high (151.05) to create a hard **150.1–151.3 resistance band**.

---

## 7. Key levels (all derived from tool output)

**Support ladder (down):**
| Level | Source |
|---|---|
| 148.33–148.39 | 01-03 low / 01-02 low (immediate base) |
| 145.59 | Close − 1×ATR |
| 144.52–145.30 | 12-06 close / 12-11 low 143.64 / VWMA-reversion zone |
| **143.84–143.94** | **Bollinger lower band + rising 50-SMA (the pivotal line)** |
| 143.13 | 2023-12-05 low |
| 142.81 | 2023-12-04 low (structural swing low) |
| 142.71 | Close − 2×ATR |

**Resistance ladder (up):**
| Level | Source |
|---|---|
| 149.93 | 2024-01-02 close |
| **150.15** | **Bollinger middle (20-SMA)** |
| 151.05–151.25 | 01-03 high / 10-EMA 151.15 / VWMA 151.25 |
| 152.38 | 2024-01-02 high |
| 153.34–154.07 | Late-December congestion & peak close |
| 155.12–155.63 | 12-19 / 12-20 highs |

The 143.8–144.0 zone is the highest-quality confluence in the entire setup: a **rising** 50-SMA and the lower Bollinger band coincide within 0.10 index points. It also sits just above the 142.81–143.13 double low from early December.

---

## 8. Scenarios and actionable triggers

**Scenario A — Bullish resolution (base case: 50–55%).**
The pullback is a normal reset within a strong uptrend. Price stabilizes in the 146–148 area, reclaims 150.15 (Bollinger mid) and then 151.25 (10-EMA/VWMA) on above-average volume (>50M). MACD histogram stops expanding and curls back toward zero; RSI holds above 45.
→ **Triggers long entries** on a daily close above 151.25, with 153.34 as the next objective and 155.63 the stretch target. Stop for that entry: below 148.33.

**Scenario B — Deeper but trend-preserving retest (30–35%).**
Price continues to bleed into the 143.8–144.5 confluence (50-SMA + lower band), where the 50-SMA catches up to price. ATR has fallen, so a "healthy" retest is only ~3% lower. The tell will be whether that test happens on **declining** volume with a long lower wick / RSI positive divergence.
→ This is the **highest reward-to-risk entry zone** in the current structure. Stop below 142.50 (under the 2×ATR line and the 12-04 low), which is ~4.0% from spot — a tight, well-defined invalidation for a trend-continuation trade.

**Scenario C — Trend damage / regime warning (15–20%).**
A daily close **below 143.80** that holds, especially on volume >1.3× average, would break both the 50-SMA and the lower Bollinger band simultaneously and put 142.81 in play. A break of 142.81 opens the November shelf at ~137–140 (Nov 1–3 closes 137.00/138.07/138.60) and would likely coincide with a MACD zero-line cross.
→ Cut or hedge. This scenario invalidates the "buy the dip" premise and shifts the framework to selling rallies into 148–150.

**What would change the bearish short-term read fastest:** a close back above 150.15 with volume above 50M, or a MACD histogram that stops making lower lows while price makes a marginally lower low (positive momentum divergence).

---

## 9. Trade construction notes

- **Volatility-scaled sizing:** ATR = 2.881 (1.94%). For a 1%-of-equity risk budget with an entry near 148.5 and a stop at 142.50 (risk 5.97 pts, ~4.02%), position size ≈ 0.01 × Equity ÷ 5.97 shares. With a stop at 145.50 (risk 2.97, ~2.0%), size roughly doubles — this is why the stop choice, not the entry, dominates the risk profile here.
- **Do not chase the current candle.** Close was at 5% of the day's range, the stock lost the 10-EMA and VWMA, and MACD histogram momentum is still expanding. There is no evidence of a low yet.
- **Asymmetry:** upside to the 153.34–155.63 zone is +3.3% to +4.8%; downside to the 143.9 confluence is −3.1%. Reward/risk is not compelling at 148.47 — it becomes compelling at 144–146, and it becomes compelling on a confirmed reclaim of 151.25.
- **Time factor:** because the 50-SMA is rising ~0.43/day, a *flat* tape resolves the overextension on its own. Patience has a positive expected value here.

---

## 10. Indicator selection rationale (8 slots)

| # | Indicator | Value (2024-01-03) | Why it belongs in this setup |
|---|---|---|---|
| 1 | close_200_sma | 128.23 | Establishes the primary regime. Price +15.8% above a rising 200-SMA proves this is a correction inside an uptrend, which is the single most important filter for how to trade the pullback. |
| 2 | close_50_sma | 143.94 | The tactical trend line and the convergence point with the lower Bollinger band. Its *slope* (+0.43/day) tells you how fast the pullback room is shrinking. |
| 3 | close_10_ema | 151.15 | Fastest read on the momentum break; now declining and acting as first resistance alongside VWMA. Confirms the short-term trend flipped. |
| 4 | macd (+signal) | 2.006 / 2.660 | Crossover on 12-29 gives a dated, objective momentum-shift signal; still above zero, which keeps it a "pullback" rather than a "reversal." |
| 5 | macdh | −0.655 | Measures *acceleration* of the bearish turn. Expansion (−0.14 → −0.40 → −0.65) is what tells you the decline isn't decelerating yet — a distinction the MACD line alone can't make. |
| 6 | rsi | 48.92 | Quantifies the reset from 68.1 to neutral and flags that there is no oversold cushion yet; also exposes the mild lower-high divergence at the December top. |
| 7 | boll_ub + boll_lb (+boll mid) | 156.46 / 143.84 / 150.15 | One volatility slot used as a set: %B (0.367), bandwidth expansion-to-contraction (5.8% → 9.1% → 8.4%), and the failed upper-band ride together map the mean-reversion target at 143.84. |
| 8 | atr | 2.881 | The only risk-sizing input: 1.94% daily range, contracting from 3.45, gives the 142.7/145.6 stop ladder and the position-size math. |

**Deliberately excluded:** `vwma` passed the corroboration test but overlaps with the 10-EMA at 151.25, so it was used as confirmation rather than a separate slot; `mfi` was dropped due to ambiguous scaling (0.5525). No stochrsi-type duplicate momentum oscillators were included, since RSI already covers that function.

---

## 11. Summary table

| Dimension | Read | Evidence (2024-01-03) | Implication |
|---|---|---|---|
| Primary trend | **Bullish** | Close 148.47 vs 200-SMA 128.23 (+15.8%); 50-SMA 143.94 above 200-SMA by 12.3%; both rising | Corrections are buyable, not shortable, until 143.80 breaks |
| Intermediate trend | **Bullish, thinning buffer** | +3.15% above 50-SMA (was +10.5% on 12-18) | Support is close enough to be tested |
| Short-term trend | **Bearish** | 3 lower closes; −3.63% from 154.07; below 10-EMA (151.15) and VWMA (151.25) | Momentum lower; no bottom signal yet |
| Momentum | **Deteriorating, accelerating** | MACD 2.006 < signal 2.660; hist −0.655 and widening since 12-29 | Downside impulse not exhausted |
| Oscillator | **Neutral** | RSI 48.92, down from 68.05 on 12-18 | Room to fall; mild bearish divergence at Dec top |
| Volatility | **Contracting after expansion** | ATR 2.881 (1.94%), from 3.446; bandwidth 8.40% from 9.13% peak | Stops: 142.7–145.6; expect range expansion on a 143.8 break |
| Band position | **Lower half** | %B 0.367; failed 2σ close-above on 12-18/12-19 | Mean-reversion target = 143.84 (lower band) |
| Volume | **Mildly negative** | 49.4M vs ~47.0M 20-day avg; 31.4→27.1→39.8→47.3→49.4 while price fell | Distribution-lite; rally had faded on 25–36M volume |
| Pivotal level | **143.84–143.94** | Lower Bollinger + rising 50-SMA confluence | The line that defines bull vs. broken |
| Immediate resistance | **150.15 / 151.05–151.25** | Boll mid / day high, 10-EMA, VWMA | Reclaim = short-term repair confirmed |
| Action bias | **Wait / buy-the-dip** | No capitulation, no reclaim | Preferred entries: 144–146 zone, or confirmed close >151.25 |
| Invalidation | **Close < 142.81** | 12-04 swing low; below 2×ATR (142.71) | Shift to neutral/defensive, target 137–140 shelf |