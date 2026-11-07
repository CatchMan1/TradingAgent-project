# AAPL — Multi-Timeframe Technical Report
**Analysis date: 2026-07-29 · Latest verified session close: $338.19**

---

## 1. Verified Snapshot (source of truth)

All exact price/indicator values below come from the `get_verified_market_snapshot` call for 2026-07-29. The `get_stock_data` CSV and the indicator series agree with it line-for-line — no discrepancies were found between tools.

| Field | Value (2026-07-29) |
|---|---|
| Open | 339.73 |
| High | 344.57 |
| Low | 337.35 |
| **Close** | **338.19** |
| Volume | 56,090,800 |
| close_10_ema | 330.84 |
| close_50_sma | 308.59 |
| close_200_sma | 277.21 |
| macd / signal / hist | 9.609 / 8.437 / 1.172 |
| rsi | 66.78 |
| boll / ub / lb | 322.40 / 346.14 / 298.66 |
| atr | 8.018 |
| vwma | 328.51 |
| mfi (snapshot-scaled, 0–1) | 0.695 |

**Candle character worth flagging:** AAPL printed a **new intraday high of 344.57** but closed at 338.19 — only $0.84 above the session low. That is a close in the **bottom ~12% of the day's 7.22-point range**, and a small down-close (−1.54 vs open) after the 07-28 up-day. New-high days that close near the low are not automatically bearish, but on a tape this extended it is a legitimate short-term supply signal.

---

## 2. Indicator Selection and Why

The market condition is a **strong, mature intermediate-term uptrend with a recent sharp shakeout and V-shaped recovery, now testing all-time-high territory while short-term momentum decelerates.** That dictates a mix of trend confirmation, momentum-quality checks, volatility-based risk sizing, and volume validation:

| Indicator | Role in this specific context |
|---|---|
| `close_200_sma` | Confirms the strategic trend is intact and rising (not a dead-cat bounce) |
| `close_50_sma` | Defines the intermediate trend and the primary "trend-following" pullback zone |
| `close_10_ema` | Times entries; separates healthy consolidation from trend damage |
| `macd` | Confirms the July momentum re-acceleration is a real regime shift, not noise |
| `macdh` | Detects *momentum quality* — critical here, because price is at highs but histogram is making a lower peak |
| `rsi` | Overbought/extension gauge plus divergence detection at new highs |
| `atr` | Sizes stops/positions given a 2.4% average daily range; also tracks volatility contraction |
| `vwma` | Validates whether the rally is being paid for by real volume (institutional participation) |

I deliberately **excluded** `macds` (fully derivable from `macd` + `macdh`), `boll_ub`/`boll_lb` as standalone picks (band levels are already in the verified snapshot and are used below), and any oscillator that duplicates RSI's information.

---

## 3. Trend Structure — Cleanly Bullish, Textbook Stack

The moving-average stack is in a perfect bullish sequence on the verified session:

**Close 338.19 > 10 EMA 330.84 > VWMA 328.51 > 50 SMA 308.59 > 200 SMA 277.21**

- **Long-term (200 SMA):** 277.21 and rising monotonically — from 248.56 on 2026-03-31 to 277.21 on 2026-07-29 (+11.5% in ~4 months). The 50 SMA has sat above the 200 SMA for the entire observable window (at least since 2026-03-31), and the spread has **widened** from 11.46 points to 31.38 points. This is an expanding, not maturing, golden-cross configuration.
- **Intermediate (50 SMA):** 308.59, up from 260.02 on 2026-03-31 (+18.7%). It turned up decisively in May and has not flattened since — the June drawdown barely dented its slope (291.15 on 06-25 → 308.59 today).
- **Short-term (10 EMA):** 330.84, rising from a trough of 289.33 on 06-29. This is the key line to watch: the 10 EMA has not been decisively reclaimed-and-lost since the recovery began.

