# GOOGL — Technical Analysis & Trading Plan
**As of session close 2026-09-25 | Reference price: $343.92**

> **Data integrity note:** The `get_stock_data` CSV (128 sessions, 2026-03-25 → 2026-09-25) and the `get_verified_market_snapshot` for 2026-09-25 agree exactly on OHLCV for every overlapping row (e.g., 9/25 O 342.35 / H 347.03 / L 341.11 / C 343.92 / V 21.88M). **No discrepancy found.** All exact price and indicator values below are taken from the verified snapshot; all derived percentages are computed only from tool-provided rows.

---

## 1. Regime Classification: Long-Term Uptrend, Medium-Term Correction, Short-Term Coiled Spring

GOOGL is **not** in a clean trend on any single timeframe — it is in three different regimes stacked on top of each other. That stacking is the single most important observation in this report.

| Timeframe | Gauge | Reading | Verdict |
|---|---|---|---|
| Long-term | 200SMA = **338.21**, rising ~+0.15/day | Price **+1.69%** above it | **Intact uptrend** |
| Medium-term | 50SMA = **344.29**, falling since 7/13 (peak 372.80) | Price **−0.11%** below it | **Correction / neutral** |
| Short-term | 10EMA = **344.46**; 20SMA (Boll mid) = **342.17**; VWMA = **344.06** | Price pinned inside a **2.3-point cluster (−0.16% to +0.51%)** | **Compression / no edge** |

The 50SMA has fallen **28.5 points from its 7/13 peak of 372.80 to 344.29** while the 200SMA has climbed from **319.42 (7/13) to 338.21**. That has compressed the 50/200 spread from **53.4 points (16.7%) on 7/13 to just 6.08 points (1.80%) today** — the narrowest in the entire six-month sample. This is a trend that has stopped trending, not a trend that has reversed.

---

## 2. Trend Structure: A Descending Sequence of Highs With Floors That Hold

The narrative in the price data is unusually clean:

- **H1 melt-up:** close **273.50 (3/30)** → intraday high **408.61 (5/18)**, a **+49.4%** advance in roughly seven weeks.
- **Break #1 — 7/23:** close **342.09 (7/22) → 317.69 (7/23) = −7.13%** on **69.42M shares** (~2.6× the recent ~27M average). This is the defining event of the second half of the year. It converted the chart from uptrend to distribution.
- **Break #2 — 8/5:** **383.34 open → 356.77 low → 362.43 close (−4.03%)** on **46.93M shares**, a failed gap-up.
- **Since then: a descending ceiling.** The sequence of rally highs is unambiguous: **408.61 (5/18) → 384.48 (8/5) → 364.17 (9/22) → 359.44 (9/18) → 347.03 (9/25)**.
- **Floors, however, are holding:** intraday lows of **314.90 (7/23)**, **338.57 (8/20)**, **327.74 (9/10)**, **336.02 (9/24)**, **341.11 (9/25)**. The September floor is ~13 points above the July low.

**Interpretation:** this is a **broad 327–365 distribution/base with a downward-sloping ceiling** — a mild descending-triangle flavor rather than a clean symmetrical coil. Descending highs imply supply is being fed into strength; holding floors above the July low implies the longer-term bid has not abandoned the name. Neither side has won. The compression in the reference levels (Section 5) says the tie is about to be broken.

**The 9/22 rejection is the most recent, and most instructive, supply event.** Price printed **364.17** — its highest level since 8/5 — then closed at **351.16**, **13.01 points (3.57%) below the high**, essentially printing a shooting star. The following session gave back **−3.80%** to **337.83** on **35.58M shares**. That is textbook failed-breakout behavior, and it defines the near-term supply shelf.

---

## 3. Momentum: A Fresh Bullish Cross That Is Already Rolling Over

This is where the nuance lives, and where a superficial read would get trapped.

**MACD (verified 9/25): MACD line +0.083, signal −0.367, histogram +0.451.**

The bullish sequence was real:
- Histogram turned positive **9/14** (−0.426 on 9/11 → **+0.573**).
- MACD line crossed the **zero line on 9/21** (+0.637), the first positive reading since 8/11.
- MACD line peaked at **+1.076 on 9/22**; histogram peaked at **+2.002 on 9/21**.

