# AMZN — Technical Analysis Report
**As of the session close of 2024-02-02** | Data window: 2023-07-03 → 2024-02-02 (149 rows)

---

## 1. What Just Happened (the defining event)

The 2024-02-02 session is the single most important input for any read on AMZN right now.

| Metric | 2024-02-01 | 2024-02-02 | Change |
|---|---|---|---|
| Open | 155.87 | 169.19 | gap up +$13.32 (+8.55%) vs prior *high* |
| High | 159.76 | 172.50 | new high for the visible window |
| Low | 155.62 | 167.33 | low is *above* the entire prior 149-session high |
| Close | 159.28 | **171.81** | +$12.53 = **+7.87%** |
| Volume | 76.54M | **117.22M** | ~2.6x the ~45M recent norm |

Source of truth: `get_verified_market_snapshot` for 2024-02-02. These figures reconcile exactly with the `get_stock_data` CSV — **no discrepancies found** between tools.

Three structural facts follow directly from the data:

1. **This is a true breakaway gap, not an intraday spike.** The Feb 2 low (167.33) is higher than the prior window high (161.73 on 2024-01-30). The entire 159.76 → 167.33 zone is unfilled.
2. **It confirmed a breakout of a 6-week range.** AMZN closed between 144.57 (2024-01-04) and 161.26 (2024-01-29) for essentially all of January; Feb 2 closed ~6.5% above the top of that range.
3. **It is event-driven.** A one-session +7.87% move on 2.6x volume with a full gap is characteristically a news/earnings reaction. *(Inference — the tool set does not contain fundamental or headline data, so the cause is not verified here; only the price/volume signature is.)*

For context, the last comparable signature in this window was 2023-08-04 (+8.27% close-to-close, 153.1M volume) — which was followed by a drift to 142.22 on 2023-08-07 before a slow fade back to 125.98 by 2023-09-27. That is the relevant historical analogue for gap behavior in this name, and it argues for patience rather than chasing.

---

## 2. Indicator Selection (8) and Why

| Indicator | Value (2024-02-02) | Why it earns a slot here |
|---|---|---|
| **close_10_ema** | 159.8715 | Fastest read on whether the gap is being *held* or *sold*. Naturally becomes the first trailing reference after a vertical move. |
| **close_50_sma** | 151.5602 | Medium-term trend spine; quantifies how stretched price is versus the trend it must eventually revert toward. |
| **close_200_sma** | 133.9535 | Strategic trend benchmark; confirms the multi-month structure is up, so pullbacks are buyable, not shortable. |
| **macd** | 3.4647 | Detects whether the impulse is a genuine momentum re-acceleration vs. a one-day print. |
| **macdh** | 0.9443 | Measures the *thrust quality* of the move (histogram at a multi-month extreme = expansion, not exhaustion-by-slowing). |
| **rsi** | 73.7790 | Flags overbought extension and, more usefully here, lets us monitor for bearish divergence if price stalls at highs. |
| **boll_ub** | 166.3346 | Defines the statistical "stretched" boundary; close > upper band quantifies the extension objectively rather than by feel. |
| **atr** | 3.8797 | The only defensible basis for stops and position size after a volatility regime shift. |

*Deliberately excluded:* `close_10_ema` vs `boll` (20 SMA) overlap on short-term mean; `boll_lb` (145.07) is irrelevant at 18% above it; `mfi`/`vwma` were cross-checked (VWMA = 158.7868) as volume corroboration but not selected — the volume signal is already unambiguous in raw volume (117.2M).

---

## 3. Trend Structure: Unambiguously Bullish, Compressingly Extended

**Long-term (200 SMA):** 133.9535 and rising monotonically across the entire visible window — from 115.28 (2023-10-05) to 133.95 (2024-02-02), roughly +0.24/day. The 50 SMA has been above the 200 SMA every session in the dataset (no death-cross risk). Price is **+28.3% above the 200 SMA**. That is a late-stage-extension reading, not an early-trend reading.

**Medium-term (50 SMA):** 151.5602, also rising monotonically — 132.18 (2023-10-27) → 151.56 (2024-02-02). Price is **+13.4% above it**. The 50 SMA's steady grind with no flattening is important: the trend was already intact *before* the gap, which is what makes the gap a continuation-type breakaway rather than a blow-off top in a broken chart.

**Short-term (10 EMA):** 159.8715. The EMA turned up sharply from its 2024-01-05 trough (149.0987) and has now re-accelerated (157.22 → 159.87 on the gap day). Price sits **+7.48% above the 10 EMA** — about two normal daily ranges (2 x ATR = 7.76). This is the "held-but-stretched" configuration: trend-followers should be long, but the *entry* is poor here.

**Path since the swing low:** 119.57 close (2023-10-26) → 171.81 = **+43.7% in ~14 weeks**. And 144.57 (2024-01-04) → 171.81 = **+18.8% in 20 sessions**. The slope is steepening, which typically precedes either a consolidation or a sharp mean-reversion — it rarely persists linearly.

