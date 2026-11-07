# AMZN — Comprehensive Fundamental Research Report
**As of:** 2026-07-20 | **Latest filed period:** Q1 2026 (quarter ended 2026-03-31), 10-Q accepted 2026-04-30 | **Latest annual:** FY2025 (10-K accepted 2026-02-06)
**Data basis:** Point-in-time SEC XBRL facts (only information publicly filed on or before 2026-07-20 is used). All figures USD.

---

## 1. Company Identification & Profile

- **Entity:** Amazon.com, Inc. (`AMZN`), SEC CIK 0001018724, filer accession prefix `0001018724-26-…`
- **Segment structure:** `NumberOfOperatingSegments = 3` — consistent with Amazon's **North America**, **International**, and **AWS** reporting segments.
- **Share structure:** $0.01 par common stock; 100bn shares authorized; **11,269M shares issued** and **10,754M outstanding** at 2026-03-31; **10,757,109,436 shares outstanding as of 2026-04-22** (10-Q cover). Amazon's reported "outstanding" excludes ~515M treasury shares.
- **Reporting cadence:** December fiscal year-end. Next scheduled catalyst: **Q2 2026 results (late July 2026)** — not yet in the data.

> **Data caveats (important for traders):** (a) `get_fundamentals` returned raw SEC fact tags rather than a pre-built profile, so no market price, market cap, or valuation multiples (P/E, EV/EBITDA) are available from this dataset — those must be layered in from a pricing source. (b) `get_insider_transactions` returned **DATA_UNAVAILABLE** — there is no authorized point-in-time insider archive for AMZN; **no insider buying/selling inference is made or should be made.**

---

## 2. Q1 2026 Income Statement — Acceleration on Both Lines

| Metric ($M) | Q1 2026 | Q1 2025 | YoY |
|---|---|---|---|
| Revenue | 181,519 | 155,667 | **+16.6%** |
| Cost of goods & services | 87,463 | 76,976 | +13.6% |
| **Gross profit** | **94,056** | **78,691** | **+19.5%** |
| Gross margin | **51.8%** | 50.6% | +126 bp |
| Total costs & expenses | 157,667 | 137,262 | +14.9% |
| **Operating income** | **23,852** | **18,405** | **+29.6%** |
| Operating margin | **13.1%** | 11.8% | +131 bp |
| Non-operating income | 15,982 | 3,274 | +388% |
| Pre-tax income | 39,834 | 21,679 | +83.7% |
| Income tax | 9,560 | 4,553 | — (24.0% vs 21.0% ETR) |
| **Net income** | **30,255** | **17,127** | **+76.7%** |
| **Diluted EPS** | **$2.78** | **$1.59** | **+74.8%** |
| Basic EPS | $2.82 | $1.62 | +74.1% |
| Diluted shares | ~10,883M | ~10,771M | +1.0% |

### ⚠️ The single most important earnings-quality point
**Roughly $12.3bn of Q1 2026 non-operating income is an unrealized mark-up on non-marketable equity securities**, disclosed as `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount = $12,328M` (vs just **$37M** in Q1 2025). Supporting evidence:
- `OtherNonoperatingIncomeExpense` = $15,647M (vs $2,749M) — the bulk of the non-operating swing.
- `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` on the balance sheet jumped **$16.2bn → $48.1bn** in one quarter.
- `DeferredIncomeTaxExpenseBenefit` exploded to **$12,798M** from $507M — a hallmark of book/tax timing on unrealized gains (cash taxes paid were only $1,323M).

**Stripping out the ~$12.3bn pre-tax gain (≈$9.4bn after tax, ≈$0.86/share), "core" Q1 2026 EPS ≈ $1.92 — still +21% YoY.** So the operating business genuinely accelerated; the headline +75% is roughly 45 points of mark-to-market, 21 points of real earnings growth at the tax-adjusted level, plus a mix/tax effect. Traders should not capitalize the $2.78 as run-rate.

