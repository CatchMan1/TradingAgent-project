# GOOGL — Alphabet Inc. — Multi-Timeframe Technical Assessment
**Analysis date: 2026-08-07 (last completed session) | Close: $354.30**

---

## 1. Data integrity & verification note

I first pulled the full 2026 OHLCV series (150 sessions, 2026-01-02 → 2026-08-07) and then requested the deterministic verification snapshot for 2026-08-07. **No discrepancies were found between the two sources.** Cross-checks:

| Value | `get_stock_data` | Verified snapshot | Match |
|---|---|---|---|
| Close 08-07 | 354.29998779 | 354.29998779 | ✅ |
| Open / High / Low 08-07 | 356.72 / 358.90 / 353.78 | 356.72 / 358.90 / 353.78 | ✅ |
| Volume 08-07 | 19,859,900 | 19,859,900 | ✅ |
| close_50_sma | — | 356.505599 | ✅ (matches indicator pull) |
| rsi | — | 50.745265 | ✅ (indicator pull: 50.74526) |
| atr | — | 12.858912 | ✅ |
| macd / macds / macdh | — | 0.93762 / -2.04849 / 2.98611 | ✅ |

Corporate actions: `split = 1.0` on every row; two cash dividends are recorded — **$0.21 on 2026-03-09** and **$0.22 on 2026-06-08**. The total-return index therefore sits marginally above the raw close (357.46 vs 354.30 on 08-07). All prices below are **raw (unadjusted-for-dividend) closes**; the dividend drag on the whole series is negligible (~$0.43, ~0.12%).

---

## 2. Selected indicators (8) and why they fit this market context

The current context is **not a clean trend** — it is a violent, high-volatility whipsaw inside a broader multi-month downtrend, with a long-term uptrend still intact underneath. That calls for a set that separates *trend hierarchy* from *momentum thrust* from *volatility envelope*.

| # | Indicator | Role in this specific setup | Why non-redundant |
|---|---|---|---|
| 1 | **close_10_ema** | Short-term pivot / has the rebound stalled? | Price is *0.08%* from it — a genuine knife-edge |
| 2 | **close_50_sma** | Medium-term trend + the failed-reclaim line | Falling for 19 sessions = the dominant headwind |
| 3 | **close_200_sma** | Long-term regime filter | Rising, price +7.7% above → bull structure intact |
| 4 | **macd** | Regime flip: signal-line and zero-line reclaim | Captures the 07-31→08-05 momentum turn |
| 5 | **macdh** | Thrust magnitude and *decay* | Reveals momentum already rolling over since 08-04 |
| 6 | **rsi** | Overbought/oversold reset, 70/30 context | Reset 62.6→50.7 without breaking down |
| 7 | **boll_ub** | Where the 08-05 blow-off died | Band-tag rejection is the key bearish evidence |
| 8 | **atr** | Position sizing and stop placement | Vol is 3.6% of price — sizing is the main risk lever |

*Supplementary context from the same verified computation (not part of the core 8): Bollinger middle 348.762, lower band 314.999, VWMA 345.105, and the snapshot's MFI of 0.486 (≈48.6 on a 0–100 scale, i.e. neutral money flow) — all corroborate the neutral-to-cautious read.*

---

## 3. Price structure: a three-act year

**Act 1 — January to May: powerful uptrend.**
GOOGL opened 2026 at 315.15 (01-02), dipped to 273.50 (03-30), then staged a major re-rating. The 04-30 session gapped from a 349.94 close to a 374.07 open and closed at **384.80 on 72.0M shares** — the single largest up-volume event in the dataset. The advance peaked at a **400.80 close on 2026-05-08** (intraday high 408.61 on 05-18, 403.70 on 05-13).

**Act 2 — mid-May to 07-23: distribution and downtrend.**
From 400.80 the stock bled lower for two months. The 50-day SMA topped out at **372.80 on 2026-07-13** and has fallen every session since. The decline accelerated into a high-volume gap-down on **2026-07-23: prior close 342.09 → open 321.13, close 317.69 (-7.13%) on 69.4M shares**. That print pierced the lower Bollinger band (329.21 that day, 314.90 low on the day vs. a 321.85 band by 07-27). Measured from the 400.80 close, that was a **-20.8% drawdown**.

