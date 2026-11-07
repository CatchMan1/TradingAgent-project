# AAPL — Technical Analysis Report
**As of the close of 2026-09-03 (verified snapshot)** | Price basis: USD

---

## 1. Verified Market Snapshot (source of truth)

| Field | 2026-09-03 |
|---|---|
| Open | 324.87 |
| High | 330.81 |
| Low | 324.11 |
| **Close** | **328.21** |
| Volume | 37,225,800 |
| Total Return Index | 334.04 |
| Prior session close | 324.96 (2026-09-02) |

**Verified indicator values, 2026-09-03:**

| Indicator | Value | Read |
|---|---|---|
| close_10_ema | 319.41 | Price +2.76% above |
| close_50_sma | 314.255 | Price +4.44% above |
| close_200_sma | 283.607 | Price +15.73% above |
| macd | 2.672 | Above zero, rising |
| macds (signal) | 0.644 | MACD above signal |
| macdh | 2.028 | Positive and expanding |
| rsi | 63.38 | Constructive, not overbought |
| boll (mid) | 312.808 | Price +4.92% above |
| boll_ub | 327.375 | Price +0.26% **above** upper band |
| boll_lb | 298.241 | Band width 29.13 (~9.3% of mid) |
| atr | 7.377 | 2.25% of price |
| vwma | 315.206 | Price +4.12% above |
| mfi | 0.6599 (≈66 normalized) | Positive money flow, not extreme |

*Cross-check: all indicator series returned by the indicator tool agree with this snapshot to the published decimal (e.g., RSI 63.384, MACD 2.6722, hist 2.0278, ATR 7.3766, 50SMA 314.255, 200SMA 283.607). No discrepancies to flag.*

---

## 2. Regime Diagnosis: Primary Uptrend, Intermediate Recovery, Short-Term Breakout — but Extended

Three time frames are currently telling **different but compatible** stories:

1. **Primary (200-day): intact uptrend.** The 200 SMA has risen monotonically every session in the sample: **274.58 on 2026-07-20 → 283.61 on 2026-09-03**. Price is 15.7% above it.
2. **Intermediate (50-day): bullishly configured but only just re-accelerating.** The 50 SMA bottomed around **309.19 on 2026-08-14** and has since turned up to **314.255** (+1.6% in 14 sessions). It sits **30.65 points (10.8%) above the 200 SMA** — a wide, widening golden-cross spread.
3. **Short-term (10-day): impulsive and extended.** The 10 EMA has risen for **nine consecutive sessions** from **310.27 (2026-08-25) to 319.41 (2026-09-03)**, and price closed 2.76% above it.

**The critical nuance:** the primary trend never broke, but the *intermediate* trend did take real damage in late July/early August. This is a **recovery/repair phase inside a bull trend**, not a fresh bull leg from a clean base — which changes both the entry logic and the stop logic.

---

## 3. The Mid-Summer Break: What Actually Happened

Tracing the verified OHLCV:

| Event | Date | Verified prices |
|---|---|---|
| Highest close in window | 2026-07-28 | 340.08 (intraday high 342.89 on 7/28; 344.57 on 7/29) |
| **Gap-down shock** | 2026-07-31 | Prior close 333.43 → open 304.81, low 300.00, **close 308.91** (−7.35% on the day) on **132,489,100** shares |
| Closing low of correction | 2026-08-12 | **302.25** (intraday low 300.57) |
| Max drawdown, close-to-close | 7/28 → 8/12 | **−11.12%** (340.08 → 302.25) |
| Max drawdown, high-to-low | 344.57 → 300.57 | −12.77% |
| Recovery to date | 8/12 → 9/3 | **+8.59%** (302.25 → 328.21) |

**Key structural observation:** the 7/31 session was an **opening gap of −8.58%** (333.43 → 304.81 open) on roughly 2.6× typical volume. This was event-driven, not an orderly distribution. Combined with the **2026-06-25** session (close 275.15, −6.30%, 107.0M shares) and the 6/26 volume spike to **261.8M**, AAPL has now produced **two discrete single-day shock drops in ~10 weeks**. That fat left tail must be priced into position sizing — it is the single most important risk fact in this dataset.

**But the recovery has been technically high quality.** Since the low, we have a textbook series of **higher lows and higher highs**:

- Lows: 300.57 (8/12) → 302.94 (8/17) → 307.01 (8/21) → 312.80 (8/31) → 324.11 (9/3)
- Highs: 319.28 (8/19) → 322.37 (8/28) → 327.30 (9/1) → **330.81 (9/3)**

