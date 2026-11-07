# AMZN — Fundamental Research Report
**Amazon.com, Inc. (NASDAQ: AMZN)**
**As of: 2026-07-30 (post-close) | Primary source: Q2 2026 Form 10-Q, accession 0001018724-26-000026, EDGAR acceptance 2026-07-31 02:11:13 UTC (= ~22:11 ET on 2026-07-30)**

---

## 1. Executive Summary — Why This Report Matters Right Now

The single most important fact in this dataset: **AMZN's Q2 2026 10-Q was accepted by EDGAR at 2026-07-31 02:11 UTC, which is ~22:11 ET on 2026-07-30 — i.e., after today's cash close.** The market has **not yet priced** these numbers. Every figure below is new information for the 2026-07-31 session.

Three things stand out, and they pull in opposite directions:

1. **The operating business inflected hard and positive.** Q2 2026 revenue grew **+19.6% y/y** (accelerating from +16.6% in Q1), operating income grew **+43.2% y/y**, and operating margin hit **13.7%** (vs. 11.4%) — a record level for a June quarter. EBITDA margin expanded **+314bps** to **23.7%**.
2. **Headline EPS is overwhelmingly an accounting event, not cash.** Diluted EPS of **$5.75** includes roughly **$3.59/share** from a **$50.5B non-cash upward revaluation of non-marketable equity securities** (balance jumped **$16.2B → $122.3B** in six months). Excluding that item, "core" Q2 EPS is roughly **$2.16**.
3. **The cash engine is now inverted.** TTM operating cash flow of **$161.4B** is being outspent by TTM capex of **$173.0B** → **TTM free cash flow of –$11.6B**, versus **+$13.5B** a year prior. Long-term debt nearly **doubled** (from $68.8B to $133.0B) in six months, and quarterly interest expense rose **+155% y/y**.

**Net read:** a genuine, high-quality *operating* beat wrapped in a very low-quality *earnings* headline, funded by a balance-sheet transformation toward leverage. This is a "the print is good but read the footnotes" setup.

---

## 2. Company Profile & Reporting Structure

- **Entity:** Amazon.com, Inc., SEC filer CIK 0001018724. Common stock par $0.01; 100,000,000,000 shares authorized.
- **Segments:** `NumberOfOperatingSegments = 3` for H1 2026 — consistent with the three-segment structure (North America, International, AWS). Segment-level revenue/operating income detail is **not** present in the retrieved tag set (see §11 caveats).
- **Share count:** 10,783,000,000 shares outstanding at 2026-06-30; 10,786,313,572 per the 2026-07-22 cover-page count. Shares outstanding rose from 10,731M at 2025-12-31 (+0.5% in six months) — pure stock-compensation dilution.
- **Capital returns:** No share-repurchase or dividend line items appear in the cash-flow tag set. All capital is being directed to capex, M&A and debt service.
- **Insider transactions:** **DATA UNAVAILABLE.** The vendor's archive has no authorized, point-in-time insider-transaction record for AMZN as of 2026-07-30. No inference is drawn; treat insider flow as an open question.

---

## 3. Income Statement — Q2 2026 (three months ended 2026-06-30)

Net sales are **not** directly present in the retrieved tags (the dataset is truncated alphabetically before revenue tags). They are **exactly derivable** from Amazon's income-statement identity: *Total costs and expenses + Operating income = Net sales.*

