# AMZN — Fundamental Research Report
**As of 2024-02-12 | Data basis: FY2023 Form 10-K (filed/accepted 2024-02-02, accn 0001018724-24-000008) plus prior-year comparative facts, all point-in-time filtered to be public by the trade date.**

---

## 1. Executive snapshot

AMZN (Amazon.com, Inc.) has just closed the books on a **transformational FY2023**: revenue re-accelerated, operating income roughly **tripled**, and operating cash flow **nearly doubled**, while capital intensity *fell*. The FY2023 10-K is the freshest fundamental catalyst available on 2024-02-12 (filed 2024-02-02), so the trade date sits in the immediate post-print window.

| Metric (FY, $M) | 2021 | 2022 | 2023 | 2023 YoY |
|---|---|---|---|---|
| Revenue (derived: total costs & expenses + operating income) | 469,822 | 513,983 | **574,785** | **+11.8%** |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| Operating income | 24,879 | 12,248 | **36,852** | **+200.9%** |
| Operating margin | 5.30% | 2.38% | **6.41%** | +403 bp |
| Pretax income | 38,151 | (5,936) | 37,557 | n.m. |
| Net income | 33,364 | (2,722) | **30,425** | n.m. |
| Diluted EPS ($) | 3.24 | (0.27) | **2.90** | n.m. |
| Operating cash flow | 46,327 | 46,752 | **84,946** | **+81.7%** |
| Capex (purchases of PP&E) | 61,053 | 63,645 | 52,729 | −17.2% |
| **Free cash flow** | **(14,726)** | **(16,893)** | **+32,217** | swing of +$49.1B |

*Revenue is not returned as a single line by the vendor feed (output truncated before the "Revenues" tag); it is reconstructed exactly as `CostsAndExpenses + OperatingIncomeLoss`, which reconciles to Amazon's reported $574.785B / $513.983B / $469.822B — a high-confidence derivation.*

---

## 2. Company profile & segment structure

- **Identity:** Amazon.com, Inc. — three reportable operating segments (confirmed by `NumberOfOperatingSegments = 3` in the FY2023 filing): **North America**, **International**, and **Amazon Web Services (AWS)**.
- **Business mix:** online and physical stores, third-party marketplace (1P/3P), Prime subscription, advertising (sponsored ads, retail media, Prime Video ads launched Jan-2024), AWS cloud (compute, storage, database, AI/ML including Trainium/Inferentia silicon and Bedrock), devices (Echo, Kindle, Fire), logistics (FBA, Amazon Air, trucking), plus "other bets" (Kuiper LEO satellites, Zoox, healthcare via One Medical, pharmacy).
- **Scale markers from the filing:** 10,383,812,291 shares outstanding as of 2024-01-24; **public float $1.184 trillion** at 2023-06-30; 100B shares authorized; 1.6B shares reserved for future issuance (equity comp capacity ~15% of shares outstanding).
- **Capital structure philosophy:** no dividend, minimal buybacks (see §6), reinvestment-led. FY2023 was Amazon's first year with **zero long-term debt issuance** ($0 proceeds) and **zero share repurchases** since 2021 — a deliberate deleveraging/cash-preservation posture as capex pivots to AI infrastructure.

---

## 3. Income statement analysis — the margin inflection is the story

**3.1 Revenue & cost structure**
Revenue grew **+9.4% in 2022** then **+11.8% in 2023**, i.e. re-acceleration of ~240 bp. Critically, total costs & expenses grew only **+7.2%** in 2023 vs +12.8% in 2022 — the operating leverage that drove the entire earnings beat.

FY2023 cost stack (from filing tags):

| Line | 2023 ($M) | % of revenue | 2022 ($M) | 2021 ($M) |
|---|---|---|---|---|
| Cost of goods & services sold | 304,739 | 53.0% | 288,831 | 272,344 |
| Fulfillment + tech/content + other (residual) | 116,708 | 20.3% | 101,607 | 82,551 |
| Marketing expense | 44,370 | 7.7% | 42,238 | 32,551 |
| — of which advertising (media) spend | 20,300 | 3.5% | 20,600 | 16,900 |
| G&A expense | 11,816 | 2.1% | 11,891 | 8,823 |
| **Total costs & expenses** | **537,933** | **93.6%** | 501,735 | 444,943 |

