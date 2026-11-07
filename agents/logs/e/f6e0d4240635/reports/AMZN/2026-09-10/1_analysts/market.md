# AMZN — Multi-Timeframe Technical Review
**Analysis date: 2026-09-10 | Last close: $251.89**

---

## 1. Data integrity note

The `get_stock_data` series (252 rows, 2025-09-10 → 2026-09-10) and the `get_verified_market_snapshot` agree exactly on the final session and on every indicator value used below. **No discrepancy to flag.** The `technical_total_return_index` equals the close on every row (dividend = 0.0), so the price series is effectively a total-return series with no distribution adjustment — all percentage moves below are pure price moves.

Latest verified bar (2026-09-10): **O 250.11 / H 253.15 / L 249.58 / C 251.89 / V 25.48M**.

---

## 2. Bottom line

AMZN is in a **short-term downtrend nested inside an intact longer-term uptrend**. The stock has traced a textbook sequence of **lower highs and lower lows since the 2026-08-03 peak**, has now closed below its 50-day SMA for the first time since 2026-07-30, and its MACD has crossed back below zero. At the same time, the **200-day SMA is still rising**, the 50/200 spread is positive, and the prior higher-low structure (196.00 → 199.14 → 226.16) is unbroken.

The most important new information is not the direction — it is the **volatility collapse**. Bollinger bandwidth has compressed from ~29.7% on 2026-08-10 to ~6.2% today, and ATR has fallen 37% from its 2026-08-03 level. That is a coiled-spring setup sitting **directly on the lower Bollinger band**, which resolves the indecision but does not itself pick the direction. Because price, momentum and the volume-weighted average all lean lower, the **near-term skew is modestly bearish within a neutral-to-bullish longer-term structure**. This is a "reduce conviction, define levels, wait for the break" tape — not a high-conviction directional entry.

---

## 3. Indicator selection and why (8 chosen, non-redundant)

| Indicator | Role in this specific setup | Why it earns a slot |
|---|---|---|
| `close_200_sma` | Strategic trend anchor | Separates "short-term pullback" from "trend failure"; coincides almost exactly with the unfilled gap floor and is the natural downside magnet |
| `close_50_sma` | Medium-term pivot | Price has just lost it after 5+ weeks above; it is both the first evidence of trend damage and the first resistance to reclaim |
| `vwma` | Volume-weighted "fair value" | Volume-weighted holders' average (258.16) sits **above** spot — quantifies overhead supply that a plain SMA cannot |
| `macd` | Momentum regime / zero-line | The zero-line cross on 2026-09-09 is a regime-change marker, distinct from the signal crossover |
| `macdh` | Momentum acceleration & cross timing | Sign flip = signal crossover; slope shows whether the bear leg is accelerating or exhausting (it is re-widening) |
| `rsi` | Exhaustion / divergence check | At 43.6 with price on the lower band, RSI answers the key question: is there room to fall? (Yes.) |
| `boll` | Band benchmark + squeeze measurement | Bandwidth vs. the 2026-08-10 reading is the single best volatility-regime datapoint |
| `atr` | Position sizing & stop distance | Essential after a 12.6% earnings gap and during a squeeze; converts levels into risk units |

Deliberately **excluded**: `close_10_ema` (subsumed by VWMA, which adds volume information — see §5), `macds` (redundant with `macdh`, whose sign flip encodes the crossover), `boll_ub`/`boll_lb` as standalone selections (band values are read from the verified snapshot inside the `boll` analysis), and any oscillator with a >70/<30 trigger profile that would duplicate RSI.

---

## 4. Multi-timeframe trend structure

### 4.1 Long-term (strategic): intact uptrend
- **`close_200_sma` = 239.62**, rising every session since late June (232.51 on 2026-06-12 → 239.62 today, +3.1%).
- **`close_50_sma` = 254.95** vs. 200-day = 239.62 → **positive spread of +15.33 (+6.4%)**, i.e. the golden-cross configuration remains in force.
- The 252-session swing structure is **higher lows and higher highs**: lows at 197.28 (2026-02-13) → 199.14 (2026-03-27) → 226.16 (2026-07-29); highs at 247.86 (2026-01-09) → 265.91 (2026-04-29) → **287.20 (2026-08-03, 52-week high)**.
- Current price is **+5.1% above the 200-day** and sits at the **61st percentile** of the 52-week range (196.00–287.20). Nothing in the long-term data says "trend over."

