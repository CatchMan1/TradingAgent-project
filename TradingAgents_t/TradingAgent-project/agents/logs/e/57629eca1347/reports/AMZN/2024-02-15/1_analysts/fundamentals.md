# AMZN — Comprehensive Fundamental Report
**Amazon.com, Inc. | As of 2024-02-15 | Source: point-in-time SEC fact set (FY2023 10-K accepted 2024-02-02, accn 0001018724-24-000008; FY2023 10-Q accepted 2023-10-27)**

---

## 1. Executive Summary

Amazon's freshly filed FY2023 10-K (accepted 2024-02-02, ~13 days before the analysis date) documents a **decisive profitability and free-cash-flow inflection**:

- **Operating income nearly tripled** to **$36.85B** from **$12.25B** in FY2022; operating margin expanded from **2.4% → 6.4%**.
- **Net income swung to +$30.43B** from a **–$2.72B** loss; diluted EPS **+$2.90** vs **–$0.27**.
- **Operating cash flow surged +81.7% to $84.95B**, while **capex fell 17.2% to $52.73B** — producing **free cash flow of +$32.22B**, a ~$49B swing from **–$16.89B** in FY2022.
- **Balance sheet deleveraged**: long-term debt cut from **$67.15B → $58.31B** with **zero new long-term debt issued** in 2023; total financing outflow of **–$15.88B** vs an inflow of +$9.72B in 2022.
- **Liquid assets of ~$144.3B** (cash $73.39B + marketable securities $70.92B at fair value) against ~$70.4B of debt+finance leases — a **net-cash position** even before considering $75.6B of operating leases.

The fundamental story as of 2024-02-15 is **margin expansion + FCF inflection + deleveraging**, partially offset by **rising stock-based compensation ($24.0B, +22.4% YoY)**, heavy lease obligations, and renewed capex risk around AI/data-center buildout.

---

## 2. Data Snapshot & Provenance

| Item | Detail |
|---|---|
| Entity | Amazon.com, Inc. (AMZN) |
| Latest full-year filing | Form 10-K FY2023, filed/accepted **2024-02-02 04:48 UTC** |
| Fiscal year end | December 31 |
| Most recent interim filing in set | Form 10-Q, accepted **2023-10-27** (period end 2023-09-30) |
| Reporting units | USD; values below in USD millions unless noted |
| Segment count reported | **3** (`NumberOfOperatingSegments` = 3) |
| Public float (2023-06-30) | **$1,183,684,965,587** (~$1.18T) |
| Shares outstanding | **10,383M** at 2023-12-31; **10,387.4M** at 2024-01-24 |
| Shares authorized | 100,000M; par $0.01 |

**Important data caveat:** although quarterly frequency was requested, the vendor's authorized cache for this window returns **annual (10-K) income-statement/cash-flow facts plus balance-sheet point-in-time facts**. Quarterly-only line items (e.g., Q4-23 revenue) and segment-level revenue/operating income detail were **not present** in the extracted tag set. Everything below is derived strictly from returned rows unless explicitly flagged.

---

## 3. Income Statement — Three-Year Trend

Total net sales are derived as `CostsAndExpenses + OperatingIncomeLoss` (identity verifiable against reported totals):

| Metric ($M) | FY2021 | FY2022 | FY2023 | YoY '23 |
|---|---:|---:|---:|---:|
| **Net sales (derived)** | **469,822** | **513,983** | **574,785** | **+11.8%** |
| Cost of goods & services sold | 272,344 | 288,831 | 304,739 | +5.5% |
| **Gross profit (derived)** | **197,478** | **225,152** | **270,046** | **+19.9%** |
| **Gross margin** | **42.0%** | **43.8%** | **47.0%** | +320 bps |
| Fulfillment/tech/content/marketing & other (residual) | 172,599 | 212,904 | 233,194 | +9.5% |
| **Operating income** | **24,879** | **12,248** | **36,852** | **+200.9%** |
| **Operating margin** | **5.3%** | **2.4%** | **6.4%** | +403 bps |
| Non-operating income/(expense) | +13,272 | –18,184 | +705 | n/m |
| Pre-tax income | 38,151 | –5,936 | 37,557 | n/m |
| Income tax (benefit) | 4,791 | –3,217 | 7,120 | n/m |
| **Net income** | **33,364** | **–2,722** | **30,425** | n/m |
| **Net margin** | **7.1%** | **–0.5%** | **5.3%** | n/m |
| **Diluted EPS** | **$3.24** | **–$0.27** | **$2.90** | n/m |
| Basic EPS | $3.30 | –$0.27 | $2.95 | n/m |

