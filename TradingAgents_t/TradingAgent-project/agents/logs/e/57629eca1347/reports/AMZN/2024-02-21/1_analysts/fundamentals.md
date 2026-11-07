# AMZN — Fundamental Research Report
**As of:** 2024-02-21 | **Instrument:** AMZN (Amazon.com, Inc.) | **Primary source:** FY2023 Form 10-K (accession 0001018724-24-000008), accepted 2024-02-02 04:48:30 UTC — i.e., the most recent audited filing available on the analysis date. No filings dated after 2024-02-02 are in the point-in-time dataset.

> **Data provenance note:** Every figure below is either (a) a reported XBRL fact from the FY2023 10-K, or (b) explicitly labeled **"derived"** arithmetic from reported facts. Revenue is *not* present as a tagged row in this cache, so it is derived as `CostsAndExpenses + OperatingIncomeLoss` and cross-checked against reported cost lines. Insider-transaction data was **not available** for AMZN (see §9).

---

## 1. Executive summary

AMZN's FY2023 10-K marks a genuine **inflection from "growth-at-any-cost" to "profitable growth + cash generation."**

| Signal | FY2021 | FY2022 | FY2023 | Read |
|---|---|---|---|---|
| Revenue (derived) | $469.8B | $514.0B | **$574.8B** | Re-accelerated to **+11.8%** from +9.4% |
| Operating income | $24.9B | $12.2B | **$36.9B** | 3.0x the 2022 trough |
| Operating margin | 5.30% | 2.38% | **6.41%** | Best of the three years |
| Net income | $33.4B | **–$2.7B** | **$30.4B** | Full recovery |
| Diluted EPS | $3.24 | –$0.27 | **$2.90** | Still below 2021 (SBC dilution + higher share count) |
| Operating cash flow | $46.3B | $46.8B | **$84.9B** | **+81.7%** YoY |
| Capex (productive assets) | $61.1B | $63.6B | **$52.7B** | –17.1% YoY |
| **Free cash flow (derived)** | **–$14.7B** | **–$16.9B** | **+$32.2B** | **+$49.1B YoY swing** |

The core story: Amazon **cut capital intensity while revenue re-accelerated**, and cost growth (+5.5% COGS, +9.5% total opex) lagged revenue growth (+11.8%) for the first time in years. That single combination drove a ~$49B free-cash-flow swing and near-total deleveraging.

---

## 2. Company profile & business structure

- **Entity:** Amazon.com, Inc.; FY ends December 31; files as a large accelerated filer (CIK 1018724). Shares outstanding at 2023-12-31: **10,383M**; at 2024-01-24: **10,387.4M** (cover page). Authorized shares 100,000M; par $0.01.
- **Reporting structure:** The 10-K reports **3 operating segments** (`NumberOfOperatingSegments = 3`) — Amazon's North America, International, and AWS segments. *Caveat: segment-level revenue and operating-income tags were not returned by the vendor cache for this date, so this report relies on consolidated figures.*
- **Capital structure:** No dividend. `PaymentsForDividends` does not appear anywhere in the cash-flow fact set; share repurchases were **$0 in FY2023** (and $0 in FY2021), after $6.0B in FY2022.
- **Market value reference:** `EntityPublicFloat = $1.184T` as of 2023-06-30 (10-K cover page). No current price/quote data was available in the dataset, so **valuation multiples cannot be computed here** — see §11 for per-share anchors traders can apply their own multiple to.

---

## 3. Income statement deep dive

### 3.1 Revenue and cost build (derived revenue; reported cost lines)

| $ millions | FY2021 | FY2022 | FY2023 | YoY '23 |
|---|---|---|---|---|
| Cost of goods & services sold | 272,344 | 288,831 | 304,739 | **+5.5%** |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| **Revenue (derived)** | **469,822** | **513,983** | **574,785** | **+11.8%** |
| Gross profit (derived) | 197,478 | 225,152 | 270,046 | +20.0% |
| **Gross margin** | 42.03% | 43.80% | **46.98%** | +318 bps |
| Operating expenses ex-COGS (derived) | 172,599 | 212,904 | 233,194 | +9.5% |
| **Operating income** | **24,879** | **12,248** | **36,852** | **+200.9%** |
| **Operating margin** | 5.30% | 2.38% | **6.41%** | +403 bps |

