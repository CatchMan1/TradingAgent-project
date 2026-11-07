# AAPL — Technical & Trend Analysis
**Analysis date: 2026-07-15 (close) | Verified snapshot source: B‑project frozen rows**

---

## 1. Verified Snapshot (source of truth)

| Field | 2026-07-15 |
|---|---|
| Open | 317.62 |
| High | 328.73 |
| Low | 317.32 |
| **Close** | **327.50** |
| Volume | 60,957,600 |
| Change vs 2026-07-14 close (314.86) | **+12.64 pts / +4.01%** |

**Indicator values on the latest session (verified snapshot):**

| Indicator | Value | Read |
|---|---|---|
| close_10_ema | 312.9172 | Price 4.66% above |
| close_50_sma | 300.5286 | Price 8.97% above |
| close_200_sma | 273.4300 | Price 19.78% above |
| MACD | 6.6033 | Positive, expanding |
| MACD signal | 3.8369 | MACD above signal |
| MACD histogram | 2.7664 | Re-accelerating |
| RSI(14) | 68.7699 | Approaching overbought |
| Bollinger mid (20) | 301.9275 | Price 8.47% above |
| Bollinger upper | 329.8257 | Price 0.71% **below** upper band |
| Bollinger lower | 274.0293 | Band width ≈ 18.5% of mid |
| ATR(14) | 8.3273 | 2.54% of close |
| VWMA | 296.4191 | Price 10.48% above |
| MFI | 0.8146 | ⚠️ *scaled 0–1 (~81.5 on 0–100); flagging scale discrepancy — not used as a signal* |

> Discrepancy note: everything else reconciles cleanly between the raw OHLCV pull and the verified snapshot. The only ambiguity is the MFI value being reported on a 0–1 rather than 0–100 scale. I have not converted it into a hard signal.

---

## 2. Multi‑Timeframe Trend Structure — Strongly Bullish and Stacked

The moving-average complex is in textbook bullish alignment:

**Price (327.50) > 10 EMA (312.92) > 50 SMA (300.53) > 200 SMA (273.43)**

- **200 SMA is rising monotonically.** It has climbed every single session from 246.12 on 2026-03-17 to 273.43 on 2026-07-15. The long-term trend is unambiguously up.
- **50 SMA is rising faster than the 200 SMA**, moving from 260.02 on 2026-03-31 to 300.53 on 2026-07-15. The 50 SMA was already above the 200 SMA at the start of the retrieved indicator window (261.99 vs 246.12 on 2026-03-17), meaning the golden-cross regime has been in force throughout and the spread has widened modestly — a signature of a mature uptrend, not a fresh reversal.
- **The 10 EMA has just curled up hard.** It bottomed at 289.33 on 2026-06-29 and has risen sequentially to 312.92 by 2026-07-15. Price crossed back above the 10 EMA around 2026-07-02 (close 308.63 vs 10 EMA 293.59) and has stayed above it since — a clean short-term trend re-assertion after the June shakeout.

**Structural read:** The June episode (see §6) was a correction *within* an intact primary uptrend, not a trend break. The 200 SMA was never threatened: the June low close of 275.15 on 2026-06-25 stayed above the then-200 SMA (~269.2).

---

## 3. Momentum — A Fresh, Powerful Thrust Off a Washout

The momentum data tells the most actionable story:

**RSI trajectory (verified series):**
- 2026-05-28: 79.79 (overbought, peak)
- 2026-06-09: 42.64 (momentum collapse)
- **2026-06-25: 32.20 (near-oversold washout)**
- 2026-07-13: 64.16 → 2026-07-14: 61.45 → **2026-07-15: 68.77**

The RSI round-trip from ~80 → 32 → ~69 is a classic "reset-and-reload" pattern. At 68.77 it is knocking on the 70 threshold but is **not** yet an extreme reading, and importantly it has arrived there via a *fresh breakout* rather than by grinding sideways. In strong uptrends RSI can hold 70–80 for extended periods (as it did in late May), so 68.77 should be read as "strength, with limited headroom," not as an automatic sell signal.

**MACD (verified series):**
- Histogram bottomed at **−3.4986 on 2026-06-12**, then improved for eight straight sessions before the 2026-06-25 shock re-widened it to −2.7873.
- **Bullish MACD/signal crossover on 2026-07-02** (MACD −0.686 vs signal −0.947).
- **MACD crossed above zero on 2026-07-06** (0.879) — the regime flip from bearish to bullish momentum.
- MACD line has since accelerated: 1.94 (07-07) → 2.96 → 3.95 → 4.61 → 5.24 → 5.47 → **6.60 (07-15)**.
- Histogram: 2.74 (07-09), 2.72, 2.68, **2.33 (07-14)**, then **2.77 (07-15)**. The brief three-session fade in the histogram was *resolved upward* on the breakout day — that is a bullish re-acceleration, not a divergence.

