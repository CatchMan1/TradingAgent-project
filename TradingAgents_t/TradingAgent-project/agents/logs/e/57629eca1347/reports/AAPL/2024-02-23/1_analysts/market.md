# AAPL — Multi-Timeframe Technical Report (as of the 2024-02-23 close)

## 1. Data anchor & verification note

Everything below is anchored to the **verified snapshot for 2024-02-23**, which I treated as the source of truth.

| Item | Verified value |
|---|---|
| 2024-02-23 OHLCV | O 185.01 / H 185.04 / L 182.23 / C **182.52** / Vol **45,119,700** |
| Prior session (02-22) | O 183.48 / H 184.96 / L 182.46 / C 184.37 / Vol 52,292,200 |

**Consistency check:** the `get_stock_data` CSV and the verified snapshot agree row-for-row, and every indicator value returned by `get_indicators` (50SMA 188.9672, 200SMA 183.7327, 10EMA 184.1287, MACD −1.73296, Signal −1.29499, Hist −0.43796, RSI 40.1015, ATR 3.01636, VWMA 185.3829, Boll UB 192.6379 / LB 179.9761) matches the snapshot **exactly**. No discrepancies to flag.

---

## 2. Indicator selection (8 core indicators) and why they fit this context

The current context is a **medium-term uptrend that has lost short-term control and is testing its long-term trend line**, inside a ~2% ATR regime — i.e. a "trend-decision" tape, not a clear trend-following or a clear mean-reversion tape. That argues for a set split across horizon, momentum, volatility and volume:

1. **close_200_sma** — the level just lost; the single most important strategic line at 183.73.
2. **close_50_sma** — defines the still-intact intermediate uptrend and its rolling-over slope (188.97).
3. **close_10_ema** — the fastest level that tells us whether sellers are still in immediate control (184.13).
4. **macd** — confirms the momentum regime is below zero (−1.733).
5. **macds** — needed to date and grade the bearish crossover; without it the MACD read is incomplete.
6. **rsi** — independent (non-EMA-based) momentum read to check whether the pullback is exhausted (40.10).
7. **atr** — position sizing/stop placement in a contracting-volatility tape (3.016).
8. **vwma** — volume-weighted "true" average cost; distinguishes distribution from a low-volume drift (185.38).

Supplementary overlay (values pulled from the verified snapshot, not part of the core eight): **Bollinger middle 186.307, upper 192.638, lower 179.976**. I excluded `mfi`, `boll`-middle as a separate signal, and duplicate momentum oscillators to avoid redundancy.

---

## 3. Trend structure — three horizons disagree

**Long term (200 SMA = 183.73):** The 200-day is still *rising* — it climbed every session in the returned window, from 178.87 (2023‑12‑26) to 183.73 (2024‑02‑23). But price is now **below it**: 182.52 vs 183.73 = **−0.66%**. That is a fresh, single-session loss of the line (02‑22 closed 184.37, above the then-183.69 200SMA; 02‑23 closed below the 183.73 200SMA). One close is a *warning*, not a confirmed regime change — the 200SMA is also rising into price, which tends to compress the buffer.

**Medium term (50 SMA = 188.97):** Price is **−3.42%** below the 50-day. The 50-day peaked at **190.93 on 2024‑01‑30** and has fallen on 17 consecutive sessions to 188.97 — a slow but unambiguous roll-over. Importantly, **50SMA (188.97) remains above 200SMA (183.73)**, so the golden-cross structure is intact; however the spread has compressed from **8.73 (01‑30)** to **5.23 (02‑23)**, roughly a 40% narrowing in four weeks. That is the classic signature of an intermediate trend losing its bid rather than breaking.

**Short term (10 EMA = 184.13):** Price is **−0.87%** below the 10-EMA, and the 10-EMA has fallen from 191.41 (01‑29) to 184.13 without a single up-session in between. The short-term trend is cleanly down.

**Layered resistance stack above spot:** 10EMA 184.13 → VWMA 185.38 → Bollinger mid 186.31 → 50SMA 188.97 → Feb swing high 191.05 (02‑07). Each is a distinct, verifiable hurdle; price is currently *below all four* of the shorter ones. That is a weak structural position.

---

## 4. Momentum — bearish, but decelerating

