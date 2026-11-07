# AAPL — Multi-Timeframe Technical Assessment (as of 2024-02-12 close)

**Ticker:** AAPL (Apple Inc.) · **Latest verified session:** 2024-02-12 · **Close:** 187.15

---

## 1. Verified Data Anchor

All figures below come from `get_verified_market_snapshot` (2024-02-12). I cross-checked every indicator against the individual `get_indicators` series and **found no discrepancies** — snapshot values match the series to the decimal.

| Item | Value (2024-02-12) |
|---|---|
| Open / High / Low / Close | 188.42 / 188.67 / 186.79 / **187.15** |
| Volume | 41,781,900 |
| close_10_ema | 188.395 |
| close_50_sma | 190.435 |
| close_200_sma | 183.185 |
| macd / macds / macdh | −0.3587 / −0.2213 / **−0.1374** |
| rsi (14) | 45.93 |
| boll / boll_ub / boll_lb | 189.212 / 196.544 / 181.881 |
| atr | 3.156 |
| vwma | 188.789 |

*(The snapshot also carries an MFI value of 0.42773; its 0–1 scaling is ambiguous, so I deliberately excluded money-flow indicators from the signal set.)*

---

## 2. Executive Summary — Regime: **Bullish Primary Trend / Weakening Medium-Term Trend / Neutral-Range Short Term**

AAPL is in a **structurally intact but decelerating uptrend**. The long-term benchmark is still rising and price remains above it, yet every faster measure — 10-EMA, 50-SMA, VWMA, MACD — sits *above* the current price, and the 50-SMA has begun to roll over for the first time in the visible window. That combination (price trapped between a rising 200-SMA far below and a cluster of falling short-term averages immediately overhead) is the textbook definition of a **consolidation/pullback inside a bull trend**, not a trend reversal and not a fresh breakout.

**Net stance:** Tactically neutral-to-slightly-bearish; strategically still constructive. Two-sided range tactics are favored over directional conviction until either the 190.4–191.1 overhead cluster is reclaimed or 183.2 (200-SMA) is decisively broken.

---

## 3. Trend Structure

### 3.1 Long-term (close_200_sma = 183.185): unambiguously up
The 200-SMA has risen **monotonically every single session** in the sampled period: 172.95 on 2023-11-14 → 183.18 on 2024-02-12, roughly **+10.2 points (+5.9%) in about three months**, a slope near +0.13/day that is *accelerating slightly* (it added 0.117 in the last session alone, versus ~0.11/day in late November).

- Close 187.15 is **+2.16% above** the 200-SMA.
- Critically, the 200-SMA is still ~4.0 points *below* the 2024-01-31 low (184.35) and ~3.9 points below the 2024-02-02 intraday low (179.25). **Price has not tested the 200-SMA at any point in the sampled window.** The uptrend is intact but its final line of defense is untested and therefore unproven at current volatility.

### 3.2 Medium-term (close_50_sma = 190.435): rolling over
This is the most important negative observation in the dataset. The 50-SMA rose from **176.34 (2023-11-14) to a peak of 190.925 on 2024-01-30**, then fell on nine consecutive sessions to 190.435. The decline is small (−0.49, −0.26%) but the *inflection* is real and coincides exactly with price loss of that level.

- Close 187.15 is **−1.73% below** the 50-SMA.
- Price has closed **below the 50-SMA every session since 2024-01-30** (nine sessions), after having been *above* it from 2024-01-19 through 2024-01-26 (closes 191.56, 193.89, 195.18, 194.50, 194.17 versus a then-rising 50-SMA in the 189.8–190.8 zone).
- **50-SMA minus 200-SMA** has compressed from **+8.73 (2024-01-30)** to **+7.25 (2024-02-12)**. The bullish separation remains very wide (7.25 points ≈ 4% of price), so this is a *narrowing* of a strong trend, not a threat of a bearish crossover. But a narrowing spread driven by a falling fast average and a rising slow average means the medium-term impulse is being absorbed.

