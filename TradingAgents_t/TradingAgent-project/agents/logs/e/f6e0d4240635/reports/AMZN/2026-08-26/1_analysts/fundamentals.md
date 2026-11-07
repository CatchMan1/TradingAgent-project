# AMZN — Fundamental Deep-Dive (point-in-time as of 2026-08-26)

**Instrument:** `AMZN` (Amazon.com, Inc.) · **Last reported period:** Q2 FY2026, quarter ended 2026-06-30 · **Filing used:** Form 10-Q, accession 0001018724-26-000026, accepted 2026-07-31 02:11 UTC · **Prior filing available:** Q1 FY2026 10-Q (0001018724-26-000014, accepted 2026-04-30)

---

## 1. Data provenance and coverage caveats (read this first)

Everything below is drawn from the SEC XBRL fact package, filtered by actual EDGAR acceptance time ≤ 2026-08-26. Three important limitations shape the analysis:

1. **No revenue tag is present in the fact set.** Revenue is therefore **derived** as `CostsAndExpenses + OperatingIncomeLoss`, which is exactly how Amazon's income statement is constructed (Total net sales − Total costs and expenses = Operating income). All derived revenue figures are flagged as such.
2. **No segment data, no price/market-cap data, no guidance.** The facts show `NumberOfOperatingSegments = 3` only. No P/E, EV, or market-cap multiples are computed in this report — I will not fabricate them.
3. **Insider transactions: DATA_UNAVAILABLE.** The vendor has no authorized point-in-time Form 4 archive for `AMZN` as of 2026-08-26. No insider buying/selling is inferred or reported. Traders should pull Form 4s directly if that factor matters.

The fact set is effectively a **two-quarter snapshot (Q1 + Q2 FY2026) plus FY2025 year-end balance-sheet anchors and trailing-twelve-month (TTM) figures for the period 2025-07-01 → 2026-06-30.** There is no multi-year annual history in this package, so long-run CAGR work is not possible here.

---

## 2. Company profile

Amazon.com, Inc. is a global technology and logistics conglomerate operating three reportable segments (confirmed by `NumberOfOperatingSegments = 3`): **North America** retail/marketplace, **International** retail/marketplace, and **Amazon Web Services (AWS)** cloud infrastructure. Revenue streams span online and physical stores, third-party seller services, advertising, subscription (Prime), and AWS compute/storage/database/AI services. Led by CEO Andy Jassy, with Jeff Bezos as Executive Chairman. *(Business description is general knowledge; the retrieved fact set does not include a profile document — segment-level revenue and margin are not available from these tools.)*

What the financials *do* confirm about the current operating model:
- A **capital-intensive infrastructure build-out** is underway (TTM capex $173.0B, +60.7% YoY) with depreciation re-accelerating (+42% YoY in Q2).
- The company is **not returning capital**: no dividend and no buyback tags appear; share count rose 0.5% in H1 from stock issuance.
- It has become **materially leveraged** in a way it was not a year ago (long-term debt +$63.2B in six months).
- It carries a **very large private-equity investment portfolio** that is now the single largest swing factor in reported earnings.

---

## 3. Income statement — Q2 FY2026 (three months ended 2026-06-30)

| Line ($M) | Q2 2026 | Q2 2025 | Δ |
|---|---|---|---|
| Revenue (**derived**) | **200,606** | 167,702 | **+19.6%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% |
| Gross profit (derived) | 104,828 | 86,893 | +20.6% |
| **Gross margin** | **52.3%** | 51.8% | +0.45 pt |
| Total costs & expenses | 173,145 | 148,531 | +16.6% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** |
| **Operating margin** | **13.7%** | 11.4% | **+2.3 pt** |
| Nonoperating income, net | 53,396 | 1,686 | +3,067% |
| — of which non-marketable equity revaluation | **50,486** | 49 | nm |
| Pretax income | 80,857 | 20,857 | +288% |
| Income tax | 18,199 | 2,678 | +580% |
| **Effective tax rate** | **22.5%** | 12.8% | +9.7 pt |
| **Net income** | **62,647** | 18,164 | **+245%** |
| **Diluted EPS** | **$5.75** | $1.68 | +242% |
| Diluted shares (implied) | ~10,895M | ~10,812M | +0.8% |

