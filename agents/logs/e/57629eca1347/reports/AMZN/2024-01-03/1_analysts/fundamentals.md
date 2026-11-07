# AMZN — Fundamental Deep Dive (Point-in-Time as of 2024-01-03)

**Ticker:** AMZN | **Company:** Amazon.com, Inc. | **Latest data in hand:** Form 10-Q for the quarter ended **2023-09-30**, accepted by EDGAR **2023-10-27 02:36 UTC** (accn 0001018724-23-000018), plus the Q2-2023 10-Q (accepted 2023-08-04).

---

## 0. Data Coverage & Integrity Notes (read first)

| Item | Status |
|---|---|
| Most recent filing available at 2024-01-03 | Q3-2023 10-Q (filed 2023-10-27) — Q4/FY2023 results were **not yet published** |
| Income statement, balance sheet, cash flow | ✅ Available for Q3-23, 9M-23, with 9M-22 / Q3-22 / 12-31-2022 comparatives |
| Revenue line item in XBRL cache | ⚠️ **Not tagged** in the returned dataset. Revenue is **derived** as `CostsAndExpenses + OperatingIncomeLoss` (identity holds exactly; cross-checked vs. reported figures) |
| FY2022 10-K figures | ⚠️ Not present in the point-in-time cache — I do **not** extrapolate annual FY2022 revenue/op income |
| Segment P&L (NA / Intl / AWS) | ⚠️ Not in dataset (only `NumberOfOperatingSegments = 3`) |
| Price / valuation multiples | ❌ Not available from these tools |
| **Insider transactions** | ❌ **DATA_UNAVAILABLE** — the vendor has no authorized point-in-time insider archive for AMZN as of 2024-01-03. **No insider activity is inferred or fabricated in this report.** |

All figures in **USD millions** unless stated.

---

## 1. Company Profile (per filing structure)

Amazon.com, Inc. is a global technology and e-commerce conglomerate operating through **three reportable segments** (per XBRL `NumberOfOperatingSegments = 3`): **North America**, **International**, and **Amazon Web Services (AWS)**. Revenue streams captured in the filing include online stores, third-party seller services (1P/3P marketplace, fulfillment, advertising), subscription services (Prime), physical stores, and AWS cloud infrastructure/AI services. Operating footprint is asset-heavy: **$73.9B of operating lease liabilities** and **$12.5B of finance lease liabilities** on the 9/30/23 balance sheet, plus a **$284.4B contractual-obligation backlog** (purchase obligations, leases, debt) — i.e., this is a fixed-cost, scale-driven model where volume leverage is the primary margin driver.

---

## 2. Income Statement — The Margin Inflection Is Real

| Metric | Q3-2023 | Q3-2022 | Δ |
|---|---|---|---|
| Revenue (derived) | **143,083** | 127,101 | **+12.6%** |
| Cost of goods & services | 75,022 | 70,268 | +6.8% |
| Gross profit | **68,061** | 56,833 | +19.8% |
| **Gross margin** | **47.6%** | 44.7% | **+287 bp** |
| Total costs & expenses | 131,895 | 124,576 | +5.9% |
| **Operating income** | **11,188** | 2,525 | **+343%** |
| **Operating margin** | **7.82%** | 1.99% | **+583 bp** |
| Non-operating income/(expense) | +1,001 | +419 | — |
| Pre-tax income | 12,189 | 2,944 | +314% |
| Tax | 2,306 | 69 | ETR 18.9% vs 2.3% |
| **Net income** | **9,879** | 2,872 | **+244%** |
| **Diluted EPS** | **$0.94** | $0.28 | **+236%** |

**Nine-month comparison (the more robust read, removes Q3 seasonality):**

