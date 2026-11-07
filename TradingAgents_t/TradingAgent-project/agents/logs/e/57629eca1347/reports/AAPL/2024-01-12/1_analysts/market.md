# AAPL — Technical Analysis Report
**As of the session of 2024-01-12 (last completed session) | Instrument: AAPL (Apple Inc.)**

---

## 1. Verified baseline (source of truth)

The verified snapshot for **2024-01-12** and the raw OHLCV series agree exactly — no discrepancy to flag on price, volume, or indicator values.

| Field | 2024-01-12 |
|---|---|
| Open | 186.06 |
| High | 186.74 |
| Low | 185.19 |
| **Close** | **185.92** |
| Volume | 40,477,800 |
| 50 SMA | 189.02 |
| 200 SMA | 180.69 |
| 10 EMA | 186.49 |
| MACD | −1.610 |
| MACD Signal | −0.847 |
| MACD Histogram | −0.763 |
| RSI(14) | 43.06 |
| Bollinger Mid / Upper / Lower | 190.27 / 201.41 / 179.12 |
| ATR(14) | 2.936 |
| VWMA | 186.69 |

> **Data caveat:** the snapshot also reports an `mfi` of **0.316275**. The scale is ambiguous (likely a 0–1 normalization of ~31.6 rather than a raw 0–100 reading). Because I cannot verify the scale, I do **not** use MFI as evidence anywhere in this report.

---

## 2. Regime classification: **long-term uptrend intact, medium-term correction, short-term downtrend decelerating**

Three timeframes are currently in conflict, which is the single most important observation in this report:

- **Strategic (200 SMA):** bullish. Close 185.92 is **+2.90% above** the 200 SMA at 180.69, and the 200 SMA is *rising* (172.73 on 2023-11-13 → 180.69 on 2024-01-12, a +7.96 advance over roughly two months). No death-cross risk: the 50 SMA (189.02) remains **+4.61% above** the 200 SMA.
- **Intermediate (50 SMA):** broken. AAPL has closed **below the 50 SMA for nine consecutive sessions** (2024-01-02 through 2024-01-12). Close is **−1.64%** (−3.10 points) under it.
- **Short-term (10 EMA):** downtrend, but flattening. AAPL has closed below the 10 EMA for **16 consecutive sessions** (from 2023-12-20 onward). Close is −0.31% under it.

**Critical nuance on the 50 SMA:** it is still sloping *up* (~+0.30/day) because it is rolling off the November/early-December prices (roughly 176–182), not because price is strong. It will keep grinding higher for several more sessions *even if price goes nowhere*. Two implications: (a) the price/50-SMA bearish cross is **not** yet a confirmed trend break in the average itself, and (b) the bar for a bullish "reclaim of the 50 SMA" is a moving target that is rising toward 189+ rather than a static 189.0.

---

## 3. Why these 8 indicators were selected

I chose a **complementary, non-redundant set spanning all four analytic dimensions** rather than piling up similar oscillators:

| Indicator | Role in this specific context |
|---|---|
| `close_200_sma` | Anchor for the intact primary uptrend; defines the line in the sand near 180.7 |
| `close_50_sma` | The level the market actually lost; primary intermediate resistance/trigger |
| `close_10_ema` | Captures the deceleration in the pullback; fastest read on trend repair |
| `macd` | Confirms the crossover into negative territory on 2024-01-04 |
| `macdh` | Diagnoses whether downside momentum is *accelerating or fading* — the key live question |
| `rsi` | Documents the oversold flush (28.79) and the quality of the bounce |
| `atr` | Converts every level above into a tradable, volatility-adjusted stop distance |
| `vwma` | Tests whether the decline was volume-confirmed or air-pocket noise |

Deliberately excluded as redundant: Bollinger middle/upper/lower (highly correlated with the 50 SMA + ATR already selected — band values are still quoted from the snapshot for context), and oscillator stacking (RSI is used alone; adding StochRSI/MFI would double-count the same momentum signal).

---

## 4. Indicator-by-indicator evidence

### 4.1 Moving-average stack — compressed bearish alignment
Structure on 2024-01-12: **Price 185.92 < 10 EMA 186.49 < VWMA 186.69 < 50 SMA 189.02**, with the **200 SMA 180.69** far below. This is a *bearish short-term stack inside a bullish long-term stack*.

