# GOOGL — Multi-Timeframe Technical Report (as of 2026-09-18)

## 1. Verification note

I pulled the full OHLCV history (2025-09-18 → 2026-09-18, 252 rows) and then called `get_verified_market_snapshot` for 2026-09-18. **All indicator values in that snapshot match the `get_indicators` series exactly** (no conflicts to flag): close_50_sma 345.5772, close_200_sma 337.4959, close_10_ema 343.6237, macd −0.3208, macds −1.8654, macdh +1.5445, rsi 54.99, boll 341.7865, boll_ub 352.7962, boll_lb 330.7768, atr 8.4006, vwma 341.1005. Any figure below that is derived (averages, % changes, slopes) is my own arithmetic on those rows and is labeled as such. The snapshot's `mfi` reads 0.52744, which looks like a normalized 0–1 scale rather than the standard 0–100, so I did **not** use it.

**Latest verified session (2026-09-18):** open 357.31, high 359.44, low 348.45, close **349.54**, volume **47.63M**. That is +0.64% versus the 2026-09-17 close of 347.33 — but −2.75% from the intraday high, with the close sitting only **9.9% up from the day's low** inside the range. It was also an outside day (took out both the prior high of 349.50 and the prior low of 343.89).

---

## 2. Trend hierarchy: intact primary uptrend, damaged intermediate trend, repairing short-term trend

**Long term (200 SMA) — constructive.** The 200 SMA is at **337.50** and still rising (~+0.16 pts/session from 335.94 on 2026-09-04 to 337.50 on 2026-09-18). Price is **+3.57%** above it. On a 12-month basis GOOGL is up from 252.03 (2025-09-18) to 349.54, **+38.7%**, and it is +11.7% YTD from the 2025-12-31 close of 313.00. The primary trend is up.

**Intermediate (50 SMA) — still down, but decelerating.** The 50 SMA is **345.58**, *below* price but in a persistent decline from 372.80 on 2026-07-13. The important nuance is the **rate of change**: it fell −0.75 pts/session between 2026-07-22 (367.48) and 2026-08-21 (351.77), but only −0.30 pts/session between 2026-09-04 (348.57) and 2026-09-18 (345.58). A flattening 50 SMA after a sharp decline is a basing characteristic, not a fresh breakdown characteristic.

**Short term (10 EMA) — clearly turning up.** The 10 EMA is **343.62**, up from 337.63 on 2026-09-10. It sits **1.95 points below the 50 SMA**, down from a 10.0-point gap on 2026-09-10. At that +1.34 pts/session convergence rate, a **10 EMA > 50 SMA cross is roughly 1–3 sessions away** if the pace holds. That has not happened yet — this is a setup, not a confirmed signal.

**The 50/200 spread is the single biggest structural risk.** 50 SMA − 200 SMA = **+8.08 points** (50 above 200). The gap has compressed from 12.63 on 2026-09-04 (−0.46/session). If both slopes persist, the gap closes in roughly **18 sessions, i.e., mid-October 2026** — that is a live death-cross watch. Note the cross is not imminent *this week*, and the decelerating 50 SMA slope is exactly what could prevent it. But it is the reason I would not treat the long-term uptrend as unambiguously safe.

**Where price sits in the larger range:** GOOGL peaked at an intraday **408.61 on 2026-05-18** (highest close 402.62 on 2026-05-13) and is **−14.5%** from that high. The correction low was **314.90 on 2026-07-23** (close 317.69). Price is **+10.0%** off that low and +5.1% off the 2026-09-10 close of 332.60.

---

## 3. The 2026-09-18 session is the story: high-volume rejection, not a breakout

Three details make this candle a warning rather than a triumph:

1. **The gap fully filled intraday.** Open 357.31 versus the prior close of 347.33 was a +2.87% gap. The session low of **348.45** is *below* the prior day's high of 349.50, so the entire gap was filled the same day. That is the signature of an exhaustion gap, not a breakaway gap.
2. **The close was in the bottom tenth of the range** — 349.54 against a 348.45–359.44 range (9.9% of range). Buyers who chased the open are underwater by 7.77 points.
3. **Volume was climactic.** 47.63M shares versus a **20-session average of ~25.4M** that I computed from the daily rows — about **1.9x**. It is the heaviest volume since 2026-07-23 (69.4M).

This mirrors the **2026-08-05** session almost exactly: high **384.48**, close 362.43 (−4.03%), volume 46.93M, closing in the bottom 20% of the range on a heavy-volume day. Price then fell **−14.8% over 25 sessions** to 327.74 (2026-09-10). I am not claiming a repeat — that is n=1 — but it is the closest structural analog in the dataset and it argues against assuming the Sep 18 high gets reclaimed quickly.

Contrast that with **2026-07-31**, the other recent high-volume day: +6.7% (333.66 → 356.13) on 46.50M with the close at 86.8% of the day's range. That was accumulation. Sep 18 is the opposite composition — same volume, opposite close location.

**Level confluence worth noting:** the 2026-04-29 close was 349.94, the last close before the +10.0% gap-up on 2026-04-30 (open 374.07, close 384.80). Since then, three consecutive sessions have clustered at that origin — 2026-09-14 high 349.91, 2026-09-17 high 349.50, 2026-09-18 close 349.54. The 349.5–350 zone is behaving as a pivot/magnet.

---

## 4. Selected indicators and why (8 total)

**1) close_10_ema — 343.62.** Chosen as the fastest legitimate read on momentum, and because it is the first line of defense for the emerging short-term upturn. It has risen five straight sessions. Price closing back below it would invalidate the "repair" thesis quickly.

**2) close_50_sma — 345.58.** Chosen as the intermediate battlefield. Price is only +1.15% above it, so it is close enough to be a real decision point, and its slope change (halving negative slope) is the key evidence of basing versus continuation.

**3) close_200_sma — 337.50.** Chosen as the strategic trend filter and the reference for the 50/200 spread. It also provides the structural invalidation level for any long: 337.50 is 3.4% below spot.

**4) macd — −0.3208 (signal −1.8654, histogram +1.5445).** Chosen over an oscillator because the crossover is fresh and measurable: the histogram flipped positive on **2026-09-14 (+0.573)** after −0.829 on 2026-09-10 and has expanded every session since (+0.915, +0.972, +1.266, +1.545). The MACD line has climbed from −3.905 (2026-09-10) to −0.321. **Crucially, the line is still below zero**, so this is a bullish crossover *below* the zero line — an early bottoming signal that still needs the zero-line reclaim (~1–3 sessions at the current +0.66/session thrust) to become a trend signal.

**5) rsi — 54.99.** Chosen as the "how much room is left" gauge. It is neutral, not overbought, recovering from 39.36 (2026-09-09). There is room to 70. Also constructive: RSI lows are rising — 33.27 (2026-06-26), 31.02 (2026-07-23), **39.36 (2026-09-09)** — a mild positive divergence against price's higher low. The corollary is that Sep 18's rejection was **not** an overbought unwind; it was supply appearing at resistance, which is harder to "fix" with time alone.

**6) boll_ub — 352.80.** Chosen as the immediate resistance and failed-breakout marker. Price closed **0.93% below** it. The 2026-09-18 open (357.31) gapped *above* the band and closed back inside — a textbook band-failure signal.

**7) boll_lb — 330.78.** Chosen as the downside envelope and squeeze measurement. Price is 5.4% (18.76 points) above it. The band rose from 329.23 (2026-08-28) to 330.78 — the *rising* lower band is a quiet positive.

**8) atr — 8.40.** Chosen because this is a risk-management and regime call as much as a directional one. ATR is at a 90-session low (the low was 7.983 on 2026-09-10) and is down 39.7% from 13.93 on 2026-08-05. At 2.40% of spot it is the correct input for stop placement, not a fixed point stop.

