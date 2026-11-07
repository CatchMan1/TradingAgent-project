# AMZN — Detailed Multi-Indicator Technical Report
**As of the session of 2024-02-12 | Reference price: $172.34**

---

## 1. Verified data baseline (source of truth)

The verified snapshot for 2024-02-12 and the indicator series I pulled agree **exactly** — no discrepancies to flag.

| Item | Value (2024-02-12) |
|---|---|
| Open | 174.80 |
| High | 175.39 |
| Low | 171.54 |
| **Close** | **172.34** |
| Volume | 51,050,400 |
| Split / Dividend | 1.0 / 0.0 (price-only series; TR index = close) |

Because dividend = 0 and split = 1.0 throughout the window, the technical-total-return index is identical to the close, so all "return" figures below are pure price changes.

**Indicators on the latest session (verified):**
close_10_ema **168.03** · close_50_sma **154.52** · close_200_sma **135.94** · MACD **5.5008** · Signal **4.3832** · Histogram **+1.1176** · RSI(14) **67.90** · Boll mid **161.57** · Boll upper **176.88** · Boll lower **146.26** · ATR **3.737** · VWMA **165.00**

---

## 2. Selected indicators and why they fit this market context

The context is a **post-earnings-gap, high-momentum uptrend that is now extended and entering consolidation**. That regime needs (a) trend structure across three horizons, (b) momentum confirmation *and* exhaustion detection, (c) volatility for stop/level calibration, and (d) volume participation. My eight selections:

1. **close_10_ema** — the tightest trend trigger; the natural "first pullback" reference after a gap, and the line that separates "healthy consolidation" from "trend break."
2. **close_50_sma** — medium-term trend and the yardstick for how *stretched* price is (the core risk metric here).
3. **close_200_sma** — long-term regime anchor; it defines the primary bull structure that the other signals are traded with, not against.
4. **macd** — trend-following momentum; the only tool in the set that captures the *sustained* acceleration visible since early February. (Its signal line and histogram are derived from the same computation, so they are not separately counted to avoid redundancy.)
5. **rsi** — the divergence/exhaustion detector that a trend-only toolkit misses. In a strong trend RSI stays elevated, so I use it for *divergence and extension*, not for 70/30 reversal calls.
6. **boll_ub** — statistically scaled breakout/overbought boundary; gives a moving objective ceiling (~176.9) instead of an arbitrary resistance guess.
7. **atr** — pure risk calibration. With ATR at 3.74 (~2.2% of price) after an earnings volatility spike, stop distance must be volatility-normalized, not fixed.
8. **vwma** — volume-weighted confirmation. It answers whether the gap advance was *participated in*, which price-only averages cannot.

Deliberately **excluded**: `macds` and `macdh` (derived from `macd`, redundant as selections — though I cite their values), `boll`/`boll_lb` (I use the upper band as the trigger and reference mid/lower as components), and any oscillator that duplicates RSI's function.

---

## 3. Trend structure: clean, aligned, and stretched

**The stack is fully bullish and correctly ordered:** price 172.34 > 10 EMA 168.03 > 50 SMA 154.52 > 200 SMA 135.94.

- **200 SMA is rising without hesitation:** 124.76 (2023-12-14) → 125.05 → … → 133.61 (2024-02-01) → 135.94 (2024-02-12), gaining roughly 0.33–0.36/day recently. A steadily rising long-term average means the uptrend is being *fed by new higher closes*, not just by lagging data falling out the back.
- **50 SMA is rising faster:** 138.42 (12-14) → 151.05 (02-01) → 154.52 (02-12), ~+0.52/day. The 50 SMA sits **13.7% above** the 200 SMA, confirming a mature bullish separation rather than an early cross.
- **Price is above every average and above VWMA** — no counter-trend evidence anywhere in the stack.

**But the extension is the story.** Measured from the verified values:

| Distance from | Value | Gap ($) | Gap (%) |
|---|---|---|---|
| 10 EMA | 168.03 | +4.31 | **+2.56%** |
| VWMA | 165.00 | +7.34 | **+4.45%** |
| 50 SMA | 154.52 | +17.82 | **+11.53%** |
| 200 SMA | 135.94 | +36.40 | **+26.77%** |

An 11.5% premium to the 50 SMA is a *statistically crowded* condition. Historically these premiums tend to mean-revert via time (sideways drift) or via a sharp 1–2 ATR flush — and ATR is 3.74, so a full flush to the 50 SMA is ~4.8 ATR of downside. That does not argue against the trend; it argues against **initiating size at 172–175** rather than at the 10 EMA.

