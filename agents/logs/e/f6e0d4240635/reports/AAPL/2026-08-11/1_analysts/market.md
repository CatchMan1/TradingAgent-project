# AAPL — Technical & Structural Analysis
**Analysis date: 2026-08-11 (close) | Instrument: AAPL (Apple Inc.)**
*All OHLCV and indicator values below are sourced from the verified market snapshot for 2026-08-11 and the indicator toolkits run against the same frozen data. Where I computed derived figures (percentages, spreads, slopes), the arithmetic is shown so it can be audited.*

---

## 1. Verified Price Snapshot — the anchor for everything that follows

| Item | Value (2026-08-11) |
|---|---|
| Open / High / Low / Close | 307.75 / 309.97 / 302.79 / **304.91** |
| Volume | 37,476,700 |
| Session change vs 08-10 close (308.26) | **−3.35 (−1.09%)** |
| Session range | 7.18 pts (**2.33%** of price) |
| Dividend adjustment | 0.27 ex-date on 2026-08-10 (prior payouts: 0.26 on 2026-02-09, 0.27 on 2026-05-11) |
| Total-return index | 310.33 (vs. price 304.91 — reflects reinvested dividends) |

**No data discrepancy was found.** Every indicator value returned by the individual indicator calls matched the verified snapshot exactly (e.g. `close_50_sma` 309.5574 vs. tool 309.5574; `macd` −0.8274; `macds` 2.4437; `macdh` −3.2711 = −0.8274 − 2.4437 ✓; `rsi` 41.919; `atr` 8.8147; `vwma` 318.1412; Bollinger mid 322.4815 = (347.0524 + 297.9106)/2 ✓). One caveat: the snapshot's `mfi` prints as **0.507**, which is a 0–1 normalised scale rather than the conventional 0–100 scale — I am therefore **not** using it as a signal input, only flagging the ambiguity.

---

## 2. Regime Classification: **long-term uptrend intact, medium-term trend stalled, short-term downtrend**

This is the single most important framing. AAPL is *not* in a broken bull market, and it is *not* still trending up on any timeframe shorter than a year. It is in a **post-breakdown consolidation inside a mature uptrend** — a distribution/repricing phase following a violent, high-volume gap on 2026-07-31.

The evidence for each layer:

**Long-term (bullish).** Close 304.91 sits **+25.04 pts (+8.95%) above the rising 200 SMA at 279.87**. That 200 SMA has climbed monotonically every single session in the visible window (277.96 on 07-31 → 279.87 on 08-11, ≈ **+0.27 pts/day**). The 50 SMA (309.56) remains comfortably above the 200 SMA (279.87) — a golden-cross configuration with a **+29.69 pt spread**. On a year-to-date basis AAPL is up **+12.51%** (271.01 on 2026-01-02 → 304.91) and **+23.60%** off the 2026-01-20 closing low of 246.70.

**Medium-term (stalled / rolling over).** This is where the damage is. The 50 SMA's slope has **collapsed by roughly 96%**:
- 2026-07-02 → 2026-07-30: 293.52 → 309.30 = **+15.78 pts over 20 sessions ≈ +0.79 pts/day**
- 2026-07-30 → 2026-08-11: 309.30 → 309.56 = **+0.26 pts over 8 sessions ≈ +0.03 pts/day**

A 50-day average that goes flat after a strong advance is the classic signature of **trend exhaustion, not trend continuation**. Critically, the 50 SMA has also flipped from support to a ceiling: price closed *below* it on 07-31 (308.91 vs 309.50), 08-03 (303.42 vs 309.52), 08-10 (308.26 vs 309.70) and 08-11 (304.91 vs 309.56), with only a brief 4-day reclaim (08-04 → 08-07) that failed.

**Short-term (bearish).** Price (304.91) is **−8.46 pts (−2.70%) below the 10 EMA at 313.37**, and the 10 EMA has declined for **eight consecutive sessions** (331.31 on 07-30 → 313.37 on 08-11, ≈ **−2.24 pts/day**). The 10 EMA is still *above* the 50 SMA (313.37 vs 309.56) — but the gap is only 3.81 pts and closing at ~2 pts/day. **A bearish 10/50 EMA cross is plausibly 1–3 sessions away if price stays under 310.** That is the next mechanical event on the calendar, and it is a flow-of-funds trigger for systematic trend followers.

---