**Extension is the main structural concern.** Close is **+9.59% above the 50 SMA** and **+3.69 ATR above it**. Normalized, that is the stretched end of AAPL's typical range. Price is 2.2% above the 10 EMA and 2.9% above the VWMA. In other words: the trend is strong, but **new-money entry here is buying in the upper decile of the short-term distribution**, not at a good location.

---

## 4. The June Shock and the July Recovery — What Actually Happened

This is the most important context for reading today's tape:

1. **Peak-to-trough:** Close 315.20 (2026-06-02) → close 275.15 (2026-06-25), a **−12.71%** correction. The 06-25 session itself was −6.12% (293.08 → 275.15) on 107.0M shares.
2. **Capitulation volume:** 06-26 traded **261.8M shares** — roughly 5x the current 12-session average — while closing *up* at 283.78 after an intraday low of 274.21. That is a classic high-volume reversal/exhaustion bar.
3. **The breakout gap:** 2026-07-02 closed 308.63 from 294.38 (+4.84%) on 75.4M shares, reclaiming the entire 06-17–06-24 shelf in one session. This is the single most important bullish evidence in the dataset — a gap-up through resistance on above-average volume.
4. **Recovery magnitude:** 275.15 (06-25 close) → 338.19 (07-29) = **+22.91% in 23 sessions.** That is a V-shaped recovery, not a rounded base — which is powerful but also means the move is not "rested."

**Year-to-date context:** 271.86 (2025-12-31 close) → 338.19 = **+24.40% YTD**; from the 2025-11-03 start of the dataset (269.05) the gain is **+25.71%**.

---

## 5. Momentum — Positive, But Decelerating at the Margin

**RSI = 66.78.** Not overbought. The path is informative:
- Peaked at **71.65 on 2026-07-17** (briefly overbought, 71.43 on 07-16)
- Fell to **58.11 on 2026-07-23** during a healthy 3-day pause
- Recovered to 68.90 on 07-28, now 66.78

**Mild bearish divergence:** the 07-29 close (338.19) and 07-28 close (340.08) are both *higher* than the 07-17 close (333.74), yet RSI is *lower* (66.78 / 68.90 vs 71.65). This is a genuine, tool-verified lower-high in momentum against a higher-high in price. It is **not** a standalone sell signal — in strong trends RSI persistently lags price — but it downgrades the case for chasing.

**MACD is corroborating the same story:**
- MACD line flipped negative on 06-25 (−1.59) and stayed negative through 07-01
- **Bullish crossover on 2026-07-02** (histogram turned positive at +0.261) — the same session as the breakout gap, which is a strong dual confirmation
- MACD line has since climbed to **9.609** with signal at 8.437 — the widest positive spread since early June
- **But the histogram is making a lower high:** peak **+3.337 on 07-17** → +0.795 on 07-23 → rebound to +1.310 on 07-28 → **+1.172 on 07-29 (rolling over again)**

So: MACD is in a confirmed bullish regime (line > signal, both rising), while the *rate of change* of that bullishness has already peaked. This is the classic signature of a trend entering a **consolidation/pause phase rather than a reversal phase**.

---

## 6. Volatility and Risk Sizing

**ATR = 8.018**, or **2.37% of the close** — a genuinely elevated daily range for a mega-cap.

Volatility is **contracting during the advance**, which is constructive:
- 8.74 (07-02, gap day) → 8.09 (07-13) → **8.02 (07-29)**
- Compare to the June panic peak of 8.26 (06-30) and 7.88 (06-25)

Rising price + falling ATR = orderly trend, not a blow-off. It also means **stops can be set slightly tighter than June levels would suggest.**

**Bollinger context (verified snapshot):** middle 322.40, upper **346.14**, lower 298.66. Bandwidth is (346.14 − 298.66) / 322.40 = **14.7%** of the middle band — a wide, expanding band consistent with a trending market, not a squeeze. The close sits **0.99 ATR below the upper band (346.14)** — price is knocking on the door of the upper band without having escaped it, i.e. extended but not parabolic.

