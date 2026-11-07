# AAPL — Technical Assessment for 2026-08-14

## 1. Data integrity & verified anchor

All claims below are anchored to `get_verified_market_snapshot` for **AAPL** as of **2026-08-14**. I cross-checked every indicator value against the separate `get_indicators` pulls and found **no discrepancies** — snapshot and indicator series agree to the decimal (e.g. RSI 43.672337, MACD −2.461164, MACD signal 0.187072, histogram −2.648236, 50SMA 309.1908, 200SMA 280.48365, 10EMA 309.459029, Bollinger mid 318.4285 / upper 344.589548 / lower 292.267453, ATR 7.860879, VWMA 314.112816).

One flag: the snapshot reports `mfi = 0.485091`, which appears to be on a 0–1 rather than 0–100 scale. Its scale is ambiguous, so I have **excluded it** from the signal set rather than interpret an arbitrary reading.

**Latest verified session (2026-08-14):** Open 306.00, High 307.49, Low 304.30, **Close 305.93**, Volume 28,229,400, total-return index 311.3665.

---

## 2. Trend structure: a healthy long-term uptrend inside a broken intermediate trend

AAPL is currently a **two-speed tape**, and the whole report hinges on keeping those speeds separate.

**Long-term (primary trend) — intact and bullish.**
The 200-day SMA at **280.48** is rising monotonically (271.06 on 2026-07-06 → 280.48 on 2026-08-14, roughly +0.22/session). The close of 305.93 sits **+9.1% above it**. The 50-day SMA at **309.19** sits **+10.2% above the 200-day** (spread ≈ 28.7 points). That is a wide, still-positive structural alignment — the primary uptrend has not been invalidated by the July/August damage.

**Intermediate trend (50-day) — rolled over and now mildly declining.**
The 50SMA peaked at **309.786 on 2026-08-07** and has ticked down for five straight sessions to 309.191. That is the first sustained flattening-to-decline in the series since early July. Critically, the close has been **below the 50SMA for 11 consecutive sessions** (from 2026-07-31 through 2026-08-14), which is the defining characteristic of the current corrective phase.

**Short-term (10-day) — still falling, but decelerating.**
The 10EMA collapsed from **331.31 (2026-07-30)** to **309.459 (2026-08-14)** — a ~21.9-point decline in 11 sessions. Price is **−1.14% below** it. Note the razor-thin 10EMA vs 50SMA gap: **309.459 vs 309.191, a spread of just +0.27**. With the 10EMA dropping roughly 1–1.2 points per session and the 50SMA drifting down ~0.1–0.2, a **bearish 10/50 cross is plausible within 1–3 sessions**. This is the single most important near-term technical risk in the setup, and it happens to coincide almost exactly with where price needs to prove itself.

**Where we are in the range:** Within the 2026 data available (2026-01-02 → 2026-08-14), the highest close is **340.08 (2026-07-28)** and the highest intraday print is **344.57 (2026-07-29)**. The lowest close in the window is **246.63 (2026-03-30)** with an intraday low of **243.42 (2026-01-20)**. From the 7/28 closing peak, the current close is **−10.04%**; from the 7/29 intraday high to the 8/12 closing low of 302.25, the tape fell **−12.28%**. So this is a **10–12% drawdown within an intact primary uptrend** — historically a repair zone, not a trend-ending zone, *provided* 300 and then the 200SMA hold.

---

## 3. The 2026-07-31 regime break — the event that set the current tone

This is the fact that dominates the current chart, and it deserves precision:

- **2026-07-30:** Close 333.43, volume 74.8M.
- **2026-07-31:** Open **304.81** (a huge gap down of −28.62 from the prior close), high 310.69, **low 300.00**, close **308.91**, volume **132.49M**.

That is a **close-to-close decline of −24.52 points (−7.35%)** on volume ~1.77x the prior session. The gap zone from **304.81 up to 333.43** remains entirely **unfilled** — price has not traded above 316.29 (the 8/6 high) since. This unfilled gap is the dominant overhead supply shelf and the reason bounces keep stalling in the 308–313 area.

