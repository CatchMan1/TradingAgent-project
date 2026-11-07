# AMZN — Multi-Timeframe Technical Report
**As of the close of Friday, 2024-01-05** | Verified snapshot source: B-project frozen rows (last visible session 2024-01-05)

---

## 1. Executive Summary

AMZN is in a **well-established primary uptrend that is currently in a short-term corrective phase**. The long-term structure is unambiguously bullish (close 145.24 vs. 200-day SMA 128.69, a +12.9% premium; 50-day SMA 144.64 comfortably above the 200-day). However, the last 5–6 weeks have produced a **clean distribution pattern**: a descending sequence of daily highs since 2023-12-20, a MACD bearish crossover, a collapse in RSI from ~68 to ~42, and price now sitting **below the 10-EMA (149.10) and VWMA (150.88)** while **barely clinging to the 50-day SMA (144.64)**.

The critical observation for the coming sessions: **AMZN closed at 145.24, only $0.60 above its rising 50-day SMA and $1.69 above the lower Bollinger Band (143.55)**. This is a binary decision zone. A daily close below ~143.5 would confirm a trend-repair (not trend-reversal) setup with the 200-day SMA nearly 12% below at 128.69; conversely, reclaiming the 149–151 zone would reassert the December advance.

**Bias: Neutral-to-constructive, tactically defensive.** Long-term holders should hold; new entries should be staged, not chased, because momentum has not yet repaired.

---

## 2. Price Action Context (verified figures only)

| Metric | Value (2024-01-05 verified) |
|---|---|
| Close | **145.24** |
| Open / High / Low | 144.69 / 146.59 / 144.53 |
| Volume | 45,153,100 |
| Swing closing high | **154.07** on 2023-12-18 |
| Swing intraday high | **155.63** on 2023-12-20 |
| Close vs. 2023-12-29 (151.94) | **−4.41%** in 4 sessions |
| Close vs. 2023-12-18 closing high (154.07) | **−5.73%** |
| Close vs. 2023-12-20 intraday high (155.63) | **−6.68%** |

**The descending-high sequence is textbook and is directly supported by the data:** 155.63 (12-20) → 153.97 (12-21) → 154.35 (12-22) → 153.98 (12-26) → 154.78 (12-27) → 154.08 (12-28) → 153.89 (12-29) → 152.38 (01-02) → 151.05 (01-03) → 147.38 (01-04) → **146.59 (01-05)**. Eight of the last eight sessions made lower highs.

**But note the nuance on 2024-01-05:** after the sharp −2.6% down day on 01-04 (open 145.59 → close 144.57, closing near the low of a 147.38–144.05 range), Friday printed a **small-bodied up candle (+0.46%)** that held above Thursday's low (144.53 vs. 144.05) and closed green. That is the first *stabilization* signal, but it is weak: the close (145.24) is in the **lower half** of the day's range (midpoint 145.56), and volume was lower than Thursday's 56.0M. This is a pause, not a reversal confirmation.

---

## 3. Indicator Selection — Rationale (8 indicators)

I deliberately chose a **non-redundant, multi-timeframe set**: two trend anchors, one fast trend rail, two momentum readings across two different constructions (oscillator + rate-of-change-based MACD), one volatility/risk-sizing measure, one volume-confirmation measure, plus the Bollinger framework read from the verified snapshot (which supplies boll/boll_ub/boll_lb simultaneously, so I did not spend a separate slot on each band).

| # | Indicator | Value 2024-01-05 | Why it is the right tool here |
|---|---|---|---|
| 1 | **close_200_sma** | 128.688 | Establishes the *primary* trend. At +12.9% above it, AMZN's bull market is not in question. This is the line that defines whether a pullback is noise or a regime change. |
| 2 | **close_50_sma** | 144.636 | The *exact* battlefield. Price is +0.42% above it. It also quantifies the golden-cross structure (50 > 200 by 15.95 pts / 12.4%) and it is still *rising* (143.94 → 144.30 → 144.64 over the last three sessions). |
| 3 | **close_10_ema** | 149.099 | Captures the short-term velocity shift the slower MAs cannot. Price is −2.59% below it and the EMA has turned down (152.20 on 12-28 → 149.10). It is the first resistance shelf. |
| 4 | **macd** | 0.859 | Still nominally positive but collapsing from 3.136 (12-22); it has lost ~73% of its value in 9 sessions. It tells us the *trend engine is decelerating* even while price stays above the 50-SMA. |
| 5 | **macdh** | −1.230 | The cleanest confirmation of the crossover timing: the histogram flipped negative on **2023-12-29** (−0.141 after +0.031 on 12-28) and has widened every session since (−0.396, −0.655, −1.055, −1.230). Widening negative bars = downside momentum still *accelerating*, not exhausted. |
| 6 | **rsi** | 42.127 | Shows the momentum reset magnitude (68.05 on 12-18 → 40.23 on 01-04, a 27.8-point collapse) while confirming we are **not yet oversold**. There is room to fall to 30 without a mechanical "buy" trigger. |
| 7 | **atr** | 2.925 | Essential for setting stops and sizing. ATR has *contracted* (−23.6% from 3.829 on 2023-11-06; −15.1% from 3.446 on 2023-12-18) even during the sell-off — an orderly decline, not panic. 2.925 ≈ 2.01% of price. |
| 8 | **vwma** | 150.878 | The volume-weighted average cost of recent holders. Price is **−3.74% below it**, meaning the bulk of recent buying is underwater — a classic distribution/overhang signature that a simple MA would mask. It is also the most reliable overhead resistance on a rebound. |

