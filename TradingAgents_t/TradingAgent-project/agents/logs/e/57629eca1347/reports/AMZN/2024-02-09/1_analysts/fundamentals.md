# AMZN — Fundamental Deep Dive (Point-in-Time: 2024-02-09)

**Company:** Amazon.com, Inc. — ticker **AMZN** (US)
**Primary source:** FY2023 Form 10-K, accession `0001018724-24-000008`, filed/accepted **2024-02-02 04:48 UTC** — i.e., the freshest audited disclosure available as of today (7 days old). All figures below are SEC XBRL facts filtered to what was actually public by 2024-02-09, so nothing is look-ahead.

---

## 1. Executive summary — the five things that matter

1. **FY2023 was a genuine inflection year, not just a rebound.** Net sales **$574.8B (+11.8% YoY)**, operating income **$36.85B (6.4% margin, +201% YoY)**, net income **$30.43B** vs **–$2.72B** in FY2022. Diluted EPS **$2.90** vs **–$0.27**.
2. **Free cash flow flipped from deeply negative to strongly positive:** CFO **$84.95B** minus capex **$52.73B** = **FCF ≈ +$32.2B**, versus **–$16.9B** in FY2022 and **–$14.7B** in FY2021 — a **~$49.1B YoY swing**. This is the single biggest fundamental change in the print.
3. **The FCF is Q4-loaded and shows operating, not accounting, leverage.** Derived from cumulative-to-annual deltas: **Q4-23 CFO ≈ $42.5B** (vs $29.2B in Q4-22) and **Q4-23 capex ≈ $14.6B**, implying **Q4-23 FCF ≈ $27.9B** — roughly **87% of the full year's FCF** in one quarter, and more than double Q4-22's ~$12.6B.
4. **Capex intensity is falling while the asset base matures:** capex/sales **9.2%** (FY23) vs **12.4%** (FY22) and **13.0%** (FY21); capex/D&A down to **1.08x** from **1.52x**. Depreciation & amortization rose to **$48.7B**. Mechanically, this is what turns CFO into FCF.
5. **Balance sheet de-risked materially:** cash + marketable securities **≈$144.3B**; long-term debt down to **$58.3B** from **$67.2B**; **zero** new long-term debt issued in 2023; finance leases down to **$12.1B**. Working capital swung from **–$8.6B** (2022) to **+$7.4B** (2023). Buybacks were **$0** in 2023 — an unused capital-return lever.

**Bottom line for traders:** the FY23 10-K supports a *quality-of-earnings upgrade* thesis (margin expansion + FCF inflection + deleveraging), but the stock's valuation already discounts a lot, and the **key swing risk is 2024 capex re-acceleration** (visible early in Q3→Q4-23 capex: $12.5B → $14.6B) plus **$24.0B of stock comp** that is rising faster than revenue.

---

## 2. Company profile and reporting structure

- **Amazon.com, Inc.** operates in **three reportable segments** (`NumberOfOperatingSegments = 3` in the FY23 10-K): **North America**, **International**, and **Amazon Web Services (AWS)**.
- Revenue engines: online stores, third-party seller services (1P/3P marketplace), subscription services (Prime), **advertising**, and AWS cloud (compute, storage, database, AI/ML).
- **Scale markers from the filing:** total assets **$527.9B**; shares outstanding **10,387,381,291** as of **2024-01-24**; public float **$1.184T** as of **2023-06-30**.
- **Note on data granularity:** the tag set returned does **not** contain segment-level revenue or the individual "fulfillment / technology & infrastructure" expense lines. Segment mix conclusions below are limited to what the tags support. Where I derive a figure, it is labeled *(derived)*.

---

## 3. Income statement analysis

**Net sales are not a direct tag in this dataset — they are derived as `CostsAndExpenses + OperatingIncomeLoss`, which reconciles exactly to Amazon's reported net sales** (574,785 / 513,983 / 469,822). Cross-check: FY23 operating margin implied is 6.41%, consistent with the reported ~6.4%.

