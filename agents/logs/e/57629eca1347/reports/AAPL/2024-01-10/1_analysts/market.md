# AAPL — Multi-Timeframe Technical Review (as of the 2024-01-10 session)

## 1. Data verification & scope

Everything below is anchored to the **verified snapshot for AAPL as of 2024-01-10** and the indicator series returned for the same date. The two sources agree exactly on every overlapping value (close_50_sma 188.4114, close_10_ema 186.8429, 200 SMA 180.4146, MACD −1.6075, signal −0.4115, histogram −1.1960, RSI 43.33, ATR 3.0132, VWMA 188.0312), so **no discrepancy needs flagging**. The verified latest row:

| Field | 2024-01-10 |
|---|---|
| Open | 184.35 |
| High | 186.40 |
| Low | 183.92 |
| **Close** | **186.19** |
| Volume | 46,792,900 |

One methodological note: the indicator history extends further back than the OHLCV file I pulled (the 200-SMA series starts 2023-09-12), so I treat the vendor's SMA/MACD/RSI values as authoritative for their own lookback and only make level/percentage claims I can derive from printed prices and printed indicator values.

---

## 2. The core picture: intact primary uptrend, unfinished intermediate correction

AAPL is in a **two-speed setup**. The long-term structure is still bullish, while the short-term and intermediate-term structure has been damaged since mid-December. Three facts define this:

**Bullish structural evidence (slow timeframes):**
- Close 186.19 sits **+3.20% above the rising 200-day SMA (180.4146)**.
- The 200-SMA has risen every single session in the printed series, from 175.2672 (2023-12-01) to 180.4146 (2024-01-10). That is +5.15 points in about 27 sessions (~+0.19/session) — and *faster* than its earlier pace (168.0363 on 2023-09-12 → 175.2672 on 2023-12-01, ~+0.13/session). The long-term trend is not just up, it is **accelerating**.
- The **50-SMA (188.4114) is well above the 200-SMA**, a golden-cross configuration, and the spread (about 8.0 points, ~4.4%) has been widening (2023-12-01: 179.4516 vs 175.2672 = 4.18 gap → 2024-01-10: 8.00 gap).

**Bearish intermediate evidence (fast timeframes):**
- Price is **below the 50-SMA by 1.18%** (186.19 vs 188.4114), below the **10-EMA by 0.35%** (186.8429), below **VWMA by 0.98%** (188.0312) and **2.68% below the Bollinger mid (191.3235)**.
- The 50-SMA's *rate of change* is decaying: +0.434/session between 2023-12-01 (179.4516) and 2023-12-15 (183.7876), versus **+0.269/session** between 2024-01-03 (187.0648) and 2024-01-10 (188.4114) — roughly a 38% deceleration. A flattening 50-SMA directly overhead is exactly what you do *not* want to see on a bounce attempt.

**The key measurement — the December–January distribution:**
- Peak close **198.11 (2023-12-14)**, with intraday peak **199.62** the same day — the highest print in the visible window (data begins 2023-07-03).
- Trough close **181.18 (2024-01-05)**, intraday low **180.17**.
- That is **−8.54% on closes** (181.18/198.11) and −9.74% intraday.
- The decisive event was **2024-01-02**: previous close 192.53 (2023-12-29) → open 187.15, i.e. a **−2.79% gap down**, followed by a −3.58% down day to 185.64 on **82.49M shares** (the heaviest volume since the 128.54M quad-witching session on 2023-12-15). That gap zone, **187.15–192.53, remains unfilled**, and it is now the central overhead supply shelf.
- From the 2024-01-05 low the stock has clawed back **+2.76%** (181.18 → 186.19) in three sessions, but on *shrinking* volume.

So the honest read is: **bullish primary trend, bearish-to-neutral intermediate trend, tentative short-term stabilization.**

---

## 3. Momentum: the reset is real, the reversal is not yet proven

**MACD family (12/26/9):** the deterioration is unambiguous and well-documented by the printed series.
- Bearish crossover (MACD below signal) occurred on **2023-12-19** (MACD 3.5022 vs signal 3.5590). MACD had peaked at **3.7507 on 2023-12-15** — a full session *after* the price peak at 198.11 on 2023-12-14. That one-day lag is a textbook momentum roll-over.
- MACD then crossed **below zero on 2024-01-03→2024-01-04** (0.0549 → −0.7023), and the signal line followed below zero on **2024-01-09** (−0.1125). Both lines are now negative — a "confirmed bear" MACD state, not a mere wiggle.
- **However**, the histogram is contracting: from −1.747 (2024-01-08) to −1.499 (2024-01-09) to **−1.196 (2024-01-10)**. Two consecutive sessions of downside-momentum deceleration. This is the earliest, weakest but most timely bullish tell in the whole report — and it is *not* yet a buy signal, because the MACD line is still falling (best case −1.6075 on 01-10 vs −1.6110 on 01-09 is a near-flat 0.0036 tick).

