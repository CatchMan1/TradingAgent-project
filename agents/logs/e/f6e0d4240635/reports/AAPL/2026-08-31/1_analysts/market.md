# AAPL — Multi-Horizon Technical Report (as of close 2026-08-31)

## 1. Data integrity check (done first)

I pulled price history (`get_stock_data`, 2026-02-01 → 2026-08-31, 146 rows) and then the **verified snapshot** for 2026-08-31. I cross-checked every indicator against the snapshot and **found no discrepancies** between my indicator pulls and the verified snapshot:

| Field | Verified snapshot | My indicator pull | Match |
|---|---|---|---|
| Close 2026-08-31 | 316.850006 | 316.85 | ✅ |
| Open / High / Low | 319.60 / 321.24 / 312.80 | same | ✅ |
| Volume | 41,242,700 | same | ✅ |
| close_50_sma | 312.376799 | 312.376799 | ✅ |
| close_200_sma | 282.810150 | 282.810150 | ✅ |
| close_10_ema | 313.709501 | 313.709501 | ✅ |
| macd / macds / macdh | 0.297150 / −0.680104 / 0.977253 | 0.297150 / −0.680104 / +0.977253 | ✅ (0.297+0.680=0.977) |
| rsi | 54.076935 | 54.076935 | ✅ |
| boll / boll_ub / boll_lb | 310.5325 / 319.510464 / 301.554535 | bands match | ✅ |
| atr | 7.245075 | 7.245075 | ✅ |
| vwma | 310.796430 | 310.796430 | ✅ |
| mfi (snapshot only) | 0.572083 (~57.2 on 0–100 scale) | not separately pulled | — |

**All exact price/indicator figures below are sourced from the verified snapshot or from the indicator series returned by the tools.** Note the dividend adjustments in the data (0.26 on 2026-02-09, 0.27 on 2026-05-11, 0.27 on 2026-08-10); total-return index closed at 322.48 on 2026-08-31.

---

## 2. Indicator selection and why (8 core, all five categories covered)

| # | Indicator | Category | Why it earns a slot in *this* market condition |
|---|---|---|---|
| 1 | `close_200_sma` | Trend (long) | AAPL sits ~12% above a rising 200-SMA. This is the arbiter of whether the July/August damage is a correction inside a bull trend or the start of something larger. |
| 2 | `close_50_sma` | Trend (medium) | The pivot that matters *right now*: price (316.85) is only 1.4% above it (312.38), so the 50-SMA is the line separating "repair" from "failed bounce." |
| 3 | `close_10_ema` | Trend (short) | Post-shock, timing is everything. The 10-EMA (313.71) has stopped falling and turned up, and price is back above it — the earliest evidence of demand. |
| 4 | `macd` | Momentum | MACD (0.297) has just crossed above zero from a deep −2.68 trough (2026-08-17). Tells us the momentum *regime* is being rebuilt, not just a bounce. |
| 5 | `macds` | Momentum trigger | Needed as the crossover partner: the bullish cross occurred **2026-08-26** and has been confirmed for four straight sessions. Using `macd` without `macds` would lose the trigger date. |
| 6 | `rsi` | Momentum / overbought-oversold | 54.08 = neutral with room in both directions. Also lets me anchor the July excess (71.4/71.6 on 07-16/07-17) and the August reset (40.2 on 08-12). |
| 7 | `atr` | Volatility / risk | ATR 7.245 (2.29% of price) is compressing from the 9.87 post-crash peak — directly sets stop distance and position size for any trade taken now. |
| 8 | `vwma` | Volume confirmation | Price 1.95% above VWMA (310.80) which has turned up after declining from 329.58 (07-30) — volume-weighted cost basis confirms the recovery is not purely a thin-tape artifact. |

*Supplementary cross-check (retrieved, not counted in the 8):* `boll_ub` / `boll_lb` / `boll` — used only to assess band compression and the 2026-08-28 upper-band tag.

