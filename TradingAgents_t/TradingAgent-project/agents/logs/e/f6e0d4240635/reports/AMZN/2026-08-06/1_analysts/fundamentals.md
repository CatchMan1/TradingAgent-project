# AMZN — Fundamental Research Report
**Prepared:** 2026-08-06 · **Instrument:** AMZN (Amazon.com, Inc.) · **Basis:** Point-in-time SEC facts public on/before 2026-08-06 (latest filing: Q2-2026 Form 10-Q, accession 0001018724-26-000026, accepted 2026-07-31 02:11 UTC; prior 10-Q accession 0001018724-26-000014 accepted 2026-04-30)

---

## 1. What is new this week (the actual catalyst)

The freshest fundamental event is decisive: **AMZN filed its Q2-2026 (period ended 2026-06-30) 10-Q on 2026-07-31**, i.e. six days before this report. Everything below is drawn from that filing plus the Q1-2026 10-Q and trailing comparatives. There is no ambiguity about staleness — this is the newest possible data set.

The headline numbers look spectacular, but the composition matters far more than the headline:

| Metric | Q2 2026 | Q2 2025 | Δ y/y |
|---|---|---|---|
| Revenue (derived) | $200.6B | $167.7B | **+19.6%** |
| Operating income | $27.46B | $19.17B | +43.2% |
| Operating margin | 13.69% | 11.43% | **+226 bps** |
| Non-operating income | $53.40B | $1.69B | +3,067% |
| Pre-tax income | $80.86B | $20.86B | +287% |
| Net income | $62.65B | $18.16B | +245% |
| Diluted EPS | $5.75 | $1.68 | **+242%** |

**Critical read:** $53.4B of the $80.9B pre-tax profit (66%) came from *non-operating* items — overwhelmingly fair-value mark-ups on non-marketable equity securities. Strip them out and Q2 core pre-tax profit was $27.46B (= operating income exactly), producing roughly **$1.95 of core EPS versus $5.75 reported**. The reported number is approximately 2.9x the underlying operating earnings power.

**Data note on revenue:** the vendor slice returned does not include an explicit revenue XBRL tag (`RevenueFromContractWithCustomer*`). Revenue is therefore derived as `CostsAndExpenses + OperatingIncomeLoss`, which ties out exactly across every period presented and is internally consistent. Flagged for transparency; all growth rates below depend on this derivation.

---

## 2. Company profile

Amazon.com, Inc. is a global technology and retail conglomerate. The Q2-2026 filing confirms **three operating segments** (XBRL: `NumberOfOperatingSegments = 3`), consistent with the long-standing structure of North America, International, and Amazon Web Services. Revenue pools are: online and physical stores retail, third-party seller services (commissions, fulfillment, ads-linked), subscription (Prime), advertising, and AWS cloud/compute. The business model is characterised by (a) structurally negative working capital, (b) very large and rising capital intensity, and now (c) a rapidly growing portfolio of equity stakes in private companies (AI/technology), whose marks flow through the income statement under the fair-value option.

Segment-level revenue and profit detail was **not** present in the returned data slice — only the segment count. That is a genuine analytical gap this week.

---

## 3. Income statement: operating leverage is real, and it is the bullish core of the story

Derived quarterly reconstruction (all $B):

| | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 |
|---|---|---|---|---|
| Revenue (derived) | 155.7 | 167.7 | 181.5 | 200.6 |
| Cost of goods & services | 77.0 | 80.8 | 87.5 | 95.8 |
| Gross profit | 78.7 | 86.9 | 94.1 | 104.8 |
| Gross margin | 50.6% | 51.8% | 51.8% | **52.3%** |
| Fulfillment + tech/content + other (residual) | 47.0 | 53.3 | 56.9 | 62.9 |
| Marketing | 9.8 | 11.4 | 10.3 | 11.7 |
| G&A | 2.6 | 3.0 | 2.6 | 2.8 |
| Total costs & expenses | 137.3 | 148.5 | 157.7 | 173.1 |
| **Operating income** | **18.4** | **19.2** | **23.9** | **27.5** |
| **Operating margin** | 11.8% | 11.4% | 13.1% | **13.7%** |
| Non-operating income | 3.3 | 1.7 | 16.0 | 53.4 |
| Pre-tax income | 21.7 | 20.9 | 39.8 | 80.9 |
| Tax expense | 4.6 | 2.7 | 9.6 | 18.2 |
| Effective tax rate | 21.0% | 12.8% | 24.0% | 22.5% |
| Net income | 17.1 | 18.2 | 30.3 | 62.6 |
| Diluted EPS | 1.59 | 1.68 | 2.78 | 5.75 |

**What the detail proves — margin expansion is broad-based, not mix-shifted:**

- Revenue +19.6% y/y while **COGS grew +18.5%** → gross margin up 50 bps.
- Combined fulfillment/technology-and-content/other grew **+17.9%**, below revenue → ~100 bps of leverage in the largest cost pool.
- **Marketing spend grew only +2.5%** ($11.42B → $11.70B) against +19.6% revenue → ~120 bps of leverage. This is the single cleanest evidence of demand-pull rather than bought growth.
- **G&A fell 6.0%** y/y ($2.97B → $2.79B).
- **Share-based compensation was essentially flat**: $10.07B in H1-2026 vs $10.22B in H1-2025 (−1.5%) against +18.2% revenue growth. SBC/revenue has therefore compressed materially — genuinely shareholder-friendly relative to prior years. Unrecognised SBC remains $24.8B.

**H1-2026 aggregates:** revenue $382.1B (+18.2% y/y), operating income $51.3B (13.43% margin vs 11.62%), net income $92.9B, diluted EPS $8.53 (vs $3.27).

**H1-2026 core (ex-non-operating) estimate:** $39.5B net income → ~$3.63 core EPS vs ~$2.89 in H1-2025, i.e. **+25.6% core earnings growth**. Still excellent — just less than half the reported rate.

---

## 4. Earnings quality: the single most important item in this report

Two XBRL tags explain almost the entire y/y profit explosion:

- `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount`: **$16.2B (12/31/25) → $122.3B (6/30/26)**, up 655%.
- `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount`: **$62.81B in H1-2026**, of which **$50.49B landed in Q2 alone** ($12.33B in Q1).

Supporting detail: `EquitySecuritiesFvNiGainLoss` $1.30B in Q2; `FairValueAdjustmentOfWarrants` −$1.45B in Q2; `NonoperatingIncomeExpense` $53.40B in Q2.

Implications a trader must price:

1. **Non-cash, non-recurring, and model-valued.** These are Level 3 fair values on private company stakes. They flow through EPS but generate zero operating cash. `DeferredIncomeTaxExpenseBenefit` was $30.49B in H1-2026 vs $0.52B in H1-2025 — confirming the tax on these gains is deferred/unrealized, not cash-taxed (cash taxes paid actually *fell* to $3.98B from $5.64B).
2. **The balance sheet is now 20% mark-to-market securities:** $122.3B non-marketable equity + $97.9B available-for-sale debt = $220.2B, or **20.1% of $1,095.7B total assets**. AMZN's book value is now materially levered to private-AI valuation sentiment.
3. **Reversal risk is asymmetric.** A private-mark reset would hit GAAP EPS hard without touching operating cash flow. Conversely, further mark-ups can keep flattering EPS regardless of retail/AWS performance.
4. **The gain accelerated violently in Q2** ($12.3B → $50.5B quarter-over-quarter). Inflection points of that size in Level 3 marks warrant scepticism, not extrapolation.

**Actionable:** any earnings model, screen, or sell-side consensus anchored on GAAP EPS ($5.75 Q2; $8.53 H1) is mis-specified. Re-base on operating income ($27.46B Q2, 13.7% margin) and operating cash flow.

