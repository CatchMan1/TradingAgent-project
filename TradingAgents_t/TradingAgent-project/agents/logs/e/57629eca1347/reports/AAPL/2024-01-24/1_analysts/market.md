# AAPL — Multi-Indicator Technical Review
**As-of date:** 2024-01-24 (last completed session) | **Close:** 194.50 | **Data window reviewed:** 2023-07-03 → 2024-01-24 (142 sessions)

---

## 1. Snapshot verification (source of truth)

The verified snapshot for 2024-01-24 is fully consistent with the historical series I pulled (`get_stock_data`) and with every indicator series returned by `get_indicators` — **no discrepancies to flag**. All values below are from the verified snapshot:

| Field | Value (2024-01-24) |
|---|---|
| Open / High / Low / Close | 195.42 / 196.38 / 194.34 / **194.50** |
| Volume | 53,631,300 |
| close_50_sma | 190.531 |
| close_200_sma | 181.602 |
| close_10_ema | 190.409 |
| macd / macds / macdh | 0.591 / −0.534 / **+1.124** |
| rsi | 60.92 |
| boll (20 SMA) / boll_ub / boll_lb | 188.188 / 197.622 / 178.754 |
| atr | 3.179 |
| vwma | 186.772 |

Verified cross-checks: MACD − signal = 0.591 − (−0.534) = +1.124 ✔; Bollinger mid + 2σ / − 2σ = 197.62 / 178.75 ✔.

---

## 2. Indicators selected (8) and why they fit this market context

AAPL is in a **post-correction, V-shaped recovery inside an intact primary uptrend**, testing overhead December supply on **fading volume**. That combination needs (a) trend scaffolding, (b) momentum confirmation, (c) band/volatility position, (d) risk scaling, (e) volume-quality checks. I avoided redundant pairs (no MACD-signal + histogram + MACD triple; no RSI + stochastic).

1. **close_50_sma** — the regime line the pullback never broke; rising slope quantifies trend health.
2. **close_200_sma** — strategic trend/regime anchor; confirms the golden-cross structure is intact.
3. **macd** — momentum regime shift: zero-line cross and signal cross are the cleanest confirmation of the Jan 18–24 impulse.
4. **rsi** — measures how much of the snapback is already "spent"; 60.9 with 70 headroom is decision-relevant.
5. **boll_ub** — where the rally meets statistical supply; the December fail-point and the current test.
6. **boll_lb** — critical here because closes were *below* the lower band on Jan 2–5; that anchors the mean-reversion case and defines the opposite extreme.
7. **atr** — volatility expanded during the January gap-down; needed for stop distance and position size.
8. **vwma** — the only volume-integrated price level: reveals whether buyers are paying up on conviction or drifting on thin tape.

*(Auxiliary from snapshot, not separately selected: close_10_ema 190.41 for the short-term pivot cluster.)*

---

## 3. Price structure and the January shock

- The December peak close was **198.11 (2023-12-14)**, with an intraday high of **199.62** the same day.
- Distribution followed: 12/20 high 197.68, 12/21 high 197.08 — a sequence of **lower highs**.
- **2024-01-02:** gap-down and −3.6% session (192.53 → 185.64) on **82.49M shares**, the largest volume in the window except 12/15's 128.5M index-event day.
- Selling climaxed with a **181.18 close on 2024-01-05** (intraday low 180.17). Drawdown from the 12/14 close: **−8.5%** (198.11 → 181.18); from the 12/14 high: −9.7% (199.62 → 180.17).
- **Jan 2–5 closes were all BELOW the lower Bollinger band** (e.g., 1/5 close 181.18 vs boll_lb 182.32) — a statistical oversold extreme, not merely an "RSI low."
- **2024-01-17** retested the low zone (low 180.30, close 182.68), then **01-18 gapped up** from 182.68 to a 186.09 open and closed 188.63 on **78.01M shares** — the highest volume since the 1/2 breakdown. That gap (**182.68–186.09**) is still unfilled (lowest subsequent low: 185.83 on 1/18) and is the most important structural support beneath the market.
- Four consecutive up closes followed: 188.63 → 191.56 → 193.89 → 195.18, then **2024-01-24 printed a higher high (196.38) but closed lower at 194.50, in the bottom ~8% of the day's 2.04-point range.** That is a stalling bar, not a breakdown.

