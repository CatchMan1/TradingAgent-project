# AMZN — Technical & Trend Report as of 2024-01-18

## 1. Data integrity note (read first)

The `get_stock_data` CSV and `get_verified_market_snapshot` agree **exactly** for 2024-01-18 — no discrepancy to flag:

| Field | Verified value |
|---|---|
| Open | 152.77 |
| High | 153.78 |
| Low | 151.82 |
| Close | **153.50** |
| Volume | 37,850,200 |

Every indicator value quoted below (RSI 57.33, MACD 1.5446 / signal 1.5566, 10 EMA 152.26, 50 SMA 148.12, 200 SMA 130.82, ATR 2.9829, VWMA 150.88, Bollinger 145.92 / 151.79 / 157.66) was cross-checked against the snapshot and matches the indicator tool output to the decimal. The snapshot's `mfi` field reads 0.4426 (a normalized scale, not the conventional 0–100), so it is excluded from the analysis.

## 2. Bottom line

AMZN is in a **mature, intact primary uptrend that has entered a consolidation/deceleration phase near its highs**. Price is above every moving average in a perfectly stacked bullish sequence, the 50/200 SMA golden cross is wide and widening, and the pullback off the January high has been orderly and low-volume. However, momentum is measurably weaker than price: both MACD and RSI printed **lower peaks at higher price highs** between mid-December and 11 January, and the MACD line has rolled flat on the signal line with a marginally negative histogram. This is a *trend-intact but momentum-cooling* setup — a "buy the pullback, don't chase the breakout" tape rather than a fresh-trend-entry tape.

## 3. Trend architecture — fully stacked and bullish

Current ordering of price vs. averages on 2024-01-18:

**Close 153.50 > 10 EMA 152.26 > Bollinger mid 151.79 > VWMA 150.88 > 50 SMA 148.12 > 200 SMA 130.82**

- **200 SMA (130.82)** has risen every single session in the window, from 120.58 on 2023-11-20 to 130.82 now — the long-term trend benchmark is sloping up, not flat. Price sits **~17.3% above it**, which is extended but typical of a healthy stage-2 advance, not evidence of a top by itself.
- **50 SMA (148.12)** has climbed from 133.78 (2023-11-20) to 148.12, gaining roughly $0.30/day in the last week. The 50/200 spread is **$17.30 (~13.2% of the 200 SMA)** — a wide, well-established golden cross. The crossover is long since confirmed; it is no longer a "signal," it is structural context.
- **10 EMA (152.26)** is the operative short-term line. Price closed above it on 01-18 after closing *below* it on 01-16 (153.16 vs EMA 152.04) and 01-17 (151.71 vs EMA 151.98). The 01-18 close is a **short-term reclaim**, which is the first constructive micro-signal in three sessions.
- The 10 EMA itself flattened from 152.05 (01-16) → 151.98 (01-17) → 152.26 (01-18). It is basing, not curling down — consistent with a pause inside an uptrend.

**Price path context (all tool-verified):** the October 2023 low close was **119.57 (2023-10-26)** with an intraday low of 118.35. From there to the **157.17 intraday high on 2024-01-11** is a large advance, and the more recent, more relevant structure is a **~one-month high-level range between roughly 149.9 and 157.2**. This is a distribution-vs.-reaccumulation range at the highs, and how the next breakout/downbreak resolves is the single most important decision point.

## 4. Momentum — the weak link

### MACD (line 1.5446 / signal 1.5566 / histogram −0.0120)
The MACD story is the most informative part of this report:

- MACD peaked at **3.136 on 2023-12-22**, then decayed to 2.782 by 12-29 and crossed below the signal (histogram −0.141) on **2023-12-29**.
- The histogram bottomed at **−1.230 on 2024-01-05** (MACD 0.859 vs signal 2.089) — a deep, fast momentum washout — then repaired, crossing back above signal on **2024-01-12** (histogram +0.094).
- That bullish recross **failed almost immediately**: histogram flipped to −0.039 on 01-17 and is −0.012 on 01-18. MACD line and signal are effectively fused at ~1.55.
- **Critical observation:** price closed at its highest level of the whole window on **2024-01-11 at 155.18**, but MACD that day was only **1.462** versus **2.971 on 2023-12-19** when price closed lower at 153.79. That is a clean, dated **negative momentum divergence** — price higher high, MACD lower high.
- The absolute MACD level (1.54) versus the December peak (3.14) says the *rate of ascent* has halved even though price is near the highs. This is characteristic of a trend transitioning from impulsive to corrective/grinding.

