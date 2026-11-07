# AMZN — Multi-Timeframe Technical Report
**As of the close of 2026-08-24 | Last price: $262.07**

---

## 1. Data integrity check (read this first)

The verified snapshot is internally consistent with the individual indicator pulls — every value I cite matches to the last decimal:

| Field | Snapshot value | Indicator tool | Match |
|---|---|---|---|
| close_50_sma | 250.14 | 250.1399996948242 | ✅ |
| close_200_sma | 238.38975 | 238.3897499847412 | ✅ |
| close_10_ema | 262.626115 | 262.6261147274536 | ✅ |
| macd / macds / macdh | 3.159032 / 4.630797 / −1.471765 | 3.159032 / 4.630797 / (derived −1.4718) | ✅ |
| rsi | 52.484976 | 52.48497614400838 | ✅ |
| boll / ub / lb | 262.912499 / 293.804193 / 232.020805 | 262.91249923706056 | ✅ |
| atr | 7.282371 | 7.282370565470431 | ✅ |
| vwma | 267.411578 | 267.4115779690638 | ✅ |

**One flag:** the snapshot's `mfi` field reads **0.285378**, which is outside the 0–100 scale a Money Flow Index must occupy. I treat that field as corrupt and did **not** use it. All conclusions below rest on the OK rows above.

**Indicators selected (8 slots, MACD counted as one family):** `close_200_sma`, `close_50_sma`, `close_10_ema`, `macd`+`macds` (used jointly to verify crossovers), `rsi`, `boll` (with upper/lower bands from the snapshot), `atr`, `vwma`.
*Why this set:* AMZN is in a **post-catalyst regime** — a violent gap followed by orderly drift — so I need (a) two slow trend anchors to judge whether the trend survived the gap, (b) one fast anchor to time entries, (c) momentum to gauge whether the pullback is exhaustion or reversal, (d) band/volatility data because post-gap band geometry is distorted and directly relevant to sizing, and (e) a volume-weighted price because the gap was transacted on enormous volume, making the *dollar-weighted* cost basis far more informative than a simple average here. I deliberately avoided stacking redundant momentum oscillators (no second RSI-family or stochastic) and avoided using three near-identical short averages.

---

## 2. What actually happened: the regime-defining event

The series from 2025-12-01 to 2026-08-24 (183 rows) contains a decisive structural break that dominates every indicator reading today:

- **2026-07-30:** close **235.50**, volume 101.8M, high 239.82.
- **2026-07-31:** open **265.00**, close **271.58**, high 273.23, volume **129.1M** — a gap of **+$29.50 (+12.5%)** from the prior close, on the largest volume in the visible window.
- **2026-08-03:** close **284.02**, intraday high **287.20** (the highest high in the entire retrieved dataset), volume 90.8M.
- Then a **controlled 13-session bleed**: 284.02 (08-03) → **258.63** (08-21) = **−$25.39, or −8.94%**.
- **2026-08-24:** close **262.07**, up +$3.44 (+1.33%) from 258.63, closing in the upper part of the day's 259.05–263.32 range on **28.07M** shares.

So the current question is *not* "is AMZN bullish?" — the tape already answered that in late July. The question is: **is the −8.9% drift a healthy post-gap digestion, or the early stage of a failed breakout?**

Note also two earlier high-volume dislocations with the same signature: **2026-02-05/02-06** (103.5M then 179.2M shares; close 232.99 → 210.32, and a slide to 198.79 by 02-13) and **2026-06-26** (248.4M shares, an outlier that marked a low at 227.01 two sessions earlier). Large single-day volume expansions in this name have repeatedly coincided with scheduled corporate catalysts. I am *not* asserting a causal claim about the 07-31 event — only that its volume/price signature is that of an information shock, and that such gaps typically require weeks of repair before trend continuation.

---

## 3. Trend structure: bullish in layers, corrective in the last leg

**Long-term (200-day SMA) — bullish and rising.**
200-SMA at **238.39**, up from 235.01 on 07-31 and from 234.66 on 07-28. It bottomed in the 2026-07-28/29 area (234.66/234.66) and has curled higher. Price sits **+$23.68 (+9.93%)** above it. That is a wide-but-not-extreme premium — historically the kind of cushion that absorbs a pullback without breaking the primary trend.

