# AAPL Technical Analysis Report — As of 2024-01-17

## 1. Executive Summary
AAPL is in a **short- and medium-term downtrend that is now testing a critical long-term support zone**. The stock closed at **182.68** on 2024-01-17, trading **below** its 10-EMA (185.37), **below** its 50-SMA (189.32), and — more importantly — only about **1% above** its 200-SMA (180.91). Momentum is firmly negative (MACD below zero and below its signal line; RSI weak at 36.7), while volatility has expanded (ATR 3.10, wide Bollinger bands). The picture is a corrective pullback within a still-intact longer-term uptrend, with the 180–181 area as the line in the sand.

## 2. Indicator Selection & Rationale
I selected **8 complementary indicators** spanning trend, momentum, volatility, and volume:

| Category | Indicator | Why selected here |
|---|---|---|
| Trend (long) | **close_200_sma** | Defines the long-term regime; price is hovering just above it, making it the single most important support test. |
| Trend (medium) | **close_50_sma** | Captures the medium-term trend now rolling over; price has lost it, signaling trend deterioration. |
| Trend (short) | **close_10_ema** | Responsive gauge of the short-term swing; price below it confirms immediate downside momentum. |
| Momentum | **macd** | Confirms the shift from bullish to bearish momentum (crossed below zero). |
| Momentum | **macds** | Signal-line provides the crossover trigger and confirms the bearish bias. |
| Momentum | **rsi** | Independent momentum/overbought-oversold read; shows weakness without capitulation. |
| Volatility | **atr** | Elevated and rising; essential for sizing stops and positions in a fast-moving tape. |
| Volume | **vwma** | Volume-weighted trend confirms whether selling is being backed by volume (distribution). |