### Underlying operating momentum (the clean signal)
- **Revenue +16.6%** is a clear re-acceleration versus the FY2025 total cost base growth of +11.9% (implying FY2025 revenue growth in the low-teens).
- **Depreciation rose +32.8% YoY ($18,945M vs $14,262M)** — the AI/data-center build is now a heavy P&L item, yet operating margin still *expanded* 131 bp to 13.1%. That is the highest-quality datapoint in the release: **revenue and gross margin are outrunning the depreciation drag.**
- Cost discipline: Marketing +5.6%, G&A **-1.6%** — opex growing far slower than revenue.
- SBC $4,032M (+9.3%), decelerating as a share of revenue (2.2%).
- Interest expense **$800M vs $541M (+48%)** — the cost of the new debt is starting to show; investment income $1,135M partly offsets.
- Revenue visibility: `ContractWithCustomerLiabilityCurrent` $20.9bn; **$9.4bn of Q1 revenue came from opening deferred balance** — AWS/Prime prepaid backlog is being consumed normally.

---

## 3. Balance Sheet — A Step-Change Quarter (the "AI balance sheet")

| $M | 2026-03-31 | 2025-12-31 | Δ |
|---|---|---|---|
| Cash & equivalents | **101,816** | 86,810 | +15,006 |
| Available-for-sale securities | 42,200 | 45,800 | -3,600 |
| Accounts receivable (net) | 75,532 | 67,729 | +7,803 |
| Inventory (net) | 36,534 | 38,325 | **-1,791** |
| Total current assets | 255,155 | 229,083 | +26,072 |
| Non-marketable equity securities | **48,100** | 16,200 | **+31,900** |
| Other non-current assets | 151,827 | 122,607 | +29,220 |
| Operating lease ROU asset | 88,741 | 86,054 | +2,687 |
| **Total assets** | **916,630** | **818,042** | **+98,588** |
| Current liabilities | 216,756 | 218,005 | -1,249 |
| Long-term debt (noncurrent) | **119,074** | 65,648 | **+53,426** |
| Finance lease liability | 13,325 | 12,286 | +1,039 |
| Operating lease liability | 91,617 | 89,252 | +2,365 |
| Other non-current liabilities | 48,072 | 35,985 | +12,087 |
| **Total liabilities** | **~474,716** | ~406,977 | +67,739 |
| **Shareholders' equity (derived)** | **~441,900** | ~411,065 | +30,835 |

**Key ratios (derived):**
- **Current ratio: 1.18x** (255.2 / 216.8) — comfortable.
- **Total debt incl. finance leases: ~$138.8bn** (119.1 + 2.8 current + 13.3 + ~2.8). **Debt/equity ≈ 0.31x** — leverage remains modest despite the jump.
- **Cash + AFS securities: ~$144.0bn vs gross debt ~$138.8bn → roughly net-neutral** (~+$5bn net cash) *before* $91.6bn of operating leases and $16.5bn of finance-lease undiscounted payments.
- **Book value ≈ $41/share**; **ROE (TTM net income $90.8bn / ending equity) ≈ 20.5%**; on average equity ≈ 21.3%.
- Inventory **declined** $1.8bn sequentially while revenue grew 16.6% YoY — very lean working capital, aided by inventory valuation reserves falling $3.3bn → $2.8bn.

### Two balance-sheet red flags to monitor
1. **$53.4bn of long-term debt issued in a single quarter** (proceeds tag confirms) with **zero long-term repayments** — LT debt up **+81% in three months**. Total debt maturities were $2.75bn (next 12m), $8.83bn (yr 2), $4.75bn (yr 3), $3.0bn (yr 4), $4.5bn (yr 5), **$45.0bn beyond year 5** as of 2025-12-31. The curve has been pushed long — rate-sensitive but no near-term refinancing wall.
2. **Non-marketable equity exposure tripled to $48.1bn** (16% of equity). This is now a material, hard-to-value asset on the books, and its mark-ups are flowing through EPS. A reversal quarter would create a visible headline hit.

---

## 4. Cash Flow & Capital Allocation — Free Cash Flow Has Effectively Gone to Zero

