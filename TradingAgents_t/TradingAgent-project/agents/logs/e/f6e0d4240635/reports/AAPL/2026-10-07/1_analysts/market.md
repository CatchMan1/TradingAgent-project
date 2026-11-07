# AAPL — Technical Analysis & Trading Plan
**As of close 2026-10-07** | Analysis basis: daily OHLCV 2026-03-02 → 2026-10-07 (153 sessions), point-in-time data

---

## 1. Verified market state (source of truth)

The `get_stock_data` series and the `get_verified_market_snapshot` agree row-for-row on the 2026-10-07 bar — **no discrepancy to flag**.

| Field | Value (2026-10-07) |
|---|---|
| Open | 336.96 |
| High | 338.67 |
| Low | 332.78 |
| **Close** | **336.67** |
| Volume | 34,147,900 |
| Prior close (10-06) | 333.63 → **+0.91%** |
| Dividend adjustment | none on the bar (last ex-div 0.27 on 2026-08-10) |

Snapshot indicator set (10-07): 50SMA 322.28 · 200SMA 290.08 · 10EMA 334.13 · MACD 3.272 · Signal 4.088 · Histogram −0.816 · RSI 57.68 · Boll mid 334.48 / upper 341.90 / lower 327.05 · ATR 6.58 · VWMA 335.56.

---

## 2. The big picture: a mature uptrend that has stopped making progress

AAPL's primary trend is unambiguously up. From the 2026-03-30 closing low of **246.63** to today's **336.67**, the stock is **+36.5%** in roughly six months. But the character of the trend has changed materially since late July, and the last three months are best described as **a high-level base/digestion phase inside a larger uptrend**, not a fresh impulse leg.

Three distinct regimes are visible in the data:

1. **March–July advance (246.63 → 344.57 intraday high on 2026-07-29).** Persistent higher highs and higher lows, with pullbacks consistently shallow.
2. **The 2026-07-31 air pocket.** The stock closed 333.43 on 07-30, then *opened at 304.81* and closed at **308.91 — a −7.36% single-session loss on 132.5M shares** (roughly 3× the surrounding volume). This is the single most important risk event in the sample, and it happened without any precursor in the technical data.
3. **August base → September recovery → October compression.** A base at 302–320 in August, a rally to **345.34 intraday on 2026-09-22** (a marginal +0.22% higher high than the July 344.57 print) and **341.07 close on 2026-09-25** (the highest close in the sample), followed by a tight 329.40–341.07 close-to-close coil over the last nine sessions.

**The key structural read:** price is now essentially unchanged versus the 2026-07-28 close of 340.08 (−1.0%). Two and a half months of work, including a 7%+ shock, have produced **zero net progress on a closing basis**. That is the definition of a distribution/consolidation range near highs — bullish *if* it resolves upward, but it deserves respect as a two-sided zone until it does.

---

## 3. Indicator selection and rationale

I selected eight complementary indicators covering trend (two horizons), short-term momentum/mean-reversion, volatility regime, and volume-weighted confirmation. Redundancy was deliberately avoided (e.g., no separate MACD signal line in the table — its value is derived and quoted; no stochastics alongside RSI).

**Why this set fits the current context:** the dominant features right now are (a) an intact but flattening uptrend, (b) a volatility squeeze, and (c) a momentum reset that has not yet become a downtrend. That combination demands trend anchors to keep us on the right side, oscillators to time entries into a range, a volatility measure for sizing/stops, and a volume-weighted price to judge whether holders are in profit.

### 3.1 `close_50_sma` — 322.28 (rising, but decelerating)
- Price is **+4.47%** above it. The 50SMA has risen every session in the sample, but the *rate* has collapsed: 315.80 (09-08) → 318.46 (09-14) is **+0.67/session**, while 322.09 (09-30) → 322.28 (10-07) is **+0.04/session**.
- Interpretation: the medium-term trend is still up but has gone flat. This is typical of a trend digesting, not of a trend breaking — the line is not yet rolling over.
- **Actionable level:** 322.28 is the medium-term line in the sand. A daily close below it would be the first objective evidence that the September uptrend has failed.