**RSI(14):** 43.33 today. The sequence is the important part:
- 70.02 on **2023-12-08** (the only overbought print in the window) while price closed 195.71; price then made a **higher close of 198.11 on 2023-12-14 with a lower RSI of 69.69** — a **mild bearish momentum divergence** that preceded the whole decline.
- Capitulation reading: **28.79 on 2024-01-05** (only oversold print in the window), 29.78 on 2024-01-04.
- Recovery: 41.34 (01-08) → 40.60 (01-09) → **43.33 (01-10)**. RSI has lifted ~14.5 points off the low *without* price making a lower low (01-08 low 181.50 > 01-05 low 180.17) — a constructive higher-low + rising-RSI combination.
- Critically, RSI at 43 is **neither oversold nor overbought**. The easy "buy the flush" trade is already gone; this is now a *trend-resumption* question, not a mean-reversion question. RSI needs to reclaim ~50–55 to validate a genuine shift in control.

---

## 4. Volatility & bands: cheap entry, wide stops, confluence at 180

- **ATR(14) = 3.0132**, i.e. **1.62% of price**. ATR expanded from 2.5746 (2023-12-29) to 3.0132 (2024-01-10), about **+17%** — volatility expanded *into* the decline, a risk-off signature, and it has stayed elevated even as price bounced. Stops sized off December's 2.57 ATR are now too tight.
- Bollinger (20,2): mid **191.3235**, upper **202.6208**, lower **180.0262**, bandwidth ~22.59 points (11.8% of the mid).
- Price at 186.19 is at **%B ≈ 0.27** — lower third of the band, below the mid, not at the lower band. There is room to fall inside the band before a statistical "stretched" condition appears.
- **The single most important confluence in this chart: the Bollinger lower band (180.0262) and the rising 200-SMA (180.4146) sit 0.39 points apart, and the 2024-01-05 intraday low was 180.17 — literally inside that cluster.** That 180.0–180.4 zone is the line in the sand for the entire bullish thesis.

---

## 5. Volume: distribution on the way down, apathy on the way up

- The decline was **volume-confirmed**: 82.49M on 2024-01-02, 72.00M on 2024-01-04, 62.38M on 2024-01-05.
- The rebound has been **volume-starved**: 59.14M (01-08), 42.84M (01-09), 46.79M (01-10). The 21-session mean volume from the printed rows is roughly **56.6M**, so today's 46.79M is about **17% below average**. A rally on fading volume is a *counter-trend bounce* until proven otherwise.
- **VWMA = 188.0312 vs close 186.19**: the volume-weighted average participant is **underwater by ~0.98%**. That is a direct, mechanical description of overhead supply — sellers are sitting between 188 and 192.5. VWMA has declined for eight straight sessions (195.53 on 2023-12-26 → 188.03 on 2024-01-10), confirming that recent volume has been transacted at progressively lower prices.

---

## 6. Actionable map of levels

**Resistance (in order of importance):**
1. **186.84** — 10-EMA. First hurdle; price is 0.35% below it. A close above it puts the short-term trend back to neutral.
2. **188.03 / 188.41** — VWMA and 50-SMA, stacked within 0.4 points. This is the *real* test. Reclaiming it converts the bounce into a trend-repair.
3. **191.32** — Bollinger mid (20-SMA).
4. **192.53** — 2023-12-29 close; filling this closes the 187.15–192.53 gap. This is where the December breakdown is objectively repaired.
5. **194.83–195.71** — December congestion; **196.95–199.62** is the December supply top.

**Support:**
1. **183.92** — today's low; short-term pivot.
2. **181.18–181.50** — 2024-01-05 close / 2024-01-08 low.
3. **180.03–180.41** — Bollinger lower + 200-SMA + 01-05 intraday low 180.17. **Primary structural support.**
4. Below that: **178.85** (2023-08-07 close) and **176.38** (2023-11-01 close region / 176.57 2023-08-16).

---

## 7. Trade construction

**Bias: neutral-to-constructive, with a strict "prove it" filter.** The primary uptrend, rising 200-SMA, widening golden cross and the RSI/MACD-histogram stabilization argue *against* shorting into support. But the falling MACD, price below the 50-SMA/VWMA, the unfilled 187.15–192.53 gap and the light-volume bounce argue *against* blindly buying 186.

**Scenario A — Trend resumption (primary plan).** Trigger: a daily close **above 188.41** (50-SMA) on volume ≥ ~56M (21-session mean), ideally with MACD histogram continuing to narrow. Entry ~188.4–189.0; stop 1×ATR below the trigger low, or hard stop **below 185.50** (under the 10-EMA/prior pivot) for a tight version, or **below 180.0** for a swing version. Targets: 191.32 → 192.53 (gap fill) → 194.83. Risk/reward on the swing version: ~7.5 points risk to first target ~4.9 points, ~1:1 to T1 and ~1:2 to T3 — therefore **scale out at 191.3 and 192.5 rather than holding for the December high.**

