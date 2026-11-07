# GOOGL (Alphabet Inc.) — Multi-Timeframe Technical Report
**Analysis date: 2026-08-20 (latest completed session) | Close: $340.67**

---

## 1. Bottom Line

GOOGL is in a **medium-term corrective downtrend nested inside an intact long-term uptrend**, and it is currently **coiling in a volatility contraction right on top of a rising 200-day SMA**. Price sits below every short/intermediate average (10 EMA $346.03, 50 SMA $352.00, VWMA $356.17) but comfortably above the 200 SMA ($332.72). The tape is not broken — it is undecided, and the resolution is likely to be a directional move rather than more chop: ATR has collapsed to $9.62 (the lowest reading in the entire 60-session window I pulled), and the last eight sessions have traveled in a ~1.7% band ($340.67–$346.36 on closes).

**Net bias: neutral-to-bearish near term ($340s break risk toward $332), with a clearly defined bullish re-entry trigger above $352–$356.** This is a "wait for the level" tape, not a "chase the move" tape.

---

## 2. Data Verification

- The frozen OHLCV series and the verified snapshot **agree exactly** on the 2026-08-20 bar: O 343.06 / H 343.90 / L 338.57 / C 340.67 / V 18,570,400. No discrepancy to flag.
- Snapshot-indicator values match the `get_indicators` series on the same date (50 SMA 352.0004 vs 352.000399; RSI 44.0271 vs 44.027096; MACD −2.3304; ATR 9.6175). **Internally consistent — no reconciliation needed.**
- Corporate actions in the series are cash dividends only, no splits: $0.21 (2025-12-08), $0.21 (2026-03-09), $0.22 (2026-06-08) — a quarterly cadence implying a minor ex-div event in early September 2026. Immaterial to the technical setup, but worth knowing if holding short-dated options.

---

## 3. Price Structure — The Dated Evidence

**The macro phase (bull trend intact but decelerating):**
- 2025-11-20 close $289.45 → 2026-01-29 close $338.25: a clean five-month advance.
- Then a sharp Q1 break: intraday high $349.00 (2026-02-03) down to a close of $273.50 (2026-03-30) — a −21.6% drawdown that the 200 SMA absorbed.
- Then an explosive recovery, including a large single-session repricing on 2026-04-30 (prior close $349.94 → close $384.80, high $385.84, volume 72.0M). Peak close of the whole window: **$402.62 on 2026-05-13**; peak intraday: **$408.61 on 2026-05-18**.

**The distribution phase (May → August): a sequence of lower highs**
1. $408.61 intraday (2026-05-18)
2. $373.65 intraday (2026-07-15)
3. $384.48 intraday (2026-08-05)
…with sharp, high-volume downside air pockets inside it:
- **2026-07-16:** opened $373.06, closed $354.46 — a −4.4% reversal day off the Jul 15 high (volume 41.2M).
- **2026-07-23:** prior close $342.09 → opened $321.13 (−6.1% gap) → closed $317.69 (−7.1% on the day), low $314.90, on **69.4M shares** (~2.4× the trailing average). This is the single largest volume print in the dataset and the most damaging bar of the sequence.
- **2026-08-05:** prior close $377.65 → opened $383.34 → high $384.48 → **closed $362.43** (−4.0% on the day; open-to-close −5.7%), volume 46.9M. A textbook failed breakout / distribution bar that defines the top of the current range.

**The current micro-structure (Aug 11 → Aug 20): flat, tight, low-volume base**
Closes: 343.80, 343.54, 346.36, 345.90, 344.00, 344.20, 344.72, **340.67**. Lows: 343.39, 340.88, 343.76, 344.50, 341.93, 340.19, 340.66, **338.57**. That is a ±1% box for seven sessions, capped by the 10 EMA (346.03) and floored in the 338.5–341 zone.

**Note the deterioration on the final bar:** 2026-08-20 closed at $340.67 — the **lowest close since 2026-07-30** ($333.66), and it closed below every one of the prior seven sessions. This is a small but real downside resolution attempt out of the coil.

---

## 4. Why These Eight Indicators

I deliberately spread across four non-overlapping information families rather than stacking correlated momentum oscillators:

| Family | Chosen | Purpose / why not redundant |
|---|---|---|
| Trend (medium) | **close_50_sma** | The active ceiling. Also the fastest-declining average, so it measures how much trend damage is being done. |
| Trend (long) | **close_200_sma** | The strategic line in the sand and the only *rising* major average. Defines whether this is a correction or a regime change. |
| Trend (short) | **close_10_ema** | Captures the 2-week swing and the immediate trigger level; provides timing the SMAs cannot. |
| Momentum | **macd** | Trend/momentum crossovers — currently the cleanest read on the failed August recovery. |
| Momentum (rate of change) | **macdh** | Shows whether momentum is *accelerating or decaying*, which the MACD line alone hides. Diverges earliest. |
| Oscillator | **rsi** | Independent overbought/oversold + exhaustion gauge. (Deliberately not paired with StochRSI — redundant.) |
| Volatility | **atr** | Position sizing and stop placement; here it is also the single best "coil" detector. |
| Volume | **vwma** | The only indicator that fuses price *with* participation — critical because July/August was a volume-driven story (69.4M and 46.9M prints). |

Bollinger bands were not selected, but the snapshot supplies them (middle $347.14 / upper $375.98 / lower $318.31) and I reference them as context because the middle band coincides almost exactly with the 50 SMA and the lower band with the July low.

---

## 5. Indicator-by-Indicator Read

### 50 SMA — $352.00 (falling): the ceiling
The 50 SMA peaked at **$372.80 on 2026-07-13** and has bled to **$352.00** — about **−$0.80/session** for 26 straight sessions, with no sign of flattening (it printed 352.47, 352.84, 353.33, 353.89, 354.16, 354.47, 355.12 over the past two weeks — a smooth monotonic decline). Price is **−3.2% below** it. Until GOOGL closes above this line, every rally is, technically, a counter-trend bounce. Critically, the 50 SMA sits inside the **$352–$358** band that also contains the VWMA ($356.17), the 2026-08-11 gap zone (prior close $357.52 → $343.80 close), and the 2026-08-07 close ($354.30). That is a dense supply shelf, not a thin line.

### 200 SMA — $332.72 (rising): the floor and the regime line
Rising steadily from **$311.69 (2026-06-22) to $332.72 (+$0.51/session)**, price is **+2.4% above** it. The 50/200 spread remains positive — **$19.28, or +5.8%** — so no death cross exists. But the spread is compressing at ~$1.3/session, which, if both slopes persist, brings the averages into contact in roughly two months (extrapolation, not a forecast — flagging it as a projection, not tool output).

**This is the most important single number in the report:** $332.72. A weekly close below it would convert a tradable correction into a trend change.

### 10 EMA — $346.03 (rolling over): the immediate trigger
Trajectory: 363.81 (06-22) → 336.80 (07-30) low → **355.10 (08-10) high** → **346.03 (08-20)**. It has now turned down for six consecutive sessions (353.05, 351.32, 350.42, 349.60, 348.58, 347.78, 347.23, 346.03) while price has been flat — that is the short-term average *falling to meet* a stalled price, i.e., the bounce impulse has fully decayed. Price closed **$5.36 below** it on 08-20. First bullish repair signal = a daily close back above $346.

### MACD — −2.33 / Signal −1.55 / Histogram −0.78 (fresh bearish cross)
The August story in one line: MACD went from **−8.83 (2026-07-27)** to **+1.18 (2026-08-10)**, a violent momentum snap-back that produced the Aug 3–4 rally to $380.52. It has since rolled straight over: 0.94 (08-06) → 0.26 (08-11) → −0.48 (08-12) → −1.92 (08-19) → **−2.33 (08-20)**.

The histogram tells you *when*: it peaked at **+4.45 on 2026-08-04**, flipped negative on **2026-08-14** (−0.17), and has deteriorated every session since (−0.43, −0.56, −0.56, **−0.78**). So the bearish MACD crossover is only **five sessions old** and the histogram is still *expanding* negative — momentum is accelerating down, not stabilizing. This is the strongest argument against catching the dip here.

### RSI — 44.03 (neutral, with room to fall)
Path: 31.02 (2026-07-23, near-oversold capitulation) → 62.56 (2026-08-04, the peak) → **44.03**. Down 18.5 points in 12 sessions. Two things matter:
1. **It is not oversold.** There is no mean-reversion cushion; the RSI can travel to the high-30s without any "washed out" signal.
2. **No bullish divergence has formed.** Price made a marginally lower low on 08-20 while RSI made a marginally lower reading (46.52 → 44.03) — RSI is *confirming* the drift lower, not diverging from it.

