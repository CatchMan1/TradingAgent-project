# AAPL — Multi-Timeframe Technical Assessment
**As of the close of 2026-10-05 · Last price $332.89**

---

## 1. Verified snapshot (source of truth)

Before any interpretation, the verified snapshot for AAPL on 2026-10-05:

| Field | Value |
|---|---|
| Open | 332.82 |
| High | 336.21 |
| Low | 331.65 |
| **Close** | **332.89** |
| Volume | 34,400,900 |
| close_10_ema | 333.5511 |
| close_50_sma | 322.4136 |
| close_200_sma | 289.4500 |
| MACD (12,26) | 3.4838 |
| MACD signal | 4.5529 |
| MACD histogram | −1.0690 |
| RSI (14) | 53.789 |
| Bollinger mid (20) | 332.5410 |
| Bollinger upper | 346.1594 |
| Bollinger lower | 318.9226 |
| ATR (14) | 6.8582 |
| VWMA | 335.4715 |

**Data integrity note:** I cross-checked `get_stock_data` (151 rows, 2026-03-02 → 2026-10-05) against `get_verified_market_snapshot`. The 2026-10-05 OHLCV row and every indicator value agree exactly between the two sources — no discrepancy to flag. One structural caveat: the 200-day SMA is vendor-computed and therefore uses price history *before* 2026-03-02, which is outside the retrieved CSV; treat the 289.45 figure as authoritative but its internal composition as not independently verifiable from this dataset. Two dividend rows exist ($0.27 on 2026-05-11 and 2026-08-10), no splits.

---

## 2. Regime classification

**Primary regime: intact long-term uptrend, currently in a short-term momentum digestion/coiling phase.**

The three facts that define the current state:

1. **Trend is up and stacked correctly** — price (332.89) > 50-SMA (322.41) > 200-SMA (289.45). Both averages are rising.
2. **Momentum has decelerated** — MACD has crossed below its signal (histogram −1.069 for five consecutive sessions), the 10-EMA has rolled over and price is below it, and RSI has cooled from 66.9 to 53.8.
3. **Volatility is contracting inside a defined range** — ATR down 14.8% from its 09-11 peak, Bollinger width down 23.6% from its 09-23 peak, and price pinned almost exactly on the 20-day mid-band (51.3% band position).

This is the signature of a *bull-market pause*, not (yet) of a distribution top. The distinction matters because the correct playbook differs: trend-following longs stay valid while support holds, but new entries at the middle of the range have poor reward-to-risk until a breakout or a proper retest occurs.

---

## 3. Trend structure, by timeframe

### Long-term (200-SMA): firmly bullish
- 200-SMA at **289.45**, up from 281.50 on 2026-08-21 (+2.82% over ~6.5 weeks), a smooth, near-linear rise of roughly $0.30/session.
- Price sits **+15.0% above** the 200-SMA. That is a meaningful premium — historically a zone where AAPL has been prone to mean-reversion pauses — but it is down from the September peak premium. On 2026-09-22 (close 339.75), price was ~18.4% above the then-current 200-SMA (~286.9). So roughly a third of the overextension has already been worked off without breaking anything.
- 50-SMA minus 200-SMA = **+33.0 points (+11.4%)**, and widening. The golden-cross regime established earlier in 2026 remains fully intact.

### Medium-term (50-SMA): rising but has gone flat
- 50-SMA at **322.41**, up from 310.21 on 2026-08-21 (+3.94%).
- **Critical nuance:** the *rate* of rise has collapsed. Daily increments: +0.06 (09-29), +0.11 (09-30), +0.09 (10-01), +0.24 (10-02), **−0.003 (10-05)**. The 50-SMA has effectively flatlined at ~322.4 over the final six sessions.
- In practice the 50-SMA is no longer "catching up" to price. If the consolidation continues another 1–2 weeks, price will converge toward it, and a test of 322 becomes a live possibility rather than a remote one.

### Short-term (10-EMA): rolled over
- 10-EMA at **333.55**, and price closed **0.20% below it**.
- The 10-EMA peaked at **335.96 on 2026-09-28** and has declined for five straight sessions (335.96 → 334.77 → 334.45 → 333.70 → 333.70 → 333.55). The flattening of the last two sessions shows the pullback has lost downside velocity — but the average has not turned back up.
- For a trend-following swing long, the 10-EMA is the "is this working?" line. Price is on the wrong side of it. That alone argues against adding fresh length at market.

