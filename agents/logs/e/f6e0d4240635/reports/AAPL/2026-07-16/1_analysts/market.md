# AAPL — Technical Analysis Report (as of 2026-07-16)

*All exact price and indicator values below are from the verified snapshot and indicator time series (B-project frozen data), not recounted from memory. Where I compute percentage distances, I label them as derived.*

---

## 1. Market Context & Regime

AAPL is in a **well-established primary uptrend** that just printed a **fresh all-time-high close** on the analysis date. The defining feature of the last ~6 weeks is a **sharp late-June shakeout followed by an aggressive V-shaped recovery**:

- Closing peak on **2026-06-02 at 315.20**, then a decline to a **closing low of 275.15 on 2026-06-25** (intraday low 273.75). That is roughly a **−12.7% drawdown** over three-and-a-half weeks (derived from tool closes).
- The 2026-06-26 session saw **volume of 261.8M** (roughly 4–5× normal), consistent with a forced/index-driven flush rather than organic distribution.
- From the 06-25 low, price **rallied +21% to 333.26 by 07-16** (derived), reclaiming the June highs (315.20) and extending to a new high of **334.68 intraday on 07-16**.

So the market condition is: **strong trending regime, currently at highs, with short-term momentum re-accelerated but stretched (overbought).** That context drives the indicator selection.

### Indicator selection rationale (8 chosen, complementary, non-redundant)
| Indicator | Why it fits this context |
|---|---|
| **close_50_sma** (301.66) | Confirms medium-term trend and defines the "line in the sand" that survived the June shakeout. |
| **close_200_sma** (273.82) | Long-term regime filter; rising and far below price = durable bull structure. |
| **close_10_ema** (316.62) | Captures the sharp short-term momentum and gives a tight trailing reference for the recovery leg. |
| **macd** (7.87) | Measures the momentum re-acceleration and zero-line reclaim. |
| **macds** (4.64) | Signal line to time the bullish crossover and gauge trend conviction vs. the MACD line. |
| **rsi** (71.43) | Specifically needed here: flags overbought risk after a +21% run — the key tension in this setup. |
| **atr** (8.30) | Elevated volatility regime → essential for stop placement and position sizing on a stretched chart. |
| **vwma** (300.72) | Volume-weighted confirmation; distinguishes conviction-driven advances from drift. |

*Deliberately excluded: Bollinger bands (largely redundant with RSI + SMA here, though I reference the middle/upper bands from the snapshot as a secondary check), stochastics (redundant with RSI), and MACD histogram (derivable from MACD/signal).*

---

## 2. Trend Structure — Bullish and Fully Aligned

The moving-average stack is in **perfect bullish order** on the latest session:

- **Price 333.26 > 10-EMA 316.62 > 50-SMA 301.66 > 200-SMA 273.82**

Key structural readings:
- **50-SMA is rising almost monotonically** — from ~260.5 in mid-April to 301.66 now — a genuine intermediate uptrend, not a flat line.
- **200-SMA is steadily rising** — 252.1 (04-17) → 273.82 (07-16) — confirming a long-term bull regime. A golden-cross structure (50 above 200) has been in force throughout.
- **Price extension**: close is **~10.5% above the 50-SMA** and **~21.7% above the 200-SMA** (derived). That is a healthy but extended posture — trend-following longs are justified, but chasing here carries elevated mean-reversion risk.
- **Distance from the 10-EMA**: close is **~5.3% above the 10-EMA** (derived), reflecting two sharp up-days (07-15 close +4.0% to 327.50; 07-16 +1.76% to 333.26, derived). Short-term stretch is meaningful.

**Important nuance from the June dip:** the 06-25 close (275.15) actually **broke below the then-50-SMA (~291)** for several sessions, but the 50-SMA **never rolled over**, and price reclaimed it by 07-01 (close 294.38 vs 50-SMA 292.67). That classifies the drop as a **shakeout within an uptrend**, not a trend break — the 200-SMA (then ~269) was never seriously threatened.

---

## 3. Momentum — Re-accelerating and Confirmed

MACD dynamics tell the clearest story of the V-recovery:

- **MACD line rolled from +10.42 (05-28)** down to **negative territory (−2.92 on 06-29)** during the pullback, then **re-crossed above zero on 07-06** and is now **7.87**.
- The **MACD line crossed back above its signal line on 07-06** (MACD 0.88 vs signal −0.58) — a fresh **bullish crossover** — and the gap is **widening** (MACD 7.87 vs signal 4.64; histogram ≈ +3.23 from the snapshot). A widening positive histogram = **momentum strengthening**, not stalling.
- This is a textbook "**reset-and-reclaim**": the pullback fully flushed momentum, and the new leg is already near where the prior leg peaked — a sign of strong underlying demand.

---

## 4. RSI — The Central Tension (Overbought but Trend-Supported)

- RSI presciently traced the whole cycle: **peaked at 79.8 on 05-28**, collapsed to **32.2 on 06-25** (near-oversold, not quite <30), and has now climbed to **71.43** — crossing above the 70 overbought threshold.
- **Interpretation:** In the May advance, RSI spent roughly 05-08 to 05-29 lodged in the 70s (peaks to 79.8) *without* the trend breaking — evidence that in this regime RSI extremes are **trend-persistent, not automatic sell signals**. The current 71.4 is a mild overbought reading, consistent with a strong-but-extended leg.
- **Actionable read:** RSI > 70 argues against fresh aggressive chasing at the highs; it favors **buying pullbacks/dips toward support** rather than breakout-chasing, or tightening stops on existing longs. Watch for **bearish RSI divergence** (price new high, RSI lower high) as the earliest warning of exhaustion — none is present yet as RSI is still rising.

