# AAPL — Multi-Horizon Technical Analysis
**As of 2026-09-14 (verified snapshot) | Last close: $333.08**

---

## 1. Verified State of the Tape

All exact figures below come from the `get_verified_market_snapshot` call for 2026-09-14, which is treated as the source of truth.

| Field | Value |
|---|---|
| Open / High / Low / Close | 334.79 / 335.50 / 331.34 / **333.08** |
| Volume | 39,269,100 |
| 10 EMA | 324.05 |
| 50 SMA | 318.46 |
| 200 SMA | 285.24 |
| MACD / Signal / Histogram | 3.934 / 2.309 / **+1.625** |
| RSI(14) | 63.32 |
| Bollinger Mid / Upper / Lower | 317.98 / **334.02** / 301.95 |
| ATR(14) | 7.77 (2.33% of price) |
| VWMA | 321.20 |

**Derived positioning (arithmetic from the above):** price sits **+2.79%** above the 10 EMA, **+4.59%** above the 50 SMA, **+16.77%** above the 200 SMA, and **+3.70%** above VWMA. The close is only **$0.94 (0.28%)** below the upper Bollinger band, with **%B ≈ 0.97**. Bandwidth is **10.09%** of the mid-band.

**Data-integrity note:** the snapshot reports `mfi` as `0.65697`, which appears to be a fractional scaling of a standard 0–100 money-flow reading (~65.7). I have not used MFI in the analysis because of that ambiguity. Otherwise the snapshot and the `get_stock_data` CSV agree row-for-row on the 2026-09-14 OHLCV.

---

## 2. The Trend Hierarchy Is Bullish — But Price Is at the Top of Its Own Structure

The important thing to establish first is that AAPL is **not** in a downtrend, and it is **not** mid-trend either. It is a long-term uptrend that suffered a violent medium-term distribution event and has now fully retraced it.

**Long-term (200 SMA): intact and rising.** The 200 SMA has climbed monotonically in the tool output, from 242.65 (2026-02-26) to 285.24 (2026-09-14) — roughly +0.30/day with no flattening. Price is 16.8% above it. This is a healthy structural uptrend, but the extension is wide enough that mean-reversion risk toward the 200 SMA is a *tail* scenario only, not a near-term one.

**Medium-term (50 SMA): recovering after a genuine inflection.** This is the most informative series in the whole set. The 50 SMA rose from 266.99 (2026-05-18) to a plateau of ~309.8 in early August, **flattened from 2026-08-03 through 2026-08-17** (309.52 → 309.08, a net decline), then turned back up decisively: 312.38 (8/31) → 315.80 (9/8) → **318.46 (9/14)**, accelerating to roughly +0.53/day. A flattening-then-reacceleration in the 50 SMA is exactly what a completed correction inside an uptrend looks like. The turn is recent (about three weeks old), so the slope has not yet fully re-established, but the direction is unambiguous.

**Short-term (10 EMA): strong, and stretched.** The 10 EMA bottomed at 308.76 on 2026-08-17 and has climbed without interruption to 324.05, a +4.95% move in 20 sessions. Price is 2.79% above it. Stacking is textbook bullish: **333.08 > 324.05 (10 EMA) > 318.46 (50 SMA) > 285.24 (200 SMA)**. There is no moving-average conflict anywhere in the stack.

**Higher lows remain intact across the entire window:** the June low of 273.75 (2026-06-25 intraday) was followed by the August low of 300.57 (2026-08-12 intraday) — a materially higher low. The 52-week range from the CSV is roughly **236.32 (2025-09-16 low)** to **344.57 (2026-07-29 high)**; at 333.08 the stock is **+40.9% off the low** and **3.34% below the high**.

---

## 3. The Single Most Important Chart Event: The 2026-07-31 Gap

On 2026-07-30 AAPL closed at 333.43. On 2026-07-31 it opened at **304.81** and closed at **308.91** on **132.5M shares** — a **−7.35%** session with a ~28.6-point opening gap. That is the defining event of the last six weeks and it explains almost every indicator reading on the board today.

