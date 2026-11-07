# AMZN — Technical Analysis Report
**As of the close of 2026-07-29 | Verified snapshot used as source of truth**

---

## 1. Snapshot of the Current Session

| Field | Value |
|---|---|
| Open | 229.32 |
| High | 232.82 |
| Low | 226.16 |
| **Close** | **226.65** |
| Volume | 44,957,500 |
| Prior close (2026-07-28) | 230.86 |
| Session change | −4.21 (−1.82%) |

AMZN closed at **226.65**, its **lowest close since 2026-04-08** (close 221.25). The stock has now printed **five consecutive lower closes** (2026-07-23: 233.66 → 07-24: 232.11 → 07-27: 231.39 → 07-28: 230.86 → 07-29: 226.65).

Measured drawdowns (all derived from the frozen OHLCV rows):
- From the 2026-07-22 close of 244.85 → **−7.43%** in five sessions
- From the 2026-07-20 close of 249.99 → **−9.34%** in seven sessions
- From the 2026-07-15 close of 254.96 → **−11.10%** in ten sessions
- From the highest close in the dataset, 274.99 (2026-05-06) → **−17.58%**
- From the intraday high of 258.08 (2026-07-16) → **−12.18%**

---

## 2. Indicator Selection and Rationale (8 indicators)

| Indicator | Why it matters right now |
|---|---|
| **close_10_ema** (236.46) | Captures the speed of the current breakdown; price is already 4.2% below it, defining the short-term downtrend |
| **close_50_sma** (246.97) | Medium-term trend benchmark; it is falling fast and price is 8.2% below it |
| **close_200_sma** (234.66) | Strategic/macro trend line; price has now lost it for five sessions — the single most important level in this report |
| **macd / macds** (−3.75 / −1.76) | Confirms momentum regime change with a dated bearish crossover (2026-07-23) |
| **rsi** (33.31) | Gauges how stretched the sell-off is; approaching but not at the 30 oversold threshold |
| **boll_lb** (227.45) | Price closed *below* the lower band — a statistically stretched condition that also frames mean-reversion risk |
| **atr** (6.89) | Essential for position sizing and stop placement given realized volatility |
| **vwma** (242.21) | Volume-weighted benchmark; price well below it confirms sellers, not noise, are in control |

I deliberately avoided stacking redundant oscillators (e.g., RSI + stochastic) and avoided adding both MACD line and histogram as separate "independent" signals — the signal line is included only to date the crossover.

---

## 3. Trend Structure: A Textbook Sequence of Lower Highs and Lower Lows

The 2026 data shows a clear topping structure on the medium-term horizon:

**Lower highs:**
- Intraday high **278.56** (2026-05-05), close high **274.99** (2026-05-06)
- Intraday high **274.50** (2026-05-28)
- Intraday high **258.08** (2026-07-16), close 249.89
- Current price 226.65 is roughly **12% below** the July high

**Lower lows:**
- June swing low: intraday **225.55** (2026-06-25), close 227.01
- Today's low **226.16** — a higher low by only **0.61 points**, i.e., the June low is being retested almost exactly

This is important nuance: the June low has *marginally* held so far (226.16 vs 225.55), but the close at 226.65 is essentially sitting on it. This is the pivot of the entire setup.

**A significant unfilled gap sits overhead.** On 2026-07-23 the stock opened at 236.26 versus the 2026-07-22 close of 244.85 (−8.59, −3.5%), and the 07-23 high of 238.35 never traded back up to the prior close. The **238.35–244.85** zone is therefore an overhead supply pocket, not just a moving-average level.

---

## 4. Support and Resistance Map (all levels sourced from tool data)

**Resistance (stacked, in order):**
1. **230.86–232.11** — the 07-28 / 07-24 closes; the immediate "shelf" price just fell through
2. **232.82** — today's high
3. **234.66** — 200 SMA (now resistance, lost 5 sessions ago)
4. **236.46** — 10 EMA
5. **238.35** — 2026-07-23 high (bottom of the gap)
6. **242.21 / 242.72** — VWMA and Bollinger middle (20 SMA); a tight confluence
7. **246.97** — 50 SMA
8. **249.89–254.96** — 07-16 close / 07-15 close

**Support:**
1. **225.55–226.16** — June 25 low and today's low. Immediate line in the sand
2. **221.25** — 2026-04-08 close (next lower close in the dataset)
3. **219.62** — 2026-04-08 intraday low
4. **213.77–209.77** — April 2026 consolidation (04-07 close 213.77; 04-02 close 209.77) if the downtrend extends

---

## 5. Moving-Average Analysis — The Core of the Bearish Case

