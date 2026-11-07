# AMZN — Technical Analysis Report
**Analysis date: 2026-09-03 | Last close: $258.90**

All price, volume, and indicator values below are taken from `get_verified_market_snapshot` (2026-09-03) and the indicator series; the two sources agree exactly. No conflicting figures were found.

---

## 1. Selected Indicators (8) and Why

| Indicator | Value (2026-09-03) | Role in this setup |
|---|---|---|
| **close_10_ema** | 259.28 | Fast trend filter — AMZN is stalling right at it; the immediate battle line |
| **close_50_sma** | 253.32 | Medium-term trend / dynamic support; sits under the Sep 1–2 lows |
| **close_200_sma** | 238.99 | Primary trend anchor; confirms the long-term uptrend is unbroken |
| **macd** | 0.460 | Momentum regime; still >0 but collapsing toward a zero-line test |
| **macdh** | −1.354 | Measures whether the bearish momentum is accelerating or fading (it is fading) |
| **rsi** | 49.90 | Neutral momentum gauge; shows an orderly, non-panicky pullback |
| **atr** | 6.758 | Volatility-scaled stops and position sizing (2.61% of price) |
| **vwma** | 260.06 | Volume-weighted "true cost basis" of recent buyers; price is *below* it = supply overhead |

Bollinger Bands (boll 262.995 / ub 275.523 / lb 250.468) are used from the snapshot as a range framework rather than as separate selectable series, avoiding redundancy with the 50 SMA (Bollinger middle is itself a 20 SMA).

---

## 2. Primary Trend: Up, but Capped

- Close **$258.90** is **+2.20% above the 50 SMA** ($253.32) and **+8.33% above the 200 SMA** ($238.99).
- The 50 SMA is **above** the 200 SMA (253.32 vs 238.99, a **+5.99% spread**), and **both are rising** across the lookback window (50 SMA 247.59 → 253.32 since Aug 10; 200 SMA 236.82 → 238.99 over the same span). That is a textbook bullish structural backdrop.
- Longer arc: close on **2026-03-02 was $208.39** vs **$258.90** on 2026-09-03, i.e. **+24.24%** over roughly six months, with a June drawdown (low close $227.01 on 2026-06-25) that was fully recovered.

**Conclusion:** the *strategic* trend is intactly bullish. The question is purely tactical — whether the August pullback is finished.

---

## 3. Short-Term Structure: A Post-Gap Distribution That Is Losing Steam

The dominant event in the data is the **earnings-type repricing of 2026-07-30 → 07-31**:

- 2026-07-30 close **$235.50** → 2026-07-31 close **$271.58**, a **+15.32%** single-session move on **129.1M** shares (vs. a 20-day average near 33M).
- It left an **unfilled gap between the 2026-07-30 high ($239.82) and the 2026-07-31 low ($262.01)**.
- Peak close: **$284.02 on 2026-08-03** (intraday high **$287.20**).

Since that peak, AMZN has been in a controlled unwind:

- **$284.02 (Aug 3) → $254.98 (Sep 2) = −10.22%**, a five-week decay of lower highs (278.09 Aug 10 → 266.40 Aug 19 → 264.36 Aug 31 → 255.82 Sep 1).
- Critically, **RSI never reached oversold** during this slide — trough of **46.33 on 2026-09-01**, versus the July 29 bottom reading of **33.31**. Sellers have been persistent, not panicked.
- **2026-09-03 broke the sequence**: close **$258.90**, **+1.54%**, with an intraday low of **$256.00** above the prior two sessions' lows ($251.93 Sep 1, $253.40 Sep 2). That is a short-term higher low and the first constructive bar in two weeks.

### Where price sits inside the machinery
- **vs. 10 EMA ($259.28): −0.15%** — price is literally pinned to its short-term average, a compression point.
- **vs. VWMA ($260.06): −0.45%** — the volume-weighted cost of recent buyers is *above* the market. Holders in the August range are underwater, which is why 260–262 keeps capping rallies.
- **%B = 0.34** — price is in the **lower third** of the bands (250.47–275.52), below the mid-band ($263.00) by **−1.56%**. Band width is **$25.06, or 9.53% of the mid**, i.e. still a wide, two-sided regime.

