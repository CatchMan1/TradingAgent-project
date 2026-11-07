# AMZN — Technical Analysis & Trade Framework
**As of the verified session close: 2026-08-27**

---

## 1. Data Anchor (source of truth)

All exact price/indicator claims below come from the `get_verified_market_snapshot` call for 2026-08-27. I cross-checked it against the raw OHLCV series from `get_stock_data` for 2025-11-01 → 2026-08-27 and found **no discrepancies** — the 08-27 row (O 259.23 / H 259.66 / L 255.02 / C 256.26 / V 35,927,800) matches exactly in both sources.

| Indicator (2026-08-27) | Value | Read |
|---|---|---|
| Close | **256.26** | Below 10 EMA, VWMA, Bollinger mid |
| 10 EMA | 260.93 | Price **−1.79%** below |
| 50 SMA | 251.08 | Price **+2.06%** above; **rising** |
| 200 SMA | 238.59 | Price **+7.41%** above; **rising** |
| MACD | +1.796 | Positive but decaying fast |
| MACD Signal | +3.479 | **MACD below signal → bearish cross** |
| MACD Hist | −1.683 | Negative for 8th consecutive session |
| RSI | 47.23 | Neutral, no oversold cushion |
| Bollinger Mid (20 SMA) | 267.14 | −4.07% above price |
| Bollinger Upper | 282.61 | Overhead band cap |
| Bollinger Lower | 251.68 | Confluent with 50 SMA |
| ATR(14) | 6.709 | 2.62% of price; compressing |
| VWMA | 264.11 | Price **−2.97%** below → volume-weighted cost basis is overhead |

---

## 2. Why These 8 Indicators (and nothing redundant)

The dominant condition right now is **not** a clean trend, and **not** a clean range — it is a **post-event gap digestion** inside a longer-term uptrend. That demands three orthogonal kinds of information: (a) trend structure at multiple horizons, (b) momentum direction and *rate of change*, (c) volatility/volume context for risk placement.

| # | Indicator | Specific job in *this* context |
|---|---|---|
| 1 | `close_10_ema` | The immediate pullback leg — AMZN has closed below it since mid-August; it defines the first hurdle a bounce must clear. |
| 2 | `close_50_sma` | The medium-term line that just **turned up** (bottomed at 246.38 on 07-30) — the natural "buy-the-dip" reference. |
| 3 | `close_200_sma` | Confirms the multi-quarter primary uptrend is unbroken after the July washout. |
| 4 | `macd` | Momentum **level** — still positive, so this is a cooling, not a reversal… yet. |
| 5 | `macds` | Signal line gives the exact **crossover date** (2026-08-17) and the crossover's aging. |
| 6 | `rsi` | Independent (non-EMA) momentum oscillator with 0–100 bounds; tells us there is **room to fall** before oversold. |
| 7 | `atr` | Position sizing and stop distance — critical because the 07-30/07-31 gap roughly **doubled** the true range regime. |
| 8 | `vwma` | Volume-weighted truth: separates *distribution* from *digestion* and gives an overhead cost-basis level. |

I deliberately did **not** duplicate: no `boll_ub`/`boll_lb` calls (the snapshot supplies them and they conflate with RSI/ATR), no `macdh` (mathematically implied by MACD minus signal — shown in the snapshot), and no second oscillator (e.g., stochastic RSI) since it would restate `rsi`.

---

## 3. Structure: A Bullish Skeleton With a Softening Shell

**Primary trend (200 SMA, rising):** The 200 SMA has climbed monotonically through the entire window — 232.82 on 2026-06-29 to 238.59 on 2026-08-27 (+5.77 points, ~+2.5% over two months). Price at 256.26 sits 7.41% above it. The **golden-cross posture is intact**: 50 SMA (251.08) > 200 SMA (238.59), a +12.49 spread that has actually *re-widened* from 11.63 on 07-30 after compressing through July.

**Medium trend (50 SMA, turning up):** The 50 SMA declined every session from 255.94 (06-29) to a trough of **246.384 on 2026-07-30**, then reversed and has now risen for 20 straight sessions to 251.08. A turning 50 SMA beneath price is a meaningful medium-term positive that a lot of short-term bearish signals are currently arguing against.