### 3.2 `close_200_sma` — 290.08 (rising)
- Price is **+16.06%** above it; the 50SMA sits **32.20 points (+11.1%)** above the 200SMA, a firmly established golden-cross configuration with no threat of inversion.
- The 200SMA is still climbing ~+0.31/session, confirming the long-term bid.
- **Use:** strategic filter only. It is far too distant to be a trading level; its role is to say "do not short this name on a swing basis."

### 3.3 `close_10_ema` — 334.13 (turning up)
- Price is **+0.76%** above it; the 10EMA bottomed at 333.55 on 10-05 and has ticked up to 334.13.
- It has converged almost exactly with the 20-day/Bollinger midpoint (334.48), creating a **dense 334.1–334.5 short-term pivot cluster**.
- **Use:** the fastest objective read on whether the two-week drift is resolving higher. Holding above 334 keeps the short-term bias constructive.

### 3.4 `macd` — 3.272 (bearish crossover intact, momentum decelerating)
- MACD peaked at **6.248 on 2026-09-22** and has fallen **−47.6%** since.
- It crossed below its signal line on **2026-09-29** (histogram flipped from +0.537 on 09-28 to −0.283 on 09-29) — a textbook bearish crossover that coincided with the −2.66% session that day.
- **Critically, MACD remains positive (3.27)**, so this is a *momentum reset within an uptrend*, not a trend-change signal.
- **Watch:** the histogram has improved two straight sessions (−1.069 on 10-05 → −1.043 → **−0.816**). A cross back above the 4.088 signal line — likely achievable with a couple of closes above ~336–338 — would re-trigger the bullish momentum leg.

### 3.5 `macdh` — −0.816 (negative, narrowing)
- The histogram deteriorating from +2.03 (09-03, the strongest reading in the sample) to −1.07 (10-05) quantifies how much upside thrust has been bled out of the September rally.
- The two-session narrowing is the earliest hint of stabilization. I treat this as a **"watch, don't act"** signal until the histogram crosses zero.

### 3.6 `rsi` — 57.68 (neutral, recovered from 50.88)
- Sequence: 66.88 (09-22 peak) → 50.88 (09-29 trough) → **57.68 today**. This is a clean momentum reset that never reached oversold and is now turning back up.
- At 57.7 the stock is neither overbought nor oversold; there is ample headroom to 70 before momentum becomes a headwind.
- **Notable:** RSI has *not* printed a bearish divergence at the highs — the 09-22 RSI peak (66.88) came with the 09-22 price peak (345.34). The subsequent pullback was an ordinary momentum reset, not a momentum failure signal.
- **Cross-check required:** in strong trends RSI can sit above 70 for weeks, so I am not using RSI as a sell trigger here — only as a positioning gauge (buy weakness toward 45–50, get cautious above 70).

### 3.7 `boll` / `boll_ub` / `boll_lb` — 334.48 / 341.90 / 327.05
- **Bandwidth is collapsing: (341.90 − 327.05) / 334.48 = 4.44%**, versus **6.75%** on 10-06 and **10.02%** on 09-28. This is the narrowest bandwidth in the ~40-session window I evaluated (the only comparable print was 4.99% on 2026-08-27).
- Mechanically, this squeeze is caused by the 20-day window rolling out of the high-volatility August/early-September bars: the lower band has been lifted from 313.77 (09-28) to **327.05**, while the upper band has drifted down from 346.89 to **341.90**.
- **%B = (336.67 − 327.05) / (341.90 − 327.05) = 0.65** — upper half of the band, no overextension.
- **Interpretation:** compression of this magnitude typically resolves in a directional expansion within days-to-weeks, and the *direction* is usually the direction of the prevailing trend (up). But it is a **breakout setup, not a breakout**: no trigger has occurred yet. The trade is to wait for a close outside 327.05–341.90 on expanding volume.

