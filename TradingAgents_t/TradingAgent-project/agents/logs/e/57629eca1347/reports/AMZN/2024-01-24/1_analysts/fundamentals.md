# AMZN — Fundamental Research Report
**Company:** Amazon.com, Inc. (NASDAQ: AMZN)
**Report date:** 2024-01-24 | **Latest financial period available:** Q3 FY2023 (quarter ended 2023-09-30)
**Data provenance:** Point-in-time SEC fact cache, filtered by EDGAR acceptance timestamp ≤ 2024-01-24. The only filings represented are AMZN's **Q3 FY2023 10-Q** (accn 0001018724-23-000018, accepted 2023-10-27 02:36 UTC) and the **Q2 FY2023 10-Q** (accn 0001018724-23-000012, accepted 2023-08-04). All figures in **USD millions** unless noted.

---

## 0. What the "past week" actually contains — read this first

| Item | Finding |
|---|---|
| New SEC filings in the trailing week (2024-01-17 → 2024-01-24) | **None in the data package.** Most recent acceptance stamped is 2023-10-27. |
| New fundamental information since last quarter | **None.** No pre-announcement, no 8-K, no guidance update. |
| Q4/FY2023 results | **Not yet filed** (expected early February 2024) — every number below is a pre-print position. |
| Insider transactions | **DATA_UNAVAILABLE.** The archive returned no authorized point-in-time Form 3/4/5 data for AMZN. I will not infer or fabricate insider activity. |
| Segment detail (North America / International / AWS) | **Not in the retrieved tag set.** Only `NumberOfOperatingSegments = 3` is present. No segment revenue or segment operating income. |
| Share price / market cap / consensus | **Not in the data package.** I therefore cannot compute P/E, EV/EBITDA, or price targets from tool output. |

**Implication for traders:** this is a "state of the franchise as of the September quarter, entering a binary earnings event in ~1–2 weeks" report. There is no fresh fundamental catalyst embedded in the past week's disclosure flow.

---

## 1. Company profile and business model (as reflected in the filings)

- **Identity confirmed:** Amazon.com, Inc., SEC CIK 0001018724, EIN/registrant files 10-Q with three reported operating segments (`NumberOfOperatingSegments = 3`): **North America retail, International retail, and AWS** (cloud infrastructure/platform). Segment-level P&L is not disclosed in the retrieved facts.
- **Fiscal year:** calendar year (Dec 31). Note: FY2022 contained 53 weeks vs 52 in FY2023 — a small (~2%) mechanical revenue headwind to FY2023 growth that should be discounted when annualizing.
- **Multiple revenue streams** implied by the cost structure: online and physical stores (COGS-dominant), third-party seller services & advertising (high-margin, appear in the ~30% "other operating" expense pool and in gross margin), subscription, and AWS.
- **Capital intensity:** TTM purchases of productive assets (PP&E) of **$54,733M** offset by TTM D&A of **$47,528M** → capex/D&A = **1.15x**, i.e. the asset base is still growing faster than it depreciates. This is the single most important swing factor in Amazon's free cash flow.
- **Shareholder returns:** **No dividend** (no dividend tags in the dataset). **Zero buybacks in Q1–Q3 2023** (`PaymentsForRepurchaseOfCommonStock = 0` in every 2023 period; $6,000M was executed in Q1 2022 and nothing since). Capital allocation remains reinvestment + deleveraging.
- **Share count:** 10,330M outstanding at 2023-09-30, up from 10,242M at 2022-12-31 (**+0.86% in nine months**), consistent with stock-comp-driven dilution rather than issuance or repurchase.

---

## 2. Income statement deep-dive

**Note on revenue:** the cache does not contain a `Revenues` tag. Revenue is **derived** as `OperatingIncomeLoss + CostsAndExpenses`, which is arithmetically exact on Amazon's P&L presentation.

### 2.1 Quarterly (Q3) comparison

