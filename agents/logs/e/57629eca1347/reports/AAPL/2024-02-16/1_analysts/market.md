# AAPL — Multi-Horizon Technical Assessment
**As-of date: 2024-02-16** | Instrument: **AAPL** (Apple Inc.)

## 0. Verified data anchor (source of truth)

All exact levels below come from the verified snapshot for 2024-02-16 and the indicator series ending on that session. The two sources agree with no discrepancies.

| Item | Value (2024-02-16) |
|---|---|
| Open / High / Low / Close | 183.42 / 184.85 / 181.67 / **182.31** |
| Volume | 49.75M |
| 10 EMA | 185.7634 |
| 50 SMA | 189.8614 |
| 200 SMA | 183.4804 |
| Bollinger mid / upper / lower | 188.6555 / 196.4520 / 180.8590 |
| RSI(14) | 36.5795 |
| MACD / Signal / Histogram | −1.3616 / −0.7089 / −0.6527 |
| ATR(14) | 3.1800 (≈1.74% of close) |
| VWMA (20) | 186.1809 |

**Data caveat:** the snapshot also returns an `mfi` field of 0.3493. A money-flow index cannot legitimately print 0.35 on a 0–100 scale, so that value appears mis-scaled or mis-computed in the vendor feed. I have excluded it from the analysis rather than interpret it. Everything else I cite is internally consistent across `get_stock_data` and `get_indicators`.

---

## 1. Indicator selection and rationale

AAPL on 2024-02-16 is in a **short-term downtrend inside an intact but eroding intermediate uptrend**, sitting exactly on the most-watched long-term line in the market (the 200-day). That regime calls for a set that (a) measures trend at three horizons, (b) detects whether bearish momentum is still accelerating or exhausting, (c) frames the volatility envelope for oversold/stretch, and (d) confirms price action with volume. I selected eight, deliberately avoiding redundancy:

1. **close_200_sma** — the strategic trend arbiter and the level currently in play.
2. **close_50_sma** — intermediate trend and the falling overhead cap.
3. **macd** — trend/momentum state change (zero-line and signal crossings).
4. **macdh** — rate of change of that momentum (acceleration vs. deceleration); MACD level alone cannot tell you whether a decline is steepening.
5. **rsi** — oscillator position for oversold/stretch and divergence checks, independent of moving-average construction.
6. **boll_lb** — statistical stretch boundary; the natural mean-reversion reference and a defensible stop-placement anchor.
7. **atr** — realized volatility for stop distance and position sizing (the single most misused input in a falling tape).
8. **vwma** — volume-weighted average price, i.e., the approximate cost basis of recent participants, which distinguishes "quiet drift" from "distribution."

**Deliberately excluded:** `close_10_ema` (185.76) sits within 0.42 of VWMA (186.18) and is falling in lockstep with it — near-duplicate information; I reference it only as confluence. `macds` is fully implied by MACD and the histogram. `boll` (mid) at 188.66 is only 1.2 below the 50 SMA at 189.86 — redundant with the 50 SMA. `boll_ub` at 196.45 is 7.7% above spot and not decision-relevant here.

---

## 2. Trend architecture: three horizons, three different answers

**Long-term (200 SMA): still up, but the price has just fallen through it.**
The 200 SMA has risen *every single session* in the visible 2024 window — from 179.637 on 2024-01-02 to 183.480 on 2024-02-16, a gain of +3.84 points (+2.1%) over 31 sessions. That is a genuinely rising long-term baseline, not a flat one. However, the 2024-02-16 close of **182.31 is 1.17 points (−0.64%) BELOW the 200 SMA at 183.4804**. This matters because *every prior close in the visible 2024 window was above that line* — including the 2024-01-17 close of 182.68 versus a 200 SMA then at 180.91. So 2024-02-16 is the **first close below the 200-day in this dataset**, and it happened on a Friday, which raises the odds of follow-through selling or index/CTA-related de-risking rather than an immediate reclaim.

