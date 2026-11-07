# AMZN — Technical Analysis & Trade Plan (as of 2024-01-11)

**Data source of truth:** verified snapshot for 2024-01-11. Latest session: **Open 155.04 / High 157.17 / Low 153.12 / Close 155.18**, volume **49.07M**. No discrepancy was found between the price CSV and the verified snapshot — the 2024-01-11 row matches line for line.

---

## 1. Indicator selection and why this set fits the current regime

AMZN is in a **mature, high-slope uptrend that just resumed after a sharp 6-session pullback and has now punched to a new closing high**. That regime calls for (a) trend structure, (b) momentum re-acceleration confirmation, (c) a stretch/mean-reversion guard, (d) volatility for sizing, and (e) volume confirmation of the breakout. My 8 selections, with no redundant pairings:

| # | Indicator | Role in this specific setup |
|---|---|---|
| 1 | **close_50_sma** | Medium-term trend spine; at 146.80 it defines the "higher low" structure and the first structural support if the breakout fails. |
| 2 | **close_200_sma** | Long-term bull/bear arbiter; at 129.77 it confirms the primary uptrend and quantifies how far extended the move is (+19.6%). |
| 3 | **close_10_ema** | The recovery trigger: price reclaimed it on 2024-01-08/09 and it is now curling up — the fastest read on whether the bounce is real. |
| 4 | **macd** | Confirms whether the underlying intermediate momentum trend is re-asserting after the January dip. |
| 5 | **macdh** | Separates "MACD falling" from "MACD falling *less*" — critical right now, because the histogram is 5 sessions into a contraction toward a bullish crossover. |
| 6 | **rsi** | Not close to 70 (62.8), so it is being used as a *headroom/divergence* gauge rather than an overbought alarm. |
| 7 | **atr** | Volatility is re-expanding off a December compression low; ATR sets stop distance and position size objectively. |
| 8 | **vwma** | Tests whether the breakout carries volume weight; price is only modestly above VWMA, which is the main caveat to the bull case. |

*Supplementary reference (from the verified snapshot, not counted in the 8):* Bollinger mid **151.1565**, upper band **157.2954**, lower band **145.0176**. I use these only for band-position context because they happen to stack with the 10-EMA/VWMA cluster.