**Medium-term (50-day SMA) — bullish, and newly re-accelerating.**
50-SMA at **250.14**, up from a trough of **246.38 on 07-30** — i.e., the 50-day has turned up *after* the gap, which is the single most constructive medium-term read on this chart. Price is **+$11.93 (+4.77%)** above it. The 50/200 spread is **+$11.75** and widening modestly (it was +$11.63 on 07-30).

*Cross chronology (all from tool output):* the 50-SMA was **above** the 200-SMA on 2026-02-25 (227.21 vs 224.27), crossed **below** on **2026-03-11** (224.25 vs 224.64 — a death cross), stayed below through the spring (e.g., 2026-04-07: 214.06 vs 224.55), and crossed back **above** on **2026-05-06** (228.73 vs 228.08 — a golden cross). The golden-cross configuration has now held for roughly 3.5 months. That is a structural tailwind, but it is a *slow* signal and says nothing about the next two weeks.

**Short-term (10-day EMA) — bearish/rolling over.**
10-EMA at **262.63**, essentially *at* the close (262.07, i.e. price is −$0.56 / −0.21% below it). The important detail is the shape: the 10-EMA ran from 236.29 (07-30) to a peak of **267.18 on 08-12**, then flattened 266.05 → 265.19 → 264.15 → 264.46 → 263.67 → 262.75 → **262.63**. It has been declining for eight straight sessions. Price closed below it on 08-17 (261.31 vs 265.19), reclaimed it briefly on 08-19 (265.84 vs 264.46), and lost it again on 08-20/21. **This is a short-term downtrend embedded in a medium-term uptrend** — the classic "flag inside a trend" geometry.

**Net trend verdict:** primary and intermediate trends up; short-term trend down but decelerating. The price is now pinned between the 10-EMA (262.63, overhead magnet) and the 50-SMA (250.14, deep support) — with the 20-period Bollinger midpoint (262.91) sitting in almost exactly the same place as the 10-EMA. **262.6–262.9 is the pivot zone of the entire chart right now.**

---

## 4. Momentum: a textbook post-spike decay, not (yet) a reversal

**MACD — bearish crossover confirmed, but above zero.**
The MACD line exploded from −3.75 (07-29) to **+8.43 (08-11)**, then decayed monotonically to **+3.16 (08-24)**. The signal line peaked at **6.22 on 08-14** and is at **4.63**. Cross-checking the spread:

- 08-13: 7.372 − 6.119 = **+1.253**
- 08-14: 6.609 − 6.217 = **+0.392**
- 08-17: 5.830 − 6.140 = **−0.310** ← bearish crossover here

So a **bearish MACD crossover occurred on 2026-08-17**, and the histogram has been negative and expanding for six sessions to **−1.472** today.

**The nuance that matters:** the MACD line is still **+3.16, comfortably above zero**. In the June drawdown the same indicator went to −6.88 (06-25) — deeply negative. Today's configuration (positive but decelerating) is the signature of a *momentum reset inside an uptrend*, not of a distribution top. The bearish cross is a legitimate tactical warning — the last two bearish-cross-then-negative episodes (June, and 07-23 through 07-29) both preceded further downside — but the zero-line position argues against treating it as a trend-change signal. **Watch the MACD line at zero: a break below 0 would convert this from "digestion" to "failed breakout."**

**RSI — dead neutral, with room in both directions.**
RSI is **52.48**. The path: 33.31 (07-29) → **72.23 (08-03, the post-gap peak, briefly overbought)** → steady bleed → **49.74 (08-21)** → 52.48 (08-24). Two observations:
1. The RSI low of **49.74 on 08-21** never reached oversold. In a genuinely weak tape you would expect a flush into the 30s, as happened on 06-10 (32.46), 06-25 (33.63) and 07-29 (33.31). The absence of that flush is a mildly bullish tell.
2. RSI at 52.5 is the definition of no-man's-land. It is **not** a setup in itself; it is a permission slip for either scenario. It does mean that a fresh long is not chasing an overbought reading, and that a short is not selling into oversold.

**Momentum synthesis:** the 08-03 RSI peak at 72.23 alongside the price peak at 284.02 shows the two topped *together* — no bearish divergence was generated at the high. Divergence tops are the ones that usually precede durable reversals; this one looks like ordinary mean-reversion of an overbought thrust.

---

## 5. Volatility: the bands are still blown out — and that is the key tactical fact

