# AAPL — Technical Deep Dive (as of close 2024‑02‑28)

**Reference price (verified snapshot, 2024‑02‑28):** O 182.51 / H 183.12 / L 180.13 / **C 181.42**, Volume 48.95M. The `get_stock_data` CSV row for 2024‑02‑28 matches the verified snapshot exactly (O/H/L/C 182.50999/183.11999/180.13000/181.41999, vol 48,953,900) — **no data discrepancy to flag**. All level claims below are drawn from the snapshot and the indicator series returned by `get_indicators`; where I quote a period move it is computed from dated closes in that tool output.

---

## 1. The regime in one sentence

AAPL is in a **long-term uptrend (200‑day SMA rising every single session since at least 2024‑01‑02) that has lost its medium-term momentum** — price is below the 10 EMA, the 50 SMA, the 200 SMA, the VWMA *and* the 20‑day Bollinger mid-line simultaneously, MACD is at its lowest reading of 2024, yet volatility (ATR) and the MACD histogram are both **contracting**, which is the signature of a coiling, distribution-flavoured range rather than an accelerating downtrend.

---

## 2. Verified indicator dashboard (2024‑02‑28)

| Indicator | Value | Price vs. level |
|---|---|---|
| close_50_sma | **188.0558** | −3.53% |
| close_200_sma | **183.8633** | −1.33% |
| close_10_ema | **183.0519** | −0.89% |
| macd | **−1.8927** | signal −1.5756 |
| macdh | **−0.3171** | 6th session of contraction |
| rsi | **39.42** | neutral-bearish, not oversold |
| boll (20 SMA) | 184.958 | −1.91% |
| boll_ub / boll_lb | 190.5418 / **179.3742** | band width 11.17 (~6.0%) |
| atr | **3.0478** | 1.68% of price |
| vwma | 183.8708 | −1.33% |

---

## 3. Why these eight indicators (complementarity, no redundancy)

1. **close_50_sma** — the medium-term trend/regime line. It is the level that has defined the whole February fade (price has closed *below* it for 21 consecutive sessions, from 2024‑01‑30 through 2024‑02‑28).
2. **close_200_sma** — the strategic benchmark. It is the single most important line right now because price is **whipsawing across it** (above 2024‑02‑15 and 2024‑02‑22, below on 2024‑02‑16, 02‑20, 02‑21, 02‑23, 02‑26, 02‑27, 02‑28). It also frames the golden-cross risk.
3. **close_10_ema** — the fast filter. It tells us whether any bounce attempt has actually changed short-term momentum; as of 2024‑02‑28 it has *not* (price has not closed above the 10 EMA since 2024‑02‑01, with 2024‑02‑22 the only near-miss at 184.37 vs. EMA 184.49).
4. **macd** — trend/momentum oscillator; confirms the February rollover (negative since 2024‑02‑01, lowest value of 2024 on 2024‑02‑28).
5. **macdh** — momentum *rate of change*. Critically it is **not** a duplicate of MACD here: the MACD line is still drifting to new lows while the histogram has contracted from −0.7334 (2024‑02‑20) to −0.3171 (2024‑02‑28). That divergence between level and impulse is the core of the coiling thesis.
6. **rsi** — the oversold/overbought gate, used specifically to test whether this is a "buy the dip" setup. It is not: 39.42 is a mid-to-low reading with no <30 print since 2024‑01‑05 (28.79). This avoids the classic mistake of treating a 39 RSI as a capitulation signal.
7. **boll_lb** — the volatility/mean-reversion floor. At 179.3742 it sits almost exactly on the market's intraday floor, giving a *confluence* support test rather than a standalone opinion. (I use boll/boll_ub from the verified snapshot as context so the bands aren't double-counted.)
8. **atr** — the risk-sizing input. ATR has fallen to 3.0478 from a 2024 peak of 3.5864 (2024‑02‑02), i.e., **volatility compression into a decision point**, which dictates stops and position size.

