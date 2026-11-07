# AMZN — Fundamental Deep Dive
**Amazon.com, Inc. | Data as of 2026-09-03 | Latest filing: Form 10-Q for period ended 2026-06-30, filed/accepted 2026-07-31 (accn 0001018724-26-000026)**

---

## 1. Executive Summary — What the Numbers Actually Say

Amazon's June-2026 quarter shows a business that is simultaneously **accelerating at the top line, expanding operating margins, and burning free cash flow at a record pace** while reporting earnings that are **majority-driven by a non-cash revaluation of an equity stake**.

**The five things that matter:**

1. **Revenue re-accelerated to ~+19.6% y/y in Q2 2026** (derived: $200.6B) and **+18.2% in H1 2026** ($382.1B) — a marked step-up from Amazon's mid-teens historical run-rate, consistent with an AI/cloud-led inflection.
2. **Operating leverage is real:** operating income +43.2% y/y in Q2 ($27.5B) and +36.6% in H1 ($51.3B); operating margin expanded **+226bps to 13.7%** in Q2 and **+181bps to 13.4%** in H1.
3. **Earnings quality is poor at the headline level:** Q2 2026 non-operating income was **$53.4B**, of which **$50.5B was a non-cash upward price adjustment on equity securities without readily determinable fair value**. H1 2026: **$62.8B of such marks**. Stripping them out, "core" diluted EPS is roughly **$2.1 for Q2 and ~$4.0 for H1 — versus reported $5.75 and $8.53.**
4. **Free cash flow has turned negative:** H1 2026 OCF $71.4B less capex $98.4B = **–$27.0B FCF** (vs –$7.7B in H1 2025). Trailing-twelve-month capex is **$173.0B** against TTM OCF of **$161.4B** → **TTM FCF of –$11.6B.**
5. **The balance sheet is being levered to fund it:** long-term debt rose from **$68.8B (Dec-25) to $133.0B (Jun-26)**; total LT+ST debt issuance of **$102.7B in the TTM** against $5.0B LT repayments. Non-marketable equity holdings exploded from **$16.2B to $122.3B** and cash acquisitions hit **$39.8B in H1 2026** alone.

**Net read:** the *operating* engine is arguably the strongest it has ever been, but the *earnings and cash-flow optics* are heavily distorted — positively by mark-to-market gains, negatively by a capex supercycle. This is a stock where a trader must separate the two.

---

## 2. Data Provenance & Limitations (read before using any figure)

- All data are **point-in-time SEC XBRL facts** filtered by EDGAR acceptance timestamp through 2026-09-03. The latest available filing is the **Q2 2026 10-Q (period end 2026-06-30)**; a Q1 2026 10-Q (accn 0001018724-26-000014, filed 2026-04-30) is also present for prior-period balance data.
- **No annual (10-K) statements were returned.** Requesting `annual` frequency returned the same 10-Q facts. Multi-year history is therefore limited to the comparatives embedded in the Q2 2026 filing: **Q2 2026 vs Q2 2025, H1 2026 vs H1 2025, and TTM (2025-07-01 → 2026-06-30)**.
- **The tag set is partially truncated.** Tags from roughly "S" to "Z" were not returned — notably `Revenues`, `RetainedEarnings`, `StockholdersEquity`, `PropertyPlantAndEquipment`, buyback and dividend tags. **Revenue below is therefore *derived* as `CostsAndExpenses + OperatingIncomeLoss`**, which is a valid identity under Amazon's P&L presentation but should be treated as derived, not reported.
- **No segment-level revenue or profit data** is in the dataset (only `NumberOfOperatingSegments = 3`).
- **No share price, market cap, or consensus estimates** are available from these tools — valuation multiples must be computed externally.
- **Insider transactions: UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for AMZN as of 2026-09-03. **No insider buying or selling activity is inferred or fabricated in this report.**

---

## 3. Company Profile

Amazon.com, Inc. (NASDAQ: AMZN) operates three reportable segments, confirmed by the 10-Q (`NumberOfOperatingSegments = 3`):

