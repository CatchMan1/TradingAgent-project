# AMZN — Technical Analysis Report
**As-of date: 2024-02-28 | Verified close: $173.16** | Data window: 2023-08-01 → 2024-02-28 (146 sessions)

---

## 1. Verified Snapshot (source of truth)

Latest session (2024-02-28): **Open 172.44 / High 174.05 / Low 172.27 / Close 173.16 / Volume 28.18M**

| Indicator (2024-02-28) | Value |
|---|---|
| close_10_ema | 172.04 |
| close_50_sma | 159.97 |
| close_200_sma | 139.53 |
| macd | 4.111 |
| macds (signal) | 4.319 |
| macdh | −0.208 |
| rsi | 61.71 |
| boll (20 SMA) | 169.93 |
| boll_ub | 179.85 |
| boll_lb | 160.00 |
| atr | 3.42 |
| vwma | 171.45 |

*(Supplementary band/volume fields are included for level work; the eight formally selected indicators are listed in §2. All figures above are identical to the frozen snapshot — no conflicts between the OHLCV pull and the verified snapshot were found.)*

---

## 2. Indicator Selection & Rationale (8 selected)

| # | Indicator | Why it fits this market context |
|---|---|---|
| 1 | **close_10_ema** | AMZN is in a fast, post-earnings-gap uptrend where price has been riding a short average. The 10 EMA is the operative "trend-vs-pause" line (price crossed below it 2/20–2/21 and back above on 2/22), so it is the most actionable near-term filter. |
| 2 | **close_50_sma** | Confirms the medium-term trend and, critically, sits within 3 cents of the lower Bollinger band (~160) — a genuine confluence level rather than a single-line reference. |
| 3 | **close_200_sma** | Long-term regime check; distinguishes "healthy pullback in a bull leg" from "trend failure." Also quantifies how stretched price is (+24.1%). |
| 4 | **macd** | Establishes momentum regime (above/below zero) and the crossover state vs. the signal line — essential because price is consolidating, not trending cleanly. |
| 5 | **macdh** | The histogram is the cleanest read on *deceleration* here: it flipped negative 2024-02-16 and has re-widened, which the line alone understates. |
| 6 | **rsi** | With price at the top of a 4-week range, RSI tells us whether the consolidation is distribution (overbought unwind) or a reset. It also permits a divergence check versus the 2/26 high. |
| 7 | **atr** | Volatility has compressed post-earnings (3.94 → 3.42). ATR is required to set stops and size the position sensibly around the 165.7–176.4 box. |
| 8 | **vwma** | The 2/2 gap was a volume event (117.2M shares). VWMA tells us where the volume-weighted crowd is actually positioned (~171.45) — a better "real" support reference than a simple average. |

Deliberately excluded: stochastics (redundant with RSI), MACD signal line as a *selection* (its crossover information is fully captured by macd + macdh), and Bollinger middle alone (subsumed by the 20-SMA level I use for structural work).

---

## 3. Trend Structure — Three Timeframes

**Long term (200 SMA): unambiguously bullish.** The 200 SMA rose steadily from 127.98 (2024-01-02) to 139.53 (2024-02-28), a ~9.0% climb in two months, and price sits **+24.1% above it**. The 50 SMA (159.97) is far above the 200 SMA, and both are rising — the golden-cross configuration is mature and intact. There is no evidence anywhere in the 146-session window of a long-term trend break.

**Medium term (50 SMA): bullish but stretched.** The 50 SMA advanced from 143.48 (1/2) to 159.97 (2/28), +11.5%, still accelerating. Price at 173.16 is **+8.2% above the 50 SMA**. That is a meaningful extension: it says the trend is strong, but it also means the 50 SMA is not a usable stop for a swing trade — it is 13 points (≈3.8 ATRs) away.

**Short term (10 EMA): neutral / coiling.** The 10 EMA flattened hard after 2/12 (168.03) and has crawled to 172.04 by 2/28 — it went essentially sideways for four sessions (168.66 → 168.63 on 2/14–2/21) while price whipped around it, then resumed rising. Critically:

- 2024-02-20 close 167.08 vs 10 EMA 168.64 → **below**
- 2024-02-21 close 168.59 vs 10 EMA 168.63 → **marginally below**
- 2024-02-22 close 174.58 vs 10 EMA 169.71 → **reclaimed**
- 2024-02-26/27/28 closes 174.73 / 173.54 / 173.16 all **above** (EMA 171.41 / 171.80 / 172.04)

So the 10 EMA has flipped from overhead resistance back to support, but the cushion is razor-thin: **+0.65% ($1.12) above it**, and the last three sessions are consecutive lower closes (174.73 → 173.54 → 173.16, −1.05% cumulative from the 2/23 close of 174.99).

**Structure:** The dominant feature since the 2024-02-02 earnings gap is a **consolidation box of roughly 165.7 to 176.4**. Within that box the sequence is constructive: a double low at **165.75 (2/13) and 165.74 (2/20)**, then a higher low at 172.27 (2/28). The 2/26 high of **176.37 is the highest high in the entire 146-session dataset** (i.e., highest since at least Aug 2023). Price is now compressing into the apex of the box's upper half.

---

## 4. Momentum — Cooling, Not Breaking

**MACD:** The line peaked at **5.50 (2024-02-12)** and has decayed to **4.111**, a −25.3% decline in twelve sessions. The signal line (4.319) is now *above* the MACD line, i.e., a **bearish crossover is in force**. The histogram path is the important nuance:

| Date | macdh |
|---|---|
| 2024-02-09 | +1.287 |
| 2024-02-12 | +1.118 |
| 2024-02-15 | +0.203 |
| 2024-02-16 | **−0.039** (flip) |
| 2024-02-21 | **−0.530** (trough) |
| 2024-02-26 | −0.020 (recovery attempt) |
| 2024-02-28 | **−0.208** (re-widening) |

The 2/26 near-zero reading was a **failed re-cross attempt**; the histogram has widened negatively again for two sessions. Read this as *momentum deceleration inside an uptrend*, not a trend reversal: MACD remains +4.11, i.e., **above zero**, and above zero with a negative histogram is the classic "pullback in an uptrend" configuration. But the immediate signal is unambiguously bearish-lean.

**RSI:** 61.71, down from the **73.78 peak on 2024-02-02** (the earnings-gap day) and a secondary 72.43 on 2/9. The sequence of RSI highs is descending: 73.78 (2/2) → 72.43 (2/9) → 65.19 (2/26) → 61.71 (2/28), while price made a marginally higher high on 2/26 (176.37 intraday high vs. 175.39 on 2/12). That is a **mild bearish momentum divergence** — worth flagging, though it is modest and can be resolved by a simple push to a new high with RSI > 66. RSI is comfortably in neutral (post-2/20 low of 55.91), so there is **no oversold cushion and no overbought constraint** — the indicator is currently giving permissive rather than directive information.

**Net momentum read:** the up-leg's thrust has definitively faded; the market is at a decision point where momentum has to be re-earned. Prior up-thrusts in this window were reclaimed decisively (e.g., RSI 53.10 on 1/31 → 73.78 on 2/2), showing the indicator can reset and re-accelerate quickly after a shallow dip.

---

## 5. Volatility & Bollinger Framework

- **ATR 3.42** (1.98% of price), down from the **3.94 peak on 2024-02-13** and 3.88 on 2/2. Volatility is **mean-reverting and compressing** — six of the last seven sessions show declining ATR (3.93 → 3.80 → 3.68 → 3.55 → 3.42). Compression into the top of a box, with the 10 EMA flattening, is a **coil** — it resolves directionally, usually sharply. Traders should expect an expansion day rather than pre-position for further drift.
- **Bollinger (20, 2σ):** middle 169.93, upper 179.85, lower 160.00. Band width = **11.68% of the mid-line**, which is wide — a legacy of the earnings gap, not of current activity.
- **%B position:** (173.16 − 160.00) / (179.85 − 160.00) = **66.3%**. On 2024-02-23 it was (174.99 − 156.18) / (179.47 − 156.18) = **80.8%**. So price has peeled off the upper region but remains in the **upper third of the band** — consistent with a strong trend digesting, not a reversal.
- **Confluence to note:** the lower band (**160.00**) and the 50 SMA (**159.97**) are effectively the same level. A full gap-fill scenario (the 2024-02-02 gap runs from the 2/1 close of **159.28** to the 2/2 open of **169.19**) would terminate almost exactly on this band/SMA confluence. That makes **159.3–160.0 the single most important structural floor** in the dataset.

