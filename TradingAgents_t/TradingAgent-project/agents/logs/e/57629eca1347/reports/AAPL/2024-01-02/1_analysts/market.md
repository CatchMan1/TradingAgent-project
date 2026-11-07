# AAPL — Technical & Price-Action Report
**As of the close of 2024-01-02** | Data source of truth: verified market snapshot for AAPL, 2024-01-02 (all indicator values below match exactly between `get_indicators` and the verified snapshot — no discrepancy found)

---

## 1. The Session That Matters: 2024-01-02

The first trading day of 2024 was an outlier event for AAPL, and it reshapes the entire short-term technical picture.

| Field | Value (verified 2024-01-02) |
|---|---|
| Open | 187.15 |
| High | 188.44 |
| Low | 183.89 |
| **Close** | **185.64** |
| Volume | 82,488,700 |
| Prior close (2023-12-29) | 192.53 |

Key measurable facts:

- **Gap-down open of 5.38 points** from the 192.53 close to the 187.15 open (−2.79%). The entire 187.15–192.53 zone is **unfilled gap resistance** — the day's high of 188.44 never even reached the prior close.
- **Close-to-close decline of −3.58%** (192.53 → 185.64), the single largest one-day percentage drop visible in the 30-row verification window.
- The close is **−6.30% below the 2023-12-14 closing high of 198.11**, and **−7.00% below the 2023-12-14 intraday high of 199.62**.
- **Volume 82.49M** was roughly **1.55× the ~53.2M average of the 20 sessions from 2023-12-01 to 2023-12-29** (my arithmetic from the snapshot rows) and the heaviest session since 2023-12-15's 128.5M options-expiration print. This is **high-volume distribution**, not a quiet pullback.
- The session closed in the **lower third of its range** (close 185.64 vs. range 183.89–188.44 → ~34% of range), meaning sellers held control into the bell rather than buying the dip.

**Nuance:** a single large down day on heavy volume at the start of a new calendar year is exactly the kind of session that mixes genuine repricing with tax-year/positioning flow. The technical structure below tells us whether this is a one-day flush or a trend change.

---

## 2. Trend Structure: Primary Uptrend Intact, Intermediate Trend Broken

**Moving-average stack (2024-01-02):**

| MA | Value | Close vs. MA |
|---|---|---|
| 10 EMA | 192.40 | **−3.51%** (price below) |
| 50 SMA | 186.84 | **−0.64%** (price below) |
| 200 SMA | 179.64 | **+3.34%** (price above) |
| VWMA | 194.59 | **−4.60%** (price below) |

Interpretation:

1. **Short-term trend has flipped down decisively.** The 10 EMA has rolled over from 195.51 (12/19) to 192.40, and price is now 6.76 points beneath it. The 10 EMA is also converging on the 50 SMA; a 10/50 bearish cross would confirm the intermediate-trend break.
2. **The 50 SMA is the line in the sand right now.** It sits at 186.84, only 1.20 points above the close. Critically, the 50 SMA has been *below* price for the entire visible 30-session window (it printed 179.74 on 12/04 while price was 189.43), and **2024-01-02 is the first close in that window beneath it**. Note the 50 SMA is still *rising* (+0.20/session: 186.63 → 186.84), so this is a fresh, unconfirmed loss of the medium-term average — a reclaim within 1–3 sessions is still very achievable.
3. **The primary (long-term) uptrend is not broken.** Price is still +3.34% above a steadily rising 200 SMA (175.45 on 12/04 → 179.64 on 01/02), and the 50 SMA (186.84) remains comfortably above the 200 SMA (179.64), a positive-slope spread of +7.20 points — the post-golden-cross structure is intact. The October higher low at 165.67 (10/26 intraday low) versus the November higher low at 170.12 (11/01 low) remains valid; the 01/02 low of 183.89 does not yet violate any major swing low.

**So the hierarchy is:** long-term up (200 SMA, rising) → intermediate up but cracking (50 SMA, price just lost it) → short-term down (10 EMA, sharply declining). This is a **pullback within an uptrend until proven otherwise, but a pullback with unusual institutional force behind it.**

---

## 3. Momentum: Deterioration Was Visible *Before* the Break

**MACD complex:**

