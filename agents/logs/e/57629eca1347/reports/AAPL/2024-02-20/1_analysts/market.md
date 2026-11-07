# AAPL — Technical Analysis Report (as of 2024-02-20)

## Data Integrity Note
All price, volume, and indicator figures below come from the frozen rows returned by `get_stock_data` (2023-08-01 → 2024-02-20, 140 rows) and the `get_verified_market_snapshot` for 2024-02-20. The two sources are **consistent** — every overlapping OHLCV row and every indicator value (close_50_sma 189.6462, rsi 35.2251, atr 3.1264, boll_lb 180.0380, vwma 185.6497) matches between the snapshot and the individual `get_indicators` pulls. No discrepancy to flag.

**Latest verified session (2024-02-20):** Open 181.79, High 182.43, Low 180.00, Close 181.56, Volume 53.67M.

---

## 1. Indicator Selection & Rationale (8 chosen)

| # | Indicator | Role in this specific context |
|---|---|---|
| 1 | **close_50_sma** (189.6462) | Medium-term trend spine; AAPL just lost it, so it defines the current bearish regime boundary. |
| 2 | **close_200_sma** (183.5509) | Strategic bull/bear line; price crossed below it on 2024-02-16 — the single most important structural event to monitor. |
| 3 | **close_10_ema** (184.9991) | Short-term momentum and the first "reclaim" hurdle on any bounce. |
| 4 | **macd** (−1.6256) | Trend/impulse confirmation; quantifies how fast momentum deteriorated from +0.95 on 1/26. |
| 5 | **rsi** (35.2251) | Timing tool for whether a tradable washout is near (30-line history in this uptrend). |
| 6 | **boll_lb** (180.0380) | Locates the immediate downside magnet / mean-reversion reference; complements the SMAs with a volatility-scaled level. |
| 7 | **atr** (3.1264) | Sets stop distance and position size — critical because AAPL is in a controlled pullback, not a crash. |
| 8 | **vwma** (185.6497) | Volume-weighted cost basis of recent buyers — the "overhead supply" gauge. |

*Deliberately excluded:* MACD signal/histogram (derivable from the snapshot, redundant), boll_ub/boll middle (the snapshot provides them for reference without needing separate calls), and I avoided stacking RSI with StochRSI or double-counting Bollinger bands.

---

## 2. Price Action & Structure — A Failed Breakout, Now Testing the Floor

**The sequence of swing highs is contracting:** 199.62 intraday (2023-12-14) → 196.38 (2024-01-24) → 191.05 (2024-02-07). That is a clean series of **lower highs**.

**The lows are the opposite — remarkably flat:** 180.17 (2024-01-05), 180.30 (2024-01-17), 179.25 (2024-02-02 intraday reversal low), and 180.00 (2024-02-20 low). This is a textbook **descending-triangle / converging wedge** with a well-defined 179.25–180.30 floor.

Current leg:
- Six consecutive lower closes: 187.15 (2/12) → 185.04 → 184.15 → 183.86 → 182.31 → **181.56 (2/20)**.
- From the 2024-01-23 closing high of 195.18 to 181.56 = **−6.98%**.
- From the 2024-02-09 close of 188.85 to 181.56 = **−3.86%** in six sessions.
- Today closed in the bottom third of a 2.43-point range, just 1.56 above the session low — no intraday bid of substance.

The 2024-02-02 session deserves attention: open 179.86, low 179.25, close 185.85 on **102.55M shares** (~2× normal). That was a high-volume flush that was aggressively bought — which is exactly why 179.25 matters as the last line of defense.

---

## 3. Moving-Average Framework — Short-Term Bearish Inside a Still-Intact Long-Term Uptrend

Verified distances from the 181.56 close:

| Reference | Value | Distance |
|---|---|---|
| 50-day SMA | 189.6462 | **−4.26%** |
| Bollinger middle (20 SMA) | 188.0390 | −3.45% |
| VWMA | 185.6497 | −2.20% |
| 10-day EMA | 184.9991 | −1.86% |
| 200-day SMA | 183.5509 | **−1.09%** |
| Bollinger lower band | 180.0380 | +0.85% (above it) |

**Two concrete, dated crossover events:**
- The close first fell **below the 50-SMA on 2024-01-30** (close 188.04 vs SMA 190.93) and has not reclaimed it since.
- The close first fell **below the 200-SMA on 2024-02-16** (close 182.31 vs SMA 183.48) — a *first* loss of the long-term line in the window I can verify. This is the most meaningful bearish development on the chart.

