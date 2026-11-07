# AMZN — Fundamental Research Report (as of 2026-08-12)

## 1. Data provenance, scope and gaps

| Item | Status |
|---|---|
| Primary source | Point-in-time SEC facts, filtered by EDGAR acceptance time |
| Freshest filing | Q2 FY2026 Form 10-Q, accession `0001018724-26-000026`, accepted **2026-07-31 02:11 UTC** (12 days before the analysis date) |
| Prior filing | Q1 FY2026 10-Q, accession `0001018724-26-000014`, accepted 2026-04-30 |
| Fiscal year | Calendar year (Dec 31 year-end); Q2 = quarter ended 2026-06-30 |
| Reported segments | `NumberOfOperatingSegments = 3` (consistent with North America / International / AWS structure) |
| Insider transactions | **DATA UNAVAILABLE** — no authorized point-in-time insider archive for AMZN. No inference made. |
| Not available in feed | Top-line `Revenues` tag, segment-level revenue/operating income, total stockholders' equity line, share price / valuation multiples, consensus estimates, guidance. |

**Important derivation note:** the vendor feed contains no `Revenues` tag. Amazon's income statement format is *Net sales − Costs and expenses = Operating income*, so I derive revenue as **`CostsAndExpenses` + `OperatingIncomeLoss`**. This is internally consistent across every period in the feed (see checks below) but should be validated against the filed statement before trading off the exact figure. All revenue and revenue-ratio figures below are labeled "derived".

---

## 2. Company profile (context)

Amazon.com, Inc. (**AMZN**) operates three reportable segments — North America retail, International retail, and Amazon Web Services (AWS) — plus advertising, third-party seller services, subscription (Prime), and a large portfolio of equity investments (notably AI/technology stakes carried as *equity securities without readily determinable fair value*). The balance sheet shows the classic Amazon structure: very large operating-lease and finance-lease footprints, negative working capital funded by payables, heavy capex on fulfillment/technology infrastructure, and now a rapidly growing non-operating investment book.

---

## 3. Q2 FY2026 income statement (quarter ended 2026-06-30)

| $M | Q2 FY2026 | Q2 FY2025 | Δ y/y |
|---|---:|---:|---:|
| Revenue (derived) | **200,606** | 167,702 | **+19.6%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% |
| Gross profit (derived) | 104,828 | 86,893 | +20.6% |
| Gross margin | **52.3%** | 51.8% | +50 bp |
| Marketing | 11,698 | 11,416 | +2.5% |
| G&A | 2,788 | 2,965 | −6.0% |
| D&A (incl. finance-lease amort.) | 19,988 | 15,227 | **+31.3%** |
| Operating lease cost | 4,118 | 3,426 | +20.2% |
| Total costs & expenses | 173,145 | 148,531 | +16.6% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** |
| Operating margin | **13.7%** | 11.4% | +230 bp |
| Non-operating income, net | **53,396** | 1,686 | +3,067% |
| Pre-tax income | 80,857 | 20,857 | +288% |
| Income tax | 18,199 | 2,678 | +580% |
| Effective tax rate | 22.5% | 12.8% | +970 bp |
| **Net income** | **62,647** | 18,164 | **+245%** |
| Diluted EPS | **$5.75** | $1.68 | +242% |
| Diluted shares (implied) | ~10,895M | ~10,811M | +0.8% |
| SBC | 6,038 | 6,534 | −7.6% |

### What actually drove the quarter
Operating momentum was **genuinely strong**: revenue accelerated to +19.6% (vs +16.6% in Q1 FY2026), operating income grew 43%, and operating margin expanded 230 bp despite D&A rising ~90 bp as a share of sales (9.96% of revenue vs 9.08%). The margin gain came from **gross margin (+50 bp), marketing efficiency (−98 bp of revenue), G&A leverage (−38 bp)** and SBC discipline (−7.6% y/y).

But **the headline EPS is not operating EPS.** Roughly **$52.0B of the $53.4B non-operating income** is mark-to-market revaluation, dominated by the line item *upward price adjustment on equity securities without readily determinable fair value*: **$50.5B in Q2 alone** (and $12.3B in Q1, $62.8B for H1). Bridge:

| $M | Q2 FY2026 |
|---|---:|
| Operating income | 27,461 |
| Interest income | 1,295 |
| Interest expense | (1,314) |
| FX gain | 227 |
| Marketable-equity / AFS unrealized gains | 1,319 |
| Warrants fair-value adjustment | (1,449) |
| Non-marketable equity revaluation & other (residual) | ~52,018 |
| Pre-tax income | 80,857 |