But the follow-through has evaporated:
- MACD line: **1.076 (9/22) → 0.345 (9/23) → 0.129 (9/24) → 0.083 (9/25)**.
- Histogram: **2.002 (9/21) → 1.953 (9/22) → 0.977 (9/23) → 0.609 (9/24) → 0.451 (9/25)**.

The histogram has **given back 77% of its peak in four sessions**. The MACD line is now only 0.083 above zero — a single down day flips it negative. **This is a bullish crossover in name only; in substance it is a momentum fade at the zero line.** Traders who bought the 9/21 zero-line cross are roughly flat-to-down, and the momentum engine that justified the entry is gone.

**RSI (verified 9/25): 49.72.** Perfectly neutral. The recent path: **39.36 (9/9) → 58.80 (9/21) → 45.06 (9/23) → 49.72 (9/25)**. RSI briefly reached overbought-adjacent territory at 58.8 on the 9/22 spike and was rejected before 60 — a sign that buyers lacked the conviction to press. There is **no clean bullish or bearish divergence** to trade; RSI is confirming "no trend," which is itself useful information. In a range regime, RSI 45–60 is noise, not signal.

**Net momentum read:** the bearish momentum impulse from July/August has dissipated (MACD recovered from −3.91 on 9/10), but the bullish replacement has failed to establish itself. Momentum is **neutral with a negative tilt** because the freshest impulse is decelerating.

---

## 4. Volatility: A Textbook Squeeze With a Measurable Two-Sided Resolution

**Bollinger (verified 9/25): middle 342.174, upper 354.975, lower 329.373.**

- **Band width: 25.60 points = 7.48% of the middle band.**
- On **8/10** the width was **67.91 points (19.5%)**. On **7/27** it was **59.61 points (16.9%)**.
- **7.48% is the tightest band width in the entire 60-session indicator window** — and the squeeze has been persistent, not a one-day artifact (width has held 6.2–7.5% for eight straight sessions).

**ATR (verified 9/25): 8.785 = 2.56% of price.** Down from **13.93 on 8/5** and **11.76 on 7/27** — a ~37% collapse in realized daily range in under two months. ATR ticked up modestly from **8.12 (9/4)** to **9.15 (9/23)**, then eased to **8.79**, suggesting the 9/23 selloff was a brief volatility pulse, not a regime shift.

**Position within the bands:** %B = (343.92 − 329.373) / (354.975 − 329.373) = **56.8%** — upper-middle of the channel, exactly where an unresolved market sits.

**The measured-move framework this creates is unusually tidy:**

| Direction | Trigger | Measured move (1 band width from mid) | Confluence with real structure |
|---|---|---|---|
| **Up** | Close > 354.97 | **342.17 + 25.60 = 367.77** | Just above the **364.17 (9/22)** rejection high; below **376.69 (8/3)** |
| **Down** | Close < 329.37 | **342.17 − 25.60 = 316.57** | Just above the **314.90 (7/23)** crash low |

Both measured-move targets land almost exactly on pre-existing structural levels. That is a strong, tool-supported reason to treat a band-width resolution as the primary trading thesis rather than trying to predict the direction in advance.

---

## 5. The Compression Cluster: Why the Next Move Should Be Decisive

Five independent reference levels are currently stacked inside a **2.28-point (0.66%)** window:

| Level | Value | Distance from 343.92 |
|---|---|---|
| 10EMA | 344.459 | −0.16% |
| 50SMA | 344.290 | −0.11% |
| **Close** | **343.920** | **—** |
| VWMA | 344.061 | +0.04% |
| Bollinger mid (20SMA) | 342.174 | +0.51% |

Price is *literally sitting on the average of every participant in the market* — the 10-day, 20-day, 50-day, and volume-weighted cost bases all converge at 342–344. In this condition, there is no "support" to bounce from and no "resistance" to break; there is only a spring. **When price, VWMA, and a flat 50SMA coincide, the market is at equilibrium and the next sustained directional flow resolves the whole cluster at once.** This is why the plan below is trigger-based rather than forecast-based.

---

## 6. Volume & Participation: The Rebound Is Under-Supported

**VWMA (verified 9/25): 344.061 vs close 343.92** — price is **0.04% below** its volume-weighted average price. Volume-weighted holders are exactly at breakeven. That is neutral, but the *derivative* is more interesting: VWMA bottomed at **339.386 (9/11)** and has risen for five of the last six sessions (**342.23 → 343.70 → 343.93 → 343.80 → 344.06**). The volume-weighted cost basis has stopped falling and is curling up — a quiet, constructive sign that the September dip was absorbed.