### 3.3 Short-term (close_10_ema = 188.395): bearish alignment, flattening
The 10-EMA has been effectively **flat-to-down since 2024-01-26 (191.33)**, printing 188.40 on 2024-02-12. Price closed below it on 2024-02-08 (188.32 vs 188.63) and again on 2024-02-12 (187.15 vs 188.40), while marginally exceeding it on 2024-02-09 (188.85 vs 188.67) — a whipsaw pattern that confirms the absence of short-term directional control.

Note the ordering: **10-EMA (188.40) < 50-SMA (190.44)**, i.e., short-term averages are now *below* the medium-term average. That is a bearish short-term stack, though the 10-EMA is still 5.2 points above the 200-SMA, so no medium/long-term bearish stack exists.

---

## 4. Momentum

### 4.1 MACD: second bearish crossover in six weeks, histogram re-widening
MACD's path is a study in failed recovery:
- **+3.73 (2023-12-14)** → **−1.93 (2024-01-17)** — a major momentum collapse.
- Recovery to **+0.95 (2024-01-26)** and **+0.944 (2024-01-29)** — this upside attempt **stalled below the prior peak by a wide margin** (0.95 vs 3.73).
- **Bearish crossover on 2024-01-30/31**: MACD was still above signal on 2024-01-30 (+0.633 vs +0.270) but crossed below on 2024-01-31 (+0.091 vs +0.235). It has remained below signal for nine consecutive sessions.
- Latest: MACD **−0.359**, signal **−0.221**, histogram **−0.137**.

The histogram is the nuanced part. It bottomed at **−0.503 on 2024-02-02**, then contracted steadily to **−0.065 on 2024-02-09**, before **re-widening to −0.137 on 2024-02-12**. So: downside momentum was decaying through the week of Feb 5–9 (constructive), then **re-accelerated on the final session** (destructive). The MACD line itself also turned down again (from −0.2516 on Feb 9 to −0.3587), meaning the "bear cross losing force" thesis was rejected at the last bar. This is a genuinely two-sided reading and argues against aggressive positioning either way.

### 4.2 RSI: mid-range, no edge, no divergence
RSI at **45.93** is squarely neutral — below 50, above 30. The path is informative:
- **28.79 on 2024-01-05** (oversold — and the Jan 5 close of 181.18 was the lowest close since 2023-11-01).
- Rally to **62.62 on 2024-01-23** — RSI *failed to reach 70* on a move where price tagged 195.75. That is a lower-high in momentum versus the 69.69 RSI print on 2023-12-14 when price was 198.11, i.e. mildly non-confirming but **not a clean, textbook divergence** (different cycle highs, so I will not over-claim it).
- Rolled back to **39.60 (2024-01-31)** then a bounce to 50.81 (Feb 7) and now 45.93.

Key point: RSI has *not* re-entered oversold despite price sitting 5.5% below its December high. There is **room for further downside without a mechanical mean-reversion bid**, which weakens the "buy the dip now" case.

---

## 5. Volatility and Band Positioning

### 5.1 ATR (3.156, = 1.69% of price): elevated, and that matters for risk
ATR fell to a local low of **2.567 on 2023-12-28**, jumped to **3.586 on 2024-02-02** (earnings-gap session), and has since decayed modestly to **3.156**. It remains **~23% above the late-December trough**. Consequences:

- Normal daily noise is roughly ±3.16 points. **A one-day move of 2–3 points carries no information** in this regime; only closes outside ~±3.2 points from the prior close should be treated as signals.
- A 2-ATR stop is **6.3 points**. On a long entered at the 2024-02-12 close of 187.15, a 2-ATR stop at ~180.8 would sit **below the 200-SMA and below the 2024-02-02 low (179.25)** — too wide and structurally misplaced. Risk therefore must be defined by *structure* (see §7), with ATR used to **size** the position rather than place the stop.

