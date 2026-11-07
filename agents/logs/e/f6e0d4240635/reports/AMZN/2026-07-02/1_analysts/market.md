# AMZN — Technical Deep-Dive Report (as of 2026-07-02)

## 1. Market Context & Why These 8 Indicators

AMZN is currently navigating a **short-term rebound nested inside a medium-term corrective downtrend, with the long-term uptrend still intact.** After topping near $278 in early May, the stock slid to an intraday low of **$225.55 on 2026-06-25**, then bounced ~6.9% over the last five sessions to close at **$242.67 on 2026-07-02**. This "bounce-in-a-pullback" structure requires indicators that separate *trend* (where are we relative to longer anchors?) from *momentum* (is the bounce real or a dead-cat?) and *volatility/risk* (how big should stops be?).

The 8 complementary indicators chosen—deliberately avoiding redundancy:

| Indicator | Value (07-02) | Role in this setup |
|---|---|---|
| **close_50_sma** | 255.42 | Medium-term trend resistance — price sits ~5% below it; defines the correction |
| **close_200_sma** | 232.98 | Long-term trend line — price ~4% above; the line that has defined the bounce floor |
| **close_10_ema** | 239.07 | Short-term momentum — price ~1.5% above; confirms the bounce is live |
| **macd** (line/signal/hist) | -4.39 / -5.30 / **+0.92** | Momentum regime shift — histogram just turned positive (bullish crossover) |
| **rsi** | 48.70 | Overbought/oversold — recovered from ~33.6 on 06-25 to neutral; not yet confirming bullish |
| **boll** (mid/ub/lb) | 240.25 / 252.65 / 227.84 | Mean-reversion & volatility envelope — price atop the mid-band, recent low tagged the lower band |
| **atr** | 8.21 | Volatility sizing — ~3.4% of price; sets realistic stop distances |
| **vwma** | 236.81 | Volume-weighted confirmation — price above it, but only modestly; warns rebound is on light volume |

I excluded `macds`/`macdh` as standalone picks (their signal is captured via the MACD line's crossover reading), and skipped `stochrsi`/`mfi` to avoid overlapping momentum/oscillator redundancy. Trend is triangulated by three structurally different averages (10 EMA, 50 SMA, 200 SMA), which is intentional.

---

## 2. Trend Analysis

**Long-term (200 SMA = 232.98): INTACT BULLISH.** Price at 242.67 sits ~$9.7 (~4.2%) above the 200 SMA, which is *rising* (from 230.77 on 05-26 to 232.98 today). Notably, the **June 25 sell-off pierced this line intraday (low 225.55) and closed below it (227.01) but was immediately reclaimed** the following sessions — a constructive sign that the long-term trend line is acting as support on a closing basis. The 50 SMA (255.42) remains above the 200 SMA, so the **golden-cross configuration is technically still in place**, but the 50 SMA has rolled over (peaked ~257.1 on 06-18, now 255.42) while the 200 SMA creeps up — the gap is narrowing and worth monitoring for a potential future cross.

**Medium-term (50 SMA = 255.42): BEARISH / CORRECTION.** Price is ~5% *below* the 50 SMA, and the 50 SMA itself is now sloping *down* after flattening in mid-June. This is the cleanest evidence that the May→June decline is a genuine medium-term down-leg, not noise. The 50 SMA (~255) is the key overhead hurdle the bulls must reclaim to negate the correction.

**Short-term (10 EMA = 239.07): BULLISH TURN.** The 10 EMA bottomed at ~236.70 on 06-26 and has turned up for four straight sessions; price is ~1.5% above it. This is textbook short-term momentum re-acceleration off the low.

**Structure of the move:** The decline ran from a 05-05 intraday high of **278.56** to the 06-25 low of **225.55** — an ~19% drawdown. The bounce from 227.01 (06-25 close) to 242.67 is **+6.9% in five sessions**, but notably the strongest volume day (06-26, **248.4M shares**) coincided with the low and likely reflects Russell/index reconstitution flows rather than pure directional conviction.

---

## 3. Momentum Analysis

**MACD — the most actionable signal right now.** The MACD line bottomed at **-6.88 on 06-26** and has climbed for four consecutive sessions to **-4.39**. More importantly, the **histogram has flipped positive (+0.92)**, meaning the MACD line has crossed *above* its signal line — a fresh bullish crossover. *Caveat:* the MACD line remains **below zero**, so this is a "momentum improving within a still-negative regime" read — an early-warning reversal signal, not a confirmed trend flip. A push of the MACD line above zero (~$246+ would likely do it) would be the stronger confirmation.

**RSI — recovering but unconfirmed.** RSI bottomed at **32.46 (06-10)** and again tagged **33.63 (06-25)**, then rallied to **48.70** — a clean recovery that crossed the 40 line on 06-29. It is *just* below the 50 midline, meaning momentum is neutralizing but has **not yet flipped bullish**. There is no bearish divergence visible in this window. Getting RSI above 50 would corroborate the MACD crossover.

**The two momentum gauges agree:** the worst of the selling is behind, but confirmation (RSI > 50, MACD > 0) is still pending. This argues for treating the current move as a **tradable bounce with a bullish tilt, conditional on follow-through** — not yet a full trend reversal.

---

## 4. Volatility & Mean-Reversion

**Bollinger Bands (mid 240.25 / upper 252.65 / lower 227.84):** Price closed at **242.67, just above the mid-band (240.25)** — the classic mean-reversion achievement after the June sell-off. The 06-25 low (225.55) tagged/pierced the lower band (then ~227.8), a textbook oversold extreme from which the bounce launched. Band width is ~10.3% of the mid-band — moderately wide, reflecting the elevated volatility of the June decline. Upside band resistance aligns closely with the 50 SMA zone (~252–255), reinforcing that ceiling. **Watch the mid-band at 240.25 as the pivot:** holding above it favors continuation toward the upper band; losing it reopens the lower-band test.

**ATR = 8.21 (~3.4% of price):** Daily range is elevated versus the ~6.7 ATR in late May. For swing risk management, a 1.5×ATR stop is ~$12.3 and a 2×ATR stop is ~$16.4 — meaning any stop placed tighter than roughly one ATR (~$8) is likely to be whipsawed. Position sizing should be scaled down to account for the wider-than-normal range.

---

## 5. Volume Confirmation

**VWMA = 236.81 vs. price 242.67:** Price is ~2.5% above the volume-weighted average — a mild bullish confirmation, but the VWMA itself is only *just* flattening (236.70 on 06-26 → 236.81 on 07-02) after a long slide. That flatness tells us the **rebound has not been accompanied by heavy accumulation** — much of the recent volume is concentrated in the 06-26 reconstitution spike (248.4M) rather than steady buying. Recent up-days (06-29: +3.2% on 77.6M; 07-01–07-02) are carrying average-to-below volumes (48–66M). **This is the main caution flag: the bounce lacks volume conviction so far.**

---

## 6. Key Levels & Actionable Framework

**Resistance (overhead):**
- **$246.7–250** — immediate: 07-02 high (246.72) and 06-29 swing high (249.71); the price this rebound must clear.
- **$252.65** — Bollinger upper band.
- **$255.42** — 50 SMA (the medium-term trend gate; reclaiming it flips the medium-term bias).

**Support (below):**
- **$240.25** — Bollinger mid-band (immediate pivot).
- **$239.07** — 10 EMA (short-term trend).
- **$236.81** — VWMA (volume-weighted floor).
- **$232.98** — 200 SMA (major long-term support / the line defended on 06-25).
- **$227.84 / $225.55** — Bollinger lower band and the 06-25 swing low (last-resort support).

**Scenarios:**
- **Bullish continuation (base case for a bounce trader):** Hold above 240.25 mid-band → MACD >0 and RSI >50 → target 246–250, then 252.65/255.42. Confirmation = a close above the 50 SMA.
- **Neutral/consolidation:** Chop between the mid-band (240) and the 10 EMA/VWMA (237–239) as the oversold bounce digests.
- **Failure back into downtrend:** A close back below ~237 (10 EMA/VWMA cluster) would negate the short-term turn and re-target the 200 SMA (233) and ultimately the 227.8/225.55 low.

**Risk-management note:** With ATR at 8.21, a long entry near the mid-band should use a stop below the 200 SMA (~$232) — roughly 1.1–1.3× ATR — to avoid being stopped by normal noise while respecting the structural support. Reward-to-risk toward the 50 SMA (~255) is attractive *if* the mid-band holds, but the weak volume argues for smaller size and waiting for the RSI/MACD confirmation rather than chasing the first day.

---

## 7. Data Integrity Note

The verified market snapshot (2026-07-02) and the raw OHLCV series are **fully consistent** — the snapshot's latest row (close 242.67, high 246.72, low 241.08, volume 48.25M) matches the price data, and all indicator values I analyzed from `get_indicators` match the snapshot (50 SMA 255.42, 200 SMA 232.98, 10 EMA 239.07, MACD -4.39, signal -5.30, hist +0.92, RSI 48.70, Boll mid 240.25/ub 252.65/lb 227.84, ATR 8.21, VWMA 236.81). No discrepancies found. (I disregarded the snapshot's MFI field of 0.64 as it appears normalized/unrelated and it was not part of my selected set.)

