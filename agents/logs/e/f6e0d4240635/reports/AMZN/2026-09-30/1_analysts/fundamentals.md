# AMZN — Fundamental Deep Dive
**Amazon.com, Inc. | SEC facts through the Q2 2026 10-Q (period ended 30-Jun-2026; filed 31-Jul-2026)**
**Analysis date: 30-Sep-2026**

---

## 1. Data provenance, scope and limitations (read first)

Everything below is derived from the point-in-time SEC fact package available as of 2026-09-30. Three caveats matter for a trader:

| Item | Status |
|---|---|
| Latest reported period | **Q2 2026 (quarter ended 30-Jun-2026)**, 10-Q accepted 2026-07-31 |
| Q3 2026 | Quarter **ends today**; results not yet filed → no Q3 data exists in the slice |
| Segment detail (NA / Int'l / AWS revenue & margin) | **Not in the slice.** Only `NumberOfOperatingSegments = 3` is tagged. Segment tables must come from the 10-Q itself |
| Revenue line item | **Not directly tagged.** Reconstructed exactly as `CostsAndExpenses + OperatingIncomeLoss` (this recon reproduces the actual reported Q2-25 figure of $167,702M and H1-25 $323,369M to the dollar, so the method is validated) |
| Market price / market cap | **Not available in this toolset** → no P/E, EV/EBITDA or price targets are computed here. Earnings and cash-flow anchors are provided instead |
| Insider transactions | **DATA_UNAVAILABLE** — the vendor has no authorized point-in-time insider archive for AMZN. No insider activity is inferred or fabricated |
| Annual statements | The annual endpoint returned the same fact set (no separate FY2023/FY2024 history). FY2025 is **derived** as H1-2025 + (TTM Jun-26 − H1-2026); those figures are labelled "derived" |

---

## 2. Company profile (structural view)

Amazon.com, Inc. (AMZN) is a three-segment business (`NumberOfOperatingSegments = 3`): **North America**, **International**, and **Amazon Web Services**. Revenue pools span online stores, third-party seller services (1P/3P retail + FBA), advertising, subscription services (Prime), physical stores, and AWS (IaaS/PaaS, database, custom silicon — Trainium/Inferentia — and managed AI services). Fiscal year = calendar year.

What the *financials* tell us about the current operating model (this is the important part for a trader):

- This is no longer a low-margin retail story being re-rated by AWS mix alone. **H1 2026 operating margin was 13.4% vs 11.6% in H1 2025**, with revenue +18.2% — i.e., margin *expanded* while capex intensity roughly doubled. That combination is unusual and is the single most important fundamental fact in this dataset.
- The company has simultaneously become (a) a **capital-intensive AI infrastructure builder** (capex 26% of revenue), (b) a **levered borrower again** (long-term debt +93% in six months), and (c) a **large holder of private AI equity** ($122.3B of non-marketable equity securities, marked up $62.8B in H1 2026). Those three facts drive both the upside and the earnings-quality risk.

---

## 3. Income statement: revenue re-acceleration + real operating leverage

### 3.1 Reconstructed quarterly P&L (USD millions)

| USD M | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 | Q2 YoY | H1 2025 | H1 2026 | H1 YoY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Net sales (derived)** | 155,667 | 167,702 | **181,519** | **200,606** | **+19.6%** | 323,369 | **382,125** | **+18.2%** |
| Cost of sales | 76,976 | 80,809 | 87,463 | 95,778 | +18.5% | 157,785 | 183,241 | +16.1% |
| Total costs & expenses | 137,262 | 148,531 | 157,667 | 173,145 | +16.6% | 285,793 | 330,812 | +15.8% |
| **Operating income** | 18,405 | 19,171 | 23,852 | **27,461** | **+43.2%** | 37,576 | **51,313** | **+36.6%** |
| Operating margin | 11.8% | 11.4% | 13.1% | **13.7%** | +230 bp | 11.6% | **13.4%** | +180 bp |
| Non-operating income (exp.) | 3,274 | 1,686 | 15,982 | **53,396** | n.m. | 4,960 | **69,378** | n.m. |
| Pre-tax income | 21,679 | 20,857 | 39,834 | 80,857 | +288% | 42,536 | 120,691 | +184% |
| Tax | 4,553 | 2,678 | 9,560 | 18,199 | | 7,231 | 27,759 | |
| Effective tax rate | 21.0% | 12.8% | 24.0% | 22.5% | | 17.0% | 23.0% | |
| **Net income** | 17,127 | 18,164 | 30,255 | **62,647** | **+245%** | 35,291 | **92,902** | **+163%** |
| **Diluted EPS** | 1.59 | 1.68 | 2.78 | **5.75** | **+242%** | 3.27 | **8.53** | **+161%** |

*Q2-2026 annualised revenue run-rate: **~$802B**.*

### 3.2 The critical distinction: headline EPS vs. "core" EPS

Q2 2026 non-operating income was **$53.4B**, of which **$50.5B was an upward fair-value adjustment on equity securities without a readily determinable fair value** (i.e., private-company marks — the Anthropic-type stake). H1 2026 marks totalled **$62.8B** vs only **$86M** in H1 2025.

Strip that out (tax-effecting at the period rate) and the underlying business looks like this:

| USD M (except EPS) | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 |
|---|---:|---:|---:|---:|
| Reported diluted EPS | 1.68 | **5.75** | 3.27 | **8.53** |
| Non-operating income | 1,686 | 53,396 | 4,960 | 69,378 |
| After-tax non-operating contribution (est.) | ~1,470 | ~41,380 | ~4,120 | ~53,800 |
| **Core net income (est.)** | ~16,700 | **~21,300** | ~31,200 | **~39,500** |
| **Core diluted EPS (est.)** | **~1.55–1.60** | **~1.95** | **~3.00** | **~3.64** |
| Core EPS growth | — | **~+23% (22–27% range)** | — | **~+22%** |

**Actionable read-through:** the headline "+242% EPS growth" is mostly a non-cash mark-to-model gain. The *real* earnings engine grew ~22–23% with ~13–14% operating margins. Any valuation or screening done on reported GAAP EPS (H1 $8.53, TTM $135.3B net income) will materially overstate sustainable earnings power. Forward models should use ~$1.95 quarterly core EPS as the Q2-26 base, growing ~20%+.

### 3.3 Operating cost structure — where the leverage came from

H1 2026 vs H1 2025 (% of revenue):

| Line (USD M) | H1 2025 | % rev | H1 2026 | % rev | Change |
|---|---:|---:|---:|---:|---:|
| Cost of sales | 157,785 | 48.8% | 183,241 | 48.0% | +16.1% (**gross margin +85 bp**) |
| Marketing | 21,179 | 6.55% | 22,012 | 5.76% | **+3.9%** (79 bp of leverage) |
| G&A | 5,593 | 1.73% | 5,375 | 1.41% | **−3.9%** (32 bp of leverage) |
| Stock-based comp | 10,223 | 3.16% | 10,070 | 2.64% | **−1.5%** (52 bp of leverage) |
| D&A | 29,489 | 9.12% | 38,933 | 10.19% | **+32.0%** (107 bp headwind) |
| Operating lease cost | 6,666 | 2.06% | 8,035 | 2.10% | +20.5% |
| Interest expense | 1,057 | — | 2,114 | — | **+100.0%** |
| Interest income | 2,151 | — | 2,430 | — | +13.0% |

The striking feature: **SBC fell 1.5% and G&A fell 3.9% while revenue rose 18.2%.** Margin expansion is therefore *not* comp-driven — it is genuine cost discipline plus mix. Offsetting that, **D&A is compounding at +32%** (Q2-26 D&A $19,988M, +31.3% YoY) as the 2024–2025 capex wave enters service, and **interest expense doubled** as debt was issued. Both headwinds are set to intensify (see §6–7).

**Operating leverage math:** operating income grew 36.6% on 18.2% revenue growth → incremental margin of ~**24%** on incremental revenue. If that holds, every $10B of incremental quarterly revenue adds roughly $2.4B of operating income.

---

## 4. Earnings quality: the $122B private-equity book is now a P&L driver

| Metric (USD B) | 31-Dec-2025 | 30-Jun-2026 | Change |
|---|---:|---:|---:|
| Equity securities w/o readily determinable FV (carrying value) | 16.2 | **122.3** | **+106.1** |
| Upward price adjustments recognised in earnings (period) | $0.086 (H1-25) | **$62.814 (H1-26)** | +73,000% |
| — of which Q2 2026 | — | **$50.486** | |
| Deferred income tax expense (H1) | 0.518 | **30.489** | +$30.0B |
| Cash income taxes paid (H1) | 5.638 | **3.978** | −29% |

Three conclusions:

1. **Scale:** the private-equity portfolio is now **11.2% of total assets** and roughly the size of the entire long-term debt balance ($133.0B). It is a genuine, under-appreciated asset — but it is opaque, unlisted and valued by the company's own marks.
2. **Non-cash:** H1 2026 cash taxes were only **$4.0B against $27.8B of tax expense**, because the marks create deferred tax liabilities (~$30.5B of deferred expense). This flatters near-term cash conversion and will reverse if marks reverse.
3. **Symmetry risk:** the same mechanism that added ~$41B after-tax (~$3.80/share) to Q2 2026 EPS can subtract it. A 30% mark-down of the $122.3B portfolio would be a ~$37B pre-tax hit (~$2.60–2.90/share). This is the **single largest source of GAAP EPS volatility** into Q3/Q4 2026.

Also note: **AOCI swung from +$28.2B to +$66.3B (+$38.1B)** in six months, driving comprehensive income of $131.0B vs net income of $92.9B. FX was only −$1.6B, so ~**+$39.7B of other investment/securities marks** flowed through OCI. Book value therefore rose by the full $131.0B of comprehensive income in H1 — a very large equity build, but one with mark-to-market reversal risk.

---

## 5. Balance sheet: bigger, more levered, still liquid

| USD B | 31-Dec-2025 | 30-Jun-2026 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 86.81 | 78.21 | −8.60 |
| Marketable securities (AFS) | 45.80 | 97.90 | **+52.10** |
| **Total cash + securities** | **132.61** | **176.11** | **+43.50** |
| Accounts receivable, net | 67.73 | 88.09 | **+20.36 (+30.1%)** |
| Inventory, net | 38.33 | 38.18 | −0.15 |
| Current assets | 229.08 | 249.26 | +20.18 |
| Equity securities w/o RDFV | 16.20 | 122.30 | **+106.10** |
| **Total assets** | **818.04** | **1,095.69** | **+277.65 (+33.9%)** |
| Accounts payable | 121.91 | 147.44 | +25.53 |
| Accrued liabilities | 75.52 | 73.41 | −2.11 |
| Current liabilities | 218.01 | 241.27 | +23.27 |
| Long-term debt — current | 2.75 | 3.33 | +0.58 |
| Long-term debt — non-current | 65.65 | 128.89 | **+63.24** |
| **Total long-term debt** | **68.84** | **133.00** | **+64.16 (+93.2%)** |
| Finance lease liabilities | 12.29 | 13.45 | +1.16 |
| Operating lease liabilities | 89.25 | 96.32 | +7.07 |
| Contract liabilities (deferred revenue) | 25.00 | 24.92 | −0.08 |
| Additional paid-in capital | 140.02 | 149.62 | +9.60 |
| AOCI | +28.23 | +66.29 | **+38.06** |

**Liquidity & leverage diagnostics**
- Current ratio: **1.03x** (249.26 / 241.27) vs 1.05x at year-end — thin, but structurally normal for Amazon.
- Liquid assets / current liabilities: **0.73x**.
- Net debt position: debt + finance leases **$146.5B** vs cash + securities **$176.1B** → **net cash of ~$29.6B**. Include operating leases ($96.3B, off the "debt" line but real) and net obligations are ~**$66.7B** — under 0.5x annualised EBITDA (~$180B run-rate). Balance sheet remains investment-grade strong.
- Interest coverage: H1 operating income $51.3B / interest expense $2.1B = **24x** (Q2: 21x). Not a solvency issue; a *trend* issue.
- **Contractual obligations: $650.0B**, of which **$78.1B due within 12 months** (purchase commitments, likely AWS capacity/energy/chips), plus operating lease payments of $116.4B undiscounted. This is the fixed-cost backbone of the AI build-out and the key downside operating-leverage risk if demand slows.

**Working capital flags**
- AR +30.1% vs revenue +19.6% YoY → DSO ~40 days (vs ~37 at year-end). Watch for receivables build in AWS/ads.
- Inventory flat at $38.2B on ~20% growth → inventory turns improved materially (a genuine efficiency positive). Inventory valuation reserves fell $3.3B → $3.0B.
- AP +21% — suppliers are financing part of the build.

---

## 6. Cash flow: the capex story is the whole story

| USD B | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 | FY2025 (derived) | **TTM Jun-26** |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash flow | 32.52 | **45.39** | 49.53 | **71.42** | 139.51 | **161.40** |
| Purchases of PP&E (capex) | 32.18 | **54.21** | 57.20 | **98.41** | 131.82 | **173.03** |
| **Free cash flow (OCF − capex)** | **+0.33** | **−8.82** | **−7.67** | **−26.99** | **+7.69** | **−11.63** |
| Business acquisitions, net | 1.70 | **24.36** | 1.65 | **39.77** | — | **41.96** |
| Purchases of marketable securities | 17.80 | 26.01 | 31.13 | 49.26 | — | 72.90 |
| Proceeds from sales/maturities | 11.44 | 24.20 | 19.18 | 41.88 | — | 67.09 |
| LT debt issued | 0.00 | 13.56 | 0.75 | **67.00** | — | **81.93** |
| LT debt repaid | 2.75 | 2.75 | 2.75 | 2.75 | — | 5.02 |
| Net financing cash flow | −2.54 | +10.15 | −2.59 | **+62.91** | — | **+75.16** |
| Net investing cash flow | −39.42 | −79.25 | −69.23 | **−143.46** | — | **−216.78** |
| D&A | 15.23 | 19.99 | 29.49 | 38.93 | 65.76 | **75.20** |

**Interpretation**

1. **Cash generation is accelerating faster than earnings.** Q2 2026 OCF +39.6% YoY; H1 OCF +44.2%; OCF margin 18.7% of revenue. That is real, and it is *despite* a working-capital drag from receivables and the non-cash nature of the investment gains.
2. **Free cash flow has turned negative.** TTM FCF **−$11.6B** (vs +$13.5B in the prior TTM period, and +$7.7B in FY2025). Capex is running at **25.8% of H1 revenue** and **27.0% in Q2 alone** — up from ~17.7% in H1 2025. Capex is compounding: Q1-26 $44.2B → Q2-26 $54.2B.
3. **The gap is being funded with debt, not just cash.** $67.0B of long-term debt issued in H1 2026 ($81.9B TTM) versus $0.75B in H1 2025. Net financing inflow of +$62.9B in H1. This is the mechanism behind the 93% jump in long-term debt and 100% jump in interest expense.
4. **M&A has re-appeared at scale:** **$39.8B of cash for business acquisitions in H1 2026** (Q2 alone $24.4B) versus $1.7B in H1 2025 — the largest such outlay in the company's history. The disclosure slice does not name targets; combined with the $106B increase in the private-equity book, the likely read is strategic AI/compute investments. **This is a material, under-modelled use of cash.**
5. **Depreciation lag:** TTM D&A $75.2B against $173.0B of capex. As that base depreciates (even over 6 years), D&A should trend toward $110–130B annually within 24 months, i.e., a **$35–55B annual P&L headwind** — surmountable only if the new capacity earns AWS/AI revenue at high incremental margins.
6. **No buyback signal:** shares outstanding rose from 10,731M to 10,783M (+0.5%) and 10,786.3M as of 22-Jul-2026; APIC rose $9.6B (roughly SBC). Capital is going to capex, M&A and debt service, not repurchases.

---

## 7. Multi-period fundamental history (derived where noted)

| USD B | TTM Jun-25 | FY2025 (derived) | H1 2026 | TTM Jun-26 | Trend |
|---|---:|---:|---:|---:|---|
| Net sales | n/a | n/a | 382.13 | n/a | +18.2% H1 YoY (accelerating: Q1 +16.6%, Q2 +19.6%) |
| Operating income | n/a | n/a | 51.31 | n/a | +36.6% H1 YoY; margin 11.6% → 13.4% |
| Net income | 70.62 | **77.67** | 92.90 | **135.28** | Inflated by investment marks in 2026 |
| Operating cash flow | 121.14 | 139.51 | 71.42 | **161.40** | +33% TTM |
| Capex | 107.66 | 131.82 | 98.41 | **173.03** | +61% TTM |
| Free cash flow | +13.48 | +7.69 | −26.99 | **−11.63** | Deteriorating |
| D&A | 58.56 | 65.76 | 38.93 | **75.20** | +28% TTM |
| Diluted EPS | n/a | n/a | 8.53 | n/a | Core EPS ~3.64 (ex-marks) |

The trajectory is unambiguous: **revenue and operating profit are inflecting upward at the fastest rate in years, while free cash flow is inflecting downward and the balance sheet is releveraging to fund it.** That is a classic "growth investment cycle" signature — bullish for the revenue/margin line, bearish for FCF-based valuation and near-term multiple support.

---

## 8. Fundamental scorecard — green flags vs. red flags

**Green flags**
- Revenue growth accelerated to **+19.6% YoY** in Q2 2026 (from +16.6% in Q1) — a ~$802B annualised run-rate.
- Operating margin **13.7%** (+230 bp YoY), operating income **+43%**; incremental margins ~24%.
- **SBC −1.5%** and G&A −3.9% on +18% revenue → leverage is structural, not comp-driven.
- Operating cash flow **+44%** in H1 to $71.4B; OCF margin 18.7%.
- **$176.1B** of cash + securities; net cash excluding leases; 24x interest coverage; current ratio 1.03x.
- Inventory flat on ~20% growth → working-capital efficiency improving.
- **$122.3B** private-equity/AI portfolio (11% of assets) = latent, unrecognised optionality.

**Red flags**
- **Earnings quality:** ~45% of H1 2026 net income ($62.8B of $120.7B pre-tax) came from non-cash private marks; cash taxes were only $4.0B vs $27.8B expense. Reversal risk is symmetric.
- **Negative FCF:** TTM **−$11.6B**; H1 capex $98.4B = 25.8% of revenue; Q2 capex $54.2B = 27.0% of revenue.
- **Releveraging:** LT debt **+93%** to $133.0B in six months; $82B issued TTM; interest expense **+100%** in H1.
- **$650B of contractual obligations** ($78.1B within 12 months) — a fixed-cost bet on AI demand.
- **D&A +32% YoY** and rising — a mechanical margin headwind for 2027–2028.
- **$39.8B of H1 acquisitions** + $106B private-equity build = large, opaque capital allocation.
- AR +30% vs revenue +19.6%; current ratio 1.03x — limited cushion.
- **No insider-transaction data available** — a genuine information gap in this dataset (not a red flag about the company).

---

## 9. Actionable insights for traders

**1. Trade the core, not the headline.** Build models on ~**$1.95 core EPS** for Q2-26 and ~**$3.64 for H1-26** (annualised run-rate ~$7.8, before seasonality). Reported GAAP EPS ($5.75 Q2, $8.53 H1, $135.3B TTM net income) embeds ~$3.80/share of non-cash marks in Q2 alone. If the market is anchoring on GAAP EPS, AMZN's multiple looks far cheaper than economic reality — and a mark-down quarter would look like a "miss" even if operations beat.

**2. The Q3 2026 print (late Oct 2026) is a three-variable event.** Watch: (a) revenue ≥ ~$205–210B to sustain the +19% trajectory; (b) operating margin holding ≥13% *despite* D&A +30%+; (c) capex guidance — Q2 alone was $54.2B, TTM $173.0B, and the trend is up. A revenue beat paired with an FCF/capex miss is the most likely negative surprise configuration.

**3. Free cash flow is the pressure point.** TTM FCF is negative and capex intensity has jumped from ~18% to ~26% of revenue. Traders using FCF yield or DCF will get a much lower value than EPS-multiple users. The bull case requires AWS/AI revenue to inflect hard enough in 2027 to justify the depreciation that is already contracted. Position sizing should reflect that this is a 12–24 month thesis, not a 2-quarter one.

**4. Debt is now a rate-sensitive variable.** $82B issued in twelve months, interest expense doubled to a ~$5B+ annualised run-rate. Further issuance is likely while capex runs at $200B+/yr. Rising long yields are now a **direct** earnings and duration headwind for AMZN in a way they were not in 2023–2025.

**5. The $122.3B private book is a two-sided catalyst.** It is ~11% of assets and roughly the size of total long-term debt. Positive catalysts: IPO/mark-up events at AI holdings force revaluation and could fund capex without more debt. Negative catalyst: a private AI valuation reset produces a large non-cash charge and deferred-tax reversal. Track the "upward/downward price adjustment" footnote each quarter — it is the single most volatile line in the P&L.

**6. Watch the $650B contractual obligation line.** It grew and is now ~1.6 years of total revenue. It signals confidence in AI demand, but converts a demand slowdown into an operating-leverage problem rather than a flexible cost cut. This is the bear-case anchor.

**7. Insider signal is missing, not neutral.** The vendor has no authorized insider archive for AMZN as of 2026-09-30, so no conclusion about management buying or selling can be drawn. Do not treat the absence of reported sales as a positive — source Form 4 data separately before relying on insider sentiment.

**8. What would change the thesis:**
- *Bull confirmation:* AWS re-acceleration disclosed in the Q3 segment table (not in this slice) + capex guide capped near $200B + FCF turning positive in 2027 → justify multiple expansion.
- *Bear confirmation:* operating margin compression below 12% as D&A catches up, another $50B+ debt raise, or a downward revaluation of the private-equity book.

---

## 10. Key fundamental summary table

| Category | Metric | Latest value (period) | Prior / comparison | Signal |
|---|---|---|---|---|
| **Scale** | Net sales (derived) | **$200.61B (Q2-26)** | $167.70B (Q2-25) → **+19.6%** | Strongly positive (accelerating) |
| | Net sales | **$382.13B (H1-26)** | $323.37B (H1-25) → +18.2% | Positive |
| | Annualised revenue run-rate | **~$802B** | — | — |
| **Profitability** | Operating income | **$27.46B (Q2-26)** | $19.17B → **+43.2%** | Strongly positive |
| | Operating margin | **13.7% (Q2-26)** | 11.4% → **+230 bp** | Positive |
| | Operating margin | **13.4% (H1-26)** | 11.6% → +180 bp | Positive |
| | Incremental operating margin | **~24%** | — | Positive |
| **Earnings quality** | Reported diluted EPS | **$5.75 (Q2-26)** | $1.68 → +242% | Distorted |
| | Non-operating income | **$53.40B (Q2-26)** | $1.69B | Flag |
| | Private-equity mark-up in P&L | **$50.49B (Q2-26) / $62.81B (H1-26)** | $0.05B / $0.09B | Major risk |
| | **Core (ex-marks) EPS (est.)** | **~$1.95 (Q2-26)** | ~$1.55–1.60 → **+~23%** | Positive, but slower than headline |
| | Effective tax rate | 22.5% (Q2-26) / 23.0% (H1-26) | 12.8% / 17.0% | Normalising |
| | Cash taxes paid vs tax expense | **$3.98B vs $27.76B (H1-26)** | $5.64B vs $7.23B | Flag (deferred, non-cash) |
| **Cash flow** | Operating cash flow | **$45.39B (Q2-26) / $71.42B (H1-26)** | +39.6% / +44.2% | Strongly positive |
| | OCF, TTM | **$161.40B** | $121.14B prior TTM → +33% | Positive |
| | Capex | **$54.21B (Q2-26) / $98.41B (H1-26)** | +68% / +72% | Risk |
| | Capex / revenue | **27.0% (Q2-26) / 25.8% (H1-26)** | ~17.7% (H1-25) | Major risk |
| | **Free cash flow, TTM** | **−$11.63B** | +$13.48B prior TTM | Negative |
| | Acquisitions (cash) | **$39.77B (H1-26)** | $1.65B (H1-25) | Flag (opaque) |
| **Balance sheet** | Total assets | **$1,095.69B (30-Jun-26)** | $818.04B (31-Dec-25) → **+33.9%** | — |
| | Cash + marketable securities | **$176.11B** | $132.61B → +$43.5B | Strongly positive |
| | Long-term debt | **$133.00B** | $68.84B → **+93.2%** | Risk |
| | Finance lease liabilities | $13.45B | $12.29B | Neutral |
| | Operating lease liabilities | $96.32B | $89.25B | Watch |
| | Net debt ex-operating leases | **−$29.6B (net cash)** | — | Positive |
| | Current ratio | **1.03x** | 1.05x | Neutral/weak |
| | AOCI | **+$66.29B** | +$28.23B → +$38.06B | Volatile |
| | Comprehensive income (H1) | **$130.96B** | Net income $92.90B | Mark-driven |
| **Commitments** | Contractual obligations | **$650.03B** | — | Risk |
| | Due within 12 months | **$78.08B** | — | Watch |
| **Capital returns** | Shares outstanding | 10,783M (30-Jun-26) | 10,731M (31-Dec-25) → +0.5% | No buyback |
| | SBC | $10.07B (H1-26), **−1.5% YoY** | 2.64% of revenue (vs 3.16%) | Positive |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | — | No signal |
| **Valuation** | Price / market cap / multiples | **Not available in dataset** | — | Cannot compute |

---

### Bottom line for the trading desk
AMZN's **operating business is firing on all cylinders** — 19.6% revenue growth, 13.7% operating margins, +43% operating income, +44% operating cash flow, with cost discipline (SBC and G&A down) rather than accounting help. But **the reported earnings are materially inflated by ~$63B of non-cash private-AI marks**, **free cash flow is negative (−$11.6B TTM)**, **capex is 26% of revenue**, and the company has **doubled its long-term debt in six months** to fund it. The correct posture is: **own the operating momentum, discount the headline EPS, and underwrite the capex/depreciation cycle and the mark-to-model equity book explicitly.** The Q3 2026 print in late October — revenue trajectory, margin durability against +30% D&A, and capex/2027 guidance — is the next binary fundamental test.