- **North America** — the retail marketplace (1P and 3P), Prime subscription, physical stores (Whole Foods), and the advertising business.
- **International** — the same commerce stack across Europe, Japan, and other geographies.
- **Amazon Web Services (AWS)** — cloud compute, storage, database, and an expanding AI stack (custom silicon, model hosting, and managed AI services).

The economic engine is a **negative-cash-conversion retail flywheel** (customers pay quickly, Amazon pays suppliers slowly) that funds a high-margin cloud and advertising complex, which in turn funds reinvestment. As of June 2026, that reinvestment has pivoted aggressively toward **AI infrastructure, acquisitions, and strategic equity stakes** — a shift visible in every major line of the financial statements below.

---

## 4. Income Statement — Q2 and H1 2026

### 4.1 Summary table ($ millions)

| Metric ($M) | Q2 2025 | Q2 2026 | YoY | H1 2025 | H1 2026 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Revenue *(derived)* | 167,702 | 200,606 | **+19.6%** | 323,369 | 382,125 | **+18.2%** |
| Cost of goods & services | 80,809 | 95,778 | +18.5% | 157,785 | 183,241 | +16.1% |
| Gross profit | 86,893 | 104,828 | +20.6% | 165,584 | 198,884 | +20.1% |
| **Gross margin** | 51.8% | **52.3%** | +45bps | 51.2% | **52.1%** | +84bps |
| Marketing expense | 11,416 | 11,698 | +2.5% | 21,179 | 22,012 | +3.9% |
| G&A expense | 2,965 | 2,788 | –6.0% | 5,593 | 5,375 | –3.9% |
| Total costs & expenses | 148,531 | 173,145 | +16.6% | 285,793 | 330,812 | +15.8% |
| **Operating income** | 19,171 | **27,461** | **+43.2%** | 37,576 | **51,313** | **+36.6%** |
| **Operating margin** | 11.4% | **13.7%** | +226bps | 11.6% | **13.4%** | +181bps |
| Non-operating income/(expense) | 1,686 | **53,396** | +3,067% | 4,960 | **69,378** | +1,299% |
| Pre-tax income | 20,857 | **80,857** | +288% | 42,536 | **120,691** | +184% |
| Income tax expense | 2,678 | 18,199 | +580% | 7,231 | 27,759 | +284% |
| *Effective tax rate* | 12.8% | 22.5% | | 17.0% | 23.0% | |
| **Net income** | 18,164 | **62,647** | **+245%** | 35,291 | **92,902** | **+163%** |
| **Diluted EPS** | $1.68 | **$5.75** | **+242%** | $3.27 | **$8.53** | **+161%** |
| Basic EPS | $1.71 | $5.82 | | $3.32 | $8.64 | |
| Share-based comp | 6,534 | 6,038 | –7.6% | 10,223 | 10,070 | –1.5% |
| D&A | 15,227 | 19,988 | +31.3% | 29,489 | 38,933 | +32.0% |

### 4.2 What's driving the operating improvement

- **Gross margin +45bps y/y in Q2 and +84bps in H1** — mix shift toward AWS and advertising, plus continued logistics cost deflation.
- **Marketing expense grew just 2.5% y/y in Q2 against 19.6% revenue growth** — a 98bps decline as a share of revenue (6.81% → 5.83%). This is direct evidence of brand/Prime flywheel efficiency.
- **G&A fell 6.0% y/y in absolute dollars** — remarkable operating discipline (1.77% → 1.39% of revenue).
- **SBC fell 7.6% y/y in Q2** while revenue grew ~20%: SBC fell from 3.90% to 3.01% of revenue. Unrecognized SBC of **$24.8B** remains to be expensed (~2.5 years at the current run-rate, or ~1.2 years at the TTM rate).
- **Residual "fulfillment + technology & content + other" bucket** (derived) = $62.9B in Q2 2026 vs $53.3B in Q2 2025 — grew 17.9%, slightly *slower* than revenue (31.4% → 31.3% of revenue). Technology & content investment is being absorbed, not ballooning.

**Caution — depreciation is now a margin headwind:** D&A rose **+31.3% y/y in Q2** to $19,988M, or **9.96% of revenue vs 9.08%** a year ago. With $173B of TTM capex entering service, D&A growth will continue to outrun revenue growth for several years. This is the mechanical offset to the gross-margin story.

