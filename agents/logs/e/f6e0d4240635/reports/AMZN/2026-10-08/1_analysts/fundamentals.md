# AMZN — Fundamental Deep Dive
**As of 2026-10-08 | Latest reported period: Q2 FY2026 (quarter ended 2026-06-30) | Source: SEC 10-Q filed 2026-07-31, point-in-time filtered**

---

## 1. Scope, Data Provenance & Caveats (read first)

| Item | Detail |
|---|---|
| Entity | Amazon.com, Inc. (`AMZN`) — resolved identity confirmed |
| Latest fundamental filing | Form 10-Q, accession 0001018724-26-000026, **accepted 2026-07-31 02:11 UTC** |
| Period covered | Q2 2026 and six months ended 2026-06-30; prior-year comparatives (Q2/H1 2025) |
| New filings in trailing week | **None.** The most recent acceptance timestamp in the cache is 2026-07-31. There is no fresh 8-K/10-Q/Form 4 data in the 2026-10-01 → 2026-10-08 window. |
| Insider transactions | **DATA UNAVAILABLE** — the vendor has no authorized, point-in-time insider-transaction archive for AMZN as of 2026-10-08. No inference or fabrication of insider activity is made in this report. |
| Price / valuation data | **Not provided by the toolset.** No P/E, EV/EBITDA, P/FCF or market-cap multiples can be computed. All analysis below is statement-based. |
| Revenue line | The `Revenues` tag was **not present** in the retrieved cache. Revenue is therefore **derived as `OperatingIncomeLoss + CostsAndExpenses`**, which is arithmetically exact for this filing. Derived figures are flagged **(D)**. |
| Frequency note | The vendor returned the same 10-Q fact set for annual and quarterly requests; no full-year 10-K series (FY2023–FY2025) was supplied. Historical depth is limited to TTM/Q2-2025 comparatives. |

> **Bottom line up front:** AMZN's *operating* business is accelerating — Q2 2026 revenue grew ~19.6% y/y with operating margin expanding ~226 bps to 13.7%, and operating cash flow rose 40% y/y. But **headline EPS ($5.75) is roughly 2.7x "core" EPS (~$2.16)** because ~$50.5B of Q2 pre-tax income came from non-cash upward revaluations of non-marketable equity securities. Simultaneously, capex has gone vertical ($54.2B in one quarter), TTM free cash flow has turned **negative (~-$11.6B)**, and total debt has nearly doubled in six months to $133.0B. The equity story is now a three-way tug-of-war between AI-driven operating leverage, an enormous mark-to-market asset, and a capital-intensity/debt cycle.

---

## 2. Company Profile (structural facts from the filing)

- **Name:** Amazon.com, Inc. (`AMZN`), Delaware corporation, SEC CIK 0001018724.
- **Reporting structure:** The 10-Q discloses **3 operating segments** (`NumberOfOperatingSegments = 3`) — consistent with **North America, International, and Amazon Web Services (AWS)**.
- **Business model:** Online and physical retail, third-party marketplace, Prime subscription, advertising, AWS cloud/compute, logistics/fulfillment, devices, and a large portfolio of equity investments (including non-marketable, fair-valued positions).
- **Share base:** 10,783M shares outstanding at 2026-06-30 (10,731M at 2025-12-31); **10,786.3M at 2026-07-22**. Authorized 100,000M shares, $0.01 par. Diluted count implied by Q2 EPS ≈ **10,895M**.
- **Dividends:** No dividend line items appear in the cash-flow tags; capital return is via share issuance/repurchase mechanics only. Debt issuance is the dominant financing flow.
- **Fiscal year:** Calendar year (Dec-31).

---

## 3. Income Statement — Q2 FY2026 vs Q2 FY2025

| $ millions | Q2 2026 | Q2 2025 | Δ y/y |
|---|---:|---:|---:|
| Revenue **(D)** | **200,606** | 167,702 | **+19.6%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% |
| **Gross profit (D)** | **104,828** | 86,893 | **+20.6%** |
| Gross margin | **52.26%** | 51.81% | +45 bps |
| Total costs & expenses | 173,145 | 148,531 | +16.6% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** |
| **Operating margin** | **13.69%** | 11.43% | **+226 bps** |
| Interest income | 1,295 | 1,085 | +19.4% |
| Interest expense | (1,314) | (516) | **+154.7%** |
| Non-operating income, net | **53,396** | 1,686 | n.m. |
| Pre-tax income | **80,857** | 20,857 | +287.7% |
| Income tax | 18,199 | 2,678 | +579.6% |
| Effective tax rate | **22.51%** | 12.84% | +967 bps |
| **Net income** | **62,647** | 18,164 | **+244.9%** |
| Net margin | **31.23%** | 10.83% | +2,040 bps |
| Diluted EPS | **$5.75** | $1.68 | **+242.3%** |
| Basic EPS | $5.82 | $1.71 | +240.4% |

