# AMZN — Fundamental Research Report
**As of 2026-10-01 | Latest filed data: Q2 2026 Form 10-Q (accepted 2026-07-31 02:11 UTC)**

---

## 1. Data Basis & Scope (read first)

- **No new SEC filings in the past week.** The most recent filing in the point-in-time dataset is the June-2026 10-Q filed 2026-07-31. The next fundamental catalyst is Q3 2026 results (typically late October), i.e., *after* today's date.
- **Vendor limitations encountered:** (a) the package does **not** return a revenue XBRL tag, segment-level P&L, retained earnings/stockholders' equity, price, or market cap; (b) annual (10-K) series were **not** available — the annual calls returned the same 10-Q fact set; (c) **insider-transaction data is explicitly unavailable** ("no authorized, point-in-time insider archive for AMZN"). No insider activity is inferred or fabricated below.
- **Revenue is derived** as `CostsAndExpenses + OperatingIncomeLoss`, which reconciles exactly to known prior-year figures (Q2 2025: 148,531 + 19,171 = **$167,702M**, the actual reported figure). Derived values are labeled *(calc)*.
- Company profile details are general knowledge; the only profile fact returned by the tools is **3 reportable operating segments** (XBRL `NumberOfOperatingSegments = 3`), consistent with North America, International, and AWS.

---

## 2. Company Frame

Amazon.com, Inc. (AMZN) is a Seattle-based technology and retail conglomerate operating through three segments: **North America**, **International**, and **Amazon Web Services (AWS)**. Revenue pools include online and third-party marketplace sales, Prime subscriptions, advertising, AWS cloud/AI infrastructure, physical stores, and devices. The 2026 fundamental story is a **triple inflection**: (1) revenue growth re-accelerating toward ~20%, (2) record operating margins, and (3) a historic AI-driven capex and debt-funding cycle — overlaid by a **very large non-cash mark-to-market gain** that distorts headline EPS.

---

## 3. Headline Results — Q2 and H1 2026

*(calc = derived; $ millions)*

| | Q1 2025 | Q2 2025 | H1 2025 | Q1 2026 | Q2 2026 | H1 2026 |
|---|---|---|---|---|---|---|
| Revenue *(calc)* | 155,667 | 167,702 | 323,369 | 181,519 | **200,606** | **382,125** |
| YoY growth | — | — | — | +16.6% | **+19.6%** | **+18.2%** |
| Operating income | 18,405 | 19,171 | 37,576 | 23,852 | **27,461** | **51,313** |
| Operating margin | 11.82% | 11.43% | 11.62% | 13.14% | **13.69%** | **13.43%** |
| Non-operating income | 3,274 | 1,686 | 4,960 | 15,982 | **53,396** | **69,378** |
| Pre-tax income | 21,679 | 20,857 | 42,536 | 39,834 | **80,857** | **120,691** |
| Tax expense (rate) | 4,553 (21.0%) | 2,678 (12.8%) | 7,231 (17.0%) | 9,560 (24.0%) | 18,199 (22.5%) | 27,759 (23.0%) |
| Net income | 17,127 | 18,164 | 35,291 | 30,255 | **62,647** | **92,902** |
| Diluted EPS | 1.59 | 1.68 | 3.27 | 2.78 | **5.75** | **8.53** |

**The single most important fact in this report:** H1 2026 pre-tax income of $120.7B includes **$62.8B of "upward price adjustment" on equity securities without readily determinable fair value** (Q2 alone: $50.5B). This is a **non-cash, model-based revaluation** of a large private equity holding — the vendor does not identify the issuer, though the scale/timing is consistent with a major AI-model-developer stake.

---

## 4. Earnings Quality: Headline vs. Core

| $ millions | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 |
|---|---|---|---|---|
| Upward mark on private equity securities | 49 | **50,486** | 86 | **62,814** |
| After-tax mark (@22.5%/23%) | 38 | **39,126** | 71 | **48,367** |
| Mark contribution to diluted EPS | $0.00 | **≈$3.59** | $0.01 | **≈$4.44** |
| Headline diluted EPS | 1.68 | **5.75** | 3.27 | **8.53** |
| **Core diluted EPS (ex-mark) *(calc)*** | **1.68** | **≈2.16** | **3.27** | **≈4.09** |
| Core EPS growth | — | **+29%** | — | **+25%** |

