## AAPL — Multi-Factor Technical Report (as of 2026-07-28)

### 1. Data integrity check
Both tool sets agree exactly on the latest session, so there is **no discrepancy to flag**:

| Field | Verified snapshot (2026-07-28) | get_stock_data row |
|---|---|---|
| Open / High / Low / Close | 340.03 / 342.89 / 335.60 / **340.08** | identical |
| Volume | 51,859,000 | 51,859,000 |
| RSI(14) | 68.897 | 68.897 |
| MACD / Signal / Hist | 9.454 / 8.144 / 1.310 | 9.454 / 8.144 / 1.310 |

Close of 340.08 is the **highest close in the entire visible history** (Dec 1, 2025 → Jul 28, 2026), and the intraday high of 342.89 is also a window high. The prior window closing high was 288.62 on 2026-05-08's neighborhood — precisely, 288.62 high on 2025-12-03 and a 315.20 close on 2026-06-02 — so July is unambiguously blue-sky territory for this dataset.

---

### 2. Selected indicators (8) and why they fit this context

| # | Indicator | Latest value | Role in this setup |
|---|---|---|---|
| 1 | close_10_ema | 329.21 | Short-term trend/entry timing in a fast, high-beta advance |
| 2 | close_50_sma | 307.83 | Medium-term trend spine & pullback support |
| 3 | close_200_sma | 276.79 | Strategic bull/bear arbiter (price +22.9% above) |
| 4 | macd | 9.454 | Trend-change/crossover engine; at window high |
| 5 | macdh | 1.310 | Second derivative of momentum — catches re-acceleration vs exhaustion |
| 6 | rsi | 68.90 | Overbought/extension gauge + divergence detector |
| 7 | vwma | 326.48 | Only volume-weighted confirmation of the rally's legitimacy |
| 8 | atr | 8.08 | Volatility-scaled stops and position sizing |

Deliberately excluded as redundant: `macds` (fully implied by macd vs macdh), `boll` middle (a 20-SMA that duplicates the 10-EMA/50-SMA read; bands cited below only as supplementary verified context), `boll_lb` (irrelevant at 16% below price).

---

### 3. Trend structure: textbook bullish stack, unusually extended

The moving-average ordering is perfectly stacked and **all four slopes are positive**:

**Price 340.08 > 10 EMA 329.21 > VWMA 326.48 > 50 SMA 307.83 > 200 SMA 276.79**

- Price vs 10 EMA: **+3.3%**
- Price vs 50 SMA: **+10.5%**
- Price vs 200 SMA: **+22.9%**
- 50 SMA vs 200 SMA: **+11.2%** (a firmly established golden-cross regime; the 50-day has climbed every session since at least 2026-06-18, from 288.74 → 307.83, roughly +0.71/day)

The low structure confirms the trend is genuine, not a single spike: **245.51 (2026-03-30) → 245.70 (2026-04-07) → 273.75 (2026-06-25) → 319.35 (2026-07-23)** — a sequence of sharply rising higher lows. From the 2026-03-30 close of 246.63 to today's 340.08 the instrument has gained **+37.9%**; from the 2026-06-24 close of 293.08 it is **+16.0%** in about 24 sessions.

**Nuance:** the 10-EMA is 6.9% above the 50-SMA. That kind of spread is characteristic of a momentum thrust, not a sustainable grind — it is the single biggest argument for scaling in on weakness rather than chasing strength.

---

### 4. Momentum: re-acceleration after a clean reset (the key bullish tell)

RSI path is the most instructive sequence in the data:
- **2026-07-16: 71.43, 2026-07-17: 71.65** — first genuine overbought print of the advance, coincident with the 7/17 high of 334.99.
- Price then corrected sideways-to-down to 321.66 (2026-07-23) while RSI cooled all the way to **58.11** — an ~13.5-point reset.
- **2026-07-28: 68.90**, i.e., RSI has recovered nearly back to 70 *with price at a new all-time high for the window.*

That is the classic "overbought reset without price breakdown" pattern — momentum was vented through time/small correction rather than through distribution. The absence of a lower RSI high against a higher price high means **no bearish divergence is currently present**. The caution is that 68.90 leaves very little headroom before a second overbought condition, and 71.65 is the level a further push must beat.

