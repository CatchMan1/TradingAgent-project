# GOOGL — Alphabet Inc.
## Technical Deep-Dive | Analysis Date: 2026-08-04 (Close $377.65)

**Data integrity note:** The OHLCV returned by `get_stock_data` and the `get_verified_market_snapshot` agree exactly on the 2026-08-04 row (O 368.22 / H 380.52 / L 367.50 / C 377.65 / Vol 35,705,700). All exact price and indicator values below are taken from the verified snapshot; no reconciliation was required. All splits = 1.0 (no split adjustment distortion). Cash dividends of $0.21 (2025-12-08), $0.21 (2026-03-09) and $0.22 (2026-06-08) are the only corporate actions in the window — immaterial to the technical reads (total-return index 381.02 vs. close 377.65).

---

## 1. The Dominant Narrative: A Violent Correction Inside an Intact Uptrend, Followed by a Two-Week Snap-Back

The 9-month window tells a three-act story:

**Act I — Secular advance (Nov 2025 → May 2026).** GOOGL climbed from a 2025-11-04 close of 277.54 to a closing peak of **402.62 on 2026-05-13** (+45% on close), with an intraday high of **408.61 on 2026-05-18**. Volume expanded materially during the November 2025 leg-up (85.2M on 11/24, 88.6M on 11/25) — genuine accumulation, not a drift.

**Act II — Distribution and breakdown (May → July 2026).** A textbook sequence of **lower highs** formed after the May peak: 408.61 (5/18) → 376.00 (6/16) → 375.27 (7/16) → 373.65 (7/15). Every rally was sold at progressively lower levels, while the 50-day SMA peaked at **372.80 on 2026-07-13** and rolled over. On **2026-07-23** the structure broke violently: a −7.1% single-session collapse from 342.09 to **317.69** on **69.4M shares** (~2.4× the recent 25–30M baseline), with an intraday low of 314.90. Measured peak-to-trough on closing prices, that is a **−21.1% drawdown** (402.62 → 317.69) — a technical bear market inside a longer-cycle uptrend.

**Act III — Exhaustion gap and V-recovery (July 23 → Aug 4).** The 7/23 gap-down on capitulation volume into the 314.90 low has been fully reversed. From the 7/23 close of 317.69 to today's 377.65 is **+18.87% in eight sessions**, including three consecutive acceleration days:

| Date | Close | 1-Day Change | Volume |
|---|---|---|---|
| 2026-07-30 | 333.66 | — | 30.2M |
| 2026-07-31 | 356.13 | **+6.74%** | 46.5M |
| 2026-08-03 | 373.51 | **+4.88%** | 38.7M |
| 2026-08-04 | 377.65 | **+1.11%** | 35.7M |

Critically, **the multi-month sequence of lower highs has been broken**: today's close of 377.65 and intraday high of 380.52 both exceed every July swing high (375.27 on 7/16) and the June high (376.00 on 6/16). The intermediate downtrend is structurally broken; only the May highs (402.62/408.61) remain overhead.

---

## 2. Trend Structure — Bullish Reclaim, But the Medium-Term Average Is Still Falling

| Average | Value (2026-08-04) | Close vs. Average | Direction |
|---|---|---|---|
| close_10_ema | **352.04** | +7.3% above | Turning up sharply |
| close_50_sma | **358.23** | +5.4% above | **Still declining** (−0.20 today; ~−0.91/session avg since 7/13) |
| close_200_sma | **327.55** | +15.3% above | Rising +0.63/session |
| vwma | **343.56** | +9.9% above | Turned up 7/31 after bottoming at 340.17 |

**The single most important development today is the 50-SMA reclaim.** From 2026-06-22 (close 349.68 vs. 50SMA 367.99) through 2026-07-31 (close 356.13 vs. 50SMA 358.74), GOOGL closed *below* its 50-day SMA on every single session. The first close back above it came on **2026-08-03** (373.51 vs. 358.43), confirmed by today's 377.65. That is a ~6-week downtrend being negated on the trend filter that matters most to swing traders.

**Two structural caveats, however:**

1. **The 50-SMA itself is still falling.** A price reclaim ahead of the average turning up is a *mean-reversion* signal, not yet a confirmed trend reversal. The 50SMA has decelerated (from −0.31/day on 7/31 to −0.20/day today) as higher recent closes enter the window, but it has not yet inflected. A close back below 358 would turn this into a failed reclaim.
2. **The 50/200 spread is compressing fast.** It was $53.38 on 2026-07-13 and is $30.68 today (358.23 vs. 327.55). No death cross is imminent — the 200SMA is rising and the price is 15% above it — but if price rolls back under ~350 for several weeks, the gap could close. I would not trade off this risk today; I flag it as a monitor for late Q3.

