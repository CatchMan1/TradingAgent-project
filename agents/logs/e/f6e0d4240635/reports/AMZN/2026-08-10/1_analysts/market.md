# AMZN — Deep-Dive Technical Report (as of close 2026-08-10)

## 1. Bottom line

AMZN is in a **post-catalyst breakout-and-hold regime**, not a mature trend. A single-session repricing on 2026-07-31 (prior close 235.50 → close 271.58, +15.3%) reset every trend and volatility measure on the chart. Price has since consolidated rather than retraced: after the 2026-08-03 peak close of 284.02, the stock corrected only to 272.26 (2026-08-06, −4.1%) and has now recovered to **278.09** on 2026-08-10 — within ~2.1% of the post-gap high.

The tape is **bullish but extended and decelerating**. Trend structure is unambiguously positive (price above the 10 EMA, 50 SMA and 200 SMA, both SMAs rising). Momentum is strongly positive (MACD 8.37, its highest in the visible 60-session window) but the histogram has now declined for four consecutive sessions — a classic "momentum plateau inside consolidation." RSI at 65.87 is constructive rather than overbought, having cooled from 72.23 on 2026-08-03.

The tactical problem is location, not direction: **278.09 sits directly inside the April–May 2026 supply shelf** (intraday highs of 273.88 on 2026-04-30, 278.56 on 2026-05-05) with the 2026-08-03 high of 287.20 overhead, while the 2026-07-31 gap (235.50 → 265.00 open) remains **entirely unfilled** ~5% below.

---

## 2. Verified price state (source of truth)

From `get_verified_market_snapshot` for 2026-08-10 (identical to the `get_stock_data` rows — **no discrepancy found**):

| Field | Value |
|---|---|
| Open / High / Low / Close | 274.01 / 280.14 / 273.60 / **278.09** |
| Volume | 35,731,900 |
| 10 EMA | 266.0273 |
| 50 SMA | 247.5888 |
| 200 SMA | 236.8169 |
| MACD / Signal / Histogram | 8.3729 / 4.4685 / 3.9044 |
| RSI | 65.867 |
| Bollinger (20,2) mid / upper / lower | 253.1315 / 290.6939 / 215.5691 |
| ATR | 9.1334 |
| VWMA | 257.3079 |
| MFI (as returned) | 0.51769 |

⚠️ **Flag:** the snapshot returns MFI as **0.51769**, i.e. on a 0–1 scale (~51.8 if rescaled to 0–100). I am treating it as *approximately neutral money flow*, not as an extreme reading. Note that this neutral money-flow print conflicts directionally with RSI 65.9 and is consistent with the volume dry-up discussed in §6 — but the scale ambiguity means I do not build a signal on it.

---

## 3. The regime shift: what 2026-07-31 actually did

| Date | Close | Volume | Note |
|---|---|---|---|
| 2026-07-29 | 226.65 | 44.96M | Swing low close |
| 2026-07-30 | 235.50 | 101.84M | Volume already elevated *into* the print |
| 2026-07-31 | 271.58 | **129.05M** | Gap open 265.00; +15.3% session |
| 2026-08-03 | 284.02 | 90.83M | High 287.20 — highest price in the visible 9-month window |
| 2026-08-06 | 272.26 | 30.67M | Consolidation floor close |
| 2026-08-10 | 278.09 | 35.73M | Recovery to upper half of range |

Measured facts (all from returned rows):
- From the 2026-07-29 close (226.65) to 2026-08-10 (278.09) = **+22.7% in eight sessions**.
- 2026-07-31 volume of 129.05M is the largest in the visible dataset except 2026-06-26 (248.37M, an index-rebalance-type print).
- The gap is a **true price gap**: 2026-07-30 close 235.50 vs 2026-07-31 open 265.00. Nothing in the 235.50–265.00 band has traded since.
- ATR jumped from 6.89 (2026-07-29) to a peak of 9.98 (2026-08-05), now 9.13 — a **+32% volatility regime change** in one week.

