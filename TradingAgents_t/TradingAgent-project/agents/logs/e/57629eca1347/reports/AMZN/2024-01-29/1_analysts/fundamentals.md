# AMZN — Fundamental Research Report
**Company:** Amazon.com, Inc. (AMZN)
**Analysis date:** 2024-01-29 | **Data as of:** latest filing accepted by EDGAR = Q3 2023 Form 10-Q (accepted 2023-10-27), period ended **2023-09-30**
**Source:** Point-in-time SEC XBRL facts (no post-Oct-2023 filings in the archive)

> **Critical data-timing note:** The FY2023 10-K (Q4/holiday quarter) has **not yet been filed** as of 2024-01-29. Everything below is as of 9/30/2023. AMZN's Q4 2023 report is due within days of this analysis date — this is the single dominant near-term catalyst and *is not reflected in any figure in this report*. Revenue was not returned as a discrete tag in the extract; I reconstruct it as **CostsAndExpenses + OperatingIncomeLoss** (this reconciles exactly: Q3'23 = $131,895M + $11,188M = $143,083M).

---

## 1. Company Profile & Business Structure

Amazon operates **3 reportable segments** (confirmed: `NumberOfOperatingSegments = 3`):
- **North America** (retail, marketplace, ads, Prime)
- **International** (retail, marketplace, ads, Prime)
- **AWS** (cloud compute, storage, database, AI/ML)

Structural characteristics visible in the filing data:
- **No dividends and no buybacks**: `PaymentsForRepurchaseOfCommonStock = $0` for 9M 2023 and for the full trailing-12M period (vs. $6.0B repurchased in 2022). All capital is being reinvested into capex, AWS infrastructure, and debt reduction.
- **Heavy lease-based asset model**: operating lease liabilities **$73.9B** + finance lease liabilities **$12.5B** = **$86.4B** of lease obligations, alongside $67.5B of debt — total fixed obligations of ~$153.8B.
- **Equity-compensation-heavy culture**: $17.7B of SBC in 9M 2023 alone, and **$23.3B of unrecognized future SBC** already granted.
- **Share count creep**: 10,330M shares outstanding at 9/30/23 vs. 10,242M at 12/31/22 (**+0.9% in 9 months**); 10,334.0M as of the 10/18/23 cover date.

---

## 2. Income Statement — The Margin Inflection Is Real and Large

*(All $M. Revenue = CostsAndExpenses + OperatingIncomeLoss)*

| Metric | Q3 2022 | Q3 2023 | YoY | 9M 2022 | 9M 2023 | YoY |
|---|---|---|---|---|---|---|
| **Revenue** | 127,101 | **143,083** | **+12.6%** | 364,779 | **404,824** | **+11.0%** |
| Cost of goods & services | 70,268 | 75,022 | +6.8% | 203,191 | 212,186 | **+4.4%** |
| **Gross margin** | 44.7% | **47.6%** | +290 bps | 44.3% | **47.6%** | +330 bps |
| Total costs & expenses | 124,576 | 131,895 | +5.9% | 355,268 | 381,181 | +7.3% |
| **Operating income** | 2,525 | **11,188** | **+343%** | 9,511 | **23,643** | **+148.6%** |
| **Operating margin** | 2.0% | **7.8%** | +580 bps | 2.6% | **5.8%** | +320 bps |
| Marketing expense | 11,014 | 10,551 | −4.2% | 29,420 | 31,468 | +7.0% |
| G&A expense | 3,061 | 2,561 | −16.3% | 8,558 | 8,806 | +2.9% |
| D&A | 10,327 | 12,131 | +17.5% | 29,236 | 34,843 | +19.2% |
| Interest expense | 617 | 806 | +30.6% | 1,673 | 2,469 | +47.6% |
| Interest & investment income | 277 | 776 | +180% | 544 | 2,048 | +276% |
| Non-operating income/(expense) | +419 | +1,001 | — | (14,485) | +228 | — |
| Pre-tax income | 2,944 | 12,189 | +314% | (4,974) | **23,871** | n.m. |
| Tax expense | 69 | 2,306 | — | (1,990) | 4,058 | — |
| **Net income** | 2,872 | **9,879** | **+244%** | (3,000) | **19,801** | n.m. |
| **Diluted EPS** | 0.28 | **0.94** | +236% | (0.29) | **1.89** | n.m. |
| Effective tax rate | 2.3% | 18.9% | — | −40.0% | 17.0% | — |

