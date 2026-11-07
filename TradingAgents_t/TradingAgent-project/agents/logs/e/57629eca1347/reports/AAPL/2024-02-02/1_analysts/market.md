# AAPL — Multi-Timeframe Technical Assessment (as of 2024-02-02 close)

**Data integrity note:** The verified snapshot and the raw OHLCV CSV agree exactly on the 2024-02-02 row (O 179.86 / H 187.33 / L 179.25 / C 185.85 / V 102,551,700) and on all indicator values quoted below. No discrepancy was found between tools, so all figures below are internally consistent.

---

## 1. The setup in one paragraph

AAPL is caught between two opposing structures. The **long-term trend is still up** (price 185.85 sits ~1.8% above a rising 200-day SMA at 182.49, and the 50-day SMA at 190.65 remains 8.16 points above it — a healthy bullish alignment). But the **medium-term trend is down**: since the 2023-12-14 high of 199.62, AAPL has printed a sequence of lower highs (199.62 → 196.38 on 2024-01-24 → 187.33 on 2024-02-02) and, on 2024-02-02, a marginal lower low at 179.25. Momentum has rolled over (MACD crossed below its signal on 2024-01-31 and below zero on 2024-02-01), price is below the 10 EMA (188.53), the 20-day Bollinger mid (188.16) **and** the VWMA (188.83). Yet the 2024-02-02 session itself was strikingly constructive: a ~3.75% gap-down open (179.86 vs. 186.86) that made a low of 179.25 — undercutting both the 2024-01-05 low (180.17) and the 2024-01-17 low (180.30) and piercing the lower Bollinger Band (179.54) — before closing at 185.85, i.e. **81.7% of the day's range**, on **102.6M shares (~1.8× the ~57M 20-day average)**. That is a textbook failed-breakdown / washout-and-reclaim bar, but it has *not* yet been confirmed by any close above the 186.9–188.8 resistance cluster.

---

## 2. Indicator selection and rationale

I selected **eight** indicators to cover five non-overlapping information channels:

| # | Indicator | Latest value (2024-02-02) | Why it earns a slot |
|---|---|---|---|
| 1 | **close_200_sma** | 182.4919 | The strategic regime line and the floor of the January range; rising ~0.10/day. Defines where the multi-year bull case breaks. |
| 2 | **close_50_sma** | 190.6504 | Medium-term trend + the top of the current consolidation. Slope has just turned flat (peaked 190.9252 on 2024-01-30), which is the key "regime friction" observation. |
| 3 | **macd** | −0.3959 (signal 0.0490) | Captures the momentum regime shift with dates: bearish crossover 2024-01-31, zero-line break 2024-02-01. |
| 4 | **rsi** | 43.34 | Independent momentum oscillator to test whether the selloff is exhausted (it is *not* oversold) and to detect divergence at the 195 retest. |
| 5 | **boll_ub** | 196.7759 | Defines the top of the squeeze and the breakout trigger zone; falling from 202.95 on 2024-01-08. |
| 6 | **boll_lb** | 179.5361 | The 2024-02-02 intraday undercut-and-reclaim of this line is the single most actionable volatility event on the chart. |
| 7 | **atr** | 3.5864 (1.93% of price) | Jumped +10.7% day-over-day, the highest reading in the 60-day window; mandatory for stop placement and sizing in a two-way tape. |
| 8 | **vwma** | 188.8268 | Adds the volume dimension the price averages lack; price *below* VWMA means the recent volume-weighted buyer is underwater (distribution). |

*Deliberately excluded:* `close_10_ema` (188.53) and `boll` middle (188.156) are effectively redundant with the resistance cluster already covered by the 50-SMA/VWMA discussion — but they are the two other rungs of the same 186.9–188.8 wall, so I reference them as context. `macds`/`macdh` and `stochrsi` would duplicate the MACD-line and RSI information already selected.

---

## 3. Trend analysis — a bull market in a corrective phase

**Long-term (bullish, intact).** The 200-day SMA has risen monotonically through the entire window: 175.45 on 2023-12-04 → 182.49 on 2024-02-02 (+4.0%), and its daily increment has actually *accelerated* slightly into the print (+0.097 on the last session). The 50-day SMA (190.65) is 4.5% above it. No death-cross risk is remotely close — the 50-SMA would have to fall roughly 8+ points to meet the rising 200-SMA. Structurally, the primary trend is not in question.

**Medium-term (bearish/rolling over).** Two details matter:
- The 50-day SMA **stopped rising** after peaking at 190.9252 on 2024-01-30 and has printed three consecutive declines (190.8190 → 190.7624 → 190.6504). That is a fresh slope inflection, not a long-standing condition.
- Price has closed below the 50-SMA for four straight sessions: 184.40 (2024-01-31), 186.86 (2024-02-01), 185.85 (2024-02-02) — the longest such run since the January gap-down.

