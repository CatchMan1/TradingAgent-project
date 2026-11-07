# AMZN — Multi-Timeframe Technical Report
**As of session close 2024‑02‑26** · Benchmark date treated as "now" · All exact levels below are anchored to the verified B‑project snapshot

---

## 1. Bottom line

AMZN is in a **confirmed, mature-stage uptrend** (price > 10 EMA > 50 SMA > 200 SMA, all rising) that has spent the last three weeks **digesting the 2024‑02‑02 earnings gap in a ~165.7–176.4 range**. The 2024‑02‑26 session printed the highest high of the retrieved 2023‑11‑01 → 2024‑02‑26 window (176.37) but gave much of it back to close at 174.73, and it did so on **below-average volume (44.37M vs a 49.22M 9‑session average)**.

Momentum is **re-accelerating but not yet confirmed**: the MACD histogram has recovered from −0.53 (2024‑02‑21) to −0.02 (2024‑02‑26) — roughly 96% of the way back to a bullish re‑cross — while RSI at 65.19 has room below 70. My bias is **constructive/continuation, traded as a buy-the-dip within the range with a breakout add-on trigger above 176.37 on expanding volume**, not as a chase at 174.73.

---

## 2. Source of truth (verified snapshot, 2024‑02‑26)

| Field | Value |
|---|---|
| Open | 175.70 |
| High | 176.37 |
| Low | 174.26 |
| **Close** | **174.73** |
| Volume | 44,368,600 |
| Split / Dividend | 1.0 / 0.0 |

Snapshot indicator values (used throughout): close_50_sma **158.9614**, close_200_sma **138.9034**, close_10_ema **171.4089**, macd **4.3764**, macds **4.3962**, macdh **−0.0198**, rsi **65.1905**, boll **168.6035**, boll_ub **179.8788**, boll_lb **157.3282**, atr **3.6768**, vwma **171.0417**.

The `get_indicators` series reconciles exactly with these snapshot values on 2024‑02‑26 — **no discrepancy to flag** between vendors.

---

## 3. The 8 indicators selected (and why this set is complementary, not redundant)

| # | Indicator | Role in this specific market context |
|---|---|---|
| 1 | **close_50_sma** (158.96) | Medium-term trend + the dynamic floor that defines the *investable* trend. Rising +0.55/session. |
| 2 | **close_200_sma** (138.90) | Long-term regime filter. Confirms the 50>200 bullish stack and quantifies how extended price is (+25.8%). |
| 3 | **close_10_ema** (171.41) | Short-term momentum/entry timing. Fastest arbiter of "dip vs. breakdown" in a range. |
| 4 | **macd** (4.38) | Absolute trend momentum (positive and rising = trend intact). |
| 5 | **macdh** (−0.02) | Precise cross state and *rate of change of momentum* — the single most actionable datapoint right now. |
| 6 | **rsi** (65.19) | Overbought/oversold and exhaustion gauge. Critical here because this name has repeatedly pinned >70. |
| 7 | **atr** (3.68) | Volatility-scaled stops/position sizing (2.10% of price). Replaces arbitrary stop distances. |
| 8 | **vwma** (171.04) | Participación-weighted validation. Directly tests whether the melt-up has real volume behind it. |

Deliberately excluded: `macds` (fully derivable as macd − macdh), `boll_lb`/`boll` as primary (bands are used below only as a supplementary cross-check), and any stochastics (redundant with RSI).

*Supplementary cross-check (retrieved, not part of the 8‑indicator set): Bollinger middle 168.60 / upper 179.88 / lower 157.33.*

---

## 4. Trend structure — textbook bullish stack, but stretched

