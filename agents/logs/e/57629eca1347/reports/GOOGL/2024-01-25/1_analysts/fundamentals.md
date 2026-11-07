# GOOGL (Alphabet Inc.) — Fundamental Research Report
**As of:** 2024-01-25 | **Latest SEC filing in dataset:** Q3 2023 Form 10-Q, filed 2023-10-25 (accepted 2023-10-24 22:39 UTC)

---

## 0. Bottom Line Up Front

**No new GOOGL filings exist in the authorized point-in-time dataset during the trailing week.** The freshest hard data remains the September 30, 2023 balance sheet and the nine-month 2023 period. The fundamentals through Q3 2023 describe a business in a clear **margin-recovery + capital-return** phase:

- **Revenue re-accelerated:** Q3'23 revenue **$76.69B, +11.0% YoY** (vs. +4.9% in 1H'23). 9M'23 revenue **$221.08B, +6.9%**.
- **Operating leverage is real:** Q3'23 operating income **$21.34B (+24.6% YoY)**, operating margin **27.8% vs. 24.8%** a year ago. Gross margin expanded **+180bp to 56.7%**.
- **Cash generation inflected:** 9M'23 operating cash flow **$82.83B (+22.0%)** and free cash flow **$61.60B (+40.0%)** on *lower* capex ($21.23B, −11.1%).
- **Two earnings-quality caveats that a trader must size:** (1) Q3'23 diluted EPS of **$1.55** was inflated by an abnormally low **7.1% effective tax rate** — normalizing to the 9M run-rate implies EPS closer to **~$1.43**; (2) roughly **$10.4B** of the 9M OCF improvement is a non-recurring tax-timing benefit (higher income taxes payable), meaning underlying OCF growth was closer to **+5%**, not +22%.
- **Balance sheet is fortress-grade:** **$119.94B** cash + marketable securities against roughly **$15.3B** of debt principal (FY22 10-K maturity schedule) — a **~$105B net cash** position, ~$9.56 cash+securities per share.
- **Immediate catalyst:** Q4/FY2023 results are due in early February 2024, i.e., **within days of the as-of date**. FY2023 10-K was *not* yet filed, so full-year FY23 figures are not yet point-in-time available.

**Net read:** fundamentals are improving on every operating line, but the headline growth rates in EPS and OCF overstate the underlying run-rate, and the stock enters its Q4 print with elevated expectations. Position sizing, not direction, is the differentiated call here.

---

## 1. Data Provenance, Cut-off, and Known Gaps (read this before using the numbers)

This report is built from a **point-in-time SEC XBRL fact cache filtered by EDGAR acceptance timestamp ≤ 2024-01-25**. That creates specific, material boundaries:

| Item | Status |
|---|---|
| Latest 10-Q (Q3 FY23, period end 2023-09-30) | ✅ Available, filed 2023-10-25 |
| FY2023 Form 10-K (period end 2023-12-31) | ❌ **Not yet filed** as of 2024-01-25 → no FY23 full-year or Q4'23 data |
| Income statement detail | ⚠️ **Partial** — revenue tag was not returned; revenue **derived** (see §2.1) and cross-validated |
| Balance sheet | ⚠️ **Truncated** — no PP&E, goodwill, total current liabilities, or long-term debt line returned |
| Cash flow | ✅ 9M'23 vs 9M'22, plus FY20–FY22 aggregates |
| Segment revenue (Services / Cloud / Other Bets) | ❌ Not in dataset — no segment P&L available |
| **Insider transactions** | ❌ **DATA_UNAVAILABLE.** The vendor has no authorized insider-transaction archive for GOOGL at this date. **No insider buying/selling is inferred or fabricated anywhere in this report.** |
| Price / market cap / valuation multiples | ❌ Not provided — **no P/E, EV/EBITDA, or price target can be computed here** |

Numbers below are in **USD millions** unless stated. "Derived" = computed from tool-returned line items; "reported" = tagged fact.

