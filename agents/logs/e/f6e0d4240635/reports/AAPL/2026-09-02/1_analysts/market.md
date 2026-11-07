# AAPL — Multi-Timeframe Technical Report
**As of the 2026-09-02 close | Verified snapshot source: B‑project frozen rows**

---

## 1. What the tape actually shows (verified)

| Item | Value |
|---|---|
| 2026-09-02 OHLC | O 326.87 / H 328.40 / L 323.53 / **C 324.96** |
| Volume | 33.78M (vs. 53.17M on 9/01) |
| Prior session (9/01) | C 325.13, H 327.30, Vol 53.17M |
| 50-SMA | 313.55 |
| 200-SMA | 283.33 |
| 10-EMA | 317.45 |
| MACD / Signal / Hist | 1.896 / 0.137 / **+1.759** |
| RSI(14) | 60.86 |
| Bollinger (20,2) | Mid 312.02 / **Upper 324.65** / Lower 299.38 |
| ATR(14) | 7.43 (≈2.29% of price) |
| VWMA | 313.89 |

The snapshot and the historical indicator series are **internally consistent** (MACD 1.8962, signal 0.1374, RSI 60.857, Bollinger mid 312.018, ATR 7.4286, VWMA 313.887 all match exactly). One data-integrity note: the snapshot's `mfi` field reads **0.6529**, which is a 0–1 scale rather than the usual 0–100, so I have excluded it rather than misreport it. No OHLCV conflicts were found between the two tools.

---

## 2. The one fact that dominates this chart

On **2026-07-31** AAPL opened at **304.81** against the prior close of **333.43 (7/30)** and closed at **308.91 — a −7.36% single-session repricing on 132.49M shares**, roughly 3× the recent average. The prior day's low was 329.59 and the 7/31 high was 310.69, leaving a **≈18.9-point unfilled gap band between 310.69 and 329.59**. The swing high immediately before the break was **344.57 (7/29 intraday)**; the post-break low was **300.00 (7/31) / 302.25 close (8/12)**.

Everything since has been a **recovery attempt into that gap**. At 324.96, price has retraced roughly **75% of the 310.69–329.59 gap** and about **56% of the full 344.57 → 300.00 decline** (the 50% level sits at 322.29; the 61.8% at **327.55**, right under the 9/2 high of 328.40). Context: +19.9% from the 2026-01-02 close (271.01) and +41.5% from 229.72 on 2025-09-02 — the long-term trend is intact.

---

## 3. Indicators selected (8) and why

| # | Indicator | Why it earns a slot in *this* market |
|---|---|---|
| 1 | **close_200_sma** | Defines whether the July gap was a trend break or a shakeout. It is the line that says "structurally, nothing broke." |
| 2 | **close_50_sma** | The battleground of August — price oscillated around it for six weeks; it is now the medium-term pivot. |
| 3 | **close_10_ema** | The gap-retracement is a fast move; this captures it and gives the nearest trailing reference. |
| 4 | **macd** | The zero-line is the cleanest read on whether the August downtrend has actually reversed rather than just bounced. |
| 5 | **macds** | Needed to date the crossover objectively (a crossover without a date is a story, not evidence). |
| 6 | **rsi** | Calibrates how much of the bounce is already "used up" before the gap-fill resistance bites. |
| 7 | **boll_ub** | Price is closing *above* the upper band — the key "extension vs. breakout" question for the next 1–3 sessions. |
| 8 | **atr** | Volatility collapsed post-event; ATR sets defensible stops and position size. |

*Deliberately excluded:* a second oscillator (stochastic/RSI variants — redundant), and I used Bollinger mid/lower plus VWMA as cross-checks rather than as separate selections since VWMA (313.89) is within 0.11% of the 50-SMA (313.55).

---

## 4. Trend analysis

### 4.1 Long term: uptrend, unbroken
- **200-SMA 283.33 and rising** (280.67 on 8/17 → 283.33 on 9/02, +2.66 in 16 sessions).
- Price is **+14.7% above the 200-SMA**. Even at the 8/12 low close of 302.25, price never came within 7% of it. The 7/31 event was a **valuation reset inside a bull trend**, not a structural breakdown.
- **50-SMA (313.55) sits 30.2 points above the 200-SMA**, and the spread is *widening* (28.4 on 8/17 → 30.2 on 9/02). Bullish long-term alignment.

### 4.2 Medium term: 50-SMA has stopped falling and turned up
- 50-SMA bottomed at **309.08 on 8/17** and has risen every session since: 309.44 (8/19) → 310.50 (8/24) → 311.22 (8/26) → 312.00 (8/28) → 313.55 (9/02).
- The price/50-SMA relationship is the clearest April–September tell: price **lost** it on 8/10–8/17 (closes 308.26, 304.91, 302.25, 305.26, 305.93, 305.59 vs. a rising average), **reclaimed** it on 8/18 (310.03 vs 309.13), **slipped below again** 8/21–8/25 (309.35, 310.34, 309.90), and then **broke out decisively above** on 8/26 (313.45) through 9/02 (324.96). Three failed retests followed by a hold is a constructive pattern — but it also means **313.5 is now the "line in the sand" for the medium-term thesis**.

