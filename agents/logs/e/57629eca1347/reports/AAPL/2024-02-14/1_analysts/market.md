# AAPL — Multi-Timeframe Technical Report
**Analysis date: 2024-02-14 | Last session close: 184.15**

---

## 0. Data integrity / verification note

All exact price and indicator levels below come from the **verified market snapshot (2024-02-14)** and the indicator series retrieved for the same simulated date. The snapshot's final OHLCV row (close 184.15, high 185.53, low 182.44, volume 54,630,500) **agrees exactly** with the last row of the raw OHLCV pull — no discrepancy to flag. One minor caveat: the snapshot also returns an `mfi` value of 0.3576, a scale inconsistent with the conventional 0–100 MFI; **I have excluded it** from the analysis rather than interpret an ambiguous number.

**Verified readings, 2024-02-14:**

| Metric | Value |
|---|---|
| Close / Open / High / Low | 184.15 / 185.32 / 185.53 / 182.44 |
| Volume | 54.63M |
| 10 EMA | 187.124 |
| 50 SMA | 190.195 |
| 200 SMA | 183.340 |
| MACD / Signal / Hist | −0.865 / −0.412 / −0.454 |
| RSI(14) | 40.05 |
| Bollinger mid / upper / lower | 189.356 / 196.225 / 182.488 |
| ATR(14) | 3.183 |
| VWMA | 187.334 |

---

## 1. Indicator selection and rationale (8 selected)

| # | Indicator | Why it earns a slot in *this* tape |
|---|---|---|
| 1 | **close_200_sma** | The single most important line right now: price is only **+0.81 (+0.44%)** above it. It defines whether this is a pullback or a trend break. |
| 2 | **close_50_sma** | Captures the medium-term trend that AAPL has just lost, and quantifies the resistance overhead (190.20). Also lets me track the 50/200 spread. |
| 3 | **close_10_ema** | Short-term momentum proxy; price has been riding below it since Feb 8 and it is now rolling over — the fastest read on whether the 3-week slide is decelerating. |
| 4 | **macd** | Confirms the momentum regime shift (zero-line cross on Feb 1). |
| 5 | **macdh** | Distinguishes *stalling* from *re-accelerating* downside — critical right now because the histogram compressed for a week then flared again. (I used the signal-line value from the snapshot rather than a separate `macds` series to avoid a third redundant MACD call.) |
| 6 | **rsi** | Gauges how much selling pressure remains before an oversold reset, and lets me compare this leg to the Jan 4–5 washout. |
| 7 | **atr** | Position sizing and stop placement — volatility has re-expanded (3.24 → 3.59 after Feb 2), so fixed-point stops are unsafe. |
| 8 | **vwma** | Volume-weighted "true" cost basis of recent buyers. Price is **below** it (184.15 vs 187.33), which is the cleanest available evidence of distribution. |

**Deliberately excluded:** Bollinger Bands as a *selected* series (I use the three band values from the verified snapshot as a contextual cross-check — see §5), plus `close_10_ema`-adjacent redundancy such as stochrsi, and MFI (ambiguous scale). No two selected indicators are mathematical restatements of each other.

---

## 2. Trend hierarchy: one instrument, three conflicting signals

### 2.1 Long-term (6–12 months): intact uptrend
- The **200 SMA is rising monotonically** — 179.64 on Jan 2 → 183.34 on Feb 14, a gain of ~+0.075/day (~+1.5 points/month). A rising long-term average is structural evidence of an uptrend.
- **AAPL has not closed below the 200 SMA in any session in the visible 2024 window** (Jan 2 – Feb 14). The closest approach was Jan 5: close 181.18 vs 200 SMA 180.02.
- The bounce sequence is unambiguous: **166.89 (Oct 26) → 198.11 (Dec 14) → 181.18 (Jan 5) → 195.18 (Jan 23)**. Higher lows on the major swing scale (Oct low → Jan low) and a higher high in December.

