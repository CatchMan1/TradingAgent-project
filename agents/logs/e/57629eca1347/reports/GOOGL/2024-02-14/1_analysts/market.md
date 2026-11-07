# GOOGL — Technical Analysis Report
**Analysis date (as-of): 2024-02-14 | Ticker: GOOGL (Alphabet Inc.)**

Data integrity note: `get_stock_data` (137 rows, 2023-08-01 → 2024-02-14) and `get_verified_market_snapshot` (2024-02-14) agree on the latest session and every indicator value cited below. The dataset shows `split = 1.0` and `dividend = 0.0` for all rows, so the total-return index equals the close; no adjustment distortions are present.

---

## 1. Price context for the latest session

| Field | 2024-02-14 |
|---|---|
| Open | 146.08 |
| High | 146.52 |
| Low | 144.09 |
| **Close** | **145.94** |
| Volume | 22.70M |
| Close vs. 2024-02-13 (145.14) | +0.55% |

The tape over the last three weeks is the whole story: GOOGL printed its highest close in the retrievable window at **153.51 on 2024-01-29** (high 153.78), then gapped from the 2024-01-30 close of **151.46** to a **140.10** close on 2024-01-31 (−7.50%) on **71.91M shares** — roughly 3× the ~25M share cadence of the preceding weeks. This is the signature of an event-driven repricing (the data shows the gap and volume, not the cause). A second high-volume flush took the price to an intraday **136.50** on 2024-02-02 (62.50M shares). From that low the stock staged a **+9.16% rebound to a 149.00 close on 2024-02-09**, then failed at 149.44 and slipped back to 145.14 (2024-02-13) before the modest 145.94 bounce on 2024-02-14.

Measured from the 2024-01-29 close to the 2024-02-02 close, GOOGL lost **7.25%**; measured close-to-low it lost **11.08%**. The subsequent recovery has retraced only about half of that damage. **The 2024-01-31 gap (151.46 → 143.62 open) remains unfilled.**

---

## 2. Trend structure — three timeframes, three different messages

**Long-term (close_200_sma = 131.07, rising):** Price sits **+11.35%** above the 200-day. The 200 SMA has climbed every session in the visible series (126.77 on 2024-01-16 → 131.07 on 2024-02-14), and the 50 SMA (141.01) sits **7.6% above** the 200 SMA. That is textbook bullish long-term alignment with no death-cross risk anywhere in sight. Nothing in the last three weeks has damaged the primary uptrend; the January high (153.51) was itself a new high in this dataset.

**Medium-term (close_50_sma = 141.01, rising):** The 50-day has advanced monotonically from 133.61 (2024-01-05) to 141.01 (2024-02-14), a gain of ~5.5% in roughly six weeks. Price is **+3.49%** above it. Critically, the 50 SMA (141.01) sits almost exactly on top of the 2024-01-31 close (140.10) and just below the 2024-02-02 close (142.38) — a genuine **confluence support shelf at ~140–142.4**.

**Short-term (close_10_ema = 145.99):** This is where the picture turns neutral-to-soft. Price closed **0.05 points (−0.03%) below the 10 EMA**, and the 10 EMA itself has rolled over: 146.19 (2024-02-12) → 146.00 (2024-02-13) → 145.99 (2024-02-14). The short-term mean has flattened and the price is now oscillating around it rather than trending away from it. Note also the wide **~4.98-point (3.5%) spread between the 10 EMA and the 50 SMA**, meaning the short-term price is still extended relative to its medium-term anchor and has room to mean-revert without breaking trend.

**Synthesis:** the trend hierarchy is bullish (200 SMA < 50 SMA < price), but the *immediate* impulse is a sideways consolidation inside the earnings gap. This is a "trend intact, momentum paused" configuration, not a reversal.

---

## 3. Momentum — the bearish crossover is still in force

- **MACD = 1.246 vs. Signal = 1.595 → Histogram = −0.349.**
- The bearish crossover fired between 2024-01-30 (histogram +0.824) and 2024-01-31 (−0.077), coinciding exactly with the gap-down session.
- The histogram then bottomed at **−0.892 on 2024-02-05** and repaired to **−0.239 on 2024-02-12** — giving the appearance of a turnaround — but has **deteriorated back to −0.349 on 2024-02-14** as the MACD line fell from 1.528 (Feb 12) to 1.246 (Feb 14).
- The MACD line (1.246) remains **above zero**, so this is a bullish-regime pullback in momentum, not a bearish regime. But **no bullish crossover has occurred**, and the failed histogram repair is a caution flag against front-running a re-acceleration.
- **RSI = 53.04** — dead center. For context: RSI hit **78.25 on 2024-01-29** (overbought at the high), collapsed to **43.62 on 2024-01-31**, and has since recovered to the low-50s. The oscillator has fully reset without reaching oversold. That reset is constructive for the medium term (overbought condition worked off) but provides no directional edge today. RSI at 53 offers no divergence signal I can substantiate from this data.