### 4.3 Earnings quality — the single most important adjustment

The non-operating line is where the headline numbers are made:

| $M | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 | TTM |
|---|---:|---:|---:|---:|---:|
| Interest & investment income | 1,085 | 1,295 | 2,151 | 2,430 | — |
| Interest expense | (516) | (1,314) | (1,057) | (2,114) | — |
| Equity securities FV-NI gain | 393 | 1,300 | 188 | 454 | — |
| **Upward price adj. on non-marketable equity** | **49** | **50,486** | **86** | **62,814** | — |
| Warrant fair-value adjustment | (590) | (1,449) | (212) | (1,051) | — |
| FX transaction gain | 70 | 227 | 68 | 387 | — |
| **Total non-operating income** | **1,686** | **53,396** | **4,960** | **69,378** | — |

- **$50.5B of Q2 2026 pre-tax income (62.4% of pre-tax) came from revaluing non-marketable equity holdings.** H1: $62.8B (52.1% of pre-tax).
- This is **non-cash, non-recurring in nature, and reversible.** It sits in income (not OCI) and therefore flows straight into GAAP EPS, but adds nothing to operating cash flow.
- The tax charge associated with it is largely **deferred and non-cash**: H1 2026 book tax expense was $27.8B but **cash taxes paid were only $4.0B (3.3% of pre-tax)**. TTM: $6.6B cash taxes paid vs $41.4B deferred tax expense.

**Pro-forma "core" earnings (my adjustment):**

| | Q2 2026 | H1 2026 |
|---|---:|---:|
| Reported pre-tax income | 80,857 | 120,691 |
| Less: non-marketable equity mark-up | (50,486) | (62,814) |
| **Core pre-tax income** | **30,371** | **57,877** |
| Tax @ ~25% (normalized) | (7,593) | (14,469) |
| **Core net income** | **~22,778** | **~43,408** |
| **Core diluted EPS** | **~$2.09–2.16** | **~$3.99** |
| Reported diluted EPS | $5.75 | $8.53 |
| **Reported premium to core** | **~+170%** | **~+114%** |

**Core EPS grew ~+24% y/y in Q2 and ~+22% in H1.** That is a genuinely good result for a company this size — but it is *less than a tenth* of the reported growth rate. Any screen or headline that uses GAAP EPS growth will mis-rank this quarter.

---

## 5. Balance Sheet — June 30, 2026 vs December 31, 2025

### 5.1 Key items

| $M | 2025-12-31 | 2026-06-30 | Change | % |
|---|---:|---:|---:|---:|
| Cash & equivalents | 86,810 | 78,213 | (8,597) | –9.9% |
| Marketable (AFS) securities | 45,800 | 97,900 | +52,100 | +113.8% |
| Accounts receivable, net | 67,729 | 88,092 | +20,363 | **+30.1%** |
| Inventory, net | 38,325 | 38,184 | (141) | –0.4% |
| **Total current assets** | 229,083 | 249,264 | +20,181 | +8.8% |
| **Total assets** | 818,042 | **1,095,689** | **+277,647** | **+33.9%** |
| Accounts payable | 121,909 | 147,440 | +25,531 | +20.9% |
| Accrued liabilities | 75,520 | 73,406 | (2,114) | –2.8% |
| **Total current liabilities** | 218,005 | 241,274 | +23,269 | +10.7% |
| Long-term debt (total) | 68,836 | **132,995** | +64,159 | **+93.2%** |
| — of which non-current | 65,648 | 128,894 | +63,246 | +96.3% |
| — of which current | 2,748 | 3,330 | +582 | +21.2% |
| Operating lease liabilities | 89,252 | 96,320 | +7,068 | +7.9% |
| Finance lease liabilities | 12,286 | 13,451 | +1,165 | +9.5% |
| Deferred revenue (contract liability) | 25,000 | 24,948 | (52) | –0.2% |
| Additional paid-in capital | 140,024 | 149,619 | +9,595 | +6.9% |
| Accumulated OCI | 28,230 | **66,287** | +38,057 | **+134.8%** |
| Shares outstanding | 10,731 | 10,783 | +52 | +0.5% |

