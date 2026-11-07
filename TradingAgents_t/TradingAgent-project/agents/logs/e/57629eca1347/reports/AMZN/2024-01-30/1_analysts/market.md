# AMZN — Technical & Trend Report (as of 2024-01-30 close)

**Verified data source:** `get_verified_market_snapshot` (2024-01-30) cross-checked against `get_stock_data` and `get_indicators`. All figures below agree between the two; the snapshot's implied signal line (MACD 2.706628 − histogram 0.501961 = 2.204667) exactly matches the reported `macds` value, so **no data discrepancy to flag**.

---

## 1. The single most important fact: 2024-01-30 was a bearish outside reversal day at a new high

| Field | Value |
|---|---|
| Open | 160.70 |
| High | 161.73 **(new high of the entire dataset, above 1/29's 161.29)** |
| Low | 158.49 (below 1/29's 158.90) |
| **Close** | **159.00** |
| Prior close (1/29) | 161.26 |
| Day change | **−1.40%** |
| Volume | 45.21M (~+3% vs the 11-session mean of ≈43.8M) |
| Close location in range | **bottom ~16%** of a 3.24-point range |

This is a textbook *outside day with a lower close*: it took out the prior session's high **and** low, then settled near the bottom of its range on unremarkable volume. In an established uptrend that pattern is a short-term distribution warning, not a trend-killer — the trend evidence below is still overwhelmingly positive, but the marginal buyer on 1/30 was clearly less aggressive than on 1/29.

---

## 2. Why these eight indicators (complementarity, not redundancy)

| Indicator | Role in this specific setup |
|---|---|
| **close_200_sma** | Strategic regime filter — is AMZN in a primary uptrend or not? |
| **close_50_sma** | Medium-term trend + the pullback "shelf" where buyers should reappear |
| **close_10_ema** | Fast trend line, and the first tripwire for the current parabolic leg |
| **macd** | Trend momentum magnitude, and the divergence test vs Dec's peak |
| **macdh** | Crossover timing + momentum acceleration/deceleration (the histogram just printed its first contraction) |
| **rsi** | Overbought/extension gauge — it just failed above 70, which is the crux of the 1/30 candle |
| **atr** | Volatility regime for stop placement & sizing (volatility is *compressing* into a possible expansion) |
| **vwma** | Confirms whether the rally is volume-supported or a hollow drift |

I deliberately excluded `boll`, `boll_ub`, `boll_lb` **as selected inputs**, using the snapshot's band values only as a reference overlay, because the 10-EMA/RSI pair already captures the same extension information with less duplication. Stochastics were skipped (redundant with RSI). MFI exists in the snapshot but was not selected to keep the count at eight.

---

## 3. Trend structure: a clean, stacked, rising bull market

- **Close 159.00 vs 50-SMA 150.517 (+5.64%) vs 200-SMA 133.060 (+19.50%).**
- **Stacking is perfect and widening:** 10-EMA 157.107 > 50-SMA 150.517 > 200-SMA 133.060, with the 50/200 spread at **+17.46 points** — the classic bullish stack, no death-cross risk anywhere on the horizon.
- **Both averages are rising with a steepening slope.** 50-SMA: 132.19 (2023-11-01) → 143.05 (2023-12-29) → **150.52 (2024-01-30)**. 200-SMA: 115.11 (2023-10-02) → 127.73 (2023-12-29) → **133.06 (2024-01-30)**. The 50-SMA accelerated from +10.9 to +7.5 points per month, i.e. the medium-term trend is *strengthening*, not flattening.
- Cumulative move supported by the data: **2023-10-26 close 119.57 → 2024-01-29 close 161.26 = +34.9%**. Of that, the January leg alone: **1/04 close 144.57 → 1/29 close 161.26 = +11.5%** in 17 sessions — steep enough to be extended.

**Nuance:** because the 50-SMA sits 5.6% *below* price and has already been outrun, the trend's "dynamic support" is far away. In the near term the operative support is the 10-EMA and the 153.5–155.9 shelf, not the 50-SMA.

---

## 4. Momentum: still positive, but decelerating and showing a swing divergence

**RSI** — 63.09 on 1/30, down sharply from **70.41 on 1/29** (and 67.05 on 1/26). Key reads:
- RSI **breached 70 for the first time since 2023-12-18 (68.05)** on 1/29, then immediately recoiled. That is the *exact* signature of a short-term exhaustion high.
- The January correction never produced an oversold reading: RSI troughed at **40.23 (2024-01-04)** and again only 53.72 (1/17) — buyers defended before true oversold, which is a hallmark of a strong uptrend, and also why upside fuel is now limited without a rest.
- 63 is "strong but not stretched." Historically in this dataset, RSI has spent most of the last two months in the 54–68 band, so 63 is dead-center of the prior range — neutral-bullish, no signal by itself.

**MACD** — line 2.7066, signal 2.2047, histogram **+0.5020**.
- The crossover sequence is unambiguous and recent: histogram was negative through 12/15, flipped **positive 12/18**, went negative again 12/29–1/11 (the January dip), then re-crossed **positive on 2024-01-12 (+0.0937)** and has been positive ever since — a 12-session sustained bullish cross.
- Histogram expansion run: 0.109 (1/19) → 0.129 → 0.199 → 0.272 → 0.343 → 0.441 → **0.598 (1/29) → 0.502 (1/30)**. **The 1/30 contraction is the first in seven sessions** — momentum is still positive but no longer accelerating. This corroborates the RSI rejection.
- **Important caveat (bearish divergence):** price made a materially higher high — close 153.42 on 2023-12-22 vs **159.00 on 2024-01-30** — while the MACD line **peaked at 3.136 (12/22) and only reached 2.707 now.** Momentum is not confirming the price high. This is a *caution* flag for new longs at the highs, not a sell signal in a stacked uptrend.

---

## 5. Volatility & extension: coiling, and price is riding the top of the envelope

**ATR = 2.9654** (≈**1.87%** of price). Volatility has *contracted* meaningfully:
- 3.446 (2023-12-18) → 2.806 trough (2023-12-28) → 3.120 (2024-01-11) → **2.965 (1/30)**.
- 1/30's range of 3.24 points = **1.09× ATR**. Ordinary.

Low, stable ATR during a grinding advance is a "complacency" regime — it makes 2×ATR stops tight (≈5.93 pts, 3.7%), which is convenient, but it also means a volatility expansion (earnings-type shock, or simply mean reversion of ATR) would blow through such stops quickly. Budget for the expansion, don't assume the calm persists.

**Bollinger overlay (snapshot values, reference only):** middle 153.536, upper **162.482**, lower 144.590.
- 1/29 closed 161.26, only **1.22 points (0.75%)** below the upper band; 1/30's high of 161.73 still *failed* to reach 162.48.
- **%B on 1/30 = (159.00 − 144.5896) / (162.4824 − 144.5896) = 0.805.** Price is high in the band but has now turned down *from* the band rather than closing through it — the difference between a breakout and a rejection.
- Bandwidth 17.89 points (11.6% of the middle) — wide, i.e., the move has already been "paid for" in volatility terms.

---

## 6. Volume confirmation: supportive, but not a conviction breakout

- **VWMA = 155.881**, and price is **+2.00% above it**. VWMA is rising hard (151.62 on 1/23 → 153.22 → 154.29 → 155.21 → **155.88**), confirming that the last five up-sessions were volume-backed on an aggregate basis — the advance is *real*, not a hollow drift.
- But note **VWMA (155.88) sits below the 10-EMA (157.11)**. Because volume-weighted average price lags the simple recent price, this means a meaningful chunk of recent turnover occurred in the 151–156 zone. Recent buyers' average cost is ≈156, i.e. only **~1.9% below the last close**. If 155.88 breaks, a cohort of recent longs moves underwater — that is the mechanical reason 155–156 matters more than its technical "look."
- 1/30's 45.2M shares is average, **not a distribution spike**. A genuine top usually shows climactic volume; this does not. That asymmetry (weak close, ordinary volume) is why I read 1/30 as *rotation/consolidation risk* rather than *reversal*.

---

## 7. Levels that matter (all levels derived from the tool data)

**Upside**
1. **161.29–161.73** — 1/29 close-high and 1/30 intraday high; the immediate ceiling and the breakout trigger.
2. **162.48** — Bollinger upper band; the "close above the band" confirmation level.
3. Round-number gravity at **160 / 165**.

**Downside**
1. **157.11** — 10-EMA. First tripwire; losing it ends the "close above fast trend" streak.
2. **155.88** — VWMA (= average recent buyer cost). Confluence with the psychological 156.
3. **154.55 / 153.90–153.93** — 1/25 low, and the 1/22–1/23 lows. The January shelf.
4. **150.5–153.5** — 50-SMA (150.52) + Bollinger middle (153.54); the *structural* line in the sand.
5. **144.05–144.57** — 1/04 low/close; the January swing low, and just above the lower band (144.59). A close below this would invalidate the entire January advance.

A 2×ATR stop from 159.00 = **153.07**, which lands almost exactly on the 153.5 support shelf — a rare and useful confluence. That is the natural invalidation zone for any long taken here.

---

## 8. Actionable read for a trader on 2024-01-30

**Bias: bullish trend, tactically neutral-to-cautious on the next 1–3 sessions.** Everything structural says "own it": price above all three key averages, averages rising and stacking, MACD in a 12-session positive cross, VWMA confirming. Everything *tactical* says "don't add at 159–161": RSI just rejected 70, the histogram contracted for the first time in seven sessions, MACD is diverging vs the December peak, price failed at the top Bollinger band, and 1/30 closed in the bottom sixth of a wide range on a new high.

Three concrete plans, in order of preference:

1. **Buy the pullback, not the print (preferred).** Scale in at **155.9–157.1** (VWMA / 10-EMA). Stop on a *close* below **153.0** (below the 1/22–1/25 shelf and ≈2×ATR). This offers roughly 4.0 points of stop risk against 4.4+ points to the 161.3 retest — a positive expectancy structure, unlike buying at 159.
2. **Momentum continuation, only on confirmation.** Long only on a **close above 161.73** (ideally above 162.48, i.e., a band *close-through*, not a wick). Stop 2×ATR ≈ **155.8**, below the 10-EMA. Recognize this is the higher-risk variant: it requires the MACD divergence to be negated by a fresh momentum thrust.
3. **Stand aside / no short.** Shorting a stacked-uptrend with a rising 50-SMA 5.6% below price and a positive MACD cross is fighting the tape. The 1/30 outside day is a reason to *stop adding*, not a reason to be short. A short only becomes interesting on a decisive close below **155.88**, and even then the 50-SMA at 150.52 is a hard magnet.

**Sizing note:** with ATR at 1.87%, a 2×ATR stop (≈3.7% of price) implies roughly **27% of equity notional per 1% of account risk**. Because ATR is at the low end of its recent range (2.97 vs 3.45 on 12/18), consider sizing off a *normalized* ATR of ~3.3–3.4 rather than today's compressed value, so that a volatility expansion does not force an outsized loss.

**Event-risk flag (not from tool data):** AMZN's quarterly earnings were scheduled for the first days of February, i.e. **within days of this report's date**. Nothing in the OHLCV above prices that gap. A 3-point ATR understates single-day earnings risk by a wide margin — trim or hedge exposure rather than carrying full size through the print, and treat all the tight stop math above as valid only for non-event sessions.

---

## 9. Summary table

| Dimension | Evidence (2024-01-30) | Read |
|---|---|---|
| **Regime (200-SMA)** | Close 159.00 vs 200-SMA 133.06 → **+19.5%**; 200-SMA rising 115.11 (10/02) → 133.06 | Strong primary uptrend |
| **Medium trend (50-SMA)** | Close vs 50-SMA 150.52 → **+5.6%**; 50-SMA 132.19 (11/01) → 150.52, slope steepening | Uptrend intact, price extended |
| **Short trend (10-EMA)** | 10-EMA 157.11; stack 157.11 > 150.52 > 133.06 | Perfect bullish stack; 10-EMA is first tripwire |
| **Momentum (MACD)** | 2.707 / signal 2.205 / hist **+0.502**; positive cross since 1/12 | Bullish, but hist contracted for 1st time in 7 sessions |
| **Divergence** | MACD peak 3.136 (12/22) vs 2.707 now, while close rose 153.42 → 159.00 | **Bearish momentum divergence** — caution flag |
| **Breadth of momentum (RSI)** | 63.09, from **70.41** on 1/29; Jan trough only 40.23 (1/04) | Overbought washout, mid-range; neutral-bullish |
| **Extension (Bollinger)** | Upper 162.482 / mid 153.536 / lower 144.590; %B = **0.805**; 1/30 high 161.73 failed the band | Rejected at the envelope, not a band breakout |
| **Volatility (ATR)** | 2.9654 (**1.87%** of price), down from 3.446 (12/18) | Compressed — expect expansion; 2×ATR = 5.93 (stop 153.07) |
| **Volume (VWMA)** | 155.881, rising 5 straight sessions; price **+2.0%** above | Advance is volume-confirmed; ~156 is recent buyers' cost |
| **Candle (1/30)** | New high 161.73, low 158.49 < prior low, close 159.00 (−1.40%), bottom 16% of range, 45.2M (≈average) | **Bearish outside reversal on no volume climax** |
| **Key resistance** | 161.29–161.73, then **162.48** (upper band) | Breakout needs a *close* above |
| **Key support** | 157.11 (10-EMA) → 155.88 (VWMA) → 153.90–154.55 → **150.52** (50-SMA) | Structural invalidation ~153 |
| **Stance** | Bullish trend / tactically cautious | **Buy 155.9–157.1 pullback (stop <153.0); chase only on close >161.73; do not short. Watch imminent earnings gap risk.** |