**Practical risk parameters:**
- 1 ATR ≈ $8.02; 2 ATR ≈ $16.04
- Structural swing low to defend: **319.35 (07-23 low)** — that is 18.84 points, or **2.35 ATR**, below the 338.19 close
- Using a 2-ATR stop from the current price implies a stop near **$322**, which conveniently coincides with the Bollinger middle (322.40) — a high-confluence risk level

---

## 7. Volume / Participation — Confirmed, With One Caveat

**VWMA = 328.51** and it is screaming higher: 296.42 (07-15) → 310.27 (07-17) → 328.51 (07-29). A VWMA rising this steeply means the **recent volume-weighted average transaction price is chasing price upward** — buyers are transacting at progressively higher prices. Price is 2.9% above VWMA, so the trend is volume-supported.

**The caveat:** the June decline carried *heavier* volume than the July advance. The 07-14 → 07-29 stretch averages roughly **50M shares/session** (sum of the 12 sessions ≈ 603M), versus 107M on 06-25 and 261.8M on 06-26. The rally is real but it is not a high-conviction volume expansion — it is *adequate*, not *overwhelming*. Recent up-days have clustered in the 47M–63M range (e.g., 62.97M on 07-16, 63.41M on 07-17, 47.49M on 07-24, 51.86M on 07-28, 56.09M on 07-29), which is healthy accumulation-grade volume.

