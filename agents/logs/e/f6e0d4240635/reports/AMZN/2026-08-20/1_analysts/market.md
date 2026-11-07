# AMZN — Multi-Timeframe Technical Report
**Analysis date:** 2026-08-20 · **Last verified close:** $260.11 · **Data source:** verified market snapshot (source of truth)

---

## 0. Verification & data notes (read first)

- The `get_stock_data` series and the `get_verified_market_snapshot` **agree exactly** on the 2026-08-20 row: open 263.16, high 263.84, low 259.52, **close 260.11**, volume 28,374,100. No discrepancy to flag.
- All indicator values below are taken from the verified snapshot / indicator tool output and match each other to the decimal (e.g. 50 SMA 249.3162, 200 SMA 238.3029, 10 EMA 263.6652, MACD 4.1466, signal 5.3831, histogram −1.2365, RSI 50.916, ATR 7.7458, VWMA 272.0527).
- The snapshot also returns an MFI-like field (0.35155). It is **not** on the approved indicator list, so I have deliberately excluded it from the analysis rather than build a thesis on an unverifiable scale.
- Bollinger values (mid 260.05, upper 296.45, lower 223.65) are used as a **supplementary volatility-envelope check** beyond the 8 core indicators; they are verified numbers, not estimates.

**8 selected indicators and why:** `close_10_ema` (short-term timing), `close_50_sma` (medium trend + key support reference), `close_200_sma` (long-term regime + golden-cross context), `macd` (momentum trend level), `macdh` (rate-of-change of momentum — the earliest signal of the current stall), `rsi` (momentum state / overbought reset), `atr` (volatility regime → stop and size calibration), `vwma` (volume-weighted participation → overhead supply). This set deliberately avoids redundancy: three *different* trend horizons, one momentum oscillator, one momentum-difference measure, one volatility measure, one volume-weighted price measure.

---

## 1. What actually happened: a violent re-rating, then a controlled give-back

The six-month tape has three distinct regimes:

**Regime 1 — February earnings shock (2/5–2/17).** AMZN closed 222.69 on 2/5, opened 202.70 on 2/6 (a ~9% gap down) on 179.2M shares, and bottomed at 196.00 on 2/17. Also note 2/6 volume was the second-largest in the entire sample.

**Regime 2 — methodical April–July advance.** Off the 3/27 low close of 199.34, price ground higher to 274.00 on 5/28, then chopped sideways-to-lower into 7/29 (close 226.65). Critically, the **50 SMA crossed above the 200 SMA on 2026-05-06** (228.73 vs 228.08) — a textbook golden cross that has stayed intact and widened since (today +11.01 points).

**Regime 3 — the 7/31 re-rating and the August fade.** 7/30 closed 235.50; **7/31 opened 265.00 and closed 271.58** on 129.1M shares. 8/3 extended to 284.02 (intraday high **287.20**, the high of the sample) on 90.8M shares. Since then, thirteen sessions of persistent distribution:

| Date | Close | High | Low | Volume |
|---|---|---|---|---|
| 2026-08-03 | 284.02 | **287.20** | 278.00 | 90.8M |
| 2026-08-04 | 277.42 | 281.07 | 275.82 | 69.7M |
| 2026-08-10 | 278.09 | 280.14 | 273.60 | 35.7M |
| 2026-08-12 | 267.28 | 273.46 | 267.10 | 29.9M |
| 2026-08-14 | 262.65 | 265.81 | 262.42 | 27.3M |
| 2026-08-17 | 261.31 | 265.75 | 258.34 | 43.9M |
| 2026-08-18 | 259.45 | 262.18 | **257.73** | 33.2M |
| 2026-08-19 | 265.84 | 266.40 | 258.58 | 35.8M |
| 2026-08-20 | **260.11** | 263.84 | 259.52 | **28.4M** |

- Peak close (8/3) to 8/20 close: **284.02 → 260.11 = −8.42%**.
- Intraday peak (287.20) to 8/20 close: **−9.43%**.
- Yet still **+10.45%** above the 7/30 pre-gap close of 235.50, and **+30.5%** above the 3/27 low close of 199.34.

