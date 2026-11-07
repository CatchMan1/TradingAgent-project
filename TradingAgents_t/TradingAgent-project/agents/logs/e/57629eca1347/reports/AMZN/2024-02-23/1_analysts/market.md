# AMZN — Multi-Timeframe Technical Assessment (as of session close 2024‑02‑23)

**Verification note:** Every exact price/indicator figure below was cross-checked against `get_verified_market_snapshot` (curr_date 2024‑02‑23). The snapshot, `get_stock_data`, and `get_indicators` outputs are fully consistent (latest close 174.99; 50SMA 158.42; 200SMA 138.56; 10EMA 170.67; MACD 4.325 vs signal 4.401; RSI 65.75; ATR 3.797; VWMA 170.66). One caveat: the snapshot reports `mfi` as **0.445475**, which is almost certainly a 0–1 normalization (~44.5 on a 0–100 scale) rather than a raw reading — I treat it only as "neutral money flow," not as a precise level, and flag it as a scale discrepancy rather than reconciling it.

---

## 1. Indicators selected (8) and why

| Indicator | Role in this specific context |
|---|---|
| `close_50_sma` | Primary medium-term trend spine and the *dynamic support* reference for a stock that is extended above its averages |
| `close_200_sma` | Long-term regime/golden-cross confirmation; anchors how stretched price is (26% above) |
| `close_10_ema` | Timing tool for the tight 2–4 day pullback rhythm seen in Feb 2024 |
| `macd` | Measuring whether the new price high is momentum-confirmed |
| `macds` | Crossover trigger; documents the mid-Feb whipsaw |
| `rsi` | Overbought / divergence check (price made a higher high; RSI did not) |
| `atr` | Volatility regime shift post-earnings → stop distance and position size |
| `vwma` | Confirms whether the breakout is volume-backed (price vs volume-weighted mean) |

Deliberately excluded: `boll`/`boll_ub`/`boll_lb` and `macdh` were **not** selected as primary indicators (band values are used only as snapshot context to avoid double-counting "distance from mean"), and no momentum oscillator is duplicated (RSI only, no stochastic).

---

## 2. Trend structure: clean, mature, and now accelerating again

**Price vs averages (2024‑02‑23 close 174.99):**

- **10 EMA 170.67** → price is **+2.53%** above it (short-term bullish, not yet stretched).
- **50 SMA 158.42** → price is **+10.47%** above it.
- **200 SMA 138.56** → price is **+26.29%** above it (long-term extension, the main structural risk).
- **50 SMA − 200 SMA = +19.85 pts = +14.33%** → textbook golden-cross configuration, and the spread is *widening*, which is trend-strengthening rather than trend-exhausting.

**Slope evidence (tool-derived):**
- 50 SMA: 150.52 (2024‑01‑30) → 158.42 (2024‑02‑23) = **+7.90 pts in 17 sessions (~+0.46/session)**, and it has risen on **every single session** in the visible window from 2023‑10‑26 (132.31) onward — no flattening whatsoever.
- 200 SMA: 133.06 (2024‑01‑30) → 138.56 (+5.50 over the same 17 sessions, ~0.32/session). The 50 SMA is rising ~1.4x faster than the 200 SMA → spread widening, confirmed.

**Swing structure:** Higher lows throughout the recovery — 119.57 close (2023‑10‑26) → 127.12 (2023‑09‑29 is not a low in sequence, skip) → **149.91 low (2024‑01‑17)** → **155.62 low (2024‑02‑01)** → **165.75 low (2024‑02‑13)** → **165.74 low (2024‑02‑20)**. That last pair is a near-perfect **double bottom at 165.7–165.8**, and it is the single most useful structural support in this dataset.

**Higher highs:** 175.00 high (2024‑02‑09) → 175.39 (2024‑02‑12) → **175.75 (2024‑02‑23)**, with the highest **close** of the entire retrieval window (since 2023‑08‑01) printed at **174.99** today. (Note: the retrieval window begins 2023‑08‑01, so I cannot and do not claim an all-time-high status.)

---

## 3. Momentum: price is confirming, momentum is *not* — the key nuance

**MACD state:**
- MACD **4.3250**, signal **4.4001**, histogram **−0.0762** → line is *below* signal, i.e., a formally bearish crossover state.
- But trace the sequence: the histogram turned negative on **2024‑02‑16** (−0.039) and bottomed at **−0.530 on 2024‑02‑21**, then **−0.250 (02‑22) → −0.076 (02‑23)**. That is rapid compression → the bearish cross is close to being *reversed*.
- **Whipsaw evidence:** the bearish cross fired at the 2024‑02‑16 close of **169.51**; price is now **174.99, +3.2% above** that signal. A mechanical MACD crossover trade would have been stopped/whipsawed. This argues for using MACD as a *filter*, not a trigger, in this regime.
- **Bearish divergence:** MACD peaked at **5.50 on 2024‑02‑12** while price has since made a higher high (174.99 vs 172.34 close on 02‑12). Momentum peak precedes price peak — the Feb 22–23 advance is *less* momentum-charged than the Feb 1–9 leg, even though price is higher.

