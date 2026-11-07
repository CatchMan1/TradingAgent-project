# AAPL (Apple Inc.) — Technical Assessment as of Thursday, 2024-02-01

**Verified snapshot (source of truth):** close **186.86**, open 183.99, high 186.95, low 183.82, volume **64,885,400**. Snapshot indicator readings: 50-SMA 190.762, 200-SMA 182.395, 10-EMA 189.128, MACD −0.1376, signal 0.1602, histogram −0.2978, RSI 45.074, Bollinger mid 187.959 / upper 196.972 / lower 178.946, ATR 3.241, VWMA 189.294.

All indicator-tool outputs I pulled (same ticker, same date) matched the verified snapshot to the displayed precision — **no discrepancies to flag**. One data note: the snapshot also carries an `mfi` field reading **0.5272**, which is not on the standard 0–100 scale, so I have deliberately excluded it rather than misread it.

---

## 1. The tape: what actually happened into 2024-02-01

Using only tool rows:

- **Peak of the visible window:** close 198.11 and intraday high 199.62 on **2023-12-14**.
- **January capitulation:** a gap-down open on **2024-01-02** (prior close 192.53 → open 187.15) on **82.49M** shares — the heaviest volume since 2023-12-15 (128.54M). Price then slid to a closing low of **181.18** on 2024-01-05 (intraday 180.17), where RSI printed **28.79** (oversold).
- **January recovery:** a rally of +7.73% from the 181.18 close to a **195.18** close on 2024-01-23 (intraday high 196.38 on 01-24) — i.e., the rebound **failed to reclaim the 12-14 high on both a closing and an intraday basis**, producing a lower high.
- **Current leg down:** 195.18 (01-23 close) → 184.40 (01-31 close), with **2024-02-01** reversing hard: opened at 183.99 (below the prior close), printed a lower low at 183.82, then closed at 186.86 — in the top 3% of the session range (range 3.13 pts ≈ 0.97 ATR).

Arithmetic on visible prices: the pullback from the 01-23 closing high is **−4.26%**; from the 12-14 closing peak it is **−5.68%**. On an intraday basis the drop from the 01-24 high (196.38) to the 02-01 low (183.82) is **−6.40%**, which retraces roughly **77%** of the 180.17 → 196.38 January advance — i.e., this is a *deep* intraday retracement, not a shallow flag.

---

## 2. Indicator selection (8) and why

The context is a **corrective pullback inside an intact primary uptrend, with momentum rolling over but price structure still making higher lows**. That calls for a trend-ladder (long/medium/short), a momentum oscillator pair, a volatility/risk input, and a participation check — not a pile of correlated oscillators.

| # | Indicator | Role in this specific setup |
|---|---|---|
| 1 | **close_200_sma** | Primary-trend arbiter; the rising 200-day is the line that decides whether this is a dip or a trend break. |
| 2 | **close_50_sma** | The medium-term trend and the exact level AAPL just lost on 2024-01-30; slope is decelerating — key evidence. |
| 3 | **close_10_ema** | Fast momentum/entry timing; price has been below it since 2024-01-30. |
| 4 | **macd** | Confirms the momentum regime shift; also crossed below zero on 2024-02-01. |
| 5 | **macdh** | Histogram sign changes date the crossovers precisely and show whether bearish momentum is accelerating or exhausting. |
| 6 | **rsi** | Independent (non-EMA) momentum read to test whether the pullback has produced an oversold reset — it has not. |
| 7 | **atr** | Required to convert every level into a risk unit, size positions, and judge whether a stop is realistically placed. |
| 8 | **vwma** | Volume-weighted cost basis — tells us whether recent buyers are trapped above price (a supply overhang). |

**Excluded as redundant:** `boll` (a 20-SMA, essentially a fourth moving average), `macds` (its information is fully captured by the MACD/histogram pair), and `stochrsi`-type duplicates of RSI. I still reference the Bollinger bands as *secondary* confluence for level identification only.

---

## 3. Trend structure: three timeframes, three different answers

**Long term — bullish, and not yet threatened.** The 200-day SMA rose from **171.504 (2023-11-03)** to **182.395 (2024-02-01)**, +6.35%, and its slope has been remarkably steady (+1.00 pts over the ten sessions to 01-19, +1.10 pts over the ten sessions to 02-01). The 50-day has been above the 200-day for the entire visible window. Close 186.86 sits **+2.45% (+1.38 ATR) above** the 200-day. The primary trend is up.

