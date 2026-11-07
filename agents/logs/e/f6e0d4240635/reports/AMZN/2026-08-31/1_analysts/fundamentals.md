# AMZN (Amazon.com, Inc.) — Fundamental Research Report
**As of:** 2026-08-31 | **Latest filing in data:** Form 10-Q for the quarter ended 2026-06-30 (filed 2026-07-31) | **Ticker:** AMZN

---

## 0. Data provenance & important limitations (read first)

All figures below are **point-in-time SEC XBRL facts** accepted by EDGAR on or before 2026-08-31, drawn from the **Q2-2026 10-Q (accn 0001018724-26-000026, filed 2026-07-31)** and the **Q1-2026 10-Q (accn 0001018724-26-000014, filed 2026-04-30)**.

Four gaps I could not close with the available tools, and I am **not** filling them with estimates disguised as facts:

| Gap | Status |
|---|---|
| **FY2025 / FY2024 10-K annual facts** | Not in the cache. `annual` frequency requests returned the *same* 10-Q dataset. No multi-year revenue/segment history available. |
| **Revenue line item** (`Revenues`, `RevenuesNetOfInterestExpense`) | Not tagged in payload — **derived** as `CostsAndExpenses + OperatingIncomeLoss` (exact identity for this line item). |
| **Segment detail** (NA / International / AWS) | Only `NumberOfOperatingSegments = 3` is disclosed. No segment revenue or AWS margin. |
| **Insider transactions** | Tool returned `DATA_UNAVAILABLE` — no authorized point-in-time insider archive for AMZN. **No insider activity is inferred or fabricated here.** |
| **Share price / market cap** | Not provided. **No valuation multiples are computed.** I supply the earnings, cash-flow and book-value bases so a pricing layer can be applied. |

---

## 1. Company profile (context, not from tool output)

Amazon.com, Inc. (AMZN, Nasdaq) is a global technology and retail conglomerate operating as **three reportable segments**: North America, International, and Amazon Web Services (AWS). Revenue is a blend of (i) online and physical stores, (ii) third-party seller services (1P/3P + Fulfillment by Amazon), (iii) advertising, (iv) subscription services (Prime), and (v) AWS cloud/compute. The economic engine has migrated toward the two high-margin businesses — **AWS and advertising** — which is visible in the margin data below. Filings confirm the three-segment structure as of H1 2026.

---

## 2. Executive summary — what the numbers actually say

**Six things matter, in order of importance to a trader:**

1. **Operating momentum is strong and accelerating.** Q2-2026 revenue ≈ **$200.6B, +19.6% YoY** (vs +16.6% in Q1-2026). Operating income **$27.5B, +43% YoY**; operating margin **13.7%, +226bp YoY**. This is genuine operating leverage, not financial engineering.
2. **Reported EPS is heavily inflated by a non-cash mark-up of private equity stakes.** Q2-2026 included a **$50.5B pre-tax upward revaluation** of equity securities without readily determinable fair value (`EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment`). That equalled **62% of Q2 pre-tax income** and **52% of H1 pre-tax income**. Reported diluted EPS of **$5.75** is *not* an operating number.
3. **A ~$122B unlisted equity position now sits on the balance sheet** (11.2% of assets), up from $16.2B at 2025-12-31. It is marked via the income statement with **no public price reference** — a first-order, hard-to-hedge source of earnings volatility in *both* directions.
4. **Capex has gone vertical: $98.4B in H1-2026, +72% YoY = 25.8% of revenue.** TTM capex **$173.0B vs TTM D&A $75.2B (2.3x)**. Free cash flow has turned **negative**: **–$27.0B in H1-2026** and **–$11.6B TTM**.
5. **The funding is debt and asset marks, not cash generation.** Gross long-term debt nearly **doubled to ~$132.2B in six months**; $67.0B of LT + $15.4B of ST paper issued in H1. Interest expense **+155% YoY** ($1.31B in Q2). Net interest income has collapsed to roughly zero.
6. **Liquidity is still ample.** Cash + marketable securities **$176.1B** (+32.8% YTD) — comfortably above debt ex-leases ($43.9B net cash). The balance sheet can fund the buildout; the *equity* story is what gets stressed by negative FCF.

