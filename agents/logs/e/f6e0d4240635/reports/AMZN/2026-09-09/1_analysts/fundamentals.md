# AMZN — Fundamental Deep Dive (data through the 10-Q filed 31-Jul-2026)

**Company:** Amazon.com, Inc. (AMZN) · **Analysis date:** 09-Sep-2026 · **Latest reported period:** Q2 FY2026 (quarter and six months ended 30-Jun-2026)
**Data basis:** Point-in-time SEC facts public by 09-Sep-2026, sourced from the Q2-2026 10-Q (accession 0001018724-26-000026) and the Q1-2026 10-Q (0001018724-26-000014). Figures in USD millions unless noted.

> **Data caveats (important):** (1) The vendor returned only point-in-time 10-Q facts — no true multi-year annual series — so comparisons below are year-over-year from the same filing rather than a 5-year history. (2) Revenue is **not tagged directly**; it is derived as `CostsAndExpenses + OperatingIncomeLoss`, a method that reproduces known prior-year revenue exactly (Q2-25: $167.70B; H1-25: $323.37B). (3) **No price/market-cap data** is available from this toolset, so no P/E or EV multiples are asserted. (4) **Insider-transaction data is explicitly unavailable** for AMZN in this archive — no insider inference is made.

---

## 1. Company profile and business model

Amazon operates three reportable segments (the filing confirms `NumberOfOperatingSegments = 3`): **North America**, **International**, and **Amazon Web Services (AWS)**. The economic engine is a three-layer flywheel:

- **Retail/marketplace & logistics** — high-volume, thin-margin first-party and third-party commerce, monetized increasingly through seller fees and a vast fulfillment/logistics network.
- **Advertising** — high-margin, fast-growing, and embedded across retail search, Prime Video, and third-party sites; a primary driver of the consolidated gross-margin and operating-margin expansion visible below.
- **AWS (cloud + AI infrastructure)** — the profit pool and now the dominant capital sink. The Q2-2026 cash-flow statement shows the largest infrastructure build in the company's history, alongside a **$650.0B contractual-obligation backlog** that reads as locked-in cloud/AI capacity and purchase commitments.

The balance sheet is no longer a pure operating balance sheet: at 30-Jun-2026 it carries **$122.3B of non-marketable equity securities** (up from $16.2B at year-end) and **$97.9B of available-for-sale debt securities**, meaning reported earnings and book value are now materially exposed to private-AI and rate marks.

---

## 2. Income statement — strong core, but headline EPS is heavily "marked"

### 2.1 Derived quarterly and half-year P&L

| $M | Q2-26 | Q2-25 | Δ y/y | Q1-26 | H1-26 | H1-25 | Δ y/y |
|---|---:|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | **200,606** | 167,702 | **+19.6%** | 181,519 | **382,125** | 323,369 | **+18.2%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 87,463 | 183,241 | 157,785 | +16.1% |
| Gross profit | **104,828** | 86,893 | +20.6% | 94,056 | 198,884 | 165,584 | +20.1% |
| Gross margin | **52.3%** | 51.8% | +45 bp | 51.8% | 52.1% | 51.2% | +85 bp |
| Marketing | 11,698 | 11,416 | +2.5% | 10,314 | 22,012 | 21,179 | +3.9% |
| G&A | 2,788 | 2,965 | −6.0% | 2,587 | 5,375 | 5,593 | −3.9% |
| SBC (allocated) | 6,038 | 6,534 | −7.6% | 4,032 | 10,070 | 10,223 | −1.5% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** | 23,852 | **51,313** | 37,576 | **+36.6%** |
| Operating margin | **13.7%** | 11.4% | +226 bp | 13.1% | 13.4% | 11.6% | +182 bp |
| Interest expense | 1,314 | 516 | +154.7% | 800 | 2,114 | 1,057 | +100.0% |
| Interest income | 1,295 | 1,085 | +19.4% | 1,135 | 2,430 | 2,151 | +13.0% |
| **Non-operating income, net** | **53,396** | 1,686 | n.m. | 15,982 | **69,378** | 4,960 | n.m. |
| Pre-tax income | 80,857 | 20,857 | +287.7% | 39,834 | 120,691 | 42,536 | +183.7% |
| Tax expense | 18,199 | 2,678 | n.m. | 9,560 | 27,759 | 7,231 | n.m. |
| Effective tax rate | 22.5% | 12.8% | — | 24.0% | 23.0% | 17.0% | — |
| **Net income** | **62,647** | 18,164 | **+244.9%** | 30,255 | **92,902** | 35,291 | **+163.2%** |
| Diluted EPS | **$5.75** | $1.68 | +242% | $2.78 | **$8.53** | $3.27 | +161% |
| Diluted shares (implied) | 10,895 | 10,812 | +0.8% | ~10,880 | 10,895 | 10,792 | +1.0% |