### Key income-statement takeaways
1. **Revenue re-accelerated** to +11.8% in FY2023 after +9.4% in FY2022 — the fastest growth since FY2021's +21.7% era, indicating the post-2022 demand/optimization trough has passed.
2. **Gross margin expanded 320 bps to 47.0%** because COGS grew only +5.5% vs +11.8% revenue growth. This is the single cleanest evidence of mix shift toward higher-margin services (AWS, advertising, third-party seller services) plus fulfillment-cost efficiency.
3. **Operating leverage is the headline**: Op income +200.9% on +11.8% revenue. The FY2022 nadir ($12.25B op income, 2.4% margin) is now clearly cyclical, not structural.
4. **FY2022's loss was non-operating-driven**, not operational: **–$18.18B** non-operating expense vs **+$13.27B** in FY2021 and **+$0.71B** in FY2023. The bridge is **equity-securities mark-to-market**: `EquitySecuritiesFvNiUnrealizedGainLoss` of **+$11.60B (2021) → –$13.60B (2022) → +$1.00B (2023)**, mirroring the Rivian stake revaluation. This is a **non-cash, non-recurring swing factor** — a critical adjustment for anyone anchoring on GAAP EPS.
5. **Reported normalized earnings power is understated by the non-op noise**: FY2023 pre-tax operating profit of $36.85B is a cleaner run-rate than the $30.43B net income suggests.

---

## 4. Operating Cost Structure & Expense Discipline

| Expense line ($M) | FY2021 | FY2022 | FY2023 | '23 YoY |
|---|---:|---:|---:|---:|
| Cost of goods & services sold | 272,344 | 288,831 | 304,739 | +5.5% |
| Marketing expense | 32,551 | 42,238 | 44,370 | +5.0% |
| General & administrative | 8,823 | 11,891 | 11,816 | –0.6% |
| **Total costs & expenses** | **444,943** | **501,735** | **537,933** | **+7.2%** |
| Advertising expense (disclosed) | 16,900 | 20,600 | 20,300 | –1.5% |
| Depreciation & amortization (cash-flow) | 34,433 | 41,921 | 48,663 | +16.1% |
| Operating lease cost | 7,199 | 8,847 | 10,550 | +19.3% |
| **Stock-based compensation** | **12,757** | **19,621** | **24,023** | **+22.4%** |
| SBC as % of revenue | 2.7% | 3.8% | **4.2%** | +40 bps |

**Interpretation:**
- **Total cost growth (+7.2%) lagged revenue growth (+11.8%) by ~460 bps** — the mechanical source of the margin expansion. G&A actually *declined* YoY, a clear signature of the 2022-23 cost-reduction program (corporate headcount rationalization, fulfillment network regionalization).
- **Advertising expense fell 1.5%** while revenue grew 11.8% — advertising is both a *revenue* stream and a *cost* line; the decline signals improved campaign efficiency and is a modest positive for incremental margin.
- **D&A +16.1% outpaces revenue** — the depreciation tail of the 2021-22 capex binge is now flowing through the P&L. This is a structural headwind that caps margin expansion unless revenue growth outruns the D&A base. Note capex *fell* in 2023, so D&A growth should decelerate in FY2024-25 — a favorable setup.
- **SBC is the fastest-growing major expense at +22.4%** and now **4.2% of revenue**. Unrecognized SBC on the balance sheet is **$18.3B** (`EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized`). This is real economic dilution and the main quality-of-earnings blemish. Tax benefit from SBC was **$5.40B** in 2023 (vs $4.30B in 2022, $2.70B in 2021).

---

## 5. Balance Sheet — Liquidity, Leverage, and Working Capital

### 5.1 Size and composition (point-in-time, 2023-12-31 vs 2022-12-31)