**Read:** momentum is genuinely neutral. The MACD histogram path (−0.24 → −0.35) says the buyers who stepped in on Feb 5–9 have not yet regained control of the tape.

---

## 4. Volatility and band positioning

- **Bollinger:** middle = **146.555**, upper = **153.958**, lower = **139.152**.
- Price at 145.94 sits **0.61 points (0.4%) below the middle band** and at roughly the **46th percentile** of the band range — i.e., slightly in the lower half of a wide envelope.
- **Bandwidth = 10.10% of the middle band**, contracting sharply from **13.58% on 2024-02-02** (upper 154.36 / lower 134.72 / mid 144.54). This is a post-event volatility compression, and it matters: compressing bands after a violent gap typically precede a directional resolution rather than a quiet drift.
- Note the upper band has been flat-to-lower for eight sessions (154.84 on Jan 30 → 153.96 on Feb 14) while the **lower band has risen steadily** (133.22 on Jan 30 → 139.15 on Feb 14). That is a coiling structure — the market is converging on a decision.
- **ATR = 3.07** (~2.1% of price). ATR peaked at **3.51 on 2024-02-02** (from 2.70 on 2024-01-30) and is decaying. Use 3.07 as the unit of risk: a 1-ATR stop is ~3 points, 2-ATR ~6.1 points. Stops tighter than ~3 points are inside normal noise in this regime.

---

## 5. Volume — the tell that the bounce is unpriced

- **VWMA = 145.21.** Price at 145.94 is only **0.73 points above** the volume-weighted mean. The VWMA has gone flat since 2024-02-01 (145.99 → 145.21) despite the stock swinging between 136.50 and 149.44. Translation: **the volume-weighted cost basis of recent holders is essentially at the current price.** The market is balanced; neither side has accumulated an edge.
- The 2024-02-14 up-day volume of **22.70M** is roughly **28% below** the ~31.7M average of the prior ten sessions — a low-conviction bounce.
- By contrast, the 2024-02-09 push to 149.00 came on **26.83M** (above average), and the 2024-02-13 decline came on **27.84M**. Distribution volume has been at least matching accumulation volume since the gap. Until an up-day prints **>30M**, treat rallies as repair, not re-accumulation.

---

## 6. Actionable framework

**Bias: constructive on the medium term, neutral-to-cautious tactically. Do not chase; let the range resolve.**

**Bullish trigger / add-on zone:**
- A **daily close above 149.44** (2024-02-09 high) with volume >30M reopens the path to the **151.46** gap origin and then **153.05–153.78** (2024-01-25/01-29 highs). That would be the first objective evidence that the gap-down is being rejected.
- A **MACD bullish crossover** (line above 1.595 signal) alongside a reclaim of the 146.56 Bollinger middle would confirm; the two should be required together, given the whipsaw in the histogram between Feb 5–14.
- Stop discipline: place risk below **143.69** (2024-02-13 low) — roughly 1.9 × ATR from 149.44 — or below 143.62, the gap's origin open.

**Bearish trigger:**
- A **close below 143.69** puts the **141.01 50-day SMA / 140.10 (Jan 31 close) / 142.38 (Feb 2 close)** confluence shelf in play. Because three independent references cluster within ~2.7 points, this is the line that matters.
- A decisive break of 139.15 (lower band) plus a loss of the 50 SMA would invalidate the post-earnings recovery thesis and expose **136.50** (2024-02-02 low). A close under that low would mark a lower low and shift the medium-term read to distribution.

**Range view (most probable near term):** 143.69 – 149.44 with a 145.2–146.0 pivot (VWMA/10 EMA cluster). The stock has spent eight sessions inside this envelope; the falling ATR and contracting bands suggest the resolution is weeks, not months, away.

**Risk management:**
- Size off ATR 3.07, not off a fixed percentage. A 1-ATR stop on a 145.94 entry is 142.87 — which usefully sits just under the 50 SMA confluence.
- RSI at 53 and MACD negative mean there is no momentum tailwind; reduce position size versus what you would carry when price is above the 10 EMA with a positive histogram.
- Avoid treating the 2024-02-09 high (149.44) as confirmed resistance or the 2024-02-02 low (136.50) as confirmed support — both are single-print extremes from a two-week window, not tested levels.

