# AAPL — Multi-Timeframe Technical Review
**Analysis date:** 2026-09-28 · **Last verified close:** $338.40

---

## 1. Data integrity note

The `get_stock_data` pull and the verified snapshot agree **exactly** on the latest session: 2026-09-28 open 340.37 / high 342.99 / low 338.04 / **close 338.40** / volume 32,820,800. No conflict to reconcile.

One housekeeping point: `technical_total_return_index` = 344.41 versus the cash close of 338.40. That gap reflects cumulative dividend reinvestment (ex-dividend $0.27 on 2026-05-11 and again on 2026-08-10), **not** a price discrepancy. All price levels below are cash prices.

**Indicators selected (8):** `close_50_sma`, `close_200_sma`, `macd`, `rsi`, `boll_ub`, `boll_lb`, `atr`, `vwma`. These cover trend (fast/slow structure), momentum (rate of change + oscillator), volatility/mean-reversion (bands + true range), and participation (volume-weighted price), with minimal overlap. The snapshot additionally supplies the 10-EMA (335.96), Bollinger mid-line (330.33) and MACD signal (5.54) as cross-checks.

---

## 2. Executive summary

AAPL is in a **confirmed, maturing primary uptrend** that has just repaired the single largest technical damage of the year (the 2026-07-31 earnings-type gap). Price sits ~0.8% below the highest close in the visible seven-month window and ~2.5% below the upper Bollinger band, with every major moving average stacked bullishly beneath it.

The nuance: **momentum is decelerating as price makes new highs, volume is thinning, and the stock is stretched 17.5% above its 200-day average.** This is a "hold core, buy pullbacks, do not chase" tape rather than a fresh breakout entry.

| Regime | Reading | Interpretation |
|---|---|---|
| Primary (200-day) | Price 338.40 vs 288.07 = **+17.5%** | Strong bull, but extended |
| Intermediate (50-day) | Price 338.40 vs 321.93 = **+5.1%** | Bullish; 50 > 200 by 11.8% |
| Short-term (10-EMA) | 338.40 vs 335.96 = **+0.7%** | Intact but testing |
| Momentum | RSI 61.8, MACD 6.08 > signal 5.54 | Positive, cooling |
| Volatility | ATR 6.83 (**2.0%** of price), band width 10.0% | Normal, post-squeeze |
| Participation | Price 338.40 vs VWMA 332.07 = **+1.9%** | Buyers in control |

---

## 3. Trend structure: a textbook bullish stack, with one caveat

**Long-term.** The 200-day SMA has risen every single session since at least 2026-06-01 (263.60 → 288.07, +9.3%) and the close is 17.5% above it. That is unambiguous evidence of a durable uptrend — and simultaneously the most important risk in this report. Historically, extensions of this magnitude in a mega-cap tend to be resolved by *time* (sideways consolidation) or *price* (a 5–8% mean-reversion flush back toward the 50-day), not by immediate acceleration.

**Intermediate.** The 50-day SMA (321.93) is above the 200-day (288.07) by $33.85, or **11.8%** — a wide, mature spread that confirms the golden-cross regime is long established rather than nascent. Critically, the 50-day is still *rising*: 315.80 on 2026-09-08 → 321.93 on 2026-09-28 (+1.9%), though the slope is flattening (it added only 0.68% between 2026-09-17 and 2026-09-28). A flattening 50-day under a rising price is the classic signature of a trend transitioning from "impulse" to "grind."

**Short-term.** The 10-EMA at 335.96 has contained the September advance; the lowest close since 2026-09-10 is 316.22 (09-08) and, more relevantly, the 2026-09-24 low of 334.30 held *above* the 10-EMA. Price is now sitting right on top of it.

**The structural story that matters most:** the 2026-07-31 session gapped down from a 333.44 close to a 310.69 high (−7.4% on 132.5M shares — the second-largest volume print of the year). That left a wide supply shelf between ~310 and ~333. **AAPL did not close above 333.44 again until 2026-09-17 (337.00)** — 33 sessions later — and has since closed as high as 341.07. That is a completed, validated recovery of the entire event shock, and it is the strongest single piece of bullish evidence in this dataset.