Deliberately excluded: MACD signal (redundant with macd/macdh pair), stochrsi (duplicates rsi), and VWMA as a *selected* indicator (its 183.87 simply confirms the 200 SMA — I use it only as corroboration, not as a ninth slot).

---

## 4. Trend and structure analysis

### 4.1 Long-term: intact but flattening
- 200 SMA rose every session from 179.637 (2024‑01‑02) to **183.8633** (2024‑02‑28) — an unbroken sequence in the tool output. Higher-lows structure on the daily closes: 166.89 (2023‑10‑26) → 181.18 (2024‑01‑05) → 181.16 (2024‑02‑26) is roughly a double bottom, and the December high (199.62 intraday on 2023‑12‑14, close 198.11) remains far above.
- **But** the 50 SMA has rolled over: peak 190.9252 on 2024‑01‑30, now 188.0558 — a decline of ~2.87 points in 21 sessions (~−0.14/session) while the 200 SMA rises ~+0.077/session. The 50/200 spread has compressed from 8.73 points (2024‑01‑30) to **4.19 points** (2024‑02‑28). At that arithmetic pace the golden-cross spread would close in roughly 19 sessions — call it late March. **This is a watch item, not a forecast**: a single strong week reverses it.

### 4.2 Medium-term: clean lower-high sequence
Descending swing highs since the January peak:
- 196.38 (2024‑01‑24 intraday high, close 194.50)
- 191.05 (2024‑02‑07)
- 184.96 (2024‑02‑22)
- 183.92 (2024‑02‑27)
- 183.12 (2024‑02‑28)

Against a **flat, repeatedly tested floor**: intraday lows of 179.25 (2024‑02‑02), 180.00 (2024‑02‑20), 179.56 (2024‑02‑27), and 180.13 (2024‑02‑28) — and each time the close finished well above the low (185.85, 181.56, 182.63, 181.42). Lower highs + a defended flat floor + contracting ATR = a **descending-triangle / apex-forming coil**, not a clean downtrend.

### 4.3 Momentum: bearish but decelerating
- **MACD** −1.8927 is the most negative reading in 2024; the signal line at −1.5756 means no bullish cross. However, the MACD line's new low on 2024‑02‑28 (−1.8927 vs −1.8712 on 2024‑02‑26) is a marginal, not decisive, extension.
- **MACD histogram** has improved for six straight sessions off the 2024‑02‑20 trough (−0.7334 → −0.3171). Flow still negative, but the *second derivative* has turned up. A histogram cross above zero would put MACD near a signal cross around the 2024‑02‑22–02‑23 price zone (~183–184) — i.e., the histogram and the 200 SMA are pointing at the same trigger.
- **RSI 39.42** sits in the 35–44 band it has occupied since 2024‑02‑12 (extremes: 35.23 on 2024‑02‑20, 44.05 on 2024‑02‑22). This is a *persistent weak* regime, not oversold. In January, by contrast, RSI printed 29.78 (2024‑01‑04) and 28.79 (2024‑01‑05) before a 195+ rally — **the market is not offering that kind of washout now**, which caps the reward on naive dip-buying.

### 4.4 Volatility and volume: the tell
- **ATR 3.0478** (1.68% of price), down from 3.5864 on 2024‑02‑02 and 3.3699 on 2024‑01‑22. The 2024‑02‑26 reading of 2.9516 was the lowest since early January. Compression inside a defined range usually precedes expansion — direction is unresolved.
- **Volume distribution is asymmetric.** The largest volume in the entire visible window is 2024‑02‑02 at **102.55M** — a wide-range down day (open 179.86, low 179.25, close 185.85 vs. prior close 186.86). The February recovery attempts have occurred on much lighter tape (2024‑02‑22: 52.29M; 2024‑02‑27: 54.32M; 2024‑02‑28: 48.95M). Big volume down, light volume up = classic distribution.
- **VWMA 183.8708** (essentially identical to the 200 SMA at 183.8633) means the volume-weighted average buyer is **above** the current price — the average February participant is underwater. That is a supply overhang directly at 183.9.
- Snapshot-supplied money-flow reading (mfi = 0.279992) is consistent with weak accumulation. *Caveat: the scale of that field is ambiguous (0–1 vs 0–100); treat it only as "low," not as a precise threshold breach.*

