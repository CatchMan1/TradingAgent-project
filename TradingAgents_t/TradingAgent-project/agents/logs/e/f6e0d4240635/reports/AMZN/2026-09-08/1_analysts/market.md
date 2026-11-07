# AMZN — Multi-Timeframe Technical Review (as of close, 2026‑09‑08)

## 1. Data integrity check
The `get_verified_market_snapshot` (2026‑09‑08) and the `get_stock_data` CSV agree exactly on the latest row, so there is **no conflicting print to reconcile**:

| Field | 2026‑09‑08 |
|---|---|
| Open | 256.68 |
| High | 257.99 |
| Low | 254.75 |
| Close | **256.97** |
| Volume | 29,398,000 |
| Prior close (09‑04) | 258.51 → **−1.54 / −0.60%** |

Caveat: 2026‑06‑26 shows 248,372,100 shares vs ~25–50M typical — an obvious index/event anomaly. I do **not** use it in any volume average or conclusion. I have no news/fundamental feed, so catalyst references below are inferred from price/volume behaviour only, and are labeled as such.

---

## 2. The big picture: an uptrend that is digesting a violent repricing

The 2026 path in the data is a V‑shaped recovery, a long churn, then a step-change:

- **Feb capitulation:** 245.63 intraday high (02‑02) → **196.00 low (02‑17)**, a −20% collapse over 11 sessions on heavy volume (179.2M on 02‑06).
- **Recovery / base-building:** a grinding 4‑month climb from ~199 to ~275 by early May, with repeated failures in the **263–275** zone (263.99 on 04‑24, 274.99 on 05‑06, 272.05 on 05‑04).
- **Summer decay:** a lower-high sequence into **225.55 low (06‑25)** — a full round-trip give-back to the February/March area.
- **The step-change:** 07‑29 close 226.65 → 07‑30 close 235.50 (101.8M shares) → **07‑31 gap up: prior close 235.50, open 265.00, close 271.58 (129.1M shares)** → **08‑03 intraday high 287.20, close 284.02 (90.8M shares)**.

That 07‑30 to 08‑03 volume signature — 101.8M / 129.1M / 90.8M against a ~32M 20‑day norm — is consistent with a **news/fundamental repricing**, not ordinary flow. It is the single most important structural feature on the chart, because it left a **29.50‑point unfilled gap (235.50 → 265.00)** beneath the market.

Since 08‑03, the stock has been in a **controlled, declining-channel distribution**:

| Date | High | Close |
|---|---|---|
| 08‑03 | **287.20** | 284.02 |
| 08‑05 | 282.79 | 272.65 |
| 08‑10 | 280.14 | 278.09 |
| 08‑11 | 278.84 | 272.27 |
| 08‑13 | 269.58 | 265.13 |
| 08‑19 | 266.40 | 265.84 |
| 08‑28 | 267.56 | 266.43 |
| 08‑31 | 264.36 | 259.77 |
| 09‑04 | 261.12 | 258.51 |
| 09‑08 | 257.99 | **256.97** |

Lower highs are unbroken. From the 08‑03 close of 284.02 to 256.97 is **−27.05 points (−9.52%) over 24 sessions** — a textbook orderly counter-trend decline, not a crash.

**The retracement quality matters:** the 09‑01 low of **251.93** has retraced from 265.00 down to 251.93, i.e. **13.07 of the 29.50‑point gap (44%)**. The gap is *partially* filled; **235.50–251.93 remains unfilled**. That is the structural downside magnet if 251.93 gives way.

Notably, **08‑28 was a bull trap**: a wide-range close at 266.43 on 49.5M shares (highest volume since 08‑05), immediately reversed on 08‑31 to 259.77 on 46.1M. Supply is proven at 266–268.

---

## 3. Indicator-by-indicator

### Trend structure — `close_50_sma` = 254.435 and `close_200_sma` = 239.295
- **50 SMA has risen every single session** in the visible window: 246.384 (07‑30) → 254.435 (09‑08), +8.05 points (+3.3%).
- **200 SMA has also risen monotonically**: 234.755 (07‑30) → 239.295 (09‑08).
- 50 SMA is **15.14 points (6.3%) above** the 200 SMA, and both are sloping up. The **golden-cross structure is intact and widening** — the strategic trend is still bullish.
- But price at 256.97 sits only **+2.54 points (+1.0%) above the 50 SMA**. That is a thin cushion. The last time the 50 SMA was this close to being tested was the 07‑23 to 07‑29 breakdown (price 226.65 vs 50 SMA 246.38 — far *below* it, and it recovered via the gap).
- So: **primary trend up, intermediate trend down, and the two are about to collide at 254.4.** That is the decision point.

