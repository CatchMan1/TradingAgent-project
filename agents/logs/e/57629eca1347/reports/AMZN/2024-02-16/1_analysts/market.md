# AMZN (Amazon.com, Inc.) — Technical Report as of 2024-02-16

**Verified close: $169.51** (open 168.74 / high 170.42 / low 167.17 / volume 48,107,700). All price and indicator values below come from the verified snapshot and the cached indicator series; the `get_stock_data`, `get_indicators`, and `get_verified_market_snapshot` outputs were **mutually consistent** — no conflicting values were found, so no discrepancy flag is required. (One note: I did not use `mfi` from the snapshot because its returned scale, 0.4373, is not interpretable as a 0–100 money-flow index.)

---

## 1. Regime assessment: powerful uptrend now in a high-volatility digestion phase

AMZN has gone from a 2024-01-04 close of **$144.57** to **$169.51** on 2024-02-16, and from the 2023-10-26 close of **$119.57** to today's level — a trend that is clearly intact but currently *stalled* at the top of a very steep advance.

The structure is textbook bullish on the medium/long horizon:

| Measure | Value (2024-02-16) | Implication |
|---|---|---|
| close_50_sma | 156.4058 | Rising every session since mid-Jan (147.82 on 01-17) |
| close_200_sma | 137.2324 | Rising steadily (130.57 on 01-17) |
| 50 SMA vs 200 SMA | +13.97% spread | Golden-cross configuration, spread **widening** |
| Price vs 50 SMA | +8.38% | Extended, but not extreme for a trend leader |
| Price vs 200 SMA | +23.52% | Confirms a secular-stage uptrend |

The key nuance: **the 50-day is rising at roughly +0.5/day and the 200-day at +0.35/day** (156.41 vs 155.95 and 137.23 vs 136.90 one session apart). Both are being dragged up *by* price, meaning they are confirmations, not supports nearby. The nearest real dynamic support is **not** the 50 SMA at 156.41 — that is 7.7% below spot. Traders anchoring stops to the 50-day are taking far more risk than they realize.

## 2. Short-term structure has deteriorated: the Feb 2 earnings gap is being worked off

Timeline of the most recent, tool-supported price action:

- **2024-02-01 → 02-02:** close 159.28 → 171.81, a **+7.86% close-to-close move**, on a massive **117,218,300 shares** (Feb 2 opened at 169.19, above the Feb 1 high of 159.76). This left an unfilled gap/air pocket roughly **159.76 → 169.19**.
- **2024-02-09:** high 175.00, close 174.45 (the highest close in the dataset).
- **2024-02-12:** high **175.39** (marginal new high), but close only 172.34 — a rejection at the highs.
- **2024-02-13:** low **165.75**, close 168.64 (**−2.15%** vs Feb 12 close) on 56,345,100 shares — the gap's upper region was tested but **not filled** (165.75 held well above 159.76).
- **2024-02-14 → 02-16:** 170.98 → 169.80 → **169.51**, with highs of 171.21, 171.17, and 170.42 — a sequence of **lower highs** and a coil between roughly 167.2 and 171.2.

So price has spent **11 sessions consolidating a +7.9% shock**, and the top of that consolidation is being tested and rejected rather than broken.

## 3. Momentum is decelerating — a fresh MACD bearish crossover

This is the most actionable short-term signal in the dataset:

- **macd:** peaked at **5.5008 on 2024-02-12**, then 5.2295 → 5.1440 → 4.9242 → **4.6728** (Feb 16).
- **macds (signal):** 4.3832 → 4.5524 → 4.6707 → 4.7214 → **4.7117**.
- **macdh:** +1.1176 (Feb 12) → +0.6771 → +0.4732 → +0.2028 → **−0.0389 (Feb 16)**.

The histogram has now **crossed below zero for the first time since 2024-01-17** (when it was −0.0392). Note the symmetry: that January negative histogram was immediately followed by 13 sessions of positive, expanding momentum into the Feb 2 gap. The signal is *symmetric in magnitude but opposite in sign* — early, fragile, but worth respecting. A one-session negative histogram is a warning, not a confirmed trend reversal; traders should require 2–3 consecutive negative prints plus a lower low before treating it as a short signal.

