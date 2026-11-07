# AMZN — Technical & Trend Analysis
**As of the close of 2026-09-04 · Last price $258.51**

---

## 1. Data integrity note

I pulled the full daily series (192 sessions, 2025-12-01 → 2026-09-04) and the verified snapshot for 2026-09-04. The two sources are **fully consistent**: the latest row is O 259.07 / H 261.12 / L 255.29 / C 258.51 / V 30,749,900, and every indicator value returned by `get_indicators` matches the snapshot to the decimal (e.g., 50-SMA 253.9494, RSI 49.5491, MACD 0.3392). **No discrepancy to flag.** All figures below are drawn from those two tool outputs; any percentage I quote is simple arithmetic between two explicitly dated prices.

*(The snapshot also returns an `mfi` of 0.4888 on a 0–1 scale; because the scaling convention is ambiguous and MFI is outside the selected set, I have not used it.)*

---

## 2. Price structure — what actually happened

**The regime is: a completed post-earnings impulse, followed by a controlled six-week retracement that is now trying to stabilize.**

Key anchors from the verified data:

| Date | Event | Price |
|---|---|---|
| 2026-07-29 | Pullback low close (pre-earnings) | 226.65 |
| 2026-07-30 | Volume 101.8M, close 235.50 (event eve) | 235.50 |
| 2026-07-31 | **Gap-up open 265.00** vs prior close 235.50; close 271.58 on 129.1M | 271.58 |
| 2026-08-03 | Impulse peak: intraday high **287.20**, close 284.02 on 90.8M | 284.02 |
| 2026-08-18 | First pullback low close | 259.45 |
| 2026-08-28 | Lower-high rally: high 267.56, close 266.43 on 49.5M — **immediately rejected** | 266.43 |
| 2026-09-01 | Pullback low: intraday **251.93**, close 254.92 | 254.92 |
| 2026-09-04 | Close 258.51; high 261.12 faded into the close | 258.51 |

Three structural facts matter:

1. **The 7/31 gap is still unfilled.** The void runs from 235.50 (7/30 close) to 265.00 (7/31 open). At 258.51 AMZN is sitting *inside* that gap, in its upper half. Nothing about the price action since 8/3 has repaired or negated that gap — it is a large, unresolved structural feature.
2. **Since 8/3, the sequence of highs and lows is descending:** highs 287.20 (8/3) → 278.84 (8/11) → 267.56 (8/28); lows 257.73 (8/18) → 251.93 (9/1). That is a textbook short-term downtrend nested inside a medium-term uptrend.
3. **The retracement has been orderly, not distributive.** Measured from the 8/3 close (284.02) to the 9/4 close (258.51), the decline is **−8.98%**. Measured from the 8/3 intraday high (287.20) to the 9/1 intraday low (251.93), it is **−12.28%**. Against the pre-earnings close of 226.65 (7/29), AMZN is still **+14.06%**. So this is a give-back of part of an impulse, not a trend break.

A useful confluence exercise: the post-gap range 235.50 → 287.20 is 51.70 points. The **50% retracement sits at 261.35** — which lands almost exactly on the 20-day Bollinger basis of **262.20**. The 61.8% retracement is 255.25, and the 9/1 low (251.93) marked a ~68% retracement. In other words, the entire "support/resistance" debate is happening inside a single, well-defined retracement ladder.

---

## 3. Why these eight indicators

This is a **post-impulse consolidation inside a confirmed primary uptrend**, with volatility collapsing. That regime needs (a) multi-horizon trend structure to separate "pullback" from "reversal," (b) a momentum oscillator that isn't already saturated, (c) a band/volatility model to frame the compressed range, and (d) a volume cross-check because the whole move was volume-driven (earnings gaps).

