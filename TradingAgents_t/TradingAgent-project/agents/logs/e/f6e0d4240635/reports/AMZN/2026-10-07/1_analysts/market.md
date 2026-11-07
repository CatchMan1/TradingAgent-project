## AMZN — Multi-Timeframe Technical Assessment

**Reference data:** Verified snapshot for 2026-10-07 plus daily OHLCV from 2026-04-01 to 2026-10-07 (131 rows).

---

### 1. Market Context and Regime

AMZN closed **2026-10-07 at 259.92**, up **+1.42%** from 256.29 on 2026-10-06, on volume of **36.23M**. The session opened at 254.23 (below the prior close), sold to 253.17, then closed at 259.92 — essentially the high of the day (high 260.14). That is a wide-bodied, close-on-high reversal candle (body 5.69, range 6.97 ≈ 1.23× ATR), which is a meaningfully different signature from the drifting, low-conviction tape that dominated September.

The larger context is a **two-month corrective range inside an intact long-term uptrend**:

- Closing peak in the visible window: **284.02 on 2026-08-03** (intraday high 287.20). Current close is **-8.49%** below that.
- Corrective low: **245.96 close on 2026-09-16** (intraday 244.30), retested as **246.15 close on 2026-09-28** (intraday 244.73).
- From that 9/16 low, AMZN is **+5.68%** in 15 sessions; from the 9/28 retest, **+5.60%** in 7 sessions.
- Over the trailing month (vs. 256.97 close on 2026-09-08) the stock is only **+1.15%** — i.e., the move is a V-shaped recovery *within* a flat monthly structure, not yet a new trend leg.

So the correct framing is: **short-term bullish reversal attempt inside a medium-term neutral/corrective range, nested inside a long-term uptrend.** That distinction drives everything below — this is a *reclaim* trade, not a breakout-to-new-highs trade.

---

### 2. Indicator Selection and Rationale

I selected eight complementary indicators, one or two per analytical function, to avoid redundancy:

| Function | Indicator | Why it fits this context |
|---|---|---|
| Long-term trend anchor | **close_200_sma** | Confirms whether the correction is a dip or a regime change; defines the line the bulls must defend |
| Medium-term trend / pivot | **close_50_sma** | Price just reclaimed it after 20 sessions below — the single most important level on the chart right now |
| Short-term momentum | **close_10_ema** | Distinguishes the fresh 3-day impulse from the September drift; also a tight trailing stop reference |
| Momentum/trend crossover | **macd** (+ macds from snapshot) | Detects the transition from corrective to impulsive; the histogram turn is the earliest confirmation here |
| Momentum strength / stretch | **rsi** | Confirms the rally is *not* overbought, i.e., there is room before exhaustion |
| Volatility envelope | **boll_ub** (+ boll / boll_lb from snapshot) | Quantifies the squeeze and whether 10/07 was a genuine band-break or a stretch |
| Risk calibration | **atr** | Volatility has compressed ~38% since August; stops and targets must be sized off *this* ATR, not August's |
| Volume confirmation | **vwma** | Tests whether the rally is volume-supported or a low-liquidity drift |

Excluded deliberately: `close_200_sma`/`close_50_sma` overlap with `boll` (20 SMA), so I use the bands as a volatility tool rather than a third average; `macds`/`macdh` are read from the verified snapshot rather than re-plotted (redundant with `macd`); no stochastics (redundant with RSI).

---

### 3. Trend Structure

**Long-term (200 SMA): unambiguously bullish.** 200 SMA = **241.848**, rising monotonically across the entire window (234.66 on 2026-07-29 → 240.73 on 2026-09-24 → 241.85 on 2026-10-07). Price sits **+7.47%** above it. Critically, the September correction *never touched* the 200 SMA — the lowest close was 245.96, still ~1.7% above the line. The long-term trend was never threatened.

**Golden-cross configuration intact.** 50 SMA (258.01) sits **16.16 points (+6.7%)** above the 200 SMA, and has for the entire visible window. No death-cross risk anywhere in the near term.

