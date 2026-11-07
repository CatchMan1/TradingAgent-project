# GOOGL (Alphabet Inc.) — Fundamental Research Report
**Analysis date:** 2026-08-03 | **Latest filing in scope:** Form 10-Q for period ended **2026-06-30**, accepted 2026-07-23 (accn 0001652044-26-000071); FY2025 Form 10-K accepted 2026-02-05 (accn 0001652044-26-000018).

---

## 0. Data provenance, scope, and limitations (read first)

- All figures below are **point-in-time SEC XBRL facts** filtered by actual EDGAR acceptance timestamp ≤ 2026-08-03, so nothing is post-dated/restated.
- **Important caveat:** the returned fact set was truncated alphabetically (line items roughly A→"FiniteLivedIntangibleAssets"). Consequently **revenue, R&D, sales & marketing, PP&E, total liabilities/equity, and several cash-flow lines were not directly available.** Where I state revenue, it is **derived arithmetically and internally audited** as revenue = *CostsAndExpenses + OperatingIncomeLoss* (this reconciles exactly to real reported Alphabet figures for H1 2025: $65,157M + $31,271M = $96,428M for Q2'25 and $124,785M + $61,877M = $186,662M for H1'25 — a strong validation of the method).
- **Insider transactions: DATA UNAVAILABLE.** The vendor has no authorized, point-in-time insider-transaction archive for GOOGL as of 2026-08-03. I will not infer or fabricate insider activity; treat this as an information gap, not as evidence of no activity.

---

## 1. Company profile (context, not tool-derived)

Alphabet Inc. (GOOGL) is the parent of Google. Reporting structure: **Google Services** (Search & other, YouTube ads, Network, subscriptions/platforms/devices — the profit engine and cash cow), **Google Cloud** (infrastructure + Workspace/enterprise AI), and **Other Bets** (long-horizon ventures). Alphabet carries an unusually large **non-operating investment portfolio** (public and private equity stakes), which — as shown below — has become a *first-order* driver of reported GAAP earnings and of the balance sheet. Alphabet pays a dividend (initiated 2024) and has historically been a large repurchaser of stock.

The 10-Q in scope shows a company in the middle of an **unprecedented AI infrastructure build-out financed by an unprecedented capital raise.** That is the single most important fundamental story in this report.

---

## 2. Income statement — Q2 2026 and H1 2026

### 2.1 Core P&L (USD millions)

| Metric | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---|---|---|---|---|---|
| Revenue (derived) | **119,796** | 96,428 | **+24.2%** | **229,692** | 186,662 | **+23.1%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| Gross profit | 73,853 | 57,389 | +28.7% | 142,478 | 111,262 | +28.1% |
| **Gross margin** | **61.7%** | 59.5% | +220 bp | **62.0%** | 59.6% | +240 bp |
| R&D + S&M (residual) | 26,622 | 26,138 | +1.9% | 51,260 | 50,767 | +1.0% |
| G&A | 6,461 | 5,209 | +24.0% | 10,752 | 8,748 | +22.9% |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 149,226 | 124,785 | +19.6% |
| **Operating income** | **40,770** | 31,271 | **+30.4%** | **80,466** | 61,877 | **+30.0%** |
| **Operating margin** | **34.0%** | 32.4% | +160 bp | **35.0%** | 33.1% | +190 bp |
| Non-operating income/(expense) | **97,983** | 2,662 | n.m. | **135,699** | 13,845 | n.m. |
| Pre-tax income | 138,753 | 33,933 | +309% | 216,165 | 75,722 | +185% |
| Income tax | 26,560 | 5,737 | | 41,394 | 12,986 | |
| **Effective tax rate** | **19.1%** | 16.9% | +220 bp | **19.1%** | 17.1% | +200 bp |
| **Net income** | **112,193** | 28,196 | +298% | **174,771** | 62,736 | +179% |
| Diluted EPS | **$9.11** | $2.31 | +294% | **$14.24** | $5.12 | +178% |
| Basic EPS | $9.23 | $2.33 | | $14.41 | $5.16 | |
| SBC (allocated) | 8,000 | 6,000 | +33% | 15,200 | 11,500 | +32% |
| Depreciation | n/a (H1 only) | | | 13,586 | 9,485 | +43.2% |
| Interest income | 1,430 | 1,050 | +36% | 2,811 | 2,051 | +37% |
| Interest expense | 1,278 | 261 | +390% | 1,811 | 295 | **+514%** |

