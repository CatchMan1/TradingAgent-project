# AAPL — Fundamental Deep Dive
**As of 2026-08-06 | Primary source: Q3 FY2026 Form 10-Q, filed 2026-07-31 (accession 0000320193-26-000020); prior 10-Q filed 2026-05-01; FY2025 10-K filed 2025-10-31**

---

## 0. Data provenance & what I could NOT verify

Before the analysis, so you know exactly how much weight to put on each section:

| Item | Status |
|---|---|
| Income statement, balance sheet, cash flow (Q3 FY26 + 9M FY26 + comparatives) | ✅ Full detail, point-in-time, filed 6 days ago |
| Prior-year comparatives (Q3 FY25, 9M FY25), Q1/Q2 FY26 partial lines | ✅ Available |
| FY23–FY25 annual cash flow (CFO, CFI, CFF) | ✅ Available |
| FY2025 annual income statement & balance sheet (full-year) | ❌ Not in retrieved slice |
| Segment/product-level revenue (iPhone, Services, etc.) | ❌ Not returned by tool |
| Company profile / business description | ❌ Not returned — profile below is general background, **not** tool-sourced |
| Share price, market cap, valuation multiples | ❌ Not returned — I triangulate an *implied* range below, clearly flagged |
| Insider transactions | ❌ **`DATA_UNAVAILABLE`** — no authorized archive. I make **no** inference about insider activity. |

All figures USD millions unless noted.

---

## 1. Executive summary — the one-paragraph version

AAPL just delivered a **genuinely strong operating-leverage quarter** (Q3 FY26, ended 2026-06-27, reported 2026-07-31): revenue **+16.4% YoY**, gross margin **50.06% (+357bp)**, operating income **+26.6%**, diluted EPS **+28.7%**. Nine-month FY26 revenue is **+16.2%** with EPS **+22.4%** — a dramatic acceleration versus Apple's recent mid-single-digit history, and it is arriving *with* margin expansion, not because of it. Cash generation is exceptional: **9M CFO $117.0B (+43% YoY)**, **FCF $110.2B**, FCF margin **30.2%**, CFO/NI conversion **115%**. The balance sheet is the strongest in years — **net cash ~$62.2B**, up ~$28.5B in nine months, with long-term debt down $8.4B and zero new long-term issuance. Two items demand scrutiny rather than celebration: **inventory +94% (raw materials +260%)** and a **~$13.3B jump in net intangibles**, alongside a **~$23B one-quarter equity increase** in Q2 FY26 that net income and buybacks cannot explain — most consistent with meaningful M&A. Gross margin at 50% is a record-area number that is the single biggest mean-reversion risk in the thesis.

---

## 2. Company profile
*(General background — the fundamental tool returned no profile document; treat as context, not evidence.)*

Apple Inc. designs, manufactures and sells smartphones (iPhone), personal computers (Mac), tablets (iPad) and wearables (Watch, AirPods, Vision), and monetizes an installed base of ~2.3B active devices through Services (App Store, iCloud, Music/TV+, advertising, Apple Pay, licensing). The model is vertically integrated hardware with an increasingly Services-weighted, high-margin recurring layer, distributed through retail, carrier and online channels globally. Structural characteristics relevant to the numbers below: extreme supplier-financed negative working capital, a very low capex-intensity model (Apple has historically outsourced manufacturing), and the largest buyback program in corporate history.

---

## 3. The latest quarter — Q3 FY2026 (ended 2026-06-27)

| Line item | Q3 FY26 | Q3 FY25 | YoY |
|---|---:|---:|---:|
| Revenue | **109,417** | 94,036 | **+16.4%** |
| Cost of sales | 54,647 | 50,318 | +8.6% |
| **Gross profit** | **54,770** | 43,718 | **+25.3%** |
| **Gross margin %** | **50.06%** | 46.49% | **+357 bp** |
| R&D | 11,729 | 8,866 | **+32.3%** |
| SG&A (S&M 5,034 / G&A 2,312) | 7,346 | 6,650 | +10.5% |
| Total opex | 19,075 | 15,516 | +22.9% |
| **Operating income** | **35,695** | 28,202 | **+26.6%** |
| **Operating margin %** | **32.62%** | 29.99% | **+263 bp** |
| Non-operating income/(expense) | +572 | (171) | +743 |
| Pre-tax income | 36,267 | 28,031 | +29.4% |
| Tax | 6,478 | 4,597 | — |
| **Effective tax rate** | **17.86%** | 16.40% | **+146 bp** |
| **Net income** | **29,789** | 23,434 | **+27.1%** |
| **Diluted EPS** | **$2.02** | $1.57 | **+28.7%** |
| Diluted shares (implied) | ~14,748M | ~14,926M | (1.2%) |

