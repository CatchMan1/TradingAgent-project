# AMZN — Multi-Timeframe Technical Assessment (as of 2026-08-18)

## 0. Data integrity check

`get_stock_data`, `get_indicators`, and `get_verified_market_snapshot` **agree exactly** on the 2026-08-18 row (O 260.63 / H 262.18 / L 257.73 / C 259.45, volume 33,171,300) and on every indicator value used below (50-SMA 248.5854, 200-SMA 238.0085, 10-EMA 264.1475, MACD 5.0045, signal 5.9127, histogram −0.9082, RSI 50.925, Bollinger mid 257.6805 / upper 296.2725 / lower 219.0885, ATR 7.8582, VWMA 267.2688). **No discrepancies to flag.**

One caution: the snapshot also returns `mfi = 0.527372`, which appears to be on a 0–1 scale (≈52.7 on the conventional 0–100 scale). I use it only as a neutral cross-check and do not build any conclusion on it.

---

## 1. Regime call: **bullish primary trend, bearish short-term momentum, decision point in progress**

AMZN is in an **orderly, low-volume retracement inside a still-intact post-earnings uptrend**, but that retracement has now reached the first real decision level (the 20-day mid-band at 257.68) and confirmed a short-term momentum breakdown (MACD bearish cross, price below the 10-EMA and below the volume-weighted average price).

Three facts define the setup:

1. **The long/intermediate trend is unambiguously up.** Close 259.45 sits **+4.4% above the 50-SMA (248.5854)** and **+9.0% above the 200-SMA (238.0085)**. Both averages are rising into the close, and the 50-SMA is in a *fresh* upturn — it bottomed at 246.3842 on 2026-07-30 and has climbed for 13 straight sessions to 248.5854. Price has closed above the 50-SMA for **13 consecutive sessions** since the 2026-07-31 breakaway gap.
2. **The short-term trend has rolled over.** Six consecutive lower closes (2026-08-11 through 2026-08-18), four consecutive closes below the 10-EMA (2026-08-13 onward), a MACD/signal bearish cross on 2026-08-17–18, and a failed lower high at 278.09 (2026-08-10) versus the 284.02 close high of 2026-08-03.
3. **Participation, not price, is the strongest argument for the bulls.** The pullback is happening on *falling* volume (27.3–43.9M) versus the 129.05M (2026-07-31) and 90.83M (2026-08-03) breakout sessions. That is consolidation behaviour, not liquidation. However, the VWMA at **267.2688 — 2.9% above spot** — says the average volume-weighted buyer of the last ~month is underwater, which creates genuine overhead supply into 265–268.

---

## 2. The 2026 context the current price sits inside

From the retrieved 157-session series:

- **Jan 2026 peak:** close 247.38 (01-09), intraday high 248.94 (01-12).
- **Feb event shock:** close 222.69 (02-05, −4.4%) then a gap-down open of 202.70 on 2026-02-06 with 179.2M shares; low 200.31. Drawdown from the Jan high was roughly −19.5%.
- **Six-week base** at roughly 196–218 (Feb 12 low 199.60 → Mar 27 low 199.14).
- **April breakaway:** close 213.77 (04-07) → 221.25 (04-08, gap open 223.79) → 233.65 (04-09).
- **Grind to a new all-time closing high of 284.02 and intraday high of 287.20 on 2026-08-03.**
- **Current pullback:** −8.65% from the 284.02 close (284.02 → 259.45) and −9.66% from the 287.20 print. Year-to-date, +14.55% (226.50 on 01-02 → 259.45).

Structurally important: **rising swing lows** — 196.00 (2026-02-17) → 199.14 (2026-03-27) → 225.55 (2026-06-25) → 226.16 (2026-07-29). The current low of 257.73 is far above that progression, so the higher-lows sequence is intact.