**ATR = 7.28**, or **2.78% of the $262.07 close**.

The ATR path is instructive: it compressed to **6.89 on 07-29** (pre-gap), spiked to **9.98 on 08-05** (post-gap peak), and has contracted for **15 of the last 19 sessions** down to 7.28. Volatility is normalizing but is **still ~5.7% above the pre-gap baseline**. Practical translation: the market is calmer than it was two weeks ago, but not yet back to its July rhythm. Position sizes should still be trimmed relative to a pre-catalyst book.

**Bollinger (20,2):** middle **262.91**, upper **293.80**, lower **232.02**.
Read the geometry carefully, because it drives a specific conclusion:

- Implied standard deviation = (293.80 − 262.91) / 2 ≈ **$15.45/share** — extraordinarily wide.
- Total band width ≈ **$61.78**, or **23.5% of the midpoint**.
- **%B = (262.07 − 232.02) / 61.78 ≈ 0.49** — dead center of the bands.

The bands are wide because the 20-day window is still dominated by the 235→284 swing. **Consequence: the upper and lower bands are functionally useless as near-term signals.** A touch of the 293.80 upper band would require a +12.1% move; the 232.02 lower band is −11.5% away. Neither is a realistic tactical trigger. What the bands *do* tell you is that **the 20-period mean (262.91) has caught up to price** — price closed 262.07, just −$0.84 (−0.32%) beneath it. After a post-gap glide lower, price rejoining a rising-before-it 20-mean is a mean-reversion completion, not a breakdown. In the sessions ahead, expect **band-width contraction** as the gap rolls out of the lookback — a squeeze regime, which favors range tactics over breakout tactics.

---

## 6. Volume: the most underrated evidence in this chart

**VWMA = 267.41.** Price is **−$5.34 (−2.0%)** below the volume-weighted average price of the recent window.

This is the single most cautionary number in the report. Because 07-31 (129.1M) and 08-03 (90.8M) were transacted at 265–284, the **dollar-weighted cost basis of recent participants sits above spot**. Anyone who bought the gap is underwater. The gap between VWMA (267.41) and the 50-SMA (250.14) — **$17.27** — quantifies how much more "expensive" the volume-weighted holder is than the time-weighted one. That overhead supply is exactly what capped the 08-19 rally at a 266.40 high (close 265.84), a rejection just beneath the VWMA.

**But the volume behavior during the pullback is genuinely constructive.** Rolling my own sums from the verified CSV:
- 21-session average (2026-07-27 → 2026-08-24) ≈ **47.0M** shares.
- Last 10 sessions (2026-08-11 → 2026-08-24) ≈ **32.6M** shares.
- 2026-08-24 volume: **28.07M** — roughly **60% of the 21-session average**.

Declining price on **contracting** volume is supply exhaustion, not distribution. Institutions distribute into strength on heavy volume; they do not bleed a stock lower on 60% of average participation. Meanwhile the two up-attempts that failed (08-17, 43.9M; 08-19, 35.8M) did so on *rising* volume — so there are real sellers at 265–272, but they are not aggressively pressing.

**Volume verdict:** overhead supply confirmed at 265.8–272.3 (VWMA zone), but the pullback lacks the volume signature of a top. Net: **range-bound with an upward bias once the supply is absorbed.**

---

## 7. Levels that matter (all drawn from verified rows)

**Resistance (ascending):**
| Level | Source | Why it matters |
|---|---|---|
| **262.63 / 262.91** | 10-EMA / Bollinger mid (20-SMA) | Immediate pivot; price is 0.2–0.3% below. Reclaim = momentum repair. |
| **265.84 / 266.40** | 08-19 close / 08-19 high | Proven rejection point; also ~VWMA (267.41) approaches here |
| **267.41** | VWMA | Volume-weighted breakeven of the gap buyers |
| **272.27 / 273.23** | 08-11 close / 07-31 high | Bottom edge of the post-gap distribution shelf |
| **278.09 / 278.84** | 08-10 close / 08-11 high | Prior swing high |
| **284.02 / 287.20** | 08-03 close / 08-03 intraday high | Top of the structure = highest high in the dataset |

