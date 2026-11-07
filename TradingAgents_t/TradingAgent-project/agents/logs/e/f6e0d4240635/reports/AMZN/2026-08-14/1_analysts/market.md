# AMZN — Technical & Trend Report
**Analysis date: 2026-08-14 (session close) | Source of truth: verified market snapshot**

---

## 1. Verified Snapshot — Where AMZN Actually Stands

The verified snapshot for **2026-08-14** is the authoritative reference for every figure below:

| Field | Value |
|---|---|
| Open / High / Low / **Close** | 264.88 / 265.81 / 262.42 / **262.65** |
| Volume | 27,251,700 |
| close_10_ema | 266.05 |
| close_50_sma | 248.17 |
| close_200_sma | 237.70 |
| MACD / Signal / Histogram | 6.609 / 6.217 / **0.392** |
| RSI(14) | 53.49 |
| Bollinger mid / upper / lower | 256.52 / 295.43 / 217.61 |
| ATR | 8.17 |
| VWMA | 263.41 |

All values returned by the individual indicator calls are **identical to the snapshot** — no discrepancy to flag. The only note: the snapshot also lists `mfi = 0.526`, but the scale (0–1 vs 0–100) is not documented in the payload, so I exclude it from the analysis rather than misread it.

**Position of price relative to each reference:**
- vs 10 EMA (266.05): **−1.28%** → *below* short-term trend
- vs VWMA (263.41): **−0.29%** → *marginally below* volume-weighted cost
- vs Bollinger mid / 50 SMA (256.52 / 248.17): **+2.39% / +5.84%** → *well above* medium-term trend
- vs 200 SMA (237.70): **+10.50%** → *firmly above* long-term trend

This is the signature of a **strong medium/long-term uptrend undergoing a short-term corrective pullback**, not of a trend reversal.

---

## 2. The Defining Event: The 2026-07-31 Earnings Gap

Any honest read of AMZN must start here. The dated price history shows:

- **2026-07-29:** close 226.65, RSI 33.31 (oversold), ATR 6.89
- **2026-07-30:** open 233.35, close **235.50**, volume **101.8M** (up day into the event)
- **2026-07-31:** open **265.00**, high 273.23, close **271.58**, volume **129.05M** — a **+15.3% single-session close-to-close move** and an opening gap of ~29.5 points vs the prior close of 235.50
- **2026-08-03:** close **284.02** (high **287.20**), volume 90.83M — the highest close and highest intraday print in the entire visible window (since 2026-01-15)

The 129.05M shares on 07-31 is the **largest volume session since 2026-06-26 (248.4M)** and one of the three largest since the February earnings cluster (2026-02-05: 103.5M; 2026-02-06: 179.2M). This is structural re-pricing on institutional participation, not a sentiment wiggle.

**Critical nuance:** the gap void sits between **235.50 (07-30 close)** and **265.00 (07-31 open)**. With the 08-14 close at **262.65**, AMZN has now traded *back inside the top edge of that gap*. The gap is no longer "fully intact." That materially changes the risk map: the first genuine air-pocket below is the 50% retracement of that gap at **≈250.25**, which conveniently coincides with the **50 SMA at 248.17**.

---

## 3. Trend Structure — Bullish Stack, Rising Slopes

**Long-term (200 SMA = 237.70):** Rising monotonically through the entire visible window: 232.59 on 2026-06-15 → 234.75 on 2026-07-30 → 237.70 on 2026-08-14. The long-term trend is unambiguously up and *accelerating slightly* in slope.

**Medium-term (50 SMA = 248.17):** This is the most informative slope change. The 50 SMA **declined persistently** from 257.10 (2026-06-18) to a trough of **246.384 (2026-07-30)** — a two-month bleed. Since 07-30 it has turned **up for 11 consecutive sessions** (246.38 → 248.17). That is a genuine medium-term trend inflection confirmed by price, not just by price crossing a line.

**Golden-cross configuration:** 50 SMA (248.17) > 200 SMA (237.70), with the spread **widening** (+10.46 now). The bullish alignment is intact and strengthening.

**Short-term (10 EMA = 266.05):** The 10 EMA whipped from 236.46 (07-29) to a peak of **267.18 (08-12)** — an extraordinarily fast re-rating — and has now **rolled over for two sessions** (267.18 → 266.81 → 266.05). Price closed below it for a third straight day. The 10 EMA crossed above the 50 SMA on **2026-08-03** (250.22 vs 247.01); that bullish cross remains valid.

