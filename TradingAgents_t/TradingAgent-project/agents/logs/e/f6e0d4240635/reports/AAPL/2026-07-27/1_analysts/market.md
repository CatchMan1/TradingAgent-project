# AAPL — Technical Analysis Report
**Analysis date: 2026-07-27 | Latest session: 2026-07-27 | Close: $336.91**

---

## 1. Verified Data Anchor

All exact price and indicator levels below come from the `get_verified_market_snapshot` call for 2026-07-27 and the indicator series retrieved through that same simulated date. No conflicts between the OHLCV tool and the snapshot were found — both agree on the 2026-07-27 row (O 334.54 / H 339.57 / L 334.02 / C 336.91 / Vol 49.60M).

| Metric | Value (2026-07-27) |
|---|---|
| Close | 336.91 |
| Session range | 334.02 – 339.57 (5.55 pts) |
| Volume | 49,604,300 |
| 10 EMA | 326.79 |
| 50 SMA | 306.99 |
| 200 SMA | 276.38 |
| Bollinger mid / upper / lower | 317.04 / 347.08 / 287.01 |
| RSI(14) | 67.29 |
| MACD / Signal / Histogram | 8.927 / 8.816 / +1.111 |
| ATR(14) | 8.14 (2.42% of price) |
| VWMA | 324.54 |

**One data caveat:** the snapshot returns an `mfi` value of `0.6225`. That is not on the standard 0–100 scale, so I am treating it as out-of-scale/unreliable and excluding it from the analysis rather than guessing a normalization.

---

## 2. Indicator Selection (8) and Why

The regime is a **confirmed, volatility-expanding uptrend with a fresh breakout to new highs and re-accelerating momentum** — not a range, not a downtrend. That dictates trend-plus-confirmation plus a stretch gauge and a risk gauge:

| # | Indicator | Role in this regime |
|---|---|---|
| 1 | `close_10_ema` | Dynamic trend rail for the current leg; the trailing stop reference in a fast uptrend |
| 2 | `close_50_sma` | Medium-term trend spine; distinguishes "pullback in uptrend" from "trend break" |
| 3 | `close_200_sma` | Strategic bull/bear benchmark; confirms golden-cross structure |
| 4 | `macd` | Trend/momentum impulse and cross-over state on a slower timeframe than price |
| 5 | `rsi` | Overbought/oversold and, crucially here, **divergence detection** |
| 6 | `boll_ub` | Quantifies how extended price is relative to its own volatility envelope |
| 7 | `atr` | Position sizing and stop placement in a 2.4%-daily-range tape |
| 8 | `vwma` | Volume-weighted confirmation — separates a real breakout from drift |

Deliberately excluded: `macds`/`macdh` (histogram is derived arithmetically from the two verified lines and adds no independent information), `boll`/`boll_lb` (used for context only, already in the verified snapshot), `macd` duplicates, and any stochastics (redundant with RSI).

---

## 3. Trend Structure: Bullish on All Three Horizons, With a Steepening Slope

**Long term — decisively bullish.** Price (336.91) sits **+21.9% above the 200 SMA (276.38)**, and the 200 SMA itself is grinding higher every session (262.83 on 2026-05-28 → 276.38 on 2026-07-27). The 50 SMA (306.99) is **11.1% above** the 200 SMA and has risen monotonically from 274.04 (2026-05-28) to 306.99. That is a deeply entrenched golden-cross structure, established long before this window and not remotely threatened.

**Medium term — bullish and accelerating.** The 50 SMA has added roughly 33 points in two months. Price is +9.7% above it. Equally important, the 50 SMA has been **rising through the entire June drawdown** — the June selloff to 275.15 (close, 2026-06-25) never even reached the 50 SMA at that time (291.15), which is textbook "correction within an uptrend" behaviour rather than trend damage.

**Short term — bullish, with a fresh breakout.** Price is +3.1% above the 10 EMA (326.79), and that EMA has turned up sharply: 289.33 on 2026-06-29 → 319.73 on 2026-07-17 → 326.79 on 2026-07-27. Sequence of higher closes over the last four sessions: 321.66 (07-23) → 333.02 (07-24) → 336.91 (07-27), with 339.57 today's high being **the highest print in the entire 2025-12-01 → 2026-07-27 dataset**.