| Line item | Q2 2026 | Q2 2025 | Δ y/y |
|---|---|---|---|
| **Net sales (derived)** | **$200,606M** | **$167,702M** | **+19.6%** |
| Cost of goods & services sold | 95,778 | 80,809 | +18.5% |
| *Gross profit (derived)* | *104,828* | *86,893* | *+20.6%* |
| *Gross margin* | *52.3%* | *51.8%* | *+50bps* |
| Marketing expense | 11,698 | 11,416 | +2.5% |
| G&A expense | 2,788 | 2,965 | –6.0% |
| Fulfillment + tech/content + other (derived residual) | 62,881 | 53,341 | +17.9% |
| **Total costs and expenses** | **173,145** | **148,531** | **+16.6%** |
| **Operating income** | **27,461** | **19,171** | **+43.2%** |
| *Operating margin* | *13.7%* | *11.4%* | *+230bps* |
| Depreciation, depletion & amortization *(embedded above)* | 19,988 | 15,227 | +31.2% |
| Stock-based compensation *(embedded above)* | 6,038 | 6,534 | –7.6% |
| Interest expense (non-operating) | 1,314 | 516 | +154.7% |
| Investment income — interest | 1,295 | 1,085 | +19.4% |
| Equity securities FV-NI gain | 1,300 | 393 | +231% |
| Non-marketable equity upward revaluation | **50,486** | 49 | **n/m** |
| Warrant fair-value adjustment | (1,449) | (590) | n/m |
| FX transaction gain | 227 | 70 | +224% |
| **Non-operating income, net** | **53,396** | **1,686** | **+3,067%** |
| Pre-tax income | 80,857 | 20,857 | +287.7% |
| Income tax expense | 18,199 | 2,678 | +579.6% |
| *Effective tax rate* | *22.5%* | *12.8%* | *+970bps* |
| **Net income** | **62,647** | **18,164** | **+244.9%** |
| **Diluted EPS** | **$5.75** | **$1.68** | **+242%** |
| Basic EPS | 5.82 | 1.71 | +240% |
| Diluted shares (derived) | ~10,895M | ~10,811M | +0.8% |
| **Memo: EBITDA (op. inc. + D&A)** | **47,449** | **34,398** | **+37.9%** |
| *EBITDA margin* | *23.7%* | *20.5%* | *+314bps* |

### 3.1 Cost leverage is real and broad-based
Q2 operating margin expanded 230bps. Decomposing the improvement as a share of revenue (each vs. Q2 2025):

- Gross margin: **+50bps**
- Marketing as % of revenue: **6.81% → 5.83%** = **+98bps** of margin (revenue +19.6% against marketing +2.5% — extraordinary discipline)
- G&A as % of revenue: **1.77% → 1.39%** = **+38bps**
- Fulfillment/tech/other combined: **31.8% → 31.3%** of revenue = **+50bps**

Critically, that residual line already **absorbs 88bps of extra depreciation** (D&A rose from 9.08% to 9.96% of revenue as the capex program enters service). **Underlying cash operating-cost leverage inside fulfillment and technology is therefore ~138bps of revenue in a single quarter** — the operational efficiency story is materially stronger than the headline margin suggests.

### 3.2 Revenue growth is *accelerating* — with one caveat
- Q1 2026: $181,519M vs $155,667M = **+16.6%**
- Q2 2026: $200,606M vs $167,702M = **+19.6%**
- Sequential q/q: **+10.5%** (Q1→Q2 2026) vs **+7.7%** (Q1→Q2 2025)

**Caveat:** H1 2026 cash spent on acquisitions was **$39,767M** (Q2 alone: **$24,359M**), versus just **$1,652M** in H1 2025. A portion of the acceleration is likely **inorganic**. The 10-Q tag set does not disclose acquired-revenue contribution. **This is the #1 item to reconcile on the call** — if 300bps of the acceleration is acquired, the organic story is more like +16–17%, still good but not an inflection.

---

## 4. Quality of Earnings — The $50B Question

This is the analytical crux of the print.

| Metric | Q2 2026 |
|---|---|
| Reported diluted EPS | **$5.75** |
| Non-marketable equity upward revaluation, pre-tax | **$50,486M** |
| After-tax at 22.5% statutory-rate assumption | ~$39,127M |
| Per diluted share | **~$3.59** |
| **"Core" EPS excluding the mark-up** | **~$2.16** |
| Share of reported EPS that is non-cash revaluation | **~62%** |

**Supporting evidence from the filing:**
- `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount` = **$50,486M** for Q2 2026 and **$62,814M** for H1 2026.
- The carrying value of non-marketable equity securities went from **$16,200M (2025-12-31)** to **$122,300M (2026-06-30)** — **+$106.1B in six months.** This single line now equals **11.2% of total assets**.
- Cash taxes paid in Q2 2026 were only **$2,655M** against a **$18,199M** tax provision. Deferred tax expense was **$17,691M** in the quarter and **$41,441M** TTM. The earnings are explicitly **not cash-backed** — the mark-up creates a deferred tax liability rather than a cash outflow.
- Cash conversion: OCF/net income fell from **1.79x** (Q2 2025) to **0.72x** (Q2 2026). Note this is *not* because operating cash flow is deteriorating (it grew **+39.6%** y/y) — it is purely because the denominator is inflated.