**Intermediate (50 SMA): rolling over, and now overhead.**
The 50 SMA peaked at **190.9252 on 2024-01-30** and has declined for twelve straight sessions to **189.8614**. The slope is now roughly −0.088/day and steepening (the drop from 02-14 to 02-16 was −0.333 over two sessions). Price at 182.31 is **7.55 points (−3.98%) below the 50 SMA**. The 50/200 spread has compressed from +8.64 on 2024-01-30 to **+6.38 today**. With the 50 falling ~0.09/day and the 200 rising ~0.07/day, the gap closes at roughly 0.16/day — implying a **death-cross risk window of roughly 40 trading sessions (late April)**, not an immediate event. The structural "golden cross" alignment is therefore *intact but being consumed*.

**Short-term: clean, orderly downtrend.**
The tape has printed **five consecutive lower closes** on 2024-02-12 through 2024-02-16: 187.15 → 185.04 → 184.15 → 183.86 → 182.31, a loss of **−2.59% in a week**. Over the same week the 10 EMA slid from 188.40 to 185.76 and the VWMA from 188.79 to 186.18. Lower highs are unambiguous: 191.05 (02-07), 189.99 (02-09), 188.67 (02-12), 186.21 (02-13), 185.53 (02-14), 184.49 (02-15), 184.85 (02-16 — a marginal uptick inside a down close). Lows: 183.51 → 182.44 → 181.35 → 181.67, i.e. still descending but with the last low 0.32 *above* the prior one — a first, small sign of downside deceleration.

**Measured from the swing high:** from the 2024-01-23 close of 195.18 to 182.31 is **−12.87 points (−6.59%)**. From the 2023-12-14 close of 198.11 it is **−15.80 points (−7.98%)**. This is a correction, not a trend break of the primary advance (which would need the 200 SMA to flatten/turn down).

---

## 3. Momentum: bearish and re-accelerating, not yet exhausted

**MACD has completed the full bearish sequence.** The MACD line peaked at **+0.9512 on 2024-01-26**, crossed below its signal on **2024-01-31**, crossed below zero on **2024-02-01 (−0.1376)**, and has now fallen to **−1.3616** — the lowest reading since 2024-01-17 (−1.9256). Critically, the histogram shows a *second leg down*: it improved from −0.4449 (02-02) to −0.0646 (02-09) as price stabilized, then deteriorated for four consecutive sessions to **−0.6527**, the most negative print since the January 17 low. That is momentum **re-accelerating to the downside**, not basing. The histogram has now been negative for twelve consecutive sessions.

**RSI at 36.58 is weak but not washed out.** The trajectory is the story: 62.62 (2024-01-23) → 39.60 (01-31) → 50.81 (02-07) → **36.58 (02-16)**, a 26-point collapse in under four weeks and the lowest since the January 17 reading of 36.71. Two important nuances:
- **36.58 is above 30.** In a tape that has not yet capitulated, RSI typically needs to either tag ~30 or produce a *bullish divergence* (price lower low, RSI higher low) to mark a durable low. **Neither condition exists today** — price made a lower low on 02-16 while RSI also made a lower low (39.49 → 36.58). No divergence, no exhaustion signal.
- Equally, RSI is *not* in the 25–30 zone where trend-continuation shorts historically get poor entry economics. This is the awkward middle: too weak to buy the dip, too extended to chase the breakdown.

---

## 4. Volatility and stretch: near the lower band, but bands are wide

- **Bollinger position:** close 182.31 vs lower band 180.859 and mid 188.6555. **%B = 9.3%** — price is in the bottom decile of the envelope, only **1.45 points (0.46 ATR)** above the lower band. Total band width is 15.59 points, or **8.3% of the midpoint**, which is wide for AAPL. Consequence: "at the lower band" here does *not* mean "unusually stretched relative to recent realized range" — it means price is at the bottom of an unusually wide range that the late-January spike created.
- **Band dynamics:** the lower band *rose* from 178.19 (01-17) to 182.49 (02-14) as the January spike was absorbed, then **turned down to 180.86** on 02-16 as the early-February highs rolled into the window. The mid band has flattened and is now rolling (189.36 on 02-14 → 188.66 on 02-16). A flattening mid + expanding downside is a bearish-band configuration until proven otherwise.
- **ATR at 3.18 (1.74% of price)** is *below* the 2024-02-02 peak of 3.586 but above the mid-January 3.10. So the decline is being delivered with **moderate, not panicked, volatility**. That is characteristic of orderly distribution — sellers in control, buyers simply absent.
- **Position sizing:** with ATR = 3.18, a 1-ATR stop is 1.74% of price; a 2-ATR stop is 3.5%. Any stop tighter than ~1.6 points (0.5 ATR) is inside the daily noise band and will be taken out; the 02-16 range alone was 3.18 points (181.67–184.85), exactly 1 ATR.

