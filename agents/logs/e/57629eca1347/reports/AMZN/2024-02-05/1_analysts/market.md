# AMZN — Multi-Timeframe Technical Report
**As of the close of 2024-02-05 | Verified snapshot source: `get_verified_market_snapshot(2024-02-05)`**

---

## 1. Data Integrity Check

The OHLCV row for 2024-02-05 returned by `get_stock_data` and by the verified snapshot are **identical** (close 170.31, volume 55,081,300), and every indicator value at 2024-02-05 in the `get_indicators` histories matches the snapshot exactly (e.g., `close_50_sma` = 152.0884 in both). **No discrepancy to flag** on price or indicator values.

One caveat: the snapshot also returns `mfi` = **0.690601**, which is on a 0–1 scale rather than the conventional 0–100 Money Flow Index scale. I could not resolve the scaling from the tool output, so I am **not** using MFI in this analysis — treating it as unverified rather than inventing an interpretation.

---

## 2. Regime Classification

AMZN is in a **confirmed, accelerating uptrend that just received a volume-backed event-driven re-rating** (the 2024-02-02 post-earnings session). It is simultaneously **short-term extended** across nearly every stretch metric. This is the classic "strong trend, poor entry" configuration: the tape is bullish, but price is far from any mean that could act as support.

Key structural facts directly from the data:

| Event | Date | Numbers |
|---|---|---|
| Pre-earnings close | 2024-02-01 | 159.28 |
| Gap open | 2024-02-02 | 169.19 (**+6.22%** vs prior close) |
| Gap-day range | 2024-02-02 | High 172.50 / Low 167.33 / Close 171.81 (**+7.87%**) |
| Gap-day volume | 2024-02-02 | **117,218,300** (2.33× the 20-session average of ≈50.2M) |
| Follow-through day | 2024-02-05 | Close 170.31 (**−0.87%**), high 170.55, low 167.70, volume 55.08M (1.10× avg) |

The follow-through session is the most informative single row: **it held above the entire gap-day range's lower half and never traded below 167.70, which is above the 2024-02-02 low of 167.33**, and it did so on volume that was barely above average — i.e., **no distribution**. A failed gap typically shows a close below the gap-day low on expanding volume. That did not happen.

---

## 3. Indicator Selection (8 selected, with rationale)

| # | Indicator | Why it is the right tool here |
|---|---|---|
| 1 | **close_50_sma** | The intermediate trend spine and the natural pullback magnet after a +12% extension. Confirms trend slope rather than just direction. |
| 2 | **close_200_sma** | Long-term benchmark; needed to quantify how far the trend is from its structural mean (a real risk input at +26.8%). |
| 3 | **close_10_ema** | Fastest trend line available; the correct first "does the thrust survive?" reference for a post-gap tape. |
| 4 | **macd** | Level of trend momentum; tells us whether the Feb-2 event was a genuine regime shift or a spike. |
| 5 | **macdh** | Preferred over `macds` because it encodes **both** the crossover and the *acceleration* — the single most important thing to monitor after a momentum thrust (I pulled `macds` as well: 2.8364). |
| 6 | **rsi** | The only tool that quantifies the overbought stretch and, crucially, whether momentum is diverging from price. |
| 7 | **boll_ub** | Price is *above* it. In a breakout regime the upper band stops being a sell signal and becomes a strength/trapped-position gauge — this is the key ambiguity to resolve, so it gets a slot. |
| 8 | **atr** | Volatility has structurally repriced (3.16 → 3.90). Any stop or size decision must be ATR-derived, not fixed-dollar. |

**Deliberately excluded:** `boll_lb` and `boll` (used as cross-checks only — the middle at 156.96 and lower at 145.63 are cited below but are not primary signals), `macds` (redundant with `macdh`), `mfi` (scaling unresolved). **`vwma` was pulled as the volume cross-check** and is discussed in §7 — it is the one indicator I would add if a ninth slot existed.

