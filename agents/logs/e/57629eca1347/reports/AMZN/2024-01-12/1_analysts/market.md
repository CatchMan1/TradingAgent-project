# AMZN — Multi-Indicator Trend & Tactical Assessment
**As of the close of Friday, 2024-01-12** | Data vendor: B-project frozen OHLCV | Verified snapshot used as source of truth

---

## 0. Data verification note

The raw OHLCV pull (`get_stock_data`) and the `get_verified_market_snapshot` agree **exactly** on the 2024-01-12 row and on every indicator value I cite (e.g., MACD 1.64298, MACD histogram 0.093688, RSI 61.267467, ATR 3.053154, VWMA 150.936484, 50-SMA 147.226, 200-SMA 130.054, 10-EMA 151.797). No reconciliation or discrepancy flag was required. One item I deliberately excluded: the snapshot also reports an `mfi` of 0.505215, whose scale (0–1 vs 0–100) is ambiguous in this feed, so I made no money-flow claim based on it.

**Latest verified session (2024-01-12):** Open 155.39 | High 156.20 | Low 154.01 | Close **154.62** | Volume 40.48M | Split 1.0 | Dividend 0.0.

---

## 1. Indicator selection (8 of the offered set) and rationale

| Indicator | Why selected for *this* market context |
|---|---|
| **close_10_ema** (151.797) | The rally is fast and shallow-pullback in character; a responsive average is the cleanest way to time entries where dips are only 1–3 sessions long (see the 2024-01-04 → 2024-01-12 recovery). |
| **close_50_sma** (147.226) | Primary intermediate trend spine and the level that has contained every meaningful pullback since November; also separates "healthy pullback" from "trend break." |
| **close_200_sma** (130.054) | Strategic trend benchmark and extension gauge (price is ~18.9% above it — a mean-reversion risk input, not a trading signal). |
| **macd** (1.643) | Captures the medium-term momentum inflections that produced the November top and the early-January reset. |
| **macdh** (0.0937) | Directly answers "is the momentum crossover real or a whipsaw?" — critical here because this oscillator has flipped signs repeatedly. Chosen instead of `macds`, since the signal line is implied by the MACD/histogram pair (avoids redundancy). |
| **rsi** (61.267) | The advance is unaccompanied by an overbought extreme; RSI also mapped the 2024-01-04 momentum low (40.2) that preceded the current leg. |
| **atr** (3.053) | Position sizing and stop placement: with price in the 150s, a stop measured in % is meaningless — ATR is ~2.0% of price and *contracting* while price rises. |
| **vwma** (150.936) | The only volume-integrated input: it tests whether the January advance is being confirmed by where volume actually traded, and it now doubles as a support level. |

Deliberately excluded: `boll`/`boll_ub`/`boll_lb` were not re-pulled as a time series but their verified values (mid 151.445, upper 157.669, lower 145.222) are used from the snapshot; `stochrsi`/MFI would duplicate the RSI message; `macds` duplicates the MACD/histogram information.

---

## 2. Trend structure — fully stacked, but extended

The moving-average stack on 2024-01-12 is textbook bullish and in the correct order:

**Price 154.62 > 10-EMA 151.797 > 50-SMA 147.226 > 200-SMA 130.054**