**Trading implication:** if the sell-side "beat" narrative is built on the $5.75, it is fragile — any analyst marking to a "core" number gets ~$2.16. Conversely, if the market correctly strips the mark-up and focuses on $27.5B of operating income and 13.7% margins, the print is excellent. **How the desk commentary frames the EPS quality on the 2026-07-31 open is likely to drive the gap direction more than the raw numbers.**

**Second-order risk:** this is a **mark-to-model** asset. If the underlying private holding (a large AI-related position, given the size/shape) sees a down-round or a public comp de-rates, this $122.3B asset can reverse *through the income statement* just as violently. There is **no offsetting cash** to cushion it.

---

## 5. Cash Flow & Capex — The Free-Cash-Flow Inversion

| | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | TTM to 2026-06-30 | TTM to 2025-06-30 |
|---|---|---|---|---|---|---|
| Operating cash flow | **45,387** | 32,515 | **71,419** | 49,530 | **161,403** | 121,137 |
| Capex (purchases of productive assets) | **54,208** | 32,183 | **98,411** | 57,202 | **173,028** | 107,656 |
| **Free cash flow** | **(8,821)** | **+332** | **(26,992)** | (7,672) | **(11,625)** | **+13,481** |
| Capex / OCF | **119%** | 99% | **138%** | 116% | **107%** | 89% |
| Cash taxes paid | 2,655 | 4,761 | 3,978 | 5,638 | 6,635 | 11,788 |
| Acquisitions, net of cash | 24,359 | 1,700 | 39,767 | 1,652 | 41,956 | 4,809 |

**Key observations:**
- **Operating cash flow growth is excellent:** Q2 **+39.6% y/y**, H1 **+44.2% y/y**, TTM **+33.0%**. Core cash generation is accelerating faster than revenue.
- **Capex growth is even faster:** Q2 **+68.4%**, H1 **+72.0%**, TTM **+60.7%**. Q2's $54.2B is an all-time-high quarterly figure and implies a **~$217B annualized run-rate**.
- **The FCF crossover is the headline negative:** TTM FCF swung from **+$13.5B to –$11.6B**, a **$25.1B deterioration**. This is the first clearly negative TTM FCF print in the modern Amazon era.
- **Capex growth (+72%) far exceeds D&A growth (+32%)**, meaning the depreciation drag on the P&L is **still in the early innings** — D&A will keep climbing as this cohort matures, mechanically pressuring future margins even if cash opex stays disciplined.
- **Forward commitments confirm the spend isn't slowing:** total contractual obligations at 2026-06-30 were **$650,034M**, of which **$78,084M** falls due within twelve months, $53,406M in year two, $46,767M in year three, $42,219M in year four — implying **~$429.6B beyond year four**. Even netting out $116.4B of undiscounted operating-lease payments, this is a very large multi-year purchase-commitment book (AI capacity, chips, energy). **Capex is contractually locked in, not discretionary.**

---

## 6. Balance Sheet — Larger, More Liquid, and Much More Levered

| Item | 2026-06-30 | 2025-12-31 | Δ |
|---|---|---|---|
| **Total assets** | **$1,095,689M** | $818,042M | **+$277,647M (+33.9%)** |
| Cash & equivalents | 78,213 | 86,810 | –8,597 |
| Available-for-sale debt securities | 97,900 | 45,800 | **+52,100** |
| **Cash + marketable securities** | **176,113** | **132,610** | **+$43,503M (+32.8%)** |
| Accounts receivable, net | 88,092 | 67,729 | +20,363 (+30.1%) |
| Allowance for doubtful accounts | 2,800 | 2,400 | 3.2% of gross AR (was 3.5%) |
| Inventory, net | 38,184 | 38,325 | –141 (**–0.4%**) |
| Non-marketable equity securities | **122,300** | **16,200** | **+$106,100M** |
| Accounts payable | 147,440 | 121,909 | +25,531 (+20.9%) |
| Accrued liabilities | 73,406 | 75,520 | –2,114 |
| Current liabilities | 241,274 | 218,005 | +23,269 |
| Current assets | 249,264 | 229,083 | +20,181 |
| **Current ratio** | **1.033x** | 1.051x | –0.018x |
| Long-term debt (total, incl. current $3,330) | **132,995** | 68,836 | **+64,159 (+93.2%)** |
| Finance lease liabilities | 13,451 | 12,286 | +1,165 |
| Operating lease liabilities | 96,320 | 89,252 | +7,068 |
| Contract liabilities (deferred revenue) | 24,928 | 25,000 | –72 (flat) |
| Additional paid-in capital | 149,619 | 140,024 | +9,595 |
| Accumulated OCI | **+66,287** | +28,230 | **+38,057 (flag — see §11)** |
| Shares outstanding | 10,783M | 10,731M | +52M |