### 5.2 Bollinger (20,2): lower half of a moderately narrow band
- Midline **189.212**, upper **196.544**, lower **181.881**; total width **14.66 = 7.75% of the midline** — a moderately compressed envelope consistent with the sideways action of Feb 5–12.
- Close 187.15 sits at roughly **36% of the band width** (i.e., in the lower half, below the midline).
- The lower band at 181.88 is only ~2.6 points below the 200-SMA (183.18) — **support is unusually concentrated in the 181.9–183.2 zone**, which makes that zone either a high-probability bounce area or, if it fails, the trigger for a genuine trend change.

Note the 2024-02-02 session: **open 179.86 vs prior close 186.86 (−3.75%), low 179.25 (−4.07%)**, closing back at 185.85 (−0.54%). That is a large-volume (102.55M) **rejection wick** — supply was absorbed intraday. I will not claim it "bounced off support," as the band values for that date are not in the verified set, but the open/low/close sequence is documented and is the single most constructive bar in the recent tape.

---

## 6. Volume and Participation

### 6.1 VWMA (188.789) above price — sellers have the marginal edge
VWMA rose from **185.25 (2024-01-18)** to a local peak of **189.72 (2024-02-07)**, then eased to **188.789**. Price at 187.15 is **−0.87% below VWMA**.

Interpretation: the volume-weighted average transaction price of the recent period is **above** the current price, meaning **recent buyers are, in aggregate, underwater** and the marginal seller is transacting at a discount. VWMA above price = mild distribution. It has also turned down for three sessions (189.72 → 189.56 → 189.19 → 188.79), so volume-weighted flow is rolling with price rather than leading it.

### 6.2 Volume is drying up on the drift lower
From the provided CSV, the **20-session average volume (2024-01-16 → 2024-02-12) is ≈56.8M shares**. The 2024-02-12 print of **41.78M is ~74% of that average**. The pattern of the last six sessions — 69.7M (Feb 5), 43.5M, 53.4M, 41.0M, 45.2M, 41.8M — shows **declining participation into declining price**. That is *not* panic distribution; it is apathy/low-conviction drift, which typically resolves with a catalyst rather than a cascade.

### 6.3 Event distortion
The **2024-02-02** session (102.55M shares, ~1.8× the 20-day average, 8-point intraday range) is the dominant volume event of the window and created a reference low at 179.25 that any bear case must contend with.

---

## 7. Price-Level Map (all levels derived from verified rows)

**Resistance (overhead cluster, tightly stacked):**
1. **188.40–188.79** — 10-EMA (188.395) and VWMA (188.789). First hurdle; price failed here on Feb 12.
2. **189.21–189.99** — Bollinger midline (189.212) and the 2024-02-09 high (189.99).
3. **190.44–191.05** — 50-SMA (190.435) and the 2024-02-07 high (191.05). **The decisive zone.**
4. **191.95–192.20** — 2024-01-19 high (191.95) and 2024-01-29 high (192.20).
5. **195.18–196.54** — 2024-01-22 (195.33) / 01-23 (195.75) / 01-24 (196.38) highs, plus Bollinger upper (196.544). Major supply shelf.
6. **198.11–199.62** — 2023-12-14 close/high; the top of the sampled range (−5.5% to −6.3% from spot).

**Support:**
1. **186.79–187.35** — 2024-02-12 low (186.79) and 2024-02-08 low (187.35). Immediate pivot.
2. **185.84–185.85** — 2024-02-05 low (185.84) and 2024-02-02 close (185.85).
3. **184.35** — 2024-01-31 low. The last higher-low before the earnings gap.
4. **183.18–183.63** — **200-SMA (183.185)** + 2024-01-16 close/low area (183.63 / 180.93). The line in the sand.
5. **181.88–182.00** — Bollinger lower (181.881).
6. **179.25** — 2024-02-02 low; the tail-risk level.

---

## 8. Actionable Plan (Conditional, Trigger-Based)

**Bias: Neutral. Treat 186.79–191.05 as the operating box.**