---

## 2. Company Profile (context)

Alphabet Inc. is the parent of Google. Its reportable structure is **Google Services** (Search & other, YouTube ads, Network/partner properties, subscriptions/platforms/devices — including Google Play, YouTube Premium/TV, Google One, Pixel), **Google Cloud** (Google Cloud Platform and Google Workspace), and **Other Bets** (early-stage, long-duration bets such as Waymo). Advertising remains the dominant profit engine; Google Cloud is the second-largest and fastest-scaling revenue line. The company is a **single-class-A/B/C share structure** with combined shares outstanding of **12,541M** at 2023-09-30.

*Note: profile description is company-identity context; the segment-level financials are not in the dataset and are deliberately not quantified here.*

---

## 3. Income Statement Analysis

### 3.1 Revenue (derived and validated)

The dataset did not return a revenue tag, so revenue is derived as **`CostsAndExpenses + OperatingIncomeLoss`** (a valid identity for this filer's presentation, as total costs include cost of revenue and all opex, excluding OI&E).

| Period | Derived Revenue | Basis |
|---|---|---|
| Q3 2023 | **$76,693M** | 55,350 + 21,343 |
| 9M 2023 | **$221,084M** | 160,488 + 60,596 |
| Q3 2022 | **$69,092M** | 51,957 + 17,135 |
| 9M 2022 | **$206,788M** | 150,106 + 56,682 |

**Validation:** these derived figures reconcile exactly to Alphabet's disclosed quarterly revenue of $69,787M (Q1'23) + $74,604M (Q2'23) + $76,693M (Q3'23) = $221,084M. The derivation is trustworthy.

**Growth trajectory:**

| Metric | Q3'23 | Q3'22 | YoY | 9M'23 | 9M'22 | YoY |
|---|---|---|---|---|---|---|
| Revenue | 76,693 | 69,092 | **+11.0%** | 221,084 | 206,788 | **+6.9%** |
| 1H implied revenue | — | — | — | 144,391 | 137,696 | +4.9% |

**Actionable insight:** the quarterly growth profile is **accelerating sharply through the year** (+4.9% in 1H → +11.0% in Q3). Q3 is also sequentially stronger ($76.69B vs. a $72.20B 1H run-rate, **+6.2% QoQ**). Momentum was up and to the right into the Q4 print.

### 3.2 Margins

| Metric | Q3'23 | Q3'22 | Δ | 9M'23 | 9M'22 | Δ |
|---|---|---|---|---|---|---|
| Cost of revenue | 33,229 (43.3% of rev) | 31,158 (45.1%) | **−180bp** | 95,757 (43.3%) | 90,861 (43.9%) | −60bp |
| Gross profit | 43,464 | 37,934 | +14.6% | 125,327 | 115,927 | +8.1% |
| Gross margin | **56.7%** | 54.9% | +180bp | **56.7%** | 56.1% | +60bp |
| Opex (total less COGS) | 22,121 (28.8%) | 20,799 (30.1%) | −130bp | 64,731 (29.3%) | 59,245 (28.6%) | +70bp |
| **Operating income** | **21,343** | 17,135 | **+24.6%** | 60,596 | 56,682 | +6.9% |
| **Operating margin** | **27.8%** | 24.8% | **+300bp** | 27.4% | 27.4% | flat |

**Actionable insight:** the entire margin story is **cost-of-revenue driven** (data-center efficiency, lower depreciation intensity after capex discipline, and mix). Opex as a % of revenue actually *rose* over 9M (28.6% → 29.3%), meaning the 9M operating margin was flat despite gross-margin gains — G&A grew to $11,219M from $10,628M (+5.6%). The Q3 recovery is genuine but is **one quarter of evidence**, and it is the single most important thing to confirm on the Q4 call.

### 3.3 Below the operating line — the key quality flag

