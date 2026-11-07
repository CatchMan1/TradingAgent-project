# AAPL — Multi-Timeframe Technical Report
**As of the close of 2026-10-02 | Last price: $333.69**

---

## 1. Verified Data & Integrity Check

All exact price, volume, and indicator claims below come from the `get_verified_market_snapshot` for **AAPL** dated **2026-10-02**, cross-checked against `get_stock_data` (both agree exactly on the final row).

**Latest verified session (2026-10-02):**

| Field | Value |
|---|---|
| Open | 333.26 |
| High | 334.54 |
| Low | 330.61 |
| **Close** | **333.69** |
| Volume | 33,278,600 |
| Prior close (10-01) | 330.32 |
| Session change | +3.37 (+1.02%) |
| Split / Dividend | 1.0 / 0.0 |

**Verified indicators on 2026-10-02:** 10-EMA 333.698 · 50-SMA 322.416 · 200-SMA 289.159 · MACD 3.807 · Signal 4.820 · Histogram −1.013 · RSI 54.72 · Bollinger mid 331.895 / upper 346.624 / lower 317.166 · ATR 7.035 · VWMA 335.300.

⚠️ **Data note:** the snapshot reports `mfi = 0.702609`, which reads as a 0–1 normalized scale rather than the usual 0–100. MFI is not part of my selected set, so this does not affect the conclusions, but it is flagged for anyone using the raw field.

---

## 2. Price Action & Market Structure

**The 2026 tape has been strongly bullish, with two violent event-driven interruptions.**

- YTD: close went from **271.01 (2026-01-02)** to **333.69 (2026-10-02)** = **+23.13%**. Total-return index over the same span: 275.07 → 339.62 = **+23.47%** (three small dividends: 0.26 on 2026-02-09, 0.27 on 2026-05-11, 0.27 on 2026-08-10).
- YTD range from the data: low **243.42 (2026-01-20 intraday)**, high **345.34 (2026-09-22 intraday)**.
- Two high-volume shocks define the structure:
  1. **2026-06-25/26:** close 293.08 → 275.15 on 107.0M shares, then 283.78 on **261.8M shares**. That marked the June low (intraday 274.21) and the launch point of the summer advance.
  2. **2026-07-31:** prior close **333.43** → open **304.81** (a **−8.58% gap**), close 308.91 on **132.5M shares** (~3× the current 20-day pace). This is not explained by anything in the technical data — it is an event-style repricing. The July high was 344.57 (2026-07-29).
- **Measured recovery:** 2026-08-12 low 300.57 → 2026-09-22 high 345.34 = **+14.89%**, fully repairing the entire 7/31 gap. The 7/30 pre-gap close (333.43) and today's close (333.69) are within **$0.26** of each other — AAPL is sitting exactly at the "gap-fill" decision line.

**Near-term structure has turned into a range with a lower high sequence.** After the 345.34 high (9/22), highs stepped down: 341.67 (9/25), 342.99 (9/28), 339.50 (9/30), 332.48 (10/1), 334.54 (10/2). Lows: 328.70 (9/29) → **325.81 (10/1)** → 330.61 (10/2).

**The important nuance:** 2026-10-01 undercut the 9/29 low (325.81 vs 328.70) but reversed to close at 330.32, and 2026-10-02 gapped up and held (open 333.26, close 333.69, closing in the upper quarter of a 3.93-point range). That is a textbook **failed breakdown / bear-trap** pattern at the 326 area — bullish short-term information, though not yet confirmed by momentum indicators.

Week-to-date: 341.07 (9/25 close) → 333.69 = **−2.16%**, with a 325.81 intraweek low that was bought.

---

## 3. Trend Structure — Three Timeframes, Three Different Messages

| Timeframe | Indicator | Value | Price vs. indicator | Signal |
|---|---|---|---|---|
| Long-term | 200-SMA | 289.159 | **+15.40%** | Strong uptrend, rising every session |
| Medium-term | 50-SMA | 322.416 | **+3.50%** | Uptrend, rising every session |
| Short-term | 10-EMA | 333.698 | **−0.002%** | Flat/rolled over, price pinned to it |

**Long-term (bullish, unambiguous).** The 200-SMA has risen every single session in the pull: 264.81 (2026-06-04) → 289.16 (2026-10-02). Price is 15.4% above it. The 50-SMA sits **$33.26 (+11.50%) above** the 200-SMA, and that spread is still widening — a persistent bullish MA stack (10-EMA > 50-SMA > 200-SMA). Strategic trend risk is low.