The 8/12 retest of the 8/3 low (302.56) held on **lower volume (41.7M vs 75.1M)** — a constructive, non-capitulative secondary test, not a distribution low.

---

## 4. Momentum: The Strongest Part of the Story

### MACD — clean, confirmed bullish reversal
- MACD **crossed below zero on 2026-08-11** (−0.827), bottomed at **−2.676 on 2026-08-17**.
- It **re-crossed above zero on 2026-08-31** (+0.297) and has since accelerated to **2.672**.
- MACD (2.672) sits **above** its signal (0.644) — the classic bullish posture.
- **The histogram has expanded for six consecutive sessions**: 0.152 (8/26) → 0.416 (8/27) → 0.896 (8/28) → 0.977 (8/31) → 1.511 (9/1) → 1.759 (9/2) → **2.028 (9/3)**.

This is not a marginal crossover — it is an **accelerating, broadening momentum thrust** confirmed by both the zero-line cross and six bars of histogram expansion. Historically this pattern favors continuation, but the histogram is now at its widest point of the leg, meaning the "easy" part of the momentum move is behind us; the first histogram contraction is the earliest warning to watch.

### RSI — room left, but note the prior divergence lesson
- RSI bottomed at **40.22 on 2026-08-12** — notably it **never reached 30/oversold**. That is a sign of underlying strength during the correction (buyers absorbed supply), and it is consistent with the recovery.
- RSI has since climbed to **63.38** (+23 points in 15 sessions): 47.86 (8/18) → 53.85 (8/19) → 51.43 (8/26) → 57.37 (8/28) → 61.06 (9/1) → **63.38 (9/3)**.
- **Not overbought.** There is ~6.6 RSI points of headroom before the 70 threshold.
- **Critical historical caution from this dataset:** RSI peaked at **66.78 on 2026-07-29 and 68.90 on 2026-07-28** — just below overbought — and the stock then gapped down −7.35% two sessions later. RSI did **not** flag that top via divergence; the signal was the *structure* (a failure to make further price progress while RSI stalled at 66–69). **We are now approaching that same 66–69 zone.** A push to 67–69 that fails to produce a new price high above 330.81 would be a meaningful, repeatable warning.

---

## 5. Volatility: Squeeze Resolved Upward

- ATR: **8.06 (7/30) → 9.87 (7/31, the gap day) → 7.38 (9/3)**. Volatility has fully mean-reverted from the shock. ATR is now **2.25% of price** — normal-to-low for AAPL, and declining (down from 7.63 on 8/21).
- Bollinger width collapsed into a genuine squeeze, then expanded:
  - **2026-08-27:** bands at 317.04 / 301.61 (width 15.43, **~5.0% of mid**) — the tightest reading in the sample.
  - **2026-09-03:** bands at 327.38 / 298.24 (width 29.13, **~9.3% of mid**).
  - Contrast: on **2026-07-23**, bands were 346.68 / 276.31 (width 70.36, ~23% of mid) — extreme post-event volatility.
- **Interpretation:** the 5% wide squeeze of 8/27 broke to the **upside** on 8/28 (bands immediately widened, close 319.70). This is a **volatility-expansion breakout**, not a fake-out band tag — price has held above the expanding upper band's trajectory for four sessions.

**However:** the 9/3 close of **328.21 is 0.26% above the upper band (327.375)**. Statistically, closes outside the band in a low-ATR regime tend to either (a) mark trend ignition with continued riding of the band, or (b) revert to the 20-day mid (312.81) within a few sessions. The tie-breaker is volume — see below.

---

## 6. Volume & Participation: The One Genuine Flaw

This is where I would push back on an otherwise clean bullish picture.

| Date | Close | Volume | Context |
|---|---|---|---|
| 2026-08-28 | 319.70 | 38,649,400 | Breakout from squeeze |
| 2026-09-01 | 325.13 | **53,167,400** | Strongest volume of the recovery; +1.66% |
| 2026-09-02 | 324.96 | 33,776,400 | Light pullback — good |
| **2026-09-03** | **328.21** | **37,225,800** | **New recovery high on sub-average volume** |

**Today's new high (close and intraday) came on volume roughly in line with — arguably below — the recent 3-week average (low-to-mid 40s millions).** The genuine conviction candle was **9/1 at 53.2M**. For a breakout to 328+ to be structurally sound, I would want to see a **>50M-share session** accompanying a close above 330.81.