| Metric | 9M-2023 | 9M-2022 | Δ |
|---|---|---|---|
| Revenue (derived) | **404,824** | 364,779 | **+11.0%** |
| Cost of goods & services | 212,186 | 203,191 | **+4.4%** |
| Gross profit | 192,638 | 161,588 | **+19.2%** |
| Gross margin | 47.6% | 44.3% | +328 bp |
| **Operating income** | **23,643** | 9,511 | **+148.6%** |
| **Operating margin** | **5.84%** | 2.61% | **+323 bp** |
| Interest expense | (2,469) | (1,673) | +47.6% |
| Interest & investment income | 2,048 | 544 | 3.8x |
| Net interest position | **(421)** | (1,129) | 63% better |
| Non-operating income/(expense) | +228 | **(14,485)** | Rivian mark swing |
| Pre-tax income | 23,871 | (4,974) | nm |
| Tax expense/(benefit) | 4,058 | (1,990) | ETR 17.0% |
| **Net income** | **19,801** | **(3,000)** | **+$22.8B swing** |
| **Diluted EPS** | **$1.89** | $(0.29) | nm |

### The decomposition that matters
- **Incremental operating margin on 9M-23 = 35.3%** ($14,132M of incremental operating income on $40,045M of incremental revenue). The blended 5.8% margin massively understates the marginal economics of the current cost base.
- **100% of the operating-income expansion came from gross margin.** Non-COGS operating expenses grew +11.1% — *exactly* in line with revenue (+11.0%), so they were effectively flat as a % of sales. COGS grew only **4.4%** against **11.0%** revenue growth → **+328 bp of gross margin**, contributing ~$13.3B of the $14.1B delta.
- **The 2022 "one-time" drag is gone.** 9M-22 non-operating expense was **–$14,485M**, driven by **–$11,300M of equity-securities FV losses** (Rivian). 9M-23 non-operating was **+$228M**, including **+$1,000M of equity FV gains**. So the earnings *level* shift is ~50% operating, ~50% mark-to-market normalization — but the **operating** improvement is the durable part.

### Expense-line detail (9M-23 vs 9M-22, % of revenue)
| Line | 9M-23 | 9M-22 | Comment |
|---|---|---|---|
| Marketing | 31,468 (7.77%) | 29,420 (8.07%) | +7.0% — **leverage**, grew below revenue |
| G&A | 8,806 (2.18%) | 8,558 (2.35%) | +2.9% — near-frozen, layoff/overhead discipline |
| Depreciation & amortization | 34,843 (8.61%) | 29,236 (8.01%) | **+19.2%** — the catch-up from the 2021-22 capex binge |
| Share-based comp | 17,704 (4.37%) | 14,015 (3.84%) | **+26.3%** — real cost, non-cash |
| Operating lease cost | 7,799 | 6,472 | +20.5% |
| Finance-lease ROU amortization | 4,524 | 4,586 | –1.4% (fleet/warehouse leases rolling off) |
| Asset impairment | 420 | 350 | minimal |
| Contract termination loss | 200 | 300 | minimal |

**Quality read:** earnings are *clean*. Impairments ($420M) and contract-termination charges ($200M) are ~2.6% of operating income — no big-bath story. The main "non-operating" boost is the **+$1,196M of equity-securities FV gains in Q3-23** (~$0.09–0.11 of EPS after tax), which traders should strip when annualizing.

---

## 3. Cash Flow — The Core Bull Case (FCF Inflection)

| Metric | 9M-2023 | 9M-2022 | TTM to 9/30/23 | Prior TTM | 
|---|---|---|---|---|
| Operating cash flow | **42,481** | 17,579 | **71,654** | 39,665 |
| Capex (productive assets) | **(38,141)** | (47,053) | **(54,733)** | (65,988) |
| **FCF (OCF – capex)** | **4,340** | **(29,474)** | **16,921** | **(26,323)** |
| Finance-lease principal repayments | (3,605) | (6,301) | (5,245) | (8,561) |
| **FCF after finance-lease principal** | **735** | (35,775) | **11,676** | (34,884) |
| Net cash used in investing | (37,232) | (26,780) | (48,053) | (39,360) |
| Net cash from/(used in) financing | (9,133) | +9,632 | (9,047) | +6,532 |
| FX effect on cash | (288) | (1,730) | +349 | (1,836) |
| **Net change in cash** | **(4,172)** | (1,299) | **+14,903** | +5,001 |
| Net income (TTM) | 19,801 (9M) | (3,000) | **20,079** | 11,323 |

