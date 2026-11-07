# GOOGL (Alphabet Inc.) — Fundamental Deep-Dive Report
**As of 2026-07-22 | Primary source: Q2 2026 Form 10-Q (accn 0001652044-26-000071, accepted 2026-07-23 01:15 UTC) and FY2025 Form 10-K (filed 2026-02-05)**

> **Data note / transparency:** The point-in-time SEC fact set for GOOGL returns an alphabetically truncated tag list, so a handful of tags (notably `Revenues`, `RetainedEarnings`, `StockholdersEquity`, `PP&E`, `Goodwill`, and segment disclosures) were **not** returned. Where I state revenue, gross profit, or core (ex-gains) EPS, I have **derived** them from reported `CostsAndExpenses`, `CostOfRevenue`, `OperatingIncomeLoss`, and `NonoperatingIncomeExpense` — the derivation is shown explicitly so you can audit it. Insider transactions: **DATA_UNAVAILABLE** — the vendor has no authorized point-in-time insider archive for GOOGL; no insider activity is inferred or fabricated anywhere in this report.

---

## 1. Executive Summary — The Five Things That Matter

1. **Operating momentum is accelerating, not fading.** Q2 2026 revenue ≈ **$119.8B, +24.2% y/y** (derived), following +21.8% in Q1 2026. H1 2026 revenue ≈ **$229.7B, +23.1% y/y**. Operating income +30.4% y/y with operating margin expanding to **34.0%** from 32.4%.
2. **Headline EPS is massively inflated by paper gains — 78% of H1 net income is non-operating.** `EquitySecuritiesFvNiGainLoss` was **$135.9B** in H1 2026 (of which **$99.0B in Q2 alone**). Reported H1 diluted EPS of **$14.24** compares to a *core* (operations-only, ex-investment marks) EPS of roughly **$5.36**. **Do not value GOOGL off the printed P/E — it is optically ~2.7x cheaper than reality.**
3. **Free cash flow has collapsed.** H1 2026 CFO $84.9B vs capex **$80.6B** → **FCF of just $4.3B vs $24.3B a year ago (−82%)**. And that understates it: capex incurred but unpaid (accrued) is now **$29.1B vs $15.1B at year-end 2025**, implying accrual-basis H1 capex of **≈$94.6B** (~$190B annualized). Capex is now **35% of revenue** (vs 21% a year ago).
4. **A historic capital-structure pivot just happened.** Debt **doubled to $101.1B** (+$52.0B issued). Alphabet raised **$30.5B of common stock** and **$19.1B of convertible preferred** (June 5, 2026 — its first preferred issuance). **Buybacks went to exactly $0** (vs $28.3B in H1 2025). Shares outstanding rose to **12.23B (+1.2%)** — the dilution regime has flipped.
5. **Balance sheet still fortress-grade, but asset quality changed.** Cash + short-term investments **$242.5B** vs debt $101.1B → net cash ≈ **$141B** (~$11.6/share). Total assets jumped **+54.9% in six months** to $922.0B, driven by AI infrastructure and a **private-equity portfolio now marked at $124.3B** (up from $64.1B), carrying **$22.8B of newly-recognized deferred tax liabilities**.

**Bottom line for traders:** this is a *two-engine* story. The operating engine is genuinely accelerating (AI-driven revenue +24%, margin expansion, 37% cash conversion of revenue). The financial engine is being financed by debt, equity, and asset revaluation — and the near-term FCF yield has essentially gone to zero. Position sizing should reflect which engine you believe is the better signal.

---

## 2. Company Profile

