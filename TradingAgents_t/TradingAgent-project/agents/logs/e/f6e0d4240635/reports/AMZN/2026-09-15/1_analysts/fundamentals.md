# AMZN — Fundamental Deep Dive
**Analysis date:** 2026-09-15 · **Latest filing available:** Form 10-Q filed 2026-07-31 for the quarter ended **2026-06-30** · **Next reporting catalyst:** Q3 2026 results (period ends 2026-09-30, expected late October)

---

## 1. Executive summary

AMZN enters Q3 2026 in the most capital-intensive phase in its history, and the fundamentals are bifurcated:

- **The core business is accelerating, not slowing.** Derived Q2 2026 revenue of **$200.6B (+19.6% y/y)** is faster than Q1's **+16.6%**, with operating income up **+43% y/y** and operating margin expanding to **13.7%** from 11.4%. Core (ex-mark-to-market) EPS grew roughly **+29%**.
- **Reported earnings massively overstate run-rate profitability.** H1 2026 net income of **$92.9B** includes **$62.8B of pre-tax non-cash upward revaluations of non-marketable equity securities** (~$48B after tax, ~52% of net income). Reported diluted EPS of $8.53 is not a clean earnings base.
- **Free cash flow has turned negative.** TTM operating cash flow of **$161.4B** vs. TTM capex of **$173.0B** = **FCF of –$11.6B**, versus **+$13.5B** in the prior TTM period. H1 2026 capex was **25.8% of revenue** (vs. 17.7% a year ago).
- **The balance sheet has been re-levered to fund it.** Total debt (incl. finance leases) rose **+$65.0B (+80%) in six months** to **$145.7B**; interest expense more than doubled. Liquidity remains formidable at **$176.1B** (cash + marketable securities), leaving a still-net-cash position of roughly **–$30B**.
- **Off-balance-sheet commitments are the single biggest risk.** Total contractual obligations are **$650.0B**, with ~$78B due within twelve months — consistent with large multi-year AI/compute and content purchase commitments.

**Stance:** Fundamentally constructive on the operating franchise (re-acceleration + margin expansion is rare and valuable at this scale), but the equity is now a **"prove-the-AI-return" story**, not a cash-flow-compounding story. Reported EPS should not be capitalized; use core EPS (~$2.16 in Q2, ~$4.09 in H1) and monitor capex and private-investment marks.

---

## 2. Data basis, derivations and limitations (read before using numbers)