Since 7/31 the tape has been **repair-and-chop, not recovery**: closes of 303.42 (8/3), 309.38, 311.00, 312.41, 313.33 (8/7) — then a fade to 308.26, 304.91, **302.25 (8/12)**, 305.26, 305.93. August's high (316.29 on 8/6) is a **lower high** versus July's 344.57. Lower highs plus a declining 10EMA is textbook corrective structure, even if the lows have so far held.

**The one constructive detail:** the last three sessions have produced **rising intraday lows — 300.57 (8/12) → 302.05 (8/13) → 304.30 (8/14)** — and rising closes off 302.25. That is a nascent short-term base attempt directly on top of the 300.00 (7/31) low. It is real but unconfirmed: it has not been tested by volume.

---

## 4. Momentum: bearish, but the rate of deterioration is visibly slowing

**RSI = 43.67**, up from the 2026-08-12 print of **40.22** and the 8/3 print of **40.34**. Key nuance: **RSI never reached 30 (oversold)** even on the −7.35% gap day (43.24 on 7/31). That cuts both ways:
- It tells you the selloff was an orderly de-risking rather than capitulation — supportive of a bottoming process.
- It also means there is **no oversold spring loaded** to fuel a violent mean reversion. RSI in the low-to-mid 40s is "neutral-bearish," the least informative zone for a directional trigger.
- For context, RSI peaked at **71.65 on 2026-07-17** and **71.43 on 7/16** — a genuine overbought top that preceded the breakdown by ~2 weeks. That top distribution is now resolving.

**MACD = −2.461**, signal = **+0.187**, histogram = **−2.648**. The sequence is unambiguous:
- Histogram flipped negative on **2026-07-31** (from +0.643 on 7/30 to −1.365) — a clean bearish crossover on the gap day.
- MACD line itself crossed below zero on **2026-08-11** (+0.072 → −0.827) and has deepened daily since; the signal line is still marginally positive, so the MACD/signal relationship remains fully bearish.
- **The important nuance:** the histogram bottomed at **−3.634 on 2026-08-05** and has now improved for three consecutive sessions (−3.343 on 8/12 → −3.035 on 8/13 → **−2.648 on 8/14**). Meanwhile price made a marginal *lower* low on 8/12 versus 8/5. Price lower + histogram higher is a **modest, early, unconfirmed positive momentum divergence**. I want to be explicit: one divergence inside an established downtrend is a *watch item*, not a buy signal. It requires a confirming price trigger (see §7).

---

## 5. Volatility & Bollinger structure: compression after expansion

**ATR = 7.861**, which is **2.57% of the close**. The ATR path is very informative: it sat at **8.0–8.3** through mid-July, spiked to **9.872 on 2026-07-31** (the gap day), and has now **declined for ten consecutive sessions** (9.87 → 8.94 → 8.55 → 8.22 → 7.86). Volatility expansion has fully mean-reverted. Practically:
- A 1x-ATR daily range is ~**7.9 points**; a 1.5x-ATR risk unit is **~11.8 points** (~3.9% of price). Any stop tighter than ~1 ATR (≈8 points) inside this chop is at high risk of noise-triggering.
- Falling ATR into a flattening price is classic **coiling** behavior — it usually resolves with a range expansion. Direction is not implied by the coil itself; the trigger levels in §7 define it.

**Bollinger (20,2):** middle **318.43**, upper **344.59**, lower **292.27**.
- Bandwidth = **52.32 / 318.43 ≈ 16.4%** of the mid-band — still very wide because of the late-July blowoff.
- **%B ≈ 0.26** — price at roughly the 26th percentile of the band, i.e. **lower third but not at the lower band**. So there is no "band-touch reversal" signal here; the lower band at **292.27** is intact and *untested*.
- The mid-band is **falling** (324.37 on 7/31 → 318.43 on 8/14) and sits **−3.93% above** the current close. It is the natural magnet/ceiling on any rally, and it lines up reasonably well with the 8/6–8/7 supply zone around 313–316.
- The upper band at 344.59 essentially marks the July high (344.57 intraday high on 7/29) — a striking coincidence that reinforces that price was a 2-sigma outlier at the top.

---

## 6. Volume & participation: the bounces are unconvincing

