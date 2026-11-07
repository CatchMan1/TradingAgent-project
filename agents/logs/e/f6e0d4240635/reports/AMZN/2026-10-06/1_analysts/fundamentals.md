# AMZN — Fundamental Research Report
**Analysis date:** 2026-10-06 | **Latest SEC filing in dataset:** Form 10-Q for period ended 2026-06-30, accepted 2026-07-31 | **Ticker:** AMZN

---

## 1. Executive Summary

AMZN's most recent reported quarter (Q2 2026) shows **genuinely strong operating momentum** — revenue up ~19.6% YoY, operating income up ~43%, and operating margin expanding ~226 bps — but **headline EPS is heavily distorted by a large non-cash, non-operating equity revaluation**. Reported Q2 2026 net income of $62.6B includes roughly **$50.5B of pre-tax upward fair-value adjustments on equity securities without readily determinable fair value** (≈$12.3B in Q1 2026, ≈$62.8B for H1 2026). Adjusted for these marks, Q2 EPS is closer to **~$2.16 versus the reported $5.75**, and H1 EPS closer to **~$4.12 versus $8.53**.

At the same time, AMZN is in the middle of an **unprecedented capital-expenditure cycle**: TTM purchases of productive assets reached **$173.0B (+60.7% YoY)**, Q2 capex alone was **$54.2B (27% of revenue)**, and trailing-twelve-month **free cash flow turned negative (−$11.6B)** versus +$13.5B a year earlier. The gap is being funded with debt — long-term debt nearly doubled to **$133.0B** in six months, with **$82.4B of new long- and short-term borrowings** in H1 2026, alongside **$39.8B of business acquisitions**.

**Bottom line for traders:** the operating business is accelerating and margins are expanding, but reported earnings quality is poor this year and FCF is negative. Valuation work should use adjusted, ex-mark earnings; the key forward debate is whether the AI/infrastructure capex converts into AWS/advertising revenue before depreciation and interest expense compress margins. The next fundamental catalyst is the Q3 2026 report (expected late October 2026); no newer SEC financials than the 2026-07-31 10-Q are in the dataset.

---

## 2. Company Profile

AMZN is Amazon.com, Inc., a global technology and e-commerce conglomerate. The filing confirms **three operating segments** (`NumberOfOperatingSegments = 3`, period ended 2026-06-30): **North America, International, and Amazon Web Services (AWS)**. The business spans:

- **Online retail & third-party marketplace** (1P and 3P), supported by a global fulfillment and logistics network
- **AWS** — cloud compute, storage, database, and an expanding AI infrastructure/services stack
- **Advertising** — sponsored products/brands, display, and streaming TV advertising
- **Subscription services** — Prime, Prime Video, Music, etc.
- **Physical stores** (Whole Foods), devices (Echo, Kindle, Fire), and other businesses

**Data limitation:** the vendor feed confirms the three-segment structure but does **not** break out segment revenue or segment operating income. It also does not expose a standalone `Revenue` tag; revenue below is derived as `OperatingIncomeLoss + CostsAndExpenses`, which reconciles exactly. Prior full-year income statements (FY2024/FY2025) are not exposed in this dataset. No share-price data was available, so valuation multiples cannot be computed here.

---

## 3. Income Statement Analysis (Q2 2026 and H1 2026)

### 3.1 Reported results