| USD M | Q3 FY2023 | Q3 FY2022 | Δ y/y |
|---|---:|---:|---:|
| Revenue (derived) | **143,083** | **127,101** | **+12.6%** |
| Cost of goods & services | 75,022 | 70,268 | +6.8% |
| Gross profit | 68,061 | 56,833 | +19.8% |
| Gross margin | **47.6%** | **44.7%** | **+289 bp** |
| Marketing | 10,551 | 11,014 | −4.2% |
| G&A | 2,561 | 3,061 | −16.3% |
| Fulfillment + tech/content + other (implied residual) | 43,761 | 40,233 | +8.8% |
| Total costs & expenses | 131,895 | 124,576 | +5.9% |
| **Operating income** | **11,188** | **2,525** | **+343%** |
| Operating margin | **7.82%** | **1.99%** | **+583 bp** |
| Interest expense | 806 | 617 | +30.6% |
| Interest & investment income | 776 | 277 | +180% |
| Non-operating income (equity securities gains etc.) | 1,001 | 419 | +139% |
| Pre-tax income | 12,189 | 2,944 | +314% |
| Tax | 2,306 | 69 | n/m |
| Effective tax rate | 18.9% | 2.3% | +1,660 bp |
| **Net income** | **9,879** | **2,872** | **+244%** |
| Net margin | **6.90%** | **2.26%** | **+464 bp** |
| Diluted EPS | **$0.94** | **$0.28** | **+236%** |
| SBC | 5,829 | 5,556 | +4.9% |

**The margin bridge — where the 583 bp came from:**
1. **COGS leverage: +289 bp** (52.4% of revenue vs 55.3%). Mix shift toward third-party/services/advertising plus logistics cost discipline.
2. **The combined fulfillment/technology/content bucket: roughly +110 bp** — it grew only **8.8%** against **12.6%** revenue growth. This is the operating-leverage proof point: the largest cost pool is now growing slower than the top line.
3. **Marketing: +131 bp** (7.37% of revenue vs 8.67%) and **G&A: +62 bp** (1.79% vs 2.41%) — the 2022–23 headcount/cost reset showing up.
4. Offset: **D&A rose 8.48% of revenue vs 8.13%** (−35 bp) as the 2020–22 capex vintage depreciates.

### 2.2 Nine-month (year-to-date) comparison

| USD M | 9M FY2023 | 9M FY2022 | Δ y/y |
|---|---:|---:|---:|
| Revenue (derived) | **404,824** | **364,779** | **+11.0%** |
| COGS | 212,186 | 203,191 | +4.4% |
| Gross margin | 47.6% | 44.3% | +330 bp |
| Marketing | 31,468 | 29,420 | +7.0% |
| G&A | 8,806 | 8,558 | +2.9% |
| Implied other operating | 128,721 | 114,099 | +12.8% |
| Total costs & expenses | 381,181 | 355,268 | +7.3% |
| **Operating income** | **23,643** | **9,511** | **+149%** |
| Operating margin | **5.84%** | **2.61%** | **+323 bp** |
| Interest expense | 2,469 | 1,673 | +47.6% |
| Interest income | 2,048 | 544 | +276% |
| Non-operating income | 228 | (14,485) | n/m (2022 held $11.3B equity-securities losses, mostly Rivian) |
| Pre-tax income | 23,871 | (4,974) | n/m |
| Tax | 4,058 | (1,990) | n/m |
| Effective tax rate | **17.0%** | benefit | — |
| **Net income** | **19,801** | **(3,000)** | n/m |
| Net margin | **4.89%** | (0.82)% | +571 bp |
| Diluted EPS | **$1.89** | **$(0.29)** | n/m |
| SBC | 17,704 | 14,015 | +26.3% |
| D&A | 34,843 | 29,236 | +19.2% |

**Key observations:**