- Price is **+1.86%** above the 10-EMA, **+5.02%** above the 50-SMA, and **+18.89%** above the 200-SMA.
- The 50-SMA is **+13.2%** above the 200-SMA (spread 17.17), so the golden-cross regime is long established, not nascent. Even on the earliest row available for both series (2023-11-13), 50-SMA 133.16 already sat well above 200-SMA 119.59 — this is a mature uptrend, not a fresh crossover to trade.
- **Slopes are uniformly positive and accelerating short-term:** 50-SMA rose from 143.48 (2024-01-02) to 147.23 (+3.75, +2.6% in 7 sessions); 200-SMA from 127.98 to 130.05 (+1.6%). The 10-EMA *fell* from 152.20 (2023-12-28) to a trough of 149.10 (2024-01-05 and 2024-01-08) and has now reversed back up to 151.80 — a completed short-term momentum reset, not a trend reversal.
- **Swing structure:** higher highs (2023-11-20 146.63 → 2023-11-27 149.26 → 2023-12-18 154.85 → 2023-12-20 155.63 → 2024-01-11 **157.17**) with higher lows (2023-09-27 123.04 → 2023-10-26 118.35 → 2023-12-04 142.81 → 2024-01-04 144.05 → 2024-01-12 154.01).
- **Magnitude:** +25.9% from 122.77 (2023-06-01) to 154.62, and **+29.3%** off the 2023-10-26 close of 119.57. The most recent week was the strongest: **+6.46%** from the 2024-01-05 close (145.24).

**The nuance:** the 18.9% premium to the 200-SMA and 5.0% premium to the 50-SMA mean the trend is *extended*, and 2024-01-12's inside day (high 156.20 < 157.17; low 154.01 > 153.12) says the market is pausing at the highs rather than accelerating. Trend-aligned, but not a low-risk chase entry.

---

## 3. Momentum — the key tension in this setup

**MACD just generated a fresh bullish crossover, but it is a weak one, and momentum has not confirmed the new price high.**

- MACD line: 1.643 vs signal 1.549; **histogram turned positive at +0.0937 on 2024-01-12** after being negative since 2023-12-29 (trough −1.230 on 2024-01-05). The MACD line bottomed at 0.779 (2024-01-08) and has risen four straight sessions.
- **Whipsaw warning:** over the last six weeks the histogram has crossed zero four times — negative from 2023-11-30, positive 2023-12-18 through 2023-12-28, negative 2023-12-29 through 2024-01-11, positive again 2024-01-12. The signal with the *highest* information content here is confirmation over the next 2–3 sessions, not the crossing day itself.
- **Momentum divergence (the most important caveat):** the 2024-01-11 close of 155.18 was the highest close in the sample, yet MACD was 1.462 there versus **2.732 on 2023-12-18** (close 154.07), and RSI was 62.79 versus **68.05** on 2023-12-18. New price high, lower momentum high. That is a mild bearish divergence — consistent with a grinding, narrow advance rather than an explosive one.
- **RSI 61.27** sits in the constructive middle zone: below the 70 overbought threshold, well above 50. Note the shape of the recent RSI path: 52.9 (01-02) → 48.9 (01-03) → **40.2 (01-04, the leg low)** → 51.7 → 56.2 → 60.4 → 62.8 → 61.3. RSI bottomed at ~40 rather than 30 — a hallmark of a strong uptrend where pullbacks are shallow. RSI has not exceeded 68.05 in the entire visible window, i.e., this leg is *not* being driven by a blow-off reading.

**Interpretation:** the momentum configuration supports continuation, but the *quality* of the signal is medium, not high. Treat a close back under the 10-EMA with a negative histogram over the coming sessions as a whipsaw confirmation rather than a surprise.

---

## 4. Volatility & bands — orderly, coiled, with defined risk

- **ATR 3.053** = **1.97% of price**. ATR has *fallen* from 3.726 (2023-11-15) and 3.130 (2023-12-01) while price made new highs — volatility contraction inside an uptrend, which generally favors trend continuation over breakdown.
- ATR-implied reference levels from close 154.62: 1×ATR = **151.57** (coincides with the 20-SMA/10-EMA cluster); 2×ATR = **148.51** (just above the 2024-01-09 low of 148.21).
- **Bollinger (verified 2024-01-12):** mid 151.445, upper **157.669**, lower **145.222**. Bandwidth is 12.45, or **8.22% of the mid** — wide, i.e., the tape is already moving. **%B = 0.755**: price is in the upper quarter of the band but *did not* close at/above the upper band. The 2024-01-11 intraday high of 157.17 effectively tagged the upper band (157.67) and was rejected — a legitimate, data-supported resistance observation (not a claimed historical bounce).
- Combination read: wide bands + falling ATR + price just under the upper band = a **coiled consolidation at the top of a range**, with 157.2–157.7 as the ceiling and 151.4–151.6 as the floor of the current micro-range.

