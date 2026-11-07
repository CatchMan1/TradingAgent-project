# AMZN — Multi-Timeframe Technical Analysis as of 2024-01-19

## 1. Data integrity check (performed first)

The frozen OHLCV pull (2023-06-01 → 2024-01-19, 160 rows) and the verified snapshot agree row-for-row on the latest session, and every indicator value in the snapshot matches the standalone `get_indicators` series on 2024-01-19 (e.g., RSI 60.72, MACD 1.6928, signal 1.5838, 50-SMA 148.432, 200-SMA 131.083, ATR 2.9855, VWMA 151.076). **No discrepancy to flag.** One caveat: the snapshot's `mfi` field prints as `0.508872`, which is inconsistent with a 0–100 MFI scale, so I exclude it rather than interpret an ambiguous number.

**Verified latest session (2024-01-19):** Open 153.83 / High 155.76 / Low 152.74 / **Close 155.34** / Volume 51.65M.

---

## 2. Indicator selection and rationale (8 selected)

| # | Indicator | Why it's the right tool here |
|---|---|---|
| 1 | **close_200_sma** | Establishes the primary regime. AMZN is deep in a long-term uptrend; this anchors "trade with the trend." |
| 2 | **close_50_sma** | The medium-term trend spine and the level that has repeatedly defined the swing structure (including the January pullback low zone). |
| 3 | **close_10_ema** | Captures the fast momentum that has flipped positive again since January 17; also the practical trailing trigger. |
| 4 | **macd** (+ **macds**/histogram as companion) | Measures whether the January re-acceleration is genuine or just a bounce, and exposes the momentum divergence vs. price highs. |
| 5 | **rsi** | Determines whether price is stretched. Critically, it never exceeded 70 on this leg, so it tells us about remaining fuel, not exhaustion. |
| 6 | **boll_ub** / **boll_lb** (with middle) | Defines the volatility envelope: where breakout continuation lives and where a mean-reversion fade begins. |
| 7 | **atr** | Position sizing and stop placement — mandatory given ATR is at a 3-month low, i.e., a compression that historically resolves into expansion. |
| 8 | **vwma** | Confirms whether the rally is volume-supported and identifies the average cost basis of recent buyers (~151). |

I deliberately avoided redundancy: no stochastic/RSI pairing, no triple moving-average stacking beyond what the trend hierarchy requires, and no second volatility measure beyond ATR + Bollinger width.

---

## 3. The trend hierarchy: textbook bullish alignment

- **Close 155.34 > 50-SMA 148.432 > 200-SMA 131.083.** Price sits **+18.51%** above the 200-SMA and **+4.65%** above the 50-SMA. This is a fully stacked uptrend with no crossover ambiguity.
- **The 50/200 spread is widening, not narrowing:** the gap has grown from roughly 17.9 points at end-October to **17.35 points today** on a rising 200-day base (131.08), i.e., ~13.2% above the long-term average. Widening spread = trend acceleration, not decay.
- **Slopes are positive and steepening on the medium term:** the 50-SMA has climbed from 132.18 (2023-10-27) to 148.432 (2024-01-19), and gained ~0.31 points in the last session alone (147.822 → 148.432 on 2024-01-18 → 2024-01-19).
- **The 10-EMA has re-crossed upward into price:** 10-EMA 152.82 vs. close 155.34 (+1.65%). The 10-EMA bottomed at 149.099 on 2024-01-05 and 2024-01-08 and has risen every session since 2024-01-09 (149.512 → 152.820). Fast momentum is unambiguously re-accelerating.
- **Magnitude of the primary leg:** from the 2023-10-26 close of 119.57 (intraday low 118.35) to 155.34 today, AMZN is up **+29.9%** in about 58 sessions. Today's close is the **highest close in the entire June-2023-to-date window**, marginally above the 2024-01-11 close of 155.18.