| $M | Q1 2026 | Q1 2025 | TTM (Apr'25–Mar'26) | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| Operating cash flow | 26,032 | 17,015 | **148,531** | 84,946 | 115,877 | 139,514 |
| Capex (productive assets) | **44,203** | 25,019 | **151,003** | 52,729 | 82,999 | **131,819** |
| **Free cash flow (OCF − capex)** | **(18,171)** | (8,004) | **~ (2,472)** | **+32,217** | **+32,878** | **+7,695** |
| Capex / OCF | 170% | 147% | **102%** | 62% | 72% | **94%** |
| D&A | 18,945 | 14,262 | 70,439 | — | — | — |
| Acquisitions (net of cash) | **15,408** | (48) | 19,297 | — | 3,680 | — |
| Long-term debt issued | **53,441** | 746 | 68,368 | 0 | 0 | 15,673 |
| Net financing cash flow | +52,767 | (47) | +62,475 | (15,879) | (11,812) | +9,661 |
| Net investing cash flow | (64,212) | (29,803) | (176,954) | (49,833) | (94,342) | (142,545) |

### The central fundamental story: reinvestment has consumed all of FCF
- **Capex growth: +57.4% (2024), +58.8% (2025), +76.7% YoY in Q1 2026.** Capex is now **2.14x depreciation** — the asset base is still being built far faster than it is being consumed.
- **FY2025 FCF collapsed 77% to $7.7bn; TTM FCF is approximately −$2.5bn.** This is the first genuinely negative trailing FCF print in the modern Amazon era and is the most important number for anyone modelling valuation off cash flow.
- The gap is being funded with debt: **Q1 2026 investing outflow of $64.2bn was covered by $52.8bn of net financing inflow.** Capital structure is shifting from internally funded to debt-funded growth.
- **`CapitalExpendituresIncurredButNotYetPaid` rose from $16.8bn (2024) to $27.0bn (2025)** — a further sign that even the reported capex number lags commitments.
- **Reported purchase/contractual obligations of $569.3bn at 2026-03-31** (with $57.1bn due within twelve months, $48.9bn in year 2, $40.4bn year 3, $38.6bn year 4, $46.5bn remainder-of-FY). Even allowing for the fact that this tag can include lease and take-or-pay categories, its scale versus a ~$144bn liquidity pool is the key structural risk in this report — it implies **multi-year committed spend well beyond the current capex run-rate**, and should be verified line-by-line against the 10-Q text.
- **Offsetting positive:** OCF quality is intact. TTM OCF $148.5bn exceeds TTM net income $90.8bn by $57.7bn, backed by $70.4bn D&A and $27.7bn other non-cash items. Cash taxes paid in Q1 2026 were only $1.3bn — operating cash conversion is genuinely strong; it is simply all being spent.
- **Q1 2026 acquisition outlay $15.4bn** with goodwill rising only $176M → the outlay was largely structured as an equity/convertible-style investment (consistent with the $48.1bn non-marketable equity bucket) rather than a consolidated acquisition. Watch for deal-specific disclosure next quarter.

**Multi-year capital-allocation history:** FY2023 → FY2025 saw OCF +64% ($84.9bn → $139.5bn) but capex **+150%** ($52.7bn → $131.8bn), i.e. reinvestment intensity rose faster than cash generation in every year. SBC has been **steadily declining**: $24.0bn (2023) → $22.0bn (2024) → $19.5bn (2025), a genuine positive for per-share value. Advertising expense: $20.3bn → $21.4bn → $23.5bn. Comprehensive income: $31.9bn → $62.3bn → **$105.9bn**, reflecting both earnings growth and the securities marks.

---

## 5. Lease & Off-Balance-Sheet Profile

- **Operating leases:** liability $91.6bn; undiscounted payments $110.1bn (next 12m $13.9bn, yr 2 $12.9bn, yr 3 $11.6bn, yr 4 $10.4bn); weighted-average discount rate **3.8%** (up from 3.7%).
- **Finance leases:** liability $13.3bn; undiscounted $16.5bn; discount rate **3.6%**. Q1 2026 finance-lease ROU amortization $733M, interest $102M.
- Combined lease + debt service is a real fixed-cost layer (~$15.8bn TTM operating lease payments + $1.6bn finance lease principal + interest) sitting under an operating margin that is still only 13.1%.

---

## 6. Insider Transactions

**Not available.** The insider-transactions data source explicitly returned `DATA_UNAVAILABLE: no authorized, point-in-time insider-transactions archive for AMZN by 2026-07-20`. **No conclusion about insider sentiment should be drawn, and no insider activity has been inferred or fabricated here.** This is a genuine information gap, not a "no activity" signal.

