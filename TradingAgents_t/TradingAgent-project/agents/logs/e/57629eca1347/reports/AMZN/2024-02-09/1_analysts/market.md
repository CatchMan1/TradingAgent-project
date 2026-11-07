# AMZN — Technical & Trend Report (as of close 2024-02-09)

**Source of truth:** verified snapshot 2024-02-09. All indicator values below reconcile exactly with both the `get_indicators` series and the verified snapshot (no discrepancies found).

---

## 1. Headline read

AMZN closed **174.45** on 2024-02-09, up **+2.71%** from 169.84 (Feb 8), on **56.99M** shares. The session traded 170.90 open → 175.00 high → 170.58 low, i.e. a wide-range day that closed in the top ~12% of its range and printed the **highest close and highest intraday high in the entire retrieved sample (2023-06-01 → 2024-02-09)**.

This is a **trend-continuation breakout on expanding volume**, sitting inside a mature, historically stretched uptrend. The indicator set tells one consistent story with one caveat: momentum is strong and *accelerating*, but the stock is simultaneously extended on every mean-reversion yardstick (RSI 72.4, Bollinger ride, +13.3% above the 50-day SMA). That combination argues for **participating on strength/breakout confirmation or on a shallow pullback**, not for chasing a full-size position at 174.

Structure recap:
- **Earnings gap (2024-02-02):** 159.28 → 171.81 close (**+7.87%**), volume **117.2M** (roughly 2.5× the ~45M recent typical). This left an unfilled gap zone between the **Feb 1 high (159.76)** and the **Feb 2 low (167.33)**.
- **Post-gap digestion (Feb 5–8):** closes 170.31 / 169.15 / 170.53 / 169.84 — a tight 4-day box with lows 167.65–168.94 and highs 170.55–171.43. Textbook high-tight flag.
- **Resolution (Feb 9):** breakout to 175.00, close 174.45, +35% volume vs. Feb 8 (42.3M → 57.0M).

---

## 2. Indicator selection and why (8 indicators, complementary, non-redundant)

| Indicator | Role in this context |
|---|---|
| `close_200_sma` | Strategic anchor: confirms the primary uptrend and how far the trend has run |
| `close_50_sma` | Medium-term trend + the key extension/pullback reference for this thrust |
| `close_10_ema` | Short-term momentum + first dynamic support for a fast trend |
| `macd` | Trend/momentum engine, zero-line and slope confirmation |
| `macds` | Crossover trigger to date-stamp the signal (avoids eyeballing) |
| `rsi` | Overbought/stretched condition and divergence watch |
| `boll_ub` | Breakout / "riding the band" detection |
| `boll_lb` | Band-width and volatility asymmetry (mid-band = 20 SMA benchmark) |

Referenced from the verified snapshot but **not** charted separately: **ATR 3.7288** (≈2.14% of price — stop sizing) and **VWMA 163.9803** (volume-confirmation benchmark). Deliberately excluded: `macdh` (derivable from macd−macds, redundant), `boll` mid (≈20 SMA, already proxied), `stochrsi` (duplicates RSI).

---

## 3. Trend structure: fully stacked, unusually wide

All three averages are rising and stacked in perfect bullish order on 2024-02-09:

- **10 EMA = 167.0768** (was 157.2184 on Feb 1 — +6.3% in six sessions)
- **50 SMA = 154.0036** (was 143.4762 on Jan 2 — +7.3% over ~5 weeks)
- **200 SMA = 135.6057** (was 127.9832 on Jan 2 — +6.0%)

Price sits **+4.41% above the 10 EMA**, **+13.28% above the 50 SMA**, and **+28.65% above the 200 SMA**. The 50/200 spread has widened to **18.40 points** (154.00 vs 135.61), from 13.56 on 2023-11-13 (133.16 vs 119.59) — the trend is not merely intact, it is *broadening*. 10 EMA minus 50 SMA = **+13.08 points (+8.5%)**, a wide short-term-to-medium-term spread typical of a late-stage thrust rather than an early-stage basing move.