1. **The earnings inflection is structural, not a one-off.** 9M operating income more than doubled on only 11% revenue growth. There is no single non-recurring line inflating it — the gain is spread across COGS, fulfillment/tech, marketing and G&A. This is the cleanest read in the entire dataset.
2. **The tax rate normalization matters.** 9M23 effective rate of 17.0% (vs 21% statutory, helped by ~$600M of R&D credits) is now a *normal* rate after two years of distorted comparisons. Going forward, incremental pre-tax profit converts at ~83% — do not extrapolate the Q3'22 2.3% tax rate.
3. **Non-operating income has flipped from a liability to an asset.** 9M22 carried a **$(14,485)M** non-operating loss (equity securities −$11,300M, warrants +$1,606M). 9M23 is **+$228M**, and Q3'23 alone was **+$1,001M** (equity gains $1,196M, warrant adjustments $27M). The mark-to-market drag that crushed 2022 GAAP EPS is gone; but note this line is now a *source* of EPS that is non-operating and mark-to-market volatile — do not capitalize it.
4. **Net interest is at an inflection.** Q3'23: interest expense $806M vs interest income $776M — essentially neutral. 9M: $2,469M expense vs $2,048M income. The rising cost of the $80B debt stack is now almost fully offset by earnings on the ~$99B securities portfolio. Further rate hikes hurt less than they did in 2022.
5. **SBC is enormous relative to profit.** 9M23 SBC of **$17,704M equals 75% of 9M operating income ($23,643M)** and 4.4% of revenue. Unrecognized future SBC is **$23,300M**. Any "adjusted/EBITDA" framing must confront this: operating income is heavily stock-comp-funded, and it is why GAAP EPS ($1.89) lags basic-to-diluted share creep.
6. **Sequential momentum:** operating margin went 2.61% (9M22) → 5.84% (9M23), with Q3 alone at 7.82% — the **best quarterly operating margin in the dataset by a wide margin**. Trajectory is up and to the right.

---

## 3. Cash flow: the real story

| USD M | TTM (2022-10-01 → 2023-09-30) | 9M FY2023 | 9M FY2022 | Q3 FY2023 | Q3 FY2022 |
|---|---:|---:|---:|---:|---:|
| Net income | **20,079** | 19,801 | (3,000) | 9,879 | 2,872 |
| D&A | **47,528** | 34,843 | 29,236 | 12,131 | 10,327 |
| SBC | n/a | 17,704 | 14,015 | 5,829 | 5,556 |
| Deferred tax | (7,779) | (4,412) | (4,781) | (1,196) | (825) |
| WC: AR & other operating assets | (19,152) | (10,364) | (13,109) | (6,718) | (4,794) |
| WC: accrued liabilities | (3,245) | (9,022) | (7,335) | (1,321) | (20) |
| WC: deferred revenue | +1,454 | +949 | +1,711 | (25) | +54 |
| **Operating cash flow** | **71,654** | **42,481** | **17,579** | **21,217** | **11,404** |
| Purchases of PP&E | (54,733) | (38,141) | (47,053) | (12,479) | (16,378) |
| **Free cash flow (OCF − PP&E)** | **16,921** | **4,340** | **(29,474)** | **8,738** | **(4,974)** |
| FCF margin | **3.1%** | 1.1% | (8.1)% | 6.1% | (3.9)% |
| Investing cash flow | (48,053) | (37,232) | (26,780) | (11,753) | (15,608) |
| Financing cash flow | (9,047) | (9,133) | +9,632 | (8,948) | +3,016 |
| LT debt issued | 8,235 | **0** | 12,931 | **0** | 107 |
| LT debt repaid | (4,643) | (3,386) | (1) | 0 | 0 |
| Short-term debt proceeds | 28,002 | 17,395 | 30,946 | 216 | 12,338 |
| Short-term debt repaid | (35,136) | (19,339) | (21,757) | (8,095) | (7,916) |
| Buybacks | **0** | **0** | 6,000 | 0 | 0 |
| Operating lease payments | (10,052) | (7,687) | (6,268) | (2,692) | (1,813) |
| Finance lease principal | (5,245) | (3,605) | (6,301) | (1,005) | (1,465) |

**Read-through:**