Derived quarterly bridge (H1 less Q2) for precision on Q1 2026: revenue **$109,896M** (+21.8% vs Q1'25 $90,234M), operating income **$39,696M** (36.1% margin), net income **$62,578M**, diluted EPS **$5.13**.

### 2.2 The two stories inside this P&L

**(A) The operating business is accelerating — genuinely.**
Revenue growth stepped up from +21.8% in Q1 to **+24.2% in Q2**, and operating margin expanded **+160 bp YoY to 34.0%** *despite* depreciation +43%, SBC +33%, and G&A +24%. Gross margin +220 bp to 61.7% is the tell: revenue is scaling faster than the cost of delivering it. This is not a "growth at any cost" quarter — it is **accelerating revenue with expanding margins**, which is the single most bullish fundamental combination available.
*Actionable:* 2026's organic operating momentum is stronger than 2025's. Any narrative of "AI capex destroying the P&L" is contradicted on the operating line so far.

**(B) ~71% of Q2 net income was NOT operating income.**

| Q2 2026 pre-tax composition | $M | % of pre-tax |
|---|---|---|
| Operating income | 40,770 | 29.4% |
| Non-operating (equity securities gains, net interest) | 97,983 | 70.6% |

The non-operating line is dominated by **equity securities fair-value gains**:
- `EquitySecuritiesFvNiGainLoss`: **$99,031M in Q2'26** (vs $1,286M in Q2'25); **$135,946M in H1'26** (vs $11,044M).
- Of the H1 total, only $836M was realized (`EquitySecuritiesFvNiRealizedGainLoss`); **~$21.5B was unrealized on marketable equity holdings**, and the remainder relates to the large **non-readily-determinable (private) equity portfolio**, whose cumulative upward valuation adjustments exploded from **$44,485M (12/31/25) to $85,732M (6/30/26)**.
- `DebtAndEquitySecuritiesGainLoss` H1'26: **$135,803M** vs $11,411M.

**Core (ex-investment-gain) earnings power, Q2 2026:** strip the ~$98.0B non-operating line, add back net interest (~+$0.15B) → pre-tax core ≈ **$40.9B**; at 19.1% tax → net ≈ **$33.1B** → **core diluted EPS ≈ $2.65–2.70** vs $2.31 reported a year ago (**~+15–17%**). *That is still excellent* — but it is **3.4x lower than the $9.11 headline.**

**This is the most important trading insight in this report:** GOOGL's reported EPS, ROE, and P/E on this quarter are **structurally distorted by mark-to-market on an investment portfolio**, and the distortion is *large enough to break naive screening*. A trader looking at trailing P/E printed off $14.24 of H1 EPS would conclude the stock is dramatically cheaper than it is.

---

## 3. Balance sheet — a 55% expansion in six months

