# AAPL — Multi-Timeframe Technical Review (as of 30 Sep 2026)

## 0. Data verification first

The verified snapshot for **AAPL** on 2026-09-30 and the final row of the OHLCV file agree exactly: **open 330.80, high 339.50, low 330.14, close 333.02, volume 49,988,600**. No price-level discrepancy exists between the two sources.

One data-quality flag: the snapshot reports **MFI = 0.7766**, which is not on the standard 0–100 scale used by that oscillator. I have **excluded MFI entirely** from this analysis rather than re-scale or interpret it. Everything below is based on the verified OHLCV plus the eight trend/momentum/volatility/volume indicators listed in Section 1.

---

## 1. Indicator selection and why this set fits the current market

AAPL is in a **mature, low-volatility primary uptrend that is currently digesting a fresh swing high** — not a crash, not a breakout, not a range. That regime calls for a layered trend read, one momentum oscillator, one momentum-differential, one volatility measure for risk placement, and one participation measure. My eight:

| # | Indicator | Role in this specific context |
|---|---|---|
| 1 | **close_200_sma** | Strategic anchor — confirms the primary trend is intact and quantifies how stretched the stock is. |
| 2 | **close_50_sma** | The intermediate trend and the first meaningful "trend failure" line; also the pullback target if the short-term correction deepens. |
| 3 | **close_10_ema** | Detects the short-term shift that began 29 Sep; price has lost this line, which is the earliest objective evidence of consolidation. |
| 4 | **macd** | Measures the absolute momentum level — still positive and elevated, so the uptrend's engine has not reversed. |
| 5 | **macds** | Provides the crossover trigger; the MACD line has just slipped below signal, which is the cleanest "momentum has peaked" flag available. |
| 6 | **rsi** | Independent (non-EMA-based) momentum read; at 54 it shows the pullback has reset overbought pressure without approaching oversold — i.e., room in both directions. |
| 7 | **atr** | Essential here because the stock has produced two single-day declines of 6–7% in the past year; ATR sets defensible stops and position size. |
| 8 | **vwma** | The only volume-integrated price measure; it reveals that the average *volume-weighted* buyer is now above the market — a subtle distribution tell that pure price averages miss. |

Deliberately excluded: **boll_ub/boll_lb** (used only as contextual envelope from the verified snapshot, since ATR already covers risk width and the 50-SMA/10-EMA cover trend), **macdh** (redundant with macd/macds, which I use for the same crossover information), and **MFI** (invalid scale).

---

## 2. Trend structure: primary uptrend intact, intermediate still rising, short-term rolling over

**Primary trend — bullish and strengthening.**
- Close 333.02 vs **200-SMA 288.60** → price is **15.4% above** the long-term mean.
- The 200-SMA has risen every session in the 40-session window: **278.24 (3 Aug) → 288.60 (30 Sep)**, roughly +10.4 points in two months. A rising long-term anchor means the uptrend is being *built*, not merely held.
- **50-SMA (322.09) sits 33.49 points / 11.6% above the 200-SMA (288.60)**, and that spread is widening (50-SMA +0.58 over the last five sessions vs 200-SMA +1.44 — both rising, no cross risk remotely in play). This is a healthy golden-cross configuration.

**Intermediate trend — bullish, but decelerating at the margin.**
- 50-SMA: **315.15 (4 Sep) → 322.09 (30 Sep)**, a steady ~0.7/session climb. It has not flattened at all.
- The stock closed above the 50-SMA every session since **18 Aug 2026** (on 17 Aug the close was 305.59 vs a 50-SMA of 309.08; on 18 Aug the close was 310.03 vs 309.13), i.e. ~31 consecutive sessions.
- September was a net up month: **316.85 (31 Aug) → 333.02 (30 Sep) = +5.1%**.

**Short-term trend — corrective.**
- The 10-EMA turned down: **335.96 (28 Sep) → 334.77 (29 Sep) → 334.45 (30 Sep)**, and the close (333.02) is **0.43% below it**. That is the first objective short-term trend break since the September leg began.
- Swing sequence from the August low was textbook higher highs/higher lows: lows at **302.05 (13 Aug) → 309.90 (9 Sep) → 328.35 (15 Sep)** and highs at **320.28 (20 Aug) → 330.81 (3 Sep) → 338.34 (17 Sep) → 345.34 (22 Sep)**.
- That sequence cracked on **29 Sep**, when the close fell to 329.40 and the intraday low reached **328.70** — marginally under the 15 Sep swing low of 328.35. It is a *marginal* break, not a decisive one, and the 30 Sep session (low 330.14, close 333.02) reclaimed it. Treat 328.35–330.14 as a contested floor rather than a broken one.

