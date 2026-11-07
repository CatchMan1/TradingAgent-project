# AMZN — Multi-Horizon Technical Report
**As of the 2026-09-28 close | Verified snapshot price: $246.15**

---

## 1. Data integrity check (done first)

I pulled the full OHLCV history (251 sessions, 2025-09-29 → 2026-09-28) and then the deterministic verification snapshot for 2026-09-28. **The two agree exactly** — every close, volume figure, and indicator value in this report is taken from the verified snapshot, which is treated as the source of truth. No reconciliation or flag is required.

| Field | Verified value (2026-09-28) |
|---|---|
| Open / High / Low / Close | 246.63 / 247.77 / 244.73 / **246.15** |
| Volume | 32,596,700 |
| 50-SMA | 256.1534 |
| 200-SMA | 240.9390 |
| 10-EMA | 250.9444 |
| MACD / Signal / Histogram | −2.3529 / −1.7392 / −0.6137 |
| RSI(14) | 41.24 |
| Bollinger mid / upper / lower | 253.292 / 261.7749 / 244.8091 |
| ATR(14) | 5.7457 |
| VWMA | 251.7238 |

---

## 2. Executive verdict

AMZN is in a **three-speed market**: the long-term uptrend is intact, the medium-term trend has stalled and is rolling over, and the short-term trend is a clean sequence of lower highs with a failed bounce off the lower Bollinger Band. Momentum is bearish but **not yet oversold** (RSI 41.2), volatility has compressed sharply (ATR down ~42% from its early-August peak), and volume is unremarkable — today's 32.6M is roughly in line with the ~33.9M average of the prior 19 sessions.

Net: **neutral-to-bearish drift inside a still-valid long-term uptrend**, with price pinned against a well-defined support shelf at 244.3–244.8. This is a decision point, not a trend-following entry in either direction. The compressed ATR and shrinking Bollinger width argue that a range expansion is building — but the tools show no evidence yet of which side wins.

---

## 3. Trend structure, by horizon

### 3.1 Long-term (200-SMA): intact but being tested
- Confirmed close **240.939**, and it is **rising steadily**: 238.68 (2026-08-28) → 240.94 (2026-09-28), about +0.11/session.
- Price at 246.15 sits only **+2.16% above** the 200-SMA. Given ATR is 2.33% of price, the long-term trend line is effectively **one average daily range away** — i.e., "above it" is technically true but not comfortable.
- 50-SMA (256.15) remains **above** the 200-SMA (240.94), a spread of 15.21 points (+6.3%). The golden-cross structure from the 2026 recovery is **not** broken. This is the single strongest bullish fact in the dataset.

### 3.2 Medium-term (50-SMA): rolling over
- 50-SMA at **256.153**, price **3.91% below** it.
- The slope has decelerated hard: +3.81 points between 2026-08-28 (251.66) and 2026-09-14 (255.47), but only **+0.68 points** between 2026-09-14 and 2026-09-28 (256.15). The 50-SMA is flattening — typical of an uptrend losing its bid, not yet of a downtrend.
- Bollinger mid-line / 20-SMA at **253.292**; price is 2.82% below it. The 20-SMA is now *below* the 50-SMA, the classic short-term-below-medium-term stacking of a corrective phase.

### 3.3 Short-term (10-EMA and swing structure): lower highs, failed reclaim
- 10-EMA at **250.944**, price 1.91% below. The 10-EMA has fallen monotonically from **267.16 (2026-08-11)** to 250.94, with no up-turn.
- The bounce of 2026-09-17→09-22 did push price above the 10-EMA for four sessions (closes 251.19, 253.71, 258.45, 254.98 vs EMAs 252.73, 252.91, 253.92, 254.11) — **but it failed on 2026-09-23** (close 249.27 vs EMA 253.23) and price has not reclaimed it since. A failed reclaim of the 10-EMA after a multi-day bounce is a bearish continuation signature.
- Lower-high sequence, all from tool data: **287.20** (2026-08-03 intraday high) → **267.56** (2026-08-28) → **261.12** (2026-09-04) → **259.49** (2026-09-21) → **247.77** (2026-09-28). Four consecutive lower swing highs.
- Lower closing lows: 256.26 (08-27) → 254.92 (09-01) → 251.89 (09-10) → 245.96 (09-16); the current 246.15 close is essentially retesting that 09-16 low.

