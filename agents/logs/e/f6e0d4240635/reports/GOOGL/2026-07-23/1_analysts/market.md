# GOOGL (Alphabet Inc.) — Technical Report as of 2026-07-23

## 1. What Happened Today: A Breakaway Gap on Heavy Volume

The verified snapshot for **GOOGL** shows a violent repricing on the session of **2026-07-23**:

| Field | 2026-07-22 | 2026-07-23 | Change |
|---|---|---|---|
| Open | 348.16 | **321.13** | −27.03 (−7.76%) |
| High | 349.94 | 324.49 | — |
| Low | 341.73 | **314.90** | — |
| Close | 342.09 | **317.69** | −24.40 (**−7.13%**) |
| Volume | 39,334,100 | **69,419,700** | +76.5% |

Three structural facts are directly verifiable from the data:

1. **A true breakaway gap.** Today's high (324.49) is *below* yesterday's low (341.73), leaving an unfilled gap of **17.24 points** between 324.49 and 341.73. The open itself gapped −6.13% from the prior close.
2. **A weak close.** The close of 317.69 sits only 2.79 above the session low and 6.80 below the open — i.e., in the bottom ~29% of the day's 9.59-point range. Sellers controlled the close; there was no intraday reclaim attempt.
3. **Volume confirmation.** 69.42M shares is ~2.1× the 20-session average (~33.16M, computed from the 2026-06-24 → 2026-07-22 rows) and ~2.6× the trailing 10-session average (~26.39M). A −7% day on double-plus volume is distribution, not noise.

The magnitude, the gap, and the volume profile are characteristic of an **event-driven fundamental repricing**. I have no news/fundamental tool in this workflow, so I flag the catalyst as an inference only — the *price and volume* evidence is what I can verify.

> **Discrepancy flag:** the verified snapshot reports `mfi = 0.311527`, which is not a valid value for a 0–100 money-flow oscillator. I treat this as a data/scaling artifact and have excluded MFI from the analysis and indicator selection rather than build a conclusion on it.

---

## 2. Indicator Selection and Rationale

Given a **post-breakdown, high-volatility, event-gap regime**, the goal is (a) to locate price within the trend hierarchy, (b) to judge whether momentum is exhausted or re-accelerating, (c) to size the extreme, and (d) to confirm the move with volume. I selected 8 complementary indicators:

| Indicator | Value (2026-07-23) | Why it is relevant here |
|---|---|---|
| **close_10_ema** | 346.00 | Fastest read on the short-term trend; quantifies how far price has detached from the recent mean |
| **close_50_sma** | 366.06 | Medium-term trend spine; now rolling over and confirming the lower-highs structure |
| **close_200_sma** | 323.56 | Long-term regime line; price closed below it — the key strategic tell |
| **macd** | −6.33 | Measures whether the downdraft is decelerating or re-accelerating |
| **rsi** | 31.02 | Quantifies oversold stretch and flags divergence potential |
| **boll_lb** | 329.21 | Defines statistical stretch and the first mean-reversion target |
| **atr** | 12.22 | Volatility regime for stop placement and position sizing |
| **vwma** | 350.15 | Volume-weighted fair value; confirms whether volume is validating price |

---

## 3. Trend Hierarchy: The Entire April–July Advance Has Been Erased

### Long-term (200 SMA) — the regime just cracked
- 200 SMA = **323.56** and rising toward it at ~0.36/session.
- Close 317.69 is **−1.81% below** the 200 SMA.
- Within the visible window (2025-12-01 → 2026-07-23), every prior close sat *above* the 200 SMA — even the March 2026 washout (close 273.50 on 2026-03-30 vs 200 SMA 263.23). **Today is the first close below the 200-day line in the visible data.** That is a strategic regime downgrade, not a routine pullback.

### Medium-term (50 SMA) — rolling over, price deeply detached
- 50 SMA = **366.06**, down from a peak of **372.80 on 2026-07-13** — the average has turned down.
- Close 317.69 is **−13.21% below** the 50 SMA. That is an extreme short-term dislocation; historically (within this window) GOOGL has not traded this far below its 50-day mean.
- 50 SMA (366.06) vs 200 SMA (323.56): the **golden-cross configuration is still intact** (spread 42.50, ~13.1% of the 200 SMA), but it is eroding at roughly 1.7–1.8 points per session. Mechanical extrapolation (not a forecast) puts the 50/200 crossover flat in ~20–25 sessions if the current slope persists. This is the structural risk to watch on a strategic horizon.