**The bull case is not dead, but it is being eaten away:**
- The 50-SMA is still above the 200-SMA (189.65 vs 183.55) — the golden-cross structure from 2023 remains intact.
- But the **spread is compressing**: 8.74 points on 2024-01-30 → 6.10 points today. The 50-SMA has rolled over (peak 190.9252 on 1/30, now 189.6462, falling ~0.12/day) while the 200-SMA still rises (~0.07/day). *Projection, not a forecast:* at that pace the gap closes in roughly 30+ sessions, putting death-cross risk in late March/April unless price stabilizes.
- The 10-EMA (185.00) remains **above** the 200-SMA (183.55) — the short-term average has not yet capitulated. But it is dropping ~0.77/day, so by arithmetic alone it is only ~2 sessions from crossing below the 200-SMA. Treat that as a watch item, not a confirmed signal.

**Stacked averages are now in bearish order** (10-EMA 185.00 < 50-SMA 189.65; price below both), which is the classic short-term down-trend alignment.

---

## 4. Momentum — Deteriorating, But Not Yet at January's Extreme

**MACD:** −1.6256 (line) vs −0.8922 (signal) → histogram −0.7334, i.e. the MACD line is *below* its signal and the gap is negative. Trajectory is the story:

- +0.9512 (2024-01-26 peak) → +0.0913 (1/31) → **crossed below zero on 2024-02-01** (−0.1376) → −0.3959 (2/2) → −0.2516 (2/9) → −0.6069 (2/13) → −1.0812 (2/15) → −1.3616 (2/16) → **−1.6256 (2/20)**.
- Momentum has now fallen for four straight sessions at an accelerating rate (−0.22, −0.26, −0.28, −0.26 per day).
- **Context:** the January low printed MACD at −1.9256 (2024-01-17). Today's −1.6256 is still slightly *better* than that trough — so MACD is testing, not yet breaking, its prior low. A MACD reading below −1.93 with price holding above 179 would create a **bullish divergence** (lower price low, higher momentum low). That is the highest-value signal to watch on the next 1–3 sessions.

**RSI:** 35.23 and falling from 50.81 on 2024-02-07. Not oversold (>30), so no mechanical washout signal yet. Important precedent inside this window: RSI bottomed at **28.79 on 2024-01-05** and 29.78 on 2024-01-04, and that coincided with the 180.17 low on 1/5 — i.e., in this uptrend the *tradable* low came only after RSI broke 30. Another ~5 points of downside in RSI is the typical prerequisite.

---

## 5. Volatility & Bollinger Positioning — Controlled Bleed, Not Panic

- **ATR = 3.1264, i.e. ~1.72% of the close.** That is *down* from 3.5864 on 2024-02-02 and 3.3406 on 1/18. Realized volatility is compressing even as price declines — consistent with orderly distribution rather than a disorderly break.
- **Bollinger (from verified snapshot):** lower 180.0380, middle 188.0390, upper 196.0400 → bandwidth ≈ 8.54% of the middle, a moderate, non-squeezed reading.
- The close (181.56) sits in the **lower quartile** of the bands, 1.52 above the lower band. The lower band has *turned down* (182.49 on 2/14 → 181.83 → 180.86 → **180.04**), so the downside envelope is now expanding *into* the 179–180 support shelf rather than defending it. That raises the odds that a break of 179.25 coincides with a band-walk lower.

---

## 6. Volume & VWMA — Supply Is Sitting Above the Market

- **VWMA = 185.6497**, versus a 181.56 close: the volume-weighted average price of recent participants is **2.20% above the market**, meaning the marginal buyer is underwater and every rally into the mid-180s meets sellers who are trying to get out at breakeven. VWMA peaked at 189.72 on 2024-02-07 and has rolled over every session since (189.72 → 189.19 → 188.79 → 188.07 → 187.33 → 186.68 → 186.18 → **185.65**).
- **Volume on the decline is rising, mildly:** last-5-session average ≈ 56.0M (2/13–2/20) versus the prior-5 average ≈ 45.0M (2/6–2/12), roughly +24%. Rising volume on falling price = distribution, but the absolute level (~50–65M) is well below the 102.55M of the 2024-02-02 flush, so there is **no capitulation signature** yet.
- Contrast: the two big-volume up-days (2024-01-18, 78.0M, +3.3% close-to-close; 2024-02-02, 102.6M) were *reversal/buying* days. The market has repeatedly found buyers on volume spikes — that is the bull's strongest evidence.

