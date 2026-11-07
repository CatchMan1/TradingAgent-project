# AAPL Technical Analysis Report — As of 2024-02-15

## Data provenance & consistency check
All figures below are anchored to the **verified market snapshot (2024-02-15)**. The values returned by the individual indicator calls are **fully consistent** with the snapshot (e.g., RSI 39.49, 50-SMA 190.08, 200-SMA 183.41, MACD −1.08, ATR 3.18, VWMA 186.68). No discrepancy to flag.

**Latest session (2024-02-15):** Open 183.55 · High 184.49 · Low 181.35 · **Close 183.86** · Volume 65.43M · split 1.0 · dividend 0.0.

---

## 1. Market context — a short-term downtrend testing a long-term floor
AAPL has transitioned from a strong Q4-2023/January rally into a **rolling short-to-medium-term pullback** that is now pressing against a critical long-term trend line. The structure is best described as: *short-term bearish, medium-term rolling over, long-term still constructive but under active test.*

From the closing peak of **195.18 on 2024-01-23**, the stock has declined to **183.86 (−5.80%)** in roughly three weeks. The decline has been orderly until the last week, when momentum accelerated (describe below).

---

## 2. Indicator selection rationale (8 indicators, non-redundant)
I selected a complementary suite spanning trend, momentum, volatility, and volume:

| Category | Indicator | Why chosen for this setup |
|---|---|---|
| Trend (long) | **close_200_sma** | Price is literally sitting on this line — the single most important strategic level right now. |
| Trend (medium) | **close_50_sma** | Captures the roll-over of the intermediate trend and defines the resistance ceiling. |
| Trend (short) | **close_10_ema** | Fast read on whether near-term selling pressure is easing or intensifying. |
| Momentum | **macd** | Confirms trend/momentum deterioration and crossover dynamics. |
| Momentum | **rsi** | Gauges whether the pullback is becoming over-extended (potential snap-back) or has room to fall. |
| Volatility | **boll_lb** | Frames whether price is stretched to the downside (band support zone). |
| Volatility | **atr** | Live volatility input for stop placement and position sizing. |
| Volume | **vwma** | Validates whether the move is volume-backed (distribution) vs. drift. |

*(I used `boll_lb` for the band edge and read the middle/upper band from the snapshot; MACD signal/histogram were cross-checked via the snapshot rather than duplicated as separate calls to avoid redundancy.)*

---

## 3. Trend analysis

### Long-term (200-SMA = 183.41) — the line in the sand
- The 200-SMA is **rising steadily** (177.79 on 2023-12-18 → 183.41 on 2024-02-15), confirming the broader uptrend is technically intact.
- But price has fallen **right onto it**: close 183.86 is only **+0.25% above** the 200-SMA. This is a classic make-or-break retest.
- The **2024-02-15 low of 181.35 briefly pierced** both the 200-SMA and the Bollinger lower band before closing back above — a marginal intraday undercut that recovered, but a warning sign of weakening support absorption.

### Medium-term (50-SMA = 190.08) — trend rolled over
- The 50-SMA **peaked at ~190.93 on 2024-01-30 and has since turned down** (to 190.08), confirming the intermediate trend has topped.
- Price is **−3.27% below** the 50-SMA, which now acts as overhead resistance.
- The 50-SMA (190.08) remains **above** the 200-SMA (183.41), so the golden-cross structure isn't dead — but the gap is **narrowing fast** (from ~8 points in early January to ~6.7 now). Continued weakness raises **death-cross risk**.

### Short-term (10-EMA = 186.53) — persistent downside momentum
- The 10-EMA has **fallen from 191.41 (2024-01-29) to 186.53**, a steep, unbroken decline.
- Price (183.86) is **−1.43% below** the 10-EMA, and the EMA is above both price and the VWMA — the classic **bearish short-term stack** (price < 10-EMA < 50-SMA).
- The only constructive nuance: the **last three closes** (185.04 → 184.15 → 183.86) show **decelerating downside momentum**, and the 2024-02-15 candle closed above its low. Selling is losing a bit of bite, but not yet reversing.

---

## 4. Momentum analysis

### MACD (−1.08) — bearish and re-accelerating
- MACD crossed **below zero on 2024-02-01** (from +0.09 on 2024-01-31 to −0.14) and has slid to **−1.08**.
- It is **below its signal line** (−0.55) with a **negative histogram (−0.54) that is expanding** — the line went from −0.25 (2024-02-09) to −1.08 (2024-02-15). This is momentum *accelerating to the downside*, the strongest bearish confirmation in the indicator set.
- This is the most important caution: the MACD is not yet showing the "histogram curling up" precondition for a bottom.

### RSI (39.49) — weak, but NOT oversold
- RSI dropped from **50.81 (2024-02-07) to 39.49**, i.e., momentum has swung decisively to the bearish side.
- Critically, it is **above the 30 oversold threshold** — there is **room to fall further** before a technical snap-back becomes likely. RSI briefly hit 28.79 on 2024-01-05 (the last true oversold reading) and rallied from there; we are **not there yet**.
- The RSI trajectory (lower highs: 62.6 → 50.8 → 39.5) mirrors the price structure and argues against premature bottom-fishing.

---

## 5. Volatility analysis

### Bollinger bands (Middle 189.12 · Upper 196.41 · Lower 181.83)
- Price (183.86) sits in the **lower quarter of the band**, roughly **%B ≈ 0.14** ((183.86−181.83)/(196.41−181.83)).
- The **lower band at 181.83** is the immediate downside magnet/support; the 2024-02-15 low (181.35) tagged just beneath it. A close below ~181.8 would signal downside band-walking.
- The middle band (189.12) aligns closely with the 50-SMA (190.08), reinforcing the **~189–190 resistance shelf**.