**The 10-EMA is the cleanest read of the current thrust:** it bottomed at 336.80 on 7/30 and is now 352.04, i.e. it has risen $15.24 in four sessions. Price is **$25.61 (1.99× ATR) above the 10-EMA** — statistically extended. Historically in this dataset, comparable 10-EMA extensions have preceded at least short-term consolidation (e.g., the 7/7 stretch resolved with a 4-session pullback from 367.03 to 352.51 by 7/13). Expect digestion, not straight-line continuation.

---

## 3. Momentum — A Below-Zero MACD Cross With an Unusually Powerful Histogram

| | 2026-07-30 | 2026-07-31 | 2026-08-03 | 2026-08-04 |
|---|---|---|---|---|
| macd | −8.163 | −6.143 | −3.104 | **−0.357** |
| macds (signal) | −6.746 | −6.625 | −5.921 | **−4.808** |
| macdh | −1.417 | **+0.482** | +2.817 | **+4.451** |

- **Bullish MACD crossover occurred on 2026-07-31** (histogram flipped positive).
- The **histogram at +4.451 is the largest positive reading in the entire 60-session lookback** — larger than the early-July false start peaked at (+1.83 on 7/7). Momentum is expanding, not merely turning.
- **The MACD line is still below zero (−0.357)**. The zero-line cross is the next confirmation trigger and, given a +2.75/day slope on the MACD line, it is plausibly 1–2 sessions away if price simply holds above ~373. A zero-line cross would mark the shift from "oversold bounce" to "trend re-establishment."
- **Direct historical analogue and its lesson:** the identical pattern (histogram turning positive while MACD stayed deeply negative) fired around 2026-07-01/07-02 (macdh +0.50 with MACD at −4.34, close 359.91). That rally failed at 367.03 on 7/7 and gave back everything. **What is different this time:** (a) the histogram is 2.4× larger, (b) price is *above* the 50SMA whereas on 7/7 it was below (367.03 vs. 372.08), and (c) up-volume is heavier (46.5M vs. 24.0M on 7/7). This is a stronger version of the same signal — but the July failure is a valid reason to demand confirmation rather than chase.

**RSI: 62.56 (verified, 2026-08-04)** — a 31.6-point swing in eight sessions (31.02 on 7/23 → 62.56 today). Context:
- The 7/23 reading of 31.02 was the lowest since the 33.27 print on 2026-06-26; GOOGL never reached the classic 30 oversold threshold, i.e. the selling never became statistically extreme — which arguably makes the snap-back more about short-covering than about a durable sentiment reset.
- RSI is now approaching the 70 overbought zone without being there. In trending regimes RSI can hold 60–70 for weeks. **The bearish divergence risk is what matters:** if price makes a new high above 380.52 while RSI fails to exceed 62.56, that would flag momentum exhaustion.

---

## 4. Volatility — Expanding, Wide Bands, Price Pressing the Upper Band

- **ATR: 12.87** (verified), up from 10.31 on 7/14 and 11.29 on 7/30. That is **3.41% of the $377.65 close**. Volatility is *rising into the rally* — a hallmark of real range expansion rather than a low-volatility drift higher. It also means every practical stop must be at least ~$13 wide or it will be noise-hit.
- **Bollinger (20, 2σ): middle 348.94 / upper 382.85 / lower 315.03**, bandwidth **19.4%** — extraordinarily wide, the signature of the 7/23 crash and its reversal. 
- **%B = 0.923**: price sits 92% of the way from mid-band to upper band. The close of 377.65 is **$5.20 (1.4%) below the upper band**, and today's intraday high of 380.52 came within $2.33 of it but did not tag it.
- **Interpretation:** in a volatility-expansion regime, riding the upper band is a continuation signal, not an overbought sell signal. But price has *not* closed outside the band, so this is still a "test," not a breakout. A close above **382.85** would be the mechanical breakout trigger; a rejection here leaves the 7/16–7/22 breakdown zone as unfinished business.
- The lower band at 315.03 brackets the 7/23 low of 314.90 almost exactly — a useful sanity check that the Bollinger envelope captured the true capitulation extremity.

---

## 5. Volume — Accumulation Is Real, But Thinning on the Last Two Days

