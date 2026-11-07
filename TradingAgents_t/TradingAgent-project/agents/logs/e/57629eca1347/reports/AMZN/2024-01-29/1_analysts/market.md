## AMZN — Technical Analysis, 2024‑01‑29 (close **$161.26**)

*Data window used: 2023‑07‑03 → 2024‑01‑29 (145 sessions). All price/indicator figures below are taken from the verified snapshot and the indicator series returned for `AMZN`; the snapshot and the individual indicator calls agree to the last decimal (e.g., 50SMA 150.2012, RSI 70.406, MACD 2.6772, ATR 2.9443, VWMA 155.2077), so no reconciliation issue arose.*

---

### 1. Market context and why these indicators

`AMZN` is in a **confirmed, accelerating intermediate uptrend** trading at the top of its visible range, with a **binary catalyst (Q4 earnings, typically the first week of February — verify the exact date independently, it is not verifiable from my data tools) directly ahead**. That combination means the analysis must answer three separate questions, so I selected indicators that map 1:1 to them:

| Question | Selected indicators |
|---|---|
| Is the trend intact and where is structural support? | `close_50_sma`, `close_200_sma`, `close_10_ema` |
| Is momentum still *building* or already fading into the highs? | `macd`, `macds` |
| Is the move overextended / what is the correct risk unit? | `rsi`, `atr`, `vwma` |

I deliberately avoided redundancy: no `macdh` (its crossover timing is already captured by `macd` vs `macds`), no `boll` middle band (it duplicates the 20‑day trend read already given by `close_10_ema`/`close_50_sma`). I did pull `boll_ub`/`boll_lb` **as a corroborating cross‑check only** (see §2), not as one of the eight core selections.

---

### 2. Trend structure: a textbook bullish stack, but stretched

