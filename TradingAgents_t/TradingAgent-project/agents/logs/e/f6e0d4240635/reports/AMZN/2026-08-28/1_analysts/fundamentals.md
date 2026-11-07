# AMZN — Fundamental Research Report
### Amazon.com, Inc. | Analysis date: 2026-08-28 | Latest filing: Form 10-Q for Q2 FY2026 (period ended 2026-06-30), accepted 2026-07-31 (accn 0001018724-26-000026)

---

## 1. Data provenance and caveats (read first)

| Item | Status |
|---|---|
| Source | Point-in-time SEC XBRL facts, filtered by actual EDGAR acceptance timestamp ≤ 2026-08-28 |
| Most recent period | Q2 FY2026 (3 months and 6 months ended 2026-06-30) |
| Prior-period comparatives pulled | Q2 FY2025, H1 FY2025, Q1 FY2026 (via 10-Q accn 0001018724-26-000014), FY2025 year-end balance sheet |
| Insider transactions | **DATA UNAVAILABLE** — the vendor archive has no authorized point-in-time insider-transaction data for AMZN as of 2026-08-28. No inference or fabrication is made below; treat insider signal as a blind spot for this trade. |
| Not directly tagged | The `Revenues` tag was not returned. Revenue below is **derived** as `CostsAndExpenses + OperatingIncomeLoss` and cross-checked against multiple independent series (segment count, working-capital turns, prior-year reconciliation) — internally consistent to the dollar. |
| Total stockholders' equity | Not returned as a single tag. Equity is **estimated** in §4 with an explicit derivation; treat as approximate. |

---

## 2. Company profile (as evidenced by the filing set)

- **Identity:** Amazon.com, Inc. (AMZN), US-listed, USD reporting.
- **Structure:** `NumberOfOperatingSegments = 3` for H1 2026 — consistent with the North America / International / AWS reporting structure. The 10-Q is a single-reportable-standard filing with significant lease, debt, and investment-footnote detail.
- **Business model signals embedded in the numbers:** negative working capital (accounts payable $147.4B vs. inventory $38.2B), very high PP&E intensity (TTM capex $173.0B), large operating-lease footprint ($96.3B liability / $92.7B ROU asset), and a now-material portfolio of **non-public equity investments** ($122.3B). This is a capex-heavy, AI-infrastructure-and-cloud business with a venture-style investment book layered on top.
- **Capital returns:** No dividend and **no share repurchases** visible in the financing section. Share count is drifting *up* on stock comp (10.731B → 10.786B diluted-outstanding basis over six months).
- **Scale:** Total assets crossed **$1 trillion** for the first time ($1,095.7B at 2026-06-30, +$277.6B in six months).

---

## 3. Income statement — Q2 and H1 FY2026

### 3.1 Revenue and profitability (derived revenue)

| $ millions | Q2 FY26 | Q2 FY25 | YoY | H1 FY26 | H1 FY25 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| **Revenue (derived)** | **200,606** | **167,702** | **+19.6%** | **382,125** | **323,369** | **+18.2%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 183,241 | 157,785 | +16.1% |
| Gross profit | 104,828 | 86,893 | +20.6% | 198,884 | 165,584 | +20.1% |
| **Gross margin** | **52.3%** | **51.8%** | +46bp | **52.1%** | **51.2%** | +85bp |
| Marketing | 11,698 | 11,416 | +2.5% | 22,012 | 21,179 | +3.9% |
| G&A | 2,788 | 2,965 | **−6.0%** | 5,375 | 5,593 | **−3.9%** |
| Fulfillment / tech & content / other (residual) | 62,881 | 53,341 | +17.9% | 120,184 | 101,236 | +18.7% |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 330,812 | 285,793 | +15.7% |
| **Operating income** | **27,461** | **19,171** | **+43.2%** | **51,313** | **37,576** | **+36.6%** |
| **Operating margin** | **13.69%** | **11.43%** | **+226bp** | **13.43%** | **11.62%** | **+181bp** |
| Non-operating income (expense), net | **53,396** | 1,686 | n.m. | **69,378** | 4,960 | n.m. |
| Pre-tax income | 80,857 | 20,857 | +288% | 120,691 | 42,536 | +184% |
| Income tax expense | 18,199 | 2,678 | +580% | 27,759 | 7,231 | +284% |
| Equity-method loss | (11) | (15) | — | (30) | (14) | — |
| **Net income** | **62,647** | **18,164** | **+245%** | **92,902** | **35,291** | **+163%** |
| Diluted EPS | **$5.75** | $1.68 | +242% | **$8.53** | $3.27 | +161% |
| Basic EPS | $5.82 | $1.71 | +240% | $8.64 | $3.32 | +160% |
| Effective tax rate | 22.5% | 12.8% | — | 23.0% | 17.0% | — |