MACD confirms rather than contradicts:
- MACD line: **-2.916 (2026-06-29, the washout low) → +9.454 (2026-07-28)**, a monotonic climb with the line printing a fresh window high today.
- Histogram: peaked at **3.337 (2026-07-17)**, contracted to **0.795 (2026-07-23)**, and has now re-expanded for three straight sessions: **0.908 → 1.111 → 1.310**.
- Crucially, the MACD line made a **higher high (9.454) alongside price's higher high** — momentum is leading, not lagging.

**The offsetting risk:** a MACD line at 9.45 is the most stretched reading in the dataset, and the histogram at 1.31 is still only ~39% of its 7/17 peak. A histogram roll-over from this altitude would be a faster warning than a slow bleed, because the signal line is chasing from far below.

---

### 5. Volume/participation: the one genuine soft spot

- **VWMA 326.48** sits 4.2% *below* price and *above* the 50-SMA (307.83). Because volume-weighted average price leads the simple average, buyers have been transacting at progressively higher prices — the advance is **volume-backed in aggregate, not hollow**. VWMA has risen every session since 6/30 (288.84 → 326.48).
- The June washout is the other important volume fact: **2026-06-25 closed -6.1% (293.08 → 275.15) on 107.0M shares, then 2026-06-26 reversed to 283.78 on 261.8M shares** (the largest volume in the dataset by a wide margin). Price never revisited 274. That is a high-volume capitulation-and-absorption signature, and the rally originates from it.
- **However**, current participation is thinning. 5-session average volume (7/22–7/28) ≈ **45.7M** versus the 20-session average ≈ **50.0M** — the breakout to new highs on 7/24 and 7/27–7/28 is occurring on *below-average* volume. That is a divergence worth respecting: price breakout quality is medium, not high.

The 2026-07-28 candle itself is constructive but not emphatic: it closed at 61.5% of its range ((340.08−335.60)/(342.89−335.60)), leaving a modest upper wick after tagging 342.89.

---

### 6. Volatility and band position

- **ATR 8.08 = 2.38% of price.** ATR bottomed near 7.00 on 2026-06-24, spiked to 8.74 on 2026-07-02, and has settled in the 7.9–8.3 zone for three weeks — volatility is elevated but *stable*, which is favorable for trend-following (no whipsaw expansion).
- **Bollinger (supplementary, from verified snapshot):** middle 319.96, upper 346.71, lower 293.21. Close is above the middle, **1.95% below the upper band**; %B = **0.876**; bandwidth = **16.7%** (very wide).
- Note the lower band has rocketed from 275.95 (6/30) to 293.21 — the mean is being dragged up hard, a signature of a strong up-trend rather than a squeeze setup.

Interpretation: price is in the upper third of an expanding band, **not riding the upper band** (%B 0.88, not >1.0). That argues the move has room to tag 346.71 without being statistically extreme, but it is no longer a low-risk entry.

---

### 7. Actionable levels and playbook

**Reference levels (all tool-derived):**

| Level | Price | Source |
|---|---|---|
| Intraday window high | **342.89** | 2026-07-28 high |
| Bollinger upper band | **346.71** | verified snapshot |
| +1 ATR projection | 348.16 | ATR arithmetic (not a forecast) |
| 10 EMA | **329.21** | indicator |
| VWMA | **326.48** | indicator |
| 7/22–7/23 congestion / swing low | 321.62 – 323.34 low 319.35 | OHLCV |
| 50 SMA | **307.83** | indicator |
| 1× / 2× / 3× ATR below close | 332.00 / 323.92 / 315.84 | ATR arithmetic |

**Scenario A — Continuation (base case, ~55% weight):** A decisive *close* above **342.89** on volume expanding back above ~50M keeps the trend intact and opens the 346.71 upper band. Because the risk/reward of buying 340.08 with a structurally sound stop under 319.35 is only about 0.3:1, **do not initiate full size at market here.** If adding, size at ⅓–½ and place the stop under **334.00** (below the 2026-07-17 high of 334.99, now potential support) — ~1.8% risk, ≈0.75 ATR.

**Scenario B — Preferred entry on weakness:** Let price come to the **329–332** zone (10 EMA 329.21 ≈ 1 ATR below close). Stop under **319.35** (7/23 swing low). That yields roughly 3.2% risk against 4.7% to the upper band — approximately **1.5:1**, materially better than the current price. A tag of **321–326** (2× ATR / VWMA region) would be an even higher-conviction add as long as the 50-SMA at 307.83 is not breached.