**Short-term (bearish, but decelerating).** The 10 EMA peaked at 191.4059 on 2024-01-29 and has fallen to 188.53, with price below it. Critically, the short-term average stack is now **inverted relative to price**: close 185.85 < 10 EMA 188.53 ≈ Bollinger mid 188.156 < VWMA 188.83 < 50-SMA 190.65. The one thing not inverted is the 200-SMA at 182.49.

**Structure:** AAPL is in a broad **178–199 box** carved out since late December. Inside that box, the sequence since 2023-12-14 is lower highs with only marginally lower lows — an overlapping, low-conviction bleed rather than an impulse decline. The 2024-02-02 low of 179.25 vs. the 2024-01-17 low of 180.30 is a **lower low by only 1.05 points**, which is exactly the kind of marginal break that a high-volume reversal bar can invalidate.

---

## 4. Momentum — the weight of evidence is negative, but small in magnitude

**MACD (dated path, all tool-derived):**
- Peak momentum thrust: `macd` reached **+0.9512 on 2024-01-26** and `macdh` peaked at **+1.1282 on 2024-01-25**.
- **Bearish crossover:** `macd` 0.0913 fell below `macds` 0.2346 on **2024-01-31** (histogram flipped to −0.1434).
- **Zero-line break:** `macd` went negative on **2024-02-01** (−0.1376) and is now −0.3959, with `macds` at 0.0490.
- Histogram has expanded negative three sessions running: −0.1434 → −0.2978 → −0.4449. That is accelerating downside momentum — **but** the magnitude is only ~22% of the January trough (−2.0447 on 2024-01-05). In other words, this is a *shallow* rollover by the standards of the last two months.

**Divergence evidence (the important nuance):** The January rally retested the December price zone with materially weaker internals:
- 2023-12-08 close 195.71 → RSI 70.02. 2024-01-23 close 195.18 → RSI 62.62. **Same price, ~7.4 RSI points lower.**
- 2023-12-15 MACD +3.7507 vs. 2024-01-26 MACD +0.9512. **Same price zone, ~2.8 points lower momentum peak.**

Both are classic momentum divergences at a lower high — the 2024-02-02 breakdown is the *consequence* of that fading impulse, not a fresh shock.

**RSI at 43.34** is neutral-to-weak. It bottomed at 28.79 on 2024-01-05 (the only genuine oversold reading in the window), recovered to 62.62 by 2024-01-23, and has now slid back. Two things it tells us: (a) the recent overbought condition has been fully relieved, but (b) **no oversold spring is loaded** — there is room to fall to 180 without any RSI support. The 2024-02-02 bounce lifted RSI only to 45.07 (on 2024-02-01) before fading to 43.34, meaning the reversal bar did *not* translate into momentum improvement.

---

## 5. Volatility and Bollinger structure — a squeeze sitting on top of a floor

| Bollinger metric | 2024-01-08 | 2024-01-24 | 2024-02-02 |
|---|---|---|---|
| Upper band | 202.952 | 197.622 | 196.776 |
| Middle (20 SMA) | 192.202 | 188.188 | 188.156 |
| Lower band | 181.451 | 178.754 | 179.536 |
| Bandwidth % of mid | 11.19% | 10.02% | 9.16% |

Bandwidth has compressed for four consecutive weeks — a **volatility squeeze** (upper band falling 6.2 points while the lower band has *risen* 0.8 points from its 2024-01-17 low of 178.194). Squeezes resolve directionally, and the resolution is not yet determined; the neutral band position of the close (2.3 points above the lower band, 10.9 below the upper) is consistent with indecision, not with a trend break.

**The 2024-02-02 bar is the key micro-event:** the low of 179.25 traded **0.29 below** the lower band (179.536) and **0.92 below** the 2024-01-05 low (180.17), then closed 6.31 above the band. Undercutting a band and immediately reclaiming it is one of the highest-quality short-term washout signals available — but it is a *short-term* signal, and it is worthless without a follow-through close above the resistance cluster.

**ATR = 3.5864 (1.93% of price)** is the highest reading in 60 days, up from 3.2407 (+10.7%) in a single session, and the 2024-02-02 true range of 8.08 points was ~2.5× the prior ATR. Practical consequences:
- 1× ATR below the close = **182.26**, which sits almost exactly on the 200-SMA (182.49) — a useful confluence stop.
- 2× ATR below = **178.68**, i.e. below the 2024-02-02 low and below the whole January floor: that is the "thesis is wrong" stop.
- Position sizing must be cut: at 1.93% daily ATR versus 1.58% on 2024-01-30 (3.2153), identical dollar risk requires ~18% fewer shares.

---

## 6. Volume — the confirmation the price action lacks