| # | Indicator | Role in this specific setup |
|---|---|---|
| 1 | `close_10_ema` | Detects whether the short-term down-swing has actually stopped; price is currently pinned to it (−0.24%). |
| 2 | `close_50_sma` | Defines the swing-trend line and has *not been closed below* since 7/30 — the cleanest invalidation level. |
| 3 | `close_200_sma` | Confirms the strategic trend and the golden-cross regime; both averages are rising. |
| 4 | `macd` | Measures whether the pullback has eroded the underlying positive momentum (still > 0, but fading fast). |
| 5 | `rsi` | At 49.5 it is genuinely neutral — no overbought/oversold distortion, so it can register the *next* divergence. |
| 6 | `boll` (+`boll_ub`/`boll_lb`) | The ±2σ envelope has compressed violently (29.6% → 8.7% of basis); this is the best available breakout bracket. |
| 7 | `atr` | Volatility has contracted from 9.98 to 6.69 — directly sets stop distance and position size. |
| 8 | `vwma` | The gap move was volume-driven; VWMA tells us whether holders are in profit at current prices. |

I deliberately avoided pairing RSI with a second oscillator, and I did not add a third MACD parameter set — the histogram (macd − macds = −1.179) is fully implied by the MACD pair and adding it would be redundant.

---

## 4. Trend: bullish primary, bearish intermediate, flattening short-term

**Long-term (200-SMA): intact and rising.**
`close_200_sma` = **239.12**, up from 238.68 on 8/28 and 234.75 on 7/30. It has been rising continuously for the entire visible window. Price is **+8.11%** above it — a healthy premium with no extension extreme. The 50-SMA (253.95) sits **14.83 points (+6.2%) above** the 200-SMA, so the golden-cross configuration is intact and the spread is *widening*, not compressing.

**Medium-term (50-SMA): the line in the sand.**
`close_50_sma` = **253.95**, up from 251.66 on 8/28 and 246.38 on 7/30 — a steady, positive slope. Critically: **AMZN has not closed a single session below its 50-SMA since 7/30** (the last sub-50-SMA close was 235.50 on 7/30, before the gap). Even during the 9/1 washout, the close of 254.92 held above the then-50-SMA of 252.41. That is the strongest single piece of evidence that this is a retracement, not a distribution top.

**Short-term (10-EMA): flattening at the scene of the crime.**
`close_10_ema` = **259.14**, down from its 8/12 peak of 267.18, but the *rate* of decline has collapsed: −0.97 on 9/1, −0.08 on 9/2, −0.08 on 9/3, −0.14 on 9/4. The close (258.51) is **0.24% below** it. Flat 10-EMA + price straddling it = the down-move has lost its driving force, but buyers have not yet taken control.

**Interpretation:** the three averages are stacked bullishly (price 258.51 > 50-SMA 253.95 > 200-SMA 239.12), but price is *below* its own 10-EMA. That is the classic signature of a pullback in an uptrend that has bottomed in *time* but not yet in *confirmation*.

---

## 5. Momentum: decay is decelerating

**MACD is the most informative indicator on the board right now.**

- `macd` peaked at **8.432 on 8/11** and has bled to **0.339 on 9/4**.
- `macds` (signal) peaked at **6.217 on 8/14**; it is now **1.519**.
- The bearish crossover occurred when the histogram flipped negative on **8/17** (−0.310).
- The histogram bottomed at **−1.683 on 8/27** and has now improved for three consecutive sessions: −1.585 (9/2) → −1.354 (9/3) → **−1.179 (9/4)**.

Two things follow. First, the **MACD line is still above zero** — a bearish crossover *in positive territory* is, mechanically, a pullback signal rather than a trend-reversal signal. Second, the **histogram is contracting from below**, which is the earliest objective evidence that selling pressure is exhausting. The actionable warning: MACD is only **0.34 above the zero line**. A cross below zero in the coming sessions would materially downgrade the medium-term picture and would likely coincide with a 50-SMA breach.

**RSI is neutral and, importantly, unsullied.**

`rsi` = **49.55**, essentially dead-center. The path is revealing:
- 72.23 on 8/3 (the impulse peak — mildly overbought, never extreme)
- 65.87 on 8/10, 55.64 on 8/19, 55.85 on 8/28 — a clean sequence of **lower RSI highs**, confirming the descending price highs
- 46.33 on 9/1 (pullback low), then 49.90 / 49.55 on 9/3–9/4

