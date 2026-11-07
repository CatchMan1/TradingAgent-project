# AAPL — Technical & Tactical Review (as of Monday, 2026-08-17)

**Verified reference row (source of truth):** 2026-08-17 O 306.21 / H 307.66 / L 302.94 / **C 305.59**, volume 38,169,300. Total-return index 311.02.
All price and indicator values below are taken from the verified snapshot and the indicator series; `get_stock_data` and `get_verified_market_snapshot` agree exactly on OHLCV for every overlapping row — **no data discrepancy to flag** for the fields used. (One cosmetic note: the snapshot's `mfi` prints as 0.4236, a 0–1 normalized scale rather than 0–100; I did not use it.)

---

## 1. Regime classification: intact primary uptrend, damaged intermediate trend, unresolved short-term base

AAPL is in a **"bull trend under distribution"** state — the most ambiguous of set-ups:

| Layer | Reading | Verdict |
|---|---|---|
| Primary (200-day) | Close 305.59 vs **200 SMA 280.67** (+8.88%), 200 SMA rising every session (279.41 on 08‑07 → 280.67 on 08‑17) | **Bullish** |
| Intermediate (50-day) | Close 305.59 vs **50 SMA 309.08** (−1.13%); 50 SMA rolled over: peak **309.79 on 2026‑08‑07** → 309.08 on 08‑17 (6 consecutive declines) | **Deteriorating** |
| Short (10-day) | **10 EMA 308.76**, falling every session since 2026‑07‑30 (331.31); price below it by −1.03% | **Bearish** |
| Structure | 2026‑07‑28 close **340.08** (29th intraday high **344.57**) → 305.59 = **−10.14%** (−11.30% from the intraday high) | **Corrective** |
| 50 > 200 | 309.08 > 280.67, spread +28.41 pts (+10.1% of the 200 SMA) | **Golden-cross structure still live** |

The key point: the *long-term* trend engine is untouched, but the *medium-term* engine that drove the June–July advance has stalled. The 50 SMA flattening and rolling over while price sits beneath both the 10 EMA and the 50 SMA is textbook intermediate-term deterioration inside a primary uptrend.

---

## 2. Price structure — what actually happened, with dates and prices

1. **The July parabola:** close **275.15 (2026‑06‑25) → 340.08 (2026‑07‑28) = +23.60%** in 23 sessions. RSI hit **71.65 on 2026‑07‑17** and **71.43 on 07‑16** — a genuine overbought extreme, not a "70 touch-and-go."
2. **The break:** 2026‑07‑30 close 333.43 → **2026‑07‑31 open 304.81, close 308.91, low 300.00 on 132,489,100 shares** — a −7.36% one-session repricing on roughly 2.6× the average volume of the past five sessions (37.18M). That is a classic **distribution / gap-down** event, and it left a supply shelf across **314–333**.
3. **The base attempt:** since 07‑31 the tape has built a **300.00–313.33** box:
   - Support tested at **low 300.00 (07‑31)**, **low 302.56 (08‑03)**, **low 300.57 (08‑12)** — three touches of the same 300–302.6 shelf.
   - Resistance capped at **high 316.29 (08‑06)**, **close 313.33 (08‑07)**, then a fade to 302.25 (08‑12).
   - Last three sessions: 305.26 → 305.93 → 305.59, i.e. a tight 0.2% coil directly under the 10 EMA/50 SMA cluster.

### Fibonacci confluence (derived from real swing points, not invented)
- Rally range 275.15 → 340.08 = 64.93 pts.
- **50% retracement = 307.62** — sits inside the **10 EMA 308.76 / 50 SMA 309.08** cluster.
- **61.8% retracement = 299.95** — sits precisely inside the **300.00–302.56** support shelf.

So price at 305.59 is trapped between a **307.6–309.1 pivot ceiling** and a **300.0–302.6 support floor**. That is the whole story: a 2.3%-wide decision box.

---

## 3. Momentum — the nuance is in the second derivative

**MACD (line −2.6758, signal −0.3855, hist −2.2903):** unambiguously bearish on level — the MACD line crossed below zero on **2026‑08‑11** (first negative print since July) and made successively lower lows into 08‑17 (−2.186 → −2.461 → −2.676). A bearish line/signal crossover occurred around 08‑10/08‑11.

**But the histogram is decelerating.** Peak downside momentum was **−3.634 on 2026‑08‑05**; the histogram has since narrowed to −3.343 (08‑12), −3.035 (08‑13), −2.648 (08‑14), **−2.290 (08‑17)** — four consecutive contractions. Translation: the *bearish trend is still in force, but the selling impulse is exhausting*. This is the early-warning condition for a bullish MACD crossover, **not** the crossover itself. Trading the crossover before it prints is how accounts get chopped up in a 300–313 box.

**RSI 43.41:** neutral-bearish, and critically **not oversold** — there is 13 points of downside room before 30. The RSI collapse from 71.65 (07‑17) to 40.22 (08‑12) maps the entire momentum reset. One constructive detail: the **08‑03 RSI low was 40.34 on a price low of 302.56, while the 08‑12 RSI low was 40.22 on a *lower* price low of 300.57** — a marginal, unconfirmed positive divergence (momentum stopped deteriorating as price made a lower low). Aug 17 RSI ticked to 43.41 from 43.67 — flat, not yet turning up.

**Verdict:** momentum is bottoming, not reversing. Requires confirmation.

---

## 4. Volatility — a coiled spring, but a wide one

- **ATR 7.64** (2.50% of price), down from **9.87 on 2026‑07‑31** and **8.02 on 07‑29**. Volatility is contracting for the fourth straight week — consistent with the box formation and with post-shock digestion.
- **Bollinger (verified snapshot):** middle **317.38**, upper **343.84**, lower **290.91**. Bandwidth = 52.93 pts = **16.68% of the middle band** — extremely wide, a legacy of the July collapse. Price at 305.59 sits at **−3.71% below the middle band** and **+5.05% above the lower band**, in the lower third of the envelope.
- The middle band is falling fast (**324.37 on 07‑31 → 317.38 on 08‑17**), which mechanically drags the whole envelope down and will keep pressuring price until the middle band flattens. Notably, the middle band at 317.38 and the 07‑31 gap zone both cluster at ~317 — a major confluence resistance.
- **Implication:** with ATR at 7.64 and a 300–313 box, a single day's range (~7.6 pts, 2.5%) can *fake* a breakdown to 298 or a breakout to 313 without any real change in trend. Demand closing prices, not wicks.

---

## 5. Volume — the strongest bearish tell, and the strongest bullish consolation

- **VWMA 311.96** vs close 305.59 = **−2.04%**. Price is trading below its volume-weighted average price, and VWMA has declined every session since **329.58 (07‑30)**. Read: the volume-weighted holder base is **underwater**, and rallies into 312 are running into trapped supply — rallies become sell zones until VWMA is reclaimed.
- The 261,775,500 shares on **2026‑06‑26** (with the close at 283.78 vs a 274.21 low — a huge-volume reversal bar) and the 132,489,100 shares on **2026‑07‑31** (a −7.36% distribution bar) are the two dominant volume events of the last three months. The first marked a durable low; the second marked a top. The current leg has **no high-volume accumulation bar to offset it**.
- Constructively, the pullback is happening on **shrinking volume**: last five sessions (08‑11 to 08‑17) average **37.18M** vs 132.49M on 07‑31, and **28,229,400 on 2026‑08‑14** is the lightest session in the visible 40-session window. Fading volume on a fade = supply drying up, which is what a base is supposed to look like.

---

## 6. Actionable scenarios and levels

**Pivot zone: 307.6–309.1** (50% retracement + 10 EMA + 50 SMA). Whoever controls this band controls the next 5%.

### Base case — range 300–313 (highest probability)
Chop between the triple-tested 300–302.6 floor and the 313–316 ceiling while the MACD histogram grinds toward zero. Trade the edges, stand aside in the middle: risk/reward at 305.59 is roughly 1:1 against either boundary, which is not a trade.

### Bull case — needs two confirmations, not one
1. Daily **close above 309.08** (50 SMA), ideally above **313.33** (08‑07 close).
2. MACD histogram turning **positive** (currently −2.29) and RSI back above **50**.
3. Volume expansion above ~50M on the up-day (the last five sessions averaged only 37.2M).
→ Targets: **317.38** (Bollinger middle) → **321.66–327.74** (07‑23/07‑21 congestion) → **333.43** (07‑30 close). A close above 317.4 with volume would invalidate the bearish distribution thesis outright.
*Entry tactic:* buy the reclaim of 309.1, stop on a close below **300.0** (−9.1 pts ≈ 1.2 ATR), or tighter at 303 (−6.1 pts ≈ 0.8 ATR — but that stop sits inside the noise band; I'd prefer 298, under the 08‑12 low, for a viable hold).

### Bear case — the trigger is 300, not 305
A decisive close **below 300.00** (which would also break the 61.8% retracement at 299.95 and put price under all three base lows) opens:
- **290.91** (Bollinger lower band, −4.8%), then
- **280.67** (200 SMA, −8.2% — the primary trend line in the sand).
→ Short entry on the 300 break, stop above **310** (≈1.3 ATR), targets 291 then 281. Note the 200 SMA is *rising* ~1.3 pts per six sessions, so it will be ~282–283 by mid-September — a moving, not fixed, target.

### Invalidation / risk map
- Bullish thesis dead if: daily close < 300.00.
- Bearish thesis dead if: daily close > 317.38 with ≥50M volume.
- Anything between 302.6 and 313.3 on <40M volume = noise; do not size up.

### Position sizing (using ATR, not guesswork)
ATR 7.64 = 2.50% of price. A 2×ATR stop is 15.27 pts (5.0%). At a 1% account risk budget, that implies a **maximum position of ~20% of equity** for a swing long from this zone. In a 16.7%-wide Bollinger envelope with a falling middle band, favor smaller size and wider stops over tight stops and full size — a 0.8×ATR stop (6.1 pts) is statistically inside the daily noise and will be tagged.

---

## 7. Why these eight indicators were chosen (complementarity, not duplication)

| Indicator | Value (2026‑08‑17) | Why it earns a slot here |
|---|---|---|
| **close_200_sma** | 280.67, rising | Defines the *primary* trend and gives a non-negotiable bear target/invalidation. |
| **close_50_sma** | 309.08, rolling over from 309.79 (08‑07) | The intermediate trend and the single most important pivot overhead — its slope change is the core signal. |
| **close_10_ema** | 308.76, falling since 07‑30 | Fast, confirms the short-term downtrend and stacks with the 50 SMA into one 307.6–309.1 decision band. |
| **macd** (+ histogram) | −2.676 / hist −2.290, narrowing from −3.634 (08‑05) | Captures the crucial second-derivative story: bearish level, decaying impulse. |
| **rsi** | 43.41, with a marginal 08‑03/08‑12 non-confirmation | Flags that there's *room* to fall (not oversold) and surfaces the weak divergence. |
| **boll** (middle; envelope from snapshot) | 317.38 mid, 343.84 / 290.91 bands | Quantifies the 16.68% envelope, the falling mean as resistance, and gives the 290.91 downside magnet. |
| **atr** | 7.64 (2.50% of price), falling | Converts every level into a risk-defined stop and dictates position size; the compression itself is a signal. |
| **vwma** | 311.96 | The only volume-integrated price measure here — proves the holder base is underwater and that rallies to 312 face supply; independent of the SMA/EMA family. |

Deliberately excluded: `macds` (derivable from macd + macdh), `boll_ub`/`boll_lb` as separate selections (used from the snapshot to avoid triple-weighting one family), stochastic-type oscillators (redundant with RSI), and `mfi` (its snapshot value is on a non-standard 0–1 scale).

---

## 8. Key takeaways

1. **Do not confuse a primary uptrend with an intermediate downtrend.** AAPL is +8.88% above a *rising* 200 SMA (280.67) — the long-term bid is intact. But it is −1.13% below a *now-falling* 50 SMA (309.08) and −1.03% below the 10 EMA (308.76), with the 50 SMA down six sessions in a row.
2. **The 2026‑07‑31 gap (−7.36% on 132.5M shares) changed the character of the tape.** It created a 314–333 supply shelf and put VWMA (311.96) above price — every rally is now selling into underwater holders.
3. **The bearish momentum is decelerating, not reversing.** MACD histogram has contracted four straight sessions off the −3.634 low, but the MACD line is still making lower lows and RSI (43.41) is nowhere near oversold.
4. **300.00–302.56 is the line.** Three separate tests (300.00 on 07‑31, 302.56 on 08‑03, 300.57 on 08‑12) plus the 61.8% retracement at 299.95. A close below it targets 290.91 then 280.67.
5. **307.62–309.08 is the gate.** A close above it, with volume >50M and MACD hist positive, reopens 317.38 and then 321.7–327.7.
6. **Volume says the pullback is orderly:** last five sessions average 37.18M vs 132.49M on the distribution bar, and 08‑14's 28.23M was the lightest in 40 sessions. That's constructive for a base — but the absence of a high-volume up-bar means the base is unconfirmed.

**Stance: neutral / no new exposure at 305.59.** This is a middle-of-the-box price with ~1:1 risk/reward in both directions. Wait for either (a) a high-volume reclaim of 309.1–313.3 to go long toward 317.4+, or (b) a close below 300 to go short toward 291 and 281. Risk 1×–2× ATR (7.6–15.3 pts), and keep position size ≤20% of equity at a 1% risk budget.

---

## Summary table

| Dimension | Reading (2026‑08‑17) | Signal | Key level / action |
|---|---|---|---|
| Close / OHLCV | 305.59 (O 306.21, H 307.66, L 302.94) | — | Vol 38.17M vs 5-day avg 37.18M |
| Primary trend (200 SMA) | 280.67, rising; price +8.88% | **Bullish** | Bear target / ultimate support 280.67 |
| Intermediate trend (50 SMA) | 309.08; peak 309.79 on 08‑07, 6 straight declines | **Deteriorating** | Reclaim 309.08 = bullish trigger |
| Short trend (10 EMA) | 308.76, falling since 07‑30 | **Bearish** | Price below → intraday resistance |
| Swing structure | 340.08 (07‑28) → 305.59 = −10.14%; 07‑31 gap −7.36% | **Corrective** | 314–333 supply shelf overhead |
| Fibonacci | 50% = 307.62; 61.8% = 299.95 | Neutral | Confluence with 50 SMA and 300 support |
| MACD | −2.676 / signal −0.3855 / hist −2.290 | **Bearish, decelerating** | Hist narrowing 4 sessions from −3.634 (08‑05) |
| RSI | 43.41 | **Neutral-bearish** | Not oversold; marginal 08‑03/08‑12 divergence |
| Bollinger | Mid 317.38, up 343.84, low 290.91; width 16.68% | Volatile, mean falling | 317.38 resistance; 290.91 downside magnet |
| ATR | 7.64 (2.50% of price), falling from 9.87 (07‑31) | **Volatility compression** | 2×ATR stop = 15.3 pts → size ≤20% equity |
| VWMA | 311.96; price −2.04% below, falling since 07‑30 | **Bearish** | 312 = volume-weighted supply zone |
| Range box | 300.00 – 313.33 (all three base lows 300.00/302.56/300.57) | **Coiling** | Trade edges only; avoid the middle |
| Bull trigger | Close > 309.08, then > 313.33, vol > 50M, MACD hist > 0 | Pending | Targets 317.38 → 321.66/327.74 → 333.43 |
| Bear trigger | Close < 300.00 | Pending | Targets 290.91 → 280.67 (200 SMA) |
| Recommendation | **HOLD / NO NEW POSITION at 305.59** | Neutral | Await a 300 break or a 309–313 reclaim |