**Cost-line detail, Q2 2026 vs Q2 2025 (% of revenue):**
- Depreciation & amortization: $19,988M = **9.96%** vs $15,227M = 9.08% (**+31.3% YoY**, a 0.9 pt margin headwind). Of this, PP&E depreciation alone was $13,869M vs $9,766M (**+42%**).
- Stock-based comp: $6,038M = **3.01%** vs $6,534M = 3.90% (**down 7.6% in dollars** — a real ~0.9 pt margin tailwind).
- Marketing: $11,698M = **5.83%** vs $11,416M = 6.81% (+2.5% — far below revenue growth; ~1.0 pt of leverage).
- G&A: $2,788M = 1.39% vs $2,965M = 1.77% (−6.0%).
- Operating lease cost: $4,118M = 2.05% vs $3,426M = 2.04%.
- Interest expense: $1,314M vs $516M (**+155%**); interest income $1,295M vs $1,085M. **Net interest is now ~$0 (−$19M) versus +$569M a year ago.**

**Q1 FY2026 as derived (H1 less Q2):** revenue ≈ **$181,519M**, operating income **$23,852M** (**13.1%** margin), net income $30,255M, nonoperating income $15,982M of which **$12,328M** was non-marketable equity revaluation. So the operating-margin trajectory across the last four quarters is roughly **11.8% (Q1'25) → 11.4% (Q2'25) → 13.1% (Q1'26) → 13.7% (Q2'26)**: a genuine, sustained step-up in core profitability, independent of the investment marks.

**H1 FY2026 vs H1 FY2025:**

| Line ($M) | H1 2026 | H1 2025 | Δ |
|---|---|---|---|
| Revenue (derived) | **382,125** | 323,369 | **+18.2%** |
| Gross margin | 52.0% | 51.2% | +0.8 pt |
| Operating income | **51,313** | 37,576 | **+36.6%** |
| Operating margin | **13.4%** | 11.6% | +1.8 pt |
| Nonoperating income | 69,378 | 4,960 | nm |
| Pretax income | 120,691 | 42,536 | +184% |
| Tax / effective rate | 27,759 / **23.0%** | 7,231 / 17.0% | +6.0 pt |
| Net income | **92,902** | 35,291 | +163% |
| Diluted EPS | **$8.53** | $3.27 | +161% |
| D&A | 38,933 | 29,489 | +32.0% |
| SBC | 10,070 | 10,223 | −1.5% |

---

## 4. The single most important issue: earnings quality / the $115B equity re-rating

This is the crux of the AMZN fundamental story right now and it is easy to misread off a screen.

**What happened in the P&L:** Amazon recorded **$62,814M of pre-tax upward fair-value adjustments on equity securities without readily determinable fair value** in H1 FY2026 ($50,486M of it in Q2 alone, $12,328M in Q1). That compares with just $86M total in H1 FY2025. This is a **non-cash, mark-to-model gain on a private investment** that flows *below* the operating line — yet it produced roughly **80% of Q2 net income**.

Quantifying how much of the headline is not operations:
- Q2 **operating income $27,461M** vs **net income $62,647M** — net income is **2.3× operating income**.
- Diluted EPS of **$5.75** contains roughly **$3.59/share** attributable to the revaluation (($62,647 − $23,537) ÷ 10,895M shares).
- **Adjusted Q2 EPS:** stripping the $50,486M gain → pretax $30,371M. Taxed at the reported 22.5% rate: **≈ $2.16** (+29% YoY vs $1.68). But note the tax line is almost entirely *deferred*: Q2 deferred tax was **$17,691M of an $18,199M total tax charge**, i.e. ~97% of the tax provision is the deferred tax on the unrealized gain. If you also exclude that deferred tax (it reverses only on sale/realization), Q2 adjusted EPS is **≈ $2.74 (+63% YoY)**.
- **Practical range for sustainable Q2 EPS: ~$2.15–$2.75**, vs a GAAP headline of $5.75 and an implied TTM GAAP diluted EPS of **≈ $12.4** ($135,281M TTM net income ÷ ~10,890M shares). **Roughly 40–45% of trailing GAAP EPS is mark-to-market, not earnings.** Any valuation screen using TTM GAAP EPS on AMZN is materially wrong right now.

