# AAPL — Multi-Timeframe Technical Assessment (as of 2026-07-20)

## 1. Verified Baseline (source of truth: snapshot 2026-07-20)

| Item | Value |
|---|---|
| Last close | **326.59** (open 333.51, high 333.71, low 323.68) |
| Session change | **−2.14%** vs 2026-07-17 close of 333.74 (derived from tool rows) |
| Volume (2026-07-20) | 53,468,000 |
| Most recent swing high (in data window) | **334.99 on 2026-07-17** (intraday); prior day high 334.68 |
| 50-day SMA | 303.43 (rising every session since at least 2026-05-21) |
| 200-day SMA | 274.58 (rising slowly) |
| 10-day EMA | 320.98 (turning up sharply) |
| MACD / Signal / Hist | 8.883 / 6.159 / **2.724** |
| RSI(14) | **63.87** (down from 71.65 on 2026-07-17) |
| Bollinger (20,2) | mid 306.95 · upper 341.70 · lower 272.19 |
| ATR(14) | 8.27 (≈2.5% of price) |
| VWMA | 314.02 (accelerating upward) |

The raw OHLCV pull (158 rows, 2025-12-01 → 2026-07-20) and the verification snapshot agree exactly on the 2026-07-20 row and all indicator values — **no data discrepancy to flag**. (Note ex-dividend rows of 0.26 on 2026-02-09 and 0.27 on 2026-05-11; the total-return index diverges slightly from price around those dates, which is expected.)

## 2. Selected Indicators (8) and Why

1. **close_50_sma** — the operative medium-term trend spine; price is currently significantly extended above it, which is the single most important mean-reversion risk input.
2. **close_200_sma** — confirms the strategic regime (price ~19% above it, with the 50-SMA far above the 200-SMA = established bullish structure, not a bottoming trade).
3. **close_10_ema** — the fast trend filter that has been riding the July advance; it is the first tripwire for trend damage.
4. **macd** — confirms the July momentum re-acceleration and gives the crossover timeline.
5. **macdh** — the earliest quantitative warning of momentum deceleration; it has just turned down for the first time since 2026-07-02.
6. **rsi** — pins down the overbought-then-cooling sequence (71.65 → 63.87 in one session) without duplicating MACD's role.
7. **atr** — volatility-scaled stop and position-sizing input; this name has repeatedly printed 7–9 ATR, so fixed-percentage stops are inappropriate.
8. **vwma** — volume-confirmation of the advance; the jump in VWMA is the tell that the July rally was volume-supported, not a thin squeeze.

(Deliberately excluded: Bollinger middle overlaps heavily with the 50-SMA at 306.95; `macds` is redundant once `macd` and `macdh` are in; stochastics would duplicate RSI.)

## 3. Price Structure and Regime

**Regime: volatile, volume-confirmed uptrend with an extended short-term position.**

The data window contains three distinct phases:
- **Dec 2025 – Mar 2026: corrective/base-building.** From a 2025-12-02 close of 286.19 the stock fell to a 246.70 close on 2026-01-20 (low 243.42), rebounded to 280.91 (2026-02-06 high), fell again to a 246.00 low on 2026-03-20. That was a wide, choppy, downward-sloping range.
- **Apr – early Jun 2026: accumulation and advance.** Steady climb to a 315.45 high on 2026-06-02 and 317.40 on 2026-06-08.
- **2026-06-09 → 2026-06-26: sharp shakeout.** Close fell from 301.54 (2026-06-08) to 275.15 (2026-06-25) on 107.0M shares, then 2026-06-26 printed an enormous **261.8M-share** session with a low of 274.21 and a close of 283.78 (+3.1% vs the prior close) — a classic high-volume downside exhaustion / reversal signature in the tape.
- **2026-06-29 → present: V-shaped recovery to new highs.** Close went from 281.74 (2026-06-29) to **333.74 (2026-07-17)**, a **+21.3% move in 13 sessions**, with the 2026-07-17 high of 334.99 being the highest print in the entire window.

**The most recent session matters:** 2026-07-20 opened at 333.51, failed at 333.71, sold to 323.68, and closed at 326.59 — below the 2026-07-17 low of 329.00. That is a bearish reversal day immediately after a record high, on 53.5M shares. The saving grace is that the 323.68 low held **above** the 10-EMA (320.98) and well above the 2026-07-15 low of 320.73… rather, the 2026-07-15 *low* was 317.32 and the 2026-07-15 close was 327.50, so the pullback is still inside the prior day's structure and has not broken the fast trend.

