# AAPL — Technical Analysis Report (as of 2024-01-22)

**Verification note:** `get_stock_data` and `get_verified_market_snapshot` agree exactly on the 2024-01-22 row (O 192.30 / H 195.33 / L 192.26 / C **193.89** / V 60.13M). **No discrepancies found**; all exact price levels and indicator values below are taken from the verified snapshot and the indicator series.

---

## 1. Where Price Actually Is

AAPL closed at **193.89** on 2024-01-22, up **+1.22%** from 191.56 on 2024-01-19 and **+7.02%** from the 2024-01-05 closing low of 181.18. That move has unfolded in three distinct phases, each directly visible in the frozen rows:

| Phase | Dates | Price behavior |
|---|---|---|
| Sharp drawdown | 2023-12-29 → 2024-01-05 | 192.53 → 181.18 (−5.90%); 2024-01-02 alone was −3.58% |
| Base / accumulation | 2024-01-08 → 2024-01-17 | 181.17–186.74 range; **four separate tests of the 180.2–180.9 zone held** (lows 180.88 on 01-04, 180.17 on 01-05, 180.93 on 01-16, 180.30 on 01-17) |
| Thrust / breakout | 2024-01-18 → 2024-01-22 | +3.26%, +1.55%, +1.22% = **+6.14% in three sessions**, gapping up on 01-18 (open 186.09 vs prior close 182.68) |

The 195.33 intraday high on 2024-01-22 is the strongest print since 2023-12-22 (195.41), and 193.89 is the highest close since 2023-12-20 (194.83). This is a **recovery leg re-entering the upper half of the December distribution**, not a new all-time-high breakout.

---

## 2. Trend Framework — Full Bullish Stack, With a Caveat

**Verified 2024-01-22 values and distance from close (193.89):**

- **close_200_sma = 181.295** → price is **+6.95%** above. Rising steadily (180.69 on 01-12 → 181.30 on 01-22, ~+0.14/day). Long-term trend is unambiguously up.
- **close_50_sma = 190.043** → price is **+2.02%** above. Rising (~+0.24/day; 189.02 on 01-12 → 190.04 on 01-22). Price **reclaimed the 50-day on 2024-01-19** (close 191.56 > 50SMA 189.80) after being below it from 2024-01-02 through 2024-01-18.
- **close_10_ema = 188.237** → price is **+3.00%** above. The 10 EMA bottomed at 185.37 on 2024-01-17 and has hooked up for three straight sessions (185.96 → 186.98 → 188.24).

**The caveat — and it's an important nuance:** the 10 EMA (188.24) is still *below* the 50 SMA (190.04). That is the mechanical footprint of the January dip: the short-term average is still digesting 180–183 prices while the 50-day has barely rolled over. This means the fastest bullish confirmation is still pending: **a 10-EMA cross back above the 50-SMA**, which at current slopes would require a few more sessions of price ≥ 190. Until then, the "stack" is incomplete.

**Golden-cross status:** 50 SMA (190.04) sits **+8.75 points (+4.83%)** above the 200 SMA (181.30), and the spread is widening because both averages are rising. This is a mature, healthy bullish alignment — but also a stale one (it was already positive in mid-December at 182.85 vs 177.05), so it is confirmation, not a fresh signal.

---

## 3. Momentum — A Genuine Reset, With the MACD Still Below Zero

**RSI = 60.69** (verified). The series tells the whole story of the V-shaped recovery:
- 28.79 on 2024-01-05 (oversold)
- 36.71 on 2024-01-17
- 51.59 on 2024-01-18, 56.96 on 2024-01-19, **60.69 on 2024-01-22**

This is a ~32-point round trip in 11 sessions with **no overbought reading yet** — there is still roughly 9 points of headroom to the 70 threshold. Critically, RSI at 60.7 while price is still 2.1% below the 2023-12-14 close (198.11) and 2.4% below that day's 199.62 high is a *healthy* configuration, not a bearish divergence (a divergence would require price at a new high with RSI lower — that has not occurred).

**MACD complex (verified):**
- MACD line = **−0.408** (still below zero)
- Signal = **−1.064**
- Histogram = **+0.656**, and it **flipped positive on 2024-01-19 (+0.203), the first positive reading since 2023-12-18** (+0.014)