- **2024-02-02 volume 102,551,700** is the heaviest session since 2023-12-15 (128.5M, an options-expiry date) and ~1.8× the ~57M average of the last 20 sessions. Combined with the reversal close, this reads as **absorption/capitulation buying into weakness** rather than continued liquidation.
- Against that, the **VWMA (188.83)** is above price for the first time since 2024-01-16–17: the volume-weighted average buyer over the recent window is underwater by ~3.0 points. VWMA peaked at 189.395 on 2024-01-30 and has rolled over, confirming that the 2024-01-18→01-26 advance was distributed into, not accumulated.
- Contrast the two heavy-volume down days: 2024-01-02 (82.5M, close 185.64 from 192.53 — pure gap-and-go distribution) versus 2024-02-02 (102.6M, close 185.85 from a 179.25 low — buying response). Same price destination, opposite mechanics. The most recent evidence favors the bulls' argument at the margin.

---

## 7. The 2024-02-02 candle, read carefully

| Attribute | Value |
|---|---|
| Gap vs. 2024-02-01 close | 179.86 − 186.86 = **−7.00 (−3.75%)** |
| Range | 187.33 − 179.25 = **8.08 pts (4.35% of close)** |
| Close location in range | **81.7%** (upper quintile) |
| Body | +5.99 from open (bullish) |
| Close vs. 200-SMA | +3.36 above (182.49) |
| Close vs. prior day's low (183.82) | Above — gap filled and reclaimed |
| Close vs. 10 EMA / VWMA | **Below both** |

Interpretation: the session repaired the intraday damage but **did not restore the trend**. A gap that opens below support, fills, and closes green is a bullish *attempt*; it becomes a bullish *signal* only when the prior day's close (186.86) and then the 188.16/188.53/188.83 cluster are reclaimed. Until then, treat 2024-02-02 as a successful defense of the 200-SMA rather than a reversal.

---

## 8. Level map (all levels derived from tool output)

**Resistance (overhead):**

| Level | Source | Significance |
|---|---|---|
| 186.86 | 2024-02-01 close | First hurdle to confirm the reversal bar |
| 187.33 | 2024-02-02 high | Intraday supply from the gap-down session |
| 188.16 / 188.53 / 188.83 | Boll mid / 10 EMA / VWMA | **Confluence wall — the decisive gate.** A close above this triple is the highest-value signal on the board |
| 190.65 | 50-SMA | Medium-term regime restoration |
| 191.73–191.95 | 2024-01-29 close / 2024-01-19 high | Prior swing shelf |
| 195.18–196.38 | 2024-01-23 close / 2024-01-24 high | January rejection zone |
| 196.78 | Bollinger upper | Squeeze-top breakout trigger |
| 199.62 | 2023-12-14 high | 52-week high in the dataset (close 185.85 is 6.9% below) |

**Support (underneath):**

| Level | Source | Significance |
|---|---|---|
| 183.82–184.35 | 2024-02-01 low / 2024-01-31 low | Immediate shelf |
| 182.49 | 200-SMA | **Primary thesis line**, ~1.8% below close |
| 182.26 | Close − 1×ATR | Confluence stop with the 200-SMA |
| 180.17–180.30 | 2024-01-05 low / 2024-01-17 low | January floor |
| 179.54 | Bollinger lower | Volatility floor |
| 179.25 | 2024-02-02 low | **Hard invalidation of the washout thesis** |
| 178.19–178.66 | January Bollinger-lower lows | Final structural floor of the 2024 box |

---

## 9. Scenario map (subjective weights, explicitly not tool-derived)

**A. Constructive resolution — squeeze resolves upward (~40% weight).**
Trigger: a daily close **above 188.83 (VWMA)**, ideally above 190.65, on volume ≥ the 57M average. Confirmation comes from `macdh` curling up from −0.44, RSI reclaiming 50, and the close holding above the 200-SMA. Targets: 191.73–191.95, then 195.18–196.38, then 196.78. Stop for anyone entering on confirmation: below 186.86 or 1×ATR (182.26) for swing positions.

**B. Grind lower within the box / no-man's land (~40% weight).**
Price chops between 182.49 and 188.83 while ATR stays elevated and the Bollinger squeeze deepens. This is the highest-probability tape *given* the current configuration: MACD negative but shallow, RSI 43 (neither oversold nor overbought), flat 20-SMA, and a fresh high-volume reversal that has not been confirmed. Actionable stance: reduce size, sell the 188.2–188.8 cluster / buy the 182.5–183.8 shelf, and require closes — not intraday prints — for any regime call.

**C. Breakdown (~20% weight).**
Trigger: a close **below 182.49 (200-SMA)** on above-average volume, followed by a close below 179.25. That would flip the long-term regime line and convert the "failed breakdown" of 2024-02-02 into a mere pause in a downtrend. Then the 178.19 January band lows are the last defense, and a box-break measured move (box height ~17–18 points projected from the break level — a rule of thumb, not a tested statistic here) points materially lower. Note the specific danger: the 2024-02-02 low was *below* every January low, so the "floor" already has a crack in it.

