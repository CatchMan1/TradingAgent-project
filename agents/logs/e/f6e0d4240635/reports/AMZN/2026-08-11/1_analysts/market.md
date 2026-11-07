# AMZN — Multi-Horizon Technical Report
**Analysis date: 2026-08-11 | Last verified close: $272.27 | Source of truth: verified snapshot (2026-08-11)**

---

## 1. Market Context: Why These Indicators

AMZN is in an **event-driven, post-gap consolidation** regime. The tape shows a violent earnings-type repricing (2026-07-31 gap) followed by six sessions of sideways digestion. That combination — a lagging trend that has just flipped bullish, a volatility regime that has doubled in two weeks, and momentum that is decelerating from an extreme — requires indicators that separate **trend structure** from **momentum thrust** from **risk sizing**.

Selected set (8, complementary, non-redundant):

| # | Indicator | Role in this specific context |
|---|---|---|
| 1 | **close_10_ema** | Fast trend anchor / trailing stop inside the new post-gap uptrend |
| 2 | **close_50_sma** | Medium-term trend; validates whether the gap created a genuine trend change |
| 3 | **close_200_sma** | Long-term regime filter (structural bull vs. bear) |
| 4 | **macd** | Trend/momentum direction after a discontinuity |
| 5 | **macdh** | Momentum *thrust* — earliest warning of deceleration/divergence |
| 6 | **rsi** | Overbought/oversold and post-gap cooling profile |
| 7 | **atr** | Volatility regime + stop distance + position sizing |
| 8 | **vwma** | Volume-weighted confirmation that the gap was institutionally backed |

Bollinger bands (boll / boll_ub / boll_lb) are used as a **supplementary cross-check** from the verified snapshot rather than as a ninth selection, since ATR already covers the volatility dimension.

---

## 2. Price Structure — What Actually Happened

Verified OHLCV sequence (all from the snapshot / price history, exact values):

| Date | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|
| 2026-07-29 | 229.32 | 232.82 | 226.16 | **226.65** | 44.96M |
| 2026-07-30 | 233.35 | 239.82 | 231.06 | **235.50** | 101.84M |
| 2026-07-31 | **265.00** | 273.23 | 262.01 | **271.58** | **129.05M** |
| 2026-08-03 | 278.29 | **287.20** | 278.00 | **284.02** | 90.83M |
| 2026-08-04 | 276.06 | 281.07 | 275.82 | 277.42 | 69.75M |
| 2026-08-05 | 281.59 | 282.79 | 270.73 | 272.65 | 45.12M |
| 2026-08-06 | 272.77 | 275.48 | 271.06 | 272.26 | 30.67M |
| 2026-08-07 | 272.87 | 278.31 | 272.75 | 274.48 | 33.86M |
| 2026-08-10 | 274.01 | 280.14 | 273.60 | 278.09 | 35.73M |
| 2026-08-11 | 278.69 | 278.84 | 271.36 | **272.27** | 31.90M |

**Key structural observations, all directly evidenced:**

1. **A discrete, unfilled gap exists between 2026-07-30 close ($235.50) and 2026-07-31 open ($265.00).** This is a $29.50 air pocket (~11% of current price). It is the single most important structural feature on the chart.
2. **The move was 3-session vertical:** close-to-close from $226.65 (07-29) to $284.02 (08-03) = **+25.3%**, printing an intraday high of **$287.20** on 08-03 — the highest price in the 2026 data set.
3. **Volume confirms institutional participation:** 129.05M on 07-31 and 90.83M on 08-03 versus a ~30–45M baseline in the surrounding sessions.
4. **Volume is now decaying:** 69.75M → 45.12M → 30.67M → 33.86M → 35.73M → 31.90M. That is constructive *digestion* (sellers not pressing) but also *waning conviction* (no accumulation yet at the highs).
5. **2026-08-11 is a short-term warning bar:** opened $278.69, high $278.84, closed $272.27 — closing *below* the 2026-08-10 low ($273.60) and near the session low ($271.36). Bearish engulfing of the prior day's range.

**Prior context (supports the "recovery, not fresh breakout" framing):**
- The stock was in a downtrend into late July: $274.99 close (2026-05-05) → $227.01 close (2026-06-25) = **−17.4%**, and a second leg to $226.65 (2026-07-29).
- January 2026 started at $226.50; 2026-08-11 at $272.27 = **+20.2% YTD**, so the gap recovered all of the May–July drawdown and more.

---

## 3. Trend Structure (MAs)

Verified values on 2026-08-11:

| Indicator | Value | Price vs. level | Slope behavior |
|---|---|---|---|
| close_10_ema | **267.16** | Price +1.91% above | Rising every session since 07-29 (236.46 → 267.16) |
| close_50_sma | **247.62** | Price +9.96% above | Bottomed 246.38 on 07-30, now turning up |
| close_200_sma | **237.09** | Price +14.84% above | Rising steadily (233.0 on 07-02 → 237.09) |

**Interpretation:**
- **Full bullish stack:** Price (272.27) > 10-EMA (267.16) > 50-SMA (247.62) > 200-SMA (237.09). 50 > 200 by $10.53 (4.4%), so the **golden-cross regime remains intact**.
- The 10-EMA is the operative trend line. It has risen ~$30.7 in 9 sessions. Price has not closed below it since 2026-07-29.
- **Caution — the averages are structurally stale.** The 50-SMA only just stopped declining (a two-session uptick). The 200-SMA is $35 below spot. Both are *slow-conforming* to an event gap, so a close below the 10-EMA would NOT yet be reflected in the 50/200. **Do not use the 50-SMA as a risk level in this regime** — it's 10% away and would permit a catastrophic loss.
- The 50-SMA at 247.62 sits *inside* the gap zone (235.50–265.00), which means a gap-fill scenario would break the 50-SMA before finding equilibrium. That is a structural fragility worth naming.

---

## 4. Momentum (MACD, MACD Histogram, RSI)

| Date | MACD | Signal | Histogram | RSI |
|---|---|---|---|---|
| 2026-07-29 | −3.75 | — | −1.99 | **33.31** |
| 2026-07-30 | −3.63 | — | −1.50 | 44.41 |
| 2026-07-31 | −0.62 | — | +1.21 | **67.88** |
| 2026-08-03 | +2.74 | — | +3.66 | **72.23** |
| 2026-08-05 | +6.00 | — | **+4.62** | 63.49 |
| 2026-08-07 | +7.58 | — | +4.09 | 64.21 |
| 2026-08-10 | +8.37 | 5.19* | +3.90 | 65.87 |
| **2026-08-11** | **+8.43** | **5.26** | **+3.17** | **60.97** |

*\*Signal derived from MACD − histogram.*

- **MACD crossed above zero on 2026-07-15** ($254.96 close day), dipped back negative 07-23 to 07-30, then produced a decisive re-cross and is now at **+8.43**, the highest reading in the 2026 window. The MACD line is still making higher highs (8.37 → 8.43 on the last session).
- **The histogram is the important nuance:** it peaked at **+4.62 on 2026-08-05** and has contracted for **five consecutive sessions** (4.62 → 4.58 → 4.36 → 4.09 → 3.90 → **3.17**) while price went 272.65 → 272.27. Positive-but-shrinking histogram = **momentum thrust is fading, trend is not broken.** This is the classic signature of a consolidation/flag, not a reversal — but it removes the case for chasing at current levels.
- **RSI cooled from 72.23 (08-03) to 60.97 (08-11)** — a ~11-point mean reversion with price only −4.1% off the 08-03 close ($284.02 → $272.27). RSI unwinding via *time/consolidation* rather than *price destruction* is a bullish-quality tell. At 60.97, RSI is **not overbought** and has room to re-expand.
- Note the RSI pattern 72.23 → 65.87 → 60.97 mirrors price's lower highs (284.02 → 278.09 → 272.27): these are **matching lower highs, not a genuine divergence**. There is no confirmed bearish RSI divergence in the data.
- **Caveat on all momentum readings:** the July 31 gap mechanically inflated MACD/RSI. Extremes here are partly event artifacts, so treat the *rate of change* of these indicators as more informative than their absolute level.

---

## 5. Volatility & Band Structure (ATR + Bollinger cross-check)

| Metric | 2026-07-29 | 2026-08-11 | Change |
|---|---|---|---|
| ATR (14) | 6.892 | **9.015** | **+30.8%** |
| ATR as % of close | 3.04% | **3.31%** | +27bp |
| Bollinger middle (20SMA) | 242.72 | **254.37** | +4.8% |
| Bollinger upper (2σ) | 258.00 | **292.77** | +13.5% |
| Bollinger lower (2σ) | 227.45 | **215.97** | −5.0% |
| Band width (UB−LB)/mid | 12.58% | **30.20%** | **≈2.4×** |