**Recovery math (verified closes):** 181.18 (1/5) → 195.18 (1/23) = **+7.7%** in 12 sessions; 194.50 on 1/24 is still **+7.3%** off the low and **+1.5%** on the week.

---

## 4. Trend: the pullback never damaged the primary uptrend

- **Price 194.50 vs 50 SMA 190.53 → +2.1% above.** The 50 SMA rose every single session in the sample: 178.36 (11/27) → 186.63 (12/29) → **190.53 (1/24)**, including *through* the January selloff. A rising 50 SMA during a −8.5% drawdown means the drop was a counter-trend retracement, not a trend change.
- **Price vs 200 SMA 181.60 → +7.1% above.** The 200 SMA is also rising monotonically (174.53 on 11/27 → 181.60 now). 50 SMA > 200 SMA by 8.93 points (~4.9% of the 200 SMA) and the spread is **widening** — a confirmed golden-cross regime with positive slope on both averages.
- **10 EMA 190.41** has been reclaimed since 1/19 and is still *marginally* below the 50 SMA (190.41 vs 190.53). That hairline gap is informative: the short-term average has only just caught up to the medium-term one, i.e., **the recovery is ~13 sessions old and short-term trend repair is nearly — but not fully — complete.**

**Implication:** the path of least resistance remains up, but the easy mean-reversion money has been made. The 190.4–190.5 area (10 EMA + 50 SMA cluster) is now the *line in the sand* for the bullish case.

---

## 5. Momentum: bullish regime flip, with one caveat

- **MACD line crossed zero between 2024-01-22 (−0.408) and 2024-01-23 (+0.184)**, and extended to **+0.591 on 1/24**. The ascent from −1.926 (1/17) to +0.591 in five sessions is a violent momentum flip.
- MACD is **above its signal (−0.534)**, giving a **histogram of +1.124** — a wide positive gap confirming that the *rate of change* is accelerating, not just the level.
- **RSI 60.92**, up from **28.79 on 1/5** and back above 50 on **1/18 (51.59)**. It peaked at 62.62 on 1/23 and eased to 60.92 on 1/24. RSI is **neither overbought nor diverging at a fresh extreme** — there is roughly 9 RSI points of headroom before the 70 threshold.
- **Caveat — momentum is weaker than at the same price in December:** on 2023-12-08 AAPL closed 195.71 with RSI 70.02 (MACD 3.41 on 12/07); on 2024-01-23 it closed 195.18 with RSI 62.62 and MACD 0.18. Same price, materially softer momentum. This is partly mechanical (RSI/EMA-state reset by the January air-pocket), but it does argue that a **clean breakout above 197.6–199.6 needs fresh volume, not just price drift.**

---

## 6. Volatility and band position: from lower-band extreme to 83% of the range

- Bollinger **mid 188.19**, **upper 197.62**, **lower 178.75**. Bandwidth = (197.62 − 178.75) / 188.19 = **10.0%**, down from 11.2% on 1/17 — modest contraction while price travels up through the band structure.
- **%B = (194.50 − 178.75) / 18.87 = 0.83.** Price sits in the upper quartile of the band but **has not tagged the upper band (197.62)** at any point in the recovery — a sign of steady accumulation rather than a blow-off.
- Critically, the band midpoint (188.19) is **below** current price and *fallen* from 192.64 on 1/5, because the 20-day mean still carries the January break. Price is therefore trading above a descending mean — a bullish divergence that resolves either by the mean catching up (time) or price reverting (price).
- **ATR 3.179** (1.63% of price), up from **2.575 on 12/29** and troughing near **3.10 on 1/17** before the gap. Volatility expanded on the decline and has stayed elevated during the rebound (3.34 / 3.34 / 3.37 on 1/18–1/22). Stop distances must respect the post-shock regime: **1.5×ATR = 4.77; 2×ATR = 6.36 (3.27% of price).**

