# AMZN — Fundamental Research Report
**As of 2026-10-02 | Latest reported period: Q2 2026 (quarter ended 2026-06-30), 10-Q accepted 2026-07-31**

---

## 1. Executive Summary

AMZN enters Q4 2026 with **exceptional operating momentum but deteriorating free cash flow and a dramatically levered balance sheet**. Q2 2026 revenue reached **$200.6B (+19.6% YoY)**, operating income **$27.5B (+43.2% YoY)**, and operating margin **13.7% (+226 bps YoY)** — the strongest growth/margin combination in the dataset. However, **62% of Q2 pre-tax income came from a non-cash upward revaluation of non-marketable equity securities** ($50.5B), inflating GAAP EPS to $5.75 versus an estimated **~$2.16 core EPS**.

The company is in the middle of an extraordinary AI/cloud capital cycle: **H1 2026 capex of $98.4B (+72% YoY)**, TTM capex **$173.0B**, TTM free cash flow **–$11.6B**. This is being funded with debt — **long-term debt rose 93% in six months to $133.0B** — while purchase obligations hit **$650.0B** (including $78.1B due within 12 months).

**Stance: Fundamentally constructive / accumulate on weakness, but do not chase headline GAAP EPS.** The operating business is compounding faster than costs; the accounting earnings are noisy and the cash-flow/leverage trajectory warrants disciplined position sizing.

---

## 2. Data Provenance & Limitations (Important)

- Data is **point-in-time SEC XBRL** filtered by EDGAR acceptance time. Latest filing is the **Q2 2026 10-Q (accession 0001018724-26-000026)**.
- Revenue is **not directly tagged** in the extract; it is derived as `CostsAndExpenses + OperatingIncomeLoss` and reconciles exactly across periods (e.g., Q2 2026: 173,145 + 27,461 = 200,606).
- The "annual" statement tools returned the **same 2025–2026 quarterly facts**, not FY2022–FY2024 history. Multi-year history below is therefore **derived from trailing-period arithmetic**, not independently reported annual statements.
- **Segment-level revenue, AWS growth, advertising revenue, and backlog are not in the dataset.** Three reportable segments are confirmed (`NumberOfOperatingSegments = 3`).
- **Insider transactions are unavailable** — the vendor has no authorized point-in-time archive for AMZN. This is a data gap, not evidence of zero activity. Do not infer insider sentiment.
- No share price, market cap, or consensus estimates are available, so **no valuation multiples or price targets are presented**.
- Some XBRL tags are internally inconsistent (e.g., AOCI +$38.1B vs. negligible AFS unrealized gains). The report relies on primary aggregates (assets, cash, debt, equity securities, income statement) and flags where composition is unclear.

---

## 3. Company Profile

**Amazon.com, Inc. (Nasdaq: AMZN)** — founded 1994, headquartered in Seattle. The world's largest e-commerce marketplace and largest cloud infrastructure provider, operating through **three reportable segments**:

1. **North America** — online and physical stores, third-party marketplace commissions, Fulfillment by Amazon, Prime subscriptions, advertising, and devices.
2. **International** — the same commerce and advertising stack across Europe, Asia, and other geographies, generally at lower margins than North America.
3. **Amazon Web Services (AWS)** — cloud compute, storage, databases, analytics, networking, and AI/ML services; the primary profit engine and the focus of the current capex cycle.

Additional high-margin revenue streams include **advertising** (increasingly material), **subscription services (Prime)**, **Amazon Prime Video/Music/Games**, and **logistics-as-a-service**. Leadership: CEO Andy Jassy; Executive Chairman Jeff Bezos. The company is founder-influenced but has a single share class and no dual-class control structure.

The current fundamental story is a **retail margin recovery + AWS/AI reinvestment** combination: retail profitability is funding, and debt is supplementing, a historic build-out of AI data-center capacity.

---

## 4. Income Statement — Q2 and H1 2026