**Key read-throughs:**
- **Cost of sales grew +8.6% against revenue +16.4%.** That spread is the entire margin story — it implies mix shift toward higher-margin revenue (Services / higher ASPs / favorable component costs), not price-led volume.
- **R&D +32.3% YoY is the single largest opex delta** and consistent with a heavy AI/silicon investment cycle. Crucially, revenue is outgrowing it, so it is not yet margin-dilutive.
- **Non-operating swung from −$171M to +$572M**, adding ~$743M of pre-tax tailwind — a real but non-core contributor (~1.3% of pre-tax). Do not capitalize this in a forward earnings model.
- **The tax rate rose 146bp YoY**, a headwind. EPS growth of +28.7% was achieved *despite* it.
- Sequentially vs. H1 FY26 averages, opex intensity jumped (17.4% of revenue in Q3 vs 14.6% in H1) — but this is **seasonal** (Q3 FY25 was 16.5%), so do not extrapolate Q3's opex ratio into Q4.

---

## 4. Year-to-date FY2026 (9 months) and H1 split

| Line item | 9M FY26 | 9M FY25 | YoY |
|---|---:|---:|---:|
| Revenue | **364,357** | 313,695 | **+16.2%** |
| Gross profit | 178,782 | 146,860 | +21.7% |
| Gross margin % | **49.07%** | 46.82% | +225 bp |
| R&D | 34,035 | 25,684 | **+32.5%** |
| SG&A | 22,315 | 20,553 | +8.6% |
| Opex | 56,350 | 46,237 | +21.9% |
| Operating income | 122,432 | 100,623 | +21.7% |
| Operating margin % | **33.60%** | 32.08% | +152 bp |
| Non-operating | +670 | (698) | +1,368 |
| Pre-tax income | 123,102 | 99,925 | +23.2% |
| Tax / rate | 21,638 / **17.58%** | 15,381 / 15.39% | +219 bp |
| **Net income** | **101,464** | 84,544 | **+20.0%** |
| Net margin % | 27.85% | 26.95% | +90 bp |
| **Diluted EPS** | **$6.88** | $5.62 | **+22.4%** |
| D&A | 9,973 | 8,571 | +16.4% |
| SBC | 10,523 | 9,680 | +8.7% |
| SBC % of revenue | 2.89% | 3.09% | −20 bp ✅ |

**Derived H1 (6M) FY26, from 9M minus Q3** (the tool did not split Q1/Q2 revenue, so I aggregate rather than fabricate a quarterly split):

| Line item | H1 FY26 | H1 FY25 | YoY |
|---|---:|---:|---:|
| Revenue | 255,940 | 219,659 | +16.5% |
| Gross profit | 124,012 | 103,142 | +20.2% |
| Gross margin % | **48.45%** | 46.96% | +149 bp |
| Operating income | 86,737 | 72,421 | +19.8% |
| Operating margin % | 33.89% | 32.97% | +92 bp |
| Pre-tax income | 86,835 | 71,894 | +20.8% |
| Diluted EPS | $4.85 | $4.05 | +19.8% |

**Margin trajectory — the most useful signal in this dataset:** H1 FY26 gross margin **48.45%** → Q3 FY26 **50.07%**. A ~160bp sequential step-up in gross margin within the same fiscal year is a material inflection. If it holds into the October print, the FY26 exit run-rate margin is ~50%+, which would force consensus estimate revisions upward. If Q3's 50% proves to be a mix/timing peak, the stock's multiple is the vulnerable variable.

