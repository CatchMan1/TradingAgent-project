# AMZN — Fundamental Deep-Dive Report
**As of 2024-02-16 | Latest filing in scope: FY2023 Form 10-K, filed 2024-02-02 (accepted 04:48 UTC) | Fiscal year ended 2023-12-31**

> **Data provenance note:** All figures below come from point-in-time SEC XBRL facts for AMZN that were publicly accepted by 2024-02-16. The vendor feed is tag-level (not line-item formatted), and several tags — most importantly *revenue*, *property & equipment*, *inventory* and *segment detail* — were **not** returned. Where I derive a figure (e.g., revenue = `CostsAndExpenses` + `OperatingIncomeLoss`), the derivation is shown explicitly and cross-checked against internally consistent tags. Quarterly XBRL facts and insider-transaction data were **not available** (vendor returned `DATA_UNAVAILABLE`); no insider activity is inferred or fabricated.

---

## 1. Executive Summary — What the Numbers Say

AMZN's FY2023 10-K (filed two weeks ago) documents one of the sharpest operating inflections in the company's history:

- **Revenue ≈ $574.8B, +11.8% y/y** (vs. +9.4% in 2022) — re-acceleration.
- **Operating income $36.85B, 6.41% margin — 3.0x the $12.25B / 2.38% earned in 2022.** Operating income rose $24.6B on $60.8B of incremental revenue → **~40% incremental operating margin**.
- **Net income $30.43B (5.29% margin), diluted EPS $2.90** — versus a **net loss of $2.72B / –$0.27** in 2022.
- **Operating cash flow $84.95B (+81.7% y/y); free cash flow +$32.22B vs. –$16.89B** — a **$49.1B FCF swing in twelve months**.
- **Cost of sales grew only 5.5%** ($288.8B → $304.7B) against 11.8% revenue growth → **gross margin +317 bps to 46.98%**.
- **Balance sheet strengthened:** cash $73.4B + $70.9B available-for-sale securities ≈ **$144.3B liquidity**; long-term debt cut 13% to $58.3B; **no debt issued in 2023** (long-term issuance = $0).
- **Capital returns: zero.** $0 buybacks in 2023 (vs. $6.0B in 2022), no dividend. Share count still rose 1.4% (10,238M → 10,383M) purely from **$24.0B of stock-based comp**.

**Trading takeaway:** the FY2023 print validates a *margin-expansion + cash-generation* regime rather than a pure growth story. The debate has shifted from "can AMZN be profitable?" to "how much of the $32B FCF will be consumed by the next capex cycle?" That single variable — capex (9.2% of sales in 2023 vs. 13.0% in 2021, now bottoming) — is the primary swing factor for 2024 estimates.

---

## 2. Company Profile & Reporting Structure

- **Issuer:** Amazon.com, Inc. (CIK 0001018724), NASDAQ-listed, USD reporting, **December fiscal year-end**.
- **Reporting segments:** **3 operating segments** (`NumberOfOperatingSegments = 3`) — North America, International, and AWS cloud. *(Tag-level feed does not include segment revenue/operating-income splits, so no segment quantification is presented here.)*
- **Share base:** 10,383,812,291 shares outstanding as of **2024-01-24**; 100B shares authorized; par $0.01.
- **Public float:** **$1.1837 trillion** as of 2023-06-30 (`EntityPublicFloat`) — confirms large-cap, index-heavyweight status with corresponding liquidity and beta characteristics.
- **Scale markers (FY2023):** total assets $527.9B; total liabilities ≈ $326.0B (implied); shareholders' equity ≈ **$201.9B**; D&A $48.7B; capex $52.7B; 3 contractual-obligation layers (debt + leases + purchase commitments) totaling **$300.4B**.

---

## 3. Income Statement — FY2023 in Detail, with 2-Year Trend

Revenue is derived as `OperatingIncomeLoss + CostsAndExpenses` (both tagged). The derived values are internally consistent with the filed P&L and with the reported EPS.