**10 EMA (236.46):** Fell from 247.60 (2026-07-21) to 236.46 in six sessions — a −4.5% collapse in the average itself. Price at 226.65 is **4.15% below** it. The 10 EMA is now pointing sharply down, which is the classic "fast average rolling over" signature of a fresh impulse leg lower rather than a shallow pullback.

**50 SMA (246.97):** Down from **257.10 on 2026-06-18** to 246.97 — a **−10.13 point** decline in roughly six weeks, and it is still declining ~0.4–0.75 points per session. Price is **8.23% below** it.

**200 SMA (234.66):** Slowly *rising* (232.50 on 2026-06-12 → 234.66 today). This is the crucial divergence: the long-term benchmark is still climbing while price collapses beneath it.

**Golden-cross status:** The 50 SMA (246.97) is still **above** the 200 SMA (234.66), so the medium-term golden-cross structure is technically intact. **But the spread has compressed from about 24.3 points (2026-06-18: 257.10 vs 232.80) to about 12.3 points today.** With the 50 SMA falling and the 200 SMA rising, the gap is closing at roughly 0.5–0.6 points per session. At the current pace a **death cross would be approached in roughly a month** if nothing changes. I flag this as a *trajectory*, not a forecast — a sharp reversal would re-steepen the 50 SMA.

**Price vs 200 SMA:** Closes of 233.66 (07-23), 232.11 (07-24), 231.39 (07-27), 230.86 (07-28), 226.65 (07-29) are all below the 200 SMA. Notably, this is the **second** break of the 200 SMA this year: a first break occurred 2026-06-22 through 2026-06-30 (e.g., 06-25 close 227.01 vs 200 SMA 232.80), after which price reclaimed it and rallied to 254.96 by 07-15. That precedent means a failed second break is a legitimate bull scenario — but the current break is accompanied by *accelerating* momentum, unlike the June episode's basing.

---

## 6. Momentum: MACD Confirms a Dated Regime Shift

| Date | MACD | Signal | Histogram |
|---|---|---|---|
| 2026-07-15 | +0.260 | −1.864 | +2.124 |
| 2026-07-20 | +0.824 (local peak) | −0.622 | +1.446 |
| 2026-07-22 | +0.559 | −0.158 | +0.717 |
| **2026-07-23** | **−0.530** | **−0.233** | **−0.297 (bearish crossover)** |
| 2026-07-24 | −1.500 | −0.486 | −1.014 |
| 2026-07-27 | −2.301 | −0.849 | −1.452 |
| 2026-07-28 | −2.945 | −1.268 | −1.677 |
| **2026-07-29** | **−3.751** | **−1.765** | **−1.986** |

Three things stand out:

1. **The bullish MACD cross that began around 2026-07-15 (MACD crossing above signal) has been fully reversed** — the bearish crossover dates to **2026-07-23**.
2. The MACD line has gone from +0.82 (07-20) to −3.75 in seven sessions, a **4.57-point swing** — that is momentum *collapse*, not drift.
3. The histogram is **expanding negatively every session** (−0.30 → −1.01 → −1.45 → −1.68 → −1.99). There is no sign of deceleration yet. Traders waiting for a "momentum trough" have no evidence for it as of this close.

---

## 7. RSI: Approaching Oversold, But Not There — And No Divergence Yet

RSI has deteriorated with unusual speed:

- 2026-07-15: **60.14** (the local peak)
- 2026-07-20: 54.04
- 2026-07-22: 48.40
- 2026-07-23: 38.62 (single-session drop of ~9.8 points — a genuine momentum break)
- 2026-07-28: 36.54
- **2026-07-29: 33.31**

**Critical nuance on divergence:** A bullish divergence requires price to make a lower low while RSI makes a higher low. Comparing today to the June low:
- Price: 226.65 now vs 227.01 close on 2026-06-25 → **lower**
- RSI: 33.31 now vs 33.63 on 2026-06-25 → **also marginally lower**

So **there is no confirmed bullish divergence**. The RSI is simply confirming the price weakness. RSI 33.31 is above the 30 oversold threshold and above the 2026-06-10 reading of 32.46, so this is "stretched but not exhausted." Historically in this dataset RSI readings of 32–37 have produced sharp reflex bounces (e.g., 06-10 32.46 → 06-15 43.22; 06-25 33.63 → 06-29 46.20), which is why an *oversold bounce* is a legitimate tactical scenario, but those bounces did **not** reverse the larger 2026 downtrend.

---

## 8. Bollinger Bands: A Close Below the Lower Band

| Band | Value |
|---|---|
| Upper | 257.996 |
| Middle (20 SMA) | 242.723 |
| **Lower** | **227.449** |
| Close | 226.650 |