- **The FCF inflection is dramatic and quantifiable: a +$46.4B swing in nine-month FCF ($(29,474)M → +$4,340) and a +$13.7B swing in Q3 alone.** TTM FCF is now **+$16,921M** positive versus deeply negative a year ago.
- **How much of that is earnings vs. capex restraint?** Roughly half and half. 9M OCF rose **+$24,902M** and 9M capex fell **+$8,912M**. So ~74% OCF, ~26% capex — but OCF itself is now earnings-driven (see next point).
- **Working capital is a headwind, not a tailwind — an important caution.** 9M23 working capital consumed roughly **$(18.4)B** (AR/other −$10.4B, accrued liabilities −$9.0B, partly offset by deferred revenue +$0.9B). Meanwhile 9M OCF of $42,481M vs. net income $19,801M + D&A $34,843M + SBC $17,704M + deferred tax $(4,412)M = $67,936M → a residual drag of ~$(25.5)B. **Translation: the OCF improvement is not financed by stuffing payables.** Accounts payable actually *fell* from $79,600M (Dec-22) to $72,004M (Sep-23), a ~$7.6B cash outflow. That is a sign of normalized supplier terms — healthy, but it means the "free float" tailwind is exhausted and OCF growth from here must come from actual profit.
- **Balance-sheet-funded cash flow is over.** 9M23 financing was **$(9,133)M** outflow vs **+$9,632M** inflow in 9M22. **No long-term debt was issued in 2023** (zero in Q1, Q2 and Q3), $3,386M was repaid, and short-term borrowings are being netted down (9M: $17,395M drawn vs $19,339M repaid). Amazon has switched from a debt-funded capex cycle to a self-funded one — the single most durable signal in this dataset.
- **Capex trajectory is the swing risk.** Q3'23 capex of $12,479M was the lowest quarterly figure in the dataset (vs $16,378M in Q3'22, and vs H1'23 average of ~$12,831M). Capex/revenue is down to **9.4% from 12.9%** in 9M22. **If capex reaccelerates for AI/datacenter buildout — which is the most plausible use of the improving FCF — the FCF ramp stalls even if operating margins hold.** Capex/D&A at 1.15x says depreciation will keep climbing regardless.
- **Cash-flow quality flag:** TTM FCF/Net income = **84%**, which is respectable only because net income is understated by heavy D&A; on an EBITDA basis, TTM EBITDA proxy (operating income $26,380M + D&A $47,528M) = **~$73,908M**, i.e. FCF conversion of ~23% of EBITDA. Amazon remains a *reinvestment machine*, not a cash-cow — yet.

---

## 4. Balance sheet: fortress liquidity, negative working capital, hidden lease leverage

| USD M | 2023-09-30 | 2022-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 49,605 | 53,888 | (4,283) |
| Marketable securities (AFS, fair value) | 49,871 | n/a in cache | — |
| **Cash + securities** | **~99,476** | n/a | — |
| Accounts receivable, net | 43,420 | 42,360 | +1,060 |
| Inventory, net | 35,406 | 34,405 | +1,001 |
| Total current assets | 142,995 | 146,791 | (3,796) |
| **Total assets** | **486,883** | **462,675** | **+24,208 (+5.2%)** |
| Accounts payable | 72,004 | 79,600 | **(7,596)** |
| Accrued liabilities | 58,812 | 62,566 | (3,754) |
| Total current liabilities | 145,214 | 155,393 | (10,179) |
| Long-term debt — current | 5,995 | 2,999 | +2,996 |
| Long-term debt — noncurrent | 61,098 | 67,150 | (6,052) |
| **Total long-term debt** | **67,472** | **70,542** | **(3,070)** |
| Finance lease liabilities | 12,466 | 15,783 | (3,317) |
| **Debt + finance leases** | **79,938** | **86,325** | **(6,387)** |
| Operating lease liabilities | 73,902 | 69,040 | **+4,862** |
| Deferred revenue (current + noncurrent) | 17,098 | 16,100 | +998 |
| Shares outstanding (M) | 10,330 | 10,242 | +88 |

