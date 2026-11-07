# AMZN — Multi-Timeframe Technical Analysis
**Analysis date: 2026-08-06 (close) — Last verified print: $272.26**

Data integrity note: `get_stock_data` (190 rows, 2025-11-03 → 2026-08-06) and `get_verified_market_snapshot` (2026-08-06) agree exactly on the final row (O 272.77 / H 275.48 / L 271.06 / C 272.26 / V 30,672,900). Every indicator value returned by `get_indicators` matches the snapshot to the decimal (RSI 63.195, MACD 6.8312, MACD hist 4.3613, ATR 9.5854, VWMA 254.9519, 50-SMA 247.4544, 200-SMA 236.2466, 10-EMA 260.8727). **No discrepancies to flag.**

---

## 1. The single most important fact on the chart

Between the 2026-07-30 close ($235.50) and the 2026-07-31 session, AMZN **gapped up and closed at $271.58** — a **+15.32% single-session move** on **129.05M shares**, versus 44.96M on 2026-07-29 (≈2.9x). The 2026-07-31 low of $262.01 is wholly above the 2026-07-30 high of $239.82, leaving an **unfilled gap of ~$22.19 (9.4% of the pre-gap close)**. This is an event-driven repricing (earnings-type gap), not a drift.

Three sessions later the price path is:

| Date | Close | High | Low | Volume |
|---|---|---|---|---|
| 2026-07-30 | 235.50 | 239.82 | 231.06 | 101,839,800 |
| 2026-07-31 | 271.58 | 273.23 | 262.01 | 129,054,800 |
| 2026-08-03 | **284.02** | **287.20** | 278.00 | 90,830,200 |
| 2026-08-04 | 277.42 | 281.07 | 275.82 | 69,748,100 |
| 2026-08-05 | 272.65 | 282.79 | 270.73 | 45,119,800 |
| 2026-08-06 | 272.26 | 275.48 | 271.06 | 30,672,900 |

The **$284.02 close on 2026-08-03 is the highest close in the entire dataset** (previous high close $274.99 on 2026-05-06; previous intraday high $278.56 on 2026-05-05). AMZN then gave back **−4.14%** from that record close to $272.26, and — critically — **closed back below the prior six-month range ceiling of ~$275–278.5**. The breakout is *printed but not yet confirmed on a closing basis.*

---

## 2. Selected indicators (8) and why each earns its slot

The regime is **post-event volatility expansion inside an intact long-term uptrend, at the apex of a six-month base**. That dictates a mix of (a) multi-horizon trend anchors, (b) momentum-regime detectors that can survive a gap, (c) a volatility unit for stop sizing, and (d) a volume-weighted reference to test whether the gap was sponsored by real money.

| # | Indicator | Why this one, in this context |
|---|---|---|
| 1 | **close_10_ema** | The only average fast enough to trace the post-gap trend. It has already vaulted from 236.29 (07-30) to 260.87 (08-06) and is the first dynamic line that will validate or fail the breakout. |
| 2 | **close_50_sma** | Medium-term pivot that **just inflected upward** (246.38 on 07-30 → 247.45 on 08-06) after declining from 257.10 on 06-18. Inflection under a fresh breakout is a classic confirmation signature. |
| 3 | **close_200_sma** | Long-term benchmark. Price is 15.2% above it and the line is rising (236.25 vs 234.66 on 07-29), so this is trend *confirmation*, not a battleground. Also anchors the golden-cross structure (50 > 200 by $11.21). |
| 4 | **macd** | Best detector of the momentum *regime flip*: MACD went from −3.75 (07-29) to +6.83 (08-06), a +10.6-point swing in five sessions. |
| 5 | **macdh** | Added instead of `macds` to avoid a redundant third MACD line while capturing *momentum acceleration*. The histogram data embeds the signal-line relationship and is already showing the first deceleration (4.62 on 08-05 → 4.36 on 08-06). |
| 6 | **rsi** | The gap created a rare 3-session oversold→overbought whipsaw (33.3 → 72.2), so RSI is currently the cleanest read on whether buying pressure is exhausting or merely resetting. |
| 7 | **atr** | Indispensable here: ATR jumped from 6.89 (07-29) to 9.59 (08-06), **+39%**, i.e. 3.52% of price. Every stop and size calculation below is denominated in ATR, not in fixed percentages. |
| 8 | **vwma** | The gap was a volume event. VWMA at 254.95 vs a 272.26 close (+6.78%) tells us the *volume-weighted* cost basis is far below spot — both a sponsorship signal and a magnet on any deeper pullback. |

*Supporting (from the verified snapshot, not counted in the eight): Bollinger middle 250.14, upper 284.28, lower 215.99; MFI 47.2.*

