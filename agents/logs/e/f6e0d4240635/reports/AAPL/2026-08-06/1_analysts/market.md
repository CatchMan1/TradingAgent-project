# AAPL — Multi-Timeframe Technical Review (as of 2026-08-06, close)

## 1. Verified Data Anchor

All exact price/indicator claims below come from the verified snapshot for AAPL on **2026-08-06** (which matches the OHLCV pull — no discrepancy between the two sources):

| Field | Value |
|---|---|
| Open / High / Low / Close | 314.34 / 316.29 / 309.23 / **312.41** |
| Volume | 46,139,900 |
| close_10_ema | 317.5807 |
| close_50_sma | 309.7358 |
| close_200_sma | 279.1573 |
| MACD / Signal / Histogram | 1.3777 / 4.8540 / **−3.4762** |
| RSI(14) | 46.8770 |
| Bollinger mid / upper / lower | 323.5310 / 345.9483 / 301.1137 |
| ATR | 9.3334 |
| VWMA | 320.9467 |
| MFI (reference only) | 0.4517 |

---

## 2. Indicator Selection and Why

I deliberately chose **8 complementary indicators** spanning trend horizon, momentum, volatility, and participation — avoiding duplicated information (e.g., RSI *or* StochRSI, not both; MACD line *and* signal used only because the signal is what defines the crossover state, with the histogram treated as the derived read rather than a separate pick).

| # | Indicator | Role in this specific context |
|---|---|---|
| 1 | **close_200_sma** | Strategic anchor. AAPL is in a 5-month uptrend off the March/April 2026 base; the 200-day confirms whether the July 31shock is a pullback or a regime change. |
| 2 | **close_50_sma** | The exact line price is currently testing (309.74). This is the single most decision-relevant level on the chart right now. |
| 3 | **close_10_ema** | Captures the short-term damage from the July 31 gap. Fast signal of whether the bounce has any traction. |
| 4 | **macd** | Trend/momentum regime: still positive (1.38) → bull trend intact but decelerating. Distinguishes "pullback" from "reversal." |
| 5 | **macds** | Defines the crossover state. MACD (1.38) is below signal (4.85) → bearish crossover in force since 2026-07-31. |
| 6 | **rsi** | Positions the pullback on the 30/70 scale (46.9) — resets overbought without reaching oversold, which is characteristic of trend continuation, not exhaustion. |
| 7 | **atr** | Volatility has structurally expanded (8.06 → 9.33 in five sessions). Mandatory for stop placement and sizing after a −8.6% gap. |
| 8 | **vwma** | Integrates volume with price. VWMA (320.95) sitting *above* spot is direct evidence the heavy-volume cohort is underwater — the cleanest read on whether the bounce is supply-absorbing or supply-distributing. |

*(Bollinger bands were pulled as reference for band-width/%B geometry and the 301.11 lower band, and are used in the volatility section rather than counted as separate trend picks.)*

---

## 3. The Regime: An Intact Intermediate Uptrend Inside a Violent Short-Term Downtrend

This is not a clean chart, and the honest read is that AAPL is in a **three-timeframe conflict**:

**Long-term (6–12 months): clearly bullish.**
- close_200_sma = **279.16** and rising monotonically every session in the sample (269.73 on 2026-06-29 → 279.16 on 2026-08-06, ≈ +0.31/day).
- Spot at 312.41 sits **+11.9% above** the 200-day. The 50-day (309.74) is **11.0% above** the 200-day — a wide, mature golden-cross spread with no death-cross risk anywhere in sight.
- The sequence of higher swing lows since the Q1 base is intact: 245.51 (2026-03-30 low) → 245.70 (2026-04-07 low) → 273.75 (2026-06-25 low). Even after the July 31 collapse, the 300.00 low remains far above the June low.

**Intermediate (1–3 months): bullish but decelerating and now wounded.**
- The July advance was powerful: close 281.74 (2026-06-29) → 340.08 (2026-07-28), with the intraday high at **344.57 on 2026-07-29**.
- But the 50-day has rolled essentially flat: 309.4994 (07-31) → 309.5228 (08-03) → 309.6106 (08-04) → 309.6542 (08-05) → 309.7358 (08-06). A 50-day SMA that adds only ~0.08/day after adding ~0.77/day in mid-July is a trend that has lost its slope. **Flattening ≠ breaking**, but it removes the "rising support" cushion.

