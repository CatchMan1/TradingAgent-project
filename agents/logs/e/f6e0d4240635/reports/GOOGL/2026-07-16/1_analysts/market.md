# GOOGL — Alphabet Inc. | Technical Analysis Report
**Analysis date: 2026-07-16 (last completed session). All price/indicator levels below are taken from the verified market snapshot and indicator tool output for that date.**

---

## 1. Data integrity notes (read first)

- The verified snapshot's latest row is **2026-07-16: O 373.06 / H 375.27 / L 352.30 / C 354.46, volume 41,158,500**, with a 22.97-point range — roughly **2.0× the current ATR (11.58)**. This was a violent, high-volume reversal session and it materially changes the short-term read.
- **Scale caveat:** the snapshot reports `mfi = 0.431357`, which appears to be normalized to 0–1 (i.e. ≈43 on the standard 0–100 scale). Because the vendor's scaling is ambiguous, I treat it as "roughly neutral-to-weak" rather than citing a precise value. All other indicator values are on their standard scales and are internally consistent with the OHLCV series.
- Two small cash distributions appear in the data (ex-dates **2026-03-09, $0.21** and **2026-06-08, $0.22**). They are immaterial to the technical picture but explain minor gaps between raw closes and the total-return index.

---

## 2. Market context: where this stock sits structurally

| Reference | Value (2026-07-16) | Close vs. reference |
|---|---|---|
| Close | 354.46 | — |
| 10 EMA | 359.44 | −1.4% |
| 50 SMA | 371.42 | **−4.5%** |
| 200 SMA | 321.14 | **+10.4%** |
| Bollinger mid (20 SMA) | 356.75 | −0.6% |
| Bollinger upper | 374.63 | −5.4% |
| Bollinger lower | 338.87 | +4.6% |
| VWMA | 353.95 | +0.1% |
| ATR | 11.58 (≈3.3% of price) | — |
| RSI(14) | 46.21 | neutral |
| MACD / Signal / Hist | −1.19 / −2.04 / **+0.86** | hist positive, both lines < 0 |

**The 2026 tape in one paragraph:** GOOGL began the year at 315.15 (2026-01-02 close), ground higher, gapped down hard on 2026-02-05 (open 312.22 vs. prior close 333.04, on 88.2M shares), recovered, then staged a major breakout on **2026-04-30** (open 374.07 vs. prior close 349.94, close 384.80 on 72.0M shares). It topped out at a **close of 402.62 on 2026-05-13** (intraday high 403.70), then corrected to a **close low of 337.39 on 2026-06-26** — with 114.7M shares traded that day, the highest volume in the dataset. From that low it rebounded to 367.03 (2026-07-07), pulled back to 352.51 (2026-07-13), spiked to 370.92 (2026-07-15) — and then gave it all back on 2026-07-16.

---

## 3. Trend structure: bullish skeleton, damaged intermediate trend, broken short-term setup

**Long-term (200 SMA) — intact bullish.**
The 200 SMA sits at **321.14 and is rising monotonically**, climbing from 309.56 on 2026-06-16 (+11.6 points, ≈+3.7% in a month). Price is 10.4% above it. The 50 SMA (371.42) is ~50 points (~15.6%) above the 200 SMA, so a death cross is not remotely a near-term risk; the golden-cross structure established earlier in 2026 remains valid. **Strategic bias stays constructive.**

**Medium-term (50 SMA) — deteriorating.**
This is the most important nuance in the report. The 50 SMA stopped rising and has now **turned down for the first time in the visible window**: 372.80 (2026-07-13) → 372.29 (07-14) → 372.00 (07-15) → **371.42 (07-16)**. A flattening-then-rolling 50 SMA, with price 4.5% below it since mid-June, defines a **corrective range** rather than a trend continuation. The 50 SMA has also acted as a ceiling: the 2026-07-15 rally closed at 370.92, just shy of it, and the 2026-07-16 session failed right on top of it (high 375.27) before collapsing.