**Deliberately excluded:** `close_50_sma` vs `boll` are near-duplicates in a 20/50 pair (the middle band is essentially a 20-SMA at 250.14 vs the 50-SMA at 247.45 — I use the bands only as a volatility envelope, not as a second trend line). No stochastics/StochRSI (would double-count RSI). No `macds` as a standalone (its information is already in `macdh`).

---

## 3. Trend structure — bullish alignment, but stretched

**Full stack is bullish and correctly ordered:** Close 272.26 > 10-EMA 260.87 > VWMA 254.95 > Bollinger mid 250.14 > 50-SMA 247.45 > 200-SMA 236.25.

| Measure | Value | Read |
|---|---|---|
| Price vs 10-EMA | **+4.37%** | Short-term extended but within one ATR |
| Price vs 50-SMA | **+10.03%** | Moderately stretched; mean-reversion risk |
| Price vs 200-SMA | **+15.24%** | Strong primary uptrend, historically extended |
| Price vs VWMA | **+6.78%** | Volume-weighted buyer base well underwater-to-profit; pullback magnet |
| 10-EMA vs 50-SMA | +13.42 pts | Fast line leading — momentum, not trend decay |
| 50-SMA vs 200-SMA | +11.21 pts | Golden-cross structure intact |

**The six-month picture matters more than the daily stack.** AMZN spent roughly February–July 2026 in a wide base bounded by the 2026-02-13 close low of $198.79 (intraday $196.00 on 2026-02-17) and the 2026-05-06 close high of $274.99 (intraday $278.56 on 2026-05-05). Inside that base it ran a full cycle: −17.45% from 274.99 (05-06) to 227.01 (06-25), then **+25.1%** from 227.01 to the 284.02 record close on 08-03. The 07-31 gap drove price above the top of that six-month range for the first time — that is the strategic event. But the 08-06 close of $272.26 is **back inside the old range ceiling**, which is exactly the ambiguity a trader must price.

**Trend verdict:** Primary trend up, intermediate trend up and accelerating, short-term trend in a post-gap digestion phase. The 50-SMA turning up on 08-06 while the 200-SMA accelerates (+1.59 points in the six sessions from 07-29 to 08-06 vs a much flatter June slope) is genuine, hard confirmation — those are slow lines that do not fake inflection.

---

## 4. Momentum — powerful flip, first signs of fatigue

- **MACD** crossed above its signal on **2026-07-31** (MACD −0.62 vs signal −1.84), a textbook gap-driven bullish crossover, and has extended to **6.83 vs 2.47** (histogram +4.36).
- **But the histogram has already peaked:** 1.21 (07-31) → 3.66 (08-03) → 4.58 (08-04) → **4.62 (08-05) → 4.36 (08-06)**. Two consecutive prints of flattening/decreasing upside acceleration. This is *early* — one to two sessions old — but it argues against chasing the current price and in favour of either a defined pullback entry or a volume-confirmed breakout entry.
- **RSI 63.20.** It tagged **72.23 on 2026-08-03** (mildly overbought), then eased to 67.04 → 63.49 → 63.20. A cooling RSI that stays above 60 with price holding above the 10-EMA is the *healthy* version of overbought-unwind. Contrast with 2026-07-29's **33.31** — the indicator travelled 38.9 points in three sessions. **Practical implication: RSI's mean-reversion signal is currently unreliable; use it only as momentum confirmation.** A fresh push above ~70 with a new price high would be the "strong trend rides the band" case; a drop below ~50 would confirm the breakout is failing.

---

## 5. Volatility & Bollinger envelope — an extreme, and therefore likely transient, expansion

- **ATR 9.59** vs 6.89 on 2026-07-29 = **+39.2%** in six sessions. ATR is 3.52% of the $272.26 close.
- **Band width = 68.29 points** (upper 284.28 − lower 215.99) around a middle of 250.14 → **27.3% of the mean.** On 2026-07-30 the same measure was 31.22 points on a 242.41 middle = **12.9%.** Band width has more than doubled in four sessions.
- **Close sits at the 82.4th percentile of the envelope** ((272.26 − 215.99) / 68.29). It is 4.4% below the upper band — not riding it, not rejected by it.

Interpretation: when the envelope expands this violently it usually *contracts* afterward. Two paths: (a) price consolidates sideways/time-wise until the 20-day mean (250.14, rising fast: 243.86 → 250.14 between 07-31 and 08-06) catches up, or (b) the whole gap unwinds back toward that mean. Path (a) is currently favoured by the declining-volume pullback. The expanded band also means **the upper band at 284.28 is not a hard resistance level** — it is a moving target that will be at a materially different price within a week.

---

