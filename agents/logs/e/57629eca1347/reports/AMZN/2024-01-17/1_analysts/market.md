# AMZN — Technical Analysis Report (as of the 2024‑01‑17 close)

**Instrument:** `AMZN` (Amazon.com, Inc.)
**Last verified session:** 2024‑01‑17 — O 151.49 / H 152.15 / L 149.91 / **C 151.71** / Vol 34.95M
**Verification note:** All indicator values below are taken from `get_verified_market_snapshot` for 2024‑01‑17 and cross‑checked line‑for‑line against `get_indicators`. They match exactly (50SMA 147.822, 200SMA 130.567, 10EMA 151.984, MACD 1.5204, Signal 1.5596, Histogram −0.0392, RSI 53.72, ATR 3.053, VWMA 150.895). No conflict between tools. One caveat: the snapshot also returns `mfi = 0.4367`, which is not on the standard 0–100 MFI scale; I have **excluded money flow** from this analysis rather than misread it.

---

## 1. Why these 8 indicators

| Indicator | Role in this specific setup |
|---|---|
| `close_200_sma` | Anchor of the multi‑month uptrend; needed to know whether this is a trend‑continuation dip or a trend break |
| `close_50_sma` | The medium‑term pivot — currently the single most important decision line below price |
| `close_10_ema` | Detects the short‑term inflection; price just lost it, which is the first warning of a stall |
| `macd` | Trend/momentum backbone; shows whether the December impulse is still alive |
| `macdh` | Converts MACD from a level to a *rate of change*; the sign flip on 01‑17 is the crux of the near‑term call |
| `rsi` | Neutral‑zone momentum gauge + divergence detector; AMZN has spent Jan oscillating 40–63, so 70/30 thresholds are not binding but slope is informative |
| `atr` | Position sizing and stop placement — volatility is compressed, which changes the correct stop distance |
| `vwma` | Confirms whether price is above or below the *volume‑weighted* cost basis; useful because volume has been drying up |

Deliberately excluded: Bollinger bands as separate calls (the verified snapshot already gives 151.82 / 157.73 / 145.91, so I use those without spending indicator slots), and I avoided stacking redundant oscillators (no StochRSI alongside RSI).

---

## 2. Trend structure — bullish primary, stalling secondary

**Long‑term (200 SMA) — firmly bullish.** 200SMA = **130.57**, rising every session (127.98 on 01‑02 → 130.57 on 01‑17, ≈ +0.26/day). Price at 151.71 sits **+16.2% above** it. This is not a market in danger of a primary trend break; it is a market far extended above its long‑term mean.

**Golden‑cross regime intact.** 50SMA **147.82** vs 200SMA **130.57** → spread of +17.26 points (**+13.2%**). The 50SMA has risen monotonically from 133.78 (11‑20) to 147.82 (01‑17), roughly +0.27/day. (I cannot date the actual crossover from the visible window, so I am not asserting a specific cross date.)

**Medium‑term (50 SMA) — bullish but price is compressing toward it.** Price is only **+2.63%** above the 50SMA. That gap was much wider in mid‑December: on 12‑18 close was 154.07 vs 50SMA 139.42 (+10.5%). In other words, **the 50SMA has been catching up to price** — the classic signature of a trend transitioning from impulse to consolidation, not a trend in free‑fall.

**Short‑term (10 EMA) — the first genuine crack.** 10EMA = **151.984**. The 01‑17 close of **151.71 is −0.18% below it** — the first close beneath the 10EMA since 01‑05 (and before that, since early January). Trace the sequence:

- 12‑29 close 151.94 vs 10EMA 152.15 → below
- 01‑02 → 01‑05: four consecutive closes below (01‑04: 144.57 vs 149.96)
- 01‑08 close 149.10 vs 10EMA 149.0989 → *marginally* reclaimed
- 01‑09 through 01‑16: six consecutive closes above, peaking 01‑11 at 155.18 vs 151.17
- **01‑17: 151.71 vs 151.98 → lost again**, and the 10EMA itself has flattened (152.15 on 12‑29 → 151.98 on 01‑17, i.e. no net gain in three weeks)

