# AMZN — Multi-Timeframe Technical & Tactical Report
**As of close 2026-09-22 | Last price: $254.98**

---

## 0. Data Integrity Check

I first compared the raw OHLCV pull (`get_stock_data`, 203 sessions from 2025-12-01) against the deterministic verification snapshot. **The two sources agree exactly** on the 2026-09-22 row and on all indicator values below — no reconciliation is required. All levels in this report are drawn from those two outputs only.

### Verified baseline (source of truth)

| Metric | Value | Price vs. level |
|---|---|---|
| Close / Open / High / Low | 254.98 / 255.11 / 259.00 / 253.78 | — |
| Volume | 41,982,600 | ~24% above 20-day avg (~33.9M) |
| 10 EMA | 254.1097 | Price +0.34% |
| 50 SMA | 256.2554 | Price **−0.50%** |
| 200 SMA | 240.5339 | Price **+6.01%** |
| Bollinger mid (20 SMA) | 255.7700 | Price −0.31% |
| Bollinger upper / lower | 265.1056 / 246.4344 | −3.82% / +3.47% |
| MACD / Signal / Histogram | −1.3670 / −1.3102 / **−0.0568** | Below zero, hist. ≈ flat |
| RSI(14) | 49.22 | Neutral |
| ATR(14) | 5.9680 | 2.34% of price |
| VWMA | 253.9158 | Price +0.42% |
| 50 SMA − 200 SMA spread | +15.72 (+6.54%) | Bullish structure intact |

---

## 1. Regime Diagnosis: A Bull Trend in an Orderly, Compressing Correction

AMZN is **not** in a downtrend — it is in the *third month of a corrective consolidation inside a well-established primary uptrend*. The evidence is structural, not anecdotal:

- **Primary trend up:** Price is 6.0% above a still-rising 200 SMA, and the 50/200 spread has *widened* from +10.39 on 2026-08-13 to +15.72 on 2026-09-22. The long-term moving-average engine is still accelerating even while price chops.
- **Intermediate trend stalled:** The 50 SMA's daily rate of change has decayed sharply — +6.84 points over the 20 sessions to 09-08 versus only +1.83 points over the 10 sessions to 09-22. The medium-term slope is flattening toward horizontal.
- **Short-term trend turning up:** The 10 EMA bottomed at 252.73 (09-17) and has risen for three consecutive sessions to 254.11.

**The cycle in numbers (all tool-derived):** the rally ran from the 2026-02-17 low of 196.00 to the 2026-08-03 intraday high of 287.20 (+46.5%). From the 08-03 closing high of 284.02, AMZN fell to 244.30 on 09-16 — a **−13.98% drawdown** — then bounced +5.79% to 258.45 on 09-21 before giving back 1.34% today. Price now sits **10.22% below the 08-03 closing peak** and **+4.37% above the 09-16 low**.

Critically, **the character of this decline is bullish-repair, not distribution:** ATR has contracted from 8.54 (08-13) to 5.97 (−30%) while price fell. Corrections that occur on contracting volatility and without a volume climax typically resolve higher once the moving-average structure catches up.

**However — the failed breakout is a genuine warning.** The 08-03 spike to 287.20/284.02 marginally exceeded the May high of 278.56 but could not hold above it, and price has since re-entered the 244–278 range. That makes **265–278 a supply zone**, not open air. (See §5.)

---

## 2. Why These Eight Indicators (Selection Rationale)

The context demands four distinct information types: (a) trend *structure*, (b) momentum *inflection timing*, (c) mean-reversion *positioning*, and (d) volatility/volume *confirmation*. I selected exactly one or two from each bucket to avoid redundancy:

| Indicator | Role in this specific setup |
|---|---|
| `close_50_sma` | The **battleground level**. Price is 0.50% below it; it is also converging *down* toward price. The single most important pivot. |
| `close_200_sma` | Confirms the primary uptrend and marks the deep-support confluence (~240.5) with the Jul-31 earnings gap boundary. |
| `close_10_ema` | Captures the 3-session momentum turn (252.73 → 254.11) and gives a tight invalidation for short-term longs. |
| `macd` | Establishes that intermediate momentum is still **net negative** (−1.37), preventing premature bullish enthusiasm. |
| `macdh` | The highest-value signal today: histogram compression from −1.54 to −0.06 in four sessions is the *timing* tell for an imminent bullish crossover. |
| `rsi` | Independent momentum gauge showing the 09-16 low was never oversold (39.45) — an orderly pullback — and is now neutral at 49.2. |
| `atr` | Sizes stops and flags the volatility contraction that precedes expansion. |
| `vwma` | Confirms whether the bounce has volume-weighted backing (price is only +0.42% above it — a fragile edge). |

*Supplementary (from the verified snapshot, not part of the core eight): Bollinger bands, used purely for envelope levels — upper 265.11, lower 246.43, bandwidth 7.30%.*

I deliberately excluded `macds` (its information is fully captured by `macd` + `macdh`), `boll_ub`/`boll_lb` (snapshot already supplies them), and any oscillator duplicate of RSI.

---

## 3. Trend Read: A Textbook Moving-Average Coil

The defining feature of the current tape is a **four-way moving-average convergence inside 0.9%**:

- 50 SMA: **256.26**
- Bollinger mid / 20 SMA: **255.77**
- 10 EMA: **254.11**
- Close: **254.98**

Price is threaded *through* this cluster rather than above or below it. That is a coiled-spring configuration, and it is corroborated by volatility: ATR at 5.97 is the lowest reading in the entire 08-13→09-22 window (versus 8.54 six weeks ago), and the Bollinger envelope is only 7.30% wide.

**The nuance most traders will miss:** the 50 SMA does not need price to fall to meet it. The July observations rolling out of the 50-day window (07-14 at 247.49, 07-17 at 247.23, 07-20 at 249.99, 07-28 at 230.86) are being replaced by ~255 prints. As long as AMZN holds roughly ≥250, **the 50 SMA will continue rising toward price at ~0.10–0.15/day**. A "reclaim" of the 50 SMA may therefore occur *passively* within 1–2 weeks — which is constructive, but also means a close above 256 in isolation is a weak signal. It must be paired with momentum confirmation.

Volume structure supports the "orderly" read: the entire Aug–Sep decline occurred on routine volume (30–45M), with **no capitulation print** at the 09-16 low (33.5M, below the 20-day average). The absence of a selling climax means the 244.30 low is *unconfirmed* as a final low — a retest cannot be ruled out.

---

## 4. Momentum Read: Downside Momentum Is Exhausted, but Not Yet Reversed

This is the most actionable part of the analysis, and it is a story of **near-completion, not completion**.

- **MACD line:** −2.286 (09-17) → −1.540 (09-21) → **−1.367 (09-22)**. A clear upward hook.
- **MACD histogram:** −1.539 (09-16) → −0.859 (09-18) → −0.245 (09-21) → **−0.057 (09-22)**. That is a **96% contraction in four sessions**.
- **Status:** MACD (−1.3670) remains *below* signal (−1.3102). **No crossover has occurred yet.** One to two more flat-to-up sessions at ~255–257 would mechanically trigger it.

Interpretation: the *second derivative* has turned positive (selling pressure decelerating) while the *first derivative* is still negative (the trend is still down on this timeframe). That is the classic "bottoming, not yet broken out" configuration. Buying the crossover itself is late; buying the histogram compression — with a defined stop — is the higher-expectancy version.

**RSI at 49.22** confirms neutrality with two useful details: (1) the 09-16 trough was only 39.45, so this correction never reached oversold — consistent with a bull-market pullback rather than a top; and (2) the RSI rebounded to 52.69 on 09-21 and has already slipped back to 49.22, i.e., the bounce is losing momentum, not accelerating.

**The bearish tell on today's candle:** AMZN opened 255.11, traded up to 259.00, and closed at 254.98 — near the session low (−1.34% d/d) on 41.98M shares. Combined with 09-21's high of 259.49, this is **two consecutive rejections from the 259 area**. That level is now a confirmed short-term ceiling on a closing basis.