| Metric ($M) | Q2 2025 | Q2 2026 | YoY | H1 2025 | H1 2026 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | 167,702 | 200,606 | **+19.6%** | 323,369 | 382,125 | **+18.2%** |
| Cost of goods & services | 80,809 | 95,778 | +18.5% | 157,785 | 183,241 | +16.1% |
| Gross profit | 86,893 | 104,828 | +20.6% | 165,584 | 198,884 | +20.1% |
| Gross margin | 51.8% | **52.3%** | +45 bps | 51.2% | **52.1%** | +84 bps |
| Total costs & expenses | 148,531 | 173,145 | +16.6% | 285,793 | 330,812 | +15.8% |
| Operating income | 19,171 | **27,461** | **+43.2%** | 37,576 | **51,313** | **+36.6%** |
| Operating margin | 11.43% | **13.69%** | +226 bps | 11.62% | **13.43%** | +181 bps |
| Non-operating income | 1,686 | 53,396 | n.m. | 4,960 | 69,378 | n.m. |
| Pre-tax income | 20,857 | 80,857 | +287.7% | 42,536 | 120,691 | +183.7% |
| Tax expense | 2,678 | 18,199 | +579.6% | 7,231 | 27,759 | +283.9% |
| Effective tax rate | 12.8% | 22.5% | — | 17.0% | 23.0% | — |
| Net income | 18,164 | **62,647** | **+244.9%** | 35,291 | **92,902** | **+163.3%** |
| Diluted EPS | $1.68 | **$5.75** | +242.3% | $3.27 | **$8.53** | +160.9% |
| Diluted shares | ~10,812 | ~10,897 | +0.8% | ~10,793 | ~10,891 | +0.9% |

**Q1 2026 for reference:** revenue $181,519M (+16.6% YoY), operating income $23,852M (13.14% margin), net income $30,255M, diluted EPS $2.78.

### 3.2 The earnings-quality issue: $62.8B of equity marks

The single most important insight in this report:

- **`EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount` = $50,486M in Q2 2026 and $62,814M in H1 2026** (vs just $49M in Q2 2025 and $86M in H1 2025).
- **`EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` jumped from $16.2B at 2025-12-31 to $122.3B at 2026-06-30** — a $106.1B increase, of which ~$62.8B is fair-value appreciation and the rest likely additions.
- This is booked inside **non-operating income** ($53.4B in Q2, $69.4B in H1), which is **63% of Q2 pre-tax income** and **52% of H1 pre-tax income**.
- It is **non-cash** and **mark-to-model** (Level 3, no readily determinable market price). It is also reflected in the effective tax rate rising to ~22.5% via **deferred tax expense of $17.7B in Q2 / $30.5B in H1**, even though **cash taxes paid were only $2.7B in Q2 / $4.0B in H1**.

**Adjusted (ex-mark) earnings estimate:**

| | Q2 2025 | Q2 2026 adj. | H1 2025 | H1 2026 adj. |
|---|---:|---:|---:|---:|
| Pre-tax ex equity marks ($M) | ~20,808 | ~30,371 | ~42,450 | ~57,877 |
| Tax @ ~22.5% | — | 6,834 | — | 13,022 |
| Adjusted net income ($M) | ~18,164 | **~23,537** | ~35,291 | **~44,855** |
| Adjusted diluted EPS | $1.68 | **~$2.16** | $3.27 | **~$4.12** |
| Adjusted growth | — | **~+28.6%** | — | **~+26.0%** |

**Takeaway:** underlying EPS growth is a healthy ~26–29%, not the reported ~160–240%. Anyone annualizing $5.75 × 4 = $23.00 will overstate run-rate earnings by roughly 2.5x. Conversely, the underlying franchise is still compounding EPS at a mid-to-high-20s rate.

### 3.3 Operating cost discipline is a real positive

- **Stock-based comp fell to $6,038M in Q2 2026 from $6,534M** (−7.6% YoY) and $10,070M vs $10,223M in H1 — SBC is now only **3.01% of revenue vs 3.90%** a year ago. This is a meaningful quality improvement.
- **Marketing expense +2.5% YoY** in Q2 ($11,698M) against +19.6% revenue growth — marketing intensity fell from 6.81% to **5.83%** of revenue.
- **G&A fell 6.0% YoY** to $2,788M (1.39% of revenue vs 1.77%).
- **D&A rose 31.3% YoY** to $19,988M in Q2 (9.96% of revenue vs 9.08%) and $38,933M in H1 (+32.0%). This is the leading edge of the capex wave hitting the P&L and is the main structural margin headwind to watch.
- **Interest expense more than doubled**, to $1,314M in Q2 from $516M, and $2,114M vs $1,057M in H1 — a direct consequence of the debt-funded buildout. Interest coverage is still comfortable at **~20.9x** (Q2 operating income / interest expense) but has roughly halved YoY. Interest income of $1,295M now barely offsets interest expense.

---

## 4. Balance Sheet Analysis