**Important caveat on extension:** within the visible 50-SMA series (starting 2023-11-13), Friday's **+13.28%** premium is the most stretched reading on record in the sample, essentially tied with Feb 2's +13.36%. By contrast Jan 29 was +7.36% and Dec 18 was +10.51%. Extension, not trend, is the risk here.

**Precedent for what happens after stretch (tool-supported):** RSI peaked at 68.05 on 2023-12-18 (close 154.07) and price then ground sideways-to-down for ~2.5 weeks, bottoming at a **144.05 intraday low on 2024-01-04** (close 144.57) — a **−6.17%** drawdown from the Dec 18 close. That is the most recent analog of a stretched tape resolving via time/price consolidation rather than collapse.

---

## 4. Momentum: MACD re-accelerating, not diverging

| Date | MACD | Signal | Histogram |
|---|---|---|---|
| 2023-12-22 | 3.1360 | 2.8731 | +0.263 |
| 2024-01-05 | 0.8587 | 2.0889 | −1.230 |
| 2024-01-19 | 1.6928 | 1.5838 | +0.109 (re-cross) |
| 2024-02-01 | 2.4503 | 2.2844 | +0.166 |
| 2024-02-02 | 3.4647 | 2.5204 | +0.944 |
| 2024-02-05 | 4.1003 | 2.8364 | +1.264 |
| 2024-02-06 | 4.4590 | 3.1609 | +1.298 |
| 2024-02-07 | 4.7993 | 3.4886 | +1.311 |
| 2024-02-08 | 4.9562 | 3.7821 | +1.174 |
| **2024-02-09** | **5.3904** | **4.1038** | **+1.287** |

Signal sequence supported by the data:
1. MACD crossed **below** signal on 2023-12-29 (2.7820 vs 2.9230) into the January chop.
2. Re-crossed **above** on **2024-01-19** (1.6928 vs 1.5838) — the currently live bullish crossover.
3. MACD has risen **every session** since Feb 1 and is now **5.3904**, the highest print in the entire visible window (prior peak 3.1360 on 2023-12-22), and comfortably above the zero line.

Nuance worth flagging: the histogram *cooled* from 1.311 (Feb 7...) — specifically 1.298 on Feb 6 → 1.311 on Feb 7 → **1.174 on Feb 8** — before re-expanding to **1.287** on Feb 9. That one-day dip coincided exactly with the Feb 7–8 consolidation and was then resolved by the breakout. No bearish MACD divergence exists against price at the Feb 9 high; momentum confirmed the new high. That is the strongest single bull argument in this report.

---

## 5. RSI: genuinely overbought, with a recent warning shot

- **2024-02-09: 72.43** — above the 70 threshold.
- The current leg's pattern: **70.41 (Jan 29)** → 63.09 (Jan 30) → **53.10 (Jan 31)** → 60.36 (Feb 1) → **73.78 (Feb 2)** → 70.69 → 68.31 → 69.62 → 68.11 → **72.43 (Feb 9)**.

Two readings of this:
- **Bullish:** RSI reset from 73.78 to 68.1 during the Feb 5–8 flag *without* a price breakdown, then re-accelerated on the breakout. That "overbought → cool → re-overbought" path is characteristic of trend continuation, not of a blow-off top.
- **Cautionary:** RSI has now made back-to-back excursions above 70 (Feb 2 and Feb 9) while RSI 73.78 on Feb 2 was *not* exceeded on Feb 9 despite a higher closing price. That is a **very early, unconfirmed negative divergence (price higher high, RSI marginally lower high)**. It is one data point and inside a strong trend — RSI can stay >70 for weeks — but it means "buy the breakout with a stop," not "buy with impunity."

Note also the Jan 29–31 episode: RSI 70.41 → 53.10 in two sessions while price fell 161.26 → 155.20 (−3.76%). That shows how fast sentiment can flip in this name at these levels.

---

## 6. Bollinger Bands: breakout plus volatility expansion