**Interpretation:** trend-following conditions favor the long side. The "buy the dip in an uptrend" playbook has already worked once this month: price fell to 144.05 intraday on 2024-01-04 (with the 50-SMA at 144.30 that day) and 144.53 on 2024-01-05 (50-SMA 144.64), then reclaimed the average — a documented test of the 50-SMA zone as demand.

---

## 4. Momentum: improving, but with an important divergence caveat

**MACD (12/26/9):**
- MACD line **1.6928** vs. signal **1.5838**, histogram **+0.1090**.
- The histogram was negative on 2024-01-16 (−0.0110... line 1.6497 vs. signal 1.5694), 2024-01-17 (−0.0392), and 2024-01-18 (−0.0120), and flipped **positive on 2024-01-19**. This is a fresh, one-session-old bullish crossover — early, not confirmed.
- The MACD line bottomed at **0.7788 on 2024-01-08** and has climbed for most sessions since (1.6928 today), a clear re-acceleration off the January correction.

**The caveat traders must not skip:** MACD peaked near **3.89 on 2023-11-20/11-27** when price closed ~146. Price is now **6.3% higher than that close while MACD is ~56% lower**. That is a classic momentum-divergence signature — higher price highs on weaker momentum. The same pattern appears in RSI (68.05 on 2023-12-18 at a 154.07 close; 60.72 today at a 155.34 close). **This does not break the trend, but it lowers the odds of a high-velocity melt-up and raises the odds of a grind/chop or a failed breakout at the 157–158 area.**

**RSI:** 60.72, mid-upper range but **not overbought**. The January swing low in RSI was 40.23 on 2024-01-04 — never oversold either. The recovery sequence (40.2 → 51.7 → 56.2 → 60.4 → 62.8 → 61.3 → 57.4 → 53.7 → 57.3 → 60.7) shows a buyer-controlled tape with no exhaustion signal. Because RSI topped out at ~68 rather than 75–80, there is genuine headroom to ~70+ before overbought becomes binding.

**Net momentum read:** tactically bullish, structurally decelerating. Use momentum confirmation rather than anticipatory entries.

---

## 5. Volatility and the Bollinger envelope

- **Bollinger:** middle (20-SMA) **151.8685**, upper **157.8864**, lower **145.8506**. Bandwidth = **7.93%** of the middle.
- **Position within the band (%B) ≈ 78.8%** — riding the upper third, but *inside* the band, not piercing it. In strong trends this is continuation territory; it only becomes a fade signal if price closes outside the upper band and then re-enters.
- **Bandwidth dynamics matter here:** bandwidth was ~3.9% on 2023-12-15 (a serious squeeze), and has since expanded to ~7.9%. That is a volatility expansion phase, consistent with the trend making higher highs and higher lows.
- **ATR is 2.9855**, i.e., **1.92% of price** — down from 3.63 on 2023-11-22 and 3.45 on 2023-12-18. Volatility is compressing again *while* price pushes to new highs — a coiling pattern. The practical consequence: stops must be wider in ATR terms than they were during the November high-volatility window, and a break beyond the 157.89 upper band with volume would signal a volatility breakout rather than a routine wick.

**Risk math:** 2×ATR = **5.97 points**. A 2-ATR stop from the 155.34 close sits at **149.37**, which conveniently overlaps the 2024-01-17 low of 149.91 and the 50-SMA (148.43) region — a structurally meaningful confluence rather than an arbitrary number.

---

## 6. Volume and participation