### 3.4 Where price sits in the year's range
- 52-week range (tool data): **low 196.00 (2026-02-17)**, **high 287.20 (2026-08-03)**. Current price is at the **55.0%** percentile of that range — dead center.
- The Feb→Aug advance was **+46.5%** (196.00 → 287.20). The current pullback is **−13.33%** from the 284.02 closing peak (−14.29% from the 287.20 intraday high).
- Fibonacci retracements of that advance: 23.6% = 265.68, **38.2% = 252.36**, **50% = 241.60**, 61.8% = 230.84. Price (246.15) has cleared the 38.2% level and is probing toward the 50% level. Note how 252.36 (38.2%) stacks almost exactly on the 20-SMA at 253.29 — a genuine confluence resistance, not a coincidence of my arithmetic.
- **Gap structure:** the earnings gap of 2026-07-31 ran from the prior close of 235.50 to an open of 265.00. Price is now **inside that gap** and has retraced **63.9%** of it. In other words, most of the July earnings re-rating has been given back. The 235.50 level (gap origin / 2026-07-30 close) is the logical "full fill" magnet if 240.9 fails.

---

## 4. Momentum

### 4.1 MACD: bearish, and the bullish reset failed
- MACD **−2.353**, signal **−1.739**, histogram **−0.614**.
- The MACD line rolled below zero between 2026-09-08 (+0.118) and 2026-09-09 (−0.421) and has stayed negative since. It crossed below its signal line on the same 09-08/09-09 window (signal was 1.239 while MACD was 0.118).
- Critically, the histogram compressed to **−0.057 on 2026-09-22** — an imminent bullish crossover — then **widened back out to −0.614 by 2026-09-28**. That is a *failed* momentum reset, which historically carries more bearish information than a clean cross because it traps the counter-trend buyers who leaned on the 09-21 high.
- Both MACD and signal are below zero, so even a future crossover would initially be a "zero-line retest" rather than a trend change.

### 4.2 RSI: weak, but not the washout level
- RSI **41.24**, down from 52.69 (2026-09-21) and 44.54 (2026-09-25).
- The recent RSI trough was **39.45 on 2026-09-16**, which produced a +5.08% snapback to 258.45 by 2026-09-21 (245.96 → 258.45). RSI has *not* made a lower low than 39.45 on this leg (41.24), even though price is essentially flat versus the 09-16 close. That is a **tentative, unconfirmed positive divergence** — one data point, not a validated pattern.
- 41 is the "weak but working" zone, not the 30-level capitulation zone. There is **no oversold mean-reversion trigger** here. In the strong-trend phase of July–August, RSI ran 63–72 (peaking 72.23 on 2026-08-03, the exact day of the high) — the mirror image of today.

### 4.3 Momentum takeaway
The momentum complex says: **trend fatigue, not trend failure.** MACD below zero + RSI in the low 40s + failure to hold the 10-EMA is a distribution/consolidation profile. It does not, by itself, break the 200-SMA uptrend.

---

## 5. Volatility and Bollinger structure

