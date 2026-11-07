# AMZN — Multi-Timeframe Technical Report
**Analysis date: 2026-07-16 (last completed session: 2026-07-16)**
**Verified close: $249.89 | Session range $248.00–$258.08 | Volume 45,343,700**

---

## 0. Data integrity check

The `get_stock_data` pull (2026-01-01 → 2026-07-16, 134 rows) and the `get_verified_market_snapshot` (30-row lookback) agree row-for-row on the OHLCV series, including the 2026-07-16 bar (O 255.12 / H 258.08 / L 248.00 / C 249.89 / V 45.34M). **No discrepancy to flag.** All indicator values below are taken from the verified snapshot and the indicator service, which are internally consistent.

---

## 1. Trend hierarchy: long-term up, medium-term repairing, short-term at a decision point

**Long-term (bullish, intact).** AMZN closed at $249.89 versus a 200-day SMA of **$233.94**, i.e. **+6.8% above it**, and the 200-SMA is still grinding higher (233.03 on 2026-07-06 → 233.94 today). The 50-SMA ($252.66) remains above the 200-SMA, so the structural bullish stack persists. The whole of 2026's February low (intraday $200.31 on 2026-02-06) through to the present fits an uptrend whose *higher-degree* structure has not broken.

**Medium-term (neutral-to-repairing).** This is the nuance in the chart. The 50-SMA **peaked at $257.10 on 2026-06-18 and has rolled over every session since**, printing $252.66 today. Price is now **1.1% below the 50-SMA**. That rollover is the technical scar from the June decline: 274.99 close (2026-05-06) → 274.00 close (2026-05-28) → 227.01 close (2026-06-25), a **-17.5% drawdown from the 2026-05-28 close and -19.0% from the 2026-05-05 intraday high of $278.56**.

**Short-term (improving, but just got tested).** Since the 2026-06-25 capitulation close ($227.01; intraday low $225.55), price has built a clean sequence of **rising lows and rising highs**:

| Swing | Date | Price |
|---|---|---|
| Low | 2026-06-25 | 225.55 (intraday) |
| Low | 2026-07-08 | 240.52 |
| Low | 2026-07-14 | 243.80 |
| Low | 2026-07-16 | 248.00 |
| High | 2026-06-29 | 249.71 |
| High | 2026-07-15 | 256.48 |
| High | 2026-07-16 | 258.08 |

That is **+10.1% off the 2026-06-25 close** (227.01 → 249.89) and **+14.4% off the 2026-06-25 low** to the 2026-07-16 high (225.55 → 258.08). The pattern is a *recovery channel inside a larger 227–278 consolidation*, not a new breakout leg — yet.

**YTD context:** +10.3% from the 2026-01-02 close of $226.50; +18.8% from the 2026-02-06 panic low close of $210.32.

---

## 2. Selected indicators (8) and why

Given a **post-correction repair phase inside a long-term uptrend, with a fresh rejection candle at a declining 50-SMA**, the relevant questions are: (a) is the long-term trend still valid, (b) is momentum actually turning or just bouncing, (c) where is the volatility envelope, and (d) is volume confirming? The eight selected indicators answer exactly those:

**1. close_200_sma — the trend anchor.** $233.94 and rising. It defines the line in the sand: an -6.4% move from here would be needed to break the primary uptrend. Any long thesis is "buying dips within an uptrend," and this indicator is what makes that framing valid rather than hopeful.

**2. close_50_sma — the battleground.** $252.66 and falling for ~20 sessions. This is the single most informative level on the chart right now because price *just reclaimed it and lost it within one session* (see §4). A flattening/turning 50-SMA would be the first confirmation the June damage is repaired.

**3. macd — the momentum turn.** MACD line **-6.88 (2026-06-26) → +0.57 (2026-07-16)**, crossing zero on 2026-07-15. This is a genuine regime shift in momentum, not noise: 13 consecutive rising readings.

**4. macds — the signal line, needed to date the crossover.** Signal sits at **-1.378**, so the MACD line crossed **above** it around 2026-07-14/15. Without the signal line the crossover cannot be dated or validated.

**5. rsi — momentum quality and headroom.** **54.19**, up from **33.63 on 2026-06-25** and a local peak of **60.14 on 2026-07-15**. Crucially, RSI is *not* overbought, meaning the recovery has room — but it has also failed to reach 60+ on the strongest day, i.e. momentum is moderate, not impulsive.

