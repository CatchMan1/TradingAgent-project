# AAPL — Technical Analysis Report (as of Friday, 2024-01-19)

## 1. Bottom line

AAPL closed **191.56** on 2024-01-19, up **+1.55%** from 188.63 the prior session and **+4.86%** from the 182.68 close on 2024-01-17. That two-day surge has:

- Reclaimed the **50-day SMA (189.802)** — the first close above it since 2023-12-29.
- Reclaimed the **10-day EMA (186.981)** on 2024-01-18, the first close above it in roughly a month.
- Produced a **bullish MACD crossover** (MACD −1.0257 vs signal −1.2282, histogram **+0.2025** — the first positive histogram reading since December).
- Occurred on **expanding volume** (68.9M on 01-19, 78.0M on 01-18, vs an approximate 20-session average near 53M).

But the *price posture* is still recovery, not breakout: the close remains **−3.31% below the 2023-12-14 close of 198.11**, the MACD line is still **below zero**, and price has run straight into the **192.5–194.8 congestion shelf** from the November/December distribution. The setup is best described as **a constructive trend-reclaim inside a still-unresolved multi-week range**, with favorable short-term momentum but poor immediate reward-to-risk at the current quote.

**Priority action: do not chase 191.56. Buy the first pullback into 188.2–189.8 with a defined stop, or add only on a volume-confirmed close above 194.8.**

---

## 2. Verified price data (source of truth)

From `get_verified_market_snapshot` for 2024-01-19:

| Field | 2024-01-19 | 2024-01-18 | 2024-01-17 |
|---|---|---|---|
| Open | 189.33 | 186.09 | 181.27 |
| High | 191.95 | 189.14 | 182.93 |
| Low | 188.82 | 185.83 | 180.30 |
| Close | **191.56** | 188.63 | 182.68 |
| Volume | 68,903,000 | 78,005,800 | 47,317,400 |

Two details matter here:

1. **Close location in range is very strong.** On 01-19 the close sat at **87.5%** of the day's 3.13-point range; on 01-18 it sat at **84.6%** of that day's 3.31-point range. Back-to-back closes near session highs after a gap-up on 01-18 (open 186.09 vs prior close 182.68) is the signature of demand absorbing supply, not a short-covering blip.
2. **The gap held.** The 01-18 opening gap from 182.68 to 186.09 (≈1.87%) was not filled on either session — the 01-19 low of 188.82 is well above it. Unfilled gaps of this kind act as a defensive shelf at ~182.7–186.1.

*Data-integrity note:* the indicator tool and the verified snapshot agree to the last decimal on every value I use below (e.g., close_200_sma 181.15395 vs 181.153951; MACD −1.025708 in both; RSI 56.95514; ATR 3.339126; VWMA 185.362996). I found **no conflict** between sources. One flag: the snapshot's `mfi` prints **0.415111**, which is a 0–1 scale (≈41.5 on the conventional 0–100 scale) rather than a raw MFI. Reading it as 41.5, money flow is **neutral-to-slightly-negative** and has *not* yet confirmed the price rebound — a caution, not a veto. I did not select MFI as a core indicator because of this unit ambiguity.

---

## 3. Selected indicators (8) and why

| # | Indicator | 2024-01-19 value | Role in this specific context |
|---|---|---|---|
| 1 | close_50_sma | 189.802 | Medium-term trend + the level just reclaimed; distinguishes a real turn from a bounce |
| 2 | close_200_sma | 181.153951 | Strategic trend anchor and confluence with the 180.2–181.2 floor |
| 3 | close_10_ema | 186.981048 | Fast momentum trigger; identified the 01-18 inflection |
| 4 | macd | −1.025708 | Regime line: shows momentum improving but still net-negative |
| 5 | macdh | +0.202537 | Encodes signal-line crossover; earliest momentum-inflection evidence |
| 6 | rsi | 56.95514 | Overbought/oversold + divergence check at the 180 zone |
| 7 | atr | 3.339126 | Stop placement, position sizing, ATR-normalized levels |
| 8 | vwma | 185.362996 | Volume-weighted cost basis; tests whether the rally is volume-backed |

