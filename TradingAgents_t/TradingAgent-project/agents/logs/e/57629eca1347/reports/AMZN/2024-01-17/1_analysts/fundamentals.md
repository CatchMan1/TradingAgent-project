# AMZN — Amazon.com, Inc.
## Fundamental Research Report | Data as of 2024-01-17

---

## ⚠️ 0. Data Scope, Staleness & Integrity Notes (read first)

Before the analysis, three important caveats about what the toolset actually returned:

1. **The most recent SEC filing in the dataset is the Q3-2023 10-Q, accepted 2023-10-27** (accession 0001018724-23-000018). There have been **no new financial filings in the past week** — or in the past ~11 weeks. Every balance-sheet and cash-flow item is "as of 2023-09-30." Q4/FY2023 results were **not yet reported** as of 2024-01-17 (AMZN typically reports early February), so **no FY2023 annual statement data exists in this dataset.**
2. **Annual requests returned identical data to quarterly requests.** The `freq=annual` calls for the income statement, balance sheet, and cash flow returned the same Q3-2023 10-Q fact set. I therefore reconstruct trailing-twelve-month (TTM) and year-to-date aggregates arithmetically from the disclosed periods rather than relying on annual statements.
3. **Insider transactions are unavailable.** The vendor explicitly returned: *"no authorized, point-in-time insider-transactions archive for AMZN by 2024-01-17."* I will **not** infer or fabricate insider buying/selling. This is a genuine information gap in this report.
4. **Price/market-cap data is not provided by these tools.** Where I compute valuation multiples I use an explicit reference price and flag it as an assumption, not tool output.
5. A handful of widely-reported FY2022/Q4-2022 figures (e.g., FY2022 revenue $513.98B) are used **only** to build TTM bridges and are marked as external to the tool output.

**Bottom line on data:** this is a *point-in-time, Q3-2023-anchored* fundamental picture. It is highly informative on the margin and cash-flow inflection, but it is **blind to Q4 2023 (the holiday quarter)**, which is the single most important swing factor for the stock over the next two weeks.

---

## 1. Company Profile & Business Model

**Amazon.com, Inc. (AMZN)** — the world's largest e-commerce and cloud-infrastructure company. The 10-Q confirms **3 reportable operating segments** (`NumberOfOperatingSegments = 3`):

| Segment | What it is | Economic character |
|---|---|---|
| **North America** | Retail, marketplace (1P + 3P), Prime, advertising, devices, physical stores | High-volume, capex-heavy; margin inflection underway |
| **International** | Same model ex-North America (EU, UK, JP, IN, etc.) | Historically loss-making, swinging toward profitability |
| **AWS** | Cloud compute, storage, database, AI/ML, plus advertising-adjacent services | The profit engine — structurally highest margin |

**Key structural facts visible in the data:**
- **Third-party/marketplace and advertising are embedded in reported "revenue"** but are far higher-margin than 1P retail — this is why Amazon's blended gross margin can rise without any pricing power.
- **Capital intensity is extreme**: TTM purchases of productive assets (capex) of **$54.7B**, TTM depreciation & amortization of **$47.5B**.
- **Leases are a first-order part of the balance sheet**: **$73.9B** of operating lease liabilities plus **$12.5B** of finance lease liabilities at 9/30/23. Any "debt" analysis that ignores leases understates leverage by ~$86B.
- **Equity compensation is a material economic cost**: $17.7B in 9M-2023 alone, with **$23.3B of unrecognized SBC** still to be expensed.

---

## 2. Income Statement Analysis — The Margin Inflection Is Real and Large

Note: the dataset does **not** contain a discrete `Revenues` tag. Revenue is reconstructed as **`CostsAndExpenses` + `OperatingIncomeLoss`** on every period, and this reconstruction reconciles exactly to Amazon's reported net sales — a strong internal consistency check.

### 2.1 Reconstructed revenue & profitability