## 3. The Anatomy of the 2026-07-31 Breakdown — the pivot of this whole analysis

This single session re-set the character of the chart, and it deserves precise description:

| Session | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|
| 2026-07-28 | 340.03 | 342.89 | 335.60 | **340.08** | 51.9M |
| 2026-07-29 | 339.73 | **344.57** | 337.35 | 338.19 | 56.1M |
| 2026-07-30 | 333.10 | 334.75 | 329.59 | 333.43 | 74.8M |
| **2026-07-31** | **304.81** | 310.69 | **300.00** | **308.91** | **132.5M** |
| 2026-08-03 | 309.58 | 311.80 | 302.56 | 303.42 | 75.1M |

- **Opening gap: −28.62 pts (−8.58%)** from the 07-30 close of 333.43 to the 07-31 open of 304.81.
- **Close-to-close: −24.52 pts (−7.35%)** — the largest single-session decline in the entire 152-session window available to me.
- **Volume: 132.5M**, roughly **2.4×** the ~55M average of the preceding week, and the heaviest print since 2026-06-26 (261.8M, which itself looks like a rebalance/index event given the 3.4× volume spike with only a modest price move).
- **An unfilled gap zone remains between 310.69 (07-31 high) and 329.59 (07-30 low)** — a ~19-point supply shelf that has not been tested in the 8 sessions since.

The magnitude of the gap, combined with the volume signature, is consistent with an **event-driven repricing** (guidance, news, or a material fundamental re-rate) rather than an ordinary technical failure. I am not asserting the specific cause — the data does not tell me — but the *shape* matters for how you trade it: post-event gaps of this type typically produce **weeks of range-bound chop** while the new information is digested, rather than immediate V-shaped recoveries.

Since the gap, price has traced a **lower-high sequence**: 313.33 (08-07) → 308.26 (08-10) → 304.91 (08-11). It has not printed a close above 313.33 in eight sessions.

---

## 4. Momentum: deterioration confirmed, but *not yet* oversold

**MACD (line −0.827, signal 2.444, histogram −3.271).** Three separate bearish facts:
1. **Bearish crossover occurred on 2026-07-31** (MACD 6.891 fell below signal 8.256) — the crossover led the price breakdown by zero days, confirming it in real time.
2. **MACD crossed below zero on 2026-08-11** (from +0.072 on 08-10 to −0.827) — this is the medium-term momentum regime flipping from positive to negative. Not trivial.
3. **The histogram has been negative for eight straight sessions** and re-widened on 08-11 (−3.189 → −3.271) after narrowing mid-week (−3.634 on 08-05 → −3.181 on 08-07). Interpretation: the *deceleration of the decline* that began around 08-05 has **stalled again**. Momentum is not repairing itself.

But note the nuance: the MACD line (a 12/26 EMA differential) has fallen from 9.61 (07-29) to −0.83 — a 10.4-point collapse in nine sessions. That is an extreme, near-vertical move in the oscillator. **Oscillators that fall this fast typically need a mean-reversion pause even inside a continuing downtrend.** This argues against chasing fresh shorts at the current level and argues for selling *rallies* into 310–314 instead.

**RSI (41.92).** RSI peaked at **71.65 on 2026-07-17** and **71.43 on 07-16** — genuinely overbought. Then came a textbook **bearish divergence**: price made a *higher* high-close on **07-28 (340.08 vs 333.74 on 07-17)**, while RSI made a *lower* high (**68.90 vs 71.65**). That divergence was the earliest warning of the 07-31 break.
- Current reading **41.92** is neutral-to-weak. It is **not** oversold (no 30 print, not even close).
- RSI bottomed at **40.34 on 08-03** and has effectively retested that zone (41.92) while price is marginally *higher* (304.91 vs 303.42). This is a **very mild positive divergence — too shallow to trade on its own**, but it does confirm that the 302–303 area is being defended.
- The practical read: RSI at 42 in a downtrend means **there is ~12 points of downside room before an oversold bounce signal fires**. There is no "washed-out" bid here.

---

## 5. Volatility: expanding on the downside, and that changes position sizing

**ATR = 8.81 pts** — equal to **2.89% of the closing price**. The ATR series tells a clean story:
- 2026-07-02 → 07-30: ranged 7.90 – 8.74, averaging ≈ **8.1** (a quiet, orderly uptrend).
- 2026-07-31: **jumped to 9.87** (+22.5% in one session) on the gap.
- 2026-08-11: **8.81** — still **~9% above the July baseline** and no longer contracting (8.94 → 8.81 is flat).