*Monitored but not selected (redundancy control):* `macds` (captured by `macdh`), `boll`/`boll_ub`/`boll_lb` (referenced below as supplementary volatility context from the snapshot), and `mfi` (scale ambiguity noted above). I deliberately avoided stacking RSI with a stochastic-type oscillator, and avoided three MACD variants in the core set.

---

## 4. Trend structure — long-term intact, medium-term repaired

**Long-term (200-day SMA): firmly bullish and still rising.**
The 200SMA climbed every session in the window: 178.225 (12-20) → 179.488 (12-29) → 181.154 (01-19), a gain of ~2.93 points in 20 sessions (~1.5%/month). Price at 191.56 sits **+5.75% above** it. There is no death-cross threat anywhere in this data — the 50SMA has been above the 200SMA throughout, and the gap is currently **8.648 points (50SMA 4.77% above the 200SMA)**.

**Medium-term (50-day SMA): rising, and just reclaimed by price.**
The 50SMA advanced from 184.843 (12-20) to 189.802 (01-19), i.e., ~+0.15/day. Critically, it **never turned down** during the January drawdown — the pullback was a price event, not a trend-structure break. Price closed below it for 12 consecutive sessions (01-02 through 01-18) and closed above it on 01-19 by **+0.93%**. A rising 50SMA under a declining price is precisely how a healthy consolidations-in-uptrend looks, and that condition has now resolved in the bulls' favor on a closing basis.

**Short-term (10-day EMA): inflection confirmed.**
10EMA bottomed at 185.371 (01-17) and has now turned up: 185.964 (01-18) → 186.981 (01-19). Price is **+2.45% above** it. The EMA flattening-to-turning, combined with price above it, is the standard short-term trend-flip confirmation. Note the 10EMA remains *below* the 50SMA (186.98 vs 189.80) — the short-term average is still catching up, so the alignment is not yet fully bullish (price > 10EMA > 50SMA > 200SMA would be ideal). That full stack-up requires 10EMA above 189.80, roughly a week of sideways-to-higher action.

**Trend verdict:** strategic uptrend intact and confirmed (price > 200SMA, 50 > 200, both rising). Medium-term damaged but repaired at the 50SMA. Short-term bullish reversal in progress but not yet structurally complete.

---

## 5. Momentum — bullish crossover, still in negative territory

**MACD (12/26/9):**
- MACD line peak: **3.227** (12-20) → trough **−1.926** (01-17) → **−1.026** (01-19).
- Signal line: 3.493 (12-20) → −1.279 (01-18) → −1.228 (01-19) — the signal line has now *stopped falling and ticked up*, which is the mechanical signature of a crossover.
- Histogram: −0.265 (12-20) → trough **−2.045** (01-05) → −0.283 (01-18) → **+0.203** (01-19).

Three readings of this:

1. **The histogram has been improving for nine straight sessions** (from −2.045 on 01-05), well before the price breakout. That is the *leading* part of the signal and it was visible while price was still making lows near 180.3.
2. **The crossover is above the histogram's extreme but below the zero line.** A bullish MACD cross that occurs while MACD < 0 is a "recovery cross," historically less reliable than one above zero. It needs price confirmation — which it is now getting via the 50SMA reclaim and volume.
3. **The size of the move is notable but not extreme.** The MACD line gained 0.90 points in two sessions (from −1.926 to −1.026). To reach zero, MACD needs roughly another +1.03, which given the current rate of change is a matter of days — but that also means the *fastest* part of the momentum impulse may be behind us.