**Implication:** the prior trend (a failing July rally: 254.96 on 2026-07-15 → 226.65 on 2026-07-29, −11.1%) has been invalidated and replaced by a higher, event-anchored range. The stock is now attempting its *second* assault on the 273–287 zone after the April–May attempts failed.

---

## 4. Trend structure — strong, but historically extended

**Selected: `close_10_ema`, `close_50_sma`, `close_200_sma`**

| Measure | Value | Close vs. it |
|---|---|---|
| 10 EMA | 266.03 | **+4.5%** |
| 50 SMA | 247.59 | **+12.3%** |
| 200 SMA | 236.82 | **+17.4%** |
| VWMA | 257.31 | **+8.1%** |

- **Stacking is fully bullish:** close > 10 EMA > 50 SMA > 200 SMA. The 50 SMA sits 10.77 points above the 200 SMA and that spread is widening (50 SMA 246.38 on 2026-07-30 → 247.59 on 2026-08-10; 200 SMA 234.75 → 236.82). The **200 SMA has risen in every session from 232.46 (2026-06-11) to 236.82** — the long-term floor is genuinely ascending, not flat.
- **The 50 SMA just inflected.** It declined every session from 257.10 (2026-06-18) to 246.38 (2026-07-30), then turned up. That is a medium-term trend re-acceleration signal that turns *independent* of the gap print.
- **The 10 EMA is nearly vertical:** 236.29 (2026-07-30) → 266.03 (2026-08-10), +29.7 points in seven sessions. It is now 12.07 points *below* price — a 4.5% cushion, and roughly 1.3 ATR.
- **The stretch is the caution.** Price at +12.3% over the 50 SMA and +17.4% over the 200 SMA, with the 10 EMA–50 SMA spread at 18.44 points (≈7.0% of price), is an extended posture. Historically (within this dataset) such separation has been resolved by *time* (sideways drift) more than by *price* (sharp mean reversion) — but it does mean new longs here carry poor reward-to-risk relative to a pullback entry.

**Read:** trend = up, intact, and volume-confirmed. **Do not short a stacked, rising MA structure.** But buy the pullback, not the extension.

---

## 5. Momentum — positive, decelerating, no divergence yet

**Selected: `macd`, `macdh`, `rsi`**

- **MACD is at its window high:** 8.3729 on 2026-08-10, up monotonically from −3.75 (2026-07-29). The MACD line crossed **above zero on 2026-08-03** (2.74) and the **signal line crossed above zero on 2026-08-04** (0.225) — a full bullish regime confirmation on both.
- **The histogram is the warning.** 4.62 (2026-08-05) → 4.58 → 4.36 → 4.09 → **3.90** (2026-08-10). Four straight declines *while price rose* on 2026-08-10 (+1.31%). This is the mathematical signature of a trend that is still up but **losing acceleration** — the classic consolidation-phase reading. It is not yet a sell signal (histogram remains firmly positive), but it argues against chasing and for a tighter trigger.
- **RSI 65.87** — above 60 (bullish regime) and below 70 (not overheated). The only overbought print in the entire 60-session window was **72.23 on 2026-08-03**. RSI's path 72.23 → 67.04 → 63.49 → 63.20 → 64.21 → **65.87** mirrors price's path 284.02 → 277.42 → 272.65 → 272.26 → 274.48 → 278.09.
- **No confirmed divergence.** Both RSI and price made *lower highs* into 2026-08-06 and both have turned up together — this is a **healthy, non-divergent reset** of an overbought condition. That is the single most constructive momentum detail in this report: the 2026-08-03 overbought condition was worked off by a −4.1% pullback rather than a breakdown, and RSI re-accelerated (64.21 → 65.87) into the recovery.

**Read:** momentum supports continuation; the flattening histogram says continuation requires a **volume-expanded break of 280–287**, not a drift.

---