---

## 7. Actionable Insights for Traders

### Bull case (evidence-based)
1. **Revenue re-acceleration to +16.6% with 131 bp of operating-margin expansion *despite* depreciation +32.8%** — the operating leverage thesis is intact and better than feared.
2. **Gross margin broke above 51.8%**, +126 bp YoY, showing mix shift toward higher-margin services/AWS/advertising is still working.
3. **Working capital is exceptionally lean**: inventory down sequentially on double-digit revenue growth, inventory reserves falling.
4. **Balance sheet still investment-grade-comfortable**: 1.18x current ratio, ~0.31x debt/equity, liquidity ≈ gross debt, no maturity wall until 2031+.
5. **SBC declining for three straight years** ($24.0bn → $19.5bn) — genuine per-share earnings support.
6. **Backlog/deferred revenue $20.9bn** plus large multi-year commitments imply multi-year demand visibility.

### Bear case (evidence-based)
1. **TTM FCF ≈ −$2.5bn and FY2025 FCF down 77%.** Any valuation framework anchored on FCF yield must assume capex eventually normalizes — that is a narrative bet, not a reported fact.
2. **Earnings growth is materially non-operating.** ~$12.3bn of Q1 2026 pre-tax income was an unrealized mark on private equity stakes; ~$0.86 of the $2.78 EPS was non-cash mark-up. Core EPS ≈ $1.92. **Do not extrapolate the $2.78.**
3. **Debt-funded capex:** $53.4bn LT debt raised in one quarter; interest expense +48% YoY and rising with each tranche.
4. **$48.1bn of illiquid, hard-to-value equity exposure** (11% of assets, 16% of equity) whose marks now swing reported EPS both ways.
5. **$569bn of disclosed contractual/purchase obligations** vs ~$144bn liquidity — a genuine multi-year execution risk if AI demand timing slips.
6. **Effective tax rate stepping up** (24.0% vs 21.0%) — a headwind to EPS growth math.

### Concrete trading frameworks
- **Decompose the Q2 2026 print (due late July 2026):** the market will focus on (a) whether revenue growth holds ≥15%, (b) whether operating income grows ≥25% on an *operating* basis, and (c) whether capex guidance/cash capex is revised above the ~$151bn TTM run-rate. **A capex raise without a matching revenue raise is the highest-probability negative catalyst; a capex raise *with* AWS acceleration is the highest-probability positive one.**
- **Track the non-marketable equity line ($48.1bn) and the deferred tax line.** A quarter where `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount` is zero or negative will make headline EPS look abruptly weak even if operations are fine — position for headline volatility traps around that.
- **Watch TTM FCF crossing zero.** If Q2 2026 OCF growth (~+30% YoY pace) meets a flat capex number, FCF turns positive and the "capex is destroying FCF" narrative deflates quickly. That, in our reading, is the single largest re-rating lever available.
- **Interest expense trajectory:** at $800M/quarter and climbing with $53bn of new debt, expect ~$1bn+/quarter by year-end. Compute coverage: TTM operating income comfortably covers it (operating income alone dwarfs interest by >25x), so this is a margin-drag issue, not a solvency issue.
- **Flag for verification (not resolvable from this dataset):** the composition of the $569.3bn "contractual obligation" figure, the identity/terms of the $15.4bn Q1 2026 investment outlay, and the identity of the private-company stake driving the $12.3bn mark-up. These should be read in the 10-Q footnotes before sizing a position.

### Positioning summary
Fundamentally, AMZN is **operationally stronger than at any point in its history (record gross margin, record operating margin, 16.6% top-line growth) while simultaneously being at its weakest point in a decade on free cash flow.** That combination historically resolves favorably *if* the capex is demand-backed — and the revenue acceleration, $20.9bn deferred revenue, and $569bn of commitments all point in that direction. The trade is a **"trust the capex" trade**, and it carries no cash-flow cushion if AI demand timing slips. **Quality of earnings is the watch item, not quality of the franchise.**

---

## 8. Key Metrics Summary Table

