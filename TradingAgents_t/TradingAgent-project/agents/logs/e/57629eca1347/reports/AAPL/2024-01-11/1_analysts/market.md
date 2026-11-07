# AAPL — Multi-Timeframe Technical Report (as of 2024-01-11)

## 0. Data integrity check (done first)

I pulled the full daily OHLCV series (2023-06-01 → 2024-01-11) and then called the verified snapshot. **The two agree exactly**: the latest row in both is 2024-01-11 with O=186.54, H=187.05, L=183.62, C=185.59, V=49,128,400, and the snapshot's indicator values match the last values of each indicator time series I retrieved (e.g., `close_50_sma` 188.7174, `rsi` 42.1376, `macd` −1.6343, `macdh` −0.9782, `atr` 3.0429, `vwma` 187.2809). **No discrepancy to flag.** All levels below are drawn from tool output; where I do arithmetic (percentage moves, averages), I show the inputs.

---

## 1. The core narrative: a short-term corrective downtrend inside a still-intact long-term uptrend

The cleanest way to describe AAPL on 2024-01-11 is the **stacking order of its averages**, which is unusually orderly:

| Rank | Measure | Value (2024-01-11) | Position vs. close (185.59) |
|---|---|---|---|
| 1 | Bollinger middle (20 SMA) | 190.87 | +5.28 above |
| 2 | 50-day SMA | 188.72 | +3.13 above |
| 3 | VWMA | 187.28 | +1.69 above |
| 4 | 10-day EMA | 186.62 | +1.03 above |
| 5 | **Close** | **185.59** | — |
| 6 | 200-day SMA | 180.55 | −5.04 below |
| 7 | Bollinger lower band | 179.41 | −6.18 below |

Every short- and medium-term reference (10 EMA, VWMA, 50 SMA, 20 SMA) is **above** price; the only reference **below** price is the long-term 200-day SMA. That is the textbook signature of a *pullback within an uptrend* rather than a broken trend — but it is also an unambiguous statement that short-term control has passed to sellers.

Supporting trend evidence:
- **50 > 200 with a widening spread.** The 50-day SMA has risen every session in the sample: 185.97 (2023-12-27) → 186.63 (12-29) → 187.40 (01-05) → 188.41 (01-10) → 188.72 (01-11). The 200-day SMA is also rising: 179.09 (12-27) → 180.02 (01-05) → 180.55 (01-11). The spread (188.72 − 180.55 = **+8.17, ~4.5%**) is wider than it was a month ago (188.72 vs. 175.27 − … i.e., on 2023-12-01 it was 179.45 − 175.27 = +4.18). The long-term uptrend is *not* being threatened by the pullback.
- **But price lost the 50-day on 2024-01-02 and has not reclaimed it.** Every close from 2023-11-13 through 2023-12-29 was above the then-current 50-day SMA; every close from 2024-01-02 (185.64 vs. 50-day 186.84) through 2024-01-11 (185.59 vs. 188.72) has been below it. That is a regime shift at the intermediate horizon.
- **Lower highs are still in force.** Sequence of daily highs after the peak print: 199.62 (12-14) → 196.95 (12-19) → 197.68 (12-20) → 195.41 (12-22) → 194.66 (12-28) → 194.40 (12-29) → 188.44 (01-02) → 185.60 (01-08) → 186.40 (01-10) → 187.05 (01-11). The last three highs have ticked *up*, which is a tentative stabilization, but 187.05 remains **7.35 below** the 12-29 high (194.40).
- **Drawdown from the peak close:** 198.11 (2023-12-14) → 185.59 = −12.52 points, **−6.32%**. Year-to-date: 192.53 (2023-12-29) → 185.59 = **−3.60%**. From the 2023-10-26 close of 166.89 the stock is still **+11.20%**, which is why the 200-day remains far below.

Note: 199.62 (2023-12-14) is the highest print *in the returned data window* (2023-06-01 onward); I am not asserting it is an all-time high.

---

## 2. Why these 8 indicators (and not others)

The setup is a **pullback in an uptrend with decelerating downside momentum and elevated volatility** — so I need (a) two trend anchors at different speeds, (b) a responsive mean to time entries, (c) a momentum oscillator pair to judge whether the correction is exhausting, (d) a volatility unit for stops/sizing, and (e) one volume-weighted confirmation. I deliberately avoided redundancy:

1. **close_200_sma** — strategic trend anchor (is the uptrend intact?). Slow by design, used only for regime.
2. **close_50_sma** — the intermediate trend line price just lost; the key "line in the sand" for the correction.
3. **close_10_ema** — the short-term mean, used to define the immediate downtrend and to time any reclaim.
4. **macd** — trend-following momentum; the zero-line break is the definitive evidence of the momentum shift.
5. **macdh** — the *rate of change* of that momentum; this is where the actionable information is right now (four consecutive days of improvement).
6. **rsi** — bounded oscillator to catch the oversold reset and to test whether the bounce has real thrust (50 midline test). Complements MACD because it is price-normalized and doesn't share MACD's EMA construction.
7. **atr** — converts the elevated volatility into stop distance and position size; also a sanity check on whether daily ranges are expanding or contracting.
8. **vwma** — the only volume-integrated metric; tells us whether the volume-weighted "average owner" is in profit or loss, which is precisely what distinguishes a healthy shakeout from distribution.

Deliberately excluded: `macds` (fully implied by macd + macdh; macdh is the more informative of the pair for this phase), `boll`/`boll_ub`/`boll_lb` as *selected* inputs (I reference the snapshot's band values as corroboration only — they'd triple-count the 20-day mean already covered), and the snapshot's `mfi` (the reported 0.256 is not a plausible MFI reading in a 0–100 scale, so I do not rely on it). Also no Stochastic/StochRSI — pure redundancy with RSI in a market this directional.

---

## 3. Indicator-by-indicator read

### 3.1 MACD — the momentum regime has flipped, but the bleeding has stopped
- MACD crossed **below zero on 2024-01-04** (from +0.055 on 01-03 to −0.702 on 01-04) and has deteriorated only marginally since: −1.346 (01-05) → −1.485 (01-08) → −1.611 (01-09) → −1.607 (01-10) → **−1.634 (01-11)**. It is essentially flat over the last three sessions — i.e., the *decline in momentum has stopped accelerating*.
- Signal line (snapshot) = **−0.656**, so MACD sits **0.978 below** its signal. The bearish crossover happened well before the zero-line break: the histogram first went negative on 2023-11-30 (−0.011) and has been predominantly negative since 2023-12-19.
- **Histogram: four consecutive improving sessions** — −2.045 (01-05, the low) → −1.747 (01-08) → −1.499 (01-09) → −1.196 (01-10) → **−0.978 (01-11)**. This is a ~52% retracement of the histogram's negative extreme. It is the single most constructive data point in this report, and it typically *precedes* the MACD/signal bullish crossover. Extrapolating the recent slope (~+0.22/day), a crossover is plausible within roughly 4–5 sessions **if** price stops making lower closes — but extrapolation is not a forecast, and any new low resets it.

### 3.2 RSI — a textbook weak bounce off oversold
- RSI bottomed at **28.79 on 2024-01-05** (the only sub-30 reading in the sample), then jumped to 41.34 (01-08), 40.60 (01-09), 43.33 (01-10), and **42.14 (01-11)**.
- The critical observation: RSI has now spent **seven consecutive sessions below 50** (from 35.37 on 01-02), and the recovery has **stalled in the low-40s** while price has actually risen (+2.43% from 181.18 to 185.59). Price rallying while RSI plateaus just under 50 = buyers are making price progress but not momentum progress. That is characteristic of a **counter-trend bounce**, not a new leg up.
- Prior regime for contrast: RSI was consistently 60–73 through October–December (e.g., 73.13 on 2023-11-20, 70.02 on 12-08, 69.49 on 12-13) — the overbought readings that preceded the December peak. There is a large "air gap" between current momentum and the prior uptrend's momentum.

### 3.3 Bollinger context (corroboration from the verified snapshot)
- Middle **190.87**, upper **202.32**, lower **179.41** → band width 22.91, or **~12.0% of the middle band**. That is a wide envelope, consistent with the December blow-off into 199.62 followed by the January air-pocket drop.
- Price at 185.59 sits at **%B ≈ 0.27** ((185.59 − 179.41) / 22.91) — lower third of the envelope, but **6.18 above the lower band**. Translation: no longer oversold on a band basis, but no band-walk strength either. The lower band at **179.41** coincides almost exactly with a 2×ATR stop from current price (185.59 − 6.09 = 179.50), which strengthens 179.4–180.2 as a meaningful downside reference zone.

### 3.4 ATR — volatility expansion argues for smaller size, wider stops
- ATR(14) = **3.043**, ≈ **1.64% of the 185.59 close**.
- The path matters: ATR compressed to **2.567 on 2023-12-28**, then expanded to 3.008 (01-02), 3.071 (01-08) and 3.043 (01-11). Volatility roughly **+18%** off the late-December trough (3.043/2.567 = 1.185).
- Practical consequences: (i) a "normal" day is now ~±3 points, so a 1.5–2.0 point stop is inside the noise; (ii) the 2024-01-11 range (187.05 − 183.62 = **3.43**) exceeded 1 ATR, and 01-02's range (188.44 − 183.89 = **4.55**) was ~1.5 ATR — wide-range, two-way sessions; (iii) with ATR rising, *reduce* share count rather than tighten stops.