**Medium-term (50 SMA): the key event of the session.** The 50 SMA bottomed at **246.38 on 2026-07-30** and has risen every session since — reaching **258.01** on 2026-10-07. The 50 SMA flattened in late September (256.29 on 9/23 → 256.15 on 9/28 → 256.54 on 10/2) as the June lows rolled off, then turned up again over the last three sessions (256.93 → 257.43 → 258.01) — a subtle but important re-steepening.

Price crossed **below** the 50 SMA on 2026-09-09 (close 252.40 vs. SMA 254.68) and stayed below for exactly **20 consecutive sessions** through 2026-10-06 (close 256.29 vs. SMA 257.43). **2026-10-07 is the first close back above it** (259.92 vs. 258.01, +0.74%). That is a textbook trend-reclaim signal, and it is the highest close since 2026-08-28 (266.43).

**Short-term (10 EMA): flipped up decisively.** 10 EMA bottomed at **249.66 on 2026-10-01** and has turned up to **252.91**. Price is **+2.77%** above it, and the EMA has now crossed above the 50 SMA's September plateau. The 10 EMA slope (250.26 → 251.35 → 252.91 over the last three sessions) is accelerating.

**Market structure:** The September sequence made a marginally **higher low** — 244.30 (9/16 intraday) → 244.73 (9/28) — and the 10/07 high of **260.14** exceeded the 9/21 swing high of 259.49. Higher low + higher high = the first credible short-term uptrend signature since early August. It has *not*, however, exceeded the 9/04 high of **261.12**, so the reversal is not yet confirmed on a swing basis.

---

### 4. Momentum

**MACD: bullish crossover, but below zero — early-stage.** MACD line = **-0.5637**, signal = **-1.6684**, histogram = **+1.1047**.

- The **bullish crossover occurred on 2026-10-05** (MACD -1.949 crossed above signal -2.095). I use 10/05 rather than 10/02 deliberately: on 10/02 MACD (-2.195) was still fractionally *below* signal (-2.132).
- The histogram has expanded three straight sessions: **+0.146 (10/05) → +0.602 (10/06) → +1.105 (10/07)**. That is accelerating, not flattening — the healthiest part of the signal.
- But MACD remains **below zero**, which means the *trend* is still technically in the corrective phase; this is a mean-reversion leg until the zero line is reclaimed.

**RSI: 58.45 — constructive, with room.** RSI bottomed at **39.45 on 2026-09-16** and 41.24 on 2026-09-28, then rose 41.93 → 45.20 → 44.20 → 48.56 → 48.42 → 54.52 → **58.45**. The three-session surge from 48.42 to 58.45 is a genuine momentum shift (a 10-point move in three sessions). Importantly, there is **~11.5 points of headroom** before the 70 overbought threshold — this rally is not chasing an exhausted tape. There is no bearish RSI divergence in the recent data (price higher highs are matched by RSI higher highs since 9/28).

**Momentum verdict:** Confirmed short-term, unconfirmed medium-term. The setup is "early", which is exactly where the risk/reward is best but the probability of follow-through is lowest.

---

### 5. Volatility and the Squeeze

**ATR = 5.648** (2.17% of price). This is a **~38% compression** from 9.133 on 2026-08-10 and from 7.245 on 2026-09-01. ATR has fallen essentially monotonically and printed its lowest reading of the window on **2026-10-05 (5.543)** before ticking up to 5.648 on 10/07 — the first uptick, consistent with range expansion beginning.

**Bollinger (20,2): a squeeze that is now resolving upward.**
- Middle: 251.629 | Upper: 259.737 | Lower: 243.520 | Full width: **16.22 points (6.24% of price)**
- The middle band has been **falling steadily** (261.14 on 9/08 → 251.63 on 10/07) — the 20-day center of gravity drifted down 3.6% over the month, which is why 10/07 has to climb to reclaim the 50 SMA *and* the upper band simultaneously.
- The **10/07 close of 259.92 is 0.18 points (0.07%) above the upper band**. This is a marginal, not decisive, band break. Combined with the expanding ATR uptick, it reads as the *start* of a volatility expansion phase rather than a blow-off.
- Because the middle band is still declining while the upper band turns up (258.38 on 10/06 → 259.74 on 10/07), the band geometry is now opening — a classic squeeze-release pattern. The lower band at 243.52 also coincides almost exactly with the September low zone (244.30/244.73), which gives that level objective significance.

