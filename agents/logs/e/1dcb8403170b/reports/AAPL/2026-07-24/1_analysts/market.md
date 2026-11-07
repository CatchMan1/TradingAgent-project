# AAPL — Multi-Timeframe Technical Analysis
**Analysis date: 2026-07-24 | Last completed session: 2026-07-24 | Source of truth: verified market snapshot**

---

## 1. Data Integrity & Verification Baseline

The verified snapshot (2026-07-24) and the `get_stock_data` CSV agree **row-for-row** with zero discrepancy, and every indicator value returned by `get_indicators` matches the snapshot exactly (close_50_sma 306.2314 / close_200_sma 275.9804 / close_10_ema 324.5396 / macd 8.4465 / macds 7.5385 / macdh 0.9080 / rsi 65.2331 / boll_ub 346.3577 / boll_lb 282.4133 / atr 8.2629 / vwma 322.8027). **No conflicts to flag.**

**Latest verified bar (2026-07-24):**
| Field | Value |
|---|---|
| Open | 321.79 |
| High | 334.37 |
| Low | 321.62 |
| Close | **333.02** |
| Volume | 47,489,400 |
| Prior close (2026-07-23) | 321.66 |
| Session change | **+11.36 (+3.53%)** |
| Session range | 12.75 pts (**3.83%** of close) = **1.54× ATR** |

Two data caveats worth stating explicitly rather than silently absorbing:
- The snapshot's `mfi` field prints as **0.616349**, i.e. a 0–1 normalized scale, not the conventional 0–100. Read as ~61.6. It is *not* an 0.6 MFI reading. I have not used it in the signal set.
- Volume on **2026-06-26 was 261,775,500** (~5× the surrounding sessions) and **2026-06-25 was 107,013,700**. This is a rebalance/event-type volume spike, not organic trend volume. It contaminates any simple moving-average-of-volume read and I treat it as an outlier below.

---

## 2. Regime Classification

AAPL is in a **confirmed, mature, primary uptrend** that is currently in an **accelerated re-acceleration phase after a completed mid-cycle correction**. The defining sequence, all from verified closes:

1. **Rally:** 2025-10-01 close 255.45 → 2026-06-02 close 315.20.
2. **Correction:** 2026-06-02 close 315.20 → 2026-06-25 close 275.15 = **−12.71%** in 16 sessions.
3. **Recovery to new highs:** 2026-06-25 close 275.15 → 2026-07-17 close 333.74 = **+21.29%**.
4. **Shallow pullback:** 2026-07-17 close 333.74 → 2026-07-23 close 321.66 = **−3.62%**.
5. **Reclaim:** 2026-07-24 +3.53% to 333.02, i.e. **+21.03% off the 06-25 low**.

The structural signature of this regime is that **the June decline was absorbed and fully retraced within four weeks** — a hallmark of a bull-market pullback rather than a trend reversal. The 2026-07-24 bar is an **outside/engulfing day**: it opened at 321.79, printed a low of 321.62, then closed at 333.02 — above the entire 2026-07-23 range (319.35–323.30) — while closing within 2 points of the 06-25-to-date closing high.

---

## 3. Trend Structure — Three Nested Timeframes

### Long-term (200 SMA) — unambiguously bullish
- **close_200_sma = 275.98**, rising monotonically every single session in the dataset (261.99 on 05-26 → 275.98 on 07-24).
- Price at 333.02 sits **+20.67% above** the 200 SMA.
- This is a *strategic* confirmation only. At +20.7% extension, the 200 SMA is useless as a tactical stop (it would imply a 17% drawdown) but it is decisive evidence that the primary trend is up and that long-side bias is correct.

### Medium-term (50 SMA) — bullish, but extended
- **close_50_sma = 306.23**, also rising every session (271.72 on 05-26 → 306.23 on 07-24).
- **50 SMA minus 200 SMA = +30.25 pts**, and the spread is **widening** (it was +9.73 on 05-26). The golden-cross configuration established earlier remains intact and is *expanding* — a textbook continuation signature, not a deteriorating one.
- Price sits **+8.75% above** the 50 SMA. Context for that number: at the 06-25 low (273.75 intraday) price was **~6.0% below** the then-50 SMA of 291.15. The pendulum has swung from 6% below to 8.75% above in 21 sessions. **Mean-reversion risk toward the 50 SMA is now materially higher than it was three weeks ago**, even though trend direction is unchanged.

