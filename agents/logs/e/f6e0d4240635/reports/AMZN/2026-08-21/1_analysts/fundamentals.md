# AMZN — Comprehensive Fundamental Report
**As of 2026-08-21 | Latest SEC filing in dataset: Form 10-Q accepted 2026-07-31 (period ended 2026-06-30)**

---

## 1. Data provenance & important caveats

| Item | Status |
|---|---|
| Source | Point-in-time SEC XBRL facts, filtered by actual EDGAR acceptance timestamp (nothing after 2026-08-21) |
| Latest balance-sheet date | 2026-06-30 (10-Q filed 2026-07-31) |
| Prior-period filing in dataset | 10-Q filed 2026-04-30 (period ended 2026-03-31) |
| **Insider transactions** | **DATA_UNAVAILABLE** — no authorized point-in-time insider archive for AMZN exists in the data package. No insider buying/selling is inferred or fabricated in this report. |
| Segment detail | Not disclosed in the extracted fact set (only `NumberOfOperatingSegments = 3` confirmed) |
| Revenue tag | Not returned by the vendor; **revenue is derived as `CostsAndExpenses + OperatingIncomeLoss`**, which is an exact identity for this issuer's P&L format |
| "Annual" statement calls | Returned the same point-in-time fact set as quarterly; hence FY2025/FY2024 figures below are **derived** from TTM arithmetic and flagged as such |

Everything labeled **(derived)** is arithmetic from reported facts, not a vendor estimate. Everything else is reported.

---

## 2. Company profile

**Amazon.com, Inc. (AMZN)** — the world's largest e-commerce and cloud-infrastructure company, operating **three reportable segments** (confirmed: `NumberOfOperatingSegments = 3`):
1. **North America** (retail, marketplace, advertising, Prime)
2. **International** (retail/marketplace ex-North America)
3. **AWS** (cloud compute, storage, database, AI/ML services)

Secondary engines not broken out in the data but visible through margin behavior: **advertising** (high-margin, in-segment), **subscriptions (Prime)**, and an increasingly material **investment portfolio** (equity stakes carried at fair value). Shares outstanding: **10,783.1M** at 2026-06-30; **10,786.3M** at 2026-07-22. Par $0.01; 100B shares authorized. No dividend.

---

## 3. Income statement — the headline is *not* the story

### 3.1 Reported results (USD millions, except EPS)

| Metric | Q2 2026 | Q2 2025 | Δ y/y | Q1 2026 (derived) | Q1 2025 (derived) | Δ y/y |
|---|---|---|---|---|---|---|
| Revenue (derived) | **200,606** | 167,702 | **+19.6%** | 181,519 | 155,667 | +16.6% |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 87,463 | 76,976 | +13.6% |
| Gross profit (derived) | **104,828** | 86,893 | +20.6% | 94,056 | 78,691 | +19.5% |
| Gross margin | **52.3%** | 51.8% | +45 bp | 51.8% | 50.6% | +124 bp |
| Marketing | 11,698 | 11,416 | +2.5% | 10,314 | 9,763 | +5.6% |
| G&A | 2,788 | 2,965 | −6.0% | 2,587 | 2,628 | −1.6% |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 157,667 | 137,262 | +14.9% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** | 23,852 | 18,405 | +29.6% |
| Operating margin | **13.7%** | 11.4% | **+226 bp** | 13.1% | 11.8% | +130 bp |
| Non-operating income | **53,396** | 1,686 | n/m | 15,982 | 3,274 | n/m |
| Pre-tax income | **80,857** | 20,857 | +287.7% | 39,834 | 21,679 | +83.7% |
| Tax expense | 18,199 | 2,678 | — | 9,560 | 4,553 | — |
| Effective tax rate | 22.5% | 12.8% | — | 24.0% | 21.0% | — |
| **Net income** | **62,647** | 18,164 | **+244.9%** | 30,255 | 17,127 | +76.7% |
| **Diluted EPS** | **$5.75** | $1.68 | +242% | $2.78 | $1.59 | +75% |
| Diluted shares (implied) | 10,895M | 10,811M | +0.8% | ~10,887M | ~10,771M | +1.1% |

