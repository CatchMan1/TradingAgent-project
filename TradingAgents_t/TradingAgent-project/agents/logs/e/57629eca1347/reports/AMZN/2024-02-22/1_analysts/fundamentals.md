# AMZN — Fundamental Research Report
**As-of date: 2024-02-22 | Primary source: FY2023 Form 10-K (accession 0001018724-24-000008), filed/accepted 2024-02-02 04:48 UTC; + Q3 FY2023 Form 10-Q (filed 2023-10-27)**

---

## 1. Important data-scope notes (read first)

- All figures below are **point-in-time SEC facts available on/before 2024-02-22**. The FY2023 10-K had been public for 20 days at the analysis date — this is the freshest possible audited dataset.
- **AMZN's insider-transaction archive was unavailable** for this date. No insider buying/selling is reported or inferred here. Do not treat the absence as a signal either way.
- The vendor tag set for AMZN does **not** include several standard tags (net sales, PP&E, goodwill, inventory, total stockholders' equity, segment detail). Where possible I **derived** missing items arithmetically and label them `[derived]`. Anything not derivable is explicitly flagged as "not in dataset" rather than estimated.
- **Revenue derivation check `[derived]`**: `CostsAndExpenses + OperatingIncomeLoss` reproduces reported net sales exactly for three straight years (2021: 444,943+24,879 = **469,822**; 2022: 501,735+12,248 = **513,983**; 2023: 537,933+36,852 = **574,785**). All margin math below is built on this reconciled base.

---

## 2. Company profile & reporting structure

Amazon.com, Inc. (AMZN) is a global technology and e-commerce conglomerate operating **3 reportable segments** (confirmed: `NumberOfOperatingSegments = 3`): North America, International, and Amazon Web Services (AWS). Revenue engines: online and physical stores, third-party seller services, advertising, subscription services (Prime), and AWS cloud/enterprise services.

Structural facts from the 10-K cover page and equity note:
- **Shares outstanding: 10,387,381,291** as of 2024-01-24 (post-year-end, most current count in dataset).
- Shares outstanding 12/31/23: **10,383M** (12/31/22: 10,242M) → **+1.4% YoY dilution**.
- Shares issued: 10,898M (12/31/23) vs 10,757M (12/31/22); authorized 100B; par $0.01.
- **Public float $1.184 trillion** as of 2023-06-30.
- Employees are not tagged, but `EmployeeRelatedLiabilitiesCurrent` held flat at **$7.70B** in both 2022 and 2023 — consistent with a stabilized (post-2022/23 layoff) headcount cost base.
- 1.6B shares reserved for future issuance → ~15% of the current share count, the structural source of ongoing dilution via SBC.

---

## 3. Income statement: the margin inflection is the story

### 3.1 Top line and gross margin `[revenue & gross profit derived]`

| $M | FY2021 | FY2022 | FY2023 | YoY '23 |
|---|---|---|---|---|
| Net sales `[derived]` | 469,822 | 513,983 | 574,785 | **+11.8%** |
| Cost of sales | 272,344 | 288,831 | 304,739 | +5.5% |
| Gross profit `[derived]` | 197,478 | 225,152 | **270,046** | +20.0% |
| **Gross margin** | 42.0% | 43.8% | **47.0%** | **+320 bp** |

Growth re-accelerated (9.5% → 11.8%) while cost of sales grew only 5.5%. Gross margin expanded **320 bp in one year and 500 bp in two years** — this is the single most important fundamental fact in the dataset. The mix shift toward higher-margin third-party services, advertising and AWS, plus regionalization of the fulfillment network and cost-to-serve discipline, is visible directly in the cost line.

### 3.2 Operating leverage

| $M | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Total costs & expenses | 444,943 | 501,735 | 537,933 |
| **Operating income** | **24,879** | **12,248** | **36,852** |
| **Operating margin** | 5.30% | 2.38% | **6.41%** |

Operating income **tripled off the 2022 trough (+201% YoY)** and is now 48% above the 2021 peak on 22% more revenue. FY2023 operating margin of 6.41% is the highest in company history.

Expense detail that *is* tagged (partial opex view):
- Marketing expense: 44,370 (+5.0% YoY) — marketing grew at **less than half** the rate of revenue.
- Advertising expense (a component): 20,300, **down 1.5% YoY** (20,600 in 2022) — first decline, evidence of cost discipline.
- G&A: 11,816, **down 0.6%** (11,891 in 2022).
- D&A: 48,663 (+16.1% vs capex **−17.2%**) → depreciation is now **outpacing** capex, mechanically supporting margins.
- Operating lease cost: 10,550 (+19.2%).
- Fulfillment / technology & content / "other" line items are **not in the dataset** — a genuine gap in opex granularity.

### 3.3 Below the line, taxes, and EPS

| $M | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Operating income | 24,879 | 12,248 | 36,852 |
| Interest expense | 1,809 | 2,367 | 3,182 |
| Investment income | 448 | 989 | **2,949** |
| Nonoperating income/(expense) | +13,272 | **−18,184** | +705 |
| Pretax income | 38,151 | −5,936 | 37,557 |
| Income tax | 4,791 | −3,217 | 7,120 |
| **Net income** | **33,364** | **−2,722** | **30,425** |
| Net margin | 7.10% | −0.53% | 5.29% |
| **Diluted EPS** | **$3.24** | **−$0.27** | **$2.90** |
| Basic EPS | $3.30 | −$0.27 | $2.95 |

Key reads:
1. **Earnings quality has structurally improved.** FY2021's $33.4B net income was inflated by $13.3B of non-operating gains (Rivian stake mark-up); FY2022's loss was driven by a **−$18.2B** non-operating swing (Rivian markdowns). FY2023's $30.4B is ~**97% operating-derived** (non-operating contribution only +$705M). This is the cleanest earnings base in years.
2. **Investment income nearly tripled to $2,949M**, almost fully offsetting the $3,182M interest expense → net interest cost collapsed to roughly **−$233M** from −$1,378M in 2022. The balance sheet is now essentially self-funding.
3. **Interest coverage (EBIT/interest) = 11.6x**, up from 5.2x in 2022.
4. **Tax is normalizing against AMZN**: effective rate 19.0% in 2023 vs a *benefit* in 2022. Cash taxes paid jumped to **$11,179M** from $6,035M — cash tax rate of ~29.8% of pretax income. Deferred tax expense was **−$5,876M**, i.e., book income is still running ahead of cash tax. Watch this: the 2021–22 deferred-tax tailwind (largely stock-comp and federal R&D capitalization) is shrinking.
5. **Foreign operations inflected**: pretax foreign income 5,229 (2023) vs 2,289 (2022) vs 2,272 (2021); domestic pretax 32,328 vs −8,225 vs 35,879. International profitability is a new, underappreciated profit pool (+128% YoY).

### 3.4 EBITDA `[derived]`

| $M | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Operating income | 24,879 | 12,248 | 36,852 |
| D&A | 34,433 | 41,921 | 48,663 |
| **EBITDA** | 59,312 | 54,169 | **85,515** |
| EBITDA margin | 12.6% | 10.5% | **14.9%** |

One-year EBITDA growth of **+57.9%**. Note SBC ($24,023M) sits inside this and is *not* added back here — if you treat SBC as a real cost (it is), EBITDA of $85.5B already reflects it.

---

## 4. Cash flow: the year FCF turned, and turned violently

### 4.1 Full-year picture

| $M | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| **Operating cash flow** | 46,327 | 46,752 | **84,946** |
| Capex (productive assets) | 61,053 | 63,645 | **52,729** |
| **Free cash flow `[derived]`** | **−14,726** | **−16,893** | **+32,217** |
| Finance-lease principal | 11,163 | 7,941 | 4,384 |
| **FCF after fin.-lease principal `[derived]`** | −25,889 | −24,834 | **+27,833** |
| Investing cash flow | −58,154 | −37,601 | −49,833 |
| Financing cash flow | +6,291 | +9,718 | **−15,879** |
| Net change in cash (incl. FX) | −5,900 | +17,776 | +19,637 |

Reads:
- **OCF +81.7% YoY** to $84.9B, an OCF margin of **14.8%** vs 9.1% in 2022. Cash generation, not accounting earnings, is where the re-rating case lives.
- **Capex cut 17.2%** to $52.7B — capex/sales fell to **9.2%** from 13.0% in 2021. Capex is now only **62% of OCF**, versus 137% in 2022. The 2021–22 buildout (logistics + AWS capacity) is being harvested, not extended.
- **FCF swing of +$49.1B in one year** ($−16.9B → +$32.2B). This is the first meaningfully positive FCF year since 2018-19 era dynamics.
- Precision on Q4 concentration `[derived from 10-Q 9M + 10-K FY]`: 9M-23 OCF was $42,481M and 9M capex $38,141M → 9M FCF of just **+$4,340M**. Therefore **Q4-23 alone contributed ~$42.5B OCF and ~$27.9B FCF (≈87% of the full-year FCF)**. Massive seasonality — do not annualize Q4 FCF naively, and do not extrapolate a single weak quarter from a Q1/Q2 print.

### 4.2 Capital allocation — a decisive shift to deleveraging

| $M | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| LT debt issued | 19,003 | 21,166 | **0** |
| LT debt repaid | 1,590 | 1,258 | 3,676 |
| ST debt proceeds | 7,956 | 41,553 | 18,129 |
| ST debt repaid | 7,753 | 37,554 | 25,677 |
| **Buybacks** | **0** | 6,000 | **0** |
| Marketable securities purchased | 60,157 | 2,565 | 1,488 |
| Proceeds from sales/maturities | 59,384 | 31,601 | 5,627 |

- **Zero long-term debt issued in FY2023** — the first year in decades without a benchmark bond deal. Net short-term borrowings fell ~$7.5B.
- **Buybacks paused** ($0 in 2023 after $6.0B in 2022). Capital is being directed at debt paydown and liquidity build, not shareholder returns. For a trader: **no buyback bid under the stock** in this window, and no dividend.
- The securities portfolio was largely *liquidated* through 2022 ($31.6B of sales/maturities vs $2.6B purchases) and is now minimal-flow ($5.6B out vs $1.5B in).

---

## 5. Balance sheet: fortress, not leverage

### 5.1 Liquidity and debt

| $M | 12/31/2022 | 12/31/2023 | Change |
|---|---|---|---|
| Cash & equivalents | 53,888 | **73,387** | +19,499 |
| Marketable securities (AFS, fair value) | not in dataset | **70,919** | — |
| **Cash + securities** | — | **~144,306** `[derived]` | — |
| Total cash (incl. restricted) | 54,253 | 73,890 | +19,637 |
| Long-term debt (carrying) | 67,150 | **58,314** | −8,836 |
| Finance lease liabilities | 15,783 | 12,109 | −3,674 |
| Operating lease liabilities | 69,040 | 75,639 | +6,599 |
| **Total debt + finance leases** | 82,933 | 70,423 | −12,510 |
| **Net cash (cash+sec. − debt − fin. leases)** `[derived]` | — | **≈ +73,883** | — |

- **Gross debt reduction of ~$12.5B** while cash grew ~$19.5B → ~$32B of net deleveraging in twelve months.
- **Net cash position ≈ $73.9B**, i.e., ~14% of total assets. Even counting all operating leases ($75.6B) as debt, the company is roughly **net-debt-neutral** — a remarkable place for a $575B-revenue, capex-heavy enterprise.
- **Leverage ratios `[derived]`**: Debt/EBITDA 0.68x (0.82x incl. finance leases; 1.71x incl. operating leases). Down from 1.53x on the same basis in 2022. This is investment-grade AA-style leverage on a company that still grows ~12%.
- Maturity ladder (12/31/23): 2024 $8,500M; 2025 $5,286M; 2026 $3,146M; 2027 $8,750M; 2028 $2,250M; thereafter $39,250M → **total principal ~$67,182M**. Only ~13% matures within 12 months and it is covered ~8.6x by the cash balance alone. **Refinancing risk is effectively nil**, which matters if rates stay elevated.
- AFS securities maturity profile: $65,159M within 1 year, $4,430M in 1–5 yrs, $394M in 5–10 yrs, $936M >10 yrs. Amortized cost $71,265M vs fair value $70,919M → a net unrealized **loss of only ~$346M** (down from the deep 2022 hole); AOCI improved from −$4,487M to −$3,040M.

### 5.2 Working capital, receivables, and forward demand

| $M | 12/31/2022 | 12/31/2023 | Change |
|---|---|---|---|
| Accounts receivable, net | 42,360 | 52,253 | +23.4% |
| Allowance for doubtful accounts | 1,400 | 1,700 | +21.4% |
| Write-offs | 1,300 | 1,600 | +23.1% |
| Accounts payable | 79,600 | 84,981 | +6.8% |
| Accrued expenses & other current | 62,566 | 64,709 | +3.4% |
| **Current liabilities `[derived]`** | **155,393** | **164,917** | +6.1% |
| Current assets | 146,791 | 172,351 | +17.4% |
| **Current ratio `[derived]`** | **0.94x** | **1.05x** | +0.11 |
| **Working capital `[derived]`** | **−8,602** | **+7,434** | +16,036 |
| Unearned revenue (contract liability), total | 16,100 | **20,600** | **+28.0%** |
| — current portion | 13,227 | 15,227 | +15.1% |
| — **non-current portion** | 2,900 | **5,700** | **+96.6%** |
| Refund liability | 1,300 | 1,400 | +7.7% |

Actionable reads:
- **Current ratio crossed above 1.0 for the first time in years (0.94x → 1.05x)**, and working capital flipped from a **−$8.6B deficit to +$7.4B**. The "negative working capital" model that worried investors through 2022 has been repaired.
- **AR grew 23.4%, roughly 2x revenue growth (11.8%)** — a genuine watch item. It likely reflects mix shift toward AWS/enterprise and advertising receivables (longer terms, higher quality) rather than collection stress, since doubtful-account allowance and write-offs grew in line with AR (write-offs still only 3.1% of gross AR). Monitor DSO: AR/revenue = 9.1% vs 8.2% in 2022.
- **Payables grew only 6.8% vs 11.8% revenue** — Amazon is *paying suppliers faster* (or at least not stretching them further). This is a cash *headwind* to OCF that was more than offset by profit growth; it also implies less vendor-financing reliance going forward.
- **Unearned revenue +28%, with the non-current portion nearly doubling (+97%)** — the strongest forward-looking demand signal in the dataset. Multi-year prepaid AWS commitments and Prime subscriptions are being booked. Contract-with-customer-liability revenue recognized in FY2023 was $12,400M.
- **Contractual obligations total $300,409M** (12/31/23), of which: op leases $90,777M, finance leases $14,106M, LT debt $67,182M → implied **purchase and other obligations of roughly $128B** (content, cloud capacity, energy, logistics). This is the largest off-balance-sheet-style claim on future cash and the key structural risk to the FCF story; the >5-year slice is $157,824M.

### 5.3 Asset base and intangibles

| $M | 12/31/2021 | 12/31/2022 | 12/31/2023 |
|---|---|---|---|
| Total assets | 420,549 | 462,675 | **527,854** |
| Current assets | — | 146,791 | 172,351 |
| Finite-lived intangibles, net | — | 4,950 | 6,540 |
| — gross / accum. amort. | — | 7,135 / 2,185 | 10,082 / 2,395 |
| Indefinite-lived intangibles (ex-goodwill) | — | 1,147 | 1,147 |
| Finance lease ROU, gross | — | 68,000 | 62,500 |
| — accumulated amortization | — | 45,200 | 44,700 |

- Total assets +14.1% YoY, entirely consistent with the profit/OCF build (no large M&A step-up).
- **PP&E and goodwill are not tagged in this dataset** — a real gap. Reported capex of $52.7B against $48.7B D&A implies the net PP&E base is roughly flat, which is itself an important inference: **the asset base stopped compounding while revenue grew 11.8%.**
- **Finance lease ROU gross fell from $68.0B to $62.5B and finance-lease principal payments collapsed from $11.2B (2021) → $7.9B (2022) → $4.4B (2023)**. Amazon is running off its finance-leased logistics/equipment book. Operating leases are taking its place (liability +9.6%, cash lease payments +21.0% to $10,453M) — a shift worth noting for anyone comparing EBITDA across years, since op-lease cost sits *above* the operating income line while finance-lease interest sits below it.
- Intangibles additions ($2.9B gross) plus an **$8.0B jump in deferred-tax assets for in-process R&D ($6,824M → $14,800M)** confirm meaningful acquisition/technology spend (healthcare, media content, AI licensing) that is *not* visible as goodwill in this tag set. Amortization of intangibles remains trivially small ($706M) and is scheduled at $715M/$631M/$563M/$552M/$534M for 2024–28, with $3,545M thereafter.

---

## 6. Equity, dilution, and shareholder economics

| $M | 12/31/2022 | 12/31/2023 | Change |
|---|---|---|---|
| Common stock ($0.01 par) | 108 | 109 | +1 |
| **Additional paid-in capital** | 75,066 | **99,025** | **+23,959** |
| AOCI | −4,487 | −3,040 | +1,447 |
| Shares outstanding | 10,242M | 10,383M | +141M |
| Shares issued | 10,757M | 10,898M | +141M |
| **SBC expense** | 19,621 | **24,023** | **+22.4%** |
| SBC tax benefit | 4,300 | 5,400 | +25.6% |
| Unrecognized SBC (not yet expensed) | — | **18,300** | — |

Critical observations:
- **APIC rose $23,959M, essentially equal to the $24,023M of SBC expense.** In plain terms, virtually all of AMZN's book-equity growth in 2023 came from issuing stock to employees, not from retaining earnings — a nuance that matters for anyone computing ROE or book value. (Total stockholders' equity is **not tagged** in this dataset, so ROE cannot be computed from tool data; do not quote one.)
- **SBC is 4.2% of revenue and 28.3% of operating cash flow**, and it is growing 22.4% — faster than revenue (11.8%). SBC is now equal to **79% of net income**. Any FCF-based valuation should deduct SBC or at minimum address it: adjusted for SBC, 2023 "true" FCF is closer to **~$8B on a post-SBC, post-finance-lease basis** (`32,217 − 24,023 = 8,194`), which is emphatically not the "FCF is fixed" headline. This is the single best bear counter-argument in the dataset.
- **Unrecognized SBC of $18.3B** is a pre-committed future expense (~9 months of current run-rate), so SBC will not decline quickly even if hiring freezes continue.
- Dilution remains modest at ~1.4%/yr and the basic-vs-diluted EPS gap is only 1.7%, so the per-share math is not badly distorted — but it is permanent, not temporary.