### Short-term (10 EMA) — bullish, freshly reasserted
- **close_10_ema = 324.54**, up from 289.33 on 06-30. The short-term average has risen **~12% in under four weeks** — a steep, momentum-driven slope.
- Price is **+2.61% above** the 10 EMA.
- The 2026-07-24 low of **321.62** briefly undercut the 2026-07-23 10 EMA value of **322.66** and was reclaimed the same session — a same-bar failed breakdown. That is the single most constructive tactical detail in the dataset, *but note it is a one-bar observation, not a validated multi-test support level.*

**Trend verdict:** all three timeframes point the same direction (up), stacked in correct order (price > 10 EMA > 50 SMA > 200 SMA). This is a "do not short" configuration. The debate is purely about **entry timing and extension**, not direction.

---

## 4. Momentum — The Critical Nuance

### MACD: bullish, but decelerating then stabilizing
- **macd 8.4465 / macds 7.5385 / macdh +0.9080.**
- The bullish signal sequence is fully documented: histogram turned positive on **2026-07-02 (+0.261)**, MACD crossed above its signal then, and MACD crossed above **zero on 2026-07-06 (+0.879)**. Both crossovers remain valid — no bearish crossover has occurred.
- **However**, the histogram peaked at **+3.337 on 2026-07-17** and decayed to **+0.795 on 2026-07-23** before ticking back to **+0.908** on 07-24. MACD peaked at 8.927 on 07-21 and is now 8.447.

### RSI: overbought reset without price damage
- **RSI 65.23** (from 58.11 on 07-23, 62.54 on 07-22).
- RSI hit **71.65 on 2026-07-17** — its highest reading since **79.79 on 2026-05-28**. It then reset to 58.11 on 07-23 during a pullback of only −3.62%, and is now rebuilding.
- **This is the bullish interpretation:** a momentum oscillator reset from overbought territory *without* a corresponding price breakdown is the classic "flag-and-continue" profile seen in strong uptrends.
- **This is the bearish interpretation of the exact same data:** on 2026-07-17 price closed **333.74** with RSI **71.65**; on 2026-07-24 price closed **333.02** (essentially identical, −0.72 pts) with RSI **65.23** (−6.4 RSI points). Price is at the same level with materially less momentum. **That is a negative divergence**, and it is corroborated by the MACD histogram being 73% below its 07-17 peak (0.908 vs 3.337) at effectively the same price.

**How to weight it:** a single-episode divergence at the prior high of a strong uptrend is a *warning to tighten risk and avoid chasing*, not a standalone sell signal. It becomes actionable only if confirmed by (a) failure at 334–335 and (b) a break of the 10 EMA / 07-23 low. Note the intraday high also failed to confirm: 2026-07-24 high **334.37** vs 2026-07-17 high **334.99** and 2026-07-16 high **334.68** — a lower intraday high inside the same resistance cluster.

---

## 5. Volatility & Bollinger Framework

| Measure | Value | Interpretation |
|---|---|---|
| ATR(14) | **8.26** | 2.48% of price — elevated vs the ~5.6–6.1 ATR in late May |
| Boll middle (20 SMA) | **314.39** | rising steeply (294.88 on 07-01) |
| Boll upper | **346.36** | |
| Boll lower | **282.41** | |
| Band width | **63.94 pts = 20.34% of middle** | extreme expansion |
| Close position in bands | **79.1%** of band width | upper third, but not band-riding |