### 3.2 First-half aggregates

| Metric | H1 2026 | H1 2025 | Δ |
|---|---|---|---|
| Revenue (derived) | **382,125** | 323,369 | **+18.2%** |
| Gross profit | 198,884 | 165,584 | +20.1% |
| Gross margin | 52.0% | 51.2% | +83 bp |
| Operating income | **51,313** | 37,576 | **+36.6%** |
| Operating margin | **13.4%** | 11.6% | +182 bp |
| Non-operating income | 69,378 | 4,960 | n/m |
| Pre-tax income | 120,691 | 42,536 | +183.7% |
| Net income | **92,902** | 35,291 | +163.2% |
| Diluted EPS | **$8.53** | $3.27 | +160.9% |
| Marketing | 22,012 | 21,179 | +3.9% |
| G&A | 5,375 | 5,593 | −3.9% |
| SBC (allocated) | 10,070 | 10,223 | **−1.5%** |
| D&A | 38,933 | 29,489 | +32.0% |
| Interest expense | 2,114 | 1,057 | +100.0% |
| Interest income | 2,430 | 2,151 | +13.0% |
| Cash taxes paid | 3,978 | 5,638 | −29.4% |

### 3.3 ⚠️ Quality of earnings: ~$52B of Q2 pre-tax income was non-cash mark-to-market

This is the single most important analytical point in the dataset.