## 4. Trend Evidence

- **Stacked bullish alignment:** close 326.59 > 10-EMA 320.98 > VWMA 314.02 > 50-SMA 303.43 > 200-SMA 274.58. Every layer is rising. Price sits **+1.75%** above the 10-EMA, **+4.0%** above VWMA, **+7.6%** above the 50-SMA and **+18.9%** above the 200-SMA.
- The 50-SMA has climbed monotonically from 269.49 (2026-05-21) to 303.43, and the 200-SMA from 261.07 to 274.58 — the golden-cross structure is intact and widening (spread ≈ 28.9 points).
- **The +7.6% gap to the 50-SMA is the stretched part.** In this dataset, comparable extension readings preceded the multi-day pullbacks of mid-February (2026-02-12, −5.2% day) and early June (2026-06-09, −3.6% day). Extension is a risk input, not a sell signal, because the trend layers beneath it are all rising.

## 5. Momentum Evidence (MACD / Histogram / RSI)

- **MACD turned up decisively:** the histogram flipped positive on **2026-07-02** (0.26) after being negative since roughly 2026-06-10, i.e., a bullish MACD/signal crossover at the start of July. MACD rose from −2.92 (2026-06-29) to **8.88** (2026-07-20), with the signal at 6.16.
- **But the histogram has just peaked:** macdh went 2.72 → 3.34 (2026-07-17) → **2.72** (2026-07-20). That is the *first* decline in the histogram since the 2026-07-02 crossover. Historically in this dataset the histogram peaked ~1–2 sessions before short-term price highs (e.g., macdh peaked 2026-06-12 at −3.50 before the June slide deepened). Treat this as an early deceleration flag, not a trend reversal.
- **RSI cooled hard and fast:** 71.43 (2026-07-16) and 71.65 (2026-07-17) were the only overbought readings in the entire window; 2026-07-20's 63.87 is a **−7.8 point single-session drop**. RSI is now in neutral-bullish territory with substantial headroom — which is constructive for continuation as long as it re-hooks upward. A slide below ~55 without a price recovery would argue the July impulse is over.

## 6. Volatility and Bollinger Context

- **ATR 8.27** (~2.5% of price), up from ~7.0 in mid-June. The 2026-06-25/26 events (daily ranges of ~15 and ~11.7 points) permanently re-rated this stock's volatility. Expect 8–10 point daily ranges.
- **Bollinger bands are expanding violently:** upper band went 312.68 (2026-07-01) → 341.70 (2026-07-20); lower band sits at 272.19. Band width of ~69.5 points reflects an upside volatility expansion (trending, not mean-reverting, conditions).
- Crucially, **price is 15.1 points *inside* the upper band (326.59 vs 341.70)** — it is *not* riding/closing above the band. The July advance was a controlled breakout rather than a parabolic blow-off, which is a point in favor of trend continuation.
- **ATR-scaled levels:** 1.5×ATR = 12.4 → **~314.2** (lands almost exactly on the VWMA at 314.02); 2×ATR = 16.5 → **~310.1** (just under the 2026-07-14 low of 311.91). These are the natural swing-stop zones.

## 7. Volume Confirmation (VWMA)

- VWMA has ripped from 289.27 (2026-06-29) to **314.02**, and the last three sessions alone took it from 300.72 → 310.27 → 314.02. Because VWMA weights recent price by volume, this acceleration means the heaviest recent volume occurred at the *higher* prices — genuine participation, not a drift higher.
- Approximate volume work from the raw rows: the last 20 sessions average **~65.8M shares**, but that is distorted by the 261.8M (2026-06-26) and 107.0M (2026-06-25) capitulation prints. Excluding those two, the average is **~52.6M**. The 2026-07-15/16/17 breakout days (61.0M, 63.0M, 63.4M) ran roughly **17–20% above** that ex-spike norm — accumulation on strength.
- The 2026-07-20 down day (53.5M) was *below* the three breakout days. That is a mild positive: the sell-off has not yet shown the distribution volume that would confirm a top.

## 8. Actionable Plan