---

## 5. Balance sheet: dramatic expansion, thin liquidity, heavy debt issuance

| $B | 2025-12-31 | 2026-06-30 | Δ |
|---|---|---|---|
| Cash & equivalents | 86.81 | 78.21 | −9.9% |
| Available-for-sale debt securities | 45.80 | 97.90 | **+113.8%** |
| Accounts receivable, net | 67.73 | 88.09 | **+30.1%** |
| Inventory, net | 38.33 | 38.18 | −0.4% |
| **Current assets** | **229.08** | **249.26** | +8.8% |
| Equity securities w/o readily determinable FV | 16.20 | 122.30 | **+655%** |
| **Total assets** | **818.04** | **1,095.69** | **+33.9%** |
| Accounts payable | 121.91 | 147.44 | +20.9% |
| Accrued liabilities | 75.52 | 73.41 | −2.8% |
| **Current liabilities** | **218.01** | **241.27** | +10.7% |
| Long-term debt, total | 68.84 | 132.99 | **+93.2%** |
| — of which current | 2.75 | 3.33 | +21.2% |
| Operating lease liabilities | 89.25 | 96.32 | +7.9% |
| Finance lease liabilities | 12.29 | 13.45 | +9.5% |
| Contract liabilities (current) | 20.58 | 20.43 | −0.7% |
| AOCI (cumulative) | 28.23 | 66.29 | +134.8% |
| Additional paid-in capital | 140.02 | 149.62 | +6.9% |
| Shares outstanding (M) | 10,731 | 10,783 | +0.5% |

**Observations:**

- **Total assets grew 33.9% in six months.** Roughly $106B of that is the equity-stake revaluation + down; the rest is investment, acquisitions and receivables.
- **Current ratio deteriorated to 1.033** (249.26/241.27) from 1.051. Cash + AFS of $176.1B covers 73% of current liabilities. Ample for a company with $161.4B LTM operating cash flow, but the trend is negative.
- **Net cash position excluding leases:** cash + AFS $176.1B less debt $133.0B less finance leases $13.5B = **+$29.6B net cash**. Add the $96.3B operating-lease liability and the picture flips to net debt — but operating leases are matched by revenue-generating assets.
- **Cash conversion cycle is strongly negative (structural funding advantage):** using Q2-2026 flows — AR days 40.0, inventory days 36.3, AP days ~140.0 → **CCC ≈ −64 days.** AMZN is financed by its suppliers.
- **Receivables are a yellow flag.** AR +30.1% YTD vs revenue +19.6% y/y. The allowance for doubtful accounts rose only 16.7% ($2.40B → $2.80B), so **coverage fell from 3.54% to 3.18% of gross AR**. Either mix is shifting toward slower-paying enterprise/AWS-style customers, or credit provisioning is lagging. Monitor next quarter.
- **Inventory is a green flag.** Flat at $38.2B despite +19.6% revenue, and inventory valuation reserves *fell* $0.3B — healthy sell-through, no obsolescence build.

---

## 6. Cash flow: the bear case lives here

| $B | LTM to 6/30/25 | LTM to 6/30/26 | Δ | H1 2025 | H1 2026 |
|---|---|---|---|---|---|
| Operating cash flow | 121.14 | **161.40** | +33.2% | 49.53 | 71.42 |
| Capex (productive assets) | (107.66) | **(173.03)** | **+60.7%** | (57.20) | (98.41) |
| **Free cash flow** | **+13.48** | **(11.63)** | **negative** | **(7.67)** | **(26.99)** |
| Business acquisitions, net | (4.81) | **(41.96)** | +772% | (1.65) | (39.77) |
| Net investing cash flow | (123.57) | (216.78) | — | (69.23) | (143.46) |
| Net financing cash flow | (8.65) | **+75.16** | — | (2.59) | +62.91 |

