# AAPL — Technical & Trend Assessment
**Analysis date: 2026-09-15 | Latest settled session: 2026-09-15 | Close: $331.34**

---

## 1. Verified Data Baseline

I first pulled the daily OHLCV history (2026-02-15 → 2026-09-15, 146 rows) and then ran the deterministic `get_verified_market_snapshot` for 2026-09-15. **The two sources are fully consistent** — the snapshot's indicator values match the series returned by `get_indicators` to the decimal (RSI 61.309, MACD 4.3044, Signal 2.7078, Bollinger mid 319.2710 / upper 335.2531 / lower 303.2889, ATR 7.5518, VWMA 322.1473). No discrepancy to flag.

**Latest bar (2026-09-15):** Open 330.14 · High 331.78 · Low 328.35 · **Close 331.34** · Volume 31,748,200
**Prior bar (2026-09-14):** Close 333.08 · High 335.50
**Recent swing high:** 336.22 intraday on 2026-09-11 (close 332.27)
**2026 visible-window high:** 344.57 intraday on 2026-07-29 (close 338.19)

---

## 2. Market Regime: Intact Uptrend, Mid-Cycle Re-Acceleration

The dominant structure is a **primary uptrend with a completed corrective phase and a fresh leg higher.**

**Primary trend (200-day):** Close 200-SMA = **285.51**, rising every session in September (~+0.26/day), e.g. 283.07 on 09-01 → 285.51 on 09-15. Price at 331.34 sits **+16.05% above** the 200-SMA. The 50-SMA (318.84) is **+11.67% above** the 200-SMA and also rising (~+0.7/day, from 312.94 on 09-01). This is a wide, positively-sloped moving-average stack — the hallmark of a durable uptrend, not a topping pattern. No death-cross risk is remotely present.

**Intermediate trend (50-day):** The 50-SMA bottomed at 309.08 on 2026-08-17 and has climbed uninterrupted since (309.13 → 318.84). Price **reclaimed the 50-SMA on 2026-08-28** (close 319.70 vs 50-SMA 312.00) and has held above it for all 12 sessions since.

**Short-term trend (10-day EMA):** 325.38, rising steeply since 09-09 (318.26 → 319.77 → 322.05 → 324.05 → 325.38). Price is **+1.83% above** it. The 10-EMA crossed **above** the 50-SMA around 2026-09-08/09-09 — a short-term bullish alignment signal that is still only ~6 sessions old.

**Structural read of the recovery:** The higher-low / higher-high sequence is clean and tool-verifiable:
- Higher low: 2026-08-12 intraday low **300.57** → 2026-09-09 intraday low **309.90** (+3.1%)
- Higher highs: 2026-08-19 high **319.28** → 2026-09-01 high **327.30** → 2026-09-11 high **336.22**

The 2026-07-31 collapse deserves attention because it defines the overhead supply. On 07-30 AAPL closed 333.43; on 07-31 it opened **304.81** and closed **308.91** (−7.37%) on 132.5M shares — the ranges do not overlap, so a genuine unfilled price gap exists between **304.81 and 333.43**. The stock has now recovered to **331.34, i.e. into the top of that gap**. This is the single most important tactical fact in the report: the market is retesting the origin of the July breakdown. A close above 333.43 would fully repair that event.

---

## 3. Momentum: Confirmed Bullish, Not Yet Overbought

**MACD:** 4.304 vs Signal 2.708 → **Histogram +1.597**.
- The MACD line bottomed at **−2.676 on 2026-08-17**, the signal at **−1.290 on 2026-08-25**.
- The bullish crossover occurred **2026-08-31** (MACD +0.297 vs Signal −0.680), the MACD line crossed zero on **2026-09-01** (1.209), and the signal line crossed zero on **2026-09-02** (0.137).
- The histogram has now printed positive for **11 consecutive sessions** and at **1.597 is the highest reading since 2026-07-28 (1.31)**. It did briefly compress on 09-08/09-09 (0.934 → 0.426) before re-expanding — that is a "dip-buy" signature rather than a fade.
- Caveat: the histogram is still below the 2026-07-17 reading of 3.337, so this is a re-acceleration, not a blow-off thrust.

**RSI:** **61.31**, down from 63.32 on 09-14 and 62.79 on 09-11. This is the key nuance: price is near its swing high while RSI is **not** overbought. The July rally died with RSI at 71.65 on 07-17; today there is roughly 9 points of headroom before the 70 threshold. The RSI path also shows a constructive higher low (40.22 on 08-12 → 49.35 on 09-09) that mirrors the price higher low. RSI 61 in a rising 50/200 stack should be read as **trend continuation fuel, not exhaustion**.

