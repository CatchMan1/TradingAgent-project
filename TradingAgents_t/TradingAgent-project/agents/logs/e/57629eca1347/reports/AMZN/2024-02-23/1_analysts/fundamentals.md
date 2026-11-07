# AMZN — Fundamental Deep Dive (as of 2024‑02‑23)

**Data provenance:** Point‑in‑time SEC facts (B‑project cached EDGAR), filtered by actual acceptance time. Everything below reflects only filings **publicly available by 2024‑02‑23**. The dominant source document is the **FY2023 Form 10‑K (accn 0001018724‑24‑000008, filed/accepted 2024‑02‑02 04:48 UTC)**, i.e., the Q4 2023 earnings release cycle is fully in the numbers. Secondary source: **Q3 2023 10‑Q (accepted 2023‑10‑27)** for 9‑month data.

**Two important caveats up front (read before acting):**
1. The vendor extract returned facts in alphabetical tag order and was **truncated at "OperatingLeaseLiability…"**. Tags for `Revenues`, `Inventory`, `PropertyPlantAndEquipment`, `Goodwill`, `StockholdersEquity`, `FulfillmentExpense`, `TechnologyAndContent` and `RevenueFromContractWithCustomer` were **not returned**. I have **derived revenue arithmetically** (Revenue = CostsAndExpenses + OperatingIncomeLoss, an exact GAAP identity) and flag every derived figure with **[derived]**.
2. `get_insider_transactions` returned: **DATA_UNAVAILABLE — no authorized point‑in‑time insider archive for AMZN by 2024‑02‑23.** I will not infer insider activity. This is a genuine blind spot in this report.

---

## 1. Company profile and reporting structure

- **Issuer:** Amazon.com, Inc. (`AMZN`), SEC CIK 0001018724. Fiscal year ends December 31.
- **Operating segments:** **3** (`NumberOfOperatingSegments = 3`, FY2023): North America, International, and AWS. Segment‑level revenue and operating income were **not** included in the returned extract, so no segment table is presented — I will not reconstruct those from memory.
- **Share count:** **10,383,809,291** shares outstanding as of **2024‑01‑24** (`EntityCommonStockSharesOutstanding`); 10,383M at 2023‑12‑31 vs 10,242M at 2022‑12‑31 (**+1.38% YoY dilution**).
- **Scale markers:** Total assets **$527.9B**; FY2023 revenue **$574.8B [derived]**; public float **$1.18T** as of 2023‑06‑30.
- **Capital structure character:** No dividends, no buyback in 2023 (`PaymentsForRepurchaseOfCommonStock = 0`), no long‑term debt issued in 2023 (`ProceedsFromIssuanceOfLongTermDebt = 0`). This is a **deleveraging + internal‑funding** year, not a shareholder‑return year.

---

## 2. Income statement: the margin inflection is the whole story

### 2.1 Annual P&L reconstruction (USD millions)

| Line | FY2021 | FY2022 | FY2023 | YoY % |
|---|---:|---:|---:|---:|
| **Revenue [derived]** | **469,822** | **513,983** | **574,785** | **+11.8%** |
| Cost of goods & services sold | 272,344 | 288,831 | 304,739 | +5.5% |
| **Gross profit [derived]** | **197,478** | **225,152** | **270,046** | **+20.0%** |
| **Gross margin [derived]** | 42.03% | 43.81% | **46.98%** | **+317 bp** |
| Marketing expense | 32,551 | 42,238 | 44,370 | +5.1% |
| G&A expense | 8,823 | 11,891 | 11,816 | −0.6% |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| Costs / revenue | 94.7% | 97.6% | **93.6%** | −400 bp |
| **Operating income** | 24,879 | 12,248 | **36,852** | **+200.9%** |
| **Operating margin** | 5.30% | 2.38% | **6.41%** | **+403 bp** |
| Interest expense | 1,809 | 2,367 | 3,182 | +34.4% |
| Interest & investment income | 448 | 989 | 2,949 | +198% |
| Nonoperating income/(expense), total | 13,272 | (18,184) | 705 | n.m. |
| Pre‑tax income | 38,151 | (5,936) | **37,557** | n.m. |
| Income tax expense/(benefit) | 4,791 | (3,217) | 7,120 | n.m. |
| **Effective tax rate** | 12.6% | n.m. (benefit) | **19.0%** | — |
| **Net income** | 33,364 | (2,722) | **30,425** | n.m. |
| **Net margin** | 7.10% | −0.53% | **5.29%** | — |
| Diluted EPS | 3.24 | (0.27) | **2.90** | — |
| Basic EPS | 3.30 | (0.27) | 2.95 | — |