**Liquidity & leverage metrics:**
- **Cash + securities / (debt + finance leases) = 99,476 / 79,938 = 1.24x → net cash of ~$19.5B.**
- Including operating lease liabilities (a genuine fixed obligation): net debt of **~$54.4B** against TTM EBITDA of ~$73.9B → **~0.7x**. Leverage is not a balance-sheet risk at this size.
- **Current ratio = 142,995 / 145,214 = 0.985.** Below 1.0 — structurally normal for Amazon (supplier-funded), but the direction matters: it improved from 0.944 at Dec-22, and working capital deficit narrowed from $(8,602)M to $(2,219)M.
- **Undiscounted operating lease commitments rose to $88,814M from $81,273M**, and the weighted-average discount rate rose to **3.2% from 2.8%**. Total contractual obligations are **$284,407M**, of which **$35,712M falls due in the next twelve months**. Rent is a growing, rate-sensitive fixed cost — a slow margin headwind to monitor.
- **Equity:** the total stockholders' equity line is **not present in the retrieved tag set**. Implied from assets less the tagged liabilities (current $145,214M + LT debt $61,098M + op-lease $65,810M + fin-lease $10,081M) leaves **~$204.7B before "other non-current liabilities,"** so actual equity is lower — approximately **$190B** is a reasonable estimate. I am flagging this as an estimate, not a reported figure. On that basis: **book value/share ≈ $18.4**, and **TTM ROE ≈ 10.6%**, **ROA ≈ 4.1%**, **asset turnover ≈ 1.17x**.
- **The equity build is stock-comp, not retained earnings.** Additional paid-in capital rose from $75,066M (Dec-22) to **$92,711M** (Sep-23) — **+$17,645M, essentially identical to 9M SBC of $17,704M.** Meanwhile AOCI worsened to $(5,003)M from $(4,487)M on FX translation (−$1,388M in Q3 alone). Read: absent the 4.4%-of-revenue stock comp, book value would be roughly flat despite $19.8B of net income, because of reinvestment-driven depreciation. This is the crux of the dilution argument.

---

## 5. Financial history at a glance (as available in the cache)

| Metric | 9M FY2022 | FY2022 (comparative) | 9M FY2023 | Trend |
|---|---:|---:|---:|---|
| Revenue | 364,779 | 513,983* | **404,824** | +11.0% y/y |
| Operating income | 9,511 | 12,248* | **23,643** | +149% |
| Operating margin | 2.61% | 2.38%* | **5.84%** | quadrupling off trough |
| Net income | (3,000) | (2,722)* | **19,801** | swing to record |
| Diluted EPS | (0.29) | (0.27)* | **1.89** | swing to record |
| OCF | 17,579 | 46,752* | **42,481** | +142% |
| Capex | 47,053 | 58,632* | **38,141** | −19% |
| FCF | (29,474) | (11,880)* | **4,340** | positive |
| SBC | 14,015 | n/a | **17,704** | +26% |
| Buybacks | 6,000 | 6,000 | **0** | paused |
| Total debt + fin. leases | n/a | 86,325 | **79,938** | −7.4% |

\* FY2022 totals are derived by adding the Q4-2022 stub ($= FY total − 9M) using the company's reported FY2022 figures; they sit outside the point-in-time cache and should be treated as comparative context only. **TTM (Oct-2022 → Sep-2023), computed entirely from in-cache 12-month rows:** net income **$20,079M**, OCF **$71,654M**, PP&E purchases **$54,733M**, D&A **$47,528M**, deferred tax **$(7,779)M**, AR/other operating assets **$(19,152)M**.

---

## 6. Insider transactions

**DATA_UNAVAILABLE.** The news/filing vendor returned: *"the B-project data package has no authorized, point-in-time insider-transactions archive for AMZN by 2024-01-24. Do not infer or fabricate insider activity."*

**Consequence for the trade:** no signal can be extracted on insider buying/selling, 10b5-1 plan activity, or executive conviction heading into the Q4 print. This removes one input from the sentiment/conviction framework. Note the structural context that *is* in the data: insider economics are dominated by equity grants (SBC 4.4% of revenue, $23.3B unrecognized), which mechanically generates sales-to-cover activity — but I have **no data** confirming any specific transaction and will not speculate.

---

## 7. Fundamental scorecard — what the evidence supports

**Bullish evidence (directly from filings):**
1. **Operating margin nearly tripled, then quadrupled:** 1.99% (Q3'22) → 7.82% (Q3'23); 2.61% → 5.84% YTD. Broad-based, no one-off line.
2. **FCF has definitively turned:** $(29.5)B → +$4.3B in nine months; TTM +$16.9B. Q3 standalone FCF of $8.7B vs $(5.0)B.
3. **Revenue re-accelerating gently:** +11.0% YTD, +12.6% in Q3 — with the 53rd week in the prior year acting as a mechanical drag.
4. **Deleveraging without dilution:** debt+finance leases down $6.4B, zero LT issuance in 2023, while net cash position is ~$19.5B.
5. **Cost discipline is visible in the P&L:** marketing −4.2% y/y and G&A −16.3% y/y in Q3 *while* revenue grew 12.6%.
6. **Capex discipline is the FCF lever:** capex/revenue 9.4% vs 12.9%; Q3 capex the lowest in the dataset.