---

## 4. Momentum: Expansion, Not Exhaustion (yet)

- **MACD 3.4647** vs signal **2.5204** → histogram **+0.9443**.
- The histogram has been positive since 2024-01-19 (with a brief dip to −0.039 on 01-17 / −0.012 on 01-18), rising from 0.109 (01-19) to a local peak of 0.598 (01-29), compressing to 0.153 (01-31) on the pullback, then **exploding to 0.9443** — the largest positive reading anywhere in the Dec–Feb window.
- Read: this is **momentum expansion**, the signature of a fresh impulse leg. A bearish divergence would require a *higher* price high with a *lower* MACD peak. That does not exist yet. However, the histogram has already spent a month rising; histogram peaks characteristically occur 1–3 weeks *after* price peaks, so it offers no protection against a near-term pullback.

**RSI 73.78** is the single cleanest caution flag. It printed 70.41 on 2024-01-29 and then fell to 53.10 by 2024-01-31 — proving this stock *can* snap from overbought to neutral in two sessions without losing the longer trend. Prior RSI extremes in the window: 68.05 (2023-12-18) preceded a fade from ~154 to 144.05; 40.23 (2024-01-04) marked the January low. RSI >70 in a strong uptrend is not a sell signal — it is a signal that **the risk/reward of new entries at market is poor**.

---

## 5. Volatility Regime Shift — the Key Risk-Management Fact

- **ATR: 3.8797**, up from 3.1612 (2024-02-01) and a flat ~2.9–3.1 for all of January. That is a **+22.7% one-day jump in ATR**.
- ATR as % of price = **2.26%** (vs 1.98% the day before). The Feb 2 range itself (172.50 − 167.33 = 5.17) equals **1.33x ATR**.
- **Bollinger bandwidth expanded** from ~8.4% on 2024-01-03 (156.46 − 143.84 over a ~150 middle) to **13.66%** now (166.33 − 145.07 over 155.70). Volatility is expanding on the upside — a bullish breakout signal — but it also means every stop you set must be wider, and therefore every position smaller, or your dollar risk silently doubles.
- **Close (171.81) is 3.29% ABOVE the upper band (166.3346)**. In the visible window this is the first time price has exceeded the upper band, which confirms breakout force but simultaneously marks a statistically stretched condition. Upper-band rides in strong trends are real, but the *initial* violation is usually followed by a retest toward the 20-day middle (**155.70**) or at minimum a pause.

**Volume confirmation:** 117.22M vs. the ~40–50M January norm. VWMA (20-day, verified snapshot) = **158.7868**, meaning the average buyer over the last four weeks is up **+8.2%** on the close. That is a large aggregate open profit — which is both supportive (holders are not trapped) and a pullback risk (profit-taking supply).

---

## 6. Actionable Framework

### The core tension
Every trend indicator is bullish and every extension indicator is stretched. The resolution is *not* "buy or don't buy" — it is **"be long the trend, but source the entry from weakness, not from the gap."**

### Level map (all levels derived from tool output, with dates)

| Level | Value | Basis |
|---|---|---|
| Session high / window high | **172.50** | 2024-02-02 high |
| Close | 171.81 | 2024-02-02 |
| Stretch boundary | 166.33 | Bollinger upper |
| 1-ATR retracement | 167.93 | 171.81 − 3.8797 |
| Feb 2 low (gap top) | **167.33** | 2024-02-02 low — first "gap must hold" test |
| 10 EMA / gap top | **159.87** | 10 EMA 159.8715 ≈ Feb 1 high 159.76 |
| Full gap fill / Feb 1 close | **159.28** | 2024-02-01 close |
| 20-day middle band | 155.70 | `boll` |
| VWMA (20d) | 158.79 | verified snapshot |
| 50 SMA | **151.56** | medium-term trend spine |
| January range top→bottom | 161.26 → 144.57 | 2024-01-29 close / 2024-01-04 close |
| Measured-move target | **178.89** | Jan range height 16.69 added to 161.26 |
| 200 SMA | 133.95 | long-term benchmark |

### Trade construction

**1. For existing longs — hold, tighten mechanically.** Trail with 2x ATR = **164.05**, which conveniently sits just under the Feb 2 low (167.33) and above the 10 EMA. Alternatively use the 10 EMA (159.87) as a closing-basis trend stop; a daily close below 159.87 would break the gap *and* the fast trend simultaneously — a clean, non-arbitrary invalidation. Do not move stops to breakeven inside 1 ATR of price; at 2.26% daily ATR you will be stopped by noise.