All figures **$M** unless noted. Q2 = Apr–Jun; H1 = Jan–Jun.

| Line item | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | 200,606 | 167,702 | **+19.6%** | 382,125 | 323,369 | **+18.2%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 183,241 | 157,785 | +16.1% |
| **Gross profit** | **104,828** | **86,893** | **+20.6%** | **198,884** | **165,584** | **+20.1%** |
| Gross margin | 52.3% | 51.8% | +46 bps | 52.0% | 51.2% | +85 bps |
| Marketing expense | 11,698 | 11,416 | +2.5% | 22,012 | 21,179 | +3.9% |
| G&A expense | 2,788 | 2,965 | –6.0% | 5,375 | 5,593 | –3.9% |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 330,812 | 285,793 | +15.8% |
| **Operating income** | **27,461** | **19,171** | **+43.2%** | **51,313** | **37,576** | **+36.6%** |
| **Operating margin** | **13.7%** | **11.4%** | **+226 bps** | **13.4%** | **11.6%** | **+181 bps** |
| Interest income | 1,295 | 1,085 | +19.4% | 2,430 | 2,151 | +13.0% |
| Interest expense | 1,314 | 516 | **+154.7%** | 2,114 | 1,057 | **+100.0%** |
| Non-operating income, net | 53,396 | 1,686 | +3,067% | 69,378 | 4,960 | +1,299% |
| Pre-tax income | 80,857 | 20,857 | +287.7% | 120,691 | 42,536 | +183.7% |
| Income tax expense | 18,199 | 2,678 | +579.6% | 27,759 | 7,231 | +283.9% |
| Effective tax rate | 22.5% | 12.8% | — | 23.0% | 20.5% | — |
| **Net income** | **62,647** | **18,164** | **+244.9%** | **92,902** | **35,291** | **+163.2%** |
| Net margin | 31.2% | 10.8% | — | 24.3% | 10.9% | — |
| **Diluted EPS** | **$5.75** | **$1.68** | **+242.3%** | **$8.53** | **$3.27** | **+160.9%** |
| Diluted shares (implied) | ~10,895 | ~10,812 | +0.8% | ~10,891 | ~10,793 | +0.9% |
| SBC expense | 6,038 | 6,534 | –7.6% | 10,070 | 10,223 | –1.5% |
| D&A expense | 19,988 | 15,227 | +31.3% | 38,933 | 29,489 | +32.0% |

**Derived Q1 2026 (for trend context):** revenue $181,519M (+16.6% YoY), operating income $23,852M, operating margin 13.1%, net income $30,255M, diluted EPS $2.78.

**Key observations:**

- **Revenue growth accelerated through the half** (+16.6% → +19.6%), with Q2 the fastest quarter in the dataset. Q2 annualized revenue run-rate is **~$802B**.
- **Cost discipline is real:** total costs grew 16.6% versus 19.6% revenue growth; marketing grew only 2.5% and G&A declined 6.0%. SBC fell 7.6% YoY.
- **Gross margin expansion (+46 bps)** plus operating leverage drove a **226 bps** operating margin gain. Q2 annualized operating income run-rate is **~$110B**.
- **D&A is ramping hard (+31% YoY, 10.0% of revenue vs. 9.1%)** — the leading edge of depreciation from the capex surge. This is the key margin headwind for coming quarters.

---

## 5. Quality of Earnings — The $50B Mark-to-Market Issue

This is the single most important analytical adjustment for traders.

| Item | Q2 2026 | H1 2026 |
|---|---:|---:|
| Reported pre-tax income | 80,857 | 120,691 |
| Upward revaluation of non-marketable equity securities | 50,486 | 62,814 |
| % of pre-tax income | **62.4%** | **52.0%** |
| Non-operating income, net | 53,396 | 69,378 |