### 2.2 What actually drove the quarter — and what didn't

- **Core operating momentum is genuinely excellent.** Revenue accelerated to **+19.6% y/y** in Q2 (from +16.6% in Q1) — extraordinary for a ~$760B-revenue-scale business — while operating income grew **43%**, producing **+226 bp of operating leverage**. Gross margin reached **52.3%**, and the mix is telling: marketing spend grew only **2.5%** and G&A fell **6.0%** against 19.6% revenue growth, and **SBC fell 7.6% y/y**. Amazon is getting operating leverage from advertising/AWS mix and cost discipline, not from investment cuts in the core.
- **But 66% of Q2 EPS was not operating.** Non-operating income of **$53.4B** included a **$50.5B upward revaluation of non-marketable equity securities** in the quarter alone (**$62.8B in H1-26**) — a single private holding being marked up (the size and timing are consistent with the AI-investment stake). This is non-cash, non-recurring, and booked above the tax line, which is why the effective tax rate jumped to 22.5% and deferred tax expense hit **$17.7B** in Q2.
- **"Core" EPS is far lower than the headline.** Applying the reported tax rate to operating income:
  - Q2-26 core EPS ≈ **$1.95** vs reported **$5.75** (core +26% y/y vs $1.55).
  - H1-26 core EPS ≈ **$3.63** vs reported **$8.53** (core +26% vs $2.89).
  - Put differently: **Q2 net margin of 31.2% collapses to ~10.6% on an operating basis.** Reported EPS overstates underlying earning power by roughly **2.9x** this quarter.
- **Offsets inside non-operating income** are real but small: warrant fair-value adjustment was a **−$1.45B loss** in Q2 and −$1.05B in H1, and FX gains were +$227M. Traders should expect this line to be a two-way volatility source, not a one-way uplift.
- **Depreciation is the coming margin tax.** Q2 depreciation (PP&E only) rose **+42% y/y to $13.87B**; total D&A rose **+31% to $19.99B** — versus 19.6% revenue growth. Quarterly D&A is now running ~$80B annualized against TTM revenue of roughly $760B, i.e. ~10% of sales and climbing as the AI build depreciates.
- **Interest expense doubled y/y** (+155% in Q2) as debt was raised, though at 0.7% of revenue and **20.9x operating-income coverage** it remains a manageable drag.

---

## 3. Balance sheet — liquidity intact, but leverage and mark-to-market exposure jumped

| $M | 30-Jun-26 | 31-Dec-25 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 78,213 | 86,810 | −8,597 |
| AFS debt securities | 97,900 | 45,800 | +52,100 |
| Accounts receivable, net | 88,092 | 67,729 | **+30.1%** |
| Inventory, net | 38,184 | 38,325 | −0.4% |
| Current assets | 249,264 | 229,083 | +8.8% |
| **Total assets** | **1,095,689** | 818,042 | **+33.9%** |
| Accounts payable | 147,440 | 121,909 | +20.9% |
| Current liabilities | 241,274 | 218,005 | +10.7% |
| Long-term debt, current | 3,330 | 2,748 | +21.2% |
| Long-term debt, non-current | 128,894 | 65,648 | **+96.3%** |
| **Total long-term debt** | **132,224** | 68,396 | **+93.3%** |
| Finance lease liabilities | 13,451 | 12,286 | +9.5% |
| Operating lease liabilities | 96,320 | 89,252 | +7.9% |
| Non-marketable equity securities | **122,300** | 16,200 | **+655%** |
| Deferred revenue (current + non-current) | 24,928 | 24,976 | −0.2% |
| Additional paid-in capital | 149,619 | 140,024 | +6.9% |
| AOCI | 66,287 | 28,230 | +38,057 |
| Shares outstanding (M) | 10,783 | 10,731 | +0.5% |

**Key balance-sheet reads:**