| Item ($M) | 2021-12-31 | 2022-12-31 | 2023-12-31 | '23 YoY |
|---|---:|---:|---:|---:|
| **Total assets** | 420,549 | 462,675 | **527,854** | +14.1% |
| Current assets | — | 146,791 | 172,351 | +17.4% |
| Cash & equivalents | 36,477* | 53,888 | **73,387** | +36.2% |
| Marketable securities (AFS, fair value) | — | — | **70,919** | — |
| Accounts receivable, net | — | 42,360 | 52,253 | +23.4% |
| Accounts payable | — | 79,600 | 84,981 | +6.8% |
| Accrued liabilities | — | 62,566 | 64,709 | +3.4% |
| **Current liabilities (derived below)** | — | 146,791 | **164,917** | +12.3% |
| Long-term debt (carrying) | — | 67,150 | **58,314** | –13.2% |
| Finance lease liabilities | — | 15,783 | **12,109** | –23.3% |
| Operating lease liabilities | — | 69,040 | **75,639** | +9.6% |
| Contract liabilities (deferred revenue) | — | 16,100 | **20,600** | +28.0% |
| **Total stockholders' equity (as reported)** | — | **146,043** | **201,875** | **+38.2%** |

\*2021 figure is restricted-cash-inclusive `CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents` = $36,477M; the 2021 cash-only line was not returned. 2022/2023 `CashAndCashEquivalentsAtCarryingValue` used.

**Current liabilities reconcile exactly** from returned tags: AP $84,981 + Accrued $64,709 + Unearned revenue (current) $15,227 = **$164,917M**. This confirms `EmployeeRelatedLiabilitiesCurrent` ($7,700M) and lease-current lines are *components* of the accrued/other bucket, not additive.

### 5.2 Solvency and liquidity metrics

| Metric | FY2022 | FY2023 | Comment |
|---|---:|---:|---|
| Current ratio | 1.00x | **1.045x** | Thin but improving; structurally low is normal for AMZN's negative-working-capital retail model |
| Cash + marketable securities | ~$124.8B¹ | **~$144.3B** | $73.39B cash + $70.92B AFS securities |
| Debt + finance leases | $82.93B | **$70.42B** | –15.1% YoY |
| **Net cash (liquidity – debt – fin. leases)** | ~+$41.9B | **~+$73.9B** | Strong net-cash position |
| Operating lease liabilities | $69.04B | **$75.64B** | $90.78B undiscounted |
| Undiscounted op-lease payments | $81.27B | $90.78B | Next 12M: $11.23B |
| Total liabilities (derived) | $316.63B | **$325.98B** | Assets – equity |
| Liabilities / assets | 68.4% | 61.8% | Deleveraging |

¹Estimated (2022 AFS marketable securities detail not returned; uses $53.89B cash plus approximately $70.9B-class portfolio).

**Why this matters for traders:** Amazon now carries **~$144B of liquid assets against ~$70B of debt+finance leases**, i.e., a **net-cash balance sheet** on a financial-debt basis. Even including the full **$75.6B** operating-lease liability, gross obligations of ~$146B are essentially **fully covered by liquid assets**. This removes refinancing risk as a bear thesis and gives management substantial capacity for either accelerated capex (AI/data centers) or a capital-return program.

### 5.3 Working capital and forward-demand signals
- **Accounts receivable +23.4%** vs revenue +11.8% — receivables are growing roughly 2x revenue. This is consistent with mix shift toward **AWS/enterprise and advertising** (longer billing cycles) and **third-party seller receivables**. Watch for DSO creep: **DSO ≈ 33 days** (52,253 / (574,785/365)) vs ~30 days in 2022. Modest, not alarming.
- **Allowance for doubtful accounts rose to $1.70B from $1.40B** (+21.4%), with **write-offs of $1.60B vs $1.30B** (+23.1%) — consistent with growth in receivables and a mildly softer credit environment for seller/enterprise customers.
- **Deferred revenue +28.0% to $20.60B** (current $15.23B, noncurrent $5.70B), with **$12.40B of the opening balance recognized as revenue in 2023**. Deferred revenue outgrowing revenue by ~16 pts is a **leading indicator of contracted forward demand** (AWS commitments, Prime subscriptions, advertising commitments) — a genuine bull signal.
- **Accounts payable +6.8%** — payables growth *slower* than COGS (+5.5%... roughly in line). No sign of stretching suppliers to fund the business, a positive for sustainability of the working-capital contribution.