**MFI from the snapshot reads 0.695** (on the vendor's 0–1 scale, ≈69.5 normalized) — money-flow is firmly positive and approaching, but not at, an extreme. This corroborates the VWMA read.

---

## 8. Key Levels (all tool-derived)

| Level | Price | Basis |
|---|---|---|
| Resistance 3 | ~350.00 | Psychological / round number (not tool-derived — flag as such) |
| Resistance 2 | **346.14** | Bollinger upper band |
| Resistance 1 | **344.57** | 2026-07-29 intraday high (all-time-high zone in the dataset) |
| Spot | **338.19** | 2026-07-29 close |
| Support 1 | **330.84** | 10 EMA |
| Support 2 | **328.51** | VWMA (volume-weighted demand) |
| Support 3 | **322.40** | Bollinger middle band |
| Support 4 | **319.35** | 07-23 swing low (structure) |
| Support 5 | **308.59** | 50 SMA — intermediate trend line in the sand |
| Support 6 | **298.66** | Bollinger lower band |
| Support 7 | **273.75** | 06-25 capitulation low (major; a break invalidates the whole structure) |

---

## 9. Actionable Scenarios

**A. Base case — bullish continuation after digestion (highest probability)**
The trend stack, rising 50/200 SMA, positive MACD, and volume-confirmed VWMA all point up. But with price 3.69 ATR above the 50 SMA, RSI printing a lower high, and today's weak close near the session low, **chasing at 338 is poor location.**
- **Preferred entry:** pullback into **328.50–331.00** (VWMA + 10 EMA confluence). This is the highest reward-to-risk zone in the current structure.
- **Stop:** below **319.35** (≈1.5 ATR below the pullback zone) or a tighter 2 ATR at ~$322 for aggressive accounts.
- **Targets:** 344.57 (prior high) → 346.14 (upper band) → 350 round number.
- Risk/reward on the pullback entry to the 346 band is roughly **15 up / 10 down ≈ 1.5:1**; to 350 it is ~2:1.

**B. Breakout continuation**
A **daily close above 344.57 on volume > 70M** would resolve the momentum divergence to the upside and validate the histogram's re-acceleration. Confirmation requires the MACD histogram to make a **new high above 3.337** — otherwise it's a fake-out. Target 350, then measured-move extension.

**C. Consolidation / range (also plausible near-term)**
Given today's rejection candle, expect a 7–15 session range between **322.40 (Boll mid)** and **346.14 (Boll upper)**. In this regime, buy the lower band, sell the upper, and stop trading breakouts until ATR expands again.

**D. Trend-damage triggers — what would change the thesis**
- **Close below 328.51 (VWMA)** → volume support failing; downgrade to neutral
- **Close below 322.40 (Boll mid)** → short-term trend broken; expect a test of the 50 SMA
- **Close below 308.59 (50 SMA)** → intermediate uptrend broken; the +22.9% recovery is invalidated
- **Close below 298.66 (Boll lower)** → reconsider long bias entirely

---

## 10. Explicit Caveats and Unverified Items

- The mild RSI/histogram divergence described above is **real and tool-verified**, but divergences in strong uptrends frequently resolve upward. Do not treat it as a reversal call.
- I make **no claim** of historical support/resistance "bounces" at these levels, because the tool output does not establish that prior tests occurred at these specific prices.
- The "50 SMA > 200 SMA" condition is verified as holding from 2026-03-31 onward; the dataset does not extend far enough to date the golden cross itself, so no cross date is asserted.
- **Dividend cadence observation (inference, not tool-verified):** the CSV records $0.26 on 2025-11-10, $0.26 on 2026-02-09, and $0.27 on 2026-05-11 — a roughly quarterly cadence that would put the next ex-dividend date in **early-to-mid August 2026**, i.e., immediately ahead. Treat this as an unconfirmed calendar risk and verify independently.
- The `mfi` value (0.695) is reported on the vendor's 0–1 scale; I have not normalized it against a historical distribution, so treat it as directional only.
- Data gaps on 2026-04-03 and 2026-06-19 correspond to US market holidays; they are not data errors.

---

## 11. Summary Table

| Dimension | Reading (2026-07-29) | Signal | Confidence |
|---|---|---|---|
| **Price** | 338.19 close; new high 344.57 but closed bottom 12% of range | Weak candle at highs | Medium |
| **Long-term trend** | 200 SMA 277.21, rising +11.5% since Mar-31 | Bullish | High |
| **Intermediate trend** | 50 SMA 308.59, above 200 SMA by 31.4 pts (widening) | Bullish | High |
| **Short-term trend** | 10 EMA 330.84, price +2.2% above it | Bullish but extended | Medium-High |
| **Extension risk** | +9.59% / 3.69 ATR above 50 SMA | Overstretched — poor entry | High |
| **MACD** | 9.609 > signal 8.437; hist +1.172 | Bullish regime confirmed | High |
| **MACD histogram quality** | Peak 3.337 (07-17) → 1.172 now (lower high) | Decelerating momentum | Medium |
| **RSI** | 66.78; lower high vs 71.65 on 07-17 | Not overbought; mild bearish divergence | Medium |
| **ATR / volatility** | 8.018 (2.37% of price), contracting from 8.74 | Orderly trend; use for stops | High |
| **Bollinger** | Mid 322.40 / Up 346.14 / Low 298.66; bandwidth 14.7% | Trending, close 0.99 ATR from upper band | High |
| **VWMA** | 328.51, rising steeply from 296.42 on 07-15 | Volume confirms the advance | High |
| **Volume quality** | ~50M avg over last 12 sessions vs 262M June panic; recent up-days 47–63M | Adequate, not overwhelming | Medium |
| **June shock** | −12.71% (06-02 → 06-25); +22.91% recovery to 07-29 | V-shaped, un-rested | High |
| **YTD performance** | +24.40% from 271.86 (2025-12-31) | Strong | High |
| **Key support** | 330.84 / 328.51 / 322.40 / 319.35 / 308.59 | Laddered demand below | High |
| **Key resistance** | 344.57 / 346.14 / ~350 | Immediate ceiling zone | High |
| **Recommended action** | **Buy pullbacks into 328.50–331.00, not the current extension; stop under 319.35; targets 344.57 → 346.14 → ~350** | Constructive, disciplined | Medium-High |
| **Thesis invalidation** | Daily close below 308.59 (50 SMA) | Trend broken | — |