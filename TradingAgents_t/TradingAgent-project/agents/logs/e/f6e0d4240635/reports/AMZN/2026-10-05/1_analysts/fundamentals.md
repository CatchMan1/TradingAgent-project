# AMZN — Fundamental Research Report
**Analysis date: 2026-10-05 | Latest fiscal data: quarter ended 2026-06-30 | Primary source: Form 10-Q filed 2026-07-31 (accn 0001018724-26-000026); prior 10-Q filed 2026-04-30 (accn 0001018724-26-000014)**

---

## 1. Bottom line

AMZN's fundamentals show **two very different companies layered on top of each other**:

1. **A core retail/AWS/ads business that is accelerating and expanding margins hard** — revenue +19.6% y/y in Q2 2026 (derived), operating income +43.2% y/y, operating margin 13.7% vs 11.4%, and this *despite* a ~90bp headwind from surging depreciation.
2. **An AI-infrastructure build-out so large it has turned the company free-cash-flow negative and nearly doubled gross debt in six months** — TTM capex $173.0B (~27% of Q2 revenue), TTM FCF **–$11.6B**, total debt $132.2B vs $68.4B at 12/31/25, plus **$650.0B of contractual (mostly purchase) obligations**.

Headline EPS is *massively* flattered by non-cash marks: **~$63B of 1H26 pre-tax income (~52%) came from upward revaluation of non-marketable equity securities** (the carrying value jumped from $16.2B to **$122.3B**). Stripping that out, 1H26 core EPS is ~**$4.10 vs $3.27 (+25%)**, not the reported +161%.

**Actionable read:** the operating engine is genuinely strong and under-appreciated beneath the noisy headline print; the risk is concentrated in (a) capex intensity and funding, (b) the sustainability of an AI-valuation-driven $122B asset, and (c) negative FCF into a rising rate/leverage backdrop. The next hard catalyst is the **Q3 2026 report (late Oct 2026)** — the company is in its pre-earnings blackout, consistent with the absence of insider filings.

---

## 2. Company profile & data provenance

| Item | Detail |
|---|---|
| Company | Amazon.com, Inc. (`AMZN`) |
| Reporting segments | **3** (North America, International, AWS — per `NumberOfOperatingSegments` = 3) |
| Latest filing | 10-Q for quarter ended 2026-06-30, filed/accepted **2026-07-31** |
| Prior filing | 10-Q for quarter ended 2026-03-31, filed 2026-04-30 |
| Shares outstanding | **10,783.0M** (2026-06-30); 10,786.3M as of 2026-07-22 cover date |
| Shares issued | 11,298M; treasury ~515M |
| Insider transactions | **DATA UNAVAILABLE** — vendor has no authorized point-in-time insider archive for AMZN. No insider activity is inferred or fabricated. |

**Important caveats on this dataset:**
- No **new filing occurred in the week ending 2026-10-05**. The most recent authoritative disclosure is the Q2 10-Q from 2026-07-31. Everything below is a point-in-time read of that filing.
- The vendor returns a **flat SEC-fact list**, not a clean multi-year model. There is **no direct `Revenues` tag, no gross profit, no segment revenue, no full-year 2023/2024/2025 annual statements, and no insider data**. I therefore **derive revenue from the identity `Revenue = CostsAndExpenses + OperatingIncomeLoss`**, which reconciles precisely to known AMZN results for 2025 — so the derived figures are reliable. Where I estimate, it is labeled.

---

## 3. Income statement — derived quarterly and year-to-date

### 3.1 Derived revenue and operating results