**Medium term — deteriorating.** The price lost the 50-day on **2024-01-30** after holding above it from 01-19 through 01-29 (e.g., 191.56 vs 189.80 on 01-19; 188.04 vs 190.93 on 01-30). More telling than the break itself is the **decay in the 50-day's slope**: +2.115 pts across the ten sessions ending 01-19 versus only **+0.72 pts** across the ten sessions ending 02-01. It also ticked *down* on 01-31 (190.819) and 02-01 (190.762) — the first decline in the visible window (data back to 2023-11-03). A flattening 50-day at ~190.8 is now overhead resistance rather than support.

**Short term — bearish, with a one-day reprieve.** The 10-EMA has fallen four straight sessions (191.406 → 190.794 → 189.631 → **189.128**), and price is **−1.20% below it**. The alignment is 10-EMA (189.13) < Bollinger mid / 20-SMA (187.96) < 50-SMA (190.76), while the 200-SMA (182.40) remains far below. That is a *partial* bearish stack — short-term bearish, long-term bullish — the classic corrective-pullback signature.

**The constructive counterpoint:** intraday lows are rising — **180.17 (01-05) → 180.30 (01-17) → 183.82 (02-01)**. Price is compressing between a flat ceiling (closes 195.18/194.50/194.17 on 01-23/24/25) and a rising floor (180.2 → 183.8). That is a coil, and it will resolve.

---

## 4. Momentum: the crossovers have flipped against the bulls

From the MACD/signal/histogram series:

- **Bullish crossover 2024-01-19** (histogram flipped positive: +0.2025, up from −0.2832 on 01-18).
- MACD peaked at **0.9512 on 01-26**; histogram peaked at **1.1282 on 01-25** — note momentum peaked *after* price (price high 01-23/24). That is typical distribution behavior: price leads, momentum lags then fails.
- **Bearish crossover 2024-01-31** (MACD 0.0913 vs signal 0.2346; histogram −0.1434) — after which the histogram **expanded negative to −0.2978** on 02-01 while MACD itself **crossed below zero** (−0.1376). That is a fresh, accelerating bearish signal, not a stale one, and the signal line (0.1602) is now above both MACD and rolling over.

**A wider divergence worth respecting:** the December-to-January price peaks are 198.11 → 195.18 (lower high), while the MACD peaks are **3.751 (2023-12-15) → 0.951 (2024-01-26)** — a dramatically lower momentum high on the retest. This is a macro-scale bearish momentum divergence across ~6 weeks. It does not invalidate the primary uptrend, but it argues that the 195–199 zone is now supply, not a launchpad.

**RSI at 45.07 is the key non-confirmation for dip buyers.** It collapsed from 62.62 (01-23) to 39.60 (01-31) and rebounded to 45.07 with the 02-01 candle. Critically, **it never reached oversold** (the only sub-30 print in the window was 28.79 on 2024-01-05). With price 9.6% below its December high and RSI still mid-range, there is **no mean-reversion fuel** here — the 02-01 bounce is a reaction to a lower-low rejection, not an oversold snap-back.

---

## 5. Volatility and participation

**ATR is 3.241, or 1.73% of price.** The regime expanded from 2.575 (2023-12-29) to a peak of 3.340 (2024-01-18) and has only modestly cooled. In practical terms: daily noise is ±3.24 points, so any stop tighter than ~3 points from entry is a coin flip.

**Bollinger (secondary reference):** upper 196.972, mid 187.959, lower 178.946 → total width **18.03 pts = 9.59% of the mid, ≈5.6 ATR**. That is narrower than the 01-05 panic (20.63 pts, 10.71% of mid) but far wider than 12-19 (12.34 pts, 6.39%). The 02-01 close at 186.86 is **−0.58% below the mid-band** and 4.42% above the lower band. Bands are contracting modestly after the January expansion — consistent with the coil described above.

**VWMA 189.294 is above the close** — the volume-weighted average transaction price of the recent window is ~2.43 points (1.30%) higher than the last print. Translation: **recent buyers are underwater**, and the 189–190 zone carries supply. VWMA has, however, flattened and turned very slightly up (189.125 → 189.395 → 189.335 → 189.294) since 01-29, meaning the selling pressure that dominated 01-02 → 01-18 has stopped getting worse.