**Bias: bullish trend, tactically cautious for 1–3 sessions.** The trend is objectively up on every chosen measure, but (a) price is +7.6% over the 50-SMA, (b) MACD histogram has just rolled over, (c) RSI dropped 7.8 points in one day, and (d) 2026-07-20 was a bearish outside/reversal day closing below the prior day's low. The probability-weighted path is consolidation or a shallow dip into support, not an immediate collapse.

**Scenarios and levels (all derived from tool data):**
- **Breakout continuation:** a daily close above **334.99** (2026-07-17 high) re-opens the upside with the Bollinger upper band at **341.70** as the first mechanical target, then extension toward the ~2×ATR-off-breakout zone near 342–350. This scenario requires MACD histogram to re-expand above 3.34.
- **Orderly pullback (base case):** support ladder = **320.98** (10-EMA) → **317.32–314.02** (2026-07-15 low / VWMA cluster) → **306.95** (Bollinger mid) → **303.43** (50-SMA). A hold anywhere in the 314–321 band keeps the July uptrend intact and offers a better risk/reward entry than chasing 326.59.
- **Trend damage:** a daily close below **311.91** (2026-07-14 low) after failing to reclaim 334.99 would break the fast-trend sequence and put **303–307** (50-SMA + Bollinger mid) in play. A close below the 50-SMA would be the first structural change in this leg.

**Risk management:**
- Swing stop placement: **~318.5** (1×ATR below the 2026-07-20 close) for tight tactical longs; **~310.0** (2×ATR) for wider trend positions — both are just under real structural levels, which is where stops belong in an 8-point-ATR name.
- Position sizing: with ATR at 2.5% of price, size to a fixed dollar risk (e.g., risk 0.5–1% of equity per unit of 2×ATR) rather than a fixed share count.
- For new longs, prefer scaling in at 320.98 / 314.02 rather than at market, given the extension. Momentum accounts should not add while RSI is falling and the histogram is shrinking.

**What would flip the bias:** (1) a volume-expansion close below 314.02 on rising volume suggests the VWMA has flipped from support to resistance; (2) MACD crossing back below its signal (histogram < 0, currently at +2.72, so ~3–4 sessions of erosion away); (3) RSI failing to hold 55.

## 9. Key Points Summary

| Dimension | Reading (2026-07-20) | Interpretation | Level to watch |
|---|---|---|---|
| Price vs 50-SMA | 326.59 vs 303.43 (**+7.6%**) | Uptrend intact but short-term extended | 303.43 (mean-reversion magnet) |
| Price vs 200-SMA | 326.59 vs 274.58 (**+18.9%**) | Strategic bull regime; 50 > 200 golden-cross structure | 274.58 |
| 10-EMA | 320.98, sharply rising | Fast trend healthy; last pullback low (323.68) held above it | 320.98 first support |
| MACD / Signal | 8.883 / 6.159 | Bullish, crossover occurred 2026-07-02 | Signal 6.16 |
| MACD Histogram | 2.724, down from 3.337 (2026-07-17) | **First deceleration since the July 2 crossover** | Re-expansion above 3.34 = all-clear; < 0 = bearish cross |
| RSI | 63.87, from 71.65 | Left overbought, now neutral-bullish; 71.4/71.6 were the only overbought prints in the window | 55 (bear) / 70 (re-overbought) |
| Bollinger | mid 306.95 · UB 341.70 · LB 272.19 | Bands expanding; price inside UB → breakout, not blow-off | 341.70 upside target; 306.95 first major support |
| ATR | 8.27 (~2.5%) | Volatility re-rated higher since 2026-06-25/26 | 1.5×ATR ≈ 314.2; 2×ATR ≈ 310.1 |
| VWMA | 314.02, accelerating up | Volume-weighted participation confirms advance | 314.02 = volume-defined trend line |
| Volume | 63.4M (Jul 17) breakout vs ~52.6M ex-spike norm; 53.5M on Jul 20 dip | Accumulation on strength, no clear distribution yet | >70M down-day = distribution warning |
| Recent swing high | 334.99 (2026-07-17) — highest in the data window | Breakout trigger | Close > 334.99 = continuation |
| Recent swing lows | 317.32 (Jul 15), 311.91 (Jul 14), 274.21 (Jun 26 capitulation) | Support ladder beneath price | Loss of 311.91 = leg damage |
| **Net stance** | **Bullish trend / tactically neutral-to-cautious near-term** | Hold longs with ATR stops; add on 314–321 pullback; don't chase >334.99 without histogram confirmation | Bias flips bearish under ~311.9 |