**Key observations:**
1. **TTM OCF +80.6% ($39.7B → $71.7B) while TTM capex fell –17.1% ($66.0B → $54.7B).** That two-way squeeze flipped FCF from **–$26.3B to +$16.9B** in twelve months — a **$43.2B swing**. Q3 alone: OCF $21.2B vs $11.4B (+86%), capex $12.5B vs $16.4B (–23.8%) → **Q3 FCF $8.7B vs –$5.0B**.
2. **Cash conversion is exceptional: 9M OCF / net income = 2.15x.** Part of that is non-cash D&A ($34.8B) and SBC ($17.7B).
3. **Cash flow was achieved *despite* working-capital headwinds**, which makes the quality *better*, not worse:
   - Accrued liabilities & other operating liabilities: **–$9,022M** in 9M-23 (vs –$7,335M 9M-22)
   - Accrued liabilities on balance sheet: **$58,812M vs $62,566M** at 12/31/22 (**–6.0%**)
   - Accounts payable: **$72,004M vs $79,600M** at 12/31/22 (**–$7,596M**, –9.5%)
   - AR & other operating assets: **–$10,364M** use of cash
   → Amazon is **not** flattering OCF by stretching payables; it is paying suppliers faster/normalizing as inventory velocity improves (inventory valuation reserves cut to $2.6B from $2.8B). This is a higher-quality cash number than a payable-stretch.
4. **Cash taxes running hot vs book:** cash taxes paid $6,982M (9M-23) vs book tax expense $4,058M; cash tax is **29% of pre-tax income vs a 17.0% book ETR** — the gap is deferred tax benefits (–$4,412M 9M-23, –$7,779M TTM), largely SBC/ capitalization-related. Do **not** model FCF off the 17% book ETR; assume a rising cash tax trajectory.

---

## 4. Balance Sheet — Deleveraging into a Net-Cash Position

| Item | 9/30/2023 | 12/31/2022 | Δ |
|---|---|---|---|
| Cash & equivalents | 49,605 | 53,888 | –7.9% |
| Marketable securities (AFS, FV) | 49,871 | n/a | — |
| **Cash + securities** | **~99,476** | ~110,000 | –9.5% |
| Accounts receivable, net | 43,420 | 42,360 | +2.5% |
| Inventory, net | 35,406 | 34,405 | +2.9% |
| **Current assets** | **142,995** | 146,791 | –2.6% |
| **Total assets** | **486,883** | 462,675 | **+5.2%** |
| Accounts payable | 72,004 | 79,600 | **–9.5%** |
| Accrued liabilities | 58,812 | 62,566 | –6.0% |
| Deferred revenue (current) | 14,398 | 13,227 | +8.8% |
| Deferred revenue (noncurrent) | 2,700 | 2,900 | –6.9% |
| **Current liabilities** | **145,214** | 155,393 | –6.6% |
| LT debt — current portion | 5,995 | 2,999 | +99.9% |
| LT debt — noncurrent | **61,098** | 67,150 | –9.0% |
| **Total LT debt** | **~67,093** | ~70,149 | **–4.4%** |
| Finance lease liabilities | 12,466 | 15,783 | **–21.0%** |
| Operating lease liabilities | 73,902 | 69,040 | **+7.0%** |
| Operating lease ROU asset | 70,758 | 66,123 | +7.0% |
| APIC | 92,711 | 75,066 | +23.5% (SBC + stock issuance) |
| AOCI | (5,003) | (4,487) | –516 |
| Shares outstanding | 10,330M | 10,242M | +0.9% |