**Volume tells a mildly constructive story on the latest session:** 64.89M on 02-01 (an up day) versus 55.47M (01-31) and 55.86M (01-30) — roughly **1.17×** the 20-session average of ≈55.6M (computed from tool rows 2024-01-04 → 2024-02-01). Up-day volume expanding 17% over the two preceding down days is a modest accumulation hint, but it is well short of the 82.49M character of the 01-02 distribution day. One day is not confirmation.

---

## 6. Level map (every figure derived from tool output)

**Resistance (stacked, in order):**
1. **187.96** — 20-SMA / Bollinger mid (immediate, price is right at it)
2. **189.13–189.29** — 10-EMA and VWMA: a tight supply shelf and the trapped-buyer cost basis
3. **190.76** — 50-SMA, now rolling flat; the medium-term line in the sand
4. **192.42–196.38** — Jan 23–24 closes (195.18/194.50) and intraday high 196.38
5. **196.97** — Bollinger upper band
6. **198.11 / 199.62** — 12-14 close / intraday high

**Support (stacked):**
1. **183.82–184.35** — 02-01 low / 01-31 low; first line of defense, already tested once
2. **182.40** — rising 200-SMA (this is also ≈the 50% retracement of the 166.89 → 198.11 closing advance, at 182.50)
3. **180.17–180.30** — the 01-05 and 01-17 lows: a double bottom that has held twice
4. **178.95** — Bollinger lower band

The **180.2–182.5** zone is the highest-confluence area on the chart: a double bottom, a rising 200-day, the lower Bollinger band, and a 50% retracement all cluster there. A decisive break of that shelf would be a genuine trend event, not a routine dip.

---

## 7. Actionable playbook

**Bias: neutral-to-constructive long-term, tactically defensive short-term.** The honest read is "correction inside an uptrend, at an inflection point, with momentum still pointing down." Do not front-run a bottom; make the market prove it.

**Scenario A — Reclaim (probability-weighted preferred): long the confirmation, not the print.**
Trigger: a close **above 189.30** (clears VWMA, 10-EMA, and the 187.96 mid-band together) with volume ≥ the ~55.6M 20-day average, ideally accompanied by the MACD histogram turning back up from −0.30. Stop: **183.50** (below the 02-01 low 183.82, ≈1.05 ATR below entry) — risk ≈5.80/share. Targets: **190.76** (50-SMA, 1.4R, take partials), **195.18** (2.6R), **196.97** (3.1R).

**Scenario B — Range grind: buy the confluence shelf, size small.**
Trigger: a retest of **183.80–184.40** that holds (higher low, RSI holding above ~40). Stop: **182.00** — *below* the 200-SMA, accepting a slightly larger stop, because a stop at 182.50 sits inside the most obvious support magnet and will be swept. Risk ≈2.40/share. Target: 187.96 then 189.13. Note this setup's 1.7:1 to the mid-band is thin; treat it as a trade, not a position.

**Scenario C — Trend break: stand aside or short the failure.**
Trigger: a **close below 180.17** (breaking the double bottom) — this would also put price under the 200-SMA and the lower band simultaneously. That flips the primary-trend read from "up" to "at risk" and targets the next visible reference (no tool-supported level exists below 178.95 in this dataset, which itself argues for taking profits rather than projecting). A preliminary warning shot would be a close below **182.40** on expanding volume.

**Position sizing (ATR-based):** with ATR 3.241, a standard 2-ATR stop is 6.48 points (3.47% of price). On a $100,000 account risking 1% ($1,000), that is **≈154 shares (~$28.8k notional)**. If you use the tighter Scenario A stop (5.80 risk), size rises to ~172 shares. Nothing larger is justified while the MACD is below zero and expanding negative.

**Invalidation / what changes the view:**
- **Bullish flip:** MACD histogram turns positive again (a close above ~189.3 would likely force it), 10-EMA reclaims the 50-SMA, and RSI pushes back above 55–60.
- **Bearish flip:** a close below 183.82 that is *not* reversed intraday, or any close below 182.40, plus histogram making new lows (below −0.30).

