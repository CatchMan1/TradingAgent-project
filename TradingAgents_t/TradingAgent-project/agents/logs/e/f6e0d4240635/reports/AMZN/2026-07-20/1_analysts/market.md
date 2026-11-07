# AMZN — Multi-Timeframe Technical Report (as of close 2026-07-20)

## 0. Data integrity note
`get_stock_data`, `get_verified_market_snapshot`, and `get_indicators` all agree on the 2026-07-20 session: **O 248.76 / H 252.89 / L 248.00 / C 249.99, volume 32,406,500**, with RSI 54.04, MACD 0.824, MACD signal −0.622, histogram 1.446, ATR 7.454, VWMA 245.58, 50-SMA 251.633, 200-SMA 234.215, 10-EMA 247.599, Bollinger mid/upper/lower 242.34 / 256.65 / 228.03. **No discrepancies found between vendors** — all numbers below are the verified snapshot values unless a date is explicitly attached from the historical series.

## 1. Regime diagnosis: a coiled "trend-repair" market, not a clean trend
AMZN is in a three-way conflict across timeframes, which is the single most important thing to understand before acting:

- **Long-term (bullish):** Close 249.99 sits **+6.7% above a rising 200-SMA (234.21)**, which has climbed every session since at least 2026-06-10 (232.39 → 234.21). That is the signature of an intact primary uptrend.
- **Medium-term (bearish/decaying):** The **50-SMA is falling hard** — 257.10 on 2026-06-18 → 253.10 on 2026-07-15 → 251.63 on 2026-07-20 — and price is **0.65% below it**. In the last 28 sessions, the *only* close above the 50-SMA was 2026-07-15 (254.96 vs 253.10), and it was surrendered the very next day.
- **Short-term (bullish):** Since the 2026-06-25 capitulation close of 227.01, price has built a clean **sequence of higher lows — 225.55 (2026-06-25), 240.52 (2026-07-08), 243.59 (2026-07-17)** — a **+10.1% recovery** to 249.99, with a rising 10-EMA (237.59 on 2026-06-25 → 247.60 on 2026-07-20).

Net: price is sandwiched between a rising 200-SMA and a falling 50-SMA. This is a **transitional/coiling regime**, and coiling regimes are resolved by a range break, so the correct stance is *conditional* rather than directional.

## 2. Momentum: bullish crossover with an early deceleration warning
This is the most nuanced signal in the data, and it is genuinely two-sided:

**Bullish evidence:**
- MACD crossed **above its signal line on 2026-07-01** (histogram −0.101 → +0.470) and the histogram has been positive for 14 consecutive sessions.
- MACD crossed **above zero on 2026-07-15** (0.260) and has extended to 0.824 — the first positive MACD reading in the visible window.
- The signal line is rising steeply: −5.65 (2026-06-30) → −0.62 (2026-07-20).
- RSI repaired from **33.63 on 2026-06-25 to 54.04** — recovered without ever becoming overbought, meaning there is *plenty of headroom* to 70.

**Bearish/cautionary evidence:**
- The **MACD histogram has contracted for four straight sessions: 2.124 (2026-07-15) → 1.946 → 1.576 → 1.446**. Momentum is still positive but *decelerating* precisely as price ran into the 50-SMA.
- RSI peaked at **60.14 on 2026-07-15** and is now 54.04. Momentum has not made a higher high on the 2026-07-20 rebound.
- **Two consecutive failed upper-band breakouts:** on 2026-07-15 the high of 256.48 pierced the upper Bollinger band (254.80) and closed back inside (254.96); on 2026-07-16 the high of 258.08 pierced the band (255.38) and reversed to close at 249.89 — a **bearish reversal day closing near the low (248.00)** on elevated volume (45.34M). That is distribution, not accumulation, at the highs.

## 3. Volume: the recovery has volume support, but the last push does not
- **VWMA is confirming the uptrend** — 236.88 (2026-07-10) → 237.87 → 238.81 → 240.52 → 244.79 (2026-07-17) → 245.58 (2026-07-20). That acceleration in a volume-weighted average is the strongest single piece of bullish corroboration in this dataset: buyers are paying up in size, not just on thin prints. Price is **+1.8% above VWMA**.
- **But**: the 2026-07-20 advance (+1.12% from 247.23) came on **32.4M shares, roughly two-thirds of the 20-session average (~49M ex the 248M outlier)**. A light-volume rebound into resistance is a lower-quality signal.
- Historical volume signatures to respect: **248.4M on 2026-06-26** (by far the largest in the 158-row window; next highest 179.2M on 2026-02-06) accompanied a sharp reversal off the low, and **101.0M on 2026-04-30** accompanied a gap-up-and-fade from a 273.88 high to a 265.06 close. This name repeatedly produces violent event-driven gaps (also 2026-02-05: 232.99 → 222.69, then 2026-02-06: 222.69 → 210.32, on 103.5M/179.2M shares). **Gap risk is a first-order consideration for anyone holding through late July.**

## 4. Volatility: compressing — a breakout setup is building
ATR has contracted from **8.59 (2026-06-29) to 7.45 (2026-07-20)**, about **3.0% of price**. Meanwhile the Bollinger bands have flipped from collapsing to expanding at the top: upper band 250.59 (2026-07-07) → 256.65 (2026-07-20) while the lower band is flat at ~228.0. **A tightening ATR against widening upper bands after a higher-low sequence is a classic pre-breakout coil.** Use ATR, not fixed percentages, for risk: a 1.5×ATR stop is ~$11.2; a 1×ATR stop is ~$7.5.