**The key mechanism:** COGS grew only **+5.5%** — roughly half the revenue growth rate — lifting gross margin ~320 bps. Opex ex-COGS grew +9.5%, *below* revenue growth. This is simultaneous gross-margin and operating-leverage expansion, the rarest and most valuable earnings pattern in retail-plus-cloud models.

### 3.2 Disclosed expense lines (reported tags)

| $ millions | FY2021 | FY2022 | FY2023 | Comment |
|---|---|---|---|---|
| Marketing expense | 32,551 | 42,238 | 44,370 | +5.0% — near-zero growth, tight discipline |
| General & administrative | 8,823 | 11,891 | 11,816 | –0.6% — flat/declining |
| Advertising expense (subset) | 16,900 | 20,600 | 20,300 | –1.5% |
| Share-based compensation (total) | 12,757 | 19,621 | **24,023** | **+22.4%** — the one line outrunning revenue |
| Depreciation, depletion & amortization | 34,433 | 41,921 | 48,663 | +16.1% (lagged effect of prior capex) |
| of which depreciation | 22,909 | 24,924 | 30,225 | +21.3% |
| of which finance-lease ROU amortization | 9,857 | 6,097 | 5,899 | –3.2% (lease book shrinking) |
| Interest expense | 1,809 | 2,367 | 3,182 | +34.4% (rate effect on floating/refi) |
| Interest & investment income | 448 | 989 | 2,949 | **+198%** — cash-yield tailwind |
| Nonoperating income/(expense), net | 13,272 | (18,184) | 705 | 2022 carried –$13.6B equity-securities mark |
| Pretax income | 38,151 | (5,936) | **37,557** | |
| Income tax expense/(benefit) | 4,791 | (3,217) | 7,120 | |
| **Effective tax rate** | 12.56% | 54.2% *benefit* | **18.96%** | Normalizing |
| **Net income** | **33,364** | **(2,722)** | **30,425** | |

**Peak-to-peak observation:** FY2023 operating income ($36.9B) is **48% above FY2021** ($24.9B), but net income ($30.4B) is still **9% below** FY2021 ($33.4B). Why? (i) interest expense rose $1.4B, (ii) the FY2021 non-operating line had a **+$13.3B equity-securities gain** vs only **+$0.7B** in FY2023 (`EquitySecuritiesFvNiUnrealizedGainLoss` swung from +$11.6B in 2021 → –$13.6B in 2022 → +$1.0B in 2023), and (iii) the tax rate normalized. **Operating income is the cleaner read on the underlying business; it says the franchise is materially stronger than in 2021.**

### 3.3 Quality-of-earnings checks

- **SBC is a real and growing cost:** $24.0B in FY2023 = **4.18% of revenue** (vs 3.82% in '22, 2.72% in '21) and **28.3% of operating cash flow**. Unrecognized SBC on unvested awards at 12/31/23: **$18.3B**. FCF after subtracting SBC (a defensible "SBC-adjusted FCF") is only **~$8.2B**, not $32.2B. This is the single biggest gap between the GAAP-optimist and the skeptical view.
- **Cash taxes tripled:** `IncomeTaxesPaidNet` = $3.7B → $6.0B → **$11.2B** (+85% YoY). Cash tax rate of **29.8% of pretax income** is *above* the 19.0% book rate. Deferred tax benefit was –$5.9B, meaning book earnings are still being flattered by deferred items; the deferred-tax tailwind is shrinking as IPR&D credits get consumed.
- **D&A is rising faster than capex now** ($48.7B D&A vs $52.7B capex) — a classic sign of a maturing asset base and a leading indicator that *reported* margins already carry the depreciation of the 2021–22 build-out. If capex re-accelerates in 2024, depreciation follows with a lag.

---

## 4. Balance sheet & liquidity

### 4.1 Assets (reported)

