# AMZN — Detailed Technical Analysis & Trading Plan
**Analysis date: 2026-07-22 (latest visible session) · Source of truth: verified market snapshot**

---

## 1. Verified snapshot (single source of truth)

| Metric | Value (2026-07-22) |
|---|---|
| Open / High / Low / Close | 248.27 / 248.45 / 242.45 / **244.85** |
| Volume | 34.11M |
| close_10_ema | 247.09 |
| close_50_sma | 250.60 |
| close_200_sma | 234.46 |
| macd / macds / macdh | 0.559 / −0.158 / **+0.717** |
| rsi | 48.40 |
| boll / boll_ub / boll_lb | 243.61 / 256.71 / 230.51 |
| atr | 7.09 |
| vwma | 247.03 |

**Cross-tool consistency check:** the values returned by `get_indicators` for close_10_ema (247.09183), close_50_sma (250.604), close_200_sma (234.4614), macd (0.558946), macds (−0.158203), macdh (0.717149), rsi (48.402928), boll (243.6115), boll_ub (256.709835), boll_lb (230.513165), atr (7.092471) and vwma (247.031989) **match the verified snapshot to the decimal**. The OHLCV row for 2026-07-22 in `get_stock_data` also matches the snapshot exactly. **No discrepancy to flag.**

---

## 2. Market regime and higher-timeframe context

AMZN is in a **mature uptrend that has already suffered one significant correction and is now in a volatile, unresolved consolidation**:

- **Q1 2026 breakdown:** a violent two-session repricing on 2026-02-05 (close 222.69, volume 103.5M) and 2026-02-06 (close 210.32, volume **179.2M**, open 202.70 — a large gap down from the prior close). The absolute low of the year so far is the **196.00 intraday low on 2026-02-17**.
- **Powerful recovery:** from the 2026-02-12 close of 199.60 to the **2026-05-05 intraday high of 278.56** — a +39.6% run in under three months. Trend structure above the 200-SMA was clean throughout.
- **Correction phase:** 278.56 (2026-05-05) → **225.55 intraday low on 2026-06-25** (−19.0% peak-to-trough, close-to-close 274.99 on 5/6 → 227.01 on 6/25 = −17.5%). This took price below the 50-SMA decisively.
- **Rebound:** 227.01 (6/25 close) → **258.08 intraday high on 2026-07-16** (+13.7%), then a five-session fade to 244.85. The current level retraces roughly **41% of the July rebound** (arithmetic from tool prices: (258.08 − 244.85) / (258.08 − 225.55) ≈ 40.7%).

**Verdict:** long-term structure (200-SMA) is intact and rising, medium-term structure (50-SMA) is still bearish-tilted, and short-term structure has just turned neutral-to-soft. This is a **"bull trend, mid-cycle pullback inside a base"** regime — where trend-following signals are unreliable on their own and **confirmation filters matter more than usual**.

---

## 3. Why these 8 indicators (complementary, non-redundant)

| Indicator | Role in this specific context |
|---|---|
| **close_50_sma** | The battle line. Price has been oscillating around it since mid-June; it is the single most informative medium-term reference right now (250.60, declining). |
| **close_200_sma** | Confirms the strategic uptrend is unbroken (234.46, rising). Defines where the "buy the dip" thesis would be invalidated. |
| **close_10_ema** | Fast, responsive read on whether the July rebound has genuinely rolled over (247.09, price below it). |
| **macd** (+ signal/histogram) | Detects the momentum inflection: the MACD line only just crossed **above zero on 2026-07-15** — a young, fragile bullish signal. Histogram slope is the early-warning system. |
| **rsi** | Neutral 48.4 gives no overbought/oversold edge; its *path* (60.1 → 48.4 in five sessions) exposes fading thrust better than price alone. |
| **atr** | Required for stop placement and position sizing in a 2.9%-of-price daily range environment; ATR is compressing, which changes appropriate stop width. |
| **vwma** | The only volume-weighted truth-serum available. Price below a *rising* VWMA (247.03) is an ambiguous-but-important signal I explain in §7. |
| **boll_ub / boll_lb** (with boll middle) | Band width has collapsed from ~50.7 points (6/22) to ~26.2 points today — a volatility-contraction regime that typically precedes a directional resolution. |

Deliberately **excluded:** stochrsi (redundant with RSI), macds as a standalone (captured inside the MACD family), and any 200-SMA-plus-longer overlays (redundant).

---

## 4. Trend structure: three timeframes, three different answers