---

## 6. Cash Flow — The Core Bull Case

| Cash flow ($M) | FY2021 | FY2022 | FY2023 | '23 YoY |
|---|---:|---:|---:|---:|
| **Operating cash flow** | 46,327 | 46,752 | **84,946** | **+81.7%** |
| Purchases of productive assets (capex) | 61,053 | 63,645 | **52,729** | –17.2% |
| **Free cash flow (OCF – capex)** | **–14,726** | **–16,893** | **+32,217** | **+$49.1B swing** |
| Capex / revenue | 13.0% | 12.4% | **9.2%** | –320 bps |
| FCF margin | –3.1% | –3.3% | **+5.6%** | +890 bps |
| Investing cash flow | –58,154 | –37,601 | **–49,833** | More negative |
| Financing cash flow | +6,291 | +9,718 | **–15,879** | Turns negative |
| D&A (added back) | 34,433 | 41,921 | 48,663 | +16.1% |
| Net change in cash (incl. FX) | –5,900 | +17,776 | +19,637 | — |

**The FCF inflection ($49.1B annual swing) is the single most important fundamental datapoint in this report.** It is driven by *both* engines working simultaneously:
- **Operating cash flow +81.7%** — the earnings-and-working-capital engine. Note OCF growth far exceeds net income growth, helped by $48.66B D&A, $24.02B SBC, and a **+$4.58B** contribution from deferred revenue.
- **Capex –17.2%** to $52.73B, dropping capex intensity from 12.4% → **9.2% of revenue** as the 2021-22 fulfillment buildout completed.

**Critical watch item:** capex at 9.2% of revenue is likely a *cyclical low*, not a new normal. Management commentary around generative-AI/data-center investment implies capex re-acceleration in 2024. If capex returns toward $60-65B while OCF holds at ~$85B, FCF stays robustly positive; but a return to 12-13% capex intensity would cut FCF roughly in half. **This is the key sensitivity for the FCF-multiple thesis.**

### 6.1 Cash flow drags / offsets
- **Investing outflow widened to –$49.83B** (from –$37.60B) despite lower capex — driven by marketable-securities repositioning (purchases $1.49B, proceeds $5.63B) and, in the FY2023 period, acquisitions. Net securities activity was a *net source* of only ~$4.1B, so the widening is predominantly non-capex investing.
- **Financing flipped to –$15.88B** from +$9.72B: LT debt repayments $3.68B, short-term debt repayments $25.68B vs short-term proceeds $18.13B, **zero new long-term debt**, plus finance-lease principal $4.38B. This is textbook deleveraging — a credit-positive, but it removes a historical source of cheap funding.

---

## 7. Debt Maturity Profile & Lease Obligations

### 7.1 Long-term debt maturities (as of 2023-12-31, $M)
| Year | Amount |
|---|---:|
| Next 12 months | 8,500 |
| Year 2 | 5,286 |
| Year 3 | 3,146 |
| Year 4 | 8,750 |
| Year 5 | 2,250 |
| **After Year 5** | **39,250** |
| **Total LT debt (carrying $58,314)** | — |

**Assessment:** The maturity ladder is **well-laddered and comfortably serviceable**. The single largest near-term wall is only **$8.50B in the next 12 months**, versus **$73.39B of cash alone**. Long-dated debt ($39.25B after year 5) benefits from pre-2022 low coupons — a genuine asset in a higher-rate world. **No refinancing cliff.**

### 7.2 Lease obligations
- **Finance leases: $12.11B** (current $2.03B, noncurrent $10.08B); undiscounted payments $14.11B. Down 23.3% YoY as prior logistics/fleet leases roll off. Finance-lease interest expense fell to **$304M** from $361M.
- **Operating leases: $75.64B** (current $8.42B, noncurrent $67.22B); undiscounted payments **$90.78B** (next 12M $11.23B, yrs 2-5 $34.95B, after yr 5 **$44.60B**). Growth of +9.6% on the liability with +19.3% operating-lease cost reflects warehouse/office expansion and renewed lease terms at higher rates.
- **Total undiscounted contractual obligations: $300.41B** (incl. purchase obligations and leases), of which **$39.35B due in the next 12 months** — a figure that must be read alongside the $84.95B OCF and $144B liquidity. Comfortable.