**Short-term (10 EMA) — bearish flip.**
The 10 EMA is 359.44 and price has just closed below it (−1.4%). The 10 EMA itself has gone flat-to-down (360.55 on 07-15 vs. 359.44 on 07-16) after a modest July up-slope. The sequence of short-term structure — 07-15's high-volume push to 370.92, then an immediate gap-up open at 373.06 that reversed to a 354.46 close — is textbook **failed breakout / bullish-trap** behavior.

**Candlestick read (structural, not predictive flourish):** 2026-07-16 is a **bearish engulfing candle** — it opened above the prior close (373.06 > 370.92) and closed below the prior session's open (354.46 < 357.97), fully engulfing 2026-07-15's bullish body, and closed in the bottom ~10% of its own range. That is a distribution signature, not noise, given the volume (below).

**VWMA check:** price (354.46) is effectively *at* the VWMA (353.95, +0.1%). The volume-weighted average cost of recent participants is therefore roughly break-even — meaning there is a large, price-sensitive holder base clustered right here. VWMA has also stopped declining (350.02 on 07-10 → 353.95 on 07-16), a mild hint that buyers were accumulating on the July dip, but the 07-16 reversal puts that at risk.

---

## 4. Momentum: quietly improving beneath the surface, but stalling

- **MACD line = −1.19, signal = −2.04, histogram = +0.86.** The MACD line crossed **above** its signal line around **2026-07-02** (histogram flipped positive that day: −0.10 → +0.50), and the MACD line itself has recovered from −7.35 (2026-06-26) to −1.19. That is a genuine momentum *repair*. **But** both lines remain below zero (bearish regime), and the histogram has been **compressing**: +1.83 (07-07) → +1.74 → +1.81 → +2.20 (07-13, net of the crossover mechanics) → **+0.86 (07-16)**. The MACD line also rolled over from −0.78 (07-15) to −1.19 (07-16). Translation: **the recovery is decelerating, not accelerating.**
- **RSI = 46.21.** Fully neutral, with a jagged path: 33.27 (2026-06-26, near-oversold) → 53.65 (07-06) → 43.77 (07-13) → 56.87 (07-15) → 46.21 (07-16). Importantly, RSI has printed **higher lows** (33.3 in late June vs. 43.8 in mid-July), which is a mild positive divergence against the price structure — but there is **no clean bullish price/RSI divergence** I can substantiate from the tool output, and RSI is nowhere near oversold. Neutral momentum with no edge either way.

**Net momentum verdict:** a stabilizing-but-not-accelerating setup. This favors range tactics with tight invalidation, not a conviction trend entry.

---

## 5. Volatility & envelope: bands are compressing, ATR is re-expanding

- **Bollinger band width = 374.63 − 338.87 = 35.76 points ≈ 10.0% of the 356.75 midpoint.** Upper band has been fading (376.98 on 07-15 → 374.63 on 07-16) as the 20-day envelope tightens — a coiling pattern that typically precedes a directional resolution.
- **ATR = 11.58, up from 10.31 on 2026-07-14** — an 12% one-session expansion, entirely attributable to the 22.97-point range on 07-16. Volatility expanding *on a downside reversal day* is a warning, not a comfort.
- The 2026-07-16 high of **375.27** tagged just above the upper band (**374.63**) and was rejected. In the current regime, unless a close occurs above that band, the envelope's upper edge remains a sell zone, not a breakout trigger.
- Price is sitting in the **middle-lower half of the envelope** (0.6% below the mid-band), which is consistent with a range-bound, two-sided market.

---

## 6. Volume: the strongest bearish evidence in the dataset

