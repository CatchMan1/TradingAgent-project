# AAPL — Technical Deep Dive | Verified as of 2024-02-29

## 1. Data anchor (source of truth)

The verified snapshot and the OHLCV pull agree row-for-row, so there is **no data discrepancy to flag**. Latest visible session:

| Field | 2024-02-29 |
|---|---|
| Open | 181.27 |
| High | 182.57 |
| Low | 179.53 |
| **Close** | **180.75** |
| Volume | 136,682,600 |
| Split / Div | 1.0 / 0.0 |

Prior close (2024-02-28): 181.42 → **–0.67 points, –0.37%**. Close printed in the lower third of the day's 3.04-point range — a soft, sell-into-the-close session.

Snapshot indicator values (2024-02-29): `close_50_sma 187.7194 | close_200_sma 183.9042 | close_10_ema 182.6334 | macd –1.9652 | macds –1.6535 | macdh –0.3116 | rsi 38.07 | boll 184.7755 | boll_ub 190.6662 | boll_lb 178.8848 | atr 3.0472 | vwma 183.1272 | mfi 0.2469`

*Note: the `mfi` value of 0.2469 is clearly outside the 0–100 scale of Money Flow Index; I am treating it as a malformed/unscaled output and deliberately excluding it from the analysis rather than interpreting it.*

---

## 2. Indicator selection and why

| Indicator | Why it fits this specific setup |
|---|---|
| **close_50_sma** (187.72) | The medium-term trend has visibly rolled over (190.92 on 2024-01-30 → 187.72). This is the line price must reclaim to neutralize the February downtrend. |
| **close_200_sma** (183.90) | The decisive battlefield. Price *closed above* it as recently as 2024-02-22 (close 184.37 vs 200SMA 183.69) and has closed below it every session since 2024-02-23. It is still rising, so the long-term uptrend is intact but under test. |
| **close_10_ema** (182.63) | Fastest read on whether the immediate impulse is down (it is), and the first meaningful intraday resistance on any bounce. |
| **macd** (–1.9652) | Momentum has been negative since 2024-02-01 and is at the lowest reading in this 2024-01-22 → 2024-02-29 window. |
| **macds** (–1.6535) | MACD crossed below signal on **2024-02-02** (macd –0.396 vs signal +0.049) and has stayed below — a persistent, not a one-day, bearish regime. |
| **rsi** (38.07) | Weak but *not* oversold, meaning there is still mechanical room toward 30 without a reversal claim. Also the cleanest place to check for divergence. |
| **atr** (3.0472) | Volatility is contracting (3.59 on 2024-02-02 → 3.05). Determines stop distance and position size in a compressed range. |
| **vwma** (183.13) | Price 180.75 is *below* the volume-weighted average price, i.e. recent sellers transacted at higher prices — capital is being distributed, not accumulated. |

Deliberately excluded: `boll_ub`/`boll_lb` as standalone selections (values taken from the verified snapshot instead, to avoid double-counting the 20-period mean already implied by VWMA/10-EMA), `macdh` (derivable from the two MACD lines I did pull), and any stochastics/RSI variant (redundant with RSI).

---

## 3. Trend structure: a fully bearish short-term stack pressing on the long-term line

Ranked from lowest to highest, the entire moving-average complex is inverted relative to price — price sits at the **bottom of the stack**:

```
180.75  ← Close (2024-02-29)
182.63  ← 10 EMA      (price –1.03%)
183.13  ← VWMA        (price –1.30%)
183.90  ← 200 SMA     (price –1.71%)
184.78  ← Bollinger mid (price –2.18%)
187.72  ← 50 SMA      (price –3.71%)
190.67  ← Bollinger upper
178.88  ← Bollinger lower (support)
```

Key readings:

- **The 200-day has been lost.** Closes from 2024-02-23 through 2024-02-29 (182.52 / 181.16 / 182.63 / 181.42 / 180.75) are all below the then-rising 200 SMA. This is the single most important structural fact on the chart.
- **The 50 SMA has rolled over and is falling ~0.33 pts/session** (190.92 on 2024-01-30 → 187.72), while the 200 SMA still rises ~0.04 pts/session. The 50–200 spread has compressed to **+3.82 points (+2.08%)**. A *scenario*, not a prediction: at the current slope differential of roughly 0.37 pts/day, that cushion could be consumed in about 10 sessions if price simply stalls. I am flagging this as a risk to monitor, **not** as a confirmed death cross — none exists on 2024-02-29.
- **The intermediate downtrend is well-established.** From the 2024-01-23 close of 195.18 to 180.75 is **–7.39%** over 25 sessions. The February highs never exceeded the January high (2024-01-23 intraday 195.75 vs February's high of 191.05 on 2024-02-07) — a lower-high sequence.
- **Short-term trend is down but decelerating in slope:** the 10 EMA is falling but the daily incremental decline has flattened (–1.47 pts from 2024-02-21 to 2024-02-23 vs –0.78 pts from 2024-02-27 to 2024-02-29).

---

## 4. Momentum: negative, but the rate of deterioration is easing

**MACD (deeply negative):**
- MACD line: –1.9652, its lowest reading in the retrieved 2024-01-22 → 2024-02-29 window.
- Signal: –1.6535. MACD has been below signal continuously since **2024-02-02** — 19 consecutive sessions of bearish alignment.
- **Histogram is narrowing**, which is the most constructive detail in the whole report:

| Date | MACD | Signal | Histogram |
|---|---|---|---|
| 2024-02-20 | –1.6256 | –0.8922 | **–0.7334** (trough) |
| 2024-02-21 | –1.7533 | –1.0644 | –0.6889 |
| 2024-02-23 | –1.7330 | –1.2950 | –0.4380 |
| 2024-02-26 | –1.8712 | –1.4102 | –0.4610 |
| 2024-02-27 | –1.8409 | –1.4964 | –0.3445 |
| 2024-02-28 | –1.8927 | –1.5756 | –0.3171 |
| **2024-02-29** | **–1.9652** | **–1.6535** | **–0.3116** |

The histogram has improved from –0.73 to –0.31 while price made a marginally *lower* low (181.56 close on 2024-02-20 → 180.75 on 2024-02-29). Downside momentum is still negative but **no longer accelerating**. That is a "sell pressure exhausting" tell — not a buy signal by itself.

**RSI (weak, not washed out):**
- 38.07 on 2024-02-29, vs the window low of **35.23 on 2024-02-20**.
- Price is lower than on 2024-02-20, but RSI is higher — a **mild positive divergence** on the short-term oscillator. Bear in mind the 2024-02-22 RSI pop to 44.05 failed within three sessions (back to 38.07), so this divergence has already been "tested and rejected" once.
- 38 is above the 30 oversold threshold. In a falling-trend regime, RSI can drift to 30–35 without a bottom, which is exactly what Feb 16–20 demonstrated (36.58 → 35.23 while price slid from 182.31 to 181.56).

---

## 5. Volatility: a compressed coil sitting on the lower band

- **ATR 3.0472** = **1.69% of the 180.75 close**. ATR has declined from 3.5864 (2024-02-02) — a ~15% contraction in realized range even as price fell. Falling ATR into a support test typically resolves with an expansion move rather than a slow bleed; direction is unresolved.
- **Bollinger geometry** (from verified snapshot): mid 184.78, upper 190.67, lower 178.88. Band width = 11.78 points = **6.37% of the mid**.
- **%B ≈ 0.16** — price is in the bottom sixth of the band, but **has not closed below the lower band** (180.75 > 178.88). No band-break exhaustion signal is present yet.
- The 2024-02-29 low of **179.53** is notable: it is the **lowest intraday print since 2023-11-07** (low 178.97) within the retrieved data — price is probing a fresh multi-month low *without* a volatility expansion. That is the classic signature of a squeeze before resolution.

---

## 6. Volume: the loudest signal of the session

- **2024-02-29 volume: 136,682,600** — the **highest daily volume in the entire retrieved window (2023-09-01 → 2024-02-29)**, exceeding 2023-12-15 (128,538,400) and 2024-02-02 (102,551,700).
- Versus the trailing 20-session average of approximately **54.0M** (computed from the retrieved rows, 2024-01-31 → 2024-02-28), that is roughly **2.5× normal**.
- Critically, this volume came on a **down day** with the close in the lower third of the range and a new multi-month low. Elevated volume into weakness is distribution behavior.
- **Caveat I want to be explicit about:** 2024-02-29 is a month-end session, and quarter/month-end index and fund rebalancing inflates prints independently of directional conviction. The volume is real and directional-leaning, but I would not treat a single month-end print as a durable regime signal.
- **VWMA (183.13) sits above price and is falling steeply** (189.72 on 2024-02-07 → 183.13). Every recent volume-weighted transaction has been at higher prices than the current close. That confirms sellers, not buyers, are setting the marginal price.

One constructive footnote from the earlier tape: **2024-02-02** printed 102.55M on a wide-range up day (open 179.86, low 179.25, high 187.33, close 185.85) — a high-volume demand footprint in the 179–180 area. That is directly relevant to the support case below.

---

## 7. Levels, scenarios, and actionable triggers

**Support ladder**
- **180.17–180.30** — January floor (2024-01-05 low 180.17; 2024-01-17 low 180.30).
- **179.53** — 2024-02-29 low, the operative pivot; also the 2024-02-27 low (179.56) — a tight double-bottom-ish shelf.
- **178.88** — Bollinger lower band, essentially coincident with the pivot. A close below both is the clean breakdown trigger.
- **176.21** — 2023-11-06 low, the next visible structural reference in the retrieved data.
- ATR extension: 180.75 – 2×ATR (6.09) ≈ **174.66**, roughly aligning with the low-175s.

**Resistance ladder**
- **182.63** (10 EMA) → **183.13** (VWMA) → **183.90** (200 SMA) → **184.78** (Bollinger mid). This is a dense, 2.15-point shelf; a single close won't be enough to declare it cleared.
- **187.72** (50 SMA) — the line that would flip the intermediate trend.
- **190.67** (upper band).

**Scenario A — Bearish continuation (primary, given the stack):**
Trigger: **daily close below 179.53 on volume > 60M** (i.e., above the ~54M norm). Targets 176.21, then ~174.66 (2×ATR). Invalidation: a reclaim of 183.90 (200 SMA) on rising volume.

**Scenario B — Base building / range (currently most consistent with the internals):**
Trigger: continued holds of 179.53–180.17 while the MACD histogram keeps narrowing and RSI holds above 35.23. This is a **coil**, and the ATR compression argues the resolution will be fast. Do not front-run it; wait for the break, then trade the retest.

**Scenario C — Bullish repair:**
Requirements, in order: (1) close above **183.90** (200 SMA), (2) close above **184.78** (Boll mid) — that also puts price back over VWMA and the 10 EMA, (3) MACD line crossing above signal. Until all three, bounces are counter-trend. The first real confirmation that February's distribution is over is a weekly close above **185.85** (the 2024-02-02 close, the origin of the big-volume demand day).

---

## 8. Risk management and execution notes

- **ATR 3.0472 (1.69% of price)** is the sizing unit. A 1.5×ATR stop is ~4.57 points; 2×ATR is ~6.09 points (~3.4% of price). With volatility this compressed, **stops placed at 1×ATR (≈3.05) inside the 179.5–182.5 chop will be whipsawed.**
- Long stop reference: **178.88** (lower band) or 1.5×ATR below entry, whichever is tighter after entry.
- Short stop reference: **184.78** (Bollinger mid); a close above that structurally contradicts the short thesis.
- Expect a resolution inside roughly 5–8 sessions given the ATR contraction and the tight 179.5–184.8 range (~2.9% wide).
- Do not treat the 2024-02-29 volume as conclusive in isolation — Monday 2024-03-04's volume will reveal whether it was rebalance flow or genuine supply.
- **Verified limitation:** everything above is derived from 2023-09-01 → 2024-02-29 data only. I have no tool support for claims about longer-term support/resistance, prior golden/death crosses, or post-2024-02-29 price action, and I make none.

---

## 9. Summary table

| Dimension | Reading (2024-02-29) | Interpretation | Actionable level / trigger |
|---|---|---|---|
| **Close** | 180.75 (–0.37% d/d) | Lower-third close, soft tape | — |
| **Short-term trend** (10 EMA) | 182.63, price –1.03% below | Down | Reclaim 182.63 = first relief |
| **Volume-weighted price** (VWMA) | 183.13, price –1.30% below | Distribution confirmed | Close > 183.13 needed for repair |
| **Long-term trend** (200 SMA) | 183.90, price –1.71% below; closed below since 2024-02-23 | **Long-term uptrend breached but SMA still rising** | Reclaim 183.90 = thesis flip |
| **Medium-term trend** (50 SMA) | 187.72, price –3.71% below; rollover from 190.92 | Bearish; 50–200 cushion only +2.08% | 50/200 compression = watch for cross risk (~10 sessions at current slope) |
| **Momentum** (MACD / Signal) | –1.9652 / –1.6535; below signal since 2024-02-02 | Persistent bearish regime | MACD–signal cross above 0 = trend repair |
| **Momentum internals** (Histogram) | –0.3116, improving from –0.7334 (2024-02-20) | Downside decelerating | 3+ more narrowing sessions = coil warning |
| **Oscillator** (RSI) | 38.07 (window low 35.23 on 2024-02-20) | Weak, not oversold; mild positive divergence | <35.23 = new downside leg risk; >50 = repair confirmed |
| **Volatility** (ATR) | 3.0472 (1.69%); down from 3.5864 | Compression into a test | 1.5×ATR stop ≈ 4.57; 2×ATR ≈ 6.09 |
| **Bands** (Boll) | mid 184.78 / ub 190.67 / lb 178.88; %B ≈ 0.16 | Lower quartile, no band break | Break < 178.88 = expansion down |
| **Volume** | 136.68M ≈ 2.5× 20-day avg; highest in window | Heavy distribution (month-end caveat) | >60M on a break below 179.53 validates it |
| **Primary pivot** | **179.53** (2024-02-29 low, lowest since 2023-11-07) | Line in the sand | < 179.53 → 176.21, then ~174.66; recover 183.90+ → repair |
| **Stance** | Deliverable = **defensive / sell rallies until 183.90 reclaimed** | Bearish short-term inside a tested long-term uptrend | Tactical longs only on a confirmed MACD-histogram turn *plus* a hold of 179.53 |

**Bottom line for AAPL:** as of 2024-02-29 the position is a **downtrend inside an intact-but-bruised long-term uptrend**. Price is below the 10 EMA, VWMA, 200 SMA, Bollinger mid, and 50 SMA — a complete bearish stack — with a fresh multi-month low, MACD at its window low, RSI at 38, and 2.5× normal volume on a down day. The only genuinely constructive evidence is second-order: the MACD histogram is narrowing for a sixth session, RSI is forming a mild higher low, and the 179–180 shelf has absorbed several tests plus one high-volume demand day (2024-02-02). That argues for a **coiled base case with real two-way risk**, not a clean short. The price levels that convert this ambiguity into a trade are unambiguous: **179.53 down, 183.90 up.**