**MACD:** Line −1.733 vs Signal −1.295, Histogram **−0.438**. The bearish crossover occurred when the histogram flipped negative on **2024‑01‑31 (−0.143)**, after printing **+0.362 on 01‑30** — i.e. the momentum top was 01‑30. The histogram then narrowed to −0.065 on **02‑09**, re-widened to **−0.733 on 02‑20**, and has since narrowed again to **−0.438**. So we have a **two-session deceleration of bearish momentum** (02‑22 −0.484 → 02‑23 −0.438), while the MACD *line* also ticked up off its 02‑21 low (−1.753 → −1.733) even as price made a marginally lower close.

This is a **constructive-but-unconfirmed** nuance: momentum is no longer accelerating lower, but the MACD line remains firmly below zero and below its signal. It argues against chasing shorts into the 180s and argues *for* waiting for either a reclaim of 184.13–185.38 or a fresh histogram expansion below −0.73 to confirm continuation.

**RSI = 40.10.** Mid-range bearish, no oversold cushion. The path matters: RSI bottomed at **35.23 on 02‑20** (price low 180.00 that day), rebounded to **44.05 on 02‑22**, then fell back to 40.10 on 02‑23. For reference, the January low was **RSI 28.79 on 01‑05** (close 181.18, low 180.17). The tape is therefore **less oversold now than at the January low, despite similar price** — that is a mild negative: the same price is being reached with *less* selling pressure being worked off. There is room for another leg toward the 30s without any extreme being reached.

**Net momentum read:** bearish bias, decelerating, not capitulatory. No confirmed bullish divergence is present in the data I pulled — I am not going to claim one.

---

## 5. Volatility, range and the cost basis of the tape

**ATR = 3.016 (≈1.65% of spot).** ATR has contracted from **3.586 on 02‑02** (post-earnings, volume 102.6M) to 3.016 — a ~16% decline in daily range. Combined with the Bollinger envelope compressing from **14.85 wide (02‑09)** to **12.66 wide (02‑23)** — a band width contraction from **7.85% to 6.80%** of the 186.31 mid-band — this is a **volatility contraction inside a downtrend**, which typically resolves directionally rather than persisting.

**VWMA = 185.38**, i.e. price is **−1.54%** below the volume-weighted average price. VWMA peaked at **189.72 on 02‑07** and has declined every session since to 185.38. The read: the marginal volume-weighted holder of the last ~20 sessions is **underwater**, which supplies overhead supply on any bounce into the 185s.

**Volume quality:** 02‑23's 45.12M is roughly **83% of the 20-session mean of ~54.2M** (computed from the returned rows). The down-move is happening on **declining** volume — the sessions with heavy participation in February were 02‑02 (102.6M), 02‑05 (69.7M) and 02‑15 (65.4M), none of which were decisive breakdowns. So the break below the 200-day has, so far, **not been confirmed by volume expansion**. This is a meaningful argument for treating 183.73 as contested rather than lost.

**Notable single-session pattern:** 02‑23 opened at 185.01 (essentially the session high of 185.04) and closed at 182.52, **below the 02‑22 open of 183.48** — a **bearish engulfing of the prior day's real body**, closing only **10.3%** up from the session low ((182.52−182.23)/(185.04−182.23)). That is a weak close and the cleanest bearish micro-signal in the recent tape.

**February range:** high **191.05 (02‑07)**, low **180.00 (02‑20)**. Midpoint 185.53 — remarkably close to the VWMA (185.38). Price at 182.52 sits in the **lower third** of the month's range. Drawdown from the 01‑23 close of 195.18 is **−6.49%**; from the 2023‑12‑14 close of 198.11 it is **−7.87%** (intraday 12‑14 high 199.62 → −8.57%).

---

## 6. Key levels (all from tool output)

**Support**
- **182.23** — 02‑23 low (immediate).
- **180.00–180.30** — the most-tested shelf in the dataset: 02‑20 low **180.00**, 01‑05 low **180.17**, 01‑17 low **180.30**. Bollinger lower band at **179.98** sits right on top of it → **confluence at ~180**.
- **178.7–178.9** — late-January lower-band region (178.67–178.83 across 01‑24 to 01‑31); a break of 180 opens this zone.

**Resistance**
- **184.13** — 10EMA (first gate to neutralize the short-term downtrend).
- **185.38** — VWMA (the average-cost ceiling).
- **186.31** — Bollinger middle / 20-SMA basis.
- **188.97** — 50SMA.
- **191.05** — 02‑07 high; then **196.38** — 01‑24 high.

---

## 7. Actionable plan

**Bias: neutral-to-bearish tactically, with the medium-term uptrend on probation.** The 50>200 structure plus contracting volatility on declining volume argue against an outright trend-short; the price structure (below 10EMA/VWMA/Boll-mid/200SMA, bearish engulfing, MACD below zero) argues against buying the dip blindly.

