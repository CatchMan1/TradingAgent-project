# AAPL — Multi-Indicator Technical Analysis (as of 2026-07-20)

## 1. Selected indicators and why (8 total)

| # | Indicator | Role in this setup |
|---|---|---|
| 1 | `close_50_sma` | Medium-term trend + dynamic support for a stock that has rallied ~32% off its late-March base |
| 2 | `close_200_sma` | Long-term regime filter; confirms the bull structure is intact, not a counter-trend bounce |
| 3 | `close_10_ema` | The line that carried the July vertical advance — the first place a healthy pullback should be contained |
| 4 | `macd` | Captures the mid-June momentum collapse and the July re-acceleration |
| 5 | `macds` | Crossover timing (bearish cross in early June, bullish recross on 2 July) — used as a confirmation filter, not a standalone signal |
| 6 | `rsi` | Measures whether the July push became overbought and whether the 20 July fade broke momentum |
| 7 | `atr` | Volatility has expanded materially since May; essential for stop placement and position sizing |
| 8 | `vwma` | Volume-weighted confirmation of the rebound and a gauge of where the average recent buyer's cost basis sits |

Deliberately **excluded**: `boll`/`boll_ub`/`boll_lb` (largely redundant with the 20-SMA + ATR information already captured, though I reference snapshot values below), `macdh` (derivable from `macd` − `macds`), and `mfi` (a second overbought oscillator alongside RSI).

All figures below come from the verified snapshot and the indicator tool outputs, which agree row-for-row with the raw OHLCV pull — **no data discrepancies were found**.

---

## 2. Price structure: a vertical July advance just hit its first pothole

**Verified latest session (2026-07-20):** Open 333.51, High 333.71, Low 323.68, **Close 326.59**, Volume 53.47M.

That is a **−7.15 (−2.14%)** change from the 2026-07-17 close of 333.74, and critically it is a *reversal candle*: price opened essentially at the high (333.71 vs. open 333.51) and closed within ~3 points of the low. The intraday range of 10.03 points is ~1.2× the current ATR of 8.27, so this was an above-average-range down day.

The context matters more than the day itself:

- **The run-up:** close 281.74 on 2026-06-29 → close 333.74 on 2026-07-17 = **+52.00 (+18.46%) in 13 sessions**, including two large gap-up demand days: 2026-07-02 (open 294.12 → close 308.63, +4.9% on 75.4M shares) and 2026-07-15 (open 317.62 → close 327.50, +4.0% on 61.0M shares).
- **The high-water mark:** intraday **334.99 on 2026-07-17** (with 334.68 on 2026-07-16) — that cluster is now the immediate resistance shelf.
- **The pullback:** the 2026-07-20 close of 326.59 sits *below* the 2026-07-15 close of 327.50, meaning the last four sessions of buyers are roughly flat-to-underwater — a classic short-term exhaustion footprint after a parabolic leg.

**Important context on the June shakeout:** on 2026-06-25 AAPL fell from 293.08 to 275.15 (**−6.12%**) on 107.0M shares, followed by a **261.8M-share** session on 2026-06-26 (index-rebalance-like volume) that closed at 283.78. The rally into July was built directly on top of that flush — a high-volume capititation-then-reclaim pattern, which historically tends to be a *constructive* base rather than a top, but it also left the stock with a wide, volatile trading range.

---

## 3. Trend: textbook bullish alignment, but extended

| MA | Value (2026-07-20) | Close vs. MA |
|---|---|---|
| `close_10_ema` | **320.98** | +1.7% above |
| `close_50_sma` | **303.43** | +7.6% above |
| `close_200_sma` | **274.58** | +18.9% above |

- The stack is perfectly ordered (10 EMA > 50 SMA > 200 SMA) and **all three are rising**. The 50 SMA has climbed for 40+ consecutive sessions, from 269.49 on 2026-05-21 to 303.43 today. The 200 SMA has risen from 261.07 (2026-05-21) to 274.58 — slow but monotonic, i.e., no death-cross risk anywhere in sight.
- The 50 SMA crossed above the 200 SMA well before this window and the spread is now widening (+28.85 points), which is the signature of a **maturing, accelerating uptrend**.
- However, price is **+7.6% above the 50 SMA**. For a mega-cap, that is a stretched relationship. In the May–June leg, price ran as far as ~305 vs. a 50 SMA of ~278 (≈+9.7%) before the 2026-06-25 flush. So the current extension is meaningful but not yet at the prior extreme — there is room for a further squeeze, but the reward/risk for chasing here is poor.

---

## 4. Momentum: strong, but decelerating at the margin

**MACD / Signal / Histogram (2026-07-20): 8.883 / 6.159 / +2.724**