**Derived solvency metrics:**
- **Current ratio: 0.985x** (142,995 / 145,214) — up from **0.945x** at 12/31/22. Still **below 1.0**, structurally normal for Amazon but a genuine liquidity constraint if credit markets tighten.
- **Quick ratio: 0.74x** ((142,995 – 35,406) / 145,214).
- **Net debt (ex-leases): ~–$19.9B, i.e., a NET CASH position.** (67,093 debt + 12,466 finance leases – 99,476 cash & securities.)
- **Including operating leases (a real fixed obligation): ~+$54.0B of net obligations** vs. TTM OCF of $71.7B → **~0.75x OCF**. Manageable.
- **Interest coverage: 9.6x** (9M EBIT 23,643 / interest 2,469), up from **5.7x** (9,511 / 1,673). With investment income of $2,048M, **net interest is nearly neutral** ($-421M for 9M; **Q3 net interest ≈ –$30M**).
- **Total undiscounted lease commitments: $103.4B** (operating $88.8B + finance $14.6B). **Total contractual obligations: $284.4B.**
- **Estimated book equity ~$183B** (derived: 12/31/22 equity + 9M net income + SBC + AOCI move) → **ROE (annualized 9M) ≈ 16%**, vs. a TTM ROA of only ~4.2%. Equity returns are improving off a low asset-turnover base.

**Capital allocation signals:**
- **Share repurchases: $0 in all of 2023** ($0 in 9M-23 and TTM), versus **$6,000M in 9M-22**. Buyback was fully suspended — cash is going to debt paydown and capex.
- **No long-term debt issued in 2023** ($0 in 9M-23); **$3,386M repaid**. FY-to-date TTM: $8,235M issued, $4,643M repaid.
- **Short-term debt actively churned:** $17,395M proceeds vs. $19,339M repayments in 9M — modest net paydown.
- **Dilution:** shares outstanding **+0.9%** YTD (10,242M → 10,330M; 10,334.0M as of 2023-10-18 cover date). Diluted share count in Q3 was ~10,510M. **Unrecognized SBC expense of $23.3B** = ~1.3 years of the current $17.7B/9M run-rate — a persistent 4.4%-of-revenue non-cash cost and a slow structural dilution drift (~1%/yr).

---

## 5. Insider Transactions

**DATA_UNAVAILABLE.** The configured news/vendor package contains **no authorized, point-in-time insider-transaction archive for AMZN as of 2024-01-03**. I therefore make **no claim** about insider buying or selling for this name; any figure asserted elsewhere would be unverifiable. Treat insider flow as an open item to source separately before sizing a position.

---

## 6. Actionable Insights for Traders

### Bullish evidence (high conviction, from primary filings)
1. **Durable gross-margin re-rating, not a one-off.** COGS +4.4% vs revenue +11.0% for 9M-23 is a **structural** cost reset (regionalized US fulfillment network, headcount rationalization, lower unit shipping costs, AWS cost actions) now flowing through the P&L. Gross margin of 47.6% is the single most important number in the filing.
2. **Incremental operating margin of 35.3%** means each incremental dollar of revenue is now worth ~35x the blended margin. If revenue growth holds low-double-digits, operating income compounds far faster than sales — the 9M-23 +148.6% op-income growth is the template.
3. **FCF inflection is the cleanest, least narrative-dependent datapoint:** TTM FCF **–$26.3B → +$16.9B** in four quarters, and **Q3-23 FCF of $8.7B vs –$5.0B** a year ago. Capex *down* 17% TTM while OCF *up* 81% is the mechanical signature of the 2022-23 "efficiency" era paying off.
4. **Balance sheet is now a tailwind, not a risk:** net cash ex-leases, debt down $3.0B, finance leases down 21%, interest coverage up from 5.7x to 9.6x, net interest expense near zero (a ~$0.7B annualized EPS benefit vs. 2022).
5. **Deferred revenue growth (+8.8% current)** and **$284.4B of contractual obligations** imply forward demand visibility (AWS commitments + Prime subscriptions) is intact.