| Metric | Q3'23 | Q3'22 | 9M'23 | 9M'22 |
|---|---|---|---|---|
| Nonoperating income/(expense), net of interest | **−146** | −902 | **+709** | −2,501 |
| Interest income (other) | 1,066 | 615 | 2,755 | 1,515 |
| Interest expense | 116 | 101 | 239 | 267 |
| Pre-tax income | 21,197 | 16,233 | 61,305 | 54,181 |
| Income tax | 1,508 | 2,323 | 8,197 | 7,833 |
| **Effective tax rate** | **7.1%** | 14.3% | **13.4%** | 14.5% |
| Net income | **19,689** | 13,910 | **53,108** | 46,348 |
| Net margin | **25.7%** | 20.1% | 24.0% | 22.4% |
| Diluted EPS | **$1.55** | $1.06 | **$4.16** | $3.50 |
| Diluted shares (implied) | ~12,703M | ~13,123M | — | — |

**Actionable insight #1 — the tax rate is doing real work.** Q3'23's 7.1% rate vs. a 14.5% normalized rate accounts for roughly **$1.56B of the tax line** (21,197 × 14.5% = $3,074M vs. $1,508M reported). Restating Q3'23 at a 14.5% rate: net income ≈ **$18,123M**, diluted EPS ≈ **$1.43**. That means **~$0.12 of the $1.55 print (~8%) was a low tax rate rather than operating performance.** Year-over-year, tax added roughly **$0.12–0.13 of the +$0.49 EPS improvement.** Annualize a 7.1% rate at your peril; the 9M rate of 13.4% is already normalizing upward, and 2024 should revert toward the mid-teens absent new discrete items.

**Actionable insight #2 — interest income is now material.** $2.76B over nine months (+81.8% YoY) off a ~$120B cash/securities pile is a real, recurring earnings stream that cushions OI&E. But with rate cuts priced for 2024, this tailwind **stops helping and starts hurting** — model it as a headwind to 2024 EPS growth.

**Actionable insight #3 — equity-mark volatility is shrinking.** 9M'22 OI&E was a **−$2.5B drag** (equity securities FV-NI unrealized loss of −$2,494M). 9M'23 flipped to a modest **+$709M** contributor despite a further −$194M FV-NI loss and a −$789M FX transaction loss. The year-over-year swing from the "other income" line is ~$3.2B, which is **non-operating noise, not business improvement.**

### 3.4 Stock-based compensation — the dilution leak

| Metric | Q3'23 | Q3'22 | YoY | 9M'23 | 9M'22 | YoY |
|---|---|---|---|---|---|---|
| SBC (allocated) | 5,800 | 5,000 | **+16.0%** | **16,500** | 14,400 | **+14.6%** |
| SBC % of revenue | 7.6% | 7.2% | +40bp | **7.5%** | 7.0% | +50bp |
| SBC % of operating income | 27.2% | 29.2% | — | 27.2% | 25.4% | +180bp |

**Actionable insight:** SBC is growing **faster than revenue** (14.6% vs. 6.9%) and faster than operating income over nine months. Share count still fell from 12,849M to 12,541M (−308M, **−2.4%**) because repurchases ($45.31B) swamped net SBC issuance — so buybacks are partly **offsetting dilution rather than shrinking the float**. If SBC growth outpaces the buyback pace, the "EPS beats revenue" mechanical tailwind fades.

---

## 4. Balance Sheet Analysis (2023-09-30 vs. 2022-12-31)

