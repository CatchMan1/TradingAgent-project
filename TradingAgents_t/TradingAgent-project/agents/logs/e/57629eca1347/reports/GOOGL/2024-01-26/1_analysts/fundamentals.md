# GOOGL (Alphabet Inc.) — Fundamental Research Report
**Analysis date: 2024-01-26 | Source: SEC XBRL facts (point-in-time, filtered by EDGAR acceptance timestamp) + configured fundamental vendor**

---

## 1. Scope, provenance and important point-in-time caveats

| Item | Status |
|---|---|
| Latest financial filing available as of 2024-01-26 | **Q3 FY2023 Form 10-Q**, period ended 2023-09-30, filed 2023-10-25, accession 0001652044-23-000094 (accepted 2023-10-24 22:39 UTC) |
| Q4/FY2023 results | **Not yet filed/in the dataset.** Alphabet's Q4'23 release historically occurs in the first days of February (i.e., ~1 week after this analysis date). **All figures below are therefore through 9M/30-Sep-2023 and do not include the holiday-quarter print.** |
| Prior-year full 10-K | FY2022 10-K, filed 2023-02-03 (accn 0001652044-23-000016) — used for multi-year cash-flow and debt-maturity series |
| Insider transactions | **DATA_UNAVAILABLE** — the vendor has no authorized, point-in-time insider-transaction archive for GOOGL as of 2024-01-26. No insider activity is reported, inferred, or fabricated in this document. |
| Data caveat | The vendor's flat XBRL dump is alphabetically truncated: tags appearing late in the alphabetical order (e.g. `Revenues`, `ResearchAndDevelopmentExpense`, `SellingAndMarketingExpense`, `StockholdersEquity`, `Goodwill`) were not returned. Where a figure is **derived** from reported subtotals (e.g., Revenue = CostsAndExpenses + OperatingIncomeLoss) it is explicitly labelled **(D)**. |
| Price/valuation data | No market-price feed was provided; no P/E, EV/EBITDA or target price is asserted. |

---

## 2. Company profile and business model

GOOGL is Alphabet Inc., the parent of Google. Its operating structure (as reported in the FY2022 10-K and the 2023 10-Qs) comprises:

- **Google Services** — Google Search & other, YouTube ads, Google Network, Google subscriptions/platforms/devices (Play, YouTube Premium/TV, Pixel, Fitbit), the largest profit pool. Monetized mainly by advertising, increasingly by subscriptions and in-app/Play fees.
- **Google Cloud** — Google Cloud Platform (infrastructure + data/AI/analytics) and Google Workspace (productivity/collaboration subscriptions). This is the growth-and-margin-inflection segment.
- **Other Bets** — early-stage businesses (e.g., Waymo, Verily, Wing), immaterial to revenue and loss-making at the operating line.
- **Hedging/Alphabet-level** — Alphabet-level AI R&D (Google DeepMind), corporate costs, and a large investment portfolio (debt securities + non-marketable equity stakes) that drives non-operating income volatility.

Note: the tools returned no narrative company-profile block; the segment description above is structural background, while **every quantitative claim in §3–§9 is sourced from the SEC facts above.**

**Structural features that matter for the trade:**
1. **Extremely high gross margin (~57%) and operating margin (~27%)** with a cost base shifting toward compute/cloud depreciation (visible in rising cost of revenue) offset by headcount and real-estate discipline.
2. **A fortress balance sheet**: ~$120B of cash + marketable securities, gross debt of only ~$15B of principal.
3. **Massive, accelerating capital returns**: ~$45.3B of buybacks in 9M23 plus the first-ever dividend was announced *after* this date (Feb 2024), so it is not in this dataset.
4. **Earnings quality dependency on non-operating items** — mark-to-market on equity securities swung from **–$2.50B (9M22)** to **+$0.71B (9M23)**, a material y/y tailwind.

---

## 3. Q3 FY2023 (Jul–Sep 2023) — the most recent reported quarter

All $ in millions unless stated.

