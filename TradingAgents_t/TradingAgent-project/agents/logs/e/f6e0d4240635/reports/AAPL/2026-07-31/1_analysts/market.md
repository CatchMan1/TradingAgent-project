# AAPL — Technical Situation Report
**As of the close of 2026-07-31** | Source of truth: verified B-project snapshot for 2026-07-31 (all exact OHLCV and indicator values below are taken from that snapshot / the frozen OHLCV cache)

---

## 1. What actually happened on the tape

The single most important fact is the last session. AAPL printed:

| Field | 2026-07-31 |
|---|---|
| Open | 304.81 |
| High | 310.69 |
| **Low** | **300.00** |
| **Close** | **308.91** |
| Volume | **132,489,100** |
| Prior close (2026-07-30) | 333.43 |

Derived moves (computed directly from those two verified rows):

- **Gap down at the open: −8.58%** (304.81 vs 333.43)
- **Close-to-close: −7.35%** (308.91 vs 333.43) — **the largest single-session percentage decline anywhere in the Oct-2025 → Jul-2026 data window I retrieved.** The next-worst sessions in the window are 2026-06-25 (−6.12%) and 2026-02-12 (−5.00%).
- **Close vs. open: +1.35%**, and **close vs. session low: +2.97%** — i.e. a long lower shadow and a green body relative to the *open*. Buyers did absorb supply at the 300 area.
- **Volume 132.5M** versus a ~50.8M average across the preceding 21 sessions (07-01 → 07-30) — roughly **2.6x normal**. It is the highest volume session since 2026-06-26 (261.8M) and the third-largest in the whole window behind 2026-06-26 and 2025-12-19 (144.6M).

**Interpretation with nuance:** This is not a drifting pullback; it is an *event-style repricing* on institutional-size volume. The candle is ambiguous by design — a gap-down-and-close-higher shape (bullish absorption) wrapped inside a −7.35% body on record-relative volume (bearish distribution). In my reading the **volume, not the shadow, is the dominant signal**: one green reversal candle on 2.6x volume does not repair a trend, but it does define a level (300.00) that the market has now publicly defended once.

Context: 2026-07-28's close of **340.08** was the highest close in the retrieved window, and 2026-07-29's high of **344.57** was the window's high. From those marks the 2026-07-31 close represents **−9.16% from the 07-28 closing high** and **−10.35% from the 07-29 intraday high** — a fully-fledged 10% correction off the high in three sessions.

---

## 2. Selected indicators (8) and why each earns its slot

**Market context being modeled:** a mature, steeply-rising uptrend that has just suffered a violent single-day volume break — the classic "trend-break vs. bull-market shakeout" decision point. That requires (a) trend benchmark structure, (b) momentum confirmation, (c) volatility envelope + volatility magnitude for risk sizing, and (d) a volume-weighted reality check on where the marginal buyer sits. Duplicates were deliberately excluded (no MACD signal line *and* histogram *and* RSI-plus-stochastic stacking).

| # | Indicator | Value 2026-07-31 | Role in this specific setup |
|---|---|---|---|
| 1 | **close_50_sma** | **309.4994** | The mid-term trend line that the close just lost by 0.19%. First close below it since 2026-06-30. The pivotal level. |
| 2 | **close_200_sma** | **277.9605** | Strategic trend anchor. Price is still **+11.14% above** it and the line is rising (268.49 on 06-22 → 277.96 on 07-31). Keeps the primary uptrend intact. |
| 3 | **close_10_ema** | **327.2373** | Fast momentum gauge and the first real overhead resistance. Price is **−5.60%** below it; the 10-EMA has already rolled over (331.31 on 07-30 → 327.24). |
| 4 | **macd** | **6.8910** (signal **8.2562**, histogram **−1.3652**) | The crossover event: histogram flipped negative for the first time since 2026-06-25 → 2026-07-01, i.e. the first bearish MACD crossover in 21 sessions. Line is still >0, so it's a *momentum* break, not a *level* break. |
| 5 | **rsi** | **43.2439** | Momentum reset: **61.66 → 43.24 in one day**, an 18.4-point collapse. Critically, **it is not oversold** — no mechanical bounce fuel. |
| 6 | **boll_lb** | **304.2213** (mid **324.3670**, upper **344.5127**) | Volatility envelope. The session low (300.00) undercut the lower band intraday, but the close (308.91) finished back **inside** the band. %B ≈ **0.116**; bandwidth ≈ **12.4%** of the mid-band. |
| 7 | **atr** | **9.8721** (≈ **3.20%** of price) | Volatility expanded from 8.06 (07-30) to 9.87. This is the position-sizing and stop-placement engine for both longs and shorts. |
| 8 | **vwma** | **326.3853** | The volume-weighted "true average entry" of recent buyers. It rose from 288.84 (06-30) to 329.58 (07-30) — meaning heavy volume transacted at 320–340. Price is now **−5.35% below it**: July's volume-weighted cohort is underwater, which is overhead supply. |