**Liquidity:** $176.1B of cash and securities, of which **$96.5B matures within one year** — ample cover for the $78.1B of 12-month contractual obligations. Liquidity is not a near-term issue.

**Leverage:** gross debt (long-term debt + finance leases) rose to **$146.4B** from **$81.1B**. Including operating leases, total obligations are **~$242.8B**. Against $176.1B of cash/securities, net debt including leases is roughly **+$67B**, versus a net-cash position at year-end. Amazon has formally become a levered credit story. **Interest expense is the tell:** Q2 $1,314M vs $516M (**+155%**), H1 $2,114M vs $1,057M. Coverage is still comfortable (**20.9x** operating income in Q2), but the trajectory is steep and each incremental $10B of debt adds roughly $450–500M of annual interest at current rates.

**Balance-sheet asset growth is mostly non-cash:** of the $277.6B increase in total assets, **$106.1B is the non-marketable equity mark-up**, ~$52.1B is AFS securities (a reclassification of liquidity, largely funded from cash/operations), and the rest is capex-driven PP&E plus goodwill from $39.8B of acquisitions. **Only a modest fraction reflects cash retained from earnings.**

---

## 7. Working Capital & Efficiency

- **Inventory turns are exceptional.** Inventory was **flat at $38.2B** while H1 COGS rose to $183.2B. Annualizing H1 COGS (~$366.5B) against $38.2B inventory implies **~9.6x turns** — a structurally lean position that removes a major historical risk factor ahead of peak season.
- **Negative cash-conversion cycle preserved:** AP ($147.4B) plus accrued ($73.4B) = $220.8B of non-interest-bearing float against $126.3B of AR + inventory. Amazon still funds operations with supplier capital, and AP grew in line with revenue (+20.9% vs +19.6%).
- **Receivables are the one soft spot:** AR grew **+30.1%** vs revenue **+19.6%** — a ~10pt gap. This is consistent with (a) mix shift toward AWS/ads/enterprise customers with longer terms, and (b) acquired receivables. Bad-debt allowance as a share of gross AR actually *improved* (3.5% → 3.2%), so credit quality is not the driver. **Worth monitoring: if AR keeps outgrowing revenue, it will quietly absorb cash exactly when FCF is already negative.**
- **Deferred revenue flat at $24.9B** — no obvious demand-signal deterioration, but no acceleration either.

---

## 8. Tax Analysis

| | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | TTM |
|---|---|---|---|---|---|
| Income tax expense | 18,199 | 2,678 | 27,759 | 7,231 | — |
| Effective rate | **22.5%** | 12.8% | **23.0%** | 17.0% | — |
| Deferred tax expense | 17,691 | 11 | 30,489 | 518 | **41,441** |
| Cash taxes paid | 2,655 | 4,761 | 3,978 | 5,638 | **6,635** |
| Cash tax / pre-tax income | 3.3% | 22.8% | 3.3% | 13.3% | — |

The GAAP rate normalized to a more conventional ~22.5% (from an artificially low 12.8%), and **97% of Q2's tax charge was deferred**. TTM cash taxes of $6.6B against TTM net income of $135.3B is an exceptionally low cash tax rate — a real cash advantage, but one driven substantially by the non-cash gain generating a DTL rather than by structural tax planning. **Do not model forward cash taxes off this TTM figure.**

---

## 9. H1 2026 Aggregate & TTM View

| Metric | H1 2026 | H1 2025 | Δ | TTM (Jul'25–Jun'26) |
|---|---|---|---|---|
| Net sales (derived) | **$382,125M** | $323,369M | **+18.2%** | n/a (FY25 base not in tag set) |
| Operating income | **51,313** | 37,576 | **+36.6%** | — |
| Operating margin | **13.4%** | 11.6% | +180bps | — |
| EBITDA | **90,246** | 67,065 | **+34.6%** | — |
| EBITDA margin | **23.6%** | 20.7% | +290bps | — |
| Non-operating income | **69,378** | 4,960 | +1,299% | — |
| Net income | **92,902** | 35,291 | **+163.2%** | **135,281** |
| Diluted EPS | **$8.53** | $3.27 | +160.9% | — |
| Operating cash flow | **71,419** | 49,530 | +44.2% | **161,403** |
| Capex | **98,411** | 57,202 | +72.0% | **173,028** |
| Free cash flow | **(26,992)** | (7,672) | –$19.3B | **(11,625)** |
| D&A | **38,933** | 29,489 | +32.0% | **75,200** |
| SBC | **10,070** | 10,223 | **–1.5%** | — |
| Acquisitions | **39,767** | 1,652 | +2,307% | 41,956 |