**Deliberately excluded:** `macdh` (fully derivable from `macd`/`macds`), `boll` middle (near-duplicate of a 20-SMA the 10-EMA/50-SMA already cover), stochastics/momentum duplicates of RSI.

---

## 3. Trend structure: bullish long-term, repairing medium-term, neutral-to-improving short-term

**Long-term (dominant): intact bull market.**
- Close 316.85 vs 200-SMA 282.81 → **+12.0%** above the long-term mean, and the 200-SMA is rising every session (277.96 on 2026-07-31 → 282.81 on 2026-08-31).
- The 50-SMA (312.38) sits **+10.5%** above the 200-SMA (282.81). Throughout the entire visible window (from at least 2026-06-02, where the spread was 13.8 points) this relationship has been bullish and the spread has **widened to 29.6 points** — trend *acceleration*, not deterioration.
- Critically: the two violent down-shocks (see §4) never came close to the 200-SMA. The 2026-07-31 low of 300.00 was still 6.1% above the 200-SMA on that date (277.96). **The primary trend has not been challenged on a closing basis at all.**

**Medium-term: a rolling correction that is being repaired.**
- The 50-SMA stopped rising in August. It peaked at 309.79 on 2026-08-07, actually rose slightly into 08-19 (309.44) and 08-26 (311.22), and is now 312.38. Its slope flattened to near-zero from 2026-08-03 (309.52) through 2026-08-18 (309.13) — i.e., the 50-SMA spent roughly three weeks going sideways while price whipsawed. That is the signature of a **time-based consolidation**, not a fresh leg down.
- Price has reclaimed the 50-SMA: closes of 313.45 (08-26), 314.58 (08-27), 319.70 (08-28), 316.85 (08-31) are all above 312.38.

