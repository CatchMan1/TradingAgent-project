# AMZN Technical Analysis Report — As of 2026-07-06

## 1. Snapshot & Price Context

AMZN closed **2026-07-06 at $244.16** (O 243.80 / H 246.04 / L 240.88), on volume of ~40.0M shares. This is the latest row in the verified snapshot and is treated as the source of truth for all price/indicator levels below.

The dominant structural story is a **medium-term correction inside a still-intact long-term uptrend**, with the stock now in a **multi-week rebound**:

- **Peak:** $274.99 closing peak on 2026-05-06 (intraday highs reached ~276–278.5 on 2026-05-04/05).
- **Trough:** $227.01 closing low on 2026-06-25 (intraday low $225.55). That is a **~17.5% peak-to-trough drawdown** on a closing basis.
- **Rebound:** $227.01 → $244.16 = **+7.55% off the low**, with price reclaiming several key averages.

The recovery has been stair-stepped: a sharp reversal day on **2026-06-26** (close $232.69 on an outsized **248.4M** shares — ~4–5× typical volume, consistent with a quarter-end/index event) followed by a grind higher into the first week of July.

## 2. Indicator Selection & Rationale

I selected **8 complementary indicators** spanning trend, momentum, volatility, and volume — deliberately avoiding redundancy (e.g., no RSI + Stochastic overlap):

| Indicator | Value (2026-07-06) | Why it's suitable here |
|---|---|---|
| **close_50_sma** | 255.19 | Medium-term trend & the key overhead resistance; the market is currently in a correction between the 50- and 200-day averages. |
| **close_200_sma** | 233.03 | Long-term trend benchmark and support confluence; the June dip tested this zone. |
| **close_10_ema** | 240.00 | Short-term momentum / entry timing; price just crossed back above it, signaling the rebound. |
| **macd / macdh** | -3.69 / +1.29 (signal -4.98) | Momentum crossover: histogram turned positive = improving momentum, though still sub-zero (bearish territory). |
| **rsi** | 50.05 | Gauges the oversold-recovery; now neutral, neither stretched nor washed out. |
| **boll (middle)** | 239.76 (UB 250.60 / LB 228.93) | Dynamic benchmark + volatility envelope to frame breakout vs. mean-reversion risk. |
| **atr** | 8.00 | Elevated volatility → position sizing and stop placement. |
| **vwma** | 237.00 | Volume-weighted confirmation of the rebound (price now above VWMA). |

## 3. Trend Structure (Moving Averages)

- **Price vs. 200 SMA (233.03):** Close at $244.16 is **+4.8% above** the 200 SMA, which is *slowly rising* (232.8 → 233.0 over the past week). The long-term uptrend remains intact. Notably, the June 22–25 sell-off briefly pierced below the 200 SMA (June 25 close $227.01) before rapidly reclaiming it — the 200 SMA acted as a **confluence floor**.
- **Price vs. 50 SMA (255.19):** Close is **-4.3% below** the 50 SMA, which is *declining* (peaked ~257.1 on 2026-06-18, now 255.2). This is the clearest sign the **medium-term trend is still down**; the 50 SMA is the pivotal resistance that must be reclaimed to confirm a full trend reset.
- **Price vs. 10 EMA (240.00):** Close is **above** the rising 10 EMA (which bottomed ~236.7 on June 26). Short-term momentum has flipped constructive.
- **MA alignment:** 50 SMA (255.2) > 200 SMA (233.0) > price (244.2) is a *bullish-but-correcting* stack. The 50/200 golden-cross gap is **narrowing** as the 50 SMA rolls over — worth monitoring, though a death cross is nowhere near imminent given the ~22-point gap.

**Read:** Price has reclaimed the two lower rails (200 SMA and 10 EMA) but remains capped under the declining 50 SMA. This is a textbook **rebound inside a correction**, not yet a confirmed new uptrend leg.

## 4. Momentum (MACD & RSI)

- **MACD:** Line at **-3.69**, signal at **-4.98**, histogram **+1.29 and expanding** (turned positive ~2026-07-01 from a June trough near -6.9). This is a **bullish crossover** — momentum is improving — but the MACD line remains **below zero**, so the intermediate-term momentum is technically still negative. Constructive, but early.
- **RSI:** **50.05**, dead neutral. RSI bottomed at **32.5 on 2026-06-10** and again ~33.6 on 2026-06-25 (never deeply oversold), then climbed steadily back to the midline. This confirms selling pressure exhausted without a capitulation, leaving **room in both directions** — no overbought constraint yet, but also no oversold cushion.

**Read:** Momentum has clearly turned up from the June low (positive histogram, RSI recovery to neutral), but the sub-zero MACD line argues this is a **repair rally** that still needs follow-through above the 50 SMA to become a durable trend.

## 5. Volatility (Bollinger Bands & ATR)