**Net:** the operating business is compounding faster than at any point in the last several years, while the *reported* earnings and *reported* free cash flow have both decoupled from that operating reality — one inflated by mark-ups, one deflated by an AI-infrastructure super-cycle. Price the operating line; discount the marks.

---

## 3. Income statement — quarterly reconstruction

Derived revenue = `CostsAndExpenses + OperatingIncomeLoss`. Dollars in millions.

| Metric | Q1-2025 | Q2-2025 | H1-2025 | Q1-2026 | Q2-2026 | H1-2026 | Q2 YoY |
|---|---|---|---|---|---|---|---|
| **Net sales (derived)** | 155,667 | 167,702 | 323,369 | 181,519 | **200,606** | **382,125** | **+19.6%** |
| Cost of goods & services | 76,976 | 80,809 | 157,785 | 87,463 | 95,778 | 183,241 | +18.5% |
| **Gross profit** | 78,691 | 86,893 | 165,584 | 94,056 | **104,828** | **198,884** | +20.6% |
| *Gross margin* | 50.55% | 51.83% | 51.20% | 51.81% | **52.26%** | **52.05%** | +43bp |
| Marketing | 9,763 | 11,416 | 21,179 | 10,314 | 11,698 | 22,012 | +2.5% |
| G&A | 2,628 | 2,965 | 5,593 | 2,587 | 2,788 | 5,375 | −6.0% |
| SBC (total) | 3,689 | 6,534 | 10,223 | 4,032 | 6,038 | 10,070 | −7.6% |
| D&A | 14,262 | 15,227 | 29,489 | 18,945 | **19,988** | **38,933** | +31.3% |
| Operating lease cost | 3,240 | 3,426 | 6,666 | 3,917 | 4,118 | 8,035 | +20.2% |
| Total costs & expenses | 137,262 | 148,531 | 285,793 | 157,667 | 173,145 | 330,812 | +16.6% |
| **Operating income** | 18,405 | 19,171 | 37,576 | 23,652 | **27,461** | **51,313** | **+43.2%** |
| *Operating margin* | 11.82% | 11.43% | 11.62% | 13.03% | **13.69%** | **13.43%** | +226bp |
| Non-operating income/(exp.) | 3,274 | 1,686 | 4,960 | 15,982 | **53,396** | **69,378** | n.m. |
| Pre-tax income | 21,679 | 20,857 | 42,536 | 39,834 | **80,857** | **120,691** | +288% |
| Income tax | 4,553 | 2,678 | 7,231 | 9,560 | 18,199 | 27,759 | +580% |
| *Effective tax rate* | 21.0% | 12.8% | 17.0% | 24.0% | **22.5%** | **23.0%** | +970bp |
| **Net income** | 17,127 | 18,164 | 35,291 | 30,255 | **62,647** | **92,902** | **+245%** |
| Net margin | 11.0% | 10.8% | 10.9% | 16.7% | **31.2%** | 24.3% | +20.4pt |
| **Diluted EPS** | 1.59 | 1.68 | 3.27 | 2.78 | **5.75** | **8.53** | +242% |
| Basic EPS | — | 1.71 | 3.32 | — | 5.82 | 8.64 | — |

**Sequential read:** revenue **+10.5% QoQ** ($181.5B → $200.6B) and operating income **+16.1% QoQ**. Momentum is *up*, not flattening.

---

## 4. The earnings-quality problem — the single most important item in this report

### 4a. Where the Q2 non-operating income came from