**Verdict on trend:** three timeframes, three different answers — long-term up, medium-term turning up, short-term rolling down. The dominant trend is up; the actionable condition is a **pullback within an uptrend**.

---

## 4. Momentum — Rolling Over From an Overbought Extreme

**RSI(14) = 53.49.** The path matters more than the level:
- 33.31 on 07-29 (oversold, pre-gap) → **72.23 on 08-03** (overbought, post-gap peak) → **53.49 on 08-14**
- That is an **18.7-point collapse in nine sessions**, landing almost exactly mid-range

**Interpretation:** This is the *constructive* version of a momentum reset. RSI has fully normalized to neutral **without** price breaking the 50 SMA or even the Bollinger middle band. There is no bearish RSI divergence claim I can substantiate from tool output, and I will not assert one. What is verifiable is that the overbought condition that existed on 2026-08-03 (RSI 72.23) has been worked off, and RSI at 53.5 leaves room in either direction — it is a *decision point*, not a signal.

**MACD = 6.609, Signal = 6.217, Histogram = +0.392.** The MACD line bottomed on 07-29 at **−3.751** and exploded to **8.432 on 08-11**, its peak. Since then it has decayed for **three straight sessions** (7.985 → 7.372 → 6.609) while the signal line keeps rising (5.806 → 6.119 → 6.217). The histogram compression is dramatic and measurable:

| Date | Histogram (MACD − Signal) |
|---|---|
| 2026-08-10 | +3.904 |
| 2026-08-11 | +3.171 |
| 2026-08-12 | +2.179 |
| 2026-08-13 | +1.253 |
| 2026-08-14 | **+0.392** |

At this rate of decay the histogram crosses zero **within roughly one to two sessions** unless price stabilizes immediately. Traders should expect a **bearish MACD crossover** in the very near term.

**Crucial context:** even after that crossover, the MACD line would sit at ~6.5, *deeply positive*. This is a **momentum cool-off from an extreme, not a momentum breakdown.** Treating the crossover as a short signal in isolation would ignore that the underlying impulse remains strongly positive.

---

## 5. Volatility — Expanded Regime, Now Compressing

**ATR = 8.17** (3.11% of the 262.65 close). The regime shift is stark:
- Pre-gap (2026-07-24 to 07-29): ATR 7.22 → 6.89 — a *contracting, quiet* tape
- Post-gap peak (2026-08-05): ATR **9.98**
- Now (08-14): **8.17**, declining for six consecutive sessions

So volatility is still **~18% above** the pre-gap baseline but is actively compressing. Practical translation for risk sizing: a "normal" daily range in AMZN is now roughly $8, versus ~$7 in late July. Stops placed tighter than ~1×ATR (≈$8) are inside the noise band and will be hit by mechanics rather than by thesis failure.

**Bollinger bands (supplementary context from the snapshot):** mid 256.52, upper **295.43**, lower **217.61**. Band width is **≈77.8 points, or 30.3% of the middle band** — extreme expansion. Two observations:
1. AMZN's 287.20 peak on 08-03 **never reached the upper band** (which was 272.99 that day). Price has not "ridden the band" — the bands blew out *after* price had already peaked. Standard band-touch mean-reversion logic is therefore not applicable here.
2. The **middle band (256.52) is rising** sharply (243.86 on 07-31 → 256.52 now) and sits just above the 50% gap retracement. That makes **248–257 a densely layered support shelf**, not a single line.

---

## 6. Volume — The Most Constructive Element

**VWMA = 263.41**, price 0.29% below it. The volume-weighted average price of the recent window is essentially *at* the market — recent buyers are at breakeven, not trapped. VWMA has risen relentlessly from 240.82 (07-30) to 263.41, confirming that the post-gap advance carried genuine volume-weighted accumulation.

**The pullback's volume signature is the bullish tell:**

| Date | Close | Chg | Volume |
|---|---|---|---|
| 08-03 | 284.02 | — | 90,830,200 |
| 08-05 | 272.65 | −1.7% | 45,119,800 |
| 08-10 | 278.09 | +1.3% | 35,731,900 |
| 08-11 | 272.27 | −2.1% | 31,895,700 |
| 08-12 | 267.28 | −1.8% | 29,941,100 |
| 08-13 | 265.13 | −0.8% | 32,170,200 |
| 08-14 | 262.65 | −0.9% | **27,251,700** |