In a strong trend RSI can stay pinned, so treat 44 as "bearish-leaning neutral," not as a buy signal.

### ATR — $9.62 (contracting sharply): the coil
Peak of the window: **$13.93 on 2026-08-05** (the reversal bar). Now **$9.62**, its lowest reading across the 60 sessions retrieved, down **31% in 11 sessions**. ATR is 2.8% of spot.

Two practical uses:
- **Volatility compression** this tight after a high-volume August impulse typically precedes a range expansion. The direction is what's unknown — this indicator gives you the *size*, not the *side*.
- **Position sizing:** 1× ATR stop from $340.67 ≈ $331.05 — which lands almost exactly on the 200 SMA ($332.72). Nice confluence: a volatility-normal stop and a structural stop occupy the same $331–333 zone. A 1.5× ATR stop is ~$14.43 (≈$326.24), 2× ATR ~$19.23 (≈$321.44). Because ATR is *low*, you can hold a larger share count per unit of risk than you could two weeks ago — but you must widen the stop in price terms, or the compressed volatility will stop you out on noise.

### VWMA — $356.17 vs price $340.67: the volume verdict
Price is **$15.50 (−4.4%) below** the volume-weighted average — meaning the average *dollar* traded over the recent window is 4.4% above spot. Anyone who bought the August rally in size is underwater. VWMA rose from $340.17 (07-30) to $356.34 (08-19) — that rise is a lagging artifact of the heavy Aug 3–5 volume — and it **ticked down for the first time on 08-20 (356.34 → 356.17)**. First downtick is not a trend, but it is the first sign the volume-weighted center of gravity is turning lower.

The gap between VWMA and the 50 SMA has essentially closed ($356.17 vs $352.00). When the volume-weighted mean and the simple mean converge, it usually means the volume-weighted crowd is now positioned at a *loss* relative to the simple trend — a supply overhang.

---

## 6. Volume & Participation (computed from the returned series)

- **21-session average volume (2026-07-23 → 2026-08-20): ≈ 29.3M shares.**
- **Last 5 sessions (08-14 → 08-20): 17.81 / 18.29 / 19.25 / 19.73 / 18.57M = ≈ 18.7M**, roughly **64% of the 21-day average**.
- The pattern is unambiguous: heavy volume on the *down* bars (07-23: 69.4M; 08-05: 46.9M), heavy volume on the *up* impulse (07-31: 46.5M; 08-03: 38.7M; 08-04: 35.7M), then **volume dry-up to the lowest levels of the period once price stalls**.

**Interpretation (nuanced):** Light volume during the current drift is *not* aggressive distribution — sellers are not panicking. That is the single best counter-argument to a bearish call. But it is equally *not* accumulation: there is no high-volume up-day absorbing supply. This is a market where neither side is committed, which is exactly what a coil looks like. The resolution bar will very likely come with volume ≥ 30M; **grade any breakout/breakdown by volume or you will be faked out** (recall 08-05 was a high-volume *failure*, so volume confirms direction only in conjunction with a close in the direction of travel).

---

## 7. The Core Tension — a genuinely two-sided tape

**Bearish evidence (near-term, dominant):**
1. Price below 10 EMA, 50 SMA, VWMA, and the Bollinger middle band ($347.14) — a full four-for-four.
2. MACD crossed below signal only 5 sessions ago; histogram at −0.78 and still expanding.
3. 50 SMA declining monotonically for 26 sessions (−$20.80 since 07-13).
4. Sequence of lower highs: $408.61 → $384.48; lower lows: $330.20 (06-26) → $314.90 (07-23).
5. RSI at 44 with no divergence and no oversold cushion.
6. 2026-08-20 was the lowest close in 14 sessions and broke below the seven-session box floor.
7. VWMA just ticked down — the volume-weighted holder base is above spot.

**Bullish evidence (medium-term, load-bearing):**
1. 200 SMA $332.72 is **rising** at ~$0.51/session and price is above it — the primary trend is intact.
2. 50/200 golden configuration still in force (+$19.28 spread); no death cross.
3. ATR compression to a 60-session low — historically the precondition for expansion, and the prior two compressions (late June/early July, late July) both resolved *upward* in this dataset (06-26 close $337.39 → 07-15 close $370.92; 07-30 close $333.66 → 08-04 close $377.65). I note these are two dated observations, not a validated statistical edge — n=2.
4. Volume is drying up on the decline, not expanding.
5. RSI at 44 is a long way from the 31.02 capitulation print of 07-23 that marked the last durable low.
6. The $338.5–341 shelf has held on five separate sessions (08-12, 08-17, 08-18, 08-19, 08-20) — buyer interest, if small.