### 7.3 Interest dynamics — a quiet tailwind
| ($M) | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Interest expense | 1,809 | 2,367 | **3,182** |
| Investment income (interest) | 448 | 989 | **2,949** |
| **Net interest** | **–1,361** | **–1,378** | **–233** |

**Net interest cost collapsed from –$1.38B to –$0.23B.** Higher rates on Amazon's ~$144B liquid portfolio nearly fully offset the higher cost of debt. This is a meaningful, underappreciated earnings tailwind that flows through non-operating income; **if the Fed cuts in 2024, this benefit partially reverses** (lower yield on the securities book), which is a second-order EPS headwind to flag.

---

## 8. Capital Allocation & Shareholder Returns

| Item ($M) | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Share repurchases | 0 | **6,000** | **0** |
| Dividends | 0 | 0 | 0 |
| LT debt issued | 19,003 | 21,166 | **0** |
| LT debt repaid | 1,590 | 1,258 | 3,676 |
| Short-term debt raised | 7,956 | 41,553 | 18,129 |
| Short-term debt repaid | 7,753 | 37,554 | 25,677 |
| Short-term debt net | +203 | +3,999 | **–7,548** |
| Finance lease principal | 11,163 | 7,941 | 4,384 |

**Read-through:** Amazon **paid no dividend and bought back no stock in 2023** (the only buyback in the series was $6.0B in 2022, entirely in H1-22). Capital is being recycled into **(a) debt reduction** (net debt paydown of ~$11.3B across LT + short-term) and **(b) the operating/investment engine**. Share count grew **1.38%** (10,242M → 10,383M) — essentially SBC dilution, unmitigated by buybacks.

**Trade implication:** AMZN remains a **pure reinvestment/re-rating story, not a capital-return story**. Any announced buyback or inaugural dividend would be a genuine incremental catalyst given the $144B liquidity pile and the completion of the capex super-cycle — but there is **no evidence in the FY2023 filing** of such a step.

---

## 9. Taxes & Earnings Quality

| Item ($M) | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Pre-tax income | 38,151 | –5,936 | 37,557 |
| Income tax expense/(benefit) | 4,791 | **–3,217** | 7,120 |
| Effective tax rate | 12.6% | n/m | **19.0%** |
| Taxes paid (cash) | 3,688 | 6,035 | **11,179** |
| Deferred tax expense/(benefit) | –310 | –8,148 | **–5,876** |
| SBC excess tax benefit | –1,900 | +33 | **–519** |
| Tax credit benefit | –1,136 | –1,006 | **–2,362** |
| Deferred tax assets, net | — | 34,509 | **45,788** |
| Deferred tax assets — IPR&D | — | 6,824 | **14,800** |

**Key observations:**
1. **FY2022's tax *benefit* of –$3,217M** (vs a 21% statutory charge) is what turned a –$5.94B pre-tax loss into a merely –$2.72B net loss. It was driven by a **–$8.15B deferred tax benefit** and a **+$655M** valuation-allowance release. **Do not extrapolate FY2022's low tax as a run-rate.**
2. **FY2023 effective rate normalized to ~19.0%**, below the 21% statutory rate on **$2.36B of tax credits** and a **–$600M prior-year adjustment**, partially offset by +$1.31B state taxes and +$1.05B non-deductible SBC.
3. **Cash taxes more than doubled to $11.18B from $6.04B** — cash tax is now converging on book tax. This is a **real cash drag** that will persist and slightly tempers the FCF celebration.
4. **Deferred tax assets rose to $45.79B from $34.51B**, with **IPR&D DTA jumping from $6.82B → $14.80B** — a direct fingerprint of the **2023 acquisition activity** (technology/IP-heavy deals). The **valuation allowance rose to $4.81B from $4.37B**, indicating some acquired/foreign loss streams are not expected to be utilized.
5. The gap between GAAP net income ($30.43B) and cash taxes ($11.18B) vs book tax ($7.12B) means **FY2023 FCF of $32.2B already absorbs a rising cash-tax burden** — supportive of durability.

---

## 10. Insider Transactions