## 6. Volume — the strongest single argument that this pullback is not distribution

The post-gap volume sequence is a clean monotonic decay:

**129.05M (07-31) → 90.83M (08-03) → 69.75M (08-04) → 45.12M (08-05) → 30.67M (08-06).**

The 2026-08-06 volume is **76% below the gap-day volume** and is among the lowest prints in the three months preceding the gap (comparable to 27.73M on 2026-07-21 and 29.65M on 2026-07-08). Price gave back 4.14% from the record close on **shrinking** volume — the classic signature of profit-taking and absence of supply rather than institutional liquidation. If the gap were a bull trap, you would expect heavy volume on the red candles; that is not what the tape shows.

**VWMA confirms sponsorship:** it has risen every session since 2026-07-30 (240.82 → 245.72 → 250.17 → 252.45 → 253.80 → **254.95**), meaning the volume-weighted centre of trade is climbing fast. That is the fingerprint of accumulation, not churn. The flip side: price at +6.78% over VWMA means the average recent buyer is sitting on a large gain, which creates reflexive supply at the first sign of trend failure.

**One caution from the snapshot:** MFI 47.2 — neutral money flow, *not* confirming a strong-highs breakout. This is a mild non-confirmation worth watching; it often resolves within a few sessions after an event gap, but it argues against assuming immediate continuation.

---

## 7. Precise level map

| Level | Price | Source / date | Character |
|---|---|---|---|
| Bollinger upper | 284.28 | 2026-08-06 value | Rising, soft resistance |
| Record close | **284.02** | 2026-08-03 | Key breakout-validation trigger |
| Intraday high | **287.20** | 2026-08-03 | Hard resistance / stop-run level |
| Prior range ceiling | 278.56 / 274.99 | 2026-05-05 high / 2026-05-06 close | **Needs a close above to confirm breakout** |
| Recent close shelf | 277.42 / 272.65 | 2026-08-04 / 08-05 | Immediate battle zone |
| 07-31 close | 271.58 | 2026-07-31 | Being tested right now |
| **Immediate pivot** | **271.06** | 2026-08-06 low | First line of defence |
| 10-EMA | 260.87 | rising ~2.5/day | Primary trailing support |
| Gap top / 07-31 low | **262.01** | 2026-07-31 | Line in the sand for the breakout |
| 1×ATR below close | 262.67 | 272.26 − 9.59 | Coincides with gap top — high-confluence |
| VWMA | 254.95 | 2026-08-06 | Volume-weighted magnet |
| Bollinger mid | 250.14 | 2026-08-06 | Time-based mean |
| 50-SMA | 247.45 | 2026-08-06 | Trend-defining support |
| 200-SMA | 236.25 | 2026-08-06 | Bull-market floor |
| Gap fill low | 239.82 | 2026-07-30 high | Full-gap-fill scenario |

Note the **tight confluence cluster at 247–263** (50-SMA, Bollinger mid, VWMA, gap top, 1-ATR) — roughly 3.5% to 9.1% below spot. That is where a real test of the breakout would occur, and it is unusually well-defined, which makes it a high-quality area for a risk-defined long entry or for stop placement *behind* rather than *at* the market.

---

## 8. Actionable scenarios

**A. Bull continuation (primary, but needs proof).**
Trigger: a **close above ~$278.5** (reclaiming the prior range ceiling) with volume **above ~60M** — i.e. at least half the gap-day participation. Then the extension targets are $284.02 (record close), $287.20 (07-03 high), and the rising upper band (~284–290). Trail with the 10-EMA, which is ascending roughly 2.5 points per session and should reach ~265–268 within three sessions. Do **not** buy simply because MACD is positive — the histogram is already rolling over.

**B. Flag consolidation (highest-probability near term).**
Range **~$271–$284** for another 3–8 sessions while the 10-EMA climbs and the Bollinger width contracts. Play the edges, not the middle: buy the $271–262 zone with a stop, or fade $284–287 against the record high. ATR of 9.59 means the daily noise alone is ±3.5%, so entries within $2–3 of a level are effectively level-less.

**C. Failed gap (the tail that matters).**
A **close below $262.01** invalidates the 07-31 gap structurally. Path then opens to **$254.95 (VWMA) → $250.14 (Boll mid) → $247.45 (50-SMA)**, with a full gap-fill at $239.82 as the terminal target (−11.9% from spot). Note that a full gap fill would still leave price above the 200-SMA at 236.25 — so even this bearish scenario is technically a **bull-market pullback**, not a trend reversal. That asymmetry is important: the downside case is deep but non-structural.

