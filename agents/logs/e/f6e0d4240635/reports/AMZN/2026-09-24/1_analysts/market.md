# AMZN — Multi-Timeframe Technical Review
**As of Thursday, 2026-09-24 (close) | Verified snapshot used as source of truth**

---

## 1. Snapshot of Verified Data

| Item | Value |
|---|---|
| 2026-09-24 OHLC | O 246.02 / H 250.43 / L 245.60 / **C 249.38** |
| Volume | 33.04M (≈0.93× the 20-session average of ~35.4M I compute from the tape) |
| 10 EMA | 252.53 |
| 50 SMA | 256.18 |
| 200 SMA | 240.73 |
| VWMA | 252.96 |
| RSI (14) | 44.20 |
| MACD / Signal / Hist | −1.881 / −1.482 / **−0.399** |
| Bollinger mid / upper / lower | 254.64 / 264.07 / 245.20 |
| ATR | 5.97 (2.39% of price) |
| MFI (snapshot only) | 0.374 |

**Data integrity check:** the last row of `get_stock_data` (2026-09-24: 246.02/250.43/245.60/249.38, 33,040,100 shares) matches `get_verified_market_snapshot` exactly, and every indicator value from the indicator tools matches the snapshot (10 EMA 252.53, 50 SMA 256.18, 200 SMA 240.73, MACD −1.8808/−1.4820, RSI 44.195, ATR 5.970, VWMA 252.96). **No discrepancy to flag.** One caveat: the local price history supplied begins 2026-02-20 (150 rows), so the 200 SMA is taken as vendor-computed rather than independently reconstructed from the CSV.

---

## 2. Why These Eight Indicators

AMZN is in a **post-earnings consolidation that has rolled into a short-term downtrend inside a still-intact long-term uptrend**, on **compressing volatility and shrinking volume**. That regime needs: two trend anchors to separate the strategic from the tactical, one fast average for timing, a momentum oscillator + MACD pair for thrust/decay, ATR for risk sizing during compression, and a volume-weighted price to test whether the drift is being "voted" by real size.

1. **close_10_ema** – fast timing; tells us whether the bounce attempts have any traction.
2. **close_50_sma** – the medium-term pivot AMZN has been fighting since September; also dynamic resistance.
3. **close_200_sma** – the line that defines whether this is a correction or a trend break.
4. **macd** – measures the momentum regime shift out of the August high.
5. **macds** – required to read the crossover; MACD without its signal is uninterpretable here.
6. **rsi** – shows whether downside momentum is exhausted (it is not yet) and flags any divergence.
7. **atr** – volatility is contracting; this sets stops, targets, and position size.
8. **vwma** – distinguishes a low-volume drift from genuine distribution.

*Deliberately excluded:* `boll`, `boll_ub`, `boll_lb` (the snapshot values are quoted for context, but they largely duplicate the 50 SMA + ATR information already covered), and `macdh` (it is arithmetic from the two MACD series I already have).

---

## 3. Long-Term Structure: Uptrend, Bruised But Intact

- **200 SMA = 240.73 and rising monotonically** every session in the visible window (237.86 on 2026-08-17 → 240.73 on 2026-09-24). Price at 249.38 sits **+3.59% above it**, so the primary trend has not been violated.
- **50 SMA (256.18) > 200 SMA (240.73)** by 15.45 points — a bullish structural alignment. But the 50 SMA has **just stopped rising**: 256.29 on 9/23 → 256.18 on 9/24, the first down-tick in the series after climbing from 248.32 on 8/17. That is the mechanical footprint of the September drift.
- The bigger arc: AMZN closed **210.11 on 2026-02-20** and **249.38 on 2026-09-24 (+18.7%)**, with a decisive April re-rating (213.77 on 4/7 → 221.25 on 4/8 → 233.65 on 4/9) and a July/August earnings explosion.
- **The earnings breakaway:** 7/30 close **235.50** → 7/31 open **265.00** and close **271.58** on 129.1M shares (7/30 volume 101.8M). The move peaked at **284.02 close / 287.20 intraday on 8/3**. From that 8/3 close to 9/24's 249.38, AMZN is **−12.20%**; from the 287.20 high to the 9/16 low of 244.30, **−14.94%**.
- **The gap is still partially unfilled:** the 235.50→265.00 earnings gap has been retraced to 245.60 (≈70% of the gap), but the 235.50 base has never traded again. That zone is the structural "line in the sand" for the bull case.

**Interpretation:** a normal, orderly retracement of an unusually violent 25.3% advance (226.65 on 7/29 → 284.02 on 8/3), not yet a trend reversal.

---

## 4. Medium-Term Structure: A Textbook Descending Sequence

Since the 8/3 peak, the tape has printed **lower highs and lower lows**:

- **Highs:** 287.20 (8/3) → 267.56 (8/28) → 261.12 (9/4) → 259.49 (9/21)
- **Lows:** 255.02 (8/27) → 251.93 (9/1) → 250.65 (9/9) → 249.58 (9/10) → 247.22 (9/15) → **244.30 (9/16)**
- **Most recent:** 247.76 (9/23) and **245.60 (9/24)** — a *marginally higher* low versus 244.30, six sessions later.