| Line | 2023-09-30 | 2022-12-31 | Δ |
|---|---|---|---|
| Cash & equivalents | **30,702** | 21,879 | **+40.3%** |
| Marketable (AFS debt) securities | 85,218 | — | — |
| **Cash + marketable securities** | **119,935** | 113,762 | **+5.4%** |
| Accounts receivable, net | 41,020 | 40,258 | +1.9% |
| Inventory, net | 2,957 | 2,670 | +10.8% |
| **Total current assets** | **176,310** | 164,795 | **+7.0%** |
| Non-marketable equity securities | 28,821 | 28,529 | +1.0% |
| Equity securities FV-NI | 4,973 | 5,156 | −3.5% |
| Equity method investments | 1,500 | 1,500 | 0.0% |
| **Total assets** | **396,711** | 365,264 | **+8.6%** |
| **Total liabilities** | **123,509** | 109,120 | **+13.2%** |
| **Stockholders' equity (derived)** | **273,202** | 256,144 | **+6.7%** |
| Equity / assets | **68.9%** | 70.1% | −120bp |
| Operating lease liabilities (cur + non-cur) | 15,265 | 14,978 | +1.9% |
| Finance lease liabilities | 2,314 | 2,142 | +8.0% |
| Deferred tax assets, net | **10,983** | 5,261 | **+108.7%** |
| Income taxes payable, current | **13,528** | 1,632 | **+729%** |

**Key observations for traders:**

1. **Liquidity is overwhelming and improved.** Cash quadrupled… no — cash grew 40% to $30.7B, and total cash + marketable securities reached **$119.94B**. Against ~**$15.3B** of debt principal (sum of the FY22 10-K maturity ladder: 221 + 1,156 + 1,159 + 2,163 + 1,166 + 9,447), net cash is roughly **~$105B**, or **~$9.56 per share**. This is a floor under downside, and it funds the entire buyback without leverage.
2. **Liabilities grew 13.2%, faster than assets (8.6%).** The driver is identifiable: **accrued income taxes current jumped from $1.63B to $13.53B** (+$11.9B) and **deferred tax assets nearly doubled to $10.98B**. This is the tax-accrual event discussed in §6 — a **timing/accrual build, not a debt-funded deterioration.** Watch this line: a reversal in 2024 would *drain* cash.
3. **AFS unrealized losses are healing.** Accumulated unrealized loss in the AFS portfolio narrowed to **$4,244M** from $4,779M, and short-dated (<12mo) unrealized loss positions collapsed from $2,029M to $762M. A rate-driven recovery in the securities book is a secondary, non-P&L source of book value improvement.
4. **Non-marketable equity book is carried above cost on mark-ups.** Cumulative upward adjustments of **$18,000M** vs. downward adjustments of **$6,700M** (up from $4,500M a year ago) on a $28.8B carrying value. If public comparables de-rate, this book is exposed.
5. **Book value per share ≈ $21.79** (273,202 / 12,541M).

*Gap:* PP&E, goodwill, total current liabilities at 9M'23, and the explicit long-term-debt line were not returned by the tool. Debt is therefore **estimated from the FY22 maturity schedule**, not taken from a 9/30/23 tag.

---

## 5. Cash Flow Analysis — Where the Truth Lives

| Metric | 9M'23 | 9M'22 | YoY |
|---|---|---|---|
| Operating cash flow | **82,831** | 67,881 | **+22.0%** |
| Capex (PP&E purchases) | 21,232 | 23,890 | **−11.1%** |
| **Free cash flow (derived)** | **61,599** | **43,991** | **+40.0%** |
| FCF margin | **27.9%** | 21.3% | +660bp |
| Capex % of revenue | 9.6% | 11.6% | −200bp |
| Investing cash flow | (20,896) | (14,071) | 48.5% more outflow |
| Financing cash flow | (52,785) | (52,128) | −1.3% |
| Share repurchases | **45,313** | 43,889 | +3.2% |
| Debt proceeds | 9,298 | 44,322 | −79.0% |
| Debt repayments | 9,621 | 45,350 | −78.8% |
| FX effect on cash | (327) | (643) | improved |
| Net change in cash | +8,823 | +1,039 | **+749%** |

**Annual context (FY, from the 10-K facts):**