| $M unless noted | FY2021 | FY2022 | FY2023 | YoY 2023 |
|---|---|---|---|---|
| Net sales *(derived)* | 469,822 | 513,983 | 574,785 | **+11.8%** |
| Cost of goods & services sold | 272,344 | 288,831 | 304,739 | +5.5% |
| Gross profit *(derived)* | 197,478 | 225,152 | 270,046 | +19.9% |
| **Gross margin** | 42.0% | 43.8% | **47.0%** | +320 bp |
| Marketing expense | 32,551 | 42,238 | 44,370 | +5.0% |
| G&A expense | 8,823 | 11,891 | 11,816 | –0.6% |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| **Operating income** | 24,879 | 12,248 | **36,852** | **+201%** |
| **Operating margin** | 5.3% | 2.4% | **6.4%** | +403 bp |
| Interest expense | 1,809 | 2,367 | 3,182 | +34.4% |
| Interest & investment income | 448 | 989 | 2,949 | +198% |
| Nonoperating income/(expense) | 13,272 | (18,184) | 705 | n.m. |
| Pre-tax income | 38,151 | (5,936) | 37,557 | n.m. |
| Income tax expense/(benefit) | 4,791 | (3,217) | 7,120 | n.m. |
| **Net income** | 33,364 | (2,722) | **30,425** | n.m. |
| Diluted EPS | $3.24 | ($0.27) | **$2.90** | n.m. |
| Diluted shares *(derived)* | ~10,298M | ~10,082M | ~10,491M | +4.1% |

**What the numbers actually say**

- **Gross margin +500 bp over two years (42.0% → 47.0%)** is the core story: mix shift toward AWS/advertising/3P services, plus fulfillment-regionalization and cost discipline. Cost of sales grew only **+5.5%** against **+11.8%** revenue — that gap *is* the operating leverage.
- **Operating margin of 6.4%** is the highest of the three years shown and was achieved *despite* marketing (+5%) and D&A (+16%) growth.
- **Cost discipline is visible:** G&A was flat-to-down **year over year** ($11,816M vs $11,891M) on 11.8% revenue growth.
- **Quality-of-earnings caveat:** FY2023 pre-tax income of $37.56B includes **~$2.95B of interest income** (a rate-driven, cyclical tailwind) and a **+$1.0B unrealized gain on equity securities** (vs **–$13.6B** in 2022 — the Rivian-type mark). Strip those and "core" pre-tax is closer to **$33.6B**. Likewise FY2021's $33.4B net income was heavily flattered by **+$11.6B** of unrealized equity gains — that year is a poor comparison base.
- **Tax:** provision of $7,120M on $37,557M pre-tax = **~19.0% effective rate**, but **cash taxes paid were $11,179M** and the deferred tax line was a **$5,876M benefit**. Cash tax rate is running above book — a headwind to FCF growth going forward.
- **Stock-based comp is the biggest non-cash friction:** **$24,023M in FY23 (+22.4% YoY)**, up from $19,621M and $12,757M. SBC is now **4.2% of revenue** (vs 3.8% / 2.7%) and equals **~65% of operating income**. **$18.3B of unrecognized SBC** remains to be expensed. Share count rose **+1.3%** (10,898M issued vs 10,757M) — dilution is real but modest relative to peers.

---

## 4. Cash flow and free cash flow — the investment case

| $M | FY2021 | FY2022 | FY2023 | Change |
|---|---|---|---|---|
| Cash from operations | 46,327 | 46,752 | **84,946** | **+81.7%** |
| Purchases of productive assets (capex) | (61,053) | (63,645) | (52,729) | –17.2% |
| **Free cash flow (CFO – capex)** | **(14,726)** | **(16,893)** | **+32,217** | **+49,110** |
| Capex / sales | 13.0% | 12.4% | **9.2%** | –320 bp |
| D&A | 34,433 | 41,921 | 48,663 | +16.1% |
| Capex / D&A | 1.77x | 1.52x | **1.08x** | improving |
| CFO / net income | 1.39x | n.m. | **2.79x** | — |
| Investing cash flow | (58,154) | (37,601) | (49,833) | — |
| Financing cash flow | +6,291 | +9,718 | **(15,879)** | deleveraging |
| Operating lease payments | 6,722 | 8,633 | 10,453 | +21.1% |
| Finance lease principal payments | 11,163 | 7,941 | 4,384 | –44.8% |

