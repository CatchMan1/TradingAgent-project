# AMZN — Multi‑Timeframe Technical Report
**As of close 2026‑08‑17 | Reference price: $261.31**

---

## 0. Data provenance & verification

All exact OHLCV, price levels, and indicator values below come from `get_verified_market_snapshot` (2026‑08‑17) and the `get_indicators` series, both stamped on the frozen row set visible on 2026‑08‑17. The 2026‑08‑17 row is the latest visible session.

- **Latest session (2026‑08‑17):** O 265.44 / H 265.75 / L 258.34 / **C 261.31**, volume 43,896,500.
- **Discrepancy check:** the snapshot's indicator values match the independent `get_indicators` series **exactly** (10 EMA 265.191382, 50 SMA 248.31699, 200 SMA 237.86275, MACD 5.83001, signal 6.139756, histogram −0.309746, RSI 52.430887, Boll mid 257.0855 / upper 295.928771 / lower 218.242228, ATR 8.120336, VWMA 265.270273). No conflict to reconcile.
- **One flag:** the snapshot reports `mfi = 0.522961`. That is on a 0–1 scale rather than the standard 0–100, so I am **not** using it in the analysis rather than rescaling an unverified number.
- `dividend = 0.0` and `split = 1.0` on every row in the window, and `technical_total_return_index` equals `close` throughout — so price return = total return here; no adjustment artifacts.

---

## 1. Indicators selected (8) and why

| # | Indicator | Category | Role in this specific setup |
|---|---|---|---|
| 1 | `close_10_ema` | Moving average (fast) | Price just lost it on 2026‑08‑13 and was rejected at it intraday on 2026‑08‑17 → the immediate momentum line. |
| 2 | `close_50_sma` | Moving average (medium) | Rising, flattening trend line; the structural bull/bear pivot for a swing trade. |
| 3 | `close_200_sma` | Moving average (long) | Overall trend benchmark; rising since July. Defines whether this dip is a trend dip or a trend break. |
| 4 | `macd` (line + `macds` signal, `macdh` hist) | Momentum | Captures the exact turn: bullish regime since late July, first bearish histogram print on 2026‑08‑17. |
| 5 | `rsi` | Momentum | RSI cooled 72.2 → 52.4 without oversold; confirms an orderly reset, not capitulation. |
| 6 | `boll` (20 SMA; upper 295.93 / lower 218.24) | Volatility/trend baseline | The 20 SMA at 257.09 is the single most important near-term pivot; band width quantifies the post-earnings volatility regime. |
| 7 | `atr` | Volatility | Sizing and stop placement — critical after a volatility regime shift (ATR 6.89 → 9.95 → 8.12). |
| 8 | `vwma` | Volume-weighted | Shows where volume actually transacted; at 265.27 it independently confirms the 265 resistance cluster. |

Deliberately **excluded:** `boll_ub`/`boll_lb` as standalone picks (their values are read off the `boll` envelope), and any second oscillator — RSI plus a stochastic-type reading would be redundant here.

---

## 2. Price action: a post‑earnings gap that is being mean-reverted

The dominant feature on the chart is the **2026‑07‑31 gap**: AMZN closed 235.50 on 2026‑07‑30, then opened 265.00 and closed **271.58** on volume of 129.05M — a **+36.08 point (+15.3%)** single-session move on roughly 3x the surrounding turnover. It then extended to a close of **284.02 on 2026‑08‑03** (intraday high 287.20), the high of this entire window.

Since 2026‑08‑03 the tape has done nothing but fade:

| Date | Close | Volume |
|---|---|---|
| 2026‑08‑03 | 284.02 | 90.83M |
| 2026‑08‑04 | 277.42 | 69.75M |
| 2026‑08‑05 | 272.65 | 45.12M |
| 2026‑08‑06 | 272.26 | 30.67M |
| 2026‑08‑07 | 274.48 | 33.86M |
| 2026‑08‑10 | 278.09 | 35.73M |
| 2026‑08‑11 | 272.27 | 31.90M |
| 2026‑08‑12 | 267.28 | 29.94M |
| 2026‑08‑13 | 265.13 | 32.17M |
| 2026‑08‑14 | 262.65 | 27.25M |
| 2026‑08‑17 | **261.31** | **43.90M** |