**Longer-horizon context (all computed from concrete dated closes):**
- 2025-09-30 close 254.63 → 2026-09-30 close 333.02 = **+30.8% over twelve months**.
- 2025-12-31 close 271.86 → 333.02 = **+22.5% year-to-date**.
- 2025-09-10 intraday low 225.95 → 333.02 = **+47.4%** off the visible 12-month low.

This is a stock in a persistent uptrend, now **3.6% below its 22 Sep intraday high of 345.34** (close basis: 339.75 → 333.02 = −2.0%). Nothing in the trend data says "reversal." The evidence says "pause."

---

## 3. Momentum: the engine is still running, but it downshifted on 22–29 September

**MACD (line 4.72, signal 5.32, histogram −0.60).**
- The MACD line rose almost monotonically from **−2.68 (17 Aug) to a peak of 6.25 (22 Sep)**, then eased to **4.72**. It remains **well above zero**, which is the key point: this is a *cooling* of positive momentum, not a shift into negative momentum.
- The **MACD line crossed below its signal on 29 Sep** (histogram −0.28) and the gap widened to **−0.60** on 30 Sep. Historically in this dataset, that configuration (August) preceded a genuine correction — hist was negative from 3 Aug through 25 Aug, with MACD as low as −2.68 on 17 Aug and price at 305.59. So the signal deserves respect, but note the difference: in August the MACD line was *below zero*; now it is at +4.72. The August episode was a momentum reversal; this is a momentum stall.
- **Subtle divergence worth flagging:** the histogram peaked at **+2.03 on 3 Sep**, while price made a higher high on 22 Sep (339.75 close / 345.34 high) with a *lower* histogram high (**+1.54**). The "thrust" behind the September advance was already fading before the price peak — which is precisely why the 22 Sep top was followed by a quick two-session give-back rather than a breakout continuation.

**RSI (54.37).**
- RSI peaked at **66.88 on 22 Sep** and at **66.32 on 21 Sep** — the strongest reading of the entire leg, and **it never reached 70**. There was no classic overbought exhaustion at the high; the stock simply ran out of buyers.
- The drop to **50.88 (29 Sep)** was a 16-point, two-session reset, and 30 Sep's bounce lifted it back to **54.37**. That is a neutral, mid-range reading: no oversold cushion, no overbought headwind.
- Note the **absence of RSI divergence**: price made a higher high on 22 Sep and RSI made a higher high too (66.88 vs 63.38 on 3 Sep). The bearish evidence is confined to the MACD histogram, which makes the current pullback look more like rotation/consolidation than distribution.
- For reference, the August low was accompanied by RSI **40.2 on 12 Aug** with the close at **302.25**. That is the template for a real momentum washout — we are 14 RSI points above it.

---

## 4. Volume and participation: the weakest part of the bull case right now

**VWMA (335.34) is above price — for the second straight session.**
- VWMA has climbed relentlessly: **308.80 (21 Aug) → 335.34 (30 Sep)**.
- Price was above VWMA as recently as **28 Sep** (close 338.40 vs VWMA 332.07). The cross happened on **29 Sep** (close 329.40 vs VWMA 333.99) and persisted on 30 Sep (333.02 vs 335.34, a **0.69% shortfall**).
- Interpretation: the **average volume-weighted dollar paid by recent buyers is now ~2.32 points above the market**. That is a mild but real overhead-supply condition — recent buyers are slightly underwater, which tends to cap rallies until price reclaims that line. **Reclaiming 335.34 is the single cleanest confirmation that the pullback is over.**

**Raw volume read.**
- 30 Sep traded **49.99M shares**, versus a rough 21-session September average of **~42.8M** (computed from the daily volumes in the file, 1–30 Sep) — i.e. **~1.17× average**.
- That above-average volume came on an **up day (+1.1%) that closed 6.48 points below its high of 339.50** — the candle has a long upper wick and closed in the lower third of its range (range 330.14–339.50; close 333.02 is 31% up from the low). On above-average volume, that is a **supply/rejection signal at resistance**, not an accumulation signal.
- Constructively, the **29 Sep decline (−2.66%) occurred on 38.48M shares, below the September average** — a pullback on lighter volume is characteristic of profit-taking rather than institutional exit.
- For context on event risk, the two largest volume days in the visible window were **26 Jun 2026 (261.8M)** and **18 Sep 2026 (86.6M)**; both coincide with index/rebalance-type flow. The 31 Jul gap (prior close 333.43 → close 308.91, **−7.36%** on 132.5M) is a reminder that this name can gap through any stop.

