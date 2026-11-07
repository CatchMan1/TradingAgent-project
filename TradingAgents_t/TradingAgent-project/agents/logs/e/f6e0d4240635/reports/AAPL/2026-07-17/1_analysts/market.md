# AAPL — Technical Deep-Dive Report (as of 2026-07-17)

## 1. Market Context Summary

AAPL is trading in a **confirmed, accelerating uptrend** following a violent mid-June shakeout and a rapid V-shaped recovery. Price closed at **333.74** on 2026-07-17 (session range 329.00–334.99, volume ~63.4M), which is right at the top of the recent range and just beneath the 2026-07-16 high of **334.68** and the 2026-07-17 intraday high of **334.99**. The structure — price above the 10 EMA above the 50 SMA above the 200 SMA, all rising — is the textbook bullish stack, but short-term extension metrics (RSI, distance from moving averages) argue for tactical patience rather than indiscriminate chasing.

**Indicator selection rationale (8 chosen, complementary, non-redundant):**
- `close_10_ema`, `close_50_sma`, `close_200_sma` — three time horizons of trend/support without overlap.
- `macd` + `macdh` — crossover *state* plus momentum *rate of change* (histogram); I skipped the separate signal line to avoid redundancy since the histogram encodes the spread.
- `rsi` — overbought/oversold and momentum-failure detection, especially relevant after the June momentum break.
- `atr` — volatility-scaled stops and position sizing; ATR has changed materially (5.6 → 8.1) so this is essential.
- `vwma` — volume-weighted confirmation of whether the breakout is being bought by real flow or is thin.
- (Bollinger bands from the verified snapshot used for extension context; avoided duplicating with `boll` since the middle line ≈ overlapping the 20 SMA already implied by trend stack.)

---

## 2. Trend Structure — Bullish and Intact

| Metric (2026-07-17) | Value | Price vs. Level |
|---|---|---|
| Close | 333.74 | — |
| 10 EMA | 319.73 | +4.4% above |
| 50 SMA | 302.65 | +10.3% above |
| 200 SMA | 274.22 | +21.7% above |
| VWMA | 310.27 | +7.6% above |

- **10 EMA** has turned up sharply: 291.02 (2026-06-26) → 308.52 (2026-07-13) → **319.73** (2026-07-17). This is the fastest legitimate "trend re-acceleration" signal available.
- **50 SMA** has risen every session since late March (260.05 on 2026-03-30 → **302.65** today) and is now ~28 points (≈10%) below price. The 50/200 spread (+28.4 points, 50 > 200) confirms the long-term **golden-cross regime** remains in force; the 200 SMA itself is grinding higher (246.6 in mid-March → 274.2 today).
- The **order of the stack (price > 10 EMA > 50 SMA > 200 SMA)** with all slopes positive is the highest-conviction configuration for trend-following.

**Caveat:** price sitting 10.3% above the 50 SMA and 7.6% above the VWMA is statistically stretched. In healthy trends this is resolved either by time (sideways drift) or shallow price pullbacks toward the 10 EMA — not necessarily by trend reversal.

---

## 3. Momentum — Rebuilt From a Deep Break, Now Expanding

**MACD journey (source of truth: indicator series):**
- MACD line rolled over in early June: 10.39 (2026-05-29) → 0.17 (2026-06-24) → **-2.92** trough (2026-06-29).
- It crossed **above zero on 2026-07-06** (0.88) and has risen every session since: 5.24 (07-13) → 7.87 (07-16) → **8.82** (07-17).
- The **histogram flipped positive on 2026-07-02** (+0.26) after bottoming at -2.79 on 2026-06-25, and is expanding again into month-end: 2.33 (07-14) → 2.77 (07-15) → 3.23 (07-16) → **3.34** (07-17).

This is a fresh, early-stage momentum thrust (histogram positive ~11 sessions), not a late-stage exhausted one. The one-week dip in the histogram on 07-13/07-14 was immediately re-expanded — evidence buyers absorbed the first round of profit-taking near 315–317.

**RSI:** 71.65 — just crossed the 70 overbought line (68.77 on 07-15, 71.43 on 07-16, 71.65 today). Context matters enormously here:
- Late May, RSI ran at **78–80** (peak 79.79 on 2026-05-28) and price subsequently fell from 315.20 (2026-06-02 close) to 275.15 (2026-06-25 close), a **-12.7% drawdown**, with RSI bottoming at **32.2** on 2026-06-25.
- Today's overbought reading is far less extreme than that May episode. In strong trends RSI can hold >70 for weeks — the tool data shows a prior instance of ~9 sessions above 70 before the break. Treat 70 as a **"reduce chase size" flag, not a sell signal**, but watch for bearish divergence (price higher highs without RSI higher highs).

---

## 4. Volatility — Regime Has Widened; Size Stops Accordingly

- **ATR (14) = 8.13** (~2.4% of price), up from ~5.6 in late May and a peak of 8.74 on 2026-07-02. The June 25 crash day (-6.1% close-to-close: 293.08 → 275.15) with 107M volume, followed by 261.8M volume on 2026-06-26 (+3.1% close), permanently raised the volatility regime.
- **Bollinger context (verified snapshot):** middle 305.52, upper 339.20, lower 271.83. Close (333.74) sits inside the upper band but ~1.6% below it — riding the band in a strong trend, *not* a band thrust/breakout extension. Band width ≈ 22% of the middle line, confirming the wide-volatility regime.
- **Practical implication:** fixed-point stops are hazardous at this ATR. A 2×ATR stop ≈ **16 points**. A volatility trailing stop beneath the 10 EMA (319.73) is roughly 14 points of room, consistent with 1.7×ATR.