That last detail is the only constructive medium-term fact on the chart: a potential short-term double-bottom around **244.3–245.6**. It is a *forming* pattern, not a confirmed reversal — the lower-high sequence above it is completely intact.

**Moving-average stack:** price 249.38 < 10 EMA 252.53 < VWMA 252.96 < 50 SMA 256.18. Fully bearish short-term alignment, with the 10 EMA crossing **below** the 50 SMA on **9/15** (254.65 vs 255.56) — a datable, still-widening bearish cross (now −3.65 points). Price has chopped across the 50 SMA three times in September (above on 9/11 at 256.78 vs 255.25; below on 9/14 and every session from 9/15 except none) — the repeated failure at the 50 SMA is what makes it valid *resistance* rather than support.

**Fibonacci check on the 226.65 (7/29) → 284.02 (8/3) leg (+57.37 points):**
- 38.2% retracement ≈ 262.10
- 50.0% ≈ 255.34 (coincides almost exactly with the 50 SMA at 256.18)
- 61.8% ≈ **248.56**

9/23 closed 249.27 and 9/24 closed 249.38 — **both sessions held the 61.8% retracement**. That is the single most important tactical level in play right now.

---

## 5. Momentum: Decelerating, Not Capitulating

- **MACD = −1.881, signal = −1.482, histogram = −0.399.** MACD has been below its signal line for the *entire* 8/17–9/24 window (it was already 5.83 vs 6.14 on 8/17), and crossed **below zero on 9/9** (+0.118 on 9/8 → −0.421 on 9/9). The MACD line printed its decline low at −2.286 on 9/17, recovered to −1.367 by 9/22, then **rolled back over to −1.881 on 9/24 — a fresh closing low for the move.** The histogram's re-expansion (−0.057 on 9/22 → −0.288 on 9/23 → −0.399 on 9/24) says the late-September stabilization attempt failed. This is a bearish *re-acceleration*, not a bottoming signal.
- **RSI = 44.20.** Mid-lower range, not oversold. It bottomed at **39.45 on 9/16** (its lowest reading of the window) and has oscillated 44–53 since, failing at 52.69 on 9/21. Critically, the 9/16 price low (244.30) came with a *lower* RSI than the 8/27 price low (255.02, RSI 47.23) — **no bullish divergence**. In a strong uptrend RSI at 44 means "room to run lower"; here it means there is roughly 14 points of RSI air down to the 30 line, i.e., price can fall to the 200 SMA without an oversold reading.
- **VWMA = 252.96 and falling for 16 consecutive sessions** from 272.05 on 8/20. Price is 1.41% *below* it. Volume-weighted money has been exiting on every rally since late August. This is the cleanest distribution signature on the board.

---

## 6. Volatility and Volume: Coiled

- **ATR has compressed from 8.12 (8/17) to 5.97 (9/24), −26.5%.** That is a 2.39% daily range — tight for AMZN. Bollinger width (264.07 − 245.20 = 18.87 points, 7.41% of the 254.64 mid) confirms a squeeze.
- Price closed at **249.38, in the lower 22% of the Bollinger envelope** — (249.38 − 245.20) / 18.87 = 22.2%. Not tagged at the lower band (245.20), so no mechanical mean-reversion trigger either.
- **Volume has dried up.** Recent sessions cluster at 24–44M versus 101.8M (7/30) and 129.1M (7/31). The 9/24 reversal candle — open 246.02, low 245.60, close 249.38, i.e. closing at **78% of the day's range** — is constructive but came on **33.0M, below the ~35.4M 20-day average**. Buyers showed up, but not in force. The 9/23 down day, by contrast, traded 44.2M (above average).
- **Conclusion:** compressed range + shrinking volume = energy storage. The break of 244.30 or 261.12 is likely to be resolved with an ATR expansion, and the direction should be taken from the volume on the break, not the break itself.

---

## 7. Actionable Levels and Scenarios

**Reference points (all from tool data):**
- 200 SMA / structural floor: **240.73**, rising
- September low cluster: **244.30** (9/16 low) and **245.60** (9/24 low)
- 61.8% retracement: **~248.56**; current price 249.38
- 10 EMA: **252.53** | VWMA: **252.96**
- 50 SMA / 50% retracement: **256.18 / ~255.34**
- Resistance cluster: **259.49 (9/21 high) – 261.12 (9/4 high)**
- Next shelf: **267.56 (8/28 high)**, then **287.20 (8/3 high)**

**Scenario A — Bear continuation (base case, ~50%):** A daily close **below 244.30** confirms the lower-high/lower-low sequence and opens 240.73 (200 SMA) immediately, with ~235.50 (7/30 close, unfilled gap base) as the second objective. Note the measured move from the 287.20 → 244.30 decline (−42.9 points) projected from the 261.12 lower high gives ~218 — i.e., a full gap fill is not an extreme scenario if 240.73 fails. Invalidated on a close back above 253.