| Metric ($M) | Q3-2022 | **Q3-2023** | YoY Δ | 9M-2022 | **9M-2023** | YoY Δ |
|---|---:|---:|---:|---:|---:|---:|
| **Net sales (derived)** | 127,101 | **143,083** | **+12.6%** | 364,779 | **404,824** | **+11.0%** |
| Cost of goods & services | 70,268 | **75,022** | +6.8% | 203,191 | **212,186** | +4.4% |
| **Gross profit** | 56,833 | **68,061** | +19.8% | 161,588 | **192,638** | +19.2% |
| **Gross margin** | 44.7% | **47.6%** | **+290 bps** | 44.3% | **47.6%** | **+330 bps** |
| Marketing expense | 11,014 | **10,551** | **−4.2%** | 29,420 | **31,468** | +7.0% |
| G&A expense | 3,061 | **2,561** | **−16.3%** | 8,558 | **8,806** | +2.9% |
| Total costs & expenses | 124,576 | **131,895** | +5.9% | 355,268 | **381,181** | +7.3% |
| **Operating income** | 2,525 | **11,188** | **+343%** | 9,511 | **23,643** | **+149%** |
| **Operating margin** | 1.99% | **7.82%** | **+583 bps** | 2.61% | **5.84%** | **+323 bps** |
| Non-operating income/(expense) | 419 | **1,001** | +139% | (14,485) | **228** | nm |
| Pre-tax income | 2,944 | **12,189** | +314% | (4,974) | **23,871** | nm |
| Income tax | 69 | **2,306** | nm | (1,990) | **4,058** | nm |
| **Net income** | 2,872 | **9,879** | **+244%** | (3,000) | **19,801** | nm |
| **Net margin** | 2.26% | **6.90%** | +464 bps | −0.82% | **4.89%** | nm |
| **Diluted EPS** | $0.28 | **$0.94** | **+236%** | $(0.29) | **$1.89** | nm |
| Tax rate | 2.3% | **18.9%** | — | nm | **17.0%** | — |

### 2.2 The three decisive observations

**(a) Operating leverage is overwhelming, not marginal.** 9M-2023 total costs & expenses grew **+7.3%** against revenue growth of **+11.0%** — a ~370bp cost-growth gap that flowed almost entirely to operating income. In Q3 alone, costs grew **+5.9%** vs. revenue **+12.6%**, producing a **583bp** operating-margin expansion to **7.82%**. Operating income more than quadrupled year-over-year to $11.2B on a single quarter.

**(b) The leverage came from *cost* lines, not just revenue mix.** Two lines shrank outright in Q3:
- **Marketing expense −4.2% YoY** despite revenue +12.6% (9M: +7.0%, well below revenue growth).
- **G&A −16.3% YoY** (9M: +2.9%).

That is the signature of the 2022–2023 cost-restructuring program (fulfillment regionalization, corporate headcount reductions) still working through the P&L. This is *high-quality* margin expansion — it is not a one-time accounting item. Note 9M-2023 G&A includes a **$200M contract-termination loss** (vs. $300M in 9M-2022), which I conservatively left in the expense base.

**(c) Q3 net income was flattered by ~$1.2B of mark-to-market gains — adjust for it.** `EquitySecuritiesFvNiGainLoss` was **+$1,200M in Q3-2023** (vs. +$1,000M for the full first nine months, implying **−$200M in H1**). This non-operating gain sits inside the $1,001M non-operating line. Backing it out, Q3 pre-tax income of $12,189M drops to roughly **$11.0B**, and net income to roughly **$9.0B** (~$0.86/share vs. the reported $0.94). **The operating line ($11,188M) is the clean number; the EPS line carries a ~$0.08–0.09 boost from investment marks.** Traders extrapolating Q3 EPS as a run-rate should haircut ~8–10%.

### 2.3 Interest expense & the rate cycle — an underappreciated tailwind

| ($M) | Q3-2022 | Q3-2023 | 9M-2022 | 9M-2023 |
|---|---:|---:|---:|---:|
| Interest expense | 617 | **806** | 1,673 | **2,469** |
| Interest & investment income | 277 | **776** | 544 | **2,048** |
| **Net interest** | **(340)** | **(30)** | **(1,129)** | **(421)** |

