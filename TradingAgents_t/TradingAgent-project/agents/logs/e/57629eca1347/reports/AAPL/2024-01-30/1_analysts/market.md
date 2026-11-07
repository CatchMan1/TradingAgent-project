# AAPL — Technical & Momentum Assessment (as of 2024-01-30 close)

**Verification note:** The verified snapshot and the raw OHLCV pull agree exactly for the 2024-01-30 row (O 190.94 / H 191.80 / L 187.47 / C 188.04, volume 55,859,400) and for every indicator value I cite below (e.g., RSI 45.8818, MACD 0.6326, signal 0.2705, histogram 0.3621, 50 SMA 190.9252, 200 SMA 182.1909, 10 EMA 190.7940, ATR 3.2153, VWMA 189.3951). The signal value is internally consistent: 0.632559 − 0.362076 = 0.270483. **No discrepancies found between tools.** All price references below come directly from the returned daily rows or the snapshot.

---

## 1. Indicator selection and why these eight

| Indicator | Role in this specific setup |
|---|---|
| **close_200_sma** (182.19) | The dominant structural line — AAPL's primary uptrend is still intact above it. Defining "bull trend vs. breakdown." |
| **close_50_sma** (190.93) | The battleground level. Price just lost it after a 7-session reclaim; it also marks the flat/rolling-over medium-term trend. |
| **close_10_ema** (190.79) | Short-term momentum trigger; today's close is the first below it since 2024-01-17. |
| **macd** (0.63) | Captures the mid-Jan momentum flip from negative to positive and its current fade. |
| **macdh** (0.36) | Shows *rate of change* of that momentum — three consecutive declining bars is the key early-warning signal here. |
| **rsi** (45.9) | Confirms the fast unwind from 62.6 → 45.9 without oversold cushion; also frames room-to-fall. |
| **atr** (3.22) | Volatility is expanding (2.57 on 12/29 → 3.22 today), so stops and sizing must be ATR-based, not fixed. |
| **vwma** (189.40) | Volume-weighted "true" average entry; price is below it, which corroborates that the recent up-leg is being sold into. |

**Why this set is complementary, not redundant:** I deliberately avoided stacking oscillators (no stochrsi alongside RSI) and skipped `macds` because the histogram already delivers the signal-line information in a more readable form. Bollinger bands (middle 187.89, upper 196.96, lower 178.82 per the verified snapshot) are quoted only as supplementary context — they are *not* part of the eight-indicator selection. The set spans four orthogonal dimensions: trend (10 EMA / 50 SMA / 200 SMA), momentum (MACD + histogram + RSI), volume-weighted price (VWMA), and risk/volatility (ATR). The current market is a **high-level consolidation inside a longer uptrend with momentum decelerating from a failed breakout** — that is precisely a regime where you need trend-structure levels *plus* momentum-rate-of-change *plus* a volatility input for stop placement.

---

## 2. Multi-timeframe trend read

**Long term (200 SMA) — bullish, but the line is running up under a stalling price.**
The 200 SMA has climbed monotonically from 179.64 (2024-01-02) to 182.19 (2024-01-30), and price at 188.04 sits **+3.21% above it**. The 50 SMA (190.93) remains above the 200 SMA (182.19), a spread of ~8.7 points — the golden-cross structure established during the Nov–Dec advance is still in force. Structurally, nothing here says "trend broken." What it does say is that the 200 SMA is rising *into* price, i.e., the cushion under the market is thinning.

**Medium term (50 SMA) — flat-to-rolling, and price has just been rejected at it.**
The 50 SMA rose from 184.16 (2023-12-18) to 190.93 (2024-01-30), but note its slope: it has essentially flatlined over the last five sessions (190.69 → 190.84 → 190.92 → 190.93), reflecting the December peak falling out of the averaging window. The price/SMA interaction is the single most instructive sequence in the dataset:

- Price closed **below** the 50 SMA on 2024-01-02 (185.64 vs 186.84) and stayed below through 2024-01-18.
- It **reclaimed** the 50 SMA on 2024-01-19 (191.56 vs 189.80) and held above for seven consecutive sessions through 2024-01-29 (191.73 vs 190.92).
- On 2024-01-30 it **closed back below** it: 188.04 vs 190.93.

That is a textbook failed reclaim — the 50 SMA has flipped from support back into overhead resistance on the most recent bar.

**Short term (10 EMA) — momentum break.**
The 10 EMA bottomed at 185.37 on 2024-01-17 and rose to 191.41 by 2024-01-29. Today's 10 EMA is **190.79**, and price at 188.04 is **2.75 points / 1.45% below it** — the first close beneath the 10 EMA since 2024-01-17. Even more telling, the 10 EMA briefly crossed *above* the 50 SMA on 2024-01-25 (191.09 vs 190.69) and has now crossed back **below** it (190.79 vs 190.93) — a whipsaw that argues against treating the mid-Jan bounce as a fresh trend leg.

**Structure of highs — lower high on the daily chart.**
The December sequence printed 198.00 (2023-12-13) and 199.62 (2023-12-14). The January rebound topped at 195.33 (2024-01-22) / 195.75 (2024-01-23) / 196.38 (2024-01-24). That is a **lower high** (~3.2 points below the December peak). Combined with the failed 50 SMA reclaim, the medium-term bias has shifted from "pullback in an uptrend" toward "range/distribution under resistance."

---

## 3. Momentum: decelerating, not yet oversold

**MACD (0.63) vs signal (0.27) — still bullish, but the cross is slipping away.**
The MACD line was at −1.93 on 2024-01-17 and turned positive on 2024-01-23 (0.184) — its first positive reading since the January selloff began. It peaked at 0.951 on 2024-01-26 and is now 0.633. The histogram is the cleaner tell:

- 2024-01-23: **+0.998**
- 2024-01-24: **+1.124**
- 2024-01-25: **+1.128** (peak)
- 2024-01-26: **+0.962**
- 2024-01-29: **+0.764**
- 2024-01-30: **+0.362**

That is **three straight sessions of contraction**, with the last one cutting the bar by more than half. At this decay rate, a bearish MACD/signal crossover is plausible within roughly 2–4 sessions if price doesn't stabilize — and the MACD line is only 0.63 above zero, so a negative-line crossover is not far behind.

**RSI (45.9) — momentum unwound, no divergence, no cushion.**
RSI went 62.62 (2024-01-23) → 60.92 → 60.07 → 55.62 → 53.93 → **45.88** (2024-01-30). A ~16.7-point collapse in five sessions. Two things matter here:
1. **The rally stalled at 62.6, not 70.** In a healthy uptrend leg you'd expect a push into the 65–70 zone. Failure at ~63 signals the buyers ran out of conviction rather than being "overbought."
2. **RSI at 45.9 is neutral, not oversold.** Applying the 70/30 framework, there is roughly 17 points of downside room before the 30 threshold is even approached. The January 4–5 episode is the reference: RSI printed 29.78 and 28.79 on 2024-01-04/05 and, critically, the low of that washout was 180.17 on 2024-01-05. RSI in the high 40s is not a mean-reversion buy signal in this construction.

**No positive divergence is present** in the data: the 2024-01-17 price low (180.30) came with RSI 36.71, and the subsequent rally to 195.75 lifted RSI to 62.6 — a normal, non-divergent advance followed by a normal pullback.

---

## 4. Volume and VWMA: the rally is losing its volume bid

**VWMA (189.40) now sits above spot (188.04).** That means the volume-weighted average dollar paid over the VWMA window is ~0.72% above the current price — the marginal buyer from the January rebound is underwater. VWMA bottomed at 185.25 on 2024-01-18 and has risen to 189.40, but because price has fallen *through* it, this flips from a supportive rising line into overhead supply. Note also VWMA (189.40) < 50 SMA (190.93): the volume-weighted trend is *weaker* than the simple trend, which is what you see when the recent volume is concentrated on lower prices.

**Daily volume profile of the January swing:**