- **VWMA = 151.076**, and price is **+2.82%** above it. The volume-weighted average cost of recent buyers is ~151, meaning the bulk of January accumulation is in profit — supportive for holding, but it also marks ~151 as the line where those same holders turn into sellers.
- **VWMA has flattened**: 150.632 (2024-01-10) → 150.878 (01-18) → 151.076 (01-19), i.e., roughly +0.44 points over seven sessions while price advanced from 153.73 to 155.34. Flat VWMA under rising price = the advance is being made on **less volume-weighted conviction** than the December leg (VWMA ran 147.43 → 150.70 between 2023-12-18 and 2023-12-29). This corroborates the MACD/RSI divergence.
- **Session-level volume, however, is constructive:** 51.65M on 2024-01-19 versus a ~41.5M average across the prior ~21 sessions — roughly **+25% relative volume** on an up-closing day that also reclaimed the 10-EMA. The prior pullback day (2024-01-17, close 151.71) traded only 34.95M. Down-days on light volume, up-days on expansion: accumulation-style behavior.
- Context reference: the heaviest prints in the dataset are event-driven (153.13M on 2023-08-04, 133.31M on 2023-07-21, 125.31M on 2023-10-27, 110.09M on 2023-12-15 — the latter a quarterly-expiration date). Nothing in January resembles those, so this is orderly institutional flow, not a catalyst spike.

---

## 7. Actionable level map

| Level | Value | Source (all verified) | Role |
|---|---|---|---|
| Resistance R3 | **160.00** | Psychological round number (inferred, not tool-computed) | Extended target |
| Resistance R2 | **157.89** | Bollinger upper band, 2024-01-19 | Breakout trigger / fade zone |
| Resistance R1 | **157.17** | 2024-01-11 intraday high (swing high) | Immediate ceiling |
| **Spot** | **155.34** | 2024-01-19 close | — |
| Pivot | **151.87** | Bollinger middle / 20-SMA | Bull/bear short-term divider |
| Support S1 | **152.82** | 10-EMA | Trailing-stop reference |
| Support S2 | **151.08** | VWMA | Cost-basis defense line |
| Support S3 | **149.91** | 2024-01-17 low | Pattern low; must hold |
| Support S4 | **148.43** | 50-SMA | Trend spine |
| Support S5 | **145.85** | Bollinger lower band | Deeper mean-reversion |
| Support S6 | **144.05** | 2024-01-04 low | January floor |

---

## 8. Scenario playbook with explicit triggers

**A. Bullish continuation (base case, ~55% weight).**
Trigger: a close **above 157.17** (01-11 high) with volume ≥ ~50M, ideally with %B pushing above 100 (close > 157.89).
Plan: enter/add on the breakout close or on the first successful retest of 157.17 as support. Stop 2×ATR below entry (~5.97 points) or below the 10-EMA. First target 160, secondary measured move toward the 2023 high-water zone above. Confirm with MACD histogram expanding for 2–3 sessions rather than contracting — given the existing momentum divergence, this confirmation is non-negotiable.

**B. Range consolidation at the highs (most probable alternative, ~30%).**
Trigger: repeated rejection at 157.0–157.9 while price holds above 151.7–152.8.
Plan: trade the box — accumulate near **151.0–152.8** (VWMA / 10-EMA / 20-SMA cluster) with stops below **149.91**; take partials into 155.5–157.9. ATR of only ~3.0 means the box is ~6 points wide, i.e., about 2×ATR — right-sized for swing trades. Avoid chasing the middle of the range.

**C. Trend-damage pullback (~15%).**
Trigger: an impulsive close **below 149.91** (01-17 low) that is not immediately reclaimed; or a close below the **50-SMA at 148.43**.
Plan: stand aside or flip tactical short with a target at 145.85 (lower band) and 144.05 (January low). Note that the 50-SMA is rising ~0.3 points/day, so by late January the mechanical trend line itself will be near 150 — the "no-trade" band tightens fast.

---

## 9. Position sizing note

With ATR = 2.9855 (1.92% of price), a 2-ATR stop is ~3.84% of notional. Risking 1% of equity per trade implies roughly **26% notional exposure**. If using a tighter 1.5-ATR stop (~4.48 points, under 151), sizing rises to ~34% notional — but that stop sits inside the normal daily noise envelope (recent daily ranges include 3.5+ points), so it will be hit by noise more often. **Recommendation: use the 2-ATR / ~149.4 stop, sized at ~25% notional, rather than a tight stop with larger size.**

---

## 10. What would change this view

