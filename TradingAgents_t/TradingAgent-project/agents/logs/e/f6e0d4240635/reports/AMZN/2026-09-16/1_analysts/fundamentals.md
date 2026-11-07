# AMZN — Comprehensive Fundamental Report
**Analysis date:** 2026-09-16 | **Latest filing:** Q2 2026 Form 10-Q (period ended 2026-06-30, accepted 2026-07-31) | **Next report due:** Q3 2026 (period ends 2026-09-30)

---

## 1. Bottom line

AMZN's operating engine is accelerating: Q2 2026 revenue reached a derived **$200.6B (+19.6% YoY)**, operating income **$27.5B (+43.2% YoY)**, and operating margin **13.7% (+226 bps YoY)**. Cost discipline in marketing, G&A and stock-based comp more than offset a 31% jump in depreciation.

However, **headline GAAP EPS is heavily distorted by non-cash mark-to-market gains**. Q2 2026 net income of **$62.6B** includes a **$50.5B upward revaluation of equity securities without readily determinable fair value** (and $62.8B for H1 2026). On a cleaned-up basis, Q2 EPS is roughly **$2.15–$2.20**, not the reported **$5.75** — still up ~29% YoY, but far less dramatic than the reported +243%.

The other defining feature is the **AI/datacenter capex cycle**: TTM capex of **$173.0B** (+60.7% YoY) has pushed TTM free cash flow to **–$11.6B** (from +$13.5B a year earlier). AMZN is funding this with a near-doubling of debt (long-term debt $68.8B → $133.0B in six months). Liquidity remains ample ($176.1B cash + marketable securities), but FCF and future depreciation are the key swing factors for the equity.

**Stance implied by the fundamentals:** operating momentum is genuinely strong; reported earnings quality is weak; cash-flow inflection depends on capex plateauing. This is a "watch capex, discount the marks" setup rather than a clean earnings beat story.

---

## 2. Data basis and limitations (important)

- Figures are point-in-time SEC XBRL facts accepted by 2026-09-16. Latest period: **2026-06-30**.
- **Revenue is not directly exposed in the returned tag set.** I derived net sales as `CostsAndExpenses + OperatingIncomeLoss`, which reconciles exactly to AMZN's reported Q2 2025 net sales of $167.7B — validating the method.
- **Total stockholders' equity and total liabilities were truncated** from the vendor feed; leverage ratios are therefore presented on gross debt and liquidity rather than D/E.
- **Full-year FY2025 income statement/cash-flow rows were not available** (only 10-Q data). H2 2025 figures below are derived as TTM minus H1 2026 and are labeled as such.
- **Insider transactions:** the vendor returned `DATA_UNAVAILABLE` — no authorized point-in-time insider archive for AMZN. I have not inferred or fabricated any insider activity.
- No market price or valuation multiples were supplied; this is a fundamental-only report.

---

## 3. Company profile

**Amazon.com, Inc. (AMZN)** — the Q2 2026 10-Q reports **3 operating segments**: North America, International, and Amazon Web Services. The business combines online and third-party marketplace retail, Prime subscriptions, advertising, logistics/fulfillment, devices, and cloud infrastructure/services (AWS). The current fundamental story is dominated by AWS/AI infrastructure investment and the associated capex, depreciation and financing.

---

## 4. Income statement analysis

### 4.1 Quarterly progression (USD millions; revenue derived)

| Metric | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 | Q2 YoY |
|---|---:|---:|---:|---:|---:|
| Net sales (derived) | 155,667 | 167,702 | 181,519 | **200,606** | **+19.6%** |
| Cost of goods & services | 76,976 | 80,809 | 87,463 | 95,778 | +18.5% |
| Gross profit | 78,691 | 86,893 | 94,056 | 104,828 | +20.6% |
| Gross margin | 50.6% | 51.8% | 51.8% | **52.3%** | +45 bps |
| Total costs & expenses | 137,262 | 148,531 | 157,667 | 173,145 | +16.6% |
| Operating income | 18,405 | 19,171 | 23,852 | **27,461** | **+43.2%** |
| Operating margin | 11.8% | 11.4% | 13.1% | **13.7%** | +226 bps |
| Non-operating income | 3,274 | 1,686 | 15,982 | **53,396** | +3,067% |
| Pre-tax income | 21,679 | 20,857 | 39,834 | 80,857 | +287.7% |
| Tax expense | 4,553 | 2,678 | 9,560 | 18,199 | +579.6% |
| Effective tax rate | 21.0% | 12.8% | 24.0% | **22.5%** | +970 bps |
| Net income | 17,127 | 18,164 | 30,255 | **62,647** | +244.9% |
| Diluted EPS | ~$1.59 | $1.68 | ~$2.78 | **$5.75** | +242% |