Computed from those rows:
- **−8.0%** from the 2026‑08‑03 close (284.02 → 261.31); **−9.0%** from the 2026‑08‑03 intraday high of 287.20.
- 2026‑08‑17 is the **lowest close of the entire post-gap period** (i.e., since 2026‑07‑30).
- The pullback has retraced **46.8%** of the 235.50 → 284.02 advance (48.52 points); **53.2%** of the move is still retained.
- 2026‑08‑17 closed **below the 2026‑08‑14 low of 262.42** and near the session low of 258.34 — a weak close.

**Structural nuance that matters more than the percentage:** before the gap, the April–May 2026 range had a ceiling around the **274.99 close / 278.56 intraday high** area (2026‑05‑06 and 2026‑05‑05 respectively). The 2026‑08‑03 spike to 287.20 cleared it, but price has now fallen back **below that old ceiling** — the breakout has failed on a closing basis and price is back inside the pre-earnings range. That is a throwback/failed-breakout pattern, not a clean continuation.

---

## 3. Trend structure: three timeframes, three answers

**Long term — bullish and improving.**
`close_200_sma` = **237.86**, up from 233.17 on 2026‑07‑08 to 237.86 on 2026‑08‑17 — monotonically rising every session in that stretch. Price is **+23.45 (+9.9%)** above it. `close_50_sma` (248.32) sits **+10.46 above** the 200 SMA (4.4% spread) and is itself rising (246.38 on 2026‑07‑30 → 248.32). Bullish MA alignment is intact and the long-term trend is repaired from the February 2026 breakdown (low close 198.79 on 2026‑02‑13).

**Medium term — bullish but decelerating.**
The 50 SMA has flattened: it fell from 254.60 (2026‑07‑08) to 246.38 (2026‑07‑30), then turned up only modestly to 248.32 — a rise of just 1.94 points in 12 sessions. Price is **+12.99 (+5.2%)** above it. That gap can be closed by further price erosion without any trend damage.

**Short term — bearish.**
`close_10_ema` = **265.19**. Price closed below it on 2026‑08‑13, 2026‑08‑14, and 2026‑08‑17, and the 10 EMA has already rolled over (267.18 on 2026‑08‑12 → 265.19). Most telling: on **2026‑08‑17 the session high was 265.75, essentially tagging the 10 EMA at 265.19, and sellers rejected it**, closing 4.44 points lower. That is a textbook intraday rejection at the fast average.

**Net:** the short-term trend has turned down *inside* an intact medium- and long-term uptrend. This is a counter-trend pullback within a bull structure — the highest-probability interpretation — until the 50 SMA is lost on a closing basis.

---

## 4. Momentum: the turn is confirmed, but it is young

**MACD** peaked at **8.432 on 2026‑08‑11** and has declined every session since: 7.985 (08‑12) → 7.372 (08‑13) → 6.609 (08‑14) → **5.830 (08‑17)**. The signal line (`macds`) is **6.140**, so the histogram printed **−0.3097** on 2026‑08‑17 — the **first negative histogram reading since 2026‑07‑30**, ending a run of twelve consecutive positive prints (peak histogram 4.619 on 2026‑08‑05). Mechanically, a bearish MACD crossover has just occurred.

Two important gradations:
1. **Both MACD and its signal remain above zero** (5.83 and 6.14) — this is a *momentum reset within a positive regime*, not a regime flip. Compare 2026‑07‑29, when MACD was −3.75 and the histogram −1.99: the current negative histogram is an order of magnitude smaller.
2. **A mild bearish divergence preceded the high:** on 2026‑08‑10 price closed higher than 2026‑08‑07 (278.09 vs 274.48, a higher high) while the MACD histogram made a lower high (3.904 vs 4.090). Momentum stalled *before* price rolled over. Note RSI did **not** diverge (64.21 → 65.87), so the divergence signal is moderate, not strong.