**(A) Primary — range-fade the overhead stack (preferred on evidence)**
Sell rallies into **189.2–190.4**. Rationale: price, 10-EMA, VWMA, and 50-SMA all cap this zone; MACD is below signal and re-widening; RSI 45.9 with no oversold cushion.
- Stop: daily close **above 191.10** (above the 2024-02-07 high).
- Targets: **186.80** (Feb 12 low) → **184.40** (Jan 31 low) → partial at **183.20** (200-SMA).
- Risk ≈ 1.0–1.9 points to stop from a 190.0 entry; reward 3.2–6.6 points — favorable R:R only if you enter at the *top* of the zone, so this is an entry-discipline trade, not a set-and-forget one.

**(B) Secondary — tactical long at structural support**
Buy **184.40–186.80**, ideally on a positive-reversal bar with volume ≥ 50M.
- Stop: close **below 182.90** (below Bollinger lower 181.88 is too loose; below the 200-SMA at 183.19 is the logical invalidation). Use 1.5×ATR (≈4.7) sizing.
- Targets: **188.80** (VWMA) → **190.44** (50-SMA).
- Do **not** hold this long through a decisive close below 183.18 — see (D).

**(C) Breakout long (momentum re-ignition)**
Requires **daily close > 190.55** *and* MACD crossing back above its signal line *and* RSI > 55. Two of three is not enough given the Jan 26–29 false start.
- Targets: **195.20** → **196.54** (Bollinger upper). Stop **187.40**.

**(D) Breakdown (regime change)**
A **daily close below 183.18** would be the first loss of the 200-SMA in the entire sampled window and would convert the primary trend from bullish to neutral/negative. Given the 50-SMA's nine-session decline and MACD below signal, this is a *live* scenario, not a tail.
- Downside sequence: **181.88** (Bollinger lower) → **179.25** (Feb 2 low) → measured-move extension below that.
- Stop on any existing long: hard exit on a close below 183.18; use 2×ATR (6.3) as the minimum expected travel, not as a stop distance.

**Position sizing:** At ATR 3.156 (1.69% of price), size **~25–30% smaller than a low-volatility regime**. If risking 1% of equity per trade with a structural stop 4.0 points away, position = 0.25% of equity per point of risk.

---

## 9. Why These Eight Indicators