Amazon has nearly **neutralized its net interest position**. Investment income rose **3.8x** (from $544M to $2,048M for 9M) as its ~$99.5B cash & securities pile earned higher rates — this almost fully offset the rise in interest expense. Additionally, **interest expense is now falling sequentially**: 9M total of $2,469M less Q3's $806M implies ~$1,663M in H1 (≈$832M/quarter), meaning Q3's $806M is below the H1 run-rate as gross debt falls. This is a durable, structural EPS tailwind for 2024 that is easy to overlook.

### 2.4 SBC and the dilution reality

| ($M) | Q3-2022 | Q3-2023 | 9M-2022 | 9M-2023 |
|---|---:|---:|---:|---:|
| Allocated SBC | 5,556 | **5,829** | 14,015 | **17,704** |
| SBC as % of revenue | 4.37% | **4.07%** | 3.84% | **4.37%** |
| Unrecognized SBC (at 9/30/23) | — | — | — | **23,300** |

- SBC grew **+26% YoY** in 9M-2023, *faster than revenue*. Q3 SBC of $5,829M vs. Q3 net income of $9,879M — **SBC equals ~59% of GAAP net income in the quarter.**
- Absolute SBC of ~$17.7B (9M) vs. TTM GAAP net income of **$20.1B** — i.e., **stock compensation is roughly the same size as all trailing earnings.** This is the single most important quality-of-earnings flag in the report. Free cash flow is *not* SBC-adjusted, so headline FCF is overstated relative to a cash-comp equivalent by roughly $23-24B/yr.
- **Dilution:** shares outstanding rose from **10,242M (12/31/22) → 10,330M (9/30/23)**, +0.86% in nine months (~**1.15% annualized**). Share count issued rose from 10,757M to 10,845M. Modest but persistent.
- **$23.3B of unrecognized SBC** will be recognized over roughly the next four years — a pre-committed, non-discretionary expense headwind of ~$5-6B/year baked into future GAAP margins.

---

## 3. Balance Sheet — Fortress, With Leases as the Real Leverage

**Statement date: 2023-09-30** (earliest comparative column available is 2022-12-31; a meaningful caveat — the "prior period" is nine months prior, not one quarter).

| ($M) | 2022-12-31 | **2023-09-30** | Change | % |
|---|---:|---:|---:|---:|
| Cash & equivalents | 53,888 | **49,605** | (4,283) | −7.9% |
| AFS marketable debt securities (FV) | — | **49,871** | — | — |
| **Cash + securities** | — | **≈99,476** | — | — |
| Accounts receivable (net) | 42,360 | **43,420** | +1,060 | +2.5% |
| Inventory (net) | 34,405 | **35,406** | +1,001 | +2.9% |
| Total current assets | 146,791 | **142,995** | (3,796) | −2.6% |
| Total assets | 462,675 | **486,883** | +24,208 | **+5.2%** |
| Accounts payable | 79,600 | **72,004** | **(7,596)** | **−9.5%** |
| Accrued liabilities | 62,566 | **58,812** | (3,754) | −6.0% |
| Total current liabilities | 155,393 | **145,214** | (10,179) | −6.5% |
| Long-term debt (total) | 70,542 | **67,472** | (3,070) | −4.4% |
| — of which current | 2,999 | **5,995** | +2,996 | +99.9% |
| — of which noncurrent | 67,150 | **61,098** | (6,052) | −9.0% |
| **Finance lease liabilities** | 15,783 | **12,466** | (3,317) | −21.0% |
| **Operating lease liabilities** | 69,040 | **73,902** | +4,862 | **+7.0%** |
| Operating lease ROU asset | 66,123 | **70,758** | +4,635 | +7.0% |
| Deferred revenue (contract liab., curr.) | 13,227 | **14,398** | +1,171 | +8.9% |
| Shares outstanding (M) | 10,242 | **10,330** | +88 | +0.86% |

### 3.1 Liquidity — adequate, not lavish

- **Current ratio: 142,995 / 145,214 = 0.985x** (up from 0.945x at 12/31/22). Still marginally below 1.0 — Amazon has *never* run a conservative current ratio and relies on negative working-capital dynamics and $99.5B of liquid assets.
- **Cash + marketable securities of ~$99.5B** covers **all** funded debt ($67.5B) plus finance leases ($12.5B) with ~$19.5B left over. **On a funded-debt basis, Amazon is net cash by ~$19.5B** (79,938 − 99,476 = −19,538).
- **Lease-adjusted, it is net *debt*:** including operating leases, total obligations are **$153.8B** and net debt is **~+$54.4B**. Net debt/lease-adjusted EBITDA (TTM EBITDA ≈ $73.9B) is a comfortable **~0.7x**. **Leverage is not a solvency issue under any framing.**