**TTM "core" earnings power estimate:** strip the non-operating income entirety from H1 2026 (op income $51.3B × 77.5% = ~$39.8B) and you get an annualized core net income run-rate in the **$80B range** — versus a TTM GAAP net income of $135.3B. **Roughly 40% of TTM GAAP earnings are non-operating.**

---

## 10. Risk Register (ranked by materiality to the next 90 days)

| # | Risk | Evidence | Severity |
|---|---|---|---|
| 1 | **Earnings-quality rejection** — market discounts headline EPS as non-cash | ~62% of Q2 EPS from a $50.5B mark-up; cash taxes 3.3% of pre-tax | High (immediate) |
| 2 | **Non-marketable equity reversal** — $122.3B mark-to-model asset can impair through P&L | 11.2% of total assets; +$106.1B in 6 months | High |
| 3 | **Negative & widening FCF** | TTM –$11.6B vs +$13.5B prior year; capex/OCF 138% in H1 | High |
| 4 | **Leverage inflection** | LT debt +93% in 6 months; interest expense +155% y/y | High |
| 5 | **Depreciation wave** — capex +72% vs D&A +32% means margin drag still building | D&A/rev 9.08% → 9.96% | Medium-High |
| 6 | **Inorganic revenue masking organic deceleration** | $39.8B H1 acquisitions vs $1.7B prior year | Medium |
| 7 | **Locked-in spending** — $650.0B contractual obligations, ~$429.6B beyond year 4 | Purchase-commitment book | Medium |
| 8 | **Receivables outgrowing revenue** | AR +30.1% vs revenue +19.6% | Medium |
| 9 | Thin current ratio | 1.033x, down from 1.051x | Low |
| 10 | Insider signal unknown | Vendor archive unavailable | Unknown |

---

## 11. Data Integrity Caveats (read before acting)

1. **Net sales, gross profit, fulfillment+tech residual, core EPS, FCF, EBITDA, margins, diluted share count and TTM figures are DERIVED by arithmetic** from reported tags (principally the identity *Net sales = CostsAndExpenses + OperatingIncomeLoss*). They are internally consistent and tie across Q1/Q2/H1, but they are **not** direct vendor line items. The revenue/detail tags sit past the alphabetical truncation point of this point-in-time extract.
2. **`AccumulatedOtherComprehensiveIncomeLossNetOfTax` rising +$38,057M in six months is unexplained** by the disclosed components: FX translation was **–$1,563M** and gross unrealized gains on AFS debt securities were only **$7M** at period end. **Verify against the 10-Q statement of stockholders' equity before relying on book value.** It does not change any conclusion above (AOCI is non-cash and excluded from operating analysis).
3. **`DebtSecuritiesAvailableForSaleUnrealizedGainLoss` = $92,000M for H1 2026** is internally inconsistent with a $7M gross unrealized gain at 2026-06-30. Treat that tag as unreliable/mislabeled and disregard.
4. **No segment-level (NA / Intl / AWS) revenue or operating income** is present. AWS growth and margin are the single most important swing factors and **cannot be assessed from this dataset** — get them from the earnings release/call.
5. **Insider transactions: DATA_UNAVAILABLE.** No authorized point-in-time archive exists for AMZN as of 2026-07-30. Nothing has been inferred or fabricated.
6. **No market price, valuation multiple, consensus estimate or FY2025 full-year total** is in the retrieved tag set. Absolute valuation (P/E, EV/EBITDA) cannot be computed here.
7. **Filing timestamp:** `accepted_at` 2026-07-31 02:11:13 UTC = ~22:11 ET on 2026-07-30. The 10-Q is a post-close event relative to today's session.

---

## 12. Actionable Trading Insights

