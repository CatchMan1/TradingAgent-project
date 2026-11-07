# AMZN — Technical Analysis Report
**As of:** Friday, 2026-08-28 (latest settled session in the data)
**Verified snapshot price:** Close **266.43** (O 258.32 / H 267.56 / L 257.78), Volume **49.55M**

---

## 1. Data integrity check

I pulled 206 sessions of OHLCV (`get_stock_data`, 2025-11-03 → 2026-08-28) and the verified snapshot for 2026-08-28. **The two sources are identical row-for-row for the recent window** — no discrepancy to flag. Also note: get_stock_data contains 206 rows but the snapshot's indicator set is the authoritative source for exact current indicator values; where I quote history for an indicator I use the `get_indicators` series, and where I quote a current value I use the snapshot (they agree, e.g., close_50_sma 251.6592 in both, RSI 55.852184 in both).

One data-quality observation worth flagging: **AMZN gapped enormously between 2026-07-30 (close 235.50) and 2026-07-31 (open 265.00, close 271.58, volume 129.05M)** — a +12.5% open-vs-prior-close gap on ~3.4x the recent 20-day average volume. This is almost certainly an earnings-type repricing event. Every moving average, MACD and Bollinger reading on the current chart is being distorted by that single discontinuity, so I weight structure (pre-gap vs post-gap) alongside the smoothed indicators rather than relying on them in isolation.

---

## 2. Indicator selection and rationale (8 indicators, non-redundant)

| Indicator | Why it earns a slot in *this* market context |
|---|---|
| **close_50_sma** (251.66) | The medium-term trend anchor. Critical here because the 50-SMA *rolled over* from 257.10 (2026-06-18) to a trough of 246.38 (2026-07-30) and has now turned back up to 251.66. That inflection is the single cleanest read on whether the post-gap advance is a genuine trend resumption or a failed spike. |
| **close_200_sma** (238.68) | Long-term regime filter. Rising steadily (+3.0% since 2026-06-01) and ~28 points below price, confirming a structural bull regime. Stops me from mistaking an 8-day pullback for a trend change. |
| **close_10_ema** (261.93) | Fast-touch mean reversion/entry timing. Price was **below** this line for six straight sessions (2026-08-20 → 08-27) and reclaimed it on 2026-08-28, and the EMA itself ticked up for the first time since 2026-08-12. That is the earliest short-term turn signal available. |
| **macd** (2.086) | Momentum regime. Macd peaked at 8.432 on 2026-08-11 and decayed to 1.796 on 2026-08-27 before ticking up on 2026-08-28. Tells me the impulse is *fading but stabilising*, not dead. Signal/histogram from the snapshot (macds 3.200, macdh **−1.114**) show the crossover state is still bearish — an honest, non-confirming read. |
| **rsi** (55.85) | Overbought/oversold and reset quality. RSI hit 72.23 on 2026-08-03 (overbought), mean-reverted to 47.23 by 2026-08-27 without breaking 30, and snapped back to 55.85. A *reset* from overbought that holds neutral-to-strong is a classic continuation signature. |
| **boll_ub** (282.21) | Upper volatility envelope. Contracting hard from 296.99 (2026-08-19) → 282.21 (2026-08-28) while price based — this quantifies the volatility compression and gives a defined upside objective. (Bollinger middle 266.88 and lower 251.56 are taken from the verified snapshot to complete the band structure.) |
| **atr** (7.04) | Position sizing and stop placement. ATR expanded to 9.99 on 2026-08-05 (post-gap) and has since compressed to 7.04 — **2.64% of price**. That contraction is the most actionable risk fact on the page: stops must be wide enough to survive ~7 points of noise, but the regime is normalising, permitting larger size than two weeks ago. |
| **vwma** (263.06) | Volume-weighted confirmation. Distinguishes a low-conviction drift from real accumulation. VWMA rolled up to 272.05 (2026-08-20) then slipped to 263.06, and price closed **back above it** on 2026-08-28 — a volume-weighted reclaim, which is a materially stronger signal than a simple MA reclaim. |