**Derived quarterly bridge (from cumulative tags) — the most actionable finding in the dataset:**

| $M | 9M-2022 | 9M-2023 | Q4-2022 *(derived)* | Q4-2023 *(derived)* |
|---|---|---|---|---|
| CFO | 17,579 | 42,481 | 29,173 | **42,465** |
| Capex | 47,053 | 38,141 | 16,592 | 14,588 |
| **FCF** | **(29,474)** | **+4,340** | **+12,581** | **+27,877** |

Interpretation: 9M-23 FCF was only **$4.3B**; **Q4 alone produced ~$27.9B**. That is a **+122% YoY** improvement in the seasonally most important quarter, driven by **both** a $13.3B higher CFO and $2.0B lower capex. It validates that the margin story is translating into cash, not just into the P&L. It also means **the FY23 FCF number is highly concentrated in one quarter** — a Q4 execution miss or a capex step-up would compress the annual figure disproportionately.

**Capex read-through:** Q3-23 capex $12.5B → Q4-23 $14.6B is a sequential **re-acceleration**. Add that FY23 capex was cut while revenue grew 11.8%, and the asset base is now depreciating faster than it is being replaced (capex/D&A 1.08x). **The FY24 debate is whether capex snaps back toward 12%+ of sales** (AI/cloud infrastructure), which would cut FCF materially even with flat margins.

---

## 5. Balance sheet, liquidity and solvency

| $M | 2022-12-31 | 2023-12-31 | Change |
|---|---|---|---|
| Cash & equivalents | 53,888 | **73,387** | +36.2% |
| Marketable securities (AFS fair value) | — | **70,919** | — |
| **Cash + securities** | — | **≈144,306** | — |
| Accounts receivable, net | 42,360 | 52,253 | +23.4% |
| Current assets | 146,791 | 172,351 | +17.4% |
| Accounts payable | 79,600 | 84,981 | +6.7% |
| Accrued expenses & other current liab. | 62,566 | 64,709 | +3.4% |
| Unearned revenue (current) | 13,227 | 15,227 | +15.1% |
| **Total current liabilities** *(derived: AP + accrued + unearned)* | **155,393** | **164,917** | +6.1% |
| **Working capital** *(derived)* | **(8,602)** | **+7,434** | **+16.0B swing** |
| Current ratio *(derived)* | 0.94x | **1.05x** | improving |
| Long-term debt (carrying) | 67,150 | **58,314** | –13.2% |
| Finance lease liabilities | 15,783 | **12,109** | –23.3% |
| Operating lease liabilities | 69,040 | **75,639** | +9.6% |
| Total assets | 462,675 | **527,854** | +14.1% |
| Total stockholders' equity *(10-K reference)* | 146,043 | **201,875** | +38.2% |

**Liquidity/solvency takeaways**

