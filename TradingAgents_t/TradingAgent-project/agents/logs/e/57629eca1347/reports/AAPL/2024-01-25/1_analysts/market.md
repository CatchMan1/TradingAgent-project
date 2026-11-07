# AAPL — Technical Report (as of 2024-01-25 close)

**Source of truth:** verified snapshot for 2024-01-25 plus indicator series pulled from the frozen OHLCV set. All indicator values below match the snapshot exactly — **no discrepancies to flag**.

---

## 1. Market State Summary

AAPL closed **194.17** on 2024-01-25 (O 195.22 / H 196.27 / L 193.11), a marginal **−0.33 (−0.17%)** vs. the 2024-01-24 close of 194.50, on **54,822,100** shares (≈0.99× the ~55.5M 20-session average I computed from the visible rows, i.e. essentially average, not confirming or denying the move).

The tape is in a **recovery uptrend inside a larger, still-uncertain trading range**:
- Short-term: strongly bullish (price > 10EMA > 50SMA > 200SMA, rising).
- Medium-term: **bullish but at the top of a 3-month distribution box** (164.00 intraday low on 2023-08-17 → 199.62 intraday high on 2023-12-14 per the frozen data; more relevantly, the last two months have traded between ~178.19 and ~199.62).
- Momentum: improving rapidly from an oversold washout, but **structurally weaker than at the December highs** — a nuance that matters for anyone chasing.

Session path that produced this: a decline from the 2023-12-14 close high of **198.11** to a **28.79 RSI low on 2024-01-05**, a retest of ~180.2–180.3 (2024-01-05 low 180.17; 2024-01-17 low 180.30), then a six-session vertical recovery from the 2024-01-17 close of **182.68** to the 2024-01-23 close of **195.18** (+12.50, **+6.84%**). The last two sessions have been consolidation/absorption: 2024-01-24 closed 194.50 and 2024-01-25 closed 194.17, with the 2024-01-25 close printing slightly **below the 2024-01-24 low of 194.34** — a small but real intraday failure at the highs.

---

## 2. Indicator Selection and Rationale

I selected **8 complementary indicators** covering trend (three timeframes), momentum (two independent engines), volatility/band positioning, and volume-price confirmation. Deliberate exclusions: no stochastics (redundant with RSI), no MFI (the snapshot value 0.643 reads as a 0–1 scaled series and is not directly comparable to a 0–100 benchmark here, so I did not lean on it).

| # | Indicator | 2024-01-25 value | Why it is in the set |
|---|---|---|---|
| 1 | **close_10_ema** | 191.0926 | Fastest read on the six-session impulse; defines the short-term trend spine and first dynamic support. |
| 2 | **close_50_sma** | 190.6864 | Medium-term trend/pivot. Currently the key line separating "healthy pullback" from "failed breakout." |
| 3 | **close_200_sma** | 181.7623 | Strategic trend filter and the anchor of the golden-cross structure. |
| 4 | **macd** | 0.8767 | Momentum impulse + zero-line cross detection. |
| 5 | **macds** | −0.2515 | Signal line to date the crossover (occurred 2024-01-19) and gauge remaining runway. |
| 6 | **rsi** | 60.0675 | Overbought/oversold and divergence control in a range-bound tape. |
| 7 | **boll** (+ UB 197.8115 / LB 178.6765) | 188.2440 | Mean-reversion framework: a 20-SMA benchmark, and %B/band-width tell us whether 194 is "stretched" or "mid-range." |
| 8 | **atr** | 3.1774 | Sizing and stop placement; volatility is expanding, which changes stop distances materially. |

Supplementary cross-check (used for confirmation, not as a primary signal): **vwma = 187.7709**.

---

## 3. Trend Structure — Full Bullish Stack, but the Rally Is "Price-Led"

**The moving-average stack is unambiguously bullish and steepening:**

| Layer | Value | Close vs. layer | Slope evidence (frozen data) |
|---|---|---|---|
| Close | 194.17 | — | — |
| 10 EMA | 191.09 | **+1.61%** | 185.37 on 2024-01-17 → 191.09 on 2024-01-25 — a ~5.7-point, 8-session acceleration |
| 50 SMA | 190.69 | **+1.83%** | 189.21 (2024-01-16) → 190.69 (2024-01-25), rising ~0.16/session |
| 200 SMA | 181.76 | **+6.83%** | 177.79 (2023-12-18) → 181.76 (2024-01-25), steadily rising |