**Interpretation:** MACD is in a neutral, coiled state. The near-zero histogram means the next meaningful signal is a *decisive* separation — a sustained histogram expansion above ~+0.3 or below ~−0.3 would carry real information. The current wiggle around zero does not. Do not trade the 01-12/01-17 flip-flops; they are noise inside a flat MACD.

### RSI (57.33)
- RSI peaked at **68.05 on 2023-12-18**, dropped to **40.23 on 2024-01-04** (a near-oversold washout that did *not* reach 30), rebounded to **62.79 on 2024-01-11**, slipped to **53.72 on 2024-01-17**, and is back to **57.33**.
- Second divergence: RSI 62.79 at the 155.18 price high (01-11) versus RSI 68.05 at the lower 154.07 close (12-18). Mild, same direction as the MACD divergence.
- RSI has not exceeded 70 since mid-December — so there is **no overbought condition to work off**, which is a bullish-neutral fact. There is also no fresh oversold reset, meaning the "buy the dip in RSI" trigger has already been spent on the 01-04 spike to 40.
- RSI in the mid-50s inside an uptrend is the classic **neutral/coiling zone** — historically where continuation setups form, not where reversals begin.

**Net:** momentum is not broken, but it is *not confirming* price strength. Two dated divergences across two independent oscillators is a meaningful caution flag that reduces the probability of a clean immediate breakout to new highs.

## 5. Volatility and bands — compression into the range

- **ATR = 2.9829**, i.e. **1.94% of price**. ATR has contracted from 3.53 (2023-11-20) and from a local peak of 3.45 (2023-12-18), and is now at the lowest reading in the window except for the 2.81 print on 2023-12-29. Realized volatility is falling into the consolidation.
- **Bollinger (20,2):** lower 145.92, middle 151.79, upper 157.66. Total width = **11.74 points = 7.73% of the mid-band** — a compressed band. Position within the band (%B) ≈ **(153.50 − 145.92) / 11.74 ≈ 0.65**, i.e. upper-middle, not hugging the upper band.
- The upper band (157.66) sits just above the **157.17** intraday high of 2024-01-11 — those two levels cluster into a real resistance shelf at ~157–158.
- The lower band (145.92) sits inside the verified support cluster described in §7.

**Compression implication:** a ~7.7% band width with ATR near a two-month low is a classic squeeze condition. Squeezes resolve directionally with expansion; the resolution is more likely to be tradable than the current chop. Direction is *not* implied by the squeeze itself — it must be taken from the trigger (§8).

## 6. Volume and VWMA — the missing confirmation

- **VWMA = 150.88**, with price 153.50 → price is **~1.7% above** the volume-weighted average. That is bullish in direction, but note the VWMA has been **flat-to-down for three weeks**: 151.09 (01-02) → 151.25 (01-03) → 150.63 (01-10) → 150.88 (01-18). Volume-weighted price is going nowhere while the index price oscillates above it. That means recent turnover has been transacting in the low 150s — supply is being absorbed up there, but buyers are not yet paying up aggressively.
- **The 01-17 undercut-and-reclaim is the most useful volume/level detail:** the intraday low was **149.91**, piercing VWMA (150.90 that day), yet the close recovered to **151.71, above the VWMA**. A one-day undercut of a volume-weighted level that closes back above it is a constructive tell.
- **But the 01-18 bounce is on light volume:** 37.85M shares versus a rough average of ~44–45M across the prior eleven sessions (01-02 47.3M, 01-03 49.4M, 01-04 56.0M, 01-05 45.2M, 01-08 46.8M, 01-09 43.8M, 01-10 44.4M, 01-11 49.1M, 01-12 40.5M, 01-16 41.4M, 01-17 34.95M). The bounce does **not** carry volume confirmation.
- Offsetting that: the decline itself was also light — 40.5M, 41.4M and 34.95M, with **01-17's 34.95M the lowest volume of the entire recent stretch**. A low-volume pullback into support is normally *constructive* (no distribution signature). So the correct read is "supply is absent on both sides" — a drift, not a fight.