### 2.2 Intermediate (1–3 months): churning distribution / range
- Since the **Dec 14 close of 198.11**, price has been range-bound. Today's 184.15 is **−7.05% below** that Dec 14 close.
- The working range is roughly **179.25 (Feb 2 intraday low) to 196.38 (Jan 24 intraday high)** — a ~9% band for two months, with two failed attempts at the highs (Dec 14: 198.11 close/199.62 high; Jan 24: 196.38 high).
- **The 50/200 relationship is deteriorating at the margin.** The 50 SMA has been above the 200 SMA (golden-cross configuration) for the entire window, but the spread has **narrowed from 7.20 points on Jan 2 to 6.86 today**, because the 50 SMA has turned down (peak 190.925 on Jan 30 → 190.195 now, −0.73 in 11 sessions) while the 200 SMA keeps climbing. This is not a death cross — but the trend quality is decaying, and continued downside mechanically worsens it.

### 2.3 Short-term (days–weeks): clear, orderly downtrend
This is where the actionable information is. The **sequence of lower highs is textbook**:
- Jan 24 high **196.38**
- Feb 7 high **191.05**
- Feb 12 high **188.67**
- Feb 14 high **185.53**

Coupled with a **bearish moving-average stack**: price 184.15 < 10 EMA 187.12 < 50 SMA 190.20, while the 200 SMA (183.34) sits just beneath price. The 10 EMA crossed **below** the 50 SMA on **Jan 30** (10 EMA 190.79 vs 50 SMA 190.93) and has stayed below since — that was the formal short-term trend flip.

Recent run-rate, verified from closes:
- **Feb 7 → Feb 14: 189.41 → 184.15 = −2.78%** in six sessions.
- **Feb 9 → Feb 14: 188.85 → 184.15 = −2.49%**, and Feb 12/13/14 were three consecutive down days (−0.90%, −1.13%, −0.48%).
- **YTD: 192.53 (Dec 29) → 184.15 = −4.35%.**

---

## 3. Momentum: bearish, and *re-accelerating*

**MACD (line −0.865, signal −0.412, histogram −0.454):**
- The MACD line **peaked at +0.951 on Jan 26** — lagging the Jan 23/24 price peak, a routine confirmation failure — then **crossed below zero on Feb 1** (0.091 → −0.138).
- The histogram turned negative on **Jan 31** (−0.143), i.e., the line crossed below its signal there.
- Crucially, the histogram **compressed toward a bullish cross and then failed**: −0.445 (Feb 2) → −0.243 → −0.125 → −0.113 → **−0.065 (Feb 9)** → −0.137 → −0.308 → **−0.454 (Feb 14)**. That is a classic *failed re-crossover* — sellers regained control before the momentum repair completed.
- Feb 14's histogram is the **most negative reading since Jan 17 (−0.718)**, and the MACD line is the **lowest since Jan 19 (−1.026)**. Momentum is still deteriorating into the print.

**RSI 40.05:** falling from **50.81 on Feb 7** (−10.8 points in five sessions). Two things matter:
1. **It is not oversold.** The Jan 4–5 washout bottomed at **28.79**, so this leg has real room before hitting a comparable extreme. There is no reason to front-run a bounce on RSI alone.
2. **After the Jan 5 RSI low of 28.79, price closed at 181.18 and reached 195.18 by Jan 23 (+7.7%).** That is one genuine instance in the data of deeply oversold RSI marking a tradeable low — but it is a single sample, not a validated edge, and today's 40 is nowhere near that zone.

**No bullish divergence yet.** Feb 13's low (183.51) → Feb 14's lower low (182.44) came with RSI also lower (41.72 → 40.05). Price and momentum are confirming each other — bearish alignment, not exhaustion.

---

## 4. Volume and participation: sellers hold the volume-weighted cost basis

- **VWMA 187.334 > close 184.15.** The volume-weighted average price of recent activity sits **3.18 points (1.70%) above** the market. The marginal buyer is underwater — this is the definition of distribution.
- The VWMA **peaked at 189.72 on Feb 7** and has fallen every session since (189.56 → 189.19 → 188.79 → 188.07 → 187.33), tracking price down rather than cushioning it.
- **Volume context:** the 22 sessions from Jan 16 through Feb 14 averaged roughly **56.7M shares**. Down days of Feb 13 (56.53M) and Feb 14 (54.63M) were essentially *at* that average — there is **no capitulation signature**. A washout low usually prints 1.5–2× average volume.
- Contrast with the one genuine volume event in the window: **Feb 2, 102.55M shares (≈1.8× the 22-day average)** on an 8.08-point range (high 187.33, low 179.25, close 185.85 — closing in the upper third of the range). That absorbed supply and produced a **179.25 → 191.05 rally over the following three sessions**. The lesson for risk management: in this tape, *high-volume intraday undercuts have marked short-term lows*; quiet drift lower (what we have now) does not.