---

## 5. Volume — the weak link in the bullish case

- VWMA 150.936; price is **+2.44%** above it. VWMA rose from 144.63 (2023-11-29) to 151.25 (2024-01-03), then **flattened and dipped** to 150.63 (2024-01-10) before ticking up to 150.94 by 2024-01-12. Price reclaimed VWMA on 2024-01-08 and has stayed above it — volume-weighted buyers are in profit.
- **But volume is not expanding on the breakout.** The 2024-01-11 session that printed the highest close and highest high of the dataset drew 49.07M shares; the 2024-01-04 capitulation day drew 56.04M; the 2023-12-15 quad-witching session drew 110.09M. My computed 20-session average volume (2023-12-14 → 2024-01-12) is **≈46.8M**.
- **2024-01-12 volume was 40.48M — about 86% of that average, and the lowest volume of any 2024 session** (47.3M, 49.4M, 56.0M, 45.2M, 46.8M, 43.8M, 44.4M, 49.1M, 40.5M). Pullbacks on declining volume are benign; breakouts on declining volume are suspect. The current pattern is the former — but it leaves the upside unconfirmed.
- **Confirmation threshold:** an upside break should be accompanied by volume ≥ 50M (above the top of the recent 43–49M cluster, excluding the 56M event day) to be treated as institutional participation rather than drift.

---

## 6. Actionable levels (all derived from verified OHLCV)

**Resistance**
1. **156.20** — 2024-01-12 high (immediate trigger).
2. **157.17** — 2024-01-11 high, the dataset high.
3. **157.67** — Bollinger upper band (verified 2024-01-12); the 156.2–157.7 zone is a confluent supply shelf.

**Support**
1. **154.01** — 2024-01-12 low (inside-day floor).
2. **153.73–155.04** — **unfilled upward gap** from 2024-01-11 (open 155.04 vs 2024-01-10 close 153.73); the 2024-01-12 low of 154.01 held above it.
3. **153.12 / 151.71–151.88** — 2024-01-11 low; 2024-01-09 high and 2024-01-10 low.
4. **151.45–151.80** — the key cluster: 20-SMA 151.445, 10-EMA 151.797, and 1×ATR 151.57. Losing this on a closing basis would neutralize the short-term trend.
5. **150.94** — VWMA.
6. **148.21–148.39** — 2024-01-09 low / 2024-01-02 low; ~2×ATR.
7. **147.23** — 50-SMA (intermediate trend line in the sand).
8. **145.22** — Bollinger lower band; **144.05–144.57** — 2024-01-04 low / close.

---

## 7. Scenarios and plan

**A. Base case — bullish continuation (highest-probability, needs a volume trigger).** A close above **156.20** with volume ≥ 50M opens 157.17 → 157.67, and a decisive close above 157.67 puts the price in a blue-sky extension where the 1×ATR (3.05) step-ladder from the breakout close is the only guide. Stop: below the breakout day's low or below 153.12. Do **not** pre-empt the trigger — with MACD diverging and volume contracting, breakout failure risk is real.

**B. Preferred risk-adjusted entry — buy the pullback into 151.45–152.00.** This is where the 10-EMA, 20-SMA and 1×ATR converge. Stop: **148.00–148.20** (below the 2024-01-09 low and 2×ATR), i.e., roughly 3.5 points / ~2.3% of risk. Reward to 157.2 is ~5.2 points — a ~1.5:1 setup that improves to ~2.4:1 if targeting 157.67. RSI holding above ~45 on such a dip would be the quality filter (RSI already demonstrated 40.2 as its January floor).