---

## 10. Actionable plan and risk management

1. **Do not chase the 2024-02-02 reversal bar.** It closed below the 10 EMA, the 20-SMA and the VWMA, and RSI actually *fell* (45.07 → 43.34). The bar is a reason to stop being short-term bearish, not a reason to be aggressively long.
2. **The single best executable trigger is 188.83 (VWMA) on a closing basis**, because it coincides with 188.16 and 188.53. Buying strength above that cluster with a stop under 186.86 gives roughly a 2-point risk against a ~5–7 point first target (191.73 then 195.18) — a workable 2.5–3.5:1 setup.
3. **For holders: 182.49 is the line in the sand.** A close below the rising 200-SMA is the objective, mechanical signal that the 2023–24 uptrend has failed, and it is only 1.8% away. Use it (or 182.26 = close − 1 ATR) rather than a round-number stop.
4. **Volatility-adjusted sizing is mandatory.** ATR rose 10.7% in one session to 3.5864 (1.93% of price). Shares = (risk budget in $) ÷ 3.5864 for a 1-ATR stop, or ÷ 7.173 for a 2-ATR stop. With 2024-02-02's 8.08-point true range, any stop tighter than ~3.5 points will be noise-stopped.
5. **Watch the squeeze.** Bandwidth has gone 11.19% → 10.02% → 9.16%. Compression this persistent typically precedes an expansion of 2× ATR or more; be positioned to react rather than to predict, since both 196.78 and 179.54 are live targets depending on resolution.

**What would change the thesis (checklist):**
- Bullish flip: close > 188.83 + `macd` back above `macds` + RSI > 50.
- Bearish flip: close < 182.49 (200-SMA) + `macdh` beyond −0.70 + RSI < 35.
- Neutral continuation: everything else — respect the 182.49–188.83 box.

---

## 11. Summary table

| Dimension | Reading (2024-02-02) | Direction | Key evidence | Action |
|---|---|---|---|---|
| **Primary trend (200-SMA)** | 182.4919, rising ~+0.10/day | Bullish | +4.0% since 2023-12-04; price +1.84% above | Hold core; 182.49 is invalidation |
| **Medium trend (50-SMA)** | 190.6504, slope turned flat (peak 190.9252 on 2024-01-30) | Deteriorating | 4 consecutive closes below it | No add until reclaimed |
| **Short-term average (10 EMA)** | 188.5316, falling from 191.4059 (2024-01-29) | Bearish | Price 2.68 below | Short-term bias down |
| **Momentum (MACD)** | −0.3959 vs signal +0.0490; hist −0.4449 | Bearish, shallow | Crossover 2024-01-31; zero-cross 2024-02-01; hist only 22% of January trough | Confirm with price, don't front-run |
| **Oscillator (RSI)** | 43.34 | Neutral-weak | Not oversold (Jan low was 28.79); bearish divergence at 195 retest (70.02 → 62.62) | No mean-reversion buy yet |
| **Volatility envelope** | UB 196.7759 / LB 179.5361; bandwidth 9.16% | Squeeze | Compressed from 11.19% (2024-01-08) | Expect expansion; trade the break |
| **Band event** | Low 179.25 pierced LB 179.536 and reclaimed | Short-term bullish tell | Failed breakdown below Jan lows (180.17/180.30) | Needs close > 186.86 to matter |
| **Risk (ATR)** | 3.5864 (1.93% of price), 60-day high | Rising | +10.7% d/d; 2/2 range 2.5× prior ATR | Halve size; 1-ATR stop 182.26, 2-ATR 178.68 |
| **Volume (VWMA)** | 188.8268, above price; 2/2 volume 102.55M ≈ 1.8× avg | Conflicted | VWMA > price = distribution; heavy-volume reversal close = absorption | Wait for resolution |
| **Net posture** | Bull trend / bear correction inside a 179–197 box | **Neutral, tactical** | Price between 200-SMA and 50-SMA; 3 of 4 shorter averages inverted | Range-trade or stand aside; go with the close beyond 182.49 or 188.83 |

**Bottom line:** AAPL is a rising long-term trend currently digesting inside a narrowing, high-volatility box, and 2024-02-02 was a credible *defense* of the 200-SMA rather than a confirmed reversal. The evidence is genuinely two-sided — momentum (MACD crossover, zero-line break, negative histogram), RSI (43), and VWMA (price below it) all lean bearish, while the 200-SMA, the squeezed bands, and the highest-volume reversal close since mid-December lean bullish. The disciplined play is to let the market choose between **188.83** and **182.49**, size for 1.93% daily ATR, and treat any position taken before that resolution as a range trade, not a trend trade.