# AAPL — Multi-Indicator Technical Report (as of 2024-02-27)

**Verified session (source of truth — `get_verified_market_snapshot`)**

| Field | Value |
|---|---|
| Open / High / Low / Close | 181.10 / 183.92 / 179.56 / **182.63** |
| Volume | 54,318,900 |
| 10 EMA | 183.4146 |
| 50 SMA | 188.3896 |
| 200 SMA | 183.8250 |
| VWMA | 184.480995 |
| MACD / Signal / Hist | −1.840875 / −1.496360 / −0.344516 |
| RSI(14) | 41.92 |
| Boll mid / UB / LB | 185.289 / 190.7737 / 179.8043 |
| ATR | 3.0522 |

All values returned by `get_indicators` match the snapshot to the reported precision — **no discrepancy to flag**. (The snapshot's `mfi` prints as `0.356`, which is not on a 0–100 scale; I have deliberately excluded it rather than interpret an ambiguous scale.)

---

## 1. Indicators selected (8) and why

1. **close_200_sma** — the decisive line right now: price is only marginally below it. It separates "normal correction inside an uptrend" from "trend break."
2. **close_50_sma** — the medium-term direction and the first real overhead supply shelf; also needed to monitor the 50/200 spread, which is compressing.
3. **close_10_ema** — responsive gauge for the short-term down-leg and for defining a tactical reclaim trigger.
4. **macd** — zero-line position + slope of momentum; confirms whether the February decline is still accelerating.
5. **macds** — required to date the crossovers and to quantify how far a bullish turn is from triggering.
6. **rsi** — overbought/oversold and, more importantly, RSI *peak structure* versus price peak structure (divergence test).
7. **atr** — volatility regime for stop distance and position sizing; ATR has been contracting, which changes the sizing math.
8. **vwma** — the volume-weighted truth of where holders are positioned; it is doing the heaviest lifting in the "distribution vs accumulation" call.

Deliberately omitted: `boll`/`boll_ub`/`boll_lb` and `macdh` — the snapshot provides the bands and histogram, and RSI + MACD already cover the momentum axes that a fourth momentum/volatility-band indicator would duplicate.

---

## 2. Price structure: a January–February range with a deteriorating ceiling

Using only tool-dated prices:

- **December 14, 2023 high 199.62** (close 198.11) is the top of the swing.
- **January 5, 2024 low 180.17** — first leg down.
- **January 23, 2024 high 195.75** (close 195.18) — the January rally peak.
- **February 2, 2024 low 179.25** on **102,551,700** shares — the heaviest volume in the window and the February floor.
- **February 7, 2024 high 191.05** — a materially *lower* high.
- **February 20, 2024 low 180.00**, then **February 23 high 185.04** — an even lower high.
- **February 27, 2024 low 179.56**, close **182.63** — retest of the floor zone, closing back in the upper 70% of the day's 4.36-point range on higher volume (54.3M vs 40.9M on Feb 26).

That sequence is **lower highs (195.75 → 191.05 → 185.04) against a repeatedly defended 179.25–180.00 floor**: a converging, distribution-flavored structure, not an accumulation base. The bearish read is reinforced by the fact that the Feb 27 test of 179.56 has **not** yet produced a higher low versus Feb 2's 179.25.

**Fibonacci confluence on the October→December advance** (Oct 26, 2023 low 165.67 → Dec 14, 2023 high 199.62, range 33.95):
- 38.2% retracement ≈ **186.65** (already lost)
- 50% retracement ≈ **182.65** — today's close of **182.63** is sitting almost exactly on it
- 61.8% retracement ≈ **178.64** — essentially the same zone as the Feb 2 low (179.25) and the Feb 27 low (179.56)

So the market is currently pinned at the 50% retracement, with the 61.8% level coinciding with the structural floor. That confluence is the reason 178.6–180.0 matters far more than any single indicator line.

---

## 3. Trend: short-term bearish inside a still-intact long-term uptrend, but the test is live

**Full moving-average stack (bearish ordering):**
`Close 182.63` < `10 EMA 183.41` < `200 SMA 183.83` < `VWMA 184.48` < `50 SMA 188.39`

- **200 SMA (183.83) is rising** — it climbed from 182.29 on Jan 31 to 183.82 on Feb 27. The primary trend is still up.
- **But price closed below it on Feb 23 (182.52 vs 183.73), Feb 26 (181.16 vs 183.78) and Feb 27 (182.63 vs 183.83)** — three consecutive closes beneath a rising 200-day, currently **0.65% below**. That is a *trend test*, not yet a trend break, but it is the single most important technical fact on the page.
- **50 SMA (188.39) is now rolling over**: 190.93 on Jan 30 → 190.48 on Feb 9 → 188.39 on Feb 27. Price has closed **below the 50 SMA for 20 consecutive sessions** (since Jan 30, when close 188.04 met 50 SMA 190.93). That is a persistent, not transient, breakdown of medium-term trend.
- **50/200 spread is compressing fast**: 8.74 points on Jan 30 (190.93 − 182.19) → **4.57 points** today (188.39 − 183.83). With the 50 SMA falling ~0.2–0.3/day and the 200 SMA rising ~0.05/day, the gap would close in roughly **2–3 weeks (mid-to-late March)** if this slope persists. A death cross is now a live scenario rather than a theoretical one, and it would be a strategic (not tactical) signal.
- **10 EMA at 183.41** has capped price action: the close has been below it every session since **Feb 12** (188.39 EMA vs 187.15 close that day). A close above 183.41 is the first, minimal sign of stabilization; it is not a buy signal by itself.

**Verdict on trend:** bullish long-term (rising 200-day, 50 > 200), bearish intermediate (20 sessions below the 50-day, 50-day declining), bearish short-term (below 10 EMA, VWMA and now the 200-day).

---

## 4. Momentum: the decline is decelerating, but nothing has turned

**MACD**
- MACD crossed **below zero on Feb 1, 2024** (−0.1376), and crossed **below its signal on Feb 2** (MACD −0.3959 vs signal 0.0490). Both conditions have persisted for the whole of February.
- MACD bottomed at **−1.8712 on Feb 26** and ticked up to **−1.8409 on Feb 27**, while the signal line kept falling to −1.4964.
- **Histogram path:** −0.6889 (Feb 21) → −0.4843 (Feb 22) → −0.4380 (Feb 23) → −0.4610 (Feb 26) → **−0.3445 (Feb 27)**. The histogram has improved by ~0.34 in four sessions. That is classic **downside momentum deceleration** — the selling impulse is fading.
- Interpretation: the *rate of decline* is easing, but MACD remains negative and below signal. A bullish MACD crossover requires roughly 0.35 of further convergence; if price holds above ~182 it is plausible within a few sessions, but a MACD crossover that occurs while MACD is still well below zero is a low-quality signal until price also reclaims 184.5–185.3.

**RSI**
- **41.92** today, up from 37.44 (Feb 26) and the February trough of **35.23 (Feb 20)**.
- Critically, RSI **never reached 30** in the February slide (lows 36.58 on Feb 16, 35.23 on Feb 20), whereas it hit **28.79 on Jan 5** — and the January oversold reading was followed by a rally to 195.18 by Jan 23. The absence of a genuine oversold reset this time means the February low is a *less* reliable springboard than the January one.
- **RSI peak structure is bearish:** 62.62 (Jan 23) → 50.81 (Feb 7) → 44.05 (Feb 22) → 41.92 now. Price and RSI are making lower highs together — **no bullish divergence exists.** The Feb 27 uptick of +4.5 RSI points is a bounce, not a divergence.
- RSI in the low-40s is genuinely neutral: there is room to fall to 30 without any "oversold" argument, and room to rise to 60–70 without resistance.

---

## 5. Volatility and bands: compressed, and a failed break of the lower band

- **ATR 3.0522**, down from 3.5864 on Feb 2 and 3.3699 on Jan 22. Volatility is **contracting** even as price grinds lower — typical of the tail end of a corrective leg, and consistent with the narrowing range (converging highs and a flat floor).
- ATR = **1.67% of the close**. Practical stop math: 1×ATR ≈ 179.58 from today's close; 1.5×ATR ≈ 178.05; 2×ATR ≈ 176.53.
- Today's true range was **4.36 points (1.43× ATR)**, an expansion day, driven by the 179.56 spike low.
- **Bollinger (20,2): mid 185.289, upper 190.774, lower 179.804.** Bandwidth is only **6.0% of the midline** — a squeeze relative to the ~11-point width. %B = **0.258**, i.e. price sits in the lower quartile of the bands.
- **Feb 27 pierced the lower band intraday (low 179.56 vs LB 179.80) and closed back inside at 182.63.** That is a one-session failed breakdown — a modest positive, but it is only meaningful if it is *not* reversed in the next session or two.

---

## 6. Volume: distribution still in control

- **VWMA 184.48 is above the close (182.63)** and has fallen monotonically from 189.72 on Feb 7 to 184.48 today. The volume-weighted holding cost is **1.00% above** spot: the average recent buyer is underwater. That is a supply-overhang condition, and every rally into 184.5–185.3 has to absorb it.
- The heaviest print in the window is **Feb 2 at 102.55M** on a wide 179.25–187.33 range closing at 185.85 — a high-volume absorption day that established the floor. Broad selling days since then have run 40–65M, i.e. **no climactic capitulation volume** at the Feb 20/Feb 27 tests. Bottoming typically wants either climactic volume or a drying-up of volume followed by a high-volume up day; we have neither.
- Feb 27's **54.3M on a long-lower-tail up-close** is constructive but unconfirmed.
- Structural caution: `vwma` is a 20-ish-day average, so it lags. Its slope, not its level, is the message — and the slope is down.

---

## 7. Actionable plan (levels, invalidation, sizing)

**Bias: neutral-to-bearish tactical; bullish strategic only above 188.4.** The stock is in a corrective range, capped by lower highs, with the 200-day under attack. I would not be adding long exposure at 182.63 into a declining VWMA and a negative MACD.

**A. Trend-test / continuation-short (primary tactical setup)**
- Trigger: a failed rally into **184.5–185.3** (VWMA 184.48 / Bollinger mid 185.29) — i.e. intraday push rejected and closed back below 184.0.
- Stop: **186.6–187.0** (above the Jan/Feb 12–13 breakdown band; Feb 12 close 187.15). Risk ≈ 1.8–2.4 points ≈ 0.6–0.8 ATR — tight, so size accordingly or widen to 187.5.
- Targets: **180.0 / 179.25**, then **178.64** (61.8% retracement). Reward:risk ≈ 1.5:1 to 2:1.
- Invalidation: two consecutive closes above 185.3, or a MACD bullish crossover with price above 185.
- Note: this is counter to the rising 200-day, so treat it as a swing trade, not a core short.

**B. Breakdown-short (higher-conviction, event-driven)**
- Trigger: a **daily close below 179.25** (Feb 2 low) — a decisive break of the floor that would also break the 61.8% retracement at 178.64.
- Stop: **181.5** (back inside the range). Risk ≈ 2.3 points ≈ 0.75 ATR.
- Targets: 176.5, then 175.5 (the Nov 2023 congestion from Nov 2 close 177.57 down to Nov 1 low 170.12 area).
- Caution: false breaks of this floor are the main risk given how many times 179.25–180.00 has been touched (Feb 2, Feb 20, Feb 27). Require the close, not the intraday print.

**C. Mean-reversion long (tactical, tight)**
- Trigger: a retest of **179.5–180.5** that holds and closes above 180.0, ideally with volume below the 40M level (supply drying up).
- Stop: **178.4** (below the 61.8% retracement at 178.64 and the Feb 2 low). Risk ≈ 1.6–2.0 points.
- Target 1: **184.4** (VWMA). Target 2: 185.3 (Bollinger mid). Reward:risk ≈ 2.5:1 to 3:1 on target 1.
- Only take this if the MACD histogram keeps improving. If the histogram deteriorates again below −0.46, stand down.

**D. Trend-repair long (strategic confirmation)**
- Trigger: a **close above 188.39 (50 SMA)** with MACD back above zero. That would neutralise the 20-session downtrend, restore the bullish MA stack, and target 190.77 (Bollinger upper, which is also the Feb 7 high zone 191.05), then 195.75 (Jan 23 high).
- Do *not* pre-position for this. The intermediate trend is still pointed down.

**Sizing:** with ATR at 3.05 (1.67% of price), a 1%-of-equity risk budget permits a position of roughly 0.6× the size you would use at AAPL's higher-volatility regimes (e.g. when ATR was ~3.6 in early February, or ~5+ in the Oct 2023 downdraft). Contracting ATR argues for *larger* nominal size per unit of risk but *tighter* percentage stops — a combination that punishes anyone who widens stops "because it's quiet."

---

## 8. What would change my mind

- **Bullish:** two closes above 184.5–185.3 **and** a MACD bullish crossover **and** VWMA flattening/turning up. Reclaiming the 200-day (183.83) with volume > 60M would be an additional early tell.
- **Bearish escalation:** a close below 179.25 on > 70M shares, or the 50 SMA crossing below the 200 SMA (currently ~15 sessions away at current slopes), or RSI breaking below 35 while price makes a new low (which would confirm, not contradict, the downtrend).
- **Neutral resolution:** continued churn between 179.25 and 188.39 with ATR falling further — in which case the correct answer is smaller size and fewer trades, not a directional bet.

---

## 9. Summary table

| Dimension | Evidence (date, level) | Read | Actionable level |
|---|---|---|---|
| Long-term trend | 200 SMA 183.8250, rising; close 182.63 = **0.65% below**; below it since Feb 23 close (182.52) | Uptrend intact but **under test** | Reclaim > 183.83 = relief; sustained closes below = trend break |
| Intermediate trend | 50 SMA 188.3896, falling from 190.9252 (Jan 30); **20 straight closes below** it since Jan 30 | Bearish | 188.39 is the strategic ceiling |
| Short-term trend | Close 182.63 < 10 EMA 183.4146 (below since Feb 12) < 200 SMA | Bearish | 183.41 = first stabilization trigger |
| 50/200 spread | 8.74 pts (Jan 30) → **4.57 pts** now, compressing ~0.3/day | Death-cross drift | Watch ~mid-to-late March |
| Price structure | Highs 195.75 (Jan 23) → 191.05 (Feb 7) → 185.04 (Feb 23); floor 179.25 (Feb 2), 180.00 (Feb 20), 179.56 (Feb 27) | Lower highs, flat floor = distribution | Break < 179.25 is the bear trigger |
| Fibonacci | 50% retrace = 182.65 (close 182.63); 61.8% = 178.64 | Pinned at 50%; 61.8% + floor confluence | 178.6–180.0 is the pivotal zone |
| MACD | MACD −1.8409 (trough −1.8712 Feb 26), signal −1.4964, below zero since **Feb 1**, below signal since **Feb 2** | Bearish, **decelerating** | Histogram −0.6889 (Feb 21) → −0.3445 (Feb 27) |
| RSI | 41.92; Feb lows 35.23 (Feb 20), 36.58 (Feb 16); Jan low 28.79 (Jan 5); RSI peaks 62.62 → 50.81 → 44.05 | Neutral-bearish, **no divergence**, never truly oversold | Break < 35 = fresh downside; > 55 = genuine repair |
| Bollinger | Mid 185.289, UB 190.774, LB 179.804; %B 0.258; width 6.0% of mid | Lower quartile, **squeeze**; Feb 27 pierced LB (179.56) and closed back in | 185.29 = mean-reversion magnet; 179.80 = band support |
| ATR | 3.0522 (1.67% of close), down from 3.5864 (Feb 2); Feb 27 true range 4.36 (1.43× ATR) | Volatility contracting | 1×ATR stop ≈ 179.58; 1.5× ≈ 178.05; 2× ≈ 176.53 |
| VWMA | 184.480995 > close 182.63; declining from 189.7199 (Feb 7) | **Distribution / supply overhang** | Reclaim of 184.48 = evidence of accumulation |
| Volume | Feb 2: 102.55M (floor day); recent 40–65M; Feb 27 54.3M with long lower tail | No capitulation, no accumulation | Needs > 60–70M up-close to validate a bottom |
| Tactical bias | Bearish MA stack, negative MACD, decaying histogram | **Neutral-to-bearish tactical, bullish only > 188.4** | Sell rallies 184.5–185.3; buy 179.5–180.5 with 178.4 stop |

**One-line summary:** AAPL is a correction, not yet a broken long-term uptrend — but it has lost its 50-day for 20 sessions, closed below a rising 200-day for three, and is being rejected by a declining VWMA. The 178.6–180.0 confluence is the line in the sand; 184.5–185.3 is the gate that must open before any bullish case becomes actionable.