The recovery sequence, all from tool data:
- 2026-07-31 low: 300.00; 2026-08-12 low/close: 300.57 / 302.25 (the actual trough)
- 2026-08-12 close to 2026-09-14 close: **302.25 → 333.08 = +10.20%**
- 2026-08-26: MACD crosses back above its signal line
- 2026-08-31: MACD crosses back above zero
- 2026-09-10: +3.6% session (315.34 → 326.57) on **70.0M shares**, the heaviest up-volume in the recovery
- 2026-09-14: 333.08 — **$0.35 below the 2026-07-30 pre-gap close of 333.43**

This is the crux: **the entire 7/31 gap has now been filled.** Price has climbed back into the zone where every buyer who was long before the gap is back at breakeven. That zone (roughly **333.43 → 336.22**) is where supply is most likely to appear, and it is precisely where the stock closed on 9/14. The next 1–2 weeks are a referendum on whether the gap-down was a one-off repricing or a mistake the market has now corrected. A decisive close above 336.22 negates the gap entirely; rejection here leaves a large, freshly-formed double-top-ish supply shelf overhead.

**Critical context on gap frequency:** over the trailing 12 months the CSV contains at least three single-session declines worse than −5%:
- 2026-02-12: 275.50 → 261.73 (**−5.00%**)
- 2026-06-25: 293.08 → 275.15 (**−6.12%**, 107M shares)
- 2026-07-31: 333.43 → 308.91 (**−7.35%**, 132.5M shares)

This is a name with a fat left tail. Any stop placed inside 1×ATR ($7.77) can be jumped cleanly, and position sizing must respect that.

---

## 4. Momentum: Genuinely Strong, With One Honest Caveat

**MACD is the cleanest bullish signal on the board.** The line turned up from −2.676 (2026-08-17) to 3.934 (2026-09-14), reclaimed its signal line around 2026-08-26, and reclaimed zero on 2026-08-31 (0.297). The histogram has expanded every session in the recent run: **1.034 (9/4) → 1.267 → 1.374 → 1.571 → 1.902 → 2.309 (9/14)**, with the line-to-signal gap now **+1.625**. That is accelerating, not decelerating, momentum — the highest MACD reading since 2026-07-30 (9.24), though still far below it. Momentum thrust of this shape usually argues for continuation rather than immediate reversal.

**RSI at 63.32 is strong-but-not-overbought**, and it is *not* at a level that historically caps this name: on 2026-07-16 and 2026-07-17 RSI printed 71.43 and 71.65. It has risen from 49.35 on 2026-09-09 to 63.32 in three sessions — a fast, impulsive move, but with headroom before the 70 line.

**The caveat worth stating plainly:** on 2026-07-17 AAPL closed at 333.74 with RSI at 71.65. On 2026-09-14 it closed at 333.08 — essentially the *same price* — with RSI at 63.32. Same price, **8.3 RSI points lower**. That is a technical momentum divergence, and it is a real warning that the current advance is carrying less thrust per point gained than the July advance did. I would not over-read it: the intervening −7.35% drawdown and full retracement mechanically reset the RSI denominator, and RSI is measured on closes while the July peak was set on a different volatility regime. The honest interpretation is **"the retest of the highs is happening with less momentum behind it than the original push — confirmation required, not assumed."**

---

## 5. Volatility and Bollinger Positioning: Riding the Band

The Bollinger system is doing something specific. From the 7/31 shock, the lower band was pushed down to 289.77 (8/20) while the upper band sat at 341.28 — an extremely wide, shock-driven envelope. Since then the bands have **re-expanded in the direction of the advance**: upper band 317.04 (8/27) → 328.33 (9/8) → 331.86 (9/11) → **334.02 (9/14)**, while the lower band has climbed from 293.39 (8/25) to **301.95 (9/14)**. A rising lower band alongside a rising upper band is a trend re-establishment, not a squeeze.