1. **Liquidity is still fortress-grade:** $78.2B cash + $97.9B AFS securities = **~$176B of liquid assets**, against $3.3B of debt due within a year. Current ratio is **1.03x** (1.05x at year-end) — thin by retail standards but normal for Amazon's negative-working-capital model.
2. **Net debt remains modest ex-leases:** $132.2B debt + $13.5B finance leases − $176.1B cash/securities = **~$30B net cash**. Including $96.3B of operating leases, adjusted net debt is roughly **$66B** — about 0.8x annualized operating income, so leverage is not a solvency issue. But the **93% six-month increase in long-term debt** ($82B of LT issuance plus $20.8B of short-term borrowings on a TTM basis) is a clear funding signal for the capex program.
3. **The asset side is now an investment book as much as an operating one.** Total assets grew **$277.6B (+33.9%) in six months**, of which **$106.1B** is the revaluation plus addition of non-marketable equity securities and **$52.1B** is added AFS securities. Reported book value and EPS are therefore levered to private-AI valuations and bond marks, not just retail/cloud operations.
4. **AOCI rose $38.1B to $66.3B**, and comprehensive income of **$131.0B** exceeded net income of $92.9B by ~$38B. That is mark-to-market equity accretion — real to book value, but not cash and reversible.
5. **Receivables are the one working-capital yellow flag:** AR grew **30.1%** vs revenue growth of 18–20%, while the allowance fell to **3.2% of AR** (from 3.5%). DSO on Q2 revenue is ~40 days. This is consistent with a mix shift toward advertising/AWS billing, but it bears monitoring for collection quality.
6. **Deferred revenue is flat y/y (+0.3%) while revenue grows 18%** — meaning the forward revenue visibility is *not* sitting in contract liabilities; it sits in the **$650.0B contractual-obligation disclosure** (see below).

### Commitments — the single most important forward-looking disclosure

| Contractual obligations, 30-Jun-26 | $M |
|---|---:|
| **Total** | **650,034** |
| Due next 12 months | 78,084 |
| Due year 2 | 53,406 |
| Due year 3 | 46,767 |
| Due year 4 | 42,219 |

This ~$650B book (≈60% of total assets and roughly 0.85x TTM revenue) is the clearest evidence of **multi-year AWS/AI capacity and content commitments**. It is simultaneously the bull case (locked-in demand, visibility) and the bear case (fixed, largely non-cancellable cost if AI demand disappoints). Note that $78B falls due inside twelve months, versus $161B of TTM operating cash flow — absorbable, but it consumes most of annual cash generation before capex.

---

## 4. Cash flow — the central fundamental issue: FCF has turned negative

| $M | Q2-26 | Q2-25 | H1-26 | H1-25 | TTM (Jul-25→Jun-26) | Prior TTM |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash flow | 45,387 | 32,515 | **71,419** | 49,530 | **161,403** | 121,137 |
| Capex (productive assets) | 54,208 | 32,183 | **98,411** | 57,202 | **173,028** | 107,656 |
| **Free cash flow** | **(8,821)** | 332 | **(26,992)** | (7,672) | **(11,625)** | **+13,481** |
| Capex / revenue | **27.0%** | 19.2% | 25.8% | 17.7% | ~23% | ~16% |
| Capex / OCF | 119% | 99% | **138%** | 116% | **107%** | 89% |
| Business acquisitions, net | 24,359 | 1,700 | **39,767** | 1,652 | 41,956 | 4,809 |
| LT debt issued | 13,557 | 0 | 66,998 | 746 | 81,925 | 746 |
| ST debt, net | (205) | 701 | (296) | 436 | 164 | 286 |
| Financing cash flow | +10,146 | −2,539 | **+62,913** | −2,586 | +75,160 | −8,652 |
| Investing cash flow | −79,245 | −39,424 | **−143,457** | −69,227 | −216,775 | −123,569 |
| Cash change | −23,765 | −8,440 | −9,179 | −20,859 | +19,474 | −10,220 |

**Interpretation:**

