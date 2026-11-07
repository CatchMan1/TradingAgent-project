# AMZN — Fundamental Deep Dive (point-in-time as of 2024‑01‑19)

**Company:** Amazon.com, Inc. (`AMZN`) — 3 reportable operating segments per XBRL (`NumberOfOperatingSegments` = 3: North America, International, AWS)
**Latest reported period in dataset:** Q3 FY2023, 10‑Q filed **2023‑10‑27** (`accn 0001018724-23-000018`). Q4/FY2023 had **not** been filed as of 2024‑01‑19 → no Q4 numbers are reflected anywhere below.

---

## 1. Data availability & methodology (read first)

- All figures are **SEC XBRL facts filtered by EDGAR acceptance timestamp ≤ 2024‑01‑19**. Nothing is forward‑looking or leaked.
- The extract returned is a **tag-level dump, truncated alphabetically**. Two consequences:
  - **Revenue tags (`RevenueFromContractWithCustomer…`) were cut off.** I therefore derive revenue from the accounting identity **Revenue = `CostsAndExpenses` + `OperatingIncomeLoss`**. This is validated: Q3'22 derives to **$127,101M** and Q3'23 to **$143,083M**, matching Amazon's reported quarterly revenue.
  - **Full-year FY2022 statements and retained-earnings tags were also cut off**, so no clean FY2022 income statement/equity line is available. TTM windows are used instead.
- No annual filing was used for 2023 (10‑K filed Feb 2024, after the analysis date).
- **Insider transactions: DATA UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for AMZN at 2024‑01‑19. I will not infer or fabricate insider activity — treat insider signal as *blank* for this analysis.
- Units: **USD millions** unless stated.

---

## 2. Income statement — the re-acceleration story

| Metric | Q3 FY22 | Q3 FY23 | YoY | 9M FY22 | 9M FY23 | YoY |
|---|---|---|---|---|---|---|
| Revenue (derived) | 127,101 | 143,083 | **+12.6%** | 364,779 | 404,824 | **+11.0%** |
| Cost of goods & services | 70,268 | 75,022 | +6.8% | 203,191 | 212,186 | +4.4% |
| Gross profit | 56,833 | 68,061 | +19.8% | 161,588 | 192,638 | +19.2% |
| **Gross margin** | **44.7%** | **47.6%** | +2.9 pt | **44.3%** | **47.6%** | **+3.3 pt** |
| Total costs & expenses | 124,576 | 131,895 | +5.9% | 355,268 | 381,181 | +7.3% |
| **Operating income** | **2,525** | **11,188** | **+343%** | **9,511** | **23,643** | **+149%** |
| **Operating margin** | **1.99%** | **7.82%** | +5.8 pt | **2.61%** | **5.84%** | **+3.2 pt** |
| Pre-tax income | 2,944 | 12,189 | +314% | (4,974) | 23,871 | n.m. |
| Income tax | 69 | 2,306 | — | (1,990) | 4,058 | — |
| **Net income** | **2,872** | **9,879** | **+244%** | **(3,000)** | **19,801** | n.m. |
| Diluted EPS | $0.28 | **$0.94** | +236% | $(0.29) | **$1.89** | n.m. |