| $M | Q2 2026 | Q2 2025 | y/y | 1H 2026 | 1H 2025 | y/y |
|---|---:|---:|---:|---:|---:|---:|
| **Revenue (derived)** | **200,606** | **167,702** | **+19.6%** | **382,125** | **323,369** | **+18.2%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 183,241 | 157,785 | +16.1% |
| COGS % of revenue | 47.7% | 48.2% | –45bp | 48.0% | 48.8% | –83bp |
| Other operating costs (derived) | 77,367 | 67,722 | +14.2% | 147,571 | 128,008 | +15.3% |
| Other opex % of revenue | 38.6% | 40.4% | –181bp | 38.6% | 39.6% | –97bp |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 330,812 | 285,793 | +15.8% |
| **Operating income** | **27,461** | **19,171** | **+43.2%** | **51,313** | **37,576** | **+36.6%** |
| **Operating margin** | **13.69%** | **11.43%** | **+226bp** | **13.43%** | **11.62%** | **+181bp** |
| Non-operating income | 53,396 | 1,686 | n.m. | 69,378 | 4,960 | n.m. |
| Pre-tax income | 80,857 | 20,857 | +288% | 120,691 | 42,536 | +184% |
| Income tax | 18,199 | 2,678 | +580% | 27,759 | 7,231 | +284% |
| Effective tax rate | 22.5% | 12.8% | +970bp | 23.0% | 17.0% | +600bp |
| **Net income** | **62,647** | **18,164** | **+245%** | **92,902** | **35,291** | **+163%** |
| Diluted EPS | **$5.75** | **$1.68** | +242% | **$8.53** | **$3.27** | +161% |
| Diluted shares (derived) | ~10,895M | ~10,812M | +0.8% | ~10,891M | ~10,793M | +0.9% |

**TTM (Jul-2025 → Jun-2026):** net income **$135,281M**; OCF **$161,403M**; D&A **$75,200M**; capex **$173,028M**; SBC **~$20.6B** (1H26 $10.07B + implied 2H25).

### 3.2 Where the margin expansion comes from (Q2 2026)

| Expense line | Q2 2026 | % rev | Q2 2025 | % rev | Δ (bp) |
|---|---:|---:|---:|---:|---:|
| Cost of goods & services | 95,778 | 47.7% | 80,809 | 48.2% | –45 |
| Marketing | 11,698 | 5.83% | 11,416 | 6.81% | **–98** |
| G&A | 2,788 | 1.39% | 2,965 | 1.77% | **–38** |
| Stock-based comp | 6,038 | 3.01% | 6,534 | 3.90% | **–89** |
| Depreciation & amortization | 19,988 | 9.97% | 15,227 | 9.08% | **+89 (headwind)** |
| Residual (fulfillment, tech, stores, etc.) | 36,855 | 18.4% | 31,580 | 18.8% | –45 |
| **Total costs** | **173,145** | **86.3%** | **148,531** | **88.6%** | **–226** |

**Key insight:** margin expansion is *high quality*. Amazon got 226bp of operating leverage while absorbing an **89bp depreciation headwind**. G&A actually **declined in absolute dollars** (–$177M), and SBC fell 130bp as a share of revenue in two quarters. This is a business harvesting scale, not one buying growth with opex.

Depreciation is the leading indicator that matters: Q2 2026 D&A $19,988M vs $15,227M (+31.3%), and 1H26 $38,933M vs $29,489M (+32.0%). With $173B of TTM capex landing, D&A will keep compounding at ~30%+ — that is the structural drag on 2027 margins.

---

## 4. Earnings quality — the single most important adjustment

Non-operating income of **$69,378M in 1H26** ($53,396M in Q2 alone) is almost entirely **non-cash revaluation gains** on non-marketable equity securities:

| Driver ($M) | Q2 2026 | 1H 2026 | 1H 2025 |
|---|---:|---:|---:|
| Upward price adjustment, equity securities w/o readily determinable FV | **50,486** | **62,814** | 86 |
| Equity securities FV-NI gain | 1,300 | 454 | 188 |
| Fair value adjustment of warrants | (1,449) | (1,051) | (212) |
| Interest income | 1,295 | 2,430 | 2,151 |
| Interest expense | (1,314) | (2,114) | (1,057) |
| FX transaction gain | 227 | 387 | 68 |
| **Reported non-operating income** | **53,396** | **69,378** | **4,960** |

**Pro-forma "core" earnings (my calculation, clearly an estimate):**