---

## 4. Momentum: Bearish Cross in Place, But Decelerating

**MACD:** the line peaked at **8.432 on 2026-08-11** and has bled to **0.460**. The signal sits at **1.814**, so MACD has been below signal since the **2026-08-17** histogram flip (histogram −0.310 that day). This is an unresolved bearish crossover.

**But the histogram is contracting:** −1.585 (Sep 2) → **−1.354 (Sep 3)**, the first meaningful improvement in over a week, and the MACD line's daily decline is flattening (1.094 → 0.567 → 0.460). Two readings to manage:

1. **A MACD zero-line break (line < 0)** would confirm medium-term momentum loss — the line is only 0.46 away, roughly one ATR/15 of daily drift. This is the single most important mechanical level in the report.
2. **A histogram turn positive** (a fresh bullish crossover) would be the first evidence the correction is over. Neither has happened yet.

**RSI:** **49.90** — dead neutral, having recovered from 46.33. There is no divergence signal available in the data (no lower price low paired with a higher RSI low through Sep 1 — RSI made a marginally higher low at 49.9 vs 46.3 while price made a marginally higher close, which is a mild confirmation of stabilization, not a divergence).

---

## 5. Volume: The Missing Piece of the Bull Case

- **2026-09-03 volume: 26.89M vs. a 20-day average of ≈32.85M (0.82×)**. The bounce is *not* demand-confirmed.
- The strongest up-volume in the August range was **2026-08-28** (close $266.43 on **49.55M**) — and that rally was fully given back by Sep 1–2. That looks like supply into strength, not accumulation.
- Down-day volumes have been unremarkable (Sep 1: 31.70M; Sep 2: 24.01M), meaning the decline is drift rather than capitulation — supportive of a basing thesis, but also of a market that hasn't cleared its overhead.
- **VWMA ($260.06) is above price and falling slowly** (from 272.05 on Aug 20 to 260.06). Until price closes above it, volume-weighted flow remains net distributional.
- Data-integrity note: **2026-06-26 printed 248.37M shares**, a clear index-rebalance-style outlier; exclude it from any average-volume calculation.

---

## 6. Levels That Matter (all derived from tool output)

**Resistance**
| Level | Source |
|---|---|
| **$258.90–259.28** | Last close / 10 EMA — immediate pivot |
| **$260.06** | VWMA — must be reclaimed to neutralize the August supply |
| **$263.00** | Bollinger middle band |
| **$266.43–267.56** | Aug 28 close / Aug 28 high (last supply shelf) |
| **$272.27–273.23** | Aug 11 close / Jul 31 high |
| **$275.52** | Bollinger upper band |
| **$284.02 / $287.20** | Aug 3 close / high — the cycle top |

**Support**
| Level | Source |
|---|---|
| **$256.00** | Sep 3 low (short-term higher low) |
| **$253.32–253.40** | **50 SMA + Sep 2 low — key confluence** |
| **$251.93** | Sep 1 low |
| **$250.47** | Bollinger lower band |
| **$239.82–262.01** | Unfilled 7/30→7/31 gap zone; price is in its **upper half** |
| **$238.99** | 200 SMA — the line in the sand |

The **$250.47–$253.32 cluster** (lower band + 50 SMA) is the most important confluence on the chart: three of the last four sessions' lows (251.93 / 253.40 / 256.00) have been formed inside or just above it.

---

## 7. Scenario Playbook

### A. Base case (≈50%): Range churn, $250–$263
RSI ~50, MACD near zero, price mid-gap, and below-average volume all point to two-way chop. Trade the edges, not the middle. Sell rallies into 260–263; buy the 253–255 retest.

### B. Bullish resolution (≈30%): Reclaim of the 260–263 shelf
**Trigger:** a daily close **above $260.06 (VWMA)** on volume **>32.9M** (20-day average), ideally with the MACD histogram turning positive and RSI >55.
- Entry ~260.50; **stop $250.30** (below the lower band and the 50 SMA; this is ~1.5× ATR of $10.14). Risk $10.20.
- Targets: **$267.56** (+$7.06, 0.7R) → **$272.50** (+$12.00, 1.2R) → stretch **$275.52** (1.5R).
- *Note the asymmetry is only fair at 260.* A better version of the same trade is **buying the $253–255 test with a stop at $249.00** (below the band): risk ~$5, first target $263.00 = **1.8R**, second $267.56 = **2.7R**. That is the higher-quality expression of the bullish thesis.