Also important for context on the *current* pattern: in June–July, price repeatedly **failed at or below the 50-SMA** (e.g., close 227.01 vs 50-SMA 256.45 on 2026-06-25; close 235.50 vs 50-SMA 246.38 on 2026-07-30). The 50-SMA reclaim is only 13 sessions old, which is why a retest of 248.59 would be structurally normal rather than alarming.

---

## 3. Indicators selected (8) and why

| # | Indicator | Value (2026-08-18) | Why it is the right tool here |
|---|---|---|---|
| 1 | **close_10_ema** | 264.1475 | Fastest read on whether the 6-session slide is decelerating. Price is below it; reclaiming 264.15 is the minimum condition for a bounce. |
| 2 | **close_50_sma** | 248.5854 | The operative intermediate pivot and freshly *rising*. Defines the "healthy pullback" boundary. Also confluent with the Jan 2026 highs (247.38 close / 248.94 high). |
| 3 | **close_200_sma** | 238.0085 | Long-term regime filter. Rising monotonically (230.06 on 05-20 → 238.01 on 08-18); no death-cross risk. Confirms this is a correction inside an uptrend. |
| 4 | **macd** | 5.0045 | Still **positive** despite the slide from 8.4324 (08-11). Distinguishes "momentum reset" from "trend break" (late July MACD was −3.75). |
| 5 | **macdh** | −0.9082 | Captures the timing of the bearish cross (turned negative 08-17, deepened 08-18) and the *velocity* of the unwind (4.62 on 08-05 → −0.91 now). |
| 6 | **rsi** | 50.925 | Momentum reset gauge: 72.23 (08-03) → 50.93, a 21-point round trip in 11 sessions. Neutral, with room in either direction. |
| 7 | **vwma** | 267.2688 | The most informative indicator right now: spot is **2.9% below** the volume-weighted price. Quantifies trapped/overhead supply from the 07-31–08-05 high-volume window. |
| 8 | **atr** | 7.8582 (3.03% of price) | Stop placement and sizing. Volatility spiked to 9.9827 (08-05, 3.66% of price) post-gap and is now contracting — a normalization signal. |

I deliberately excluded stochastics (redundant with RSI), the MACD signal line as a standalone (its information is fully contained in MACD + histogram), and the Bollinger **upper/lower** bands as *trade triggers* — the band width is 29.95% of the mid-band, making the outer bands nearly meaningless right now (more below). The **Bollinger mid-band (boll = 257.6805)** is used as a level because it equals the 20-day SMA.

---

## 4. Trend analysis, layer by layer

### Long term (200-SMA): solid, improving
200-SMA has risen every single session in the retrieved window, from 230.0610 (2026-05-20) to 238.0085 (2026-08-18), a 3.5% three-month slope. The 50-SMA sits **10.58 points above** it (248.5854 vs 238.0085). The spread peaked near 11.63 on 2026-07-30 (246.3842 vs 234.7547) and has narrowed modestly — a hint of slowing leadership, not a trend break. A close below 238 is not a realistic base case; it would require a further −8.3%.

### Intermediate (50-SMA): the key structural line
The 50-SMA went **239.6716 (05-20) → peaked 257.1002 (06-18) → trough 246.3842 (07-30) → 248.5854 (08-18)**. That U-shape is a classic "trend digest then resume" signature. Price probing back toward 248.59 would be a **retest of the average from above** — the single highest-quality long entry zone in this structure. Note the confluence: 248.5854 (50-SMA) sits almost exactly on the January 2026 ceiling (close high 247.38 on 01-09; intraday 248.94 on 01-12), which is textbook breakout-retest geometry *if* it gets there.

### Short term (10-EMA): bearish, price is on the wrong side
10-EMA **267.1837 (08-12 peak) → 264.1475 (08-18)**; close 259.45 is **−1.78% below** it. Four consecutive closes below (08-13, 08-14, 08-17, 08-18). The 10-EMA is descending for the first time since 2026-07-29, and it sits *below* the VWMA (264.15 vs 267.27), meaning even the fast average is under the volume-weighted cost basis.

