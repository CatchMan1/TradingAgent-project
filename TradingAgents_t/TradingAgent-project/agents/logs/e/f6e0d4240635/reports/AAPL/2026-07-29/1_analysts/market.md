# AAPL — Technical & Trend Analysis
**Analysis date: 2026-07-29 (close) | Verified snapshot source of truth: `get_verified_market_snapshot` for 2026-07-29**

---

## 1. Verified price state (source of truth)

| Field | Value |
|---|---|
| Open | 339.73 |
| High | 344.57 |
| Low | 337.35 |
| **Close** | **338.19** |
| Volume | 56,090,800 |
| Total-return index | 343.899 |
| 50 SMA | 308.5888 |
| 200 SMA | 277.2134 |
| 10 EMA | 330.8389 |
| MACD / Signal / Hist | 9.6087 / 8.4367 / +1.1720 |
| RSI(14) | 66.78 |
| Bollinger mid / upper / lower | 322.4005 / 346.1370 / 298.6640 |
| ATR(14) | 8.0184 |
| VWMA | 328.5078 |
| MFI (as reported) | 0.6948 (appears 0–1 scaled ≈ 69.5 on a 0–100 convention — **units ambiguous, flagged, not used for signals**) |

**Consistency check:** every indicator value returned by `get_indicators` today matches the verified snapshot to the decimal (RSI 66.784645, MACD 9.608724, ATR 8.018410, VWMA 328.507824, Boll UB 346.137043, 50SMA 308.5888, 200SMA 277.213449, 10EMA 330.838916). **No discrepancies found.** The single ambiguity is the MFI scaling noted above.

---

## 2. Indicators selected (8) and why

| Indicator | Role in this context |
|---|---|
| `close_200_sma` | Strategic trend anchor — confirms the primary uptrend and that AAPL is not in a bear regime. |
| `close_50_sma` | Medium-term trend + dynamic support; measures trend *slope* and the 50/200 spread. |
| `close_10_ema` | Short-term momentum/entry timing; the level a trend-follower trails in a fast up-leg. |
| `macd` | Momentum regime shifts and crossovers around the aggressive June→July reversal. |
| `rsi` | Overbought risk and divergence checks in a strongly trending tape. |
| `boll_ub` | Breakout/extension gauge; price is riding a steeply rising band — the key near-term ceiling. |
| `atr` | Volatility-scaled stops and position sizing; there is real single-day gap risk in this name. |
| `vwma` | Volume-weighted cost basis — separates genuine accumulation from drift. |

Deliberately excluded as redundant: `macds`/`macdh` (signal and histogram derive arithmetically from `macd`; histogram +1.17 is quoted from the snapshot), `boll`/`boll_lb` (values taken from the snapshot rather than burning a slot), and no second oscillator (RSI already covers momentum; stochrsi/other oscillators would be duplicative). Bollinger *upper* was kept over mid/lower because the actionable near-term question is breakout extension, not oversold.

---

## 3. Primary trend: confirmed, mature, and accelerating

- Close **338.19** vs **50 SMA 308.59 (+9.6%)** vs **200 SMA 277.21 (+22.0%)**. Price > 50SMA > 200SMA with both averages rising — textbook bullish stack.
- The 50 SMA sits **+11.3% above** the 200 SMA (308.59 vs 277.21), and the 50 SMA has risen every single session in the pulled window from 260.02 (2026-03-31) to 308.59 (2026-07-29). This is a *broadening* golden-cross, not a flattening one.
- The 200 SMA has climbed monotonically from 248.56 (2026-03-31) to 277.21 — the long-term trend line itself is being pushed up, i.e., higher lows are being made structurally.
- **Year-to-date context:** 2026-01-02 close 271.01 → 338.19 = **+24.8%**. Measured off the January low close (246.70 on 2026-01-20) the advance is **+37.1%**.

**Verdict: primary uptrend intact and strengthening. This is a trend-following / buy-the-dip environment, not a mean-reversion environment.**

---

## 4. The structural story: a 5-month range broke out in mid-July

Reading the actual OHLC from `get_stock_data`:

1. **January high-to-low:** ran to 278.95 intraday (2026-02-04) then sold off hard — 2026-02-12 closed 261.73 from 275.50 (−5.0% day, on 81.1M shares).
2. **A well-defined floor at ~243–246:** four separate intraday tests — 2026-01-20 low **243.42**, 2026-03-20 low **246.00**, 2026-03-30 low **245.51**, 2026-04-07 low **245.70**. This is the most reliable support shelf in the dataset because it is multi-touch and months apart.
3. **A ceiling at ~315–317:** intraday highs 315.45 (2026-06-02), 316.94 (2026-06-03), **317.40 (2026-06-08)**. That became the range top.
4. **June shakeout:** 2026-06-25 closed **275.15** from 293.08 (**−6.1%**, 107.0M shares), then 2026-06-26 printed an enormous **261.8M share** session with a low of 274.21 and a close of 283.78 (+3.1%, closing near the high of a 274.21–285.95 range). That is a capitulation-and-reclaim signature on roughly 5× normal volume.
5. **Reclaim and breakout:** 2026-07-15 closed **327.50** (+4.0% from 314.86, 61.0M) and 2026-07-16 closed **333.26** (+1.8%, 63.0M) — decisively above the 317.40 range ceiling, on expanding volume. From the 2026-06-25 close of 275.15 to today's 338.19 is **+22.9%** in about 24 sessions.