### 5.2 What stands out

- **Total assets grew 33.9% in six months** — a $278B expansion. The two dominant drivers visible in the data: **non-marketable equity securities +$106.1B** (from $16.2B to $122.3B, now ~11.2% of total assets) and **cash M&A of $39.8B** in H1 (largely goodwill/intangibles, though the goodwill tag was not returned). Total asset growth of this magnitude with only +0.5% share count growth implies **external financing and revaluation, not organic earnings retention alone.**
- **Long-term debt nearly doubled (+93%) to $133.0B.** Add finance leases ($13.5B) → **$146.4B of debt**. Add operating leases ($96.3B) → **$242.7B of total fixed obligations.**
- **Liquidity is nonetheless strong:** cash $78.2B + AFS securities $97.9B = **$176.1B**, giving a **net cash position of ~$29.7B** on a debt-only basis. Gross debt / annualized Q2 EBITDA ($27.5B OI + $20.0B D&A = $47.4B × 4 = ~$190B) ≈ **0.77x**. Even including operating leases, **~1.28x**. This is not a leverage problem *yet*.
- **Accounts receivable +30.1% in six months** versus roughly +18% revenue growth. Derived DSO (H1 basis) ≈ **41.7 days** vs an estimated ~35 days at year-end 2025 — an ~6-day deterioration. Watch this: it could reflect a mix shift toward enterprise/AWS billing, or looser terms. It is a **$20B+ cash drag** and a genuine yellow flag on cash conversion.
- **Payables +20.9% to $147.4B** — derived DPO ≈ **140 days**. Combined with DIO ≈ 36 days and DSO ≈ 40 days, the **cash conversion cycle is roughly –64 days**. The negative-CCC funding model is intact and remains a structural advantage.
- **Current ratio 1.03** (was 1.05) — tight, but Amazon's current liabilities are overwhelmingly non-interest-bearing trade payables, so this is not a solvency signal.
- **No buyback, no dividend:** shares outstanding rose 0.5% and APIC rose $9.6B (≈ SBC). Capital is being recycled into capex/M&A, not returned.
- **AOCI rose $38.1B to $66.3B** — a large book-equity boost that bypasses the income statement. *Note: the source of this swing is not cleanly identifiable in the returned tag set (H1 FX translation OCI was actually –$1.6B). Treat the AOCI jump as an unresolved data item and do not extrapolate it into book value without the full 10-Q.*

> **Not retrievable:** total stockholders' equity, retained earnings, and PP&E were not returned in the truncated tag set. Equity is therefore *not* computed here rather than estimated. With APIC $149.6B + AOCI $66.3B + common stock $0.1B and substantial cumulative retained earnings, book equity is materially positive and large — total liabilities are the residual and are not a concern given the interest coverage below.

### 5.3 Coverage & solvency

- **Interest coverage (operating income / interest expense): 20.9x in Q2 2026; 24.3x in H1 2026.**
- Interest expense doubled y/y (Q2: $516M → $1,314M) and will keep climbing as the new debt seasons. At a ~4.5–5% average coupon on ~$146B, run-rate interest expense approaches **$6.5–7.0B annually** vs $4.2B annualized from H1. Still trivially covered by $110B+ of annualized operating income.

---

## 6. Cash Flow — The Capex Supercycle

### 6.1 Summary ($ millions)

| $M | Q2 2025 | Q2 2026 | YoY | H1 2025 | H1 2026 | YoY | TTM Jun-26 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Operating cash flow | 32,515 | 45,387 | **+39.6%** | 49,530 | 71,419 | **+44.2%** | **161,403** |
| Capex (productive assets) | 32,183 | 54,208 | **+68.4%** | 57,202 | 98,411 | **+72.0%** | **173,028** |
| **Free cash flow** | **332** | **(8,821)** | n.m. | **(7,672)** | **(26,992)** | n.m. | **(11,625)** |
| Acquisitions, net of cash | 1,700 | 24,359 | +1,333% | 1,652 | 39,767 | +2,307% | **41,956** |
| Purchases of marketable securities | 17,797 | 26,006 | +46% | 31,130 | 49,262 | +58% | 72,902 |
| Proceeds from sale/maturity of securities | 11,441 | 24,196 | +111% | 19,178 | 41,882 | +118% | 67,090 |
| Investing cash flow | (39,424) | (79,245) | n.m. | (69,227) | (143,457) | n.m. | **(216,775)** |
| Financing cash flow | (2,539) | 10,146 | n.m. | (2,586) | 62,913 | n.m. | **+75,160** |
| Net income | 18,164 | 62,647 | | 35,291 | 92,902 | | 135,281 |
| D&A | 15,227 | 19,988 | | 29,489 | 38,933 | | **75,200** |