- Price at 333.02 is **13.34 pts (4.0%) below the upper band** — it is *not* hugging the band. In a strong trend, price typically rides the upper band; the fact that it is 4% shy while making near-record highs means the bands have expanded *faster than price*, i.e. this is a **volatility expansion phase, not a squeeze breakout**. Squeeze-breakout logic does not apply here.
- **Important mechanical artifact, flagged rather than interpreted as a signal:** boll_lb jumped from **276.31 (07-23) to 282.41 (07-24)** and boll (middle) jumped from **311.49 to 314.39** in one session. This is almost entirely the **20-day rolling window** dropping the 2026-06-24/06-25 crash closes (293.08 and 275.15) and absorbing the 07-24 surge. The lower band's 6.1-point one-day jump is a **window effect, not new buying support.** Anyone using 282.41 as "support" should understand it is arithmetic from a rolling window, not a tested level.
- **ATR is the more honest volatility read:** 8.26 pts means a "normal" day now moves ±2.5%. The 2026-07-24 range of 12.75 pts was 1.54× ATR — a genuine expansion day, and it should recalibrate stop distances *upward*, not downward.
- ATR has drifted *down* from its 07-02 peak of 8.74 despite the huge 07-24 range — volatility is high but **not accelerating to new extremes**, consistent with an orderly trend rather than a blow-off.

---

## 6. Volume Confirmation — the Weakest Link

**VWMA = 322.80**, and price (333.02) is **+3.17% above** it. VWMA has risen from 288.84 (06-30) to 322.80 — a steep climb confirming that **recent buying is occurring at rising volume-weighted prices** (accumulation, not distribution). Price above VWMA is a genuine bullish confirmation.

**But the raw volume does not confirm the 07-24 move:**
- 07-24 volume **47.49M** vs 07-23 **40.84M** = **+16.3% session-over-session** — good.
- 20-session average (06-26 to 07-24) = **~61.4M**, but that includes the **261.8M** 06-26 outlier. **Excluding that outlier: ~50.8M.**
- So 07-24's 47.49M is **7% below the outlier-adjusted average** and **23% below the raw average**.

**Conclusion:** the +3.53% outside-day reclaim was **not volume-confirmed**. It is a good price signal on indifferent volume. That materially lowers the probability that 334–335 breaks on the first attempt, and it argues against chasing.

---

## 7. Actionable Playbook

### Reference levels (all from verified output)
| Level | Price | Basis |
|---|---|---|
| Bollinger upper | 346.36 | verified snapshot |
| Resistance cluster | **334.37 / 334.68 / 334.99** | 07-24 high / 07-16 high / 07-17 high |
| 2026-07-17 closing high | 333.74 | verified CSV |
| **Current** | **333.02** | 07-24 close |
| 10 EMA | 324.54 | verified snapshot |
| VWMA | 322.80 | verified snapshot |
| 07-23 low / 07-21 low | **319.35 / 322.22** | verified CSV |
| Bollinger middle (20 SMA) | 314.39 | verified snapshot (see window caveat) |
| 50 SMA | 306.23 | verified snapshot |
| Bollinger lower | 282.41 | verified snapshot (window-inflated) |
| 2026-06-25 low | 273.75 | verified CSV |
| 200 SMA | 275.98 | verified snapshot |

### Trade A — Preferred: buy the pullback (highest R:R)
- **Trigger:** a pullback holding **319.35** (07-23 low) on declining volume, ideally into the **322.80–324.54** (VWMA / 10 EMA) confluence.
- **Entry zone:** 322–325.
- **Stop:** close below **318.50** (below 07-23 low, ~0.6× ATR of the entry zone).
- **Target 1:** 334.90 (resistance cluster). **Target 2:** 346.36 (upper band).
- **R:R:** ~1 : 1.8 to T1 and **~1 : 3.5** to T2 (risk ~5.5 pts, reward ~10 / ~22 pts).
- **Why this is preferred:** chasing at 333.02 with a stop under 319.35 gives only ~1 : 0.9 to T1. The reward/risk is simply better 8 points lower.

### Trade B — Breakout continuation (requires volume)
- **Trigger:** a **close above 335.00** — and this must come with volume **> 60M** to invalidate the tepid 47.5M reading. Without that volume, treat a 335 poke as a likely false breakout into the divergence.
- **Stop:** close back below **324.54** (10 EMA).
- **Target:** 346.36 (upper band), with a stretch toward the measured move of the 07-17→07-23 pullback width (11.9 pts) projected from 335 ≈ 347 — which conveniently **converges with the upper band at 346.36**. That confluence is the strongest technical argument for the breakout case.
- **R:R:** ~1 : 1 at best. Only take this with a trailing intraday stop, not a wide structural stop.

