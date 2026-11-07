# AAPL — Multi-Timeframe Technical Analysis
**Analysis date: 2026-08-10 | Last verified close: $308.26**

---

## 1. Data Integrity & Verification Note

The last row of the OHLCV pull and the verified market snapshot **match exactly** on all fields (O: 306.83 / H: 308.26 / L: 304.61 / C: 308.26 / Vol: 44,812,500 / dividend 0.27). No discrepancy to flag between `get_stock_data` and `get_verified_market_snapshot`. All exact figures below are quoted from those two tool outputs.

One transparency note: the snapshot also returned an `mfi` value (0.50473). That indicator is **not** in my selected set and its scale is ambiguous, so I make no claims from it.

**Important accounting detail:** 2026-08-10 is an ex-dividend session ($0.27). The Aug 7 → Aug 10 close-to-close move of −5.07 (−1.62%) includes ~0.09% of ex-dividend mechanics. The economically meaningful decline is ~−1.53%. Do not double-count this when attributing the down day to selling pressure.

---

## 2. Indicator Selection & Rationale (8 selected)

| # | Indicator | Why it fits *this* market context |
|---|---|---|
| 1 | **close_10_ema** | AAPL is in a post-gap downtrend where a short-term mean is the fastest honest read on whether selling pressure is easing. Price has not closed above it once since the gap. |
| 2 | **close_50_sma** | This is the battleground. Price is oscillating *around* it (reclaimed Aug 5–7, lost Aug 10). It is also flattening — the single best evidence that the medium-term trend has stalled rather than broken. |
| 3 | **close_200_sma** | Needed to keep perspective: the long-term trend is still up and price is ~10% above it. Prevents over-bearish tactical framing. |
| 4 | **macd** | The line is collapsing toward zero from +9.61 in nine sessions. Zero-line crosses are the cleanest regime filter after a shock. |
| 5 | **macdh** | The histogram flipped negative on 2026-07-31 (−1.37 from +0.64) and is now −3.19. It is the earliest, most sensitive read on whether downside momentum is accelerating or decaying. |
| 6 | **rsi** | At 44.1 it says "neutral, room to fall" — critically, **not oversold**, so there is no mechanical mean-reversion bid yet. Also the cleanest place to hunt for a bullish divergence. |
| 7 | **atr** | Jumped from 8.02 (Jul 29) to 9.87 (Jul 31) and is still 8.94 = **2.90% of price**. Position sizing and stop placement are impossible without this. |
| 8 | **vwma** | The decisive **volume** input. At 319.09 it sits **$10.83 (3.51%) above price** — the volume-weighted cost basis of recent buyers is underwater. That is trapped supply overhead, invisible on a simple MA. |

*Supporting context only (retrieved, not counted in the 8): Bollinger middle 322.98 / upper 346.43 / lower 299.53. Used for envelope checks, since ATR already covers the volatility dimension.*

**Why no redundancy:** the three MAs are deliberately on separate timeframes (10/50/200 = days/weeks/months), MACD + histogram give level and rate-of-change (not the same thing), RSI is a normalized momentum oscillator independent of MACD's EMA construction, and ATR (volatility, $ terms) and VWMA (volume, price terms) are categorically different information streams.

---

## 3. Price Action: The Story in the Data

### The run-up
From the 2026-01-20 low close of **246.70**, AAPL built a persistent uptrend to the **2026-07-29 close of 338.19** — a gain of **+91.49 points (+37.08%)** over roughly six months. The July acceleration was sharp and volume-backed: 2026-07-15 +4.01% to 327.50 on 61.0M shares, then 2026-07-16 333.26 on 63.0M, culminating in an intraday high of **344.57 on 2026-07-29**.

### The shock
2026-07-30 closed **333.43**. On **2026-07-31** AAPL opened at **304.81** — a gap of −28.62 unfilled from the prior close — traded down to **300.00**, and closed **308.91** on **132,489,100 shares**, the highest volume since the 2026-06-26 session (261.8M). Single-session damage: **−24.52 (−7.35%)**.

### The failed bounce (the key finding)
Seven sessions later, the bounce has **not** repaired anything:

- **2026-08-06** high **316.29** → **2026-08-07** high **314.81** → **2026-08-10** high **308.26**. **Lower highs.**
- **Volume on the bounce decayed monotonically**: 75.0M (Aug 3) → 68.0M (Aug 4) → 49.4M (Aug 5) → 46.1M (Aug 6) → **34.4M (Aug 7)**. Rallying on shrinking volume into overhead supply is the textbook signature of a bear flag, not accumulation.
- Price **reclaimed the 50 SMA on Aug 5–7** (closes 311.00 / 312.41 / 313.33 vs 50 SMA 309.65 / 309.74 / 309.79) and then **lost it on Aug 10** (close 308.26 vs 50 SMA 309.70). A failed reclaim is a materially stronger bearish signal than never having reclaimed at all.
- **AAPL has not closed above the 10 EMA for seven consecutive sessions** (since 2026-07-31).
- **Aug 10 is a narrow-range day**: range 3.65 points = **0.41 × ATR(8.94)**, closing at the session high (308.26 = high) after opening at 306.83. Stabilization *attempt*, but on 44.8M shares — no conviction behind it.

### Historical precedent for these gap-shocks (explicitly caveated)
Two prior single-session shocks appear in the tool data, and both mean-reverted:
- **2026-02-11 close 275.50 → 2026-02-12 close 261.73** (−5.00%, 81.1M). Trough **255.78 on 2026-02-13**; pre-gap level reclaimed by **2026-02-25 (274.23)** — about 8 sessions.
- **2026-06-24 close 293.08 → 2026-06-25 close 275.15** (−6.11%, 107.0M). Trough low **274.21 on 2026-06-26**; pre-gap level not just reclaimed but exceeded by **2026-07-01 (294.38)** — about 5 sessions.

**This is two observations, not a validated edge**, and the current case is already diverging: six sessions after the gap, price is still 25.17 points below the pre-gap close, with lower highs and decaying volume. The "V-shaped recovery" playbook is **not** confirming so far.

---

## 4. Indicator-by-Indicator Read

**Trend stack — bearish short term, stalling medium term, intact long term**
- Close 308.26 < 10 EMA 315.25 (−6.99, −2.27%) → short-term trend down.
- Close 308.26 < 50 SMA 309.70 (−1.44, −0.47%) → medium-term support lost again.
- Close 308.26 > 200 SMA 279.64 (**+28.62, +10.24%**) → long-term uptrend intact.
- 50 SMA (309.70) > 200 SMA (279.64), spread 30.06, **both rising** → golden-cross regime structurally intact.
- **But the 50 SMA has stopped rising**: 309.79 (Aug 5) → 309.74 → 309.79 → 309.79 → **309.70 (Aug 10)**. First actual tick down. That is the definition of a stalling medium-term trend.
- **10 EMA is converging on the 50 SMA fast**: gap was 21.89 on Jul 30, now 5.55, closing at roughly 1.5 points/session. A **bearish 10/50 cross near ~310 within ~3–4 sessions** is the single most concrete forward-looking event on the chart.

**MACD — decisive bearish crossover already underway**
- MACD line: 9.61 (Jul 29) → **0.072 (Aug 10)**. Nine sessions, −9.54.
- Signal: 8.44 → **3.26**.
- Histogram: +0.64 (Jul 30) → −1.37 (Jul 31, the crossover) → −3.63 (Aug 5 trough) → −3.18 (Aug 7) → **−3.19 (Aug 10)**.
- **Nuance worth flagging:** the histogram has stopped deteriorating (−3.63 → −3.19 over three sessions) while price made a *lower* close on Aug 10. That is a *very early* hint of downside deceleration — but the MACD **line is still falling** (0.878 → 0.072) and is about to cross **below zero**. Decaying momentum in a still-negative configuration is not a buy signal; it is a "stop adding to shorts, don't buy yet" signal.
- Base case: **MACD goes negative within 1–3 sessions**, which historically coincides with trend continuation, not reversal, when the 10 EMA is this far below price.

**RSI — 44.10, neutral-bearish, no edge either way**
- Path: 71.65 (Jul 17) → 61.66 (Jul 30) → **43.24 (Jul 31)** → 40.34 (Aug 3) → 47.58 (Aug 7) → **44.10 (Aug 10)**.
- Two points: (a) the overbought condition from July has fully unwound, so the *fuel* for further downside is no longer "overbought pressure"; (b) at 44 it is **not oversold**, so there is no mechanical snap-back bid. RSI is squarely in no-man's-land — the absence of a signal is itself the signal: **no mean-reversion trade here.**

**Bollinger envelope — price in the bottom ~19% of the band**
- Middle 322.98, Upper 346.43, Lower 299.53. Bandwidth = 46.90 = **14.52% of the middle** — very wide.
- **%B = (308.26 − 299.53) / 46.90 = 18.6%.** Price is in the lower quintile, pressing the downside, but **not touching** the lower band — arguing against an "exhaustion bottom."
- Bands are **expanding** (width 40.29 on Jul 30 → 46.90 on Aug 10) — post-gap volatility expansion, not a squeeze. Breakouts from expanding bands have better follow-through than squeeze breakouts.