- The company carries **$122.3B of equity securities without readily determinable fair value**, up from **$16.2B at 2025-12-31 (+655%)**. The H1 upward price adjustment of **$62.8B** flows through non-operating income and net income but is **entirely non-cash and subject to reversal**.
- The remaining increase (~$43B) reflects **new equity investment purchases**, consistent with the investing cash-flow line and the $39.8B of H1 acquisition payments.
- **Core EPS estimate (excluding non-marketable equity revaluations only):**

| Metric | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Reported diluted EPS | $5.75 | $1.68 | +242% | $8.53 | $3.27 | +161% |
| **Core diluted EPS (est.)** | **~$2.16** | **$1.68** | **+29%** | **~$4.09** | **$3.27** | **+25%** |

**Implication:** Operating earnings are genuinely strong (+29% core EPS), but **headline EPS overstates run-rate profitability by ~2.7x in Q2**. A future reversal of these marks could produce a large GAAP "miss" with no change in the operating business — and vice versa. Traders should anchor on **operating income, operating margin, and AWS/retail segment profit**, not GAAP EPS.

**Additional quality flags:**
- **Deferred tax expense of $30.5B in H1** versus cash taxes paid of only **$4.0B**. Book income is running well ahead of taxable income, likely due to unrealized gains and accelerated depreciation. Future cash tax normalization is a risk.
- **Effective tax rate rose to 23.0%** (from 20.5%), a headwind that partially offsets operating strength.
- **TTM net income of $135.3B** includes an unknown amount of H2 2025 marks; it is not a clean earnings base.

---

## 6. Balance Sheet — Explosive Expansion and Rapid Leverage

All figures **$M**. Comparison: 2025-12-31 → 2026-06-30.

| Balance sheet item | 2025-12-31 | 2026-06-30 | Change | % |
|---|---:|---:|---:|---:|
| Cash & equivalents | 86,810 | 78,213 | –8,597 | –9.9% |
| Available-for-sale securities | 45,800 | 97,900 | +52,100 | +113.8% |
| Accounts receivable, net | 67,729 | 88,092 | +20,363 | +30.1% |
| Inventory, net | 38,325 | 38,184 | –141 | –0.4% |
| **Current assets** | **229,083** | **249,264** | **+20,181** | **+8.8%** |
| Equity securities w/o readily determinable FV | 16,200 | 122,300 | +106,100 | **+655%** |
| Operating lease ROU assets | 86,054 | 92,743 | +6,689 | +7.8% |
| **Total assets** | **818,042** | **1,095,689** | **+277,647** | **+33.9%** |
| Accounts payable | 121,909 | 147,440 | +25,531 | +20.9% |
| Accrued liabilities | 75,520 | 73,406 | –2,114 | –2.8% |
| **Current liabilities** | **218,005** | **241,274** | **+23,269** | **+10.7%** |
| Long-term debt (total) | 68,836 | 132,995 | +64,159 | **+93.2%** |
| — of which current | 2,748 | 3,330 | +582 | +21.2% |
| — of which non-current | 65,648 | 128,894 | +63,246 | +96.3% |
| Finance lease liabilities | 12,286 | 13,451 | +1,165 | +9.5% |
| Operating lease liabilities | 89,252 | 96,320 | +7,068 | +7.9% |
| AOCI | 28,230 | 66,287 | +38,057 | +134.8% |
| Additional paid-in capital | 140,024 | 149,619 | +9,595 | +6.9% |
| Shares outstanding (M) | 10,731 | 10,783 | +52 | +0.5% |

**Liquidity & solvency metrics (2026-06-30):**

| Metric | Value |
|---|---:|
| Cash + AFS securities | **$176.1B** |
| Current ratio | **1.03x** |
| Quick ratio (cash + AFS + AR) / current liabilities | 1.10x |
| (Cash + AFS) / current liabilities | 0.73x |
| Long-term debt / (cash + AFS) | 0.76x |
| (LT debt + finance leases) / (cash + AFS) | 0.83x |
| (LT debt + all leases) / (cash + AFS) | **1.38x** |
| Interest coverage (Q2 operating income / interest expense) | **20.9x** |
| Interest coverage (H1) | 24.3x |

