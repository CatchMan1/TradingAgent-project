# AAPL — Multi-Factor Technical Report (as of close 2024-01-23)

**Data integrity note:** The `get_verified_market_snapshot` output and the `get_indicators` series agree exactly on every overlapping value (50-SMA 190.2892, 200-SMA 181.4524, 10-EMA 189.4995, MACD 0.1837, ATR 3.2663, VWMA 186.0448, Bollinger upper 197.4577 / lower 178.8283, RSI 62.6196). No reconciliation was required. One caution: the snapshot's `mfi` field prints 0.560288, which is off the standard 0–100 scale, so **MFI is excluded** from this analysis rather than misread.

---

## 1. Verified price structure

| Item | Value |
|---|---|
| 2024-01-23 OHLCV | O 195.02 / H 195.75 / L 193.83 / **C 195.18** / Vol 42.36M |
| 50-SMA | 190.29 |
| 200-SMA | 181.45 |
| 10-EMA | 189.50 |
| VWMA (volume-weighted) | 186.04 |
| Bollinger (20-SMA / UB / LB) | 188.14 / 197.46 / 178.83 |
| RSI(14) | 62.62 |
| MACD / Signal / Histogram | +0.184 / −0.815 / **+0.998** |
| ATR(14) | 3.27 (1.67% of price) |

AAPL closed 2024-01-23 at 195.18, the highest close in the visible dataset since 2023-12-15 (197.57) and only −1.48% from the 2023-12-14 record close of 198.11.

## 2. Trend: bullish primary, freshly re-accelerated

This is a textbook bullish stack on the verified numbers:

- **Close 195.18 > 50-SMA 190.29 (+2.58%) > 200-SMA 181.45 (+7.57%).**
- The 50-SMA has sat above the 200-SMA for the entire visible 2023-09-25 → 2024-01-23 window (e.g., 183.10 vs 168.42 on 09-25), and the spread is now **widening** again: 8.84 points (4.87% of the 200-SMA), up from 7.51 points on 2023-10-27. Widening 50/200 separation = trend re-strengthening, not maturing.
- The 200-SMA itself is still climbing monotonically (168.42 on 09-25 → 181.45 on 01-23), so the long-term benchmark offers no downside pressure.

**The important nuance is the *recency* of the recovery.** From 2024-01-02 through 2024-01-17, price traded *below* the 50-SMA (e.g., 2024-01-17 close 182.68 vs 50-SMA 189.32). The reclaim happened on **2024-01-19** (close 191.56 vs 50-SMA 189.80), and has been held for three sessions. That is a genuine regime flip, but a very young one — three closes of confirmation, not twenty.

**Short-term persistence:** the 10-EMA (189.50) is rising sharply — 185.37 on 01-17 → 189.50 on 01-23 — and price is 3.00% above it. Notably, **the 10-EMA (189.50) still sits BELOW the 50-SMA (190.29)**. That is a lingering artifact of the January drawdown. A 10-EMA/50-SMA upcross would be the cleanest confirmation that the short-term trend has structurally repaired; it has not happened yet.

## 3. Momentum: powerful but entering the "watch zone"

**MACD is the single most constructive signal on the board.**
- Histogram: −0.718 (01-17) → −0.283 (01-18) → **+0.203 (01-19)** → +0.656 (01-22) → **+0.998 (01-23)**. A bullish MACD/signal crossover occurred 2024-01-19, and the histogram has now expanded for four consecutive sessions — acceleration, not just a crossover.
- The MACD *line* turned positive on 01-23 (+0.184), its first positive print since 2024-01-03 (+0.055). That is a **zero-line cross**, which in a rising 50/200 regime is the higher-quality version of the signal.
- Context for how washed-out the prior reading was: MACD bottomed at −1.926 on 2024-01-17. The current print is a +2.11-point swing in four sessions.