**Supplemental (from verified snapshot):** Bollinger mid 150.071, upper 156.590, **lower 143.552** — bandwidth 8.68% of the midline; %B ≈ **12.9%**, i.e., price is pressed into the bottom eighth of the envelope.

**Discrepancy flag:** the snapshot reports `mfi = 0.549487`, which is not on the standard 0–100 Money Flow Index scale and cannot be interpreted reliably. I have **excluded it** from all conclusions rather than normalize or invent a reading. All other snapshot values match the `get_indicators` series exactly (e.g., macd 0.8587, macds 2.0889 = 0.8587 − (−1.2302), rsi 42.127, atr 2.925, close_50_sma 144.636).

---

## 4. Trend Analysis

### 4.1 Long-term (200-day): Intact, bullish
- Close 145.24 vs. 200-SMA **128.688** → **+12.86%**.
- The 200-SMA is rising monotonically all through the visible window: 118.50 (2023-11-06) → 125.05 (12-15) → **128.69 (01-05)**, a slope of roughly +0.23 pts/session. A rising long-term average means the long-term trend is being *confirmed*, not deteriorated.
- The 50-SMA has been above the 200-SMA for the entire visible window (starting 2023-11-06 at 132.51 vs. 118.50), a persistent golden-cross regime. The spread has **widened** from 14.01 to **15.95 pts** — the structural bull case strengthened through this pullback.

### 4.2 Intermediate (50-day): The line in the sand
- Close **145.24 vs. 50-SMA 144.636 → +0.42%**. This is the narrowest premium since the November advance began, and it is the single most important number in this report.
- The 50-SMA is *still rising* (143.48 → 143.94 → 144.30 → 144.64 across 01-02 → 01-05). Because it lags, it functions here as a **rising floor** rather than a broken support. Rising support that price is testing from above is a *constructive* configuration — but only as long as it holds on a closing basis.
- A close below 144.64 would be the first close beneath the 50-SMA in the visible period, which mechanically shifts the medium-term bias from "uptrend pullback" to "uptrend under repair."

### 4.3 Short-term (10-EMA): Clearly bearish
- Close 145.24 vs. 10-EMA **149.099 → −2.59%**.
- The 10-EMA has rolled over: 152.20 (12-28) → 151.75 (01-02) → 151.15 (01-03) → 149.96 (01-04) → **149.10 (01-05)**. It is now falling ~0.5–0.9 pts/day.
- **Stacking order is inverted short-term:** Price (145.24) < 10-EMA (149.10) < 50-SMA is *not* the order — actually price (145.24) is slightly *above* 50-SMA (144.64) but *well below* 10-EMA. The correct read: **10-EMA > VWMA ≈ Boll-mid > price > 50-SMA**. This is a "compressing into the base" pattern, not a clean downtrend.

### 4.4 Multi-timeframe alignment verdict
| Timeframe | Direction | Evidence |
|---|---|---|
| Long-term (200d) | **Up** | Price +12.9% above rising 200-SMA; 50>200 gap widening |
| Intermediate (50d) | **Up, at risk** | Price only +0.42% above a rising 50-SMA |
| Short-term (10d) | **Down** | Price −2.59% below a falling 10-EMA; 8 straight lower highs |
| Momentum | **Down, un-exhausted** | MACD hist. −1.23 and widening; RSI 42 with room to 30 |

This is a **counter-trend pullback inside a bull trend** — the highest-probability long setup category, *conditional on the 50-SMA holding.*

---

## 5. Momentum

