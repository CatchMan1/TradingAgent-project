# AMZN — Multi-Indicator Technical Analysis
**Analysis date:** 2026-07-30 | **Last close:** $235.50 | **Instrument:** AMZN (Amazon.com, Inc.)

---

## 1. Data Integrity Check

I cross-validated the raw OHLCV series against the verified snapshot. **No discrepancies.** Both sources agree exactly on the latest session:

| Field | 2026-07-30 |
|---|---|
| Open | 233.35 |
| High | 239.82 |
| Low | 231.06 |
| Close | **235.50** |
| Volume | **101,839,800** |

All indicator values in the snapshot reconcile precisely with the standalone `get_indicators` series at 2026-07-30 (50SMA 246.3842, 200SMA 234.7547, 10EMA 236.2879, MACD −3.6343 / signal −2.1387 / hist −1.4955, RSI 44.4109, Boll mid 242.4125 / UB 258.0216 / LB 226.8034, ATR 7.3408, VWMA 240.8180). The snapshot also returns an MFI of 0.359586; that value appears to be on a 0–1 normalized scale (≈36 on a 0–100 scale). I treat it only as a soft, directionally-weak cross-check and do not lean on it.

---

## 2. Market Context — What Actually Happened in 2026

The dominant fact is that **AMZN is in a broad, volatile range with a deteriorating medium-term slope**, not a clean trend:

- **Jan 2026:** rally to a swing high close of **247.38 (2026-01-09)**.
- **Feb 2026:** a violent breakdown. **2026-02-05** closed 222.69 on 103.5M shares, then **2026-02-06** gapped down (open 202.70) and printed a **200.31 low** on **179.2M shares**. The floor was ultimately **196.00 intraday on 2026-02-17**.
- **Mar–May 2026:** a powerful recovery. From the 2026-04-07 close of 213.77 the stock accelerated — **221.25 (04-08) → 233.65 (04-09) → 238.38 (04-10)** — and ran to a **278.56 intraday high on 2026-05-05**, closing 274.99 on **2026-05-06**. Note 2026-04-30 was a huge-range distribution day (high 273.88, low 256.16, close 265.06, 101.0M shares).
- **June 2026:** a sustained slide from 270.64 (05-29) to **227.01 (06-25)**, with a **248.4M-share reversal day on 2026-06-26** (low 226.13, close 232.69) that marked a short-term bottom.
- **July 2026:** a rebound to **254.96 close / 258.08 high on 2026-07-15/16**, followed by a fresh leg down — **233.66 on 2026-07-23 (−4.57%, on a −3.51% opening gap)** — into **226.65 on 2026-07-29 (low 226.16)**.
- **2026-07-30:** a high-volume reversal. Opened 233.35, dipped to 231.06, closed **235.50 (+3.90% d/d)** at the upper end of the range, on **101.8M shares ≈ 2.6× the ~39M 20-session average**.

**The single most important structural observation:** AMZN's 2026-07-29 low **(226.16)** and its 2026-06-26 low **(226.13)** are **three cents apart after five weeks of chop**. RSI also double-tested the same zone (33.63 on 2026-06-25 vs 33.31 on 2026-07-29). This is a **tested double-bottom / demand shelf at ~225.5–226.2**, not a random low. That is the line in the sand.

---

## 3. Indicator Selection — Rationale for the Eight

I selected indicators to cover four non-overlapping information axes, deliberately avoiding redundant pairs (e.g., RSI + StochRSI, or MACD line + signal + histogram all as separate "picks"):