- **Gross cash + securities ≈ $144.3B** against **debt + finance leases ≈ $70.4B** → **net cash ≈ +$74B** (ex-operating leases). Including operating leases ($75.6B), the company is roughly **net-debt-neutral** — a dramatic change from the 2021–22 build-out era.
- **Debt was actively reduced:** no long-term debt issued in 2023 (vs $21.2B in 2022), $3.68B of LT repayments, and **net short-term debt paydown of ~$7.5B** ($18.1B drawn vs $25.7B repaid).
- **Working capital turned positive for the first time in this window** (+$7.4B vs –$8.6B). Note the *composition*: AP grew just **+6.7%** while revenue grew 11.8%, so the old "vendor-financing" cash tailwind is fading — future cash generation leans more on actual profit and less on stretching payables.
- **Interest coverage is comfortable:** EBIT/interest **11.6x**; EBITDA (EBIT + D&A) of **$85.5B** vs interest of $3.2B = **26.9x**.
- **Returns improving:** ROE ≈ **17.5%** on average equity ($30.4B / $174.0B avg) vs a negative 2022 — the balance sheet is now an earnings asset, not a drag.
- **Receivables/watch item:** DSO ≈ **33 days** (up from ~30), allowance for doubtful accounts up to $1.7B, write-offs up to $1.6B — small but drifting in the wrong direction.

---

## 6. Capital allocation and forward commitments

- **Buybacks: $0 in FY2023** (vs $6.0B in FY2022). **Dividends: none.** With net cash of ~$74B and $32B of FCF, capital return remains the single largest *unactivated* catalyst in this dataset.
- **Reinvestment** remains the priority: $52.7B capex, plus finite-lived intangible additions lifting gross intangibles to $10.1B, plus AWS capacity.
- **Contractual obligations total $300.4B**, of which only **$39.3B is due within 12 months**; **$157.8B falls due after year five** — long-duration commitments consistent with multi-year AWS/cloud contracts and content licenses. This is a *demand signal* as much as an obligation.
- **Deferred revenue (contract liabilities) grew to $20.6B from $16.1B (+28%)**, and **$12.4B of FY23 revenue came from amounts already in deferred revenue** at the start of the year — evidence of a growing backlog of prepaid/committed business (Prime, AWS).
- **Debt maturity ladder is well-laddered:** $8.5B due in 12 months, $5.3B yr-2, $3.1B yr-3, $8.75B yr-4, $2.25B yr-5, $39.25B beyond year five.

---

## 7. Quality-of-earnings scorecard

| Signal | Reading | Assessment |
|---|---|---|
| CFO vs net income | 2.79x | ✅ Strong cash conversion |
| Accruals | D&A $48.7B + SBC $24.0B are 73% of CFO add-backs | ⚠️ Earnings dependent on non-cash add-backs |
| SBC as % of revenue | 4.2% (rising 3 straight years) | ⚠️ Real dilution cost; $18.3B unrecognized |
| Interest income contribution | $2.95B, 40% of pre-tax growth tailwind | ⚠️ Rate-cycle dependent |
| Equity mark-to-market | +$1.0B (2023) vs –$13.6B (2022) | ⚠️ Volatile swing factor (Rivian-type) |
| Cash tax vs book tax | $11.18B paid vs $7.12B provision | ⚠️ Cash tax rate rising |
| Deferred revenue growth | +28% | ✅ Forward demand visibility |
| Working capital | –$8.6B → +$7.4B | ✅ Improving, though AP growth slowed |
| Goodwill/intangibles impairment | $0 in FY23 | ✅ No impairment |
| Dilution | Shares +1.3% | Neutral |

---

## 8. Insider activity

**DATA UNAVAILABLE.** The data package contains **no authorized point-in-time insider-transactions archive for AMZN as of 2024-02-09**. I will not infer or fabricate insider buying/selling. Treat this as a genuine gap: any statement in the market about Amazon insider activity around this print is **not verifiable through my tools** and should be sourced independently (Form 4 filings on EDGAR).

---

## 9. Actionable insights for traders

**Bull case (evidence-based, from this 10-K):**
1. **FCF inflection is structural so far:** FCF +$32.2B vs –$16.9B, with capex intensity down 320 bp to 9.2% of sales while revenue accelerated to +11.8%. If FY24 capex holds near $55–60B and CFO stays at $85B+, FCF remains $25–30B+ — the basis for any multiple-expansion argument.
2. **Margin expansion is broad and repeatable:** gross margin +500 bp in two years with G&A *down* YoY and marketing up only 5%. There is more room in fulfillment/regionalization and in AWS cost-per-unit.
3. **Balance sheet optionality:** ~$144B liquidity, net cash ~$74B ex-leases, debt down 13%, and **zero buybacks in FY23**. Announcement of a buyback or a dividend initiation would be a new, un-priced catalyst.
4. **Demand visibility:** deferred revenue +28% and $157.8B of obligations beyond year five.