## 7. Verified key levels

| Level | Value | Source / status |
|---|---|---|
| Resistance (band top) | **157.66** | Bollinger upper band, 2024-01-18 |
| Resistance (intraday high) | **157.17** | 2024-01-11 high |
| Resistance | **156.20** | 2024-01-12 high |
| Resistance | **155.63 / 155.12** | 2023-12-20 / 2023-12-19 highs |
| Resistance (recent) | **154.99 / 153.78** | 2024-01-16 / 2024-01-18 highs |
| Pivot | **153.50** | 2024-01-18 close |
| Pivot | **152.26** | 10 EMA |
| Pivot | **151.79** | Bollinger 20-SMA mid |
| Support | **150.88** | VWMA |
| Support (swing) | **149.91** | 2024-01-17 low |
| Support (major) | **148.12** | 50 SMA |
| Support (cluster) | **145.92 / 145.52 / 144.53 / 144.05 / 143.64** | Bollinger lower / 12-14 low / 01-05 low / 01-04 low / 12-11 low |
| Long-term support | **130.82** | 200 SMA |
| Measured vol | **≈$2.98** | ATR(14) |

The **144.05–145.92 zone** is the highest-conviction demand shelf: five separate verified touch points between 2023-12-11 and 2024-01-05, plus the lower Bollinger band. The **148.12 (50 SMA)** is the first line of trend defence; below it, the 50 SMA has not yet been tested on a closing basis in this entire advance since November.

## 8. Actionable scenarios

### A. Base case — range continuation (highest probability given flat MACD + compressed ATR + light volume)
Trade the edges of **149.9–157.2**.
- **Long-side entry zone:** 150.5–151.8 (VWMA / Boll mid / prior close cluster). Invalidation: **daily close below 149.91**. Risk from 151.80 to 149.70 = **$2.10 (≈0.7 ATR)** — tight, because the level is well-defined.
- **Trim/avoid-add zone:** 156.2–157.7. Only add on a *volume-expanded* close above 157.66.
- Expect chop; this is a mean-reversion tape inside a bull trend, not a momentum tape.

### B. Bull continuation trigger
- **Trigger:** daily close **above 157.66** (upper band) on volume **≥ ~50M** (i.e. clearly above the ~44M recent average), with **MACD histogram expanding above +0.30** and MACD line turning up off 1.54.
- **Confirmation hierarchy:** close > 157.66 → MACD histogram positive and rising → RSI > 60 without exceeding 75.
- **Stop:** 1.5–2.0 ATR under the breakout level ≈ **153.5–154.5** (2 × 2.98 = 5.96 below 157.66 → 151.70; a tighter 1.5 ATR → 153.19). Since the MACD divergence argues against a clean breakout, a *retest* entry at 155–156 after a breakout would offer materially better risk/reward than the breakout print itself.
- **Sizing:** with ATR at 1.94%, risk-per-share is ~$3; for a 1% equity risk on a $100k book ($1,000), that is ~**330 shares**. Scale to the stop distance actually used, not to a fixed share count.

### C. Bear / trend-test trigger
- **Trigger:** daily close **below 151.79** (Boll mid) — already marginal, price closed below it on 01-17 — followed by a close **below 149.91**, ideally on volume > 50M. That would break the post-January swing low and convert the flat MACD into a sustained negative histogram.
- **First target:** **148.12 (50 SMA)**. Second: **145.92–144.05** support shelf. A break of 144.05 on volume would be the first genuine trend-damage signal and would put the 200 SMA (130.82) into play as a longer-horizon objective — a ~15% drawdown from current price, so this is not a tail-risk footnote.
- **Stop for existing longs:** 2 ATR below the 01-18 close = 153.50 − 5.97 = **147.53**, which conveniently sits just below the 50 SMA at 148.12. That combination — 1.9% ATR, 50 SMA at 148.12, 2-ATR stop at 147.53 — is the cleanest risk architecture available here.