| Axis | Chosen | Why for *this* tape |
|---|---|---|
| Medium trend | **close_50_sma** | The 50SMA is falling steeply and is the primary overhead magnet; it also drives death-cross math. |
| Long-term trend / floor | **close_200_sma** | Price is trading *centimeters* from it ($235.50 vs 234.75). It is the current bull/bear arbitration line. |
| Short-term timing | **close_10_ema** | The immediate resistance directly above today's close — the first gate the bounce must clear. |
| Momentum regime | **macd** | Captures the 2026-07-23 regime flip (positive→negative) and today's first deceleration. |
| Momentum/mean-reversion | **rsi** | Confirms the 33-area double test and today's snap-back; identifies whether the bounce is exhaustion or initiation. |
| Volatility / mean reversion | **boll_lb** | 2026-07-29 was a *close below the lower band* (226.65 vs 227.45) — a genuine statistical stretch event that today reversed. |
| Risk calibration | **atr** | ATR ≈ $7.34 (3.1% of price) sets stops, targets, and position size objectively. |
| Volume conviction | **vwma** | Distinguishes whether the move is being *distributed* or *accumulated*; close < VWMA is a real warning here. |

(Bollinger mid/upper, MACD signal/histogram, and MFI were pulled and are cited as cross-checks, but the eight above carry the thesis.)

---

## 4. Trend Structure: Three Horizons, Three Different Messages

**Long-term (200SMA = 234.7547) — still intact, barely.**
The 200SMA is *rising* (232.84 on 2026-06-22 → 234.75 today), and today's close of 235.50 sits **just +0.32% above it**. Critically, **2026-07-29 closed at 226.65, i.e., −3.40% BELOW the 200SMA (234.659)** — the first decisive sub-200SMA close since the late-June cluster (2026-06-22/25/26 all closed marginally below it). Today reclaimed it. This is a **failed breakdown so far, not a confirmed one** — but the margin is only $0.75. It is fragile.

**Medium-term (50SMA = 246.3842) — clearly bearish.**
- Price is **−4.42% below** the 50SMA.
- The 50SMA has fallen every single session in the window: **257.08 (2026-06-22) → 246.38 (2026-07-30)**, a −10.70 decline, and it is now decelerating at ~**$0.67–0.74 per session** (7/27: −0.735, 7/28: −0.727, 7/29: −0.727, 7/30: −0.665). Any rally meets a *descending* ceiling, not a static one.
- **Death-cross math:** the 50SMA−200SMA spread is **+11.63** (246.3842 − 234.7547). At the current ~$0.70/session narrowing pace, that gap closes in roughly **16–17 sessions (mid-to-late August)** *if price simply goes nowhere*. I am not asserting a death cross will occur — I am saying the clock is now visible, and it requires price to hold above ~$235–240 to be avoided.

**Short-term (10EMA = 236.2879) — bearish, but being challenged.**
The 10EMA peaked at 247.60 (2026-07-20) and has collapsed to 236.29, with today's close **$0.79 (−0.33%) below it**. Today's close is *right at* this line. A close above 236.29 tomorrow would be the first objective short-term evidence of a momentum turn; a rejection there would confirm the bounce as a dead-cat.

**Net alignment:** close ($235.50) is **below** the 50SMA, **below** the 10EMA, **below** the Bollinger mid, and **above** the 200SMA. That is a textbook **bearish short-term stack inside an intact long-term uptrend** — i.e., a corrective downtrend within a larger uptrend, currently testing its last major support.

---

## 5. Momentum: The Most Nuanced Part of the Setup

**MACD — bearish regime, but decelerating.**
- The MACD line was **positive from 2026-07-15 (+0.2602) through 2026-07-22 (+0.5590)**, peaking at **+0.8237 on 2026-07-20**.
- On **2026-07-23** it flipped both below zero (−0.5298) *and* below its signal — a dual bearish crossover in a single session, coinciding with the −4.57% gap-down day.
- It is now **−3.6343**, below the signal at **−2.1387**, histogram **−1.4955**.
- **The one constructive detail:** the histogram improved from **−1.9863 (7/29) to −1.4955 (7/30)**, a +0.49 narrowing — the **first histogram improvement since 2026-07-22**. That is a deceleration of downside momentum, not a reversal. One print is not a signal; a second consecutive narrowing would be.

