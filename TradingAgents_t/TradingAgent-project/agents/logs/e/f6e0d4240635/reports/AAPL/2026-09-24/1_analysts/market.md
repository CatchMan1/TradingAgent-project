# AAPL — Multi-Timeframe Technical Report
**As of close 2026-09-24**

---

## 1. Bottom Line

AAPL is in a **well-established primary uptrend that is currently pausing, not reversing**. Price sits above all three key moving averages (10 EMA, 50 SMA, 200 SMA) in correct bullish sequence, the 50/200 SMA spread is widening, and the volume-weighted average price has risen on **21 consecutive sessions**. However, the *thrust* of the move has measurably decayed since the 2026-09-22 high: MACD histogram has contracted four sessions in a row, RSI has rolled from 66.9 to 61.3, and the 10 EMA's daily increment has collapsed from +1.49 to +0.39.

**Verdict: constructive but do not chase at 335.92.** The setup favors (a) holding existing longs with a defined trail, and (b) adding on either a controlled pullback into 328–330 or a volume-confirmed breakout above 345.34. Buying here offers roughly **0.7:1 reward-to-risk** to the recent high against a 2-ATR stop — a poor entry inside an intact trend.

---

## 2. Data Integrity Note

The OHLCV from `get_stock_data` and the `get_verified_market_snapshot` **agree exactly** on the latest session — open 336.72, high 338.91, low 334.30, close **335.92**, volume **24,733,100**. No discrepancy to flag. All price levels and indicator values below are sourced from the verified snapshot or from `get_indicators` output on the same frozen row.

One scale caveat: the snapshot reports `mfi = 0.639429`, which is a **0–1 normalized** reading (≈64 on a conventional 0–100 scale), not a raw MFI. I treat it as ≈64 and do not build any conclusion that depends on the exact scale.

---

## 3. Trend Structure — Full Bullish Stack, But Short-Term Slope Is Rolling Over

| Average | Value | Price vs. Average | Slope (last 10 sessions) |
|---|---|---|---|
| 10 EMA | 334.16 | **+0.53%** | Rising, but decelerating |
| 50 SMA | 321.68 | **+4.43%** | +4.44 pts (~+1.4%) |
| 200 SMA | 287.45 | **+16.86%** | +3.57 pts (~+1.3%) |

**Stack is textbook bullish:** price (335.92) > 10 EMA (334.16) > 50 SMA (321.68) > 200 SMA (287.45). The 50/200 spread is **34.23 points** and *widening* — the 50 SMA added +4.44 points over ten sessions while the 200 added only +3.57. This is a golden-cross regime that is still accelerating at the structural level, not maturing.

**The nuance is in the short-term slope.** The 10 EMA's daily increments tell the story plainly:
- 2026-09-21: 331.56 → 2026-09-22: 333.05 (**+1.49**)
- 2026-09-23: 333.77 (**+0.72**)
- 2026-09-24: 334.16 (**+0.39**)

The 10 EMA has gone from advancing 1.49 points a day to 0.39 in three sessions — a **74% collapse in the rate of change**. Price closed only 1.76 points above that average, versus roughly 5 points above it on 9/22. This is the signature of a trend *catching its breath*, not of distribution. Notably, the 10 EMA-to-20 SMA gap (334.16 vs 328.07 = **6.09 points, 1.8%**) is the most stretched part of the fan — precisely where mean-reversion pressure builds.

**Two structural shocks worth remembering.** This instrument has produced two single-session air pockets inside the retrieved window:
- 2026-07-30 close 333.43 → 2026-07-31 close 308.91 = **–7.36%** (intraday low 300.00) on **132.5M** shares.
- 2026-06-24 close 293.08 → 2026-06-25 close 275.15 = **–6.12%** on **107.0M** shares.

**Implication:** an ATR of 6.96 (2.07% of price) materially *understates* the tail risk of a stop being gapped through. Size positions on event-gap risk, not on ATR alone.

---

## 4. Momentum — The Core Tension in This Setup