**Bull case (what to lean on):**
- Revenue growth **accelerated** 16.6% → 19.6%; sequential q/q of +10.5% beat last year's +7.7%.
- Operating income **+43%** with **broad-based** leverage: marketing +2.5%, G&A –6.0%, COGS +18.5% — all against +19.6% revenue.
- **SBC fell 7.6% y/y** while revenue grew ~20%. This is a genuine, underappreciated margin tailwind and a cultural/comp-discipline signal.
- **EBITDA +37.9%** to $47.4B, margin 23.7%. Operating cash flow +39.6%. The cash engine is healthy; it is simply being out-invested.
- Inventory **flat** while COGS +18.5% — no demand-destruction signal in the goods business.
- Liquidity **+32.8%** to $176.1B; $96.5B of it maturing inside a year.

**Bear case (what to fade):**
- ~62% of the $5.75 EPS is a **non-cash, mark-to-model revaluation**. Core EPS ≈ **$2.16**.
- **TTM FCF is negative (–$11.6B)** and H1 capex/OCF is 138%. Next quarter's capex will almost certainly exceed $54.2B again.
- **LT debt +93% in six months**; interest expense +155%. Interest is now a $5B+ annual run-rate and rising.
- **$122.3B** of non-marketable equity is 11.2% of assets and carries **two-way** P&L volatility.
- **$650.0B** of contractual obligations — the capex program is contractual, not optional.
- D&A is compounding at +32% off a base that is about to absorb a $173B annualized capex cohort.

**Concrete monitoring thresholds for the next 90 days:**
| Metric | Trigger for concern | Trigger for confirmation |
|---|---|---|
| Q3 2026 revenue growth | < +15% y/y (organic decel) | ≥ +18% with organic disclosure |
| Q3 2026 operating margin | < 11.5% (D&A outrunning leverage) | ≥ 13.5% sustained |
| Q3 2026 capex | > $60B (FCF hole deepens) | ≤ $52B with OCF growth ≥ 35% |
| TTM FCF | < –$25B | Back toward breakeven |
| LT debt | > $150B | Flat/declining |
| Interest expense (quarterly) | > $1.6B | < $1.4B |
| Non-marketable equity balance | Below $110B (reversal begins) | Above $130B |
| Cash taxes / pre-tax income | > 10% (losing the deferral benefit) | Stays < 8% |

**Positioning framing:** this is a **binary on narrative, not on numbers**. The operating data supports a constructive stance; the earnings-quality data supports a fade of any gap-up that is justified by "$5.75 EPS beat." A probability-weighted approach is to treat the **operating segment strength as the durable, tradable edge** (long horizon) and the **EPS headline as a volatility event** to be faded on the print (short horizon). Watch the 2026-07-31 open commentary: if the tape focuses on 13.7% margins and +19.6% growth, upside follow-through is likely; if the tape discovers the $50.5B mark-up and negative FCF intraday, expect the gap to fade.

---

## 13. Key Points Summary