- **ATR 5.746**, equal to **2.33% of price**. It has collapsed from **9.995 on 2026-08-05** and **7.20 on 2026-08-31** — a ~42% contraction from the post-earnings peak. That is a textbook volatility compression into a coil.
- **Bollinger width** = (261.775 − 244.809) / 253.292 = **6.70%** of the mid-line. That is narrow for a name with a 2.3% ATR and reflects the 20-day realized range shrinking.
- Price at 246.15 is only **1.34 points (+0.55%) above the lower band (244.809)**. It is riding the bottom of the envelope, not bouncing off the middle.
- **Important precedent:** on 2026-09-16 AMZN *closed below* the lower band (close 245.96 vs band 246.835) and then snapped back +5.08% in three sessions. One instance only — I would not call this a validated "band undercut = buy" rule, but it does show the band is being used as a mean-reversion magnet rather than a breakdown rail so far.
- **Interpretation:** narrow bands + falling ATR + price pinned at the lower rail usually resolve in a directional expansion. Because price is also sitting on horizontal support (244.3–244.8), the *level* of resolution matters far more than the *fact* of it.

---

## 6. Volume and participation

- **VWMA 251.724** vs price 246.15 → price is **2.21% below** the volume-weighted average. Volume-weighted holders are underwater on the recent window; VWMA has declined from **272.05 (2026-08-20)** to 251.72 without a single up-session, which is a persistent distribution signature.
- Today's volume of **32.6M** is roughly in line with the ~33.9M average of the prior 19 sessions (my calculation from the tool's rows). **No volume expansion on the decline** — this is a low-conviction drift, not a stampede. That cuts both ways: it argues against capitulation, but it also means there is no accumulation footprint to buy against.
- For scale, the event days dwarf this: **179.2M on 2026-02-06** (−9.73%), **166.3M on 2025-10-31** (+9.59%), **129.1M on 2026-07-31** (+15.32%), and **101.8M on 2026-07-30**. Separately, **248.4M on 2026-06-26** (range 226.13–233.90) looks like an index/rebalance print and marks a high-volume shelf at **226–234** — a logical deeper support if 240.9 gives way.
- A 20-session chart of volume shows a steady bleed from 30–52M in early September to 25–34M in the last two weeks. **Sellers are not pressing, and buyers are not stepping up.** Classic pre-resolution standoff.

---

## 7. Key levels (all derived from tool output)

| Level | Price | Source / date |
|---|---|---|
| Record high | 287.20 | Intraday high, 2026-08-03 |
| Aug swing high | 267.56 | High, 2026-08-28 |
| Sept 4 rejection | 261.12 | High, 2026-09-04 |
| Bollinger upper | 261.775 | 2026-09-28 |
| Sept double-top zone | 259.49–259.50 | Highs 2026-09-03 / 2026-09-21 |
| 50-SMA | 256.153 | 2026-09-28 |
| Bollinger mid / 20-SMA | 253.292 | 2026-09-28 |
| 38.2% retrace | 252.36 | Calculated from 196.00 / 287.20 |
| VWMA | 251.724 | 2026-09-28 |
| 10-EMA | 250.944 | 2026-09-28 |
| Spot | **246.15** | Close, 2026-09-28 |
| Support cluster | **244.30–244.81** | Low 2026-09-16 (244.30), low 2026-09-28 (244.73), lower Boll (244.809) |
| 50% retrace | 241.60 | Calculated from 196.00 / 287.20 |
| 200-SMA | 240.939 | 2026-09-28 |
| Gap origin | 235.50 | Close, 2026-07-30 (pre-earnings gap) |
| Volume shelf | 226.13–233.90 | Range, 2026-06-26 (248.4M shares) |

---

## 8. Actionable scenarios

### Base case (highest probability given the evidence): continued 240–260 chop
Price is mid-range (55th percentile of the 52-week range), below a flattening 50-SMA, above a rising 200-SMA, with RSI at 41 and a narrowing MACD histogram. The path of least resistance is sideways-to-lower inside the 244.3–256.2 band until either the support shelf or the 50-SMA is resolved. **Trade small, fade extremes, do not chase.**