### Short-term (10 EMA) — downtrend accelerating
- 10 EMA = **346.00**, down from 360.55 on 2026-07-15.
- Close is **−8.18% below** the 10 EMA. The 10 EMA is now only ~22.4 points above the 200 SMA and falling ~2.3/session — it is on track to lose the 200 SMA before the 50/200 pair does.

### Price structure — a textbook lower-highs sequence
The close sequence of swing highs is unambiguous:

| Swing high | Date | Close | Intraday high |
|---|---|---|---|
| Peak 1 | 2026-05-08 | 400.80 | 402.00 |
| Peak 2 | 2026-05-18 | 396.94 | **408.61** |
| Peak 3 | 2026-05-28 | 390.13 | 391.87 |
| Peak 4 | 2026-06-16 | 373.25 | 376.00 |
| Peak 5 | 2026-07-15 | 370.92 | 375.27 (7/16) |

Today's low of **314.90** decisively undercuts both the 2026-07-17 low (341.36) and the June swing low (330.20 intraday on 2026-06-26). **Lower highs + a new lower low = confirmed downtrend**, not a pullback within an uptrend.

### Drawdown context (all computed from tool rows)
- From the **2026-05-08 closing high of 400.80**: 317.69 = **−20.7%**
- From the **2026-05-18 intraday high of 408.61**: close = **−22.3%**; today's low of 314.90 = **−22.9%**
- Versus the **2025-12-31 close of 313.00**: 317.69 = only **+1.50%** year-to-date — i.e., roughly seven months of gains have been surrendered in this move.
- Lowest close since **2026-04-08** (317.32). The 2026-04-08 close of 317.32 and 2026-04-09 close of 318.49 bracket today — everything purchased between early April and mid-July is now underwater.

---

## 4. Momentum: Re-Acceleration of the Downtrend, Not Exhaustion

### MACD — fresh bearish crossover, now widening hard
- MACD line: **−6.33** (from −3.78 on 7/22, −0.78 on 7/15)
- Signal line: **−3.34**
- Histogram: **−2.99** (from −1.19 on 7/22, and **+1.48** on 2026-07-15)

The histogram flipped negative on **2026-07-17** (−0.049) after a July recovery attempt, and has expanded negatively for four consecutive sessions. This is the *opposite* of a momentum washout: the MACD line is making a new low for the move and diverging further from its signal. Notably, the MACD line is now approaching its June low (−7.35 on 2026-06-26), so a **bullish divergence would require a higher low in the MACD line against a lower price low** — that does not yet exist.

### RSI — approaching oversold, but not divergent
- RSI: **31.02** (from 40.55 on 7/22, 43.10 on 7/21)
- The RSI fell **9.5 points in one session** — a sharp velocity of decline typical of trend acceleration.
- RSI is just above the 30 threshold. The comparable June episode bottomed at **33.27 on 2026-06-26** before a bounce, and RSI hit **38.98 on 2026-06-22**. Today's 31.02 is the lowest RSI print in the visible window.
- **Critically, there is no bullish divergence**: price made a lower low and RSI made a lower low. In strong downtrends RSI can sit in the 25–40 band for weeks; 31 alone is not a buy signal.

---

## 5. Volatility and Statistical Stretch

### Bollinger Bands — expansion in the direction of the break
- Middle (20 SMA): **353.39**
- Upper: **377.57** | Lower: **329.21**
- Bandwidth: **13.68%** of the middle (48.36 points), up from **10.12%** (35.90 points) on 2026-07-22 — a one-day band expansion of ~35%.
- **Close of 317.69 is 3.50% BELOW the lower band.**

Interpretation nuance: riding/closing below the lower band in a *range* is a mean-reversion signal; closing below an *expanding* lower band on 2× volume after a gap is far more often **trend continuation / volatility repricing**. The prudent read is: stretched enough for a violent counter-trend snap-back, but not evidence of a bottom.

### ATR — volatility regime step-up
- ATR = **12.22**, up from 11.07 (+10.4% in one day), and from 10.31 on 2026-07-14.
- ATR as % of price = **3.85%**. Risk per unit of position has nearly quadrupled versus the ~2.6% implied by June's ATR readings relative to price.
- Today's true range (using the prior close of 342.09): **27.19 points** — the largest in the visible window.

