# AMZN — Fundamental Deep Dive (point-in-time: 23 Sep 2026)

**Identity check:** SEC CIK 1018724 (visible in the accession numbers) = Amazon.com, Inc. All figures below come from the 10-Q filed **2026-07-31** for the period ended **2026-06-30**, plus the prior-quarter 10-Q filed 2026-04-30. **No filing has occurred in the past ~8 weeks**, so this is the most recent fundamental truth set; Q3 2026 (quarter ending 9/30/26) is the next catalyst.

**Data caveats (important for how you use this):**
- The vendor package contains **no annual (FY2024/FY2025) statements, no segment P&L, no guidance, and no price/market-cap data**. History below is built from quarterly facts (Q1'25 → Q2'26) plus trailing-twelve-month (TTM) tags. Longer multi-year history could not be retrieved.
- Revenue is **derived** as `CostsAndExpenses + OperatingIncomeLoss` (the "Revenues" tag is absent). This derivation reproduces known Q2'25/H1'25 revenue ($167.7B / $323.4B) exactly, so it is reliable.
- **Insider transactions: DATA_UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for AMZN. I will not infer or fabricate insider activity.

---

## 1. Executive summary — the six things that matter

1. **Operating momentum is accelerating at immense scale.** Q2'26 revenue ≈ **$200.6B, +19.6% y/y** — the first $200B quarter and the strongest growth in the dataset — while operating margin expanded to **13.7%** from 11.4%. Growth *and* margin expansion simultaneously at this size is the single most bullish fundamental datapoint.
2. **Headline EPS is largely fictional this year.** Q2'26 GAAP EPS of **$5.75** includes a **$50.5B non-cash mark-up of non-marketable equity securities** (plus $1.3B marketable equity gains, less $1.45B warrant losses). Roughly **~80% of Q2 pretax income was non-operating mark-to-market**. Adjusted, Q2 EPS is **~$2.17 (+27% y/y)** — still excellent, but less than 40% of the reported number.
3. **Capex is a super-cycle, and free cash flow has gone negative.** TTM capex **$173.0B** vs TTM OCF **$161.4B** → **TTM FCF ≈ –$11.6B**; H1'26 FCF **–$27.0B**. Capex is now **27% of revenue** (Q2'26) vs 19% a year ago, with capex at **2.3x depreciation** — meaning the depreciation wave has barely begun.
4. **The build-out is being debt-funded.** Long-term debt rose from **$68.8B to $133.0B in six months (+93%)**; $81.9B issued TTM. Interest expense **+155% y/y** in Q2. Net cash (cash+securities minus debt+finance leases) **halved from $51.5B to $29.7B**.
5. **A $122.3B private-equity stake now sits on the balance sheet** (11% of total assets), up from $16.2B at year-end (7.5x in six months). It added **$62.8B of pretax income in H1'26** and **$38.1B to AOCI/book value**. It is marked, not monetized — and reversible.
6. **Balance sheet remains fortress-grade:** $78.2B cash + $97.9B liquid securities = **$176.1B**, against $146.4B total debt + finance leases. The company is still net cash; the *trajectory* is what has changed.

---

## 2. Company profile

Amazon.com, Inc. (NASDAQ: AMZN), founded 1994, headquartered in Seattle. The Q2'26 filing confirms **3 reportable operating segments**: **North America**, **International**, and **Amazon Web Services (AWS)**. Revenue lines inside those segments: online stores, third-party seller services (1P/3P marketplace, fulfillment, advertising), subscription services (Prime), AWS (compute, storage, database, AI/ML), physical stores, and other. The business is vertically integrated across logistics, retail, advertising, cloud infrastructure, custom silicon, and — increasingly — energy and data-center capacity (the filing discloses **270 million MWh of energy derivative notional** and $650B of contractual obligations, consistent with power/space commitments for AI infrastructure).

In practical terms for a trader: AMZN is three businesses in one wrapper — a low-margin, high-volume retail/logistics machine; a high-margin advertising and subscription annuity layered on top of it; and AWS, the profit engine and the reason capex is exploding. The **segment split was not returned by the tools**, so all margin commentary below is consolidated.

---

## 3. Income statement — Q2 and H1 2026

### 3.1 Consolidated results ($B unless noted)