### D. What would flip the momentum picture
1. **MACD histogram sustained above +0.30 for 3+ sessions** while price holds above 152.26 → divergence resolved bullishly.
2. **RSI pushing through 62.79 (the 01-11 peak)** on a new price high → divergence neutralized.
3. Conversely, **RSI failing below 50** while MACD histogram deepens below −0.30 → deceleration becomes distribution.

## 9. Risk notes and honest limitations

- **Event risk is not in these numbers.** Daily technicals computed through 2024-01-18 contain no information about the upcoming quarterly report; a binary gap event can invalidate every level in §7 in one session. Reduce position size ahead of it rather than relying on stops (gaps bypass stops).
- **The 200 SMA extension (~17.3% above) is real but not a signal.** It argues for smaller adds and wider stops, not for shorting a stacked uptrend.
- **The divergences are mild, not decisive.** RSI 68.05 → 62.79 and MACD 2.97 → 1.46 at higher highs are cautionary, but divergence in a strong trend frequently resolves *through* price consolidation rather than through reversal — which is precisely the range scenario in §8A.
- **Verify, don't assume.** If the verified snapshot ever conflicts with a secondary data source on an exact level, treat the snapshot as truth and re-derive the level table.

## 10. Summary table

| Dimension | Reading (2024-01-18) | Signal | Weight |
|---|---|---|---|
| Price | 153.50 close, +1.18% vs 151.71 | Rebound day, light volume | — |
| Long-term trend (200 SMA) | 130.82, rising daily; price +17.3% above | **Bullish, extended** | High |
| Medium trend (50 SMA) | 148.12, rising ~$0.30/day; price +3.6% above | **Bullish** | High |
| Golden cross | 50 SMA − 200 SMA = +$17.30 (13.2%) | **Confirmed, matured** | High |
| Short trend (10 EMA) | 152.26, flattened; price reclaimed it 01-18 | Neutral-to-bullish | Medium |
| Bollinger | 145.92 / 151.79 / 157.66; width 7.73%; %B ≈ 0.65 | **Squeeze / compression** | High |
| MACD | 1.5446 vs signal 1.5566, hist −0.0120 | **Flat / coiled**, lower highs vs Dec | High |
| MACD divergence | Price high 155.18 @01-11 vs MACD 1.462; Dec-19 MACD 2.971 @153.79 | **Negative divergence** | Medium-High |
| RSI | 57.33; peak 62.79 @01-11 vs 68.05 @12-18 | Neutral, mild divergence | Medium |
| ATR | 2.9829 (1.94% of price), contracting | Low vol → squeeze fuel | High |
| VWMA | 150.88, flat 3 weeks; price +1.7% above | Weak confirmation | Medium |
| Volume | 37.85M vs ~44M recent avg; 01-17 34.95M lowest | No conviction either way | Medium |
| Structure | Range ~149.9–157.2; support cluster 144.05–145.92 | **Range / consolidation** | High |
| **Bias** | **Bullish trend, neutral-to-cooling momentum** | **Buy pullbacks 150.5–151.8; don't chase** | — |
| **Invalidation** | Close < 149.91 → test 148.12; close < 144.05 → trend damaged | — | — |
| **Upside trigger** | Close > 157.66 on ≥50M volume + MACD hist > +0.30 | — | — |
| **Risk unit** | 1 ATR = $2.98; 2-ATR stop from 153.50 = 147.53 | — | — |

**Indicators selected (8):** `close_10_ema`, `close_50_sma`, `close_200_sma` (three time horizons of trend, no redundancy between them), `macd`, `macds` (crossover/momentum-change engine, complementary to the trend filters), `rsi` (independent overbought/oversold + divergence check that MACD cannot provide), `atr` (volatility/stop-sizing), `vwma` (volume-weighted confirmation of the trend). Bollinger band values are taken directly from the verified snapshot for the squeeze/range analysis. Deliberately excluded: `macdh` (fully derivable from `macd`/`macds`), `boll`/`boll_lb` (upper band + snapshot triple covers it), and stochastics/MFI (would duplicate RSI's information and the snapshot's MFI is on a non-standard scale).