**Q2-2026 alone:** CFO $45.39B; capex $54.21B; **FCF −$8.82B**; acquisitions $24.36B; total cash decline $23.77B.

**The three facts that define the current fundamental tension:**

1. **Capex is consuming >100% of operating cash flow.** LTM capex/CFO = **107%**. H1-2026 capex/revenue = 25.8%, versus 17.7% in H1-2025 — a 46% relative step-up in capital intensity. This is the AI/datacenter and logistics build-out.
2. **Capex is 2.3x depreciation** (LTM capex $173.0B vs LTM D&A $75.2B). Depreciation is already accelerating hard: Q2-2026 $19.99B vs Q2-2025 $13.87B, **+44.1%** (H1: $38.93B vs $29.49B, +32.0%). A large, mechanical margin headwind is locked in for coming quarters regardless of demand.
3. **The funding gap is being closed with debt, not equity.** H1-2026 gross debt issuance: $67.0B long-term + $15.4B short-term = **$82.4B**, against only $18.4B of repayments. Interest expense rose **+155% y/y** in Q2 ($0.52B → $1.31B) and +100% in H1 ($1.06B → $2.11B). Even so, coverage is comfortable: Q2 operating income/interest = **20.9x**; H1 = 24.3x. Investment income ($2.43B H1) still broadly offsets interest ($2.11B H1).

**Cash conversion of *core* earnings is excellent:** H1-2026 core net income ≈ $39.5B vs CFO $71.4B = **1.81x**. The cash engine is genuinely strong; it is simply being out-spent. This is a reinvestment-cycle story, not a profitability-deterioration story — but it does mean GAAP FCF is not currently a supportive valuation input.

---

## 7. Commitments, obligations and off-balance-sheet load

At 2026-06-30 (XBRL `ContractualObligation`):

| Commitment | $B |
|---|---|
| **Total contractual obligations** | **650.03** |
| Remainder of FY2026 | 42.75 |
| Due in next twelve months | 78.08 |
| Year 2 | 53.41 |
| Year 3 | 46.77 |
| Year 4 | 42.22 |
| Operating lease payments (undiscounted) | 116.35 |
| Finance lease payments (undiscounted) | 16.66 |
| Other commitments (remainder of FY) | 2.15 |

Total obligations of **$650.0B** are 4.0x LTM operating cash flow — heavily weighted to multi-year purchase commitments (AI compute, content, logistics capacity). These are largely *demand-contingent* capacity contracts and are arguably a bullish signal about forward demand; but they also convert a flexible cost structure into a fixed one. Operating lease discount rate ticked up to 3.9% from 3.7%, and the operating lease liability rose $7.1B in six months — real-estate/capacity expansion continues.

---

## 8. Insider transactions — NOT AVAILABLE (do not infer)

`get_insider_transactions` returned an explicit data-unavailability response: the B-project package holds **no authorized, point-in-time insider-transactions archive for AMZN by 2026-08-06**. No insider buying, selling, or 10b5-1 activity can be reported, estimated, or implied. Any insider signal must be treated as **unknown** for this analysis. Do not read this as either bullish or bearish confirmation — it is simply absent evidence, and should not be weighted in the trade.

---

## 9. Synthesis: how to trade this

**The bull case (well-evidenced):**
- Revenue +19.6% y/y at ~$800B+ annualised run-rate, i.e. accelerating, with marketing spend flat and G&A down — textbook operating leverage.
- Operating margin +226 bps y/y to 13.69%; H1 at 13.43% vs 11.62%.
- Core EPS growth ~+26% y/y, roughly double what a mature retailer should produce.
- SBC discipline (−1.5% y/y against +18% revenue) and inventory discipline.
- Net cash (ex-leases) ≈ +$29.6B; interest cover >20x; negative 64-day cash conversion cycle.