---

## 5. Volume confirmation: distribution, with one important demand marker

The VWMA is the cleanest read here. It peaked at **189.7199 on 2024-02-07**, then fell every session to **186.1809**, and price (182.31) is **2.08% below it**. That means the volume-weighted cost basis of recent buyers is ~3.87 points above the market — recent buyers are collectively underwater, which caps rallies with supply (the "overhead trap"). VWMA is falling *faster* than the 10 EMA (VWMA −3.54 points since 02-07 vs 10 EMA −2.94), which is exactly what you see when down-days carry heavier volume than up-days.

That reading is corroborated by the raw tape:
- The 2024-02-05 → 02-09 bounce (+2.0% from 185.85 to 188.85) occurred on **declining volume**: 69.7M, 43.5M, 53.4M, 41.0M, 45.2M. Low-volume rally = short covering / lack of sellers, not accumulation.
- Then the 02-13 → 02-15 decline came on **56.5M, 54.6M, 65.4M** — Feb 15's 65.4M is the heaviest down-day volume since Feb 2's 102.6M. Rising volume on falling price = distribution.
- **The exception worth flagging:** 2024-02-02 printed **102.55M** (the heaviest session in the visible window) with a low of **179.25** and a close of 185.85 — a large intraday reversal. That single row is the strongest evidence that there is real demand in the **179–180 zone**. Any flush toward 180 should be treated as a potential *absorption* event rather than an automatic breakdown.

---

## 6. Key levels (all derived from tool output)

**Resistance (overhead stack, in order):**
| Level | Source | Distance from 182.31 |
|---|---|---|
| 183.48 | 200 SMA (rising) | +0.64% |
| 184.85 | 2024-02-16 high | +1.39% |
| 185.76 | 10 EMA | +1.89% |
| 186.18 | VWMA (falling) | +2.12% |
| 188.66 | Bollinger mid | +3.48% |
| 189.86 | 50 SMA (falling) | +4.14% |

**Support:**
| Level | Source | Distance from 182.31 |
|---|---|---|
| 181.35 | 2024-02-15 low | −0.53% |
| 180.86 | Bollinger lower band | −0.80% |
| 180.30 | 2024-01-17 low | −1.10% |
| 180.17 | 2024-01-05 low | −1.17% |
| 179.25 | 2024-02-02 low (102.6M-volume reversal) | −1.68% |

The **180.17–181.35** zone is a four-touch cluster (01-05, 01-17, 02-15, plus the 180.86 lower band). It is the single most important shelf on the chart. Below it, 179.25 is the last visible demand marker.

---

## 7. Actionable scenarios

**Base case (highest probability): continued drift lower into the 180.2–181.4 shelf, then an attempted bounce.** Rationale: 50 SMA falling, MACD histogram re-accelerating negative, price below all short and intermediate averages, VWMA overhead — but RSI at 36.6 and price only 0.46 ATR from the lower band argue that the *next* 2–3 points of downside are harder to harvest than the last 10.

**Bearish/continuation setup.** Sell rallies rather than breakdowns. The 185.7–186.2 confluence (10 EMA + VWMA) is the highest-quality short entry: it caps risk at ~2.5–2.9 points to a stop above 188.7 (Bollinger mid), i.e. under 1 ATR, while targeting 180.9 then 179.3. A close back above 186.2 invalidates the short thesis and the falling-VWMA regime.

**Bearish breakdown trigger.** A **close below 180.86** (lower band) with volume ≥ 65M opens 180.30 → 179.25. But note the 02-02 evidence: 179.25 already produced a 6.6-point intraday reversal on 102.6M volume. I would not short *into* that level; I would want it to break first.