**Medium-term (bullish, but support is far away).** The 50-SMA at 322.42 has been rising ~$0.10–0.25/session and has not been closed below since 2026-09-09 (close 315.34 vs SMA 316.47); the last durable break was 2026-08-25. However, it is **3.5% below spot** — a cushion, not a nearby trigger. The 9/29 low (328.70) sits *above* it, meaning the recent consolidation is holding above medium-term support.

**Short-term (neutral/soft).** The 10-EMA peaked at 335.962 on 2026-09-28 and has drifted to 333.698. Price closed below it on 9/29, 9/30 and 10/1, and on 10/2 closed essentially *at* it ($0.008 below). This is the immediate battle line: a decisive close above ~335.5–336 would flip short-term trend back up; repeated rejection keeps the 326–335 chop alive.

---

## 4. Momentum — Cooling, Not Broken

**MACD system (bearish crossover, in progress):**
- MACD line: peak **6.248 (2026-09-22)** → **3.807 (10/02)** — seven consecutive declines.
- Signal: **4.820**, still rising but flattening.
- Histogram: **−1.013**, negative for four straight sessions and expanding (−0.283 on 9/29 → −0.601 → −0.990 → −1.013).
- The bullish MACD regime ran from the 2026-08-26 crossover (histogram +0.152) through 2026-09-28; the bearish crossover on **2026-09-29** is fresh. MACD remains **above zero**, so this is a *momentum deceleration within an uptrend*, not a trend reversal signal. The key tell: the histogram's negative slope is *flattening* (−0.990 → −1.013 vs. the prior −0.389 step), consistent with downside momentum losing force.

**RSI(14): 54.72 — dead neutral.**
- Path: 66.88 (9/22) → 62.90 → 61.32 → 65.67 (9/25) → 61.79 → **50.88 (9/29)** → 54.37 → 51.43 → **54.72 (10/02)**.
- Over that same span price fell only 1.8% while RSI fell ~12 points — momentum cooled faster than price, the classic signature of *consolidation* rather than distribution.
- RSI is above 50 (mild bullish bias) and nowhere near 70 or 30. There is no oversold mean-reversion edge and no overbought exhaustion signal. There is **no valid RSI divergence** in the tool output — I am not claiming one.

**Interpretation:** momentum is neutral. The market has no momentum tailwind right now, but also no momentum breakdown. This favors *level-based* trading over trend-following at this exact price.

---

## 5. Volatility — A Coiling Spring

**ATR(14): 7.035**, equal to **2.11% of price**.
- Down from **9.872 (2026-07-31)** = **−28.7%**, and from 8.046 (2026-09-11) = −12.6%.
- Realized daily range is compressing. Practical stop distance: 1.5×ATR ≈ **$10.55**; 2×ATR ≈ **$14.07**.

**Bollinger (20,2):** mid **331.895**, upper **346.624**, lower **317.166**.
- Bandwidth = (346.624 − 317.166)/331.895 = **8.88%**, down from ~16.2% on 2026-08-12 — a halving of volatility.
- The **lower band is rising fast** (311.02 on 9/24 → 317.17 on 10/02) while the **upper band is flat** (346.15 → 346.62). That is a classic **squeeze/coil** formation, and it typically resolves directionally.
- **%B = 0.561** — price sits just above the middle band, in the upper half of the envelope but 3.7% below the upper band. No band-riding, no oversold tag.

**Actionable read:** the 331.90 middle band is the pivot of the entire setup. Above it, the coil resolves toward 346.6; below it, toward 317.2. The mid-band rose from 330.96 (9/29) to 331.90 (10/02) — a gently rising baseline, which is a mild bullish tilt.

---

## 6. Volume & Volume-Weighted Price

**VWMA: 335.300** — price is **0.48% below** it.
- VWMA rose relentlessly from 309.10 (2026-08-27) to 335.34 (9/30), then **flattened for three sessions** (335.338 → 335.300 → 335.300).
- A flat VWMA with price below it means the volume-weighted buyer's average cost (~335.30) is now overhead supply. **Reclaiming 335.30 is the single cleanest volume-confirmation signal available.**