**RSI state: 65.75** (up from 55.91 on 2024‑02‑20).
- **Not overbought.** But note the lower-high sequence while price made higher highs: **73.78 (Feb 2) → 72.43 (Feb 9) → 65.75 (Feb 23)**. That is a second, independent momentum divergence.
- **Critical context — how this stock has treated high RSI in this window:** the two prior overbought prints produced only *shallow, short* consolidations: RSI 73.78 (Feb 2) → price dipped to a 168.64 close on Feb 13 (−2.1% from 172.34); RSI 72.43 (Feb 9) → price dipped to 167.08 close on Feb 20 (−3.0% from 172.34). **In this trend, high RSI has been a "trim/trail" signal, not a reversal signal** — supported directly by the prices above.
- Net: two divergences (MACD and RSI) = **do not add aggressively at the highs**; but zero evidence of distribution = **do not short**.

---

## 4. Volatility and band position

- **ATR 3.797 = 2.17% of the 174.99 close.** ATR was **2.94 on 2024‑01‑29** and jumped to **3.88 on 2024‑02‑02** (the earnings-related gap: prior close 159.28 → 02‑02 open 169.19, a **+6.2% gap** that remains unfilled). ATR has stayed in the 3.7–3.9 band since → the stock is in a **higher-volatility regime than January** (~+29% ATR expansion), which must be reflected in stops and size.
- **Bollinger context (snapshot):** mid **167.823**, upper **179.468**, lower **156.178**. Price at 174.99 sits at **~62% of the distance from mid to upper** — inside the band, *not* riding it. Upper band implies **+2.56%** of headroom before a band-touch signal.
- **Today's bar (2024‑02‑23):** open 174.28, high 175.75, low 173.70, close 174.99, volume 59,715,200. Range of just **2.05 pts = 0.54 ATR** — a controlled, narrow consolidation day at the highs *following* Thursday's big bar. Prior bar 2024‑02‑22: open 173.10, high 174.80, low 171.77, **close 174.58 (+5.99, +3.55%)**. Two consecutive strong closes into the high end of the range = buyers still in control at the print.

---

## 5. Volume / participation: the breakout is volume-backed

- **VWMA 170.66**, price **+2.54%** above it, and VWMA has risen for 15 consecutive sessions (163.98 on 2024‑02‑09 → 170.66 on 2024‑02‑23). Price above a rising VWMA = volume-weighted buyers are in profit and the trend is being paid for, not just drifting.
- 10 EMA (170.67) just crossed **marginally above** VWMA (170.66) on 2024‑02‑23 after sitting below it on 02‑21 (168.63 vs 168.87) and 02‑22 (169.71 vs 170.31) — a mild but real short-term re-acceleration tell.
- **Volume comparison (computed from the retrieved rows):** 15-session average (2024‑02‑02 → 02‑23) = **54.1M**; excluding the earnings-day 117.2M outlier, the other 14 sessions average **49.6M**.
  - Up days 02‑22 (55.4M) and 02‑23 (59.7M) are **+12% and +20%** vs the ex-earnings average → conviction buying.
  - Down day 02‑20 (167.08 close, −1.4%) traded only **42.0M**, well *below* average → low-conviction selling.
- This volume asymmetry (up days above average, down days below) is the strongest single argument that the Feb 22–23 push is real rather than a trap, and it partially offsets the momentum divergences.

---

## 6. Key levels (all tool-derived, with dates)

**Resistance**
| Level | Source |
|---|---|
| **175.75** | 2024‑02‑23 high — the immediate breakout trigger |
| 175.39 / 175.00 | 2024‑02‑12 high / 2024‑02‑09 high — a tight supply cluster at 175.0–175.75 |
| **179.47** | Bollinger upper band — the only tool-derived upside reference above price |

**Support**
| Level | Source |
|---|---|
| 173.70 | 2024‑02‑23 low (first intraday shelf) |
| 171.77 | 2024‑02‑22 low |
| **170.66–170.67** | VWMA and 10 EMA confluence — the "trend intact" line |
| **167.82** | Bollinger mid (20 SMA) |
| **165.74–165.75** | 2024‑02‑13 and 2024‑02‑20 lows — double bottom, the trend-invalidation pivot |
| 159.28 | 2024‑02‑01 close (origin of the unfilled +6.2% earnings gap) |
| **158.42** | 50 SMA — the last strategic support before the gap fills |

---

## 7. Actionable plan

**Bias: constructive/bullish, but size down and trail — do not chase the print.**