### 6.2 Interpretation — three separate stories

**(a) Operating cash generation is genuinely strong.** OCF +44% y/y in H1, TTM $161.4B. Reported net income TTM was $135.3B, but ~$62.8B of that was a non-cash equity mark-up and ~$41.4B was deferred tax add-back. **Excluding the equity mark-up, "cash-backed" net income was roughly ~$72B, and OCF of $161B represents ~2.2x coverage** — the underlying cash engine is healthier than the GAAP numbers imply, once you decompose it.

The headwinds inside OCF are working capital: TTM drags of **–$21.4B from AR/other operating assets**, **–$6.1B from accrued liabilities**, **–$0.7B from deferred revenue**, offset by **+$17.8B from other non-current assets**.

**(b) Capex is the entire reason FCF is negative.** TTM capex of **$173.0B** is roughly **22% of annualized revenue** — versus Amazon's historical 6–10%. H1 2026 capex alone ($98.4B) exceeded all of H1 2025 by 72%. This is a deliberate, board-level decision to build AI/cloud/logistics capacity, not a cost overrun. **The FCF number is an investment-cycle artifact, and will inflect sharply upward the moment capex growth decelerates** — but it is also the primary thing that can break the equity story if the revenue doesn't materialize.

**(c) M&A is a new and under-appreciated line item.** **$39.8B in H1 2026**, $42.0B TTM, versus $4.8B in the prior TTM period — an **8.7x increase**. Combined with the $106B increase in non-marketable equity securities, Amazon is deploying well over $100B of capital into strategic (likely AI-ecosystem) positions in a single year. This is a fundamental shift in capital allocation and introduces **integration risk and valuation risk** that did not exist in the prior model.

---

## 7. Forward Obligations & Revenue Visibility

| $M (as of 2026-06-30) | Amount |
|---|---:|
| **Total contractual obligations** | **650,034** |
| Due in next 12 months | 78,084 |
| Due in remainder of FY2026 | 42,752 |
| Due in year 2 | 53,406 |
| Due in year 3 | 46,767 |
| Due in year 4 | 42,219 |
| Beyond year 4 (residual) | ~429,500 |
| Operating lease payments, undiscounted | 116,350 |
| — next 12 months | 14,765 |
| Finance lease payments, undiscounted | 16,660 |
| Deferred revenue (current + non-current) | 24,948 |
| Revenue recognized from deferred balance in H1 2026 | 15,200 |

**Two readings, both important:**

1. **Possibility / demand signal:** $650B of contractual obligations — 2.7x the entire on-balance-sheet debt + lease stack — is consistent with large, multi-year AI compute, energy, and content commitments. If these are customer-backed (i.e., AWS capacity contracted to hyperscale AI customers), they represent extraordinary forward revenue visibility.
2. **Risk signal:** if a material portion is *unconditional purchase* commitments to suppliers (chips, power, data-center capacity) rather than matched to contracted customer demand, Amazon has locked in ~$120B of near-term spend against an uncertain AI demand curve. **This is the largest single off-balance-sheet item and the most important thing to interrogate in the 10-Q footnotes.**

Deferred revenue of $25.0B (flat y/y, $15.2B recognized in H1) is modest relative to a ~$780B revenue base — Amazon's model is still overwhelmingly transactional, not subscription-committed.

---

## 8. Insider Transactions

**Not available.** The data vendor returned:

> *"DATA_UNAVAILABLE: the B-project data package has no authorized, point-in-time insider-transactions archive for AMZN by 2026-09-03. Do not infer or fabricate insider activity."*