### 4.2 Medium-term: first crack in the trend
- Price closed **below the 50-day SMA on 2026-09-09 (252.40 vs 254.68) and again on 2026-09-10 (251.89 vs 254.95)**. The prior close below that line was **2026-07-30** — the session before the earnings gap. This is the **first 50-day break since the 2026-07-31 breakout**.
- The 50-day is still **rising** (~+0.43/session over the last nine sessions), so this is a *test from above*, not yet a failed average. A rising 50-day that price cannot reclaim within a few weeks is the classic "distribution" signature; two closes do not confirm it.
- **Important nuance:** the 50-day (254.95) is *below* the 20-day/Bollinger middle (259.38). Short-term average above medium-term average is a **bearish alignment for the retracement leg**, even though 50 > 200 is bullish. The market is compressing, not trending cleanly.

### 4.3 Short-term: established downtrend
The swing map since the peak is unambiguous and every turn is verifiable in the OHLC data:

| Date | Event | Price |
|---|---|---|
| 2026-08-03 | Peak high / peak close | 287.20 / 284.02 |
| 2026-08-10 | Lower high | 280.14 |
| 2026-08-18 | Swing low | 257.73 |
| 2026-08-19 | Lower high | 266.40 |
| 2026-08-28 | **Lower high** (failed rally) | 267.56 |
| 2026-09-10 | **Lower low** | 249.58 |

That is **three descending highs and a descending low** — a defined, orderly downtrend channel, not noise. From the 2026-08-03 close to today: **−11.31%**.

- The 2026-08-28 session (+3.97%, 256.26 → 266.43 on **49.5M shares**, the heaviest volume since 2026-08-03) was the bulls' best shot and it **failed within three sessions**, with price giving back the entire gain by 2026-09-01 (close 254.92). A high-volume up-day that is fully retraced is a failed-breakout/false-breakout pattern and is the strongest single piece of bearish evidence in the recent tape.
- Price has closed below the 10-day EMA in **15 of the last 17 sessions** (2026-08-18 → 2026-09-10), the only exceptions being 2026-08-19 and 2026-08-28. Persistent, not episodic.

---

## 5. Volume-weighted positioning (VWMA)

- **`vwma` = 258.16**, versus close **251.89** → price is **2.43% below the volume-weighted average price**.
- VWMA peaked at **272.05 on 2026-08-20** and has declined every session since (−5.1%). It is falling *faster* than the 50-day, which tells you the **recent volume has been transacted at lower prices** — sellers are, on balance, the ones setting the marginal price.
- Interpretation: the 256–258 zone is not merely a moving average; it is the **average cost basis of recent volume**. Any rally into that zone should expect supply. This is precisely why VWMA was selected over `close_10_ema` (256.55) — same neighborhood, but VWMA carries the extra information that the *volume* is behind it.
- **Volume character of the decline:** 2026-08-31 was the heaviest distribution day of the slide (−2.5%, 46.1M shares); 2026-09-01 −1.9% on 31.7M; 2026-09-09 −1.77% on 33.1M. But **2026-09-10's decline came on only 25.48M shares — the lightest volume since 2026-08-26 (21.5M)**. That is a mild positive divergence in effort-vs-result: price made a new closing low for the leg on *contracting* volume. It is **not** a reversal signal (no price divergence, and one day is one day), but it argues against panic-selling pressure and raises the odds of a stabilization attempt near the band.

---

## 6. Momentum

### MACD — regime change, confirmed
- **`macd` = −0.879**, **`macds` = +0.550**, **`macdh` = −1.429**.
- The MACD line **crossed below its signal on 2026-08-17** (5.83 vs 6.14) and the histogram has been negative for **18 consecutive sessions**. This is not a fresh crossover — the cross is four weeks old and already "spent."
- What *is* fresh: the **MACD line crossed below zero on 2026-09-09** (−0.42, first negative print since 2026-07-30) and extended to −0.879 today. The zero-line break is the more significant event because it says the *trend* momentum, not just the momentum-of-momentum, has flipped negative.
- **Histogram path:** −1.114 (2026-08-28) → −1.154 → −1.454 → −1.585 → −1.354 → −1.179 → −1.120 → **−1.328 → −1.429**. Note the brief narrowing into 2026-09-08 that looked like exhaustion, followed by **two sessions of re-widening**. Downside momentum is **re-accelerating, not decelerating**. That kills the "bottoming" thesis for now.

