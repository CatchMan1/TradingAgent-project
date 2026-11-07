# GOOGL — Multi-Timeframe Technical Report
**Analysis date:** 2026-08-14 · **Last verified close:** 345.90 (session high 350.45 / low 344.50, volume 17,808,600)

All price levels and indicator values below come from the verified snapshot and indicator pulls for GOOGL as of 2026-08-14. Where I derive a percentage or an average, I show the arithmetic so it can be checked.

---

## 1. Where GOOGL stands right now

| Metric | Value (2026-08-14) | Read |
|---|---|---|
| Close | 345.90 | — |
| 10 EMA | 349.60 | Price **below** by 1.06% |
| 50 SMA | 353.89 | Price **below** by 2.26% |
| 200 SMA | 331.38 | Price **above** by 4.38% |
| VWMA | 353.30 | Price **below** by 2.09% |
| Bollinger mid / upper / lower | 346.41 / 378.16 / 314.66 | Price sits **0.15% below the midline**, %B ≈ 49 |
| RSI(14) | 47.04 | Neutral, no overbought/oversold |
| MACD line / signal / hist | −1.1369 / −0.9704 / −0.1665 | Bearish, freshly below zero |
| ATR(14) | 11.01 | 3.18% of price; contracting |

The single most useful framing: **GOOGL is in a long-term uptrend that is currently being digested by a medium-term corrective downtrend.** Price is trapped between a falling 50 SMA above and a rising 200 SMA well below, sitting almost exactly on the Bollinger midline.

---

## 2. Trend hierarchy

### Long-term (200 SMA) — intact and rising
The 200 SMA has climbed without interruption across the sample: 308.75 (2026-06-15) → 326.27 (2026-07-31) → 331.38 (2026-08-14), a slope of roughly **+0.38 points/day (~+1.9/week)**. Price at 345.90 is **+4.38% above it**. On a 12-month basis, close-to-close from 202.94 (2025-08-14) to 345.90 is **+70.4%**. Nothing in the data says the primary uptrend has broken.

### Medium-term (50 SMA) — rolling over, but decelerating
The 50 SMA peaked at **372.80 on 2026-07-13** and has fallen every session since, to **353.89**. That decline is decelerating: from Jul 13 to Jul 31 it averaged about −0.86/day, while over the last ten sessions (358.74 on Jul 31 → 353.89) it has averaged about **−0.48/day**. Structurally, the sequence of lower highs is visible in the closes: 402.62 (2026-05-13) → 370.92 (2026-07-15) → 377.65 (2026-08-04). The August bounce failed to exceed the May/June highs.

Important: the 50 SMA (353.89) remains **22.5 points above** the 200 SMA (331.38). With the 50 falling ~0.5/day and the 200 rising ~0.38/day, convergence is slow — a death cross is not a near-term event on current slopes, but the gap is narrowing and worth monitoring weekly.

### Short-term (10 EMA) — bearish
The 10 EMA at 349.60 is above price (345.90). Price has not closed above the 10 EMA since the Aug 5 reversal day. Short-term control belongs to sellers.

---

## 3. Momentum — deterioration, not capitulation

**MACD:** The line bottomed at −8.83 on 2026-07-27 during the July washout, surged to a peak of **+1.18 on 2026-08-10**, then rolled over and crossed **below zero on 2026-08-12** (−0.482). As of Aug 14 it is −1.1369 versus a signal of −0.9704, histogram −0.1665. That is a **fresh bearish crossover with only a small negative histogram** — early-stage momentum loss rather than a deep downside thrust. The August recovery impulse has been fully unwound on this measure.

**RSI:** 47.04, squarely neutral. It peaked at only **62.56 on 2026-08-04** — the August rally never reached overbought, which is itself a warning that the bounce lacked thrust. During the July collapse RSI bottomed at **31.02 (2026-07-23)**, just kissing the 30 threshold; that low was bought aggressively (see the ±20% recovery below), so the indicator's oversold signals have been short-lived in this regime. RSI at 47 leaves room in both directions — no edge from mean-reversion here.

---

## 4. Volatility — compressing after an event-driven spike

ATR has fallen from **13.93 (2026-08-05)** to **11.01 (2026-08-14)**, four straight sessions of contraction. At 3.18% of price, daily risk is still elevated in absolute terms (roughly 11 points), but the trend is clearly toward normalization.

Bollinger geometry tells the same story with more nuance:
- Upper band: 382.97 (Aug 10) → 381.88 (Aug 11) → 378.81 (Aug 12) → 378.16 (Aug 14) — **falling fast**
- Lower band: 314.57 (Aug 11) → 314.66 (Aug 14) — **flat**
- Bandwidth: (378.163 − 314.656) / 346.409 = **18.3% of the midline**

That is an extremely wide envelope (the product of the July gap and the August spike-and-reverse), and the upper band is now curling down toward a flat lower band — the first mechanical signature of a **volatility squeeze in formation**. A squeeze after such a wide envelope usually resolves directionally with a range expansion; the *direction* must be taken from price structure, not from the bands.

