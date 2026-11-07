# GOOGL — Multi-Horizon Technical Assessment (as of close 2026-09-23)

## 1. Verified Snapshot Facts (source of truth)

| Field | Value |
|---|---|
| 2026-09-23 OHLC | O 349.86 / H 350.00 / L 337.45 / **C 337.83** |
| Volume | 35,576,200 |
| Prior close (2026-09-22) | 351.16 |
| One-day change | **−13.33 (−3.80%)** |
| close_10_ema | 345.072 |
| close_50_sma | 345.072 |
| close_200_sma | 337.950 |
| MACD / Signal / Hist | +0.3449 / −0.6323 / **+0.9772** |
| RSI | 45.06 |
| ATR | 9.155 |
| VWMA | 343.933 |
| Bollinger mid / upper / lower | 341.99 / 354.78 / 329.20 |

Everything below is anchored to this frozen snapshot; no post-close information is used.

---

## 2. Why These 8 Indicators

I chose a **trend-hierarchy + momentum + risk + volume** set, deliberately avoiding duplicate oscillators:

1. **close_10_ema** — the fastest read on the two-week rally that just failed.
2. **close_50_sma** — the intermediate trend line that has flipped from support to overhead supply; also the trigger level for any bullish repair.
3. **close_200_sma** — the long-term bull/bear line that GOOGL is now sitting directly on; also required to monitor the compressing 50/200 spread.
4. **macd** — confirms the 2026-09-14 bullish crossover and the 2026-09-21 zero-line reclaim, both now at risk.
5. **macdh** — measures whether that crossover is strengthening or decaying; this is where the deterioration first shows.
6. **rsi** — regime gauge (above/below 50) and whether there is downside room before oversold.
7. **atr** — volatility is expanding on the selloff; needed for stop placement and position sizing.
8. **vwma** — volume-weighted fair value, the cleanest test of whether the decline is distribution or noise.

*(Bollinger bands appear above only as snapshot context, not as one of the eight selections.)*

---

## 3. Trend Structure: A Bull Market Under Intermediate Duress

**Long horizon — still up, but only just.** The 200-day SMA is **rising**: 333.38 on 2026-08-24 → 337.95 on 2026-09-23. GOOGL closed at 337.83, i.e. **0.04% below it** — technically a break, but only $0.12 and well inside one ATR ($9.15). Treat this as a **test of the 200-day, not a confirmed break**. It is the single most important line in the chart right now.

**Intermediate horizon — clearly down.** The 50-day SMA is **falling**: 351.57 (8/24) → 345.07 (9/23). Price is **2.10% below** it, and 10-EMA and 50-SMA are effectively identical at 345.07, creating a single, well-defined overhead shelf.

**The 50/200 spread is collapsing.** On 8/24 the 50-SMA was 18.2 points above the 200-SMA; on 9/23 it is **7.12 points** (2.11%). At the trailing 30-session rates (50-SMA ≈ −0.22/day, 200-SMA ≈ +0.15/day) the lines converge at roughly 0.37/day, implying a **potential death cross in about 19 trading sessions (~late October 2026)** if nothing changes. That is a mechanical projection, not a forecast — but it defines the clock the bulls are working against.

**The three-month picture is a distribution range, not an uptrend.** GOOGL closed at 337.39 on 2026-06-26 and 337.83 on 2026-09-23 — **+0.13% over three months**. Within that window the sequence of peaks has decayed: intraday high 408.61 (2026-05-18) → 384.48 (2026-08-05) → 359.44 (2026-09-18) → 364.17 (2026-09-22). Lows are roughly flat-to-lower (330.20 on 6/26 vs 327.74 on 9/10). **Lower highs + flat lows = compression with a bearish tilt.** That is the structural backdrop against which today's break must be judged.

---

## 4. The 2026-09-22 → 09-23 Reversal Is the Story

- **2026-09-22:** opened 357.65, ran to **364.17**, closed **351.16** — a ~13-point upper wick, closing in the bottom third of the range.
- **2026-09-23:** opened 349.86, high **350.00**, low **337.45**, closed **337.83** — a bearish session closing essentially on the low, leaving an **unfilled gap zone between 350.00 and 351.16**.
- **The rally has been fully erased:** the 9/23 close (337.83) is *below* the 9/11 close (338.50), meaning eight sessions of gains were given back in one day.