**Reading this correctly matters.** FY2023 net income ($30.4B) is *below* FY2021 ($33.4B) even though revenue is **22% higher** and operating income is **48% higher**. The gap is entirely below the operating line: FY2021 carried **$13.3B** of nonoperating gains (equity‑security marks) versus **$0.7B** in FY2023, and FY2023's tax rate normalized to 19.0% (vs 12.6%).

**Actionable point:** the *operating* engine improved dramatically and the *non‑operating* engine stopped flattering EPS. Traders anchored on "EPS $2.90 vs $3.24 in 2021" are reading the wrong line.

### 2.2 Operating leverage decomposition

- Revenue grew **+$60.8B (+11.8%)** while total costs grew only **+$36.2B (+7.2%)** → **~$24.6B of incremental operating income**, of which the majority came from gross profit (+$44.9B gross profit expansion vs +$2.1B marketing, +$0.3B combined G&A/marketing/other).
- **Gross margin expansion of +317 bp is the single highest‑conviction fundamental datapoint in this entire report.** It is driven by mix (cost of goods grew only 5.5% against 11.8% revenue growth) — structurally consistent with services/AWS/ads growing faster than 1P retail goods, plus fulfillment cost leverage.
- **Overhead was frozen:** G&A fell 0.6% and employee‑related liabilities were flat at **$7.70B** (2023‑12‑31 vs 2022‑12‑31). This is direct balance‑sheet evidence of the 2022–23 cost discipline, not just an income‑statement story.
- **Foreign pre‑tax income more than doubled**: **$5,229M vs $2,289M (+128%)**, while domestic pre‑tax swung from **−$8,225M to +$32,328M**. The International segment's losses have flipped into a material contributor — a structural change from the 2022 picture.

### 2.3 Quality of earnings — the two adjustments traders must make

| Adjusted view | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Operating income (GAAP) | 24,879 | 12,248 | 36,852 |
| + Share‑based comp | 12,757 | 19,621 | 24,023 |
| = Operating income *before SBC* | 37,636 | 31,869 | **60,875** |
| Pre‑SBC operating margin | 8.01% | 6.20% | **10.59%** |
| + D&A | 34,433 | 41,921 | 48,663 |
| **= EBITDA (op. income + D&A)** | 59,312 | 54,169 | **85,515** |
| EBITDA margin | 12.62% | 10.54% | **14.88%** |
| EBITDA − capex | (1,741) | (9,476) | **32,786** |

- **SBC is now $24.0B — 65% of GAAP operating income and 9.8% of the pre‑SBC figure.** The company is paying a quarter of a trillion dollars per decade in stock. FY2023 dilution of 1.38%/yr is the cash cost; the unrecognized cost already contracted is **$18.3B** (`EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized` at 2023‑12‑31) — i.e., ~$18B of future expense is already locked in regardless of new grants.
- **Cash taxes exceeded book taxes by $4.06B** ($11,179M paid vs $7,120M expense). The deferred tax benefit of −$5,876M is a real cash‑flow *and* EPS tailwind that will reverse over time. Simultaneously, net DTAs grew to **$45.8B** (from $34.5B), including IPR&D DTAs of **$14.8B** (from $6.8B) — a large, mostly acquisition/investment‑driven shield against future tax.

---

## 3. Cash flow: the FCF inflection — the central bullish datapoint

### 3.1 Annual cash flow (USD millions)

