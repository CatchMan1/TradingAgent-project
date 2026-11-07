# AMZN — Multi‑Timeframe Technical Report
**As of close, 2026‑09‑15 | Last price: $248.42**

All price, level, and indicator values below come from the verified snapshot for 2026‑09‑15 and the indicator series filtered to that date. The snapshot and the indicator tool outputs are internally consistent (50‑SMA 255.5554 / 200‑SMA 240.0278 / 10‑EMA 254.6540 / MACD −1.6208 / signal −0.3188 / histogram −1.3020 / RSI 41.4171 / Boll mid 257.8605 / upper 266.7926 / lower 248.9284 / ATR 6.2182 / VWMA 256.5143) — no discrepancy to flag.

---

## 1. Why these indicators were selected

AMZN is in a specific and diagnostically demanding setup: a large event‑driven gap in late July, a subsequent orderly 6‑week fade, and a sharp collapse in realized volatility. That combination needs four non‑overlapping lenses rather than eight correlated oscillators:

- **Trend structure across three horizons** — `close_10_ema` (tactical), `close_50_sma` (swing), `close_200_sma` (strategic), so we can tell whether this is a pullback in an uptrend or the start of a trend change.
- **Momentum/rate‑of‑change** — `macd` (with `macds` and `macdh` as the internal confirmation layers) to measure whether the downside impulse is accelerating or merely grinding.
- **Mean‑reversion + volatility regime** — `rsi` plus `boll`/`boll_ub`/`boll_lb` to locate where price sits inside its statistical envelope and whether the envelope is compressing or expanding. `atr` is included separately because band width and ATR answer different questions (dispersion vs. true range) and both are needed for stop placement.
- **Volume‑weighted participation** — `vwma` to test whether the price decline is being validated by where volume actually traded.

Deliberately excluded: redundant momentum oscillators (StochRSI, etc. would duplicate RSI), and a second volatility measure beyond ATR + bands.

---

## 2. Trend structure: bullish on the long horizon, bearish on every shorter one

**The strategic trend is still intact but the tactical trend has clearly rolled over.**

| Horizon | Measure | Value | Price vs. measure |
|---|---|---|---|
| Tactical (2 weeks) | 10‑EMA | **254.65** | −2.45% |
| Swing (10 weeks) | 50‑SMA | **255.56** | −2.79% |
| Strategic (40 weeks) | 200‑SMA | **240.03** | **+3.50%** |
| Volume‑weighted | VWMA | **256.51** | −3.16% |

- **200‑SMA at 240.03 is rising ~+0.12/day** (238.79 on 9/01 → 240.03 on 9/15). The 50‑SMA sits **15.5 points (6.5%) above** it, so the golden‑cross structure from the spring advance remains valid. The primary uptrend is *not* broken.
- **But the 50‑SMA has stopped rising with authority.** It advanced +2.29 points from 8/28 to 9/04 (+0.46/day), then only +1.61 points from 9/04 to 9/15 (+0.23/day). Slope has halved and is now decelerating toward flat — the classic signature of a trend that has lost its impulse.
- **The 10‑EMA has been in a monotonic decline from 267.16 (8/11) to 254.65 (9/15).** AMZN closed below the 10‑EMA in **10 of the last 11 sessions** (the lone exception being 9/11, at 256.78 vs. 256.59). That is persistent, not noisy, short‑term weakness.
- The 10‑EMA (254.65) < 50‑SMA (255.56) < VWMA (256.51) < Bollinger mid (257.86) forms a **tight, descending stack of overhead resistance between ~254.6 and ~257.9**. This is the defining technical feature of the current tape: every rally is being absorbed in a 3.3‑point band.

**Swing sequence is unambiguously lower highs and lower lows:**
- Highs: **284.02** (8/03 close) → **266.43** (8/28) → **258.90** (9/03) → **256.78** (9/11)
- Lows: **257.73** (8/18) → **251.93** (9/01) → **249.58** (9/10) → **247.22** (9/15)

---

## 3. Momentum: MACD has crossed into negative territory, but the impulse is grinding, not accelerating

- **MACD line: −1.621**, down from a cycle peak of **+8.43 on 8/11**. It crossed zero on **9/09** (−0.421) and has extended lower each session since.
- **Signal line: −0.319.** The MACD has been **below its signal continuously for 21 straight sessions** (first negative histogram print 8/17 at −0.310).
- **Histogram: −1.302.** Critically, the histogram has been trapped between roughly **−1.06 and −1.69 for the last month**:
  - 9/08 −1.120 → 9/09 −1.328 → 9/10 −1.429 → 9/11 −1.110 → 9/14 −1.061 → **9/15 −1.302**