### Bearish trigger — close below 244.30
- A daily close below **244.30** (the 2026-09-16 swing low) would be the first lower low since the August top, break the lower Bollinger rail with price *already* riding it, and convert the band from magnet to rail.
- First target: **240.94 (200-SMA) / 241.60 (50% retrace)**. If that fails, the gap-fill objective is **235.50**, with the 226–234 volume shelf behind it.
- Confirmation requirement: **volume above ~45M** (roughly 1.3× the recent 19-session average). A low-volume drift through 244.3 has repeatedly been bought back in this dataset (see 2026-09-16).
- Invalidation for the bear case: a same-day or next-day reclaim of 246.5+ on strong volume.

### Bullish trigger — reclaim 251.7–253.3
- The first real repair is a close back above the **VWMA (251.72) and 10-EMA (250.94)** together, then the **Bollinger mid / 20-SMA (253.29)**. That would neutralize the short-term downtrend and put the 38.2% retrace (252.36) back in play as support.
- A close above the **50-SMA at 256.15** is required to flip the medium-term trend. Above that, the **259.49–261.12** supply shelf is the next hurdle; clearing it opens **266.4–267.6**.
- A more aggressive, lower-probability setup: a positive RSI divergence confirmed by a higher low in price near 244–245 while RSI holds above ~39.5. Today's 41.24 vs the 09-16 39.45 is the *seed* of that, but it is one observation and should not be traded alone.

### Event-risk overlay (critical)
The dataset shows four violent, earnings-style gaps in twelve months: **2025-10-31 (+9.59%)**, **2026-02-06 (−9.73%)**, **2026-04-30/05-01**, and **2026-07-31 (+15.32%)**. The spacing is roughly quarterly, which *implies* a report in late October 2026 — **this date is an inference, not confirmed by the tools**. Sizing a swing position through that window without event-risk reduction would be the single largest avoidable error here. Note also that the 2026-05-01 → 2026-07-30 period shows how the stock can grind sideways for three months between prints.

---

## 9. Risk management specifics

- ATR-based stop for a swing position: **1.5× ATR ≈ 8.6 points**, **2.0× ATR ≈ 11.5 points**. A long entered near 246 with a 1.5× ATR stop sits at ~237.5 — which is *below* the 200-SMA and therefore a structurally sensible location, not merely a volatility-derived one.
- Position sizing example: risking 1% of equity with an 8.6-point stop on a $246 stock implies position notional of ~28.6% of equity (1% ÷ 3.5% price risk). Adjust to your own risk budget.
- Because ATR has compressed to 2.33% of price from 9.99 (≈3.5% of price) in early August, the same dollar risk now buys **~70% more shares** than it did six weeks ago. Do not carry old position sizes into a new volatility regime.
- Do not place resting stops exactly at 244.30 — the 2026-09-16 session traded to 244.30 and closed at 245.96, and today's low was 244.73. Give the level ~1 ATR of room or wait for a confirmed close.

---

## 10. What would change my view

| Would flip me bullish | Would flip me bearish |
|---|---|
| Close > 253.29 (20-SMA) on volume >45M | Close < 244.30 on volume >45M |
| MACD histogram turns positive and MACD reclaims zero | MACD makes a new low while price holds 246 (bearish divergence) |
| 10-EMA turns up and price holds above it 3+ sessions | 50-SMA crosses below 20-SMA (death-cross of the short stack) |
| RSI > 50 with price making a higher high above 259.50 | 200-SMA (240.94) closes below on expanding volume |
| 50-SMA resumes a steeper slope | VWMA continues to fall while price makes a lower high |

---

## 11. Indicator selection rationale