- **2026-07-16: 41.2M shares vs. a July average of roughly 25M** (July sessions before it ran 15.9M–28.3M) — call it **1.6–1.7×** normal. Downside reversal + elevated volume = supply.
- The July rebound itself came on **declining volume** (28.3M on 07-15 rising, but 15.9M/18.3M on 07-13/14), i.e. a **weak-hands bounce**. Volume-based confirmation therefore **does not** support the bullish case yet.
- Volume history shows this name suffers outsized event-driven repricing: **88.2M shares on 2026-02-05** (gap down), **72.0M on 2026-04-30** (gap up +10%), and **114.7M on 2026-06-26** (a −2.4% day, no gap — the profile of an index/rebalance or block-driven session). Practical implication: **stops placed inside the normal 25–30M-volume daily noise will get run**, so ATR-based buffers matter more than usual here.

---

## 7. Actionable levels and scenarios

**Support ladder (from actual bars, not projections):**
1. **351.0 – 352.5** — the immediate floor: lows of 351.08 (07-09), 351.75 (07-13), 351.09 (07-14), 352.30 (07-16). A four-touch cluster; the pivotal line in the sand.
2. **346.1 – 346.4** — 06-24 close 345.29 / 06-23 close 346.13 / 06-11 low 346.36.
3. **338.5 – 341.0** — Bollinger lower (338.87) + June lows (340.20, 341.72).
4. **330.2 – 337.4** — the 2026-06-26 capitulation low (intraday 330.20, close 337.39). A break here would negate the entire post-June rebound and put the 200 SMA (321.14) in play.

**Resistance ladder:**
1. **359.4 – 361.0** — 10 EMA (359.44) / 07-14 close (359.51); first hurdle for any bounce.
2. **366.5 – 371.4** — 07-06 close 366.46, 07-07 close 367.03, plus the **50 SMA at 371.42** (the key medium-term gate).
3. **373.2 – 375.3** — 07-07 high 373.16, 07-15 high 373.65, **07-16 high 375.27**, Bollinger upper 374.63. A dense, freshly-defended supply shelf.
4. **378.5 – 380.3** — late-May breakdown zone (05-29 close 380.34, low 378.46).
5. **382.5 – 388.9** — May congestion (05-22 close 382.97 → 05-26 close 388.88).

**Scenario A — Failed breakout resolves lower (base case, ~55% weight).**
The 07-16 engulfing candle implies sellers are active into 373–375. **Trigger:** a daily close below 351.0. **Path:** 346.4 → 341.7 → 338.9 (lower band) → 337.4. **Invalidation:** a reclaim of 361 on rising volume.

**Scenario B — Range repair / re-attack (alternate, ~35% weight).**
Support at 351–352 holds, MACD histogram re-expands, and price grinds back to the 50 SMA. **Trigger:** two consecutive closes above **361** with volume > ~30M, ideally with RSI > 55. **Targets:** 366.5 → 371.4 (50 SMA) → 374.6 (upper band). **Confirmation of a genuine trend resumption** requires a **close above 375.3**, which would break the three-session supply shelf; that opens 380.3 and then 387–389.

**Scenario C — Trend failure (~10% weight).** A close below **337.4** (June close low) forces a reassessment of the long-term structure and activates the 200 SMA at 321.14 as the next major magnet. The rising 200 SMA makes this a low-probability path *near term*, but the 07-16 candle is exactly the kind of tape that precedes it.

**Risk management / sizing:**
- ATR = 11.58 (≈3.3% of price). Use **1.5× ATR ≈ 17 points** for swing stops — e.g., a long entered near 356 would stop below **339** on a wide swing basis, or **~345** on a tighter 1× ATR basis aligned with support #2. A short from near 362 would stop above **379**.
- With a 1% equity risk budget and a 17-point stop, a position of ~0.06% of equity per point ≈ position notional of roughly **20% of equity**. Cutting size is the correct response to expanding ATR plus a fresh distribution candle.
- **Do not** chase the 07-16 close at 354.46: price is pinned to the VWMA (353.95), i.e. in the middle of a two-sided battleground with no edge.

---

## 8. Indicator selection rationale (8 chosen, complementary, non-redundant)

