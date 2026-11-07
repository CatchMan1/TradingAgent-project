## AMZN — Multi-Indicator Technical Assessment (as of close 2024-02-21)

**Data-integrity note:** The `get_stock_data` history (141 sessions, 2023-08-01 → 2024-02-21) and the `get_verified_market_snapshot` agree on every overlapping row (OHLCV, splits = 1.0, dividends = 0.0). **No discrepancy to flag.** All price and indicator values below are taken from the verified snapshot or the indicator series returned by the tools. (Note: 2024-02-19 is absent because it was a U.S. exchange holiday.)

---

### 1. Market context and the dominant event

AMZN's primary feature on the chart is the **post-earnings repricing gap of 2024-02-02**: the stock closed 2024-02-01 at **159.28** and then opened 2024-02-02 at **169.19**, closing **171.81** with a **117.22M** share volume print and an intraday high of **172.50**. That is a **+7.87% close-to-close move** on roughly 2.5× the then-prevailing volume. The origin high on 2024-02-01 was 159.76 while the 2024-02-02 low was 167.33, so an **unfilled gap band of approximately 159.76–167.33** remains beneath the price.

Since that gap, price has been in a **constructive consolidation** rather than a distribution:
- Swing high **175.39** intraday on 2024-02-12 (close 172.34); prior high **175.00** on 2024-02-09 (close 174.45 — the highest close in the sample).
- Two intraday lows essentially identical: **165.75** (2024-02-13) and **165.74** (2024-02-20).
- Latest session (2024-02-21): open 168.94, high **170.23**, low 167.14, close **168.59**, volume **44.42M**.

So the stock is oscillating inside a **~165.7 to ~175.4** post-earnings range, currently in the lower-middle of it, ~3.9% below the 2024-02-12 high.

---

### 2. Trend structure — unambiguously bullish, but decelerating at the short end

| Measure | Value (2024-02-21) | Read |
|---|---|---|
| Close | 168.59 | — |
| 10 EMA | 168.629 | Price is *at*, marginally below, the 10 EMA |
| 50 SMA | 157.291 | Price **+7.18%** above |
| 200 SMA | 137.872 | Price **+22.28%** above |