**Measured moves (from tool output):**
- 2026-06-25 close 275.15 → 2026-07-27 close 336.91 = **+22.4%** in roughly one month.
- 2026-06-08 intraday high 317.40 → 2026-06-25 intraday low 273.75 = **−13.8%** June drawdown, fully recovered and exceeded.
- 2026-01-20 low close 246.70 → 336.91 = **+36.6%**.

The pattern is a clean **higher-low sequence**: 246.70 (Jan) → 255.78 (Feb) → 247.99 (Mar) → 251.49 (Mar) → 273.75 (Jun) → 319.35 (Jul 23). Each pullback floor has been materially higher since March.

---

## 4. Momentum: Two-Wave Advance, But Watch the Divergences

**MACD is in a strong bullish configuration.** MACD line 8.927 > signal 8.816, histogram **+1.111**. The bullish cross occurred on **2026-07-02** (histogram flipped to +0.261 after being −2.09 on 06-30) and the MACD line has been above signal ever since.

Crucially, this is the **second momentum impulse**, not the first:
- Wave 1: histogram peaked at **+3.337** on 2026-07-17 (MACD 8.815).
- Compression: histogram collapsed to **+0.795** by 2026-07-23 (the 321.66 pullback) — note it stayed *positive*, i.e. a momentum reset, not a trend reversal.
- Wave 2: histogram re-expanded +0.908 (07-24) → **+1.111** (07-27); MACD line printed a new high of 8.927.

**However, momentum is not expanding proportionally to price.** Today's MACD line (8.927) is essentially flat versus 2026-07-21 (8.9271) and 2026-07-20 (8.883), while price has advanced from 326.59 to 336.91. This is a **nascent flat-to-negative MACD divergence** — early, not decisive, but it argues against chasing size at the highs.

**RSI is the more instructive warning.** At 67.29 it is comfortably below the 70 overbought threshold — technically still "room to run." But:
- RSI on **2026-07-17 = 71.65** with close 333.74
- RSI on **2026-07-27 = 67.29** with close 336.91 (**higher price, lower RSI → negative divergence**)
- Zooming out: RSI on **2026-05-28 = 79.79** with close 312.06 — price is now 8% higher but RSI is 12.5 points lower. That is a **multi-month momentum divergence** worth flagging.

The bullish counter-argument: RSI bottomed at **32.20 on 2026-06-25** (an oversold washout) and has since built a rising sequence (39.9 → 46.9 → 50.9 → 60.3 → 63.8 → 64.2 → 68.8 → 71.4). The 07-16/07-17 overbought reading was correctly followed by a three-session cooldown to 58.11 (07-23) *without breaking the 10 EMA on a closing basis* — the classic "overbought reset inside a trend" that typically precedes another leg higher. Today's re-acceleration to 67.29 is consistent with that.

**Net read:** momentum supports further upside, but the divergence complex means the right posture is *trail tight and add on pullbacks*, not *chase breakouts*.

---

## 5. Volatility and Band Position: Extended, But Not a Blow-Off

Bollinger geometry (verified snapshot):
- Mid 317.04, Upper 347.08, Lower 287.01
- **Bandwidth = 18.95% of the mid line** (60.07 / 317.04)
- **%B = 83.1%** — price is in the upper fifth of the envelope but **inside** it

Bandwidth has roughly **doubled**: on 2026-07-02 it was 11.9% (312.31 − 277.29 over mid 294.80); on 2026-06-12 it was 10.1%. Bands are expanding in both directions — upper band 312.31 (07-02) → 347.08 (07-27), lower band 277.29 → 287.01 (which has now *turned up*, a bullish tell as the June downside volatility dissipates).

Interpretation: **price has not closed above the upper band** during this July advance (e.g. 2026-07-17 close 333.74 vs upper band 339.20 — still inside). That is the signature of a *trend* rather than a *climax*. Blow-off tops typically show repeated closes above the upper band followed by band-walk failure. We do not have that yet. The upper band at **347.08** is the natural near-term magnet/ceiling, only 3.0% above spot.

