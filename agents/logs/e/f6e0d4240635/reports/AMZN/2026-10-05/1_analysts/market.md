# AMZN — Multi-Timeframe Technical Assessment
**As of close 2026-10-05 | Last print $251.40**

---

## 0. Data verification

The verified snapshot for 2026-10-05 and the indicator series returned by `get_indicators` agree exactly on every value used below (close 251.40; 50SMA 256.93; 200SMA 241.51; 10EMA 250.26; MACD −1.9486; signal −2.0950; hist +0.1464; RSI 48.42; Boll mid 251.29, upper 258.52, lower 244.05; ATR 5.543; VWMA 250.83). **No discrepancies to flag.** All price levels, dates, and percentage changes below are computed from the tool's OHLCV rows only.

**Indicators selected (8 slots, non-redundant):** `close_10_ema`, `close_50_sma`, `close_200_sma`, `macd` (read with its `macds` signal and histogram), `rsi`, `boll` (read with `boll_ub`/`boll_lb` as one volatility construct), `atr`, `vwma`.

Rationale for this set: AMZN is in a **post-earnings-gap consolidation with contracting volatility**, where (a) trend direction is ambiguous across horizons, (b) risk must be sized off a shrinking ATR, and (c) a squeeze resolution is the dominant forward event. That mix requires the three-horizon MA stack to separate timeframes, MACD/RSI for momentum inflection versus exhaustion, the Bollinger set to quantify compression and define the breakout/invalidation rails, ATR for stop and size, and VWMA to test whether volume is confirming or diverging from price. Oscillators like stochrsi or a second volatility measure would be redundant here.

---

## 1. Regime diagnosis: compressed range inside a weakening medium-term uptrend

The single most important observation is that **realized volatility has collapsed while price has gone nowhere**. ATR has fallen from **9.59 on 2026-08-06 to 5.54 on 2026-10-05 (−42%)**, and Bollinger bandwidth has compressed from **41.0 points on 2026-08-26 (286.61 − 245.60) to 14.47 points today (258.52 − 244.05)** — roughly a two-thirds contraction. Bandwidth is now **~5.8% of spot**, an unusually tight envelope for a mega-cap that moved 15.3% in a single session on 2026-07-31.

Meanwhile spot at 251.40 sits **at 50.8% of the band width** — essentially on the 20-day mean (251.29). That is the definition of a coiled, directionless tape. The practical implication: **mean-reversion trades work until they violently stop working**, and the ATR says the eventual expansion will be fast relative to recent daily ranges.

---

## 2. Trend structure — three horizons, three different answers

**Long term (200SMA) — intact bullish.** The 200SMA has risen monotonically through the entire sample: 236.25 (2026-08-06) → 241.51 (2026-10-05), climbing roughly 0.05–0.13 points per session. Spot is **+4.10% above it**. The 50SMA sits **15.42 points above the 200SMA (6.4% spread)**, and that spread has *widened* from 11.21 points on 2026-08-06. The golden-cross structure is not merely intact, it is broadening. Nothing in the long-term data argues for a bearish strategic stance yet.

**Medium term (50SMA) — damaged but stabilizing.** Price has closed **below the 50SMA since roughly 2026-09-10** (that day: close 251.89 vs 50SMA 254.95) — about 18 consecutive sessions. Spot is **−2.15%** below it. However, the 50SMA itself has stopped falling: it bottomed at **256.087 on 2026-09-29** and has ticked up to **256.930** today (+0.84 over four sessions). This is mechanical — the low late-July prints (226.65 on 7/29) are rolling out of the window and being replaced by ~250 prints — but it means the medium-term benchmark is now a *rising* ceiling rather than a falling one. That is a materially different setup than mid-September.

**Short term (10EMA) — turning up.** The 10EMA bottomed at **249.66 on 2026-10-01** and has risen to **250.26**. Spot has closed above it two straight sessions (251.52 on 10/2, 251.40 on 10/5) after being below it continuously from 2026-08-12 through 2026-09-30. The short-term tape has stopped deteriorating.

**Net:** long-term up, medium-term consolidating below a rising 50SMA, short-term basing. This is a **"wait for resolution" structure, not a trend-following structure.**

---

## 3. Momentum — a fresh, unconfirmed bullish crossover inside negative territory

The MACD sequence tells the story precisely:

| Date | MACD | Signal | Histogram | Reading |
|---|---|---|---|---|
| 2026-08-11 | +8.43 (cycle peak) | 5.26 | +3.17 | Strong uptrend |
| 2026-09-08 | +0.118 | 1.239 | −1.12 | Rollover complete |
| 2026-09-09 | **−0.421** | 0.907 | −1.33 | **Crosses below zero** |
| 2026-09-29 | **−2.560 (trough)** | −1.903 | −0.657 | Max downside momentum |
| 2026-10-02 | −2.195 | −2.132 | −0.063 | Convergence |
| **2026-10-05** | **−1.949** | **−2.095** | **+0.146** | **Bullish crossover — day 1** |

Two nuances traders must not miss. First, **the bullish MACD crossover occurred today, 2026-10-05** — it is a one-session signal with zero confirmation. Second, **both lines remain deeply below zero** (−1.95 / −2.10). A crossover below the zero line is a *deceleration of a downtrend*, not an uptrend signal; historically these fail more often than zero-line crossovers and need price confirmation. The MACD line has, however, risen for four consecutive sessions off the 9/29 trough, which is genuine improvement.

**RSI at 48.42** is neutral — no edge from overbought/oversold. But the *path* matters: RSI printed **39.45 on 2026-09-16** and **41.24 on 2026-09-28**, both of which marked local price lows (245.96 and 246.15 closes), and has now recovered to 48.4 without the price making a higher high. Within this specific consolidation, the sample shows RSI ~40 acting as a tactical accumulation zone and RSI ~52–56 (52.7 on 9/21, 55.9 on 8/28) capping short-lived rallies. I present that as a description of the last eight weeks, not a validated rule.

---

## 4. Volume — sellers are losing conviction, buyers are not yet committed

VWMA is the cleanest read. It fell without interruption from **272.05 on 2026-08-20 to 250.77 on 2026-10-01** — a textbook distribution signature, with price below the volume-weighted average the entire way. It has now **flattened and ticked up to 250.83**, and spot (251.40) is marginally above it. That is the first sign since August that volume-weighted participants are no longer selling into strength.

Absolute volume supports "waning conviction, no accumulation": the 20-session average (2026-09-08 → 2026-10-05) is **~35.6M shares**, and today's 39.27M is only **~1.10×** that. Compare that to the conviction events: **129.1M on 2026-07-31**, **90.8M on 2026-08-03**, **49.5M on 2026-08-28** (a failed push to 267.56 that closed at 266.43 and gave it all back two sessions later). There is no evidence of institutional re-accumulation at 251 — just an absence of urgent selling.

**Structural overhead supply:** the 271–284 zone (2026-07-31 close 271.58, 2026-08-03 close 284.02, intraday high 287.20) was transacted on 90–129M share days. Holders from that window are underwater by 8–12%. That is the wall any advance must clear, and it explains why rallies keep dying in the high 250s.

---

## 5. Key levels (all tool-derived)

**Resistance ladder**
- **253.55–254.53** — the last two sessions' intraday highs (253.56 on 10/2, 254.53 on 10/5). Today's candle opened 250.19, spiked to 254.53, and closed at 251.40 — an **upper-shadow rejection**, so this is live, immediate supply.
- **256.93** — rising 50SMA.
- **258.45–259.50** — the decisive cluster: 258.52 upper Bollinger band, 258.45 close on 2026-09-21, 259.49 intraday high that day, 259.50 high on 2026-09-03.
- **266.43–267.56** — 2026-08-28 close and high (failed breakout).
- **271.58 / 284.02 / 287.20** — the July–August gap zone and all-time-relevant highs in this sample.

**Support ladder**
- **250.19–251.29** — today's low, the 20-day mean (251.29), the 10EMA (250.26) and VWMA (250.83) all stacked within 1.1 points. This is the pivot of the entire consolidation.
- **245.96–244.30** — 2026-09-16 close and low; the September floor.
- **244.05–244.73** — lower Bollinger band plus 2026-09-28 intraday low (244.73) and 9/29 low (245.14).
- **241.51** — 200SMA. **The line in the sand.**
- **238.00** (2026-06-10 close), then **232.79–233.66** (June/July lows).

---

## 6. Scenarios and probability weighting

**Base case — range persists (≈55%).** Price continues to oscillate in **244–259**, with the 250–251 cluster as the fulcrum. The squeeze has not yet produced a directional catalyst, MACD is unconfirmed, and volume is unremarkable. Chop between the rails.

