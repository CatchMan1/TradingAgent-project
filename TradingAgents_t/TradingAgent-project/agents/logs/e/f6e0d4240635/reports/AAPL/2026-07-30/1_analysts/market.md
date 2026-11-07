# AAPL — Technical & Trend Analysis (as of close 2026‑07‑30)

## 1. Data Integrity Note

`get_stock_data` (2025‑10‑01 → 2026‑07‑30) and `get_verified_market_snapshot` (2026‑07‑30) return **identical** final rows and identical indicator values — no discrepancy to flag. All OHLCV, band, MA, RSI, MACD and ATR figures below are taken from the verified snapshot.

**Latest visible session (2026‑07‑30):** Open 333.10 · High 334.75 · Low 329.59 · **Close 333.43** · Volume **74,817,800**
Prior session (2026‑07‑29): Open 339.73 · High **344.57** · Low 337.35 · Close 338.19 · Volume 56,090,800

Day-over-day: **−4.76 (−1.41%)**, with a gap-down open of −5.09 (−1.51%) versus the prior close, and volume running ~35–70% above the typical July session (most July sessions printed 34M–63M; 74.8M is the heaviest volume since 2026‑07‑02's 75.4M).

---

## 2. Market Regime Assessment

AAPL is in a **well-established, mature primary uptrend with decelerating short-term momentum and a fresh two-session reversal off all-time highs on expanding volume.** The tape is not broken — every major trend metric remains positive — but the *rate of change* has clearly peaked. This is a "trend intact, momentum on watch" configuration, which argues for managing existing longs rather than aggressively adding at market.

Regime classification: **Bull trend → late-stage momentum phase / consolidation risk elevated.**

---

## 3. Trend Structure — Moving Average Stack

| Metric | Value (2026‑07‑30) | Position vs. close 333.43 |
|---|---|---|
| close_10_ema | 331.31 | Price **+0.64%** above |
| close_50_sma | 309.30 | Price **+7.80%** above |
| close_200_sma | 277.65 | Price **+20.09%** above |
| vwma | 329.58 | Price **+1.17%** above |

**Stack is textbook bullish and fully ordered:** 10EMA (331.31) > 50SMA (309.30) > 200SMA (277.65). Price sits above all three.

- **The 200SMA is confirming, not driving.** At 277.65 it is 20% below spot; it has risen every single session from 263.60 (2026‑06‑01) to 277.65 (+5.3% over ~40 sessions). A 50SMA/200SMA premium of **11.4%** (309.30 / 277.65) signals a golden-cross structure that has been in force for a long time and is *widening*, not narrowing. That is characteristic of a durable uptrend, but also of a trend extended far from its mean — 20% above the 200SMA is not a low-risk entry zone.
- **The 50SMA is climbing steeply:** 291.15 (2026‑06‑25) → 309.30 (2026‑07‑30), roughly **+0.73 per session** over 25 sessions. Rising medium-term slope = the uptrend's backbone is intact.
- **The 10EMA is where the battle is right now.** It sits at 331.31 and has been advancing only ~0.3–0.5/session (330.84 → 331.31 in the last day). Spot closed 333.43, just **2.12 points above it**. A flat-to-lower close near 330–333 in the next 1–3 sessions would put price *below* the 10EMA and be the first objective short-term trend-tinged signal since 2026‑06‑24 (last session price closed under the 10EMA was 2026‑06‑24: close 293.08 vs 10EMA 296.51).

**Sequencing of the move (all from verified rows):**
- Secondary low: **2026‑06‑25 close 275.15** (intraday low 273.75) following an 8.75% slide from 301.54 (2026‑06‑08), with a 261.8M-share session on 2026‑06‑26 (index/rebalance-type volume).
- Recovery + impulsive advance: 275.15 (2026‑06‑25 close) → **340.08 (2026‑07‑28 close)** = **+23.6% in 23 sessions**. That is an unusually steep advance and is the core reason momentum metrics got stretched.
- 340.08 (2026‑07‑28) is the highest close in the entire visible record (data from 2025‑10‑01); the highest high is **344.57 on 2026‑07‑29**.
- Widest context: close 255.45 (2025‑10‑01) → 333.43 = **+30.5%** over ~10 months. Year-to-date from 271.01 (2026‑01‑02 close) → +23.0%.

---

## 4. Momentum — Where the Deterioration Is Visible

### MACD (12/26/9)
- MACD line: **9.241** (prior 9.609 on 2026‑07‑29 — first down-tick after nine consecutive up-sessions from −2.916 on 2026‑06‑29)
- Signal line: **8.598**, still rising (+0.16/day)
- Histogram: **0.643**

**This is the single most important observation in the report.** The MACD histogram peaked at **3.337 on 2026‑07‑17** and has compressed through 2.724 (7/20) → 2.214 (7/21) → 1.599 (7/22) → 0.795 (7/23) → 1.111 (7/27) → 1.310 (7/28) → 1.172 (7/29) → **0.643 (7/30)**. That is an **81% collapse from peak** while price made a *higher* close on 2026‑07‑28 (340.08 vs 333.74 on 2026‑07‑17).

That is a **classic bearish momentum divergence** confirmed on the histogram, not merely an RSI artifact. The bull cross itself was registered on 2026‑07‑02 (histogram turned positive at +0.261); it remains intact today, but the remaining MACD-minus-signal cushion is only 0.643 and shrinking ~0.53/session. **If price does not reclaim 336+, a bearish MACD crossover is plausible within roughly 1–3 sessions.** That crossover is the cleanest mechanical trigger for de-risking.

### RSI (14)
- Current: **61.66** (2026‑07‑29: 66.78; 2026‑07‑28: 68.90)
- Overbought episode: **71.43 (2026‑07‑16) and 71.65 (2026‑07‑17)** — two consecutive sessions above 70, immediately followed by a drop to 326.59 on 2026‑07‑20 (−2.14%).
- Second divergence: RSI 71.65 at close 333.74 (2026‑07‑17) versus RSI **68.90** at the *higher* close 340.08 (2026‑07‑28) — a **lower momentum high against a higher price high**.
- RSI never reached 70 on the 7/28 attempt, and has now retreated to 61.66 — above the 50 midline, so the *primary* momentum bias is still positive, but the overbought engine has visibly lost thrust.
- Useful reference points from the June episode: RSI bottomed at **32.20 on 2026‑06‑25** (near-oversold) and that marked the tradable low within one session. During the 7/20–7/23 dip RSI only reached **58.11 (2026‑07‑23)** before turning up — showing dip-buyers are still responsive and that RSI ~58 is acting as a soft intra-trend floor.

**Read:** RSI at 61.66 is neutral-to-constructive, not a sell signal on its own. The signal is the *pattern* — two failed pushes at/above 70 and a lower high — layered against the MACD histogram divergence.

---

## 5. Volatility & Bollinger Structure

| Metric | 2026‑07‑30 | Context |
|---|---|---|
| Boll middle (20SMA) | 324.35 | Below spot by 2.7%; steep uptrend |
| Boll upper | 344.54 | Contracting from 346.68 (2026‑07‑23) |
| Boll lower | 304.16 | Rose from 271.83 (2026‑07‑17) |
| ATR (14) | 8.06 | 2.42% of close |

- **%B = 0.725** — price sits in the upper third of the band but has **not** been rejected at the upper band; the 344.57 high (7/29) tagged almost exactly the upper band (344.54 on 7/30). That confluence at ~344.5 is the resistance to respect.
- **Band structure is compressing fast from the bottom.** Bandwidth ((UB−LB)/middle) was **22.0% on 2026‑07‑17**, and is **12.45% today**. The lower band has vaulted from 271.83 to 304.16 in nine sessions because the June crash prints rolled out of the 20-day window. This is a *mean-reversion after shock* signature, not a genuine volatility squeeze — the correct interpretation is that the bands are normalizing, so a break of the middle band (324.35) would be a more meaningful event now than it would have been two weeks ago.
- **ATR 8.06 (2.42% of price)** is slightly *lower* than the 8.74 peak on 2026‑07‑02, despite the violent June range. Volatility is contracting into the current consolidation attempt — consistent with a market digesting a 23.6% rally rather than distributing in panic. That said, the 7/30 session's true range (334.75 → 329.59, plus the 5.09 gap) is larger than ATR, i.e., **an above-normal-range day** in a normally-volatile name.

**Risk-management translation:** a 1.5×ATR stop from 333.43 = **321.3**; a 2×ATR stop = **317.3**. Both sit comfortably below the 10EMA/VWMA cluster but above the 50SMA, making them structurally sensible rather than arbitrary.

---

## 6. Volume & Participation (VWMA + raw volume)

- **VWMA 329.58**, price **1.17% above**. VWMA has risen **eight consecutive sessions** (322.80 on 2026‑07‑24 → 329.58 on 2026‑07‑30) and, critically, jumped from 300.72 (2026‑07‑16) to 310.27 (2026‑07‑17) — large-cap volume migrating upward, which typically marks institutional accumulation rather than retail froth.
- Price above VWMA = the volume-weighted owner base is in profit. That is a support condition. **A daily close below 329.58 would be an early warning of trend fatigue**; note how tightly it coincides with today's low (329.59) and the 10EMA (331.31) → a dense support shelf at **329.5–331.3**.
- **The volume sequence into the top is the warning.** Advance days: 47.5M (7/24), 49.6M (7/27), 51.9M (7/28) — healthy expansion. Then 56.1M (7/29) on a *reversal bar* (opened 339.73, closed 338.19, high 344.57), then **74.8M (7/30) on a −1.41% day**. Volume rising into declining prices over the last two sessions is the classic footprint of **distribution at a high**, and it is the strongest bearish tell in this dataset.
- July's rally days for reference: 75.4M (2026‑07‑02, +4.85% from 294.38 → 308.63), 60.9M (7/15), 63.0M (7/16), 63.4M (7/17). So 74.8M on a down day is at the top of the July volume distribution — a genuinely notable event, not noise.

---

## 7. Actionable Playbook

### Bias
**Constructive medium-term, tactically cautious short-term.** Trend-followers should stay long with tightened stops; fresh capital should wait for either (a) a reclaim of 336–340 that re-expands the MACD histogram, or (b) a controlled pullback into 324–329 that holds.

### Levels (all derived from verified rows / snapshot indicators)
| Level | Value | Significance |
|---|---|---|
| Resistance 1 | **344.5–344.6** | 2026‑07‑29 high 344.57 + Boll upper 344.54 — the confluence to beat |
| Resistance 2 | **340.1** | 2026‑07‑28 closing high (record close in visible window) |
| Pivot / trigger | **338.2** | 2026‑07‑29 close — reclaim puts the uptrend back in control |
| Support 1 | **329.5–331.3** | VWMA 329.58 + today's low 329.59 + 10EMA 331.31 |
| Support 2 | **324.4** | Boll middle (20SMA) |
| Support 3 | **319.35** | 2026‑07‑23 low |
| Trend line | **309.30** | 50SMA — bullish thesis explicitly invalidated below here |
| Deeper | **304.16** | Boll lower band |

### Scenario map
1. **Bull resumption (≈35%):** Reclaim 338.2, then a close above 344.5 on >55M volume. MACD histogram re-expands above 1.5 and RSI pushes back through 70. Add on strength with initial stop 2×ATR below entry. Targets are open-ended above the record high; trail with the 10EMA.
2. **Base/consolidation (≈40%, highest probability):** Price chops in the **324.4–344.5** band for 1–3 weeks, letting the 50SMA (rising ~0.73/day) and the 10EMA catch up. Action: hold core, sell only against 344.5, buy 324–329 with the 10EMA/VWMA shelf as the reference. This is the healthiest resolution.
3. **Trend break (≈25%):** A daily close below **329.58** (VWMA) with MACD histogram flipping negative, then below **324.35** (Boll middle), opens 319.35 and then the 50SMA at 309.30. A close under 309.30 would convert this from "pullback" to "trend damage" and warrant standing aside.

### Concrete triggers to act on
- **De-risk trigger:** MACD line crosses below signal (needs ~0.64 more convergence) **and/or** a close under 331.31 (10EMA).
- **Add trigger:** close > 338.2 with volume > 60M, or a successful retest of 324–329 that closes back above the 10EMA.
- **Stop discipline:** 2×ATR (16.12 points) → **317.3**, which sits ~2.6% under the 50SMA and would survive normal noise. With ATR at 2.42% of price, position size should be scaled so that a 2ATR adverse move costs ≤1% of equity (≈ 41% of a normal-risk unit versus a 1% ATR name — i.e. **size down materially**).

### What would change the read
- RSI re-reaching 70+ *with* an expanding MACD histogram → the divergence thesis fails, upgrade to trend-continuation.
- VWMA rolling over while price stays above it → hidden distribution; treat as an early exit.
- A high-volume close above 344.57 → new leg; abandon all cautionary framing.

---

## 8. Indicator Selection Rationale (8 selected)

| Indicator | Why it earns a slot here |
|---|---|
| **close_10_ema** | The immediate decision line. Price is only 0.64% above it; the trend's short-term health is literally this number. |
| **close_50_sma** | The rising backbone (+0.73/session) and the level that defines thesis invalidation. Non-redundant with the 10EMA given the 7.8% separation. |
| **close_200_sma** | Establishes that this is a *primary* uptrend (+20.1% premium) and quantifies extension risk. Different time horizon, different job. |
| **macd** | Captures the absolute momentum regime and enables crossover tracking; shows the first down-tick after nine up-sessions. |
| **macdh** | The cleanest available evidence of the 81% histogram collapse and the price/momentum divergence. Chosen over `macds` because the histogram encodes both lines' relationship. |
| **rsi** | Independent overbought/oversold and divergence framework; confirmed the 6/25 low at 32.2 and the double-70 failure. Not redundant with MACD (different math, momentum vs. rate-of-change). |
| **atr** | Mandatory here — volatility is contracting after a shock, so stop placement and position sizing must be ATR-anchored (2.42% of price). |
| **vwma** | Only indicator in the set that fuses price with volume. Detects the volume-expansion-into-decline pattern and defines the volume-weighted support shelf at 329.58. |

Deliberately **excluded:** `macds` (derivable from macd/macdh), `boll`/`boll_ub`/`boll_lb` (used as verified context above rather than as a separate slot, since the 20SMA at 324.35 overlaps heavily with the 10EMA/50SMA framing), and `mfi` (would duplicate the volume-plus-momentum work VWMA+RSI already do).

---

## 9. Summary Table

| Dimension | Reading (2026‑07‑30) | Interpretation | Action |
|---|---|---|---|
| **Close** | 333.43 (−1.41%, gap-down) | Two-day reversal off 344.57 record high | Reduce/add only on triggers |
| **Volume** | 74.8M vs ~45–55M norm | Distribution signature into decline | Bearish weight |
| **MA stack** | 10EMA 331.31 > 50SMA 309.30 > 200SMA 277.65 | Perfect bullish order, all rising | Trend intact |
| **Price vs. MAs** | +0.64% / +7.80% / +20.09% | Short-term at the edge, long-term extended | Tighten, don't chase |
| **MACD / signal / hist** | 9.241 / 8.598 / **0.643** | Histogram −81% from 7/17 peak; bearish divergence | Watch for cross under |
| **RSI** | 61.66 (from 71.65 on 7/17) | Lower high vs. higher price high; above 50 | Caution, not exit |
| **Bollinger** | Mid 324.35 · UB 344.54 · LB 304.16 · %B 0.73 | Upper band tagged at 344.57; bandwidth 12.45% from 22.0% | Range 324–344 likely |
| **ATR** | 8.06 (2.42%) | Volatility mildly contracting; 7/30 range above-normal | Stops: 321.3 (1.5×) / 317.3 (2×) |
| **VWMA** | 329.58, price +1.17% above | Rising 8 straight sessions; volume-weighted support | Close below = warning |
| **Key support** | 329.5–331.3 → 324.4 → 319.35 → 309.30 | Layered, well-defined | Buy zone 324–329 |
| **Key resistance** | 338.2 → 340.1 → 344.5 | 344.5 confluence = decisive | Add above 338.2 on volume |
| **Net bias** | Bull trend, decelerating momentum | **Hold with tighter stops; await resolution** | Neutral-to-cautious tactical |