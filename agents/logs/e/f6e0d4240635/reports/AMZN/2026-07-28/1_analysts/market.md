# AMZN — Technical & Trend Assessment
**Analysis date:** 2026-07-28 (latest completed session: 2026-07-28)
**Reference price (verified snapshot, 2026-07-28):** Open 232.85 · High 233.11 · Low 228.10 · **Close 230.86** · Volume 44,521,600

---

## 0. Data integrity check (read first)

All indicator values below are cross-checked against the `get_verified_market_snapshot` output for 2026-07-28. The point-in-time OHLCV series and the snapshot agree line-for-line on the final row (close 230.86, volume 44.52M), **so no reconciliation is required**.

Two flagging notes:
1. **The snapshot's `mfi` value is 0.354128**, which is outside the canonical 0–100 range for Money Flow Index and therefore internally inconsistent. I have **excluded MFI** from this analysis rather than reinterpret a number I cannot verify.
2. The snapshot's ATR (6.910234) and the `atr` series (6.910234065727488) agree; Bollinger middle in the snapshot (243.307) matches the `boll` series on 2026-07-28 (243.30699996948243). No conflicts found.

---

## 1. Structural trend: a two-tier market

AMZN is in **two different trends at once**, and that tension is the single most important fact in this report.

**Long-term (200-day): still constructive, but the price has just slipped beneath it.**
- 200 SMA on 2026-07-28 = **234.664**, and it is still *rising* (+0.028/day; 231.52 on 2026-05-29 → 234.66 now).
- Close 230.86 is **1.62% below** the 200 SMA. This is not the first violation: the stock closed below the 200 SMA on 2026-06-22 (232.79 vs 232.84) and 2026-06-25 (227.01 vs 232.795), then reclaimed it in July. **It crossed back below on 2026-07-23** (close 233.66 vs 200 SMA 234.532) and has stayed below for four sessions.
- Interpretation: the multi-month uptrend is *damaged but not broken*. Rather than treat the 200 SMA as support, treat it as **overhead supply at ~234.7** until price closes decisively back above it.

**Intermediate (50-day): clearly deteriorating.**
- 50 SMA = **247.721**, down from 256.637 on 2026-06-17 and falling ~0.73/day. Price is **6.81% below** it.
- The 50 SMA sits **+5.55% above** the 200 SMA, so the "golden-cross" alignment from the spring rally is still nominally intact — but the 50 SMA is descending toward a *rising* 200 SMA at roughly 0.75 points/day of convergence on a 13.06-point gap (~17–18 sessions). A **death cross becomes a live risk in late August/September 2026** if the current drift persists. That is a strategic, not tactical, consideration — but it matters for anyone sizing a swing position here.

**Short-term (10 EMA): firmly bearish.**
- 10 EMA = **238.644**, and it has rolled over hard: 247.59 on 2026-07-21 → 238.64 on 2026-07-28 (−9 points in five sessions, ~−2/day).
- Price is **3.26% below the 10 EMA**. Price has been below it since 2026-07-23.

**The stack is fully inverted below the price now:** close 230.86 < 200 SMA 234.66 < 10 EMA 238.64 < VWMA 243.53 ≈ Bollinger mid 243.31 < 50 SMA 247.72. When every average sits overhead, rallies are countertrend until proven otherwise.

### The shape of the move (verified closes)
- Cycle peak close: **274.99 on 2026-05-06** (intraday high 278.56 on 2026-05-05).
- First leg down into 2026-06-25 close **227.01** (intraday low 225.55).
- Recovery into 2026-07-15/16: closes **254.96** and 249.89, with the swing intraday high at **258.08 on 2026-07-16**.
- Then a **failed rally / lower high** and a sharp reversal:
  - 2026-07-22 close 244.85
  - 2026-07-23 close 233.66 (**−4.57%**, and it *gapped* — 07-22 low 242.45 vs 07-23 high 238.35, leaving an **unfilled gap between ~238.35 and ~242.45**)
  - 2026-07-24 close 232.11
  - 2026-07-27 close 231.39
  - 2026-07-28 close 230.86
- Net: **five consecutive lower closes**, −5.71% from the 07-22 close, −9.45% from the 07-15 high close (254.96), and **−16.05% from the 2026-05-06 peak close**.
- Year-to-date context: 2026-01-02 close was 226.50, so AMZN is only **+1.9% YTD** — an entire 5-month round trip has been given back.

---

## 2. Momentum: the July thrust has fully failed

**MACD (line / signal / histogram on 2026-07-28): −2.945 / −1.268 / −1.676**