**Context on the move itself** (computed from the supplied OHLCV): 131.69 (2023-08-01) → 172.34 = **+30.9%**; 119.57 (2023-10-26 close) → 172.34 = **+44.1%** off the October low. The 2024-02-09 close of 174.45 is the highest close in the entire supplied window (since 2023-08-01).

---

## 4. The February 2 gap: the defining structural event

On **2024-02-02** AMZN opened at **169.19** versus the prior close of **159.28** — a **+6.22% opening gap** — and closed at **171.81** (+7.87% close-to-close) on **117.2M shares**, roughly 2.3–2.6× the typical ~45–50M session volume in January.

What matters technically is what happened *after*:

- **Seven consecutive sessions (02-02 through 02-12) have closed above the 169.19 gap open.** The gap has **not been filled**; the lowest post-gap intraday print is 167.33 (02-02), and the lowest post-gap close is 169.15 (02-06). Unfilled gaps of this size on heavy volume act as demand shelves, but they are also downside magnets if the shelf breaks.
- **Volume has decayed normally:** 117.2M (02-02) → 55.1M → 42.5M → 47.2M → 42.3M → 57.0M (02-09) → 51.1M (02-12). This is textbook post-event digestion, not distribution.
- **The high-water mark of the move is 175.39 (02-12), with 175.00 (02-09) just beneath it.** That 175.0–175.4 band is now the immediate supply zone.

---

## 5. Momentum: still positive, but the *rate of improvement* is fading

**MACD remains firmly bullish in absolute terms:** MACD 5.5008 vs Signal 4.3832 → histogram **+1.1176**, with the MACD line above the signal since mid-January (histogram crossed positive on 2024-01-12 at +0.094 and has stayed positive since, apart from two marginal negatives on 01-17/01-18).

The MACD line's advance is steep: 2.45 (02-01) → 3.46 (02-02) → 4.10 → 4.46 → 4.80 → 4.96 → 5.39 → **5.50 (02-12)**.

**However, the histogram is rolling over:** peak **+1.3107 on 2024-02-07**, then 1.1741 (02-08), 1.2866 (02-09), **1.1176 (02-12)**. Two of the last three sessions show contraction *while price set a new high (175.39 on 02-12 and 174.45 close on 02-09)*. That is early-stage momentum deceleration — not a sell signal (the histogram is still >1.0 and well above zero), but it is exactly the profile that precedes 3–8 session consolidations.

**RSI tells the same story more precisely.** RSI went 60.36 (02-01) → **73.78 (02-02)** → 70.69 → 68.31 → 69.62 → 68.11 → **72.43 (02-09)** → **67.90 (02-12)**.

Two readings matter:
- **RSI has not been above 70 on 02-12 despite a higher intraday high (175.39) than 02-09 (175.00) and 02-02 (172.50).** That is a *mild negative divergence* forming on the daily chart — bearish at the margin, and consistent with the MACD histogram fade.
- Equally important: RSI **never reached classic blow-off >80** during this leg, and it has repeatedly reset from ~68–73 to the high-50s/low-60s without price breaking structure (e.g., 01-29 RSI 70.41 → 01-31 RSI 53.10 with price only pulling back 161.26 → 155.20 close). That pattern — **RSI resetting through price drift rather than price collapse** — is a hallmark of a strong uptrend digesting gains, and it argues the trend has more room than an overbought reading alone would suggest.

---

## 6. Volatility and bands: expansion in the trend's direction, now compressing

- **ATR:** 2.94 (01-29) → 3.16 (02-01) → **3.88 (02-02)** → 3.84 → 3.70 → 3.62 → 3.73 → **3.737 (02-12)**. The earnings event spiked daily range expectations ~30%, and ATR has since decayed gently. At 3.74, ATR = **2.17% of price**: any stop tighter than ~$3.7 is inside normal noise and will be swept.
- **Bollinger geometry is bullish, not a squeeze:** upper band **156.46 (01-03) → 176.88 (02-12)**, lower band **143.84 → 146.26** — the upper band has expanded ~20 points while the lower band rose only ~2.4 points. Bandwidth = 30.62 points, or **18.95% of the 161.57 middle band**, i.e. volatility expanding *in the direction of the trend*.
- **Position within the bands (%b) = 0.852** — (172.34 − 146.26) / (176.88 − 146.26). Price is riding the **upper third** of the band without closing above the upper band. Riding the upper band in a strong trend is normal; it becomes an exhaustion warning only if price *closes* decisively above it and then fails.
- **Critical observation: price has NOT closed above the upper band on any session in this leg.** The 02-09 high of 175.00 and 02-12 high of 175.39 both stalled ~1.5–1.9 below the then-current upper band. The upper band at 176.88 is a genuinely untested ceiling.

