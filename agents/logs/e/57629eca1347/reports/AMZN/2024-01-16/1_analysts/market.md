# AMZN — Technical Assessment as of Tuesday, 16 January 2024

**Data integrity note:** The OHLCV row for 2024-01-16 returned by `get_stock_data` and by `get_verified_market_snapshot` are identical (O 153.53 / H 154.99 / L 152.15 / C 153.16 / V 41.38M), and every indicator value quoted below is taken from the verified snapshot or from the indicator series computed on that same frozen row set. No conflicts to flag. The snapshot also returns an `mfi` field (0.443756) whose scaling is ambiguous (looks 0–1 normalized rather than 0–100), so it is deliberately excluded from the analysis.

---

## 1. Verified data baseline (2024-01-16)

| Field | Value |
|---|---|
| Close | **153.16** |
| Open / High / Low | 153.53 / 154.99 / 152.15 |
| Volume | 41,384,600 |
| 50 SMA | 147.5492 |
| 200 SMA | 130.3187 |
| 10 EMA | 152.0450 |
| MACD / Signal | 1.6497 / 1.5694 (hist +0.0803) |
| RSI(14) | 57.373 |
| Bollinger mid / upper / lower | 151.7325 / 157.6983 / 145.7667 |
| ATR | 3.0379 |
| VWMA | 150.9839 |

---

## 2. Trend structure: primary uptrend intact and unusually extended

**Long-term (200 SMA = 130.32).** The 200-day average has risen monotonically through the entire visible window — 120.37 on 2023-11-17 to 130.32 on 2024-01-16, i.e. roughly +9.95 points, or +8.3%, in two months. A steadily rising 200 SMA is the cleanest evidence available that the primary trend is up. The close of 153.16 sits **+17.53% above** the 200 SMA.

**Medium-term (50 SMA = 147.55).** The 50 SMA has climbed without a single down-tick in the whole lookback (133.72 on 2023-11-17 → 147.55 on 2024-01-16, +10.3%). The 50/200 spread has widened from +13.35 points on 2023-11-17 to **+17.23 points** on 2024-01-16, confirming trend acceleration rather than decay. Price is **+3.80% above** the 50 SMA.

**Interpretation:** Trend-following filters (price > 50 SMA > 200 SMA, both rising) are unambiguously bullish. The nuance is *distance*: an ~17.5% premium to the 200 SMA is a stretched condition, which raises the cost of chasing strength and argues for buying pullbacks into the moving-average cluster rather than breakout extensions.

---

## 3. Short-term structure: churn, a failed push at highs, and a two-session fade

The last four weeks have been a **range/consolidation phase layered on top of the uptrend**, and the details matter:

- **29 Dec 2023 close 151.94 → 16 Jan 2024 close 153.16** = +0.80% across eleven sessions. Essentially a churn box.
- **The January dip:** close fell from 149.93 (2 Jan) to **144.57 (4 Jan)**, with an intraday low of **144.05**. On that date the 50 SMA was **144.3024** — the low pierced the 50-day average by ~0.25 points and the session closed **back above it** (144.57). The following five sessions all closed higher: 145.24, 149.10, 151.37, 153.73, **155.18 (11 Jan)**. That is a documented dip-and-reclaim of the 50 SMA, not an assumed one.
- **The impulse:** 144.57 → 155.18 = **+7.34% in five sessions**.
- **The fade:** 11 Jan's 155.18 was the highest close in the entire dataset (its intraday high of **157.17** was also the highest high), but the next two sessions reversed: 154.62 on 12 Jan (−0.36%) and **153.16 on 16 Jan (−0.94%)**. Cumulatively −1.30% off the closing high, retracing about 18% of the January impulse.
- **The 1/16 candle is weak on its face:** open 153.53, high 154.99, low 152.15, close 153.16 — a close near the session low and roughly in the bottom of a 2.84-point range (≈0.94 ATR). Likewise 1/11 closed at 155.18 after tagging 157.17, leaving a ~2-point upper shadow. Both suggest supply overhead near 155–157.

**Key structural read:** the 11 Jan high of 157.17 exceeded the December swing highs (155.12 on 19 Dec; **155.63 on 20 Dec**) and then closed back inside the December range within two sessions. That is an *unconfirmed breakout attempt* — treat 155.6–157.2 as the overhead decision zone and 151.7–149.1 as the near-term demand shelf, until price resolves.

---