The close is **below the lower band by 0.80 points (−0.35%)**. Band width is approximately **12.58%** of the middle line ((257.996 − 227.449) / 242.723), which is wide — realized volatility is elevated, so the bands are not tight enough for a classic "squeeze breakout." Instead, this is a **trend-riding-the-lower-band** configuration. The recommended interpretation: prices can and do ride the lower band in strong downtrends; a close below the band is *not* by itself a buy signal. It does, however, raise the probability of a violent short-covering snap toward the middle band (242.72) if any positive catalyst appears.

Also note the **lower band itself has started rising** (228.03 on 07-20 → 227.45 today) while price fell through it — the band is flattening because the 20-day window is still absorbing the July rally. This is a mechanical artifact, not support.

---

## 9. Volume Analysis: Distribution Is Expanding

From the raw OHLCV:
- 20-session average volume (2026-07-01 → 2026-07-29): approximately **39.1 million**
- 2026-07-29 volume: **44.96 million** — about **15% above** that average
- Down days on this leg: 07-23 **47.47M**, 07-28 **44.52M**, 07-29 **44.96M** — each above the recent average
- Quiet up/recovery days earlier in July were 27.7M–34.6M (e.g., 07-21: 27.73M, 07-14: 30.11M, 07-20: 32.41M)

That pattern — **heavy volume on declines, light volume on advances** — is distribution. The **VWMA (242.21)** confirms it: price has been *below* VWMA since 2026-07-23 after four sessions above it (07-17: 244.79 → 07-22: 247.03). A VWMA of 242.21 means the average *volume-weighted* dollar has been paid at a level **6.42% above** the current price — the average buyer over this window is underwater.

**Volume caveats to be honest about:** two sessions in this dataset are clearly non-representative — 2026-06-26 (248.4M, ~5x normal) and 2026-02-05/02-06 (103.5M / 179.2M). These look like structural events (index rebalancing / news-driven repricing) and should not be treated as genuine trend-confirmation. Also, 2026-02-06 shows a brutal event risk profile worth remembering: open 202.70 vs prior close 222.69 (−8.98% gap) on 179.2M shares. **This name gaps hard on news — a stop resting just below the June low is exposed to that risk.**

---

## 10. Volatility and Risk Sizing

- **ATR (14) = 6.892 points = 3.04% of the 226.65 close.**
- ATR has *contracted* from its local peak of 8.591 on 2026-06-29 to 6.892 today. The current sell-off is therefore happening on somewhat lower per-session realized range than June — it is more of a persistent one-way grind than a volatility explosion. That is consistent with distribution rather than capitulation, and capitulation is usually what marks lows.

**Sizing implications:**
- A 1×ATR stop from 226.65 = 219.76 — sits just above the 219.62 April low, i.e., a natural but tight placement.
- A 2×ATR stop = 212.87 — below the April consolidation, safety from noise but a 6.1% risk.
- For risk-parity sizing: to risk 1% of equity with a 2×ATR stop (13.78 points), position size ≈ 0.073% of equity per point, i.e., roughly **1 share per $1,378 of equity risk budget at 1% risk**.

---

## 11. Actionable Scenarios