**Volume analysis (last 20 sessions, 2026-09-04 → 2026-10-02):**
- Approximate average volume: **~42.2M shares**.
- 2026-10-02 volume: **33.28M = ~21% below** that average.
- 2026-10-01 (the reversal day): 36.31M — also below average.
- Compare to the genuine volume events: 132.5M (7/31), 261.8M (6/26), 86.6M (9/18).

**Critical nuance:** the 10/1–10/2 recovery is occurring on **light volume**. That makes it a *constructive* pattern but not yet a *confirmed* one. Light-volume rebounds in an uptrend are normal, but they are vulnerable to a retest. Confirmation requires either a volume expansion above 335.3 or a successful retest of 326–331 on shrinking volume.

---

## 7. Key Levels (all data-derived)

**Resistance**
| Level | Source |
|---|---|
| 334.54 | 2026-10-02 high |
| **335.30** | **VWMA** — volume-weighted cost basis |
| 336.13 | 2026-09-18 close |
| 337.00 | 2026-09-17 close |
| 339.50 | 2026-09-30 high |
| 341.07 / 341.67 | 2026-09-25 close / high |
| 342.99 | 2026-09-28 high |
| **345.34** | **2026-09-22 high — YTD high** |
| 346.62 | Bollinger upper band |

**Support**
| Level | Source |
|---|---|
| **331.90** | **Bollinger mid / 20-SMA — pivot** |
| 330.61 / 330.32 / 330.14 | 10/02 low / 10/01 close / 09/30 low |
| 328.70 | 2026-09-29 low |
| **325.81** | **2026-10-01 reversal low — key invalidation** |
| 322.42 | 50-SMA |
| 317.17 | Bollinger lower band |
| 309.90 / 300.57–302.25 | 09/09 low / August low zone |

---

## 8. Scenario Playbook

### Base case — constructive range, bias to buy support (highest-quality setup)
The primary trend (50/200) is up, the 10/1 undercut-and-reclaim is bullish, the mid-band is rising, and RSI is above 50. But MACD is negative and the rebound is on light volume, so **chasing strength at 334 is poor risk/reward**.

- **Preferred entry:** scale into **331.9–330.6** (Bollinger mid / 10/1–10/2 lows).
- **Stop:** daily close below **325.80** (under the 10/1 reversal low). Risk ≈ $5.5–6.0/share (<1 ATR — tight but structurally justified).
- **Targets:** 339.50, then 341.07/341.67, then 345.34.
- **R:R:** roughly **1.5:1 to 2.2:1**.
- **Confirmation to add:** a daily close above **335.30 (VWMA)** on volume > 42M.

### Momentum breakout — only on confirmation
- **Trigger:** daily close > **335.30**, ideally > 336.13 (9/18 close), with volume expansion.
- **Stop:** 328.70 (9/29 low) — risk ~$6.6–7.6.
- **Target:** 341.07, then 345.34.
- **R:R:** only ~**0.9:1 to 1.3:1** unless entered on a retest of 333–334. Take reduced size or wait for the retest. Do not chase a gap into 341; the reward to the YTD high is thin relative to the stop.

### Bear case — breakdown
- **Trigger:** daily close below **328.70**, confirmed by a close below **325.81**.
- **Stop:** above **335.30** (risk ~$6.6–9.5).
- **Targets:** **322.42 (50-SMA)**, then **317.17 (lower band)**.
- **R:R:** ~**1.0:1 to 1.7:1**.
- **Caveat:** this is a counter-trend tactical short against a rising 50/200-SMA stack with the 200-SMA advancing every session. Size small and treat 322.42 as a likely bounce zone, not a hold-to-target.

### Invalidation / "view changer"
- A close back above **341.07** (9/25 closing high) with positive MACD histogram re-engagement would re-open the 345.34 test and end the consolidation narrative.
- Two consecutive closes below **322.42 (50-SMA)** would break the medium-term uptrend and shift the strategic bias to neutral/defensive.

---

## 9. Risk Management & Sizing

Using ATR = **7.035**:
- **1.5×ATR = $10.55** (tactical swing stop)
- **2.0×ATR = $14.07** (wider structural stop)

Example on a **$100,000 account risking 1% ($1,000)**:
- Entry 331.90, stop 325.80 → risk $6.10 → **163 shares (~$54,100 notional)**. That is a large notional for a 1.8% stop; cap notional independently (e.g., ≤50–60% of account) rather than letting the tight stop drive size.
- Entry 335.50, stop 325.80 → risk $9.70 → **103 shares (~$34,600 notional)**.
- Volatility-adjusted alternative: stop at 2×ATR below entry (335.50 − 14.07 = 321.43) → risk $14.07 → **71 shares (~$23,800 notional)**.