**Volume/money flow:** price at 254.98 is only 0.42% above VWMA (253.92). The VWMA is still declining (272.05 on 08-20 → 253.92 now) but has flattened dramatically — a 1.7-point drop over the last four sessions versus 10+ points in the prior two weeks. The average volume-weighted buyer is barely in profit: **the bounce has not yet been validated by volume.** The snapshot's money-flow proxy (0.503) reads neutral.

---

## 5. Level Map (every level traceable to tool output)

**Resistance ladder**
| Level | Source |
|---|---|
| 259.00–259.50 | 09-21 high 259.49, 09-22 high 259.00, 09-03 high 259.50 |
| 261.12 | 09-04 high |
| **265.11** | Bollinger upper band |
| 266.40 / 267.56 | 08-19 high / 08-28 high |
| 272.65–273.90 | 08-05 close / 04-30 high |
| 278.56 / 284.02 / 287.20 | 05-05 high / 08-03 close / 08-03 high |

**Support ladder**
| Level | Source |
|---|---|
| 253.92 | VWMA (immediate) |
| 251.88–252.40 | 09-18 low 251.88, 09-01 low 251.93, 09-09 close 252.40 |
| 249.24–249.58 | 09-17 low / 09-10 low |
| 247.22 | 09-15 low |
| **246.43** | Bollinger lower band |
| **244.30** | 09-16 low (cycle low) |
| **239.82–240.53** | 07-30 high (earnings-gap boundary) + 200 SMA — the major confluence floor |

Note the **gap geometry**: the 07-31 earnings gap runs from 239.82 (07-30 high) to 265.00 (07-31 open). Price has retraced into but not filled it. A full gap-fill would mean a test of ~240 — precisely where the 200 SMA sits. That is the line in the sand for the primary uptrend.

---

## 6. Scenario Map

**A. Base case — Range resolution higher (≈45%):** The 50 SMA converges down to price, the MACD crosses positive within 1–3 sessions, and AMZN clears 259.50 → 265.10 → 267.56. Requires a daily close >259.50 on volume ≥40M. *Note the R:R problem: chasing the breakout with a 1.5-ATR stop (≈251) risks ~8.5 points to make ~5.6 to the upper band. Poor. Buy the retest, not the print.*

**B. Base case — Continued coil / retest of 246–250 (≈35%):** The 259 rejections hold, price revisits the 249–252 shelf, RSI resets into the low 40s, and the setup improves. This is the *desirable* path for new longs.

**C. Bear case — Break of 244.30 (≈20%):** A close below 244.30 invalidates the higher-low structure and opens 240.53 (200 SMA) / 239.82 (gap boundary). A close below 239.82 would kill the primary uptrend thesis and target the July consolidation at 226.65.

---

## 7. Actionable Trade Plans

**Plan 1 — Preferred: Buy the 249.50–252.00 shelf (limit orders, not market).**
- Entry: 250.50 (mid-shelf; aligns with 09-10/09-17 lows and just above the 246.43 lower band)
- Stop: **246.80** (below the 09-15 low of 247.22) → risk ≈ 3.70 (0.62 ATR)
- Targets: T1 **258.50** (+8.00, 2.2:1) · T2 **265.10** (+14.60, 3.9:1)
- Rationale: buys support with the primary trend, avoids the rejection zone, and keeps risk inside one ATR.

**Plan 2 — Momentum confirmation: buy the *retest* of a 259.50 breakout.**
- Trigger: daily close >259.50 with volume >40M **and** MACD > signal
- Entry: first pullback into 256.00–257.00 (reclaimed 50 SMA)
- Stop: **251.90** (below 09-18 low) → risk ≈ 4.5
- Targets: 265.10 (1.9:1) · 267.56 (2.5:1)
- Do **not** enter at the breakout print itself.

**Plan 3 — Tactical short (lower probability, counter-trend): only on a failed retest of 259.**
- Trigger: intraday push to 258.50–259.50 that closes back below **254.00** (10 EMA)
- Stop: **261.50** (above 09-04 high) → risk ≈ 5.5
- Targets: 249.50 (0.9:1 — marginal) · 246.40 (1.4:1) · 244.30 (1.9:1)
- This is a fade, not a position. Stand down if 50>200 spread keeps widening.