| ($M) | 2025-12-31 | 2026-06-30 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 86,810 | 78,213 | −9.9% |
| Available-for-sale debt securities | 45,800 | 97,900 | +113.8% |
| **Cash + AFS securities** | **132,610** | **176,113** | **+32.8%** |
| Accounts receivable, net | 67,729 | 88,092 | +30.1% |
| Inventory, net | 38,325 | 38,184 | −0.4% |
| Current assets | 229,083 | 249,264 | +8.8% |
| **Total assets** | **818,042** | **1,095,689** | **+33.9%** |
| Accounts payable | 121,909 | 147,440 | +20.9% |
| Accrued liabilities | 75,520 | 73,406 | −2.8% |
| Current liabilities | 218,005 | 241,274 | +10.7% |
| Long-term debt (total) | 68,836 | **132,995** | **+93.2%** |
| — of which current | 2,748 | 3,330 | +21.2% |
| — of which non-current | 65,648 | 128,894 | +96.3% |
| Finance lease liabilities | 12,286 | 13,451 | +9.5% |
| Operating lease liabilities | 89,252 | 96,320 | +7.9% |
| Contract liabilities (current) | 20,576 | 20,428 | −0.7% |
| Equity securities w/o readily determinable FV | 16,200 | **122,300** | **+655%** |
| AOCI | 28,230 | 66,287 | +134.8% |

### Key balance-sheet observations

1. **Liquidity is adequate but not deep.** Current ratio = **1.03x** (249,264 / 241,274); quick ratio = **0.88x**. Working capital is only **$7.99B**. AMZN relies on operating cash flow and continuous debt-market access rather than a large liquidity cushion.
2. **Debt has been transformed in six months.** Total borrowings plus leases rose to **$242.8B** from **$170.4B** (+42.5%). Net debt *including* leases is **~$66.7B**; excluding leases AMZN still holds **net cash of ~$43.1B** (debt $133.0B vs cash+AFS $176.1B). Gross debt/EBITDA is roughly **0.7x ex-leases and ~1.3x including leases** — not stretched, but the trend is clearly leveraging.
3. **Receivables are growing faster than revenue** (+30.1% vs +18.2% H1) — worth monitoring for collections and for mix shift toward advertising/AWS (which carry receivables), but the allowance for doubtful accounts rose only modestly ($2.4B → $2.8B).
4. **Inventory is flat** ($38.2B) against ~19.6% revenue growth — excellent inventory efficiency and a sign the retail business is not overstocked.
5. **The asset base is increasingly mark-to-model.** The **$122.3B** of non-marketable equity securities equals **11.2% of total assets**. Combined with a **$38.1B increase in AOCI** in H1, the balance sheet now carries substantial fair-value sensitivity that is not reflected in operating cash flow. Note: the feed does not break out all OCI components (FX translation was only −$1.56B), so the full composition of the AOCI build cannot be verified from this dataset.
6. **Contractual obligations total $650.0B** at 2026-06-30, with **$78.1B due within twelve months** (including $42.8B in the remainder of FY2026), $53.4B in year two, $46.8B in year three, and $42.2B in year four. This includes operating leases ($116.4B) and finance leases ($16.7B) plus purchase/content/capacity commitments. The near-term claim on cash flow is meaningful but manageable against ~$161B TTM operating cash flow.

---

## 5. Cash Flow Analysis — The Central Tension

| ($M) | TTM to 2025-06-30 | TTM to 2026-06-30 | YoY |
|---|---:|---:|---:|
| Operating cash flow | 121,137 | **161,403** | **+33.2%** |
| Purchases of productive assets (capex) | 107,656 | **173,028** | **+60.7%** |
| **Free cash flow (OCF − capex)** | **+13,481** | **−11,625** | **n.m.** |
| Acquisitions of businesses, net | 4,809 | **41,956** | +772% |
| Purchases of marketable securities | 46,731 | 72,902 | +56.0% |
| Proceeds from sale/maturity of securities | 30,924 | 67,090 | +117.0% |
| Net cash used in investing | (123,569) | **(216,775)** | +75.4% |
| Proceeds from LT debt | 746 | **81,925** | n.m. |
| Proceeds from ST debt | 8,187 | 20,798 | +154.0% |
| Net cash from financing | (8,652) | **+75,160** | n.m. |
| Net change in cash | — | **+19,474** | — |