- **A classic volatility-squeeze breakout:** band width expanded from 12.58% to 30.20% in nine sessions. This is a *regime change in volatility*, not noise, and it demands smaller position sizes for the same dollar risk.
- **%B position:** (272.27 − 215.97) / (292.77 − 215.97) ≈ **0.73** — upper half of the bands, above the middle (254.37), but **not riding the upper band** ($20.5 below it). So there is no Bollinger "overbought breakout" signal firing; the upper band at 292.77 is not a realistic near-term target magnet — it's a volatility artifact.
- **Actionable volatility math:** 1×ATR = $9.02; 2×ATR = $18.03.
  - 2×ATR stop from 272.27 = **$254.24**, which converges almost exactly with the **Bollinger middle (254.37)** and the **2026-07-15 close/breakout area (254.96)**. That tri-level confluence makes ~$254 the highest-quality structural invalidation zone.
  - 1.5×ATR = $13.53 → **$258.74**, near **VWMA (258.53)**.
  - The **10-EMA at 267.16** is only 0.57×ATR away — an appropriate *trailing* stop for a momentum trader, but far too tight for a position trade given 3.3% daily range.

---

## 6. Volume Confirmation (VWMA)

- **VWMA = $258.53** and has risen for eight straight sessions (240.82 on 07-30 → 258.53 on 08-11).
- Price (272.27) is **+5.31% above VWMA.** Because VWMA is volume-weighted, this confirms that **the bulk of recent traded value occurred well below spot** — i.e., the gap-up was absorbed by real volume, not a thin print. This is a genuine confirmation signal, not a cosmetic one.
- The ordering **VWMA (258.53) > 50-SMA (247.62)** while **VWMA < 10-EMA (267.16)** tells the story precisely: the volume-weighted "true cost basis" of the last ~20 sessions sits *between* the two averages, i.e., longs are, on average, in profit and the market has accepted the new range.
- **Divergence to watch:** price has made a lower high (284.02 → 278.09 → 272.27) on *declining* volume (90.8M → 35.7M → 31.9M). Declining volume in a pullback is healthy; declining volume on an *attempted advance* would not be. Watch for a volume expansion above ~45–50M on any push through $280 as the confirmation trigger.
- Supplementary snapshot reading: MFI at 0.5167 (≈51.7 on a 0–100 scale) — neutral, consistent with "no aggressive volume-weighted distribution yet."

---

## 7. Levels Map (all levels derived from tool output)

| Level type | Price | Source |
|---|---|---|
| Resistance 1 | **$278.31 – $278.84** | 08-07 high $278.31; 08-11 high $278.84 |
| Resistance 2 | **$280.14 – $282.79** | 08-10 high $280.14; 08-04 high $281.07; 08-05 high $282.79 |
| Resistance 3 / swing high | **$287.20** | 08-03 intraday high (2026 high) |
| Spot | **$272.27** | 08-11 close |
| Support 1 (short-term shelf) | **$270.73 – $271.36** | 08-05 low $270.73; 08-06 low $271.06; 08-11 low $271.36 |
| Support 2 | **$267.16** | 10-EMA |
| Support 3 | **$265.00** | 07-31 gap open |
| Support 4 | **$262.01** | 07-31 gap-session low |
| Support 5 (confluence) | **$254.24 – $254.96** | 2×ATR stop zone + Bollinger middle $254.37 + 07-15 close $254.96 |
| Support 6 | **$247.62** | 50-SMA |
| Structural void begins | **$235.50** | 07-30 close (unfilled gap floor) |

**Note on the gap floor:** the 235.50–265.00 region contains no traded prices. There is *no* technical support between $262 and $235.50 except the 50-SMA at $247.62. Gap statistics are not a law, but the 2026 record contains a precedent worth naming: the 2026-02-04 close ($232.99) to 2026-02-05 open ($224.91) gap down was fully retraced by 2026-04-09 (close $233.65). Gaps in this name have filled before — which is why the $265 area deserves respect as a *risk trigger*, not merely a reference.

---

## 8. Actionable Scenarios

**Bullish continuation (needs confirmation):**
- Trigger: a close **above $280.14** (08-10 high) with volume **> ~45M**.
- Targets: $284.02 (08-03 close) → $287.20 (08-03 high) → measured move extension.
- Confirmation stack: MACD histogram stops contracting (turns up from 3.17), RSI reclaims > 65, 10-EMA keeps rising.
- Invalidation: close back below $271.36.

**Base case — range digestion (highest probability given the evidence):**
- Range: **$270.73 – $287.20**, currently trading in the lower third.
- Fading $282–287 and buying $271–273 is coherent; the declining histogram (thrust fading) and declining volume support mean-reversion inside the range rather than a trend leg.
- The 10-EMA at 267.16 rising ~$1.5–3/day will catch up to price within ~2–4 sessions, resolving the setup one way or the other.

**Bearish / gap-fill risk:**
- Trigger 1: **close below $270.73** → expect a test of the 10-EMA ($267.16) and then the **$265.00 gap open**.
- Trigger 2: **close below $265.00** → the air pocket to the 50-SMA ($247.62) and the 2×ATR/Bollinger confluence ($254.24–254.96) opens up. Note price would still be *above* the 200-SMA ($237.09) in that scenario — the long-term regime would survive even a full gap fill, which is why the 200-SMA is the wrong stop but the right *strategic* bull/bear line.

