# AMZN — Technical Analysis Report (as of close 2024-01-26)

## 1. Bottom line

AMZN is in a **confirmed, multi-timeframe uptrend** with a fresh breakout to new period highs, improving momentum, and *falling* volatility — a constructive combination. The price closed at **159.12**, the highest close in the entire 2023-07-01 → 2024-01-26 dataset, after printing an intraday high of **160.72**. Price sits above all four key averages I track (10-EMA, VWMA, 50-SMA, 200-SMA) with a **positive, expanding MACD histogram** for a sixth consecutive session.

The two legitimate cautions are (a) **short-term extension** — the close is ~4.2% above the 20-day Bollinger mid-line and ~6.2% above the 50-SMA, with RSI at 67.0 knocking on the overbought door — and (b) **oscillator-level divergence versus the November/December peaks**, where MACD and RSI made *lower* highs while price made *higher* highs. Net: trend-following bias stays long, but the asymmetry favors buying pullbacks or breakout retests over chasing the print at 159.

---

## 2. Verified snapshot (source of truth)

From `get_verified_market_snapshot` for 2024-01-26:

| Field | Value |
|---|---|
| Open / High / Low / Close | 158.42 / 160.72 / 157.91 / **159.12** |
| Volume | 51.05 M |
| 10-EMA | 155.670 |
| 50-SMA | 149.892 |
| 200-SMA | 132.460 |
| MACD / Signal / Hist | 2.3706 / 1.9297 / **+0.4409** |
| RSI(14) | 67.047 |
| Bollinger mid / upper / lower | 152.789 / 160.495 / 145.083 |
| ATR(14) | 2.9869 |
| VWMA | 154.288 |

Every indicator value returned by the `get_indicators` calls matches the snapshot exactly (e.g., 50-SMA 149.8919998 vs 149.892; MACD 2.3705590337 vs 2.370559). **No data conflicts.** One footnote: the snapshot's `mfi` field reads **0.739205**, which is inconsistent with the standard 0–100 MFI scale and appears to be a 0–1 normalized value (≈74, i.e., money-flow also in overbought territory). I am *not* using MFI in the signal set for that reason — flagging rather than reconciling.

---

## 3. Indicators selected (8) and why

| Indicator | Role in this specific context |
|---|---|
| **close_10_ema** | Trend-following trail for a fast-moving, breakout regime. Price has held above it since Jan 18; it defines the "do not touch" line for momentum longs. |
| **close_50_sma** | Medium-term regime + dynamic support. Rising every session since early January — quantifies trend strength rather than just direction. |
| **close_200_sma** | Strategic trend anchor; confirms this is a primary uptrend, not a counter-trend rally. Also measures how stretched the trend is (+20.1%). |
| **macd** | Captures the intermediate momentum regime and the Dec→Jan momentum reset. |
| **macdh** | The *signal* line itself is redundant once MACD and the histogram are known (signal = MACD − hist), so I use the histogram to time the re-acceleration and to spot divergence. |
| **rsi** | Overbought/oversold and divergence detection in a trending tape — the main counterweight to the bullish trend read. |
| **boll / boll_ub / boll_lb** | Treats the 20-SMA basis + envelopes as one volatility/extension module: bandwidth measures whether the breakout has volatility behind it, and %B measures how extended price is within the envelope. |
| **atr** | Non-negotiable for stop placement and sizing given ATR has compressed from 3.45 → 2.99 while price broke out. |
| **vwma** | Volume-confirmation filter — the key question at new highs is whether *volume-weighted* cost basis is confirming, and VWMA has turned up sharply over the last three sessions. |

Deliberately excluded: a stochastic-type oscillator (redundant with RSI), and the MACD signal line as a standalone (derivable). That keeps 8 non-overlapping inputs spanning trend, momentum, volatility, and volume.

---

## 4. Trend structure

**Primary trend (200-SMA): bullish.** 200-SMA at 132.460 and rising monotonically: 127.983 (Jan 2) → 132.460 (Jan 26), a +3.5% advance in 17 sessions. Every close in the visible window from late November onward is above it.

**Intermediate trend (50-SMA): bullish and accelerating.** 50-SMA: 143.476 (Jan 2) → 149.892 (Jan 26) = **+4.47% in 17 sessions**, rising without a single down-tick in the series. The 50/200 spread is **+17.43 points (+13.2%)**, and the 50-SMA has been above the 200-SMA for the entire visible window (Nov 27, 2023 – Jan 26, 2024) — i.e., a persistent golden-cross regime. *Caveat:* my dataset begins 2023-07-01, so I cannot pin the exact crossover date; I make no claim about when the cross occurred.