1. **Breakout add (preferred for trend accounts):** trigger on a **close above 175.75** with volume **≥ ~55M** (above the 15-day average of 54.1M). Initial stop at **167.40** (close − 2×ATR = 174.99 − 7.59), which sits just under the 167.82 mid-band and comfortably above the 165.74 double bottom. Risk ≈ **4.3%**. First scale-out reference **179.47** (upper band); there is no tool-derived resistance above 175.75, so trail the balance rather than inventing upside targets.
2. **Pullback add (better risk/reward):** buy the **170.5–167.8** zone (VWMA/10 EMA into mid-band) on a *reduction* in downside volume, with RSI resetting into the 50–55 zone. Stop below **165.50** (under the double bottom). Risk from 171.00 ≈ **3.2%**. This honors the observed Feb 2024 pattern of 2–4 day shallow dips (Feb 13: −2.1%; Feb 20: −3.0%) rather than deep corrections.
3. **Position sizing:** at 2.17% ATR and a 2‑ATR stop, risk-per-share is 7.59 (4.3%). For 1% account risk, notional ≈ **23% of equity** — but cut that materially if you use the tighter 3.2% pullback stop, since the same dollar risk supports a larger notional. Volatility has risen ~29% since late January; **reduce share count vs. a January-sizing framework** for the same dollar risk.
4. **Management rules given the divergences:** (a) If price closes below **170.66 (VWMA/10 EMA)** while MACD histogram is still negative, halve exposure — the volume-backed trend has failed. (b) A close below **165.74** invalidates the entire Feb advance and shifts focus to the **159.28** gap origin and **158.42** 50 SMA. (c) If the MACD line crosses back above its signal (needs roughly a +0.08 histogram swing from today's −0.076), treat that as confirmation to restore full size — it would convert the 02‑16 whipsaw into a bullish re-cross.
5. **What would make this a sell, not a trim:** a high-volume close below 165.74, *or* an RSI break under ~50 concurrently with price under the 20 SMA (167.82). Neither is present today.

---

## 8. Nuanced caveats

- **Two simultaneous momentum divergences** (MACD line 4.32 vs its 5.50 peak of 02‑12; RSI 65.75 vs 73.78/72.43) while price prints its highest close of the window. In a strong trend these typically resolve *sideways-to-shallow*, exactly as they did on Feb 13 and Feb 20 — but they are a legitimate reason to prefer the pullback entry over the breakout chase.
- **Extension risk is real at the structural level:** +26.3% above the 200 SMA and +10.5% above the 50 SMA. This is a mature leg, not an early one; the risk/reward for fresh full-size longs at 175 is worse than it was at 158–160 in early February.
- **The unfilled 159.28→169.19 earnings gap** is the structural "air pocket" beneath the entire February advance. It has not been tested, which is bullish, but it also means the zone between the 50 SMA (158.42) and the gap origin is thin in terms of prior trading.
- **MFI scale ambiguity** (0.445475) — I read it as ~44.5/100 = neutral money flow that does *not* confirm the breakout. Because the scale is uncertain, I assign it low weight and do not base any decision on it.
- **No dividends or splits** affected the window (split = 1.0, dividend = 0.0 on every retrieved row), so the total-return index equals close price and no adjustment distortion exists.

---

## 9. Summary table

| Dimension | Evidence (as of 2024‑02‑23) | Read | Action |
|---|---|---|---|
| Price | Close **174.99** (highest close in the 2023‑08‑01→2024‑02‑23 window); high 175.75; vol 59.7M | New high, close in upper half of range | Consolidation day after +3.55% on 02‑22 — constructive |
| Short-term trend | 10 EMA **170.67**; price **+2.53%** above; 10EMA just crossed above VWMA | Bullish, mildly extended | Trend intact line = 170.66–170.67 |
| Medium-term trend | 50 SMA **158.42**, rising every session since 2023‑10‑26; +0.46/session over last 17 | Strong, no flattening | 158.42 is strategic support |
| Long-term trend | 200 SMA **138.56**; 50−200 = **+19.85 (+14.33%)** and widening | Golden-cross regime, strengthening | Favors long side, but +26.3% extension caps size |
| MACD | 4.325 vs signal 4.401 → hist **−0.076**, improving from −0.530 (02‑21) | Bearish cross since 02‑16, *fading*; whipsawed (−3.2% below current price) | Filter, not trigger; re-cross imminent |
| RSI | **65.75** (55.91 on 02‑20); lower highs 73.78→72.43→65.75 vs higher price highs | Not overbought; mild negative divergence | Trim/trail, do not short |
| Volatility | ATR **3.797 = 2.17%** of price; up ~29% from 2.94 (01‑29) | Regime shift higher post-earnings | Stop = 2 ATR ≈ 167.40; shrink size |
| Bands | Mid **167.82**, upper **179.47**, lower **156.18** | Price at ~62% of mid→upper; not riding the band | Upside reference 179.47 |
| Volume | VWMA **170.66**, 15 used: 15-day avg 54.1M (49.6M ex-earnings); up days 55.4M/59.7M; down day 42.0M | Buying conviction, thin selling | Confirms the breakout leg |
| Structure | Double bottom **165.74/165.75** (02‑13, 02‑20); unfilled gap 159.28→169.19 | Well-defined risk pivot | Invalidation below 165.74 |
| **Plan** | Breakout add >**175.75** on ≥55M vol, stop **167.40**; or pullback buy **170.5–167.8**, stop **<165.50** | Constructive, size-adjusted | Invalidate on close <165.74 |