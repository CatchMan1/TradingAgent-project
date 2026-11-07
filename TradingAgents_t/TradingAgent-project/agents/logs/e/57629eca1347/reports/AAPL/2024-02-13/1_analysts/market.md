# AAPL — Multi-Timeframe Technical Report (as of 2024-02-13 close)

## 1. Verified source-of-truth snapshot

The verification snapshot and the raw price history agree exactly (no discrepancy to flag on OHLCV or indicator values). I also independently rebuilt the 20‑day SMA from the raw closes and got **189.283**, matching the snapshot's `boll` — so the indicator layer is internally consistent.

| Field | Value (2024-02-13) |
|---|---|
| Open / High / Low / Close | 185.77 / 186.21 / 183.51 / **185.04** |
| Day change | −2.11 (−1.13%) vs 187.15 (2024-02-12) |
| Volume | 56,529,500 |
| 10 EMA | 187.785 |
| 50 SMA | 190.337 |
| 200 SMA | 183.268 |
| VWMA | 188.073 |
| MACD / Signal / Hist | −0.6069 / −0.2984 / **−0.3084** |
| RSI(14) | 41.72 |
| Bollinger (mid / upper / lower) | 189.283 / 196.412 / 182.154 |
| ATR(14) | 3.190 (1.72% of price) |

⚠️ Data note: the snapshot's auxiliary `mfi` field prints **0.356**, which is not a valid 0–100 MFI reading (it looks like a 0–1 scaled or malformed value). I have **excluded it** from the analysis rather than interpreting it.

---

## 2. Trend structure: intact medium-term uptrend, deteriorating short-term trend, price trapped in the middle

**Long-term (200 SMA): still constructive.** The 200 SMA is *rising* — 182.395 (2024-02-01) → 182.592 (02-05) → 183.068 (02-09) → **183.268 (02-13)**, roughly +0.87 points in nine sessions. Price at 185.04 sits **+0.97% above** it. The long-term trend has not broken.

**Medium-term (50 SMA): rolling over.** The 50 SMA *peaked* at **190.925 on 2024-01-30** and has declined every session since: 190.819 (01-31) → 190.650 (02-02) → 190.480 (02-09) → **190.337**. That is a slope change from rising to falling, which is the single most important structural shift in this dataset. Price is **−2.78% below** the 50 SMA.

**The 50/200 configuration remains bullish (50 > 200), but the spread is compressing:** 190.925 − 182.191 = **8.73 points on 01-30**, versus 190.337 − 183.268 = **7.07 points on 02-13**. A narrowing bull spread with a falling 50 SMA is the classic early signature of a trend transitioning from trending-up to range/consolidation.

**Short-term (10 EMA): bearish.** The 10 EMA rolled over from 191.406 (01-29) to **187.785**, and price is **−1.46% below** it — the fastest average is now acting as overhead resistance rather than support.

**Price location:** 200 SMA (183.27) < **price (185.04)** < 10 EMA (187.79) < VWMA (188.07) < Bollinger mid (189.28) < 50 SMA (190.34). Price is in the **lower third of a compression channel**, beneath every short- and medium-term average while still above the long-term average. This is a *corrective pullback inside an uptrend*, not yet a trend reversal — but the burden of proof has shifted to the bulls.

**Short-term market structure is making lower highs and lower lows:**
- Swing high 196.38 intraday (2024-01-24) → lower high 191.05 (2024-02-07) → lower high 186.21 (2024-02-13)
- Swing low 184.35 (2024-01-31) → **lower low 183.51 (2024-02-13)**

---

## 3. Momentum: bearish and *re-accelerating* — the key nuance

**MACD:** The MACD line crossed below its signal on **2024-01-31** (MACD 0.091 vs signal 0.235) and crossed below zero on **2024-02-01** (−0.138). It peaked at 0.951 on 01-26.

The histogram path is the important detail:
| Date | Histogram |
|---|---|
| 2024-02-01 | −0.296 |
| 2024-02-02 | **−0.445** (widest) |
| 2024-02-06 | −0.243 |
| 2024-02-07 | −0.125 |
| 2024-02-09 | **−0.065** (narrowest) |
| 2024-02-12 | −0.137 |
| 2024-02-13 | **−0.308** |

From 02-02 to 02-09 the histogram contracted by ~85%, which is the textbook setup for a bullish MACD crossover. **That recovery failed.** On 02-12 and 02-13 the histogram re-widened sharply negative (−0.065 → −0.308) and the MACD line itself turned down again (−0.252 → −0.607). This "failed re-tightening" is a materially more bearish signal than a simple negative MACD: downside momentum has *resumed* rather than decayed. A fresh bullish crossover is not imminent at this trajectory.

**RSI: 41.72, downside room, no divergence.** RSI rolled from 50.81 (02-07) → 45.93 (02-12) → **41.72**. It is below the 50 midline but well above oversold 30. Critically, **there is no bullish divergence**: price's lower high at 191.05 (02-07) versus 195.75 (01-23) was matched by a lower RSI high (50.8 vs 62.6) — momentum is simply tracking price lower, confirming rather than contradicting the downtrend. With 41.7, price could fall another ~4–5% before momentum gets stretched. For reference, the 2024-01-05 low (close 181.18) coincided with RSI 28.79.