| Item | Status |
|---|---|
| Source | Point-in-time SEC facts, filtered by EDGAR acceptance time; all figures from 10-Q filed 2026-07-31 (accn 0001018724-26-000026) and 10-Q filed 2026-04-30 (accn 0001018724-26-000014) |
| **Revenue** | **Not present as a tagged fact in the extract.** Derived as `CostsAndExpenses + OperatingIncomeLoss` (arithmetically exact for Amazon's income statement) |
| Segment revenue/profit | Not provided; only `NumberOfOperatingSegments = 3` |
| Full-year history | No 10-K annual facts in the extract; only H1 (6-month) comparatives, quarterly points, and TTM (2025-07-01→2026-06-30) aggregates |
| Price / market cap / valuation multiples | **Not available** — no pricing feed. P/E, EV/EBITDA and FCF yield cannot be computed here |
| Insider transactions | **DATA_UNAVAILABLE** — no authorized point-in-time insider archive for AMZN. No insider activity is asserted in this report |
| Total liabilities / total equity / PP&E / goodwill | Not individually tagged in the extract; certain subtotals are estimated and flagged as such |

---

## 3. Company profile (as reflected in the filing)

Amazon.com, Inc. (**AMZN**) reports **three operating segments**: North America, International, and Amazon Web Services (AWS). Revenue streams embedded in the P&L include online and physical stores, third-party seller services, advertising, subscription services, and AWS cloud/compute. The balance sheet in this period reveals three strategically important, non-P&L features:

1. **Hyperscale infrastructure build-out** — capex of $173B TTM, heavy operating-lease footprint ($96.3B lease liability, $116.4B undiscounted payments).
2. **A large private-technology investment portfolio** — `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` of **$122.3B**, up from **$16.2B** at 2025-12-31.
3. **Convertible/warrant-linked instruments** — `FairValueAdjustmentOfWarrants` of –$1,051M in H1 2026 and –$1,449M in Q2 2026, indicating mark-to-market drag from warrant liabilities.

No dividend and no share repurchase tags exist in the period — capital allocation is entirely organic capex plus M&A.

---

## 4. Income statement: re-acceleration with real operating leverage

### 4.1 Quarterly reconstruction (USD millions)

| | Q2 2026 | Q2 2025 | Δ y/y | Q1 2026 (derived) | Q1 2025 (derived) | Δ y/y |
|---|---:|---:|---:|---:|---:|---:|
| **Revenue (derived)** | **200,606** | 167,702 | **+19.6%** | **181,519** | 155,667 | **+16.6%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 87,463 | 76,976 | +13.6% |
| Gross profit | 104,828 | 86,893 | +20.6% | 94,056 | 78,691 | +19.5% |
| Gross margin | **52.3%** | 51.8% | +45bp | 51.8% | 50.6% | +125bp |
| Marketing | 11,698 | 11,416 | +2.5% | 10,314 | 9,763 | +5.6% |
| G&A | 2,788 | 2,965 | –6.0% | 2,587 | 2,628 | –1.6% |
| Operating lease cost | 4,118 | 3,426 | +20.2% | 3,917 | 3,240 | +20.9% |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 157,667 | 137,262 | +14.9% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** | **23,852** | 18,405 | **+29.6%** |
| **Operating margin** | **13.7%** | 11.4% | **+230bp** | 13.1% | 11.8% | +130bp |
| Interest expense | (1,314) | (516) | +154.7% | (800) | (541) | +47.9% |
| Interest income | 1,295 | 1,085 | +19.4% | 1,135 | 1,066 | +6.5% |
| Equity-securities FV gains | 1,300 | 393 | +231% | (846) | (205) | n/m |
| **Non-operating income, net** | **53,396** | 1,686 | +3,066% | **15,982** | 3,274 | +388% |
| Pre-tax income | 80,857 | 20,857 | +287.7% | 39,834 | 21,679 | +83.7% |
| Tax | 18,199 | 2,678 | +579.6% | 9,560 | 4,553 | +110.0% |
| Effective tax rate | 22.5% | 12.8% | +970bp | 24.0% | 21.0% | +300bp |
| **Net income** | **62,647** | 18,164 | +244.9% | **30,255** | 17,127 | +76.7% |
| Diluted EPS | **$5.75** | $1.68 | +242% | $2.78 | $1.59 | +74.8% |

### 4.2 First-half aggregate

| | H1 2026 | H1 2025 | Δ |
|---|---:|---:|---:|
| Revenue (derived) | **382,125** | 323,369 | **+18.2%** |
| Cost of goods & services | 183,241 | 157,785 | +16.1% |
| Marketing | 22,012 | 21,179 | +3.9% |
| G&A | 5,375 | 5,593 | –3.9% |
| D&A (incl. finance-lease amortization) | 38,933 | 29,489 | +32.0% |
| Share-based compensation | 10,070 | 10,223 | **–1.5%** |
| Total costs & expenses | 330,812 | 285,793 | +15.8% |
| **Operating income** | **51,313** | 37,576 | **+36.6%** |
| Operating margin | **13.4%** | 11.6% | +180bp |
| Interest expense | 2,114 | 1,057 | +100.0% |
| Interest income | 2,430 | 2,151 | +13.0% |
| Non-operating income, net | 69,378 | 4,960 | +1,299% |
| Pre-tax income | 120,691 | 42,536 | +183.7% |
| Tax | 27,759 | 7,231 | — |
| Effective tax rate | **23.0%** | 17.0% | +600bp |
| **Net income** | **92,902** | 35,291 | +163.2% |
| Diluted EPS | **$8.53** | $3.27 | +160.9% |
| Diluted shares (implied) | ~10,891M | ~10,793M | +0.9% |

### 4.3 The critical adjustment — earnings quality

The entire gap between 13% operating margin and 31% net margin in Q2 is the private-equity mark-up.

| Component | H1 2026 | Q2 2026 | Q1 2026 |
|---|---:|---:|---:|
| Pre-tax upward price adjustment, non-marketable equity securities | 62,814 | 50,486 | 12,328 |
| After-tax at ~23% | ~48,367 | ~38,874 | ~9,493 |
| % of reported net income | **52.1%** | **62.1%** | **31.4%** |
| Reported diluted EPS | $8.53 | $5.75 | $2.78 |
| **Core (ex-mark) diluted EPS, est.** | **~$4.09** | **~$2.16** | **~$1.91** |
| Core EPS growth y/y | **~+25%** | **~+29%** | **~+20%** |

**Interpretation:** AMZN's underlying franchise grew core earnings roughly 25–29%, which is strong. But roughly **half of H1 reported net income is non-cash and non-distributable**, tied to the fair value of private AI-era equity stakes. This is a mark-to-model asset with reversal risk. Traders anchoring on a reported-EPS P/E will materially misprice the stock.

**Also note:** `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` rose from **$16.2B → $122.3B** in six months. Only $62.8B of that increase ran through income, implying ~$43B came from **new investments in-kind/convertibles, additions, or FX** — i.e., AMZN is aggressively expanding this exposure, not merely marking up an old stake.

---

## 5. Balance sheet: transformed in six months

| Item | 2026-06-30 | 2025-12-31 | Δ | Δ % |
|---|---:|---:|---:|---:|
| Cash & equivalents | 78,213 | 86,810 | –8,597 | –9.9% |
| Marketable (AFS) securities | 97,900 | 45,800 | +52,100 | +113.8% |
| **Cash + securities** | **176,113** | 132,610 | **+43,503** | **+32.8%** |
| Accounts receivable, net | 88,092 | 67,729 | +20,363 | +30.1% |
| Inventory, net | 38,184 | 38,325 | –141 | –0.4% |
| Current assets | 249,264 | 229,083 | +20,181 | +8.8% |
| Non-marketable equity securities | **122,300** | 16,200 | **+106,100** | **+655%** |
| Operating lease ROU asset | 92,743 | 86,054 | +6,689 | +7.8% |
| **Total assets** | **1,095,689** | 818,042 | **+277,647** | **+33.9%** |
| Accounts payable | 147,440 | 121,909 | +25,531 | +20.9% |
| Accrued liabilities | 73,406 | 75,520 | –2,114 | –2.8% |
| Current liabilities | 241,274 | 218,005 | +23,269 | +10.7% |
| Long-term debt, current | 3,330 | 2,748 | +582 | +21.2% |
| Long-term debt, noncurrent | 128,894 | 65,648 | +63,246 | +96.3% |
| Finance lease liabilities (total) | 13,451 | 12,286 | +1,165 | +9.5% |
| **Total debt incl. finance leases** | **145,675** | **80,682** | **+64,993** | **+80.5%** |
| Operating lease liabilities (total) | 96,320 | 89,252 | +7,068 | +7.9% |
| Contract liabilities (deferred revenue) | 24,878 | 24,976 | –98 | –0.4% |
| AOCI | 66,287 | 28,230 | +38,057 | +134.8% |
| Additional paid-in capital | 149,619 | 140,024 | +9,595 | +6.9% |
| Shares outstanding | 10,783M | 10,731M | +52M | +0.5% |

### Key observations

- **Total assets grew 34% in six months.** The binding constraint is no longer demand — it is capital deployment. The increase decomposes approximately into: private equity stakes **+$106.1B**, AFS securities **+$52.1B**, receivables **+$20.4B**, operating leases **+$6.7B**, cash **–$8.6B**, with the residual (~$100B, **estimated**) in net PP&E and acquisition-related intangibles/goodwill.
- **Net debt position:** 145.7 – 176.1 = **–$30.4B (net cash)** vs. **–$51.9B** at year-end. Still net cash, but the cushion **shrank by ~$21.5B** in six months, and that is *after* issuing $67B of debt.
- **Liquidity and current ratio:** 249.3 / 241.3 = **1.03x**. Thin. AMZN runs negative working capital by design; a 1.03x current ratio with $176B of liquidity is not a solvency concern, but it leaves no slack if receivables/payables terms tighten.
- **Working-capital efficiency is very strong:** revenue +18% while inventory is **flat**, and AP grew +21%. Inventory turns improved sharply — a genuine efficiency signal, not just accounting.
- **AOCI +$38.1B** is unexplained by FX (–$1.6B translation) and cannot be reconciled to the AFS portfolio (which shows only $7M unrealized gains / $67M losses at 6/30). **Flagged for verification in the 10-Q notes** — this suggests unrealized gains in an investment or hedging category not separately tagged in this extract.
- **Receivables quality:** allowance $2.8B on $88.1B AR = **3.2%** coverage, up from $2.4B/3.5% at year-end — consistent with mix shift toward advertising/AWS (higher-quality counterparties).

---

## 6. Cash flow: the central issue

### 6.1 TTM (2025-07-01 → 2026-06-30) vs. prior TTM (2024-07-01 → 2025-06-30)

| | TTM Jun-2026 | TTM Jun-2025 | Δ |
|---|---:|---:|---:|
| Operating cash flow | **161,403** | 121,137 | **+33.2%** |
| Capex (purchases of productive assets) | **(173,028)** | (107,656) | **+60.7%** |
| **Free cash flow (OCF – capex)** | **(11,625)** | **+13,481** | **–$25.1B swing** |
| Acquisitions, net of cash | (41,956) | (4,809) | +772% |
| Purchases of marketable securities | (72,902) | (46,731) | +56.0% |
| Sales/maturities of securities | 67,090 | 30,924 | +117.0% |
| D&A (add-back) | 75,200 | 58,562 | +28.4% |
| Net income | 135,281 | 70,623 | +91.5% |
| LT debt issued | 81,925 | 746 | n/m |
| LT debt repaid | (5,022) | (7,434) | –32.4% |
| ST debt, net | +1,643 | +286 | n/m |
| **Net financing cash flow** | **+75,160** | (8,652) | n/m |

### 6.2 Quarterly capex vs. operating cash flow

| | Q2 2026 | Q1 2026 | Q2 2025 | Q1 2025 |
|---|---:|---:|---:|---:|
| Operating cash flow | 45,387 | 26,032 | 32,515 | 17,015 |
| Capex | (54,208) | (44,203) | (32,183) | (25,019) |
| **Quarterly FCF** | **(8,821)** | **(18,171)** | **+332** | **(8,004)** |
| Capex / revenue | **27.0%** | 24.4% | 19.2% | 16.1% |
| OCF / revenue | 22.6% | 14.3% | 19.4% | 10.9% |

**Read-through:** capex intensity has risen **~1,000bp in two quarters**. Even with operating cash flow growing 33% TTM, the company is out-spending it. The funding mix is now explicit: **$82B of long-term debt issuance TTM, $67B in H1 2026 alone**, plus $42B of acquisitions. This is a deliberate balance-sheet-funded land-grab for AI capacity — bullish if the compute converts to AWS revenue, corrosive if it does not.

**Depreciation lag:** TTM D&A of $75.2B against $173.0B of capex implies a capex/D&A ratio of **2.3x**. As this PP&E is placed in service, depreciation will step up materially — a **mechanical margin headwind** of several billion dollars per year that is not yet visible in the 13.7% operating margin. H1 D&A already grew +32% vs. revenue +18%.

---

## 7. Capital structure, covenants and commitments

| Metric | Value | Comment |
|---|---:|---|
| Total debt incl. finance leases | $145.7B | +80.5% in 6 months |
| Cash + AFS securities | $176.1B | 1.2x gross debt |
| **Net debt / (net cash)** | **(30.4)B** | Net cash, but halved |
| Q2 annualized interest expense | ~$5.3B | +155% y/y; avg cost ~3.6% |
| Q2 EBIT / interest expense | **20.9x** | Ample coverage |
| Operating lease liabilities | $96.3B | Undiscounted $116.4B; 3.9% discount rate |
| Finance lease liabilities | $13.5B | Undiscounted $16.7B |
| **Total contractual obligations** | **$650.0B** | ~$78.1B due within 12 months; ~$42.8B remainder of FY2026 |
| Contract liabilities (deferred revenue) | $24.9B | Flat y/y; $15.2B recognized in H1 from opening balance |
| Cash taxes paid H1 2026 | $3,978 | vs. book tax $27,759 → **effective cash tax rate ~3.3% of pre-tax** |
| Deferred tax expense H1 2026 | $30,489 | Overwhelmingly from non-cash equity mark-ups |

**Two important points for traders:**

1. **Cash taxes are trivially low relative to book taxes** because the private-equity gains are unrealized and generate deferred tax. This flatters cash flow optics and will reverse on monetization.
2. **$650B of contractual obligations** — roughly 1.7x TTM revenue — is the largest single fixed-cost exposure in the company's history. If AI demand normalizes, this converts from operating leverage into operating drag. This is the number to watch in every subsequent 10-Q.

---

## 8. Insider transactions

**DATA_UNAVAILABLE.** The vendor's point-in-time package contains no authorized insider-transaction archive for AMZN as of 2026-09-15. No insider buying or selling is asserted, inferred, or fabricated in this report. Any signal in this dimension must be sourced independently (Forms 3/4/5 via EDGAR) and should be treated as unverified until then.

---

## 9. Actionable insights for traders

### Bullish evidence (high confidence)
1. **Revenue re-acceleration at scale:** +19.6% in Q2 vs. +16.6% in Q1 — a ~300bp sequential acceleration on a $200B quarterly base. This is the strongest single argument in the dataset.
2. **Genuine operating leverage:** operating income +43% y/y on revenue +19.6%; margin +230bp. Cost discipline is visible — marketing +2.5% and G&A **–6.0%** against +19.6% revenue; SBC actually **declined 1.5%** y/y (rare and bullish for per-share value).
3. **Core EPS +29%** — the franchise is compounding earnings at roughly 1.5x revenue growth even after stripping the marks.
4. **Working-capital efficiency:** flat inventory and +21% payables on +18% revenue implies improving turns and供应商 leverage.
5. **$176B liquidity and 21x interest coverage** — no refinancing orsolvency risk near term, even with $145.7B of debt.
6. **Optionality not in earnings:** $122.3B of private AI-era equity stakes is a large, under-appreciated asset base whose value is recognized only sporadically.

### Bearish evidence (high confidence)
1. **Negative TTM FCF (–$11.6B)** and a **–$25.1B swing** in twelve months. Capex is 27% of revenue and rising.
2. **Earnings quality:** ~52% of H1 net income is a non-cash private-mark gain. A 30% downward revision of that portfolio would erase roughly **$14.5B** of after-tax income — about **16% of H1 EPS**.
3. **Leverage inflection:** debt +80% in six months, interest expense +155% in Q2. Coverage is fine now; the *rate of change* is the warning.
4. **Depreciation cliff:** capex/D&A at 2.3x guarantees multi-year D&A growth well above revenue growth, compressing margins from here absent offsetting mix shift.
5. **$650B contractual obligations** create asymmetry — a demand air-pocket is now a P&L event, not just a growth disappointment.
6. **Effective tax rate normalization:** 23.0% H1 2026 vs. 17.0% H1 2025; a 600bp headwind that may persist.

### Positioning implications
- **Do not use reported EPS.** TTM reported EPS is roughly **$12.4–12.6**, of which ~**$4.45** is after-tax private-equity marks. TTM **core EPS ≈ $8.0**. Any multiple analysis must use core.
- **The stock is now a capex-ROI derivative.** The single highest-information variable for the next 2–4 quarters is **capex guidance and AWS growth**, not retail margin. A quarter where capex/revenue holds above ~25% while AWS growth decelerates would be the bear trigger; capex plateauing with AWS accelerating is the bull trigger.
- **Watch the gap between OCF growth (+33%) and capex growth (+61%).** Convergence of those two lines is the mathematical definition of the bull case reasserting itself.
- **Near-term event risk is concentrated at Q3 earnings (~late October).** Two specific items to check: (a) whether the non-marketable equity carrying value moves again (a *downward* adjustment would hit reported EPS hard), and (b) whether the AOCI increase of $38B is explained.
- **Asymmetry:** the operating franchise is demonstrably healthier than a year ago, but the equity's earnings base is lower-quality and its balance sheet less flexible. Long-bias requires tolerance for negative FCF; short-bias requires tolerance for +19% revenue growth and $176B of liquidity. Neither side has a clean, high-conviction edge from fundamentals alone.

### Risk register

| Risk | Trigger to monitor | Magnitude |
|---|---|---|
| AI capex over-build | Capex/revenue >27% with AWS deceleration; rising contractual obligations | High |
| Private-mark reversal | Downward fair-value adjustment line; carrying value >$122B | High |
| Depreciation step-up | D&A growth >30% y/y while margin flat | Medium-High |
| Leverage creep | Debt >$160B; interest expense >$6B annualized | Medium |
| Tax normalization | Effective rate sustained >23% | Medium |
| Working-capital reversal | Inventory or AR growth outpacing revenue | Medium |
| AOCI opacity | Unresolved $38B increase | Low-Medium (disclosure) |

---

## 10. Key metrics summary table

| Category | Metric | Latest | Prior / y/y | Interpretation |
|---|---|---|---:|---|
| **Growth** | Revenue, Q2 2026 (derived) | $200,606M | +19.6% y/y | Re-acceleration from Q1's +16.6% |
| | Revenue, H1 2026 (derived) | $382,125M | +18.2% y/y | Best growth in years at this scale |
| **Profitability** | Operating income, Q2 2026 | $27,461M | +43.2% y/y | Operating leverage is real |
| | Operating margin, Q2 2026 | 13.7% | +230bp y/y | Structural, not one-off |
| | Operating margin, H1 2026 | 13.4% | +180bp y/y | |
| | Gross margin, Q2 2026 | 52.3% | +45bp y/y | Modest mix benefit |
| | Net income, H1 2026 | $92,902M | +163.2% y/y | **52% from non-cash marks** |
| **Per share** | Diluted EPS, Q2 2026 (reported) | $5.75 | +242% y/y | Inflated by $50.5B mark |
| | **Core diluted EPS, Q2 2026 (est.)** | **~$2.16** | **~+29% y/y** | **True run-rate** |
| | Core diluted EPS, H1 2026 (est.) | ~$4.09 | ~+25% y/y | |
| | Diluted shares | ~10,891M | +0.9% y/y | Minimal dilution — bullish |
| | SBC, H1 2026 | $10,070M | –1.5% y/y | Declining as % of revenue |
| **Cash flow** | TTM operating cash flow | $161,403M | +33.2% | Strong |
| | TTM capex | $173,028M | +60.7% | The whole story |
| | **TTM free cash flow** | **–$11,625M** | vs. +$13,481M | **Negative** |
| | Q2 2026 capex / revenue | 27.0% | vs. 19.2% | Up ~780bp |
| | TTM D&A | $75,200M | +28.4% | Capex/D&A = 2.3x |
| **Balance sheet** | Total assets | $1,095,689M | +33.9% in 6 mo | Capital deployment |
| | Cash + marketable securities | $176,113M | +32.8% in 6 mo | Fortress liquidity |
| | Total debt incl. finance leases | $145,675M | +80.5% in 6 mo | Re-levered to fund AI |
| | Net cash / (debt) | $(30.4)B | was $(51.9)B | Cushion halved |
| | Current ratio | 1.03x | vs. 1.05x | Thin by design |
| | Inventory | $38,184M | –0.4% in 6 mo | Excellent turns |
| | Non-marketable equity securities | $122,300M | +655% in 6 mo | Hidden asset / mark risk |
| | AOCI | $66,287M | +$38,057M | **Unexplained by FX — verify** |
| | Contractual obligations | $650,034M | — | ~$78B due <12 mo |
| **Returns/capital** | Interest coverage (Q2) | 20.9x | from ~37x | Still strong; trending down |
| | Cash taxes / pre-tax income, H1 | ~3.3% | vs. 23.0% book | Deferred, will reverse |
| | Dividend / buyback | None | None | 100% reinvestment |
| **Insider** | Insider transactions | **Unavailable** | — | No inference made |

---

## 11. Bottom line

AMZN's **operating engine is unambiguously stronger than a year ago** — 19.6% revenue growth, 13.7% operating margin, +29% core EPS, minimal dilution, improving working capital. But the **financial statements are now dominated by two forces that are not operating earnings**: a $62.8B private-equity mark-up in H1 and a $65B debt-funded capex surge that has pushed TTM free cash flow to **–$11.6B**.

The trade is therefore not "is Amazon's business good" (it is) but **"is the market correctly pricing the duration and return on $173B of annual capex and a $122B private-AI equity book?"** Until the reported-to-core EPS gap closes and capex/revenue stabilizes, fundamental analysis supports a **constructive but valuation-dependent** view — one that must be paired with a price, which this dataset does not contain. Insiders: **no data available; no view expressed.**

*Prepared from SEC point-in-time facts accepted on or before 2026-09-15. Revenue, Q1 2026 line items, core EPS and certain balance-sheet residuals are derived/estimated and labeled as such.*