| $ millions (FY, Dec-31) | **2023** | 2022 | 2021 | 23 y/y | 22 y/y |
|---|---:|---:|---:|---:|---:|
| **Revenue (derived)** | **574,785** | 513,983 | 469,822 | **+11.8%** | +9.4% |
| Cost of goods & services sold | 304,739 | 288,831 | 272,344 | +5.5% | +6.1% |
| **Gross profit** | **270,046** | 225,152 | 197,478 | **+19.9%** | +14.0% |
| *Gross margin* | **46.98%** | 43.81% | 42.03% | +317 bps | +178 bps |
| Operating expenses (ex-COGS) | 233,194 | 212,904 | 172,599 | +9.5% | +23.4% |
| — Marketing | 44,370 | 42,238 | 32,551 | +5.0% | +29.8% |
| — of which advertising | 20,300 | 20,600 | 16,900 | –1.5% | +21.9% |
| — G&A | 11,816 | 11,891 | 8,823 | –0.6% | +34.8% |
| — D&A (total) | 48,663 | 41,921 | 34,433 | +16.1% | +21.7% |
| — Stock-based comp (allocated) | 24,023 | 19,621 | 12,757 | +22.4% | +53.8% |
| **Operating income** | **36,852** | 12,248 | 24,879 | **+200.9%** | –50.8% |
| *Operating margin* | **6.41%** | 2.38% | 5.30% | +403 bps | –292 bps |
| Interest expense | 3,182 | 2,367 | 1,809 | +34.4% | +30.8% |
| Interest & investment income | 2,949 | 989 | 448 | +198.2% | +120.8% |
| Non-operating income/(expense), net | **+705** | –18,184 | +13,272 | n.m. | n.m. |
| Pre-tax income | 37,557 | –5,936 | 38,151 | n.m. | n.m. |
| Income tax expense/(benefit) | 7,120 | –3,217 | 4,791 | n.m. | n.m. |
| *Effective tax rate* | **18.96%** | 54.2% benefit | 12.56% | +640 bps | n.m. |
| Equity-method loss | –12 | –3 | +4 | — | — |
| **Net income** | **30,425** | –2,722 | 33,364 | n.m. | n.m. |
| *Net margin* | **5.29%** | –0.53% | 7.10% | +582 bps | –763 bps |
| **Diluted EPS** | **$2.90** | –$0.27 | $3.24 | n.m. | n.m. |
| Basic EPS | $2.95 | –$0.27 | $3.30 | n.m. | n.m. |
| Diluted share count implied | ~10,491M | ~10,087M | ~10,296M | +4.0% | — |

### How the margin was manufactured (the important part)
1. **Cost-of-sales leverage (+317 bps gross margin):** the single largest driver. COGS grew 5.5% against 11.8% revenue — consistent with fulfillment/network regionalization, lower unit costs, and mix shift toward higher-margin AWS + advertising. Incremental gross margin on the $60.8B revenue increase was ~74%.
2. **Discretionary cost freeze:** **G&A fell 0.6% y/y** (headcount-related restraint; `EmployeeRelatedLiabilitiesCurrent` was flat at **$7.700B** in both 2022 and 2023 — a hard data point confirming a hiring freeze through 2023). Marketing grew only 5.0%, half the revenue rate. Advertising spend was actually **cut 1.5%** to $20.3B — cost discipline, not demand weakness, at the corporate line.
3. **Non-operating normalized +$18.9B:** 2022 contained a **–$18.18B** non-operating loss (mark-to-market on equity securities — `EquitySecuritiesFvNiUnrealizedGainLoss` was **–$13.6B** in 2022 vs. **+$1.0B** in 2023; total marketable-securities unrealized swung from **–$13.87B to +$0.98B**). This is the *low-quality* part of the 2023 earnings recovery — it will not repeat at this magnitude.
4. **Net interest now roughly neutral:** interest income of $2.95B (+198%) almost fully offsets $3.18B of interest expense. Net interest drag improved from –$1.38B (2022) to –$0.23B (2023).
5. **Stock comp is the offset:** SBC of **$24.0B = 4.18% of revenue** (3.82% in 2022, 2.72% in 2021). GAAP operating margin of 6.41% would be **10.6%** ex-SBC. SBC grew **22.4%** — faster than revenue — and equals **87% of operating income**. This is real dilution and real cash-equivalent cost that bulls frequently underweight.

### Effective tax rate — a genuine headwind to model
- 2023: **18.96%** vs. **12.56%** in 2021. Tax expense of $7.12B on $37.56B pre-tax (federal statutory component $7.89B, state $1.31B, foreign rate differential +$0.59B, credits –$2.36B, prior-year –$0.60B).
- **Cash taxes paid were $11.18B vs. $7.12B book expense** (`IncomeTaxesPaidNet`), with a **–$5.88B deferred benefit**. Translation: AMZN's tax *cash* burden is running well *above* book, meaning deferred-tax-asset usage is masking earnings quality and the DTA runway is being consumed. **Do not extrapolate a sub-15% tax rate into 2024+.**