**Interpretation:**

- **Still investment-grade strong, but levering fast.** $176B of liquid assets comfortably covers $133B of long-term debt, and interest coverage is ~21x. However, debt nearly doubled in six months and interest expense more than doubled YoY.
- **Total fixed obligations are larger than they appear:** $133.0B LT debt + $13.5B finance leases + $96.3B operating leases = **~$242.8B**, versus $176.1B of liquid assets. The $122.3B equity stake is a genuine asset but is illiquid and mark-to-model.
- **Working capital is a cash-flow crutch:** payables rose $25.5B (+20.9%) while inventory was flat and revenue grew 18%. Estimated **AP days ~140**, **inventory days ~36**, **DSO ~40**, giving a **negative cash conversion cycle of roughly –64 days**. This is a structural strength but offers limited incremental benefit if growth slows.
- **Receivables +30%** outpaced revenue growth; worth monitoring for advertising/AWS billing mix or collection quality (allowance rose from $2.4B to $2.8B).
- **Total assets crossed $1.1 trillion**, up 33.9% in six months — driven by the equity stake (+$106B), AFS securities (+$52B), capex, and acquisitions.

---

## 7. Cash Flow — The Core Debate

All figures **$M**.

| Cash flow item | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | TTM Jun-26 | TTM Jun-25 |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash flow | 45,387 | 32,515 | 71,419 | 49,530 | **161,403** | 121,137 |
| Capital expenditures | 54,208 | 32,183 | 98,411 | 57,202 | **173,028** | 107,656 |
| **Free cash flow** | **(8,821)** | **332** | **(26,992)** | **(7,672)** | **(11,625)** | **13,481** |
| Acquisitions, net of cash | 24,359 | 1,700 | 39,767 | 1,652 | 41,956 | 4,809 |
| Purchases of marketable securities | 26,006 | 17,797 | 49,262 | 31,130 | 72,902 | 46,731 |
| Proceeds from sale/maturity of securities | 24,196 | 11,441 | 41,882 | 19,178 | 67,090 | 30,924 |
| Net investing cash flow | (79,245) | (39,424) | (143,457) | (69,227) | (216,775) | (123,569) |
| Net financing cash flow | 10,146 | (2,539) | 62,913 | (2,586) | 75,160 | (8,652) |
| LT debt issued | 13,557 | 0 | 66,998 | 746 | 81,925 | 746 |
| LT debt repaid | (2,752) | (2,751) | (2,752) | (2,751) | (5,022) | (7,434) |
| ST debt issued | 9,368 | 2,093 | 15,386 | 3,908 | 20,798 | 8,187 |
| D&A | 19,988 | 15,227 | 38,933 | 29,489 | 75,200 | 58,562 |
| Cash taxes paid | 2,655 | 4,761 | 3,978 | 5,638 | 6,635 | 11,788 |

**Derived FY2025 figures** (TTM Jun-26 less H1 2026 plus H1 2025; assumes no restatements):

| Metric | FY2025 (derived) |
|---|---:|
| Operating cash flow | ~$139.5B |
| Capital expenditures | ~$131.8B |
| **Free cash flow** | **~$7.7B** |
| Net income | ~$77.7B |

**Interpretation:**

- **Operating cash flow is booming (+44% H1, +33% TTM), but capex is consuming all of it and more.** FCF swung from **+$13.5B** (TTM Jun-25) to **+$7.7B** (FY25 derived) to **–$11.6B** (TTM Jun-26).
- **Q2 annualized capex is ~$217B** — roughly 27% of revenue. H1 capex was **1.38x operating cash flow**.
- **Capex is 2.3x TTM D&A**, meaning the asset base is still growing rapidly; depreciation will keep accelerating for several quarters even if capex plateaus tomorrow.
- **The funding mix has shifted decisively to debt:** $67.0B of LT debt and $15.4B of ST debt issued in H1, versus $2.8B and $15.7B repaid respectively. Net financing inflow of **$62.9B**.
- **Acquisitions jumped to $39.8B in H1** (vs. $1.7B in H1 2025), plus ~$43B of equity investments — a large, non-routine deployment of capital that complicates organic comparisons.
- **Cash taxes are remarkably low ($4.0B H1 vs. $27.8B tax expense)**, flattering FCF relative to true economic taxes. Normalization would make FCF look worse.