**RSI (14): neutral, with room, and a mild positive divergence at the low.**
- 12-20: 58.18 → 01-05 low: **28.79** (briefly oversold) → 01-17: **36.71** → 01-18: **51.59** → 01-19: **56.96**.
- The divergence: price's second test of the ~180 zone on 01-17 (low **180.30**) was marginally *higher* than the 01-05 low (**180.17**), while RSI made a decisively **higher low (36.71 vs 28.79)**. That is a textbook momentum non-confirmation of the downtrend at a defined support level, and it preceded the current rally.
- At 56.96, RSI is comfortably below 70 — **no overbought constraint**, so there is room for further upside without a momentum ceiling. Equally, it is not yet in the 60–70 "strong trend" band, so it does not corroborate a breakout; it corroborates *recovery*.
- Caveat: a 20-point two-session RSI jump is partly a mechanical artifact of Wilder smoothing against a sharp reversal. Treat the *divergence* as the signal, not the level jump.

---

## 6. Volatility — ATR rising, but the Bollinger squeeze is the story

**ATR: 3.339 (1.74% of price).** Up from 2.575 (12-29) and 2.937 (01-12) — volatility expanded during the January decline and **has not contracted** despite the rally. The last two sessions' true ranges (01-18: 3.31; 01-19: 3.13) are right at ATR, so this is "normal" current volatility, not a spike. Practical implications:
- 1×ATR = 3.34; 1.5×ATR = 5.01; 2×ATR = 6.68.
- Stops tighter than ~1 ATR (i.e., under 188.2) sit inside normal daily noise and will likely be harvested.
- Position size should be scaled off 3.34, not off December's ~2.6. Using the old ATR would oversize positions by ~28%.

**Bollinger context (supplementary, from the verified snapshot):**
- Middle (20SMA) = **188.165**; Upper = **197.535**; Lower = **178.795**.
- Band width has **contracted ~12.8%** since 01-08 (21.50 points then vs 18.74 now), even as ATR rose slightly. Bands narrowing while ATR holds is a *compression* pattern — the market is coiling.
- **%B = 0.68**: price is in the upper-middle third of the envelope, above the basis (188.165) but ~3.0% below the upper band (197.535). It is neither stretched nor capped.
- The close at 191.56 is **+1.80% above the middle band** — confirming the mean has been reclaimed. In a squeeze, the middle band often acts as the pivot between regimes; holding above it keeps the odds tilted upward.

**Volatility verdict:** rising realized volatility + contracting bands = a pending resolution. Direction is being decided by whether price can clear 194.8–197.5 on volume; failure to do so keeps the risk of a return to the band floor (~178.8–181.2) live.

---

## 7. Volume participation — the most important improvement in this dataset

**VWMA (185.363) is now below price.** That is a meaningful change: it means the **volume-weighted average transaction price over the period (185.36) is under the current quote (191.56)** — recent buying occurred above the crowd's average cost basis. Price is **+3.34% above VWMA**. Equally important, VWMA **stopped falling**: 195.363 (12-29) → 185.451 (01-17) → 185.253 (01-18) → **185.363 (01-19)** — the first uptick in three weeks.

**Volume comparison (approximate 20-session average ≈ 53.2M):**

| Session | Direction | Volume | vs ~20d avg |
|---|---|---|---|
| 2024-01-02 | down (−3.58%) | 82,488,700 | ~1.55× |
| 2024-01-04 | down | 71,983,600 | ~1.35× |
| 2024-01-16 | down | 65,603,000 | ~1.23× |
| **2024-01-18** | **up** | **78,005,800** | **~1.47×** |
| **2024-01-19** | **up** | **68,903,000** | **~1.30×** |

The honest read: **distribution was real** (01-02, 01-04, 01-16 all sold on above-average volume), **and so is the current accumulation** (01-18, 01-19 bought on above-average volume). This is a genuine volume-backed reversal attempt, not a drift. But note the caveat: this is a **two-session sample**, and combined 01-18/01-19 volume (146.9M) is still smaller than the single 2023-12-15 session (128.5M at the December top). One more high-volume up day above 192.5 would convert this from "attempt" to "confirmed."

