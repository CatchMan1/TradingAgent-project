# AMZN — Multi-Timeframe Technical Analysis
**Analysis date: 2026-08-19 | Last verified close: $265.84**

---

## 1. Sources, verification, and data integrity notes

All exact price, volume, and indicator values below come from the **verified market snapshot for 2026-08-19** and the point-in-time OHLCV series (2025-11-03 → 2026-08-19, 199 rows). The snapshot and the price series are **fully consistent** — the last row in the CSV (2026-08-19: O 260.85 / H 266.40 / L 258.58 / C 265.84 / V 35,762,400) matches the snapshot exactly. No reconciliation was needed.

Two things I explicitly flag:

1. **No dividends and no splits** in the window (`split = 1.0`, `dividend = 0.0` on every row), so `technical_total_return_index` equals the close. All percentage moves below are pure price moves.
2. **Bollinger Bands are currently distorted.** Snapshot values: middle 258.73, upper **296.99**, lower **220.47**. That is a band width of ≈76.5 points, or ≈29.6% of the middle band. I verified this is not a data error — the 20-session window (2026-07-23 → 2026-08-19) contains both the 226.65 low-close (07-29) and the 284.02 high-close (08-03), which inflates the sample standard deviation to ≈19.1. **Consequence: band-touch and "walking the band" signals are unusable right now.** The upper band is ~11.7% above spot — price would need a limit-up-style move to tag it. Bollinger is therefore *excluded* from my 8-indicator decision set and used only as a reference for the 20-day mean.

---

## 2. The single most important fact: AMZN is post-repricing, mid-consolidation

The last four weeks contain the entire story:

| Date | Close | Volume | Note |
|---|---|---|---|
| 2026-07-29 | 226.65 | 44.96M | Low of a *second* test of the ~226–227 zone |
| 2026-07-30 | 235.50 | 101.84M | First impulse (+3.90%) |
| 2026-07-31 | 271.58 | 129.05M | **+15.32% single session** |
| 2026-08-03 | 284.02 (H 287.20) | 90.83M | Highest close/high in the entire sample |
| 2026-08-18 | 259.45 (L 257.73) | 33.17M | Pullback trough: **−8.65% from 08-03 close** |
| 2026-08-19 | **265.84** | 35.76M | **+2.46%**, close above 08-18's high (262.18) |

The 07-29 → 07-31 move was **+19.82% in two sessions on 3.4× and 2.9× the recent average volume**. That volume signature is consistent with a hard fundamental catalyst (typically a quarterly report), but the dataset does not label the event, so I will not assert the cause — only the effect: a violent re-rating that left a large gap zone beneath price (07-30 low 231.06 → 07-31 open 265.00) and a dense supply shelf above it.

Structurally, 07-29 (close 226.65, low 226.16) is a **second test of the 2026-06-25 low (close 227.01, low 225.55)** — a ~226/227 double-bottom that the subsequent rally resolved higher from. Concurrently, the February 2026 collapse (02-05 close 222.69 → 02-06 low **200.31** on 179.2M shares) marks the cycle low; from 200.31 to the 08-03 high of 287.20 is **+43.4%**.

---

## 3. Indicator selection and why these 8

| Indicator | Value (2026-08-19) | Why it belongs in this specific setup |
|---|---|---|
| **close_200_sma** | 238.22 | The primary-trend arbiter after a +43% run off the Feb low. Needed to know whether the retracement is a dip or a regime change. |
| **close_50_sma** | 249.00 | The medium-term line the post-gap pullback has *not* tested. Also the natural invalidation level for a swing long. Rising for 15 straight sessions — trend confirmation. |
| **close_10_ema** | 264.46 | Post-gap price discovery is fast; the 10 EMA is the only average fast enough to time the 08-19 reclaim. |
| **macd** | 4.81 | Trend/momentum regime: still positive and above zero despite the pullback. |
| **macdh** | −0.8817 | The *deceleration* signal — negative for 3 sessions. Distinguishes "healthy pullback" from "momentum rollover" at the margin. |
| **rsi** | 55.64 | Post-spike mean reversion: 72.23 (08-03) → 50.93 (08-18) → 55.64. Confirms the overbought condition was worked off *without* a breakdown. |
| **atr** | 7.8554 (2.95% of price) | Post-gap volatility is still ~27% above its 07-29 level (6.89). Mandatory for stop placement and sizing. |
| **vwma** | 271.9144 | The decisive level. Price sits **below** the volume-weighted average of recent trade — the cleanest read on whether the 08-03 buyers are trapped or absorbed. |