| Component (Q2-2026) | $M | Q2-2025 $M |
|---|---|---|
| **Upward revaluation, equity securities w/o readily determinable FV** | **50,486** | 49 |
| Marketable-securities unrealized gain | 1,319 | 388 |
| Equity securities FV-NI gain | 1,300 | 393 |
| Interest income | 1,295 | 1,085 |
| Interest expense | (1,314) | (516) |
| FX transaction gain | 227 | 70 |
| Warrant fair-value adjustment | (1,449) | (590) |
| Sum of tagged items | 51,864 | 879 |
| **Reported non-operating income** | **53,396** | **1,686** |

The $50.5B mark-up is **1,030x** the year-ago equivalent ($49M). H1-2026 total: **$62,814M** pre-tax, of which $50,486M landed in Q2 alone (Q1-2026: $12,328M).

### 4b. Adjusted ("core") earnings estimate

| | Q2-2026 | H1-2026 |
|---|---|---|
| Pre-tax income (reported) | 80,857 | 120,691 |
| Less: upward revaluation | (50,486) | (62,814) |
| Pre-tax income ex-revaluation | 30,371 | 57,877 |
| Mark-up as % of reporting pre-tax income | **62.4%** | **52.0%** |
| After-tax @ 22.5%/23.0% ETR | 23,537 | 44,565 |
| **Core diluted EPS (est.)** | **≈ $2.16** | **≈ $4.09–4.50** |
| Reported diluted EPS | 5.75 | 8.53 |
| **Inflation vs. core** | **~2.7x** | **~2.0x** |

**Trader takeaway:** the $5.75 print is a ~$2.16 operating-adjacent quarter, roughly in line with seasonally normal progression but flattered by disposal of low-margin mix and leverage — and *not* a 242%-growth quarter. Any consensus built off the headline is mis-anchored. Conversely, the same mark-up mechanism could reverse in a private-market down-round and produce a violent negative EPS surprise with no operating deterioration at all.

### 4c. Corroboration from the cash-flow statement
- **OCF/NI ratio: 0.77x in H1-2026** (OCF $71.4B vs NI $92.9B). Contribution from a *non-cash* income item inflates net income above operating cash generation.
- **Deferred tax expense TTM $41.4B** (H1-2026: $30.5B; Q2: $17.7B) vs **cash taxes paid TTM of only $6.6B**. Cash tax rate in H1-2026 = **3.3%** of pre-tax income vs a 23.0% book rate. The gap is largely DTLs created by the unrealized gains (and accelerated depreciation).
- Reported pre-tax income is therefore **twice-supported** by non-cash items: investment marks *up* and tax accruals *up*.

### 4d. But note the genuine quality *improvements*
- **SBC fell 7.6% YoY in Q2** ($6,038M vs $6,534M) to **3.01% of revenue vs 3.90%** — real discipline against a 19.6% revenue increase.
- **Marketing down to 5.83% of revenue from 6.81%; G&A down to 1.39% from 1.77%.**
- **Inventory flat at $38,184M** (−0.4% since 2025-12-31) while Q2 revenue rose 19.6% — quarterly turns ≈2.5x (~10x annualized).
- Gross margin **+43bp YoY**, i.e., mix shift toward AWS/ads is still working *through* the P&L.

---

## 5. Balance sheet — assets, leverage, and the composition shift

Dollars in millions.