- **`EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` jumped from $16.2B (2025-12-31) → $122.3B (2026-06-30)** — a **+$106.1B** increase in six months.
- Within that, **`UpwardPriceAdjustment` on those securities = $50,486M in Q2 2026 alone** and **$62,814M in H1 2026** (vs just $49M in Q2 2025). This is a fair-value write-up of unlisted equity holdings (consistent with Amazon's large AI-model-lab stakes) recognized **through the income statement**.
- Other non-core non-operating items in Q2 2026: equity securities FV-NI gain **+$1,300M**, marketable securities gain **+$1,319M**, warrant fair-value change **−$1,449M**.
- Total identifiable investment/mark-to-market swing in Q2 2026 ≈ **+$51.7B pre-tax**; in H1 2026 ≈ **+$62.6B pre-tax**.
- The tax consequence is real and mostly **deferred**: `DeferredIncomeTaxExpenseBenefit` = **$30,489M in H1 2026** ($17,691M in Q2) versus $518M in H1 2025. Cash taxes actually **fell** to $3,978M.

**Reconciling to "core" earnings (derived):**

| Metric | Q2 2026 | Q2 2025 | Δ | H1 2026 | H1 2025 | Δ |
|---|---|---|---|---|---|---|
| Reported diluted EPS | $5.75 | $1.68 | +242% | $8.53 | $3.27 | +161% |
| Less: after-tax investment markups | ~$3.67 | ~$0.02 | — | ~$4.43 | ~$0.02 | — |
| **Core diluted EPS (derived)** | **~$2.08** | ~$1.66 | **+25%** | **~$4.10** | ~$3.25 | **+26%** |
| Reported net income | 62,647 | 18,164 | — | 92,902 | 35,291 | — |
| **Core net income (derived)** | **~22,600** | ~17,950 | **+26%** | **~44,700** | ~35,050 | **+28%** |

**Takeaway:** roughly **64% of Q2 2026 GAAP EPS and ~52% of H1 EPS was non-cash, non-recurring investment revaluation.** Stripping it out, the underlying business still compounded core EPS at a healthy **~25–26% y/y** — but the headline "$5.75, +242%" is *not* a run-rate. Any trader anchoring on GAAP P/E at the Q2 print is mispricing AMZN by a wide margin.

### 3.4 What is genuinely improving

- **Operating leverage is real and accelerating**: revenue +19.6% vs total cost growth +16.6% → +226 bp of operating margin in Q2. Marketing grew only **+2.5%** and **G&A fell −6.0%** while revenue grew ~20% — cost discipline, not just mix.
- **Gross margin 52.3%** (+45 bp y/y) suggests high-margin mix (AWS, ads, third-party services) continues to outgrow 1P retail.
- **SBC discipline**: SBC was **−1.5% y/y in H1** ($10,070M) against +18% revenue, so SBC intensity fell from 3.2% to 2.6% of revenue. Unrecognized future SBC is **$24.8B**. This is a genuine, rare positive for a mega-cap tech in an AI capex cycle.
- **D&A +32% y/y** (TTM $75,200M) confirms the capex is landing in service — but it also means depreciation is now a ~9.9% of revenue drag that will keep growing.

---

## 4. Balance sheet — a $1 trillion asset base and a doubling of debt

### 4.1 Balance sheet (USD millions)

| Line | 2026-06-30 | 2025-12-31 | Δ |
|---|---|---|---|
| Cash & equivalents | 78,213 | 86,810 | −9.9% |
| Marketable (AFS) securities | 97,900 | 45,800 | **+113.8%** |
| **Total liquid assets (derived)** | **176,113** | 132,610 | **+32.8%** |
| Accounts receivable, net | 88,092 | 67,729 | **+30.1%** |
| Inventory, net | 38,184 | 38,325 | −0.4% |
| **Current assets** | **249,264** | 229,083 | +8.8% |
| Equity securities w/o readily determinable FV | **122,300** | 16,200 | **+654.9%** |
| Operating lease ROU asset | 92,743 | 86,054 | +7.8% |
| **Total assets** | **1,095,689** | 818,042 | **+33.9%** |
| Accounts payable | 147,440 | 121,909 | +20.9% |
| Accrued liabilities | 73,406 | 75,520 | −2.8% |
| **Current liabilities** | **241,274** | 218,005 | +10.7% |
| Long-term debt — current portion | 3,330 | 2,748 | +21.2% |
| Long-term debt — non-current | **128,894** | 65,648 | **+96.3%** |
| **Total long-term debt** | **132,995** | 68,836 | **+93.2%** |
| Finance lease liabilities | 13,451 | 12,286 | +9.5% |
| Operating lease liabilities | 96,320 | 89,252 | +7.9% |
| Deferred revenue (current + non-current) | 24,928 | 24,976 | flat |
| Shares outstanding | 10,783M | 10,731M | +0.5% |
| Additional paid-in capital | 149,619 | 140,024 | +6.9% (SBC) |
| AOCI | **66,287** | 28,230 | **+134.8%** |

**Estimated equity and leverage (derived):** Total equity ≈ **$520–530B** (12/31/25 ~$385–390B + H1 net income $92.9B + AOCI +$38.1B + APIC +$9.6B). Book value ≈ **$48.7/share**. Gross debt (L-T debt + finance leases) = **$146.4B** vs liquid assets **$176.1B** → still a **net cash position of ~$30B**. Including operating leases ($96.3B), net obligations ≈ **$67B**. Against a derived TTM EBIT of ~$100B and TTM D&A of $75.2B (EBITDA ≈ **$175B**), gross debt/EBITDA is **~0.84x** and interest coverage ~30x. **Leverage is not a solvency issue — but the *rate of change* is the story.**

### 4.2 Three balance-sheet signals traders must respect

1. **Debt nearly doubled in six months** ($68.8B → $133.0B) while cash fell 10%. The company is **financing the AI build with borrowed money**, not just internal cash flow. Q2 alone added $13.6B of LT debt.
2. **The $106B equity-securities write-up is a two-sided sword.** It inflates book value and equity (~20% of total equity is now an unlisted asset carried at a mark), while creating a **~$30B+ deferred tax liability** and setting up a symmetric downside if private AI valuations compress. This line item is *not* liquid, *not* cash-generative, and *not* controllable by management.
3. **AOCI rose $38.1B in H1 2026** while FX translation was only **−$1.6B** — i.e., ~$40B of the OCI move came from something other than currency (fair-value/hedge-related gains, since the AFS debt book shows only $7M gross unrealized gains and $67M gross losses at 6/30/26). Comprehensive income of $131.0B vs net income of $92.9B in H1 quantifies the gap. Traders should read the 10-Q OCI note before treating book value as clean tangible value.

---

## 5. Cash flow — AMZN is now free-cash-flow negative

### 5.1 Cash flow (USD millions)

| Metric | TTM (Jul'25–Jun'26) | TTM (Jul'24–Jun'25) | Δ | H1 2026 | H1 2025 | Q2 2026 | Q1 2026 |
|---|---|---|---|---|---|---|---|
| Operating cash flow | **161,403** | 121,137 | **+33.2%** | 71,419 | 49,530 | 45,387 | 26,032 |
| Purchases of productive assets (capex) | **(173,028)** | (107,656) | **+60.7%** | (98,411) | (57,202) | (54,208) | (44,203) |
| **Free cash flow (derived)** | **(11,625)** | **+13,481** | **turned negative** | **(26,992)** | (7,672) | **(8,821)** | **(18,171)** |
| Acquisitions, net of cash | (41,956) | (4,809) | **+772%** | (39,767) | (1,652) | (24,359) | (15,408) |
| Net investing cash flow | (216,775) | (123,569) | +75.4% | (143,457) | (69,227) | (79,245) | (64,212) |
| LT debt issued | — | 746 | — | 66,998 | 746 | 13,557 | 53,441 |
| ST debt issued | — | 8,187 | — | 15,386 | 3,908 | 9,368 | 6,018 |
| LT + ST debt repaid | — | (15,335) | — | (18,434) | (6,225) | (12,325) | (2,082) |
| **Net financing cash flow** | **+75,160** | (8,652) | n/m | **+62,913** | (2,586) | +10,146 | +52,767 |
| D&A (non-cash add-back) | 75,200 | 58,562 | +28.4% | 38,933 | 29,489 | 19,988 | 18,945 |
| Cash taxes paid | 6,635 | 11,788 | −43.7% | 3,978 | 5,638 | 2,655 | 1,323 |

### 5.2 Interpretation

- **Capex intensity has crossed into uncharted territory**: Q2 capex **$54.2B = 27.0% of quarterly revenue**; H1 capex/revenue = 25.8%. TTM capex $173.0B is **up 61% y/y** and now **exceeds TTM operating cash flow by $11.6B**.
- **FCF flipped from +$13.5B to −$11.6B on a TTM basis.** This is the first sustained negative-FCF regime for AMZN since the 2021–22 build. It is the cleanest single explanation for why the balance sheet suddenly needs $82B of debt issuance.
- **OCF quality is still high**: OCF grew **+33% y/y**, *faster* than revenue, despite a **$21.4B working-capital drag from receivables/other assets** (AR +30% in six months) and a **$6.1B drag from accrued liabilities**. Cash taxes paid fell 44% — a real cash benefit, but one that is partly a function of the deferred-tax build on investment gains and accelerated depreciation.
- **~$40B of cash M&A in H1 2026** (vs $1.65B in H1 2025) is a step-change in inorganic capital deployment. That, plus capex, plus the equity-securities build, means **H1 2026 saw ~$140B of investing outflow against $71B of operating inflow** — bridged almost entirely by debt.
- Financing was **+$62.9B in H1 2026 vs −$2.6B in H1 2025**: the single largest financing inflow in company history in the dataset. **No buyback is visible** (share count rose 0.5%, consistent with SBC dilution only).

---

## 6. Off-balance-sheet commitments: the $650B number

| Commitment (as of 2026-06-30) | USD millions |
|---|---|
| `ContractualObligation` (total) | **650,034** |
| Due — remainder of fiscal 2026 | 42,752 |
| Due — next twelve months | **78,084** |
| Due — year 2 | 53,406 |
| Due — year 3 | 46,767 |
| Due — year 4 | 42,219 |
| Operating lease payments due (undiscounted) | 116,350 |
| Finance lease payments due (undiscounted) | 16,660 |
| Other commitments (remainder of FY) | 2,145 |

**$650B of contractual obligations with ~$78B due inside twelve months** — roughly 39% of TTM operating cash flow. These are largely purchase/usage commitments (compute, content, logistics, energy) rather than debt. Two competing readings for traders:
- **Bullish**: management is committing capital because it sees contracted AI/cloud demand it cannot otherwise serve; these commitments underwrite future revenue visibility.
- **Bearish**: the obligations create an inflexible cost base exactly as FCF is negative and debt is rising, and they sit outside the "$146B" headline debt figure most screens use.

Context: the prior-quarter 10-Q (2026-04-30) shows the same commitments scaling up quickly (e.g., finance-lease payments due rose from $16,496M at 3/31/26 to $16,660M at 6/30/26; operating-lease payments from $110,135M to $116,350M). The commitment stack is *still growing*.

---

## 7. Multi-year history (derived where noted)

| Period | Revenue (derived) | Operating income | Net income | Diluted EPS | Capex | FCF |
|---|---|---|---|---|---|---|
| FY2024 (actual, memory-anchored; not in dataset) | ~$638B | $68.6B | $59.2B | $5.53 | $77.7B | ~$38B |
| TTM Jun-2025 (derived) | **~$656.8B** | ~$69.0B (derived) | **$70,623M** | ~$6.54 | $107,656M | **+$13,481M** |
| FY2025 (derived from TTM roll) | ~$715–725B (est.) | ~$86B (est.) | **~$77,700M** | **~$7.17** | ~$130B (est.) | slightly positive |
| H1 2026 (reported) | **$382,125M** | **$51,313M** | **$92,902M** | **$8.53** | $98,411M | **−$26,992M** |
| Q2 2026 run-rate (×4) | **~$802B** | ~$110B | n/m (gain-inflated) | n/m | ~$217B | negative |
| TTM Jun-2026 (reported) | — | ~$100B (derived) | **$135,281M** | ~$12.42 | $173,028M | **−$11,625M** |

Derivation chain for FY2025 net income: TTM Jun-2026 ($135,281) = FY2025 − H1 2025 ($35,291) + H1 2026 ($92,902) → **FY2025 ≈ $77,692M**. FY2025 net margin ≈ 10.8% vs FY2024's 9.3%.

**Trajectory summary:** revenue growth re-accelerated from ~11% (2024) to **~18–20% (H1 2026)**; operating margin expanded from 10.8% (2024) to **13.4% (H1 2026)**; net income more than doubled TTM; and capex intensity exploded from ~12% to ~26% of revenue. The business is simultaneously getting **more profitable operationally** and **less cash-generative**.

---

## 8. Insider transactions

**No data available.** The vendor explicitly returned `DATA_UNAVAILABLE` for AMZN insider transactions in the point-in-time window. I will not infer or fabricate insider activity. Notable observable proxy: **share count rose only 0.5% in H1 2026 (10,731M → 10,783M) and APIC rose $9.6B**, consistent with stock-compensation issuance and **no meaningful open-market buyback** — i.e., capital is being directed entirely into capex, M&A, equity stakes, and debt service.

---

## 9. Actionable insights for traders

**1. Re-base your EPS model — the GAAP print is a mirage, but a favorable one to fade.**
Q2 2026 GAAP EPS of $5.75 includes ~$3.67 of after-tax mark-to-market. **Core EPS ≈ $2.08 (+25% y/y)**. H1 core EPS ≈ **$4.10 vs $3.25 (+26%)**. Action: if the stock has re-rated on headline EPS/beat-and-raise optics, that re-rating is vulnerable to a sell-side normalization cycle once models exclude the markup. Conversely, the **core +25% compounding is genuinely strong** and supports the medium-term thesis.

**2. Operating leverage is the strongest fundamental in the dataset — lean into it.**
Revenue +19.6% vs opex +14.2% in Q2; marketing +2.5%; G&A −6.0%; SBC −1.5%; operating margin +226 bp to 13.7%. This is structural (AWS/ads mix + logistics efficiency), not one-off. **Any operating-margin guide of ≥13% for H2 2026 should be treated as conservative.**

**3. Negative FCF is the bear case, and it is now a fact, not a forecast.**
TTM FCF **−$11.6B** (vs +$13.5B a year ago); H1 2026 **−$27.0B**; Q2 capex = **27% of revenue**. Action: watch the *next* 10-Q for (a) whether capex/revenue stops rising, (b) whether OCF growth (+33%) can outrun capex growth (+61%), and (c) the pace of further debt issuance. A capex guide-down would be the single most powerful positive catalyst available; a capex guide-up accompanied by another $20B+ debt raise would be a de-rating trigger.

**4. Reframe valuation on EV/EBIT, not P/E.**
With derived TTM EBIT ≈ $100B, TTM D&A $75.2B, net cash ~$30B (ex-leases), and a GAAP EPS polluted by markups, **EV/EBIT and EV/(EBIT+D&A)** are the only comparables that survive this quarter. P/E on $12.42 TTM GAAP EPS overstates cheapness; P/E on ~$8.00 core TTM EPS is the honest number.

**5. Treat the $122B private-equity-stake book as an embedded option, and size it accordingly.**
$106B of value was added in six months, $50.5B of it in Q2 alone. This is a **levered, illiquid, mark-to-model AI exposure** sitting inside a retail/cloud company. A 25% markdown would be a ~$30B pre-tax hit if it flowed through earnings again (symmetric accounting), plus an unwind of ~$8–9B of the associated deferred tax liability. It cuts both ways and adds a *new, idiosyncratic* source of EPS volatility that did not exist a year ago.

**6. Monitor the $650B commitment stack as a leading demand indicator.**
$78B due within 12 months against $161B TTM OCF leaves ~48% of operating cash flow pre-committed. Rising commitments + rising capex + rising debt = management conviction in AI demand. It is simultaneously the biggest **flexibility risk** if demand disappoints.

**7. Leverage: comfortable, but the trajectory warrants a stop-loss discipline.**
Gross debt $146.4B (<0.9x derived EBITDA), interest coverage ~30x, net cash ex-leases. **Not a credit stress story.** But LT debt +93% in six months and interest expense +100% y/y (Q2 +155%) means the *direction* is now a real variable. Watch the credit-spread/AI-capex narrative linkage — AMZN is increasingly trading as an AI-capex name, not a defensive retail compounder.

**8. Data gaps you should close before trading.**
Segment revenue (AWS vs North America vs International), AWS backlog/RPO, advertising revenue, and management guidance are **absent from this dataset**. Q2 filing dates (10-Q accepted 2026-07-31) suggest the print is ~3 weeks old; the next scheduled fundamental catalyst is the Q3 2026 report. Also obtain insider Form 4 data from an alternate source, since the tool returned none.

**Net fundamental read: high-quality, accelerating core operations funding an extremely aggressive AI-infrastructure and M&A build via new debt, with a GAAP earnings picture materially flattered by private-markup gains and free cash flow temporarily negative. Fundamentally bullish on operating momentum; tactically cautious on the durability of headline EPS and on the FCF/debt trajectory.**

---

## 10. Key points summary

| Category | Metric | Value | Signal |
|---|---|---|---|
| **Growth** | Q2 2026 revenue (derived) | $200.6B, **+19.6% y/y** | 🟢 Re-acceleration |
| | H1 2026 revenue (derived) | $382.1B, +18.2% y/y | 🟢 |
| | Q2 2026 run-rate | ~$802B annualized | 🟢 |
| **Profitability** | Q2 2026 operating income | $27.5B, **+43.2% y/y** | 🟢 Best-in-class leverage |
| | Q2 2026 operating margin | **13.7%** (+226 bp y/y) | 🟢 Structural expansion |
| | H1 2026 gross margin | 52.0% (+83 bp y/y) | 🟢 Mix shift to AWS/ads |
| | Q2 2026 marketing / G&A | +2.5% / **−6.0% y/y** | 🟢 Cost discipline |
| | H1 2026 SBC | $10.1B, **−1.5% y/y** | 🟢 Rare positive |
| **Earnings quality** | Q2 2026 reported EPS | $5.75 (+242%) | 🔴 64% is non-cash markup |
| | Q2 2026 **core EPS (derived)** | **~$2.08 (+25%)** | 🟡 Real but far less dramatic |
| | H1 2026 equity-sec upward adjustment | **$62.8B pre-tax** | 🔴 Non-cash, reversible |
| | Private equity stakes (carrying value) | **$122.3B** (from $16.2B) | 🔴 Illiquid mark-to-model |
| | H1 2026 effective tax rate / cash taxes | 23.0% book / $4.0B cash (−29%) | 🟡 Deferred-tax driven |
| **Cash flow** | TTM operating cash flow | $161.4B (**+33.2% y/y**) | 🟢 |
| | TTM capex | **$173.0B (+60.7% y/y)** | 🔴 |
| | **TTM free cash flow (derived)** | **−$11.6B** (vs +$13.5B PY) | 🔴 Regime change |
| | H1 2026 FCF / Q2 capex intensity | −$27.0B / **27.0% of revenue** | 🔴 |
| **Balance sheet** | Total assets | **$1,095.7B** (+33.9% in 6 mo) | 🟡 |
| | Total long-term debt | **$133.0B (+93.2% in 6 mo)** | 🟡 Watch trajectory |
| | Liquid assets (cash + AFS) | $176.1B (+32.8%) | 🟢 Net cash ~$30B |
| | Operating + finance lease liabilities | $109.8B | 🟡 |
| | Gross debt / derived TTM EBITDA | **~0.84x** | 🟢 Low absolute leverage |
| | Interest expense | Q2 +155% y/y; H1 +100% y/y | 🟡 Rising fast off low base |
| **Capital allocation** | H1 2026 cash M&A | **$39.8B** (vs $1.65B PY) | 🟡 Step-change, integration risk |
| | H1 2026 net financing inflow | **+$62.9B** (vs −$2.6B PY) | 🔴 Debt-funded build |
| | Share count / buyback | 10,783M, +0.5% in H1; **no buyback visible** | 🟡 SBC dilution only |
| | Shares outstanding (2026-07-22) | 10,786.3M | — |
| **Commitments** | Total contractual obligations | **$650.0B**; **$78.1B due <12 mo** | 🟡 Conviction vs flexibility |
| **Equity** | Est. book value / BVPS (derived) | ~$525B / **~$48.7** | 🟡 ~20% is private marks |
| | AOCI | **$66.3B** (from $28.2B); FX only −$1.6B | 🟡 ~$40B non-FX OCI |
| **Insider activity** | Any insider buys/sells | **DATA UNAVAILABLE — not inferred** | ⚪ No read |
| **Segments** | Reported segments | 3 (N. America, International, AWS) | ⚪ No segment detail in dataset |
| **Overall fundamental read** | | Accelerating core ops + record capex + negative FCF + flattered GAAP EPS | **Bullish operations / tactically cautious on headline EPS & FCF-debt trajectory** |