Elevated and sticky ATR means: (a) wider stops are required, which mechanically **reduces position size** for the same dollar risk; (b) intraday noise will generate false breakouts of the 300–310 range.

**Bollinger envelope (20-day):** mid **322.48**, upper **347.05**, lower **297.91**.
- Price at 304.91 sits **−17.57 pts (−5.45%) below the middle band** and only **+7.00 pts (+2.35%) above the lower band**. It is riding the lower half of the envelope — the classic position for a market in a short-term downtrend.
- **Envelope geometry is the tell:** band width has gone **63.95 pts (07-24) → 40.29 pts (07-31) → 49.14 pts (08-11)**. After the spike-induced squeeze, the bands are **re-expanding again** — and they are expanding *asymmetrically*: the **upper band has been capped at 344.5–347.1 since 07-30** while the **lower band has slid from 304.22 to 297.91**. Band width is now **15.2% of the mid-band**.
- The **mid-band (20 SMA) has rolled over** from 324.35 (07-31) to 322.48 — the first sustained decline in the 20-day average in this dataset. A falling 20-day mean with a flat upper band is a textbook "drift-down" configuration.
- Note also that on **2026-08-03 the close of 303.42 came within 1.16 pts of that day's lower band (302.26)** — a near-touch that produced a 3-day bounce to 313.33. The lower band is functioning as a genuine dynamic support reference. **If price closes a second time at/near the lower band while the band is still falling, that is a materially worse signal than the 08-03 touch.**

---

## 6. Volume & Participation: the most damning evidence is here

**VWMA = 318.14** — that is **+13.23 pts (+4.16%) ABOVE** the closing price. The interpretation is unambiguous: the volume-weighted average transaction price over the lookback is meaningfully higher than where the stock trades today, meaning **the marginal, volume-backed holder is underwater**. That is the definition of distribution.

The VWMA path shows exactly where that overhead supply was built:
- 2026-07-16: 300.72 → 2026-07-30: **329.58** (a 28.9-point rise in 10 sessions — the market paid up heavily into the 07-15/07-28 advance on 55–75M share days).
- 2026-07-31: 326.39 (the 132.5M-share day dragged it down 3.2 pts).
- 2026-08-11: **318.14** — still 9 points above spot, and *still declining*.

VWMA (318.14) is also **above the 50 SMA (309.56)** — a confirmation that recent activity clustered at *higher* prices than the simple average, i.e. **supply is overhead, not below**.

**The rally-vs-decline volume test:**
- **Bounce attempt, 08-04 → 08-07:** volumes of 68.0M, 49.4M, 46.1M, **34.4M** — **declining on every single consecutive up-session**, and the weakest day was the highest close (313.33). This is a failing rally: **no demand**.
- **Decline, 08-10 → 08-11:** 44.8M, 37.5M. Notably **37.5M on 08-11 is the second-lightest print of the entire visible window** (only 41.3M on 07-22 and 34.4M on 08-07 are comparable).
- **Synthesis — this is the key nuance most readers will miss:** the breakdown was on **massive** volume (132.5M), but the follow-through selling is on **contracting** volume. That combination — heavy distribution *into* a gap, then light, drifting, low-conviction selling — describes a market that has **already absorbed the shock and is now range-trading**, not one that is actively collapsing. It favours a **300–315 range / sell-rallies posture** over an aggressive trend-following short at current prices.

---

## 7. Level Map (all levels traceable to tool output)

**Resistance (overhead) — the ladder is dense, which is bearish for upside progress:**
| Level | Source | % above 304.91 |
|---|---|---|
| 309.56 | 50 SMA | +1.53% |
| 309.97 | 08-11 session high | +1.66% |
| 313.33–313.37 | 08-07 close / 10 EMA | +2.76% / +2.78% |
| 316.29 | 08-06 high | +3.73% |
| 318.14 | VWMA | +4.34% |
| 322.48 | Bollinger mid (20 SMA) | +5.76% |
| 329.59 → 333.43 | 07-30 low → 07-30 close (**gap zone**) | +8.09% → +9.37% |
| 344.57 | 07-29 high (window high) | +13.0% |