The tight cluster at **186.49–186.69** (10 EMA + VWMA) and **185.92 (price)** is meaningful: price spent the entire last week pinned within ~0.8 points (+0.4%) of both average lines without closing decisively above either. That is compression, not capitulation.

The 10 EMA's *rate of change* is the tell: it fell from 195.51 (2023-12-19) to 186.49, but daily declines have shrunk to −0.05, −0.23, −0.13 over the last three sessions. **The average's slope is rolling flat**, which is the mechanical precursor to a price/10-EMA reclaim — not proof of one.

### 4.2 MACD — bearish, but the histogram is improving for five straight sessions
- MACD crossed **below zero on 2024-01-04** (from +0.055 on 2024-01-03 to −0.702) and has held negative since.
- The MACD line crossed below its signal earlier — the histogram first turned negative on **2023-12-19** (−0.057) and bottomed at **−2.045 on 2024-01-05**.
- Since that trough, the histogram has improved every single session: −2.045 → −1.747 → −1.499 → −1.196 → −0.978 → **−0.763**. That is a **+1.28 improvement in five sessions**, roughly 63% of the trough magnitude recovered.

**Interpretation:** the *selling impulse* is decaying much faster than price is recovering — a classic "momentum trough" pattern that often precedes a stabilization, but the MACD line (−1.610) is still 0.76 below its signal (−0.847), so **no bullish crossover has occurred**. This is a "decline decelerating," not a "reversal confirmed."

### 4.3 RSI — neutral at 43, recovering from a genuine oversold flush
RSI path: 70.02 (**2023-12-08**, overbought peak) → declining through December → **28.79 on 2024-01-05** (oversold) → 41.34 → 40.60 → 43.33 → 42.14 → **43.06**.

The recovery from 28.79 to 43.06 accompanied a price recovery from 181.18 (2024-01-05 close) to 185.92 — a **+2.62%** bounce. Because RSI rose *alongside* price, there is **no RSI divergence** to trade here, bullish or bearish. RSI at 43 is genuinely neutral: it has ~27 points of headroom before overbought and is no longer generating a mean-reversion signal. Note that RSI stalled between 01-08 and 01-12 (41.3 → 43.1 while price tried 186.19 and failed) — the bounce is losing thrust.

### 4.4 ATR — volatility is moderate and contained
ATR(14) = **2.936**, i.e. **1.58% of the 185.92 close**. ATR has been remarkably stable: 2.57 on 2023-12-29, spiking to 3.01 on 2024-01-02 (the gap day) and settling at 2.94. It has *not* expanded the way it did in the September–October 2023 drawdown, which supports the "controlled correction" read rather than "distribution/breakdown."

Practical translation:
- 1 ATR below the close = **182.98**
- 2 ATR below the close = **180.05** — which sits almost exactly on the **200 SMA at 180.69**. That confluence is the most important risk number on this page.

### 4.5 Bollinger context (from verified snapshot)
Middle **190.27**, Upper **201.41**, Lower **179.12**. Band width ≈ 22.29, or **11.7% of the middle band** — wide, reflecting December's expansion. Price at 185.92 sits in the **lower half** of the bands: **−2.29%** below the middle and **+3.8%** above the lower band. Notably, the January low close (181.18) and intraday low (180.17 on 2024-01-05) **never touched the lower band** — the pullback has been shallow relative to the prevailing volatility envelope.

---

## 5. Volume and participation — the most bearish single data point

`vwma` = **186.69**, above the close of 185.92. Price is trading **below its volume-weighted average price**, which means the average dollar transacted over the VWMA window is at a *higher* level than the current print — i.e., recent volume-weighted activity has been net distributional. VWMA has fallen from 195.53 (2023-12-26) to 186.69, confirming the sellers carried the volume on the way down.

The session-level pattern reinforces it:
- **Down volume was heavy:** 82.49M on 2024-01-02 (gap-down day, range 183.89–188.44, prior close 192.53 → open 187.15 = a **−2.79% opening gap**), and 71.98M on 2024-01-04.
- **Up volume was light:** 59.14M on 2024-01-08, 46.79M on 2024-01-10, and only **40.48M on 2024-01-12** — roughly **half** the 01-02 volume.