**Short-term (days–weeks): bearish, with an unconvincing bounce.**
- The 10-EMA has collapsed from **331.31 (2026-07-30) to 317.58 (2026-08-06)** — a −13.73 (−4.1%) roll in five sessions. That is the signature of a gap event, not a drift.
- The moving averages are now stacked in a **near-term bearish order above price**: 10-EMA 317.58 > spot 312.41; VWMA 320.95 > spot; 20-day (Boll mid) 323.53 > spot.
- Only the 50-day (309.74) and 200-day (279.16) remain below price. Price is wedged between a falling fast average overhead and a flattening medium average beneath — a **compression zone roughly 310–318** that will resolve.

### The event that defines the current tape: 2026-07-31
- 2026-07-30 close: **333.43**. 2026-07-31 open: **304.81** → a gap of **−28.62 (−8.58%)**.
- 2026-07-31 range: 300.00–310.69, close **308.91** (−7.35% on the day).
- Volume **132,489,100** versus roughly **50.8M** average across the preceding 21 sessions — approximately **2.6× normal**. This was institutional-size repricing, not retail noise.
- Critically, the 07-31 **high of 310.69 never traded back into the 310.69–333.43 void**, so that gap is **completely unfilled**. Unfilled gaps of this size act as overhead supply; every rally into 318–330 must absorb sellers who bought the top of the July run.

For context, this is the second high-volume distribution event of the summer: 2026-06-25 (−4.6% to 275.15 on 107.0M) and 2026-06-26 (261.8M shares, the largest volume in the dataset). Both times the market recovered, which argues for buying dips — but both times it took weeks and a lower low first.

---

## 4. Momentum: Deteriorating, But at Mid-Range, Not Capitulation

- **MACD has collapsed but not broken zero.** The MACD line peaked at **9.6087 on 2026-07-29** and is now **1.3777** — a −8.23 (86%) decay in six sessions. It remains *positive*, which on a classical reading means the primary uptrend is damaged, not reversed.
- **The histogram rolled over before price did.** MACD − signal: +1.310 (07-28) → +1.172 (07-29) → +0.643 (07-30) → **−1.365 (07-31)** → −2.978 (08-03) → −3.521 (08-04) → −3.634 (08-05) → **−3.476 (08-06)**. The histogram is *still negative but is no longer making lower lows* — the first (weak) sign of downside momentum stalling.
- **RSI is mid-range and rising off a shallow trough.** 71.65 on 2026-07-17 (overbought) → 66.78 on 2026-07-29 → **40.34 on 2026-08-03** → 46.88 now. This is a textbook "reset within an uptrend": RSI cooled from overbought to near-oversold and has turned up **without price breaking the 50-day on a closing basis**.
- **Bearish divergence preceded the break.** Price printed a *higher* close on 2026-07-29 (338.19 vs 333.74 on 2026-07-17) while RSI printed a *lower* high (66.78 vs 71.65). Momentum was already thinning three sessions before the gap. This is now confirmed, not a hypothesis — but it has largely played out.

**Nuance worth stating plainly:** an RSI of 46.9 is the market's most ambiguous reading. It is neither a buy signal (no oversold edge) nor a sell signal (no overbought edge). It says *the easy money in both directions has been made for now.*

---

## 5. Volatility: Structurally Higher — Respect It