| Assets | 2025-12-31 | 2026-06-30 | Δ |
|---|---|---|---|
| Cash & equivalents | 86,810 | 78,213 | −8,597 |
| Marketable securities (AFS debt) | 45,800 | **97,900** | **+52,100** |
| Accounts receivable (net) | 67,729 | 88,092 | +20,363 (+30.1%) |
| Inventory (net) | 38,325 | 38,184 | −141 |
| **Total current assets** | 229,083 | 249,264 | +20,181 (+8.8%) |
| **Equity securities w/o readily det. FV** | **16,200** | **122,300** | **+106,100 (+655%)** |
| Operating lease ROU asset | 86,054 | 92,743 | +6,689 |
| Equity-method investments | 659 | 395 | −264 |
| **Total assets** | **818,042** | **1,095,689** | **+277,647 (+33.9%)** |
| **Liabilities & equity** | | | |
| Accounts payable | 121,909 | 147,440 | +25,531 (+20.9%) |
| Accrued liabilities | 75,520 | 73,406 | −2,114 |
| Long-term debt — current | 2,748 | 3,330 | +582 |
| Operating lease liability — current | 12,655 | 13,745 | +1,090 |
| Finance lease liability — current | 1,544 | 1,688 | +144 |
| **Total current liabilities** | 218,005 | 241,274 | +23,269 (+10.7%) |
| **Long-term debt — noncurrent** | 65,648 | **128,894** | **+63,246 (+96.3%)** |
| Operating lease liability — noncurrent | 76,597 | 82,575 | +5,978 |
| Finance lease liability — noncurrent | 10,742 | 11,763 | +1,021 |
| AOCI (equity) | 28,230 | 66,287 | +38,057 |
| Additional paid-in capital | 140,024 | 149,619 | +9,595 |
| Shares outstanding (M) | 10,731 | 10,783 | +52 |

**Composition insight — the balance sheet changed character in six months:**
- **Non-marketable equity +$106.1B.** Of this, **$62.8B is income-statement revaluation**; the residual **~$43.3B is new capital deployed**, consistent with **$39.8B of business acquisitions** in H1 (Q1 $15.4B + Q2 $24.4B vs just $1.7B in all of H1-2025 — a **24x** step-up).
- **AOCI +$38.1B**, taking total comprehensive income to **$131.0B vs net income of $92.9B**. This OCI gain (tagged `DebtSecuritiesAvailableForSaleUnrealizedGainLoss` = $92,000M for H1-2026, versus only $7M of *gross accumulated* unrealized gain on the AFS debt book at 6/30) is the least transparent line in the filing. Treat the $38B as **non-cash, unrealized, and not verifiable from the disclosed maturity schedule** — do not capitalize it.
- **Book equity expanded ~$141B** (NI $92.9B + AOCI $38.1B + APIC $9.6B), with **share count up only 0.5%** since YE2025 (10,731M → 10,783M; 10,786.3M as of 2026-07-22) — i.e., **no buyback support**, all equity growth is organic/retained plus SBC.
- **Total equity level is not directly in the payload** (no `StockholdersEquity` tag). Compute as `Assets − Liabilities` when a liabilities-complete source is available; do not rely on a derived P/B until then.

---

## 6. Liquidity, leverage & coverage

| Metric | 2025-12-31 | 2026-06-30 |
|---|---|---|
| Cash + marketable securities | 132,610 | **176,113** (+32.8%) |
| Total debt (current + noncurrent) | 68,396 | **132,224** (+93.3%) |
| Finance lease liabilities | 12,286 | 13,451 |
| Operating lease liabilities | 89,252 | **96,320** |
| **Total debt + lease obligations** | 169,934 | **241,995** |
| Net cash (debt) excl. leases | +64,214 | **+43,889** |
| Net debt incl. all leases | −37,324 | **−65,882** |
| Current ratio | 1.051 | **1.033** |
| Cash + securities / current liabilities | 0.61x | **0.73x** |
| Debt / total assets | 8.4% | **12.1%** |

**Coverage:** Q2-2026 annualized operating income ≈ **$109.8B** against annualized interest expense ≈ **$5.26B** → **~21x** interest coverage. Solvency is not a near-term issue. **Funding risk is a duration/maturity question, not a solvency question** — and the $650B contractual-obligation stack below.

---

## 7. Cash flow — the FCF inflection is the crux

Dollars in millions.