- **Golden-cross regime is intact and expanding:** 50 SMA − 200 SMA = **+8.92** points today vs. **+6.36** on 2023-12-18. A widening positive spread means the medium-term trend is not merely intact but strengthening.
- **The critical compression zone is 190.69–191.09.** The 10 EMA and 50 SMA are now only **0.41 points apart** — a tight confluence band. Price closed on 2024-01-25 *above* both, but by less than one ATR (3.18). This is the single most important level cluster on the chart: it is simultaneously the trend-defining 50 SMA and the momentum-defining 10 EMA.
- **Caution — the advance is not volume-confirmed.** VWMA (187.77) sits **3.41% below price** and, notably, **below both the 10 EMA and the 50 SMA**. In a genuinely accumulation-driven advance, VWMA typically tracks or leads price upward. Its position below the 50 SMA tells us the *dollar-weighted* average entry of recent participants is ~187.8, i.e. this rally has been driven by relatively lighter-volume, higher prices rather than heavy institutional accumulation. VWMA has, however, turned up (185.45 on 2024-01-17 → 187.77 on 2024-01-25), so the gap is closing rather than widening — mildly improving, not yet convincing.

---

## 4. Momentum — Two Bullish Crossovers Dated, One Structural Warning

**MACD (0.8767) vs. Signal (−0.2515), Histogram = +1.1282.**

Two clean, datable events occurred:
1. **Bullish MACD/signal crossover on 2024-01-19** — MACD −1.0257 crossed above signal −1.2282 (the prior session, 2024-01-18, had MACD −1.5621 vs. signal −1.2789, i.e. still below).
2. **MACD zero-line cross on 2024-01-23** — MACD +0.1837, the first positive print since 2024-01-03 (+0.0549).

The histogram has expanded for four straight sessions (−1.0287 on 2024-01-16 → +1.1282 on 2024-01-25), which is the cleanest evidence of *accelerating* upside momentum currently on the chart.

**The warning:** momentum recovery is strong in *rate of change* but weak in *level*. On 2023-12-18, when price closed at **195.89** — only ~0.9% above today's close — MACD was **3.5873**. Today, at 194.17, MACD is **0.8767**, roughly **76% lower**. That is a **bearish momentum divergence across the swing structure**: price is retesting the December high zone with far less underlying thrust. RSI confirms the same picture: **64.48 on 2023-12-19** vs. **60.07 now** at a comparable price. Traders should therefore treat a fresh high above ~196–198 as a *momentum-quality test*, not an automatic continuation signal. If price makes a higher high while MACD stays well under ~3.5 and/or RSI fails to exceed ~65, that is a classic exhaustion/divergence setup into a supply zone.

**RSI at 60.07** — not overbought (70 threshold untouched), squarely in the "trend continuation, room to run" band. The full path is instructive: **28.79 on 2024-01-05** (oversold, and the *only* oversold of the period) → 36.71 on 2024-01-17 → reclaim of 50 on **2024-01-18 (51.59)** → peak **62.62 on 2024-01-23** → 60.07 today. The slight RSI easing while price holds near the highs is mild consolidation, not yet a divergence, because price also eased (−0.52% from the 2024-01-23 close). Watch for RSI to fail below ~55 on any renewed push to the highs.

---

## 5. Volatility and Band Positioning — Upper Range, Not Extended

**Bollinger (20, 2σ):** mid **188.2440**, upper **197.8115**, lower **178.6765**.
- **Band width = 19.135 points = 10.16% of the mid-band.** This has *narrowed* from 20.628 (UB 202.951 / LB 182.323) on 2024-01-05, so bands are contracting again after the January expansion — consistent with consolidation after the impulse.
- **%B = 0.81** — price at 194.17 sits 81% of the way from the lower to the upper band, i.e. **upper third but NOT at the upper band**. Distance to the upper band is **3.64 points ≈ 1.15 ATR**. Translation: there is still ~1 ATR of headroom before the band itself begins to cap price. This is a "strong but not stretched" reading, which favors trend-continuation over mean-reversion *unless* the upper band rejects.
- Price is **+5.93 above the mid-band (188.24, +3.15%)**, and the mid-band has flattened/turned up: 188.797 (2024-01-17) → 188.118 (2024-01-22) → 188.244 (2024-01-25). A flattening mid-band is what you want to see before trusting a breakout attempt; it has only just begun to curl.