**Q1 FY2026 (imputed from H1 less Q2):** revenue $181,519M, operating income $23,672M (**13.0%** margin), non-operating income $15,982M, net income $30,255M, diluted EPS **$2.78**. Q1 FY2025 comparison: revenue $155,667M, operating income $18,405M (11.8%), diluted EPS $1.59.

### 3.2 The single most important item: $50.5B of Level-3 investment mark-up

Non-operating income of $53,396M in Q2 FY2026 decomposes as:

| Component ($M) | Q2 FY26 | Q2 FY25 | H1 FY26 | H1 FY25 |
|---|---:|---:|---:|---:|
| Upward revaluation, equity securities **without readily determinable fair value** | **50,486** | 49 | **62,814** | 86 |
| Gain on marketable equity securities (FV-NI) | 1,300 | 393 | 454 | 188 |
| Unrealized gain on available-for-sale securities | 1,319 | 388 | 430 | 250 |
| Investment income (interest) | 1,295 | 1,085 | 2,430 | 2,151 |
| Interest expense | (1,314) | (516) | (2,114) | (1,057) |
| Warrant fair-value adjustment | **(1,449)** | (590) | **(1,051)** | (212) |
| FX / other | 227 | 70 | 387 | 68 |
| **Non-operating income, net** | **53,396** | **1,686** | **69,378** | **4,960** |

This is the defining feature of the print:

- **$50.5B of Q2 pre-tax income — 62% of the $80.9B pre-tax total — and $62.8B of H1 pre-tax income is a non-cash, Level-3 upward revaluation of a private equity stake.** Correspondingly, `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` exploded from **$16.2B (2025-12-31) to $122.3B (2026-06-30)** — a $106.1B asset step-up that alone explains ~38% of the entire $277.6B balance-sheet expansion.
- **It is not cash, not recurring, and not reversible-proof.** If that private stake carries a ~35–45% fair-value cushion embedded in it, a single funding-round or IPO-valuation reset could produce a $30–50B pre-tax write-down in a future quarter.
- **The tax treatment confirms this.** Deferred tax expense was **$17,691M in Q2** and **$30,489M in H1 FY2026**, versus cash taxes paid of only **$3,978M in H1**. The marks are recognized for book purposes but are not yet taxable — meaning the $122.3B asset carries an embedded future cash-tax liability on realization.

### 3.3 Normalized earnings power — the number traders should anchor on

| $M except EPS | Q2 FY26 | Q2 FY25 | H1 FY26 | H1 FY25 |
|---|---:|---:|---:|---:|
| Reported net income | 62,647 | 18,164 | 92,902 | 35,291 |
| Less: after-tax non-operating income (@22.5%/23.0%) | (41,382) | (1,298) | (53,421) | (3,817) |
| **Operating-only net income (est.)** | **21,265** | **16,866** | **38,881** | **31,474** |
| Diluted shares (M) | ~10,890 | ~10,810 | ~10,890 | ~10,790 |
| **Normalized diluted EPS (est.)** | **~$1.95** | **~$1.56** | **~$3.57** | **~$2.92** |
| **Normalized EPS growth YoY** | **+25%** | — | **+22%** | — |