Notable: **marketing grew only +5.0% and G&A was flat to down (−0.6%)** — cost discipline, headcount rationalization, and fulfillment-network regionalization are visibly flowing through. Marketing spend is 7.7% of sales, the lowest ratio in three years (2021: 6.9%… 2022: 8.2%), suggesting the 2022 demand-shock spend is over.

**3.2 Two big non-operating swing factors (do not extrapolate blindly)**
- `NonoperatingIncomeExpense`: **+13,272 (2021) → −18,184 (2022) → +705 (2023)**. The 2022 hole was largely the Rivian/equity-securities mark: `EquitySecuritiesFvNiUnrealizedGainLoss` was **−13,600 in 2022 vs +11,600 in 2021 vs only +1,000 in 2023**. So 2021 EPS was flattered by ~$11.8B of paper gains, and 2022 was crushed by ~$12.7–13.6B of paper losses. **FY2023's $2.90 EPS is the first clean, "core" earnings number in three years** — that is an important quality-of-earnings upgrade.
- **Interest is now roughly a wash:** interest expense **3,182** (up from 2,367; +34%) is essentially offset by `InvestmentIncomeInterest` of **2,949** (up from 989; +198%) on the ~$144B liquidity pool. Net interest drag only ~$233M. `IncomeLossFromEquityMethodInvestments` trivial (−12M).

**3.3 Tax**
- Book tax expense **7,120** on pretax **37,557 = 19.0% effective rate** (2022: a −3,217 *benefit*; 2021: 4,791 / 12.6%).
- **Cash taxes paid 11,179** — 30.0% of pretax income, >90% above the book charge. Driver: `IncomeTaxesPaidNet` +85% YoY and a `DeferredIncomeTaxExpenseBenefit` of **−5,876** (deferred benefit). Related: `DeferredTaxAssetsInProcessResearchAndDevelopment` jumped from **6,824 → 14,800** (+$8.0B) — consistent with capitalized R&D under §174 tax rules creating a growing deferred asset / cash-tax drag. **Watch item:** rising cash taxes are a real FCF headwind for 2024–2025 even if book EPS keeps compounding.
- Tax credits recognized rose to **2,362** (from 1,006) — a modest ongoing support.
- Geographic split: domestic pretax **32,328**, foreign **5,229** — the international segment has finally turned structurally profitable, a key bull point.

**3.4 Segment/operating reads (structure confirmed, granular segment P&L not returned by feed)**
Three-segment structure with North America now solidly profitable, International at/near break-even, and AWS the profit engine. The +403 bp margin expansion with revenue +11.8% and total cost growth of only +7.2% is inconsistent with heavy promotional intensity — implying mix shift toward **higher-margin AWS, advertising, and 3P seller services/fulfillment fees**.

---

## 4. Balance sheet — fortress liquidity, retail-style negative working capital

| Balance sheet item ($M) | 2022-12-31 | 2023-12-31 | Δ |
|---|---|---|---|
| Cash & equivalents | 53,888 | **73,387** | +36.2% |
| Marketable (AFS) securities, fair value | — | **70,919** | — |
| **Total liquid assets** | ~ | **144,306** | — |
| Accounts receivable, net | 42,360 | 52,253 | **+23.4%** |
| Allowance for doubtful AR | 1,400 | 1,700 | +21.4% |
| Current assets | 146,791 | 172,351 | +17.4% |
| Total assets | 462,675 | **527,854** | +14.1% |
| Accounts payable | 79,600 | 84,981 | +6.8% |
| Accrued liabilities | 62,566 | 64,709 | +3.4% |
| Contract liabilities (deferred revenue), total | 16,100 | 20,600 | +28.0% |
| — current / noncurrent | 13,227 / 2,900 | 15,227 / 5,700 | +15.1% / +96.6% |
| Debt (carrying amount) | 67,150 | **58,314** | −13.2% |
| Finance lease liabilities | 15,783 | 12,109 | −23.3% |
| Operating lease liabilities | 69,040 | 75,639 | +9.6% |
| Additional paid-in capital | 75,066 | 99,025 | +31.9% |
| AOCI | (4,487) | (3,040) | improved |
| Shares outstanding (yr-end) | 10,242 | 10,383 | +1.4% |