| | Q2 2026 | Q2 2025 | y/y | 1H 2026 | 1H 2025 | y/y |
|---|---:|---:|---:|---:|---:|---:|
| Reported pre-tax | 80,857 | 20,857 | | 120,691 | 42,536 | |
| Less: equity revaluation + FV gains, net of warrants | (50,337) | (181) | | (62,217) | (62) | |
| **Core pre-tax** | **~30,520** | **~20,676** | **+47.6%** | **~58,474** | **~42,474** | **+37.7%** |
| After tax @ effective rate | 23,653 | 18,031 | | 45,025 | 35,253 | |
| **Core net income** | **~23,650** | **~18,030** | **+31.2%** | **~45,030** | **~35,250** | **+27.7%** |
| **Core diluted EPS** | **~$2.17** | **~$1.67** | **+30%** | **~$4.13** | **~$3.28** | **+26%** |

**So: headline EPS +242%, core EPS ~+30%.** Still an excellent number — but traders must not capitalize $5.75 as recurring. Roughly **~60% of Q2 EPS and ~52% of 1H EPS was a mark-to-model gain on a private AI asset**, not cash.

**Sensitivity:** each $10B of further revaluation ≈ **$0.71 of EPS** (after tax ~$7.8B / 10.9B shares). A 20% markdown of the $122.3B carrying value ≈ **$24.5B pre-tax, ~$2.25 EPS** — a ~7% hit to a "core + mark" run-rate EPS of ~$11–12.

**Tax quality note:** 1H26 deferred tax expense was **$30,489M** against total tax expense of $27,759M — i.e., **current cash taxes were a net benefit**; cash taxes paid were only **$3,978M**. TTM deferred tax expense **$41,441M** vs TTM cash taxes paid **$6,635M**. Reported operating cash flow is therefore **inflated by a very large non-cash deferred-tax add-back**. Adjusting TTM OCF for deferred taxes: **$161.4B – $41.4B ≈ $120B**, which is **below TTM capex of $173.0B**. This is the cleanest single argument that AMZN's cash generation, as currently reported, is weaker than the headline.

---

## 5. Balance sheet — size, liquidity, and a $106B asset re-rating

| $M | 2026-06-30 | 2025-12-31 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 78,213 | 86,810 | –8,597 |
| Available-for-sale debt securities | 97,900 | 45,800 | **+52,100** |
| Accounts receivable, net | 88,092 | 67,729 | **+20,363** |
| Inventory, net | 38,184 | 38,325 | –141 |
| **Total current assets** | **249,264** | **229,083** | +20,181 |
| **Non-marketable equity securities** | **122,300** | **16,200** | **+106,100** |
| Operating lease ROU assets | 92,743 | 86,054 | +6,689 |
| **Total assets** | **1,095,689** | **818,042** | **+277,647 (+33.9%)** |
| Accounts payable | 147,440 | 121,909 | +25,531 |
| Accrued liabilities | 73,406 | 75,520 | –2,114 |
| Current portion of LT debt | 3,330 | 2,748 | +582 |
| Current operating lease liability | 13,745 | 12,655 | +1,090 |
| **Total current liabilities** | **241,274** | **218,005** | +23,269 |
| Long-term debt, noncurrent | **128,894** | **65,648** | **+63,246** |
| Noncurrent operating lease liability | 82,575 | 76,597 | +5,978 |
| Noncurrent finance lease liability | 11,763 | 10,742 | +1,021 |
| Deferred revenue (current + noncurrent) | 24,928 | 25,000 | –72 |
| Common stock / APIC | 113 / 149,619 | 112 / 140,024 | +9,596 |
| Accumulated OCI | 66,287 | 28,230 | +38,057 |

**Reconciliation of the $277.6B asset increase in six months (my bridge):**

| Component | $B |
|---|---:|
| Non-marketable equity securities revaluation/step-up | +106.1 |
| Available-for-sale securities build | +52.1 |
| Net PP&E (capex $98.4B less depreciation $38.9B) | ~+59.5 |
| Acquisitions (incl. goodwill/intangibles) | +39.8 |
| Accounts receivable | +20.4 |
| Cash drawdown | –8.6 |
| Other (leases, tax assets, etc.) | ~+8.3 |
| **Total** | **~+277.6** |

This is a **coherent and highly informative bridge**: Amazon spent ~$140B of cash on capex + M&A in six months, re-rated a private AI stake by $106B, and funded the difference with **$64.5B of net new debt**.