- **ATR has stepped up from 8.06 (2026-07-30) to 9.33 (2026-08-06)**, +15.8% in five sessions. At 2.99% of spot, this is an elevated-volatility regime.
- The 2026-07-31 true range (prior close 333.43 → low 300.00) was **33.43 points ≈ 4.1× the prevailing ATR**. One-session tail risk has been demonstrated, not theorized.
- **Bollinger geometry is extremely wide and skewed.** Mid = 323.53, Upper = 345.95, Lower = 301.11 → bandwidth ≈ **44.84 points = 13.9% of the mid band**. That is a post-shock expansion, meaning: (a) the bands are *not* currently useful as mean-reversion triggers, and (b) any "touch the lower band" bounce logic is unreliable when the lower band is itself falling.
- Position of price within the bands: **%B ≈ 0.25** — the lower quartile. Price is closer to the lower band (spot 312.41 vs 301.11 = **11.30 above**) than to the mid band (11.12 below) by a near coin-flip. Practically, spot is pinned at the lower edge of the cloud.
- Note the lower band's own arc: 271.83 (2026-07-17) → 304.16 (2026-07-30) → 301.11 now. The lower band *peaked and turned down* — meaning the 20-day volatility expansion is beginning to reverse, which typically favors range repair over continued trending.

---

## 6. Volume and Participation: The Bounce Is Under-Supported

This is where the read gets genuinely cautious.

- **VWMA (320.95) > spot (312.41).** The volume-weighted average transacted price over the window is **8.54 points (2.7%) above** the current price. Translation: the aggregate dollar-weighted holder base is underwater. That is a supply-overhang condition, not a support condition.
- VWMA has also rolled over decisively: 329.58 (2026-07-30) → 326.39 → 325.09 → 323.70 → 322.28 → **320.95**. Six consecutive declines.
- **VWMA (320.95) is 11.2 points *above* the 50-SMA (309.74).** A VWMA running well above the simple average means the heavy-volume sessions clustered at *higher* prices — i.e., the July 15–30 advance and the July 31 gap were transacted at premium levels. Distribution at highs.
- **The rebound's volume profile is deteriorating, not confirming:** 75,052,000 (08-03) → 68,001,000 (08-04) → 49,438,800 (08-05) → **46,139,900 (08-06)**. Price rose from 303.42 to 312.41 while volume fell ~38%. **Rising price on falling volume after a distribution day is the classic signature of a technical reflex bounce, not a resumption of the uptrend.**
- Contrast with the two prior capitulations, which both drew **expanding** volume on the lows (107.0M on 06-25, 261.8M on 06-26) and thereby marked tradeable bottoms. The 08-03 low of 302.56 has **not** yet produced a comparable volume capitulation. That is the single largest missing ingredient for a durable low.

---

## 7. Level Map (every level derived from tool output)

**Resistance (overhead stack — this is a thick ceiling):**
| Level | Source |
|---|---|
| 316.29 | 2026-08-06 high (immediate) |
| **317.58** | close_10_ema — first real test |
| 319.35 | 2026-07-23 low (broken swing support, now supply) |
| **320.95** | VWMA — the underwater-cost line |
| **323.53** | Bollinger mid (20-day) + 323.68 (2026-07-20 low) — confluence |
| 329.59 | 2026-07-30 low (last close before the gap) |
| **333.43–333.74** | Gap origin / 2026-07-17 close — the full gap-fill objective |
| 344.57 | 2026-07-29 intraday high (all-time-window high in this dataset) |

**Support:**
| Level | Source |
|---|---|
| **309.74** | close_50_sma — the line in the sand |
| 309.23 | 2026-08-06 low (already tested intraday) |
| 302.56 | 2026-08-03 low |
| **301.11** | Bollinger lower band |
| **300.00** | 2026-07-31 low — round number + post-gap floor |
| ~294–295 | June consolidation shelf (e.g., 2026-06-23 close 294.30, 2026-07-01 close 294.38) |
| 283.78 / 273.75 | 2026-06-26 close / 2026-06-25 low — the deeper retest zone |

The critical observation: **support at 300–302 and resistance at 317–324 are only ~5% apart, with price dead-center at 312.41.** This is a coil, and the ATR (9.33) says it can be traversed in a single session.

---

## 8. Scenarios With Explicit Triggers

**Bull case — "gap-fill repair" (my base case, ~45% weight)**
Trigger: a **close above 317.58 (10-EMA)**, ideally with volume back above ~65M, confirming the rebound has real sponsorship.
Path: 320.95 (VWMA) → 323.53 (Boll mid) → 329.59 → 333.4 gap origin.
Logic: 50-SMA held, RSI reset from 72 to 47 and turned up, MACD still positive, histogram stopped making lower lows, 200-day rising. Historically in this dataset, both June shocks (06-25, 06-26) resolved into a stronger July rally (275.15 → 344.57, +25.9%). The pattern of "high-volume shakeout then reclaim" is the established behavior in this name.
**What invalidates it:** a close back below 309.2 on expanding volume.