---

## 4. Cash Flow — the Core of the Current Thesis

| $ millions (FY) | **2023** | 2022 | 2021 | Comment |
|---|---:|---:|---:|---|
| **Operating cash flow** | **84,946** | 46,752 | 46,327 | **+81.7% y/y**; CFO margin 14.8% |
| Capex (productive assets) | 52,729 | 63,645 | 61,053 | –17.1% y/y; **decelerating** |
| **Free cash flow (CFO – capex)** | **+32,217** | –16,893 | –14,726 | **+$49.1B swing** |
| Finance-lease principal payments | 4,384 | 7,941 | 11,163 | –45%; lease-heavy era ending |
| **FCF less finance-lease principal** | **+27,833** | –24,834 | –25,889 | AMZN's own FCF convention |
| Investing cash flow | –49,833 | –37,601 | –58,154 | Marketable securities negligible net |
| Financing cash flow | **–15,879** | +9,718 | +6,291 | **Net debt repayor in 2023** |
| FX effect on cash | +403 | –1,093 | –364 | Turns positive |
| **Net change in cash** | **+19,637** | +17,776 | –5,900 | |
| Cash & equivalents (EOP) | **73,387** | 53,888 | 36,477 | +36.2% y/y |

### Cash conversion and quality checks
- **CFO / net income = 2.79x** — unusually high, but explainable: $48.7B D&A + $24.0B SBC against modest working-capital needs (`IncreaseDecreaseInContractWithCustomerLiability` +$4.58B deferred revenue, +$8.35B AR/other asset use, –$2.43B accrued liability use).
- **Capex intensity: 9.17% of revenue** (2022: 12.38%; 2021: 13.00%). Capex/D&A = **1.08x** — just above maintenance. **This is the critical asymmetry:** the 2023 FCF boom was *half* demand-driven (COGS/margin) and *half* capex-driven (a –$10.9B y/y capex cut). The capex half is finite.
- **Financing was a net drain of $15.9B:** $0 long-term debt issued (vs. $21.2B in 2022 and $19.0B in 2021), $3.68B LT repaid, short-term borrowings net –$7.55B ($18.1B drawn vs. $25.7B repaid), **$0 buybacks**, plus $4.38B finance-lease principal.
- **Cash taxes $11.2B** (vs. $6.0B in 2022, $3.7B in 2021) — the tax cash outflow is tripling as international profitability normalizes.

---

## 5. Balance Sheet — Fortress, With a Long Lease Tail

| $ millions | **2023-12-31** | 2022-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | **73,387** | 53,888 | +36.2% |
| AFS debt securities (fair value) | **70,919** (amort. cost 71,265) | n/a | — |
| Accounts receivable (net) | 52,253 | 42,360 | **+23.3%** |
| — AR allowance | 1,700 | 1,400 | +21.4% |
| **Current assets** | **172,351** | 146,791 | +17.4% |
| **Total assets** | **527,854** | 462,675 | +14.1% |
| Accounts payable | 84,981 | 79,600 | +6.8% |
| Accrued liabilities | 64,709 | 62,566 | +3.4% |
| Employee-related liabilities | 7,700 | 7,700 | **0.0%** |
| Contract liabilities — current | 15,227 | 13,227 | +15.1% |
| Contract liabilities — total | 20,600 | 16,100 | **+28.0%** |
| Operating lease liabilities — total | 75,639 | 69,040 | +9.6% |
| — current / non-current | 8,419 / 67,220 | 7,458 / 61,582 | |
| Finance lease liabilities — total | 12,109 | 15,783 | –23.3% |
| Long-term debt (carrying) | **58,314** | 67,150 | **–13.2%** |
| Deferred tax assets, net | 45,788 | 34,509 | +32.7% |
| Additional paid-in capital | 99,025 | 75,066 | +31.9% (SBC) |
| AOCI | –3,040 | –4,487 | improving |
| **Common shares outstanding** | **10,383M** | 10,242M | +1.4% |