- **VWMA = 343.56** vs. close 377.65 → price is **+9.9% above the volume-weighted average price of the recent window.** Two readings: (a) the marginal buyer over this window is now solidly in profit, which supports holding behavior; (b) it also means the *average* holder's cost basis is ~$34 below spot, i.e. there is a large pool of "recently profitable but recently burned" supply that can be shaken loose at the first sign of a stall.
- **Up-volume quality:** the two biggest recovery days carried real volume — 46.5M on 7/31 (+6.74%) and 38.7M on 8/3 (+4.88%) — both well above the ~25–30M recent baseline. The 7/23 sell-off on 69.4M was absorbed rather than extended, which is what you want to see.
- **The caution flag:** volume has *declined* on each of the last two sessions (46.5M → 38.7M → 35.7M) while price advanced. Two days is not a distribution call, but a third and fourth declining-volume up-day would suggest the rally is running on fumes into the 380–386 supply shelf.
- **Snapshot note:** a money-flow reading of **0.536** appears in the verified snapshot (field `mfi`). The scale is ambiguous (fractional rather than 0–100), so I am deliberately **not** building any conclusion on it. It is broadly consistent with a mid-range, non-extreme flow reading, nothing more.

---

## 6. Actionable Level Map (all levels sourced from tool OHLC rows or verified indicator values)

**Resistance**
| Level | Source |
|---|---|
| **380.52** | 2026-08-04 intraday high — immediate ceiling |
| **380.34** | 2026-05-29 close (late-May supply shelf) |
| **382.85** | Bollinger upper band (verified 8/4) — breakout trigger |
| 385.69 / 385.84 / 386.76 | 5/1 close / 4/30 high / 5/1 high — heavy May supply cluster |
| 392.82 | 5/5 intraday high |
| 397.99 / 400.80 | 5/7 and 5/8 closes |
| 402.62 / 403.70 / 408.61 | 5/13 close / 5/13 high / 5/18 high — the May peak zone |

**Support**
| Level | Source |
|---|---|
| 373.51–375.27 | 8/3 close, 7/7 high (373.16), 7/15 high (373.65), 7/16 high (375.27) — broken resistance, now first support |
| 367.50 / 366.46 | 8/4 intraday low / 7/6 close |
| **363.35** | 8/3 gap low (upward gap from 7/31 high of 358.58) |
| **358.23–358.58** | 50-SMA + 7/31 high — **the line in the sand** |
| 352.04 / 348.94 | 10-EMA / Bollinger middle |
| 343.56 / 340.00 | VWMA / 7/31 gap low (7/30 high 336.51 = lower gap edge) |
| 317.69 / 314.90 | 7/23 close and intraday low — the capitulation floor |

**Two unfilled upward gaps** now sit below price: **336.51–340.00** (7/30 high → 7/31 low) and **358.58–363.35** (7/31 high → 8/3 low). Both are legitimate partial-fill targets if the rally reverses; the upper gap (358.58–363.35) overlaps the 50-SMA and is therefore the most technically significant downside magnet.

---

## 7. Scenarios and Execution Plan

**Scenario A — Continuation (my base case, ~55% weight).**
Requirements: hold above 373.51 and, more defensively, above 367.50; MACD crosses zero; volume holds above ~30M.
- **Trigger A1 (breakout):** daily close above **382.85** (upper band) with volume ≥ 40M. Targets: 386.76 → 392.82 → 402.62.
- **Trigger A2 (pullback entry, better R:R):** buy the retest of **373–375** or the 10-EMA at **352** if the pullback is shallow and low-volume. Stop 1.5 ATR (~$19) below entry, i.e. ~356 for a 375 entry, or ~333 for a 352 entry.
- Risk: at 377.65 you are buying 2 ATR above the 10-EMA and 1.4% under a wide upper band, into a documented May supply shelf at 380–386. **Chasing here is the lowest-quality entry available.**

**Scenario B — Rejection / lower-high failure (~30% weight).**
A stall at 380.52–386.76 with declining volume would create a *new* lower high only if it fails below the 402.62 May peak — but more importantly, a rejection at the May supply shelf after an 18.9% eight-day vertical move is a classic exhaustion signature.
- **Trigger:** daily close back below **358.23** (50-SMA) — this negates the 8/3 reclaim and reopens 348.94 → 343.56 → 340.00.
- Deeper failure target: 317.69/314.90 retest, which would make the 7/23 low a double bottom if held, or a fresh breakdown if not.

**Scenario C — Choppy digestion (~15% weight).**
Most probable near-term path given 2-ATR extension: a 3–10 session range between **363 and 382**, letting the 10-EMA (352.04 and rising ~$3–5/session) and 50-SMA (358.23) catch up. This is where patient swing traders get a low-risk long at the 10-EMA rather than at today's close.