**What happened on the balance sheet:**
- Non-marketable equity securities carried value: **$16,200M (12/31/25) → $122,300M (6/30/26)**, a **+$106.1B** increase — now **11.2% of total assets**.
- Accumulated OCI: **$28,230M → $66,287M**, a **+$38,057M** increase in six months. The associated unrealized-gain fact moved from **$39,500M cumulative (FY2025) to $92,000M (H1 2026)**, i.e. ~+$52.5B pre-tax recognized *outside* the income statement; at a ~28% tax rate that reconciles almost exactly to the +$38.1B AOCI move ($92.0B × 0.72 = $66.2B ≈ the $66.3B AOCI balance).
- Combined, **~$115B of pre-tax value accretion on equity investments in six months** ($62.8B through P&L + $52.5B through OCI), against a $106.1B increase in carrying value. The size, timing and reporting mechanics are consistent with a step-change re-rating of Amazon's large private AI-model investment(s). **The investee identities are not disclosed in the retrieved fact set — treat that linkage as inference, not fact.**
- Small related items: marketable equity FV gains $1,300M (Q2) / $454M (H1); **warrant fair-value losses of −$1,449M (Q2) and −$1,051M (H1)** — a reminder these marks cut both ways.

**Trading implication:** AMZN's reported earnings now embed a $122B+ private-mark asset that is periodically re-appraised. A 25% downward revision in that stake would be a ~$30B pre-tax hit and would swing GAAP EPS by ~$2.20/share in a single quarter. Reported EPS volatility is now structurally decoupled from operating performance.

---

## 5. Cash flow — a capex supercycle, and negative free cash flow

| TTM ($M, 7/1/25–6/30/26) | Value | Prior TTM (7/1/24–6/30/25) | Δ |
|---|---|---|---|
| Operating cash flow | **161,403** | 121,137 | +33.2% |
| Capex (`PaymentsToAcquireProductiveAssets`) | **173,028** | 107,656 | **+60.7%** |
| **Free cash flow (OCF − capex)** | **−11,625** | +13,481 | **swing of −$25.1B** |
| Acquisitions, net of cash | 41,956 | 4,809 | +772% |
| Proceeds from LT debt issuance | 81,925 | 746 | nm |
| Net financing cash flow | **+75,160** | −8,652 | nm |
| Net investing cash flow | **−216,775** | −123,569 | +75% |

**Quarterly cash flow:**

| ($M) | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|
| OCF | 45,387 | 32,515 | 71,419 | 49,530 |
| Capex | 54,208 | 32,183 | 98,411 | 57,202 |
| **FCF** | **−8,821** | **+332** | **−26,992** | −7,672 |
| Acquisitions | 24,359 | 1,700 | 39,767 | 1,652 |
| Net financing | +10,146 | −2,539 | +62,913 | −2,586 |

Key readings:
- **Capex is 25.8% of H1 revenue** (27.0% in Q2 alone). Annualizing Q2, run-rate capex is **>$215B/yr**. This is the largest capital program in the company's history and it is still accelerating.
- **FCF has turned negative on a TTM basis for only the second time in this dataset** (−$11.6B), and the H1 deterioration was −$19.3B YoY. The company is being funded by **debt, not internal cash**.
- **Working capital was a ~$46B cash drag over the TTM** — receivables & other operating assets +$21.4B, other non-current assets +$17.8B, accrued/other operating liabilities −$6.1B, contract liabilities −$0.7B. Ex-neutral working capital, TTM OCF would have been ~$207B. The AR build is the item to watch (§7).
- OCF still grew 33% and comfortably exceeds D&A+SBC — the operating engine is working; the issue is deployment, not generation.

---

## 6. Balance sheet and leverage

**Assets ($M):**

| | 6/30/2026 | 12/31/2025 | Δ |
|---|---|---|---|
| Cash & equivalents | 78,213 | 86,810 | −8,597 |
| Available-for-sale debt securities | 97,900 | 45,800 | +52,100 |
| Accounts receivable, net | 88,092 | 67,729 | **+20,363 (+30.1%)** |
| Inventory, net | 38,184 | 38,325 | −141 |
| **Current assets** | **249,264** | 229,083 | +20,181 |
| **Non-marketable equity securities** | **122,300** | 16,200 | **+106,100** |
| **Total assets** | **1,095,689** | 818,042 | **+277,647 (+33.9%)** |