### Short-term momentum — `close_10_ema` = 258.743
- Price is **1.77 points (0.69%) below** the 10 EMA, which is itself rolling over (267.18 peak on 08‑12 → 258.74).
- AMZN has closed **below the 10 EMA in 16 of the last 18 sessions** (the only exceptions: 08‑19 and 08‑28). This is a persistent, not random, short-term downtrend.
- The 10 EMA (258.74) is converging on the rising 50 SMA (254.43) from above. If the 10 EMA crosses below the 50 SMA, that is the classic confirmation that the correction has become the trend rather than a pause.

### Momentum rollover — `macd` = 0.118, `macds` = 1.239, `macdh` = −1.120
This is the cleanest bearish signal on the board, and also the most "late":
- MACD peaked at **8.432 on 08‑11** and has decayed for 19 straight sessions to **0.118** — a 98.6% erosion.
- The **signal cross fired on 08‑17** (histogram −0.310) and the histogram bottomed at **−1.683 on 08‑27** before improving slightly to **−1.120**. So downside momentum is decelerating, but has not turned.
- The MACD line at 0.118 is **one or two sessions from crossing the zero line**. Historically that confirms an established downtrend — but with price already −9.5% off the high and RSI at 48, the zero-line cross is a *late* signal and a poor standalone short trigger.
- **Practical read:** bearish momentum is intact but exhausting. Watch the histogram: two consecutive sessions narrowing (−1.354 → −1.179 → −1.120) is the early tell for a squeeze resolution *upward*.

### Momentum level — `rsi` = 48.121
- Dead-center neutral. Peak was **72.23 on 08‑03** (overbought at the blow-off top), and RSI has stair-stepped down: 65.87 (08‑10) → 55.64 (08‑19) → 55.85 (08‑28) → 49.90 (09‑03) → **48.12**.
- Critically, **there is no bullish divergence**: the 09‑01 price low (251.93) came with RSI 46.33, versus the 08‑27 low (255.02) at RSI 47.23 — RSI was *lower* with the lower price, confirming rather than contradicting the decline.
- RSI at 48 means there is **neither oversold support nor overbought resistance** — the indicator offers no edge right now, which itself argues for waiting for a range break rather than anticipating one.

### Volatility compression — `boll` = 261.141, `boll_ub` = 270.007, `boll_lb` = 252.275
- **Bandwidth = 17.732 / 261.141 = 6.79%.** On 08‑18 it was **77.185 / 257.681 = 29.95%**. That is a **~77% contraction in 15 sessions** — an extreme squeeze, and the single most actionable observation in this report.
- **%B = (256.97 − 252.275) / 17.732 = 0.265** — price sits in the lower quartile of the envelope, hugging but not piercing the lower band.
- The **middle band is falling fast**: 267.142 (08‑27) → 261.141 (09‑08), roughly −0.9/session. If price simply holds flat, the upper resistance line *comes down to meet it* within days — meaning a close above ~261 becomes progressively easier without any real buying.
- Bands are contracting around a **flat 20‑day price distribution**, exactly the setup that precedes an expansion move. Direction is unresolved; timing is not.

### Volatility budget — `atr` = 6.483
- ATR has collapsed from **9.948 (08‑03) to 6.483 (−34.8%)**. Daily ATR is **2.52% of price**.
- This is the number that sizes everything: `1×ATR = 6.48`, `1.5×ATR = 9.72`, `2×ATR = 12.97`.
- Contracting ATR *plus* contracting Bollinger bandwidth is a double confirmation of a coiled market. It also means **stops placed on ATR logic will be unusually tight in absolute terms, and unusually likely to be swept** — favor closes over intraday wicks for stop placement.

### Volume-weighted positioning — `vwma` = 259.567
- Price (256.97) is **2.60 points (1.0%) below** the VWMA, and the VWMA has been **falling since 08‑20 (272.05)**.
- Interpretation: the average *volume-weighted* cost of recent holders is **above spot**. Recent buyers are collectively underwater, which creates **overhead supply on any rally into 259–260** — precisely where the 10 EMA (258.74) and the falling Bollinger mid (261.14) also sit.
- This is why the 08‑28 spike to 267.56 failed: it ran straight into the volume-weighted cost basis and got sold.
- Crucially, this is *not* a capitulation profile: no high-volume down day has reset the VWMA lower. It is drift, not dumping.

---

## 4. Composite read: a textbook coiling triangle at a trend decision

Everything points to one setup. The market has compressed into a **narrow ~10‑point decision box**:

**Support cluster — 251.9 to 254.4**
- Bollinger lower band: **252.275**
- 09‑01 swing low: **251.93**
- 50‑day SMA: **254.435** (rising, +1.0% below price)