**The most important structural fact:** the 8/20 close of 260.11 is now **below the entire 7/31 session range** (open 265.00, low 262.01, high 273.23). Three of the last four closes (8/17: 261.31, 8/18: 259.45, 8/20: 260.11) sit beneath that 7/31 low of 262.01. The breakaway gap's real body has been fully retraced, and price is now working **into the gap void** (unfilled between 7/30's high of 239.82 and 7/31's open of 265.00). Roughly the top ~19% of that void has now been penetrated. This materially weakens the "breakaway gap never fills" bull case but does not yet break it.

---

## 2. Trend: three timeframes, three answers

**Long-term (200 SMA) — bullish.** 200 SMA has risen monotonically in the observed window from 226.02 (4/22) to **238.30 (8/20)**, and price is **+9.15% above it**. The 50/200 spread is +4.62% and widening slightly. Nothing in the long-term structure is damaged.

**Medium-term (50 SMA) — bullish, and just bottomed.** The 50 SMA declined from 257.10 (6/18) to a trough of **246.38 (7/30)**, then turned up: 246.63 (7/31) → 247.59 (8/10) → 248.17 (8/14) → **249.32 (8/20)**. The earnings gap arrested and reversed the medium-term slope. Price is **+4.33% above** the 50 SMA, i.e. the pullback has not even tested medium-term support.

**Short-term (10 EMA + price structure) — bearish.** The 10 EMA peaked at **267.18 (8/11–8/12)** and has declined for six straight sessions to **263.67 (8/20)**. Price has closed below it in five of the last six sessions (8/13, 8/14, 8/17, 8/18, 8/20), with only the 8/19 spike (265.84) above it. Confirming the short-term downtrend, both swing highs and swing lows are falling since 8/3:

- Swing highs (closing basis): 284.02 → 278.09 → 266.40 → 263.84
- Swing lows (closing basis): 272.26 → 267.28 → 259.45 → 260.11

**Synthesis:** this is a *pullback inside an uptrend*, not a trend reversal — but it is a pullback with genuine distribution characteristics, not a benign drift. The single most consequential number is that **price is 3.56 points (1.35%) below a falling 10 EMA while still 10.79 points above a rising 50 SMA.** That compression between a falling short-term average and a rising medium-term average is the definition of a resolution setup.

---

## 3. Momentum: the earnings impulse has fully decayed

**MACD (12/26/9):**
- MACD line bottomed at −6.88 (6/26–7/09 area), crossed zero on **7/15** (0.26), and peaked at **8.43 (8/11)**.
- It has now fallen for seven consecutive sessions to **4.15 (8/20)**.
- Signal line peaked at 6.22 (8/14) and is at **5.38**, so the MACD line sits **below** signal.
- Histogram: peak **+4.62 (8/05)** → zero on **8/17 (−0.31)** → **−1.24 (8/20)**. **A confirmed bearish crossover (8/17) that is still widening.**

Nuance that matters: both MACD (4.15) and signal (5.38) remain **well above zero**. A negative histogram with a positive MACD line is a *de-risking / consolidation* signal, not a trend-sell signal — in strong uptrends this configuration has historically marked digestive pauses more often than reversals. The trigger that would upgrade this to a genuine bearish momentum regime is the **MACD line crossing below zero**, and that requires another ~4.15 points of decay (roughly 8–12 sessions at the current rate of change). Traders should not front-run that.

**RSI (14):** 72.23 on **8/03** (the price peak — a clean overbought print at the top), then a textbook monotonic reset: 65.87 (8/10) → 60.97 → 57.06 → 55.41 → 53.49 → 52.43 → 50.93 (8/18) → 55.64 (8/19) → **50.92 (8/20)**. This is the *constructive* version of an RSI reset: the overbought condition was worked off without RSI breaking 40 or price breaking the 50 SMA. However, RSI has now **failed to make a higher high on the 8/19 bounce** (55.64 vs 65.87 on 8/10), which confirms weakening momentum rather than signaling a fresh leg up. RSI at 50.9 is genuinely neutral — it provides **no directional edge**; there is no divergence signal in either direction in the verified data.