- **Bollinger:** Middle **239.76**, Upper **250.60**, Lower **228.93**. Price ($244.16) sits in the **upper half** of the bands, **+1.8% above the middle** and ~2.6% below the upper band. The band width (~21.7) is wide, reflecting elevated realized volatility. The June 25 close near $227 tracked **at/below the lower band** — a classic stretched/reversal zone — and price has since mean-reverted back through the middle band.
- **ATR:** **8.00**, up from ~6.6–6.7 in mid-May (peak 8.59 on 2026-06-29). Volatility is **elevated and only now easing**. This matters for risk: stops need to be wider (roughly 1–1.5× ATR ≈ $8–12) to avoid noise-triggered exits, and position sizes should be scaled down accordingly.

## 6. Volume Confirmation (VWMA)

- **VWMA:** **237.00**, and price ($244.16) is **above it** — a mildly bullish confirmation that recent buying is occurring at higher prices than the volume-weighted norm.
- The VWMA had been declining through June (peaking ~268 in mid-May → ~236.5 late June) and has now **flattened**, mirroring the price stabilization.
- The **2026-06-26 volume spike (248.4M)** on an up-close reversal is the most important volume signal in the dataset — it marked a shift in the supply/demand balance near the lows and preceded the current recovery.

## 7. Key Levels Map (tool-supported)

- **Resistance:** $246.04 (2026-07-06 high) → $249.71 (2026-06-29 high) → **$250.60 (Boll upper)** → **$255.19 (50 SMA)** — the decisive trend line.
- **Support:** $240.00 (10 EMA) / $239.76 (Boll middle) → $237.00 (VWMA) → **$233.03 (200 SMA)** → $227.01 (2026-06-25 low) / $225.55 intraday.

## 8. Actionable Insights

1. **Bias is turning constructive but unconfirmed.** The rebound off $227 has reclaimed the 200 SMA, 10 EMA, Bollinger middle, and VWMA — a cluster of positive signals. But the declining 50 SMA (~$255) and sub-zero MACD keep the intermediate trend technically bearish. A **daily close above $250–255** would be the trigger that flips the medium-term picture bullish.
2. **Watch the $250–255 resistance belt.** This combines the June 29 swing high ($249.7), the Bollinger upper band ($250.6), and the 50 SMA ($255.2). Rejection here favors a return toward the $240/237 support zone; a clean break and hold above it opens the prior $265–275 range.
3. **Support is layered and well-defined.** $240 (10 EMA/Boll middle) and $237 (VWMA) are the near-term footing; the **$233 (200 SMA)** is the line in the sand. A close below $233 would invalidate the rebound thesis and re-expose $227/225.
4. **Momentum is improving but early.** The MACD bullish crossover (+ histogram) and RSI back to 50 support a "buy-the-dip-confirmation" stance for swing traders, but the sub-zero MACD line cautions against aggressive sizing until the 50 SMA is reclaimed.
5. **Volatility is elevated.** With ATR at 8.00, use ATR-based stops (~$8–12 buffer) and reduce position size; intraday swings of 3–4% remain likely.
6. **Volume needs to keep confirming.** The June 26 volume spike is a positive tell, but sustained upside should ideally come with volume above ~40M/share; fading volume on rallies toward $250+ would be a warning.

## 9. Summary Table

| Category | Indicator | Latest (2026-07-06) | Signal / Interpretation |
|---|---|---|---|
| Price | Close | $244.16 | +7.55% off 06-25 low ($227.01); ~17.5% below 05-06 peak ($274.99) |
| Trend (LT) | close_200_sma | 233.03 | Price +4.8% above; rising → **long-term uptrend intact** |
| Trend (MT) | close_50_sma | 255.19 | Price -4.3% below; declining → **medium-term still bearish** |
| Trend (ST) | close_10_ema | 240.00 | Price above; rising → **short-term constructive** |
| Momentum | macd | -3.69 | Below zero (bearish) but improving |
| Momentum | macdh | +1.29 | Positive & expanding → **bullish crossover signal** |
| Momentum | rsi | 50.05 | Neutral; recovered from ~33 low → **no overbought constraint** |
| Volatility | boll (mid/UB/LB) | 239.76 / 250.60 / 228.93 | Price upper-half, above middle → **mean-reverting higher** |
| Volatility | atr | 8.00 | Elevated (vs ~6.7 in mid-May) → **wider stops, smaller size** |
| Volume | vwma | 237.00 | Price above → **buying confirmation** |
| Key Resistance | — | 246 → 249.7 → 250.6 → 255.2 | Trend flip needs close > $250–255 |
| Key Support | — | 240 → 237 → 233 → 227 | Rebound invalid below $233 (200 SMA) |

**Bottom line:** AMZN is executing a credible **rebound from the June low within a larger correction**. Short-term momentum, breadth of reclaimed moving averages, and volume confirmation are all bullish-leaning, but the declining 50 SMA (~$255) and sub-zero MACD mean the recovery is **not yet a confirmed trend change**. The tactical trade is to respect $233 as the failure line, use $240/$237 as near support, and treat a decisive close above $250–255 as the confirmation to turn outright bullish.