# AAPL — Technical Analysis Report
**Analysis date: 2026-08-18 (verified snapshot) · Instrument: AAPL · Company: Apple Inc.**

---

## 1. Verified Snapshot — Single Source of Truth

The `get_verified_market_snapshot` output for **2026-08-18** is the authoritative data point used throughout this report. It agrees exactly with the per-indicator time series returned by `get_indicators` (no conflicts to flag).

| Field | Value (2026-08-18) |
|---|---|
| Open | 307.58 |
| High | 311.49 |
| Low | 305.74 |
| **Close** | **310.03** |
| Volume | 53,424,500 |
| close_10_ema | 308.99 |
| close_50_sma | 309.13 |
| close_200_sma | 280.87 |
| macd / macds / macdh | −2.459 / −0.800 / −1.659 |
| rsi | 47.86 |
| boll / boll_ub / boll_lb | 316.49 / 342.68 / 290.30 |
| atr | 7.51 |
| vwma | 309.70 |
| MFI (as reported) | 0.417 |

> **Data-integrity note:** the snapshot reports MFI as **0.417348** (a 0–1 scale) rather than the conventional 0–100 scale, so I am deliberately *not* selecting or interpreting it as a money-flow reading. Every other field cross-checks cleanly against the indicator series.

---

## 2. Regime Diagnosis: A Violent De-Risking Inside an Intact Primary Uptrend

The defining event in the current tape is **2026-07-31**: AAPL closed at 333.43 on 2026-07-30 and then printed an open of 304.81, a low of 300.00, and a close of **308.91** on 2026-07-31 — a **−24.52 point (−7.35%)** single-session close-to-close decline on **132,489,100 shares**, roughly 2.5× the ~50M share norm of the preceding weeks. Because the 07-30 low (329.59) and the 07-31 high (310.69) do not overlap, this also left an **unfilled gap band of 310.69 → 329.59** directly above the current price.

Since that day, the market has done exactly two things:
1. **Stabilized** in a defined range: closes from 2026-08-03 through 2026-08-17 have all landed between **302.25 (2026-08-12)** and **313.33 (2026-08-07)**.
2. **Began to repair**, culminating in the 2026-08-18 session: close **310.03** after an open of 307.58, high 311.49, low 305.74 — closing in the **upper ~75% of the day's 5.75-point range** on **53.4M shares**, the heaviest volume in ten sessions.

So the correct framing is **not** "bear market" and **not** "new uptrend." It is **a post-shock base-building phase inside a still-rising long-term trend, sitting precisely at a cluster of moving averages that will decide the next leg.**

---

## 3. Indicator Selection (8 selected)

| # | Indicator | Why it earns a slot in *this* context |
|---|---|---|
| 1 | **close_200_sma** | Establishes whether the July break was a trend change or a correction. At 280.87 it definitively answers that question. |
| 2 | **close_50_sma** | Currently **flat** at 309.13 and sitting within 0.3% of price — the single most important decision level on the chart. |
| 3 | **close_10_ema** | Short-term slope. It has been falling since 07-30 and just produced its first uptick — timeliest available turn signal. |
| 4 | **macd** | Captures the momentum *regime* shift: above zero all July, negative since 08-11. |
| 5 | **macdh** | The histogram is the actionable part: contraction from −3.63 to −1.66 while MACD is still below zero = decelerating downside momentum, the earliest mechanical evidence of a turn. |
| 6 | **rsi** | Confirms that the overshoot was in *price* (71+ on 07-16/17) but never in *momentum* — and quantifies the current neutral reset. |
| 7 | **atr** | Essential here: an ATR of 7.51 (2.42% of price) after a 9.87 spike sets stop distance and position size objectively. |
| 8 | **vwma** | The volume-weighted cost basis is the key tell on whether the 07-31 supply is being absorbed or distributed. |

