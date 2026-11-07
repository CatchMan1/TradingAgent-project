# GOOGL — Alphabet Inc. | Technical Analysis Dossier
**Analysis date:** 2026-09-01 (latest completed session) · **Close:** $335.02 · **Data window:** 252 sessions (2025-09-02 → 2026-09-01)

---

## 1. Indicator Selection & Rationale

| # | Indicator | Why it earns a slot in this context |
|---|---|---|
| 1 | **close_200_sma** | Price is sitting *exactly* on it (335.05 vs close 335.02). This is the single most consequential level on the chart; the primary trend regime is being adjudicated today. |
| 2 | **close_50_sma** | Medium-term trend spine. It is the upper boundary of the current breakdown structure and its slope/pacing gives the timing for a potential death-cross. |
| 3 | **macd** | Captures the re-acceleration of downside momentum after the failed August recovery — the 2nd leg of a bearish sequence. |
| 4 | **rsi** | Needed to test whether the selloff is stretched. It is *not* (<50, >30), which is decisive for the risk asymmetry argument. |
| 5 | **boll_lb** | Rising lower band converging on price — identifies the precise invalidation level (332.89) for the "trend holds" case. |
| 6 | **boll_ub** | Establishes the width of the envelope; together with the lower band it reveals a violent 1-month volatility compression (squeeze). |
| 7 | **atr** | Sizes stops and targets in the current (contracting) volatility regime and tests whether the decline is orderly or panicked. |
| 8 | **vwma** | Volume-weighted fair value of recent participants. At 343.28 it sits *above* price → recent buyers are underwater → quantifies overhead supply. |

*Confirmation-only (read from the verified snapshot, not separately selected to stay within the 8-indicator cap):* `close_10_ema` (342.36), Bollinger mid / 20-SMA (346.43), `macds` (−2.202), `mfi` (0.490).

**Redundancy avoided:** no double-counting of momentum oscillators (RSI used, StochRSI/MFI excluded as primary); no Bollinger-mid + 50-SMA + VWMA triple-count — each of those measures a *different* thing (mean-reversion anchor, simple trend, volume-weighted cost basis).

---

## 2. Headline Read: A Long-Term Uptrend Testing Its Last Structural Line

The entire setup compresses to one number pair:

- **Close 2026-09-01: $335.02**
- **200-day SMA: $335.05**

Price is **0.01% below** its 200-day benchmark. Everything else in this report is essentially a referendum on whether that line holds.

Context for how we got here:
- **Trailing 12-month return:** $211.35 (2025-09-02 close) → $335.02 = **+58.5%**. The long-term trend is unambiguously up.
- **Drawdown from peak close:** $402.62 (2026-05-13) → $335.02 = **−16.8%**. Intraday peak was $408.61 (2026-05-18); from that high the drawdown is **−18.0%**.
- The 200-day SMA is **rising** at roughly +0.24/day (322.20 on Jul 20 → 335.05 on Sep 1). It is not a static floor — it is a **moving goalpost rising into price**, which mechanically tightens the squeeze each week.

---

## 3. Structural Damage: Dates and Prices

### 3.1 The distribution events
- **2026-07-22 → 2026-07-23:** close-to-close **−7.13%** ($342.09 → $317.69) on **69.4M shares** (vs. a ~23.5M 20-day average). This is the defining supply event of the period.
- **2026-08-05:** opened $383.34, printed a high of $384.48, then closed at **$362.43** — a **−5.74% reversal from the high to the close** (−4.03% close-to-close) on **46.9M shares**. This is a textbook failed-breakout / distribution day.
- Note the offsetting **2026-07-31** thrust: $333.66 → $356.13 (**+6.74%**) on 46.5M shares. The bulls had a violent bid on Jul 31 and it was spent by Aug 5. That is a failed rally, not an accumulation leg.

### 3.2 The sequence of lower highs (post-Aug 5)
| Date | High | Note |
|---|---|---|
| 2026-08-05 | 384.48 | Failed spike; closed 362.43 |
| 2026-08-24 | 351.60 | Lower high #1 |
| 2026-08-28 | 349.14 | Lower high #2 |
| 2026-09-01 | 337.20 | Lower high #3 (accelerating) |