---

## 4. Volatility: extremely wide bands, mechanically set to compress

This is the most under-appreciated part of the setup.

- Bollinger (20,2): mid **260.05**, upper **296.45**, lower **223.65**. Full bandwidth = **72.80 points = 28.0% of price** (2σ ≈ 36.4 pts, i.e. a 20-day σ of ~18.2, or ~7.0% of price). On 7/06 the same measure was 21.68 points (9.0% of price). **Bandwidth has more than tripled in six weeks.**
- **The 8/20 close (260.11) is sitting almost exactly on the middle band (260.05).** Zero edge, maximum indecision.
- The upper band is 14% above spot — price never tagged it even at the 284.02 peak (upper band was 290.69 on 8/10). No band-ride occurred, so band-based "overbought" reads are useless here.
- **Mechanical caveat:** the 7/31 and 8/3 gap sessions remain inside the 20-day window. They roll out by roughly **end-August**. Expect a large, involuntary narrowing of Bollinger bandwidth around then. Do **not** mistake that statistical artefact for a market-generated squeeze signal — this is the one place where a naive Bollinger reading will mislead.
- **ATR (14):** peaked at **9.948 (8/03)** and has declined for **nine consecutive sessions** to **7.746 (8/20)** — a **−22.1%** contraction. ATR is now **2.98% of price**. Combined with the wide-band-to-mid-band pin, this is a **coiling** tape: volatility is contracting *and* price is at the mean of a much-widened distribution. Historically that resolves violently, in one direction.

**Risk calibration from ATR:** 1×ATR = 7.75 (3.0%), 1.5×ATR = 11.62 (4.5%), 2×ATR = 15.49 (6.0%). Any stop tighter than ~1 ATR (~8 points) is noise-tight given this regime.

---

## 5. Volume & participation: no capitulation, but real overhead supply

- **Participation is drying up on the pullback.** 8/20's 28.37M shares is among the three lightest sessions since early April (8/14's 27.25M and 5/22's 27.54M were the only lighter). The trailing 10-session average (8/07–8/20) is roughly **33.2M**, versus 129.1M on 7/31 and 90.8M on 8/03 — **volume has normalized to ~26% of peak-day levels**. That is consistent with *orderly digestion*, not panic liquidation. That is the strongest argument that this is a pullback, not a top.
- **But the biggest post-gap volume day was a down day:** 8/17's 43.90M shares accompanied a decline from 262.65 to 261.31. That is distribution, and it is the only session in the last six with clearly elevated volume.
- **VWMA:** 272.05 versus a 260.11 close — **price is 4.39% below its volume-weighted average price**. VWMA has *risen* from 245.72 (7/31) to 272.05 (8/20) while price has fallen. Mechanically this is driven by the huge-volume gap days entering the window, so I would not over-read the magnitude — but the message is real: **the volume-weighted holder base from late July is underwater, creating supply overhead in the 265–272 zone.** That is exactly where the 10 EMA (263.67) and 8/19's high (266.40) also sit. Three independent measures converge on the same resistance band.

---

## 6. Levels map (all derived from tool data, not asserted from memory)

**Resistance (upside):**
| Level | Derivation |
|---|---|
| 263.67 | 10 EMA (falling, 8/20) |
| 266.40 | 8/19 high — most recent swing high |
| 267.45 | 38.2% retracement of the 235.50 → 287.20 earnings leg |
| 272.05 | VWMA — volume-weighted average price |
| 273.46 / 273.50 | 8/12 high / 8/19 VWMA zone |
| 278.09–280.14 | 8/10 close and high |
| 287.20 | Sample high (8/03) |