**Quarterly cash flow detail:**

| ($M) | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 |
|---|---:|---:|---:|---:|
| Operating cash flow | 17,015 | 32,515 | 26,032 | **45,387** |
| Capex | 25,019 | 32,183 | 44,203 | **54,208** |
| Free cash flow | (8,004) | +332 | **(18,171)** | **(8,821)** |
| Capex / revenue | 16.1% | 19.2% | 24.4% | **27.0%** |
| OCF / revenue | 10.9% | 19.4% | 14.3% | **22.6%** |

### Interpretation

- **Operating cash flow is compounding strongly** (+33% TTM, +44% H1), and OCF margin of 22.6% in Q2 is a genuine high. Cash taxes remain very low ($6.6B TTM vs $27.8B of H1 book tax expense), which flatters OCF — a **cash-tax normalization is a latent FCF risk**.
- **Capex is now consuming more than 100% of operating cash flow** (TTM capex/OCF = 107%; H1 2026 = 138%). Free cash flow is negative on both a TTM and H1 basis.
- **The funding mix has flipped from self-funding to debt funding.** AMZN raised **$82.4B of debt in H1 2026** (plus $20.8B ST) and executed **$39.8B of acquisitions** (including $24.4B in Q2 alone). Essentially all of the negative FCF and M&A was financed with borrowings.
- **Earnings are not being confirmed by cash flow this year.** H1 2026 net income of $92.9B exceeded operating cash flow of $71.4B, precisely because ~$62.8B of income was non-cash equity marks. On an adjusted basis, cash conversion is very strong (~1.6–1.9x), which supports the quality of the *operating* franchise.

---

## 6. Financial History & Trend Summary

Only the latest 10-Q and its prior-year comparatives are exposed by the data vendor; the table below uses all available periods plus derived trailing-twelve-month cash flow.

| Metric | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 | H1 2025 | H1 2026 | TTM Jun-26 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Revenue ($M, derived) | 155,667 | 167,702 | 181,519 | 200,606 | 323,369 | 382,125 | n/a |
| Gross margin | 50.6% | 51.8% | 51.8% | 52.3% | 51.2% | 52.1% | n/a |
| Operating income ($M) | 18,405 | 19,171 | 23,852 | 27,461 | 37,576 | 51,313 | n/a |
| Operating margin | 11.8% | 11.4% | 13.1% | 13.7% | 11.6% | 13.4% | n/a |
| Net income ($M) | 17,127 | 18,164 | 30,255 | 62,647 | 35,291 | 92,902 | **135,281** |
| Diluted EPS | $1.59 | $1.68 | $2.78 | $5.75 | $3.27 | $8.53 | n/a |
| SBC ($M) | 3,689 | 6,534 | 4,032 | 6,038 | 10,223 | 10,070 | n/a |
| D&A ($M) | 14,262 | 15,227 | 18,945 | 19,988 | 29,489 | 38,933 | **75,200** |
| Capex ($M) | 25,019 | 32,183 | 44,203 | 54,208 | 57,202 | 98,411 | **173,028** |
| Operating cash flow ($M) | 17,015 | 32,515 | 26,032 | 45,387 | 49,530 | 71,419 | **161,403** |
| Free cash flow ($M) | (8,004) | 332 | (18,171) | (8,821) | (7,672) | (26,992) | **(11,625)** |

**Trend read:** margin expansion is sequential and broad-based (gross margin +45 bps YoY in Q2, operating margin +226 bps), while the capex curve is steepening faster than revenue. Q2 2026 is the fifth consecutive quarter in the dataset with capex intensity rising.

---

## 7. Segment & Business Commentary