---

## 5. Volatility and band structure: compressed but re-expanding

- **ATR 3.183 = 1.73% of price.** It bottomed at ~2.94 on Jan 12, jumped to **3.586 on Feb 2** (event-driven), and has since eased to 3.18 — still ~8% above the January trough.
- **Bollinger (from verified snapshot):** mid **189.36**, upper **196.23**, lower **182.49**. Bandwidth = **13.74 points (7.25% of the mid)** — not a squeeze, but not elevated either.
- **Price (184.15) is in the lower half of the bands**, just **1.66 points above the lower band**.
- **Notable intraday detail:** Feb 14's low of **182.44 undercut the lower band at 182.49 by 5 cents**, and the session closed **1.29 points (55% of the day's range) above the low, back inside the band**. That is a marginal "band pierce and recover" — weak evidence of near-term stabilization, and it should not be over-read on one session with average volume.
- **Confluence to remember: the Bollinger mid (189.36) is almost exactly where the declining 50 SMA (190.20) sits.** That 189.3–190.2 zone is a thick, dual-source resistance shelf.

---

## 6. Level map (all levels derived from verified rows)

**Resistance (overhead, in order):**
| Level | Source |
|---|---|
| 185.53 | Feb 14 high (immediate) |
| **187.12 / 187.33** | 10 EMA / VWMA — the first real test of any bounce |
| 188.67 | Feb 12 high |
| **189.36 – 190.20** | Bollinger mid + 50 SMA (major shelf) |
| 191.05 | Feb 7 high (last lower high) |
| 196.38 | Jan 24 high (range top) |

**Support (below, in order):**
| Level | Source |
|---|---|
| 183.82 | Feb 1 low |
| **183.51 / 183.34** | Feb 13 low / **200 SMA — the line in the sand** |
| **182.49 / 182.44** | Bollinger lower band / Feb 14 low |
| 181.18 / 180.30 / 180.17 | Jan 5 close / Jan 17 low / Jan 5 low |
| **179.25** | Feb 2 low — the range floor |

---

## 7. Actionable scenarios and trade construction

**Base case — bearish drift inside an intact uptrend.** Price is pinned between a rising 200 SMA (support) and a falling 10 EMA/VWMA (resistance), with re-accelerating negative MACD. The path of least resistance near-term is **lower, toward 183.3–182.5**, where the 200 SMA and lower band converge.

