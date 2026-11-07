# AAPL — Multi-Timeframe Technical Analysis
**Analysis date: 2026-09-18 (close) | Last verified price: $336.13**

---

## 1. Data Verification Note

Both the raw OHLCV pull (`get_stock_data`) and the `get_verified_market_snapshot` agree exactly on the 2026-09-18 row, and the indicator series match the snapshot values to the decimal. **No discrepancies to flag.** All price levels and indicator values below are sourced from the verified snapshot / indicator output.

| Field | 2026-09-18 value |
|---|---|
| Open / High / Low / Close | 337.91 / 338.49 / 332.53 / **336.13** |
| Day change (vs 337.00 prior close) | −0.87 (−0.26%) |
| Volume | 86,588,200 shares |
| 10 EMA | 329.92 |
| 50 SMA | 320.14 |
| 200 SMA | 286.34 |
| Bollinger mid / upper / lower | 322.64 / 341.01 / 304.27 |
| RSI(14) | 64.25 |
| MACD / Signal / Histogram | 5.517 / 3.915 / 1.603 |
| ATR(14) | 7.31 |
| VWMA | 326.37 |

---

## 2. Trend Structure: Bullish, and Re-Accelerating

**Long-term (200 SMA): intact and rising.** The 200 SMA has climbed monotonically through the entire visible window — 261.07 on 2026-05-21 to 286.34 on 2026-09-18. Price at 336.13 sits **+17.4% above** it. The 50 SMA (320.14) sits **11.8% above** the 200 SMA, i.e., a well-established golden-cross configuration with a widening spread. That spread is a "trend is strong" signal, but also the main mean-reversion risk if momentum stalls.

**Medium-term (50 SMA): flat pause, then re-slope.** The 50 SMA is the most informative line here:
- It rose steadily from 269.49 (2026-05-21) to 309.30 (2026-07-30).
- It then **flattened for roughly three weeks** (309.30 → 309.08 on 2026-08-17 → 309.78 on 2026-08-07), absorbing the 2026-07-31 gap-down.
- It has since resumed rising to 320.14, a slope of roughly **+0.50 points/session over the last 22 sessions** (~0.16%/day).

That "flat-then-resume" profile is the classic signature of a pause inside an uptrend rather than a trend reversal. Price is **+4.99% above the 50 SMA**, a moderate — not extreme — extension.

**Short-term (10 EMA): steep and clearly leading.** The 10 EMA has risen from 318.26 on 2026-09-09 to 329.92 on 2026-09-18 (+11.66 points in seven sessions), and price is **+1.88% above it**. The moving averages are in textbook bullish stack: **price (336.13) > 10 EMA (329.92) > 50 SMA (320.14) > 200 SMA (286.34)**.

**Trend repair evidence:** The 2026-07-31 session gapped from a 333.43 close (7/30) to a 304.81 open and closed at 308.91 (−7.35%, 132.5M shares), leaving a supply void between 310.69 and 333.43. That entire gap zone has now been **fully recovered**, with 9/18's 336.13 the highest close since 2026-07-29 (338.19) and the 338.49 intraday print the highest high since 2026-07-29's 344.57. Recovering a −7% gap in seven weeks is a materially bullish structural signal.

---

## 3. Momentum: Fresh Regime Shift, Not Yet Overbought

**MACD has completed a full reset-and-recross cycle.** The MACD line went negative on 2026-08-11 (−0.83), bottomed at −2.68 on 2026-08-17, recrossed above zero on 2026-08-31 (+0.30), and crossed above its signal line on 2026-09-01/09-02. It now reads **5.517 vs. a 3.915 signal**, a positive histogram of **+1.603**.

Nuance worth flagging: the histogram expanded to 1.625 on 2026-09-14, cooled to 1.538 on 2026-09-16, and is now 1.603 — i.e., **momentum is strongly positive but the rate of acceleration has flattened over the last four sessions** while price pressed into resistance. That is a "watch, don't chase" condition, not a sell signal. The absolute MACD level (5.52) remains well below the July peak (9.61 on 2026-07-29), leaving headroom.

**RSI at 64.25 — constructive but approaching a historically dangerous zone for this name.** RSI has built a sequence of higher lows since the August trough (40.2 on 2026-08-12 → 47.9 on 8/18 → 49.3 on 9/9 → 64.25 now). Critically, it is **not yet overbought**, and there is no bearish divergence: the 9/17–9/18 highs (338.34/338.49) came with RSI above the 9/11 reading (62.79 vs 64.25 at a higher high).

However, 2026's record in AAPL argues for treating RSI >70 as a genuine warning rather than a "ride the trend" signal:
- RSI 76–80 in late May 2026 (peaking 79.79 on 2026-05-28) preceded a slide from 315.20 (6/2) to 290.55 (6/9).
- RSI 71.4–71.6 on 2026-07-16/17 preceded a two-week chop and then the −7.35% break on 2026-07-31.
- RSI 68.90 on 2026-07-28 was the exact top tick before that break.