**Support (downside):**
| Level | Derivation |
|---|---|
| 259.52–257.73 | 8/20 low and 8/18 low (six-session floor) |
| 255.25 | 61.8% retracement of the earnings leg |
| 249.32 | 50 SMA (rising) — key medium-term line |
| 246.38–246.56 | 7/30 50-SMA trough / 78.6% retracement — the confluence line |
| 239.82 | 7/30 high = bottom of the unfilled gap void |
| 238.30 | 200 SMA (rising) — long-term floor |
| 223.65 | Bollinger lower band (rising fast; mechanically distorted) |

Note the genuinely useful confluence: **260.11 corresponds to the ~50% retracement of the entire earnings leg** (50% by closes = 259.76; 50% by intraday extremes = 261.35). Price has landed on the dead centre of the re-rating. That is why the next directional break matters so much.

---

## 7. Actionable framework — three conditional scenarios

The honest verdict is: **no edge at 260.11.** Price is at the Bollinger mid-band, RSI is 50.9, and MACD has just crossed down but remains above zero. The correct posture is *defined* reaction levels, not prediction.

**Scenario A — Preferred: pullback long into 249–252 (probability-weighted as the highest reward/risk).**
- Rationale: 50 SMA 249.32 rising, 78.6% retrace 246.56, and the 8/14–8/18 lows above it. A test of the 50 SMA would also coincide with MACD approaching zero — the classic second-chance entry in a rising 200-SMA regime.
- Illustrative structure: entry ~251, stop **244.50** (below the 246.38/246.56 confluence; per-share risk 6.50 ≈ 0.84 ATR), targets 263.70 (10 EMA) → 266.40 → 273.50. Reward-to-risk to the second target ≈ **2.4:1**.
- Do **not** treat this as a guarantee the 50 SMA holds — it is a level to respond to, and the stop exists precisely because it may not.

**Scenario B — Breakout continuation: needs price confirmation, not anticipation.**
- Trigger: a **close above 266.40** (8/19 high, also reclaiming the 10 EMA and pushing into the VWMA) with volume **above ~45M** and MACD histogram turning back positive.
- Illustrative structure: entry ~267, stop **258.50** (below the 8/18 low 257.73; risk 8.50 ≈ 1.1 ATR), targets 278.09 then 284.02 → reward/risk ≈ 1.3:1 then 2.0:1.
- Note the weaker payoff: chasing a breakout in a contracting-volatility tape gives less favourable maths than buying support.

**Scenario C — Breakdown / gap-fill (counter-trend; smaller size).**
- Trigger: a **close below 257.73** (8/18 low) that is not reversed within one session, with confirmation on a close below **249.32** (50 SMA).
- Illustrative structure: entry ~257, stop **266.50** (risk 9.50 ≈ 1.2 ATR), targets 246.50 (78.6% retrace) then **239.82** (full gap void fill) → reward/risk ≈ 1.1:1 then 1.8:1.
- Caveat: this is shorting into a rising 200 SMA with a live golden cross. Reduce size accordingly.

**Invalidation / trend-damage checklist:**
- Close below **249.32** → medium-term trend flips neutral; below **246.38** → the earnings structure is broken and the 239.82 gap-fill becomes the base case.
- MACD line below **zero** (from 4.15) → bearish momentum regime confirmed.
- RSI below **40** → distribution confirmed (not extreme; RSI hit 33.31 on 7/29 pre-gap).
- Conversely, a close back above **266.40** with the histogram turning positive repairs the 8/03–8/20 lower-high sequence.

**Position sizing note:** with ATR at 2.98% of price (vs 2.65% on 7/29 pre-gap and 3.50% at the 8/03 peak), size positions off the *current* 7.75 ATR, not the calmer pre-earnings regime. A 1.5-ATR stop implies ~11.6 points (~4.5%) of risk per share — roughly 12–15% smaller share counts than a pre-earnings volatility assumption would suggest.

---

## 8. The nuanced bottom line