---

## 5. Cash flow — this is the strongest part of the story

| Line item | 9M FY26 | 9M FY25 | YoY |
|---|---:|---:|---:|
| **Operating cash flow** | **116,996** | 81,754 | **+43.1%** |
| Capex (PP&E) | 6,799 | 9,473 | −28.2% |
| **Free cash flow** | **110,197** | 72,281 | **+52.5%** |
| FCF margin | **30.2%** | 23.0% | +720 bp |
| Investing cash flow | (18,811) | +17,782 | — |
| Financing cash flow | (94,575) | (93,210) | — |
| Net change in cash | +3,610 | +6,326 | — |
| Buybacks | 62,094 | 70,579 | −12.0% |
| Dividends paid | 11,778 | 11,559 | +1.9% |
| SBC tax withholding | 6,462 | 5,719 | +13.0% |
| LT debt repaid | 8,146 | 9,682 | — |
| LT debt issued | **0** | 4,481 | — |
| Commercial paper change | (5,911) | (65) | — |

**Quarterly CFO decomposition (derived):**

| Quarter | FY26 CFO | FY25 CFO | YoY |
|---|---:|---:|---:|
| Q1 (Dec) | 53,925 | 29,935 | **+80.2%** |
| Q2 (Mar) | 28,702 | 23,952 | +19.8% |
| Q3 (Jun) | 34,369 | 27,867 | +23.3% |
| **9M total** | **116,996** | **81,754** | +43.1% |

**Insight traders should not miss:** the +43% CFO growth was **front-loaded into Q1 FY26 (+80% YoY)**. Q1 is Apple's seasonal working-capital release quarter, so a chunk of that is timing. Q2 and Q3 reverted to a still-excellent but far more normal +20–23%. **Model FY26 full-year CFO off the Q2/Q3 run-rate, not off the 9M total.**

Free cash flow quarterly (derived): Q3 FY26 CFO 34,369 − capex 2,455 = **$31.9B (29.2% FCF margin, +30.8% YoY)**. Q3 capex of $2.46B is only **2.2% of revenue** — Apple is simply not a capex-AI story. That matters: if the market is paying for an AI narrative, it is being delivered through **R&D and acquired intangibles**, not through data-center capex.

**Working capital caveat (important):** The working-capital lines in the retrieved cash-flow data carry signs that contradict the balance-sheet deltas — e.g., accounts receivable *fell* $8.4B on the balance sheet ($39.8B → $31.4B) while the cash-flow line is shown as −$8,316M. I therefore read these **directionally, not as reported**: AR was roughly a **$8.4B source of cash** and inventory a **~$5.4B use of cash** during 9M FY26. Net-net, working capital was a modest tailwind, which means **the underlying CFO quality is genuinely high — it is not a pure working-capital illusion.**

---

## 6. Balance sheet — de-risking, plus two anomalies

| Item | 2026-06-27 | 2025-09-27 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 39,544 | 35,934 | +3,610 |
| Marketable securities — current | 22,855 | 18,763 | +4,092 |
| Marketable securities — noncurrent | 84,118 | 77,723 | +6,395 |
| **Total cash & investments** | **146,517** | **132,420** | **+14,097** |
| Accounts receivable | 31,398 | 39,777 | **−21.1%** |
| Nontrade receivables | 27,509 | 33,180 | −17.1% |
| **Inventory** | **11,092** | **5,718** | **+94.0%** ⚠️ |
| — Raw materials & purchased parts | 7,645 | 2,124 | **+260%** ⚠️ |
| — Finished goods | 3,447 | 3,594 | −4.1% |
| Other current assets | 17,420 | 14,585 | +19.4% |
| Current assets | 149,818 | 147,957 | +1.3% |
| **Intangibles, gross** | **38,220** | **24,950** | **+53.2%** ⚠️ |
| **Intangibles, net** | **25,417** | **13,301** | **+91.1%** ⚠️ |
| Other noncurrent assets | 77,557 | 72,634 | +6.8% |
| **Total assets** | **383,266** | **359,241** | +6.7% |
| Accounts payable | 64,525 | 69,860 | −7.6% |
| Other current liabilities | 62,259 | 66,387 | −6.2% |
| Current liabilities | 149,326 | 165,631 | −9.8% |
| LT debt incl. current | 82,300 | 90,700 | −9.3% |
| — of which current | 11,007 | 12,350 | — |
| — of which noncurrent | 71,340 | 78,328 | — |
| Commercial paper | 1,997 | 7,979 | **−75.0%** |
| Other noncurrent liabilities | **55,080** | **41,549** | **+32.6%** ⚠️ |
| Total liabilities | 275,746 | 285,508 | −3.4% |
| **Stockholders' equity** | **107,520** | **73,733** | **+45.8%** ⚠️ |
| Shares outstanding (M) | 14,608.96 | 14,773.26 | −1.1% |