**Key reads:**
1. **Net cash, not net debt.** Liquid assets of **$144.3B** vs debt of $58.3B + finance leases $12.1B = **$70.4B**, i.e. a **~$73.9B net cash position** before operating leases. Combined with 11.6x EBIT/interest coverage, credit risk is essentially a non-issue.
2. **Active deleveraging.** Debt −$8.8B, finance leases −$3.7B, and *zero* LT debt issued in 2023. That is a deliberate post-2022-rate-shock balance-sheet repair.
3. **Operating leases are the real "hidden" liability: $75.6B**, with $90.8B of undiscounted future payments ($11.2B due in 12 months, $44.6B beyond year five). `ContractualObligation` totals **$300.4B** (~57% of total assets): 39.3 / 30.9 / 25.7 / 28.4 / 18.3 / 157.8 ($M by year, next-12m through >5yr).
4. **AR growth (+23.4%) vastly outpaces revenue (+11.8%)** — consistent with the mix shift toward advertising and 3P/merchant receivables (faster payment cycles for sellers) and AWS enterprise billing. Bad-debt write-offs rose to $1.6B but remain trivially small (3.1% of AR gross) — no consumer credit deterioration signal.
5. **Deferred revenue +28%**, with noncurrent deferred revenue nearly doubling ($2.9B → $5.7B) — a forward-demand signal (Prime prepayments, AWS commitments); $12.4B of 2022 deferred revenue converted to 2023 revenue.
6. **Negative working capital is structural, not distress.** Current assets $172.4B vs identifiable current liabilities already ≥$184.5B (AP 84,981 + accrued 64,709 + employee 7,700 + op-lease current 8,419 + finance-lease current 2,032 + contract liab current 15,227 + refund liab 1,400), implying a **current ratio ≈ 0.9x**. This is supplier-financed retail working capital, backed by $144B of liquidity — the classic Amazon model.
7. **APIC +$24.0B (+32%)** mirrors SBC of $24.0B → dilution is *entirely* offset issuance-wise (shares +1.4% only because buybacks in prior years and issuance nets out). $18.3B of unrecognized SBC cost remains to be expensed — a persistent ~4% of revenue drag.
8. **Retained earnings and total stockholders' equity were not returned by the feed** (output truncation at "IntangibleAssetsGrossExcludingGoodwill"). For context, Amazon reported total stockholders' equity of **$201.9B at 2023-12-31** (vs $146.0B at 2022-12-31) in the same 10-K; I flag this as an external figure, not tool-verified, but it is consistent with assets $527.9B less liabilities ~$326.0B.

---

## 5. Cash flow — the single most important fundamental change

| Cash flow item ($M) | 2021 | 2022 | 2023 |
|---|---|---|---|
| Net income | 33,364 | (2,722) | 30,425 |
| D&A (incl. finance-lease ROU amortization) | 34,433 | 41,921 | 48,663 |
| — of which depreciation | 22,909 | 24,924 | 30,225 |
| Stock-based comp | 12,757 | 19,621 | 24,023 |
| **Operating cash flow** | 46,327 | 46,752 | **84,946** |
| Purchases of PP&E (capex) | (61,053) | (63,645) | (52,729) |
| **Free cash flow** | (14,726) | (16,893) | **+32,217** |
| Investing cash flow | (58,154) | (37,601) | (49,833) |
| Financing cash flow | +6,291 | +9,718 | **(15,879)** |
| FX effect on cash | (364) | (1,093) | +403 |
| Net change in cash | (5,900) | +17,776 | +19,637 |

**Decomposition of the $38.2B OCF jump:** D&A +$6.7B, SBC +$4.4B, net income +$33.1B (partly offset by working-capital drags). Working-capital items *worked against* cash in 2023: AR/other operating assets consumed **$8.3B**, accrued liabilities consumed **$2.4B**, other noncurrent assets consumed **$12.3B** (partly §174 capitalized R&D and content spend), while AP and deferred revenue contributed positively. **So the OCF surge is genuine earnings quality, not working-capital engineering** — arguably understating true cash generation.

