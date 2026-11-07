# AMZN — Technical Analysis Report (as of 2026-07-24)

## 1. Bottom Line

**AMZN has lost its medium-term footing and is testing the last major structural support in the 226–235 zone.** The July recovery impulse (off the 2026-06-25 close of 227.01) topped on 2026-07-15/16 at 254.96 close / 258.08 intraday high — a clear **lower high** versus the May peak — and has been unwound in just two sessions: **-4.57% on 2026-07-23 (a -3.51% opening gap down) and -0.66% on 2026-07-24, closing at 232.11.**

Three independent facts define the current condition, all verified from tool output:

1. **Price closed below the 200-day SMA** (234.59) for the second straight session — the first loss of that line since it was reclaimed on 2026-06-29.
2. **Price is pressed against the lower Bollinger Band** (231.85), closing only **$0.26 above it**, after printing a 231.34 intraday low.
3. **MACD issued a fresh bearish crossover *and* lost its zero line on 2026-07-23**, while RSI collapsed from 60.14 (07-15) to **37.49** — the lowest reading since 2026-06-25 (33.63).

Bias: **short-term bearish / corrective**, with the tape at a decision point. The burden of proof has shifted to the bulls: a close back above 234.59 is the *minimum* repair; above 242.4 confirms a failed breakdown.

---

## 2. Verified Snapshot (source of truth)

| Field | 2026-07-24 |
|---|---|
| Open | 234.38 |
| High | 234.95 |
| Low | 231.34 |
| **Close** | **232.11** |
| Volume | 35,017,400 |
| close_10_ema | 242.369738 |
| close_50_sma | 249.223201 |
| close_200_sma | 234.588200 |
| macd / signal / hist | -1.500471 / -0.486117 / -1.014354 |
| rsi | 37.494037 |
| boll (mid) / ub / lb | 243.836 / 255.821742 / 231.850258 |
| atr | 7.222284 |
| vwma | 245.519692 |

*Cross-check:* the `get_indicators` series and the snapshot agree to the decimal for every overlapping value (RSI 37.494037, ATR 7.222284, MACD -1.500471, boll_lb 231.850258 vs 231.8502579). **No discrepancy to flag between tools.** The one item I cannot verify with any available tool is the *cause* of the 2026-07-23 gap — no news/catalyst feed is available, so the event is treated as a price fact only (see §8).

---

## 3. Price-Action Narrative (all levels from the OHLCV series)

**2026 map:** Capitulation low 2026-02-13 close **198.79** (intraday 197.28, after a two-day -9.73% slide from 232.99 on 02-04 to 210.32 on 02-06 on 179.2M shares) → V-shaped recovery → April breakout (04-08 to 04-17, 209.77 → 250.56) → **May peak: close 274.99 on 05-06, intraday high 278.56 on 05-05** (note the 04-30 reversal bar: open 273.17, low 256.16, close 265.06 on 101.0M shares) → two-month slide to the **June low: close 227.01 on 2026-06-25** (intraday 225.55) → 06-26 reconstitution print of **248.4M shares at 232.69** → July rebound to **254.96 close on 07-15 / 258.08 high on 07-16**.

That July rebound is the critical tell: **it failed to exceed the 258.08 prior swing and stalled 16.5% below the May high.** Since 07-16, the sequence has been lower highs (258.08 → 252.89 → 249.34 → 248.45) and then a hard break of the lows:

- 07-22 close 244.85
- 07-23 **gap open 236.26** (vs 244.85 prior close), close **233.66 (-4.57%)** on 47.5M shares
- 07-24 open 234.38, high 234.95, **low 231.34**, close **232.11 (-0.66%)**, i.e. **-5.20% in two sessions**

**Two structural details matter:**