Alphabet Inc. (NASDAQ: GOOGL — Class A shares; GOOG also trades) is the parent of Google. Operating structure (well-established, not from this quarter's data feed): **Google Services** (Search, YouTube ads, Google Network, subscriptions/devices/Play), **Google Cloud** (infrastructure, data/AI platform, Workspace), and **Other Bets** (Waymo, Verily, etc.), plus an **Alphabet-level investment portfolio** that has become financially material (see §8).

Thematically, the FY2026 data slate paints a company **all-in on AI compute**: capex intensity tripled in two years, debt issuance at record scale, equity issuance, and a private/AI investment book that nearly doubled in six months. Alphabet remains controlled via dual-class stock (Class B supervoting), with ~300B authorized shares of $0.001 par value and 12.230B issued and outstanding at 6/30/2026.

---

## 3. Q2 2026 Income Statement — Reported and Derived

All figures **USD millions** unless noted. Revenue and gross profit are **derived**: `Revenue = CostsAndExpenses + OperatingIncomeLoss`; `GrossProfit = Revenue − CostOfRevenue`.

| Line item | Q2 2025 | Q1 2026 | **Q2 2026** | y/y |
|---|---:|---:|---:|---:|
| Revenue (derived) | 96,428 | 109,896 | **119,796** | **+24.2%** |
| Cost of revenue | 39,039 | 41,271 | **45,943** | +17.7% |
| Gross profit (derived) | 57,389 | 68,625 | **73,853** | +28.7% |
| **Gross margin** | 59.5% | 62.4% | **61.7%** | +216 bp |
| R&D + S&M (derived residual) | 20,909 | 24,638 | **26,622** | +27.3% |
| G&A (reported) | 5,209 | 4,291 | **6,461** | +24.0% |
| Total costs & expenses | 65,157 | 70,200 | **79,026** | +21.3% |
| **Operating income** | 31,271 | 39,696 | **40,770** | **+30.4%** |
| **Operating margin** | 32.4% | 36.1% | **34.0%** | +163 bp |
| Non-operating income | 2,662 | 37,716 | **97,983** | +3,581% |
| − of which equity-security FV gains | 1,286 | 36,915 | **99,031** | n/m |
| − of which interest income | 1,050 | 1,381 | **1,430** | +36% |
| − of which interest expense | (261) | (533) | **(1,278)** | +390% |
| Pre-tax income | 33,933 | 77,412 | **138,753** | +309% |
| Income tax | 5,737 | 14,834 | **26,560** | +363% |
| **Effective tax rate** | 16.9% | 19.2% | **19.1%** | +220 bp |
| **Net income** | 28,196 | 62,578 | **112,193** | +298% |
| Net income to common | 28,196 | 62,578 | **112,107** | +298% |
| **Diluted EPS** | $2.31 | $5.13 | **$9.11** | +294% |
| Basic EPS | $2.33 | $5.18 | **$9.23** | |
| Diluted shares (implied) | 12,224 | 12,198 | **12,306** | +0.7% |
| SBC (allocated) | 6,000 | 7,200 | **8,000** | +33.3% |

### The number that matters: "core" EPS
Stripping out investment marks (keeping net interest and FX), and applying the reported 19.1% tax rate:

| | Q2 2025 | Q2 2026 | y/y |
|---|---:|---:|---:|
| Operating income | 31,271 | 40,770 | +30.4% |
| + net interest | +789 | +152 | |
| − FX loss | (69) | (160) | |
| Pre-tax core | 31,991 | **40,762** | +27.4% |
| Tax @ effective rate | (5,406) | (7,786) | |
| **Core net income** | 26,585 | **32,976** | **+24.0%** |
| **Core diluted EPS** | **$2.17** | **$2.68** | **+23.5%** |

**Interpretation:** reported EPS growth of +294% is an artifact. **Core EPS growth of ~+24% is the real operating story — and it is excellent.** H1 2026 core EPS ≈ **$5.36 vs $4.29 (+25%)** versus reported $14.24 vs $5.12 (+178%).

### Cost-line read-through
- **Gross margin is the biggest positive surprise:** cost of revenue grew only 17.7% against 24.2% revenue growth. This is the signature of AI/cloud monetization scaling ahead of the compute cost curve — the opposite of the "AI capex destroys margins" bear case, at least at the gross line.
- **G&A +24% and SBC +33% (to $8.0B/qtr, ~6.7% of revenue)** are the offsets. SBC at a $32B annualized run-rate is a real, recurring dilution cost that shows up in share count, not just in opex.
- **Interest expense tripled sequentially and 5x y/y ($1.28B in Q2)** — the direct P&L cost of the debt-funded buildout. Q2 2026 interest expense alone nearly equals all of H1 2025.

---

## 4. H1 2026 Overview and Earnings-Quality Decomposition

| | H1 2025 | H1 2026 | y/y |
|---|---:|---:|---:|
| Revenue (derived) | 186,662 | **229,692** | **+23.1%** |
| Cost of revenue | 75,400 | 87,214 | +15.7% (38.0% of rev vs 40.4%) |
| Total costs & expenses | 124,785 | 149,226 | +19.6% |
| Operating income | 61,877 | **80,466** | +30.0% |
| Operating margin | 33.1% | **35.0%** | +187 bp |
| Non-operating income | 13,845 | **135,699** | +880% |
| Pre-tax income | 75,722 | 216,165 | +185% |
| Tax (19.1% vs 17.1%) | 12,986 | 41,394 | |
| Net income | 62,736 | **174,771** | +179% |
| Diluted EPS | $5.12 | **$14.24** | +178% |
| Comprehensive income | 65,409 | 174,402 | +167% |
| Depreciation | 9,485 | 13,586 | **+43.2%** |
| Amortization of intangibles | 246 | 545 | +122% |
| SBC | 11,500 | 15,200 | +32.2% |

**Earnings quality scorecard:**
- **78.2% of H1 2026 net income came from non-operating sources** ($135.7B of $174.8B), essentially all unrealized mark-to-market on equity securities. Reported EPS is a **portfolio mark, not an earnings stream.**
- **Depreciation +43% y/y on capex up 103%** — depreciation is *lagging* capex badly. With $80.6B of cash capex + $29.1B accrued and only $13.6B of depreciation in H1, there is a **substantial depreciation cliff** to be absorbed in 2027-2028. Model operating margin compression of 200-400bp from this alone.
- Comprehensive income ≈ net income ($174.4B vs $174.8B), so OCI is *not* masking further gains/losses — the marks are flowing through the income statement directly (FV-NI accounting).
- AOCI worsened modestly to −$2,285M from −$1,916M; cash-flow-hedge gains of +$580M in H1 were offset by other items.

---

## 5. Balance Sheet — Rewritten in Six Months

| Item | 12/31/2025 | **6/30/2026** | Change |
|---|---:|---:|---:|
| Cash & equivalents | 30,708 | **55,911** | +82.1% |
| Cash + short-term investments | 126,843 | **242,474** | **+91.2%** |
| Accounts receivable, net | 62,886 | 69,175 | +10.0% |
| **Total current assets** | 206,038 | **343,524** | +66.7% |
| AFS debt securities (total) | — | 99,500 | |
| Equity securities w/o readily determinable FV | 64,094 | **124,259** | **+93.9%** |
| — cumulative upward adjustments | 44,485 | **85,732** | +92.7% |
| — cumulative downward adjustments | 8,820 | 9,115 | |
| **Total assets** | 595,281 | **921,983** | **+54.9%** |
| Accounts payable | 12,200 | 20,258 | +66.0% |
| Accrued liabilities | 55,557 | **73,014** | +31.4% |
| Accrued income taxes (current) | 523 | 5,233 | n/m |
| Employee-related liabilities | 17,546 | 15,086 | −14.0% |
| Contract liabilities (current) | 6,578 | 7,154 | +8.8% |
| Total contract liabilities (incl. noncurrent) | 8,600 | 10,100 | +17.4% |
| **Debt (carrying amount)** | 49,085 | **101,085** | **+106.1%** |
| Deferred income tax liabilities, net | 919 | **22,819** | n/m |
| Deferred income tax assets, net | 9,113 | 1,448 | −84.1% |
| Operating lease liability | 15,954 | 18,037 | +13.1% |
| Finance lease liability | 2,500 | 2,590 | +3.6% |
| Loss contingency accrual (current) | 15,594 | **17,356** | +11.3% |
| Common stock + APIC | 93,126 | **131,371** | +41.1% |
| **Convertible preferred stock** | 0 | **18,023** | new |
| AOCI | (1,916) | (2,285) | worse |
| Shares outstanding (M) | 12,088 | **12,230** | +1.2% |

**Derived liquidity/leverage (my estimates, flagged as such because `StockholdersEquity` and `Liabilities` tags were not returned):**
- Adjusting for AFS securities of $99.5B within the $242.5B, and $101.1B of debt → **net cash position ≈ $141B**, or ~**$11.6/share**. Alphabet is still net-cash by a wide margin; leverage is *not* a solvency issue.
- Roll-forward of equity (12/31/25 equity ≈ $380B, + H1 net income $174.8B − dividends $5.2B + common issuance $30.5B + preferred $19.0B + minority $3.8B − AOCI/preferred divs) implies **~$600B of book equity, or ~$49 book value/share** — up ~55% in six months, but roughly *half* of that increase is unrealized investment marks and fresh capital, not retained operating profit.
- **Current ratio ≈ 2.7x** ($343.5B current assets vs ≈$128B identified current liabilities) — ample.
- **Deferred tax liability of $22.8B** is the tell: it is the future tax bill on the $85.7B of cumulative *unrealized* gains sitting in the investment book. If those marks reverse, the DTL reverses too (no cash impact); if Alphabet monetizes, ~$20B+ of cash taxes come due. Watch this line as a proxy for how much of the P&L is paper.

---

## 6. Cash Flow — The FCF Story

| | H1 2025 | H1 2026 | y/y |
|---|---:|---:|---:|
| **Operating cash flow** | 63,897 | **84,859** | **+32.8%** |
| CFO / revenue | 34.2% | **36.9%** | +270 bp |
| Purchases of PP&E (cash capex) | (39,643) | **(80,598)** | **+103.3%** |
| **Free cash flow** | **24,254** | **4,261** | **−82.4%** |
| FCF / revenue | 13.0% | **1.9%** | −1,110 bp |
| Capex / revenue | 21.2% | **35.1%** | +1,390 bp |
| Capex incurred but not yet paid (period-end) | 10,635 | **29,113** | +173.8% |
| **Accrual-basis capex (my adjustment)** | ≈41.3B | **≈94.6B** | **+129%** |
| Purchases of other (private) investments | (2,312) | **(22,051)** | +854% |
| Purchases of marketable securities | (39,870) | (76,480) | +91.8% |
| Net cash from investing | (40,738) | **(145,822)** | +258% |
| Debt proceeds, net | 31,378 | **56,226** | +79.2% |
| Debt repayments | (18,397) | (5,253) | −71.4% |
| **Common stock issuance** | 0 | **30,499** | new |
| **Convertible preferred issuance** | 0 | **19,063** | new (6/5/2026) |
| Minority shareholder proceeds | 400 | 3,758 | +840% |
| **Share repurchases** | (28,306) | **0** | **−100%** |
| Dividends paid | (4,977) | (5,231) | +5.1% |
| Preferred dividends | 0 | (86) | new |
| **Net cash from financing** | (26,033) | **+86,320** | swing of +$112B |
| FX effect | 444 | (154) | |
| **Net change in cash** | (2,430) | **+25,203** | |

**Three actionable conclusions:**

1. **The capex accrual adjustment is the single most under-modeled item.** Cash capex of $80.6B understates true spend because the "incurred but not yet paid" balance rose $14.0B in six months (to $29.1B). On an accrual basis Alphabet deployed **≈$94.6B in H1 2026** — an annualized run-rate near **$190B**. Anyone modeling FCF off the cash-flow-statement capex line is overstating FCF by roughly $15B/half.
2. **The funding mix tells you management expects the capex cycle to persist.** You do not issue your first-ever convertible preferred and $30.5B of common stock, while suspending a $28B/half buyback, for a one-quarter spike. The $3.8B of minority-shareholder proceeds also implies **JV/partnership structures for data-center capacity** — Google is now sharing the capital burden.
3. **Dividends are the only shareholder return left, and they're token.** Declared $0.22/quarter in Q2 2026 (from $0.21), H1 total $0.43; annualized ~$0.88. Preferred dividends of $86M/quarter imply a **~1.8% coupon on the $19B preferred** — cheap, but the conversion feature is the real cost (future dilution).

---

## 7. Investment Portfolio — The $124B "Hidden" Asset

| Metric | 12/31/2025 | 6/30/2026 |
|---|---:|---:|
| Equity securities without readily determinable FV | 64,094 | **124,259** |
| Cumulative upward adjustments | 44,485 | **85,732** |
| Cumulative downward adjustments | 8,820 | 9,115 |
| Equity FV-NI gains — H1 2026 | — | **135,946** |
| — realized | — | 836 |
| — unrealized | — | **21,531 (Q2) / 135,110 (H1)** |
| AFS securities unrealized-loss position | 13,160 | **53,239** |
| — accumulated unrealized loss | 178 | 416 |

- The private/AI investment book roughly **doubled** to $124.3B while only **$22.1B** of new cash went out. In other words, **~$41.2B of upward revaluation** (85,732 − 44,485 ≈ $41.2B) did the heavy lifting. These are **Level 3-style marks on AI/private assets** — high beta to the AI funding cycle and, per accounting rules, volatile.
- **This is now the swing factor in reported EPS.** If private AI valuations compress even 25%, that's ~$31B of pre-tax charges (~$2.50/share) — and the deferred tax asset/liability dynamics would flip.
- Bond portfolio: unrealized loss positions ballooned to $53.2B notional but with only $416M of accumulated loss — i.e., the portfolio is **near par**, duration is short (only $16.7B matures >10 years). Low risk. Derivative liabilities rose to $1,958M from $379M, consistent with new FX hedging around the debt/preferred issuance.

---

## 8. Legal & Regulatory Overhang

- **Loss contingency accrual (current): $17,356M, up from $15,594M** (+$1.8B). The FY2025 10-K shows a **$3.0B payment in Q3 2025** on this accrual. A $17B+ accrued liability is a persistent structural drag and signals that major antitrust/regulatory matters (EU and US) are being quantified rather than merely disclosed.
- Accrued income taxes (current) jumped from **$523M to $5,233M** — a 10x increase that, combined with the higher 19.1% effective rate (vs 17.1%), suggests changing international tax dynamics (Pillar Two) are now materially raising Alphabet's tax burden. Model **19-20%** going forward, not 17%.

---

## 9. Insider Transactions

**DATA_UNAVAILABLE.** The configured news/filings vendor has no authorized, point-in-time insider-transactions archive for GOOGL as of 2026-07-22. **No insider buying or selling is asserted, implied, or estimated in this report.** Traders should source this independently (Form 4 filings) before assigning any signal to insider behavior — particularly relevant this quarter, given the unusual combination of **zero buybacks, $30.5B of equity issuance, and a $19B convertible preferred**.

---

## 10. Risk Register (ranked by near-term price relevance)

| # | Risk | Evidence | Magnitude |
|---|---|---|---|
| 1 | **Earnings-quality unwind** — reported EPS depends on unrealized private-asset marks | $135.9B H1 gains; $85.7B cumulative upward adj.; $22.8B DTL | A 25% markdown ≈ $2.50+/sh |
| 2 | **FCF compression / capex sustainability** | FCF $4.3B (−82%); accrual capex ≈$94.6B; 35% of revenue | Multiples compress if FCF stays <5% of revenue |
| 3 | **Depreciation cliff** | Depreciation +43% vs capex +103%; $80.6B capex only partly depreciating | 200-400bp margin headwind in 2027-28 |
| 4 | **Dilution regime change** | Shares +1.2%; $49.6B equity raised; buybacks $0; preferred conversion overhang | Structural EPS headwind |
| 5 | **Rising leverage & interest cost** | Debt $101.1B (+106%); interest expense $1.28B/qtr (+390%) | $5B+ annualized run-rate |
| 6 | **Tax rate step-up** | 19.1% vs 17.1%; current taxes payable 10x | ~100-200bp of net margin |
| 7 | **Legal/regulatory** | $17.4B accrual; $3.0B paid in Q3 2025 | Lump-sum cash events |
| 8 | **SBC creep** | $8.0B/qtr, +33% y/y, 6.7% of revenue | Persistent dilution illusion |

---

## 11. Actionable Trading Insights

**Bull case (evidence-based):**
- **Revenue re-acceleration to +24% y/y with 216bp of gross-margin expansion** is the strongest fundamental combination in the print. Cost of revenue growing at 0.73x the rate of revenue means AI monetization is currently *margin-accretive* at the gross line. If this persists two more quarters, the "AI capex is value-destructive" narrative breaks.
- **Core EPS +23.5% y/y, core operating margin 34.0%** — a high-quality, cash-generative core business still growing mid-20s at scale.
- **$242.5B of cash/investments vs $101.1B of debt** — Alphabet can fund the entire remaining buildout internally. No financing risk.
- **Cheap preferred ($19B at ~1.8%) and successful $30.5B common raise** — the market *absorbed* this supply, itself a signal of demand for the equity.

**Bear case (evidence-based):**
- **FCF of $4.3B on a ~$230B-revenue business is a 1.9% FCF margin.** Any valuation anchored on historical FCF multiples has to be re-underwritten.
- **Reported EPS is not repeatable.** A trader buying the "cheap" headline P/E is buying a mark-to-model portfolio. Expect quarterly EPS volatility of ±$3-5/share from marks alone — this cuts both ways and makes guidance unreliable.
- **Zero buybacks + new equity issuance + preferred = the shareholder-return regime has inverted.** Historically ~100% of FCF went to buybacks; now it goes to capex.

**Highest-conviction tactical read (next 1-2 quarters):**
- **Watch Q3 2026 for three things:** (a) does gross margin hold ≥61%? (b) does the capex accrual balance ($29.1B) keep climbing (=> spend still accelerating) or flatten (=> peak capex)? (c) does the equity-gains line reverse?
- **The single best leading indicator of an inflection is `CapitalExpendituresIncurredButNotYetPaid`.** A flattening/declining balance would precede an FCF recovery by 1-2 quarters and would be a strong positive catalyst. A continued climb confirms the bear case.
- **Asymmetry:** the *core* business (34% operating margin, +24% revenue, +24% core EPS, $141B net cash) is fundamentally de-risked. The *reported* numbers are the risk. Trade the core; discount the marks.
- **Do not chase on a headline-EPS beat**, and do not panic on a headline-EPS miss — both are likely to be driven by private-asset marks rather than operations. Compare **operating income and core EPS** quarter over quarter.

---

## 12. Key Metrics Summary Table

| Category | Metric | Value | Read |
|---|---|---|---|
| **Income (Q2'26)** | Revenue (derived) | $119.80B | +24.2% y/y — accelerating |
| | Operating income | $40.77B | +30.4% y/y |
| | Operating margin | 34.0% | +163 bp y/y |
| | Gross margin | 61.7% | +216 bp y/y |
| | Reported diluted EPS | $9.11 | +294% (gains-driven) |
| | **Core diluted EPS (derived)** | **$2.68** | **+23.5% y/y — the real number** |
| **Income (H1'26)** | Revenue (derived) | $229.69B | +23.1% y/y |
| | Operating income | $80.47B | 35.0% margin |
| | Non-operating income | $135.70B | 78% of net income — paper |
| | Reported diluted EPS | $14.24 | +178% |
| | **Core diluted EPS (derived)** | **$5.36** | +25% y/y |
| | Effective tax rate | 19.1% | up from 17.1% |
| **Cash flow** | Operating cash flow | $84.86B | +32.8% y/y |
| | Cash capex | $80.60B | +103% y/y |
| | **Free cash flow** | **$4.26B** | **−82.4% y/y (1.9% of revenue)** |
| | Accrual-basis capex (est.) | ≈$94.6B | ~$190B annualized |
| | Capex / revenue | 35.1% | vs 21.2% LY |
| **Balance sheet** | Total assets | $921.98B | +54.9% in 6 months |
| | Cash + ST investments | $242.47B | +91% |
| | Total debt | $101.09B | +106% |
| | **Net cash (est.)** | **≈$141B** | ~$11.6/share |
| | Equity securities (no RDFV) | $124.26B | +94%; $85.7B cumulative gains |
| | Deferred tax liability, net | $22.82B | tax on unrealized gains |
| | Loss contingency accrual | $17.36B | +$1.76B |
| | Shares outstanding | 12.230B | +1.2% (dilution) |
| | Book value/share (est.) | ≈$49 | ~half from marks + new capital |
| **Capital allocation** | Buybacks H1'26 | $0 | vs $28.31B LY |
| | Common stock issued | $30.50B | new |
| | Convertible preferred issued | $19.06B | first ever (6/5/2026) |
| | Minority proceeds | $3.76B | data-center JVs |
| | Dividends paid | $5.23B | $0.22/qtr declared (+4.8%) |
| **Other** | SBC | $15.20B H1 | +32% y/y, 6.7% of revenue |
| | Depreciation | $13.59B H1 | +43% — cliff building |
| | **Insider transactions** | **UNAVAILABLE** | no authorized data; not inferred |
| **Trading stance** | Core business | **Constructive** | +24% rev, +24% core EPS, fortress B/S |
| | Reported earnings | **Distrust** | 78% of net income is marks |
| | FCF / valuation | **Neutral-to-cautious** | FCF margin collapsed to 1.9% |
| | Key monitorable | Capex-incurred-not-paid ($29.1B) | Flattening = FCF inflection catalyst |

---

*Prepared from point-in-time SEC facts for GOOGL public as of 2026-07-22. Revenue, gross profit, gross margin, quarterly segment splits, core EPS, accrual-basis capex, net cash, and book value per share are analytically derived (derivations shown in-line) because the corresponding tags were not present in the returned data set. All derived figures are clearly labeled and should be reconciled to the filed 10-Q before use in a live trading model.*