- **Perfect alignment:** 10 EMA (171.41) > 50 SMA (158.96) > 200 SMA (138.90). All three are rising simultaneously. This is the highest-quality trend configuration available from these tools.
- **Golden-cross regime is widening, not decaying:** 50 SMA − 200 SMA spread = **20.06 pts** today vs **15.11 pts** on 2023‑12‑28 (142.57 vs 127.46). The medium-term trend is *accelerating relative to* the long-term trend.
- **Price extension:** close 174.73 is **+1.94% above the 10 EMA**, **+9.92% above the 50 SMA**, **+2.16% above VWMA**, and **+25.80% above the 200 SMA**. The +25.8% premium over the 200 SMA is normal for a powerful trend but raises the cost of a failed breakout — this is a "manage risk" number, not a "short" number.
- **Slope detail:** 50 SMA gained +0.545 in the last session (158.4164 → 158.9614); 200 SMA gained +0.340 (138.5629 → 138.9034); 10 EMA gained +0.738 (170.6708 → 171.4089). All positive, all consistent. No rolling-over anywhere.
- **Trend since the November base:** close 137.00 (2023‑11‑01) → 174.73 (2024‑02‑26) = **+27.5%**, with the 50 SMA up from 142.57 (2023‑12‑28) to 158.96 — i.e., the average itself has climbed to meet price repeatedly rather than price collapsing into it.

**Structural read:** this is a *trend in good health but mid-pause*, not a trend at a top from a moving-average standpoint. The 50 SMA is not scheduled to intersect the current price zone for weeks, so a "trend-break" reading requires price to lose 171.4 / 168.6 first.

---

## 5. Momentum — the crux of the current setup

**MACD:** line 4.3764 vs signal 4.3962 → histogram **−0.0198**. The bearish cross occurred on **2024‑02‑16** (first negative histogram, −0.0389). Sequence since:

| Date | macd | macdh |
|---|---|---|
| 2024‑02‑07 (hist peak) | 4.7993 | **+1.3107** |
| 2024‑02‑16 (cross under) | 4.6728 | −0.0389 |
| 2024‑02‑21 (hist trough) | 3.9531 | **−0.5296** |
| 2024‑02‑22 | 4.1699 | −0.2502 |
| 2024‑02‑23 | 4.3250 | −0.0762 |
| 2024‑02‑26 | **4.3764** | **−0.0198** |

Three consecutive sessions of shrinking negative histogram = **momentum is repairing at an accelerating rate**, and the MACD line has turned up from 3.9531 → 4.3764 in three sessions while the signal line flattened (4.4827 → 4.3962). A bullish re-cross is plausibly 1–3 sessions away *if price simply holds ~174*. Crucially, **MACD remains comfortably above zero (4.38)** — the correction was a momentum reset inside an uptrend, not an absolute momentum breakdown.

**RSI:** 65.19. Key observations, all directly from tool output:
- RSI has already proven it can run in overbought territory here: **73.78 (2024‑02‑02)** and **72.43 (2024‑02‑09)**. A 65 reading is *not* a ceiling — it is mid-range for this name's recent behavior.
- The correction's RSI low was **55.91 (2024‑02‑20)** — it never broke 50. Shallow, trend-consistent pullback.
- **One caution worth flagging honestly:** price made a marginally higher high (176.37 on 2024‑02‑26 vs 175.39 on 2024‑02‑12) while RSI made a lower high (65.19 vs 67.90). That is a *technically* negative divergence, but the new price high exceeds the prior by only 0.98 pts (~0.6%) — too small to be a high-conviction exhaustion signal. Treat it as a reason to demand volume confirmation on any breakout, not as a standalone sell signal.

**Verdict on momentum:** bullish repair in progress, with the 2024‑02‑26 close (174.73) sitting *below* the 2024‑02‑23 close (174.99) — i.e., the rally has not yet closed at a new window high. That last 0.26 pts is trivial in price but decisive in signal quality.

---

## 6. Volatility and band context

- **ATR = 3.6768** (2.10% of the 174.73 close). ATR peaked at **3.9412 on 2024‑02‑13** and has eased; volatility was *not* expanding into the 2024‑02‑26 high, which is consistent with a drift-up rather than a thrust.
- Practical stop math: 1×ATR ≈ 3.68; **2×ATR ≈ 7.35**, which from 174.73 lands at **167.38** — coincidentally right on top of the 167.08 (2024‑02‑20 close) / 165.74 structural zone. That confluence is the single most useful risk number in this report.
- **Bollinger (supplementary):** middle 168.60, upper **179.88**, lower **157.33**. Price at 174.73 sits at **%B ≈ 77%** of the band. The bands have been *expanding upward* — lower band 144.59 (2024‑01‑30) → 157.33 (2024‑02‑26), upper band 162.48 → 179.88 — a directional volatility expansion rather than a squeeze. The upper band at 179.88 is the natural first objective/target zone, **5.15 pts (+2.95%)** above the close.