**Short trend (10 EMA, rolling over):** The 10 EMA peaked at **267.183 on 2026-08-12** and has stepped down every session since → 260.929. Price has been below it since 08-13 and is now 1.79% beneath. This is the clearest evidence of an intact, orderly short-term downtrend.

**Swing structure (higher lows, higher highs):** Using intraday extremes from the data:
- Lows: **199.14 (2026-03-27) → 225.55 (2026-06-25) → 226.16 (2026-07-29)** — higher lows, though the last two are only marginally separated (0.61 pts), i.e. the floor is effectively flat at ~225–226.
- Highs: 264.50 (2026-04-24) → 278.56 (2026-05-05) → **287.20 (2026-08-03)** — a clean sequence of higher highs.

Conclusion: **constructive on the strategic horizon, corrective on the tactical horizon.** These are not contradictory; they are the normal signature of a pullback within an uptrend — but the pullback is not yet finished.

---

## 4. The Anatomy of the Post-Earnings Gap (the core story)

This is the single most important episode to understand, because it defines every level that matters:

| Date | Close | Volume | Note |
|---|---|---|---|
| 2026-07-29 | 226.65 | 44.96M | Pre-event low close area |
| 2026-07-30 | 235.50 | 101.84M | First impulse; H 239.82 |
| 2026-07-31 | **271.58** | **129.05M** | Opened **265.00** vs prior close 235.50 → a **~29.50 point (≈12.5%) true gap** |
| 2026-08-03 | **284.02** | 90.83M | Peak close; intraday H **287.20** |
| 2026-08-27 | 256.26 | 35.93M | Inside the gap, −9.77% from peak close |

Facts derived arithmetically from these verified closes:
- The impulse from 226.65 → 284.02 = **+25.3% in three sessions**.
- The 07-30-close-to-07-31-open gap of **235.50 → 265.00** remains **unfilled**, and price at 256.26 is trading *inside* it. That makes the gap, not the moving averages, the operative container.
- Retracement arithmetic on that impulse (226.65 → 284.02, range 57.37): **38.2% = 262.10**, **50% = 255.34**, **61.8% = 248.57**. Price at 256.26 is effectively sitting **on the 50% retracement**, with the 38.2% level (262) acting as the level bulls must reclaim.
- The 61.8% level at 248.57 lands almost exactly on the **50 SMA (251.08) / Bollinger lower band (251.68)** cluster → a genuinely meaningful confluence band at **~248.5–252**.

Note the symmetry with February: 2026-02-05 → 2026-02-06 took AMZN from 232.99 to 210.32 (**−9.73% in two sessions**, on 103.5M then 179.2M volume), and the stock then spent March building a base at 199–217. The lesson the data supports: this name gaps violently on catalysts, then **takes 6–10 weeks to rebuild a base**. We are only 18 sessions past the August event.

---

## 5. Momentum: Deteriorating, But Not Broken

**MACD** is the most instructive series here. It bottomed at −6.203 on 2026-06-29, crossed above signal on **2026-07-31** (MACD −0.623 vs signal −1.836), peaked at **8.432 on 2026-08-11**, and has fallen every session since to **1.796**. The bearish crossover occurred on **2026-08-17** (MACD 5.830 vs signal 6.140 → hist −0.310). The histogram has been negative and *widening* (now −1.683) for 8 sessions.

Quantify the decay: MACD losses over the last four sessions were −0.302, −0.371, −0.371, −0.639. At roughly −0.30 to −0.45 per session, the MACD line reaches the **zero line in ~3–5 sessions (≈ 2026-09-01 to 2026-09-03)**. A zero-line cross is the meaningful regime marker: it would say momentum has fully round-tripped the earnings impulse, and it is the single most important near-term technical event to watch.