**Bear case — "unfilled gap = lower high" (≈35% weight)**
Trigger: rejection at 317.6–321.0 (a lower high versus 333.43) followed by a **daily close below 309.74 with volume > 60M**.
Path: 302.56 → 301.11 → **300.00**. A decisive break of 300 opens 294–295 and then the 283.78 / 273.75 June lows.
Logic: the gap is unfilled, VWMA is overhead, the bounce is on shrinking volume, and the 50-SMA has gone flat — flat averages break.
**Note:** the 300–302 zone carries triple confluence (07-31 low, Bollinger lower band 301.11, 08-03 low 302.56). Expect a *fight* there, not a clean slice.

**Neutral/chop case (≈20% weight)**
No trigger needed; happens if neither 309.2 nor 317.6 closes out. Range 309–318, ATR compresses, Bollinger bands narrow back toward ~10%. In this case every indicator on this list is near-useless and the correct action is to reduce activity, not add to it.

---

## 9. Actionable Risk Management

- **Volatility-scaled stops.** With ATR = 9.33, a 1×ATR stop below the 50-SMA gives 309.74 − 9.33 = **300.41**, which lands *almost exactly* on the 2026-07-31 low of 300.00. That confluence makes **300 a high-quality, non-arbitrary invalidation level** — if 300 breaks, the post-shock floor thesis is wrong.
- **Sizing math:** long entry near 312.4 with a 300.0 stop = **12.4 points (3.97%) of risk per share**. Size positions off that number, not off a fixed dollar amount. If your per-trade risk budget is 1% of equity, position notional ≈ 25% of equity per 1% risk unit — i.e., ATR alone has roughly doubled the dollar risk of the same share count versus mid-July.
- **Don't average into 310–313 before confirmation.** The 10-EMA is still falling ~2.2 points/day. Buying into a falling short-term average with VWMA overhead and declining volume is buying without an edge. Wait for either (a) a volume-confirmed reclaim of 317.6, or (b) a flush toward 300–302 that *reverses* on high volume.
- **Asymmetry check:** upside to the gap fill is 333.4 − 312.4 = **21.0 points (+6.7%)**; downside to the 300 floor is **12.4 points (−4.0%)**. That's a ~1.7:1 reward/risk to the *first* real resistance cluster — adequate but not compelling, and it improves materially only if you can enter nearer 305–307.
- **Event risk is the dominant unknown.** The magnitude and volume of the 2026-07-31 gap (−8.6%, 2.6× volume) is larger than any single session in the prior six months and is characteristic of a fundamental/news catalyst rather than a pure technical breakdown. Technical indicators cannot price an information shock; treat any technical long as conditional on no further negative headlines.

---

## 10. What Would Change My View (Monitoring Checklist)

| Watch item | Bullish resolution | Bearish resolution |
|---|---|---|
| Close vs 10-EMA (317.58) | Close above, ideally 2 consecutive | Repeated rejection at/below |
| Volume on up days | Returns to >65M | Stays <50M (bounce fails) |
| Close vs 50-SMA (309.74) | Holds/extends (now +0.86% above) | Closes below on >60M |
| MACD histogram | Turns positive (needs MACD > 4.85) | Makes new low below −3.63 |
| RSI | Reclaims 50–55 | Loses 40 (08-03 low was 40.34) |
| VWMA | Flattens / price reclaims 320.95 | Continues falling, price stays below |
| 2026-07-31 gap | Partially filled (>329.6) | Remains fully unfilled for weeks |

---

## 11. Honest Caveats