---

## 4. Trend Structure

**Long term (200 SMA): bullish and steepening.**
`close_200_sma` has risen **every session in the visible window**: 128.9403 (2024-01-08) → 134.2836 (2024-02-05), i.e. **+5.34 (+4.14%) in 20 sessions**. A 200-day average moving 4.1% in a month is a statistical tell of a powerful primary uptrend. Price at 170.31 sits **+26.83% above** it (170.31 / 134.2836).

**Intermediate term (50 SMA): bullish, and the spread is widening — this is the highest-quality signal in the dataset.**
`close_50_sma`: 145.1902 (2024-01-08) → 152.0884 (2024-02-05), **+6.90 (+4.75%)**, rising monotonically for 20 consecutive sessions. The 50/200 spread has expanded from **+16.25** on 2024-01-08 to **+17.81** on 2024-02-05. A widening — not flattening — 50/200 spread means the golden-cross configuration is *maturing*, not topping. Note the 50 SMA is far below price (+11.98% extension), which is both confirmation of trend and the source of air-pocket risk.

**Short term (10 EMA): parabolic.**
`close_10_ema`: 157.2184 (2024-02-01) → 159.8715 (2024-02-02) → **161.7694 (2024-02-05)**. That is a +2.9% two-session jump in the EMA itself — a rate of change the series has not shown elsewhere in the window. Price is **+5.28% above** the 10 EMA. This is the signature of a thrust day, and it means the 10 EMA is *chasing* price rather than supporting it; it is not yet usable as a stop.

**Stacking:** price 170.31 > 10EMA 161.77 > 50SMA 152.09 > 200SMA 134.28 — a fully ordered bullish stack on all three horizons. **There is no trend-configuration conflict in this chart.** The only question is price.

---

## 5. Momentum

**MACD has re-accelerated to the strongest reading in the sample.**
- `macd`: 2.4503 (2024-02-01) → 3.4647 (2024-02-02) → **4.1003 (2024-02-05)**
- `macds`: 2.2844 → 2.5204 → **2.8364**
- `macdh`: 0.1659 → 0.9442 → **1.2639**

Three things matter here:

1. **The histogram peak of 1.2639 is more than double the prior local peak of 0.5980 (2024-01-29).** This is not a re-test of old momentum; it is a new momentum regime.
2. **There was a genuine momentum fade immediately before the event, and it was resolved upward.** `macdh` decayed from 0.5980 (2024-01-29) → 0.5020 (2024-01-30) → 0.1528 (2024-01-31) → 0.1659 (2024-02-01). A lot of traders would have read that as a roll-over. The earnings gap destroyed that read. The lesson for position management: **the Jan-31 fade was noise in a rising-trend tape, not a top.**
3. **The MACD crossover itself is young.** `macdh` first turned positive on 2024-01-12 (+0.0937), briefly went negative 2024-01-17/18 (−0.0392 / −0.0120), and re-crossed on 2024-01-19. So the current signal is a *re-acceleration of a 3-week-old bullish cross* — historically the higher-quality version of a MACD signal, because it has already survived one shakeout.

**RSI: overbought, but without divergence — which is the crucial distinction.**
`rsi`: 70.4061 (2024-01-29) → 63.0924 (2024-01-30) → 53.1036 (2024-01-31) → 60.3601 (2024-02-01) → **73.7790 (2024-02-02)** → **70.6937 (2024-02-05)**

- The Jan-29 → Jan-31 collapse from 70.41 to 53.10 **reset** the oscillator without breaking price structure (the Jan-31 close of 155.20 held well above the Jan-17 swing low of 149.91). That reset is precisely why RSI had room to reach 73.78 on the gap rather than stalling at 70.
- **Price made a higher high (172.50 on 2024-02-02 vs 161.73 on 2024-01-30) and RSI made a higher high (73.78 vs 70.41). No bearish divergence exists yet.** The slip to 70.69 on 2024-02-05 accompanies a lower close — that is mechanical, not a divergence.
- Actionable read: RSI > 70 in a confirmed uptrend with rising 50/200 spread is a **continuation filter, not a sell signal**. The signal to watch is a *lower* RSI high on a *higher* price high — that has not occurred.