**RSI** = **52.43**. The path is clean and informative: 33.31 (2026‑07‑29, near-oversold) → 72.23 (2026‑08‑03, the only overbought print) → 65.87 (08‑10) → 52.43 (08‑17). RSI has given back the entire overbought premium and now sits almost exactly mid-range. **Implication: there is no oversold cushion.** Dips can continue without triggering a mean-reversion bid, and equally there is ammunition for a resumption without overbought resistance. RSI is genuinely neutral — a poor timing tool right here, which is why the MA/level work carries the load.

---

## 5. Volume and participation: the tell is in the mix

Volume has compressed sharply since the gap: 129.05M (07‑31) → 90.83M (08‑03) → 30.67M (08‑06) → **27.25M (08‑14)**, the lowest of the window. That is exactly what a healthy post-earnings consolidation looks like — sellers not aggressive.

But **2026‑08‑17 breaks the pattern**: volume rose to **43.90M**, up ~61% from 2026‑08‑14 and about **1.33x the 5-session average of ~33.0M** (computed: 08‑11 through 08‑17). It was a down day (−1.34, −0.51%), closing below the prior day's low, near the session low. Volume expanding on a downside break of a short-term low is a mild distribution signal. It is still **below the 21-session average of ~47.8M** (computed from 2026‑07‑20 to 2026‑08‑17), so this is not climactic selling — one caution flag, not a reversal of the tape.

**VWMA** = **265.27**, still *rising* (260.45 on 08‑12 → 265.27 on 08‑17) because the gap's enormous volume still dominates the weighted average. Price at 261.31 is **−3.96 (−1.5%) below VWMA**. A sub-VWMA reading while VWMA rises means the marginal, volume-weighted holder is now underwater — recent buyers are losing money, which tends to create overhead supply on rallies back to that level.

---

## 6. Volatility regime: expansion, then bleed

ATR went 6.89 (2026‑07‑29) → **9.95 (2026‑08‑03)** → **8.12 (2026‑08‑17)**, a steady seven-session decline from the post-gap peak. ATR at 8.12 equals **3.1% of the 261.31 close** — elevated versus the ~2.8% pre-gap reading but contracting.

This matters for strategy in two ways:
- **Declining ATR during a drift lower = orderly de-risking, not panic.** It supports the "consolidation" read over a "distribution top" read.
- **Compressed-then-expanding volatility resolves in a direction.** ATR has bled for seven sessions while price coiled under 265; a break of the 257–266 bracket is likely to come with an ATR expansion, and stops placed inside 1×ATR will get clipped.

**Bollinger envelope** (20 SMA basis, 2σ): middle **257.09**, upper **295.93**, lower **218.24**. Total bandwidth is **77.69 points = 30.2% of the middle band** — an extremely wide envelope caused by the gap, and a structural warning that band edges are *not* actionable here (the lower band at 218.24 is 16.5% below spot; it cannot function as a real oversold trigger). Position within the bands: **%B ≈ 0.554** — dead center. The useful output from this indicator is the **middle line at 257.09**, which is drifting up (243.86 on 07‑31 → 257.09 on 08‑17) and is now converging on price from below.

---

## 7. The levels map (with confluence)

Every level below is derived from tool output; confluence is what gives each one weight.

**Overhead — the pivot cluster at ~265.2–265.5 (very high conviction):**
Three independent measures converge within 0.3 points:
- `close_10_ema` = **265.19**
- `vwma` = **265.27**
- 38.2% retracement of the 235.50→284.02 advance = **265.49** (computed)
- Plus the 2026‑08‑17 intraday high **265.75** — where price was just rejected.

A daily close back above **265.75** would invalidate the short-term bearish structure. Until then, this zone is supply.

**Above that:** 274.48 (08‑07 close) → **278.09 (08‑10 close)** and the 278.56 old-range intraday high → **284.02 / 287.20** (08‑03 close/high).