**What the numbers say:**
1. **Operating leverage is the story.** Revenue +11.0% against COGS +4.4% produced a **330 bps gross-margin expansion** and a **320 bps operating-margin expansion** over 9M. Q3 alone delivered 7.8% operating margin — the highest quarterly level in the dataset and a 4x improvement YoY. Cost discipline (fulfillment/regionalization, headcount, marketing/G&A down) plus lower unit costs from a re-architected network are flowing straight to the operating line.
2. **Q4 2022 comparison base is now the key swing factor — and it's absent from the data.** Since 9M 2023 operating income ($23.6B) already exceeds full-year 2022 operating income, the trailing-twelve-month operating margin is materially above the 5.8% 9M figure. Any Q4 2023 print that fails to hold ~7%+ operating margin would puncture the re-rating thesis.
3. **Earnings quality caveat:** Q3 2023 non-operating income of $1,001M includes a **$1,200M mark-to-market gain on equity securities** (Rivian-type holdings). Strip it out and core pre-tax income is ~$11.0B; net income closer to ~$8.9B. This is *not* repeatable and should be excluded from run-rate earnings.
4. **Interest dynamics have flipped from headwind to neutral.** Interest expense rose 47.6% YoY to $2,469M, but interest income rose 276% to $2,048M — 9M net interest cost is just **$421M** vs. $1,129M a year ago. With $99.5B of liquid assets earning ~5% and gross debt being paid down, this is now a modest tailwind.
5. **Deferred tax is a live earnings support:** a **−$4,412M deferred tax benefit** in 9M 2023 reduced the effective rate to 17.0% (cash taxes paid: $6,982M). Sustained deferred benefits would keep the tax rate below the 21% statutory level — a recurring, if quiet, EPS helper.
6. **SBC is growing faster than revenue** (+26.3% vs +11.0%). GAAP margins are flattered relative to cash economics; $17.7B of 9M operating income is SBC add-back. Adjust operating margin for SBC and 9M op margin falls to roughly **~1.4%** on a fully-loaded basis. Any "margin expansion" claim must be read against this.

---

## 3. Cash Flow — The FCF Inflection Is the Most Bullish Datapoint in the Dataset

*(Trailing 12 months = 2022-10-01 → 2023-09-30, per filed XBRL; prior TTM = 2021-10-01 → 2022-09-30)*

| Metric ($M) | TTM to 9/30/22 | TTM to 9/30/23 | Change |
|---|---|---|---|
| **Operating cash flow** | 39,665 | **71,654** | **+$32.0B (+80.6%)** |
| Capex (purchases of productive assets) | 65,988 | **54,733** | **−$11.3B (−17.1%)** |
| **Free cash flow (OCF − capex)** | **(26,323)** | **+16,921** | **+$43.2B swing** |
| FCF after finance-lease principal | (34,884) | 11,676 | +$46.6B |
| D&A | 39,103 | 47,528 | +21.5% |
| Net income | 11,323 | 20,079 | +77.3% |
| Income taxes paid (cash) | 4,674 | 8,677 | +85.6% |

**Quarterly detail (capex vs. OCF):**

| $M | Q3 2022 | Q3 2023 | YoY |
|---|---|---|---|
| OCF | 11,404 | **21,217** | **+86.1%** |
| Capex | 16,378 | **12,479** | **−23.8%** |
| FCF | (4,974) | **+8,738** | +$13.7B |
| 9M OCF | 17,579 | **42,481** | **+141.7%** |
| 9M Capex | 47,053 | **38,141** | −18.9% |
| 9M FCF | (29,474) | **+4,340** | +$33.8B |

