# GOOGL (Alphabet Inc.) — Technical Analysis Report
**Analysis date: 2026-07-17 | Last verified close: $346.77**

---

## 1. Data Integrity Note

All indicator values cited below were cross-checked between `get_indicators` and the `get_verified_market_snapshot` (2026-07-17). **No discrepancies were found** — e.g., close_50_sma 370.587, RSI 42.23, MACD −2.105, ATR 11.689, boll_lb 337.812, vwma 358.203 match to the decimal. The snapshot is treated as the source of truth for all OHLCV/level claims.

---

## 2. Market Context: What Kind of Regime Is GOOGL In?

GOOGL is **not** in a clean trend or a clean range — it is in a **mature, high-level uptrend that has transitioned into a volatile, downward-sloping corrective phase**, with the long-term trend still intact but the intermediate trend now hostile.

Three timeframes disagree, and that disagreement *is* the trade:

| Timeframe | Evidence | Verdict |
|---|---|---|
| **Long-term (annual)** | close_200_sma = **321.66**, rising ~$0.5/session for 45 consecutive sessions (292.33 on 2026‑05‑18 → 321.66 on 2026‑07‑17). Price is **+7.8% above** it. 50 SMA (370.59) is **+15.2% above** the 200 SMA (golden-cross configuration, no crossover risk) | **Bullish / intact** |
| **Intermediate (quarterly)** | Price **−6.4% below** close_50_sma (370.59). 50 SMA rolled over: peak 372.80 on 2026‑07‑13 → 370.59 on 2026‑07‑17. Price has closed below the 50 SMA every session since 2026‑06‑17 | **Bearish / rolling over** |
| **Short-term (daily)** | Price −2.9% below close_10_ema (357.14), −3.2% below VWMA (358.20), MACD just crossed below its signal (hist −0.049), RSI collapsed 56.9 → 42.2 in two sessions | **Bearish momentum shock** |

**The decisive price fact:** GOOGL closed at **370.92 on 2026‑07‑15**, having rallied +9.9% off the 2026‑06‑26 close of 337.39. On 2026‑07‑16 it opened at 373.06, printed a high of **375.27**, then closed at **354.46** on **41.16M shares** (roughly double the 15–28M share sessions of the prior week) — a wide-range bearish reversal candle. On 2026‑07‑17 it gapped down (open 346.00) and closed **346.77**, with a low of **341.36**. Two-session decline: **−6.5%**.

Critically, the 7/15 high of **373.65** stopped almost exactly at the **50‑day SMA (372.00 on 7/15)** and inside the **Bollinger upper band (373.99)**. The July rally was a textbook **failed retest of the 50 SMA from below**. That is a bearish structural signal, not a random dip.

---

## 3. Indicator Selection & Rationale (8 indicators)

I deliberately chose a set that separates **trend** from **momentum** from **volatility** from **participation**, avoiding redundancy (I omitted macds as a standalone because macdh already encodes the crossover state, and omitted boll_ub from the primary set because the snapshot value was sufficient for the 7/15 rejection test):

1. **close_50_sma** — the exact level that rejected price on 7/15; the intermediate trend arbiter.
2. **close_200_sma** — strategic bull/bear dividing line and the anchor for risk placement.
3. **close_10_ema** — captures the short-term momentum break in real time.
4. **macd** — momentum regime (positive/negative territory), which has been **negative since 2026‑06‑09**.
5. **macdh** — timing: reveals the 7/2–7/16 histogram recovery and its **fresh flip to negative on 7/17**.
6. **rsi** — overbought/oversold capacity: at 42.2 there is still downside room before capitulation readings.
7. **boll_lb** — defines the current statistical floor (~337.8) which sits almost exactly on the June support cluster.
8. **atr** — position sizing and stop distance in an elevated-volatility tape.
9. **vwma** (bonus/volume confirmation) — the only volume-weighted view; it is rising while price falls, a distribution tell.

---

## 4. Detailed Indicator Read

### 4.1 Moving averages — a compression/correction inside a bull structure
- **Price 346.77 < 10 EMA 357.14 < VWMA 358.20 < 50 SMA 370.59** — full bearish short-term stacking.
- The **50 SMA is still 15.2% above the 200 SMA** and the 200 SMA is rising one-directionally. Historically-wide MA spreads mean the intermediate mean is far from the long-term mean — i.e., the market is **mean-reversion-prone toward the 200 SMA** if the 50 SMA decisively fails.
- The 50 SMA itself is flattening (370.42 on 7/1 → 372.80 peak on 7/13 → 370.59 on 7/17). Flattening of a 50 SMA after a 5-month advance typically precedes either a multi-week base or a trend break. **Watch the 200 SMA at 321.66: as long as it holds, dips are corrective, not cyclical.**