Four consecutive down closes, but on **declining volume into the lowest volume of the whole sequence (27.25M)**. That is the profile of **supply drying up / absence of bids**, not aggressive institutional distribution. The one genuine distribution day was **2026-08-05** — open 281.59, high 282.79, low 270.73, close 272.65 on 45.1M: an outside reversal on elevated volume, which marked the start of this corrective leg.

**Caveat:** light-volume declines can resolve *either* way — they often precede a sharp continued slide if no buyer steps in. Declining volume is a *mitigating* factor, not a buy signal.

---

## 7. Mapping the Levels (all derived from dated tool output)

**Resistance — overhead, in order:**
1. **263.41** — VWMA (immediate; 0.29% above close)
2. **266.05** — 10 EMA (the level price must reclaim to neutralize the short-term downtrend)
3. **267.10** — 08-12 low; **269.58** — 08-13 high (broken support cluster)
4. **272.3–274.5** — the 08-11/08-07/08-06 congestion band
5. **278.0–280.1** — 08-10 close/high (the last lower-high pivot to clear)
6. **287.20** — 08-03 intraday high; **284.02** — 08-03 record close

**Support — below, in order:**
1. **262.01** — 07-31 gap-day low; **262.42** — 08-14 low. *This is the immediate line in the sand, and it is being tested today.*
2. **256.52** — Bollinger middle (rising)
3. **250.25** — 50% retracement of the 235.50→265.00 gap
4. **248.17** — 50 SMA (rising)
5. **237.70** — 200 SMA (the line that would invalidate the whole post-February uptrend)

Support *and* resistance are therefore separated by only ~1.3% (262.01 vs 266.05) — a compressed coil where the next 2–3 sessions are likely to be decisive.

---

## 8. Actionable Playbook

**Base case (preferred): bullish continuation after a shallow retest.**
The confluence of (a) rising 50 SMA, (b) rising 200 SMA with widening spread, (c) RSI reset to 53 from 72 without structural damage, (d) volume drying up on the decline, and (e) VWMA essentially at price — argues that this is a **digestion of the earnings gap**, not the start of a new downtrend.
- **Trigger:** a close back above the **10 EMA at 266.05**, ideally with volume >35M and a MACD histogram that stops compressing.
- **Sequence of objectives:** 269.6 → 274.5 → 278.1 → 287.2.
- **Confirmation bonus:** a fresh histogram expansion *before* the zero-line cross would invalidate the bearish-crossover setup entirely.

