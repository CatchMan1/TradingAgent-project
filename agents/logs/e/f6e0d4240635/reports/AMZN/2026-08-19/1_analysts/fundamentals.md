# AMZN — Fundamental Deep Dive (as of 2026-08-19)

**Company:** Amazon.com, Inc. (`AMZN`) | **Latest filing in dataset:** Form 10-Q, period ended 2026-06-30, accepted 2026-07-31 (accn 0001018724-26-000026)
**All figures in USD millions unless noted.** All facts below are point-in-time SEC facts public by 2026-08-19.

---

## 1. Data provenance, scope and limitations (read first)

| Item | Status |
|---|---|
| Source | Point-in-time SEC facts cache (10-Q for Q2 2026, filed 2026-07-31; prior 10-Q filed 2026-04-30). Rows filtered by actual EDGAR acceptance timestamp — no look-ahead. |
| Periods available | Q2 2026, Q1 2026, H1 2026; comparatives Q2 2025, H1 2025; balance sheet snapshots 2025-12-31 and 2026-06-30; trailing-twelve-month (TTM) roll-ups ending 2026-06-30. |
| Annual statements | Requesting annual frequency **returned the same interim fact set** — the vendor snapshot contains **no FY2023–FY2025 annual comparatives**. Multi-year trend work is therefore proxied with TTM vs. prior-TTM and H1-over-H1 comparisons. Flagged, not fabricated. |
| Revenue line | The `Revenues` tag is **not present** in the extract. Revenue is **derived as `CostsAndExpenses` + `OperatingIncomeLoss`**, which reconciles exactly to Amazon's reported revenue for the 2025 comparatives (H1 2025 = $323,369M; Q2 2025 = $167,702M). Derivation is reliable. |
| Segment detail | Only `NumberOfOperatingSegments = 3` is disclosed. **No segment revenue/operating-income split** (North America / International / AWS) is in the extract — segment conclusions below are qualitative only. |
| Insider transactions | **DATA_UNAVAILABLE** — the data package has no authorized point-in-time insider-transaction archive for AMZN as of 2026-08-19. **No insider activity is inferred or fabricated.** This is a genuine information gap traders should fill from Form 4 filings directly. |
| Share price / market cap | Not provided by these tools. Valuation multiples are deliberately **not** quoted; the report gives the core-earnings base you need to apply your own price. |

---

## 2. Company profile

Amazon.com, Inc. operates three reportable segments — **North America, International, and AWS** — spanning: first-party online retail, third-party marketplace and fulfillment services, Prime subscription (video/music/gaming/logistics benefits), digital advertising, physical stores (Whole Foods), devices (Echo, Kindle, Fire), and **Amazon Web Services** (compute, storage, database, and AI infrastructure/services — Trainium/Inferentia silicon, Bedrock, SageMaker). The 2026 balance sheet confirms a company in a **capital-intensive AI/infrastructure expansion phase**, with a large and rapidly growing strategic equity-investment book alongside the operating business.

---

## 3. Income statement — Q2 and H1 2026 vs. 2025

### 3.1 Headline progression

