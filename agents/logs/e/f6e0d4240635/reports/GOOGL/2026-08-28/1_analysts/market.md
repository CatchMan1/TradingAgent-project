# GOOGL — Multi-Timeframe Technical Report
**As of close 2026-08-28 | Last verified print: $346.59**

---

## 1. Data Integrity Check (done first)

I cross-checked `get_stock_data` against `get_verified_market_snapshot` before writing anything. The 2026-08-28 row agrees exactly in both sources (O 340.71 / H 349.14 / L 340.27 / **C 346.59** / V 25,347,200), and every indicator value quoted below is taken from the verified snapshot or from the per-indicator series keyed to that same date. **No conflict between tools.**

One flag worth raising: the snapshot's `mfi` field prints **0.492722**. Conventional MFI is on a 0–100 scale, so this looks like a 0–1 normalized print (~49.3) that is numerically almost identical to RSI (49.259). Because I cannot confirm the scaling, **I excluded MFI from the signal set** rather than interpret it. Also note three cash dividends in the visible window (0.21 on 2025-12-08, 0.21 on 2026-03-09, 0.22 on 2026-06-08) — the `technical_total_return_index` tracks above price by roughly the accumulated dividend, so price-based levels and TRI-based levels are not interchangeable. No splits (all `split` = 1.0).

---

## 2. Regime Classification

GOOGL is in a **volatility-compression coil nested inside a mature medium-term corrective downtrend, sitting on top of an intact long-term uptrend.** That three-layer description matters, because each timeframe gives a different answer:

| Timeframe | Reference | Reading | Verdict |
|---|---|---|---|
| Short (2–3 wks) | close_10_ema **345.02** | Close 346.59 is **+0.45%** above | Neutral / mildly constructive |
| Medium (2–3 mo) | close_50_sma **349.78** | Close is **−0.91%** below; 50SMA falling | Corrective downtrend |
| Long (9–12 mo) | close_200_sma **334.57** | Close is **+3.59%** above; 200SMA rising | Uptrend intact |

This is not a trending market right now. It is a market that has stopped going down and has not yet started going up, and is doing so on shrinking range.

---

## 3. The Path That Led Here — Three Discrete Events

**Event 1 — The 2026-07-23 gap-down.** GOOGL closed 2026-07-22 at 342.09 and opened 2026-07-23 at **321.13**, closing at **317.69** (−7.1%) on **69.42M shares** versus 39.33M the prior session. That left an unfilled-at-the-time gap between 321.13 and 342.09. The gap was subsequently **fully repaired** — the 2026-07-31 close of 356.13 sits above the entire gap zone. RSI troughed at **31.02** on 2026-07-23, never reaching the 30 oversold threshold.

**Event 2 — The V-recovery into 2026-08-04/05.** From the 317.69 low, price rallied in six sessions to a 377.65 close on 2026-08-04. Then 2026-08-05 printed **open 383.34 / high 384.48 / low 356.77 / close 362.43** on 46.93M shares — a wide-range bearish reversal. The 384.48 high was the **highest intraday print since 2026-05-29 (385.24)** and it failed immediately. That is a textbook failed-breakout signature, verifiable directly in the data.

**Event 3 — The current 13-session coil (2026-08-12 → 2026-08-28).** Since the reversal, the entire range has been **338.52 (low, 2026-08-27) to 351.60 (high, 2026-08-24)** — a **3.8% band**, while ATR is **8.48 (2.45% of price)**. The net drift over those 13 sessions is −3.1%. In other words, *the average daily range is nearly as wide as the entire two-week range, with no net progress.* That is the definition of chop/mean-reversion, and it is hostile to breakout entries placed inside the band.

Note also the **failed second high**: 2026-08-04 high 380.52 → 2026-08-05 high 384.48 → rejection. Price has since retraced **−8.2% from the 377.65 close (2026-08-04)** and **−11.0% from the 384.48 intraday peak**, and sits **−13.9% below the 402.62 all-time-window closing high of 2026-05-13** (and −15.2% below the 2026-05-18 intraday high of 408.61).

---

## 4. Volatility: The Core Story

This is where the actionable information is.

