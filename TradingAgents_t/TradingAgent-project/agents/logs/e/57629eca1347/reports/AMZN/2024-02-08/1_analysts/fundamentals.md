# AMZN — Fundamental Research Report
**As of 2024-02-08 | Primary source: FY2023 Form 10-K (filed/accepted 2024-02-02), financial tables 6 days old**

---

## 1. Bottom line

AMZN just delivered the single most consequential fundamental print of its post-2022 reset: **FY2023 revenue of ~$574.8B with operating income of $36.85B (+201% YoY), net income of $30.43B (vs. a $2.72B loss in 2022), and free cash flow of $32.2B (vs. negative $16.9B a year ago).** The inflection is driven by three mechanical levers visible directly in the filings: (1) revenue growth of +11.8% against total cost growth of only +7.2%, (2) capex *falling* 17% to $52.7B while operating cash flow rose 82%, and (3) the disappearance of the 2022 non-operating drag (2022 non-operating was **–$18.18B**, largely equity-securities mark-to-market, vs. **+$0.71B** in 2023).

Cash generation is extremely back-end loaded: **derived Q4-2023 operating cash flow was ~$42.5B and Q4 free cash flow ~$27.9B — roughly 87% of the entire year's FCF was produced in the December quarter.** Any trader extrapolating the Q4 FCF run-rate into Q1 will be disappointed; any trader dismissing AMZN as a low-FCF story is now working off stale data.

---

## 2. Why the timing matters

The FY2023 10-K was accepted by EDGAR at **2024-02-02 04:48 UTC** — six trading days before the analysis date. Everything below is point-in-time filtered to facts *public by 2024-02-08*, so no later filings, restatements, or price action are embedded. **Insider-transaction data is explicitly unavailable in this data package for AMZN as of this date; no insider buying or selling is inferred or reported here.**

---

## 3. Company profile and structure

Amazon.com, Inc. is a global technology and e-commerce conglomerate. The FY2023 10-K reports **`NumberOfOperatingSegments = 3`**, consistent with its three reportable segments:

| Segment | Nature of business |
|---|---|
| North America | Retail, marketplace, advertising, Prime subscriptions, devices, logistics |
| International | Same model across non-US geographies, historically lower-margin/emerging |
| AWS | Cloud infrastructure, database, analytics, AI/ML services — the profit engine |

Business-model characteristics that matter for the fundamentals:
- **Negative working-capital retail**: payables and unearned revenue fund operations (AP $84.98B + unearned revenue $15.23B at YE23).
- **Two cost lines are quasi-fixed and self-funded**: fulfillment/logistics and technology & content — combined ~$176B of the $537.9B cost base (derived residual; the aggregate 10-K tags for these lines fall outside this data snapshot).
- **SBC is a real, growing cost**: $24.0B in 2023, 4.2% of revenue, +22.4% YoY — faster than revenue.
- **Scale reference**: `EntityPublicFloat` of **$1.1837 trillion** at 2023-06-30; **10.387B shares outstanding at 2024-01-24**.

---

## 4. Income statement — the operating-leverage story

*(All $ in millions; revenue derived as `CostsAndExpenses + OperatingIncomeLoss`, which reconciles exactly to reported net sales in all three years.)*

| | 2021 | 2022 | 2023 | FY23 YoY |
|---|---|---|---|---|
| Net sales (derived) | 469,822 | 513,983 | **574,785** | **+11.8%** |
| Cost of goods & services | 272,344 | 288,831 | 304,739 | +5.5% |
| **Gross profit** | **197,478** | **225,152** | **270,046** | **+19.9%** |
| Gross margin | 42.0% | 43.8% | **47.0%** | +320 bps |
| Marketing (S&M) | 32,551 | 42,238 | 44,370 | +5.0% |
| G&A | 8,823 | 11,891 | 11,816 | –0.6% |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| **Operating income** | **24,879** | **12,248** | **36,852** | **+200.9%** |
| Operating margin | 5.30% | 2.38% | **6.41%** | +403 bps |
| Non-operating income/(expense) | 13,272 | **(18,184)** | **705** | n.m. |
| Interest expense | 1,809 | 2,367 | 3,182 | +34.4% |
| Investment income (interest) | 448 | 989 | 2,949 | +198% |
| Pre-tax income | 38,151 | (5,936) | 37,557 | n.m. |
| Income tax | 4,791 | (3,217) | 7,120 | — |
| **Net income** | **33,364** | **(2,722)** | **30,425** | n.m. |
| Net margin | 7.10% | (0.53%) | **5.29%** | — |
| Diluted EPS | 3.24 | (0.27) | **2.90** | n.m. |
| Basic EPS | 3.30 | (0.27) | 2.95 | n.m. |