### 4.2 MACD — a failed bullish repair
- MACD line bottomed at **−7.35 (2026‑06‑26)**, repaired to **−0.78 (2026‑07‑15)** — a strong, sustained improvement.
- But the **MACD line never crossed into positive territory**, even at the July price peak. That is a classic **bearish divergence in trend quality**: price made a higher high vs. mid-June (373.65 vs 376.00 on 6/16 — roughly a double top) while MACD stayed negative.
- The **histogram peaked at +1.83 on 2026‑07‑07**, decayed to +0.60 by 7/13, spiked to +1.48 on 7/15, then collapsed to **−0.049 on 2026‑07‑17** — a **fresh bearish MACD/signal crossover on the last session**. This is the single most actionable fresh trigger in the dataset.

### 4.3 RSI — weak but *not* washed out
- **42.23** on 7/17 (from 56.87 on 7/15). Not oversold.
- Reference points from tool data: RSI reached **33.27 on 2026‑06‑26** (the June low day, close 337.39), and **70.30 on 2026‑05‑18** (near the May peak). So **symmetric downside room of roughly 9 RSI points exists before the market reaches its June oversold footing.**
- Nuance: RSI at 56.87 on 7/15 was a *higher* high than RSI 52.52 on 6/16 while price made a marginally lower high (373.65 vs 376.00) — a mild **positive divergence** that is now being invalidated by the 7/17 collapse. Do not trade off it; it failed.

### 4.4 Bollinger Bands — price being squeezed toward the floor
- Middle (20 SMA) **355.90**, upper **373.99**, lower **337.81**. Bandwidth = **10.2% of the middle line** — wide, consistent with a high-ATR tape.
- Price at 346.77 sits in the **lower third** of the band, **2.7% above the lower band (337.81)**.
- **The lower band (337.8) and the June support cluster nearly coincide** — 6/26 close 337.39 / low 330.20; 6/29 low 340.67; 6/24 low 341.93; 6/23 low 340.20; 7/17 low **341.36**. This forms a dense **340–342 pivot with a 337.5–338.5 band floor beneath it**. That is the highest-probability demand zone in the visible data.

### 4.5 ATR — volatility re-expanding during the decline
- ATR **11.69** = **3.37% of close**. It compressed as low as 10.31 on 7/14, then expanded on 7/16 (+11.58) and 7/17 (+11.69) — **volatility expansion on down days** confirms the move is impulsive, not drift.
- Practical translation: a 1×ATR stop below 346.77 ≈ **335.1**; 2×ATR ≈ **323.4** — which lands just above the 200 SMA (321.66). The 200 SMA is the natural "max pain" risk line.
- With ATR at ~3.4% of price, **position size should be roughly 60–70% of what it was in mid-July** (ATR 10.3), holding dollar risk constant.

### 4.6 VWMA & volume — the distribution tell
- VWMA **358.20** and *rising* (350.15 on 7/13 → 353.95 on 7/16 → 358.20 on 7/17) **while price falls**. Rising volume-weighted average price against falling price means the heaviest recent volume transacted at *higher* prices — i.e., sellers are distributing into the July bounce, and buyers are now underwater. **Price is 3.2% below VWMA: bearish confirmation.**
- Volume evidence: 2026‑07‑16 traded **41.16M shares** vs. 15.9M (7/13), 18.3M (7/14), 28.3M (7/15). The largest single-day volume in the last four months is **114.7M on 2026‑06‑26** — a down day that closed 7.4% above its intraday low (low 330.20, close 337.39), which reads as capitulation/flush absorption.
- **Caveat (flagged, not invented):** a −4.4% single-session drop on 7/16 with ~2× normal volume implies a catalyst (fundamental/news). The provided data contains **no explanatory information**; I will not speculate on its cause.

### 4.7 Longer-horizon structure for context
- 2026 low close: **273.50 (2026‑03‑30)**; the April 30 gap-up session (open 374.07 from prior close 349.94, close **384.80, +10.0%**, volume **72.0M**) launched the May highs: closing high **400.80 (2026‑05‑08)**, intraday high **408.61 (2026‑05‑18)**.
- From that May peak, GOOGL has now retraced to 346.77 = **−13.5%** from the 5/8 closing high. This is a **textbook corrective drawdown within a bull trend**, but the character of the correction (lower highs at 408.61 → ~402 (5/13 close) → 376.00 (6/16) → 375.27 (7/16)) is a clean **descending sequence of highs**. Until a daily close above ~376, the pattern is "lower highs."