**Liquidity / leverage:**
- Current ratio: **1.03x** (249.3 / 241.3) — thin, and structurally thin by design given negative working capital.
- Cash + AFS securities: **$176.1B**; total debt **$132.2B** + finance leases **$13.5B** = **$142.5B** → **net cash ~$33.6B** *before* $96.3B of operating lease liabilities.
- Including operating leases ($96.3B PV; $116.4B undiscounted), total obligations are **~$239B**.
- **Note:** cash ($78.2B) + AFS ($97.9B) + AR ($88.1B) + inventory ($38.2B) = $302.4B, which exceeds reported current assets of $249.3B. The AFS balance likely includes noncurrent maturities, or the vendor's current-asset tag is incomplete. Treat the $176.1B cash+securities figure as gross liquidity, not all current.

**Equity:** retained earnings and other noncurrent liabilities were not returned in this dataset, so total stockholders' equity is not directly computable. Reported equity *components* are common stock $113M, APIC $149.6B, AOCI $66.3B. Scaling from known end-2024 book equity (~$286B) plus FY2025 net income, 1H26 net income of $92.9B and $9.6B of APIC additions, **book equity is plausibly in the ~$470–520B range** (estimate, not reported) — meaning roughly $575–625B of total liabilities against $1.096T of assets. Leverage remains moderate on a book basis; the concern is the **rate of change**, not the level.

---

## 6. Cash flow — the core tension

| $M | Q2 2026 | Q2 2025 | 1H 2026 | 1H 2025 | TTM (Jul25–Jun26) |
|---|---:|---:|---:|---:|---:|
| Operating cash flow | 45,387 | 32,515 | 71,419 | 49,530 | **161,403** |
| Capex (productive assets) | (54,208) | (32,183) | (98,411) | (57,202) | **(173,028)** |
| **Free cash flow** | **(8,821)** | **+332** | **(26,992)** | **(7,672)** | **(11,625)** |
| Acquisitions, net of cash | (24,359) | (1,700) | (39,767) | (1,652) | **(41,956)** |
| **FCF after M&A** | **(33,180)** | **(1,368)** | **(66,759)** | **(9,324)** | **(53,581)** |
| Investing cash flow | (79,245) | (39,424) | (143,457) | (69,227) | (216,775) |
| Financing cash flow | +10,146 | (2,539) | +62,913 | (2,586) | **+75,160** |

**Capex intensity:**
- Q2 2026: **27.0% of revenue** (54,208 / 200,606)
- 1H 2026: **25.8% of revenue** (98,411 / 382,125)
- 1H 2025: 17.7% — so capex intensity rose **~810bp y/y**
- Implied 2H 2025 capex: $74.6B (~$37B/qtr) → **Q2 2026's $54.2B is a ~46% step-up in run-rate in three quarters**

**Funding sources (TTM):**
- Long-term debt issued: **$81,925M** (vs $746M in the prior-year period — a **110x** increase)
- Short-term debt issued: **$20,798M**
- LT repayments: $5,022M; ST repayments: $20,634M
- Net debt raised ≈ **$75.2B financing inflow**

**This is the crux:** AMZN is now funding a self-described AI capacity build with debt while running negative FCF. That is a legitimate strategic choice if returns on that capex exceed the cost of capital — but it removes the "fortress, self-funding" attribute that historically justified a premium multiple, and it makes the stock more sensitive to credit conditions and to any disappointment in AWS/AI demand.

---

## 7. Debt, leases, and off-balance-sheet commitments

| $M | 2026-06-30 | 2025-12-31 | Change |
|---|---:|---:|---:|
| Long-term debt (total, incl. current) | **132,995** | 68,836 | **+64,159 (+93%)** |
| — of which noncurrent | 128,894 | 65,648 | +63,246 |
| — of which current | 3,330 | 2,748 | +582 |
| Finance lease liabilities | 13,451 | 12,286 | +1,165 |
| Operating lease liabilities (PV) | 96,320 | 89,252 | +7,068 |
| **Total debt + leases** | **242,766** | **170,374** | **+72,392** |
| Interest expense (1H) | 2,114 | 1,057 | **+100%** |
| Annualized interest / avg total debt | ~3.2% | — | low coupon, IG |