---

## 4. Momentum: positive, but leaking at the margin

- **MACD line: 6.079**, above the **signal at 5.542**, histogram **+0.537**. The line has been positive since 2026-08-31 (0.297) after a deep negative stretch (−2.68 on 2026-08-17). That is a genuine regime flip from correction to advance.
- However, the MACD line **peaked at 6.25 on 2026-09-22** and has since printed 6.21 → 6.02 → 6.21 → 6.08 while price made a marginally higher closing high on 2026-09-25 (341.07). The histogram is compressing. This is early-stage *momentum fatigue*, not a sell signal — the crossover is still bullish and the histogram is still positive.
- **The bigger divergence:** MACD reached **9.61 on 2026-07-29** when price closed at 338.19. Today price is $3.30 higher (341.07 peak close) but MACD is 37% lower. **Price higher high, MACD materially lower high.** Same pattern in RSI: **71.65 on 2026-07-17** at a 333.74 close versus **66.88 on 2026-09-22** at a 339.75 close (and 65.67 on the 341.07 close of 09-25).

**How to weight this:** in strong trends these divergences are common and often resolve upward after consolidation. But they do argue against paying up for breakout entries. Two independent momentum measures confirming the same deceleration is not noise.

- **RSI 61.79** is in the bullish-control zone (50–70) and — importantly — is **not overbought**. The stock has room to run before RSI becomes a constraint. The oscillator range all September has been 49.3 (09-09) to 66.9 (09-22): a healthy churn band, neither euphoric nor broken.

---

## 5. Volatility and Bollinger Bands: the squeeze already resolved upward

This is the most actionable structural observation in the data.

| Date | Lower | Mid | Upper | Width % of mid |
|---|---|---|---|---|
| 2026-08-12 | 295.18 | 321.22 | 347.26 | **16.2%** |
| 2026-08-27 | 301.61 | 309.33 | 317.04 | **5.0%** ← squeeze low |
| 2026-09-28 | 313.77 | 330.33 | 346.89 | **10.0%** |

Bollinger width compressed from 16.2% (post-crash) to **5.0% on 2026-08-27**, then expanded to 10.0% today **while price rose from ~309 to ~338**. That is a textbook squeeze-breakout resolution to the upside — the low-volatility coil has already fired. ATR corroborates: 9.87 on 2026-08-03 → 7.23 on 2026-08-25 → 6.83 today, i.e., realized volatility halved, then re-expanded modestly as price advanced.

**Where price sits inside the envelope:** `%B = (338.40 − 313.77) / (346.89 − 313.77) = 0.74`. Price is in the upper quartile of the band but has **not tagged the upper band** at any point in the visible window. This matters: the rally is *not* a blow-off band-walk. There is a clean +2.5% of runway to 346.89 before mean-reversion pressure builds, and the mid-line at 330.33 is the band's gravitational center on any pullback.

**ATR-based risk budget:** ATR = $6.83 (2.02% of price).
- 1 ATR below close = 331.57 (essentially the Bollinger mid)
- 1.5 ATR = 328.16
- 2 ATR = 324.74
- 2.25 ATR ≈ 323.03 — sits almost exactly on the rising 50-day SMA (321.93), making a "stop under the 50-day" and a "2.25-ATR stop" functionally the same trade.

---

## 6. Volume and participation: constructive, but thinning

**VWMA is the cleanest bullish confirmation on the chart.** It has risen in nine of the past ten weeks: 309.19 (2026-08-25) → 317.99 (09-10) → 326.37 (09-18) → **332.07 today**. Price at 338.40 sits **1.9% above** the volume-weighted average price of the recent tape. Translation: the marginal buyer is in profit, and the average dollar transacted is chasing higher. When VWMA leads price up like this, dips tend to get absorbed.

**But the tape is getting quieter at the highs.** Average volume of the last ten sessions (09-15 → 09-28) is ~38.8M versus ~45.7M for the prior ten (09-01 → 09-14). The rally's final leg is occurring on roughly **15% less volume**. Note also that 2026-09-18's 86.6M print is a quarterly-expiry/rebalance artifact, not directional conviction — strip it out and the volume decay is more pronounced.