### Sequence of highs and lows (the cleanest read)
- 08-03: close high **284.02**, intraday high **287.20**
- 08-05: close 272.65 → bounce attempt
- 08-10: **lower high close 278.09** (failed to exceed 284.02)
- 08-18: close 259.45, **lowest intraday print (257.73) since 2026-07-30**

Lower high, then lower low = short-term downtrend by definition. The question is whether it is a *corrective* downtrend (inside an uptrend) or a *reversal* downtrend. The trend averages and volume profile say corrective; the VWMA and MACD say the risk is real.

---

## 5. Momentum: unwinding, but from a low base

**RSI (50.925).** The 72.23 reading on 2026-08-03 was the only meaningful overbought peak of the move (also 67.88 on 07-31, 65.87 on 08-10). RSI has now given back 21.3 points in 11 sessions and is dead-neutral. For a stock 4.4% above a rising 50-SMA, RSI in the low 50s is *not* a sell signal — in strong uptrends RSI typically bottoms in the 40–50 zone. **A daily close with RSI under ~40 while price holds above 248.59 would be the first genuinely constructive "oversold into support" setup.** Conversely, RSI losing 45 without price losing 257.68 would suggest the 42-point June-to-August advance is being actively unwound.

**MACD (5.0045) / signal (5.9127) / histogram (−0.9082).** Bearish cross confirmed over two sessions. Critical nuance: **the MACD line is still positive**, unlike the 2026-07-23 to 07-30 window when MACD ran −0.53 to −3.75. The difference in interpretation is large:
- Late July: price 244.85 → 226.65 while MACD went negative = momentum breakdown *into* the gap-up. It resolved with a violent reversal.
- Now: MACD positive and only just crossed = **deceleration at high altitude**.

Also note the **whipsaw precedent in this very dataset**: the histogram was negative for six sessions (07-23 to 07-30) and then flipped sharply positive on 07-31. MACD crosses in AMZN 2026 have not been reliable in choppy conditions; do not treat the 08-17 cross as a standalone short signal.

Histogram trajectory: **+4.6192 (08-05) → +3.1711 (08-11) → +0.3922 (08-14) → −0.3097 (08-17) → −0.9082 (08-18)**. The decline has been monotonic for eight sessions — that is a steady, not panicked, momentum bleed.

---

## 6. Volatility and bands

**ATR = 7.8582 = 3.03% of price.** Path: **6.8924 (07-29) → 9.9827 post-gap (08-05) → 7.8582 (08-18)**. In percentage terms ATR% went 3.04% → 3.66% → 3.03% — i.e., the earnings-gap volatility expansion has *fully normalized* and we are back to the pre-gap regime. Practical consequence: stops must be sized against ~$7.90 of daily range. A 1.5×ATR stop from 259.45 lands at **247.66**, which sits conveniently just under the 50-SMA/January-high confluence at 248.59.

**Bollinger (boll 257.6805 / ub 296.2725 / lb 219.0885).**
- Band width = **29.95% of the mid-band**, up from **11.1% on 2026-07-15** (254.7978/227.9532 around a 241.38 mid) — a 2.7× expansion driven by the 07-31 gap. The outer bands are therefore *not* tradeable levels; the upper band at 296.27 is 14.2% away and meaningless as resistance.
- **%B = 0.523** — price is almost exactly mid-band.
- **The signal that matters: the close of 259.45 is only +0.69% above the 20-day mid-band at 257.6805, and today's low of 257.73 essentially tagged it (0.05 above).** This is the tightest pivot on the chart. Since the mid-band equals the 20-SMA, a close below it converts a "pullback" into a "20-day trend break."

---

## 7. Volume and the overhead-supply problem