---

## 7. Actionable Scenarios

**Bias: tactically bearish / neutral, structurally bullish on a 6–12 month horizon.** This is a pullback testing the bottom of a five-week range, not a confirmed trend reversal — the 200-SMA is still rising and 50 > 200.

**Bearish trigger (primary):** a **daily close below 179.25** (the 2024-02-02 reversal low, confirmed against the 180.00 low of 2/20 and the 180.04 Bollinger lower band). That completes the descending triangle.
- Measured-move objective (triangle height = 191.05 − 179.25 = 11.80) projects to roughly **167–168** — a projection, not a verified level. Treat only the *trigger* as data-backed.
- Risk management: stop 1.5×ATR (≈4.69) above entry, or a close back above 183.55 (200-SMA) as an invalidation.
- Do **not** pre-position short into the 180 support; wait for the close below it, because the 2/2 and 1/5 and 1/17 lows all held in that zone.

**Bullish trigger (tactical reversal):** reclaim and close **above 183.55 (200-SMA)**, then confirmation above **185.00 (10-EMA) / 185.65 (VWMA)**. Stretch target = 188.04 (Bollinger middle), then the 189.65 50-SMA. A close above 186.50 would put price back inside the January 18–26 consolidation and neutralize the short-term downtrend.

**Mean-reversion setup (highest reward/risk):** price tags **179.25–180.04** with RSI ≤30 while MACD holds above the −1.9256 January trough. That combination = oversold + bullish momentum divergence at a triple-tested floor. Stop below 178.19 (the 2024-01-17 Bollinger lower band, the lowest band reading in the January base); target 184.99–185.65 (10-EMA/VWMA).

**What would falsify the bear case outright:** two consecutive closes above 186.50 with above-average volume (>70M), or MACD crossing back above its signal line while price holds 180.

---

## 8. Key Points Summary

| Category | Reading (2024-02-20) | Interpretation | Actionable Level |
|---|---|---|---|
| **Close / Range** | 181.56; O 181.79 / H 182.43 / L 180.00 | 6th straight lower close, weak close in range | Below 179.25 = breakdown |
| **50-SMA** | 189.6462 (−4.26%) | Medium-term trend lost; rolling over from 1/30 peak | Reclaim needed for bull turn |
| **200-SMA** | 183.5509 (−1.09%) | **First close below it on 2024-02-16** — key warning | 183.55 = bull/bear pivot |
| **10-EMA** | 184.9991 (−1.86%) | Short-term momentum down; ~2 sessions from 200-SMA cross | 185.00 = first reclaim hurdle |
| **Golden cross** | 50 > 200 (189.65 vs 183.55) | Still intact but spread shrank 8.74 → 6.10 since 1/30 | Death-cross risk late Mar/Apr (projection) |
| **MACD** | −1.6256 / signal −0.8922 / hist −0.7334 | Negative since 2024-02-01, accelerating down | Watch vs −1.9256 (1/17) for divergence |
| **RSI** | 35.2251 (from 50.81 on 2/7) | Falling but not oversold; 30 was the January buy zone | ≤30 + price at 180 = reversal setup |
| **Bollinger** | LB 180.038 / Mid 188.039 / UB 196.040 | Lower quartile; lower band turning down toward support | 180.04 alongside 179.25–180.30 floor |
| **ATR** | 3.1264 (1.72%) | Volatility *contracting* — orderly pullback, no panic | 1.5×ATR ≈ 4.69 stop buffer |
| **VWMA** | 185.6497 (−2.20% vs close) | Overhead supply; VWMA declining 8 straight sessions | 185.65 = supply wall |
| **Volume** | 53.67M (5-day avg ≈56M vs 45M prior) | Mild distribution; no capitulation vs 2/2's 102.55M | >70M on a rally = genuine demand |
| **Structure** | Lower highs 199.62 → 196.38 → 191.05; flat lows ~180 | Descending triangle into support | Resolution below 179.25 or above 186.50 |
| **Net bias** | Bearish short-term / bullish long-term | Pullback within an uptrend, testing the floor | Wait for the range to resolve |