**Bear case / risks:**
1. **Q4 concentration:** ~87% of FY23 FCF came from Q4-23. A soft Q4 or a heavy Q1-24 capex print would make the FCF narrative look fragile quarter-to-quarter.
2. **Capex re-acceleration is already visible:** Q3-23 $12.5B → Q4-23 $14.6B. Capex/D&A at 1.08x is arguably *below* maintenance-plus-growth for a cloud/AI business; a snap-back to 12% of sales would add ~$16B of capex and halve FCF.
3. **SBC dilution and comp inflation:** $24.0B, +22% YoY, 65% of operating income. Any move to "fix" comp via more cash comp hits margins directly.
4. **Earnings mix is not all operating:** $2.95B interest income + $1.0B equity marks. A rate-cut cycle and mark-to-market reversals would compress headline EPS.
5. **Cash taxes rising:** $11.2B paid vs $7.1B provision, deferred benefit shrinking from –$8.1B to –$5.9B — a structural FCF headwind.
6. **Vendor-financing tailwind fading:** AP +6.7% vs revenue +11.8%; positive working capital now must be sustained by profit, not by payables stretch.

**Concrete monitoring triggers for the next print (Q1-24, expected late April):**
- **Capex:** >$16–17B in a single quarter = FCF downgrade; ≤$13B = FCF upgrade.
- **Operating margin:** ≥6.5% sustains the margin-expansion thesis; <5.5% breaks it.
- **AWS growth and advertising growth** (segment detail required — not available in this dataset).
- **SBC growth:** any print above +20% YoY keeps dilution risk live.
- **Deferred revenue:** growth <15% would flag slowing committed demand.
- **Capital return:** any buyback authorization is a step-change signal given ~$74B net cash.
- **Insider Form 4s:** must be sourced externally (see §8).

**Positioning framing (fundamental, not price-based):** The FY23 10-K is a *high-quality* report — it converts a 2022 story of negative FCF and margin collapse into positive FCF and 6.4% operating margins in 12 months. But because FY2023 EPS of $2.90 includes ~$0.36 of after-tax interest income and an equity-mark tailwind, and because the FCF is one quarter in nature, the appropriate posture is *"constructive but verify capex"*: the thesis holds as long as management defends capex discipline and margin. Note that **valuation multiples cannot be computed here** — no price/market-cap or consensus data was provided by the tools; apply the reported EPS ($2.90 diluted) and derived metrics to your own market data.

---

## 10. Data provenance and gaps (read this before acting)

- **Covered:** FY2021–FY2023 annual income statement, balance sheet and cash flow from the **FY2023 10-K (filed 2024-02-02)**; partial 2023 quarterly cash-flow facts from the **Q3-23 10-Q (filed 2023-10-27)** used for the Q4 bridge.
- **Derived (labeled):** net sales, gross profit, total current liabilities, working capital, current ratio, quarterly Q4 figures, free cash flow, coverage ratios.
- **Not available from tools:** segment revenue/operating income (3 segments exist but no segment tags), fulfillment and technology & infrastructure expense lines, inventory balances (so no inventory turns), quarterly income statement detail, consensus estimates, market price/market cap, and **insider transactions**.
- **Precision caveat:** "cash + securities" uses the AFS fair value of $70,919M; Amazon also holds non-marketable equity of $754M, excluded here.
- **Reference figures not in the tag subset (from the 10-K balance sheet):** total stockholders' equity $201,875M (2023) and $146,043M (2022); total liabilities implied at $325,979M. Used only for ROE/leverage context.

---

## 11. Key points summary table