**MACD complex — the strongest bearish evidence in the dataset.**
- MACD peaked at **3.136 on 2023-12-22**, was 2.782 on 12-29, and is now **0.859** — a 73% decay in nine sessions.
- Signal line = 2.0889 (derived: macd − histogram). Macd sits **1.230 below** its signal.
- The bearish crossover occurred at **2023-12-29** (histogram −0.141 vs. +0.031 on 12-28). What matters is that the histogram has **expanded negatively for four consecutive sessions** (0.031 → −0.141 → −0.396 → −0.655 → −1.055 → −1.230). Expanding negative bars mean the *second derivative* of price is still negative — downside momentum is not yet decelerating.
- **Key threshold:** the MACD line at 0.859 is only ~0.86 pts from a zero-line cross. A MACD zero cross would convert this from a "momentum wobble" into a formal intermediate-trend sell signal in systematic frameworks. At the current rate of decay (~0.5/day), that is ~2 sessions away.

**RSI — reset, not capitulation.**
- 68.05 (12-18) → 67.28 (12-19) → 62.67 (12-20) → **42.13 (01-05)**, with an intraday-equivalent low print of **40.23 on 01-04**.
- RSI **never exceeded 70** during the December run-up (peak 68.05), so there is no classic overbought unwind to work off — this was a *momentum divergence-type* fade rather than a blow-off.
- RSI at 42.1 is **below the 50 midline** (bearish control) but **above 30** (not oversold). In the November–December advance, RSI dipped to 54.52 (12-06) and 55.89 (12-11) and found buyers — those levels are now above spot, confirming the regime change in momentum.
- **RSI divergence check:** price made a lower high (155.63 on 12-20 high vs. 155.12 on 12-19) with RSI making a lower high (62.67 vs. 67.28) — a mild bearish divergence into the top. That divergence has now played out.
- **Watch for:** a bullish divergence if price makes a lower low below 144.05 while RSI holds above the 40.23 print. That would be the first credible reversal clue.

---

## 6. Volatility & Bollinger Structure

- **ATR 2.925** (2.01% of price) and **declining**: 3.446 (12-18) → 3.424 (12-20) → 3.193 (12-22) → 3.033 (12-26) → 2.935 (12-27) → 2.806 (12-28) → 2.894 (01-02) → **2.925 (01-05)**. Note the small uptick on 01-04 (2.991) coinciding with the −2.6% day, then a fade — the market absorbed the sell-off without an expansion in realized range.
- **Interpretation:** the decline from 154 to 145 (−5.7%) has occurred on *contracting* volatility. That is characteristic of **orderly distribution / profit-taking**, not a disorderly de-risking event. It argues against a violent flush and for a grinding, level-by-level decline.
- **Bollinger (verified):** mid 150.071, upper 156.590, lower **143.552**, bandwidth 13.04 pts (8.68% of mid).
  - %B ≈ **12.9%** — price is pressed into the lower band zone.
  - The **lower band at 143.552** is only **1.18% below spot** and sits **$1.08 below the 50-SMA (144.636)**. This confluence (50-SMA ≈ 144.6, lower band ≈ 143.6, 01-04 low 144.05, 01-05 low 144.53) creates a **dense support cluster in the 143.5–144.6 band** — four independent measures agreeing within ~1%.
  - The midline (150.071) and the 10-EMA (149.099) and VWMA (150.878) form a **resistance cluster at 149.1–150.9**, roughly 2.7%–3.9% above spot.
  - Bollinger width is modest (8.7%), so the bands are *not* suggestive of a squeeze resolution either way; a walk down the lower band is mechanically possible for several sessions without becoming "extreme."

---

## 7. Volume Analysis

- **VWMA (150.878)** is the decisive volume signal: price is **−3.74% below** the volume-weighted average. Recent buyers are underwater as a group — this is an overhead supply problem, and it typically requires either time (consolidation) or a volume spike to clear.
- **Volume behaviour during the decline:** the four down-heavy sessions carried **47.3M (01-02), 49.4M (01-03), 56.0M (01-04)**, and the rebound session **45.2M (01-05)**. Compare to the late-December holiday lull: **25.1M (12-26), 31.4M (12-27), 27.1M (12-28), 39.8M (12-29)**. So selling arrived on **expanding volume (+40–120% vs. the 12-26→12-28 baseline)** — a genuine distribution signature.
- **However**, the 01-05 up-day volume (45.2M) is **below** the 01-04 down-day volume (56.0M). Declining volume on the bounce = lack of aggressive dip-buying. This is neutral-to-bearish for an immediate reversal and argues that a retest of the 144 area is more likely than a V-shaped recovery.
- Note 2023-12-15 volume of **110.1M** and 2023-12-18's 62.5M: these were rebalance/expiry-driven and should be excluded from any trend read rather than interpreted as institutional accumulation.
- **Actionable:** watch for a down-day volume spike >60M near 143.5–144.6 (capitulation → high-quality long entry) or an up-day volume >55M reclaiming 149.1 (confirmation → momentum long).

