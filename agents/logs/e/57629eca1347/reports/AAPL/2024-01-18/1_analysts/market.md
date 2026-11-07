# AAPL — Technical Assessment, 2024‑01‑18

## 1. Verified Market Snapshot (source of truth)

| Field | Value |
|---|---|
| Date | 2024‑01‑18 |
| Open | 186.09 |
| High | 189.14 |
| Low | 185.83 |
| **Close** | **188.63** |
| Volume | 78,005,800 |
| Prev. close (01‑17) | 182.68 |
| 1‑day change | **+3.26%** (188.63 vs 182.68) |
| Gap vs prior close | +1.87% (open 186.09 vs 182.68) |
| Close position in day's range | ~85% (188.63 within 185.83–189.14) |

Indicator values on the latest visible session (verified snapshot):

| Indicator | Value | Read |
|---|---|---|
| close_50_sma | 189.5554 | Price **below** by −0.49% |
| close_200_sma | 181.0270 | Price **above** by +4.20% |
| close_10_ema | 185.9635 | Price **above** by +1.43% |
| macd | −1.5621 | Below zero |
| macds | −1.2789 | MACD below signal |
| macdh | −0.2832 | Negative but contracting hard |
| rsi | 51.5886 | Neutral |
| boll (mid) | 188.4340 | Price **just above** (+0.10%) |
| boll_ub | 198.4974 | +5.23% above close |
| boll_lb | 178.3706 | −5.44% below close |
| atr | 3.3406 | 1.77% of price; highest in 40 sessions |
| vwma | 185.2534 | Price **above** by +1.82% |

**Consistency check:** the frozen OHLCV CSV and the verified snapshot agree exactly on the 2024‑01‑18 row (188.63 close, 78,005,800 volume) and on every indicator value. No discrepancy to flag.

---

## 2. Indicator Selection (8, non‑redundant)