---

## 7. Derived profitability and quality metrics

| Metric `[all derived]` | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Gross margin | 42.0% | 43.8% | **47.0%** |
| Operating margin | 5.30% | 2.38% | **6.41%** |
| EBITDA margin | 12.6% | 10.5% | **14.9%** |
| Net margin | 7.10% | −0.53% | **5.29%** |
| OCF margin | 9.86% | 9.10% | **14.78%** |
| FCF margin | −3.13% | −3.29% | **+5.60%** |
| Capex / sales | 13.0% | 12.4% | **9.2%** |
| Capex / OCF | 131.8% | 136.1% | **62.1%** |
| D&A / capex | 0.56x | 0.66x | **0.92x** |
| ROA (net income / avg assets) | — | −0.62% | **6.14%** |
| Asset turnover (sales / avg assets) | — | 1.16x | **1.16x** |
| Interest coverage (EBIT/int.) | 13.8x | 5.2x | **11.6x** |
| SBC / revenue | 2.7% | 3.8% | **4.2%** |
| OCF / net income | 1.39x | n.m. | **2.79x** |
| FCF / net income | n.m. | n.m. | **1.06x** |

Interpretation: **asset turnover held flat at 1.16x while margins expanded ~400 bp** — meaning the entire profitability improvement is *margin-driven, not volume/leverage-driven*. That is the higher-quality kind of improvement, and it is also the kind most at risk if the company re-accelerates capex (e.g., for AI infrastructure). The D&A/capex ratio crossing toward 1.0x is the mechanism, and it reverses the moment capex inflects upward.