**RSI — recovered from the ledge, but no divergence of strength.**
- RSI bottomed at **33.31 on 2026-07-29** and rebounded to **44.41** today. Note it **did not go below 30** — this was a "near-oversold grind," not a capitulation washout.
- The 33.31 low **precisely echoes the 33.63 low of 2026-06-25**, reinforcing the ~226 double bottom as a genuine momentum shelf.
- **Internal deterioration preceded the drop:** RSI peaked at **60.14 on 2026-07-15** (close 254.96). On **2026-07-16** price printed a *higher* high (**258.08 vs 256.48**) while RSI *fell* to **54.19** — a legitimate bearish momentum divergence that correctly preceded the 258.08 → 226.16 (−12.4%) decline.
- Today's RSI of 44.41 is mid-range: it has room to run to 60 without any overbought constraint, which *supports* further mean-reversion — but 44 is also nowhere near "buy signal" territory.

---

## 6. Volatility & Mean Reversion

**Bollinger Bands (20,2): mid 242.4125 | upper 258.0216 | lower 226.8034.**
- **2026-07-29 was a genuine band-break:** close 226.65 vs lower band 227.4487 (low 226.16). Today's close of 235.50 snapped back inside the band — a classic **lower-band tag and revert**, historically the highest-probability short-term mean-reversion setup.
- **Bandwidth is 12.88%** ((258.02−226.80)/242.41). That is dramatically compressed vs late June — on 2026-06-22 it was **20.2%** ((276.85−226.14)/251.49). Volatility has halved. However, bandwidth has begun **re-expanding** over the last three sessions (11.1% → 12.6% → 12.9%), which typically *precedes* a directional resolution.
- **Confluence worth flagging:** the July range is roughly **226.16 to 258.08**; its midpoint is **242.12**, which is within $0.30 of the Bollinger mid at **242.41**. The 20-SMA and the range pivot are the *same level*. That makes **~242** the single most important decision point on the chart.

**ATR = 7.3408 (3.12% of price).**
ATR has **contracted** from 8.59 (2026-06-29) to 6.89 (2026-07-29) before ticking up to 7.34 today with the wide 8.76-point range. Practical translation:
- 1 ATR ≈ $7.34, 2 ATR ≈ $14.68.
- A stop placed beneath the **226.13/226.16 double bottom** (e.g., 225.50) from today's 235.50 is **$10.00 = 1.36 ATR** — a *statistically valid* stop, not an arbitrary one.
- A 1-ATR stop at 228.16 would sit *inside* normal daily noise and above the swing low — it would be noise-stopped. **Do not use a sub-1.3-ATR stop below a tested low here.**

---

## 7. Volume: The Bear's Best Argument

**VWMA = 240.8180.** Price at 235.50 is **−2.21% below** the volume-weighted average. This means the **average dollar transacted over the lookback is under water** — recent selling has occurred on heavier volume than recent buying. That is distribution, and it is the cleanest counter-argument to the bullish bounce narrative.

The VWMA trajectory tells the story: it rose steadily from 236.70 (2026-06-26) to a peak of **247.03 on 2026-07-22**, then rolled over to 240.82 — a **$6.21 decline in six sessions**, faster than the 50SMA. Volume-weighted money flow turned before price did.

**The offsetting bullish datum:** today's **101.8M shares (~2.6× the 20-day average of ~39M)** on a close near the session high is *accumulation-style* volume — the mirror image of 2026-06-26's 248.4M-share reversal that produced a 5% bounce. Two consecutive high-volume reversal days (6/26 and 7/30) at the *same price zone* (226–231) is meaningful demand evidence.

**Verdict on volume:** conflicting. Price < VWMA = bearish positioning; today's volume signature = bullish absorption. **The tiebreaker is follow-through on the next 1–3 sessions.**

---

## 8. Synthesis — Three Scenarios With Explicit Levels

**Resistance ladder (overhead):**
1. **236.29** — 10EMA (immediate gate, $0.79 above)
2. **240.82** — VWMA (distribution line)
3. **242.41** — Bollinger mid = July range midpoint (the pivotal level)
4. **246.38** — falling 50SMA
5. **247.55–249.99** — the 2026-07-20/21 congestion closes
6. **254.96–258.08** — 2026-07-15/16 highs and upper band (258.02)