### Trade C — The short case (only for tactical traders)
- **Setup:** negative divergence (price = 07-17 level, RSI −6.4 pts, MACD histogram −73%) inside a 3-touch resistance cluster, on non-confirming volume.
- **Trigger:** rejection candle at 334–335 **plus** a decisive loss of **324.54** (10 EMA) and then **319.35**.
- **Stop:** above 335.50.
- **Target:** 314.39 (Boll middle), then 306.23 (50 SMA).
- **Caveat:** this is a **counter-trend** trade against a stacked bullish MA structure with a rising, expanding golden cross. Position size at half normal. The 50 SMA at 306.23 is 12 pts below the middle band and 15 pts away — bear in mind that during the June decline price only reached 6% below the 50 SMA before reversing, so a full round-trip to the 50 SMA is an ambitious target for a short.

### Risk management calibration
- **ATR 8.26 = 2.48% of price.** Size positions so that a **1.5×ATR** adverse move (≈12.4 pts, to ~320.6) costs no more than your per-trade risk budget. A 2×ATR stop is 316.5.
- **Do not use fixed-point stops carried over from May.** ATR was 5.6 on 05-29 and is 8.26 now — stops must be **~47% wider** for equivalent protection.
- **Expect ±2.5% daily noise.** The 07-24 bar alone spanned 3.83%. Single-bar reads of 07-24 are low-confidence; require a close.

---

## 8. What Would Change the View

| Development | Signal |
|---|---|
| Close > 335.00 on volume > 60M | Divergence negated; continuation to 346.36 live |
| Close < 319.35 | Short-term trend break; 314.39 then 306.23 (50 SMA) in play |
| MACD histogram crosses below zero (currently +0.908) | Bearish MACD crossover confirmed — first momentum failure since 07-02 |
| 50 SMA − 200 SMA spread contracts from +30.25 | Long-term structure deteriorating; currently the opposite |
| Price closes below the 50 SMA (306.23) | Would break the pattern of the June decline (which bottomed ~6% below the 50 SMA); regime change |
| RSI reclaims > 71 with price > 335 | Divergence resolved to the upside; confirms 07-17 was a pause, not a top |

---

## 9. Indicator Selection Rationale (8 selected)

| Indicator | Why it earns a slot here |
|---|---|
| **close_10_ema** | The regime is momentum-driven and fast; the 10 EMA is the operative tactical line (324.54) and it defined the 07-24 undercut-and-reclaim. Not redundant with the 50/200, which are far away. |
| **close_50_sma** | Provides the medium-term trend read *and* the extension metric (+8.75%) that drives the mean-reversion risk assessment. The 50/200 spread (+30.25 and widening) is the cleanest golden-cross diagnostic available. |
| **close_200_sma** | Strategic trend anchor; confirms the June drawdown was a correction, not a reversal. Its slow, monotonic rise (261.99 → 275.98) is unambiguous. |
| **macd** | Best-in-class for verifying that the 07-02 bullish crossover and 07-06 zero-line cross remain intact, and for measuring the deceleration (8.927 on 07-21 → 8.447) at resistance. |
| **rsi** | Essential for this specific setup: it is the indicator that exposes the divergence (71.65 @ 333.74 vs 65.23 @ 333.02). Skipping it would miss the single most important caveat. |
| **boll_ub** | Bands are at 20.34% width — an extreme expansion regime. The upper band at 346.36 is both the primary upside target and the *convergence point* for the measured-move projection, making it functionally valuable. |
| **atr** | Volatility has structurally changed (5.6 → 8.26) and the 07-24 bar was 1.54× ATR. ATR is the only indicator here that produces defensible stop distances and position sizes. |
| **vwma** | The sole volume-integrated measure in the set, and it carries the whole accumulation/distribution verdict: price +3.17% above VWMA confirms volume-weighted accumulation even while raw 07-24 volume fails to confirm the breakout. |

