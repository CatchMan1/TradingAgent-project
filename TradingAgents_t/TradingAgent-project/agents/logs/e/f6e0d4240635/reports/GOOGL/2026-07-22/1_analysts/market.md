# GOOGL — Multi-Timeframe Technical Report (Analysis date: 2026-07-22)

## Data integrity note

The verified snapshot for GOOGL (2026-07-22) and the `get_stock_data` OHLCV series agree exactly on the most recent row, so there is no conflict to flag:

| Field | Verified snapshot 2026-07-22 |
|---|---|
| Open | 348.16 |
| High | 349.94 |
| Low | 341.73 |
| Close | **342.09** |
| Volume | 39,334,100 |

Snapshot indicator values (the source of truth for all numbers below): 50-SMA **367.475**, 200-SMA **323.194**, 10-EMA **352.290**, MACD **–3.783**, MACD signal **–2.588**, MACD histogram **–1.195**, RSI **40.55**, Bollinger mid **354.77 / upper 372.72 / lower 336.82**, ATR **11.07**, VWMA **356.75**. (Snapshot also reports MFI = 0.342 — a fractional-scale print equal to ~34.2 on a 0–100 basis, i.e., mild net outflow. Scale is ambiguous in the feed, so I use it only as weak corroboration, not as a standalone signal.)

---

## 1. Executive read

GOOGL is in a **medium-term corrective downtrend inside a still-intact long-term uptrend**. The short-term structure deteriorated sharply between 2026-07-15 and 2026-07-22: a high-volume reversal bar on 07-16, a gap-down on 07-17, and a fresh lower close on 07-22 has left price below the 10-EMA, VWMA, 50-SMA and the Bollinger mid-line, with MACD freshly cross-over bearish and RSI falling but **not yet oversold**.

The trade-relevant asymmetry: because RSI (~40.6) and ATR (~3.2%) leave room for further downside before exhaustion, the path of least resistance is **lower/consolidative into the 337 → 330 → 323 zone**, while the 50/200-SMA spread (+13.7%) is historically stretched and the long-term trend remains up. That makes this a **"sell strength / stand aside, do not buy the dip yet"** configuration rather than a clean short-the-close or a buy-the-close.

---

## 2. Price structure: what actually happened

**Phase 1 — Structural uptrend into May.** The series rose from a 330.54 close on 2026-01-22 to a closing high of **402.62 on 2026-05-13** (window intraday high **408.61 on 2026-05-18**). Two earnings-type gaps dominate the record: a gap *down* on 2026-02-05 (prior close 333.04 → open 312.22, volume 88.2M) and a gap *up* on 2026-04-30 (prior close 349.94 → open 374.07, volume 72.0M).

**Phase 2 — Distribution and markdown, May → June.** Price drifted down from the May high to a closing low of **337.39 on 2026-06-26** (low 330.20), a **–15.0% drawdown** from the 402.62 close. Note 2026-06-26 volume of **114.7M** — 3–4× normal, consistent with a quarterly rebalance/derivative-expiry session rather than pure directional conviction.

**Phase 3 — Volume-light recovery, 06-29 → 07-15.** Price rallied from 337.39 to **370.92 on 2026-07-15**, a **+9.9%** bounce. Critically, this advance was on *contracting* volume: 34213900 → 35237200 → 26736400 → 25974800 → 26915800 → 24045600 → 22094800 → 24729100 → 18146100 → **15901700 (07-13, lowest in the entire window)** → 18259400 → 28284600. A rally on shrinking participation is a low-quality rally.

**Phase 4 — Failed breakout / breakdown, 07-16 → 07-22.** The 07-16 session is the key bar: it **opened 373.06, printed a high of 375.27, then closed 354.46** — an outside/engulfing reversal spanning ~6.1% of price on **41.16M** volume. 07-17 gapped down (open 346.00 vs prior close 354.46, low 341.36, close 346.77). Then 351.99 (07-20), 347.15 (07-21), and **342.09 today on 39.33M volume** — the second-highest volume since the reversal bar.

