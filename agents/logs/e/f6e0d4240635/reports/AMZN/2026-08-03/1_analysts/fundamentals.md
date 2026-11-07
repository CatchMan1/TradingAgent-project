# AMZN — Fundamental Research Report
**Amazon.com, Inc. (NASDAQ: AMZN)** | Point-in-time: 2026-08-03 | Basis: SEC facts accepted through 2026-07-31

---

## 1. What is new this week (the driver of the entire analysis)

The single most important fundamental event of the past week is that **AMZN's Q2 2026 Form 10-Q was accepted by EDGAR on 2026-07-31 at 02:11 UTC** (accession 0001018724-26-000026). Everything below is sourced from that filing plus the prior Q1 2026 10-Q (filed 2026-04-30, accn 0001018724-26-000014). There is **no stale data** in this report — the Q2 balance sheet and H1 income/cash-flow statements are three days old.

Three headline facts from the new filing:

1. **Revenue re-accelerated and margins expanded materially** — Q2 2026 revenue +19.6% y/y to ~$200.6B, operating income +43% y/y.
2. **A ~$50.5B non-cash gain** on non-marketable equity securities hit Q2 non-operating income, inflating net income to $62.6B (EPS $5.75). This is the dominant driver of the headline numbers and must be stripped out.
3. **The capex/AI infrastructure supercycle has pushed trailing-twelve-month free cash flow negative** — TTM capex of $173.0B now exceeds TTM operating cash flow of $161.4B, funded by a near-doubling of debt in six months.

---

## 2. Company profile and how to read this data set

Amazon operates **three reportable segments** (the filing tags `NumberOfOperatingSegments = 3`), the standard structure of North America retail, International retail, and Amazon Web Services. Note: **segment-level revenue and segment operating income were not present in the extracted fact set**, so no segment splits are quoted here — I will not estimate them.

**Critical methodological note on revenue:** the extracted fact set contains **no revenue tag**. All revenue figures below are derived from the accounting identity:

> Revenue = `CostsAndExpenses` + `OperatingIncomeLoss`

This identity validates precisely against the comparative periods (Q2 2025 derived revenue of $167.70B, operating income $19.17B, net income $18.16B and diluted EPS $1.68 all tie out as internally consistent), so the derivation is reliable. Where a figure is derived, it is labelled.

---

## 3. Income statement — quarterly and half-year detail (derived revenue)

| $ millions | Q2 2026 | Q1 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|---|
| Revenue (derived) | **200,606** | 181,519 | 167,702 | **382,125** | 323,369 |
| y/y growth | **+19.6%** | +16.6% | — | **+18.2%** | — |
| Cost of goods & services | 95,778 | 87,463 | 80,809 | 183,241 | 157,785 |
| Gross profit | **104,828** | 94,056 | 86,893 | 198,884 | 165,584 |
| Gross margin | **52.3%** | 51.8% | 51.8% | 52.1% | 51.2% |
| Marketing | 11,698 | 10,314 | 11,416 | 22,012 | 21,179 |
| G&A | 2,788 | 2,587 | 2,965 | 5,375 | 5,593 |
| Fulfillment + tech & content (derived) | 62,881 | 57,303 | 53,341 | 120,184 | 101,236 |
| Total costs & expenses | 173,145 | 157,667 | 148,531 | 330,812 | 285,793 |
| **Operating income** | **27,461** | **23,852** | **19,171** | **51,313** | **37,576** |
| Operating margin | **13.7%** | 13.1% | 11.4% | **13.4%** | 11.6% |
| y/y operating income growth | **+43.2%** | +29.6% | — | **+36.6%** | — |
| Non-operating income/(expense) | **53,396** | 15,982 | 1,686 | **69,378** | 4,960 |
| Pre-tax income | 80,857 | 39,834 | 20,857 | 120,691 | 42,536 |
| Income tax | 18,199 | 9,560 | 2,678 | 27,759 | 7,231 |
| Effective tax rate | 22.5% | 24.0% | 12.8% | **23.0%** | 17.0% |
| **Net income** | **62,647** | **30,255** | **18,164** | **92,902** | **35,291** |
| Net margin | 31.2% | 16.7% | 10.8% | 24.3% | 10.9% |
| Diluted EPS | **$5.75** | $2.78 | $1.68 | **$8.53** | $3.27 |