---

## 7. Volume and participation — the weak link

- **2024‑02‑02 earnings-type gap:** close 159.28 (02‑01) → open 169.19 → close 171.81 on **117,218,300 shares**. That is +7.87% versus the prior close and roughly **2.2× the 53.6M 20‑session average** (which itself includes the event day). The gap floor remains unfilled.
- **Participation has since faded.** 20‑session average volume ≈ **53.63M**; last 9 sessions average ≈ **49.22M**; 2024‑02‑26 volume **44.37M** is ~**10% below** the 9‑session average and ~**17% below** the 20‑session average.
- The three sessions that produced the new high (02‑22: 55.39M, 02‑23: 59.72M, 02‑26: 44.37M) show **declining volume into the high** — 02‑26 was the *lowest* of the three.
- **VWMA = 171.04**, and it has risen every session in the retrieved window (165.73 on 02‑13 → 171.04 on 02‑26). Price at +2.16% over VWMA confirms that, on a volume-weighted basis, the marginal buyer is in profit — a bullish structural fact. But VWMA is *catching up to* price rather than price being *pulled up by* volume, which is precisely what a low-volume high looks like.

**Interpretation:** no distribution yet (no high-volume down days in the range; the largest down-volume day was 2024‑02‑13 at 56.35M on a −2.15% close), but **the breakout is unconfirmed**. A close above 176.37 on ≥ 55–60M shares is what would convert this from "range drift" to "breakout."

---

## 8. Key levels (all derived from snapshot/near-session tool output)

| Level | Price | Source / significance |
|---|---|---|
| **Resistance 2** | **179.88** | Bollinger upper band (2024‑02‑26) — statistical stretch/target |
| **Resistance 1** | **176.37** | 2024‑02‑26 high — highest high in the retrieved window |
| Intraday pivot | 175.75 | 2024‑02‑23 high |
| Close-level pivot | 174.99 | 2024‑02‑23 close (highest close in window) |
| **Spot** | **174.73** | 2024‑02‑26 close |
| **Support 1** | **171.41 / 171.04** | 10 EMA / VWMA (confluence) |
| **Support 2** | **168.60** | Bollinger middle (20 SMA) |
| **Support 3** | **167.08 – 165.74** | 2024‑02‑20 close and the 2024‑02‑13 / 2024‑02‑20 twin lows (165.75 / 165.74) |
| **Support 4 (major)** | **158.96 – 159.76** | Rising 50 SMA + the unfilled 2024‑02‑02 gap floor (02‑01 high 159.76); also ≈ the 2024‑02‑01 close 159.28 |

The 165.74–167.08 zone has now been tested twice (lows 165.75 on 2024‑02‑13 and 165.74 on 2024‑02‑20, both closing back above 167) and is the line that separates "digestion" from "failed gap."

---

## 9. Scenarios, triggers, and trade construction

**Base case — range digestion with an upward tilt (highest-probability).** Price chops 168.6–176.4 while the 10 EMA (rising +0.74/day) and VWMA (+0.4 to +1.6/day) converge underneath. MACD re-crosses bullish without a big price gain. *Action: hold core longs; do not add at 174–175.*

**Bullish continuation — breakout trigger.** Daily **close > 176.37 with volume > 55M**. Confirmation stack required: macdh flips positive, RSI holds > 65 without spiking > 78, and VWMA continues rising. *First objective 179.88 (Bollinger upper); measured-range extension from the 10.63-pt consolidation (165.74–176.37) projects to roughly 187 if the range breaks cleanly — treat that as a stretch target, not a forecast.* *Invalidation: close back under 171.41.*