### 4.3 Short term: clean bullish stack
- **10-EMA 317.45 > 50-SMA 313.55 > 200-SMA 283.33** — a fully aligned short-term uptrend.
- The 10-EMA crossed above the 50-SMA on **8/28** (313.01 vs 312.00) and has risen from **308.76 (8/17) to 317.45 (9/02)**, a +8.7-point slope in 11 sessions.
- Price is **+2.36% above the 10-EMA**, which is a normal working distance in an uptrend but leaves little cushion for a bad open.

### 4.4 Momentum: the reversal is new, dated, and accelerating
- **MACD crossed above its signal on 8/26** (histogram flipped from −0.149 on 8/25 to **+0.152**).
- **MACD crossed above zero on 8/31** (+0.297, after −0.028 on 8/28) — the first positive MACD reading since **8/10**.
- The **signal line crossed zero on 9/02** (0.137). Both lines are now positive: a fully reset momentum regime.
- The **histogram has expanded for five straight sessions**: 0.896 (8/28) → 0.977 (8/31) → 1.511 (9/01) → **1.759 (9/02)**. This is genuine acceleration, not a one-day blip.
- For symmetry: the MACD peak before the crash was 9.61 (7/29), so the current 1.90 is early-cycle, not late-cycle.

### 4.5 RSI: room, but no longer cheap
- RSI bottomed at **40.20 (8/12)**, printed **43.24 on the 7/31 crash day**, and has climbed to **60.86**.
- It is **not overbought**; RSI sat at 71.4–71.6 on 7/16–7/17 near 333, so there is technical headroom toward ~70 (roughly 328–335 in price terms).
- Note the slight stall: 61.06 (9/01) → 60.86 (9/02) while price closed marginally lower. Not a divergence (price also fell), but the *rate of change* of momentum is flattening right at gap resistance.

### 4.6 Volatility and Bollinger: squeeze → expansion, and price is riding the upper band
- Bollinger width collapsed from **20.3%** on 7/24 (upper 346.36 / lower 282.41) to **5.0%** on 8/27 (upper 317.04 / lower 301.61) — a textbook post-event squeeze.
- It has now **expanded to 8.1%** (upper 324.65 / lower 299.38), with the bands turning *up* (mid 309.32 on 8/27 → 312.02 on 9/02).
- **Closing price is above the upper band for the third time in four sessions** (8/28: 319.70 vs 318.86; 9/01: 325.13 vs 322.39; 9/02: 324.96 vs 324.65). In strong trends this is a continuation signal; late in a retracement it is a stretch signal. The tiebreaker is volume — and 9/02 volume (33.8M) was **~16% below the 21-session average of ~40.3M**, versus 9/01's 53.2M (**+32% above average**). So the breakout day had volume confirmation; the stalling day did not.
- **ATR 7.43** (2.29% of price), down from 9.87 on 7/31 and 8.55 on 8/12. Volatility is normalizing, which argues for **tighter stops than August would have required** but also means a 2×ATR stop (~14.9 points) is now affordable.

### 4.7 Candle read for 9/02
Open 326.87, high 328.40, close 324.96 — closed **1.91 below the open and 1.43 off the low**, i.e., a bearish-bodied session that closed in the bottom third of its range, on light volume, right at the upper band and at the 61.8% retracement (327.55). That is the profile of **supply appearing at gap resistance**, not of a breakout continuing.

---

## 5. Key levels (all tool-derived)

**Resistance**
1. **327.55** — 61.8% retracement of 344.57→300.00 (price is 2.6 points below it)
2. **328.40** — 9/02 intraday high; **329.59** — 7/30 low, i.e., gap-fill completion
3. **333.43–334.75** — 7/30 close / 7/30 high; the origin of the crash candle
4. **344.57** — 7/29 intraday high, the highest print in the supplied history (price is **−5.69%** below it)