- **Upper band 175.4099**, **lower band 145.9601**, implied mid (20 SMA) **160.6850**.
- Close 174.45 is **0.96 points (0.55%) below the upper band**, and **+8.57% above the mid band**.
- **Band width = 29.45 points = 18.33%** of the mid band, up from **8.22%** on 2024-01-12 (157.67 upper / 145.22 lower / 151.45 mid). Volatility has more than doubled in under a month.

Upper band trajectory: 163.0982 (Feb 1) → 166.3346 (Feb 2) → 168.2833 (Feb 5) → 169.8912 (Feb 6) → 171.6704 (Feb 7) → 173.1157 (Feb 8) → **175.4099 (Feb 9)**. The band is expanding upward at ~1.1–2.3 points/day — a directional volatility regime, not a squeeze.

Interpretation: price is **walking/riding the upper band**, which in strong trends is a *continuation* signal — but the lower band at **145.96** being 16.6% below spot tells you the two-sided risk. A normal "band-touch to mid-band" mean reversion would target **~160.7**, which coincides closely with the **VWMA 163.98** and the unfilled earnings gap zone (**159.76–167.33**). That confluence is the highest-value downside reference on the chart.

---

## 7. Volume and volume-weighted confirmation

- **VWMA = 163.9803** vs price 174.45 → price is **+6.39% above** the volume-weighted average. VWMA sits *above* the implied 20-SMA (160.685), which means the volume-weighted price is higher than the simple average — up-days carried heavier volume than down-days. That is genuine accumulation, not just price drift.
- **Feb 2: 117.2M** on the +7.87% earnings gap; **Feb 9: 57.0M** (+34.7% vs Feb 8's 42.3M) on the breakout. The pattern is *expansion on up-thrusts*, contraction during the Feb 5–8 flag (42.3M–55.1M), then re-expansion at the resolution. Classic accumulation footprint.
- **Snapshot MFI = 0.6336.** Flag: this vendor reports MFI on a 0–1 scale, i.e. roughly **63.4** — *below* an 80 overbought reading. So money-flow is strong but **not** confirming extreme exhaustion, which partially offsets the RSI/Bollinger extension concern.

---

## 8. Volatility and risk sizing

- **ATR = 3.7288 = 2.14% of the 174.45 close.** Recent daily ranges corroborate: Feb 9 = 4.42, Feb 2 = 5.17, Feb 6 = 3.06, Feb 8 = 2.55, Feb 7 = 1.94.
- Volatility is elevated (post-earnings), so position size should be scaled down vs. a quiet regime: a 2×ATR stop is **7.46 points**, i.e. ~4.3% of price.

---

## 9. Actionable map: levels, scenarios, and triggers

**Resistance**
- **175.00** — Feb 9 high; also the highest high in the retrieved sample. Nothing above it in-sample, so use round-number/measured-move logic beyond (~180) rather than calling it "resistance."
- 171.43–172.50 — Feb 2 high 172.50 / Feb 8 high 171.43 (now support once reclaimed).

**Support (in order)**
1. **170.58** — Feb 9 low (tightest stop reference for the breakout trade).
2. **167.65–167.08** — Feb 5 low (167.65) and the 10 EMA (167.0768). This is *the* line in the sand for the short-term trend.
3. **163.98 (VWMA)** — volume-weighted trend benchmark.
4. **159.76–167.33** — unfilled Feb 2 earnings gap; also brackets implied 20-SMA at 160.685.
5. **155.20 / 154.81** — Jan 31 close / Jan 31 low; ~equal to **50 SMA 154.0036**.
6. **145.96** — Bollinger lower band (stress case).

**Bullish continuation (base case, ~60% weight given trend/volume/MACD)**
- Trigger: hold above 170.58 and reclaim/close above **175.00** on ≥55M volume.
- Invalidation: a close back below **167.08** (10 EMA) breaks the current thrust's momentum character.
- Stop logic: 2×ATR from 174.45 = **166.99**, which sits just under the 10 EMA and inside the Feb 5 low — a coherent structural stop rather than an arbitrary one.

**Preferred entry, if not already long**
- **Do not chase full size at 174.45** (+13.3% above 50 SMA, 0.55% under the upper band). Two viable tactics:
  - *Scale-in on strength:* starter position above 175.00 with stop 166.99 (risk 7.46 ≈ 4.3%).
  - *Buy the pullback:* first add zone **167–168** (10 EMA / Feb 5 low), second add **164** (VWMA). A pullback of ~1×ATR (to ~170.7) is routine; a pullback of ~2×ATR (~167) would still leave the uptrend fully intact.

**Bearish / mean-reversion scenario (secondary, ~40%)**
- Catalysts are technical, not fundamental: RSI 72.4 with a nascent price-vs-RSI divergence, price at the upper band, +13.28% above the 50 SMA, and an 18.3% band width.
- Confirmation would be: close below 167.08 → then below 163.98 (VWMA). Target one = **160.69** (20-SMA / Bollinger mid), which overlaps the **159.76–167.33** gap. Target two = **154.00** (50 SMA). That path would be roughly a **−7.9% to −11.7%** drawdown from 174.45 — materially larger than the −6.17% Dec 18→Jan 4 analog, so size accordingly.

**What would flip the bias**
- MACD histogram turning negative (currently **+1.287**) while price makes a higher high — the clearest objective divergence sell signal.
- A high-volume close back inside the Feb 5–8 box (below 169.15) that traps the Feb 9 breakout buyers.
- Conversely, RSI pushing decisively above 73.78 (the Feb 2 peak) alongside a new price high would invalidate the nascent divergence and support chasing.

---

## 10. Summary table

| Dimension | Reading (2024-02-09) | Signal | Actionable takeaway |
|---|---|---|---|
| Close / OHLCV | 174.45; O 170.90 H 175.00 L 170.58; 56.99M | Bullish (new sample high, strong close) | Breakout confirmed on +34.7% volume vs Feb 8 |
| 10 EMA | 167.0768 (from 157.2184 on Feb 1) | Bullish, steep | First dynamic support; stop just below ≈166.99 |
| 50 SMA | 154.0036 (price **+13.28%**) | Bullish trend / **extended** | Most stretched premium in sample; avoid full-size chase |
| 200 SMA | 135.6057 (price **+28.65%**) | Primary uptrend intact | Strategic long bias; 50/200 spread widening (18.40) |
| MACD / Signal | 5.3904 / 4.1038; hist **+1.287** | Strongly bullish, no divergence | Highest MACD in sample; live cross since 2024-01-19 |
| RSI | **72.43** (peak 73.78 on Feb 2) | Overbought, early divergence risk | Trend can persist >70; use stops, not discretion |
| Bollinger UB / LB | 175.4099 / 145.9601 (mid 160.685) | Band ride + vol expansion (width 18.33% vs 8.22% on Jan 12) | Price 0.55% under UB; mean-revert target 160.69 |
| ATR | 3.7288 (2.14%) | Elevated volatility | 2×ATR stop = 7.46 pts; reduce position size |
| VWMA | 163.9803 (price **+6.39%**) | Volume-weighted accumulation | Above 20-SMA ⇒ up-volume dominance; pullback magnet |
| MFI | 0.6336 (≈63.4 on 0–100; **scale flag**) | Positive, not overbought | Offset to RSI/Bollinger exhaustion risk |
| Key support | 170.58 / 167.65–167.08 / 163.98 / 159.76–167.33 / 154.00 | — | Escalating invalidation ladder |
| Key resistance | 175.00 (sample high) | — | No in-sample resistance above; use measured moves |
| Leverage caveat | Feb 2 gap 159.28→171.81 (+7.87%) unfilled | Two-sided risk | Gap zone 159.76–167.33 is the reversion target |
| **Net bias** | **Bullish trend, extended entry** | **Buy strength in tranches or buy 167–168 dip** | Stop 166.99 (2×ATR); first target >175.00 |

*Data notes: the 50-SMA premium history is bounded by the indicator series start (2023-11-13); "highest in sample" refers to the retrieved window 2023-06-01 → 2024-02-09 and is not an all-time-high claim. MFI's 0–1 scaling is the vendor's convention — flagged rather than converted silently. All price/indicator levels above match the verified snapshot exactly.*