## 6. Volatility and the volume picture

**Selected: `atr`, `vwma`** (with Bollinger as cross-check from the snapshot)

- **ATR 9.1334 = 3.28% of price.** Down modestly from the 9.98 peak (2026-08-05) — volatility is *cooling* from the gap spike, which is exactly what a digesting consolidation should look like. Practical consequence: a 1-ATR risk band from 278.09 is 268.96; 1.5 ATR is 264.4; 2 ATR is 259.8. **Stops must be at least 1×ATR wide or they will be noise-stopped.**
- **Bollinger cross-check:** mid 253.13, upper 290.69, lower 215.57 → **bandwidth 29.7% of the mid**, an extraordinarily wide envelope caused by the gap. %B = (278.09 − 215.57) / (290.69 − 215.57) = **0.83** — upper third, but *not* at the band. Note the mechanics: price closed **above** the upper band on 2026-08-03 (284.02 vs UB 272.99), then the band expanded faster than price, so price is now 12.6 points *inside* the band. That is the normal signature of a volatility expansion absorbing a breakout, and it removes the "riding the band" upside pressure.
- **VWMA 257.31 is rising steeply** — 240.82 (2026-07-30) → 257.31 (2026-08-10), +16.5 points. Because VWMA is volume-weighted, this confirms the gap was **real accumulation, not a thin squeeze**: buyers' average cost has climbed ~7% in seven sessions. Price at +8.1% above VWMA is a meaningful cushion but also a warning that late buyers are paying ~8% over the volume-weighted crowd.
- **Volume dry-up in consolidation (constructive):** 2026-07-31 129.05M and 2026-08-03 90.83M vs 2026-08-04 69.75M, 08-05 45.12M, 08-06 30.67M, 08-07 33.86M, 08-10 35.73M. The five post-gap sessions average ~43.0M vs ~109.9M for the two breakout sessions — consolidation volume is ~39% of breakout volume. Declining volume on a pullback = **no aggressive distribution**. But 2026-08-10's 35.73M is only ~0.71× my estimated ~50.1M 20-session average — the recovery day was **not** demand-driven. Breakouts on sub-average volume fail more often than they succeed.

**Read:** volatility contraction + volume contraction = a **coiling range**. The resolution direction will be decided by which side breaks *with* volume.

---

## 7. Levels — precise, data-derived

**Resistance**
- **280.14** — 2026-08-10 intraday high (immediate).
- **281.07** — 2026-08-04 intraday high (the post-gap "shoulder").
- **287.20** — 2026-08-03 intraday high; highest print in the visible dataset; the breakout ceiling.
- **290.69** — Bollinger upper band (dynamic; expanding ~3.2 pts/day, so it rises into any breakout).