**Short-term: constructive but capped.**
- 10-EMA 313.71 is above the 50-SMA (312.38) and below price (316.85) — correct bullish stacking for an early uptrend.
- The 10-EMA bottomed at 308.76 on 2026-08-17 and has risen to 313.71 on 2026-08-31, a clean upward inflection over 10 sessions.
- But price has not yet made a higher high above 322.37 (2026-08-28 intraday high), and the 2026-08-31 session was a **rejection day**: open 319.60 (above the previous close of 319.70's zone), high 321.24, close 316.85, low 312.80 — closing in the lower half of the range and giving back 0.89% (319.70 → 316.85).

---

## 4. Event map — two distribution shocks define the whole tape

The six-month price history is not a smooth trend; it contains two high-volume breaks that a trader must respect:

**Shock 1 — 2026-06-25:** close 293.08 (06-24) → open 287.40 → low 273.75 → close 275.15. Close-to-close **−6.11%** on 107.0M shares. The next session (2026-06-26) printed **261.8M shares** (an extreme outlier — roughly 6× the ~43M recent norm) and closed +3.14% at 283.78. Price then rallied **+20.7%** (281.74 on 2026-06-29 → 340.08 on 2026-07-28).

**Shock 2 — 2026-07-31:** prior close 333.43 (07-30) → **gap open 304.81** (−8.58%) → low 300.00 → close 308.91. Close-to-close **−7.36%** on **132.5M shares**. Measured from the 2026-07-29 intraday high of 344.57 to the 07-31 low of 300.00, that is **−12.94%** in three sessions.

**The nuance that matters:** Shock 1 was fully retraced and then some. Shock 2 created an **unfilled gap between 304.81 and 333.43** — a supply vacuum that is still overhead. Since 2026-08-04 (close 309.38), AAPL has closed *above the gap-open of 304.81* on every session, and has spent four weeks grinding inside the **lower third** of that gap. The highest high since 2026-07-31 is **322.37 (2026-08-28)** — meaning the **326–334 upper half of the gap is entirely untested**. That is the single most important structural fact on this chart.

So the current tape is best described as: *a post-crash base being built inside the body of the crash candle, with the lower half reclaimed and the upper half not yet challenged.*

---

## 5. Momentum: the most actionable signal on the board

- **MACD crossover confirmed.** MACD crossed above its signal on **2026-08-26** (macd −1.1007 vs macds −1.2524 → histogram +0.152). The histogram has expanded monotonically: **+0.152 (08-26) → +0.416 (08-27) → +0.896 (08-28) → +0.977 (08-31)**. That is a four-session momentum thrust, not a one-day blip.
- **MACD has also crossed zero**: 0.297 on 2026-08-31, up from a trough of −2.676 on 2026-08-17 and from −2.461 on 2026-08-14. Recovering a positive MACD is a regime change from "corrective downtrend" to "neutral/up."
- **But be honest about the context:** MACD is only **+0.297**, and the signal line is still **negative (−0.680)**. This is an *early-cycle* crossover occurring below the zero line — historically the noisiest kind. It is a reason to be constructive, not a reason to be aggressive. The prior peak MACD was **9.61 (2026-07-29)**, so the momentum engine is at ~3% of its July amplitude.
- **RSI 54.08** — dead center of the range. Sequence: **71.43 (07-16) / 71.65 (07-17)** = overbought at the top → collapse → **40.22 (08-12)** = washed out → **54.08 (08-31)**. The RSI has recovered ~14 points without a price breakout, which is the classic "momentum rebuilding under resistance" pattern. No RSI divergence is present at the highs or lows, so there is no reversal warning currently — but equally no oversold cushion to lean on if price rolls over.
- **MFI 0.572** (verified snapshot) corroborates: neutral-to-positive money flow, not a distribution reading. Consistent with RSI ~54.

---

## 6. Volatility and Bollinger structure: a coiled spring

- **ATR 7.245** (2.29% of price). Trajectory: 8.06 (07-30) → **9.87 (07-31, the crash)** → 8.22 (08-13) → **7.10 (08-27)** → 7.245 (08-31). ATR is now essentially at the **low end of the entire July–August visible window**, having round-tripped the volatility spike.
- **Bollinger compression is dramatic.** Upper band: **346.43 (08-10) → 319.51 (08-31)**; lower band: **289.77 (08-20) → 301.55 (08-31)**. Band width collapsed from **35.0 points on 2026-07-02** to **17.96 points on 2026-08-31** — roughly a **49% compression**.
- **Read this correctly:** bands are narrowing *from both sides* because realized volatility died, not because price broke down. Combined with a flat 50-SMA and a fresh MACD cross, this is a **squeeze setup** — the resolution direction is undetermined, but the *magnitude* of the next move is likely to exceed the last three weeks' drift.
- **Practical squeeze footprint:** on **2026-08-28** price closed at 319.70, marginally **above** the upper band (318.86) — a short-term overbought "band tag." On **2026-08-31** it was rejected back inside (close 316.85 < upper band 319.51). With 2.2% ATR and 5.8% band width, a single normal-range day is now sufficient to break either band.

---

## 7. Volume and participation

- **2026-08-31 volume 41.24M** — unremarkable, slightly under the August average and a modest uptick vs 38.65M on 08-28. The rally into 319.70 was **not** on expanding volume; that is a mild negative for the breakout thesis.
- **VWMA 310.80**, price **+1.95%** above it. VWMA peaked at **329.58 (2026-07-30)** and fell to **307.76 (2026-08-19)**, then flattened and turned up: 308.41 → 308.80 → 309.15 → 309.19 → 309.11 → 309.10 → 309.99 → **310.80**. Translation: the volume-weighted average buyer from the last several weeks is *slightly* underwater on the highs but now seeing price above their cost basis. VWMA sloping up under price = accumulation-friendly.
- **The volume asymmetry is the warning:** the largest volume prints of the period were **down/panic sessions** (107.0M on 06-25; 132.5M on 07-31), plus the anomalous 261.8M on 06-26. No comparable *up* volume has appeared in August. Until a 60M+ up-day accompanies a break of 322, treat upside follow-through as provisional.

---

## 8. Key levels (all derived from actual tool-printed prices)

**Resistance (ascending):**
| Level | Source |
|---|---|
| 319.51 | Bollinger upper band (2026-08-31) — immediate |
| 320.28 | Intraday high 2026-08-20 |
| 321.24 | Intraday high 2026-08-31 |
| **322.37** | **Highest high since the 07-31 crash (2026-08-28) — the breakout trigger** |
| 326.79–328.73 | 2026-07-16 low / 2026-07-15 high (top of the open gap's lower half) |
| 333.43–334.99 | 2026-07-30 close (pre-gap) / 2026-07-16–17 highs — the gap fill |

**Support (descending):**
| Level | Source |
|---|---|
| 313.71 | 10-EMA |
| **312.38** | **50-SMA — the pivot; also ~2026-08-31 low (312.80)** |
| 308.80–309.60 | 2026-08-26 low / 2026-08-19 low |
| 305.74–302.05 | 2026-08-18 low / 2026-08-13 low |
| **300.00–301.55** | **2026-07-31 low (300.00) + Bollinger lower band (301.55) — the line in the sand** |

Note how the 50-SMA (312.38), the 10-EMA (313.71) and the 08-31 low (312.80) cluster into a **312–314 micro-support shelf**. Price is sitting directly on it.

---

## 9. Actionable playbook

**Base case (probability-weighted highest): range continues 302–322 until a volume-backed resolution.**
- The tape has four consecutive closes above the 50-SMA but has failed twice near 320–322. With ATR at 7.25, the 302–322 box is only ~2.8 ATR wide — it should resolve within roughly 2–4 weeks.
- Trade the box, don't predict the break: buy the 312–314 shelf with a stop below 308.80; sell/fade 320–322.

**Bullish scenario (buy the confirmation, not the anticipation):**
- **Trigger:** a daily close **above 322.37 on volume ≥ ~60M** (i.e., ≥1.4× the recent ~43M norm). A close above 319.51 alone is insufficient given the 08-28 band-tag rejection.
- **Targets:** 326.79 (07-16 low) → 333.43–334.99 (gap fill). The gap fill is a ~5.2% move from 316.85 (333.43/316.85 − 1).
- **Stop:** below 312.38 (50-SMA); a close under 308.80 invalidates.
- **Risk sizing:** entry 322.5 with stop 311.5 = 11 points ≈ 3.4% ≈ **1.5× ATR** — consistent with the current 7.245 ATR. Size so a 1.5-ATR loss is ≤1% of equity.
- **Confirmations required before adding:** MACD histogram keeps expanding above +1.0; RSI pushes through 60; VWMA continues rising.

**Bearish scenario (this is the one to respect, because the overhead gap is real):**
- **Trigger:** daily close **below 312.38 (50-SMA)**, confirmed by a close below **308.80**. That would flip the 10-EMA back under the 50-SMA and likely drag MACD back below its signal.
- **Targets:** 302.05 → **300.00–301.55** (07-31 low + lower band). A decisive break of 300.00 opens the pre-crash structure, but note there is **no tool-supported downside reference between 300.00 and the 200-SMA at 282.81** — be cautious about price targets in that vacuum.
- **Invalidation of the bear case:** the 200-SMA at 282.81 remains 10.7% below spot; a bear thesis is a *medium-term* thesis only, and contradicts the 50>200 configuration until that changes.

**Neutral / risk-management overlay:**
- With ATR compressed to 7.245, **options-premium-selling is structurally attractive** inside 302–322 (band squeeze = cheap realized vol relative to implied), while **straddle/strangle buyers** are positioned for the eventual expansion. Both are legitimate; the data supports "resolution coming," not its direction.
- Avoid chasing the 08-28→08-31 candle: it tagged and was rejected by the upper band on light volume.

---

## 10. What would change my view

**Bullish upgrades:** (a) close >322.37 on ≥60M volume; (b) MACD histogram >+1.0 with MACD line >+1.0; (c) RSI >60 without a price pullback; (d) 10-EMA >50-SMA by >1% with both rising.
**Bearish downgrades:** (a) close <312.38 then <308.80; (b) MACD rolls back below its signal before the line clears +1.0; (c) RSI fails at 55–60 and turns down — would signal the 08-26 crossover was a head-fake; (d) Bollinger expansion to the *downside* with expanding volume.
**Structural caveat:** the 2026-07-31 gap (304.81–333.43) is the dominant overhead feature. Until AAPL closes above 333.43, every rally is technically a retracement inside a crash candle, no matter how good the short-term momentum looks.

---

## 11. Summary table

| Dimension | Reading (2026-08-31) | Evidence | Interpretation | Actionable takeaway |
|---|---|---|---|---|
| **Last price** | 316.85 | Verified snapshot; O 319.60 / H 321.24 / L 312.80; vol 41.24M | Rejection day, closed lower half of range, −0.89% vs 08-28 | Don't chase; wait for a close >322.37 |
| **Long-term trend** | Bullish | 200-SMA 282.81, rising; price +12.0% above | Primary uptrend intact; both crashes held well above it | Strategic bias stays long |
| **50/200 structure** | Bullish, widening | 50-SMA 312.38 = +10.5% over 200-SMA; spread 13.8 → 29.6 pts since 06-02 | Golden-cross regime, accelerating | No death-cross risk near term |
| **Medium-term trend** | Flattening / repairing | 50-SMA 309.79 (08-07) → 312.38 (08-31); ~3 weeks sideways | Time-based consolidation, not distribution | Range trade 302–322 |
| **Short-term trend** | Improving | 10-EMA 313.71, bottomed 308.76 (08-17), price above both MAs | Bullish MA stacking restored | Longs valid above 312.38 |
| **MACD** | Early bullish cross | Cross on 08-26; hist +0.152→+0.416→+0.896→+0.977; MACD 0.297 > 0 but signal −0.680 | 4-session thrust, but sub-zero = low-conviction | Constructive, not aggressive; needs >+1.0 |
| **RSI** | 54.08 neutral | 71.65 (07-17) → 40.22 (08-12) → 54.08 | Momentum rebuilding, no divergence | Room both ways; watch 60 |
| **Volatility** | Compressing hard | ATR 7.245 (2.29%); peak 9.87 (07-31); low 7.10 (08-27) | Post-shock vol crush | Tighten stops; expect expansion |
| **Bollinger** | Squeeze | Width 17.96 (5.8% of 310.53) vs 35.0 on 07-02; UB 319.51, LB 301.55 | ~49% compression, resolution pending | Breakout trade setup forming |
| **Volume** | Neutral / unconfirmed | 41.24M vs ~43M Aug norm; VWMA 310.80, price +1.95% above, VWMA turning up | Accumulation-friendly but no up-volume confirmation | Need ≥60M up-day to trust breakout |
| **Key resistance** | 319.51 / 320.28 / 321.24 / **322.37** / 326.79 / 333.43 | Bands, 08-20 & 08-31 highs, 08-28 high, 07-16 low, 07-30 close | 322.37 is the pivot; 333.43 fills the gap | Buy stops above 322.37 |
| **Key support** | 313.71 / **312.38** / 308.80 / 302.05 / **300.00–301.55** | 10-EMA, 50-SMA, 08-26 low, 08-13 low, 07-31 low + LB | 312–314 is the immediate shelf | Sell stops below 308.80 |
| **Unfilled gap** | 304.81 → 333.43 (from 07-31) | 07-30 close 333.43; 07-31 open 304.81 | Price holds lower third of crash body; upper half untested since 07-31 | Rally = retracement until >333.43 |
| **Risk parameters** | ATR 7.245 (2.29%) | Stop 1.5×ATR ≈ 11 pts ≈ 3.4% | Position size so 1.5-ATR loss ≤1% equity | 1R ≈ 7–11 points |
| **Verdict** | **Constructive range / squeeze** | Bull trend + fresh MACD cross + vol compression, capped by unfilled gap | Bull bias for *structure*, neutral for *timing* | Trade 302–322 box; add only on >322.37 with volume |