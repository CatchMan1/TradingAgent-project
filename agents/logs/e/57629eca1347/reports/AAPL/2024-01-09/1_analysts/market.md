# AAPL — Technical Analysis Report (as of Tuesday, 2024-01-09)

**Source of truth:** `get_verified_market_snapshot` for 2024-01-09. All indicator values below were cross-checked against that snapshot and matched `get_indicators` output to the decimal — **no data conflicts to flag.**

---

## 1. Where AAPL Is Trading Right Now

| Field | 2024-01-09 | 2024-01-08 | Change |
|---|---|---|---|
| Open | 183.92 | 182.09 | +1.83 |
| High | 185.15 | 185.60 | — |
| Low | 182.73 | 181.50 | — |
| **Close** | **185.14** | 185.56 | **−0.42 (−0.23%)** |
| Volume | 42,841,800 | 59,144,500 | −16.3M |

AAPL closed at 185.14, a narrow inside-ish session (range 2.42 vs. ATR of 3.05) that gave back a trivial 0.23% after Monday's strong reversal candle. The important fact is not the daily bar but the **position in the structure**: price is simultaneously *below* the 10 EMA, the 50 SMA, the VWMA and the Bollinger midline, and *above* the 200 SMA and the lower Bollinger band. That is the signature of a **corrective pullback inside an intact longer-term uptrend** — a distribution phase, not yet a trend reversal, but with unambiguous short-term bearish control.

---

## 2. Indicator Selection & Rationale

I deliberately chose a **two-timeframe trend core + one momentum family + one volatility regime gauge + one volume-conviction gauge**, avoiding redundant oscillators (no RSI/StochRSI pairing):

| Slot | Indicator(s) | Why it earns a place here |
|---|---|---|
| 1 | `close_10_ema` | This is a fast, accelerating downtrend; I need a responsive line to time entries/exits. It has flipped to resistance. |
| 2 | `close_50_sma` | The line AAPL just lost on 01-02 — the single most important short-term trend boundary right now. |
| 3 | `close_200_sma` | The strategic bull/bear dividing line, and it sits almost exactly where the January low printed. Essential for framing risk. |
| 4 | `macd` + `macds` + `macdh` | Momentum regime change: zero-line cross + signal cross + histogram slope give the *direction, trigger, and deceleration* in one package. |
| 5 | `rsi` | Confirms the momentum reset from overbought to oversold and gauges whether the bounce has room. |
| 6 | `boll` + `boll_ub` + `boll_lb` | Volatility regime: a genuine band-squeeze release has occurred; bands define the mechanical support/resistance envelope. |
| 7 | `atr` | Required for sizing stops and targets in a market where daily range has expanded ~19% in nine sessions. |
| 8 | `vwma` | Answers the question price alone cannot: *is the bounce happening on conviction or on fumes?* |

---

## 3. Trend Structure — Three Timeframes Diverge

**Long-term (bullish, intact):** The 200 SMA sits at **180.285** and is rising monotonically every session in the sample (175.09 on 2023-11-30 → 180.28 on 2024-01-09). The 50 SMA at **188.052** remains above it, so the 50/200 "golden-cross" configuration is still in force, with a spread of **+7.77 points (+4.31%)** and *both* averages sloping up. Strategically, no damage yet.

**Medium-term (deteriorating):** The 50 SMA has gone from "support" to "overhead." AAPL's last close above the 50 SMA was **2023-12-29** (close 192.53 vs. 50 SMA 186.63). Since the 01-02 gap down, price has closed below it for **six consecutive sessions**, and the gap between close and the 50 SMA is now **−2.91 (−1.55%)**. Note the 50 SMA is still *rising* at roughly +0.25 to +0.37/day — meaning price must rally just to keep pace with a rising hurdle, a classic "bearish drift" mechanic.

**Short-term (bearish, but decelerating):** The **10 EMA at 186.988** has declined for **six straight sessions** off 195.041 (2023-12-15) — a −4.1% collapse in the average. Critically, the 10 EMA crossed **below** the 50 SMA on **2024-01-08** (187.399 vs. 187.687) and the gap widened on 01-09 (186.988 vs. 188.052). That short-term-over-medium-term cross is the cleanest single bearish signal in the dataset.