### The three operating takeaways

**a) Two consecutive quarters of margin expansion against a rising depreciation load.** H1 2026 operating margin of 13.4% vs 11.6% is achieved *despite* depreciation & amortization rising **+32% y/y** (H1 2026 $38.9B vs $29.5B). That means gross-margin and cost-discipline gains are genuinely outpacing the D&A headwind — a strong quality signal for the operating story.

**b) Cost leverage is broad-based, not one-off.** Marketing expense grew only **+3.9%** (to 5.8% of revenue from 6.8%) and G&A actually **declined −3.9%** despite 18% revenue growth. Stock-based compensation *fell* to $10.07B in H1 2026 from $10.22B, i.e. **2.6% of revenue vs 3.2%** — real operating leverage, though $24.8B of unrecognised SBC remains to be expensed.

**c) Gross margin above 52% is the new anchor.** Q2 2026 gross profit of $104.8B (52.3%) vs $86.9B (51.8%) a year ago. If this holds, it supports the mix-shift thesis (higher-margin AWS, advertising and third-party services) — but note we only have two comparable quarters in this dataset, so the durability is unproven.

---

## 4. Earnings quality — the $50.5B question

This is the most important analytical issue in the report. **Q2 2026 net income of $62.6B is not an operating number.**

Composition of Q2 2026 non-operating income of $53.4B:
- **Upward price adjustment on equity securities without readily determinable fair value: +$50,486M** (H1 2026: **+$62,814M**, vs just $86M in H1 2025). This is a Level 3, mark-to-model remeasurement of private-company equity stakes.
- Unrealised gain on marketable securities: +$1,319M
- Equity securities FV-NI gain: +$1,300M
- Interest income: +$1,295M
- FX gain: +$227M
- Interest expense: −$1,314M
- Warrant fair-value adjustment: −$1,449M

**Backing out the marks:**

| $ millions | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|
| Reported pre-tax income | 80,857 | 20,857 | 120,691 | 42,536 |
| Less: private-equity upward adjustments | (50,486) | (49) | (62,814) | (86) |
| Less: marketable/equity FV-NI gains | (2,619) | (781) | (884) | (438) |
| **"Clean" pre-tax income** | **~27,752** | **~20,027** | **~56,993** | **~42,012** |
| "Clean" net income (est., ~23%/17% tax) | **~21,500** | **~16,600** | **~43,900** | **~34,900** |
| **"Clean" diluted EPS (est.)** | **~$1.97** | **~$1.54** | **~$4.03** | **~$3.23** |

**Insight for traders:** headline EPS grew **+242%** y/y in Q2 (5.75 vs 1.68), but **operating EPS grew roughly +28%**. That is still an excellent result — but it is a completely different magnitude, and any headline-based screen or naive multiple will misprice this quarter.

**Two corroborating red flags on earnings quality:**
1. `DeferredIncomeTaxExpenseBenefit` was **+$30,489M** in H1 2026 versus **cash taxes paid of only $3,978M** against a $27,759M tax provision. The earnings are non-cash and the tax is deferred — consistent with unrealised gains that are not yet taxable. When those stakes are monetised, a large cash tax bill crystallises.
2. **AOCI jumped from $28.2B to $66.3B** in six months (+$38.1B), and the filing tags `DebtSecuritiesAvailableForSaleUnrealizedGainLoss = $92,000M` for H1 2026 — a figure that cannot be explained by the $97.9B AFS debt portfolio, whose gross unrealised gain is only **$7M** and gross loss **$67M**. This tag is either a reclassification of the private-stake revaluations through OCI or a tagging inconsistency; either way, **~$38B of book equity accretion in six months is mark-driven, not cash-driven.** Treat it as unverified until the OCI note is read in full.

---

## 5. Balance sheet — scale, liquidity, and a decisive shift in capital structure

