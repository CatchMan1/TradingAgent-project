# AAPL — Multi-Timeframe Technical Analysis (as of 2026-10-06)

**Bottom line:** AAPL remains in a well-established primary uptrend (price ~15% above a rising 200-day SMA, 50-day SMA ~11% above the 200-day), but it has spent the last two weeks in a tightening sideways consolidation directly on its 20-day mean. Short-term momentum has cooled (MACD bearish crossover on 2026-09-29), volatility has compressed to the lowest level in the visible two-month window, and price is trading slightly *below* its volume-weighted average — a sign of mild overhead supply rather than aggressive distribution. This is a coiled, neutral-to-constructive setup awaiting resolution, not a trend-following entry at current levels.

---

## 1. Verified snapshot anchors (source of truth: 2026-10-06)

| Metric | Value | Read-through |
|---|---|---|
| Close / Open / High / Low | 333.63 / 332.28 / 334.38 / 330.62 | Small-bodied, inside-range day; close in upper half |
| Volume | 30,449,000 | Below recent average (~39M over last ~19 sessions) |
| close_50_sma | 322.348 | Rising, but slope flattening; +3.50% below price |
| close_200_sma | 289.759 | Rising ~0.25 pts/day; price +15.14% above |
| close_10_ema | 333.565 | Price essentially pinned to it (+0.02%) |
| macd / macds / macdh | 3.2497 / 4.2922 / **-1.0425** | Positive but below signal → short-term bearish |
| rsi | 54.56 | Neutral, mid-range |
| boll / boll_ub / boll_lb | 333.412 / 344.656 / 322.167 | Price at 51% of band width |
| atr | 6.637 | ~1.99% of price; lowest reading since early Aug |
| vwma | 335.499 | Price 0.56% *below* volume-weighted average |
| mfi (snapshot only) | 0.703 | Moderate, non-extreme money flow |

No conflicts were found between `get_stock_data`, the individual indicator series, and the verified snapshot — all values match to the decimal.

---

## 2. Trend structure

**Long term (bullish, intact).** The 200-day SMA has climbed monotonically in the visible window: 279.41 on 2026-08-07 → 289.76 on 2026-10-06 (+3.7% in two months). Price at 333.63 sits 15.1% above it. The 50-day SMA (322.35) is 11.3% above the 200-day, so the golden-cross configuration is mature and wide, not freshly triggered. Nothing in the data suggests a long-term trend break; a bearish structural change would require a close below roughly 290, which is ~13% away.

**Medium term (rising, decelerating).** The 50-day SMA rose from 309.79 (2026-08-07) to 322.35 (2026-10-06), but its daily increment has compressed to near zero: 322.176 (10-01) → 322.416 (10-02) → 322.414 (10-05) → 322.348 (10-06). That is a classic signature of a trend digesting its August–September advance rather than accelerating.

**Short term (sideways / coiling).** Since the 2026-09-22 swing high (intraday 345.34, close 339.75), price has printed a sequence of lower closes into 2026-09-29 (close 329.40, low 328.70) and has since recovered to 333.63. Over the same stretch:
- 10-day EMA peaked at 335.96 (2026-09-28) and has drifted down to 333.565, now flat for four sessions (333.70, 333.70, 333.55, 333.57) — a textbook short-term equilibrium.
- Price has closed in a ~329–341 band for roughly six sessions.
- Longer context: the 2026-07-30 close was 333.43 and the 2026-10-06 close is 333.63 — effectively **flat over ~2.3 months** (after the 2026-07-31 earnings-like gap from 333.43 to 308.91 and subsequent full recovery). This is a two-month base at the highs, not a fresh breakout.