So a **bullish MACD crossover has occurred below the zero line**. The MACD line's trajectory is steep and monotonic: −1.926 (01-17) → −1.562 → −1.026 → −0.408. This is the classic early-stage reversal signature: histogram expansion first, then a zero-line test. **A close of the MACD line above zero would be the higher-conviction confirmation**, and at the current pace that test is imminent rather than theoretical. Treat the current signal as *constructive but unconfirmed* — below-zero crosses in choppy tapes produce frequent false starts (e.g., the histogram was positive on 2023-12-13/14 and rolled straight back over).

---

## 4. Volatility & Band Structure — Room to the Upper Band, but Volatility Is Expanding

**Bollinger (20, 2σ), verified:**
- Middle (boll) = **188.118** — price is +3.07% above; this line has been *falling* (194.18 on 12-28 → 188.12 on 01-22), and price has now crossed back above it.
- Upper = **197.356** — only **+1.75%** above the close.
- Lower = **178.880** — 8.39% below.
- Bandwidth = (197.356 − 178.880) / 188.118 = **9.82%** — narrow-to-normal, i.e., the bands are *not* yet in a squeeze or an expansion blowout.

The practical read: **197.4 is the first defined overhead objective and it lines up with the December supply zone** (2023-12-14 high 199.62, 2023-12-21 high 197.08, 2023-12-22 high 195.41). Price is pressing into a *cluster* of resistance, not a clean air pocket.

**ATR = 3.370** (verified), up **+31%** from 2.575 on 2023-12-29 and at the top of the 90-day visible range. That equals **1.74% of the close** — the daily "noise" band is now wide enough that a 2–3 point intraday shakeout is unremarkable. Volatility expanding *into* resistance is a two-sided signal: it validates the strength of the thrust, but it also raises the probability of a failed probe and a wide-swing reversal.

**Risk-management arithmetic (derived from verified ATR):**
- 1×ATR stop ≈ 190.5 — inside the normal noise band; too tight for a swing position.
- 1.5×ATR ≈ 188.8 — sits right at the 10 EMA (188.24) / Bollinger middle (188.12). **This is the logical invalidation for the breakout.**
- 2×ATR ≈ 187.1 — below both the 10 EMA and the band mid, safer for wide stops.

---

## 5. Volume Confirmation — Supportive, Not Euphoric

**VWMA = 185.588** (verified). Price is **+4.47%** above the volume-weighted average price — meaning the volume-weighted cost basis of recent buyers is comfortably in profit, which reduces overhead supply pressure. The VWMA has just **inflected upward** (185.253 on 01-18 → 185.363 → 185.588), the first upturn since mid-December. That is a genuine volume-confirmed shift.

Raw volume from the frozen rows: the 19 sessions from 2023-12-22 through 2024-01-22 average **≈53.9M shares**. The breakout sessions ran **78.0M on 2024-01-18 (~1.45× the recent average)** and **68.9M on 2024-01-19 (~1.28×)**, with 60.1M on 2024-01-22 (~1.12×). **Participation expanded on the up-move and is tapering only modestly as price extends — a constructive, orderly pattern rather than a volume climax.** The one flag: 60.1M on 2024-01-22 is below 01-18/01-19, so the third day of the thrust was the lightest. Watch whether a push through 197–200 attracts volume; a low-volume probe into the December high would be a warning.

---

## 6. Scenario Map (Actionable)

**Bull case — continuation (base case given the evidence):**
- Trigger: sustained hold above the **50 SMA at 190.04**; ideally MACD line crossing above zero.
- Path: **197.36 (Bollinger upper)** → **197.08/199.62 (Dec 2023 highs)** → psychological 200.
- Confirmation: 10 EMA (188.24) crossing above the 50 SMA (190.04), which would re-complete the bullish stack.

**Neutral / consolidation case:**
- A digestion between **188.12 (band mid/10 EMA region, 188.1–188.2) and 195.3–197.4** would be normal consolidation after +6.1% in three sessions. Backing and filling here keeps the MACD histogram positive and lets the 50 SMA catch up.