No Form 4 purchases or sales are reported here, and **none should be assumed.** For a name this size, insider signal is typically low-value anyway (founder holdings dominate and sales are programmatic), but traders should source Form 4s separately if that input matters to the thesis.

---

## 9. Synthesized Fundamental Assessment

### Bull case (evidence-backed)
- **Revenue acceleration to ~+19% y/y with simultaneous margin expansion** — the rarest and most valuable combination in large-cap tech. Q2 OI +43%, H1 +37%.
- **Operating leverage is broad-based:** marketing +2.5%, G&A –6.0%, SBC –7.6% against +19.6% revenue. Every controllable cost line is being squeezed.
- **Core EPS growing ~22–24% y/y** even after fully removing the equity mark-up.
- **Negative cash conversion cycle of roughly –64 days** — structurally self-funding working capital.
- **Net cash of ~$30B** on a debt-only basis; gross leverage ~0.8x EBITDA (~1.3x including leases); interest coverage ~21–24x. The balance sheet has ample room.
- **$650B of contractual obligations** implies enormous, multi-year demand visibility if customer-backed.
- **$24.8B of unrecognized SBC** — future comp expense is already known and declining as a % of revenue.

### Bear case (evidence-backed)
- **~52–62% of H1/Q2 pre-tax income is a non-cash equity revaluation** that can reverse. A 20% markdown on the $122.3B non-marketable book would be a ~$24B pre-tax hit — roughly half of a full quarter's operating income.
- **TTM FCF of –$11.6B and H1 FCF of –$27.0B.** Capex is 22% of revenue and rising 72% y/y.
- **Debt nearly doubled in six months** (+$64B), and interest expense is compounding at +100% y/y.
- **$42B of TTM M&A** with integration and impairment risk, into a $122B equity-stake book with no observable exit liquidity.
- **D&A growing +31% y/y and now 10.0% of revenue** — mechanical margin pressure ahead as the $173B capex base depreciates.
- **AR +30.1% vs revenue +18%** — early sign of receivables quality deterioration or mix-driven cash drag (~$20B).
- **Cash taxes at just 3.3% of pre-tax income** — a future normalization to a mid-teens cash rate would remove a meaningful EPS tailwind.

### What to watch (catalyst calendar & KPIs)
1. **Q3 2026 results (~late October 2026)** — first read on whether H2 capex growth decelerates and whether revenue holds ~+18–20%.
2. **Capex guidance.** The single highest-leverage variable for the equity. Any signal of a plateau instantly converts a –$27B H1 FCF into a positive number.
3. **The $122.3B non-marketable equity book** — any disclosed mark-down, IPO, or secondary sale is a major swing factor for GAAP EPS.
4. **AWS growth and backlog disclosure** — needed to validate the $650B contractual obligation book.
5. **Footnote detail on the $650B contractual obligations** — customer-backed vs. unconditional supplier commitments.
6. **AR days and OCF conversion** — confirm the +30% AR build is mix, not credit.
7. **Debt trajectory** — whether the $102.7B TTM issuance pace continues; watch the credit rating and coupon.

### Positioning implication
The fundamental picture supports a **constructive operating view with a skeptical earnings view**. Traders should **anchor on operating income (+43% y/y), gross margin (52.3%), and revenue growth (~19.6%)** — all accelerating — and **discount GAAP EPS (~60%+ of which is a non-cash mark-up)**. The dominant near-term risk is not demand or margins; it is the **capex/FCF/debt triad** and the **reversibility of the equity revaluation**. A trader long the fundamental trend should watch capex guidance as the primary invalidation trigger; a trader short the print should recognize that the *operating* trends give little ammunition.

*Valuation cannot be assessed from these tools — no price or market-cap data is available. Apply multiples externally, and on a core (ex-mark-to-market) EPS base rather than GAAP.*

---

## 10. Key Points Summary Table