I deliberately did **not** include Bollinger bands (distorted, see §1), a stochastic (redundant with RSI), or both MACD line and signal as separate entries beyond what's needed — the histogram already encodes the crossover state.

---

## 4. Trend analysis

**Primary trend — bullish, intact, and *improving*.**
Close 265.84 vs 200 SMA 238.22 = **+11.59%**. The 200 SMA has risen every session since at least 2026-04-21 (225.86 → 238.22), a monotonic ~12-month base. The 50 SMA at 249.00 sits **10.78 points above** the 200 SMA, and that spread is widening (it was 9.63 on 07-30). This is a mature, still-expanding bullish alignment — no death-cross risk anywhere on the horizon.

**Intermediate trend — corrective consolidation inside an uptrend.**
The 50 SMA bottomed at 246.38 on 2026-07-30 and has climbed for 15 consecutive sessions to 248.9978. Critically, the entire post-gap pullback (08-03 → 08-18) occurred **entirely above the 50 SMA** — the closest approach was 259.45 on 08-18, still **4.2% above** the 50-day. That is the hallmark of a trend digesting a vertical move, not of distribution.

**Short-term trend — the 08-19 session is a genuine reversal signal, on weak volume.**
The 10 EMA flattened then rolled over from 267.18 (08-12) to 264.15 (08-18) before ticking up to 264.46. On 08-19 price:
- opened at 260.85, dipped only to 258.58 (**held above the 08-18 low of 257.73**),
- closed at 265.84, i.e. **above the 08-18 high of 262.18** — a bullish outside/reversal session,
- reclaimed the 10 EMA (264.46) by +0.52%.

That is a textbook higher-low + prior-high-reclaim sequence. The caveat is volume: **35.76M vs a ~48.2M 21-session average (≈71% of normal)**. A reversal on contracting volume is *unconfirmed*.

**The one genuinely bearish data point: price vs VWMA.** VWMA is 271.9144 — price is **2.23% below it**. The VWMA has climbed relentlessly from 245.72 (07-31) to 271.91 because the enormous volume printed at 265–284. Translated: **the average dollar-weighted buyer of the last ~20 sessions is under water by ~$6.** That overhead supply shelf is the single best explanation for why every rally attempt between 08-04 and 08-11 stalled in the 272–278 band. Until price closes above ~272 on expanding volume, bounces are suspect.

---

## 5. Momentum analysis