**Short-term trend: bullish, freshly re-accelerated.** 10-EMA at 155.670, rising for eight straight sessions (151.797 on Jan 12 → 155.670). The sequence that matters: close dipped *below* the 10-EMA on Jan 17 (151.71 vs 151.98), reclaimed it on Jan 18 (153.50 vs 152.26), and has not looked back — five consecutive closes above it, including five consecutive higher closes Jan 22–26 aside from the Jan 22 dip day.

**Stacking (most bullish possible ordering):**
Close 159.12 > 10-EMA 155.67 > VWMA 154.29 > 50-SMA 149.89 > 200-SMA 132.46.

The stacking is textbook. The *gap* between price and the 50-SMA, however, is **6.16%**, which is the widest of the visible window — that is a mean-reversion magnet, not a trend signal.

**Longer-horizon context:** from the Oct 26, 2023 closing low of **119.57**, AMZN is **+33.1%**; from the Oct 27 reversal close of 127.74, **+24.6%**. Year-to-date (from the Dec 29 close of 151.94), **+4.73%**. From the Jan 4 close of 144.57, **+10.06% in 15 sessions**. (All figures computed directly from the tool's OHLC rows.)

---

## 5. Momentum: improving, but not at prior extremes

**MACD (2.3706) vs signal (1.9297), histogram +0.4409.** The important story is the *round trip*:

- MACD peaked at **3.886** on Nov 27 and decayed to **0.779** on Jan 8 — a full momentum reset to ~20% of its peak while price fell only from 147.73 to 149.10.
- From the Jan 8 trough, MACD has advanced every session: 0.779 → 0.888 → 1.153 → 1.462 → 1.643 → 1.650 → 1.520 → 1.545 → 1.693 → 1.745 → 1.865 → 2.005 → 2.163 → **2.371**.
- The histogram crossed back positive on Jan 12 (+0.0937), wobbled marginally negative on Jan 17–18 (−0.0392, −0.0120), then expanded for six straight sessions to **+0.4409** — the strongest reading since Dec 19. Expanding histogram = the *rate* of momentum gain is still increasing, which is what you want to see at highs.

**The divergence caveat:** MACD at 2.371 with price at 159.12 is a **lower momentum high against a higher price high** (price 147.73 → 159.12, MACD 3.886 → 2.371). Similarly RSI: 68.05 on Dec 18 at a 154.07 close versus **67.05 today at 159.12**. This is a *mild, marginal* negative divergence — it argues the advance is becoming less steep per unit of price, not that it is reversing. It is a reason to tighten risk, not to go short. This is exactly why the histogram (currently expanding) should outweigh raw divergence until the histogram itself rolls over.

**RSI 67.05.** Not overbought (threshold 70) but approaching. Path: 40.23 (Jan 4 — the only sub-45 print in the window) → 53.72 (Jan 17 dip) → 67.05 now. In strong trends RSI can and does run 70–80; a flat-or-rising RSI at 67 with price at highs is trend-healthy. A push above 70 that *fails* to hold is the more meaningful warning than 70 itself.

---

## 6. Volatility and extension: the striking part of the setup

**Bollinger:** mid 152.789, upper **160.495**, lower 145.083.
- **%B = (159.12 − 145.083) / (160.495 − 145.083) = 0.911.** Price is riding the upper band — 91% of the way up the envelope. In a breakout this is normal "band-walking," but it also means the easy money from the mid-band is gone.
- **Bandwidth = 15.412 / 152.789 = 10.09%**, up from **8.95%** on Jan 2 (13.42/149.97). So the bands are *expanding* as price breaks out — volatility is confirming direction rather than contracting against it. This is the bullish configuration (squeeze → expansion with price at the top).
- Today's high of 160.72 actually pierced the upper band (160.495) intraday and closed just back inside — a near-miss band tag rather than a decisive breakout above it.

**ATR = 2.9869, or 1.88% of price.** ATR has *fallen* from 3.446 (Dec 18) and 3.050 (Jan 12) even as price has risen to new highs. Falling ATR + rising price = orderly, low-churn advance with shallow pullbacks; it is a hallmark of accumulation rather than distribution. It also means stop distances can be tighter than November-December norms without being noise-prone.

**Extension metrics to respect:** close is **+4.15%** above the 20-day Bollinger basis (152.789) and **+3.13%** above VWMA (154.288). Both are the most stretched readings in the visible window. Statistically, this is where multi-day consolidation shallow pullbacks originate — into the 155–156 zone (10-EMA / VWMA) — not where durable failure originates, given the trend backdrop.

---

## 7. Volume confirmation

- Today's volume **51.05 M** vs a **~44.0 M 20-session average** (my calculation from the tool's rows) = **1.16×**. Moderate confirmation — real participation, but far from a blow-off or climactic volume signature. Healthy breakout characteristics.
- Up-day volume is doing the confirming work: **Jan 19 51.65 M** (+1.2% close), **Jan 26 51.05 M** (+0.87% close, new high), and **Jan 24 48.55 M** (+0.55%, the first 158.51 print). Down days have been comparatively light (Jan 17 34.95 M, Jan 23 37.99 M) *except* **Jan 4: 56.04 M on a −2.4% close (148.47 → 144.57)** — the single largest volume of January on a down day. That looked like distribution at the time, but it marked the swing low that launched the current +10% leg, which is why I read it as capitulation/re-accumulation, not topping volume.
- **VWMA has turned sharply higher:** 150.90 (Jan 17) → 151.08 → 151.29 → 151.62 → 152.25 → 153.22 → **154.288**. The volume-weighted cost basis is now racing upward toward price, meaning recent buyers are both plentiful and in profit. That is the single best volume-based confirmation of the breakout.
- Ignore Dec 15's 110.09 M print as a flow artifact (index/liquidity event), not a trend signal.