Three consecutive lower highs, each compression-tighter, is a **descending-triangle / bear-flag geometry**, and today's close ($335.02) is at the *lower* edge of that structure.

### 3.3 The range that just broke
From **2026-08-11** onward the stock oscillated between **$338.52** (Aug 27 low) and **$357.61** (Aug 10 high). The last two sessions broke the floor:
- **2026-08-31:** close $339.35, **−2.09%**, low $337.16, volume **33.49M** (~1.42× the 20-day average).
- **2026-09-01:** close $335.02, **−1.28%**, low $333.05, volume **23.34M** (~1.0× average).

**Critical nuance:** the breakdown is only *half* volume-confirmed. Day one was expanded (33.5M), day two was merely average (23.3M). Compare against the genuine distribution days (69.4M on Jul 23, 46.9M on Aug 5, 114.7M on Jun 26 — the latter likely an index/rebalance print). A high-conviction breakdown should be running **>30M sustained**. It isn't yet. Treat the break as **real but unproven**.

---

## 4. Moving-Average Geometry: Bearish Stack, One Regime Still Intact

### 4.1 The stack is fully inverted above price
| Level | Value | Close vs. level |
|---|---|---|
| 50-day SMA | 348.911 | **−3.98%** |
| Bollinger mid (20-SMA) | 346.432 | −3.29% |
| VWMA | 343.280 | −2.41% |
| 10-day EMA | 342.358 | −2.14% |
| **Close** | **335.020** | — |
| **200-day SMA** | **335.051** | **−0.01%** |

Every short- and medium-horizon average sits above price, and they are ordered **bearishly** (10 EMA < VWMA < 20-SMA < 50-SMA). Note especially that the **20-day mean has now crossed below the 50-day mean** — the short-term trend has deteriorated even relative to the already-declining medium-term trend. That is a second-derivative warning, not just noise.

### 4.2 The 50/200 spread is collapsing
- **2026-07-20:** 369.666 − 322.200 = **+47.47** (14.7% of the 200-SMA)
- **2026-08-21:** 351.769 − 333.025 = **+18.74**
- **2026-09-01:** 348.911 − 335.051 = **+13.86** (4.14% of the 200-SMA)

Convergence over the last 7 sessions: **−0.698/day**. Holding that slope, the 50-SMA would cross the 200-SMA in roughly **20 trading sessions (~early October 2026)**. Still a golden-cross regime *today* — but the buffer has shrunk 71% in six weeks. (This is a linear projection, not a forecast; any rally of >2% would defer it materially.)

### 4.3 The 200-day has been broken once before — and reclaimed
This is the most useful precedent in the file:
- **2026-07-23:** close $317.69 vs 200-SMA $323.56 → **closed below**
- **2026-07-24:** close $319.74 vs 200-SMA $323.90 → **closed below**
- **2026-07-27:** close $326.56 vs 200-SMA $324.31 → **reclaimed**

So the last 200-day breach lasted exactly **two sessions** and was reversed by a +2.1% session. That tells you (a) the level has genuine buyers around it, and (b) two consecutive closes below is the *minimum* bar for calling a regime break.

---

## 5. Momentum: Bearish Re-acceleration, But Not Capitulation

### 5.1 MACD
| Date | MACD line |
|---|---|
| 2026-08-05 | **+0.585** (bullish cross above zero) |
| 2026-08-10 | **+1.180** (peak) |
| 2026-08-12 | −0.482 (re-crossed below zero) |
| 2026-08-20 | −2.330 (local trough) |
| 2026-08-25 | −1.807 (feeble bounce) |
| 2026-08-28 | −2.021 |
| 2026-08-31 | −2.348 |
| **2026-09-01** | **−2.924** ← largest 1-day deterioration since the Aug 5 turn |