**"Core" (ex-investment marks) Q2 FY2026 estimate:** pre-tax ≈ **$27.4B** → net ≈ **$21.3B** → **EPS ≈ $1.95**, versus **$1.59** core in Q2 FY2025 (+~23%). So the true operating EPS growth rate is ~20–23%, not +242%.

### Half-year FY2026 (Jan–Jun)

| $M | H1 FY2026 | H1 FY2025 | Δ |
|---|---:|---:|---:|
| Revenue (derived) | 382,125 | 323,369 | +18.2% |
| Operating income | 51,313 | 37,576 | +36.6% |
| Operating margin | 13.4% | 11.6% | +180 bp |
| Non-operating income | 69,378 | 4,960 | n.m. |
| Pre-tax income | 120,691 | 42,536 | +184% |
| Tax | 27,759 | 7,231 | — |
| Effective tax rate | 23.0% | 17.0% | +600 bp |
| Net income | 92,902 | 35,291 | +163% |
| Diluted EPS | $8.53 | $3.27 | +161% |
| Core EPS (est., op income + net interest, taxed at effective rate) | **~$3.65** | ~$2.97 | **+~23%** |

Q1 FY2026 in isolation (H1 minus Q2): revenue ~$181,519M, operating income $23,852M (13.1% margin), net income $30,255M (including a $12.3B non-marketable revaluation gain). **Growth accelerated Q1→Q2 (+16.6% → +19.6%).**

---

## 4. Earnings quality — the single most important fundamental issue

1. **$62.8B of pre-tax non-cash revaluation gains in H1 FY2026** (vs $86M in H1 FY2025). Tax-effected at ~23%, that is ~$48B of net income — **more than half of reported H1 net income ($92.9B)**.
2. **The asset backing those marks exploded:** *equity securities without readily determinable fair value* went from **$16.2B (2025-12-31) to $122.3B (2026-06-30)** — now **11.2% of total assets**. This is a concentrated, model-valued position in AI-era private companies whose marks are not observable in a market.
3. **OCI is also running hot:** comprehensive income H1 FY2026 = **$130,959M** vs net income $92,902M, i.e., **+$38,057M of other comprehensive income**, even though FX translation was **−$1,563M**. That implies roughly **$39.6B of securities/other OCI gains**, consistent with the reported ~$92B tax-basis unrealized gain figure for H1. AOCI jumped from **$28,230M → $66,287M**. This is volatile, reversible equity, not operating capital.
4. **Mark-to-market cuts both ways and already has:** warrants fair-value adjustment was a **−$1,449M loss in Q2** (vs −$590M in Q2 FY2025), and the tax rate is rising sharply (22.5% Q2 vs 12.8%; 23.0% H1 vs 17.0%), with **deferred tax expense of $17.7B in Q2 / $30.5B in H1 / $41.4B LTM** — i.e., most of the tax charge on the gains is non-cash.

**Trading implication:** the reported P/E on AMZN is being optically compressed by gains that carry no cash and can reverse. Any model that capitalizes headline EPS or book value (which includes both the $122B equity book and the $66B AOCI) will misprice AMZN. Use operating income, OCF, and core EPS.

---

## 5. Balance sheet (2026-06-30 vs 2025-12-31)

| $M | 2026-06-30 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 78,213 | 86,810 | −9.9% |
| AFS marketable securities | 97,900 | 45,800 | +113.8% |
| **Cash + marketable securities** | **176,113** | 132,610 | **+32.8%** |
| Accounts receivable, net | 88,092 | 67,729 | +30.1% |
| Inventory, net | 38,184 | 38,325 | **−0.4%** |
| Current assets | 249,264 | 229,083 | +8.8% |
| **Equity securities w/o determinable FV** | **122,300** | 16,200 | **+654.9%** |
| Operating lease ROU asset | 92,743 | 86,054 | +7.8% |
| **Total assets** | **1,095,689** | 818,042 | **+33.9%** |
| Accounts payable | 147,440 | 121,909 | +21.0% |
| Accrued liabilities | 73,406 | 75,520 | −2.8% |
| Current liabilities | 241,274 | 218,005 | +10.7% |
| Long-term debt (total) | **132,995** | 68,836 | **+93.2%** |
| — of which noncurrent | 128,894 | 65,648 | +96.3% |
| Finance lease liabilities | 13,451 | 12,286 | +9.5% |
| Operating lease liabilities | 96,320 | 89,252 | +7.9% |
| Contract liabilities (current + noncurrent) | 24,928 | 24,976 | flat |
| AOCI | 66,287 | 28,230 | +134.8% |
| Additional paid-in capital | 149,619 | 140,024 | +6.9% |
| Shares outstanding | 10,783M | 10,731M | +0.5% (10,786.3M at 2026-07-22) |