This two-bar sequence — exhaustion wick followed by a gap-and-sell — is the highest-quality bearish evidence in the dataset. It matters more than any single oscillator reading because it happened at the top of the range where sellers had previously been trapped.

Additional confirmation: the 9/22 high of 364.17 was **~2.6% above the 354.78 upper Bollinger band** (as measured on the 9/23 snapshot) before closing back inside the band. That is a failed upside extension, not a breakout.

---

## 5. Momentum: Bullish Crossover Intact, Internals Deteriorating Fast

**MACD:** The MACD line crossed above its signal on **2026-09-14** (histogram flipped from −0.43 to +0.57) and crossed above zero on **2026-09-21** (+0.637). Both events still stand: MACD +0.345 vs signal −0.632, histogram **+0.977**.

**But the histogram has broken its uptrend:** 1.545 (9/18) → 2.002 (9/21, peak) → 1.953 (9/22) → **0.977 (9/23)**. That is a >50% single-session decay, and the MACD line itself collapsed from 1.076 to 0.345 (−0.73). At this rate the histogram flips negative within roughly **two sessions** — which would mark the failure of the 9/14 crossover. Watch the **MACD line's zero line at 0.00** as the second domino.

**RSI:** 58.80 (9/21) → 55.26 (9/22) → **45.06 (9/23)**. Two key observations:
- The rally to a 354.97 close **never pushed RSI above 59** — no overbought reading, i.e. no real buying power behind it. Weak rallies fail more easily.
- RSI has now lost the 50 midline, shifting the short-term regime from bullish to **neutral-bearish**. It is **not oversold**; the September 9 low printed RSI 39.36. **There is roughly 6 RSI points of downside room even if price only retests the 9/10 low** — the oscillator is not yet a reason to buy.

---

## 6. Volatility and Volume: Expanding Downside, Genuine Distribution

