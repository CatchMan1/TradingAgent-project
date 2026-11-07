# AMZN — Multi-Timeframe Technical Report (as of 2026-07-21)

**Data basis:** All price levels and indicator values below come from the verified snapshot for 2026-07-21 (latest row: O 249.11 / H 249.34 / L 246.42 / **C 247.55** / V 27.73M) and the indicator series pulled from the same frozen dataset. No external or unverified figures are used.

---

## 1. Market context — what regime is AMZN in?

AMZN is in a **long-term uptrend that is being digested by a medium-term corrective range**. Three distinct phases are visible in the 2026 data:

| Phase | Window | Evidence |
|---|---|---|
| Uptrend | Jan 2 (226.50) → May 6 close 274.99 (intraday high 278.56 on May 5) | Consistent higher highs; Apr 8 gap up (221.25 close → 221.25→233.65 on Apr 9) |
| Correction | May 6 close 274.99 → Jun 25 close 227.01 (low 225.55) | −17.4% on closing basis; MACD rolled from +5.72 (May 22) to −6.87 (Jun 25/26) |
| Base / recovery | Jun 25 low 225.55 → Jul 21 close 247.55 | +9.0% off the close low; sequence of **rising lows** |

**Rising-low sequence (tool-verified lows):** 225.55 (Jun 25) → 226.13 (Jun 26) → 233.80 (Jun 29) → 234.90 (Jul 1) → 238.25 (Jul 9) → 243.59 (Jul 17) → 246.42 (Jul 21). That is a constructive, tightening structure — but note the *highs* are not yet confirming: 256.48 (Jul 15) → 258.08 (Jul 16) → 252.89 (Jul 20) → 249.34 (Jul 21). Price is compressing into a **coiling wedge directly beneath the declining 50-day SMA**.

**The single most important structural fact:** close 247.55 sits **below** the 50-SMA (251.16) but **above** a **rising** 200-SMA (234.35). That is the classic "uptrend + pullback/consolidation" signature, not a trend break — but it also means overhead supply is actively being defended.

---

## 2. Why these eight indicators were selected

In a post-correction base inside a long-term uptrend, the decision-relevant questions are: (a) is the primary trend intact, (b) is the correction over, (c) is momentum genuinely rebuilding or just bouncing, (d) where is the volume confirming, and (e) how wide do stops need to be. The chosen set answers each without redundancy:

1. **close_200_sma** — primary trend anchor / invalidation benchmark.
2. **close_50_sma** — the actual overhead obstacle and medium-term trend direction.
3. **macd** — crossover + zero-line regime change (the recovery's core evidence).
4. **macdh** — momentum *thrust* and rate of change (critical: it is already decelerating).
5. **rsi** — two-sided exhaustion gauge; confirms there is no overbought ceiling near resistance.
6. **boll_ub** — objective breakout/overbought test that coincides with the July rejection high.
7. **atr** — volatility regime + stop/position-sizing arithmetic (currently contracting).
8. **vwma** — the volume-weighted "true" cost basis, to distinguish accumulation from a drifting bounce.

(Deliberately excluded: `close_10_ema` — at 247.59 it is virtually identical to the 247.55 close, so it adds no independent information; `macds` is implied by `macd` + `macdh`; `boll` middle and `boll_lb` are quoted in the text but not counted as separate selections.)

---

## 3. Trend analysis (moving averages)

- **200-SMA = 234.35, rising steadily** (230.55 on May 22 → 234.35 on Jul 21, ~+0.13/day). The primary trend is up. Price is **+5.6% above** it. Even the June capitulation (low 225.55) held above the 200-SMA.
- **50-SMA = 251.16, still falling** (peak 257.10 on Jun 18 → 251.16 on Jul 21, ~−0.45/day). Price is **−1.44% below** it. This is the crux: the 50-SMA is a *descending* line, so "breaking out" requires price to do more than hold still.
- **50/200 spread = +16.8 points** (was ~+20 in mid-June). The golden-cross configuration remains firmly intact — no death-cross risk in any actionable timeframe — but the spread is narrowing because the 50-SMA keeps declining.
- **Short-term:** the 10-EMA (247.59) has flattened and is now *exactly* at price. That is textbook equilibrium — neither bulls nor bears control the last two weeks.

**Read:** trend scoreboard is 2-to-1 bullish (200-SMA up, price above it) versus 1 bearish (50-SMA down, price below it). This is a **neutral-to-constructive** posture, and it demands a level-triggered plan rather than a direction bet.

---

## 4. Momentum analysis (MACD family + RSI)

**MACD is the strongest bullish evidence on the chart, with one important caveat:**
- MACD line crossed **above zero on 2026-07-15** (0.260), the first positive reading since the June decline. It now sits at **0.801** vs signal **−0.337**.
- The MACD/signal **bullish crossover occurred 2026-07-01** (histogram flipped positive: +0.470) — the recovery has been "in play" for ~14 sessions.
- **Caveat:** the histogram has contracted for **four consecutive sessions**: 2.124 (Jul 15) → 1.946 → 1.576 → 1.446 → **1.139 (Jul 21)**. Thrust is fading while price stalls under 250. This is the classic "momentum made the turn but the impulse is losing fuel" configuration — it argues for *buying strength above resistance*, not buying blindly into the middle of the range.

**RSI = 51.31 — neutral, and that is bullish-leaning in context:**
- RSI bottomed at **32.46 (Jun 10)** and **33.63 (Jun 25)** — never reached 30, i.e., the correction never produced a true oversold washout. It then recovered to **60.14 on Jul 15** and has eased to 51.31.
- At 51 with price pressing resistance, there is **~19 points of headroom** before overbought. RSI is not capping upside. Conversely, RSI making a lower high (60.14 → 54.04 → 51.31) alongside price's lower high is a mild negative divergence to monitor — if price makes a new recovery high above 258 while RSI stalls under 60, treat the breakout with suspicion.

---

## 5. Volatility & bands

- **Bollinger upper = 256.82; middle = 243.07; lower = 229.33.** The close of 247.55 sits at **~66% of band width** — upper half, but not extended.
- The **middle band has turned up** (bottomed at 239.68 on Jul 8 → 243.07 on Jul 21). A rising 20-SMA is the earliest, quietest confirmation that the June downtrend has stopped.
- **Confluence of resistance is unusually clean:** upper band 256.82 + Jul 16 high 258.08 + Jul 15 high 256.48. Three independent measures cluster in **256.5–258.1**. That is *the* level.
- **ATR = 7.18 (~2.9% of price), down from 8.59 on Jun 29 (−16%).** Volatility is contracting — consistent with a coil, and a warning that a low-ATR consolidation usually resolves in a sharp directional move. Do not assume low vol persists.

---

## 6. Volume / participation

- **VWMA = 246.49, rising** (236.5 on Jun 30 → 246.49 on Jul 21) and price is **above** it. Volume-weighted buyers are in profit and the volume-weighted cost basis is climbing — a genuine accumulation signal, not just price drift.
- **The Jun 26 session is the footprint that matters:** 232.69 close on **248.37M shares** — roughly **5.3×** the ~47M typical 20-day pace (excluding that outlier, the 20-session average is ~47.0M). A volume spike of that magnitude at a swing low is capitulation/exhaustion, strengthening the case that **225.55–232.69** is a defended floor.
- **The one clear warning:** July volume is decaying. Jul 21's **27.73M** is the lowest in the visible July record and only ~59% of the ~47M typical pace, while price pushes into resistance. Breakouts on shrinking volume fail more often than they succeed. **A close above 258 on <40M shares should be discounted; the same close on >55M is a real signal.**

---

## 7. Actionable plan

**Bias: neutral-to-constructive. Trade the levels, not the middle of the range.**

**Bullish trigger (primary):**
- **Daily close above 251.16 (50-SMA)** = first confirmation of medium-term repair.
- **Daily close above 258.1 (Jul 16 high / upper band zone) on above-average volume** = the actionable long trigger.
- Staged upside references: **256.5–258.1** → **265.06** (Apr 30 close) → **271.17–274.99** (May consolidation / high-close zone).
- Stop for a breakout long: **1.5 × ATR ≈ 10.8 points** below entry, or a close back under 250.0 (whichever is tighter).

**Bearish / failure triggers:**
- **Close below 246.4–246.5** (VWMA 246.49 + Jul 21 low 246.42) = the coil starts leaking.
- **Close below 243.07** (Bollinger middle / 20-SMA) = the base is broken; the "rising middle band" thesis dies.
- Next supports: **238.25 (Jul 9 low)** → **229.33 (lower band)** → **225.55 (Jun 25 low)**. A close under 225.55 invalidates the entire recovery and puts the rising 200-SMA (234.35) on the table as the last major support.
- Short-side stop: above **251.2–253.0**.

**Risk management arithmetic (from ATR 7.18):**
- 1×ATR = ~240.4; 1.5×ATR = ~236.8; 2×ATR = ~233.2 (which lands almost exactly on the 200-SMA — a natural "catastrophe stop" confluence).
- Because ATR is compressing, size positions *up* modestly only after a confirmed breakout expands volatility — do not size up into a coil.

**What would change the read:**
- *More bullish:* MACD histogram re-expands above 2.12 while price clears 258; volume expands; RSI > 60.
- *More bearish:* histogram rolls negative before price clears 251; lower-high sequence extends (failure at 250/252); VWMA flattens/turns down.

---

## 8. Data notes & caveats

- **No discrepancy** was found between the price series and the verified snapshot; the 2026-07-21 row matches in both (C 247.55, V 27.73M), and all snapshot indicator values (50-SMA 251.16, 200-SMA 234.35, RSI 51.31, MACD 0.801 / signal −0.337 / hist 1.139, Boll 243.07/256.82/229.33, ATR 7.18, VWMA 246.49) match the indicator tool output exactly.
- The snapshot includes **mfi = 0.672** on a non-standard (0–1) scale. I have **excluded it** from the analysis rather than re-scale it, because its normalization is unverified; directionally it implies positive money flow but I make no claim on it.
- All levels described as "support/resistance" are **observed high/low/close references from tool output**, not statistically validated bounce zones. The February event (Feb 5 close 222.69 → Feb 6 open 202.70, close 210.32 on 179.2M shares) is cited only as a historical gap reference, not as a predictive pattern.

---

## Key Points Summary

| Factor | Reading (2026-07-21) | Signal | Level / Note |
|---|---|---|---|
| Close | 247.55 | Neutral | Between 50-SMA and 200-SMA |
| 200-SMA | 234.35, **rising** (+0.13/day) | **Bullish** | Price +5.6% above; primary uptrend intact |
| 50-SMA | 251.16, **falling** (−0.45/day) | **Bearish** | Price −1.44% below; overhead wall |
| 50/200 spread | +16.8 pts | Bullish (intact) | Golden-cross config holds; narrowing |
| 10-EMA | 247.59 ≈ price | Neutral | Dead equilibrium — coiling |
| MACD | +0.801 (above 0 since Jul 15) | **Bullish** | First positive regime since June |
| MACD histogram | 1.139, **4 straight declines** from 2.124 (Jul 15) | **Caution** | Thrust fading into resistance |
| RSI | 51.31 | Neutral / bullish-leaning | Headroom to 70; lower highs 60.1→54.0→51.3 |
| Bollinger upper | 256.82 (mid 243.07, lower 229.33) | Resistance zone | Confluent with Jul 16 high 258.08 |
| Bollinger middle | 243.07, **turned up** from 239.68 (Jul 8) | Mild bullish | Earliest turn confirmation; key support |
| ATR | 7.18 (−16% since Jun 29) | Coil / compressing | Stops: 240.4 (1×), 236.8 (1.5×), 233.2 (2×) |
| VWMA | 246.49, **rising**; price above | **Bullish** | Accumulation confirmation |
| Volume | 27.73M on Jul 21 (~59% of ~47M pace) | **Caution** | Jun 26: 248.4M spike = capitulation floor |
| Primary trigger | Daily close > 258.1 on >55M volume | Long | Targets 265.06 → 271–275 |
| Primary invalidation | Close < 243.07; hard stop < 225.55 | Reduce / exit | 200-SMA 234.35 is last major support |

**Bottom line:** AMZN is a **long-term uptrend digesting a medium-term correction**. Momentum has genuinely turned up (MACD above zero, VWMA rising, higher lows, rising 20-SMA), but the rally is arriving at a dense resistance cluster (251–258) on shrinking volume and decelerating MACD thrust. The highest-probability play is **wait for a volume-confirmed close above 258.1 to add longs, keep stops at ~1.5×ATR, and treat a close below 243.07 as the signal that the base has failed.**