---

## 8. Illustrative valuation math (no price feed available)

I have no market-price tool, so treat this as a sensitivity framework rather than a quote. Using the **10,387,381,291 shares outstanding as of 2024-01-24** and 2023 fundamentals of $30,425M net income, $85,515M EBITDA, $32,217M FCF, and ~$73.9B net cash:

| Assumed share price | Market cap | EV | P/E (2023) | EV/EBITDA | P/FCF | P/FCF post-SBC |
|---|---|---|---|---|---|---|
| $150 | $1.56T | $1.49T | 51x | 17.4x | 48x | 190x |
| $170 | $1.77T | $1.69T | 58x | 19.8x | 55x | 217x |
| $190 | $1.97T | $1.90T | 65x | 22.2x | 61x | 240x |

**The valuation is not cheap on trailing numbers — it is a forward-margin bet.** The bull case requires FY2024 operating margin to keep climbing (retail cost-to-serve + AWS + advertising mix) and capex to stay near 9–10% of sales. The bear case is simply: SBC-adjusted FCF is ~$8B, capex re-accelerates for AI, and the multiple compresses.

---

## 9. Actionable conclusions for traders

**Bullish evidence (hard, from the filing):**
1. Operating income **+201% YoY** to $36,852M; operating margin at a **record 6.41%**, gross margin +320 bp to 47.0%.
2. **FCF swung +$49.1B in one year** to +$32,217M; OCF +81.7% to $84,946M; capex cut 17.2% to 9.2% of sales.
3. **~$32B of net deleveraging**: zero LT debt issued, gross debt + finance leases down $12.5B, cash +~$19.5B, **net cash ≈ $73.9B**. Debt/EBITDA 0.68x.
4. **Current ratio repaired** 0.94x → 1.05x; working capital −$8.6B → +$7.4B.
5. **Unearned revenue +28% overall, non-current +97%** — the best forward-demand indicator in the dataset.
6. **Earnings quality is now ~97% operating** (non-operating only +$705M), versus years distorted by Rivian mark-to-market.
7. Foreign pretax income **+128%**; international is finally a profit contributor.