### RSI — no oversold cushion, no divergence
- **`rsi` = 43.62**, down from 55.85 on 2026-08-28 and from 49.55 on 2026-09-04.
- The **lowest reading since 2026-07-29 (33.31)**, but still **mid-range and 13.6 points above oversold**. Critically, this is not the profile of a washed-out tape: in the July drawdown RSI reached 33.31 and price bottomed at 226.16, giving a much better risk/reward for buyers than today.
- **No bullish divergence exists.** Price made a lower low on 2026-09-10 (249.58 vs 255.02 on 2026-08-27) and RSI made a lower low (43.62 vs 47.23). Momentum is confirming price, not diverging from it.
- Similarly, there is **no bearish divergence** left to trigger a further leg down from a stretched condition — RSI is neutral, so it can drift toward 35–40 without any mechanical support.

---

## 7. Volatility and band structure — the squeeze is the story

| Measure | 2026-08-10 | 2026-09-10 | Change |
|---|---|---|---|
| Bollinger upper | 290.69 | **267.48** | −8.0% |
| Bollinger middle (20 SMA) | 253.13 | **259.38** | +2.5% |
| Bollinger lower | 215.57 | **251.28** | +16.6% |
| **Bandwidth (UB−LB)/mid** | **29.68%** | **6.25%** | **−79%** |
| ATR (14) | 9.13 | **6.26** | −31% (vs 9.95 on 08-03) |

- **The squeeze is extreme.** A bandwidth collapse from 29.7% to 6.25% in one month, driven almost entirely by the *lower* band racing up (+16.6%) while the *upper* band collapsed (−8.0%), is a textbook volatility-contraction pattern. The bands are converging on price, not price chasing the bands.
- **Price is pinned to the lower band:** close 251.89 vs lower band 251.28 → **%B ≈ 3.8%**. The 2026-09-10 intraday low of **249.58 actually traded through the lower band (251.28) before closing back above it** — an undercut-and-recover. That is a *potential* short-term stabilization tell, but one session is not confirmation, and it happened on the lightest volume of the recent window.
- **`atr` = 6.26 = 2.49% of price.** This matters mechanically:
  - Today's range was 3.57 points = **0.57 ATR** — a quiet, indecisive session.
  - A stop placed inside ~6 points of entry is inside one day's normal noise and will be randomly harvested.
  - **2 × ATR below 251.89 = 239.4**, which lands *exactly* on the 200-day SMA (239.62) and the gap floor (239.82). That confluence is the structural stop for a swing position.
- **The real risk: gap risk.** This name has produced two >8% earnings-driven gaps in eight months (2026-02-06: 222.69 → 202.70 open, −8.98%; 2026-07-31: 235.50 → 265.00 open, +12.5%). ATR-based stops provide **no protection** across such an event. If a catalyst falls inside your holding window, size for the gap, not the ATR.

---

## 8. Price-level map (all levels derived from tool data)

**The unfilled earnings gap (2026-07-31)** is the organizing structure: 2026-07-30 high **239.82** → 2026-07-31 low **262.01**, a **9.25% gap**. Price at 251.89 is roughly **51% filled**.

Fibonacci retracement of the 2026-07-30 close (235.50) → 2026-08-03 high (287.20), range 51.70:

| Fib | Level | Confluence observed in the data |
|---|---|---|
| 38.2% | **267.45** | 2026-08-28 high **267.56** tagged it almost exactly, then failed |
| 50.0% | **261.35** | Inside the gap; 20-day SMA 259.38 just below |
| 61.8% | **255.25** | 2026-09-04 close 258.51 stalled above it; price now below |
| 78.6% | **246.56** | Next downside objective; below the lower band |
| 100% | **235.50** | 2026-07-30 close = gap origin |

**Resistance stack (a 1.7%-wide wall from 254.95 to 259.38):**

| Level | Value | Distance from close |
|---|---|---|
| 50-day SMA | **254.95** | +1.2% |
| 10-day EMA | 256.55 | +1.9% |
| VWMA (volume-weighted cost) | **258.16** | +2.5% |
| Bollinger middle / 20 SMA | **259.38** | +3.0% |
| 61.8% Fib | 255.25 | +1.3% |

> This clustering is the single most actionable observation in the report: **four independent measures sit within 4.4 points of each other**. A close above ~259.4 is a genuine trend repair; anything below ~254.9 is still a failed bounce.

**Support stack:**