- **Headline EPS overstates core earnings power by ~2.7x in Q2 and ~2.1x in H1.**
- Core growth of ~25–29% is nonetheless genuinely strong, and is supported by operating income (+43% YoY in Q2), not by accounting.
- **Cash-flow integrity check:** the mark gain is correctly *excluded* from operating cash flow. TTM operating cash flow of $161.4B reconciles with net income $135.3B + D&A $75.2B + deferred tax $41.4B + SBC ~$20.9B − mark gains $62.8B − working-capital uses ~$46.0B. **OCF/NI = 1.19x** — cash earnings are real; the *P&L* is what is distorted.
- Additional non-cash drag: **warrant fair-value losses of $1.45B in Q2** ($1.05B H1 2026).
- **Tax rate normalization is a headwind:** 22.5–23.0% in 2026 vs 12.8% in Q2 2025 (partly tax on unrealized marks and higher pre-tax base). Cash taxes remain light ($2.66B paid in Q2 vs $18.2B expensed), with **$30.5B of deferred tax expense in H1** — non-cash.

---

## 5. Margin & Cost Structure — Where the Leverage Came From

Q2 2026 cost lines as % of revenue (vs Q2 2025):

| Line | Q2 2026 $M | % rev | Q2 2025 % rev | Δ |
|---|---|---|---|---|
| Cost of goods & services | 95,778 | 47.74% | 48.19% | **−45 bp** |
| Fulfillment/tech/content/other *(derived)* | 42,892 | 21.38% | 22.73% | **−135 bp** |
| Marketing | 11,698 | 5.83% | 6.81% | **−98 bp** |
| G&A | 2,788 | 1.39% | 1.77% | **−38 bp** |
| D&A | 19,988 | 9.96% | 9.08% | **+88 bp** |
| **Total costs** | **173,145** | **86.31%** | **88.57%** | **−226 bp** |

**Read-through:** operating margin expansion of **+226 bp to 13.69%** came from genuine operating leverage across COGS, fulfillment, marketing and G&A, *partly offset* by depreciation. D&A grew **+31% YoY** in Q2 ($20.0B vs $15.2B; TTM $75.2B vs $58.6B). With TTM capex at **2.30x TTM D&A**, the depreciation headwind will intensify for several quarters — this is the key margin risk into 2027.

**SBC discipline:** $6.04B in Q2 vs $6.53B prior year (3.0% vs 3.9% of revenue); H1 $10.07B vs $10.22B. Unrecognized SBC $24.8B. Share count 10,783M (Jun 30) vs 10,731M (Dec 31) = **+0.5% dilution** — modest. No buyback outflows appear in the cash flow statement.

---

## 6. Cash Flow & The Capex Super-Cycle

| $ millions | H1 2025 | H1 2026 | TTM (Jul'25–Jun'26) |
|---|---|---|---|
| Operating cash flow | 49,530 | **71,419** | **161,403** |
| Capex (purchases of productive assets) | 57,202 | **98,411** | **173,028** |
| **Free cash flow *(calc)*** | **−7,672** | **−26,992** | **−11,625** |
| Business acquisitions, net of cash | 1,652 | **39,767** | **41,956** |
| Net investing cash flow | −69,227 | −143,457 | −216,775 |
| Net financing cash flow | −2,586 | **+62,913** | **+75,160** |

