# GOOGL — Alphabet Inc. | Fundamental Research Report
**Report date: 2026-09-04 | Latest available filings: Q2 2026 Form 10-Q (period ended 2026-06-30, accepted 2026-07-23); FY2025 Form 10-K (filed 2026-02-05)**

---

## 1. Data Provenance & Method Notes (read first)

- All figures below are **point-in-time SEC XBRL facts** filtered by EDGAR acceptance timestamp (no look-ahead). Latest data: **Q2 2026 10-Q**, accession `0001652044-26-000071`.
- **Revenue is not a directly returned tag** in this dataset. It is derived and cross-checked as:
 `Revenue = CostsAndExpenses + OperatingIncomeLoss`
 This reconciles exactly across every period used (H1'26, Q2'26, Q1'26, H1'25, Q2'25, Q1'25). All revenue and gross-profit figures are **derived, not reported**.
- Diluted share counts are **derived** (`NetIncomeLoss ÷ diluted EPS`); they tie within rounding.
- **`get_fundamentals` returned the raw SEC fact archive, not a narrative company profile.** No segment revenue, geographic mix, guidance, consensus estimates, or price data were available.
- **`get_insider_transactions` returned `DATA_UNAVAILABLE`** — the data package has no authorized insider-transaction archive for GOOGL as of 2026-09-04. **No insider buying/selling is inferred or fabricated.** This is a genuine information gap, not a "zero activity" reading.
- Because **no share price was provided**, no P/E, EV/EBITDA, or price-target math is presented. Any such figures in the market should be sanity-checked against the ex-gains EPS in §4.

---

## 2. Company Profile (context; not derived from the returned dataset)

Alphabet Inc. (**GOOGL**, Class A common) is the parent of Google. Operating structure: **Google Services** (Search & other advertising, YouTube ads, Network, Google subscriptions/platforms/devices), **Google Cloud** (infrastructure, platform, Workspace, and AI/Gemini enterprise offerings), and **Other Bets** (notably Waymo). Alphabet also carries a very large **equity investment portfolio** (marketable and non-marketable), which — as quantified in §5 — has become a first-order driver of reported earnings and balance-sheet size. FY2025 year-end total assets were **$595.3B**; by mid-2026 they were **$922.0B**, a +54.9% six-month expansion.

---

## 3. Q2 2026 & First-Half 2026 Results (all $M except per-share)

| Metric | Q2 2026 | Q2 2025 | Δ YoY | H1 2026 | H1 2025 | Δ YoY |
|---|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | 119,796 | 96,428 | **+24.2%** | 229,692 | 186,662 | **+23.0%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| Gross profit | 73,853 | 57,389 | +28.7% | 142,478 | 111,262 | +28.1% |
| **Gross margin** | **61.7%** | 59.5% | +220bp | **62.0%** | 59.6% | +240bp |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 149,226 | 124,785 | +19.6% |
| **Operating income** | **40,770** | 31,271 | **+30.4%** | **80,466** | 61,877 | **+30.0%** |
| **Operating margin** | **34.0%** | 32.4% | +160bp | **35.0%** | 33.2% | +190bp |
| Non-operating income | **97,983** | 2,662 | n.m. | **135,699** | 13,845 | +880% |
| Pre-tax income | 138,753 | 33,933 | +309% | 216,165 | 75,722 | +185% |
| Income tax | 26,560 | 5,737 | — | 41,394 | 12,986 | — |
| **Effective tax rate** | **19.1%** | 16.9% | +220bp | **19.1%** | 17.1% | +200bp |
| Net income | **112,193** | 28,196 | +298% | **174,771** | 62,736 | +179% |
| Net income to common | 112,107 | 28,196 | +298% | 174,685 | 62,736 | +178% |
| **Diluted EPS** | **$9.11** | $2.31 | +294% | **$14.24** | $5.12 | +178% |
| Diluted shares (derived) | 12,315M | 12,209M | +0.9% | 12,273M | 12,253M | +0.2% |

