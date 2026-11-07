# AMZN — Technical Analysis Report (as of 2026-08-03)

## 1. Verified market state (source of truth)

From `get_verified_market_snapshot` (2026-08-03), which I cross-checked against the `get_stock_data` series — the two agree exactly on the latest rows, with no discrepancy to flag:

| Field | Value |
|---|---|
| Open / High / Low / Close | 278.29 / 287.20 / 278.00 / **284.02** |
| Volume | 90,830,200 |
| Prior session (2026-07-31) close | 271.58 (vol 129,054,800) |
| Session before (2026-07-30) close | 235.50 (vol 101,839,800) |

AMZN is in a **violent, volume-confirmed upside breakout to new highs** for the visible data window (which begins 2025-11-03).

---

## 2. Anatomy of the move — this is the whole story

The three-session sequence from 2026-07-29 to 2026-08-03 dominates every indicator reading:

- **2026-07-29 close: 226.65** (low 226.16) — the trough of a five-month range low.
- **2026-07-30: close 235.50**, high 239.82.
- **2026-07-31: gap-and-go.** Open 265.00 versus the 7/30 high of 239.82 → a **~10.5% opening gap**. Close 271.58, i.e. **+15.32%** on the day (235.50 → 271.58). Volume 129.05M.
- **2026-08-03: second gap.** Open 278.29 versus the 7/31 high of 273.23. Closed 284.02, **+4.58%**, high 287.20. Volume 90.83M.

Cumulative: **226.65 → 284.02 = +25.3% in three sessions**, and +25.6% from the 7/29 intraday low of 226.16.

Three structural observations:

1. **This clears the entire 2026 range.** The highest *prior* high in the data set was 278.56 (2026-05-05); the highest prior *close* was 274.99 (2026-05-06). On 8/3 AMZN opened at 278.29 — essentially exactly at that old high — dipped to 278.00 (0.56 below it), then closed 284.02, i.e. **unambiguously above the 2026 ceiling**. That is a textbook break-and-hold rather than a failed poke.
2. **Two unfilled gaps remain open**: 239.82–265.00 (7/31) and 273.23–278.29 (8/3). Unfilled gaps in a parabolic leg are both the signature of conviction *and* the most likely magnet on any mean reversion. Thin-air support is the key structural risk here.
3. **Participation is enormous.** Summing the visible sessions from 2026-07-06 to 2026-08-03 gives ~1,002M shares over 21 sessions ≈ **47.7M shares/session average**. 7/31 was ~2.7× that; 8/3 ~1.9×; combined ~4.6× a single average day. This is not a thin-tape squeeze — real volume transacted at higher prices.

Caveat on causality: price data alone cannot confirm *why* this happened. The +15.3% single-session magnitude and the volume signature are consistent with a fundamental catalyst (earnings-type event), but I will not assert a specific catalyst since no tool supports it.

**Quality-of-close nuance:** 7/31 closed in the top ~15% of its range (85.3% of range: (271.58−262.01)/(273.23−262.01)); 8/3 closed at 65.4% of its range ((284.02−278.00)/(287.20−278.00)) — still constructive, but the second day was **weaker on both volume (down ~30%) and closing location**. Follow-through breadth is decelerating, not accelerating.

---

## 3. Trend structure across horizons — fully aligned bullish, but extremely stretched

| Average | 2026-08-03 | Close vs. average |
|---|---|---|
| 10 EMA | 250.22 | **+13.5%** |
| 20-SMA / Bollinger mid | 245.85 | **+15.5%** |
| 50 SMA | 247.01 | **+15.0%** |
| VWMA | 250.17 | **+13.5%** |
| 200 SMA | 235.35 | **+20.7%** |