### 4.5 Measured moves from dated closes (tool-supported)
- 2024‑01‑23 close 195.18 → 2024‑02‑28 close 181.42: **−7.05%**
- 2023‑12‑14 close 198.11 → 2024‑02‑28: **−8.42%**
- 2024‑02‑01 close 186.86 → 2024‑02‑28: **−2.91%**
- 2024‑01‑05 close 181.18 → 2024‑02‑28 close 181.42: **+0.13%** — an eight-week round trip with zero net progress. That single fact best describes this tape.

---

## 5. Actionable levels (all derived from tool output)

**Resistance ladder**
| Level | Source | Significance |
|---|---|---|
| 183.05 | 10 EMA | First gate; no close above since 2024‑02‑01 |
| 183.86–183.87 | 200 SMA + VWMA | The pivot of the entire month; 8 crosses since 2024‑02‑15 |
| 184.96 | Bollinger middle (20 SMA) | Range mid-point / mean-reversion target |
| 186.86–187.33 | 2024‑02‑01 close / 2024‑02‑02 high | Prior supply shelf |
| 188.06 | 50 SMA | Medium-term regime flip |
| 190.54 | Bollinger upper | Range ceiling |
| 196.38 | 2024‑01‑24 high | Structural breakout level |

**Support ladder**
| Level | Source | Significance |
|---|---|---|
| 180.13 | 2024‑02‑28 low | Immediate |
| 179.25–180.00 | 2024‑02‑02 / 02‑20 / 02‑27 lows | Triple-tested floor |
| 179.37 | Bollinger lower band | Confluence with the floor |
| 177.56–178.19 | 2023‑09‑07 close / 2023‑09‑08 | Next shelf if the floor fails |
| 173.5–174.0 | 2023‑09‑13 / 2023‑08 zone | Deeper air pocket |

---

## 6. Trade construction and scenarios

**Base case (highest probability given compression + flat floor): continued 179.3–185.0 chop.** ATR-based mean reversion, small size, no chasing in the middle of the range (183–184 is the worst risk/reward inside the band).

1. **Bullish trigger (reclaim):** a daily close **above 184.0** (clearing 10 EMA 183.05, 200 SMA 183.86 and VWMA 183.87 in one stroke) confirmed by volume **> ~60M** (i.e., clearly above the 40–55M February bounce average, heading toward the 102M distribution print). Then: stop 1.5×ATR ≈ 4.6 points back (~179.4, i.e., under the floor), first target 186.86–187.33, second 188.06 (50 SMA). Only a close above 188.06 re-establishes the medium-term uptrend and makes 190.5–196.4 the objective.
2. **Bearish trigger (breakdown):** a daily close **below 179.25** on expanding volume invalidates the triple floor and the Bollinger lower band simultaneously. Range height = 184.96 − 179.37 ≈ 5.6 points, projecting to roughly **173.8** — which aligns with the 173.5–174.0 shelf. Stop for that trade: back above 181.5 (~1 ATR+).
3. **Neutral / do-nothing zone:** 180.2–183.0. Mid-band, no edge, ATR 3.05 means ~1.7% daily noise — a single session can cross three of these levels. Avoid.

**Risk management specifics**
- ATR 3.0478 → a 1.5×ATR stop is ~4.57 points (~2.5%); 2×ATR is ~6.10 (~3.4%). Position size against that, not against a fixed 5%.
- Because ATR is at a multi-week low (2.95 on 2024‑02‑26), **volatility expansion is the asymmetric risk**: stops set too tight inside the coil will be run before the resolution.
- Nothing in the tool output supports a "bounce off support" claim beyond the observation that intraday lows near 179.3–180.1 have been bought three times (2024‑02‑02, 02‑20, 02‑27). That is three data points, not a validated pattern — and the largest volume of the period was *selling*.

