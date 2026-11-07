# AMZN — Technical Deep Dive as of Friday, 2026-09-18

## 1. Verified data baseline

Every price and indicator figure below comes from the frozen OHLCV rows and the verified snapshot for 2026-09-18. **The two sources agree exactly** (close 253.71, 50-SMA 255.8398, 200-SMA 240.30075, 10-EMA 252.9089, MACD −2.0937, signal −1.2348, histogram −0.8590, RSI 48.0426, Bollinger 256.1335 / 265.8819 / 246.3851, ATR 6.0360, VWMA 254.1001) — no reconciliation was required. The snapshot also returns an `mfi` field of 0.4162, which is on a non-standard (0–1) scale; I have **not** used it anywhere in this analysis.

**Latest session (2026-09-18):** Open 252.92 · High 255.43 · Low 251.88 · **Close 253.71** · Volume **52.27M**. Up +1.00% on the day, +0.31% above the open, and closed above the 9/17 high of 252.73.

---

## 2. Regime diagnosis: a high-level uptrend, a mid-level distribution phase, and a short-term volatility squeeze

The chart is best read as **three nested timeframes that currently disagree**, which is why the market is compressed:

| Timeframe | Proxy | Reading |
|---|---|---|
| Long-term (strategic) | 200-SMA 240.30, rising from 236.82 on 8/10 | **Bullish.** Price is +5.58% above it; it has not been tested since February. |
| Medium-term (positional) | 50-SMA 255.84, rising but flattening | **Neutral-to-deteriorating.** Price has closed **below** it for 5 consecutive sessions (9/14–9/18). 50 > 200 by 15.54, so the golden-cross configuration is intact. |
| Short-term (tactical) | 10-EMA 252.91, VWMA 254.10 | **Bearish, but stabilizing.** The 10-EMA has fallen every session from 266.03 (8/10) to 252.91, but ticked *up* on 9/18 for the first time in weeks (252.73 → 252.91). |

The dominant event in the dataset is the **earnings-style gap on 2026-07-30/31**: close 235.50 (7/30) → open 265.00 and close 271.58 (7/31) on 129.05M shares, followed by a peak close of **284.02 on 8/3 (intraday high 287.20)**. Since that high, AMZN has carved a textbook sequence of **lower highs and lower lows**:

- Highs: 287.20 (8/3) → 282.79 (8/5) → 280.14 (8/10) → 266.40 (8/19) → 267.56 (8/28) → 261.12 (9/4) → 257.59 (9/11) → 255.95 (9/14) → **255.43 (9/18)**
- Lows: 257.73 (8/18) → 255.02 (8/27) → 251.93 (9/1) → 249.58 (9/10) → **244.30 (9/16)**

From the 8/3 close of 284.02 to the 9/16 close of 245.96 the stock lost **13.4%**; from 284.02 to the current 253.71 it is **−10.7%**. The 9/16 close of 245.96 was the lowest close since 7/29 (226.65).

**Critically, the decline has been orderly, not climactic.** Average volume across the 7/30–8/3 advance was roughly 107M/day (101.8M, 129.1M, 90.8M). Average volume across the pullback is roughly one-third of that (the 20-session average through 9/18 is ≈32.9M). Distribution, yes — but controlled profit-taking rather than liquidation. That distinction matters for which side of the squeeze you should favor.

---

## 3. Trend indicators — what each one is actually saying

**50-SMA (255.84).** This is *the* level in play. Price has closed beneath it five sessions running, yet the average itself is still creeping higher: 252.41 (9/1) → 254.43 (9/8) → 255.25 (9/11) → 255.56 (9/15) → 255.56 (9/16) → 255.71 (9/17) → 255.84 (9/18). The slope has decelerated to roughly +0.04%/day — the 50 is **flattening into price**, which is precisely how a trend matures. A reclaim of 255.84–256.13 (Bollinger basis) would neutralize the pullback; another week of closes below it will bend the average over.

**200-SMA (240.30).** Unambiguously constructive: +1.47% over the last 28 sessions, ~+0.05%/day, and the 50/200 spread has actually *widened* from 10.77 (8/10) to 15.54 (9/18). No death-cross risk is remotely close — the 50 would need to fall ~6% relative to the 200. The 200-SMA is the natural "line in the sand" for the long-term thesis and coincides with the bottom of the 7/31 gap (239.82).

