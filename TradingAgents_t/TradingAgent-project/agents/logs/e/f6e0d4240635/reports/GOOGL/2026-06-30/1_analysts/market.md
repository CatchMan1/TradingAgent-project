# GOOGL (Alphabet Inc.) — Technical Analysis Report
**Analysis date: 2026-06-30 | Latest verified close: $357.37**

## 1. Snapshot of the current setup
The verified market snapshot (source of truth, 2026-06-30 session) shows:

| Metric | Value |
|---|---|
| Open / High / Low / **Close** | 353.87 / 358.62 / 350.40 / **357.37** |
| Volume | 35.24M |
| 10-EMA | 353.22 |
| 50-SMA | 369.94 |
| 200-SMA | 315.01 |
| MACD / Signal / Hist | -6.05 / -4.93 / **-1.12** |
| RSI(14) | 47.93 |
| Bollinger Mid / Upper / Lower | 358.53 / 378.59 / 338.47 |
| ATR(14) | 11.96 |
| VWMA | 351.81 |

GOOGL is caught at a **decision point**: a powerful, still-intact long-term uptrend is passing through a **medium-term corrective pullback**, and the last two sessions show a **short-term oversold bounce** off a high-volume capitulation low.

## 2. Trend structure (three timeframes)
**Long-term — clearly bullish.** Price ($357.37) sits **+13.4% above a rising 200-SMA ($315.01)**. That benchmark climbed every session into the date (313.85 → 314.42 → 315.01 over the last three rows). The 50-SMA ($369.94) is far above the 200-SMA, confirming a mature **golden-cross, uptrend alignment**. Nothing in the long-term structure has broken.

**Medium-term — corrective / bearish tilt.** Price is **~3.4% below the 50-SMA ($369.94)**, which has gone almost flat (369.28 → 369.63 → 369.94). The decline from the mid-May peak has been orderly on the 50-SMA basis: the stock peaked at a **May 18 intraday high of $408.61** and a **May 8 close of $400.80**, then slid to a **June 26 close of $337.39** — a **−15.8% closing drawdown** (−19.2% on the intraday high-to-low, $408.61 → $330.20). The 50-SMA is now acting as the overhead barrier that must be reclaimed to call the correction over.

**Short-term — turning up.** Two consecutive strong sessions: June 29 closed at $353.65 (**+4.8%** from the June 26 close of $337.39) and June 30 added another **+1.05%** to $357.37. Price has **reclaimed the 10-EMA ($353.22)** and the **VWMA ($351.81)** — the first short-term bullish signs since the June slide began.

## 3. Momentum
- **RSI(14) = 47.93**, recovering from **33.27 on June 26** (near-oversold) through 45.6 (June 29) to 47.9. It is now neutral, with plenty of room in either direction and **no overbought constraint on a further bounce**. Notably, the RSI at the June 26 low (33.3) was only modestly below the June 3 low's RSI (38.8) despite a much lower price ($337 vs $359) — a **mild bullish momentum divergence** worth watching.
- **MACD = −6.05 vs Signal −4.93.** MACD remains **below** its signal (formally bearish), *but the histogram is contracting fast*: −3.24 (June 26) → −2.17 (June 29) → **−1.12 (June 30)**. The MACD line has curled up for two sessions while the signal keeps falling — the classic **early setup for a bullish crossover**. A confirmed MACD-over-signal cross would be the momentum trigger validating the rebound.

## 4. Volatility & volume
- **ATR(14) = 11.96**, up from ~9.3 in early June — **expanding volatility** (~3.3% of price). Daily ranges are wide; **position sizes should be reduced** and stops set wider (≈1.5–2× ATR).
- **Volume tells the story of the low.** The **June 26 session traded 114.7M shares** — roughly 2.5–4× the typical 25–45M — with the close ($337.39) well above the low ($330.20). That high-volume flush-and-close-off-the-low is a textbook **seller-exhaustion / washout** signature, followed by the two-day snap-back. The preceding decline also had heavy distribution days (June 2: 50M on a −3.9% day; June 3: 55M), so the high-volume reading cuts both ways — but the *price response* (immediate strong rebound) currently favors the bull interpretation.
- **VWMA = 351.81**, below price now, but the volume-weighted average has slid relentlessly from ~$392.8 (May 21) to $351.8, confirming that **volume has been on the sell side** through the correction. Price reclaiming it is a tentative positive; sustained price *above* a *rising* VWMA would be needed to fully confirm a trend shift.