### 3.5 VWMA — the volume-weighted owner is underwater
- VWMA = **187.28**, above the 185.59 close by 1.69 (**−0.90%** from the VWMA).
- More importantly, VWMA has rolled over hard: **195.53 (12-26) → 195.36 (12-29) → 194.59 (01-02) → 191.21 (01-05) → 188.03 (01-10) → 187.28 (01-11)**. It peaked at 195.53 on 2023-12-26 and has fallen ~8.25 points in 11 sessions. VWMA now undercuts the 50-day SMA (188.72) — meaning recent volume has been transacted at *lower* prices than the simple average would suggest, i.e., **distribution on the way down**. A close back above 187.3 would be the first objective sign that this has stopped.

### 3.6 Volume behavior — the "tell" of this correction
From the returned OHLCV:
- **Down days carried the volume.** 2024-01-02 (gap-down, −3.58%: 192.53 → 185.64) printed **82,488,700** shares — excluding the 2023-12-15 quarterly-expiry/index-rebalance print of 128.5M, that is the largest single-session volume in the entire returned window back to **2023-09-15 (109.3M)**. 2024-01-04 printed 72.0M on a −1.27% day (181.91 from 184.25).
- **The rebound came on lighter volume.** 2024-01-08 through 01-11: **59.1M → 42.8M → 46.8M → 49.1M**, with 01-09's 42.8M the lightest of the four. The simple average of the last 21 sessions (computed from the returned volumes) is ≈**56.1M**, so the entire bounce has traded **below average** — 01-11's 49.1M is ~12% light.
- Contrast with the December advance: 12-13 70.4M, 12-14 66.8M on up days. The buying that built the December high had volume behind it; the current bounce does not.
- **Verdict:** heavy-volume decline + light-volume rally = classic *distribution / weak-rally* pattern. It does not preclude a tradeable bounce, but it argues the bounce should be **sold into supply, not chased**.

### 3.7 Price action on the snapshot day itself (an important intraday clue)
2024-01-11: O 186.54, H **187.05**, L **183.62**, C 185.59, V 49.13M.
- This is an **outside day** — high 187.05 > 01-10's high 186.40, and low 183.62 < 01-10's low 183.92 — that **closed below both its open and the prior close** (186.19).
- The high of 187.05 *poked above* the 10-day EMA (186.62) and stopped just short of the VWMA (187.28) before reversing. In other words, the single most obvious resistance cluster (186.6–187.3) was **tested and rejected on the same session**. That is a failed breakout attempt, not a breakout.
- The close at 185.59 is in the upper-middle of the day's 3.43-point range, so it was not a collapse — but the session's net message is "supply overhead."

---

## 4. Levels that matter (all derived from tool output)

**Resistance, in order of proximity:**
| Level | Source | Why it matters |
|---|---|---|
| 186.62 | 10-day EMA (01-11) | Immediate lid; rejected intraday on 01-11 |
| 187.28 | VWMA (01-11) | Volume-weighted breakeven; short-term control line |
| 188.72 | 50-day SMA (01-11) | Lost 01-02; first *meaningful* trend reclaim |
| 190.87 | Bollinger middle | 20-day mean; bearish while below |
| 192.53 / 187.15 | 2023-12-29 close / 2024-01-02 open | Unfilled gap zone from the 01-02 gap-down |
| 194.40–194.66 | 2023-12-28/29 highs | Top of the December lower-high sequence |

**Support, in order of proximity:**
| Level | Source | Why it matters |
|---|---|---|
| 183.62 | 2024-01-11 low | Nearest structural low; break = outside-day follow-through |
| 181.18 / 180.17 | 2024-01-05 close / low | The low of this correction |
| 180.55 | 200-day SMA | **The** long-term trend line — the line that defines the regime |
| 179.41 | Bollinger lower band | ~2×ATR (179.50) — confluence zone |
| 176.6–177.6 | Nov 2–3 closes (177.57, 176.65) | Next shelf below the 200 SMA if it fails |

Note: 180.17 (01-05 low) and 180.55 (200-day SMA) form a **0.38-point confluence**; a decisive close below ~180.2 would be a genuine long-term trend break, not a wiggle.

---

## 5. Actionable framing

**Base case (highest probability given the evidence): range/consolidation between ~180 and ~189.** The long-term uptrend (50 > 200, both rising, price above the 200) caps downside; the loss of the 50-day, negative MACD, sub-50 RSI and light-volume rally cap upside. The improving MACD histogram says the *easy* short is over.