**Implication:** low-ATR squeezes resolve in either direction. The 10/07 candle argues up, but the burden of proof is on follow-through.

---

### 6. Volume and Participation

**VWMA = 251.803**, versus close 259.92 → price is **+3.22% above** the volume-weighted average. VWMA bottomed at **250.65 on 2026-10-02** and has turned up (250.83 → 251.35 → 251.80), which means the recent upside is being transacted at prices that are beginning to lift the volume-weighted mean. That is mild confirmation.

But the caveat is important: **volume is not expanding.** 10/07's 36.23M is only about **1% above** the ~35.9M average of the last 21 sessions (my hand-computed figure from the OHLCV, not a tool-reported average). For comparison: the 2026-07-31 earnings gap printed **129.05M** and 2026-08-03 printed **90.83M**. So this reclaim is happening on **ordinary, not institutional, volume**.

Interpretation: the price structure is bullish, the participation is neutral. Reclaims on average volume are more prone to retest the breakout level (the 50 SMA / upper band zone at 258–260) before continuing. A session above 45–50M on a close above 261 would materially upgrade the signal.

---

### 7. Actionable Levels

Derived only from tool output with dates:

**Resistance**
1. **259.5–261.1** — immediate supply shelf: highs of 259.50 (9/03), 261.12 (9/04), 259.49 (9/21), 260.14 (10/07). Also contains the Bollinger upper band (259.74).
2. **264.36** — 2026-08-31 high. **266.43 / 267.56** — 2026-08-28 close/high.
3. **272.27 / 274.48** — 2026-08-11 close / 2026-08-07 close; then the **284.02** (8/03) peak.

**Support**
1. **258.01** — 50 SMA; the level just reclaimed. A close back below it invalidates the reclaim.
2. **252.91** — 10 EMA; **251.63** — Bollinger middle. This 251.6–252.9 band is the first real demand shelf and the natural failure point for a false breakout.
3. **248.42** — 2026-09-15 close; **246.15 / 246.67** — 9/28 and 9/29 closes.
4. **244.30 / 243.52** — September intraday low / Bollinger lower band (confluence).
5. **241.85** — 200 SMA; a close below it would break the long-term uptrend.

---

### 8. Scenarios, Triggers, and Risk Management

**Scenario A — Continuation (base case, moderately favored):** Hold above 258 and clear **261.12** on expanding volume. Targets: 264.36 → 266.43/267.56 → 272.27. A close above 261.12 would be the first higher high since August and would confirm the short-term trend change.
- *Trigger:* daily close > 261.12 with volume > 45M.
- *Stop:* below 251.30 (Bollinger middle / below 10 EMA) — roughly **2.0× ATR** below entry, ~3.7% risk.
- At 261 entry, first target 266.43 gives ~2.1%, target 272.27 ~4.3% → modest R:R to T1, acceptable R:R to T2.

**Scenario B — Failed breakout / range rotation (high probability of at least a retest):** Rejection at 259.7–261.1 and a close back under **256.29** (10/06 close). Expect a retest of 252.9 (10 EMA) / 251.6 (Boll mid), with 248.4 as the stretch. Because volume did not confirm the break, this scenario deserves real weight — I would not add to longs above 260 without volume.
- *Invalidation of the bullish reclaim:* a daily close below **258.01** (50 SMA) turns the 10/07 candle into a one-day false break.

**Scenario C — Structural break (lower probability given 200 SMA support):** Close below **246.15** breaks the 9/16→9/28 higher-low structure and opens 244.30 and then the 200 SMA at 241.85. This is the "the correction is not over" scenario and would flip the medium-term bias to neutral/negative.