**Interpretation (important nuance):** the MACD line is falling steadily, but the histogram is *not* making a fresh momentum low. This is an **orderly, persistent downtrend — not a momentum crash**. It argues against panic but also against calling a bottom: there is no bullish divergence in the histogram, and 9/15 shows slight re‑expansion of negative momentum (−1.061 → −1.302).

- **RSI: 41.42**, down from **55.85 (8/28)** and **72.23 at the 8/03 peak**. It is not oversold (>30), and it made a **lower low on 9/15 (41.42) with a lower price low (247.22) than 9/10 (RSI 43.62 on a 249.58 low)** — that is confirmation of weakness, **not** bullish divergence.
- RSI’s y≈41 reading historically maps to “weak but not exhausted” — in an intact uptrend this is a dip‑buy zone, in a rolling‑over trend it is the *middle* of the move down. The 200‑SMA and lower‑low structure tell us which regime we are in.

---

## 4. Volatility: an extreme Bollinger squeeze, and price is now poking below the lower band

This is the most actionable part of the setup.

- Bollinger mid: **257.86**; upper: **266.79**; lower: **248.93**
- **Bandwidth = 6.93%** of the mid band ((266.79 − 248.93) / 257.86)
- On **8/14**, bandwidth was **30.3%** (295.43 − 217.61 over a 256.52 mid). That is a **~4.4x compression in one month**.
- **Close 248.42 is $0.51 (0.20%) BELOW the lower band.** %B ≈ **−0.03**.
- **ATR: 6.22, or 2.50% of price** — down **37.7%** from 9.98 on 8/05.

Two readings, both valid:
1. **Short‑term stretched.** A close outside the lower band with RSI at 41 typically produces a snapback toward the mid‑band/10‑EMA. Mean‑reversion traders have a case for a bounce toward **251–255**.
2. **Squeeze + breakdown is a dangerous combination.** The bands are historically narrow *because* the post‑gap volatility died. Narrow bands resolve in expansion, and the first close outside the band, with the mid‑band falling ~0.5–1.0 point/day, biases the resolution **downward** until price reclaims the mid‑band.

Note that today’s range (253.27 − 247.22 = **6.05 points ≈ 0.97× ATR**) was an ordinary‑sized day — not a volatility event. And the **close at 248.42 sat just $1.20 above the low of 247.22** — sellers owned the close. That is a weak‑close signature.

---

## 5. Volume: mild distribution, but no capitulation

- 9/15 volume: **36.28M**, versus a **~32.5M average over the prior 21 sessions → ~1.12× average**.
- The decline is happening on **subdued volume** (recent sessions mostly 21–36M) compared with the event days of **129M (7/31)** and **102M (7/30)**.
- **VWMA 256.51** sits **3.16% above price** and has fallen from 272.05 (8/20) to 256.51 — meaning the average *volume‑weighted* buyer of the last ~20 sessions is underwater. That is overhead supply, not support.

**Nuance to flag:** this is a **breakdown without high‑volume confirmation**. Price broke the September floor (see below) on only 1.1× volume. That reduces the conviction of the bear case — it looks like slow drift/absence of bids rather than institutional liquidation. It is a reason to size positions modestly, not a reason to ignore the break.

---

## 6. The breakdown itself, and the levels that matter

**The single most important technical event on 9/15:** AMZN closed at **248.42**, decisively below the September consolidation floor of roughly **250.6–251.9** (9/01 low 251.93, 9/09 low 250.65, 9/10 low 249.58). That is a 3‑week range failure. It also broke the 9/10 swing low (249.58) and printed a new lower low at 247.22.

Measured/derived levels (arithmetic from tool data, not asserted historical bounces):

| Level | Value | Basis |
|---|---|---|
| Immediate resistance | **251.9–252.4** | Broken Sept floor / 9/01 & 9/09 closes |
| Key resistance cluster | **254.65 / 255.56 / 256.51 / 257.86** | 10‑EMA / 50‑SMA / VWMA / Boll mid |
| Secondary resistance | **258.6–259.8** | 8/21 & 8/31 closes |
| **Gap 50% fill** | **~248.76** | Midpoint of 7/30 close 235.50 → 7/31 low 262.01; **price closed just below it** |
| 61.8% retrace of 227.01→287.20 | **~249.99** | Just above current price — already lost |
| **First major support confluence** | **≈238.0–240.0** | 200‑SMA 240.03 + 78.6% retrace 239.89 + a −17.1% drawdown (matching the magnitude of the May–June correction) |
| Gap origin / deeper support | **235.50**, then **227.01** (6/25 low) | 7/30 close; June swing low |

**Gap status:** the 7/31 gap from 235.50 up to 262.01 is now **~51% filled**. Price resting almost exactly at the half‑gap level is meaningful — a breakaway gap that gives back more than half its body materially weakens the bullish event thesis.

