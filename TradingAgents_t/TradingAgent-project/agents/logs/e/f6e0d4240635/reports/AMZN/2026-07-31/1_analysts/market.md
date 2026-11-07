# AMZN — Multi-Horizon Technical Deep Dive
**Analysis date:** 2026-07-31 (latest completed session in the dataset)
**Primary source of truth:** `get_verified_market_snapshot` (2026-07-31). All OHLCV and indicator levels below are taken from that snapshot and cross-checked against the `get_stock_data` CSV — the 2026-07-31 row is **identical in both sources**, so there is no data conflict to flag.

---

## 1. The headline event: a violent, high-volume regime shift

The single most important observation is the last two sessions.

| Date | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|
| 2026-07-29 | 229.32 | 232.82 | 226.16 | 226.65 | 44.96M |
| 2026-07-30 | 233.35 | 239.82 | 231.06 | 235.50 | 101.84M |
| 2026-07-31 | 265.00 | 273.23 | 262.01 | **271.58** | **129.05M** |

- 2026-07-31 gap: prior close 235.50 → open 265.00 (+12.5% gap), close 271.58 = **+15.3% on the session**.
- Two-session move: 226.65 (7/29 close) → 271.58 = **+19.8%**.
- Off the 7/29 intraday low of 226.16 → 271.58 = **+20.1%**.
- The close sits at **85% of the day's range** (range 262.01–273.23), i.e. buyers held into the bell, though the day's high of 273.23 was not reclaimed.
- Volume of 129.05M is roughly **3x the ~30–50M typical July sessions** and the heaviest print since 2026-06-26's 248.37M outlier.