AMZN sits at a genuine three-way inflection. The **long-term and medium-term trends are intact and objectively improving** (200 SMA rising nine months, golden cross since 2026-05-06 and widening, 50 SMA turned up on 7/31, price +9.15% / +4.33% above them). The **short-term trend is unambiguously lower** (falling 10 EMA, confirmed MACD bearish crossover on 8/17, four consecutive lower swing highs, all of the 7/31 gap candle retraced). The two readings are not contradictory — they describe a maturing pullback within an uptrend. What tips the balance toward caution rather than aggression is that (a) price is now below its volume-weighted average price (272.05), (b) the pullback's only high-volume session (8/17, 43.9M) was a down day, and (c) 8/19's strong reversal close (265.84, near the session high) **failed to follow through** on 8/20, which closed in the bottom ~14% of its range. Meanwhile the *constructive* counterweights are real: no capitulation volume, ATR contracting for nine straight sessions, and an RSI that reset from 72.2 to 50.9 without breaking the 50 SMA.

The most defensible action at 260.11 is to **not initiate in the middle of the range**. Let the tape pick a side: 257.73 for the downside resolution, 266.40 for the upside. The pending mechanical collapse in Bollinger bandwidth at month-end will make that resolution look sharper than it economically is — don't be fooled by it.

---

## 9. Summary table

| Dimension | Reading (2026-08-20) | Interpretation | Actionable level / trigger |
|---|---|---|---|
| **Close** | 260.11 (open 263.16, H 263.84, L 259.52, vol 28.37M) | Closed bottom ~14% of range; weak close | — |
| **10 EMA** | 263.67, falling 6 sessions (peak 267.18 on 8/11–12) | Short-term trend **down**; price 1.35% below | Reclaim >263.67 needed for repair |
| **50 SMA** | 249.32, rising since 7/30 trough of 246.38 | Medium-term trend **up**; price +4.33% | Support 249.32; break = neutral |
| **200 SMA** | 238.30, rising since 4/22 (226.02) | Long-term trend **up**; price +9.15% | Golden cross (5/06) intact, spread +11.01 |
| **MACD** | 4.15 (peak 8.43 on 8/11) | Momentum decaying but still positive | Zero-line cross = regime change |
| **MACD hist** | −1.24; zero crossed 8/17 (peak +4.62 on 8/05) | Confirmed **bearish crossover**, widening | Turn back positive = repair |
| **RSI** | 50.92 (peak 72.23 on 8/03) | Fully reset, neutral; no divergence | <40 bearish / >65 bullish |
| **ATR** | 7.746 (2.98% of price); down 9 sessions from 9.948 | Volatility **contracting**; coiled | 1×ATR=7.75; 1.5×ATR=11.62 stop unit |
| **VWMA** | 272.05; price 4.39% **below** | Overhead supply / underwater holder base | Resistance cluster 265–272 |
| **Bollinger** (suppl.) | Mid 260.05 / UB 296.45 / LB 223.65 | Price pinned at mid-band; bandwidth 28% of price, mechanically set to compress by month-end | Edge only on a band tag; ignore "squeeze" headlines |
| **Gap structure** | 7/30 high 239.82 → 7/31 open 265.00 | Close **below** the entire 7/31 session; ~19% of void penetrated | Full fill target 239.82 |
| **Fib of earnings leg** | 235.50 → 287.20 | 260.11 = ~50% retracement (259.76 by close) | 38.2% 267.45; 61.8% 255.25; 78.6% 246.56 |
| **Scenario A (preferred)** | Long 249–252 | Buying rising 50 SMA in an uptrend | Stop 244.50; targets 263.7 / 266.4 / 273.5; R:R ~2.4:1 |
| **Scenario B** | Long >266.40 close, vol >45M | Breakout continuation | Stop 258.50; targets 278.09 / 284.02; R:R ~1.3–2.0:1 |
| **Scenario C** | Short <257.73, confirm <249.32 | Gap-fill continuation (counter-trend, small size) | Stop 266.50; targets 246.50 / 239.82; R:R ~1.1–1.8:1 |
| **Verdict** | No edge at 260.11 — mid-band, RSI 50.9, hist negative | Mature pullback in an intact uptrend; wait for resolution | Let 257.73 or 266.40 break first |