**MACD (line 6.02 / signal 5.21 / histogram 0.81).** The MACD line turned positive on 2026-08-28 (small negative the prior session) and the histogram crossed above zero on **2026-08-26** — a clean, early trend-resumption trigger that has been correct for a month. But the histogram has now fallen for four straight sessions: **1.69 (9/17) → 1.60 (9/18) → 1.61 (9/21) → 1.54 (9/22) → 1.20 (9/23) → 0.81 (9/24)**. The MACD line itself peaked at 6.25 on 9/22 and has ticked down to 6.02. Momentum is **still positive but losing force** — a deceleration, not a crossover. A histogram break below zero would be the confirmation of a deeper consolidation.

**RSI 61.32.** RSI has held a bullish 50–67 band since 2026-09-09 (49.35 on 9/9 → 66.88 on 9/22 → 61.32 today). Crucially, **it never reached 70** on this leg. That matters: the pullback is occurring from *non-overbought* conditions, which historically argues for rotation rather than reversal. The 9/4–9/9 dip to 50.20–49.35 was bought aggressively (9/10 +3.5% on 70.0M shares), showing responsive demand on weakness.

**The one genuine warning sign — a mild negative momentum divergence.** On 2026-09-22, price printed an intraday high of **345.34**, exceeding the prior swing high of **344.57** (2026-07-29). Yet:
- MACD line: **6.25** vs **9.45** at the July peak — a far lower momentum reading
- RSI: **66.88** vs **68.90** at the July peak — a lower high

A marginal new price high on materially weaker momentum is a **real but unconfirmed** divergence. It is a single instance, it is intraday-only (the 9/22 close of 339.75 did *not* exceed the 7/28 record close of 340.08), and price has not broken any support since. Treat it as evidence for *consolidation before continuation*, not as a short signal.

---

## 5. Volatility and Bollinger Structure — Compression at the Top

| Band | Value | Price Position |
|---|---|---|
| Upper | 345.12 | Price is **2.74%** below |
| Middle (20 SMA) | 328.07 | Price is **+2.39%** above |
| Lower | 311.02 | Price is **+8.02%** above |

- **%B = 73.0%** — upper third of the envelope, consistent with trend strength but short of the 80%+ "band-walk" extreme.
- **Bandwidth = 10.39%** — the envelope has been re-expanding after compressing in late August (upper band bottomed at 317.04 on 8/27, lower at 289.77 on 8/20).
- **ATR 6.96**, down from a local peak of 8.05 on 2026-09-11 — volatility is *contracting* into the highs.
- **Today's range was 4.61 points = 0.66 ATR** — a narrow-range session.

**The critical confluence: the upper band (345.12) is sitting almost exactly on the 9/22 high (345.34).** That is a 0.06% coincidence — a single decisive level where the breakout zone, the prior high, and statistical overbought all converge. This is the single most important price on the chart right now.

Narrow ranges plus contracting ATR plus a confluence level typically precedes an **expansion move within 1–2 weeks**. Direction is not yet determined; the resolution itself is the signal.

**ATR-derived levels (from close 335.92):**
- –1 ATR = **328.96** → essentially the 20 SMA at 328.07. Supports the 328–329 zone.
- –2 ATR = **321.99** → the 50 SMA sits at 321.68, a **0.10%** gap. An unusually clean structural stop.
- +1 ATR = **342.88** → almost exactly the 2026-07-28 high of 342.89.
- +2 ATR = **349.84**, and 345.34 + 1 ATR = **352.30**.

---

## 6. Volume and Participation — Accumulation, Then a Genuine Volume Dry-Up

**VWMA has risen on every single session from 2026-08-17 (311.96) to 2026-09-24 (329.86)** — 21 consecutive up-days in a volume-weighted average is a strong, unambiguous accumulation footprint. Price at 335.92 is **1.84% above VWMA**, meaning the average dollar is in profit and there is no overhead supply from recent buyers pressuring the tape.

**The volume pattern on the September advance vs. the pullback is supportive:**

| Date | Close | Change | Volume |
|---|---|---|---|
| 09-10 | 326.57 | +3.56% | 70.0M |
| 09-11 | 332.27 | +1.75% | 50.7M |
| 09-17 | 337.00 | +1.38% | 36.7M |
| 09-22 | 339.75 | +0.23% | 40.7M |
| 09-23 | 337.02 | –0.80% | 31.7M |
| **09-24** | **335.92** | **–0.33%** | **24.7M** |