| Session | Close | Volume | Read |
|---|---|---|---|
| 2026-07-30 | 235.50 | 101,839,800 | Pre-event positioning |
| 2026-07-31 | 271.58 | **129,054,800** | Gap up 265.00 open from 235.50 close; low 262.01; high 273.23 |
| 2026-08-03 | 284.02 | 90,830,200 | Blow-off closing high (high 287.20) |
| 2026-08-11 → 08-14 | 272.27 → 262.65 | 31.9M / 29.9M / 32.2M / 27.3M | Decline on drying volume |
| 2026-08-17 | 261.31 | **43,896,500** | Heaviest down day of the slide — first distribution warning |
| 2026-08-18 | 259.45 | 33,171,300 | Volume recedes again |

Two readings, both true:
- **Bullish:** the entire −8.65% retracement has occurred on ~33M shares/day versus 90–129M on the way up. Sellers are not aggressive.
- **Bearish:** the VWMA (267.2688) is **2.93% above spot and still rising** (265.2703 on 08-17 → 267.2688 on 08-18). Assuming a ~20-session weighting window, the huge 07-31/08-03 volume keeps the VWMA pinned high for roughly two more weeks. **Every rally into 265–268 will be meeting supply from buyers who are currently losing money.** That is the single best explanation for why the 08-05 bounce stalled at 278.09 and why the gap support at 262.01 failed on 08-17 (first close below the 2026-07-31 session low).

---

## 8. Level map (all values tool-derived)

**Resistance**
| Level | Value | Source |
|---|---|---|
| Gap/session low reclaim | **262.01** | 2026-07-31 low; price closed below it first on 2026-08-17 |
| 10-EMA | **264.1475** | Fast trend |
| VWMA (volume-weighted cost) | **267.2688** | Overhead supply / trapped buyers |
| Congestion | 272.27–274.48 | Closes 08-11 and 08-07 |
| Lower high | **278.09** | 2026-08-10 close |
| All-time high zone | **284.02 / 287.20** | 2026-08-03 close / intraday high |

**Support**
| Level | Value | Source |
|---|---|---|
| **Immediate pivot** | **257.6805** | 20-SMA / Bollinger mid; today's low 257.73 |
| Air pocket → 50-SMA | 248.5854 | 50-SMA, confluent with Jan 2026 highs (247.38 close / 248.94 high) |
| Gap-fill zone | 239.82 – 235.50 | 2026-07-30 high / close (top edge of the unfilled 07-31 gap) |
| 200-SMA | 238.0085 | Long-term regime line |

---

## 9. Actionable playbook