---

## 5. Actionable Framework

**Bias: tactically bearish / defensive; strategically still constructive.** The trend of the last 6 weeks is down-and-sideways momentum, but the 200 SMA (321.66) and 340–342 pivot are both intact floors.

### Scenario A — Continuation toward the band floor (base case, ~45%)
Triggers: daily close below **341.36** (7/17 low). Targets: **337.8** (boll_lb) → **330.2** (6/26 low). Stop/invalidation: reclaim of **347–352** on declining volume.

### Scenario B — Support holds, base-building (also ~35%)
The 340–342 zone is the densest confluence in the data (June lows + July low + lower Bollinger band just beneath). A close back above **10 EMA 357.1** would neutralize the immediate breakdown; a close above **VWMA 358.2** confirms real demand. First objective then **370.6 (50 SMA)**.

### Scenario C — Trend-repair resolution (low probability, ~20%, but high payoff)
Requires a daily close **above 375.3–376.0** (the 7/16 high and 6/16 high — a confluence double-top neckline) AND MACD hist back above +1.0. That would open the 5/18 high of **408.61**.

### Hard risk management
- **Do not treat 346.77 as "cheap."** RSI 42 and price 2.7% above the lower band mean the market is mid-range, not exhausted.
- Any long attempted at 340–342 needs a stop materially below **335.1** (1×ATR) — with ATR at 11.69 the whipsaw risk is high; a close below 337.8 invalidates the zone.
- Any short needs a stop above the 50 SMA (**370.6**), because that level is the last line of defense for the intermediate trend and a reclaim would be a regime change.
- Strategic accumulation zone, if the correction deepens: **321.7–329.2** (200 SMA + June low 330.20 + 2×ATR).

---

## 6. Key Points Summary

| Item | Value / Observation | Signal |
|---|---|---|
| **Last close (2026‑07‑17)** | **346.77** (O 346.00 / H 348.52 / L 341.36), volume 29.96M | Bearish continuation day, gap-down |
| **2-session move** | 370.92 (7/15) → 346.77 (7/17) = **−6.5%** | Impulsive decline |
| **close_50_sma** | **370.59**, rolling over from 372.80 peak (7/13); rejected price at 7/15 high 373.65 | Bearish — price below resistance |
| **close_200_sma** | **321.66**, rising every session; price +7.8% above | Bullish — long-term trend intact |
| **close_10_ema** | **357.14**; price 2.9% below | Bearish short-term |
| **MACD / Signal / Hist** | −2.105 / −2.056 / **−0.049** | Fresh bearish crossover on 7/17; MACD never went positive during July rally |
| **RSI** | **42.23** (from 56.87 on 7/15); June low reading was 33.27 | Weak, not oversold — room to fall |
| **Bollinger** | mid **355.90** / ub 373.99 / **lb 337.81** | Price in lower third; floor near June support |
| **ATR** | **11.69** (3.37% of price), expanding on down days | Volatility expansion = high risk; size down ~30–40% |
| **VWMA** | **358.20** and *rising* while price falls | Distribution — heavy volume transacted above price |
| **Support zones** | 341.4–343.7 (June/July lows) → **337.8** (band floor) → **330.2** → **321.7** (200 SMA) | Layered demand |
| **Resistance zones** | 355.9 → **357.1–358.2** (10 EMA/VWMA) → **370.6** (50 SMA) → **375.3–376.0** (double top) → 408.6 | Layered supply |
| **Structural read** | Sequence of lower highs 408.61 → 376.00 → 375.27 | Correction, not yet a reversal |
| **Framework** | Tactically bearish, strategically constructive; tactical short bias valid below 357–358, invalid above 370.6 | Neutral-bearish |
| **Indicators used** | close_50_sma, close_200_sma, close_10_ema, macd, macdh, rsi, boll_lb, atr (+vwma) | Non-redundant, multi-factor |

**Bottom line:** GOOGL's trend structure is unambiguous — a bull market whose intermediate engine has stalled. The July rebound failed precisely at the 50‑day SMA (370.6), and the 7/16–7/17 two-day, high-volume, high-ATR reversal has flipped MACD back negative while pushing price below the 10 EMA and rising VWMA. The 340–342 pivot and the 337.8 Bollinger floor are the first real test; **337.8 and 321.7 are the two levels that define whether this is a buying opportunity or a trend break.** Trade small, respect the ATR, and wait for the 341.36/337.8 resolution rather than anticipating it.