**Support**
- **273.60** — 2026-08-10 intraday low (first line).
- **270.73** — 2026-08-05 intraday low / consolidation floor; the pivotal short-term level.
- **266.03** — 10 EMA (rising into price).
- **265.00** — 2026-07-31 gap open. This is where the unfilled gap begins.
- **262.01** — 2026-07-31 intraday low. **This is the structural line in the sand**: holding it keeps the gap intact; losing it opens the 235.50–265.00 void.
- **257.31** — VWMA (volume-weighted cost basis of the breakout).
- **253.13** — Bollinger mid / 20-day mean.
- **247.59** — 50 SMA (the trend's last line of defence).

**Range context:** the visible 9-month range runs from a closing low of 198.79 (2026-02-13; intraday 196.00 on 2026-02-17) to the 2026-08-03 high of 287.20. At 278.09 the stock sits at **~89.7% of that range** — top-decile positioning. That is where breakouts are made *or* where failed breakouts become violent.

---

## 8. Actionable scenarios

**A. Bull continuation (primary, ~50% weight).** Trigger: daily close **above 281.07** on volume **≥ 55–60M** (well above the recent ~35M). With MACD histogram re-expanding, targets are **287.20**, then the rising Bollinger upper band (**~290.7 today, climbing**). Invalidation: any close back below **273.60**.
- *Entry discipline:* the extension argues for buying a **240m–48h hold above 280** rather than the touch, or waiting for a retest of **270.7–273.6** with a higher low.

**B. Base / coiling range (also high probability, ~30% weight).** The declining MACD histogram plus sub-average volume says the most likely near-term path is chop between **270.73 and 287.20** while the 10 EMA (266.03) and 50 SMA catch up. This scenario is *supported*, not merely possible: it is the standard resolution of a +22.7%/8-session move with cooling momentum. Tactics: buy 271–273 with a stop under 265, sell 283–287; do not pay up in the middle (278) where you have 5 points to support and 9 to resistance.

**C. Failed breakout / gap risk (~20% weight).** Trigger: close below **270.73**, confirmed by close below **266.03 (10 EMA)**. Then **262.01** (gap-day low) becomes the decision point. A close below 262.01 puts the **235.50–265.00 gap in play** — a ~10% drawdown from here — with the 50 SMA at 247.59 and Bollinger mid at 253.13 inside that void. Watch the 200 SMA (236.82) as the ultimate bear target. **Critically, this scenario needs no bearish divergence to trigger** — it can happen on simple profit-taking after a 22.7% squeeze, which is why the stop location matters more than the thesis.

---

## 9. Risk management and execution notes

- **Position sizing:** use ATR 9.13. A 2-ATR stop from 278.09 is 259.83 and sits just below the 2026-07-31 low (262.01) — a sensible structural stop. Size = (account risk budget) / (2 × ATR ≈ 18.3 points), i.e. roughly **half the share count you would use on a 1-ATR stop**.
- **Volatility-adjusted trimming:** because ATR has fallen from 9.98 → 9.13 while price has risen, the *risk* per share has compressed ~9% — a modest green light for adding on a confirmed breakout, provided volume confirms.
- **What would change my mind fastest:** (1) a MACD histogram cross below zero (from +3.90) — that would imply a momentum regime flip inside a consolidation; (2) a close below the 10 EMA at 266.03; (3) a high-volume down day (>60M) that breaks 270.73.
- **Do not ignore the calendar:** this is a **post-earnings drift environment**. The absence of scheduled catalysts until the next report means price is running on positioning and flow — hence the volume sensitivity. Momentum signals in this state decay faster than in trend-catalyst regimes.
- **Multiple-timeframe consistency:** daily trend up (stacked MAs), daily momentum up but decelerating (MACD high, histogram falling), daily volume neutral/soft (VWMA rising but recent days sub-average). That trio argues for **core long + tactical patience**, not aggressive new exposure at 278.

---

## 10. Selected indicators and rationale

| Indicator | Value (2026-08-10) | Why it was selected for this context |
|---|---|---|
| `close_10_ema` | 266.03 | Fastest gauge of whether the +22.7% thrust is intact; the rising EMA provides the first dynamic trailing stop (266.03). |
| `close_50_sma` | 247.59 | Medium-term trend and the level that just inflected upward (246.38 → 247.59) — independent confirmation the trend turned, not just the gap. |
| `close_200_sma` | 236.82 | Long-term regime filter; rising every session since 2026-06-11, confirming the multi-month base is intact. |
| `macd` | 8.3729 | Confirms momentum regime via the zero-line crossings on 2026-08-03/04 and the highest reading in the window. |
| `macdh` | 3.9044 | Detects *deceleration* — four straight declines (4.62 → 3.90) despite rising price; the key "don't chase" signal. |
| `rsi` | 65.87 | Flags the overbought reset (72.23 → 63.20 → 65.87) and lets us verify there is **no** bearish divergence. |
| `atr` | 9.1334 | Post-gap volatility is 32% above pre-gap; dictates stop distance (1–2 ATR) and position size. |
| `vwma` | 257.31 | Validates that the gap was volume-backed accumulation; its steep rise to 257.31 shows the true cost basis of breakout buyers is 8% below spot. |

*Bollinger bands (mid 253.13 / UB 290.69 / LB 215.57) and MFI (~0.52 scaled) were pulled from the verified snapshot as cross-checks rather than as primary selections, to avoid duplicating the volatility (ATR) and momentum (RSI) roles.*

---

## 11. Key points summary

| Dimension | Reading | Evidence (dated, from tool output) | Implication |
|---|---|---|---|
| **Primary trend** | Strong up | Close 278.09 > 10 EMA 266.03 > 50 SMA 247.59 > 200 SMA 236.82; 200 SMA rose every session 232.46 (06-11) → 236.82 (08-10) | Do not fight the trend; buy pullbacks |
| **Catalyst** | Event-driven repricing | 235.50 (07-30) → 271.58 (07-31), +15.3% on 129.05M shares | Higher platform, but gap-anchored = fragile |
| **Extension** | Stretched | +12.3% vs 50 SMA, +17.4% vs 200 SMA, +8.1% vs VWMA | Poor entry at 278; wait for 271–273 or a confirmed break |
| **Momentum level** | Positive, at highs | MACD 8.37 (window high); MACD >0 since 08-03; signal >0 since 08-04 | Bullish backdrop confirmed |
| **Momentum acceleration** | Cooling | MACD histogram 4.62 (08-05) → 3.90 (08-10), 4th straight decline | Avoid chasing; require volume confirmation |
| **Overbought risk** | Low | RSI 65.87; only overbought print in window was 72.23 (08-03) | Room to run if breakout triggers |
| **Divergence** | None confirmed | RSI 72.23→65.87 mirrors price 284.02→278.09 (both lower highs, both turning up) | Healthy consolidation, not distribution |
| **Volatility** | Elevated, softening | ATR 9.13 (3.3% of price), off 9.98 peak (08-05); Bollinger bandwidth 29.7% | Size positions on 1–2 ATR; stops ≥9 pts |
| **Volume** | Drying up | Post-gap 5-session avg ~43.0M vs 109.9M on 07-31/08-03; 08-10 at 35.73M (~0.71× 20-session avg) | Coiling; breakout needs ≥55–60M to be credible |
| **Volume-weighted cost** | Well below price | VWMA 257.31, up from 240.82 (07-30) | Gap was real accumulation; +8.1% cushion |
| **Range position** | Top decile | 278.09 = ~89.7% of the 198.79 (02-13) → 287.20 (08-03) range | Breakout-or-failure zone; asymmetry matters |
| **Immediate resistance** | 280.14 / 281.07 / 287.20 | 08-10 high / 08-04 high / 08-03 high | Break >281 on volume targets 287.20 → 290.69 |
| **Immediate support** | 273.60 / 270.73 / 266.03 / 265.00 / 262.01 | 08-10 low / 08-05 low / 10 EMA / gap open / 07-31 low | Below 262.01, the 235.50–265.00 gap opens |
| **Bull trigger** | Close > 281.07 on ≥55–60M volume | — | Targets 287.20, then Bollinger UB 290.69 |
| **Bear trigger** | Close < 270.73, confirmed < 266.03 | — | Targets 262.01, then 253.13 / 247.59 |
| **Preferred stance** | Long-biased, patient | Stacked rising MAs + no divergence, offset by extension + soft volume | Accumulate 271–274; trail stop 1.5–2 ATR; trim 283–287 |

**Data-integrity note:** `get_stock_data` and `get_verified_market_snapshot` returned identical OHLCV rows for 2026-08-10 and all overlapping dates — no conflict. The only anomalous value is the MFI returned as `0.51769` (0–1 scale rather than 0–100), which I have flagged rather than reinterpreted; it was not used as a primary signal. The 20-session volume average (~50.1M) and all percentage changes above are arithmetic derived from the returned rows, not additional vendor data.