**Liabilities & obligations ($M):**

| | 6/30/2026 | 12/31/2025 | Δ |
|---|---|---|---|
| Accounts payable | 147,440 | 121,909 | +25,531 |
| Accrued liabilities | 73,406 | 75,520 | −2,114 |
| **Current liabilities** | **241,274** | 218,005 | +23,269 |
| Long-term debt — current | 3,330 | 2,748 | +582 |
| Long-term debt — noncurrent | 128,894 | 65,648 | **+63,246** |
| **Total long-term debt** | **132,995** | 68,836 | **+64,159 (+93%)** |
| Finance lease liabilities | 13,451 | 12,286 | +1,165 |
| Operating lease liabilities | 96,320 | 89,252 | +7,068 |
| Total contractual obligations (incl. purchase commitments) | **650,034** | — | — |
| — due within 12 months | 78,084 | — | — |

**Derived liquidity and coverage:**
- **Liquid assets: $176,113M** (cash $78,213M + AFS $97,900M), of which **$96,471M of the AFS portfolio matures within one year** — very high-quality liquidity.
- **Total debt incl. finance leases: $146,446M → net cash position of ~+$29.7B.** But add operating leases ($96.3B) and total fixed obligations reach **~$243B**.
- **Current ratio: 1.03×** (249,264 / 241,274) — down from 1.05× at year-end; thin, but Amazon's current liabilities are largely non-interest-bearing payables.
- **Coverage:** annualized Q2 interest expense of ~$5.3B against ~$100B+ run-rate operating income remains very comfortable, but interest expense **doubled YoY in H1** and the direction of travel is adverse.
- Fixed obligations: $78.1B due within 12 months vs $161.4B TTM OCF and $176.1B liquid assets — **manageable, but it leaves no room for capital returns.** Contractual obligations of $650B (mostly purchase/content/capacity commitments) are a genuine forward earnings claim and should be monitored as they reset each quarter ($46.5B "remainder of fiscal year" at 3/31/26 → $42.8B at 6/30/26).

**How the H1 asset growth was funded:** ~+$63.2B net new long-term debt (of $67.0B LT and $15.4B short-term issued, $2.8B + $15.7B repaid), ~$62.9B net financing inflow, plus $92.9B of net income and $38.1B of OCI gains. **Total cash actually fell $9.2B** (total cash + restricted $90,106M → $80,927M) despite $131B of accounting profit — that is the definitive proof that reported earnings are not converting to cash at the capex supercycle's current pace.

---

## 7. Watch items and red/amber flags

1. **Receivables growing 30.1% vs revenue ~19.6%.** AR of $88,092M implies **DSO ≈ 40 days** on Q2 revenue (88,092 / 200,606 × 91). The allowance for doubtful accounts rose 16.7% ($2,400M → $2,800M) — **slower than AR**, so allowance coverage slipped from 3.42% to 3.08% of gross AR. Watch advertising/seller-financing credit quality.
2. **Deferred tax buildup.** TTM deferred tax expense **$41,441M** against **cash taxes paid of only $6,635M**. H1 current tax was actually a **net benefit of −$2,730M** (tax expense $27,759M less deferred $30,489M). Cash tax is running at a *negative* rate on $120.7B of pretax income. This flatters near-term EPS; it also means a large deferred tax liability now sits against the equity stake that crystallizes on any disposal.
3. **$39.8B of acquisitions in H1 2026** ($24.4B in Q2 alone) vs $1.7B in H1 2025 — a **24× increase**. Goodwill/intangibles effects and integration risk are unquantified in this fact set. This is the most under-appreciated line in the filings.
4. **Derivative assets jumped 6.3×** ($112M → $705M) and energy notional of 270 GWh-equivalent suggests meaningful power-price hedging tied to datacenter load. Power cost is becoming a P&L variable.
5. **Goodwill-free-of-hype check:** inventory was flat (+/-0) while revenue grew 19.6% — excellent working-capital discipline on the retail side. Inventory valuation reserves fell 9.1% ($3,300M → $3,000M). No channel-stuffing signal.
6. **Unrecognized SBC of $24.8B** remains to be expensed — roughly 2+ years at the current run-rate. Dilution is modest (~0.5% per half) but the expense is real and already above the line.