**H1 2026 vs H1 2025:** revenue **$382.1B vs $323.4B (+18.2%)**; operating income **$51.3B vs $37.6B (+36.6%)**; operating margin **13.4% vs 11.6%**; net income **$92.9B vs $35.3B**; diluted EPS **$8.53 vs $3.27**.

**Derived H2 2025** (TTM minus H1 2026): net income **$42.4B**, operating cash flow **$90.0B**, capex **$74.6B**, D&A **$36.3B**.

### 4.2 The margin story is real — and it is opex-led

Q2 2026 operating margin expanded 226 bps despite depreciation acting as a drag:

| Expense ratio (% of revenue) | Q2 2025 | Q2 2026 | Change |
|---|---:|---:|---:|
| Marketing | 6.81% | 5.83% | **–98 bps** |
| G&A | 1.77% | 1.39% | –38 bps |
| Stock-based comp | 3.90% | 3.01% | **–89 bps** |
| Total D&A | 9.08% | 9.96% | +88 bps |
| — of which PP&E depreciation | 5.82% | 6.91% | +109 bps |

This is high-quality margin expansion: marketing spend grew only 2.5% against 19.6% revenue growth, and SBC fell 7.6% YoY. It also highlights the forward risk — **depreciation is compounding faster than revenue** and will keep doing so as the capex base is placed in service.

Interest expense rose to **$1,314M in Q2 2026 (+155% YoY)** from $516M, and H1 2026 interest expense was **$2,114M vs $1,057M (+100%)**, directly reflecting the debt build.

---

## 5. Earnings quality — the single most important adjustment

Q2 2026 non-operating income of **$53.4B** included:

- **+$50.5B** upward price adjustment on equity securities without readily determinable fair value (H1 2026: **+$62.8B**, vs just $86M in H1 2025)
- +$1.3B equity securities FV gain; +$1.3B marketable securities gain; +$1.3B interest income
- –$1.3B interest expense; –$1.4B warrant fair-value adjustment

This is a **non-cash, illiquid mark** (the related balance sheet line jumped from $16.2B to **$122.3B** in six months). It is real economic value if realizable, but it is not operating earnings and can reverse.

**Approximate adjusted EPS (my estimate, 22.5% tax):**

| | Q2 2026 | H1 2026 |
|---|---:|---:|
| Reported diluted EPS | $5.75 | $8.53 |
| Less after-tax non-marketable equity mark | ~$3.59 | ~$4.44 |
| **Adjusted EPS (est.)** | **~$2.16** | **~$4.09** |
| Prior-year comparable | $1.68 | ~$3.26 |
| **Adjusted YoY growth** | **~+29%** | **~+25%** |

Additional quality point: H1 2026 tax expense was **$27.8B**, but **cash taxes paid were only $4.0B**. Deferred tax expense was **$30.5B**, largely tied to the unrealized gains. Reported net income and the tax line are therefore heavily non-cash this year — cash generation is better than the P&L optics suggest, while GAAP EPS is worse quality.

---

## 6. Balance sheet analysis

### 6.1 Balance sheet snapshot (USD millions)