---

## 4. Volatility and Bollinger: a well-defined confluence shelf below

- **ATR = 3.190**, or **1.72% of price**. ATR expanded from ~2.57 in late December to a local peak of **3.586 on 2024-02-02** and has since eased to 3.19 — volatility is elevated but cooling.
- **Bollinger:** mid 189.283, upper 196.412, lower **182.154**. Bandwidth is only **7.53%** of the mid (14.26 points full width), i.e. bands are relatively compressed — consistent with the consolidation read.
- **%B = 0.20** — price is in the bottom fifth of the band but **not tagging the lower band**. There is no band-touch/pierce yet, meaning no capitulation signal.
- **Confluence shelf:** Bollinger lower **182.154** + 200 SMA **183.268** + 02-13 intraday low **183.51** cluster into a **182.15–183.51** support zone roughly 1.5 points thick. That the 2024-02-13 low (183.51) held **0.24 points above the 200 SMA (183.27)** is a concrete, date-stamped confluence test — and it held. This zone is the pivot for the entire setup.

---

## 5. Volume: sellers own the volume-weighted average, but there is no distribution climax

- **VWMA = 188.073**, in a clear downtrend from 189.720 (02-07). Price is **−1.61% below** VWMA, meaning the average dollar transacted over the recent window is above the current price: recent buyers are, on balance, underwater. This is a genuine bearish confirmation that pure price-MA analysis can miss.
- **02-13 volume 56.53M** versus a ~57.6M average of the prior nine sessions and versus **102.55M on 2024-02-02** (the wide-range reversal day, low 179.25 → close 185.85). So the current pullback is happening on **unremarkable volume**.
- Interpretation: this is an *orderly* decline, not panic selling. The positive read is no distribution climax; the negative read is **no washout/capitulation** either — nothing yet forcing a bottom. The 102.55M session on 02-02 marks the real volume node of interest.

---

## 6. Key levels (all from tool output)

| Level | Price | Source / date |
|---|---|---|
| Major resistance 2 | 195.75–196.38 | Intraday highs 2024-01-23 / 01-24; near Boll upper 196.41 |
| Resistance 3 | 191.05 | 2024-02-07 high |
| **Resistance 1 (trend pivot)** | **190.34** | 50 SMA (falling) |
| Resistance 1b | 189.28 | Bollinger mid |
| Resistance 1c | 187.79–188.07 | 10 EMA / VWMA cluster |
| **Spot** | **185.04** | 2024-02-13 close |
| Near support | 186.21 → 183.51 | 02-13 high → 02-13 low |
| **Support shelf** | **182.15–183.51** | Boll lower 182.15, 200 SMA 183.27, 02-13 low 183.51 |
| Breakdown trigger | 181.18 | 2024-01-05 close (RSI 28.8 low) |
| Deeper support | 179.25–180.17 | 2024-02-02 low / 2024-01-05 low |

**Context for the downside:** the 2024-02-13 close of 185.04 is **−6.60%** from the 2023-12-14 close of 198.11 (total-return index 199.212 → 186.306, **−6.48%**), and **−5.19%** from the 2024-01-23 close of 195.18. Month-to-date, however, AAPL is essentially flat: 184.40 (01-31 close) → 185.04 = **+0.35%**. So the last two weeks are a chop-and-fade range, not a crash.

---

## 7. Actionable interpretation and scenarios

**Bias: neutral-to-cautiously-bearish short term, structurally bullish long term. Do not initiate new long exposure at 185.04.**

The problem with buying here is location: price is *mid-range*. Support is 1.5–2.9 points (−0.8% to −1.6%) away, while the first meaningful resistance (VWMA/10 EMA cluster at 187.8–188.1) is only 2.8–3.0 points (+1.5%–1.6%) away — with ATR at 3.19, that is roughly **one average day's range**, making the reward-to-risk near 1:1 against a 183.3 stop. That is not a tradeable edge.

**Scenario A — Breakdown / continuation lower (bear case, favored by momentum):**
- Trigger: daily close **below 183.27** (200 SMA) with volume > ~57M, i.e. expanding versus the recent norm.
- Confirmation: MACD histogram stays below −0.30 or widens.
- Targets: 181.18 → 179.25/180.17.
- Invalidation: a close back above 185.0 within two sessions (failed breakdown).
- Note: A close below the rising 200 SMA would be the first real damage to the long-term trend and would flip the 50/200 spread into active compression rather than mere digestion.

**Scenario B — Support holds, range trade (base case):**
- The 182.15–183.51 shelf holding, with a reversal bar or a MACD-histogram contraction back toward −0.15, sets up a long back toward 187.8–189.3 (10 EMA/VWMA → Boll mid). That is roughly +1.5% to +2.3% of upside against ~1.5% risk — acceptable only with a tight stop.
- Stop: **181.90** (below Boll lower 182.15) or 1.5×ATR ≈ 4.8 points beneath entry, whichever is wider. Size so that a stop-out costs ≤1% of account equity.

