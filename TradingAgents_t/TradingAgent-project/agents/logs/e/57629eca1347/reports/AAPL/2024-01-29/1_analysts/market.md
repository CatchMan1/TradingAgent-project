# AAPL — Technical Analysis Report (as of close 2024-01-29)

## 0. Indicator selection & why

The tape as of 2024-01-29 is a **post-earnings-cycle-style pullback inside an intact medium/long-term uptrend** — price is compressing between a rising 50-day SMA and a flattening short-term EMA after a failed push toward the December highs. For that regime I selected eight non-redundant tools:

| Chosen | Role in this context |
|---|---|
| close_50_sma | The live trend line price is currently testing (~191) |
| close_200_sma | Long-term regime filter / golden-cross benchmark |
| close_10_ema | Short-term momentum proxy for the current 4-day fade |
| macd + macds | Trend-change confirmation (recent bullish crossover to validate) |
| rsi | Overbought/oversold & momentum divergence check on the Jan bounce |
| atr | Position sizing / stop placement in a 1.6%/day volatility regime |
| vwma | Volume-weighted "true" cost basis to test whether the bounce has real participation |

Deliberately omitted: Bollinger bands (a 20-SMA envelope would duplicate the 50-SMA/ATR level-and-volatility work; the snapshot's band values are used only as a cross-check), StochRSI (redundant with RSI), and MACD histogram (redundant with macd/macds crossovers).

---

## 1. Verified price state (source of truth: verified snapshot)

- **2024-01-29 OHLCV:** open 192.01, high 192.20, low 189.58, **close 191.73**, volume 47.15M. The session closed in the lower third of its range, i.e. sellers controlled the close.
- Prior four sessions are a textbook **descending sequence of lower highs and lower lows**: highs 196.38 (01-24) → 196.27 (01-25) → 194.76 (01-26) → 192.20 (01-29); lows 194.34 → 193.11 → 191.94 → 189.58.
- Context: closing peak **198.11 on 2023-12-14** (intraday high 199.62 that day) → drawdown low close **181.18 on 2024-01-05** (low 180.17) → rebound close **195.18 on 2024-01-23** → now 191.73.
  - Close-to-close drawdown from the 12-14 peak: **−3.22%**; from the 12-14 intraday high: **−3.95%**.
  - Rebound 01-05 → 01-23 close-to-close: **+7.73%**; pullback since 01-23: **−1.77%**.
- Volume on the decline is *not* expanding: 47.15M on 01-29 versus roughly **56.6M average across the 19 sessions from 2024-01-02 to 2024-01-29** (~17% lighter). Distribution-style volume was concentrated earlier (82.5M on 01-02, 78.0M on 01-18), not in the last three sessions.

## 2. Trend structure: bullish on both timeframes, but stalling short-term

- **50-SMA = 190.92; 200-SMA = 182.08.** Close 191.73 sits **+0.42% above the 50-SMA** and **+5.30% above the 200-SMA**. The 50-SMA is above the 200-SMA by **+4.86%** and both are rising (50-SMA 186.84 on 01-02 → 190.92 on 01-29; 200-SMA 179.64 → 182.08). The 50>200 configuration has held throughout the entire Oct 2023–Jan 2024 window in the tool output, so the long-term uptrend is confirmed — not newly formed.
- **10-EMA = 191.41.** Close is only **+0.17%** above it. The 10-EMA flattened hard (191.09 on 01-25 → 191.33 → 191.41), i.e. the short-term impulse has decayed to neutral.
- Interpretation: the medium-term structure is a **rising-support uptrend with price coiled directly on top of it**. This is a decision point, not a trend break — but the burden of proof is now on buyers.

## 3. Momentum: bullish crossover still intact, but the thrust is fading

- **MACD 0.944 vs signal 0.180** → MACD crossed back above its signal around **2024-01-23** (MACD 0.184 vs signal −0.815) and has stayed above it. That is a valid momentum-recovery signal off the January low.
- However the MACD line **stalled**: 0.877 (01-25) → 0.951 (01-26) → 0.944 (01-29), and the implied histogram (0.962 → 0.764, snapshot `macdh` = 0.7636) is **contracting**. The crossover is holding; the acceleration is not.
- **RSI 53.93**, down from 62.62 on 01-23 and 56.96 on 01-19 — neutral, no overbought constraint, no oversold cushion. For reference, RSI bottomed at **28.79 on 2024-01-05** (a genuine oversold print) and reset to 36.7 on 01-17 before the rally. Current 54 means the January oversold fuel has been spent; RSI has room to fall to ~40 without breaking anything structural, but it is no longer a tailwind.
- Net read: **momentum = constructive but decelerating**. A MACD/signal bearish cross (needs ~3–5 more down sessions, or one sharp −2% day) would be the first corroboration of a deeper pullback.

## 4. Volatility, bands and the volume-weighted cost basis

- **ATR = 3.13**, i.e. **1.63% of the 191.73 close**. ATR has been stable at 3.1–3.4 since 01-18 (peaked 3.37 on 01-22) after rising from 2.57 on 12-29 — volatility is elevated relative to late December but no longer expanding.
- Snapshot Bollinger reference: **mid 188.11, upper 197.42, lower 178.81**. Close is **+1.92% above the mid-band**, **−2.97% below the upper band** and **+7.23% above the lower band**. Bandwidth ≈ 9.9% of the mid — wide, consistent with a trend that is still "on" rather than a squeeze.
- **VWMA = 189.13**, below the close by **+1.38%**. Price holding above the volume-weighted average means the average recent buyer is still in profit — a mildly supportive, non-distributionary condition. Note the gap is narrowing: VWMA has climbed every session since 185.25 on 01-18, so the cushion is being consumed. **A close below ~189.1 (VWMA) would mean the marginal January buyer is underwater** — an important sentiment line.

## 5. Levels that matter (all derived from tool output)

**Resistance**
1. **193.9–195.2** — 01-22/01-23 closes (the failed rally shelf).
2. **196.3–196.4** — 01-24/01-25 highs; reclaiming this invalidates the lower-highs sequence.
3. **197.42** — Bollinger upper band (snapshot).
4. **198.11 / 199.62** — 12-14 close / intraday high; the range top.

**Support**
1. **191.41 / 190.92** — 10-EMA / 50-SMA (immediate, being tested now).
2. **189.58** — 01-29 session low.
3. **189.13** — VWMA ("pain threshold" for January buyers).
4. **188.11** — Bollinger mid / 20-SMA; losing it flips the short-term structure negative.
5. **185.6–186.1** — 01-08/01-10 closes and the 01-18 breakout gap zone.
6. **182.08** — 200-SMA, coinciding with the 01-05/01-17 area (181.2–182.7). This is the line that would put the *primary* uptrend in question.

## 6. Actionable playbook

**Base case (highest probability given the evidence):** consolidation between **189.5 and 195.2**, with 191–191.4 as the pivot. Momentum is positive but decaying, volume is light, and RSI is neutral — this is a "wait for confirmation" tape, not a chase.

- **Long / add-on-confirmation:** wait for a *close above 193.9* on volume ≥ ~56M (the 19-session average) to re-arm the trend toward 196.4 → 197.4. A close below 190.9 first, then a reclaim, is the lower-quality version of the same trade.
- **Trend-following hold:** longs can be held while close > 50-SMA (190.92) and MACD > signal. Two consecutive closes below both 190.9 and 189.1 (VWMA) is a legitimate scale-out trigger — that combination says the short-term trend and the volume-weighted cost basis have both failed.
- **Short / tactical fade (counter-trend, higher risk):** only valid on a **close below 188.11 (Bollinger mid)** with expanding volume; first target 185.6–186.1, second 182.1 (200-SMA). The 50>200 configuration means any short is a swing trade, not an investment thesis.
- **Stop placement / sizing with ATR = 3.13:** structural stop for a long entered near 191–192 is **~2×ATR ≈ 6.3 points**, i.e. below 185.5–186 (which conveniently overlaps the 185.6 gap zone). A tighter 1×ATR (≈3.1 pts, ~188.6) sits inside normal daily noise and will likely be clipped. Size positions so a 2-ATR adverse move costs ≤1% of capital.
- **Risk asymmetry note:** upside to the 12-14 high (198.11) is ~+3.3%; downside to the 200-SMA (182.08) is ~−5.0%. With ATR at 1.6%/day, price can traverse either in 2–3 sessions — hence the emphasis on *closing* confirmation rather than intraday breaks.

## 7. What would change the view

- **Bullish flip:** close > 196.4 with RSI > 60 and MACD histogram expanding again → new leg toward 197.4–199.6.
- **Bearish flip:** close < 188.1 with volume > ~56M, MACD crossing below signal, RSI < 45 → 185.6 then 182.1 in play.
- **Neutral continuation:** continued drift in the 189.5–195.2 band on sub-average volume; in that case do nothing until the range resolves.

*Data-integrity note: the verified snapshot's 50-SMA (190.9246), 200-SMA (182.0785), 10-EMA (191.4059), MACD (0.9436), signal (0.1800), RSI (53.9297), ATR (3.1296) and VWMA (189.1251) match the indicator-tool outputs exactly — no discrepancy to flag. The snapshot additionally reports Bollinger values (188.115 / 197.423 / 178.807) and MFI 0.5865, which are used here only as cross-checks.*

---

## Key points summary

| Dimension | Reading (2024-01-29) | Signal |
|---|---|---|
| Price | Close 191.73 (O 192.01 / H 192.20 / L 189.58) | Closed in lower third of range |
| 50-SMA | 190.92 (rising; 186.84 on 01-02) | Close +0.42% above → trend intact, being tested |
| 200-SMA | 182.08 (rising; 179.64 on 01-02) | Close +5.30% above → primary uptrend intact |
| 50 vs 200 | +4.86% spread, both rising | Golden-cross regime in force all window |
| 10-EMA | 191.41 (flattened) | Short-term momentum neutral; price +0.17% above |
| MACD / Signal | 0.944 / 0.180 | Bullish cross since ~01-23, but MACD stalling |
| MACD Histogram | 0.764 (from ~0.962 on 01-26) | Thrust contracting — caution |
| RSI | 53.93 (from 62.62 on 01-23) | Neutral; no longer oversold, no overbought cap |
| ATR | 3.13 (1.63% of price) | Use ~3-pt (1×) noise band, ~6.3-pt (2×) stop |
| VWMA | 189.13 (rising from 185.25 on 01-18) | Price above it, but cushion narrowing |
| Bollinger (snapshot) | mid 188.11 / UB 197.42 / LB 178.81 | Price +1.9% over mid, −3.0% under UB |
| Volume | 47.15M vs ~56.6M 19-session avg | Declining volume on the fade = mildly constructive |
| Structure | 4 straight lower highs/lows (196.38→192.20) | Short-term downtrend within uptrend |
| Key resistance | 193.9–195.2 / 196.4 / 197.4 / 198.1–199.6 | Confirmation needed above 193.9 |
| Key support | 190.9 / 189.6 / 189.1 / 188.1 / 185.6–186.1 / 182.1 | 188.1 is the structural line |
| Bias | **Bullish primary trend, neutral-to-fading short-term** | Hold/scale, don't chase; confirm at 193.9 or 188.1 |