**Bullish reversal requirements (do not front-run these).** I would require two of three: (1) RSI ≤ 30 **or** a bullish RSI divergence against a lower price low; (2) a close back above the 200 SMA at 183.48; (3) MACD histogram turning positive. A mean-reversion long at 180.9–181.4 with a stop below 179.90 keeps risk ≈1.0–1.5 points (0.3–0.5 ATR) — mechanically attractive, but it is **counter-trend** and should be sized at roughly half normal.

**Risk-management specifics.** ATR 3.18 → stop distances of ~1.6 (0.5 ATR) are noise-level and will fail; use ≥2.5 points (≈0.8 ATR) minimum, or ~3.9 points for a 1.25-ATR structural stop. Post-02-16, the 02-16 low at 181.67 is the nearest structural pivot. A weekly close below 180.17 would mark the first failure of the four-touch shelf and shift the intermediate trend from "correction" to "distribution phase."

**What would change my mind quickly:** a high-volume reclaim of 183.48 (200 SMA) that holds for two sessions. Because the 200 SMA is *rising*, a reclaim would put the long-term trend and price back in agreement — and would likely coincide with a MACD histogram inflection. That combination is the cleanest long signal available in this structure.

---

## 8. Summary table

| Dimension | Reading (2024-02-16) | Interpretation | Actionable use |
|---|---|---|---|
| **Close** | 182.31 | 5th straight lower close; −6.59% from 195.18 (01-23) | Short-term downtrend confirmed |
| **200 SMA** | 183.4804, rising since 01-02 (179.64→183.48) | **First close below it in 2024 window** (−0.64%) | Line in the sand; close back above = trend repair |
| **50 SMA** | 189.8614, peaked 190.9252 on 01-30, 12 straight down | Intermediate trend rolled over; 3.98% overhead | Cap on rallies; 50/200 spread +6.38, shrinking ~0.16/day |
| **10 EMA** | 185.7634, falling from 188.40 (02-12) | Fast trend down; confluence with VWMA | Short-entry zone 185.7–186.2 |
| **MACD** | −1.3616 (signal −0.7089) | Below zero since 02-01; lowest since 01-17 | Bearish regime, no crossover yet |
| **MACD hist** | −0.6527, 4th straight more-negative print | Momentum **re-accelerating** down after 02-09 pause | Not basing; favors sell-the-rally |
| **RSI** | 36.5795, from 62.62 (01-23) | Weak but >30; **no divergence** (lower low in both) | No exhaustion signal; don't buy the dip yet |
| **Bollinger lower** | 180.8590 (%B = 9.3%, width 8.3%) | Bottom decile of a wide envelope, 0.46 ATR away | Target / stop anchor; 180.86 break = continuation |
| **ATR** | 3.1800 (1.74% of price) | Orderly, moderating from 3.586 (02-02) | Use ≥2.5-pt stops; 1 ATR = 1.74% sizing unit |
| **VWMA** | 186.1809, falling from 189.7199 (02-07) | Price 2.08% below recent cost basis | Distribution confirmed; rallies meet supply |
| **Volume** | 49.75M (02-16); 65.4M (02-15) | Heaviest down day since 102.6M (02-02) | Down-volume > up-volume = distribution |
| **Support shelf** | 180.17–181.35 (4 touches) + 180.86 band | Highest-confluence demand zone | Long *only* on reversal signal; break = bearish |
| **Primary bias** | **Tactically bearish / defensive** | Up-trend intact (rising 200 SMA) but intermediate rolled | Sell 185.7–186.2; targets 180.9 / 179.3; stop >188.7 |
| **Invalidation** | Close > 183.48 then > 186.18 on volume | Long-term trend and price realign | Flip to neutral/long; death-cross risk recedes |

---

**Bottom line for AAPL:** The 2024-02-16 session delivered the first close below a *rising* 200-day SMA in the visible dataset, on the fifth consecutive down day, with a re-accelerating negative MACD histogram and price below a falling VWMA — a coherent distribution signature. The offsetting evidence is genuine but secondary: RSI at 36.6 rather than ≤30, price just 0.46 ATR above the lower Bollinger band, a marginally higher low on 02-16, and a documented 102.6M-volume absorption day at 179.25. Net: the path of least resistance is lower into the 180.2–181.4 shelf, with the best risk-adjusted expression being short-side entries into the 185.7–186.2 confluence rather than fresh breakdown chasing near 181.