### 6a. The good
- **Net cash position ≈ $62.2B** (146,517 cash+investments − 84,297 total debt incl. CP), up from ~$33.7B nine months ago. That is a **~$28.5B net-cash build in three quarters** on top of ~$74B returned to shareholders. Rare combination.
- **Deleveraging is active and deliberate:** LT debt −$8.4B, **zero new long-term debt issued** (vs $4.5B in the prior-year period), commercial paper cut 75%. Management is choosing balance-sheet strength over incremental leverage.
- **Collections are excellent:** AR −21% while revenue grew +16% → DSO of **~26 days**.
- **Current ratio improved to 1.003** from 0.893. Still tight (structurally so), but no longer <1.
- **Debt/equity 0.78x** vs 1.34x at FY25 year-end.
- **Cash conversion cycle ≈ −63 days** (inventory 18.5 days + AR 26.1 days − AP 107.5 days). The business is still funded by its supply chain.

### 6b. The three yellow flags

**(1) Inventory +94%, raw materials +260%.** Raw materials of $7.6B versus $2.1B nine months ago is not a normal seasonal move, and finished goods are actually *flat* ($3.45B vs $3.59B). That combination — raw-up, finished-flat — points to a **deliberate component/parts stockpile ahead of a product ramp, or a tariff/geopolitical supply hedge.** Bull case: pre-build for a significant launch, implying confidence in forward demand. Bear case: if demand disappoints, this becomes a write-down that lands directly in the 50% gross margin. **In my view this is the highest-information item in the entire filing.** Watch inventory in the FY26 10-K (late October) more closely than any other line.

**(2) Intangibles +$13.3B net / +$13.2B gross, and other noncurrent liabilities +$13.5B.** Net intangibles more than doubled to $25.4B while capex *fell* 28%. Apple does not accumulate $13B of intangibles organically — this is the signature of **acquisitions or asset purchases** in FY26. The matching $13.5B rise in noncurrent other liabilities hints at earnouts, deferred consideration, or tax positions. This is invisible in the cash-flow statement (no large "acquisitions, net of cash acquired" line surfaced in the retrieved tags), which is itself worth verifying.

**(3) The $23B equity anomaly.** Stockholders' equity jumped from $73,733M to $106,491M between 2025-09-27 and 2026-03-28 — **+$32.8B in one quarter** — while Q2 FY26 net income was only ~$29.6B (derived) against roughly $20B of buybacks + dividends + SBC withholding. Common stock & APIC rose only $7.1B over nine months, and AOCI barely moved (−$5.57B → −$5.38B). **Roughly $15–23B of the equity increase is not explained** by earnings, buybacks, or OCI.

> **Synthesis of (2) and (3):** the most internally consistent explanation is **material inorganic activity in FY26, at least partly stock-funded**, which would raise equity, raise intangibles, raise noncurrent liabilities, and explain the APIC increase — all four of which are observed. I am flagging this as a **probable but unconfirmed ~$13–20B M&A event**. It is neither in the income statement nor obviously in the cash-flow financing lines, so it is being largely ignored by a headline-reading market. **Do not model it as recurring EPS.** If an acquisition of that size occurred, amortization of the acquired intangibles (accumulated amortization rose $11.65B → $12.80B, i.e., +$1.15B in nine months ≈ $150M/quarter and rising) becomes a slow, creeping EPS headwind.