**Conclusion:** the bounce from 181.18 to 185.92 is a **low-conviction, declining-volume rally**. That is the strongest argument that the 186.5–186.7 resistance cluster will hold on first test.

---

## 6. Level map

**Resistance (in order):**
1. **186.49–186.69** — 10 EMA + VWMA cluster (price is *inside* it now)
2. **187.05** — 2024-01-11 high (the immediate swing high)
3. **188.44–189.02** — the **unfilled 2024-01-02 gap** (188.44 high vs 192.53 prior close) with the **50 SMA at 189.02** sitting inside it. This is a stacked, high-quality resistance zone.
4. **190.27** — Bollinger middle
5. **193.50–195.71** — December shelf (2023-12-22 close 193.60; 2023-12-08 high 195.99)
6. **198.11 / 199.62** — 2023-12-14 close and intraday high (the December peak)

**Support (in order):**
1. **185.19** — 2024-01-12 intraday low
2. **183.62–183.89** — 2024-01-11 low and 2024-01-02 low (the front edge of the breakdown structure)
3. **180.17–181.18** — 2024-01-05 low / close, plus 2-ATR at 180.05
4. **180.69** — **200 SMA** (the primary trend line; near-perfect confluence with 2 ATR)
5. **179.12** — Bollinger lower band

**Reference points for context (tool data, not inferences):** the 2023-12-14 close of 198.11 to the 2024-01-12 close of 185.92 is **−6.15%**. The 2024-01-05 close of 181.18 to the 2024-01-12 close of 185.92 is **+2.62%**. The October 2023 closing low was 166.89 (2023-10-26); the close is **+11.4%** above it.

---

## 7. Actionable scenarios with explicit triggers

### Scenario A — Bullish repair (needs confirmation, ~30% weight)
**Trigger:** a daily close **above 187.05**, ideally with volume > 50M, then a close **above 189.02** (50 SMA).
**Confirmation:** MACD line crossing above its signal (needs MACD to rise ~0.76 from −1.610); MACD histogram turning positive.
**Path/target:** 190.27 (Boll mid) → gap-fill completion toward 192.53 → December shelf 193.5–195.7.
**Invalidation:** any close back below 185.19.
**Why it's not the base case yet:** volume is falling on the bounce and price cannot clear the 10 EMA/VWMA cluster. Do not front-run this — wait for the close.

### Scenario B — Range compression / base-building (base case, ~45% weight)
**Range:** **183.6 – 187.1**, i.e. roughly ±1 ATR (2.94) around the 185.4 midpoint.
**Rationale:** ATR flat at ~2.94, RSI neutral at 43, MACD histogram improving but no crossover, price pinned between the 10 EMA/VWMA cluster overhead and the 01-11 low beneath. 16 sessions of lower closes without a volatility expansion is textbook digestion.
**Trade:** fade the extremes with tight risk. Longs near 183.9–184.3 risking below 183.4; shorts near 186.9–187.1 risking above 187.4. Require a volume uptick before treating either edge as a breakout.

### Scenario C — Trend-break continuation (~25% weight)
**Trigger:** a daily close **below 183.62** (2024-01-11 low) — that would break the week's higher-lows pattern and confirm the 2024-01-02 gap as a true distribution event.
**Next:** 180.17–181.18 (Jan 5 low) → **180.69 (200 SMA)**.
**Critical threshold:** a close **below 180.17** would be the first break of the 200 SMA since the trend began and would flip the primary classification from "uptrend correction" to "trend damage," opening 179.12 (Boll lower).
**What argues against it:** the 200 SMA is rising fast (+0.13/day) and the Oct-2023 low is 11.4% below; the long-term bid has repeatedly defended higher levels. Position for this, don't predict it.

---

## 8. Risk management and position sizing