**Short-term (10 EMA) — bearish tilt.** Close 244.85 is **2.24 points (−0.9%) below** the 10-EMA at 247.09. The 10-EMA itself flattened hard: it ran 243.83 → 247.60 between 7/13 and 7/20 and has now ticked *down* to 247.09 — its first decline since the rebound began. Price has closed below it two consecutive sessions (7/21, 7/22).

**Medium-term (50 SMA) — bearish, but stabilising.** The 50-SMA peaked at **257.10 on 2026-06-18** and has declined every session since, reaching 250.60 today (a 37-session slide). Critically, the *rate* of decline is decelerating: 254.03 → 253.72 → 253.37 → 253.10 → 252.66 → 252.13 → 251.63 → 251.16 → 250.60 (7/10→7/22). That's ~0.55/session early in July vs ~0.48/session in the last week. The rolling-off window still contains early-June closes in the 260s–270s, so the 50-SMA will keep drifting lower for a few more weeks even if price sits still — meaning **the 250.6 barrier is a moving target that gets easier to reclaim over time**.

**Long-term (200 SMA) — bullish and intact.** 200-SMA at 234.46 and rising steadily (232.35 on 6/9 → 234.46 today, +0.9% over six weeks). Price sits **+10.39 points (+4.4%) above it**. The **50 > 200 configuration (golden-cross state) persists**, but the spread has compressed from **24.3 points on 6/18 (257.10 vs 232.80) to 16.1 points today** — a 34% narrowing. No death cross is imminent given the 50-SMA's flattening, but the trend *quality* is measurably weaker than in April/May.

**Interpretation:** price is trapped in the "no-man's-land" between a bullish 200-SMA (234.46) and a bearish/declining 50-SMA (250.60). The 16-point band between them is the current decision zone.

---

## 5. Momentum: bullish signal, deteriorating quality

The MACD family tells the cleanest story of the last five weeks:

- **MACD line bottomed at −6.88 on 2026-06-26**, then rose monotonically to +0.824 on 7/20 and has now slipped to **+0.559** (two sessions of decline).
- **The line crossed above its signal around 2026-07-01** (histogram flipped positive: −0.101 on 6/30 → +0.470 on 7/1) and **crossed above zero on 2026-07-15** (0.260). Both are legitimate bullish events, now roughly three weeks and one week old respectively.
- **The histogram has now rolled over for five straight sessions:** 2.124 (7/15) → 1.946 → 1.576 → 1.446 → 1.139 → **0.717 (7/22)**. That is a **66% contraction in momentum thrust in five sessions** while price fell only 4.0%. This is textbook *momentum divergence at the signal-line level*: the bullish crossover remains valid, but its engine is losing power.
- The gap between MACD (0.559) and signal (−0.158) is only 0.72 points — a fairly thin cushion. A further ~1.1% decline in price, sustained, would plausibly trigger a bearish re-cross.

**RSI: 48.4 — dead neutral, but the trajectory is informative.** RSI peaked at **60.14 on 2026-07-15** (the strongest reading since the correction), then 54.19 → 51.32 → 54.04 → 51.31 → **48.40**. It never reached overbought, which tells us the July rally was a **mean-reversion bounce, not a new impulsive leg**. For context, RSI bottomed at **33.63 on 2026-06-25** (the price low) — it also never hit 30. A market that neither overshoots nor overboughts is a market in balance, waiting for a catalyst.

---

## 6. Volatility: contraction regime, and what it implies for risk

- **ATR has fallen from 8.59 (2026-06-29) to 7.09 today** — a 17.5% decline in average true range, and the lowest reading in the visible lookback window. ATR/price = **2.90%** per session.
- **Bollinger width is collapsing:** upper 256.71, lower 230.51 → width **26.20 points**. On 2026-06-22 that width was **50.71 points** (276.85 − 226.14). That is an **~48% compression in one month**. Band width near 10.7% of the mid-band (243.61) is tight for AMZN.
- **Price positioning within the bands:** close 244.85 is **+1.24 above the middle band (243.61)** and roughly midway between the bands (≈55% of the way up from the lower to the upper band). It is **11.86 points below the upper band** and **14.34 points above the lower band**. Nothing extreme.

**Practical consequence:** narrow ATR + narrow Bollinger width = **a coiled market**. Historically this pattern resolves in a directional expansion, but the tool output does not allow me to claim any historical win-rate; treat it as a *conditional probability setup*, not a forecast. For risk purposes:
- **1×ATR stop = 7.09 points** (~2.9%).
- **1.5×ATR stop = 10.6 points** (~4.3%) — my preferred buffer given the current whipsaw character.
- Position size = (Account risk %) ÷ (Stop distance in $). Example: $100,000 account, 1% risk ($1,000), 2×ATR stop (14.18) ⇒ ~70 shares.