**Structural pivot history worth noting (tool-verified):**
- 2025-10-10: intraday low **244.00** (close 245.27) — the low of the visible 12-month window; price is +36.7% above it.
- 2026-01-20: close 246.70 / low 243.42 — retest that held.
- 2026-06-25: close 275.15 (from 293.08 the prior day) — a second sharp single-session repricing.
- 2026-07-31: close 308.91 (from 333.43), low 300.00 — third large gap.
- 2026-09-22: intraday high **345.34** — the 12-month high; price is 3.39% below it.

The repeated pattern of large single-session gaps (Feb 12, Jun 25, Jul 31) is consistent with earnings/event risk. A similar event is plausibly due in the late-October window; **confirm the actual date independently before sizing around it.**

---

## 3. Momentum: deterioration, but contained

**MACD (3.2497 / signal 4.2922 / histogram −1.0425).**
- MACD peaked at **6.248** on 2026-09-22 and has fallen for nine consecutive sessions to 3.250 (−48% from peak).
- The **bearish crossover occurred on 2026-09-29**: MACD 5.188 vs signal 5.471 (histogram −0.283 vs +0.537 on 2026-09-28).
- The histogram has bottomed at −1.069 (2026-10-05) and improved marginally to −1.043 (2026-10-06) — the first hint that the downside impulse is decelerating, though one session is not confirmation.
- Crucially, MACD is still **positive**, so this reads as a momentum reset within an uptrend, not a trend reversal signal.

**RSI (54.56).**
- RSI peaked at 66.88 (2026-09-22) and 66.32 (2026-09-21) — **never reaching 70**, meaning the September advance was persistent but not euphoric.
- It fell to 50.88 on 2026-09-29 (the session that tested 328.70) and has recovered to 54.56, i.e., dip buyers stepped in around the mid-line.
- No clean bearish divergence is visible: on 2026-09-25 price closed higher (341.07) than 2026-09-22 (339.75) while RSI was lower (65.67 vs 66.88) — a marginal, not decisive, divergence.
- Net: neutral with a slight constructive tilt; there is room to run to ~65–70 before momentum becomes a headwind again.

**Read:** momentum is in a corrective phase, but both MACD and RSI are above their mid-lines/base levels. This favors "pause" over "reversal."

---

## 4. Volatility: a genuine squeeze is forming

- **ATR = 6.637**, down from 8.046 on 2026-09-11 (−17.5%) and the lowest reading in the entire 8-week series. That is 1.99% of the 333.63 close.
- **Bollinger width has contracted sharply:** upper 346.89 / lower 313.77 on 2026-09-28 (width 33.12) → upper 344.66 / lower 322.17 on 2026-10-06 (width **22.49**, −32%). Current bandwidth is 6.74% of the 333.41 middle band.
- The bands are converging **symmetrically** around the middle (upper fell ~2.2 pts, lower rose ~8.4 pts over the period, converging onto the flat 20-day mean).
- Price sits at 51% of band width (333.63 vs mid 333.41), i.e., dead-center.

Compression of this magnitude typically precedes an expansion move; the direction is *not* pre-determined by the squeeze itself. The tie-breakers are (a) whether price closes above 339.75–341.07 on expanding volume (bull resolution) or below 328.70 (bear resolution), and (b) confirmation from MACD histogram flipping positive/negative.

---

## 5. Volume and participation

- **VWMA = 335.499 vs close 333.63** → price is 0.56% *below* the volume-weighted average. Aggregate recent volume is transacting slightly above the current price, which implies supply sitting in the 334–336 zone.
- VWMA has been flat at 335.30–335.50 since 2026-09-30 after a steep climb from 309.19 (2026-08-25) to 335.34 (2026-09-30). A flat, elevated VWMA with price below it = stalled, volume-supported advance that needs fresh demand to reclaim 335.5.
- **Volume is drying up:** 30.45M on 2026-10-06 versus recent sessions such as 86.59M (2026-09-18, likely index/derivative expiry), 70.01M (2026-09-10), 50.72M (2026-09-11), 49.99M (2026-09-30). Roughly 22% below the ~39M mean of the last ~19 sessions. Low-volume drift inside a range is neutral/coiling; low-volume *breakout* would be suspect.
- Snapshot MFI 0.703 (not independently re-computed here) is consistent with modest net inflows — neither accumulation thrust nor distribution.