**Bullish trigger (needs confirmation, don't front-run it):**
- Daily **close above 187.28 (VWMA)** — ideally above **188.72 (50 SMA)** — on volume ≥ **56M** (the 21-session average) and with **MACD histogram crossing above zero**.
- Staged targets: 190.87 (Boll middle) → 192.53 (gap fill) → 194.4–194.7 (December highs).
- Invalidation: a close back below 183.62 after such a trigger.
- Note that 01-11 *already* probed 187.05 and failed — so a first attempt at this zone failing again would be expected; the signal is a *close*, not a wick.

**Bearish trigger:**
- Daily **close below 183.62** (outside-day low). Then 181.18/180.17, with the **200-day SMA at 180.55 as the decision point**.
- A close below ~180.2 opens 179.41 (lower band) and then the 176.6–177.6 shelf; with ATR at 3.04, that move is roughly 1.5 ATR away and could occur in 2–3 sessions.
- Invalidation: a reclaim of 186.6 (10 EMA).

**Risk management (using the tool-reported ATR of 3.043, 1.64% of price):**
- Stop distance: **1.5–2.0× ATR = 4.56–6.09 points**. A long entered near 185.6 would need a stop under ~181.0–179.5, which sits *below* the 200-day SMA — i.e., a long here is really a bet on the 200-day holding, and should be sized as such.
- Position sizing: for a 1.0% account risk with a 6.09-point (2×ATR) stop, shares = (0.01 × equity) / 6.09. For a $1,000,000 book that is ~164 shares (~$30,500 notional, ~3% of equity). The rising ATR means the *same* dollar risk buys fewer shares than it did on 2023-12-28 (ATR 2.567).
- Preference: **wait for confirmation rather than average into a light-volume bounce.** The volume asymmetry is the strongest argument against aggressive dip-buying at 185.6.

**What would change the view:**
1. A close above 188.72 with above-average volume → flip to constructive, correction likely over.
2. A close below 180.55 (200 SMA) → flip to strategic bearish; the 50/200 spread begins compressing and the multi-month uptrend is in question.
3. MACD histogram turning back down from here (i.e., a new lower low in the histogram) → the four-day improvement was a false dawn; expect a retest of 181.18.

---

## 6. Summary table

| Dimension | Reading (2024-01-11) | Interpretation | Signal |
|---|---|---|---|
| Close / range | 185.59; H 187.05, L 183.62 (outside day), V 49.1M | Failed test of 186.6–187.3; closed below prior close | Bearish short-term |
| Long-term trend | 200 SMA 180.55, rising; price +2.8% above | Uptrend intact, not yet threatened | Bullish (strategic) |
| Intermediate trend | 50 SMA 188.72, rising; price 3.13 below | Lost 50 SMA on 2024-01-02; not reclaimed | Bearish (tactical) |
| Short-term trend | 10 EMA 186.62, falling from 195.04 (12-15) | Lower highs since 12-14 (199.62 → 187.05) | Bearish, decelerating |
| MACD / Signal | −1.634 / −0.656 | Below zero and below signal since 01-04 | Bearish regime |
| MACD histogram | −0.978, 4th straight improvement (−2.045 low) | Downside momentum decelerating; crossover pending | Early bullish turn |
| RSI | 42.14 (from 28.79 on 01-05) | 7 straight closes < 50; bounce stalling below midline | Neutral/weak |
| Bollinger | Mid 190.87 / UB 202.32 / LB 179.41; %B ≈ 0.27 | Wide bands (12% of mid); no band-walk | Neutral |
| ATR | 3.043 (1.64% of price), up from 2.567 on 12-28 | Volatility expanding → smaller size, wider stops | Risk-off tilt |
| VWMA | 187.28, down from 195.53 (12-26); price below | Volume-weighted owner underwater = distribution | Bearish |
| Volume pattern | 82.5M on 01-02 decline vs. 42.8–59.1M on the bounce | Heavy selling, light buying | Bearish |
| Key resistance | 186.62 → 187.28 → 188.72 → 190.87 → 192.53 | Stacked supply overhead | — |
| Key support | 183.62 → 181.18/180.17 → **180.55 (200 SMA)** → 179.41 | 200 SMA is the regime line | — |
| Overall stance | Corrective pullback in an intact uptrend; momentum bottoming but unconfirmed | Avoid chasing the light-volume bounce; trade the 180.5–188.7 range edges with ATR-based risk | **Neutral with a slight bearish tactical bias** |

*All figures above come from the verified snapshot of 2024-01-11 and the retrieved OHLCV/indicator series. Percentage moves and averages are simple arithmetic on those printed values; no historical backtest, "validated" support bounce, or unobserved price level has been asserted.*