---

## 8. Off-Balance-Sheet Commitments — The $650B Question

| Contractual obligation | 2026-06-30 |
|---|---:|
| **Total** | **$650,034M** |
| Due in remainder of fiscal year | $42,752M |
| Due in next 12 months | **$78,084M** |
| Due in year 2 | $53,406M |
| Due in year 3 | $46,767M |
| Due in year 4 | $42,219M |
| Due beyond year 4 (derived) | **~$429.6B** |

- The **near-term obligation jumped from $46.5B at 2026-03-31 to $78.1B at 2026-06-30 (+68% q/q)**.
- The **$429.6B long-dated tail** is the clearest quantitative signal of multi-year AI/cloud capacity, energy, and chip commitments. It supports the demand narrative but creates substantial fixed-cost operating leverage — in both directions.
- Finance lease payments total **$16.7B undiscounted** (liability $13.5B); operating lease payments **$116.4B undiscounted** (liability $96.3B).

**Trading read:** This is either (a) evidence of contracted AI demand that de-risks the capex, or (b) a massive fixed-cost bet that punishes margins if demand softens. The market will likely reward visible backlog conversion and punish any slowdown in AWS growth.

---

## 9. Financial History & Trend Summary

Because the vendor returned only 2025–2026 facts, the usable history is short but directionally clear:

| Period | Revenue | Op income | Op margin | Net income | Diluted EPS | OCF | Capex | FCF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Q1 2025 | 155,667 | 18,405 | 11.8% | 17,127* | $1.59* | 17,015 | 25,019 | (8,004) |
| Q2 2025 | 167,702 | 19,171 | 11.4% | 18,164 | $1.68 | 32,515 | 32,183 | 332 |
| H1 2025 | 323,369 | 37,576 | 11.6% | 35,291 | $3.27 | 49,530 | 57,202 | (7,672) |
| FY2025 (derived) | n/a | n/a | n/a | ~77,670 | n/a | ~139,514 | ~131,819 | ~7,695 |
| Q1 2026 | 181,519 | 23,852 | 13.1% | 30,255* | $2.78* | 26,032 | 44,203 | (18,171) |
| Q2 2026 | 200,606 | 27,461 | 13.7% | 62,647 | $5.75 | 45,387 | 54,208 | (8,821) |
| H1 2026 | 382,125 | 51,313 | 13.4% | 92,902 | $8.53 | 71,419 | 98,411 | (26,992) |
| TTM Jun-26 | n/a | n/a | n/a | 135,281 | n/a | 161,403 | 173,028 | (11,625) |

\*Derived as H1 minus Q2. All $M except EPS.

**Trend conclusions:**
1. **Revenue growth is accelerating** (16.6% → 19.6%) and gross margin is expanding.
2. **Operating margin has stepped up ~180–230 bps YoY** and is holding above 13%.
3. **Net income/EPS are increasingly distorted** by investment marks, especially in 2026.
4. **Capex intensity has roughly doubled** (from ~17–19% of revenue in H1 2025 to ~26–27% in Q2 2026).
5. **FCF has gone from positive to structurally negative** over the trailing year.

---

## 10. Insider Transactions

**No data available.** The vendor explicitly reports no authorized point-in-time insider-transactions archive for AMZN as of 2026-10-02. No insider buying or selling is inferred or fabricated. Traders should treat this as a missing input and rely on SEC Form 4 filings directly if insider behavior is part of the thesis.