*Screened but excluded:* VWMA and the 20 SMA/mid-band are highly correlated with the 50 SMA here; MFI has ambiguous scaling. VWMA is used below strictly as a volume cross-check.

---

## 5. Volatility regime: a compressed coil, mid-range

**Bollinger bandwidth has halved.** (352.80 − 330.78) / 341.79 = **6.44%**, versus **12.01%** on 2026-08-28. ATR at 8.40 confirms the compression independently. Volatility compression of this magnitude typically precedes an expansion move — but it does not tell you the direction, and the prevailing 4-month drift is sideways-to-down from the May high.

**Structure inside the compression is a contracting range:**
- Swing low 314.90 (2026-07-23) → **higher low** 327.74 (2026-09-10), +4.1%
- Swing high 384.48 (2026-08-05) → **lower high** 359.44 (2026-09-18), −6.5%
- A rising lower boundary (314.90 → 327.74 ≈ +0.39 pts/session) and a falling upper boundary (384.48 → 359.44 ≈ −0.84 pts/session) converge in roughly **24 sessions, i.e., late October** — coincidentally the same window as the potential 50/200 death cross. That is the decision window.

**Mid-range location:** using 314.90–384.48 as the working range, 349.54 sits at **49.8%** — dead center. That is why neither direction offers good expectancy *right now*.

**Support shelf (dense):** 10 EMA 343.62, Bollinger mid 341.79, VWMA 341.10 all cluster in **341.1–343.6**, and 1 ATR below spot is 341.14 — an almost exact coincidence with the VWMA. Below that, 200 SMA **337.50**. Then 2 ATR (332.74), the lower band (330.78), and the 327.74 swing low.

**Volume confirms participation but not direction:** VWMA is 341.10 and rising from 339.39 (2026-09-11), with price 2.47% above it. Price > VWMA means the volume-weighted holder base is in profit — constructive — but VWMA *below* the 50 SMA (341.10 vs 345.58) shows the heaviest volume transacted lower, consistent with distribution into strength rather than accumulation at these levels.

---

## 6. Actionable plan

**Bias: neutral-to-constructive, but do not initiate at mid-coil.** The momentum internals (MACD histogram, 10 EMA, RSI, rising lower band) are improving while the price action (Sep 18 rejection, 1.9x volume, bottom-10% close) is deteriorating. Those conflict. Resolve the conflict with price, not with prediction.

**Primary setup — buy the retest, not the breakout.** Wait for a pullback into **343.6–341.1** (10 EMA → VWMA/mid-band) that holds with a reversal close.
- Entry reference ~**344.00**; stop **336.90** (just below the 200 SMA at 337.50, −2.1% from entry, ~0.85 ATR)
- Targets: **352.80** (upper band, +2.6%), **359.44** (Sep 18 high, +4.5%), **371.87** (2026-08-27 upper band, +8.1%)
- Reward/risk: ~1.2:1 to T1, ~2.2:1 to T2, ~3.9:1 to T3. Best expectancy of any setup here.

**Secondary setup — breakout confirmation.** Require a **daily close above 359.44** with volume ≥ the 20-session average (~25M) *and* a close in the top third of the day's range — the exact test Sep 18 failed.
- Entry ~**360.00**; stop **352.80** (upper-band retest, −2.0%)
- Targets: **371.87** then **380.52–384.48** (2026-08-04/08-05 highs). R/R ~1.6:1 and ~3.4:1.

**Bearish setup.** Requires a decisive close below the **341.1–343.6** cluster; a break of 345.58 (50 SMA) alone is not enough because it sits inside the cluster.
- Entry ~**340.00**; stop **349.50** (above the Sep 14–17 highs cluster, +2.8%)
- Targets: **337.50** (200 SMA), **330.78** (lower band), **327.74** (Sep 10 low). R/R ~0.3:1, ~1.0:1, ~1.4:1 — **poor**, which is itself the signal that shorting mid-range is not worth it. Only a break of **327.74** opens 314.90 and would justify a fresh short.