### 3.2 The working-capital unwind is the most important balance-sheet signal

**Accounts payable fell $7.6B (−9.5%) and accrued liabilities fell $3.8B (−6.0%) in nine months** — a combined **~$11.3B cash outflow**. This is the reversal of the 2020–2022 pandemic-era payables stretch. Two implications:

1. **It is a headwind to reported operating cash flow** — meaning the +142% OCF growth in 9M-2023 (below) is *understated* in underlying quality. Amazon generated that growth **despite** an $11.3B working-capital drag.
2. **It is a warning as a comp.** Once payables stabilize, this drag disappears — but so does the "easy" optics of OCF growth driven by the base effect. Watch the DPO trend: at 9/30/23, AP of $72.0B against annualized COGS of ~$283B implies **~93 days payable**.

Inventory discipline is exemplary: inventory up only **+2.9%** YoY against revenue **+12.6%** — inventory days (COGS basis) of roughly **46 days**. Inventory valuation reserves were also *released* ($2.8B → $2.6B), confirming the 2022 overstock problem is fully resolved.

### 3.3 Debt management is disciplined — and a hidden earnings lever

- **No new long-term debt issued in 2023** (`ProceedsFromIssuanceOfLongTermDebt` = $0 for both 9M-23 and Q3-23).
- **$3,386M of long-term debt repaid** in 9M-2023, plus **$4,643M** in the TTM period.
- Short-term debt: $17,395M drawn vs. $19,339M repaid → **net −$1,944M**.
- **Finance lease principal payments of $3,605M** in 9M-2023; finance lease liabilities down **−21%** to $12.5B.
- The **+99.9% jump in current portion of LTD ($3.0B → $6.0B)** means ~$6.0B of debt matures within twelve months — easily covered by the $49.6B cash balance, but it explains part of the financing cash outflow.

**Rising lease discount rate:** the weighted-average operating lease discount rate rose from **2.8% (12/31/22) to 3.2% (9/30/23)**. This inflates the present value of lease liabilities and the associated interest accretion — a small but persistent P&L drag as legacy low-rate leases roll at higher rates.

---

## 4. Cash Flow — The Real Story of This Dataset

### 4.1 Operating cash flow

| ($M) | Q3-2022 | **Q3-2023** | 9M-2022 | **9M-2023** | TTM (to 9/30/23) |
|---|---:|---:|---:|---:|---:|
| **Operating cash flow** | 11,404 | **21,217** | 17,579 | **42,481** | **71,654** |
| YoY growth | — | **+86.1%** | — | **+141.7%** | — |
| Capex (productive assets) | 16,378 | **12,479** | 47,053 | **38,141** | **54,733** |
| **Free cash flow** | **(4,974)** | **+8,738** | **(29,474)** | **+4,340** | **+16,921** |
| D&A | 10,327 | **12,131** | 29,236 | **34,843** | **47,528** |
| Capex / D&A | 1.59x | **1.03x** | 1.61x | **1.09x** | **1.15x** |

**This is the dramatic inflection.** On a nine-month basis, free cash flow swung from **−$29.5B to +$4.3B — a +$33.8B improvement.** TTM FCF is now **+$16.9B** versus roughly **−$16.9B** for FY2022. Drivers in order of magnitude:

1. **Operating income +$14.1B** (9M-2023 vs. 9M-2022, $23.6B vs. $9.5B) — the margin story, converting ~1:1 into cash.
2. **Capex −$8.9B (−18.9%)** — 9M capex of $38.1B vs. $47.1B. Q3 capex of $12.5B was down **−23.8%** YoY.
3. **Capex/D&A has collapsed to ~1.03–1.09x** from 1.6x — Amazon has moved from *investing ahead of demand* to *harvesting* prior investment.

### 4.2 The critical caveat on FCF durability