---

## 6. Volume — the Most Under-Appreciated Signal

The 2/2 earnings session printed **117.2M shares** — about **2.3×** the 21-session average of roughly **51.8M** (1/30–2/28), with a +9.91-point gap (+6.22%) from the 159.28 close to the 169.19 open, and a close of 171.81 (+7.87%). That gap is **unfilled**, and unfilled volume-backed gaps are the primary reason to treat this as a bullish continuation structure.

Since then, volume has decayed, and the last three sessions are notable:

| Date | Close | Volume |
|---|---|---|
| 2024-02-22 | 174.58 | 55.4M |
| 2024-02-23 | 174.99 | 59.7M |
| 2024-02-26 | 174.73 | 44.4M |
| 2024-02-27 | 173.54 | 31.1M |
| 2024-02-28 | 173.16 | **28.2M** |

At **28.2M**, the latest session is roughly **45% below** that ~51.8M average. **Interpretation — two-sided:**
- *Constructive:* a three-day drift lower on shrinking volume is **not distribution**. Sellers are absent; this reads as supply exhaustion into a holiday-shortened, low-liquidity tape (which also explains the tight 1.78-point range on 2/28).
- *Cautionary:* the 2/26 push to a new high (176.37) also came on sub-average volume (44.4M) — a **volume non-confirmation** of the breakout attempt. A new high on light volume is the market's way of saying "no sponsorship above here yet."

**VWMA (171.45):** price is **+1.0% above** the volume-weighted average, i.e., the volume-weighted crowd is in profit and the reference line is rising but decelerating (170.66 → 171.04 → 171.28 → 171.45 over four sessions vs. +1.0/day earlier in February). VWMA at 171.45 sits just **$0.60 below the 10 EMA (172.04)** — a tight short-term support cluster.

---

## 7. Actionable Level Map

**Resistance**
1. **175.75** — 2/23 high
2. **176.37** — 2/26 high; window (146-session) high-water mark
3. **179.85** — upper Bollinger band; natural upside objective if 176.37 clears

**Support**
1. **172.04 / 171.45** — 10 EMA + VWMA cluster (first-line, only 0.65–1.0% below price)
2. **169.93** — Bollinger mid-line / 20 SMA; losing this shifts the short-term bias negative
3. **168.64 → 167.08** — 2/13 and 2/20 closing lows
4. **165.75 / 165.74** — the double bottom; the box floor and the line that defines "consolidation" vs. "failed breakout"
5. **169.19 → 159.28** — the unfilled 2024-02-02 gap zone; **159.97–160.00 (50 SMA + lower band)** is the terminal confluence

---

## 8. Scenarios & Trade Construction

**Bull continuation (base case, given the primary trend and unfilled gap):**
Trigger = a daily close **above 176.37** on volume **≥ 55M** (i.e., above the ~51.8M average — the level that has been missing). Confirmation would be MACD histogram turning positive again and RSI pushing back above 66. First target 179.85 (upper band); a band-width expansion above that is a trend-acceleration regime, not a mean-reversion one.
Risk/reward from 173.16: ~+1.8% to 176.37 and ~+3.9% to the upper band, against a stop below ~168.

**Range/pause (highest probability near term):** With MACD below signal, RSI fading, three lower closes, and volume drying up, **continued work between 169.9 and 176.4** is the most probable outcome. Range tactics apply: buy the 171.4–172.0 cluster, sell 175.8–176.4, size small because ATR compression means the resolution will be quick.

**Bear breakdown:** A close **below 169.93** (Bollinger mid) invalidates the short-term uptrend and opens 167.08, then the **165.74–165.75 double bottom**. A close below 165.74 breaks the four-week box and targets the gap. Note the gap is *large* (9.91 points) and partially backfills naturally — the first real demand shelf on a gap-fill is the 159.28–160.00 zone, which is 7.6% below spot.