- **Operating cash flow quality is strong in absolute terms** — TTM OCF of **$161.4B, +33% y/y** — and H1 OCF grew **+44%**. Cash conversion is lower than net income (OCF/NI ≈ 72–77%) precisely because the $62.8B equity mark-up is non-cash and removed in the reconciliation.
- **But capex has exploded to $173.0B TTM** (+61% y/y), reaching **27% of Q2 revenue**. Free cash flow is **negative $11.6B TTM**, a swing of ~$25B from +$13.5B a year earlier, and **−$27.0B in H1-26 alone**. Q2 marked the second consecutive quarter of negative FCF (−$18.2B in Q1, −$8.8B in Q2).
- **The gap is being funded with debt and business acquisitions of ~$40B in H1.** That is a strategic choice, not distress — but it changes the equity story from "self-funding cash machine" to "levered AI infrastructure build."
- **Watch depreciation follow-through:** capex front-loads cash outflows today and D&A charges tomorrow. If the ~$170–200B annualized capex run-rate persists, D&A could approach $100B+/year within 4–6 quarters, mechanically compressing operating margin unless revenue growth and mix (advertising/AWS) offset it.

---

## 5. Insider transactions

**DATA_UNAVAILABLE.** The vendor archive contains no authorized, point-in-time insider-transaction record for AMZN as of 09-Sep-2026. This report makes **no inference and no fabrication** regarding insider buying or selling. Treat insider sentiment as an information gap for this analysis; do not read the absence of data as either bullish or bearish.

---

## 6. Fundamental scorecard — bull vs. bear

**Bull case (evidence-based):**
1. **Revenue re-accelerated to +19.6% y/y** ($200.6B) at enormous scale, with Q1 also +16.6% — acceleration, not deceleration.
2. **Operating leverage is working:** operating income +43% y/y, margin +226 bp to 13.7%, with marketing +2.5%, G&A −6%, and SBC −7.6%. Gross margin 52.3%.
3. **OCF +33% TTM to $161.4B**; H1 OCF +44%.
4. **$176B liquid assets** and only $3.3B of debt maturing within a year; interest coverage 20.9x.
5. **$650B of contractual obligations** provides unusually long visibility on AWS/AI demand.
6. **Share count nearly flat** (+0.8% y/y) — no dilution problem.

**Bear case (evidence-based):**
1. **FCF is negative**: −$11.6B TTM, −$27.0B H1; capex at 27% of revenue. Any AI-spending disappointment hits returns on this base.
2. **Earnings quality is poor at the headline**: $62.8B of H1 pre-tax income came from marking up private equity holdings; 66% of Q2 EPS was non-operating. Reported EPS ($5.75) is ~2.9x core ($1.95).
3. **Debt up 93% in six months to $132B**, interest expense +155% y/y; further issuance likely if capex persists.
4. **Depreciation +31–42% y/y** and accelerating — a structural margin headwind into 2027.
5. **Mark-to-market cuts both ways**: private-AI valuation compression or a warrant mark loss would create headline EPS misses with no operating cause; FY26 EPS comparisons will be extremely noisy.
6. **$78B of obligations due within 12 months** plus $98B of H1 capex consumes essentially all annual operating cash flow.
7. **AR +30% vs revenue +19%** with a thinner allowance — a modest but real collections watch item.

---

## 7. Actionable insights for traders

1. **Decompose every AMZN print into three lines before reacting: operating income, non-operating income, and capex.** The market-visible "EPS beat/miss" is currently a poor proxy for the business. Q2-26 is the template: a 43% operating-income beat plus a $50.5B private mark produced $5.75 of EPS versus ~$1.95 of core EPS. Position for the possibility that headline beats are discounted and headline misses (mark-downs) are over-punished.
2. **Treat negative FCF as the primary swing factor.** The stock's fundamental narrative now hinges on whether the ~$170B+ capex run-rate is demand-backed. The **$650B contractual-obligation backlog argues it is** — but the market will trade the FCF trajectory quarter to quarter. A capex guide-down or slowing backlog growth is the cleanest positive catalyst; an upward capex revision without matching revenue visibility is the cleanest negative.
3. **Use core EPS for valuation work.** With ~10.78B shares and reported TTM net income of $135.3B (~$12.4 TTM EPS, approximate), applying a market multiple to reported earnings overstates normalized earnings power by roughly 40–50%. Core annualized run-rate from H1-26 is roughly **$7.3/share**; that is the cleaner anchor for a P/E framework. (Price data is unavailable here, so the multiple itself must be applied by the reader.)
4. **Monitor the depreciation ramp as the 2027 margin story.** Q2 PP&E depreciation +42% y/y vs revenue +19.6%. If D&A growth continues at 2x revenue growth, operating margin expansion could stall even with healthy top line — the first sign would be gross margin flattening from 52.3%.
5. **Watch the debt-issuance cadence and credit metrics.** $82B of TTM LT issuance and 93% six-month debt growth is fine at 0.8x adjusted EBITDA-ish leverage with $176B liquidity, but a third consecutive half of $60B+ issuance would put rating/spread headlines into the equity narrative.
6. **Event risk calendar:** the next fundamental checkpoint is the **Q3-2026 report (expected late October 2026)**. Key items: AWS growth and backlog/commitment disclosure, capex guide, D&A step-up, non-operating mark direction, and receivables. Do not assume the Q2 non-operating gains repeat.
7. **Insider data is unavailable** — this is a genuine blind spot. Traders relying on insider confirmation should source it separately rather than infer from this report.