- The 07-24 low of **231.34 took out the 06-22/06-23 lows of 232.24 / 232.00**, breaking the "higher low" sequence that had been in place since late June. The next objective reference is the 06-25/06-26 cluster at **225.55 / 226.13**.
- The 07-24 close at 232.11 sits **$0.77 off the session low in a 3.61-point range (~21% of range)** — a weak close with no intraday reversal signature. There is **no evidence in this data of a support hold or reversal bar yet.**
- **Volume is not climactic.** 07-23's 47.5M is only ~1.13x the ~42.2M average of the other 19 sessions in the last 20 (my arithmetic excludes the 248.4M reconstitution print). By comparison, the February washout ran 179.2M and the 06-26 print 248.4M. **No capitulation read → the 226 support zone remains the plausible downside magnet.** 07-24's 35.0M (below that ~42M average) is a mild deceleration in selling, nothing more.

---

## 4. Selected Indicators (8) and Evidence

I chose a complementary set spanning **trend (3 timeframes), momentum (MACD pair), exhaustion (RSI), volatility envelope (Bollinger lower + ATR)** — deliberately avoiding redundancy (no RSI+StochRSI overlap, no MACD-histogram duplication of the MACD pair, 10-EMA used instead of close_50_sma alone so short-term signals aren't lagged).

**1. close_10_ema = 242.37 — short-term trend down.** Price is **10.26 (-4.23%) below it**, and the EMA itself has now rolled over: 247.60 (07-20) → 247.09 (07-22) → 244.65 (07-23) → 242.37 (07-24). The 10-EMA is falling ~2.3 points/session, so it will chase price lower — treat 242.4 as moving (declining) resistance, coincidentally convergent with the Bollinger mid band (243.84).

**2. close_50_sma = 249.22 — medium-term trend broken.** It has declined uninterrupted from 257.10 (06-18) to 249.22, a **-0.315/session** drift that has steepened to **-0.58/session** over the last five sessions (252.13 on 07-17 → 249.22). Price is **6.87% below it**. Implication: every reflex rally into the 245–250 zone meets a falling 50-SMA headwind.

**3. close_200_sma = 234.59 — the line in the sand.** Slow and still *rising* (+0.09/session: 233.33 on 07-10 → 234.59), yet price has closed beneath it two sessions running (**233.66 on 07-23, 232.11 on 07-24**), after holding above it from 2026-06-29 through 2026-07-22. **A failed retest of a rising 200-SMA is a materially more bearish configuration than a routine dip**, because it invalidates the June–July recovery thesis rather than merely trimming it.

**4–5. macd = -1.500 / macds = -0.486 (hist -1.014) — momentum fully reversed.** The clean lifecycle in the data:
- **07-01:** bullish crossover (MACD -5.061 > signal -5.531)
- **07-15:** MACD crosses zero (+0.260) — impulse confirmed
- **07-20:** MACD peak at +0.824, signal -0.622
- **07-23:** **bearish crossover** (MACD -0.530 < signal -0.233) **and zero-line break in the same session**
- **07-24:** MACD -1.500, histogram -1.014 — the most negative histogram reading since 2026-06-25 (-1.747)

A 15-session impulse erased in two sessions. The histogram's steepening slope is a nowcast of further downside momentum, not a bottoming pattern.

**6. rsi = 37.49 — weak but NOT oversold.** Sequence: 60.14 (07-15) → 51.32 (07-17) → 48.40 (07-22) → 38.62 (07-23) → **37.49**. It is a **two-day collapse with no positive divergence** and still ~7.5 points above the 30 threshold. For reference, the 06-25 print was 33.63, i.e. **RSI has room to fall before reaching even the June oversold extreme.** Do not front-run a bottom on RSI alone.

**7. boll_lb = 231.85 (mid 243.84, upper 255.82) — price riding the lower band.** Close 232.11 is **$0.26 above the band**; the 231.34 intraday low pierced it. Band width is **23.97 points = 9.83% of the mid**. Notably the *mid band is rising* (242.34 on 07-20 → 243.84 on 07-24) while price falls, because the 20-day window is dropping the 06-25 low — meaning price is now **11.73 (-4.8%) below the mean**. Two readings: (a) band-riding in a downtrend is a continuation signal, not a buy signal; (b) a snap-back toward 243.8 is a *5%* move and therefore lower-probability than tagging 226 first.

**8. atr = 7.22 (3.11% of price) — volatility is contained, which is itself informative.** ATR *fell* into the drop (8.59 on 06-29 → 7.09 on 07-22 → 7.22). The two-day -12.74 move equals ~1.76 ATR. **An orderly, gap-driven decline on unremarkable ATR is characteristic of institutional de-risking rather than panic** — historically more likely to extend to the next shelf than to V-bottom instantly. Use ATR for stops: 1.5× = 10.8 pts, 2× = 14.4 pts.

**Supporting (from snapshot, not counted in the eight): vwma 245.52.** Price is **5.46% below the volume-weighted average** — the volume-weighted crowd is underwater. VWMA rose into 07-22 (247.03) then flattened (246.23 → 245.52), i.e. the sellers are now transacting at lower prices than the recent volume-weighted consensus — a distribution footprint confirming the MACD signal.

---

## 5. Levels (derived strictly from tool data)

**Overhead resistance**
| Level | Source |
|---|---|
| 234.59 | 200-SMA (immediate reclaim trigger) |
| 236.00–236.87 | 07-23 gap-fill origin / 06-17 low 236.00 / 06-23 high 236.87 |
| 242.37–243.84 | 10-EMA + Bollinger mid (confluence) |
| 244.85–247.5 | Unfilled gap zone from 07-22 close to 07-23 open; 07-09 close 247.04 |
| 249.22 | Falling 50-SMA |
| 255.82–258.08 | Bollinger upper / 07-16 swing high |

**Downside support**
| Level | Source |
|---|---|
| 231.34–231.85 | 07-24 low + lower Bollinger Band |
| 227.01–225.55 | 06-25 close / 06-25-06-26 low cluster (primary target) |
| ~223 | Measured continuation: 232.11 − 1.25×ATR ≈ 223; also below the June band trough (221.62 on 06-25) |

---

## 6. Actionable Playbook

**Scenario A — Bearish continuation (base case, ~55–60%).**
Trigger: failure to reclaim 234.59 on a closing basis, or a break of 231.34.
Entry: rallies into **236–240** (gap zone) or momentum break below 231.34. Stop: **above 244.85** (invalidation = gap fully filled and prior close reclaimed) ≈ 8.5 pts from a 236.3 entry (~1.2 ATR). Targets: **227.0 → 225.5**, then ~223. Risk/reward at 236.3 entry / 227 target ≈ 1.2:1 — thin; better R/R is the break-of-231.34 version with a 236.0 stop (4.7 pts risk vs 8.8 pts to 225.5 ≈ 1.9:1).

**Scenario B — Failed breakdown / mean reversion (~25%).**
Trigger: a **close above 234.59** *plus* MACD histogram turning up from -1.01 (i.e. MACD rising back toward -0.49) *plus* RSI reclaiming 43–45.
Entry: 234.6–236.0 on the reclaim. Stop: below **231.34** (~3.5 pts, <0.5 ATR — tight, so size accordingly). Targets: **242.4 (10-EMA/mid band) → 249.2 (50-SMA)**. This is the highest-R/R trade on the board if it triggers, because the stop is very near.

**Scenario C — No-trade / wait (do nothing while 231.3–234.6 compresses).** The 3.3-point band between the lower Bollinger Band and the 200-SMA is a coil; ATR 7.22 means daily noise alone can trigger either side. Wait for a close outside the band.

**Risk management (ATR-calibrated):** ATR 7.22 = 3.11% of 232.11. For a 1%-of-equity risk budget, position size = (0.01 × equity) / (2 × 7.22) = **0.069% of equity per $1 of share price**. Halve normal size on any pre-200-SMA-reclaim long; a rising 200-SMA that price has just lost is a whipsaw-prone location.

---

## 7. Nuances and Risks to This View

- **The June precedent cuts both ways.** After the 06-25 close of 227.01 with RSI 33.63, AMZN rallied to 254.96 by 07-15 (+12.3%). That is *observed data*, not a validated signal — and the difference this time is the **failure below the 200-SMA**, which did not occur on the 06-25 low (price was *below* it then too: 227.01 vs 232.80). Be honest about this: both the June low and today's low sit below the 200-SMA, but June's was followed by a reclaim on 06-29; today's has not been reclaimed.
- **Death-cross clock is ticking, but not yet.** 50-SMA (249.22) is still 14.64 above the 200-SMA (234.59), down from 24.50 on 06-18. At the current -0.58/session 50-SMA slope, convergence would take roughly 25 sessions. **This is a late-August event, not a today event** — do not pre-trade it as imminent.
- **Unexplained gap.** The -3.51% 07-23 gap is a price fact; its cause is unverifiable with the tools available. If it was an event (e.g., a guidance/earnings-type catalyst), technical levels are less reliable than usual and the 226 zone may be reached in one move. Treat 07-23's 47.5M volume as *elevated but not exhaustive*.
- **Counter-signal to watch:** declining volume on the second down day (35.0M vs ~42.2M 20-day norm) plus ATR staying flat at 7.22 — if 07-25/07-28 produces an inside day holding above 231.34, the bear case degrades to a range.

---

## 8. Summary Table

| # | Indicator | Value (07-24) | Signal | Interpretation |
|---|---|---|---|---|
| 1 | close_10_ema | 242.37 | Bearish | Price -4.23% below; EMA rolling over (-2.3/day) |
| 2 | close_50_sma | 249.22 | Bearish | -6.87% below; 6-week downtrend, slope steepening to -0.58/day |
| 3 | close_200_sma | 234.59 | **Bearish (new)** | 2nd close below a *rising* 200-SMA; lost the 06-29 reclaim |
| 4 | macd | -1.500 | Bearish | Zero-line lost 07-23; impulse from 07-01 reversed |
| 5 | macds | -0.486 | Bearish | Bearish crossover 07-23; hist -1.01, worst since 06-25 |
| 6 | rsi | 37.49 | Weak, not oversold | Down from 60.14 (07-15); June low was 33.63 |
| 7 | boll_lb | 231.85 | At support | Close only +$0.26 above band; intraday pierced to 231.34 |
| 8 | atr | 7.22 (3.11%) | Neutral/contained | Orderly de-risking, not panic; ATR flat → no capitulation |
| — | vwma (snapshot) | 245.52 | Bearish confirm | -5.46% below; VWMA flattening = distribution |
| — | Volume 07-24 | 35.0M | Mildly constructive | Below ~42.2M 20-day norm; selling decelerating |

| Item | Detail |
|---|---|
| **Ticker** | AMZN |
| **Verdict** | Corrective / bearish bias; at decision point |
| **Key trigger (bull)** | Close > 234.59 (200-SMA) + MACD hist turning up |
| **Key trigger (bear)** | Close < 231.34 (07-24 low / lower band) |
| **Primary downside target** | 227.01 → 225.55 (June low cluster) |
| **Upside repair targets** | 236.0–236.9 gap → 242.4–243.8 (10-EMA/mid) → 249.22 (50-SMA) |
| **Stop framework** | 1.5×ATR = 10.8 pts; 2×ATR = 14.4 pts |
| **Structural warning** | Lower high 258.08 (07-16) vs 278.56 (05-05); higher-low structure broken |
| **Death cross** | ~25 sessions out at current slopes — not imminent |
| **Unverifiable** | Cause of the 07-23 -3.51% opening gap |
| **Data integrity** | `get_indicators` and verified snapshot agree exactly — no discrepancy |