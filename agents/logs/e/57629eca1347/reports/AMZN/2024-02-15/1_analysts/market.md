# AMZN — Multi-Indicator Technical Report
**As of the close of 2024-02-15 (verified snapshot) | Price basis: $169.80**

---

## 1. Latest Verified Bar & Data Source Check

| Field | Value (2024-02-15) |
|---|---|
| Open | 170.58 |
| High | 171.17 |
| Low | 167.59 |
| Close | 169.80 |
| Volume | 49,855,200 |

**Consistency check:** the values returned by the individual indicator calls (`close_10_ema` 168.867, `close_50_sma` 155.953, `close_200_sma` 136.903, `macd` 4.924, `macds` 4.721, `rsi` 61.128, `boll_ub` 178.311, `atr` 3.848) are **identical** to the verified snapshot, and the snapshot's OHLCV matches the raw CSV. **No discrepancies found.** The snapshot additionally supplies `macdh` = 0.2028, `boll` (20-SMA) = 164.123, `boll_lb` = 149.936, `vwma` = 167.136, `mfi` = 0.496 — these are treated as source-of-truth below.

---

## 2. Trend Structure — Bullish on All Three Horizons, but Short-Term Slope Is Decelerating

**Long-term (200 SMA = 136.90):** Price is **+24.0%** above the 200 SMA. The 200 SMA has risen every single session in the sample, from 125.35 on 2023-12-18 to 136.90 on 2024-02-15 — a gain of 11.55 points in 40 sessions (~+0.29/day). There is no ambiguity in the primary trend.

**Medium-term (50 SMA = 155.95):** Price is **+8.9%** above the 50 SMA. The 50 SMA rose from 139.42 (2023-12-18) to 155.95 (2024-02-15), ~+0.41/day. Critically, the **50 SMA sits 19.05 points (13.9%) above the 200 SMA** and both are rising — a mature, positively-sloped moving-average stack (a "golden cross" condition that was established long before this window and remains intact).

**Short-term (10 EMA = 168.87):** Close 169.80 is only **+0.55%** above the 10 EMA. This is the tightest price-to-fast-MA relationship of the three, and it is the tell. Cadence of the 10 EMA:

| Date | 10 EMA | Daily change |
|---|---|---|
| 2024-02-02 | 159.87 | +2.65 |
| 2024-02-05 | 161.77 | +1.90 |
| 2024-02-07 | 164.46 | +1.35 |
| 2024-02-09 | 167.08 | +1.64 |
| 2024-02-12 | 168.03 | +0.96 |
| 2024-02-14 | 168.66 | +0.52 |
| 2024-02-15 | 168.87 | **+0.21** |

The short-term average is still rising but the *rate of rise has collapsed by ~87%* since the 2024-02-02 earnings gap. That is the signature of a trend transitioning from impulse to digestion — not from up to down, but from fast to slow.

**Stacking order:** Close (169.80) > 10 EMA (168.87) > 20-SMA/Bollinger mid (164.12) > 50 SMA (155.95) > 200 SMA (136.90). A perfectly ordered bullish stack with the shortest average *not yet* broken.

---

## 3. The Defining Event: An Unfilled Earnings Gap and Its Consolidation Box

The single most important structural fact in this dataset is the **2024-02-02 bar**: open 169.19 versus the 2024-02-01 high of 159.76 and close of 159.28. That is an opening gap of **$9.43 (+5.9% vs. the prior high, +6.2% vs. the prior close)**, on **117.2M shares** — 2.3× the trailing 20-session average volume of roughly 51.3M. The 2/2 session closed at 171.81 after printing 172.50.

Ten sessions later:

- The **gap remains entirely unfilled**. The lowest print since is 165.75 (2024-02-13), still $5.99 above the 2024-02-01 high of 159.76. Gap-and-hold behavior of this duration is a structural bullish signal.
- Price has built a **consolidation box**: 2/2 high 172.50 / 2/12 high 175.39 on the top; 2/13 low 165.75 on the bottom. Close on 2/15 (169.80) is essentially mid-box.
- Inside that box, the **2024-02-13 session is the notable bar**: open 167.73, low 165.75, close 168.64 — an intraday undercut that was fully reclaimed by the close, and the 10 EMA held (168.14 that day vs. 168.64 close). Rejection of the breakdown attempt.
- The 20-session range (from 2024-01-17) spans **149.91 to 175.39**.