### H1 FY2026 vs H1 FY2025

| $ millions | H1 2026 | H1 2025 | Δ y/y |
|---|---:|---:|---:|
| Revenue **(D)** | **382,125** | 323,369 | **+18.2%** |
| Cost of goods & services | 183,241 | 157,785 | +16.1% |
| Gross margin | **52.05%** | 51.21% | +84 bps |
| Total costs & expenses | 330,812 | 285,793 | +15.8% |
| **Operating income** | **51,313** | 37,576 | **+36.6%** |
| **Operating margin** | **13.43%** | 11.62% | **+181 bps** |
| Non-operating income, net | **69,378** | 4,960 | n.m. |
| Pre-tax income | **120,691** | 42,536 | +183.7% |
| Income tax | 27,759 | 7,231 | +283.9% |
| Effective tax rate | **23.00%** | 17.00% | +600 bps |
| **Net income** | **92,902** | 35,291 | **+163.2%** |
| Diluted EPS | **$8.53** | $3.27 | **+160.9%** |
| Diluted shares (implied) | ~10,895M | ~10,794M | +0.9% |

**Derived quarterly bridge (D):**

| $ millions | Q1 2026 | Q2 2026 | Q1 2025 | Q2 2025 |
|---|---:|---:|---:|---:|
| Revenue | 181,519 | 200,606 | 155,667 | 167,702 |
| Operating income | 23,852 | 27,461 | 18,405 | 19,171 |
| Net income | 30,255 | 62,647 | 17,127 | 18,164 |

**Key read-throughs:**
- **Revenue accelerated** from +16.6% in Q1 to +19.6% in Q2 — a ~300 bp sequential acceleration, unusually strong for a company of this size.
- **Operating leverage is real:** total costs grew 16.6% vs revenue +19.6%. Q2 gross margin +45 bps, operating margin +226 bps. H1 opex ex-COGS grew only **+15.3%** ($147.6B vs $128.0B).
- **Marketing discipline:** Q2 marketing $11.698B vs $11.416B (+2.5%); H1 +3.9%. G&A actually *fell* 3.9% in H1 ($5.375B vs $5.593B).
- **Tax rate normalization** is a real headwind: 22.5% in Q2 vs 12.8% a year ago; 23.0% vs 17.0% in H1. This alone removes several billion of net income versus a naïve extrapolation.
- **Interest expense more than doubled** (Q2 +155%), a direct consequence of the debt-funded buildout (Section 6).

---

## 4. Earnings Quality — the $63 Billion Question

This is the single most important analytical adjustment in the report.

| $ millions | H1 2026 | Q2 2026 | Q1 2026 (D) |
|---|---:|---:|---:|
| Upward price adjustment, equity securities w/o readily determinable FV | **62,814** | **50,486** | 12,328 |
| Equity securities FV-NI gain | 454 | 1,300 | (846) |
| Warrant fair-value adjustment | (1,051) | (1,449) | 398 |
| Non-operating income, net (reported) | 69,378 | 53,396 | 15,982 |
| **Non-operating income ex-upward-revaluation** | **6,564** | **2,910** | 3,654 |
| **Pre-tax income ex-upward-revaluation (D)** | **57,877** | **30,371** | 27,506 |
| **Core net income @ ~23%/22.5% tax (D)** | **~44,570** | **~23,534** | ~21,036 |
| **Core diluted EPS (D)** | **~$4.09** | **~$2.16** | ~$1.93 |