| $ millions | 2026-06-30 | 2025-12-31 | Change |
|---|---|---|---|
| Cash & equivalents | 78,213 | 86,810 | −8,597 |
| Marketable securities (AFS debt) | 97,900 | 45,800 | **+52,100** |
| **Cash + securities** | **176,113** | **132,610** | **+43,503** |
| Accounts receivable, net | 88,092 | 67,729 | **+30.1%** |
| Inventories | 38,184 | 38,325 | −0.4% |
| Total current assets | 249,264 | 229,083 | +8.8% |
| **Non-marketable equity securities** | **122,300** | **16,200** | **+655%** |
| **Total assets** | **1,095,689** | **818,042** | **+34.0%** |
| Accounts payable | 147,440 | 121,909 | +20.9% |
| Accrued liabilities | 73,406 | 75,520 | −2.8% |
| Total current liabilities | 241,274 | 218,005 | +10.7% |
| Long-term debt — noncurrent | **128,894** | 65,648 | **+96.3%** |
| Long-term debt — current | 3,330 | 2,748 | +21.2% |
| Finance lease liabilities | 13,451 | 12,286 | +9.5% |
| Operating lease liabilities | 96,320 | 89,252 | +7.9% |
| Deferred revenue (current) | 20,428 | 20,576 | −0.7% |
| Additional paid-in capital | 149,619 | 140,024 | +6.9% |
| Accumulated OCI | 66,287 | 28,230 | +134.8% |
| Shares outstanding (M) | 10,783 | 10,731 | +0.5% |
| Diluted shares implied (EPS) | ~10,895 | — | — |

### What jumps out

1. **Total assets grew $277.6B (+34%) in six months.** Roughly $106B of that is the private-equity portfolio revaluation/purchases; the rest is infrastructure capex (AWS/AI capacity) plus M&A. Total assets have become substantially a mark-to-model and long-lived-asset balance sheet.
2. **Debt nearly doubled.** Long-term debt (incl. current) went from $68.4B to $132.2B (+$63.8B). Add finance leases → **$145.7B of debt**, plus **$96.3B of operating leases** → **$242.0B of total fixed obligations**.
3. **But AMZN is still net cash.** $176.1B of cash + securities against $145.7B of debt = **~$30B net cash**, before operating leases. Leverage is therefore not a solvency issue — it is an *interest-cost and flexibility* issue.
4. **Current ratio is thin at 1.03x** ($249.3B / $241.3B) vs 1.05x at year-end. Typical for Amazon's negative-working-capital retail model, but the cushion is narrowing.
5. **Receivables +30.1% in six months outpaces the ~18% revenue growth.** AR days on Q2 revenue ≈ **40 days**. Mix (AWS + advertising) explains part of it, but this is worth monitoring for collections and working-capital drag.
6. **No buyback and minimal dilution:** shares +0.5% in six months, APIC +$9.6B (SBC). Capital is going to capex, M&A and equity stakes — not to shareholders.
7. **Contractual obligations of $650.0B** (of which $78.1B due in the next twelve months and a further $42.8B in the remainder of FY2026). This is the clearest quantitative evidence of long-dated capacity/power/content commitments underpinning the AI build-out. It is also a genuine execution risk if demand assumptions slip.

*Equity note:* the `StockholdersEquity` tag was not in the extract. Roll-forward estimate: Dec 2025 equity ≈ $419B → Jun 2026 ≈ **$555–565B** (net income $92.9B + AOCI $38.1B + SBC $10.1B). On that basis **debt/equity ≈ 24–26%** — comfortably investment grade.

---

## 6. Cash flow — the capex supercycle and the FCF cliff

| $ millions | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | TTM (Jul'25–Jun'26) | FY2025 (derived) |
|---|---|---|---|---|---|---|
| Operating cash flow | **45,387** | 32,515 | **71,419** | 49,530 | **161,403** | 139,514 |
| y/y growth | +39.6% | — | **+44.2%** | — | +33.2% | — |
| Capex (productive assets) | **54,208** | 32,183 | **98,411** | 57,202 | **173,028** | 131,819 |
| y/y growth | +68.4% | — | **+72.0%** | — | +60.7% | — |
| **Free cash flow** | **(8,821)** | 332 | **(26,992)** | (7,672) | **(11,625)** | **+7,695** |
| D&A | 19,988 | 15,227 | 38,933 | 29,489 | 75,200 | 65,756 |
| Capex / revenue | **27.0%** | 19.2% | **25.8%** | 17.7% | — | — |
| Acquisitions (net of cash) | 24,359 | 1,700 | **39,767** | 1,652 | 41,956 | — |
| Investing cash flow | (79,245) | (39,424) | (143,457) | (69,227) | (216,775) | — |
| Financing cash flow | +10,146 | (2,539) | **+62,913** | (2,586) | **+75,160** | — |