---

## 6. Volatility and Bollinger Positioning

- `boll` (20 SMA): **156.9555**
- `boll_ub`: **168.2833** (up from 163.0982 on 2024-02-01 — an aggressive expansion)
- `boll_lb`: **145.6277**
- Bandwidth: **14.43%** of the middle band.
- **Close 170.31 is +2.03 (+1.20%) ABOVE the upper band.**

This is the single most two-sided fact in the report. Closing above the upper band means one of two things, and the tape has not yet told us which:
- **Riding-the-band breakout** (bullish): `boll_ub` expanding from 163.10 → 166.33 → 168.28 over three sessions is textbook volatility expansion into a breakout, and bands that expand while price stays outside them usually indicate institutional demand, not exhaustion.
- **Statistical stretch** (mean-reversion risk): a close >2σ above the 20-SMA has negative short-horizon expectancy *on average*, and the 20-SMA at 156.96 is **−7.8%** below the current price.

Note also that the **lower band barely moved** (145.07 on Feb 2 → 145.63 on Feb 5) while the upper band exploded. That asymmetry is volatility skew to the upside — a directional breakout signature, not a symmetric squeeze.

**ATR is the risk-management anchor:**
`atr`: 2.9654 (2024-01-30) → 3.0536 (2024-01-31) → 3.1612 (2024-02-01) → 3.8797 (2024-02-02) → **3.8961 (2024-02-05)**.

ATR has repriced **+31.4%** since 2024-01-30 and now equals **2.29% of price**. Practical consequences:
- **2×ATR = 7.79 points.** A trend-following stop on a position entered near 170.31 lands at **≈162.52** — which sits almost exactly on the 10 EMA (161.77) and just above the Feb-1 breakout close (159.28). That is a *coherent* stop: it invalidates the gap structure, not just the entry day.
- **Any fixed-percentage stop tighter than ~1.8% will be noise-stopped.** The 2024-02-02 gap-day low (167.33) is only **0.77 ATR** below the current close. Placing a stop there is arithmetically likely to be triggered by ordinary volatility.

---

## 7. Volume Confirmation

No volume indicator was in my primary 8, so I pulled `vwma` as the cross-check. It is strongly confirming:

- `vwma`: 156.4213 (2024-02-01) → 158.7868 (2024-02-02) → **159.8866 (2024-02-05)**
- **VWMA (159.89) is +5.13% above the 50 SMA (152.09).**

This is the confirmation that matters. A simple average treats the 117.2M-share session the same as a 34.9M-share session; the VWMA does not. The fact that the volume-weighted average sits **7.80 points above** the simple one means the recent high-volume sessions printed at **higher** prices — i.e., large buyers, not large sellers. A gap-up distributed into would have pulled VWMA *below* the 50 SMA, not above it.

Volume details:
- 20-session average: **≈50.2M** (computed from the 20 rows 2024-01-08 → 2024-02-05).
- 2024-02-02: 117.22M = **2.33×** average — genuine institutional participation.
- 2024-02-05: 55.08M = **1.10×** average — mild, orderly consolidation. **A −0.87% give-back on 1.1× volume is not distribution.** Distribution would look like a down 2%+ day on 1.5×+ volume.

---

## 8. Key Levels (all derived from tool output; no invented levels)