| $ millions | 2021-12-31 | 2022-12-31 | 2023-12-31 | YoY |
|---|---|---|---|---|
| Cash & equivalents | 36,477* | 53,888 | **73,387** | +36.2% |
| Marketable securities (AFS, fair value) | n/a | n/a | **70,919** | — |
| Accounts receivable, net | n/a | 42,360 | **52,253** | +23.4% |
| **Total current assets** | n/a | 146,791 | **172,351** | +17.4% |
| **Total assets** | **420,549** | **462,675** | **527,854** | **+14.1%** |

\* 2021 figure is *cash + restricted cash* (`CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents`); 2022/23 comparable totals were $54,253M and $73,890M.

**Liquidity is very strong:** cash $73.4B + marketable securities $70.9B = **~$144.3B of liquid resources**, up from ~$118B a year earlier. AFS securities are 92% maturing within one year ($65.2B amortized cost), so the book is essentially a Treasury ladder — low duration risk (unrealized loss only ~$346M on a $71.3B book).

### 4.2 Liabilities, debt and leases (reported)

| $ millions | 2022-12-31 | 2023-12-31 | Change |
|---|---|---|---|
| Accounts payable | 79,600 | **84,981** | +6.8% |
| Accrued liabilities | 62,566 | 64,709 | +3.4% |
| Employee-related liabilities | 7,700 | 7,700 | flat |
| Contract liabilities (deferred revenue), total | 16,100 | **20,600** | +28.0% |
| — current | 13,227 | 15,227 | +15.1% |
| — noncurrent | 2,900 | **5,700** | **+96.6%** |
| **Long-term debt (carrying)** | **67,150** | **58,314** | **–8,836** |
| Finance lease liabilities | 15,783 | 12,109 | –3,674 |
| Operating lease liabilities | 69,040 | **75,639** | +6,599 |

**The deleveraging is the headline.** Total debt + leases = **$146.1B** versus **$144.3B** of cash and securities → **net debt ≈ $1.8B, i.e. essentially net-debt-neutral including leases.** Excluding operating leases, AMZN is **~$73.8B net cash**. For context, FY2023 EBITDA (operating income + D&A) is roughly **$85.5B**, implying gross debt/EBITDA of **~1.7x** and net debt/EBITDA of **~0.02x**.