---

## 7. Volume quality: the one genuinely bearish counterpoint

- **VWMA = 186.77**, i.e., price (194.50) is **+4.1% above** the volume-weighted average price of its recent trade. That gap says recent buyers are paying up aggressively relative to where volume has actually transacted.
- VWMA is **turning up** (185.25 on 1/18 → 185.36 → 185.59 → 186.04 → 186.77) but remains **3.8 points BELOW the 50 SMA (190.53)**. Translation: heavy volume is concentrated in the **186–188 zone** (the 1/2, 1/4, 1/8, 1/16, 1/18 sessions), not at current prices. If the market revisits 186–188, the volume-weighted holder base sits right there — supply risk is real in that band.
- **The rally's volume is decaying:** 78.01M (1/18) → 68.90M (1/19) → 60.13M (1/22) → **42.36M (1/23, ~78% of the ~54.2M 20-day average)** → 53.63M (1/24, on a *down* close). Rising price on shrinking volume is the classic signature of a **short-covering/mean-reversion bounce rather than fresh institutional demand.** The 1/24 down-session volume exceeding 1/23's up-session volume is a second, smaller warning.

---

## 8. Levels map (all prices from verified tool output)

| Type | Level | Source |
|---|---|---|
| Resistance 5 | **199.62** | 2023-12-14 intraday high (window high) |
| Resistance 4 | 198.11 | 2023-12-14 close |
| Resistance 3 | **197.62** | Bollinger upper band (1/24) |
| Resistance 2 | 197.68 / 197.08 | 12/20 / 12/21 highs |
| Resistance 1 | **196.38** | 1/24 intraday high |
| Pivot | 194.50 | 1/24 close |
| Support 1 | 193.83 / 192.26 | 1/23 / 1/22 lows |
| Support 2 | **190.41–190.53** | 10 EMA + 50 SMA cluster |
| Support 3 | 188.19 | Bollinger mid / 1/18 close 188.63 |
| Support 4 | **182.68–186.09** | Unfilled 1/18 gap (bottom/top) |
| Support 5 | 180.17–180.30 | 1/5 low / 1/17 low |
| Strategic | 181.60 | 200 SMA (close below = regime change) |

---

## 9. Actionable scenarios and trade construction

**Base case — bullish continuation (probability weighted highest given trend + momentum alignment).**
The setup is a bull flag/recovery above a rising 50/200 SMA stack with MACD freshly positive. Requires a **close above 197.62 (upper band)** to open the 198.11 → 199.62 December supply shelf.
- *Entry A (breakout):* close > 197.62 with volume ≥ 60M (reclaiming the 1/19 level). Stop **1.5×ATR ≈ 4.8 points** below entry (~192.8), i.e., just under the 1/23–1/24 lows. First target 199.62; ATR-based extension 203.5–206.0 (199.62 + 1–2 × ATR).
- *Entry B (preferred risk/reward — buy the pullback):* 190.4–191.5 zone (10 EMA/50 SMA). Stop on a **close below 188.19** (Bollinger mid), risk ≈ 2.5–3.3 points (~1×ATR), target 197.6 → 199.6. This offers ~2.5:1 to 3:1 versus ~1.2:1 for chasing at 194.5.

**Bear/neutral case — stalling at supply on fading volume.**
Triggers to watch: (i) failure to close above 196.38–197.62 and a break of 193.83; (ii) 1/24's weak close (bottom 8% of range) confirmed by another rejection; (iii) volume staying sub-50M on up days. Sequence would be 190.4 → 188.19 → gap fill into **186.09 → 182.68**. A close below 182.68 would void the bullish structure and put the 200 SMA (181.60) in play.