## 5. Volatility bands (Bollinger context)
Price ($357.37) is **just below the 20-SMA middle band ($358.53)**. On June 26 the low ($330.20) briefly **pierced the lower band ($338.47)** and snapped back — a mean-reversion "band pierce and reclaim," a classic short-term low signal. The bands are wide (lower $338.47 to upper $378.59) reflecting elevated volatility. Immediate overhead is the **middle band ~$358.5**; a close above it opens the upper band (~$378.6).

## 6. Key levels to trade around
- **Resistance:** $358.5 (Bollinger mid, immediate) → $369.9 (50-SMA) → $373–376 (June breakdown shelf) → $378.6 (upper band) → $400–408 (May peak zone).
- **Support:** $353 (10-EMA) / $351.8 (VWMA) → $338.5 (lower band) → **$330.2 (June 26 swing low — the line in the sand)**.

## 7. Actionable scenarios
**Bullish (short-term long):** The washout-and-reclaim setup argues the June 26 low can hold. Traders could look to own the bounce around **$353–357** (or on a dip to the 10-EMA/VWMA cluster ~$351–353), with a **stop below the June 26 low near $330** (≈2 ATR). First targets $369.9 (50-SMA) and $378.6 (upper band). *Confirmation trigger:* a MACD bullish crossover (histogram flipping positive) and a close above the $358.5 mid-band.

**Bearish / caution:** The medium-term trend is still down — price is under the 50-SMA and MACD remains below zero and below signal. A rally that **stalls at the 50-SMA ($369.9)** would be a lower-high and could resume the correction toward the lower band ($338) and the June low ($330). A decisive close **below $330** on volume would invalidate the bounce and target the deeper $302–314 support shelf (February–March congestion).

**Bias:** Constructive short-term, neutral-to-cautious medium-term. The weight of evidence supports treating this as a **tradable bounce within a correction** rather than a confirmed trend reversal — until GOOGL reclaims the 50-SMA on volume.

## 8. Caveats & discrepancies
- The OHLCV in `get_stock_data` and the verified snapshot are **consistent** (identical rows for overlapping dates) — no conflict to flag.
- The snapshot's `mfi` field printed as `0.338824`, an unclear scaling; **I am not relying on MFI** for any claim here.
- No historical support/resistance "bounce" or exact percentage figures are asserted beyond those directly computed from the tool output above.

---

## Summary Table — Key Points

| Dimension | Reading (2026-06-30) | Interpretation | Actionable Takeaway |
|---|---|---|---|
| **Price** | $357.37 (+1.05% d/d; +4.8% over 2 sessions) | Sharp rebound off June 26 low | Bounce in progress |
| **10-EMA** | $353.22 | Price above → short-term upturn | near-term support |
| **50-SMA** | $369.94 (flat) | Price ~3.4% below → medium-term bearish | overhead resistance / trend gate |
| **200-SMA** | $315.01 (rising) | Price +13.4% above → long-term bull intact | strategic uptrend confirmed |
| **Golden cross** | 50-SMA > 200-SMA | Bullish long-term structure | dip-buying bias tactically |
| **MACD / Signal** | −6.05 / −4.93 | MACD below signal but histogram contracting (−3.24→−1.12) | watch for bullish crossover |
| **RSI(14)** | 47.93 | Neutral, recovering from 33.3 | room to run both ways |
| **Bollinger** | Mid 358.53 / Up 378.59 / Low 338.47 | Pierced lower band June 26 & reclaimed | mean-reversion low signal |
| **ATR(14)** | 11.96 (~3.3% of price) | Volatility expanding | smaller size, stops ≈1.5–2 ATR |
| **VWMA** | 351.81 (declining) | Price just above; volume was sell-side | weak bullish confirmation |
| **Volume signal** | June 26: 114.7M (washout) | Capitulation / exhaustion | supports short-term bottom |
| **Key support** | $351–353 / $338.5 / **$330.2** | June low is the line in the sand | stop below $330 |
| **Key resistance** | $358.5 / $369.9 / $373–378 / $400–408 | 50-SMA is the pivotal barrier | reclaim 50-SMA = correction over |
| **Overall bias** | Long-term bull, medium-term corrective, short-term bouncing | Tradable relief rally | Tactical long w/ tight risk; reassess at 50-SMA |

*Selected indicators (8, non-redundant): close_10_ema, close_50_sma, close_200_sma, macd, macds, rsi, atr, vwma — spanning trend, momentum, overbought/oversold, volatility/risk, and volume confirmation. Bollinger bands referenced from the verified snapshot as supplementary context.*