*Deliberately excluded:* `macds`/`macdh` as separate calls (redundant with `macd` + snapshot values), `boll`/`boll_lb` as separate series (snapshot-supplied), and any stochastics (duplicative of RSI).

---

## 3. Trend structure

### 3.1 Long-term: intact bullish
- Close 266.43 sits **+11.6% above** the 200-SMA (238.68) and **+5.9% above** the 50-SMA (251.66).
- 50-SMA (251.66) > 200-SMA (238.68) — the bullish alignment has been uninterrupted across the entire window I pulled.
- The 200-SMA has risen every single session since 2026-06-01 (231.70 → 238.68), so the long-term slope is genuinely positive, not flat.

### 3.2 Intermediate: a genuine inflection, not a dead-cat
- The 50-SMA bottomed at **246.384 (2026-07-30)** and has climbed to **251.659 (2026-08-28)** — twelve consecutive sessions of rising values. This is the strongest structural fact in the report: the medium-term average *turned up* underneath a consolidating price.
- Price action since the gap: **2026-07-31 high 273.23 → 2026-08-03 high 287.20 → 2026-08-10 high 280.14 → 2026-08-19 high 266.40 → 2026-08-28 high 267.56.** That is a clear sequence of *lower highs* — the market has been digesting the gap, and the burden of proof sits with the bulls to break the pattern.

### 3.3 Short-term: the turn happened today
The 2026-08-28 session is the most important candle in the recent window:
- Opened 258.32, dipped only to 257.78 (holding above the 2026-08-27 low of 255.02), then closed at **266.43 — 88% of the way up the day's range** (range 257.78–267.56).
- Close-to-close: **+3.97%** (256.26 → 266.43). Open-to-close: **+3.14%**.
- Volume **49.55M vs a ~38.2M average of the prior 20 sessions (~1.3x)** — an up day on expanding volume, which is the constructive counterpart to the declining volume during the 2026-08-12 → 08-27 drift (21.5M–35.9M).

Practical read: the pullback from 287.20 (2026-08-03) to 255.02 (2026-08-27) — a −11.2% high-to-low drawdown — has produced its first high-volume reversal day, and price has reclaimed both the 10-EMA and the VWMA in one session.

---

## 4. Momentum and volatility diagnostics