---

## 7. Indicator selection rationale (8 primary)

| # | Indicator | Value (2024-02-14) | What it uniquely tells us | Why it is in the set |
|---|---|---|---|---|
| 1 | close_10_ema | 145.99 | Price is 0.03% below a flattening short mean | Timeliest read on whether the bounce has legs; catches momentum shifts the SMAs miss |
| 2 | close_50_sma | 141.01 | Rising medium anchor, +3.49% below price | Defines the trend-break line and doubles as confluence support with 140.10/142.38 |
| 3 | close_200_sma | 131.07 | +11.35% below price, rising, 50>200 by 7.6% | Confirms the primary uptrend is undamaged — prevents over-reacting to a 2-week drawdown |
| 4 | macd | 1.246 (signal 1.595, hist −0.349) | Bearish crossover still open; hist re-weakened (−0.24 → −0.35) | Best available measure of intermediate momentum regime; only 2 of the set's signals are momentum |
| 5 | rsi | 53.04 | Full reset from 78.25 (Jan 29) to 43.62 (Jan 31), now neutral | Confirms the overbought excess has been worked off without an oversold extreme — non-redundant with MACD (levels vs. rate of change) |
| 6 | boll_ub | 153.958 | Upper band flat while lower band rises → coiling | Defines the upside objective and quantifies the post-gap squeeze (bandwidth 13.58% → 10.10%) |
| 7 | atr | 3.07 | ~2.1% of price; peaked 3.51 on Feb 2, now decaying | Required for stop placement and position sizing in an event-driven tape |
| 8 | vwma | 145.21 | Price only +0.73 above volume-weighted cost | Distinguishes volume-backed price from drift — this is what exposed the low-conviction 22.7M bounce |

*Supporting sub-components read but not counted separately: `boll` middle (146.555), `boll_lb` (139.152), `macds` (1.595) — these belong to the MACD and Bollinger constructs already selected and add no independent information.*

---

## 8. Key levels and signals summary

| Item | Level / Reading | Interpretation | Action |
|---|---|---|---|
| Close 2024-02-14 | 145.94 | Inside the Jan 31 earnings gap | Neutral; no position edge at spot |
| 10 EMA | 145.99 | Price marginally below; EMA flattening | Short-term momentum not confirmed |
| VWMA | 145.21 | Price +0.73 above; VWMA flat since Feb 1 | Market is balanced — no conviction either way |
| Bollinger middle | 146.555 | Price 0.61 below | Reclaim = first sign of buyer control |
| Immediate resistance | 149.00–149.44 (Feb 9) | Rally failed here | Close above on >30M volume = long trigger |
| Gap fill / next resistance | 151.46 / 153.05–153.78 | Unfilled Jan 31 gap | Objective if 149.44 breaks |
| Immediate support | 143.62–143.69 | Gap origin open / Feb 13 low | Close below = bearish trigger |
| Confluence support | 140.10–142.38 with 50 SMA 141.01 | Three independent references cluster | Trend-invalidation zone |
| Lower band / event low | 139.152 / 136.50 | Break = lower low, distribution | Exit / reverse bias |
| RSI | 53.04 | Neutral, reset from 78.25 | No edge; do not fade or chase on RSI alone |
| MACD | 1.246 vs 1.595 signal, hist −0.349 | Bearish crossover open, hist re-widening negative | Wait for positive crossover before adding |
| ATR | 3.07 | ~2.1% daily range, decaying from 3.51 | 1-ATR stop ≈ 3 pts; size accordingly |
| Bollinger bandwidth | 10.10% (from 13.58% on Feb 2) | Compressing after event shock | Expect directional resolution within weeks |
| Volume | 22.70M vs ~31.7M 10-day avg (−28%) | Feb 14 bounce is low-conviction | Require >30M on up-days to confirm |
| Trend regime | 200 SMA 131.07 < 50 SMA 141.01 < price 145.94 | Bullish hierarchy intact | Stay long-biased structurally; trade the range tactically |

**Bottom line for GOOGL:** The primary uptrend is intact and the January overbought condition has been fully digested, but the 2024-01-31 gap-down has left a momentum scar — MACD is still bearish-crossed, price is pinned at the 10 EMA/VWMA cluster, and the latest bounce came on 28% below-average volume. Treat 143.69 and 149.44 as the decision rails: a volume-backed close above 149.44 with a MACD crossover reopens the gap fill toward 151.46–153.78, while a close below 143.69 concentrates risk into the 141–140 confluence and, if that fails, 136.50. Until one of those resolves, GOOGL is a range trade with ATR-based risk, not a momentum trade.