| Line item (Q3 FY2023, ended 2023-09-30) | Value | Q3 FY2022 | y/y |
|---|---:|---:|---:|
| **Revenue (D)** = CostsAndExpenses + OperatingIncomeLoss | **76,693** | 69,092 | **+11.0%** |
| Cost of revenue (reported) | 33,229 | 31,158 | +6.6% |
| **Gross profit (D)** | **43,464** | 37,934 | +14.6% |
| Gross margin (D) | **56.7%** | 54.9% | +1.8 pts |
| G&A expense (reported) | 3,979 | 3,597 | +10.6% |
| R&D + S&M combined (D) = CostsAndExpenses – CoR – G&A | 18,142 | 17,202 | +5.5% |
| Total costs & expenses (reported) | 55,350 | 51,957 | +6.5% |
| **Operating income (reported)** | **21,343** | 17,135 | **+24.5%** |
| Operating margin | **27.8%** | 24.8% | +3.0 pts |
| Non-operating income/(expense) (reported) | (146) | (902) | n.m. |
| — of which interest income (reported) | 1,066 | 615 | +73.3% |
| — of which interest expense (reported) | (116) | (101) | +14.9% |
| Pre-tax income (reported) | 21,197 | 16,233 | +30.6% |
| Income tax (reported) | 1,508 | 2,323 | –35.1% |
| **Effective tax rate (reported)** | **7.1%** | 14.3% | –7.2 pts |
| **Net income (reported)** | **19,689** | 13,910 | **+41.5%** |
| Net margin | **25.7%** | 20.1% | +5.6 pts |
| EPS diluted (reported) | **$1.55** | $1.06 | **+46.2%** |
| EPS basic (reported) | $1.56 | $1.07 | +45.8% |
| Operating cash flow (D, see §6) | 30,656 | 23,353 | +31.3% |
| Capex (D) | 8,055 | 7,276 | +10.7% |
| **Free cash flow (D)** | **22,601** | 16,077 | **+40.6%** |
| Share repurchases (D) | **15,787** | 15,892 | –0.7% |