- **Long-term:** 200 SMA 235.35 is rising steadily (234.75 on 7/30 → 235.01 on 7/31 → 235.35 on 8/3). Price is 20.7% above it — a well-established primary uptrend, and a full year-to-date recovery from the February capitulation (close low 198.79 on 2026-02-13).
- **Medium-term:** 50 SMA sits **above** the 200 SMA (247.01 vs 235.35), so the long-term bullish stack is intact. But note the 50 SMA had been *falling* every session from 256.89 (6/24) to 246.38 (7/30) — a deteriorating intermediate trend. It has only just ticked up (246.38 → 246.63 → 247.01) on the last two days. **The 50 SMA has not yet "caught up" to this breakout**; it is a lagging, mixed signal.
- **Short-term:** the 10 EMA rolled from 236.29 (7/30) to 242.70 (7/31) to 250.22 (8/3). Direction is unambiguously up, but price is 13.5% above it — historically an extreme reading that mean-reverts more often than it persists.

**Key confluence insight:** the 20-SMA (245.85), 10 EMA (250.22), VWMA (250.17) and 50 SMA (247.01) are **clustered in a tight 245.8–250.2 band**. That is the single most meaningful support shelf on the chart — and it is 12–13% below spot. Any serious retest of this cluster would be the highest-quality, lowest-risk long entry, but a trader may have to wait for a 12%+ drawdown to get it.

---

## 4. Momentum — a violent reset, now at the top of the range

**RSI:** 33.31 (7/29) → 44.41 (7/30) → 67.88 (7/31) → **72.23 (8/3)**. This is one of the sharpest RSI repricings possible: from near-oversold to clearly overbought in three sessions. Mechanically this reflects the two gaps far more than a gradual accumulation of buying pressure.

- 72.23 is above the 70 threshold, but in the robust uptrends this indicator flags, RSI can *stay* above 70 for extended periods. **Overbought is not a sell signal here — it's a "do not chase full size" signal.**
- More important is the absence of bearish divergence: RSI made a new high alongside a new price high. There is no evidence of distribution yet.

**MACD:** the line went **−3.63 (7/30) → −0.62 (7/31) → +2.74 (8/3)**, crossing the **zero line on 8/3**. The signal line is at **−0.92**, so the histogram is **+3.66** — i.e. MACD crossed *above* its signal line as well. Two simultaneous bullish triggers (zero-line cross + signal cross) in two sessions.

Nuance: MACD at only +2.74 after a +25% three-day move tells you how deeply negative momentum was beforehand. This is a **fresh momentum regeneration off a weak base, not the continuation of an already-mature trend impulse** — which is constructive for a swing horizon but also means the indicator is "catching up" from below and will need several more sessions to confirm durability.

---

## 5. Volatility — expanding sharply; this changes position sizing, not direction

- **ATR: 6.89 (7/29) → 7.34 (7/30) → 9.51 (7/31) → 9.95 (8/3)** — up ~44% in three sessions. ATR is now **3.50% of price** per day.
- **Bollinger upper band: 258.02 (7/30) → 264.20 (7/31) → 272.99 (8/3)**, middle 245.85, lower 218.71. Band width = 54.28 points = **22.1% of the middle band** — violent expansion.
- **Close is 4.0% above the upper band** (284.02 vs 272.99).

Interpretation: riding/closing above the upper band in a genuine breakout is *normal* and is how strong trends begin — but a 4% overshoot combined with a bandwidth of 22% signals an unstable, news-driven volatility regime. Historically these resolve in one of two ways: (a) sideways consolidation that lets the band "walk up" to price, or (b) a sharp snapback. The single worst assumption right now is that normal volatility will resume immediately.

---

## 6. Volume-price confirmation (VWMA)

VWMA = **250.17**, having risen from 240.82 (7/30). Price is 13.5% above VWMA. The value of this indicator here: VWMA incorporates volume, and it rose **+3.9% in two sessions** — confirming that the breakout was transacted on genuine volume rather than an illiquid drift. If this rally had been hollow, VWMA would have lagged far more. That is a real bullish tell. But the identical 13.5% gap to both VWMA and the 10 EMA underlines that **volume-weighted buyers are, on average, ~34 points underwater relative to the current print** — i.e. profit-taking pressure from recent buyers is a live risk.