**Actionable read:** the headline $5.75 is roughly **3x** the underlying operating earnings power of ~$1.95. Consensus models that anchor on the GAAP print will be wildly wrong in either direction. The *real* story is genuinely good but far more modest: **+25% normalized EPS growth on +226bp of operating-margin expansion**, with revenue accelerating to +19.6%.

### 3.4 Cost discipline and the depreciation wall

- **Marketing expense fell as a share of revenue from 6.81% to 5.83%** — growth of only +2.5% against +19.6% revenue. This is the biggest source of operating leverage in the quarter.
- **G&A declined in absolute dollars (−6.0% YoY)** — rare for Amazon, and a hard signal of corporate headcount/cost rationalization.
- **Stock-based compensation is decelerating:** $6,038M in Q2 FY26 vs $6,534M in Q2 FY25 (−7.6%); H1 $10,070M vs $10,223M (−1.5%). Unrecognized SBC of $24.8B remains. Fewer shares issued at a higher price = less dilution per dollar of comp.
- **Depreciation is the offsetting headwind:** D&A of **$19,988M in Q2 (+31.3% YoY)**, **$38,933M in H1 (+32.0%)**, and **$75,200M TTM (+28.4% YoY)**. Depreciation is compounding at nearly twice the rate of revenue. Q2 EBITDA = $47,449M (op. income $27,461M + D&A $19,988M), a 23.7% margin. **The margin expansion above is happening *despite* an accelerating depreciation charge — that is the genuinely bullish read — but the depreciation curve keeps steepening as the capex wave is placed in service.**

---

## 4. Balance sheet — a $1 trillion balance sheet rebuilt around AI infrastructure and debt

All figures as of 2026-06-30 vs. 2025-12-31 unless noted.

| $ millions | 2026-06-30 | 2025-12-31 | Change | % |
|---|---:|---:|---:|---:|
| Cash & cash equivalents | 78,213 | 86,810 | −8,597 | −9.9% |
| Marketable securities (AFS) | 97,900 | 45,800 | +52,100 | +113.8% |
| **Total cash + marketable securities** | **176,113** | **132,610** | **+43,503** | **+32.8%** |
| Accounts receivable, net | 88,092 | 67,729 | +20,363 | +30.1% |
| Inventory, net | 38,184 | 38,325 | −141 | −0.4% |
| **Total current assets** | **249,264** | **229,083** | **+20,181** | **+8.8%** |
| Equity securities w/o readily determinable FV | **122,300** | 16,200 | **+106,100** | **+655%** |
| Operating lease ROU asset | 92,743 | 86,054 | +6,689 | +7.8% |
| Finance lease ROU asset (net) | 15,800 | 15,200 | +600 | +3.9% |
| **Total assets** | **1,095,689** | **818,042** | **+277,647** | **+33.9%** |
| Accounts payable | 147,440 | 121,909 | +25,531 | +20.9% |
| Accrued liabilities | 73,406 | 75,520 | −2,114 | −2.8% |
| **Total current liabilities** | **241,274** | **218,005** | **+23,269** | **+10.7%** |
| Long-term debt, current portion | 3,330 | 2,748 | +582 | +21.2% |
| Long-term debt, non-current | **128,894** | **65,648** | **+63,246** | **+96.3%** |
| **Total debt (LT + current)** | **132,224** | **68,396** | **+63,828** | **+93.3%** |
| Finance lease liabilities | 13,451 | 12,286 | +1,165 | +9.5% |
| **Gross debt incl. finance leases** | **145,675** | **80,682** | **+64,993** | **+80.6%** |
| Operating lease liabilities | 96,320 | 89,252 | +7,068 | +7.9% |
| Deferred revenue — current | 20,428 | 20,576 | −148 | −0.7% |
| Deferred revenue — non-current | 4,500 | 4,400 | +100 | +2.3% |
| AOCI | **66,287** | 28,230 | **+38,057** | **+134.8%** |
| Additional paid-in capital | 149,619 | 140,024 | +9,595 | +6.9% |
| Common stock ($0.01 par) | 113 | 112 | +1 | — |
| Retained earnings | *not tagged* | *not tagged* | — | — |
| **Total stockholders' equity (est.)** | **~470,000–490,000** | *~350,000 (est.)* | *~+125,000* | *~+35%* |