### Interpretation — this is the core debate

- **Operating cash flow is excellent and accelerating (+44% y/y in H1).** The business is generating more cash than ever.
- **But capex grew 72% y/y and consumed 138% of operating cash flow in H1.** Capex intensity has gone from 17.7% to 25.8% of revenue in one year. TTM capex of $173.0B vs TTM OCF of $161.4B means **AMZN has crossed into negative TTM free cash flow (−$11.6B)**, down from **+$7.7B in FY2025**.
- **The shortfall is being funded with debt and asset sales**, not with cash: $82.4B of gross debt issuance in H1 2026 (plus $15.4B short-term), $62.9B of net financing inflow, alongside $39.8B of cash acquisitions.
- **H1 2026 FCF of −$27.0B vs −$7.7B in H1 2025** is a $19.3B deterioration. This is a *deliberate* investment cycle, not distress — but it means **FCF-based valuation screens will look much worse than earnings-based screens for the next several quarters**, and the market's tolerance for it depends entirely on forward AWS/AI revenue visibility.

---

## 7. Capital allocation, financing, and the "equity stake economy"

- **Debt:** `ProceedsFromIssuanceOfLongTermDebt` H1 2026 = **$66,998M** (TTM $81,925M) vs repayments of $2,752M → net LT debt add of $64.2B. Short-term borrowings were rolled heavily ($15.4B raised / $15.7B repaid) — commercial paper is being used as a liquidity buffer.
- **Interest cost is inflecting:** Q2 2026 interest expense of **$1,314M vs $516M a year ago (+155%)**; H1 2026 $2,114M vs $1,057M. Annualising Q2 → ~$5.3B/yr, still easily covered by Q2 operating income of $27.5B (~21x), but the trend is unmistakable as the debt load doubles.
- **Investment income is offsetting it:** H1 2026 interest income of $2,430M vs $2,151M — net interest cost is still modest.
- **Equity stakes are now a first-order asset class for AMZN:** $122.3B of non-marketable equity securities (11.2% of total assets), up from $16.2B. This appears to be the mechanism by which AMZN is monetising its position in AI compute counterparties — the $50.5B Q2 mark-up and the *negative* warrant fair-value adjustment (−$1,449M) both point to a large, concentrated, private-position exposure embedded in the equity base and the P&L.
- **Contractual commitments of $650B** ($78.1B due within 12 months) are the forward funding requirement that explains why the balance sheet is being levered now.

---

## 8. Insider transactions

**Data unavailable.** The vendor archive returned: *"no authorized, point-in-time insider-transactions archive for AMZN by 2026-08-03."* I will not infer, estimate or fabricate insider activity. Traders should source Form 4 filings directly from EDGAR if insider signal is part of the thesis. Note that share count rose only 0.5% in six months and no treasury/buyback line appears in the extracted financing tags, so there is no evidence in this dataset of either notable issuance or repurchase.

---

## 9. Red flags and risk register