---

## 8. Levels and risk management

**Immediate resistance**
- **160.72** — today's high, and the highest print in the dataset. This is also essentially the Bollinger upper band (160.495); expect a fight here.
- **164.2 (measured move)** — the Jan 17–22 micro-base ran from 149.91 to 157.05 (~7.14 points of height). A breakout above its high (157.17 on Jan 11) projects to roughly 164.3. Treat as a target zone, not a precise level.

**Support (in order of importance)**
1. **157.75 / 154.55** — Jan 25's close and low; the most recent higher-low structure. Losing 154.55 breaks the current short-term sequence.
2. **155.67** — 10-EMA. First line of defense for the momentum long.
3. **154.29** — VWMA. Volume-weighted cost basis; a close below here would say recent buyers are underwater and materially weaken the breakout case.
4. **153.90 / 153.93** — the Jan 22 and Jan 23 lows. Clean shelf.
5. **149.89–149.91** — 50-SMA *and* the Jan 17 low coincide here. This is the trend-defining support. A close below it invalidates the intermediate uptrend.
6. **144.05** — Jan 4 low; the structural swing low of the January reset.

**Stops and sizing (ATR-based, using 2.9869)**
- 1.5 × ATR below close = **154.64** → sits almost exactly on the 10-EMA (155.67) / VWMA (154.29) cluster. Aggressive but trend-consistent.
- 2.0 × ATR below close = **153.15** → just under the Jan 22/23 lows (153.90/153.93). This is the highest-conviction stop: it requires price to break a *visible* support shelf, not just noise.
- With ATR at 1.88% of price, a 2-ATR stop (3.75% risk) supports roughly **26% of equity notional per 1% of account risk** — i.e., position sizing can be meaningfully larger than during the December 3.45-ATR regime, which is a genuine, quantifiable benefit of the volatility compression.

**Risk/reward note:** Buying at 159.12 with a 153.15 stop (5.97 risk) against a 164.3 first target (5.18 reward) is **<1:1** — poor. Waiting for a retest of the 155.5–156.0 area improves the ratio to roughly **1:1.8** (risk ~2.9 to the 153.15 stop, reward ~8.3 to 164.3). That math is the core argument against chasing today's print.

---

## 9. Actionable scenario map

**Base case (~55%) — shallow consolidation then continuation.** Price digests the 159–161 area, dips into 155.5–157.0 (10-EMA/VWMA, without breaking 154.55), RSI cools from 67 to ~55–58, MACD histogram stays positive but flattens, then attempts 160.72 → 164. *Action:* add/re-add on the pullback into the 155.7–156.5 band; keep the 153.15 stop.

**Bull extension (~25%) — band-walk.** A decisive close above the Bollinger upper band (currently 160.495) with volume >50 M would turn this into a band-walking trend; watch for RSI to move into 70–75 and *hold*. *Action:* trail with the 10-EMA; do not fade RSI >70 in a confirmed trend.

**Bear/range break (~20%).** Fail at 160.5–160.7, then lose 154.55 *and* the VWMA. First real damage signal is a close under 153.90. *Action:* stand aside; a close below the 50-SMA (149.89) is the actual trend-invalidation trigger and would reframe the picture as a failed breakout back into the December range.