### 6c. Other balance-sheet observations
- **Deferred revenue (total contract liability) $14.90B, +8.8%** over nine months vs revenue +16.2%. The forward-looking subscription backlog is growing **more slowly than total revenue** — a mild caution on the Services growth rate, or simply a function of Services being billed in arrears. It is the one KPI here that is not confirming the acceleration story.
- **Accumulated depreciation $76.7B vs $76.0B** — essentially flat against a rising asset base. The installed asset base is largely depreciated, which flatters future margins as capex stays low.
- **Dividends per share declared: $0.79 for 9M FY26 vs $0.76 (+3.9%)**, with Q3 at $0.27 vs $0.26. Annualized ≈ **$1.05–1.06/share**. Payout ratio is only **11.6% of net income** — enormous room to raise, and a plausible modest catalyst at the next declaration.

---

## 7. Capital returns — disciplined, but decelerating

| 9M FY26 | Amount | vs 9M FY25 |
|---|---:|---:|
| Buybacks | $62,094M | −12.0% |
| Dividends | $11,778M | +1.9% |
| SBC tax withholding | $6,462M | +13.0% |
| **Total cash returned** | **$73,872M** | −10.1% |
| **As % of FCF ($110,197M)** | **67.0%** | vs 114% last year |

This is a real behavioral shift: in 9M FY25 Apple returned **114% of FCF** (i.e., outspending cash generation, funded by the balance sheet). In 9M FY26 it returned **67%**, while simultaneously cutting debt and building net cash by $28.5B. Management has pivoted from maximizing per-share accretion to **fortifying the balance sheet** — plausibly to fund the inorganic activity visible in intangibles. 

**Share count math:** net shares retired 164.3M (−1.1%) for $62.1B. Because SBC issuance partly offsets repurchases, actual shares bought exceeded 164.3M, so the **implied average repurchase price is at or below ~$378/share.**

**Long-term financing trend (from 10-K):** net cash used in financing was **−$108.5B (FY23), −$122.0B (FY24), −$120.7B (FY25)**, and **−$94.6B in just 9M FY26**. The pace of gross capital return is roughly flat-to-up, but the *net* figure is now smaller because debt is being repaid rather than issued.

---

## 8. Derived valuation triangulation *(flagged — no price feed available)*

The tools returned no share price. Two independent anchors from the filing:

1. Implied average buyback price **≤ ~$378** (from $62,094M / 164.3M net shares retired; lower if SBC issuance was material).
2. Share count 14,595M (10-Q cover date 2026-07-17).

**Forward EPS build (estimate, not tool output):** 9M diluted EPS is **$6.88**. Q4 is seasonally Apple's largest quarter. Carrying forward Q4 FY25's implied ~$1.8–1.9 with 20–25% growth implies **FY26 diluted EPS ≈ $9.0–9.5**, i.e. **+20–25% YoY**.

**Implied multiple:**

| Assumed price | Market cap | P/E on FY26E EPS ~$9.2 |
|---|---:|---:|
| $300 | ~$4.38T | ~33x |
| $340 | ~$4.96T | ~37x |
| $378 | ~$5.52T | ~41x |

**Takeaway:** at any point in that range, AAPL trades at a **premium multiple that requires the current ~20%+ EPS growth to persist.** Fundamentals support the growth (16% revenue, 50% GM, 22% EPS). The risk is not the P&L — it is that a 33–41x multiple on a hardware-anchored franchise has essentially no cushion if gross margin reverts toward 47%.

---

## 9. Insider activity

**Not available.** The tool returned `DATA_UNAVAILABLE`, explicitly stating there is no authorized point-in-time insider-transactions archive for AAPL by 2026-08-06. I will not infer, estimate, or characterize insider behavior. **Treat this dimension as a genuine information gap and do not let any secondary source fill it for you on this date.**

---

## 10. Actionable conclusions for a trader

