# AMZN — Multi-Horizon Technical Review (as of 2026-08-05)

## 1. Verified state of the tape

Source of truth: `get_verified_market_snapshot` for 2026-08-05. The latest visible session is **2026-08-05**, and it matches the last row of `get_stock_data` exactly (no discrepancy between the two tools — flagged and cleared).

| Field | Value (2026-08-05) |
|---|---|
| Open / High / Low / Close | 281.59 / 282.79 / 270.73 / **272.65** |
| Volume | 45,119,800 |
| Prior close (08-04) | 277.42 → **-1.72%** |
| Day range | 12.06 pts = 4.42% of close |
| Close location in range | **15.9%** (closed near the day's low) |
| Split / Dividend | 1.0 / 0.0 (no adjustment noise) |

Snapshot indicator values: `close_50_sma 247.315`, `close_200_sma 235.9505`, `close_10_ema 258.3422`, `macd 5.9988`, `macds 1.3796`, `macdh 4.6192`, `rsi 63.4898`, `boll 248.8745`, `boll_ub 281.4050`, `boll_lb 216.3440`, `atr 9.9827`, `vwma 253.8037`, `mfi 0.466476`.

**Data-integrity flag:** the snapshot's `mfi` prints as **0.466476**, which is not on the standard 0–100 Money Flow Index scale. I am excluding it as unreliable rather than reinterpreting it. Everything else cross-checks against the indicator series I pulled (`macd 5.998783`, `rsi 63.48977`, `atr 9.982704`, `vwma 253.803698` all match).

---

## 2. The defining event: a violent, volume-confirmed gap (2026-07-30 → 08-03)

This is not a normal trend; it is a **structural repricing** that reset every indicator. The dated sequence:

- **07-29:** close 226.65, RSI 33.31 — the stock was in a 5-session breakdown (244.85 on 07-22 → 226.65, **-7.4%**), heading toward the June lows (227.01 close on 06-25).
- **07-30:** volume 101.8M (vs ~35–45M typical), high 239.82, close 235.50 — pre-catalyst positioning.
- **07-31:** **open 265.00 vs prior close 235.50 = +12.53% gap open**; close 271.58 (+15.32%), low 262.01, volume **129,054,800** — the second-largest volume in the entire 189-session dataset.
- **08-03:** close **284.02** (+4.58%), intraday high **287.20**, volume 90.8M.
- **08-04:** 277.42 (**-2.32%**), volume 69.7M.
- **08-05:** 272.65 (**-1.72%**), volume 45.1M — volume down ~65% from the 07-31 peak; close in the bottom 16% of the day's range.

Two consequences that matter more than any oscillator:

1. **An unfilled gap band of 235.50 → 262.01 exists.** The 07-31 session's low (262.01) never revisited the prior close (235.50). Technically, that entire zone is un-traded. The bullish case requires that zone to stay unfilled; the bear tail risk is a full air-pocket retracement into it.
2. **The new-high breakout has not held on a closing basis.** Prior to 07-31, the highest *close* in the dataset was **274.99 (2026-05-06)** and the highest *high* was **278.56 (2026-05-05)**. The 08-03 close of 284.02 and high of 287.20 cleared both decisively — but 08-05's close of **272.65 is back below both** the 274.99 prior high close and the 278.56 prior high. As of today, the breakout is **unconfirmed**, and price is sitting *inside* the prior multi-month range's ceiling, not above it. That is the single most important nuance in this report.

---

## 3. Trend structure across three horizons (all bullish, but of very different quality)

**Long term (200 SMA = 235.95) — intact uptrend.** Price is **+15.55%** above the 200 SMA. The 200 SMA has been grinding higher without interruption: 232.24 (06-08) → 234.76 (07-30) → **235.95 (08-05)**. Persistent positive slope.

**Medium term (50 SMA = 247.32) — was deteriorating, now stabilizing.** The 50 SMA fell from **257.10 (06-18) to a low of 246.38 (07-30)**, a −10.7-point decline that was compressing the 50/200 spread from **+24.3 (06-18)** toward a potential bearish cross. The spread bottomed around **+11.1 (07-29)** and has since widened to **+11.36 (08-05)** with the 50 SMA turning up (+0.93 over four sessions). **A death-cross setup was averted by three sessions of price action** — that is bullish, but the margin (4.8% of the 200 SMA) remains thin. Price is **+10.24%** above the 50 SMA — historically stretched.

**Short term (10 EMA = 258.34) — sharp V-reversal, price extended.** The 10 EMA bottomed at **236.29 (07-30)** and has risen to **258.34 (08-05)** — +9.3% in four sessions. Price at 272.65 sits **+5.54% above the 10 EMA**, i.e. well outside the normal pullback band. Short-term trend direction: unambiguously up; short-term *entry timing*: poor.

**Read:** the trend hierarchy is a textbook bullish stack (price > 10 EMA > 50 SMA > 200 SMA), but it was assembled by a **news-driven vertical gap, not by a base**. There is no rounded bottom, no multi-week accumulation pattern — the 07-23→07-29 decline was intact until 07-31. V-shaped, event-driven advances carry a higher two-way risk than base-building advances because there is no congested support beneath price.

---

## 4. Momentum: a fresh, expanding — but historically unreliable — MACD cross

| Date | MACD | Signal | Histogram |
|---|---|---|---|
| 07-29 | -3.751 | -1.765 | -1.986 |
| 07-30 | -3.634 | -2.139 | -1.496 |
| 07-31 | -0.623 | -1.836 | **+1.213** (cross) |
| 08-03 | +2.736 | -0.921 | +3.657 (zero-line cross) |
| 08-04 | +4.809 | +0.225 | +4.585 |
| 08-05 | **+5.999** | **+1.380** | **+4.619** |

The MACD line crossed its signal on **07-31**, crossed the zero line on **08-03**, and is now at its highest reading of the visible window. That is a high-quality *regime change* signal.

**The critical caveat:** this regime has produced **false MACD signals repeatedly within the last five weeks.** The histogram was positive from **07-01 through 07-22** (peaking at +2.12 on 07-15) before rolling over to negative on **07-23** and staying negative through 07-30 — a failed four-week bullish signal that resolved with a −7.4% decline. So a histogram crossover alone is *not* sufficient evidence here.

**Second caveat — momentum is already decelerating:** the histogram's daily increments were **+2.44 (07-31→08-03), +0.93 (08-03→08-04), +0.03 (08-04→08-05)**. The rate of momentum acceleration collapsed to near zero on the same day price closed near its low. That is the first sign of exhaustion in the thrust.

**RSI = 63.49** — a staggering 3-session swing: **33.31 (07-29) → 44.41 (07-30) → 67.88 (07-31) → 72.23 (08-03) → 63.49 (08-05)**, a **+38.9 point move in three sessions**. Interpretation: RSI is now in the *constructive but no longer overbought* 60–70 band. Notably, RSI is cooling *faster* than price (price −4.0% from the 08-03 close, RSI −8.7 points) — that is **constructive digestion**, not distribution. But there is **no confirmed bearish RSI divergence**, only two sessions of lower highs/lower RSI, which is insufficient to call a top.

---

## 5. Volatility: a regime shift, not a blip

**ATR = 9.98**, up from **6.89 (07-29)** — **+44.9% in five sessions**, the highest ATR in the visible window. ATR/price = **3.66%** per day. Practical translation: a 1-session move of ±10 points (~±3.7%) is now *ordinary*.

**Bollinger bands (supplementary confirmation from the snapshot):**
- Upper band: **281.41**, Lower: **216.34**, Middle (20 SMA): **248.87**. Bandwidth = **65.07 points = 26.1% of the middle band** — an extreme expansion.
- On **08-03**, the close of **284.02 exceeded the then-upper band of 272.99** — a textbook band breakout/extension.
- On **08-05**, the close of 272.65 is back **inside** the band, and the day's high of 282.79 was effectively rejected at the upper band (**281.41**). The upper band is now acting as measured resistance, not a launchpad.
- Position within the bands: **86.6%** of the way from lower to upper — still elevated, leaving room to mean-revert without damaging the trend.

**Interpretation:** band expansion of this magnitude after a gap typically means one of two things — (a) a durable new volatility regime with follow-through, or (b) a one-off event that mean-reverts as the bands normalize. The **close back inside the upper band after a single session above it** leans toward (b) at least for the near term, with a high probability of multi-week chopping between roughly **262 and 284** while the 10 EMA and the 50 SMA close the distance to price.

---

## 6. Volume and participation: the pullback is orderly, but the cost basis is close beneath

- **VWMA = 253.80**, price **+7.42%** above it. The VWMA has vaulted from **240.82 (07-30) to 253.80 (08-05)** (+5.4% in four sessions) because the rally occurred on enormous volume. That makes 253.80 a genuine, volume-weighted "recent market cost" reference — and it sits **inside the unfilled gap band**.
- **10 EMA (258.34) > VWMA (253.80)** by 4.54 points: the most recent buying is above the volume-weighted average, i.e. buyers are in profit — bullish, but also a source of supply if momentum stalls.
- **Volume pattern on the retracement is the most bullish single fact in this report:** 129.05M (07-31) → 90.83M (08-03) → 69.75M (08-04) → **45.12M (08-05)**. The pullback is occurring on **declining volume (down ~65% from the gap day)** — the signature of profit-taking rather than institutional distribution. There has been no high-volume reversal day so far. Conversely, there has also been no capitulation flush, meaning the seller overhang may not be fully cleared.

---

## 7. Key levels — every figure traced to a dated observation

| Level | Price | Provenance (dated) | Role |
|---|---|---|---|
| Intraday high | **287.20** | 2026-08-03 high (highest in the 189-session dataset) | Breakout trigger / resistance |
| Bollinger upper | **281.41** | Snapshot 2026-08-05 | Rejected here on 08-05 (high 282.79) |
| Prior range high | **278.56** | 2026-05-05 high | Resistance zone 278.5–281.4 |
| Prior range high close | **274.99** | 2026-05-06 close | **Lost on 08-05 (272.65)** — breakout unconfirmed |
| Gap-day open | **265.00** | 2026-07-31 open | First meaningful support shelf |
| Gap-day low | **262.01** | 2026-07-31 low | Bull-case line in the sand |
| 10 EMA | **258.34** | Snapshot 2026-08-05 | Short-term trend filter |
| VWMA | **253.80** | Snapshot 2026-08-05 | Volume-weighted cost basis |
| Bollinger middle | **248.87** | Snapshot 2026-08-05 | Mean-reversion magnet |
| 50 SMA | **247.32** | Snapshot 2026-08-05 | Medium-term line; conjunct with 20 SMA (1.55 pts apart) |
| 200 SMA | **235.95** | Snapshot 2026-08-05 | Last line of long-term defence |

Note the confluence: **247.3–248.9** contains the 50 SMA and the 20 SMA/Bollinger middle within 1.55 points — which is why I did **not** select the Bollinger middle as a separate indicator (it would duplicate the 50 SMA signal). Similarly, **253.8–258.3** bundles VWMA and the 10 EMA into one support shelf.

---

## 8. Actionable framework

**Do not chase at 272.65.** Price is 5.5% above its 10 EMA, momentum acceleration has stalled (+0.03 histogram increment), the close was in the bottom 16% of the range, the close is back under the prior range's 274.99 high, and the upper band rejected at 281.41. The risk/reward for a fresh long here is roughly −13 to the first real support shelf vs +14.5 to the high — but with 3.66% daily ATR, that stop is less than 1.5 ATR away, i.e. inside the noise band.

**Three scenarios with defined triggers:**

- **Bull continuation (needs confirmation):** a **close above 281.41** (upper band) with volume back above ~70M reopens **287.20**, and on a break, measured extension of the 65-point band width from the 248.87 mid implies an upside objective near **295–300**. Entry: either the breakout close, or a staged add on a hold of 265.00.
- **Consolidation (highest probability, ~2–4 weeks):** chop between **262.01 (gap low) and 284.02/287.20**, letting the 10 EMA (258.34, rising ~2.5 pts/day at current pace) climb into price. This is the *healthy* outcome — it would rebuild a technical base that the gap never provided. Range-trading, not trend-following, is the correct playbook here.
- **Failure / gap-fill risk:** a **close below 258.34 (10 EMA)** then **253.80 (VWMA)** shifts the tape to neutral. A **close below 247.32 (50 SMA)** — which would also break the 20 SMA at 248.87 — opens the unfilled **235.50 → 262.01** band, with the **200 SMA at 235.95** as the terminal support for the long-term uptrend. Because that gap zone is completely un-traded, slippage through it can be fast and large.

**Risk management (ATR-calibrated):**
- **Volatility-scaled stop:** 1.5 × ATR ≈ **15 points**; 2 × ATR ≈ **20 points**. From 272.65, a 2-ATR stop is **252.65** — which lands almost exactly on the VWMA of 253.80. That is the cleanest confluence stop in the current structure: it sits below the volume-weighted cost basis *and* above the 50 SMA.
- **Position sizing:** with ATR at 9.98 vs a pre-gap reading of 6.89, the same dollar risk implies **~31% smaller position size** than three weeks ago. Halve or third normal size on any new entry until ATR compresses back below ~8.
- **Event risk is structural, not incidental.** This instrument has produced three prior volume/gap dislocations in the visible window: **2026-02-05/02-06** (232.99 → 210.32 close, low 200.31, volume 179.2M), **2026-04-08** (gap open 223.79 vs prior close 213.77, volume 51.1M) and **2026-07-31** (129.1M). The data does not label the catalyst, but the signature is consistent with scheduled fundamental events (e.g. quarterly reports). Anyone holding through the next such date should size for a ±12–18% overnight gap, not a 3.7% ATR day.

**Invalidation checklist — the thesis breaks if:**
1. A daily close below **253.80** (VWMA) with volume >70M (distribution return).
2. A daily close below **247.32** (50 SMA), which would re-open the 50/200 compression toward a death cross.
3. A new MACD histogram contraction to negative *before* price clears 287.20 — repeating the 07-23 pattern that preceded the last −7.4% leg.
4. RSI pushing to 75+ without price making a new closing high above 284.02 (a genuine bearish divergence).

---

## 9. Indicator selection rationale (8 selected, non-redundant)

| # | Indicator | Value (08-05) | Why it is the right tool *for this specific setup* |
|---|---|---|---|
| 1 | **close_10_ema** | 258.34 | Fastest read on the post-gap trend; defines the first pullback buy zone; price +5.54% above it quantifies "don't chase." |
| 2 | **close_50_sma** | 247.32 | Captures the near-death-cross that was averted; doubles as the medium-term support that keeps the gap thesis alive. |
| 3 | **close_200_sma** | 235.95 | Anchor for whether this is a breakout to a new regime or a counter-trend spike; +15.55% spread frames downside air. |
| 4 | **macd** | 5.999 | Confirms the regime change via the 07-31 signal cross and 08-03 zero-line cross; one clean momentum authority (signal line referenced from snapshot, not a separate selection). |
| 5 | **macdh** | 4.619 | Adds the *rate of change* dimension MACD alone lacks — the +2.44 → +0.93 → +0.03 deceleration is the key early-warning datapoint. |
| 6 | **rsi** | 63.49 | Quantifies the V-reversal (33.3 → 72.2 → 63.5) and distinguishes healthy digestion from a blow-off top. |
| 7 | **atr** | 9.98 | The single most actionable risk input right now: volatility +44.9% in 5 sessions dictates stop distance and position size. |
| 8 | **vwma** | 253.80 | Price integrated with volume — uniquely validates that this rally is volume-backed, and supplies the cleanest stop confluence at 253.8. |

**Deliberately excluded:** `boll` middle (248.87 is only 1.55 points from the 50 SMA — redundant), `boll_lb` (extreme band widening already captured by ATR; the lower band at 216.34 is not a tradable level within this horizon), and `macds` (derivable from MACD + histogram). Bollinger upper/lower *values* are cited above from the verified snapshot as supplementary extension evidence, not as core selections.

---

## 10. Bottom line

AMZN is in a **confirmed long-term uptrend (+15.6% above the 200 SMA) that has just been violently re-energized by an event-driven, high-volume gap** — MACD crossed up on 07-31 and through zero on 08-03, RSI swung 39 points in three sessions, and the pullback is occurring on shrinking volume, which argues for profit-taking rather than distribution. But the advance is **vertical, unsupported by a base, and technically incomplete**: the 08-03 break to 287.20 has not held, the 08-05 close of 272.65 sits back *below* the 05-06 prior high close of 274.99, the histogram's acceleration has flatlined, and the upper band (281.41) rejected price to the day's low. ATR at 9.98 (+44.9% in five sessions) means the correct posture is **smaller size, wider stops, and staged entries** — the highest-probability path is 262–284 consolidation while the 10 EMA (258.34) catches up, with a close above 281.41 required to re-engage the upside and a close below 247.32 opening the unfilled 235.50–262.01 gap.