Verified snapshot: MACD **−2.924**, signal **−2.202**, histogram **−0.721**. The MACD line is below its signal *and* breaking to new lows for the move. The August bullish cross (Aug 5–11) has fully failed — that cross lived for roughly five sessions and produced a $384 high that was immediately sold. **A failed bullish MACD cross followed by a lower low in the oscillator is a high-quality trend-continuation signal.**

### 5.2 RSI
- **2026-09-01: 41.25** (from 49.26 on Aug 28, 44.06 on Aug 31).
- The recent RSI range since Aug 11 has been **44.03 – 52.24** — a persistently sub-50, sub-neutral band. That is characteristic of *distribution*, not accumulation.
- **It is not oversold.** The July capitulation low printed **RSI 31.02 on 2026-07-23**. There is roughly 10 RSI points of downside room before the same exhaustion condition is met.
- RSI is making **lower highs in the oscillator** (62.56 Aug 4 → 52.24 Aug 10 → 49.53 Aug 24 → 49.26 Aug 28 → 41.25 Sep 1), confirming price's lower highs. No bullish divergence is present.

**Verdict:** momentum is bearish and *accelerating*, with no exhaustion signal. This is the single strongest argument against bottom-fishing at the 200-day.

---

## 6. Volatility: A Violent Squeeze Into a Support Test

### 6.1 Bollinger Bands
| | 2026-08-19 | 2026-09-01 | Change |
|---|---|---|---|
| Upper band | 377.61 | **359.97** | −17.64 |
| Mid (20-SMA) | 346.00 | **346.43** | ~flat |
| Lower band | 314.37 | **332.89** | **+18.52** |
| **Width %** | **18.3%** | **7.8%** | **−57%** |

The envelope has collapsed by more than half in nine sessions (mechanically driven by the Aug 5–10 price spike rolling out of the 20-day window). Forward-looking, the window now contains only the calm $338–352 chop, so **bands will stay tight** — a classic squeeze setup that historically precedes an **expansion move**. Direction is not dictated by the squeeze, but **price is resolving it downward**, which tilts the odds bearish.

Price closed just **0.64% above the lower band (332.89)**. Riding the lower band = trend intact; a close below it = volatility expansion to the downside.

### 6.2 ATR — the decline is orderly, which is both good and bad
- **ATR (2026-09-01): 8.385** — the **lowest reading in the 45-session window**.
- Down **−39.8%** from 13.931 on 2026-08-05.
- ATR/Close = **2.50%**.

**Interpretation:** each successive down-leg is smaller and more controlled. That is the signature of a **maturing, low-panic pullback** — supportive of a base forming. But it cuts both ways: compressed ATR *into* a support test means the cost of being wrong is small, yet the **risk of a violent expansion gap is elevated**. Contraction resolves in expansion.

---

## 7. Volume: The Overhead-Supply Problem

**VWMA (2026-09-01) = 343.280**, i.e. **2.41% above the close**. The volume-weighted average price of the recent window is higher than the current price → **the marginal recent buyer is underwater**. This is a measured, quantified statement of overhead supply, and it explains why every rally in August died at $349–352.

VWMA's trajectory is instructive:
- Rose from 345.36 (Aug 10) to **356.34 (Aug 19)** *while price was flat at ~$344* → heavy volume transacted at higher prices.
- Since then: 356.34 → 353.65 → 350.76 → 347.84 → 346.49 → 345.38 → 344.72 → 343.93 → **343.28**, a steady nine-session decline.

Notice that VWMA is now converging *down toward* price rather than price rallying up to it. This is exactly how a downtrend "absorbs" overhead supply — through **time and lower prices**, not through a rally.

**Raw-volume texture:** Aug 13–25 volumes ran 17.8M–26.3M, among the lightest of the year. That is *sellers drying up*, but with no demand offset. Light-volume drift lower is a **vacuum**, and vacuums fall easily.

---

## 8. Levels Map (all tool-derived)