**Deliberately excluded:** `macds` (the signal line is informational but its information is fully contained in `macdh`); `boll_ub`/`boll_lb` as *formal selections* — I reference the 316.49 / 290.30 levels from the verified snapshot as supporting context, but 20-day band width is largely duplicative of ATR for the volatility role. No oscillators beyond RSI, to avoid the redundancy trap (no StochRSI, no second momentum oscillator).

---

## 4. Trend Structure: Three Timeframes, Three Different Answers

**Long term (close_200_sma = 280.87) — bullish and strengthening.**
Price at 310.03 sits **29.16 points (+10.38%)** above the 200-day. The 200-day itself is rising monotonically: 279.41 on 2026-08-07 → 280.87 on 2026-08-18, gaining roughly 0.2 points per session. Critically, the 50-day (309.13) is **28.26 points above** the 200-day, so the golden-cross configuration established earlier in 2026 (the 50-day was already above the 200-day by 2026-04-20 at 260.51 vs 252.44) is widening, not compressing. **Nothing in the July drawdown damaged the primary trend.** For the 200-day to be tested, AAPL would need another ~9.4% decline.

**Medium term (close_50_sma = 309.13) — flat, and that is the story.**
The 50-day has effectively gone horizontal: 309.79 (2026-08-07) → 309.70 (08-10) → 309.56 (08-11) → 309.48 (08-12) → 309.28 (08-13) → 309.19 (08-14) → 309.08 (08-17) → 309.13 (08-18). It is drifting down by fractions of a point per day. A flattening 50-day after a sharp decline is textbook **transitional** behavior — the prior uptrend impulse has been neutralized but no downtrend has been established. Price at 310.03 is **+0.90 points (+0.29%)** above it — technically a reclaim, but only by a hair. This is a coin flip that will resolve.

**Short term (close_10_ema = 308.99) — first genuine inflection.**
The 10-EMA tells the more useful story. It topped at **331.31 on 2026-07-30** and declined without interruption to **308.76 on 2026-08-17** — nineteen consecutive lower values. On **2026-08-18 it ticked up to 308.99**, the first positive change in that sequence. Price at 310.03 is **+1.04 points (+0.34%)** above it. Short-term momentum has, for the first time since the gap, stopped deteriorating.

**The confluence is the point.** Three independent averages — 10-EMA (308.99), 50-SMA (309.13), VWMA (309.70) — have compressed into a **0.71-point band**, and the 2026-08-18 close of 310.03 is **above all three simultaneously**. Price reclaiming a tightly-clustered average stack after a shock is one of the more reliable "supply absorbed" configurations. But it is a *one-session* reclaim on 53M shares — it needs follow-through.

---

## 5. Momentum: Decelerating Downside, Not Yet Uptrend

**MACD — regime change is real.** The MACD line peaked at **9.61 on 2026-07-29**, collapsed to 6.89 on 07-31, and crossed **below zero on 2026-08-11 (−0.827)**. It bottomed at **−2.676 on 2026-08-17** and ticked up to **−2.459 on 2026-08-18** — again, the first uptick. The signal line continues to fall (0.187 on 08-14 → −0.385 on 08-17 → **−0.800 on 08-18**), which is why a **bullish MACD crossover has not yet occurred and is not in the data**. On current trajectories the two lines converge around the −1.3 to −1.5 area within roughly 3–5 sessions if price holds ~310.

**MACD histogram — the most constructive signal on the chart.** Readings: −1.365 (07-31) → −2.978 (08-03) → **−3.634 (08-05, trough)** → −3.476 (08-06) → −3.181 (08-07) → −3.189 (08-10) → −3.271 (08-11) → −3.343 (08-12) → −3.035 (08-13) → −2.648 (08-14) → −2.290 (08-17) → **−1.659 (08-18)**. That is **five consecutive sessions of contraction** and a **54% reduction from the trough**. Translated: the *rate* of downside momentum loss has been cut in half. The histogram remains negative — so this is a "less bad," not a "good" — but it is the standard precursor to a zero-line cross.