**How it was funded — no new long-term debt:**
- `ProceedsFromIssuanceOfLongTermDebt` = **$0** in FY2023 (vs $21.2B in '22, $19.0B in '21)
- Long-term repayments: $3,676M; short-term borrowings net **–$7,548M** (18,129 proceeds vs 25,677 repayments)
- Financing activities: **–$15,879M** outflow (vs +$9,718M inflow in '22)

**Maturity ladder is manageable:** $8.5B due in the next 12 months (fully covered ~9x by cash), $5.3B year 2, $3.1B year 3, $8.75B year 4, $2.25B year 5, $39.25B thereafter. Total contractual obligations (incl. leases and purchase commitments) = **$300.4B**, of which $39.3B is due within 12 months and **$157.8B after year five** — long-dated, largely operating-lease and content/purchase commitments, not financial debt.

**Working-capital model (derived, approximate):** Current liabilities ≈ $191.6B vs current assets $172.4B → **current ratio ≈ 0.90**. This is structural, not distress: Amazon funds itself on ~102 **days payable** (AP $85.0B / COGS $304.7B × 365) against ~33 **days receivable**. **Flag:** AP grew +6.8% while COGS grew +5.5% — stretch is *stable, not expanding*; and AR grew +23.4% (33.2 days, up from 30.1) faster than revenue, with the doubtful-account allowance up to $1.7B from $1.4B. Watch for receivables quality in 2024 — this is a mild yellow flag, not red.

**Contract liabilities +28% (noncurrent +97%) is a genuine forward-demand signal** — $12.4B of FY2023 revenue was recognized from the prior-year deferred balance, and the growing noncurrent portion implies multi-year AWS/enterprise commitments being signed.

---

## 5. Cash flow statement — the heart of the thesis

| $ millions | FY2021 | FY2022 | FY2023 | YoY |
|---|---|---|---|---|
| **Operating cash flow** | 46,327 | 46,752 | **84,946** | **+81.7%** |
| Capex (purchases of productive assets) | (61,053) | (63,645) | (52,729) | –17.1% |
| **Free cash flow (derived)** | **(14,726)** | **(16,893)** | **+32,217** | **+49,110** |
| Investing cash flow (total) | (58,154) | (37,601) | (49,833) | — |
| Financing cash flow (total) | +6,291 | +9,718 | **(15,879)** | — |
| Net change in cash (incl. FX) | (5,900) | +17,776 | **+19,637** | — |

**Working-capital and non-cash drivers of the OCF jump:**
- D&A add-back $48,663 (+16.1%)
- SBC add-back $24,023 (+22.4%)
- Deferred taxes: **–$5,876** (a *drag* — good, means less accounting flattery)
- Contract liabilities: **+$4,578** contribution (vs +$2,216 in '22) — real cash collected ahead of revenue
- Accrued liabilities & other operating liabilities: **–$2,428** (drag, unchanged in direction from '22's –$1,558)
- AR & other operating assets: –$8,348 (drag)

**Capex intensity is falling fast:** capex/revenue = 13.00% → 12.38% → **9.17%**. OCF/revenue = 9.86% → 9.10% → **14.78%**. FCF margin = **5.60%** in FY2023 vs negative in both prior years.

**Q4 is carrying the year (derived by subtracting 9M FY2023 10-Q cumulative figures from the FY total):**
- Q4 2023 OCF = 84,946 – 42,481 = **$42,465M** (50.0% of the full year)
- Q4 2023 capex = 52,729 – 38,141 = **$14,588M**
- **Q4 2023 FCF = $27,877M = 86.5% of full-year FCF**
- 9M 2023 FCF was only **$4,340M**

**Trading implication:** earnings and cash generation at AMZN are extraordinarily Q4-weighted. Any quarter-to-quarter deceleration in Q4 holiday/ad peak will look dramatic on a TTM-FCF basis even if the annual trend is intact — and conversely, a strong Q4 mechanically "confirms" the FCF story. Do not extrapolate the Q4 FCF run-rate as a base rate.

---

## 6. Capital allocation scorecard (FY2023)

| Use of cash | Amount | Comment |
|---|---|---|
| Capex | $52.7B | –17% YoY; still 9.2% of revenue — largest single use |
| Long-term debt repayment | $3.7B | No new LT issuance |
| Net short-term debt repayment | $7.5B | |
| Finance lease principal | $4.4B | Lease book shrinking |
| Operating lease payments | $10.5B | Rising with footprint |
| Share repurchases | **$0** | Repurchase authorization dormant |
| Dividends | **$0** | Never paid |
| Acquisitions/intangibles | Intangibles gross $8.3B → **$10.1B**; IPR&D DTA $6.8B → **$14.8B** | Reflects M&A activity in FY2023; goodwill/intangibles rose, and finite-lived intangibles net grew to $6.5B |

**Assessment:** AMZN chose **balance-sheet repair and organic reinvestment over shareholder returns.** With only 3.3% share-count growth over two years and zero buybacks, there is no per-share financial-engineering support — the EPS story is entirely operational. That's a cleaner but less forgiving setup: any operating miss flows straight through to EPS and FCF/share.

---

## 7. Growth, margin and return metrics (derived)

| Metric | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Revenue growth | — | +9.4% | **+11.8%** |
| Gross margin | 42.03% | 43.80% | **46.98%** |
| Operating margin | 5.30% | 2.38% | **6.41%** |
| Net margin | 7.10% | (0.53%) | **5.29%** |
| OCF margin | 9.86% | 9.10% | **14.78%** |
| FCF margin | (3.13%) | (3.29%) | **+5.60%** |
| Capex / revenue | 13.00% | 12.38% | **9.17%** |
| SBC / revenue | 2.72% | 3.82% | 4.18% |
| SBC / OCF | 27.5% | 42.0% | **28.3%** |
| D&A / revenue | 7.33% | 8.16% | 8.47% |
| EBIT / interest expense | 13.8x | 5.2x | **11.6x** |
| Net interest (income – expense) | (1,361) | (1,378) | **(233)** |
| Total debt + leases / EBITDA (derived) | — | — | **~1.7x gross / ~0.02x net** |
| Diluted EPS | $3.24 | ($0.27) | **$2.90** |
| FCF per share (derived, ~10,491M dil. shares) | ($1.40) | ($1.61) | **$3.07** |

---

## 8. What changed in FY2023 vs. the 2022 bear case

1. **Capex discipline** — the single most important variable. $63.6B → $52.7B while growing revenue faster. The 2022 bear thesis was "Amazon is a capital furnace with negative FCF"; FY2023 numerically invalidates that.
2. **Gross margin +318 bps** on COGS growing at less than half the revenue rate — implies mix shift toward higher-margin revenue (advertising, third-party services, AWS) and/or fulfillment-cost leverage.
3. **Interest income nearly neutralized interest expense** (+$2.95B income vs $3.18B expense; net cost only $233M vs $1.38B in 2022). The rate environment that hurt in 2022 became a tailwind on the $144B liquidity pile.
4. **Deleveraging with zero new long-term debt.**
5. **The offsets:** SBC +22% to $24.0B, cash taxes +85% to $11.2B, and the shrinking deferred-tax benefit all mean **headline EPS growth in 2024 will require real operating profit growth, not accounting help.**

---

## 9. Insider transactions

**DATA UNAVAILABLE.** The vendor's point-in-time archive contains **no authorized insider-transaction (Form 4) data for AMZN as of 2024-02-21**. I will not infer, estimate, or fabricate insider buying or selling.

**How to treat this:** absence of data is **not** evidence of absence of insider sales (AMZN executives, including its founder, have historically sold under 10b5-1 plans). Treat insider sentiment as an **unresolved input** for AMZN and source it independently (SEC EDGAR Form 4 filings, Forms 144) before relying on it. It should not factor into the current recommendation either way.

---

## 10. Risks and watch-items (evidence-based)

| Risk | Evidence from the filing data | Severity |
|---|---|---|
| **SBC dilution & expense creep** | SBC $24.0B, +22.4% YoY, 4.18% of revenue; $18.3B unrecognized; share count +1.4% YoY, +3.3% over 2 yrs; **zero buybacks** to offset | **High** — FCF ex-SBC only ~$8.2B |
| **Cash tax normalization** | Cash taxes $11.2B (+85%); cash tax rate 29.8% vs book 19.0%; deferred benefit –$5.9B and DTA valuation allowance rising to $4.8B | High — suppresses future EPS upside |
| **Capex re-acceleration** | Capex/revenue fell to 9.17%; but D&A already $48.7B and rising. Any AI/infrastructure build-out reverses the FCF tailwind with a lag into depreciation | Medium-High |
| **Q4 concentration** | Q4 = 50% of annual OCF, 86.5% of annual FCF | Medium — event risk/volatility |
| **Receivables growth > revenue growth** | AR +23.4% vs revenue +11.8%; DSO 30.1 → 33.2; allowance $1.4B → $1.7B | Medium |
| **Current ratio < 1** | ~0.90 (derived) — structurally reliant on continuous operating cash flow and vendor terms | Low-Medium |
| **Lease/commitment overhang** | Operating leases $75.6B (+$6.6B); total contractual obligations $300.4B, $157.8B beyond year 5 | Low (long-dated) |
| **Tax/regulatory** | Rising state & local tax ($1.3B reconciliation item), foreign differential flipping to +$594M, prior-year adjustments –$600M | Low-Medium |
| **Concentration in "other income"** | Non-operating line swung +$13.3B → –$18.2B → +$0.7B across three years on equity marks; earnings are cleaner now but this line can re-inject volatility | Low |

---

## 11. Actionable insights for traders

**The setup is fundamentally constructive but no longer a "cheap FCF story" — it is now a "prove-the-margin" story.**

1. **Trade the operating-margin trend, not the EPS line.** Operating margin went 5.30% → 2.38% → 6.41%. The FY2023 exit rate is the highest of the three years. In any quarter where operating margin prints below ~5.5%, the FY2023 narrative is broken; above ~6.4% and it is being confirmed. This is the single highest-signal metric in the filings, because it is uncluttered by equity marks and tax noise.

2. **Capex commentary is the swing factor for the whole FCF thesis.** FY2023 FCF of +$32.2B exists *because* capex fell 17% while OCF rose 82%. OCF alone accounts for more than the entire FCF improvement. If management signals a 2024 capex re-acceleration back toward $60B+, FCF could halve or worse even with OCF growth — because the FCF base is now positive and therefore *fully exposed* to capex changes (this was masked when FCF was negative).

3. **Discount the FCF number for SBC before valuing.** $32.2B reported FCF → **~$8.2B SBC-adjusted FCF**. Sophisticated sellers will use the latter. On ~10.49B diluted shares that is **$0.78/share of SBC-adjusted FCF** vs **$3.07/share of reported FCF** — a 4x difference. Know which number the marginal buyer is using.

4. **Watch cash taxes as an EPS ceiling.** Cash taxes rose 85% to $11.2B on pretax income of $37.6B (29.8% cash rate vs 19.0% book rate). Even flat operating income with a normalizing cash tax rate compresses EPS. Deferred tax benefit (–$5.9B) is a shrinking prop.

5. **Balance sheet is now an asset, not a liability, for the equity.** Net debt ~$1.8B including leases; ~$73.8B net cash excluding them; $144B liquidity; coverage 11.6x; $8.5B due in 12 months. **This removes refinancing/rate risk from the thesis entirely** and means any incremental debt capacity is optionality (buybacks, M&A) rather than a need. A buyback announcement would be a disproportionately positive catalyst given zero repurchases in FY2023 and a dormant authorization.

6. **Deferred revenue +28% (noncurrent +97%) is the best hard evidence of forward demand in the filing.** $12.4B of FY2023 revenue came from the prior-year deferred balance. Sequentially rising noncurrent contract liabilities implies multi-year enterprise commitments — this is the number to track for the cloud/enterprise franchise, and it is not a management-provided KPI.

7. **Position sizing around Q4 seasonality.** With 86.5% of full-year FCF generated in Q4, TTM-FCF multiples compress sharply into and after a strong Q4 and expand mechanically in Q1/Q2. Expect multiple dislocation around the Q1 print that is seasonal, not fundamental.

8. **Per-share anchors to apply your own multiple** (no live price available in this dataset): diluted EPS **$2.90**, reported FCF/share **$3.07**, SBC-adjusted FCF/share **$0.78**, operating income/share **$3.51**, book asset value/share **$50.83** (total assets / 10,383M shares — *not* book equity). Diluted share count ~**10,491M** (derived from $30,425M net income / $2.90 diluted EPS).

9. **Directional stance:** Fundamentals support a **constructive / long-bias** view on operating income and cash generation, with the primary near-term risks being (a) a 2024 capex guide-up and (b) SBC/cash-tax drag on EPS. This is not a "cheap" setup on SBC-adjusted cash flow — it is a **quality-of-franchise** setup where margin durability, not revenue growth, is the variable that matters.

---

## 12. Explicit data gaps in this dataset

- **Insider transactions:** unavailable — no Form 4 archive (§9). Do not treat as neutral signal.
- **Revenue, segment revenue, and segment operating income:** no tagged rows returned; revenue derived arithmetically and cross-validated. Segment names inferred from the resolved company identity, not from the data (`NumberOfOperatingSegments = 3` is the only segment fact present).
- **No quarterly income statement for Q1–Q3 FY2023** (the cache holds 10-K facts plus 10-Q *cumulative cash-flow* facts only); Q4 figures in §5 are derived by subtraction.
- **PP&E net, inventory, stockholders' equity, retained earnings, total liabilities, and shares repurchased under authorization** — truncated from the fact set (all fall alphabetically after the last returned row), so ROE, inventory turns, and exact book equity could not be computed.
- **No price/quote/market-cap data** — all valuation multiples must be computed externally.

---

## 13. Key points summary

| Category | Metric | FY2021 | FY2022 | FY2023 | YoY '23 | Signal |
|---|---|---|---|---|---|---|
| **Scale** | Revenue (derived, $B) | 469.8 | 514.0 | **574.8** | +11.8% | 🟢 Re-accelerating |
| **Profitability** | Operating income ($B) | 24.9 | 12.2 | **36.9** | +200.9% | 🟢 3x trough |
| | Operating margin | 5.30% | 2.38% | **6.41%** | +403 bps | 🟢 Best in 3 yrs |
| | Gross margin | 42.03% | 43.80% | **46.98%** | +318 bps | 🟢 COGS +5.5% vs rev +11.8% |
| | Net income ($B) | 33.4 | (2.7) | **30.4** | nm | 🟢 Full recovery |
| | Diluted EPS ($) | 3.24 | (0.27) | **2.90** | nm | 🟡 Below 2021 |
| **Cash generation** | Operating cash flow ($B) | 46.3 | 46.8 | **84.9** | +81.7% | 🟢🟢 Step change |
| | Capex ($B) | 61.1 | 63.6 | **52.7** | –17.1% | 🟢 Discipline |
| | **Free cash flow ($B, derived)** | (14.7) | (16.9) | **+32.2** | +49.1 | 🟢🟢 The thesis |
| | FCF margin | (3.13%) | (3.29%) | **5.60%** | +889 bps | 🟢 |
| | Capex / revenue | 13.00% | 12.38% | **9.17%** | –321 bps | 🟢 |
| **Balance sheet** | Cash + securities ($B) | ~36 | ~125 | **144.3** | +15% | 🟢 |
| | Long-term debt ($B) | — | 67.2 | **58.3** | –$8.8B | 🟢 No new issuance |
| | Debt + leases ($B) | — | 151.9 | **146.1** | –$5.8B | 🟢 |
| | **Net debt incl. leases ($B, derived)** | — | ~27 | **~1.8** | –$25B | 🟢🟢 Near neutral |
| | Current ratio (derived) | — | ~0.92 | **~0.90** | flat | 🟡 Structural |
| | Total assets ($B) | 420.5 | 462.7 | **527.9** | +14.1% | 🟢 |
| **Cost discipline** | Marketing expense ($B) | 32.6 | 42.2 | **44.4** | +5.0% | 🟢 |
| | G&A ($B) | 8.8 | 11.9 | **11.8** | –0.6% | 🟢 |
| **Quality flags** | SBC ($B) | 12.8 | 19.6 | **24.0** | +22.4% | 🔴 Watch |
| | SBC / revenue | 2.72% | 3.82% | **4.18%** | +36 bps | 🔴 Rising |
| | Cash taxes paid ($B) | 3.7 | 6.0 | **11.2** | +85% | 🟠 Normalizing |
| | Effective book tax rate | 12.56% | (54.2%) | **18.96%** | — | 🟠 Rising |
| | AR growth vs. revenue | — | — | **+23.4% vs +11.8%** | — | 🟠 DSO 30.1→33.2 |
| | Deferred revenue ($B) | — | 16.1 | **20.6** | +28.0% | 🟢 Noncurrent +97% |
| **Returns to holders** | Buybacks | $0 | $6.0B | **$0** | — | 🟡 Dormant |
| | Dividends | $0 | $0 | **$0** | — | ⚪ None |
| | Share count (M) | 10,242 | 10,383 | **10,387** | +1.4% | 🟡 SBC dilution |
| **Insider activity** | Form 4 data | — | — | **UNAVAILABLE** | — | ⚪ No data — do not infer |
| **Derived per share** | Reported FCF/share | (1.40) | (1.61) | **$3.07** | — | 🟢 |
| | SBC-adj. FCF/share | ~(1.78) | ~(2.85) | **~$0.78** | — | 🟠 4x lower |
| | Operating income/share | 2.43 | 1.18 | **$3.51** | — | 🟢 |
| **Valuation** | Price / market cap | — | — | **NOT AVAILABLE** | — | ⚪ Public float $1.184T @ 6/30/23 |

**Bottom line:** AMZN's FY2023 10-K is the most fundamentally important filing in three years. It converts the bear case (negative FCF, capital furnace, no returns of capital) into a bull case (positive $32B FCF, margin expansion, ~net-debt-neutral) — **but** the improvement is levered to capex discipline and partly flattered by $24B of SBC and a still-elevated deferred-tax benefit. The highest-conviction signals are **operating margin (6.41%), OCF (+82%), capex/revenue (9.17%), and net debt (~$1.8B)**. The highest-conviction warnings are **SBC/revenue (4.18% and rising), cash taxes (+85%), and Q4 concentration (86.5% of FCF)**. Insider data is a genuine blind spot on this date and should be sourced separately before it enters any decision.