**Act 3 — 07-24 to now: violent V-shaped rebound, then rejection.**
From the 317.69 low close, the stock ran **+18.9% in eight sessions** to 377.65 (08-04): 356.13 (07-31, **+6.7% on 46.5M**), 373.51 (08-03), 377.65 (08-04, high 380.52). Then came the tell:

> **2026-08-05 — open 383.34, high 384.48, low 356.77, close 362.43 on 46.9M shares.**
> A **27.71-point range (7.4% of price)**, the largest single-session expansion in the recent window, closing in the bottom ~20% of its range. The high of 384.48 exceeded that day's upper Bollinger band (382.92) by 1.56 points and was immediately rejected.

Two follow-through sessions confirmed the failure: 357.75 (08-06, high 364.13, closed near the low) and **354.30 (08-07), closing in the bottom 10% of a 353.78–358.90 range**. Net move from the 08-04 close: **-6.18% in three sessions**, giving back roughly a third of the entire rebound.

---

## 4. Indicator-by-indicator reading (verified values, 2026-08-07)

### 4.1 Moving averages — a compressed, conflicted hierarchy
- **close_10_ema = 354.566.** Price (354.30) is **$0.27 / 0.08% below** it. The 10-EMA rocketed from 336.80 (07-30) to 354.63 (08-06) and has now gone **flat** (354.57). A flat short-term average with price pinned to it = momentum stalemate.
- **close_50_sma = 356.506.** Price is **$2.21 / 0.62% below**. Critically: GOOGL closed *above* the 50-SMA for four straight sessions (**08-03: 373.51 vs 358.43; 08-04: 377.65 vs 358.23; 08-05: 362.43 vs 357.82; 08-06: 357.75 vs 357.20**) and then **lost it on 08-07**. That is a textbook failed reclaim of a declining medium-term average. The 50-SMA itself has fallen **19 consecutive sessions, from 372.80 to 356.51 (-0.86/session)**.
- **close_200_sma = 329.112**, still **rising** (+0.51/session; 319.42 on 07-13 → 329.11 now). Price is **+25.19 / +7.65% above** it.
- **Golden-cross compression:** the 50-200 gap has narrowed from **+53.38 (16.71% of the 200-SMA) on 07-13 to +27.39 (8.32%) on 08-07** — a ~1.37/session convergence. Pure extrapolation (~20 more sessions) would put a death cross in play, but the 50-SMA flattens automatically if price merely holds ~355, so treat this as a **watch item, not a forecast**.

**Verdict:** long-term uptrend intact, medium-term downtrend intact, short-term neutral. The price is trapped between a rising 200-SMA far below and a falling 50-SMA immediately overhead.

### 4.2 MACD complex — genuine bullish turn, but already decelerating
- **macd = +0.938** (from -8.833 on 07-27). It **crossed above its signal line on 07-31** (-6.143 vs -6.625) and **reclaimed the zero line on 08-05** (+0.585).
- **macds = -2.048**, MACD is above signal by 2.986.
- **macdh = +2.986**, down from the **08-04 peak of 4.451** — three consecutive declines (4.451 → 4.315 → 3.738 → 2.986). The MACD line itself ticked down for the first time on 08-07 (0.938 vs 0.943 on 08-06).

**Verdict:** the momentum *regime* flipped bullish on 07-31 and remains bullish, but the *thrust* peaked on 08-04 — exactly the session before the 08-05 reversal. The histogram is confirming the price rejection rather than contradicting it.

### 4.3 RSI — clean round-trip, no divergence
- **31.02 on 07-23** (the price low; note it did **not** break 30, and no bullish divergence formed — RSI made a lower low with price) → **62.56 on 08-04** → **50.75 now**.
- The 08-04 peak at 62.56 **never reached the 70 overbought threshold**, which is itself informative: the rebound was strong but never climactic, and RSI has now bled back to dead-center.

**Verdict:** pure neutral. RSI gives no edge here — no oversold, no overbought, no divergence. It argues against fighting either direction with conviction.

### 4.4 Bollinger envelope — extreme width, mid-band gravity
- **Middle = 348.762 | Upper = 382.525 | Lower = 314.999.**
- **Bandwidth = 67.53, or 19.4% of the middle band** — an exceptionally wide envelope, consistent with the 06-26 (114.7M) and 07-23 (69.4M) volume shocks.
- **%B = 0.582** — price sits just above the middle of the envelope.
- The full oscillation is now visible: **lower-band pierce on 07-23 (low 314.90 vs band ~316–329)** → mean-reversion → **upper-band tag-and-reject on 08-05 (high 384.48 vs band 382.92)** → back to the middle band.