I used 8 indicators across four non-redundant dimensions:
- **close_50_sma + close_200_sma** — separate medium- from long-term trend and expose the flattening 50-SMA against a still-rising 200-SMA. This is the core of the "three-speed market" thesis.
- **close_10_ema** — the only fast trend measure used; it dates the failed bounce precisely (09-23) rather than leaving it to eyeballing. I deliberately did **not** add a second short average, to avoid redundancy.
- **macd + macds/macdh** — the zero-line, signal-line and histogram together distinguish "bearish but decelerating" from "bearish and re-accelerating." The 09-22 histogram near-zero then re-widening is the key non-obvious finding.
- **rsi** — independent, bounded momentum oscillator to test whether the decline is oversold (it is not) and to check for divergence.
- **boll_ub + boll_lb** (with the snapshot's mid-line) — gives both envelope position and band width, which is what actually quantifies the volatility compression.
- **atr** — converts every level into a risk unit and shows the 42% volatility collapse.
- **vwma** — the only volume-integrated price measure; it confirms the decline is volume-endorsed (price below VWMA) even though absolute volume is light.

Deliberately excluded: `boll` (the mid-line is already in the verified snapshot and is functionally the 20-SMA), and any second oscillator — adding one would duplicate RSI's information while inviting conflicting signals.

---

## 12. Summary scorecard

| Dimension | Reading (2026-09-28) | Signal | What it means for AMZN |
|---|---|---|---|
| **Price** | 246.15 close; high 247.77, low 244.73 | — | 55th percentile of the 196.00–287.20 52-week range; −13.3% from the 284.02 closing peak |
| **Long-term trend** | 200-SMA 240.939, rising ~+0.11/day; price +2.16% above | **Bullish (weakening)** | Uptrend intact but only ~1 ATR of cushion; golden-cross stack (50 > 200) still valid at +15.21 pts |
| **Medium-term trend** | 50-SMA 256.153; price −3.91%; 50-SMA slope collapsed to +0.68 pts over 10 sessions | **Bearish** | Uptrend has stalled; 50-SMA is flattening and price cannot reclaim it |
| **Short-term trend** | 10-EMA 250.944, price −1.91%; lower highs 287.20→267.56→261.12→259.49→247.77 | **Bearish** | Clean four-step lower-high sequence; 09-17→09-22 bounce failed on 09-23 |
| **Momentum (MACD)** | MACD −2.353, signal −1.739, hist −0.614 | **Bearish** | Below zero and below signal since ~09-09; histogram's failed reset at −0.057 (09-22) is a bearish tell |
| **Momentum (RSI)** | 41.24 (prior trough 39.45 on 09-16) | **Weak, not oversold** | No mean-reversion trigger; one-session-old tentative positive divergence is unconfirmed |
| **Volatility** | ATR 5.746 (2.33% of price), down 42% from 9.995 (08-05); Boll width 6.70% | **Compressed / coiling** | Range expansion is building; direction unproven |
| **Band position** | Price 1.34 pts (+0.55%) above lower band 244.809 | **At support** | Riding the bottom rail; 09-16 closed *below* the band then snapped back +5.08% |
| **Volume** | 32.6M vs ~33.9M 19-session avg; VWMA 251.724, price −2.21% below | **Neutral-negative** | No distribution climax, no accumulation; volume-weighted holders underwater |
| **Immediate support** | 244.30 / 244.73 / 244.809 | **Critical** | Triple confluence; a close below opens 240.94 → 235.50 |
| **Immediate resistance** | 250.94 / 251.72 / 253.29 / 256.15 | **Layered** | Needs 253.29 to neutralize, 256.15 to flip medium-term |
| **Risk unit** | 1.5× ATR = 8.6 pts; 2× ATR = 11.5 pts | — | Size positions off ATR, not off old dollar stops |
| **Event risk** | Quarterly gaps: 2025-10-31 +9.6%, 2026-02-06 −9.7%, 2026-07-31 +15.3% | **High (inferred)** | Probable late-Oct catalyst — inference, not tool-confirmed; reduce size into it |
| **Actionable stance** | Neutral-to-bearish bias; range trade 244.3–256.2 | **Wait for resolution** | Bearish below 244.30 on >45M volume; bullish above 253.29, confirmed above 256.15 |

*This report is technical analysis of historical price data, not investment advice. All exact figures are from the verified snapshot dated 2026-09-28; derived percentages and retracement levels are arithmetic on that data and are labeled as such.*