### Price structure: an 8-session coil after a failed push at 345
Sequence of daily highs since the top: 345.34 (09-22) → 341.80 → 338.91 → 341.67 → 342.99 → 337.09 → 339.50 → 332.48 → 334.54 → **336.21 (10-05)**.
Sequence of daily lows over the same span: 335.50 (09-23) → 334.30 → 334.53 → 338.04 → 328.70 → 330.14 → **325.81 (10-01)** → 330.61 → **331.65 (10-05)**.

Read correctly: the *first* five sessions made lower highs (a pullback), then 09-29 broke the range down to 328.70, then 10-01 flushed to **325.81** and reversed, and the last three sessions have produced **rising lows (325.81 → 330.61 → 331.65) with rising highs (332.48 → 334.54 → 336.21)**. That is a short-term *basing* pattern nested inside a larger uptrend — constructive, but it is occurring *below* the VWMA and *below* the 10-EMA, so it is not yet a confirmed resumption.

**Important structural observation:** the 344.5–345.3 zone has now rejected price twice. Intraday high on 2026-07-29 was **344.57**; the next session closed at 333.43 and the session after that **gapped open at 304.81** (−7.36% close-to-close vs. 333.43). Then on 2026-09-22 the market printed **345.34** and again failed. Two tests, two failures, one violent gap in between. This makes 344.5–345.3 the single most important resistance shelf on the chart, and it makes the current consolidation a *distribution risk* as much as a *coiling opportunity*.

---

## 4. Momentum

### MACD: bearish cross, but above zero
- MACD line **3.484** vs. signal **4.553**; histogram **−1.069**.
- The bearish crossover occurred on **2026-09-29**, when the histogram flipped from **+0.537** (09-28: 6.0786 − 5.5420) to **−0.283** (09-29: 5.1877 − 5.4712).
- The MACD line peaked at **6.248 on 2026-09-22** and has fallen 44% since — a genuine deceleration, not noise.
- **However**: the MACD line is still *positive* (3.48 > 0). A signal-line cross above the zero line is a pullback-within-uptrend signal. A cross *below* zero would be a materially more serious event, and at the current pace of decline (~0.4–0.8/session) that is roughly 5–8 sessions away unless price stabilizes.
- **Encouraging detail:** the histogram has stopped widening. Last four readings: −0.990 (10-01), −1.013 (10-02), −1.069 (10-05). The deterioration is decelerating. A histogram turn back above zero would be the cleanest early re-entry trigger, and it typically leads price by a few sessions.

### RSI: neutral, no extremes, tentative positive divergence
- RSI at **53.79**, down from its period peak of **66.88 on 2026-09-22** — a 13-point cooling, but nowhere near oversold.
- Over the last month RSI has ranged 49.3 (09-09) to 66.9 (09-22). It has not touched 70 at any point in the retrieved window, meaning the September rally never became a blow-off. That is *bullish for durability* — there is no trapped overbought supply to force-unwind.
- **Tentative positive divergence:** price made a lower low on 10-01 (325.81 vs. 328.70 on 09-29), while RSI made a marginally *higher* low (51.43 vs. 50.88). The magnitude is small and the sample is two points — I would not trade it standalone, but it corroborates the "flush-and-recover" reading of the 10-01 session.

**Momentum synthesis:** the bearish MACD cross says "don't chase." The neutral RSI and above-zero MACD say "don't panic." Net: momentum is *coiling*, and the resolution direction is unproven.

---

## 5. Volatility and the squeeze setup

### ATR: compressing
- ATR(14) = **6.858**, equal to **2.06% of the close**.
- Down **14.8%** from 8.046 on 2026-09-11.
- Realized true ranges for the last five sessions: 4.56 (10-05), 3.93 (10-02), 6.67 (10-01), 9.36 (09-30), 8.39 (09-29) — averaging 6.58, which is consistent with the ATR reading (no conflict).
- Practical translation: a normal day is now ±$6.86, i.e., roughly ±2%. Stops tighter than ~$7–8 are inside the noise band and will be harvested.

### Bollinger Bands: textbook contraction with a flat upper band
| | 2026-09-23 | 2026-10-05 | Change |
|---|---|---|---|
| Upper | 344.764 | 346.159 | +0.40% |
| Mid | 326.948 | 332.541 | +1.71% |
| Lower | 309.132 | 318.923 | +3.17% |
| Width | 35.632 | 27.237 | **−23.6%** |