**Capex/D&A of 1.03x is not a sustainable steady state for a company growing revenue double-digits and building AI/cloud capacity.** Management guided on the Q3-2023 call toward **re-accelerating capex in 2024** (AWS infrastructure and generative-AI compute). If FY2024 capex returns to the $60–65B range while D&A is ~$50B, TTM FCF of $16.9B **compresses meaningfully**. **The current FCF number should not be extrapolated — it is the product of a temporarily suppressed capex trough.**

### 4.3 Cash flow quality

Strong:
- OCF growth of +142% was achieved **despite** an ~$11.3B payables/accruals drag and a $10.4B increase in receivables/other operating assets (9M-2023: `IncreaseDecreaseInAccountsReceivableAndOtherOperatingAssets` = 10,364). Underlying cash generation is *better* than reported.
- D&A is genuine and rising ($47.5B TTM) — the asset base is real, not capitalized fluff.
- Deferred revenue grew $1,171M — customers prepaying (Prime/AWS) is a genuine quality signal.

Weak:
- **Deferred tax has been a recurring *benefit* rather than expense:** `DeferredIncomeTaxExpenseBenefit` was **−$4,412M in 9M-2023** and **−$7,779M in TTM**. Roughly half of cash taxes are being deferred via stock-comp-related deductions and bonus depreciation. **Cash taxes paid were only $6,982M in 9M-2023 against pre-tax income of $23,871M — a ~29% cash rate but with $7.0B of the accrual deferred.** When the SBC-driven deferred tax benefit normalizes, cash taxes rise and OCF falls. This is a structural, under-appreciated OCF headwind.
- **No buyback support:** `PaymentsForRepurchaseOfCommonStock` = **$0** in 2023 (and $0 in the TTM period). The last repurchase was $6.0B in 9M-2022. Amazon is returning **zero** capital while issuing ~1.15%/yr of stock — net *dilutive* to shareholders.

### 4.4 Financing & investing summary

| ($M) | 9M-2022 | **9M-2023** | TTM |
|---|---:|---:|---:|
| Operating cash flow | 17,579 | **42,481** | 71,654 |
| Investing cash flow | (26,780) | **(37,232)** | (48,053) |
| Financing cash flow | +9,632 | **(9,133)** | (9,047) |
| Net change in cash (incl. FX) | (1,299) | **(4,172)** | +14,903 |

Financing swung from **+$9.6B to −$9.1B** — Amazon has flipped from a borrower to a deleverager. That is a genuinely bullish signal on cash generation confidence.

---

## 5. Commitments & Off-Balance-Sheet Obligations

At 9/30/23, total `ContractualObligation` of **$284,407M**, with the near-term maturity ladder:

| Obligation ($M, at 9/30/23) | Amount |
|---|---:|
| Remainder of fiscal 2023 | 8,914 |
| **Due within next 12 months** | **35,712** |
| Due in year 2 | 28,429 |
| Due in year 3 | 23,789 |
| Due in year 4 | 26,581 |
| **Total contractual obligations** | **284,407** |

Operating lease payment schedule (undiscounted, total **$88,814M**): $3,245M remainder of FY23, $9,977M within 12 months, $9,390M yr-2, $8,678M yr-3, $7,879M yr-4. Finance lease payments total $14,574M ($2,178M within 12 months).

**Interpretation:** ~$35.7B due within twelve months against $99.5B of liquid assets and $71.7B TTM OCF — **comfortably serviceable**. The operating-lease ladder ($88.8B undiscounted, ~9.0x annual rent) is the largest single off-balance-sheet item and represents the fixed-cost base of the physical fulfillment network. **Note the tension: Amazon is simultaneously growing operating leases (+7% in nine months) while cutting capex (−19%).** That substitution — leasing instead of buying — flatters reported FCF, because operating lease payments sit in *operating* cash flow rather than capex. **Investors should treat ~$10.1B of TTM operating lease payments as economically equivalent to capex.** Doing so reduces TTM FCF from $16.9B to roughly **$6.8B** — a materially less impressive number, and the most honest way to view it.

---

## 6. Valuation Framing (with explicit assumptions)