**Larger context:** the recovery from the 2023-10-26 close of 119.57 to the 2024-02-09 close of 174.45 is **+45.9%**, and from the 2023-12-29 close of 151.94 to 169.80 is **+11.7%**. The stock arrives at mid-February extended on an intermediate basis while basing on a short-term basis.

---

## 4. Momentum — MACD Is Peaking; This Is the Main Caution Flag

**MACD line = 4.924, Signal = 4.721, Histogram = 0.203.**

- The bullish crossover was confirmed on **2024-01-12** (MACD 1.643 crossed above signal 1.549) and the histogram has been positive continuously since.
- The histogram peaked at **1.118 on 2024-02-12** and has decayed for **four consecutive sessions**: 1.118 → 0.677 → 0.473 → **0.203**. The MACD line itself has rolled over from its 2/12 peak of 5.501 (5.229 → 5.144 → 4.924) while the signal line keeps grinding up (4.383 → 4.552 → 4.671 → 4.721).
- At the recent convergence pace (~0.27 histogram points per session), the histogram is **within roughly one to two sessions of a bearish crossover**. This is a mechanical projection from the last two days' deltas, not a forecast — but it means the bull-momentum signal is on the clock.

Interpretation: MACD remains in a **positive regime and is nowhere near the zero line** (4.92 is a strongly elevated reading), so the primary momentum backdrop is still bullish. What has changed is that the *second derivative* has flipped — the impulse is exhausting. Historically in this window, similar histogram decay phases (e.g., 2023-12-27 to 2024-01-05, when MACD fell from 3.06 to 0.86 and RSI fell from 63.9 to 42.1) coincided with 5–7% pullbacks before trend resumption, not with trend termination.

**RSI = 61.13**, and the trajectory is the interesting part:

| Date | RSI | Close |
|---|---|---|
| 2024-02-02 | 73.78 | 171.81 |
| 2024-02-09 | 72.43 | 174.45 |
| 2024-02-12 | 67.90 | 172.34 |
| 2024-02-13 | 60.72 | 168.64 |
| 2024-02-14 | 63.36 | 170.98 |
| 2024-02-15 | **61.13** | 169.80 |

Two readings matter:

1. **RSI never exceeded ~74** even on the 2/2 earnings spike and the 2/9 high. There is no embedded overbought extreme requiring mean reversion — the stock has digested gains through *time*, not through a violent RSI reset. This is normally a constructive characteristic.
2. **A modest negative divergence**: RSI made a lower high (72.43 on 2/9) against a price high, and the subsequent sequence is a staircase down (73.78 → 72.43 → 61.13) while price only gave back 1.2% from the 2/9 close. RSI is falling faster than price — internal momentum is leaking. The mid-line (50) sits far below at 61, so the RSI regime is still bullish, but it is no longer "trend-strength" territory.

---

## 5. Volatility — Wide Bands, Room to Run, and a Clean Stop Anchor

- **Bollinger:** mid 164.12, upper **178.31**, lower **149.94**. Bandwidth = (178.31 − 149.94) / 164.12 = **17.3%** — very wide, reflecting the earnings gap's vol expansion. Close is **+3.46% above the mid-band** and **−4.77% below the upper band**. The stock is in the upper half of the envelope but *not* hugging the upper band — no breakout-thrust condition, no squeeze.
- **ATR = 3.848**, i.e. **2.27% of price** — elevated versus the ~2.0% typical of this window pre-earnings (ATR was 2.94–3.06 through late January) but already contracting from the 3.94 peak on 2/13. Post-event volatility is normalizing, which typically precedes a directional resolution.
- **ATR-derived levels (arithmetic from the verified close):**
  - 1 ATR up = 173.65 (just under the 2/12 high of 175.39 and the 2/9 high of 175.00)
  - 1.5 ATR down = **164.03** — which lands within 9 cents of the Bollinger mid-band at 164.12. A genuine confluence level.
  - 2 ATR down = 162.10

---

## 6. Volume — Accumulation Bias, Neutral Money Flow