**Interpretation:** at 64.25 there is roughly one more "leg" of room before the historical caution zone, but the current setup — extended price, rising RSI, price at prior supply — is precisely the configuration that produced the July failure.

---

## 4. Volatility and Band Positioning

**Bollinger:** mid 322.64, upper 341.01, lower 304.27. Band width has **expanded sharply** (28.48 points on 2026-09-09 vs. 36.74 today), which validates the breakout rather than a squeeze. Price sits at **%B ≈ 0.87** — in the upper fifth of the band, above the mid-line by 4.18%, but with **4.88 points (1.45%) of room to the upper band at 341.01**.

The key observation: **the upper band (341.01) converges almost exactly with the July supply shelf** (closing high 340.08 on 2026-07-28; intraday high 344.57 on 2026-07-29). This is a rare double-confirmation of a resistance zone at **338–344**.

**ATR at 7.31 = 2.17% of price.** Volatility has actually **compressed** from the post-breakdown peak (9.87 on 2026-07-31) and the recent 8.05 (2026-09-11). Falling ATR into rising price is characteristic of an orderly, low-chaos advance — a healthy sign. But 2.17% daily range means normal noise can shake out tight stops.

**ATR-derived mechanics (arithmetic, not prediction):**
- 1× ATR stop from 336.13 → 328.82 (just under the 10 EMA)
- 1.5× ATR → 325.16 (basically the VWMA at 326.37)
- 2× ATR → 321.50 (essentially the 50 SMA at 320.14)

The alignment of 1.5×ATR with VWMA and 2×ATR with the 50 SMA is unusually clean and makes risk definition straightforward.

---

## 5. Volume and Participation

- **VWMA 326.37** vs. price 336.13 → price is **+2.99% above** the volume-weighted average. The VWMA has risen for ten straight sessions (309.19 on 2026-08-25 → 326.37). This confirms the advance is being made at *higher* prices on real volume — not a drift on thin tape.
- **2026-09-18 volume of 86.59M is ~2.1× the 19-session average of ~41.2M** (8/21–9/17). That is a genuine outlier.
- **Caveat that matters for interpretation:** 2026-09-18 is the third Friday of September, consistent with a quarterly derivatives-expiration session. Expiration-driven volume is mechanically inflated and **should not be read as directional confirmation**. Note also that despite the volume surge, 9/18 closed **down −0.26% and below its open**, with the 338.49 high rejected. That is ambiguous (absorption or distribution), and the next 2–3 sessions must resolve it.
- The prior high-volume days in the window were all **downside**: 2026-07-31 (−7.35%, 132.5M), 2026-06-25 (−6.12%, 107.0M), 2026-02-12 (−5.00%, 81.1M). This name has repeatedly produced **violent, high-volume gap-downs** in 2026. That asymmetry argues for pre-defined risk rather than reactive stops.
- The snapshot also carries an MFI reading of 0.6818 (≈68 on a 0–1 normalized scale, assuming that convention), which is consistent with positive but not yet extreme money flow — below the conventional 80 threshold.

---

## 6. Key Levels

**Resistance (in order):**
1. **338.49** — 9/18 intraday high (highest since 7/29)
2. **340.08** — 7/28 closing high; the pivot for a new high in the data set
3. **341.01** — Bollinger upper band (confluence)
4. **344.57** — 7/29 intraday high; the prior swing ceiling

**Support (in order):**
1. **332.53** — 9/18 low (immediate)
2. **329.92** — 10 EMA
3. **326.37** — VWMA
4. **322.64** — Bollinger mid
5. **320.14** — 50 SMA (with 322.6 mid-band, this forms a **320–323 confluence shelf** — the single most important line in the sand)
6. **315.3–316.2** — early-September consolidation (closes 9/8–9/9)
7. **304.27** — Bollinger lower band; **300–302** — August low closes (302.25 on 8/12; 300.00 intraday low on 7/31)

---

## 7. Actionable Framing

**Base case (bullish continuation, needs confirmation):** The trend, momentum, and volume-weighted structure all point higher. A **daily close above 338.49–340.08 on volume ≥ the ~41M recent average** confirms the breakout and opens a mechanical 1×ATR path toward **~347** (340 + 7.31) and 2×ATR toward **~355**. Because the breakout would clear the July ceiling, a failure there would be the second rejection at the same level — that pattern usually produces a deeper retest, so the breakout needs to *hold*, not merely print.

**Preferred entry discipline:** Chasing at 336 into a 338–344 resistance wall with RSI at 64 and a flat MACD histogram is poor risk/reward. Two better structures:
- **Buy the retest:** 329–330 (10 EMA) with a stop below 325 (VWMA/1.5 ATR); risk ≈ 4.5–5 points, reward to 344 ≈ 14 points → roughly 3:1.
- **Buy the breakout confirmation:** close >340.08, stop at 333 (−1 ATR back inside the range), target 351–355.