| | H1-2025 | H1-2026 | YoY | TTM to 2026-06-30 |
|---|---|---|---|---|
| **Operating cash flow** | 49,530 | **71,419** | **+44.2%** | **161,403** (prior TTM 121,137, +33.2%) |
| Capex (productive assets) | 57,202 | **98,411** | **+72.0%** | **173,028** (prior 107,656, +60.7%) |
| **Free cash flow (OCF − capex)** | **(7,672)** | **(26,992)** | worse | **(11,625)** (prior +13,481) |
| Acquisitions, net of cash | 1,652 | **39,767** | 24x | 41,956 |
| Purchases of marketable securities | 31,130 | 49,262 | +58% | 72,902 |
| Proceeds from sales/maturities | 19,178 | 41,882 | +118% | 67,090 |
| LT debt issued | 746 | **66,998** | n.m. | 81,925 |
| ST debt issued / (repaid) | 3,908 / (3,474) | 15,386 / (15,682) | — | 20,798 / (20,634) |
| LT debt repaid | (2,751) | (2,752) | — | (5,022) |
| **Investing cash flow** | (69,227) | **(143,457)** | 2.1x | **(216,775)** |
| **Financing cash flow** | (2,586) | **+62,913** | n.m. | **+75,160** |
| D&A | 29,489 | 38,933 | +32.0% | 75,200 |
| Operating lease payments | 7,320 | 7,804 | +6.6% | 15,522 |
| Cash taxes paid | 5,638 | 3,978 | −29% | 6,635 |

**Three hard numbers for the model:**

1. **Capex intensity: 25.8% of revenue in H1-2026** (Q2 alone **27.0%**), versus **17.7%** in H1-2025 and **19.2%** in Q2-2025. Capex/D&A is **2.71x** in Q2 — depreciation has not yet begun to reflect this spend. **D&A is already 9.96% of revenue** (up from 9.08%) and will keep climbing; that is a structural margin headwind that will arrive *whether or not* the AI capacity monetises.
2. **Cash burn after all investment:** OCF $71.4B − capex $98.4B − acquisitions $39.8B = **−$66.8B in six months**, met by **+$64.1B net new debt**. Amazon is *leveraging into* the buildout, not self-funding it.
3. **The offset is tax deferral:** cash taxes of $3,978M on $120,691M of pre-tax income (3.3%). If/when cash tax rates normalise, the FCF gap widens further with no change in operations.

---

## 8. Contractual obligations & lease stack (off-balance-sheet pressure)

**Total contractual obligations at 2026-06-30: $650.0B** (tag `ContractualObligation`).

| Due | $M |
|---|---|
| Remainder of FY2026 | 42,752 |
| Next 12 months | 78,084 |
| Year 2 | 53,406 |
| Year 3 | 46,767 |
| Year 4 | 42,219 |
| Thereafter (residual) | ~387,000 |
| **Total** | **650,034** |

**Operating leases:** $116,350M undiscounted (recognised liability $96,320M; discount rate **3.9%**, up from 3.7%), $14,765M due in next 12 months. **Finance leases:** $16,660M undiscounted ($13,451M recognised), $1,775M within 12 months.

The **$387B "thereafter" tail is the tell** — this is the profile of multi-year compute/power/content commitments, not ordinary retail purchase orders. It is a *demand-side commitment* if the AI thesis is right, and a *fixed-cost liability* if it is not. Either way it explains why debt is being raised at scale now.

---

## 9. Insider transactions

**DATA_UNAVAILABLE.** The news/filings vendor holds no authorized point-in-time insider-transaction archive for AMZN as of 2026-08-31. **No insider buying or selling is reported, implied, or estimated here.** Do not treat the absence as a signal in either direction — treat it as an unmonitored risk. This is a genuine blind spot in the current information set, and it means one of the classic confirmations for a negative-FCF, high-capex, high-multiple story (management selling into strength, or founders buying weakness) cannot be checked from this toolkit.

---

## 10. Actionable insights for traders