| # | Risk | Evidence | Severity |
|---|---|---|---|
| 1 | **Negative TTM free cash flow** | TTM capex $173.0B > TTM OCF $161.4B → FCF −$11.6B; H1 2026 FCF −$27.0B vs −$7.7B | High |
| 2 | **Earnings quality / mark-to-model** | $62.8B of H1 pre-tax income from Level 3 private-equity revaluations; 68% of H1 net income is non-operating | High |
| 3 | **Debt doubling and rising interest** | LTD $68.4B → $132.2B in 6 months; interest expense +155% y/y in Q2 | Medium-High |
| 4 | **Depreciation wave still ramping** | D&A +32% y/y with capex +72%; D&A/revenue 10.2% vs 9.1% — margin tailwind must keep outpacing this | Medium-High |
| 5 | **$650B of contractual obligations** | $78.1B due within 12 months | Medium-High |
| 6 | **Tax rate normalisation** | ETR 23.0% H1 2026 vs 17.0% H1 2025; cash taxes only $4.0B vs $27.8B provision (deferral, not avoidance) | Medium |
| 7 | **Receivables growth > revenue growth** | AR +30.1% in 6 months; 40 days | Medium |
| 8 | **OCI / AFS tag inconsistency** | $92.0B `DebtSecuritiesAvailableForSaleUnrealizedGainLoss` cannot be reconciled to a $97.9B portfolio with $7M gross gains | Medium (needs verification) |
| 9 | **Thin current ratio** | 1.03x vs 1.05x | Low-Medium |
| 10 | **Concentration risk in a single private-stake complex** | $122.3B of Level 3 assets; reversal would hit both book value and reported EPS | Medium |

---

## 10. Actionable conclusions for traders

**The bullish case is real and it is operational, not accounting:**
- Revenue growth **accelerated** from +16.6% (Q1) to **+19.6%** (Q2 2026), on top of an already strong +18.2% H1.
- Operating margin expanded 230bp y/y in Q2 (13.7% vs 11.4%) **while depreciation rose 31%** — this is the highest-quality line in the entire filing.
- Operating cash flow +44% y/y in H1 to $71.4B. Advertising/marketing cost growing only 3.9% and G&A down 3.9% confirms genuine leverage.
- Net cash position (~$30B) and ~25% debt/equity mean the balance sheet can absorb this build-out.

**The bear case is a cash-flow and quality-of-earnings case:**
- **Do not anchor on the $5.75 quarterly EPS or $8.53 half-year EPS.** On a clean basis (excluding the private-equity and marketable-security marks), Q2 EPS is **~$1.97** and H1 EPS **~$4.03**. Screens and consensus multiples built on the headline will be ~2.9x too high on Q2.
- **FCF is negative on a trailing basis** and the H1 deterioration is accelerating (−$27.0B vs −$7.7B). Until capex/revenue rolls over, FCF-based valuation support is absent.
- **Debt-funded capex + $650B of commitments** means the financing trajectory, not the operating trajectory, is the swing variable if demand visibility softens.

**Specific things to monitor (in priority order):**
1. **Q3 2026 capex and FY capex commentary** — does capex/revenue exceed 26–27%? Any guidance implying capex >$200B annualised would extend the negative-FCF regime.
2. **AWS revenue growth and AWS operating margin** — the only durable justification for 27%-of-revenue capex. (Not available in this extract; must be taken from the segment note.)
3. **The size and marks of the private-equity portfolio** — $122.3B now. A 20% markdown would wipe out ~$24B of book value and ~$2.20 of EPS. Ask whether the Q2 mark-up is transaction-validated or model-based.
4. **Interest expense run-rate** — $1,314M in Q2; crossing ~$1.6–1.8B/quarter would signal the debt build is outpacing internally generated cash.
5. **Operating margin durability ex-D&A** — the key question is whether gross margin can hold above 52% as depreciation/revenue climbs from 10.2% toward 12%+.
6. **Cash taxes vs. deferred taxes** — a shift toward cash tax payments ($4.0B vs $27.8B provision) would mark the beginning of monetisation of the gains, and simultaneously confirm the value is real.

**Positioning summary:** the operating business is inflecting positively and the Q2 print is genuinely strong on an ex-marks basis (+28% y/y operating EPS). The reported numbers, however, are heavily flattered by a discrete non-cash event, while free cash flow has turned negative and leverage has doubled. The correct trade framing is **"own the operating leverage, discount the mark-up, and stay wary of the FCF trajectory"** — not "EPS tripled."

---

## 11. Explicit data limitations (so the next analyst can build on this)

- **No revenue tag** in the vendor extract; all revenue is derived as `CostsAndExpenses + OperatingIncomeLoss` (validated against known comparatives).
- **No segment-level** revenue, operating income, or AWS metrics available.
- **No `StockholdersEquity`, `Liabilities`, `PropertyPlantAndEquipmentNet`, or cash-flow tags for SBC/buyback lines** in the extract; equity and debt/equity are roll-forward estimates and are labelled as such.
- **No income-statement or balance-sheet history before FY2025** — the dataset is point-in-time (two 10-Qs), so multi-year trend claims are limited to H1 2025, H1 2026, TTM and derived FY2025.
- **Annual-frequency calls returned the same quarterly data** — no separate 10-K series exists in this package.
- **Insider transactions unavailable** (explicitly; not inferred).