**Interpretation and actionable read-through:**
- **The FCF swing is earnings-driven, not working-capital-driven.** Working capital was a use of cash in *both* periods (9M'23 use ≈ $18.4B: AR/other −$10.4B, accrued liabilities −$9.0B, partly offset by +$0.9B contract liabilities; 9M'22 use ≈ $18.7B). So the +$24.9B improvement in 9M OCF came from **operating profitability and non-cash add-backs (D&A +$5.6B)**, not from stretching payables. That is the highest-quality FCF improvement possible.
- **Capex discipline (+17% decline TTM) is the second driver.** Capex fell from 17.9% of revenue (9M'22) to **9.4% of revenue (9M'23)**. Amazon is harvesting the 2021–22 infrastructure build. **Risk:** any signal (in the imminent Q4 call) that 2024 capex re-accelerates for AI/ AWS will compress near-term FCF — this is the key bear vector for the stock.
- **OCF conversion is strong:** 9M'23 OCF $42.5B vs. net income $19.8B = **2.15x cash conversion**, supported by $35.7B of D&A + SBC.
- **Still no capital returns.** $0 buyback, $0 dividend. Financing outflow was −$9,133M in 9M'23 (net LT debt repayments of $3,386M; short-term borrowings $17,395M vs. $19,339M repayments). When AMZN eventually resumes buybacks, that is a discrete re-rating catalyst to monitor.

---

## 4. Balance Sheet — Deleveraged, Liquid, and Lease-Heavy

*(9/30/2023 vs. 12/31/2022, $M)*

| Item | 12/31/2022 | **9/30/2023** | Change |
|---|---|---|---|
| Cash & equivalents | 53,888 | **49,605** | −4,283 |
| Marketable securities (AFS, FV) | — | **49,871** | — |
| **Total liquid assets** | ~103,700 | **99,476** | — |
| Accounts receivable, net | 42,360 | 43,420 | +1,060 |
| Inventory, net | 34,405 | **35,406** | +1,001 |
| **Current assets** | 146,791 | **142,995** | −3,796 |
| **Total assets** | 462,675 | **486,883** | **+24,208** |
| Accounts payable | 79,600 | **72,004** | **−7,596** |
| Accrued liabilities | 62,566 | 58,812 | −3,754 |
| **Current liabilities** | 155,393 | **145,214** | −10,179 |
| Long-term debt (current) | 2,999 | 5,995 | +2,996 |
| Long-term debt (non-current) | 67,150 | **61,098** | −6,052 |
| **Total debt** | 70,149 | **67,093** (67,472 gross) | **−3.1B** |
| Finance lease liability | 15,783 | **12,466** | −3,317 |
| Operating lease liability | 69,040 | **73,902** | +4,862 |
| Contract liabilities (deferred revenue) | 16,100 | 17,098 | +998 |
| AOCI | (4,487) | (5,003) | −516 |
| Additional paid-in capital | 75,066 | **92,711** | +17,645 |

**Liquidity & leverage calculations:**
- **Current ratio: 0.985** (142,995 / 145,214) — below 1.0, but this is structurally normal for Amazon given its payables-funded model.
- **Quick ratio: 0.74** ((142,995 − 35,406) / 145,214); **cash-to-current-liabilities: 0.69**.
- **Net cash position (ex-leases): $32.0B** (99,476 liquid − 67,472 debt). **Net cash including finance leases: $19.5B.** Including operating leases: **net debt of ~$54B** (still <0.5x annualized revenue).
- **Deleveraging is complete and deliberate:** gross debt down $3.1B, and **zero long-term debt issued in 9M 2023** (vs. $8.2B issued in the prior TTM). Finance lease liabilities down 21%.
- **Contractual obligations: $284.4B total**, with $35.7B due within 12 months, $28.4B in year 2, $23.8B in year 3, $26.6B in year 4, and the remainder ($169.8B) beyond — dominated by the $88.8B of undiscounted operating lease commitments. Refinancing risk is low; **renewal/lease-roll risk is the structural exposure** (weighted-average discount rate rose from 2.8% to **3.2%**, so renewed leases are getting more expensive).
- **Asset quality signals are benign:** inventory valuation reserves fell $2.80B → $2.60B (better sell-through/less markdown risk); allowance for doubtful accounts $1.40B → $1.50B (AR coverage steady at ~3.5%); impairments minimal at $420M for 9M.
- **Equity build:** APIC +$17.6B (SBC issuance) plus 9M net income $19.8B less $0.5B AOCI. Note: total stockholders' equity is not returned as a discrete tag in this extract, so ROE cannot be computed from tool data alone — flag this as a data gap rather than estimate it.