**Momentum is stabilising, not yet confirmed.**
- MACD: 8.432 (2026-08-11 peak) → 1.796 (2026-08-27) → **2.086 (2026-08-28)**, first uptick in eleven sessions.
- BUT macd (2.086) remains **below** macds (3.200), histogram **−1.114**. The bearish crossover is technically *still in force*. A close above roughly the 3.2 signal level is what would flip this to a confirming signal.
- RSI 55.85 is the ideal middle ground: it reset from 72.23 (2026-08-03) to 47.23 (2026-08-27) **without ever touching 30**, and has room to run to 70 before becoming extended again. There is no RSI divergence claim I can substantiate here — on 2026-08-27 price made a lower low (255.02 vs 2026-08-18's 257.73) and RSI was also lower (47.2 vs 50.9), which is *consistent*, not divergent.

**Volatility is compressing — a resolution setup.**
- Bollinger band width: (282.21 − 251.56) / 266.88 = **11.5% of price**, with the upper band down 15 points from 296.99 (2026-08-19). Bands are squeezing.
- ATR 7.04 (2.64% of price), down from 9.99 on 2026-08-05. Post-gap volatility has largely normalized.
- Interpretation: post-earnings-gap digestion is complete-ish; the next directional move (whichever way) is likely to be a *range expansion* out of the 251.5–282.2 envelope rather than more chop inside it.

**Volume-weighted positioning is supportive.**
- VWMA 263.06 < close 266.43. The aggregate volume-weighted cost basis of the recent period sits *below* spot, meaning recent buyers are collectively in profit — a supportive, low-overhead condition.
- The huge 7/31 (129.05M) and 8/3 (90.83M) sessions established the current value area in the 265–284 zone; the 2026-08-28 close re-enters the bottom of that zone on better volume.

---

## 5. Actionable levels (all prices from tool output, with the date that produced them)

**Resistance**
1. **266.88** — Bollinger middle (snapshot). Price closed 266.43, i.e. **−0.17%**, effectively pinned at it. This is the immediate gate.
2. **267.56** — 2026-08-28 intraday high. A close above this confirms the reversal day followed through.
3. **272.05–274.48** — VWMA peak 272.05 (2026-08-20) and the 2026-08-06/08-07 closes (272.26 / 274.48). First real supply shelf.
4. **278.09–284.02** — 2026-08-10 close 278.09 and 2026-08-03 close 284.02 (the post-gap closing high).
5. **282.21** — Bollinger upper band; **287.20** — the 2026-08-03 intraday high (all-time-high proxy for this window).

**Support**
1. **263.06** (VWMA) and **261.93** (10-EMA) — a tight 1.1-point confluence cluster, just reclaimed. This is the "was it real?" line.
2. **255.02** — 2026-08-27 swing low, the lowest print since the gap.
3. **251.66 (50-SMA) / 251.56 (Bollinger lower)** — a near-perfect confluence shelf 0.10 points wide. This is the line in the sand for the intermediate uptrend.
4. **235.50–262.01** — the entirely unfilled gap void from 2026-07-30's close to 2026-07-31's low. A break of 251.5 puts this void in play; that is the tail-risk scenario.

---

## 6. Trading plans with defined risk

**Plan A — Momentum continuation (primary, bullish)**
- **Trigger:** daily close > **267.56** with volume ≥ ~40M (i.e., at least the recent average, ideally >1.3x).
- **Stop:** close below **261.9** (10-EMA). Risk from a 267.6 entry = **2.1%**.
- **Targets:** 273.5 (+2.2%, ~1.1R) → 278.1 (+3.9%, ~1.9R) → 282.2 Bollinger upper (+5.5%, ~2.6R).
- **Note:** Risk/reward is only adequate if the stop is the tight 10-EMA stop. Using a structural stop under 255.02 (risk 4.7%) against a 282 target (reward 5.4%) gives just ~1.1:1 — not worth it. **Prefer the tighter invalidation and smaller size.**

**Plan B — Pullback buy into support (higher quality R/R)**
- **Trigger:** retest of **262–263** (VWMA/10-EMA cluster) that holds on *declining* volume.
- **Stop:** close below **255.02** (2026-08-27 low). Risk = ~3.0%.
- **Target:** 272–274 shelf. Reward = ~4.2% → **~1.4:1**, acceptable. Add runner toward 282.2.

**Plan C — Invalidation / short bias**
- **Trigger:** close below **251.5** (50-SMA + lower Bollinger confluence). At that point the 12-session rise in the 50-SMA is negated, MACD would likely be deeply negative, and the 235.5–251.5 zone is the vacuum.
- **Avoid shorting the 262–267 zone** — that is where the volume-weighted demand and the fresh reversal candle sit.

**Risk management anchors**
- ATR = 7.04. Use **1.5× ATR ≈ 10.6 points** for swing stops (puts a 266.43 entry's stop at ~255.8 — which aligns almost exactly with the 2026-08-27 low of 255.02, a nice independent confirmation).
- Size positions so that a 2-ATR adverse move (≈14 points, 5.3%) is survivable.
- Position size *up* modestly from the 2026-08-05 regime (ATR 9.99) and *down* if ATR re-expands above ~9.

---

## 7. Nuanced caveats — what would make me wrong

1. **The bearish MACD crossover is unresolved.** macd 2.086 < macds 3.200, hist −1.114. One strong day does not repair an eleven-session momentum decay. Require the histogram to cross back positive before treating the uptrend as re-confirmed.
2. **The lower-high sequence (287.20 → 280.14 → 266.40) is still intact.** Until price prints a close above ~274.5, the post-gap pattern is technically distribution, not accumulation.
3. **One session is not a trend.** The 2026-08-28 candle is encouraging (88% close-in-range, 1.3x volume), but 2026-08-19 also produced a strong day (close 265.84 from 259.45, volume 35.8M) that failed within 24 hours (2026-08-20 close 260.11). Follow-through is the discriminator.
4. **The gap remains unfilled.** 235.50 → 262.01 is open air. Post-earnings gaps of this size are often revisited on a multi-week horizon; a failure at 267–274 keeps that risk live.
5. **RSI at 55.85 has no margin of safety either way** — it neither confirms breakout strength nor offers a dip-buy oversold entry. This is a "prove it" tape.

**Net assessment:** Constructive-to-bullish with a strict confirmation trigger. Trend alignment (price > 50-SMA > 200-SMA, both rising), a 50-SMA that has turned up for twelve straight sessions, a clean RSI reset, contracting volatility, and a volume-backed reclaim of the 10-EMA and VWMA all point higher. But momentum confirmation (MACD histogram) and price structure (lower highs) have **not** yet validated it — so buy the *confirmation at 267.56+* or the *retest at 262–263*, not the middle of the range.

---

## 8. Key metrics summary

| Metric | Value (2026-08-28) | Signal / Interpretation |
|---|---|---|
| Close | **266.43** | +3.97% d/d; closed at 88% of day's range |
| Day range | 257.78 – 267.56 | Held above 08-27 low (255.02) |
| Volume | **49.55M** | ~1.3x prior-20-session avg (~38.2M) — bullish expansion |
| close_10_ema | 261.93 | Reclaimed; first uptick since 08-12 → **short-term bullish** |
| close_50_sma | 251.66 | Rising 12 straight sessions from 246.38 (07-30) → **intermediate bullish** |
| close_200_sma | 238.68 | +3.0% since 06-01 → **long-term bullish** |
| Price vs 50/200 SMA | +5.9% / +11.6% | Trend alignment intact |
| macd / macds / macdh | 2.086 / 3.200 / **−1.114** | Below signal → **unconfirmed**, but first uptick in 11 sessions |
| RSI | 55.85 | Reset from 72.23 (08-03), never oversold → healthy, neutral-strong |
| Boll middle / upper / lower | 266.88 / 282.21 / 251.56 | Close pinned at middle band; bandwidth ~11.5% → **squeeze** |
| ATR | 7.04 (2.64% of price) | Down from 9.99 (08-05) → volatility normalizing |
| VWMA | 263.06 | Price above → volume-weighted demand confirmed on 08-28 |
| Structure | Lower highs 287.20 → 280.14 → 266.40 → 267.56 | Distribution pattern **not yet broken** |
| Key resistance | 266.88 / 267.56 / 272–274 / 278–284 / 282.21 / 287.20 | Break above 267.56 = confirmation trigger |
| Key support | 262–263 / 255.02 / **251.6 (50-SMA + lower band)** | Below 251.5 = thesis invalidated, gap void 235.5–251.5 opens |
| Unfilled gap | **235.50 – 262.01** (from 07-31) | Tail risk; not a base case |
| Primary bias | **Bullish, conditional on 267.56 close** | Preferred stop 261.9 (2.1% risk); 1.5×ATR ≈ 10.6 pts |
| Risk/reward | Plan A ~1.9–2.6R to 278–282; Plan B ~1.4R | Favor Plan B (retest 262–263) for cleaner R/R |

*All prices, volumes, and indicator values above are drawn from the `get_stock_data` series and the `get_verified_market_snapshot` for 2026-08-28; no percentage move, level, or "bounce" is asserted without a corresponding dated observation in that output.*