**Bearish continuation (primary, needs confirmation):**
- Trigger: a **close below 182.23** (02‑23 low) with MACD histogram **re-expanding below −0.733** (the 02‑20 reading) and/or volume above the ~54M mean.
- First target **180.00–180.30** (triple-tested shelf + lower band), then 178.7–178.9.
- Invalidation: a close back above **184.13** (10EMA).
- Stop reference: 1.5× ATR ≈ **4.5 points** → ~186.7 if entering near 182.2; i.e. risking back above the VWMA/Boll-mid cluster.

**Bullish mean-reversion (secondary, contingent):**
- Trigger: a close above **185.38** (VWMA) and, more importantly, above **186.31** (Boll-mid) — that would also stop the 10EMA from continuing to decline.
- Targets **188.97** (50SMA), then 191.05.
- Invalidation: rejection at 184.1–186.3 leaving a lower high and a fresh low under 182.23.

**Sizing note:** with ATR at 3.016 (1.65%), a 1-ATR daily move is ~3 points. Any stop inside 2.5 points (≈0.8 ATR) is inside the noise band and will likely be wicked — the 02‑23 session alone ranged 2.81 points.

**What would materially change the view:** (a) a *volume-confirmed* close below 183.73/182.23 — turns "on probation" into "downtrend"; (b) a reclaim of 186.31 that turns the Bollinger mid-band back into support — restores the Jan uptrend; (c) 50SMA crossing back down through... it is still 5.23 above the 200SMA, so **watch the 50/200 spread**: continued compression at the current pace would put them close together within weeks, and a death cross would be a strategic, not tactical, signal.

---

## 8. Summary table

| Dimension | Indicator (verified 2024-02-23) | Reading | Interpretation | Actionable level |
|---|---|---|---|---|
| Price | Close 182.52 (O 185.01 / H 185.04 / L 182.23) | Bearish engulfing of 02-22 body; close 10.3% up from low | Sellers in control into the close | Trigger < 182.23 |
| Long trend | close_200_sma **183.73** (rising) | Price −0.66% below; lost on 02-23 | Regime warning, unconfirmed | Reclaim > 183.73 |
| Medium trend | close_50_sma **188.97** (falling 17 sessions from 190.93 on 01-30) | Price −3.42% below; 50 > 200 still | Uptrend intact but eroding | 188.97 resistance |
| Short trend | close_10_ema **184.13** | Price −0.87% below; unbroken decline since 01-29 | Short-term downtrend | Reclaim > 184.13 |
| Momentum | macd **−1.733** / macds **−1.295** / macdh **−0.438** | Bearish cross since 01-31; histogram narrowing 2 sessions | Bearish, decelerating | Expansion < −0.733 |
| Momentum (independent) | rsi **40.10** | Off 35.23 (02-20) and 44.05 (02-22); Jan low was 28.79 | Room to fall, not oversold | 30 zone = exhaustion watch |
| Volatility | atr **3.016** (1.65%) | Down from 3.586 (02-02); Boll width 6.80% vs 7.85% (02-09) | Coiling — directional resolution likely | 1.5×ATR ≈ 4.5 pt stop |
| Volume/cost basis | vwma **185.38** (peaked 189.72 on 02-07) | Price −1.54% below; 02-23 vol 45.1M ≈ 83% of ~54.2M mean | Overhead supply; break lacks volume confirmation | Resistance 185.38 |
| Range | Feb high **191.05** (02-07) / low **180.00** (02-20) | Price in lower third; midpoint 185.53 | Range-bound with bearish tilt | 180.00–180.30 shelf |
| Auxiliary | boll **186.307** / ub **192.638** / lb **179.976** | Bands compressing; price below mid | Neutral-to-weak within envelope | Lower band ≈ support shelf |

**Bottom line for AAPL:** the tape is in a *decision zone*, not a trend. Price is sandwiched between a **triple-tested 180 support shelf** (reinforced by the lower Bollinger band at 179.98) and a **dense resistance stack at 184.13 / 185.38 / 186.31**. The higher-probability path is a retest of ~180 unless AAPL reclaims 184.13–186.31 on expanding volume; a downside break of 180 opens 178.7–178.9. Because volatility is contracting (ATR 3.02, band width 7.85%→6.80%) and the 200-day breach has not been volume-confirmed, I would size positions small, use stops outside ~1 ATR, and require a **volume-confirmed** close before treating either break as real.