| Leg | Dates | Volume character |
|---|---|---|
| Impulse up | 2024-01-18 (+3.3% close) / 01-19 (+1.6%) | **78.0M / 68.9M** — well above average, genuine institutional participation |
| Follow-through drift | 01-22 → 01-25 | 60.1M / 42.4M / 53.6M / 54.8M — fading volume into higher prices (negative breadth signal) |
| Reversal down | 01-26 → 01-30 | 44.6M / 47.1M / **55.9M** — volume *expanding* on the final down day |

Using the returned daily volumes, the 20-session average through 2024-01-30 is roughly **56.6M**. So 2024-01-30's 55.86M is *not* a capitulation spike — it's an ordinary-volume decline day, and it is the heaviest of the last six sessions. The nuance cuts both ways: the up-leg had better volume than the down-leg by absolute terms (arguably accumulation), but the *trend* of volume has been shrinking on rallies and picking up on declines — mildly distributive.

**Today's candle internals are bearish:** the close (188.04) sits in the **bottom 13%** of the 4.33-point range (187.47–191.80), and the range was 1.35× the 3.22 ATR. Sellers closed the session in control, giving back the entire intraday advance from the 190.94 open.

---

## 5. Volatility and risk calibration

ATR(14) has risen from **2.57 (2023-12-29) → 3.22 (2024-01-30)**, a ~25% expansion. ATR as a percentage of price is **1.71%**. The trend of ATR matters more than the level: rising ATR alongside a falling close and a contracting MACD histogram is the classic "volatility expanding in the wrong direction" signature. Practical implications:

- **Stop placement:** a 1.5× ATR buffer is ~$4.82, a 2.0× ATR buffer is ~$6.43. Stops tighter than ~$3.20 (1 ATR) will be noise-triggered in this regime.
- **Sizing example:** on a $100,000 account risking 1% ($1,000) with a 1.5-ATR stop ($4.82), the position is ~207 shares (~$38,900 notional, ~39% of account). Tighter stops would mean larger notional — which is exactly why sizing off ATR rather than off a fixed dollar stop matters here.
- **Bollinger context (supplementary, from the verified snapshot):** middle 187.89, upper 196.96, lower 178.82. Price closed at 188.04 — barely **0.15 above the middle band**. That makes 187.89 a near-term pivot: hold it and the 20-day mean is support; lose it and the next magnet is the lower half of the band.

---

## 6. Actionable levels (all derived from tool output)

**Resistance (stacked overhead):**
1. **189.40** — VWMA
2. **190.79–190.93** — the 10 EMA / 50 SMA cluster (the key decision zone)
3. **191.80** — 2024-01-30 high
4. **192.20–192.42** — 2024-01-26 / 01-29 highs and closes
5. **194.50–195.75** — 2024-01-23/24/25 highs (prior swing high shelf)
6. **196.96** — upper Bollinger band; also the 2024-01-24 high of 196.38 stopped just short of this zone

**Support (progressive):**
1. **187.89** — Bollinger middle band (immediate pivot)
2. **187.47** — 2024-01-30 low
3. **185.19–185.56** — 2024-01-12 low / 2024-01-08 close
4. **182.68 / 180.30** — 2024-01-17 lows; then **181.18 / 180.17** (2024-01-05 washout close/low)
5. **182.19** — 200 SMA (the structural line of last resort)

---

## 7. Scenario map with triggers

**A. Bearish continuation (highest-probability near term given the momentum tape):** A close below 187.47–187.89 opens 185.19, then the 180.17–182.68 congestion from mid-December to early January. The 200 SMA at 182.19 sits inside that congestion — a test there would be the first genuine threat to the long-term trend. Confirmation markers: MACD histogram turning negative, MACD line losing 0.27 (signal), 10 EMA crossing decisively under the 50 SMA.

**B. Range/neutral (also very plausible):** Price chops between roughly 185 and 194 to work off the January volatility, with RSI oscillating in the 40–60 band. Consistent with a flat 50 SMA and a still-rising 200 SMA. In this regime, mean-reversion entries near 185–186 with stops under 183.5 (below the 200 SMA cushion) and targets at 190.9–192.4 offer ~2:1 to 3:1.

