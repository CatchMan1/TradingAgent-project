# AMZN — Multi-Factor Technical Assessment (as of 2024-02-20 close)

## 1. Data integrity check

I first pulled the full OHLCV series (2023‑08‑01 → 2024‑02‑20) and then the verified snapshot. The snapshot's latest row and its indicator panel **match the indicator pulls exactly** (e.g., `close_50_sma` 156.857, `macd` 4.2288, `macds` 4.6151, `macdh` −0.3864, `rsi` 55.909, `boll` 165.447 / `boll_ub` 178.379 / `boll_lb` 152.515, `atr` 3.803, `vwma` 168.073). **No discrepancy to flag** between sources. One data-quality caveat: the three consecutive closes of 125.980 (2023‑09‑26 → 09‑28) are a vendor artifact and are excluded from any inference. Also note 2024‑02‑19 was a U.S. market holiday — there is correctly no bar between 02‑16 and 02‑20.

Verified latest bar (2024‑02‑20): **O 167.83 / H 168.71 / L 165.74 / C 167.08**, volume **41,980,300**.

---

## 2. Where AMZN stands in the primary trend

**The long-term and intermediate trend are unambiguously up, and the short-term trend has rolled over inside that uptrend.**

- `close_200_sma` = **137.55**, rising steadily (~+0.32/session since late January). Price is **+21.5% above** it.
- `close_50_sma` = **156.86**, rising ~+0.45/session. Price is **+6.5% above** it. The 50 SMA sits **~19.3 points above** the 200 SMA and the gap is *widening* — a classic, mature golden-cross configuration, i.e., trend confirmation rather than a fresh signal.
- `close_10_ema` = **168.64**. The close of 167.08 is **−0.92% below** it, and the 10 EMA has flattened (168.99 on 02‑16 → 168.64 on 02‑20) after a steep ascent. This is the first structural crack: the fastest average has stopped rising and price has lost it.

Direction of travel over the run: 2023‑10‑26 close **119.57** → 2024‑02‑12 close **172.34** = **+44.1%** in ~3.5 months. The 02‑20 close is **−3.05%** from that 02‑12 peak close and **−4.7%** from the 02‑12 intraday high of **175.39**.

---

## 3. The event that defines the current regime: the 2024‑02‑02 earnings gap

- 02‑01 close: **159.28**
- 02‑02 open: **169.19**, close **171.81**, volume **117,218,300** — the largest volume print in the entire 140‑session sample.

That is a **+7.87% close-to-close gap** on record volume. Everything since is *post-gap price discovery*, and the relevant frame is not "is AMZN in an uptrend" (it is) but "is the gap holding, and is the gap being digested at the upper or lower end of its range?"

Post-gap range so far: **low 165.75 (02‑13) — high 175.39 (02‑12)**. At 167.08, AMZN is trading in the **lower quarter** of that range.

**Critical observation:** the 02‑20 low was **165.74** versus the 02‑13 low of **165.75** — a near-exact retest of the post-earnings floor, which held and was bought back to a close of 167.08. That level also coincides with the `boll` middle band at **165.45**. So **165.45–165.80 is a genuine, tool-verified confluence support**, tested twice.

---

## 4. Momentum: deterioration is measurable and sequential

I deliberately selected **both** `macd` and `macdh` because the crossover *and* the rate of change matter here.

- `macd` peaked at **5.5008** on 2024‑02‑12 and has fallen for four straight sessions to **4.2288** on 02‑20.
- `macds` (signal) is still *rising* to **4.6151** — it lags.
- `macdh` went **+0.2028 (02‑15) → −0.0389 (02‑16) → −0.3864 (02‑20)**. The **bearish MACD crossover occurred on 2024‑02‑16**, and the histogram has since **deepened nearly 10×**. Momentum is not merely flat; it is accelerating to the downside.

- `rsi` = **55.91**, down from **72.43 (02‑09)** and **73.78 (02‑02)**. It has fully unwound the overbought condition without reaching oversold. Note the **mild bearish RSI divergence**: price printed a *higher* high on 02‑12 (175.39 vs 175.00 on 02‑09) while RSI *fell* (67.90 vs 72.43) — supply was entering at the highs.

Important nuance: in this trend, RSI in the **40–50** zone has been a reload area rather than a sell signal (2024‑01‑04: RSI 40.23 at close 144.57, followed by a rally to 175.39 by 02‑12). At 55.9 there is still **substantial room to cool off before the trend structure is threatened.**

---

## 5. Volatility and Bollinger structure: bands are wide, and the lower band is racing up

- `boll_ub` = **178.38** (peaked 178.58 on 02‑16 — the upper band has stopped expanding).
- `boll` = **165.45**; `boll_lb` = **152.52**.
- Bandwidth = **15.6% of price** — extremely wide, a direct consequence of the earnings gap. Bollinger bandwidth does not mean "about to break out"; here it means **mean-reversion mechanics dominate**: the **lower band surged from 145.96 (02‑09) to 152.52 (02‑20)** as pre-gap data rolled out of the 20‑day window. The band is *rising to meet price*, not price falling to the band. The 02‑20 close is only **+0.99% above the middle band**.
- `atr` = **3.803**, up from ~**2.95** in late January, = **2.28% of price**. Post-earnings, AMZN is ~29% more volatile per day than it was pre-gap. Position sizes must be cut accordingly; stops set off pre-earnings ATR will be whipsawed.

Two more cross-checks from the same framework:
- `vwma` = **168.07**. Price at 167.08 is **−0.59% below** the volume-weighted average — meaning the **average dollar-weighted buyer since the gap is marginally underwater**. That is a mild distribution tell and confirms 168.1 as immediate supply.
- Volume: 02‑20's **41.98M** is roughly **14% below** the ~48.6M average of the 11 sessions since 02‑02 (ex-earnings-day). A pullback on **contracting** volume is *constructive consolidation*, not aggressive liquidation — the one genuinely bullish offset to the bearish momentum picture. The counterweight: 02‑13's **−2.2% session on 56.35M** (the highest volume since the gap) shows real profit-taking existed.

