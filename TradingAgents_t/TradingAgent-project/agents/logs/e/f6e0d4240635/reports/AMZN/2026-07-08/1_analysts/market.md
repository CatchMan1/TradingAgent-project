# AMZN — Technical Analysis Report (as of 2026-07-08)

## Data integrity note
All OHLCV and indicator values below are taken from the **verified market snapshot for AMZN dated 2026-07-08**, which is internally consistent with the `get_indicators` outputs (RSI 49.41, MACD −2.53, signal −4.17, ATR 7.70, VWMA 236.80, 50-SMA 254.60, 200-SMA 233.17, 10-EMA 241.55). I found **no discrepancy** between the raw price feed and the snapshot. The snapshot additionally supplied Bollinger Bands (mid 239.68 / upper 250.37 / lower 229.00) and a positive MACD histogram (+1.63), which I use.

**Latest verified bar (2026-07-08):** Open 244.27 · High 244.80 · Low 240.52 · **Close 243.62** · Volume 29.65M.

---

## 1. Multi-timeframe trend structure

AMZN is caught in a **conflict between timeframes** — this is the single most important observation for the current setup.

- **Long-term (bullish):** Price (243.62) sits **above the 200-SMA (233.17)**, and that 200-SMA is gently rising (232.8 on 6/22 → 233.17 on 7/8). The primary uptrend is intact.
- **Medium-term (corrective/bearish):** Price is **below the 50-SMA (254.60)**, and the 50-SMA has rolled over — it peaked near **257.10 on 6/18** and has declined every session since. This is the overhead lid on the current bounce.
- **Short-term (recovering/bullish):** Price (243.62) is **back above the 10-EMA (241.55)**, and the 10-EMA has turned up from its 6/29 trough (237.33) → 241.55.

The 50-SMA remains above the 200-SMA (254.60 > 233.17), so the **golden-cross structure is still technically intact**, but the spread is **narrowing** (≈24.3 pts on 6/18 → ≈21.4 pts on 7/8). The market is mid-way through a mean-reversion rebound inside a larger medium-term down-swing.

**Context of the swing:** AMZN peaked intraday at **278.56 on 2026-05-05**, sold off to an intraday low of **225.55 on 2026-06-25** (close 227.01), and has since rebounded to 245.98 (7/7 close) before easing to 243.62. That is roughly a **~19% peak-to-trough decline** (arithmetic from those two concrete prints) followed by a ~8% recovery off the low.

---

## 2. Momentum

- **MACD (line −2.53 / signal −4.17 / histogram +1.63):** The MACD line is still **below zero** (i.e., the swing momentum was negative), but it has **crossed decisively above its signal line** and the histogram is **positive and expanding** (from −6.87 on 6/25 to +1.63 now). This is a classic **bullish momentum crossover inside oversold territory** — an early-recovery signal, not yet a confirmed trend reversal.
- **RSI 49.41:** Firmly **neutral**. RSI bottomed at **32.46 (6/10)** and again near **33.63 (6/25)** — testing oversold but not deeply — and has recovered to the mid-40s/50 area. Neutral RSI means there is **no mechanical ceiling or floor** here; price has room to run in either direction. The absence of a fresh overbought (>70) reading means the bounce is not yet stretched.

Momentum is **constructively turning up** but is not yet confirmed — it needs price confirmation (a hold above the 10-EMA/Bollinger mid) to be trusted.

---

## 3. Volatility & risk (ATR, Bollinger)

- **ATR 7.70** (~3.2% of price): Volatility is **elevated** relative to the calmer May period (ATR ≈6.7). It ratcheted up through June (7.0 → 8.59 on 6/29) and is now easing slightly. This matters for risk sizing — stops must be wider than in a low-vol regime.
- **Bollinger Bands (mid 239.68 / upper 250.37 / lower 229.00):** Price (243.62) sits in the **upper half** of the band, above the middle line. The bands are **wide** (≈8.9% width), reflecting the recent volatility. Price is **not** pinned to either extreme, so there is no immediate mean-reversion edge from the bands alone — but the **mid-line (239.68)** is the pivotal short-term pivot, and the **upper band (250.37)** converges with 50-SMA resistance near 250–255.

Taken together: elevated volatility + a mid-band price = a market that is **coiling**, awaiting a directional resolution rather than one that is extended.

---

## 4. Volume confirmation (VWMA + volume events)

- **VWMA 236.80:** Price (243.62) is **above** the volume-weighted average, a modest bullish tilt. Critically, the VWMA has **flattened** over the last ~7 sessions (236.5–237.0), indicating the volume-weighted center of gravity has **stopped falling** — consistent with a base forming.
- **Capitulation signature:** On **2026-06-26**, volume spiked to **248.4 million** (~5–8× a normal session) right at the swing low (close 232.69 near the 225.55 intraday low), immediately followed by a push to 240.14 (6/29). This prints as a likely **capitulation / high-volume absorption** event at the low — supportive of the current recovery, though it needs follow-through.