---

## 8. Actionable insights for traders

**Bias: constructive on the operating business, cautious on the reported-earnings optics and financing trajectory.**

**A. Do not value `AMZN` off trailing GAAP EPS.**
TTM GAAP diluted EPS ≈ **$12.4**, but ~$5.8–6.0/share of that is non-cash private-market revaluation. Normalized trailing EPS is **~$7.00–7.75** (TTM net income ex-$62.8B marks, with partial deferred-tax add-back), and *current run-rate* EPS is roughly **$8.80–11.00 annualized** (Q2 adjusted $2.15–2.75 × 4). If your screen shows AMZN at ~19× on TTM EPS, the right number is closer to ~30–35× — and if a peer screen shows it at 12×, the screen is broken, not the stock.

**B. The operating story is unambiguously improving — that is the fundamental long.**
Operating margin went from 11.4% → 13.7% YoY with operating income +43.2% on revenue +19.6%. The drivers are high quality and repeatable: SBC down 7.6% in dollars, marketing growth (+2.5%) less than a seventh of revenue growth, G&A down 6%, gross margin +45bp, and inventory flat. Roughly **+2.0 pt of opex/cost leverage offset a −0.9 pt D&A headwind**, netting +2.3 pt of margin. This is an earnings-power story that the mark-to-market noise is obscuring.

**C. FCF is the bear case and the key catalyst either way.**
TTM FCF **−$11.6B**, capex run-rate **>$215B annualized**, funded with **+$75.2B of net financing**. Trade the capex guide, not the EPS line. A capex guide-down (or any signal that the AI build is being paced) is a **material positive** — every $25B of capex reduction is ~$25B of annual FCF recovery against a ~$1.0B/yr interest cost. Conversely, another half-year at this pace implies **$60–80B more debt**, further interest expense growth (+155% YoY already) and continued negative FCF.

**D. Balance-sheet risk is low but not negligible.**
Net cash of ~$29.7B, $176B liquid with $96.5B maturing inside a year, and 1.03× current ratio. Default risk is not the issue; **the issue is that rising leverage removes the buyback/dividend optionality that would otherwise support the multiple**, and it makes AMZN more sensitive to rate moves than at any point in the last decade.

**E. Specific event triggers to watch into the Q3 FY2026 print (expected late October 2026):**
1. **Any revaluation or impairment of the $122.3B non-marketable equity position.** A down-round or mark-down is a >$20B GAAP EPS event. Symmetrically, a further up-round is another mechanical EPS spike. Expect outsized option-implied moves around any AI funding-round news.
2. **Capex and FY2026 capex commentary** — the highest-information disclosure.
3. **Interest expense and any new debt issuance / credit rating commentary** (H1 saw $67.0B LT + $15.4B ST gross issuance).
4. **AR / DSO trend** (currently ~40 days): a move above ~43 days alongside decelerating revenue would be an early warning on seller/advertiser credit.
5. **Disclosure on the $39.8B of H1 acquisitions** — what was bought and whether it is dilutive to margins.
6. **Effective tax rate normalization** — cash taxes are running near zero; a step-up is a direct EPS headwind.

**F. What would make me turn negative on the fundamentals:** operating margin falling back below ~12% while capex stays above $50B/quarter (that combination would mean the AI build is not being monetized); or AR days pushing past ~45 with allowance coverage still falling; or a marked deterioration in the $122B private stake with a simultaneous rise in leverage.

**G. Insider signal: unavailable.** No authorized Form 4 archive exists for `AMZN` at this point-in-time. Do not read anything into the absence of insider data — it is a data gap, not a signal.

---

## 9. Key metrics summary table