The data confirms **three reportable segments** but provides no segment-level revenue or profit. From the consolidated numbers, the margin expansion (gross margin to 52.3%, operating margin to 13.7%) alongside 19.6% revenue growth implies a favorable mix shift toward higher-margin revenue — consistent with **AWS and advertising outgrowing the retail base** — plus effective cost controls in fulfillment and SBC. The 31% YoY increase in D&A and 27%-of-revenue capex are consistent with an aggressive **AI/cloud infrastructure build-out** across AWS data centers and custom silicon. Because segment data is unavailable, traders should treat the mix-shift inference as directional, not quantified, and wait for the 10-Q segment footnote or the Q3 call for confirmation.

---

## 8. Insider Transactions

**DATA UNAVAILABLE.** The vendor's point-in-time archive contains **no authorized insider-transaction data for AMZN as of 2026-10-06**. No insider buying or selling should be inferred, assumed, or fabricated. This is a genuine information gap in this report, not a signal of zero activity.

---

## 9. Risks

1. **Earnings-quality / mark-to-model risk (highest).** $122.3B of non-marketable equity securities, ~11% of assets. A downward revaluation would hit non-operating income and EPS with no cash impact but significant sentiment impact. The $50.5B Q2 mark alone equals ~80% of reported Q2 net income.
2. **Negative free cash flow and rising leverage.** TTM FCF −$11.6B; LT debt +93% in six months; capex +61% YoY. If capex stays at this run-rate and OCF growth decelerates, further debt issuance or a slower buyback/dividend posture is likely.
3. **Depreciation and interest cliff.** D&A +31% YoY and interest expense +155% YoY. Both lag capex/debt issuance, so margin pressure likely intensifies into 2027 even if revenue holds.
4. **Cash-tax normalization.** Cash taxes are running at a fraction of book tax expense; any change would directly reduce OCF.
5. **Thin liquidity ratios.** Current ratio 1.03x, quick ratio 0.88x. AMZN depends on capital-market access.
6. **Data/analytics risk.** No segment detail, no FY2025 annual statements, no price data, no insider data in this feed. Conclusions on mix and valuation are therefore incomplete.
7. **Concentration/valuation sensitivity** from the large private-equity stake: a single asset's valuation now drives a material share of reported earnings and book value.

---

## 10. Actionable Insights for Traders

1. **Do not trade off headline EPS.** Use **~$2.16 adjusted Q2 EPS** and **~$4.12 adjusted H1 EPS** for multiples and trend analysis. Reported $5.75 / $8.53 overstate sustainable earnings by roughly 2.5x. If consensus or screens are built on GAAP EPS, AMZN will look artificially cheap.
2. **The operating story is a genuine beat.** Revenue +19.6%, operating income +43%, operating margin +226 bps, SBC down 7.6%, marketing intensity down ~100 bps. Underlying EPS growth of ~26–29% is strong for a company of this size. This supports a constructive medium-term stance.
3. **Watch free cash flow as the swing factor.** The bull case requires capex to plateau or AWS/AI revenue to inflect before D&A and interest compress margins. The bear case is a multi-year negative-FCF, debt-funded capex cycle. Key checkpoints: Q3 2026 capex/revenue (currently 27%), TTM FCF (currently −$11.6B), and LT debt (currently $133.0B).
4. **Leverage is not yet a crisis.** Net cash ex-leases (~$43B), debt/EBITDA ~0.7–1.3x, interest coverage ~21x. This is a "watch" item, not a "sell" trigger. But the trajectory (debt +93% in six months) warrants monitoring each quarter.
5. **Position for event risk into Q3 2026 earnings (late October).** No SEC financials after 2026-07-31 are in the dataset, so the Q3 print is the next real information event. The set-up: easy adjusted-EPS comparison vs a year-ago quarter with no equity marks, but a harder GAAP comparison vs Q3 2025 only if new marks occur. Volatility around the equity-stake marks is likely to be high and directionally unpredictable.
6. **Treat the $122.3B private-equity stake as a separate, optionality-like asset.** It adds real economic value but should be valued with a discount for illiquidity and mark uncertainty; it also makes GAAP earnings lumpy. Stress-testing a 20–30% markdown implies a ~$25–37B pre-tax hit — material to a single quarter's EPS.
7. **No insider signal available.** Do not read the absence of insider data as either bullish or bearish.

---

## 11. Key-Points Summary Table