---

## 7. Volume: the missing ingredient of the rebound (VWMA)

This is the most nuanced part of the picture and deserves careful reading:

- **VWMA is at 247.03 and *rising* aggressively** — it climbed from 236.52 (2026-06-30) to 247.03 today, a **+4.4% rise in three weeks**. That means the volume-weighted center of trading has moved *sharply upward*, i.e., the bulk of recent contracts changed hands at progressively higher prices. On its own, that is a bullish read on accumulation.
- **But price (244.85) is now 2.18 points (−0.9%) BELOW the VWMA.** The cost basis of recent buyers is above the current price. That is a short-term negative: the marginal buyer is underwater, and the VWMA at ~247 becomes an overhead supply shelf.
- **Volume is drying up.** Today's 34.11M is well below the 22-session average of ~56.6M, and below the ex-outlier average of ~47.4M (the 2026-06-26 print of **248.4M** is a clear outlier, likely an index/rebalance event, and should be excluded from any average). Recent sessions cluster at **27.7M–45.3M**, versus 60M–78M during the June decline.
- **The bullish reading:** a decline on contracting volume (7/17 → 7/22 on 43.6M → 32.4M → 27.7M → 34.1M) is consistent with **orderly profit-taking rather than distribution**.
- **The bearish reading:** the +13.7% July rebound was itself built on below-average volume — 30–45M/day versus 60M+ during the selloff. **Low-conviction rallies are more likely to be retraced.**

**Net:** the volume evidence is genuinely mixed and argues for *patience*, not conviction in either direction. Confirmation of any long thesis should require a **>50M-share up-day** through the 247–250.6 zone.

---

## 8. Actionable price levels (all derived from tool-printed prices)

**Resistance (overhead stack — this is why the rally stalled):**
1. **247.03 / 247.09** — VWMA and 10-EMA convergence. A tight, meaningful cluster. Today's failure to hold it is the proximate cause of the fade.
2. **249.34 / 249.65** — 2026-07-21 high (249.34) and 2026-07-13 high (249.65).
3. **250.60** — the declining 50-SMA, plus the 2026-07-10 high of 251.03 just above.
4. **254.96 / 256.48 / 258.08** — 2026-07-15 close, 2026-07-15 high, and 2026-07-16 high (the swing high of the rebound). Bollinger upper band at 256.71 sits inside this zone, reinforcing it.

**Support:**
1. **242.45** — today's low, and just below the Bollinger middle band at 243.61. A close below both would confirm the short-term rollover.
2. **240.14–241.70** — the 6/29–7/1 congestion (closes 240.14, 238.34, 241.70), reinforced by the 7/8 low of 240.52.
3. **232.00–234.46** — a *major* confluence: the 200-SMA (234.46), the 6/23–6/24 lows (232.00 / 232.95) and the 6/22–6/24 closes (232.79 / 234.11 / 234.27). A daily close below ~232 would flip the long-term trend read to neutral.
4. **225.55–227.01** — the June swing low, with the Bollinger lower band at 230.51 as an intermediate marker.

---

## 9. Scenarios and trade plans

**Base case — range consolidation between ~240 and ~251 (probability-weighted by the evidence).** Trend (200-SMA up), momentum (MACD positive but fading), volume (light) and volatility (compressed) all point to chop. **Action: no new full-size position; manage existing longs with a trailing plan; wait for the range to resolve.**

*Scenario A — Bullish resolution (needs 251+):* A daily close **above 250.60 (50-SMA) on volume > 50M** would neutralise the medium-term bear structure and put 254.96 → 258.08 in play, with the Bollinger upper band at 256.71 as the magnet. Entry on the breakout close or on the first successful retest of 247–248 from above. **Initial stop: 2×ATR = 14.2 points below entry (i.e., ~237.5 if entering near 251.7)**, which sits just under the 240.14 support shelf — a wide but volatility-appropriate stop. Reduce size accordingly.

*Scenario B — Bearish resolution (needs 242.45 to break):* A daily close **below 242.45 and the Bollinger middle at 243.61** with expanding volume opens the 240 area and then the 234.5 region. The MACD would likely re-cross bearishly at that point, and the 50/200 spread would compress further. **Do not short into the 200-SMA (234.46)** — that is where dip-buyers and the long-term trend are most likely to defend, and where a reversal risk is highest.

