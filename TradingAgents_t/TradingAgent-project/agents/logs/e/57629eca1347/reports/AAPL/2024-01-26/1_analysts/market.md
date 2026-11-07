# AAPL — Multi-Timeframe Technical Report (as of 2024-01-26 close)

## 1. Verified data baseline

All exact figures below come from the verified snapshot for **2024-01-26** (the raw OHLCV pull and the indicator tool outputs agree with it to the decimal — no discrepancies to flag).

| Item | Value |
|---|---|
| Open / High / Low / Close | 194.27 / 194.76 / 191.94 / **192.42** |
| Volume | 44,594,000 |
| 10 EMA | 191.33 |
| 50 SMA | 190.84 |
| 200 SMA | 181.92 |
| Bollinger mid / upper / lower | 188.21 / 197.70 / 178.71 |
| RSI(14) | 55.62 |
| MACD line / signal / histogram | 0.951 / −0.011 / **+0.962** |
| ATR(14) | 3.15 (≈1.64% of price) |
| VWMA | 188.61 |
| MFI (snapshot scale) | 0.655 (≈65.5) |

Two recent price pivots anchor everything that follows, both directly from the data: the closing high of **198.11 on 2023-12-14** (intraday 199.62), and the January trough of **181.18 close on 2024-01-05** (intraday low 180.17).

## 2. Trend structure — bullish stack, but the 200-day is the story

- **Long-term:** 200 SMA at 181.92 and rising monotonically across every session in the visible window (168.46 on 2023-09-28 → 181.92 on 2024-01-26). That is a slow, persistent uptrend, not a flat-line average.
- **Medium-term:** 50 SMA at 190.84, above the 200 SMA by 8.92 points (**+4.90% spread**) — a mature golden-cross configuration rather than a fresh cross event. The 50 SMA itself turned up in January: 186.63 (2023-12-29) → 190.84 (2024-01-26).
- **Stacking:** Close (192.42) > 10 EMA (191.33) > 50 SMA (190.84) > 200 SMA (181.92). This is a textbook bullish ribbon alignment, and the 10 EMA/50 SMA crossover is *very* recent — price only reclaimed the 50 SMA on 2024-01-19 (close 191.56 vs 50 SMA 189.80).
- **Sequence:** −2.87% from the 2023-12-14 close (198.11) to 192.42; the drawdown bottomed at −8.54% (198.11 → 181.18 on 2024-01-05), and the rebound from the 2024-01-05 low to the 2024-01-23 high (195.75) was **+8.65%**. The stock has recovered roughly three-quarters of that drawdown and is now consolidating.

**Nuance:** the trend is bullish on the daily, but 192.42 is still 3.74% below the 2023-12-14 intraday high of 199.62. This is a *repair* rally inside a correction, not a confirmed breakout to new highs. Rallies into prior-high territory need volume confirmation, which is currently the weak link (Section 5).

## 3. Momentum — fresh MACD crossover, decelerating thrust

- **MACD crossed back above its signal line on 2024-01-19** (MACD −1.026 vs signal −1.228; the prior session, 01-18, was still below at −1.562 vs −1.279). The MACD line has since risen for five straight sessions: −1.026 → −0.408 → +0.184 → +0.591 → +0.877 → **+0.951**, and the signal has now caught up to −0.011, so the line is on the verge of crossing the zero line.
- **The histogram is the caution flag:** +0.656 (01-22) → +0.998 → +1.124 → +1.128 (01-25) → **+0.962 (01-26)**. The impulse peaked on 01-25 and rolled over slightly. Mechanically this is the signal line converging on a still-rising MACD line — but practically it means the *rate of improvement* in momentum has flattened at the exact moment price hit 196.4 and turned down.
- **RSI(14) at 55.62** — neutral-to-constructive, well off overbought. The path matters: RSI printed **28.79 on 2024-01-05** (oversold) and **36.71 on 2024-01-17**, i.e. a distinctly higher momentum low on a price test of the same 180-area support (intraday 180.17 on 01-05 vs 180.30 on 01-17). That non-confirmation of the second low is the highest-quality signal in this whole dataset and it has been validated by the subsequent +6.80% move into 01-26.
- RSI has since cooled from 62.62 (01-23) to 55.62 (01-26) without price breaking down. In a healthy uptrend that's normal digestion; if RSI rolls back under ~45 while price sits near 194–196, it would instead read as a failed momentum push.

## 4. Volatility — expanding regime, price mid-upper Bollinger