**Event risk is the dominant unknown.** The 2026-07-31 session (−8.58% overnight gap on 132.5M shares) proves AAPL can reprice violently between closes, invalidating any stop placed inside a single day. Keep position sizes such that a gap of that magnitude (≈8–9%, ≈$30 at current price) is survivable, and avoid maximal exposure into unscheduled catalysts.

---

## 10. Bottom Line

**AAPL is in a confirmed long-term and medium-term uptrend that is currently consolidating, with short-term momentum cooled and volatility coiling.**

- **Bullish evidence:** price +15.4% above a rising 200-SMA, +3.5% above a rising 50-SMA, bullish MA stack intact, 50-SMA premium over 200-SMA widening to +11.5%, RSI above 50, Bollinger mid-band rising, a failed breakdown at 325.81 on 10/1, and a full repair of the −8.58% July gap.
- **Bearish/cautionary evidence:** MACD crossed below signal on 9/29 with an expanding negative histogram, price below the 10-EMA for four sessions, price below the VWMA (335.30), lower highs since 9/22, and a light-volume rebound (~21% below the 20-day average).
- **Net:** **Neutral-to-constructive (accumulate on weakness, don't chase).** The cleanest trade is buying the 331.9–330.6 zone with a hard stop under 325.80, targeting 341 then 345.3. A close above 335.30 on volume is the signal to add; a close below 325.81 flips the tactical bias bearish toward 322.4 and 317.2.

---

## 11. Summary Table — Selected Indicators & Key Points

| Indicator | Value (2026-10-02) | What It Says | Actionable Implication |
|---|---|---|---|
| **close_10_ema** | 333.698 | Price pinned to it; EMA rolled from 335.96 (9/28) | Short-term pivot. Close >335.5 = momentum turns up |
| **close_50_sma** | 322.416 | Rising daily; price +3.50% above; last break 9/9 | Medium-term uptrend intact; 322.4 is deeper support |
| **close_200_sma** | 289.159 | Rising every session; price +15.40% above | Strategic uptrend confirmed; low trend risk |
| **MA stack** | 10-EMA > 50-SMA > 200-SMA | 50-SMA premium over 200-SMA = +11.50% ($33.26) | Bullish alignment, still widening |
| **macd** | 3.807 | Above zero but 7 straight declines from 6.248 (9/22) | Momentum decelerating within uptrend |
| **macds** | 4.820 | MACD below signal since 9/29 | Fresh bearish crossover — caution on new longs |
| **macdh** | −1.013 | Negative 4 sessions; expansion flattening | Downside momentum weakening, not accelerating |
| **rsi** | 54.72 | Neutral, down from 66.88 (9/22); above 50 | No oversold bounce edge; no overbought risk |
| **boll / boll_ub / boll_lb** | 331.895 / 346.624 / 317.166 | Bandwidth 8.88% vs 16.2% on 8/12; lower band rising | Squeeze coiling; 331.90 pivot, 346.62/317.17 targets |
| **atr** | 7.035 (2.11% of price) | Down 28.7% from 7/31 peak | 1.5×ATR stop ≈ $10.55; 2×ATR ≈ $14.07 |
| **vwma** | 335.300 | Price 0.48% below; VWMA flat 3 sessions | 335.30 is overhead supply; reclaim = volume confirmation |
| **Volume** | 33.28M vs ~42.2M 20-day avg | Rebound on ~21% below-average volume | Recovery unconfirmed; watch for retest |
| **Structure** | 325.81 (10/1 low) → 333.69 | Failed breakdown + gap-fill at 333.43 | Bullish short-term, but lower highs persist |
| **Key resistance** | 334.54 / **335.30** / 341.07 / 345.34 | VWMA then prior highs then YTD high | Breakout needs volume; thin R:R above 341 |
| **Key support** | **331.90** / 328.70 / **325.81** / 322.42 | Boll mid, swing low, reversal low, 50-SMA | Buy zone 331.9–330.6; invalidation <325.81 |
| **Stance** | — | Primary trend up; short-term momentum neutral | **Accumulate on dips; don't chase. Stop <325.80. Targets 341 / 345.34** |