**Drawdown math (verified):**
- From 8/03 peak close 284.02 → 248.42 = **−12.54%**
- From 8/03 intraday high 287.20 → 248.42 = **−13.50%**
- 3/16 close 211.74 → 248.42 = **+17.32%**
- For context, the 5/28→6/25 decline was **−17.15%** and the subsequent 6/25→8/03 rally was **+26.51%**. AMZN has been a violent-swing instrument in 2026; the current −13.5% is *not yet* outside the norm of its own pullbacks, which is why the 238–240 zone is the line in the sand.

---

## 7. Actionable playbook

**Base case (moderate conviction): continued grind lower toward 240, with bounces capped at 255–258.**
The weight of evidence — price below 10‑EMA/50‑SMA/VWMA/Boll mid, MACD below zero and below signal, 21 straight negative histogram prints, RSI with a lower low, lower highs/lows for six weeks, and a fresh break of the September floor — points down. The missing ingredient is volume confirmation.

- **Bearish continuation trigger:** a close below **247.22** (9/15 low). Targets **240.0** (200‑SMA), then **235.5**.
- **Bearish invalidation:** a daily close back above **251.9–252.4** (reclaiming the broken floor) — first warning; a close above **257.9** (Boll mid + VWMA + 50‑SMA stack) — full invalidation.
- **Risk sizing:** ATR is 6.22 (2.50%). A 1×ATR stop from 248.42 sits at **~242.2**; a 1.5×ATR stop at **~239.1**, which conveniently coincides with the 200‑SMA. Size so that a full trip to the 238–240 confluence is survivable.

**Counter‑trend/mean‑reversion setup (lower conviction, requires patience):**
Price outside the lower band + RSI 41 + ATR at the low end of its recent range is textbook short‑term stretch. But **do not front‑run it** — there is no bullish reversal candle, no volume spike, and no RSI divergence. Wait for a **close back above 251.9** with volume ≥ 1.3× the 21‑day average before considering longs. First target would be **254.65→255.56**, where the 10‑EMA and 50‑SMA offer a natural exit.

**What would change the picture:**
1. A **high‑volume** (≥50M) down day closing at the lows — that would convert this drift into real distribution and open 235.5 quickly.
2. A close above **257.9** that holds for two sessions — MACD would likely curl back above signal and the squeeze would resolve upward.
3. A retest of **238–240** that holds on declining volume and produces a positive RSI/histogram divergence — the highest‑quality long entry in this structure, with the 200‑SMA as the backstop.

---

## 8. Key points summary

| Category | Reading (2026‑09‑15) | Signal | Actionable takeaway |
|---|---|---|---|
| **Last price** | Close **248.42**; low 247.22; volume 36.28M (1.12× avg) | Weak close, mild volume | Close near low = sellers control the tape |
| **10‑EMA** | **254.65** (−2.45% vs price), declining 7 weeks | Bearish tactical | Overhead resistance; below = stay defensive |
| **50‑SMA** | **255.56** (−2.79%), slope halved to +0.23/day | Weakening swing trend | Price must reclaim this to neutralize the fade |
| **200‑SMA** | **240.03** (+3.50%), rising | Bullish strategic | Primary uptrend intact; 240 is the critical stop zone |
| **MACD / signal / hist** | **−1.621 / −0.319 / −1.302** | Bearish; crossed zero 9/09 | 21 straight negative histograms, but flat — grind, not crash |
| **RSI** | **41.42** | Weak, not oversold | Lower low with lower price = no bullish divergence |
| **Bollinger** | mid **257.86**, UB **266.79**, LB **248.93**; bandwidth **6.93%** (from 30.3% on 8/14) | Extreme squeeze; close **0.20% below LB** | Squeeze + lower‑band pierce biases expansion downward |
| **ATR** | **6.22** (2.50% of price), −37.7% from 9.98 (8/05) | Volatility compressed | Use 1–1.5×ATR stops: ~242.2 to ~239.1 |
| **VWMA** | **256.51** (−3.16% vs price), falling | Bearish | Volume‑weighted buyers underwater = overhead supply |
| **Structure** | Lower highs 284.02→266.43→258.90→256.78; lower lows 257.73→251.93→249.58→247.22 | Downtrend | Six consecutive weeks of distribution |
| **Breakdown** | Closed below Sept floor **250.6–251.9** and below gap 50% fill **~248.76** | Bearish trigger fired | Confirmation needed on volume |
| **Support cluster** | **238.0–240.0** (200‑SMA 240.03 + 78.6% retrace 239.89 + prior‑correction‑equivalent −17.1%) | High‑confluence demand zone | Best risk/reward for longs if reached with divergence |
| **Invalidation** | Close > **251.9** (warning); close > **257.9** (full) | — | Above 257.9 the bear case is void |