**RSI — a notably shallow reset.** The critical observation: RSI reached **71.43 (2026-07-16)** and **71.65 (2026-07-17)** — genuinely overbought — immediately before the reversal. Yet during the entire −7.35% shock and its aftermath, **RSI never breached 30**. The lowest print was **40.22 on 2026-08-12**, with 40.34 on 08-03. RSI bottomed in the low-40s and has now recovered to **47.86 (2026-08-18)**, up from 43.41 on 08-17. Two readings follow:
- The July high was a **price overshoot against weakening momentum**, i.e. distribution into strength, not a healthy continuation.
- But the absence of an oversold reading during the flush means **the selling was contained** — thin panic, not a sustained de-rating. That is a mild positive.

At 47.86, RSI sits dead-center: **no oversold edge to buy, no overbought risk to sell.** It is the definition of a market waiting for a catalyst.

---

## 6. Volatility: Normalizing, Which Favors Range-Then-Break

**ATR (7.51, 2.42% of price).** The 07-31 gap exploded ATR from 8.06 (07-30) to **9.87 (07-31)**. It has decayed monotonically since: 9.78 (08-04) → 9.33 (08-06) → 8.96 (08-07) → 8.55 (08-12) → 8.22 (08-13) → 7.86 (08-14) → 7.64 (08-17) → **7.51 (08-18)**. This is a clean **eight-session volatility normalization**. Falling ATR inside a horizontal price range is the classic coil: energy being stored, not expended. It also has direct practical value — it is the objective basis for sizing (see §9).

**Bollinger context.** Middle band **316.49**, upper **342.68**, lower **290.30**; band width **52.38 points (16.55% of the mid-band)**; %B ≈ **0.38**. Price at 310.03 is **6.46 points (−2.04%) below** the 20-day mid-band, having been **+9.2% above it** on 2026-07-17 (close 333.74 vs mid 305.52). That is a complete mean-reversion round trip. Note that the band geometry is shifting *downward with price* — the lower band has fallen from 304.22 (07-31) to 290.30 while the upper has eased from 344.51 to 342.68 — so the bands are not yet contracting into a squeeze; they are being dragged. A close above 316.49 would be the first objective sign that the mid-band has been reclaimed and the July damage is being reversed.

---

## 7. Volume & Participation: The VWMA Test

This is where the evidence is most interesting and most cautionary.

**VWMA has been falling every single session since 2026-07-30 (329.58) to 2026-08-18 (309.70)** — twenty consecutive declines. Interpretation: the bulk of recent transacted volume occurred at *higher* prices. VWMA trading **above** spot for most of August (e.g. 320.94 on 08-06 vs close 312.41; 317.19 on 08-12 vs close 302.25) means the average recent buyer was **underwater** — overhead supply from trapped longs, which caps rallies. That is genuine distribution pressure.

**But on 2026-08-18 the relationship inverted.** Close **310.03** vs VWMA **309.70** — price is **+0.33 points (+0.11%) above** the volume-weighted cost basis for the first time in this recovery. Combined with the 53.4M share volume (versus a ~51.9M twenty-session average that is itself inflated by the 132M and 75M shock days — i.e. ~20% above the true recent norm), and a close in the upper quarter of the daily range, the session reads as **constructive absorption**.

**Honest caveat:** 53.4M is *not* a conviction breakout volume. It is 40% of the 07-31 capitulation volume. One session above VWMA is a hypothesis, not a confirmation.

---

## 8. Key Levels — Evidence-Based

| Level | Price | Evidence (dated) |
|---|---|---|
| **Gap-fill target** | 329.59 | 2026-07-30 low; unfilled gap boundary |
| Resistance 3 | 323.45 | 2026-07-13 high |
| Resistance 2 | 321.66 | 2026-07-23 close |
| Resistance 1 | 316.49 | Bollinger mid / 20-SMA (2026-08-18) |
| **Immediate resistance** | **311.49 / 313.33** | 2026-08-18 high / 2026-08-07 close |
| **Spot** | **310.03** | 2026-08-18 close |
| **Pivot cluster** | **308.99 – 309.70** | 10-EMA / 50-SMA / VWMA (2026-08-18) |
| Range floor | 302.25 | 2026-08-12 close |
| **Critical support** | **300.00 – 300.57** | 2026-07-31 low / 2026-08-12 low |
| Support 2 | 290.30 | Bollinger lower band |
| Major support | 280.87 | 200-SMA |
| Structural low | 273.75 | 2026-06-25 low |