- The carrying value of **equity securities without readily determinable fair value exploded from $16.2B (2025-12-31) to $122.3B (2026-06-30)** — a **+$106.1B** balance-sheet increase, of which **$62.8B was recognized through the income statement** in H1. This is almost certainly a large private AI/technology stake (directionally consistent with Amazon's Anthropic position), marked up on a new financing round.
- **It is non-cash, non-recurring, and reversible.** A future down-round would flow through the same line as a loss. There is no cash-flow support for it in operating activities.
- **Stripping it out, Q2 core EPS ≈ $2.16 vs $1.68 reported a year ago (+29%)**, and H1 core EPS ≈ $4.09 vs $3.27 (+25%). That is still excellent — but it is roughly **one-third of the headline growth rate** the tape will initially print.
- Watch the **`EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment`** line every quarter: it is now the swing factor in AMZN's GAAP EPS, larger than quarterly operating income.

---

## 5. Cash Flow — strong operations, historic capex, negative FCF

### Q2 and H1

| $ millions | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---:|---:|---:|---:|
| Operating cash flow | **45,387** | 32,515 | **71,419** | 49,530 |
| Capex (productive assets) | **(54,208)** | (32,183) | **(98,411)** | (57,202) |
| **Free cash flow (D)** | **(8,821)** | **+332** | **(26,992)** | **(7,672)** |
| Business acquisitions, net | (24,359) | (1,700) | **(39,767)** | (1,652) |
| Net purchases of marketable securities | (1,810) | (6,356) | (7,380) | (11,952) |
| Investing cash flow | (79,245) | (39,424) | (143,457) | (69,227) |
| Financing cash flow | +10,146 | (2,539) | **+62,913** | (2,586) |
| D&A | 19,988 | 15,227 | 38,933 | 29,489 |
| Share-based comp | 6,038 | 6,534 | 10,070 | 10,223 |
| Taxes paid, net | 2,655 | 4,761 | 3,978 | 5,638 |

### Trailing-twelve-month (2025-07-01 → 2026-06-30) vs prior TTM

| $ millions | TTM Jun-2026 | TTM Jun-2025 | Δ |
|---|---:|---:|---:|
| Operating cash flow | **161,403** | 121,137 | **+33.2%** |
| Capex | **173,028** | 107,656 | **+60.7%** |
| **Free cash flow (D)** | **(11,625)** | **+13,481** | **swing of -$25.1B** |
| D&A | 75,200 | 58,562 | +28.4% |
| Net income | 135,281 | 70,623 | +91.6% |

**Interpretation:**
- **Operating cash flow is the strongest line in the entire report** (+33% TTM, +44% H1, +40% Q2). The core franchise is generating cash faster than ever.
- **Capex intensity is extreme:** Q2 capex was **27.0% of revenue** (vs 19.2% a year ago); H1 was **25.8%** (vs 17.7%). TTM capex of $173.0B exceeds TTM OCF by $11.6B.
- **FCF has flipped negative on a TTM basis** for the first time in the modern Amazon era. Q2 alone was -$8.8B; H1 -$27.0B.
- **Acquisitions added another $39.8B** of cash outflow in H1 ($24.4B in Q2 alone) — a step-change from ~$1.7B in the prior-year period. This is incremental to capex and is a key unexplained use of cash that warrants scrutiny in the 10-Q footnotes.
- **SBC is flat** (~$10.1B H1 vs $10.2B) and now only ~5.3% of OCF — a meaningful quality improvement versus prior years. Unrecognized future SBC is **$24.8B**.
- **Cash taxes fell** to $3.98B H1 despite pre-tax income nearly tripling — the gap between book tax expense ($27.8B) and cash taxes is driven by **deferred tax of $30.5B H1**, largely the non-cash equity revaluation. Cash tax conversion remains favorable.

---

## 6. Balance Sheet — liquidity is ample, but leverage is rising fast

| $ millions | 2026-06-30 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 78,213 | 86,810 | (8,597) |
| Available-for-sale debt securities | **97,900** | 45,800 | **+52,100** |
| **Total cash + marketable securities (D)** | **176,113** | 132,610 | **+43,503** |
| Accounts receivable, net | 88,092 | 67,729 | +20,363 |
| Inventory, net | 38,184 | 38,325 | (141) |
| Current assets | 249,264 | 229,083 | +20,181 |
| Total assets | **1,095,689** | 818,042 | **+277,647** |
| Accounts payable | 147,440 | 121,909 | +25,531 |
| Accrued liabilities | 73,406 | 75,520 | (2,114) |
| Current liabilities | 241,274 | 218,005 | +23,269 |
| Long-term debt (current) | 3,330 | 2,748 | +582 |
| Long-term debt (noncurrent) | 128,894 | 65,648 | +63,246 |
| **Total debt (D)** | **132,995** | **68,836** | **+64,159 (+93.2%)** |
| Operating lease liability (total) | 96,320 | 89,252 | +7,068 |
| Finance lease liability (total) | 13,451 | 12,286 | +1,165 |
| Contract liabilities (deferred revenue) | 24,928 | 25,000 | (72) |
| Equity securities w/o readily determinable FV | **122,300** | 16,200 | **+106,100** |
| Accumulated OCI | **66,287** | 28,230 | **+38,057** |
| Additional paid-in capital | 149,619 | 140,024 | +9,595 |

**Liquidity & leverage metrics (D, analyst-computed):**

| Metric | 2026-06-30 |
|---|---:|
| Current ratio | **1.03x** (vs 1.05x at 12/31/25) |
| Working capital | $7.99B (vs $11.08B) |
| Cash + securities / current liabilities | **0.73x** |
| Net debt ex-leases | **–$43.1B (net cash)** |
| Net debt incl. op+finance leases | **+$66.7B** |
| Total debt / annualized H1 EBITDA (~$180.5B) | **0.74x** |
| Total debt + leases / EBITDA | **~1.35x** |
| H1 interest coverage (EBIT/interest) | **24.3x** (Q2: 20.9x) |
| Contractual obligations (total) | **$650.0B**; $78.1B due <12 months |

**Interpretation:**
- Amazon is **still net-cash excluding leases**, and 24x interest coverage is investment-grade comfortable. This is not a solvency story.
- But the **direction of travel is unambiguous**: debt +93% in six months, $82B of LT debt issued TTM, $20.8B of ST debt issued TTM, and interest expense now running at a **~$5.3B annualized** pace (Q2 $1.314B × 4) versus ~$2.1B in H1 2025. Each 100 bps of refinancing cost now matters at a scale it did not a year ago.
- **The asset side is doing the heavy lifting:** +$106.1B of private equity securities and +$52.1B of AFS securities explain most of the $277.6B asset growth, alongside ~$59B of net PP&E from capex and ~$40B of acquisitions.
- **AOCI +$38.1B in six months** materially boosts book value, but ~$41.4B of Q2 other comprehensive income is *also* non-cash and market-dependent. Reported book value is now highly sensitive to mark-to-market swings in both the OCI and earnings lines.
- **Supplier financing remains a core strength:** AP +$25.5B (+21%) versus inventory flat. Payables are funding the working-capital cycle.

---

## 7. Operating Efficiency & Working Capital (H1 2026, 181 days)

| Metric | H1 2026 | Comment |
|---|---:|---|
| Days inventory outstanding (DIO) | **~37.7 days** | Inventory flat y/y despite +18% revenue |
| Days sales outstanding (DSO) | **~41.7 days** | AR +30% y/y, faster than revenue — monitor |
| Days payable outstanding (DPO) | **~145.6 days** | Extended supplier terms; +$25.5B AP |
| **Cash conversion cycle** | **~–66.2 days** | Best-in-class negative CCC |
| Inventory turns (annualized) | **~9.6x** | Disciplined |
| Capex / revenue | **25.8%** | vs 17.7% prior year |
| FCF margin | **–7.1%** | vs –2.4% prior year |
| Operating margin | **13.4%** | vs 11.6% prior year |

The **negative ~66-day cash conversion cycle is the engine** that lets Amazon run negative FCF while still growing OCF 33%. But note AR growing faster than revenue (+30% vs +18%) — a mild yellow flag on receivables quality, with the allowance for doubtful accounts up to $2.8B from $2.4B.

---

## 8. AOCI, Deferred Revenue & Other Balance-Sheet Signals

- **Deferred revenue / contract liabilities:** $24.9B total ($20.4B current + $4.5B non-current), roughly flat since year-end. **$15.2B of revenue was recognized in H1 from beginning deferred balances** — healthy backlog conversion but no sequential growth in the liability, suggesting subscription/Prime growth is being recognized as fast as it is billed.
- **Operating leases:** total liability $96.3B; undiscounted payments $116.4B; weighted-average discount rate **3.9%** (up from 3.7%). $15.5B of operating lease payments in TTM. Lease commitments are a real, growing fixed cost.
- **Pension/OPEB, goodwill, PP&E, retained earnings, and total stockholders' equity** were not included in the returned fact set (the alphabetical cache truncates at "FinanceLease"); total equity cannot be computed exactly and is deliberately **not estimated** here. Known equity components are APIC $149.6B, common stock $0.113B, and AOCI $66.3B.
- **Derivative book is tiny** ($705M assets / $133M liabilities) and not a risk factor. Energy hedges notional 270,000 MWh H1.

---

## 9. Insider Transactions

**No data available.** The provider returned:

> `DATA_UNAVAILABLE: the B-project data package has no authorized, point-in-time insider-transactions archive for AMZN by 2026-10-08. Do not infer or fabricate insider activity.`

Accordingly, **no conclusion about insider buying or selling is offered.** Traders should source Form 4 data independently before assigning any signal here.

---

## 10. Actionable Insights for Traders

### The bullish case (evidence-based)
1. **Revenue re-accelerated to +19.6% y/y in Q2** (+16.6% in Q1) — the strongest growth implied by this dataset, with operating margin expanding 226 bps.
2. **Operating leverage is broad-based:** gross margin +45 bps, marketing +2.5%, G&A –3.9%. Incremental revenue is dropping to operating income at a very high rate.
3. **OCF +33% TTM / +44% H1** — the cash-generating core is stronger than at any prior point in the supplied history.
4. **Negative ~66-day cash conversion cycle** and +$25.5B of payables fund the buildout internally.
5. **Net cash ex-leases (–$43B net debt)** and 24x interest coverage — balance-sheet risk is low despite the debt surge.
6. **$122.3B of private equity holdings** ($106.1B increase in six months) is a large, under-appreciated sum-of-the-parts asset. Even if the $62.8B H1 markup is non-cash, the *carrying value* is now ~11% of total assets.

### The bearish/quality case
1. **Headline EPS overstates core earnings by ~2.7x in Q2.** GAAP diluted EPS $5.75 vs core ~$2.16. If the tape prices the headline print at face value, expect a violent re-rating when the composition is understood — or on any future mark-down.
2. **TTM FCF is –$11.6B**, a ~$25.1B deterioration y/y. Capex is 27% of revenue in Q2. The market's willingness to capitalize $173B of annual capex is the key swing factor.
3. **Debt +93% in six months to $133.0B**, interest expense +155% y/y, ST debt issuance $20.8B TTM. Refinancing risk is rising from a low base.
4. **$39.8B of H1 acquisitions** ($24.4B in Q2) is a large, opaque cash use that is *not* capex — verify in the 10-Q footnotes what was bought and at what multiple.
5. **Tax rate normalization** (22.5% vs 12.8% in Q2) removes a tailwind that flattered 2025 comparatives.
6. **AOCI +$38B and private-equity marks** mean reported book value and EPS are now unusually sensitive to private-market and rate conditions. This is a lower-quality, higher-beta earnings stream than a pure retail/AWS story.

### Concrete monitoring triggers for the next quarter (Q3 FY2026 report, expected late October 2026)
| Trigger | Bullish threshold | Bearish threshold |
|---|---|---|
| Revenue growth y/y | ≥ +19% | < +15% |
| Operating margin | ≥ 13.5% | < 12.0% |
| Capex (quarterly) | ≤ $50B | > $60B |
| TTM FCF | Turning back positive | Worse than –$20B |
| Interest expense (quarterly) | ≤ $1.4B | > $1.8B |
| Upward equity revaluation line | Absent but core EPS ≥ $2.30 | **Any write-down / impairment** |
| Total debt | Stable or declining | > $145B |
| AR growth vs revenue growth | AR ≤ revenue growth | AR > revenue +10 pts |

### Positioning implications
- **Model core EPS, not GAAP.** Build Q3 off the ~13.4% operating margin and ~23% tax rate, then add mark-to-market separately. Consensus that anchors on the $5.75 print will be wildly wrong in either direction.
- **The stock is now a capex-cycle story.** The single highest-information item in the next filing is capex guidance and whether AWS revenue growth justifies it. Operating cash flow growth is necessary but no longer sufficient.
- **Watch the private-equity mark as a risk factor, not just a benefit.** A $122.3B asset marked through earnings creates a mechanically large downside EPS tail in a risk-off private-market environment.
- **Credit is not the trade yet, but it is the tail risk.** Debt/EBITDA of ~0.7x (ex-leases) is fine; the pace (+93% in six months) is what would eventually compress the multiple if capex doesn't convert to FCF within 4–6 quarters.
- **No insider signal available** — do not assume management conviction either way from this dataset.

---

## 11. Key Points Summary

| Category | Metric | Value | Signal |
|---|---|---|---|
| **Latest filing** | 10-Q accepted | 2026-07-31 | No new data in trailing week |
| **Scale** | Total assets | $1,095.7B | +$277.6B in 6 months |
| **Growth** | Q2 revenue **(D)** | $200.6B, +19.6% y/y | **Accelerating** (Q1 +16.6%) |
| **Growth** | H1 revenue **(D)** | $382.1B, +18.2% y/y | Strong |
| **Profitability** | Q2 operating income / margin | $27.5B / **13.69%** | +226 bps y/y — bullish |
| **Profitability** | H1 operating income / margin | $51.3B / 13.43% | +181 bps y/y |
| **Earnings quality** | Q2 non-operating income | $53.4B, incl. **$50.5B equity revaluation** | **Low quality / non-cash** |
| **Earnings quality** | Q2 GAAP EPS vs core EPS **(D)** | **$5.75 vs ~$2.16** | Headline overstates ~2.7x |
| **Earnings quality** | H1 GAAP EPS vs core EPS **(D)** | **$8.53 vs ~$4.09** | Core still +25% y/y |
| **Tax** | Q2 / H1 effective rate | 22.5% / 23.0% | vs 12.8% / 17.0% — headwind |
| **Cash generation** | TTM operating cash flow | **$161.4B, +33.2%** | Best line in the report |
| **Capital intensity** | Q2 capex / revenue | **27.0%** ($54.2B) | Extreme; vs 19.2% prior yr |
| **Free cash flow** | TTM FCF **(D)** | **–$11.6B** (vs +$13.5B) | **Key bear point** |
| **Free cash flow** | H1 FCF **(D)** | –$27.0B | vs –$7.7B prior yr |
| **M&A** | H1 acquisitions, net | $39.8B ($24.4B in Q2) | Large, must be verified |
| **Liquidity** | Cash + AFS securities | **$176.1B** | Ample |
| **Leverage** | Total debt | **$133.0B, +93.2% in 6M** | Rising fast from low base |
| **Leverage** | Net debt ex-leases | **–$43.1B (net cash)** | Still comfortable |
| **Leverage** | Debt / annualized EBITDA **(D)** | ~0.74x (ex-leases); ~1.35x incl. leases | Manageable |
| **Coverage** | H1 EBIT / interest | 24.3x | Strong, but interest +155% y/y |
| **Working capital** | Cash conversion cycle **(D)** | **–66.2 days** | Best-in-class |
| **Liquidity ratio** | Current ratio | 1.03x (from 1.05x) | Slight tightening |
| **Hidden asset** | Equity securities w/o readily determinable FV | **$122.3B** (from $16.2B) | ~11% of assets; illiquid, mark-to-market |
| **Book value** | AOCI | $66.3B (from $28.2B) | +$38.1B non-cash |
| **Compensation** | H1 SBC | $10.07B (flat y/y) | Improving quality; $24.8B unrecognized |
| **Deferred revenue** | Contract liabilities | $24.9B, flat | $15.2B recognized in H1 |
| **Segments** | Operating segments | 3 | NA / International / AWS (inferred) |
| **Shares** | Outstanding | 10,783M (10,786.3M at 7/22/26) | +0.5% YTD dilution |
| **Dividend** | — | None | — |
| **Insider activity** | — | **Data unavailable** | No signal; do not infer |
| **Valuation** | — | **Not computable** | No price data in toolset |

### One-paragraph verdict
AMZN enters Q3 2026 with the **best operating momentum in the supplied dataset** — 19.6% revenue growth, 13.7% operating margin, 33% TTM OCF growth, a negative 66-day cash cycle, $176B of liquid assets and net cash excluding leases. Against that, the company is running a **$173B annualized capex program that has pushed TTM FCF to –$11.6B**, has **nearly doubled debt to $133B in six months**, and is reporting **GAAP EPS that is ~2.7x core EPS** because of a $62.8B non-cash private-equity markup. The trade is therefore not "is Amazon growing" — it clearly is — but **whether the market correctly discounts the earnings mix and tolerates a multi-quarter negative-FCF capex cycle.** Position sizing should reflect that the next print's headline EPS is likely to look spectacular while the cash-flow and debt lines look strained; the fundamental trigger to watch is capex discipline versus AWS/AI revenue conversion.