The tools do not supply price or consensus data. Using a **reference share price of ~$154** (mid-January 2024 levels) and **~10,490M diluted shares**:

| Metric | Calculation | Result |
|---|---|---|
| Market cap | 10,490M × $154 | **~$1,615B** |
| TTM net income (tool-derived, 10/22–9/23) | — | **$20,079M** |
| TTM diluted EPS (approx.) | $1.89 (9M) + (~$0.03) Q4-22 | **~$1.86** |
| **P/E (TTM)** | — | **~83x** |
| TTM revenue | 404,824 + ~149,200 (Q4-22) | **~$554B** |
| **P/S** | — | **~2.9x** |
| TTM operating income | 23,643 − 9,511 + 12,248 (FY22) | **~$26.4B** |
| **EV / TTM operating income** | EV ≈ $1,596B (net cash adj.) | **~60x** |
| TTM EBITDA | 26,380 + 47,528 D&A | **~$73.9B** |
| **EV / EBITDA** | — | **~21.6x** |
| **EV / (EBITDA − capex)** | 73,908 − 54,733 = 19,175 | **~83x** |
| **P / TTM FCF** | 1,615 / 16.9 | **~95x** |
| **P / lease-adjusted TTM FCF** | FCF 16.9 − 10.1 opex lease | **~240x** |

**Verdict:** On *trailing* FCF, AMZN is extremely expensive (95x, or ~240x if you expense operating leases like capex). On *trailing* EBITDA it is merely rich (21.6x). **The entire bull case is a forward bet that operating margins hold above 7% and that FCF inflects toward $40–60B as capex growth normalizes against a growing D&A base.** The stock has already discounted a large portion of the Q3 margin surprise. There is **very little margin of safety** in trailing multiples, and **significant event risk** in the upcoming print.

---

## 7. Actionable Insights for Traders

**1. The margin recovery is the strongest, most defensible fundamental signal in this dataset.**
Operating margin expanded **+583bp YoY in Q3** (1.99% → 7.82%) and **+323bp for nine months**, driven by cost lines (marketing −4.2%, G&A −16.3% in Q3) rather than by accounting. **Action:** margin expansion, not revenue growth, is the correct lens for AMZN. Watch the cost-growth-vs-revenue-growth gap; at +5.9% vs. +12.6% it remains wide open.

**2. Free cash flow has inflected but is at a cyclical peak — do not extrapolate.**
TTM FCF of $16.9B vs. roughly −$16.9B a year earlier is a genuine transformation. But capex/D&A of **1.03x** is unsustainably low for a double-digit grower, and management has flagged 2024 capex re-acceleration. **Action:** treat $16.9B FCF as a ceiling, not a base. Lease-adjusted FCF is closer to **~$6.8B**. Position sizing should reflect a mid-single-digit-billion FCF base, not $17B.

**3. Haircut Q3 EPS by ~8–10% before annualizing.**
$1.2B of equity-securities mark-to-market gains (Rivian-type stakes) inflated Q3. Clean EPS is approximately **$0.85–0.86**, not $0.94. **Action:** if the market is anchoring to a $0.94 quarterly run-rate ($3.76 annualized → ~41x), it is over-extrapolating.

**4. SBC is the largest quality-of-earnings risk and is being ignored.**
SBC of **$17.7B (9M-2023, +26% YoY)** is roughly equal to **TTM GAAP net income of $20.1B**, plus **$23.3B of unrecognized SBC** queued up. Add back the ~$17.7B of SBC to income and AMZN's "true" cash earnings picture is far less impressive; subtract it from FCF and the $16.9B becomes negligible. **Action:** any FCF-based valuation must be SBC-adjusted, or it is systematically ~$23B/yr too optimistic.

**5. The working-capital unwind is a $11.3B cash drag that (a) proves OCF quality and (b) will create a difficult comp.**
Payables −$7.6B and accruals −$3.8B in nine months. **Action:** the +142% OCF growth is *understated* in underlying quality — good. But this drag is finite; once payables stabilize, OCF growth decelerates mechanically. Don't expect +142% repeats.