| Metric | Q2 2026 | Q2 2025 | Δ YoY | H1 2026 | H1 2025 | Δ YoY |
|---|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | **200,606** | 167,702 | **+19.6%** | **382,125** | 323,369 | **+18.2%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 183,241 | 157,785 | +16.1% |
| Gross profit (derived) | 104,828 | 86,893 | +20.6% | 198,884 | 165,584 | +20.1% |
| Gross margin | **52.3%** | 51.8% | +50bp | **52.0%** | 51.2% | +80bp |
| Marketing | 11,698 | 11,416 | +2.5% | 22,012 | 21,179 | +3.9% |
| G&A | 2,788 | 2,965 | −6.0% | 5,375 | 5,593 | −3.9% |
| D&A | 19,988 | 15,227 | +31.3% | 38,933 | 29,489 | +32.0% |
| SBC | 6,038 | 6,534 | −7.6% | 10,070 | 10,223 | −1.5% |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 330,812 | 285,793 | +15.8% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** | **51,313** | 37,576 | **+36.6%** |
| **Operating margin** | **13.7%** | 11.4% | **+230bp** | **13.4%** | 11.6% | **+180bp** |
| Non-operating income | 53,396 | 1,686 | n.m. | 69,378 | 4,960 | n.m. |
| Pre-tax income | 80,857 | 20,857 | +288% | 120,691 | 42,536 | +184% |
| Tax expense | 18,199 | 2,678 | — | 27,759 | 7,231 | — |
| Effective tax rate | 22.5% | 12.8% | +970bp | 23.0% | 17.0% | +600bp |
| **Net income** | **62,647** | 18,164 | **+245%** | **92,902** | 35,291 | **+163%** |
| Diluted EPS | **$5.75** | $1.68 | +242% | **$8.53** | $3.27 | +161% |
| Diluted shares | ~10,895 | ~10,812 | +0.8% | ~10,891 | ~10,792 | +0.9% |

**Key read: the operating business genuinely accelerated.** Revenue growth stepped up from **+16.6% in Q1 2026** ($181,519M) to **+19.6% in Q2 2026**, while operating margin expanded 230bp and operating income rose 43%. Cost discipline is visible: marketing +2.5% and G&A −6.0% against +19.6% revenue (marketing fell to **5.8% of sales from 6.8%**), and SBC fell to **3.0% of revenue from 3.9%**. Gross margin expanded on mix (advertising/AWS/3P fees).

### 3.2 Earnings-quality bridge — this is the single most important analytical point

Reported EPS of **$5.75 (+242%)** is **not** a clean read on the business:

- **Non-operating income was $53,396M in Q2 2026** vs $1,686M a year earlier. The dominant driver is **`EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment` = $50,486M in Q2 2026** ($62,814M in H1 2026) — i.e., **non-cash mark-to-market gains on large private/non-marketable equity stakes (AI-ecosystem investments)**. Q1 2026 carried ~$12,328M of the same.
- Secondary items: unrealized gains on marketable securities $1,319M; equity securities FV-NI gains $1,300M; FX gains $227M; interest income $1,295M; partly offset by **interest expense $1,314M** and a **warrant fair-value charge of $1,449M**.
- **Approximated "core" earnings stripping investment marks** (operating income + net interest, taxed at the reported rate):

| Core estimate | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---:|---:|---:|---:|
| Operating income + net interest | 27,461 + 316-ish ≈ 27,442 | 19,740 | 51,629 | 38,670 |
| Core net income (post ~22.5%/12.8% tax) | **~21,300** | ~17,200 | **~39,800** | ~32,100 |
| Core diluted EPS | **~$1.96** | ~$1.59 | **~$3.65** | ~$2.97 |
| **Core EPS growth** | **~+23%** | — | **~+23%** | — |

**Conclusion: core EPS growth is ~23%, not +242%.** Any model, screen, or narrative using the GAAP $5.75 or the TTM $135,281M net income will **massively overstate normalized earnings power**. Conversely, the underlying operating improvement (+43% operating income) is real and impressive.

Two further quality flags:
- **Deferred tax expense $30,489M in H1 2026** (vs $518M in H1 2025) while **cash taxes paid were only $3,978M**. The gap is the non-cash tax on unrealized investment gains. TTM cash taxes paid: $6,635M. **Cash tax burden remains very light** — a positive for cash generation, but confirms reported earnings are inflated by unrealized marks.
- **Effective tax rate rising** (17.0% → 23.0% H1/H1) is a real, recurring headwind to core EPS going forward (Pillar-2/global minimum tax, jurisdictional mix).

---

## 4. Balance sheet (2026-06-30 vs. 2025-12-31)