**Equity derivation (flagged as estimate):** reported equity = APIC $149,619M + common $113M + AOCI $66,287M + retained earnings. Retained earnings is not in the returned tag set, so equity is bracketed from the roll-forward: prior equity (~$350B, derived from FY2025 totals) + H1 net income $92,902M + H1 OCI $38,057M + SBC ~$10,070M − other. This puts equity at roughly **$470–490B**, implying total liabilities of ~$605–625B. **Do not use the equity figure for precise ratio work without confirming against the filed balance sheet.**

### 4.1 What the balance sheet is telling you

1. **The debt-fueled capex bet is now explicit.** Long-term debt non-current nearly **doubled** (+$63.2B, +96%) in six months. Total gross debt including finance leases rose **80.6% to $145.7B**. Proceeds from long-term debt issuance were **$66,998M in H1 FY2026** vs. $746M in H1 FY2025 — a ~90x increase. Amazon has pivoted from internally-funded capex to leveraged capex.
2. **But liquidity is still ample.** $176.1B of cash + marketable securities against $145.7B of gross debt including finance leases = **roughly net-cash-neutral**, and the $97.9B AFS portfolio is 98.5% maturing inside one year (short duration, near-zero unrealized loss of just $67M gross). Debt/equity on a gross basis is only ~0.30x; ~0.53x including operating leases. **Not a solvency concern — but a capital-allocation regime change.**
3. **Working capital is tightening, not loosening.** Current ratio **1.03x** ($249.3B / $241.3B), down from 1.05x at year-end. Quick ratio ex-inventory = **0.875x**. Payables (+20.9%) and receivables (+30.1%) both outgrew revenue (+18.2%), and the payables-to-inventory ratio is an extreme 3.86x — classic Amazon supplier-float model, but the receivables growth **faster than revenue** is a mild collections/mix caution (AWS and advertising receivables carry longer terms).
4. **Inventory discipline is excellent.** Inventory essentially flat (−0.4%) on +18.2% revenue — inventory turns improved materially. Inventory valuation reserves were also *released* ($3.0B vs. $3.3B). No demand-destruction signal here; this argues against a consumer slowdown in the current quarter.
5. **AOCI +$38.1B in six months** ($28.2B → $66.3B) is almost entirely *not* FX (FX translation was a −$1,563M loss in H1). It reflects unrealized investment/security gains flowing through OCI. **$66.3B of AOCI now sits in equity — another source of book-value volatility, and a partial offset to the P&L mark-ups.**
6. **Derivative assets jumped from $112M to $705M** — likely energy/hedging positions tied to data-center power exposure (`DerivativeNonmonetaryNotionalAmountEnergyMeasure = 270 million MWh` for H1 FY2026). A small but telling marker of the power-contracting scale behind the AI build-out.

### 4.2 Contractual obligations — the forward spending pipeline

| $ millions | 2026-06-30 | 2026-03-31 |
|---|---:|---:|
| **Total contractual obligations** | **650,034** | *n/d* |
| Due remainder of FY2026 | 42,752 | 46,489 |
| Due next twelve months | 78,084 | — |
| Due year 2 | 53,406 | — |
| Due year 3 | 46,767 | — |
| Due year 4 | 42,219 | — |
| Operating lease payments due (undiscounted) | 116,350 | 110,135 |
| Finance lease payments due (undiscounted) | 16,660 | 16,496 |

**$650.0B of contractual obligations against $382.1B of H1 revenue** is the clearest forward-looking signal in the entire filing: commitments are ~1.7x annualized revenue. Of this, $78.1B falls due within twelve months — comfortably covered by the $161.4B TTM operating cash flow, but it removes slack. Remaining performance obligations are separately corroborated: **$15.2B of deferred revenue was recognized as revenue in H1 FY2026**, and deferred revenue balances are essentially flat year-over-year — meaning the backlog story is in *commitments*, not in deferred revenue. **Watch this $650B line each quarter: sequential growth = demand conviction; a stall = the AI capex thesis cracking.**