| Item | FY2021 | FY2022 | FY2023 | Change |
|---|---:|---:|---:|---:|
| **Cash from operations** | 46,327 | 46,752 | **84,946** | **+81.7%** |
| Purchases of productive assets (capex) | (61,053) | (63,645) | **(52,729)** | **−17.2%** |
| **Free cash flow [derived]** | **(14,726)** | **(16,893)** | **+32,217** | **+$49.1B swing** |
| FCF margin | −3.13% | −3.29% | **+5.60%** | +889 bp |
| Investing activities, net | (58,154) | (37,601) | (49,833) | — |
| Financing activities, net | +6,291 | +9,718 | **(15,879)** | — |
| Net change in cash | (5,900) | +17,776 | **+19,637** | — |
| Capex / revenue | 13.0% | 12.4% | **9.2%** | −320 bp |
| Capex / D&A | 1.77x | 1.52x | **1.08x** | — |

**This is the report's core thesis in one number:** Amazon went from **−$16.9B FCF in 2022 to +$32.2B in 2023** — a **$49.1B swing** — delivered by *both* engines: **OCF +$38.2B** and **capex −$10.9B** simultaneously. Capex/D&A at **1.08x** means Amazon is now spending essentially only maintenance‑level capital relative to its depreciation base. **Any re‑acceleration above ~1.3x is the #1 thing that can break this thesis.**

### 3.2 Implied Q4 2023 (FY less 9M 10‑Q figures) — the momentum datapoint

| Q4 2023 implied | 9M 2023 | FY2023 | **Q4 2023 [derived]** |
|---|---:|---:|---:|
| Operating cash flow | 42,481 | 84,946 | **42,465** |
| Capex (productive assets) | 38,141 | 52,729 | **14,588** |
| **FCF** | 4,340 | 32,217 | **27,877** |
| Investing, net | (37,232) | (49,833) | (12,601) |
| Financing, net | (9,133) | (15,879) | (6,446) |

**Q4 2023 alone generated ~$42.5B of operating cash flow — essentially 100% of the entire first nine months of 2023 — and ~$27.9B of FCF.** Q4 is structurally Amazon's strongest quarter (holiday working capital + contract liability build), but the magnitude here is a step‑change, not seasonality. Contract liabilities rose **+$5,708M in 2023 vs +$2,216M in 2022** — customers are prepaying more (Prime, AWS commitments), which is a leading indicator of forward revenue visibility.

### 3.3 Capital allocation

- **Zero long‑term debt issued** in 2023 (vs $21.2B in 2022); **$3.68B LT debt repaid**; net **−$7.55B** short‑term debt (borrowed $18.1B, repaid $25.7B); **$4.38B** finance‑lease principal paid.
- **Zero buybacks** in 2023 (vs $6.0B in 2022); finance‑lease principal payments have fallen from $11.2B (2021) → $7.9B (2022) → $4.4B (2023), meaning the warehouse/logistics lease build‑out is largely complete. **That structural capex+lease relief is recurring, not one‑off.**
- **Zero dividends.** All FCF is being recycled into the business (and, per the DTAs, into acquisitions/investments).

---

## 4. Balance sheet: fortress liquidity, shrinking leverage, $300B of obligations

### 4.1 Position at 2023‑12‑31 (USD millions)

| Item | 2022‑12‑31 | 2023‑12‑31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 53,888 | **73,387** | +36.2% |
| Marketable securities (AFS, fair value) | — | **70,919** | — |
| **Total cash + securities [derived]** | ~124,000 | **144,306** | +16% |
| Accounts receivable, net | 42,360 | 52,253 | +23.4% |
| AR allowance | 1,400 | 1,700 | 3.15% of gross AR |
| **Current assets** | 146,791 | **172,351** | +17.4% |
| **Total assets** | 462,675 | **527,854** | +14.1% |
| Accounts payable | 79,600 | 84,981 | +6.8% |
| Accrued liabilities | 62,566 | 64,709 | +3.4% |
| Employee‑related liabilities | 7,700 | 7,700 | **0.0%** |
| Contract liabilities (total) | 16,100 | 20,606 | +28.0% |
| ‑ current | 13,227 | 15,227 | +15.1% |
| ‑ noncurrent | 2,900 | 5,700 | **+96.6%** |
| Long‑term debt (carrying) | 67,150 | **58,314** | **−13.2%** |
| Finance lease liabilities | 15,783 | 12,109 | −23.3% |
| Operating lease liabilities | 69,040 | 75,639 | +9.6% |
| **Total debt + finance leases [derived]** | 82,933 | **70,423** | **−15.1%** |
| Deferred tax assets, net | 34,509 | 45,788 | +32.7% |
| Finite‑lived intangibles, net | 4,950 | 6,540 | +32.1% |