*Data-integrity note:* the OHLCV from `get_stock_data` and the verified snapshot agree exactly on the 2026-07-31 row and on every indicator value listed (rsi 43.2439, macd 6.89101, macds 8.256228, macdh −1.365218, atr 9.872098, boll 324.367, boll_ub 344.512719, boll_lb 304.221281, close_50_sma 309.4994, close_200_sma 277.960499, close_10_ema 327.23729, vwma 326.385284). **No discrepancy to flag.**

---

## 3. Trend read — three timeframes, three different answers

### Long term (200-SMA): intact uptrend
The 200-SMA is at **277.96** and rising steadily (+3.5% over the five-plus weeks from 268.49 on 2026-06-22). Price at 308.91 is **+11.14% above** it. The 50-SMA (309.50) sits **31.54 points (~11.35%) above** the 200-SMA — a wide, still-positive "golden cross" spread. Nothing in this data window says the multi-quarter uptrend is broken. Long-horizon holders are not being told to exit by the primary trend; they're being told to tolerate a deeper excursion.

### Medium term (50-SMA): broken — but only just
This is the crux. The close of 308.91 vs. the 50-SMA of 309.4994 is a breach of **0.19%** — technically a break, materially a "sitting on the line." What matters more:
- The 50-SMA's own slope has flattened dramatically: 306.99 (07-27) → 307.83 → 308.59 → 309.30 → 309.50. Its day-over-day gain has decelerated to ~0.2 points. A flattening 50-SMA after a vertical advance is the classic signature of a trend that has run out of fuel, and it means the 50-SMA will stop providing upward pull within days.
- This is the **first close below the 50-SMA since 2026-06-30**. The July advance (07-01 close 294.38 → 07-28 close 340.08, +15.5%) is now, in one session, back at its own origin: the 2026-07-02 breakout close was **308.63** — the 07-31 close of 308.91 is essentially exactly there. **The entire July leg has been round-tripped.**

### Short term (10-EMA / VWMA / MACD / RSI): firmly bearish
- Price is **−5.60%** below the 10-EMA (327.24) and **−5.35%** below the VWMA (326.39). That 326–327 **confluence** is now the dominant overhead supply shelf: it is simultaneously the fast average, the volume-weighted average cost, and within 2 points of the Bollinger mid-band (324.37). Three independent measures of "fair recent value" cluster in a 3-point zone. That is a real ceiling, not a cosmetic one.
- MACD histogram flipped to **−1.3652** — the first bearish crossover since 2026-07-01, and a fast one (0.643 → −1.365 in a session).
- RSI at **43.24** has erased the entire overbought episode: it peaked at **71.65 on 2026-07-17** and again at **68.90 on 2026-07-28**, and is now mid-range. **This is the most important asymmetry in the report**: the June 2026 low was made with RSI at 32.20 (2026-06-25), i.e. genuinely oversold. Today's RSI has ~11 points of room before it reaches that condition. There is no mechanical "oversold" bid waiting here.

---

## 4. The absorption detail worth respecting

I want to be precise and not oversell it. Facts: on 2026-07-31, price **traded to 300.00**, which is **below** the Bollinger lower band of 304.22, then closed at 308.91 — back inside the band, **+2.97% off the low**, and **+1.35% above the open**. A close back inside the band after an intraday undercut is a textbook "failed extension" pattern.

There is also a directly observable analogue in this dataset (presented as pattern, **not** as validation): on 2026-06-25 and 2026-06-26 AAPL sold off on 107.0M and then 261.8M shares, bottomed at 273.75/274.21, and rallied to 344.57 by 2026-07-29. High-volume capitulation *has* marked lows in this instrument recently. **However**, note the crucial difference: in June the RSI reached 32.20 and price was sitting on the 50-SMA area from below with the 200-SMA only ~4% away. Today RSI is 43.24 and price is suspended in mid-air with **~10% of empty space down to the 200-SMA**. The June analogue is suggestive; it is not equivalent.

**My judgment: the one-day absorption at 300 is a reason not to panic-sell into it, not a reason to buy it.**

---

## 5. Actionable levels (all from verified data)

**Resistance (overhead):**
1. **312.66** — 2026-07-06 close (first shelf)
2. **316.22** — 2026-07-09 close
3. **324.37 / 326.39 / 327.24** — Bollinger mid / VWMA / 10-EMA **confluence cluster** (the real test)
4. **333.43** — 2026-07-30 close, the breakdown origin (a close back above this would neutralize the gap)
5. **340.08** and **344.57** — 2026-07-28 record close and 2026-07-29 high