**C. Bear/invalidations.** (i) A close below **151.45** (20-SMA) with a MACD histogram flipping negative = failed crossover, target 148.2. (ii) A close below **147.23** (50-SMA) = intermediate trend damage; the 10-EMA would then be below the 50-SMA and the "buy every dip" regime is over. (iii) The 18.9% extension above the 200-SMA means any macro/rate shock has a long runway back to 147/130 — size positions accordingly (a 1×ATR stop is only ~2% wide, so position size should be scaled to ATR, not to a fixed dollar stop).

**Risk-management specifics given ATR 3.05:** use 1.5–2.0 ATR stops (4.6–6.1 points). With ATR contracting, volatility-based sizing will *increase* share count for the same dollar risk versus November — be intentional about that. Event risk: AMZN's Q4 FY2023 report lands in the late-January/early-February window; the tools here contain no earnings-date data, so any position carried into that window is exposed to a gap far larger than 1 ATR (note the 2023-08-04 post-earnings session: open 141.06 vs prior close 128.91, a +9.4% gap).

---

## 8. Summary judgement

Constructive but late-stage-short-term. The primary trend (50 > 200, both rising; higher highs and higher lows since September) is unambiguous and the recent pullback was resolved in five sessions with RSI never breaking 30 — a strong-trend signature. Against that: price is 18.9% above the 200-SMA, MACD is making a lower high against a higher price high, the histogram just crossed positive on the first try after three failed crosses, and the breakout volume is the lightest of 2024. That combination argues for **staged exposure: partial size on strength above 156.20 with volume, with a reserve for the 151.5–152.0 cluster**, and a hard disregard for the bullish case below 147.23.

---

## 9. Key points table

| Dimension | Reading (2024-01-12) | Signal | Actionable level / note |
|---|---|---|---|
| Verified close | 154.62 (O 155.39 / H 156.20 / L 154.01) | — | Inside day vs 2024-01-11 |
| 10-EMA | 151.797 (rising after 149.10 trough) | Bullish, short-term reset complete | 1st support; loss neutralizes momentum |
| 50-SMA | 147.226 (+3.75 in 7 sessions) | Bullish, mature uptrend | Trend line in the sand |
| 200-SMA | 130.054 | Bullish | Price +18.89% above = extension risk |
| MA stack | 154.62 > 10-EMA > 50-SMA > 200-SMA | Strongly bullish | 50/200 spread 17.17 (+13.2%) |
| MACD / Signal | 1.643 / 1.549 (hist +0.0937) | Fresh bullish cross, low quality | 4th zero-cross in 6 weeks → demand confirmation |
| Momentum divergence | Jan-11 close high 155.18 vs Dec-18 RSI 68.05 → 62.79; MACD 2.732 → 1.462 | Mildly bearish | Watch for failure at 156–157.7 |
| RSI | 61.267 (Jan-04 low 40.2) | Constructive, not overbought | >45 on dips = trend intact |
| Bollinger | Mid 151.445 / UB 157.669 / LB 145.222; %B 0.755; width 8.22% | Upper-band, wide, coiled | 157.67 = ceiling; 151.45 = floor |
| ATR | 3.053 (1.97% of price), contracting | Orderly trend | 1×ATR 151.57; 2×ATR 148.51 |
| VWMA | 150.936 (price +2.44% above; slope re-turning up) | Confirming, but soft | Reclaim held since 2024-01-08 |
| Volume | 40.48M vs ~46.8M 20-session avg (86%); lowest of 2024 | **Not confirming** | Break needs ≥50M |
| Unfilled gap | 153.73 → 155.04 (2024-01-11) | Support shelf | 2024-01-12 low 154.01 held above it |
| Upside triggers | 156.20, 157.17, 157.67 | Breakout levels | Staged entry; stop < breakout low |
| Downside invalidation | 151.45 / 148.21 / 147.226 | Tiered | Below 147.23 = trend damage |
| Risk sizing | 1.5–2.0 ATR = 4.6–6.1 pts; earnings gap risk (no earnings date in tool data) | Caution | Scale size to ATR, not fixed $ |