**RSI** at 47.23 confirms the same message without the EMA smoothing. It peaked at **72.23 on 2026-08-03** (genuine overbought), printed 65.87 on 08-10, then stair-stepped down: 57.06 (08-12) → 53.49 (08-14) → 50.93 (08-18) → 47.23 now. Key nuances:
- There is **no bullish RSI divergence**: RSI made lower highs alongside lower price highs on 08-03 → 08-10, so the fade is *confirmed* momentum, not exhausted momentum.
- 47.23 is mid-range — **neither overbought nor oversold**. There is roughly 17 points of downside before a 30 reading, meaning the oscillator provides **no downside cushion** for anyone buying here.
- The one historical reference point in the window: RSI hit 33.31 on 2026-07-29, and the very next session began a +25% move. That is a reminder that in AMZN this oscillator's *extremes*, not its mid-zone, have been the actionable signal.

---

## 6. Volatility & Volume: The Most Constructive Part of the Picture

**ATR is compressing fast.** From 6.892 on 07-29, ATR spiked to **9.998 on 2026-08-05** (peak post-gap), then decayed for 15 of the next 16 sessions to **6.709**. That is a **−33% volatility collapse** in three weeks. Mechanically this means:
- The 27.76-point drawdown from 284.02 to 256.26 equals **4.1x current ATR** — a textbook-magnitude, non-panic pullback.
- ATR is now **2.62% of price**. Stops that would have been adequate at 10.0 ATR (e.g., ±20 points) are far too wide now; conversely, pre-August stops set at ~7 points are roughly right again.
- Bollinger bandwidth is **30.93 points = 11.58% of the 267.14 mid-line** — still wide, a leftover of the event, but narrowing as ATR falls. Bandwidth contraction precedes resolution.

**Volume argues for digestion, not distribution — with one caveat.**
- The 22-session average (07-29 → 08-27) is **~45.0M**. The last six sessions (08-20 → 08-27) average only **~29.2M**, roughly **65% of that**. Sellers are not pressing.
- The three heaviest days of the window (129.05M on 07-31, 101.84M on 07-30, 90.83M on 08-03) were all **up** days that repriced the stock higher. Accumulation on the event.
- Caveat: **08-27 volume rose to 35.93M from 21.53M the prior session** while price fell 1.54% (260.28 → 256.26) and closed at 256.26 against a 255.02 low — i.e., near the bottom of a 4.64-point range. That single-session uptick in selling pressure is a mild warning that the "quiet drift" may be transitioning to something with a bid behind it.

**VWMA is the quiet bearish tell.** At **264.11** it sits **2.97% above** the close, and it has rolled over from its 08-20 peak of 272.05. Because VWMA weights by volume, its position above price means the **volume-weighted average cost of everyone who traded the recent period is underwater**. That overhead "cost basis" at 264 is precisely where supply should appear on any bounce — and it happens to sit within a point of the 10 EMA (260.93) and the 38.2% retracement (262.10). Three independent methods pointing at 261–264 is the most robust feature of this chart.

---

## 7. The Level Map

**Resistance (in order of proximity):**
1. **258.24–260.28** — the 08-26 close and the 08-17/08-21 lows-turned-supply (08-17 low 258.34; 08-21 low 257.04).
2. **260.93** — 10 EMA; the first structural hurdle.
3. **261–264** — triple confluence: 38.2% retracement (262.10) + VWMA (264.11).
4. **267.14** — Bollinger mid / 20 SMA. Reclaiming this flips the short-term bias back to neutral-positive.
5. **270.73–273.23** — the 08-05 low and 07-31 high; the top of the gap's upper half.
6. **282.61 / 284.02 / 287.20** — Bollinger upper, peak close, intraday peak. The full-recovery ceiling.

**Support (in order of proximity):**
1. **255.02** — 08-27 low; immediate floor. A close below it opens the air pocket.
2. **251.08–251.68** — **50 SMA + Bollinger lower band** (0.6 points apart). The highest-quality support on the chart.
3. **248.57** — 61.8% retracement, completing the 248.5–252 confluence band.
4. **~242** — 2 ATR below current price (242.84); also the 08-04/08-05 congestion area (270.73 low is not it — the pre-gap shelf sits at 233–247).
5. **235.50** — the 07-30 close and the **bottom of the unfilled gap**. A full gap fill is a −8.1% scenario from 256.26 and would break the 200 SMA thesis only if it kept going.

---

## 8. Scenarios & Actionable Playbook