Net: **–7.8% from the 07-15 close in five sessions**, and **–15.0% from the May closing high**. Today's low (341.73) is essentially a retest of the 07-17 low (341.36); the close (342.09) is only 0.36 above that low, i.e., the market closed the session sitting **on** the July low rather than bouncing off it.

Position in the window range: **(342.09 – 273.50) / (402.62 – 273.50) = 53%** — dead center, so neither a value nor a momentum extreme on a longer-horizon basis.

---

## 3. Indicator-by-indicator analysis

### 3.1 Trend — 50-SMA (367.48) and 200-SMA (323.19)
- Price is **–6.91% below the 50-SMA** and **+5.85% above the 200-SMA**. The long-term trend is unambiguously intact (200-SMA has risen monotonically every session in the record: 321.66 on 07-17 → 323.19 on 07-22, ~+0.51/session).
- The 50-SMA has **rolled over**: it peaked at **372.797 on 2026-07-13** and has fallen for **seven consecutive sessions** to 367.475. That is a fresh, dated slope change — the first sustained decline in the 50-SMA in the entire sample.
- The **50/200 spread is 44.28 points = 13.70% of the 200-SMA**. Extended readings like this are a *mean-reversion warning*, not a timing signal: the most probable resolution is either time (200-SMA grinds up toward price) or price (price grinds down toward the 50-SMA). Today, price is doing the work.

### 3.2 Short-term momentum — 10-EMA (352.29)
- Price is **–2.90% below the 10-EMA**. The 10-EMA rolled from a local peak of **360.55 on 07-15** to 352.29 today, and is now **falling faster than the 50-SMA** — the classic short-term-over-medium-term underperformance signature.
- The 10-EMA (352.29) sits **below** the 50-SMA (367.48) by 15.19 points. The short-term average being below the medium-term average with price below both = clean bearish stack.

### 3.3 Momentum — MACD (–3.783) / Signal (–2.588) / Histogram (–1.195)
- The MACD line is **negative and re-accelerating lower**. Sequence: –0.782 (07-15, the local best) → –1.188 → –2.105 → –2.383 → –2.961 → **–3.783**.
- The MACD line made a **lower high** (–0.78 on 07-15 vs the June trough of **–7.35 on 06-26**) and has now turned down again. Failure of the MACD to reclaim zero on the June–July bounce is the single clearest confirmation that the bounce was corrective, not impulsive.
- **Bearish crossover is dated**: the histogram was still positive through 07-16 (+0.86 as measured by MACD minus signal), flipped to **–0.049 on 2026-07-17**, and has widened to **–1.195 today**. The histogram is expanding negatively — momentum is *accelerating* to the downside, not merely negative.

### 3.4 Momentum — RSI (40.55)
- RSI has collapsed from **56.87 on 07-15 to 40.55 today**, a 16.3-point drop in five sessions.
- **Not oversold.** The June capitulation low printed **33.27 on 06-26**, so there is ~7 points of headroom before RSI revisits its own recent floor. Historically in this sample, RSI in the 33–40 band has been the zone where the June low formed — meaning current momentum is *approaching*, not *at*, a washout.
- **No bullish divergence exists.** Price and RSI are in agreement (both lower vs 07-17: close 346.77 → 342.09; RSI 42.23 → 40.55). Similarly vs the 06-26 low (close 337.39 / RSI 33.27), both are higher today — again confirming, not diverging. Do not build a bottom thesis on divergence that the data does not contain.