**Divergence check:** I see no confirmed price/momentum bearish divergence in the supplied data. Price made a higher high on 07-15 (328.73) while MACD made a higher high (6.60) and RSI made a higher high (68.77). Momentum is confirming price.

---

## 4. Volatility & Bollinger Positioning — Riding the Upper Band, Bands Expanding

- Close 327.50 sits **0.71% below the upper band (329.83)** — price is pressing the top of the envelope. In trending markets, "riding the band" is continuation behavior; the tell is that the *upper band itself is rising steeply* (312.68 on 2026-07-01 → 329.83 on 2026-07-15), which means the envelope is chasing price upward rather than price merely spiking into a static ceiling.
- **Band width ≈ 18.5%** of the middle band ((329.83 − 274.03) / 301.93), versus a much tighter envelope in mid-June (~10–11% around the 303–304 mid). Volatility is expanding in the direction of the trend — a breakout regime, not a squeeze.
- **ATR is 8.33 (2.54% of price)**, elevated versus the 5.5–6.0 range in late May. ATR bottomed... rather, it *peaked* at 8.74 on 2026-07-02, cooled to 7.90 on 2026-07-14, and re-ticked to 8.33 on the 07-15 range expansion (daily range 317.32–328.73 = 11.41 pts, ≈1.37× ATR).

**Implication:** Stops placed inside 1× ATR (≈8.3 pts) of price will be noise-harvested. Risk levels must be ATR-scaled (§7).

---

## 5. Volume / Participation — Breakout Is Volume-Supported

- 2026-07-15 volume **60.96M** versus roughly **51.1M average across the 18 "normal" sessions** in the last 20 trading days (computed from the returned rows, excluding the two anomalous prints of 107.0M on 06-25 and 261.8M on 06-26). That is roughly **+19% above normalized participation** on the breakout day.
- **VWMA = 296.42**, with price 10.48% above it. Two readings: (a) volume-weighted buyers are heavily in profit, which is supportive; (b) a double-digit gap above VWMA is a *mean-reversion magnet* and an extension warning. Historically in this dataset, gaps of this magnitude above VWMA preceded either strong continuation (May) or sharp give-back (late June).
- 2026-06-26's 261.8M print is a clear outlier (index/rebalance-type event); I would not treat it as directional conviction.

---

## 6. The June Shock — Context That Shapes the Risk Profile

On **2026-06-25** AAPL closed at **275.15**, down **6.12%** from 293.08 on 2026-06-24, on 107.0M shares, with an intraday low of 273.75. From that low, the stock has recovered to **327.50 — +19.63%** in 14 trading sessions. This V-shaped recovery off a high-volume down day is powerful but also means:
- The rally is **steep and un-refreshed**; recent buyers are tightly clustered in the 300–327 zone.
- Late-June lows (275.15 close / 273.75 intraday) now coincide with the **lower Bollinger band (274.03)** — a confluence that would be the last line of defense in a failed-breakout scenario.

---

## 7. Actionable Levels & Trade Construction

**Resistance / extension zones (all derived from returned rows):**
- **328.73** — 2026-07-15 high; also the highest high in the entire Dec-2025→Jul-2026 dataset. A close above this confirms continuation.
- **329.83** — Bollinger upper band; immediate friction zone.
- ~332–335 — 1× ATR extension above today's high (328.73 + ~3.3 to ~8.3).

**Support ladder:**
| Level | Source |
|---|---|
| 317.32 | 2026-07-15 low (immediate) |
| 315.78 / 315.45 | 2026-07-13 low / 2026-06-02 high (breakout shelf) |
| **312.92** | **10 EMA — trend-health line for swing longs** |
| 311.91 | 2026-07-14 low |
| 307.0–308.2 | July consolidation (07-06 low 307.00, 07-08 low 307.05) |
| **300.5–301.9** | **50 SMA (300.53) + Bollinger mid (301.93) — must-hold for the primary trend** |
| 296.42 | VWMA |
| 274.0–275.2 | Lower band (274.03) + 06-25 washout low |