**Pullback-buy — preferred risk/reward entry.** Retest of **171.0–171.4** (VWMA/10 EMA confluence) or **168.6** (Bollinger middle) *on lighter volume and with the 50 SMA still rising*. This is the highest-quality entry because it lets you place a stop under 167.08 (≈1.6 ATR from 171) while keeping the trend structure intact.

**Bearish failure — invalidation ladder.**
1. Close < 171.04 (VWMA) → short-term trend broken, momentum cross fails.
2. Close < 168.00 (below Bollinger middle 168.60) → distribution risk rises.
3. Close < **165.74** → twin-low support gone; gap-fill risk toward **159.76/158.96** (gap floor + 50 SMA confluence), which is roughly 9% below spot. Note that ATR of 3.68 means such a move is ~2.7 ATR — a multi-session event, not a one-day shock.

**Sizing note (ATR-based):** with ATR at 2.10% of price, a 2×ATR stop ≈ 4.2% of position value. Size so that a stop at 167.38 (2×ATR below spot) risks ≤1–2% of portfolio equity. Because price is 25.8% above the 200 SMA, keep total exposure below what you'd run in a freshly-based trend.

---

## 10. What would change this view

- **Bullish flip to "confirmed breakout":** close > 176.37 on volume > 55M **and** macdh > 0 **and** a fresh RSI high above 72.43 would simultaneously erase the mild negative divergence.
- **Bearish flip to "trend at risk":** a high-volume (≥ 56M) close below 168.60, or two consecutive closes below 171.04 — both would put the MACD cross back in play at a lower level and shift the tape from "digestion" to "distribution."
- **Data caveat:** the retrieved OHLCV window begins 2023‑11‑01, so 176.37 is the highest high **of that window only** — I am deliberately not claiming an all-time high, and no historical backtest of support/resistance holds was run. The 2024‑02‑02 gap's association with a scheduled catalyst is inferred from its +7.87% size and 2.2× volume, not confirmed by a news feed.

---

## 11. Summary table

| Dimension | Reading (2024‑02‑26) | Signal | Actionable implication |
|---|---|---|---|
| **Trend (long)** | Close 174.73 vs 200 SMA 138.9034 (+25.8%), 200 SMA rising +0.34/day | **Bullish, extended** | Trend-following longs valid; avoid fresh full-size adds at extension |
| **Trend (medium)** | 50 SMA 158.9614, rising +0.545/day; 50−200 spread 20.06 (was 15.11 on 12/28) | **Bullish, widening** | Dynamic floor ~9.9% below spot; not a near-term concern |
| **Trend (short)** | 10 EMA 171.4089, price +1.94% above | **Bullish** | First line of defense; close < 171.41 = short-term trend break |
| **MACD** | 4.3764 vs signal 4.3962 | **Neutral, repairing** | Bullish re-cross likely in 1–3 sessions if price holds ≥174 |
| **MACD hist** | −0.0198 (from −0.5296 on 02/21) | **Improving sharply** | Confirms momentum reset, not breakdown |
| **RSI** | 65.19 (low of pullback 55.91 on 02/20) | **Bullish, not overbought** | Room to 70+; watch mild negative divergence vs 176.37 |
| **Volume** | 44.37M vs 49.22M 9-day avg; 02‑02 gap on 117.22M | **Neutral-negative** | Breakout needs >55M to be credible |
| **VWMA** | 171.0417, price +2.16% above | **Bullish** | Buyers in profit on volume-weighted basis |
| **ATR** | 3.6768 (2.10% of price) | **Moderate** | 2×ATR stop ≈ 167.38 — aligns with structure |
| **Bollinger (supp.)** | Mid 168.60 / UB 179.88 / LB 157.33; %B ≈ 77% | **Expanding upward** | 179.88 = first target; 168.60 = range floor |
| **Key resistance** | 176.37 → 179.88 | — | Buy stop above 176.37 w/ volume |
| **Key support** | 171.41/171.04 → 168.60 → 167.08/165.74 → 158.96–159.76 | — | Laddered invalidation plan |
| **Overall stance** | Constructive uptrend mid-consolidation | **Buy dips / add on confirmed breakout** | Preferred entry 168.6–171.4; avoid chasing 174–175 |