### 3.5 Volume — VWMA (356.75)
- Price is **–4.11% below the volume-weighted average price**. This is the most informative single number in the report: the *dollar-weighted average recent participant is underwater*. VWMA has also turned down (peak 358.74 on 07-20 → 356.75 today), so the volume-weighted cost basis is now supply overhead, not support.
- The volume signature around the reversal is textbook distribution: **rallies on 15.9M–28.3M, declines on 41.2M and 39.3M**. Today's 39.33M is roughly 1.3× the ~30.3M average of the last 21 sessions excluding the 06-26 rebalance spike — above-average volume on a down day that closed at the session low quartile.

### 3.6 Volatility — ATR (11.07)
- ATR = **11.07 = 3.24% of price**, up from a local trough of **10.31 on 07-14**. Volatility is *expanding* into the decline — a hallmark of directional (not choppy) downside.
- Bollinger envelope (snapshot): mid 354.77, upper 372.72, lower 336.82; **width = 10.1% of the mid-band**. Price sits in the **lower third**, 5.27 (1.54%) above the lower band and 30.63 (8.9%) below the upper band. Bands are not yet "squeezed-then-expanded" enough to imply a mechanical snapback; riding toward the lower band remains a live path.

---

## 4. Levels that matter (all from tool output)

**Resistance (overhead, in order):**
1. **349.94** — today's high; also the 07-21 close was 347.15, so 347–350 is the immediate supply shelf.
2. **352.29** — 10-EMA (first momentum gate).
3. **354.46–354.77** — 07-16 close and Bollinger mid-band.
4. **356.75** — VWMA (the "all-clear" line for a genuine trend repair).
5. **367.48** — 50-SMA.
6. **372.72–375.27** — Bollinger upper band and the 07-16 reversal high.

**Support (below, in order):**
1. **341.36–341.73** — the 07-17 low and today's low, a tested double trough.
2. **336.82** — Bollinger lower band.
3. **330.20–337.39** — the 06-26 low and closing low.
4. **323.19** — 200-SMA.

Note that resistance clusters are tight and stacked (349.9 / 352.3 / 354.8 / 356.8) while support is comparatively sparse between 336.8 and 323.2. That asymmetry favors continuation over reversal on a first test.

---

## 5. Scenarios with explicit triggers

**Base case (bearish continuation / grind — highest probability given MACD histogram expansion + volume pattern):** A close below **341.36** opens 336.8 (lower band) and then the 330.2–337.4 June shelf. ATR-projected 5-session downside at 1× ATR from 342.09 ≈ **331.5**, which conveniently coincides with the June low zone. *Confirmation required:* a daily close under 341.36 with volume ≥ ~35M.

**Alternate case (mean-reversion bounce — credible but unconfirmed):** Because the 50/200 spread is 13.7% extended and the 200-SMA is rising ~0.5/day, a relief rally into **349.9–356.8** is entirely plausible without any trend change. *Do not treat it as a buy signal* unless GOOGL closes **above 356.75 (VWMA)** with the MACD histogram turning positive and RSI back above ~48. A rally that stalls at the 10-EMA/354.8 mid-band is a **shorting opportunity**, not a breakout.

**Bull invalidation (trend repair):** Two consecutive closes > **367.48 (50-SMA)** with the histogram positive and expanding would neutralize the corrective structure. Given the 50-SMA is falling and price is 6.9% away, this is not a near-term prospect.

---

## 6. Actionable plan

