# AAPL — Technical Analysis Report (as of 2024-01-31 close)

## 0. Data integrity note

All exact price/indicator values below come from the **verified market snapshot for 2024-01-31** (AAPL). I cross-checked the snapshot against the full OHLCV series returned by `get_stock_data` (2023-09-01 → 2024-01-31): the 2024-01-31 row is identical in both (O 187.04 / H 187.10 / L 184.35 / C 184.40 / V 55,467,800). I also verified internal consistency of MACD: `macd (0.0913) − macds (0.2346) = −0.1434`, which exactly matches the reported `macdh = −0.143358`. **No discrepancies to flag.**

**Indicator set selected (8):** `close_50_sma`, `close_200_sma`, `close_10_ema`, `macd`, `rsi`, `boll_lb` (used together with the `boll` mid / `boll_ub` envelope), `atr`, `vwma`.

Why this mix: AAPL is at an inflection where **trend structure is still bullish on the long horizon but has just been broken on the short horizon**, with volatility expanding. That calls for (a) three time horizons of trend (10 EMA / 50 SMA / 200 SMA), (b) one momentum oscillator pair that is *not* redundant — MACD for trend-momentum inflection, RSI for exhaustion/OB-OS state, (c) a volatility envelope to define breakout/failure and a mean-reversion magnet, (d) ATR for stop and size calibration, and (e) VWMA to test whether price is above or below the volume-weighted cost basis of recent participants. I deliberately excluded the MACD signal line and histogram as *separate* selections because both are algebraically derivable from `macd`+`macds` (shown above), and excluded stochastics/MFI to avoid duplicating RSI's information.

---

## 1. Where AAPL actually stands

| Metric (2024-01-31) | Value |
|---|---|
| Close | **184.40** |
| Day range | 184.35 – 187.10 (open 187.04) |
| Volume | 55.47M |
| 10 EMA | 189.63 |
| 50 SMA | 190.82 |
| 200 SMA | 182.29 |
| VWMA | 189.33 |
| RSI | 39.60 |
| MACD / Signal / Hist | 0.0913 / 0.2346 / −0.1434 |
| Boll mid / upper / lower | 187.83 / 196.98 / 178.67 |
| ATR | 3.249 |

**Structural stack:** `50 SMA (190.82) > 10 EMA (189.63) ≈ VWMA (189.33) > CLOSE (184.40) > 200 SMA (182.29)`.

This is the classic signature of a **bullish primary trend under short-term distribution**. Price remains above the 200 SMA, and the 50 SMA sits 8.53 points (4.7%) above the 200 SMA — the golden-cross regime established earlier is intact. But price has lost *every* short- and medium-term reference in a single week, and the 10 EMA has slipped **below** the 50 SMA (10 EMA 191.41 on 1/29 → 189.63 on 1/31, versus a 50 SMA that is flattening at 190.82–190.93). That is the first short-term bearish MA cross of this sequence.

---

## 2. Price action: six consecutive down closes, orderly not climactic

From the 1/23 close of **195.18**, AAPL has closed lower for six straight sessions: 194.50 (1/24), 194.17 (1/25), 192.42 (1/26), 191.73 (1/29), 188.04 (1/30), 184.40 (1/31). Cumulative decline: **−10.78 points, −5.52%** — all figures directly from the verified closes above.

Three details matter more than the headline percentage:

1. **The 1/31 candle is a near-marubozu bearish session.** Open 187.04, high 187.10, low 184.35, close 184.40 — a 2.70-point range of which 2.69 was realized to the downside, closing on the low. Sellers controlled the entire session; there was no intraday defense.
2. **Acceleration, not deceleration.** Daily declines: −0.35%, −0.17%, −0.90%, −0.36%, **−1.92%**, **−1.94%**. The two largest down days are the last two. Distribution is building, not exhausting.
3. **Volume is rising but not climactic.** 1/31 volume of 55.47M is roughly in line with the ~56.5M average across the 21 January sessions I can count in the dataset (approximate, computed from the returned rows), versus 42.4M on the 1/23 *up* day and 44.6M on 1/26. Rising volume on down days with falling volume on up days is a distribution pattern — but because there is **no volume spike**, there is **no capitulation/exhaustion signal** yet. This argues for lower prices or time-based repair rather than a V-bottom.

**The failed-high structure is the important context.** The December closing high was **198.11 (12/14)** with an intraday high of **199.62 (12/14)**. The January rally topped out at a close of **195.18 (1/23)** and an intraday high of **195.75 (1/23)** — a clear **lower high**. Combined with a break of the 185.9–188.6 congestion zone (1/12 close 185.92, 1/18 close 188.63, 1/19 close 191.56), the intermediate-term picture is now a lower-high / lower-low sequence *inside* a still-rising 200 SMA.