The down-days since the high have come on **lighter volume than the up-days** — the opposite of distribution. And **2026-09-24's 24.73M is the lowest volume in the entire 147-session retrieved history** (prior lows: 25.87M on 8/25, 26.22M on 3/11), just **58% of the ~42.6M average across the last 21 sessions**.

That is a meaningful, nuanced read: **a pullback that cannot attract sellers.** It also means the pullback carries no informational weight — low-volume declines are easy to reverse.

*Two volume caveats:* (1) 2026-09-18's 86.6M is a **quarterly options-expiry / index-rebalance artifact**, not a conviction day — do not annualize it. (2) MFI at ≈64 is in the same neutral-bullish zone as RSI, showing **no money-flow divergence** against price.

---

## 7. Key Level Map

**Resistance (ascending):**
| Level | Source |
|---|---|
| **345.34** | 2026-09-22 intraday high — the decisive level |
| 345.12 | Bollinger upper band (confluence) |
| 344.57 | 2026-07-29 high |
| 342.89 | 2026-07-28 high / price +1 ATR |
| 340.08 | 2026-07-28 record close in window |

**Support (descending):**
| Level | Source | Distance |
|---|---|---|
| 334.16 | 10 EMA | –0.53% |
| 331.34 | 2026-09-15 close | –1.36% |
| **328.07–330.00** | 20 SMA / VWMA 329.86 | –2.39% |
| 325.13 | 2026-09-01 close | –3.21% |
| **321.68–321.99** | 50 SMA / price –2 ATR | –4.23% |
| 315.34 | 2026-09-09 close (rally origin) | –6.14% |
| 302.56–303.42 | August base | –9.8% |
| 300.00 | 2026-07-31 low | –10.7% |

---

## 8. Scenario Framework

**Bull continuation (base case, ~50%).** A close above **345.34** with volume ≥ **64M** (1.5× the 21-day average) opens **349.84–352.30** (ATR-derived), with a measured-move extension toward 359. Prior evidence supports this: the entire 7/29–7/31 decline (344.57 → 300.00) has already been retraced in full, and VWMA's unbroken 21-session climb shows no supply overhang.

**Base-case consolidation (most likely near term, ~35%).** Price chops in a **328–345** range for one to three weeks while the 10 EMA catches down toward the 20 SMA, RSI resets to 50–55, and the MACD histogram makes a controlled retreat toward zero without the MACD line crossing the signal. This resolves the overbought short-term extension without breaking the intermediate trend.

**Bear reversal (~15%).** Requires a *close* below **328.07** on above-average volume, confirmed by a MACD line/signal bearish crossover (currently the gap is only 0.81 and shrinking fast) and the 10 EMA crossing below the 20 SMA. First downside objective then **321.68–321.99** (50 SMA / 2 ATR), then 315.34. Only a break of 315.34 would invalidate the intermediate uptrend.

---

## 9. Actionable Plans

**Plan A — Pullback accumulation (best risk/reward).** Buy **328.00–330.00** (20 SMA + VWMA + –1 ATR all cluster here), stop **319.50** (below the 50 SMA and 2 ATR), target 1 **345.00**, target 2 **352.30**.
- Risk ≈ 2.8%, reward to T1 ≈ 4.7% → **R:R ≈ 1.7:1**; to T2 **≈ 2.6:1**.
- Confirmation to wait for: RSI holding ≥50 and a bullish reversal candle on above-average volume.

**Plan B — Breakout continuation.** Buy a **close above 345.34** with volume ≥64M; stop **338.50** (below the breakout base / under 1 ATR); target **352.30**, then 359.
- Risk ≈ 2.0%, reward ≈ 2.0% at T1 → **R:R ≈ 1.0:1**, so scale in and trail rather than take a full position at the trigger.
- Do **not** buy the intraday poke through 345.34 — the 9/22 false marginal high is the cautionary example.

**Plan C — Existing longs.** Hold. Trail the stop at **321.50** (under the 50 SMA); that is 4.3% of risk and sits at a structural level rather than an arbitrary one. If the MACD line crosses below its signal while price is still above 328, tighten to **327.50**.