**Interpretation:** this is a single-catalyst repricing (the volume signature and the gap profile match the pattern of AMZN's prior event days — see §9 for why that matters). Every moving average, band and oscillator reading below is therefore *distorted by one print*, and must be read as "post-event state," not as the smooth trend that existed on 2026-07-30.

---

## 2. Indicators selected (and why)

| Indicator | Value 2026-07-31 | Why it earns a slot here |
|---|---|---|
| **close_200_sma** | 235.0122 | The strategic line in the sand. Price is 15.6% above it — the only thing distinguishing "pullback in an uptrend" from "failed rally." |
| **close_50_sma** | 246.629 | Medium-term trend spine and the first *meaningful* downside reference after the gap. Just printed its first uptick in weeks (246.384 → 246.629). |
| **close_10_ema** | 242.7047 | Short-term momentum gauge. Best proxy for "is the gap-hold intact or is it bleeding out." |
| **macd** (+ macds/macdh) | -0.6231 / -1.8356 / **+1.2125** | Captures whether the move has genuine momentum backing. Note: **momentum is still below the zero line** — see §4. |
| **rsi** | 67.8788 | Non-redundant overbought/stretched check without duplicating MACD's job (I deliberately did **not** add stochrsi — it would be pure redundancy). |
| **boll_ub / boll / boll_lb** | 264.2034 / 243.8580 / 223.5126 | Upper band straddle quantifies *how far outside* normal dispersion price closed — the single cleanest "extension" metric available. |
| **atr** | 9.5114 | Non-negotiable for position sizing and stops after a +15% day. ATR jumped +29.6% in one session (7.3408 → 9.5114). |
| **vwma** | 245.7199 | Confirms whether the rally happened on *real* participation. Price sits 10.5% above VWMA = the volume-weighted cost basis of recent holders is far below spot. |

---

## 3. Trend structure: three horizons that disagree

**Long term (200 SMA) — intact and mildly constructive.**
200 SMA = 235.01, rising steadily (232.86 on 2026-06-30 → 235.01 now). Price 271.58 = **+15.56% above** it. The 50 SMA (246.63) remains **4.94% above** the 200 SMA, so the long-term golden-cross structure from earlier in the year has *not* been invalidated by the May–July drawdown.

**Medium term (50 SMA) — was deteriorating, now challenged.**
The 50 SMA fell almost monotonically from 255.69 (2026-06-30) to 246.384 (2026-07-30) — a textbook declining-medium-trend profile that mirrored the price slide from the May high. On 2026-07-31 it ticked up to 246.629, the **first uptick in the visible window**. One session does not make a trend, but it is the first evidence of the medium-term slope flattening.

**Short term (10 EMA) — whipsawed, now decisively reclaimed.**
The 10 EMA collapsed from 247.60 (7/20) to 236.288 (7/30) as price slid, then price exploded to 271.58 = **+11.90% above** the 10 EMA (242.70). That is extreme short-term extension; historically such gaps to the 10 EMA mean-revert intraday-to-swing even in genuine uptrends.

**Bottom line:** the trend hierarchy is *bullish-to-neutral long term, freshly repaired short term, unresolved medium term.* The 2026-07-31 candle did not create a new uptrend; it bought the bulls a large option on one.

---

## 4. Momentum: bullish crossover, but a low-quality one

- MACD line: **-0.6231**. Signal: **-1.8356**. Histogram: **+1.2125**.
- The histogram flipped from **-1.4955 (7/30)** to **+1.2125 (7/31)** — a fresh bull cross *on the last session*.
- **Critical nuance:** the MACD line is still **below zero**, so this is a *below-zero bull cross* — the weakest class of MACD signal, and one that often fails.
- **Also critical:** this is a **re-cross**, not a first cross. The histogram was already positive from 2026-07-15 (MACD 0.2602 vs signal -1.8642) through 2026-07-22, then flipped negative on 2026-07-23 and stayed negative for six sessions. The July 15–22 bullish setup *failed* (price fell from 254.96 on 7/15 to 226.65 on 7/29). Treating the 7/31 cross as validated would be repeating that mistake.
- **RSI 67.8788** — up from 44.41 (7/30) and 33.31 (7/29, the washed-out reading of the local bottom). RSI is now within ~2 points of the 70 overbought line. In strong trends RSI can ride above 70, so this is not a sell signal by itself — but it means the *easy* momentum entry has already happened.
- **Divergence watch:** the highest RSI in the visible window was 60.14 on 2026-07-15 at a 254.96 close. Price is now 6.5% higher with RSI only 7.7 points higher — no bearish divergence yet, but if price prints 274–278 with RSI *below* ~68, that would be a genuine negative divergence and a warning.

---

## 5. Volatility and extension: the most cautionary part of the chart

| Metric | 2026-07-30 | 2026-07-31 | Change |
|---|---|---|---|
| ATR | 7.3408 | **9.5114** | **+29.6%** |
| Boll upper | 258.0216 | 264.2034 | +6.18 |
| Boll middle | 242.4125 | 243.8580 | +1.45 |
| Boll lower | 226.8034 | 223.5126 | -3.29 |
| Band width | 31.22 | **40.69** | +30.3% |

- Close of 271.58 is **+7.38 points (+2.8%) above the upper Bollinger band (264.20)**. Closing outside the band is by definition a statistical breakout — but with the band having *just expanded 30%*, the upper band is now chasing price rather than containing it. In practice this configuration resolves two ways: a second leg higher (band ride), or a snap-back to the middle band at 243.86 — which is **10.2% below spot**.
- ATR/price = **3.5%**. For risk purposes: 1 ATR = 9.51 points; a 1-ATR stop from 271.58 sits at 262.07 — almost exactly the 7/31 low of 262.01. A 1.5-ATR stop = ~257.3; a 2-ATR stop = ~252.6.
- **The unfilled gap is enormous:** 7/30 high 239.82 → 7/31 low 262.01 = a **22.19-point (8.4%) void with zero trade inside it.** Technically it is air below the market; there is no volume shelf to arrest a slide between 262 and 240.

---

## 6. Participation: volume confirms, but the cost basis is a double-edged sword

- VWMA = **245.7199**; price is **+10.5% above** it. On 7/30 the VWMA was 240.818, so the two heaviest sessions of the month (101.84M and 129.05M shares) pulled the volume-weighted average sharply higher — real, size-driven accumulation, not a thin-tape drift.
- Implication A (bullish): the average recent buyer is deeply in profit, so there is little *underwater* supply to create overhead selling pressure on the way up.
- Implication B (bearish): the same fact means there is a large cohort with a 10%+ cushion that can be liquidated without hesitation if sentiment flips — exactly the dynamic that produced the 2026-06-26 volume spike (248.37M shares) and the low of 226.13 that day.

---

## 7. The context that matters most: where 271.58 sits in the bigger range

The May–July structure is a wide distribution range, and 7/31 closed *inside* it, near the top:

- **Range top:** intraday high 278.56 (2026-05-05); 277.80 (2026-05-06); highest **close** 274.99 (2026-05-06).
- **Range bottom:** 226.16 (2026-07-29 low), 226.13 (2026-06-26 low).
- Decline from 278.56 → 226.16 = **-52.40 points (-18.81%)**.
- The +19.8% two-day surge retraced the *entire* decline: 50% = 252.36 (cleared), 61.8% = 258.54 (cleared), 78.6% = 267.35 (cleared), 100% = 278.56 (not yet).
- 271.58 is **-1.24% below the 274.99 close high** and **-2.51% below the 278.56 intraday high**.

This is a full **V-shaped retracement in two sessions**, terminating directly beneath the most heavily defended supply zone of the past three months. That is a genuinely difficult spot: maximum momentum, maximum overhead resistance.

---

## 8. Actionable level map

**Resistance**
- 273.23 — 2026-07-31 high (immediate trigger)
- 274.99 — highest close in range (2026-05-06)
- 277.80 / 278.56 — range top (2026-05-06 / 2026-05-05 highs)

**Support**
- 264.20 — Bollinger upper band (now the first shelf)
- 262.01 — 2026-07-31 low (gap-hold line)
- 258.54 — 61.8% retracement of the May–July decline
- 252.36 — 50% retracement
- 246.63 — 50 SMA
- 243.86 — Bollinger middle band / 242.70 — 10 EMA (**cluster: this is the real line of consequence**)
- 239.82 → 235.50 — top of the unfilled gap / gap-day prior close
- 235.01 — 200 SMA
- 230.86 / 226.65 / 226.16 — late-July lows
- 223.51 — Bollinger lower band

---

## 9. Scenario playbook

**Bull continuation (primary tactical setup, but needs a trigger)**
- Trigger: a **close above 273.23**, ideally with volume ≥ 60M. That opens 274.99 → 277.80/278.56.
- Confluence: MACD histogram stays positive and the MACD line crosses **above zero** (currently -0.62 — that is the confirmation that is missing).
- Stop: below 262.01 (7/31 low) = ~1 ATR of risk from 271.58, roughly **3.5%**. Alternative structural stop: 257.3 (1.5x ATR).
- Position sizing: because ATR is 3.5% of price, size to a fixed *dollar* risk — a 1-ATR stop is 3.6x wider than it was in mid-July (ATR 7.34 on 7/30, and ~6.87 on 2026-06-01). Halve normal size versus a pre-gap regime.

**Base case / most likely near term — digestion of the gap**
- The combination of RSI 67.9, +11.9% above the 10 EMA, +2.8% above the upper Bollinger band, a below-zero MACD cross, and hard resistance at 274–278 argues for chop/retracement rather than immediate trend extension.
- Preferred entry zone: **258–264** (61.8% fib 258.54, 7/31 low 262.01, upper band 264.20). This is the zone where an add is buying support instead of chasing a 15% candle.
- Do **not** add between 265 and 273 without a fresh high — that is the worst risk/reward in the structure.

**Bear / invalidation**
- First warning: a close **below 262.01** (7/31 low) — the gap stops holding.
- Structural break: a close **below the 242.70–246.63 cluster (10 EMA / 50 SMA)**. That would simultaneously break the 10 EMA, the 50 SMA, the Bollinger middle band, and (roughly) the VWMA at 245.72 — four independent confirmations in one zone. Below it, the 22-point air pocket to **239.82/235.50 (200 SMA at 235.01)** becomes the path of least resistance.
- Historically grounded caution: AMZN's own recent event gaps have **not** held. On 2025-10-30 AMZN closed 222.86; the 2025-10-31 gap-day closed 244.22; it peaked at 258.60 on 2025-11-03 (two sessions later) and then fell to 217.14 by 2025-11-20 — **-11.1% below the gap-day close and -16.0% below the gap-week peak.** The opposite-direction analog is equally instructive: 2026-02-05 closed 222.69, gapped to a 2026-02-06 open of 202.70, and kept sliding to 198.79 by 2026-02-13. Both cases show one-day gap emotion being substantially retraced. I am not claiming 7/31 will repeat this — I am flagging that "the gap is the new trend" has been a losing assumption on this name recently.

---

## 10. Risks, caveats, and what would change my mind

1. **Single-print distortion.** Every MA/band/oscillator level here is contaminated by one 15% session. The 50 SMA declines 0.3–0.7 points/day at its current pace; the true medium-term trend will only be readable after 5–10 sessions.
2. **Catalyst is unverified.** The tools give me no news, earnings, or fundamentals. The volume signature (101.8M then 129.1M) plus the gap profile is *consistent with* an event-driven repricing, but I cannot confirm the cause, and a move of this size without a durable fundamental driver has a much higher retracement probability.
3. **Below-zero MACD + failed prior cross** = momentum confirmation is genuinely weak, notwithstanding the green histogram.
4. **Extended versus every reference:** +15.6% vs 200 SMA, +10.1% vs 50 SMA, +11.9% vs 10 EMA, +10.5% vs VWMA, +2.8% above the upper band. Mean-reversion pressure is high even under a bullish thesis.
5. **Volatility regime change.** ATR up 29.6% in one day means yesterday's stop distance is today's noise. Rewrite stops; do not carry pre-7/30 risk parameters into this regime.
6. **What would flip me constructive:** a MACD zero-line cross, a hold of 262 on any retest with declining volume, and a decisive breakout above 278.56. **What would flip me defensive:** any close below 262.01, or an RSI print in the mid-60s on a new price high (bearish divergence).

---

## 11. Summary table

| Dimension | Reading (2026-07-31) | Signal | Key level | Actionable note |
|---|---|---|---|---|
| **Latest session** | O 265.00 / H 273.23 / L 262.01 / **C 271.58** / V 129.05M | Gap +15.3%, close at 85% of range | — | Heaviest volume since 2026-06-26 |
| **Long-term trend** | close_200_sma **235.0122**, rising | Bullish (price +15.56%) | 235.01 | Strategic support; far below spot |
| **Medium-term trend** | close_50_sma **246.629** (first uptick in weeks) | Repairing / unresolved | 246.63 | 50 SMA still 4.94% above 200 SMA |
| **Short-term trend** | close_10_ema **242.7047** | Bullish but stretched (+11.90%) | 242.70 | Extreme extension vs 10 EMA |
| **Momentum (MACD)** | macd **-0.6231**, signal -1.8356, hist **+1.2125** | Fresh bull cross, below zero | 0.00 line | Prior July cross failed — needs zero-line cross |
| **Momentum (RSI)** | **67.8788** (from 44.41 prior day) | Strong, approaching overbought | 70 | Watch for divergence above 274 |
| **Volatility (ATR)** | **9.5114** (+29.6% d/d) | Regime shift up | 262.07 (1 ATR) | ATR = 3.5% of price → cut size |
| **Bollinger** | UB **264.2034** / mid **243.8580** / LB **223.5126** | Close **+2.8% outside upper band** | 264.20 | Band width expanded 30% in a day |
| **Participation** | vwma **245.7199** | Confirms real accumulation; price +10.5% | 245.72 | Large profit cushion = latent supply |
| **Structure** | Full V-retrace of 278.56→226.16 decline in 2 sessions | At range top, not through it | 274.99 / 278.56 | −1.24% / −2.51% from those highs |
| **Primary trigger (long)** | Close > **273.23** on ≥60M volume | Pending | Targets 274.99 → 278.56 | Stop 262.01 (~3.5% risk) |
| **Preferred entry** | Pullback to **258–264** | Not yet active | Fib 61.8% = 258.54 | Do not chase 265–273 |
| **Invalidation** | Close < **262.01**, structural break < **242.70–246.63** | Bearish | Gap air pocket to 235.50 / 200 SMA 235.01 | Four indicators break at once |
| **Biggest risk** | One-day, uncaused repricing; prior AMZN gaps (2025-10-31, 2026-02-06) partially retraced | Caution | — | Treat 7/31 as an option, not a trend |
| **Stance** | Constructive bias, **no chase**; buy support, require breakout confirmation | Selective long / neutral-until-confirmed | — | Risk off if 262.01 gives way |