**How I weight it:** the *direction of momentum* points down (MACD/EMA structure), the *structure* points to a range, and the *long-term trend* points up. For a swing trader that means **no high-conviction directional position right now** — but a very well-defined set of triggers on both sides.

---

## 8. Actionable Plan

### Levels (all traceable to tool output)

| Level | Value | Source |
|---|---|---|
| Supply shelf / target zone | $375.98–$384.48 | Bollinger upper ($375.98); 08-04 close $377.65; 08-05 high $384.48 |
| Aug 5 breakdown close | $362.43 | 2026-08-05 |
| **Heavy resistance band** | **$352.00–$358.58** | 50 SMA $352.00; 08-07 close $354.30; VWMA $356.17; 08-10 close $357.52; 07-31 high $358.58 |
| Bollinger middle | $347.14 | Snapshot |
| **Short-term trigger** | **$346.03** | 10 EMA |
| Spot | $340.67 | 2026-08-20 close |
| **Pivot floor** | **$338.57–$341.93** | 08-20 low $338.57 through 08-17 low $341.93; 08-12 low $340.88; 08-19 low $340.66 |
| **Regime line** | **$332.72** | 200 SMA |
| Next support | $330.20 | 2026-06-26 low |
| Bollinger lower | $318.31 | Snapshot |
| Prior capitulation low | $314.90 | 2026-07-23 |

### Scenario A — Bullish repair (reclaim)
**Trigger:** daily close **above $346.03** (10 EMA) on volume ≥ 25M, *confirmed* by a subsequent close **above $352.00** (50 SMA).
**Invalidation:** failure back below $340.
**Staged targets:** $356.17 (VWMA) → $362.43 (08-05 close) → $375.98 (Bollinger upper).
**Risk note:** the $352–$358 shelf is heavy; expect a fight. Do not treat the first poke into it as a breakout.
**MACD requirement:** the histogram must turn up from −0.78. A price reclaim without a histogram inflection is a low-quality signal.

### Scenario B — Breakdown (the higher-probability short side as of today)
**Trigger:** daily close **below $338.57** (08-20 low), ideally with volume expansion toward 30M+.
**First target:** $332.72 (200 SMA). **Second:** $330.20 (06-26 low). **Stretch:** $318.31 (Bollinger lower) / $314.90 (07-23 low).
**Stop:** above $346.03 (10 EMA) — i.e., ~1.6× ATR, $5.36 above spot, or ~0.56% risk on a $340.67 entry to the trigger level. Given ATR $9.62, a more robust stop is $350.00 (≈2× ATR including the trigger distance).
**Caveat — important:** shorting directly into a *rising* 200 SMA with ATR already compressed and volume dried up is a lower-quality trade than it looks. The reward to the 200 SMA is only 2.4%, versus a stop of 2.7%. **The risk/reward on a fresh short here is roughly 1:1 — not compelling.** A better short entry is either (a) a failed retest of $352–$356 from below, or (b) a bounce-and-roll after a break of $338.57 has already triggered.

### Scenario C — Range / do nothing (currently the modal case)
Price stays in **$338.5–$346.0**. Both A and B are invalid. Sit out; the ATR compression means the eventual move will be *fast*, so pre-place your alert levels rather than your orders.

### Preferred tactical posture
1. **Flat or minimal size now.** The tape is mid-coil with a 1:1 short R:R and a broken-but-not-recovered long structure.
2. **Trade the levels, not the middle.** Wait for $346.03+ (long) or $338.57− (short).
3. **Best asymmetry is the long side on a reclaim**, because the 200 SMA is rising beneath you and the downside targets are only ~7% away while the retracement target ($375.98+) is ~10% away with trend support.
4. **Best entry quality is a failed breakdown**: a dip under $338.57 that reverses and closes back above $341 with volume would be a high-quality long with a tight stop under the reversal low and the 200 SMA as a structural backstop.
5. **Sizing discipline:** with ATR at $9.62 (down 31% in 11 sessions), size in *risk units*, not share counts — a 1-ATR stop is ~$9.62 (2.8%), a 2-ATR stop ~$19.23 (5.6%). If you use a 2-ATR stop, your share count should be roughly half of what it was on 2026-08-05 when ATR was $13.93 for the same dollar risk. Note that a 1× ATR stop ($331.05) sits just *below* the 200 SMA ($332.72) — that's the cleanest structural placement.