**Avoid:** initiating at 335.92. To the 345.34 high the upside is **2.80%**; to a 2-ATR stop (321.99) the downside is **4.15%** → **R:R ≈ 0.67:1**. The trend is good; this *price* is not the entry.

---

## 10. Monitoring Checklist

1. **345.34 on volume** — the single decisive resolution trigger.
2. **MACD histogram** — a close below 0 flips the momentum regime (currently 0.81, falling ~0.4/session, so ~2 sessions from zero at this rate).
3. **10 EMA (334.16)** — loss of this on a closing basis is the first crack; a 10/20 SMA cross would confirm.
4. **Volume on down-days** — continue to require down-volume below up-volume. A 50M+ distribution day would change the read.
5. **Bandwidth (10.39%)** — further compression precedes an expansion move; position ahead of it, not during it.

---

## Selected Indicators and Rationale

| Indicator | Value (2026-09-24) | Why It Was Selected |
|---|---|---|
| **close_10_ema** | 334.16 | The immediate pivot holding the trend; its *slope* revealed the deceleration that no other single metric showed |
| **close_50_sma** | 321.68 | Intermediate trend anchor and dynamic support; converges with the 2-ATR stop at 321.99 for a high-quality risk level |
| **close_200_sma** | 287.45 | Confirms the primary regime and validates the widening 50/200 golden-cross spread |
| **macdh** | 0.81 | Captures momentum *rate of change*; its four-session contraction is the key warning, earlier than any crossover |
| **rsi** | 61.32 | Establishes the pullback is from non-overbought levels; exposes the mild price/MACD/RSI divergence at 345.34 |
| **boll_ub** | 345.12 | Its 0.06% convergence with the 9/22 high creates the decisive breakout/rejection level |
| **atr** | 6.96 | Position sizing and stop placement; also identifies the event-gap risk ATR understates |
| **vwma** | 329.86 | Confirms accumulation via 21 consecutive rises and flags the 328–330 support confluence |

---

## Key Points Summary

| Dimension | Reading | Evidence | Signal |
|---|---|---|---|
| **Primary trend** | Strong uptrend | Price 16.86% above 200 SMA (287.45); 50 SMA above 200 and widening (+4.44 vs +3.57 over 10 sessions) | Bullish |
| **Intermediate trend** | Intact, rising | Price 4.43% above 50 SMA (321.68), which added 4.44 pts in 10 sessions | Bullish |
| **Short-term trend** | Pausing | 10 EMA increments 1.49 → 0.72 → 0.39; price only +0.53% above it | Neutral / cooling |
| **Momentum** | Positive but decaying | MACD 6.02 > signal 5.21, but histogram 1.69 → 0.81 over four sessions | Weakening |
| **Overbought risk** | Low-to-moderate | RSI 61.32, never exceeded 70 on this leg; %B = 73.0% | Not extended |
| **Momentum divergence** | Mild, unconfirmed | New high 345.34 vs lower MACD (6.25 vs 9.45) and lower RSI (66.88 vs 68.90) | Caution |
| **Volatility** | Contracting | ATR 6.96 from 8.05 on 9/11; today's range 0.66 ATR; bandwidth 10.39% | Coiling |
| **Participation** | Accumulation, then dry-up | VWMA up 21 straight sessions 311.96 → 329.86; 9/24 volume 24.7M = lowest in 147 sessions | Bullish |
| **Decisive level** | 345.34 | Equals Bollinger upper band 345.12; +2.74% from close | Breakout / rejection pivot |
| **Primary support** | 328.07–330.00 | 20 SMA + VWMA 329.86 + –1 ATR 328.96 | Buy zone |
| **Trend invalidation** | 321.68–321.99 | 50 SMA + 2 ATR; only 315.34 breaks the intermediate trend | Stop zone |
| **Action** | Hold, don't chase | R:R 0.67:1 at spot vs. 1.7:1 into 328–330 | Accumulate on pullback |

*All figures derive from the verified snapshot and `get_indicators` output for 2026-09-24. No claim here relies on historical support/resistance bounces that the tool output does not directly evidence.*