| Metric | Q1'25 | Q2'25 | Q1'26 | Q2'26 | Q2 y/y | H1'25 | H1'26 | H1 y/y |
|---|---|---|---|---|---|---|---|---|
| Revenue (derived) | 155.667 | 167.702 | 181.519 | **200.606** | **+19.6%** | 323.369 | **382.125** | **+18.2%** |
| Cost of goods/services | 76.976 | 80.809 | 87.463 | 95.778 | +18.5% | 157.785 | 183.241 | +16.1% |
| Gross profit | 78.691 | 86.893 | 94.056 | 104.828 | +20.6% | 165.584 | 198.884 | +20.1% |
| Gross margin | 50.6% | 51.8% | 51.8% | **52.3%** | +50bp | 51.2% | **52.0%** | +80bp |
| Operating expense | 51.032 | 67.722 | 70.204 | 77.367 | +14.2% | 128.008 | 147.571 | +15.3% |
| Opex % of revenue | 32.8% | 40.4% | 38.7% | **38.6%** | –180bp | 39.6% | **38.6%** | –100bp |
| **Operating income** | 18.405 | 19.171 | 23.852 | **27.461** | **+43.3%** | 37.576 | **51.313** | **+36.6%** |
| **Operating margin** | 11.8% | 11.4% | 13.1% | **13.7%** | **+230bp** | 11.6% | **13.4%** | **+180bp** |
| Non-operating income | 3.274 | 1.686 | 15.982 | **53.396** | nm | 4.960 | 69.378 | nm |
| Pretax income | 21.679 | 20.857 | 39.834 | **80.857** | +288% | 42.536 | 120.691 | +184% |
| Tax expense | 4.553 | 2.678 | 9.560 | 18.199 | +580% | 7.231 | 27.759 | +284% |
| Effective tax rate | 21.0% | 12.8% | 24.0% | **22.5%** | +970bp | 17.0% | 23.0% | +600bp |
| Net income | 17.127 | 18.164 | 30.255 | **62.647** | +245% | 35.291 | **92.902** | +163% |
| Diluted EPS | 1.59 | 1.68 | 2.78 | **5.75** | +242% | 3.27 | **8.53** | +161% |
| Diluted shares (B) | ~10.77 | ~10.81 | ~10.88 | ~10.90 | +0.8% | ~10.79 | ~10.89 | +0.9% |
| **Adjusted EPS (est.)*** | 1.57 | 1.70 | 1.96 | **2.17** | **+27%** | 3.27 | **4.13** | **+26%** |

\*Adjusted = GAAP excluding (i) upward fair-value adjustments on non-marketable equity securities, (ii) marketable equity FV gains, (iii) warrant FV changes; taxed at the reported effective rate. This is my estimate, not a company-reported figure.

### 3.2 What the P&L is actually telling you

- **Top-line reacceleration is real and sequential.** Growth went 16.6% (Q1'26) → 19.6% (Q2'26). Revenue added **$18.9B sequentially**. Opex grew only 14.2% y/y against 19.6% revenue growth → genuine operating leverage, not cost cuts (G&A actually *fell* 6% to $2.788B, and marketing grew just 2.5% to $11.698B, while the growth investment went into technology/content and infrastructure, buried in COGS).
- **Gross margin is the swing factor.** Q2 gross margin 52.3% (+50bp y/y) on 18.5% COGS growth. The mix shift toward AWS/ads/3P services is doing the work, partially offset by depreciation of new AI infrastructure flowing through cost of sales.
- **Depreciation is the visible tax on the build-out:** D&A **$19.988B in Q2'26, +31.3% y/y**; H1 **$38.933B, +32.0%**; TTM **$75.2B**. Depreciation is growing ~1.6x faster than revenue. Operating margin still expanded anyway — that is the strongest evidence the incremental revenue is high-margin.
- **Reported EPS is not a usable earnings proxy.** The $5.75 includes **$50.486B** of upward adjustments on non-marketable equity (Q2) and **$62.814B** for H1. Remove the noise and the operating business earned **~$2.17** in Q2 and **~$4.13** in H1 — roughly **+26–27% y/y**. Anyone screening on "TTM EPS ~$12.4" is overstating normalized earnings power by ~30–45%.
- **Tax quality check:** Q2 tax provision $18.199B of which **$17.691B was deferred** — i.e., the tax on the unrealized marks is non-cash and deferred. **Cash taxes paid were only $2.655B in Q2 and $3.978B in H1 (a ~7% cash tax rate on adjusted pretax income)**. This is a genuine cash-flow advantage, but it also means the GAAP tax rate will stay elevated as marks accumulate.
- **Net interest income has flipped negative:** Q2 interest income $1.295B vs interest expense $1.314B. H1 still net positive (+$0.316B) but the crossover just happened — a direct consequence of the debt build.
- **SBC is flat-to-down:** $6.038B in Q2'26 vs $6.534B; $10.070B H1 vs $10.223B. Unrecognized SBC of $24.8B remains. Share count is drifting up ~0.5–0.9% y/y — no evidence of buyback support in this dataset.