**10-EMA (252.91).** Price (253.71) has reclaimed it by 0.80 points — a one-day event, not a trend. But it is the first time since late August that price has closed above the 10-EMA after being below it, and the EMA itself turning up (+0.18) is an early tell that the two-day bounce has real short-term force.

**VWMA (254.10).** The most underrated signal on this chart. AMZN has closed **below its volume-weighted average price for 25 consecutive sessions (since 8/14)**, and the VWMA has declined monotonically from 272.05 (8/20) to 254.10. That means the volume-weighted marginal buyer is underwater and every rally has been sold into. Price is now only 0.39 (−0.15%) below it — the closest it has been in that entire stretch. **Reclaiming 254.10 on volume would be the first objective evidence that the distribution phase is ending.** Failing there keeps the sellers in control.

---

## 4. Momentum — improvement, but no confirmed reversal

**MACD (−2.0937) vs Signal (−1.2348).** The bearish crossover occurred on 8/17 (MACD 5.830 vs signal 6.140) and the MACD line crossed **below zero on 9/9** (0.118 → −0.421), which downgraded the trend from "consolidation" to "corrective." The line bottomed at −2.2863 on 9/17 and ticked up to −2.0937 on 9/18. The signal line, however, is still falling (−1.0200 → −1.2348). **There is no bullish crossover yet, and claiming one would be premature.**

**Histogram (−0.8590).** This is the most encouraging datapoint on the board. The histogram has been negative for **24 consecutive sessions** (since 8/17), bottoming at −1.5387 on 9/16 and improving for three straight sessions: −1.5387 → −1.2662 → −0.8590. That is a ~0.68 improvement in two days — bearish momentum is decaying at an accelerating rate. At this pace, a MACD/signal crossover is roughly **2–4 sessions away** *if* price holds above ~251.5. A roll back under 249 would likely abort it.

**RSI (48.04).** From 65.87 on 8/10 to a trough of **39.45 on 9/16**, then 45.39 (9/17) and 48.04 (9/18) — an 8.6-point two-session recovery. That is a sharp reflex bounce with plenty of headroom before overbought (70). Note the caution: RSI at the 9/16 low (39.45) was a *lower* low than at the 9/10 low (43.62) while price also made a lower low — **no bullish divergence was generated**. Likewise the MACD histogram made a lower low on 9/16 (−1.5387) than on 9/10 (−1.4286). So the 9/18 rally is a momentum *stabilization*, not a divergence-confirmed bottom. That argues for scaling, not for a full-size entry.

---

## 5. Volatility — a genuine Bollinger squeeze at the low end of its range

This is the defining feature of the current setup:

| Measure | 2026-08-10 | 2026-08-27 | 2026-09-18 |
|---|---|---|---|
| Bollinger upper | 290.69 | 282.61 | **265.88** |
| Bollinger basis (20-SMA) | 253.13 | 267.14 | **256.13** |
| Bollinger lower | 215.57 | 251.68 | **246.39** |
| Band width ($) | 75.13 | 30.93 | **19.50** |
| Band width (% of basis) | 29.7% | 11.6% | **7.61%** |
| ATR (14) | 9.13 | 6.71 | **6.04** |

Band width has compressed **74% from the 8/10 peak**, and ATR has fallen every week to 6.04 — its lowest reading in the entire 40-session lookback, and equal to just **2.38% of price** (versus 3.5% on 8/10). This is a coiled spring. Two mechanical implications:

1. **Mean-reversion trades now have a poor payoff.** Bands this tight get "ridden," not faded, when they resolve.
2. **The resolution will likely be large.** A squeeze of this magnitude typically produces a move of 1.5–2.5 ATR (9–15 points, i.e. ±3.5% to ±6%) within 2–4 weeks. The 7/30–7/31 earnings gap (~14% in two sessions) is a reminder that this name resolves violently around catalysts.

Price sits at **37.6% of band width** (above the lower band, below the basis) — the lower half, consistent with the short-term downtrend, but no longer pinned to the lower band as it was on 9/16.

---

## 6. Volume — the day's most important new information

The 9/18 session printed **52.27M shares**, which is:
- **+71.7%** versus 9/17 (30.44M),
- **1.59×** the ~32.9M 20-session average,
- the **highest volume since 8/4** (69.75M) — i.e., the heaviest tape in six weeks.