**Divergence to respect:** VWMA (185.36) sits *below* the 50SMA (189.80). The volume-weighted cost basis is still beneath the simple average, meaning a large amount of supply was transacted lower in this range. If price loses 185.36, the volume picture flips back to distributive.

---

## 8. Key levels (all drawn from tool output with dates)

**Resistance (overhead supply):**
| Level | Source | Distance from 191.56 |
|---|---|---|
| 191.95 | 2024-01-19 high (immediate) | +0.20% |
| 192.53 | 2023-12-29 close | +0.51% |
| 193.15–193.58 | 2023-12-27 / 12-28 closes | +0.83% / +1.05% |
| 194.68–194.83 | 2023-12-21 / 12-20 closes | +1.63% / +1.71% |
| 196.95 | 2023-12-19 high | +2.81% |
| 197.535 | Bollinger upper band | +3.12% |
| 198.11 / 199.62 | 2023-12-14 close / high | +3.42% / +4.21% |

The **192.5–194.8 band** is the critical gate: it is where November's congestion (11-21 close 190.64, 11-22 close 191.31, 12-05 close 193.42) and December's failed-top distribution overlap. This is the most likely place for the rally to stall.

**Support (structural):**
| Level | Source | Distance from 191.56 |
|---|---|---|
| 189.802 | 50-day SMA | −0.92% |
| 188.82 | 2024-01-19 low | −1.43% |
| 188.165 | Bollinger middle (20SMA) | −1.77% |
| 186.981 | 10-day EMA | −2.39% |
| 185.363 | VWMA | −3.23% |
| 182.68–186.09 | 01-17 close to 01-18 open (unfilled gap) | −4.6% to −2.9% |
| 180.17–181.15 | 01-05 low 180.17, 01-17 low 180.30, 200SMA 181.154 | −5.9% to −5.4% |
| 178.795 | Bollinger lower band | −6.66% |

The **180.17–181.15 confluence** (two tests of ~180.2 bracketing the rising 200SMA, with a higher RSI low on the second test) is the line in the sand. A close below it would invalidate the entire bullish reconstruction and reopen the October 2023 gap region.

---

## 9. Trade plan — specific, actionable, sized to ATR

**The core problem: reward-to-risk at 191.56 is poor.** With a technically sound stop below the VWMA/10EMA cluster (~185.0), risk is 6.56 points, while the first meaningful target (194.8) is only 3.24 points away.

| Entry | Stop | Risk | T1 194.8 | R/R | T2 197.5 | R/R | T3 199.6 | R/R |
|---|---|---|---|---|---|---|---|---|
| 191.56 (chase) | 185.00 | 6.56 | +3.24 | **0.49:1** | +5.97 | **0.91:1** | +8.06 | **1.23:1** |
| 188.50 (Boll mid / 50SMA zone) | 185.00 | 3.50 | +6.30 | **1.80:1** | +9.03 | **2.58:1** | +11.12 | **3.18:1** |
| 188.50 | 186.90 (below 10EMA) | 1.60 | +6.30 | **3.94:1** | +9.03 | 5.64:1 | +11.12 | 6.95:1 |

**Primary plan (preferred):**
- **Zone to buy:** 188.20–189.80 — the overlap of the Bollinger middle (188.165), the 50SMA (189.802), and the 01-19 low (188.82). Note these three levels are stacked within 1.6 points, which is a genuinely tight, well-defined demand shelf.
- **Stop:** daily close below **185.00** (under VWMA 185.363 and the 10EMA 186.981). That is ~1.9 ATR from the 191.56 close and ~2.6 ATR from a 188.5 entry.
- **How to enter:** scale in — 50% at 189.5, 50% at 188.3. If price never pulls back, do not force it.
- **Position sizing:** risk no more than 1% of equity per unit of 3.34-point ATR. Concretely, shares = (0.01 × equity) ÷ 3.50 for the 188.50-entry/185.00-stop version. Example: $100,000 account → $1,000 risk → ~285 shares (≈$53,700 notional). Cap notional at whatever your leverage policy permits; at 1.74% daily ATR, AAPL is not a low-volatility position.