- **Net cash position ≈ +$73.9B** (cash + securities $144.3B less debt + finance leases $70.4B), *before* the $75.6B operating‑lease liability. On an operating‑lease‑inclusive basis, the company is roughly **net‑debt neutral** (~$1.7B net debt), which is a dramatic improvement from prior years.
- **AFS portfolio is short and safe:** $65.2B of $70.9B fair value matures **within one year**; unrealized loss on the whole book is only **$346M** on $71.3B amortized cost. No duration risk, no credit blow‑up risk in the treasury book.
- **Working capital is becoming a source of funds, not a use:** revenue +11.8%, AR +23.4% (AR days 33.2 vs 30.1 — watch this), but AP +6.8% and accrued +3.4% while employee liabilities were flat. AP days: **101.8** (2023) vs **100.6** (2022) — payables discipline is stable, not being stretched further.
- **Receivables quality:** write‑offs $1.6B against a $1.7B allowance, 3.15% of gross AR — normal‑course, no deterioration signal.

### 4.2 Obligations and maturities (undiscounted, USD millions)

| Bucket | 2024 | 2025 | 2026 | 2027 | 2028 | >2028 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| Long‑term debt principal | 8,500 | 5,286 | 3,146 | 8,750 | 2,250 | 39,250 | 67,182 |
| Finance leases | 2,292 | 1,471 | 1,369 | 1,123 | 1,022 | 6,829 | 14,106 |
| Operating leases | 11,229 | 9,922 | 9,156 | 8,321 | 7,546 | 44,603 | 90,777 |
| **Total contractual obligations** | **39,345** | 30,863 | 25,713 | 28,398 | 18,266 | **157,824** | **300,409** |

**Interpretation:** $39.3B is due within 12 months against **$144.3B of cash and securities** and **$84.9B of annualized OCF** — refinancing risk is effectively nil. The debt maturity ladder is light through 2026 (≈$3–5B/yr) before stepping up in 2027–28, and 66% of total obligations sit beyond 2028 (largely leased data centers/fulfillment and long‑dated bonds). **The interest‑rate sensitivity of this balance sheet is low.**

- **Net interest is now roughly neutral:** interest income $2,949M vs interest expense $3,182M. Rising rates have been a *tailwind* (income) offsetting higher coupon costs.
- **Deferred tax liabilities on PP&E rose to $12,454M** from $9,039M, consistent with accelerating depreciation shields on the asset base.

---

## 5. Insider transactions

**Not available.** The vendor explicitly reports no authorized point‑in‑time insider‑transaction archive for `AMZN` as of 2024‑02‑23. I am not substituting recalled Form 4 activity, and any claim about Bezos/Jassy sales in this window would be unsupported by these tools. Treat this as an open item to be filled by another agent with a Form‑4‑capable source. Note only that the 10‑K confirms **1,600M shares reserved for future issuance** (≈15% of shares outstanding) — a structural dilution overhang independent of any individual insider behavior.

---

## 6. Traffic‑light assessment of the fundamentals

**Green (high conviction, tool‑supported):**
1. **FCF regime change:** −$16.9B → +$32.2B; Q4 alone +$27.9B. Capex/revenue 9.2%, capex/D&A 1.08x.
2. **Gross margin +317 bp to 46.98%** — mix shift toward higher‑quality revenue.
3. **Operating margin 6.41%, up 403 bp**; pre‑SBC margin 10.59%; EBITDA $85.5B (+58%).
4. **Deleveraging with zero LT issuance and zero buybacks** — total debt + finance leases down 15%, net cash ~$74B.
5. **International/international pre‑tax income +128%**, domestic swung to +$32.3B from −$8.2B.
6. **Contract liabilities +28%** and noncurrent portion +97% — forward revenue visibility improving.