- **Capex is running at 27.0% of Q2 revenue** ($54.2B in a single quarter; $44.2B in Q1) vs 17.7% of revenue in H1 2025. Annualizing the Q2 run-rate implies ~$217B — versus TTM OCF of $161B. **Negative FCF is structural, not seasonal**, and worsened by ~$19.3B YoY in H1.
- Despite that, **Q2 OCF rose 40% YoY to $45.4B** (22.6% OCF margin) — the core engine is funding most of the build.
- **$39.8B of cash M&A in H1 2026** (vs $1.65B a year ago; $24.4B in Q2 alone) is a major capital-allocation shift. The fact set does not name the target(s) — this **must be verified in the 10-Q business-combination note** before underwriting.
- Financing inflows reconcile almost entirely to debt: TTM long-term debt issued **$81.9B**, short-term borrowings **$20.8B**, repayments $25.7B, finance-lease principal $1.6B.

---

## 7. Balance Sheet — Doubling Down with Debt

| $ millions | 2025-12-31 | 2026-06-30 | Change |
|---|---|---|---|
| Cash & equivalents | 86,810 | 78,213 | −9.9% |
| Available-for-sale debt securities | 45,800 | **97,900** | +113.8% |
| Accounts receivable | 67,729 | **88,092** | **+30.1%** |
| Inventory | 38,325 | 38,184 | −0.4% |
| Total current assets | 229,083 | 249,264 | +8.8% |
| **Total assets** | **818,042** | **1,095,689** | **+33.9%** |
| Accounts payable | 121,909 | **147,440** | +21.0% |
| Long-term debt (incl. current) | 68,836 | **132,995** | **+93.2%** |
| Finance lease liabilities | 12,286 | 13,451 | +9.5% |
| Operating lease liabilities | 89,252 | 96,320 | +7.9% |
| Equity securities w/o readily determinable FV | 16,200 | **122,300** | **+655%** |
| AOCI | 28,230 | 66,287 | **+38,057** |
| Total current liabilities | 218,005 | 241,274 | +10.7% |

**Key observations**

1. **The $277.6B asset increase is dominated by two non-operating items:** the private equity stake (+$106.1B) and AFS securities (+$52.1B). Only ~$20B is receivables growth.
2. **Debt nearly doubled in six months** (+$64.2B). Total debt + finance leases rose from **$81.1B to $146.4B (+81%)**. Adding operating leases, total obligations are **$242.8B** vs $170.4B.
3. **Net cash position is shrinking fast but still positive:** cash + AFS ($176.1B) minus debt + finance leases ($146.4B) = **net cash of $29.7B**, down from $51.4B at year-end. Including operating leases, **net debt is $66.7B** (from $37.9B).
4. **Liquidity is high quality:** $96.5B of the $97.9B AFS portfolio matures within one year. Current ratio is thin at **1.03x** ($249.3B / $241.3B) but backed by $176B of liquid assets.
5. **Working-capital efficiency improved:** inventory flat (−0.4%) against +18% H1 revenue; payables +21% (supplier/vendor financing, ~140 days of COGS). **Receivables +30%, however, outpace revenue growth** — worth monitoring for ad/AWS billing and credit quality (allowance rose to $2.8B from $2.4B).
6. **AOCI jumped +$38.1B**, far more than the −$1.56B FX translation loss, implying mark-to-market gains routed through OCI. The fact set does not cleanly identify the source (AFS unrealized position is only a $67M loss) — **flag for verification**; this is a second, quieter equity boost of non-cash origin.
7. **Contractual obligations total $650.0B** at 6/30/26: $42.8B remainder of FY26, $78.1B due within 12 months, $53.4B year 2, $46.8B year 3, $42.2B year 4. This is a very large forward commitment book (consistent with AI/data-center capacity, chips, content and leases) — a demand bet as much as a financing obligation.
8. **Interest coverage remains comfortable:** Q2 operating income $27.5B / interest expense $1.31B = **20.9x**. But interest expense rose **+155% YoY** in Q2 ($1.31B vs $0.52B), and interest income ($1.30B) only just offsets it.

*Stockholders' equity could not be computed — the vendor omitted retained earnings and the `StockholdersEquity` tag. Book value is nonetheless up materially from H1 net income (+$92.9B) and AOCI (+$38.1B).*

---

## 8. Insider Transactions