**Scenario B — Range chop (≈30%):** 244.30–261.12 persists. With ATR 5.97, that is a ~2.8 ATR-wide box. Trade only the edges; stop at 1×ATR (~6 points) beyond the boundary. Do nothing between 250 and 258 — that is the middle of no-man's-land where the 10 EMA, VWMA, and 50 SMA are bunched (252.5–256.2).

**Scenario C — Bull reclaim (≈20%):** Requires a **daily close above 256.18 (50 SMA)** *and* above 259.49, ideally with MACD histogram turning positive and volume >45M. That would set up a retest of 267.56, and above it the 8/3 high at 287.20. Note this scenario needs the MACD line (−1.881) to cross back above signal (−1.482) first — it is currently moving the wrong way.

**Risk management specifics:**
- 1×ATR = **5.97 points (2.39%)**; 1.5×ATR ≈ **8.95**; 2×ATR ≈ **11.94**. Size positions so a 1.5–2×ATR stop is ≤1% of equity.
- A stop just under 244.30 from 249.38 is ~5.1 points, *less than* one ATR — too tight for this regime; either use 243.00 (≈1.07×ATR below) or wait for a bounce to 252–253 to enter short with a tighter invalidation.
- Long entry is only justified on a *volume-confirmed* reclaim of 252.96–253.00 (VWMA/10 EMA), stop ~247 (≈1×ATR), first target 256.18, second 259.50. That is roughly 6 points of risk for 6.5–10 points of reward — acceptable only if the volume condition prints.

---

## 8. Bottom Line

AMZN is **bullish on the strategic horizon (200 SMA rising, price +3.59% above it, 50 > 200 SMA) and bearish on the tactical horizon** (price below the 10 EMA, VWMA and 50 SMA; a lower-high sequence from 8/3 through 9/21; MACD re-deepening below zero; VWMA falling 16 straight sessions). The market is compressing (ATR −26.5%) at the 61.8% Fibonacci retracement (~248.56) and just above a two-week double-bottom attempt at 244.3–245.6. **The correct posture is patient and level-driven, not directional:** the next 1–2 ATR expansion out of 244.30–261.12 will define the trade, and the 9/24 hammer's below-average volume means it does not yet qualify as confirmation.

---

## 9. Key Points Summary

| Category | Indicator / Level | Value (2026-09-24) | Reading | Signal |
|---|---|---|---|---|
| Price | AMZN close | 249.38 (O 246.02 / H 250.43 / L 245.60) | Closed at 78% of range; bounce held 61.8% Fib (~248.56) | Neutral-to-constructive single session, unconfirmed |
| Trend – long | close_200_sma | 240.73 (rising from 237.86 on 8/17) | Price +3.59% above; primary uptrend intact | **Bullish** |
| Trend – medium | close_50_sma | 256.18 (peaked 256.29 on 9/23) | Price −2.65% below; first down-tick in the series; rejected repeatedly in Sept (9/11 above, 9/14+ below) | **Bearish** (turning) |
| Trend – short | close_10_ema | 252.53 | Price −1.25% below; 10 EMA crossed below 50 SMA on 9/15, spread now −3.65 | **Bearish** |
| Momentum | macd | −1.881 (zero-cross 9/9) | Fresh closing low for the decline (prior −2.286 on 9/17 is the only deeper print) | **Bearish** |
| Momentum | macds | −1.482 | MACD below signal the entire 8/17–9/24 window; hist re-widening (−0.057 → −0.399) | **Bearish re-acceleration** |
| Momentum | rsi | 44.20 | Bottomed 39.45 on 9/16; no divergence vs 8/27 (47.23); ~14 pts to oversold | Neutral-bearish, not exhausted |
| Volatility | atr | 5.97 (2.39% of price), down 26.5% from 8.12 (8/17) | BB width 7.41% of mid; squeeze conditions | **Breakout pending** |
| Volatility | boll_lb / boll_ub | 245.20 / 264.07 (mid 254.64) | Price in lower 22% of envelope; lower band just under 245.60 low | Mildly bearish, no tag |
| Volume | vwma | 252.96, falling 16 sessions from 272.05 (8/20) | Price −1.41% below; volume-weighted distribution | **Bearish** |
| Volume | 9/24 volume | 33.04M vs ~35.4M 20-day avg | Rally on below-average volume; 9/23 down day 44.2M | Weak conviction in the bounce |
| Structure | Lower highs | 287.20 (8/3) → 267.56 (8/28) → 261.12 (9/4) → 259.49 (9/21) | Four-step descending sequence | **Bearish** |
| Structure | Support cluster | 244.30 (9/16 low) / 245.60 (9/24 low) | Double-bottom attempt, ~70% of 235.50→265.00 gap retraced | Pivot level |
| Structure | Resistance cluster | 259.49–261.12, then 267.56, then 287.20 | Bulls need a close above 256.18 first | Pivot level |
| Risk | Stop sizing | 1×ATR 5.97 / 1.5×ATR 8.95 / 2×ATR 11.94 | Stops under 244.30 are sub-1-ATR — too tight | Use ≥1.07×ATR |
| Trade bias | Net | — | Strategic long, tactical short, range-compressed at a key Fib | **Neutral-bearish; sell rallies into 252.5–256.2, buy only a volume-confirmed reclaim or a 200-SMA flush** |