**But the volume pattern on the bounce is poor:**

| Session | Close | Change | Volume | Context |
|---|---|---|---|---|
| 9/22 | 351.16 | −1.07% | 29.79M | Rejection from 364.17 |
| **9/23** | **337.83** | **−3.80%** | **35.58M** | **High-volume distribution** |
| 9/24 | 342.36 | +1.34% | 23.78M | Rebound on 33% less volume |
| 9/25 | 343.92 | +0.46% | 21.88M | Rebound on 38% less volume |

- **10-session average volume ≈ 28.5M; 21-session average ≈ 26.7M.**
- The 9/23 decline traded **35.58M** (≈25% above the 10-day average); the two rebound sessions traded **23.78M and 21.88M** (≈17–23% *below* average).
- **Selling is happening on expanding volume; buying is happening on contracting volume.** Until that inverts, rallies toward 350–355 should be treated as liquidity for sellers, not confirmation.

**Also note 9/18:** volume **47.63M** with a high of **359.44** and close of **349.54** — a high-volume session that failed to hold its high. Large-volume failure at resistance is a distribution fingerprint.

**Gap risk is empirically elevated:** this instrument produced **−7.13% (7/23)** and **−4.03% (8/5)** single-session moves on 2–2.5× normal volume within the sample. Any position held overnight should be sized for a 2×ATR (~17.6 points, 5.1%) adverse gap, not a 1×ATR one.

---

## 7. Structural Map — Levels That Matter

**Resistance (ascending):**
1. **347.03** — 9/25 high (immediate)
2. **349.50–350.00** — 9/17 high 349.50; 9/23 high 350.00; multiple closes 349–351
3. **354.97–355.26** — **upper Bollinger band**, aligned with the 9/22–9/23 breakdown zone
4. **357.61–359.44** — 9/21 high 357.61; 9/18 high 359.44
5. **364.17** — 9/22 rejection high; **the range ceiling**
6. **376.69–380.52** — 8/3 and 8/4 highs
7. **384.48** — 8/5 high (post-July breakdown peak)

**Support (descending):**
1. **342.17–342.35** — Bollinger mid; 9/25 open 342.35
2. **340.19–341.11** — 8/18 low 340.19; 9/25 low 341.11; 8/20 close 340.67
3. **337.83–338.21** — **200SMA at 338.21** + 9/23 close 337.83 *(the pivotal line)*
4. **332.82–335.02** — 9/1 close 335.02; 9/2 low 332.82
5. **327.74–329.37** — 9/10 low 327.74; **lower Bollinger band 329.37**
6. **314.90** — 7/23 low (the structural bull-case line)

---

## 8. Actionable Trading Plan

### Base case (highest probability): stay neutral inside 337.8–355.0
Price is at equilibrium with a neutral RSI, a fading MACD, contracting volume, and a squeeze. **There is no positive-expectancy directional entry at 343.92.** The correct action today is patience, with pre-defined triggers. Do not pay up in the middle of the cluster.

### Scenario A — Bullish breakout (primary upside trigger)
- **Trigger:** daily **close above 355.00** (clears the upper band, the 9/22–9/23 breakdown zone, and the 350/354 supply shelf) **on volume ≥ 30M** (above the 28.5M 10-day average). An intraday poke is not enough — the 9/22 wick is the precedent for false breaks.
- **Entry:** 355.5–357.5 on the close or on a successful retest of 355.
- **Stop:** **349.00** (below the 350 shelf; ~0.75 ATR) for tactical — or **343.50** (below the 50SMA cluster; ~1.4 ATR) for a wider swing.
- **Targets:** **364.17** (T1, range high), **367.8** (T2, band-width measured move), **376.7** (T3, 8/3 high).
- **R:R:** ~1.4:1 to T1 and ~3.2:1 to T2 on the tight stop; ~1.0:1 to T1 and ~1.9:1 to T2 on the wide stop. *Because the tight stop offers better R:R but a higher stop-out rate in a 2.56%-ATR name, the wide stop is preferred unless the breakout comes with ≥35M volume.*