| Category | Metric ($M unless noted) | Latest (Q2 FY26 / 6-30-26) | Comparable prior | Change | Read-through |
|---|---|---|---|---|---|
| **Growth** | Revenue (derived) | 200,606 | 167,702 (Q2'25) | **+19.6%** | Re-accelerating top line |
| | Revenue, H1 (derived) | 382,125 | 323,369 (H1'25) | +18.2% | |
| **Profitability** | Gross margin | 52.3% | 51.8% | +0.45 pt | Mix/ad leverage |
| | Operating income | 27,461 | 19,171 | +43.2% | Core engine strong |
| | Operating margin | 13.7% | 11.4% | **+2.3 pt** | Real operating leverage |
| | Net income | 62,647 | 18,164 | +245% | ~80% from non-cash marks |
| | Diluted EPS | $5.75 | $1.68 | +242% | Not repeatable |
| **Earnings quality** | Nonoperating income | 53,396 | 1,686 | nm | |
| | — non-marketable equity revaluation | **50,486** | 49 | nm | 80% of Q2 net income |
| | Adjusted EPS (ex-mark, 22.5% tax) | **~$2.16** | $1.68 | +29% | Core growth |
| | Adjusted EPS (ex-mark & deferred tax) | **~$2.74** | $1.68 | +63% | Upper bound |
| | Effective tax rate | 22.5% | 12.8% | +9.7 pt | Mostly deferred |
| | Deferred tax expense | 17,691 | 11 | nm | Non-cash |
| **Cash flow** | Operating cash flow (Q2) | 45,387 | 32,515 | +39.6% | Strong |
| | Capex (Q2) | 54,208 | 32,183 | +68.4% | 27.0% of revenue |
| | **Free cash flow (Q2)** | **−8,821** | **+332** | nm | Negative |
| | TTM OCF | 161,403 | 121,137 | +33.2% | |
| | TTM capex | 173,028 | 107,656 | +60.7% | Supercycle |
| | **TTM FCF** | **−11,625** | +13,481 | −$25.1B | Key bear metric |
| | H1 acquisitions | 39,767 | 1,652 | 24× | Unexplained M&A ramp |
| **Balance sheet** | Total assets | 1,095,689 | 818,042 (12/31/25) | +33.9% | |
| | Non-marketable equity securities | **122,300** | 16,200 | +655% | 11.2% of assets |
| | Cash + AFS securities | 176,113 | 132,610 | +32.8% | Strong liquidity |
| | Total long-term debt | **132,995** | 68,836 | **+93%** | Funded the build |
| | Finance lease liabilities | 13,451 | 12,286 | +9.5% | |
| | Operating lease liabilities | 96,320 | 89,252 | +7.9% | |
| | Current ratio | 1.03× | 1.05× | −0.02× | Thin but low-risk liabilities |
| | Net cash (liquid − debt & fin. leases) | +~29,700 | +~51,500 | −$21.8B | Deleveraging reversed |
| | Contractual obligations | 650,034 | — | — | $78.1B due <12 mo |
| **Book value** | AOCI | 66,287 | 28,230 | **+134.8%** | +$38.1B OCI gains |
| | APIC | 149,619 | 140,024 | +6.9% | SBC + issuance |
| | Shares outstanding | 10,783M | 10,731M | +0.5% | Minimal dilution |
| | Shares outstanding (7/22/26) | 10,786.3M | — | — | |
| **Returns/other** | Interest expense (Q2) | 1,314 | 516 | +155% | Rising fast |
| | Interest income (Q2) | 1,295 | 1,085 | +19.4% | Now offsetting |
| | SBC (Q2) | 6,038 | 6,534 | −7.6% | Genuine restraint |
| | Unrecognized SBC | 24,800 | — | — | ~2+ yrs of expense |
| | D&A (Q2) | 19,988 | 15,227 | +31.3% | AI infra ramping |
| | Insider transactions | **DATA UNAVAILABLE** | — | — | Not inferable |

---

**Bottom line for `AMZN`:** a genuinely improving operating business (13.7% operating margin, +19.6% revenue, real opex discipline) wrapped inside an accounting period distorted by ~$115B of private-equity revaluation, funded by a debt-financed, >$200B annualized capex program that has pushed free cash flow negative. Trade the capex trajectory and the private-stake re-appraisal risk; use ~$2.15–$2.75 of quarterly normalized EPS and ~$7.00–$7.75 of normalized TTM EPS as your anchors, not the $5.75/$12.4 GAAP figures.