**Bear/consolidation case:** Rejection at 338–341 with a close **below the 10 EMA (329.92)** opens the 326.37 VWMA, then the 320–323 confluence. The bull thesis is only *structurally* impaired on a **daily close below the 50 SMA (320.14)** — at that point the medium-term trend has broken and 315 / 304 come into play.

**Position sizing:** With ATR at 7.31 (2.17%), a 1.5 ATR stop is ~11 points (~3.3%). Size positions so that a full stop costs no more than your normal per-trade risk budget; because of this name's demonstrated gap risk (four −3.6% to −7.4% single sessions in 2026), a stop-market can slip — consider defining risk with options or reducing nominal size rather than relying on a tight stop.

**What would change the stance:**
- **Bullish invalidation:** daily close <320.14 (50 SMA); or MACD crossing back below its signal line while price fails at 338.
- **Bullish confirmation:** close >340.08 on above-average volume, with MACD histogram making a new high (>1.63).
- **Warning flags:** RSI pushing above 70 *into* the 338–344 zone (repeat of the late-May and late-July setups); a new price high on declining volume; VWMA flattening while price rises (non-confirmation).

---

## 8. Indicator Selection Rationale (8 slots)

| Indicator | Why it earns a slot in this context |
|---|---|
| **close_10_ema** | The advance is fast and steep; the 10 EMA (329.92) is the operative trailing trigger and defines the first-line stop. |
| **close_50_sma** | Captured the crucial July–August flattening and September re-slope; the 320.14 level is the definitive medium-term invalidation. |
| **close_200_sma** | Confirms the structural uptrend and quantifies how extended the market is (+17.4%). |
| **macd** | Best measure of the August-to-September regime flip (negative → positive, zero-line recross 8/31). |
| **macds** (with macd) | The signal-line cross on 9/1–9/2 and the histogram's recent flattening are the cleanest read on whether momentum is still accelerating. |
| **rsi** | Essential here given 2026's documented pattern of RSI >70 preceding sharp drops; also confirms no bearish divergence at the 9/17–9/18 highs. |
| **boll_ub/boll_lb** (Bollinger) | The 341.01 upper band converging with the July supply zone is the strongest confluence in the chart; band width expansion validates the breakout. |
| **atr** | Converts every level into a risk distance (7.31 = 2.17%), enabling 1.5×ATR ≈ VWMA and 2×ATR ≈ 50 SMA stops. |
| **vwma** *(supplementary volume cross-check)* | Price +2.99% above a rising VWMA confirms the move is volume-backed; also flags that 9/18's 86.6M print is expiration-distorted rather than pure demand. |

---

## 9. Key Points Summary Table

| Category | Reading (2026-09-18) | Signal | What It Means / Trigger |
|---|---|---|---|
| **Price** | 336.13 (−0.26%) | Neutral day at resistance | Highest close since 7/29; 338.49 high rejected |
| **10 EMA** | 329.92 (price +1.88%) | **Bullish** | First support; close below opens 326 |
| **50 SMA** | 320.14 (price +4.99%) | **Bullish**, re-sloping | Flat 7/30–8/17 then resumed; hard invalidation |
| **200 SMA** | 286.34 (price +17.39%) | **Bullish/Extended** | Golden cross intact; 11.8% 50-vs-200 spread |
| **MACD** | 5.517 vs signal 3.915 | **Bullish** | Zero-line recross 8/31; histogram flat at ~1.60 |
| **RSI(14)** | 64.25 | **Constructive, caution nearing 70** | No divergence; >70 into 338–344 was a sell in May/July |
| **Bollinger** | Mid 322.64 / UB 341.01 / LB 304.27 | Upper half, %B ≈ 0.87 | UB 341.01 converges with July supply 340–344 |
| **ATR(14)** | 7.31 (2.17%) | Volatility compressing | 1.5×ATR → 325.2; 2×ATR → 321.5 |
| **VWMA** | 326.37 (price +2.99%) | **Bullish** | 10 straight sessions rising; volume confirms trend |
| **Volume** | 86.59M vs ~41.2M 19-day avg (~2.1×) | **Ambiguous** | Third-Friday expiration distortion; watch follow-through |
| **Resistance** | 338.49 → 340.08 → 341.01 → 344.57 | Pivot zone | Close >340.08 on volume = breakout confirmation |
| **Support** | 332.53 → 329.92 → 326.37 → 320–323 → 304–315 | Stacked | 320–323 (50 SMA + mid-band) is the key shelf |
| **Base case** | Uptrend intact, extended into supply | **Buy retests, don't chase** | 329–330 entry / stop <325 = ~3:1 to 344 |
| **Bear trigger** | Daily close **< 320.14 (50 SMA)** | Trend break | Targets 315, then 304–308 |
| **Bull trigger** | Daily close **> 340.08** on ≥ average volume | Breakout | 1×ATR path ~347; 2×ATR ~355 |
| **Risk note** | 4 single-session drops of −3.6% to −7.4% in 2026 | Gap risk elevated | Use ATR/options-defined risk, not tight stops |