---

## 11. Fundamental Scorecard

### Strengths
- **Revenue +19.6% at ~$800B annualized scale** — extraordinary for a company this size.
- **Operating income +43%** with **226 bps of margin expansion**; marketing and G&A growing well below revenue.
- **Negative cash conversion cycle (~–64 days)** and flat inventory despite double-digit growth — best-in-class working capital.
- **$176B liquid assets** and **21x interest coverage** — balance sheet remains strong despite rapid debt growth.
- **SBC discipline** (–1.5% H1) and minimal share count growth (+0.5%).
- **$122B equity portfolio** provides optionality/hidden value (though illiquid and mark-to-model).
- **$650B contractual commitments** imply multi-year demand visibility for AI/cloud capacity.

### Risks / Red flags
- **Negative TTM FCF (–$11.6B)** and H1 FCF of –$27.0B; capex at 27% of revenue and 1.38x OCF.
- **Long-term debt +93% in six months** to $133.0B; interest expense +155% YoY. More issuance likely if capex persists.
- **62% of Q2 pre-tax income from non-cash equity marks** — high earnings volatility and reversal risk.
- **Depreciation +31–42% YoY** and capex at 2.3x D&A — margin headwind building into 2027.
- **Deferred taxes $30.5B vs. cash taxes $4.0B** — future cash tax normalization risk.
- **Purchase obligations $650B**, with near-term obligations up 68% q/q — fixed-cost leverage cuts both ways.
- **Current ratio 1.03x** — thin on a reported basis, reliant on payables and securities.
- **$39.8B H1 acquisitions** — integration and impairment risk; reduced comparability.
- **No insider data** — one less corroborating signal.

---

## 12. Actionable Trading Insights

**Overall stance: Constructive / Overweight bias on operating fundamentals; buy weakness, don't chase GAAP EPS strength.**

1. **Trade the operating line, not the net income line.** Q2 core EPS is ~$2.16 vs. $5.75 reported. If the stock reacts to a headline EPS beat driven by equity marks, fade it; if it sells off on a mark-driven "miss" while operating income and margin hold, treat it as an entry opportunity.

2. **Watch operating margin for the first sign of capex digestion.** The bull case requires margin to hold ≥13% while depreciation accelerates. A drop below ~12.5% despite double-digit revenue growth would signal the capex cycle is outrunning returns.

3. **FCF inflection is the re-rating catalyst.** TTM FCF is –$11.6B. Any guidance implying capex plateau (or AWS revenue acceleration that improves capex productivity) would be strongly positive. Conversely, another upward revision to capex without matching revenue visibility is a sell signal.

4. **Monitor leverage quarterly.** LT debt at $133B and rising; interest expense at a $5.3B annualized run-rate in Q2. If LT debt exceeds ~$160–170B without FCF turning positive, credit and equity risk premia should widen.

5. **Treat the $122B equity stake as a separate, volatile asset.** It is ~11% of total assets and drives GAAP earnings. Any disclosed markdown would hit EPS hard; any IPO/monetization would be a windfall. Size positions for this binary.

6. **Near-term event risk is high.** The next quarterly report (typically late October, not confirmed by tools) will likely feature: strong revenue, strong operating income, noisy EPS, negative FCF, and updated capex guidance. Expect elevated implied volatility around the print.

7. **Confirm demand with segment data.** This dataset does **not** include AWS growth, advertising revenue, or backlog. Before adding, pull the Q2 2026 10-Q/earnings release to verify that AWS growth and advertising are accelerating — the capex thesis depends on it.

8. **Position sizing:** Given negative FCF, doubling debt, and $650B of commitments, a full-size momentum position is not warranted despite excellent operating momentum. A core position with room to add on capex/FCF clarity is the better risk-adjusted expression.

---

## 13. Key Points Summary Table