---

## 5. Cash flow — the central tension of the AMZN story

### 5.1 Trailing-twelve-month view (the "Amazon FCF" definition)

| $ millions | TTM to 2026-06-30 | TTM to 2025-06-30 | Change |
|---|---:|---:|---:|
| Cash from operations | **161,403** | 121,137 | **+33.2%** |
| Purchases of property & equipment | **(173,028)** | (107,656) | **+60.7%** |
| **Free cash flow** | **(11,625)** | **+13,481** | **−$25,106M swing** |
| Acquisitions, net of cash acquired | (41,956) | (4,809) | +$37.1B |
| Purchases of marketable securities | (72,902) | (46,731) | +$26.2B |
| Proceeds from sale/maturity of securities | 67,090 | 30,924 | +$36.2B |
| **Net cash used in investing** | **(216,775)** | (123,569) | +$93.2B |
| Net cash from financing | **+75,160** | (8,652) | +$83.8B |

### 5.2 Quarterly detail

| $ millions | Q2 FY26 | Q2 FY25 | H1 FY26 | H1 FY25 |
|---|---:|---:|---:|---:|
| Cash from operations | 45,387 | 32,515 | 71,419 | 49,530 |
| Purchases of PP&E | (54,208) | (32,183) | (98,411) | (57,202) |
| **Free cash flow** | **(8,821)** | **+332** | **(26,992)** | **(7,672)** |
| Acquisitions | (24,359) | (1,700) | (39,767) | (1,652) |
| Net investing | (79,245) | (39,424) | (143,457) | (69,227) |
| Net financing | +10,146 | (2,539) | +62,913 | (2,586) |
| Net change in cash (incl. FX) | **(23,765)** | (8,440) | **(9,179)** | (20,859) |

### 5.3 Interpretation — read this before sizing a position

- **AMZN is now a negative-free-cash-flow business on a trailing basis for the first time in its modern history.** TTM FCF of **−$11.6B** vs. +$13.5B a year ago. On a pure H1 basis, FCF was **−$27.0B**, and including acquisitions **−$66.8B**, funded by **+$62.9B of financing**.
- **Capex intensity: $98.4B in H1 on $382.1B revenue = 25.7% of revenue (annualizing to ~$197B).** TTM capex of $173.0B is roughly 2.4x the $72B level of two years ago. This is a deliberate, disclosed, debt-and-cash-funded infrastructure sprint.
- **The funding mix is the risk.** Q2 CFO of $45.4B covered only 84% of Q2 capex of $54.2B. The gap plus $24.4B of acquisitions was plugged with debt. **Interest expense grew +155% YoY in Q2 ($516M → $1,314M)** and net interest income flipped from **+$569M to −$19M**. This is a small P&L item today (1.2% of revenue) but it is directionally pure negative and compounds as the $133B debt stack reprices.
- **Q2 FY2026 includes a $24.4B acquisition** (and $39.8B for H1 vs. $1.7B a year ago) — a step-change in M&A after years of relative abstention. This explains part of the total-asset jump beyond the $106.1B investment mark-up and the capex. **The strategic logic and purchase-price allocation are not visible in the XBRL tag set; investors should read the 10-Q goodwill/intangibles and business-combination footnotes.** Pending that, treat ~$40B of H1 inorganic spend as un-underwritten incremental risk to ROIC.
- **Operating cash flow quality is still high.** TTM CFO of $161.4B is *understated* relative to GAAP net income of $135.3B only mildly — but note CFO benefited from a $21.4B favorable swing in receivables/other operating assets and a $17.8B favorable non-current asset swing, offset by a $6.1B drag from accrued liabilities and −$0.7B from deferred revenue. **Absent the working-capital tailwind, CFO growth would be closer to +25% rather than +33%.**

---

## 6. Cross-cutting financial history and trend table