**Risk calibration (per verified ATR of 5.648 = 2.17% of price):**
- With ATR down 38% from August, *absolute* stops must be tightened; using August-era stops (9+ points) would now be ~1.6× wider than the market's actual noise.
- A 2×ATR stop from 259.92 = **248.6**; a 1.5×ATR stop = **251.4**. The 251.3–251.6 zone (10 EMA/Boll mid/1.5 ATR) is the tightest defensible stop.
- For 1% account risk with a 251.3 stop on a 260 entry (3.34% risk per share), position size ≈ 30% of account notional. With the wider 248.6 stop (4.35%), size ≈ 23%.

**What would change my mind, in order of importance:**
1. A close below 258.01 (50 SMA) — kills the reclaim.
2. MACD histogram rolling back toward zero / MACD failing to reach the zero line — the 10/05 crossover was below zero and is inherently lower-quality.
3. Continued refusal above 261.12 while RSI stalls in the high 50s — would flag distribution into strength.
4. A rally on declining volume — confirms the "average participation" concern.

**Cross-checks / discrepancies:** The verified 2026-10-07 snapshot matches the OHLCV tool's final row exactly (O 254.23 / H 260.14 / L 253.17 / C 259.92 / V 36.23M), and all indicator values from `get_indicators` reconcile with the snapshot (50 SMA 258.0088, 200 SMA 241.848, 10 EMA 252.9104, MACD -0.5637, RSI 58.4544, Boll upper 259.7366, ATR 5.6485, VWMA 251.8030). **No conflicts found.** One note: the snapshot's `mfi` field returns 0.655, which appears to be a 0–1 normalized value rather than the conventional 0–100 scale; I have not used it in this analysis.

---

### 9. Summary Table

| Dimension | Reading (2026-10-07) | Interpretation | Signal |
|---|---|---|---|
| Close | 259.92 (+1.42% d/d) | Close on session high; highest close since 8/28 | Bullish |
| 200 SMA | 241.848, rising | Price +7.47% above; Sept low never tested it | Bullish (long-term) |
| 50 SMA | 258.009, rising | Reclaimed after 20 sessions below (first close above since 9/08) | Bullish (medium-term) |
| 10 EMA | 252.910, turning up | Price +2.77% above; slope accelerating 3 sessions | Bullish (short-term) |
| Golden cross | 50 SMA − 200 SMA = +16.16 | Intact all window; no death-cross risk | Bullish |
| MACD / Signal / Hist | -0.5637 / -1.6684 / +1.1047 | Bullish cross 10/05; hist expanding 3 sessions; still sub-zero | Early bullish |
| RSI | 58.45 (from 39.45 on 9/16) | Rising, ~11.5 pts of headroom to 70; no divergence | Supportive |
| Bollinger | Mid 251.63 / UB 259.74 / LB 243.52 | Close 0.07% above UB; width 6.24%; squeeze releasing upward | Breakout attempt |
| ATR | 5.648 (2.17%); -38% since 8/10 | Volatility compression; first uptick 10/07 | Coiled |
| VWMA | 251.803, turning up | Price +3.22% above; trend mildly volume-confirmed | Neutral-positive |
| Volume | 36.23M vs ~35.9M 21-day avg | No expansion; rally lacks institutional confirmation | Caution |
| Structure | Low 244.30 (9/16) → 244.73 (9/28); high 260.14 (10/07) | Higher low + higher high; but 261.12 still caps | Improving |
| Immediate resistance | 259.5–261.1, then 264.36, 266.43/267.56, 272.27 | Multi-touch supply shelf overhead | Pivot zone |
| Immediate support | 258.01, then 251.6–252.9, 248.4, 246.2, 244.3/243.5, 241.85 | Layered demand | Long bias while >258 |
| Bull trigger | Close >261.12 on volume >45M | Confirms higher high and trend change | Entry |
| Bear trigger | Close <258.01 (reclaim fails) / <246.15 (structure breaks) | Range rotation / deeper correction | Exit / stand aside |
| Stop reference | 251.3 (1.5×ATR) or 248.6 (2×ATR) | Sized to current, not August, volatility | Risk ~3.3–4.4% |
| Net bias | Short-term bullish / medium-term neutral / long-term bullish | Reclaim trade, not a breakout trade | **Constructive, unconfirmed** |