### C. Bearish resolution (≈20%): Loss of the 250.5–253.3 shelf
**Trigger:** a daily close **below $250.47** on expanding volume, plus a MACD zero-line break.
- That opens the lower half of the gap: **$245.22** (Jun 8 close) → **$240** area → **200 SMA $238.99** (−7.7% from spot).
- Stop for any short/fade: **$264.00** (above the mid-band and the Aug 31 high).

### Risk management using ATR
- Daily ATR = **$6.758 (2.61% of price)**, down from a post-gap peak of **$9.98 on 2026-08-05** — volatility is compressing, which favours tighter stops and smaller stops-in-waiting but also warns of an imminent expansion move.
- Practical stop distances: 1×ATR = $252.14 (coincides with the 50 SMA); 1.5×ATR = $248.77 (below the lower band); 2×ATR = $245.38 (gap-fill zone).
- Size positions at **≤1% account risk per 1.5 ATR**, i.e. a 3.9% stop implies ~25% notional per unit of risk budget. *Caveat: no verified account or portfolio data was provided — these are mechanical suggestions, not personalized advice.*

---

## 8. Bottom Line

AMZN is in a **bullish primary trend (price +8.3% over the 200 SMA, 50 SMA rising above a rising 200 SMA) that is fighting a bearish short-term tape (below 10 EMA, below VWMA, below Bollinger mid, MACD below signal, negative histogram).** The correction, down **−10.22% from the Aug 3 close of $284.02**, is decelerating rather than breaking down: RSI held above 46, the histogram just contracted for the first time in a week, and support formed inside the **$250.5–$253.3** confluence.

The decisive variable is **$260.06 (VWMA)**: above it, the August distribution is neutralized and 267.5 → 272.5 reopens. Below the **$250.47** lower band, the unfilled gap toward **$239** and the 200 SMA becomes the magnet. **Because the Sep 3 bounce came on 0.82× average volume, it does not yet qualify as confirmation** — the correct stance is patience with a defined trigger in each direction, not anticipation.

---

## Summary Table

| Factor | Reading (2026-09-03) | Interpretation | Bias |
|---|---|---|---|
| Close | $258.90 (+1.54% d/d) | First bounce after 5 down weeks | Mildly constructive |
| 10 EMA | 259.28 (price −0.15%) | Pinned at the pivot; unbroken | Neutral |
| 50 SMA | 253.32 (price +2.20%) | Rising medium-term support | Bullish |
| 200 SMA | 238.99 (price +8.33%) | Primary uptrend intact | Bullish |
| 50/200 spread | +5.99% | Golden-cross structure | Bullish |
| MACD / Signal | 0.460 / 1.814 | Bearish cross, line near zero | Bearish |
| MACD Histogram | −1.354 (from −1.585) | Decelerating bearish momentum | Turning neutral |
| RSI | 49.90 (trough 46.33 on Sep 1) | Neutral, no oversold flush | Neutral |
| Bollinger mid / ub / lb | 262.995 / 275.523 / 250.468 | %B = 0.34, lower third | Bearish tactical |
| VWMA | 260.06 (price −0.45%) | Overhead supply; cost basis above spot | Bearish |
| ATR | 6.758 (2.61% of price) | Volatility compressing from 9.98 (Aug 5) | Regime shift pending |
| Volume (Sep 3) | 26.89M vs 20-day avg ≈32.85M | Bounce is NOT demand-confirmed | Bearish qualifier |
| Primary support | **$250.47–$253.32** | Bollinger lower + 50 SMA + Sep 1–2 lows | Must hold |
| Primary resistance | **$260.06–$263.00** | VWMA + Bollinger mid | Must break |
| Actionable view | **No chase at 258.9** | Buy 253–255 w/ stop 249 (1.8R+), or buy strength >260 on >33M volume; short below 250.4 | Neutral / tactical |