## 4. Momentum: reset, re-cross, but with a mild negative divergence

- **RSI 57.37**, mid-range. It collapsed from 68.05 (18 Dec) to **40.23 (4 Jan)** — a full reset to neutral without reaching 30 — then recovered to 62.79 (11 Jan) before easing to 61.27 and 57.37. No overbought/oversold constraint is currently binding, which leaves room in either direction. The relevant nuance: **RSI was 62.79 on 11 Jan with price at a new high (155.18), versus 68.05 on 18 Dec with price at 154.07** — a mild negative divergence (lower momentum oscillator on a marginally higher price).
- **MACD 1.6497 vs signal 1.5694, histogram +0.0803.** The MACD line peaked at 3.136 on 22 Dec, decayed to a trough of 0.779 on 8 Jan (histogram −1.230 on 5 Jan), and has since rebuilt to 1.650. The histogram crossed back positive on **12 Jan (+0.0937)** and printed **+0.0803 on 16 Jan** — a fresh bullish MACD crossover, but one whose histogram is already *contracting* by ~14% day-over-day. Early-cycle crossovers with shrinking histograms are the least reliable variety.
- Same divergence framing on MACD: **1.463 MACD on 11 Jan at 155.18 vs 3.136 on 22 Dec at 153.42** — momentum is not confirming the marginal high.

**Net:** momentum is *improving but not confirming*. This is a consolidation signature, not a fresh acceleration signature.

---

## 5. Volatility and the price envelope

- **ATR 3.0379 ≈ 1.98% of price.** ATR has contracted from 3.446 (18 Dec) and 3.423 (20 Dec) — quiet, orderly tape. Useful, concrete risk math: 1×ATR ≈ 3.04 pts, 1.5×ATR ≈ 4.56 pts, 2×ATR ≈ 6.08 pts.
- **Bollinger (20, 2σ): mid 151.73, upper 157.70, lower 145.77.** Bandwidth = **7.86%** of the mid-band — a compressed envelope. Price at 153.16 sits above the mid-band (+0.94%) but **4.54 points (≈2.9%) below the upper band**, i.e. *not* riding the band. Squeeze-like compression ahead of the 155–157 decision zone implies an expansion move is more likely than continued drift, and ATR-based sizing is the right frame for it.
- Note the lower band (145.77) is now *above* the 4 Jan low (144.05) and above the 4 Jan close — the envelope itself has been lifted by the rally, which is consistent with a rising floor.

---

## 6. Volume: participation is the weakest link

- **VWMA 150.98**, price **+1.44%** above it. VWMA has been virtually flat since 3 Jan (151.25 → 150.98), meaning the volume-weighted cost basis of recent buyers sits at ~151. Price is comfortably above it — holders are in profit — but the flat VWMA tells you the December–January rally has not been *volume-expanding*.
- **Volume evidence:** 20-session average volume (15 Dec–16 Jan) is ≈**46.0M**; excluding the 15 Dec quad-witching print of 110.1M it is ≈**42.6M**. The 16 Jan volume of **41.4M is below both**. Constructively, the two down sessions (12 Jan 40.5M; 16 Jan 41.4M) came on *lighter* volume than the 11 Jan up session (49.1M) — consistent with orderly profit-taking rather than distribution. But the 12 Jan–16 Jan fade also shows no dip-buying surge yet.
- The late-December advance was on notably thin volume (25.1M on 26 Dec, 27.1M on 28 Dec, 31.4M on 27 Dec) — the 151–155 shelf was built without conviction. That is precisely why the 155.6–157.2 breakout zone needs a volume confirmation.

---

## 7. Actionable framework

**Bias: constructive/trend-following, but not chase.** The primary trend is strong and orderly; short-term momentum is only partially repaired and the tape is compressing under a twice-rejected 155–157 zone.