**ATR — 8.94 (2.90% of price)**
- Snapshot of the vol regime: 8.02 (Jul 29) → **9.87 (Jul 31)** → 8.94 (Aug 10). Roughly +11% above pre-gap volatility.
- Practical consequence: any stop tighter than ~$6 (0.7 ATR) will be noise-stopped. Use 1.0–1.5 ATR ($8.94–$13.41).
- Sizing math: risking 1% of equity with a 1-ATR stop implies notional exposure of ≈ 1% / 2.90% ≈ **34% of equity**; at 1.5 ATR ≈ **23%**.

**VWMA — the most underrated bearish datum**
- VWMA **319.09**, i.e. **$10.83 (3.51%) above the close**. The volume-weighted average transaction price of recent participants is meaningfully above spot.
- VWMA jumped from 296.42 (Jul 15) to 310.27 (Jul 17) — the breakout was transacted on 60–63M share days. VWMA peaked at **329.58 (Jul 30)** and has declined every session since.
- Interpretation: heavy supply was accumulated in the **$310–330** zone and is now losing money. That converts the gap zone into **active overhead resistance**, not just a chart memory. Combined with decaying bounce volume, this is a distribution read.

---

## 5. Levels (all derived from tool output, with source dates)

**Resistance (ascending)**
1. **309.70** — 50 SMA (Aug 10). Immediate; just lost.
2. **313.33–316.29** — Aug 7 close / Aug 6 high. The failed-bounce ceiling.
3. **315.25** — 10 EMA. Unreclaimed for 7 sessions.
4. **319.09** — VWMA. Trapped-supply pivot.
5. **322.98** — Bollinger middle (20 SMA). Mid-range magnet on any real repair.
6. **333.43–334.75** — Jul 30 close / Jul 30 high. The **gap-fill** ceiling; full repair target.