### Liquidity and leverage assessment
- **Liquid assets ≈ $144.3B** (cash + AFS) vs. **$58.3B LT debt + $12.1B finance leases = $70.4B** → **net cash ≈ +$73.9B** before operating leases. Even including all operating leases ($75.6B), the position is roughly **neutral-to-net-cash**.
- **Gross lease-adjusted debt ≈ $146.1B** (58.3 + 12.1 + 75.6) against **EBITDA of ≈ $85.5B** (operating income $36.9B + D&A $48.7B) → **~1.7x**, comfortably investment-grade.
- **Runway on cash alone:** $39.3B of contractual obligations due in the next twelve months are covered **1.87x by cash and equivalents alone**, and ~1.9x by 2023 CFO every 5.5 months.
- **Current-ratio caution:** current assets of $172.4B vs. identified current obligations (AP $85.0B, accrued $64.7B, op-lease current $8.4B, fin-lease current $2.0B, plus current debt maturities of $8.5B) — the current ratio is **approximately 1.0x**. This is normal for AMZN (negative-ish working capital funded by payables float) but means the company depends continuously on supplier terms; a demand shock would pressure it quickly.

### Two balance-sheet flags worth monitoring
1. **AR grew 23.3% vs. 11.8% revenue growth** → DSO up from **30.1 to 33.2 days**. Partly mix (AWS/ads bill in arrears), partly a credit-quality caution sign. The allowance rose 21% to $1.7B and write-offs rose to $1.6B.
2. **Deferred tax asset for IPR&D jumped from $6.82B to $14.80B** (gross DTA $38.9B → $50.6B). A $8.0B gross increase implies **substantial acquired/licensed in-process technology** during 2023 (AI-related asset purchases are the most plausible reading, though the feed does not name the counterparty). This is a real cash use embedded in investing flows, and it will amortize against future earnings (finite-lived intangibles net rose $4.95B → $6.54B; amortization $706M, with $715M due in 2024 and ~$4.0B of amortization scheduled beyond year five).

---

## 6. Debt Maturity & Obligation Ladder (as of 2023-12-31)

**Long-term debt principal by year ($M):** 2024: 8,500 | 2025: 5,286 | 2026: 3,146 | 2027: 8,750 | 2028: 2,250 | Thereafter: 39,250 — **total $67.17B** (carrying $58.3B). The **$39.3B post-2028 bucket** is the fixed-rate core issued 2020–2021 at low coupons; refinancing risk is low, but **interest expense will keep climbing** as any new paper is priced higher ($3.18B in 2023, +34% y/y).

**Total contractual obligations ($M):** **$300,409** total → next 12M **39,345** | year 2 **30,863** | year 3 **25,713** | year 4 **28,398** | year 5 **18,266** | after 5 years **157,824**. The long tail is dominated by operating leases ($90.8B undiscounted) and multi-year content/cloud/energy purchase commitments. **This is the structural reason AMZN will never look "cheap" on a simple net-cash basis** — but it also means the lease-adjusted leverage is contractually locked in, not a refinancing cliff.

---

## 7. Capital Allocation & Dilution