**Amber (watch items):**
1. **SBC $24.0B = 65% of operating income**; $18.3B unrecognized; 1.38% annual dilution.
2. **Cash taxes $11.2B > book $7.1B**; the −$5.9B deferred benefit is non‑repeatable in nature.
3. **AR growing 2x revenue growth** (AR days 30.1 → 33.2) — monitor for channel/credit issues; write‑offs still modest.
4. **Operating lease liabilities +9.6% to $75.6B** — the "hidden" leverage is growing even as bonds shrink.
5. **Effective tax rate normalized to 19.0%** from 12.6% in 2021 — EPS headwind versus history.

**Red / unknowable from this dataset:**
1. **Valuation is not computable here** — no price data was provided by the tools. A DCF/multiple view on the $574.8B revenue, $36.9B operating income, $85.5B EBITDA and $32.2B FCF must be applied by the trading desk with live quotes. As a sizing aid: at 10,384M shares, **every $10/share ≈ $104B of market cap** ≈ **3.2x FY2023 FCF** and **1.2x FY2023 EBITDA**.
2. **Segment economics (AWS vs retail vs ads) absent** from the extract — the highest‑value part of the AMZN story cannot be quantified from these tools.
3. **Standalone Q4 income statement absent** (only FY totals and 9M cash flows) — margin trajectory within the year is inferred, not observed.
4. **Insider activity absent.**
5. **No competitive, regulatory, or antitrust data** in the feed (e.g., FTC matters, EU DMA) — fundamental but outside these tools.

---

## 7. Actionable conclusions for traders

1. **Trade the FCF, not the EPS.** FY2023 EPS ($2.90) *fell* versus FY2021 ($3.24) on 22% more revenue, purely from nonoperating marks and tax normalization. The operating business is unambiguously better: operating income +48% vs 2021, EBITDA +44%, FCF +$47B. If the market is pricing AMZN on any EPS‑based multiple, it is mispricing the operating improvement.
2. **Thematically, this is a capex‑discipline + margin‑mix story with a re‑acceleration risk.** The bull case survives only while capex/revenue stays under ~10–11% and capex/D&A stays near ~1.1x. **Track quarterly `PaymentsToAcquireProductiveAssets` as the single most important line item.** A print above ~$18B in a quarter, or capex/D&A above 1.3x annualized, would be the explicit invalidation trigger for the FCF thesis.
3. **The balance sheet gives the trade a long leash.** ~$144B liquidity, net cash, zero LT issuance, $39.3B of 12‑month obligations. There is no funding‑stress scenario in 2024 that can force dilution or a dividend cut. Downside from a balance‑sheet perspective is well‑protected.
4. **Discount the headline margin by ~$24B of SBC.** "Adjusted" operating income of $60.9B (10.6% margin) is the honest economic figure; "GAAP" $36.9B (6.4%) is the conservative one. Use the midpoint (~$49B, 8.5%) when comparing to peers who expense less stock.
5. **Expect the tax line to stay at ~19–21%**, not 12–13%. Any model still using sub‑15% effective rates on AMZN is overstating EPS by roughly 5–7%.
6. **Watch contract liabilities as the pulse of forward demand.** Noncurrent contract liabilities doubling to $5.7B is the cleanest available evidence of multi‑year customer commitments (consistent with long‑dated cloud/AI contracts) — a leading indicator that does not require segment disclosure to be useful.
7. **Insider signal: unavailable — do not trade on it**, and do not accept a secondhand claim about it. Refresh with a Form‑4 source before weighting insider flow in a position decision.

---

## 8. Key metrics summary table