I want to be precise here: **there is no confirmed bullish RSI divergence.** The 9/1 price low (251.93) came with an RSI low (46.33) that was *lower* than the 8/27 reading (47.23) alongside a *lower* price — that is confirmation, not divergence. What we have instead is a simple recovery off sub-50. The bullish case would strengthen on an RSI push through **56** (the ceiling of the last two rallies) accompanied by a price close above 262.

---

## 6. Volatility: an extremely compressed spring

This is the most striking feature of the chart.

**Bollinger envelope (±2σ around the 20-SMA):**
- Basis (`boll`): **262.20**
- Upper (`boll_ub`): **273.63**
- Lower (`boll_lb`): **250.76**
- Width: **22.87 points = 8.72% of the basis**

Now compare with 8/19, when the bands were at their widest: UB 296.99, LB 220.47, width **76.53 = 29.6% of basis**. The envelope has compressed to roughly **30% of its August peak width** in twelve sessions. That is a dramatic volatility contraction.

Two mechanical consequences:
1. **The bands are now a genuine bracket.** With the lower band at 250.76 and the 9/1 low at 251.93, there is tight confluence beneath the market. The upper band at 273.63 coincides roughly with the 8/10–8/11 congestion (278 area). A close outside either edge after this degree of compression would be a high-information event.
2. **The lower band is rising fast** (215.57 on 8/10 → 250.76 on 9/4), which is the signature of a basis rolling over while price holds — i.e., the band is coming up to meet the price rather than the price collapsing to meet the band. That is a *constructive* geometry.

**ATR (14):** **6.69**, or **2.59% of the close**. It has fallen from **9.98 on 8/5** and **7.25 on 9/1**. This is a direct, quantified argument for *tighter* stops and *larger* position size than three weeks ago — and it also means that a 1×ATR stop (≈$6.7) is now too tight for a swing thesis given the 8/28–9/1 whipsaw range (high 267.56 → low 251.93 = 15.63 points, or 2.3 ATR).

---

## 7. Volume: the pullback is not being distributed

Raw volume recently versus the August impulse:

| Date | Close | Volume | Read |
|---|---|---|---|
| 2026-08-03 | 284.02 | 90.8M | Peak-price, heavy participation |
| 2026-08-28 | 266.43 | 49.5M | Up-day on rising volume, but rejected at 267.56 |
| 2026-08-31 | 259.77 | 46.1M | Down −2.5%, elevated volume — the day's only real distribution print |
| 2026-09-01 | 254.92 | 31.7M | Down, volume *falling* |
| 2026-09-02 | 254.98 | 24.0M | Lowest volume of the sequence; price held |
| 2026-09-03 | 258.90 | 26.9M | Up on light volume |
| 2026-09-04 | 258.51 | 30.7M | Up on moderate volume, but closed near session low of range |

The pattern is **volume drying up into the low** — 24.0M on 9/2 vs 90.8M on 8/3. That is the behavior of a market where sellers have run out of urgency, not one where institutions are exiting. The blemish is 8/31, and the 9/4 intraday fade (high 261.12 → close 258.51) shows supply still sitting near 261.

**VWMA: 259.78.** Price at 258.51 is **0.49% below** the volume-weighted average — marginally negative, meaning the average dollar of recent volume is a hair underwater. But note the VWMA is falling rapidly (272.05 on 8/20 → 259.78 on 9/4) and is *converging on price*, not diverging above it. Concretely: VWMA (259.78), 10-EMA (259.14), and the 9/3–9/4 closes (258.90, 258.51) are all inside a **1.3-point band**. The market has found a volume-weighted equilibrium in the 258.5–260 zone. That is a coiled, decision-ready condition.

---

## 8. Level map (all values from verified 2026-09-04 data)

**Resistance — layered and close overhead**
- **259.14–259.78** — 10-EMA / VWMA (immediate; price is inside it)
- **260.11–262.20** — 8/20 close, 9/4 high (261.12), **20-SMA/Bollinger basis 262.20**, and the 50% retracement of the post-gap range (261.35). This is the single most important zone on the chart.
- **265.00–267.56** — top of the 7/31 gap (265.00) and the 8/28 rejection high (267.56)
- **273.63** — upper Bollinger band
- **278.00–278.84** — 8/3 open / 8/11 high congestion
- **287.20** — 2026 high (8/3 intraday)