**Scenario A — Bullish continuation (needs confirmation, do not front-run):**
Trigger: a daily close back above **264.15 (10-EMA)** and preferably above **267.27 (VWMA)** on volume > ~45M. That combination would flip the VWMA from resistance to support.
- Entry on the reclaim, or on the first higher close after it.
- Stop: below 257.68 (−0.7% from spot, but ~0.9 ATR — tight; a wider stop under the week's low at 257.73 is more robust).
- Targets: 272–274 (first), 278.09 (second), 284.02 (third). Measured from 259.45 that is +4.8% / +7.2% / +9.5%.

**Scenario B — Buy the deeper retest (highest quality/highest expectancy):**
Zone: **248–253**, i.e., the rising 50-SMA (248.5854) plus the July congestion. This is where the intermediate trend and the January-2026 breakout shelf coincide.
- Invalidation: a daily close below **245** (below the 50-SMA and ~1.6 ATR from 248.59).
- That zone would also arrive with RSI likely in the high-30s/low-40s — the classic "oversold into rising support" configuration.
- Risk from 259.45 down to that zone is −4.2%.

**Scenario C — Breakdown management (risk control, not a short recommendation on its own):**
Trigger: a daily close below **257.6805** with expanding volume (>50M). The MACD is already negative and the histogram is accelerating lower, so the confirmation would be additive.
- First objective: **248.59 (−4.2%)**.
- Second: the **239.82–235.50** gap-fill shelf (−7.6% to −9.2%). Note there is essentially no verified trading structure between 248.59 and 239.82 in the retrieved data — this is an **air pocket**, which is why 248.59 matters so much.

**Position sizing illustration (ATR-based):** with ATR = 7.8582, a 1.5×ATR stop is $11.79/share. On a $100,000 account risking 1% ($1,000), that is ~85 shares (~$22,000 notional, 22% of equity). The 3.03% daily ATR argues for *smaller* than normal size regardless of direction conviction — this is a 3%-daily-range environment, not a 1.5% one.

**What would change my view:**
- Bearish flip: 50-SMA rolling back down; close below 248.59; RSI breaking 40 while price is below the mid-band; MACD histogram worse than −2.0.
- Bullish re-acceleration: close above 267.27 on >50M volume with rising RSI back above 60; the 50/200 spread widening again above 11.6.
- Regime shift I cannot see: the 2026-07-31 gap (235.50 → 265.00 open) almost certainly reflects an unscheduled fundamental catalyst. **I have no news, earnings, or estimate data in these tools** — all of the above is price/volume geometry only. Any fundamental surprise would invalidate the technical framework, and the 08-17 volume uptick (43.9M) is worth checking against headlines before committing capital.

---

## 10. Summary table

| Dimension | Reading (2026-08-18) | Evidence | Bias |
|---|---|---|---|
| **Primary trend (200-SMA)** | Bullish | Close 259.45 = **+9.01%** vs 200-SMA 238.0085, which has risen every session since 05-20 (230.06 → 238.01) | ▲ Up |
| **Intermediate trend (50-SMA)** | Bullish, freshly re-established | 50-SMA 248.5854, trough 246.3842 on 07-30 now turning up; 50 > 200 by 10.58 pts; 13 consecutive closes above | ▲ Up |
| **Short-term trend (10-EMA)** | Bearish | Close −1.78% vs 10-EMA 264.1475; 4 straight closes below; 6 straight lower closes (08-11 → 08-18) | ▼ Down |
| **Momentum (RSI)** | Neutral / reset | 72.23 (08-03) → **50.925**; not oversold, not overbought | ◄► Neutral |
| **Momentum (MACD)** | Decelerating, bearish cross | MACD **+5.0045** vs signal 5.9127; histogram **−0.9082** (negative 2 sessions, from +4.62 on 08-05); MACD still above zero | ▼ Down (mild) |
| **Volatility (ATR)** | Elevated but normalizing | ATR **7.8582** = 3.03% of price; 9.9827 (08-05) → 7.8582; back to pre-gap regime | ◄► Neutral |
| **Bands** | Wide; price at mid-band | Mid 257.6805, UB 296.2725, LB 219.0885; width 29.95% of mid (vs 11.1% on 07-15); %B = 0.523 | ◄► Pivot |
| **Volume / participation** | Pullback on light volume **but** overhead supply | Down days 27.3–43.9M vs 129.1M/90.8M on 07-31/08-03; **VWMA 267.2688 = 2.93% above spot and rising** | ▼ Caution |
| **Immediate pivot** | 257.6805 / 257.73 | 20-SMA mid-band + today's low — 0.69% below the close | ⚑ Decision |
| **Key support** | 248.5854 (50-SMA), then 239.82–235.50 gap shelf | 50-SMA confluent with Jan-2026 highs 247.38/248.94; air pocket below 248.59 | — |
| **Key resistance** | 262.01 → 264.15 → 267.27 → 278.09 → 284.02/287.20 | 07-31 low; 10-EMA; VWMA; 08-10 lower high; ATH zone | — |
| **Drawdown from peak** | **−8.65%** from 284.02 close (−9.66% from 287.20 high) | Six-session orderly retracement | — |
| **YTD performance** | **+14.55%** | 226.50 (01-02) → 259.45 | ▲ Up |
| **Net stance** | **Hold longs; no new full size until 264.15 reclaimed or 248.59 retested. Risk defined by 257.68 (tight) and 245 (structural).** | Trend up, momentum down, price at the pivot | ◄► **Neutral / wait for trigger** |