---

## 9. Actionable Plan

**Base case (highest probability): continued 300–316 range, resolving higher.** Rationale: falling ATR, RSI at 47.9, flat 50-SMA, 10-EMA turning up, histogram contracting five straight sessions, price above the average cluster. Nothing here supports a directional bet *today* — but the asymmetry is upward.

**Bull scenario — triggers and ladder:**
- **Trigger:** a daily close above **311.49** (2026-08-18 high), ideally **above 313.33** (2026-08-07 close) on volume > 55M.
- **Confirmation:** MACD/macds crossover (currently −2.459 vs −0.800, converging).
- **Targets:** **316.49** (20-SMA) → **321.66–323.45** → **329.59** (gap boundary).
- **Stop:** **298.50** — below the 300.00/300.57 shelf *and* below 1.5×ATR (1.5 × 7.51 = 11.27; 310.03 − 11.27 = 298.76) from the current price. Placing it under both the structural floor and the ATR-derived level avoids noise stops.
- **Risk/reward from 311.50 entry:** risk 13.00; R:R ≈ **0.4 / 1.4 / 2.2** to the three targets.

**Bear scenario — triggers:**
- **Trigger:** a daily close below **300.00**. That would invalidate the 08-18 reclaim of the 10-EMA/50-SMA/VWMA cluster and confirm the base as a distribution shelf.
- **Targets:** **290.30** (lower band) → **280.87** (200-SMA, the long-term line in the sand) → **273.75** (2026-06-25 low).
- Note the 50-SMA would then be *above* price and rolling over — the mechanical setup for a medium-term downtrend.

**Do-nothing zone:** **302.25 – 311.49.** This is where 11 of the last 12 sessions have closed. Trading inside it means paying the spread for noise; ATR of 7.51 means a normal day spans ~2.4% and will stop out tight positions on both sides.

**Sizing.** With ATR at 7.51 (2.42% of 310.03), a 1-ATR adverse move costs 2.4%. At a 1% account risk per trade and a 13.00-point stop, position size = (0.01 × Equity) / 13.00 per share. Prefer **half size** until either 311.49 breaks with volume or 300.00 breaks — the flat 50-SMA is genuinely unresolved.

**For existing longs:** the 200-SMA at 280.87 gives ~9.4% of room before the primary trend is even questioned; use 298.50 as a tactical (not strategic) exit and consider re-entry on a confirmed 316.49 reclaim. **For short sellers:** the setup is late — five sessions of histogram contraction and a reclaimed average cluster make fresh shorts at 310 a poor location; wait for a 300.00 break.

---

## 10. Nuances, Risks, and What Would Change My Mind

1. **The 07-31 gap is the single dominant chart feature.** An unfilled 18.90-point gap (310.69 → 329.59) is both the bull target and the bear's reminder that the shock was never repaired. Until 310.69 is cleared and held, the drawdown remains "open."
2. **The absent oversold reading is double-edged.** RSI never hit 30 — bullish (contained selling) but also bearish (no capitulation flush to mark a durable low). The 07-31 volume spike of 132.5M is the closest thing to a climax print.
3. **Volume is the weakest link in the bull case.** 53.4M on 08-18 is unremarkable. A move through 311.49–313.33 on <45M would be a low-quality breakout.
4. **VWMA declining 20 straight sessions** is real overhead supply. One session above it does not erase it.
5. **No historical/backtest validation is claimed.** Every level and reading above derives from the frozen rows dated 2025-11-03 through 2026-08-18 and the verified 2026-08-18 snapshot; no statement about how AAPL behaved at these levels in prior cycles is asserted.
6. **Dividend/total-return note:** the frozen data shows ex-dividend cash amounts of 0.26 (2025-11-10), 0.26 (2026-02-09), 0.27 (2026-05-11) and 0.27 (2026-08-10). The total-return index stands at **315.54 versus a close of 310.03**, so price-only readings understate holder returns modestly. Indicator values are computed on the price series, not the TR index.
7. **Discrepancy check:** snapshot and indicator series agree to six decimals on all 13 shared fields. The only anomaly is the **MFI scale (0.417)**, which I have excluded from interpretation rather than rescaling.