**Risk management, concretely:**
- ATR is 12.87 (3.41% of price). A 1-ATR stop is $12.87; a 2-ATR stop is $25.74. Anything tighter will be stopped by ordinary noise in this regime.
- Cash volatility sizing: to risk 1% of equity per position with a 2-ATR stop, position size = 1% ÷ 25.74 per share ≈ 0.0389% of equity per $1 of share price — i.e. roughly half the share count you would use in a 1.5% ATR name.
- **Do not add to a position on a green day below 382.85.** Both unfilled gaps below are legitimate downside magnets.

**What would change my mind (bearish):** a close below 358.23; a MACD histogram that rolls over before the MACD line crosses zero; or an RSI divergence (price > 380.52 with RSI < 62.56).
**What would confirm the bull case decisively:** MACD zero-line cross + a close above 382.85 + a weekly close above 386.76 on expanding volume.

**Event-risk caveat:** the −7.1% gap on 2026-07-23 on 69.4M shares is inconsistent with normal technical drift and implies a discrete catalyst. Nothing in the price recovery removes that event risk; the technical structure is repaired, the fundamental question that caused the gap is not addressed by any indicator here.

---

## 8. Indicator Selection Rationale

Chosen (8): **close_50_sma, close_200_sma, close_10_ema, macd, macdh, rsi, atr, vwma** — plus Bollinger band values read from the verified snapshot. Rationale: this is a **volatility-expansion regime immediately following a 21% correction and a violent V-reversal**, so the analysis must simultaneously answer four independent questions — *is the long-term trend intact* (200SMA), *has the medium-term downtrend been negated* (50SMA), *how stretched is the short-term thrust* (10EMA), *is momentum genuinely inflecting or is this another July-style fakeout* (MACD + histogram), *is sentiment extreme* (RSI), *how wide must stops be* (ATR), and *is the volume behind the rally real* (VWMA). I deliberately avoided redundancy: I used **macdh over macds** for time-series work (the histogram conveys the crossover date and expansion magnitude more directly than the signal line, whose value I take from the verified snapshot), and I omitted stochRSI (redundant with RSI in a regime where RSI's absolute level is the point), close_10_sma (redundant with the 10-EMA), and boll/boll_lb time series (band width and %B are fully captured by the verified snapshot's three band values plus ATR).

---

## 9. Summary Table

| Dimension | Reading (2026-08-04) | Signal | Key Evidence |
|---|---|---|---|
| **Long-term trend** | 200-SMA 327.55, rising; price +15.3% above | **Bullish** | 200SMA +0.63/session; no death cross; 50/200 gap $30.68 (was $53.38 on 7/13) |
| **Medium-term trend** | 50-SMA 358.23, still falling | **Improving / unconfirmed** | First close above 50SMA since 2026-06-18, on 2026-08-03; SMA itself has not inflected |
| **Short-term trend** | 10-EMA 352.04, rising $15.24 in 4 sessions | **Strongly bullish, extended** | Price = 1.99× ATR above the 10-EMA |
| **Momentum (MACD)** | MACD −0.357, signal −4.808, hist **+4.451** | **Bullish crossover, below zero** | Crossover on 7/31; hist is largest positive in 60 sessions; zero-line cross 1–2 sessions away |
| **Momentum (RSI)** | 62.56 | **Bullish, not overbought** | +31.6 pts in 8 sessions from 31.02 (7/23); no divergence yet |
| **Volatility (ATR)** | 12.87 (3.41% of price), rising | **Expanding** | Up from 10.31 (7/14); requires ≥$12.87 stops |
| **Volatility (Bollinger)** | Mid 348.94 / UB 382.85 / LB 315.03; %B 0.923 | **Testing upper band** | Bandwidth 19.4%; price $5.20 below UB; not yet a band breakout |
| **Volume** | VWMA 343.56; price +9.9% above it | **Confirming, but thinning** | 46.5M (7/31) → 38.7M (8/3) → 35.7M (8/4) on up-days |
| **Structure** | Lower-high sequence broken | **Bullish** | 8/4 high 380.52 > 375.27 (7/16) > 376.00 (6/16) — but still below 402.62 (5/13) |
| **Immediate resistance** | 380.52 / 382.85 / 386.76 | — | 8/4 high, upper band, May supply cluster |
| **Critical support** | 373.51 / 367.50 / **358.23** | — | Broken resistance, 8/4 low, 50-SMA + 7/31 high |
| **Invalidation** | Close < 358.23 | **Flip bearish** | Negates the 8/3 reclaim; targets 348.94 → 343.56 → 340.00 |
| **Net stance** | **Constructive but do not chase** | **Buy pullbacks, confirm breakouts** | 18.87% in 8 sessions = 2-ATR extension into supply; best R:R at 373–375 retest or 352 10-EMA |