**RSI adds a mild negative divergence:** 73.78 on 2024-02-02 and 72.43 on 2024-02-09, versus **67.90 on 2024-02-12** even as price printed its highest high (175.39). RSI has now cooled to **60.56**, which is the *healthy* end of the range — it has reset from overbought **without price breaking down**. This is the constructive interpretation: momentum is being digested, not destroyed. RSI at 60.6 in an uptrend historically leaves room in both directions, so it is not a standalone signal here.

## 4. Volatility has re-rated — position sizing must change

- **atr: 3.8056** on Feb 16, versus **2.9443 on 2024-01-29** — a **+29% expansion** in average true range in under three weeks.
- ATR is now **2.25% of price** ($3.81 / $169.51).
- **Bollinger width:** upper 178.5807 − lower 151.0833 = **27.50 points, i.e. 16.7% of the middle band (164.8320)**. On 2024-01-17 the same width was (157.7276 − 145.9114)/151.8195 = **7.8%**. Band width has **more than doubled** — the classic signature of a volatility expansion/breakout regime, not a mean-reverting coil.

Practical consequence: a stop that was valid at 1.5×ATR in late January (~4.4 points) is now too tight (~5.7 points minimum). Size positions to a fixed dollar risk using **ATR ≈ 3.81**, not a fixed share count.

**Where price sits in the bands:** %B = (169.51 − 151.08) / (178.58 − 151.08) ≈ **0.67**. Price is in the upper half of an expanding channel and **5.1% below the upper band** — not overbought on a band basis, which is consistent with a flag/pause rather than a blow-off top.

## 5. Volume validates the trend, but buying pressure is thinning

- **vwma: 167.6386** — price (169.51) sits **+1.12% above** the volume-weighted average. The volume-weighted trend is rising monotonically (165.00 on Feb 12 → 166.47 → 167.14 → 167.64), confirming that the Feb 2 gap was made on genuine institutional participation (117.2M shares), not a thin squeeze.
- **Caution:** the rally to 175.00/175.39 on Feb 9–12 happened on 56.99M and 51.05M shares — **less than half** the Feb 2 volume. Meanwhile the distribution day of Feb 13 (down 2.15%, low 165.75) came on **56.35M**. Volume is currently heavier on the down days than on the recent up days. That is a distribution tell and is why the MACD crossover deserves attention.
- Feb 16's 48.11M is the lightest of the last four sessions — the tape is drying up into the range high, which usually resolves directionally.

## 6. The eight indicators I selected and why

1. **close_10_ema (168.9839)** — price is only **+0.31%** above it. This is *the* line that defines the current short-term trend; losing it decisively would confirm the momentum breakdown. Chosen over a stochastic-type oscillator because it captures the same information with a trend filter.
2. **close_50_sma (156.4058)** — the medium-term trend/support reference and the anchor for the "how extended are we?" question (+8.38%).
3. **close_200_sma (137.2324)** — long-term regime confirmation; the 50>200 spread (+13.97%, widening) rules out a structural bear case.
4. **macd (4.6728)** — necessary for detecting the momentum inflection; I reconciled it with its signal and histogram rather than adding redundant oscillators.
5. **rsi (60.5639)** — independently measures the overbought reset and the Feb 9/Feb 12 divergence. Distinct from MACD because it is bounded and shows *exhaustion* rather than *rate of change*.
6. **boll_ub (178.5807)** — the breakout/upside target zone and half of the band-width read.
7. **boll_lb (151.0833)** — the other half of the width calculation (16.7% vs 7.8% on Jan 17) plus the downside volatility envelope.
8. **atr (3.8056)** — the only indicator here that is purely about *risk sizing and stop distance*; it is doing the work that no trend or momentum indicator does.

*(Ancillary cross-check, not part of the core eight: **vwma 167.6386**, used above to confirm the trend is volume-supported.)* I deliberately avoided pairing RSI with a stochastic/Williams %R, and avoided stacking MACD with a second momentum oscillator — that would be redundant in a regime this directional.

## 7. Actionable plan