**Composite read:** A stacked, *bearish-aligned* short-term structure (price < 10 EMA < 50 SMA) inside a *bullish-aligned* long-term structure (price > 200 SMA, 50 > 200). This is textbook corrective consolidation, and it resolves at one of two lines: **188.05** above or **180.28** below.

---

## 4. Momentum — The MACD Story Is the Whole Story

The MACD family describes a complete momentum cycle in the last 20 sessions:

- **MACD line** peaked at **+3.751 on 2023-12-15**, decayed steadily, crossed **below the signal line** during the 12-19/12-20 window, and crossed **below zero on 2024-01-04** (+0.055 → −0.702). It is now **−1.611**, the most negative reading in the visible window.
- **Signal line** is at **−0.113**, itself rolling over — the signal line crossing zero confirms the bear phase has been formally registered, not just an intraday wiggle.
- **Histogram** turned negative on **2023-12-19** (−0.057) and widened relentlessly to **−2.045 on 2024-01-05** — the trough. Since then it has *contracted three sessions running*: −2.045 → −1.747 (01-08) → **−1.499 (01-09)**.

**Interpretation and nuance:** The histogram contraction is a **deceleration signal, not a buy signal**. In a declining-momentum regime, a contracting negative histogram often precedes a reflex rally — and indeed the 01-08 session delivered one (+2.4% close-to-close). But the MACD line at −1.61 is still falling, and no bullish crossover has occurred. The honest read: **downside momentum is exhausting, but the trend has not turned.** Traders should treat the histogram contraction as "stop pressing shorts blindly," not "go long."