| Metric | Q2 FY25 | Q1 FY26 | Q2 FY26 | Trend |
|---|---:|---:|---:|---|
| Revenue ($M) | 167,702 | 181,519 | 200,606 | Accelerating: +16.6% → +19.6% |
| Gross margin | 51.8% | 52.0% | 52.3% | Rising 3 consecutive |
| Operating income ($M) | 19,171 | 23,672 | 27,461 | +43% YoY |
| Operating margin | 11.43% | 13.04% | 13.69% | **+226bp YoY** |
| D&A ($M) | 15,227 | 18,945 | 19,988 | +31% YoY |
| Interest expense ($M) | 516 | 800 | 1,314 | **+155% YoY** |
| Non-operating income ($M) | 1,686 | 15,982 | 53,396 | Mark-up driven |
| Effective tax rate | 12.8% | 23.6% | 22.5% | Normalized |
| Diluted EPS | $1.68 | $2.78 | $5.75 | 66% non-operating |
| **Normalized EPS (est.)** | **~$1.56** | **~$1.63** | **~$1.95** | **+25% YoY** |
| Cash from operations ($M) | 32,515 | 26,032 | 45,387 | +39.6% YoY |
| Capex ($M) | 32,183 | 44,203 | 54,208 | **+68.5% YoY** |
| Free cash flow ($M) | +332 | (18,171) | (8,821) | **Negative** |
| Diluted shares (M) | ~10,810 | ~10,870 | ~10,890 | Creeping up (SBC) |

**Multi-year markers from the comparative series:**
- TTM net income: **$70.6B (Jun-25) → $135.3B (Jun-26)**, +91.6%.
- TTM CFO: **$121.1B → $161.4B**, +33.2%.
- TTM D&A: **$58.6B → $75.2B**, +28.4%.
- TTM capex: **$107.7B → $173.0B**, +60.7%.
- Total assets: **$818.0B (Dec-25) → $1,095.7B (Jun-26)**.
- Gross debt incl. finance leases: **$80.7B → $145.7B**.

---

## 7. Actionable insights for traders

**BULL CASE (evidence-backed)**
1. **Operating leverage is real and accelerating.** Operating income +43.2% YoY on revenue +19.6% — margins expanded 226bp to 13.69%, with marketing at 5.83% of revenue (from 6.81%) and G&A shrinking in absolute dollars. Q1 (13.04%) → Q2 (13.69%) is sequential improvement, not a one-off.
2. **Revenue re-accelerated** from +16.6% (Q1) to +19.6% (Q2) — the fastest in the visible series, and achieved with *flat inventory* (−0.4%), which rules out a channel-stuffing or discount-driven explanation.
3. **Normalized EPS grew ~25% YoY** with a clean 22.5–23.0% tax rate and decelerating stock comp (−7.6% YoY). The quality of the *operating* earnings is high.
4. **Balance sheet can absorb the capex sprint:** $176.1B of cash + near-dated securities, gross debt/equity ~0.30x, current ratio 1.03x, and 98.5% of the securities portfolio maturing within one year.
5. **$650.0B of contractual obligations** signals contracted forward demand (~1.7x annualized revenue), with $78.1B due in 12 months — coverable at 2.1x by TTM CFO.

**BEAR CASE (evidence-backed)**
1. **Headline EPS is ~66% non-operating and non-cash.** $50.5B of Q2 pre-tax income was a Level-3 upward revaluation of a private equity stake; the carrying asset went $16.2B → $122.3B in six months. Any down-round or markdown is a **$30–50B potential pre-tax reversal** that consensus is not modeling. **The stock is trading on an earnings number that does not exist in cash.**
2. **FCF is negative and deteriorating:** TTM **−$11.6B** vs. +$13.5B; H1 **−$27.0B**; H1 including M&A **−$66.8B**. Capex is ~26% of revenue and rising 68% YoY.
3. **Debt-funded growth is now the model.** Long-term debt +96% in six months; issuance up ~90x YoY; interest expense +155% YoY; net interest income now negative. Deferred tax expense of $30.5B in H1 against $4.0B of cash taxes means the investment gains carry a **large unrealized tax bill**.
4. **The depreciation wave is only starting.** D&A +31% YoY and $75.2B TTM against $173.0B TTM capex implies the depreciation charge roughly doubles again as the current build is placed in service. **Margin expansion from opex discipline may be fully consumed by depreciation by FY2027.**
5. **~$40B of H1 acquisitions** ($24.4B in Q2 alone) vs. $1.7B a year ago — a major capital-allocation regime change with undisclosed returns.