- The cycle reads cleanly: a **bearish cross on 2026-06-03** (MACD 9.51 vs. signal 9.75) preceded the June decline; MACD went **negative from 2026-06-25 through 2026-07-01** (trough −2.916 on 2026-06-29); a **bullish recross occurred on 2026-07-02** (MACD −0.686 vs. signal −0.947), and MACD reclaimed zero on 2026-07-06.
- Since then, MACD has gone essentially vertical: 0.879 (7/06) → 2.959 (7/08) → 5.240 (7/13) → 8.883 (7/20). That is a genuine, confirmed momentum regime shift, and both lines are rising.
- **The nuance that matters on the day:** the histogram *shrank* from 3.337 on 2026-07-17 (8.815 − 5.478) to 2.724 today. MACD itself barely advanced (8.815 → 8.883). That is the first evidence in nine sessions that the *rate of* momentum expansion has stalled. First-derivative deterioration of a stretched oscillator is an early warning, not a sell signal.

**RSI (2026-07-20): 63.87**

- RSI pushed into overbought on 2026-07-16 (71.43) and 2026-07-17 (**71.65**) — the first 70+ readings since the May–June top zone (78.8 on 2026-05-29). It has now cooled to 63.87 without price breaking down.
- This is a *mid-range* reading with a bullish trend: in a strong uptrend, RSI 60–65 is the "buy-the-dip" region rather than a warning. The May–June precedent is instructive and cautionary in equal measure: RSI sat at 76–80 for most of late May, then AAPL fell ~11% from 315.20 (2026-06-02 close) to 275.15 (2026-06-25) as RSI collapsed to 32.20. **RSI stayed extreme for a week before the break — so RSI alone is not timing.**
- No regular bearish divergence is confirmed yet: RSI at 71.65 (7/17) vs. RSI 68.77 (7/15) tracked the higher price high, and today's lower RSI accompanies a lower close — consistent, not divergent.

---

## 5. Volume: buyers are in control but sitting on profit

**VWMA (2026-07-20): 314.02** — price is **+4.0% above** the volume-weighted average price.

- The VWMA's path shows exactly where volume went: it *fell* from 308.56 (2026-06-08) to a trough of 288.84 (2026-06-30) on that heavy June decline, then turned up sharply — 296.42 (7/15) → 300.72 (7/16) → 310.27 (7/17) → 314.02 (7/20). A climbing VWMA accompanied by price above it is one of the cleaner confirmations of *institutional* accumulation.
- The offset: with the volume-weighted cost basis at 314.02 and price at 326.59, the average recent buyer holds a ~4% paper gain. That is precisely the pool of supply that produced the 2026-07-20 reversal. Expect 314–317 to be the first real shelf where that supply gets absorbed.
- **Volume detail worth flagging:** the 2026-07-20 decline occurred on 53.47M shares, *below* the 63.41M of 2026-07-17 and 62.97M of 2026-07-16. A reversal on contracting volume is far less damaging than distribution on expansion — this argues for "pause/consolidation" rather than "top."

---

## 6. Volatility and risk budgeting

**ATR (14): 8.269** = **2.53% of the 326.59 close.**

- ATR has inflated structurally: 5.81 (2026-05-21) → 7.29 (2026-06-09) → 8.26 (2026-06-30) → 8.74 peak (2026-07-02) → 8.27 today. Volatility roughly **+42%** over two months even as price trended *up*. Position sizes should be scaled down accordingly: the same dollar risk now buys ~42% fewer shares than in May.
- For reference on band positioning (from the snapshot, not a selected indicator): Bollinger mid 306.947, upper **341.700**, lower 272.194. Price at 326.59 sits about a quarter of the way inside the upper band — **not** at a breakout-pinning extreme, and ~15.1 points below the upper band. The upper band at ~341.70 roughly coincides with the ATR-based upside extension from the 334.99 high.

---

## 7. Actionable levels and scenarios

**Immediate resistance**
- **334.99 / 334.68** — 2026-07-17 and 2026-07-16 intraday highs. A close above 334.99 re-opens the trend and targets the upper Bollinger band near **341.70**.
- 333.71 (2026-07-20 high) is the intraday lid to clear first.

**Immediate support (in order)**
1. **320.98** — 10 EMA. Holding this on a closing basis keeps the short-term trend intact.
2. **317.31 / 316.22** — closes of 2026-07-13 and 2026-07-09; also the 2026-07-15 open (317.62). A dense intraday shelf.
3. **314.02** — VWMA / volume-weighted cost basis. This is the highest-conviction pullback-buy zone.
4. **306.95** — Bollinger mid / 20-SMA; ~**303.43** is the rising 50 SMA just beneath it. A break of 303 would shift the medium-term structure from "uptrend with pullback" to "trend in question."

**Scenarios**
- **Bull continuation (base case while 10 EMA holds on a close):** the 2026-07-20 candle is digested in a 320–335 range for several sessions, RSI resets toward 55–60, MACD histogram stops shrinking, and a close above 334.99 targets 341.70. This fits the pattern of the July gap-up days, which were real demand, not exhaustion gaps (both closed near session highs).
- **Deeper consolidation (needs watching):** a close below 320.98 opens a slide to the 314–317 cluster. Given ATR of 8.27, that is ~1 ATR down, a routine two-day move. Only a close below **303.43** would invalidate the medium-term trend thesis.
- **Failed-rally/top risk:** the May–June analogue — RSI 78–80, price ~+9.7% above the 50 SMA, followed by an 11% drawdown. Today's setup is *less* extended (RSI 64, +7.6% above the 50 SMA) and today's decline came on lighter volume, so the analogue is a reason for discipline, not a reason to short.