**Secondary plan (breakout):**
- Trigger on a **daily close above 194.83** (the 12-20 close) with volume ≥ 70M, i.e., above the 20-session average. Stop: below 191.50 (the 01-19 high/close area), risk 3.3 = 1 ATR. Target 197.5, then 199.6.
- Rationale for requiring volume: the December 13–15 advance (closes 197.96, 198.11, 197.57) carried 70.4M/66.8M/128.5M and still failed. A breakout on sub-average volume has a high probability of repeating that failure.

**What not to do:** do not buy at 191.56 with a stop under 188.8. That is a 0.8-ATR stop inside the day's normal noise — a coin flip on a random 2-point pullback.

**For existing holders:** hold the core. The 200SMA trend, 50>200 structure, 50SMA reclaim, MACD cross, and volume expansion all support staying long. Consider trimming 20–33% into 194.5–197.5 if you are carrying size, and re-adding in the 188–190 zone. Re-evaluate the whole thesis on any close below 185.0.

---

## 10. Scenario matrix and what would change my mind

| Scenario | Probability weighting | Trigger / evidence to watch | Playbook |
|---|---|---|---|
| **Pullback-and-hold (base case)** | Highest | Price retraces into 188.2–189.8, holds on declining volume, 10EMA stays above 186 | Buy the zone; stop 185; targets 194.8/197.5 |
| **Direct breakout** | Moderate | Daily close > 194.83 on volume ≥ 70M; MACD line crosses zero; %B > 0.85 | Add on breakout, stop 191.0–191.5 |
| **Failure / range re-entry** | Moderate | Rejection at 192.5–194.8, close back below 50SMA (189.80), then below VWMA (185.36) | Stand aside; re-buy only at 181 or on a fresh 50SMA reclaim |
| **Trend break** | Low but high-cost | Close below 180.17–181.15 (01-05 low / 01-17 low / 200SMA) | Exit longs; the MACD recovery cross and RSI divergence are void |