| Category | Key Finding | Evidence | Trading Implication |
|---|---|---|---|
| **Reported Q2 2026** | Revenue $200.6B (+19.6% YoY); operating income $27.5B (+43.2%); operating margin 13.69% (+226 bps) | Derived from `OperatingIncomeLoss` + `CostsAndExpenses`; 10-Q filed 2026-07-31 | Strong core operating momentum; supports constructive view |
| **Earnings quality** | $50.5B Q2 / $62.8B H1 non-cash equity revaluation inside non-operating income | `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment` | Reported EPS $5.75 is ~2.5x adjusted; use ~$2.16 (Q2) / ~$4.12 (H1) |
| **Adjusted growth** | Underlying EPS growth ~+28.6% Q2, ~+26.0% H1 | Ex-mark pre-tax income, 22.5% tax | Healthy, but far below the +161–242% headline |
| **Cost discipline** | SBC −7.6% YoY (3.01% of revenue vs 3.90%); marketing 5.83% vs 6.81%; G&A −6.0% | `AllocatedShareBasedCompensationExpense`, `MarketingExpense`, `GeneralAndAdministrativeExpense` | Margin expansion is partly structural, not just mix |
| **Capex supercycle** | TTM capex $173.0B (+60.7%); Q2 $54.2B = 27.0% of revenue; H1 $98.4B | `PaymentsToAcquireProductiveAssets` | Key swing factor for FCF and future D&A |
| **Free cash flow** | TTM FCF **−$11.6B** vs +$13.5B prior TTM; H1 2026 −$27.0B | OCF $161.4B − capex $173.0B | Negative FCF is the central bear argument |
| **Operating cash flow** | TTM $161.4B (+33.2%); Q2 $45.4B (+39.6%); OCF margin 22.6% | `NetCashProvidedByUsedInOperatingActivities` | Cash generation is genuinely robust |
| **Debt** | LT debt $133.0B (+93.2% in 6 months); $82.4B raised in H1; interest expense +154.7% YoY | `LongTermDebt`, `ProceedsFromIssuanceOfLongTermDebt` | Leverage rising but still moderate; coverage ~21x |
| **Liquidity** | Cash + AFS $176.1B; current ratio 1.03x; quick ratio 0.88x; net cash ex-leases ~$43.1B | Balance sheet at 2026-06-30 | Adequate, dependent on capital markets |
| **Asset quality risk** | Non-marketable equity securities $122.3B (11.2% of assets), up from $16.2B; AOCI $66.3B (+$38.1B) | `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` | Mark-to-model volatility risk to EPS and book value |
| **Working capital** | AR +30.1% vs revenue +18.2%; inventory flat at $38.2B; AP +20.9% | Balance sheet | Inventory efficient; monitor receivables |
| **Obligations** | Total contractual obligations $650.0B; $78.1B due within 12 months | `ContractualObligation` | Manageable vs OCF but limits flexibility |
| **Acquisitions** | TTM $42.0B; H1 2026 $39.8B ($24.4B in Q2) | `PaymentsToAcquireBusinessesNetOfCashAcquired` | Debt-funded inorganic growth; integration risk |
| **Segments** | 3 reportable segments confirmed; no segment P&L in feed | `NumberOfOperatingSegments = 3` | Mix-shift inference only; verify in 10-Q/earnings call |
| **Insider activity** | **No data available** for AMZN as of 2026-10-06 | Vendor archive unavailable | Do not infer; genuine information gap |
| **Next catalyst** | Q3 2026 earnings expected late October 2026; latest filing 2026-07-31 | Dataset contains no filings after 2026-07-31 | Event risk; monitor capex, FCF, marks, and guidance |

**Overall fundamental stance:** **Constructive on the operating franchise, cautious on reported earnings quality and cash flow.** AMZN is growing revenue ~19% with expanding margins and improving cost discipline, but is simultaneously running negative FCF, nearly doubling debt, and booking a large share of net income from non-cash, mark-to-model equity gains. Traders should anchor on adjusted earnings (~$2.16 Q2 / ~$4.12 H1), watch capex intensity and TTM FCF as the decisive variables, and treat the $122.3B private-equity stake and the Q3 2026 print as the main sources of asymmetric risk.