**Resistance (in order of proximity)**
| Level | Source | Significance |
|---|---|---|
| 337.20 | 2026-09-01 high | Immediate ceiling / first lower-high |
| 338.52 | 2026-08-27 low | Broken range floor → now resistance |
| 340.65–342.00 | Aug 27 / Aug 26 closes | Congestion band |
| **342.36** | 10-day EMA | **First neutralizer** |
| **343.28** | VWMA | Overhead-supply line |
| **346.43** | Bollinger mid / 20-SMA | Trend-repair threshold |
| **348.91** | 50-day SMA | **Bull-case proof** |
| 349.14 | 2026-08-28 high | Structural lower high |
| 351.60 | 2026-08-24 high | Break = end of lower-high series |

**Support**
| Level | Source | Significance |
|---|---|---|
| **335.05** | **200-day SMA** | **THE line** |
| 333.05 | 2026-09-01 low | Intraday defense |
| **332.89** | **Bollinger lower** | **Breakdown confirmation trigger** |
| 326.63 | Derived: close − 1 ATR (8.385) | First measured target |
| 324.18–324.45 | Jul 24 high / Jul 27 low | Congestion shelf |
| 319.74 | 2026-07-24 close | Prior 200-SMA breach close |
| 317.69 / 314.90 | 2026-07-23 close / low | **Swing low — must hold for the bull case** |

---

## 9. Scenarios With Explicit Triggers