Price at 333.08 with %B ≈ 0.97 is **pinned to the upper band**. In strong trends this is a continuation signature, not a sell signal — but it does mean the *entry* is poor here and the *risk* of a one- to three-day mean-reversion wobble back toward the 10 EMA (324.05) or the band mid/50 SMA confluence (**317.98 / 318.46** — these two are effectively the same level, a useful cluster) is elevated.

**ATR at 7.77 (2.33% of price) has compressed meaningfully** from the post-gap peak of 9.87 (2026-07-31) and 9.83 (8/3), bottoming near 7.10 (8/27) before ticking up to 7.77. Volatility normalization after a shock is typically constructive for trend continuation — but the slight uptick in ATR over the last three sessions (7.51 → 7.63 → 7.90 → 8.05 → 7.77) alongside price at resistance suggests the range is beginning to widen again at the decision point.

---

## 6. Volume: The Advance Is Real, But 9/14 Was a Stalling Day

**VWMA at 321.20 is the volume-confirmation anchor.** It bottomed at 307.76 on 2026-08-19 and has risen to 321.20, meaning the volume-weighted average price of the recent period is now 3.70% *below* the market — holders are in aggregate profit and the advance has genuine volume behind it. Price above a rising VWMA is a constructive combination; VWMA at 321.20 also acts as a volume-weighted reference on any pullback.

**But the last three sessions show a decaying participation pattern:**
- 2026-09-10: 70.0M shares, +3.56% — heavy accumulation ✅
- 2026-09-11: 50.7M shares, +1.75% — good follow-through ✅
- 2026-09-14: 39.3M shares, +0.24% — light, and the session **opened at 334.79, printed 335.50, and closed at 333.08, below the open**, a narrow-range (4.16 points vs 7.77 ATR) indecision candle right at the upper band

Against a 20-session average volume of roughly **43.1M** (computed from the CSV), 9/14 traded at about **91% of average**. That is not distribution, but it is also not the volume you want to see on a breakout attempt through a gap-fill and a 52-week-high shelf. The burden of proof sits on the bulls to show a high-volume close above 336.22.

For reference, the largest volume prints in the window — 261.8M (2026-06-26), 163.7M (2025-09-19), 144.6M (2025-12-19), 132.5M (2026-07-31) — cluster on rebalance/expiry-style dates and shock days. I am not attributing causes; the point is that this stock's volume spikes are frequently event-driven rather than trend-driven, which reinforces the gap-risk argument in Section 3.

---

## 7. Actionable Levels and Scenarios

All levels below are actual prices printed in tool output, not estimates.

**Resistance ladder**
| Level | Source | Distance from 333.08 |
|---|---|---|
| 334.02 | Bollinger upper band (2026-09-14) | +0.28% |
| 335.50 | 2026-09-14 high | +0.73% |
| 336.22 | 2026-09-11 high (recovery high) | +0.94% |
| 340.08 | 2026-07-28 close (closing high) | +2.10% |
| 344.57 | 2026-07-29 high (52-week high) | +3.45% |

**Support ladder**
| Level | Source | Distance from 333.08 |
|---|---|---|
| 324.05 | 10 EMA | −2.71% |
| 321.20 | VWMA | −3.57% |
| 318.46 / 317.98 | 50 SMA / Bollinger mid (confluence) | −4.39% / −4.53% |
| 315.34 | 2026-09-09 close | −5.33% |
| 309.90 | 2026-09-09 low | −6.96% |
| 301.95 | Bollinger lower band | −9.34% |
| 300.57 / 302.25 | 2026-08-12 low / close (post-gap trough) | −9.75% / −9.25% |

**Scenario matrix**

