# AAPL (Apple Inc.) — Technical Analysis Report
**Analysis date (simulated "now"): 2026-07-10 | Last close: $315.32 (2026-07-10)**

> Data provenance: prices and indicator values below are drawn from the point-in-time OHLCV series and cross-checked against the **Verified Market Snapshot for AAPL as of 2026-07-10**, which I treat as the source of truth for exact OHLCV / price / indicator levels. Where I cite a value it matches that snapshot. This is a simulated as-of date; treat it as the operating "now."

---

## 1. Executive Summary

AAPL is in a **well-established, multi-timeframe uptrend that is reasserting itself after a sharp late-June shakeout.** Price sits at $315.32, essentially retesting the June swing high, having fully repaired a ~13% June drawdown with a powerful V-shaped recovery. The trend structure (price > 10 EMA > 50 SMA > 200 SMA) is textbook bullish, MACD has just delivered a fresh bullish crossover with an expanding histogram, and RSI has reset from overbought back to a healthy ~63. The main caveat is **elevated volatility (ATR ~8.1, ~2.6% of price) and proximity to the upper Bollinger band**, meaning upside momentum is strong but the stock is "stretched" and prone to sharp two-way swings.

---

## 2. Price Action & Trend Context

**The June shakeout and V-recovery (supported by daily data):**
- Price peaked at a **close of $315.20 on 2026-06-02** (intraday high $317.40 on 2026-06-08), then rolled over.
- A two-stage selloff bottomed at a **close of $275.15 on 2026-06-25** (intraday low $273.75) on heavy **107.0M volume**. The next session, **2026-06-26, printed $283.78 on 261.8M volume** — an extreme-volume reversal/absorption day that marked the turning point.
- From that $275.15 low, price recovered to **$315.32 by 2026-07-10 — a +14.6% rebound in roughly two weeks.** A standout thrust was **2026-07-02 (+4.8%, $294.38 → $308.63) on 75.4M volume**, a high-conviction breakout day.
- The pullback low (~$275) held **above the long-term 200-day benchmark (now $272.45)**, i.e., the strategic uptrend was never broken — only the medium-term trend was tested.

**Structural trend read (moving-average architecture):**
- **Price $315.32 > 10 EMA $306.57 > 50 SMA $297.77 > 200 SMA $272.45.** Perfect bullish stacking.
- The **50 SMA ($297.77) sits ~9.3% above the 200 SMA ($272.45)** — a healthy, widening golden-cross spread confirming a durable long-term uptrend.
- Price is **+5.9% above the 50 SMA** and **+15.7% above the 200 SMA**, showing extension but not extreme.
- Notable: during the late-June dip, price briefly **closed below the 50 SMA** (e.g., $275.15 close vs. ~$291 SMA on 2026-06-25) before **reclaiming it on 2026-07-01** ($294.38 close vs. $292.67 50 SMA). That reclaim is a classic "breakdown-then-reclaim" bullish continuation signal.

---

## 3. Momentum Analysis

**MACD (bullish, fresh and accelerating):**
- MACD line **$4.61**, signal **$1.89**, histogram **+$2.72** (all per snapshot).
- The **MACD line crossed above its signal line on 2026-07-02** (macd −0.69 vs. signal −0.95) and then **crossed above zero on 2026-07-06** (macd +0.88). Two consecutive bullish triggers.
- The **histogram flipped positive on 2026-07-02 and has expanded for six straight sessions** (0.26 → 2.72), indicating *accelerating* upside momentum, not just a bounce.

**RSI (reset, with room to run):**
- RSI **62.93** as of 2026-07-10.
- It was **overbought at 73.58 on 2026-06-02**, fell to a near-oversold **32.20 on 2026-06-25** during the selloff, and has climbed back to ~63. This is a **constructive reset** — momentum is strong but RSI is *below* the 70 overbought threshold, leaving headroom before momentum becomes stretched.

---

## 4. Volatility Analysis

- **ATR (14): $8.09**, i.e., ~**2.57% of the $315.32 close**. ATR expanded from ~$5.7–6.0 in early June to a peak of ~$8.7 on 2026-07-02 and remains elevated — the June event structurally raised the stock's volatility regime. Position sizing and stop distances should reflect this (e.g., a 2×ATR stop ≈ $16/point).
- **Bollinger (20, 2σ):** middle **$298.10**, upper **$321.20**, lower **$275.01**. Price at $315.32 sits in the **upper ~87% of the band (%B ≈ 0.87)**, ~$5.9 (~1.9%) below the upper band. Bandwidth ≈ **15.5% of the mid-band** — wide, consistent with the elevated-volatility read. Riding the upper band is a sign of strength, but leaves limited cushion before a mean-reversion snap.

---

## 5. Volume Confirmation

- **VWMA $293.13** vs. price $315.32 → price is **+7.6% above the volume-weighted average**, confirming the advance is supported by volume-weighted participation rather than a thin drift.
- The **261.8M-volume session on 2026-06-26** and the **75.4M-volume breakout on 2026-07-02** are the two highest-conviction footprint days of the recovery — both bullish (capitulation/reversal, then continuation thrust).

---

## 6. Selected Indicators (8) — Rationale