| Line | 2026-06-30 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 78,213 | 86,810 | −9.9% |
| Marketable securities (AFS debt) | 97,900 | 45,800 | **+113.7%** |
| Accounts receivable, net | 88,092 | 67,729 | **+30.1%** |
| Inventory, net | 38,184 | 38,325 | −0.4% |
| Current assets | 249,264 | 229,083 | +8.8% |
| Non-marketable equity securities (no ready fair value) | **122,300** | 16,200 | **+655%** |
| Operating lease ROU asset | 92,743 | 86,054 | +7.8% |
| **Total assets** | **1,095,689** | 818,042 | **+33.9%** |
| Accounts payable | 147,440 | 121,909 | +20.9% |
| Accrued liabilities | 73,406 | 75,520 | −2.8% |
| Current liabilities | 241,274 | 218,005 | +10.7% |
| Long-term debt (current 3,330) | **132,995** | 68,836 | **+93.2%** |
| Finance lease liabilities | 13,451 | 12,286 | +9.5% |
| Operating lease liabilities | 96,320 | 89,252 | +7.9% |
| Deferred revenue (current + non-current) | 24,928 | 24,976 | flat |

**Observations:**

1. **Liquidity is strong but the mix shifted.** Cash fell 10% while marketable securities more than doubled → total cash + securities = **$176,113M**. Current ratio **1.03** (was 1.05) — thin, as is structurally normal for Amazon given payables-funded working capital and $20.4B of customer prepayments.
2. **Debt nearly doubled in six months.** Total debt ex-finance leases rose from $68,836M to **$132,995M** (+$64.2B), funded by **$66,998M of long-term debt issued in H1 2026** ($81,925M TTM). Leverage is still modest for the cash-flow base but the *rate of change* is the story.
3. **Net cash still positive:** cash + AFS ($176,113M) vs. debt + finance leases ($146,446M) → **~+$29.7B net cash**, down from a much larger cushion at year-end as capex/M&A absorbed it.
4. **AOCI +$38,057M** (28,230 → 66,287) in six months — a very large other-comprehensive gain, consistent with the massive unrealized revaluation of strategic holdings and unrealized AFS gains. Note FX translation *detracted* $1,563M in H1 2026 (vs +$4,849M in H1 2025) — a dollar-strength headwind.
5. **Book value accretion ≈ $140.6B in H1 2026** (net income $92.9B + APIC/SBC-related +$9.6B + OCI +$38.1B). **No buyback and no dividend**: APIC rose in line with SBC, share count rose from 10,731M to 10,783M (**+0.5% dilution**), and 10,786.3M shares were outstanding at 2026-07-22.
6. **Crucially: $122.3B — ~11% of total assets — is non-marketable equity with no readily determinable fair value.** That is the source of the earnings uplift *and* the biggest mark-to-market risk on the balance sheet.

**Working-capital flag:** receivables grew **+30.1%** vs. revenue **+19.6%** YoY (DSO ≈ **40 days**). Not yet alarming (advertising/AWS/3P billing mix), but receivables are outgrowing the top line and the allowance rose to $2,800M from $2,400M. Inventories are flat despite ~20% growth — genuinely good working-capital management.

---

## 5. Cash flow and the capex super-cycle

| Metric | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | TTM 6/26 | Prior TTM 6/25 |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash flow | **45,387** | 32,515 | **71,419** | 49,530 | **161,403** | 121,137 |
| Capex (productive assets) | **54,208** | 32,183 | **98,411** | 57,202 | **173,028** | 107,656 |
| **Free cash flow (OCF − capex)** | **(8,821)** | +332 | **(26,992)** | (7,672) | **(11,625)** | +13,481 |
| Acquisitions, net of cash | 24,359 | 1,700 | **39,767** | 1,652 | 41,956 | 4,809 |
| Net investing cash flow | (79,245) | (39,424) | (143,457) | (69,227) | (216,775) | (123,569) |
| Net financing cash flow | +10,146 | (2,539) | **+62,913** | (2,586) | +75,160 | (8,652) |
| D&A | 19,988 | 15,227 | 38,933 | 29,489 | **75,200** | 58,562 |