Net: **price trend is bullish, volume confirmation is neutral-to-negative at the margin.** The two disagree, and that disagreement is the core tension in this setup.

---

## 5. Volatility and risk geometry

- **ATR(14) = 7.25**, or **2.18% of the close**. That is moderate and slightly *rising* (6.83 on 28 Sep → 7.25 on 30 Sep) after compressing through mid-September (7.11 on 27 Aug). Rising ATR into a pullback = the tape is getting less orderly.
- 30 Sep's true range was **9.36 points = 1.29× ATR** — an expansion day, driven by the 339.50 spike-and-fade.
- Bollinger envelope from the verified snapshot: **mid 331.35, upper 346.44, lower 316.27**, bandwidth **30.17 points = 9.1% of the mid**, and price is at **%B ≈ 0.56** — dead center of the upper half. Bands have been edging wider (9 Aug lower band 297.1 vs 316.3 now), consistent with a trend that is still expanding rather than coiling.
- **Practical implication:** a 1.5×ATR stop is ~10.9 points (3.3%), and a 2×ATR stop is ~14.5 points (4.4%). Anything tighter than ~5 points (0.7 ATR) will be stopped by ordinary noise — the 29 Sep range alone was 8.39 points.

---

## 6. Level map (all levels derived from dated tool output)

**Resistance (overhead):**
| Level | Source | Significance |
|---|---|---|
| **334.45** | 10-EMA (30 Sep) | First hurdle; price closed below it |
| **335.34** | VWMA (30 Sep) | Volume-weighted cost basis; bullish reclaim trigger |
| **337.00 / 338.49** | 17 Sep close / 18 Sep high | Prior consolidation ceiling |
| **339.50** | 30 Sep intraday high | Immediate rejection high — the breakout pivot |
| **341.67 / 342.99** | 25 Sep high / 28 Sep high | Lower-high cluster to clear |
| **345.34** | 22 Sep high (12-month high) | Swing high; the level that defines the uptrend |
| **346.44** | Bollinger upper band | Statistical extension; breakout confirmation zone |

**Support (downside):**
| Level | Source | Significance |
|---|---|---|
| **331.35** | Bollinger mid / 20-SMA | First line; close is only 1.67 above it |
| **330.14** | 30 Sep low | Session low, tested and held |
| **328.35–328.70** | 15 Sep low / 29 Sep low | The contested higher-low floor; a close below invalidates the short-term uptrend |
| **322.09** | 50-SMA | Trend-defining support; ~3.3% below spot |
| **316.27** | Bollinger lower band | Volatility-adjusted downside magnet |
| **309.90** | 9 Sep low | Prior swing low |
| **300.57–302.05** | 12–13 Aug lows | Major structural floor |
| **288.60** | 200-SMA | Primary trend invalidation (15.4% below spot) |

---

## 7. Actionable interpretation and trade construction

**Base case (my leaning): digestion between 328 and 340, with an upward bias while the 50-SMA rises.** The evidence for this: 50/200-SMA configuration is strongly bullish and still widening, MACD is above zero, RSI is neutral at 54, and the pullback has occurred on below-average volume (29 Sep). The evidence against immediate continuation: price below the 10-EMA *and* VWMA, MACD below signal with a widening negative histogram, and a rejection wick at 339.50 on above-average volume. Net: **trend-following bias up, entry timing poor right here.**

**Bullish trigger — wait for confirmation, don't front-run it.** A daily close **above 335.34 (VWMA)** would repair the volume-weighted damage; a close **above 339.50** would confirm the 30 Sep wick was absorption rather than distribution. Confirmation ideally comes with volume ≥ ~50M. Targets then: **345.34**, then **346.44** (upper band), with the measured move of the 328–340 range projecting toward ~**352**. Invalidation for this setup: a close back below **331.35**.

**Bearish trigger.** A daily close **below 328.35** (which would also be the first close below the 20-SMA/mid-band since 18 Aug) opens **322.09 (50-SMA)** quickly. The 50-SMA is the line in the sand: **a close below 322 would mark the first break of intermediate trend support since August** and shift the tactical bias to the **316.27 lower band** and then **309.90**.