**C. Bullish invalidation of the pullback:** Only a **close back above 190.93 (50 SMA)** with volume re-expanding toward 70M+ would reopen 194.5 and 195.75, and then the 196.96 upper band. Note the burden of proof is higher here: the January 19–29 reclaim above the 50 SMA already failed once on 2024-01-30, and the lower-high structure at 195.75/196.38 remains unbroken. A first bullish *step* — not a buy signal by itself — would be reclaiming the 10 EMA at 190.79.

**Event risk flag (not tool-verified):** AAPL historically reports its December-quarter results in the first days of February. If that catalyst lands in the next few sessions, all of the above technical logic is subordinate to the gap risk — position sizing should be cut to reflect the fact that a 3.2 ATR (~1.7%) daily range is likely to be exceeded. Confirm the exact date from an independent source; it is not derivable from the price data provided.

---

## 8. Bottom line

AAPL on 2024-01-30 is a **long-term uptrend (price +3.2% over a rising 200 SMA) undergoing a medium-term loss of momentum**. The evidence is convergent rather than ambiguous: price rejected at the 50 SMA after a 7-session reclaim, back below the 10 EMA for the first time since 2024-01-17, below VWMA, RSI unwound from 62.6 to 45.9 with room still to fall, MACD histogram contracting for three straight sessions, a lower high at 196.38 versus the 199.62 December peak, and expanding ATR. The counterweight is equally real — the golden-cross structure (50 > 200) is intact, the 200 SMA is rising, the 2024-01-18/19 rally carried genuine volume (78.0M / 68.9M), and today's volume of 55.9M was not a distribution blow-off. Net: **constructive on structure, defensive on momentum.** The trade is to respect the 187.47–190.93 decision zone rather than to anticipate; conviction longs should wait for a reclaim of 190.93 with volume, and the tactical bias favors fading strength into 190.8–192.4 with stops beyond the 1.5 ATR envelope.

---

### Key metrics summary

| Metric | Value (2024-01-30) | Interpretation |
|---|---|---|
| Close | **188.04** | −1.93% vs 191.73 (2024-01-29); bottom 13% of day's range |
| Day range | 187.47 – 191.80 | 4.33 pts = 1.35× ATR; bearish close |
| Volume | 55.86M | ≈20-session avg (~56.6M); heaviest of last 6 sessions |
| 10 EMA | 190.79 | Price 1.45% below — short-term break |
| 50 SMA | 190.93 | Price below after 7 sessions above — failed reclaim |
| 200 SMA | 182.19 | Price +3.21% above; rising (179.64 on 2024-01-02) |
| 50 vs 200 SMA | 190.93 vs 182.19 | Golden-cross structure intact (+8.7 spread) |
| VWMA | 189.40 | Above spot — volume-weighted holder underwater |
| RSI(14) | **45.88** | From 62.62 (1/23); neutral, ~17 pts of room to 30 |
| MACD / Signal | 0.633 / 0.270 | Positive but fading; peak 0.951 (1/26) |
| MACD Histogram | **0.362** | 3 straight declines from 1.128 peak — momentum decelerating |
| ATR(14) | 3.22 (1.71%) | Up from 2.57 (12/29) — volatility expanding |
| Bollinger mid/up/low | 187.89 / 196.96 / 178.82 | Price 0.15 above middle band — 187.89 is the pivot |
| Nearest resistance | 189.40 → 190.79–190.93 → 191.80 → 195.75 → 196.96 | Stacked; needs >190.93 close to matter |
| Nearest support | 187.89 → 187.47 → 185.19–185.56 → 182.19 (200 SMA) | 200 SMA coincides with Jan congestion |
| Stance | **Neutral / tactically defensive** | Structure bullish, momentum bearish — trade the 187.5–191 zone |
| Suggested stop buffer | 1.5× ATR ≈ $4.82 | ~183.2 from 188.04; ~186.1 from a 190.9 entry |