# AAPL — Multi-Timeframe Technical Report
**Analysis date: 2026-07-23 (close) · Instrument: AAPL (Apple Inc.)**

---

## 1. Verified snapshot (source of truth)

| Field | Value (2026-07-23) |
|---|---|
| Open | 321.73 |
| High | 323.30 |
| Low | 319.35 |
| **Close** | **321.66** |
| Volume | 40,840,800 |
| 10 EMA | 322.655 |
| 50 SMA | 305.467 |
| 200 SMA | 275.599 |
| MACD / Signal / Hist | 8.107 / 7.312 / +0.795 |
| RSI(14) | 58.11 |
| Bollinger mid / upper / lower | 311.492 / 346.677 / 276.307 |
| ATR(14) | 7.918 (~2.46% of price) |
| VWMA | 321.376 |

All figures below come from the frozen OHLCV rows and the indicator calls above; every level cited has a concrete date attached.

---

## 2. Why these 8 indicators (complementary, non-redundant)

| Indicator | Role in this specific context |
|---|---|
| **close_200_sma** (275.60) | Strategic trend anchor. AAPL is a bull-market structure; 200 SMA is rising ~0.3/day — the primary filter for "trade with the trend." |
| **close_50_sma** (305.47) | Medium-term trend + rising dynamic support, 5.3% below price. Defines the "trend is intact" line. |
| **close_10_ema** (322.66) | Short-term momentum trigger. Price closed **below** it on 7/23 for the first time since 6/30 — the earliest, cleanest warning of a momentum shift. |
| **macd** (8.11) | Confirms trend/momentum regime change. Line is still above signal (7.31) but is rolling over from 8.93 on 7/21. |
| **rsi** (58.11) | Overbought/oversold reset gauge. 71.65 (7/17) → 58.11 = mechanical reset **without** price damage. |
| **boll_ub** (346.68) | Extension/volatility-expansion gauge; distinguishes "riding the band" (healthy trend) from "failed extension." |
| **atr** (7.92) | Pure risk tool: stop placement and position sizing in a fast tape. |
| **vwma** (321.38) | Volume-weighted truth of where recent buyers actually own stock — currently *at* price, the key line in the sand. |

Deliberately excluded: `macds`/`macdh` (duplicative of `macd`; signal cross is already derivable from the verified snapshot), `boll`/`boll_lb` (the 50/200 SMAs already cover the mean-reversion/rubber-band function and the 20-period mid is quoted above), and `stochrsi` (redundant with RSI).

---

## 3. Trend structure — three timeframes, one direction

**Long-term (200 SMA): strongly bullish and still steepening.**
The 200 SMA rose from 261.99 (5/26) to 275.60 (7/23). Price at 321.66 sits **+16.7% above** it. The 50 SMA has been above the 200 SMA throughout the sample; the spread today is +29.87 points, i.e. the 50 SMA is **10.8% above** the 200 SMA — a wide, mature golden-cross configuration. This is late-stage-but-intact trend, not a top formation. Note the 200 SMA is the *only* downside level that would require a genuine trend break (a ~14% drawdown from here), so it is a strategic, not tactical, reference.

**Medium-term (50 SMA): the load-bearing support.** The 50 SMA has risen every single session from 271.72 (5/26) to 305.467 (7/23), gaining roughly 0.6–0.9 points per day. Critically, it is *rising into* price rather than price falling to a flat line — a textbook healthy configuration. Price is +5.3% above it.

**Short-term (10 EMA): the first crack.** The 10 EMA accelerated from 290.25 (7/1) to 322.66 (7/23) — a 32-point climb in three weeks, mirroring a near-vertical July advance. On 7/23 the close of 321.66 printed **below** the 10 EMA (322.66) for the first time since 6/30. That is a legitimate short-term momentum break, but note the magnitude: only −0.31%. One marginal close is a yellow flag, not a red one; a second consecutive close below would make it meaningful.