---

## 7. Volume: participation confirms the trend, VWMA confirms it twice

- **VWMA = 165.00**, rising every session since 01-03 (151.25 → 165.00), and price at 172.34 is **+4.45% above it**. Because VWMA weights by actual traded volume, this says the average *dollar-relevant* transaction over the period occurred near 165 — anyone who bought the bulk of the float is in profit. That is accumulation, not distribution.
- **10 EMA (168.03) sits above VWMA (165.00)** by 3.03. Short-term price tendency is above the volume-weighted mean, which is the bullish configuration. Watch for a **cross below** — that would be the first credible sign that volume-weighted holders are being given a better exit than entry.
- The 02-02 volume spike (117.2M) was **not** followed by heavy-volume down days. The largest post-gap down-volume session was 02-12 at 51.1M — modest, and only ~2 sessions' worth of average. No distribution signature yet.

---

## 8. The 2024-02-12 session itself: a warning candle inside a bull trend

This single bar deserves isolation because it is the freshest information:

- Opened **174.80** (a gap up from 174.45), pushed to **175.39** (new high), then reversed to close at **172.34** — **below the prior day's close**.
- **Close location within the day's range = 0.21** — it closed in the **bottom 21%** of a 3.85-point range (~1.03 ATR). By contrast, 02-09 closed at 0.88 of its range and 02-02 at 0.87. This is a clear shift in intraday control.
- The bar is a **failed breakout / bearish reversal bar at the top of a seven-session range**, formed right under the untested upper Bollinger band (176.88).

Interpretation: short-term supply appeared exactly where it needed to appear — at the 175.0–175.4 level — and buyers did not defend the close. Combined with RSI's lower high (67.90) and the MACD histogram fade (1.31 → 1.12), **the near-term risk/reward for fresh longs at 172–175 is poor**. It is not a trend-reversal call: nothing has broken, MACD is still rising in absolute terms, and price remains 2.56% above the 10 EMA.

---

## 9. Actionable levels

**Resistance (upside):**
- **175.00** — 02-09 high (first shelf)
- **175.39** — 02-12 high, the current swing high
- **176.88** — Bollinger upper band; the trigger level for a genuine breakout continuation. A daily close above this, on volume ≥ ~57M (the 02-09 post-gap peak), would re-open the trend and invalidate the 02-12 reversal bar.

**Support (downside), in order of likely first touch:**
- **171.54** — 02-12 low. Losing this confirms the reversal bar and opens 170.
- **170.31–170.55** — 02-05 close / 02-05–02-07 congestion
- **169.19** — the 02-02 gap **open**. This is the single most important near-term line: a daily close below it breaks the seven-session post-gap floor.
- **168.03** — 10 EMA; the "healthy pullback" target and the best long-entry reference
- **167.33 / 167.65** — 02-02 and 02-06 lows (post-gap intraday floor)
- **165.00** — VWMA (volume-weighted cost basis of the move)
- **161.57** — Bollinger middle / 20-SMA; coincides with the top of the unfilled gap zone
- **159.28** — 02-01 close; a full gap fill. 5.9 ATR away — a low-probability, high-consequence scenario.

---

## 10. Trade plans

**Bias: bullish primary trend, neutral-to-cautious short-term. Prefer buying pullbacks over chasing breakouts.**

**Plan A — Pullback accumulation (preferred)**
- Entry zone: **168.00–169.20** (10 EMA + gap-open confluence). Scale in: 50% at 169.0, 50% at 168.0.
- Stop: **166.00** — below the 10 EMA *and* below the 02-02 low of 167.33, giving ~1.4% risk from a 168.5 average entry (~0.7 ATR). Use a *close* basis to avoid ATR noise sweeps, or widen to 165.40 (≈1 ATR below the gap-day low).
- Targets: T1 175.00, T2 176.88 (upper band); trail remainder behind the 10 EMA.
- Invalidation: daily close below 167.33 with volume >50M ⇒ stand aside, the post-gap shelf is gone.