| Level | Value | Source | Role |
|---|---|---|---|
| **Resistance / breakout pivot** | **172.50** | 2024-02-02 high — highest print in the entire 2023-08-01→2024-02-05 window | Trigger for continuation |
| Gap-day intraday high | 170.55 | 2024-02-05 high | Immediate micro-resistance; price closed 0.24 below it |
| **First support (gap floor)** | **167.33** | 2024-02-02 low | The line a failed gap must break; also 0.77 ATR away |
| Gap-fill / 10 EMA confluence | 161.77 | `close_10_ema` | Trend-intact pullback zone |
| Breakout shelf | 159.76–159.89 | 2024-02-01 high 159.76; `vwma` 159.8866 | Deeper buy zone; VWMA and the pre-gap high agree |
| **Structure break** | **155.20** | 2024-01-31 close (low 154.81) | Below this, the post-earnings structure is broken |
| Bollinger middle | 156.9555 | `boll` | Same neighborhood as above; add as confluence |
| **Trend invalidation** | **152.0884** | `close_50_sma` | The intermediate trend is intact above this |
| 200 SMA | 134.2836 | `close_200_sma` | +26.8% away — not tradable as support |

---

## 9. Actionable Scenarios

**Base case (bullish continuation, needs confirmation):**
The ordered MA stack, maximally-wide 50/200 spread, fresh MACD thrust at a 2× prior-peak reading, higher RSI high with no divergence, and VWMA above the 50 SMA all point the same way. **The trigger is a daily close above 172.50** accompanied by volume at or above the 50.2M average. Until that happens, price is coiling between 167.33 and 172.50. There is **no visible resistance above 172.50 anywhere in the available data window**, so a confirmed break has no measured overhead supply to fight.

**Pullback-buy case (preferred risk/reward):**
Because price is **+11.98% above the 50 SMA**, **+5.28% above the 10 EMA**, and **+1.20% above the upper Bollinger band**, buying at 170.31 is chasing. The two high-quality scaled-entry zones:
- **Zone 1 — 167.33 to 163.00:** a retest of the gap-day low that holds. Confirmation = a reversal close back above 167.33 with volume below the average (i.e., a quiet retest).
- **Zone 2 — 159.76 to 161.77:** the 10 EMA plus the VWMA plus the 2024-02-01 pre-gap high. This is the highest-conviction confluence in the chart: three independent measures within 1.3% of each other.

**Invalidation / exit:**
- **First warning:** a daily close below **167.33** on volume ≥1.5× average. That converts the gap into a failed breakaway gap.
- **Structural break:** a close below **155.20–156.96** (Jan-31 close / Bollinger middle). At that point the entire post-earnings re-rating is undone and the Jan-17 low of 149.91 becomes the next reference.
- **Trend damage:** a close below the **50 SMA at 152.09** — but note this is 11% lower, so it is a *strategic* stop, not a trading stop.

**Position-sizing discipline:** with ATR at 3.8961 (2.29% of price), size positions off the ATR stop distance (≈7.79 points / 4.6%), not off a dollar target. Two-thirds of the current ATR increase occurred in a single session (3.1612 → 3.8797 on 2024-02-02), so realized volatility is likely to *stay* elevated for 5–10 sessions — do not revert to pre-earnings sizing.

---

## 10. Risks to This Read

1. **Event-driven gaps mean-revert more often than trend gaps do.** The Feb-2 move was an earnings re-rating, and earnings gaps lack the multi-week accumulation base that produces durable breakouts. The 2024-02-05 session (close 170.31, inside the gap range, on light volume) is unresolved — it neither confirms nor refutes.
2. **Every stretch metric is simultaneously elevated** (−1.20% outside the upper band, RSI 70.69, +5.28% over the 10 EMA, +11.98% over the 50 SMA, +26.83% over the 200 SMA). Correlated stretch readings do not diversify each other; a mean-reversion snap would hit all of them at once.
3. **RSI at 73.78 on 2024-02-02 is only the second-highest reading in the window** — the stock has already shown it can run to 70+ and then reset hard (70.41 → 53.10 in two sessions, Jan 29 → Jan 31). That precedent argues for a *breather*, not necessarily a reversal.
4. **A single missing prior high is not proof of open air.** The dataset begins 2023-08-01. "No resistance above 172.50" is a statement about *this window only*, not about the security's full history.
5. **MFI could not be verified** (0.69 on an ambiguous scale) and is excluded — if a money-flow confirmation is required, treat it as absent rather than supportive.