---

## 6. Actionable playbook

**Base case: bullish digestion, not distribution — but not yet a buy.** The trend stack (price > 50 SMA > 200 SMA, both rising) is intact; the drawdown is −3.1% from the swing close and is occurring on shrinking volume. However, three short-term signals — price below the 10 EMA, a fresh and deepening MACD bearish cross, and price below VWMA — argue against adding exposure *at* 167.08. The trade is to buy the *confirmation of the hold*, not the anticipation of it.

**Scenario A — Bullish resumption (preferred):**
- Trigger: a close back above the **10 EMA (168.64)** and then above **169.51** (02‑16 close), ideally on volume > 50M.
- Confirmation: `macdh` turns back positive (i.e., MACD reclaims 4.62).
- Targets: **172.34** (02‑12 close) → **175.39** (02‑12 high). A decisive close above 175.39 breaks the post-gap range and voids the short-term top.
- Stop: below **165.45** (Bollinger middle / double-test low).

**Scenario B — Support fails (risk case):**
- Trigger: a close below **165.45–165.80** on expanding volume. That invalidates the double-test and signals the earnings gap is being sold.
- Next zones: **159.28–159.76** (02‑01 close and 02‑01/02‑02 gap origin — the gap-fill magnet), then **156.86** (rising 50 SMA). Note this is a **single, wide air-pocket** — there is no volume shelf between 165.5 and 159.3, so a break could move fast.

**Risk management (ATR-based, using the verified ATR of 3.803):**
- Stop distance of **1.5× ATR ≈ 5.7 pts**, or ~2× ATR ≈ 7.6 pts for swing positions.
- With a conservative 1% account risk and a 5.7‑pt stop, position size = 0.175% of account per share price unit — i.e., **cut pre-earnings position sizes by roughly 25–30%** to keep dollar risk constant versus January volatility.

**What would flip me bearish on the intermediate trend:** a weekly close below the 50 SMA (156.86) — that level is ~6.5% away and rising, so it is not imminent. **What would flip me aggressively bullish:** a volume-confirmed reclaim of 175.39.

---

## 7. Why these eight indicators (complementarity, not redundancy)

| Slot | Indicator | Unique job in this setup |
|---|---|---|
| 1 | `close_10_ema` | Times the short-term stall — price is below it for the first time since early February |
| 2 | `close_50_sma` | Defines the swing-trend floor (156.86) and its rising slope confirms the trend is not broken |
| 3 | `close_200_sma` | Confirms the strategic regime (golden-cross, +21.5% above) and filters out short-term noise |
| 4 | `macd` | Establishes the bearish crossover versus the signal line and the peak-to-now decay (5.50→4.23) |
| 5 | `macdh` | Measures *acceleration* of that decay (−0.04 → −0.39) — catches the rollover earlier than the lines alone |
| 6 | `rsi` | Quantifies the overbought unwind (73.8 → 55.9) and the mild price/RSI divergence at the 02‑12 high |
| 7 | `boll_ub` | Prices a wide-band, post-gap regime and shows the upper band has stopped expanding at ~178 |
| 8 | `atr` | Sizes stops/positions for a 2.28%/day volatility regime (3.80 vs 2.95 pre-earnings) |

Supplemented (not part of the core eight) by `boll`/`boll_lb` for mean-reversion geometry and `vwma` as a volume-weighted cost-basis check — both independently corroborated the same conclusion.

---

## 8. Key points summary

| Dimension | Verified reading (2024‑02‑20) | Signal | Interpretation / Action |
|---|---|---|---|
| Latest bar | O 167.83 / H 168.71 / L 165.74 / C 167.08; vol 41.98M | Neutral | Lower half of post-gap range; volume ~14% below post-gap average |
| Primary trend | 50 SMA 156.86 (rising); 200 SMA 137.55 (rising); price +21.5% above 200 | **Bullish** | Golden-cross regime intact; no trend break |
| Short-term trend | Close 167.08 vs 10 EMA 168.64 (−0.92%) | **Bearish** | First loss of the 10 EMA since early Feb; 10 EMA flattening |
| MACD | 4.2288 vs signal 4.6151; hist −0.3864 | **Bearish** | Crossover on 02‑16; histogram deepened ~10× in two sessions |
| RSI | 55.91 (from 73.78 on 02‑02) | Neutral/weakening | Overbought fully unwound with room to 40–50 without trend damage; mild divergence at 02‑12 high |
| Bollinger | Mid 165.45 / UB 178.38 / LB 152.52; bandwidth 15.6% | Neutral | Wide post-earnings bands; LB racing up (145.96→152.52) = band moving to price |
| ATR | 3.803 (2.28% of price), vs ~2.95 in late Jan | Elevated | Halve/trim size; stops at 1.5×ATR ≈ 5.7 pts |
| VWMA | 168.07 | Mild bearish | Average post-gap buyer is marginally underwater; immediate supply at 168.1 |
| Key support | 165.45–165.80 (Boll mid + 02‑13 low 165.75 + 02‑20 low 165.74) | Pivot | Double-tested; break opens air-pocket to 159.28–159.76, then 50 SMA 156.86 |
| Key resistance | 168.64 (10 EMA) → 169.51 → 172.34 → 175.39 | Pivot | Reclaim of 175.39 on volume voids the short-term top |
| Bias | Bullish consolidation, unconfirmed | **Hold / buy-the-confirmation** | Wait for a close > 168.64–169.51 to add; invalidate below 165.45 |