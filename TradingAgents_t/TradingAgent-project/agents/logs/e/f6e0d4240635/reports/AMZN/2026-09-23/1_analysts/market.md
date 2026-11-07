# AMZN — Multi-Timeframe Technical Assessment (as of close 2026-09-23)

## 1. Verified snapshot baseline

All exact figures below come from the `get_verified_market_snapshot` output for 2026-09-23 and reconcile exactly with the per-indicator tool outputs (no discrepancies found — the snapshot's `macdh` of −0.2884 is arithmetically equal to MACD −1.6707 minus signal −1.3823).

| Metric | Value (2026-09-23) |
|---|---|
| Open / High / Low / Close | 253.00 / 253.99 / 247.76 / **249.27** |
| Volume | 44.21M |
| Day change (vs 254.98) | **−5.71 (−2.24%)**; close in the bottom ~24% of the day's 6.23-point range |
| 10 EMA | 253.23 |
| 50 SMA | 256.29 |
| 200 SMA | 240.63 |
| VWMA | 253.54 |
| Bollinger mid / upper / lower | 255.18 / 264.60 / 245.76 |
| RSI(14) | 44.07 |
| MACD / Signal / Histogram | −1.671 / −1.382 / −0.288 |
| ATR(14) | 6.06 (2.43% of price) |

Contextual returns computed strictly from the frozen rows: **−12.23%** from the 2026-08-03 closing peak of 284.02; **−1.56%** vs the 10 EMA; **−2.74%** vs the 50 SMA; **−1.69%** vs VWMA; **+3.59%** vs the 200 SMA; **+9.81%** from the 2026-06-25 closing low of 227.01; **+18.64%** from the first row in the sample (2026-02-20 close 210.11).

---

## 2. The structural story: a post-gap distribution inside an intact primary uptrend

The dominant feature of this dataset is the **2026-07-30 → 2026-07-31 gap**: close 235.50 on 7/30 (high 239.82) to an open of 265.00 on 7/31, closing 271.58 on 129.05M shares — then a peak close of **284.02 on 8/03** (intraday high 287.20) on 90.83M shares. That is a +15.3% single-session repricing on roughly 3–4× normal volume, almost certainly an event-driven (earnings-type) gap. The unfilled gap band **239.82–265.00** remains the single largest structural void beneath price.

Since 8/03, AMZN has traced a textbook sequence of **lower highs**: 280.14 (8/10) → 266.40 (8/19) → 267.56 (8/28) → 261.12 (9/04) → 257.59 (9/11) → 255.43 (9/18), with the recent swing low at **244.30 (9/16)**. The bounce into 9/21–9/22 topped at 259.49 / 259.00 and failed. That 9/21 high sits almost precisely at the **38.2% retracement of the 287.20 → 244.30 decline (≈260.7)** and immediately below the declining 50 SMA — a classic "first retracement that fails" signature.

However — and this is the key nuance — **the primary trend is still up**. The 200 SMA at 240.63 is rising monotonically (239.12 on 9/04 → 240.63 on 9/23), the 50 SMA remains 15.66 points *above* it (a still-positive golden-cross configuration worth +6.5%), and price is 3.6% above the 200 SMA. What we have is a **damaged intermediate-term trend inside a healthy long-term trend** — the most treacherous combination for directional conviction, because both bulls and bears can build a valid case from the same chart.

---

## 3. Trend structure: three averages, three different messages

**200 SMA (240.63) — strategic bull, untouched.** Price has not closed below the 200 SMA anywhere in the visible window. It is rising ~0.09 points per session. It also sits *inside* the bottom edge of the 7/31 gap (top of the pre-gap bar at 239.82). That makes **239.8–240.6 a genuine confluence floor**, not just a line.

**50 SMA (256.29) — the battleground.** This is where the tape has become genuinely two-sided. Counting daily closes against the 50 SMA since 9/09: below (9/09), below (9/10), **above** (9/11 at 256.78 vs 255.25), below (9/14–9/18), **above** (9/21 at 258.45 vs 256.10), below (9/22 and 9/23). That is five separate crossings in ten sessions — a whipsaw regime, not a trend. The 9/23 close (249.27) is 7.02 points (2.74%) below it. Mechanically, the 50 SMA's slope is already decelerating (256.10 → 256.26 → 256.29 over the last three sessions), and with 7/15's 254.96 rolling out of the window and being replaced by closes near 249–250, **the 50 SMA will flatten and likely turn down in the coming sessions** if price stays here. That will mechanically narrow the 50/200 spread.

**10 EMA (253.23) — fresh bearish cross.** The 10 EMA flattened through 9/16–9/18 (253.07 → 252.91), ticked up to 254.11 on 9/22, then rolled to 253.23. Price closed *above* it on 9/21 and 9/22, and *below* it on 9/23. Short-term momentum has flipped back down within the last session.

**The actionable insight:** 10 EMA (253.23), VWMA (253.54), and Bollinger mid (255.18) form a tight **253.2–255.2 resistance cluster**, with the 50 SMA at 256.29 immediately above as the last layer. Price is below all four. Until that shelf is reclaimed on a closing basis, rallies are counter-trend.

---

## 4. Momentum: deterioration confirmed on two independent measures

**MACD is the cleanest bearish evidence.** The MACD line crossed *below* its signal between 8/14 (line 6.609 vs signal 6.217, above) and 8/17 (line 5.830 vs signal 6.140, below) — a bearish cross five weeks ago that has never been reversed. The MACD line then rolled from +8.43 (8/11) to negative territory on 9/09, and the signal line crossed below zero on 9/15 (0.0067 → −0.3188). Critically, the histogram's attempt to repair failed: **−0.245 (9/21) → −0.057 (9/22) → −0.288 (9/23)**. The MACD line made a lower low (−1.671 vs −1.367 on 9/22) while the signal line continued to slide, i.e. the two-day stabilization was a head-fake. Note the MACD line is still above its 9/17 trough (−2.286), so this is *resumption of a downtrend*, not a new momentum low — a subtle but important distinction for anyone sizing a chase.

**RSI(14) at 44.07 shows a persistent sequence of lower highs**: 72.23 (8/03, overbought) → 65.87 (8/10) → 55.64 (8/19) → 55.85 (8/28) → **52.69 (9/21)** → 49.22 → 44.07. The 9/16 low printed 39.45 — the only genuine oversold-ish reading in the decline — and the bounce off it only reached 52.69 before failing. RSI at 44 is **neutral-with-a-bearish slope**, and importantly *not* oversold: there is room to fall to 30–35 without any mean-reversion argument being triggered. Anyone buying "because RSI is low" is misreading a 44 print.

---

## 5. Volatility: coiling, and coiling in a downtrend

**ATR has compressed from 9.95 (8/03) to 6.06 (9/23), a −39% contraction.** Bollinger bandwidth is 7.38% (upper 264.60 − lower 245.76, divided by mid 255.18) with the lower band only 1.41% below the close. %B is approximately **0.19** — price is in the lower fifth of the bands but not hugging the lower band.

Two implications:
1. **This is a volatility contraction inside a falling structure.** Such coils resolve in the direction of the prevailing pressure more often than not, and the prevailing pressure (lower highs, MACD below zero, price under VWMA) is down.
2. **Levels are close together relative to daily range.** At 6.06 ATR, a single ordinary session can traverse from the close at 249.27 to the 50 SMA at 256.29 (+1.16 ATR) or to the 9/16 low at 244.30 (−0.82 ATR). That argues for **buffers of 0.5–1.0 ATR around every level** rather than resting orders exactly on them, and it explains the 50-SMA whipsawing.

---

## 6. Volume: distribution, not capitulation

VWMA at 253.54 is **above** price by 1.69%, and its trajectory is unambiguously down: 272.05 (8/20) → 267.41 (8/24) → 262.05 (8/31) → 258.16 (9/10) → 253.54 (9/23). Translation: **each successive volume-weighted cohort of buyers is underwater**, and the most recent 3–4 weeks of accumulated volume sits ~4 points above the last price. That is the definition of overhead supply — every bounce into 253–255 meets sellers who are close to break-even and eager to exit.

Recent volume detail: the 9/18 spike (52.27M) coincided with a +1.04% up day and the third Friday of September, and the four sessions 9/18–9/23 averaged roughly 45.4M versus roughly 34.9M for the trailing 20 sessions — **elevated turnover at the top of the bounce**. The 9/23 decline came on 44.21M, about 1.27× the 20-day average and higher than 9/22's 41.98M: modest but real selling confirmation. Notably, there is **no capitulation volume spike** anywhere in the August–September decline (the largest down-day volume was 46.09M on 8/31), which is consistent with an orderly distribution rather than a flushed bottom.

---

## 7. Synthesis: how the signals actually stack

- **Bullish weight:** price +3.6% above a rising 200 SMA; 50 SMA still above 200 SMA; higher low at 247.76 (9/23) vs 244.30 (9/16); price just 1.4% above the lower Bollinger band; no distribution climax.
- **Bearish weight:** price below 10 EMA, VWMA, Bollinger mid, and 50 SMA simultaneously; MACD below zero *and* below signal with a re-widening negative histogram; five-week sequence of lower price highs; RSI making lower highs at 44 with room to fall; VWMA declining and above price; close at the low end of the day's range.

Net: **the tactical path of least resistance is lower, but the strategic trend is higher — so this is a "sell strength, don't chase weakness" tape.** Mid-range entries (249–251) have the worst risk/reward in this configuration precisely because the 244–260 range has whipsawed the 50 SMA five times in ten sessions.

---

## 8. Actionable playbook (levels, triggers, invalidation, sizing)

**Scenario A — Base case (range-bound distribution, ~55% weight): fade the 253–256 shelf.**
- Entry zone: 253.2–256.3 (10 EMA → 50 SMA). Best risk/reward is in the **upper half (255.0–256.3)**, ideally on a rejection candle or an intraday reclaim that fails to close above 256.29.
- Invalidation: daily **close above 259.50** (9/21 high), which would also reclaim the 38.2% retracement zone.
- Targets: 245.76 (Bollinger lower) → 244.30 (9/16 low) → 240.63 (200 SMA).
- Math: short at 256.0 with a 260.0 stop = 4.0 risk; to 244.30 = 11.7 reward → **≈2.9:1**. The same trade entered at 249.27 with the same stop is only ≈1.3:1 — which is exactly why the entry level, not the thesis, matters here.

**Scenario B — Tactical bull reclaim (~25% weight).**
- Trigger: daily **close above 256.29 with volume > 40M** *and* MACD histogram turning positive. A close above 259.50 is confirmation.
- Targets: 264.60 (upper Bollinger), then the 267.5 area (8/28 high).
- Invalidation: back below 249.20 (9/23 close).
- Caution: this is a counter-trend trade against a five-week pattern of lower highs; treat it as a range trade, not a new leg.

**Scenario C — Breakdown continuation (~20% weight).**
- Trigger: daily **close below 244.30** on volume > 45M (i.e., a break that is not just an ATR wobble).
- Targets: 240.63 (200 SMA, confluence with the 239.82 gap edge) first; then a measured move of the 259.50–244.30 range (15.2 points) projected from 244.30 implies **≈229.1**, which lines up loosely with the 6/25 low at 227.01.
- Invalidation: reclaim of 249–250.

**Risk management / sizing.** With ATR at 6.06 (2.43%), a stop at the 50 SMA from the last close is 7.02 points (1.16 ATR) — a sane, not-too-tight distance. Size positions as **risk budget ÷ 7.02** (e.g., $100 of risk per trade → ~14 shares). Cut size by half if trading the mid-range, because 0.8–1.2 ATR of daily travel will stop out technically-correct positions on noise alone.

**What would flip the read to bullish:** (1) a daily close above 256.29 on above-average volume, (2) MACD histogram turning positive and the MACD line reclaiming zero, (3) a higher low above 249 followed by a reclaim of 253.2. **What would flip it decisively bearish:** a close below 244.30, which would break the higher-low structure *and* put the 200 SMA and the gap edge in play on the same day.

**Caveats.** The sample is limited to 2026-02-20 onward, so no 52-week or multi-year reference points are available. The July 31 gap is identified as event-driven solely by its shape (15% gap, ~3–4× volume); the tool set contains no verified earnings calendar, so upcoming catalysts are unknown. The snapshot's MFI field (0.4336) appears scale-normalized rather than 0–100 and was therefore excluded from the analysis rather than misinterpreted.

---

## 9. Key points summary

| Category | Indicator / Level | Reading (2026-09-23) | Signal | Actionable interpretation |
|---|---|---|---|---|
| Price | Close | 249.27 (−2.24% d/d) | Bearish | Closed in bottom 24% of 247.76–253.99 range |
| Trend (long) | 200 SMA | 240.63, rising | Bullish | Primary uptrend intact; price +3.59% above |
| Trend (mid) | 50 SMA | 256.29, slope decelerating | Neutral/bearish | 5 crosses in 10 sessions; likely to roll over; price −2.74% |
| Trend (short) | 10 EMA | 253.23 | Bearish | Fresh close below it on 9/23 after 2 days above |
| Momentum | MACD | −1.671 | Bearish | Below zero since 9/09; lower low vs 9/22 |
| Momentum | MACD signal | −1.382 | Bearish | Below zero since 9/15 |
| Momentum | MACD histogram | −0.288 (from −0.057) | Bearish | Failed repair — negative re-widening |
| Momentum | RSI(14) | 44.07 | Bearish-neutral | Lower highs 72.23 → 52.69 → 44.07; not oversold |
| Volatility | ATR(14) | 6.06 (2.43%) | Coiling | −39% from 8/03's 9.95; use 0.5–1 ATR buffers |
| Volatility | Bollinger (mid/UB/LB) | 255.18 / 264.60 / 245.76 | Bearish tilt | %B ≈ 0.19; price in lower fifth; LB only 1.41% below |
| Volume | VWMA | 253.54, declining | Bearish | Price below it; recent volume-weighted buyers underwater = supply |
| Volume | Recent turnover | 9/23 44.21M ≈ 1.27× 20-day avg (~34.9M) | Mildly bearish | Above-average volume on a down day; no capitulation print |
| Structure | Resistance cluster | 253.23–256.29 | Pivot | Primary tactical decision zone |
| Structure | Support ladder | 245.76 → 244.30 → 240.63 | Downside targets | 239.8–240.6 = gap edge + 200 SMA confluence |
| Structure | Failed retracement | 9/21 high 259.49 | Bearish | ≈38.2% retrace of 287.20→244.30; rejected |
| Trade plan | Fade 255.0–256.3, stop 260, target 244.30 | ≈2.9:1 R/R | Base case | Best entry is strength into the shelf, not mid-range |
| Invalidation | Daily close > 259.50 | Flips to neutral/bullish | Risk trigger | Also reclaims the 38.2% level |