**DATA UNAVAILABLE.** The vendor's news/fundamentals package has no authorized, point-in-time insider-transaction archive for AMZN as of 2026-10-01. Per instruction, no insider buying or selling is inferred. Treat this as a **research gap, not a signal** — do not read the absence of data as either bullish or bearish. Insiders should be checked directly via Form 4 filings before sizing a position.

---

## 9. Valuation Perspective (without price data)

The package contains **no share price or market cap**, so multiples cannot be computed here. What can be provided is the earnings basis a trader should use:

- **TTM GAAP diluted EPS ≈ $12.42** (TTM net income $135.3B ÷ ~10.9B diluted shares) — inflated.
- **Estimated TTM core EPS ≈ $7.9–8.0** after removing after-tax mark gains.
- Applying a market multiple to the *headline* number would make the stock look **~55% cheaper than it is on core earnings**. Any screen or model keyed to trailing GAAP P/E is mis-specified for AMZN this year.
- The private equity stake carries **$122.3B, or ~$11.22/share pre-tax** (~$8.7/share after tax) of balance-sheet value — optionality that is *not* in operating earnings, but which can reverse.

---

## 10. Risks & Catalysts

**Bear/risk case**
1. **Mark-to-market reversal:** a down-round or valuation reset on the $122.3B private holding would hit EPS directly — every **10% markdown ≈ $12.2B pre-tax ≈ $1.12/share**.
2. **FCF compression:** annualized capex (~$217B) exceeds TTM OCF ($161B); continued debt issuance is likely, and leverage has already risen ~81% in six months.
3. **Depreciation drag:** capex/D&A at 2.3x implies D&A growth of 25–30%+, a persistent 100–250 bp margin headwind.
4. **$650B of contractual obligations** against $176B of liquid assets — an aggressive demand assumption.
5. **Receivables +30% vs revenue +18%** and a rising allowance; watch collections.
6. **Tax rate normalization** (12.8% → 22.5%) and rising interest expense (+155%).
7. **Concentration/opacity:** no segment disclosure in this dataset, and a 12%-of-assets private valuation that is model-based.

**Bull case**
1. **Revenue acceleration** (+19.6% in Q2 vs +16.6% in Q1), broad-based.
2. **Operating margin at 13.69%**, +226 bp YoY, with operating income +43%.
3. **SBC flat and dilution only +0.5%** — margin gains are not being paid for in stock.
4. **Inventory flat on +18% revenue** — genuine efficiency.
5. **OCF +40% YoY in Q2**, OCF/NI 1.19x — high cash conversion.
6. **Net cash of $29.7B** ex-leases, 20.9x interest coverage, $96.5B of AFS maturing within a year.
7. **Embedded optionality** in the $122.3B private stake.

---

## 11. Actionable Conclusions

1. **Do not underwrite AMZN on headline EPS or trailing P/E.** Use core EPS (~$2.16 in Q2, ~$4.09 in H1, ~$8 TTM). The GAAP number is ~2x core because of a non-cash private-company revaluation.
2. **The operating business is genuinely inflecting positively.** Revenue +19.6%, operating margin +226 bp, operating income +43%, SBC flat. This is the strongest part of the report and supports a constructive fundamental stance.
3. **The cash-flow story has inverted.** FCF is **−$27.0B in H1 2026** and **−$11.6B TTM**. Anyone using FCF-based valuation or dividend/buyback screens will misprice AMZN. The correct framing is *investment-cycle* earnings: capex 27% of revenue, D&A set to compound.
4. **Monitor the debt trajectory quarterly.** +$64.2B of long-term debt in six months and $650B of contractual obligations imply further issuance. Watch the interest-expense line (+155% YoY) and any change in short-term commercial paper usage.
5. **Scrutinize the $39.8B of H1 M&A and the $43B of equity-securities additions.** The fact set gives no counterparty or rationale. This is the single biggest disclosure gap and should be resolved from the 10-Q notes before adding exposure.
6. **Verify the $38.1B AOCI increase** — it is too large to be FX and appears to be an OCI mark; it flatters book value if non-cash.
7. **Positioning takeaway:** fundamentals support a **constructive/accumulate-on-weakness** stance on the *operating* franchise, but with **reduced confidence in reported EPS and FCF**, and a clear catalyst calendar: Q3 2026 print (late Oct) for capex guide, FCF, mark stability, receivables, and debt. Insiders cannot be assessed — obtain Form 4 data independently.