| Item | 2025-12-31 | 2026-06-30 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 86,810 | 78,213 | –8,597 |
| AFS debt securities | 45,800 | **97,900** | +52,100 |
| **Cash + securities** | **132,610** | **176,113** | **+43,503** |
| Accounts receivable, net | 67,729 | 88,092 | **+30.1%** |
| Inventory | 38,325 | 38,184 | –0.4% |
| Current assets | 229,083 | 249,264 | +8.8% |
| **Total assets** | **818,042** | **1,095,689** | **+33.9%** |
| Accounts payable | 121,909 | 147,440 | +20.9% |
| Accrued liabilities | 75,520 | 73,406 | –2.8% |
| Current liabilities | 218,005 | 241,274 | +10.7% |
| Long-term debt (incl. current) | 68,836 | **132,995** | **+93.2%** |
| Finance lease liabilities | 12,286 | 13,451 | +9.5% |
| Operating lease liabilities | 89,252 | 96,320 | +7.9% |
| Equity securities w/o readily determinable FV | 16,200 | **122,300** | **+655%** |
| APIC | 140,024 | 149,619 | +9,595 |
| AOCI | 28,230 | 66,287 | +38,057 |
| Shares outstanding (M) | 10,731 | 10,783 | +0.5% |

### 6.2 Liquidity and leverage

- **Current ratio: 1.03x** (249,264 / 241,274) — thin, but supported by $97.9B of AFS securities, of which **$96.5B matures within one year**.
- **Quick ratio: ~0.88x** ((249,264 – 38,184) / 241,274).
- **Gross debt:** $132,995M long-term debt + $13,451M finance leases = **$146.4B**.
- **Net cash excluding operating leases: +$29.7B** ($176.1B liquid assets – $146.4B debt/ finance leases).
- **Net debt including $96.3B operating leases: ~–$66.7B** — a more complete but still manageable picture given ~$100B+ annualized operating income.
- Debt increased ~$64B in six months while **$39.8B of cash acquisitions** and **$98.4B of capex** were deployed in H1. Long-term debt issuance was **$67.0B** and short-term borrowings **$15.4B** in H1 2026.

### 6.3 Working capital and hidden assets

- **Receivables +30.1%** versus revenue +19.6% — receivables are outgrowing sales. The allowance for doubtful accounts rose only from $2.40B to $2.80B (+16.7%), so **coverage fell from 3.5% to 3.2%** of gross receivables. Worth monitoring, though not alarming at this scale.
- **Inventory flat**, a positive sign of supply-chain discipline.
- **Deferred revenue (contract liabilities) $24.9B vs $25.0B at year-end — flat.** No evidence of a demand acceleration or deterioration in this leading indicator.
- **$122.3B of non-marketable equity securities** is the single largest new asset. It explains ~38% of the $277.6B asset increase and is **illiquid and mark-to-model**. Similarly, the **+$38.1B AOCI** swing reflects unrealized investment gains, not cash.

### 6.4 Off-balance-sheet commitments

- **Total contractual obligations: $650.0B** at 2026-06-30.
  - Due within 12 months: **$78.1B** (remainder of FY2026: $42.8B)
  - Year 2: $53.4B; Year 3: $46.8B; Year 4: $42.2B
- **Operating lease payments:** $116.4B undiscounted vs $96.3B liability.
- **Finance lease payments:** $16.7B undiscounted vs $13.5B liability.

The $650B commitment stack — likely including AI capacity, chips, energy and logistics — is a demand-conviction signal but also a fixed-cost risk if AI monetization lags.

---

## 7. Cash flow and capital allocation

### 7.1 Cash flow summary (USD millions)

| Metric | H1 2025 | H2 2025 (derived) | H1 2026 | TTM Jun-26 | Prior TTM Jun-25 |
|---|---:|---:|---:|---:|---:|
| Operating cash flow | 49,530 | 89,984 | **71,419** | **161,403** | 121,137 |
| Capex (productive assets) | 57,202 | 74,617 | **98,411** | **173,028** | 107,656 |
| **Free cash flow** | **–7,672** | **+15,367** | **–26,992** | **–11,625** | **+13,481** |
| D&A | 29,489 | 36,267 | 38,933 | 75,200 | 58,562 |
| Acquisitions, net of cash | 1,652 | 2,524 | **39,767** | 41,956 | 4,809 |
| Investing cash flow | –69,227 | — | –143,457 | –216,775 | –123,569 |
| Financing cash flow | –2,586 | — | **+62,913** | **+75,160** | –8,652 |
| Cash taxes paid | 5,638 | — | 3,978 | 6,635 | 11,788 |