---

## 7. Level map and risk parameters (all derived from tool output)

**Overhead:** none from prior price action — 287.20 (8/3 high) is the only reference; it is a new high in the visible window.

**Support ladder:**
| Level | Price | Source |
|---|---|---|
| 8/3 low | **278.00** | First-line intraday support |
| 7/31 high / 8/3 gap top | **273.23 – 278.29** | Gap floor; losing 273.23 opens the gap |
| 7/31 open | **265.00** | Upper edge of the big gap |
| 10 EMA / VWMA / 50 SMA / 20-SMA | **245.85 – 250.22** | The major confluence shelf |
| 200 SMA | **235.35** | Primary trend line of last resort |
| 7/30 high | **239.82** | Bottom edge of the 7/31 gap |

**ATR-based risk references off a 284.02 close:**
- 0.6 ATR → **278.0** (8/3 low; a "tight" but easily violated stop)
- 1.5 ATR → **~269.1**
- 2.0 ATR → **~264.1** — this coincides almost exactly with the **7/31 gap open at 265.00**, making ~264–265 the most logical structural stop for a swing long.

---

## 8. Actionable scenarios

**A. Trend continuation (base case given trend + volume + momentum alignment).** A hold above 278.00 keeps 287.20 in play and, on a decisive close above it, opens blue-sky continuation. Because ATR is ~10 points, expect **±2.5–3.5% daily noise**; a stop tighter than ~1.5 ATR will likely be noise-stopped. Size positions off ATR (cut share count roughly 30–40% versus a month ago, when ATR was ~6.9), not off dollar allocation.

**B. Consolidation / band-walk (bullish, patient).** Sideways trade between roughly 273 and 287 for 1–3 weeks would let the 10 EMA (250.22 and rising ~7–8 points/session) and the 50 SMA converge upward. This is the *healthiest* resolution and the one that offers a low-risk entry without paying a 13.5% extension premium.

**C. Gap-fill mean reversion (the main risk).** A close below 273.23 targets the 265.00 area (2×ATR) and, in a genuinely negative catalyst reversal, the **239.82–265.00** gap. Any long held through that zone is accepting a 15–17% drawdown from spot. Note the 8/3 session already showed *decelerating* volume and a weaker close — the first minor warning shot, not yet a signal.

**Invalidation logic:** bull case intact while price holds above the 273–278 gap zone on a closing basis; structurally broken on a close back below ~250, which would return price to the 20-SMA/50-SMA/VWMA cluster and likely invalidate the breakout entirely.

**What I would *not* do:** initiate a full-size new long at 284.02 with a 2×ATR stop. That is 7% per-share risk at 3.5% daily volatility, 4% above the upper Bollinger band, 13.5% above the 10 EMA, with two unfilled gaps beneath. If participating, scale in (e.g., partial now, partial on a 278–273 retest, partial on the 250 shelf), or wait for the band to catch up.

---

## 9. Indicator selection rationale (8 indicators, non-redundant)

| Indicator | Why it is the right tool for *this* context |
|---|---|
| **close_10_ema** | Most responsive read on the breakout's velocity; quantifies the 13.5% extension that dictates entry timing. |
| **close_50_sma** | Reveals that the intermediate trend was *deteriorating* pre-breakout (256.89 → 246.38) — the nuance most breakout-chasers miss. |
| **close_200_sma** | Confirms the primary uptrend (price +20.7%, 200 SMA rising) and that no death-cross risk exists. |
| **macd** | Caught the zero-line cross on 8/3 and the signal cross (histogram +3.66); I derived the histogram as MACD − signal (2.74 − (−0.92)) rather than spending a slot on `macdh`. |
| **rsi** | The 33 → 72 round-trip is the cleanest evidence of a shock repricing; used to check for divergence, not to call a top. |
| **boll_ub** | Measures band expansion (22.1% width) and the +4.0% overshoot — a volatility-regime signal nothing else in the list provides. |
| **atr** | Essential here: volatility nearly doubled, so stop distance and position size must be recomputed. Anchors the 264–265 and 269 stop logic. |
| **vwma** | Distinguishes a volume-backed breakout from a hollow squeeze; its +3.9% two-session rise confirms real participation. |