**No-trade zone: 344–352.** Nothing here pays.

**Position sizing (ATR-based, 1% account risk):** a 1-ATR stop (8.40) risks 2.40% → max notional ~41% of account; a 2-ATR stop (16.80) risks 4.80% → ~21%. The 344/336.90 setup risks ~2.1%, implying ~47% notional at 1% risk — cap notional at 25–30% and accept ~0.5–0.6% risk instead, given the event/coil risk.

**What would change the view:**
- *More bullish:* 10 EMA crossing above the 50 SMA **and** MACD reclaiming zero **and** a close above 359.44 — all three, not one.
- *More bearish:* close below 341.10 on above-average volume, or the 50 SMA crossing below the 200 SMA in mid-October.
- *Neutralizing:* another low-volume drift inside 341–353; the squeeze simply extends.

**Key risks not captured by this dataset:** no news, earnings-calendar, options, or peer/macro data was available. A single unscheduled catalyst can invalidate the coil geometry overnight — the Sep 18 gap itself is evidence of that. The dividend of 0.22 (ex-date 2026-09-04) means the close series is not total-return adjusted, but at 0.065% of price it is immaterial to these signals.

---

## 7. Summary tables

| Indicator | Value (2026-09-18) | Signal | Key level / interpretation |
|---|---|---|---|
| Close | 349.54 | Neutral / rejection | Bottom 9.9% of 348.45–359.44 range; +0.64% d/d |
| Volume | 47.63M | **Bearish warning** | ~1.9x the ~25.4M 20-day average (computed); heaviest since 2026-07-23 |
| close_10_ema | 343.62 | Bullish (short-term) | Rising 5 sessions; 1.95 pts below 50 SMA, cross ~1–3 sessions away |
| close_50_sma | 345.58 | Neutral / flattening | −0.30 pts/session vs −0.75 in Jul–Aug; price +1.15% above |
| close_200_sma | 337.50 | **Bullish (long-term)** | Rising ~+0.16/session; price +3.57% above; 3.4% below spot |
| 50 SMA − 200 SMA | +8.08 | **Deteriorating** | Compressed from 12.63 (2026-09-04); death cross ~mid-Oct if slopes persist |
| macd | −0.3208 | Bullish crossover, sub-zero | Histogram +1.5445, positive 5 straight sessions (flipped 2026-09-14) |
| rsi | 54.99 | Neutral, room to run | Up from 39.36 (2026-09-09); rising RSI lows 33.27→31.02→39.36 |
| boll_ub | 352.7962 | Resistance | Close 0.93% below; open gapped above band and failed back inside |
| boll_lb | 330.7768 | Support | Rising from 329.23 (2026-08-28); price +5.4% above |
| Bollinger bandwidth | 6.44% | **Squeeze** | Halved from 12.01% (2026-08-28) |
| atr | 8.4006 | Low volatility | 2.40% of spot; −39.7% from 13.93 (2026-08-05); near 90-day low |
| vwma | 341.1005 | Constructive, but below 50 SMA | Price +2.47% above; heavy volume transacted lower |
| Angle |  |  |  |

| Scenario | Trigger | Invalidation | Targets | R/R |
|---|---|---|---|---|
| **Preferred: buy retest** | Hold of 343.6–341.1 with reversal close (~344 entry) | Stop 336.90 (below 200 SMA) | 352.80 / 359.44 / 371.87 | 1.2 / 2.2 / 3.9 |
| Breakout continuation | Close >359.44 on ≥25M volume and top-third close (~360 entry) | Stop 352.80 | 371.87 / 380.52–384.48 | 1.6 / 3.4 |
| Bearish breakdown | Close <341.10 on above-average volume (~340 entry) | Stop 349.50 | 337.50 / 330.78 / 327.74 | 0.3 / 1.0 / 1.4 (poor) |
| **Current stance** | No position at 344–352 (mid-coil, 49.8% of range) | — | — | Poor expectancy both ways |