**Downside support:**
- **258.34** — 2026‑08‑17 session low (first line of defense).
- **259.76** — the 50% retracement of the post-gap advance (computed: 284.02 − 0.5×48.52).
- **257.09** — Bollinger middle / 20 SMA, and rising. **Confluence shelf at 257–260** combining the 50% retrace, the session low, and the 20 SMA.
- **254.03** — 61.8% retracement (computed).
- **248.32** — `close_50_sma`. This is the structural bull line: the last 12 sessions have not come near it.
- **239.82** — 2026‑07‑30 high = the **gap-fill target** (full gap closure). Note how close this sits to the **200 SMA at 237.86**, making **237.9–239.8** the ultimate structural backstop where gap fill and the long-term average coincide.

---

## 8. Scenarios and triggers

**Base case — continued digestion inside 257–266 (neutral).** Price has already retraced 46.8% of the gap on shrinking ATR and thin volume. The most likely path is a few more sessions of chop between the 20 SMA (257.09) and the 10 EMA/VWMA cluster (265.2–265.5), letting the 10 EMA catch down to price. Confirmation: ATR continues to fall and volume stays under ~35M.

**Bull resumption (needs a trigger, don't front-run it).** Trigger: a **daily close above 265.75** — ideally on volume above the ~47.8M 21-session average — which would reclaim the 10 EMA, VWMA, and the 38.2% retrace simultaneously, and would likely coincide with the MACD histogram curling back positive. Targets: 274.5, then 278.1, then 284.02/287.20. Note the RSI reset from 72 to 52 leaves room for this without immediately re-entering overbought.

**Deeper mean reversion (the risk case).** Trigger: a **daily close below 257.09** (20 SMA), particularly with volume above ~50M. That converts 257–260 from floor to ceiling and opens 254.03 (61.8%), then 248.32 (50 SMA). A close under the 50 SMA would be the first material crack in the medium-term trend and would put a partial gap fill toward 239.8–237.9 on the table. That would be roughly a further 9% drawdown from 261.31 — worth sizing for even if you consider it the less likely branch.

**Bias statement:** constructive on the *structure* (above a rising 50/200 SMA pair, MACD still above zero, RSI neutral not overbought), cautious on the *timing* (below 10 EMA, below VWMA, first bearish MACD histogram, weak 2026‑08‑17 close on rising volume). Net posture: **wait for the resolution of 257–266 rather than anticipate it.** Neither chasing the fade nor buying the dip mid-range is well-compensated here.

---

## 9. Risk management and execution

- **ATR = 8.12 (3.1% of price).** Volatility-normalized stops:
  - Tactical long off a 257–259 hold: 1×ATR stop ≈ **248.9–251.0** — which lands just under the 50 SMA (248.32), i.e., the stop is placed beyond a real level rather than at a random distance. Good.
  - Momentum long on a 265.75 reclaim: 1×ATR stop ≈ **257.6**, which sits on the 20 SMA/50% retrace shelf. Also structurally coherent.
  - Existing longs: 1.5×ATR from 261.31 ≈ **249.13**; a 2×ATR stop ≈ **245.07** gives the position room through the 50 SMA but accepts meaningful give-back.
- **Position sizing:** risk budget ÷ stop distance. With a 1.5×ATR stop (12.18/share), a 1%-of-equity risk implies notional exposure ≈ 8.2% of equity per unit of risk budget. Given the 3.1% daily ATR, any position should be sized smaller than it would have been pre-gap (ATR was 6.89 on 2026‑07‑29, so volatility is ~18% higher).
- **Don't place stops at round numbers inside the 257–266 bracket** — the 2026‑08‑17 range alone was 7.41 points and price is oscillating around both the 20 SMA and the 10 EMA. Expect noise.
- **Invalidation of the cautious stance:** two consecutive closes above 265.75 with expanding volume. **Invalidation of the constructive stance:** a close below 248.32.
- **Known unknown:** the 2026‑07‑31 gap almost certainly reflects a corporate catalyst (volume 129M vs ~35M baseline). I have no event data in these tools, so I make no claim about its cause. Absent that information, treat the levels as mechanical and do not assume the fundamental move "must" be defended.

---

## 10. Monitoring checklist

1. **257.09 vs. daily closes** — the entire near-term thesis hinges on this line.
2. **265.19 / 265.27 / 265.49** — the 10 EMA / VWMA / 38.2% confluence; watch for the second rejection or the reclaim.
3. **MACD histogram sign** — −0.31 is barely negative; a flip back positive within a session or two would neutralize the crossover (whipsaw risk is real here).
4. **Volume on down days** — 43.90M on 2026‑08‑17 vs ~33M five-day average. If that escalates above ~60M on a break of 257, upgrade the bear case materially.
5. **ATR direction** — continued contraction favors range; expansion confirms the break, whichever way it goes.
6. **50 SMA slope** — currently +1.94 points over 12 sessions. If it rolls flat or down, the medium-term trend claim weakens.

---

## Key points summary

| Dimension | Reading (2026‑08‑17) | Interpretation | Actionable level / trigger |
|---|---|---|---|
| **Latest session** | O 265.44 / H 265.75 / L 258.34 / C 261.31; vol 43.90M | Weak close, below prior day's low, volume up ~61% d/d | Close 261.31 below 262.42 (08‑14 low) |
| **Short-term trend** | `close_10_ema` 265.19; price −1.5% below | Bearish; 10 EMA rejected price intraday (high 265.75) | Reclaim > 265.75 = structure repaired |
| **Medium-term trend** | `close_50_sma` 248.32, rising but flattening; price +5.2% above | Bullish, decelerating | Loss of 248.32 = trend crack |
| **Long-term trend** | `close_200_sma` 237.86, rising; 50 > 200 by 10.46; price +9.9% above | Bullish, improving | 237.9–239.8 = gap fill + 200 SMA backstop |
| **Momentum (MACD)** | MACD 5.830, signal 6.140, hist −0.310 (first negative since 07‑30); MACD peaked 8.432 on 08‑11 | Bearish crossover, but both lines > 0 → reset, not reversal | Hist curl positive = fade the bear signal |
| **Momentum (RSI)** | 52.43, from 72.23 (08‑03) | Neutral; overbought fully unwound, no oversold cushion | Not actionable standalone |
| **Volatility** | ATR 8.120 (3.1% of price), down from 9.948 (08‑03) | Orderly de-risking; coil likely to resolve | Break of 257–266 with ATR expansion |
| **Bands** | Mid 257.09 / UB 295.93 / LB 218.24; %B 0.554; width 30.2% | Center of envelope; band edges unusable | 20 SMA 257.09 = key pivot |
| **Volume-weighted** | VWMA 265.27 and rising; price −1.5% below it | Marginal volume-weighted holder underwater → overhead supply | 265.2–265.5 confluence resistance |
| **Retracement math** | 46.8% of the 235.50→284.02 advance given back | Just under half of the gap-up erased | 50% = 259.76; 61.8% = 254.03 |
| **Failed breakout** | 08‑03 close 284.02 / high 287.20 vs pre-gap ceiling ~278.56; now 261.31 | Spike above old range failed; back inside prior range | Regaining 278.09 restores the breakout |
| **Bias** | Bullish structure, bearish short-term tape | Neutral / wait-for-resolution | Range 257.09 – 265.75 defines the trade |
| **Risk** | 1×ATR stop distances: 253.19 (from 261.31); 248.9–251.0 (from 257–259 entry); 257.6 (from 265.75 entry) | Size down vs pre-gap (ATR +18% since 07‑29) | Stop beyond the 50 SMA for tactical longs |

*This is a technical analysis of verified historical data, not a guarantee of future outcomes. Levels are mechanical references derived from tool output; no historical support/resistance "bounce" claims are made beyond what the cited rows show.*