**Verdict:** the two-week range has effectively been a band-to-band round trip. The middle band at **348.76** is the magnetic level; the bands are too wide to be useful as standalone triggers right now, but the *rejection quality* at the upper band is high-signal.

### 4.5 ATR — elevated and rising; size down
- **ATR = 12.859 = 3.63% of close.** It bottomed at 10.31 (07-14) and rose to **13.93 (08-05)** as the whipsaw expanded.
- Reference stops: 1×ATR = **341.44**; 1.5×ATR = **335.01**; 2×ATR = **328.58** (coincidentally just under the 200-SMA at 329.11).
- **Sizing math:** with $100,000 of equity and 1% risk ($1,000) against a 1×ATR stop (12.86/share), that is ~78 shares ≈ **$27,600 notional ≈ 27.6% of equity**. A 2×ATR stop halves that to ~14%. Do the arithmetic before entry — a 3.6% daily range on a $354 stock will punish naive full-size positions.

### 4.6 Volume cross-checks (supporting, not core selection)
- **VWMA = 345.105**, rising (340.17 on 07-30). Price is **+2.66% above** it → the volume-weighted cost basis of recent buyers sits just under the market; holders in aggregate are in modest profit, which is mildly supportive.
- **Volume signature of the reversal is bearish:** the 08-05 rejection carried **46.9M**, versus 38.7M (08-03) and 35.7M (08-04) on the two big up days. Supply met the rally at higher volume than demand created it.
- **The pullback is on fading volume:** 46.9M → 25.2M → **19.9M** (08-07), the lowest since 07-13. That is *corrective*-looking rather than panic distribution — but it equally signals an absence of aggressive buyers.
- Snapshot **MFI 0.486** (~48.6/100) corroborates neutral money flow.

---

## 5. Composite read and scenario map

**Net assessment: neutral with a short-term bearish tilt inside a longer-term bullish structure.** The bullish case rests on a rising 200-SMA, a positive MACD, price above VWMA, and a corrective-looking volume profile on the pullback. The bearish case rests on a failing 50-SMA reclaim, an upper-Bollinger rejection on the highest down-volume of the move, a rolling MACD histogram, and a decisively weak close on 08-07 near the session low. Neither side owns conviction, and RSI at 50.75 says the same thing.

*(I am assigning no numeric probabilities — the evidence does not support point estimates.)*

**Bullish scenario — requires confirmation**
- **Trigger:** a daily close **above 362.43** (the 08-05 close, the first level the reversal failed to hold) with volume **> ~35M** (above the recent 6-session average of ~35.5M).
- **Path:** 364.13 (08-06 high) → **373.5–377.6** (08-03/08-04 closes) → **380.5–384.5** (08-04 high, upper band 382.52, 08-05 high).
- **Invalidation of the bear thesis:** a close **above 384.48** reclaims the 08-05 reversal entirely and reopens the May 380–408 supply zone.
- **Confirmation would come as:** 10-EMA turning up again and re-taking the 50-SMA, MACD histogram re-expanding above 4.45.

**Bearish scenario — the path of least resistance right now**
- **Trigger:** a daily close **below 348.76** (Bollinger middle / 20-SMA), confirmed by a break of **345.11** (VWMA).
- **Path:** 341.4–342.1 (07-17 low 341.36 / 07-22 close 342.09 — also the 1×ATR stop zone) → 336.7–337.4 (07-29, 06-26 closes) → **329.1** (200-SMA). A 200-SMA break would be the first since the 2026 uptrend began and would flip the long-term regime filter.
- **Structural bear marker:** 317.69 / 314.90 (07-23) remains the line in the sand.

**Neutral/range scenario (the highest-probability *description*, not a point forecast)**
- Churn between **345 (VWMA) and 357–362 (50-SMA/08-05 close)** while the 50-SMA flattens and the Bollinger bands narrow from 19.4%. Range traders would fade the extremes; trend traders should stand aside.

---

## 6. Actionable plan — concrete levels and risk mechanics