**ATR = 3.1774 = 1.64% of price — volatility is EXPANDING, not calm.**
- Trough of the recent period: **2.5673 on 2023-12-28**; today 3.1774 = **+23.8% higher**.
- Recent peak: **3.3699 on 2024-01-22**.
- Practical consequence: **1×ATR ≈ 3.18, 1.5×ATR ≈ 4.77, 2×ATR ≈ 6.35**. Stops tighter than ~2.5–3.0 points (0.8–0.9 ATR) are inside the daily noise band and will be hit randomly. A stop just under the 10 EMA/50 SMA cluster (~189.0) is ~5.2 points below close = **~1.6 ATR**, which is a defensible noise buffer.

---

## 6. Support / Resistance Ladder (all levels derived from verified rows and indicator values)

**Resistance**
1. **196.27** — 2024-01-25 intraday high (the immediate rejection point).
2. **197.8115** — Bollinger upper band; a close above this puts price "outside the band," which is a genuine breakout signal in a trend, not a fade.
3. **198.11** — 2023-12-14 close, the highest close in the frozen window (−1.99% from here).
4. **199.62** — 2023-12-14 intraday high, the highest print in the window (−2.73% from here).
5. **~200.00** — psychological round number, coincident with the above supply cluster. Note the 2024-01-04 to 2024-01-11 upper bands (201.99–202.95) bracket this zone, marking where the last two upside attempts died.

**Support**
1. **193.11** — 2024-01-25 low.
2. **191.09** — 10 EMA (short-term momentum spine).
3. **190.69** — 50 SMA (**the line in the sand**; the two above form a 0.41-point confluence band).
4. **188.24** — Bollinger mid-band / 20-SMA (mean reversion target if 190.7 fails).
5. **186.09 open and 185.83 low on 2024-01-18**, versus the 2024-01-17 close of 182.68 — an **unfilled gap-up of ~1.87%** that has not been retested. This is the second-tier support shelf and coincides closely with VWMA (187.77).
6. **182.68** — 2024-01-17 close (the launch point of the current leg).
7. **180.17 / 180.30** — 2024-01-05 and 2024-01-17 lows; a **double bottom** of the January consolidation.
8. **178.6765** — Bollinger lower band (final band support).

---

## 7. Actionable Frameworks

**Bias: constructive/modestly long, but sized for a range top.** The trend stack (price > 10EMA > 50SMA > 200SMA, widening golden cross, MACD above signal and above zero, RSI 60) does not support shorting strength. But price is entering a **known supply shelf (197.8–200) with lower MACD/RSI than the last time it was here**, and volume-weighted price lags by 3.4%. That argues for *buying pullbacks rather than breakouts*, and for taking partial profits into 197.8–199.6.

**Setup A — Pullback long (preferred, higher reward/risk).**
- Entry zone: **191.0–192.0** (10 EMA / 50 SMA confluence, first touch).
- Invalidation: close below **189.0** (below the 50 SMA by ~0.9%, ~1.6 ATR). Hard stop on a *close* basis given expanding ATR.
- Targets: **197.8 (upper band)**, then **199.6 (Dec high)**, stretch to 202.
- Reward/risk at 191.5 entry, 189.0 stop, 197.8 target: risk 2.5, reward 6.3 → **~2.5:1**.

**Setup B — Breakout continuation (lower win rate, needs volume confirmation).**
- Trigger: close **above 196.27**, ideally above **197.81**, with volume **> ~70M** (well above the ~55.5M 20-day average — the 2024-01-18 session at 78.0M is the template).
- Stop: **193.0** (below the 2024-01-25 low, ~1 ATR).
- Target: 199.6 first, 202 second.
- Do **not** take this breakout on average or below-average volume: the VWMA lag already warns that upside participation is thin.