**Q1 2026 for completeness (derived by subtraction):** revenue **$109,896M** (+21.8% vs Q1'25 $90,234M), gross margin **62.4%**, operating income **$39,696M** (36.1% margin, +29.7% YoY), non-operating income **$37,716M**, diluted EPS **$5.13**.

### 3.1 The core operating engine is genuinely accelerating
- Revenue growth of **+24.2% in Q2 and +23.0% in H1** is a marked step-up versus Alphabet's low-to-mid-teens growth of recent years. The trajectory is stable-to-improving sequentially (Q1 +21.8%, Q2 +24.2%), which argues against a one-off.
- **Cost of revenue grew only 15.7% against 23.0% revenue growth** — gross margin expanded **240bp to 62.0%**. This is important: it means the massive AI compute build is *not yet* compressing gross margin, implying either strong pricing/utilization or favorable mix (e.g., higher-margin Cloud/AI relative to the incremental cost base).
- **Operating income grew 30.0% versus 23.0% revenue growth** — margin expansion of ~190bp. Operating expense (total costs ex-cost-of-revenue) rose 25.6% to $62,012M (H1). G&A rose 22.9% to $10,752M. Combined R&D + S&M (derived as $51,260M, vs $40,637M) rose **26.1%** — investment is rising fast, but operating leverage is still positive.
- **Operating margin 35.0% H1 2026 vs 33.2% H1 2025** is the single most bullish fundamental datapoint in this report: it rebuts the bear case that AI capex would immediately destroy margins.

### 3.2 Earnings quality: ~63% of reported EPS is NOT operating income
This is the most important analytical adjustment in this report.

| | Q2 2026 | H1 2026 |
|---|---:|---:|
| Diluted EPS (reported) | $9.11 | $14.24 |
| After-tax non-operating income per share¹ | **$6.44** | **$8.94** |
| **"Operating-derived" EPS²** | **$2.68** | **$5.30** |
| Prior-year comparable | $2.13 | $4.19 |
| **Core EPS growth** | **+25.8%** | **+26.6%** |

¹ `NonoperatingIncomeExpense × (1 − effective tax rate) ÷ diluted shares`
² `OperatingIncomeLoss × (1 − effective tax rate) ÷ diluted shares` (illustrative; excludes net interest)

**Drivers of the non-operating line:** `DebtAndEquitySecuritiesGainLoss` of **$135,803M** in H1 2026, of which `EquitySecuritiesFvNiGainLoss` was **$135,946M** ($99,031M in Q2 alone). Realized gains were only $836M and unrealized gains on securities *still held* at period-end were $21,531M — implying the bulk of the gain was realized on disposal/remeasurement during the half. Non-operating income also absorbed interest expense of **$1,811M** (vs $295M, **+514%**) offset by interest income of $2,811M.

**Trader takeaway:** headline EPS of $14.24 (H1) / $9.11 (Q2) is not a repeatable earnings base. On a core basis the company earned **~$5.30 in H1 2026, up 26.6%** — still excellent, but roughly **40% of the headline number**. Any screen, quant model, or sell-side "beat" narrative anchored on GAAP EPS will overstate the sustainable earnings power and could make the stock appear materially cheaper than it is.

---

## 4. Balance Sheet: A Structural Transformation in Six Months

| Balance sheet item ($M) | 2026-06-30 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| **Total assets** | **921,983** | 595,281 | **+54.9%** |
| Current assets | 343,524 | 206,038 | +66.7% |
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| **Cash + short-term investments** | **242,474** | 126,843 | **+91.2%** |
| Available-for-sale debt securities | 99,500 | n/a | — |
| Accounts receivable, net | 69,175 | 62,886 | +10.0% |
| **Non-marketable equity securities (FV)** | **124,259** | 64,094 | **+93.9%** |
| — cumulative upward adjustments | 85,732 | 44,485 | +41,247 |
| — cumulative downward adjustments | (9,115) | (8,820) | +295 |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| Employee-related liabilities | 15,086 | 17,546 | −14.0% |
| Contract liabilities (deferred revenue) | 10,100 | 8,600 | +17.4% |
| **Debt (carrying amount)** | **101,085** | 49,085 | **+105.9%** |
| Finance lease liabilities | 2,590 | 2,500 | +3.6% |
| Operating lease liabilities | 18,037 | 15,954 | +13.1% |
| **Deferred tax liabilities, net** | **22,819** | 919 | **+2,383%** |
| **Loss contingency accruals (current)** | **17,356** | 15,594 | **+11.3%** |
| Convertible preferred stock | 18,023 | 0 | new |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| AOCI | (2,285) | (1,916) | — |
| Shares outstanding | 12,230M | 12,088M | +1.2% |

**Observations:**
1. **Liquidity is extraordinary.** $242.5B cash + short-term investments against ~$103.7B of debt + finance leases implies **net cash of roughly $139B**. Current ratio is approximately **2.6x** (estimated current liabilities ~$127–130B), so the negative-FCF quarter is not a solvency issue.
2. **The asset base ballooned $327B in six months**, of which roughly **$115.6B is liquid investments, $60.2B is non-marketable equity, and a large remainder is PP&E from capex**. Investments (liquid + private) now equal roughly **40% of total assets** — Alphabet is increasingly a holding company with an operating business attached.
3. **Leverage doubled.** Long-term debt went from $49.1B to $101.1B. Interest expense of $1,811M in H1 (+514%) annualizes to ~$3.6B — still trivially covered by $80.5B of operating income, but the direction of travel matters for 2027 EPS.
4. **A $22.8B deferred tax liability has appeared** (from $0.9B), almost entirely a consequence of unrealized investment appreciation. This is a real future cash/effective-tax drag and explains the effective rate moving from 17.1% → 19.1%.
5. **Legal/regulatory exposure is visible and growing:** loss contingency accruals of **$17.4B** (current), up $1.8B in six months, plus a **$3.0B payment made in Q3 2025** per the 10-K. This is consistent with major antitrust/ad-tech remedies but **the specific matters are not described in the returned dataset**.
6. **Working capital is healthy:** AR grew only 10.0% against 23.0% revenue growth — DSO improved to roughly **53 days** (from ~59), i.e., no deterioration in collections despite rapid revenue growth. Deferred revenue +17.4% supports forward visibility.
7. **Dilution has resumed.** Share count rose 1.2% after years of shrinkage, alongside a **$30.5B common stock issuance** and **$19.1B of convertible preferred issued on 2026-06-05**. Preferred dividends of $86M were paid in Q2 and sit *senior* to common.

---

## 5. Cash Flow: The Central Controversy

| Cash flow ($M) | H1 2026 | H1 2025 | Δ | Q2 2026 | Q2 2025 |
|---|---:|---:|---:|---:|---:|
| **Operating cash flow** | **84,859** | 63,897 | **+32.8%** | 39,069 | 27,747 |
| Capital expenditures (cash) | **80,598** | 39,643 | **+103.3%** | 44,924 | 22,446 |
| **Free cash flow (CFO − capex)** | **4,261** | 24,254 | **−82.4%** | **(5,855)** | +5,301 |
| Capex / revenue | **35.1%** | 21.2% | +1,390bp | **37.5%** | 23.3% |
| Capex / operating cash flow | **95.0%** | 62.0% | — | 115.0% | 80.9% |
| Depreciation | 13,586 | 9,485 | +43.2% | — | — |
| Share-based compensation | 15,200 | 11,500 | +32.2% | 8,000 | 6,000 |
| Net investing cash flow | (145,822) | (40,738) | n.m. | — | — |
| Net financing cash flow | **+86,320** | (26,033) | n.m. | — | — |
| Dividends paid | 5,231 | 4,977 | +5.1% | — | — |
| **Share repurchases** | **0** | **28,306** | **−100%** | 0 | — |

**Decomposition of the financing inflow (H1 2026):**
| Source | $M |
|---|---:|
| Debt issuance, net of costs | 56,226 |
| Common stock issuance | 30,499 |
| Convertible preferred issuance (2026-06-05) | 19,063 |
| Minority interest contributions | 3,758 |
| **Gross capital raised** | **~109,546** |
| Less: dividends | (5,231) |
| Less: debt/lease repayments | (5,253) |

**Decomposition of the investing outflow (H1 2026):**
| Use | $M |
|---|---:|
| Property, plant & equipment | 80,598 |
| Purchases of other (equity) investments | 22,051 |
| Net purchases of marketable securities | 9,784 |

### 5.1 Interpretation — the three findings that matter most

**(a) Free cash flow has effectively gone to zero, and turned negative in Q2.**
H1 FCF of **$4.3B (−82% YoY)** and a **Q2 deficit of −$5.9B** is a genuine regime change for a company that historically produced $60–75B of annual FCF. Capex absorbed **95% of operating cash flow** in H1 and **115% in Q2**. This is a deliberate strategic choice — funded by a **$109.5B capital raise** — but it removes the buyback/FCF-yield support that historically underpinned the multiple.

**(b) The capex-to-depreciation ratio (5.9x) is a 2027 margin warning.**
Capex of $80.6B in six months against depreciation of only $13.6B means the depreciation charge is set to accelerate materially as assets are placed in service. Depreciation already grew **43.2% YoY** while revenue grew 23.0%. Even if revenue growth holds at ~20%+, depreciation growth of 40–60% would mechanically compress operating margin by 200–400bp over the next 12–24 months. **This is the key medium-term risk to the current margin-expansion narrative.**

**(c) Capital allocation has inverted.**
- **Buybacks: $28.3B in H1 2025 → $0 in H1 2026.**
- **Equity issuance: $0 → $49.6B** (common + preferred). Alphabet raising *equity* at scale is a signal about the perceived cost/scale of the AI buildout, and about management's read on its own valuation.
- **Capex: +103% YoY.**
- **Dividend: raised ~5%** ($0.41 → $0.43 per half; Q1 $0.21, Q2 $0.22). Payout remains trivial (~6% of GAAP EPS, ~28% of core EPS) — the dividend is a formality, not a return-of-capital engine.

---

## 6. Investment Portfolio — The Hidden Second Business

| Metric ($M) | 2026-06-30 | 2025-12-31 |
|---|---:|---:|
| Non-marketable equity securities (carried at fair value) | 124,259 | 64,094 |
| Cumulative upward fair-value adjustments | 85,732 | 44,485 |
| Cumulative downward adjustments | (9,115) | (8,820) |
| AFS debt securities (fair value) | 99,500 | — |
| — of which maturing within 1 year | 16,699 | — |
| — 1–5 years | 50,932 | — |
| — 5–10 years | 15,288 | — |
| — >10 years | 16,581 | — |
| Unrealized loss position (AFS) | 416 | 178 |

- **$135.9B of equity-securities gains in six months** drove 63% of H1 EPS and $60.2B of the balance-sheet growth. The cumulative upward revaluation reserve on private holdings nearly doubled ($44.5B → $85.7B), consistent with **one or more large valuation events / mark-ups in Alphabet's private growth portfolio**.
- Gross unrealized losses on the AFS debt book widened modestly ($178M → $416M) but remain immaterial (0.4% of the $99.5B book); $53.2B of the portfolio sits in an unrealized-loss position, mostly <12 months — a rates-sensitivity, not a credit, issue.
- **Trading implication:** this book is a **$124B embedded call option** (≈13% of total assets, vs ~0% net debt after netting cash). Further IPO/round catalysts could produce repeat gains; equally, **mark-to-market reversals are a live risk to reported EPS** in any risk-off quarter. Investors should value the operating business and the investment portfolio **separately (sum-of-the-parts)** rather than applying a multiple to consolidated GAAP EPS.

---

## 7. Insider Activity

**No data available.** The insider-transactions source returned an explicit `DATA_UNAVAILABLE` for GOOGL for the period ending 2026-09-04. This report makes **no claim** about insider buying or selling, and traders should not interpret the absence as neutral or bearish — it is simply an unavailable input. Recommend sourcing Form 4 data directly before drawing conclusions.

---

## 8. Key Risks (ranked by likely impact on the equity)

| # | Risk | Evidence | Severity |
|---|---|---|---|
| 1 | **Depreciation cliff compressing margins in 2027** | Capex $80.6B H1 vs depreciation $13.6B (5.9x); depreciation already +43% YoY | High |
| 2 | **Sustained negative free cash flow** | Q2 FCF −$5,855M; H1 FCF −82% YoY; capex 37.5% of revenue | High |
| 3 | **Earnings-quality / valuation confusion** | 63% of H1 EPS from non-operating gains; headline EPS 2.7x core EPS | High |
| 4 | **Mark-to-market reversal risk on $124B private book** | $135.9B H1 gains; cumulative upward reserve $85.7B | High |
| 5 | **Rising leverage & interest burden** | Debt $101.1B (+106%); interest expense +514% YoY | Medium |
| 6 | **Dilution / preferred seniority** | Shares +1.2%; $30.5B common + $19.1B preferred issued; buyback at $0 | Medium |
| 7 | **Legal/regulatory drag** | $17.4B loss contingency accruals (+$1.8B in 6M); $3.0B paid Q3'25 | Medium |
| 8 | **Tax rate normalization** | ETR 17.1% → 19.1%; DTL $0.9B → $22.8B | Medium |
| 9 | **AI capex arms-race escalation** | Gross raise of $109.5B in one half; "other investments" $22.1B | Medium |

**Mitigants:** $242.5B liquid assets, ~$139B net cash, 35.0% operating margin, +30% operating income growth, 2.6x current ratio, and a $17.4B accrual already booked (i.e., known legal costs are largely provided for).

---

## 9. Actionable Insights for Traders

1. **Do not value GOOGL on GAAP EPS.** H1 2026 GAAP EPS of $14.24 includes ~$8.94 of after-tax investment gains. Use **core EPS of ~$5.30 (H1, +26.6% YoY)** and, better, **segment-level operating income / EV-to-operating-income**, treating the $242B liquid portfolio and $124B private book as separate SOTP assets.
2. **The bull case is real and operational, not just financial engineering.** Revenue +23–24%, gross margin +240bp, operating margin +190bp, operating income +30%. Positive operating leverage *while* spending at 37.5% of revenue on capex is the strongest evidence that AI is monetizing. Position sizing should respect this.
3. **Watch three specific prints next quarter:** (i) capex guidance/direction, (ii) whether FCF is negative again, (iii) depreciation growth. A second consecutive negative-FCF quarter combined with a capex guide-up is the most likely trigger for multiple compression.
4. **The buyback halt is a de-rating risk, not just a cash-flow item.** The historical $60–80B/yr repurchase bid was a structural support. Its absence, replaced by *issuance*, changes the supply/demand picture for the float.
5. **Trade the volatility of the private book.** Quarters with large upward marks will produce GAAP "beats" that are non-cash and non-recurring — fade the initial reaction if the beat is investment-driven and core operating income is in line. Conversely, a mark-down quarter that leaves operating income intact is likely a buying opportunity.
6. **Balance-sheet optionality is underappreciated.** ~$139B net cash plus a $124B private portfolio means downside is cushioned and management retains the ability to fund capex without further equity issuance — unless capex accelerates again, in which case watch for more preferred/common supply.
7. **Monitor the $22.8B deferred tax liability.** If investment gains are realized, cash taxes rise; if they reverse, the DTL unwinds. Either way, the 19.1% effective rate looks like the new baseline, not a one-off.

---

## 10. Summary Table

| Category | Metric | Value | Read-through |
|---|---|---|---|
| **Identity** | Company / Ticker | Alphabet Inc. / **GOOGL** | Class A common; latest 10-Q acc. `0001652044-26-000071` |
| **Scale** | H1 2026 revenue (derived) | $229,692M | +23.0% YoY |
| | Q2 2026 revenue (derived) | $119,796M | +24.2% YoY (Q1 +21.8%) — accelerating |
| **Profitability** | H1 gross margin | 62.0% | +240bp YoY |
| | H1 operating income | $80,466M | +30.0% YoY |
| | H1 operating margin | 35.0% | +190bp YoY — positive operating leverage |
| **Earnings quality** | H1 GAAP diluted EPS | $14.24 | +178% YoY |
| | H1 core (operating-derived) EPS | **~$5.30** | **+26.6% YoY**; GAAP is 2.7x core |
| | Non-operating gains, H1 | $135,699M | 63% of GAAP EPS; equity securities FVNI $135,946M |
| **Cash flow** | H1 operating cash flow | $84,859M | +32.8% YoY |
| | H1 capex | $80,598M | +103.3% YoY (35.1% of revenue) |
| | **H1 free cash flow** | **$4,261M** | **−82.4% YoY** |
| | **Q2 2026 free cash flow** | **−$5,855M** | First negative quarter in the dataset |
| | Capex / depreciation | 5.9x | Implies 2027 depreciation surge |
| **Balance sheet** | Total assets | $921,983M | +54.9% in six months |
| | Cash + ST investments | $242,474M | +91.2% |
| | Debt (carrying) | $101,085M | +105.9% |
| | Estimated net cash | **~$139B** | Fortress liquidity |
| | Non-marketable equity | $124,259M | +93.9%; 13.5% of assets |
| | Deferred tax liability | $22,819M | vs $919M — tax on unrealized gains |
| | Loss contingency accruals | $17,356M | +$1.8B in 6M; $3.0B paid Q3'25 |
| | Shares outstanding | 12,230M | +1.2% — dilution resumed |
| **Capital allocation** | H1 2026 buybacks | **$0** | vs $28,306M H1 2025 |
| | H1 2026 equity raised | **$49,562M** | $30,499M common + $19,063M preferred |
| | H1 2026 debt raised (net) | $56,226M | Total gross raise ~$109.5B |
| | Dividend per share (H1) | $0.43 | +~5% YoY; payout ~28% of core EPS |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | No inference made |
| **Verdict** | Fundamental stance | **Constructive on operations, cautious on headline EPS and FCF** | Core earnings power compounding ~26%, but GAAP optics and capex intensity are the swing factors |

**Bottom line:** GOOGL's underlying business is performing at its best in years — 23–24% revenue growth, widening gross and operating margins, and 30% operating-income growth despite the largest capex program in company history. However, **62% of the reported profit growth is non-operating investment revaluation, free cash flow has collapsed to zero (negative in Q2), and the company has pivoted from returning $28B/half to buying capital — $109.5B of it.** The equity should be owned on core operating momentum, sized against a 2027 depreciation cliff, and valued on a sum-of-the-parts basis that separately marks ~$139B of net cash and a $124B private investment book.