- Band width is **8.19% of the mid-band**, down from **10.90%** twelve sessions ago.
- **The shape is the tell:** the upper band has been essentially frozen at 346.2–346.9 for six consecutive sessions, while the lower band has climbed aggressively from 309.1 to 318.9. That is a volatility squeeze forming *under* a fixed ceiling.
- **Position within the bands: 51.3%** — price is dead-center. Center-band straddles are the lowest-information position on the chart: no edge long, no edge short. The edge only appears on a decisive band-tag or a band-width expansion.
- Implication: the next 1–2 weeks should see a range expansion. Expanding ATR + expanding band width in the *direction of the break* is the confirmation filter; a break on flat/declining volume is the classic false-breakout trap.

---

## 6. Volume and participation

### VWMA: price is below the volume-weighted cost basis
- VWMA **335.47** vs. close **332.89** → price is **0.77% below** it.
- VWMA has *stalled*: 335.34 (09-30) → 335.30 (10-01) → 335.30 (10-02) → 335.47 (10-05), versus a steep prior climb from 308.80 on 08-21 (+8.6%).
- Interpretation: the average dollar-weighted buyer from the recent window is slightly underwater. That creates a supply pocket on any rally into 335–336 — precisely where the 10-05 high (336.21) printed. VWMA and the session high are effectively the same level, which upgrades 335.5–336.2 from "minor resistance" to "the pivot."

### Volume behavior: participation faded into the high
- The September advance launched on genuinely strong volume: 65.6M (09-09), 70.0M (09-10), 50.7M (09-11), 86.6M (09-18, likely an index/expiry session).
- But the final push to the 345.34 high came on declining volume: 40.7M (09-22), 31.7M (09-23), 24.7M (09-24 — the lowest in the series), 30.0M (09-25).
- The 09-29 breakdown carried 38.5M, and the 09-30 recovery carried **50.0M** — up-volume exceeded down-volume on the test, which is modestly constructive (buyers defended 328–330).
- 2026-10-05 volume of 34.4M is **0.82× the 20-session average of ~42.0M** (computed from the 20 sessions 09-08 → 10-05). Nobody is voting.

**Volume synthesis:** fading volume into a double-top rejection zone, followed by low-volume chop, is *ambiguous*. It is not the heavy-volume distribution that would confirm a top, nor the volume thrust that would confirm accumulation. It is a market waiting for a catalyst.

### Event-risk history (must be respected)
The retrieved window contains two violent, high-volume dislocations that both recovered — but only after inflicting serious drawdowns:
- **2026-06-25:** open 287.40 → close 275.15 (from 293.08 prior close), 107.0M shares, followed by 261.8M shares on 06-26 (a capitulation-and-reversal session closing at 283.78).
- **2026-07-31:** prior close 333.43 → **open 304.81** → close 308.91, 132.5M shares, a −7.36% close-to-close gap with no intraday escape.

Both were recovered (06-25 low 273.75 → 344.57 by 07-29; 07-31 close 308.91 → 345.34 by 09-22), which argues the dip-buying regime is intact. But it also means **gap risk around events is empirically large** — larger than ATR implies, because ATR does not capture overnight gaps of this magnitude. Any position held through a known catalyst should be sized for a −7% gap, not for a 2% daily range.

---

## 7. Actionable level map

All levels below are drawn directly from retrieved prices; no level is inferred from unobserved history.

| Type | Level | Source / date |
|---|---|---|
| Resistance 4 | **346.16** | Bollinger upper band, 2026-10-05 |
| Resistance 3 | **344.57 – 345.34** | 2026-07-29 high / 2026-09-22 high — **double rejection shelf** |
| Resistance 2 | **341.67 – 342.99** | 2026-09-25 high / 2026-09-28 high |
| Resistance 1 | **339.50** | 2026-09-30 high |
| **Pivot** | **335.47 – 336.21** | VWMA / 2026-10-05 high |
| Spot | **332.89** | 2026-10-05 close |
| Support 1 | **331.65** | 2026-10-05 low |
| Support 2 | **330.14 – 330.61** | 2026-09-30 low / 2026-10-02 low |
| Support 3 | **328.70** | 2026-09-29 low — range floor |
| Support 4 | **325.81** | 2026-10-01 low — flush low, key invalidation |
| Support 5 | **322.41** | 50-SMA (flatlined) |
| Support 6 | **318.92** | Bollinger lower band |

