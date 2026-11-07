# AAPL — Technical Analysis Report
**As of the close of 2026-09-22 | Price: $339.75**

---

## 1. Data Integrity Check (completed first)

The raw OHLCV series (`get_stock_data`, 2026-02-20 → 2026-09-22, 148 sessions) and the `get_verified_market_snapshot` agree exactly on the latest session and on every indicator value I cite (e.g., 50-SMA = 321.064199 in both sources; close = 339.75 in both). **No discrepancy to flag.** All price levels, band values and indicator readings below are taken from, or directly computed from, those two verified sources.

**Latest session (2026-09-22):** Open 340.14 | High 345.34 | Low 338.75 | Close 339.75 | Volume 40.71M

---

## 2. Why These 8 Indicators

| Selected | Role in this specific setup |
|---|---|
| `close_200_sma` | Defines the primary regime. Price is 18.4% above it — establishes we are trading *with* a powerful long-term uptrend, not against it. |
| `close_50_sma` | The medium-term trend spine and the level that separates a "healthy pause" from a "trend break." |
| `close_10_ema` | Captures the short-term impulse and gives a tight, actionable trailing reference for the current leg. |
| `macd` | Detects the August momentum trough and the September re-acceleration; also enables a like-for-like comparison with the July peak. |
| `rsi` | Flags whether this push toward the old high is overbought or has fuel left; also used for divergence work. |
| `boll_ub` | The immediate "overhead magnet/resistance" in a trend-expansion phase; today's high actually pierced it. |
| `atr` | Converts all the above into position size and stop distance (a volatility regime check as well). |
| `vwma` | Confirms whether the rally is being paid for by volume, or is a thin drift. |

Deliberately excluded: `macds`/`macdh` (the snapshot supplies signal 4.703771 and histogram 1.544044, so the MACD family is covered without a redundant call), `boll` middle and `boll_lb` (available in the verified snapshot: 325.592 / 306.897), and `mfi` (0.7372 in the snapshot — noted qualitatively, but highly correlated with RSI here).

---

## 3. The Big Picture: A Full Round-Trip Recovery Inside an Uptrend

The 148-session window tells a clean three-act story, all supported by the data:

1. **Advance (Feb → late July):** AAPL climbed from a 264.58 close (2026-02-20) to a 340.08 close (2026-07-28) — the highest close in the entire dataset. The technical total return index rose from 268.80 to 345.79 over the period (**+28.6%**).
2. **Distribution (2026-07-31):** A violent gap lower — close 333.43 → **308.91, −7.36% on 132.5M shares**, the single largest volume print in the dataset. Follow-through took price to a 302.25 close on 2026-08-12, a **−11.12% drawdown from the 340.08 peak**.
3. **Re-accumulation and recovery (Aug 13 → Sep 22):** **+12.41%** off the 302.25 low, in 28 sessions, with price now back within **0.10%** of the July closing high.

**The key structural fact:** despite the July collapse, the 200-SMA never rolled over. It has risen monotonically from 269.03 (2026-06-24) to **286.88**, and it is still rising ~0.28 points per session. That is the signature of a correction inside an intact primary uptrend, not a trend reversal. The 50-SMA (321.06) sits **34.18 points above** the 200-SMA — a wide, widening bullish separation.

---

## 4. Trend Layers — Alignment Is Bullish but Stretched

| Layer | Value | Price vs. level | Read |
|---|---|---|---|
| 10-EMA | 333.05 | **+2.01%** | Short-term trend up, price above |
| VWMA | 328.85 | **+3.31%** | Volume-weighted holders in profit |
| 50-SMA | 321.06 | **+5.82%** | Medium-term trend up |
| Bollinger mid (20-SMA) | 325.59 | **+4.35%** | Price in upper half of band |
| 200-SMA | 286.88 | **+18.43%** | Long-term trend strongly up |

**Interpretation:** Perfect bullish stacking (price > 10-EMA > VWMA > 50-SMA > 200-SMA). But the *distance* between price and each average is the risk. The 10-EMA has risen in an almost unbroken line from 308.76 (2026-08-17) to 333.05, and price is now 6.70 above it. A routine mean-reversion to the 10-EMA is −2.0%; to the VWMA is −3.2%; to the 50-SMA is −5.5%. **The reward in front of price (0.1% to the July high) is smaller than the routine pullback risk behind it (2–5.5%).** That asymmetry is the central tactical problem in this chart.

---

## 5. Momentum — Strong, Re-Accelerating, but Diverging at the High

**MACD (verified: 6.247814 | signal 4.703771 | histogram 1.544044)**

- MACD bottomed at **−2.676** on 2026-08-17 and has risen for **25 consecutive sessions**.
- It crossed zero on **2026-08-31** (−0.028 → +0.297), converting the tape from bear to bull momentum.
- The histogram is positive, but at **1.54 against a 6.25 MACD line**, the signal line is still catching up. This reads as a *young, steady trend leg* rather than a blow-off acceleration — the kind of profile that typically persists rather than snaps, but also one that offers little cushion if price stalls.