**Bull case (primary, given the dominant trend):**
- Long bias remains valid while AMZN holds **above 165.75** (the Feb 13 low) — the gap zone above 159.76 stays unfilled, which is a sign of demand, not weakness.
- **Trigger 1 (higher-probability):** a reclaim of **171.21** (Feb 14 high) and then a close above **172.34** (Feb 12 close) on volume ≥ 55M would re-assert the uptrend and target the **175.00/175.39** highs.
- **Trigger 2 (breakout):** a decisive close above **175.39** on volume > 60M opens the **178.58** upper-band area; with width expanding, an overshoot toward the band is realistic.
- **Invalidation:** a close below the **10 EMA (168.98)** is a warning; a close below the **Feb 16 low of 167.17** followed by a break of **165.75** puts the **159.76 → 169.19 gap** in play, with the **50 SMA at 156.41** as the next structural floor.

**Bear case (tactical, not structural):**
- The setup for a short is *specific*: fresh MACD histogram < 0 (already true on Feb 16), RSI making lower highs, lower highs at 171.21/171.17/170.42, and lighter volume on rallies.
- Realistic downside objective is **165.75 → 164.83 (Bollinger middle)** and, if that fails, the **159.76** gap top. This is a counter-trend trade against a +13.97% 50/200 spread; keep it small and time-boxed.

**Risk management (ATR-based):**
- Structural risk from spot to the Feb 13 low is **169.51 − 165.75 = 3.76 points ≈ 0.99 × ATR** — a sensible, volatility-matched stop for a swing long.
- For a fresh long entry near 170, a 1.5×ATR stop is **≈5.7 points (~$164.3)**, which conveniently sits just under the gap-adjacent support cluster.
- Reduce position size ~25–30% versus late-January levels purely because ATR expanded from 2.94 to 3.81 (+29%) while the price level is only ~15% higher.

## 8. Summary table

| Dimension | Reading (2024-02-16) | Interpretation | Action |
|---|---|---|---|
| Close | **169.51** (O 168.74 / H 170.42 / L 167.17) | Coiling under 171–175 supply | Wait for resolution |
| Volume | 48.11M (vs 117.22M on 02-02) | Rally participation thinning | Needs >55–60M to confirm upside |
| 10 EMA | 168.9839 (price +0.31%) | Price riding the line | Losing it = first warning |
| 50 SMA | 156.4058 (price +8.38%) | Trend intact but far below | Not a usable near-term stop |
| 200 SMA | 137.2324 (price +23.52%) | Secular uptrend | Rules out structural bear case |
| 50 vs 200 SMA | 156.41 vs 137.23 = +13.97%, widening | Golden-cross regime | Strategic long bias |
| MACD / Signal / Hist | 4.6728 / 4.7117 / **−0.0389** | First bearish crossover since 01-17 | Confirmation needed (2–3 prints) |
| RSI | **60.5639** (from 73.78 on 02-02) | Overbought reset, no breakdown; lower high vs 02-12 price high | Neutral-to-constructive |
| Bollinger (lb / mid / ub) | 151.0833 / 164.8320 / 178.5807 | %B ≈ 0.67; width 16.7% vs 7.8% on 01-17 | Expanding volatility, room to 178.58 |
| ATR | **3.8056** (2.25% of price; +29% since 01-29) | Volatility re-rated | Widen stops, cut size |
| VWMA (ancillary) | 167.6386 (price +1.12%) | Volume-weighted trend still up | Trend is volume-supported |
| Resistance | 171.21 → 172.34 → **175.00/175.39** → 178.58 | Cluster of rejected highs | Breakout triggers |
| Support | 168.98 (10 EMA) → **167.17** → **165.75** → 164.83 → 159.76 | Gap air pocket below 165.75 | Invalidation levels |

**Bottom line:** AMZN is in a strong, confirmed medium- and long-term uptrend (50 SMA 13.97% above the 200 SMA, both rising; VWMA rising) that is currently *digesting* an earnings-driven +7.86% gap on Feb 2. The short-term tape has weakened — a fresh MACD bearish crossover, lower highs from 175.39, and declining volume on rallies — while RSI has reset to a neutral 60.56 rather than flashing a top. The asymmetry favors trading the resolution of the **167.17–171.21** coil: above 172.34 targets 175.39/178.58, below 165.75 opens the 159.76 gap. Size with ATR 3.81, not with fixed stops.