**Key reads:**
- **Operating leverage is unambiguous**: gross margin +320 bps, cost base growing at 60% of the revenue rate, operating income tripled off a low 2022 base.
- **Interest expense is rising fast (+34%)** even as debt falls — refinancing at higher coupons plus finance-lease interest. It is still only 8.6% of operating income (interest coverage **11.6x** on EBIT).
- **Investment income of $2.95B nearly offset interest expense of $3.18B** — net interest was essentially zero, a direct benefit of the cash pile and higher short rates.
- **Net margin (5.29%) is *below* 2021 (7.10%) while operating margin is *above* 2021.** The gap is entirely non-operating: 2021 was flattered by +$13.3B of investment gains. **Core operating profitability is at a record high; reported net margin is not.** This is the most important nuance in the print for anyone valuing AMZN on core earnings.
- **Ad spend** (Amazon's own) was $20,300 — down 1.5% from $20,600 in 2022, i.e., disciplined marketing while revenue grew 11.8%.

---

## 5. Cash flow — the real inflection

| | 2021 | 2022 | 2023 |
|---|---|---|---|
| Operating cash flow | 46,327 | 46,752 | **84,946** (+81.7%) |
| Purchases of PP&E (capex) | 61,053 | 63,645 | **52,729** (–17.1%) |
| **Free cash flow (OCF – capex)** | **(14,726)** | **(16,893)** | **+32,217** |
| Finance-lease principal repayments | 11,163 | 7,941 | 4,384 |
| **FCF less finance-lease principal** | (25,889) | (24,834) | **27,833** |
| Investing cash flow, net | (58,154) | (37,601) | (49,833) |
| Financing cash flow, net | +6,291 | +9,718 | **(15,879)** |
| FX effect | (364) | (1,093) | +403 |
| Net change in cash | (5,900) | +17,776 | **+19,637** |
| Capex / revenue | 13.0% | 12.4% | **9.2%** |
| FCF margin | (3.1%) | (3.3%) | **+5.6%** |

**Derived intra-year cadence (from 10-Q nine-month figures subtracted from the 10-K full year):**

| Derived period | OCF | Capex | FCF |
|---|---|---|---|
| 9M 2023 (reported in Q3 10-Q) | 42,481 | 38,141 | 4,340 |
| Q3 2023 alone (reported) | 21,217 | 12,479 | 8,738 |
| **Q4 2023 alone (derived)** | **42,465** | **14,588** | **27,877** |
| TTM to 2023-09-30 (reported) | 71,654 | 54,733 | 16,921 |

**Actionable insight:** ~87% of FY2023 free cash flow landed in Q4. The Q4 FCF margin on a revenue base of roughly $170B (Q4 is seasonally the largest quarter) implies ~16% quarterly FCF margin — a number that will compress sharply in Q1/Q2 due to seasonal working-capital reversal. **The structural story (capex down, OCF up) is real; the quarterly run-rate is not a fair base for Q1 expectations.**

Cash flow quality: OCF of $84.9B versus net income of $30.4B is a 2.79x conversion, supported by $48.7B of D&A and $24.0B of SBC — both non-cash. This is high-quality *for a capital-intensive model*, but note that **SBC is economically a transfer to employees**, and shares issued rose from 10,757M to 10,898M (+141M, +1.3%) in FY2023 alone. Buyback-adjusted, per-share value accretion is lower than headline EPS growth implies.

---

## 6. Balance sheet and liquidity

*(All $ in millions)*

| | 2022-12-31 | 2023-12-31 | Change |
|---|---|---|---|
| Cash & equivalents | 53,888 | **73,387** | +36.2% |
| Marketable securities (AFS, fair value) | n/a in snapshot | **70,919** | — |
| **Total cash + securities** | ~111,000 | **144,306** | +30% |
| Accounts receivable, net | 42,360 | 52,253 | +23.4% |
| Current assets | 146,791 | 172,351 | +17.4% |
| Total assets | 462,675 | **527,854** | +14.1% |
| Accounts payable | 79,600 | 84,981 | +6.8% |
| Accrued expenses & other | 62,566 | 64,709 | +3.4% |
| Unearned revenue (current) | 13,227 | 15,227 | +15.1% |
| **Total current liabilities (sum of the 3 above)** | **155,393** | **164,917** | +6.1% |
| **Current ratio** | 0.94 | **1.05** | improved |
| Long-term debt (carrying) | 67,150 | **58,314** | –13.2% |
| Finance-lease liabilities | 15,783 | 12,109 | –23.3% |
| Operating-lease liabilities | 69,040 | 75,639 | +9.6% |
| **Total debt incl. leases** | 151,973 | 146,062 | –3.9% |
| Stockholders' equity (derived: APIC + retained earnings + AOCI + common stock) | 146,043 | **201,875** | +38.2% |
| Total liabilities (derived: assets – equity) | 316,632 | 325,979 | +2.9% |
| Shares outstanding | 10,242M | 10,383M | +1.4% |

**Reads:**
- **AMZN is now in a net-cash position**: $144.3B of cash + securities against $58.3B of funded debt. Even including finance and operating leases ($146.1B total obligations), liquidity covers debt comfortably.
- **Working capital flipped positive**: +$7.4B at YE23 vs. –$8.6B at YE22; current ratio crossed above 1.0 for the first time in years. This is a genuine de-risking of the balance sheet.
- **Equity grew $55.8B in one year** (retained earnings +$30.4B, APIC +$24.0B from SBC). Book value per share ~$19.44.
- **Debt-to-equity fell to 28.9%** (from 46.0%) on a carrying-debt basis.
- **Unearned revenue (deferred revenue) up 26.6% to $20.6B total** (current $15.23B + noncurrent $5.70B), and $12.4B of prior deferred revenue was recognized in 2023 — a forward-demand indicator that is accelerating. This is a leading indicator for AWS commitments and Prime subscriptions.

### Debt maturity ladder (face value, at 2023-12-31)
2024: $8,500 | 2025: $5,286 | 2026: $3,146 | 2027: $8,750 | 2028: $2,250 | Thereafter: $39,250 | **Total: $67,182M**
Weighted heavily to 2029+, with only $8.5B due in the next twelve months against $144B of liquidity — **refinancing risk is negligible.**

### Contractual obligations (a genuine forward risk to monitor)
Total contractual obligations at YE23: **$300,409M**, comprising (derived decomposition) operating leases $90,777M, long-term debt principal $67,182M, finance leases $14,106M, and a residual of roughly **$128B of purchase obligations and other commitments** (content, cloud capacity, energy, logistics). The >5-year bucket alone is **$157,824M**. This is the single biggest off-balance-sheet-style overhang — a large share of it is almost certainly AI/datacenter and content commitments, which supports the AWS growth narrative but also locks in future cash outflows.

---

## 7. Capital allocation

| | 2021 | 2022 | 2023 |
|---|---|---|---|
| Long-term debt issued | 19,003 | 21,166 | **0** |
| Long-term debt repaid | 1,590 | 1,258 | 3,676 |
| Short-term debt raised | 7,956 | 41,553 | 18,129 |
| Short-term debt repaid | 7,753 | 37,554 | 25,677 |
| Share repurchases | 0 | 6,000 | **0** |
| Dividends | none evidenced | none evidenced | **none evidenced** |

**Reads:**
- **Zero long-term debt issuance in 2023** and a net reduction in short-term borrowings of ~$7.5B — a deliberate deleveraging year funded entirely by internal cash flow.
- **No buybacks in 2023** (after $6B in 2022) and **no dividend**. Capital is being recycled into capex, AWS capacity, and acquisitions rather than returned. Shareholders are being paid in equity value, not cash — and are being diluted ~1.3%/yr by SBC as the offsetting cost.
- Capex of $52.7B remains enormous in absolute terms but is now comfortably covered 1.6x by OCF. **The "investment supercycle" narrative peaked in 2022; the 2023-24 story is harvest.**

---

## 8. Returns and quality metrics

| Metric | 2022 | 2023 | Comment |
|---|---|---|---|
| ROE (net income / avg equity) | (1.8%) | **17.5%** | (15.1% on ending equity) |
| ROIC (NOPAT / equity + debt + fin. leases – cash & securities) | ~4.6% | **~23%** | NOPAT = $29,850M |
| ROIC incl. operating leases in capital | — | **~14.7%** | More conservative, lease-adjusted |
| EBITDA (op. income + D&A) | 54,169 | **85,515** | 14.9% margin (2022: 10.5%) |
| EBITDA incl. operating-lease cost add-back | 63,016 | **96,065** | 16.7% margin |
| Effective tax rate (book) | 54.2% (benefit) | **19.0%** | |
| **Cash taxes paid** | 6,035 | **11,179** | **29.8% of pre-tax income** |
| COGS / revenue | 56.2% | 53.0% | |
| SBC / revenue | 3.8% | 4.2% | rising — watch |
| D&A / revenue | 8.2% | 8.5% | |

**Quality flag worth acting on:** book tax expense of $7,120M included a **deferred tax benefit of –$5,876M**, while **cash taxes actually paid were $11,179M**. Headline net income and EPS were *supported* by deferred tax accounting; the cash tax rate (29.8%) is materially higher than the 19.0% book rate. A trader should haircut the durability of the 5.3% net margin somewhat — normalized for cash taxes, net income would have been closer to ~$26.4B. Notably, the deferred tax asset for IPR&D doubled from $6.82B to $14.80B, reflecting capitalized technology/content — an accounting choice to monitor.

---

## 9. What to watch (ranked by impact)

1. **Q1-2024 FCF normalization.** Q4 alone produced $27.9B of FCF; 9M produced $4.3B. Expect a materially lower Q1 FCF print, and expect sell-side models to be recalibrated. Trade the *trend* (capex discipline), not the *rate*.
2. **Capex guidance direction.** FY23 capex of $52.7B is down 17%. If AMZN re-accelerates capex for AI infrastructure (highly plausible given the ~$128B purchase-obligation residual), the FCF inflection stalls for 2–4 quarters. This is the single biggest swing factor to the bull case.
3. **SBC dilution vs. buybacks.** $24.0B of SBC (+22.4%) with zero repurchases. If AMZN starts buying back stock to offset dilution, it is a strong signal that management views the FCF inflection as durable.
4. **Interest expense trajectory (+34%).** Interest coverage is 11.6x and net interest was ~flat thanks to $2.95B of investment income; but as cash is redeployed into capex and debt matures into higher coupons, this tailwind fades.
5. **Deferred revenue and purchase obligations.** Unearned revenue +26.6% and noncurrent deferred revenue doubling to $5.70B are the best available proxies for AWS backlog/committed demand in this data set.
6. **Segment mix (not available as tagged facts in this snapshot).** AWS margin is the swing factor for consolidated operating margin. The 47.0% gross margin and 6.41% operating margin imply a rich mix, but the 10-K segment revenue/operating-income tags were not returned by the data vendor — **verify AWS revenue and AWS operating income directly from the 10-K before sizing a position on segment-level assumptions.**

---

## 10. Trading implications

**Bull case (evidence-based):**
- Operating income tripled to $36.85B and operating margin hit a record 6.41% — the 2022 cost reset is fully reflected.
- FCF swung +$49.1B YoY to +$32.2B; capex fell while OCF rose 82%.
- Net cash balance sheet ($144.3B liquidity vs. $58.3B debt), current ratio >1.0, equity +38%.
- Zero LT debt issuance, $3.7B repaid, no need for external capital.
- Deferred revenue +26.6% and noncurrent deferred revenue doubled — forward demand is accelerating.

**Bear/risk case (evidence-based):**
- 87% of FY23 FCF came from Q4 — the FCF run-rate is not repeatable quarterly; near-term prints will look like a deceleration.
- Net income was helped by a $5.88B deferred tax benefit; cash taxes were 29.8% of pre-tax income.
- SBC of $24.0B (+22.4%) with zero buybacks = ~1.3%/yr dilution; "EPS" growth is partly a share-count and tax artifact.
- $128B+ of purchase obligations and $157.8B due beyond five years constrain future flexibility.
- Operating margin of 6.41% is still thin versus mega-cap tech peers; there is no valuation anchor in this data set — **no price, market cap, or multiple data was provided, so no valuation conclusion can be drawn from this report alone.**

**Positioning conclusion:** The fundamentals support a *constructive* stance on AMZN on a 12-month horizon — the FCF inflection is real, funded internally, and the balance sheet has been de-risked. The tactical risk is a Q1-2024 FCF "air pocket" and any capex re-acceleration announcement. A trader should treat the FY2023 10-K as a **regime change in cash generation**, but size positions off normalized quarterly FCF of ~$5–8B (9M23 run-rate), not the $27.9B Q4 figure.

---

## 11. Data limitations disclosed

- **Insider transactions: UNAVAILABLE.** No authorized point-in-time insider archive exists for AMZN by 2024-02-08. No insider activity is reported or inferred.
- **No price, market cap, valuation multiple, or consensus estimate data** was provided — nothing in this report should be read as a valuation call.
- The vendor's fact set truncates alphabetically after "Intangible…", so **revenue tags, segment revenue/operating income, inventory, PP&E, retained earnings, and total liabilities were not directly returned.** Revenue was derived from `CostsAndExpenses + OperatingIncomeLoss` (reconciles exactly to reported net sales in all three years); equity and total liabilities were derived from component accounts; segment conclusions are limited to `NumberOfOperatingSegments = 3`.
- Quarterly income statement data for FY2023 quarters is **not** in this snapshot (the 10-K carries annual durations); Q4 cash-flow figures are arithmetic derivations from the FY 10-K minus the Q3 10-Q nine-month figures and are labeled as such.

---

## 12. Key metrics summary table

| Category | Metric | FY2021 | FY2022 | FY2023 | YoY / Note |
|---|---|---|---|---|---|
| **Scale** | Net sales (derived, $M) | 469,822 | 513,983 | **574,785** | +11.8% |
| | Shares outstanding (M) | — | 10,242 | 10,383 | +1.4% |
| | Public float (6/30/23) | — | — | **$1.184T** | 10-K cover |
| **Profitability** | Gross margin | 42.0% | 43.8% | **47.0%** | +320 bps |
| | Operating income ($M) | 24,879 | 12,248 | **36,852** | +200.9% |
| | Operating margin | 5.30% | 2.38% | **6.41%** | +403 bps |
| | Net income ($M) | 33,364 | (2,722) | **30,425** | n.m. |
| | Net margin | 7.10% | (0.53%) | **5.29%** | below 2021 on non-op |
| | Diluted EPS | 3.24 | (0.27) | **2.90** | n.m. |
| **Cash flow** | Operating cash flow ($M) | 46,327 | 46,752 | **84,946** | +81.7% |
| | Capex ($M) | 61,053 | 63,645 | **52,729** | –17.1% |
| | Free cash flow ($M) | (14,726) | (16,893) | **+32,217** | +$49.1B swing |
| | FCF margin | (3.1%) | (3.3%) | **+5.6%** | |
| | Capex / revenue | 13.0% | 12.4% | **9.2%** | –320 bps |
| | Q4-23 FCF (derived, $M) | — | — | **~27,877** | ~87% of FY FCF |
| **Balance sheet** | Cash + securities ($M) | ~36,477 | ~111,000 | **144,306** | +30% |
| | Long-term debt ($M) | — | 67,150 | **58,314** | –13.2% |
| | Total debt incl. leases ($M) | — | 151,973 | **146,062** | –3.9% |
| | Net cash position | — | net debt | **net cash** | $58.3B debt vs $144.3B liquid |
| | Total assets ($M) | 420,549 | 462,675 | **527,854** | +14.1% |
| | Stockholders' equity ($M) | — | 146,043 | **201,875** | +38.2% |
| | Current ratio | — | 0.94 | **1.05** | crossed above 1.0 |
| | Debt / equity | — | 46.0% | **28.9%** | |
| **Returns** | ROE (avg equity) | — | (1.8%) | **17.5%** | |
| | ROIC (lease-excl.) | — | ~4.6% | **~23%** | |
| | EBITDA ($M) | — | 54,169 | **85,515** | 14.9% margin |
| | Interest coverage (EBIT/int.) | 13.8x | 5.2x | **11.6x** | |
| **Capital allocation** | LT debt issued ($M) | 19,003 | 21,166 | **0** | deleveraging |
| | Buybacks ($M) | 0 | 6,000 | **0** | |
| | Dividends | none | none | **none** | not evidenced |
| | SBC ($M) | 12,757 | 19,621 | **24,023** | +22.4%, 4.2% of rev |
| **Quality flags** | Cash taxes paid ($M) | 3,688 | 6,035 | **11,179** | 29.8% of pre-tax |
| | Book tax rate | 12.6% | 54.2% benefit | **19.0%** | deferred benefit –$5,876M |
| | Contractual obligations ($M) | — | — | **300,409** | $157,824M >5 yrs |
| | Unearned revenue, total ($M) | — | 16,100 | **20,600** | +28.0% |
| **Insider activity** | Transactions | — | — | **N/A** | data unavailable — none reported |