- **Capex discipline:** capex fell 17.2% to $52.7B, dropping capex/sales from 12.4% → **9.2%**. This is the mechanical driver of the FCF swing; it cannot keep falling forever as AWS/AI infrastructure ramps (management guided to higher 2024 capex).
- **Financing turned negative for the first time:** repayments of ST debt $25,677, LT debt $3,676, finance-lease principal $4,384 vs proceeds of ST debt $18,129 and **$0 new LT debt**. Net −$15.9B.
- **Zero buybacks in 2023** (0 vs $6.0B in 2022, 0 in 2021) — capital is being recycled into PP&E/AI rather than returned.
- **Cash conversion:** OCF/net income **2.79x**; (D&A + SBC) = $72.7B = **86% of OCF** — non-cash add-backs dominate, so OCF quality hinges on the durability of SBC and the depreciating asset base, not on accounting windows.
- Finance-lease principal payments fell from $11.2B (2021) → $7.9B (2022) → $4.4B (2023) — logistics/real-estate lease build-out is maturing, freeing cash.

---

## 6. Returns, efficiency and quality ratios (computed)

| Ratio | 2021 | 2022 | 2023 | Comment |
|---|---|---|---|---|
| Gross margin proxy (1 − COGS/rev) | 42.0% | 43.8% | **47.0%** | +320 bp; services/ads/AWS mix |
| Operating margin | 5.30% | 2.38% | **6.41%** | 3-yr high |
| Net margin | 7.10% | −0.53% | 5.29% | 2021 inflated by Rivian gains |
| ROA (NI / avg assets) | 8.2% | −0.6% | **6.1%** | |
| Asset turnover | ~1.19x | ~1.16x | **1.16x** | stable |
| ROE (NI / avg equity, ext. equity) | ~24% | −1.8% | **~17.5%** | |
| Capex / sales | 13.0% | 12.4% | **9.2%** | key FCF lever |
| SBC / revenue | 2.72% | 3.82% | **4.18%** | creeping dilution cost |
| D&A / revenue | 7.33% | 8.16% | **8.47%** | heavy asset base |
| EBIT / interest expense | 13.8x | 5.2x | **11.6x** | comfortable |
| FCF / net income | n.m. | n.m. | **1.06x** | rare for AMZN |
| Cash taxes / pretax income | 9.7% | n.m. | **29.8%** | rising cash-tax drag |

---

## 7. Insider transactions

**DATA UNAVAILABLE.** The configured news/filing vendor has **no authorized, point-in-time insider-transactions archive for AMZN as of 2024-02-12**. Per data-integrity rules, no insider buying or selling activity has been inferred, estimated, or fabricated here. **Treat insider sentiment as an unresolved input** — do not read this omission as either bullish or bearish. If position sizing depends on insider behavior (e.g., post-10-K Form 4 clusters in early February), that must be sourced separately before the trade is executed.

---

## 8. Post-period earnings event (disclosure-timing note)

The FY2023 10-K was **accepted 2024-02-02 04:48 UTC**, i.e. two business days before the analysis date. The Q4-2023/FY2023 results release preceded it (late January/Feb 1). **The vendor feed here carries only annual and partial quarterly tags — it does not return a quarterly revenue series, segment P&L, or the Q4 line items.** Consequently:
- The FY2023 figures in this report are **tool-verified**.
- Any quarterly split (e.g., Q4-23 revenue ≈ $170B with ~14% growth, Q4 operating income ≈ $13B, AWS and advertising growth rates) is **from the company's earnings release, not from this dataset**, and should be treated as *secondary/corroborative* rather than audited. The direction is consistent with the 10-K: Q4 carried an outsized share of the full-year operating-income step-up given the H1-2023 comparison base.

**Trading implication:** the fundamental "surprise" is already public and digested. The trade is now about *sustainability of the 6.4% operating margin and the 2024 capex/AI trajectory*, not about the FY2023 print itself.

---

## 9. Risks (specific, filing-supported)