**Scenario B — Failed bounce / roll-over (risk plan).** Trigger: rejection at 186.8–188.4 followed by a close **below 183.92**. Then the 181.18–181.50 shelf, and a break of **180.0** would target 178.85 then 176.38–177.00. Note that a break of 180.0 also breaks the 200-SMA, which is the formal end of the primary uptrend — that is the point at which the whole framework flips from "buy the dip" to "reduce exposure."

**Scenario C — Choppy drift (highest probability near term).** Given RSI 43 (mid-range), ATR 1.62%, and two sessions of histogram contraction without a cross, the most likely path is **186–189 chop** while the 50-SMA continues to flatten toward price. In this regime, neither the long nor the short has an edge; the correct action is to do nothing until 184.0 or 188.5 breaks.

**Risk management specifics:**
- 1 ATR = 3.01 points (1.62%). Position size so that a stop at 180.0 from ~186.2 (a 6.2-point / 3.3% move, ≈2 ATR) costs no more than your per-trade loss budget. A 2-ATR stop is required here precisely *because* volatility expanded ~17% since 2023-12-29.
- Avoid placing stops exactly at 180.17/180.41 — that cluster is obvious and will be probed. Use 179.85–179.95.
- Do not chase strength into 188.5–192.5 on sub-50M volume; that zone is where the Jan 2 gap sellers are trapped long.

---

## 8. What would change my mind

- **Bullish confirmation:** close > 188.41 on volume > 56M, *plus* MACD line crossing back above signal (currently −1.6075 vs −0.4115 — a gap of 1.196 still to close).
- **Bullish invalidation:** any close < 180.0 (breaks the 200-SMA and the lower Bollinger band simultaneously).
- **Short-side confirmation:** a lower high below 188.4 followed by a close below 183.92; MACD histogram re-expanding negatively after this two-session contraction.

---

## 9. Summary table

| Dimension | Reading (2024-01-10) | Interpretation | Actionable level / trigger |
|---|---|---|---|
| Close / latest bar | 186.19 (H 186.40, L 183.92, O 184.35, Vol 46.79M) | Third up-session off the low; +2.76% from 181.18 (01-05) | Needs > 188.41 to matter |
| 200-SMA | 180.4146, rising ~+0.19/session (was 175.2672 on 12-01) | **Primary uptrend intact and steepening** | Close < 180.0 = thesis broken |
| 50-SMA | 188.4114, but slope decayed ~38% (0.434 → 0.269 pts/session) | Golden cross **intact** (8.0 pt spread) but intermediate trend flattening | Reclaim 188.41 = repair |
| 10-EMA | 186.8429, price 0.35% below | Short-term trend still down | Close > 186.84 = neutral |
| MACD / Signal / Hist | −1.6075 / −0.4115 / **−1.1960** | Bear cross since 12-19; zero-line break on 01-04; **histogram narrowing 2 sessions** (−1.747 → −1.499 → −1.196) | Histogram positive + line above signal = buy trigger |
| RSI(14) | 43.33 (low 28.79 on 01-05; 70.02 peak on 12-08) | Oversold reset **completed**; bearish divergence at the 12-14 high already paid off | > 50–55 to confirm control shift |
| Bollinger (20,2) | Mid 191.3235 / UB 202.6208 / LB 180.0262; %B ≈ 0.27 | Lower third of band; **LB + 200-SMA + 01-05 low cluster at 180.0–180.4** | 180.0–180.4 = decisive support |
| ATR(14) | 3.0132 (1.62% of price), up ~17% since 2.5746 on 12-29 | Volatility expanded into the decline and has not faded | Size stops at ~2 ATR; stop 179.9 |
| VWMA | 188.0312, price 0.98% below; 8 straight down sessions | Volume-weighted buyer is underwater → overhead supply 188–192.5 | Bull case requires reclaiming 188.03 |
| Volume profile | 82.49M (01-02), 72.00M (01-04) down; 42.84M (01-09), 46.79M (01-10) up; vs ~56.6M 21-session mean | **Distribution down, apathy up** — bounce is unconfirmed | Need ≥ 56M on the breakout close |
| Gap | 2023-12-29 close 192.53 → 2024-01-02 open 187.15 (−2.79%), unfilled | 187.15–192.53 is the supply shelf | Fill at 192.53 = full repair |
| Drawdown | 198.11 (12-14 close) → 181.18 (01-05 close) = **−8.54%**; intraday 199.62 → 180.17 = −9.74% | Normal correction inside an uptrend — so far | −10%+ and loss of 200-SMA = trend change |
| **Verdict** | **Bullish primary / bearish intermediate / stabilizing short-term** | Buy confirmation, not anticipation | Long trigger > 188.41 on >56M vol; abort < 183.92; invalid < 180.0 |