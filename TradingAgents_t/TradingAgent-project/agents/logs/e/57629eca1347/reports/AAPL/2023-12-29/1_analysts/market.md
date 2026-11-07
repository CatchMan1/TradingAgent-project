# AAPL — Technical & Market Structure Report (as of 2023-12-29)

## 1. Verified price context

The verified snapshot for `AAPL` shows the 2023-12-29 session as:

| Field | Value |
|---|---|
| Open | 193.90 |
| High | 194.40 |
| Low | 191.73 |
| **Close** | **192.53** |
| Volume | 42.67M |
| Prior close (2023-12-28) | 193.58 |

So the last session was an inside-ish, mildly negative day (−0.54% close-to-close), closing in the lower half of its range and below the prior session's low (193.17). This is the fourth consecutive close in the 193–195 shelf after the 198.11 close on 2023-12-14, which is the **highest close in the retrieved June–December window** (verified data shows the prior high close was 196.45 on 2023-07-31).

All indicator values below are taken from the verified snapshot / indicator feeds and are internally consistent (no tool conflict to flag).

## 2. Indicators selected (8) and why

| # | Indicator | Rationale in this specific context |
|---|---|---|
| 1 | `close_10_ema` (193.90) | The stock has shifted from markup to consolidation; the short-term average is the first objective arbiter of whether that consolidation resolves up. It has already rolled over (peak 195.51 on 2023-12-19), so it doubles as near-term resistance. |
| 2 | `close_50_sma` (186.63) | Primary medium-term trend anchor and the natural downside magnet/dynamic support for a pullback inside an intact uptrend. Rising ~0.33/day. |
| 3 | `close_200_sma` (179.49) | Long-term regime filter. Price is +7.3% above it and the 50-SMA sits 3.98% above the 200-SMA — a confirmed bullish long-term alignment, which changes how a short-term pullback should be interpreted. |
| 4 | `macd` (1.558) | Still positive (above zero) but decelerating for seven straight sessions from 3.75 (2023-12-15) to 1.56 — captures momentum decay before trend damage. |
| 5 | `macds` (2.425) | The MACD line crossed **below** the signal on ~2023-12-19 (3.502 vs 3.559) and the gap has widened every session since; using both lines makes the crossover an auditable event rather than a vague "momentum weakening." |
| 6 | `rsi` (51.06) | Neutral, not oversold. Critically, it exposes a **negative divergence**: RSI peaked at 73.13 on 2023-11-20 and only reached 69.69 on 2023-12-14 when price made a higher close (198.11 vs 191.45). Momentum did not confirm the price high. |
| 7 | `atr` (2.57) | Risk sizing plus a volatility read. ATR has fallen from 3.20 (2023-11-14) to 2.57 (≈1.34% of price), i.e., a volatility contraction typical of a coil before resolution — this sizes stops and tells us breakouts may be "real" rather than noise-driven. |
| 8 | `vwma` (195.36) | Volume-weighted cost basis. Price at 192.53 is **1.45% below** VWMA, meaning recent volume-weighted buyers are underwater — overhead supply, and a concrete level (~195.4) that must be reclaimed to neutralize it. |

*Supplementary reference (retrieved but not counted among the 8): Bollinger bands — `boll` mid 194.31, `boll_ub` 198.82, `boll_lb` 189.80 (2023-12-29).*

## 3. Trend structure: two bullish frames, one bearish short-term frame

**Long/medium term — intact and mature bullish.** Close 192.53 > 50-SMA 186.63 > 200-SMA 179.49, with both averages rising and the 50/200 spread at +3.98% and widening. From the 2023-09-28 close of 170.69 (and the 2023-09-28 intraday low of 167.62) to 2023-12-29 the stock is +12.8% on a close-to-close basis (192.53/170.69), and it is +6.9% from the 2023-06-01 close of 180.09. This is a stock in a well-established uptrend, not a broken chart.

**Short term — a distribution-flavored stall, not a collapse.** Evidence:
- Price has closed below the 10-EMA for five consecutive sessions (last close above it: 2023-12-19 at 196.94 vs EMA 195.51).
- Lower highs since 2023-12-20: 197.68 → 197.08 → 195.41 → 193.89 → 193.50 → 194.66 → 194.40. Lower lows into 2023-12-27 (191.09) and 2023-12-29 (191.73).
- Close is below the 20-session Bollinger mid-line (194.31) for the fourth straight session (2023-12-26 onward) — a persistent, if mild, loss of the mean.
- MACD has declined seven consecutive sessions and holds a bearish signal crossover dated 2023-12-19; the histogram is −0.867.

**But the pullback is orderly and volume-light.** The 2023-12-29 volume of 42.67M is roughly 20% below the ~53M average of the 20 sessions from 2023-12-01 to 2023-12-29 (computed directly from the retrieved rows). Selling has not come with expanding volume — the only huge volume prints were 128.5M on 2023-12-15 (quarterly/futures expiry mechanics, price *up* that day) and 70.4M on 2023-12-13 (up day). No high-volume down day appears in the last three weeks. That argues for profit-taking/consolidation rather than institutional distribution.

## 4. Momentum and mean-reversion read

- **RSI 51.06** is the neutral midpoint: it has fully unwound the December overbought condition (70.0 on 2023-12-08; 73.13 on 2023-11-20) without reaching oversold. There is room to go either way; RSI provides no edge on its own here, only the confirmation that the froth is gone.
- **December overextension was real and has been corrected.** On 2023-12-14 the close of 198.11 was *above* that day's upper Bollinger band of 197.66 — a band-ride/overbought condition. The subsequent move has retraced to 192.53, i.e., 2.82% below the 2023-12-14 close and now 0.9% *below* the mid-band.
- **Volatility compression.** Bollinger width has contracted from 21.76 (upper 196.56 / lower 174.80 on 2023-11-29) to 9.03 on 2023-12-29, i.e., from ~11.6% to ~4.65% of the mid-line, and ATR has fallen 20% in six weeks. Narrow bands plus falling ATR inside an uptrend typically precede a directional resolution; because trend and the 50/200 stack are bullish, the base case favors an upside resolution — but the trigger has not fired.