**ATR at 8.14** (2.42% of price) is elevated versus 5.57 on 2026-05-28 and 6.79 on 2026-06-08, peaking at 8.74 on 2026-07-02 post-selloff. Volatility has settled into the 7.9–8.3 band over the last three weeks — a *stable elevated* regime, which is favourable for trend-following but demands wider stops.

---

## 6. Volume / Participation: Confirmed Trend, Unconfirmed Breakout

VWMA at **324.54** with price 3.8% above it, and VWMA rising steeply (288.84 on 06-30 → 310.27 on 07-17 → 324.54 on 07-27) confirms the uptrend is volume-weighted, not just price drift. This is the single strongest bullish confirmation in the dataset.

But the *quality* of the new high deserves scrutiny, computed from the retrieved rows:
- The breakout sessions 2026-07-15/16/17 carried elevated volume: 60.96M / 62.97M / 63.41M.
- The last three sessions carrying price to a new high were lighter: 47.49M (07-24) and 49.60M (07-27), versus a ~49M average across the 17 July sessions I can compute from the CSV.
- The largest volumes in the entire window were the **June capitulation**: 107.01M (06-25) and 261.78M (06-26) — the largest single-session print in the dataset, occurring on the *low*, which in hindsight marked the low and set up the July recovery.
- Biggest July volume: 75.35M on 2026-07-02, the launch day of the recovery leg.

**Conclusion:** volume confirms the *trend* but the marginal new high is being made on merely average volume. That is a "watch, don't chase" signal — a breakout to 342–347 on sub-45M volume would be suspicious; on 60M+ it would be a strong continuation signal.

---

## 7. Actionable Levels

| Level | Price | Source | Significance |
|---|---|---|---|
| Bollinger Upper | **347.08** | verified snapshot | Near-term upside magnet / extension cap |
| Today's high | **339.57** | verified OHLCV | Immediate breakout trigger |
| 20-day mid | **317.04** | verified snapshot | Trend benchmark; must hold on closing basis |
| 10 EMA | **326.79** | verified snapshot | First dynamic support / trailing-stop rail |
| VWMA | **324.54** | verified snapshot | Volume-weighted fair value; losing it = participation breakdown |
| 2026-07-23 low | **319.35** | verified OHLCV | Last swing low; structural pivot of the current leg |
| 2×ATR below close | **320.63** | ATR-derived | Volatility stop coincides almost exactly with the 07-23 low |
| 50 SMA | **306.99** | verified snapshot | Medium-term trend line in the sand |
| Bollinger Lower | **287.01** | verified snapshot | Now rising — regime floor |

---

## 8. Scenarios and Trade Construction

**Base case (bullish continuation, ~55% weight):** Price holds above 326.79 (10 EMA) and attacks **339.57 → 347.08**. Confirmation requires volume ≥60M and the MACD histogram expanding beyond its 07-17 peak of 3.34. Entry on a *close* above 339.57, or preferably on a pullback into 326–330.

**Pullback case (~30%):** The RSI/MACD divergences resolve via a retest of **324.54 (VWMA) → 319.35 (07-23 low)**. This zone coincides with the 2×ATR stop (320.63) and is the highest-probability accumulation area given the rising 50 SMA far below. A hold there with RSI holding 45+ keeps the trend intact.

**Bear case (~15%):** A daily close below **319.35** breaks the higher-low sequence and puts **317.04 (Boll mid) and then 307.0 (50 SMA)** in play. That would require the MACD line to cross back under its signal — histogram is currently +1.11 and would need roughly two to three consecutive down sessions of 1%+ to flip.

**Risk parameters given ATR = 8.14:**
- Trend-follower stop: **1×ATR** below entry ≈ 328.8 if entering near 337 (tight, and it sits just under the 10 EMA — expect noise stops).
- Swing stop: **2×ATR** ≈ 320.6, aligned with the 07-23 swing low. This is the more robust level.
- Position sizing: with ATR at 2.42% of price, a 1% account risk per trade implies roughly half the share count of a normal-volatility (1.2% ATR) tape. Size down accordingly.
- Because RSI sits at 67.3 and %B at 83%, prefer **scaling in** (⅓–½ initial) rather than full size at market.