**The path that produced this setup (all from tool data):**
- 6/24 close 293.08 → 6/25 close **275.15** (−6.12%), intraday low 273.75 (−6.59%), on 107.0M shares — an unexplained gap-down in the data (no news available from these tools).
- 6/26 printed 261.8M volume — a massive outlier, roughly 4–5× the July average, consistent with an index/rebalance-type event. Treat this bar as mechanically distorted, not as a directional signal.
- V-shaped recovery: 275.15 (6/25) → **333.74** (7/17) = **+21.3% in 15 sessions**, a ~1.3%/day advance. This is the definition of a parabolic leg.
- The breakout that matters: 7/15 close 327.50 (**+4.01%** vs 7/14's 314.86) on 61.0M shares, 7/16 and 7/17 both ~63M shares at new highs (333.26 / 333.74). This cleared the entire **May–June consolidation ceiling of roughly 315.20–317.40** (5/29 high 315.00; 6/2 close-highs 315.20 / 316.94; 6/8 high 317.40) on expanding volume — a high-quality breakout.
- Since 7/17 the tape has gone **four consecutive lower closes**: 333.74 → 326.59 → 327.74 → 325.89 → **321.66** (−3.62% from the record close, high-water mark 334.99 on 7/17).

---

## 4. Momentum: resetting, not reversing

- **RSI:** 71.65 on 7/17 → 58.11 on 7/23. That peak was the highest since 79.79 (5/28). The important detail: **the RSI peak and the price peak coincide on 7/17**, so there is no bearish RSI divergence at the high. This pattern — RSI falling ~13.5 points while price falls only ~3.6% — is characteristic of momentum *digestion*, not distribution. The RSI low in the 6/25 flush was 32.20; RSI has since held a higher-low sequence (32.2 → 39.9 → 46.9 → 50.97 → 60.26 → 71.65 → 58.11). Watch 50 as the dividing line between "healthy pullback" and "momentum failure."
- **MACD:** Line 8.107, signal 7.312, histogram **+0.795** — still bullish, but the histogram has now contracted from the 7/21 peak, and the MACD line peaked at 8.927 (7/21) and has ticked down two sessions. The June episode is the relevant template: in June the MACD fell from 10.09 (5/26) to a trough of −2.92 (6/29) *during the consolidation*, then re-accelerated. MACD's job now is binary: does it cross below 7.31 (bearish cross, confirming the pullback extends) or curl back up above ~8.9 (trend continuation)?

---

## 5. Volume: the pullback is quiet, which is constructive

- **VWMA = 321.376 vs close 321.66 (+0.09%).** This is the single most important number in the report. The VWMA has exploded higher — 296.42 (7/15) → 321.38 (7/23), a 25-point jump in six sessions — because the breakout was transacted on heavy volume. Price now sits *exactly* on the volume-weighted cost basis of recent buyers. Bull case: the VWMA acts as a rising floor and the average July buyer is still green. Bear case: any close decisively below ~321.4 puts the entire recent buyer cohort underwater, which typically invites supply.
- **Volume character:** breakout days 7/15 (61.0M), 7/16 (63.0M), 7/17 (63.4M) averaged ~62.4M. The four pullback sessions averaged ~43.6M (53.5M, 41.3M, 38.8M, 40.8M), with 7/22's 38.8M the lightest of the group. **Rising volume on the advance, contracting volume on the decline** = accumulation pattern, i.e. supply is not aggressive.

---

## 6. Volatility and the Bollinger extension

- **Bollinger upper band: 312.68 (7/1) → 346.68 (7/23), +10.9%.** The band has expanded violently upward, and price is now **7.2% below** the upper band (321.66 vs 346.68) while sitting **+3.3% above** the mid-band (311.49). In the 7/15–7/17 thrust, price was pressing toward the upper-band envelope; it has now stepped back inside. Band expansion of this magnitude is a volatility-regime warning: the ranges available in *either* direction are now much larger than they were in early July.
- **ATR = 7.918 (2.46% of price).** ATR crept from 5.81 (5/26) to a peak of 8.74 (7/2), and has eased to 7.92 — still elevated. Practical translation:
  - 1×ATR stop from 321.66 = **313.74**
  - 1.5×ATR = **309.78**
  - 2×ATR = **305.82** (which lands almost exactly on the 50 SMA at 305.47)
  This is why the 50 SMA is the natural invalidation line for a swing position: a 2-ATR stop and the medium-term trend line coincide.

---

## 7. The level map (all levels derived from tool output)

**Resistance**
1. **322.66** — 10 EMA (immediate, lost on 7/23)
2. **325.89–327.74** — 7/21–7/22 closes, the underside of the last three sessions
3. **333.74 / 334.99** — 7/17 record close and record intraday high
4. **346.68** — Bollinger upper band (dynamic; a price reaching it would be a re-acceleration)

**Support**
1. **321.38** — VWMA (price is sitting on it *today*); confluence with 319.35 (7/23 low) makes **319.35–321.40** the immediate decision zone
2. **317.32** — 7/15 breakout candle low (never violated since the breakout)
3. **315.20–317.40** — the old May–June ceiling, now the primary retest zone; this is the highest-probability dip-buy area
4. **311.49** — Bollinger mid (20 SMA), rising fast; watch it converge toward the breakout zone over the next week
5. **305.47** — 50 SMA (medium-term trend invalidation; also 2×ATR)
6. **275.60** — 200 SMA (strategic trend invalidation)

Note the structure of the levels: price has held 319.35 > 317.32 > 315.20. **No support has been broken.** The pullback so far is a three-and-a-half percent retrace of a 21% leg (only ~15% retracement of the move), which is exceptionally shallow.

---

## 8. Nuanced assessment & actionable plan

**Base case (highest probability): bull-market consolidation before a retest of 334–335.** Supporting evidence: price above a rising 50 SMA and a rising 200 SMA; MACD still above signal; VWMA rising and untested; volume contracting into the pullback; RSI reset from 71.7 to 58.1 with no divergence at the high; the breakout zone (315–317) never given back. The parabolic character of the 7/1–7/17 leg (+21.3% in 15 sessions) argues for several more sessions of chop or a deeper flush toward 315–317 before continuation.

**Actionable ideas**

1. **For existing longs:** Keep the position, but tighten the trail. Two valid trailing stops:
 - *Tactical:* daily close below **317.32** (7/15 breakout low) = reduce 1/3 to 1/2.
 - *Strategic:* daily close below the **50 SMA (305.47)** = exit the swing position. Using 2×ATR (7.92) that is a ~5% risk distance — size accordingly (e.g., risk 1% of equity → notional ≈ 20% of equity if you use the full 15.8-point stop distance).
2. **For new entries (do not chase):** Wait for one of two setups:
 - *Pullback buy:* a tag of **315.20–317.40** that holds on *below-average* volume, with RSI remaining above ~45. Stop below 311.49 (Boll mid) initially, move to below 305.47 if held. First target 333.74, then 346.68 (Boll upper).
 - *Breakout buy:* a daily close above **334.99** on volume >~60M (matching the 7/15–7/17 breakout days). Stop 1×ATR (7.9) below the breakout close.
3. **What would flip the bias to bearish (all must be confirmed by tool data, not assumed):**
 - Daily close below **321.38 (VWMA)** that is *not* recovered within 1–2 sessions → recent buyers underwater.
 - **MACD crossing below its signal (7.31)** — currently 8.11 vs 7.31, so a further ~10% erosion of MACD is required.
 - **RSI breaking and holding below 50** (currently 58.1).
 - Two consecutive closes below the 10 EMA (already one on 7/23).
 In that scenario, the 311.49 (Boll mid) → 305.47 (50 SMA) zone becomes the measured downside objective.

**Discrepancies / data caveats I want to flag rather than reconcile:**
- The verified snapshot lists `mfi = 0.618` — an unusual scale for Money Flow Index (normally 0–100). I have deliberately **not** used it in the analysis because its scaling is ambiguous.
- The 6/25 −6.12% gap and the 6/26 volume of 261.8M (≈6× the July mean) are unexplained by the available data tools; I am treating them as event/mechanical distortions and not as technical signals. No fundamental or earnings information is available from these tools, so no event-risk date is asserted here.
- AAPL went ex-dividend 2026-02-09 ($0.26) and 2026-05-11 ($0.27); the technical total-return index (327.09) exceeds the raw close (321.66), so total-return based metrics are marginally higher than price-based ones.

---

## 9. Summary table

| Dimension | Reading (2026-07-23) | Interpretation | Level / Trigger to watch |
|---|---|---|---|
| **Primary trend (200 SMA)** | 275.60, rising; price +16.7% above | Bullish, mature | Close below 275.60 = structural break |
| **Medium trend (50 SMA)** | 305.47, rising ~0.6–0.9/day; price +5.3% above | Bullish, support rising into price | 305.47 = swing invalidation |
| **Short-term (10 EMA)** | 322.66; close 321.66 **just below** (first since 6/30) | Early momentum crack, minor (−0.31%) | 2nd close below = caution |
| **MACD** | 8.11 vs signal 7.31, hist +0.80, rolling over from 8.93 (7/21) | Bullish but decelerating | Cross below 7.31 = extension of pullback |
| **RSI** | 58.11 (from 71.65 on 7/17) | Overbought reset, **no bearish divergence** | Hold >50 = bullish; <50 = caution |
| **Bollinger upper** | 346.68, +10.9% in 22 sessions; price 7.2% below it | Volatility expansion; price stepped back inside bands | 346.68 = re-acceleration target |
| **ATR** | 7.92 (2.46%); 1×=313.7, 2×=305.8 | Elevated; warrants smaller size / wider stops | 2×ATR ≈ 50 SMA ⇒ clean risk line |
| **VWMA** | 321.38; close +0.09% above | Price exactly at recent buyers' cost basis | Losing 321.38 = supply risk |
| **Volume behavior** | Breakout days ~62.4M vs pullback days ~43.6M | Accumulation pattern; quiet pullback | Need >60M on a new-high thrust |
| **Structure** | 4 lower closes from 333.74 (−3.62%), only ~15% retrace of the +21.3% leg; supports 319.35/317.32/315.20 all intact | Consolidation within an uptrend | 315.20–317.40 = prime dip-buy retest |
| **Bias** | **Bullish with near-term consolidation** | Hold longs w/ trailing stops; buy 315–317 retest, don't chase | Bear flip: <321.38 VWMA + MACD cross + RSI <50 |