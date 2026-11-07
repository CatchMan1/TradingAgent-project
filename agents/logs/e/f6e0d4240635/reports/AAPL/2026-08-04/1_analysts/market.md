# AAPL — Technical Analysis Report (as of close 2026-08-04)

## 1. What the tape just did

AAPL printed a violent two-session air-pocket at the end of July, then stabilized on the session I'm analyzing.

- **Record close:** 340.08 on 2026-07-28 (intraday high 344.57 on 2026-07-29).
- **2026-07-31:** gapped down to a 304.81 open from a 333.43 prior close (−8.6% gap), traded 310.69 high to **300.00 low**, closed 308.91 on **132.49M shares** — roughly 2.4x the ~55M average of the prior 22 sessions (computed from the tool's own rows).
- **2026-08-03:** continued down to a 303.42 close (low 302.56) on 75.05M shares.
- **2026-08-04 (verified snapshot):** open 302.73, low 301.32, high 310.42, **close 309.38**, volume 68.00M. That is a **+1.96%** day that closed in the upper third of its range, above the 300–302 shelf.

Net: **−9.03% from the 340.08 record close in four sessions**, but the last session is a constructive reversal candle, not another capitulation bar. The pullback has retraced price back into the **308.63–312.66** zone that was the launch pad on 2026-07-02/07-06 — i.e., a retest of the breakout area rather than a full trend break.

## 2. Indicator selection (8 core) and why

The market context is *a high-momentum uptrend that has just suffered a high-volume shock* — so I need (a) multi-horizon trend structure, (b) momentum confirmation/divergence, (c) volatility for risk sizing, and (d) volume-weighted price to test whether the selling was distribution.

| Indicator | Value 2026-08-04 | Why it matters here |
|---|---|---|
| close_50_sma | 309.61 | Price is sitting *exactly* on it (309.38). This is the pivotal line of the whole setup. |
| close_200_sma | 278.54 | Strategic trend anchor; defines the bull-market line and the downside magnet. |
| close_10_ema | 320.45 | Captures the short-term break; also the first real resistance overhead. |
| macd | 3.110 | Still positive → the shock is a momentum reset, not yet a zero-line trend flip. |
| macds | 6.631 | Crossed **above** the MACD line on 2026-07-31 → bearish trigger. |
| rsi | 44.68 | Overbought condition (71.65 on 07-17) fully unwound without a price collapse to oversold. |
| atr | 9.775 | Volatility repriced +22% on 07-31 (8.06 → 9.87); essential for stops and sizing. |
| vwma | 323.70 | Volume-weighted cost of the recent advance sits **above** price → recent buyers are underwater (distribution signature). |

*Supplementary cross-check (not counted in the core 8): the Bollinger envelope from the verified snapshot — middle 323.841, upper 345.657, lower 302.025. The 08-04 close sits only ~17% of the way up from the lower band, inside a still-very-wide ~43.6-point envelope (~13.5% of the middle band) that is a direct volatility read on the shock.*

## 3. Trend structure — three timeframes, three different answers

**Long term (bullish, intact).** Close 309.38 is **+11.07% above the 200SMA (278.54)**, and the 50SMA (309.61) is **31.07 points (+11.2%) above** the 200SMA. The golden-cross configuration has been in place all year and the 200SMA is still rising steadily (277.96 on 07-31 → 278.54 on 08-04, ~+0.4/5 sessions). Nothing in the long-term data says this uptrend is over; the 200SMA has not been touched since Q1 (the January–March base lows of 243.42 on 2026-01-20 and 245.51 on 2026-03-30).

**Medium term (deteriorating / at the decision point).** The 50SMA has gone flat: 309.30 (07-30) → 309.50 (07-31) → 309.52 (08-03) → 309.61 (08-04). A flattening 50SMA after a parabolic run is the classic signature of a trend transitioning to neutral. Price closing at 309.38 versus a 309.61 50SMA is a **coin-flip test** — a break of it in either direction is a legitimate signal, but the *slope* of the average has stopped helping the bulls.

**Short term (bearish).** Price is **3.45% below the 10EMA (320.45)**, which itself peaked at 331.31 on 07-30 and has fallen four straight sessions. VWMA (323.70) peaked 329.58 on 07-30 and has also turned down for four sessions, and price is **4.42% below it**. A price below both the fast EMA and the volume-weighted average means the average recent buyer — including everyone who bought the July breakout — is now holding a loss. That is overhead supply, and it is why the 320–324 area is the critical overhead test.

## 4. Momentum — the reset, quantified

- **RSI** fell from 71.65 (2026-07-17) to 40.34 (2026-08-03) — a **31.3-point collapse in 11 sessions** — and has ticked back to **44.68**. Important nuance: RSI never reached 30. It got to 40.3 and bounced, which historically in a strong uptrend (RSI in the 60s–70s for weeks) is the *shallow* version of a reset. But 44.68 is also unambiguously below the 50 midline, so the immediate momentum bias is negative-neutral, not positive.
- **MACD:** the line peaked at 9.609 on 07-29 and is now 3.110 (−6.50), with the signal at 6.631. The bearish crossover occurred **on 2026-07-31** and the histogram has deteriorated monotonically: +0.643 (07-30) → −1.367 (07-31) → −2.978 (08-03) → **−3.521 (08-04)**. Note the histogram's *rate* of deterioration slowed slightly on 08-04 (change of −0.54 vs −1.61 the prior session) — early deceleration, not yet a turn.
- **Key distinction:** the MACD line at +3.110 remains above zero. This is a bearish cross *within* a positive regime. A close of the MACD line below zero would be the second, more serious confirmation, and it would likely coincide with a break of the 300–302 shelf.

## 5. Volatility and risk — the most actionable part

ATR rose from 8.06 (07-30) to **9.775 (08-04)**, a **+21.3%** expansion in three sessions. At 3.16% of the 309.38 close, this repriced daily risk materially.

- **Hard stops based on 1x ATR from the 309.38 close** land near **299.60** — essentially the 300.00 low of 07-31. A 2x ATR stop lands near **289.8**.
- **Practical implication:** position size should be cut roughly 20% versus late July for the same dollar risk. A 1.5x ATR (≈14.7 points) risk unit is a reasonable swing-trade framework.
- The 08-04 session range was 9.10 points (301.32–310.42), very close to 1 ATR — normal for this new regime, not an outlier.
- Bollinger width of ~43.6 points means a "normal" move from the middle band (323.84) to the lower band (302.03) is fully achievable in a few sessions, which is exactly what happened between 07-30 and 08-03. Don't treat lower-band contact as a bounce signal on its own.

## 6. Volume — the tell behind the drop

The 132.49M shares on 07-31 is the second-highest volume in the entire trailing year of this dataset, behind only 261.78M on 2026-06-26. The combination of a −8.6% gap, a close near the low of the range, and 2.4x average volume is textbook **distribution**, and the VWMA turning down for four sessions confirms it: the volume-weighted cost basis (323.70) is now above spot.

There is a mitigating detail: volume *declined* on the two sessions after the shock (132.49M → 75.05M → 68.00M) while price held the 300.00 line. Fading volume on a retest is more consistent with panic exhaustion than with a sustained institutional exit. The prior comparable shock in this dataset — the 2026-06-25 gap down from a 293.08 close to 275.15 (−6.1%) on 107.01M shares, with a 273.75 low — was fully retraced within five sessions (close back to 294.38 by 07-01). That is a *precedent in the data*, not a guarantee, but it argues for treating this as a shakeout until the 300 level actually breaks.

## 7. Levels that matter (all from tool output)

**Immediate support / pivot**
- **309.61** — 50SMA; 309.38 close is *on* it. This is the line in the sand for the neutral thesis.
- **308.63–312.66** — the 07-02 and 07-06 closes, i.e., the breakout shelf price has retraced into.
- **301.32–302.56** — 08-04 low, 08-03 low, and the lower Bollinger band at 302.03. A confluence shelf.
- **300.00** — 07-31 low; the psychological and structural floor of the shock.

**Resistance**
- **320.45** — 10EMA (fast, falling).
- **321.66** — 07-23 close, the last minor swing low before the final leg up.
- **323.70 / 323.84** — VWMA and Bollinger middle band. **A close above this cluster is the single cleanest proof that the shock is fully absorbed.**
- **333.43** — 07-30 close (the pre-gap close); the gap-fill objective.
- **340.08 / 344.57** — record close (07-28) and record intraday high (07-29).

**Downside if the shelf fails**
- **293.08–294.38** — 2026-06-24 close / 07-01 close region, an intermediate pause zone.
- **278.54** — 200SMA, only ~10% below spot and the strategic line.
- **273.75** — 2026-06-25 low, sitting just below the 200SMA. A 274–279 confluence is the "trend repair or trend break" zone.

## 8. Actionable playbook

**Bull / continuation (base case leans slightly this way, but is conditional):** The 08-04 reversal (low 301.32, close 309.38, upper-third of range) plus fading volume plus a still-positive MACD line argues the 300–302 shelf is being defended. Confirmation requires **two consecutive closes back above 320.45 (10EMA)**, then a break of **323.70–323.84 (VWMA / mid-band)**. Above that, the 333.43 gap-fill and a retest of 340.08 become live. Stop for such a setup belongs below **300.00**, sized at ~1x ATR (9.78) or better.

**Bear / failure:** A **daily close below 300.00** invalidates the reversal day and the lower band, and converts the 50SMA cross into a genuine medium-term breakdown. First objective 293–294, then 278.54 (200SMA). A concurrent MACD line push below zero would raise confidence in that path materially.

**Neutral / highest-probability near term:** chop between roughly **300 and 324** as the 10EMA rolls over and the 50SMA flattens. In this regime the correct action is patience — do not buy at 309 in the middle of the range with ATR at 3.2% of price; wait for the edge of the range or for a reclaim of the 320–324 cluster.

**Risk rules:** risk ≤ 0.5–1% of capital per position; stops at 1–1.5 ATR (≈10–15 points); reduce size ~20% vs late-July levels; avoid holding through the next high-volume session without a defined stop, since the 07-31 gap (−8.6% overnight) proves that gap risk in this name is real and stops do not protect against it.

## 9. Key points summary

| Category | Reading (2026-08-04) | Signal |
|---|---|---|
| Close / range | 309.38, high 310.42, low 301.32 | Constructive reversal day, +1.96% |
| Drawdown | −9.03% from 340.08 record close (07-28) | Sharp but not trend-destroying |
| 200SMA | 278.54, rising | Long-term uptrend intact (+11.07% above) |
| 50SMA | 309.61, flattened | Neutral; price exactly on it |
| 10EMA | 320.45, falling 4 sessions | Short-term bearish (−3.45%) |
| VWMA | 323.70, falling 4 sessions | Recent buyers underwater → overhead supply |
| MACD / Signal | 3.110 / 6.631, hist −3.521 | Bearish cross on 07-31, but line still >0 |
| RSI | 44.68 (from 71.65 on 07-17) | Overbought fully unwound, sub-50 |
| ATR | 9.775 (+21.3% since 07-30) | Size down; 1-ATR stop ≈ 299.6 |
| Volume | 132.49M (07-31) ≈2.4x avg; 68.0M (08-04) | Distribution, now fading |
| Bollinger | mid 323.84 / upper 345.66 / lower 302.03 | Price in lower third; wide bands |
| Pivotal support | 300.00–302.56 | Break = medium-term breakdown |
| Pivotal resistance | 320.45–323.84 | Reclaim = shock absorbed |
| Stance | Neutral with a defensive bullish tilt | Wait for 300 break or 324 reclaim |

*Data note: all OHLCV and indicator values above are taken from the verified snapshot for 2026-08-04 and the indicator series, which agree with each other. One flag: the snapshot also reports an `mfi` value of 0.4759, which appears to be on a 0–1 scale rather than the standard 0–100 MFI scale; I have therefore excluded money-flow from the analysis rather than interpret a number whose normalization is unclear.*