**Interpretation:** Momentum and trend are aligned. There is no bearish divergence between price and either RSI or MACD in the visible data. The one yellow flag is that the 09-10→09-11 push was fast (+3.56% then +1.75%), which invites short-term consolidation.

---

## 4. Volatility & Bollinger Structure: Compression Before Expansion

- **Bollinger middle:** 319.27 · **Upper:** 335.25 · **Lower:** 303.29
- **Band width:** 31.96 points = **10.0% of the mid-band**. On 2026-08-12 the width was 52.07 points and on 2026-07-29 it was 47.48. Bands have contracted ~39% from the August peak-width reading — a textbook **volatility contraction** following the July/August event risk.
- **%B position: 87.8%** — price is in the upper quintile of the band but has **not** closed decisively outside it (09-11 closed 332.27 vs an upper band of 331.86, a marginal 0.12% overshoot; 09-14 and 09-15 closed back inside). This is a "walking the upper band" setup that historically resolves in the direction of the prevailing trend, but it requires confirmation.
- **ATR: 7.552** (2.28% of price). ATR peaked at 9.872 on 2026-07-31 (post-gap), compressed to 7.104 on 2026-08-27, and has ticked back up to 7.55 as the September advance began. Rising ATR + rising price = healthy expansion, not distribution.
- **Risk framing:** 1×ATR below the close = **323.79**; 2×ATR = **316.24**.

---

## 5. Volume / Participation

- **VWMA: 322.15.** Price is **+2.85% above** the volume-weighted average — volume-weighted holders are in profit and the VWMA is turning up (317.04 on 09-09 → 322.15 on 09-15). That is genuine accumulation, not a low-volume drift.
- The breakout sequence was volume-backed where it mattered: **09-10 +3.56% on 70.0M**, **09-11 +1.75% on 50.7M**, and the 09-09 shakeout on 65.6M.
- **The caution:** participation is fading on the last two bars — 39.3M on 09-14 and **31.7M on 09-15**, versus a rough 20-session average near 42M. The 09-15 session is also a mild inside-ish down day (open 330.14 below the prior close, high 331.78, close 331.34, low 328.35), consistent with digestion rather than reversal. Ideally the next upside break comes on ≥50M shares; a push to new highs on sub-35M volume would be suspect.

---

## 6. Why These Indicators Were Selected (8)

| # | Indicator | Value (2026-09-15) | Why it fits this context |
|---|---|---|---|
| 1 | **close_10_ema** | 325.38 | Captures the fresh September thrust and defines the immediate trailing support / trend-follow stop. |
| 2 | **close_50_sma** | 318.84 | The line price reclaimed on 08-28; the pivot separating "recovery" from "failed rally." Also the tactical invalidation level. |
| 3 | **close_200_sma** | 285.51 | Confirms the primary uptrend and quantifies how extended price is (+16.05%). Strategic anchor. |
| 4 | **macd** | 4.304 | Measures the mid-term momentum shift; zero-line reclaim on 09-01 validates trend change. |
| 5 | **macds** | 2.708 | Timing device — the 08-31 crossover and its 09-02 zero-cross mark the entry window; distance from MACD gauges conviction. |
| 6 | **rsi** | 61.31 | Non-redundant oscillator: confirms there is headroom before overbought and lets us watch for divergence at the 336–344 resistance. |
| 7 | **boll_ub** | 335.25 | Quantifies the immediate breakout ceiling and the overbought/extension zone. |
| 8 | **boll_lb** | 303.29 | Anchors the downside objective and identifies the lower boundary of the August base. |

**ATR** and **VWMA** were also retrieved and are used above for stop sizing and participation confirmation, but were kept out of the core eight to avoid over-weighting volatility/volume signals that are already partially embedded in the Bollinger and MACD reads.

---

## 7. Actionable Levels & Scenarios

**Immediate resistance cluster (0.6%–1.5% above):**
- **333.43** — 2026-07-30 close, the top of the unfilled 07-31 gap
- **335.25** — Bollinger upper band
- **336.22** — 2026-09-11 swing high (the trigger level)
- **342.89** — 2026-07-28 intraday high · **344.57** — 2026-07-29 intraday high (visible-window high)

**Immediate support cluster (1.8%–3.9% below):**
- **325.38** — 10-EMA (first line of defense)
- **322.15** — VWMA
- **319.27 / 318.84** — Bollinger mid-band and 50-SMA (the real line in the sand)
- **316.24** — 2×ATR stop reference
- **309.90** — 2026-09-09 low (structure break)
- **303.29** — lower Bollinger band, adjacent to the 2026-08-12 close of 302.25