### 3.3 Trailing-twelve-month snapshot

| TTM metric (Jul'25–Jun'26) | Value |
|---|---|
| Net income | **$135.281B** |
| Net income ex-H1'26 mark-ups (est.) | **~$72–87B** (range depends on Q3/Q4'25 marks, unknown) |
| Diluted EPS (reported) | **~$12.4** |
| Core EPS run-rate (Q2'26 annualized) | **~$8.7** |
| Operating cash flow | **$161.403B** |
| Capex | **$173.028B** |
| Free cash flow | **–$11.625B** |
| D&A | **$75.200B** |
| Cash taxes paid | **$6.635B** |
| Deferred tax expense | **$41.441B** |

---

## 4. Balance sheet — the two big stories are the private stake and the debt

### 4.1 Balance sheet ($B)

| Item | 12/31/25 | 6/30/26 | Change |
|---|---|---|---|
| Cash & equivalents | 86.810 | 78.213 | –8.597 |
| Marketable (AFS) securities | 45.800 | 97.900 | **+52.100** |
| Accounts receivable, net | 67.729 | 88.092 | +20.363 (+30.1%) |
| Inventory, net | 38.325 | 38.184 | –0.141 |
| **Current assets** | 229.083 | 249.264 | +20.181 |
| **Non-marketable equity securities** | **16.200** | **122.300** | **+106.100 (7.5x)** |
| **Total assets** | **818.042** | **1,095.689** | **+277.647 (+33.9%)** |
| Accounts payable | 121.909 | 147.440 | +25.531 (+20.9%) |
| Accrued liabilities | 75.520 | 73.406 | –2.114 |
| **Current liabilities** | 218.005 | 241.274 | +23.269 |
| Long-term debt (incl. current portion) | 68.836 | 132.995 | **+64.159 (+93.2%)** |
| Finance lease liability | 12.286 | 13.451 | +1.165 |
| Operating lease liability | 89.252 | 96.320 | +7.068 |
| AOCI | 28.223 | 66.287 | **+38.064** |
| Additional paid-in capital | 140.024 | 149.619 | +9.595 |
| Shares outstanding (B) | 10.731 | 10.783 | +0.5% |
| Working capital | 11.078 | 7.990 | –3.088 |
| Current ratio | 1.051x | **1.033x** | –0.018x |

### 4.2 Interpretation

- **Total assets grew $277.6B (+34%) in six months** — of which **$106.1B is the revaluation of a private equity stake** and roughly **$64B is debt-funded cash/securities accumulation**. Only a minority of the asset growth reflects operating scale.
- **The $122.3B non-marketable position is now 11.2% of total assets.** It is the second-largest identifiable asset class after PP&E. It rose 7.5x in six months on **$62.8B of upward adjustments** (plus purchases). The filing does not name the holding, but the size, timing and mark pattern are consistent with a large strategic AI investment (widely associated with Amazon's Anthropic stake) — treated here as an inference, not a stated fact. **This is the largest single source of earnings and book-value volatility in the company.**
- **Book equity** is not directly in the extract. Derived: total equity is roughly **$550–570B** (up from ~$400–420B at YE25), reflecting $131.0B of H1 comprehensive income plus ~$10B SBC. That implies reported ROE of ~24–28% TTM, but **core ROE of ~15–17%** on ~$85–90B of core earnings. The gap is entirely mark-to-market.
- **Current ratio 1.03x** is thin but structurally normal for AMZN, which funds itself with **$147.4B of payables (+20.9%)**. Payables are growing slightly faster than revenue — supplier financing is doing real work here. Receivables growing **+30%** vs revenue **+19.6%** is worth a second look (mix shift toward AWS/ads/business customers; allowance rose $2.4B→$2.8B).
- **Inventory is flat at $38.2B while revenue grew 19.6%** — inventory turns are improving and inventory valuation reserves fell $3.3B→$3.0B. That is a clean, high-quality signal in the retail business.
- **Leverage:** gross debt + finance leases **$146.4B** vs cash + securities **$176.1B** → **net cash ~$29.7B**, down from **~$51.5B** at YE25. Adding operating leases ($96.3B), total fixed obligations are ~$242.7B. Against ~$100B+ of EBITDA this is still investment-grade-light, but the direction of travel is unambiguous: **the company is converting balance-sheet headroom into AI infrastructure.**

---

## 5. Cash flow — the crux of the debate

### 5.1 Cash flow ($B)

| Metric | Q2'25 | Q1'26 | Q2'26 | H1'25 | H1'26 | TTM |
|---|---|---|---|---|---|---|
| Operating cash flow | 32.515 | 26.032 | **45.387** | 49.530 | **71.419** | **161.403** |
| Capex (productive assets) | 32.183 | 44.203 | **54.208** | 57.202 | **98.411** | **173.028** |
| **Free cash flow** | **+0.332** | **–18.171** | **–8.821** | **–7.672** | **–26.992** | **–11.625** |
| Acquisitions, net of cash | 1.700 | 15.408 | **24.359** | 1.652 | **39.767** | 41.956 |
| Purchases of marketable securities | 17.797 | 23.256 | 26.006 | 31.130 | 49.262 | 72.902 |
| Proceeds from sales/maturities | 11.441 | 17.686 | 24.196 | 19.178 | 41.882 | 67.090 |
| LT debt issued | 0.000 | 53.441 | 13.557 | 0.746 | 66.998 | 81.925 |
| LT debt repaid | 2.751 | 0.000 | 2.752 | 2.751 | 2.752 | 5.022 |
| ST debt, net | +0.701 | +4.836 | –0.205 | +0.434 | +4.636 | +1.600 |
| **Net financing** | –2.539 | +52.767 | +10.146 | –2.586 | **+62.913** | **+75.160** |
| **Net investing** | –39.424 | –64.212 | –79.245 | –69.227 | **–143.457** | **–216.775** |
| Net change in cash | –8.440 | — | –23.765 | –20.859 | –9.179 | +19.474 |

| Ratio | Q2'25 | Q2'26 |
|---|---|---|
| Capex / revenue | 19.2% | **27.0%** |
| Capex / OCF | 99% | **119%** |
| Capex / D&A | 2.11x | **2.71x** |

### 5.2 Interpretation

- **OCF is compounding fast: H1'26 $71.4B vs $49.5B (+44%)**, and Q2 OCF of $45.4B is the highest quarterly figure in the dataset. Operating cash generation is *not* the problem.
- **The problem is that capex is compounding faster: H1 capex $98.4B vs $57.2B (+72%)**, and Q2 capex of $54.2B is a quarterly record. **Capex is now 27% of revenue and 2.7x depreciation** — this is the mathematical signature of an infrastructure build where the depreciation drag is still 2–3 years from peaking.
- **FCF is structurally negative for now** (–$11.6B TTM, –$27.0B H1). Importantly, it is *improving sequentially*: Q1'26 was –$18.2B, Q2'26 –$8.8B, because OCF rose $19.4B sequentially while capex rose $10.0B. If that delta persists, Q3/Q4 could return to positive FCF — **that is the single most important thing to watch**.
- **M&A has re-entered the story in a big way:** $39.8B in H1'26 vs $1.65B in H1'25, with **$24.4B in Q2 alone**. This is a step-change in capital deployment, funded with debt, that will add intangible amortization and integration risk in 2027.
- **The funding mix has completely flipped:** H1'26 net financing **+$62.9B** vs –$2.6B in H1'25. Amazon went from a self-funding FCF machine to a debt-funded builder in two quarters.

---

## 6. Forward obligations — the $650B number

At 6/30/26 the company disclosed **total contractual obligations of $650.0B**, with a maturity ladder of:

| Due | $B |
|---|---|
| Remainder of FY26 (Jul–Dec) | 42.752 |
| Next 12 months (from 6/30/26) | 78.084 |
| Year 2 | 53.406 |
| Year 3 | 46.767 |
| Year 4 | 42.219 |
| Beyond | ~387 |

Separately: **operating lease payments of $116.4B** (undiscounted; $14.8B within 12 months) and finance lease payments of $16.7B. The operating lease liability rose $89.3B → $96.3B in six months, with the weighted-average discount rate up 3.7% → 3.9%.

**Read-through:** $78.1B of obligations due within twelve months is roughly 1.7x annualized OCF-after-interest headroom being pre-committed. This is a demand *signal* (long-dated AI/compute/energy commitments imply contracted demand) and a *risk* (fixed-cost rigidity if the demand curve disappoints). It also explains why debt issuance accelerated.

---

## 7. Capital returns, dilution, and insider activity

- **No buyback evidence in the dataset.** Cash flow lines show no treasury-stock purchases; share count rose from 10.731B to 10.783B (+0.5%) and diluted from ~10.81B to ~10.90B (+0.8%). At current free cash flow, buybacks are not a 2026 lever.
- **SBC discipline is decent:** down y/y in absolute dollars despite 19% revenue growth, though the $24.8B unrecognized cost will flow through 2027–2029.
- **Insider transactions: DATA_UNAVAILABLE.** The vendor package contains no authorized point-in-time insider archive for AMZN as of 2026-09-23. **No insider buying or selling is reported or implied in this note.** Do not read the absence of data as an absence of activity — it is a data gap, and it is a genuine analyst blind spot this week.

---

## 8. Risk register

| # | Risk | Evidence | Magnitude |
|---|---|---|---|
| 1 | **Earnings quality / mark reversal** | $122.3B non-marketable stake; $62.8B H1 mark-up = ~68% of H1 pretax income | A 10% markdown = ~$12.2B pretax, ~$0.86 EPS, ~2% of book |
| 2 | **Depreciation wave** | Capex $173.0B TTM = 2.3x D&A; D&A already +31% y/y | Each $10B of incremental D&A ≈ 2.6% of quarterly revenue as margin headwind |
| 3 | **Negative FCF persists** | –$11.6B TTM; capex 27% of revenue and rising | Prolonged negative FCF compresses the multiple independent of EPS |
| 4 | **Leverage trajectory** | Debt +93% in 6 months; net cash halved; interest expense +155% | Another two quarters at this pace → net debt, and a higher cost of capital |
| 5 | **Fixed-cost rigidity** | $650B contractual obligations, $78.1B due <12 months | Demand shortfall converts operating leverage into operating deleverage |
| 6 | **Working-capital dependence** | Current ratio 1.03x; AP $147.4B (+20.9%) | Supplier terms or a demand shock would bite quickly |
| 7 | **M&A integration** | $39.8B H1'26 acquisitions vs $1.65B H1'25 | Amortization + execution risk into 2027 |
| 8 | **Tax rate normalization** | Cash tax 7% vs GAAP 23%; $41.4B TTM deferred tax | Any change to deferral/global minimum tax hits cash flow |
| 9 | **Information staleness** | Last filing 7/31/26; no guidance, no segment data, no insider data | 8-week blind spot into a Q3 print |

---

## 9. Actionable conclusions for traders

**The bull case is operating, not accounting.** Revenue growth accelerated to +19.6% *while* operating margin expanded 230bp to 13.7%, *while* depreciation grew 31%. That combination is very hard to fake and is the cleanest evidence that the AI infrastructure spend is converting into high-margin revenue (AWS + ads). The retail core is also visibly healthier: inventory flat on 19.6% revenue growth, G&A down 6%, marketing up only 2.5%.

**The bear case is cash flow and balance-sheet transformation.** Amazon spent $173B on capex over twelve months, $39.8B on acquisitions in six months, issued $82B of debt, and produced **negative free cash flow**. Net cash halved. Contractual obligations stand at $650B. If AI demand digests, the fixed-cost base doesn't flex.

**Concrete positioning guidance:**

1. **Do not trade AMZN off GAAP EPS.** Reported TTM EPS ~$12.4 vs a core run-rate of ~$8.5–8.7. Use Q2'26 adjusted EPS **$2.17** (annualized ~$8.7) and H1 adjusted **$4.13** as your base. A screen showing "cheap on TTM earnings" is wrong by 30–45%.
2. **The single highest-conviction catalyst is the FCF inflection.** Q1'26 FCF –$18.2B → Q2'26 –$8.8B is a $9.3B sequential improvement driven by OCF (+$19.4B q/q) outrunning capex (+$10.0B q/q). If Q3 delivers positive FCF, the "capex is destroying cash" narrative breaks and the stock should re-rate. If capex steps up again (likely, given the $650B obligation ladder), expect multiple compression regardless of EPS.
3. **Watch capex/revenue at the Q3 print.** 27.0% in Q2'26 is the line in the sand. A print above ~30% is a de-rating risk; a print at or below 27% with revenue growth ≥18% is a strong add signal.
4. **Track the mark, don't forecast it.** The $122.3B private stake is ~11% of assets and worth ~$0.86 of EPS per 10% move. Consensus models that extrapolate H1's $62.8B gain into H2 will be badly wrong in either direction. Any Q3 headline EPS number should be mentally de-marked before you react.
5. **Credit signals lead equity signals here.** Interest expense +155% y/y, net interest income turning negative, and $82B of TTM issuance are early-warning indicators. If AMZN issues another $40B+ in H2, expect equity holders to start pricing the leverage, not the earnings.
6. **Near-term setup:** no filing since 7/31/26 means the market is trading on stale fundamentals and narrative. Q3'26 earnings (late October) is the next real information event. Position sizing should reflect binary exposure to (a) Q3 revenue growth ≥18%, (b) operating margin ≥13%, and (c) capex discipline.
7. **Insider flow is a blank.** No data exists in this package. If that matters to your process, source it independently before acting — do not assume quiet insiders.

**Net fundamental stance: constructive on the operating business, cautious on the cash-flow/leverage transition, and neutral-to-negative on reported earnings quality.** The company is executing better than at any point in the dataset; it is also spending and borrowing more aggressively than at any point in the dataset. Those two facts will resolve in the Q3/Q4 prints.

---

## 10. Key points summary

| Dimension | Key metric / evidence | Read-through |
|---|---|---|
| **Identity** | Amazon.com, Inc., SEC CIK 1018724; 3 reportable segments (NA, International, AWS) | Confirmed; segment P&L not available in dataset |
| **Revenue** | Q2'26 **$200.606B, +19.6% y/y**; Q1'26 +16.6%; H1 +18.2% | Acceleration, first $200B quarter — bullish |
| **Operating margin** | Q2'26 **13.7%** vs 11.4% (+230bp); H1 13.4% vs 11.6% | Genuine operating leverage despite depreciation +31% |
| **Gross margin** | Q2'26 52.3% vs 51.8%; H1 52.0% vs 51.2% | Mix shift to AWS/ads/3P services |
| **Reported EPS** | Q2'26 **$5.75**; H1 **$8.53**; TTM ~$12.4 | **~80% of Q2 pretax income is non-cash marks — not usable** |
| **Adjusted EPS (est.)** | Q2'26 **$2.17 (+27%)**; H1 **$4.13 (+26%)**; annualized ~$8.7 | The real earnings trajectory is solid mid-20s growth |
| **Earnings quality** | $62.8B H1 non-marketable mark-up; $41.4B TTM deferred tax; cash tax rate ~7% | GAAP inflated, but cash earnings are real and lightly taxed |
| **Private stake** | Non-marketable equity **$16.2B → $122.3B** (11.2% of assets) | Largest single swing factor; ±$0.86 EPS per 10% move |
| **Operating cash flow** | Q2'26 **$45.4B**; H1 **$71.4B (+44%)**; TTM $161.4B | Strong and accelerating |
| **Capex** | Q2'26 **$54.2B**; H1 $98.4B (+72%); TTM $173.0B; **27.0% of revenue**; 2.3x D&A | AI super-cycle; depreciation wave still ahead |
| **Free cash flow** | TTM **–$11.6B**; H1 **–$27.0B**; Q1 –$18.2B → Q2 –$8.8B | Negative but improving sequentially — key catalyst |
| **M&A** | H1'26 **$39.8B** vs $1.65B H1'25 ($24.4B in Q2) | New capital-deployment regime; integration + amortization risk |
| **Debt** | LTD **$68.8B → $133.0B (+93%)** in 6 months; $81.9B TTM issuance | Funding the build with debt — leverage trajectory matters |
| **Liquidity** | Cash $78.2B + securities $97.9B = **$176.1B**; net cash ~$29.7B (was $51.5B) | Still net cash, but halved |
| **Working capital** | Current ratio 1.03x; AP $147.4B (+20.9%); inventory flat on +19.6% revenue | Efficient, but dependent on supplier terms |
| **Obligations** | **$650.0B** total contractual; **$78.1B due <12 months**; op leases $116.4B | Demand signal *and* fixed-cost risk |
| **Capital returns** | No buyback evidence; shares +0.5% y/y; SBC flat y/y | No buyback support in 2026 |
| **Insider activity** | **DATA_UNAVAILABLE** | Explicit blind spot — do not infer |
| **Next catalyst** | Q3'26 results (~late Oct 2026); quarter closes 9/30/26 | Watch revenue growth ≥18%, op margin ≥13%, capex/revenue ≤27%, FCF sign |
| **Stance** | Bullish operations / cautious cash-flow & leverage / skeptical headline EPS | Trade the FCF inflection, not the GAAP print |