**Interpretation — the core debate for AMZN today:**

- **OCF quality is excellent:** +44% H1/H1 and +33% TTM/TTM, with an OCF margin of **22.6% in Q2 2026** (vs 19.4%). Cash conversion is being *helped* by light cash taxes ($6.6B TTM) and disciplined working capital.
- **But capex is exploding:** $98.4B in H1 2026 (+72% YoY), with **Q2 alone at $54.2B (+68% YoY)**, = **27.0% of Q2 revenue** (vs 19.2%). Annualizing Q2 run-rate → **~$217B of capex**, against TTM D&A of only **$75.2B**.
- **FCF is negative and worsening:** TTM **−$11.6B** vs **+$13.5B** a year ago; H1 2026 **−$27.0B**. Including acquisitions, TTM discretionary cash outflow is ~**−$53.6B**.
- **The gap is debt-funded:** +$67.0B of bonds issued in H1 2026 against negative FCF and $39.8B of M&A. Interest expense is already responding: **$1,314M in Q2 2026 (+155% YoY)**; H1 $2,114M (+100%).
- **The depreciation lag is the forward margin risk.** D&A is only **43% of TTM capex** (37% in Q2). As the AI/data-center build depreciates (multi-year useful lives), **D&A growth should keep running at 30%+ annually**, mechanically compressing operating margin unless revenue/mix offsets it. Q2 2026 already shows D&A at **10.0% of revenue vs 9.1%** a year ago.
- **Interest coverage remains comfortable:** annualized Q2 operating income ~$109.8B vs. annualized interest ~$5.3B → **~21x**. Lease-adjusted debt (incl. $96.3B operating leases) / annualized EBITDA (~$178B) ≈ **1.4x**. Not a solvency story; a *capital-allocation and duration* story.

---

## 6. Contractual obligations and off-balance-sheet commitments (at 2026-06-30)

| Obligation | Total | Due next 12M |
|---|---:|---:|
| Total contractual obligations | **650,034** | **78,084** |
| Operating leases (undiscounted) | 116,350 | 14,765 |
| Finance leases (undiscounted) | 16,660 | 1,775 |
| Purchase/other commitments | — | 21,450 |
| Unrecognized SBC (not a cash obligation) | 24,800 | — |

Obligations rose from an in-quarter trajectory of ~$46.5B due-in-remainder-of-year (Mar-2026 disclosure) to **$42.8B at Jun-30** for the remainder — but the *total* stack of **$650B** (mostly content, energy, cloud capacity and purchase commitments tied to the AI build) is the key forward cost lever. Compare it to TTM OCF of $161B: the committed multi-year spend is ~4x annual operating cash generation. Operating lease discount rate ticked up to **3.9%** from 3.7%.

---

## 7. Insider transactions

**Not available.** The data package explicitly has no authorized, point-in-time insider-transactions archive for `AMZN` as of 2026-08-19. I will not estimate or infer insider behavior. Traders should source Form 4s directly (technically required within two business days) — this is a material blind spot in the current evidence set, particularly for a quarter in which a ~$50B non-cash mark-up on private holdings was booked.

---

## 8. Bull case vs. bear case — evidence-based

### Bull (supported by the data)
1. **Operating momentum inflected higher**: revenue growth +16.6% → +19.6% sequentially, operating income +43% YoY, margin +230bp to 13.7%. Cost leverage is broad (marketing −170bp of sales, G&A down outright).
2. **Operating cash generation is compounding fast**: TTM OCF $161.4B (+33%), Q2 OCF margin 22.6%, cash taxes only $6.6B TTM.
3. **Still net-cash** (~$29.7B) and leverage ~1.4x lease-adjusted EBITDA despite a historic borrowing spree — the balance sheet can carry this build.
4. **$122.3B strategic equity book + $97.9B liquid securities** = an embedded, appreciating option on the AI ecosystem, plus genuine financing capacity.
5. **Shareholder dilution minimal**; SBC down as % of revenue; no buyback means 100% of retained economics recycled into the build.