### Scenario B — Support reclaim (preferred long entry)
- **Setup:** flush into **333–338** (200SMA / 9/2 low zone), RSI dipping into the high-30s, followed by a bullish reversal day on above-average volume.
- **Entry:** 334–336 on the reversal close.
- **Stop:** **326.50** (below the 327.74 September low; ~1.0 ATR).
- **Targets:** **349.5** (T1), **355.0** (T2).
- **R:R:** ~2.0–2.8:1. This is structurally the highest-quality long because it buys at the *bottom* of the compressed range rather than chasing a mid-cluster breakout, with the rising 200SMA as a tailwind.

### Scenario C — Breakdown (bearish trigger)
- **Trigger:** daily **close below 337.50** — this simultaneously breaks the 200SMA (338.21), the 9/23 low close (337.83), and the 9/24 low (336.02).
- **Entry:** 337.0 or on the retest of 338 from below.
- **Stop:** **344.50** (above the 50SMA/10EMA/VWMA cluster; 0.85 ATR).
- **Targets:** **332.82** (T1), **327.74** (T2), **316.57** (T3, band-width measured move / July low).
- **R:R:** ~1.2:1, ~2.6:1, ~5.9:1. The reward skew is attractive precisely because the 50/200 spread is so compressed — a 200SMA break has very little buffer beneath it before the 327–330 shelf.

### Scenario D — Short the supply (mean-reversion fade)
- **Setup:** rally into **354–359** with declining volume and MACD histogram rolling back toward zero.
- **Entry:** 354–357. Stop **361.50** (above the 9/18 high 359.44; 0.85 ATR). Targets **344** then **338**.
- **Note:** this is counter-trend to the long-term uptrend — treat as a tactical trade, not a position.

### Position sizing guidance
- 1 ATR = **8.79 points = 2.56%** of price. Size so a **1.5×ATR (~13.2 points, 3.8%)** adverse excursion equals your per-trade risk budget.
- For gap protection, assume a **2×ATR (~17.6 points, 5.1%)** overnight gap is possible — this instrument delivered two moves of 4–7% on 2×+ volume in the last two months.
- Avoid new full-size entries into this name while price is inside 342–345; the cluster offers no stop-loss refuge. Either let it break out (Scenario A), break down (C), or come to you at 333–338 (B).

---

## 9. What Would Change the View

**To bullish (upgrade to constructive):**
- A close above **355.00** on **≥30M** volume — confirms the squeeze resolves upward and repairs the 9/22 rejection.
- The 50SMA (344.29) flattening and turning up, which requires sustained closes above ~350.
- MACD histogram expanding back above **+1.0** while the MACD line holds above zero.
- VWMA pushing decisively above the 50SMA with price leading it.

**To bearish (downgrade to defensive):**
- A close below **337.50** — breaks the 200SMA and the September low close simultaneously.
- The **50/200SMA death cross.** At current trajectories (50SMA −0.195/day, 200SMA +0.151/day), the 6.08-point gap closes in roughly **17–20 sessions — mid-to-late October** — if price simply stays in the 340s. This is the single most important calendar risk in the chart: the 50SMA will keep falling mechanically as May's 385–403 closes roll out of its window, so **the cross can occur even if price goes sideways or grinds modestly higher.** A death cross would not invalidate the long-term bull case immediately, but it would confirm the July high as a durable lower-high structure.
- MACD line rolling back below zero while the histogram turns negative (a failed zero-line cross).
- Volume expanding on down days while contracting on up days — the current pattern continuing.

**Neutral resolution (still possible):** the squeeze could bleed out sideways through October. In that case, the 50SMA and 200SMA converge into a flat, tangled pair, and the setup's edge decays. If price is still inside 337–355 with band width under 8% in three weeks, stand down and wait for the next compression.

---

## 10. Indicator Selection Rationale

From the available list I selected **eight** indicators to maximize complementary coverage and avoid redundancy:

| Indicator | Category | Why it was chosen for *this* market |
|---|---|---|
| **close_50_sma** | Trend | Captures the active medium-term correction; it is the level price is pinned to and its slope is the key deteriorating input for the 50/200 cross. |
| **close_200_sma** | Trend | The only clean read on whether the primary uptrend survives; rising at 338.21 and directly beneath price. |
| **macd** | Momentum | Detects the zero-line cross attempt and its failure — the core momentum narrative right now. |
| **macdh** | Momentum | More timely than the signal line for measuring the *deceleration* of the 9/21 impulse (2.00 → 0.45). |
| **rsi** | Momentum | Confirms the absence of trend (49.7) and would flag any capitulation into the 333–338 support zone. |
| **boll_ub / boll_lb** | Volatility | Quantifies the 7.48% squeeze — the tightest in 60 sessions — and provides the 354.97 / 329.37 breakout and measured-move framework. |
| **atr** | Volatility | Sets stop distances (8.79 pts, 2.56%) and position size; essential given the demonstrated 4–7% gap risk. |
| **vwma** | Volume | Tests whether the rebound has real participation; at 344.06 the volume-weighted cost basis is curling up but price is not leading it — a neutral-to-soft tell. |

*Deliberately excluded:* **close_10_ema** (currently 344.46, just 0.17 above the 50SMA — informationally redundant during the squeeze), **macds** (its content is fully captured by the MACD/histogram pair), and **boll** middle as a standalone (342.17 is within 2.1 points of the 50SMA; the upper/lower bands carry the non-redundant information).

---

## 11. Bottom Line

GOOGL is a **long-term uptrend in a medium-term distribution**, currently frozen at the exact average of every relevant participant. The July 23 breakdown (−7.13% on 2.6× volume) and the 9/22 failed breakout at 364.17 (13-point upper wick, followed by −3.80% on 35.6M shares) both argue that rallies are being sold. But the rising 200SMA at 338.21, the higher September floor above the July low, and the curling VWMA argue against outright bearishness. **The tie-breaker is a 7.48% Bollinger squeeze with a measurable move to 367.8 or 316.6.**

**Do not take a position in the middle of the cluster.** Trade the edges: buy a confirmed close above 355 on volume, buy a flush into 333–338 that reverses, or sell a confirmed close below 337.50. The compressed 50/200 spread means any resolution will travel further and faster than the last six weeks of price action would suggest.

---

## Key Levels & Signals Summary

| Metric | Value (2026-09-25, verified) | Interpretation |
|---|---|---|
| **Close** | **343.92** (+0.46%) | Pinned at equilibrium |
| **Session range** | 341.11 – 347.03 | Narrow, contracting |
| **Volume** | 21.88M | ~23% below 10-day avg (28.5M) |
| **50SMA** | 344.29 | Falling since 7/13 (372.80); price below |
| **200SMA** | 338.21 | Rising ~+0.15/day; price +1.69% above |
| **50/200 spread** | 6.08 pts (1.80%) | **Narrowest in 6-month sample** |
| **10EMA** | 344.46 | Price −0.16%; part of the cluster |
| **VWMA** | 344.06 | Price −0.04%; curling up from 339.39 (9/11) |
| **Bollinger mid / UB / LB** | 342.17 / 354.97 / 329.37 | Width 7.48% — **tightest in 60 sessions** |
| **%B** | 56.8% | Upper-middle, no extreme |
| **MACD / Signal / Hist** | +0.083 / −0.367 / +0.451 | Bullish cross fading fast (hist peak 2.00 on 9/21) |
| **RSI** | 49.72 | Neutral; failed at 58.8 on 9/21 |
| **ATR** | 8.79 (2.56%) | Down 37% from 13.93 (8/5) |
| **Drawdown from high** | −15.8% from 408.61 (5/18) | Correction, not bear market |

| Signal / Level | Price Zone | Action | Stop | Targets |
|---|---|---|---|---|
| **Upside breakout** | Close > **355.00** on ≥30M vol | **Buy** | 343.50 (wide) / 349.00 (tight) | 364.17 → 367.8 → 376.7 |
| **Support reclaim** | **333–338** + reversal day | **Buy** (best R:R) | 326.50 | 349.5 → 355.0 |
| **Downside breakdown** | Close < **337.50** | **Sell/short** | 344.50 | 332.82 → 327.74 → 316.57 |
| **Supply fade** | **354–359** on weak volume | **Tactical short** | 361.50 | 344 → 338 |
| **Neutral** | **342–345** | **No trade** | — | — |
| **Death-cross watch** | 50SMA vs 200SMA (6.08 gap) | Reduce size / hedge | — | Est. **mid-to-late Oct** if price stays in 340s |

*Disclaimer: This is technical analysis based solely on the tool-provided price and indicator data as of 2026-09-25. It is not investment advice; position sizing and risk tolerance must be determined independently.*