**Key observations:**
- **OCF grew +44.2% YoY in H1** ($71.4B vs $49.5B) and +33.2% on a TTM basis — the earnings are translating into cash.
- **Capex grew +72.0% YoY in H1** and +60.7% TTM. Q2 2026 capex alone was **$54.2B, or 27.0% of revenue** (H1: 25.8%). Annualized, that is a >$200B run-rate.
- **Q2 2026 FCF was –$8.8B**; Q1 2026 was –$18.2B.
- The entire FCF deterioration is capex-driven: TTM OCF rose $40.3B, but capex rose $65.4B.
- **Financing flipped from –$8.7B (prior TTM) to +$75.2B**, funding acquisitions and the capex gap.
- **No meaningful buyback is evident**: share count rose 0.5% in six months and 1.9% YoY (issued shares 11,246M → 11,298M). Capital allocation priority is clearly growth investment, not return of capital.

---

## 8. Financial history summary

| Period | Revenue (derived) | Operating income | Operating margin | Net income | Diluted EPS |
|---|---:|---:|---:|---:|---:|
| Q1 2025 | 155,667 | 18,405 | 11.8% | 17,127 | ~1.59 |
| Q2 2025 | 167,702 | 19,171 | 11.4% | 18,164 | 1.68 |
| H1 2025 | 323,369 | 37,576 | 11.6% | 35,291 | 3.27 |
| H2 2025 (derived) | n/a | n/a | n/a | 42,379 | n/a |
| Q1 2026 | 181,519 | 23,852 | 13.1% | 30,255 | ~2.78 |
| Q2 2026 | 200,606 | 27,461 | 13.7% | 62,647 | 5.75 |
| H1 2026 | 382,125 | 51,313 | 13.4% | 92,902 | 8.53 |
| **TTM Jun-26** | **~764B annualized run-rate** | n/a | n/a | **135,281** | n/a |

Sequential momentum: revenue **+10.5% QoQ**, operating income **+15.1% QoQ**, margin **+55 bps QoQ** in Q2 2026. YoY growth accelerated from +16.6% in Q1 to +19.6% in Q2.

---

## 9. Insider transactions

**No data available.** The vendor explicitly reported no authorized point-in-time insider-transactions archive for AMZN as of 2026-09-16. This is a data gap, not a signal; no insider buying or selling should be inferred from this report.

---

## 10. Risks and monitorables

**Bear-side risks**
1. **Earnings quality/reversal risk:** ~$3.59 of Q2's $5.75 EPS came from a non-cash, illiquid equity mark. A valuation reset in that holding could produce a large GAAP earnings swing.
2. **Capex/FCF risk:** TTM FCF is –$11.6B with capex at 27% of quarterly sales. Continued upward capex revisions would extend the negative FCF period.
3. **Depreciation cliff:** PP&E depreciation rose 42% YoY in Q2 and will keep stepping up as AI assets are commissioned — a structural margin headwind of potentially 100+ bps.
4. **Rising leverage and interest cost:** Debt +93% in six months; Q2 interest expense +155% YoY. Refinancing costs and credit spreads now matter.
5. **$650B contractual obligations:** a large fixed-cost/demand-risk overhang if AI workloads monetize slower than planned.
6. **Tax normalization:** H1 cash taxes were only $4.0B vs $27.8B of book tax. A shift toward cash tax normalization would reduce future cash flow growth.
7. **Receivables/allowance:** AR +30% vs revenue +19.6%, with allowance coverage down to 3.2%.

**Bull-side supports**
1. Revenue acceleration (+19.6%) with gross margin at 52.3%.
2. Genuine opex leverage: marketing, G&A and SBC all down as a % of sales.
3. OCF +44% YoY in H1 and +33% TTM.
4. $176.1B of cash and near-maturity securities; net cash positive before operating leases.
5. $122.3B of non-marketable equity holdings — substantial asset value not reflected in operating earnings.
6. Flat inventory and flat deferred revenue suggest no demand deterioration.