**Specific confirmation triggers I'd want before increasing exposure:**
1. A **third consecutive close above 189.80** (proves the 50SMA reclaim isn't a one-day head fake).
2. **10EMA crossing above 50SMA** (currently 186.98 vs 189.80 — roughly 5–8 sessions away at current slopes).
3. **MACD line crossing above zero** (needs +1.03 from −1.026).
4. **RSI sustaining 55–65** without spiking past 70 — trend strength, not exhaustion.

**What would invalidate the bullish read quickly:**
- A volume-heavy reversal day that closes below 188.17 (Bollinger mid) — that would put price back under the mean and re-open 185.4/181.2.
- A MACD histogram roll-over back below zero within 3–5 sessions (the histogram is only +0.20; it would take very little selling to flip it). This is the single most fragile part of the setup.

---

## 11. Nuance and honest limitations

- **This is a two-day reversal.** Two strong closes and two above-average up-volume sessions do not establish a trend. The 12/14 close of 198.11 has not been retested, and price is still lower-highs on the daily sequence (194.83 on 12-20, 192.53 on 12-29, 191.95 intraday on 01-19) until 192.53 is cleared on a closing basis.
- **No claim of historical validation.** I have not run a backtest of MACD-below-zero crosses or Bollinger squeezes for this instrument, and I am not asserting that these setups "worked" historically. Everything above is a description of current tool output plus mechanical level arithmetic.
- **Support/resistance levels are derived from actual closes/lows/highs printed in the tool data on the stated dates**, not from subjective chart drawing. Where I refer to a "congestion shelf," it is because multiple closes from distinct dates cluster there (e.g., 194.68 on 12-21 and 194.83 on 12-20).
- **The 20-session volume average (~53.2M) is my own arithmetic** on the tool's OHLCV rows for 2023-12-20 through 2024-01-19, not a tool-provided field. It is labeled approximate for that reason.
- **MFI scale discrepancy flagged** (0.415111, i.e., 41.5 on a 0–100 convention) and excluded from the core signal set rather than silently rescaled.
- **Bollinger values are used as supplementary context** from the verified snapshot; only 8 indicators are formally "selected," and the Bollinger family was intentionally left out of that eight to avoid diluting focus given ATR already covers volatility and the 50SMA covers the mean.

---

## 12. Summary table

| Dimension | Reading (2024-01-19) | Interpretation | Actionable level / signal |
|---|---|---|---|
| **Close / OHLCV** | 191.56; H 191.95; L 188.82; V 68.9M | Strong close at 87.5% of range; second straight; unfilled gap 182.68→186.09 | Gap is support at 182.7–186.1 |
| **50-day SMA** | 189.802 (rising from 184.843 on 12-20) | Reclaimed on 01-19, first time since 12-29; price +0.93% above | Hold above = bullish; lose = caution |
| **200-day SMA** | 181.153951 (rising from 178.225 on 12-20) | Strategic uptrend intact; price +5.75% above | Floor confluence at 180.17–181.15 |
| **10-day EMA** | 186.981048 (turning up from 185.371 on 01-17) | Reclaimed 01-18; price +2.45% above; still < 50SMA | Full stack-up needs 10EMA > 189.80 |
| **MACD** | −1.025708 (crossed above signal −1.228245) | Bullish crossover but **below zero** — recovery cross | Needs >0 to be trend-confirming |
| **MACD histogram** | +0.202537 (from −2.045 on 01-05) | 9 sessions of improvement; first positive print | Roll-over <0 soon = setup fails |
| **RSI** | 56.95514 (28.79 on 01-05 → 36.71 on 01-17) | Positive divergence at 180; not overbought; room to run | 55–65 healthy; >70 = exhaustion |
| **ATR** | 3.339126 (1.74% of price) | Elevated and rising; 2.575 on 12-29 | Stops ≥1.5 ATR; 1A=3.34, 2A=6.68 |
| **VWMA** | 185.362996 (first uptick since 12-29) | Price +3.34% above volume-weighted cost; buying is volume-backed | Losing 185.36 flips to distributive |
| **Volume vs ~20d avg (53.2M)** | 01-18: 78.0M (1.47×); 01-19: 68.9M (1.30×) | Real accumulation, but only a 2-session sample | Need 1 more >70M up day |
| **Bollinger (supplementary)** | Mid 188.165; UB 197.535; LB 178.795; %B 0.68 | Above mean; bands −12.8% since 01-08 = squeeze | Resolve via 194.8 up or 181 down |
| **Resistance** | 192.53 / 194.68–194.83 / 197.535 / 199.62 | 192.5–194.8 is the November/December supply gate | Close >194.83 on volume = breakout |
| **Support** | 189.802 / 188.82 / 188.165 / 186.981 / 185.363 / 181.15 / 180.17 | 188.2–189.8 is a 1.6-pt confluence shelf | Buy zone 188.2–189.8 |
| **Structure verdict** | Uptrend intact, medium-term repaired, short-term reversing | Recovery inside unresolved range; not yet a breakout | — |
| **Recommended posture** | **Don't chase 191.56. Buy 188.2–189.8, stop 185.0, targets 194.8 / 197.5** | Entry at 188.5 gives 1.8:1 to 3.2:1 vs 0.5:1–1.2:1 at 191.56 | Breakout add only >194.83 on ≥70M |
| **Invalidation** | Close below 180.17–181.15 (with MACD histogram back <0) | Bullish reconstruction void | Exit longs |