**The bull case, stated with evidence:**
1. **Growth re-rating is real and accelerating.** 9M revenue +16.2%, Q3 +16.4% — versus Apple's historical mid-single digits. This is a new regime, not noise, because it is confirmed across revenue, gross profit, operating income and EPS simultaneously.
2. **Operating leverage is working.** Q3 gross margin 50.06% (+357bp) with COGS growing half as fast as revenue. Margin expansion is coming from mix/cost, and R&D (+32%) is being absorbed without margin damage.
3. **Cash generation is elite and clean.** $110.2B FCF in nine months, 115% CFO/NI conversion, working capital roughly neutral. Q3 FCF margin 29.2% and rising.
4. **Balance sheet is a fortress.** $62.2B net cash, +$28.5B in nine months, debt actively reduced. This is downside protection the market is not paying attention to.
5. **Low capital intensity = high cash conversion durability.** Capex at 1.9% of revenue.

**The bear case / where I would push back:**
1. **A 50% gross margin is the peak-margin risk.** Reverting even to 48% would cut ~$2.2B of annualized gross profit (~3% of pre-tax income) and, more importantly, break the margin-expansion narrative that the multiple is built on.
2. **Inventory +94% / raw materials +260% is an unhedged bet.** If that pre-build precedes a demand disappointment, the write-down lands in the exact line item driving the story.
3. **Tax rate +219bp YoY** (15.39% → 17.58%). If this is structural rather than timing, it is a persistent ~2% EPS headwind.
4. **Non-operating income swung +$1.37B** YoY — if rates fall, that tailwind reverses.
5. **CFO growth is front-loaded** in Q1 (+80%). The +43% headline flatters the run-rate; Q2/Q3 were +20–23%.
6. **Buyback pace slowed 12%** and total capital return fell to 67% of FCF. Less per-share support than the market is used to.
7. **Deferred revenue growth (+8.8%) lags revenue growth (+16.2%)** — the only KPI that fails to confirm the acceleration.

**Specific, testable actions:**

| # | Action | Trigger / evidence to check |
|---|---|---|
| 1 | **Own the margin-expansion trade into the Q4 FY26 print (late Oct 2026), sized for event risk** | H1 GM 48.45% → Q3 50.07% is a within-year inflection. Confirm continuity quarterly. |
| 2 | **Set the invalidation at gross margin < 48%** in Q4 FY26 | That would unwind the +357bp story and, at 33–41x, compress the multiple fast. |
| 3 | **Read inventory before you read EPS in the FY26 10-K** | Inventory $5.7B→$11.1B and raw materials $2.1B→$7.6B. A further build = ramp confidence; a write-down = margin risk. |
| 4 | **Demand the 10-K explain the ~$13.3B intangible increase and ~$23B Q2 equity jump** | If it is a ~$13–20B acquisition, model incremental amortization (~$150M/qtr and rising, accumulated amortization already +$1.15B in 9M) and do **not** extrapolate acquired growth as organic. |
| 5 | **Screen for a dividend increase at the next declaration** | 9M DPS $0.79 (+3.9%), payout only 11.6% of net income, $62B net cash. Very high probability, low-risk catalyst. |
| 6 | **Model FY26 CFO off Q2/Q3's ~$29–34B/quarter, not the 9M total** | Q1's +80% YoY is seasonally inflated. FY26 CFO ≈ $145–150B is the defensible figure, not a naive 4/3 × 116,996 = $156B. |
| 7 | **Treat the valuation, not the fundamentals, as the binding constraint** | Fundamentals are clean; a 33–41x implied multiple leaves no room for a margin reset. Position sizing should reflect that asymmetry. |
| 8 | **Do not act on insider data** | Archive unavailable as of 2026-08-06. No inference permitted. |

**Net stance: fundamentally bullish, valuation-conditional.** The Q3 FY26 filing is the best operating data AAPL has produced in years on growth *and* margin *and* cash flow simultaneously, funded from a fortress balance sheet. But it arrives at a premium multiple, with peak gross margin and an unexplained ~$13–20B of inorganic activity sitting in the balance sheet. The trade is to be long the margin story with a hard stop at gross margin <48%, and to read the FY26 10-K's inventory and intangibles notes before adding size.

---

## 11. Key points summary