**Support ladder (below):**
1. **234.75** — rising 200SMA (currently $0.75 beneath the close)
2. **231.06** — 2026-07-30 low
3. **226.13 / 226.16** — June 26 / July 29 double bottom + lower band (226.80)
4. **~221–223** — June 23–24 lows (232.00/232.95 aren't support; the June 22 low 232.24 and June 25 low 225.55 are the relevant ones)

**Scenario A — Base case (roughly 50%): Range repair, 236 → 242.**
The lower-band revert plus the double-bottom hold plus the 200SMA reclaim argue for continued mean-reversion toward the 10EMA (236.29), then VWMA (240.82), then the 242.41 pivot. This is a *bounce inside a downtrend*, not a trend change, unless 246.38 is reclaimed. **Trigger:** close above 236.29. **Confirmation:** up-volume on the breakout day.

**Scenario B — Bull escalation (roughly 20%): Trend repair, 242 → 250+.**
Requires a *daily close above 242.41* on above-average volume, which would put price back above the VWMA, the 20-SMA, and the July range midpoint simultaneously — neutralizing the distribution read and stalling the 50SMA decline. Next objectives 246.38 → 249.99 → 258.02. **This is the only scenario that removes the death-cross clock.**

**Scenario C — Bear resumption (roughly 30%): Failure at 236–242 → retest 226.**
If the bounce is rejected at the 10EMA or VWMA, the sequence that matters is a **daily close below 231.06** (today's low) and especially **below 226.13** on volume. A confirmed break of the double bottom opens the air pocket toward the ~221–223 June lows, and would likely produce the 50/200 death cross in the process.

---

## 9. Actionable Trade Plans

**Plan 1 — Tactical long (mean reversion, not a trend trade).**
- **Entry:** (a) aggressive — current 235.50 with a limit no higher than 236.50; or (b) preferred — on a *pullback into 231–233* that holds (better R:R, less chasing).
- **Stop:** **225.50** (below both 226.13 and 226.16). Risk ≈ $10.00 = **1.36 ATR** — appropriate.
- **Targets:** T1 240.82 (VWMA), T2 242.41 (Boll mid/pivot), T3 246.38 (50SMA).
- **Honest R:R assessment:** from 235.50 the T1 reward is $5.32 vs $10.00 risk = **0.53:1**; T2 = **0.69:1**; T3 = **1.09:1**. *This is a poor entry.* Entering on a 231–233 pullback improves T2 R:R to ~1.4:1. **Do not size this as a high-conviction swing.**
- **Sizing math:** on a $100,000 account risking 1% ($1,000) with a $10 stop → **100 shares (~$23,550 notional, ~23.5% of account)**. Halve it if the 236.29 reclaim doesn't happen within two sessions.

**Plan 2 — Short into strength (the structurally superior setup).**
- **Entry zone:** **242–247**, i.e., the confluence of Bollinger mid (242.41), VWMA (240.82→242), and the falling 50SMA (246.38). The 50SMA descending into price is the key edge.
- **Stop:** **248.50** (above the 248.44 close of 2026-07-21 and above the 50SMA). Risk ≈ $4–6.
- **Targets:** T1 234.75 (200SMA), T2 226.80 (lower band), T3 226.13 (double bottom). Reward $16–20 vs $5 risk ≈ **3:1 to 4:1**.
- **Invalidation:** a *daily close above 247.55* on volume — that breaks the lower-high sequence and voids the setup.

**Plan 3 — Event-driven breakout (both directions).**
Because bandwidth is compressing but re-expanding (12.88% and rising for three sessions) after a 20%→13% contraction, a directional resolution is loading. Trade the *break of the range edges* on volume: **> 246.38** favors the bulls toward 258; **< 226.13** favors the bears toward 221.

**Risk-management rules specific to this tape:**
- Do not use stops tighter than **1.3 ATR ($9.5)** when positioning against the 226 shelf — ATR is $7.34 and daily ranges have been 8+ points.
- Treat **242.41** as the regime line. Longs above it, shorts below it.
- Watch the **50SMA−200SMA spread (+11.63)** weekly. If it compresses below ~+5 without a price recovery, positioning should tilt defensively ahead of the cross.

---

## 10. What Would Prove Me Wrong

- **Bullish invalidation of my cautious stance:** two consecutive daily closes **above 242.41** with volume > 60M, *and* MACD histogram turning positive. That combination would force a re-rating to "uptrend resumption."
- **Bearish invalidation of the bounce thesis:** a close **below 231.06** tomorrow would reframe today's 101.8M-share candle as a one-day squeeze/covering event rather than accumulation, and put 226.13 back in play immediately.
- **Indicator caveat:** today's MACD histogram improvement (−1.99 → −1.50) and RSI jump (33.3 → 44.4) are **single-session** observations. Neither constitutes a trend signal in isolation, and I have not claimed historical backtest validation of any level.

---

## 11. Summary Table

| Dimension | Reading (2026-07-30) | Interpretation | Actionable Level |
|---|---|---|---|
| **Close** | 235.50 (+3.90% d/d) | High-volume reversal candle, high in range | Range: 231.06–239.82 |
| **Volume** | 101.84M (~2.6× 20-day avg ~39M) | Absorption/accumulation signature — but needs follow-through | Confirm with >39M on a close >236.29 |
| **200 SMA** | 234.7547 (rising) | Long-term trend intact *by +0.32% only*; reclaimed today after 7/29 breach (−3.40%) | **234.75 = bull/bear arbitration line** |
| **50 SMA** | 246.3842 (falling ~$0.70/session) | Medium-term bearish; descending ceiling; price −4.42% below | **246.38** = trend-repair gate |
| **50−200 spread** | +11.63 | Death-cross clock visible; ~16–17 sessions at current pace | Monitor weekly; <+5 = defensive |
| **10 EMA** | 236.2879 (falling from 247.60 on 7/20) | Price $0.79 below — bounce is stalling exactly at first resistance | **Close >236.29 = short-term turn confirmed** |
| **MACD** | −3.6343 vs signal −2.1387; hist −1.4955 | Bearish regime since 7/23 dual crossover, but hist first narrowed since 7/22 | Need 2nd narrowing for validity |
| **RSI** | 44.4109 (from 33.31 on 7/29) | Near-oversold double test (33.63 on 6/25); not oversold, no overbought cap | 30/70 unused; 50 = momentum midline |
| **Bollinger (mid/UB/LB)** | 242.4125 / 258.0216 / 226.8034 | 7/29 closed *below* lower band → today reverted inside. Bandwidth 12.88% vs 20.2% on 6/22 | **242.41 = range midpoint + 20SMA = pivot** |
| **ATR** | 7.3408 (3.12% of price) | Contracted from 8.59 (6/29); rising slightly with today's range | Min viable stop ≈ $9.5–10; 2 ATR = $14.68 |
| **VWMA** | 240.8180 (fell $6.21 in six sessions) | Close is −2.21% **below** VWMA → distribution; bear's strongest evidence | **240.82** = first real supply |
| **Key support** | 234.75 → 231.06 → 226.13/226.16 | Double bottom (6/26 low 226.13; 7/29 low 226.16 — 3¢ apart) + lower band 226.80 | **226.13 is the thesis decider** |
| **Key resistance** | 236.29 → 240.82 → 242.41 → 246.38 → 258.02 | Four stacked ceilings; only a close >242.41 repairs the trend | **242.41 is the regime line** |
| **Overall bias** | **Neutral-to-bearish; tactical bounce in progress** | Corrective downtrend within an intact long-term uptrend, sitting on a tested double bottom | Long above 236.29 (poor R:R) / Short 242–247 (3–4:1 R:R) |