### 🔻 Bear continuation — *highest probability, ~50%*
**Trigger:** daily close below **332.89** (Bollinger lower) AND below **333.05** (Sep 1 low), ideally with volume **>30M**.
**Path:** 326.63 (1 ATR) → 324.2 (Jul congestion) → 317.7 (Jul 23 close).
**Rationale:** MACD at new lows for the move, RSI not oversold, no bullish divergence, VWMA overhead, 20-SMA now below 50-SMA.
**Confirmation needed:** the volume test. A break on ~23M (today's pace) is a *drift*, not a break — and drifts get reversed.

### ➡️ Base / chop — *~35%*
**Trigger:** defends 333–335, oscillates 335–349, ATR stays <9.5.
**What to do:** nothing directional. This is the highest-probability *outcome shape* for a squeeze that hasn't picked a direction. Use the coiled range for defined-risk option structures or wait for the real resolution.

### 🔼 Bull repair — *~15% absent new information*
**Trigger sequence (needs all three):**
1. Close above **342.36** (10-EMA) — neutralizes the immediate downtrend;
2. Close above **346.43** (20-SMA/Boll mid) — first higher close in 8 sessions;
3. Close above **348.91** (50-SMA) *and* **351.60** (Aug 24 high) — breaks the lower-high series.
**What would generate it:** a reclaim of the 200-day with an ATR expansion day on >30M volume, or a fundamental catalyst. Note the Jul 31 +6.74% thrust proves this name can produce violent upside gaps — but it also proves such gaps were *sold* within four sessions.

---

## 10. Risk Management (ATR-calibrated)

- **ATR = 8.385 (2.50% of price).** Position sizing should reflect that this is a *low* volatility reading; a re-expansion to the August level (ATR 13.9) would **inflate risk by 66%** on unchanged position size. Size to the *expanded* ATR, not today's.
- **Long stop reference:** below **332.89** (Boll lower) — a close there invalidates the 200-day defense. That is ~0.64% of risk from the close, deliberately tight because the level is so well-defined. Beware whipsaw: the July analogue produced a 2-day false break.
- **Long target reference:** 346.43 (20-SMA) / 348.91 (50-SMA) = +3.4% / +4.1%.
- **Short entry reference:** a confirmed close <332.89 with volume expansion; **stop above 342.36** (10-EMA) — ~2.8% risk, ~2.6% to the first target (326.63). Reward:risk ≈ 1:1 to the first target, improving to ~1:2 at 317.7.
- **Do not fade the 200-day with size until you see a volume signature.** The August evidence is that oversold bounces in this name were sold at $349–352 within sessions.

---

## 11. Data Integrity & Caveats

- **No discrepancies** between `get_stock_data` and the verified snapshot. The 2026-09-01 row reconciles exactly (O 336.00 / H 337.20 / L 333.05 / C 335.02 / V 23,342,700), and the snapshot's indicator values match the `get_indicators` series (50-SMA 348.9108, 200-SMA 335.0507, 10-EMA 342.3580, MACD −2.9237, RSI 41.2496, Boll_UB 359.9695, Boll_LB 332.8945, ATR 8.3854, VWMA 343.2801).
- **`mfi` = 0.49034** in the snapshot — this is a normalized (0–1) scale, not the standard 0–100. Read as ~49/100 = neutral. Not used as a signal here.
- Historical 200-day SMA is only evaluable from **2026-07-20** forward in this dataset (200 sessions of prior history are required), so all 200-day claims are confined to that window.
- The 20-day average volume (~23.5M) and the 1-ATR-derived level (326.63) are **computed from tool output**, not vendor-provided fields; they are labeled as derived.
- The death-cross timing (~early October 2026) is a **linear extrapolation** of the observed 7-session convergence slope, not a prediction.
- Dividends were small but present (e.g., $0.21 ex-dates 2025-09-08, 2025-12-08, 2026-03-09, $0.22 on 2026-06-08); the total-return index (338.008 vs. price 335.020) is used for all long-horizon return math.
- **No fundamentals, earnings dates, or news are in scope here.** A stock sitting on its 200-day after a −16.8% drawdown and a July gap-down on 69M shares often has a catalyst behind it; this report is price/volume/indicator-only.

---

## 12. Summary Table

| Dimension | Reading (2026-09-01) | Signal | Actionable takeaway |
|---|---|---|---|
| **Price** | $335.02 (−1.28% d/d) | Bearish | Closed in the lower third of the day's range |
| **Primary trend** | 200-SMA 335.051, rising +0.24/d | **At the line** | Close is 0.01% *below*; the entire thesis rides here |
| **Medium trend** | 50-SMA 348.911, falling | Bearish | −3.98% below 50-SMA; upper bound of any bounce |
| **Short trend** | 10-EMA 342.358, falling | Bearish | −2.14% below; first neutralizer on a rally |
| **MA regime** | 50-SMA − 200-SMA = +13.86 (was +47.47 on 7/20) | Deteriorating | Golden cross still intact; death cross ~20 sessions away on current slope |
| **MACD** | −2.924 vs signal −2.202, hist −0.721 | **Bearish, accelerating** | Failed Aug bullish cross; new low for the move |
| **RSI** | 41.25 (from 49.26 on 8/28) | Bearish, **not oversold** | ~10 pts of room to the July exhaustion print of 31.02 |
| **Bollinger width** | 7.8% (from 18.3% on 8/19) | **Squeeze** | −57% compression; expansion imminent, direction unresolved |
| **Bollinger lower** | 332.894, rising | Trigger level | Close below = breakdown confirmation |
| **ATR** | 8.385 (2.50% of price), −39.8% vs Aug 5 | Compressed | Orderly decline = maturing pullback; but size to *expanded* ATR |
| **VWMA** | 343.280 (−2.41% below price? No — price is below it) | **Overhead supply** | Recent buyers underwater; VWMA converging *down* to price |
| **Volume (20d avg)** | 23.5M; 8/31 = 33.5M (1.42×), 9/1 = 23.3M (1.0×) | **Unconfirmed** | Breakdown has only half a volume signature — needs >30M sustained |
| **Key support** | 335.05 / 333.05 / 332.89 → 326.63 → 317.69 | — | Loss of 332.89 opens 326.6 then the July low |
| **Key resistance** | 342.36 → 346.43 → 348.91 → 351.60 | — | Three closes needed to repair; 348.91 = bull proof |
| **Precedent** | 200-SMA breached 7/23–7/24, reclaimed 7/27 | Bullish tell | Last breach lasted 2 sessions; require 2 closes below before acting |
| **Stance** | **Defensive / wait-for-confirmation** | Neutral-to-bearish | Don't buy the 200-day on momentum that's still accelerating down; don't short a level that just held twice without volume |