- **Unit of risk:** 1 ATR = **2.94 points (1.58%)**. Use this, not round numbers.
- **Long swing stop:** below **183.4** (1.5 ATR below 185.92 ≈ 181.5 is too loose if the 01-11 low at 183.62 fails first; use the structural stop). Risk from 185.92 ≈ 2.5 points = **1.3%**.
- **Short swing stop:** above **187.4** (just above the 01-11 high of 187.05). Risk ≈ 1.5 points = **0.8%**.
- **Position sizing:** with a ~1.3% stop and a 1% account risk budget, size ≈ 0.75x of a normal unit. If you widen to a 2-ATR stop (180.05, 3.2% risk), size ≈ 0.31x.
- **Asymmetry to respect:** the upside is stacked with three resistances (186.5–186.7, 187.05, 188.44–189.02) inside 1.7% while the downside to the 200 SMA is 2.8%. **Reward/risk favors patient longs at support over momentum longs at current price.**
- **Event risk:** no tool-verified catalyst on the calendar; note the elevated 128.5M volume on 2023-12-15 (quad-witching/index event) as a reminder that index-driven flows can override technicals intraday.

---

## 9. What would change this read

| Observation | Would mean |
|---|---|
| Close > 187.05 on >50M volume | Short-term downtrend over; shift to Scenario A |
| MACD line crosses above signal (MACD ≈ −0.85) | Momentum regime flip; the single cleanest bullish confirmation available |
| Close < 183.62 | Scenario C activates; abandon range thesis |
| Close < 180.69 (200 SMA) | Primary uptrend broken; full defensive posture |
| ATR expands > 3.5 | Volatility regime change; halve position sizes and widen stops |
| VWMA crosses below price | Volume-weighted flow turning supportive — would materially upgrade the bull case |

---

## 10. Summary table

| Dimension | Indicator / Data | Reading (2024-01-12) | Interpretation | Actionable Level |
|---|---|---|---|---|
| **Primary trend** | `close_200_sma` | 180.69, rising (+7.96 since 2023-11-13) | **Intact uptrend** — close +2.90% above | Defense line at **180.69** |
| **Intermediate trend** | `close_50_sma` | 189.02, still rising but price below for 9 sessions | **Broken** — close −1.64% | Resistance/trigger **189.02** |
| **Short-term trend** | `close_10_ema` | 186.49, slope flattening (−0.05/−0.23/−0.13 last 3 days) | 16 closes below; downtrend **decelerating** | Reclaim above **186.49** |
| **Momentum state** | `macd` / `macds` | −1.610 / −0.847 (crossed below zero 2024-01-04) | **Bearish**, no bullish crossover yet | Cross needs MACD ≈ −0.85 |
| **Momentum direction** | `macdh` | −0.763, up from −2.045 on 2024-01-05 (5 straight improvements) | Selling impulse **fading**, not reversed | Positive histogram = confirmation |
| **Overbought/oversold** | `rsi` | 43.06; recovered from 28.79 (2024-01-05); peak 70.02 (2023-12-08) | **Neutral**; no divergence | <30 re-arms oversold; >50 bullish |
| **Volatility** | `atr` | 2.936 (1.58% of close); stable, no expansion | **Controlled correction** | 1 ATR = 182.98; 2 ATR = 180.05 |
| **Volume/flow** | `vwma` | 186.69 — **above** close; declining from 195.53 (2023-12-26) | **Distributional**; bounce on falling volume (40.5M vs 82.5M on 01-02) | Price above 186.69 = flow repair |
| **Envelope** (snapshot) | Bollinger | Mid 190.27 / UB 201.41 / LB 179.12; width 11.7% | Lower half of bands; Jan low never tagged LB | Range **179.12–190.27** |
| **Structure** | OHLCV | Dec-14 peak close 198.11 (high 199.62); −6.15% to 185.92 | Corrective, not yet structural damage | Unfilled gap **188.44–192.53** |
| **Net call** | Composite | Bullish long-term / bearish short-term / neutral momentum | **Range 183.6–187.1 is base case** | Buy support ≥183.6, sell resistance ≤187.1, invalidate outside |

*All figures above are drawn from the frozen point-in-time dataset and the 2024-01-12 verified snapshot, which are mutually consistent. Derived percentages are simple arithmetic on tool-provided closing prices with dates stated. No historical backtest, win-rate, or "bounce off support" claim is made — the level map describes where prices clustered, not a validated predictive edge.*