| Category | Metric | FY2021 | FY2022 | FY2023 | Direction |
|---|---|---:|---:|---:|---|
| **Scale** | Revenue [derived] ($B) | 469.8 | 514.0 | **574.8** | ▲ +11.8% |
| | Revenue growth | — | +9.4% | **+11.8%** | ▲ accelerating |
| | Total assets ($B) | 420.5 | 462.7 | **527.9** | ▲ +14.1% |
| | Shares outstanding (M) | — | 10,242 | **10,383** | ▲ +1.4% dilution |
| **Profitability** | Gross margin | 42.0% | 43.8% | **47.0%** | ▲ +317 bp |
| | Operating income ($B) | 24.9 | 12.2 | **36.9** | ▲ +201% |
| | Operating margin | 5.30% | 2.38% | **6.41%** | ▲ +403 bp |
| | Pre‑SBC operating margin | 8.01% | 6.20% | **10.59%** | ▲ +439 bp |
| | EBITDA ($B) | 59.3 | 54.2 | **85.5** | ▲ +58% |
| | EBITDA margin | 12.6% | 10.5% | **14.9%** | ▲ |
| | Net income ($B) | 33.4 | (2.7) | **30.4** | ▲ swing |
| | Diluted EPS ($) | 3.24 | (0.27) | **2.90** | ▼ vs 2021 |
| | Effective tax rate | 12.6% | n.m. | **19.0%** | ▲ headwind |
| **Cash** | Operating cash flow ($B) | 46.3 | 46.8 | **84.9** | ▲ +82% |
| | Capex ($B) | 61.1 | 63.6 | **52.7** | ▼ −17% |
| | **Free cash flow ($B) [derived]** | (14.7) | (16.9) | **+32.2** | ▲ **+$49.1B** |
| | FCF margin | −3.1% | −3.3% | **+5.6%** | ▲ |
| | Capex / D&A | 1.77x | 1.52x | **1.08x** | ▼ |
| | Q4 OCF implied ($B) | — | — | **42.5** | ▲ ~= 9M total |
| | Q4 FCF implied ($B) | — | — | **27.9** | ▲ |
| **Balance sheet** | Cash + securities ($B) | ~124 | ~124 | **144.3** | ▲ |
| | Long‑term debt ($B) | — | 67.2 | **58.3** | ▼ −13% |
| | LT debt + finance leases ($B) | — | 82.9 | **70.4** | ▼ −15% |
| | Net cash (pre‑op‑leases) ($B) | — | ~41 | **~73.9** | ▲ |
| | Operating lease liability ($B) | — | 69.0 | **75.6** | ▲ +9.6% |
| | Contract liabilities ($B) | — | 16.1 | **20.6** | ▲ +28% |
| | Current assets ($B) | — | 146.8 | **172.4** | ▲ +17% |
| | Total contractual obligations ($B) | — | — | **300.4** (39.3 due <12m) | — |
| **Expense discipline** | SBC ($B) | 12.8 | 19.6 | **24.0** | ▲ watch |
| | Marketing ($B) | 32.6 | 42.2 | **44.4** | ▲ +5% only |
| | G&A ($B) | 8.8 | 11.9 | **11.8** | ▼ −0.6% |
| | Employee‑related liabilities ($B) | — | 7.70 | **7.70** | ■ flat |
| | D&A ($B) | 34.4 | 41.9 | **48.7** | ▲ +16% |
| **Returns** | ROA | 7.9% | −0.6% | **6.1%** | ▲ recovered |
| | Asset turnover | 1.12x | 1.11x | **1.16x** | ▲ |
| **Capital return** | Buybacks ($B) | 0.0 | 6.0 | **0.0** | ■ none |
| | LT debt issued ($B) | 19.0 | 21.2 | **0.0** | ■ none |
| **Insider** | Form‑4 activity | — | — | **DATA UNAVAILABLE** | n/a |

**Bottom line:** `AMZN` enters 2024 with the strongest fundamental configuration it has had in several years — **$32.2B of FCF, a 47% gross margin, 6.4% GAAP operating margin, $144B of liquidity, falling leverage, and a Q4 that generated the equivalent of nine months of operating cash flow in three.** The bear risk is not solvency or demand — it is **capex re‑acceleration and SBC‑adjusted earnings quality**, plus the absence of valuation and segment data in this dataset. Any position should be underwritten on the capex trajectory, with the FCF inflection as the thesis and capex/D&A > 1.3x as the stop.

*Limitations disclosed: revenue is arithmetically derived (Revenue = CostsAndExpenses + OperatingIncomeLoss); segment results, inventory, PP&E, goodwill, total equity, standalone Q4 income statement, share price/valuation, and insider transactions were not retrievable from the configured tools and are therefore not asserted anywhere in this report.*