- The published ATR/RSI/MACD values depend on the vendor's window conventions; all values cited are the verified-snapshot values for the 2026-08-06 session and I have not recomputed them independently.
- There is **no claim here of support/resistance "bounces"** — the 309.23 intraday low on 2026-08-06 is a single session, not an established floor.
- The dataset ends 2026-08-06; the 344.57 high (2026-07-29) is the high within the sampled window, **not** necessarily a 52-week or all-time high.
- Percentages quoted (e.g., −8.58% gap, +11.9% above 200-SMA, +25.9% June-low-to-July-high) are computed directly from the tool's OHLC rows with the dates stated, and should be read as arithmetic, not as statistically validated signals.

---

## 12. Summary Table

| Dimension | Reading (2026-08-06) | Evidence | Interpretation | Action |
|---|---|---|---|---|
| **Long-term trend** | Bullish | 200-SMA 279.16, rising ~+0.31/day; spot +11.9% above it | Primary uptrend intact | Do not short the primary trend |
| **Intermediate trend** | Bullish, decelerating | 50-SMA 309.74; increment only +0.08/day over last 2 sessions | Support exists but has stopped rising | Watch 309.74 as the pivot |
| **Short-term trend** | Bearish | 10-EMA fell 331.31 → 317.58 in 5 sessions; price below it | Downtrend within uptrend | No new longs until 317.58 reclaimed |
| **MA structure** | Conflict / coil | Stack above price: 10-EMA 317.58, VWMA 320.95, BB-mid 323.53; below price: 50-SMA 309.74, 200-SMA 279.16 | Compression 310–318 | Trade the break, not the middle |
| **Momentum (MACD)** | Deteriorating, still positive | MACD 1.3777 vs signal 4.8540; hist −3.4762; MACD down from 9.61 on 07-29 | Bearish cross since 07-31, no zero-line break | Neutral-bearish |
| **Momentum (RSI)** | Reset, mid-range | 71.65 (07-17) → 40.34 (08-03) → 46.88 | Overbought cleared without capitulation | No edge either way |
| **Divergence** | Bearish, already realized | Higher close 338.19 (07-29) vs 333.74 (07-17) but lower RSI 66.78 vs 71.65 | Warned before the 07-31 gap | Mostly priced in |
| **Volatility** | Elevated, expanding | ATR 9.33 (2.99%), up from 8.06; 07-31 true range 33.43 | Tail risk demonstrated | Halve normal size; 1×ATR stops |
| **Bollinger** | Wide, lower-quartile | Mid 323.53, UB 345.95, LB 301.11; bandwidth 13.9%; %B ≈ 0.25 | Post-shock; bands not mean-reverting signals | LB 301.11 = support reference only |
| **Volume / VWMA** | Bearish (distribution) | VWMA 320.95 > spot 312.41; 07-31 volume 132.5M ≈ 2.6×; bounce volume 75M → 46M | Bounce lacks sponsorship | Demand volume confirmation |
| **Key event** | Unfilled gap | 07-30 close 333.43 → 07-31 open 304.81 (−8.58%); 07-31 high 310.69 | Overhead supply 310.7–333.4 | Gap fill = 333.4 target |
| **Immediate support** | 309.74 / 309.23 / 302.56 / 301.11 / 300.00 | 50-SMA, 08-06 low, 08-03 low, BB-lower, 07-31 low | Triple confluence at 300–302 | Invalidation below 300 |
| **Immediate resistance** | 316.29 / 317.58 / 320.95 / 323.53 | 08-06 high, 10-EMA, VWMA, BB-mid | Thick ceiling | First close >317.58 = bullish trigger |
| **Reward/Risk** | ~1.7 : 1 | +21.0 pts to 333.4 gap fill vs −12.4 pts to 300 stop | Adequate, not compelling at 312.4 | Prefer entries 305–307 or on confirmed reclaim |
| **Base case** | Gap-fill repair (~45%) | 50-SMA held; RSI reset; MACD >0; hist stabilizing; June analogue | Cautious constructive | Scale in only on confirmation |
| **Bear case** | Lower high then <309.74 (~35%) | VWMA overhead; shrinking bounce volume; flat 50-SMA | Break of 300 opens 294 → 283.8/273.75 | Hard stop 300 |
| **Chop case** | 309–318 range (~20%) | ATR expansion vs band-width turning down | Wait | Reduce activity |