| Category | Metric | FY2021 | FY2022 | FY2023 | Signal | Trader takeaway |
|---|---|---|---|---|---|---|
| **Growth** | Net sales *(derived)* | $469.8B | $514.0B (+9.4%) | **$574.8B (+11.8%)** | 🟢 Re-accelerating | Growth is inflecting, not decelerating — supports the FCF+margin combo |
| **Profitability** | Gross margin | 42.0% | 43.8% | **47.0%** | 🟢 +500 bp in 2 yrs | Mix shift (AWS/ads/3P) is durable |
| **Profitability** | Operating income / margin | $24.9B / 5.3% | $12.2B / 2.4% | **$36.9B / 6.4%** | 🟢 Record of the 3 yrs | Operating leverage is real, not cost-cut-only |
| **Profitability** | Net income / diluted EPS | $33.4B / $3.24 | –$2.7B / –$0.27 | **$30.4B / $2.90** | 🟢 Full recovery | Note $2.95B interest income + $1.0B equity mark flatter EPS |
| **Cash flow** | CFO | $46.3B | $46.8B | **$84.9B** | 🟢 +82% | Cash generation doubled |
| **Cash flow** | Capex | $61.1B | $63.6B | **$52.7B** | 🟢 –17% | Capex/sales 9.2% vs 12.4% — key FCF lever |
| **Cash flow** | **FCF (CFO–capex)** | –$14.7B | –$16.9B | **+$32.2B** | 🟢 **+$49.1B swing** | The core thesis change |
| **Cash flow** | Q4-23 FCF *(derived)* | — | $12.6B (Q4-22) | **$27.9B** | 🟢 +122% YoY | ~87% of FY FCF in one quarter → concentration risk |
| **Balance sheet** | Cash + securities | — | — | **≈$144.3B** | 🟢 | Ample liquidity for capex or buyback |
| **Balance sheet** | LT debt / finance leases | — | $67.2B / $15.8B | **$58.3B / $12.1B** | 🟢 –13% / –23% | Deleveraging; no LT debt issued in FY23 |
| **Balance sheet** | Net cash (ex-op-leases) *(derived)* | — | — | **≈+$74B** | 🟢 | ~Neutral including $75.6B op leases |
| **Balance sheet** | Working capital *(derived)* | — | –$8.6B | **+$7.4B** | 🟢 +$16.0B swing | But AP growth (+6.7%) lagging revenue — tailwind fading |
| **Quality** | SBC | $12.8B (2.7% of sales) | $19.6B (3.8%) | **$24.0B (4.2%)** | 🔴 Rising 3 yrs | ~65% of operating income; $18.3B unrecognized |
| **Quality** | Cash taxes paid vs provision | $3.7B / $4.8B | $6.0B / –$3.2B | **$11.2B / $7.1B** | 🔴 Rising cash tax rate | Structural FCF headwind |
| **Quality** | Interest expense / coverage | $1.8B | $2.4B | **$3.2B / 26.9x EBITDA** | 🟡 Rising but covered | Comfortable |
| **Forward** | Deferred revenue | — | $16.1B | **$20.6B (+28%)** | 🟢 | $12.4B of FY23 revenue from opening backlog |
| **Forward** | Contractual obligations | — | — | **$300.4B** ($157.8B >5 yrs) | 🟡/🟢 | Demand signal + commitment risk |
| **Capital return** | Buybacks | $0 | $6.0B | **$0** | 🟡 Unused lever | With ~$74B net cash, authorization = new catalyst |
| **Insider** | Form 4 activity | — | — | **DATA UNAVAILABLE** | ⚪ | Must be sourced externally; not inferred |

**One-line thesis:** AMZN's FY2023 10-K (filed 2024-02-02) documents a completed turnaround — 6.4% operating margin, **+$32.2B FCF from –$16.9B**, and a $74B net cash position — making the stock fundamentally better-supported than a year ago, but the durability of that FCF now rests entirely on **capex discipline in 2024** and on **$24B+ of stock comp** not eating the margin gains.