**Support (descending):**
| Level | Source | Why it matters |
|---|---|---|
| **258.63 / 257.04** | 08-21 close / 08-21 low | The pullback low — first must-hold |
| **254.96** | 07-15 close | Pre-gap swing high, now flipped to support |
| **250.14** | 50-SMA (rising) | Primary trend support; confluence with the 250–251 congestion of early July |
| **239.82 → 262.01** | 07-30 high → 07-31 open | **Unfilled earnings gap.** Its *upper* edge (262.01) is essentially today's price! |
| **238.39** | 200-SMA (rising) | Bull-market line in the sand |

**A crucial structural detail:** the 2026-07-31 gap (239.82 → 262.01) is **still unfilled**, and its *top boundary sits at 262.01* — one cent below today's 262.07 close. AMZN closed on 08-24 precisely at the roof of the unfilled gap. That is a genuine technical knife-edge: holding it keeps the gap as support; losing it turns 262.01 into the neckline of a partial gap-fill toward 250 (50-SMA) and, in the tail scenario, 239.82.

---

## 8. Scenarios and actionable playbook

### Scenario A — Bullish resolution (primary, ~50% weight)
**Trigger:** a daily close **above 262.91** (Bollinger mid/20-SMA) confirmed by a close **above 266.40**, ideally on volume > 45M (above the 10-session average of ~32.6M).
**Logic:** price reclaims the 10-EMA and 20-SMA simultaneously, MACD histogram stops expanding negative, RSI pushes back through 55–57.
**Path:** 272.27 → 278.09 → retest of 284.02.
**Execution:** buy the close-above-266.40 confirmation rather than anticipating it — the 08-19 failure at 266.40 is a fresh memory and a first-touch fade is the higher-probability outcome. Add on a *second* close above 267.41 (VWMA).
**Stop:** below **257.00** (beneath the 08-21 low). That's ~$9.40 of risk, or **1.3× ATR** — appropriately tight for a momentum entry.

### Scenario B — Continued digestion / range (highest near-term probability, ~35% weight)
**Setup:** price chops between **257.04 and 266.40** while the Bollinger width contracts and the gap rolls out of the 20-day window.
**Logic:** VWMA overhead supply at 267.41 caps rallies; light-volume pullbacks find buyers at 257–259; ATR keeps contracting from 7.28.
**Execution:** trade the range — buy 258–259.5 with a stop under 256.5, sell 265–266.4. Do **not** hold for a breakout without volume confirmation. Given ATR 7.28, a 2-ATR stop (~$14.60) is too wide for a range trade; use the structural 256.50 stop (~$1.00–2.50 of risk on entries near 258) and size accordingly.

### Scenario C — Breakdown (tail, ~15% weight)
**Trigger:** daily close **below 257.04** with expanding volume (> 45M), then a failure to reclaim 262.01.
**Logic:** the unfilled gap's upper edge fails; the 08-17 bearish MACD cross extends with the MACD line crossing below zero; VWMA-over-price confirms distribution.
**Targets:** **250.14** (50-SMA) first, then **239.82** (gap floor).
**Execution:** for a short, entry on the 257.04 break-retest, stop above **262.00** (~$5 risk ≈ 0.7 ATR), first target 250.14 (≈$7 reward → ~1.4:1), scale at 245.
**Note:** a break of the *rising* 50-SMA at 250.14 would be the first credible challenge to the May 06 golden-cross regime and would shift me to a neutral/negative structural stance.

### Risk management, explicitly
- **ATR 7.28 = 2.78% of price.** For a $100k book risking 1% ($1,000) per position with a 1.5-ATR stop (~$10.92), size ≈ **91 shares (~$23.9k notional)**. With a 2-ATR stop (~$14.56), size ≈ **68 shares (~$17.8k)**. Given the still-elevated (vs pre-gap 6.89) ATR, use the wider multiple and the smaller size.
- **Do not use Bollinger bands as stops here** — they are 11–12% away on both sides. Use ATR and the structural levels in §7.
- **Event risk is asymmetric and unscheduled from my data:** the 129M-share 07-31 bar proves a single session can move this name ±12%. Any position held through a probable catalyst date should be sized at half normal.

---

## 9. What would change my mind

**To more bullish:** a close above 267.41 (VWMA) recaptures the volume-weighted breakeven and would effectively release the overhead supply from the gap chase; MACD histogram turning positive again while the MACD line stays above zero; a higher low above 262.01.