**6. Net interest has been neutralized — a durable, under-modeled 2024 EPS tailwind.**
Investment income of $2,048M (9M) vs. $544M prior year nearly offset interest expense of $2,469M. Q3 net interest was only **−$30M** vs. **−$340M** a year ago. With $99.5B of liquid assets earning market rates and gross debt falling, **net interest should turn positive in 2024**, adding roughly $1.5–2.0B of annual pre-tax income. **Action:** this is a low-risk earnings upgrade that consensus may underweight.

**7. The balance sheet supports both defense and offense.**
Net cash of ~$19.5B ex-leases; lease-adjusted net debt of ~$54B = **0.7x EBITDA**. Zero new long-term debt in 2023, $3.4B repaid, finance leases down 21%. **Action:** no financing risk; Amazon has capacity for buybacks, M&A, or an AWS/AI capex surge without stress. This caps downside.

**8. Zero buybacks + ~1.15% annual dilution = net shareholder dilution.**
No repurchases in 2023 (vs. $6.0B in 9M-2022). **Action:** management is signaling growth reinvestment over capital return. This is *fine* given 7.8% operating margins, but it means per-share metrics lag enterprise metrics.

**9. Insider signal: NOT AVAILABLE — treat as neutral, not bullish.**
The vendor has no authorized insider-transaction archive for AMZN at this date. **Action:** do not read absence of insider data as absence of insider selling. Amazon insiders (Bezos, Jassy) sell systematically via 10b5-1 plans; treat insider flow as an unknown in the risk model.

**10. The dominant near-term risk is a binary event within ~2 weeks.**
Q4-2023 results are expected early February 2024 (not yet in the dataset). Q4 is Amazon's **largest revenue and operating-income quarter** (holiday + AWS + advertising), and it is where **2024 capex guidance will be set**. **Action:** with P/E ~83x and P/FCF ~95x, positioning into the print is a **volatility trade, not a value trade**. A capex guide above ~$65B compresses the FCF narrative and would likely de-rate the stock regardless of a Q4 revenue beat. Consider defined-risk structures over outright long exposure.

**11. Structural/regulatory overhang is unpriced in the financials.**
The FTC's antitrust suit (filed September 2023) and the EU Digital Markets Act are live. These are **not** reflected anywhere in the Q3-2023 financial statements — no accrual, no disclosed contingency in the fact set. **Action:** treat as a tail risk to the marketplace/advertising margin engine, which is precisely where the margin expansion is coming from.

---

## 8. Key-Points Summary Table