**The bear case (equally well-evidenced):**
- **FCF is negative**: −$11.6B LTM, −$27.0B in H1. Capex is 107% of CFO and 2.3x D&A.
- **66% of Q2 pre-tax profit and 57% of H1 pre-tax profit is non-operating Level 3 mark-ups.** Reported EPS of $5.75 is ~2.9x core EPS of ~$1.95. This is the highest earnings-quality risk in the data set.
- **Gross debt +93% in six months** ($68.8B → $133.0B); interest expense +155% y/y and set to keep climbing as the new debt seasons.
- Depreciation +44% y/y and accelerating — a locked-in margin headwind.
- AR +30% YTD vs revenue +19.6%, with allowance coverage falling from 3.54% to 3.18%.
- $650B of contractual obligations (4.0x CFO) convert variable costs into fixed costs.
- Current ratio 1.03 and falling; cash fell $23.8B in Q2 alone on acquisitions.

**Concrete, actionable positioning insights:**

1. **Trade the core, not the print.** If AMZN re-rates on GAAP EPS beats, that re-rating is being driven by private-startup marks. A trader should specifically watch for (a) any language on private-stake valuations in the 10-Q/10-K notes, (b) private-AI funding-round sentiment as a direct read-through to AMZN's book value, and (c) the gap between GAAP EPS growth (+242%) and core EPS growth (+27%). A squeeze higher on the optical beat is fadeable; the durable long thesis rests on the 13.7% operating margin.
2. **The single highest-conviction long signal is operating margin, not EPS.** Two consecutive quarters of y/y margin expansion with flat marketing and shrinking G&A is structural. Long thesis is intact *on that basis alone*.
3. **The single highest-conviction short/hedge signal is negative FCF plus $82B of H1 debt issuance.** If capex growth persists at +60% y/y while CFO grows +33%, FCF stays negative indefinitely and the equity becomes a rate/debt-market story. Watch the Q3-2026 10-Q (expected ~late October 2026) for: capex/revenue vs 25.8%, D&A growth vs +44%, and whether debt is tapped again.
4. **Asymmetric risk into Q3 earnings:** the Q2 markup ($50.5B) is not repeatable. Even flat operating trends plus zero mark-ups would produce a massive y/y GAAP EPS *decline* in Q3-2026 versus a marked-up comparable. Expect a mechanically ugly headline with a healthy core — a likely dislocation and a tactical entry point for core-metric buyers.
5. **Do not lean on insider data.** It does not exist in this dataset.
6. **No price or market data was supplied by the tools**, so no valuation multiple, target price, or technical level can be responsibly stated. Position sizing should be driven by the fundamental triggers above, not by assumed price levels.

**Fundamental stance: constructive on operating trajectory, cautious on reported earnings quality and cash-flow profile.** The company is executing exceptionally at the operating line while simultaneously (i) converting itself into a capital-intensive AI infrastructure owner, and (ii) reporting profits increasingly driven by paper gains. Both facts must be held simultaneously.

---

## 10. Key points summary table