**Read:** short‑term momentum has gone from up to flat. The 10EMA rolling over while the 50SMA climbs is a neutral‑to‑bearish short‑term posture *inside* a bullish primary trend.

---

## 3. Momentum — a failed MACD reset is the key bearish tell

MACD history is the most informative series here:

| Date | MACD | Signal | Histogram |
|---|---|---|---|
| 2023‑11‑20 | 3.882 | — | +0.680 |
| 2023‑12‑06 | 2.694 | — | −0.546 |
| 2023‑12‑18 | 2.732 | — | **+0.142 (bull cross)** |
| 2023‑12‑22 | 3.136 | — | +0.263 (peak histogram) |
| 2024‑01‑04 | 1.341 | — | **−1.055** |
| 2024‑01‑05 | 0.859 | — | **−1.230 (histogram trough)** |
| 2024‑01‑11 | 1.462 | — | −0.064 |
| 2024‑01‑12 | 1.643 | — | **+0.094 (bull cross #2)** |
| 2024‑01‑16 | 1.650 | 1.569 | +0.080 |
| **2024‑01‑17** | **1.520** | **1.560** | **−0.039 (bear cross)** |

The January rally *did* produce a bullish MACD crossover on 01‑12 — but it was a very weak one (histogram peaked at only +0.094 versus +0.305 on 12‑19), and it **failed within three sessions**. MACD has now crossed back below its signal line with the histogram at −0.039. Structurally this is a **lower‑high in MACD** (1.65 on 01‑16 vs 3.14 on 12‑22) confirming that each rally attempt is carrying less momentum than the last.

**RSI:** 53.72 on 01‑17, down from 62.79 on 01‑11 and 68.05 on 12‑18.
- The 12‑18 reading of 68.05 came with a close of 154.07.
- The 01‑11 reading of **62.79 came with a HIGHER close of 155.18**. That is a **negative RSI divergence** — price made a marginally higher closing high on materially lower momentum.
- RSI bottomed at 40.2 on 01‑04 and has not breached 70 or 30 in the entire visible stretch. The indicator is squarely neutral, meaning it is **not** providing an oversold entry signal and is **not** confirming an overbought breakout either.
- RSI peaked at 68.05 on 12‑18 (close 154.07) — that is a *lower* price high than 155.18, again consistent with the momentum fade, though not a textbook clean divergence.

**Composite momentum verdict:** negative‑leaning. MACD bear cross, lower highs in MACD, lower RSI high against a marginally higher price high, and price below a flattening 10EMA.

---

## 4. Volatility, bands and the "coiling" pattern

- **ATR = 3.053**, i.e. **2.01% of price**. ATR compressed from 3.53 (11‑20) to a low of 2.806 (12‑28) and has ticked back up modestly to 3.05. This is *low* volatility for a name that moved 29.8% in ten weeks.
- **Bollinger (from verified snapshot):** middle 151.8195, upper 157.7276, lower 145.9114. **Bandwidth = 7.78% of the middle band.**
- Price at 151.71 is effectively **sitting on the middle band** (−0.07%). In the last five sessions it went from the upper band (01‑11 close 155.18 vs upper 157.73) back to the mid‑line. That is the definition of a **reversion to the mean inside a range**, not a breakout or breakdown.
- Upper band at **157.73** and the 01‑11 intraday high of **157.17** nearly coincide — this is a concrete, tool‑supported resistance shelf, not an invented one.

**The pattern I see:** AMZN built a December range (intraday roughly 144–156 across 12‑13 → 12‑29), broke above it intraday on 01‑11 (high 157.17), **failed to hold**, and has now retraced back into the top half of that same range. Combined with falling ATR and falling volume, this is a **coiled, indecisive market leaning against a ceiling** — a classic distribution‑risk / continuation‑risk coin flip that should be traded with triggers, not predictions.

---

## 5. Volume and the volume‑weighted cost basis

- **VWMA = 150.895.** Price is only **+0.54%** above the volume‑weighted average — the volume‑weighted buyer is essentially flat on the position. VWMA has been **flat since 01‑03** (151.248 → 150.895) despite price swinging from 148.47 to 155.18 and back. That flatness means **the marginal volume has been transacting around 150.5–151.5** — a genuine equilibrium zone.
- **Volume is drying up:** 01‑17 volume of **34.95M** is the lowest since 12‑28 and about **17% below the ~42.2M 20‑session average** (12‑18 → 01‑17). The December breakout day (12‑15, 110.09M; 12‑18, 62.51M) and the 01‑11 new‑high day (49.07M) showed volume expansion; the pullback since 01‑11 (49.07M → 40.48M → 41.38M → 34.95M) shows *contracting* volume.
- **Interpretation:** contracting volume on a pullback is mildly **constructive** (no evidence of heavy institutional distribution), but it equally signals **absent demand**. The 01‑11 new high on 49M — below the 12‑15 and 12‑18 volumes — is consistent with the momentum divergence: new price highs on lighter participation.

---

## 6. Concrete price levels (all from verified tool data)

**Resistance**
| Level | Source |
|---|---|
| 152.15 | 01‑17 intraday high (immediate) |
| 152.15→152.15 zone / 153.16 | 01‑16 close — must reclaim to repair short‑term trend |
| 154.99 / 156.20 | 01‑16 high / 01‑12 high |
| 157.17 | 01‑11 intraday high — the range ceiling |
| 157.73 | Bollinger upper band |

**Support**
| Level | Source |
|---|---|
| 151.98 | 10EMA (now overhead, flip level) |
| 150.90 | VWMA — volume‑weighted equilibrium |
| 151.82 | Bollinger middle band |
| 149.91 | 01‑17 session low |
| 148.21 / 148.33 | 01‑09 low / 01‑02 close cluster |
| **147.82** | **50SMA — the line in the sand** |
| 145.91 | Bollinger lower band |
| 145.52 / 144.05 | 12‑14 low / 01‑04 low (the January swing low) |

**Measured moves (directly computed from tool data)**
- 10‑26 close 119.57 → 01‑11 close 155.18 = **+29.78%** (the impulse leg)
- 12‑29 close 151.94 → 01‑04 close 144.57 = **−4.85%**
- 01‑04 close 144.57 → 01‑11 close 155.18 = **+7.34%** (the V‑recovery)
- 01‑11 close 155.18 → 01‑17 close 151.71 = **−2.24%**; from the 01‑11 high of 157.17 the drawdown is **−3.47%**

---

## 7. Actionable interpretation

**Base case (highest probability): range trade 148–157.** Price is at the mid‑point of a well‑defined range, momentum is neutral (RSI 53.7), volatility is compressed (ATR 2.0%), and price is pinned to the Bollinger mid‑line and the VWMA simultaneously. There is no edge in chasing here.

**Bullish trigger (preferred long entry):**
1. A close **back above 153.16** (the 01‑16 close) with MACD histogram turning positive again, OR
2. A **test of 148.2–147.8** (January gap area + 50SMA) that holds on light volume and reverses — this is the higher reward‑to‑risk entry because it aligns with a rising 50SMA.
- **Stop:** below **144.05** (01‑04 low). From a 148 entry that is ~4.0 points ≈ **1.3 × ATR**, appropriately tight given compressed volatility. A tighter tactical stop at 146.5 (below the 50SMA and roughly 0.5 ATR under it) is defensible but risks being shaken out by normal noise given the 50SMA is rising ~0.27/day.
- **Target:** 155.2 → 157.2 (the 01‑11 high / upper band). That yields roughly 2.2–3.0 : 1 reward‑to‑risk from the 148 area.

**Bearish trigger:**
- A close **below 147.82 (50SMA)** would break the last medium‑term support and put 145.91 (lower band) and 144.05 in play. A confirmed break of 144.05 invalidates the entire October–January advance structure at the swing level and would target the 140s. Note: taking out the 50SMA requires only a −2.6% move — very achievable within one ATR‑sized week (weekly ATR ≈ 5 × 3.05).

**What NOT to do:** do not treat the 01‑11 high as a breakout. It was rejected, MACD made a lower high, and volume on the new high was below the December breakout volumes. Do not treat RSI 53.7 as a buy signal — it is neutral, and the divergence is on the bearish side.

**Position sizing:** with ATR at 3.05 (2.0% of price), a 1% account risk per trade implies roughly a 0.33× notional position using a 1.3×ATR stop — i.e. smaller than a typical-volatility sizing. If ATR expands back toward the November 3.53 level, reduce size proportionally.

**Risk events:** this is a stock whose trend can gap on earnings; the technical framework above describes the *price* structure and will be superseded by a fundamental catalyst.

---

## 8. Summary table

| Dimension | Reading (2024‑01‑17) | Signal | Evidence |
|---|---|---|---|
| Primary trend | Close 151.71 vs 200SMA 130.57 | **Bullish** | +16.2% above a rising 200SMA (127.98 → 130.57 since 01‑02) |
| Golden cross | 50SMA 147.82 > 200SMA 130.57 | **Bullish** | Spread +17.26 pts (+13.2%), 50SMA rising ~0.27/day |
| Medium trend | Price +2.63% above 50SMA | **Bullish, compressing** | Gap narrowed from +10.5% on 12‑18 to +2.63% now |
| Short trend | Close 151.71 vs 10EMA 151.98 | **Bearish turn** | First close below 10EMA since 01‑05; 10EMA flat for 3 weeks |
| MACD | 1.520 vs signal 1.560 | **Bearish** | Histogram flipped to −0.039 on 01‑17; lower high 1.65 vs 3.14 (12‑22) |
| MACD structure | Two failed bull crosses | **Bearish** | 12‑18 cross peaked at +0.305 hist; 01‑12 cross peaked at only +0.094 |
| RSI | 53.72 | **Neutral** | Down from 62.79 (01‑11); negative divergence: higher close, lower RSI |
| Volatility | ATR 3.053 (2.01%) | **Compressed** | Off 11‑20 high of 3.53; lows 2.81 on 12‑28 |
| Bollinger | Mid 151.82 / UB 157.73 / LB 145.91 | **Mean-reverting** | Price at mid‑line; bandwidth 7.78%; UB ≈ 01‑11 high 157.17 |
| Volume | 34.95M vs ~42.2M 20‑day avg | **Contracting** | 17% below average; lowest since 12‑28; no distribution signature |
| Volume price | VWMA 150.90 | **Neutral** | Price only +0.54% above; VWMA flat since 01‑03 (151.25 → 150.90) |
| Structure | Failed 01‑11 breakout of 157.17 | **Range** | Retraced −3.47% from high; back inside December range |
| **Net stance** | **Constructive but on hold** | **Neutral / reduce** | Bullish primary trend + bearish short-term momentum = wait for a trigger at 148 or 153.2 |

**Bottom line on `AMZN`:** The multi‑month uptrend is intact and well‑supported by a rising 50/200 SMA structure, but the January tape shows a failed upside breakout at 157.17, a rejected 10EMA, a lower MACD high, a bearish MACD histogram flip, and a negative RSI divergence — all on drying volume. Treat 147.8–149.9 as the actionable accumulation zone and 153.2 as the momentum repair level; a close under 147.82 invalidates the constructive case and opens 145.9 → 144.05.