---

## 3. Momentum: the bullish MACD crossover has just failed

This is the single most actionable signal in the report.

- The MACD histogram went positive on **1/19** (−0.2832 → +0.2025), the MACD line crossed zero on **1/23** (+0.1837), and the histogram peaked at **+1.1282 on 1/25**.
- Since then the histogram has decayed every session: 0.9621 (1/26) → 0.7636 (1/29) → 0.3621 (1/30) → **−0.1434 (1/31)**.
- On 1/31 the **MACD line crossed back below its signal line for the first time since 1/18**, while still barely positive (+0.0913). That is a textbook **failed bullish crossover** — the weakest possible configuration, because it fails *before* momentum has even accumulated meaningfully above zero.

**RSI confirms with unusual velocity.** RSI fell from **62.62 (1/23)** to **39.60 (1/31)** in six sessions — a 23-point collapse. Context: RSI already hit **28.79 (1/5)** in the early-January flush, rebounded to 62.62, and has now round-tripped back to the high-30s. This tells us two things: (a) the January rebound was a counter-trend bounce that has been fully retraced, and (b) RSI at 39.60 is **not oversold** — there is roughly 10 points of RSI room to the 30 line before a mean-reversion setup exists. Do not buy "because RSI is low"; it isn't.

---

## 4. Volatility: expanding, with a compressed envelope and a clear downside magnet

- **ATR = 3.249**, up from **2.567 (12/28)** and **2.575 (12/29)** — a ~26% expansion in one month, and rising for three straight sessions into month-end. At 1.76% of spot, a single average day now spans roughly 181.2–187.6.
- **Bollinger:** mid 187.83, upper 196.98, lower 178.67. Total width 18.31 points = **9.75% of the mid band**. Compare 1/5, when width was 20.63 points (10.7% of mid) — so despite the price decline, the envelope has actually **narrowed slightly**, i.e. this is a *directional* move out of a contracting range rather than an expanding-volatility breakout. Directional moves from compression tend to persist.
- Price closed **below the mid band (187.83)** for the first time since 1/17, after tagging the upper half of the envelope on 1/24 (high 196.38 vs upper band 197.62). **The upper-band ride failed.** The prior session-high cluster plus the mid-band rejection puts the 187.8–189.6 area firmly in the "supply" column.
- Critically, the **lower band has been pinned at 178.6–178.9 for two weeks** (178.67 on 1/31, 178.82 on 1/30, 178.66 on 1/16–1/17). Flat lower bands act as magnets/targets. That region lines up with, and sits just below, the **180.17–180.93 low cluster** from 1/4, 1/5, 1/16, and 1/17.

---

## 5. Volume/participation: price is below the volume-weighted cost basis

**VWMA = 189.33** versus close 184.40. Price is **2.61% below** the volume-weighted average price of the recent window, meaning the *average* recent buyer is underwater. The VWMA path is itself informative: it fell from 195.48 (12/27) to a trough of 185.25 (1/18), recovered to 189.40 (1/30) — and has now stalled (189.33 on 1/31) as price drops away beneath it. A flat-to-turning VWMA with price beneath it is a bearish-participation signal; a VWMA still making higher lows (185.25 → 189.40) is the *only* remaining short-term constructive element, and it is on the verge of rolling over.

Note that VWMA (189.33) and the 10 EMA (189.63) have converged into a **single tight resistance shelf at 189.3–189.6**, immediately below the 50 SMA at 190.82. That ~189.3–190.8 band is the decision zone.

---

## 6. Actionable framework

**Bias: tactically bearish / strategically neutral.** Long-term uptrend intact (price > 200 SMA, 50 > 200), but the short-term trend, momentum, and participation all turned negative within six sessions and did so *without* generating an oversold condition that would justify a contrarian long.