- **Bollinger:** mid 188.21, upper 197.70, lower 178.71 → bandwidth ≈10.1% of the mid-band. Price at 192.42 sits in the upper half but **2.7% below the upper band** and 2.2% above the mid-band. No band-walk, no squeeze-release signature yet — this is a "trend inside normal bands" configuration.
- **ATR 3.15** (1.64% of price). ATR bottomed at 2.57 on 2023-12-28, peaked at 3.37 on 2024-01-22, and has eased for three sessions (3.18, 3.18, 3.15). Volatility is elevated relative to the December calm but is now contracting alongside the consolidation — a mild positive for the base case, but it also means stops placed on December-era volatility are too tight.
- Practical translation: **1 ATR ≈ 3.15 points**. A structurally meaningful stop beneath the 50 SMA (190.84) needs roughly 1.5–2 ATR of room, i.e. ~186.1–187.7, which conveniently coincides with the Bollinger mid-band (188.21), the VWMA (188.61), and the unfilled 2024-01-18 gap.

## 5. Volume — the weakest part of the bull case

- VWMA at **188.61**, with price 192.42 → **+2.02% above the volume-weighted mean**. Recent buyers are, on average, in profit; the volume-weighted trend is up (185.25 on 01-18 → 188.61 on 01-26). That is genuine confirmation, not just price drift.
- However, participation is fading into the advance. Volume on the up-leg: **78.0M (01-18), 68.9M (01-19), 60.1M (01-22), 42.4M (01-23), 53.6M (01-24), 54.8M (01-25), 44.6M (01-26)**. The single biggest up-day volume of the move was the *first* day (the gap-up off the January low); the push from 195 to 196.4 on 01-23–01-24 happened on average ~48M, versus 82.5M on the 2024-01-02 down-day (close 185.64). Rally volume is running roughly half of capitulation volume.
- Interpretation: institutional accumulation is plausible near 180–188, but there is no evidence of aggressive demand at 194–196. Breakouts above 196.4 on sub-50M volume should be treated as suspect.

## 6. Key levels (all derived from tool output)

| Level | Value | Source |
|---|---|---|
| Resistance 3 | 199.62 | 2023-12-14 intraday high |
| Resistance 2 | 197.70 | Bollinger upper band |
| Resistance 1 | **196.27–196.38** | 2024-01-24/01-25 highs (leg cap) |
| Pivot / spot | **192.42** | 2024-01-26 close |
| Support 1 | **191.33** | 10 EMA (also 01-26 low 191.94 just above) |
| Support 2 | **190.84** | 50 SMA |
| Support 3 | **188.21–188.61** | Bollinger mid + VWMA |
| Support 4 | **182.93–185.83** | Unfilled 2024-01-18 gap zone |
| Support 5 | **180.17–180.30** | 2024-01-05 / 01-17 lows (must hold) |
| Support 6 | 178.71 | Bollinger lower band |

**Note on 2024-01-26's candle:** open 194.27, high 194.76, low 191.94, close 192.42 — a lower high *and* lower low versus 01-25 (196.27/193.11), closing in the bottom third of the range on lighter volume. Short-term that's distribution-ish; it has not yet violated any trend level (still above the 10 EMA and 50 SMA). One session is not a signal, but it does argue against chasing strength on Monday.

## 7. Scenarios and triggers

**Base case — constructive consolidation (roughly 55% weight).** Price holds 190.8–191.3, MACD line crosses the zero line, and a retest of 196.3 occurs. Confirmation requires a close **above 196.38 on volume ≥60M**. That opens 197.70 (Boll upper) and then 199.62. MACD zero-cross plus histogram re-expansion above +1.13 would be the corroborating momentum tell.

**Bear case — failed retest (roughly 30%).** A daily close **below 190.84** (50 SMA) invalidates the immediate bullish stack and targets the 188.2–188.6 confluence (Boll mid + VWMA). Because that cluster is the last line before the gap, a decisive break there projects toward 185.8 and then 182.9. The tell to monitor: RSI losing 45 while MACD histogram flips negative.

**Bull acceleration (roughly 15%).** A single high-volume session clearing 196.4 and holding it converts the old December breakdown area into support and makes 199.62/198.11 the immediate magnet; above that there is no tool-supported resistance in the visible window (data begins 2023-06-01, so I will not speculate beyond it).

**Invalidation of the whole bullish thesis:** a close below **180.30** would take out both January lows and break the rising 200 SMA relationship — at that point the higher-low structure is dead and the 178.71 lower band becomes the reference.

## 8. Actionable plan