| | FY2022 | FY2021 | FY2020 |
|---|---|---|---|
| Operating cash flow | **91,495** | 91,652 | 65,124 |
| Investing cash flow | (20,298) | (35,523) | (32,773) |
| Financing cash flow | **(69,757)** | (61,362) | (24,408) |

**Actionable insights — this is the most under-appreciated section:**

1. **The +22% OCF headline is largely a tax-timing artifact.** Embedded in 9M'23 operating cash flow is a **+$10,392M adjustment for "increase in income taxes"** (i.e., higher taxes payable). In 9M'22 the same line was a **−$862M drag**. Stripping the tax accrual from both periods: 9M'23 adjusted OCF ≈ **$72,439M** vs. 9M'22 ≈ **$68,743M** → underlying growth ≈ **+5.4%**, not +22.0%. **A trader extrapolating +22% OCF growth into 2024 will be badly wrong.** If that payable reverses (a $10B+ cash outflow), OCF growth could go *negative* next year on a mechanical basis.
2. **FCF growth is also capex-assisted.** Capex *fell* 11.1% to $21.23B. Alphabet has publicly signaled a step-up in 2024 AI infrastructure capex — if that guidance is confirmed at the Q4 call, the FCF tailwind reverses. The **FCF margin of 27.9% is near a cyclical high** and should be treated as a peak-ish run-rate, not a base.
3. **Capital return is entirely buyback, with no dividend.** $45.3B repurchased in 9M'23 (~$60B annualized), reducing share count 2.4%. Combined with a $119.9B liquidity pool, a **dividend initiation is the single largest un-modeled optionality** in the story — and there is **no dividend tag anywhere in the data through Q3 2023**, so as of 2024-01-25, GOOGL pays no dividend.
4. **Debt is being deleveraged, not levered.** 2022 was a $44.3B gross-issuance / $45.4B repayment year; 2023 flipped to net *repayment* ($9.30B in vs. $9.62B out). No balance-sheet risk whatsoever.
5. Investing outflows rose on marketable-securities purchases and other investments ($2,176M into other investments), consistent with continued venture/AI-stake deployment.

---

## 6. Earnings-Quality Scorecard

| Flag | Direction | Magnitude | Confidence |
|---|---|---|---|
| Q3'23 effective tax rate 7.1% vs. 14.5% normalized | **Inflates EPS** | ~$0.12/share (~8% of Q3 EPS) | High (compute) |
| $10.4B increase in income taxes payable in OCF | **Inflates OCF** | Underlying OCF growth ~+5% vs. +22% reported | High (compute) |
| Capex down 11.1% | **Inflates FCF** | FCF growth +40% flattered by capex restraint | High |
| SBC +14.6% YoY, 7.5% of revenue | **Dilutes** | Partly offset by 2.4% buyback-driven share reduction | High |
| Interest income +81.8% YoY | **Inflates EPS** | Reverses if rates fall in 2024 | High |
| Equity-mark / FX swings | **Noise** | OI&E swung +$3.2B YoY | High |
| Multiple legal/regulatory accruals held ($9,143M "loss contingency" current accrual, flat vs. $9,106M) | **Neutral/overhang** | A ~$9.1B accrual is carried on the balance sheet | High (balance) |
| Accrued liabilities jumped to $55,602M from $37,866M | **Watch item** | Composition not disclosed in dataset | Medium |
| Antitrust / regulatory outcomes | **Binary risk** | Not in dataset; not quantified here | — |

**Fair-state earnings estimate:** combining the tax normalization (~$1.56B) and stripping the ~$2.8B favorable YoY OI&E swing, *sustainable* 9M'23 net income is closer to **~$51–52B** vs. $53.1B reported — modestly lower, but still **~+11% YoY**. The operating improvement is real; the headline beats are overstated by roughly 10%.

---

## 7. Catalysts, Risks, and Data Gaps for the Next 1–4 Weeks