---

## 8. Caveats and limits of this analysis

- This dataset is **price/volume/technical only** — no fundamentals, earnings dates, guidance, or news flow. The 01-02 gap and the 12-14 → 01-05 decline are described purely as price events; I am not attributing causes.
- All "support/resistance" claims are **static levels from tool output**, not proven historical bounces. The only genuinely *observed* reaction is 2024-02-01 (lower low 183.82, close 186.86 near the high). The 180.17/180.30 double low is observed as two separate intraday lows, not as a validated demand zone.
- Percentage moves are arithmetic on visible closes and are labeled as such; they are **not backtested or annualized performance claims**.
- The 02-01 reversal is a single session. Pattern claims ("coil," "compression") are descriptive geometry of the 180.2–196.4 range, not statistical forecasts.
- No divergences were "found" beyond those explicitly quantified above (price lower high 198.11 → 195.18 vs MACD lower high 3.751 → 0.951).

---

## 9. Summary table

| Dimension | Reading (2024-02-01) | Interpretation | Actionable implication |
|---|---|---|---|
| **Verified close** | 186.86 (O 183.99 / H 186.95 / L 183.82), vol 64.89M | Reversal session: lower low rejected, closed near high in top 3% of range | Bullish *signal candidate*, needs follow-through confirmation |
| **Primary trend (200-SMA)** | 182.395, rising +6.35% since 2023-11-03; price +2.45% above | Uptrend intact, unthreatened | Do not treat this as a bear market; keep long bias on the primary timeframe |
| **Medium trend (50-SMA)** | 190.762; slope decayed (+2.12 → +0.72 pts per 10 sessions); first downtick 01-31 | Decelerating; price lost it 01-30 | 190.76 is resistance, not support, until reclaimed; a close below 182.40 would be the real medium-term break |
| **Short trend (10-EMA)** | 189.128, falling 4 straight sessions; price −1.20% below | Short-term bearish | Do not chase longs below 189.1; the 10-EMA is the first proof-of-strength gate |
| **MACD / signal / hist** | −0.1376 / 0.1602 / −0.2978 | Bearish cross 01-31; zero-line cross-down 02-01; hist expanding negative | Momentum tailwind is gone; wait for histogram to stop making lower lows before adding |
| **Momentum divergence** | Price peak 198.11 → 195.18; MACD peak 3.751 → 0.951 | Lower price high on far lower momentum high | Treat 195–199 as supply; fade strength there rather than buy it |
| **RSI** | 45.07 (from 62.62 on 01-23; low 39.60 on 01-31; Jan low 28.79) | Neutral-to-weak, **not** oversold | No mean-reversion fuel; upside needs a catalyst, not a bounce reflex |
| **ATR** | 3.241 (1.73% of price); peak 3.340 on 01-18 | Elevated, cooling slightly | 1 ATR ≈ 3.24 pts; use ≥2 ATR (≈6.5) or sub-183.5 stops; size ≈154 sh per $100k at 1% risk |
| **Bollinger (secondary)** | Mid 187.959 / UB 196.972 / LB 178.946; width 9.59% (from 10.71% on 01-05) | Modest contraction after January expansion; price just below mid | 187.96 is the immediate pivot; 178.95 is the downside extreme |
| **VWMA** | 189.294, price 1.30% below but VWMA flattening since 01-29 | Recent buyers underwater; selling pressure no longer worsening | 189.3 = trapped-buyer supply; reclaiming it is meaningful, failing there is the fade |
| **Structure** | Rising lows 180.17 → 180.30 → 183.82 vs flat top ~195–196 | Coil between rising floor and flat ceiling | Play the resolution, not the middle; breakout above 189.3 or breakdown below 180.2 |
| **Highest-confluence zone** | **180.2–182.5** (double bottom + rising 200-SMA + lower band + 50% retracement) | The decision zone for the primary trend | A close below 180.17 flips the whole read bearish; until then dips are buyable with tight risk |
| **Overall stance** | Corrective pullback within an intact uptrend; momentum bearish | **Tactically defensive, strategically constructive** | Buy confirmation above 189.3 (stop 183.5, targets 190.8/195.2/197.0) or the 183.8–184.4 retest (stop 182.0); avoid the 187–189 no-man's-land |