- **VWMA = 167.14** versus close 169.80. Price is **+1.6% above** the volume-weighted average price. Buyers who deployed volume-weighted capital over the measurement window are in profit; the volume-weighted cost basis is acting as support just below the 10 EMA (168.87) and above the Bollinger mid (164.12).
- **MFI = 0.496** (vendor 0–1 scale) ≈ **49.6** — dead neutral. No distribution signature, but equally no volume-confirmed accumulation thrust on the recent up-days.
- **Volume profile of the consolidation is unremarkable**: 42–57M on most post-gap sessions (5-session average ≈ 51.4M, 20-session average ≈ 51.3M), with only the 2/2 gap (117.2M) and 2/1 (76.5M) standing out. There is **no rising-volume advance** and **no high-volume distribution day** in the box. This is textbook coiling: neither side has committed.

---

## 7. Actionable Framework

**Bias: constructive/neutral-to-bullish. Primary trend up, short-term momentum cooling, structure intact but unresolved.** The correct posture is *not* to chase mid-box at 169.80; it is to trade the resolution of the 165.75–175.39 box with predefined invalidation.

### Level map (all values derived from verified tool output)

| Type | Level | Source |
|---|---|---|
| Resistance 4 | 178.31 | Bollinger upper band |
| Resistance 3 | 175.39 | 2/12 high (window high) |
| Resistance 2 | 175.00 | 2/9 high |
| Resistance 1 | 172.50 | 2/2 gap-day high |
| **Spot** | **169.80** | 2/15 close |
| Support 1 | 168.87 | 10 EMA |
| Support 2 | 167.59 | 2/15 low |
| Support 3 | 165.75 | 2/13 low (failed-breakdown low) |
| Support 4 | 164.12 / 164.03 | Bollinger mid / 1.5×ATR stop |
| Support 5 | ~159.28 | 2/1 close (gap origin); 159.76 = 2/1 high |
| Support 6 | 155.95 | 50 SMA |

### Scenario A — Bullish resolution (needs 172.50 close or better)
Trigger: a daily close above **172.50** (the 2/2 gap-day high), ideally on volume > ~57M (above the recent 56.99M max ex-gap). Confirmation: MACD histogram re-expands above ~0.5 and RSI reclaims 68+. Mechanical measured move of the 7.74-point box (167.65→175.39) projected off 175.39 gives **183.13** — treat as a target zone, not a prediction. Manage against Support 2.

### Scenario B — Box continuation (base case for the next several sessions)
Price chops between 165.75 and 172.50. This is what the MACD decay, neutral MFI, flat volume, and mid-box close all argue for. Do nothing in the middle; only respond at the edges. Buying the 167.59–168.87 zone (2/15 low + 10 EMA) with a stop under 165.75 is the mean-reversion trade inside the box; selling 172.50–175.00 is the fade. Note the 10 EMA is converging on price — expect it to be tested.

### Scenario C — Bullish failure (needs a close below 165.75)
A close below the 2/13 low breaks the box and puts **164.12 (Bollinger mid) / 164.03 (1.5 ATR) immediately in play** as the last short-term defense. Below that, the mechanical box projection is **159.91**, which coincides almost exactly with the **2/1 close of 159.28 and the 2/1 high of 159.76** — i.e., gap-fill territory. Execution rule: reduce/exit on a close below 165.75, do not wait for 164.

### Position sizing with ATR
Using a 2-ATR stop ($7.70 risk per share) and a 1% account risk: a $100,000 account risking $1,000 supports **~130 shares ≈ $22,070 notional (≈22% of the account)**. Tightening to a 1.5-ATR stop (164.03, which also aligns with the Bollinger mid) raises that to ~173 shares. Because ATR is 2.27% of price rather than the ~2.0% pre-earnings norm, size is ~12% smaller than it would have been in January for the same dollar risk.

---

## 8. Risks to This Read

1. **Momentum divergence is real, not cosmetic.** MACD histogram has fallen 82% in four sessions and RSI is stair-stepping lower while price holds. If the histogram flips negative with price under 168.87, the 10 EMA break becomes the first objective evidence of a short-term downtrend within a longer uptrend.
2. **Extension risk on the intermediate frame.** +24.0% above the 200 SMA and +45.9% off the October low. The 50 SMA (155.95) is 8.2% below spot — a full trend reset would be a deep drawdown even without breaking the primary trend.
3. **Gap-dependency.** The bullish structure is *defined* by the unfilled 2/2 gap. Gap fills are common; there is no rule that says this one holds. A close below 159.76 would invalidate the entire post-earnings constructive thesis.
4. **No catalyst visibility from these tools.** Only price/volume/derived indicators were used. The 2/2 gap is inferred purely from the print (169.19 open vs. 159.76 prior high, 117M shares). Any fundamental or news-driven re-rating is outside what these tools can verify, and event risk should be sourced separately.
5. **MFI at 49.6 offers no confirmation either way.** Do not treat the VWMA position (+1.6%) as strong accumulation evidence — the gap day dominates the volume weighting by construction.

