# GOOGL — Multi-Indicator Analysis, as of close 2026-07-21

**Verified reference row (source of truth):** 2026-07-21 O 351.32 / H 351.32 / L 347.00 / **Close 347.15**, volume 23,369,800. Snapshot indicator values: 50SMA 368.6492 · 200SMA 322.7117 · 10EMA 354.5570 · MACD −2.9605 · Signal −2.2894 · Histogram −0.6712 · RSI 43.1026 · Boll mid 354.9725 · Upper 372.4030 · Lower 337.5420 · ATR 11.2919 · VWMA 358.3824.

Note on scope: all twelve history/indicator pulls I made are internally consistent with the verified snapshot (no conflicts to flag). One caveat: my OHLCV pull begins 2026-01-01, so I have **no 52-week or 2025 base** — anything I say about "long-term" trend is anchored to the 200-day average that the vendor computes, not to a full year of visible price.

---

## 1. The indicator set I selected and why

This chart is a **post-peak consolidation inside a still-intact long-term uptrend, with elevated and rising volatility and repeated failed rallies**. That regime demands: (a) two trend anchors at different horizons, (b) a short-horizon momentum read for entry timing, (c) a crossover/impulse engine, (d) an oversold/mean-reversion gauge, (e) a volatility-free measure for sizing, and (f) a volume-aware price benchmark to test whether bounces have real participation.

**My 8 selected indicators:**