Deliberately excluded: `macds`/`macdh` (redundant with `macd`), `boll`/`boll_lb` (one band suffices; middle is derivable), and `stochrsi` (redundant with `rsi`).

⚠️ **Data caveat to flag:** the snapshot reports `mfi = 0.549047`. On a 0–1 scale that equals ~54.9/100 — *neutral money flow* — which sits in tension with RSI at 72.23. This may be a different period/scale convention, so I have **not** used MFI as a signal in this report; I note it only because, if read literally as ~55, it would suggest volume-weighted money flow is *not* confirming the price strength, which would be a meaningful bearish divergence worth verifying independently before relying on it.

---

## 10. Summary table

| Dimension | Reading (2026-08-03) | Interpretation | Actionable implication |
|---|---|---|---|
| **Price** | Close 284.02; High 287.20; Low 278.00 | New high, above entire 2026 range (prior high 278.56 on 2026-05-05) | Breakout confirmed; 287.20 is the only overhead reference |
| **3-session move** | 226.65 → 284.02 = **+25.3%** | Post-catalyst repricing, not a drift | Do not extrapolate; extension risk is high |
| **Volume** | 90.83M vs ~47.7M 21-session avg (1.9×); 7/31 was 129.05M (2.7×) | Genuine participation, but 8/3 volume **down ~30% d/d** | Real move, decelerating follow-through |
| **Close quality** | 65.4% of 8/3 range vs 85.3% on 7/31 | Constructive but weakening | Watch next 1–2 closes for stall |
| **10 EMA** | 250.22 (price +13.5%) | Extreme short-term extension | Avoid tight stops; pullback entries preferred |
| **50 SMA** | 247.01 (price +15.0%); only just turned up after falling from 256.89 on 6/24 | Medium-term trend was damaged pre-breakout | Medium-term signal still catching up |
| **200 SMA** | 235.35, rising (price +20.7%); 50 > 200 | Primary uptrend intact, bullish stack | Strategic bias remains long |
| **RSI** | 72.23 (from 33.31 on 7/29) | Overbought; no bearish divergence | Not a top signal — a sizing signal |
| **MACD** | +2.74 vs signal −0.92; hist +3.66; zero-line cross 8/3 | Fresh bullish momentum regeneration | Supports swing longs, needs confirmation |
| **Bollinger** | Upper 272.99, mid 245.85, lower 218.71; width 22.1%; close +4.0% above UB | Volatility explosion | Expect band-walk or sharp snapback, not calm |
| **ATR** | 9.95 (from 6.89 on 7/29); 3.50% of price | Risk per share nearly +44% | Halve/reduce position size; widen stops |
| **VWMA** | 250.17 (+13.5% below price), up from 240.82 on 7/30 | Volume-weighted buyers far underwater | Profit-taking pressure is a live risk |
| **Support shelf** | 245.85–250.22 (20-SMA/50-SMA/10-EMA/VWMA cluster) | Major confluence, ~12–13% below spot | Highest-quality long-add zone if reached |
| **Stop logic** | 278.0 (0.6 ATR) → 269.1 (1.5 ATR) → **264–265 (2.0 ATR = 7/31 gap open)** | 264–265 is the structural stop | Anything tighter risks noise-stopping |
| **Main risk** | Two unfilled gaps: 273.23–278.29 and 239.82–265.00 | Thin-air support | A close below 273.23 opens 265.00 |
| **Bias** | **Bullish trend, overbought and over-extended short term** | Trend-follow, don't chase full size | Scale entries; ATR-sized risk; invalidate < 250 |