**Read-through:**
- **Liquidity is fine but not fortress-like on a current-ratio basis:** current ratio **1.03** (249,264 / 241,274), essentially unchanged from 1.05. The perceived liquidity is backstopped by $176B of cash + securities, but $97.9B of that is AFS paper and the equity-stake book is illiquid.
- **Working capital discipline is excellent in inventory** (flat inventory on +18% revenue) but **receivables are growing faster than revenue (+30.1% vs +18.2%)**; the allowance for doubtful accounts rose to $2.8B from $2.4B (+16.7%) — slightly *lagging* AR growth. Watch this in Q3.
- **Gross leverage roughly doubled in six months.** Total debt of **$133.0B** plus $13.5B finance leases = **$146.4B**, vs $81.1B at YE2025 (+80%). Netting available liquidity of $176.1B, AMZN is still in a modest **net cash** position (−$30.4B net debt), but netting only cash ($78.2B) leaves **net debt ~$68B**.
- **No equity issuance/buyback signal is evident:** shares outstanding rose 0.5% (SBC dilution), no treasury activity is visible in the feed.

---

## 6. Cash flow, capex and free cash flow — the bear case lives here

| $M | Q2 FY2026 | Q2 FY2025 | H1 FY2026 | H1 FY2025 | LTM (Jul-25→Jun-26) | Prior LTM |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash flow | 45,387 | 32,515 | 71,419 | 49,530 | **161,403** | 121,137 |
| Capex (productive assets) | (54,208) | (32,183) | (98,411) | (57,202) | **(173,028)** | (107,656) |
| **Free cash flow (OCF − capex)** | **(8,821)** | **+332** | **(26,992)** | (7,672) | **(11,625)** | **+13,481** |
| Acquisitions, net of cash | (24,359) | (1,700) | (39,767) | (1,652) | (41,956) | (4,809) |
| Investing cash flow | (79,245) | (39,424) | (143,457) | (69,227) | (216,775) | (123,569) |
| Financing cash flow | +10,146 | (2,539) | **+62,913** | (2,586) | **+75,160** | (8,652) |

**Key facts:**
- **LTM free cash flow is NEGATIVE (−$11.6B)** versus **+$13.5B** in the prior LTM period — a ~$25B deterioration. H1 FY2026 FCF was **−$27.0B**, more than 3.5x the H1 FY2025 deficit.
- **Capex is running at 27.0% of Q2 revenue (25.7% H1)** and grew **+61% LTM** — a genuine infrastructure supercycle. LTM D&A of **$75.2B (+28%)** is the lagging consequence and will keep pressuring reported margins.
- **The gap is being funded with debt, not operations:** LTM long-term debt issuance **$81.9B** (H1 FY2026 $67.0B), short-term debt issuance $20.8B, and total debt nearly doubled. Q2 interest expense of **$1,314M was +155% y/y** (from $516M).
- **$42.0B of acquisitions in LTM** ($39.8B in H1 FY2026, $24.4B in Q2 alone) — an unusually large M&A burst that also explains part of the balance-sheet expansion. This is incremental execution/impairment risk that did not exist a year ago.
- Cash taxes paid remain low relative to book tax (**$2,655M in Q2 vs $18,199M provision; $6,635M LTM**) — a genuine cash-flow tailwind, but it also means the reported tax line overstates near-term cash drag, while creating a future deferred-tax reversal overhang.

---

## 7. Contractual obligations and lease structure