**VWMA (volume-weighted 20-day) = 314.113.** Price is **−2.61% below** it. This is a genuinely important tell: the *average volume-weighted buyer* over the last month is underwater. That is distribution, and it explains why every rally into 308–313 has met sellers — those buyers are getting back to even.

Volume profile of the correction:
- **132.5M** on the 7/31 break (the highest since the 261.8M rebalance-type print on **2026-06-26**).
- Post-break bounce volume: 75.05M → 68.00M → 49.44M → 46.14M → **34.44M** (8/7). Bounces on **decaying** volume.
- Last ten sessions average **≈46.6M**. Friday's **28.23M** is **~39% below that average** and the lightest single session since roughly late March (compare 28.15M on 2026-04-09, 28.48M on 2026-03-25).

Interpretation: **sellers are not panicking and buyers are not committed.** The 8/14 up-close on the lightest volume in four months is a low-conviction drift, not accumulation. Until a session prints meaningfully above ~50–60M in the direction of travel, treat breakouts and breakdowns with suspicion.

---

## 7. Selected indicators and why they fit this regime

1. **close_200_sma (280.48)** — establishes that the primary trend is unbroken; the single most important "don't fight the tape" reference for strategically-long positioning.
2. **close_50_sma (309.19)** — the battleground. It is simultaneously the falling intermediate trend line, the immediate overhead resistance, and now flattening downward. Its resolution defines the trade.
3. **close_10_ema (309.46)** — captures the short-term momentum turn and, at just +0.27 above the 50SMA, flags the **imminent 10/50 cross risk** that a slower average set would miss.
4. **macd (−2.461)** — confirms the intermediate trend has shifted bearish and marks the zero-line break timing (2026-08-11).
5. **macdh (−2.648, three-session contraction)** — the one indicator showing decay in bearish pressure; the earliest objective evidence of a possible momentum turn.
6. **rsi (43.67)** — quantifies that we are correcting **without** oversold extremes, i.e. no capitulation cushion; keeps expectations of a V-bottom honest.
7. **boll / bands (mid 318.43, up 344.59, lo 292.27)** — a full volatility envelope: %B at 0.26 locates price within the range, the mid-band gives a concrete rally target, and the lower band (292.27) gives the untested downside magnet. It also brackets the July top at the upper band.
8. **atr (7.861, 2.57%)** — the risk-management backbone: volatility has fully mean-reverted, so position size and stop distance should be normalized off ~8 points, not the 9.9 seen post-gap.

Deliberately excluded: StochRSI (redundant with RSI), `macds` (fully implied by macd/macdh are the actionable pair), and MFI (ambiguous scale in the verified snapshot).

---

## 8. Actionable playbook

**Bull trigger (needs a confirm):** a daily **close above 309.5** — the 50SMA/10EMA cluster — ideally on **volume >50M**. A close back above both averages would simultaneously (a) neutralize the 10/50 cross, (b) put price above the VWMA regime, and (c) open the first targets:
- **T1: 313.3** (2026-08-07 close) / **316.3** (2026-08-06 high) — the lower edge of the 7/31 gap.
- **T2: 318.4** (Bollinger mid) — natural mean-reversion magnet.
- **T3: 333.4** (2026-07-30 close) — a full gap fill; only realistic if the histogram turns positive and RSI reclaims ~55.

**Bear trigger:** a daily **close below 300.0** (the 2026-07-31 low). That would break the three-session higher-low sequence and confirm the base attempt failed:
- **D1: 292.3** (Bollinger lower band) — first downside magnet.
- **D2: 283.8** (2026-06-26 close) / the June congestion shelf.
- **D3: 280.5** (200SMA) — the primary-trend line in the sand; a close below it flips the strategic bias.

**Risk framing:** with ATR at 7.86, a stop at **1.5× ATR ≈ 11.8 points** is the minimum sane buffer. Long entries near 306 with a stop near 294 (below the Bollinger lower band) size the trade at roughly **2.6% account-at-risk per unit** — cut position size accordingly. Volatility compression argues for *smaller* initial size and adding on confirmation, not pre-positioning into the coil.