---

## 12. Key Points Summary

| Category | Metric / Point | Value | Change | Read-through |
|---|---|---|---|---|
| **Reporting** | Latest filing | Q2 2026 10-Q, filed 2026-07-31 | No new filings this week | Q3 print (late Oct) is next catalyst |
| **Growth** | Q2 2026 revenue *(calc)* | $200.6B | +19.6% YoY | Re-acceleration from +16.6% in Q1 |
| **Growth** | H1 2026 revenue *(calc)* | $382.1B | +18.2% YoY | Broad-based scale |
| **Profitability** | Q2 operating income / margin | $27.5B / 13.69% | +43.2% YoY / +226 bp | Real operating leverage |
| **Profitability** | H1 operating margin | 13.43% | +181 bp | Best-in-class for AMZN |
| **Earnings quality** | H1 private-equity mark gain | $62.8B pre-tax ($50.5B in Q2) | vs $0.09B H1 2025 | **Non-cash; 52% of pre-tax income** |
| **Earnings quality** | Q2 headline vs core EPS | $5.75 vs ≈$2.16 | +242% vs +29% YoY | Headline overstates by ~2.7x |
| **Earnings quality** | H1 headline vs core EPS | $8.53 vs ≈$4.09 | +161% vs +25% | Core growth still healthy |
| **Cash flow** | Q2 operating cash flow | $45.4B (22.6% margin) | +39.6% YoY | Cash engine intact |
| **Cash flow** | H1 free cash flow *(calc)* | **−$27.0B** | vs −$7.7B H1 2025 | Capex super-cycle |
| **Cash flow** | TTM FCF *(calc)* | **−$11.6B** | — | FCF-based screens mislead |
| **Capex** | Q2 capex | $54.2B (27.0% of revenue) | +68% YoY | Annualized ~$217B vs $161B TTM OCF |
| **Capex** | TTM capex / TTM D&A | $173.0B / $75.2B = 2.30x | D&A +31% YoY | Rising depreciation headwind |
| **M&A** | H1 2026 business acquisitions | $39.8B ($24.4B in Q2) | vs $1.65B H1 2025 | Target undisclosed — verify |
| **Balance sheet** | Total assets | $1,095.7B | +33.9% YTD | Driven by stake + securities |
| **Balance sheet** | Long-term debt | $133.0B | +93.2% YTD | Debt-funded expansion |
| **Balance sheet** | Private equity stake (no ready FV) | $122.3B (11.2% of assets) | from $16.2B | Source of EPS volatility |
| **Balance sheet** | Cash + AFS securities | $176.1B | +$43.6B | $96.5B matures <1 yr |
| **Leverage** | Net cash ex-leases / net debt incl. leases | +$29.7B / −$66.7B | from +$51.4B / −$37.9B | Still solid, deteriorating fast |
| **Leverage** | Q2 interest coverage | 20.9x | interest expense +155% | Adequate but watch |
| **Obligations** | Total contractual obligations | $650.0B | $78.1B due <12 mo | Long-dated AI/capacity bet |
| **Efficiency** | Inventory | $38.2B | −0.4% vs +18% revenue | Strong working capital |
| **Efficiency** | Receivables | $88.1B | +30.1% YTD | Outpacing revenue — monitor |
| **Capital return** | Buybacks / dividends | None evident in H1 cash flow | Shares +0.5% YTD | All cash to capex/M&A |
| **Insider** | Form 4 activity | **DATA UNAVAILABLE** | — | Research gap, not a signal |
| **Valuation** | TTM GAAP EPS vs core EPS | ≈$12.42 vs ≈$7.9–8.0 | — | Headline P/E understates multiple ~55% |
| **Bottom line** | Stance | Constructive on operations; skeptical of GAAP EPS/FCF | — | Accumulate on weakness; verify M&A, marks, AOCI |