The sequence is unambiguous:
- MACD was deeply negative through June (trough −6.875 on 2026-06-26), then repaired steadily through July, **crossing above zero on 2026-07-15** (+0.260) and peaking at **+0.824 on 2026-07-20**.
- That bullish phase lasted **only six sessions**. MACD rolled over to −0.530 on 2026-07-23, crossing **below its signal line** (signal was −0.2325) on the same day — a classic bearish crossover that also flipped MACD back below zero.
- The histogram confirms a **momentum regime change**: it peaked at +2.124 on 2026-07-15 and has printed −0.297 → −1.014 → −1.452 → **−1.676** over the last four sessions. Negative and still widening, i.e. downside momentum is *accelerating*, not merely decaying.
- Critical nuance: at **−2.945**, MACD is still well above its June trough (−6.875). This is a *fresh* deterioration at a higher absolute level, meaning there is ample room for further downside momentum before the oscillator reaches the kind of extreme that produced the late-June bounce. **Do not assume the July recovery is intact simply because MACD is "only" −3.**

**RSI: 36.54** (from 60.14 on 2026-07-15, 54.04 on 2026-07-20, 38.62 on 2026-07-23)
- Approaching, but **not in, oversold territory** (<30).
- The relevant precedent in this dataset: RSI bottomed at **32.46 on 2026-06-10** and **33.63 on 2026-06-25** — both times producing tradeable lows. Today's 36.54 is **2–4 points above that reversal zone**, so the "washed-out" condition is close but not yet reached.
- The 4-day RSI collapse from 54 to 36.5 with price only −5.7% is a velocity signal: sellers, not rotation.

---

## 3. Volatility: compression under distribution

**ATR = 6.910**, down from **8.591 on 2026-06-29** — a ~20% contraction in average true range.
- ATR is now **2.99% of price**. Daily swings are getting smaller even as the trend bends lower — a **grinding, orderly decline** rather than a capitulation. That is typically *harder* to trade countertrend, because there is no exhaustion spike to fade.
- Practical ATR-derived levels from the 230.86 close: 1×ATR down = **223.95**; 2×ATR down = **217.04**; 1×ATR up = **237.77**.

**Bollinger Bands (20, 2): middle 243.307 · upper 256.780 · lower 229.834**
- Price (230.86) closed just **+0.45% above the lower band** and **intraday pierced it** (2026-07-28 low 228.10 < 229.834), then closed back inside. That is a "band test," not yet a confirmed breakdown.
- The middle band (243.31) is now *flattening* after declining from 256.34 (2026-06-15), while the **lower band has been rising** from 221.62 (2026-06-25) to 229.83. The result is **substantial band-width compression: total width has fallen from 47.40 (18.5% of the middle, 2026-06-15) to 26.95 (11.1% of the middle, 2026-07-28)**.
- Why this matters: narrowing bands into a price decline usually resolves with an **expansion move**, and the direction of the prior trend (down) plus the volume skew (below) argue the resolution risk is downward. The upside corollary: a squeeze this tight also means a violent snap-back is possible if 228–230 holds.

---

## 4. Volume: the tape confirms distribution

**VWMA = 243.527**, and price is **5.20% below it** — the volume-weighted average holder is underwater, which caps rallies.
- VWMA rose steadily from 236.70 (2026-06-26) to a peak of **247.03 on 2026-07-22**, then flattened to 243.53 — the volume-weighted price is now *below* where the July rally peaked, i.e. the July buyers are carrying losses.

Recent volume pattern is the tell:
- The entire July recovery (2026-07-01 → 07-16, close 241.70 → 249.89) ran on **modest** volume: 53.8, 48.2, 40.0, 40.6, 29.7, 38.1, 31.7, 34.6, 30.1, 45.2, 45.3, 43.6M.
- The selloff came on **heavier** volume: **47.5M on 2026-07-23** (the −4.57% gap day) and **44.5M on 2026-07-28** (a new low close).
- The 19-session average volume (2026-07-01 through 2026-07-28) is ~**38.8M**. The 2026-07-28 down day ran **+14.7% above** that average.
- **Advancing on light volume, declining on heavy volume = distribution, not accumulation.** This is the single most persuasive bearish confirmation in the dataset, and it is not something the moving averages can tell you.

(Extreme-volume outliers for context, not trend signals: **248.4M on 2026-06-26** and **179.2M on 2026-02-06** — the latter accompanying the Feb 5–6 crash from 232.99 to 210.32.)

---

## 5. Key levels — verified, not inferred

**Resistance (in order of proximity):**
| Level | Source | Notes |
|---|---|---|
| 234.66 | 200 SMA | Rising; first real test of any bounce |
| 238.35–242.45 | 2026-07-23 gap zone | **Unfilled gap**; heavy overhead supply |
| 238.64 | 10 EMA | Falling ~2/day; dynamic resistance |
| 243.31 / 243.53 | Bollinger mid / VWMA | Confluence cluster |
| 247.72 | 50 SMA | Falling; bear-case invalidation zone |
| 254.96–258.08 | 2026-07-15 close / 07-16 intraday high | Lower-high ceiling |