**Sizing:** ATR = 5.97 = **2.34% of price**. For a 1%-of-equity risk on a 3.70-point stop, shares = 0.01 × Equity ÷ 3.70. On a $100,000 account that is 270 shares (~$67.6k notional) — **notional is too large**; cap exposure at ~25% of equity (≈98 shares, ~$25k) and accept ~0.37% risk. Because ATR is at a local low, expect a volatility expansion: **stops tighter than ~1 ATR are likely to be noise-stopped.**

---

## 8. Risks & Invalidation Checklist

1. **Event risk is the dominant tail.** The two quarterly catalysts visible in this dataset produced a **−9.73% two-day drop** (02-05 232.99 → 02-06 210.32 on 179M shares) and a **+15.32% gap** (07-30 235.50 → 07-31 271.58 on 129M). Position sizing must assume a double-digit gap is possible into the next report; do not carry full size into it.
2. **No capitulation at the 09-16 low** means the low is unproven — a retest of 244–246 is a live risk, not a tail.
3. **The 265–278 zone is failed-breakout supply**, so upside should be harvested in tranches, not held for 284.
4. **Bullish thesis invalidates** on a daily close below 244.30; it is *confirmed* on a close above 259.50 with MACD > signal and rising VWMA.
5. **Neutral-today reality:** RSI 49.2, MACD −1.37, price inside the MA coil, and two rejections at 259 mean there is genuinely **no edge at 254.98**. The disciplined action is to let price come to 250–252 or to confirm above 259.50.

---

## 9. Summary Table

| Dimension | Reading | Evidence (2026-09-22) | Implication |
|---|---|---|---|
| **Primary trend** | Bullish | Price +6.01% vs 200 SMA (240.53); 50−200 spread widened +10.39 → +15.72 since 08-13 | Do not short structurally |
| **Intermediate trend** | Flattening | 50 SMA 256.26, +1.83 pts over 10 sessions vs +6.84 over prior 20 | Consolidation, not trend |
| **Short-term trend** | Turning up | 10 EMA 252.73 (09-17) → 254.11; 3 up-sessions | Tactical long bias |
| **Price location** | Inside MA coil | Close 254.98 vs 10EMA 254.11 / 20SMA 255.77 / 50SMA 256.26 | Direction unresolved |
| **Momentum (MACD)** | Negative, improving | MACD −1.367 vs signal −1.310; hist −0.057 from −1.539 | Crossover imminent, not done |
| **Momentum (RSI)** | Neutral | 49.22; low was 39.45 (09-16), high 52.69 (09-21) | No overbought/oversold edge |
| **Volatility** | Contracting | ATR 5.97 (2.34%) vs 8.54 on 08-13; BB width 7.30% | Coil → expansion pending |
| **Volume** | Unconfirmed | Price only +0.42% vs VWMA 253.92; 41.98M today (+24% avg) | Bounce lacks conviction |
| **Price action** | Bearish short-term | 259.49 / 259.00 highs rejected; 09-22 closed near low, −1.34% | 259 is the ceiling |
| **Drawdown** | −10.22% from 284.02 (08-03) | Low 244.30 (09-16); now +4.37% off low | Correction, not breakdown |
| **Key resistance** | 259.50 → 265.11 → 267.56 | 09-21/09-03 highs; BB upper; 08-28 high | Take profit zone |
| **Key support** | 249.50–252.00 → 246.43 → 244.30 → 240.5 | 09-10/17 lows; BB lower; cycle low; 200SMA + gap | Buy zone / invalidation |
| **Preferred action** | **Wait; buy 250.50** | R:R 2.2:1 to 258.50, 3.9:1 to 265.10 | Limit orders, 3.70 stop |
| **Invalidation** | Daily close < 244.30 | Breaks higher-low structure | Exit longs, target 240.5 |

**Bottom line for AMZN:** the long-term trend is intact and the correction has been unusually orderly (contracting ATR, no volume climax, RSI never oversold). Momentum is one to two sessions from a bullish MACD cross, but today's rejection candle at 259 and a price only 0.42% above VWMA argue against chasing. The highest-expectancy play is patience: accumulate the 249.50–252.00 shelf with a stop under 246.80, or wait for a *retest* of a confirmed 259.50 breakout.