**Resistance cluster — 258.7 to 261.1**
- 10‑day EMA: **258.743**
- VWMA: **259.567** (declining, volume-weighted overhead supply)
- Bollinger middle band: **261.141** (falling toward price)

**Price 256.97 sits almost exactly in the middle of the two.**

Supporting the *bullish* resolution:
- 50 SMA above 200 SMA, both rising (+6.3% spread).
- Price above both the 50 and 200 SMA.
- MACD histogram improving three sessions running.
- Volume in the pullback (~32.4M 20‑day average vs 49.5M/46.1M on the 08‑28/08‑31 reversal days) is *not* accelerating on the downside — this is a drift, not distribution.
- The 09‑01 to 09‑08 sequence produced **higher lows** (251.93 → 253.40 → 256.00 → 255.29 → 254.75) while price held above the lower band.

Supporting the *bearish* resolution:
- 16 of 18 closes below the 10 EMA; unbroken lower-high sequence since 08‑03.
- MACD line about to cross zero; the cross itself is bearish.
- Price below the VWMA, i.e. overhead supply at 259–260.
- 08‑28 bull trap at 267.56 proves sellers are active on strength.
- **44% of the 07‑31 gap is already filled**, and unfilled gap space (235.50–251.93) is a genuine downside target if support breaks.

**My net assessment: neutral-to-constructive, with a bias to resolution *higher* only on a confirmed reclaim of 261.** The dominant trend (50/200) is up and the pullback is orderly; but the short-term structure (10 EMA, VWMA, MACD) is down. This is a **wait-for-the-break market, not a predict-the-break market** — the squeeze guarantees a move but not its direction, and ATR at 6.48 gives a cheap, well-defined risk box on either side.

---

## 5. Actionable plan

**Base case (highest probability): continued chop in the 252–262 box** for a few more sessions while the Bollinger mid decays. Trading the middle of a squeeze is negative expectancy; stand aside or reduce size.

**Bullish trigger — two-stage confirmation:**
1. *First* close above **259.57 (VWMA)** and then a close above **261.14 (Bollinger mid)**. Route confirmation: volume > **42M** (≈1.3× the ~32.4M 20‑day average).
2. Targets: **266.40–267.56** (08‑19 high / 08‑28 failed-high supply), then **270.01 (upper band) → 272.05–274.99** (04‑24 to 05‑06 congestion).
3. Invalidation: a close back below **254.43**.
4. Risk from 261.5 entry to 254.4 stop = 7.1 points ≈ **1.1×ATR** — acceptable but tight; a close-basis stop below 253.5 gives 8.0 points and is cleaner.

**Bearish trigger:**
1. A **close below 251.93** (the 09‑01 low, which is also just under the 252.28 lower band) on volume > **42M**.
2. Targets: **245–246** (the 07‑06 to 07‑20 congestion at 244–250), then **240.14** (06‑29 close) and ultimately the **235.50 gap floor**.
3. Invalidation: a reclaim of **258.74 (10 EMA)**.
4. Risk from 251.5 entry to 258.8 stop = 7.3 points ≈ **1.1×ATR**.