1. **Do not chase.** Price is 0.08% from the 10-EMA and 0.62% below the 50-SMA — there is no edge in buying mid-range at 354 with an ATR of 12.86.
2. **Wait for one of the two triggers** (close >362.43 on volume, or close <348.76). Let the market pick a side out of a 19.4%-wide envelope.
3. **For a swing long:** enter only on a confirmed close above 362.43. Stop **below 341.44** (1×ATR from 354.30) or ~348.5 for a tighter, mid-band stop. Risk ≈ $13.90/share → ~72 shares per $1,000 of risk → **~25% notional** at 1% risk. First target 373.5–377.6; second 380.5–384.5.
4. **For a short/hedge:** trigger on a close below 348.76 targeting 341.4. Stop **above 362.43** (1.8×ATR of headroom). Note: shorting into a rising 200-SMA is a counter-trend trade — halve normal size.
5. **For existing holders:** the 08-05 rejection is a legitimate reason to trim into strength rather than add. The 200-SMA at 329.11 is the structural stop for a core position; a 2×ATR stop (328.58) conveniently sits right at it.
6. **Watch list:** (a) whether the 50-SMA reclaim is retried — the 50-SMA falls ~0.86/session, so by roughly 08-14 it may be near ~350, i.e. the *level* needed to reclaim is dropping even if price stalls; (b) 50/200 gap (now 8.32%, was 16.71% on 07-13); (c) volume — a low-volume retest of 348–345 that holds would be a constructive higher low.

---

## 7. Key points summary

| Category | Observation (verified 2026-08-07) | Evidence | Implication |
|---|---|---|---|
| **Price** | 354.30 close; weak close in bottom 10% of 353.78–358.90 | OHLCV 08-07 | No intraday demand at the close |
| **Short-term trend** | Flat/stalled | Price −0.08% vs 10-EMA 354.566; 10-EMA flat at 354.57 | Stalemate, no momentum edge |
| **Medium-term trend** | Down | 50-SMA 356.506, falling 19 sessions from 372.80 (07-13) | Headwind directly overhead |
| **Failed reclaim** | Closed above 50-SMA 08-03→08-06, lost it 08-07 | 373.51/377.65/362.43/357.75 vs 358.43/358.23/357.82/357.20; 354.30 vs 356.51 | Bearish tell |
| **Long-term trend** | Up, intact | 200-SMA 329.112, rising; price +7.65% above | Bull structure not yet broken |
| **Golden cross** | Compressing fast | 50–200 gap 53.38 (16.71%) on 07-13 → 27.39 (8.32%) now | Watch item, ~1.37/session |
| **MACD** | Bullish crossover + zero-line reclaim, but decaying | macd +0.938; cross 07-31; zero-line 08-05; macdh peak 4.451 (08-04) → 2.986 | Regime flipped, thrust fading |
| **RSI** | Dead neutral, no divergence | 31.02 (07-23) → 62.56 (08-04) → 50.75 | Confirms indecision |
| **Bollinger** | Band-to-band round trip; upper-band rejection | lb pierce 07-23 (low 314.90); ub 382.525 vs 08-05 high 384.48; width 19.4%; %B 0.582 | Mid-band 348.76 is the pivot |
| **Volatility** | Elevated, rising | ATR 12.859 = 3.63% of price (from 10.31 on 07-14) | Reduce size; widen stops |
| **Volume** | Distribution at highs, fading on pullback | 08-05 46.9M (reversal) > 08-03/04 up days 38.7M/35.7M; 08-07 19.9M | Corrective, but no buyers yet |
| **VWMA** | Price above volume-weighted cost | VWMA 345.105 (rising); price +2.66% | Mild support / holders in profit |
| **Resistance** | 356.5–358.9 → 362.4 → 373.5–377.6 → 380.5–384.5 → 400.8/408.6 | Multi-date clusters | Bull trigger must clear 362.43 |
| **Support** | 348.8 → 345.1 → 341.4 → 336.7 → 329.1 → 317.7/314.9 | Boll mid, VWMA, swing lows, 200-SMA | Bear trigger is 348.76 |
| **Risk math** | 1×ATR = 341.44; 2×ATR = 328.58 ≈ 200-SMA | ATR 12.859 | 1% risk ≈ 25–27% notional |
| **Stance** | **Neutral / no position bias; trade the break, not the middle** | Composite of above | Await 362.43 (long) or 348.76 (short) |

*Caveat on scope: all statements above are derived from the frozen 2026-01-02 → 2026-08-07 dataset and the verified 2026-08-07 snapshot. I have no verified evidence for 52-week extremes, historical support/resistance outside this window, or fundamental/earnings attribution for the high-volume gap sessions (04-30, 07-23, 08-05) — those are described purely by their price/volume signature.*