### Key levels (all derived from verified tool output)
- **Resistance 1: 187.83** (Bollinger mid) — first thing a bounce must reclaim.
- **Resistance 2: 189.3–190.8** (10 EMA 189.63 + VWMA 189.33 + 50 SMA 190.82) — the real ceiling. A *close* above this band would flip the short-term bias back to bullish.
- **Resistance 3: 195.18–196.38** (1/23 close / 1/24 high), with the 12/29→1/2 gap zone (opened at 187.15 from 192.53) acting as overhead supply.
- **Support 1: 184.35** (today's low). A break confirms continuation.
- **Support 2: 182.29** (200 SMA) — the line in the sand; ATR (3.25) × 1 below today's close = 181.15, i.e. the 200 SMA is *within one average day's range*.
- **Support 3: 180.17–180.93** (four January lows) and **178.67** (lower Bollinger band).

### Trade construction
1. **Trend-following long (do not chase).** The setup is not live. A long is only justified by a **daily close above ~189.6** reclaiming the 10 EMA/VWMA shelf, ideally with MACD histogram turning positive again; stop 1.0–1.5 ATR below entry (≈3.2–4.9 points) and target the 50 SMA/195.2. Risk: you are buying a lower high unless 195.75 is exceeded.
2. **Mean-reversion long (higher expectancy).** Wait for price to probe **182.3 (200 SMA) → 180.2** with **RSI ≤ 30** and a reversal bar (close in the upper third of the range on above-average volume). Stop below **178.6** (lower band) — a close beneath the lower band after compression would invalidate the swing thesis. This is the higher-quality entry because it stacks the 200 SMA, the January low cluster, and the ATR-1 level.
3. **Tactical short (for those trading the prevailing flow).** Only on a **failed retest of 187.8–189.6** (rally stopping without a close above it), stop 1×ATR above the entry (~3.25 pts, so roughly above 191.5 if entered at 188.3), first target 182.3, second 180.2. The 1/31 close-on-the-low argues that continuation toward 182.3 is the higher-probability path, but the RSI at 39.6 and the still-rising 200 SMA argue against pressing shorts aggressively below 182.
4. **Position sizing.** With ATR = 3.249 (1.76% of spot), a 1-ATR stop is *tight* by recent standards — ATR rose 26% in a month, so size positions roughly **25% smaller** than at December's volatility to keep risk-per-trade constant. Wider (1.5–2 ATR) stops are more appropriate given the flat lower band and the possibility of a gap open.

### Event risk
AAPL's fiscal Q1 report is widely expected in the first days of February per public calendars — **this is not verifiable from the tools provided and should be independently confirmed.** If that event is imminent, note that the technical setup (compressed bands, expanding ATR, failed MACD crossover, six down days) is precisely the configuration in which a binary gap can invalidate any stop. Reducing exposure ahead of an unhedged binary event is the risk-management conclusion, not a directional one.

### What would invalidate this read
- A daily close above **190.8 (50 SMA)** on above-average volume → short-term bearish thesis dead, trend resumption toward 195–198.
- A drop below **178.6 (lower Bollinger band)** on expanding volume → the 200 SMA has failed; the 50>200 bullish regime itself comes into question.
- A *volume spike* (e.g., >80M, matching 1/2's 82.49M) down here would actually be constructive for a bounce — capitulation is what's currently missing.

---

## 7. Summary table

| Dimension | Reading (2024-01-31) | Change / Context | Interpretation | Action |
|---|---|---|---|---|
| Close | 184.40 | −5.52% from 195.18 (1/23); 6 straight down closes | Short-term downtrend, accelerating (−1.92%, −1.94% last two days) | No new longs |
| 10 EMA | 189.63 | Peaked 191.41 (1/29), now falling 2 sessions | Price 2.76% below; lost 1/30 | Resistance |
| 50 SMA | 190.82 | Rising 177.78 (11/22) → 190.93 (1/30), flattening | Price 3.37% below; medium trend rolling over | Ceiling of repair zone |
| 200 SMA | 182.29 | Rising steadily, +7.8% since 11/22 | Price still +1.16% above; golden-cross (50>200 by 4.7%) intact | Last bull line |
| MACD / Signal | 0.0913 / 0.2346 | Histogram −0.1434; peaked +1.128 (1/25) | **Failed bullish crossover** on 1/31 | Bearish |
| RSI | 39.60 | 62.62 (1/23) → 39.60; prior low 28.79 (1/5) | Below 50, **not oversold** | Wait for 30 before counter-trend long |
| Bollinger | mid 187.83 / up 196.98 / low 178.67 | Width 9.75% of mid, narrowing; lower band flat ~178.7 for 2 weeks | Mid-band rejection; directional move from compression | Target 178.7 on breakdown |
| ATR | 3.249 | +26% since 12/29 (2.57) | 1.76% of spot; 1 ATR below close = 181.15 ≈ 200 SMA | 1–1.5 ATR stops; size −25% |
| VWMA | 189.33 | Rising 185.25 (1/18) → 189.40 (1/30), now flat | Price 2.61% **below** volume-weighted cost basis | Bearish participation |
| Volume | 55.47M | ≈ in line with ~56.5M Jan average; no spike | Rising volume on declines = distribution, **no capitulation** | Favor time/lower prices over V-bottom |
| **Net thesis** | — | — | **Long-term uptrend, short-term distribution** | Defensive; buy 180–182 with RSI≤30 or buy 189.6 reclaim; do not buy 184 mid-range |