### Bear (supported by the data)
1. **Negative and deteriorating FCF** (TTM −$11.6B), capex at **27% of revenue**, and a **$650B** contractual obligation stack. If AI monetization lags, this is a multi-year cash sink.
2. **Earnings quality**: ~$62.8B of H1 2026 pre-tax income is a **non-cash mark-up on Level-3-style private stakes**. One valuation reset in private AI markets hits **both** the P&L and the $122.3B asset simultaneously. Headline EPS is not repeatable.
3. **Depreciation catch-up** (D&A 43% of TTM capex) is a structural margin headwind over the next 4–8 quarters.
4. **Rising effective tax rate** (17.0% → 23.0%) pressures core EPS growth regardless of operations.
5. **Receivables +30% vs revenue +20%**; allowance up 17% — early working-capital warning.
6. **Insider signal unavailable** — no ability to confirm management conviction during the largest capital-deployment phase in company history.

---

## 9. Actionable insights for traders

1. **Rebase every valuation on core earnings, not GAAP.** Use **~$1.96 Q2 2026 / ~$3.65 H1 2026 core EPS** (≈ +23% YoY) and **~$21–22B core quarterly net income**, not $62.6B net income / $5.75 EPS. Anyone screening AMZN on reported P/E is looking at a multiple roughly one-third too low. Conversely, screens flagging "EPS +245%" are mis-reading the driver.
2. **Treat the Q3 2026 print (~late Oct 2026) as a binary-ish catalyst**, with four specific swing factors: (a) capex guidance vs. the ~$217B annualized Q2 run-rate; (b) revenue growth holding ≥19%; (c) operating margin holding ≥13% *despite* D&A +30%; (d) any mark-to-market **reversal** on the private equity book.
3. **Position sizing should reflect a levered AI-capex + AI-valuation double exposure.** AMZN now has a beta to *private* AI valuations that it never had before — $122.3B of non-marketable equity (11% of assets) plus $62.8B of P&L marks in one half-year. Hedging/sizing has to account for a scenario in which a private-AI valuation markdown removes both EPS *and* book value at once.
4. **Monitor the funding mix quarterly.** Watch: (i) long-term debt issuance pace ($67.0B in H1 alone), (ii) interest expense (running +155% YoY), (iii) any signs of commercial-paper/short-term reliance ($15.4B ST proceeds, $15.7B repaid in H1). A pivot from debt-funded to equity- or asset-sale-funded capex would be a bearish confirmation of FCF strain; a shift to internally funded capex would be a strong bullish tell.
5. **Track the depreciation ratio as the leading margin indicator.** D&A/revenue went 9.1% → 10.0% YoY. If it crosses ~11% while revenue growth decelerates below ~15%, the margin-expansion story inverts — that is the cleanest early exit signal available in the data.
6. **Watch receivables and deferred revenue as the demand-quality check.** AR +30% vs revenue +20% bears monitoring; deferred revenue (contract liabilities) was *flat* at ~$24.9B, and $15.2B of it was recognized as H1 2026 revenue — i.e., the backlog cushion is not growing. If AR keeps outrunning revenue while deferred revenue stalls, question the durability of the growth.
7. **Fill the insider data gap manually before sizing any position** — this is the one dimension of the evidence set that is entirely missing, and it matters most precisely when a company is committing $650B of contractual obligations and booking $63B of non-cash gains.
8. **For income/defensive mandates: there is nothing here.** No dividend, no buyback, +0.5% share count creep in six months, negative FCF. This is a pure growth/aggressive-allocation instrument.