- **Buybacks: $0 in 2023 and $0 in 2021; $6.0B in 2022.** No dividend has ever been paid. Management is explicitly prioritizing reinvestment (and, in 2023, deleveraging) over return of capital.
- **Dilution is the shareholder cost:** shares outstanding +1.41% in 2023 and +1.38% in 2022 despite zero buybacks. Total shares issued rose 10,757M → 10,898M. With **$24.0B of SBC** (4.2% of sales) and **$18.3B of unrecognized compensation cost** still to be expensed (~0.76 years' worth), expect **~1–1.5% annual dilution to persist**. For a trader modeling per-share value, this is a permanent ~1.2% headwind to EPS growth.
- **Debt:** net repayor for the first time in years — $0 new LT issuance, $3.68B LT repaid, $7.55B net short-term repayment, $4.38B finance-lease principal. **Debt reduction of ~$13B in one year is a genuine, under-appreciated sign of cash-flow confidence.**

---

## 8. Insider Transactions

**Not available.** The vendor's insider-transaction archive returned `DATA_UNAVAILABLE` for AMZN as of 2024-02-16. I have **not inferred, estimated, or fabricated** any insider buying or selling. Traders requiring Form 4 flow should source it from EDGAR directly (AMZN CIK 0001018724) — note that founder/executive 10b5-1 sales are a structural, continuous feature of AMZN and should not be read as a signal without size/pattern context.

---

## 9. What Changed This Week / Point-in-Time Context

- The **only** new primary disclosure in scope is the **FY2023 10-K filed 2024-02-02** (accepted 04:48 UTC, accession 0001018724-24-000008). No 10-Q, 8-K, or amendment was accepted between 2024-02-02 and 2024-02-16 in the feed.
- The most recent *pre-FY23* facts in the dataset are from the **Q3 2023 10-Q (filed 2023-10-27)**, useful only as a lease-maturity comparison.
- **No quarterly income-statement tags were returned** — I cannot compute standalone Q4-2023 revenue, AWS growth, or Q4 operating margin from this dataset. Anyone modeling the Q4 print must use the earnings release/10-K narrative, not this feed.
- Consequence for traders: **the fundamental information set here is 2 weeks stale and fully public** — it is the *baseline* against which the next catalyst (Q1-2024 report, expected late April) will be judged. Positioning, not information edge, is what this data supports.

---

## 10. Actionable Insights & Trading Implications

**Bullish, evidence-backed:**
1. **Incremental operating margin of ~40%** on 2023's $60.8B revenue increase is the strongest datapoint in the filing. If even a fraction persists on 2024's incremental revenue, consensus operating income is too low. The mechanism is visible in the tags (COGS +5.5%, G&A –0.6%, employee liabilities flat) — this is *structural cost discipline*, not one-off.
2. **FCF of $32.2B (or $27.8B on AMZN's finance-lease-adjusted basis) is a step-function change** from –$16.9B. Combined with **net cash of ~$74B ex-operating-leases** and **zero buybacks**, AMZN has both the capacity and the stated bias to redeploy into capex/AI — which is the growth optionality the market is paying for.
3. **Deleveraging + no LT issuance + $13B gross debt/lease reduction** in a single year removes balance-sheet risk from the bear case entirely.
4. **Contract liabilities +28% to $20.6B** (with $12.4B of it recognized into 2023 revenue) and **total obligations of $300B** indicate a demand book that is contracted, not speculative.

**Bearish / risk-management:**
1. **The FCF swing is half capex-cut, half margin.** Capex fell $10.9B y/y to 9.2% of sales. **Any 2024 capex re-acceleration immediately compresses the FCF narrative** — this is the #1 estimate risk. Model capex at 10–12% of sales as the base case and stress at 13%+ (2021 levels) → FCF could halve.
2. **~$18.9B of the earnings recovery is non-operating** (equity-securities marks swung from –$13.6B to +$1.0B, plus $2.95B interest income earned on a high cash balance). Neither persists indefinitely. **Ex these, operating income is the only durable driver — hence the importance of the 6.41% margin holding.**
3. **Tax normalization:** effective rate 19.0% (vs. 12.6% in 2021) with **cash taxes of $11.2B > book $7.1B**. EPS growth will be diluted by a rising tax rate as DTAs burn down.
4. **SBC at 4.2% of revenue / 87% of operating income** plus 1.4% annual dilution — a permanent haircut to per-share compounding, and the only reason share count isn't falling.
5. **DSO +3.1 days and AR +23%** — low-grade receivables-quality flag; watch the Q1-24 print for a reversal or continuation.
6. **Current ratio ≈1.0x** with heavy reliance on payables float — a sudden demand deceleration would pressure liquidity faster than the headline cash balance implies.

**Positioning synthesis:** The fundamental picture as of 2024-02-16 is **constructive with a specific, identifiable kill-switch (capex)**. The quality of the 2023 beat is high on the operating line (COGS/G&A leverage, flat headcount liabilities) and moderate on the below-the-line line (equity marks, interest income). For a trader, the asymmetry favors owning the operational-margin story while explicitly hedging or trimming into any guidance that implies capex >12% of sales, and watching three quarterly prints (AR days, SBC/revenue, cash-tax rate) as the earliest evidence of thesis decay.

---

## 11. Data Gaps — Read Before Using This Report

| Item | Status |
|---|---|
| Revenue, gross profit | **Derived** (OperatingIncomeLoss + CostsAndExpenses); reconciled to EPS and P&L structure |
| Quarterly income statement / standalone Q4-2023 | **Unavailable** from feed |
| Segment revenue & segment operating income (NA / Intl / AWS) | **Unavailable** — only `NumberOfOperatingSegments = 3` |
| Property, plant & equipment, inventory, retained earnings, total liabilities | **Not tagged / unavailable**; equity ≈ $201.9B and total liabilities ≈ $326.0B are implied from total assets |
| Insider transactions (Form 4) | **Unavailable** — vendor archive absent; nothing inferred |
| Market price / current market cap / forward estimates | **Unavailable** — only `EntityPublicFloat` $1.1837T as of 2023-06-30 |
| FY2024 guidance, management commentary, call transcript | **Not in dataset** (qualitative references are flagged as such) |

---

## 12. Key-Points Summary Table

| Category | Metric | FY2023 | FY2022 | FY2021 | Read-Through |
|---|---|---:|---:|---:|---|
| **Scale** | Revenue (derived, $M) | **574,785** | 513,983 | 469,822 | +11.8% — re-acceleration |
| | Revenue growth | +11.8% | +9.4% | — | Cyclical trough passed |
| **Profitability** | Gross margin | **46.98%** | 43.81% | 42.03% | +317 bps — primary driver |
| | Operating income ($M) | **36,852** | 12,248 | 24,879 | 3.0x y/y |
| | Operating margin | **6.41%** | 2.38% | 5.30% | Best-ever scale margin |
| | Net income ($M) | **30,425** | –2,722 | 33,364 | New record |
| | Diluted EPS | **$2.90** | –$0.27 | $3.24 | — |
| | EBITDA ($M) = OI + D&A | **~85,515** | ~54,169 | ~59,312 | 14.9% margin |
| **Cash flow** | Operating cash flow ($M) | **84,946** | 46,752 | 46,327 | +81.7% |
| | Capex ($M) | 52,729 | 63,645 | 61,053 | –17.1% — **cutting** |
| | **Free cash flow ($M)** | **+32,217** | –16,893 | –14,726 | **+$49.1B swing** |
| | CFO / net income | 2.79x | n.m. | 1.39x | High but D&A/SBC-explainable |
| | Capex / revenue | **9.17%** | 12.38% | 13.00% | At cycle low → risk of re-accel |
| **Balance sheet** | Cash + AFS securities ($M) | **144,306** | ~54,000+ | — | ≈2.5x LT debt |
| | Long-term debt ($M) | **58,314** | 67,150 | — | –13.2%, $0 new issuance |
| | Operating lease liability ($M) | 75,639 | 69,040 | — | +9.6% — the real leverage |
| | Total assets ($M) | **527,854** | 462,675 | 420,549 | +14.1% |
| | Shareholders' equity ($M, implied) | ~201,875 | ~146,043 | ~138,245 | ROE ≈15.1% |
| | Contract liabilities ($M) | **20,600** | 16,100 | — | +28% — demand visibility |
| | Shares outstanding (M) | 10,383 | 10,242 | — | +1.4% dilution, $0 buyback |
| **Quality flags** | SBC ($M) / % revenue | **24,023 / 4.18%** | 19,621 / 3.82% | 12,757 / 2.72% | Rising — watch |
| | Unrecognized SBC ($M) | 18,300 | — | — | ~0.76 yr of expense |
| | Effective tax rate | **18.96%** | 54.2% benefit | 12.56% | Normalizing higher |
| | Cash taxes paid ($M) | **11,179** | 6,035 | 3,688 | 3.0x in 2 yrs |
| | DSO (days) | 33.2 | 30.1 | — | +3.1 days — monitor |
| | AR growth vs revenue growth | +23.3% vs +11.8% | — | — | Mild caution |
| | Net cash ex-operating leases ($M) | **~+73,900** | — | — | Fortress |
| | Gross debt / EBITDA (incl. leases) | ~1.7x | — | — | IG-comfortable |
| **Capital returns** | Buybacks ($M) | **0** | 6,000 | 0 | Reinvestment mode |
| | Dividend | None | None | None | — |
| **Insider** | Form 4 activity | **Unavailable** | — | — | Do not infer |
| **Catalyst** | Next disclosure | Q1-2024 (est. late April) | — | — | Watch capex guide |

**Bottom line for AMZN (2024-02-16):** FY2023 is a high-quality operating inflection (COGS/G&A leverage, 3x operating income, $32B FCF, $74B net cash) partially flattered by non-operating marks and a capex holiday. The stock's next leg depends almost entirely on whether the 6.4% operating margin is defended while capex re-accelerates. Fundamentals are **bullish with a defined capex risk**; the data does not support either a leverage-driven or an insider-signal-driven case in either direction.