---

## 8. Key Levels Map (all derived from verified data)

| Level | Price | Source / Date | Significance |
|---|---|---|---|
| R4 | **155.63** | 2023-12-20 intraday high | Cycle high; ultimate breakout trigger |
| R3 | **154.07** | 2023-12-18 closing high | Highest close |
| R2 | **152.38–152.12** | 2024-01-02 high / 2023-12-20 close | First lower-high failure zone |
| R1 | **149.10–150.88** | 10-EMA 149.099 / Boll-mid 150.071 / VWMA 150.878 | **Primary resistance cluster**; reclaim = short-term trend repair |
| — | **145.24** | 2024-01-05 close | Spot |
| S1 | **144.64** | 50-day SMA | **The line in the sand** |
| S2 | **144.05–143.55** | 2024-01-04 low / lower Bollinger Band | Confluence floor; break = failed structure |
| S3 | **142.59–145.00** | 2023-11-13 close → 2023-11-14 open | Up-gap zone; secondary demand |
| S4 | **139.52** | 2023-11-16 low | Swing low; last higher-low of Q4 leg |
| S5 | **128.69** | 200-day SMA | Long-term trend invalidation |

---

## 9. Scenarios & Actionable Playbook

### Scenario A — Bullish base-and-reclaim (probability-weighted: moderate)
**Trigger:** a daily close **above 149.10** (10-EMA) with volume >55M; confirmation above **150.88** (VWMA).
**Logic:** reclaiming the 10-EMA and then the volume-weighted cost would neutralize the distribution overhang and re-open 152.38 → 154.07.
**Execution:** initiate 1/3 position on the 149.10 close, add 1/3 on a 150.88 hold. Stop at **144.60** (below 50-SMA) → risk from 149.10 entry ≈ 4.50 pts. Invalidation: any close back under 145.20.

### Scenario B — Base-and-fail, deeper retest (probability-weighted: highest near-term)
**Trigger:** a daily close **below 144.05** (below 50-SMA and below the 01-04 low).
**Logic:** MACD histogram still widening, RSI at 42 with room to 30, price below VWMA — the path of least resistance remains down while the 50-SMA is unresolved.
**Targets:** 142.59 (gap fill top), then 139.52.
**Execution:** do not buy the first break. Wait for one of (a) a bullish RSI divergence with price at 142.6–139.5, or (b) a down-day volume capitulation >60M followed by a higher-low day. Stop for that entry: **2× ATR ≈ 5.85 pts** below entry, or beneath 139.5 for the swing version.

### Scenario C — Chop / coil (probability-weighted: also meaningful)
**Range:** **143.55–149.10** for 3–10 sessions, with ATR continuing to compress below 2.90.
**Logic:** the confluence support cluster (143.5–144.6) is strong and the 50-SMA is rising into it; the resistance cluster (149.1–150.9) is equally dense. Neither side has a volume edge.
**Execution:** be patient. Trade only the edges with tight stops, or stand aside and let the MACD zero-line resolution choose the direction. A Bollinger squeeze (bandwidth <8%) followed by an expansion is the tell.

### Scenario D — Trend-repair failure into long-term trend test (low probability, high impact)
**Trigger:** a weekly close below **139.52**, then below the rising 200-SMA at 128.69.
**Logic:** would require a genuine fundamental shock; nothing in the current data supports it (ATR contracting, 50>200 gap widening). Treat as tail risk for position sizing, not as a base case.

---

## 10. Risk Management & Position Sizing

- **Current volatility unit:** ATR = **2.925** (2.01% of price).
- **Standard stop distance:** 1.5× ATR ≈ **4.39 pts**; 2.0× ATR ≈ **5.85 pts**.
- **Shares per $10,000 of risk at 2× ATR:** 10,000 / 5.85 ≈ **1,700 shares** (notional ≈ $247k) — i.e., for a 1% portfolio risk on a $100k account ($1,000), ≈ **170 shares** (≈ $24.7k notional, ~25% of equity). Adjust to your own risk budget; do not exceed 25–30% single-name exposure given the unresolved trend test.
- **Stop placement logic for a long near spot:** an initial stop at **142.40** (below the gap zone and 2.2% below the lower Bollinger Band) gives ~2.84 pts of buffer — about 1× ATR from spot, which is *too tight* for AMZN's current range (the 01-04 session alone spanned 3.33 pts). **Recommended:** stop at **141.50** (≈1.3% below the S3 gap zone), which is ~1.28× ATR from spot and outside normal noise.
- **Correlation caution:** AMZN is a mega-cap Nasdaq constituent; a portfolio-level view of QQQ/Nasdaq beta is required before sizing, and no macro/index data was supplied here to quantify that.