**Risk management with ATR 3.42:**
- Tight swing stop: **1.5 × ATR = $5.13** → ~168.03, which sits just above the 167.08 closing low. This is the highest-quality invalidation level because it is *both* an ATR stop and a structural stop.
- Wide structure stop: **2.0 × ATR = $6.84** → ~166.32, but be aware this is only $0.58 above the 165.74 double bottom — i.e., a 2-ATR stop is *almost* the box-floor stop. If the box floor is the real invalidation, use ~165.2 (below the double bottom) and accept that the risk from 173.16 is **~4.6% / ~2.3 ATR** — size positions accordingly (roughly half the share count of a 1.5-ATR-stop trade at the same dollar risk).
- **Volatility warning:** with ATR compressing for six straight sessions, a fixed-dollar stop is more likely to be hit by an expansion bar. Widen stops to at least 1.5 ATR and reduce size rather than tighten stops.

---

## 9. What Would Change This View

| Development | Interpretation |
|---|---|
| Close > 176.37 on > 55M volume | Breakout confirmed; upgrade to trend-following long |
| MACD histogram turns positive again | Failed bearish cross (as happened repeatedly in January); momentum re-accelerates |
| RSI pushes > 70 with price > 176.37 | Trend re-assertion; ignore lingering "divergence" concerns |
| Close < 169.93 | Short-term trend broken; stand aside / tactical short |
| Close < 165.74 | Box failure; gap-fill toward 160 becomes the operative scenario |
| Close > 160 but ATR expanding sharply | Volatility regime shift; halve position size |

**Honest limitations:** All statements above are derived from the 146-session window (2023-08-01 → 2024-02-28) supplied by the tool. I have no verified data on longer-horizon support/resistance (e.g., 2022 highs), so the "176.37 = highest high" claim is bounded explicitly to this window. Percentage moves cited are computed directly from the close/volume series in the tool output; no historical backtest validation of these signals is claimed or available.

---

## 10. Summary Table

| Dimension | Reading (2024-02-28) | Signal | Key Level / Evidence |
|---|---|---|---|
| **Long-term trend** | Price 173.16 vs 200 SMA 139.53 (+24.1%); 200 SMA rising all window | **Bullish (strong)** | 200 SMA 127.98 (1/2) → 139.53 (2/28) |
| **Medium-term trend** | Price vs 50 SMA 159.97 (+8.2%); 50 SMA +11.5% since 1/2 | **Bullish, stretched** | 50 SMA 143.48 → 159.97 |
| **Short-term trend** | Price +0.65% above 10 EMA 172.04; reclaimed 2/22 after 2/20–2/21 dip below | **Neutral / coiling** | 10 EMA flat 168.6→168.6 (2/14–2/21), then 172.04 |
| **MACD** | 4.111 vs signal 4.319; line −25.3% from 5.50 peak (2/12); above zero | **Bearish cross inside uptrend** | Failed re-cross: hist −0.020 (2/26) → −0.208 (2/28) |
| **RSI** | 61.71; lower highs 73.78 (2/2) → 72.43 (2/9) → 65.19 (2/26) | **Mild negative divergence, neutral zone** | Neither overbought nor oversold |
| **Bollinger** | %B 66.3% (was 80.8% on 2/23); width 11.68% of mid | **Upper-third, cooling** | Mid 169.93 / UB 179.85 / LB 160.00 |
| **Volatility (ATR)** | 3.42 (1.98% of price); 6 of 7 sessions declining from 3.94 (2/13) | **Compression → expansion risk** | 1.5 ATR stop ≈ 168.03; 2 ATR ≈ 166.32 |
| **Volume / VWMA** | 28.2M vs ~51.8M 21-day avg (−45%); VWMA 171.45, price +1.0% above | **Light-volume drift = no distribution, but no sponsorship** | 2/2 earnings volume 117.2M (2.3× avg) |
| **Structure** | 4-week box 165.74–176.37; double bottom 165.75 (2/13) / 165.74 (2/20); higher low 172.27 (2/28) | **Constructive consolidation** | 176.37 = highest high in the 146-session window |
| **Gap** | 2024-02-02 gap: 159.28 close → 169.19 open (+6.22%), unfilled | **Bullish anchor / downside magnet** | 159.97–160.00 = 50 SMA + lower band confluence |
| **Actionable bias** | Hold core long; add only on volume-confirmed close > 176.37 | **Neutral-to-bullish, wait for trigger** | Stop 168.03 (1.5 ATR); invalidation 165.74 |