**Support (underfoot):**
| Level | Source | % below 304.91 |
|---|---|---|
| 302.79 | 08-11 session low | −0.70% |
| 302.56 | 08-03 low | −0.77% |
| 300.00 | 07-31 low (**key pivot**) | −1.61% |
| 297.91 | Bollinger lower band | −2.30% |
| 290.55 / 287.38–287.78 | 06-09 close / 06-09–06-10 lows | −4.71% / −5.6% |
| 279.87 | 200 SMA | −8.21% |

The **300.00–302.79 zone** is the line in the sand: it has been tested by the 07-31 low, the 08-03 low, and the 08-11 low, and has held each time. Three tests of a level within eight sessions, each on declining volume, is a **coiling pattern** — it resolves.

---

## 8. Scenarios, Triggers, and Probabilities

**A. Range-bound chop, 300–315 (≈45% — base case).** Price has already failed at 313.33 and held 300.00. Declining volume on both sides, MACD histogram still negative but no longer accelerating, RSI at 42 with no oversold print, ATR flat at 8.81, and the 50 SMA flat at 309.56 all point to digestion. *Actionable:* fade the extremes, do nothing in the middle.

**B. Breakdown / continuation lower (≈35%).** Trigger: **a daily close below 300.00 on volume >70M** (i.e. meaningfully above the 37–45M of the last two sessions — a low-volume break of 300 should be treated as a fake-out). A confirmed break opens the air pocket toward the **297.91 lower band**, then the **290.55 / 287.4** shelf, with the **279.87 200 SMA** as the major structural magnet. Note the mechanical accelerant: a **10 EMA / 50 SMA bearish cross** would likely fire in the same window.

**C. Reclaim / gap-fill attempt (≈20%).** Trigger: **a daily close above 313.37 (10 EMA) on volume >65M**, which would also turn the MACD histogram positive. That opens 316.29 → 318.14 (VWMA) → 322.48 (mid-band). A full gap fill toward 329.59–333.43 requires a genuinely new catalyst; I would not pre-position for it.

---

## 9. Actionable Trade Plans

**For existing longs (core position):** The long-term structure (price +8.95% above a rising 200 SMA, 50 > 200) does **not** justify abandoning a strategic holding. But the tactical picture warrants **trimming into strength, not adding into weakness**. If not already trimmed, use any rally into **310–314** to reduce. Hard structural stop: a weekly close below **297.91** (Bollinger lower band) would invalidate the range thesis.

**For tactical/swing traders — the higher-expectancy trade is short-the-rally, not short-the-breakdown:**
- **Entry zone: 311.50 – 314.00** (50 SMA, 10 EMA, and the 08-07 failed high all converge here).
- **Stop: 317.50** (above the 08-06 high of 316.29 and ~1 ATR above entry). Risk ≈ 4.5–6.0 pts.
- **Targets: 302.60 (T1), 298.00 (T2), 290.50 (T3).** Reward to T2 ≈ 13.5 pts.
- **R/R ≈ 2.3:1 to T2.** Favorable.
- **Invalidation:** a daily close above 318.14 (VWMA) with expanding volume — that would signal the overhead supply has been absorbed.