---

## Key points summary table

| Category | Metric | Value | Signal |
|---|---|---|---|
| **Filing** | Q2 2026 10-Q accepted | 2026-07-31 | Fresh (3 days) |
| Growth | Q2 2026 revenue (derived) | $200.6B, **+19.6% y/y** | Bullish — accelerating |
| Growth | H1 2026 revenue (derived) | $382.1B, +18.2% y/y | Bullish |
| Profitability | Q2 2026 operating income | $27.5B, **13.7% margin** (vs 11.4%) | Bullish — +43% y/y |
| Profitability | H1 2026 operating income | $51.3B, 13.4% margin | Bullish — +36.6% y/y |
| Margins | Q2 2026 gross margin | **52.3%** (vs 51.8%) | Bullish |
| Cost control | Marketing / G&A y/y | +3.9% / **−3.9%** | Bullish leverage |
| Reported EPS | Q2 2026 diluted | **$5.75** (+242% y/y) | Misleading — mark-inflated |
| **Clean EPS (est.)** | Q2 2026 ex-marks | **~$1.97** (+~28% y/y) | Genuinely strong |
| Earnings quality | H1 2026 private-equity mark-up | **+$62.8B** pre-tax | 🔴 Red flag — 68% of net income |
| Earnings quality | Non-marketable equity securities | **$122.3B** (was $16.2B) | 🔴 Level 3 concentration |
| Cash generation | H1 2026 operating cash flow | $71.4B, +44.2% y/y | Bullish |
| Cash generation | H1 2026 capex | $98.4B, **+72% y/y** | Capex supercycle |
| **Free cash flow** | TTM (Jul'25–Jun'26) | **−$11.6B** (FY2025: +$7.7B) | 🔴 FCF cliff |
| Free cash flow | H1 2026 | **−$27.0B** (H1 2025: −$7.7B) | 🔴 Deteriorating |
| Capex intensity | Q2 2026 capex/revenue | **27.0%** (vs 19.2%) | Watch closely |
| Leverage | Long-term debt | $132.2B (from $68.4B) — **+96%** | 🔴 Doubled in 6 months |
| Leverage | Interest expense Q2 2026 | $1,314M vs $516M | +155% y/y |
| Liquidity | Cash + marketable securities | **$176.1B** | Strong |
| Leverage | Net cash (ex-op leases) | **~+$30B** | Still net cash |
| Leverage | Debt/equity (est.) | ~24–26% | Manageable |
| Working capital | Current ratio | 1.03x (1.05x) | Thin |
| Working capital | Receivables | $88.1B, **+30.1%** in 6 months | Monitor |
| Obligations | Total contractual obligations | **$650.0B** ($78.1B due <12m) | 🔴 Execution risk |
| Tax | H1 2026 effective tax rate | 23.0% (vs 17.0%) | Normalising |
| Tax | Cash taxes paid vs provision | $4.0B vs $27.8B | Deferral, not avoidance |
| Capital return | Buybacks / dividends | None evident; shares +0.5% | Reinvestment mode |
| Insider activity | Form 4 data | **Unavailable** | Cannot assess |
| M&A | H1 2026 acquisitions | **$39.8B** (vs $1.7B) | Major step-up |
| Segments | Reportable segments | 3 | Segment detail N/A |

**Bottom line on AMZN:** the operating engine is firing on all cylinders — accelerating revenue, expanding margins against a rising depreciation load, and +44% operating cash flow. But the quarter's headline profitability is dominated by a $50.5B non-cash mark-to-model gain, trailing free cash flow has turned **negative**, and debt has **doubled** to fund a 27%-of-revenue capex programme backed by **$650B of contractual commitments**. Trade the operating leverage; discount the mark-up; and treat capex/revenue and AWS segment growth as the two variables that decide whether this is a compounding investment cycle or an over-build.