**Scenario A — Bullish continuation (base case, ~60% weight):** A daily close above **336.22** on volume ≥50M confirms the gap repair and re-opens **342.89**, then **344.57**. A range-measurement projection off the 300.57–336.22 base (~35.65 points) from the breakout implies roughly **371.9**; treat this as a projection, not an observed level.

**Scenario B — Constructive pullback (preferred risk/reward, ~30% weight):** A drift into **325.4–318.8** that holds on declining volume would offer a better entry than chasing at 331 with 1.6% to resistance. Buyers there could use a stop under **315.3** (09-09 close) or, more conservatively, under **309.90** (09-09 low).

**Scenario C — Failed retest / bear case (~10% weight):** A daily close back below the **50-SMA at 318.84** alongside MACD histogram turning negative would mark the 08-31–09-15 advance as a failed retest of the July gap. That would target **303–310**, with the lower band at 303.29.

**Risk management:** With ATR at 7.55 (2.28%), a volatility-scaled stop on a long entered near 331.34 should sit ~15.1 points lower (~316.2, a 4.6% risk) for a 2-ATR buffer. Size positions so that a full stop-out equals the plan's per-trade risk budget — the fast September advance means a "normal" pullback can retrace 7–8 points without damaging the trend.

**What to watch next:** (1) Does volume expand or contract on any push through 336.22? (2) Does RSI push through 70 (July-style exhaustion) or stall near 65 (healthy rotation)? (3) Does MACD histogram keep expanding past 1.60, or flatten for a third consecutive session — a flattening histogram at these levels is the earliest warning of a stall.

---

## 8. Summary Table

| Dimension | Reading (2026-09-15) | Signal | Evidence |
|---|---|---|---|
| Price | 331.34 | Neutral/digestive day | Open 330.14, H 331.78, L 328.35, V 31.7M; prior close 333.08 |
| Primary trend | 200-SMA 285.51, rising | **Bullish** | Price +16.05%; 50-SMA 11.67% above 200-SMA |
| Intermediate trend | 50-SMA 318.84, rising | **Bullish** | Reclaimed 08-28; held 12 straight sessions |
| Short-term trend | 10-EMA 325.38, rising | **Bullish** | Price +1.83% above; 10-EMA crossed above 50-SMA ~09-08 |
| Momentum | MACD 4.304 > Signal 2.708 | **Bullish** | Cross 08-31; zero-cross 09-01; hist +1.597, highest since 07-28 |
| Oscillator | RSI 61.31 | **Bullish, not extended** | Down from 63.32; ~9 pts below overbought; RSI higher low 40.2 → 49.3 |
| Volatility | ATR 7.55 (2.28%) | Expanding, controlled | Up from 7.10 (08-27); down from 9.87 (07-31) |
| Bollinger | Mid 319.27 / UB 335.25 / LB 303.29 | Upper-quartile, coiling | %B 87.8%; width 31.96 (10.0%), ~39% below 08-12 width |
| Participation | VWMA 322.15 | **Confirming** | Price +2.85%; VWMA rising from 317.04 on 09-09 |
| Volume trend | 31.7M vs ~42M 20-day avg | **Caution** | Declining volume on the 09-14/09-15 stall |
| Key resistance | 333.43 / 335.25 / 336.22 / 342.89 / 344.57 | Overhead supply | 07-30 close, upper band, 09-11 high, July highs |
| Key support | 325.38 / 322.15 / 319.27 / 318.84 / 309.90 | Layered | 10-EMA, VWMA, mid-band, 50-SMA, 09-09 low |
| Structural bias | Higher lows & higher highs since 08-12 | **Uptrend intact** | 300.57 → 309.90 lows; 319.28 → 327.30 → 336.22 highs |
| Tactical trigger | Daily close > 336.22 on ≥50M shares | Buy continuation | Target 342.89 → 344.57 |
| Preferred entry | 325.4–318.8 pullback | Better R/R | Stop < 315.3 or < 309.90 |
| Invalidation | Daily close < 318.84, then < 309.90 | Trend damage | Targets 303.29 (lower band) / 302.25 (08-12 close) |

**Bottom line:** AAPL is in a confirmed, multi-timeframe uptrend that has absorbed a −7.4% event-driven gap on 2026-07-31 and rebuilt from a 302.25 close (08-12) to 331.34 — a +9.62% recovery. Trend, momentum, and volume-weighted measures are all aligned higher, and RSI at 61.3 says the move is not stretched. The immediate obstacle is the 333.43–336.22 band at the top of the July gap. The cleanest asymmetric setup is either a volume-confirmed break of 336.22 targeting 342.89/344.57, or a pullback into the 325→319 zone with a stop below 315.3. The main things that would change this view are a loss of the 50-SMA at 318.84 with a negative MACD histogram, or a fresh high printed on conspicuously thin volume.