- **Price vs. averages (2024‑01‑29):** close 161.26 sits above the 10 EMA (156.6864), which sits above the 50 SMA (150.2012), which sits far above the 200 SMA (132.7768). This is a fully ordered bullish stack — no average is inverted.
- **Distance from trend anchors:** price is **+2.9% above the 10 EMA**, **+7.4% above the 50 SMA**, and **+21.4% above the 200 SMA**. That is a healthy trend but an unusually wide short‑term extension: on a mean‑reversion basis the 10 EMA (156.69) and VWMA (155.21) are the natural "gravity" levels.
- **Slopes are rising, not flattening:** 50 SMA went 134.59 (2023‑11‑30) → 149.89 (2024‑01‑26) → **150.2012** (2024‑01‑29); the 200 SMA went 122.21 → 132.46 → **132.7768** over the same dates. Both are still gaining ~0.30 points per session.
- **Golden‑cross regime:** the 50 SMA has been above the 200 SMA throughout the visible period and the **spread has widened from 12.38 points (2023‑11‑30) to 17.42 points (2024‑01‑29)** — the long‑term trend is strengthening, not maturing.
- **Structural high:** today printed open 159.34 / high **161.29** / low 158.90 / close **161.26** on 45.27M shares. That is the highest close and highest intraday print in the 145‑session window I have. **Caveat:** my history begins 2023‑07‑03, so I cannot claim a "52‑week" or "all‑time" high from tool output — only "highest level in the ~7 months of data provided."
- **Sequence of higher lows:** 144.05 (2024‑01‑04 low) → 149.91 (01‑17 low) → 153.90 (01‑22 low) → 154.55 (01‑25 low) → 158.90 (today's low). Each pullback has been bought at a higher level. Rally magnitude: **+11.6% from the 2024‑01‑04 close of 144.57** and **+34.9% from the 2023‑10‑26 close of 119.57**.

**Bollinger cross‑check (not a core selection):** middle 153.1830, upper **161.7717**, lower 144.5943. Today's close is only **$0.51 below the upper band** (%B ≈ 0.97) — price is *riding* the band, which in strong trends is continuation, but it also means there is essentially zero cushion for a normal-range down day. Bandwidth is ~11.2%, and the upper band has climbed for seven straight sessions (157.89 on 01‑19 → 161.77 today), confirming a genuine volatility expansion in the direction of the trend rather than a squeeze fake‑out.

---

### 3. Momentum: price is making new highs; MACD is **not** — the key nuance

- **MACD line 2.6772 > signal 2.0792**, histogram **+0.598**. The histogram has expanded for **seven consecutive sessions** (0.109 on 2024‑01‑19 → 0.598 today), the strongest momentum run since December. The MACD/signal crossover re‑fired on 2024‑01‑19 after a brief whipsaw (histogram was negative on 01‑17 at −0.039 and 01‑18 at −0.012).
- **But the crossover is not yet fully trustworthy — and there is a real divergence.** The MACD line topped at **3.136 on 2023‑12‑22** when price closed 153.42. Today price is **+5.1% higher** (161.26) yet the MACD line is **14.6% lower** (2.677 vs 3.136). Price made a higher high; the MACD line made a lower high. That is a classic momentum non‑confirmation and it argues that the current leg is *thrust driven by price discovery*, not by accelerating momentum.
- **RSI 70.406** — just through the 70 line, the highest reading in the 40‑session series (previous peak 65.31 on 2023‑12‑21). RSI is *rising with* price (no RSI divergence), which supports continuation, but at 70+ the marginal buyer is late. The December precedent is instructive: RSI ran 62–65 for a week (12/18–12/28) and then price simply went sideways‑to‑down into the 1/4 flush to 144.05. In strong trends RSI can stay >70 for weeks, so this is a **risk‑management flag, not a sell signal.**

**Interpretation:** the trend is bullish; the *pace* is the problem. Both the MACD lower high and the 0.97 %B reading say the same thing — the advance is intact but no longer cheap to enter.

---

### 4. Volume and participation: confirming, but not confirming *enthusiastically*

- **VWMA 155.2077**, up from 150.98 on 01‑04 and 152.25 on 01‑24 — i.e., the volume‑weighted average price has risen **+1.9% in four sessions** after being flat through most of January. Price gains are being validated by where volume actually transacted, which is bullish confirmation (price is +3.9% above VWMA).
- **The flaw:** today's 45.27M shares is only ~1.04× the roughly 43.6M ten‑session average. For a session that closed at a new range high, you would want a visible expansion (50M+). Compare the event‑driven volumes in the series — 153.1M on 2023‑08‑04, 125.3M on 2023‑10‑27, 100.4M on 2023‑10‑26 — to see what real institutional participation looks like on this name. The 01‑26 and 01‑29 breakouts (51.05M / 45.27M) are decent but not a surge.
- **Practical read on VWMA:** the average January holder is carrying roughly 151–155 cost basis. Dips into the 155–156 zone are therefore more likely to be absorbed than dips into 145, because they sit at the volume‑weighted break‑even of recent buyers.

---

### 5. Volatility and risk arithmetic (ATR)

- **ATR 2.9443 = 1.83% of the close.** ATR has *compressed* from 3.4232 (2023‑12‑20) — a 14% decline — even as price advanced 6.0% over that period. Today's true range (158.90–161.29 = 2.39) is below the ATR, i.e., an orderly, low‑noise grind higher.
- **Why that matters now:** volatility compression at the upper Bollinger band, immediately before an earnings report, is the precursor to an expansion move in *either* direction. Sizing must assume the ATR understates event risk; do not size as if 1.8% daily range is the worst case.
- **Stop levels built from ATR (longs):**
  - Aggressive/tactical: **1.5 × ATR ≈ $4.42 → ~156.85** (sits just above the 10 EMA 156.69 — a clean confluence).
  - Standard swing: **2 × ATR ≈ $5.89 → ~155.37** (aligns with VWMA 155.21 — the strongest confluence zone in the book).
  - Thesis invalidation: close below the 1/25 low of **154.55**, then the 2024‑01‑22 low of **153.90** and the Bollinger middle at 153.18. Below that, the 50 SMA at 150.20 is the last structural floor.
- **Position sizing example:** if risking 1% of equity with a 2×ATR stop (3.65% of price from 161.26), notional exposure ≈ 27% of equity per unit of 1% risk. That math should be halved if you intend to hold through the earnings print, because gap risk is not bounded by the ATR.

---

### 6. Actionable plan

**Bias: constructive / stay long — do not chase at 161.26.**

1. **Core trend holders:** hold. The stack (close > 10 EMA > 50 SMA > 200 SMA, both SMAs rising, widening golden‑cross spread) has not degraded. Trail stops under the 10 EMA (156.69) or use 1.5×ATR (~156.85) to protect the +11.6% move from 144.57.
2. **New entries:** wait for confluence. Two preferred zones:
   - **Zone A — 156.7–155.2** (10 EMA 156.69 + VWMA 155.21 + 1/24 close 156.87). First pullback buy.
   - **Zone B — 153.9–153.2** (2024‑01‑22 low 153.90 + Bollinger middle 153.18). Add on a deeper shakeout that holds.
   - Also note the **unfilled gap from 2024‑01‑25/26: 157.75 (close) → 157.91 (low)**. Gaps of this type frequently act as a downside magnet; a tag of 157.8 that reverses higher is a valid low‑risk trigger with the stop below 156.6.
3. **Do not buy a fresh breakout above 161.29 into earnings** with RSI >70 and %B ≈ 0.97. The reward‑to‑risk is poor: the first objective above is the upper band at 161.77 (only ~$0.51 away) and then the round number ~165 (psychological level, not tool‑derived). A failed breakout from this configuration typically retests the 10 EMA quickly.
4. **Bearish tripwires (tighten or exit):**
   - Close back **inside** the bands with a lower high, i.e., failure at 161.29–161.77 followed by a close below 157.9.
   - MACD histogram rolls back below zero (it flipped negative twice in mid‑January at −0.039/−0.012 — the signal is not bulletproof).
   - A close below **154.55** converts the pattern from "higher lows" to "lower low" and shifts the bias to neutral.
5. **Post‑event plan:** whichever way the earnings gap resolves, re-anchor on VWMA (155.21) and the 50 SMA (150.20) as the new reference. If a gap‑up holds above 161.77 with volume >1.5× the 10‑day average, the MACD divergence is effectively retired and the trend can be re‑risked; if a gap‑down closes below 153.18, the intermediate uptrend is broken and the 50 SMA at 150.20 is the line that matters.

---

### 7. Summary table

| Dimension | Evidence (2024‑01‑29, verified) | Signal | Actionable implication |
|---|---|---|---|
| **Price** | Close **161.26**, high 161.29, low 158.90, vol 45.27M | New high in visible 145‑session window | Highest level since at least 2023‑07; no overhead tool‑measured resistance |
| **Short trend** | 10 EMA **156.6864**; price +2.9% above | Bullish, extended | Trail stop ~156.7–156.9 |
| **Medium trend** | 50 SMA **150.2012**; price +7.4% above; slope +0.31/session | Bullish | Primary pullback support 150.20 |
| **Long trend** | 200 SMA **132.7768**; price +21.4% above; 50>200 spread widened 12.38→17.42 points since 11/30 | Strong bullish / golden cross | Strategic bias stays long |
| **Momentum** | MACD **2.6772** > signal **2.0792**; histogram +0.598, 7 sessions of expansion | Bullish crossover, re‑fired 01‑19 | Momentum supports continuation short term |
| **Divergence** | MACD line 3.136 @ 12/22 (close 153.42) vs 2.677 @ 161.26 (close +5.1% higher) | **Negative divergence** | Do not add size at the highs; respect trailing stops |
| **Overbought** | RSI **70.406** (highest in 40 sessions; prior peak 65.31) | At/over 70 threshold | Avoid fresh breakout buys; not a standalone sell signal |
| **Band position** | Boll UB **161.7717** / mid **153.1830** / LB **144.5943**; %B ≈ 0.97 | Riding upper band | Zero cushion; ~$0.51 to band, risk of snap‑back to 10 EMA |
| **Volatility** | ATR **2.9443** (1.83% of price), down 14% since 12/20 | Compressed | Use 1.5×ATR (156.85) / 2×ATR (155.37) stops; expect event‑driven expansion |
| **Volume** | VWMA **155.2077** (+1.9% in 4 sessions); today's volume 1.04× 10‑day avg (~43.6M) | Confirming but not surging | Breakout lacks volume conviction — demand 1.5×+ avg on any continuation |
| **Structure** | Higher lows 144.05 → 149.91 → 153.90 → 154.55 → 158.90; unfilled gap 157.75–157.91 | Bullish, intact | 157.8 gap tag as low‑risk entry trigger |
| **Event risk** | Q4 earnings expected in the first days of February (calendar date **not** verifiable via tools) | Binary | Halve size into the print; ATR understates gap risk |

**Bottom line:** `AMZN` is a high‑quality trend that has become an unattractive *entry*. Hold existing longs with stops near 156.7–156.9 (1.5×ATR / 10 EMA), buy only into the 156.7–155.2 confluence or the 153.9–153.2 confluence, and treat a failure at 161.29–161.77 alongside the MACD lower‑high as the signal that the November–January advance needs a deeper reset toward the 50 SMA at 150.20.