**To more bearish:** MACD line crossing **below zero** (currently +3.16 — this is the cleanest single tell); a close below 257.04; the 50-SMA flattening *and* price losing 262.01 on heavy volume; RSI breaking below ~45 without a price low. Also watch the **50/200 spread** (currently +11.75): a narrowing back toward zero would signal the May golden cross is losing authority.

**To neutral:** continued ATR contraction below ~6.90 and 10-session volume staying under 33M with price locked in 257–266. That is a coil, and it will resolve — but the resolution is not predictable from this dataset, so waiting for it is a legitimate strategy.

---

## 10. Summary table

| Dimension | Reading (2026-08-24) | Interpretation | Actionable implication |
|---|---|---|---|
| **Close** | 262.07 (open 259.60, H 263.32, L 259.05) | +1.33% off the 258.63 low, closed near day's high | Short-term stabilization candle |
| **200-SMA** | 238.39, rising | Price +9.93% above | Primary uptrend intact |
| **50-SMA** | 250.14, rising off 246.38 (07-30) | Price +4.77% above; 50>200 by 11.75 | Intermediate uptrend intact; golden cross since 2026-05-06 |
| **10-EMA** | 262.63, falling 8 sessions from 267.18 (08-12) | Price −0.21% below | Short-term downtrend; the immediate battleground |
| **Bollinger (20,2)** | Mid 262.91 / UB 293.80 / LB 232.02; %B ≈ 0.49 | SD ≈ $15.45, width ≈ 23.5% of mid | Bands unusable tactically; expect squeeze; 262.91 is the pivot |
| **MACD / Signal / Hist** | 3.159 / 4.631 / **−1.472** | Bearish cross on **2026-08-17**, hist expanding negative — but line still >0 | Tactical caution, not trend change; zero line is the tell |
| **RSI** | 52.48 (peak 72.23 on 08-03, low 49.74 on 08-21) | Neutral; pullback never reached oversold | Neither chasing nor capitulating; room both ways |
| **ATR** | 7.28 = 2.78% of price; down from 9.98 (08-05) | Volatility contracting but 5.7% above pre-gap 6.89 | Use ~1.5–2 ATR stops; reduce size vs pre-catalyst |
| **VWMA** | 267.41 | Price **−2.0% below** it; +$17.27 above 50-SMA | Overhead supply at 265.8–272.3; bearish near-term overhang |
| **Volume** | 28.07M vs 32.6M (10-sess avg) vs 47.0M (21-sess avg) | Pullback on ~60% of average volume | Supply exhaustion, not distribution — mildly bullish |
| **Unfilled gap** | 07-31 gap: 239.82 → 262.01 | Today's close (262.07) sits **on the gap roof** | Decisive line: hold = support; lose = target 250.14, then 239.82 |
| **Key resistance** | 262.91 → 265.84/266.40 → 267.41 → 272.27 → 278.09 → 284.02/287.20 | Ladder of proved rejections | Buy confirmation above 266.40, not anticipation |
| **Key support** | 258.63/257.04 → 254.96 → 250.14 → 239.82/238.39 | Layered, with 50-SMA as the structural one | Short invalidation below 257.04 |
| **Bias** | Constructive medium-term, neutral-to-slightly-heavy short-term | Post-gap digestion with a bull skeleton | Range tactics (257–266.4) until a volume-confirmed break |
| **Asymmetry** | ~50% bullish / ~35% range / ~15% bearish | Reward-to-risk favors waiting for confirmation | Risk 1% at ~91 sh (1.5 ATR) or ~68 sh (2 ATR) per $100k |

**Bottom line for AMZN:** the July 31 +12.5% gap on 129M shares reset this chart's center of gravity upward, and the fact that both the 50-SMA (250.14) and 200-SMA (238.39) are *rising* beneath a price that sits ~5–10% above them is not what a broken chart looks like. What is missing is fresh demand: the MACD's 08-17 bearish cross, a falling 10-EMA, and a VWMA (267.41) above spot all say the gap buyers are still nursing losses. AMZN closed on 08-24 exactly at the roof of its unfilled gap (262.01) — the single most informative line on the page. Hold it on volume above ~45M and the path to 272.27/278.09 opens; lose it and the 50-SMA at 250.14 becomes the magnet. Until one of those resolves, the honest read is a contracting range with an upward tilt, and the highest-expectancy action is to trade the edges of 257–266.4 rather than to predict the break.