- **ATR: 8.48**, down from **13.93 on 2026-08-05** — a **−39% contraction** in eleven sessions, and the **lowest ATR reading in the entire 32-session window** I pulled (7/14–8/28; prior low 8.45 on 08-27).
- **Bollinger width: 371.31 − 329.23 = 42.08, or 12.01% of the 350.27 middle band.** On 2026-08-05 the same measure was **67.91 / 19.46%** — a **−38% compression**.
- The bands are converging from *both* sides: `boll_lb` has risen from **314.37 (2026-08-19)** to **329.23 (2026-08-28)**, while `boll_ub` has fallen from **377.61 (2026-08-19)** to **371.31**.

**Important nuance — do not overstate the squeeze.** Width at 12.0% is compressed versus the August spike, but it is *not* a window extreme. Mid-July readings were tighter: **10.67% on 2026-07-14** (376.69/338.54 around 357.61) and **10.02% on 2026-07-16**. The July compression resolved as a violent **downside** expansion. So the correct statement is: *conditions favor an imminent volatility expansion, but this specific configuration has already resolved downward once in the last six weeks.* The squeeze is direction-agnostic and should be traded as such.

---

## 5. Momentum

**MACD is the single most informative near-term signal.**

| Date | macd | macds | macdh |
|---|---|---|---|
| 2026-07-27 | −8.833 | −5.196 | −3.637 |
| 2026-07-31 | −6.143 | −6.625 | **+0.482** (bull cross) |
| 2026-08-05 | +0.585 | −3.730 | +4.315 (peak) |
| 2026-08-14 | −1.137 | −0.970 | −0.166 (bear cross) |
| 2026-08-20 | −2.330 | −1.552 | −0.778 (hist trough) |
| 2026-08-28 | **−2.021** | **−1.940** | **−0.081** |

The MACD line is below its signal line, so the crossover structure is technically bearish — **but the histogram has repaired from −0.778 to −0.081**, and the MACD line ticked **up** on 2026-08-28 (−2.311 → −2.021). The MACD line and signal line are now separated by only **0.081 points**. A single ordinary up-day (ATR = 8.48) would trigger a bullish crossover. Conversely, this is the third failed attempt at a flip since 08-14, which warns that the crossover is *weak*, not *powerful*.

**RSI: 49.26** — dead neutral. It has oscillated in a tight **44.0–50.7** band for twelve straight sessions (2026-08-13: 47.27 → 2026-08-28: 49.26), with brief excursions to 44.03 (08-20) and 49.53 (08-24). No oversold condition, no overbought condition, and **no valid divergence signal** — I checked, and price's lower low on 08-26/08-27 (342.00/340.65) against RSI 45.19/44.24 does not constitute a divergence versus the 08-20 reading of 44.03 on a 340.67 close. Calling that a divergence would be inventing a signal.

The August high in RSI was **62.56 on 2026-08-04** — notably, momentum peaked *before* price made its 08-05 high. That is a real, date-stamped negative momentum characteristic of the August top.

---

## 6. Volume and Volume-Weighted Structure

- **VWMA: 344.72**, versus close 346.59 → price is **+0.54% above** the volume-weighted average. Mildly positive, but marginal.
- VWMA peaked at **356.34 on 2026-08-19** and has fallen in **seven of the last seven sessions** to 344.72, even as price went roughly sideways. Mechanically, that means the volume-weighted center of recent trade is being dragged *down* — heavy participation occurred at higher prices and is now marked at a loss.
- **Participation is fading, not building.** 5-day average volume (08-24 → 08-28) = **23.23M** vs 20-day average = **24.40M**, a ratio of **0.95**. The last five sessions printed 26.34M, 20.65M, 20.42M, 23.39M, 25.35M.
- The volume tell from the two big reversals is unambiguous: **69.42M on the 2026-07-23 breakdown** and **46.93M on the 2026-08-05 failed breakout**. Both large events were distribution. By contrast, the 2026-07-31 up-thrust (+6.7% on 46.50M) and 2026-08-03 (38.67M) carried solid volume but achieved highs that were subsequently rejected. *Rallies have been absorbed.*

**Tactical read:** a breakout from this coil on volume below ~30M (i.e., under 1.25× the 20-day average) should be treated as suspect. Low-volume coil breaks fail disproportionately.

---

## 7. The Most Underrated Insight: The Averages Are Coming Down to Price

This is the piece most readers will miss. The "bearish" setup (price below the 50SMA and below the Bollinger middle) is **partly a mechanical artifact of what is rolling out of the lookback windows** — and it is about to self-correct.