| Category | Metric | Value / Observation | Signal |
|---|---|---|---|
| **Reporting** | Latest filing | Q2 2026 10-Q, period end 2026-06-30, filed 2026-07-31 | Data ~5 weeks stale |
| **Scale** | Total assets | $1,095.7B (+33.9% in 6 months) | Massive expansion |
| **Growth** | Q2 2026 revenue *(derived)* | $200.6B, **+19.6% y/y** | **Strongly bullish** |
| **Growth** | H1 2026 revenue *(derived)* | $382.1B, **+18.2% y/y** | **Strongly bullish** |
| **Profitability** | Q2 operating income | $27,461M, **+43.2% y/y**; margin **13.7%** (+226bps) | **Bullish** |
| **Profitability** | H1 operating income | $51,313M, **+36.6% y/y**; margin **13.4%** (+181bps) | **Bullish** |
| **Profitability** | Gross margin | 52.3% Q2 / 52.1% H1 (+45 / +84bps) | Bullish |
| **Cost discipline** | Marketing / G&A / SBC y/y (Q2) | +2.5% / **–6.0%** / –7.6% vs revenue +19.6% | **Bullish** |
| **Earnings quality** | Q2 non-operating income | $53,396M, incl. **$50,486M non-cash equity mark-up** | **Bearish (quality)** |
| **Earnings quality** | H1 equity mark-ups | **$62,814M** = ~52% of pre-tax income | **Bearish (quality)** |
| **Earnings quality** | Reported vs core diluted EPS | Q2 $5.75 vs ~**$2.1**; H1 $8.53 vs ~**$4.0** | **Large optical premium** |
| **Core growth** | Core EPS growth (ex-marks) | ~+24% Q2, ~+22% H1 | Solid, not spectacular |
| **Cash flow** | TTM operating cash flow | **$161.4B** (+33% vs prior TTM $121.1B) | Bullish |
| **Cash flow** | TTM capex | **$173.0B** (~22% of revenue; +61% y/y) | **Bearish / key risk** |
| **Cash flow** | TTM free cash flow | **–$11.6B**; H1 2026 **–$27.0B** vs H1 2025 –$7.7B | **Bearish** |
| **Capex** | H1 2026 capex | $98.4B, **+72% y/y** | Investment supercycle |
| **M&A** | TTM cash acquisitions | **$41.96B** vs $4.81B prior (+772%) | New capital-allocation risk |
| **Balance sheet** | Long-term debt | $133.0B, up from $68.8B (**+93%** in 6 months) | **Bearish trend** |
| **Balance sheet** | Cash + AFS securities | $176.1B vs $132.6B at Dec-25 | Strong liquidity |
| **Balance sheet** | Net cash (debt-only) | **~+$29.7B** | Adequate cushion |
| **Balance sheet** | Total obligations incl. leases | ~$242.7B debt + operating leases | Manageable |
| **Leverage** | Gross debt / annualized EBITDA | **~0.77x** (debt) / ~1.28x (incl. leases) | Comfortable |
| **Coverage** | Operating income / interest | **20.9x (Q2), 24.3x (H1)** | Strong |
| **Non-cash items** | Non-marketable equity holdings | **$122.3B**, up from $16.2B (7.5x) = 11.2% of assets | High mark-to-market risk |
| **Non-cash items** | D&A | $19,988M Q2 (**+31.3% y/y**), 10.0% of revenue | Rising headwind |
| **Working capital** | Cash conversion cycle *(derived)* | **~–64 days** (DSO ~40, DIO ~36, DPO ~140) | Structural advantage |
| **Working capital** | Accounts receivable | $88.1B, **+30.1%** since Dec-25 vs revenue +18% | **Watch item** |
| **Tax** | Cash taxes / pre-tax income (H1) | **3.3%** (book rate 23.0%) | Future normalization risk |
| **Off-balance-sheet** | Total contractual obligations | **$650.0B**; $78.1B due within 12 months | High impact, ambiguous sign |
| **Visibility** | Deferred revenue | $25.0B; $15.2B recognized in H1 | Modest |
| **Shareholder returns** | Buybacks / dividends | **None evident**; shares +0.5% (SBC only) | Reinvestment mode |
| **Segments** | Reportable segments | **3** (North America, International, AWS); no segment financials in dataset | Info gap |
| **Insider activity** | Form 4 transactions | **DATA UNAVAILABLE — not inferable** | Unknown |
| **Data caveats** | Missing tags | Revenue (derived), equity, retained earnings, PP&E, buyback/dividend; no annual 10-K history | Verify before trading |