---

## 5. Volatility & Risk (ATR) — Regime Shifted Higher

- ATR rose from **~5.5–6.6 in May** to **8.30 now** — roughly **2.5% of the 333 price** (derived). Volatility has structurally expanded post-June.
- This has concrete implications:
  - **Stops must be wider** than the May regime would suggest. A common rule — 2×ATR ≈ **~16.6 points** — implies a stop in the **~316–317** zone for a long entered near current levels (that also aligns with the 10-EMA at 316.62 — a meaningful confluence).
  - **Position size down** proportionally: the same dollar risk now buys a smaller position because per-share risk (ATR) is ~50% higher than in May.

---

## 6. Volume Confirmation (VWMA)

- **VWMA is 300.72**, and price (333.26) is **well above it** — the uptrend is **volume-supported**, not drifting. VWMA has turned up from its late-June trough (288.84 on 06-30) and is now rising.
- The recent breakout days carried **above-average volume**: 60.96M (07-15) and 62.97M (07-16) vs. a typical ~50M — participation is confirming the new highs rather than a low-volume fakeout.
- Caveat from the tool tips: the huge 06-26 spike (261.8M) can **skew VWMA**; treat VWMA as a confirmation filter, not a precision level.

---

## 7. Key Levels (from snapshot & indicator series)

**Resistance / upside**
- **334.68** — 07-16 intraday high (immediate resistance).
- **334.79** — Bollinger Upper Band (snapshot), essentially coincident with the day's high → a **band-touch/breakout decision point**. A decisive close *above* ~335 on volume would confirm continuation; rejection here raises short-term stalling risk.

**Support / downside (stacked, bullish)**
- **~333 / 327.50** — recent closes; shallow shelf.
- **316.62** — 10-EMA, first dynamic support (aligns with a 2×ATR stop zone).
- **~315.20** — 06-02 prior closing high = breakout retest zone.
- **~303.6 (Bollinger middle) / 301.66 (50-SMA) / 300.72 (VWMA)** — a **dense confluence band** ~301–304; a pullback into this zone is the higher-probability "buy the dip" area for trend followers.
- **273.8–275.1** — 200-SMA + 06-25 low + Bollinger Lower Band (272.46): the major structural floor. A break here would invalidate the bull thesis.

---

## 8. Actionable Takeaways

1. **Bias: bullish/trend-following**, but this is a **"hold, don't chase"** juncture given RSI 71.4, a ~5.3% gap above the 10-EMA, and price pinned at the upper Bollinger band (~334.8).
2. **For existing longs:** the trend and momentum (fresh MACD crossover, expanding histogram, VWMA support, rising 50/200-SMAs) all argue to **stay long**; trail stops toward **~316 (10-EMA / 2×ATR)** to protect the recovery gains.
3. **For new entries:** prefer **buying pullbacks into the 301–316 confluence zone** (50-SMA/VWMA/Bollinger-mid/prior breakout) rather than buying the 334 print. Alternatively, require a **volume-confirmed close above ~335 (upper band)** to justify breakout continuation entries.
4. **Risk management is non-negotiable** here: ATR ≈ 8.30 means ~2.5% daily range; size positions off a **2×ATR (~16.6 pt) stop** and expect wider swings than the May regime.
5. **Watch:** (a) a rejection at the ~334.8 upper band, (b) **bearish RSI divergence**, (c) MACD histogram rolling over / MACD–signal narrowing — any of these would be the first crack in the current momentum leg. A loss of the **200-SMA (~274)** would be a full trend-invalidation signal.

*No conflicts were found between the indicator series and the verified snapshot — all latest values (SMA/EMA, MACD/signal, RSI, ATR, VWMA, Bollinger bands) match the snapshot exactly.*

---

## Summary Table

| Category | Indicator | Latest Value (07-16) | Signal / Interpretation |
|---|---|---|---|
| Price | Close | 333.26 | New all-time-high close; +21% off 06-25 low |
| Trend – short | 10-EMA | 316.62 | Price ~5.3% above → short-term stretched |
| Trend – medium | 50-SMA | 301.66 | Rising, survived June shakeout; key support |
| Trend – long | 200-SMA | 273.82 | Rising; bull regime intact; ~21.7% below price |
| Momentum | MACD | 7.87 | Re-crossed above zero 07-06; re-accelerating |
| Momentum | MACD Signal | 4.64 | Below MACD → bullish; histogram ≈ +3.23 & widening |
| Overbought | RSI | 71.43 | Overbought (>70); trend-persistent, avoid chasing |
| Volatility | ATR | 8.30 (~2.5%) | Elevated regime; 2×ATR stop ≈ 316–317 |
| Volume | VWMA | 300.72 | Price above → uptrend volume-confirmed |
| Bands (ref) | Boll Mid / UB / LB | 303.63 / 334.79 / 272.46 | Price at upper band ~334.8 = breakout decision point |
| **Net stance** | — | — | **Bullish trend, overbought/extended → hold longs, buy dips 301–316, don't chase >334; invalidate below 274** |