**Plan B — Breakout continuation**
- Trigger: **daily close > 176.88** with volume ≥ 57M.
- Stop: 1.5 × ATR = **5.61 points** below the entry close (≈171.3 from a 176.9 entry).
- Note the asymmetry: the entry is ~4.5% above the 10 EMA, so position size should be **reduced ~30–50%** versus Plan A to keep portfolio risk constant.

**Plan C — Short-term tactical short (counter-trend, small size, aggressive only)**
- Setup: rejection at 175.0–175.4 already printed (02-12). Entry on a break of **171.54** with a stop above 175.40 (risk ~3.9 = 1.03 ATR).
- First target 169.19 (gap open), second 168.03 (10 EMA). Risk/reward ≈ 0.6:1 to the first target and 0.9:1 to the second — **marginal**. This is only defensible as a short-leash tactical trade; it fights a 50-SMA-rising, MACD-positive trend. I would size it at ≤½ of a trend position, if at all.

**Risk management / sizing**
- ATR-normalize everything: 1 ATR = **$3.74 (2.17%)**. Stop distances of 1.5 ATR = $5.61; 2 ATR = $7.47.
- With a 1% capital risk budget and a 5.6-point stop, notional = (0.01 × capital) / 5.6 per share — e.g., $100k capital ⇒ ~$1,785 of exposure per 1%-risk unit at that stop.
- **Do not add to a position at 172–175.** The 11.5% premium to the 50 SMA is the dominant risk factor right now, and the 02-12 bar says the marginal buyer is already exhausted at these levels.

**What would change the thesis:** (1) daily close below 167.33 → trend break, gap-fill risk; (2) MACD histogram turning negative (currently +1.12) → momentum regime change; (3) 10 EMA crossing below VWMA → volume-weighted holders underwater; (4) RSI making a lower high while price makes a higher high at a *new* swing above 175.39 → confirmed divergence. Conversely, a volume-backed close above 176.88 reasserts the trend and would justify re-adding on the next 10 EMA retest.

---

## 11. Summary table

| Dimension | Indicator | Latest value (2024-02-12) | Signal | Evidence / note |
|---|---|---|---|---|
| **Price** | Close | **172.34** | Neutral / caution | Opened 174.80, high 175.39, low 171.54; closed in bottom **21%** of range after a new high — bearish reversal bar |
| Short trend | close_10_ema | 168.03 | Bullish | Price **+2.56%** above; rising every session; first pullback reference |
| Medium trend | close_50_sma | 154.52 | Bullish but extended | Rising ~+0.52/day; price **+11.53%** above — crowded |
| Long trend | close_200_sma | 135.94 | Bullish | Rising ~+0.34/day; price **+26.77%** above; 50 SMA 13.7% above 200 SMA |
| Momentum | macd | 5.5008 | Bullish | Above signal (4.3832); MACD line 2.45→5.50 since 02-01 |
| Momentum trend | macdh (derived) | +1.1176 | Fading | Peaked **+1.3107 on 02-07**; contracting while price made new highs |
| Overbought | rsi | 67.90 | Caution | Lower high vs 72.43 (02-09) / 73.78 (02-02) → mild negative divergence; but repeated 68→55 resets without price damage = healthy digestion |
| Volatility band | boll_ub | 176.88 | Untested ceiling | Upper band 156.46 (01-03) → 176.88; price has **not closed above it** this leg; %b = 0.852 |
| Volatility | atr | 3.737 | Elevated | 2.17% of price; spiked 3.16→3.88 on 02-02 gap, now decaying; 1 ATR = $3.74 |
| Volume | vwma | 165.00 | Bullish | Rising daily; price **+4.45%** above; 10 EMA (168.03) above VWMA — accumulation intact |
| **Structure** | 02-02 gap | Open 169.19 vs 159.28 prior close | Bullish shelf | +6.22% gap on 117.2M shares; **7 sessions** held above gap open, unfilled |
| Volume pattern | — | 51.1M (02-12) | Neutral / constructive | 117.2M spike → 42–57M digestion; no high-volume distribution day |
| **Key resistance** | — | 175.00 / 175.39 / **176.88** | Breakout trigger | Close >176.88 on ≥57M volume = trend reassertion |
| **Key support** | — | 171.54 / **169.19** / 168.03 / 167.33 / 165.00 / 161.57 | Risk ladder | Close <169.19 breaks post-gap floor; <167.33 = trend break |
| **Stance** | — | **Buy dips, don't chase** | — | Bullish regime, extended price; preferred entry 168.0–169.2, stop 166.00 |