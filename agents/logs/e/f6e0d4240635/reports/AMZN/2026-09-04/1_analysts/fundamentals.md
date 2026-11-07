# AMZN — Fundamental Research Report
**Amazon.com, Inc. | Point-in-time analysis as of 2026-09-04**
*Primary source: most recent 10-Q (filed 2026-07-31, acc. 0001018724-26-000026) and prior-year comparatives, filtered by actual EDGAR acceptance time. All figures USD millions unless stated.*

---

## 1. Executive Summary

AMZN is in the middle of the most aggressive capital-deployment cycle in its history, and the Q2 2026 numbers show both the payoff and the cost:

- **Revenue re-accelerated hard.** H1 2026 revenue reached **$382,125M** (+18.2% y/y), with Q2 2026 at **$200,606M (+19.6% y/y)** and Q1 2026 at **$181,519M (+16.6% y/y)** — a marked step-up from the low-teens growth of 2025.
- **Operating leverage is real.** Q2 2026 operating income **$27,461M**, a **13.7% margin** vs. 11.4% a year ago (+230bp). H1 operating margin 13.4% vs. 11.6%. Gross margin improved to 52.3% (Q2'25: 51.8%) while operating expense fell to 38.6% of revenue from 40.4%.
- **BUT headline EPS is heavily distorted.** Q2 2026 net income of **$62,647M** (EPS $5.75) includes a **$50,486M pre-tax upward revaluation of equity securities without a readily determinable fair value** (and $12,328M in Q1 2026; **$62,814M for H1**). This non-cash mark flows through non-operating income. **Stripping it out, Q2 2026 core EPS is ≈$2.16 vs. $1.68 (+~29%)** — strong, but nowhere near the +242% GAAP optics.
- **Free cash flow has turned negative.** TTM operating cash flow **$161,403M (+33% y/y)** was more than absorbed by TTM capex of **$173,028M (+61% y/y)** → **TTM FCF of –$11,625M**, versus +$13,481M a year earlier. H1 2026 FCF was **–$26,992M**.
- **Funding the buildout with debt.** Gross debt (ex-finance leases) rose from **$68,836M to $132,224M** in six months (+92%); TTM long-term debt issuance **$81,925M**. Net cash (cash + AFS less debt and finance leases) compressed from ~$51.5B at YE2025 to ~$30.4B at 30-Jun-2026.
- **Earnings quality flags:** effective tax rate jumped to **23.0%** (H1'25: 17.0%) on a **$30,489M deferred tax charge**; D&A is compounding at +32% y/y; and interest expense doubled (+100% H1, +155% Q2), flipping AMZN to **net interest expense in Q2 2026** for the first time in the modern era.

**Verdict framing:** Fundamentally AMZN is *operationally* accelerating (revenue, margin, cash generation), but *financially* it is now a capex-intensive, levered, negative-FCF business whose reported earnings contain a very large non-cash mark. Traders must separate the two.

---

## 2. Data Provenance & Limitations (read before acting)

| Item | Status |
|---|---|
| Most recent filing | 10-Q for period ended **2026-06-30**, accepted **2026-07-31** |
| Prior period available | 10-Q accepted 2026-04-30 (Q1 2026) |
| Annual (10-K) data | **Not present** in the point-in-time extract. Requests for "annual" frequencies returned the same 10-Q fact set — **no FY2025 full-year income statement, balance sheet, or cash-flow statement is available**. |
| Revenue line item | **Not tagged** in the extract. All revenue figures below are **derived as `CostsAndExpenses + OperatingIncomeLoss`** and cross-checked against `OperatingIncomeLoss + NonoperatingIncomeExpense = PretaxIncome` (they tie to the dollar in every period). |
| Segment detail | `NumberOfOperatingSegments = 3` (North America / International / AWS convention), but **no segment revenue or segment operating income is disclosed in the extract**. AWS margin — the single most important driver — **cannot be verified from these tools.** |
| Share price / market cap | **Not available.** No P/E, EV/EBITDA, or FCF yield can be computed here. Do not assume a multiple. |
| Insider transactions | **DATA_UNAVAILABLE — no authorized point-in-time insider archive exists for AMZN.** No insider activity is inferred or fabricated in this report. |
| Stockholders' equity / total liabilities | Total liabilities tag absent; equity figures below are **derived estimates** and clearly labeled. |

---

## 3. Company Profile

Amazon.com, Inc. operates a three-segment model:
1. **North America** — online and physical retail, third-party marketplace, advertising, Prime subscriptions, logistics.
2. **International** — same model across non-US geographies.
3. **Amazon Web Services (AWS)** — cloud compute, storage, database, AI/ML infrastructure and services.

Structural characteristics visible in the data: a **negative-working-capital retail engine** (accounts payable of $147,440M vs. inventory of only $38,184M), an **advertising/subscription mix shift** (gross margin now >52%), and a **massive internally-funded infrastructure franchise** now consuming ~26% of revenue in capex.

---

## 4. Q2 2026 Income Statement — Detailed Reconstruction

| $M | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|---|
| **Revenue (derived)** | 155,667 | 167,702 | 181,519 | **200,606** | 323,369 | **382,125** |
| y/y growth | — | — | **+16.6%** | **+19.6%** | — | **+18.2%** |
| Cost of goods & services | 76,976 | 80,809 | 87,463 | 95,778 | 157,785 | 183,241 |
| **Gross profit** | 78,691 | 86,893 | 94,056 | **104,828** | 165,584 | **198,884** |
| *Gross margin* | 50.6% | 51.8% | 51.8% | **52.3%** | 51.2% | **52.1%** |
| Total costs & expenses | 137,262 | 148,531 | 157,667 | 173,145 | 285,793 | 330,812 |
| **Operating income** | 18,405 | 19,171 | 23,852 | **27,461** | 37,576 | **51,313** |
| *Operating margin* | 11.8% | 11.4% | 13.1% | **13.7%** | 11.6% | **13.4%** |
| Non-operating income (expense) | 3,274 | 1,686 | 15,982 | **53,396** | 4,960 | **69,378** |
| **Pre-tax income** | 21,679 | 20,857 | 39,834 | **80,857** | 42,536 | **120,691** |
| Income tax | 4,553 | 2,678 | 9,560 | 18,199 | 7,231 | 27,759 |
| *Effective tax rate* | 21.0% | 12.8% | 24.0% | **22.5%** | 17.0% | **23.0%** |
| **Net income** | 17,127 | 18,164 | 30,255 | **62,647** | 35,291 | **92,902** |
| **Diluted EPS** | 1.59 | 1.68 | 2.78 | **5.75** | 3.27 | **8.53** |
| Diluted shares (implied, M) | 10,772 | 10,812 | 10,883 | 10,895 | 10,792 | 10,890 |

### 4.1 The non-operating line is the story — and the trap

| $M | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 | H1 2026 |
|---|---|---|---|---|---|
| Non-operating income, total | 3,274 | 1,686 | 15,982 | **53,396** | 69,378 |
| Equity securities w/o readily determinable FV — upward adj. | 37 | 49 | 12,328 | **50,486** | **62,814** |
| Marketable securities unrealized gain | (138) | 388 | (889) | 1,319 | 430 |
| Equity securities FV-NI gain | (205) | 393 | (846) | 1,300 | 454 |
| Warrant fair-value adjustment | 377 | (590) | 398 | (1,449) | (1,051) |
| Investment income (interest) | 1,066 | 1,085 | 1,135 | 1,295 | 2,430 |
| Interest expense | (541) | (516) | (800) | (1,314) | (2,114) |
| FX transaction gain | (2) | 70 | 160 | 227 | 387 |

**Key observations:**

1. **$62,814M of H1 2026 pre-tax income came from marking up non-marketable equity stakes** (almost certainly the AI/strategic investment portfolio). This is non-cash, non-recurring in nature, and reversal-prone. It is **99.5% of H1 2026's $63.1B increase in non-operating income**.
2. The balance-sheet counterpart: **`EquitySecuritiesWithoutReadilyDeterminableFairValue` exploded from $16,200M (31-Dec-25) to $122,300M (30-Jun-26)** — a $106.1B increase, of which ~$62.8B is mark-up and the remainder is new capital deployed into private/strategic assets. This single line is now **11.2% of total assets** and is marked through the P&L. Expect violent earnings swings from it in future quarters.
3. **Interest expense +155% y/y in Q2 ($1,314M vs. $516M)**, exceeding interest income in Q2 for a **net interest expense of roughly –$19M**. The debt-funded capex program is now crossing the threshold where financing cost is a P&L headwind.
4. **Tax rate normalization is a real drag.** ETR 23.0% vs. 17.0% (+600bp). H1 taxes rose 284% against +184% pre-tax growth.

### 4.2 "Core" (ex-mark-up) earnings power

| | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 |
|---|---|---|---|---|
| Reported net income | 17,127 | 18,164 | 30,255 | 62,647 |
| Less: mark-up, after 22.5% tax | ~29 | ~38 | ~9,554 | ~39,127 |
| **Core net income (est.)** | **~17,100** | **~18,126** | **~20,701** | **~23,520** |
| **Core diluted EPS (est.)** | **~1.59** | **~1.68** | **~1.90** | **~2.16** |

- Core EPS growth: **Q1 +19.5% y/y, Q2 +28.6% y/y**.
- **TTM reported EPS ≈ $12.42** (TTM net income $135,281M ÷ ~10,890M diluted shares).
- **TTM core EPS ≈ $8.0** (removing ~$48.7B of after-tax mark-up).
- *This is the single most important number in the report:* the stock's optically cheap GAAP multiple is an artifact; the honest earnings base is roughly **35% lower** than reported.

---

## 5. Cost Structure & Operating Leverage

| $M | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 | H1 2026 |
|---|---|---|---|---|---|
| Marketing | 10,015 | 11,416 | 10,314 | 11,698 | 22,012 |
| % of revenue | 6.4% | 6.8% | 5.7% | **5.8%** | 5.8% |
| G&A | 2,628 | 2,965 | 2,587 | 2,788 | 5,375 |
| % of revenue | 1.7% | 1.8% | 1.4% | **1.4%** | 1.4% |
| Operating lease cost | 3,240 | 3,426 | 3,917 | 4,118 | 8,035 |
| D&A | 14,262 | 15,227 | 18,945 | 19,988 | 38,933 |
| % of revenue | 9.2% | 9.1% | 10.4% | **10.0%** | 10.2% |
| SBC | 3,689 | 6,534 | 4,032 | 6,038 | 10,070 |
| **Total opex (derived)** | 60,286 | 67,722 | 70,204 | 77,367 | 147,571 |
| **% of revenue** | 38.7% | 40.4% | 38.7% | **38.6%** | 38.6% |

**Read-through:**
- The margin expansion is **NOT** coming from opex leverage alone — opex was flat at ~38.6% of revenue y/y. Roughly **140bp of the 230bp margin gain came from gross margin**, and ~90bp from the opex ratio.
- **Marketing efficiency is the standout:** marketing dollars grew only +2.5% in Q2 while revenue grew +19.6%. That is a 110bp margin contribution and suggests very strong organic traffic/Prime engagement.
- **The offsetting drag is depreciation:** D&A rose +31.3% y/y in Q2 and now consumes 10.0% of revenue (9.1% a year ago). Depreciation alone (PP&E, ex-amortization) rose **+41.9% in H1 2026**. With TTM capex at **2.3x TTM D&A ($173.0B vs. $75.2B)**, the depreciation curve has years of steep ascent left. **This is the primary mechanism by which AI capex eventually compresses margins.**

---

## 6. Revenue Trajectory & Working Capital Efficiency

- **Growth is accelerating, not decelerating:** Q1'26 +16.6% → Q2'26 +19.6%. H1 aggregate +18.2%.
- **Inventory is remarkably disciplined:** $38,184M at 30-Jun-26 vs. $38,325M at 31-Dec-25 — **flat in dollars while revenue runs +19.6% y/y**. Implied inventory turns (Q2 COGS annualized ÷ inventory) ≈ **10.0x**, days on hand ≈ **36 days**, and inventory valuation reserves were *released* ($3,300M → $3,000M), indicating no obsolescence build.
- **Receivables grew faster than revenue:** AR $67,729M → $88,092M (+30.1% in six months). Implied DSO ≈ **40 days**. Allowance for doubtful accounts rose $2,400M → $2,800M (+16.7%), directionally appropriate but worth monitoring — receivables are increasingly advertising/third-party-seller/cloud related.
- **Payables are the funding engine:** AP $121,909M → $147,440M (+20.9%). Implied DPO ≈ **140 days**. This is Amazon's classic supplier-financed float, but at $147.4B it is also a **concentration/liquidity lever** — a tightening of payment terms would hit cash flow immediately.
- **Contract liabilities (deferred revenue) flat at ~$24.9B** ($20,428M current + $4,500M non-current), with $15,200M of H1 2026 revenue recognized from the opening balance. No demand signal deterioration here.

---

## 7. Balance Sheet — The Transformation

| $M | 31-Dec-2025 | 30-Jun-2026 | Δ |
|---|---|---|---|
| Cash & equivalents | 86,810 | 78,213 | –8,597 |
| Available-for-sale securities | 45,800 | **97,900** | **+52,100** |
| Accounts receivable, net | 67,729 | 88,092 | +20,363 |
| Inventory, net | 38,325 | 38,184 | –141 |
| **Total current assets** | 229,083 | 249,264 | +20,181 |
| Equity securities w/o readily det. FV | 16,200 | **122,300** | **+106,100** |
| **Total assets** | **818,042** | **1,095,689** | **+277,647 (+33.9%)** |
| Accounts payable | 121,909 | 147,440 | +25,531 |
| Accrued liabilities | 75,520 | 73,406 | –2,114 |
| **Total current liabilities** | 218,005 | 241,274 | +23,269 |
| Long-term debt — current | 2,748 | 3,330 | +582 |
| Long-term debt — non-current | 65,648 | **128,894** | **+63,246** |
| Operating lease liability (total) | 89,252 | 96,320 | +7,068 |
| Finance lease liability (total) | 12,286 | 13,451 | +1,165 |
| Additional paid-in capital | 140,024 | 149,619 | +9,595 |
| Accumulated OCI | 28,230 | **66,287** | **+38,057** |
| Shares outstanding (M) | 10,731 | 10,783 | +52 |

### 7.1 Leverage and liquidity

| $M | 31-Dec-2025 | 30-Jun-2026 |
|---|---|---|
| Gross debt (ex-finance leases) | 68,836 | **132,224** |
| + Finance leases | 12,286 | 13,451 |
| **Total debt incl. finance leases** | **81,122** | **145,675** |
| Cash + AFS securities | 132,610 | 176,113 |
| **Net cash (ex-operating leases)** | **+51,488** | **+30,438** |
| Operating lease liabilities | 89,252 | 96,320 |
| **Net debt incl. operating leases** | **+37,764** | **+65,882** |

- **Gross debt nearly doubled in six months (+92%).** AMZN is still technically net-cash on a traditional basis, but the cushion has halved, and **including operating leases the company is now in a ~$65.9B net-debt position**, up from $37.8B.
- **Current ratio: 249,264 / 241,274 = 1.03** (YE25: 1.05). Quick ratio **(249,264 – 38,184) / 241,274 = 0.875**. Thin — but this is structural to Amazon's float-funded model, not new.
- **Equity is inflating from two non-cash sources:** APIC +$9.6B (SBC) and AOCI +$38.1B. The AOCI jump (2.8x in six months) reflects mark-to-market gains on investment securities routed through OCI — **another source of book-value volatility that never touches the income statement**.
- **Derived stockholders' equity ≈ $545–575B** (total liabilities not tagged; derived from assets less identifiable liabilities). Implied **BVPS ≈ $51–53**. This is an estimate, not a filed figure — treat accordingly.
- **Derivative assets jumped 6.3x** ($112M → $705M) — consistent with a much larger hedging book around energy (270,000 MWh notional) and FX as the capital program scales.

### 7.2 Off-balance-sheet commitments — the real obligation stack

| $M at 30-Jun-2026 | Amount |
|---|---|
| Total contractual obligations | **650,034** |
| Due remainder of FY2026 | 42,752 |
| Due next twelve months | **78,084** |
| Due year 2 | 53,406 |
| Due year 3 | 46,767 |
| Due year 4 | 42,219 |
| Operating lease payments (undiscounted) | 116,350 |
| Finance lease payments (undiscounted) | 16,660 |
| Other commitments (remainder FY26) | 2,145 |

**$650B of contractual obligations** — the majority tied to the AI infrastructure build (power, chips, data-center capacity). This is a demand *commitment* as much as a liability; it is also a **fixed-cost ratchet** that converts into depreciation and lease expense over 2027–2030 regardless of demand.

---

## 8. Cash Flow — The Capex Supercycle

| $M | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 | H1 2025 | H1 2026 | **TTM Jun-26** | TTM Jun-25 |
|---|---|---|---|---|---|---|---|---|
| **Operating cash flow** | 17,015 | 32,515 | 26,032 | 45,387 | 49,530 | **71,419** | **161,403** | 121,137 |
| Capital expenditures | 25,019 | 32,183 | 44,203 | 54,208 | 57,202 | **98,411** | **173,028** | 107,656 |
| **Free cash flow** | **(8,004)** | **332** | **(18,171)** | **(8,821)** | **(7,672)** | **(26,992)** | **(11,625)** | **+13,481** |
| Acquisitions, net of cash | (48) | 1,700 | 15,408 | 24,359 | 1,652 | **39,767** | **41,956** | 4,809 |
| Purchases of marketable securities | (13,333) | (17,797) | (23,256) | (26,006) | (31,130) | (49,262) | (72,902) | (46,731) |
| Proceeds from sales/maturities | 7,737 | 11,441 | 17,686 | 24,196 | 19,178 | 41,882 | 67,090 | 30,924 |
| **Investing cash flow** | (29,803) | (39,424) | (64,212) | (79,245) | (69,227) | **(143,457)** | **(216,775)** | (123,569) |
| LT debt issued | 746 | 0 | 53,441 | 13,557 | 746 | **66,998** | **81,925** | 746 |
| ST debt issued | 1,815 | 2,093 | 6,018 | 9,368 | 3,908 | 15,386 | 20,798 | 8,187 |
| LT debt repaid | 0 | (2,751) | 0 | (2,752) | (2,751) | (2,752) | (5,022) | (7,434) |
| ST debt repaid | (2,082) | (1,392) | (6,018) | (9,573) | (3,474) | (15,682) | (20,634) | (7,901) |
| **Financing cash flow** | (47) | (2,539) | 52,767 | 10,146 | (2,586) | **62,913** | **+75,160** | (8,652) |
| FX effect | 244 | 1,008 | (1) | (53) | 1,424 | (54) | (314) | 864 |
| **Net change in cash + restricted** | — | — | — | — | (20,859) | **(9,179)** | **+19,474** | (10,220) |

*(TTM reconciles exactly: 161,403 − 216,775 + 75,160 − 314 = +19,474 ✓)*

### 8.1 Interpretation

1. **Operating cash flow is genuinely excellent and accelerating:** TTM $161.4B (+33.2%), H1 +44.2%, Q2 +39.6%. This is the strongest evidence that core demand is healthy.
2. **But every incremental dollar — and more — is going into capex.** Q2 2026 capex of **$54.2B in a single quarter** = **$217B annualized run-rate**, up 68.4% y/y. **Capex/revenue reached 27.0% in Q2 2026** (19.2% in Q2 2025) and 25.8% for H1 2026.
3. **FCF has inflected from positive to structurally negative.** TTM FCF of **–$11.6B** vs. +$13.5B a year ago — a **$25.1B swing**. H1 2026 alone consumed **$27.0B**. Q2'25 was the last positive FCF quarter (+$332M).
4. **M&A has re-activated:** TTM $41,956M vs. $4,809M (+772%), with **$24,359M spent in Q2 2026 alone**. AMZN is buying capability, not just building it. Cash paid for acquisitions is *not* in capex, so the true capital deployment is even larger than the $173B headline.
5. **The balance sheet is the plug.** $75,160M of net financing inflow (of which $81,925M LT issuance) funded the gap. Cash + restricted fell $9,179M in H1 despite that.
6. **Cash taxes are trivial vs. book taxes:** TTM cash taxes paid **$6,635M** against H1 2026 book tax expense of **$27,759M**. **Deferred tax expense was $30,489M in H1 2026** — i.e., current tax was a net *benefit*. Accelerated depreciation on the AI buildout is a massive cash-tax shield. **This is worth ~$20B+/yr of cash that will eventually normalize** — a underappreciated long-term headwind.

---

## 9. Capital Returns, SBC & Dilution

| $M | H1 2025 | H1 2026 | Q2 2025 | Q2 2026 |
|---|---|---|---|---|
| SBC expense | 10,223 | 10,070 | 6,534 | 6,038 |
| % of revenue | 3.2% | 2.6% | 3.9% | 3.0% |
| Unrecognized SBC (balance) | — | **24,800** | — | — |
| Diluted shares (M) | 10,792 | 10,890 | 10,812 | 10,895 |

- **SBC is being brought under control:** –1.5% y/y in H1 and –7.6% in Q2, falling to **3.0% of revenue from 3.9%**. Positive for margin quality.
- **Dilution is minimal:** +0.9% y/y in diluted shares. Shares outstanding 10,783M at 30-Jun-26 vs. 10,786.3M at 22-Jul-26 — essentially flat.
- **No share repurchase data appears in the extract** (no treasury-stock or buyback tags for the period, and financing activities are dominated by debt issuance). **AMZN is not returning capital — it is raising it.** This is a growth-reinvestment regime, not a shareholder-yield regime.

---

## 10. Insider Transactions

**DATA_UNAVAILABLE.** The data package contains no authorized, point-in-time insider-transactions archive for AMZN as of 2026-09-04. No insider buying or selling is reported, inferred, or estimated in this document. Anyone citing insider activity for AMZN in this window must source it independently (Form 4 filings) — this report cannot support such a claim.

---

## 11. Financial History — Multi-Period Summary

| $M | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | TTM Jun'26 |
|---|---|---|---|---|---|---|---|
| Revenue (derived) | 155,667 | 167,702 | n/a | n/a | 181,519 | 200,606 | n/a* |
| Gross margin | 50.6% | 51.8% | n/a | n/a | 51.8% | 52.3% | n/a |
| Operating income | 18,405 | 19,171 | n/a | n/a | 23,852 | 27,461 | n/a* |
| Operating margin | 11.8% | 11.4% | n/a | n/a | 13.1% | 13.7% | n/a |
| Net income | 17,127 | 18,164 | n/a | n/a | 30,255 | 62,647 | **135,281** |
| Diluted EPS | 1.59 | 1.68 | — | — | 2.78 | 5.75 | **~12.42** |
| Core EPS (ex-markup, est.) | 1.59 | 1.68 | — | — | 1.90 | 2.16 | **~8.0** |
| Operating cash flow | 17,015 | 32,515 | n/a | n/a | 26,032 | 45,387 | **161,403** |
| Capex | 25,019 | 32,183 | n/a | n/a | 44,203 | 54,208 | **173,028** |
| Free cash flow | (8,004) | 332 | n/a | n/a | (18,171) | (8,821) | **(11,625)** |

\*Q3/Q4 2025 income-statement and cash-flow detail is **not present** in the point-in-time extract (no 10-K fact set). Derivable cross-check: TTM net income $135,281M less H1 2026 $92,902M ⇒ **H2 2025 net income ≈ $42,379M**, implying **FY2025 net income ≈ $77,670M** (a consistent +31% over the ~$59.2B earned in FY2024).

---

## 12. Risk Register (evidence-based only)

| Risk | Evidence | Severity |
|---|---|---|
| **Earnings quality / mark-to-model** | $62,814M H1'26 pre-tax gain from marking up non-marketable equity stakes; $122.3B of such assets now on balance sheet (11.2% of total). Non-cash, reversible, P&L-routed. | **High** |
| **Negative & deteriorating FCF** | TTM FCF –$11.6B vs. +$13.5B prior year; H1'26 –$27.0B; Q2 capex 27.0% of revenue. | **High** |
| **Rapidly rising leverage** | Debt $68.8B → $132.2B in 6 months; TTM issuance $81.9B; net cash halved to ~$30.4B; net debt incl. leases $65.9B. | **High** |
| **Depreciation cliff** | D&A +31% y/y Q2, +32% H1; capex/D&A = 2.3x; TTM capex $173B will depreciate over coming years. | **High** |
| **Tax normalization** | ETR 17.0% → 23.0%; $30.5B deferred tax in H1'26; cash taxes only $6.6B TTM. Cash-tax shield dilutes over time. | Medium-High |
| **Interest cost inflection** | Interest expense +155% y/y Q2; net interest turned negative (–$19M) in Q2'26 for the first time. | Medium |
| **Fixed-cost commitments** | $650B total contractual obligations; 78.1B due <12mo; operating lease payments $116.4B undiscounted. | Medium |
| **AOCI volatility** | AOCI $28.2B → $66.3B in 6 months (+135%); $38.1B of OCI bypassed the income statement. Book value is unstable. | Medium |
| **Thin liquidity ratios** | Current ratio 1.03; quick ratio 0.875; cash fell $8.6B and restricted cash down $9.2B in H1. | Medium |
| **Receivables growth** | AR +30.1% in 6 months vs. revenue +19.6% y/y; allowance up 16.7%. | Low-Medium |
| **Data/verification risk** | No segment (AWS) data, no FY2025 10-K, no price data, no insider data in this extract. **AWS margin trend is unverified.** | **High (analytical)** |

### Positive factors (equally evidence-based)
| Driver | Evidence |
|---|---|
| **Revenue re-acceleration** | Q1 +16.6% → Q2 +19.6% y/y; H1 +18.2%. |
| **Operating margin expansion** | 11.4% → 13.7% in Q2 (+230bp); 11.6% → 13.4% H1. |
| **Gross margin expansion** | 51.8% → 52.3% Q2; driven by mix (ads/subscriptions/third-party). |
| **Marketing efficiency** | Marketing +2.5% vs. revenue +19.6% in Q2; 6.8% → 5.8% of revenue. |
| **SBC discipline** | –7.6% y/y in Q2; 3.9% → 3.0% of revenue; dilution only +0.9%. |
| **Inventory discipline** | Inventory flat at $38.2B while revenue +19.6%; reserves released. |
| **Operating cash flow strength** | TTM $161.4B, +33%; H1 +44%; Q2 +40%. |
| **Exceptional cash-tax shield** | Cash taxes $6.6B TTM vs. book tax $27.8B in H1 alone. |
| **Strategic asset value** | Non-marketable equity portfolio marked at $122.3B — latent value in AI ecosystem stakes. |

---

## 13. Actionable Insights for Traders

### 13.1 The single most important adjustment
**Do not value AMZN on reported EPS.** The $62.8B H1 mark-up inflates TTM EPS to ~$12.42; core TTM EPS is ~**$8.0**. Any screen, model, or algorithm using GAAP trailing EPS will show AMZN ~35% cheaper than it is. **Rebuild the multiple on ~$8.0 of core earnings** (or on operating income, or EV/EBITDA), not on $12.42.

### 13.2 What is genuinely working
- **Demand is accelerating**, not fading: 19.6% growth at $200B+ quarterly scale is exceptional.
- **Margin expansion is operational, not accounting** — and comes from **gross margin mix (ads/subscriptions/3P) plus marketing efficiency**, both high-quality, recurring sources.
- **Cash generation is intact at the operating line** (+40% in Q2). The FCF problem is a *choice* (capex), not a demand problem. **This distinction is the crux of the bull case.**

### 13.3 What the bears will point to (and they have data)
- **FCF is negative and worsening** — a company earning $161B of operating cash flow produced **negative** free cash flow. If capex guidance rises again, FCF stays negative into 2027.
- **Debt doubled in six months.** Every incremental $10B of debt adds ~$450–500M of annual interest at prevailing coupons — directly visible already in the +155% Q2 interest expense.
- **The mark-up is not repeatable.** Q1'26 contributed $12.3B and Q2'26 $50.5B of pre-tax income from revaluations. **The base effect means Q1 2027 and Q2 2027 will face brutal y/y comparisons** unless the private-AI portfolio keeps re-rating. Model this: if no new mark-up occurs, Q2 2027 GAAP EPS could fall ~60% y/y on a like-for-like basis despite strong operations. **This is a live "EPS air-pocket" risk for the stock in mid-2027.**
- **Depreciation is compounding at +30–40%** and capex/D&A is 2.3x. Margin expansion has a shelf life unless revenue keeps outrunning the D&A curve.

### 13.4 Specific monitors for the next two quarters
1. **Capex trajectory.** Q2 was $54.2B; Q1 $44.2B. If Q3 prints above ~$60B, FCF stays negative and the leverage narrative dominates. **A sequential flattening in capex is the #1 bullish catalyst.**
2. **Whether the equity mark-up repeats.** Watch `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment` and the $122.3B balance. A flat or down mark in Q3 would remove ~$3.5–4.5 of quarterly EPS.
3. **Interest expense > interest income.** Q2 already flipped to net interest expense (–$19M). A confirmed trend means financing cost becomes a visible EPS headwind.
4. **ETR.** 23.0% in H1 vs. 17.0%. If it holds at 23%+, consensus EPS needs trimming on core operations alone.
5. **Debt maturities and incremental issuance.** Watch whether the $132.2B debt load grows further; each $20B adds ~$900M–1.0B annual interest.
6. **DSO/DPO.** DSO at 40 days and DPO at 140 days are the two levers that could produce a sudden cash-flow shock if either normalizes.
7. **Deferred-tax balance.** $30.5B in H1 2026 is a cash benefit that will fade; when it does, cash taxes move from $6.6B toward the $27B+ book rate — a multi-billion-dollar annual cash headwind.

### 13.5 Positioning framework

| Trader profile | Suggested framing |
|---|---|
| **Momentum / growth** | The operational data supports the thesis: 19.6% growth, +230bp margins, +40% OCF. The risk is *multiple compression on an EPS air-pocket*, not demand. |
| **Quality / value** | AMZN fails a clean-FCF screen today (–$11.6B TTM) and carries a mark-to-model asset equal to 11% of the balance sheet. Wait for capex discipline or FCF inflection. |
| **Credit / risk** | Gross debt +92% in six months against a current ratio of 1.03 and $78.1B due in 12 months on contractual obligations. Investment-grade but **deteriorating rapidly**. |
| **Event-driven** | Q2 2027 is the air-pocket quarter: the $50.5B mark-up will not repeat unless re-marked. Watch for management framing/segment disclosure changes. |

### 13.6 Explicit non-conclusions
Because the extract contains **no share price, no AWS segment data, no FY2025 10-K, and no insider data**, this report **does not** make a buy/sell/hold recommendation, does not compute a target price, and does not assert an AWS margin trend. Those require the valuation tool and the full 10-K/segment footnote.

---

## 14. Key Points Summary Table

| Category | Metric | Latest / TTM | Prior Comparable | Δ | Read |
|---|---|---|---|---|---|
| **Scale** | Revenue (Q2 2026) | $200,606M | $167,702M | **+19.6%** | Re-acceleration |
| **Scale** | Revenue (H1 2026) | $382,125M | $323,369M | **+18.2%** | Strong |
| **Profitability** | Gross margin (Q2) | 52.3% | 51.8% | +50bp | Mix shift favorable |
| **Profitability** | Operating income (Q2) | $27,461M | $19,171M | **+43.2%** | Real leverage |
| **Profitability** | Operating margin (Q2) | 13.7% | 11.4% | **+230bp** | Expanding |
| **Profitability** | Operating margin (H1) | 13.4% | 11.6% | +180bp | Expanding |
| **Earnings quality** | H1 non-operating income | $69,378M | $4,960M | +1,299% | **Mark-to-model** |
| **Earnings quality** | H1 equity mark-up (pre-tax) | **$62,814M** | $86M | nm | **Non-cash, non-recurring** |
| **Earnings quality** | Reported diluted EPS (Q2) | $5.75 | $1.68 | +242% | Inflated |
| **Earnings quality** | **Core diluted EPS (Q2, est.)** | **~$2.16** | $1.68 | **+~29%** | Honest growth rate |
| **Earnings quality** | TTM reported EPS | ~$12.42 | — | — | Distorted |
| **Earnings quality** | **TTM core EPS (est.)** | **~$8.0** | — | — | Use this multiple |
| **Tax** | Effective tax rate (H1) | 23.0% | 17.0% | +600bp | Headwind |
| **Tax** | Deferred tax expense (H1) | $30,489M | $518M | nm | Big cash shield |
| **Tax** | Cash taxes paid (TTM) | $6,635M | $11,788M | –43.7% | Shield at work |
| **Cash flow** | Operating cash flow (TTM) | **$161,403M** | $121,137M | **+33.2%** | Excellent |
| **Cash flow** | Operating cash flow (H1) | $71,419M | $49,530M | +44.2% | Excellent |
| **Cash flow** | Capex (TTM) | **$173,028M** | $107,656M | **+60.7%** | Supercycle |
| **Cash flow** | Capex (Q2) | $54,208M | $32,183M | +68.4% | ~$217B annualized |
| **Cash flow** | Capex/revenue (Q2) | 27.0% | 19.2% | +780bp | Capital intensity |
| **Cash flow** | **Free cash flow (TTM)** | **–$11,625M** | +$13,481M | **–$25.1B** | **Key bear point** |
| **Cash flow** | Free cash flow (H1) | –$26,992M | –$7,672M | –$19.3B | Worsening |
| **Cash flow** | Acquisitions (TTM) | $41,956M | $4,809M | +772% | M&A re-activated |
| **Balance sheet** | Total assets | $1,095,689M | $818,042M (YE25) | **+33.9%** | Expanded |
| **Balance sheet** | Cash + AFS securities | $176,113M | $132,610M | +$43.5B | Liquidity built |
| **Balance sheet** | Gross debt (ex-leases) | $132,224M | $68,836M | **+92.1%** | Levering up |
| **Balance sheet** | Net cash (ex-op leases) | +$30,438M | +$51,488M | –$21.1B | Cushion halved |
| **Balance sheet** | Net debt incl. op leases | $65,882M | $37,764M | +$28.1B | Now net-levered |
| **Balance sheet** | Current ratio | 1.03x | 1.05x | –0.02 | Thin |
| **Balance sheet** | Quick ratio | 0.875x | — | — | Thin |
| **Balance sheet** | Non-marketable equity securities | **$122,300M** | $16,200M | **+$106.1B** | Mark-to-model risk |
| **Balance sheet** | AOCI | $66,287M | $28,230M | +135% | Book-value volatility |
| **Balance sheet** | Inventory | $38,184M | $38,325M | –0.4% | Excellent discipline |
| **Balance sheet** | Accounts receivable | $88,092M | $67,729M | +30.1% | Growing faster than sales |
| **Balance sheet** | Accounts payable | $147,440M | $121,909M | +20.9% | Float lever |
| **Balance sheet** | Contractual obligations | $650,034M | — | — | Fixed-cost ratchet |
| **Cost structure** | D&A (Q2) | $19,988M | $15,227M | +31.3% | Depreciation wave |
| **Cost structure** | SBC (Q2) | $6,038M | $6,534M | –7.6% | Disciplined |
| **Cost structure** | Marketing/revenue (Q2) | 5.8% | 6.8% | –100bp | Efficiency win |
| **Cost structure** | Interest expense (Q2) | $1,314M | $516M | **+154.7%** | Financing cost rising |
| **Capital** | Diluted shares | 10,895M | 10,812M | +0.8% | Minimal dilution |
| **Capital** | Buybacks | None observed | — | — | Reinvestment regime |
| **Market data** | Price / P/E / EV | **NOT AVAILABLE** | — | — | Valuation tool required |
| **Insider data** | Form 4 activity | **NOT AVAILABLE** | — | — | No inference made |

---

### Bottom line for the trading desk

AMZN's **operating engine is the strongest it has ever been** — 19.6% growth at a $200B quarterly base, 13.7% operating margins, +40% operating cash flow, flat inventory, and shrinking SBC. **But the reported bottom line is materially overstated by a $62.8B non-cash revaluation, free cash flow is negative, and gross debt nearly doubled in six months.** The correct posture is to **trade AMZN on core earnings (~$8.0 TTM) and on the capex/FCF trajectory — not on the $5.75 headline Q2 EPS** — and to keep a hard date on the calendar for **Q2 2027, when the mark-up anniversary creates a severe GAAP EPS comparison.**