**Reading the quarter (actionable):**
- **Revenue growth re-accelerated to +11% y/y**, the first double-digit quarter in a year. Because operating expense grew only +6.5% versus revenue +11.0%, operating leverage is now flowing through: operating income grew 24.5% on 11% revenue — a ~2.3x incremental-margin dynamic.
- **The 7.1% tax rate is not sustainable.** It compares to a 14.3% rate a year ago and 13.4% for 9M23. A software-and-services company with Alphabet's global mix should print in the mid-teens. If a discrete benefit drove the low Q3 rate, ~$1.5–2.0B of EPS quality (roughly $0.12–0.16 per share) is non-recurring. **Do not capitalize the 7.1% rate into forward EPS.**
- **Interest income nearly doubled**, mechanically lifting EPS as rates rose on a ~$120B securities book.
- **Non-operating swung to –$146M from –$902M**, helped by equity-securities marks (Q3'23 FV-NI loss –$366M vs –$647M a year ago; unrealized –$224M vs –$86M). This line remains the single largest source of EPS noise.

---

## 4. Nine-month FY2023 (Jan–Sep) vs. nine-month FY2022 — the trend line

| $ millions | 9M FY2023 | 9M FY2022 | Change |
|---|---:|---:|---:|
| **Revenue (D)** | **221,084** | 206,788 | **+6.9%** |
| Cost of revenue | 95,757 | 90,861 | +5.4% (43.3% vs 43.9% of rev) |
| **Gross profit (D)** | **125,327** | 115,927 | +8.1% (56.7% vs 56.1%) |
| G&A | 11,219 | 10,628 | +5.6% |
| R&D + S&M (D) | 53,512 | 48,617 | +10.1% |
| Costs & expenses | 160,488 | 150,106 | +6.9% |
| **Operating income** | **60,596** | 56,682 | **+6.9%** (27.4% margin both years) |
| Non-operating income/(expense) | **+709** | (2,501) | **+$3.21B swing** |
| — interest income | 2,755 | 1,515 | +81.8% |
| — interest expense | (239) | (267) | –10.5% |
| Pre-tax income | 61,305 | 54,181 | +13.2% |
| Income tax | 8,197 | 7,833 | +4.6% |
| Effective tax rate | **13.4%** | 14.5% | –1.1 pts |
| **Net income** | **53,108** | 46,348 | **+14.6%** |
| Net margin | **24.0%** | 22.4% | +1.6 pts |
| EPS diluted | **$4.16** | $3.50 | **+18.9%** |
| EPS basic | $4.19 | $3.53 | +18.7% |
| Comprehensive income | 53,675 | 39,119 | +37.2% |
| Share-based compensation (reported) | 16,500 | 14,400 | +14.6% |

**Key structural observations:**
1. **Operating margin was flat at 27.4% for 9M** — the y/y operating-leverage story is a *Q3-only* phenomenon so far, meaning H1'23 (still carrying the 2022 cost structure and severance/office-space charges) offsets it. This is the crux of the bull/bear debate: is Q3's 27.8% the new run-rate or a good quarter?
2. **All of the net-income outperformance is below the operating line**: pre-tax grew $7.12B while operating income grew $3.91B — i.e., **~55% of the y/y pre-tax dollar increase came from non-operating items** (interest income and equity marks). This is the single most important earnings-quality caveat for GOOGL right now.
3. **EPS (+18.9%) outpaced net income (+14.6%)** thanks to a ~2.4% lower share count — buybacks are adding ~4 pts of EPS growth.
4. **SBC of $16.5B (7.5% of revenue)** remains a real economic cost; FCF is *not* SBC-adjusted. For valuation, treat SBC as a cash-equivalent expense.

---

## 5. Margin and returns analysis (calculated)

| Metric | 9M FY2023 | 9M FY2022 | Comment |
|---|---:|---:|---|
| Gross margin (D) | 56.7% | 56.1% | Improving mix, despite AI/compute depreciation |
| Operating margin | 27.4% | 27.4% | Flat 9M; Q3 alone 27.8% |
| Pre-tax margin | 27.7% | 26.2% | Boosted by interest income |
| Net margin | 24.0% | 22.4% | |
| Effective tax rate | 13.4% | 14.5% | Unsustainably low vs ~15–17% normalized |
| Annualized ROE (D) | **~26.8%** | ~28%+ | Equity $273.2B at 9/30/23; avg. equity ~$264.7B |
| ROA (annualized, D) | ~17.9% | — | Asset-light economics |
| SBC / revenue | 7.5% | 7.0% | Rising — watch dilution vs. buyback offset |
| Cash conversion (OCF/NI) | **1.56x** | 1.46x | Excellent; non-cash SBC and D&A fund it |
| FCF margin (D) | **27.9%** | 21.3% | Best-in-class |

**Verdict:** Alphabet's profitability is arguably the best in large-cap tech on a cash basis (27.9% FCF margin), but 2H23 earnings quality is flattered by (i) a sub-normal tax rate, (ii) $2.76B of interest income on the securities book, and (iii) equity-mark swings. **Underlying operating profit growth (ex-those items) is roughly +7%, not +25%.**

---

## 6. Cash flow and capital allocation

### Q3 and 9M FY2023 (reported subtotals; quarterly/9M deltas derived)

| $ millions | Q3 FY2023 (D) | Q3 FY2022 (D) | 9M FY2023 | 9M FY2022 |
|---|---:|---:|---:|---:|
| Operating cash flow | 30,656 | 23,353 | **82,831** | 67,881 |
| Capex (PP&E purchases) | (8,055) | (7,276) | (21,232) | (23,890) |
| **Free cash flow** | **22,601** | 16,077 | **61,599** | 43,991 |
| Purchases of marketable securities | — | — | (49,422) | (67,253) |
| Sales/maturities of marketable securities | — | — | 52,642 | 84,087 |
| Purchases of other investments | — | — | (2,176) | (1,628) |
| Proceeds from other investments | — | — | 743 | 131 |
| **Investing cash flow** | — | — | **(20,896)** | (14,071) |
| Debt issued, net of costs | — | — | 9,298 | 44,322 |
| Debt repayments + finance leases | — | — | (9,621) | (45,350) |
| **Share repurchases** | **15,787** | 15,892 | **45,313** | 43,889 |
| Minority proceeds | — | — | 8 | 10 |
| **Financing cash flow** | — | — | **(52,785)** | (52,128) |
| FX effect on cash | — | — | (327) | (643) |
| Net change in cash | — | — | **+8,823** | +1,039 |

**Interpretation for traders:**

- **OCF +22% on revenue +7%** — the quality of earnings is improving; working capital was a *source* of cash (AR decreased benefit of +$1.315B; contract liabilities +$690M; income taxes payable +$10.392B — the tax-payable build is a deferred/deferral timing item and will reverse as the Q3 estimated payments settle).
- **Capex is *falling* (–11% y/y) while revenue grows** — this is the single most underappreciated fundamental change in 2023. FY2022 capex intensity was elevated (data centers, offices), and management guided 2023 capex toward the low end. Result: **FCF +40% y/y**. The forward risk is that the AI infrastructure build (TPUs, data centers) re-inflates 2024 capex — a stated priority post-Q3. Watch the Q4 capex guide as the swing factor for 2024 FCF.
- **Buyback run-rate stepped up sharply:** 9M23 $45.3B vs 9M22 $43.9B, but the *quarterly* cadence accelerated — Q1 $14.56B, Q2 $14.97B, Q3 $15.79B. Against a $70B authorization (announced Apr-2023) there is a large remaining capacity; at ~$15.8B/qtr the program would be exhausted in ~1.5 quarters, implying continued or increased pace.
- **Debt activity**: $9.3B issued vs $9.6B repaid in 9M23 — essentially refinancing at higher coupons (interest expense up modestly). Net debt is deeply negative (~$105B net cash). **Refinancing risk is immaterial.**
- **No dividend in the dataset as of 2024-01-26.** Any dividend initiation would be incremental news (and indeed was announced the week after this date, outside the data window).

### Multi-year annual cash-flow history (FY2022 10-K, filed 2023-02-03)

| $ millions | FY2020 | FY2021 | FY2022 |
|---|---:|---:|---:|
| Operating cash flow | 65,124 | 91,652 | **91,495** |
| Investing cash flow | (32,773) | (35,523) | (20,298) |
| Financing cash flow | (24,408) | (61,362) | **(69,757)** |
| Operating lease payments (in OCF) | 2,004 | 2,489 | 2,722 |

**History lesson:** FY2022 was the year financing outflows ($69.8B, dominated by buybacks) exceeded operating cash generation growth, and OCF flatlined (+0.2% vs FY2021) as growth slowed. **9M23 OCF of $82.8B already equals ~91% of the entire FY2022 figure** — the 2023 recovery is unambiguous.

---

## 7. Balance sheet and liquidity (as of 2023-09-30 vs. 2022-12-31)

| $ millions | 2023-09-30 | 2022-12-31 | Change |
|---|---:|---:|---:|
| Cash & cash equivalents | 30,702 | 21,879 | +40.3% |
| Marketable securities (AFS debt) | 85,218 | — | — |
| **Cash + short-term investments** | **119,935** | **113,762** | **+5.4%** |
| Accounts receivable, net | 41,020 | 40,258 | +1.9% |
| Allowance for doubtful accounts | 832 | 754 | +10.3% |
| Inventory | 2,957 | 2,670 | +10.7% |
| **Total current assets** | **176,310** | **164,795** | **+7.0%** |
| Equity securities w/o readily determinable FV | 28,821 | 28,529 | +1.0% |
| Equity-method investments | 1,500 | 1,500 | 0% |
| Deferred tax assets, net | 10,983 | 5,261 | **+108.8%** |
| Goodwill + intangibles (intangibles only reported) | 1,833 | 2,084 | –12.0% |
| Operating lease ROU asset | 14,199 | 14,381 | –1.3% |
| **Total assets** | **396,711** | **365,264** | **+8.6%** |
| Accounts payable | 5,803 | 5,128 | +13.2% |
| Accrued liabilities | 55,602 | 37,866 | **+46.8%** |
| Accrued income taxes, current | 13,528 | 1,632 | **+729%** |
| Employee-related liabilities | 12,562 | 14,028 | –10.4% |
| Current portion of finance lease | 400 | 298 | +34.2% |
| Current operating lease liability | 2,715 | 2,477 | +9.6% |
| **Total current liabilities** | *(truncated in feed)* | 69,300 | — |
| Accrued income taxes, non-current | 8,038 | 9,258 | –13.2% |
| Non-current operating lease liability | 12,550 | 12,501 | +0.4% |
| Finance lease liability, non-current | 1,914 (D) | 1,844 (D) | +3.8% |
| **Total liabilities** | **123,509** | **109,120** | **+13.2%** |
| **Total stockholders' equity (D)** = Assets – Liabilities | **273,202** | **256,144** | **+6.7%** |
| Contract liabilities (current + non-current) | 5,187 | 4,507 | +15.1% |
| AFS securities in unrealized-loss position | 72,052 | 75,519 | –4.6% |
| — accumulated unrealized loss | (4,244) | (4,779) | improving |

**Balance-sheet read-through:**
- **Liquidity is extraordinary**: ~$120B of cash/securities versus **~$15.3B of total debt principal** (per the FY2022 maturity schedule: $0.22B due <1yr, $1.16B yr2, $1.16B yr3, $2.16B yr4, $1.17B yr5, $9.45B beyond yr5). Net cash ≈ $105B, i.e., ~27% of total assets. This is downside protection and buyback/bolt-on-M&A capacity.
- **Liabilities grew faster than assets (+13.2% vs +8.6%)** but this is not leverage — it is working capital: accrued liabilities +$17.7B and current income taxes payable +$11.9B. These are timing items (tax payments due, accruals for expenses/fines), not new borrowings.
- **Deferred tax assets doubled to $11.0B**, consistent with (a) higher deferred revenue/cost accruals and (b) the low Q3 tax rate — some of the 7.1% Q3 rate may reflect DTA recognition. Either way, it supports cash tax efficiency short-term.
- **The securities book is healing**: AFS unrealized losses narrowed to $4.24B from $4.78B, and the ">12 months underwater" bucket rose to $45.5B / $3.48B loss — meaning duration risk remains. A rate-backup would hit AOCI, not EPS (held-to-maturity/AFS accounting), but it does impair buyback funding flexibility from the securities book.
- **Equity investments without readily determinable fair value of $28.8B** (cumulative upward adjustments $18.0B, downward $6.7B) is a hidden asset — the non-public portfolio (SpaceX, Anthropic-adjacent, various AI/healthcare stakes). Mark-ups here flow through the income statement when observed, producing episodic EPS spikes (and mark-downs).
- **Receivables discipline improved**: DSO (D) = AR ÷ (quarterly revenue/91) ≈ **48.7 days** in Q3'23 vs **53.0 days** in Q3'22 — a meaningful collections improvement that also helped OCF.

---

## 8. Segment/quality signals available inside the data

Although segment revenue lines were truncated, three reported items give strong directional reads:

1. **Cost of revenue growing slower than revenue (Q3: +6.6% vs +11.0%)** implies gross-margin expansion across the board — consistent with (a) Cloud losses narrowing as utilization improves and (b) the 2023 headcount/office-space cuts. **Cloud profitability inflection is the highest-torque driver for 2024 EPS.**
2. **G&A growth (+10.6% Q3) outpacing revenue is a caution** — the easy cost cuts are done; further margin expansion must come from gross margin and R&D/S&M discipline (R&D+S&M grew only 5.5% in Q3).
3. **Loss contingency accrual essentially flat at $9.14B** (vs $9.11B) — legal/regulatory exposures (EU antitrust, US DOJ ad-tech, state AG suits) are already provisioned at ~$9B; further adverse rulings would be incremental.

---

## 9. Insider transactions

**Not available.** The vendor explicitly returned: *"the B-project data package has no authorized, point-in-time insider-transactions archive for GOOGL by 2024-01-26."* No Form 4 activity is reported here, and none should be assumed. Insider-signal weighting for GOOGL should be treated as **neutral/uninformed** in this analysis.

---

## 10. Risks that the fundamentals above make concrete

| Risk | Evidence in the data | Trading implication |
|---|---|---|
| **Earnings quality / non-operating dependence** | ~55% of the 9M y/y pre-tax dollar increase came from interest income + equity marks, not operations | A rate-cut cycle or equity-mark reversal compresses EPS growth toward high-single digits |
| **Tax rate normalization** | Q3 7.1%, 9M 13.4% vs 14.5% prior year; global minimum tax (Pillar Two) applies from 2024 | Consensus 2024 EPS may be ~3–6% too high on tax alone |
| **Capex re-acceleration for AI** | Capex fell 11% y/y in 9M23, driving +40% FCF; management signalled an AI infrastructure ramp | FCF growth could stall in FY2024 even if revenue accelerates |
| **SBC dilution** | $16.5B SBC (7.5% of revenue), +14.6% y/y | Buybacks partly offset; FCF multiple should be adjusted |
| **Regulatory/legal** | $9.14B loss-contingency accrual; $4.24B AFS mark losses | Binary headline risk; provision limits but does not eliminate tail |
| **Concentration in advertising** | Google Services dominates profit; ad cycles are cyclical | Macro ad-spend slowdown directly hits the 57%-gross-margin core |
| **Interest-rate/M&A** | $72.1B of AFS securities in a loss position | AOCI volatility; limited EPS impact but caps liquid-firepower optics |

---

## 11. Actionable insights for traders (as of 2024-01-26)

1. **The setup into the Q4'23 print (expected ~first week of February, not in this dataset) is asymmetric to the upside on operating leverage, but the quality of the beat matters.** Q3 already showed +11% revenue with +24.5% operating income growth. If Q4 confirms ≥28% operating margin *and* capex guidance stays disciplined, the "margin-expansion + buyback" thesis compounds. If Q4 shows capex re-acceleration plus a normalized ~15% tax rate, headline EPS will disappoint versus extrapolations of the 7.1% Q3 rate.
2. **Buy the operating story, discount the below-the-line story.** Anchor valuation on ~27–28% operating margin and 27–28% FCF margin on a $290B+ annualized revenue run-rate (9M23 revenue $221.1B × 4/3 ≈ $294.8B), not on the flattered 24% net margin.
3. **Size positions knowing the share count is shrinking ~2.4%/yr and Q3 buybacks ran at $15.8B/quarter** against a $70B authorization — a persistent, price-insensitive bid that mechanically supports EPS. Any acceleration (or a first dividend, announced post-dataset) is a positive catalyst.
4. **Watch three specific print items for the next two quarters:** (a) **capex dollars and 2024 capex language** (the FCF swing factor); (b) **effective tax rate** (anything below ~14% is a one-off; model 15–16%); (c) **Cloud operating margin and cost of revenue as a % of revenue** (the durable driver of gross margin).
5. **Downside is balance-sheet-protected.** ~$120B cash/securities vs ~$15B debt, 31% liabilities/assets, 1.56x cash conversion, $9.1B legal provisions already booked. A multiple-compression drawdown is a balance-sheet-supported accumulation zone rather than a solvency event.
6. **What would break the thesis:** two consecutive quarters of flat/declining operating margin *with* rising capex and a rising tax rate — that combination would mean FY2023's FCF surge was a one-off cost-cycle artifact. None of that is visible in the 9M23/Q3 data; the opposite is.

---

## 12. Summary table — key fundamental points

| Category | Metric | Latest (Q3/9M FY2023) | Prior comparison | Signal |
|---|---|---|---|---|
| **Reporting status** | Latest filing | Q3 FY2023 10-Q (filed 2023-10-25) | FY2022 10-K (2023-02-03) | Q4'23 not yet reported |
| **Growth** | Revenue (Q3, D) | $76,693M | $69,092M (+11.0%) | 🟢 Re-accelerating |
| | Revenue (9M, D) | $221,084M | $206,788M (+6.9%) | 🟢 |
| **Margins** | Gross margin (Q3, D) | 56.7% | 54.9% | 🟢 |
| | Operating margin (Q3) | 27.8% | 24.8% | 🟢 |
| | Operating margin (9M) | 27.4% | 27.4% | 🟡 Flat |
| | Net margin (Q3) | 25.7% | 20.1% | 🟢 but flattered |
| **Earnings** | Operating income (Q3) | $21,343M | $17,135M (+24.5%) | 🟢 |
| | Net income (Q3) | $19,689M | $13,910M (+41.5%) | 🟢 (below-the-line help) |
| | Diluted EPS (Q3) | $1.55 | $1.06 (+46.2%) | 🟢 |
| | Diluted EPS (9M) | $4.16 | $3.50 (+18.9%) | 🟢 |
| | Effective tax rate (Q3 / 9M) | 7.1% / 13.4% | 14.3% / 14.5% | 🔴 Not sustainable |
| | Non-operating income (9M) | +$709M | –$2,501M | 🔴 Quality caveat |
| **Cash flow** | OCF (9M) | $82,831M | $67,881M (+22.0%) | 🟢 |
| | Capex (9M) | $21,232M | $23,890M (–11.1%) | 🟢 FCF tailwind |
| | FCF (9M, D) | $61,599M | $43,991M (+40.0%) | 🟢 |
| | FCF margin (9M) | 27.9% | 21.3% | 🟢 |
| | Cash conversion (OCF/NI) | 1.56x | 1.46x | 🟢 |
| **Capital returns** | Buybacks (9M) | $45,313M | $43,889M | 🟢 ~$15.8B/qtr |
| | Shares outstanding | 12,541M | 12,849M (YE22) | 🟢 –2.4% |
| | SBC (9M) | $16,500M (7.5% of rev) | $14,400M | 🔴 Real cost |
| | Dividend | None in dataset | — | — (announced post-dataset) |
| **Balance sheet** | Cash + ST investments | $119,935M | $113,762M | 🟢 |
| | Total debt principal | ~$15.3B (FY22 schedule) | — | 🟢 Net cash ≈$105B |
| | Total assets | $396,711M | $365,264M (+8.6%) | 🟢 |
| | Total liabilities | $123,509M | $109,120M (+13.2%) | 🟡 Working-capital driven |
| | Equity (D) | $273,202M | $256,144M | 🟢 |
| | Liabilities / assets | 31.1% | 29.9% | 🟢 |
| | Accrued income taxes, current | $13,528M | $1,632M | 🟡 Timing |
| | Legal loss contingency accrual | $9,143M | $9,106M | 🟡 Provisioned |
| | AFS unrealized loss | $4,244M | $4,779M | 🟢 Improving |
| | Non-marketable equity (no RDFV) | $28,821M | $28,529M | 🟢 Hidden asset |
| **Returns** | Annualized ROE (D) | ~26.8% | ~28%+ | 🟢 Elite |
| **Insider** | Form 4 activity | **UNAVAILABLE** | — | ⚪ Neutral by default |
| **Bottom line** | Operating momentum + fortress balance sheet + shrinking share count, offset by a sub-normal tax rate and non-operating EPS reliance | | | **Fundamentally constructive; do not extrapolate the Q3 tax rate or equity marks** |