---

## 10. Caveats and data discrepancies

- **Event risk:** AMZN's Q4 results historically land in early February, i.e., immediately after this snapshot date. That is a binary gap risk that no technical indicator prices. Any stop placed through an earnings print is a *directional bet on the print*, not a technical stop. *Note: this is general knowledge about the company's reporting cadence, not derived from the tool output.*
- **MFI scale discrepancy** flagged in §2 (0.739205 reported instead of ~74); excluded from the signal set.
- **Divergence is marginal, not decisive:** RSI 67.05 vs 68.05 on Dec 18 is a ~1-point difference and could reverse within one session. I describe it as a *watch item* — I am not claiming a validated reversal signal, and no divergence has been confirmed by a price break.
- **No historical validation claimed:** I have not backtested these thresholds, and I make no claim that any level "held" or "rejected" in the past beyond the specific OHLC dates cited above.
- **Snapshot is point-in-time and frozen** — all values are as of the 2024-01-26 session close.
- **Golden-cross timing unknown:** the visible window starts with the 50-SMA already above the 200-SMA, so no crossover date is asserted.

---

## 11. Key points summary

| Dimension | Reading (2024-01-26) | Interpretation | Signal |
|---|---|---|---|
| Close | 159.12 (H 160.72 / L 157.91) | New period closing high; intraday pierced Bollinger upper band 160.495 | **Bullish** |
| Short-term (10-EMA) | 155.670, price +2.2% above | Above for 5 straight sessions; fast trend intact | **Bullish** |
| Medium-term (50-SMA) | 149.892, rising 17 sessions (+4.47% since Jan 2) | Trend accelerating, not flattening | **Bullish** |
| Long-term (200-SMA) | 132.460, rising (+3.5% since Jan 2) | Primary uptrend confirmed | **Bullish** |
| MA stack | 159.12 > 155.67 > 154.29 > 149.89 > 132.46 | Perfect bullish ordering | **Bullish** |
| 50/200 spread | +17.43 pts (+13.2%) | Persistent golden-cross regime | **Bullish** |
| MACD / Signal / Hist | 2.3706 / 1.9297 / **+0.4409** | Histogram positive & expanding 6 sessions; best since Dec 19 | **Bullish** |
| MACD vs Nov peak | 2.371 now vs 3.886 (Nov 27) at lower price | Lower momentum high vs higher price high | **Caution (divergence)** |
| RSI(14) | 67.05 (from 40.23 on Jan 4) | Near but below 70; marginally below Dec 18's 68.05 | **Bullish with extension risk** |
| Bollinger %B / width | 0.911 / 10.09% (was 8.95% Jan 2) | Band-walking with *expanding* bandwidth | **Bullish** |
| Extension vs 20-day basis | +4.15% above 152.789 | Most stretched in window; pullback magnet | **Caution** |
| ATR(14) | 2.9869 = 1.88% of price (down from 3.45 Dec 18) | Volatility compression during breakout = orderly advance | **Bullish / tighter stops viable** |
| VWMA | 154.288, up 6 straight sessions from 150.90 (Jan 17) | Volume-weighted cost basis confirming breakout | **Bullish** |
| Volume | 51.05 M vs ~44.0 M 20-day avg = 1.16× | Moderate confirmation, not climactic | **Bullish** |
| Nearest resistance | 160.72 (high) / 160.50 (upper band); ~164.3 measured move | First real hurdle is immediate | **Watch** |
| Key support cluster | 157.75 → 155.67 (10-EMA) → 154.29 (VWMA) → 153.90 → 149.89 (50-SMA) | 153.15 (2×ATR) is the highest-conviction stop | **Risk anchor** |
| Trend invalidation | Close below 149.89 (50-SMA) | Reframes as failed breakout | **Bear trigger** |
| R/R at 159.12 | ~0.9:1 to first target | Poor entry; better on retest 155.5–156.5 | **Don't chase** |
| Event risk | Early-February Q4 report (not from tool data) | Binary gap risk overrides technical stops | **Flag** |

**Stance:** constructive/neutral-to-long AMZN. The trend, momentum direction, volatility behavior, and volume-weighted cost basis all point the same way — but at 159.12 the entry is extended (6.2% above the 50-SMA, 91% of the Bollinger envelope, RSI 67). Preferred execution: buy the pullback into 155.5–156.5, stop 153.15, target 160.7 then ~164.3; abandon the bullish case on a close below the 50-SMA at 149.89.