1. **MACD histogram rolling back negative within 2–3 sessions** — would confirm the higher-price/lower-momentum divergence and argue the 157 area is a distribution ceiling.
2. **A close below VWMA (151.08) with above-average volume** — that would trap the entire January cohort of buyers and typically forces a deeper flush toward the 50-SMA.
3. **RSI pushing above 70 while price stalls under 157.2** — classic overbought-into-resistance combination; reduce, don't add.
4. **Volume fading back under ~35M on any further push** — the relative-volume expansion on 2024-01-19 would look like a one-off rather than the start of accumulation.
5. **Event risk:** AMZN's Q4 results have historically landed in early February (company-calendar knowledge, **not** derived from these tools). That is a binary gap risk roughly two weeks out; any position carried into it should be sized to survive a multi-ATR gap, because ATR-based stops do not protect against overnight gaps.

---

## 11. Summary table

| Dimension | Evidence (verified 2024-01-19) | Signal | Actionable implication |
|---|---|---|---|
| **Long-term trend** | Close 155.34 vs. 200-SMA 131.083 (+18.5%) | Strong bull | Core bias long; shorting is counter-trend |
| **Medium-term trend** | 50-SMA 148.432, rising +0.31/session; 50>200 spread widening | Strong bull | Buy pullbacks, not breakouts into thin volume |
| **Short-term momentum** | 10-EMA 152.820, close +1.65% above; 10-EMA up 9 straight sessions | Bull | Trailing stop reference at 152.8 |
| **MACD** | Line 1.6928 > signal 1.5838; histogram +0.109, crossed +1 session ago | Mild bull, unconfirmed | Wait for histogram expansion before adding |
| **Momentum divergence** | MACD 3.89 (11-20, close 146.13) vs. 1.69 today (close 155.34); RSI 68.05 (12-18) vs. 60.72 today | Bearish caution | Lower conviction; expect chop near highs |
| **RSI** | 60.72; mid-Jan low 40.23 (01-04); no >70 print this leg | Bull with headroom | Room to 70+ before overbought binds |
| **Bollinger** | Mid 151.8685 / UB 157.8864 / LB 145.8506; %B ≈ 78.8%; width 7.93% (from 3.9% on 12-15) | Upper-third continuation, volatility expanding | Breakout trigger 157.89; fade only on failed re-entry |
| **ATR / volatility** | ATR 2.9855 = 1.92% of price, near 3-month low | Compression | 2-ATR stop ≈ 149.37; size ~25% notional at 1% risk |
| **Volume** | 51.65M vs. ~41.5M recent average (+25%) on an up day; 01-17 pullback only 34.95M | Accumulation-leaning | Supports continuation but not confirmed alone |
| **VWMA** | 151.076 (flattening: +0.44 pts over 7 sessions); price +2.82% above | Neutral-to-positive, weakening | Break below 151 = buyer trap signal |
| **Key resistance** | 157.17 (01-11 high), 157.89 (upper band), 160.00 (psych) | — | Breakout entry trigger / partial-profit zone |
| **Key support** | 152.82 (10-EMA), 151.08 (VWMA), 149.91 (01-17 low), 148.43 (50-SMA), 145.85 (lower band), 144.05 (01-04 low) | — | Staged accumulation 151–149; invalidation < 148.43 |

**Bottom line for AMZN:** the trend, the moving-average stack, and the volume profile on 2024-01-19 all point the same way — up. But the momentum complex (MACD and RSI both printing lower highs while price prints a higher high) plus a flattening VWMA say this is a **maturing, lower-conviction advance into the 157.2–157.9 ceiling**, not a fresh launch. The highest-expectancy structure is to be a patient buyer in the **149.9–152.8** confluence zone with a stop under **149.4** (2×ATR, coinciding with the 01-17 low), or to buy a **confirmed close above 157.17 with volume ≥50M**, and to explicitly de-risk ahead of the early-February earnings event rather than holding full size through it.