| Level | Value | Basis |
|---|---|---|
| Bollinger lower band | **251.28** | Price is 0.61 above it; intraday undercut today |
| 2026-09-10 low | **249.58** | The leg's low — the line that defines "still falling" |
| 78.6% Fib | **246.56** | First objective if 249.58 breaks |
| **239.6 – 241.0** | 200-day SMA **239.62**, gap floor **239.82**, 2026-07-30 high **239.82** | Highest-confluence downside zone |
| 235.50 | 2026-07-30 close | Gap fully filled; also 100% Fib |
| 226.0 – 226.2 | 2026-06-25 low 225.55 / 2026-07-29 low 226.16 | Medium-term floor (double bottom) |

---

## 9. Scenarios with explicit invalidation

**Scenario A — Squeeze resolves downward (base case, ~45%).**
Trigger: a daily close below **249.58** (and especially below the lower band 251.28 on expanding volume).
Path: 246.56 (78.6% Fib) → **239.6–241.0** (200-day SMA + gap floor + 200% extension cluster).
Invalidation: a close back above **254.95** before 246.5 is touched.
Note: this scenario is *supported but not proven* — it requires price to keep making lower lows, which it has done for six weeks.

**Scenario B — Band-riding stabilization / chop (base case, ~35%).**
Trigger: price holds 249.5–251.3 and oscillates; bandwidth stays compressed.
Path: range 249.6 → 259.4. Nothing is resolved; the 50-day flattens.
Invalidation: a close outside 246.5 / 259.4.

**Scenario C — Squeeze resolves upward / trend repair (secondary, ~20%).**
Trigger: a **volume-expanding close above 259.4** (Bollinger middle), ideally above 262.0 (gap mid / 50% Fib).
Path: 267.4–267.6 (38.2% Fib = 2026-08-28 high) → 270.7 (2026-08-05 low) → 280.1 (2026-08-10 high).
Invalidation: a close back below 254.95.
Caution: upward squeeze resolution is the *lower-probability* path because MACD histogram is re-widening negative and VWMA is still above price. Do not anticipate it; require it.

**Scenario D — Long-term trend failure (~low probability, tail risk).**
Trigger: weekly close below **239.6** (200-day SMA + gap floor), converting the July gap into a failed breakout.
Path: 235.50 → 226.2 → opens a retest of the 196–200 floor.
This is the scenario that would invalidate the higher-low sequence and require abandoning any strategic long bias.

---

## 10. Actionable trade construction

**For a swing long (contrarian, waiting for confirmation):**
- Do **not** buy the band touch. Buy the **reclaim**: a close above **254.95** (50-day) with volume > ~35M, confirmed above 256.5.
- Stop: **246.40** (below the 78.6% Fib at 246.56) — 8.5 points = **1.36 ATR**, i.e. wide enough to survive normal noise.
- Targets: T1 **258.16** (VWMA), T2 **259.38** (Bollinger middle), T3 **267.5** (38.2% Fib / 08-28 high).
- R:R at T2 ≈ 4.3/8.5 ≈ **0.5:1** — poor. At T3 ≈ **1.5:1** — acceptable. This is why the *reclaim* entry is inferior unless the 259.4 breakout is used instead.
- **Better long entry:** close above **259.40** on volume > 40M. Stop 251.20 (below the lower band) = 8.2 points (1.31 ATR). T1 267.50 (+8.1), T2 280.14 (+20.7) → R:R ≈ **1:1 to 2.5:1**.

**For a short (trend-following, aligned with the tape):**
- Entry: close below **249.58** (2026-09-10 low), or a failed retest of 254.95–256.5.
- Stop: **257.00** (above the 10-EMA and VWMA cluster) — 7.4 points = **1.18 ATR**.
- Targets: T1 **246.56** (+3.0), T2 **240.50** (+9.1), T3 **235.50** (+14.1).
- R:R at T2 ≈ **1.2:1**; at T3 ≈ **1.9:1**. The trade only pays if the 200-day is actually tested, so **scale out at 246.5 and trail**.
- **Caveat:** shorting into a rising 200-day with RSI at 43.6 and a squeeze at the lower band is a counter-structure trade on the long horizon. Keep it tactical and small.

**For an existing holder:**
- The 50-day break is a **trim signal, not an exit signal**. The 200-day is 4.8% below and rising.
- A defensible rule: hold the core while close > 239.6; reduce incrementally on each close below 249.6; add back on a close above 259.4.
- Position sizing in this regime: with ATR at 2.49%, a 2-ATR stop is ~5% of capital per share. For a 1% account risk budget, size no more than ~20% of equity notional in a single position (1% / 5%), and cut that further if an earnings event is inside the horizon.