And it came on an **up day** (+1.00%, close above the prior day's high, close in the upper half of the range at 51.5% of H/L). That is the first volume-expansion-up-day since the 8/3 peak, and it is the kind of "effort vs. result" signature that precedes trend resolution. **However**, one session is not confirmation, and price still finished below the 50-SMA, the VWMA and the Bollinger basis — all three clustered within 2.4 points (254.10, 255.84, 256.13). The market has delivered the *attempt*; it has not yet delivered the *result*.

---

## 7. Level map (all values arithmetic from tool output — no unverified historical claims)

**Resistance stack (tight, and the whole near-term battle):**
- **254.10** — VWMA (falling daily; first hurdle)
- **255.43** — 9/18 intraday high
- **255.84** — 50-SMA
- **256.13** — Bollinger basis
- **257.59** — 9/11 high (breaking it ends the sequence of lower highs)
- **261.12** — 9/4 high
- **265.88** — Bollinger upper band

**Support stack:**
- **251.88** — 9/18 low
- **249.24** — 9/17 low (also ≈ the 61.8% retrace of the 7/29 low 226.16 → 8/3 high 287.20, at 249.47)
- **246.39** — Bollinger lower band
- **244.30** — 9/16 low, the swing low of this correction
- **240.30** — 200-SMA
- **239.82** — the 7/30 high, i.e. the bottom edge of the unfilled 7/31 gap (gap floor)
- **235.50** — 7/30 close

Two independent retracement frameworks cluster usefully: the 226.16 → 287.20 swing puts the 50% retrace at **256.68** (right at the 50-SMA/Bollinger basis) and the 61.8% at **249.47** (right at the 9/17 low). The 239.82–262.01 earnings gap remains unfilled; price has traded down *into* it (9/16 low 244.30) but never closed it.

---

## 8. Actionable scenarios

**Base case — squeeze resolves upward, but only on a confirmed trigger (probability-weighted highest, ~45%).**
Requirements: a daily close **above 256.5** (50-SMA + Bollinger basis) with volume **≥ 40M** (≈1.2× the 20-day average), ideally following through above **257.59** (9/11 high). That would flip price above all three of the 10-EMA, VWMA and 50-SMA, turn the MACD histogram positive, and target **261.12** then **265.88** (upper band).
- Entry: 256.5–257.5 on the confirming close (or on the first pullback that holds 254.1).
- Stop: **249.20**, just under the 9/17 low → risk ≈7.3 points (2.8%), about 1.2 ATR.
- First target 261.12 (+1.7%), second 265.88 (+3.6%). Blended R:R ≈1.2:1 to 1.6:1 — **adequate but not exceptional**, which is why the confirmation filter matters. A tighter stop at 251.80 (9/18 low) gives ≈2.0:1 but invites ATR-driven noise-outs.

**Bear case — squeeze breaks down (~35%).**
A daily close **below 246.39** (Bollinger lower) on expanding volume, especially if 244.30 is taken out, opens **240.30 (200-SMA)** and a gap-fill toward **239.82**. That is a 2.7–2.9% move — roughly 1.0–1.1 ATR — so the target is modest relative to the stop.
- Entry: close < 246.39.
- Stop: **251.90** (above the 9/18 low) → risk ≈5.5 points (2.2%).
- Target: 240.3–239.8 (+2.7%). R:R ≈1.2:1.
- Note the asymmetry: the *path* to 240 is only ~2.7% but the 200-SMA is rising, so shorting into it is shorting into support. Prefer tactical shorts only, with the 200-SMA as a take-profit rather than a hold.

**Range case — chop between 246.4 and 256.1 (~20%).** With ATR at 6.04, expect ±6-point daily noise. In this state, fading the extremes and doing nothing in the middle is the correct play; do not chase 9/18's bounce at 253.71, which sits almost exactly mid-band (37.6% of width) with no edge.

**What to avoid:** Buying the current 253.71 mid-range print. Price is below the 50-SMA, below the VWMA, below the Bollinger basis, with a rising but decelerating 50-SMA and no MACD crossover. The bounce is real, but it is a *recovery within* a five-week distribution channel, not a breakout. The edge lies in waiting for 256.5+ with volume, or for a flush into 244–240.

**Risk sizing with ATR 6.04:** a 2×ATR stop is ~12.1 points (4.8% of price). Size positions so that a 4.8% adverse move equals your per-trade risk budget; de-risk into the next scheduled catalyst, given the 7/31 gap behaviour.

---

## 9. Why these eight indicators were chosen

The setup is a **pullback inside a primary uptrend that has compressed into a volatility squeeze**, so the indicator set must span four independent dimensions without duplication:

1. **close_200_sma** — defines whether the primary trend is intact (it is) and where the strategic invalidation lies (240.30).
2. **close_50_sma** — the actual battleground; identifies the medium-term pivot at 255.84 and its decelerating slope.
3. **close_10_ema** — captures the short-term turn (price reclaimed it 9/18 for the first time in weeks) without lagging like the 50.
4. **macd** — distinguishes "consolidation" from "corrective trend" via the zero-line cross on 9/9 and the pending signal crossover.
5. **rsi** — quantifies the 39.45 → 48.04 oversold recovery and confirms **no** divergence was formed, which prevents overstating the bounce.
6. **Bollinger set (boll / boll_ub / boll_lb)** — the single most informative signal right now: 7.61% band width, down 74% from 8/10, i.e. a directional resolution is near.
7. **atr** — the lowest reading in the window (6.04) simultaneously confirms the squeeze and provides the only rational basis for stop placement and position sizing.
8. **vwma** — the non-redundant volume check: 25 consecutive closes below a monotonically falling VWMA is direct evidence of distribution, and 254.10 is now the nearest trigger for a regime change.

Deliberately excluded: **MACD signal line** (fully implied by MACD/histogram), **Bollinger basis as a separate 20-SMA** (already captured inside the band complex), and **MFI** (the vendor's 0.4162 value is on an incompatible scale and would be a fabricated read at face value).

---

## 10. Key points summary

| Dimension | Reading (2026-09-18) | Interpretation | Actionable level |
|---|---|---|---|
| Price | 253.71 (+1.00%) | Two-session rebound from 245.96; still −10.7% from 8/3 peak 284.02 | — |
| Long-term trend | 200-SMA 240.30, rising (+1.47% over 28 sessions) | Primary uptrend intact; price +5.58% above | 240.30 = strategic invalidation |
| Medium-term trend | 50-SMA 255.84, flattening; price −0.83% below, 5 closes below | Pullback, not yet breakdown; 50>200 by 15.54 | Reclaim 255.84/256.13 |
| Short-term trend | 10-EMA 252.91, turned up +0.18 on 9/18 | First confirmed short-term improvement | Holds above 251.88 |
| Momentum | MACD −2.094 vs signal −1.235; below zero since 9/9 | Bearish regime, no crossover yet | Close > 251.5 keeps crossover alive |
| Momentum thrust | Histogram −0.859, three straight improvements from −1.539 | Bearish momentum decaying fast | Turn positive ≈ 2–4 sessions |
| Momentum breadth | RSI 48.04, from 39.45 low; no bullish divergence | Neutral, room to 70; bounce unconfirmed | >55 = bullish confirmation |
| Volatility | Boll width 19.50 (7.61% of basis), −74% from 8/10; ATR 6.04 (lowest in window, 2.38% of price) | **Squeeze — expect a ±3.5–6% resolution** | Break 246.39 / 265.88 |
| Volume | 52.27M = 1.59× 20-day avg; highest since 8/4, on an up day | First accumulation attempt in six weeks | ≥40M on a close >256.5 |
| Volume trend | VWMA 254.10 falling daily; 25 straight closes below it | Seller-controlled; nearest upside trigger | Reclaim 254.10 |
| Near resistance | 254.10 / 255.43 / 255.84 / 256.13 / 257.59 / 261.12 / 265.88 | Tight 4-point cluster caps the bounce | Break 257.59 = trend change |
| Near support | 251.88 / 249.24 / 246.39 / 244.30 / 240.30 / 239.82 | 244.30–246.39 is the critical shelf | Break 244.30 = gap-fill risk |
| Bull trigger | Daily close >256.5 on ≥40M volume | Flips above 50-SMA, VWMA, basis | Target 261.12 → 265.88; stop 249.20 |
| Bear trigger | Daily close <246.39 on expanding volume | Squeeze breaks lower | Target 240.30 → 239.82; stop 251.90 |
| Risk sizing | ATR 6.04 = 2.38% of price; 2×ATR stop ≈ 4.8% | Size for 4.8% adverse; de-risk into catalysts | — |
| Verdict | **Neutral / no-trade at mid-range** | Bullish long-term structure + short-term stabilization, but confirmation absent | Wait for 256.5+ or 246.4− |