### 3.8 `atr` — 6.58 (falling; 1.96% of price)
- ATR has contracted from **8.94 (2026-08-10)** to **6.58**, a **−26%** decline, and from 7.25 as recently as 09-30. This independently confirms the Bollinger squeeze: realized range is shrinking while price coils.
- **Sizing math:** 1.5×ATR = **9.88**; 2×ATR = **13.17**. Any stop placed tighter than ~6.6 points is inside normal daily noise and will be clipped.
- **Caveat with teeth:** ATR understates event risk in this name. On 2026-07-31 the stock gapped and closed 7.36% lower — more than 3.5× the current ATR in a single session. Position sizing must assume a gap can exceed the ATR-based stop.

### 3.9 `vwma` — 335.56 (rising, but flat for two weeks)
- Price is **+0.33%** above the volume-weighted average price of the recent window — essentially at the volume-weighted cost basis of recent buyers.
- VWMA has gone nearly flat: 335.30 (10-01), 335.30 (10-02), 335.47, 335.50, **335.56**. Translation: **new money has been transacting at ~335.5 and is currently at breakeven.** That is a fragile equilibrium — if price loses ~333, that cohort flips to underwater and becomes latent supply.
- **Use:** 335.56 is the most defensible "fair value" line on the chart, and price closing above it on 10-07 is a modest positive (buyers paid up into the close).

---

## 4. What is *not* confirming (the honest counterweight)

1. **Volume is not validating the upside.** The 10-07 advance came on 34.1M shares versus a computed ~40M 20-session average (roughly −15%). The 09-30 recovery day did carry 50.0M — that was genuine absorption — but 10-07's push to the highest close since 09-28 is thin. A breakout above 341.90 without >45–50M shares is suspect.
2. **The 09-29 down day had above-average volume** (38.5M on a −2.66% move), i.e., the most recent high-volume *direction* was selling. That is a caution flag, not a verdict.
3. **The 50SMA slope has gone flat** — trend strength is decaying even as price holds.
4. **A marginal higher high that failed.** The 09-22 high of 345.34 exceeded July's 344.57 by only 0.22%, then reversed. Combined with the 07-30/07-31 gap, there is a real supply shelf in the **341–345.5** zone.
5. **Volume anomalies are mostly calendar artifacts, not signals.** The outsized sessions — 88.3M (03-20), 86.0M (06-18), 86.6M (09-18) — all fall on third Fridays (quarterly expiries), and 91.8M (04-30) / 132.5M (07-31) are month-ends. The extraordinary 261.8M on 06-26 is consistent with a scheduled index/rebalance event. I flag these as liquidity events rather than directional evidence (the causal labels are inference, not tool-confirmed).

---

## 5. Actionable playbook

**Base case (highest probability): continued 327–342 range trade into a squeeze resolution.** Bias is upward given the intact 50>200 structure, rising 200SMA, neutral-to-constructive RSI, and narrowing MACD histogram.

**A. Bullish continuation (primary plan)**
- **Trigger:** daily close **above 341.90** (upper band), ideally **above 342.99** (09-28 high) and with volume **>45M**.
- **Confirmation stack required:** MACD histogram positive (MACD back above 4.09) *and* RSI > 62. Two of three is acceptable; all three is a high-conviction signal.
- **Stop:** below **334.5** (20SMA/10EMA cluster) — about 7.5 points, or 1.14 ATR. ATR-consistent alternative: 1.5×ATR below entry.
- **Targets:** 345.34 (09-22 high) first; then the measured move of the August–September base (302.55 low on 08-03 → 345.34 = 42.79 points) projecting to roughly **388** — *speculative extrapolation, not a forecast*.

**B. Range accumulation (for active traders only)**
- **Zone:** 329.0–331.0 (09-29 close 329.40; repeated intraday support 330.6–331.7 across 09-30 to 10-07).
- **Stop:** below **325.81** (10-01 low), ~3.5–5 points of risk.
- **Exit:** 339.0–341.5. Roughly 1.5:1 to 2:1 reward/risk. Only valid while the 50SMA holds.

**C. Bearish breakdown (invalidation of the thesis)**
- **Trigger:** daily close **below 325.81**, confirmed by a close below **322.28** (50SMA).
- **Targets:** 316.2–317.0 (the August breakout shelf: closes of 316.83 on 08-19, 316.85 on 08-31, 316.22 on 09-08), then **308.91** (07-31 close).
- **Note:** this would also break price below VWMA (335.56) and put the entire recent buyer cohort underwater — expect supply on any bounce.
- A close back above 334 would neutralize this scenario.