**RSI at 62.62** — recovered from 28.79 on 2024-01-05 (an oversold print) and 36.71 on 2024-01-17. It is *not* overbought (< 70), so there is still headroom. **However, flag the relative-strength caveat:** on 2023-12-08 AAPL closed 195.71 with RSI 70.02; today it closes 195.18 — essentially the same price — with RSI 62.62. Same price, 7.4 RSI points weaker. Momentum is carrying the price rather than *leading* it, which is a mild negative divergence at a like-for-like level. Similarly, the 12-14 record close of 198.11 printed RSI 69.69 vs today's 62.62.

## 4. Volatility: expanding, and the bands frame the target

- **ATR 3.27**, up from 2.57 on 2023-12-28 and a December trough near 2.57–2.63. Rising ATR alongside rising price = expansion phase. Stops must be wider than the December regime allowed.
- **Bollinger:** upper 197.46, middle 188.14, lower 178.83. Close 195.18 sits at **87.8% of band height (%B ≈ 0.88)** — pressed toward the upper band but 1.15% shy of it.
- Bandwidth = (197.46 − 178.83) / 188.14 = **9.90%**, marginally narrower than the 11.2% on 2024-01-08 (202.95 upper / 181.45 lower). Bands are not in a hard squeeze, but the upper band has *fallen* from 202.95 (01-08) to 197.46 (01-23) — the volatility ceiling is descending toward price. Breakout above 197.46 would be a genuine bandwidth expansion event.

## 5. Volume: the one soft spot

This is where I would push back on the bullish tape:

- **2024-01-23 volume 42.36M is roughly 79% of the trailing-20-session average (~53M)** computed from the verified rows.
- The rally's four up-days show **monotonically decaying volume**: 01-18 → 78.0M (+3.26% to 188.63); 01-19 → 68.9M (+1.55%); 01-22 → 60.1M (+1.22%); 01-23 → 42.4M (+0.67%). Price advanced every day; participation fell every day. That is textbook fading sponsorship on the final push into resistance.
- **VWMA at 186.04 vs close 195.18 = price 4.91% above the volume-weighted cost basis.** VWMA has only just inflected up (185.25 on 01-18 → 185.36 → 185.59 → 186.04) after declining from 195.53 on 2023-12-26. Interpretation: the entire December distribution (heavy volume at 194–196) is now *above* the volume-weighted average, meaning the marginal recent buyer is in profit — supportive — but the 4.9% gap is stretched and mean-reversion toward VWMA is historically the more common resolution.

## 6. Support / resistance derived from verified rows

**Resistance**
1. **195.75** — 2024-01-23 intraday high (immediate).
2. **197.46** — Bollinger upper band.
3. **197.96 / 198.11** — 2023-12-13 close 197.96 and 2023-12-14 record close 198.11.
4. **199.62** — 2023-12-14 intraday high (the ceiling of the visible dataset).

**Support**
1. **193.83** — 2024-01-23 low; **192.26** — 2024-01-22 low (the 192.3–193.8 shelf).
2. **191.95** — 2024-01-19 high, now potential support; together with 1 forms a 191.9–193.8 first-line zone.
3. **190.29** — 50-SMA, ≈1.5 × ATR (4.90) below the close. High-confluence.
4. **188.63–188.82** — 2024-01-18 close / 2024-01-19 low; also the 20-SMA (188.14) sits just beneath.
5. **186.09–186.74** — 2024-01-18 opening gap (unfilled) and 2024-01-12 high; VWMA 186.04 sits here too.
6. **180.17–180.93** — a four-touch base: 2024-01-04 low 180.88, 01-05 low 180.17, 01-16 low 180.93, 01-17 low 180.30. This is the line in the sand.

Two gap observations worth noting, both tool-supported:
- The **2024-01-02 gap-down** (2023-12-29 close 192.53 → 01-02 open 187.15) has been **fully repaired** — close 193.89 on 01-22 and 195.18 on 01-23 are both above the gap origin. Gap-fill-and-hold is bullish.
- The **2024-01-18 gap-up** (01-17 close 182.68 → 01-18 open 186.09) remains unfilled and is the natural downside magnet if momentum stalls.