**Risk placement and sizing (using verified ATR of 7.25):**
- Swing long entered near 333: place the stop **below the 50-SMA at ~321.00–322.00**, a risk of **~11–12 points (3.3–3.6%)**, i.e. roughly 1.5×ATR. This sits under two supports (50-SMA and the 15 Sep swing low zone) and outside normal noise.
- Aggressive breakout long (entry > 339.50): stop **below 335.30 (VWMA)**, ~4.2 points (~1.2%) is too tight for 1.29×ATR daily ranges — use **~1×ATR (7.25) → ~332.25**, or size down and accept a 2×ATR stop at ~325.
- Position sizing example on a $100,000 account risking 1% ($1,000) with an 11.5-point stop: **~87 shares**. With a 2×ATR (14.5-point) stop: **~69 shares**. Never size off a stop tighter than ~0.7 ATR given the observed 8–9 point daily ranges.
- **Trailing rule:** once price makes a new close above 345.34, trail at 1.5×ATR (currently ~10.9 points) beneath the highest close.

**What would make me wrong quickly:** a close below 328.35 on expanding volume, or a MACD line crossing below zero (it would need to fall 4.72 points — not imminent, which is why I still call this a pause).

---

## 8. Nuances, caveats, and things not to over-read

1. **The August analog is instructive but not equivalent.** MACD histogram was negative 3–25 Aug while the MACD *line* was below zero and price sat at 305.59. Today the histogram is negative but the line is +4.72. Same-looking signal, materially different regime.
2. **RSI never hit 70 on the September leg** (peak 66.88). That means there was no classic blow-off top — and also no "oversold snapback" fuel at 54. RSI is genuinely uninformative as a timing tool right now; it is a *regime* read (neutral-bullish), not a trigger.
3. **30 Sep is a month- and quarter-end session**, and 18 Sep was a quad-witching session (86.6M shares). Some of the volume patterns above are flow-driven and should not be over-interpreted as conviction.
4. **Do not read the 10 Aug gap as a dividend event.** The 0.27 ex-dividend on 2026-08-10 explains only a fraction of the 313.33 → 306.83 open-to-prior-close gap; the residual was a genuine price decline. Similarly, the 31 Jul gap (−7.36%, 132.5M shares) had no dividend attached.
5. **The VWMA signal is only two sessions old.** It is a warning, not a confirmed distribution phase. If price reclaims 335.34 within a few sessions, the signal is void.
6. **MFI in the snapshot (0.7766) is unusable** — flagged, not used.

---

## 9. Summary table

| Dimension | Reading (30 Sep 2026) | Signal | Actionable takeaway |
|---|---|---|---|
| **Verified close** | 333.02 (O 330.80 / H 339.50 / L 330.14 / V 49.99M) | — | Source of truth; matches OHLCV file |
| **Primary trend (200-SMA)** | 288.60, rising from 278.24 since 3 Aug; price +15.4% above | **Bullish** | Strategic bias long; 288.60 is the invalidation line |
| **Intermediate trend (50-SMA)** | 322.09, rising ~0.7/session; 50 > 200 by 11.6% and widening | **Bullish** | 322 is the trend-holder's stop zone |
| **Short-term trend (10-EMA)** | 334.45, turned down from 335.96 (28 Sep); price −0.43% below | **Bearish** | First evidence of consolidation |
| **MACD / signal** | 4.72 vs 5.32; histogram −0.60 (crossed 29 Sep) | **Mildly bearish** | Momentum peak was 22 Sep; line still >0, so a stall not a reversal |
| **RSI** | 54.37, from 66.88 on 22 Sep; never >70 | **Neutral** | No overbought drag, no oversold cushion; not a timing tool here |
| **VWMA** | 335.34, price −0.69% below; crossed 29 Sep | **Bearish (short-term)** | Reclaim of 335.34 = pullback over |
| **ATR** | 7.25 (2.18% of price), rising from 6.83 | **Volatility expanding** | Use ≥11-point stops; 1% risk on $100k ≈ 87 shares |
| **Bollinger (context)** | Mid 331.35 / UB 346.44 / LB 316.27; %B 0.56 | **Neutral-bullish** | 331.35 first support, 346.44 breakout zone |
| **Immediate support** | 331.35 → 330.14 → 328.35 | Contested | Close below 328.35 confirms deeper pullback |
| **Immediate resistance** | 334.45 → 335.34 → 339.50 → 345.34 | Overhead | Close above 339.50 on volume = continuation |
| **12-month performance** | +30.8% (254.63 → 333.02); YTD +22.5% | **Bullish** | Pullback is 3.6% off the 345.34 high — normal |
| **Net assessment** | Uptrend intact, short-term momentum fading, volume unconvincing | **Bullish bias / neutral timing** | Buy strength above 335.34–339.50, not weakness above 328.35; stop 321–322 |