---

## 5. Valuation Frame (with explicit assumptions)

The toolset returns no price, market cap, or consensus data. To make the report tradable I apply an **assumed reference price of ~$155–160/share** (late-Jan-2024 market context, **external to these tools — verify before trading**), implying market cap ≈ **$1.60–1.65T** and enterprise value ≈ **$1.60–1.65T** (net cash ex-leases roughly offsets lease obligations).

| Multiple (on tool-derived fundamentals) | Value | Read |
|---|---|---|
| EV / annualized Q3'23 revenue ($572.3B run-rate) | **~2.8x** | Rich vs. retail, justified by AWS/ads mix |
| Price / TTM net income ($20.08B) | **~81x** | Looks extreme, but TTM spans the 2022 trough |
| Price / annualized Q3'23 net income ($39.5B) | **~41x** | More representative of current earnings power |
| Price / TTM FCF ($16.92B) | **~96x** | FCF is still early in its ramp; the *direction* (+$43B YoY) matters more than the level |
| EV / annualized Q3'23 operating income ($44.8B) | **~36x** | The cleanest "quality of earnings" multiple |

**Takeaway:** AMZN is priced for **continued margin expansion and FCF compounding**, not for current cash generation. The multiple is defensible only if Q3's ~7.8% operating margin is a floor rather than a peak, and if capex stays near 9–10% of revenue.

---

## 6. Insider Transactions

**DATA UNAVAILABLE.** The data package contains no authorized, point-in-time insider-transaction archive for AMZN as of 2024-01-29. **No insider buying or selling signal exists for this analysis, and none should be inferred or fabricated.** Traders should treat this as a blind spot and source Form 4 data separately before acting on any insider-flow thesis.

---

## 7. Actionable Conclusions for Traders

**Bull case (well-supported by this dataset):**
1. **Operating margin structurally reset** — 5.8% for 9M vs. 2.6%, with Q3 at 7.8%. Cost of sales growing at 4.4% vs. revenue at 11.0% is the proof.
2. **FCF inflection of +$43.2B TTM** with capex intensity halved (17.9% → 9.4% of revenue). This is the single most powerful re-rating driver in the data and it is *earnings-driven*, not working-capital-manipulated.
3. **Balance sheet fully de-risked** — $32B net cash ex-leases, no new LT debt issued, finance leases cut 21%, liquid assets of $99.5B, interest income now nearly offsetting interest expense.
4. **Tax and interest tailwinds** — 17.0% effective rate with a $4.4B deferred benefit, plus ~$1.5B/yr of incremental net interest income vs. 2022.

**Bear risks / what to police:**
1. **Imminent Q4 2023 report (~Feb 1, 2024)** is not in this data. The entire thesis rests on Q4 confirming ≥7% operating margin and AWS stability. Consider event-risk sizing (options, reduced gross exposure) into the print.
2. **Capex re-acceleration risk** — any 2024 capex guide above ~12% of revenue for AI/AWS would immediately compress the FCF story that justifies ~96x TTM FCF.
3. **SBC dilution** — +26% YoY to $17.7B, with $23.3B unrecognized. Fully-loaded operating margins are ~4.4 pts lower than GAAP. Diluted share count keeps rising.
4. **Non-operating gains are not repeatable** — $1.2B of Q3 equity mark-to-market gains flatter EPS by roughly $0.09–0.10; do not annualize Q3 net income without adjustment.
5. **Payables contraction of $7.6B** since year-end is a cash-flow caveat to watch (supplier payment timing) and could reverse.
6. **Lease obligations ($86.4B) and rising discount rates (2.8% → 3.2%)** create creeping occupancy cost inflation.
7. **No capital returns** — no buyback, no dividend. There is no valuation floor from shareholder yield.