I explicitly avoided `stochrsi` (duplicates RSI's information), `macds` (fully implied by MACD minus histogram), and `boll`/`boll_lb` (the middle band duplicates the 20-SMA information already covered by 10-EMA/50-SMA and VWMA).

---

## 2. Price structure: a confirmed higher-low sequence and a new high

The October–January sequence is unambiguously bullish on swing structure, using actual datapoints from the CSV:

- **Rally origin:** 2023-10-26 low **118.35** (close 119.57) — the base of the entire advance.
- **Higher lows since:** 2023-11-16 low **139.52** → 2023-12-11 low **143.64** → 2024-01-04 low **144.05**. Each pullback has terminated above the prior one.
- **Prior swing highs:** 2023-12-18 close **154.07** / intraday high **154.85**; 2023-12-20 high **155.63**.
- **January reset:** close 153.38 (2023-12-28) → **144.57** (2024-01-04), a 5-session decline of **-5.74%**, with the heaviest volume of the slide on the final day (56.04M on 2024-01-04) while price closed near the session low — a classic exhaustion/distribution finish rather than an orderly grind.
- **Recovery:** **five consecutive higher closes** — 145.24 (01-05), 149.10 (01-08), 151.37 (01-09), 153.73 (01-10), **155.18 (01-11)**. That is **+7.34% off the 2024-01-04 close** in five sessions.
- **2024-01-11** printed the highest close in the entire 2023-04-01 → 2024-01-11 dataset and cleared the 2023-12-18/12-20 supply shelf at 154.07–155.63, with a high of **157.17**.

**Read:** this is a *breakout from a V-shaped higher low*, not a bounce inside a downtrend. The bullish case is structural, not just momentum.

---

## 3. Trend: all three averages aligned, but the short-term is stretched

| Average | 2024-01-11 | Price vs. average | Slope |
|---|---|---|---|
| close_10_ema | **151.1699** | **+2.65%** | Turning up (149.10 on 01-08 → 151.17 on 01-11) |
| close_50_sma | **146.7954** | **+5.71%** | Rising steeply (+0.45/day over the last week) |
| close_200_sma | **129.7673** | **+19.58%** | Rising steadily (+0.29/day) |

- **Stacking is textbook bullish:** 10-EMA (151.17) > 50-SMA (146.80) > 200-SMA (129.77), with price above all three.
- **Golden-cross regime intact:** the 50-SMA has been above the 200-SMA throughout the window, and the spread (146.80 − 129.77 = **17.03**) is near its widest of the period — a late-stage, trend-maturity condition, not an early reversal setup.
- **The 10-EMA reclaim is the actionable signal:** price lost the 10-EMA on 2024-01-02 (close 149.93 vs EMA 151.75) and regained it on 2024-01-09 (close 151.37 vs EMA 149.51); the EMA has now inflected higher, confirming the pullback is over.
- **Caution on extension:** +5.71% above the 50-SMA is meaningful for a stock with an ATR of only ~2% of price. Historically in this window AMZN has run this far above the 50-SMA — e.g., 2023-12-18 through 12-28 — and then mean-reverted modestly (the 2024-01-02/04 dip). So the *trend* is up, but *entry timing* is not ideal at 155.

---

## 4. Momentum: MACD has bottomed, positioning for a bullish cross

Momentum had visibly deteriorated and is now repairing in a measurable, datable way:

- **MACD line:** collapsed from **3.136** (2023-12-22) to a trough of **0.7788** (2024-01-08), and has since rebounded to **1.4619** (2024-01-11). That is **+0.68 in three sessions** — a sharp inflection, not a flat bottom.
- **Signal line:** **1.5259**. MACD (**1.4619**) remains **0.064 below** signal — the histogram is still negative.
- **Histogram:** **-0.06397**, the **fifth consecutive session of contraction** from the -1.2302 low on 2024-01-05 (-1.0481 → -0.7507 → -0.3894 → -0.0640). The crossover occurred *bearish* around 2023-12-29 (histogram flipped from +0.031 on 12-28 to -0.141 on 12-29).
- **Interpretation:** the bearish MACD cross is very likely to flip back bullish within 1–3 sessions at this rate of compression. Because the MACD line is already **above zero (1.46)**, a cross above signal would be a **zero-line bullish cross** — the higher-quality variant, indicating momentum resuming in the direction of the primary trend rather than a counter-trend blip.

**Tradeable nuance:** the histogram is *still negative on close of 2024-01-11*. A trader who requires confirmation should wait for the histogram to flip positive; a trader who front-runs it is accepting that price may need one more flat-to-down session.

---

## 5. RSI: headroom, not a warning — yet

- **RSI 62.79** on 2024-01-11, up from **40.23** on 2024-01-04 (never reaching the 30 oversold line) and **48.92** on 2024-01-03.
- That is a **+22.6 point recovery in five sessions** — an aggressive but not extreme thrust.
- **No bearish divergence is present** at this point: price made a higher high (155.18 vs 153.38 on 2023-12-28) while RSI made a higher high (62.79 vs 59.01). Divergence would require RSI to roll over while price makes new highs — watch for that on the next push into 157–160.
- **History in this window is instructive:** RSI peaked at **68.05** on 2023-12-18, price subsequently stalled three sessions and dropped 5.74%. The 65–70 band has been a reliable *fade-the-short-term-extension* zone for AMZN, while the 70+ level has not been reached since November. RSI at 62.8 means roughly one more strong up-day puts the stock in that friction zone.

---

## 6. Volatility and bands: compression → expansion, with price in the upper third of the envelope

- **ATR 3.1196** = **2.01% of the 155.18 close**.
- ATR compressed from **3.446** (2023-12-18) to a low of **2.806** (2023-12-28) — a holiday-period squeeze — then re-expanded to **3.120** as of 2024-01-11. The expansion aligns with the breakout (2024-01-11 range 153.12–157.17 = 4.05 points, ~1.3× ATR), which is the healthy pattern: expansion in the direction of the breakout.
- **Bollinger position:** upper band **157.2954**, middle **151.1565**, lower **145.0176**. Price at 155.18 sits at **82.8% of the band width** — upper third, pressing the upper band but *not* closing above it.
- Band width (157.30 − 145.02 = **12.28**, ~8.1% of the mid) remains moderately wide, so this is not a coiled squeeze about to explode; the more likely path is a grind toward the upper band (157.30) rather than a vertical extension.
- **Confluence alert:** the Bollinger middle band (**151.1565**) and the 10-EMA (**151.1699**) are essentially the same value, with VWMA (**150.8029**) just below. That is a **three-indicator support shelf at 150.80–151.17**. Any pullback that holds that band is a low-risk re-entry; a close below it invalidates the "breakout" characterization and re-frames the move as a range oscillation.

---

## 7. Volume: the weak link in the bullish case

- **VWMA 150.8029**, price **+2.90% above it** — the trend *is* volume-supported, and VWMA has just turned up (150.63 on 2024-01-10 → 150.80 on 2024-01-11) after drifting down from 151.25 on 2024-01-03. That inflection is a genuine positive.
- **But the breakout volume is not convincing.** 2024-01-11 volume was **49.07M** vs 44.42M (01-10) and 43.81M (01-09) — a rise of ~10–12%, nothing like a thrust. For context, the window has far heavier prints on much smaller price moves: 110.09M on 2023-12-15 and 125.31M on 2023-10-27.
- This is a **"new high without volume expansion"** — common in continued trends but it reduces the probability of immediate acceleration. It argues for scaling in and for tighter, structure-based stops rather than chase entries.

---

## 8. Actionable trade plan

**Bias: bullish, but buy pullbacks/breakout retests rather than the 155.18 print.**

**A. Trend-following continuation (preferred)**
- **Trigger:** a close above 2024-01-11's high of **157.17** with volume above ~50M, *or* a MACD histogram flip positive while price holds above 151.17.
- **Entry zone on retest:** **151.20–152.50** (10-EMA/Bollinger-mid/VWMA shelf, minus a small premium). This is the highest-reward-for-risk entry in the current configuration.
- **Stop:** **148.90** = 2× ATR below the 2024-01-11 close (155.18 − 2×3.12), or **below 146.15** (the 2024-01-08 low, which is also just beneath the rising 50-SMA at 146.80) for a wider swing hold.
- **Targets:** 157.30 (upper band) → ~160 (psychological/round level, band extension) → measure the 2024-01-04→01-11 leg (+10.62 points) from the 151.2 retest, implying ~161.8.

**B. Breakout chase (aggressive only)**
- Entry on a confirmed close > 157.17; stop at 153.10 (2024-01-11 low) — a tight ~2.6% stop but with high whipsaw risk given sub-average volume.

**C. Invalidation / short-side triggers**
- Close **below 150.80** (VWMA) with the 10-EMA rolling back down: the breakout is void, range 144–155 applies.
- Close **below 144.05** (2024-01-04 low) breaks the higher-low pattern; 50-SMA at 146.80 would already have failed, and the next references are the Bollinger lower band **145.02** (then-stale) and the 2023-12-11 low **143.64**.
- A **bearish RSI divergence** (RSI lower high vs price higher high) on a push to 157–160 would be the signal to take profits rather than add.

**D. Risk budgeting**
- With ATR at 3.12 (2.01% of price), a 1%-of-equity risk budget implies position size ≈ (0.01 × equity) / (2 × 3.12) per unit. Treat the 146.80 50-SMA as the "trend intact" line for sizing larger swing positions; the 151.17 shelf for tactical additions.

---

## 9. Key observations summary

| Dimension | Reading (2024-01-11) | Signal | Confidence |
|---|---|---|---|
| Last close / range | 155.18; O 155.04 H 157.17 L 153.12 | Highest close in dataset; cleared 154.07–155.63 supply | High |
| 10-EMA | 151.1699 (price +2.65%) | Reclaimed 2024-01-09 and inflecting up | High |
| 50-SMA | 146.7954 (price +5.71%) | Rising, structural support; extension is a caution | High |
| 200-SMA | 129.7673 (price +19.58%) | Primary uptrend confirmed; late-stage maturity | High |
| MACD / Signal / Hist | 1.4619 / 1.5259 / **-0.0640** | Still below signal, but 5 straight sessions of contraction; bullish zero-line cross imminent | Medium-High |
| RSI | **62.79** (from 40.23 on 01-04) | Room to 70; no bearish divergence yet; 65–70 has been a friction zone | Medium |
| Bollinger | Mid 151.1565 / UB **157.2954** / LB 145.0176 | Price at 82.8% of band width; upper band is first resistance | Medium |
| ATR | **3.1196** (2.01% of price) | Re-expanding from 2.806 (12-28) low; use for stops/sizing | High |
| VWMA | 150.8029 (price +2.90%) | Supportive and turning up, but breakout volume (49.07M) is unremarkable | Medium |
| Structure | Higher lows 139.52 (11-16) → 143.64 (12-11) → 144.05 (01-04) | Bullish; intact unless 144.05 breaks | High |
| Preferred action | Buy 151.20–152.50 retest; stop 148.90 or 146.15; targets 157.30 / ~160 / ~161.8 | — | — |
| Invalidation | Close < 150.80 (VWMA) voids breakout; < 144.05 breaks structure | — | — |

**Bottom line on AMZN:** the trend, the moving-average stack, the higher-low sequence, and a *bottoms-up* MACD histogram all point one way — up. What is missing is confirmation: the MACD histogram is still fractionally negative, RSI at 62.8 has limited short-term headroom before hitting the 65–70 friction band that rejected price in mid-December, price is 5.7% above the 50-SMA, and the new high came on only a modest volume uptick. The highest-expectancy plan is therefore **buy strength on a retest of the 150.80–151.20 confluence shelf (10-EMA + Bollinger mid + VWMA) rather than at 155.18**, with structural invalidation at 148.90/146.15 and a short-term ceiling at the 157.30 upper band.