| Category | Metric | Value | Period / As-of | Read |
|---|---|---|---|---|
| **Profile** | Ticker / Entity | `AMZN` / Amazon.com, Inc. | — | 3 reportable segments |
| | Shares outstanding | 10,754M (10,757.1M @ 4/22/26) | 2026-03-31 | +0.2% QoQ |
| **Growth** | Revenue | $181,519M | Q1 2026 | **+16.6% YoY** |
| | Gross profit | $94,056M | Q1 2026 | +19.5% YoY |
| | Operating income | $23,852M | Q1 2026 | **+29.6% YoY** |
| **Margins** | Gross margin | 51.8% | Q1 2026 | +126 bp YoY |
| | Operating margin | 13.1% | Q1 2026 | +131 bp YoY |
| | Net margin (reported) | 16.7% | Q1 2026 | inflated by marks |
| | Effective tax rate | 24.0% | Q1 2026 | vs 21.0% prior |
| **EPS** | Diluted EPS (reported) | $2.78 | Q1 2026 | +74.8% YoY |
| | Diluted EPS (ex equity marks) | **~$1.92 est.** | Q1 2026 | **+21% YoY — clean growth** |
| **Earnings quality** | Non-marketable equity mark-up | **$12,328M** | Q1 2026 | vs $37M prior year |
| | Deferred tax expense | $12,798M | Q1 2026 | vs $507M prior |
| | Cash taxes paid | $1,323M | Q1 2026 | low cash-tax regime |
| **Cash flow** | TTM operating cash flow | $148,531M | Apr'25–Mar'26 | +30% vs prior TTM |
| | TTM capex | **$151,003M** | Apr'25–Mar'26 | +62% vs prior TTM |
| | **TTM free cash flow** | **~ $(2,472)M** | Apr'25–Mar'26 | **negative** |
| | FY2025 FCF | +$7,695M | FY2025 | −77% YoY |
| | Capex / OCF | 102% | TTM | vs 72% FY2024 |
| **Balance sheet** | Total assets | $916,630M | 2026-03-31 | +$98.6bn in one quarter |
| | Cash + AFS securities | ~$144,016M | 2026-03-31 | — |
| | Total debt incl. finance leases | ~$138,800M | 2026-03-31 | +81% LT debt QoQ |
| | Current ratio | 1.18x | 2026-03-31 | healthy |
| | Debt / equity | ~0.31x | 2026-03-31 | modest leverage |
| | Shareholders' equity (derived) | ~$441,900M | 2026-03-31 | +$30.8bn QoQ |
| | Book value / share | ~$41 | 2026-03-31 | — |
| | Inventory | $36,534M | 2026-03-31 | **−$1,791M QoQ** |
| | Non-marketable equity securities | **$48,100M** | 2026-03-31 | 3.0x in one quarter |
| **Obligations** | Operating lease liability | $91,617M | 2026-03-31 | undiscounted $110,135M |
| | Finance lease liability | $13,325M | 2026-03-31 | undiscounted $16,496M |
| | Contractual/purchase obligations | **$569,280M** | 2026-03-31 | $57.1bn due <12m (verify in 10-Q) |
| **History** | OCF 2023 / 2024 / 2025 | 84,946 / 115,877 / 139,514 | FY | +64% over 2 yrs |
| | Capex 2023 / 2024 / 2025 | 52,729 / 82,999 / 131,819 | FY | **+150% over 2 yrs** |
| | SBC 2023 / 2024 / 2025 | 24,023 / 22,011 / 19,467 | FY | declining — positive |
| | Comprehensive income '23/'24/'25 | 31,872 / 62,254 / 105,934 | FY | — |
| **Gaps** | Insider transactions | **DATA UNAVAILABLE** | — | no authorized archive |
| | Price / valuation multiples | **NOT IN DATASET** | — | source externally |

**Bottom line:** AMZN's *operating* fundamentals are the best they have ever been — record gross margin (51.8%), record operating margin (13.1%), 16.6% revenue growth, lean inventory, and a fortress-grade (if newly leveraged) balance sheet. But *reported* EPS is flattered by a $12.3bn private-equity mark-up (core EPS ≈ $1.92, not $2.78), and *free cash flow is now negative* (~−$2.5bn TTM) as capex ($151bn TTM) exceeds operating cash flow. The franchise quality is not in question; the earnings *quality* and the capex *payback timeline* are.