The tighter, more operative range is **325.81 – 342.99**; the coiling range of the last four sessions is just **331.65 – 336.21**. A close outside 331.65–336.21 is the first information; a close outside 325.81–342.99 is the real signal.

---

## 8. Scenario framework with explicit triggers

**Base case — continued coil, 50% weight.**
Price grinds between 328.70 and 339.50 as ATR and band width compress further. Triggers: closes holding above 330.14 but failing below 336.21; MACD histogram stabilizing near zero; volume staying below ~40M. *Action: no new position at 332.89. Manage existing longs with the stop below 325.81; wait for the range to resolve.*

**Bullish resolution — 30% weight.**
Requires, in order: (1) a daily close above **336.21** (the 10-05 high) that also reclaims VWMA at **335.47**; (2) confirmation with volume ≥ 1.2× the ~42M average, i.e. >**50M**; (3) MACD histogram turning positive. First objective **339.50**, then **341.67–342.99**, with the 344.57–345.34 double-top as the decisive test. *A breakout above 342.99 that holds projects the 17.2-point coil height (342.99 − 325.81) higher, implying roughly 360 — but given two prior rejections at 345, that projection should be treated as a contingent target, not a base case, and the 346.16 upper band will cap the first attempt.*

**Bearish resolution — 20% weight.**
Sequence: loss of **331.65** → loss of **330.14** → break of **328.70** on expanding volume (>45M). That opens **325.81**, and a daily close below it would break the pattern of rising lows and put the **322.41 50-SMA** and then **318.92 lower band** in play. A MACD move below zero would confirm. *This is the scenario the double-top at 345 and the fading volume into that high argue you must respect — not predict.*

---

## 9. Risk management, sized to actual volatility

- **ATR = 6.858 (2.06% of price).** This is the unit of risk.
- **Tactical long stop:** below 328.70 − 0.5 ATR ≈ **325.3**, i.e. ~2.3% risk from 332.89. This sits under the range floor but above the 10-01 flush low; it will survive normal noise but not a genuine breakdown.
- **Structural long stop:** below **318.95** (the 10-01 low of 325.81 minus 1.0 ATR), which conveniently coincides with the Bollinger lower band at 318.92. This is a ~4.2% risk and should only be used by position traders with a longer horizon.
- **Position sizing example:** a $100,000 account risking 1.0% ($1,000) with the 325.3 stop (7.59 points of risk) supports ~131 shares ≈ **$43,600 notional**. With the structural 318.95 stop (13.94 points) it supports ~71 shares ≈ **$23,800 notional**. Volatility is *falling*, so a fixed-dollar-risk framework will mechanically allow larger size — that is exactly when discipline matters, because a squeeze resolution can double ATR in days.
- **Gap buffer:** given the observed −7.36% overnight gap on 2026-07-31, size any catalyst-exposed position at roughly **one-third** of what the ATR math implies, or hedge with options.
- **Invalidation of the bullish thesis:** a daily close below the 50-SMA (322.41) with MACD below zero. That combination would mean the medium-term trend has stopped rising, at which point the "buy the dip" premise no longer has a trend to lean on.

---

## 10. Why these eight indicators

| Indicator | Why it earns a slot in *this* market |
|---|---|
| **close_200_sma** | Establishes the strategic regime. At +15.0% above a smoothly rising 200-SMA, it quantifies both trend integrity and mean-reversion distance — the single best answer to "is this a bull market?" |
| **close_50_sma** | Captures the medium-term trend *and* its inflection. Its six-session flatline at 322.41 is the clearest evidence that the September advance has stalled, and it defines the structural invalidation level. |
| **close_10_ema** | The fastest read on whether the pullback is over. Price below it and the EMA rolling over for five sessions is the reason not to add at market — a signal the two slower averages cannot give. |
| **macd** | The primary momentum-change detector. Identifies the 09-29 bearish cross and, crucially, its position relative to zero (still +3.48), which distinguishes a pullback from a reversal. |
| **rsi** | Independent momentum scale with bounded units. Confirms the move was never blow-off (no 70 print) and that current conditions are neutral (53.8), and provides the only divergence evidence in the dataset. |
| **boll** (with upper/lower) | Captures volatility state and position simultaneously. Width contraction of 23.6% plus a frozen upper band is a squeeze signature no oscillator reveals, and the 51.3% band position quantifies "no edge at mid-range." |
| **atr** | Converts everything above into executable risk. Without it, stop placement (325.3 vs. 318.95) and position size are guesswork. |
| **vwma** | The only volume-aware input. It shows the volume-weighted buyer is 0.77% underwater and that 335.47 is a genuine supply shelf — a level the price-only averages miss entirely. |