1. **Capex re-acceleration risk.** The +$49.1B FCF swing came from a 17% capex *cut*. AI/GPU/data-center buildout and Kuiper satellite launches require capex to rise again; a return to 12% capex/sales on $630B+ of 2024 revenue would consume ~$75B and **compress FCF by 50%+**. This is the single largest threat to the FCF narrative.
2. **Cash tax escalation.** Cash taxes already 30% of pretax vs 19% book rate, with a $14.8B §174 R&D deferred-tax asset. Tax normalization is a multi-year FCF headwind independent of operations.
3. **SBC dilution creep.** SBC/revenue up 146 bp in two years to 4.18%, with $18.3B unrecognized. GAAP earnings are ~$24B lower than cash earnings; if the stock re-rates lower, retention/comp pressure rises.
4. **Regulatory/legal.** FTC antitrust suit (filed Sept-2023), EU DMA gatekeeper obligations, and labor/organizing scrutiny — none yet quantified in the filing's reserves materially, so adverse outcomes are un-provisioned.
5. **Segment/geographic concentration of profit.** With only 3 segments and a 6.4% blended margin, a deceleration in the highest-margin segment (AWS/ads) hits consolidated operating income disproportionately given retail's thin margins.
6. **Equity-stake mark-to-market volatility.** The Rivian-style `EquitySecuritiesFvNi` swings (±$12–14B) mean GAAP EPS can mis-signal core trends in any given quarter.
7. **Lease/obligation overhang.** $300.4B contractual obligations ($157.8B beyond five years) is a fixed-cost commitment that reduces operating flexibility if demand softens.
8. **FX.** +$403M positive FX effect in 2023 vs −$1,093M in 2022; a stronger dollar would reverse this tailwind on International.

---

## 10. Actionable insights for traders

**Bull case (evidence-weighted, and the data supports this side):**
- **Margin regime change is confirmed, not narrative:** operating income +200.9% on +11.8% revenue with total expense growth of only +7.2%, gross margin +320 bp, marketing/G&A flat-to-down.
- **First clean earnings print in three years** — $2.90 diluted EPS is free of the ±$12B equity-mark distortions that defined 2021/2022. Multiple can be underwritten on core earnings.
- **FCF inflection is real and OCF-quality is high:** $32.2B FCF vs −$16.9B, and working capital *hurt* OCF in 2023 rather than flattering it.
- **Balance sheet is a call option:** ~$144B liquid vs ~$70B debt+finance leases → ~$74B net cash funds the AI capex cycle without external capital. Zero LT debt issued, zero buybacks = maximum internal funding capacity retained.
- **Forward-demand signals:** deferred revenue +28%, noncurrent deferred revenue +96.6% — committed customer spend rising faster than revenue.

**Bear/risk case:**
- The **easy FCF leverage (capex cuts) is spent.** 2024 capex must rise for AI; consensus FCF optimism may be too high.
- Cash tax rate (30%) already 1.6x the book rate and climbing.
- At roughly $174/share (market data, not from this tool set) on $2.90 FY2023 EPS, AMZN trades ~**60x trailing** — the multiple already discounts substantial margin expansion; the stock is a "prove-it-every-quarter" story.

**Concrete positioning ideas:**
1. **Own the margin story, hedge the capex story.** Long AMZN equity with a defined-risk overlay (e.g., put spread or collar) into the 2024 capex guidance cycle — the asymmetry is negative on capex surprises, positive on margin beats.
2. **Monitor these four line items each quarter as the trade's tripwires:** (a) `PaymentsToAcquireProductiveAssets` (capex) vs revenue, (b) `OperatingIncomeLoss` margin vs 6.41%, (c) `MarketingExpense`/revenue (stay ≤7.7% = discipline intact), (d) `IncomeTaxesPaidNet`/pretax (any jump above ~35% is an FCF negative).
3. **Watch AR growth vs revenue growth** (currently 52,253 vs revenue +11.8%, i.e. AR +23.4%). AR outrunning revenue by >10 pts for two consecutive quarters would flag receivables-quality/ad-mix risk.
4. **Relative-value angle:** with net cash ~$74B and 11.6x interest coverage, AMZN's credit is arguably mispriced vs its equity volatility — a long-credit/short-vol overlay is structurally supported by these fundamentals.
5. **Do not use FY2021 as a margin benchmark** (5.30% operating margin was pre-cost-reset). But note that FY2021's *net* margin (7.10%) was paper-inflated; **the honest comparison is FY2023 net margin 5.29% vs FY2022 −0.53%** — that is a ~580 bp improvement in one year on a $61B larger revenue base.
6. **Insider data is a blank.** Size the position on fundamentals only until Form 4 flow is independently sourced.