**Support (in order of proximity):**
| Level | Source | Notes |
|---|---|---|
| 229.83 | Bollinger lower band | Already pierced intraday 07-28, held on close |
| 228.10 | 2026-07-28 low | Current session floor |
| 227.01 | 2026-06-25 close | Prior swing-low close |
| **225.55** | 2026-06-25 intraday low | **The line in the sand** — 0.77 ATR below current close |
| ~210 | Feb/Mar 2026 congestion | 210.11 (02-20), 210.32 (02-06), 208.72 (02-09) |

**A nuance worth flagging:** between **~225.55 and ~210** there is essentially **no daily closing structure** in the frozen data — that band was traversed by the Feb 5–6 gap-downs (232.99 → 222.69 → 210.32, low 200.31). If 225.55 fails, price is entering a **low-friction vacuum** where it can travel fast. That is a genuine tail risk, not a forecast.

---

## 6. The two-sided case (be honest about both)

**Bear case (currently dominant):**
Price below all four key averages; MACD bearish cross with an expanding negative histogram; RSI still 6 points above oversold; five consecutive lower closes; unfilled gap overhead; distribution volume; rising lower Bollinger band narrowing into a squeeze. The July rally (227.01 → 258.08 intraday) failed precisely at the descending 50 SMA region and made a **lower high relative to May**. That is textbook corrective behavior.

**Bull case (respectable, but unproven):**
1. **The 200 SMA is still rising** and has not yet been decisively lost — a reclaim of 234.66 would neutralize the intermediate bear case.
2. **Bollinger lower band held** on 2026-07-28 despite an intraday breach — buyers appeared at 228.10.
3. **RSI bounced from 32–34 twice in six weeks** (2026-06-10 and 2026-06-25) at nearly identical price levels, and both produced +10%+ recoveries. Symmetry favors another attempt.
4. **ATR is contracting**, not expanding — no panic, no forced liquidation. Orderly pullbacks within uptrends often resolve higher.
5. The 50/200 alignment has not yet crossed.

**Resolution:** the bear case has more evidence *today*, but this is a **decision point**, not a trend-following entry. Price is compressed between the lower band (229.83) and the 200 SMA (234.66) — a 2.1% bracket. Whoever wins that bracket likely determines the next 5–8%.

---

## 7. Actionable plan

**Bias: tactically bearish / structurally neutral. Do not initiate new longs at 230.86 without a trigger.**

**A) Short-side continuation (primary, but do not chase the close)**
- Entering short at 230.86 with price sitting 0.45% off the lower Bollinger band and RSI 36.5 is **poor risk/reward** — you're selling the bottom of a compressed range into a band that just held.
- Preferred: **sell a bounce into 237.8–239.0** (10 EMA / 1×ATR up) or into **242.5–243.5** (gap zone + VWMA + Bollinger mid confluence).
- Stop: **above 244.20** on a closing basis (invalidates the gap zone). From a 238.5 entry that is ~5.7 points ≈ **0.83 ATR** ≈ 2.4% risk.
- First target: **229.8–228.1** (band + 07-28 low). Second target: **225.55**. Do not extend targets beyond 225.55 without a fresh volume confirmation on the break.

**B) Short-side breakdown trigger (higher conviction if it comes)**
- A **daily close below 225.55 on volume > 47.5M** (i.e. above the 07-23 selloff day) would confirm the range break.
- Stop: back above **230.90**. Risk ~5.3 points ≈ 0.77 ATR ≈ 2.4%.
- Note the vacuum below: expect fast travel toward 210–215. Take partials aggressively; low-structure zones produce air pockets in both directions.

**C) Long-side reversal (countertrend — small size, needs confirmation)**
- Trigger 1: a **close above 238.64 (10 EMA)** with RSI back above 50 → targets 243.3, then 247.7.
- Trigger 2 (higher quality): a **close above 247.72 (50 SMA)**, which would restore the intermediate uptrend.
- Better entry, if you want to be early: **226.0–228.5 limit zone** with a hard stop at **225.30** (below the 06-25 low). Risk ~2.7 points = 0.39 ATR ≈ 1.2% — tight, but the win rate is low; size accordingly (half of normal).
- **If 225.30 trades, the long thesis is dead. No averaging down.**

**Position sizing (use ATR, not gut):** with ATR at 6.910 (2.99% of price), a 1-ATR stop is ~3% of price. For a 1% account risk budget and a 5.4-point stop, notional exposure = (0.01 × Equity / 5.4) × 230.86 ≈ **43% of equity**. Cap it at **⅓ to ½ of that** given the unresolved squeeze and the tendency of narrow-band regimes to gap.