**Bear/invalidation case:**
- **Close below 188.12** (Bollinger middle + 10 EMA 188.24): the breakout is negated, and the MACD histogram would likely rotate back down.
- **Close below 185.59 (VWMA)**: the volume-weighted recent buyer goes underwater; the January base at 180.2–180.9 and the **200 SMA at 181.30** become the next major test. Note that zone held four times in January — it is well-defined on both sides.

**Position-sizing note:** with ATR at 1.74% of price, a full-size position carries roughly 74% more daily dollar risk than it would have in late December (ATR 2.57). Scale size down ~25–30% relative to a December-era sizing model, or widen stops and reduce units.

---

## 7. Why These Eight Indicators

| Indicator | Role in this specific setup |
|---|---|
| **close_200_sma** | Defines the dominant uptrend and the exact floor (181.30) that the January tests of 180.2–180.9 respected |
| **close_50_sma** | The level just reclaimed (190.04) — the pivot separating breakout from failed breakout |
| **close_10_ema** | Fastest read on the momentum reversal; also the pending cross vs. the 50 SMA |
| **macd** | Confirms the below-zero bullish shift and its (still missing) zero-line breakout |
| **macdh** | The *earliest* signal in this sequence — turned positive 2024-01-19 and is expanding |
| **rsi** | Measures the oversold-to-neutral reset (28.8 → 60.7) with headroom to 70; not redundant with MACD since one is bounded/threshold-based and the other is trend-difference-based |
| **atr** | Sets stops and position size in a market where volatility just rose 31% |
| **vwma** | Distinguishes a genuine volume-backed advance from a thin bounce; price is 4.47% above it |

Deliberately **excluded:** `boll` upper/lower were reviewed as *supplementary reference levels* (197.36 / 178.88) rather than core selections, to avoid doubling up on mean-reversion information already covered by ATR and the moving averages; `macds` was excluded because the histogram carries the same crossover information with more lead time; no second oscillator (e.g., stochastics) was added, per the anti-redundancy rule.

---

## 8. Key Points Summary

| Item | Verified Value (2024-01-22) | Interpretation |
|---|---|---|
| Close | **193.89** | Highest close since 2023-12-20 |
| Session range | 192.26 – 195.33 | 195.33 = highest high since 2023-12-22 (195.41) |
| Volume | 60.13M (≈1.12× 19-session avg ≈53.9M) | Up-move participation tapering slightly |
| close_200_sma | 181.295 | Price +6.95% above; rising; January floor held 4× near it |
| close_50_sma | 190.043 | Price +2.02% above; **reclaimed 2024-01-19** |
| close_10_ema | 188.237 | Price +3.00% above; hooked up, but still **below** the 50 SMA |
| Golden cross spread | 50SMA − 200SMA = **+8.75 (+4.83%)** | Mature bullish alignment, widening |
| RSI | **60.69** | Up from 28.79 (01-05); ~9 pts to overbought; no bearish divergence |
| MACD / Signal / Hist | **−0.408 / −1.064 / +0.656** | Bullish cross **below zero**; histogram positive since 01-19 |
| Bollinger upper / mid / lower | **197.356 / 188.118 / 178.880** | +1.75% to upper band; bandwidth 9.82% |
| ATR | **3.370 (1.74% of price)** | +31% since 2023-12-29; widen stops, cut size |
| VWMA | **185.588** | Price +4.47% above; slope just turned up |
| Invalidation level | **188.12–188.24** | Band mid + 10 EMA; breakout void below |
| First objective | **197.36**, then 197.08–199.62, then 200 | Convergence of Bollinger upper and Dec-2023 supply |

**Bottom line for AAPL:** the tape has shifted from corrective to constructive with real evidence — a four-times-defended long-term support zone near 180 on the 200 SMA, a reclaim of the 50 SMA, a positive MACD histogram flip, an RSI reset out of oversold, and price above the volume-weighted cost basis. What is *not* yet in place is confirmation: the MACD line remains below zero, the 10 EMA remains below the 50 SMA, and price is pushing into a dense December resistance band with rising volatility. The highest-quality trade structure is to treat **190.04 as the long-side line in the sand and 188.12 as invalidation**, targeting **197.36**, sizing to an ATR of 3.37 (≈1.7% daily range) rather than to December-era sizing.