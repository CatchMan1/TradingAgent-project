# AAPL — Technical & Tactical Assessment
**As of the verified session: 2026-09-16 (close)**

---

## 0. Data verification (source of truth check)

I cross-checked the full OHLCV pull against the deterministic `get_verified_market_snapshot` for 2026-09-16. **No discrepancies were found** — the latest row and every indicator value agree exactly:

| Field | Verified value (2026-09-16) |
|---|---|
| Open / High / Low / Close | 332.53 / 335.48 / 330.70 / **332.41** |
| Volume | 35,981,000 |
| 10 EMA / 50 SMA / 200 SMA | 326.66 / 319.27 / 285.79 |
| MACD / Signal / Histogram | 4.6309 / 3.0924 / 1.5385 |
| RSI (14) | 62.10 |
| ATR | 7.3538 (≈2.21% of price) |
| VWMA | 323.32 |
| Bollinger mid / upper / lower | 320.39 / 336.78 / 304.00 |
| Total-return index | 338.317 (vs. price 332.41) |

All references below are drawn from these two tool outputs; percentages are simple arithmetic on those dated prices.

---

## 1. Price context: a repaired gap, one step below the fill

AAPL is trading at **332.41**, in a broad, well-defined recovery from the summer drawdown:

- **Period high:** 344.57 intraday (2026-07-29); closing high **340.08** (2026-07-28).
- **Period low:** 243.42 intraday (2026-01-20). The stock is **+36.6% above** that low.
- **Current price is 3.7% below the 344.57 high.**
- The defining event in the recent tape is the **2026-07-31 gap-down**: AAPL closed 333.43 on 7/30 and opened 304.81 on 7/31, closing that day at 308.91 (**-7.35%**, volume 132.5M). The gap between 304.81 and 333.43 remains unfilled.
- From the 7/31 low of **300.00** (retested by the 8/12 low of **300.57** — a double-bottom around 300), price has recovered **+10.8%**.
- From the 8/12 close of 302.25 to today's 332.41, the stock is **+9.98%**.
- The last leg was sharp: **315.34 (9/9) → 332.41 (9/16), +5.41% in five sessions**, including a **+3.56%** session on 9/10 (315.34 → 326.57) on **70.0M shares**, i.e. ~1.67× the ~41.9M 20-session average volume.

**The key nuance:** today's close of 332.41 is only **0.31% (1.02 points) below the 7/30 pre-gap close of 333.43**. In other words, AAPL has retraced essentially the entire July 31 gap and is now testing the origin of the breakdown. This is the single most important tactical level on the chart.

---

## 2. Trend structure: bullish stack, mature trend, extended from the long-term mean

The moving-average stack is unambiguously bullish and correctly ordered:

- **Close 332.41 > 10 EMA 326.66 (+1.76%) > 50 SMA 319.27 (+4.12%) > 200 SMA 285.79 (+16.32%)**
- **50 SMA is 11.72% above the 200 SMA**, and both are rising. This is a firmly established long-term uptrend, not a fresh cross. The 200 SMA climbed from 274.58 (7/20) to 285.79 (9/16), **+4.08%**, even through the July–August selloff.
- The **10 EMA is accelerating**: 318.26 (9/9) → 326.66 (9/16), **+2.64% in five sessions**, confirming the short-term impulse is up.
- The **50 SMA stopped falling and turned up**: it bottomed at ~309.08 on 8/17 and has risen to 319.27 by 9/16 (**+3.30%**).
- **Confluence reclaim:** price closed back above both the 50 SMA and the VWMA on **8/18** (close 310.03 vs. 50 SMA 309.13 and VWMA 309.70) and has held that structure since. The only exception was **9/9**, when the close of 315.34 was 0.36% *below* the then-50 SMA of 316.47 — immediately reclaimed the next day (9/10 close 326.57).