### Bearish / risk evidence
1. **The Q4-2023 print is the binary event, and it is not in this data.** Holiday-quarter revenue mix plus **re-accelerating capex** (AI/GenAI infrastructure) is the key risk to the FCF story. Watch whether capex guidance steps back above ~$55-60B annualized — that would compress the very FCF the market is paying for.
2. **Capex is a coiled spring.** The FCF improvement is *partly* a capex holiday. D&A is already growing **+19.2%** against a *declining* capex base; when the AI buildout resumes, D&A plus capex will both rise and the margin expansion rate mathematically decelerates.
3. **Earnings quality caveat:** **+$1,196M of equity FV gains in Q3-23** and +$1,000M in 9M-23 (Rivian-type marks) sit in non-operating income. Strip them and Q3 EPS is roughly **$0.85–0.86**, not $0.94. The easy YoY non-operating comparison is now fully anniversaried — **2024 non-operating income will not repeat the 2022→2023 swing**, so headline net income growth will decelerate to the operating growth rate.
4. **Working capital is a persistent drag, not a source.** AP –$7.6B and accrued –$3.8B YTD is good for quality but means OCF has no "float release" cushion left to draw on; if revenue growth stalls, OCF growth decelerates immediately.
5. **Current ratio 0.985x, quick ratio 0.74x, $103.4B undiscounted lease commitments, $284.4B total contractual obligations.** This is a business that needs uninterrupted access to capital markets and uninterrupted cash generation. Rate/credit stress hits it asymmetrically.
6. **SBC of $17.7B (4.4% of revenue, +26% YoY) with $23.3B unrecognized** — GAAP profitability overstates distributable economics by ~$23B/yr annualized. For FCF-purist valuation, use FCF-after-SBC (TTM ≈ $16.9B – $23.6B ≈ **negative**).
7. **Cash tax rate (29% of pre-tax) running nearly double the 17% book ETR** — expect FCF growth to lag net-income growth as deferred benefits normalize.

### Concrete monitorables for the next two prints
| Watch item | Threshold that confirms bull | Threshold that breaks the thesis |
|---|---|---|
| Gross margin (quarterly) | ≥47% sustained | <45% (mix shift or price investment) |
| Operating margin | ≥7% in a non-holiday quarter | <5% |
| Capex (TTM) | ≤$55B | >$65B without matching revenue acceleration |
| TTM FCF | ≥$20B | back below $5B |
| Net interest | stays near neutral | swings >$500M expense/quarter |
| Shares outstanding | ≤+1.2%/yr | >+2%/yr (SBC creep) |
| Current ratio | >1.0x | <0.9x |

---

## 7. Summary Table — Key Fundamental Points