**Specific things to watch next quarter**
- Capex guidance/run-rate (the single biggest FCF swing factor)
- AWS revenue growth and AI backlog disclosure (not in this feed)
- Depreciation as a % of revenue (currently 10.0%)
- Interest expense trajectory and any further debt issuance
- Whether the non-marketable equity mark is revised up or down
- Share count/buyback activity
- AR growth vs revenue growth and allowance coverage

---

## 11. Actionable conclusions for traders

1. **Discount the headline EPS.** Build models off ~$2.15 Q2 2026 adjusted EPS, not $5.75. The reported +243% EPS growth overstates underlying growth by roughly 8x; underlying growth is a still-healthy ~29%.
2. **The operating beat is genuine and broad-based.** Revenue +19.6%, operating income +43%, and 226 bps of margin expansion driven by marketing, G&A and SBC leverage. This supports the quality of the core franchise.
3. **FCF is the crux.** A capex plateau or guide-down would be a meaningful positive catalyst for the equity; another leg up in capex would pressure FCF and likely the multiple. Current run-rate implies >$200B of annual capex.
4. **Watch the depreciation lag.** Even if revenue holds, the P&L will absorb rising depreciation from the 2025–2026 build. Margin expansion may slow or reverse mechanically.
5. **Balance sheet is a shock absorber, not a constraint — yet.** $176B liquid assets vs $146B debt/ finance leases leaves net cash of ~$30B. But the direction of travel (debt +93%, interest +155%) warrants monitoring.
6. **Do not read anything into insider activity** — the data is unavailable for AMZN.

---

## 12. Key points summary table

| Category | Metric | Value | Interpretation |
|---|---|---:|---|
| **Scale** | Q2 2026 net sales (derived) | $200.6B | +19.6% YoY; growth accelerated from Q1's +16.6% |
| **Profitability** | Q2 2026 operating income | $27.5B | +43.2% YoY |
| **Profitability** | Q2 2026 operating margin | 13.7% | +226 bps YoY; opex-led, not gross-margin-led |
| **Profitability** | Q2 2026 gross margin | 52.3% | +45 bps YoY |
| **Earnings** | Q2 2026 reported diluted EPS | $5.75 | +242% YoY, heavily flattered |
| **Earnings** | Q2 2026 adjusted EPS (est.) | ~$2.16 | Ex ~$3.59/share non-cash equity mark; ~+29% YoY |
| **Earnings quality** | Non-marketable equity mark, H1 2026 | +$62.8B | Non-cash, illiquid; reversal risk |
| **Earnings quality** | Deferred tax expense, H1 2026 | $30.5B | Book tax >> cash taxes ($4.0B) |
| **Cash flow** | H1 2026 operating cash flow | $71.4B | +44.2% YoY |
| **Cash flow** | H1 2026 capex | $98.4B | +72.0% YoY; 25.8% of revenue |
| **Cash flow** | TTM free cash flow | –$11.6B | vs +$13.5B prior TTM; capex-driven |
| **Cash flow** | Q2 2026 capex / revenue | 27.0% | ~$217B annualized run-rate |
| **Balance sheet** | Cash + AFS securities | $176.1B | $96.5B of securities mature <1 year |
| **Balance sheet** | Long-term debt (incl. current) | $133.0B | +93.2% in six months |
| **Balance sheet** | Net cash excl. operating leases | ~+$29.7B | Still positive, but narrowing |
| **Balance sheet** | Current ratio | 1.03x | Thin; liquidity from securities |
| **Balance sheet** | Non-marketable equity securities | $122.3B | Up from $16.2B; illiquid hidden asset |
| **Balance sheet** | Total contractual obligations | $650.0B | $78.1B due within 12 months |
| **Balance sheet** | Receivables growth | +30.1% | Ahead of +19.6% revenue growth |
| **Capital returns** | Shares outstanding | 10,783M | +0.5% in 6 months; no meaningful buyback |
| **Insider activity** | Transactions | **Unavailable** | Vendor has no authorized archive; do not infer |
| **Overall** | Fundamental read | **Strong operations / weak reported earnings quality / negative FCF** | Watch capex, depreciation and mark reversals |