**Deliberately excluded:** `macds` and `macdh` (redundant with `macd` — signal and histogram values cited narratively without consuming slots); `boll` and `boll_lb` (used as context above, but the lower band at 282.41 is currently a rolling-window artifact and the middle at 314.39 is nearly coincident with nothing price has tested, so they earn no dedicated slot); `stochrsi` (overlaps RSI); `mfi` (the snapshot returns a 0–1 normalized 0.6163, an ambiguous scale — excluded on data-quality grounds rather than analytical ones).

---

## 10. Summary Table

| Dimension | Reading (2026-07-24) | Verdict | Confidence |
|---|---|---|---|
| **Verified close** | 333.02 (+3.53% vs 321.66) | Outside/engulfing reclaim day; range 12.75 = 1.54× ATR | High |
| **Long-term trend** | Price +20.67% above 200 SMA (275.98), 200 SMA rising every session | Strong uptrend | High |
| **Golden cross** | 50 SMA − 200 SMA = +30.25, widening from +9.73 on 05-26 | Intact and expanding | High |
| **Medium-term trend** | Price +8.75% above 50 SMA (306.23) | Bullish but extended (was −6.0% vs 50 SMA at the 06-25 low) | High |
| **Short-term trend** | Price +2.61% above 10 EMA (324.54); 07-24 low 321.62 undercut then reclaimed | Bullish, one-bar evidence | Medium-High |
| **MACD** | 8.4465 / signal 7.5385 / hist **+0.908**; crossovers from 07-02 and 07-06 valid | Bullish, but hist −73% from 07-17 peak (3.337) | Medium |
| **RSI** | 65.23 (from 71.65 on 07-17, brief reset to 58.11 on 07-23) | Healthy reset **or** negative divergence — both readings valid | Medium |
| **Divergence** | Same price, −6.4 RSI pts and −2.43 MACD-hist pts vs 07-17; lower intraday high 334.37 vs 334.99 | Warning: do not chase | Medium |
| **Bollinger** | Middle 314.39 / Upper 346.36 / Lower 282.41; width 20.34%; close at 79.1% of band | Expansion, not squeeze; 4.0% below upper band | Medium-High |
| **Volatility** | ATR 8.26 = 2.48% of price (was 5.57 on 05-28) | Stops must be ~47% wider than in May | High |
| **VWMA** | 322.80; price +3.17% above, VWMA up from 288.84 on 06-30 | Volume-weighted accumulation confirmed | High |
| **Raw volume** | 47.49M vs outlier-adjusted 20-day avg ~50.8M | 07-24 move **not** volume-confirmed | High |
| **Resistance** | 334.37 / 334.68 / 334.99 cluster | Triple-touch ceiling; needs >60M volume to clear | High |
| **Support** | 324.54 (10 EMA) → 322.80 (VWMA) → 319.35 (07-23 low) → 314.39 → 306.23 (50 SMA) | Layered, well-separated | High |
| **Primary bias** | **Long**, but buy pullbacks — do not chase at 333.02 | Constructive with tight risk | Medium-High |
| **Preferred entry** | 322–325 pullback, stop <318.50, targets 334.90 / 346.36 | R:R ~1:1.8 to 1:3.5 | — |
| **Breakout entry** | Close >335.00 with volume >60M, stop <324.54, target 346.36 (measured move ≈347 converges) | R:R ~1:1 — trailing stops only | — |
| **Counter-trend short** | Only on rejection at 334–335 **+** loss of 324.54 **+** loss of 319.35; targets 314.39 / 306.23 | Half size; fights a stacked bullish MA structure | Low-Medium |
| **Key invalidation** | Close below 319.35 short-term; below 306.23 regime-change | — | High |

**Bottom line:** AAPL at 333.02 is in a documented, multi-timeframe uptrend with an expanding golden cross, volume-weighted accumulation, and a freshly reclaimed short-term average. The one thing it does **not** have is volume confirmation or momentum confirmation at the 334–335 ceiling, and it is 8.75% above its 50 SMA. The correct posture is **constructively long with patience** — let price come to the 322–325 confluence (VWMA / 10 EMA) rather than paying up into a third test of resistance on below-average volume.