**50-day SMA roll-off.** The 50-session window ending 2026-08-28 runs approximately **2026-06-18 → 2026-08-28** (49 sessions in my count plus the holiday-adjusted 06-19 gap; treat as ±1 session). The values next to drop out are:

- 2026-06-18: **368.03** (high — replaces with ~346 → drags SMA down ~0.44)
- 2026-06-22: 349.68, 06-23: 346.13, 06-24: 345.29, 06-25: 343.71, 06-26: **337.39**, 06-29: **353.65**, 06-30: **357.37**

Net arithmetic: the 50SMA keeps drifting lower for roughly 12–15 more sessions at a **decelerating** pace (current slope ≈ −0.35 to −0.55/day), moving from 349.78 toward **roughly 347–348**. Translation: **the 50SMA comes down to price; price does not need to climb to it.** That materially weakens the bear case that rests on "price is under the 50SMA."

**20-day Bollinger middle roll-off — even more decisive.** The 20-session window is exactly **2026-08-03 → 2026-08-28**. The values queued to drop out are all *above* spot:

- 2026-08-03: 373.51 → mid drops ~1.35
- 2026-08-04: 377.65 → mid drops ~1.55
- 2026-08-05: 362.43 → mid drops ~0.79
- 2026-08-06: 357.75 → mid drops ~0.56
- 2026-08-07: 354.30 → mid drops ~0.39

If price merely holds near 346.59, the **Bollinger middle falls from 350.27 to roughly 345.5–346 within 4–6 sessions**, and price flips *above* it without a single point of upside. The upper band will also fall sharply (371.31 → ~366–368), and the lower band will keep rising (329.23). **The squeeze tightens toward an apex in roughly one to two weeks.**

**200-day SMA:** rising steadily, +0.29/day, from 319.98 (2026-07-14) to **334.57**. The golden-cross structure (50 > 200) remains intact, but the spread has collapsed from **52.31 on 2026-07-14 to 15.21 today** — a **71% compression**. On current mechanical drift the spread closes toward ~10–12 within two to three weeks absent a rally. *This is the strategic risk: not a crash, but a slow structural erosion of the medium-term trend.*

---

## 8. Key Levels — All Verified From Tool Output

| Level | Price | Source / Date |
|---|---|---|
| Resistance 4 | **384.48** | 2026-08-05 high (failed breakout) |
| Resistance 3 | **380.52** | 2026-08-04 high |
| Resistance 2 | **371.31** | boll_ub, 2026-08-28 |
| Resistance 1c | **358.58 / 356.13** | 2026-07-31 high / close |
| **Resistance 1 (the decision zone)** | **349.14 – 351.60** | 2026-08-28 high 349.14 · 50SMA **349.78** · boll mid **350.27** · 2026-08-24 high **351.60** |
| **Spot** | **346.59** | 2026-08-28 close |
| Support 0 | **345.02 / 344.72** | close_10_ema / vwma |
| Support 1 | **340.18 – 340.67** | 2026-08-26 low 340.18 · 2026-08-28 low 340.27 · 2026-08-20 close 340.67 |
| **Support 2 (coil floor)** | **338.52** | 2026-08-27 low |
| Support 3 | **335.84** | 2026-06-25 low |
| **Support 4 (line in the sand)** | **334.57** | close_200_sma |
| Support 5 | **330.20 / 329.23** | 2026-06-26 low / boll_lb |
| Support 6 | **321.13 – 317.69** | 2026-07-23 gap open → close |

**Factual note on the 200SMA:** it has not been a clean floor. On **2026-07-23 (close 317.69 vs 200SMA 323.56)** and **2026-07-24 (close 319.74 vs 323.90)** GOOGL closed *below* it, then reclaimed it on 2026-07-27 (close 326.56 vs 324.31). So a two-day penetration followed by recovery already happened once this quarter. That makes the 200SMA a genuinely important level, but **not an impenetrable one** — and it argues for a stop *below* it rather than an entry *at* it.

---

## 9. Actionable Playbook

### Scenario A — Range/Neutral (highest probability, ~50%)
ATR 8.48 inside a 13.08-point range = mean reversion dominates. Trade the edges, not the middle.
- **Fade the 349.00–351.60 confluence** (50SMA + boll mid + double highs). Entry ~350.50, stop **352.60** (risk 2.10), target **341.00** (reward 9.50) → **~4.5:1**.
- **Buy the 338.80–340.60 band.** Entry ~339.50, stop **337.90** (risk 1.60), target **346.50** (reward 7.00) → **~4.4:1**.
- Add a filter: skip both fades if the session opens with volume already > 1.5× the 20-day average, because that signals the coil is resolving.