**RSI corroborates the reset:** RSI printed **70.02 on 2023-12-08** (overbought), then collapsed to **28.79 on 2024-01-05** — the lowest reading in the entire ~28-session window and a fully oversold condition — before rebounding to 41.34 and now **40.60**. Two points of nuance:
1. RSI has **not** made a bullish divergence (price made its low on 01-05, RSI made its low on the same day — they're synchronized). So there's no technical basis to call a bottom from RSI alone.
2. At 40.60, RSI sits in **neutral-bearish no-man's-land**: it has left oversold (removing the mechanical bid) but is nowhere near 50–60, which is where a real trend repair begins. This is the most fragile part of the tape for bulls — the oversold bounce fuel is already spent.

---

## 5. Volatility — A Genuine Squeeze Release, and It Broke Downward

This is the most underappreciated signal in the data:

| Date | Boll UB | Boll Mid | Boll LB | Bandwidth (UB−LB)/Mid |
|---|---|---|---|---|
| 2023-12-29 | 198.82 | 194.31 | 189.80 | **4.65%** |
| 2024-01-05 | 202.95 | 192.64 | 182.32 | **10.70%** |
| 2024-01-09 | 202.73 | 191.67 | 180.61 | **11.54%** |

A textbook **volatility contraction on 12-29 (4.65% width) exploded to 11.54% in seven sessions** — bandwidth more than doubled. Critically, the expansion was **directional to the downside**: the lower band fell from 189.80 to 180.61 (−9.19) while the upper band barely moved (198.82 → 202.73, and it has now *turned down* for two sessions). Bollinger mid at **191.673** is declining for a fifth straight session.

**Where price sits in the envelope:** %B = (185.14 − 180.614) / (202.732 − 180.614) = **20.5%**. Price is in the **bottom quintile of the bands** — weak, but *no longer riding the lower band*. The mechanical washout already happened:
- 01-04: low 180.88 vs. LB 184.39 → **pierced**
- 01-05: low 180.17 vs. LB 182.32 → **pierced**, and this was the capitulation bar
- 01-08: low 181.50 vs. LB 181.45 → **held to the penny**
- 01-09: low 182.73 vs. LB 180.61 → **held with room**

That failure-to-re-pierce sequence is real, tool-supported evidence that the **lower band is now acting as support rather than a launching pad for further downside.**

**ATR at 3.054** (1.65% of price), up from **2.567 on 2023-12-28** (+19.0%). Practical consequence: any stop placed closer than ~3 points to entry is inside the daily noise and will be harvested. A 2×ATR stop is **6.11 points**; a 1.5×ATR stop is **4.58 points**.

---

## 6. Volume & Conviction — The Bounce Is Hollow

The **VWMA at 188.691** is the tell. It is above price (−3.55, −1.88%) and rolling over hard: **195.534 (12-26) → 188.691 (01-09)**, a 6.8-point decline in nine sessions. Translation: **the volume-weighted average buyer over the recent window is underwater.** That is distribution by definition.

The volume pattern around the break is asymmetric and damaging to the bull case:

- **Selling came on expanding volume:** 2024-01-02 = **82,488,700** shares (2.3× the 12-26 low of 28,919,300), 01-04 = **71,983,600**, 01-05 = **62,379,700**. All above the ~57M average of the prior 21 sessions (my calculation from the returned rows).
- **The bounce came on fading volume:** 01-08 = 59,144,500, and 01-09 collapsed to **42,841,800 — only ~75% of that 21-session average**, and the lowest volume of any up-close since 2023-12-28.

**A two-day rally that shrinks in volume every day while sitting below the 10 EMA, 50 SMA and VWMA is, on this evidence, a counter-trend bounce rather than accumulation.** Note also that 2023-12-15's 128,538,400 shares is the largest print in the sample — I'd treat that as expiry/rebalance-driven rather than directional information, and not extrapolate from it.

---

## 7. The Gap: AAPL's Most Concrete Resistance

There is an explicit, unfilled **price gap** in the data:

- **2023-12-29:** low 191.73, close 192.53
- **2024-01-02:** open 187.15, **high 188.44**, close 185.64

The untraded zone is **188.44 → 191.73**. This creates a layered resistance stack that aligns with the moving averages:

| Level | Value (2024-01-09) | Source |
|---|---|---|
| Gap-fill ceiling | **191.73** | 12-29 low |
| Bollinger midline | **191.67** | `boll` |
| VWMA | **188.69** | `vwma` |
| 50 SMA | **188.05** | `close_50_sma` |
| Gap-fill floor | **188.44** | 01-02 high |
| 10 EMA | **186.99** | `close_10_ema` |

Note the powerful confluence: **the 50 SMA (188.05), VWMA (188.69) and the gap floor (188.44) all sit within 0.65 points of each other.** This is the "prove-it" zone. A close above ~188.70 would simultaneously reclaim the 50 SMA, the VWMA and the gap floor — a genuinely meaningful shift.

Downside support:
| Level | Value | Source |
|---|---|---|
| Bollinger lower band | **180.61** | `boll_lb` |
| **200 SMA** | **180.28** | `close_200_sma` |
| January swing low | **180.17** | 2024-01-05 intraday |

These three cluster within **0.44 points** of each other — one of the tightest, highest-conviction support shelves you can construct. **180.17–180.61 is the line in the sand.** If that shelf fails on volume, the next *reference* zone from the returned data is the August 2023 consolidation: closes of 176.57 (08-16), 177.97 (08-10), 177.79 (08-11), and the 173.48 intraday low of 2023-08-17. I am describing prior price references, not asserting they will act as support.

---

## 8. Actionable Framework

**Overall stance: HOLD / neutral-to-defensive.** Do not chase the bounce; do not press shorts into the 200 SMA. The evidence is genuinely two-sided — an intact primary uptrend against a confirmed short-term distribution — so this is a **wait-for-trigger** tape, not a conviction tape.

**Trigger A — Bearish continuation (short / reduce exposure):**
- **Confirmation:** a daily close **below 180.17** (01-05 low) with volume **> 70M**, which would simultaneously break the 200 SMA and the lower Bollinger band.
- **Invalidation:** any close back above **186.99** (10 EMA).
- **Risk sizing:** stop at **+1.5×ATR ≈ 4.6 points** above the breakdown level; position size accordingly.
- **Note:** because RSI is only 40.6 (not 60+, not overbought) and MACD's histogram is contracting, shorting strength here means shorting *into* a support confluence. This is a lower-probability, lower-reward short than it was on 2024-01-02.

**Trigger B — Bullish repair (re-engage long):**
- **Stage 1 (weak):** close above **186.99** on volume > 57M — reclaims the 10 EMA. Historically-inconclusive alone; do not size up on this.
- **Stage 2 (actionable):** a *daily close above 188.70* — clears the 50 SMA + VWMA + gap floor together, opening the 191.67–191.73 gap fill.
- **Stop:** below **184.50** (roughly 1.5×ATR beneath a stage-2 entry near 188.7) or below the 10 EMA, whichever is tighter.
- **Do not** treat the 01-08/01-09 bounce as stage 2 — volume actively contradicts it.

**Trigger C — Range / base-building (most likely near-term path):** Chop between **180.6 and 186.99** while the 50 SMA catches up and ATR cools. In this case, favor patience; the reward/risk of both directions is poor inside a 6.4-point box against a 3.05 ATR (barely 2:1 range-to-noise).

**Risk-management overlay:**
- Use **3.05 ATR** (1.65% of price) as the noise floor. Stops tighter than ~3 points are statistically indefensible here.
- The 10 EMA / 50 SMA bearish cross (01-08) argues for **reduced gross exposure** until the shorter average turns back up.
- Watch whether the MACD histogram contraction extends to a fourth and fifth session — that, plus a *volume-expanding* close above 186.99, would be the first genuine bullish alignment since 2023-12-14.

**What would change my mind to outright bearish:** a close below 180.17 on heavy volume.
**What would change my mind to outright bullish:** a close above 188.70 on volume > 60M, especially if accompanied by a MACD bullish crossover.

---

## 9. Key Points Summary

| Category | Indicator | Value (2024-01-09) | Signal | Bull/Bear |
|---|---|---|---|---|
| Price | Close | 185.14 (−0.23%) | Narrow inside session after bounce | Neutral |
| Short-term trend | 10 EMA | 186.99 | Price below; 6th straight daily decline; crossed below 50 SMA on 01-08 | **Bearish** |
| Medium-term trend | 50 SMA | 188.05 | Price below for 6 sessions; still rising, acting as overhead | **Bearish** |
| Long-term trend | 200 SMA | 180.28 | Price +4.86 (+2.70%) above; rising since 11-30 | **Bullish** |
| Trend alignment | 50 vs 200 SMA | +7.77 (+4.31%) | Golden-cross regime intact | Bullish (strategic) |
| Momentum | MACD | −1.611 | Zero-line cross on 01-04; signal at −0.113 (also negative) | **Bearish** |
| Momentum slope | MACD Histogram | −1.499 | Contracting 3 sessions (−2.045 → −1.499) | Bearish, decelerating |
| Momentum | RSI | 40.60 | Reset from 70.02 (12-08) to 28.79 (01-05); now neutral-bearish | Neutral-fragile |
| Volatility regime | Bollinger bandwidth | 11.54% (vs 4.65% on 12-29) | Squeeze released **downward** | **Bearish** |
| Volatility position | Bollinger bands | UB 202.73 / Mid 191.67 / LB 180.61 | %B = 20.5%; lower band pierced 01-04 & 01-05, held 01-08 & 01-09 | Washout occurred |
| Volatility risk | ATR | 3.054 (1.65%) | +19.0% since 12-28; 2×ATR stop = 6.11 pts | Use wide stops |
| Volume conviction | VWMA | 188.69 | +3.55 above price; fell 6.8 pts in 9 sessions | **Bearish (distribution)** |
| Volume behavior | Latest volume | 42.84M | ~75% of ~57M 21-session avg; rally on shrinking volume | Bearish (hollow bounce) |
| Resistance stack | 186.99 / 188.05 / 188.69 / 191.67 | — | 10 EMA → 50 SMA → VWMA → gap/Boll mid | Overhead |
| Support shelf | 180.17 / 180.28 / 180.61 | — | Jan low + 200 SMA + lower band, within 0.44 pts | **Line in the sand** |
| Decision | **HOLD / neutral-defensive** | — | Long-term bull, short-term distribution; wait for 188.70 or 180.17 | Two-sided |