### Scenario A — Base case (highest probability, ~45%): continued digestion into 251–255, then resolution higher
**Trigger:** Price holds above 255.02 on light volume, MACD flattens before crossing zero, RSI stabilizes in the mid-40s.
**Action:** Do **not** pre-emptively buy the mid-zone. Scale into the **251–252** confluence (50 SMA + lower band) if it is touched with a **bullish reversal candle and volume < 30M** (signalling supply exhaustion rather than breakdown).
- Entry ~252, stop **246.50** (below the 61.8% level and ≈1.4 ATR), target 1 at **260.93** (10 EMA), target 2 at **264.11** (VWMA). R:R ≈ 1.6:1 to T1, ≈2.2:1 to T2.

### Scenario B — Momentum repair (~30%): reclaim 260.93 → 264
**Trigger:** A daily close above **260.93** with MACD histogram turning positive again and volume > 40M (i.e., real demand, not a drift).
**Action:** Enter long on the reclaim, stop **252** (below the confluence band, ≈1.3 ATR), targets **267.14** then **271.58**. This is the higher-quality but lower-probability path because it requires the bearish MACD cross to be reversed.

### Scenario C — Breakdown (~25%): lose 255.02, then 251
**Trigger:** A close below **251.08** that converts the 50 SMA from support to resistance and coincides with a MACD zero-line cross.
**Action:** This invalidates the "healthy pullback" thesis. Stand aside; the next logical magnet is the 61.8% at **248.57**, and beneath that the gap floor at **235.50**. Note that the 200 SMA at 238.59 sits between them — a full gap fill would put price essentially on the 200 SMA, which historically (in this window) has been the line that mattered.

### Scenario D — Failed-breakout retest of the highs (low probability now, <10%)
Requires a rapid reclamation of 267.14 followed by a push through 273.23. Only revisit the 284–287 supply zone after a fresh MACD bullish crossover above the zero line.

---

## 9. Risk Management Specifics (ATR-anchored)

- **Stop sizing:** with ATR at 6.709, a 1.5 ATR stop is **~10.1 points**; a 2 ATR stop is **~13.4 points**. Given the ATR is still decaying, set stops *now* using ATR but **re-derive weekly** — a further drop toward the pre-event 7.0 area is likely, and a stop sized for 10.0 ATR will be needlessly wide.
- **Position sizing:** for a 1% account risk with a 2 ATR (13.4 pt) stop → size = 1% of capital ÷ 13.4 per share. For a 0.75% risk and a tighter 1.5 ATR stop → ÷10.1.
- **Do not use the 08-27 low (255.02) as a stop if entering near 256** — that is only 0.18 ATR away and will be noise-stopped. Any long here needs either a wider stop at 246.50 or a smaller size.
- **Event risk:** the 12.5% gap on 07-31 proves this instrument can reprice a quarter in a week. Avoid carrying full size into scheduled catalysts, and avoid assuming the ATR-based stop protects against gap risk.

---

## 10. What Would Change This View (falsifiers)

| Turns me **bullish** | Turns me **bearish** |
|---|---|
| Close > 260.93 (10 EMA) **and** > 264.11 (VWMA) | Close < 251.08 (50 SMA) |
| MACD histogram turns positive (would need MACD > 3.479) | MACD crosses below zero (~1–2 weeks at current decay) |
| RSI reclaims > 55 with volume > 45M | RSI < 40 *without* price making a higher low |
| 50 SMA slope stays positive and accelerates above 251.08 | 50 SMA rolls back down (currently +0.2/day) |
| A definitive higher low above 255 | 200 SMA flattens toward 238.59 and price approaches it |

---

## 11. Bottom Line

AMZN is in an **orderly, low-volume retracement of a violent earnings-driven advance, inside an intact primary uptrend**. The evidence is genuinely two-sided and should be reported as such: the bullish case rests on a rising 200 SMA, a 50 SMA that has turned up, a golden-cross spread that is re-widening, and a pullback that is only 4.1 ATR deep on contracting volume. The bearish case rests on a confirmed MACD bearish cross (2026-08-17) with an accelerating negative histogram, price below the 10 EMA and VWMA, RSI at 47 with no divergence and no oversold cushion, and an unfilled gap beneath the market down to 235.50.