---

## 7. Honest limitations

- The 50 SMA is still above the 200 SMA (188.06 > 183.86); calling this a "death cross" would be wrong as of 2024‑02‑28. The trend is *deteriorating*, not broken.
- The MACD histogram improvement is a two-week observation, not a confirmed turn; the MACD line itself made a new 2024 low on the reporting day.
- The 2024‑02‑02 102.55M-volume day included a wide intraday recovery (low 179.25 → close 185.85), so it can be read as either capitulation-buying or distribution. The subsequent lower highs on lighter volume tilt the interpretation toward distribution, but it is an inference, not a fact from the data.
- No fundamental/catalyst data (earnings, guidance, macro) is available in these tools; this is a pure price/volume technical read.

---

## 8. Summary table

| Dimension | Reading (2024‑02‑28) | Interpretation | Action |
|---|---|---|---|
| Price | 181.42 (O 182.51 / H 183.12 / L 180.13) | Below every major average | Neutral-bearish |
| 50 SMA | 188.06, falling from 190.93 (01‑30) | Medium trend rolled over; 21 closes below | Capped until 188 reclaimed |
| 200 SMA | 183.86, rising from 179.64 (01‑02) | Long trend intact; price whipsawing it | Pivot level, 8 crosses since 02‑15 |
| 10 EMA | 183.05 | Short momentum still negative | No close above since 02‑01 |
| Golden cross | 50 SMA − 200 SMA = +4.19 (was +8.73 on 01‑30) | Spreading narrowing ~0.22/session | Watch item, ~19 sessions away |
| MACD / Signal | −1.8927 / −1.5756 | Lowest of 2024, no cross | Bearish, unconfirmed turn |
| MACD hist | −0.3171, 6 sessions of improvement from −0.7334 | Downside momentum decelerating | Early warning of a turn |
| RSI | 39.42 (range 35–44 since 02‑12) | Weak but NOT oversold (Jan low was 28.79) | No capitulation bid |
| Bollinger | mid 184.96 / ub 190.54 / lb 179.37, width 6.0% | Price in lower third; lb = floor confluence | Range trade 179.4–185 |
| ATR | 3.0478 (peak 3.5864 on 02‑02) | Volatility compressing = coil | 1.5×ATR stop ≈ 4.6 pts |
| VWMA | 183.87 (≈ 200 SMA) | Average February buyer underwater | Supply at 183.9 |
| Volume | 48.95M today; 102.55M on 02‑02 down day | Heavy down-volume, light up-volume | Distribution bias |
| Structure | Lower highs 196.38 → 191.05 → 184.96 → 183.92; flat floor 179.25/180.00/179.56 | Descending coil at apex | Breakout trade, not a trend trade |
| **Primary plan** | Long only on close >184.0 with vol >60M; short/flat on close <179.25 | Range resolution | Target 187–188.1 vs. 173.8 |
| **Risk** | ATR-based stops, small size in mid-band 180–183 | Single-session noise ≈1.7% | Avoid the middle of the range |

**Bottom line for AAPL:** the long-term (200 SMA) uptrend is intact but the stock has spent eight weeks going nowhere (181.18 on 2024‑01‑05 vs. 181.42 on 2024‑02‑28) inside a tightening 179.3–185.0 coil, with distribution-style volume and momentum at 2024 lows while impulse decays. The tradeable information is in the two triggers — a volume-confirmed reclaim of 184.0 (target 188.06, then 190.5+) or a volume-confirmed break of 179.25 (target ~173.8) — and both are better expressed with ATR-scaled ~4.6-point stops than with any bet on the chop itself.