**Bearish / risk evidence (equally hard):**
1. **SBC $24,023M (+22%), = 79% of net income and 28% of OCF, growing faster than revenue.** Post-SBC FCF ≈ $8.2B, not $32.2B. Unrecognized SBC of $18.3B locks this in.
2. **FY FCF is ~87% Q4** (~$27.9B of $32.2B) — extreme seasonality means Q1/Q2 prints will look weak and can shake out momentum holders.
3. **AR +23.4% vs revenue +11.8%** — monitor DSO; a second year of this would be a yellow flag.
4. **$300.4B of contractual obligations**, ~$128B of which is purchase/content/capacity commitments not on the balance sheet.
5. **Capex has room to re-accelerate** (AI/cloud build). D&A/capex at 0.92x is a peak-favorable ratio; a capex upturn compresses FCF mechanically and quickly.
6. **No buyback ($0 in 2023) and no dividend** — no capital-return floor under the equity.
7. Cash taxes rose to **$11,179M** and the effective rate normalized to 19.0%; deferred-tax benefits (−$5,876M) are shrinking, so future EPS growth must come from operations, not tax.
8. Cash paid to suppliers grew only 6.8% vs 11.8% revenue — the payables-financing tailwind is exhausted.

**What to monitor next (data-marked):**
- Q1 FY2024 capex and whether operating margin holds above ~6% (the 2023 base) — the entire FCF thesis rests on this pair.
- Non-current unearned revenue trend (the cleanest AWS/Prime backlog proxy in this dataset).
- SBC/revenue — a break below 4% would be a genuine quality upgrade.
- Any resumption of LT debt issuance or buybacks (signals a change in capital-allocation stance).
- AR/revenue ratio (9.1%); a move above ~10% warrants scrutiny.