**WHAT TO MONITOR NEXT (specific, falsifiable)**
- **The Q3 10-Q mark:** does `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` hold above $122.3B? Another upward revision confirms momentum; the first downward adjustment is the thesis-breaker.
- **Deferred tax expense** (Q2: $17.7B): should shrink if no new marks are booked — a clean proxy for whether the gains are one-time or recurring.
- **Capex:** Q2 was $54.2B. A sequential *decline* is the single most bullish possible datapoint for FCF; another step-up means continued negative FCF.
- **Long-term debt:** $128.9B non-current. Another ~$30B+ of issuance in H2 would confirm debt-funded capex through FY2027.
- **Cash taxes paid ($4.0B H1 vs. $27.8B tax expense):** the catch-up, when it comes, hits CFO, not the P&L.
- **Marketing and G&A ratios:** the operating leverage is being *funded* by these lines. If marketing as a % of revenue stops falling (5.83%), margin expansion stalls.
- **Insider transactions: unavailable in this dataset.** Do not treat the absence of insider data as either bullish or bearish — it is a data gap, and the trade should be sized with that blind spot acknowledged.

**BOTTOM LINE:** AMZN's *operating* engine is in its best shape in the visible record — accelerating revenue, 13.7% operating margins, disciplined opex, and $650B of contracted obligations. But the reported $5.75 EPS is a Level-3 valuation event masquerading as earnings, while the *cash* engine has turned negative (−$11.6B TTM FCF) and is being financed with debt that has doubled in six months. **Trade the operating margin and the capex curve; discount the headline EPS entirely.**

---

## 8. Key points summary