| Indicator | Why it earns a slot in *this* context |
|---|---|
| **close_200_sma** | Confirms the intact primary uptrend and rising long-term floor (321.14); the strategic anchor. |
| **close_50_sma** | Detects the medium-term roll-over (just turned down) and the 371.42 ceiling — the pivot for regime change. |
| **close_10_ema** | Captures the immediate momentum flip and the 359.4 short-term hurdle; fast enough to matter post-reversal. |
| **macd** | Measures the mid-July momentum repair from −7.35 to −1.19 and its stall. |
| **macds** | Enables the signal-crossover timing (bull cross ~2026-07-02) and histogram compression read — not a duplicate of the MACD line. |
| **rsi** | Independent momentum scale (46.2, neutral) to cross-check MACD and to flag the higher-low pattern; explicitly avoids redundancy with any stochastic-style oscillator. |
| **atr** | Directly usable for stop placement and position sizing; essential given the 2×-ATR reversal bar and event-driven volume spikes. |
| **vwma** | Volume-weighted confirmation: price ≈ VWMA (354.46 vs. 353.95) shows the rebound lacked volume conviction and defines the battle line. |

*(Bollinger upper/lower bands from the verified snapshot are used as contextual envelope levels — 374.63 / 338.87 / mid 356.75 — but are not counted in the eight-indicator set to avoid duplicating the 50/20-SMA volatility/mid-line information.)*

---

## 9. Summary table

| Dimension | Evidence (2026-07-16) | Read | Implication |
|---|---|---|---|
| Primary trend | Close 354.46 vs. rising 200 SMA 321.14 (+10.4%); 50 > 200 by ~50 pts | **Bullish** | Strategic bias long; no death-cross risk |
| Intermediate trend | 50 SMA 371.42, turned down (from 372.80 on 07-13); price −4.5% below | **Corrective range** | Don't treat bounces as new uptrends |
| Short-term trend | Close below 10 EMA 359.44; failed breakout at 375.27 | **Bearish flip** | Bull trap on 07-16; favor range tactics |
| Momentum | MACD −1.19 / signal −2.04 / hist +0.86; RSI 46.2 | **Neutral, repairing, decelerating** | No edge; wait for confirmation |
| Volatility | ATR 11.58 (up from 10.31 on 07-14); bands 338.87–374.63 | **Expanding, coiled** | Reduce size, widen stops |
| Volume | 41.2M on a −4.4% reversal day (~1.6–1.7× July avg) | **Distribution** | Bounce quality suspect until volume confirms upside |
| Key support | 351.0–352.5 (4-touch cluster); 346.4; 338.9; 337.4; 330.2 | — | Close < 351 = bearish trigger |
| Key resistance | 359.4–361.0; 371.4 (50 SMA); 373.2–375.3; 380.3; 387–389 | — | Close > 375.3 = genuine bullish reversal |
| Base-case plan | Short/neutral bias below 361; sell rallies into 371–375 | **Range-trade** | Stop 1.5×ATR (~17 pts); ~20% notional at 1% risk |
| Alternative plan | Long only on close > 361 with volume > 30M, or on a successful retest of 351–352 | **Tactical long** | Targets 366.5 → 371.4 → 374.6 → 380.3 |
| Biggest risk | Event-driven gaps (88.2M on 02-05, 72.0M on 04-30, 114.7M on 06-26) | **Gap risk** | Avoid oversized positions into high-volume/news-prone sessions |

**Bottom line for GOOGL:** the long-term uptrend is intact (price 10.4% above a rising 200 SMA), but the intermediate trend has rolled over (50 SMA just turned down) and the short-term setup just failed decisively at 373–375 on the highest volume in six weeks. The most defensible posture is **neutral-to-bearish inside a 351–375 range**, with a bearish tilt below 351 targeting 346 → 341 → 339, and a legitimate bullish reset only on a volume-confirmed close above 361 first and 375.3 second. Position sizing should be cut to reflect ATR that is now expanding at 3.3% of price.