**Precedent for event risk (both directions, from the data):** 2026-02-04 close 232.99 → 2026-02-06 close 210.32 = **−9.7% over two sessions** on 179.2M shares. This name has delivered two ~10%+ event gaps (Feb down, Jul up) within six months. Any position must be sized for that.

---

## 9. Risk management specifics

Using ATR 9.59 (verified 2026-08-06):

- **New long from spot $272.26:** 1.5×ATR stop = **$257.88** (just under VWMA, inside the gap zone — vulnerable to noise). Preferred: 2×ATR stop = **$253.08**, or a close-based stop under **$262.01** if swing-trading the gap edge.
- **Position sizing:** at 3.52% daily ATR, a portfolio risking 1% per trade implies a position size roughly **half** of what the same 1% risk would permit in a 1.7%-ATR regime. Halve normal unit size until ATR mean-reverts toward ~7.
- **Asymmetric, event-aware setup:** the confluence zone $247–262 offers a tighter stop (below $245) for a similar upside target — better reward-to-risk than entering at $272 mid-range. Patience is the edge here.
- **Gap risk:** the 07-31 gap is unfilled. Any entry above $262 carries gap-fill risk to the downside; any short above $284 carries gap-and-go risk to the upside. There is no "safe" side of this specific structure — only well-defined invalidation.

---

## 10. Key points summary

| Dimension | Observation | Evidence (date / value) | Signal |
|---|---|---|---|
| **Regime** | Event-driven volatility expansion | 2026-07-30 close 235.50 → 07-31 close 271.58 = +15.32% | Post-shock digestion |
| **Primary trend** | Up, intact | Close 272.26 vs 200-SMA 236.25 (+15.24%), 200-SMA rising | **Bullish** |
| **Intermediate trend** | Up and freshly re-accelerating | 50-SMA inflected: 246.38 (07-30) → 247.45 (08-06) | **Bullish** |
| **Short-term trend** | Pullback within uptrend | −4.14% from 284.02 (08-03) to 272.26 (08-06) | Neutral / digesting |
| **MA alignment** | Perfectly stacked | 272.26 > 10-EMA 260.87 > VWMA 254.95 > 50-SMA 247.45 > 200-SMA 236.25 | **Bullish** |
| **Breakout status** | Printed but unconfirmed | 08-06 close 272.26 < prior range ceiling 274.99/278.56 | **Unresolved** |
| **MACD** | Sharp bullish flip, momentum cresting | 6.83 vs signal 2.47; hist 4.62 (08-05) → 4.36 (08-06) | Bullish, decelerating |
| **RSI** | Cooled from overbought, healthy | 72.23 (08-03) → 63.20 (08-06); low 33.31 (07-29) | Constructive, not extreme |
| **Bollinger** | Extreme expansion, price at 82nd pct | Upper 284.28 / mid 250.14 / lower 215.99; width 27.3% vs 12.9% on 07-30 | Volatility likely to contract |
| **ATR** | Expanded 39% in six sessions | 6.89 (07-29) → 9.59 (08-06) = 3.52% of price | Halve position size |
| **Volume** | Decaying pullback = no distribution | 129.05M → 90.83M → 69.75M → 45.12M → 30.67M | **Bullish** |
| **VWMA** | Sponsorship confirmed, price extended | 240.82 (07-30) → 254.95 (08-06); price +6.78% above | Bullish w/ magnet below |
| **Money flow (snapshot)** | Neutral, non-confirming | MFI 47.2 | Mild caution |
| **Immediate pivot** | $271.06 (08-06 low) | Must hold to keep near-term bid | Watch |
| **Invalidation** | Close below $262.01 | Gap top / 07-31 low | Breakout fails |
| **Upside trigger** | Close above $278.5 on >60M volume | Prior range ceiling | Confirmation |
| **Risk unit** | 1×ATR = $9.59 | 1.5ATR stop 257.88 / 2ATR stop 253.08 | Size down |

**Bottom line:** AMZN executed a genuine, high-volume breakout from a six-month base on 2026-07-31 and printed a record close of $284.02 on 2026-08-03, with every trend and volume measure now confirming an intact uptrend. The current three-session −4.14% retreat is occurring on *collapsing* volume — the bullish interpretation — but it has left price back *inside* the old range ceiling at $272.26, with the MACD histogram cresting and price 10% above its 50-SMA. The trade is therefore **constructive but not chase-able**: the higher-quality entries are either a volume-confirmed close above $278.5, or a disciplined bid in the $247–262 confluence zone where the 50-SMA, Bollinger mid, VWMA and gap top all cluster. A close below $262.01 is the unambiguous signal that the gap has failed.

*Analysis is based on frozen, point-in-time data through the 2026-08-06 session; all price, volume and indicator values are as returned by the verified snapshot and indicator tools, with no interpolated or estimated figures.*