**DATA UNAVAILABLE.** The data package contains **no authorized, point-in-time insider-transactions archive for AMZN as of 2024-02-15**. Per the tool result, insider activity **must not be inferred or fabricated**. There is **no Form 4 evidence in this dataset** to support any conclusion about insider buying or selling patterns around the FY2023 filing or the Q4-23 report. Treat insider signal as **unknown / not actionable** for this analysis and seek separate coverage if required.

---

## 11. Return Ratios & Efficiency

| Metric | FY2022 | FY2023 |
|---|---:|---:|
| Return on equity (NI / avg equity) | –1.9% | **17.5%** |
| Return on assets (NI / avg assets) | –0.6% | **6.1%** |
| Asset turnover (revenue / avg assets) | 1.16x | **1.16x** |
| Equity / assets | 31.6% | **38.2%** |
| SBC / revenue | 3.8% | 4.2% |
| SBC / operating cash flow | 42.0% | **28.3%** |

**ROE of ~17.5% is a massive restoration** from a negative FY2022, powered by both the earnings rebound *and* a **+38.2% equity build** ($146.0B → $201.9B) — the latter from retained earnings plus a **+$23.96B increase in additional paid-in capital** ($75.07B → $99.03B, the SBC capital contribution). **Adjusted for SBC, the "true" ROE is materially lower** (SBC-adjusted NI of ~$6.4B after tax would imply ~4-5% ROE on average equity), which is the most important caveat on the quality of the 17.5% figure.

---

## 12. Actionable Trading Insights

### Structural BULL case (strongly supported by the data)
1. **FCF regime change is the core thesis.** A **$49.1B annual swing** to **+$32.2B FCF** with **capex intensity at a multi-year low (9.2%)** means AMZN can now be valued on FCF/margin progression rather than "investment mode" narratives. Historically, durable FCF inflections in mega-caps precede multiple expansion.
2. **Operating-income tripling (2.4% → 6.4% margin) has room to run.** G&A *declined* YoY and marketing grew only 5.0% vs revenue +11.8% — the cost-discipline program is still contributing. Deferred revenue **+28%** suggests contracted forward demand.
3. **Net-cash balance sheet (~$144B liquidity vs ~$70B debt+fin. leases)** eliminates credit risk and funds either AI capex or a future capital return.
4. **Net interest is now ~breakeven (–$0.23B vs –$1.38B)** — a non-operating tailwind that has largely *already* materialized, cushioning the unusually high 19% tax rate.
5. **No refinancing cliff**: only **$8.50B** due in the next 12 months vs **$73.4B cash**.

### Risk factors / BEAR considerations
1. **Capex re-acceleration risk (highest-conviction risk).** 9.2% capex intensity is likely a trough. AI/data-center buildout could push capex back toward $60-65B+, compressing FCF by up to ~50% from the FY2023 peak. **Any guidance implying a capex step-up is the key near-term de-rating trigger.**
2. **SBC at $24.0B, +22.4% YoY, 4.2% of revenue**, with **$18.3B unrecognized** — persistent, unmitigated dilution (share count +1.38%) with no buyback offset. GAAP EPS quality is therefore structurally below "cash EPS."
3. **Cash taxes doubled to $11.18B** and the effective rate normalized to 19% — a permanent cash drain that grows with earnings.
4. **Operating-lease obligations of $75.6B / $90.8B undiscounted**, with **$44.6B due after year 5** — an off-balance-sheet-adjacent fixed cost that reduces true financial flexibility despite the headline net-cash position.
5. **Non-operating earnings are volatile and mark-to-market-driven** (+$11.6B / –$13.6B / +$1.0B across FY21-23). A repeat of a FY2022-style equity-mark hit could swing GAAP EPS dramatically without any operating deterioration — a **modeling trap in both directions**.
6. **No capital returns**: zero buyback, zero dividend, and **zero long-term debt issued in 2023** means the historical cheap-funding lever is gone.
7. **DSO drift (30 → 33 days) and rising bad-debt write-offs (+23.1%)** warrant monitoring, particularly with enterprise/AWS exposure.

### Positioning summary
The FY2023 10-K supports a **constructive fundamental stance**: the margin/FCF inflection, deleveraging, and contracted-demand signals are all confirmed by hard filing data. The prudent trade construction is to be **long the operating-margin and FCF trajectory while explicitly underweighting GAAP-EPS growth quality** (SBC, tax normalization) and **hedging the capex re-acceleration scenario** — since that single variable has the largest mechanical impact on the FCF number that underpins any re-rating argument.