**Invalidation matrix:**
- Bear thesis invalidated by: close > 240, or two consecutive closes > 238.64 with expanding volume.
- Bull thesis invalidated by: close < 225.55.
- Neutral/range thesis (229.8–234.7) remains valid until either boundary closes.

---

## 8. Why these 8 indicators were selected

| Indicator | Why it earns a slot in *this* market |
|---|---|
| `close_10_ema` | Fastest read on the 5-session breakdown; the falling 238.64 line is the operative near-term resistance. |
| `close_50_sma` | Defines the intermediate downtrend (price −6.81%) and measures the death-cross clock. |
| `close_200_sma` | The strategic line: still rising, price just lost it. Determines whether this is a correction or a trend change. |
| `macd` | Captures the exact failure of the July thrust and the 07-23 zero-line/signal crossover. (Signal line & histogram used as derived components — histogram peaked +2.124 on 07-15, now −1.676.) |
| `rsi` | Distinguishes "approaching oversold at 36.5" from "actually oversold," and has two verified reversal precedents at 32–34. |
| `boll_lb` | The 229.83 band is where price is *right now*; with the middle flattening, it also quantifies the squeeze (width 18.5% → 11.1%). Directly actionable. |
| `atr` | Volatility is contracting (8.59 → 6.91), which reframes the decline as orderly and sets every stop and size in this report. |
| `vwma` | The only volume-integrated trend measure here, and the one that exposed the distribution: rally on ~35M, decline on 44–47M. Price is 5.20% below 243.53. |

**Deliberately excluded:** `macdh` as a standalone (redundant with `macd`/`macds`), `boll_ub` (the upper band at 256.78 is 11% away — not decision-relevant this week, though its contraction is discussed), and `mfi` (value in the snapshot is outside its valid 0–100 range; unusable).

---

## 9. Summary table

| Dimension | Reading (2026-07-28) | Signal | Evidence |
|---|---|---|---|
| **Price** | 230.86 (−5.71% in 4 sessions) | Bearish | 5 consecutive lower closes since 07-22 (244.85) |
| **vs 200 SMA** | −1.62% (234.664, rising) | Caution / neutral | Lost on 07-23, first sustained break since late June |
| **vs 50 SMA** | −6.81% (247.721, falling 0.73/day) | Bearish | 50 > 200 by 5.55%, converging ~17 sessions |
| **vs 10 EMA** | −3.26% (238.644, falling ~2/day) | Bearish | Dynamic resistance for any bounce |
| **vs VWMA** | −5.20% (243.527) | Bearish | July buyers underwater; distribution confirmed |
| **MACD / Signal / Hist** | −2.945 / −1.268 / −1.676 | Bearish, accelerating | Bearish cross 07-23; hist 4 sessions negative and widening |
| **RSI** | 36.54 (from 60.14 on 07-15) | Bearish, near-oversold | 2–4 pts above the 32–34 reversal zone of 06-10 / 06-25 |
| **Bollinger** | Mid 243.31 · UB 256.78 · LB 229.83 | Squeeze at lower band | Close +0.45% above LB after piercing to 228.10; width 11.1% vs 18.5% on 06-15 |
| **ATR** | 6.910 (2.99% of price; peak 8.591 on 06-29) | Orderly decline | No capitulation; 1 ATR ≈ 6.9 points |
| **Volume** | 44.52M (+14.7% vs 19-day avg 38.8M) | Bearish confirmation | Down days 47.5M / 44.5M vs July rally ~35M |
| **Structure** | Lower high 258.08 (07-16) vs 278.56 (05-05) | Corrective | −16.05% from 274.99 peak close |
| **Key support** | 229.83 → 228.10 → 227.01 → **225.55** | Decision zone | 225.55 = 06-25 low, 0.77 ATR away |
| **Key resistance** | **234.66** → 238.35–242.45 (gap) → 238.64 → 243.3–243.5 → 247.72 | Overhead stack | Unfilled 07-23 gap is the pivotal zone |
| **Bias** | Tactically bearish; strategically undecided | — | Sell rallies into 237.8–239.0 / 242.5–243.5; long only on a 238.64 reclaim or a 226–228.5 flush with a 225.30 stop |
| **Invalidation** | Close > 240 (bear off) · close < 225.55 (bull off) | — | 2.1% bracket between LB and 200 SMA resolves next |

**Bottom line:** AMZN is a stock that spent five months round-tripping and is now compressing at the bottom of its range with every moving average overhead and volume pointing the wrong way for bulls. The trend of the last four sessions is down, but the *location* (0.45% off the lower Bollinger band, RSI 36.5, ATR contracting) is precisely wrong for initiating fresh shorts. The disciplined play is patience: let price choose between a bounce into 238–243 (a shorting opportunity) and a break of 225.55 (a continuation trigger). Nothing in the verified data justifies a full-size directional position at 230.86 today.