---

## 10. Key points summary

| Category | Metric | Value | YoY / Change | Read |
|---|---|---:|---:|---|
| **Growth** | Revenue Q2 2026 (derived) | $200,606M | **+19.6%** | Acceleration from +16.6% in Q1 |
| | Revenue H1 2026 | $382,125M | +18.2% | Broad-based; no segment split available |
| **Profitability** | Operating income Q2 2026 | $27,461M | **+43.2%** | Genuine operating leverage |
| | Operating margin Q2 2026 | **13.7%** | +230bp | Cost discipline in marketing/G&A |
| | Gross margin Q2 2026 | 52.3% | +50bp | Mix shift to ads/AWS/3P |
| **Earnings quality** | Reported net income Q2 2026 | $62,647M | +245% | **Inflated by non-cash marks** |
| | Reported diluted EPS Q2 2026 | $5.75 | +242% | Not repeatable |
| | **Core diluted EPS Q2 2026 (est.)** | **~$1.96** | **~+23%** | True earnings power |
| | Non-operating income H1 2026 | $69,378M | vs $4,960M | $62,814M private-equity mark-up |
| | Effective tax rate H1 2026 | 23.0% | +600bp | Recurring headwind |
| | Cash taxes paid TTM | $6,635M | — | Very light cash tax burden |
| **Cash flow** | OCF Q2 2026 / TTM | $45,387M / **$161,403M** | +39.6% / +33% | Strong core cash engine |
| | Capex H1 2026 / TTM | $98,411M / **$173,028M** | +72% / +61% | Capex = **27.0%** of Q2 revenue |
| | **Free cash flow TTM** | **(11,625)M** | from +13,481M | **Negative and widening** |
| | Acquisitions H1 2026 | $39,767M | vs $1,652M | Major M&A step-up |
| **Balance sheet** | Total assets | $1,095,689M | **+33.9% in 6 mo** | Driven by investments + capex |
| | Non-marketable equity securities | **$122,300M** | +655% (from $16,200M) | ~11% of assets; mark-to-market risk |
| | Total debt (ex-finance leases) | $132,995M | **+93.2%** in 6 mo | Funding the build |
| | Cash + marketable securities | $176,113M | +32.7% | Net cash ≈ **+$29.7B** |
| | Net new long-term debt H1 2026 | +$66,998M issued | vs $746M | Historic issuance |
| | Interest expense Q2 2026 | $1,314M | **+155%** | Coverage still ~21x |
| | Current ratio | 1.03 | from 1.05 | Thin, structurally normal |
| | Contractual obligations | **$650,034M** | $78,084M due <12M | ~4x TTM OCF |
| | Buyback / dividend | **None** | Shares +0.5% in 6 mo | Full reinvestment posture |
| **Tax/cash nuance** | Deferred tax expense H1 2026 | $30,489M | vs $518M | Non-cash tax on unrealized gains |
| **Insider** | Form 4 activity | **DATA UNAVAILABLE** | — | **Evidence gap — source externally** |
| **Analytical caveats** | Annual FY2023–25 statements | **Not in dataset** | — | Use H1/TTM comparisons only |
| | Segment P&L split | **Not in dataset** | — | 3 segments confirmed only |

**Bottom line:** `AMZN`'s *operating* fundamentals are the strongest in the dataset — 19.6% growth, 13.7% operating margin, +43% operating income, +33% TTM operating cash flow, and a still-net-cash balance sheet. But the *reported* numbers (+245% EPS) are dominated by a $62.8B non-cash mark-up on private AI stakes, while **FCF is –$11.6B TTM and capex is running at ~27% of revenue funded by $67B of new debt**. The trade is therefore a bet on continued operating leverage outrunning a rising depreciation and interest burden, without a valuation reset on a $122.3B private-equity book — and the insider-confirmation leg of that thesis cannot be verified with the tools available here.