This mix avoids redundancy (e.g., three time-framed moving averages give multi-horizon trend context; MACD+signal give crossover mechanics distinct from RSI's threshold read; ATR and VWMA add volatility/volume dimensions absent from price-only tools).

## 3. Trend Analysis (Multi-Timeframe)

**Long-term (200-SMA = 180.91): still constructive, but under pressure.**
Price at 182.68 sits roughly **+1.8 points (+0.98%) above the 200-SMA**. The 200-SMA continues to rise slowly (from 177.79 on 2023-12-18 to 180.91 on 2024-01-17), confirming the long-term uptrend structure is intact. The 50-SMA (189.32) remains above the 200-SMA, so the "golden-cross" configuration persists. **However**, price is now pressing directly down onto this long-term benchmark — a decisive daily close below 180.9 would be a meaningful long-term trend break.

**Medium-term (50-SMA = 189.32): deteriorating.**
Price is **about 3.5% below** the 50-SMA, and the 50-SMA has flattened (rising only ~0.5 points over the last five sessions vs. much faster earlier). This shows the medium-term trend has stalled and is turning. The 50-SMA at 188.80–189.32 (converging with the Bollinger middle at 188.80) is the key medium-term resistance overhead.

**Short-term (10-EMA = 185.37): clearly bearish.**
Price is ~1.45% below the 10-EMA, and the 10-EMA is rolling over sharply (from ~195 in mid-December to 185.37 now). This confirms the immediate swing is down.

**Net:** A textbook **bearish short/medium-term alignment within a still-positive long-term structure** — i.e., a correction, not yet a full regime change.

## 4. Momentum Analysis

**MACD (−1.93) vs. Signal (−1.21), histogram −0.72.** The MACD line crossed below its signal line around 2023-12-18/19 (histogram flipped from positive to negative) and then crossed **below zero around 2024-01-03/04**. Both are bearish. The histogram has stabilized near −0.72 for two sessions (Jan 16 vs Jan 17), which is a minor sign that downside momentum is not accelerating — but there is no bullish crossover yet. Momentum remains negative until the MACD line turns back above the signal line.

**RSI = 36.7.** Below the neutral 50 line, indicating weak momentum, but **not yet oversold** (30). Notably, RSI bottomed at **28.79 on 2024-01-05** (briefly oversold), recovered to ~43 by Jan 10–12, and has since faded back to 36.7 — a **failed momentum bounce**, which is a bearish tell. There is room for further downside before RSI reaches oversold again.

*(Snapshot note: the frozen snapshot also reports an MFI of ~0.30, which is extreme; I did not select MFI as a primary indicator and treat that reading with caution rather than as a core signal.)*

## 5. Volatility Analysis (ATR & Bollinger)

**ATR = 3.10** — up from ~2.57–2.88 in late December, confirming **expanding volatility** alongside the January selloff. At ~1.7% of price, ATR implies daily range potential of roughly ±3 points.

**Bollinger Bands:** middle 188.80, upper 199.40, lower 178.19. The wide band (~21 points, roughly ±5.6% around the middle) reflects elevated volatility. Price (182.68) sits in the **lower half** of the band but is **~4.5 points above the lower band (178.19)** — i.e., near, but not at, oversold extremes. The middle band (188.80) coincides with the 50-SMA, reinforcing it as resistance.

## 6. Volume Analysis (VWMA)

**VWMA = 185.45**, with price below it and the VWMA in steady decline (from ~195 in late December to 185.45). This confirms that **volume-weighted selling pressure dominates** — the downtrend is being validated by volume, not just price drift. The VWMA also clusters tightly with the 10-EMA (185.37), forming a **resistance shelf around 185.4**. Notably, the largest-volume down day was Jan 2 (82.5M shares) on the −3.6% gap; volume has since moderated (Jan 17: 47.3M), suggesting selling is broad but not yet climactic.

## 7. Key Levels (from tool-verified data)

**Resistance:**
- **185.4** — 10-EMA (185.37) + VWMA (185.45) cluster; first ceiling.
- **188.8–189.3** — Bollinger middle (188.80) + 50-SMA (189.32); trend-repair zone.
- **199.4** — Bollinger upper; near the Dec-14 high close (198.11) / Dec-14 intraday high (199.62).
- **198.11** — 2023-12-14 closing high (recent peak).

**Support:**
- **180.9** — 200-SMA; the critical long-term line.
- **180.2–180.3** — Jan-5 intraday low (180.17), Jan-16 low (180.93), Jan-17 low (180.30); a **retested floor**.
- **178.19** — Bollinger lower band; next structural downside target if 180 breaks.

## 8. Actionable Insights

1. **Near-term bias is bearish** while price stays below the 185.4 (10-EMA/VWMA) shelf. Shorts/reduced longs are favored on rallies into 185–186 that fail.
2. **Watch the 180.2–180.9 zone closely.** This is a double confluence (200-SMA + prior swing low). A **daily close below ~180** would confirm a long-term trend break and likely open a move toward the Bollinger lower band (~178.2).
3. **A reclaim of 185.4** (10-EMA/VWMA) would neutralize the immediate bearish setup; a **close back above 188.8–189.3** (Bollinger middle/50-SMA) would signal genuine trend repair and put the December highs (198–199) back in play.
4. **Momentum confirmation:** Wait for the MACD line to cross back above its signal line before treating any bounce as durable; the current MACD (below zero, below signal) still favors the downside.
5. **Risk management:** With ATR at 3.10, a protective stop ~1×ATR below a support entry near 180 would sit around ~177 (below the Bollinger lower band), while a stop just below the 200-SMA (~180) is tighter but more prone to noise. Size positions to ~1.7% daily ATR.
6. **RSI caution:** RSI at 36.7 is weak but not oversold — do not treat this as a bottom signal. The failed bounce from 28.8 back to 36.7 argues for patience rather than a mean-reversion long.

## 9. Key Points Summary Table

| Dimension | Indicator | Value (2024-01-17) | Signal / Interpretation |
|---|---|---|---|
| Price (close) | — | **182.68** | Below 10-EMA & 50-SMA, barely above 200-SMA |
| Long-term trend | 200-SMA | 180.91 | Bullish structure intact; price +0.98% above — key support |
| Medium-term trend | 50-SMA | 189.32 | Price −3.5% below; trend deteriorating |
| Short-term trend | 10-EMA | 185.37 | Price below; immediate trend down |
| Momentum | MACD | −1.93 | Bearish (below zero) |
| Momentum | MACD Signal | −1.21 | MACD below signal → bearish crossover intact |
| Momentum | MACD Hist | −0.72 | Stable, not accelerating |
| Momentum | RSI | 36.7 | Weak, not oversold; failed bounce from 28.8 |
| Volatility | ATR | 3.10 | Elevated/rising (~1.7% of price) |
| Volatility | Boll mid / UB / LB | 188.80 / 199.40 / 178.19 | Wide bands; price in lower half |
| Volume | VWMA | 185.45 | Price below → volume-confirmed distribution |
| **First resistance** | 10-EMA/VWMA | **~185.4** | Rally ceiling |
| **Trend-repair resistance** | Boll mid/50-SMA | **~188.8–189.3** | Reclaim = trend repair |
| **Critical support** | 200-SMA / Jan lows | **180.2–180.9** | Long-term line in the sand |
| **Downside target** | Bollinger LB | 178.19 | Next level if 180 breaks |
| **Overall bias** | — | — | **Bearish near/medium-term correction within intact long-term uptrend** |

*All figures above are drawn from the verified snapshot and indicator outputs dated 2024-01-17. Percentage relationships are computed directly from the cited closing prices on the stated dates.*