---

## 8. Summary table — key points at a glance

| Category | Metric | Latest (Q2/H1-26) | Prior-year comparable | Assessment |
|---|---|---:|---:|---|
| **Scale** | Q2 revenue (derived) | $200.6B | $167.7B (+19.6%) | 🟢 Accelerating |
| **Scale** | H1 revenue (derived) | $382.1B | $323.4B (+18.2%) | 🟢 Strong |
| **Profitability** | Q2 operating income | $27.46B | $19.17B (+43.2%) | 🟢 Best-in-class leverage |
| **Profitability** | Q2 operating margin | 13.7% | 11.4% (+226 bp) | 🟢 Expanding |
| **Profitability** | H1 gross margin | 52.1% | 51.2% (+85 bp) | 🟢 Mix-driven |
| **Reported EPS** | Q2 diluted EPS | $5.75 | $1.68 (+242%) | 🟡 66% non-operating |
| **Core EPS** | Q2 EPS ex-marks (est.) | ~$1.95 | ~$1.55 (+26%) | 🟢 Solid, far below headline |
| **Earnings quality** | H1 non-operating income | $69.4B | $4.96B | 🔴 57% of pre-tax income |
| **Private marks** | Non-marketable equity securities | $122.3B | $16.2B (YE25) | 🟡 $62.8B H1 revaluation |
| **Cash generation** | TTM operating cash flow | $161.4B | $121.1B (+33%) | 🟢 Excellent |
| **Capital intensity** | TTM capex | $173.0B | $107.7B (+61%) | 🔴 27% of Q2 revenue |
| **Free cash flow** | TTM FCF | **−$11.6B** | +$13.5B | 🔴 Negative and widening |
| **H1 FCF** | H1 free cash flow | −$27.0B | −$7.7B | 🔴 Deteriorating |
| **Leverage** | Total long-term debt | $132.2B | $68.4B (YE25) | 🟡 +93% in 6 months |
| **Coverage** | Q2 operating income / interest | 20.9x | 37.2x | 🟢 Still comfortable |
| **Liquidity** | Cash + AFS securities | $176.1B | $132.6B (YE25) | 🟢 Fortress |
| **Working capital** | Current ratio | 1.03x | 1.05x (YE25) | 🟡 Adequate |
| **Receivables** | AR growth y/y vs revenue | +30.1% vs +19.6% | — | 🟡 Watch collections |
| **Visibility** | Contractual obligations | $650.0B (78.1B <12m) | n/a | 🟢 Backlog; 🟡 fixed-cost risk |
| **Dilution** | Shares outstanding | 10,783M | 10,731M (YE25) | 🟢 Minimal |
| **Capital return** | Dividend / buyback | None reflected in filings | None | ⚪ Non-issue |
| **Insider activity** | Transactions | **Data unavailable** | — | ⚪ No signal available |
| **Overall** | Fundamental stance | Operating business strong; **earnings quality and FCF are the debate** | — | 🟡 Constructive long-term, event-volatile near-term |

**Bottom line:** AMZN's *operating* business is performing better than at any point in its history — 19.6% revenue growth at $200B+ quarterly scale, 13.7% operating margins, 43% operating-income growth, and $161B of TTM operating cash flow. The complication is that the market-visible numbers are distorted in both directions: **reported EPS is inflated ~3x by private-equity mark-ups**, while **free cash flow is negative $11.6B because of a historic AI-infrastructure capex cycle funded increasingly with debt**. The trade is therefore less about whether Amazon's franchises are healthy (they are) and more about whether the **$650B commitment book converts into returns before depreciation and interest consume the margin expansion** — with Q3-2026 capex guidance and backlog disclosure as the decisive near-term evidence.