### Scenario B — Squeeze Breakout Long (~30%)
The mechanical roll-off in §7 makes this more likely than the raw 50SMA position suggests.
- **Trigger (all three required):** (1) daily **close > 351.60** (2026-08-24 high), (2) close above both 50SMA (~349.5) **and** boll mid (~348.9) on the same session, (3) volume **> 30M** and MACD histogram **positive**.
- **Stop:** below **338.52** (coil low). Risk ≈ 13.1 pts ≈ **1.5× ATR**. For a tighter, higher-R multiple use **342.50** (below VWMA and the 08-24 close) → risk 9.1 pts ≈ 1.07× ATR.
- **Targets:** T1 **358.58** (+2.0%), T2 **371.31** (boll_ub, +5.7%), T3 **380.52** (2026-08-04 high).
- **R:R:** with the 342.50 stop → T2 = **2.2:1**, T3 = **3.2:1**. With the 338.52 stop → T2 = 1.5:1, T3 = 2.2:1. Take the T1 partial at 358.58 and trail on the 10EMA.

### Scenario C — Breakdown Short (~20%)
- **Trigger:** daily **close < 338.52** on expanding volume (> 30M), MACD histogram re-expanding negative (below −0.40), RSI < 40.
- **Stop:** above **346.50** (≈ 1× ATR above the trigger). For a wider, more robust stop use **351.60**.
- **Targets:** **335.84** (2026-06-25 low), **334.57** (200SMA), **330.20 / 329.23** (June low + boll_lb), then **321.13** (2026-07-23 gap open).
- **Warning:** this is a counter-long-term-trend trade into a *rising* 200SMA. Halve normal position size, and treat 335–334 as a place to bank most of the trade rather than a place to add.

### Risk management (applies to all three)
- **ATR = 8.48 = 2.45% of price.** A 2×ATR stop is 16.96 pts (4.9% of capital per share at full notional). To hold 1R at ≤1% of equity, cap full-notional exposure near **~20% of equity**, less for the counter-trend short.
- ATR is at a 32-session low. **Do not size positions using pre-August volatility** — the same dollar risk now buys a much larger share count, and the expansion-out of the coil will move faster than current daily ranges imply.
- **Levels to abandon the coil thesis:** a close above 351.60 or below 338.52 invalidates range logic immediately.

---

## 10. Why These 8 Indicators

| # | Indicator | Why it earns a slot | Non-redundancy |
|---|---|---|---|
| 1 | **close_10_ema** (345.02) | Fastest read on whether the last two weeks of chop is turning up; price +0.45% above it | Only short-horizon tool in the set |
| 2 | **close_50_sma** (349.78) | The exact level price must reclaim; also the swing factor in the 50/200 cross | The specific resistance that matters |
| 3 | **close_200_sma** (334.57) | The strategic line — defines whether this is a correction or a trend break | Structural, not tactical |
| 4 | **macd** (−2.021) | Detects the pending momentum flip; 0.081 from a cross | Trend/momentum velocity |
| 5 | **macds** (−1.940) | Required to time the crossover; the only objective trigger for Scenario B | Signal line has no substitute |
| 6 | **rsi** (49.26) | Confirms neutrality without duplicating MACD, and screens for overbought/oversold extremes | Oscillator, not a MACD derivative |
| 7 | **boll_ub** (371.31) | Lower edge of the squeeze; it is *falling*, which quantifies compression | Band geometry ≠ moving average |
| 8 | **boll_lb** (329.23) | Upper edge of the squeeze; it is *rising* — together with boll_ub it gives the width metric | Completes the width measurement |

**Deliberately excluded:** no second oscillator (stochrsi would duplicate RSI); no ADX/DMI (not in the permitted set and would duplicate trend info); no **boll** middle in the primary set (it is within 0.49 of the 50SMA — near-redundant — so I quoted it from the verified snapshot only); **atr** and **vwma** are used as risk/participation overlays from the verified snapshot rather than as directional signals. **MFI excluded** for the scaling ambiguity flagged in §1.

---

## 11. Honest Limitations