| Category | Item | Q2 2026 | Q2 2025 | Change | Read |
|---|---|---|---|---|---|
| **Event** | Q2 2026 10-Q (accession 0001018724-26-000026) | Accepted 2026-07-31 02:11 UTC (~22:11 ET 2026-07-30) | — | Post-close, unpriced | **Actionable now** |
| Revenue | Net sales (derived) | $200,606M | $167,702M | **+19.6%** | **Accelerating** (Q1: +16.6%) |
| Revenue | Sequential q/q | +10.5% | +7.7% | +280bps | Strong |
| Profit | Gross profit (derived) | $104,828M | $86,893M | +20.6% | Margin 52.3% (+50bps) |
| Profit | **Operating income** | **$27,461M** | $19,171M | **+43.2%** | Best-in-class |
| Profit | **Operating margin** | **13.7%** | 11.4% | **+230bps** | Record June-qtr |
| Profit | EBITDA | $47,449M | $34,398M | +37.9% | Margin 23.7% (+314bps) |
| Profit | Marketing expense | $11,698M | $11,416M | +2.5% | +98bps of margin leverage |
| Profit | G&A expense | $2,788M | $2,965M | –6.0% | +38bps of margin leverage |
| Profit | SBC | $6,038M | $6,534M | **–7.6%** | Underrated tailwind |
| Profit | D&A | $19,988M | $15,227M | +31.2% | 9.96% of rev (+88bps drag) |
| **Earnings quality** | Non-marketable equity revaluation | **$50,486M** | $49M | n/m | **~$3.59 of $5.75 EPS** |
| Earnings quality | Non-operating income, net | $53,396M | $1,686M | +3,067% | 66% of pre-tax income |
| Earnings quality | **Core EPS (ex mark-up, derived)** | **~$2.16** | ~$1.65 | +31% | Still respectable |
| Earnings quality | Non-marketable equity balance | $122,300M | — | +$106.1B in 6M | 11.2% of assets; mark-to-model |
| Bottom line | Net income | $62,647M | $18,164M | +244.9% | 62% non-cash |
| Bottom line | **Diluted EPS** | **$5.75** | $1.68 | +242% | Low quality |
| Bottom line | Diluted shares | ~10,895M | ~10,811M | +0.8% | Minimal dilution |
| Tax | Effective rate | 22.5% | 12.8% | +970bps | Now near-normal GAAP |
| Tax | Deferred tax expense | $17,691M | $11M | n/m | 97% of charge deferred |
| Tax | Cash taxes paid | $2,655M | $4,761M | –44% | 3.3% of pre-tax |
| **Cash flow** | Operating cash flow | $45,387M | $32,515M | **+39.6%** | Healthy |
| Cash flow | Capex | $54,208M | $32,183M | **+68.4%** | ~$217B annualized |
| Cash flow | **Free cash flow** | **–$8,821M** | +$332M | –$9.2B | **Negative** |
| Cash flow | Capex / OCF | **119%** | 99% | +20pts | Structural |
| **TTM** | Operating cash flow | **$161,403M** | $121,137M | +33.0% | — |
| TTM | Capex | **$173,028M** | $107,656M | +60.7% | — |
| TTM | **Free cash flow** | **–$11,625M** | **+$13,481M** | **–$25.1B** | **The core bear case** |
| TTM | Net income | $135,281M | $70,623M | +91.6% | ~40% non-operating |
| TTM | D&A | $75,200M | $58,562M | +28.4% | Rising drag |
| TTM | Cash taxes paid | $6,635M | $11,788M | –43.7% | Unsustainably low |
| **Balance sheet** | Total assets | $1,095,689M | $818,042M (12/31/25) | **+33.9%** | Mostly non-cash |
| Balance sheet | Cash + securities | $176,113M | $132,610M | +32.8% | Ample liquidity |
| Balance sheet | Accounts receivable | $88,092M | $67,729M | +30.1% | **Outgrowing revenue — watch** |
| Balance sheet | Inventory | $38,184M | $38,325M | **–0.4%** | ~9.6x turns; excellent |
| Balance sheet | Accounts payable | $147,440M | $121,909M | +20.9% | Float intact |
| Balance sheet | **Long-term debt (total)** | **$132,995M** | $68,836M | **+93.2%** | **Major shift** |
| Balance sheet | Finance leases | $13,451M | $12,286M | +9.5% | — |
| Balance sheet | Operating leases | $96,320M | $89,252M | +7.9% | — |
| Balance sheet | Current ratio | 1.033x | 1.051x | –0.018x | Adequate, tightening |
| Balance sheet | Deferred revenue | $24,928M | $25,000M | Flat | Neutral |
| Capital | Acquisitions, H1 | $39,767M | $1,652M | +2,307% | **Inorganic revenue risk** |
| Capital | LT debt issued, H1 | $66,998M | $746M | +8,880% | Funding the capex gap |
| Capital | Buybacks / dividends | **None observed** | None | — | 0% capital return |
| Capital | Total contractual obligations | **$650,034M** | — | $78,084M due <12M | Spend is locked in |
| Capital | Interest expense | $1,314M | $516M | **+154.7%** | Coverage still 20.9x |
| Misc | Segments | 3 | 3 | — | No segment detail in dataset |
| Misc | Insider transactions | **DATA_UNAVAILABLE** | — | — | Not inferable |

---

**Bottom line for the trader:** AMZN's Q2 2026 is a **high-quality operating quarter wrapped in a low-quality earnings headline, financed by a balance sheet that has quietly become levered.** The trade is not about whether the numbers are big — they are — but about which half of the report the tape chooses to price on 2026-07-31. Fade EPS-driven euphoria; respect the margin and cash-flow-from-operations trajectory; and watch capex, TTM free cash flow, and the $122.3B mark-to-model equity line as the three variables that will determine whether this is an inflection or a peak.