**Support**
1. **322.29** — 50% retracement of the July–August decline; failure here = failed gap fill
2. **317.45** — 10-EMA (first dynamic support)
3. **313.55–313.89** — 50-SMA / VWMA cluster, the August battleground
4. **312.02** — Bollinger mid; then **309.08–310.69** (50-SMA's August low + 7/31 high)
5. **302.25 / 300.57** — 8/12 close / 8/12 low; **299.38** — lower Bollinger band

**Volume-derived view (VWMA):** VWMA at **313.89** is rising for the third session (310.80 → 312.49 → 313.89) and price is **+3.5% above it** — buyers who transacted in size since mid-August are in profit, which supports dips. But the VWMA's slow climb versus price's fast one is the gap between "volume-backed" and "thin rally" — 9/02's low-volume stall is the caution flag.

---

## 6. Actionable plan

**Bias: constructive but tactically late.** The medium- and long-term structure is bullish; the short-term move is extended into a defined resistance band (327.5–329.6) with a stalling, low-volume candle.

**Setup A — Pullback accumulation (preferred, better R:R)**
- Entry zone **317.5–319.5** (10-EMA / prior breakout shelf).
- Stop **312.00** (below Bollinger mid and the 50-SMA) — risk ≈ 5.5–7.5 points.
- Targets **328.40**, then **334.00**. R:R ≈ 1.5–2.4.
- Invalidation: a **close below 313.5** (50-SMA) while MACD histogram contracts.

**Setup B — Gap-fill breakout (momentum)**
- Trigger: a **close above 329.59** on volume ≥ 50M (i.e., ≥ the 9/01 print).
- Stop **322.20** (50% retracement) — risk ≈ 7.4 points (1×ATR).
- Target **334.75**, then **344.50**. R:R ≈ 0.7–1.5 (thin; only worth it with volume confirmation).
- Avoid buying 325–328.5 here: reward to 334.75 is ~9.8 points against ~11.5 points of risk to the 50-SMA. **Negative R:R.**

**Setup C — Fade / hedge signal (for holders)**
- If price closes back **below 322.29** and the MACD histogram rolls over from +1.76, treat the 8/26–9/02 advance as a completed gap-fill retracement and reduce exposure; next real support is 313.5, then 309.

**Risk management**
- Stop distance = **1.5×ATR ≈ 11.1 points**; with ATR at 2.29% of price, a 1%-of-$10,000 risk budget ($100) at an 11-point stop implies **~9 shares**.
- Position size *up* only if ATR continues to compress below 7.0; size *down* if ATR re-expands above 8.5 (the 8/12–8/14 regime).
- There is no confirmed bearish divergence yet, but the **upper-band + fib-61.8% + light-volume stall** combination is the earliest warning. Treat 328.40 as a decision level, not a target to chase.

**What would change the view**
- **Bearish flip:** close below 313.5 with a negative MACD histogram → the 7/31 gap-fill fails and the August range (300–320) reasserts.
- **Bullish confirm:** close above 329.59 with ≥50M shares → gap fill completed, and the 333.43–344.57 zone becomes the next objective (a +2.9% to +6.1% move from 324.96).

---

## 7. Summary table

| Dimension | Reading (2026-09-02) | Evidence | Implication |
|---|---|---|---|
| Long-term trend | **Bullish** | Price 324.96 vs 200-SMA 283.33 (+14.7%); 200-SMA rising 280.67→283.33 | Stay structurally long; July drop was a reset, not a reversal |
| Medium-term trend | **Repaired / bullish** | 50-SMA bottomed 309.08 (8/17) → 313.55; 50>200 by 30.2 pts, spread widening | 313.5 is the thesis invalidation line |
| Short-term trend | **Bullish, extended** | 10-EMA 317.45 > 50-SMA 313.55; price +2.36% above 10-EMA | Chasing here is poor R:R |
| Momentum | **Fresh bullish regime** | MACD 1.896 > signal 0.137; crossed signal 8/26, zero 8/31; histogram 5 sessions of expansion (0.90→1.76) | Trend-following bias valid, still early cycle |
| RSI | **60.86 — constructive, not overbought** | Up from 40.20 (8/12); prior peak 71.4–71.6 (7/16–7/17) | Room to ~70 ≈ 328–335, but gain rate is flattening |
| Volatility | **Post-event squeeze now expanding** | ATR 7.43 (2.29%); BB width 5.0% (8/27) → 8.1% (9/02) | Tighter, ATR-sized stops are viable |
| Bollinger | **Riding the upper band** | Upper 324.65 vs close 324.96; 3 of last 4 closes above band | Breakout *or* exhaustion — volume decides |
| Volume / VWMA | **Supportive but weakening** | 9/01: 53.2M (+32% vs ~40.3M avg); 9/02: 33.8M (−16%); VWMA 313.89, rising 3 sessions | Buyers in control, but 9/02 lacked conviction |
| Structure / gap | **75% of gap filled** | Gap 310.69–329.59; 61.8% fib at 327.55; 9/02 high 328.40 | Heavy resistance 327.5–329.6 |
| Key resistance | **327.55 / 328.40 / 329.59 / 333.43 / 344.57** | Fib + 7/30 low/close/high + series high | Breakout requires a close >329.59 on ≥50M volume |
| Key support | **322.29 / 317.45 / 313.55 / 312.02 / 302.25** | Fib 50%, 10-EMA, 50-SMA & VWMA, BB mid, 8/12 low | Close <313.5 = failed retracement |
| Tactical stance | **Constructive, buy dips not breakouts** | Negative R:R from 325 to 334.75 vs 313.5 stop | Preferred entry 317.5–319.5; stop 312.0 |

*Caveats: this is a purely technical read of frozen price/indicator data. The 7/31 −7.36% gap is an observed fact; its cause is not established by the available tools. No fundamental, catalyst-calendar, or positioning data was used, and no historical backtest of these signals was performed.*