- **Medium/long term is strongly up.** The 50 SMA has risen every single session in the pulled window: 148.67 (2024-01-22) → **157.29** (2024-02-21), a gain of ~8.6 points in 22 sessions, with zero flat or down days in that series. The 200 SMA is doing the same, 131.34 → **137.87**. Both rising, with the 50 SMA sitting **+14.1%** above the 200 SMA — a wide, mature bullish separation, i.e. a long-established uptrend (I am not asserting a specific golden-cross date, as the tool window doesn't reach back far enough to date it).
- **Short term has flattened into equilibrium.** The 10 EMA went 168.03 (2024-02-12) → 168.63 (2024-02-21) — a rise of only **0.60 over seven sessions** — while price chopped between 165.74 and 175.39. The 10 EMA has also turned down microscopically from 168.98 (2024-02-16) to 168.63. The close at 168.59 finishing *below* the 10 EMA is the first evidence of short-term loss of control by buyers.
- **Interpretation:** this is a textbook "flag after a gap" — slope of the intermediate average intact and accelerating, short average going horizontal to let price catch up. Nothing in the moving-average complex breaks the bullish thesis yet; the 50 SMA at **157.29** is the trend's true line in the sand, ~6.7% below spot.

---

### 3. Momentum — the one genuinely cautionary cluster

**MACD (12,26,9):** MACD line **3.953**, signal **4.483**, histogram **−0.530**.
- The line peaked at **5.501** on 2024-02-12 and has fallen for six straight sessions (5.229 → 5.144 → 4.924 → 4.673 → 4.229 → 3.953).
- The **bearish crossover occurred on 2024-02-16**: histogram was +0.203 on 2024-02-15 and −0.039 on 2024-02-16, then widened to −0.386 (2024-02-20) and **−0.530** (2024-02-21).
- Critically, the **MACD line is still well above zero (3.95)**. This is a *momentum-of-momentum* cooling, not a trend reversal — the correct read is "the impulse leg off the gap has matured," not "go short the stock." A MACD histogram that keeps widening negative while price holds above 165.7 would be a warning of an exhaustion top; a histogram that starts contracting while price holds 166–171 would be the re-entry trigger.

**RSI(14):** **58.07**, down from **73.78** (2024-02-02) and **72.43** (2024-02-09), with a low of 55.91 on 2024-02-20.
- The overbought condition has been **fully unwound without a price breakdown** — best case for bulls, because it happened through time/rotation rather than through a 5–8% drawdown.
- There is a **mild bearish divergence** worth noting, supported directly by the data: RSI made successively lower highs (73.78 on 2024-02-02 → 72.43 on 2024-02-09 → 67.90 on 2024-02-12) while price made a higher high (close 171.81 → 174.45 → 172.34, and intraday 175.00 → 175.39). That is a *momentum* non-confirmation at the highs, and it is consistent with the MACD roll-over rather than a contradiction of it.
- RSI at 58 is neutral-to-constructive: room to run in either direction, no oversold cushion.

---

### 4. Volatility — wide post-earnings envelope, bands now compressing at the top

- **Bollinger (20,2):** middle **166.075**, upper **178.279**, lower **153.872**. Total width ≈ **24.41 points, ~14.7% of the middle band**.
- Band width has **expanded hard** since pre-earnings: on 2024-01-22 the bands were 145.84–158.16 (≈8.1% of the 152.00 midpoint). The 2024-02-02 gap forced the expansion.
- **But the shape has changed:** the upper band has rolled from 178.58 (2024-02-16) to **178.28**, while the lower band has climbed steadily from **151.08 → 153.87** over the same five sessions. A flattening upper band with a fast-rising lower band is the mechanical signature of **volatility contraction after a spike** — consistent with a multi-week coiling range, not an accelerating trend.
- **Position within the band (%B ≈ 0.60):** price 168.59 is modestly above the **166.08** middle band and far from the **178.28** upper band. That means: (a) no overbought-band "riding the band" condition, (b) the middle band at **~166.1** is the nearest mechanical mean-reversion reference and lines up almost exactly with the 2/13–2/20 lows of 165.74–165.75 — a genuinely confluent support shelf at **165.7–166.1**.
- **ATR(14):** **3.756**, or **2.23%** of the close, up from 3.00 (1.94%) on 2024-01-22. Volatility is elevated but contracting from the 3.94 post-earnings peak (2024-02-13).

---

### 5. Volume / participation

- `vwma` sits at **168.870** against a close of **168.590** — price has slipped *just below* the volume-weighted average, on 2024-02-20 (167.08 vs 168.07) and again on 2024-02-21. This is a **mild** distribution tell, not a decisive one: the gap is 0.17%, inside the daily noise of the 3.76 ATR.
- VWMA at 168.87 versus 50 SMA at 157.29 confirms the volume-weighted center of trading is ~11.6 points *above* the simple 50-day mean — the recent heavy-volume activity happened at higher prices, which is what a healthy post-breakout re-rating looks like.
- Raw volume is **drying up**: 117.22M (2024-02-02) → 55.08M → then a run of 42–57M sessions → **44.42M** on 2024-02-21. The last three prints (48.11M, 41.98M, 44.42M) average ~44.8M versus a 22-session average of ~51.7M (and ~48.6M excluding the earnings day). **Contracting volume on a contracting range** is the classic constructive consolidation profile; a breakdown would need an expansion in volume to be trusted.

---

### 6. Actionable scenario map

**Bull case (primary, given 50 SMA > 200 SMA, both rising, and price 7.2%/22.3% above them):**
- The consolidation resolves upward on a **daily close above 171.43** (2024-02-08 high 171.43; 2024-02-15 high 171.17 is the same shelf) **with volume above ~57M** (the 2024-02-09 level) as confirmation.
- First target **175.00–175.39** (the 2024-02-09/02-12 highs), then the **178.28** upper Bollinger band.
- MACD confirmation to demand before adding: histogram turning back up from −0.53 (i.e. a positive/bullish MACD re-cross). Until then, upside probes are lower-conviction.

**Neutral/base case (most likely near term):** continued **165.7–171.4** rotation. The flat 10 EMA (168.63) and price sitting right on it, with MACD histogram negative but the MACD line still 3.95 above zero, is the definition of balanced. Range-trading bias: buy 166–167, sell 170.5–171.4, until either boundary breaks on volume.

**Bear case (secondary, needs a trigger):**
- A **daily close below 165.74** (the 2024-02-13 and 2024-02-20 lows) breaks the shelf that coincides with the 166.08 middle band. Measured targets then become: **163.4** (1 ATR below the 2024-02-21 close), the **159.76–167.33 gap band** (partial fill already achieved with the 165.74 low), and ultimately the **gap-origin / 50 SMA confluence near 157.3–159.8** — a zone that is ~6% below spot and would be the first real test of the intermediate trend since the gap.
- The bear case is corroborated, not proven, by: MACD histogram at −0.53 and widening; close below the 10 EMA; close below VWMA; and the mild RSI lower-high sequence. It is **contradicted** by: price above the rising 50 and 200 SMA, %B at 0.60 (not weak), and declining volume on the pullback.

**Risk management (ATR-calibrated, ATR = 3.756):**
- Trend followers: place the invalidation **below 165.7** (≈0.77 ATR from spot) for a tight tactical stop, or **below 160.5** (≈2.2 ATR, under the gap band's midpoint) for a swing stop that survives noise. A 2-ATR stop is ~7.5 points / ~4.5%.
- Because ATR is 2.23% of price, size positions on a risk-per-share of ~3.8–7.5 rather than a fixed dollar stop; volatility is ~15% higher than it was on 2024-01-22 (ATR 3.00).
- Do not chase entries between 168.5–170.2: that is the no-man's-land between the 10 EMA and the 171.4 shelf, where the reward-to-risk to either boundary is under 1:1.

---

### 7. Why these indicators were selected (8, non-redundant)

| Indicator | Role in this specific setup |
|---|---|
| `close_10_ema` | Price is *pinned* to it (168.59 vs 168.63) — the single cleanest measure of whether the 3-week stall is resolving up or down. |
| `close_50_sma` | The rising intermediate trend and the true invalidation of the post-earnings move (157.29). |
| `close_200_sma` | Strategic confirmation that the 2023-10 basing (close 119.57 on 2023-10-26) turned into a durable uptrend; 137.87 is far below price, so it is used only for regime, not for entries. |
| `macd` | Detects the 2024-02-12 momentum peak (5.501) and the subsequent six-session decay to 3.953 — the core "impulse maturing" signal. |
| `macds` | Needed to date the bearish cross precisely (2024-02-16) and to watch for a re-cross as the add-on trigger; not redundant with `macd` because the cross *timing* is the trade signal. |
| `rsi` | Documents the overbought reset (73.78 → 58.07) and the lower-high sequence at the swing highs — a divergence check the MACD cannot provide. |
| `boll_ub` | 178.28 marks the realistic upside envelope and shows the upper band flattening (178.58 → 178.28) — evidence of volatility contraction, not acceleration. |
| `atr` | 3.756 / 2.23% sets stop distance and position size; essential because post-earnings ATR is ~25% above its pre-gap level. |

*(Deliberately excluded: `boll` middle 166.08 and `boll_lb` 153.87 are cited from the verified snapshot as confluence levels but not selected — the middle band is largely a 20-SMA proxy for the 10 EMA/50 SMA pair already in the set. `vwma` was reviewed and cited (168.87, price marginally below) but omitted from the formal set to stay within 8; it adds little beyond the volume-dry-up observation. `mfi` was excluded as its snapshot value (0.4967) is not on a 0–100 scale in this vendor's output and cannot be compared to standard thresholds.)*

---

### 8. Summary table

| Dimension | Reading (2024-02-21) | Signal |
|---|---|---|
| **Price** | Close **168.59** (O 168.94 / H 170.23 / L 167.14), vol 44.42M | 3.88% below 2024-02-12 high of 175.39 |
| **Primary trend** | 50 SMA **157.29** (rising daily), 200 SMA **137.87** (rising) | **Bullish** — price +7.18% / +22.28% above |
| **Short-term trend** | 10 EMA **168.629**, flat (168.03 → 168.63 over 7 sessions) | **Neutral** — price marginally below the 10 EMA |
| **Momentum (MACD)** | MACD **3.953**, signal **4.483**, hist **−0.530** | **Bearish cross 2024-02-16, widening** — but line still >0 |
| **Momentum (RSI)** | **58.07** (from 73.78 on 2024-02-02) | **Neutral-positive**; mild lower-high divergence |
| **Volatility** | Boll 166.08 / UB **178.28** / LB **153.87**; %B ≈ 0.60; ATR **3.756 (2.23%)** | Wide envelope **contracting**; upper band flattening |
| **Participation** | VWMA **168.87** vs close **168.59**; volume declining (117M → 44M) | **Mild caution**; contraction, not distribution |
| **Key resistance** | 169.51–170.23 → **171.17–171.43** → **175.00–175.39** → 178.28 | Upside trigger: close >171.43 on >57M volume |
| **Key support** | **165.74–166.08** (2/13 & 2/20 lows + Boll middle) → 163.4 (1 ATR) → **159.76–167.33 gap band** → 157.29 (50 SMA) | Downside trigger: close <165.74 |
| **Stance** | Long-biased trend intact, but momentum is in a cooling phase | **Hold/core long; add only above 171.43 with volume; tactical stop <165.7, swing stop <160.5; stand aside between 168.5–170.2** |