- **ATR 9.155**, up **14.7%** from the 7.983 local low on 9/10 — volatility is expanding *into* weakness, the normal signature of a trending decline rather than a benign pullback. ATR = **2.71% of price**.
- **9/23 true range was $12.55** (high 350.00 to low 337.45), about **1.37× ATR** — an outsized range day.
- **Volume 35.58M ≈ 1.33×** the ~26.8M average of the prior 20 sessions (derived from the tool's volume column). Elevated on a −3.8% close and near the low = **distribution, not capitulation** (no volume climax characteristic of a washout).
- **VWMA 343.93 sits above price (337.83, −1.77%).** The volume-weighted average holder is now underwater. This is the least ambiguous bearish confirmation in the set.
- Context on prior volume spikes: 2026-09-18 traded 47.63M with a 359.44 high but closed at 349.54 — a **volume spike with no price follow-through**, which preceded this week's failure. The 114.7M share session on 2026-06-26 also produced no sustained upside. **Large-volume up-days in GOOGL have not been translating into trend.**

---

## 7. Level Map (all levels derived from tool output)

**Resistance**
| Level | Basis |
|---|---|
| 341.99 | Bollinger mid — first reclaim hurdle |
| **343.93–345.07** | **VWMA + 10-EMA + 50-SMA cluster — the pivotal zone** |
| 350.00–351.16 | 9/23 high + unfilled gap |
| 354.78–359.44 | Bollinger upper + 9/18 high |
| 364.17 | 9/22 rejection high |

**Support**
| Level | Basis |
|---|---|
| **337.95** | **200-day SMA (price is 0.04% below — active test)** |
| 337.39–338.50 | 6/26 close, 9/8 & 9/11 closes — confluence shelf |
| 329.20–332.82 | Bollinger lower + 9/2 low + 6/26 low (330.20) |
| 327.74 | 9/10 swing low — the range floor |
| 317.69 | 7/23 close (next shelf below the range) |

---

## 8. Actionable Playbook

**Base case (neutral-to-bearish): hold, do not add.** GOOGL is a long-term uptrend testing its long-term trend line from below/at it, with intermediate momentum broken and volume confirming supply. This is a "prove it" moment, not a bargain-hunting moment.

**Bullish repair (needs two closes, not one):**
- Trigger: **daily close above 345.1** (the 10-EMA/50-SMA confluence) on volume **> ~27M**.
- Confirmation: MACD histogram re-expands and RSI reclaims 50.
- Targets: 351.2, then 354.8–359.4. Invalidation: close back under 341.99.
- Probability-weighted: low near term given the histogram decay and the 350.00–351.16 gap acting as a lid.

**Bearish continuation:**
- Trigger: **decisive close below 337.39** (breaks the 200-SMA test *and* the June/September shelf) on volume > 30M.
- Targets: 330–332 (Bollinger lower + June low), then **327.74**.
- A close below 327.74 converts the three-month range into a confirmed downtrend and puts 317.69 in play.
- Note: a break of 337.39 is only ~$0.45 away — the market is at the decision point *now*.

**Risk management (ATR-based):**
- 1.5× ATR = **$13.73**; 2.0× ATR = **$18.31**.
- Longs initiated near 338 with a 2×ATR stop at ~**319.5** risk 5.42% per share; at a 1% portfolio risk budget that implies ~**18% position weight**.
- A tighter, structure-based stop at **327.70** (below the range floor) risks 3.0% per share.
- Because ATR is rising, **reduce size rather than widen stops** if volatility keeps expanding.

**What would change my mind:** (a) a close above 345.1 with above-average volume, (b) a MACD histogram that re-accelerates rather than crosses zero, (c) a hold of 337.4 accompanied by a *declining* ATR (seller exhaustion), or (d) a reversal bar off 327.7–330 on volume >40M (true capitulation).

---

## 9. Key Points Summary

| Dimension | Reading (2026-09-23) | Interpretation | Actionable Level |
|---|---|---|---|
| Close | 337.83 (−3.80% d/d) | Sharp distribution day, closed near low | — |
| 10-EMA | 345.07 | Short-term trend broken; price 2.10% below | Reclaim = bullish repair |
| 50-SMA | 345.07 (falling from 351.57 on 8/24) | Intermediate trend down; now resistance | Overhead shelf 343.9–345.1 |
| 200-SMA | 337.95 (rising) | Long-term uptrend intact; price 0.04% below = live test | Decisive break <337.39 |
| 50 vs 200 spread | +7.12 pts (was +18.2 on 8/24) | Compression; mechanical death-cross risk ~late Oct | Monitor weekly |
| MACD | +0.345 vs signal −0.632 | Bullish cross (9/14) + zero reclaim (9/21) still valid | Loss of 0.00 = failed cross |
| MACD histogram | +0.977 (peak 2.002 on 9/21) | Momentum halved in one session | Flip negative ≈ 2 sessions |
| RSI | 45.06 (from 58.80 on 9/21) | Lost 50 midline; rally never overbought; not oversold | Room to ~39 (9/9 low) |
| ATR | 9.155 (+14.7% from 9/10) | Volatility expanding into weakness | 2×ATR stop ≈ 319.5 |
| VWMA | 343.93 (price 1.77% below) | Average volume-weighted holder underwater = distribution | Bearish confirmation |
| Volume | 35.58M ≈ 1.33× 20-day avg | Selling pressure, not capitulation | >40M at lows = washout |
| Bollinger (context) | Mid 341.99 / Up 354.78 / Low 329.20 | 9/22 high 364.17 overshot upper band and failed | 341.99 = first hurdle; 329.20 = downside magnet |
| 3-month performance | +0.13% (6/26 close 337.39) | Range/distribution, lower highs, not a trend | Range 327.74–384.48 |
| **Stance** | **HOLD / neutralize; no new longs** | Long-term trend testing, intermediate trend broken | Long only >345.1; bearish <337.39 |

*Data caveats: all figures are point-in-time as of the 2026-09-23 session and reflect cached OHLCV (raw prices; $0.22 ex-dividend on 2026-09-04). No fundamental, news, or post-close information is incorporated. The death-cross timeline is a linear extrapolation of trailing moving-average slopes, not a prediction.*