**Event-day map (for context on latent supply):**
- 2026-06-25: −6.1% to 275.15 on 107.0M
- 2026-06-26: +3.1% to 283.78 on **261.8M** (largest print in the sample) — capitulation-and-reclaim
- 2026-07-31: −7.4% to 308.91 on 132.5M — the gap that has now been fully repaired
- 2026-09-10: +3.6% to 326.57 on 70.0M — the volume-backed launch of the current leg

The pattern is telling: shocks are being bought aggressively and repaired within weeks. That is characteristic of a bull market absorbing bad news, not a distribution top.

---

## 7. Key levels (all derived from tool output)

**Resistance**
| Level | Source | Significance |
|---|---|---|
| 345.34 | 2026-09-22 high | **Highest high in the visible window** (just above 344.57 from 2026-07-29) — the pivot |
| 342.99 | 2026-09-28 high | Immediate intraday cap; rejected here today |
| 341.07 | 2026-09-25 close | Highest close in the window — the line that must hold to keep the breakout narrative alive |
| 346.89 | Bollinger upper | +2.5%; first statistical target |

**Support**
| Level | Source | Significance |
|---|---|---|
| 338.04 | 2026-09-28 low | Immediate floor |
| 335.96 | 10-EMA (snapshot) | Short-term trend line; held on 09-24 |
| 334.30 | 2026-09-24 low | Swing low of the current consolidation |
| 330.33 | Bollinger mid / 20-SMA | **The line that separates "upper-half regime" from "mean reversion"** |
| 328.21 | 2026-09-03 close | Prior breakout shelf |
| 321.93 | 50-day SMA | Trend-defining support; −4.9% |
| 313.77 | Bollinger lower | −7.3%; outer risk envelope |
| 309.90 | 2026-09-09 low | The higher-low that launched this leg; thesis-invalidating on a close basis |

Note the support ladder is unusually **compressed**: 10-EMA at 335.96, swing low 334.30, and Bollinger mid 330.33 all sit within a 1.7% band. That clustering means a decisive break of 330.3 would likely slice through all three at once — there is little "air pocket" cushioning below.

---

## 8. Actionable trade frameworks

### A. Core trend position (preferred posture: hold / partial add on weakness)
The primary trend is intact and the 200-day slope is positive. Remain long. **Add on pullbacks into 330–336** (Bollinger mid → 10-EMA zone) rather than at current levels.
- Entry zone: **331.00 – 335.50**
- Stop: **326.50** (below 1.5-ATR 328.16 and below the 09-03 shelf) → risk ~$6-9 from entry
- Target 1: **345.30** (window high), Target 2: **352.20** (1 ATR extension above 345.34)
- R:R at a 335.00 entry with a 326.50 stop: ~1.2:1 to T1, ~2.0:1 to T2

### B. Breakout continuation (requires confirmation — do not anticipate)
Only valid on a **close above 345.34 with volume ≥ 45M** (above the 10-day average, which is currently ~38.8M).
- Entry: 345.50–346.50 on confirmation
- Stop: **338.60** (1 ATR) — a tight leash is warranted precisely *because* MACD/RSI are diverging
- Target: **352.20** (1 ATR extension). Note the R:R here is only ~1:1, which is why this is the *secondary* plan, not the primary one. Chasing a low-volume, momentum-diverging breakout into a 17.5%-extended 200-day spread is poor expectancy.

### C. Mean-reversion / reduce scenario (invalidation)
- **Close below 330.33 (Bollinger mid)** = the upper-half regime has ended; trim and stop adding.
- **Close below 321.93 (50-day)** = intermediate trend damage; stand aside.
- **Close below 309.90** = the September higher-low sequence is broken; the July-recovery thesis is void.
- **Upside invalidation of the bear case:** a close above 345.34 with expanding MACD histogram re-opens 352–359 (2 ATR above the pivot).