## 5. Actionable levels (all derived from tool output)
| Level | Price | Basis |
|---|---|---|
| Resistance 3 | **273.88–278.56** | 2026-04-30 high / 2026-05-05 high |
| Resistance 2 | **263.99–265.06** | 2026-04-24 / 2026-04-30 closes (heavy-supply shelf) |
| Resistance 1b | **256.65–258.08** | Upper Bollinger band / 2026-07-16 high (rejection zone) |
| Resistance 1a | **251.63–252.89** | 50-SMA / 2026-07-20 high |
| **Spot** | **249.99** | 2026-07-20 close |
| Support 1 | **247.07–247.60** | 10-EMA / 2026-07-17 close (247.23) |
| Support 2 | **243.59–245.58** | VWMA (245.58) / 2026-07-17 low (243.59) |
| Support 3 | **242.34** | Bollinger middle / 20-SMA |
| Support 4 | **227.01–234.21** | 200-SMA (234.21) / 2026-06-25 close low (227.01) |

## 6. Two "tell" signals to watch in the next 5 sessions
1. **10-EMA vs 50-SMA convergence.** Gap is currently **$4.03** (247.60 vs 251.63). On 2026-07-20 the 10-EMA rose $0.53 while the 50-SMA fell $0.50 — a ~$1.03/day closure. If price merely holds flat, a **10-EMA/50-SMA bullish cross could occur within roughly 4–6 sessions**. Because the 50-SMA is *falling* (~$0.50/day), a flat price will mechanically "reclaim" it around 249–250 within a week. **Treat that mechanical cross as low-information**; demand a close above 252.89 on volume ≥45M.
2. **MACD histogram inflection.** A histogram cross back below zero (currently 1.446 and falling) with price under 247.07 would invalidate the short-term recovery and reopen 242.34, then 234.21.

## 7. Trade construction
- **Bullish trigger (preferred):** Daily close **above 252.89** with volume >45M, ideally after a successful retest of 247–248. Stop 1.5×ATR ≈ **241.7** (below the 242.34 mid-band). Targets: **256.65 → 263.99 → 273.88**. Reward:risk to the second target is roughly 2.4:1.
- **Bearish trigger:** Rejection at 251.63–252.89 confirmed by a **negative MACD histogram cross** and a close below **247.07**. Stop above the rejection high. Targets **242.34 → 234.21**.
- **Range/neutral (highest-probability base case given the coil):** 242.34–252.89 chop. Fade strength into 251–257, buy 243–246 with tight 1×ATR stops, and **do not add size into the 256–258 rejection zone** that has already failed twice on 2026-07-15 and 2026-07-16.
- **Sizing:** With ATR at 7.45, a $100k account risking 1% ($1,000) on a 1.5×ATR stop ($11.18) sizes to ~89 shares. Reduce this by half if holding through a potential late-July event gap.

## 8. Bottom line
AMZN is a **bullish primary trend (above a rising 200-SMA) repairing a medium-term correction (below a falling 50-SMA)**, with short-term momentum and volume-weighted price both pointing up but *decelerating into a well-defined resistance cluster at 251.6–258.1*. The setup is constructive but not confirmed: volume-weighted averages say buyers are in control, while the MACD histogram roll-over and the two failed upper-band pokes say the last 3% of the advance was sold. **The trade is a breakout trade, not a trend-following trade — wait for 252.89+ on volume, or buy the 243–247 retest, and avoid the middle of the range.**

### Key points summary

| Dimension | Reading (2026-07-20) | Interpretation | Actionable takeaway |
|---|---|---|---|
| **Price** | 249.99 (H 252.89 / L 248.00) | Rebounded +1.12% from 247.23 | Mid-range, just under resistance |
| **50-SMA** | 251.633, falling ~$0.50/day | Medium-term downtrend | Price 0.65% below = overhead supply; mechanical reclaim is low-quality |
| **200-SMA** | 234.215, rising | Long-term uptrend intact | 234.21 is the line in the sand; dip-buy zone |
| **10-EMA** | 247.599, rising fast | Short-term uptrend | $4.03 below 50-SMA; potential cross in ~4–6 sessions |
| **MACD / Signal** | 0.824 / −0.622 | Bullish cross 2026-07-01, zero-line cross 2026-07-15 | Trend repair confirmed on the medium-fast pair |
| **MACD histogram** | 1.446, 4th straight decline from 2.124 | Momentum decelerating at resistance | Watch for negative cross + close <247.07 as bear trigger |
| **RSI** | 54.04 (peak 60.14 on 2026-07-15) | Neutral, no overbought constraint | Room to 70; no valid divergence, but no momentum confirmation either |
| **Bollinger** | Mid 242.34 / UB 256.65 / LB 228.03 | Upper band expanding; two failed pokes (7/15, 7/16) | 256.65–258.08 = supply; 242.34 = mean reversion magnet |
| **ATR** | 7.454 (from 8.591 on 2026-06-29) | Volatility compressing ~3.0% of price | Coil pre-breakout; 1.5×ATR stop ≈ $11.2 |
| **VWMA** | 245.579, accelerating (236.88 on 7/10) | Volume confirming the recovery | Price +1.8% above; but 7/20 volume (32.4M) only ~2/3 of average |
| **Regime** | Transitional coil between rising 200-SMA and falling 50-SMA | Range 242.3–252.9, resolved only by a volume break | Trade the break or the retest, not the middle |
| **Risk flag** | 248.4M (6/26), 179.2M (2/6), 101.0M (4/30) volume events | History of violent gap repricing | Halve size into late-July event risk |