**Catalyst #1 — Q4/FY2023 earnings (early February 2024, pre-print).** The FY2023 10-K was not yet on file at 2024-01-25, so this is the dominant near-term event and it lands **inside the trading horizon**. What to actually trade on:
- **Q4 gross margin**: does the Q3 jump to 56.7% hold? This is the thesis.
- **2024 capex guidance**: a step-up materially de-rates the FCF-margin peak of 27.9%.
- **Tax rate guidance**: confirmation that 7.1% was discrete and the rate reverts to mid-teens (this is the consensus-risk item).
- **Income-taxes-payable reversal**: whether the $13.5B accrual unwinds into a cash outflow in 2024.
- **Cloud growth and margin**: not derivable from this dataset — must come from the release.

**Risk #1 — multiple compression from extrapolated growth.** The tape may be extrapolating Q3's +46% EPS growth. Reported EPS growth was aided ~8% by tax. On a normalized basis Q3 EPS grew ~**+35%** — still excellent, but a different number.

**Risk #2 — rate sensitivity of "other income."** A ~$120B securities book earning elevated rates is a *large* contributor: $2.76B in 9M'23. Every 100bp of rate decline on the liquid portfolio is roughly $1.2B of annualized pre-tax income at risk (approximate, portfolio-duration dependent).

**Risk #3 — legal/regulatory overhang.** The balance sheet carries a **$9,143M current loss-contingency accrual** (essentially flat YoY at $9,106M), which tells you management is reserving for something material and ongoing. This dataset contains no litigation narrative — treat as an unquantified tail risk that a single adverse ruling could crystallize.

**Risk #4 — FX.** Foreign currency transaction losses widened to **−$789M** in 9M'23 from −$469M. With a strong dollar, that's a continuing EPS drag that flows through OI&E.

**Confirmed data gaps (do not fill these with guesses):**
- **Insider transactions: entirely unavailable.** No Form 4 data exists in the authorized archive for GOOGL at this date. The only defensible read on management's capital-allocation conviction is the **$45.3B of open-market repurchases in 9M'23** — a company-level, not insider-level, signal. Anyone citing insider activity on GOOGL for this period is fabricating it.
- No segment revenue/profit, no PP&E, no goodwill, no total-debt tag, no dividend history (none exists), no share-price or valuation data.

---

## 8. Actionable Framings (evidence-based, no price target)

1. **Do not underwrite +22% OCF growth or +46% EPS growth.** Normalized, the underlying engine is ~**+5% OCF** and ~**+11% net income** on ~**+7% revenue**. Anchor 2024 expectations accordingly; the gap between headline and underlying is ~15 points of growth, which is exactly the kind of delta that produces post-earnings air pockets.
2. **The margin thesis is the real long, and it is a one-quarter sample.** Gross margin +180bp on a 43.3% cost-of-revenue ratio is the highest-quality datapoint in this entire report. A confirmatory Q4 gross margin ≥56% justifies paying for operating leverage; a reversion to ~55% invalidates it.
3. **Downside is floored, not fragile.** ~$105B net cash, ~$9.56/share in cash+securities, 68.9% equity/assets, no dividend obligation, and a buyback running at ~$60B annualized. This is a "buy the drawdown" balance sheet in a way most mega-caps are not.
4. **Own the tax-rate normalization risk explicitly.** The 7.1% → ~14.5% reversion is ~$0.12/quarter of EPS at risk. If the street's Q4 number implicitly carries a low rate, the *beat* may be a *miss* on quality.
5. **The un-priced optionality is a dividend.** Zero dividend through 9M'23 with $119.9B of liquidity and a maturing buyback. An initiation would broaden the holder base; its absence for now is a factual, not speculative, statement as of 2024-01-25.
6. **Sizing, not direction, is the differentiated call.** Improving operations + peak-ish FCF margin + imminent binary catalyst (Q4 print + 2024 capex/tax guidance) + a fortress balance sheet = a position that should be **core-sized with a defined event risk band around the February print**, not a maximum-conviction momentum add.