*Scenario C — Preferred asymmetric entry (buy the confluence, not the middle):* If price retraces to **236–240** while RSI holds above ~40 and volume is *not* expanding on the decline, that zone offers a favourable risk/reward against the 232/234.46 confluence: entry ~238, stop ~230.5 (−1×ATR below the 200-SMA, = 7.5 points, ~3.2% risk), first target 247–250.6 (the overhead cluster). That is a roughly **1.3:1 to 1.7:1 reward-to-risk setup** measured to the first resistance — acceptable only because the long-term trend is intact; size it as a half position.

*Scenario D — Invalidation:* A daily close **below 232.00** breaks both the 200-SMA and the June base, and would invalidate the entire "buy the dip in an uptrend" framework. At that point, stand aside entirely rather than averaging down.

**Stops and sizing rules for all scenarios:** use ATR 7.09 as the unit. Minimum stop = 1×ATR (7.09, ~2.9%); recommended = 1.5×ATR (10.6, ~4.3%) in a Bollinger-contraction regime, because false breaks are common as volatility bottoms. Never place a stop inside the 243–244 noise band.

---

## 10. Caveats and honest limitations

- **No historical validation is claimed.** I have not tested this indicator ensemble's hit rate on AMZN, and the tool output does not provide backtest statistics. All statements about "coiled markets resolving" or "low-volume rallies being retraced" are general interpretive frameworks, not measured results on this instrument.
- **No support/resistance "bounce" claims** are made. The levels in §8 are derived arithmetically from specific dated prints in the tool output (each is cited with its date); whether price *respects* them is unknowable in advance.
- **The 2026-06-26 volume print of 248.4M** is a ~4× outlier versus adjacent sessions and distorts any simple volume average; I have flagged it rather than silently incorporating it.
- **The 0.596 "mfi" value** in the verified snapshot appears to be on a 0–1 scale (≈59.6/100); it was not among my eight selected indicators and I have not used it in the analysis.
- **All indicator values above are point-in-time as of the 2026-07-22 session.** The 200-SMA includes data outside the 138-row window I pulled; I have used the tool's value (234.4614) rather than recomputing it.

---

## Summary table

| Dimension | Reading (2026-07-22) | Signal | Key evidence |
|---|---|---|---|
| **Price** | Close 244.85 (O 248.27 / H 248.45 / L 242.45), vol 34.11M | Neutral–soft | −1.09% on the day (from 247.55); −3.97% over five sessions from 254.96 |
| **Short-term trend** | Below 10-EMA 247.09 by −0.9% | Bearish | 10-EMA turned down for the first time since the rebound; two closes below it |
| **Medium-term trend** | Below 50-SMA 250.60 by −2.3% | Bearish but stabilising | 50-SMA down 37 straight sessions from 257.10 (6/18); decline decelerating to ~0.48/day |
| **Long-term trend** | Above 200-SMA 234.46 by +4.4% | Bullish, intact | 200-SMA rising (232.35 on 6/9 → 234.46); 50>200 spread narrowed 24.3 → 16.1 |
| **Momentum (MACD)** | MACD +0.559 / signal −0.158 / hist +0.717 | Bullish crossover intact, deteriorating | Hist fell 66% in five sessions (2.124 → 0.717); MACD crossed zero only on 7/15 |
| **Momentum (RSI)** | 48.40 | Neutral | Peaked at 60.14 (7/15), never overbought; trough 33.63 (6/25), never oversold |
| **Volatility** | ATR 7.09 (2.9% of price); Bollinger width 26.20 (was 50.71 on 6/22) | Contracting | ~48% band-width compression in one month; 1.5×ATR stop ≈ 10.6 pts |
| **Volume** | VWMA 247.03 and rising; price 0.9% *below* it | Mixed | ~34M today vs ~47M ex-outlier 22-day avg; July rally lacked volume |
| **Position in bands** | Boll mid 243.61 / UB 256.71 / LB 230.51 | Neutral, mid-band | Close sits ~55% up the band; 11.9 pts below UB, 14.3 above LB |
| **Overhead resistance** | 247.03–247.09 → 249.34/249.65 → 250.60/251.03 → 254.96–258.08 | Caps upside | Four-layer supply stack directly above price |
| **Downside support** | 242.45 → 240.14–241.70 → 232.00–234.46 → 225.55–227.01 | Well-defined | 200-SMA at 234.46 is the pivotal long-term line |
| **Recommendation** | **HOLD / no new full-size position** | Wait for resolution | Accumulate only on a volume-confirmed reclaim of 250.60, or buy the 236–240 confluence with a stop below 230.5; stand aside below 232 |
| **Risk parameters** | ATR 7.09; stops 7.1 (1×) to 14.2 (2×) points | — | Size = account risk ÷ stop distance; half-size in the contraction regime |