**What would invalidate the bullish thesis:** (a) daily close below 319.35; (b) MACD histogram flipping negative; (c) a close below the upper band after an excursion *plus* VWMA loss — that trio is the classic trend-exhaustion sequence; (d) declining volume on any push above 339.57.

---

## 9. Summary Table

| Dimension | Reading (2026-07-27) | Verdict | Evidence |
|---|---|---|---|
| **Primary trend** | Price 336.91 vs 200 SMA 276.38 (+21.9%) | **Bullish** | 200 SMA rising 262.83 → 276.38 since 05-28 |
| **Golden cross** | 50 SMA 306.99 > 200 SMA 276.38 (by 11.1%) | **Intact, mature** | Both slopes positive |
| **Intermediate trend** | Price +9.7% above 50 SMA; 50 SMA up 33 pts in 2 mo | **Bullish** | June dip (275.15) never reached 50 SMA |
| **Short-term trend** | Price +3.1% above 10 EMA (326.79) | **Bullish, accelerating** | 10 EMA 289.33 (06-29) → 326.79 (07-27) |
| **Breakout status** | High 339.57 = highest in dataset | **New high, unconfirmed on volume** | 49.6M vs ~49M July avg |
| **MACD** | 8.927 > signal 8.816, hist +1.111 | **Bullish, 2nd wave** | Cross on 07-02; hist peak 3.337 (07-17) → 0.795 (07-23) → 1.111 |
| **MACD caveat** | MACD flat while price +3.2% since 07-21 | **Mild negative divergence** | 8.9271 (07-21) vs 8.927 (07-27) |
| **RSI** | 67.29 | **Constructive, sub-overbought** | Reset 71.65 (07-17) → 58.11 (07-23) → 67.29 |
| **RSI caveat** | Higher price, lower RSI vs 07-17 and 05-28 | **Negative divergence — caution** | 333.74/71.65 vs 336.91/67.29 |
| **Volatility envelope** | %B = 83.1%; bandwidth 18.95% (from 11.9% on 07-02) | **Extended, expanding, not blow-off** | No close above upper band in July |
| **Immediate upside target** | 347.08 (upper band), +3.0% | **Magnet** | Verified snapshot |
| **ATR / risk** | 8.14 = 2.42% of price | **Elevated, stable** | 5.57 (05-28) → 8.14; 2×ATR = 320.63 |
| **Volume confirmation** | Price 3.8% above VWMA 324.54, VWMA rising | **Confirmed trend** | VWMA 288.84 (06-30) → 324.54 (07-27) |
| **Key support ladder** | 326.79 → 324.54 → 319.35 → 317.04 → 306.99 | Rising structure | All verified levels |
| **Key resistance ladder** | 339.57 → 342–343 (07-13 high 323.45 zone extended) → 347.08 | Thin above new highs | No historical supply above 339.57 |
| **Actionable stance** | **Buy pullbacks into 326–330; trail stops near 320.6; do not chase >339.57 on light volume** | Constructive with discipline | Divergences argue for scaled entries |

**Bottom line:** AAPL on 2026-07-27 is in a well-established, multi-month uptrend that has just posted an all-time-window high at 339.57 following a textbook 22% recovery off the 2026-06-25 washout low. Trend and volume-weighting (VWMA) confirm; momentum is positive but flattening; RSI is showing a modest negative divergence; and the tape is 83% up its volatility envelope. The setup favours **owning the trend with tight, ATR-calibrated risk and adding on dips toward 326–330**, rather than initiating full size into a low-volume new high 3% below the upper Bollinger band. The single cleanest invalidation is a daily close below **319.35**.

*Data caveats: the `mfi` field returned out-of-scale (0.6225) and was excluded. The ~49M "July average volume" is my own arithmetic over the 17 July rows returned by the OHLCV tool, not a vendor-reported figure. No historical support/resistance bounces are asserted beyond levels directly evidenced in the retrieved rows.*