**6. boll_ub — the breakout/mean-reversion boundary.** **$255.38**, versus price at $249.89. On 2026-07-15 price closed *above* the then-upper band ($254.80) — a classic "walk the band" signal — and on 2026-07-16 the band rejected price from above. This is the cleanest, objective resistance marker available. (Bollinger middle = $241.57 and lower band = $227.76 round out the envelope; the width is (255.38 − 227.76)/241.57 = **11.4% of price**.)

**7. atr — volatility-calibrated risk.** **$7.66**, ~**3.07% of price**, and contracting from $8.59 on 2026-06-29. Volatility is cooling as the June panic fades, which supports tighter, more precise stops and larger position sizes than would have been appropriate three weeks ago.

**8. vwma — volume-weighted confirmation.** **$240.52** and rising steadily from a flat ~$236.5 print through late June/early July. Price at $249.89 sits **+3.9% above VWMA**, which means buyers are paying up relative to where volume actually transacted — a genuinely constructive signal, *but* VWMA at $240.52 also marks the line below which the recovery would be volume-invalidated.

Deliberately excluded: `boll`/`boll_lb` as separate picks (redundant with `boll_ub` given the envelope is fully described by band width), `macdh` (fully derivable from macd/macds — I use it qualitatively below), `close_10_ema` (useful, cited in §5, but overlaps with VWMA/middle band for short-term level work).

---

## 3. The 2026-07-16 candle is the story of the week

This is where precision matters. The July 16 bar:

- **Open $255.12** (gap up from $254.96 close), **High $258.08**, **Low $248.00**, **Close $249.89**
- **Close is only 18.8% up from the day's low** — i.e. it closed in the **bottom fifth of its range**
- Range ($10.08) **fully engulfed** the 2026-07-15 range ($249.75–$256.48) — an **outside day**
- Net change **-1.99%** from the prior close
- Volume **45.34M**, which is ~88% of the 20-session average *excluding* the 2026-06-26 index-rebalance print of 248.37M (the raw 20-day average is ~61.3M, distorted by that single day)

Two readings, and an honest report must hold both:

**Bearish reading:** price was rejected at precisely the confluence of the declining 50-SMA ($253.10 on 7/15, $252.66 today) and the Bollinger upper band ($254.80 → $255.38), then closed back inside the envelope. July 15's close above the 50-SMA — the **first close above that average since 2026-06-02** — was undone in a single session. That is textbook failed-breakout behaviour, and it caps the near-term upside at $255–258.

**Bullish reading:** the rejection happened on **unremarkable volume** (~88% of the ex-rebalance 20-day norm), not on heavy distribution like the 60–78M prints of 2026-06-22 to 06-25. And the low held **$248.00**, still above the 10-EMA ($247.03) and far above the $240.5–241.6 support cluster. Nothing in the momentum complex broke: MACD stayed positive, RSI stayed >54.

**The one genuine caveat:** MACD histogram (macd − macds) **contracted from 2.124 (7/15) to 1.947 (7/16)** — small, but it is the first contraction in nine sessions and it is directionally consistent with the reversal candle.

---

## 4. Momentum detail — a real turn, decelerating at the edge

The MACD recovery is unusually clean and worth quantifying:

| Date | MACD | Signal | Hist |
|---|---|---|---|
| 2026-06-25 | -6.875 | -5.129 | -1.746 |
| 2026-07-02 | -4.386 | -5.302 | +0.916 |
| 2026-07-09 | -1.903 | -3.714 | +1.810 |
| 2026-07-15 | +0.260 | -1.864 | +2.124 |
| 2026-07-16 | +0.569 | -1.378 | +1.947 |

- Histogram flipped positive on/around **2026-07-01** (bullish momentum established)
- MACD line crossed **zero on 2026-07-15** (bullish trend confirmed)
- Histogram **peaked 2026-07-15** and ticked lower on 2026-07-16

RSI tells the same story in a different dimension: a textbook sub-35 washout (33.63 on 2026-06-25) followed by a 26-point round-trip to 60.14. The **absence of a bearish RSI divergence at the July highs is a positive** — the June low was an oversold exhaustion, not a momentum trap. And at 54.19, RSI has ~16 points of headroom before overbought becomes an issue.

---

## 5. Volume profile: constructive but thin

The lift from 2026-06-29 to 2026-07-16 has occurred on **light volume**:

- 2026-06-22 → 2026-06-26 average: **~105.0M** (five sessions, including the 248.37M rebalance)
- 2026-06-01 → 2026-06-30 average: **~62.6M** (21 sessions); **~53.3M** excluding the rebalance day
- 2026-07-01 → 2026-07-16 average: **~39.8M** (11 sessions)

July volume is roughly **25% below** June's ex-rebalance average. VWMA at $240.52 versus the current price is the useful synthesis: the volume-weighted center of trading is rising and price is above it (**+3.9%**), which is bullish — but the *magnitude* of July participation does not yet confirm an institutional accumulation phase. Treat the rally as **credible but unconfirmed**.

Worth noting for event risk: the tape has a history of gap dislocations — **2026-02-06** opened at $202.70 vs a $222.69 prior close (**-9.0% gap**, 179.2M shares) and **2026-02-05** already traded 103.5M shares; **2026-04-08** gapped +4.7% (223.79 vs 213.77); **2026-04-30** opened +3.85% (273.17 vs 263.04) and closed at just +0.77%. Any stop placed tight to price is exposed to these. This is a structural argument for ATR-based rather than percentage-based stops.

---

## 6. Level map (all levels derived from verified tool output)

**Resistance (ascending):**
| Level | Source |
|---|---|
| $252.66 | 50-SMA (declining) |
| $255.38 | Bollinger upper band |
| $256.48 / $258.08 | 2026-07-15 / 2026-07-16 highs |
| $262–$266 | April–May congestion: 263.99 close (4/24), 265.06 close (4/30), 263.04 close (4/29), 266.32 close (5/22) |
| $273–$278.56 | May highs: 273.88 (4/30 high), 274.75 (5/29 high), 276.10 (5/4 high), 278.56 (5/5 high) |

**Support (descending):**
| Level | Source |
|---|---|
| $248.00 | 2026-07-16 low |
| $247.03 | 10-EMA |
| $240.52–$241.57 | VWMA / Bollinger middle — **key cluster** |
| $233.94 | 200-SMA |
| $232.79 / $227.01 / $225.55 | June swing closes and low |

The **$240.5–$241.6 cluster** is the most important structure on the chart: if the pullback stops there with the MACD histogram still positive, the July advance is a legitimate higher-low base. A daily close below it flips the short-term bias back to bearish and re-opens $233.94.

---

## 7. Scenarios with explicit triggers

**Scenario A — Breakout continuation (probability-weighted as the primary case, ~45%).**
Trigger: a **daily close above $255.38–$258.08 on volume ≥50M** (i.e. clearly above the ~40M July norm). Confirmation: MACD histogram re-expands above 2.12. Target sequence: $262–266 congestion first, then $273–278. Invalidation: any close back below $247.

**Scenario B — Controlled pullback / higher-low construction (~35%).**
Trigger: drift into **$247.03 (10-EMA) → $240.52–$241.57 (VWMA / mid-band)** on contracting volume with MACD histogram remaining positive. This is the *highest-quality entry zone* for swing longs because the stop can sit under $240.5 with the 200-SMA at $233.94 as a deep backstop. A close below $240.5 with a negative histogram converts this to Scenario C.

**Scenario C — Failed bounce / retest of the base (~20%).**
Trigger: daily close below **$240.52** *and* MACD histogram flipping negative. Path opens to the **200-SMA at $233.94**, and below that the June shelf at $232.79 / $227.01 / $225.55.

---

## 8. Risk management and trade structuring

- **ATR = $7.66 (3.07% of price).** A standard 1.5×ATR stop is **~$11.50**; a 2×ATR stop is **~$15.33**.
- **Long from the $247–$249 area:** stop under $240.5 (below the VWMA/mid-band cluster) ≈ **$8.50–$9.50 risk**, i.e. ~1.2×ATR — tight but defensible given volatility is contracting. First target $255.4 (Boll upper band), second $262. Reward/risk roughly 0.7:1 to first target, ~1.7:1 to second. **Weak R:R at market — do not chase here.**
- **Long on a confirmed breakout above $258.08:** stop 1.5×ATR below entry (~$11.5), target $266. R:R ~0.7:1 initially — again, the geometry argues for waiting for either a pullback (Scenario B) or buying strength only with a wider target at $274.
- **Best R:R setup:** Scenario B entry at $241.5–$247.0 with a stop at $239.5 and a $262–266 target → **~2.5:1 to 3.5:1.** This is the trade the current structure actually offers.
- **Position sizing:** with a 2×ATR ($15.33) stop, risking 1% of equity implies a position size of ~0.065% of equity per $1 move — i.e. size roughly 40% smaller than a low-volatility regime (ATR was $7.33 on 2026-06-16, $8.59 on 2026-06-29) would allow.
- **Gap risk:** given the -9.0% gap on 2026-02-06 and the +4.7% gap on 2026-04-08, avoid holding full size into known event dates; stops do not protect against gaps.