**Bear case (respect it, don't front-run it).**
- **Trigger:** a decisive close below **262.01** (the 07-31 gap-day low) — note **262.42** was already the 08-14 low, so this is centimeters away.
- **Targets:** 256.52 (Boll mid) → 250.25 (50% gap fill) → 248.17 (50 SMA). A test of 248–250 would be a **~5.4% to ~5.6% decline** from 262.65 and would coincide exactly with the medium-term trend line plus the gap midpoint — the highest-probability *reversal* zone if the bull thesis is correct.
- **Invalidation of the bull case:** a close below the 200 SMA at **237.70**.

**Risk management (ATR-calibrated, verified values):**
- Structural stop for a long entered near 262–263: **below 256.50** (Bollinger mid) = ~$6.2 risk; below **254.5** (1×ATR = 8.17 off 262.65) if you want noise tolerance.
- Wider swing stop: **2×ATR = 16.35 → 246.30**, which sits just under the 50 SMA at 248.17 — an excellent confluence of a volatility-based and structure-based stop.
- **Position sizing:** with ATR at 3.11% of price, a 1% account risk per trade implies position size ≈ 0.32 × (account / price). Halve normal size around the binary risk that the MACD crossover and the 262.01 test represent simultaneously.
- **Reward/risk for the base case:** entry 262.65, stop 256.50 (risk 6.15), first target 274.50 (reward 11.85) ≈ **1.9:1**; to 278.10 ≈ **2.5:1**.

**What would make me wrong:** a high-volume (≥50M) close below 262.01, an expanding MACD histogram turning negative, or RSI breaking below ~45 while price is under the 10 EMA. Any of those converts this from "pullback" to "failed breakout / gap-fill in progress."

---

## 9. Risks & Caveats

- **Event-driven distortion.** The 07-31 gap is earnings/news-driven; a large portion of the "uptrend" in the moving averages is a single session's re-rating. The 50 SMA at 248.17 is still catching up to reality and will keep rising mechanically for weeks even if price stalls — do not read that as fresh bullish confirmation.
- **No historical bounce claims.** I have not asserted that any prior touch of a moving average or band produced a reversal; the levels above are derived from dated prices and their confluence, not from backtested behavior.
- **Regime risk.** Bollinger width at 30.3% of the middle band means band-based signals are unreliable right now; ATR-based risk framing is more trustworthy than band-based mean reversion.
- **Momentum is still positive.** The MACD line at 6.61 argues strongly against aggressive short exposure; this is a "reduce and wait" tape for longs and a "poorly-located" tape for shorts.

---

## 10. Key Levels Reference

| Level | Value | Source | Role |
|---|---|---|---|
| Intraday high | 287.20 | 2026-08-03 | Cycle high / major resistance |
| Record close | 284.02 | 2026-08-03 | Resistance |
| Lower-high pivot | 278.09 | 2026-08-10 close | Resistance |
| Congestion | 272.3–274.5 | 2026-08-06/07/11 | Resistance |
| 10 EMA | 266.05 | 2026-08-14 | Pivot / first resistance |
| **Last close** | **262.65** | **2026-08-14** | — |
| Gap-day low | 262.01 | 2026-07-31 | **Immediate support (in test)** |
| VWMA | 263.41 | 2026-08-14 | Cost basis of recent flow |
| Bollinger mid | 256.52 | 2026-08-14 | Support |
| 50% gap retrace | 250.25 | 235.50–265.00 gap | Support confluence |
| 50 SMA | 248.17 | 2026-08-14 | Medium-term trend |
| 200 SMA | 237.70 | 2026-08-14 | Bull-case invalidation |

---

## 11. Indicator Selection Summary

| # | Indicator | Value (2026-08-14) | Signal | Why It Was Selected |
|---|---|---|---|---|
| 1 | **close_10_ema** | 266.05 | **Bearish** (price −1.28%) | Fastest read on the short-term roll-over; the exact level to reclaim. 2 sessions of declining slope. |
| 2 | **close_50_sma** | 248.17 | **Bullish** (price +5.84%) | Caught the key inflection: 11 straight sessions rising after 2 months of decline. Definitive medium-term turn. |
| 3 | **close_200_sma** | 237.70 | **Bullish** (price +10.50%) | Confirms the strategic uptrend and widening golden-cross spread (+10.46). Defines invalidation. |
| 4 | **macd** | 6.609 | **Positive but decaying** | Peaked at 8.432 on 08-11, down 3 sessions. Shows impulse remains positive → no short thesis. |
| 5 | **macds** | 6.217 | **Crossover imminent** | Rising signal vs falling MACD; histogram +0.392 collapsing from +3.904 in 4 sessions. Best timing tool here. |
| 6 | **rsi** | 53.49 | **Neutral / reset** | 72.23 → 53.49 in 9 sessions: overbought fully unwound without structural damage. Pure decision point. |
| 7 | **atr** | 8.17 (3.11%) | **Elevated, compressing** | Sets stops and size in a post-gap regime; 2×ATR = 246.30 lands exactly at the 50 SMA. |
| 8 | **vwma** | 263.41 | **Neutral** (price −0.29%) | Volume-weighted confirmation: VWMA rising 240.82→263.41 proves the gap was institutional. Price at cost = coil. |
| — | *boll (supplementary)* | 256.52 / 295.43 / 217.61 | Context only | Band width 30.3% of mid-band → too wide for reliable band signals; used only for the 256.52 support shelf. |

**Bottom line for AMZN:** the primary trend is **up** (price > rising 50 SMA > rising 200 SMA), the intermediate condition is a **volume-light corrective pullback inside a post-earnings gap**, and the immediate tactical setup is a **compressed coil between 262.01 support and 266.05 resistance**. The asymmetry favors buying strength on a reclaim of 266.05, or buying the deeper **248–257** confluence shelf; the risk is a high-volume break of 262.01 that starts a genuine gap-fill toward 250. Wait for the resolution — the MACD histogram crossing zero in the next 1–2 sessions is the trigger to watch.