### D. Position sizing
With ATR at 2.02% of price, a 2-ATR stop is a 4.0% price risk. Size so that a full stop-out costs no more than your standard per-trade risk (e.g., a 1% portfolio risk implies ~25% notional exposure), and note that the compressed support cluster in §7 means slippage through 330 is a realistic execution risk — use limit orders into support, not stops.

---

## 9. What would change this view

**More bullish:** a volume-confirmed close above 345.34 with MACD histogram re-expanding; or a shallow, low-volume pullback to 331–336 that holds the Bollinger mid and then resumes. Either would reset the momentum divergence and validate 352+.

**More bearish:** (i) a second rejection at 345 and a close under 334.30, which would create a lower high against 2026-07-29's 344.57 and form a double-top structure; (ii) MACD rolling through its signal (currently a $0.54 cushion); (iii) RSI breaking below 50, which last happened 2026-09-09 at 49.35 — three sessions before the +7.3% leg, so a sub-50 RSI here would be a materially different signal than it was then.

---

## 10. Summary table

| Dimension | Evidence (verified) | Read | Actionable implication |
|---|---|---|---|
| **Primary trend** | Close 338.40 vs 200-SMA 288.07 (**+17.5%**), 200-SMA rising all period (263.60→288.07) | Strong bull, **extended** | Hold core; expect time-based consolidation |
| **Intermediate trend** | 50-SMA 321.93, price **+5.1%**; 50 vs 200 spread **+11.8%**, 50-SMA still rising but slope flattening | Bull, maturing | Buy dips toward 50-SMA region, not breakouts |
| **Short-term** | 10-EMA 335.96; 09-24 low 334.30 held above it; close +0.7% over 10-EMA | Intact, being tested | 1st line of defense at 334.3–336.0 |
| **Momentum** | MACD 6.08 > signal 5.54 (hist +0.54), but MACD peaked 6.25 on 09-22; RSI 61.8 vs 66.9 on 09-22 | Positive but **decelerating** | Do not chase; tighten risk on new highs |
| **Divergence** | Price high 341.07 (09-25) vs MACD 6.08; July: price 338.19 close w/ MACD 9.61. RSI 71.7 (07-17) → 65.7 (09-25) | Bearish momentum divergence | Argues for pullback entry over breakout chase |
| **Volatility** | ATR 6.83 (**2.02%**), down from 9.87 (08-03); band width 16.2% → **5.0%** (08-27) → **10.0%** | Squeeze **already resolved upward** | Trend continuation favored; vol re-expanding |
| **Band position** | %B = **0.74**; upper 346.89 (+2.5%), mid 330.33, lower 313.77 (−7.3%) | Upper quartile, **not** overbought | Runway to 346.9; mid-band is the line in the sand |
| **Participation** | Close +1.9% vs VWMA 332.07; VWMA rising 9 of 10 weeks | Buyers in control | Bullish confirmation |
| **Volume quality** | Last 10 sessions ~38.8M vs prior 10 ~45.7M (−15%); 09-18's 86.6M is expiry noise | **Thinning at highs** | Demand breakout volume ≥45M before trusting it |
| **Structural repair** | 07-31 gap (333.44 → 310.69 high); first close back above 333.44 on **09-17 (337.00)** | Gap fully recovered — **major bullish validation** | Underpins the core long thesis |
| **Resistance** | 345.34 (09-22, window high), 342.99 (09-28 high), 341.07 (record close), 346.89 (upper band) | Triple-decker supply 341–346 | Needs volume + MACD re-expansion to clear |
| **Support** | 338.04 → 335.96 (10-EMA) → 334.30 → **330.33 (Boll mid)** → 328.21 → **321.93 (50-SMA)** → 313.77 | Compressed cluster 330–336 | Break of 330.3 breaks three supports at once |
| **Invalidation** | Close <330.33 = trim; <321.93 = neutral; <309.90 = thesis void | Clear, objective stops | 2–2.25 ATR aligns with the 50-SMA stop |
| **Verdict** | Bull trend + squeeze-breakout + VWMA confirmation, offset by momentum divergence and thinning volume | **Constructive, not aggressive** | Hold core; add 331–336; breakout only on >45M volume above 345.34 |