| Category | Metric | Latest (9/30/2023) | Prior Comparative | Direction / Interpretation | Signal |
|---|---|---|---|---|---|
| **Scale** | Revenue, 9M-23 (derived) | $404,824M | $364,779M (9M-22) | +11.0% growth | Neutral-positive |
| **Growth** | Revenue, Q3-23 (derived) | $143,083M | $127,101M | +12.6% YoY — re-accelerating | Positive |
| **Profitability** | Gross margin, 9M-23 | 47.6% | 44.3% | **+328 bp** — the core thesis | **Strong positive** |
| **Profitability** | Operating income, 9M-23 | $23,643M | $9,511M | **+148.6%** | **Strong positive** |
| **Profitability** | Operating margin, 9M-23 | 5.84% | 2.61% | +323 bp; Q3 alone 7.82% | **Strong positive** |
| **Leverage test** | Incremental operating margin | 35.3% | n/a | Blended margin understates economics | **Strong positive** |
| **EPS** | Diluted EPS, 9M-23 | $1.89 | $(0.29) | +$2.18 swing | Positive |
| **EPS quality** | Equity FV gains in 9M-23 / Q3-23 | +$1,000M / +$1,196M | –$11,300M (9M-22) | Marks flatter EPS; not repeatable | Caution |
| **Cost discipline** | G&A growth, 9M | +2.9% | vs revenue +11.0% | 2.18% of revenue (from 2.35%) | Positive |
| **Cost discipline** | Marketing growth, 9M | +7.0% | vs revenue +11.0% | 7.77% of revenue (from 8.07%) | Positive |
| **Cost headwind** | D&A growth, 9M | +19.2% ($34,843M) | $29,236M | Outgrowing revenue — capex catch-up | Caution |
| **Compensation** | SBC, 9M-23 | $17,704M (4.37% of rev) | $14,015M (3.84%) | +26.3%; $23.3B unrecognized | Caution |
| **Cash generation** | OCF, TTM to 9/30/23 | **$71,654M** | $39,665M | **+80.6%** | **Strong positive** |
| **Cash generation** | Capex, TTM | **$54,733M** | $65,988M | **–17.1%** | **Strong positive** |
| **FCF** | FCF (OCF–capex), TTM | **+$16,921M** | –$26,323M | **+$43.2B swing** | **Strong positive** |
| **FCF** | FCF after finance-lease principal, TTM | +$11,676M | –$34,884M | Still positive | Positive |
| **FCF** | Q3-23 standalone FCF | +$8,738M | –$4,974M | Third straight positive quarter implied | Positive |
| **Cash quality** | OCF / net income, 9M | 2.15x | n/m (net loss) | High conversion; D&A + SBC heavy | Positive |
| **Cash quality** | Cash taxes paid vs book tax, 9M | $6,982M vs $4,058M | $4,340M | Cash tax = 29% of pre-tax vs 17% ETR | Caution |
| **Working capital** | Accounts payable | $72,004M | $79,600M (12/31/22) | **–9.5%** — no payable stretching | Positive (quality) |
| **Working capital** | Accrued liabilities | $58,812M | $62,566M | –6.0%; –$9,022M CF drag in 9M | Neutral |
| **Liquidity** | Cash + marketable securities | ~$99,476M | ~$110,000M | Ample absolute liquidity | Positive |
| **Liquidity** | Current ratio | 0.985x | 0.945x | Improving but **<1.0x** | Caution |
| **Liquidity** | Quick ratio | 0.74x | — | Thin | Caution |
| **Leverage** | Total long-term debt | ~$67,093M | ~$70,149M | –4.4%; **no LT debt issued in 2023** | Positive |
| **Leverage** | Finance lease liabilities | $12,466M | $15,783M | **–21.0%** | Positive |
| **Leverage** | Operating lease liabilities | $73,902M | $69,040M | +7.0% — real fixed cost | Caution |
| **Leverage** | Net debt ex-leases | **≈ –$19,900M (net cash)** | — | Balance sheet is a tailwind | **Strong positive** |
| **Coverage** | EBIT / interest, 9M | 9.6x | 5.7x | Interest burden halved | Positive |
| **Coverage** | Net interest, 9M / Q3 | –$421M / –$30M | –$1,129M | Effectively neutral | Positive |
| **Returns** | ROE (annualized 9M on ~$183B equity) | ~16% | ~n/m | Recovering sharply | Positive |
| **Returns** | ROA (TTM NI / avg assets) | ~4.2% | — | Low — asset-heavy model | Neutral |
| **Commitments** | Total contractual obligations | $284,407M | — | Largely purchase obligations + leases | Caution |
| **Capital return** | Buybacks, 9M-23 | **$0** | $6,000M (9M-22) | Fully suspended | Neutral-negative |
| **Dilution** | Shares outstanding | 10,330M | 10,242M | +0.9% YTD | Minor caution |
| **Insider activity** | Transactions | — | — | **DATA UNAVAILABLE — no inference made** | Unknown |
| **Event risk** | Q4/FY2023 results | Not yet reported | — | Holiday quarter + capex guide = binary | Key catalyst |

---

**Bottom line for AMZN:** the point-in-time filings show an unambiguous **fundamental inflection** — gross margin +328 bp, operating income +149%, and a **$43B TTM FCF swing from –$26.3B to +$16.9B**, all achieved *despite* a $7.6B reduction in payables (i.e., cash quality is genuine). The balance sheet has flipped to net cash ex-leases with 9.6x interest coverage and zero buybacks. The offsetting realities are: (a) the FCF step-up leans on a **capex holiday** that AI infrastructure spending will likely end, (b) ~$1.2B/quarter of non-operating equity marks flatter EPS and have now anniversaried, (c) SBC of ~$23B/yr means GAAP FCF is not shareholder FCF, and (d) the liquidity profile (current ratio 0.985x, $284B contractual obligations, $103B lease commitments) leaves no room for a demand shock. **The next Q4 print — specifically capex guidance versus gross-margin durability — is the deciding variable, and insider data must be sourced independently before acting.**