---

## 9. Risk Management Specifications

- **Volatility unit:** ATR = **$9.02 = 3.31% of price.** Use this, not a fixed 2%/5% rule.
- **Stop placement:**
  - Momentum trader: below **$267.16** (10-EMA), risk ≈ **$5.11 = 0.57×ATR** — tight, high whipsaw probability.
  - Swing position: below **$270.73** (shelf), risk ≈ **$1.54** from a $272.27 entry is *too tight* for a 3.3% ATR; realistic swing stop = **$254.24–$258.74** (2×ATR / 1.5×ATR) for risk of **$13.53–$18.03 per share.**
- **Position sizing:** shares = (account risk budget) ÷ (2 × $9.02). A $10,000 account risking 1% ($100) supports only **~5 shares** at a 2×ATR stop — the widened ATR is the binding constraint.
- **Do not** size off the pre-gap ATR of $6.89 (07-29); the volatility regime has changed by +31%.
- **Event note:** the July 31 repricing and the elevated ATR/volume pattern around 07-30 (101.8M) and 07-31 (129.1M) indicate earnings-type catalysts. ATR remains 31% above its pre-event level, so another catalyst can produce a second discrete repricing.

---

## 10. Summary Table

| Dimension | Reading (2026-08-11) | Interpretation | Actionable implication |
|---|---|---|---|
| **Close** | $272.27 (O 278.69 / H 278.84 / L 271.36) | Closed near low, below 08-10 low ($273.60) | Short-term bearish bar; no chase |
| **10-EMA** | $267.16, rising 9 sessions | Short-term uptrend intact | Trailing stop reference; price +1.91% above |
| **50-SMA** | $247.62, just turning up | Medium trend bullish but 9.96% below price | Too far to be a risk level; sits inside gap zone |
| **200-SMA** | $237.09, rising | Long-term bull regime | Price +14.84% above; strategic bull/bear line |
| **MA stack** | 272.27 > 267.16 > 247.62 > 237.09 | Full bullish alignment; 50>200 by $10.53 | Trend-following bias long, BUT extended |
| **MACD** | +8.43 (signal 5.26) | Above zero and above signal; still rising | Bullish trend momentum confirmed |
| **MACD Histogram** | +3.17, down 5 straight sessions from +4.62 (08-05) | Positive but decelerating thrust | Buy dips, not breakouts; watch for turnaround |
| **RSI** | 60.97, down from 72.23 (08-03) | Cooled via time, not price; not overbought | Room to re-expand; no divergence confirmed |
| **ATR** | $9.02 (3.31%), +30.8% vs 07-29 | Volatility regime expanded ~2.4× on bands | Halve/shrink position size; 2×ATR = $18.03 |
| **Bollinger** | Mid 254.37 / UB 292.77 / LB 215.97 | %B ≈ 0.73; width 30.20% | Upper half of bands, not band-riding; UB not a target |
| **VWMA** | $258.53, rising 8 sessions | Price +5.31% above; gap was volume-backed | Bullish confirmation of the repricing |
| **Volume** | 31.90M (vs 129.05M on 07-31) | Fading participation in consolidation | Watch >45–50M for breakout validation |
| **Resistance** | $278.3–278.8 → $280.1–282.8 → $287.20 | Layered supply overhead | Break above $280.14 on volume = long trigger |
| **Support** | $270.73–271.36 → $267.16 → $265.00 → $254.24–254.96 → $247.62 | First shelf tested 3 times (08-05, 08-06, 08-11) | Close below $270.73 flips bias; below $265 opens gap fill |
| **Structural risk** | Unfilled gap $235.50–$265.00 (no traded prices) | Air pocket / 50-SMA sits inside it | Hard risk trigger at $265.00, not at the 50-SMA |
| **Bias** | Bullish trend, decelerating momentum, wide-volatility consolidation | Digesting a +25.3% 3-session repricing | Range-trade $271–287; trend-follow only on a volume-confirmed $280+ reclaim |

**Bottom line for AMZN:** the trend is up and volume-validated, but you are buying the *fourth quartile* of a vertical, event-driven move with shrinking momentum thrust, shrinking volume, an RSI that has already cooled, and ATR up 31%. The asymmetry favors patience: either wait for a volume-confirmed reclaim of **$280.14** to add trend exposure, or wait for a pullback into the **$254–259** confluence (Bollinger middle + VWMA + 2×ATR) before establishing size. The **$270.73** shelf and the **$265.00** gap open are the two levels that decide whether this is a flag or a failed breakout.