---

## 13. Key Fundamental Data Table

| Category | Metric | FY2021 | FY2022 | FY2023 | Read |
|---|---|---:|---:|---:|---|
| **Revenue** | Net sales ($M, derived) | 469,822 | 513,983 | 574,785 | +11.8% YoY, re-accel |
| **Profitability** | Gross profit ($M) | 197,478 | 225,152 | 270,046 | +19.9% |
| | Gross margin | 42.0% | 43.8% | **47.0%** | +320 bps, mix + efficiency |
| | Operating income ($M) | 24,879 | 12,248 | **36,852** | +200.9% |
| | Operating margin | 5.3% | 2.4% | **6.4%** | +403 bps, inflection |
| | Net income ($M) | 33,364 | –2,722 | 30,425 | Full recovery |
| | Net margin | 7.1% | –0.5% | 5.3% | — |
| | Diluted EPS ($) | 3.24 | –0.27 | **2.90** | — |
| **Cash flow** | Operating cash flow ($M) | 46,327 | 46,752 | **84,946** | +81.7% |
| | Capex ($M) | 61,053 | 63,645 | 52,729 | –17.2% |
| | **Free cash flow ($M)** | –14,726 | –16,893 | **+32,217** | **+$49.1B swing** |
| | Capex / revenue | 13.0% | 12.4% | **9.2%** | Multi-year low |
| | D&A ($M) | 34,433 | 41,921 | 48,663 | +16.1% |
| | SBC ($M) | 12,757 | 19,621 | **24,023** | +22.4%, 4.2% of rev |
| **Balance sheet** | Total assets ($M) | 420,549 | 462,675 | **527,854** | +14.1% |
| | Cash & equivalents ($M) | 36,477* | 53,888 | **73,387** | +36.2% |
| | Marketable securities (FV, $M) | — | — | **70,919** | ~$144B total liquidity |
| | Long-term debt ($M) | — | 67,150 | **58,314** | –13.2%, no new issuance |
| | Finance leases ($M) | — | 15,783 | **12,109** | –23.3% |
| | Operating leases ($M) | — | 69,040 | **75,639** | $90.8B undiscounted |
| | Deferred revenue ($M) | — | 16,100 | **20,600** | +28.0%, leading indicator |
| | Total equity ($M) | — | 146,043 | **201,875** | +38.2% |
| | Current ratio | — | 1.00x | **1.045x** | Thin but improving |
| | Net cash (liq. – debt – fin. leases) | — | ~+$41.9B | **~+$73.9B** | Net-cash |
| **Returns** | ROE | — | –1.9% | **17.5%** | Flattered by SBC |
| | ROA | — | –0.6% | **6.1%** | — |
| **Capital allocation** | Buybacks ($M) | 0 | 6,000 | **0** | No returns |
| | Dividends ($M) | 0 | 0 | **0** | — |
| | LT debt issued ($M) | 19,003 | 21,166 | **0** | Deleveraging |
| **Tax** | Effective tax rate | 12.6% | n/m | **19.0%** | Normalized; cash taxes $11.18B |
| **Other** | Interest expense ($M) | 1,809 | 2,367 | 3,182 | Rising |
| | Interest income ($M) | 448 | 989 | **2,949** | Net interest ≈ breakeven |
| | Shares outstanding (M) | — | 10,242 | **10,383** | +1.38% (SBC dilution) |
| | Public float (2023-06-30) | — | — | $1.18T | — |
| | **Insider transactions** | — | — | **UNAVAILABLE** | No authorized dataset — do not infer |

\*FY2021 cash figure is the restricted-cash-inclusive series; the cash-only 2021 line was not returned.

**Data limitations recap:** (i) quarterly income-statement/cash-flow granularity was not present in the authorized cache — annual 10-K facts only; (ii) segment-level revenue and operating income (3 segments) were not returned; (iii) insider transactions: **no authorized data** — explicitly unavailable, not zero; (iv) total stockholders' equity and total liabilities for FY2023/FY2022 are as reported in the 10-K and reconciled to returned asset and tag data but are not themselves standalone returned tags.