**Interpretation:** the primary trend is up on every timeframe, and the medium-term trend has re-engaged. The caution is *extension*: price is 16.3% above its 200 SMA and the 50 SMA is 11.7% above the 200 SMA. Historically, such stretched configurations are vulnerable to sharp air pockets — and this stock already demonstrated one on 7/31 (-7.35% in a session). Trend is a tailwind; valuation of the trend (distance from mean) is a headwind.

---

## 3. Momentum: bullish re-acceleration, but decelerating at the margin

**MACD (4.6309) vs. Signal (3.0924), Histogram +1.5385:**

- The **bullish signal-line crossover occurred around 2026-08-26**, when the histogram flipped from -0.149 (8/25) to +0.152 (8/26).
- The **zero-line crossover followed on 2026-08-31** (MACD -0.028 on 8/28 → +0.297 on 8/31). Both are classic trend-confirmation events.
- The MACD line bottomed at **-2.676 on 8/17** and has risen monotonically to **+4.631**, a very large swing in under a month.
- The histogram peaked at **+2.028 on 9/3**, compressed to **+0.426 on 9/9** (the shakeout), then re-expanded to **+1.625 on 9/14**. It has since eased marginally: **1.597 (9/15) → 1.538 (9/16)**.
- **Read:** momentum is positive and above the zero line, but the histogram has now contracted for two straight sessions while price closed essentially flat. That is *deceleration at resistance*, not a reversal — but it argues against chasing strength at 332–335.

**RSI (14) at 62.10:**

- Recovered from **40.22 (8/12)** to 62.10 — a strong, orderly recovery.
- Not overbought (<70). In the 60-session lookback the RSI peak was **68.90 on 7/28**, when the close was 340.08 — so today's lower price with lower RSI is internally consistent, **not a bearish divergence**.
- RSI has made a series of higher lows since 8/12 (40.22 → 41.92 on 8/11? no — 40.22 on 8/12 was the low), and the recent dip to **49.35 on 9/9** was bought. The 50-line has been reclaimed and is holding.
- **Read:** RSI says there is *room* to run before becoming stretched, but it also says the easy part of the bounce is behind us.

---

## 4. Volatility and risk: compression after a shock

- **ATR is 7.3538**, or **2.21% of the 332.41 close**.
- ATR peaked at **9.872 on 7/31** (the gap day) and has steadily declined to 7.35, i.e. **-25.5%**. Volatility is normalizing — typical of a post-shock repair phase.
- **Bollinger context (verified snapshot):** mid 320.39, upper 336.78, lower 304.00. Bandwidth = **10.23%** of the mid-band. Price sits at **%B = 0.867**, i.e. in the upper quarter of the band but **not touching the upper band** (1.31% below it).

**Risk-management arithmetic (ATR-based):**

| Stop reference | Price | Distance from 332.41 |
|---|---|---|
| 1.0 × ATR | 325.06 | -2.21% |
| 1.5 × ATR | 321.38 | -3.32% |
| 2.0 × ATR | 317.70 | -4.43% |
| 50 SMA | 319.27 | -3.95% |
| 10 EMA | 326.66 | -1.73% |

A 1.5×ATR stop (≈321.4) sits almost exactly at the 50 SMA — a convenient structural/volatility confluence. A 2×ATR stop (≈317.7) sits just below it. For position sizing, a 1% account risk with a 3.3% stop implies roughly a 30% notional position; with a 4.4% stop, roughly 23%.

---

## 5. Volume and participation: buyers in control, but the last push was thin

