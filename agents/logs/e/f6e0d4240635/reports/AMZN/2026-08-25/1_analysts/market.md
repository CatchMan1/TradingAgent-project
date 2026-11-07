# AMZN — Technical & Trend Assessment
**As of the verified session: 2026-08-25 (close 261.06)** · Horizon: swing (2–8 weeks) with strategic overlay

---

## 0. Data integrity note (read first)

- The OHLCV series from `get_stock_data` and the `get_verified_market_snapshot` agree exactly on the latest row: **2026-08-25 O 262.51 / H 263.89 / L 259.83 / C 261.06, volume 25,550,200**. All exact price/level/indicator claims below come from the verified snapshot; the extended series is used only for *sequence and structure*.
- Internal consistency check passed: snapshot MACD 2.805783 − MACDh −1.460011 = 4.265794 = snapshot MACDs ✓; Boll middle 264.422499 = (291.424942 + 237.420056)/2 ✓.
- **Flagged discrepancy:** the snapshot reports `mfi = 0.354512`. On a 0–100 scale that would be extreme oversold, which directly contradicts RSI 51.6, price ~9% above the 200-SMA, and a positive MACD. It looks like a normalized (0–1) or malformed value. **I am not using MFI in this analysis** and would not act on it until the vendor is reconciled.
- `technical_total_return_index` equals close on every row → no dividends in the window (consistent with AMZN's no-dividend policy), so price and total-return analysis are identical here.

---

## 1. The dominant event: a post-earnings repricing, then a cooldown

The shape of this chart is best understood through one event. On **2026-07-30 (close 235.50, volume 101.8M)** price closed the session, and on **2026-07-31 AMZN opened at 265.00 and closed at 271.58 on 129.1M shares** — a **+15.3% single-session repricing that left an unfilled gap between 239.82 (7/30 high) and 265.00 (7/31 open)**. Follow-through on **2026-08-03** took the close to **284.02** (intraday high **287.20**) on 90.8M shares. That is +25.3% from the 2026-07-29 close of 226.65 in three sessions.

Everything since is the market digesting that move:

- Peak closing high: **284.02 (2026-08-03)**; peak intraday high **287.20 (2026-08-03)**.
- Trough of the pullback: **257.04 intraday (2026-08-21)**, closing low **258.63 (2026-08-21)**.
- Current close 261.06 = **−8.1% from the 284.02 closing high**, **−9.1% from the 287.20 intraday high**.
- Against the 7/29→8/3 leg (226.65 → 284.02, +57.37 pts), the **38.2% retracement sits at ~262.11 and the 50% at ~255.34**. Price at 261.06 has just undercut the 38.2% level but sits well above the 50%. This is a *shallow/orderly* digestion, not a trend break.

Critically, **the gap is nowhere near filled** — the lowest print since the gap is 257.04, which is still ~7% above the 265.00 gap origin. The gap-fill zone (~235–240) is a tail-risk scenario, not a base case.

---

## 2. Trend structure: short-term down, intermediate and long-term up

**Long term (200-SMA = 238.44): intact and rising.** The 200-SMA has climbed monotonically from 234.66 (2026-07-29) and 224.34 (2026-02-26) to 238.44 today. Price is **+9.5% above it**. The 50-SMA (250.59) crossed above the 200-SMA between 2026-05-04 (226.04 vs 227.62, below) and 2026-05-06 (228.73 vs 228.08, above) — a **golden cross roughly 2026-05-05/06** that remains firmly in force, with the 50/200 spread now **+12.15 pts (+5.1% of the 200-SMA)** and *widening*.

**Intermediate (50-SMA = 250.59): turning back up.** The 50-SMA bottomed at **246.38 on 2026-07-30** and has risen every session since to 250.59. Price is **+4.2% above it**. This is the single most important structural fact for the bull case: the earnings gap lifted the 50-SMA off its decline, so the medium-term trend is now *supporting* price from below rather than capping it.

**Short term (10-EMA = 262.34): bearish, but flattening.** The 10-EMA peaked at **267.18 (2026-08-12)** and has declined to 262.34. Price (261.06) is **−0.49% below it**. However, the rate of decline has decelerated sharply: 266.05 (8/14) → 264.15 (8/18) → 262.75 (8/21) → 262.63 (8/24) → 262.34 (8/25) — i.e. the 10-EMA is now falling ~0.1–0.2 pts/day versus ~0.6 pts/day in mid-August. **A close above 262.34 is the first mechanical repair signal.**

**Price sequence confirms a short-term descending structure:** lower highs 287.20 (8/3) → 282.79 (8/5) → 280.14 (8/10) → 278.84 (8/11) → 273.46 (8/12) → 266.40 (8/19) → 263.89 (8/25); lower lows 270.73 (8/5) → 267.10 (8/12) → 264.71 (8/13) → 262.42 (8/14) → 258.34 (8/17) → 257.04 (8/21).

**But the lows have stopped making progress:** 257.04 (8/21) → 259.05 (8/24) → 259.83 (8/25) = three consecutive higher lows, inside a 4-session box of roughly **257.0–263.9**. Combined with a flattening 10-EMA, this is the signature of a **coiling base** rather than accelerating distribution.

---

## 3. Momentum: the corrective impulse is losing force

**MACD line = 2.806, signal = 4.266, histogram = −1.460.** The MACD line ran from 8.432 (2026-08-11) down to 2.806 — a decisive cooling of momentum — and crossed below its signal on **2026-08-17** (histogram +0.392 on 8/14 → −0.310 on 8/17). Two important nuances:

1. **The MACD line is still positive (2.81).** This is a *pullback within an uptrend*, not a momentum regime flip. The same MACD line was −6.88 on 2026-06-26, so the intermediate trend is far healthier than it was in June.
2. **The histogram is rolling over at a shallower level:** −1.538 (8/21) → −1.472 (8/24) → −1.460 (8/25). Two consecutive sessions of narrowing negative bars = downside acceleration is fading. This is an *early* stabilization tell, not yet a signal — a histogram recross above zero would be the trigger.

**RSI = 51.59 — a full reset, and bullish-neutral.** RSI hit **72.23 on 2026-08-03** (overbought after the gap) and has bled to 49.74 (8/21) before ticking back to 51.59. That is a textbook **overbought washout to neutral without a price collapse** — the kind of internal reset that typically precedes continuation in an intact uptrend. For context, the June correction drove RSI to 32.46 (2026-06-10) and 33.31 (2026-07-29), so this pullback has been far milder in momentum terms. There is **no confirmed bullish divergence** (the 8/21 price low came with a lower RSI than the 8/18 close-to-close comparison), so I will not claim one.

---

## 4. Volatility: a classic post-event squeeze is forming

**ATR = 7.05, down from a 9.98 peak on 2026-08-05** (−29% in 14 sessions). ATR is now **2.70% of price**, which normalizes position sizing after the earnings inflation.

**Bollinger (verified snapshot): mid 264.42, upper 291.42, lower 237.42.** The squeeze evidence is unusually clean:

- Band width compressed from **81.42 pts (8/10: 296.99 − 215.57)** to **54.00 pts (8/25: 291.42 − 237.42)** — a **34% contraction in 11 sessions**.
- The **upper band has turned down** (296.99 on 8/19 → 291.42 on 8/25) while the **lower band has turned up sharply** (215.57 on 8/10 → 237.42 on 8/25).

Bands pinching this fast after an event typically resolve in a directional expansion. **%B = (261.06 − 237.42) / 54.00 = 0.44** — price sits just below the middle band (264.42), i.e. mildly weak within a neutral range. Note the middle band (264.42) is essentially the 20-SMA and clusters with the VWMA (266.29) and the 8/19 high (266.40) into a **263–267 resistance shelf**.

---

## 5. Volume: no distribution, but no demand either

This is where I am most constructive. Volume during the entire pullback has been **drying up**:

- Event volume: 101.8M (7/30) → 129.1M (7/31) → 90.8M (8/3).
- Pullback volume: 45.1M (8/5) → 30.7M (8/6) → 27.3M (8/14) → 28.4M (8/20) → 35.7M (8/21) → 28.1M (8/24) → **25.55M (8/25)**.
- My calculation from the tool rows: ex-earnings baseline for this 21-session window is **~36.5M shares/day**; the last five sessions average **~30.4M**. The 2026-08-25 print of **25.55M is the lowest single-session volume since 2026-04-06 (25.39M)**.

A ~9% pullback on volume running 15–30% below baseline is **not distribution** — sellers are not pressing. The corollary is that buyers are also absent, which is exactly what a squeeze builds out of.

**VWMA = 266.29 vs price 261.06 (−1.96%):** the volume-weighted cost basis since mid-July sits *above* price. Because the VWMA window is dominated by the 129M-share and 90.8M-share sessions printed at 271.58 and 284.02, this line is a direct proxy for **overhead supply**. It is worth noting that VWMA has already rolled over from its 272.05 peak (8/20) to 266.29 and will keep decaying as those heavy gap-day sessions age out of the lookback window (roughly the turn of the month). **Translation: the resistance ceiling is descending toward price on its own.** Tactically, don't chase a rally into 266–272; that zone is where trapped post-gap buyers get even.

---

## 6. What I selected and why (8 indicators, non-redundant)

| # | Indicator | Value (2026-08-25) | Why it earns a slot in *this* context |
|---|---|---|---|
| 1 | close_10_ema | 262.34 | Immediate pivot; the flattening of this line is the earliest evidence the 3-week slide is ending |
| 2 | close_50_sma | 250.59 | Medium-term trend + dynamic support; inflected up post-gap (246.38 low on 7/30) |
| 3 | close_200_sma | 238.44 | Regime anchor; confirms golden cross intact and +9.5% buffer |
| 4 | macd | 2.806 | Still positive = the pullback is corrective, not a trend reversal |
| 5 | macdh | −1.460 | Best available read on *deceleration* (−1.538 → −1.472 → −1.460) |
| 6 | rsi | 51.59 | Confirms overbought condition fully washed out without price damage |
| 7 | atr | 7.05 | Post-earnings volatility normalization → correct stop distance & size |
| 8 | vwma | 266.29 | Only selected indicator that captures **volume-weighted overhead supply** from the gap |

Deliberately excluded: `macds` (near-perfect redundancy with `macd`/`macdh`), `boll` bands (used as a verified overlay above rather than as a 9th selection — the middle band is just a 20-SMA), `mfi` (data integrity failure), and stochastics (redundant with RSI in a neutral-trend regime).

---

## 7. Actionable framework

### Scenario A — Base case (my lean): squeeze resolves upward, 55%
**Trigger:** daily close **above 262.34 (10-EMA)**, confirmed by a close **above 264.42 (Boll mid)** and MACD histogram turning positive.
**Path:** 266.3–266.4 (VWMA / 8-19 high) → 272–274 (8/5–8/7 congestion) → 278–280 (8/10–8/11 highs) → 284–287 (8/3 highs).
**Confirmation required:** up-day volume **> ~36M** (above the ex-earnings baseline). Without it, treat rallies as suspect.
**Entry/stop:** staged entry on the 264.42 reclaim; stop **253.00** (below the 8/21 low with buffer, ~1.15 ATR). Risk ≈ 11.4 pts ≈ 4.3% from a 264.4 fill.

### Scenario B — Neutral coil (30%)
**Range: 257.0–266.4.** The 4-session box (257.04–263.89) with ATR compressing and the lowest volume since April says this is genuinely possible. Do nothing in the middle of the range; buy the lower third, trim the upper third. Watch the Bollinger width — a break below ~50 pts of width raises the odds of a violent resolution.

### Scenario C — Bear case (15%)
**Trigger:** daily close **below 257.04** (the 8/21 low).
**Targets, in order:** **250.59 (50-SMA)** and **248.57 (61.8% retrace of the 226.65→284.02 leg)** — these two levels **converge into a single high-conviction support zone at ~248.5–250.6**. A daily close below 248.5 breaks both the medium-term trend and the Fibonacci structure, opening **238.44 (200-SMA)** and then the unfilled gap toward **235.50**.
This scenario requires *seeing* the break — the volume profile argues against it, but the short-term trend is objectively down until 262.34 is reclaimed, so it must be respected.

### Risk management specifics
- **ATR-based stop:** minimum 1.5 × ATR = **10.6 pts** from entry; a volatility stop on a 261 entry sits near **250.5** (which conveniently ≈ the 50-SMA).
- **Position sizing:** with a 4.3% structural stop and a 1% account risk budget, notional exposure ≈ **23% of equity**. If you use the tighter 253 stop, do not exceed that notional — the tighter stop is inside normal daily noise (1.15 ATR) and will be hit on noise.
- **Invalidation hierarchy:** 262.34 (minor) → 257.04 (moderate) → 248.57/250.59 (major) → 238.44 (trend break).
- **Event risk:** the entire structure is post-earnings. There is no scheduled binary in the immediate window per this data set, but any re-rating of the 7/30 catalyst would void the technical read.

---

## 8. Summary table

| Dimension | Reading (2026-08-25) | Signal | Key level / action |
|---|---|---|---|
| **Last session** | O 262.51 / H 263.89 / L 259.83 / C 261.06, vol 25.55M | Closed below open, lower half of range | Low-conviction day; lowest volume since 2026-04-06 |
| **Short-term (10-EMA)** | 262.34; price −0.49% below | Bearish but flattening | First repair trigger = close > 262.34 |
| **Medium-term (50-SMA)** | 250.59, rising since 246.38 (7/30) | Bullish | Price +4.2%; confluence support 248.5–250.6 |
| **Long-term (200-SMA)** | 238.44, rising | Bullish | Golden cross since ~2026-05-05/06; price +9.5% |
| **MACD / Signal / Hist** | 2.806 / 4.266 / −1.460 | Corrective, decelerating | Line still >0; hist. 3rd session narrowing; zero-recross = trigger |
| **RSI** | 51.59 (from 72.23 on 8/3) | Neutral/bullish-neutral | Overbought fully reset without price damage |
| **Bollinger** | Mid 264.42 / UB 291.42 / LB 237.42, %B 0.44 | Squeeze | Width 81.4 → 54.0 pts (−34% in 11 sessions) |
| **ATR** | 7.05 (from 9.98 on 8/5) | Volatility normalizing | 2.70% of price → ~23% max notional at 1% risk |
| **VWMA** | 266.29; price −1.96% | Overhead supply | Resistance ceiling decaying toward price ~month-end |
| **Volume trend** | ~30.4M (5d) vs ~36.5M baseline | No distribution | Demand needs > 36M on up days to validate |
| **Structure** | Lower highs 287.20→263.89; higher lows 257.04→259.83 | Coiling | 4-session box 257.0–263.9 |
| **Fib of 7/29→8/3 leg** | 38.2% = 262.11 (just lost); 50% = 255.34; 61.8% = 248.57 | Shallow digestion | 61.8% ≈ 50-SMA = major support |
| **Unfilled gap** | 239.82 → 265.00 (7/30→7/31) | Structural support void | Tail-risk fill target ~235.50 |
| **Data caveat** | `mfi` 0.354512 | **Unreliable** | Contradicts RSI/price; do not act on it |

**Bottom line:** AMZN is in a **bullish intermediate trend undergoing a normal, low-volume, volatility-compressing consolidation**. The primary trend (50 > 200, both rising) and the absence of distribution volume both argue for resolution higher, but the short-term trend is objectively down and price sits below the 10-EMA, the 20-SMA/Bollinger mid, and the volume-weighted cost basis. The tradeable edge is **patience**: buy confirmation of a 264.42 reclaim with expanding volume, or accumulate into the 248.5–250.6 confluence, and avoid the 266–272 overhead-supply zone in between.