**Scenario C — Bullish resolution (needs proof):**
- Requirement 1: reclaim 187.79 (10 EMA) *and* 188.07 (VWMA) on above-average volume, which would put price back above the volume-weighted average.
- Requirement 2: reclaim 189.28 (Boll mid) then **190.34 (50 SMA)** and *turn that 50 SMA back up*. Until the 50 SMA slope inflects upward, rallies are counter-trend bounces.
- A daily close above 190.34 would neutralize the bearish momentum call and re-open 191.05 → 195.75/196.38.

**What would change my mind fastest:** a bullish MACD histogram divergence (price lower low into 182–183 while the histogram prints a higher low) combined with an RSI divergence and a volume expansion day. None of those three is present as of 2024-02-13.

**Risk-management notes:** ATR 3.19 implies daily 1-ATR swings of ±1.7%; stops tighter than ~2 points will get noise-stopped. Typical swing stops should be 1.5–2.0×ATR ≈ 4.8–6.4 points. With Bollinger bandwidth at only 7.5%, a volatility expansion (breakout) is more likely than a continued slow drift — position for a range break rather than a grind.

---

## 8. Why these eight indicators

| Indicator | Why it earns a slot here |
|---|---|
| **close_200_sma** | The decisive line: the rising 200 SMA at 183.27 is the last remaining bullish structural anchor and coincides with the Bollinger lower band. Everything hinges on it holding. |
| **close_50_sma** | Just inflected from rising to falling (peaked 190.925 on 01-30) — the most informative *change* in the dataset; also the first real resistance a bounce must conquer. |
| **close_10_ema** | Fast confirmation of the short-term regime shift; at 187.79 it is now resistance and forms a cluster with VWMA. |
| **macd** | Captures the medium momentum regime: below zero since 02-01, and turned down again on 02-13. |
| **macds** | Necessary to date the 01-31 bearish crossover — without it the MACD line alone is ambiguous. |
| **rsi** | Distinguishes "corrective pullback" (41.7) from "capitulation" (28.8 at the 01-05 low); also the tool for detecting the divergence that would mark a bottom. |
| **atr** | Sets stops (1.5–2× = 4.8–6.4 pts) and position size; 1.72% of price defines the noise floor a stop must clear. |
| **vwma** | The only volume-integrated trend check: at 188.07 it confirms sellers control the tape and price is below the true volume-weighted cost basis — pure MAs would miss this. |

*Deliberately excluded:* `boll_ub`/`boll_lb` as separate calls (band values are supplied by the verified snapshot, and the 200 SMA already anchors the lower-band confluence); `macdh` (derivable as MACD − signal, and its divergence insight is covered narratively above); `mfi` (malformed value).

---

## 9. Summary table

| Dimension | Reading (2024-02-13) | Signal | Actionable takeaway |
|---|---|---|---|
| Close | 185.04 (−1.13% d/d) | — | Mid-range; below all short/medium averages |
| Long-term trend | 200 SMA 183.27, **rising** | Mildly bullish | +0.97% above it; long-term trend intact |
| Medium-term trend | 50 SMA 190.34, **falling** since 01-30 peak 190.925 | Bearish | −2.78% below; 50/200 spread compressed 8.73 → 7.07 |
| Short-term trend | 10 EMA 187.79, falling | Bearish | −1.46% below; resistance overhead |
| Market structure | Lower highs 196.38 → 191.05 → 186.21; lower low 184.35 → 183.51 | Bearish | Short-term downtrend within uptrend |
| MACD | −0.607 vs signal −0.298; hist re-widened −0.065 → −0.308 | Bearish (re-accelerating) | Failed bullish crossover; no bottom signal |
| RSI(14) | 41.72, below 50, no divergence | Bearish, not oversold | Room to fall ~4–5% before stretched |
| Bollinger | Mid 189.28 / Up 196.41 / Low 182.15; %B = 0.20; width 7.5% | Neutral, compressed | Breakout regime pending; price not at band |
| ATR(14) | 3.190 (1.72%) | Elevated, easing | Stops 1.5–2×ATR = 4.8–6.4 pts |
| VWMA | 188.07, falling; price 1.61% below | Bearish | Volume-weighted holder cost above spot |
| Volume | 56.5M vs ~57.6M 9-day avg; 102.6M on 02-02 | Neutral | Orderly drift, no capitulation |
| Key support | **182.15–183.51** (Boll lower + 200 SMA + 02-13 low) | Pivot | Held by 0.24 pt on 02-13 |
| Key resistance | **187.79–188.07** → 189.28 → **190.34** | Pivot | Reclaim of 190.34 required to neutralize bearish call |
| **Overall bias** | Long-term bull / short-term bear correction | **Neutral-to-bearish** | Stand aside at spot; buy the 183.3 shelf with 181.90 stop, or buy strength only on a close > 190.34 |