**Contractual obligations: $650,034M** as of 2026-06-30 — overwhelmingly AWS capacity, energy, and silicon purchase commitments:

| Bucket | $M |
|---|---:|
| Next twelve months | 78,084 |
| Year two | 53,406 |
| Year three | 46,767 |
| Year four | 42,219 |
| **Subtotal, years 1–4** | **220,476** |
| Beyond year four | ~429,558 (derived) |
| *Memo: remainder of fiscal 2026* | *42,752* |

**Comparison point:** the 12-month bucket alone ($78.1B) is **48% of TTM operating cash flow** ($161.4B) and **214% of TTM FCF-adjusted OCF** (~$120B). Layering $78B of purchase obligations + $54B/qtr of capex + $2–4B/qtr of interest on top of flat-to-declining FCF is why the debt stack doubled.

Other structural items to note:
- Unrecognized SBC: **$24.8B** — a future expense overhang (~2.4 years of current SBC run-rate).
- Dilution: diluted shares +0.8–0.9% y/y — modest, but persistent.
- Operating lease discount rate rose from 3.7% → **3.9%**, a small but real sign of a higher-rate environment.

---

## 8. Historical context & trend read

Because the vendor supplied only the current and prior-year comparative periods (no FY2023/2024 annual statements), the trend picture below is built from the point-in-time tags that are available:

| Metric | 1H 2025 | FY 2025 (implied 2H) | 1H 2026 | Direction |
|---|---:|---:|---:|---|
| Revenue | 323,369 | ~384,000 (derived/est.) | 382,125 | **Reaccelerating** — 1H26 revenue ≈ all of 2H25 |
| Operating margin | 11.62% | — | 13.43% | **+181bp** |
| D&A | 29,489 | 36,267 (derived) | 38,933 | **+32% y/y** |
| Capex | 57,202 | 74,617 (derived) | 98,411 | **+72% y/y** |
| OCF | 49,530 | 89,984 (derived) | 71,419 | +44% y/y |
| FCF | (7,672) | (3,953) (derived) | (26,992) | **Deteriorating sharply** |
| Debt | ~68,400 (12/31/25) | — | 132,995 | **+94% in 6 months** |
| Non-marketable equity | ~16,200 (12/31/25) | — | 122,300 | **+$106B re-rating** |
| Total assets | 818,042 (12/31/25) | — | 1,095,689 | **+33.9% in 6 months** |

**The pattern:** revenue growth reaccelerated to high-teens, operating leverage is real and broadening, but the capital intensity of the AI build has moved the company from "cash machine" to "cash consumer." That is the regime change traders need to price.

---

## 9. Insider transactions

**No data.** The vendor's news archive contains no authorized, point-in-time insider-transaction record for `AMZN` as of 2026-10-05, and I will not infer or fabricate Form 4 activity. Contextually, the absence is unremarkable: AMZN's Q3 2026 results are due in late October, and the company is inside its customary pre-earnings blackout window, which suppresses discretionary insider trades. **Treat insider signal as unavailable, not as bullish or bearish.**

---

## 10. Actionable insights for traders

**Bull case (evidence-based):**
1. **Core operating momentum is accelerating, not decelerating.** Q2 revenue +19.6%, op income +43.2%, op margin 13.7%. 1H26 revenue ($382.1B) already equals all of 2H25. Growth reaccelerated from ~11% in 2025 to ~18–20% now.
2. **Margin expansion is structural and broad-based.** –45bp COGS, –98bp marketing, –38bp G&A, –89bp SBC, all while absorbing +89bp of depreciation. G&A *fell in absolute dollars*.
3. **Core EPS growth of ~+30% is being masked by a noisy headline.** The market may be mis-modeling the "quality" of the Q2 beat in either direction; the durable number is core EPS ~$2.17/qtr, ~$8.6–8.8 annualized and rising.
4. **Off-balance-sheet demand signal is enormous.** $650B of contractual obligations — largely AWS capacity/energy/silicon — is management effectively pre-committing capital against demand it can see. That is a credible forward revenue indicator for AWS through 2030.
5. **The $122.3B equity stake is an unmarked optionality lever.** At $122.3B on the balance sheet vs $16.2B six months ago, it is ~11% of total assets. Any IPO/monetization event is a hard catalyst.