**Positioning summary:** Fundamentals support a **constructive medium-term stance** on AMZN driven by margin/FCF compounding and a fortress balance sheet, but the stock is **not cheap on trailing cash flow** and carries **acute near-term event risk** from the Q4 print and 2024 capex guidance. A staged entry (partial now, add on confirmed Q4 margin/capex commentary) is better risk-adjusted than a full position ahead of earnings.

---

## 8. Key Points Summary Table

| Category | Metric / Finding | Value | Signal |
|---|---|---|---|
| **Data currency** | Latest filing in archive | Q3 2023 10-Q (2023-10-27) | ⚠️ Q4/FY23 not yet reported; results imminent |
| **Growth** | 9M 2023 revenue | $404,824M, **+11.0% YoY** | 🟢 Solid, decelerating from 2022 |
| **Growth** | Q3 2023 revenue | $143,083M, **+12.6% YoY** | 🟢 Reacceleration vs. 9M |
| **Profitability** | 9M 2023 operating income | $23,643M vs. $9,511M | 🟢 **+149%** |
| **Profitability** | Q3 2023 operating margin | **7.8%** vs. 2.0% | 🟢 **+580 bps — the core thesis** |
| **Profitability** | Gross margin (9M) | **47.6%** vs. 44.3% | 🟢 COGS +4.4% vs. rev +11.0% |
| **Profitability** | 9M 2023 net income / diluted EPS | $19,801M / **$1.89** | 🟢 vs. −$3,000M / −$0.29 |
| **Quality of earnings** | Q3 non-operating income (equity MTM) | $1,001M (incl. $1,200M gain) | ⚠️ Non-repeatable; ~$0.09–0.10 of EPS |
| **Cash flow** | TTM operating cash flow | **$71,654M** (+80.6%) | 🟢 |
| **Cash flow** | TTM capex | **$54,733M** (−17.1%) | 🟢 Capex intensity 17.9% → 9.4% of rev |
| **Cash flow** | **TTM free cash flow** | **+$16,921M** vs. −$26,323M | 🟢 **+$43.2B swing — best datapoint** |
| **Cash flow** | 9M'23 working capital | ~$18.4B **use** of cash | 🟢 FCF gain is earnings-driven, not WC |
| **Balance sheet** | Cash + marketable securities | $99,476M | 🟢 |
| **Balance sheet** | Total debt / net cash ex-leases | $67,093M / **+$32.0B net cash** | 🟢 Deleveraged |
| **Balance sheet** | Current ratio / quick ratio | 0.985 / 0.74 | 🟡 Structurally thin, payables-funded |
| **Balance sheet** | Operating + finance lease liabilities | **$86,368M** | 🟡 Rising lease discount rate (2.8% → 3.2%) |
| **Balance sheet** | Contractual obligations | $284,407M ($35.7B due <12M) | 🟡 Lease-dominated; low refi risk |
| **Capital returns** | Buybacks / dividends | **$0 / $0** (9M'23) | 🟡 No shareholder-yield floor |
| **Compensation** | 9M SBC / unrecognized | $17,704M (+26.3%) / $23,300M | 🔴 Dilution & GAAP margin flattery |
| **Shares** | Diluted share count trend | 10,242M → 10,330M (+0.9% in 9M) | 🔴 Creep |
| **Interest** | 9M interest expense vs. income | $2,469M vs. $2,048M (net $421M) | 🟢 Headwind neutralized |
| **Tax** | 9M effective rate / deferred benefit | 17.0% / −$4,412M | 🟢 Below statutory |
| **Segments** | Reportable segments | 3 (NA, Int'l, AWS) | — Segment P&L not in extract |
| **Valuation** | ~81x TTM P/E; ~96x TTM P/FCF; ~2.8x EV/run-rate sales | On assumed ~$155–160/sh (external) | 🔴 Prices in continued margin/FCF ramp |
| **Insider flow** | Form 4 activity | **DATA UNAVAILABLE** | ⚫ No signal — do not infer |
| **Near-term catalyst** | Q4 2023 earnings | Due ~Feb 1, 2024 | ⚠️ Binary event risk; not in data |
| **Verdict** | Medium-term | Margin + FCF compounding, fortress B/S | 🟢 **Constructive, staged entry** |