| Category | Metric | Value / Finding | Read |
|---|---|---|---|
| **Filing** | Latest 10-Q | Q2-2026, accepted 2026-07-31 (6 days old) | Freshest possible data |
| **Growth** | Q2-2026 revenue (derived) | $200.6B, +19.6% y/y | Accelerating |
| **Growth** | H1-2026 revenue (derived) | $382.1B, +18.2% y/y | Strong |
| **Profitability** | Q2-2026 operating income / margin | $27.46B / 13.69% (+226 bps y/y) | **Bull case** |
| **Profitability** | H1-2026 operating margin | 13.43% vs 11.62% y/y | Broad-based leverage |
| **Leverage proof** | Marketing / G&A / SBC y/y | +2.5% / −6.0% / −1.5% vs revenue +19.6% | Genuine operating leverage |
| **Earnings quality** | Non-operating income Q2-2026 | $53.40B = **66% of pre-tax income** | **Bear case** |
| **Earnings quality** | Private-stake mark-up H1-2026 | $62.81B (Q2: $50.49B, Q1: $12.33B) | Non-cash, Level 3 |
| **Earnings quality** | Reported vs core Q2 EPS | $5.75 vs ≈$1.95 (est.) | ~2.9x gap |
| **Earnings quality** | Core EPS growth H1-2026 | ≈$3.63 vs ≈$2.89, **+25.6%** | Still strong |
| **Balance sheet** | Total assets | $818.0B → $1,095.7B (+33.9% YTD) | Step change |
| **Balance sheet** | Mark-to-market securities | $220.2B = **20.1% of assets** | Valuation-sensitive |
| **Balance sheet** | Gross long-term debt | $68.8B → $133.0B (**+93.2%**) | Aggressive funding |
| **Balance sheet** | Net cash ex-leases | ≈ **+$29.6B** | Adequate |
| **Balance sheet** | Current ratio | 1.033 (from 1.051) | Thinning |
| **Working capital** | Cash conversion cycle | ≈ **−64 days** | Structural advantage |
| **Working capital** | AR vs revenue growth | +30.1% vs +19.6%; allowance coverage 3.54%→3.18% | **Watch item** |
| **Working capital** | Inventory | $38.2B, −0.4% vs +19.6% revenue | Healthy |
| **Cash flow** | LTM operating cash flow | $161.4B, +33.2% y/y | Strong engine |
| **Cash flow** | LTM capex | $173.0B, +60.7% (**107% of CFO**) | **Bear case** |
| **Cash flow** | **LTM free cash flow** | **−$11.6B** (vs +$13.5B prior LTM) | **Negative** |
| **Cash flow** | H1-2026 FCF | −$27.0B | Deteriorating |
| **Cash flow** | H1-2026 gross debt raised | $82.4B vs $18.4B repaid | Funding gap closed with debt |
| **Cash flow** | Q2-2026 acquisitions | $24.36B (H1 $39.77B vs $1.65B prior) | Major M&A step-up |
| **Cash conversion** | Core NI → CFO (H1-2026) | $39.5B → $71.4B = **1.81x** | Excellent quality |
| **Cost trend** | Depreciation y/y Q2-2026 | $19.99B vs $13.87B, **+44.1%** | Locked-in headwind |
| **Cost trend** | Interest expense y/y Q2-2026 | $1.31B vs $0.52B, **+155%** | Rising with debt |
| **Coverage** | Operating income / interest Q2-2026 | 20.9x | Comfortable |
| **Obligations** | Total contractual obligations | $650.0B (4.0x LTM CFO) | Fixed-cost conversion |
| **Obligations** | Due next 12 months | $78.1B | Manageable |
| **Structure** | Operating segments | 3 (per XBRL); no segment detail available | Data gap |
| **Capital return** | Dividends / buybacks | None evidenced in returned tags | No shareholder yield |
| **Dilution** | Shares outstanding | 10,731M → 10,783M (+0.5% in 6M) | Modest |
| **Insiders** | Transactions | **DATA UNAVAILABLE — not inferable** | Do not weight |
| **Next catalyst** | Q3-2026 10-Q | ~late Oct 2026; expect ugly GAAP y/y vs marked-up base | Dislocation risk/opportunity |

---

**Caveats on data:** (1) Revenue is derived (`CostsAndExpenses + OperatingIncomeLoss`), as no direct revenue tag was returned; the identity ties exactly in all four periods. (2) Segment-level revenue/profit, goodwill, intangibles, and explicit revenue tags were not present in the returned XBRL slice. (3) No price, market-cap, or valuation-multiple data was available from these tools. (4) Insider transaction data is explicitly unavailable and has not been estimated. (5) Core-EPS figures are analyst estimates applying each period's effective tax rate to ex-non-operating pre-tax income; they are illustrative, not reported figures.