---

## 9. Summary table

| Dimension | Reading (2026-07-16) | Signal | Actionable takeaway |
|---|---|---|---|
| **Price** | Close $249.89, -1.99% d/d; range $248.00–$258.08 | Bearish reversal candle (outside day, close in bottom 19% of range) | Do not chase; wait for either $258+ confirmation or a pullback |
| **Long-term trend** | 200-SMA $233.94 (+6.8% above), rising; 50>200 | **Bullish** | Primary bias remains long; -6.4% needed to break it |
| **Medium-term trend** | 50-SMA $252.66, declining since 2026-06-18 ($257.10 peak) | **Bearish / overhead supply** | A close above $252.66 is the first repair signal |
| **Short-term trend** | 10-EMA $247.03; rising lows 225.55 → 240.52 → 243.80 → 248.00 | **Bullish** | Trend of higher lows intact as long as $248 holds |
| **Momentum (MACD)** | MACD +0.569 vs signal -1.378; hist +1.947 (peaked 2.124 on 7/15) | **Bullish, decelerating** | Zero-cross 7/15 confirmed; watch hist for re-expansion |
| **Momentum (RSI)** | 54.19 (from 33.63 on 6/25; peak 60.14 on 7/15) | **Neutral-bullish, room to run** | No divergence; not overbought |
| **Volatility (Boll)** | UB $255.38 / mid $241.57 / LB $227.76; width 11.4% | **Envelope rejection at UB** | $255.4–$258.1 caps upside; $240.5–241.6 is the floor of the recovery |
| **Volatility (ATR)** | $7.66 (~3.07%), contracting from $8.59 (6/29) | **Cooling** | 1.5×ATR stop ≈ $11.5; 2×ATR ≈ $15.3 |
| **Volume** | 45.34M on 7/16 vs ~39.8M July avg vs ~62.6M June avg | **Unconfirmed rally** | Rally on light volume; want ≥50M on a breakout |
| **VWMA** | $240.52, rising; price +3.9% above | **Constructive** | Losing $240.5 invalidates the July advance on a volume basis |
| **Key support** | $248.00 → $247.03 → $240.52–241.57 → $233.94 → $227.01 | — | $240.5 is the line that matters |
| **Key resistance** | $252.66 → $255.38 → $256.48–258.08 → $262–266 → $273–278.56 | — | Break needs volume ≥50M |
| **Best setup** | Buy $241.5–$247.0, stop $239.5, target $262–266 | **~2.5–3.5:1 R:R** | Superior to chasing at $249.89 |
| **Primary risk** | Failed 50-SMA/Boll-UB reclaim on 2026-07-16; declining 50-SMA; light-volume rally; gap-prone history (-9.0% on 2026-02-06) | — | Weekly close below $240.52 = exit longs |

---

## Bottom line

AMZN is **not** in a downtrend and **not** in a clean breakout — it is in the **transition zone where a post-correction repair meets a declining 50-SMA ($252.66) and the upper Bollinger band ($255.38)**. The bullish evidence is real and multi-dimensional: MACD has crossed both its signal line and the zero line, RSI has climbed from 33.6 to 54.2 without becoming overbought, lows are rising (225.55 → 240.52 → 243.80 → 248.00), price sits above the 10-EMA, the VWMA, the Bollinger mid-band and the 200-SMA, and ATR is contracting. The bearish evidence is equally specific: the 2026-07-16 session rejected the breakout with an outside-day reversal that closed in the bottom fifth of its range, the 50-SMA has been falling for a month, and July's advance has come on roughly 25%-lighter volume than June. **The trade is to be patient: accumulation belongs in the $241.5–$247 zone with a stop below $239.5, and breakout entries should only be taken on a close above $258.08 with volume at or above 50M.** A daily close below $240.52 flips the short-term bias back to bearish and re-targets the 200-SMA at $233.94.