1. **This is a 206-session dataset (2025-11-03 → 2026-08-28).** The 200SMA cannot be validated against a full cycle — I have no 200SMA history before 2026-07-14, so I cannot claim "first close below the 200SMA since X."
2. **No historical hit-rate is claimed anywhere in this report.** "Volatility mean-reverts" and "squeezes precede expansions" are stated as general properties, not as GOOGL-specific backtests.
3. **The roll-off arithmetic in §7 is my own calculation** on tool-provided closes. It assumes a static price and a ±1-session boundary on the lookback window. It is a directional argument, not a precise forecast.
4. **I did not attribute causes** to the 2026-04-30 gap-up (349.94 → 374.07 open, close 384.80, 72.04M volume) or the 2026-07-23 gap-down. The price and volume facts are verified; the why is not.
5. **The 2026-06-26 volume print of 114.71M** is a 3–5× outlier suggesting a mechanical/index event. It distorts any simple volume average that includes it.

---

## 12. Summary Table

| Dimension | Verified Reading (2026-08-28) | Interpretation | Actionable Implication |
|---|---|---|---|
| **Close / range** | 346.59 · H 349.14 · L 340.27 · O 340.71 | Closed in upper 71% of the day's range; +1.74% vs prior close | Constructive but one day in a chop regime |
| **Trend — short** | close_10_ema 345.02 | Close +0.45% above | Flipped back positive 2026-08-28 after 2 negative sessions |
| **Trend — medium** | close_50_sma 349.78 (falling) | Close −0.91% below | The level to reclaim; 50SMA is descending toward price (→~347–348) |
| **Trend — long** | close_200_sma 334.57 (rising +0.29/day) | Close +3.59% above | Uptrend intact; closed below it only 07-23/07-24, reclaimed 07-27 |
| **Golden cross** | 50SMA − 200SMA = 15.21 | Down from 52.31 on 2026-07-14 (−71%) | Structural erosion risk over 2–3 weeks |
| **Momentum** | macd −2.021 / macds −1.940 / macdh −0.081 | Bearish cross, but hist repaired from −0.778 | 0.081 from a bull cross — one up-day triggers it; weak, 3rd attempt |
| **Oscillator** | RSI 49.26 | Neutral; 44.0–50.7 for 12 sessions | No edge; no valid divergence |
| **Volatility** | ATR 8.48 (2.45% of price) | 32-session low; −39% from 13.93 (08-05) | Expansion likely; size for 2×ATR ≈ 17 pts |
| **Band compression** | boll 350.27 / ub 371.31 / lb 329.23 · width **12.01%** | Compressed −38% vs 19.46% on 08-05, but NOT vs 10.67% on 07-14 | Coil apex in ~1–2 weeks; July's equivalent resolved DOWN |
| **Volume-weighted** | vwma 344.72 | Close +0.54% above; VWMA fell 7 straight sessions from 356.34 (08-19) | Mild positive price, deteriorating participation |
| **Participation** | 5-day avg 23.23M vs 20-day 24.40M (0.95×) | Fading, not building | Require >30M to trust any breakout |
| **Coil bounds** | 338.52 (08-27 low) – 351.60 (08-24 high) = 3.8% | 13 sessions, net −3.1%, range ≈ 1.5× ATR | Range trades at the edges; avoid the middle |
| **Primary long trigger** | Close > 351.60 + vol > 30M + macdh > 0 | Confluence with 50SMA 349.78 & boll 350.27 | Stop 338.52 (1.5 ATR) or 342.50 (1.07 ATR); targets 358.58 / 371.31 / 380.52 |
| **Primary short trigger** | Close < 338.52 on > 30M vol, RSI < 40 | Opens 335.84 → 334.57 (200SMA) → 330.20 | Counter-trend into rising 200SMA — half size, bank at 335 |
| **Bias** | **Neutral, coiled, event-pending** | Neither the 50SMA nor the boll mid is the obstacle it appears to be | Wait for the close, not the intraday poke |

**Bottom line for GOOGL:** the two-week coil between **338.52 and 351.60** is the only thing that matters right now, and the mechanical roll-off of both the 50-day average and the 20-day Bollinger basis into the first week of September means the squeeze resolves soon — likely before 2026-09-11. The August 5 failed breakout at **384.48** and the fading volume tilt the odds slightly toward a downside resolution, but the rising 200SMA at **334.57** and an already-repaired MACD histogram argue against pressing that view. Trade the confirmed close at either boundary; do not pre-position inside a 3.8% range with ATR at 8.48.