**Bearish / cautionary evidence (also from filings):**
1. **Valuation is not in the dataset, but the earnings base is thin:** TTM diluted EPS ≈ **$1.92** (9M'23 $1.89 + derived Q4'22 ~$0.03). Any multiple applied to ~$1.92 of trailing earnings is high — the market is discounting the margin ramp continuing, not the trailing number.
2. **SBC = 75% of operating income.** "Adjusted" profitability is materially lower than GAAP; share count +0.86% in 9 months with zero buybacks.
3. **Working capital is now a $(18)B annualized drag** — payables fell $7.6B. The OCF tailwind of the 2020–22 era is gone.
4. **Capex floor:** capex/D&A at 1.15x means depreciation keeps rising; and any AI/datacenter capex cycle re-acceleration would compress FCF immediately.
5. **Operating lease liabilities up $4.9B to $73.9B, discount rate up 40 bp to 3.2%** — a rising fixed cost with $35.7B due within twelve months.
6. **Non-operating income ($1.0B in Q3) is mark-to-market and non-repeatable**; strip it and pre-tax income would have been $11,188M in Q3.
7. **FX is a persistent drag:** AOCI translation −$1,388M in Q3, −$738M YTD — international segment earnings are being eroded at the translation line.

---

## 8. Actionable takeaways for traders

**Stance the fundamentals support: constructive on the operating trajectory, neutral-to-cautious on the entry because of the pre-earnings binary and the trailing-earnings valuation.**