Volume-weighted confirmation is nonetheless supportive:
- **VWMA = 315.21**, and it has turned up after bottoming at **307.76 (8/19)** → 309.15 → 309.19 → 309.11 → 309.99 → 310.80 → 312.49 → 313.89 → **315.21**.
- Price is **+4.12% above VWMA**. That spread is healthy in an uptrend but is a *stretched* distance to add fresh risk at.

**Verdict:** participation confirms direction but not magnitude. This looks more like **short covering + orderly accumulation** than institutional breakout buying.

---

## 7. Levels That Matter (all derived from verified data)

**Resistance**
| Level | Source | Significance |
|---|---|---|
| **330.81** | 2026-09-03 high | Immediate trigger; highest print since 7/30 |
| 333.74 / 334.75 | 7/17 close / 7/30 high | Supply shelf from the July top |
| **336.91–340.08** | 7/27–7/28 closes | The July peak zone; the real test |
| 342.89 / 344.57 | 7/28 / 7/29 highs | Breakout would put AAPL at new highs |

**Support**
| Level | Source | Significance |
|---|---|---|
| 324.11 | 9/3 low | First intraday shelf |
| **319.41** | 10 EMA | Short-term momentum floor |
| **315.21** | VWMA | Volume-weighted breakeven of recent buyers |
| **314.26** | 50 SMA | Intermediate trend line; did not break in the entire August decline on a closing basis |
| 312.81 | Bollinger mid | Mean-reversion target if the band tag fails |
| 307.01 / 305.0 | 8/21 low / early-August closes | Structural higher-low |
| **298.24** | Bollinger lower band | Furthest downside band reference |

**Note the confluence:** the **50 SMA (314.26), VWMA (315.21), 10 EMA (319.41), and Bollinger mid (312.81) are compressed into a ~6.6-point (2.1%) band from 312.8 to 319.4.** This is an unusually tight support cluster. A daily close below 312.8 would break *all four at once* and materially shift the tactical picture.

---

## 8. Actionable Playbook

### Scenario A — Continuation (base case, ~55% weight)
**Trigger:** Daily close **> 330.81** on volume **> 50M**.
**Logic:** Confirms the squeeze breakout, validates the six-bar MACD histogram expansion, and clears the 9/3 high.
**Targets:** 336.91 (7/27 close) → 340.08 (7/28 peak close) → 344.57 (7/29 high).
**Stop:** 2× ATR ≈ **14.75** below entry; or a close back **below 319.41** (10 EMA), whichever is tighter.
**Sizing:** With ATR at 2.25% of price, a 2-ATR stop = ~4.5% risk. Size positions so that 4.5% is within your per-trade loss budget — but given the two gap-shock precedents (6/25, 7/31), **assume stops can gap through**; consider using ≤60% of normal size on breakout entries and adding on confirmation.

### Scenario B — Extended pullback (highest-probability *entry* scenario, ~30% weight)
**Trigger:** Rejection at 330–331, or a close back inside the Bollinger band (< 327.4) followed by drift.
**Logic:** Price is 4.4% above the 50 SMA, 0.26% outside the upper band, and RSI at 63.4 approaching the 66–69 zone that preceded the July failure. A mean-reversion tag of the 20-day mid (312.81) is entirely normal.
**Action:** **Do not chase.** Layer bids in the **319.4 → 315.2 → 314.3** confluence (10 EMA / VWMA / 50 SMA). That is where risk/reward is best defined: a 3–4 point stop under 312.8 against a 12–28 point move to the July highs.
**Invalidation:** Two consecutive closes below **312.81** (Bollinger mid + 50 SMA). Below that, the next structural references are 307.01 and then 298.24.

### Scenario C — Failed breakout / trend break (~15% weight)
**Trigger:** Close **< 312.81** with expanding volume, and/or MACD histogram turning negative while MACD rolls back under zero.
**Logic:** That would break the four-way support cluster and negate the 8/28 squeeze breakout, re-opening the 300–302 August lows.
**Action:** Exit longs; the 200 SMA at 283.61 becomes the strategic line in the sand (still 13.6% below current price — so even a full scenario-C outcome leaves the primary uptrend intact).

### What to monitor (in priority order)
1. **Volume on any close above 330.81** — the single biggest tell. Sub-40M = suspect; >50M = real.
2. **MACD histogram slope** — first contraction after six up-bars is the early warning.
3. **RSI behavior in the 66–69 zone** — a stall there without a new price high mirrors the exact 7/28–7/29 setup that preceded the −7.35% gap.
4. **RSI/price divergence** on any push into 336–340 — momentum has to confirm the new high.
5. **Bollinger band width** — continued expansion supports trend-riding; contraction back toward 5–6% with price at the upper band warns of a stall.