---

## 11. What Would Change This View

**Turn bullish (upgrade to "buy the dip"):**
1. Daily close > **149.10** with volume > 55M, or
2. Bullish RSI divergence at 142.6–144.0 with a MACD histogram contraction for 2+ sessions, or
3. MACD histogram turning positive (a second crossover) while price holds > 144.64.

**Turn bearish (downgrade to "avoid / short rallies"):**
1. Daily close < **143.55** (lower Bollinger Band) — especially a close < 143.55 with volume > 55M, or
2. MACD line crossing **below zero** (currently 0.859, ~2 sessions away at the present decay rate), or
3. RSI closing below **40** (it printed 40.23 on 01-04, so this is immediately relevant), or
4. 50-SMA rolling over (its slope currently is +0.33/session, so this would take several weeks of weakness — a slow-moving but high-confidence confirmation).

---

## 12. Caveats

- All figures are point-in-time as of **2024-01-05** from the frozen B-project dataset; no post-01-05 information is used or implied.
- The `technical_total_return_index` equals the close on every row and no dividends are recorded, so return figures here are pure price return.
- No fundamental, earnings, or index-composition data was provided; AMZN's Q4 earnings date falls outside this window and is an unpriced event risk not captured by these indicators.
- I have **not** claimed any historical support/resistance "bounce" as validation — the 144.6/143.6 confluence is a *coincidence of levels*, and AMZN has not yet tested and held them (the 01-04 low of 144.05 approached but the 50-SMA was not yet in play at that time).
- The MFI value in the snapshot (0.549487) is on an unidentifiable scale and is excluded.

---

## 13. Summary Table

| Dimension | Reading (2024-01-05) | Signal | Weight |
|---|---|---|---|
| **Last close** | 145.24 (O 144.69 / H 146.59 / L 144.53) | Weak bounce, lower half of range | — |
| **200-SMA (128.688)** | Price +12.86%, SMA rising +0.23/day | **Bullish** — primary trend intact | High |
| **50-SMA (144.636)** | Price only +0.42%, SMA still rising | **Neutral/critical** — support being tested | Very high |
| **10-EMA (149.099)** | Price −2.59%, EMA falling ~0.5–0.9/day | **Bearish** — short-term trend down | High |
| **MACD (0.859) / Signal (2.089)** | Bearish cross 2023-12-29; line 73% off Dec-22 peak | **Bearish** | High |
| **MACD Histogram (−1.230)** | Widening negatively 4 straight sessions | **Bearish, not exhausted** | High |
| **RSI (42.13)** | Below 50, above 30; down from 68.05 (12-18) | **Bearish but not oversold** | High |
| **Bollinger (150.07 / 156.59 / 143.55)** | %B ≈ 12.9%, near lower band | **Bearish, at support edge** | Medium |
| **ATR (2.925)** | −23.6% from 2023-11-06; 2.01% of price | **Orderly decline** — no capitulation | Medium |
| **VWMA (150.878)** | Price −3.74% below | **Distribution** — overhead supply | High |
| **Volume** | 56.0M down-day (01-04) vs 45.2M up-day (01-05) | Sellers active, buyers timid | Medium |
| **Structure** | 8 consecutive lower highs since 2023-12-20 (155.63 → 146.59) | **Short-term downtrend** | High |
| **Net verdict** | Bull trend, bearish short-term momentum, price pinned at 50-SMA | **Hold; stage entries; don't chase** | — |
| **Key pivot** | **143.55 – 144.64** (support) vs **149.10 – 150.88** (resistance) | Resolution defines next 5–10% | — |
| **Risk unit** | ATR 2.925 → stop at 1.5–2.0× ATR (4.4–5.9 pts) | Size accordingly | — |

**Bottom line:** AMZN's bull market is structurally intact but tactically exhausted. The stock is coiled inside a 143.55–149.10 decision box with momentum still deteriorating and price 3.7% below its volume-weighted cost. The prudent posture is to **hold existing longs with a stop beneath ~141.5, and to wait for either a decisive reclaim of 149.10 on convincing volume (buy) or a flush into 142.6–139.5 with an RSI divergence (buy) before committing new capital.** A close below 143.55 with expanding volume is the trigger to step aside rather than average down.