- **Do not buy the extension.** At 153.16 the stock is +0.73% over the 10 EMA and +0.94% over the 20 SMA — a poor risk/reward entry against a 155.6–157.7 wall, with the last two sessions closing weak.
- **Primary long entry zone: 151.7 → 150.9** (Bollinger mid 151.73 / VWMA 150.98), with a second add zone **149.1 → 148.4** (8 Jan close 149.10; 2 Jan low 148.39). Initial stop reference: **below 147.55** (50 SMA) — roughly 2×ATR below the first entry — because the 4 Jan dip-and-reclaim makes the 50 SMA the operative trend line.
- **Breakout confirmation trigger:** a daily close **above 155.63** (20 Dec high) and then **157.17/157.70** (11 Jan high / upper band), accompanied by volume **> ~46M** (20-day average). Without that volume, treat any push above 157 as suspect.
- **Bear-case trigger:** a daily close **below 148.39** breaks the January higher-low sequence and puts the **147.55** 50 SMA and then the **144.05** (4 Jan low) / 145.77 (lower band) area in play. A close below the 50 SMA would be the first structural break of the Oct–Jan uptrend.
- **Sizing:** use 1.5–2.0×ATR (4.6–6.1 points) as the nominal stop distance and scale position size inversely — at ~2% ATR, normal-sized risk is appropriate, but the compressed Bollinger bandwidth argues against assuming the current low-volatility regime persists.
- **What would change the view:** MACD histogram flipping back negative (below 0) while price sits under 153, or a third rejection at 155.6–157.2 on rising down-volume — either would shift the read from "consolidation in an uptrend" to "distribution at the highs."

**Indicator-selection rationale (8 chosen, complementary, non-redundant):** `close_200_sma` and `close_50_sma` anchor strategic and medium-term trend plus the extension measurement; `close_10_ema` provides the only fast entry-timing input; `macd` + `macdh` split the crossover event from its *strength* (critical here, since the cross just occurred but the histogram is fading); `rsi` supplies an independent, differently-constructed momentum read and the divergence check; `atr` converts the setup into stop and size numbers; `vwma` is the sole volume-integrating measure and is what invalidates or validates the breakout zone. Bollinger bands were also inspected (mid/upper/lower from the verified snapshot) as the volatility envelope but are treated as supplementary context rather than a ninth selection.

---

## 8. Summary table

| # | Indicator | Value (2024-01-16) | Signal | Evidence & interpretation |
|---|---|---|---|---|
| 1 | **200 SMA** | 130.3187 | Bullish (extended) | Rose 120.37 (11/17) → 130.32; close is **+17.53%** above. Strategic uptrend intact; extension argues against chasing. |
| 2 | **50 SMA** | 147.5492 | Bullish | Unbroken rise 133.72 (11/17) → 147.55; 50/200 spread widened +13.35 → +17.23 pts. Close **+3.80%** above. Key stop reference. |
| 3 | **10 EMA** | 152.0450 | Neutral / mild bullish | Rebuilt from 149.10 (1/5) to 152.04; close only +0.73% above → no short-term edge at current price. |
| 4 | **MACD** | 1.6497 (sig 1.5694) | Bullish crossover, fragile | Recovered from 0.779 (1/8) past the signal; but 1.463 at the 1/11 high vs 3.136 on 12/22 = mild negative divergence. |
| 5 | **MACD histogram** | +0.0803 | Fading positive | Turned positive 1/12 (+0.0937), now −14% d/d. Trough was −1.230 (1/5). New-cross momentum is not strengthening. |
| 6 | **RSI(14)** | 57.373 | Neutral | Reset 68.05 (12/18) → 40.23 (1/4) → 62.79 (1/11) → 57.37. No threshold binding; 62.79 at 155.18 vs 68.05 at 154.07 = mild bearish divergence. |
| 7 | **ATR** | 3.0379 (≈1.98%) | Volatility contracting | Down from 3.446 (12/18). 1×ATR=3.04, 1.5×=4.56, 2×=6.08 pts for stops/sizing. |
| 8 | **VWMA** | 150.9839 | Constructive but unconfirmed | Close +1.44% above; VWMA flat since 1/3 (151.25→150.98). Rally lacks volume expansion; 1/16 volume 41.4M vs ~46.0M 20-day avg. |
| — | Bollinger (supplementary) | mid 151.73 / UB 157.70 / LB 145.77 | Compression | Bandwidth 7.86%; close 4.54 pts below UB — not riding the band. Overhead wall 155.6–157.7. |
| — | **Key levels** | — | — | Resistance 155.18 close / 155.63 (12/20 H) / 157.17–157.70. Support 152.04 (10 EMA), 151.73 (20 SMA), 150.98 (VWMA), 149.10–148.39, 147.55 (50 SMA), 145.77 / 144.05. |
| — | **Stance** | — | Buy dips, don't chase | Accumulate 151.7→150.9 and 149.1→148.4; stop under 147.55; require >~46M volume to trust a break of 155.6–157.2; bear trigger = close < 148.39. |