**D. Risk management / sizing**
- Risk per share on the primary long (entry 342, stop 334.5) ≈ **7.5 points**.
- On a $100,000 book risking 1% ($1,000): **~133 shares** (~$45,500 notional). Given the 07-31 precedent, consider halving size or using a wider hard stop plus a defined-risk options structure if the position must be held through an earnings-type event.
- **Time stop:** if the squeeze does not resolve within ~10–15 sessions, momentum decay (flat 50SMA + flat VWMA) raises the odds of a false breakout; reduce exposure rather than adding.

---

## 6. Monitoring checklist for the next 1–2 weeks

| Watch item | Bullish confirmation | Bearish warning |
|---|---|---|
| Bollinger bandwidth (4.44%) | Expansion with close >341.90 | Expansion with close <327.05 |
| MACD histogram (−0.816) | Crosses above zero | Makes a lower low below −1.07 |
| RSI (57.68) | Pushes >62–65 | Loses 50 again (as on 09-29) |
| Volume vs ~40M avg | >45–50M on up days | >45M on down days |
| VWMA (335.56) | Price holds above, VWMA turns up | Price closes below 333 |
| 50SMA slope (+0.04/day) | Re-accelerates above +0.2/day | Turns negative |

---

## 7. Summary table

| Indicator | Latest value (2026-10-07) | Signal | Supporting evidence | Key level / trigger |
|---|---|---|---|---|
| **close_50_sma** | 322.28 | Bullish but flattening | Price +4.47% above; slope collapsed from +0.67/day (early Sep) to +0.04/day | Loses meaning below 322.28 |
| **close_200_sma** | 290.08 | Strongly bullish (strategic) | Price +16.06% above; 50SMA +32.20 (+11.1%) above 200SMA; 200SMA rising ~+0.31/day | Golden cross firmly intact; no near-term inversion risk |
| **close_10_ema** | 334.13 | Mildly bullish | Price +0.76% above; turned up from 333.55 (10-05); coincides with 20SMA at 334.48 | Hold above 334.1–334.5 keeps short-term bias up |
| **macd** | 3.272 | Neutral-to-bearish (reset) | Below 4.088 signal since 09-29; down 47.6% from 6.248 peak (09-22); still positive | Cross back above 4.09 = bullish re-trigger |
| **macdh** | −0.816 | Improving (less bearish) | Narrowed two sessions from −1.069 (10-05); was +2.03 at 09-03 peak | Zero-line cross is the actionable event |
| **rsi** | 57.68 | Neutral / constructive | Recovered from 50.88 (09-29); peak 66.88 (09-22); no bearish divergence at highs | >62 confirms; <50 re-opens downside |
| **boll / ub / lb** | 334.48 / 341.90 / 327.05 | Volatility squeeze | Bandwidth 4.44% vs 6.75% (10-06) and 10.02% (09-28); %B = 0.65 | Break >341.90 or <327.05 on volume |
| **atr** | 6.58 | Volatility contraction | −26% from 8.94 (08-10); 1.96% of price; 1.5×ATR = 9.88, 2×ATR = 13.17 | Stops tighter than ~6.6 pts sit in noise |
| **vwma** | 335.56 | Neutral / at fair value | Price +0.33% above; VWMA flat at 335.3–335.6 for five sessions | Loss of ~333 flips recent buyers underwater |

**Bottom line:** AAPL is a **long-term uptrend in a short-term coil**. The trend structure (price above a rising 50SMA above a rising 200SMA) argues for patience and an upward resolution; the flat 50SMA slope, flat VWMA, sub-average volume on up days, and the failed 345.34 retest argue that conviction is missing. The correct posture is **neutral-to-constructive, flat or lightly long into the squeeze, with a defined trigger above 341.90 and a hard invalidation below 325.81** — not a chase, and not a short.

*Scope note: this is a purely technical read from the supplied OHLCV and indicator tools. No news, earnings, guidance, or fundamental data was available to these tools, which is precisely why the 2026-07-31 gap risk deserves explicit sizing consideration.*