The support cluster of **VWMA (236.80) + 200-SMA (233.17) + Bollinger lower (229.00)** defines a meaningful "floor" zone. As long as price holds above it, the volume structure argues for accumulation.

---

## 5. Key levels map (from verified data)

| Level | Value | Role |
|---|---|---|
| 50-SMA | **254.60** | Primary overhead resistance (declining) |
| Bollinger upper | **250.37** | First resistance / breakout trigger |
| Recovery high (intraday) | 248.93 (7/7) | Immediate swing high |
| **Spot close** | **243.62** | — |
| 10-EMA | 241.55 | Short-term trend pivot (hold = bullish) |
| Bollinger mid | 239.68 | Short-term pivot |
| VWMA | 236.80 | Volume-weighted support |
| 200-SMA | 233.17 | Long-term trend line (key support) |
| Bollinger lower | 229.00 | Band support |
| June swing low | 227.01 close / 225.55 low | Structural breakdown level |

---

## 6. Scenarios & actionable trade ideas

**Bullish (recovery continuation) — base case while price holds 241.5+**
- Trigger: sustained close above the **10-EMA (241.55)** and **Bollinger mid (239.68)**, ideally reclaiming 248.93.
- Path: first target the **250–255 resistance zone** (Bollinger upper 250.37 + 50-SMA 254.60). A decisive close **above 254.60** would mark a genuine trend repair and open the door toward the April/May highs (~264–275).
- Momentum (MACD histogram expanding) and the June capitulation-volume base support this. Position sizing should account for ATR ~7.7 — a swing stop of ~1.5×ATR ≈ **11–12 points** below entry (e.g., beneath 236.80 VWMA) is reasonable.

**Bearish (bounce fails) — invalidation**
- Trigger: a close back **below 239.68** followed by a break of the **236.80 VWMA / 233.17 200-SMA** cluster.
- Then the bounce is over and the **June low 227.01 / 225.55** and **Bollinger lower 229.00** come into play. A break of 225.55 would confirm the medium-term downtrend resuming.

**Neutral / range**
- Given RSI 49 and mid-band price, the highest-probability near-term behavior is **range-bound consolidation between ~236 and ~255**. Range traders can buy the 236–240 support cluster (VWMA/Boll mid) and sell into 250–255 (Boll upper/50-SMA), with stops just outside each edge.

**What tilts the odds:** The multi-timeframe picture is mixed — short-term momentum and the volume base are bullish, but the declining 50-SMA and intact bearish medium-term structure mean the bounce must *prove itself* by reclaiming the 250–255 band before the long-term uptrend can be trusted to resume.

---

## 7. Summary table

| Dimension | Reading (2026-07-08) | Signal |
|---|---|---|
| Spot close | 243.62 | — |
| Long-term trend | Price > 200-SMA 233.17 (rising) | **Bullish** |
| Medium-term trend | Price < 50-SMA 254.60 (falling) | **Bearish / corrective** |
| Short-term trend | Price > 10-EMA 241.55 (turning up) | **Bullish** |
| MACD | −2.53 line, −4.17 signal, +1.63 histogram | **Bullish crossover, still sub-zero** |
| RSI | 49.41 | **Neutral** (room both ways) |
| Bollinger | Mid 239.68 / Up 250.37 / Low 229.00 | Price upper-half, no extreme |
| ATR | 7.70 (~3.2%) | **Elevated volatility** — wide stops |
| VWMA | 236.80 (flattening) | Price above; **support base** |
| Volume | 6/26 spike 248.4M at the low | Likely **capitulation/accumulation** |
| Nearest support | 241.55 / 239.68 / 236.80 / 233.17 | Staged floor |
| Nearest resistance | 248.93 / 250.37 / 254.60 | Overhead lid |
| Overall bias | Rebound within a medium-term pullback | **Cautiously constructive; needs >255 to confirm** |

**Bottom line:** AMZN is in a *short-term recovery* (MACD bullish cross, price back above the 10-EMA, rising off a high-volume low) *inside a still-bearish medium-term structure* (below a declining 50-SMA). The trade is to respect the 236–240 support cluster as the risk line and treat 250–255 as the gate that must be cleared to confirm a durable trend reversal. Elevated ATR (~7.7) demands wider stops and smaller size.

*Indicators selected (8): close_50_sma, close_200_sma, close_10_ema, macd, macds, rsi, atr, vwma — chosen to give non-redundant coverage of trend (3 timeframes), momentum (MACD pair + RSI), volatility/risk (ATR), and volume-weighted confirmation (VWMA), supplemented by Bollinger Bands from the verified snapshot.*