**Practical consequences:**
- Any stop tighter than ~1×ATR (≈12.2 points) is inside daily noise and will be hit randomly.
- A 2×ATR stop from today's close implies a **293.25** risk level.
- Position size should be cut by roughly the inverse of the ATR% change — if your prior sizing assumed ~2.5–2.6% daily range, today's regime requires ~65–70% of the previous notional for the same risk budget.

---

## 6. Volume: The VWMA Confirms This Is Real Distribution

- **VWMA (20-day) = 350.15.** Price is **−9.27% below** it.
- The VWMA actually *rose* through mid-July (350.76 on 7/14 → 358.74 on 7/20), meaning buyers were transacting at ever-higher volume-weighted prices. Today it collapsed 6.60 points in a single session — the heaviest-volume print in weeks occurred at the lowest prices, dragging fair value down hard.
- The distribution signature is cumulative, not a one-off: **2026-07-16** closed 354.46 after opening 373.06 on 41.16M shares (a bearish reversal day, range 375.27 → 352.30), followed by **2026-07-22** at 39.33M and today's 69.42M. Volume has been rising as price fell across four of the last six sessions.
- Caveat for nuance: the highest-volume day in the window was **2026-06-26 (114.71M)** on a modest −1.84% decline that was subsequently bought back (price rallied from 337.39 to 373.25 by 2026-06-16... i.e., into 2026-07-15's 370.92). So heavy-volume down days have been *absorbed* once already this summer. That is the one piece of evidence arguing for a tradable bounce rather than a collapse — but the structural damage (200 SMA loss) is new.

---

## 7. Level Map (all levels derived from tool rows)

**Resistance (in order of proximity):**
| Level | Source |
|---|---|
| **324.49** | 2026-07-23 high — must be reclaimed first |
| **329.21** | Bollinger lower band — first mean-reversion magnet |
| **337.39 / 341.36 / 342.09** | 2026-06-26 close / 2026-07-17 low / 2026-07-22 close → the gap-fill zone |
| **346.00** | 10 EMA |
| **350.15 / 353.39** | VWMA / Bollinger middle |
| **366.06** | 50 SMA — trend-repair only above here |

**Support:**
| Level | Source |
|---|---|
| **314.90** | 2026-07-23 low — the line in the sand |
| **305.46 / 306.36** | 2026-04-07 close / 2026-03-09 close |
| **298.52 – 302.02** | March 2026 congestion (2/17: 302.02; 3/2: 306.52; 3/5: 300.88; 3/6: 298.52) |
| **287.56 – 289.24** | 2026-03-31 close / 2026-03-25 low |
| **272.11 – 273.50** | 2026-03-30 intraday low / close — the 2026 structural low |

Note: **2026-04-08's close of 317.32** is the precise pivot — today's 317.69 close is 0.37 above it. Holding/breaking this micro-level matters for the short-term tape.

---

## 8. Actionable Framework

**Bias: defensive/bearish. I would not initiate or add to long exposure here.**

The evidence set — first close below the 200 SMA, confirmed lower-highs/lower-low structure, MACD histogram expanding negatively, close 3.5% below an expanding lower band, price 13.2% below a now-falling 50 SMA, on 2.1× average volume — describes a trend in **acceleration**, with the only offsetting factor being short-term statistical stretch (RSI 31, Boll lower-band breach).

**For long-side traders / holders:**
- Do not average down into this. The 200 SMA break is a regime signal that typically requires *time* (not just price) to repair.
- If holding, a stop below **314.90** (today's low) is the logical invalidation, but recognize that 1×ATR is already 12.2 points — a 314.90 stop is only ~0.2 ATR away and is likely to be noise-tested. A volatility-adjusted stop sits nearer **305 (≈1×ATR below the low)** or **293 (≈2×ATR below close)**.
- Re-entry/reclaim triggers, in ascending order of confirmation: (1) close back above **329.21** (Boll lower) on declining volume — bounce only; (2) close back above **342.09** — gap filled, immediate damage neutralized; (3) close back above **346.00** (10 EMA) with the 10 EMA turning up — short-term trend repaired; (4) **above 366.06 (50 SMA)** — strategic trend repaired.

**For short-side traders:**
- The momentum is with you, but the risk/reward at the *current* price is poor: price is 3.5% below the lower band with RSI at 31, which is exactly where counter-trend squeezes start. A retest toward **329–342** (band/gap zone) is the higher-quality location to express a short.
- Stop logic: above **342.09** invalidates the gap-down thesis; above 346 (10 EMA) invalidates the short-term downtrend.

**Risk / position-sizing notes:**
- ATR regime shift means **cut position size ~30–35%** versus the June regime for an equivalent dollar risk.
- Expect **two-sided 3–4% daily ranges** to persist until ATR rolls back under ~10.5.
- The unfilled gap at **324.49–341.73** is a magnet and a resistance shelf; treat it as the boundary of the breakdown, not as support.

**What would change my mind (bullish):** a bullish MACD histogram reversal *combined with* a higher low in price above 314.90, and a reclaim of 329–342 on contracting volume. That combination does not exist as of 2026-07-23.

---

## 9. Summary Table

| Dimension | Reading (2026-07-23) | Signal | Evidence |
|---|---|---|---|
| **Session action** | O 321.13 / H 324.49 / L 314.90 / C **317.69**, vol 69.42M | Strongly bearish | −7.13% vs 342.09 close; close in bottom 29% of range; 2.1× 20-day avg volume |
| **Gap** | Unfilled 324.49 → 341.73 | Bearish (breakaway) | Today's high < prior day's low; −6.13% opening gap |
| **Long-term trend** | close 317.69 vs **200 SMA 323.56** | **Regime downgrade** | First close below 200 SMA in the visible window (−1.81%) |
| **Medium trend** | close vs **50 SMA 366.06** | Bearish | −13.21% below a 50 SMA that peaked at 372.80 on 07-13 and is now falling |
| **Short trend** | close vs **10 EMA 346.00** | Bearish, accelerating | −8.18% below; 10 EMA down 14.6 pts since 07-15 |
| **Structure** | Lower highs 400.80 → 396.94 → 390.13 → 373.25 → 370.92; new low 314.90 | Confirmed downtrend | Undercuts 07-17 low 341.36 and 06-26 low 330.20 |
| **MACD** | −6.33 / signal −3.34 / hist **−2.99** | Bearish, re-accelerating | Histogram flipped negative 07-17 and expanded 4 straight sessions |
| **RSI** | **31.02** (from 40.55) | Oversold-adjacent, no divergence | −9.5 pts in one day; lowest reading in window; price and RSI both made lower lows |
| **Bollinger** | Mid 353.39 / UB 377.57 / **LB 329.21**; bandwidth 13.68% (vs 10.12%) | Stretched, trend-confirming | Close 3.50% below a rapidly expanding lower band |
| **ATR** | **12.22** (3.85% of price), from 11.07 | Volatility step-up | Largest true range in window (27.19 pts); cut size ~30–35% |
| **VWMA** | **350.15** | Bearish volume confirmation | Price −9.27% below; VWMA fell 6.60 pts in one session on distribution |
| **Drawdown** | −20.7% from 400.80 close (05-08); −22.3% from 408.61 intraday | Bear market territory | +1.50% YTD vs 313.00 (2025-12-31 close) |
| **Key resistance** | 324.49 / 329.21 / 341.36–342.09 / 346.00 / 350.15–353.39 / 366.06 | — | Today's high / Boll LB / gap zone / 10 EMA / VWMA-Boll mid / 50 SMA |
| **Key support** | 314.90 / 305.46–306.36 / 298.52–302.02 / 287.56–289.24 / 272.11 | — | Today's low / April-March closes / March congestion / March swings / 2026 low |
| **Stance** | **Defensive — no new longs** | Bearish bias | Trend + momentum + volume aligned down; only offset is short-term stretch |
| **Long re-entry triggers** | >329.21 → >342.09 → >346.00 → >366.06 | Staged confirmation | Bounce → gap fill → short-term repair → strategic repair |
| **Risk levels** | Stop 305 (1×ATR below low) or 293.25 (2×ATR below close) | — | ATR-based; intraday noise ~12 pts |
| **Data caveat** | Snapshot MFI = 0.3115 | Excluded | Implausible for a 0–100 oscillator; likely scaling artifact — flagged, not used |