**Derived TTM & Q4'22 bridges (all from tool data):**
- TTM (Oct'22–Sep'23) net income = **$20,079M** (tagged directly).
- Q4 FY22 net income = 20,079 − 19,801 = **+$278M** → **FY2022 net loss = −$2,722M**. So the entire FY22 loss came from the first nine months; Amazon returned to profit in Q4'22 and never looked back.
- H1 FY23 (Q1+Q2): revenue **$261,741M** (+10.1% vs H1'22 $237,678M), operating income **$12,455M** (~4.8% margin), net income **$9,922M**.

**The key structural insight — margin expansion is 100% gross-margin driven, not opex discipline:**
- Operating expense excluding COGS: 9M'23 $168,995M = **41.7% of revenue**; 9M'22 $152,077M = **41.7% of revenue**. **Exactly flat.**
- Therefore the entire +3.2pt operating-margin gain is explained by gross margin +3.3pt. Drivers visible in the tags: COGS growth (+4.4%) decelerating far below revenue growth (+11.0%).
- Marketing $31,468M (7.77% of rev) vs $29,420M (8.07%) — marketing leverage is mild.
- G&A $8,806M (2.18% of rev) vs $8,558M (2.35%).
- EBITDA (OI + D&A) 9M'23 = 23,643 + 34,843 = **$58,486M (14.4% margin)** vs 9M'22 $38,747M (10.6%).

**Non-operating / tax:**
- Non-operating income 9M'23 **+$228M** vs **−$14,485M** 9M'22 (which contained an **−$11,300M** FV hit on equity securities and −$11,528M marketable-securities unrealized loss). That swing alone is ~$14.7B of pre-tax improvement — a *non-operating, non-recurring* tailwind traders should strip out.
- Net interest is no longer a drag: 9M'23 interest expense $2,469M vs **investment income $2,048M** (net −$421M) vs 9M'22 net −$1,129M. Rising rates are now roughly neutral for AMZN's balance sheet.
- Effective tax rate 9M'23: **17.0%** (4,058/23,871); Q3'23: **18.9%**. Still below the 21% statutory rate — watch for normalization.
- Small negatives: asset impairments $420M, contract-termination loss $200M, FX losses $15M.
- **SBC remains enormous:** 9M'23 $17,704M (Q3 alone $5,829M), plus **$23,300M of unrecognized future SBC**. APIC rose $17.6B YTD; diluted shares 10,330.3M (10/18/23) vs 10,242M at 12/31/22 → ~0.9%/9mo dilution (~1.2% annualized).

---

## 3. Cash flow — the FCF inflection is the biggest fundamental change

| Metric | TTM Sep'22 | TTM Jun'23 | TTM Sep'23 | 9M FY22 | 9M FY23 |
|---|---|---|---|---|---|
| Operating cash flow | 39,665 | 61,841 | **71,654** | 17,579 | **42,481 (+142%)** |
| Capex (productive assets) | 65,988 | 58,632 | **54,733** | 47,053 | **38,141 (−18.9%)** |
| **Free cash flow** | **(26,323)** | **3,209** | **16,921** | **(29,474)** | **4,340** |

- **TTM FCF swung +$43.2B in four quarters** (−26.3B → +16.9B). That is the single most important number in this dataset.
- Q3 FY23 alone: OCF **$21,217M**, capex **$12,479M**, **FCF $8,738M (~6.1% FCF margin)**. Capex is now *below* D&A in the quarter (12,479 vs 12,131 — essentially converged): the 2021–22 fulfilment/warehouse over-build is finished.
- FCF conversion: TTM FCF / TTM net income = **84%** — unusually high quality, aided by D&A ($47,528M TTM) running near capex.
- **Cash flow headwinds worth flagging:** working capital subtracted heavily in 9M'23 — accrued liabilities/other −$9,022M, AR & other operating assets −$10,364M, and accounts payable fell **$7,596M** (79,600 → 72,004) while accrued liabilities fell $3,754M. Vendor-payables normalization is flattering the P&L but draining cash.

**Capital allocation (visible in tags):**
- **Zero share repurchases** in 2023 (0 in every 2023 period; the $6.0B authorization was exhausted in H1'22). **No dividend** in the data.
- Long-term debt: **no new LT issuance in 2023**; $3,386M repaid. Only short-term commercial paper is being rolled ($17,395M issued / $19,339M repaid 9M'23).
- Finance lease principal paid $3,605M (9M'23) — down from $6,301M (9M'22), consistent with lower lease intensity.
- Investing outflow −$37,232M (9M'23); marketable securities net purchases trivial ($1,053M bought / $4,059M matured).

---

## 4. Balance sheet — fortress liquidity, deleveraging, cheap on net-cash basis

| Item | 12/31/2022 | 9/30/2023 | Change |
|---|---|---|---|
| Cash & equivalents | 53,888 | 49,605 | −4,283 |
| Marketable securities (AFS, fair value, all maturities) | ~ | **49,871** | — |
| **Cash + securities** | ~ | **≈99,476** | — |
| Accounts receivable, net | 42,360 | 43,420 | +2.5% |
| Inventory, net | 34,405 | 35,406 | +2.9% |
| Total current assets | 146,791 | 142,995 | −2.6% |
| **Total assets** | **462,675** | **486,883** | **+5.2%** |
| Accounts payable | 79,600 | 72,004 | −9.5% |
| Accrued liabilities | 62,566 | 58,812 | −6.0% |
| Total current liabilities | 155,393 | 145,214 | −6.5% |
| Long-term debt (total) | 70,542 | 67,472 | −4.4% |
| — of which current | 2,999 | 5,995 | +100% |
| — of which noncurrent | 67,150 | 61,098 | −9.0% |
| Finance lease liabilities | 15,783 | 12,466 | −21.0% |
| **Total debt (bonds + finance leases)** | **86,325** | **79,938** | **−7.4%** |
| Operating lease liabilities | 69,040 | 73,902 | +7.0% |
| Operating lease ROU assets | 66,123 | 70,758 | +7.0% |

**Read-throughs:**
- **Current ratio 0.985** (142,995 / 145,214) — technically below 1.0, but Amazon's negative working-capital model plus $99.5B of liquid assets makes this a non-issue. **Net cash position = +$19.5B** (99,476 − 79,938). Even including all $73.9B of operating leases, net debt is only ~$54.4B — under 1x TTM EBITDA.
- **Debt down 7.4% while total assets grew 5.2%** → genuine deleveraging/self-funding, consistent with 2023's absence of new bond issuance.
- Lease mix is shifting *away* from finance leases (−21%) toward operating leases (+7%) — accounting, not economic, but it lowers reported interest expense.
- Inventory +2.9% and AR +2.5% on revenue growth of ~11% YTD → **inventory turns improving**, working capital discipline in the demand-planning chain.
- Share count outstanding 10,330.3M (10/18/2023); 108.45B shares authorized vs 10.845B issued → negligible anti-takeover/authorization overhang.

---

## 5. Off-balance-sheet & contractual obligations (a hidden call on FCF)

- **Total contractual obligations: $284,407M** at 9/30/2023.
- Operating lease payments (undiscounted): **$88,814M** — due remainder of FY23 $3,245M, year 1 $9,977M, year 2 $9,390M, year 3 $8,678M, year 4 $7,879M. Weighted-average discount rate **3.2%** (up from 2.8% at YE22).
- Finance lease payments: **$14,574M**.
- Next-twelve-month contractual obligations: **$35,712M**; due in second year $28,429M; third year $23,789M; fourth year $26,581M.
- Other commitments, remainder of FY23: $1,415M.
- **Interpretation:** ~$35.7B of near-term obligations vs $21.2B of quarterly OCF — comfortably covered ~2.4x over the next four quarters, but this is a structural fixed-cost base that caps how fast FCF can compound if growth slows.

---

## 6. Actionable conclusions for traders

**Bull case (well supported by the data):**
1. **Operating leverage is real and still early.** Gross margin +330bp in nine months with opex% frozen. If gross margin holds and marketing/G&A stay flat as a % of revenue, every incremental revenue point now drops at a high margin.
2. **FCF inflection, not just EPS.** TTM FCF $16.9B vs −$26.3B a year earlier. Capex has converged to D&A ($12.5B vs $12.1B in Q3) — the single best predictor that FCF continues to expand even without revenue acceleration.
3. **Balance sheet optionality.** Net cash $19.5B, no LT issuance in 2023, debt −7.4%, no buyback burn, no dividend. Capacity exists for either aggressive AI capex *or* a capital-return announcement — an un-priced optionality in the setup.
4. **Q3 FY23 EPS $0.94 / 9M $1.89** shows the run-rate is already far above FY22's −$2.72 loss. The market was still anchoring on FY22 when the 10‑Q was filed.

**Bear case / what to discount:**
1. **~$14.7B of the 9M'23 pre-tax improvement is non-operating** (equity-securities FV swing −11.3B → +1.0B, marketable-securities marks). Do not annualize the 149% operating-income growth without stripping this out. Core operating income 9M'23 = $23,643M is the honest number.
2. **Working capital is flattering then reversing.** AP −$7.6B and accrued liabilities −$3.8B in nine months. Payables normalization can only be drawn down once; if it continues, reported FCF (not OCF) will lag net income.
3. **Tax rate at 17.0% is below statutory** and Q3 already at 18.9%. A drift toward 21%+ is a ~4–5% EPS headwind with no operational offset.
4. **SBC of ~$23.6B annualized** (9M: $17.7B) plus $23.3B unrecognized = a persistent ~1.2%/yr dilution and a real economic cost that GAAP margins understate for a company that buys back nothing.
5. **Revenue growth decelerated** from +12.6% (Q3) to +10.1% (H1) — the quarterly cadence is 10–13%, not the 20%+ of 2021. Any multiple expansion must come from margin/FCF, not top line.
6. **Q4/FY2023 is not in the data.** Everything above is pre-holiday-quarter. The next disclosure is the binary event, and the dataset gives no guidance, no Q4 estimate, no AWS/AI capex commentary, and no segment revenue split (the extract exposes only the count of 3 segments, not their P&Ls).

**Concrete monitoring checklist (from tag-level evidence, not narrative):**
- `PaymentsToAcquireProductiveAssets` — does Q4 capex re-accelerate above the $12.5B/quarter run-rate (AI infrastructure)? A break above ~$15B/qtr is the key bear trigger for the FCF story.
- `CostOfGoodsAndServicesSold` growth vs revenue growth — the gross-margin engine. 9M COGS grew +4.4% vs revenue +11.0%; any convergence toward revenue growth kills the margin story.
- `AccountsPayableCurrent` and `AccruedLiabilitiesCurrent` — further declines mean FCF guidance risk.
- `IncomeTaxExpenseBenefit` / pre-tax income — effective rate creeping above 20%.
- `AllocatedShareBasedCompensationExpense` and `CommonStockSharesOutstanding` — dilution creep.
- `LongTermDebt` / absence of `ProceedsFromIssuanceOfLongTermDebt` — if Amazon returns to the bond market, it signals capex intensity beyond internal funding.
- `EquitySecuritiesFvNiGainLoss` — keep stripping this out of "earnings quality."

**Net stance implied by the fundamentals alone:** improving quality of earnings (gross-margin-led, FCF-backed, deleveraging, net-cash balance sheet) with decelerating-but-double-digit revenue. The data supports a **constructive fundamental view driven by margin/FCF compounding rather than revenue growth**, with the two material caveats being (a) $14.7B of non-operating noise in YTD pre-tax income and (b) the absence of any Q4 FY23 or segment-level data as of 2024‑01‑19.

---

## 7. Key points summary

| Category | Metric | Value | Read |
|---|---|---|---|
| Identity | Company / segments | Amazon.com, Inc.; 3 operating segments | NA, Intl, AWS |
| Data freshness | Latest filing | Q3 FY23 10‑Q, filed 2023‑10‑27 | No Q4/FY23 leak |
| Revenue | Q3 FY23 (derived) | $143,083M, +12.6% YoY | Re-acceleration vs H1 +10.1% |
| Revenue | 9M FY23 (derived) | $404,824M, +11.0% YoY | Double-digit, decelerating |
| Profitability | Q3 FY23 operating income | $11,188M (7.82% margin) vs 1.99% | +583bp YoY |
| Profitability | 9M FY23 operating income | $23,643M (5.84%) vs $9,511M (2.61%) | +323bp |
| Margin driver | Gross margin 9M'23 / 9M'22 | 47.6% vs 44.3% | Entire op-margin gain |
| Margin driver | Opex ex-COGS % of revenue | 41.7% vs 41.7% | Zero operating leverage |
| Earnings | Q3 FY23 net income / EPS | $9,879M / $0.94 | vs $2,872M / $0.28 |
| Earnings | 9M FY23 net income / EPS | $19,801M / $1.89 | vs −$3,000M / −$0.29 |
| Earnings quality | Non-op income 9M'23 vs 9M'22 | +$228M vs −$14,485M | ~$14.7B non-operating swing |
| Earnings quality | Effective tax rate 9M FY23 | 17.0% (Q3 18.9%) | Below statutory; normalization risk |
| Cash flow | TTM operating cash flow | $71,654M | vs $39,665M TTM Sep'22 |
| Cash flow | TTM capex | $54,733M (falling: 65,988→58,632→54,733) | Over-build complete |
| Cash flow | **TTM free cash flow** | **+$16,921M** vs −$26,323M | +$43.2B swing |
| Cash flow | Q3 FY23 FCF | $8,738M (6.1% margin) | Capex ≈ D&A |
| Cash flow | 9M FY23 working capital drag | AP −$7,596M; accrued −$3,754M | Recurring headwind |
| Balance sheet | Cash + securities | ≈$99,476M | Fortress |
| Balance sheet | Total debt (bonds + fin. leases) | $79,938M, −7.4% YTD | Deleveraging |
| Balance sheet | Net cash | ≈**+$19,538M** | Ex-operating leases |
| Balance sheet | Operating lease liabilities | $73,902M (+7.0%); ROU $70,758M | Growing fixed base |
| Balance sheet | Total assets | $486,883M (+5.2% YTD) | |
| Liquidity | Current ratio | 0.985 | Fine given $99.5B liquid |
| Obligations | Total contractual obligations | $284,407M; $35,712M due <12mo | Covered ~2.4x by annual OCF |
| Capital return | Buybacks / dividends | **$0 / $0** in 2023 | Full optionality retained |
| Debt issuance | LT bonds issued 2023 | $0; $3,386M repaid | Self-funding |
| Dilution | Shares out (10/18/23) | 10,330.3M vs 10,242M YE22 | ~0.9%/9mo |
| SBC | 9M FY23 / unrecognized | $17,704M / $23,300M | Persistent cost |
| Insider activity | — | **DATA UNAVAILABLE** | Not inferred |
| Key risk | Q4 FY23 + segment data | Absent at 2024‑01‑19 | Next print is binary catalyst |