| Scenario | Trigger | Path | Probability lean |
|---|---|---|---|
| **Breakout continuation** | Daily close **above 336.22** on volume > ~50M | 340.08 → 344.57; gap fully negated, MACD extends above 4 | Needs confirmation; momentum supports it |
| **Base case: consolidation at the gap fill** | Failure at 334–336, holds above 318–324 | Chops 324–336 for 1–3 weeks, lets 10 EMA/50 SMA catch up, resets RSI | **Highest-likelihood near-term outcome** given %B 0.97 and 9/14 volume fade |
| **Failed retest / bull trap** | Close back **below 324.05 (10 EMA)** | 321.20 VWMA → 318.46/317.98 confluence → 309.90 | Medium risk; RSI divergence and the supply shelf argue for this over a clean breakout |
| **Structural breakdown** | Close **below 315.34**, decisively below 309.90 | 301.95 lower band → 300.57 retest; 50 SMA rolls flat again | Lower probability; would require a fresh negative catalyst |

**What would change my view:** a high-volume close above 336.22 upgrades the trend to "new-leg up" and makes 344.57 the operative target. Conversely, a close below 324.05 before 336.22 is taken out converts this from "breakout watch" to "failed retest," and the RSI divergence plus the 9/14 light-volume stall would be retrospectively validated.

---

## 8. Risk Management and Execution Notes

- **Do not initiate full size at $333 with %B at 0.97.** The reward-to-risk against 336.22 resistance is roughly +0.9% versus −2.7% to the 10 EMA — unfavorable in the immediate term. Better structures: (a) wait for a close above 336.22 and buy the retest, or (b) accumulate on a pullback into the 318–324 confluence, where risk is defined and the level cluster is dense.
- **ATR-based sizing:** 2×ATR(7.77) = **$15.54**, or 4.66% of price. For a 1%-of-equity risk budget that implies roughly 21% of equity notional. But given three −5% to −7.4% single-day gaps in twelve months, **size off gap risk, not off ATR** — a realistic adverse-gap assumption is closer to one full daily range plus the gap, i.e. 8–10% of price. Halve the ATR-implied notional accordingly.
- **Stops:** a protective stop at 324.05 (below the 10 EMA) is ~2.7% away in normal conditions but is easily jumped by a gap; a structural stop at 315.34 is ~5.3% away and better survives noise, at the cost of size. Avoid tight intraday stops in this name.
- **Dividend note (from tool data):** ex-dividend dates appear at a quarterly cadence — 2025-11-10 ($0.26), 2026-02-09 ($0.26), 2026-05-11 ($0.27), 2026-08-10 ($0.27). The next quarterly print would be expected in early November on that pattern, which is a mechanical (not predictive) observation from the dividend column.

---

## 9. Why These Eight Indicators

| Indicator | Role in this specific setup | Why it is not redundant |
|---|---|---|
| **close_10_ema** | Defines the short-term trend and the first mean-reversion target (324.05) | Faster than the 50 SMA; captures the post-8/17 leg that the 50 SMA cannot resolve |
| **close_50_sma** | Identifies the mid-trend inflection — flat Aug 3–17, then re-accelerating | Separates "trend intact" from "trend broken"; lags too much for entries, perfect for regime |
| **close_200_sma** | Confirms the multi-year uptrend and the 16.8% extension | Only series that answers the strategic question; no overlap with 50 SMA's tactical role |
| **macd** | Crossover and zero-line reclaim (8/26 and 8/31) with a rising line | Trend/momentum confirmation via EMAs, distinct from RSI's ratio-based momentum |
| **rsi** | Identifies that 63.3 is strong but not extreme, and flags the 333.7/63.3 vs 333.7/71.7 divergence | Normalized oscillator; the only tool here that surfaces the divergence |
| **boll (mid / ub / lb)** | %B ≈ 0.97 at 334.02 upper band, mid 317.98 confluent with 50 SMA, lower 301.95 | Volatility-adjusted *price location*; MACD/RSI tell you momentum, not where price sits in its own distribution |
| **atr** | 7.77 = 2.33% of price; stop placement and position sizing | Pure risk measurement; no directional information, no redundancy with the oscillators |
| **vwma** | Confirms the advance has volume behind it (price 3.7% above rising VWMA) | Volume-weighted, so it disagrees with simple MAs when participation is thin — exactly the check needed after a low-volume 9/14 |