---

## 9. Why These 8 Indicators

| Indicator | Unique contribution in *this* context |
|---|---|
| **close_200_sma** | The unambiguous anchor: rising daily, price 15.7% above. Establishes that the drawdown was a correction, not a reversal. |
| **close_50_sma** | The intermediate trend that actually got tested in August; its turn up at 8/14 and rise to 314.26 is the recovery's backbone and the key support confluence. |
| **close_10_ema** | Nine consecutive up-days makes this the precise short-term trigger; it distinguishes a healthy pullback (holds 319.4) from a momentum break. |
| **macd** | The zero-line re-cross on 8/31 is the cleanest regime-change signal available from this correction. |
| **macdh** | Histogram supplies the *acceleration* read (six expanding bars) — a detail the MACD line alone cannot show, and the earliest warning of exhaustion. |
| **rsi** | Quantifies how much runway remains before overbought (63.4 vs 70) and, critically, frames the 66–69 zone that historically preceded the July gap-down. |
| **boll_ub** | Captures the squeeze (5.0% width on 8/27) and its upward resolution; identifies the current extension risk (close 0.26% above 327.38). |
| **atr** | The risk engine: 7.38 (2.25% of price) sizes stops and positions and quantifies how much volatility has already normalized post-shock. |

*Deliberately excluded:* Stochastic RSI and MFI (redundant with RSI/money flow already captured); Bollinger middle/lower and VWMA are used as **auxiliary context** drawn from the verified snapshot rather than as primary selections, keeping the formal set at eight without sacrificing the support-confluence and volume reads.

---

## 10. Summary Table

| Dimension | Reading (2026-09-03) | Evidence | Bias |
|---|---|---|---|
| Primary trend | Up | 200 SMA 283.61, rising daily from 274.58 (7/20); price +15.73% | Strongly bullish |
| Intermediate trend | Up, re-accelerating | 50 SMA 314.26, turned up from 309.19 (8/14); +10.8% above 200 SMA | Bullish |
| Short-term trend | Up, extended | 10 EMA 319.41, nine straight up-days; price +2.76% | Bullish but stretched |
| Momentum | Strong & accelerating | MACD 2.672 > signal 0.644; hist 2.028 with 6 expanding bars; zero-line cross 8/31 | Bullish |
| Overbought/oversold | Neutral-constructive | RSI 63.38 from 40.22 (8/12); ~6.6 pts to 70 | Room to run |
| Volatility | Compressed, expanding upward | ATR 7.38 (2.25%); BB width 9.3% vs 5.0% on 8/27 and ~23% on 7/23 | Favorable |
| Band position | Outside upper band | Close 328.21 vs UB 327.375 (+0.26%) | Extension risk |
| Volume confirmation | **Mixed** | 9/1: 53.2M (conviction); 9/3 new high on only 37.2M | Caution flag |
| Volume-weighted level | Rising support | VWMA 315.21, up from 307.76 (8/19); price +4.12% above | Bullish, stretched |
| Drawdown from peak | −3.49% | 340.08 (7/28 close) → 328.21 | Recovered 8.6% from 302.25 |
| Key resistance | 330.81 / 336.91 / 340.08 / 344.57 | Verified highs and closes | Watch |
| Key support cluster | 312.81–319.41 | Boll mid, 50 SMA, VWMA, 10 EMA | High-conviction zone |
| Hard invalidation | Close < 312.81 | Breaks all four support measures | Risk trigger |
| Risk sizing | ATR 7.38; 2-ATR = 14.75 (4.5%) | Two gap-shock precedents (6/25 −6.3%, 7/31 −7.35%) | Reduce size, expect gaps |
| **Overall stance** | **Bullish, but do not chase at 328** | Trend + momentum agree; volume does not confirm | **Buy 315–319 pullbacks; add on >50M close above 330.81** |

---

**Bottom line for AAPL:** The trend structure is genuinely healthy — rising 200 and 50 SMAs, price above every moving average, MACD above zero with six expanding histogram bars, RSI at 63 with headroom, and a volatility squeeze that resolved upward. But the stock is pressing a fresh recovery high **outside the upper Bollinger band on unremarkable volume**, 4.4% above its 50 SMA, entering the same RSI zone (66–69) that immediately preceded a −7.35% gap on 2026-07-31. The highest-quality action is to **let it come to you**: accumulate in the 315–319 confluence where a stop under 312.81 defines risk tightly, and only pay up above **330.81** if volume finally exceeds 50 million shares.