**Interpretation:** the June 25–26 crash was a failed breakdown that trapped sellers, and the subsequent thrust cleared a five-month ceiling. Failed breakdowns followed by range breakouts are among the highest-quality continuation setups. Note also that today's **344.57 high is the highest price in the entire 2026 dataset** — there is no overhead supply from this year.

One honest caveat: the June 25–26 episode (+260M shares, −6% single-day) is direct evidence that AAPL can gap through support instantly in this regime. Any position needs a volatility-aware stop, which is exactly why ATR is in the set.

---

## 5. Short-term momentum: strong, but the tape paused today

| Date | Close | 10 EMA | MACD | RSI |
|---|---|---|---|---|
| 2026-07-15 | 327.50 | 312.92 | 6.60 | 68.77 |
| 2026-07-17 | 333.74 | 319.73 | 8.82 | **71.65** |
| 2026-07-20 | 326.59 | 320.98 | 8.88 | 63.87 |
| 2026-07-23 | 321.66 | 322.66 | 8.11 | **58.11** |
| 2026-07-27 | 336.91 | 326.79 | 8.93 | 67.29 |
| 2026-07-28 | 340.08 | 329.21 | 9.45 | 68.90 |
| **2026-07-29** | **338.19** | **330.84** | **9.61** | **66.78** |

- **MACD regime shift is clean:** MACD bottomed at **−2.92 on 2026-06-29** and crossed back positive by 2026-07-06 (0.88). It has since printed a higher sequence (8.11 low on 07-23 → 9.61 today). With the signal at 8.44, the histogram is **+1.17 and expanding** — momentum is re-accelerating, not decaying.
- **RSI 66.78 is a *reset*, not a reversal.** RSI hit 71.65 on 2026-07-17, then cooled to 58.11 on 2026-07-23 while price only fell from 333.74 to 321.66 (−3.6%). Price made a higher high on 2026-07-28 (340.08) with RSI at 68.90 — the overbought condition was worked off *through a shallow dip and renewed buying*, which is characteristic of strong uptrends.
- **Mild negative divergence to monitor:** RSI peaked at 73.58 on 2026-06-02 (close 315.20) and at 71.65 on 2026-07-17 (close 333.74) — a *lower* RSI peak against *higher* price. This is a low-grade warning, not a sell signal, and it is partly an artifact of the June 25 crash resetting the oscillator. It becomes meaningful only if RSI fails below ~60 on the next push.
- **Today's candle is a hesitation bar, not a rejection:** 338.19 closed below yesterday's 340.08 but the session printed a *higher high* (344.57 vs 342.89) and a *higher low* (337.35 vs 335.60). The open (339.73) was near the close (338.19). Structure is intact; the body is small. Real risk would be a close back below the 10 EMA at 330.84.

---

## 6. Volatility and band geometry

- **ATR = 8.02**, i.e. **2.37% of price**. Critically, ATR has been *declining* while price made new highs: 8.74 (2026-07-02) → 8.33 (07-15) → 8.02 (today). An advance on contracting volatility is a controlled, orderly grind — the opposite of a blow-off.
- **Bollinger:** upper **346.14**, middle **322.40**, lower **298.66**; band width ≈ 47.47 points ≈ 14% of price (unusually wide, a legacy of the June whipsaw). Position within the bands (%B) = (338.19 − 298.664) / (346.137 − 298.664) ≈ **0.83**. Price is in the upper quartile of a wide envelope, not pinned to the band — there is genuine room to 346 without being statistically stretched.
- The **upper band has risen from 312.31 (2026-07-01) to 346.14** with price — the band is expanding upward rather than price tagging a flat band. That is breakout behavior.
- **Confluence map (the single most useful thing on this chart):** Bollinger middle **322.40**, the 2026-07-21/22 congestion (325.89–327.74), the 2026-07-23 low **319.35**, and 2026-07-20 low **323.68** all cluster in the **319–327** zone. That is a thick, multi-dated support shelf directly beneath the current price, and it is where the 10 EMA (330.84) is fast converging.

---

## 7. Volume confirmation

- **VWMA = 328.51** vs close 338.19 → price is **+2.95% above** the volume-weighted cost basis. VWMA has risen from 288.84 (2026-06-30) to 328.51, meaning new money is being added at progressively higher prices.
- The breakout days carried above-average volume: 2026-07-15 (61.0M), 2026-07-16 (63.0M), 2026-07-17 (63.4M), 2026-07-24 (47.5M on a +3.5% day from 321.66 to 333.02). Today's 56.1M is roughly 1.1× the ~50M July average — moderate, consistent with a consolidation day rather than distribution.
- **The one volume caution:** the biggest prints of the year were *down/reversal* sessions (107.0M on 2026-06-25; 261.8M on 2026-06-26), not the up-days. The retest of the June low came on much lighter volume than the panic itself — normal and healthy — but it means the 321–327 shelf, not the 340s, is where volume has historically asserted itself.