---

## 5. Volume Confirmation — The Breakout Is Being Bought

- **VWMA = 310.27**, up sharply from 296.42 (2026-07-15) in two sessions — a large single-day VWMA jump implies heavy volume-weighted buying near the highs, not low-volume drift.
- Daily volume during the thrust: **61.0M** (07-15, +4.0% day), **63.0M** (07-16), **63.4M** (07-17) vs. a more typical 35–50M in the June/July base. Rising price + rising volume = accumulation-style confirmation.
- The July 2 breakout day (close 308.63, +4.8% from 294.38 on 2026-07-01, volume 75.4M) was the volume ignition; subsequent sessions have held above that breakout level, consistent with a valid breakout rather than a failed one.
- **MFI ≈ 0.895** (0-1 scaled money-flow index from the snapshot) — money flow is in overbought territory, echoing RSI. Flow is strong but stretched.

---

## 6. Key Levels & Actionable Playbook

**Resistance:**
- **334.68 / 334.99** — 2026-07-16 close-high and 2026-07-17 intraday high; immediate ceiling.
- **339.20** — upper Bollinger Band; a decisive close above would signal trend acceleration (but also deeper overbought territory).

**Support (layered):**
- **~319.7** — 10 EMA; first pullback zone in a healthy trend.
- **~308.6–315.2** — the 2026-07-02 breakout close (308.63) and June 2 high close (315.20) zone; prior resistance-turned-support.
- **~310.3** — VWMA, sitting right on the breakout shelf — notably confirming that average volume-weighted holders are in profit only above ~310.
- **~302.6–305.5** — 50 SMA and Bollinger middle converge; this is the trend's "line in the sand."

**Actionable ideas:**

1. **Trend-followers already long:** hold; trail stops beneath the 10 EMA (319.73) or at 2×ATR ≈ 16 points. A close below 308.63 (breakout invalidation) would argue for a material de-risking.
2. **New entries:** chasing at 333–335 with RSI 71.6 and price 10% above the 50 SMA is poor risk/reward. Preferred zones: a controlled pullback toward **319–322** (10 EMA) or the **308–315** breakout shelf, ideally on declining volume. A breakout confirmation close above **335.00** on >60M volume is an alternative momentum entry.
3. **Swing/volatility positioning:** with ATR 8.13, scale position size ~45% smaller than in the low-vol May regime (5.6 ATR) for the same dollar risk.
4. **Momentum-failure tripwires (based on the June template):** watch for (a) MACD histogram contracting for 3+ sessions, (b) RSI making a lower high versus the 07-17 print, or (c) a high-volume close back below the 10 EMA. In June, the warning sequence began with RSI sliding from ~80 while price was still making marginal highs — divergences preceded the -12.7% move by several sessions.
5. **Upside scenario:** if price closes above 339.20 (upper band) with the histogram still expanding, the "ride the band" regime could extend toward ~350 (current close + 2×ATR), but that would occur at RSI >75 and would warrant tighter trailing management.

**No data conflicts to flag:** the verified snapshot (close 333.74; RSI 71.65; MACD 8.82/5.48/3.34; 50 SMA 302.65; 200 SMA 274.22; 10 EMA 319.73; VWMA 310.27; ATR 8.13; bands 271.83/305.52/339.20) matches the per-indicator series exactly.

---

## 7. Key Points Table

| Dimension | Reading (2026-07-17) | Interpretation | Actionable Takeaway |
|---|---|---|---|
| Price | Close 333.74; H 334.99 | At highs, testing 334.68–335.00 ceiling | Breakout confirmation needs close >335 on >60M vol |
| Trend stack | 10 EMA 319.73 < Px; 50 SMA 302.65; 200 SMA 274.22; all rising | Strong bullish stack, golden-cross regime | Primary trend up; trade with it, don't fade it |
| Extension | +10.3% vs 50 SMA; +4.4% vs 10 EMA; +7.6% vs VWMA | Short-term stretched | Prefer buy-the-dip zones 319–322 / 308–315 |
| MACD | 8.82 vs signal 5.48; hist +3.34 and expanding | Fresh momentum thrust since 07-02 zero-cross (07-06) | Momentum healthy; watch for histogram contraction |
| RSI | 71.65 (70 crossed 07-16) | Overbought, but mild vs May's 79.8 peak | Not a sell signal; reduce chase size; watch divergence |
| Volatility | ATR 8.13 (~2.4%); Boll UB 339.20 / LB 271.83 | Elevated, post-June regime | 2×ATR stop ≈16 pts; downsize ~45% vs May regime |
| Volume/flow | Breakout days 61–75M vol; VWMA 310.27 rising; MFI ~0.90 | Breakout volume-confirmed but flow overbought | Trend credible; avoid adding on low-volume stalls near 335 |
| Risk levels | Support 319.7 / 308.6–315.2 / 302.6–305.5; Resist 335 / 339.2 | Layered support structure below | Invalidation = close <308.63 (07-02 breakout close) |
| June template | -12.7% (315.20 on 06-02 → 275.15 on 06-25); 261.8M vol on 06-26 bounce | Shows how fast this name can correct | Hard risk rules required despite bullish structure |

**Bottom line for AAPL:** the technical picture is decisively bullish — confirmed breakout, expanding momentum, and volume-backed buying — but the entry timing is stretched (RSI >70, double-digit premium to the 50 SMA). The highest-probability strategy is to stay long/trail stops while waiting for pullbacks into the 319–322 or 308–315 zones to add, with a hard invalidation at a close below the 308.63 breakout level and position sizes calibrated to the new ATR-8 volatility regime.