**Scenario C — Trend damage (invalidation ladder):**
1. Close back **below 329.21** (10 EMA) → momentum trade invalidated, momentum-longs should reduce.
2. Close **below 319.35** → higher-low structure on the daily chart is broken; the move shifts to a range/mean-reversion regime.
3. Close **below 307.83** (50 SMA) → medium-term trend broken; the 200-SMA at 276.79 becomes the strategic reference.

**Position sizing:** with ATR at 2.38% of price, a 1-ATR stop is tight for this name. Size positions so that (entry − stop) × shares ≈ your fixed risk budget using the ATR-derived stop distance (8.08), not a fixed percentage.

---

### 8. What would flip the bias
- **Bearish:** MACD histogram rolling over for 2+ consecutive sessions from the 1.31 level; RSI stalling below 71.65 on a price high (a genuine double divergence); VWMA-to-price gap compressing via price falling rather than VWMA rising; volume continuing to shrink on each new high.
- **Bullish confirmation:** a high-volume close above 342.89 that also lifts RSI above 71.65 (proving the 7/17 print was not the cycle high); VWMA catching up toward 334+ (currently 326.48), which would close the 4.2% "price ahead of volume" gap.

---

### 9. Summary table

| Dimension | Reading | Evidence (2026-07-28 unless noted) | Bias / Action |
|---|---|---|---|
| Primary trend | Strong uptrend, new window high | Close 340.08 > 10EMA 329.21 > VWMA 326.48 > 50SMA 307.83 > 200SMA 276.79 | **Bullish** |
| Long-term regime | Golden cross, widening | 50SMA 307.83 vs 200SMA 276.79 (+11.2%), both rising | Bullish, strategic |
| Medium-term | Persistent higher lows | 245.51 (3/30) → 273.75 (6/25) → 319.35 (7/23) | Bullish |
| Extension vs trend | Stretched | +10.5% above 50SMA, +22.9% above 200SMA, 10EMA–50SMA gap 6.9% | Don't chase full size |
| RSI(14) | 68.90, reset then re-advanced | 71.65 peak (7/17) → 58.11 (7/23) → 68.90 now | Bullish, limited headroom |
| MACD | 9.454 (window high) vs signal 8.144 | Rose from -2.916 (6/29); higher high with price | Bullish |
| MACD histogram | 1.310, re-expanding 3 sessions | 3.337 (7/17) → 0.795 (7/23) → 0.908 → 1.111 → 1.310 | Bullish re-acceleration |
| Volume quality | Aggregate OK, recent soft | VWMA 326.48 (price +4.2% above); 5d avg 45.7M < 20d avg 50.0M | Neutral/caution |
| Washout evidence | High-volume absorption | 6/25 -6.1% on 107.0M; 6/26 +3.1% on 261.8M | Supports rally base |
| Volatility | Elevated but stable | ATR 8.08 (2.38% of price); 7.9–8.3 for three weeks | Use ATR stops |
| Band position | Upper zone, not extreme | %B 0.876; UB 346.71, middle 319.96, LB 293.21; bandwidth 16.7% | Room to 346.71 |
| Near support | 329.21 / 326.48 / 319.35 | 10EMA / VWMA / 7-23 low | Primary add zone 329–332 |
| Key resistance | 342.89 → 346.71 | 7/28 high / upper band | Breakout trigger |
| Preferred action | Hold core longs; buy dips, don't chase | R/R at market ≈0.3:1; at 329–332 ≈1.5:1 | Scale in 329–332 |
| Invalidation | 319.35 then 307.83 | Swing low / 50SMA | Cut momentum longs below 10EMA |

**Bottom line for AAPL:** the trend, momentum, and volume-weighted structure all point the same way — up — and there is no confirmed divergence in RSI or MACD. The problem is *price*, not *trend*: at 340.08 the instrument sits 3.3% above its 10-EMA, 10.5% above its 50-SMA, with a MACD line at the top of its 8-month range and volume thinning on new highs. Treat this as a **hold-and-add-on-pullback** setup (accumulation zone 329–332, invalidation 319.35), not a breakout-chase, and let the ATR of 8.08 define both stop distance and position size.