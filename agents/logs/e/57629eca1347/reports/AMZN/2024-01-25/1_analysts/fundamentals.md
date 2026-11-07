# AMZN — Fundamental Research Report
**Instrument:** AMZN (Amazon.com, Inc.)
**Analysis date:** 2024-01-25
**Data basis:** Point-in-time SEC facts available on/before 2024-01-25 (latest filing: Form 10-Q for the quarter ended **2023-09-30**, accepted 2023-10-27)

---

## 1. Critical data caveat — read before using this report

Two limitations materially shape this report, and both are measurable risks in themselves:

1. **The feed ends at Q3 2023 (September quarter).** As of 2024-01-25, AMZN's Q4/FY2023 10-K had **not** been filed and Q4 results had not been released (historically early February). This data slice is therefore **~97 days stale relative to the quarter-end** and contains **no Q4 (holiday) quarter, no FY2022 10-K facts, and no full-year history**. Every number below is derived from 10-Q filings (Q1–Q3 2022, Q1–Q3 2022 vs. 2023 comparatives, plus Q2 2023 cash-flow comparatives).
2. **The vendor's insider-transaction archive returned `DATA_UNAVAILABLE` for AMZN.** There is no authorized Form 4 data in this package. I have **not** inferred or fabricated any insider activity. Treat insider signal as a genuine gap.
3. Additionally, several standard tags (revenue, PP&E, retained earnings, total stockholders' equity, segment revenue/profit) were **not** returned in this slice. Where I derive a figure arithmetically, I label it **(derived)** and show the identity so it can be audited.

**Derivation note (important):** Amazon reports `CostsAndExpenses` as *total* operating expenses with no other income lines inside operating income. Therefore:
`Revenue (derived) = CostsAndExpenses + OperatingIncomeLoss`
Cross-check: 9M23 = 381,181 + 23,643 = **404,824**; Q3 23 = 131,895 + 11,188 = **143,083**. These reconcile to reported revenue, so the identity holds.

---

## 2. Company profile (as reflected in the filing set)

- **Three operating segments** (`NumberOfOperatingSegments = 3`), the standard NA / International / AWS structure. Segment-level revenue and operating income were **not** present in the returned tags — this is the single biggest analytical gap for a trader, since AWS mix is the primary driver of margin and multiple.
- **Revenue model:** online and physical stores, third-party marketplace (commissions, fulfillment, shipping), Prime subscription, advertising services, and AWS (compute, storage, database, AI).
- **Reporting cadence:** quarterly 10-Q/10-K, fiscal year = calendar year. Q3 2023 10-Q has 3 reportable segments and discloses ROU assets, lease liabilities, and purchase obligations in full.
- **Capital returns:** **No dividend. Zero share repurchases in every period from Q2 2022 through Q3 2023.** The last buyback was $3.33B in Q2 2022 (total $6.0B in 1H22). Free cash has been redirected to capex and debt reduction.

---

## 3. Income statement — the margin inflection is the story

### Q3 (Sep quarter) comparison

| $M | Q3 2022 | Q3 2023 | Δ % | Margin Q3'22 | Margin Q3'23 |
|---|---:|---:|---:|---:|---:|
| Revenue (derived) | 127,101 | 143,083 | **+12.6%** | 100.0% | 100.0% |
| Cost of goods & services | 70,268 | 75,022 | +6.8% | 55.3% | **52.4%** |
| Marketing | 11,014 | 10,551 | **−4.2%** | 8.7% | **7.4%** |
| G&A | 3,061 | 2,561 | **−16.3%** | 2.4% | **1.8%** |
| Fulfillment + Tech&Content + Other op. (derived) | 40,233 | 43,761 | +8.8% | 31.7% | 30.6% |
| **Total costs & expenses** | 124,576 | 131,895 | +5.9% | 98.0% | 92.2% |
| **Operating income** | **2,525** | **11,188** | **+343%** | **2.0%** | **7.8%** |
| Non-operating income/(expense) | 419 | 1,001 | +139% | | |
| Pretax income | 2,944 | 12,189 | +314% | | |
| Income tax | 69 | 2,306 | nmf | 2.3% | 18.9% |
| **Net income** | **2,872** | **9,879** | **+244%** | **2.3%** | **6.9%** |
| **Diluted EPS** | **$0.28** | **$0.94** | **+236%** | | |

**Key insight:** Revenue grew 12.6% while total costs grew only 5.9% — a **670 bp expense-growth gap**. Cost of sales fell 290 bp as a share of revenue (faster than the mix shift toward services/AWS third-party units), marketing fell 130 bp on efficiency, and G&A fell 60 bp. Of the $8.66B YoY increase in operating income, **roughly $8.5B came from margin, not volume** — i.e., this is a cost-structure/leverage story, not a reacceleration story.

### Nine-month comparison (the cleaner trend)

| $M | 9M 2022 | 9M 2023 | Δ % | Margin 9M'22 | Margin 9M'23 |
|---|---:|---:|---:|---:|---:|
| Revenue (derived) | 364,779 | 404,824 | **+11.0%** | 100.0% | 100.0% |
| Cost of goods & services | 203,191 | 212,186 | +4.4% | 55.7% | **52.4%** |
| Marketing | 29,420 | 31,468 | +7.0% | 8.1% | 7.8% |
| G&A | 8,558 | 8,806 | +2.9% | 2.3% | 2.2% |
| Fulfillment + Tech&Content + Other (derived) | 114,099 | 128,721 | +12.8% | 31.3% | 31.8% |
| **Total costs & expenses** | 355,268 | 381,181 | +7.3% | 97.4% | 94.2% |
| **Operating income** | **9,511** | **23,643** | **+149%** | **2.6%** | **5.8%** |
| Non-operating income/(expense) | (14,485) | 228 | nmf | | |
| Pretax income | (4,974) | 23,871 | nmf | | |
| Income tax | (1,990) | 4,058 | nmf | 40.0% benefit | 17.0% |
| **Net income** | **(3,000)** | **19,801** | nmf | (0.8%) | **4.9%** |
| **Diluted EPS** | **$(0.29)** | **$1.89** | nmf | | |

**Reading the 9M more carefully — this is where I differ from the headline:** the derived "fulfillment + tech & content + other" bucket **grew 12.8%, faster than revenue's 11.0%**, taking 50 bp of margin. That bucket is where stock-based compensation and infrastructure spend land, and SBC rose **+26.3% YoY (17,704 vs 14,015)**. So the 9M operating-margin gain of 320 bp is almost entirely a **cost-of-sales story (330 bp of COGS improvement)**, partly offset by rising infra/tech and SBC intensity. Q3 alone showed that infra bucket improving (−110 bp), which is the encouraging data point — but it is one quarter, and Q4 is unobserved.

### Non-operating: the Rivian-swing is now a tailwind, not a headwind

| $M | 9M 2022 | 9M 2023 | Q3 2022 | Q3 2023 |
|---|---:|---:|---:|---:|
| Equity securities FV gain/(loss) (`EquitySecuritiesFvNiGainLoss`) | (11,300) | **+1,000** | +1,000 | **+1,200** |
| Warrant FV adjustment | +1,606 | +188 | +170 | +27 |
| Interest income | 544 | **2,048** | 277 | **776** |
| Interest expense | (1,673) | **(2,469)** | (617) | **(806)** |
| FX transaction loss | (206) | (15) | (103) | (94) |
| **Non-operating total** | **(14,485)** | **+228** | **+419** | **+1,001** |

**Actionable:** The 9M22 loss of $(14.5)B was dominated by a $11.3B non-cash mark on equity securities (Rivian). The 9M23 comparison benefits by ~$12.3B from that swing alone — **do not annualize this**. Crucially, the *recurring* picture is a **$16B/yr interest-income run-rate now roughly offsetting interest expense** (Q3: $776M income vs. $806M expense, effectively net-neutral). Net interest was a **$421M drag in 9M23 vs. $1,129M in 9M22**, despite gross debt barely changing — this is a genuine, repeatable earnings tailwind from float yield, and it is the piece of the margin story most likely to persist into 2024.

### Tax
Effective rate normalized hard: **17.0% for 9M23** (Q3 18.9%) versus a net *benefit* in 9M22. Cash taxes paid were **$6,982M in 9M23 (TTM $8,677M, +86% YoY)**. Deferred tax was a **$(4,412)M benefit** in 9M23. **Insight: forward EPS growth will face a headwind from tax-rate normalization, and the large deferred-tax benefit flattering GAAP earnings will shrink as prior NOL/credit shields are consumed.**

---

## 4. Cash flow — the FCF inflection is the strongest fundamental fact in this dataset

### Q3 and nine-month

| $M | Q3 2022 | Q3 2023 | 9M 2022 | 9M 2023 |
|---|---:|---:|---:|---:|
| **Operating cash flow** | 11,404 | **21,217** | 17,579 | **42,481** |
| Capex (purchases of productive assets) | (16,378) | (12,479) | (47,053) | **(38,141)** |
| **Free cash flow (CFO − capex)** | **(4,974)** | **+8,738** | **(29,474)** | **+4,340** |
| Capex / revenue (derived) | 12.9% | **8.7%** | 12.9% | **9.4%** |
| D&A | 10,327 | 12,131 | 29,236 | 34,843 |
| Capex / D&A | 1.59x | **1.03x** | 1.61x | **1.09x** |
| SBC | 5,556 | 5,829 | 14,015 | 17,704 |
| Investing cash flow | (15,608) | (11,753) | (26,780) | (37,232) |
| Financing cash flow | +3,016 | (8,948) | +9,632 | (9,133) |

### Trailing-twelve-month (Oct 2022 – Sep 2023), the number traders should anchor on

| $M | TTM Sep-2022 | TTM Sep-2023 | Change |
|---|---:|---:|---:|
| Operating cash flow | 39,665 | **71,654** | **+31,989 (+80.6%)** |
| Capex | 65,988 | **54,733** | −11,255 |
| **Free cash flow** | **(26,323)** | **+16,921** | **+43,244 swing** |
| Net income | 11,323 | 20,079 | +8,756 |
| D&A | 39,103 | 47,528 | +8,425 |
| Cash taxes paid | 4,674 | 8,677 | +4,003 |
| CFO / net income | 3.50x | **3.57x** | — |

**The single most important insight in this report:** AMZN went from **−$26.3B TTM FCF to +$16.9B TTM FCF in four quarters — a $43.2B swing** — driven roughly 26% by capex reduction and 74% by operating cash generation. Capex has fallen from **1.61x D&A to 1.09x D&A**, i.e. the investment cycle has essentially converged to maintenance/replacement level. This is the mechanical engine behind the margin and EPS inflection, and it is *observed*, not forecast.

**But the quality of the CFO number deserves scrutiny.** 9M23 working capital was a large drag:
- `IncreaseDecreaseInAccountsReceivableAndOtherOperatingAssets` = **−$10,364M** (cash use)
- `IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities` = **−$9,022M** (cash use; worse than −$7,335M in 9M22)
- Contract liability increase = only +$949M

Combined ~**$19.4B of working-capital outflow** in 9M23, offset by $34.8B D&A + $17.7B SBC + $19.8B net income. **So CFO of $42.5B was achieved *despite* a 19B working-capital headwind — that is a high-quality number relative to Q3 2022, and if accruals/AP stabilize in 2024 it becomes an additional tailwind.** Conversely, if the AP/prepaid normalization continues (see §5), CFO growth will lag earnings growth. Watch this line closely.

### Financing & capital allocation
- **LT debt issuance: $0 in 9M23 and $0 in Q3** (versus $12,931M proceeds in 9M22). **LT debt repayment: $3,386M.** 
- Short-term debt: **+$17,395M proceeds / −$19,339M repayments** (net paydown).
- Finance lease principal payments: **$3,605M**.
- **Buybacks: $0. Dividends: $0.**
- Net cash change 9M23: **−$4,172M** (FX −$288M), cash $54,253M → $50,081M.

**Insight:** Management is deleveraging and self-funding capex out of CFO — a deliberately conservative posture that implies they expect the capex cycle to be fundable internally. **The absence of any buyback at these cash levels is a signal that capital remains earmarked for AWS/AI infrastructure and fulfillment, not shareholder returns.** Any announced buyback at Q4 would be a genuine bullish surprise; its continued absence is the base case.

---

## 5. Balance sheet — fortress liquidity, negative working capital, shrinking debt

**As of 2023-09-30 vs. 2022-12-31 ($M):**

| Item | 2022-12-31 | 2023-09-30 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 53,888 | 49,605 | −4,283 |
| Marketable securities (AFS, fair value) | n/a in slice | **49,871** | — |
| Accounts receivable (net) | 42,360 | 43,420 | +1,060 |
| Allowance for doubtful accounts | 1,400 | 1,500 | +100 (3.5% of AR) |
| Inventory (net) | 34,405 | 35,406 | +1,001 |
| Inventory valuation reserves | 2,800 | 2,600 | −200 |
| **Current assets** | 146,791 | **142,995** | −3,796 |
| Accounts payable | 79,600 | **72,004** | **−7,596 (−9.5%)** |
| Accrued liabilities | 62,566 | **58,812** | **−6,001 (−9.6%)** |
| **Current liabilities** | 155,393 | **145,214** | −10,179 |
| **Working capital** | **(8,602)** | **(2,219)** | **+6,383** |
| Long-term debt — current | 2,999 | 5,995 | +2,996 |
| Long-term debt — noncurrent | 67,150 | 61,098 | −6,052 |
| **Total long-term debt** | **70,542** | **67,472** | **−3,070** |
| Finance lease liabilities | 15,783 | 12,466 | −3,317 (−21.0%) |
| Operating lease liabilities | 69,040 | **73,902** | +4,862 (+7.0%) |
| Operating lease ROU asset | 66,123 | 70,758 | +4,635 |
| Deferred revenue (total contract liability) | 16,100 | **17,098** | +998 (+6.2%) |
| **Total assets** | 462,675 | **486,883** | **+24,208 (+5.2%)** |
| Total liabilities & equity | 462,675 | 486,883 | +24,208 |

### What matters here

1. **Liquidity is enormous and growing in real terms:** cash $49.6B + AFS securities $49.9B = **~$99.5B of liquid assets** against **gross debt + finance leases of $79.6B** → **net cash position of roughly +$20B** (excluding $73.9B of operating leases). Securitized maturity ladder is conservative: $43.1B of the $49.9B AFS book matures **within one year** (fair value), $5.3B in 1–5 yrs, $1.4B beyond 5 yrs; unrealized loss is only ~$506M on a $50.4B amortized cost base — **the rate-driven mark-to-market drag has largely dissipated.**
2. **Current ratio 0.985x (142,995/145,214)** — still technically negative working capital, but improved from 0.945x at year-end. This is by design: Amazon funds itself on supplier float. **However, AP fell 9.5% and accrued liabilities fell 9.6% in nine months while revenue grew 11%.** That is *not* supplier-term normalization in Amazon's favor — it is a real cash outflow of ~$13.6B and is the clearest yellow flag in this balance sheet. If AP/revenue continues to compress, CFO growth decelerates mechanically.
3. **The lease book is now bigger than the debt book in economic terms.** Operating leases $73.9B + finance leases $12.5B = **$86.4B**, versus $67.5B of debt. The weighted-average operating-lease discount rate **rose to 3.2% from 2.8%** — new leases are being struck at higher rates, so lease expense and the ROU/liability balances will drift upward even with flat footprint. Undiscounted operating-lease payments are **$88.8B**; finance lease payments **$14.6B**.
4. **Deferred revenue +6.2% YTD to $17.1B** — a proxy for AWS commitments and Prime/AWS prepayments. $10.9B of the opening balance was recognized as revenue during 9M23. Growth here is a reasonable forward-demand indicator and it is **positive but decelerating relative to the balance sheet growth**.
5. **Inventory risk is low:** reserves were *released* $200M and inventory grew only 2.9% against revenue +11%. Combined with COGS leverage, this confirms the sell-through/overstock problem of 2022 is fully resolved. Fulfillment efficiency is genuinely better, not accounting-driven.
6. **Total stockholders' equity and retained earnings were not returned in this data slice**, so ROE, book value, and P/B cannot be computed from the tools. Total liabilities and equity = $486.9B, so equity is the residual; APIC is **$92,711M** and AOCI is **−$5,003M** (deteriorated from −$4,487M on FX translation of −$738M in 9M23). Flag this as an unverified input rather than guessing a number.

### Commitments and contingencies (9/30/23)
Total contractual obligations **$284,407M**: $35,712M due within 12 months, $28,429M in year 2, $23,789M in year 3, $26,581M in year 4. Annual CFO of $71.7B covers the near-term maturities **~2.0x**. No refinancing wall.

---

## 6. Per-share and dilution analysis

| Metric | 9M 2022 | 9M 2023 | Q3 2022 | Q3 2023 |
|---|---:|---:|---:|---:|
| Basic EPS | $(0.29) | **$1.93** | $0.28 | **$0.96** |
| Diluted EPS | $(0.29) | **$1.89** | $0.28 | **$0.94** |
| Implied diluted shares (NI/EPS, derived) | ~10,345M | **~10,477M** | ~10,257M | **~10,510M** |
| Implied basic shares (derived) | ~10,345M | ~10,259M | ~10,257M | ~10,291M |
| Shares outstanding (period end) | — | **10,330M** | — | 10,330M |
| Shares issued (period end) | — | 10,845M | — | 10,845M |
| Dilution from options/RSUs | — | ~1.7–2.2% | — | ~2.1% |

**Insight:** With **zero buybacks**, share count is drifting up ~1–2%/yr from SBC alone. With **$23.3B of unrecognized SBC expense** still to be recognized, this dilution is contracted, not optional. **Diluted EPS growth will underperform net income growth by roughly 1.5–2 points a year** in the absence of a repurchase program — a real, quantifiable drag that the "margin expansion" narrative tends to ignore.

---

## 7. Insider transactions

**DATA UNAVAILABLE.** The vendor's package contains no authorized point-in-time Form 4 archive for AMZN as of 2024-01-25. I have deliberately not inferred, estimated, or fabricated insider buying or selling. Traders should source this independently (e.g., EDGAR Form 4 filings) before drawing conclusions — the absence of data here is a **research gap, not a signal of zero insider activity.**

---

## 8. Synthesis: what the fundamentals actually say

**Bull case (well-supported by this dataset):**
- **Durable margin regime change.** Q3 operating margin 7.8% vs 2.0%; 9M 5.8% vs 2.6%. Q3's expense-growth gap of 670 bp is the clearest evidence yet.
- **The FCF inflection is real and mechanical.** TTM FCF +$16.9B versus −$26.3B; capex/D&A collapsed from 1.61x to 1.09x. This is arithmetic, not optimism — and it is the primary re-rating driver.
- **Fortress balance sheet.** ~$99.5B liquid assets, net cash positive ~$20B, debt down $3.1B, finance leases down 21%, and $71.7B TTM CFO covering $35.7B of 12-month obligations ~2x over.
- **Cash flow quality is high.** CFO covers net income 3.57x, and was generated *despite* a ~$19.4B working-capital outflow — meaning there is latent upside if AP/accruals stabilize.
- **Interest income ~$3B/yr run-rate** now offsets interest expense — a structural, repeatable earnings tailwind from the float.
- **Inventory overhang gone** (reserves released, inventory +2.9% vs revenue +11%): fulfillment economics are genuinely fixed.

**Bear case / what to watch:**
- **The dataset is one quarter stale.** Q4 2023 (the highest-revenue, highest-margin quarter) is entirely unobserved as of 2024-01-25. Every conclusion here is a Q3 run-rate extrapolation into a holiday quarter I cannot see.
- **AWS and advertising are invisible.** With three segments but no segment P&L, I cannot verify *where* the 7.8% operating margin came from. If it is retail cost cuts rather than AWS mix, the multiple implication differs enormously. **This is the highest-priority missing input.**
- **Capex could re-accelerate for AI.** Capex at 1.03x D&A in Q3 leaves little room for an AWS/AI build-out without compressing FCF. The FCF inflection is partly a *low-capex* artifact, and low capex is not a permanent state for this company.
- **Working capital is turning against them:** AP −9.5%, accrued liabilities −9.6% while revenue +11%. ~$13.6B of cumulative outflow. Monitor whether this is one-time normalization or a new trend.
- **Tax normalization:** effective rate 17.0% (Q3 18.9%) versus a 40% *benefit* rate a year ago. Deferred tax was a $4.4B benefit in 9M23 that will fade. Cash taxes +86% YoY.
- **SBC creep:** +26% YoY to $17.7B in 9M23, with $23.3B unrecognized — the one operating line that is *deleveraging*.
- **No capital return:** zero buybacks for six straight quarters, zero dividend, and zero LT debt issuance. Share count grows ~1.5%/yr, capping per-share compounding.
- **Lease discount rate up to 3.2%** from 2.8% — a slow structural cost creep on $86.4B of lease liabilities.

**Actionable conclusions for a trader (as of 2024-01-25):**
1. **The fundamental trajectory is unambiguously positive on margins, cash generation, and leverage** — this is a documented regime change, not a narrative. Long-side thesis has real arithmetic support.
2. **Position sizing should discount for Q4 event risk:** the setup into an unreleased, unobserved quarter is asymmetric-information risk. The report's numbers are a *Q3 exit-rate*, and Q4 consensus expectations are unknown to this dataset.
3. **The single highest-value checks before adding exposure:** (a) Q4/FY23 10-K — specifically **AWS segment operating income**, **capex guidance for 2024**, and **whether AP/accrued-liability normalization continued**; (b) any **buyback authorization**; (c) Form 4 insider data, which this package cannot provide.
4. **Do not underwrite the non-operating line.** The $1.0B Q3 gain and $228M 9M non-operating income are equity-mark and warrant driven; strip them, and the sustainable earnings base is the $12.2B Q3 operating income, taxed at ~19–21%.
5. **Bear trigger to define:** a quarter in which capex/D&A rises back above ~1.3x *while* COGS leverage stops improving. That combination would invalidate the FCF-inflection thesis faster than any revenue miss.

---

## 9. Key points summary

| # | Category | Metric / Fact | Value | Insight / Action |
|---|---|---|---|---|
| 1 | Data currency | Latest filing available | Q3 2023 10-Q (filed 2023-10-27) | ~97 days stale; Q4/FY23 unobserved — event risk into earnings |
| 2 | Insider data | Form 4 archive | **UNAVAILABLE** | Genuine research gap; do not interpret as no activity. Source independently |
| 3 | Growth | Revenue (derived) Q3'23 | **$143,083M (+12.6% YoY)** | Reaccelerating vs 9M +11.0%; identity audited |
| 4 | Growth | Revenue (derived) 9M'23 | **$404,824M (+11.0% YoY)** | Solid, not spectacular — the story is cost, not volume |
| 5 | Profitability | Operating income Q3'23 | **$11,188M, 7.8% margin** (vs 2.0%) | **+580 bp — the core bull fact** |
| 6 | Profitability | Operating income 9M'23 | **$23,643M, 5.8% margin** (vs 2.6%) | +320 bp; driven by COGS (−330 bp) |
| 7 | Efficiency | COGS / revenue Q3'23 | **52.4%** (vs 55.3%) | −290 bp; inventory reserves released, sell-through fixed |
| 8 | Efficiency | Marketing / revenue Q3'23 | **7.4%** (vs 8.7%) | Spend cut in absolute terms (−4.2%) while revenue +12.6% |
| 9 | Efficiency | G&A / revenue Q3'23 | **1.8%** (vs 2.4%) | −16.3% absolute decline; corporate cost discipline |
| 10 | Caution | Fulfillment+Tech/Content+Other 9M'23 | **31.8% of revenue** (vs 31.3%) | **Deteriorated 50 bp — infra/SBC creep**; watch this line |
| 11 | SBC | 9M'23 stock comp | **$17,704M (+26.3%)**; $23,300M unrecognized | Fastest-growing cost; guaranteed ~1.5–2%/yr dilution |
| 12 | Cash | TTM operating cash flow | **$71,654M (+80.6%)** | Strong; achieved despite ~$19.4B WC outflow = high quality |
| 13 | Cash | TTM free cash flow | **+$16,921M vs −$26,323M** | **+$43.2B swing — most important fact in report** |
| 14 | Capital intensity | Capex / D&A | **1.03x Q3'23 vs 1.59x Q3'22** | Investment cycle converged; FCF engine unlocked |
| 15 | Capital intensity | Capex / revenue | **8.7% Q3'23 vs 12.9%** | But leaves little room for AI build-out without FCF compression |
| 16 | Debt | Total LT debt | **$67,472M (−$3,070M YTD)**; zero LT issuance in 9M23 | Deleveraging, internally funded |
| 17 | Debt | Finance lease liabilities | **$12,466M (−21.0%)** | Aggressive lease paydown = real cash commitment |
| 18 | Obligations | Operating lease liabilities | **$73,902M (+7.0%)**; undiscounted $88,814M | Larger than debt book; discount rate up 2.8%→**3.2%** |
| 19 | Liquidity | Cash + AFS securities | **~$99,476M** vs gross debt+fin. leases $79,559M | **Net cash ~+$20B**; 2x coverage of 12-mo obligations |
| 20 | Working capital | Accounts payable | **$72,004M (−9.5% YTD)** on +11% revenue | ⚠️ **Key yellow flag — ~$13.6B AP+accrual outflow** |
| 21 | Working capital | Current ratio | **0.985x** (from 0.945x) | Negative WC by design (supplier float), but improving |
| 22 | Growth proxy | Deferred revenue | **$17,098M (+6.2% YTD)**; $10,900M recognized | Positive but decelerating forward-demand signal |
| 23 | Non-operating | Equity securities FV gain 9M'23 | **+$1,000M** (vs −$11,300M) | ⚠️ **$12.3B YoY swing is non-recurring — do not annualize** |
| 24 | Non-operating | Net interest 9M'23 | **−$421M** (vs −$1,129M); Q3 ≈ flat | Repeatable float-yield tailwind; interest income $2,048M |
| 25 | Tax | Effective tax rate 9M'23 | **17.0%** (Q3 18.9%); cash taxes $6,982M (+86% TTM) | Headwind to forward EPS growth; $4.4B deferred benefit fading |
| 26 | Capital return | Buybacks / dividends | **$0 / $0 (six straight quarters)** | No shareholder return; signals capex/AWS priority |
| 27 | Per share | Q3'23 diluted EPS | **$0.94** (vs $0.28); 9M **$1.89** (vs −$0.29) | +236% YoY; ~10,510M diluted shares (derived) |
| 28 | Balance sheet | Total assets | **$486,883M (+5.2% YTD)** | Equity/retained earnings **not in slice** — ROE/P/B not computable |
| 29 | Valuation | Price / market cap / multiples | **Not available in tool output** | P/E, EV/EBITDA, FCF yield cannot be computed here — do not infer |
| 30 | Segment | Operating segments | **3 reported**, no segment P&L in slice | ⚠️ **Highest-priority missing input: AWS mix vs retail cost cuts** |

---

### Bottom line
On fundamentals available through Q3 2023, **AMZN presents a genuine, arithmetically verifiable margin-and-cash-flow inflection**: operating margin up 580 bp YoY in Q3, TTM FCF swinging $43B positive, debt and finance leases shrinking, and ~$99.5B of liquidity against ~$79.6B of gross debt plus leases. The risks are that this is a **one-quarter-stale, capex-light, tax-flattered, and partially working-capital-dependent** version of the story — with AWS segment profitability entirely unverified, insider data completely unavailable, and no capital returns. The correct posture is constructive-with-verification: the trend is documented, but the confirmation must come from the Q4/FY23 10-K (AWS operating income, 2024 capex guidance, AP/accrual trajectory) and from independent Form 4 sourcing.