---

## 9. Why These Eight Indicators

| Indicator | Role in this specific context |
|---|---|
| `close_200_sma` | Establishes the undisputed primary uptrend and quantifies extension (+24.0%) |
| `close_50_sma` | Confirms intermediate trend and the 50>200 stack; defines the 155.95 trend-stop |
| `close_10_ema` | The actionable line — only +0.55% away, and its slope decay is the earliest warning available |
| `macd` | Regime gauge: strongly positive (4.92) rules out a momentum breakdown, separating "cooling" from "breaking" |
| `macds` | Required to read `macd` as a signal; the crossover clock is the core timing input |
| `rsi` | Detects the 74-cap / lower-high divergence without the redundancy of a second oscillator (stochrsi deliberately excluded) |
| `boll_ub` (+ mid/lower via snapshot) | Frames the 17.3% bandwidth expansion and gives the 164.12 confluence with the ATR stop |
| `atr` | Converts everything into risk units: 3.85/share, 2.27% of price, sizing and stop placement |

Deliberately excluded: `macdh` (fully derivable from the two lines I already have; the snapshot supplies it for verification anyway), `vwma` and `mfi` (covered via the snapshot — enough to establish neutral volume flow without a third volume indicator), and duplicate oscillators of any kind.

---

## Summary Table

| Dimension | Reading (2024-02-15) | Signal | Key Level / Evidence |
|---|---|---|---|
| Close | 169.80 (O 170.58 / H 171.17 / L 167.59) | Neutral | Mid-box, −1.2% from 2/9 high of 174.45 |
| Primary trend | 200 SMA 136.90, rising ~+0.29/day | **Bullish** | Price +24.0% above |
| Intermediate trend | 50 SMA 155.95, rising ~+0.41/day | **Bullish** | Price +8.9%; 50>200 by 13.9% |
| Short-term trend | 10 EMA 168.87, slope cut from +2.65/day to +0.21/day | **Cooling** | Price only +0.55% above |
| MA stack | 169.80 > 168.87 > 164.12 > 155.95 > 136.90 | **Bullish, intact** | No cross broken |
| MACD | 4.924 vs signal 4.721, hist 0.203 | **Decelerating** | Hist 1.118 (2/12) → 0.203; bull cross from 1/12 at risk |
| RSI | 61.13 | **Neutral-bullish** | Lower highs 73.78 → 72.43 → 61.13; never >74 |
| Bollinger | Mid 164.12 / UB 178.31 / LB 149.94 | **No squeeze, no thrust** | Bandwidth 17.3%; close −4.8% under UB |
| ATR | 3.848 (2.27% of price) | **Normalizing** | 1.5 ATR = 164.03 ≈ Boll mid 164.12 |
| Volume / flow | Vol 49.9M; VWMA 167.14; MFI 0.496 | **Neutral coil** | No distribution day, no accumulation thrust |
| Structure | Unfilled 2/2 gap ($9.43); box 165.75–175.39 | **Bullish base** | 2/13 low 165.75 reclaimed |
| Setup | Range trade, wait for resolution | **Neutral-to-bullish** | Long trigger >172.50; exit <165.75 |
| Risk sizing | 2-ATR stop $7.70/share | **~22% notional** at 1% risk on $100k | 1.5-ATR stop = 164.03 |

**Bottom line for AMZN:** the trend is up on every timeframe and the post-earnings gap is holding, so the burden of proof remains on the bears. But the short-term engine is visibly spooling down — MACD histogram down 82% in four sessions, RSI printing lower highs, 10 EMA slope nearly flat, and price parked mid-box at 169.80 with neutral money flow. The disciplined play is to let 172.50 or 165.75 pick the direction, size off the 3.85 ATR, and treat 164.12/164.03 as the line that decides whether this is a pause or a top.