Note one clean confluence: the **lower band at 314.66 sits almost exactly on the 2026-07-23 intraday low of 314.90**. The market's July capitulation low and the statistically extreme lower band occupy the same ~0.25-point zone. That is the definitive line for the bear case.

---

## 5. Volume and VWMA — the most interesting divergence

Two volume facts matter:

1. **Participation has evaporated.** The last two sessions printed 17.87M and 17.81M shares. The 21-session average from 2026-07-17 through 2026-08-14 computes to roughly **31.2M** (sum ≈ 655.9M / 21). Current volume is therefore about **43% below** that average and the lowest since mid-July. Price is holding in the mid-340s on shrinking supply — a classic basing tell, though still unconfirmed.
2. **VWMA is above price and rising.** VWMA at 353.30 vs close 345.90 means the volume-weighted average transacted price of the recent window is **above** the current quote: on a volume-weighted basis, recent buyers are underwater. VWMA has also ticked up from 345.36 (Aug 10) to 353.30 (Aug 14) even as price fell — a mechanical artifact of heavy low-price July sessions (notably 2026-07-23's 69.4M shares at a 317.69 close) rolling through the window, not fresh accumulation. I would treat **353.30 as overhead supply**, not as evidence of demand.

**Event bars that define the current range (all confirmed from the OHLCV rows):**
- **2026-07-23 (bearish gap):** prior close 342.09 → open 321.13 → low 314.90 → close 317.69, on **69.4M** shares. A −7.2% close-to-close break. This gap was subsequently **filled** by the 2026-07-31 close of 356.13, and price overshot to 380.52 on 2026-08-04 — a **+20.8% recovery off the 314.90 low in eight sessions**.
- **2026-08-05 (bearish outside reversal):** open 383.34, high 384.48, close 362.43 — closing **below the prior day's low of 367.50** on 46.9M shares versus 35.7M the day before. This is the pivotal bar of the current setup and it marks 377.65–380.52 (Aug 4 close/high) as a validated lower high, with the 384.48 wick as the failure point.

---

## 6. Actionable levels

**Resistance (in order of proximity):**
1. **349.60** — 10 EMA; the first short-term hurdle
2. **353.30–353.89** — VWMA plus 50 SMA; the decisive confluence. A daily close above this band is required to repair the medium-term trend
3. **356.13–357.75** — Jul 31 close / Aug 6 close (prior shelf)
4. **377.65–380.52** — Aug 4 close/high, with **378.16** (upper band) reinforcing; **384.48** is the failure high
5. **402.62 / 403.70** — 2026-05-13 close/intraday high, the cycle peak

**Support:**
1. **343.54 / 340.88** — Aug 12 close / Aug 12–13 low cluster; the immediate pivot
2. **336.71** — Jul 29 close; gap-fill shelf
3. **331.38** — 200 SMA; the macro line in the sand
4. **314.66–314.90** — lower band / July capitulation low; the structural floor

---

## 7. Scenarios and trade construction

**Neutral/range (base case, highest probability):** Price oscillates 340–354 with the Bollinger midline at **346.41** acting as the pivot. RSI at 47, MACD only mildly negative, ATR contracting, and volume at multi-week lows all support chop rather than trend. Range traders can fade 353–354 toward 341 with tight risk; nothing in the data justifies size here.

**Bullish trigger (trend repair):** A daily close **above 353.89 (50 SMA)** accompanied by volume back above roughly 25–30M shares. Confirmation stack: 10 EMA reclaimed first (349.60), then MACD histogram turning positive, then RSI pushing through 55–60. Targets: **357.75**, then **377.65–378.16** (upper band). The full-recovery thesis is only alive above 384.48. The ATR-based stop under such an entry would sit approximately **1.5 × 11.01 ≈ 16.5 points** below entry, i.e. near 337 if entering at 353.5 — which conveniently sits just above the 200 SMA. That is a favorable structure: the stop and the macro trend line nearly coincide.

**Bearish trigger:** A decisive close below **340.88** on expanding volume. That would open **336.71** and then a test of the **200 SMA at 331.38** — the single most important level on the chart. Note that the 200 SMA is rising ~0.38/day, so it will be near ~334 in two weeks; the support is moving up to meet price, which slightly favors the bulls over time. A weekly close below the 200 SMA would invalidate the primary uptrend and put **314.66–314.90** in play.

**Risk management specifics:** With ATR at 11.01 (3.18% of price), a 1-ATR stop is ~11 points and a 2-ATR stop ~22 points. Bollinger bandwidth of 18.3% implies a two-standard-deviation daily envelope of roughly ±31 points around 346.41 — position size should be set so a 2-ATR adverse move is within tolerance. On the long side, avoid entries in the 346–350 no-man's-land: reward-to-risk is poor until either 341 support is defended with a reversal bar or 353.89 is reclaimed.

**What to watch next week:** (1) whether the 17.8M-share volume trough marks selling exhaustion or simply indifference — a down day on a volume surge would be bearish; (2) MACD histogram magnitude — a turn back toward zero without a deeper MACD decline would signal a failed bear cross; (3) the shrinking Bollinger envelope — the resolution bar is likely to be wide.

---

## 8. Caveats

- The MFI value carried in the verified snapshot (0.5695, i.e. ~57 on a 0–100 scale) is mildly constructive and does not contradict the price/volume read, but I did not select it as one of my eight and would not act on it alone.
- No indicator output here establishes historical support/resistance *bounces*; the levels above are zones where multiple tool-derived measures coincide, not tested-and-held floors.
- All figures are point-in-time as of the 2026-08-14 session; the indicator and snapshot sources agree exactly on the 50 SMA (353.894), MACD (−1.1369), RSI (47.039), upper band (378.163), lower band (314.656), ATR (11.007) and VWMA (353.301). No discrepancies were found between the two tool outputs.

---

## 9. Indicator selection rationale

I chose eight complementary measures spanning trend, momentum, volatility and volume, deliberately avoiding redundancy:

| Indicator | Why it fits this context |
|---|---|
| **close_200_sma** | Defines the primary trend that is still intact; the 331.38 level is the single most consequential line on the chart and it is rising. |
| **close_50_sma** | Captures the medium-term rollover (peak 372.80 on Jul 13 → 353.89) that price must reclaim to repair the trend. |
| **macd** | The cleanest read on the August impulse peaking and unwinding — peak +1.18 on Aug 10, zero-cross on Aug 12. |
| **rsi** | Confirms the August rally never reached overbought (62.56 max) and that RSI at 47 leaves no mean-reversion edge in either direction. Deliberately *not* paired with StochRSI to avoid redundancy. |
| **boll_ub** | Quantifies the failure zone at 377–384 and shows the band curling down — the squeeze signature. |
| **boll_lb** | Anchors the structural floor at 314.66, which coincides with the 2026-07-23 low of 314.90. |
| **atr** | Required for stop placement and sizing in a 3.2%-of-price volatility regime; also documents the four-session contraction from 13.93 to 11.01. |
| **vwma** | Detects the volume-weighted overhead supply at 353.30 (above price) and confirms the last two sessions' ~43%-below-average participation. |

Rejected as redundant: `close_10_ema` (captured via the snapshot and subsumed by MACD), `macds`/`macdh` (implied by MACD's position and provided in the snapshot), and `boll` middle (derivable from the two bands).

---

## 10. Summary table

| Dimension | Reading (2026-08-14) | Evidence | Implication |
|---|---|---|---|
| **Primary trend** | Bullish | 200 SMA 331.38, rising +0.38/day; price +4.38% above | Do not short the macro trend |
| **Intermediate trend** | Bearish / correcting | 50 SMA 353.89 vs peak 372.80 (Jul 13); price −2.26% below | Overhead resistance at 353–354 |
| **Short-term** | Bearish | Close 345.90 < 10 EMA 349.60 | No confirmed bottom yet |
| **Momentum** | Weakening | MACD −1.1369 < signal −0.9704; zero-cross Aug 12; RSI 47.04 | Early-stage erosion, not capitulation |
| **Volatility** | Contracting | ATR 13.93 (Aug 5) → 11.01 (Aug 14); bandwidth 18.3% | Squeeze forming — expect range expansion |
| **Volume** | Drying up | 17.81M on Aug 14 vs ~31.2M 21-session avg (−43%) | Possible basing; needs confirmation |
| **Volume-price** | Negative | VWMA 353.30 > close 345.90 | Recent buyers underwater; supply overhead |
| **Key reversal bar** | 2026-08-05 | Open 383.34, high 384.48, close 362.43 < prior low 367.50 on 46.9M | 377.65–384.48 is a validated lower high |
| **Pivot / fair value** | 346.41 | Bollinger midline; price 0.15% below | Choppy range 340–354 base case |
| **Resistance** | 349.60 → 353.30–353.89 → 356–358 → 377.65–380.52 → 402.62 | MAs, VWMA, Aug highs, May peak | Close above 353.89 = trend repair |
| **Support** | 340.88–343.54 → 336.71 → 331.38 → 314.66–314.90 | Aug lows, Jul shelf, 200 SMA, lower band/Jul low | Below 331.38 breaks the primary trend |
| **Bull trigger** | Daily close > 353.89 on >25–30M shares | 50 SMA + VWMA confluence | Targets 357.75, then 378 |
| **Bear trigger** | Daily close < 340.88 on rising volume | Aug 12–13 low cluster | Targets 336.71, then 331.38 |
| **Risk unit** | ATR 11.01 (3.18%) | 1-ATR ≈ 11 pts, 2-ATR ≈ 22 pts | Size positions to 2-ATR tolerance |
| **Stance** | **Neutral / wait** | Conflicting trend layers, neutral RSI, low volume | Trade the 341–354 edges, not the middle |