---

## 6. Actionable price map (all levels tool-derived)

| Level | Source | Role |
|---|---|---|
| **345.34** | 2026-09-22 intraday high | 12-month high / breakout trigger zone |
| **344.66** | Bollinger upper band (10-06) | Immediate resistance cap |
| **341.07 / 339.75** | Closes 2026-09-25 / 2026-09-22 | First resistance shelf (range top) |
| **335.50** | VWMA | Pivot: reclaim = buyers back in control |
| **333.57 / 333.41** | 10 EMA / Bollinger mid | Current equilibrium |
| **330.62** | 2026-10-06 low | Intraday support |
| **328.70 / 329.40** | 2026-09-29 low / close | Range floor; break = squeeze resolves lower |
| **322.17 / 322.35** | Bollinger lower band / 50 SMA | **Confluence support** — key medium-term line |
| **315.34 / 316.22** | Closes 2026-09-09 / 2026-09-08 | Next demand shelf if 322 fails |
| **309.90** | 2026-09-09 intraday low | Swing low of the Sep pullback |
| **289.76** | 200 SMA | Long-term bull/bear demarcation |

---

## 7. Scenarios and trade plans

**A. Bullish breakout (primary plan, not yet triggered).**
- Trigger: daily close **above 341.07** (ideally above 345.34) with volume ≥ ~45–50M (a clear expansion over the recent 30–39M).
- Targets: 344.66 (upper band) → 345.34 (prior high) → measured extension of the 322–345 range (~368) if a decisive breakout occurs.
- Stop: below 333.4 (Bollinger mid) for aggressive entries, or below 328.70 for swing entries. A 2×ATR stop from 341 = ~327.7, i.e., just under the range floor — mechanically sensible.
- Note: entering long at 333.63 *inside* the range offers poor reward/risk (~10 pts to resistance vs ~11 pts to the 50-SMA stop). Waiting for the retest of 335.5+ or the breakout is preferable.

**B. Range / mean-reversion (tactical).**
- Buy zone: **329–330** (range floor, 2026-09-29 congestion) with a stop below 328.70 or 1.5×ATR (~10 pts) → risk ~1–5 pts for ~5–8 pts to the mid/upper half. Best odds if the MACD histogram turns back toward zero.
- Deeper buy zone: **322.2–322.4** (50 SMA + lower Bollinger confluence) — a higher-quality, higher-conviction add level if reached on a non-gap move.
- Reduce/trim into 339.5–341 unless volume confirms a breakout.

**C. Bearish resolution.**
- Trigger: daily close **below 328.70** on above-average volume, with MACD histogram extending below −1.07.
- Targets: 322.17–322.35 confluence first, then 315.3–316.2.
- Invalidation: a fast reclaim of 333.5–335.5.
- Note that even in this scenario the 200-day (289.76) is far below; this would be a corrective leg within a longer uptrend, not a trend change.

**Risk sizing.** ATR 6.637 = 1.99% of price. For a 1% account risk per trade, position size ≈ 0.01 × equity ÷ (1.5–2.0 × 6.637) ≈ equity/1000 to equity/1327. Because the stock has repeatedly gapped 6–8% on event days (2026-02-12, 2026-06-25, 2026-07-31), consider half-size or defined-risk options structures into the late-October event window, since ATR-based stops do not protect against gaps.

---

## 8. Why these eight indicators