| Date | MACD | Signal | Histogram |
|---|---|---|---|
| 2023-12-08 | 3.551 | 3.458 | +0.093 |
| 2023-12-11 | 3.419 | 3.450 | **−0.031 (bearish cross)** |
| 2023-12-15 | 3.751 | 3.570 | +0.181 |
| 2023-12-22 | 2.636 | 3.237 | −0.600 |
| 2023-12-29 | 1.558 | 2.425 | −0.867 |
| **2024-01-02** | **0.782** | **2.097** | **−1.314** |

- The **MACD line has fallen for ten consecutive sessions** (3.751 on 12/15 → 0.782 on 01/02), a 79% collapse in the momentum reading in under three weeks. The signal line has now rolled over too (3.570 → 2.097), confirming that this is decelerating momentum, not a transient blip.
- The **histogram at −1.314 is the most negative print in the visible window** and worsened from −0.867 the prior session — downside momentum is *accelerating*, not stabilizing.
- **Important nuance:** the MACD line at 0.782 is **still above zero**. Absolute momentum remains positive; a zero-line cross (likely within 1–3 sessions at the current rate of decay) would be the next, more serious bearish confirmation.

**RSI:** 35.37, down from 51.06 on 12/29 and from the 69.49–69.69 zone on 12/13–12/14.

- A one-session RSI drop of ~15.7 points is extreme and consistent with capitulation-style selling. RSI is **not yet at the 30 oversold threshold** — there is still room to fall before a mechanical mean-reversion signal triggers.
- **Bearish divergence confirmed in hindsight:** RSI peaked at **70.02 on 2023-12-08** and then made a **lower high of 69.49 on 12/13 / 69.69 on 12/14** while price made a **higher high (198.11 close on 12/14)**. Momentum failed to confirm the final price push — a textbook warning that preceded the 01/02 breakdown.
- In the context of a rising 200-day trend, RSI in the mid-30s is historically a *watch-for-stabilization* zone rather than an automatic buy signal. The distinguishing factor will be whether volume dries up on subsequent down days.

---

## 4. Volatility: Bands Breached, ATR Expanding

**Bollinger Bands (20, 2σ):** middle 194.03 | upper 199.85 | lower 188.21 | bandwidth 11.64 points (≈2σ = 5.82, implying ~2.91 points of daily-scale dispersion).

- **The close of 185.64 is 2.57 points BELOW the lower band (188.21)** — a full outside-band close. In %B terms: (185.64 − 188.21) / 11.64 ≈ **−0.22**, i.e., 22% of a band-width below the lower band, roughly **2.9 standard deviations below the 20-SMA**. This is a statistically stretched condition that historically resolves either by (a) a sharp snap-back toward the middle band (194.03), or (b) the bands widening downward as a trend leg develops. The tiebreaker is the volume/ATR picture.
- The middle band at 194.03 is essentially where the **10 EMA (192.40) and the unfilled gap (187.15–192.53)** live — a very dense overhead supply cluster between ~188 and ~194.

**ATR:** 3.008, up from 2.575 the prior session (**+16.8% in one day**) and from 2.65–2.85 through late December.

- ATR at ~1.62% of price means average daily movement is now roughly 3 points. **Practical consequence: any stop placed closer than ~1×ATR (3 points) to an entry is inside normal noise.** A conventional 2×ATR stop is ~6 points.
- Rising ATR plus a downside band break plus heavy volume = the market is *repricing risk*, and position sizes should be cut mechanically (to keep dollar risk constant, size should shrink by roughly the inverse of the ATR increase, i.e., ~15–20% smaller than December sizing).

---

## 5. Volume & Participation: Confirming Distribution

- **VWMA at 194.59** versus a close of 185.64 means the volume-weighted average holder from the last 20 sessions is **underwater by 4.60%**. The VWMA has been flat-to-falling for four sessions (195.53 on 12/26 → 194.59), while price has fallen much faster — the classic "trapped-supply" configuration where rallies into 192–195 will meet sellers trying to get out at breakeven.
- The **188–195 zone** therefore carries three independent forms of overhead supply: the VWMA (194.59), the Bollinger mid-band (194.03), and the 10 EMA (192.40), plus the unfilled gap on top. A rally that stalls below ~192 should be treated as a lower high, not a recovery.
- The **82.49M shares on 01/02 (≈1.55× the 20-day average)** gives the day's price action much more informational weight than a low-volume drift. Note the sequence in late December: volumes of 28.9M–48.1M on 12/26–12/29 (holiday-thin) followed by a 82.5M distribution day — the thin tape masked the weakness until the first full-liquidity session.

---

## 6. Levels and Scenarios