**Support (descending)**
1. **304.61** — Aug 10 low. First line.
2. **300.00–302.56** — the post-gap floor, tested three times: Jul 31 low **300.00**, Aug 3 low **302.56**, Aug 4 low **301.32**. This is the line in the sand.
3. **299.53** — Bollinger lower band (confluence with #2, ~$0.50 below the floor).
4. **289.20–294.38** — the Jul 1 low / Jul 1–2 consolidation base before the +4.84% breakout on 2026-07-02 (294.38 → 308.63).
5. **279.64** — 200 SMA. The long-term trend's last word, −9.3% below spot.

---

## 6. Actionable Playbook

**Base case (highest probability): bear flag resolving lower.** Seven sessions of lower highs, decaying bounce volume, a failed 50-SMA reclaim, MACD rolling through zero, and VWMA overhead all point the same way. RSI at 44 means there is room to fall without any mechanical support.

- **Trigger:** a decisive close below **304.61** (Aug 10 low), and preferably a break of **300.00** to invalidate the triple-tested floor.
- **Stop:** above **316.29** (Aug 6 high) — ≈1.4 ATR, or tighter above 309.70 if you want a high-false-positive-rate version.
- **Targets:** 299.53 → 294–289 zone → 279.64 (200 SMA).
- **Sizing:** with ATR at 2.90% of price, a 1.5-ATR stop implies ~23% of equity notional for a 1% risk budget.

**Bull case (requires proof, not hope).** The bull argument rests entirely on the intact 200 SMA (+10.24% below), the still-positive 50>200 spread, RSI's reset from 71.6 to 44, and the two prior gap-shock mean-reversions.
- **Trigger:** a close **above 316.29** on volume **>60M** (i.e., the bounce finally attracts real bid), plus the 10 EMA (315.25) reclaimed.
- **Confirmation:** MACD histogram turning up *and* MACD line stabilizing at/above zero; RSI back above 50; close above VWMA 319.09.
- **Targets:** 322.98 (Bollinger middle) → 333.43 (gap fill).
- Does **not** currently qualify. Do not front-run it.

**Neutral/invalidated zone.** While price chops between **304.61 and 316.29**, this is a coin flip with ATR at 2.90%. Both the RSI (44) and MACD (near zero) are in the least-informative part of their ranges. **Waiting is a position.** The ATR says the market is still paying you nothing to guess.

**Explicit falsification triggers — what would make me wrong**
- A close above **319.09 (VWMA) with volume above 60M** would flip the volume thesis from distribution to accumulation.
- **RSI printing a higher low (above 43.24) while price prints a lower low below 300** would be a genuine bullish divergence and would argue for the mean-reversion playbook.
- A **10 EMA crossing back above the 50 SMA** before it crosses below would invalidate the stalling-trend read.

---

## 7. Key Points Summary

| Dimension | Reading (2026-08-10) | Evidence (tool-sourced) | Bias |
|---|---|---|---|
| **Last close** | $308.26 (open 306.83, high 308.26, low 304.61) | Verified snapshot; vol 44,812,500; ex-div $0.27 | — |
| **Short-term trend (10 EMA)** | Bearish — no close above it in 7 sessions | 10 EMA **315.25** vs close 308.26 (−2.27%); EMA fell 331.31 (Jul 30) → 315.25 | **Bearish** |
| **Medium-term trend (50 SMA)** | Stalling → rolling over | 50 SMA **309.70**, first downtick (309.785→309.700); close 308.26 below it; reclaim Aug 5–7 **failed** Aug 10 | **Bearish** |
| **Long-term trend (200 SMA)** | Intact uptrend | 200 SMA **279.64**, rising daily; price +28.62 (**+10.24%**) above; 50>200 spread 30.06 | **Bullish** |
| **MACD** | Crossover done, zero-cross imminent | MACD **0.072** vs signal **3.26**; hist **−3.19**; flipped negative 2026-07-31 | **Bearish** |
| **MACD histogram** | Deeply negative but no longer worsening | −3.63 (Aug 5) → −3.18 → **−3.19**; MACD line still falling | Bearish (faint deceleration) |
| **RSI** | Neutral, **not oversold** | **44.10**; from 71.65 (Jul 17) and the 40.34 low (Aug 3) | **Neutral** |
| **Bollinger** | Lower quintile, bands expanding | Mid 322.98 / UB 346.43 / LB 299.53; **%B = 18.6%**; width 14.52% | **Bearish** |
| **ATR / risk** | Elevated | **8.94 = 2.90% of price**; 9.87 peak (Jul 31) vs 8.02 (Jul 29) | Use 1.0–1.5 ATR stops |
| **VWMA** | Trapped supply overhead | **319.09**, +10.83 (**+3.51%**) above close; peaked 329.58 (Jul 30) | **Bearish** |
| **Volume behavior** | Bounce died on shrinking volume | 132.5M (Jul 31 shock) → 75.0M → 68.0M → 49.4M → 46.1M → **34.4M (Aug 7)** → 44.8M (Aug 10) | **Bearish** |
| **Post-gap structure** | Bear flag; lower highs | Highs 316.29 (Aug 6) → 314.81 (Aug 7) → 308.26 (Aug 10); still −25.17 vs 333.43 pre-gap | **Bearish** |
| **Key support** | 304.61 → **300.00–302.56** (3 tests) → 299.53 → 289–294 → 279.64 | Jul 31 low 300.00; Aug 3 low 302.56; Aug 4 low 301.32; Boll LB 299.53 | — |
| **Key resistance** | 309.70 → 313.33–316.29 → 315.25 → 319.09 → 322.98 → 333.43 | 50 SMA / Aug 6–7 / 10 EMA / VWMA / Boll mid / Jul 30 close | — |
| **Primary trigger to watch** | 10 EMA crossing below 50 SMA near **~310** within ~3–4 sessions | 10 EMA−50 SMA gap 21.89 (Jul 30) → 5.55 (Aug 10) | Bearish confirmation |
| **Overall stance** | **Tactically bearish; strategically still bullish; not a buy yet** | No oversold condition, no volume confirmation, no MACD repair | **Wait / favor downside** |

---

**Bottom line for AAPL:** The long-term uptrend (200 SMA at 279.64, +10.24% below spot) is genuinely intact, but everything inside a three-month horizon has deteriorated. The 2026-07-31 gap (−7.35% on 132.5M shares) has not been repaired, the subsequent bounce produced lower highs on five consecutive sessions of declining volume, the 50 SMA reclaim failed on 2026-08-10, and VWMA at 319.09 confirms that recent volume-weighted buyers are underwater and represent overhead supply. With RSI at 44.10 and MACD about to cross zero, there is no oversold cushion to catch a falling price. The trade is to respect the $300–302 floor and the $316.29 bounce ceiling, let the ATR (2.90% of price) dictate size, and demand volume confirmation above 319 before treating this as anything more than a pause in an unfinished correction.