**Invalidation levels (hard):**
- **Bull thesis damaged:** daily close < 188.19 (Bollinger mid) — price back below a still-descending 20-day mean.
- **Bull thesis void:** daily close < 182.68 (gap bottom) and/or < 200 SMA 181.60.
- **Overbought exit trigger for longs:** RSI > 70 *while* price stalls at 197.6–199.6 on declining volume.

**Position sizing (ATR-normalized):** with a 2×ATR stop (6.36 pts = 3.27% of price), risking 1% of equity implies a position of roughly **30% of equity**; with the tighter 190.4-entry / 188.19-stop construction (~1.2% risk per share) the same 1% budget supports a much larger notional. Because ATR has risen from 2.58 to 3.18 since 12/29, **reduce share count ~20% versus December norms** for the same dollar risk.

**What would make me wrong:** a volume-backed close above 197.6 followed by a decisive hold above 199.62 would shift the framework from "range top" to "new leg higher," in which case the bear case (mean reversion to 186–188) is off and trailing stops (Chandelier-style, 2×ATR ≈ 6.4 pts under the high) become the correct management tool rather than fixed targets.

---

## 10. Key points summary

| # | Dimension | Evidence (2024-01-24 verified) | Read | Action |
|---|---|---|---|---|
| 1 | Primary trend | Close 194.50 > 50 SMA 190.53 (+2.1%) > 200 SMA 181.60 (+7.1%); both rising | Bullish, intact | Buy dips, not breakdowns |
| 2 | Golden cross | 50 SMA – 200 SMA = +8.93 pts (~4.9%), widening | Regime confirmed | Strategic long bias |
| 3 | Short-term trend | 10 EMA 190.41 reclaimed since 1/19; still ≈ 50 SMA (190.53) | Repair nearly complete | 190.4–190.5 = pivot |
| 4 | Momentum | MACD 0.591 > signal −0.534; histogram +1.124; zero-line cross on 1/23 (from −0.408 on 1/22) | Bullish acceleration | Confirms long side |
| 5 | Momentum risk | RSI 60.92 vs 70.02 on 12/08 at a similar price (195.71) | Softer internals | Demand volume confirmation on breakout |
| 6 | Mean-reversion origin | Closes below lower band Jan 2–5 (1/5: 181.18 vs LB 182.32) | Snapback, not a new trend inception | Bounce is mature (+7.7% off low) |
| 7 | Band position | %B = 0.83; upper 197.62, mid 188.19, lower 178.75; bandwidth 10.0% (from 11.2%) | Upper half, not yet overbought | 197.62 = breakout trigger |
| 8 | Volatility/risk | ATR 3.179 (1.63%); 1.5×ATR 4.77, 2×ATR 6.36; ATR up from 2.575 on 12/29 | Post-shock regime | Widen stops, cut size ~20% |
| 9 | Volume quality | Rally volume 78.0 → 68.9 → 60.1 → 42.4M, then 53.6M on a down bar | Distribution-lite warning | Do not chase 194–196 |
| 10 | Volume-weighted value | VWMA 186.77, 3.8 pts below 50 SMA; price +4.1% above VWMA | Supply likely at 186–188 | Prefer entries at 190.4 / 186–188 |
| 11 | Nearest resistance | 196.38 (1/24 high) → 197.08/197.62/197.68 → 198.11 → 199.62 | Crowded overhead | Scale out into 197.6–199.6 |
| 12 | Key support | 190.4–190.5 → 188.19 → gap 182.68–186.09 → 180.17 | Clear risk map | Close < 188.19 = thesis damage |
| 13 | Trade plan | Buy 190.4–191.5, stop < 188.19, targets 197.6/199.6; or breakout close > 197.62 on ≥60M volume, stop 192.8 | ~2.5–3:1 preferred | Risk 1% equity, ATR-scaled |
| 14 | Invalidation | Close < 182.68 and/or < 200 SMA 181.60 | Regime change | Stand aside / flip bias |