**Support — three tiers**
- **253.95** — 50-SMA (never closed below since 7/30). First warning line.
- **250.76–251.93** — lower Bollinger band + 9/1 low. This is the structural floor of the post-earnings consolidation.
- **245.2–246.0** — June congestion (6/15 close 246.02, 6/16 close 246.00, 6/9 close 244.19)
- **239.12** — 200-SMA

---

## 9. Actionable plan

**Bias: neutral-to-constructive. The primary trend is up, the pullback is mature, but confirmation has not yet printed.** The current price sits mid-range between 250.76 and 273.63, which is the worst risk/reward location on the chart. Do not chase here.

### Scenario A — Bullish confirmation (base case, ~55% weight)
**Trigger:** a daily close **above 262.20** (20-SMA) with volume ≥ 40M, ideally with RSI > 56 and MACD histogram crossing back above zero.
- Entry: 262.50–263.50
- Stop: **251.00** (below the 9/1 low of 251.93 and the lower band of 250.76) = ~11 points ≈ 1.6× ATR
- Target 1: **266.50–267.56** (8/28 high) — partial exit
- Target 2: **273.63** (upper band) — R:R ≈ 1.0 from entry 262.50
- Target 3: **287.20** (2026 high) — R:R ≈ 2.2
- Note: T1 is close, so scale rather than take the whole position off; the asymmetric payoff is in T3.

### Scenario B — Range / coil resolution (needs patience)
If price continues to oscillate between **250.76 and 267.56**, the correct posture is to trade the edges, not the middle:
- Long at **252–254** (lower band + 9/1 low + just above the 50-SMA), stop **249.50** (below the band, ~2.4 points ≈ 0.4 ATR — too tight; use **248.00**, ≈1× ATR below entry), target 261.50–262.20.
- Short/trim at **266–267.50**, stop **270.50** (above the 8/28 high plus ~1 ATR), target 259–260. This is a counter-trend trade and should be sized smaller.

### Scenario C — Bearish invalidation (~20% weight)
**Triggers, in order of severity:**
1. Daily close **below 253.95** (50-SMA) — first crack; reduce long exposure.
2. Daily close **below 250.76** (lower Bollinger band) — post-earnings structure broken; next objectives 245–246, then 239.12 (200-SMA).
3. **MACD crossing below zero** (currently only 0.34 above it) — would likely front-run #1 and is the fastest early warning.

### Risk management
- ATR is **6.69 (2.59%)** and falling. A 1.5–2.0× ATR stop is now 10–13.4 points. Set position size so that a full stop-out costs ≤1% of equity: at an 11-point stop, that is roughly 0.09% of equity per share of notional — i.e., size on *risk*, not on dollar value.
- Avoid holding size into the next earnings event: the historical evidence in this dataset is that AMZN's earnings gaps are violent and immediate (2/4 close 232.99 → 2/6 close 210.32 across two sessions on 179.2M volume; and 7/30 close 235.50 → 7/31 close 271.58). Indicator-based stops do **not** protect across a gap.
- Because Bollinger width has compressed to 8.72% of basis, expect a **volatility expansion** — direction unknown. Consider a bracket approach (break of 262.20 or 250.76) rather than a directional guess.

---

## 10. What would change my mind

| Observation | Current reading | Would flip the view |
|---|---|---|
| 50-SMA slope | Rising (+2.29 over the last 5 sessions) | Flat or turning down |
| Close vs 50-SMA | +1.80% above | A close below 253.95 |
| MACD vs zero | +0.339, above zero | A cross below 0.00 |
| MACD histogram | −1.179 and improving 3 sessions | A new low below −1.68 |
| RSI | 49.5, recovering off 46.3 | A break below 40, or a failure at 56 |
| VWMA vs close | −0.49% (marginal) | VWMA diverging decisively above price |
| Pullback volume | Contracting (24.0M on 9/2) | Expansion >50M on down days |

---

## 11. Summary table — key points