| Category | Metric | Value | Signal |
|---|---|---:|---|
| **Data** | Latest filing | Q3-23 10-Q, accepted 2023-10-27 | ⚠️ Stale ~11 weeks; Q4-23 not yet reported |
| **Data** | New filings in past week | None | ⚠️ No new fundamental information |
| **Data** | Insider transactions | **Unavailable** | ⚠️ Information gap — do not infer |
| **Scale** | Q3-23 net sales (derived) | **$143.08B** (+12.6% YoY) | 🟢 Growth re-accelerating (9M: +11.0%) |
| **Scale** | TTM revenue (approx.) | ~$554B | 🟢 |
| **Margin** | Q3-23 gross margin | **47.6%** (+290bp YoY) | 🟢 Mix + cost discipline |
| **Margin** | Q3-23 operating margin | **7.82%** (+583bp YoY) | 🟢🟢 Core thesis |
| **Margin** | 9M-23 operating income | **$23.64B** (+149% YoY) | 🟢🟢 |
| **Margin** | 9M-23 cost growth vs. revenue | +7.3% vs. +11.0% | 🟢 ~370bp positive gap |
| **Earnings** | Q3-23 diluted EPS | $0.94 (clean ~$0.85–0.86) | 🟡 Inflated ~8–10% by $1.2B marks |
| **Earnings** | TTM net income | **$20.08B** | 🟢 vs. −$3.0B 9M-22 |
| **Cash flow** | 9M-23 operating cash flow | **$42.48B** (+142% YoY) | 🟢🟢 Despite $11.3B WC drag |
| **Cash flow** | TTM operating cash flow | **$71.65B** | 🟢 |
| **Cash flow** | TTM capex | **$54.73B** | 🟡 −19% YoY 9M; re-accel risk FY24 |
| **Cash flow** | **TTM free cash flow** | **+$16.92B** | 🟢 vs. ~−$16.9B FY22 |
| **Cash flow** | Lease-adjusted TTM FCF | **~$6.8B** | 🔴 Much weaker on honest accounting |
| **Cash flow** | Capex / D&A | 1.15x TTM (1.03x Q3) | 🔴 Unsustainably low |
| **Quality** | SBC (9M-23) | **$17.70B** (+26% YoY) | 🔴 ≈ TTM net income |
| **Quality** | Unrecognized SBC | **$23.3B** | 🔴 ~$5–6B/yr future expense |
| **Quality** | Deferred taxes (TTM benefit) | **−$7.78B** | 🔴 Structural OCF headwind ahead |
| **Quality** | Buybacks 2023 | **$0** | 🟡 Net dilution ~1.15%/yr |
| **Balance sheet** | Cash + securities | **~$99.48B** | 🟢 |
| **Balance sheet** | Total debt + finance leases | **$79.94B** (−$6.4B in 9M) | 🟢 Deleveraging |
| **Balance sheet** | Operating lease liabilities | **$73.90B** (+7.0%) | 🟡 Real leverage; substitutes for capex |
| **Balance sheet** | Net cash (ex-leases) | **~+$19.5B** | 🟢 |
| **Balance sheet** | Net debt (incl. leases) | ~+$54.4B (~0.7x EBITDA) | 🟢 Manageable |
| **Balance sheet** | Current ratio | **0.985x** (from 0.945x) | 🟡 Improving, still <1.0 |
| **Balance sheet** | Accounts payable | $72.00B (**−9.5%** in 9M) | 🟡 $7.6B cash drag; comp risk |
| **Balance sheet** | Inventory | $35.41B (+2.9%) | 🟢 Well-controlled vs. +12.6% rev |
| **Obligations** | Contractual obligations | **$284.4B** | 🟡 $35.7B due <12 months — coverable |
| **Interest** | Q3-23 net interest | **−$30M** (vs. −$340M) | 🟢 Near-neutral → positive in 2024 |
| **Valuation** | P/E (TTM, ref. ~$154) | **~83x** | 🔴 Priced for perfection |
| **Valuation** | EV / EBITDA (TTM) | ~21.6x | 🟡 Rich |
| **Valuation** | P / TTM FCF | **~95x** (lease-adj. ~240x) | 🔴 No margin of safety |
| **Event** | Next catalyst | Q4-23 + FY24 capex guide, ~early Feb 2024 | ⚠️ Binary, ~2 weeks out |
| **Event** | Regulators | FTC antitrust (Sep-23); EU DMA | 🔴 Unaccrued tail risk |

---

## 9. Synthesis & Stance

**The fundamental trajectory is unambiguously positive, and the data supports it with hard numbers**: a 583bp operating-margin expansion, operating income up 149% for nine months, free cash flow swinging +$33.8B year-over-year, disciplined capex, a fortress balance sheet, and net interest nearly neutralized. The 2022 "Amazon is broken" narrative is decisively refuted by this filing.

**But the quality of that improvement requires three specific haircuts**, and each one is material:
1. **$1.2B of investment marks** inflated Q3 net income — clean EPS is ~$0.85, not $0.94.
2. **$17.7B of SBC (9M)** is roughly equal to TTM net income — GAAP earnings and reported FCF both overstate distributable economics.
3. **TTM FCF of $16.9B becomes ~$6.8B** once ~$10.1B of operating-lease payments are treated as the capex substitutes they economically are, and capex/D&A of 1.03x is a trough that management has already signaled will rise.

**Net position:** the *direction* is right, the *level* of profitability and cash generation is being flattered at the margin, and the *valuation* (~83x P/E, ~95x FCF) embeds the bull case with no cushion. With Q4 results and 2024 capex guidance due within roughly two weeks, the fundamental data here argues for **constructive exposure over a 12–18 month horizon on a margin-recovery/FCF-scaling thesis, but against chasing the stock into a near-term binary event at these multiples**, and against using trailing FCF as the valuation anchor. The single most important number to watch next is **2024 capex guidance** — it, not Q4 revenue, determines whether the FCF inflection story survives.