**Risk management specifics:**
- **Position size on ATR, not dollars:** a 1% account risk with a 6.5‑point stop implies roughly 1.5× the share count you would use with an ATR of 10 (August levels). Volatility contraction mechanically permits larger size — but the sweep risk from a squeeze argues for sizing *down*, not up, until the break is confirmed.
- **Use closing prices for stops.** With ATR 6.48 and a 17.7‑point total band width, intraday wicks (e.g. 09‑08's 254.75 low vs 256.97 close) will tag obvious stop levels without confirming direction.
- **Do not average into the middle of the range.** 256.97 is the least informative price on the chart.
- **Event risk is unhedged in this analysis** — the 07‑30/07‑31 volume signature implies a catalyst-driven regime where the next fundamental print can gap the stock through any technical level, including the 29.5‑point gap zone.

**What would change my view:**
- **Bearish flip:** 50 SMA rolls flat/turns down (currently +0.5/day, watch for the slope to stall near 255), or a close below 251.93 that takes the VWMA decisively to new lows.
- **Bullish flip:** MACD histogram turns positive (MACD line crossing back above 1.24 signal), price closes two consecutive sessions above 261.14, and 10 EMA turns up through the VWMA.
- **Neither:** bandwidth stays under 7% and ATR under 6.5 — then the squeeze simply extends and the correct action is smaller size and tighter patience.

---

## 6. Indicator selection rationale (why these 8)

| Indicator | Value (09‑08) | Why it is the right tool here |
|---|---|---|
| `close_50_sma` | 254.435 | Price is only 1.0% above it and it is rising — the exact line that defines whether this is a pause or a breakdown |
| `close_200_sma` | 239.295 | Confirms the strategic uptrend is intact; 50>200 and both rising rules out a primary bear regime |
| `close_10_ema` | 258.743 | Captures the short-term downtrend (16 of 18 closes below) and is the first overhead gate |
| `macd`/`macds`/`macdh` | 0.118 / 1.239 / −1.120 | Only indicator showing the *rate of change* of the rollover, and the histogram is the earliest squeeze-resolution tell |
| `rsi` | 48.121 | Confirms no divergence at the 09‑01 low → the decline is real, not an oversold setup |
| `boll`/`boll_ub`/`boll_lb` | 261.141 / 270.007 / 252.275 | 77% bandwidth compression is the core thesis: a high-probability expansion event with defined edges |
| `atr` | 6.483 | Converts every level into a risk unit (2.52% daily); stops and sizing are impossible without it |
| `vwma` | 259.567 | Adds the volume dimension that price-only averages miss — explains *why* 266–268 failed |

Deliberately excluded: `mfi` (redundant with VWMA for the volume read here), any stochastic (redundant with RSI), and the sub-band variants already covered inside the Bollinger family. Eight families, minimal overlap: trend (3 horizons), momentum (2 forms), volatility (2 forms), and volume-weighted positioning (1).

---

## 7. Summary table

| Dimension | Reading | Evidence | Implication |
|---|---|---|---|
| **Primary trend** | Bullish | 50 SMA 254.44 > 200 SMA 239.29; both rising every session in window; spread +6.3% | Do not treat this as a bear market; rallies have structural backing |
| **Intermediate trend** | Down / corrective | 08‑03 close 284.02 → 09‑08 close 256.97 = −9.52%; unbroken lower highs 287.20 → 257.99 | Counter-trend within an uptrend; respect the channel until broken |
| **Short-term trend** | Weak | Close below 10 EMA (258.74) in 16 of last 18 sessions | Rally attempts should be sold/scaled until 261 is reclaimed |
| **Momentum** | Rolling over | MACD 8.432 (08‑11) → 0.118; signal cross 08‑17; hist −1.120 but narrowing 3 sessions | Bearish but decelerating — late for new shorts, early for longs |
| **RSI** | Neutral | 48.12; peaked 72.23 (08‑03); no bullish divergence at 09‑01 low | No edge; confirms decline rather than signaling reversal |
| **Volatility** | Extreme compression | Bollinger bandwidth 29.95% (08‑18) → 6.79% (09‑08); ATR 9.95 → 6.48 (−34.8%) | Squeeze; expansion imminent; direction unconfirmed |
| **Position in bands** | Lower quartile | %B = 0.265; price 4.70 above lower band, 13.04 below upper | Downside room is limited without a band break |
| **Volume positioning** | Bearish tilt | Price 1.0% below VWMA 259.57; VWMA falling since 08‑20 | Overhead supply at 259–261; explains 08‑28 failure at 267.56 |
| **Volume behavior** | Benign drift | 20‑day avg ≈32.4M vs 29.4M latest; down days not expanding | No capitulation — supports eventual upside resolution |
| **Key support** | 251.93–254.44 | 09‑01 low 251.93; lower band 252.28; 50 SMA 254.44 | Break on >42M volume targets 245–246, then 240.14 |
| **Key resistance** | 258.74–261.14 | 10 EMA 258.74; VWMA 259.57; mid band 261.14 | Reclaim opens 266.4–267.6, then 270–275 |
| **Gap structure** | 44% filled | 07‑31 gap 235.50 → 265.00; 09‑01 low 251.93 | 235.50–251.93 remains the structural downside magnet |
| **Stance** | **Neutral / wait-for-break** | Mid-range (256.97) inside a 252–262 squeeze | Trade the break with volume confirmation; avoid the middle |
| **Risk unit** | 6.48 pts (2.52%) | ATR 6.48; 2×ATR = 12.97 | Size on ATR; use closing-basis stops to survive squeeze wicks |

**Bottom line on AMZN:** the stock is doing exactly what a healthy but exhausted post-catalyst advance does — digesting a 25% two-day gap on contracting volatility without giving back the gap floor. The trend of consequence (50 > 200 SMA, both rising) remains up, and the 50 SMA at 254.44 is still holding on a closing basis. But the tactical tape (10 EMA, VWMA, MACD) is negative, and price is pinned in the dead center of a 6.8%-wide Bollinger squeeze. The correct posture is **flat-to-small, with pre-committed triggers at 251.93 and 261.14** — the next 6.5 points of ATR will likely be decided in a single session, and the volume on that session (above ~42M) is the only reliable tiebreaker available.