**RSI — textbook post-spike digestion.** AMZN went 33.31 (07-29, near-oversold) → 67.88 (07-31) → **72.23 (08-03, overbought)** → 50.93 (08-18, neutral pivot) → **55.64** now. The important nuance: the correction from overbought was achieved by *time/consolidation* (eight sessions of drift) rather than a momentum crash, and RSI never broke below 50 decisively (08-18's 50.93 was the low). That pattern historically favors trend continuation — RSI reset to the mid-50s gives the next leg room without immediately re-entering overbought territory. Current reading is neutral-to-bullish with **no divergence signal** available in the data (no confirmation of higher price high vs lower RSI high on this timeframe).

**MACD — positive but decelerating; the key near-term caution.**
- MACD line: peaked **8.4324 on 08-11**, now **4.8105** — five consecutive declining sessions.
- Signal line: **5.6923** (derived: 4.8105 − (−0.8817)).
- Histogram: **−0.8817**, after peaking at **+4.6192 on 08-05**. Negative since 08-17 (−0.3097), deteriorated 08-18 (−0.9082), and *marginally* improved on 08-19.

So a **bearish MACD crossover occurred on 2026-08-17** and remains in force. But the context matters: the MACD line is still at +4.81, deep above zero, and the histogram contraction is flattening. This is characteristic of momentum resetting in a strong uptrend, not of a fresh downtrend initiation. A **histogram recross above zero** (needs MACD > 5.69, roughly a close > ~272–274) would be the momentum confirmation of the 08-19 price reversal.

**Momentum vs trend conflict to state plainly:** price structure (higher low, reclaim of 10 EMA and 20-day mean) turned constructive on 08-19, while MACD (negative histogram) and VWMA (overhead supply) have not yet confirmed. The burden of proof is on the bulls.

---

## 6. Volatility and risk management

- **ATR = 7.8554**, i.e. **2.95% of spot**. It spiked from 6.89 (07-29) to a peak of **9.9478 (08-03)** on the repricing and has decayed for eight straight sessions (9.98 → 7.86). Volatility is mean-reverting *but still elevated*: the 07-01→07-29 average ATR was ~7.8, so we are essentially back to pre-gap levels while price sits 17% higher. That is a **constructive volatility contraction** — a coiling pattern.
- **Stop placement must respect 7.86 ATR.** A stop inside 1 ATR (< ~$8 away) is noise-fodder in this name right now.
  - Aggressive long stop: **$254.00** (1.5 × ATR = $11.78 below 265.84). Sits below the 07-15 close of 254.96 and below the entire 08-12→08-19 congestion. Risk = 4.45%.
  - Conservative structural stop: **$256.50**, just under the 08-18 low of 257.73. Risk = $9.34 (3.51%), ~1.19 ATR — acceptable *only* if entered on a confirmed breakout above 272 rather than at current price.
  - Invalidation stop for the trend itself: **$248.00**, below the 50 SMA (249.00). Risk = 6.7%.
- **Sizing:** with a 1.5-ATR stop, a 1% account risk implies ≈0.22× account notional; with the 50-SMA stop, ≈0.15×. Given the negative MACD histogram and light reversal volume, I would size **no more than half of a normal position on a 265–266 entry** and reserve the remainder for a close above ~272.

---

## 7. Key levels (all derived from tool data)

**Resistance (a dense, volume-backed shelf):**
- **$271.58–$272.65** — the cluster: 07-31 close 271.58, 08-05 close 272.65, 08-06 close 272.26, 08-11 close 272.27, and **VWMA 271.91**. *This is the pivot.*
- **$278.09 / $280.14** — 08-10 close / 08-10 high, the failed-rally high.
- **$284.02 / $287.20** — 08-03 close / sample high.
- **$296.99** — Bollinger upper (distorted; informational only, not a real target).

**Support:**
- **$264.46** — 10 EMA (just reclaimed).
- **$258.58–$259.45** — 08-19 low / 08-18 close; **$258.73** is the 20-day mean. A tight confluence — this is the first line of defense and it *held* on 08-19.
- **$257.73** — 08-18 low (the higher-low pivot).
- **$254.96** — 07-15 close.
- **$248.99** — 50 SMA (the structural line).
- **$238.22** — 200 SMA.
- **$226.16 / $225.55** — double-bottom lows (06-25 / 07-29).

---

## 8. Actionable playbook

**Scenario A — Bullish continuation (primary plan).**
*Trigger:* a daily close **above $272.65** with volume **≥ ~48M** (the 21-session average). That simultaneously clears the VWMA shelf, flips the MACD histogram back positive, and confirms the 08-19 reversal.
*Execution:* buy the breakout (or the first pullback to 268–270 that holds). Stop **$254.00** (1.5 ATR), or tighten to $259.50 once above 275.
*Targets:* **T1 $278.10**, **T2 $284.00**, **T3 $287.20**. A measured-move extension from the 226.65 base is larger but I will not project beyond the observed range.

**Scenario B — Range / base-building (currently the highest-probability path).**
AMZN chops between **~258.5 and ~272.5** while the histogram works off and the earnings gap rolls out of the 20-day window (the 07-30/07-31 sessions exit the window in late August, which will sharply normalize the bands). Trade the edges small; do nothing in the middle. A close back below **258.58** invalidates the 08-19 reversal and shifts focus to the 50 SMA.

**Scenario C — Trend failure.**
A decisive close below the **50 SMA at $249.00** (with the 10 EMA already below price) breaks the medium-term structure and opens **$238.22** (200 SMA). Do not pre-position for this — nothing in the data supports it yet; the 50/200 spread is widening, not narrowing.

**Explicitly: not a short here.** Price is +11.6% above a rising 200 SMA, RSI is mid-range rather than overbought, and the 08-19 session was a bullish outside day that held the higher low. Shorting into that with the primary trend up is a low-expectancy trade.

---

## 9. What would change my view

| Signal | Bullish confirmation | Bearish deterioration |
|---|---|---|
| Close vs VWMA (271.91) | Close **> 272.65** | Repeated rejection; third failure at 272 |
| MACD histogram | Recross **> 0** | Sustained decline below **−1.5** with MACD < 0 |
| RSI | Push back **> 60** | Break **< 45**, especially < 40 |
| Price structure | Higher low above **262**; holds 258.73 | Close **< 257.73**, then < 249.00 (50 SMA) |
| Volume | Breakout on **> 48M** | Distribution on a 258 breakdown > 40M |
| 10 EMA (264.46) | Stays above; 10 > 20-day mean | Crosses back below 10 EMA and 258.73 |

---

## 10. Summary table

| Dimension | Reading (2026-08-19) | Interpretation | Actionable level |
|---|---|---|---|
| **Last close** | $265.84 (+2.46%), V 35.76M | Bullish outside/reversal day, light volume | Confirmation needed |
| **close_200_sma** | 238.22 (rising 199 sessions) | Primary uptrend intact; +11.59% above | $238.22 major support |
| **close_50_sma** | 249.00 (rising 15 sessions) | Intermediate trend intact; pullback never tested it | **$249.00 = trend invalidation** |
| **close_10_ema** | 264.46 | Reclaimed on 08-19 by +0.52% | Lose it → retest 258.7 |
| **vwma** | 271.91 | Price **2.23% below** → overhead supply / trapped longs | **$272 = the pivot** |
| **macd** | 4.8105 (peak 8.4324 on 08-11) | Positive, decelerating, 5 straight declines | Recross > 5.69 = bullish |
| **macdh** | −0.8817 (bear cross 08-17) | Momentum not yet confirmed; contracting | > 0 = confirmation |
| **rsi** | 55.64 (72.23 → 50.93 → 55.64) | Overbought fully worked off, no divergence | > 60 bullish / < 45 bearish |
| **atr** | 7.8554 (2.95% of price) | Elevated but contracting 8 sessions (was 9.95) | 1.5 ATR stop = $254 |
| **Bollinger** | mid 258.73; UB 296.99 / LB 220.47 | **Distorted by the 07-30/07-31 gap** — do not trade bands | 258.73 = 20-day mean support |
| **Volume regime** | Last 5 sessions ≈34.5M vs ~48.2M avg | Pullback was low-volume (good); bounce also low-volume (unconfirmed) | > 48M needed on breakout |
| **Key structure** | 226/227 double bottom (06-25, 07-29) → 287.20 high (08-03) | Post-catalyst bull flag, 8.65% deep | Flag resolves above 272.65 |
| **Bias** | **Constructive / constructive-cautious** | Trend up, momentum resetting | Buy strength > 272.65, not weakness |