**The critical divergence:** On 2026-07-28, AAPL closed at **340.08** with MACD at **9.454**. Today it closes at **339.75** — essentially the same price — with MACD at **6.248**. The market has traveled the entire correction and recovery to arrive at the same price with **roughly one-third less upside momentum**. The same is true of RSI: **68.90** on 2026-07-28 vs. **66.88** today. This is a genuine, tool-verified momentum divergence at resistance, and it argues that a clean breakout needs *new* fuel (volume) rather than simply more of the same grind.

**RSI (66.878154)**

- Up from 43.24 (2026-08-17) to 66.88 — a powerful but orderly re-rating.
- **Not overbought** (below 70), so there is headroom, but only ~3 points of it before the zone that capped the July advance.
- RSI has not been above 70 at any point in the supplied data. That makes 70 a meaningful, untested ceiling rather than a routine level.
- Snapshot MFI = **0.7372** corroborates strong (but not extreme, <0.80) money flow.

---

## 6. Volatility & Bollinger Structure — Squeeze → Expansion, and an Upper-Band Rejection

- **Bollinger upper band: 344.29** | middle **325.59** | lower **306.90** (snapshot). Bandwidth = **37.39 points, 11.48% of the middle band** — a wide, expanding envelope.
- The upper band collapsed from **347.26 (2026-08-12)** to **317.04 (2026-08-27)** during the basing phase, then expanded to **344.29**. That contraction-then-expansion sequence is the classic resolution of a volatility squeeze, and it resolved **upward**.
- **Today's session is the tell:** the high of **345.34** actually traded **1.05 above** the upper band (344.29), then closed back at **339.75** — i.e., price tagged the extreme of the band and was rejected. The close sits in the **bottom 15%** of the day's 6.59-point range (high 345.34, low 338.75) and slightly below the 340.14 open.
- **ATR: 7.21 (2.12% of price).** Down from 9.87 on 2026-07-31 — volatility has normalized even as price advanced, which is characteristic of a controlled, orderly uptrend rather than a speculative one.

**Combined read:** a new intraday high (345.34 vs. the prior 344.57 on 2026-07-29), rejected at the upper band, on a weak close. That is not a breakdown — the close was still +0.77 on the day — but it is not breakout confirmation either.

---

## 7. Volume — The Missing Ingredient for a Breakout

- Today's **40.71M** shares is **below** the rough 20-session average of ~43M.
- For context, the recent volume signatures were: **86.59M on 2026-09-18** (price fell only 0.87 — heavy volume *absorbed* with no downside follow-through, a bullish tell), **70.01M on 2026-09-10** and **65.64M on 2026-09-09** (the launch of this leg), **132.49M on 2026-07-31** (the distribution event).
- The VWMA at **328.85** is rising and sits 10.90 below price, confirming that volume-weighted buying has been in control since late August. But note that the VWMA is **4.20 points below the 10-EMA** — the volume-weighted average is lagging the price average, meaning recent gains have come on *thinner* volume than the advance earlier in the leg.

**Verdict on volume:** the trend is volume-confirmed in aggregate, but **this specific push through 340 is not**. A breakout on ~41M shares is a much lower-quality signal than one on 60M+.

---

## 8. Key Levels (all derived from verified tool output)

**Resistance**
- **340.08** — 2026-07-28 closing high. The line in the sand; today closed 0.33 below it.
- **342.89 / 344.57** — 2026-07-28 and 2026-07-29 intraday highs.
- **344.29** — Bollinger upper band.
- **345.34** — today's high (new intraday high for the dataset).
- **~350–352** — measured-move objective: the 2026-09-01→09-09 base spanned 309.90–330.81 (20.91 points); projected from a 330.81 breakout gives ~351.7.

**Support**
- **338.75** — today's low (immediate).
- **333.05** — 10-EMA (first line of defense).
- **328.85** — VWMA (the "average buyer's cost").
- **325.59** — Bollinger middle / 20-SMA.
- **321.06** — 50-SMA (the medium-term regime line).
- **314.90 / 309.90** — 2026-09-08 and 2026-09-09 lows.
- **306.90** — Bollinger lower band; **300.57 / 300.00** — 2026-08-12 low and 2026-07-31 low.

---

## 9. Actionable Plans

**The setup in one sentence:** a high-quality, volume-confirmed uptrend that has recovered 100% of a −11.1% correction and is now pressing a double-top zone with fading momentum and a rejected upper-band tag — so *own the trend, but demand confirmation before adding at resistance.*