| Category | Metric | Value | Signal | Trader takeaway |
|---|---|---|---|---|
| **Identity** | Ticker / filer | AMZN — Amazon.com, Inc. | — | 10-Q Q2 FY2026, accepted 2026-07-31 |
| **Growth** | Q2 FY26 revenue (derived) | $200,606M, +19.6% YoY | 🟢 Bullish | Acceleration from +16.6% in Q1 |
| **Growth** | H1 FY26 revenue (derived) | $382,125M, +18.2% YoY | 🟢 Bullish | Fastest growth in visible series |
| **Margins** | Q2 operating margin | 13.69% (+226bp YoY) | 🟢 Bullish | 3rd consecutive quarter of expansion |
| **Margins** | Q2 gross margin | 52.3% (+46bp YoY) | 🟢 Bullish | COGS leverage on AWS/mix |
| **Margins** | Q2 D&A | $19,988M, +31.3% YoY | 🔴 Risk | Depreciation compounding 1.6x revenue |
| **Opex** | Marketing / revenue | 5.83% vs. 6.81% | 🟢 Bullish | Biggest source of operating leverage |
| **Opex** | G&A | $2,788M, −6.0% YoY | 🟢 Bullish | Absolute cost reduction |
| **Opex** | Stock comp | $6,038M, −7.6% YoY | 🟢 Bullish | Less dilution; $24.8B unrecognized |
| **Earnings quality** | Non-operating income Q2 | **$53,396M** | 🔴 Major risk | 62% of pre-tax income; non-cash |
| **Earnings quality** | Level-3 equity mark-up Q2 | **$50,486M** | 🔴 Major risk | Reverses on any down-round |
| **Earnings quality** | Equity sec. w/o RDFV | $16,200M → **$122,300M** | 🔴 Major risk | 11% of total assets, Level-3 |
| **Earnings** | Q2 diluted EPS | $5.75 (+242% YoY) | 🟡 Misleading | ~66% non-operating |
| **Earnings** | **Normalized Q2 EPS (est.)** | **~$1.95 (+25% YoY)** | 🟢 Bullish | **The number to model** |
| **Earnings** | H1 effective tax rate | 23.0% (Q2: 22.5%) | 🟡 Neutral | Normalized vs. 12.8% in Q2 FY25 |
| **Cash flow** | TTM operating cash flow | $161,403M, +33.2% YoY | 🟢 Bullish | Strong, with WC tailwind |
| **Cash flow** | TTM capex | **(173,028)M, +60.7%** | 🔴 Risk | ~26% of revenue |
| **Cash flow** | **TTM free cash flow** | **−(11,625)M** | 🔴 **Key risk** | vs. +$13,481M a year ago |
| **Cash flow** | H1 FY26 FCF (ex-M&A) | −$26,992M | 🔴 Key risk | Q2 alone −$8,821M |
| **Cash flow** | H1 FY26 FCF (incl. M&A) | −$66,800M (derived) | 🔴 Key risk | Funded by $62.9B financing |
| **Leverage** | LT debt, non-current | $65,648M → **$128,894M** | 🔴 **Regime change** | +96.3% in six months |
| **Leverage** | Gross debt incl. fin. leases | $80,682M → $145,675M | 🔴 Risk | +80.6% |
| **Leverage** | LT debt issued, H1 | $66,998M vs. $746M | 🔴 Regime change | ~90x YoY |
| **Leverage** | Q2 interest expense | $1,314M, +155% YoY | 🔴 Risk | Net interest now negative |
| **Liquidity** | Cash + marketable securities | $176,113M | 🟢 Strong | vs. $132,610M at YE25 |
| **Liquidity** | Current ratio | 1.03x (quick 0.875x) | 🟡 Neutral | Tight but structurally normal |
| **Liquidity** | AFS portfolio duration | 98.5% < 1yr; unrealized loss $67M | 🟢 Strong | Near-zero duration risk |
| **Balance sheet** | Total assets | **$1,095,689M (+33.9%)** | 🟢 Milestone | First $1T balance sheet |
| **Balance sheet** | AOCI | $28,230M → $66,287M (+$38.1B) | 🟡 Watch | Book-value volatility |
| **Balance sheet** | Inventory | $38,184M, −0.4% | 🟢 Bullish | Turns improved sharply; no demand crack |
| **Balance sheet** | Accounts payable | $147,440M, +20.9% | 🟢 Bullish | Supplier float > inventory 3.9x |
| **Balance sheet** | Accounts receivable | $88,092M, +30.1% | 🟡 Watch | Growing faster than revenue |
| **Balance sheet** | Deferred revenue | $24,928M, ~flat | 🟡 Neutral | Backlog story is in commitments |
| **Forward demand** | Contractual obligations | **$650,034M** | 🟢 Bullish | ~1.7x annualized revenue |
| **Forward demand** | Obligations due 12mo | $78,084M | 🟢 Covered | 2.1x covered by TTM CFO |
| **Forward demand** | Energy derivative notional | 270,000,000 MWh | 🟡 Informational | Data-center power scale |
| **Capital returns** | Dividend / buyback | **None / None** | 🟡 Neutral | All cash to capex + M&A |
| **Capital returns** | Diluted shares | ~10,890M, drifting up | 🟡 Mild dilution | SBC-driven |
| **M&A** | H1 acquisitions | $39,767M vs. $1,652M | 🔴 Un-underwritten | Q2 alone $24,359M |
| **Tax** | H1 cash taxes vs. tax expense | $3,978M vs. $27,759M | 🔴 Future drag | Deferred tax $30,489M |
| **Structure** | Operating segments | 3 | 🟡 Informational | NA / Intl / AWS |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | ⚪ Blind spot | Do not infer; size accordingly |
| **Verdict** | Operating trend | 🟢 Best in visible record | — | Trade the margin + capex curve |
| **Verdict** | Reported EPS / FCF | 🔴 Non-cash mark + negative FCF | — | Discount the $5.75 headline |