**Bull resolution (≈25%).** A daily close **above 259.50 on volume ≥45M (≈1.3× the 20-day average)** confirms the squeeze upward and the fresh MACD cross. Path: 266.4 → 267.6, then the 271.6–284 supply wall. Note that the 50SMA (256.93) is *inside* the trigger zone — a close above 259.5 also reclaims the medium-term trend line, which is why 258.5–259.5 is the level that matters rather than 253.5.

**Bear resolution (≈20%).** A daily close **below 244.05** breaks the lower band and the September floor simultaneously. Targets 241.51 (200SMA), then 238.00, then 232.8. A 200SMA break would be the first structural long-term trend violation in this sample and should force a strategic de-risking regardless of the fundamental view.

---

## 7. Actionable plan

| Element | Specification |
|---|---|
| **Bias** | Neutral / range. No directional position justified at 251.40 (mid-band, RSI 48, unconfirmed MACD). |
| **Tactical long (range)** | Accumulate **246.00–248.00** (upper half of the lower band / September floor zone). Stop **below 242.50** (≈2×ATR, and under the 200SMA). First target **256.90 (50SMA)**, second **258.50**. |
| **Tactical short (range)** | Fade **257.50–259.00** with stop **above 260.50**. Target **251.30 (mid-band)**, then **246.00**. Do not short into the 250 cluster. |
| **Breakout long** | Trigger: daily close **>259.50 with volume >45M**. Stop **below 252.00**. Targets 266.4, 271.6, 284.0. |
| **Breakdown short** | Trigger: daily close **<244.00**. Stop **above 249.50**. Targets 241.5, 238.0, 232.8. |
| **Position sizing** | ATR = 5.54 (2.2% of spot). 1R ≈ **8.3 points** (1.5×ATR); 2R ≈ **11.1 points**. Size so that a 1.5–2×ATR stop equals ≤1% of account equity. **Risk per share is small — do not upsize because "it looks cheap"; the squeeze means the next 1-day range could expand 2–3×.** |
| **Risk flags** | (1) Fresh one-day MACD cross — treat as a hypothesis, not a signal. (2) Upper-shadow rejection at 254.53 today. (3) Overhead supply at 271–284 from 90–129M-share sessions. (4) A quarterly report is typically due in late October by AMZN's historical calendar (external knowledge, not tool-derived) — consider half-size or defined-risk options into that event. |

---

## 8. Summary table

| Dimension | Reading (2026-10-05) | Interpretation | Signal |
|---|---|---|---|
| Close | 251.40 (O 250.19 / H 254.53 / L 250.18) | Mid-range, upper-shadow rejection | Neutral |
| 10 EMA | 250.26 | Price above 2 sessions; EMA turning up | Mildly bullish |
| 50 SMA | 256.93 (rising off 256.09 on 9/29) | Price −2.15% below; 18 sessions under | Medium-term bearish |
| 200 SMA | 241.51 (rising) | Price +4.10% above; 50>200 spread 15.42 pts, widening | Long-term bullish |
| MACD / Signal / Hist | −1.949 / −2.095 / **+0.146** | Bullish cross **today**, still below zero | Early, unconfirmed |
| RSI | 48.42 | Neutral; up from 39.45 (9/16) and 41.24 (9/28) | Neutral |
| Bollinger (mid / ub / lb) | 251.29 / 258.52 / 244.05 | %B = 0.51; width 14.47 (5.8%) — severe squeeze | Coiled / breakout pending |
| ATR | 5.54 (−42% from 9.59 on 8/6) | Volatility contraction; 2.2% daily range | Size up stops, not size |
| VWMA | 250.83 (flattening after 272.05 on 8/20) | Price marginally above; selling pressure easing | Mildly constructive |
| Volume | 39.27M vs ~35.6M 20-day avg (1.10×) | No accumulation signature | Neutral |
| **Structure** | **244.05–259.50 range; 250–251 pivot** | **Wait for close beyond rails** | **Range / no-trade core** |

**Bottom line for AMZN:** the long-term trend (200SMA, golden-cross spread) is still up, but the medium-term trend has been broken since 2026-09-10 and the stock is now compressing inside a 15-point band with collapsing volatility. Today's MACD cross and the 10EMA reclaim are encouraging but one session old and below the zero line. The highest-expectancy action is **not to chase 251.40**, but to trade the rails: buy 246–248 / fade 257.5–259 with ATR-derived stops, and let a close above **259.50** or below **244.00** on expanding volume dictate the next directional commitment.