---

## 9. Key Facts Summary Table

| Category | Metric | Value | Period | Signal |
|---|---|---|---|---|
| **Identity** | Company / Ticker | Alphabet Inc. / **GOOGL** | — | Mega-cap comm. services |
| **Data cut-off** | Latest filing in dataset | Q3 FY23 10-Q, filed 2023-10-25 | — | FY23 10-K **not yet filed** |
| | Insider transactions | **UNAVAILABLE — not inferred** | — | Explicit data gap |
| **Revenue (derived)** | Q3'23 | **$76,693M** (+11.0% YoY) | Q3'23 | Reacceleration |
| | 9M'23 | **$221,084M** (+6.9% YoY) | 9M'23 | 1H was +4.9% |
| **Profitability** | Q3'23 gross margin | **56.7%** (+180bp) | Q3'23 | Best datapoint in report |
| | Q3'23 operating margin | **27.8%** (+300bp) | Q3'23 | Real operating leverage |
| | 9M'23 operating margin | 27.4% (flat YoY) | 9M'23 | Opex rose to 29.3% |
| | Q3'23 net margin | **25.7%** (vs. 20.1%) | Q3'23 | Tax-flattered |
| **EPS** | Q3'23 diluted | **$1.55** (+46.2%) | Q3'23 | ~$1.43 normalized |
| | 9M'23 diluted | **$4.16** (+18.9%) | 9M'23 | vs. +14.6% net income |
| **Tax** | Q3'23 effective rate | **7.1%** | Q3'23 | **Key quality flag** |
| | 9M'23 effective rate | 13.4% (vs. 14.5%) | 9M'23 | Normalizing upward |
| **SBC** | 9M'23 allocated SBC | **$16,500M** (+14.6%) | 9M'23 | 7.5% of revenue |
| **Balance sheet** | Cash + marketable securities | **$119,935M** | 2023-09-30 | +5.4% YTD |
| | Total assets | $396,711M (+8.6%) | 2023-09-30 | — |
| | Total liabilities | $123,509M (+13.2%) | 2023-09-30 | Tax-accrual driven |
| | Stockholders' equity | **$273,202M** | 2023-09-30 | 68.9% of assets |
| | Debt principal (FY22 10-K ladder) | ~**$15,300M** | 2022-12-31 | ≈ **$105B net cash** |
| | Cash + securities / share | **~$9.56** | 2023-09-30 | Downside floor |
| | Book value / share | **~$21.79** | 2023-09-30 | — |
| | Loss contingency accrual (current) | $9,143M | 2023-09-30 | Unquantified legal overhang |
| | Income taxes payable (current) | $13,528M (from $1,632M) | 2023-09-30 | Reversal risk in 2024 |
| **Cash flow** | 9M'23 operating cash flow | **$82,831M** (+22.0%) | 9M'23 | **+5.4% ex-tax-timing** |
| | 9M'23 capex | $21,232M (−11.1%) | 9M'23 | 9.6% of revenue |
| | 9M'23 free cash flow | **$61,599M** (+40.0%) | 9M'23 | 27.9% FCF margin (peak-ish) |
| | 9M'23 buybacks | **$45,313M** | 9M'23 | Only capital return |
| | Dividend | **None** | through Q3'23 | Un-priced optionality |
| | Share count | 12,541M (−2.4% YTD) | 2023-09-30 | Buyback > dilution |
| **FY history** | OCF FY22 / FY21 / FY20 | $91,495M / $91,652M / $65,124M | FY20–22 | Stable then step-up |
| | Financing CF FY22 | **−$69,757M** | FY22 | Heavy buyback era |
| **Near catalyst** | Q4/FY23 report | **Early Feb 2024** | — | Watch GM, capex, tax, Cloud |
| **Positional read** | Stance | **Core long, event-risk banded** | — | Own margin thesis; fade headline growth extrapolation |