Deliberately excluded: `boll_ub`/`boll_lb` were analyzed as one Bollinger system to avoid double-counting; `macds`/`macdh` were read from the verified snapshot rather than selected, since MACD line plus histogram conveys the same cross/acceleration information; MFI was excluded due to the scaling ambiguity noted in Section 1.

---

## 10. Bottom Line

AAPL is in a **confirmed long-term uptrend with a repaired medium-term structure and an extended short-term position**. The post-7/31 gap has been filled to within $0.35 of the pre-gap close, MACD is accelerating, and price is above every major average with volume confirmation from VWMA. That is a bullish configuration, not a bearish one.

But the stock is doing the hardest thing a chart can do — **retesting a supply shelf formed by the highest-volume single-day decline in the dataset, at the upper Bollinger band, with lower RSI than the last time it traded at this price, on declining volume, and $0.94 below the band that capped the move.** The correct posture is **constructive but not aggressive**: treat 336.22 as the gate, treat 318–324 as the value zone, and let the market prove the breakout on volume rather than anticipating it.

---

## Key Points Summary

| Dimension | Reading (2026-09-14) | Interpretation | Actionable Level |
|---|---|---|---|
| Verified close | $333.08 (H 335.50 / L 331.34) | Narrow-range stall candle at upper band, closed below open | Watch 334.02 / 336.22 |
| Trend stack | 333.08 > 10 EMA 324.05 > 50 SMA 318.46 > 200 SMA 285.24 | Fully aligned bullish, no conflict | Long bias structurally intact |
| 200 SMA | 285.24, rising ~+0.30/day | Long-term uptrend healthy; +16.77% extension | Tail risk, not near-term risk |
| 50 SMA | 318.46, +0.53/day after flat Aug 3–17 | Medium-term inflection confirmed ~3 weeks ago | 318.46/317.98 = key confluence |
| 10 EMA | 324.05, +4.95% since 8/17 low | Strong short-term trend, price 2.79% stretched | First pullback target |
| MACD | 3.934 vs signal 2.309, hist +1.625 expanding 5 sessions | Bullish cross 8/26, zero reclaim 8/31, accelerating | Highest since 7/30 |
| RSI | 63.32 (up from 49.35 on 9/9) | Strong, not overbought; headroom to 70 | Divergence vs 7/17 (71.65 at 333.74) |
| Bollinger | %B 0.97, UB 334.02, MB 317.98, LB 301.95 | Pinned to upper band; bands re-expanding upward | Entry quality poor; break above UB unconfirmed |
| ATR | 7.77 = 2.33% of price (from 9.87 on 7/31) | Volatility normalizing, slight uptick last 3 sessions | 2×ATR stop ≈ $15.54 |
| VWMA | 321.20, rising from 307.76 (8/19) | Volume confirms advance; price +3.70% above | 321.20 as pullback reference |
| Volume | 39.27M on 9/14 vs ~43.1M 20-session avg | Rally participation fading at resistance | Want >50M on a 336.22 break |
| Unfilled business | Gap fill 333.43 → 336.22 complete in price | Supply shelf overhead; retest outcome undecided | Close >336.22 = open 340.08/344.57 |
| Recovery math | 302.25 (8/12) → 333.08 = +10.20% | V-shaped, higher low (300.57 vs 273.75 June) | Higher-low structure intact |
| Gap risk | −5.00% (2/12), −6.12% (6/25), −7.35% (7/31) | Three >5% single-day drops in 12 months | Size for gap risk, not 1×ATR |
| Stance | Constructive, not aggressive | Wait for 336.22 confirmation or 318–324 pullback | Invalidation: close <324.05 |