| Category | Metric | Latest (Q3 FY26 / 9M FY26) | Prior comparative | Signal |
|---|---|---|---:|
| **Growth** | Revenue YoY | 109,417 / **+16.4%** | 94,036 | 🟢 Accelerating strongly |
| **Growth** | 9M revenue YoY | 364,357 / **+16.2%** | 313,695 | 🟢 New regime vs historical MSD |
| **Profitability** | Q3 gross margin | **50.06%** | 46.49% | 🟢 +357bp; peak-margin risk |
| **Profitability** | 9M gross margin | 49.07% | 46.82% | 🟢 +225bp |
| **Profitability** | Q3 operating margin | **32.62%** | 29.99% | 🟢 +263bp operating leverage |
| **Profitability** | 9M net margin | 27.85% | 26.95% | 🟢 |
| **Earnings** | Q3 diluted EPS | **$2.02** | $1.57 (+28.7%) | 🟢 Fastest growth in the stack |
| **Earnings** | 9M diluted EPS | **$6.88** | $5.62 (+22.4%) | 🟢 ~2% buyback tailwind |
| **Earnings** | Effective tax rate | 17.58% (9M) | 15.39% | 🔴 ~219bp headwind |
| **Investment** | R&D YoY | 34,035 / **+32.5%** | 25,684 | 🟡 AI cycle; revenue is outgrowing it |
| **Investment** | Capex / revenue | 1.87% | 3.02% | 🟢 Asset-light; not an AI-capex story |
| **Cash flow** | 9M CFO | **116,996 (+43.1%)** | 81,754 | 🟢 But front-loaded in Q1 (+80%) |
| **Cash flow** | 9M FCF | **110,197 (+52.5%)** | 72,281 | 🟢 30.2% FCF margin |
| **Cash flow** | CFO / Net income | **115%** | 97% | 🟢 High earnings quality |
| **Balance sheet** | Total cash & investments | **146,517** | 132,420 | 🟢 +$14.1B |
| **Balance sheet** | Net cash | **~62,220** | ~33,741 | 🟢 +$28.5B in 9 months |
| **Balance sheet** | LT debt incl. current | 82,300 | 90,700 | 🟢 Actively deleveraging |
| **Balance sheet** | Commercial paper | 1,997 | 7,979 | 🟢 −75% |
| **Balance sheet** | Debt / equity | 0.78x | 1.34x | 🟢 |
| **Balance sheet** | Current ratio | 1.003 | 0.893 | 🟡 Improved but structurally tight |
| **Working capital** | Inventory | **11,092 (+94%)** | 5,718 | 🔴 **Top risk — raw materials +260%** |
| **Working capital** | DSO (derived) | ~26 days | — | 🟢 AR −21% on +16% revenue |
| **Working capital** | Cash conversion cycle | ~−63 days | — | 🟢 Supplier-funded |
| **Forward demand** | Deferred revenue | 14,900 (+8.8%) | 13,700 | 🟡 Lags revenue growth |
| **Inorganic** | Intangibles, net | **25,417 (+91%)** | 13,301 | 🟡 Probable ~$13B+ M&A |
| **Inorganic** | Other noncurrent liabilities | 55,080 (+32.6%) | 41,549 | 🟡 Consistent with deal consideration |
| **Data flag** | Stockholders' equity | 107,520 (+45.8%) | 73,733 | 🟡 ~$15–23B unexplained in Q2; verify |
| **Capital return** | 9M buybacks | 62,094 (−12.0%) | 70,579 | 🟡 Decelerating |
| **Capital return** | 9M dividends | 11,778 (+1.9%); DPS $0.79 | $0.76 | 🟢 11.6% payout → raise likely |
| **Capital return** | Total return / FCF | 67% | 114% | 🟡 Pivot to balance sheet |
| **Shares** | Diluted shares | ~14,748M | ~14,926M (−1.2%) | 🟢 |
| **Valuation** | Implied avg buyback price | ≤ ~$378 | — | 🟡 Implies ~33–41x FY26E |
| **Insider** | Transactions | **DATA_UNAVAILABLE** | — | ⚪ No inference made |
| **Catalyst** | Next report | Q4 + FY26 10-K, ~late Oct 2026 | — | Watch GM, inventory, intangibles note |