The tactical stance that fits this evidence is **patient and level-driven, not anticipatory**: the asymmetry is poor at 256.26 (mid-zone, mid-RSI, mid-gap), and materially better either (a) at the **251–252** 50 SMA / lower-band confluence, or (b) on a confirmed reclaim of **260.93 → 264.11**. The MACD zero-line cross, likely within days, is the clock ticking on this decision.

---

## 12. Summary Table

| Dimension | Reading (2026-08-27) | Evidence | Implication |
|---|---|---|---|
| **Verified close** | 256.26 | O 259.23 / H 259.66 / L 255.02; V 35.93M | Closed in bottom third of range — weak intraday tone |
| **Primary trend** | Bullish, intact | 200 SMA 238.59, rising from 232.82 (06-29); price +7.41% above | Do not short the primary trend |
| **Medium trend** | Turned up | 50 SMA 251.08, up 20 sessions from 246.38 (07-30); price +2.06% above | 251 is the line in the sand |
| **Short trend** | Down | 10 EMA 260.93, falling since 267.18 (08-12); price −1.79% below | Rallies face resistance at 261 |
| **Momentum level** | Positive but decaying | MACD 1.796 (from 8.432 on 08-11) | Cooling, not yet reversed |
| **Momentum signal** | Bearish cross | MACD < signal since 08-17; hist −1.683, widening 8 sessions | Tactical caution warranted |
| **Zero-line risk** | Approaching | MACD decays ~0.3–0.45/session from 1.796 | Zero cross possible ≈ 09-01 to 09-03 |
| **RSI** | 47.23, neutral | Peak 72.23 (08-03); no bullish divergence; no oversold cushion | Room to fall; no edge here |
| **Volatility** | Compressing | ATR 6.709 from 9.998 (08-05), −33%; 2.62% of price | Tighten stops; narrower targets |
| **Bands** | Lower half | Mid 267.14 / UB 282.61 / LB 251.68; ~−0.70σ | Bandwidth 11.58% still wide |
| **Volume** | Digestion | 6-day avg ~29.2M vs 22-day ~45.0M; but 08-27 rose to 35.9M on a down day | Sellers not aggressive — mildly concerning uptick |
| **Cost basis** | Overhead | VWMA 264.11, −2.97% above price | Supply expected on any bounce into 264 |
| **Gap status** | Unfilled | 235.50 (07-30 close) → 265.00 (07-31 open) = 29.50 pts / ~12.5% | Price is mid-gap; 235.50 is the downside magnet |
| **Fib on impulse** | At 50% | 38.2% = 262.10; 50% = 255.34; 61.8% = 248.57 | 256 is fair value; 248.5–252 is the value zone |
| **Key resistance** | 258.2 → 260.9 → 264.1 → 267.1 → 273.2 → 284.0/287.2 | Multiple verified closes | Layered; needs volume to clear |
| **Key support** | 255.0 → 251.1–251.7 → 248.6 → 242.8 → 235.5 | 50 SMA + Boll lower confluence | 251–252 is the highest-quality entry |
| **Bias** | Neutral-to-constructive | Bull structure vs. bear momentum | Wait for level; no chase at 256.26 |
| **Best entry zone** | **251–252** (long) | Confluence of 50 SMA, Boll LB, near 61.8% | Stop 246.50; T1 260.93, T2 264.11 |
| **Best confirmation** | **> 260.93 then > 264.11** on V > 40M | 10 EMA + VWMA + 38.2% all cluster | Stop 252; T 267.14 → 271.58 |
| **Invalidation** | Close < 251.08 | 50 SMA converts to resistance | Stand aside; 248.57 then 235.50 in play |
| **Sizing** | ATR-based | 1.5 ATR ≈ 10.1 pts; 2 ATR ≈ 13.4 pts | Re-derive weekly as ATR compresses |

*All prices, volumes, and indicator values above are taken directly from the `get_verified_market_snapshot` for 2026-08-27 and the `get_stock_data` OHLCV series (2025-11-01 → 2026-08-27); retracement levels, percentage changes, ATR multiples, and volume averages are arithmetic computed from those verified closes and are labeled as such. No support/resistance "bounce" claims are made — the level map describes reference prices, not validated historical reactions.*