1. **close_200_sma** — establishes the strategic regime; confirms the uptrend is intact and gives the 289.76 bull/bear line.
2. **close_50_sma** — the medium-term trend and the most relevant dynamic support (322.35) for this consolidation.
3. **close_10_ema** — captures the short-term stall precisely (flat at 333.57, exactly at price) that the slower averages cannot show.
4. **macd** — quantifies the momentum rollover (6.25 → 3.25) and the 2026-09-29 bearish crossover; still positive, so it distinguishes "reset" from "reversal."
5. **macds** — needed to time the crossover and to confirm the histogram's recent stabilization; complements rather than duplicates MACD.
6. **rsi** — independent momentum check showing no overbought extreme was reached, so the pullback is a reset, not exhaustion.
7. **boll_ub** — marks the 344.66 breakout cap and quantifies band convergence from 2026-09-28 onward.
8. **boll_lb** — supplies the 322.17 support that coincides with the 50 SMA, a high-value confluence.
9. **atr** — converts the squeeze into position-sizing and stop distances (2% daily range, lowest in 8 weeks).
10. **vwma** — the only participation/volume-aware input; price below the 335.50 VWMA is the key evidence of overhead supply that pure price averages miss.

(Deliberately omitted: stochastics-type duplicates of RSI, and MACD histogram as a separate series since it is derivable from MACD and signal.)

---

## 9. Caveats

- All values are point-in-time as of 2026-10-06; the last row is the current session and may be an incomplete/early close.
- No claim of a "bounce" off support is made — the 2026-09-29 low (328.70) and 2026-09-09 low (309.90) are cited as levels where price previously found bids, not as validated support tests.
- Percentage moves quoted are arithmetic from the verified closes, not total-return figures unless stated. The technical total return index rose from 260.28 (2025-10-06) to 339.56 (2026-10-06), but that is *not* reflected in the price series you would trade against.
- MFI (0.703) comes only from the snapshot and was not independently recomputed.

---

## 10. Summary table

| Dimension | Signal | Evidence (2026-10-06) | Implication |
|---|---|---|---|
| Primary trend | **Bullish** | Close 333.63 > 200 SMA 289.76 (+15.1%); 50 SMA 11.3% above 200 SMA; both rising | Stay structurally long-biased; don't fight the trend |
| Medium trend | **Bullish but flattening** | 50 SMA 309.79 (08-07) → 322.35 (10-06); daily change ≈ 0 last 4 sessions | Trend digesting; not accelerating |
| Short trend | **Neutral / coiling** | 10 EMA 333.565 ≈ price (+0.02%); flat 4 sessions; 6-session range ~329–341 | Wait for resolution |
| Momentum | **Corrective** | MACD 3.250 vs signal 4.292 (crossover 09-29); histogram −1.043; MACD −48% from 09-22 peak | Momentum reset, still positive |
| RSI | **Neutral** | 54.56; peak 66.88 (09-22), trough 50.88 (09-29) | Room both ways; no exhaustion signal |
| Volatility | **Squeeze** | ATR 6.637 (lowest in 8 wks, 1.99% of price); band width 33.1 → 22.5 (−32%) | Expansion move pending; direction unknown |
| Band position | **Dead center** | 51% of 322.17–344.66 width; mid 333.41 | No edge from bands at current price |
| Volume/flow | **Mildly negative** | Close 333.63 < VWMA 335.50; volume 30.4M ≈ 22% below recent average | Overhead supply 334–336; breakout needs volume |
| Near resistance | **339.75–341.07**, then **344.66 / 345.34** | Closes 09-22 & 09-25; upper band; 12-month high | Breakout trigger zone |
| Near support | **328.70/329.40**, then **322.17/322.35** | 09-29 low/close; lower band + 50 SMA confluence | Break below 328.70 → 322 test |
| Preferred action | **Wait / range-trade** | Poor reward:risk at mid-band; ATR-based stops 2×ATR ≈ 13.3 pts | Buy 329–330 or 322.2–322.4; buy breakout >341 on volume |
| Event risk | **Elevated** | Historical single-session gaps: 02-12, 06-25, 07-31 (−6% to −7.5%) | Confirm earnings date; half-size or defined risk |