### ATR (3.18) — moderate, use for risk sizing
- ATR is **~3.18**, i.e., roughly **1.7% of price** — elevated vs. December (~2.6–2.8) but off the early-Feb spike (3.59 on 2024-02-02). Volatility is moderating slightly.
- Practical use: a **1.5×ATR stop ≈ $4.77**, a **2×ATR stop ≈ $6.36**. When key level 200-SMA (183.41) is this close, ATR-based stops prevent getting shaken out by normal noise.

---

## 6. Volume analysis (VWMA = 186.68)
- The **VWMA (186.68) sits above price (183.86, −1.51%)**, meaning the volume-weighted "fair value" of recent trading is higher than current price — a sign that **selling has occurred on meaningful volume above current levels** (distribution).
- VWMA has **rolled over from 189.72 (2024-02-07) to 186.68**, confirming the volume flow has turned.
- **2024-02-02 stands out**: volume spiked to **102.55M** (vs. ~40–65M typical) on a wide-range, high-close reversal day (open 179.86, low 179.25, close 185.85). That was a strong demand footprint — and it defines the ~179–180 zone as a volume-backed support shelf.
- Recent volumes (2024-02-13: 56.53M, 02-14: 54.63M, **02-15: 65.43M**) show **rising volume on the latest down session** — mild distribution, not capitulation.

---

## 7. Key levels map

**Support (downside):**
1. **183.41** — 200-SMA (being tested now)
2. **181.83** — Bollinger lower band (intraday low 181.35 on 02-15)
3. **~179.25–180.30** — multi-touch floor (2024-01-05 low 180.17, 2024-01-17 low 180.30, 2024-02-02 low 179.25) — the **major demand shelf**, reinforced by the 02-02 volume spike.

**Resistance (upside):**
1. **186.53** — 10-EMA
2. **186.68** — VWMA (confluence at ~186.5–186.7)
3. **189.12–190.08** — Bollinger middle + 50-SMA (+50-SMA as firm ceiling)
4. **194.5–196.4** — late-January closing highs / Bollinger upper band

---

## 8. Actionable insights & scenarios

**Net read: tactically bearish / cautious. Trend is down short-term, momentum is accelerating lower, and price is sitting on the most important long-term support. This is a "wait for confirmation at a level" market, not a "chase" market.**

- **Bearish confirmation trigger:** A **daily close below ~181.8 (Bollinger lower) and especially below ~179.25** would break the volume-backed floor, open the door to a deeper correction, strengthen the case for a **50/200 death cross**, and warrant reducing exposure / adding downside protection.
- **Bullish stabilization trigger:** A **close back above the 186.5–186.7 confluence (10-EMA + VWMA)** with *expanding volume* and a **MACD histogram curling up toward zero** would be the first credible sign the pullback is ending. Reclaiming 190 (50-SMA) would neutralize the medium-term bearish case.
- **Range/neutral:** Holding **183.4–181.8** while RSI stays 35–40 and ATR cools would suggest basing — but with MACD still expanding lower, that's a *hope*, not yet a *signal*.
- **Risk management:** Place stops using **1.5–2×ATR ($4.8–$6.4)**. Longs held into 200-SMA support should size to survive a flush toward 179–180. Because RSI is *not* oversold and MACD is still falling, avoid catching the knife ahead of a confirmed reversal.
- **Position sizing:** Volatility (ATR ~1.7% of price) is moderate — normal position sizing applies, but tight stops near the 200-SMA risk noise stop-outs given the 02-15 intraday undercut.

---

## 9. Summary table

| Dimension | Indicator | Value (2024-02-15) | Signal / Interpretation |
|---|---|---|---|
| **Close** | — | **183.86** | −5.80% from 2024-01-23 close (195.18) |
| Long-term trend | close_200_sma | 183.41 | Rising; price **+0.25% above** — critical retest |
| Medium-term trend | close_50_sma | 190.08 | Turned down from ~190.93 (01-30); price **−3.27% below**; ceiling |
| Short-term trend | close_10_ema | 186.53 | Steep decline; price **−1.43% below**; bearish stack |
| Momentum | macd | −1.08 | Below zero & below signal; **histogram expanding negative** → accelerating downside |
| Momentum | rsi | 39.49 | Weak, **not oversold** (>30); room to fall; lower-high pattern |
| Volatility | boll_lb / mid / ub | 181.83 / 189.12 / 196.41 | Price in lower band (%B≈0.14); lower band = near support |
| Volatility | atr | 3.18 | ~1.7% of price; 1.5–2×ATR stop = $4.8–$6.4 |
| Volume | vwma | 186.68 | Above price (−1.51%); volume-weighted distribution; 02-02 102.5M = demand shelf ~179–180 |
| **Support** | — | 183.41 / 181.83 / 179.25–180.30 | 200-SMA → Boll lower → multi-touch floor |
| **Resistance** | — | 186.5–186.7 / 189–190 / 194.5–196.4 | 10-EMA+VWMA → 50-SMA+Boll mid → Jan highs |
| **Bias** | — | **Cautious/Bearish near-term** | Down short-term, long-term support under active test; wait for a confirmed close at either trigger |

*Disclaimer: This is a point-in-time technical assessment based solely on the frozen data provided through 2024-02-15; it is not investment advice. Levels are based on the stated indicators and can shift as new data arrives.*