I chose a complementary, non-redundant set spanning trend, momentum, volatility, and volume:

1. **close_10_ema** — captures short-term momentum and the current entry posture; price is riding above a sharply rising 10 EMA ($306.57), signaling the immediate trend is up and giving a tactical trailing reference.
2. **close_50_sma** — the medium-term trend/dynamic-support backbone; the recent dip-and-reclaim of the 50 SMA is the key tactical pivot.
3. **close_200_sma** — strategic trend confirmation; its rising slope and the 50>200 golden-cross spread validate that the long-term uptrend is intact despite the June scare.
4. **macd** — momentum/trend-change engine; the fresh zero-line and signal crossovers and expanding histogram mark the recovery as accelerating.
5. **macds** — the signal line, needed to interpret the MACD crossover and confirm (not just guess) the bullish trigger date.
6. **rsi** — overbought/oversold gauge; shows a healthy reset from 73.6 → 32.2 → 62.9, i.e., momentum reloaded without being stretched.
7. **atr** — volatility/risk-sizing; essential given the elevated, event-driven volatility for setting stops and position size.
8. **vwma** — volume-weighted trend confirmation; ensures the price strength is volume-backed (price +7.6% vs. VWMA).

*Supplementary context (from the verified snapshot, not counted in the 8): Bollinger middle/upper/lower ($298.10 / $321.20 / $275.01) — used above to gauge overbought/stretch.*

Rationale for the set: two trend anchors (50/200 SMA) + one fast trend/momentum average (10 EMA) + a momentum pair (MACD/signal) + an overbought/oversold oscillator (RSI) + a volatility/risk tool (ATR) + a volume confirmation (VWMA) covers every category without duplicating signal type (e.g., no second oscillator paired with RSI).

---

## 7. Actionable Insights

- **Bias: constructive/bullish**, but with tactical caution given stretch. The primary trend favors buyers; the tactical setup favors buying pullbacks rather than chasing a band-tag.
- **Key upside trigger:** A **daily close above the $317.40 high (2026-06-08)** with above-average volume would confirm a breakout to new highs, opening continuation toward the upper Bollinger band ($321.20) and beyond. Watch MACD histogram for continued expansion to validate.
- **Key support levels (data-anchored):**
  - **10 EMA ~$306.57** — first dynamic support / short-term trend filter.
  - **50 SMA ~$297.77** (also near the Bollinger mid $298.10) — the critical medium-term line in the sand; a close back below it would neutralize the bullish structure.
  - **June low close $275.15 / low $273.75** near the **lower Bollinger band $275.01** and the **200 SMA $272.45** — the strategic floor; losing this would flip the longer-term trend.
- **Risk management:** ATR ~$8.09 argues for wider stops. A common approach: initial stop ~1.5–2×ATR (≈$12–16) below entry, or a volatility-aware position size scaled down vs. the calmer May regime. RSI at 62.9 gives room, but a push toward 70+ near the upper band would warrant trimming/trailing rather than fresh adds.
- **What would weaken the thesis:** MACD histogram rolling over while price stalls below $317.40 (bearish divergence risk); a decisive close under the 50 SMA (~$298); or a volume-less drift higher that leaves price extended above the 10 EMA.

---

## 8. Key Points Summary Table

| Dimension | Indicator | Value (2026-07-10) | Signal | Interpretation |
|---|---|---|---|---|
| Short-term trend | close_10_ema | $306.57 | Bullish | Price ($315.32) riding well above rising 10 EMA |
| Medium-term trend | close_50_sma | $297.77 | Bullish | Price +5.9% above; dip below then reclaimed 2026-07-01 |
| Long-term trend | close_200_sma | $272.45 | Bullish | Price +15.7% above; 50>200 golden-cross spread ~9.3% |
| Momentum (line) | macd | $4.61 | Bullish | Crossed above zero 2026-07-06; rising |
| Momentum (signal) | macds | $1.89 | Bullish | MACD>signal since 2026-07-02 crossover |
| Momentum (hist.) | macdh | +$2.72 | Accelerating | Six sessions of expanding positive bars |
| Overbought/oversold | rsi | 62.93 | Neutral-bullish | Reset from 73.6→32.2→62.9; room before 70 |
| Volatility/risk | atr | $8.09 (2.57%) | Elevated | Wide stops/position sizing warranted |
| Volume trend | vwma | $293.13 | Bullish | Price +7.6% above volume-weighted avg |
| Bollinger context* | boll / ub / lb | $298.10 / $321.20 / $275.01 | Stretched-up | %B≈0.87; ~1.9% below upper band; bandwidth ~15.5% |

*\*Bollinger shown as supplementary snapshot context, not part of the formal 8-indicator set.*

**Bottom line:** AAPL exhibits a high-quality, multi-timeframe bullish alignment. The June drawdown was repaired with volume-backed conviction, momentum has freshly turned up (MACD crossover + expanding histogram, RSI reset), and the long-term trend is intact. The trade is constructive, but the stock is extended near the upper band with elevated ATR — favoring **buy-the-dip entries near the 10 EMA/$306–$298 zone with disciplined, ATR-based stops**, and a breakout confirmation above **$317.40** to add. Invalidation: sustained close below the 50 SMA (~$298).