- **Total contractual obligations: $650,034M** at 2026-06-30 — of which **$78,084M due within 12 months**, $53,406M year 2, $46,767M year 3, $42,219M year 4 (the bulk of the remainder is beyond 4 years — consistent with long-dated purchase commitments for compute/infrastructure).
- **Operating leases:** liability **$96,320M**; undiscounted payments **$116,350M**; weighted-average discount rate **3.9%** (up from 3.7%). H1 operating lease cost $8,035M (+20.6% y/y); H1 lease payments $7,804M.
- **Finance leases:** liability $13,451M; undiscounted payments $16,660M.
- **Contract liabilities** of $24,928M, with **$15,200M of H1 FY2026 revenue recognized from the opening balance** — a solid, high-visibility backlog characteristic (AWS commitments/Prime).

---

## 8. Segment / operational color available in the feed

- Three reportable segments confirmed; no segment-level revenue or operating income is exposed in this dataset, so **AWS vs retail mix cannot be quantified here** — that is a material gap for anyone trading the AI narrative.
- **Share-based compensation is shrinking** (H1 $10,070M vs $10,223M; Q2 $6,038M vs $6,534M, −7.6%), with **$24.8B of unrecognized SBC cost** remaining — modest future dilution pressure (~2.3% of a year's revenue-equivalent, spread over the vesting period).
- **Inventory valuation reserves declined** to $3,000M from $3,300M (good), and inventory units are flat on +18% revenue — inventory turns ~10x annualized (COGS $95.8B × 4 / $38.2B), i.e., ~36 days. Best-in-class.

---

## 9. Insider transactions

**Unavailable.** The B-project data package contains no authorized point-in-time insider-transactions archive for **AMZN** as of 2026-08-12. I am explicitly **not** inferring or fabricating insider buying or selling. Anyone needing this signal must source Form 4 data directly; treat any figure produced by another system as unverified.

---

## 10. Actionable insights for traders

**Constructive (buy-side) evidence**
1. **Operating acceleration is real and broad:** revenue +19.6% y/y (accelerating from +16.6%), operating income +43%, operating margin 13.7% (+230 bp). This is the highest-quality part of the print.
2. **Cost discipline beyond COGS:** marketing down ~100 bp of revenue, G&A down, SBC down 7.6% y/y — expense leverage is coming from multiple lines, not a one-off.
3. **OCF +33% LTM ($161.4B)** is the strongest cash-generation evidence in the dataset and comfortably services the new debt load (Q2 interest coverage ≈ 21x operating income / interest).
4. **Optionality is being capitalized on the balance sheet:** $122.3B of private AI-era equity stakes, marked up $62.8B in six months. If AI private marks hold, this is a hidden asset; if the company monetizes, it is a funding source for capex.
5. **Inventory at flat dollars on +18% revenue** signals no demand air-pocket and no channel stuffing.

**Cautions (sell-side / risk-management) evidence**
1. **Headline EPS is roughly 3x overstated vs operating reality** — $5.75 reported vs ~$1.95 core in Q2. Anyone anchoring on "EPS +242%" is mis-modeling AMZN. Expect the market to eventually re-rate on core earnings.
2. **Negative free cash flow (−$11.6B LTM; −$27.0B H1)** with capex at 26–27% of revenue. The FCF-based valuation floor has disappeared; the equity now depends on the capex eventually earning a return.
3. **Debt-funded expansion:** total debt +93% in six months to $133.0B, interest expense +155% y/y, and a rising effective tax rate (17% → 23%). Both are structural EPS headwinds through FY2027.
4. **Reversal risk on $122.3B of Level-3-ish equity marks.** Already visible: warrants mark-to-market losses of −$1.45B in Q2, and $38.1B of the H1 comprehensive income sits in AOCI and is recyclable/reversible. A single down-round in a key AI holding could produce a multi-billion non-cash loss and an EPS "air pocket."
5. **Prioritize Q3 FY2026 (report expected late Oct 2026) for three specific checks:** (a) does capex growth decelerate below OCF growth — i.e., does FCF turn positive; (b) does the $122.3B equity-stake balance grow again (concentration risk) or get monetized; (c) does AR growth (+30%) converge back toward revenue growth (+18%) and does the allowance keep pace.

**Positioning framework (fundamental, no price data available to compute multiples)**
- **Base case:** operating income growth in the high-20s to 30s% with margin near 13–14%; OCF growth >20%; FCF near breakeven only if capex growth moderates. That supports owning AMZN on **operating income and OCF**, not EPS.
- **Bear trigger:** capex guided up again while OCF growth decelerates, or any write-down/impairment on the $122B private-equity book. Either converts the "hidden asset" story into a leverage story.
- **Bull trigger:** decelerating capex intensity with sustained ~19% revenue growth → sharply positive FCF in FY2027, plus monetization/mark-up of AI stakes. That is the path to a genuine re-rating.
- **Valuation discipline:** do not use reported P/E, reported EPS growth, or book value (which now embeds both the $122.3B equity marks and $66.3B AOCI). Use EV/OCF, EV/operating income, and P/FCF-on-normalized-capex.

---

## 11. Key-points summary table

| Category | Metric | Latest value | Comparison | Interpretation |
|---|---|---|---|---|
| Filing | Q2 FY2026 10-Q accepted | 2026-07-31 | 12 days pre-analysis | Fresh, authoritative data |
| Growth | Revenue (derived) | $200,606M (Q2) | +19.6% y/y; Q1 +16.6% | Accelerating |
| Growth | H1 revenue (derived) | $382,125M | +18.2% y/y | Strong |
| Profitability | Operating income | $27,461M (Q2) | +43.2% y/y | Best-in-class leverage |
| Profitability | Operating margin | 13.7% (Q2) | +230 bp y/y | Expanding |
| Profitability | Gross margin | 52.3% (Q2) | +50 bp y/y | Improving mix |
| Profitability | D&A | $19,988M (Q2) | +31.3% y/y; 10.0% of rev | Capex hangover |
| Earnings quality | Non-operating income | $53,396M (Q2) | vs $1,686M y/y | ~$52B is mark-to-market |
| Earnings quality | Non-marketable equity revaluation | $50,486M (Q2); $62,814M (H1) | vs $49M in Q2 FY25 | Non-cash, non-recurring |
| Earnings | Reported diluted EPS | $5.75 (Q2); $8.53 (H1) | +242% / +161% | Heavily inflated |
| Earnings | Core EPS (est., ex-marks) | ~$1.95 (Q2); ~$3.65 (H1) | +~23% y/y | True run-rate |
| Tax | Effective tax rate | 22.5% (Q2); 23.0% (H1) | vs 12.8% / 17.0% | Structural headwind |
| Cash flow | Operating cash flow | $45,387M (Q2); $161,403M LTM | +33% LTM | Strong |
| Cash flow | Capex | $54,208M (Q2); $173,028M LTM | +61% LTM; 27% of rev | Supercycle |
| Cash flow | Free cash flow | −$8,821M (Q2); **−$11,625M LTM** | vs +$13,481M prior LTM | **Negative — key risk** |
| M&A | Business acquisitions | $39,767M H1; $41,956M LTM | vs $1,652M H1 FY25 | Large, new risk |
| Balance sheet | Total assets | $1,095,689M | +33.9% in 6 months | Investment-mark driven |
| Balance sheet | Cash + AFS securities | $176,113M | +32.8% | Ample liquidity |
| Balance sheet | Equity securities w/o determinable FV | **$122,300M** | vs $16,200M at YE25 | 11.2% of assets, mark risk |
| Balance sheet | Total debt | $132,995M | +93.2% in 6 months | Leverage doubled |
| Balance sheet | Finance + operating lease liabilities | $13,451M / $96,320M | +9.5% / +7.9% | Long-dated fixed claims |
| Liquidity | Current ratio | 1.03 | vs 1.05 | Thin but stable |
| Leverage | Interest expense | $1,314M (Q2) | +155% y/y | Cost of debt now visible |
| Working capital | Inventory | $38,184M | −0.4% in 6 months | Excellent turns (~36 days) |
| Working capital | Accounts receivable | $88,092M | +30.1% vs rev +18.2% | Watch for collection drag |
| Equity | AOCI | $66,287M | +$38,057M in H1 | Volatile, recyclable |
| Equity | Comprehensive income (H1) | $130,959M | vs NI $92,902M | +$38.1B non-P&L gains |
| Equity | Shares outstanding | 10,783M (10,786.3M at 2026-07-22) | +0.5% | SBC dilution only |
| Compensation | SBC | $6,038M (Q2) | −7.6% y/y; $24.8B unrecognized | Discipline improving |
| Obligations | Total contractual obligations | $650,034M | $78,084M due ≤12m | Large long-dated commitments |
| Backlog | Contract liabilities / H1 recognized | $24,928M / $15,200M | roughly flat | Stable commitment base |
| Insider | Form 4 activity | **Not available** | — | Do not infer |
| Missing | Segment revenue/op income, total equity, price, guidance | — | — | Material gaps for valuation |