**Bull case (evidence-weighted):**
- Revenue growth **accelerated** to +19.6% YoY in Q2 from +16.6% in Q1, on a $800B+ annualized revenue base.
- Operating margin **+226bp YoY to 13.69%**, with gross margin +43bp and *all three* discretionary expense lines (SBC, marketing, G&A) contracting as a % of revenue. Operating income +43% YoY — this is the cleanest line in the report.
- **Capital is flooding into high-return areas**: $39.8B of acquisitions and $98.4B of capex in six months, with the multi-year obligation stack ($650B) evidencing contracted forward demand.
- Liquidity fortress: **$176.1B cash + securities**; net cash ex-leases $43.9B; ~21x interest coverage; interest income ($1.30B) still roughly covers interest expense ($1.31B).
- Balance sheet capacity is real: assets +34% in six months, and the company raised $82B of LT debt in TTM without leverage metrics becoming stressed (debt/assets 12.1%).

**Bear case / risks (evidence-weighted):**
- **~52% of H1 pre-tax income and 62% of Q2 pre-tax income was a non-cash private-equity mark-up.** Core Q2 EPS ≈ $2.16 vs $5.75 reported. Any reversal is instantaneous and untrackable.
- **$122.3B (11.2% of assets) of unlisted equity** with no observable price; valuation is management/model determined.
- **Negative FCF for three straight reporting periods** (H1-2026 −$27.0B; TTM −$11.6B) and negative after-acquisition cash flow of −$66.8B in H1, financed by ~$64B of new debt.
- **Debt nearly doubled in six months** (68.4 → 132.2B) and **interest expense +155% YoY**; net interest income is now ~zero, removing a tailwind that existed in 2025.
- **Depreciation cliff**: capex is 2.71x D&A. D&A at 10.0% of revenue and rising is a mechanical margin drag in 2027+ regardless of demand.
- **Receivables +30.1% YTD vs +19.6% YoY revenue** — watch DSO and customer concentration (AI compute counterparties) as a potential early warning.
- **Cash tax rate 3.3%** cannot persist; normalisation removes a $20B+/yr FCF support.
- **$38.1B of the equity increase came through AOCI**, not the income statement, and is not reconcilable to the disclosed AFS book ($7M gross unrealized gain). Treat as unverified.
- **No buyback** to cushion the equity story (share count +0.5% YTD, all SBC-driven).

**Concrete positioning ideas with triggers:**
1. **Separate the two AMZN stories.** Trade the *operating* business (margin +43% YoY, accelerating revenue) separately from the *holding-company* marks. Any entry decision should be underwritten on operating income of ≈$51.3B H1 / ~$110B annualized run-rate, plus a capex-normalisation scenario — not on the $135.3B TTM net income.
2. **Set the Q3-2026 print (late October 2026) as the single highest-value catalyst.** Specifically watch: (a) whether the non-operating line normalises — a quarter *without* a mark-up will look like a ~60-70% YoY EPS *decline* despite healthy operations; (b) capex guide vs the $98.4B H1 pace — a further step-up with unchanged demand commentary is the bear trigger; (c) whether OCF growth (+44%) continues to outrun capex growth (+72%).
3. **Monitor the capex/OCF convergence.** H1-2026: capex 1.38x OCF. A move below ~1.0x (either OCF acceleration or capex discipline) flips FCF positive and is the cleanest re-rating catalyst available.
4. **Watch the AOCI line and the non-marketable equity balance each quarter.** A flat or down $122.3B mark is the single largest identifiable EPS risk and is *not* in operating consensus models.
5. **Watch the maturity ladder and the "thereafter" obligation tail.** If total contractual obligations rise materially above $650B while LT debt issuance continues at ~$67B/half, the credit narrative shifts from "funded buildout" to "demand quality question."
6. **Do not underwrite without insider data.** That evidence channel is dark in this dataset; if the position is sizeable, source Form 4 data independently before committing.

---

## 11. Key points summary