**Bear case (evidence-based):**
1. **Free cash flow is negative on every recent measure.** TTM FCF –$11.6B; FCF after M&A –$53.6B; 1H26 FCF –$27.0B. Capex is 27% of revenue and still stepping up ($54.2B in Q2 vs ~$37B/qtr in 2H25).
2. **Debt nearly doubled in six months** ($68.4B → $133.0B), with $82B of LT issuance TTM. Interest expense doubled y/y (+155% in Q2). Leverage inflection is real.
3. **~52% of 1H26 pre-tax income was a non-cash mark.** Mark-to-model private AI valuations can reverse; a 20% markdown is ~$2.25 of EPS.
4. **Cash-flow quality is weaker than reported.** TTM deferred tax expense $41.4B vs cash taxes $6.6B means OCF carries a large non-cash add-back; adjusted TTM OCF of ~$120B is below capex.
5. **$78.1B due within 12 months** in purchase obligations, against flat-to-negative FCF — the funding treadmill continues.

**What to watch (rank-ordered):**
| # | Catalyst / metric | Why it matters |
|---|---|---|
| 1 | **Q3 2026 results (late Oct 2026)** | First read on whether op margin holds >13% with D&A now running ~$20B/qtr |
| 2 | **2027 capex guide** | Determines whether FCF inflects or the debt path steepens |
| 3 | **AWS revenue growth & backlog conversion** | Validates the $650B contractual obligation book |
| 4 | **Any further non-marketable equity revaluation / markdown** | ±$0.71 EPS per $10B |
| 5 | **Debt issuance cadence & credit rating actions** | The marginal buyer now cares about the balance sheet |
| 6 | **Effective tax rate** | 22.5% in Q2 vs 12.8% — a 970bp headwind that persists |
| 7 | **Depreciation trajectory** | +31% y/y and compounding; the main 2027 margin risk |

**Positioning logic:** the setup favors **owning the operating story while hedging the balance-sheet/FCF story**. Concretely: the core business supports a rising earnings base (~$8.6–9.0 annualized core EPS and growing ~25–30%), but the negative-FCF/rising-leverage combination caps multiple expansion and raises drawdown risk on any AI-sentiment wobble. A trader who is bullish should prefer structures that are paid on operating margin/AWS growth rather than on headline EPS, precisely because ~half of headline EPS is a mark. A trader who is bearish should focus on the **FCF/leverage inflection** rather than on the income statement, which currently looks too good to short on its face.

**Fair-value framing (no price data was provided by the tools, so multiples cannot be computed):** the tools returned no share price, market cap, or consensus estimates. I therefore cannot state P/E or EV/EBITDA. On fundamentals alone, the relevant anchors are: core EPS run-rate ~$8.6–9.0 (annualized 1H26 core, before any 2H growth), reported TTM EPS ~$12.4, book equity ~$470–520B (est.), and net debt ~$0.0–35B depending on treatment of AFS and leases.

---

## 11. Explicit data gaps (material to the analysis)

1. **No `Revenues` tag** — revenue derived as `CostsAndExpenses + OperatingIncomeLoss`; reconciled exactly to known Q2/1H 2025 actuals, so reliable, but technically derived.
2. **No segment data** — only `NumberOfOperatingSegments = 3`. Cannot separate AWS vs North America vs International revenue, margin, or capex. **This is the biggest missing piece** for an AI-capex thesis.
3. **No annual history (FY2023/FY2024/FY2025)** — vendor returns the same facts for `annual` and `quarterly` requests. Multi-year CAGR/trend analysis is not possible from this dataset.
4. **No retained earnings / total equity / other noncurrent liabilities tags** — total equity must be estimated.
5. **No insider transactions** — explicitly unavailable; not inferred.
6. **No price, market cap, valuation multiples, consensus, or guidance data** — no valuation conclusion is possible.
7. **No Q3 2026 data** — the analysis predates the Q3 print; all figures are as of 2026-06-30.

---

## 12. Summary table

