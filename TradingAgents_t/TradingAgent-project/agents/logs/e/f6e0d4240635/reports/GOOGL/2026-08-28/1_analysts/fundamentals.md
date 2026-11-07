# GOOGL — Alphabet Inc.: Fundamental Deep-Dive
**As of:** 2026-08-28 | **Latest reported period:** Q2 2026 (10-Q filed 2026-07-23) | **Prior anchor:** FY2025 10-K (filed 2026-02-05)

---

## 1. Executive Summary — What Changed in Six Months

Alphabet has undergone the most radical financial transformation in its history as a public company, and it happened in exactly one half-year:

1. **The balance sheet roughly doubled.** Total assets went from **$595.3B (12/31/25) to $922.0B (6/30/26)**, +54.9% in six months.
2. **The company flipped from a capital-return machine to a capital-RAISING machine.** FY2024/FY2025 financing cash flow was **–$79.7B / –$37.4B**. H1 2026 financing cash flow was **+$86.3B**. Alphabet raised **~$109.6B** of gross capital in six months: $56.2B debt, **$30.5B common stock, $19.1B convertible preferred**, $3.8B minority interests — while **reducing buybacks to exactly $0** (vs. $45.7B in FY2025 and $62.2B in FY2024).
3. **Free cash flow collapsed.** H1 2026 FCF = **$4.3B** (1.9% of revenue) vs. $24.3B (13.0%) in H1 2025. **Q2 2026 FCF was NEGATIVE: –$5.9B** ($39.1B CFO vs. $44.9B capex). Capex ran at **36% of Q2 revenue**.
4. **Headline earnings are now dominated by non-operating investment gains, not the business.** H1 2026 net income of **$174.8B** includes **~$135.7B of non-operating income** (equity-securities gains). H1 2026 diluted EPS of **$14.24** contains only **~$5.36 of "core" (ex-investment-gain) EPS**. Reported EPS growth of +178% YoY overstates underlying growth of ~+25%.
5. **Dilution has returned.** Shares outstanding rose from 12.088B to 12.230B (+1.2%) in six months — the first material share-count increase in years — driven by the equity raise plus a 32% YoY jump in stock-based compensation ($15.2B in H1).

**Bottom line for traders:** the operating business is accelerating (Q2 revenue +24.2% YoY, operating income +30.4% YoY, gross margin +210bp YoY) but is now consuming essentially all of its own cash generation, funded by the largest equity/debt raise in company history. The equity story has shifted from "per-share compounding via buybacks" to "AI infrastructure buildout with dilution and negative FCF," with reported EPS polluted by volatile mark-to-market gains. **Value GOOGL on ex-investment-gain earnings and on capex/FCF trajectory, not on the $9.11 of Q2 EPS.**

---

## 2. Company Profile

Alphabet Inc. (NASDAQ: GOOGL) is the parent of Google. Its three reporting structures are **Google Services** (Search & other, YouTube ads, Google Network, subscriptions/platforms/devices — Android, Chrome, Play, Maps, hardware), **Google Cloud** (Google Cloud Platform infrastructure, Workspace and other enterprise collaboration/security products), and **Other Bets** (early-stage businesses such as autonomous driving, life sciences and venture-style investments). A large and growing portion of Alphabet's reported earnings now comes not from these segments but from its **equity investment portfolio** (marketable and non-marketable, including AI/frontier-tech and venture stakes), which sat at **$124.3B** on the balance sheet for non-marketable equity securities alone at 6/30/2026 (up from $64.1B at 12/31/25).

*Data note: this vendor feed does not expose segment-level revenue, so segment mix cannot be verified from these tools. Revenue by segment/geography is not reported in this dataset.*

---

## 3. Income Statement: Q2 2026 and H1 2026

**Important methodology note:** the vendor feed truncated the literal `Revenues`, `ResearchAndDevelopmentExpense` and `SellingAndMarketingExpense` tags. Revenue is therefore **derived** using the accounting identity that holds exactly for FY2023 and FY2024 in this dataset (CostsAndExpenses + OperatingIncomeLoss = Revenue; verified: FY2024: 237,628 + 112,390 = 350,018 ✓; FY2023: 223,101 + 84,293 = 307,394 ✓). "R&D + S&M" is the residual of total costs and expenses less cost of revenue and G&A. All derived figures are labeled *(d)*.

### 3.1 Quarterly progression ($M)