| Category | Metric | Value | Signal |
|---|---|---|---|
| **Revenue** | Q2-2026 (derived) | $200.6B, +19.6% YoY | 🟢 Accelerating (Q1 +16.6%) |
| | H1-2026 | $382.1B, +18.2% YoY | 🟢 |
| **Profitability** | Q2 operating income | $27.5B, +43.2% YoY | 🟢 Strong leverage |
| | Q2 operating margin | 13.69% (+226bp YoY) | 🟢 |
| | Q2 gross margin | 52.26% (+43bp YoY) | 🟢 Mix shift working |
| **Earnings quality** | Q2 reported diluted EPS | $5.75 | 🔴 2.7x core |
| | Q2 core EPS (est., ex-mark-up) | ≈$2.16 | 🔴 |
| | Private-equity mark-up, Q2 pre-tax | $50,486M = **62.4%** of pre-tax income | 🔴 Non-cash, model-valued |
| | Mark-up, H1-2026 pre-tax | $62,814M = **52.0%** of pre-tax income | 🔴 |
| | H1 OCF / net income | 0.77x | 🔴 NI > cash generation |
| **Cost discipline** | SBC / revenue (Q2) | 3.01% vs 3.90% | 🟢 |
| | Marketing / revenue (Q2) | 5.83% vs 6.81% | 🟢 |
| | G&A / revenue (Q2) | 1.39% vs 1.77% | 🟢 |
| **Cash generation** | TTM operating cash flow | $161.4B (+33.2%) | 🟢 |
| | TTM capex | $173.0B (+60.7%) | 🔴 |
| | **TTM free cash flow** | **−$11.6B** (was +$13.5B) | 🔴 |
| | H1-2026 FCF | −$27.0B | 🔴 |
| | H1 capex / revenue | 25.8% (Q2: 27.0%) | 🟡 Buildout |
| | Capex / D&A (Q2) | 2.71x | 🔴 Depreciation cliff ahead |
| **Balance sheet** | Total assets | $1,095.7B (+33.9% YTD) | 🟡 |
| | Cash + marketable securities | $176.1B (+32.8% YTD) | 🟢 |
| | Total debt | $132.2B (+93.3% YTD) | 🔴 Levering up |
| | Net cash ex-leases | +$43.9B | 🟢 |
| | Net debt incl. all leases | −$65.9B | 🟡 |
| | Non-marketable equity holdings | $122.3B = 11.2% of assets (+655% YTD) | 🔴 Unobservable marks |
| | Current ratio | 1.03 (from 1.05) | 🟡 |
| | Debt / total assets | 12.1% (from 8.4%) | 🟡 |
| | AOCI | $66.3B (+$38.1B YTD) | 🔴 Unverified OCI gain |
| | Shares outstanding | 10,783M (+0.5% YTD) | 🟡 No buyback support |
| **Leverage service** | Q2 interest expense | $1,314M, **+155% YoY** | 🔴 |
| | Interest coverage (Q2 annualised) | ~21x | 🟢 |
| | H1 cash tax rate | 3.3% (vs 23.0% book) | 🟡 Unsustainable support |
| **Obligations** | Total contractual obligations | $650.0B; $78.1B due in 12m; ~$387B thereafter | 🟡 Committed demand or fixed-cost risk |
| | Operating lease liabilities | $96.3B ($116.4B undiscounted, 3.9% rate) | 🟡 |
| **Capital allocation** | H1 acquisitions | $39.8B vs $1.7B LY (24x) | 🟡 |
| | H1 LT + ST debt issued | $82.4B gross | 🔴 |
| | Financing cash flow TTM | +$75.2B (from −$8.7B) | 🔴 |
| **Insider activity** | AMZN Form 4 data | **DATA_UNAVAILABLE** | ⚪ Unmonitored |
| **Segments** | Reportable segments | 3 (NA / Intl / AWS) — no segment detail in payload | ⚪ Data gap |
| **Next catalyst** | Q3-2026 earnings | ~late Oct 2026 | 🎯 Watch non-op line, capex guide, OCF/capex convergence |

**One-line thesis:** AMZN's operating engine is the strongest it has been — 19.6% growth, 13.7% operating margin, +43% operating income — but *reported* EPS is inflated ~2.7x by a $50B non-cash private-equity mark-up and *reported* FCF is negative because capex has reached 27% of revenue; trade the operating line, discount the marks, and make the H2-2026 capex-vs-cash-flow convergence the decision variable.