### What would invalidate my neutral-bearish bias
- A daily close above **$352.00** with MACD histogram turning positive → flip constructive, target $362/$376.
- Conversely, a weekly close above $358.58 without volume would be a *trap* signal, not a trend signal.
- A weekly close below **$332.72** → flip outright bearish; the 50/200 spread (+$19.28) would be at risk of inversion.

### What would invalidate my bearish near-term lean
- Two consecutive closes above **$346.03**.
- MACD histogram recovering above zero (currently −0.78).
- An up-day on volume > 35M (accumulation signature absent since 2026-08-04).

---

## 9. Risks & Caveats

- **Indicator scale ambiguity:** the snapshot reports `mfi 0.429`. I did not select MFI and am not building conclusions on it — its 0–1 vs 0–100 scaling is unclear from the output, so I am deliberately excluding it rather than misreading it.
- **Projection risk:** the "50/200 convergence in ~2 months" figure is my linear extrapolation of two slopes, not tool output. Treat it as directional color only.
- **Sample-size risk:** the "prior compressions resolved upward" observation rests on two instances in this dataset. That is anecdote, not evidence.
- **Event risk not in the data:** the series shows a quarterly dividend rhythm ($0.21 on 2025-12-08 and 2026-03-09, $0.22 on 2026-06-08), implying an early-September 2026 distribution. The dataset contains no earnings, guidance, or news — and given the 2026-04-30 gap (+9.9% in one session, 72M volume) and the 2026-07-23 gap (−7.1%), this name clearly reprices violently around catalysts. **Any position held through a scheduled event must be sized down regardless of what the technicals say.**
- **No claim of validated support/resistance:** the levels above are *observed* highs and lows on named dates, plus moving-average arithmetic. I am not asserting that any level "held historically" in a statistically validated sense.

---

## 10. Summary Table

| Dimension | Reading (2026-08-20) | Trend / Stance | Key Level |
|---|---|---|---|
| Close | $340.67 | Lowest close in 14 sessions (since 07-30) | — |
| 10 EMA | $346.03, falling 6 straight sessions | **Bearish** — price $5.36 below | Trigger: $346.03 |
| 50 SMA | $352.00, −$20.80 since 07-13 | **Bearish** — price −3.2% below | Resistance: $352.00 |
| 200 SMA | $332.72, +$0.51/session | **Bullish** — price +2.4% above | Regime line: $332.72 |
| 50/200 spread | +$19.28 (+5.8%), compressing ~$1.3/session | Golden but narrowing | — |
| MACD | −2.33 vs signal −1.55 | **Bearish** — crossed down ~08-14 | — |
| MACD Histogram | −0.78; peak +4.45 (08-04), negative since 08-14 | **Bearish, expanding** | Zero line |
| RSI | 44.03 (from 62.56 on 08-04) | **Neutral-bearish**, no divergence, no oversold | 30 / 50 |
| Bollinger (mid/UB/LB) | $347.14 / $375.98 / $318.31 | Price in lower half | MB $347.14 |
| ATR | $9.62 (−31% from $13.93 on 08-05) | **Coil** — lowest in 60 sessions | Stop: 1×ATR ≈ $331 |
| VWMA | $356.17, price −4.4% below; first downtick on 08-20 | **Bearish** — holder base underwater | $356.17 |
| Volume | 5-day avg ≈18.7M vs 21-day ≈29.3M (64%) | **No conviction either way** | 30M+ = signal |
| Structure | Lower highs $408.61→$384.48; lower lows $330.20→$314.90 | Corrective range | $338.57 / $352–358 |
| **Overall bias** | **Neutral-to-bearish near term, bullish long-term** | **Wait for resolution** | **$338.57 / $346.03 / $352.00 / $332.72** |

**One-line action:** GOOGL is coiling beneath a falling 50 SMA and above a rising 200 SMA with collapsing volatility and evaporating volume — do nothing in the $338–$346 middle, sell/scalp short a break of $338.57 toward the 200 SMA at $332.72 (acknowledging ~1:1 R:R), and turn genuinely constructive only on a volume-backed reclaim of $346.03 that targets the $352–$358 supply shelf.