| Category | Metric | Value | Read |
|---|---|---:|---|
| **Scale** | Total assets (6/30/26) | $1,095.7B | +33.9% in 6 months |
| | TTM revenue (derived/est.) | ~$765B | High-teens growth |
| | Shares outstanding | 10,783M | +0.5% in 6 months |
| **Growth** | Q2 2026 revenue (derived) | $200.6B | **+19.6% y/y** |
| | 1H 2026 revenue (derived) | $382.1B | **+18.2% y/y** |
| | Q2 2026 operating income | $27.5B | **+43.2% y/y** |
| **Margins** | Q2 2026 operating margin | **13.69%** | +226bp y/y |
| | 1H 2026 operating margin | 13.43% | +181bp y/y |
| | COGS % of revenue | 47.7% | –45bp y/y |
| | Marketing % of revenue | 5.83% | –98bp y/y |
| | SBC % of revenue | 3.01% | –89bp y/y |
| | D&A % of revenue | 9.97% | **+89bp (headwind)** |
| **Profit** | Q2 2026 net income | $62.6B | +245% y/y |
| | Q2 2026 diluted EPS | $5.75 | +242% y/y |
| | **Q2 2026 core EPS (est.)** | **~$2.17** | **~+30% y/y** |
| | 1H 2026 EPS / core EPS (est.) | $8.53 / ~$4.13 | +161% / ~+26% |
| | TTM net income | $135.3B | — |
| | Effective tax rate (Q2) | 22.5% | +970bp y/y |
| **Earnings quality** | Equity revaluation gains, 1H26 | **$62.8B** | **~52% of pre-tax income** |
| | Non-marketable equity carrying value | **$122.3B** | from $16.2B at 12/31/25 |
| | EPS sensitivity per $10B revaluation | ~$0.71 | — |
| **Cash flow** | TTM operating cash flow | $161.4B | +33% y/y |
| | TTM deferred tax expense vs cash taxes paid | $41.4B vs $6.6B | OCF is flattered |
| | **TTM free cash flow** | **–$11.6B** | **Negative** |
| | FCF after acquisitions (TTM) | –$53.6B | — |
| | 1H 2026 FCF | –$27.0B | vs –$7.7B in 1H25 |
| **Capex** | TTM capex | **$173.0B** | — |
| | Q2 2026 capex | $54.2B | **27.0% of revenue** |
| | 1H 2026 capex | $98.4B | 25.8% of revenue (vs 17.7%) |
| **Balance sheet** | Cash + AFS securities | $176.1B | Gross liquidity |
| | Total debt (incl. current) | **$133.0B** | **+93% since 12/31/25** |
| | Finance leases | $13.5B | +9.5% |
| | Operating leases (PV) | $96.3B | +7.9% |
| | Net debt position | ~–$33.6B net cash | Before $96.3B op leases |
| | Current ratio | 1.03x | Thin by design |
| **Obligations** | Total contractual obligations | **$650.0B** | Largely AWS capacity/energy/silicon |
| | Due next 12 months | $78.1B | = 48% of TTM OCF |
| | Due years 2–4 | $142.4B | — |
| | Beyond year 4 | ~$429.6B | — |
| | Unrecognized SBC | $24.8B | Future expense overhang |
| **Leverage cost** | 1H 2026 interest expense | $2.1B | **+100% y/y** |
| | Q2 2026 interest expense | $1.31B | **+155% y/y** |
| **Insider** | Form 4 activity | **Unavailable** | Not inferred |
| **Next catalyst** | Q3 2026 earnings | Late Oct 2026 | Pre-blackout now |

---

**Bottom line for `AMZN`:** this is a **high-quality operating turnaround financed by a very large, debt-funded AI bet**. The income statement is strong at the operating line and spectacular at the bottom line — but ~half the bottom line is a non-cash mark and free cash flow is negative. Traders should anchor on **core operating margin (~13.4–13.7%) and core EPS (~$2.17/qtr, ~+30% y/y)**, monitor **capex intensity (27% of revenue) and the $650B obligation book**, and treat the **$122.3B private AI stake** as both the largest source of upside optionality and the largest single source of mark-to-model downside risk. Insider flow gives no signal because none is available. The Q3 print in late October is the decisive near-term event.