| Dimension | Reading (2026-09-04) | Interpretation | Actionable level |
|---|---|---|---|
| **Price** | 258.51 (O 259.07 / H 261.12 / L 255.29) | Inside the unfilled 7/31 gap (235.50–265.00) | — |
| **Primary trend** | 200-SMA 239.12, rising; price +8.11% above | Intact, healthy premium | Golden cross intact (50 > 200 by 14.83) |
| **Swing trend** | 50-SMA 253.95, rising; price +1.80% above | Uptrend; no close below since 7/30 | **253.95 = invalidation** |
| **Short-term** | 10-EMA 259.14, flattening; price −0.24% | Down-move stalling, no confirmation yet | Reclaim 259.14 → 262.20 |
| **Momentum** | MACD 0.339 / signal 1.519 / hist −1.179 | Bullish-regime pullback; decay slowing | Hist > 0 and MACD > 0 |
| **RSI** | 49.55 (lower highs: 72.2 → 65.9 → 55.6 → 55.9) | Neutral, no divergence, room both ways | 56 = confirmation; 40 = breakdown |
| **Volatility (bands)** | 20-SMA 262.20; UB 273.63; LB 250.76; width 8.72% | Extreme compression (was 29.6% on 8/19) | Bracket 250.76 / 273.63 |
| **Volatility (ATR)** | 6.69 = 2.59% of price (peak 9.98 on 8/5) | Contracting; tighter stops justified | Stop 1.5–2.0× ATR = 10–13.4 pts |
| **Volume** | 30.7M on 9/4; 24.0M low on 9/2 | Drying up into the low = constructive | Down-day volume >50M = bearish |
| **VWMA** | 259.78; price −0.49% below | Marginal; equilibrium forming 258.5–260 | Above 259.78 = buyers back in control |
| **Structure** | Lower highs 287.20 → 278.84 → 267.56; lower low 257.73 → 251.93 | Short-term downtrend in a medium-term uptrend | Break of 267.56 ends it |
| **Drawdown context** | −8.98% from 8/3 close (284.02); +14.06% vs 7/29 close (226.65) | Correction within impulse, not reversal | — |
| **Bias** | **Neutral-to-constructive** | Wait for 262.20 reclaim; buy 252–254 with 248 stop | R:R improves materially outside 250.8–267.6 |

---

## 12. Indicator reference table

| Indicator (tool name) | Value 2026-09-04 | 20-session context | Signal |
|---|---|---|---|
| `close_10_ema` | 259.137 | 267.183 (8/12 peak) → flat last 4 sessions | Neutral (price pinned) |
| `close_50_sma` | 253.949 | 246.384 (7/30) → rising | Bullish |
| `close_200_sma` | 239.123 | 234.755 (7/30) → rising | Bullish |
| `macd` | 0.339 | 8.432 (8/11) → declining, still >0 | Weakening / pullback |
| `macds` | 1.519 | 6.217 (8/14) → declining | Bearish crossover intact |
| `macdh` *(derived)* | −1.179 | Low −1.683 (8/27) → improving 3 sessions | Early bullish turn |
| `rsi` | 49.549 | 72.232 (8/3) → 46.327 (9/1) → 49.55 | Neutral |
| `boll` | 262.197 | 243.858 (7/31) → rising then rolling | Resistance overhead |
| `boll_ub` | 273.630 | 296.993 (8/19) → collapsing | Bracket high |
| `boll_lb` | 250.764 | 215.569 (8/10) → rising fast | Bracket low / support |
| `atr` | 6.692 | 9.983 (8/5) → contracting | Lower volatility, tighter stops |
| `vwma` | 259.777 | 272.053 (8/20) → falling to price | Marginal negative |

**Bottom line for AMZN:** the primary uptrend is intact and the 50-SMA has held on a closing basis through the entire post-earnings retracement, while volume dries up and MACD's downside momentum fades. But price is coiling in a 1.3-point knot around 258.5–260 with the 20-SMA, VWMA, and 50%-gap-retracement all stacked at 261–262 overhead. The trade is to let the market choose: **a close above 262.20 with volume opens 267.56 → 273.63 → 287.20; a close below 250.76 flips the structure toward 245 and then the 200-SMA at 239.12.** Between those levels, the risk/reward is poor and patience is the position.