**Scenario A — Long the 200 SMA test (mean reversion, preferred tactical setup).**
- Trigger: entry in the **183.5–182.4** zone *only* with a confirmation candle (close back above the prior day's high, or a reversal bar closing in the upper half of its range).
- Stop: **179.9** — below the Feb 2 low (179.25) and ~1.5× ATR from the entry midpoint. Placing a stop at the 200 SMA itself (183.34) is too tight: that is **0.25 ATR** away and will be noise-stopped.
- First target: **187.1–187.3** (10 EMA/VWMA). Second: **189.4–190.2** (Boll mid/50 SMA).
- Risk/reward at an 182.9 entry with stop 179.9 (3.0 risk) and target 187.2 (4.3 reward) ≈ **1.4:1** to first target, ~2.4:1 to the second.

**Scenario B — Trend-continuation long (requires patience).**
- Trigger: a **daily close above 187.33 (VWMA)** accompanied by the **MACD histogram turning positive** (it is currently −0.454 and widening, so this is days away at best). Confirmation above **190.20 (50 SMA)** would be the higher-quality, lower-frequency signal.
- Do **not** buy the current 184 level simply because it is "near support" — price is below every short-term average, below VWMA, and momentum is still expanding to the downside.

**Scenario C — Structural break (thesis invalidated).**
- Trigger: a **daily close below 183.34 (200 SMA)** — the first such close in the visible 2024 record. That would break the last remaining pillar of the uptrend.
- Next reference: **179.25**. A close below that opens the Oct 26 low (166.89) as the strategic downside target.
- Note for shorts: the Feb 2 evidence (102.55M shares, close well off the low, +6.6 points over three sessions) argues that **fresh shorting into a high-volume flush has been poorly rewarded** in this name. Prefer shorting rallies into 187–190 over chasing breakdowns.

**Position sizing.** With ATR at 3.18 (1.73% of price), a 2-ATR stop is **6.37 points (3.5%)**. For 1% account risk per trade, sizing should be roughly `0.01 × Equity / 6.37` shares — and ATR has risen from 2.94 to 3.18 since Jan 12, so **the same dollar risk now buys ~8% fewer shares** than it did a month ago. Re-size, don't reuse old share counts.

**Risk-management note on gaps.** Feb 2 (8.08-point range, 2.25× the ATR that prevailed then) shows this instrument can gap through a stop on event risk. A 183.5-based stop construction is therefore inferior to a wider, volatility-scaled one.

---

## 8. What would change the view

| Observation | Implication |
|---|---|
| Histogram turns up and crosses zero (needs > 0 from −0.454) | Failed-cross pattern invalidated → short-term bottom likely |
| Daily close > 187.33 VWMA | Price reclaims volume-weighted cost basis → buyers back in control |
| Daily close > 190.20 (50 SMA) + 50 SMA turns up again | Range breakout retest → re-open 196.38 target |
| RSI pushes under ~30 with volume ≥ 1.5× average | Oversold reset comparable to Jan 4–5 (28.79) → high-quality mean-reversion entry |
| Daily close < 183.34 (200 SMA) | First structural break of 2024 → shift bias to neutral/bearish, watch 179.25 |
| 50/200 spread keeps compressing below ~6.0 | Trend-quality decay confirmed → reduce strategic long exposure |

---

## 9. Summary table

| Dimension | Verified reading (2024-02-14) | Interpretation | Actionable takeaway |
|---|---|---|---|
| Price | 184.15 (O 185.32, H 185.53, L 182.44) | 3rd straight down day; closed 55% up in range | Mild intraday stabilization only, no reversal signal |
| Long-term trend | 200 SMA 183.34, rising +0.075/day; price **+0.44% above** | Uptrend intact but price is glued to the line | 183.34 is the pivot for the entire thesis |
| Medium-term | 50 SMA 190.195, declining from 190.925 (Jan 30) | Price −3.18% below 50 SMA; trend lost | 189.4–190.2 = major resistance shelf |
| Short-term | 10 EMA 187.124 < 50 SMA; price below both | Bearish MA stack since Jan 30 cross | Sellers control the weeks timeframe |
| Lower highs | 196.38 (Jan 24) → 191.05 (Feb 7) → 188.67 (Feb 12) → 185.53 (Feb 14) | Textbook descending structure | Sell rallies, don't chase breakdowns |
| Momentum | MACD −0.865 / signal −0.412 / hist −0.454 | Zero-line cross Feb 1; **failed** re-cross Feb 9; hist most negative since Jan 17 | Downside momentum re-accelerating |
| RSI | 40.05 (from 50.81 on Feb 7) | Not oversold; Jan low was 28.79 | Room for more downside before a washout |
| Volume | 54.63M vs ~56.7M 22-day avg; VWMA 187.334 > price | Distribution, no capitulation yet | Wait for a high-volume flush OR a VWMA reclaim |
| Volatility | ATR 3.183 (1.73%); 2-ATR stop = 6.37 pts | Re-expanded after Feb 2 (3.59) | Size positions off ATR, not fixed points |
| Bollinger | mid 189.36 / UB 196.23 / LB 182.49 | Price in lower half; LOD 182.44 pierced LB then recovered | 182.5 is the immediate downside pivot |
| Key support | 183.34 (200 SMA) → 182.49 (LB) → 181.18–180.17 (Jan lows) → 179.25 (Feb 2) | Stacked demand but each layer must be confirmed | Stop below 179.9 for long setups |
| Key resistance | 187.12/187.33 → 188.67 → 189.36–190.20 → 191.05 → 196.38 | Thick overhead supply | Do not initiate longs below 187 until hist turns up |
| Net bias | **Short-term bearish / long-term bullish** | Pullback inside an uptrend, decaying at the edges | Prefer 183.5–182.4 with confirmation, or 187.3+ reclaim; avoid the middle |