**If short / reducing long exposure (aligned with evidence):**
- Entry zone: **349.9–354.8** (today's high → 07-16 close / mid-band), i.e., sell strength, not breakdowns.
- Stop: **359.5–361** (≈1.0–1.1× ATR above entry; also above the 07-16 close-to-07-15 gap-fill area). Hard stop above **367.5** for swing positions.
- Targets: **336.8** (lower band), then **330.2–331.5** (June low / ATR projection). Trail stops at 1× ATR (11.07).
- Position sizing: with ATR at 3.24% of price, a 1× ATR stop equals a 3.24% adverse move — size positions so that a full stop-out costs a fixed fraction of capital; do *not* apply the ~2% sizing used in low-volatility regimes.

**If flat (the defensible default):**
- Wait. Neither an oversold long nor a fresh-momentum short is well-priced at 342.09. The clean short setup is a failed rally at 352–357; the clean long setup is a volume-confirmed reclaim of 356.75.
- Re-evaluate on: (a) a close below **341.36**, or (b) a close above **356.75**.

**If long (carrying risk):**
- The 07-16 outside-reversal bar and the VWMA breach are objective de-risking signals. A stop at **<341.30** is the technically honest level; holding through it means accepting a move to the 330s/200-SMA.

**Event risk:** The two largest single-session gaps in the record (2026-02-05, 2026-04-30) coincide with quarterly reporting cadence, and 2026-07-22 falls inside the late-July mega-cap reporting window. A binary gap risk of ~6–7% magnitude (as observed on 02-05 and 04-30) is a live hazard; ATR-based stops have historically been *insufficient* on those two dates. This is an inference from gap behavior, not a confirmed event date.

---

## 7. Why these 8 indicators

| Indicator | Role in this specific setup |
|---|---|
| `close_200_sma` | Establishes that the *primary* trend is still up — prevents over-bearish framing |
| `close_50_sma` | Captures the dated, fresh slope rollover (peak 07-13) — the medium-term turn |
| `close_10_ema` | Fastest read on the 07-16→07-22 momentum break and the first resistance gate |
| `macd` | Identifies the failed reflation (lower high –0.78 vs –7.35) |
| `macds` | Dates the bearish crossover precisely at 2026-07-17 |
| `rsi` | Quantifies remaining downside room (40.55 vs 33.27 floor) and confirms *no* divergence |
| `atr` | Converts volatility into stops, targets and position size (11.07 / 3.24%) |
| `vwma` | Volume-weights the price action, exposing the low-volume rally + high-volume decline and the underwater cost basis at 356.75 |

Deliberately excluded: Bollinger upper/lower bands as *primary* signals (used only as an ancillary envelope — they add little beyond ATR + RSI here), and any redundant oscillator (a stochastic variant would duplicate RSI's information).

---

## 8. Key points summary

| Dimension | Reading (2026-07-22) | Interpretation | Actionable level |
|---|---|---|---|
| Close | 342.09 (O 348.16 / H 349.94 / L 341.73) | Closed on the July low, no bounce | Below 341.36 = continuation |
| 50-SMA | 367.475 (peaked 372.80 on 07-13) | Medium-term trend has rolled over | Resistance at 367.5 |
| 200-SMA | 323.194, rising ~0.5/day | Primary uptrend intact | Major support 323 |
| 10-EMA | 352.290, falling | Short-term bearish | First resistance 352.3 |
| MACD / Signal / Hist | –3.783 / –2.588 / –1.195 | Bearish cross 07-17, histogram *widening* | Momentum still deteriorating |
| RSI | 40.55 (56.87 on 07-15) | Weak, **not** oversold; no divergence | Floor reference 33.3 |
| VWMA | 356.753 (price –4.1%) | Volume-weighted buyer underwater | Trend repair needs >356.8 |
| Bollinger | 354.77 / 372.72 / 336.82 | Price in lower third; 1.5% above lower band | Downside magnet 336.8 |
| ATR | 11.07 (3.24% of price) | Volatility expanding into decline | 1-ATR stop ≈ 11 pts |
| Volume | 39.33M vs ~30.3M recent avg ex-spike | Distribution: up on light, down on heavy | Confirm breaks with ≥35M |
| 50/200 spread | 44.28 pts = **+13.70%** | Historically stretched | Mean-reversion risk, not timing |
| Drawdown | –7.8% in 5 sessions; –15.0% from 402.62 (05-13) | Corrective, not yet capitulative | — |
| Stance | **Neutral-to-bearish; sell rallies, don't buy dips** | Await 341.36 break or 356.75 reclaim | — |