**Deliberately excluded:** `macds` and `macdh` (both fully derivable from the `macd` series I retrieved and are redundant as *separate selections*); `boll_ub`/`boll_lb` (used, but as components of the Bollinger read rather than independent signals); and any second oscillator so as not to double-count momentum — RSI already covers that job, and stacking StochRSI on top would produce correlated, not complementary, information.

---

## 11. Bottom line

AAPL is in a **confirmed long-term uptrend undergoing a short-term momentum pause inside a tightening coil**. The bullish case rests on structure: price above a rising 50- and 200-SMA, a +15% trend premium, an RSI that never reached overbought, no breakdown of the rising-lows sequence since 10-01, and a MACD that remains above zero despite its bearish cross. The bearish case rests on *participation*: volume faded into the high, the 344.5–345.3 zone has rejected price twice (once with a −7.4% gap), the 50-SMA has flatlined, and price cannot reclaim its own VWMA.

The resolution is genuinely undetermined, which is itself the actionable insight: **at 332.89, dead-center of the Bollinger bands and below both the 10-EMA and VWMA, there is no positive-expectancy entry.** The trade is to wait for one of two clean events — a volume-confirmed reclaim of 336.21/MACD-histogram turn (long, targeting 342.99 then 344.57–345.34), or a volume-confirmed break of 328.70 (step aside, with 325.81 as the line that ends the bullish structure). Until then, manage rather than initiate.

---

## Summary Table

| Dimension | Reading (2026-10-05) | Signal | Key level / trigger |
|---|---|---|---|
| **Price** | 332.89 (O 332.82 / H 336.21 / L 331.65) | Neutral | Range 331.65–336.21 |
| **Long-term trend** | 200-SMA 289.45, rising ~$0.30/day; price +15.0% above | **Bullish** | Thesis void below 322.41 |
| **Medium-term trend** | 50-SMA 322.41, rising +3.94% since 08-21 but **flat last 6 sessions** | Bullish, decelerating | 322.41 |
| **Short-term trend** | 10-EMA 333.55; price 0.20% **below**; EMA falling 5 sessions | **Bearish tilt** | Reclaim 333.55 |
| **MACD** | 3.484 vs signal 4.553; hist −1.069 (5 sessions negative); cross 09-29 | **Bearish, above zero** | Hist > 0; MACD < 0 = escalation |
| **RSI** | 53.79 (from 66.88 on 09-22); no 70 print in window | Neutral | >60 bullish / <45 bearish |
| **Bollinger** | Mid 332.54, UB 346.16, LB 318.92; width 8.19% (−23.6% since 09-23); %B 51.3% | **Squeeze / no edge** | Break of 331.65 or 336.21 |
| **ATR** | 6.858 = 2.06% of price; −14.8% from 09-11 | Volatility contracting | Stop unit = ~$6.86 |
| **VWMA** | 335.47 vs close 332.89 → price 0.77% **below**; VWMA flat 4 sessions | **Mild bearish / supply** | 335.47 is the pivot |
| **Volume** | 34.4M = 0.82× 20-day avg (~42.0M); faded into 09-22 high | Ambiguous, low conviction | >50M needed for valid break |
| **Primary resistance** | 339.50 → 341.67–342.99 → **344.57–345.34 (double rejection)** → 346.16 | Overhead supply | Close >342.99 = breakout |
| **Primary support** | 331.65 → 330.14–330.61 → **328.70** → 325.81 → 322.41 → 318.92 | Rising lows since 10-01 | Close <328.70 = caution; <325.81 = structure break |
| **Base case (50%)** | Coil 328.70–339.50, further volatility compression | Wait | No entry at mid-range |
| **Bull case (30%)** | Close >336.21 on >50M volume + MACD hist turns positive | Buy confirmation | Targets 339.50 / 342.99 / 345.34 |
| **Bear case (20%)** | Close <328.70 on expanding volume, then <325.81 | Reduce / stand aside | Targets 322.41, 318.92 |
| **Risk unit** | ATR $6.86 (2.06%) | — | Tactical stop 325.3 (2.3%); structural 318.95 (4.2%); size for −7% gap risk |