| $M | Q1'25 | Q2'25 | Q1'26 | Q2'26 | Q2 YoY | Q2 QoQ |
|---|---|---|---|---|---|---|
| Revenue *(d)* | 90,234 | 96,428 | 109,896 | **119,796** | **+24.2%** | **+9.0%** |
| Cost of revenue | 36,361 | 39,039 | 41,271 | 45,943 | +17.7% | +11.3% |
| Gross profit *(d)* | 53,873 | 57,389 | 68,625 | **73,853** | +28.7% | +7.6% |
| **Gross margin** | 59.7% | 59.5% | 62.4% | **61.6%** | **+210bp** | –80bp |
| G&A | 3,539 | 5,209 | 4,291 | 6,461 | +24.0% | **+50.6%** |
| R&D + S&M *(d)* | 19,728 | 20,909 | 24,638 | 26,622 | +27.3% | +8.1% |
| **Operating income** | 30,606 | 31,271 | 39,696 | **40,770** | **+30.4%** | **+2.7%** |
| **Operating margin** | 33.9% | 32.4% | **36.1%** | **34.0%** | +160bp | **–210bp** |
| Non-operating income | 11,183 | 2,662 | 37,716 | **97,983** | n.m. | n.m. |
| Pre-tax income | 41,789 | 33,933 | 77,412 | **138,753** | +308.9% | +79.2% |
| Tax | 7,249 | 5,737 | 14,834 | 26,560 | +363% | +79.0% |
| **Effective tax rate** | 17.3% | 16.9% | 19.2% | **19.1%** | **+220bp** | –10bp |
| **Net income** | 34,540 | 28,196 | 62,578 | **112,193** | **+298%** | +79.3% |
| **Diluted EPS** | 2.81 *(d)* | 2.31 | 5.13 *(d)* | **9.11** | **+294%** | +77.6% |
| **Core EPS (ex-inv. gains)** *(d)* | 2.12 | 2.16 | 2.68 | **2.68** | **+24%** | **0%** |

### 3.2 Half-year view ($M)

| $M | H1 2025 | H1 2026 | Δ |
|---|---|---|---|
| Revenue *(d)* | 186,662 | **229,692** | **+23.1%** |
| Cost of revenue | 75,400 | 87,214 | +15.7% |
| Gross margin | 59.6% | **62.0%** | +240bp |
| G&A | 8,748 | 10,752 | +22.9% |
| R&D + S&M *(d)* | 40,637 | 51,260 | +26.1% |
| Opex intensity (G&A + R&D + S&M) | 26.5% | 27.0% | +50bp |
| **Operating income** | 61,877 | **80,466** | **+30.0%** |
| **Operating margin** | 33.1% | **35.0%** | **+190bp** |
| Non-operating income | 13,845 | **135,699** | **9.8×** |
| Pre-tax income | 75,722 | 216,165 | +185% |
| Tax | 12,986 | 41,394 | +219% |
| Effective tax rate | 17.1% | **19.1%** | +200bp |
| **Net income** | 62,736 | **174,771** | **+178.6%** |
| **Diluted EPS** | 5.12 | **14.24** | **+178.1%** |
| Diluted shares *(d)* | ~12,253 | ~12,306 | +0.4% |
| SBC | 11,500 | **15,200** | **+32.2%** |
| SBC % of revenue | 6.2% | 6.6% | +40bp |
| Depreciation | 9,485 | **13,586** | **+43.2%** |
| Amortization | 246 | 545 | +122% |
| Interest income | 2,051 | 2,811 | +37.0% |
| Interest expense | 295 | **1,811** | **+513%** |
| Foreign currency loss | (175) | (14) | — |

### 3.3 Reading the operating business (the good news)

- **Revenue growth is accelerating:** +21.8% YoY in Q1'26 → **+24.2% in Q2'26**. Sequential growth of +9.0% in a single quarter is exceptional for a company this size and implies a revenue run-rate of ~$479B annualized on Q2.
- **Gross margin expanded 210bp YoY** (59.5% → 61.6%), despite the cost of running AI infrastructure and serving AI features. Cost of revenue grew only +17.7% against +24.2% revenue growth — genuine operating leverage at the gross line.
- **Operating income +30.4% YoY**, faster than revenue, and **H1 operating margin expanded +190bp to 35.0%**.
- **Deferred revenue (contract liabilities) rose to $10.1B from $8.6B** (+17.4%), and $4.9B of H1 2026 revenue was recognized from the opening contract liability balance — consistent with a growing Cloud backlog.
- **Receivables discipline improved:** AR +10.0% ($62.9B → $69.2B) against +23.1% H1 revenue growth; allowance for doubtful accounts rose only modestly ($924M → $995M).

### 3.4 Reading the operating business (the warning signs)