---

## 11. What would change the view (monitoring triggers)

**Bullish repair (would flip the near-term bias):**
1. Close above **254.95** → the 50-day test is passed.
2. Close above **259.38** on volume > 40M → squeeze resolves up, VWMA reclaimed.
3. MACD histogram makes a **higher low** while price makes a lower low → genuine bullish divergence (currently absent).
4. Price reclaims VWMA (258.16) → volume-weighted buyers back in control.

**Bearish confirmation (would extend the down-leg):**
1. Close below **249.58** with volume > 35M → leg extension.
2. Close below **251.28** (lower band) with bandwidth *expanding* → squeeze resolves down.
3. MACD line accelerates below −1.5 with histogram < −2.0 → momentum capitulation, not exhaustion.
4. Any rally that stalls between 254.95 and 259.38 on *declining* volume → confirms the resistance wall as supply.

**Neutral/no-trade:**
- Continued closes between 249.6 and 254.9 on sub-30M volume. That is exactly today's condition — the squeeze unresolved. The correct action is no action beyond defined risk.

---

## 12. Limitations

- This is a **price/volume-only** analysis. No fundamental, earnings-date, news, options-implied-volatility or positioning data is in the toolset, so I cannot date the next catalyst or verify why the 2026-07-31 and 2026-02-06 gaps occurred beyond their price/volume signature.
- All support/resistance levels above are **observed clusters** in the verified data (moving averages, Fib arithmetic, prior highs/lows, gap edges). They are **not** validated bounce points; no claim of historical hold rates is made.
- Indicator values are as of the 2026-09-10 close; several (50-day slope, bandwidth) change materially session to session.
- Percentage moves are computed from the tool-supplied closes and are exact to the quoted dates, but no claim is made about intraday sequencing beyond the OHLC rows shown.

---

## 13. Summary table

| Category | Indicator / Level | Value (2026-09-10) | Reading | Interpretation |
|---|---|---|---|---|
| **Long-term trend** | `close_200_sma` | **239.62** (rising) | Bullish | +5.1% above; higher-low sequence 196.00→199.14→226.16 intact |
| **Medium-term trend** | `close_50_sma` | **254.95** (rising) | **Bearish break** | Closed below on 09-09 and 09-10 — first since 07-30 |
| **Trend alignment** | 50 − 200 spread | **+15.33 (+6.4%)** | Bullish | Golden-cross configuration still valid |
| **Short-term trend** | `vwma` | **258.16** (falling) | Bearish | Price 2.43% below volume-weighted cost; overhead supply |
| **Momentum — level** | `macd` | **−0.879** | Bearish | Crossed below zero 09-09, first since 07-30 |
| **Momentum — signal** | `macds` | **+0.550** | Bearish | MACD below signal for 18 sessions (cross 08-17) |
| **Momentum — thrust** | `macdh` | **−1.429** | **Re-accelerating** | Widened from −1.120 (09-08); no exhaustion |
| **Momentum — oscillator** | `rsi` | **43.62** | Neutral-bearish | Lowest since 07-29; **13.6 pts above oversold**; no divergence |
| **Volatility — position** | Bollinger (UB / mid / LB) | **267.48 / 259.38 / 251.28** | Bearish pin | Close 251.89 = **%B 3.8%**; intraday low 249.58 undercut band, closed back above |
| **Volatility — regime** | Bandwidth | **6.25%** (vs 29.68% on 08-10) | **Extreme squeeze** | −79% compression — expansion pending, direction unresolved |
| **Volatility — risk unit** | `atr` | **6.26** (2.49% of price) | Contracting | −37% from 08-03; 2×ATR stop = 239.4 = 200-SMA confluence |
| **Swing structure** | Highs / lows | 287.20 → 267.56; 257.73 → 249.58 | Bearish | Three lower highs, one lower low since 08-03 |
| **Key resistance wall** | 254.95 – 259.38 | 50-SMA, 61.8% Fib, 10-EMA, VWMA, 20-SMA | Critical pivot | Four independent measures within 4.4 pts |
| **Key support** | 249.58 / 246.56 / **239.6–241.0** | Leg low / 78.6% Fib / 200-SMA + gap floor | Downside objectives | Gap 51% filled; 100% fill ≈ 239.8 = 200-SMA |
| **Verdict** | — | — | **Short-term bearish, long-term bullish, volatility squeezed** | Tactical shorts/hedges favored; core longs hold above 239.6; require a close >259.4 to turn constructive |