1. **close_200_sma** — anchors the *strategic* trend so we don't mistake a pullback for a breakdown.
2. **close_50_sma** — the exact line price is fighting with right now; the pivot of the whole setup.
3. **close_10_ema** — short-term responsiveness to time entries once the turn is confirmed.
4. **macd** (with **macds**/**macdh** as one family) — momentum regime and early crossover detection.
5. **rsi** — confirms whether the bounce is overbought (it isn't) and whether momentum reset was complete.
6. **boll / boll_ub / boll_lb** — gives the 20‑day mean (188.43) plus a volatility envelope that has recently *expanded*, not squeezed.
7. **atr** — position sizing and stop placement, essential because ATR is at a 40‑session high.
8. **vwma** — volume‑weighted confirmation; the only indicator that tells us whether the 3.26% rally on 78M shares was *paid for*.

Deliberately excluded: stochrsi (redundant with RSI), MFI (the snapshot's 0.3887 scale is ambiguous and I won't over‑read it), and no second volatility measure beyond ATR + Bollinger.

---

## 3. Trend Structure: A Correction Inside an Uptrend, Now at the Decision Line

**Long‑term (strategic) trend: intact and positive.**
- 200‑day SMA = **181.03**, and it has risen monotonically every session in the visible window (175.09 on 2023‑11‑30 → 181.03 on 2024‑01‑18).
- Close is 4.20% above it.
- 50‑day SMA (189.56) sits **4.66% above** the 200‑day SMA — a still‑valid bullish moving‑average stack (no death cross).

**Medium‑term trend: corrective.**
- The stock peaked at a **198.11 close on 2023‑12‑14** (intraday high 199.62) and fell to a **181.18 close on 2024‑01‑05** — a **−8.55% drawdown** over 14 sessions.
- Since that low, AAPL has recovered to 188.63, **+4.11% over 8 sessions** (01‑08 to 01‑18).
- The 50‑day SMA kept rising through the decline (186.63 on 12‑29 → 189.56 on 01‑18), which is why price is *still* 0.49% below it — the average has been catching down to price, not leading it higher.

**Short‑term: turning up, but only one day old.**
- 10‑day EMA bottomed at **185.37 on 01‑17** and ticked up to **185.96 on 01‑18** — the first up‑tick in that series since 12‑19.
- Crucially, 10 EMA (185.96) is still **below** the 50 SMA (189.56). Short‑term is repairing *within* a medium‑term downtrend channel, not yet leading it.

**Where price sits in the January range:** the 01‑02 session gapped down from the 12‑29 close of 192.53 to a 187.15 open, leaving an unfilled gap zone of roughly **187.15–192.53**. The 01‑18 close of 188.63 puts price **inside that gap**, having finally cleared the 01‑08 to 01‑12 congestion (highs of 185.60, 185.15, 186.40, 187.05, 186.74). That is the single most constructive structural fact in this report.

---

## 4. Momentum: Improving Off a Washout, Not Yet Confirmed

**RSI — the reset is complete.** RSI fell from 69.69 (2023‑12‑14) to **28.79 on 2024‑01‑05** — a genuine oversold reading, not a shallow dip. It then jumped **28.79 → 41.34 on 01‑08** (+12.5 pts), stalled/drifted back to **36.71 on 01‑17**, and exploded **+14.9 pts to 51.59 on 01‑18**. That last jump is the largest single‑session RSI advance in the 40‑session lookback. At 51.59 the indicator is neutral: **no overbought ceiling for ~18 points of RSI room**, and the oversold fuel has been spent. RSI is confirming, not warning.

**MACD — still bearish, but deteriorating bearishness fast.**
- MACD line: −1.9256 (01‑17) → **−1.5621** (01‑18), a **+0.364** jump — the largest one‑day rise in the visible MACD series.
- Signal: −1.2789. MACD remains **0.283 below** its signal — **no bullish crossover yet**.
- Histogram: −0.7175 → **−0.2832**. This is the key nuance: the histogram has now contracted four consecutive sessions (from −2.0447 on 01‑05). It is *approaching* zero, which historically in this series precedes the cross.
- **Actionable rule:** the MACD/signal cross turns bullish when **macdh > 0**, i.e. MACD needs roughly another ~0.28 points of improvement. A flat-to-up session on 01‑19 would likely do it. Do not front‑run this; the line is still below zero, so even a cross is a "zero‑line recovery" signal, weaker than a cross above zero.

**The caution flag from the last bounce:** on 01‑08 RSI also jumped hard (28.79→41.34) on a +2.42% day, and the stock then chopped for six sessions and printed a **slightly higher but essentially equal low** (01‑17 intraday 180.30 vs 01‑05 intraday 180.17 — a $0.13 difference, statistically meaningless). So the 01‑18 move is *better* (bigger %, +3.26% vs +2.42%), but "one strong day" in this name has already failed once this month. 01‑18 is a hypothesis; 01‑19 is the test.

---

## 5. Volatility: Expansion, Not Squeeze — Size Down

- **ATR = 3.3406**, up from **2.57 on 12‑29** (+30%). It is the highest reading in the 40‑session lookback, and 1.77% of price.
- Bollinger bandwidth = (198.4974 − 178.3706) / 188.4340 = **10.68%**, versus **4.64%** on 12‑29. The envelope has **doubled in width** — this is a volatility *expansion* regime.
- Consequence: this is **not** a squeeze‑breakout setup. Do not apply tight stops. A 1×ATR stop from a 188.63 entry is 185.29; 1.5×ATR is 183.62. Anything inside ~3.30 points of entry is inside normal daily noise right now.
- Position sizing: at 1.77% ATR, a $10,000 risk budget at 1.5×ATR supports materially fewer shares than in late December. Halve normal unit size until ATR prints back under ~3.00.

---

## 6. Volume: The 01‑18 Rally Was Paid For

- Volume **78,005,800** vs a 12‑session mean of roughly **58.7M** → **~1.33× normal**. That is the second‑heaviest session since 2023‑12‑15 (128.5M, a quarterly‑expiry session).
- It is **~32% heavier** than the 01‑08 bounce day (59.1M) — the clearest differentiator between this rally attempt and the failed January one.
- **VWMA = 185.2534**, and the close is **+1.82% above it**. Checking the series: the close had been *below* VWMA every single session from 2023‑12‑20 through 2024‑01‑17. **01‑18 is the first close above the volume‑weighted average since 2023‑12‑19.** That is a meaningful regime shift: buyers are now paying up above the volume‑weighted cost basis of the recent tape.
- Caveat: VWMA itself is still *falling* (195.11 on 12‑21 → 185.25 on 01‑18). Price has crossed above a descending VWMA — constructive, but the trend of volume‑weighted price is still down. Need 2–3 more sessions of above‑VWMA closes to flip that.

---

## 7. Bollinger: First Close Above the 20‑Day Mean in 19 Sessions

- Middle band (20‑SMA) = **188.4340**; close 188.63 is **+0.10% above** it.
- The close had been below the middle band every session from **2023‑12‑22** (193.60 vs 193.6685) through **2024‑01‑17** (182.68 vs 188.797). **01‑18 ends a 19‑session streak of sub‑mean closes.** In mean‑reversion terms, that is the statistical "all clear" on the January breakdown.
- But the margin is razor thin (+$0.20). A close back under 188.43 would invalidate it immediately. Treat 188.43 as a binary line, not a zone.
- Upper band 198.50 / lower band 178.37 bracket a wide 5.2%–5.4% two‑sided envelope. Price is nowhere near either extreme — consistent with a fresh trend leg rather than an exhaustion move.

---

## 8. Levels Map (all from tool output)

| Level | Price | Source | Role |
|---|---|---|---|
| Bollinger upper | 198.50 | boll_ub 01‑18 | Major upside objective |
| 2023‑12‑29 close / gap top | 192.53 | OHLCV | Full gap fill; strong resistance shelf |
| **50‑day SMA** | **189.56** | close_50_sma | **The pivot — first real resistance** |
| 01‑18 high | 189.14 | OHLCV | Immediate intraday ceiling |
| **Close** | **188.63** | verified | — |
| Bollinger mid / 20‑SMA | 188.43 | boll | Must hold on closing basis |
| 10‑day EMA | 185.96 | close_10_ema | First dynamic support |
| 01‑18 low | 185.83 | OHLCV | Session floor |
| **VWMA** | **185.25** | vwma | **Best risk pivot (confluence w/ 10EMA)** |
| 01‑12 close | 185.92 | OHLCV | Minor |
| 01‑17 close | 182.68 | OHLCV | Breakdown trigger if lost |
| **200‑day SMA** | **181.03** | close_200_sma | **Line in the sand; long‑term trend** |
| Jan intraday lows | 180.30 / 180.17 | OHLCV 01‑17 / 01‑05 | Last defense |
| Bollinger lower | 178.37 | boll_lb | Capitulation zone |

Note on the 200‑SMA: on 01‑17 the intraday low of **180.30** traded marginally *below* that session's 200‑SMA value of **180.91**, before closing back above at 182.68. I am **not** calling that a validated support bounce — one marginal undercut-and-reclaim in a high‑ATR tape is not enough evidence. It is a *coincidence of levels worth watching*, nothing more.

---

## 9. Actionable Plan

**Bias: cautiously constructive / neutral‑to‑long with confirmation required.** The setup is a textbook "pullback within an uptrend approaching its first trend‑line test," but every short‑term signal is exactly one session old and MACD has not crossed.

**Bull case (needs 01‑19 confirmation):**
- Trigger A: **daily close above 189.56 (50‑SMA)** — confirms the medium‑term average is no longer resistance. Volume should stay above ~60M.
- Trigger B: **macdh turns positive** (MACD crosses its signal) — mechanical momentum confirmation. Currently −0.2832.
- Entry approach: rather than chasing 188.63 into the 50‑SMA, prefer (i) a close above 189.56 with follow‑through, or (ii) a pullback hold of **185.25–185.96** (VWMA / 10 EMA), which offers far better reward:risk.
- Stop: **below 185.25** for the pullback entry (~1×ATR, 3.4 pts); **below 183.62** (1.5×ATR) for a breakout entry at 189.56+.
- Targets: **189.56** → **192.53** (gap fill) → **198.50** (Boll upper). Risk/reward from 188.63 with a 185.25 stop and a 192.53 first target is roughly 3.8 : 3.3 — acceptable only if the position is sized for the current 3.34 ATR.

**Bear case (what kills this):**
- A close **back below 188.43** (Boll mid) on 01‑19 would negate the streak‑break and mark 01‑18 as a one‑day gap‑fill failure — precisely the 01‑08 pattern repeating.
- A close below **185.25 (VWMA)** voids the volume thesis; below **182.68** targets **181.03 (200‑SMA)** and then **180.17–180.30**. A decisive close below **180.17** breaks the long‑term trend line for the first time since the October lows (Boll lower 178.37 becomes the magnet).

**Risk management specifics:**
- ATR 3.34 = 1.77% of price. Assume ±1 ATR of intraday noise. Use limit orders, not market orders, into this tape.
- Reduce unit size ~30–50% versus late‑December norms until ATR < 3.00.
- Do **not** add on the same day as entry; the last three January rally attempts all gave a second, better entry within 2–5 sessions (01‑08 example: entry at 185.56 was followed by 183.63 on 01‑10 and 180.30 intraday on 01‑17).

**What would change the verdict:** two consecutive closes above the 50‑SMA with volume > 65M, plus MACD histogram > 0, flips this to a confirmed trend‑resumption long with 192.53 then 198.50 as objectives. Conversely, failure at 188.43–189.56 followed by a close under 185.25 argues the 01‑18 gap was a liquidity event inside a still‑corrective 4‑week range bounded at 178.37–192.53.

---

## 10. Summary Table

| Dimension | Reading (2024‑01‑18) | Interpretation | Signal |
|---|---|---|---|
| Close | 188.63 (+3.26% d/d) | Strongest day since early Jan; closed at 85% of range | Bullish |
| Volume | 78.0M vs ~58.7M avg (1.33×) | Conviction behind the move; 32% above the 01‑08 failed bounce | Bullish |
| 200‑SMA | 181.03, rising, price +4.20% | Long‑term uptrend structurally intact | Bullish |
| 50‑SMA | 189.56, price −0.49% | Price still capped; the immediate battleground | Neutral/critical |
| 10‑EMA | 185.96, first up‑tick since 12‑19 | Short‑term turn just beginning, still < 50‑SMA | Mildly bullish |
| MACD family | −1.562 / −1.279 / −0.283 | Below zero, no cross, but histogram +0.434 d/d (largest in window) | Improving, unconfirmed |
| RSI | 51.59 (from 36.71) | Oversold reset complete; neutral, ~18 pts of headroom | Bullish backdrop |
| Bollinger | Mid 188.43 (just reclaimed), UB 198.50, LB 178.37 | Ends 19‑session sub‑mean streak; bandwidth 10.7% = expansion | Bullish, marginal |
| ATR | 3.3406 (40‑session high, 1.77%) | Volatility expanding → smaller size, wider stops | Risk flag |
| VWMA | 185.25, price +1.82% | First close above VWMA since 2023‑12‑19 | Bullish regime shift |
| Net stance | Pullback inside uptrend, testing 50‑SMA | Long bias only on a close > 189.56 or a hold of 185.25–185.96 | Cautious long / wait for confirmation |

*All prices, volumes, and indicator values above are taken directly from the verified market snapshot and the frozen OHLCV/indicator series for 2024‑01‑18. No figure in this report is estimated or inferred beyond the arithmetic percentages explicitly shown.*