- **Sequential margin compression: –210bp from Q1'26 (36.1%) to Q2'26 (34.0%).** Two-thirds of that came from **G&A spiking +50.6% QoQ to $6,461M (5.4% of revenue vs 3.9% in Q1)** — a classic signature of legal/regulatory charges. Watch the 10-Q note on contingent liabilities (accrued legal/contingency reserve rose to $17,356M from $15,594M).
- **Depreciation is ramping ( +43% YoY) but is still trivially small relative to capex** — $13.6B of depreciation vs. $80.6B of capex in H1. **Capex is running at 5.9× depreciation.** The depreciation wave from the AI buildout has barely started.
- **Tax rate has moved up structurally:** 13.9% (FY23) → 16.4% (FY24) → 16.8% (FY25) → **19.1% (H1'26)**. The FDII benefit is shrinking (4.6% of the rate in FY23 → 2.5% in FY25), and the equity gains are being taxed at a higher blended rate. Assume a high-teens to ~20% tax rate going forward, not the mid-teens of 2023–24.

---

## 4. Earnings Quality: The Single Most Important Analytical Issue

**H1 2026's $174.8B of net income contains ~$135.7B of non-operating income — 78% of pre-tax income.** This is not operating profit and it is largely non-cash and reversible.

Composition of the equity-securities gains:

| Component ($M) | H1 2025 | H1 2026 |
|---|---|---|
| Total equity securities gains (`EquitySecuritiesFvNiGainLoss`) | 11,044 | **135,946** |
| — of which marketable FVNI unrealized | 1,088 | 21,531 |
| — of which FVNI realized | 435 | 836 |
| Debt + equity securities gains (`DebtAndEquitySecuritiesGainLoss`) | 11,411 | **135,803** |
| Cumulative UPWARD adjustments on non-marketable stakes (held) | 22,709 → 44,485 (FY24→FY25) | **44,485 → 85,732 (+40,952 in H1)** |
| Cumulative DOWNWARD adjustments | (8,820) | (9,115) |
| Non-marketable equity securities, carrying value | 64,094 (12/31/25) | **124,259 (6/30/26)** |

**Analytical flag:** the reported $135.9B gain is materially larger than the sum of its identifiable parts (marketable FVNI unrealized $21.5B + realized $0.8B + measured increase in upward adjustments on held non-marketable stakes $41.0B ≈ **$63.3B**). The remaining ~**$72.6B** implies a large transaction-related gain — most plausibly a holding that crossed into marketable/observable status (or exited the measurement-alternative bucket) and was remeasured at fair value in Q2, plus disposal gains. **The equity-securities note in the 10-Q should be reviewed to confirm the composition before extrapolating.** (I am not asserting which specific holdings are involved.)

**Consequences for traders:**
- **Q2 2026 diluted EPS of $9.11 vs. core EPS of ~$2.68.** ~70% of reported EPS is investment marks.
- Total mark-to-market exposure is enormous: **$124.3B of non-marketable + ~$99.5B of available-for-sale debt securities + marketable equity holdings** — all against equity that I estimate at roughly $600–625B. **Alphabet's earnings are now highly levered to public and private technology valuations**, both up and down.
- Q2's $21.4B of marketable-securities unrealized gains in a single quarter shows how violently this line can swing. **A reversal quarter could produce a large reported EPS miss with no operating deterioration whatsoever.**
- A **deferred tax liability of $22.8B** (up from $0.9B net at 12/31/25) has been booked against these gains — evidence the taxes are accrued but **not yet cash-paid**.

---

## 5. Balance Sheet: The Transformation ($M)

| | 12/31/2024 | 12/31/2025 | **6/30/2026** | 6-mo Δ |
|---|---|---|---|---|
| Cash & equivalents | 23,466 | 30,708 | **55,911** | +82.1% |
| Cash + short-term investments | 95,657 | 126,843 | **242,474** | **+91.2%** |
| Available-for-sale debt securities | — | 89,822 | **99,500** | +10.8% |
| Accounts receivable, net | 52,340 | 62,886 | **69,175** | +10.0% |
| **Current assets** | 163,711 | 206,038 | **343,524** | **+66.7%** |
| Non-marketable equity securities | 35,218 | 64,094 | **124,259** | **+93.9%** |
| Finite-lived intangibles, gross | — | 2,467 | **10,585** | **+329%** |
| **Total assets** | **450,256** | **595,281** | **922,983** | **+55.0%** |
| Accounts payable | — | 12,200 | **20,258** | +66.0% |
| Accrued liabilities | 51,228 | 55,557 | **73,014** | +31.4% |
| Employee-related liabilities | 15,069 | 17,546 | **15,086** | –14.0% |
| Accrued income taxes — current | 2,905 | 523 | **5,233** | **10.0×** |
| Accrued income taxes — noncurrent | 8,782 | 9,531 | **11,306** | +18.6% |
| Contract liabilities (total) | 6,000 | 8,600 | **10,100** | +17.4% |
| Legal/contingency accrual (current) | — | 15,594 | **17,356** | +11.3% |
| **Total debt (carrying)** | **12,000** | **49,085** | **101,085** | **+106.0%** |
| Finance lease liabilities | 1,677 | 2,500 | **2,590** | +3.6% |
| Operating lease liabilities | — | 15,954 | **18,037** | +13.1% |
| Deferred tax liabilities, net | 16,460 | 919 | **22,819** | **24.8×** |
| Convertible preferred stock | 0 | 0 | **18,023** | **new** |
| Common stock + APIC | — | 93,126 | **131,371** | **+41.1%** |
| AOCI | (4,800) | (1,916) | (2,285) | — |
| Shares outstanding | — | 12,088 | **12,230** | +1.2% |

**Key observations:**

- **The six-month asset increase of $326.7B breaks down roughly as:** cash + ST investments **+$115.6B**; non-marketable equity securities **+$60.2B**; net PP&E **+~$67B** (implied: $80.6B capex less $13.6B depreciation); AFS securities **+$9.7B**; AR **+$6.3B**; intangibles **+$8.1B**.
- **The +329% jump in finite-lived intangibles (plus the deferred tax dynamics) indicates M&A occurred in H1 2026** — Alphabet is acquiring, not just building. Amortization is guided by the disclosed schedule: **$747M (rest of FY26), $1,304M (FY27), $1,142M, $1,096M, $1,055M** — a headwind of roughly $1.3B/yr ramping through 2028.
- **Alphabet bought $22.05B of "other investments" in H1 2026, vs. $2.31B in H1 2025 — a 9.5× increase.** Combined with the equity raises, this is a company aggressively deploying capital into external AI/frontier-tech positions at exactly the moment it is also spending $160B+/yr on its own infrastructure.
- **Accounts payable +66% and "capex incurred but not yet paid" of $29.1B** (vs. $10.6B a year earlier) confirm that a further cash outflow is already committed and will hit H2 cash flow regardless of new decisions.
- **Deferred tax net liability of $22.8B** will unwind asymmetrically: it is a real future cash tax obligation if gains are realized, and it reverses if marks reverse.
- **Estimated equity ~$600–625B (derived), implying ~66–68% equity/assets and debt/total-capital of ~14%** — still a fortress. But note that a meaningful slice of that equity is now unrealized investment marks rather than retained operating earnings.

---

## 6. Cash Flow: The FCF Story Is the Story

| $M | FY2023 | FY2024 | FY2025 | H1 2025 | **H1 2026** |
|---|---|---|---|---|---|
| Cash from operations | 101,746 | 125,299 | 164,713 | 63,897 | **84,859** (+32.8%) |
| Purchases of PP&E (capex) | (32,251) | (52,535) | (91,447) | (39,643) | **(80,598)** (+103.3%) |
| **Free cash flow** | **69,495** | **72,764** | **73,266** | **24,254** | **4,261** |
| FCF margin | 22.6% | 20.8% | ~18.1% *(d)* | 13.0% | **1.9%** |
| Capex / revenue | 10.5% | 15.0% | ~22.5% *(d)* | 21.2% | **35.1%** |
| Depreciation | — | — | — | 9,485 | **13,586** |
| Capex / depreciation | — | — | — | 4.2× | **5.9×** |
| Investing cash flow | (27,063) | (45,536) | (120,291) | (40,738) | **(145,822)** |
| Financing cash flow | (72,093) | (79,733) | (37,388) | (26,033) | **+86,320** |
| SBC | 22,100 | 22,800 | 27,100 | 11,500 | **15,200** |

### 6.1 Quarterly cash flow decomposition ($M)
- **Q1 2026:** CFO 45,790; capex 35,674; **FCF +10,116**.
- **Q2 2026:** CFO 39,069; capex 44,924; **FCF –5,855** ← *first negative FCF quarter in the modern history of the company.*
- CFO actually **declined 14.7% sequentially** in Q2 while capex rose 25.9% QoQ. If capex continues on its Q2 trajectory, FY2026 capex exceeds **$175B** (Q2 annualized = $179.7B).

### 6.2 What this means
- **The AI buildout is now self-funding-negative.** Operating cash flow of $84.9B covered only 105% of capex in H1; that thin coverage was flattered by a low cash tax rate. **Cash taxes are about to rise:** H1 book tax expense was $41.4B but the current-tax component was only ~$13.9B (the balance was a $27.5B deferred charge). Accrued current income taxes jumped to $5.2B from $0.5B — a direct signal of higher cash tax payments in H2.
- **TTM figures (derived):** revenue ~$448.6B; operating income ~$150.4B (33.5% margin); capex ~$132.4B; **TTM FCF ~$53.3B** — down from $73.3B in FY2025 and $72.8B in FY2024, i.e. **FCF is down ~27% year-over-year while revenue is up ~23%.**
- **Divergence to monitor:** the entire bull case now depends on the AI capex generating revenue at a return above its cost of capital, and the only observable evidence so far is revenue acceleration (+24%) with margin expansion at the gross line but compression at the operating line and negative FCF. That's a *plausible* early-stage buildout signature — but it is unproven.

---

## 7. Capital Allocation: A Complete 180°

| $M | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|
| Share repurchases | 61,504 | 62,222 | 45,709 | **0** |
| Dividends paid | 0 | 7,363 | 10,049 | 5,231 |
| Dividend per share (declared) | — | — | ~0.82 | **$0.43 (2 qtrs: 0.21 + 0.22)** |
| Debt issued (net of costs) | 10,790 | 13,589 | 64,564 | **56,226** |
| Debt repaid | (11,550) | (12,701) | (32,427) | (5,253) |
| Common stock issued | 0 | 0 | 0 | **30,499** |
| Convertible preferred issued | 0 | 0 | 0 | **19,063** |
| Minority interest proceeds | 8 | 1,154 | 400 | **3,758** |
| **Net capital returned / (raised)** | **+50,000** | **+56,000** | **+9,000** | **(108,000)** |

**Interpretation:**
- **Buyback suspension is the highest-signal change in the entire dataset.** Management chose to issue $30.5B of *new common equity* at the same time it stopped repurchasing its own stock. You do not issue equity if you believe your stock is deeply undervalued — and you certainly do not do both simultaneously unless capital needs are judged extreme or credit metrics are being defended.
- **Dividend policy continues uninterrupted** ($0.21 → $0.22 quarterly, +4.8%), costing ~$5.2B/half — immaterial against the cash flows but a signal that the board still wants the income narrative intact.
- **Debt is now a real feature of the capital structure.** Total debt went from $12.0B (12/31/24) to $101.1B (6/30/26) — an **8.4× increase in 18 months**. Interest expense grew 513% YoY ($295M → $1,811M in H1). Annualized run-rate interest is ~$4.0B. Carrying amounts net of unamortized discount/issuance costs = $101,085M less $921M.
- **Maturity profile remains comfortable** (from the FY2025 10-K, before Q1/Q2 2026 issuance): $2.0B due within 12 months, $1.0B yr2, $2.7B yr3, $1.8B yr4, $5.5B yr5, **$36.1B beyond year 5**. New issuance likely lengthened this further. **Refinancing risk is low.**
- **The convertible preferred ($19.0B, ~$344M/yr dividend, $86M in Q2)** is the sleeper dilution risk: it converts to common on appreciation, so the future share count is a call option *against* equity holders in exactly the scenario where operating performance is best.
- **Diluted share count rising** (12,253M → 12,306M in H1) means EPS growth will now lag net income growth. From FY2023 to 1H2026, Alphabet went from systematically shrinking the share count to growing it.

---

## 8. Multi-Year Financial History (FY2023–FY2025 + H1 2026)

| $M unless noted | FY2023 | FY2024 | FY2025 | H1 2026 | Note |
|---|---|---|---|---|---|
| Revenue *(d)* | 307,394 | 350,018 | **~405,600** *(d)* | 229,692 | +13.9%, +15.9%, ~+15.9%*(d)*; H1'26 +23.1% |
| Cost of revenue | 133,332 | 146,306 | 162,535 | 87,214 | |
| Gross margin | 56.6% | 58.2% | 59.9% | **62.0%** | Steady, powerful expansion |
| Total costs & expenses | 223,101 | 237,628 | 273,797 | 149,226 | |
| Operating income *(d)* | 84,293 | 112,390 | **~131,800** *(d)* | 80,466 | |
| Operating margin | 27.4% | 32.1% | ~32.5% *(d)* | **35.0%** | 3 straight years of expansion |
| Equity securities gains | (392) | 3,714 | 24,080 | **135,946** | Now the dominant P&L driver |
| Effective tax rate | 13.9% | 16.4% | 16.8% | **19.1%** | Structural step-up |
| Diluted EPS | 5.80 | 8.04 | **10.81** | **14.24** | +38.6%, +34.5%, +178% |
| Basic EPS | 5.84 | 8.13 | 10.91 | 14.41 | |
| Net income *(d)* | ~72,800 | ~100,100 | **~132,300** | 174,771 | Derived from EPS × diluted shares |
| Comprehensive income | 76,996 | 99,720 | 135,054 | 174,402 | |
| SBC | 22,100 | 22,800 | 27,100 | 15,200 | +18.9% in FY25 |
| Capex | 32,251 | 52,535 | 91,447 | 80,598 | **Capex CAGR FY23→FY26E >70%** |
| Total debt (carrying) | — | 12,000 | 49,085 | **101,085** | |
| Buybacks | 61,504 | 62,222 | 45,709 | **0** | |
| Dividends | 0 | 7,363 | 10,049 | 5,231 | Initiated 2024 |

**Trajectory read:** four consecutive years of gross- and operating-margin expansion, revenue growth re-accelerating from ~14% to ~24%, and cash flow deteriorating from ~$70B of FCF to near-zero. That is precisely the financial signature of a company in the steep-investment phase of a platform transition.

**Derived TTM (through Q2 2026):** revenue ~**$448.6B**; operating income ~**$150.4B** (33.5% margin); capex ~**$132.4B**; FCF ~**$53.3B**; **diluted EPS ~$19.93**, of which **~$10.3 is core** (ex-investment gains) and **~$9.6 is investment gains**.

---

## 9. Liquidity, Solvency and Leverage

| Metric | 6/30/2026 | Comment |
|---|---|---|
| Cash + short-term investments | **$242,474M** | Up $115.6B in 6 months |
| Total debt (carrying) | $101,085M | +$52.0B in 6 months |
| Finance lease liabilities | $2,590M | |
| **Net cash (cash+ST inv. – debt)** | **+$138.8B** | Still a large net-cash position |
| Net cash excluding preferred | +$120.8B | |
| Interest coverage (H1 op. income / interest exp.) | **~44×** | 80,466 / 1,811 |
| Annualized cash interest run-rate | ~$4.0B | ~2.7% of annualized revenue |
| Current ratio *(d, est.)* | **~2.7×** | On ~$125B of estimated current liabilities |
| Debt / total capital *(d, est.)* | **~14%** | Includes preferred and est. equity of $600–625B |
| Operating lease liability | $18,037M | Remaining payments $21,333M; discounted excess $3,296M |
| Finance lease payments due | $2,920M | Discounted excess $330M |

**Verdict:** solvency is not a near-term concern, even after the leverage ramp. Coverage of ~44× and $139B of net cash give Alphabet enormous headroom. **The risk is not insolvency — it is capital-allocation returns and per-share dilution.** Note, however, that a third of the "cash" is being consumed annually by capex, so this buffer is depleting fast (net cash fell from roughly $78B→ implied... more precisely, cash grew only because $109.6B of securities were sold/raised; underlying cash generation was nearly fully absorbed).

---

## 10. Insider Transactions

**DATA UNAVAILABLE.** The data vendor has **no authorized, point-in-time insider-transaction archive for GOOGL as of 2026-08-28**. Per the vendor's explicit instruction, no insider buying or selling activity should be inferred or fabricated for this report. **Insider signal is therefore absent from this analysis** — traders should source Form 4 data independently before drawing conclusions about management's view of the buyback halt/equity issuance.

---

## 11. Risk Register / Red Flags

| # | Risk | Evidence | Severity |
|---|---|---|---|
| 1 | **Negative and deteriorating free cash flow** | Q2'26 FCF –$5,855M; H1 FCF $4,261M vs $24,254M LY; capex 36% of Q2 revenue | **High** |
| 2 | **Depreciation wave not yet in the P&L** | Capex/depreciation = 5.9×; depreciation +43% YoY already | **High** |
| 3 | **Reported EPS is ~70% investment marks and fully reversible** | Q2 EPS $9.11 vs core ~$2.68; $135.9B H1 non-operating gains | **High** |
| 4 | **Buyback halted + equity issued + convert issued = dilution** | $0 repurchases vs $45.7B FY25; $30.5B common + $19.1B preferred issued; shares +1.2% in 6 mo | **High** |
| 5 | **Concentration in AI capex with unproven returns** | $80.6B H1 capex, $29.1B incurred-not-paid; +$22.0B of external investments | **High** |
| 6 | **Cash tax step-up coming** | Book tax $41.4B vs current tax ~$13.9B; accrued current tax $0.5B→$5.2B; DTL $22.8B | Medium-High |
| 7 | **G&A/legal cost creep and contingency accruals** | G&A +50.6% QoQ; contingency accrual $15.6B→$17.4B; $3.0B settlement paid in Q3'25 | Medium |
| 8 | **Rising effective tax rate** | 13.9% → 16.4% → 16.8% → 19.1% | Medium |
| 9 | **SBC re-acceleration** | $27.1B FY25 (+19%); $15.2B H1'26 (+32%); 6.6% of revenue | Medium |
| 10 | **Rate/FX sensitivity of the investment portfolio** | $124.3B non-marketable + $99.5B AFS; AFS unrealized losses widened to $416M on $53.2B of securities in a loss position | Medium |
| 11 | **Earnings-composition opacity** | ~$72.6B of H1 gains not explained by disclosed FVNI/measurement-alternative components — requires 10-Q note review | Medium |
| 12 | Balance-sheet/solvency | Net cash +$138.8B, 44× interest coverage, debt/cap ~14% | **Low** |

---

## 12. Actionable Takeaways for Traders

### What the fundamentals actually support
1. **The core franchise is performing better than at any point in the last five years.** Revenue +24.2% YoY, gross margin 61.6%, operating margin 34.0%, operating income +30.4% YoY. Do not let the cash-flow panic obscure this.
2. **But do not use reported EPS.** On a consistent ex-investment-gain basis, **Q2 2026 core EPS is ~$2.68 (+24% YoY) and TTM core EPS is ~$10.3** — versus headline TTM EPS of ~$19.93. Any screen or model fed headline EPS will materially misprice GOOGL. The gap (~$9.6/share of TTM marks) is a mark-to-market asset, not earning power.
3. **The correct valuation frame is now FCF- and capex-based, not EPS-based.** TTM FCF of ~$53B against a $132B capex program means FCF is a *choice variable*, not an output. Model FY2026 capex of **$165–180B** (H1 $80.6B + Q2 run-rate + $29.1B already incurred-not-paid) and H2 FCF at or below zero.
4. **Expect a dilution regime, not an accretion regime.** Assume share count grows 1.5–3%/yr from SBC plus the $19B convertible, with buybacks absent while capex is at these levels. EPS growth will lag net income growth by that amount.

### Trade construction ideas
- **Long-operating / short-headline-EPS setup:** the market is likely to react to headline EPS beats/misses that are driven by marks. A quarter with strong core results but negative marks (or vice versa) is a high-probability mispricing event. Position around Q3 2026 print (expected late October 2026) with an explicit view on the direction of public tech marks.
- **Watch the Q2→Q3 operating margin line as the primary fundamental trigger.** Q2 slipped to 34.0% from 36.1%. Two consecutive quarters of margin compression with an unchanged revenue trajectory would confirm that the depreciation and opex wave is arriving faster than AI revenue — that is the bear thesis' confirmation signal. Conversely, margin *stabilization* above ~34% while revenue grows >20% is the bull confirmation.
- **Upgrade/downgrade triggers to monitor:**
  - **Bullish:** Q3 operating margin ≥35%; capex guidance held or cut; buyback explicitly resumed; depreciation growth decelerating relative to revenue; deferred revenue growing >20% YoY.
  - **Bearish:** another quarter of negative FCF; a second consecutive sequential margin decline; a large negative remeasurement of the investment portfolio; further equity/preferred issuance; a covenant-adjacent or ratings-relevant debt increase above ~$150B.
- **Event risk:** the ~$72.6B unexplained component of the H1 gain will be detailed in the 10-Q equity-securities note. If it is a one-time remeasurement on a holding that became observable, headline EPS will face a brutal comparable in 2027 — plan for a mechanical "EPS decline" headline next year that is meaningless operationally.
- **Dividend** ($0.22/qtr, ~$0.88 annualized) remains trivially covered by CFO ($84.9B vs ~$10.5B/yr) — no dividend risk.

### Specific quantified watch-list for the next print
| Item | Latest reading | Threshold that matters |
|---|---|---|
| Operating margin | 34.0% | <33% = bear confirmation; >35% = bull |
| Operating income YoY | +30.4% | <+20% = deceleration |
| Capex (quarterly) | $44.9B | >$50B = FCF stays negative |
| Capex incurred-not-paid | $29.1B | Rising = accelerating spend |
| FCF | –$5.9B | 2nd negative quarter = structural |
| Depreciation YoY | +43.2% | >+60% = margin pressure |
| SBC % revenue | 6.6% | >7% = dilution acceleration |
| Share count | 12.230B | >12.35B = dilution >2%/yr |
| Non-operating income | $98.0B | Sign flip = EPS air pocket |
| Effective tax rate | 19.1% | >20% = EPS headwind |
| Total debt | $101.1B | >$150B = leverage narrative shift |
| Contract liabilities | $10.1B | <+15% YoY = AI demand doubt |
| Buyback | $0 | Resumption = major bullish signal |

---

## 13. Data Provenance & Limitations (read before using numbers)

- **Source:** point-in-time SEC facts filtered by EDGAR acceptance time, public by 2026-08-28. Latest 10-Q (accession 0001652044-26-000071) accepted **2026-07-23**; FY2025 10-K (0001652044-26-000018) accepted **2026-02-05**.
- **Derived (not literally reported) figures are marked *(d)*:** Revenue (= CostsAndExpenses + OperatingIncomeLoss; identity verified against FY2023 and FY2024), gross profit, "R&D + S&M" residual, Q1 2026/Q1 2025 stand-alone periods (H1 less Q2), FY2025 revenue/operating income/net income, TTM aggregates, diluted share counts, core EPS, current ratio, equity and debt/capital estimates.
- **FY2025 revenue (~$405.6B), FY2025 operating income (~$131.8B) and FY2023/FY2025 net income are estimates**, back-solved from reported costs/expenses, the effective tax rate and diluted EPS × diluted shares. They are directionally reliable but should be replaced with reported figures before use in a valuation model.
- **Not available from these tools:** share price, market cap, P/E, dividend yield, EV/EBITDA (no price data); segment-level revenue and operating income; R&D and S&M separately; PP&E, goodwill, total liabilities and total stockholders' equity line items; full-year revenue/operating income for FY2025; and **all insider-transaction data**.
- **Earnings-quality caveat:** the breakdown of the $135.9B H1 2026 equity gain is only partially identifiable from the tags provided (~$72.6B unexplained). Treat the composition as provisional pending the 10-Q notes.

---

## 14. Summary Table

| Category | Metric | Latest Reading | Prior / Comparison | Direction & Signal |
|---|---|---|---|---|
| **Growth** | Revenue (Q2'26, derived) | $119,796M | +24.2% YoY, +9.0% QoQ | 🟢 Accelerating |
| | H1'26 revenue | $229,692M | +23.1% YoY | 🟢 Strong |
| | TTM revenue (derived) | ~$448,600M | — | 🟢 |
| **Profitability** | Gross margin Q2'26 | 61.6% | 59.5% Q2'25 | 🟢 +210bp |
| | Operating margin Q2'26 | 34.0% | 36.1% Q1'26 / 32.4% Q2'25 | 🟡 +YoY, –QoQ |
| | Operating income H1'26 | $80,466M | +30.0% YoY | 🟢 |
| | H1'26 operating margin | 35.0% | 33.1% H1'25 | 🟢 +190bp |
| **Earnings quality** | Reported diluted EPS Q2'26 | $9.11 | +294% YoY | 🔴 70% is investment marks |
| | Core EPS Q2'26 (derived) | ~$2.68 | +24% YoY | 🟢 True run-rate |
| | H1'26 net income | $174,771M | vs $62,736M | 🔴 78% from non-operating |
| | H1'26 non-operating income | $135,699M | vs $13,845M | 🔴 Volatile, reversible |
| | TTM EPS / core EPS (derived) | ~$19.93 / ~$10.3 | — | 🔴 Nearly 2× gap |
| **Cash flow** | H1'26 CFO | $84,859M | +32.8% YoY | 🟢 |
| | H1'26 capex | $80,598M | +103.3% YoY | 🟡 Massive buildout |
| | H1'26 FCF | **$4,261M** | vs $24,254M | 🔴 –82% |
| | Q2'26 FCF | **–$5,855M** | vs +$10,116M Q1'26 | 🔴 Negative |
| | TTM FCF (derived) | ~$53,300M | vs $73,266M FY25 | 🔴 –27% |
| | Capex/revenue | 35.1% (H1) / 37.5% (Q2) | 21.2% H1'25 | 🔴 |
| | Capex incurred-not-paid | $29,113M | $10,635M LY | 🟡 Committed H2 outflow |
| **Balance sheet** | Total assets | $921,983M | $595,281M at 12/31/25 | 🟡 +55% in 6 months |
| | Cash + ST investments | $242,474M | $126,843M | 🟢 |
| | Total debt | $101,085M | $49,085M | 🟡 2.1× in 6 months |
| | Net cash (cash – debt) | ~+$138,800M | — | 🟢 Fortress |
| | Deferred tax liability | $22,819M | $919M | 🔴 Tax on unrealized gains |
| | Contract liabilities | $10,100M | $8,600M | 🟢 +17.4% |
| | Non-marketable equity | $124,259M | $64,094M | 🟡 Hidden asset / vol risk |
| **Capital allocation** | Buybacks H1'26 | **$0** | $45,709M FY25 | 🔴 Highest-signal change |
| | Common stock issued | $30,499M | $0 prior | 🔴 Dilution |
| | Convertible preferred issued | $19,063M | new | 🔴 Future dilution |
| | Debt raised H1'26 | $56,226M | $64,564M FY25 | 🟡 |
| | Dividends H1'26 | $5,231M ($0.43/sh) | +4.8% DPS growth | 🟢 |
| | Shares outstanding | 12,230M | 12,088M | 🔴 +1.2% in 6 months |
| | SBC H1'26 | $15,200M | +32.2% YoY | 🔴 6.6% of revenue |
| **Cost structure** | Depreciation H1'26 | $13,586M | +43.2% YoY | 🟡 Wave beginning |
| | Interest expense H1'26 | $1,811M | +513% YoY | 🟡 ~44× coverage |
| | G&A Q2'26 | $6,461M | +50.6% QoQ | 🔴 Legal/opex creep |
| | Effective tax rate | 19.1% | 13.9% (FY23) | 🔴 Structural step-up |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | — | ⚪ No signal available |
| **Verdict** | Operating business | Excellent, accelerating | — | 🟢 |
| | Financial model | Transitioning to capital-intensive, diluted, FCF-negative | — | 🔴 |
| | **Net** | **Quality franchise, deteriorating per-share cash economics; value on ex-gains earnings and capex/FCF trajectory, not headline EPS** | — | 🟡 |