---

## 11. Summary Table

| Dimension | Reading (2026-08-18) | Signal | Evidence |
|---|---|---|---|
| **Primary trend** | Close 310.03 vs 200-SMA 280.87 = **+10.38%** | **Bullish** | 200-SMA rising daily (279.41 on 08-07 → 280.87); 50-SMA 28.26 pts above it |
| **Intermediate trend** | Close 310.03 vs 50-SMA 309.13 = **+0.29%** | **Neutral / unresolved** | 50-SMA flat: 309.79 (08-07) → 309.13 (08-18) |
| **Short-term momentum** | 10-EMA 308.99, first uptick after 19 declines | **Mildly bullish** | 331.31 (07-30) → 308.76 (08-17) → 308.99 (08-18) |
| **MACD regime** | MACD −2.459, signal −0.800, hist −1.659 | **Bearish but improving** | MACD below zero since 08-11; hist contracted 5 straight sessions from −3.634 (08-05) |
| **RSI** | 47.86 | **Neutral** | No oversold (<30) during the flush; low was 40.22 on 08-12; 71.65 overbought on 07-17 |
| **Volatility** | ATR 7.51 (2.42%) | **Normalizing / coiling** | 9.87 (07-31) → 7.51 (08-18), 8 straight declines |
| **Bollinger position** | %B ≈ 0.38; mid 316.49 / UB 342.68 / LB 290.30 | **Below mid, not extended** | Was +9.2% above mid on 07-17; now −2.04% below |
| **Volume-weighted basis** | VWMA 309.70 vs close 310.03 = **+0.11%** | **Tentative reclaim** | VWMA fell 20 straight sessions from 329.58 (07-30); first close above it |
| **Participation** | 53.42M shares, close at 74.6% of daily range | **Constructive but modest** | vs 132.49M on 07-31; ~20% above recent normal |
| **Structure** | Range 302.25 – 313.33 since 08-03 | **Base-building** | Unfilled gap 310.69 – 329.59 remains |
| **Bias** | Range-then-higher; long above 311.49, flat 302–311, short below 300.00 | **Cautiously bullish** | Confluence of 10-EMA/50-SMA/VWMA at 308.99–309.70 reclaimed |
| **Stop reference** | 298.50 (below 300.00 shelf and 1.5×ATR) | — | 1.5 × 7.51 = 11.27 |
| **Primary targets** | 316.49 → 321.66 → 329.59 | — | 20-SMA / 07-23 close / 07-30 low |
| **Primary downside risk** | 290.30 → 280.87 → 273.75 | — | Lower band / 200-SMA / 06-25 low |

**Bottom line for AAPL:** the July 31 gap did real technical damage but did **not** break the long-term trend — AAPL trades 10.4% above a rising 200-day. What has changed is the *character* of the tape: from trend-following to range-bound repair. The 2026-08-18 session is the most encouraging print since the shock (close 310.03, above the 10-EMA, 50-SMA and VWMA simultaneously, heaviest volume in ten sessions, MACD histogram contracting for a fifth day), but it is a single session, on unremarkable volume, with MACD still below zero and the signal line still falling. The disciplined posture is **half-size long bias above 311.49 with a 298.50 stop, flat inside 302–311, and no fresh short until 300.00 fails.**