## 5. Concrete levels and what they mean

**Upside / overhead supply**
- 193.90 — 10-EMA (first hurdle; reclaiming it turns short-term momentum neutral).
- 194.31 — Bollinger mid-line (the "mean" the price has lost).
- 194.40–195.99 — 2023-12-29/2023-12-28 highs (194.40, 194.66) and the 2023-12-08 high (195.99).
- **195.36 — VWMA**: the volume-weighted break-even of recent buyers. A close above this is the cleanest evidence that overhead supply has been absorbed.
- 197.68–198.11 — 2023-12-20 intraday high (197.68) and the 2023-12-14 record close (198.11); 199.62 is the 2023-12-14 intraday high.
- 198.82 — upper Bollinger band on 2023-12-29.

**Downside / support**
- 191.09–191.73 — 2023-12-27 low and 2023-12-29 low: the immediate floor of the current range.
- 189.80 — lower Bollinger band (a 1.44% move from the close).
- 186.63 — 50-SMA, rising; the trend's line in the sand (3.16% below the close).
- 179.49 — 200-SMA (long-term regime break level; +7.3% below price, so not a near-term risk).

Note the price's cushion above the 50-SMA has been halved: 198.11 was 8.06% above the 50-SMA on 2023-12-14; 192.53 is 3.16% above it on 2023-12-29. The trade has de-risked itself — which is an argument *against* chasing a breakdown and *for* buying the pullback zone.

## 6. Actionable plan

**Bias: constructively neutral / "buy-the-dip, don't chase."** The dominant trend is up (price > rising 50-SMA > rising 200-SMA), but short-term momentum is negative (MACD below signal since 2023-12-19, price below 10-EMA and VWMA). That mix favors patience over aggression in either direction.

1. **Trend continuation entry (preferred):** add on stabilization in the 189.8–186.6 zone (lower Bollinger band → 50-SMA). Require a reversal day (close above the prior day's high) or a reclaim of the 10-EMA, not just a touch of the level.
2. **Momentum confirmation entry:** a daily close above **195.4 (VWMA)** with above-average volume (~>53M) validates that the December supply is cleared; first target 197.7–198.8, then 199.6.
3. **Avoid adding between 193.5 and 195.4** — that is the no-man's-land between the 10-EMA/mid-band and VWMA, where the reward/risk is poor.
4. **Risk framing (ATR-based):** ATR 2.57 ≈ 1.34% of price. A standard 1.5×ATR stop is ~3.9 points; a stop under the 50-SMA at ~185.5 implies ~3.6% risk from 192.53 and ~2.9% from a 191 entry. Size positions off ATR rather than fixed dollar stops, and note that narrow ATR currently permits *larger* notional for the same risk budget — but with the offsetting risk of a volatility expansion on the resolution.
5. **Invalidation / what would change the read:** (a) a high-volume close below 189.8 (lower band) that is not quickly recovered; (b) a decisive break of the 50-SMA at 186.63 — that would put the ~179.5 200-SMA in play and mark the first real trend damage since late October; (c) bullish invalidation of the bearish short-term case: two consecutive closes above 195.4 with volume expansion.
6. **Watch item:** the negative RSI divergence (price high 2023-12-14 vs RSI high 2023-11-20) and the seven-session MACD decay mean any rally back to 198+ that arrives with *lower* RSI/histogram than December's print would be a lower-quality breakout and a candidate for trimming rather than adding.

## 7. Summary table

| Dimension | Reading (2023-12-29) | Interpretation | Level to watch |
|---|---|---|---|
| Price / session | Close 192.53, −0.54% d/d; range 191.73–194.40 | Lower-half close, 4th day in 193–195 shelf | 191.09–191.73 floor |
| Short-term trend | Close < 10-EMA 193.90 (−0.71%); 10-EMA falling since 12/19 | Bearish short-term bias | Reclaim 193.90 |
| Medium-term trend | Close > 50-SMA 186.63 (+3.16%); 50-SMA rising 0.33/day | Uptrend intact, extension unwound | 186.63 |
| Long-term trend | Close > 200-SMA 179.49 (+7.27%); 50>200 by +3.98% | Confirmed bullish regime | 179.49 |
| MACD | 1.558 vs signal 2.425; hist −0.867; bearish cross ~12/19; 7 sessions of decay | Momentum deteriorating but still positive | Cross back above signal |
| RSI | 51.06 (from 73.13 on 11/20, 70.02 on 12/08) | Neutral; negative divergence vs 12/14 price high | 45 (weakness), 60 (re-accel) |
| Bollinger | Mid 194.31 / UB 198.82 / LB 189.80; width ~4.65% vs ~11.6% on 11/29 | Price below mean; volatility squeeze | 189.80 / 194.31 |
| Volume / VWMA | 42.67M (~20% below ~53M 20-day avg); price 1.45% below VWMA 195.36 | Light-volume pullback, but recent buyers underwater | 195.36 |
| ATR / risk | 2.57 (1.34% of price), down from 3.20 on 11/14 | Compression → resolution pending; 1.5×ATR stop ≈ 3.9 pts | Stop 185.5–188 |
| Overall stance | **Hold / buy-the-dip, don't chase** | Bullish trend + bearish short-term momentum = wait for confirmation | Add 186.6–189.8 or >195.4 |