**Plan A — Breakout confirmation (preferred for new longs)**
- **Trigger:** a daily **close above 340.10**, ideally above **342.90**, with volume **≥ 55M** (i.e., at least ~25% above today's 40.7M).
- **Entry:** 340.20–343.00 on the confirming close.
- **Stop:** **333.00** (below the 10-EMA) — ~7.2 points ≈ **1.0 ATR**, roughly 2.1% risk.
- **Targets:** 344.29 (upper band) → 345.34 → **351.70** (measured move).
- **Skip it if** price clears 340 intraday but closes back below 338.75 — a second upper-band rejection.

**Plan B — Pullback accumulation (better risk/reward)**
- **Zone:** **333.05 (10-EMA) to 328.85 (VWMA)**. Both are rising, and a tag of this zone would reset RSI from 66.9 toward the mid-50s without breaking structure.
- **Entry:** scale in across 333.00 / 330.50 / 328.90.
- **Stop:** **320.50**, just under the 50-SMA — ~11 points, ~3.3% risk.
- **Targets:** 340.08, then 344.29.

**Plan C — Invalidation / risk-off**
- A **close below 333.05** breaks the short-term impulse — reduce tactical exposure.
- A **close below 328.85** puts the volume-weighted buyer base underwater — the September leg is compromised.
- A **close below 321.06 (50-SMA)** breaks the medium-term trend and opens 314.90, then 309.90. With the 200-SMA at 286.88, even that would be a correction, not a bear market — but it would invalidate the current long thesis for weeks.

**Position sizing (ATR-based)**
With ATR = **7.21**, a 1.5×ATR stop is **10.81 points**. On a $100,000 account risking 1% ($1,000), that is ~92 shares (~$31,400 notional, ~31% of equity). On the tighter Plan A stop (7.2 points) the same $1,000 risk supports ~139 shares (~$47,200 notional). Keep total exposure modest: price is 5.8% above the 50-SMA and 18.4% above the 200-SMA, both historically stretched positions that raise gap risk.

**What would upgrade the thesis to "buy aggressively":** a close above 345.34 on 60M+ shares with RSI pushing through 70 and MACD extending past 7.0. **What would downgrade it:** a second failed tag of 344–345, or MACD histogram flipping negative while price stays pinned under 340.

---

## 10. Summary Table

| Dimension | Indicator | Value (2026-09-22) | Signal | Evidence / Nuance |
|---|---|---|---|---|
| **Primary trend** | `close_200_sma` | 286.88 | **Strong bull** | Price +18.43% above; 200-SMA rising ~0.28/session since 2026-06-24 (269.03) |
| **Medium trend** | `close_50_sma` | 321.06 | **Bull** | 34.18 above the 200-SMA; up 25 straight sessions from 309.08 (2026-08-17) |
| **Short trend** | `close_10_ema` | 333.05 | **Bull, extended** | Price +2.01% above — routine pullback risk to this level |
| **Momentum** | `macd` | 6.248 (sig 4.704, hist +1.544) | **Bull** | Rose 25 sessions from −2.676; zero-cross 2026-08-31 |
| **Momentum divergence** | `macd` vs. price | 6.25 now vs. **9.45** at the 340.08 close (2026-07-28) | **Caution** | Same price, ~33% less momentum — verified divergence |
| **Momentum** | `rsi` | 66.88 | **Bull, near threshold** | Up from 43.24 (2026-08-17); never exceeded 70 in the dataset; July peak 68.90 |
| **Volatility/overhead** | `boll_ub` | 344.29 | **Resistance** | Today's 345.34 high pierced it, closed back below — rejection |
| **Volatility regime** | `atr` | 7.21 (2.12%) | **Orderly** | Down from 9.87 (2026-07-31); 1.5×ATR stop = 10.81 |
| **Volume confirmation** | `vwma` | 328.85 | **Bull, lagging** | Price +3.31% above, but VWMA sits 4.20 *below* the 10-EMA → recent gains on thinner volume |
| **Participation today** | Volume | 40.71M | **Insufficient** | Below ~43M 20-session average; vs. 70.0M (09-10), 86.6M (09-18) |
| **Candle quality** | OHLC | 340.14 / 345.34 / 338.75 / 339.75 | **Weak at highs** | Closed in bottom 15% of range after a new intraday high |
| **Key resistance** | Price levels | 340.08 → 342.89 → 344.57 → 345.34 | **Double-top test** | Close 0.33 below the July closing high |
| **Key support** | Price levels / MAs | 338.75 → 333.05 → 328.85 → 321.06 | **Layered** | 10-EMA, VWMA, then 50-SMA |
| **Stretch risk** | Price vs. 50-SMA | +5.82% | **Extended** | Mean reversion to 50-SMA ≈ −5.5% |
| **Bottom line** | Composite | — | **Bullish trend / neutral entry** | Own it, don't chase it: require a >340.10 close on ≥55M shares, or buy the 333.05–328.85 pullback; invalidate below 333.05 |