---

## 11. Summary Table

| Dimension | Reading (2024-02-05) | Signal | Actionable interpretation |
|---|---|---|---|
| **Close / OHLC** | 170.31 (O 170.20, H 170.55, L 167.70) | Neutral-to-bullish | Held gap floor 167.33; closed just under 170.55 high |
| **Volume** | 55.08M (1.10× 20-day avg ≈50.2M) | Healthy | −0.87% pullback on light volume = no distribution |
| **200 SMA** | 134.2836, +4.14% in 20 sessions | **Bullish** | Primary uptrend confirmed; price +26.83% above |
| **50 SMA** | 152.0884, +4.75% in 20 sessions, 20 consecutive rises | **Strongly bullish** | 50/200 spread widening 16.25 → 17.81 |
| **10 EMA** | 161.7694 (+2.9% in 2 sessions) | Bullish but parabolic | Chasing price; not yet a valid stop reference |
| **MACD / Signal** | 4.1003 / 2.8364 | **Bullish** | Cross 3 weeks old, survived a Jan-17/18 shakeout |
| **MACD Histogram** | 1.2639 | **Strongly bullish** | 2.1× the prior peak of 0.5980 (Jan 29); momentum re-accelerating |
| **RSI** | 70.6937 (73.7790 on Feb 2) | Overbought, no divergence | Continuation filter in this regime; watch for lower RSI high on higher price high |
| **Bollinger UB / Middle** | 168.2833 / 156.9555 | Breaking out but stretched | Price +1.20% above UB; UB expanded 163.10 → 168.28 in 3 sessions |
| **Bollinger LB** | 145.6277 (flat) | Upside volatility skew | Asymmetric band expansion = directional breakout, not squeeze |
| **ATR** | 3.8961 (+31.4% since Jan 30) | Elevated | 2×ATR = 7.79 pts → stop ≈162.52; size off ATR |
| **VWMA** | 159.8866, +5.13% above 50 SMA | **Confirms accumulation** | High-volume sessions printed at higher prices, not distribution |
| **Resistance** | 172.50 (2024-02-02 high) | Breakout pivot | Close above on ≥50M volume = continuation trigger |
| **Support 1** | 167.33 (2024-02-02 low) | First-line | Close below = failed gap warning |
| **Support 2** | 159.76–161.77 (Feb-1 high / VWMA / 10 EMA) | High-conviction buy zone | Three independent measures within 1.3% |
| **Invalidation** | 155.20–156.96 | Structural break | Post-earnings re-rating undone |
| **Trend stop** | 152.0884 (50 SMA) | Strategic only | 10.7% below price — too wide for tactical use |
| **Verdict** | **Bullish trend / poor entry** | **Avoid chasing; buy pullbacks** | Do not initiate at 170.31; scale into 167.33–163.00 and 159.76–161.77; trigger add on close >172.50 |

**Bottom line on AMZN:** the trend evidence is about as clean as it gets — every moving average rising, fully ordered, the 50/200 spread widening, MACD at a new momentum high with no RSI divergence, and VWMA confirming that the Feb-2 volume was buying rather than selling. The problem is entirely one of **price paid, not direction**. At 170.31 the stock is outside its upper Bollinger band, 5.3% above its 10 EMA, and 12.0% above its 50 SMA, in a tape whose ATR just rose 31% in four sessions. The disciplined play is to let the 167.33-to-172.50 coil resolve, buy the 159.76–161.77 confluence if offered, and use a ~162.50 (2×ATR) stop so normal post-earnings volatility cannot take you out of a trend that the indicators say is intact.