| Category | Key data / evidence | Implication for traders |
|---|---|---|
| **Identity** | Amazon.com, Inc. (AMZN); 3 reportable segments confirmed (North America, International, AWS) | Large-cap e-commerce + cloud + advertising compounder |
| **Q2 2026 revenue** | $200.6B, +19.6% YoY; H1 $382.1B, +18.2% | Growth accelerated; ~$802B annualized run-rate |
| **Q2 operating income** | $27.5B, +43.2% YoY; margin 13.7% (+226 bps) | Operating leverage is real and broadening |
| **Cost discipline** | Total costs +16.6% vs revenue +19.6%; marketing +2.5%; G&A –6.0%; SBC –7.6% | Margin expansion is driven by efficiency, not just mix |
| **Q2 GAAP EPS** | $5.75, +242% YoY | Headline number is heavily distorted |
| **Core EPS (est.)** | ~$2.16 Q2 (+29% YoY); ~$4.09 H1 (+25%) | Underlying earnings power is strong but ~2.7x lower than reported |
| **Earnings quality** | $50.5B Q2 / $62.8B H1 non-cash upward revaluation of non-marketable equity; 62%/52% of pre-tax income | High reversal risk; anchor on operating income |
| **Equity portfolio** | $122.3B non-marketable equity securities, up from $16.2B at Dec-25 (+655%) | Hidden asset and major EPS volatility source; illiquid |
| **Capex** | Q2 $54.2B (+68% YoY); H1 $98.4B (+72%); TTM $173.0B; ~27% of revenue | Historic AI/cloud build-out; depresses FCF |
| **Free cash flow** | Q2 –$8.8B; H1 –$27.0B; TTM –$11.6B vs. +$13.5B prior TTM | FCF has structurally deteriorated; key bear argument |
| **Operating cash flow** | Q2 $45.4B (+40%); H1 $71.4B (+44%); TTM $161.4B (+33%) | Cash generation from operations remains excellent |
| **Debt** | LT debt $133.0B, +93.2% in six months; $67.0B LT + $15.4B ST issued in H1 | Rapid releveraging to fund capex/acquisitions |
| **Interest** | Q2 $1.31B, +155% YoY; coverage 20.9x | Manageable now, but rising fast |
| **Liquidity** | Cash + AFS $176.1B; current ratio 1.03x; (cash+AFS)/CL 0.73x | Ample buffer, thin reported current ratio |
| **Leases** | Operating $96.3B + finance $13.5B liabilities; undiscounted payments $133.1B | Fixed obligations broader than debt headlines |
| **Commitments** | $650.0B total; $78.1B due within 12 months (+68% q/q); ~$429.6B beyond year 4 | Demand visibility vs. fixed-cost risk |
| **Working capital** | AP +$25.5B (+20.9%); inventory flat; negative CCC ~–64 days | Supports OCF but limited incremental upside |
| **Receivables** | $88.1B, +30.1% since Dec-25; allowance $2.4B→$2.8B | Watch collection/billing mix |
| **Tax** | H1 tax expense $27.8B (23.0%) vs. cash taxes $4.0B; deferred tax $30.5B | Future cash tax normalization risk |
| **Acquisitions** | H1 $39.8B vs. $1.7B prior year; TTM $42.0B | Integration/impairment risk; reduced comparability |
| **Share count** | 10,783M outstanding (+0.5% H1); no buyback evident | Minimal dilution; SBC well controlled |
| **FY2025 derived** | Net income ~$77.7B; OCF ~$139.5B; capex ~$131.8B; FCF ~$7.7B | FCF was already thin before the 2026 capex surge |
| **Insider activity** | **No data available** | Do not infer sentiment; check Form 4s directly |
| **Data gaps** | No segment/AWS/advertising/backlog detail; no price data; annual history unavailable | Verify with 10-Q before sizing; no valuation multiples computed |
| **Overall stance** | **Constructive / Overweight bias; accumulate on weakness** | Strong operating momentum offset by negative FCF, rising debt, and noisy EPS — size accordingly |