| # | Indicator | Role in this specific context |
|---|---|---|
| 1 | `close_200_sma` (322.71) | Strategic line — is the primary uptrend still valid? |
| 2 | `close_50_sma` (368.65) | Medium-term trend; now overhead resistance and clearly rolling over |
| 3 | `close_10_ema` (354.56) | Short-term regime switch; defines "bounce vs. breakdown" |
| 4 | `macd` (−2.96) | Zero-line position = momentum regime |
| 5 | `macds` (−2.29) | Crossover trigger (noise filter for #4) |
| 6 | `rsi` (43.10) | Is there oversold fuel left, and is there divergence? |
| 7 | `atr` (11.29) | Position sizing and stop distance in a 3%+ daily range tape |
| 8 | `vwma` (358.38) | Volume-weighted cost basis — are buyers stepping up or distributing? |

I deliberately **skipped** MACD histogram as a standalone (it's the arithmetic difference of #4/#5 — redundant), skipped a second oscillator (RSI alone; no StochRSI), and skipped multiple moving-average families that duplicate #1–#3. I *did* pull `boll`, `boll_ub`, `boll_lb` as **supplementary envelope context** (they define the range edges and a volatility-percentile read) — I don't count them in the core 8 because the middle band is essentially a 20-SMA and overlaps #2/#3.

---

## 2. Trend structure: three timeframes, three different answers

**Long term (200 SMA = 322.71) — still bullish.** Price sits **+7.6% above** the 200-day line, and that line is rising relentlessly: 315.61 on 7/1 → 320.60 on 7/15 → 322.71 on 7/21 (roughly +0.5/day). The 50 SMA (368.65) remains far above the 200 SMA — a golden-cross configuration with a ~46-point spread. Nothing in the long-term structure is broken. Critically, price is **26.9% above the March cycle low** (close 273.50 on 2026-03-30; intraday low 272.11), and **+10.2% year-to-date** versus the 315.15 close on 2026-01-02.

**Medium term (50 SMA = 368.65) — has turned down.** The 50 SMA peaked at **372.7972 on 2026-07-13** and has declined for six consecutive sessions to 368.6492. Price lost the 50 SMA decisively on **2026-07-17** (close 346.77, first close below it since 2026-06-29's recovery). Price is now **5.83% below** it. This is a textbook medium-term trend deterioration: the average itself has stopped rising *and* price is beneath it.

**Short term (10 EMA = 354.56) — bearish and folding over.** The 10 EMA recovered through early July (352.30 on 6/29 → 360.55 on 7/15) but has since curled down to 354.557 despite the 7/20 bounce attempt. Price is **2.09% below** it. The stack is now inverted short-term: **10 EMA (354.56) < 50 SMA (368.65)**, with price below both.

**The swing sequence — lower highs, higher lows, i.e. compression:**
- Swing highs (intraday): **408.61 (2026-05-18)** → **376.00 (2026-06-16)** → **375.27 (2026-07-16)**. Two consecutive attempts have died in the **375–376** zone.
- Swing lows (intraday): **335.84 (2026-06-25)** / **330.20 (2026-06-26)** → **341.36 (2026-07-17)**. A higher low.
- Since the 2026-05-13 closing peak of **402.62**, GOOGL is **−13.8%**; from the 5/18 intraday high of 408.61 it is **−15.0%**.

Read together: a one-month **contraction range of roughly 337–376**, currently trading in the lower-middle of it. That is a coiled, decision-pending structure — not a clean trend in either direction on the medium horizon — but the *internal* evidence (below) leans to the downside.

---

## 3. Momentum: the bearish crossover is fresh, and the histogram is expanding

- **MACD is negative (−2.9605) and has been for essentially all of June–July** — it topped at +13.62 on 2026-05-22 and printed a trough of **−7.3531 on 2026-06-26**.
- The **2026-07-02 bullish MACD/signal crossover** (MACD −4.336 vs. signal −4.836) worked for a while: price rallied 359.91 (7/2) → 370.92 (7/15), **+3.1%**. But MACD **never reclaimed zero** — a classic sign the "bull" was a counter-trend bounce, not a new leg.
- **MACD crossed back below its signal on 2026-07-17** (MACD −2.105 vs. signal −2.056). The gap has widened every session since: −0.0489 → −0.2619 (7/20) → **−0.6712 (7/21)**. Fresh bearish crossover + expanding negative impulse = downside momentum is reasserting, and it is early in the move, not exhausted.

**RSI (43.10) — fuel tank is not empty.** RSI collapsed from **56.87 (7/15)** to **43.10 (7/21)** in four sessions. It is bearish-neutral, **not oversold**. For calibration: this instrument's RSI did print **33.27 on 2026-06-26**, at the June low, before a +4.8% next-session reversal. So there is meaningful room to fall before RSI-based dip-buyers have a real edge.

One genuine positive nuance: **mild positive RSI divergence on the higher low** — price closed 346.77 on 7/17 vs. 337.39 on 6/26, yet RSI was 42.23 vs. 33.27. That is a real deterioration-in-selling-pressure signal. It is only a *watch item*, not a trigger, because price structure (lower high at 375.27) is still pointing down and RSI has since rolled over again to 43.10.

---

## 4. Volume: the bounces have poor participation; the selling has good participation

**VWMA is the most informative single line on this chart right now.** It bottomed at **350.02 on 2026-07-10** and *rose* to **358.3824 on 2026-07-21** — while price fell from ~371 to 347.15. Because VWMA weights by volume, a *rising* VWMA against *falling* price means the heaviest trading is occurring at higher prices: **distribution**. Price is **3.13% below VWMA**, i.e. the average dollar holder from the last few weeks is underwater.

Corroborating tape evidence:
- **2026-07-15 → 2026-07-16** is the key failed breakout. 7/15: +3.17% to 370.92 on 28.28M shares. 7/16: opened 373.06, printed a high of **375.27**, then reversed to close at **354.46 (−4.44%)** on **41.16M shares** — the **largest volume since 2026-06-26's 114.71M**, and an outside/reversal day. Follow-through was immediate: 7/17 gapped down to a 341.36 low and closed 346.77.
- **2026-06-26** printed **114.71M shares** (the sample's largest) with a −1.84% close and a 330.20 low; the very next session (6/29) reversed **+4.82% to 353.65**. That is genuine demand absorption at the lows — and it's the reason the 337–341 zone should not be dismissed as trivial support.
- Recent average participation is running ~23–25M/day (7/20 24.74M, 7/21 23.37M), so **the 41.16M on 7/16 is ~1.7× normal** — a high-conviction selling day, not noise.

**Conclusion:** rallies into 370–375 are being sold on above-average volume, and the 7/20 bounce (+1.5% to 351.99) came on *average* volume and was immediately surrendered on 7/21 (−1.4% to 347.15). That's a low-quality bounce.

---

## 5. Volatility and positioning math (ATR = 11.29)

- ATR is **11.2919 = 3.25% of the close** — high, and *rising* off the mid-July trough of 10.31 (7/14) to a 7/20 peak of 11.78. Expanding ATR on a down-move is a warning, not a comfort.
- **Bollinger envelope:** Upper 372.4030 / Mid 354.9725 / Lower 337.5420. Bandwidth = **9.82% of the middle band** — a mid-range reading, consistent with the 337–376 contraction. Price is **6.79% inside the upper band** and only **2.85% above the lower band** — much closer to the downside boundary.
- The **Bollinger middle band (354.9725) is falling** (358.50 on 7/1, 357.69 on 7/15, 354.97 now) — the 20-day mean is being dragged down, confirming the distribution read.
- Deltas: price is −2.20% vs. Boll mid, −2.09% vs. 10 EMA, −3.13% vs. VWMA, −5.83% vs. 50 SMA, **+7.57% vs. 200 SMA**.
- **ATR-based risk:** 1×ATR = 11.29 (3.3%), 1.5×ATR = 16.94, 2×ATR = 22.58. A stop inside ~11 points of a 347 entry is likely to be clipped by ordinary noise.

---

## 6. Actionable plan

**Bias: tactically bearish / structurally long. Net stance = reduce exposure, favor selling rallies over buying dips until 355–358 is reclaimed.**

**Bearish triggers (highest-conviction setup right now):**
1. **Loss of 341.36** (2026-07-17 intraday low) on volume >30M confirms the failure of the higher-low structure. First objective **337.54** (Bollinger lower) then **330.20** (2026-06-26 low). A deeper flush opens **322.71** — the rising 200 SMA, which is where the strategic bid lives.
2. **Sell-the-bounce zone: 354.5–358.4**, the dense confluence of 10 EMA (354.56), Boll mid (354.97), and VWMA (358.38). A rejection there — especially on declining volume — is the cleanest short entry with a defined invalidation.
3. Stop for any short from that zone: above **362.97** (2026-07-01 high) is a first warning; above **367.93** (2026-07-06 high) invalidates the whole setup. That is ~5–7 ATRs of room, so **halve normal size** and use ~9–12 points of stop on intraday-scale entries instead.

**Bullish triggers (what would actually change the read):**
1. A **daily close above 358.38 (VWMA) on volume ≥1.3× the 20-day average** — that would put price back above its volume-weighted cost basis and flip VWMA from distribution evidence to support.
2. A **daily close above 50 SMA (368.65)**, which would also mean price clears the 375–376 cap only if it closes above **376.00**; a decisive break of 375–376 breaks the lower-high sequence and reopens 388.91 (2026-07-09 high area) and then ~400.
3. MACD histogram turning positive again (needs a close above ~354 and would need several sessions) — treat this as *confirmation*, not an entry trigger.

**Strategic / long-term holder:** the 200 SMA at 322.71 is +0.5/day and rising; nothing about the YTD +10.2% or the 26.9% advance off the March low is impaired. This is a **de-risking / trim-into-strength tape, not a thesis-break tape**. Scale-back-in levels: **337.5**, **330.2**, and **322.7**.

**Risk management notes:**
- Realized gap risk is large in this record: 2026-02-05 opened **312.22 vs. a 333.04 prior close (−6.3% gap)** and 2026-04-30 opened **374.07 vs. 349.94 (+9.9% gap, 72.0M volume)**. Stops will not protect through events of that kind — size positions so a gap-through is survivable, don't rely on the stop alone.
- Do not treat the RSI positive divergence as a buy signal in isolation; in June the same divergence setup only produced a two-week bounce that failed at the 375–376 cap.
- Liquidity is not a constraint (23M+ shares/day), but volume is *informationally* important here — every signal above should be volume-confirmed.

---

## 7. Key points summary

| Dimension | Reading (2026-07-21) | Interpretation | Actionable level |
|---|---|---|---|
| Close | 347.15 (H 351.32 / L 347.00) | Closed near session low; bounce from 7/20 failed | — |
| 200 SMA | 322.7117, rising ~+0.5/day | **Primary uptrend intact**; price +7.57% above | Strategic support 322.71 |
| 50 SMA | 368.6492, falling since 7/13 peak 372.80 | **Medium-term trend has turned down**; price −5.83% below | Reclaim = trend repair |
| 10 EMA | 354.5570, curling down | **Short-term regime = bearish**; price −2.09% below | Entry pivot 354.56 |
| MACD | −2.9605 | Below zero; momentum still negative | — |
| MACD Signal | −2.2894 | **Bearish crossover 2026-07-17**; gap widening 3 sessions | Confirmation only |
| RSI | 43.1026 (from 56.87 on 7/15) | Neutral-bearish, **not oversold**; June low was 33.27 | Oversold floor ≈ 33 |
| Bollinger | Mid 354.9725 · UB 372.4030 · LB 337.5420; width 9.82% | Mid band falling; price nearer lower band (−2.20% vs mid) | Range 337.54–372.40 |
| ATR | 11.2919 (3.25% of price), rising | **Wide, expanding ranges** — halve size, widen stops | 1×=11.29, 2×=22.58 |
| VWMA | 358.3824, rising while price falls | **Distribution**; avg recent buyer underwater; price −3.13% below | Reclaim 358.38 = bullish |
| Volume | 23.37M (7/21); 41.16M on 7/16 reversal | Selling days carry volume; bounces don't | Demand >30M on up-days |
| Swing structure | Highs 408.61 → 376.00 → 375.27; lows 335.84/330.20 → 341.36 | **Lower highs + higher lows = compression 337–376** | Break 341.36 / 376.00 |
| Position vs. peak | −13.8% from 402.62 close (5/13); −15.0% from 408.61 (5/18) | Correction, not a collapse | — |
| YTD context | +10.2% vs. 315.15 (1/2); +26.9% vs. 273.50 (3/30) | Long-term trend positive | — |
| **Net bias** | **Tactically bearish, structurally long** | Sell rallies into 354.5–358.4; do not chase dips | Buy scale-ins 337.5 / 330.2 / 322.7 |

**Bottom line:** GOOGL is a stock that topped in mid-May, spent June rebuilding, and has now **failed twice at 375–376**. The 7/16 outside-day reversal on 1.7× volume, the 7/17 break of the 50 SMA, the fresh 7/17 MACD bearish cross with an expanding negative histogram, a rising VWMA above price, and RSI at 43 (not oversold) all point the same direction over a 2–6 week horizon. But the 200 SMA is still climbing and price is 7.6% above it, so this is a **risk-reduction and sell-strength tape, not a short-the-thesis tape**. The single level that would force me to abandon the bearish tactical stance is a volume-confirmed daily close above **358.38**, with **376.00** as the structural line in the sand.