| Balance sheet item (USD M) | 2026-06-30 | 2025-12-31 | Δ | Δ% |
|---|---|---|---|---|
| Cash & equivalents | 55,911 | 30,708 | +25,203 | +82.1% |
| **Cash + short-term investments** | **242,474** | 126,843 | **+115,631** | **+91.2%** |
| Accounts receivable, net | 69,175 | 62,886 | +6,289 | +10.0% |
| **Total current assets** | **343,524** | 206,038 | **+137,486** | **+66.7%** |
| Available-for-sale debt securities | 99,500 | n/a | | |
| Equity securities w/o readily determinable FV | **124,259** | 64,094 | **+60,165** | **+93.9%** |
| — cumulative *upward* adjustments | 85,732 | 44,485 | +41,247 | +92.7% |
| — cumulative *downward* adjustments | (9,115) | (8,820) | -295 | -3.3% |
| Finite-lived intangibles, gross | 10,585 | 2,467 | +8,118 | +329% |
| Finance lease ROU asset | 5,474 | 4,797 | +677 | +14.1% |
| **Total assets** | **921,983** | 595,281 | **+326,702** | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +8,058 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +17,457 | +31.4% |
| Accrued income taxes (current) | 5,233 | 523 | +4,710 | +900% |
| Accrued income taxes (noncurrent) | 11,306 | 9,531 | +1,775 | +18.6% |
| Loss contingency accrual (current) | **17,356** | 15,594 | +1,762 | +11.3% |
| **Debt, face value** | **102,006** | 49,627 | **+52,379** | **+105.5%** |
| — carrying amount | 101,085 | 49,085 | +52,000 | +105.9% |
| Finance lease liabilities | 2,590 | 2,500 | +90 | +3.6% |
| Operating lease liabilities | 18,037 | 15,954 | +2,083 | +13.1% |
| **Deferred income tax liabilities, net** | **22,819** | 919 | **+21,900** | **+2,383%** |
| Deferred income tax assets, net | 1,448 | 9,113 | -7,665 | -84.1% |
| Common stock + APIC | 131,371 | 93,126 | +38,245 | +41.1% |
| AOCI | (2,285) | (1,916) | -369 | |
| **Convertible preferred stock** | **18,023** | 0 | +18,023 | new |
| Shares outstanding | **12,230M** | 12,088M | +142M | +1.2% |
| Shares authorized | 300,000M | 300,000M | — | par $0.001 |

### 3.1 Liquidity and leverage — still fortress, but levering fast

- **Liquidity:** $242.5B cash + short-term investments, plus $99.5B AFS debt securities. Against **$102.0B face debt** + $20.6B leases. On a cash + ST-investments basis, **net cash ≈ +$140B** (vs ≈ +$78B at 12/31/25 — net cash *rose* despite the debt doubling, because liquidity rose faster).
- **But the trajectory matters:** gross debt **doubled in six months** (+$52.4B, with $56.2B of gross issuance in H1 and only $5.3B of repayments). Interest expense ran at a **$3.6B annualized run-rate in H1'26 vs ~$0.6B a year earlier (+514% YoY)** — that is a real, growing below-the-line drag that will keep compressing net income as more paper is sold.
- **Deferred tax liabilities of $22.8B** are the accounting shadow of the private-equity marks. As those gains are realized/taxed, DTLs reverse and cash taxes normalize upward. Note H1'26 deferred tax *expense* was **+$27,538M** vs **−$1,596M** in H1'25 — i.e., the enormous GAAP earnings carry a large non-cash tax charge, while cash taxes stayed low (accrued current income taxes jumped only $4.7B). **Cash-tax normalization is a forward EPS risk.**

### 3.2 The capital raise is the real news — read it as a signal