- **Price is 2.81% above VWMA (323.32)**. The VWMA has risen from **307.76 (8/19) to 323.32 (9/16)**, confirming that the recovery has been volume-supported rather than a pure drift.
- Price crossed back above the VWMA on **8/18** and has stayed above it since — the volume-weighted average holder of the recent tape is in profit.
- **The strong hands showed up on 9/10:** 70.0M shares on a +3.56% day, 1.67× the ~41.9M 20-session average. That is the highest-volume up-day of the recovery and validates the 326.5 breakout.
- **But participation has faded into resistance:** 9/14 39.3M, 9/15 31.7M, 9/16 36.0M. The latest session is **~14% below** the 20-session average. Rising price on falling volume into a known resistance cluster is a classic *warning of exhaustion*, even if it is not yet a sell signal.
- **Outlier prints to be aware of** (they can distort VWMA depending on the vendor's window): 261.8M on 2026-06-26 and 132.5M on 2026-07-31 — both likely index/rebalance or event-driven.

---

## 6. Key levels (all drawn from actual dated prices)

**Resistance**

| Level | Source |
|---|---|
| **344.57** | 2026-07-29 intraday high — period high |
| **340.08** | 2026-07-28 closing high |
| **336.78** | Bollinger upper band (9/16) |
| **335.48–336.22** | Triple rejection: 9/11 high 336.22, 9/14 high 335.50, 9/16 high 335.48 |
| **333.43** | 2026-07-30 close — full gap-fill reference (only 0.31% above spot) |

**Support**

| Level | Source |
|---|---|
| **330.70** | 9/16 low |
| **326.57–326.66** | 9/10 close and rising 10 EMA |
| **323.32** | VWMA |
| **319.27–319.97** | 50 SMA and 9/4 close |
| **315.34–316.22** | 9/8–9/9 closes; 9/9 intraday low 309.90 |
| **307.01–310.65** | 8/20–8/21 lows |
| **300.00–302.25** | 7/31 low and 8/12 low/close — double-bottom shelf |
| **285.79** | 200 SMA |
| **274.21** | 2026-06-26 low — major swing low |

---

## 7. Scenarios and an actionable plan

**Base case (neutral-to-bullish consolidation):** AAPL grinds between **326.5 and 336.2** while it works off the July gap. Momentum is positive but flattening, volume is light, and the 335.5–336.2 zone has rejected price three times (9/11, 9/14, 9/16). Expect chop and false breaks until either 336.2 is cleared on volume or 326.5 fails.

**Bullish trigger (breakout):** A **daily close above 336.3** — above the triple-rejection zone and the upper Bollinger band of 336.78 — preferably on volume above the 41.9M average, would confirm the gap fill and open **340.08** (7/28 closing high) and then **344.57** (7/29 high). Note the reward/risk at that entry is thin: a stop back below 330.70 is ~1.7% risk against ~1.1% to the first target. **A breakout entry should therefore be scaled and confirmed, not chased.**

**Bearish/invalidation trigger:** A **daily close below 326.5** (10 EMA / 9/10 breakout close) would neutralize the short-term setup and shift the focus to **323.3 (VWMA)** and then **319.3 (50 SMA)**. A close below **319.0** would break the medium-term structure that has held since 8/18 and expose **315.3** and the **307–310** shelf. ATR says a normal daily range is ~7.35 points, so one or two bad sessions could reach these levels without anything abnormal occurring.

**Execution preferences:**

1. **Do not initiate size at 332.41.** The stock is 0.3% under a full gap-fill, 1.3% under the upper Bollinger band, and directly beneath a triple-rejection zone, with volume fading. Upside to 344.57 is +3.66% while a 2×ATR stop is -4.43% — negative asymmetry.
2. **Preferred long entry:** pullback into **326.5–323.3** (10 EMA to VWMA), stop **below 319.0** (50 SMA), initial target **335.5–336.2**, then 340. This offers roughly 3–4% risk against 4–5% first-target reward plus a trend tailwind.
3. **Alternatively:** wait for a **close > 336.3 on >41.9M volume**, enter partial, add on a successful retest of 333–334, and use 326.5 as the stop.
4. **Long-term holders:** the 50 > 200 structure and rising 200 SMA justify holding a core position; the 16.3% extension above the 200 SMA argues against large new strategic adds at 332.

---

## 8. Why these eight indicators

The context is a **post-gap repair inside an established long-term uptrend, with contracting volatility and re-accelerating but flattening momentum** — so the set needs to answer four distinct questions without redundancy:

- **Trend direction and location:** `close_10_ema` (timing/entry), `close_50_sma` (medium-term structure and the key 319 support), `close_200_sma` (long-term benchmark and extension gauge). These three give a time-layered view rather than three versions of the same signal.
- **Momentum:** `macd` (trend/zero-line confirmation), `macdh` (acceleration vs. deceleration — critical right now, since the histogram is rolling over at resistance), `rsi` (overbought/oversold and divergence check without duplicating MACD).
- **Volatility/risk:** `atr` — essential after a -7.35% gap day; it converts the levels into volatility-scaled stops and position sizes.
- **Participation:** `vwma` — distinguishes a genuine, volume-backed recovery from a low-volume drift; it is the reason the 8/18 reclaim was credible and the reason the current low-volume push deserves caution.

Deliberately excluded: Bollinger bands as a *selected* indicator (the verified snapshot provides exact band levels and %B, so a dedicated call would duplicate the mean-reversion signal already delivered by RSI + ATR); `stochrsi` (redundant with RSI); `macds` (its crossover information is already encoded in `macdh`).

---

## Summary table

| Dimension | Latest reading (2026-09-16) | Signal | Actionable implication |
|---|---|---|---|
| **Close** | 332.41 | 0.31% below the 7/30 gap-fill close of 333.43 | The whole July gap is effectively retraced; decision point |
| **10 EMA** | 326.66 (+1.76% below price) | Rising fast (318.26 on 9/9) | First support / short-term trend intact |
| **50 SMA** | 319.27 (+4.12% below price) | Turned up from 309.08 (8/17) | Medium-term floor; stop cluster ~319 |
| **200 SMA** | 285.79 (+16.32% below price) | Rising (274.58 on 7/20); 50 > 200 by 11.72% | Long-term bull, but trend is extended |
| **MACD** | 4.6309 (signal 3.0924) | Bullish cross 8/26; zero cross 8/31 | Trend confirmation, still positive |
| **MACD hist.** | +1.5385 | Peaked 2.028 (9/3); eased 1.625 → 1.538 | Momentum decelerating at resistance |
| **RSI (14)** | 62.10 | Not overbought; peak 68.90 (7/28); no divergence | Room higher, but not a cheap entry |
| **ATR** | 7.3538 (2.21%) | Down 25.5% from 9.872 (7/31) | Volatility compressing; use ~7.4-pt units for stops |
| **VWMA** | 323.32 (+2.81% below price) | Rising from 307.76 (8/19); reclaimed 8/18 | Volume confirms recovery; average buyer in profit |
| **Bollinger (snapshot)** | Mid 320.39 / UB 336.78 / LB 304.00; %B 0.867 | Upper-quartile, not at band | 336.8 is resistance confluence |
| **Volume** | 35.98M vs. ~41.9M 20-day avg (-14%) | 9/10 spike 70.0M; three days of fading volume | Breakout needs volume confirmation |
| **Nearest resistance** | 333.43 / 335.48–336.22 / 336.78 / 340.08 / 344.57 | Triple rejection at 335.5–336.2 | Only a close >336.3 validates upside |
| **Nearest support** | 330.70 / 326.57–326.66 / 323.32 / 319.27 | 10 EMA and VWMA layered below | 326.5 is the short-term line in the sand |
| **Bias** | **Constructive but not chase-worthy** | Uptrend + positive momentum vs. resistance + fading volume | Buy 323–326.5 dips or a confirmed >336.3 breakout; avoid mid-range entries |
| **Risk parameters** | 1.5×ATR = 321.4; 2×ATR = 317.7 | Stop just below 50 SMA / swing structure | Size positions off ~3.3–4.4% stop distance |