**Preferred stance:** **Neutral with a defensive tilt.** The evidence does not support a chase in either direction. Price is below the 50SMA, 10EMA, Bollinger mid and VWMA (four independent bearish votes) with MACD below zero and below signal — but above a rising 200SMA, above the untested Bollinger lower band, with RSI off its lows and a contracting MACD histogram. That is a **"wait for the range to resolve"** configuration, with an explicit bias to add length only on a volume-confirmed 309.5 reclaim.

---

## 9. What would change this view

- **Upgrades:** daily close >309.5 on >50M volume; MACD histogram flipping positive; RSI closing above 50; price reclaiming VWMA (314.11); a golden-cross-style re-steepening of the 10EMA above the 50SMA.
- **Downgrades:** close <300.0; MACD line making a new low while histogram resumes widening negatively; a 10EMA cross below the 50SMA *while* price remains below both; VWMA continuing to fall while price stagnates (persistent distribution).
- **Neutralizing risk to watch:** AAPL's last two major distribution events (the 2026-06-25 −6.1% session on 107.0M volume, closing 275.15) were **V-shaped and recovered to new highs by 7/28**. That precedent warns against assuming the 7/31 break is terminal — but it also means the *real* tell is whether the 300 low gets retested on heavy volume or quietly abandoned.

---

## 10. Summary table

| Item | Verified value (2026-08-14) | Signal / interpretation |
|---|---|---|
| Close | **305.93** (O 306.00 / H 307.49 / L 304.30) | 4th consecutive higher low intraday (300.57 → 302.05 → 304.30) |
| Volume | **28.23M** | ~39% below 10-day avg (~46.6M); weakest in ~4 months — low-conviction drift |
| 10 EMA | **309.459** | Price −1.14% below; falling ~1.1/day; only +0.27 above 50SMA → cross risk |
| 50 SMA | **309.191** | Price −1.05% below; **11 straight closes beneath**; peaked 309.786 on 8/7, now rolling over |
| 200 SMA | **280.484** | Price **+9.07%** above; rising ~+0.22/day → primary uptrend intact |
| 50 vs 200 SMA | spread **+28.71 (+10.2%)** | Wide positive alignment; no death-cross threat remotely near |
| MACD | **−2.461** | Below zero (crossed 8/11) and below signal (0.187) → intermediate trend bearish |
| MACD hist | **−2.648** | Contracting 3 sessions from −3.634 (8/5) → bearish pressure decelerating; early, unconfirmed |
| RSI | **43.672** | Neutral-bearish; recovering from 40.22 (8/12); **never hit 30** even on the −7.35% gap day; top was 71.65 (7/17) |
| Bollinger mid | **318.429** | −3.93% overhead; falling → first real mean-reversion ceiling |
| Bollinger upper | **344.590** | Nearly identical to the 7/29 intraday high (344.57) — confirms top was a 2σ outlier |
| Bollinger lower | **292.267** | Untested; %B ≈ 0.26 (lower third, not at band) |
| Bollinger width | ≈**16.4%** of mid | Wide, but flattening → coiling ahead of range expansion |
| ATR | **7.861 (2.57% of price)** | Down 10 straight sessions from 9.872 (7/31); use ~8 pt unit, 1.5×ATR ≈ 11.8 pt stops |
| VWMA | **314.113** | Price **−2.61%** below → average volume-weighted buyer underwater = distribution |
| Key resistance | **309.2–309.5**, then **313.3 / 316.3**, then **318.4**, then **333.4** | 50SMA/10EMA cluster; Aug supply; Boll mid; unfilled 7/31 gap |
| Key support | **300.0–302.3**, then **292.3**, then **283.8**, then **280.5** | 7/31 low + 8/12 close; Boll lower; June shelf; 200SMA |
| Drawdown context | **−10.04%** from 340.08 (7/28 close); **−12.28%** from 344.57 (7/29 high) | Correction inside uptrend, not a broken primary trend |
| Structural event | **2026-07-31:** 333.43 → 308.91 (**−7.35%**), low 300.00, volume **132.5M** | Unfilled gap 304.81–333.43 = dominant overhead supply |
| **Net bias** | **Neutral / defensive** | Long only on volume-confirmed close >309.5; stand aside or hedge while below 309.2 and above 300 |