**Support (below):**
1. **309.50** — 50-SMA (currently being contested)
2. **304.22** — Bollinger lower band
3. **300.00** — 2026-07-31 low (the line the market defended)
4. **294.38** — 2026-07-01 close
5. **289.36** — 2026-06-30 close
6. **283.78** — 2026-06-26 close
7. **277.96** — 200-SMA, sitting essentially on top of the **274.21 / 273.75** June lows → the major structural floor

---

## 6. Trade construction

**For existing long-term holders:** the primary trend (200-SMA, +11.1%, rising) is intact. Hold, but recognize the character change: the 10-EMA/VWMA roll and the MACD cross mean the *momentum* regime has flipped from trend-following to range/repair. Do not add on this candle.

**For swing traders / new entries — do not buy the first gap-down bar on 2.6x volume.** Wait for one of two confirmations:
- **Bullish trigger:** a close back above **312.66**, ideally a higher low above **300–304**. That sets up a run at the 324–327 confluence. Stop below **299.00**. With ATR = 9.87, a 2×ATR stop is ~19.7 points, so entry ~313 with a 299 stop ≈ 1.4×ATR — acceptable.
- **Bearish trigger:** a decisive close **below 300.00** (which would also be a close below the lower Bollinger band and below the entire July base). First targets 289.36, then the 277.96 (200-SMA) / 274.21 zone. Invalidation above **327.24**.

**Position sizing (worked example, $100,000 account, 0.75% risk = $750):** long at ~309 with a stop at 299.00 = $10.00/share of risk → **75 shares (~$23,200 notional, ~23% of the account)**. The elevated ATR (3.20% of price, up from 2.4% two sessions ago) mechanically requires a *smaller* size than in mid-July — this is exactly the moment to shrink, not add.

**Asymmetry check:** upside to the 327 confluence from 308.91 is +5.9%; downside to the 200-SMA at 277.96 is −10.0%. Until price either reclaims 312.66 or loses 300.00, the reward/risk of a fresh position is poor in both directions. **Cash / patience is a legitimate position here.**

---

## 7. Key points summary

| Dimension | Reading (2026-07-31) | Signal | Actionable note |
|---|---|---|---|
| Session | O 304.81 / H 310.69 / L 300.00 / C 308.91 | Gap −8.58%, close −7.35% | Largest 1-day drop in the Oct-25→Jul-26 window |
| Volume | 132,489,100 (~2.6× prior-21-session avg ~50.8M) | **Distribution / event repricing** | 3rd-largest volume in window; highest since 2026-06-26 |
| Intraday reversal | Low 300.00 undercut Boll lower band 304.22; close 308.91 back inside, +1.35% above open | Mild bullish absorption | Defines 300.00 as the defended line |
| Long-term trend | close_200_sma 277.96 (rising); price +11.14% above | **Bullish, intact** | Strategic floor ≈ 278, with June lows 274.21/273.75 |
| Mid-term trend | close_50_sma 309.4994; close 308.91 = −0.19% | **Marginal break** | First close below 50-SMA since 2026-06-30 |
| Short-term momentum | close_10_ema 327.24 (price −5.60%); vwma 326.39 (price −5.35%) | **Bearish** | 324–327 confluence is the ceiling to beat |
| MACD | 6.8910 < signal 8.2562; histogram −1.3652 | **Bearish crossover**, line still >0 | Momentum break, not a level break |
| RSI | 43.24 (from 61.66; peaked 71.65 on 07-17) | **Neutral-weak, NOT oversold** | ~11 pts of downside room before June's 32.20 analogue |
| Volatility | ATR 9.87 = 3.20% of price; Boll bandwidth 12.4%; %B 0.116 | **Expanded** | Halve/shrink size vs. mid-July |
| July leg | 07-02 breakout close 308.63 vs. today 308.91 | **Fully round-tripped** | The July advance has been erased |
| Drawdown | −9.16% from 07-28 close 340.08; −10.35% from 07-29 high 344.57 | Corrective | Room remains to 200-SMA (−10.0%) |
| Primary bias | Tactical **bearish/defensive** inside a strategic **bull** trend | Neutral-to-underweight | Wait for reclaim of 312.66 or loss of 300.00 |
| Invalidation of bear case | Close above **327.24** (10-EMA/VWMA) | Trend repaired | Then 333.43 / 340.08 / 344.57 back in play |
| Invalidation of bull case | Close below **300.00** | Structure lost | Targets 289.36 → 277.96 / 274.21 |

**Bottom line on AAPL:** the data supports a *damaged but not broken* uptrend. The 200-SMA, its slope, and the wide positive 50/200 spread argue the bull market is alive. But the volume (2.6× normal), the MACD crossover, the close below the 50-SMA, the price −5.35% below VWMA, and — most importantly — an RSI at only 43 (no oversold cushion) argue strongly that the *path forward is lower before it is higher*. The single defensible plan is: **no new longs until 312.66 is reclaimed; no aggressive shorts until 300.00 fails; size down for ATR 9.87.**