**For tactical longs (counter-trend, lower probability):**
- **Entry: 300.50 – 303.00** (the triple-tested support shelf), only on a *stabilising* session (close in the upper half of the day's range).
- **Stop: 295.25** (below the 07-31/08-03 lows and below the 297.91 lower band; ≈1.1 ATR of risk from 304.91).
- **Target: 309.56 (50 SMA), then 313.30.** R/R ≈ 1.0–1.5:1 — **inferior to the short setup.** Only appropriate for disciplined range traders.
- **Do not** initiate a fresh momentum long until MACD reclaims its signal line *and* price closes above 313.37.

**Position sizing with ATR 8.81 (2.89% of price):** For a 1% account risk with a 6.0-pt stop, size = (0.01 × Equity) / 6.0. For a 1% risk with a 9.5-pt stop (long setup), size = (0.01 × Equity) / 9.5. **The ATR expansion from ~8.1 (July) to 8.81 (now) implies roughly a 9% reduction in share count versus July for identical dollar risk** — this is a non-discretionary adjustment.

---

## 10. What Would Change My Mind

| Development | Signal |
|---|---|
| Daily close **> 313.37** on **>65M** volume | Short-term downtrend broken; stand down on shorts |
| Daily close **> 318.14** (VWMA) | Overhead supply absorbed; re-rate to neutral-bullish |
| Daily close **< 300.00** on **>70M** volume | Continuation confirmed; add to shorts, target 290/279.87 |
| **10 EMA crosses below 50 SMA** | Mechanical trend-follower selling; expect acceleration |
| MACD histogram turns positive while price > 305 | Momentum repair; range resolution upward |
| RSI < 30 with a reversal candle | Genuine oversold entry — not present today |
| Fresh 20-day high in VWMA | Distribution is over — currently not happening |

---

## 11. Bottom Line

AAPL is a **long-term uptrend that has been interrupted by a violent, high-volume, event-shaped repricing on 2026-07-31 (−7.35% close-to-close, −8.58% opening gap, 132.5M shares)**. Eight sessions later the stock has built a **300.00–313.33 range** beneath a stalled 50 SMA, a falling 10 EMA, a freshly negative MACD, a VWMA sitting 4.16% *above* spot (trapped supply), and a Bollinger envelope expanding downward. Momentum has not repaired, but selling volume has dried up and RSI at 41.92 is not oversold — so this is **not a crash setup and not a bottom setup**. It is a **distribution-to-digestion phase with a downside bias**, where the highest-probability action is to **sell strength into 311–314 with a stop at 317.50, keep core long exposure intact while price holds above 297.91, and treat a high-volume break of 300.00 as the trigger for the next leg down toward 290 and the 279.87 200 SMA.**

---

## Summary Table

| Dimension | Indicator (value, 2026-08-11) | Reading | Implication |
|---|---|---|---|
| **Price** | Close 304.91 (−1.09% d/d); H 309.97 / L 302.79; Vol 37.48M | Lower high, light volume | Drift lower, low conviction |
| **Short-term trend** | 10 EMA **313.37** (price −2.70% below) | Falling 8 straight sessions (−2.24 pts/day) | Bearish; cross below 50 SMA imminent |
| **Medium-term trend** | 50 SMA **309.56** (price −1.50% below) | Slope collapsed +0.79 → +0.03 pts/day | **Trend exhaustion; SMA now resistance** |
| **Long-term trend** | 200 SMA **279.87** (price +8.95% above) | Rising +0.27 pts/day | **Bull market structure intact** |
| **MA structure** | 10 EMA 313.37 > 50 SMA 309.56 > 200 SMA 279.87 | Golden-cross stack, compressing | Bullish bias intact but eroding |
| **Momentum** | MACD **−0.827** vs signal **2.444**; hist **−3.271** | Crossover 07-31; **zero-line break 08-11** | Bearish regime; hist re-widening |
| **Momentum (RSI)** | **41.92** (peak 71.65 on 07-17) | Bearish divergence into 07-28 high | Weak but **not oversold**; ~12 pts of room |
| **Volatility** | ATR **8.81** (2.89% of price) | Up from ~8.1 July baseline | Wider stops, smaller size |
| **Envelope** | Mid **322.48** / UB **347.05** / LB **297.91** | Price below mid; width 15.2%, re-expanding down | Drift-down; LB is support ref |
| **Volume/participation** | VWMA **318.14** (price −4.16% below) | Volume-weighted holder underwater | **Distribution / overhead supply** |
| **Key pivot** | **300.00 – 302.79** (07-31, 08-03, 08-11 lows) | Triple-tested, declining volume | Coiling — resolution pending |
| **Gap zone** | **310.69 – 329.59** (07-31 high ↔ 07-30 low) | Unfilled for 8 sessions | Heavy resistance band |
| **Core stance** | Neutral-to-bearish tactical; constructive strategic | — | Sell 311–314, stop 317.50, targets 302.6 / 298 / 290.5 |
| **Invalidation (bearish)** | Daily close > 318.14 on >65M volume | — | Stand down |
| **Invalidation (bullish)** | Daily close < 300.00 on >70M volume | — | Target 290.55 → 279.87 |

*Indicator selection note: the eight core indicators used are `close_10_ema`, `close_50_sma`, `close_200_sma` (three time-horizons of trend with no redundancy), `macd` + `macds` (momentum regime and crossover timing — the histogram is derived as MACD minus signal and is reported only as supporting context), `rsi` (momentum extremes/divergence, deliberately not paired with another oscillator), `atr` (volatility for sizing and stops), and `vwma` (volume-confirmation, essential given the 132.5M-share outlier). The Bollinger envelope (`boll`/`boll_ub`/`boll_lb`) is used strictly as a supporting volatility cross-check rather than as an additional core selection.*