**Suggested construction:**
- **Trend-following long (primary stance):** Buy breakouts/retests above 317–320 or on a controlled pullback to the 10 EMA (312.9). Protective stop **1.5× ATR ≈ 12.5 pts** below entry (≈315.0 if entered at 327.5), or a hard stop below the 07-14 low of 311.91 for wider tolerance. Invalidated on a decisive daily close below the 50 SMA/Bollinger mid cluster (~301).
- **Position sizing:** With ATR at 8.33, size positions at ~55–60% of what you would use at the calm-May ATR of ~5.5–6.0 for the same dollar risk.
- **Do not add aggressively into 328–330** on the first touch: RSI at 68.8, price 0.7% under the upper band, and 10.5% above VWMA make a 1–2 day pause or intraday flush a live probability. The 10 EMA is the natural place that flush would resolve.
- **Short-side caution:** There is no technical basis here for counter-trend shorts. Every trend, momentum, and participation measure is aligned upward. A bear case requires either a failed breakout (rejection at 328–330 with a close back under 315.5) or a break of ~301.

---

## 8. Why These 8 Indicators (Complementary, Non-Redundant)

| Indicator | Category | Why it earns a slot |
|---|---|---|
| **close_10_ema** | Short MA | Captures the post-June inflection and functions as the swing-trend health line |
| **close_50_sma** | Medium MA | Defines the intermediate trend and the 300-area must-hold pivot |
| **close_200_sma** | Long MA | Confirms the long-term regime; 50>200 spread validates the uptrend's maturity |
| **macd** | Momentum (trend-following) | Time-stamps the Jul-2 bullish crossover and Jul-6 zero-line reclaim |
| **rsi** | Momentum (bounded) | Independent measure of overbought risk; shows the 80→32→69 reset |
| *(macds / macdh reviewed as supporting detail)* | — | Used to confirm crossover timing and histogram re-acceleration; omitted from the core set to avoid MACD-triple redundancy |
| **boll_ub** | Volatility | Quantifies extension/breakout zone at 329.83 and the rising-envelope regime |
| **atr** | Volatility | Prices the stop distance and position size in a 2.5%-of-price volatility regime |
| **vwma** | Volume | Tests whether the breakout has volume behind it and flags the 10.5% extension gap |

Deliberately excluded: `boll` and `boll_lb` (middle/lower band derivable from context and less decision-relevant than the upper band in an upside breakout), `stochrsi` (redundant with RSI), and `macds`/`macdh` from the headline set (redundant with the MACD line, though reviewed).

---

## 9. Key Takeaways

| # | Observation | Evidence | Actionable Read |
|---|---|---|---|
| 1 | Perfect bullish MA stack | 327.50 > 10EMA 312.92 > 50SMA 300.53 > 200SMA 273.43 | Trend-following longs are aligned with the tape |
| 2 | New high on the dataset | 2026-07-15 high 328.73 > prior max 323.45 (07-13) | Breakout confirmation; resistance now 328.7/329.8 |
| 3 | Breakout has volume | 60.96M vs ~51.1M normalized 18-session avg (~+19%) | Participation validates the move |
| 4 | Momentum re-accelerating | MACD 6.60 > signal 3.84; histogram 2.33→2.77 | No bearish divergence; continuation bias |
| 5 | RSI strong but not extreme | 68.77, up from 32.20 (06-25) | Strength with limited headroom; avoid chasing 328–330 |
| 6 | Pressing upper band | Close 327.50 vs UB 329.83 (−0.71%); width 18.5% | Riding an expanding envelope — trend regime, but extension risk |
| 7 | Extended above VWMA | Price +10.48% vs VWMA 296.42 | Mean-reversion magnet; scale in on pullbacks |
| 8 | Volatility elevated | ATR 8.33 = 2.54% of price (vs ~5.7 in late May) | Widen stops to ≥1.5× ATR; reduce position size |
| 9 | June was a correction, not a break | 06-25 close 275.15 (−6.12%), low 273.75; stayed above 200SMA; now +19.63% from low | Primary uptrend intact; 274–275 is the structural floor |
| 10 | Primary invalidation level | 50 SMA 300.53 / Bollinger mid 301.93 | Close below ~301 flips the intermediate bias |

**Bottom line:** AAPL is in a confirmed, volume-supported uptrend resuming off a sharp June shakeout, with all trend and momentum measures aligned higher. The tactical risk is short-term extension (RSI 68.8, price under the upper band, 10.5% above VWMA, ATR at 8.33) — which argues for buying pullbacks toward the 10 EMA (≈313) or breakout retests of the 315–317 shelf rather than chasing 328–330, with risk anchored below 311.9 (near-term) and ~301 (structural).