**Resistance (overhead):**
- **186.84** — rising 50 SMA (immediate, 1.2 pts away)
- **188.21** — Bollinger lower band (re-entry would neutralize the outside-band break)
- **188.44** — 01/02 session high
- **192.40–192.53** — 10 EMA + 01/02 gap top / 12/29 close (**the level that must be reclaimed to negate the breakdown**)
- **194.03–194.59** — Bollinger mid-band + VWMA
- **199.62/199.85** — 12/14 swing high + Bollinger upper band

**Support (below):**
- **183.89** — 01/02 session low (first test; a break reopens downside)
- **~179.64** — **rising 200 SMA** (principal trend support, +3.34% below price)
- **~177–178** — 20-day range measured-move objective: the Nov–Dec closing range was roughly 187.45 (12/04 low) to 198.00–199.62 (12/13–12/14 highs), a height of ~10.5–12 points; projecting that below the 187.45 range floor points at **≈177**, which conveniently coincides with the rising 200 SMA as it drifts higher
- **173.35** — 11/03 low (deeper structural support if 200 SMA fails)
- **165.67** — 10/26 low (primary uptrend's last major swing low; a break there would invalidate the multi-month uptrend)

**Scenario map:**

| Scenario | Trigger (verified levels) | What it would mean |
|---|---|---|
| **A. Mean-reversion bounce** (most likely tactically) | Hold 183.89; RSI < 30 on declining volume; close back above 186.84 (50 SMA) | Snap-back toward 188.21 (BB lower) then 192.4–192.5 (10 EMA / gap top). The overhead cluster makes ~192 a natural cap on a first bounce. |
| **B. Continued slide into trend support** | Close below 183.89 | Next magnet is the 200 SMA at ~179.64, with a measured-move objective of ~177. Downside is roughly 3.3–4.6% from the 185.64 close, i.e., about 2×ATR. |
| **C. Breakdown of the primary trend** | Close below the 200 SMA (~179.64) that then fails to reclaim | Would flip the long-term structure; next references 173.35 then 165.67. Not the base case — the 200 SMA is still rising. |
| **D. Full repair** | Reclaim 192.53 (prior close gap fill) and then 194.59 (VWMA) | The 01/02 session becomes a one-day flush; MACD histogram would need to flatten first (watch for a zero-line hold on MACD near 0.78). |

---

## 7. Why These Eight Indicators Were Selected

The market context is: **a mature, high-multiple mega-cap uptrend that just printed its biggest one-day decline in the visible window on 1.5× normal volume, closing below its 20-day lower Bollinger band while still above a rising 200-day average.** That context demands (a) a multi-timeframe trend map, (b) a momentum-deceleration read, (c) a volatility/stretch read, and (d) a volume-participation read — with no duplicated information.

| Indicator | Why it earns a slot here |
|---|---|
| **close_200_sma** | The only thing separating "deep pullback" from "trend change." At 179.64 and rising, it defines the invalidation line and anchors the downside target set. |
| **close_50_sma** | The level just lost (186.84). Its *slope* (still rising at +0.20/day) is the key nuance distinguishing a fresh crack from an established downtrend. |
| **close_10_ema** | Fastest read on the momentum flip (195.51 → 192.40) and the first overhead magnet on any bounce. Non-redundant with the SMAs because of its responsiveness. |
| **macd** | Quantifies the ten-session momentum collapse (3.75 → 0.78) and flags that absolute momentum is still positive — a critical nuance a moving average alone can't express. |
| **macds** | Required to interpret the MACD line: confirms the bearish cross on 12/11 and the −1.314 histogram (widest in the window), i.e., *accelerating* downside momentum. |
| **rsi** | Captures the stretch (35.37) and documents the December bearish divergence (RSI 70.02 on 12/08 vs. lower high 69.69 on 12/14 against a higher price high). Not redundant with MACD because it's a bounded oscillator measuring the *extremity* of the move, which MACD does not. |
| **atr** | Directly actionable: 3.01 (up 16.8% in one session) sets stop distance, position size, and the validity of any support level. Volatility-based, not directional — zero overlap with the rest. |
| **vwma** | The only volume-aware indicator chosen. At 194.59 vs. price 185.64, it identifies trapped supply and hard-caps the bounce zone independently of the BB/EMA cluster — plus it confirms the 82.5M volume day was distribution. |

*Deliberately excluded:* `boll_ub`/`boll_lb` were reviewed (values pulled in the verified snapshot: 199.85 / 188.21) but not selected as separate slots because `boll_lb` would duplicate the oversold-stretch information already carried by RSI plus ATR; the band levels are still cited in the analysis above from the verified snapshot. `macdh` was omitted as it is mechanically implied by `macd − macds`. `boll` (middle band) overlaps heavily with `close_10_ema`/`vwma` in the 192–195 zone.

---

## 8. Actionable Summary

1. **Bias: tactically bearish, strategically still bullish.** The 200 SMA (179.64, rising) has not been threatened; the 50 SMA (186.84) has just been lost for the first time in the visible window.
2. **Do not buy the band-break blindly.** The close is ~2.9σ below the 20-SMA with a −1.314 MACD histogram and rising ATR — that combination more often extends than reverses immediately. Wait for either (a) a close back above 186.84 with MACD histogram contracting, or (b) RSI below 30 *with* volume contracting, before scaling into longs.
3. **For new longs, the risk reference is 183.89 (01/02 low)**; with ATR at 3.01, a stop tighter than ~3 points is noise. A 2×ATR stop from a bounce entry near 187 implies roughly a 181 stop, which sits just above the 200 SMA — a technically coherent structure.
4. **For shorts/hedges, the risk reference is 192.53** (gap fill / prior close). Reward-to-risk toward 179.6–177 is approximately 3:1 from the 185.64 close against a ~6.9-point stop.
5. **Watch three specific confirmations over the next 1–3 sessions:** (i) MACD's zero-line cross from 0.782, (ii) a 10 EMA/50 SMA bearish cross (10 EMA 192.40 falling toward 186.84), and (iii) whether volume on down days stays above ~53M or dries up.
6. **Data caveat:** the verified snapshot also reports an `mfi` value of 0.339. Money Flow Index is bounded 0–100, so this print is off-scale and should be treated as unreliable rather than as an extreme oversold reading. I have not used it. No other conflicts were found between `get_indicators` and the verified snapshot — all eight values I cite match the snapshot exactly.

---

## Key Points Table

| Category | Indicator / Metric | Level (2024-01-02) | Signal | Actionable Read |
|---|---|---|---|---|
| Price | Close / Open / High / Low | 185.64 / 187.15 / 188.44 / 183.89 | Strongly bearish session | Gap-down −2.79%, closed near lows |
| Price | vs. 2023-12-14 close (198.11) | −6.30% | Correction underway | −7.00% from 199.62 intraday high |
| Volume | Session volume | 82.49M | ~1.55× 20-day avg (~53.2M) | Distribution, not drift |
| Trend – short | close_10_ema | 192.40 | Price −3.51% below, EMA rolling over | First overhead magnet on bounce |
| Trend – medium | close_50_sma | 186.84 | Price −0.64% below; **first close below in 30-session window** | Key pivot; reclaim negates breakdown |
| Trend – long | close_200_sma | 179.64 | Price +3.34% above; still rising | Primary uptrend intact; invalidation line |
| Momentum | macd | 0.782 (from 3.751 on 12/15) | 10-session collapse, still >0 | Zero-line cross is next bearish trigger |
| Momentum | macds | 2.096 | MACD below signal since 12/11 | Confirms bearish momentum regime |
| Momentum | macd histogram (derived) | −1.314 | Widest negative in window | Downside momentum accelerating |
| Momentum | rsi | 35.37 (from 51.06) | Approaching but above 30; Dec bearish divergence | Not yet a mechanical buy |
| Volatility | boll_lb / boll (snapshot) | 188.21 / 194.03 | Close 2.6 pts below lower band (%B ≈ −0.22) | ~2.9σ stretch; snap-back or band-walk |
| Volatility | atr | 3.008 (+16.8% d/d) | Expanding | Stop ≥3 pts; size down ~15–20% |
| Volume | vwma | 194.59 | Price −4.60% below | Trapped supply caps 192–195 rallies |
| Levels | Resistance | 186.84 → 188.21 → 192.4/192.53 → 194.0/194.6 → 199.6/199.9 | Dense cluster | Rally into 192 likely a lower high |
| Levels | Support | 183.89 → ~179.64 (200 SMA) → ~177 (measured move) → 173.35 → 165.67 | Staged | 179.6–177 is the high-probability downside zone |
| Scenarios | A / B / C / D | Hold 183.89: bounce to 192 / break 183.89: 200 SMA test / lose 179.64: trend change / reclaim 192.53: repair | — | Tactically bearish, strategically bullish |