---

## 8. Summary Table

| Dimension | Reading | Signal | Level to Watch |
|---|---|---|---|
| **Long-term trend (200 SMA)** | 232.98, rising; price +4.2% above | ✅ Bullish (intact) | Hold >233 |
| **Medium-term trend (50 SMA)** | 255.42, rolling down; price −5% below | ❌ Correction | Reclaim >255 to flip |
| **Short-term trend (10 EMA)** | 239.07, turning up; price +1.5% above | ✅ Bullish turn | Hold >239 |
| **MACD** | Line −4.39, hist **+0.92 (bull cross)** | ⚠️ Improving / early bullish | Line >0 above ~$246 |
| **RSI** | 48.70, recovering from 33.6 low | ⚠️ Neutral, unconfirmed | >50 = bullish confirm |
| **Bollinger** | Price 242.67 atop mid 240.25; low tagged lb 227.8 | ⚠️ Mean-reversion bounce | Pivot 240.25; cap 252.65 |
| **ATR (volatility)** | 8.21 (~3.4% of price) | Range elevated | 1.5×ATR stop ≈ $12 |
| **VWMA** | 236.81, mildly below price, flat | ⚠️ Weak volume confirm | Floor ~236.8 |
| **Overall bias** | Bounce within a medium-term pullback; long-term uptrend intact | **Cautious-bullish short-term** | Confirm on RSI>50 + MACD>0 |

**Bottom line:** AMZN (2026-07-02, $242.67) is executing a legitimate short-term rebound off the June 25 low, with the MACD histogram turning positive, RSI recovering, and the price reclaiming the Bollinger mid-band — all while the long-term 200 SMA uptrend holds. But it remains **below the falling 50 SMA**, momentum is **still sub-zero/sub-50**, and volume conviction is **light**. Treat this as a tradable bounce with defined resistance at 246–250 and 252.65–255.42, protected by support at 240 / 236.8 / 233, and demand confirmation (RSI > 50, MACD > 0) before upgrading to a full trend-reversal call.