| Indicator | Role in this specific setup | Why not redundant |
|---|---|---|
| **close_200_sma** | Defines the primary regime and the 183.19 invalidation line | Slow enough to be the "is the bull market intact?" arbiter |
| **close_50_sma** | Captures the *inflection* — peaked 2024-01-30, now falling; defines overhead resistance at 190.44 | The single most informative negative datapoint; not visible in the 200-SMA |
| **close_10_ema** | Short-term control/entry timing, shows the 10<50 bearish stack | Fast enough to flag whipsaw at 188.4 |
| **macd** | Measures whether the Jan recovery was real (it wasn't — stalled at +0.95 vs prior +3.73) | Trend-change detector on the intermediate horizon |
| **macds** | Provides the crossover event (2024-01-31) and a timing anchor | MACD line alone gives no signal event |
| **rsi** | Confirms no oversold cushion at 45.9 and the failed push to 70 | Divergent information type (rate-of-change of gains vs losses) versus EMA-difference |
| **atr** | Volatility-scaled risk: 1.69% daily noise, 2-ATR = 6.3 → structural stops required | Independent of direction; governs sizing, not signal |
| **vwma** | Volume-weighted confirmation: price *below* VWMA (188.79) = distribution | Uniquely blends price with volume; not duplicated by any average |

*Deliberately excluded:* `boll_ub`/`boll_lb` as separate selections (levels read directly from the verified snapshot; adding two more band lines would consume slots for one signal), `macdh` (fully determined by macd − macds, which I hold directly), and `stochrsi` (redundant with rsi per instructions).

---

## 10. What Would Change This View

**Toward bullish (upgrade to constructive):**
- A close above **190.55** (50-SMA) with MACD histogram turning positive, and volume > ~57M (20-day average). Would re-open 195.2–196.5.
- The MACD histogram *failing* to widen further and rolling back toward zero while price holds above 186.79 — a "bear cross exhausting" pattern, which was in progress through Feb 9 and was retested (unfavourably) on Feb 12.
- VWMA flattening and price reclaiming 188.79, flipping the volume-weighted crowd back to profit.

**Toward bearish (downgrade to defensive):**
- Close below **186.79** confirms the descending-highs structure (191.05 Feb 7 → 188.67 Feb 12) and puts 184.35 in play.
- Close below **183.18** breaks the 200-SMA — primary trend invalidated; the 50/200 spread would compress under 7.0 and continue contracting.
- MACD falling below its **2024-01-17 trough (−1.926)** would signal the corrective leg is larger than the January shakeout.

**Key caveat:** All conclusions are drawn from the visible frozen rows through 2024-02-12 only. No forward price data was consulted, and no claim is made about band behavior, support bounces, or percentage moves on dates outside the verified series.

---

## 11. Summary Table

| Dimension | Reading (2024-02-12) | Evidence | Implication |
|---|---|---|---|
| **Primary trend** | Bullish, intact | 200-SMA 183.185, rising every session since 2023-11-14 (172.95 → 183.185); close +2.16% above | Do not short the trend outright; downside is a pullback until 183.18 fails |
| **Medium-term trend** | Weakening | 50-SMA peaked 190.925 (2024-01-30), fell 9 straight sessions to 190.435; close −1.73% below; 9 closes below since Jan 30 | Overhead resistance; rallies are sellable into 190.4 |
| **Short-term structure** | Neutral, choppy | 10-EMA 188.395 < 50-SMA 190.435; price below 10-EMA; box 186.79–191.05 | Two-sided range tactics; avoid chasing |
| **Momentum (MACD)** | Bearish, re-weakening | MACD −0.359 < signal −0.221; bearish cross 2024-01-31; hist −0.503 (Feb 2) → −0.065 (Feb 9) → −0.137 (Feb 12) | Recovery attempt rejected; no long until histogram turns up |
| **Momentum (RSI)** | Neutral, no cushion | 45.93; low 28.79 (Jan 5), high 62.62 (Jan 23), failed to reach 70 | Room for further chop/drift; no oversold bid |
| **Volatility** | Elevated | ATR 3.156 (1.69% of price); trough 2.567 (Dec 28); peak 3.586 (Feb 2) | Size down ~25–30%; 2-ATR = 6.3 points of "noise" |
| **Bands** | Lower half of moderate band | Mid 189.212 / UB 196.544 / LB 181.881; width 7.75% of mid; price at ~36% of width | Mean-reversion target is 189.21; band low 181.88 clusters with 200-SMA |
| **Volume/flow** | Mild distribution | VWMA 188.789 > close 187.15 (−0.87%); VWMA turning down 3 sessions; Feb 12 volume 41.8M ≈ 74% of ~56.8M 20-day avg | Sellers have marginal edge but conviction is low — catalyst-driven resolution |
| **Key resistance** | 188.40–188.79 → 189.21–190.44 → 191.05 → 196.54 | 10-EMA/VWMA, Boll mid, 50-SMA, Feb 7 high, Boll UB | Fade zone: 189.2–190.4 with stop >191.10 |
| **Key support** | 186.79–187.35 → 185.84 → 184.35 → **183.18 (200-SMA)** → 181.88 → 179.25 | Feb 12/Feb 8 lows, Feb 5 low, Jan 31 low, 200-SMA, Boll LB, Feb 2 low | Buy zone 184.4–186.8; hard invalidation <183.18 |
| **Trade stance** | **Neutral (range)** | Convergent evidence above | Fade 189.2–190.4 → 186.8/184.4; long 184.4–186.8 with stop <182.9; breakout only >190.55 on volume |
| **Regime-change triggers** | >190.55 w/ MACD up & vol >57M = bullish; <183.18 = trend break | Verified levels | Predetermine actions before they trigger |