**Bottom line:** AMZN's FY2023 10-K shows a company that converted a cost-discipline program into hard cash — record margins, a $49B FCF inflection, and a ~$74B net cash position — while simultaneously carrying structurally high SBC and a capex cycle that could restart at any time. The fundamental trajectory is clearly positive and the balance sheet is a fortress; the *valuation* at a ~19–20x EV/EBITDA and ~55x FCF (200x+ post-SBC FCF) leaves no room for a margin stumble. Position accordingly: the data supports a constructive fundamental stance but demands strict risk control around capex guidance and the Q1 seasonal FCF trough.

---

## 10. Key points summary

| Category | Metric | FY2021 | FY2022 | FY2023 | Read-through |
|---|---|---|---|---|---|
| Scale | Net sales `[derived]` ($M) | 469,822 | 513,983 | **574,785** | +11.8%, growth re-accelerated |
| Profitability | Gross margin `[derived]` | 42.0% | 43.8% | **47.0%** | +320 bp; mix + cost-to-serve win |
| Profitability | Operating income ($M) | 24,879 | 12,248 | **36,852** | +201% YoY; record 6.41% margin |
| Profitability | EBITDA ($M) `[derived]` | 59,312 | 54,169 | **85,515** | +57.9%; 14.9% margin |
| Earnings | Net income ($M) | 33,364 | −2,722 | **30,425** | 5.29% margin; ~97% operating-derived |
| Earnings | Diluted EPS | $3.24 | −$0.27 | **$2.90** | Clean recovery; 1.7% dilution drag |
| Cash | Operating cash flow ($M) | 46,327 | 46,752 | **84,946** | +81.7%; 14.8% OCF margin |
| Cash | Capex ($M) | 61,053 | 63,645 | **52,729** | −17.2%; 9.2% of sales vs 13.0% in '21 |
| Cash | **Free cash flow** ($M) `[derived]` | −14,726 | −16,893 | **+32,217** | **+$49.1B swing**; ~87% earned in Q4 |
| Cash | FCF post-SBC ($M) `[derived]` | n.m. | n.m. | **≈8,194** | Key bear data point |
| Balance sheet | Cash + securities ($M) `[derived]` | — | — | **~144,306** | 27.3% of total assets |
| Balance sheet | LT debt carrying ($M) | — | 67,150 | **58,314** | −$8.8B; **zero new LT issuance** |
| Balance sheet | Finance lease liab. ($M) | — | 15,783 | **12,109** | −23%; book running off |
| Balance sheet | Operating lease liab. ($M) | — | 69,040 | **75,639** | +9.6%; substituting for fin. leases |
| Balance sheet | Net cash ($M) `[derived]` | — | — | **≈+73,883** | Net-cash even incl. op leases ~neutral |
| Balance sheet | Debt/EBITDA `[derived]` | — | 1.53x | **0.68x** | Fortress balance sheet |
| Liquidity | Current ratio `[derived]` | — | 0.94x | **1.05x** | Crossed above 1.0; WC +$7.4B |
| Working cap. | Unearned revenue ($M) | — | 16,100 | **20,600** | +28%; non-current +97% = backlog |
| Working cap. | AR / revenue `[derived]` | — | 8.2% | **9.1%** | AR +23.4% > rev +11.8% — monitor |
| Compensation | SBC ($M) | 12,757 | 19,621 | **24,023** | 79% of net income; +22% YoY |
| Compensation | Unrecognized SBC ($M) | — | — | **18,300** | Locks in ~9 months of expense |
| Capital return | Buybacks ($M) | 0 | 6,000 | **0** | No floor under equity |
| Taxes | Effective tax rate `[derived]` | 12.6% | n.m. (benefit) | **19.0%** | Cash taxes $11.2B; tailwind fading |
| Commitments | Total contractual obligations ($M) | — | — | **300,409** | ~$128B beyond leases/debt |
| Shares | Shares out. (M) | — | 10,242 | **10,383** | +1.4%/yr dilution |
| Data gaps | Not in dataset | — | — | — | Insider transactions; net sales tag (derived); PP&E; goodwill; inventory; total equity; segment detail; fulfillment/tech opex |