1. **The trade is a margin/FCF-inflection trade, not a growth trade.** +12.6% revenue is unremarkable; 7.82% operating margin is the event. Position sizing should reflect that the thesis breaks if operating margin rolls back below ~5%, not if growth slips to 9%.
2. **Q4/FY2023 results (early February) are the imminent binary.** The setup into the print is: (a) an extremely high bar created by Q3's 7.82% margin, (b) mechanical help from lapping 2022's Q4 impairment/severance charges (Q4'22 operating income was only ~$2.7B, so the y/y comp is easy), and (c) the first full disclosure of AWS and advertising segment economics since the cost reset. **A guide-down on operating margin, or a capex guide-up materially above the $54.7B TTM run-rate, is the bear case trigger.**
3. **Watch the capex line above all else.** It is worth ~$55B of annual FCF swing. Evidence of a datacenter/AI capex step-up inside an unchanged margin guide = margin pressure in 2024; a capex guide flat-to-down = FCF estimate revisions upward.
4. **Watch accounts payable and accrued liabilities.** 9M23 showed a $(16.6)B combined cash outflow. If AP stabilizes near $72B, OCF normalizes upward; continued AP contraction means the FCF beat was partly a one-time working-capital normalization.
5. **Do not underwrite a buyback.** $0 repurchased in three consecutive quarters. The existing authorization is effectively dormant. Capital return is not a catalyst here — debt reduction and reinvestment are.
6. **Treat the ~$1.0B/quarter non-operating gain as low-quality EPS.** For any "core earnings" model, use operating income net of SBC (9M23: $23,643M − $17,704M = **$5,939M** of operating income after stock comp), which is the honest, conservative earnings base. On that basis the stock is expensive — but so is every mega-cap platform; this is a *risk framing*, not a sell signal.
7. **Net interest is now neutral** (Q3 expense $806M vs income $776M). Rate cuts would be a small tailwind; the interest-rate sensitivity that dominated 2022–23 is over.
8. **Monitor the FX/OCI line.** $(1,388)M of translation loss in Q3 with AOCI at $(5.0)B — dollar strength is a quiet EPS drag that consensus often ignores.

---

## 9. Key data limitations (stated explicitly)

- No Q4 FY2023 / FY2023 full-year figures exist as of 2024-01-24; the newest period is the September quarter.
- The dataset contains **no `Revenues` tag** — revenue is derived as operating income + total costs and expenses.
- **No segment revenue or segment operating income** (AWS, advertising, North America, International) — the most important analytical layer for AMZN is missing.
- **No share price, market cap, or consensus estimates** → no P/E, P/S, EV/EBITDA, or target price can be computed from tool output. Any multiple cited elsewhere must come from a price feed outside this package.
- **No insider transaction data** — explicitly unavailable, not inferred.
- No FY2021 and earlier history, and no FY2022 10-K in the cache — the annual comparison table relies on derived Q4 stubs.
- Total stockholders' equity is not in the retrieved tags; the ~$190B figure is an estimate and is labelled as such wherever used.

---

## 10. Summary table — key fundamental points

| Category | Metric | Value (latest) | Comparator | Assessment |
|---|---|---|---|---|
| **Period** | Latest reported quarter | Q3 FY2023 (2023-09-30), 10-Q accepted 2023-10-27 | No new filing in trailing week | Pre-earnings, no fresh disclosure |
| **Growth** | Revenue Q3 | $143,083M | +12.6% y/y | Solid, mid-teens |
| **Growth** | Revenue 9M | $404,824M | +11.0% y/y | Steady; 53-week drag in base |
| **Profitability** | Q3 operating income | $11,188M (7.82% margin) | vs 1.99% in Q3'22 | **Major inflection — best in dataset** |
| **Profitability** | 9M operating income | $23,643M (5.84%) | vs 2.61% | +323 bp, broad-based |
| **Profitability** | Q3 net income / diluted EPS | $9,879M / $0.94 | vs $2,872M / $0.28 | +244% / +236% |
| **Profitability** | 9M net income / diluted EPS | $19,801M / $1.89 | vs $(3,000)M / $(0.29) | Swing to record; easy comparison base |
| **Quality** | SBC / operating income (9M) | $17,704M = **75%** | Unrecognized SBC $23,300M | Heavy stock-comp dependence |
| **Quality** | Effective tax rate (9M) | 17.0% | vs 2.3% in Q3'22 | Now normalized; +83% flow-through |
| **Cash flow** | TTM operating cash flow | $71,654M | vs $39,665M prior TTM | +81% |
| **Cash flow** | TTM free cash flow | **$16,921M** | vs negative a year ago | **Definitive turn positive** |
| **Cash flow** | 9M FCF | $4,340M | vs $(29,474)M | +$33.8B swing |
| **Cash flow** | Q3 FCF | $8,738M | vs $(4,974)M | +$13.7B swing |
| **Cash flow** | Working capital (9M) | ~$(18.4)B drag | AP fell $7.6B | Headwind — earnings-led, not float-led |
| **Investment** | TTM PP&E purchases | $54,733M (9.4% of 9M revenue) | vs 12.9% of revenue | Capex restraint is the FCF lever |
| **Investment** | Capex / D&A (TTM) | 1.15x | >1.0 | Asset base still expanding |
| **Balance sheet** | Cash + securities | ~$99,476M | — | Fortress liquidity |
| **Balance sheet** | Debt + finance leases | $79,938M | down from $86,325M | Deleveraging $6.4B |
| **Balance sheet** | Net cash (ex-op-leases) | ~+$19,538M | — | Net cash position restored |
| **Balance sheet** | Operating lease liabilities | $73,902M (undisc. $88,814M), rate 3.2% | up $4,862M | Rising fixed-cost/rate risk |
| **Balance sheet** | Current ratio | 0.985 | vs 0.944 at Dec-22 | Structurally <1, improving |
| **Capital return** | Buybacks 2023 YTD | **$0** | $6,000M in Q1'22 only | Dormant — no support |
| **Capital return** | Dividend | **None** | — | — |
| **Dilution** | Shares outstanding | 10,330M | +0.86% in 9 months | ~1.2% annualized dilution |
| **Insider** | Transactions | **DATA_UNAVAILABLE** | — | No signal obtainable; not inferred |
| **Valuation** | TTM diluted EPS | ~$1.92 | — | Price/multiple not in dataset |
| **Next catalyst** | Q4/FY2023 results | Early Feb 2024 (expected) | Easy y/y comp on Q4'22 charges | Binary event; watch margin guide + capex |
| **Bottom line** | — | **Operating margin + FCF inflection is real and broadening** | — | **Constructive fundamentals; valuation and pre-earnings timing are the constraints** |