- **Bias: constructive, tactically patient. HOLD core longs; add on pullbacks rather than strength into 194–196.**
- **Preferred entry zone:** 188.2–190.9 (50 SMA / Boll mid / VWMA confluence). Second tranche 186.0–187.5 if ATR expands on a gap-fill.
- **Do not chase** above 193 on declining volume — the 01-26 candle and the 44.6M print argue the risk/reward at spot is roughly balanced, with only ~2.0% to first resistance (196.38) versus ~1.6% to the first real support cluster (188.6 → using 192.42, that's −2.0%). Use limit orders.
- **Stops:** swing stop at **186.0** (≈2.0 ATR below spot, beneath the gap top and the VWMA). Tighter tactical stop below **190.30** (01-17 low area) if you want a defined-invalidation trade; accept the higher whipsaw frequency given 3.15 ATR.
- **Position sizing:** at 1.64% ATR, a 1R risk of 2% of equity implies a notional exposure of roughly 1.2× the ATR-based unit — i.e. size down versus a December-volatility basis, since ATR is ~22% higher than the 2023-12-28 reading of 2.57.
- **Targets:** T1 196.3 (leg high), T2 197.7 (Boll upper), T3 199.6 (December high). Trail the remainder with a 2×ATR chandelier once above 197.7.
- **Event risk flag (outside tool output):** AAPL's fiscal Q1 report historically lands in the first days of February, i.e. roughly a week after this analysis date. That is external calendar knowledge, **not** verified by these tools — but it materially argues against initiating full size at spot, and against holding through the print without a defined stop.

## 9. Why these eight indicators

`close_200_sma` + `close_50_sma` for strategic vs intermediate trend and the golden-cross structure; `close_10_ema` for the recent timing pivot (the 50 SMA reclaim on 01-19 and the instantaneous stack); `macd` + `macds` because the 01-19 crossover and the pending zero-line cross are the cleanest momentum-regime signals here, and the histogram (from the snapshot) shows the deceleration the lines alone hide; `rsi` for the oversold-to-neutral recovery *and* the higher-low divergence at the January double test; `atr` because volatility regime must drive stop placement and size in a 1.6% ATR tape; `vwma` because the whole bull case rests on whether the advance is volume-confirmed (so far: only partially); Bollinger bands came with the verified snapshot and are used here for the 188.21/197.70 envelope rather than as a separate selection.

## 10. Summary table

| Dimension | Reading (2024-01-26) | Signal | Key evidence |
|---|---|---|---|
| Long-term trend | 200 SMA 181.92, rising every session in window | **Bullish** | 168.46 (2023-09-28) → 181.92 |
| Intermediate trend | 50 SMA 190.84, above 200 SMA by +4.90% | **Bullish** | 50 SMA turned up from 186.63 (12-29) |
| Short-term structure | Close 192.42 > 10 EMA 191.33 > 50 SMA 190.84 | **Bullish, freshly formed** | 50 SMA reclaimed 2024-01-19 |
| MACD | 0.951 vs signal −0.011; hist +0.962 | **Bullish crossover, thrust flattening** | Crossover 2024-01-19; hist peak +1.128 on 01-25 |
| RSI | 55.62 | **Neutral / constructive** | Higher low 36.71 (01-17) vs 28.79 (01-05) on retested support |
| Bollinger | Mid 188.21 / UB 197.70 / LB 178.71 | **Upper-half, no band-walk** | Price 2.7% below upper band; bandwidth ≈10.1% |
| ATR | 3.15 (1.64% of price) | **Elevated, mildly contracting** | Up from 2.57 (12-28), peak 3.37 (01-22) |
| VWMA | 188.61 (price +2.02%) | **Mild bullish confirmation** | VWMA rising 185.25 (01-18) → 188.61 |
| Volume | 44.6M on 01-26; up-leg avg ~48–78M | **Caution — fading participation** | 78.0M on 01-18 vs 42.4M on 01-23 |
| Nearest resistance | 196.27–196.38 → 197.70 → 199.62 | Upside caps | 01-24/25 highs; Boll UB; Dec high |
| Nearest support | 191.33 → 190.84 → 188.21–188.61 → 182.93–185.83 | Downside cushions | 10 EMA; 50 SMA; Boll mid + VWMA; unfilled gap |
| Disproven level | 180.17–180.30 | **Must hold** | 01-05 and 01-17 lows |
| Overall stance | **HOLD / buy dips 188–191, don't chase 194+** | Constructive tilt | Stack intact but volume and MACD histogram lag |

*This is a technical analysis for informational purposes, not investment advice; all level and indicator claims are traceable to the verified snapshot for 2024-01-26 and the dated tool outputs above.*