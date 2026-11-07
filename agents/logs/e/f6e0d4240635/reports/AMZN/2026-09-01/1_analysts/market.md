# AMZN — Technical Deep-Dive Report
**Analysis date: 2026-09-01 | Last verified close: $254.92 | Verified via `get_verified_market_snapshot(2026-09-01)`**

---

## 0. Data Integrity Check

The verified snapshot and the `get_stock_data` CSV agree exactly on the latest session and on all historical rows I used (2026-09-01: O 254.83 / H 255.82 / L 251.93 / C 254.92, volume 31,700,100). **No discrepancies to flag.** All indicator values below are taken from the verified snapshot; all price-level and percentage claims are computed from tool-supplied OHLCV with dates cited.

| Snapshot indicator | Value (2026-09-01) |
|---|---|
| close_50_sma | 252.409 |
| close_200_sma | 238.787 |
| close_10_ema | 260.334 |
| macd / macds / macdh | 1.094 / 2.548 / −1.454 |
| rsi | 46.33 |
| boll / boll_ub / boll_lb | 264.547 / 277.487 / 251.607 |
| atr | 7.245 |
| vwma | 261.075 |

---

## 1. Selected Indicators and Why (8 chosen)

| # | Indicator | Role in this specific setup |
|---|---|---|
| 1 | **close_200_sma** | The strategic anchor. AMZN is in a long-term uptrend AND just survived a violent earnings re-rating; the 200-SMA tells us whether that re-rating held. |
| 2 | **close_50_sma** | The medium-term pivot. It bottomed on 2026-07-30 (246.38) and is now rising ~$0.40/day — it is the first real line of defense under price. |
| 3 | **close_10_ema** | Captures the *current* short-term regime, which has flipped bearish (price below it since 2026-08-31). Fast, noisy, but essential for timing. |
| 4 | **macd** | Trend/momentum backbone; shows the impulse that drove the August advance is decaying. |
| 5 | **macds** | The signal line is what converts MACD into a *trigger*. The bearish cross on 2026-08-17 is the single clearest dated deterioration event. |
| 6 | **rsi** | With price mid-range and not at an extreme, RSI's job here is to tell us **whether this dip is oversold yet** — it is not (46.3). |
| 7 | **atr** | Volatility nearly doubled post-earnings (6.89 → 9.95), then contracted to 7.25. This directly sets stop distance and position size, and flags that the "post-earnings volatility premium" is bleeding out. |
| 8 | **vwma** | The volume-weighted marginal cost basis. Price sitting **below** VWMA is the cleanest evidence that recent buying is underwater and distribution is occurring. |