---

## 8. Actionable plan

**Bias: bullish / trend-continuation, with a tighter leash on fresh entries after a +23% 24-session run.**

**Entry approaches**
1. **Continuation trigger:** a daily close above **344.57** (today's high, and the 2026 high) opens the upper band at **346.14** and then blue-sky territory above. Confirm with volume > ~60M.
2. **Preferred risk-adjusted entry:** buy the pullback into the **330.8–327.5** zone (10 EMA + recent congestion). The 10 EMA has already risen to 330.84 and catches up fast; a tag of it with RSI back near 60 would be a low-risk add.
3. **Deep-value add:** the **319–322.4** confluence (Bollinger middle + 07-23 low + 07-20 low). A close below 319 breaks the shelf, so that entry must be pre-defined, not chased.

**Risk management (ATR-based, not arbitrary)**
- Swing stop under the pullback entry: **1.5 × ATR ≈ 12.0 points**. From 330 area that is ~318 — conveniently just under the 319.35 shelf.
- Structural stop for the trend trade: a **daily close below the 50 SMA (308.59)**, currently ~2.7 ATR below spot. That is the line that would negate the July breakout thesis.
- Position size: with ATR at 2.37% of price, a 1% account risk per trade implies roughly 0.42× notional exposure per unit of 1-ATR stop distance — i.e. size down ~40% versus a 1%-ATR-volatility name.

**Invalidation / what would change the call**
- Close below **330.84 (10 EMA)** → short-term momentum lost; expect a test of 322–327.
- Close below **322.40 (Bollinger middle)** → July breakout suspect; reduce.
- Close below **308.59 (50 SMA)** → trend thesis broken.
- RSI closing below **60** on a new price high would upgrade the mild divergence noted in §5 into a genuine warning.

**Upside projection (geometry, not a tool output — flagged as derived arithmetic):** the Feb–July range was roughly 245–317, a 72-point box. A measured move from the 317.40 breakout implies ≈ **389**, which would sit well above the current 346 upper band — i.e., the band is *not* a structural ceiling, only a short-term extension marker.

---

## 9. Risk register

| Risk | Evidence | Mitigation |
|---|---|---|
| Extended short-term | Close +9.6% above 50 SMA, +23% in 24 sessions, RSI 66.78 | Scale in; don't chase >344.57 without volume |
| Gap risk is real and recent | 2026-06-25: −6.1% in one session on 107M shares | ATR-sized stops; avoid oversized single entries |
| Mild momentum divergence | RSI 73.58 (06-02) vs 71.65 (07-17) on higher price | Require RSI > 60 on next high to keep the thesis |
| Volume concentrated in down days | Largest 2026 prints: 107.0M (06-25), 261.8M (06-26) | Watch whether 344+ breakout draws >60M |
| Wide Bollinger envelope | Band width ≈ 14% of price; %B ≈ 0.83 | Treat 346 as a trim zone, not a target-and-exit |
| MFI scaling ambiguity | Snapshot reports 0.6948 | Excluded from signal logic |

---

## 10. Summary table

| Dimension | Reading (2026-07-29) | Signal |
|---|---|---|
| Close | 338.19 (H 344.57 / L 337.35) | New 2026 high intraday; small down close |
| 10 EMA | 330.84 (price +2.2%) | Bullish, rising steeply |
| 50 SMA | 308.59 (price +9.6%) | Bullish, rising 60+ sessions |
| 200 SMA | 277.21 (price +22.0%) | Bullish, rising |
| 50 vs 200 spread | +31.4 pts (+11.3%) | Golden cross broadening |
| MACD / Signal / Hist | 9.61 / 8.44 / +1.17 | Bullish, histogram expanding |
| RSI(14) | 66.78 (peak 71.65 on 07-17) | Strong, not overbought; mild lower-high |
| Bollinger UB / Mid / LB | 346.14 / 322.40 / 298.66 | %B ≈ 0.83; room to 346 |
| ATR(14) | 8.02 (2.37% of price) | Falling — orderly advance |
| VWMA | 328.51 (price +3.0%) | Volume confirms accumulation |
| Volume | 56.1M (~1.1× July avg) | Neutral/consolidation |
| Key resistance | 344.57 (2026 high) → 346.14 (upper band) | Breakout trigger |
| Key support 1 | 330.84 (10 EMA) / 327.5–325.9 | Preferred dip-buy zone |
| Key support 2 | 322.40 (Boll mid) / 319.35 (07-23 low) | Confluence shelf — thesis hinge |
| Key support 3 | 308.59 (50 SMA) | Structural stop |
| Structural floor (2026) | 243.42 / 245.51 / 245.70 / 246.00 | Four-touch demand shelf |
| **Overall stance** | **Buy-the-dip in an intact uptrend; breakout add above 344.57** | **Bullish, risk-managed** |

*This is technical analysis of tool-provided data, not investment advice. All levels are derived from the verified 2026-07-29 snapshot and the 2026-01-01 → 2026-07-29 OHLCV history.*