**Risk management guidance**
- Use **1.5× ATR ≈ 12.4 points** for a swing stop; a stop placed just under 314.02 (VWMA) from a 326.59 entry risks ~3.8% ≈ 1.5 ATR — a coherent, volatility-matched placement.
- Avoid new full-size entries at the 333–335 shelf after a reversal day. Add on confirmation (close above 334.99) or on a controlled retest of 314–321, not in the middle of the gap zone.

---

## 8. Bottom line

AAPL is in a **confirmed, structurally healthy uptrend** — rising 10 EMA/50 SMA/200 SMA in perfect order, a volume-weighted average that is climbing, MACD positive and above signal after a genuine July regime flip, and a price +32.4% off the 2026-03-30 close of 246.63. The 2026-07-20 session, however, is the **first clear distribution-flavored candle of the July advance**: a −2.14% open-at-the-high reversal from just under the 334.99 record high, with the MACD histogram contracting for the first time in nine sessions and RSI dropping ~7.8 points from an overbought 71.65. Because that reversal came on *below-average* volume, the evidence supports **"pause and consolidate"** rather than **"trend reversal."** The tradeable edge now is patience: buy the 314–321 volume-weighted/10-EMA zone or the confirmed breakout above 334.99, size positions off the elevated 8.27 ATR, and treat a close under 303.43 as the signal that the medium-term uptrend has broken.

---

## Key Points Summary

| Category | Indicator / Level | Latest value (2026-07-20) | Reading | Signal |
|---|---|---|---|---|
| Price | Close | 326.59 | −7.15 (−2.14%) vs 333.74 on 7/17; open 333.51, high 333.71, low 323.68 | Bearish reversal day at highs |
| Price | Record zone | 334.99 (7/17 high) | Rejected just below | Immediate resistance |
| Trend | `close_10_ema` | 320.98 | Price +1.7% above; rising | Short-term trend intact |
| Trend | `close_50_sma` | 303.43 | Price +7.6% above; 40+ session rise from 269.49 | Bullish but extended |
| Trend | `close_200_sma` | 274.58 | Price +18.9% above; rising since 261.07 | Long-term bull regime confirmed |
| Momentum | `macd` | 8.883 | Bullish recross 7/02; zero reclaimed 7/06 | Positive |
| Momentum | `macds` | 6.159 | Below MACD; both rising | Bullish |
| Momentum | Histogram (MACD−Signal) | +2.724 | Shrank from 3.337 on 7/17 | Early deceleration warning |
| Momentum | `rsi` | 63.87 | Down from 71.65 (7/17) / 71.43 (7/16); no confirmed divergence | Overbought has reset; neutral-bullish |
| Volatility | `atr` | 8.269 (2.53% of price) | Up from 5.81 on 5/21 (+42%) | Reduce position size; stops ≈1.5×ATR (12.4 pts) |
| Volume | `vwma` | 314.02 | Price +4.0% above; VWMA rising sharply 296.42→314.02 in 4 sessions | Accumulation confirmed; profit-taking supply risk |
| Volume | Volume 7/20 | 53.47M | Below 63.41M (7/17) and 62.97M (7/16) | Weak-volume pullback = less bearish |
| Band (snapshot, not selected) | Boll mid / upper / lower | 306.947 / 341.700 / 272.194 | Price ~quarter-way inside upper band | Not band-riding; upside room to ~341.70 |
| Level | Support 1 | 320.98 (10 EMA) | First line of defense | Hold = base case intact |
| Level | Support 2 | 317.31 / 316.22 / 314.02 | Prior closes + VWMA cost basis | Preferred pullback-buy zone |
| Level | Support 3 | 306.95 / 303.43 | Boll mid / 50 SMA | Close below 303.43 = trend broken |
| Context | June shakeout | 6/25 close 275.15 (−6.12%), 6/26 volume 261.8M | Capitulation then reclaim | Constructive base, wider range risk |
| Context | July run | 281.74 (6/29) → 333.74 (7/17) = +18.46% | Two volume-backed gap days (7/02, 7/15) | Real demand, but stretched |
| **Net stance** | — | — | Uptrend intact, short-term extended and cooling | **Hold / buy 314–321 or breakout >334.99; invalidate <303.43** |

*Note: all OHLCV and indicator values above are sourced from the verified market snapshot for 2026-07-20 and the indicator tool outputs, which matched each other exactly. The snapshot's `mfi` field printed as 0.817641 — the scale is ambiguous (0–1 would imply ~82, i.e., overbought), so I have excluded it from the analysis rather than infer a reading. Dividends of $0.26 (2026-02-09) and $0.27 (2026-05-11) are noted but not material to this technical read.*