### Scenario A — Bearish continuation (primary, given the evidence)
**Trigger:** A close below **225.55** (the 2026-06-25 low), confirmed by a close below 226.16 (today's low).
**Rationale:** Five consecutive lower closes, bearish MACD crossover with expanding negative histogram, no RSI divergence, price below 10 EMA / 50 SMA / 200 SMA / VWMA / Bollinger middle, and distribution volume.
**Targets:** 221.25 (04-08 close) → 219.62 (04-08 low) → 213.77 (04-07 close).
**Invalidation / stop:** back above 232.82 (today's high) and then a close above 234.66 (200 SMA).

### Scenario B — Oversold reflex bounce (tactical)
**Trigger:** A close back above **230.86–232.11** (the shelf it just broke) and ideally the 07-29 high of 232.82.
**Rationale:** The close is 0.35% below the Bollinger lower band, RSI 33.31, and the June low at 225.55 has (barely) held. This dataset shows RSI 32–37 tends to produce 8–13 point bounces (06-10 → 06-15: +10.7 RSI points; 06-25 → 06-29: +12.6).
**Targets:** 234.66 (200 SMA) → 236.46 (10 EMA) → 238.35 (gap fill start). **The 238.35–244.85 gap is the ceiling for any bounce** unless volume expands decisively on the upside.
**Stop:** below 225.55. Treat this as a counter-trend trade only — the trend, momentum and volume evidence all oppose it.

### Scenario C — Trend repair (needs much more work)
Only becomes valid on a **close above 242.72** (Bollinger middle) with VWMA (242.21) reclaimed and MACD back above its signal line. At that point the 50 SMA at 246.97 becomes the next test and the death-cross risk discussed in Section 5 recedes.

### What would make me wrong on the bearish bias
1. A defended retest of 225.55 with a **lower-volume** down day, followed by a strong reversal close.
2. MACD histogram contracting for 2–3 sessions while price holds above 225.55 (momentum trough).
3. Reclaim of the 200 SMA (234.66) within the next few sessions — the June episode proved this name can V-bottom off the 200 SMA.
4. A positive earnings/news catalyst (flagged: this instrument has shown −9% single-day gap risk on 2026-02-06).

### What would strengthen the bearish bias
1. A close below 225.55 on volume **above** 45M (today's level).
2. Failure of any bounce in the 230.86–234.66 zone (lower high confirmed).
3. 50 SMA crossing below the 200 SMA.
4. RSI breaking below 32.46 (the 2026-06-10 low) with price making lower lows.

---

## 12. Summary Table

| Category | Indicator / Metric | Value (2026-07-29) | Signal | Interpretation |
|---|---|---|---|---|
| **Price** | Close | 226.65 | Bearish | Lowest close since 2026-04-08 (221.25); 5 straight lower closes |
| **Price** | Session range | 232.82 / 226.16 | Bearish | Closed near the low; −1.82% on the day |
| **Price** | Drawdown from 07-22 close (244.85) | −7.43% | Bearish | Fast, one-directional decline |
| **Price** | Drawdown from 05-06 close high (274.99) | −17.58% | Bearish | Confirmed medium-term downtrend |
| **Short MA** | close_10_ema | 236.46 | Bearish | Price 4.15% below; EMA falling ~1.5 pts/session |
| **Medium MA** | close_50_sma | 246.97 | Bearish | Price 8.23% below; down 10.13 pts since 06-18 |
| **Long MA** | close_200_sma | 234.66 | **Bearish (key)** | Price below for 5 sessions; 200 SMA still *rising* — bad divergence |
| **MA structure** | 50 SMA − 200 SMA spread | +12.31 pts | Weakening | Golden cross intact but compressing; was ~24.3 pts on 06-18 |
| **Momentum** | MACD | −3.751 | Bearish | Fell from +0.824 (07-20) in seven sessions |
| **Momentum** | MACD signal | −1.765 | Bearish | Bearish crossover dated **2026-07-23** |
| **Momentum** | MACD histogram | −1.986 | Bearish | Expanding negative 5 sessions running — no deceleration |
| **Momentum** | RSI | 33.31 | Bearish / nearing oversold | Above 30; **no bullish divergence** vs 06-25 (RSI 33.63) |
| **Volatility** | ATR (14) | 6.892 (3.04% of price) | Elevated but contracting | Down from 8.591 (06-29); grind, not capitulation |
| **Volatility** | Bollinger upper / middle / lower | 257.996 / 242.723 / 227.449 | Bearish | Close is 0.80 pts **below the lower band**; riding the band |
| **Volume** | VWMA | 242.207 | Bearish | Price 6.42% below VWMA → average buyer underwater |
| **Volume** | Session volume vs 20-day avg | 44.96M vs ~39.1M | Bearish | +15%; distribution (heavy down-day, light up-day volume) |
| **Support** | Immediate | 225.55–226.16 | Pivot | June 25 low / today's low — the line in the sand |
| **Support** | Next | 221.25 → 219.62 | — | 2026-04-08 close and low |
| **Resistance** | 1st zone | 230.86–232.82 | — | Broken shelf + today's high |
| **Resistance** | 2nd zone | 234.66 / 236.46 | — | 200 SMA / 10 EMA confluence |
| **Resistance** | 3rd zone | 238.35–244.85 | — | Unfilled gap from 2026-07-23 (open 236.26 vs prior close 244.85) |
| **Resistance** | 4th zone | 242.21–242.72 / 246.97 | — | VWMA + Bollinger middle / 50 SMA |
| **Key risk** | Gap/event risk | 2026-02-06 precedent | Caution | Opened at 202.70 vs prior close 222.69 (−8.98%) on 179.2M shares — tight stops are vulnerable |

**Bottom line:** AMZN is in a confirmed short-term and medium-term downtrend with accelerating bearish momentum, expanding distribution volume, and price pressing a near-exact retest of the June low (225.55) while sitting below the Bollinger lower band. The bullish case rests entirely on (a) the June low holding, (b) the fact that this same 200-SMA break was bought in late June, and (c) genuine short-term oversold conditions. There is **no confirmed divergence or momentum trough yet**, so the trend-following evidence is heavier than the mean-reversion evidence. Favor a defensive stance with triggers as defined in Section 11, and size positions off the 3.04%-of-price ATR rather than absolute point targets.