## 7. Actionable scenarios

**A. Trend-continuation (base case, given expanding MACD histogram + zero-line cross).**
Hold/own the position. Trail risk under the 10-EMA (189.50) for tactical longs, or under **188.6** (below the 01-18/01-19 lows and the 20-SMA) for swing longs — that is a 3.4% / 1.04-ATR stop from 195.18. A daily close above **197.46–198.11** with volume ≥ ~53M (20-day average) validates a breakout and opens 199.62. *Do not* treat a low-volume poke above 197.5 as confirmation; that would be a repeat of today's decay pattern.

**B. Pullback-buy (better risk/reward than chasing).**
The 190.3–191.9 zone (50-SMA + 01-19 high) is the highest-quality entry: it is 2.0–2.6% below spot and coincides with the 1.5-ATR band (190.28). Stop below 188.6 caps risk at ~1.5%. Note this is a *level-based* setup, not an observed bounce — the tool data does not show prior tests of 190.3 as support, so treat it as a planned zone, not a proven floor.

**C. Caution tape (needs monitoring, not action yet).**
Three things would flip me neutral: (i) a close back below **190.29** (50-SMA) — invalidates the 01-19 reclaim; (ii) RSI rolling over from the 62–65 area while price prints a lower high beneath 198.11 — confirms the weakening-RSI divergence; (iii) volume staying below ~45M on further advances. A close below **186.0–186.7** (gap + VWMA confluence) breaks the trend structure outright.

**Risk sizing.** With ATR 3.27 (1.67%), a 1% account-risk position at the 188.6 stop (6.58/share risk) supports roughly half the share count of a December-sizing basis (ATR then ~2.57–2.63). Rising volatility mechanically demands smaller size — this is not optional.

**Unverified event risk.** The dataset provided contains no earnings calendar, so I cannot date it from tool output. AAPL's fiscal-Q1 report historically lands in the late-January/early-February window; if that applies here, a binary gap event sits directly in front of this setup. Flagging it as a calendar risk, not asserting a date or an estimate.

---

## Summary table

| Dimension | Indicator | Latest value (2024-01-23) | Signal | Evidence |
|---|---|---|---|---|
| Long-term trend | close_200_sma | 181.45 | **Bullish** | Rising every session in window (168.42 on 09-25); price +7.57% above |
| Medium-term trend | close_50_sma | 190.29 | **Bullish** | Price +2.58% above; 50>200 by 4.87% and widening; reclaimed only 01-19 |
| Short-term trend | close_10_ema | 189.50 | **Bullish but young** | 185.37 (01-17) → 189.50; still *below* 50-SMA — upcross pending |
| Momentum | macd | +0.184 | **Bullish** | First positive print since 01-03; +2.11 swing off −1.926 low (01-17) |
| Momentum strength | macdh | +0.998 | **Strongly bullish** | 4 straight expansions; crossed positive 01-19 |
| Momentum/overbought | rsi | 62.62 | **Constructive, not extended** | Up from 28.79 (01-05); but same price as 12-08 with 7.4 fewer RSI points |
| Volatility | atr | 3.27 (1.67%) | **Expanding** | Up from 2.57 (12-28); 1.5-ATR = 190.28 ≈ 50-SMA; size down |
| Volatility band | boll_ub / boll_lb | 197.46 / 178.83 | **Upper-band approach** | %B ≈ 0.88; bandwidth 9.90%, upper band fell from 202.95 since 01-08 |
| Volume confirmation | vwma | 186.04 | **Lagging** | Price +4.91% above; volume decayed 78.0M→42.4M across the 4-day rally |
| Structural support | Jan base | 180.17–180.93 | **Solid** | Four touches (01-04, 01-05, 01-16, 01-17) before breakout |
| **Net assessment** | — | — | **Bullish trend / stretched entry** | Own it, don't chase it: add at 190.3–191.9, invalidate below 190.29, breakout needs >53M volume |