**Bottom line:** Fundamentally, AMZN on 2024-02-12 presents the strongest operating profile since 2021 — triple-digit operating-income growth, the first positive FCF in three years, a net-cash balance sheet, and self-funded AI capex capacity. The debate has shifted from *"can Amazon make money?"* to *"how much of the FCF will the AI capex cycle consume?"* The 10-K supports owning the name; the capex line determines the entry price.

---

## 11. Key points summary table

| Category | Metric / Fact | Value | Interpretation |
|---|---|---|---|
| **Filing** | Latest 10-K | Filed/accepted 2024-02-02 (accn 0001018724-24-000008) | Freshest catalyst; 8 days pre-analysis |
| **Identity** | Company / ticker | Amazon.com, Inc. — **AMZN** | 3 operating segments |
| **Revenue** | FY2023 (derived) | **$574.8B**, +11.8% | Re-acceleration from +9.4% in FY22 |
| Revenue | FY2022 / FY2021 | $514.0B / $469.8B | |
| **Profitability** | FY2023 operating income | **$36.85B**, +200.9% | Op margin 6.41% vs 2.38% |
| Profitability | FY2023 net income / diluted EPS | $30.4B / **$2.90** | First clean EPS in 3 yrs |
| Profitability | FY2022 net income / EPS | −$2.72B / −$0.27 | Rivian markdowns |
| **Margins** | Gross margin proxy | **47.0%** (+320 bp) | Ads/AWS/3P mix |
| Margins | SBC / revenue | 4.18% (+146 bp in 2 yrs) | Dilution drag |
| Margins | Effective book tax rate | 19.0% | vs cash tax 29.8% |
| **Cash flow** | Operating cash flow FY23 | **$84.9B**, +81.7% | |
| Cash flow | Capex FY23 | $52.7B, −17.2% (9.2% of sales) | Primary FCF lever |
| Cash flow | **Free cash flow FY23** | **+$32.2B** | vs −$16.9B FY22, −$14.7B FY21 |
| Cash flow | OCF / net income | 2.79x | D&A+SBC = 86% of OCF |
| **Balance sheet** | Cash + AFS securities | $73.4B + $70.9B = **$144.3B** | Net cash ~$74B |
| Balance sheet | Debt / finance leases | $58.3B / $12.1B (both down) | Deleveraging, $0 LT issuance |
| Balance sheet | Operating lease liabilities | $75.6B | Hidden fixed cost |
| Balance sheet | Contractual obligations | $300.4B (57% of assets) | $157.8B >5 yrs |
| Balance sheet | Total assets / current assets | $527.9B / $172.4B (+17.4%) | |
| Balance sheet | Accounts receivable | $52.3B, **+23.4%** | 2x revenue growth — monitor |
| Balance sheet | Deferred revenue | $20.6B, +28.0% (noncurrent +96.6%) | Forward-demand signal |
| Balance sheet | Current ratio | ~0.9x | Structural, supplier-financed |
| **Capital allocation** | FY23 buybacks / LT debt issued | **$0 / $0** | Retaining capacity for AI capex |
| Capital allocation | FY23 net financing flow | −$15.9B | First negative year |
| **Coverage** | EBIT / interest | 11.6x | Net interest ~−$233M only |
| **Shares** | Outstanding (2024-01-24) | 10,383.8M (+1.4% YoY) | Modest dilution |
| **Insider data** | AMZN insider transactions | **UNAVAILABLE — not fabricated** | Unresolved input; do not infer |
| **Valuation** | ~$174/share (external), ~60x FY23 EPS | | Priced for margin expansion |
| **Key risk** | 2024 capex re-acceleration | Return to ~12% of sales ⇒ FCF −50%+ | Chief downside driver |
| **Stance** | Fundamental bias | **Constructive / own with capex hedge** | Tripwires defined in §10 |