H1 2026 financing inflows (`NetCashProvidedByUsedInFinancingActivities` = **+$86,320M**, vs **−$26,033M** in H1'25):

| Financing source (USD M) | H1 2026 | H1 2025 |
|---|---|---|
| Debt issued, net of costs | **56,226** | 31,378 |
| **Common stock issued** | **30,499** | 0 |
| **Convertible preferred issued (6/5/26)** | **19,063** | 0 |
| Minority/other equity contributions | 3,758 | 400 |
| Debt repayments | (5,253) | (18,397) |
| **Share repurchases** | **0** | (28,306) |
| Dividends paid | (5,231) | (4,977) |
| Other | (686) | (400) |

**Interpretation — three hard, non-speculative conclusions:**
1. **Alphabet sold $30.5B of common equity and $19.1B of convertible preferred in H1 2026 — the first common equity issuance in the modern Alphabet era.** Share count rose 142M (+1.2%). For a company that was retiring ~1.5–2% of shares annually, this is a **directional reversal in capital allocation and a dilution regime change.** A mega-cap that raises equity at these levels is telling you management's internal model requires capital beyond internal cash flow.
2. **Buybacks went to exactly zero** ($0 vs $28.3B). The historical EPS tailwind from buybacks is gone; go-forward EPS growth must come from operations (or marks). Diluted-vs-basic spread narrowed accordingly (Q2'26 spread $0.12 vs $0.02 a year ago, reflecting new preferred/dilutive instruments).
3. **Dividend continued and was raised:** $0.22/share declared per quarter in Q2'26 vs $0.21 in Q2'25 (H1 declared $0.43 total). Preferred dividends began ($86M in Q2). Total payout is modest versus earnings, but *versus free cash flow* it is now material — see below.

### 3.3 Legal / contingency watch
Loss contingency accrual (current) rose to **$17,356M**. In the FY2025 10-K, `LossContingencyAccrualPayments` of **$3,000M** was recorded in Q3 2025 — a large adverse settlement/fine (consistent with the EU ad-tech penalty). With ~$17.4B accrued, **further adverse regulatory outcomes in the US/EU remain a live, sized risk** but are provisioned rather than open-ended.

---

## 4. Cash flow — the crux of the bear case

| Cash flow (USD M) | H1 2026 | H1 2025 | Change |
|---|---|---|---|
| **Operating cash flow** | **84,859** | 63,897 | **+32.8%** |
| Capital expenditures (cash, PP&E) | **(80,598)** | (39,643) | **+103.3%** |
| **Free cash flow (OCF − capex)** | **4,261** | **24,254** | **−82.4%** |
| Purchases of marketable securities | (76,480) | (39,870) | |
| Sales/maturities of marketable securities | 66,696 | 40,930 | |
| Purchases of other (non-marketable) investments | **(22,051)** | (2,312) | +853% |
| Proceeds from other investments | 1,667 | 873 | |
| **Net investing cash flow** | **(145,822)** | (40,738) | **−258%** |
| **Net financing cash flow** | **+86,320** | (26,033) | n/m |
| FX effect on cash | (154) | 444 | |
| **Net change in cash** | **+25,203** | (2,430) | |
| Capex **incurred but not yet paid** (period-end) | **29,113** | 10,635 | +173.7% |

### 4.1 Four cash-flow conclusions

1. **Operating cash flow growth (+32.8%) actually outpaced revenue growth (+23.1%)** — excellent working-capital and cash-conversion discipline. Revenue growth is genuinely cash-generative.
2. **Free cash flow has been almost entirely consumed by capex: $4.3B in six months vs $24.3B a year ago (−82%).** Capex/revenue = **35.1%** (vs 21.2% H1'25). On an *accrued* basis — adding the $18.5B increase in capex-incurred-but-unpaid — H1'26 capex commitments are closer to **~$99B**, i.e., a **~$200B annualized run-rate**. This is the number that matters for anyone modeling buybacks, dividend growth, or deleveraging.
3. **The gap was funded with securities, debt, and equity — not from operations.** Net investing outflow of $145.8B was covered by $86.3B of financing plus the $84.9B OCF. Note also **$22.1B into non-marketable ("other") investments in H1'26**, up 9.5x YoY — Alphabet is simultaneously building datacenters *and* buying private AI/strategic stakes aggressively.
4. **The equity securities are now a self-referential part of the cash story:** $115.6B of the balance-sheet liquidity build is marketable securities purchased with raised capital, while $53.2B of the AFS portfolio sits in an unrealized-loss position (accumulated loss $416M — tiny, so duration/credit risk is low). Liquidity is real, not an artifact.

---

## 5. Financial history — what the multi-year record shows

Available annual anchors (from the FY2025 10-K acceptance set):
- **Financing cash flow:** FY2023 **−$72,093M** → FY2024 **−$79,733M** → FY2025 **−$37,388M** → **H1 2026 +$86,320M**. A clean four-point inflection: from ~$80B/yr of net capital *return* to a $86B *raise* in six months.
- **Capex incurred but not paid:** FY2023 $7,435M → FY2024 $10,326M → FY2025 $15,090M → **H1 2026 $29,113M.** The acceleration in the *accrual* is steeper than in the cash number — a leading indicator that reported capex keeps rising into 2H26.
- **Finance lease principal payments:** FY2023 $705M → FY2024 $405M → FY2025 $1,988M → H1 2026 $840M — moving from negligible to meaningful as datacenter leasing scales.
- **Debt maturity wall (as of 12/31/25, before the 2026 issuance):** $2.0B due <12m, $1.0B yr2, $2.68B yr3, $1.76B yr4, $5.5B yr5, $36.1B after yr5 — a well-laddered, long-dated profile. The 2026 issuance (+$52B) extends duration rather than creating a near-term refunding cliff. **Refinancing risk is low; interest-cost creep is the real cost.**
- **Lease obligations:** operating lease payments due $21,333M (of which $3,498M in the next 12 months); finance leases $2,920M. Modest relative to a $922B balance sheet.

---

## 6. Synthesis: quality of earnings, quality of balance sheet, quality of franchise

**Franchise quality: improving.** +24% revenue growth with +220 bp gross-margin and +160 bp operating-margin expansion, in a company already at a ~$450B+ annualized revenue run-rate, is extraordinary. Cost of revenue growth (+17.7%) lagging revenue (+24.2%) shows AI infrastructure is being monetized at better incremental economics than feared. Residual R&D+S&M growth of just ~1% YoY means **operating leverage is coming from expense discipline as much as from scale.**

**Earnings quality: poor on a headline basis, good on a core basis.** GAAP net income is now levered to private-company valuations. Two-thirds to three-quarters of net income is non-operating marks. The marks are *real* in an accounting sense and are supported by a genuine private-AI asset revaluation cycle, but they are **non-cash, non-recurring, unforecastable, and reversible.** They also created a $22.8B deferred tax liability and a permanent step-up in the tax rate (19.1% vs 16.9%).

**Balance sheet quality: still strong, now levered to a thesis.** $242B liquidity and a ~$140B net-cash position are genuine. But the direction of travel — debt +105%, preferred new, common equity issued, buybacks at zero — means the balance sheet is no longer a passive asset; **it is now an input to the AI capex bet.** If capex continues at a ~$200B annualized pace with $4B of semiannual FCF, the company will return to markets again. That is a structural change in the GOOGL equity story.

---

## 7. Actionable insights for traders

1. **Do not use GAAP EPS or trailing P/E off this quarter.** Headline Q2'26 EPS of $9.11 contains ~$6.40–6.45 of after-tax investment marks. **Core EPS ≈ $2.65–2.70 (+15–17% YoY)**. Build your multiple off core. If consensus/algo flows chase the $9.11 print, expect a valuation-driven re-rating that is *not* fundamentally supported, and vice versa on any mark-to-market reversal in Q3.
2. **Trade the two engines separately.** Operating momentum (revenue +24%, margins up) is a **long-duration positive**. Investment marks are a **noise/volatility term with negative skew** (they can reverse; note the $9.1B cumulative *downward* adjustments on the private book and $53.2B of AFS securities in unrealized-loss positions). Expect **elevated earnings-day volatility and high dispersion in Q3 estimates** purely from the marks line.
3. **The single most important number to monitor is capex, not EPS.** H1 capex $80.6B cash / ~$99B accrued against $4.3B of free cash flow. Watch: (a) the Q3 capex guide, (b) capex-incurred-but-unpaid (now $29.1B — a leading indicator), (c) depreciation/revenue (currently only 5.9% — it *will* rise hard and become a 2027 margin headwind even if revenue holds).
4. **Capital-return regime has changed — reprice it.** Buybacks $0 vs $28.3B; shares +142M (+1.2%); $30.5B common + $19.1B convertible preferred issued. **The historical ~1.5–2%/yr EPS tailwind from shrinkage is gone and has become a small headwind.** Anyone with a "buyback-supported EPS growth" model for GOOGL must cut it.
5. **Leverage is a new, monitorable variable.** Gross debt $102B, interest expense +514% YoY. Still comfortably covered (net cash ~$140B, interest coverage >20x on operating income), but if the company raises again in 2H26, treat it as confirmation the capex curve is above internal cash generation — historically a de-rating catalyst for mega-cap tech.
6. **Cash-tax normalization is an underappreciated EPS drag.** Deferred taxes were +$27.5B of expense in H1'26 while accrued current taxes rose only ~$4.7B. As private marks realize, cash taxes rise toward the 19.1%+ effective rate and the gap closes — a mechanical headwind to future FCF conversion.
7. **Watch the $17.4B legal accrual.** A $3.0B payment was made in Q3'25. Further adverse regulatory outcomes are a live but *provisioned* risk; a fresh >$2B charge would be the kind of one-off that hits the operating line.
8. **Insider signals: unavailable.** The insider-transactions dataset has no authorized point-in-time archive for GOOGL as of 2026-08-03. Do not read silence as either bullish or bearish — it is a data gap. Cross-check via Form 4s separately before acting on any insider thesis (particularly relevant given the equity issuance and 1.2% share-count increase).

---

## 8. Key points summary table

| Category | Metric | Latest (2026-06-30 / H1'26) | Prior comparable | Read-through |
|---|---|---|---|---|
| **Revenue (derived)** | Q2'26 / H1'26 | $119,796M / $229,692M | $96,428M / $186,662M | **+24.2% / +23.1% YoY — acceleration** |
| **Gross margin** | Q2'26 | 61.7% | 59.5% | +220 bp — AI monetization > cost |
| **Operating income** | Q2'26 / H1'26 | $40,770M / $80,466M | $31,271M / $61,877M | **+30.4% / +30.0% YoY** |
| **Operating margin** | Q2'26 / H1'26 | 34.0% / 35.0% | 32.4% / 33.1% | **+160/+190 bp — leverage** |
| **GAAP diluted EPS** | Q2'26 / H1'26 | $9.11 / $14.24 | $2.31 / $5.12 | Distorted by investment marks |
| **Core diluted EPS (ex-marks)** | Q2'26 est. | **~$2.65–2.70** | $2.31 | +15–17% — the honest growth rate |
| **Non-operating income** | Q2'26 / H1'26 | $97,983M / $135,699M | $2,662M / $13,845M | **71% of Q2 pre-tax income — low quality** |
| **Equity securities FV gains** | H1'26 | $135,946M (only $836M realized) | $11,044M | Non-cash, reversible |
| **Private equity book** | 6/30/26 | $124,259M (+$60.2B in 6m) | $64,094M | Mark-to-model concentration |
| **Effective tax rate** | H1'26 | 19.1% | 17.1% | +200 bp — structural |
| **Deferred tax liability** | 6/30/26 | $22,819M | $919M | Tax shadow of the marks |
| **Cash + ST investments** | 6/30/26 | $242,474M | $126,843M | +91% — fortress liquidity |
| **Gross debt (face)** | 6/30/26 | $102,006M | $49,627M | **+105% in 6 months** |
| **Net cash position** | 6/30/26 | **~+$140B** | ~+$78B | Still net cash, but levering |
| **Interest expense** | H1'26 | $1,811M (+514% YoY) | $295M | Cost of the raise |
| **Operating cash flow** | H1'26 | $84,859M | $63,897M | +32.8% — beats revenue growth |
| **Capital expenditures (cash)** | H1'26 | $80,598M | $39,643M | **+103%; 35% of revenue** |
| **Capex incurred, unpaid** | 6/30/26 | $29,113M | $10,635M | Leading indicator: capex still rising |
| **Free cash flow** | H1'26 | **$4,261M** | $24,254M | **−82% — the core bear point** |
| **Share repurchases** | H1'26 | **$0** | $28,306M | **Buyback regime ended** |
| **Common stock issued** | H1'26 | **$30,499M** | $0 | Shares +142M (+1.2%) dilution |
| **Convertible preferred issued** | 6/5/26 | **$19,063M** | $0 | New capital structure layer |
| **Dividend/share declared** | Q2'26 | $0.22 | $0.21 | Raised; H1 total $0.43 |
| **Loss contingency accrual** | 6/30/26 | $17,356M | $15,594M | Provisioned regulatory risk |
| **Shares outstanding** | 6/30/26 | 12,230M | 12,088M | First material increase in years |
| **Insider transactions** | — | **DATA UNAVAILABLE** | — | Do not infer; verify via Form 4s |

---

### Bottom line
GOOGL's **operating fundamentals are the strongest they have been in years** — 24% revenue growth *with* 160 bp of operating-margin expansion is a rare and genuinely bullish combination, and operating cash flow is compounding faster than revenue. But the **reported** results are dominated by ~$136B of mostly unrealized investment marks, and the **cash-flow and capital-structure profile has changed character**: free cash flow is down 82%, buybacks are at zero, debt has doubled, and the company issued both common and convertible preferred equity for the first time. Traders should be **constructive on the operating franchise, skeptical of headline EPS, and vigilant on capex and the next financing decision** — those, not the $9.11 print, will determine the next 12 months of GOOGL's return.