*Deliberately excluded:* MACD histogram (fully derivable from #4/#5), StochRSI (redundant with RSI), and Bollinger upper/lower as *separate* selections — the snapshot supplies those levels, so I use them as context rather than spending two of my eight slots.

---

## 2. Price Action Narrative

### Phase 1 — February to July 2026: a long, low-quality base
- The window opens at **$242.96 (2026-02-02)** and immediately breaks down to **$198.79 (2026-02-13)** — a −18.2% drawdown in nine sessions, with volume spiking to 179.2M on 2026-02-06.
- From that February low, AMZN built a **five-month ascending base**, rallying to **$274.00 (2026-05-28)** and then chopping in a wide $226–$275 range. The June drawdown was severe: **$274.00 (2026-05-28) → $227.01 (2026-06-25)**, −17.1%, with 248.4M shares traded on 2026-06-26 (a likely index/rebalance event).
- The July sequence into earnings was *deteriorating*: closes fell from $254.96 (2026-07-15) to **$226.65 (2026-07-29)**, a −11.1% slide, with RSI printing **33.31 on 2026-07-29**.

### Phase 2 — The earnings gap (2026-07-30/31): a genuine regime change
- **2026-07-30 close: $235.50. 2026-07-31 open: $265.00** — a **+12.5% opening gap**, closing at **$271.58 (+15.33% on the day)** on **129.05M shares** (vs. a July average around 37–38M, i.e. ~3.4× normal).
- Momentum carried to **$284.02 close on 2026-08-03** and an intraday high of **$287.20** — the highest close and highest high in the entire Feb–Sep window. The move from the 2026-07-29 close ($226.65) to the 2026-08-03 close was **+25.3% in three sessions**.
- RSI hit **72.23 on 2026-08-03** — its only overbought reading of the period.

### Phase 3 — August to today: a controlled but unrelenting fade
- From the **$284.02** close (2026-08-03) to **$254.92** (2026-09-01), AMZN has lost **−10.25%** over 20 sessions. From the $287.20 intraday high, the drawdown is **−11.24%**.
- **The 2026-08-28 session looked like a resolution:** +$10.17 (+3.97%) to $266.43 on 49.5M shares, intraday high $267.56. **It failed.** The next two sessions gave back −2.50% (2026-08-31) and −1.87% (2026-09-01), fully erasing the rally ($256.26 on 2026-08-27 → $254.92 on 2026-09-01, net −0.52%).
- **2026-09-01's close of $254.92 is the lowest close since 2026-07-14** ($247.49). The prior lower close was $254.96 on 2026-07-15 — so price has round-tripped the entire pre-earnings level.

**Critical structural observation:** the 2026-07-31 gap leaves an unfilled zone between the **2026-07-30 high of $239.82** and the **2026-07-31 low of $262.01** ($22.19 wide). At $254.92, price has retraced only about **one-third** of that gap from above. The remaining ~$15 of unfilled gap is a live magnet *below* current price — and it terminates almost exactly at the 200-SMA.

---

## 3. Trend Structure — Three Timeframes, Three Different Answers

| Horizon | Indicator | Reading | Verdict |
|---|---|---|---|
| Long-term | close_200_sma = **238.787**, rising from 233.03 (2026-07-06) | Price +6.76% above it | **Uptrend intact** |
| Medium-term | close_50_sma = **252.409**, rising from its 246.38 trough (2026-07-30) | Price +1.00% above it | **Uptrend, but being tested** |
| Short-term | close_10_ema = **260.334**, falling from 267.18 (2026-08-12) | Price −2.08% below it | **Downtrend** |

- **Golden cross is intact:** 50-SMA (252.41) − 200-SMA (238.79) = **+$13.62**. Both averages are rising. However, this spread *narrowed* from $22.16 on 2026-07-06 — the July collapse compressed it, and the August rally has not yet re-expanded it. It is not at risk of a death cross (the 50-SMA would need to fall ~5.7%), but the cushion is thinner than it looks.
- **10-EMA vs 50-SMA is the level to watch.** The 10-EMA is declining roughly $0.5–0.9 per session while the 50-SMA rises ~$0.40 per session. The gap is currently $7.93. **If price merely holds flat, these two averages converge in roughly 1–2 weeks and a short-term bearish cross would print** — mechanically confirming what price action already shows.
- **The 50-SMA's rise is on borrowed time.** Its current upward slope is being driven by *low* July prices (~$243–250) rolling out of the window. Those get replaced by ~$255 today. But by mid-to-late September, the **$274–$284 closes of early August** begin rolling out and get replaced by today's ~$255. **The 50-SMA will likely flatten and roll over near the end of September unless price recovers materially.** That is a structural argument against complacency.

**Summary:** this is a **pullback inside a longer uptrend**, not yet a trend break — but it is a pullback that has now eaten through the entire short-term trend structure and is knocking on the medium-term one.

---

## 4. Momentum — Deteriorating, and Not Yet Washed Out

**MACD (1.094) vs Signal (2.548): histogram −1.454.**
- MACD peaked at **8.432 on 2026-08-11** and has fallen for **14 of the last 15 sessions**.
- The **bearish crossover occurred on 2026-08-17** (histogram flipped from +0.392 on 2026-08-14 to −0.310 on 2026-08-17).
- The histogram bottomed at **−1.683 on 2026-08-27**, briefly narrowed to −1.114 (2026-08-28) and −1.154 (2026-08-31), then **re-widened to −1.454 on 2026-09-01**. This is important: the 8/28 rally failed to generate a sustained momentum-hook. **There is no positive MACD divergence and no confirmed momentum trough.**
- MACD remains above zero (1.094), so the *medium-term* trend is still technically positive — but it is falling fast and would cross zero within a week if the current pace continues.

**RSI: 46.33.**
- RSI went **72.23 (2026-08-03) → 33.31 lows are not being retested**; the recent sequence is 55.85 (8/28) → 50.08 (8/31) → 46.33 (9/1).
- **RSI has moved below 50 but is nowhere near the 30 oversold threshold.** There is no mechanical mean-reversion signal here. Historically in this dataset, the only meaningful oversold readings were 33.31 (2026-07-29) and 36.5–37.5 (2026-07-24/28), both followed by the earnings gap — so the bar for "washed out" in AMZN has recently been ~33–37, not 46.
- No clean RSI divergence exists: price and RSI both made lower highs after 2026-08-03.

**Why this matters:** in a strong uptrend, RSI holding in the 40s is a *buying* zone. Here, because MACD is re-accelerating lower and price just failed a breakout attempt at $266–267, the 40s RSI reads as **momentum still bleeding, not as value**.

---

## 5. Volatility & Bollinger Structure

- **ATR has contracted from 9.98 (2026-08-05) to 7.245 (2026-09-01)** — a 27% decline. The post-earnings volatility premium is dissipating, and the daily range is normalizing toward the pre-earnings ~$6.9–7.5 regime.
- ATR as a % of price: **2.84%**. For risk sizing: 1×ATR ≈ $7.25, 2×ATR ≈ $14.49.
- **Bollinger:** middle **264.547**, upper **277.487**, lower **251.607**. Bandwidth is ~$25.88 (9.8% of the mid-band) — **wide**, a direct legacy of the earnings gap. %B = **12.8%** — price is in the lower quartile of the band but **has not tagged the lower band** (251.61 vs close 254.92).
- **The Bollinger middle (264.55) is now above the 10-EMA (260.33) and coincides with the 8/13–8/14 congestion (~$262–266).** That makes **$264.5–266.5 a dense, well-defended overhead shelf** — and its rejection on 2026-08-28 (high 267.56) confirms it.

**Interpretation:** wide bands + falling ATR = a market that is *coiling* rather than trending. The resolution is more likely to be a directional range expansion than a slow grind. The lower band at **$251.61** sitting almost exactly on the **50-SMA at $252.41** makes that the pivotal zone.

---

## 6. Volume / Participation — The Weak Link

- **VWMA = 261.075, which is $6.16 (2.36%) ABOVE the last close.** The volume-weighted average price paid by recent participants is above the market. **Recent buyers are, on aggregate, underwater — a distribution signature, not accumulation.**
- VWMA peaked at **272.05 on 2026-08-20** and has declined for **eight consecutive sessions** to 261.08. Price has stayed below VWMA since 2026-08-21.
- **Post-earnings volume has fully normalized:** the 2026-07-31 spike (129.05M) and 2026-08-03 (90.83M) have decayed to **21.5M (2026-08-26) and 31.7M (2026-09-01)**. The 2026-09-01 decline came on the **lightest volume in over a month** — which cuts both ways: it is not panic liquidation, but it is also **no capitulation and no volume-backed reversal**.
- July's average volume (~37.8M) and the recent August average (~38.6M) are effectively identical. **The earnings breakout did not produce durable volume expansion** — the higher price level is being held by the same crowd, not a new one.

**The one modest positive:** the pullback is occurring on *declining* volume, which is characteristic of orderly profit-taking rather than forced selling. The $266.43/49.5M session on 2026-08-28 was the highest-volume up day of the fade — and it failed. That keeps the distribution read dominant.

---

## 7. Key Levels (all derived from tool OHLCV/indicator output)

**Resistance (ascending):**
1. **$255.82** — 2026-09-01 intraday high (immediate)
2. **$256.26** — 2026-08-27 close
3. **$257.04–$258.58** — 2026-08-21 low / 2026-08-19 low cluster
4. **$260.33 / $261.08** — 10-EMA / VWMA (the momentum gate)
5. **$262.01** — 2026-07-31 low = bottom edge of the unfilled gap
6. **$264.55** — Bollinger middle
7. **$266.43–$267.56** — 2026-08-28 close / high (the failed-breakout ceiling)
8. **$272.26–$272.27** — 2026-08-11 close; $277.49 Bollinger upper; $284.02 / $287.20 all-time-window highs.

**Support (descending):**
1. **$254.92** — current close
2. **$252.41 / $251.61 / $251.93** — 50-SMA / Bollinger lower / 2026-09-01 low → **a $0.80-wide triple confluence. The single most important line on the chart.**
3. **$248.00** — 2026-07-16 and 2026-07-20 lows
4. **$245.34–$246.02** — 2026-07-10 close / 2026-07-13 low
5. **$239.82–$238.79** — 2026-07-30 high **/ 200-SMA** → **the structural line in the sand**
6. **$232.79–$226.16** — June/July lows (a break of #5 opens this).

---

## 8. Actionable Playbook

### Setup A — Trend-continuation long at the confluence (highest probability, needs confirmation)
- **Trigger zone:** $251.50–$255.50, i.e. the 50-SMA/Bollinger-lower/9-01-low cluster.
- **Confirmation required (do not buy blind):** a daily close back above **$256.26** AND the MACD histogram narrowing for two consecutive sessions. Without that, you are catching a knife into an intact short-term downtrend.
- **Stop:** **$246.50** (below the $248.00 double-bottom from 2026-07-16/07-20, ~1 ATR of buffer under the 50-SMA).
- **Risk from $254.92:** $8.42 (1.16 ATR) = **3.3%**.
- **Targets:** T1 **$264.55** (Bollinger middle, +$9.63, R:R 1.14); T2 **$272.26** (+$17.34, R:R 2.06); T3 **$277.49** (+$22.57, R:R 2.68).
- **Assessment:** favorable to T2/T3 only if the $264–267 shelf is reclaimed, because that is where the last two rallies died.

### Setup B — Momentum re-entry on reclaim (cleanest signal-to-noise)
- **Wait for** a daily close above **$261.08 (VWMA)** and **$262.01 (gap floor)** simultaneously, ideally with volume > 45M.
- **Stop:** $254.00 (below the 9/1 close).
- **Target:** $272.26, then $277.49. This trades the "distribution ending" thesis and requires no bottom-picking.

### Setup C — Breakdown short / hedge trigger
- **Trigger:** a daily **close below $251.50** (breaking both the 50-SMA and the lower Bollinger band in one move).
- **Targets:** $248.00 → $245.50 → **$239.82/238.79** (200-SMA + gap-fill terminus — a natural place to take profit, not to add).
- **Stop:** $258.00 (back above the 8/21–8/27 congestion).
- **Note:** this is a counter-trend trade relative to the 200-SMA. Size it as a hedge/trim signal rather than a conviction short.

### Setup D — Risk management for existing longs
- **Trailing stop:** $246.50 (same 1.16-ATR logic). With ATR at 7.245, anything tighter than ~$7 will be noise-stopped — **2026-09-01's own range was just $3.89**, but the 2026-08-28 range was $9.78. Size for the wider days.
- **Trim discipline:** the 200-SMA at $238.79 and the 2026-07-30 high of $239.82 form the boundary between "healthy pullback" and "failed breakout." **A close below $238.79 invalidates the entire post-earnings structure** and would argue for reducing exposure to core size.

---

## 9. What Would Change the View

| Development | Signal |
|---|---|
| Close > $261.08 (VWMA) + MACD histogram turning positive | **Short-term downtrend over.** Fade invalidated. |
| Close > $267.56 (8/28 high) on volume > 50M | **Breakout confirmed.** Distribution thesis dead. |
| RSI pushing below ~37 while price holds > $251 | **Washed-out dip** — historically the highest-quality entry zone in this window (cf. 2026-07-24–07-29). |
| Close < $251.50 | **Confluence broken.** Target $245.5 → $239.8/$238.8. |
| Close < $238.79 (200-SMA) | **Post-earnings structure failed.** Strategic trend damage. |
| 10-EMA crossing below 50-SMA (~1–2 weeks out at current trajectory) | Mechanical short-term confirmation of the downtrend. |

---

## 10. Bottom Line

AMZN is a **long-term uptrend (+6.76% above a rising 200-SMA) wearing a short-term downtrend (−2.08% below a falling 10-EMA)**. The August earnings gap created a genuine level shift, but the market has spent 20 sessions giving back 10.25% of it, and the 2026-08-28 breakout attempt at $267.56 was rejected in two sessions. Every short-term measure points the same way — bearish MACD cross (2026-08-17), RSI below 50 (46.33), price below VWMA by 2.36% with VWMA falling for eight straight sessions, and MACD histogram *re-widening* negative on 2026-09-01 rather than curling up.

Yet nothing has broken structurally. The 50-SMA at $252.41, the lower Bollinger band at $251.61, and the 2026-09-01 low of $251.93 form a **$0.80-wide confluence directly under price** — and the 200-SMA at $238.79 sits almost exactly where the unfilled earnings gap from 2026-07-30/31 terminates. That is an unusually clean map: **$251.6–$252.4 is the decision line, $238.8–$239.8 is the structural line.**

The tactical conclusion: **be patient, not anticipatory.** The reward-to-risk for buying at $254.92 is mediocre (R:R 1.14 to the first real target). It becomes attractive (>2:1 to $272) either on a **flush into the high-$240s** or on a **confirmed reclaim of $261–262**. Given declining ATR (7.25, down 27% from the 2026-08-05 peak) and wide Bollinger bands, a range-expansion move is likely within the next 1–2 weeks — position sizing should reflect that, and stops should be placed at mechanical 1–2 ATR distances, not at round numbers.

---

### Key Points Summary

| Category | Indicator / Metric | Value (2026-09-01) | Reference Point | Signal |
|---|---|---|---|---|
| Long-term trend | close_200_sma | 238.787 | Rising from 233.03 (07-06) | **Bullish** — price +6.76% above |
| Medium-term trend | close_50_sma | 252.409 | Rising from 246.38 trough (07-30) | **Neutral-positive** — price only +1.00% above |
| Short-term trend | close_10_ema | 260.334 | Falling from 267.18 (08-12) | **Bearish** — price −2.08% below |
| Trend cross | 50-SMA − 200-SMA | +13.62 | Was +22.16 on 07-06 | Golden cross intact but compressed |
| Momentum (level) | macd | 1.094 | Peak 8.432 (08-11) | Above zero, decaying fast |
| Momentum (trigger) | macds / hist | 2.548 / −1.454 | Bear cross 08-17; hist re-widened 09-01 | **Bearish, not bottoming** |
| Oscillator | rsi | 46.33 | 72.23 peak (08-03); recent lows 33–37 | Below 50, **not oversold** |
| Volatility | atr | 7.245 (2.84% of price) | Peak 9.98 (08-05) | Contracting — coiling |
| Bands | boll / ub / lb | 264.547 / 277.487 / 251.607 | %B = 12.8% | Lower quartile, band untagged |
| Participation | vwma | 261.075 | Peak 272.05 (08-20), falling 8 sessions | **Distribution** — price 2.36% below |
| Price | Last close | 254.92 (H 255.82 / L 251.93) | Lowest close since 07-14 | Down −1.87% on day, −10.25% from 08-03 peak |
| Failed breakout | 08-28 high | 267.56 → close 254.92 | −4.7% in 2 sessions | Bull trap confirmed |
| Critical support | Confluence | **251.61 / 251.93 / 252.41** | 50-SMA + Boll lower + 09-01 low | **The decision line** |
| Structural support | Confluence | **238.79 / 239.82** | 200-SMA + 07-30 high (gap terminus) | **Line in the sand** |
| Primary resistance | Cluster | 260.33 / 261.08 / 262.01 | 10-EMA + VWMA + gap floor | **Momentum gate** |
| Major resistance | Cluster | 264.55 / 266.43 / 267.56 | Boll mid + 08-28 close/high | Where rallies die |
| Tactical bias | — | — | — | **Neutral-to-bearish near term; bullish structurally above $238.79** |
| Preferred action | — | — | — | **No chase.** Buy $251.5–$255.5 only on a reclaim of $256.26; or wait for a $261+ reclaim; trim below $251.50 |