**2. For new longs — do not chase 171.81.** Price is 3.3% above the upper band, RSI is 73.8, and price is 7.5% above the 10 EMA. Two-tier accumulation:
- **Tier 1 (40% of intended size):** 167.33–164.05 zone (Feb 2 low → 2 ATR). This is the "gap holds" test. A close back above 169 after a tag of this zone is the highest-quality continuation signal available.
- **Tier 2 (60%):** 161.26–159.28 (Jan 29 close / Feb 1 close). **Note the confluence:** the gap-fill level (159.28), the 10 EMA (159.87), and the top of the prior range (161.26) cluster within ~2%. If price reaches here *and holds*, it converts the gap into a normal retest — a much better risk point, with invalidation below 155.70 (middle band).

**3. Invalidation / short-side view.** A daily close below **159.28** (full gap fill) fails the breakaway thesis and shifts the stock back to range-bound, with 155.70 then 151.56 as the mechanical downside magnets. A close below 151.56 would break the 50 SMA and mark an actual trend change. Given the 200 SMA at 133.95 and rising, the structural bias remains up until 151.56 fails — so shorting is a tactical trade only, not a thesis.

**4. Position sizing (the most actionable item).** With ATR at 3.88 (2.26% of price) and a 2-ATR stop distance of 7.76: for a 1.0% account risk, size = 1.0% / 7.76 price units. Compared with early January (ATR ~2.9, 2-ATR distance 5.8), the same risk budget now buys **~25% less exposure per share**. Size down accordingly; the volatility regime changed on 2024-02-02.

### What would upgrade the thesis
- A weekly-style consolidation that *holds* above 167.33 for several sessions while RSI cools from 78 toward 60–65 without price giving up ground. That is the classic continuation setup and would justify adding back to full size with a 167 stop.
- MACD histogram holding positive while price makes a slightly higher high → confirms trend persistence.
- Follow-through volume that stays above ~60M on up-days.

### What would downgrade the thesis
- **Bearish RSI divergence:** price tags/exceeds 172.50 while RSI fails to exceed 73.78. Combined with a MACD histogram peak (as seen on 2024-01-29 at 0.598 followed by a 2-session drop to 53.10 RSI), that would be the highest-probability warning of a gap-fill toward 159–161.
- A close inside the gap (below 167.33) on rising volume — i.e., "gap and trap."
- Failure of the 10 EMA (159.87) — fast-trend break.

### The one honest caveat
Everything here is a **single-session** observation. One day of price and volume cannot establish that 167.33 will act as support or that the gap holds; the tool set contains no forward outcomes. The August 2023 analogue (gap up 2023-08-04 to 139.57, high 143.63 on 08-07, then decay to 125.98 by 2023-09-27) is a reminder that post-gap drift in AMZN has historically been *two-sided*. The disciplined stance is: **bullish bias, patient entry, ATR-scaled risk.**

---

## 7. Summary Table

| Dimension | Reading (2024-02-02, verified) | Signal | Confidence |
|---|---|---|---|
| Price action | Close 171.81, +7.87% d/d, gap 159.76→167.33 unfilled | Breakaway gap | High |
| Volume | 117.22M (~2.6x January norm) | Strong confirmation | High |
| Long-term trend | 200 SMA 133.95, rising since ≥2023-10; price +28.3% above | Bullish, extended | High |
| Medium-term trend | 50 SMA 151.56, rising; price +13.4% above; 50 > 200 all window | Bullish | High |
| Short-term trend | 10 EMA 159.87; price +7.5% above (≈2 ATR) | Bullish, overextended | High |
| Momentum | MACD 3.4647 > signal 2.5204; histogram 0.9443 = window high | Expanding thrust, no divergence | High |
| Overbought | RSI 73.78 (prior 70.41 on 01-29 → 53.10 on 01-31) | Overbought; snapback risk real | High |
| Volatility band | Close 3.29% above upper band 166.33; bandwidth 8.4%→13.7% | Breakout + statistical stretch | High |
| Volatility regime | ATR 3.88 (+22.7% d/d), 2.26% of price | Regime shift — resize | High |
| Volume-weighted cost | VWMA 158.79; holders +8.2% in profit | Supportive but profit-taking supply | Medium |
| Primary plan | Hold longs; add 167.33–164.05 (40%) and 161.26–159.28 (60%) | Buy weakness, not the gap | — |
| Stop / invalidation | Trail 2 ATR = 164.05; hard thesis break below 159.28; trend break below 151.56 | — | — |
| Upside projection | 178.89 (January range measured move) | Conditional on gap holding | Medium |
| Discrepancy check | Snapshot vs. `get_stock_data` — all OHLCV and indicator values match | Clean | — |

**Bottom line for AMZN:** the chart is in its strongest confirmed uptrend of the visible window (price, 50 SMA, 200 SMA, MACD, and volume all aligned bullish), but 2024-02-02 pushed price into a statistically stretched position (RSI 73.8, 3.3% above the upper Bollinger band, 2 ATR above the 10 EMA) at the exact moment the volatility regime shifted upward. Treat 167.33 as the gap-validity line and 159.28 as the thesis-validity line; size positions off ATR 3.88 rather than off the pre-breakout ~2.9, and let the market come back to you.