**Setup C — Trend-failure short (tactical, conditional).**
- Trigger: decisive close **below 190.5** (breaking both the 10 EMA and 50 SMA).
- Targets: **188.24** (mid-band) then **186.0** (gap-fill zone) then 182.7.
- Stop: **192.5** (~2 points, ~0.6 ATR — tight, so use smaller size or wait for a retest of 191.5 from below rather than selling the initial break).

**Sizing example (illustrative, 1% account risk):** on a $100,000 account ($1,000 risk) with a 3.5-point stop distance, max position ≈ **285 shares (≈$55.4k notional)**. Because ATR is up ~24% since 2023-12-28, the same percentage-risk rule now yields a *materially smaller* share count than it would have three weeks ago — do not carry a stale position size.

**Invalidation summary:**
- Bullish thesis void on a close **below 189.0**.
- Bearish thesis void on a close **above 197.81** (upper band) with expanding volume.
- **Chase-risk zone: 196.3–198.1** — poor reward/risk for new longs given the momentum divergence vs. December.

**Event risk:** the company's next quarterly earnings release is a known gap catalyst in this timeframe; ATR of 3.18 (1.64%) understates overnight risk around that event, so avoid holding full trend size into it unless that is intentional.

---

## 8. Key Points Table

| Dimension | Reading (2024-01-25) | Interpretation | Actionable Level |
|---|---|---|---|
| **Close** | 194.17 (−0.17% d/d); O 195.22 / H 196.27 / L 193.11 | Small rejection candle; closed below 2024-01-24 low (194.34) | 193.11 first support |
| **Volume** | 54.82M ≈ 0.99× 20-day avg (~55.5M) | No volume confirmation either way on the pullback | Breakout needs >~70M |
| **10 EMA** | 191.09 (+1.61% below price) | Fast trend up; 8-session acceleration | First dynamic support |
| **50 SMA** | 190.69 (+1.83%) | Rising ~0.16/session; the trend pivot | **Line in the sand: 190.7** |
| **200 SMA** | 181.76 (+6.83%) | Long-term uptrend intact | Strategic bull filter |
| **Golden cross** | 50SMA − 200SMA = +8.92 (was +6.36 on 2023-12-18) | Widening = strengthening medium-term trend | Regime stays bullish |
| **MACD** | 0.8767 | Bullish; zero-cross 2024-01-23 | Below 0 = momentum failure |
| **MACD signal** | −0.2515 | Bullish crossover **2024-01-19** | Histogram +1.13, 4 sessions widening |
| **RSI** | 60.07 (from 28.79 on 2024-01-05) | Recovered, not overbought; room to 70 | Divergence watch if it fails <55 on retest of highs |
| **Bollinger** | Mid 188.24 / UB 197.81 / LB 178.68; width 10.16%; %B 0.81 | Upper third, ~1.15 ATR of headroom; mid-band just curling up | 197.81 = breakout trigger / 188.24 = mean-reversion target |
| **ATR** | 3.1774 (1.64% of price); +23.8% since 2023-12-28 | Volatility expanding → wider stops, smaller size | 1.5×ATR ≈ 4.77; 2×ATR ≈ 6.35 |
| **VWMA** | 187.77 (price +3.41% above) | Volume-weighted price lags and sits **below 50 SMA** → thin-participation rally | 185–186 shelf confluence |
| **Momentum divergence** | MACD 0.88 now vs 3.59 at 195.89 close (2023-12-18); RSI 60.1 vs 64.5 | Retesting highs with ~76% less MACD thrust | Treat new highs as a *test*, not confirmation |
| **Primary resistance** | 196.27 → 197.81 → 198.11 → 199.62 → 200 | Dense supply shelf with two prior band rejections (202.0–203.0, Jan 4–11) | Take partials into 197.8–199.6 |
| **Primary support** | 191.09 → 190.69 → 188.24 → 186.0 gap → 182.68 → 180.3 double bottom → 178.68 | Layered, well-defined structure | Bull thesis void <189.0 |
| **Preferred trade** | Buy 191–192 pullback, stop <189.0, target 197.8/199.6 (~2.5:1) | Trend-following with structure behind it | Avoid chasing 196.3–198.1 |

*This is technical analysis for informational purposes, based solely on the frozen 2023-06-01 → 2024-01-25 data and the 2024-01-25 verified snapshot; it is not investment advice. Nothing above constitutes a claimed backtest or verified historical win rate.*