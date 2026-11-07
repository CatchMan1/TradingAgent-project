# AAPL — Fundamental Deep Dive (as of 2024-02-16)

## 1. Data Provenance, Coverage & Limitations

| Item | Status |
|---|---|
| Source | Point-in-time SEC facts (EDGAR-accepted on/before 2024-02-16), B-project cache |
| Latest filing incorporated | **10-Q for quarter ended 2023-12-30**, filed 2024-02-02 (accn 0000320193-24-000006) |
| Prior annual filing | **10-K for FY ended 2023-09-30**, filed 2023-11-03 (accn 0000320193-23-000106) |
| Financial statements retrieved | Income statement (Q + FY), balance sheet (Q + FY), cash flow (Q + FY) |
| **Insider transactions** | **DATA UNAVAILABLE** — the vendor has no authorized point-in-time insider archive for AAPL. No inference or fabrication is made below. |
| **Not returned by vendor** | Company profile/segment splits, current share price, valuation multiples, FY2021–FY2023 *annual revenue* line, guidance |

Because no price data was returned, **no P/E, EV/EBITDA, or yield calculations appear in this report.** Where a figure is *derived* (e.g., net income = pretax income − tax expense) it is flagged.

---

## 2. Company Identity & Business Context

Resolved identity: **Apple Inc. (AAPL)** — designer/manufacturer of iPhone, Mac, iPad, Wearables/Home/Accessories, and a large Services segment (App Store, iCloud, Music, advertising, AppleCare, payments). Revenue is heavily concentrated in iPhone and geographically concentrated in Greater China + Americas. The vendor did **not** return segment-level or geographic revenue tables, so the segment commentary below is limited to what the XBRL facts support (notably the foreign-vs-domestic pretax income split, which is a hard data point).

**Hard-data proxy for geographic mix:** of FY2023 pretax income of **$113.736B**, **$72.900B (64.1%)** was foreign-sourced. This is the single most important structural fact in the filing set — AAPL is a majority-foreign-earnings company, which drives both its low effective tax rate and its regulatory/FX sensitivity.

---

## 3. Q1 FY2024 Income Statement (quarter ended 2023-12-30) vs Q1 FY2023

| Line ($M) | Q1 FY24 | Q1 FY23 | Δ % |
|---|---:|---:|---:|
| Net sales | **119,575** | 117,154 | **+2.1%** |
| Cost of goods & services | 64,720 | 66,822 | −3.1% |
| **Gross profit** | **54,855** | 50,332 | **+9.0%** |
| R&D | 7,696 | 7,709 | −0.2% |
| SG&A | 6,786 | 6,607 | +2.7% |
| Total operating expenses | 14,482 | 14,316 | +1.2% |
| **Operating income** | **40,373** | 36,016 | **+12.1%** |
| Non-operating income/(expense) | (50) | (393) | improved $343M |
| **Pretax income** | **40,323** | 35,623 | **+13.2%** |
| Income tax expense | 6,407 | 5,625 | +13.9% |
| **Net income** | **33,916** | 29,998 | **+13.1%** |
| Diluted EPS | **$2.18** | $1.88 | **+16.0%** |
| Basic EPS | $2.19 | $1.89 | +15.9% |
| Diluted shares (derived) | ~15,558M | ~15,956M | **−2.5%** |
| SBC expense | 2,997 | 2,905 | +3.2% |
| Dividend declared/share | $0.24 | $0.23 | +4.3% |

### Margin structure — the core story
| Metric | Q1 FY24 | Q1 FY23 | Δ |
|---|---:|---:|---:|
| Gross margin | **45.87%** | 42.96% | **+291 bps** |
| Operating margin | **33.76%** | 30.74% | **+302 bps** |
| Net margin | **28.36%** | 25.61% | **+275 bps** |
| R&D as % of sales | 6.44% | 6.58% | −14 bps |
| SG&A as % of sales | 5.67% | 5.64% | +3 bps |
| Effective tax rate | 15.89% | 15.79% | +10 bps |

**Interpretation:** This is a *margin expansion* quarter, not a growth quarter. Revenue grew only 2.1%, but gross margin expanded 291 bps — COGS *fell* 3.1% in absolute dollars on higher revenue. That combination (flat-to-down unit COGS, up revenue) points to favorable mix (Services and/or higher-end hardware) plus commodity/logistics cost relief. **Operating leverage was extreme: +2.1% revenue produced +12.1% operating income.** Note that opex rose only 1.2% — R&D was actually cut 0.2% y/y in nominal dollars, which is unusual for AAPL and worth monitoring (it is the first line item you'd expect to see inflate if the AI/headset investment cycle were ramping).

**EPS grew 16.0% vs net income growth of 13.1%** — a 2.9-point uplift purely from the shrinking share count (diluted shares −2.5%). Traders should treat roughly 20-25% of EPS growth as financial engineering rather than operating.

---

## 4. Balance Sheet (2023-12-30 vs 2023-09-30)

| Line ($M) | 2023-12-30 | 2023-09-30 | Δ % |
|---|---:|---:|---:|
| Cash & cash equivalents | 40,760 | 29,965 | +36.0% |
| Marketable securities — current | 32,340 | 31,590 | +2.4% |
| Marketable securities — noncurrent | 99,475 | 100,544 | −1.1% |
| **Cash + marketable securities (ex-restricted)** | **172,575** | 162,099 | **+6.5%** |
| Restricted marketable securities | 13,900 | 13,800 | +0.7% |
| Accounts receivable | 23,194 | 29,508 | −21.4% |
| Nontrade receivables | 26,908 | 31,477 | −14.5% |
| Inventory | 6,511 | 6,331 | +2.8% |
| **Total current assets** | **143,692** | 143,566 | +0.1% |
| **Total assets** | **353,514** | 352,583 | +0.3% |
| Accounts payable | 58,146 | 62,611 | −7.1% |
| Commercial paper | 1,998 | 5,985 | **−66.6%** |
| Current portion of LT debt | 10,954 | 9,822 | +11.5% |
| **Total current liabilities** | **133,973** | 145,308 | −7.8% |
| Long-term debt (noncurrent) | 95,088 | 95,281 | −0.2% |
| **Total debt (CP + term debt)** | **107,998** | 111,085 | −2.8% |
| **Total liabilities** | **279,414** | 290,437 | −3.8% |
| **Shareholders' equity** | **74,100** | 62,146 | **+19.2%** |
| Deferred revenue (total / current) | 12,500 / 8,264 | 12,100 / 8,061 | +3.3% / +2.5% |
| Shares outstanding (M) | 15,460.2 | 15,550.1 | −0.6% |

### Derived liquidity & leverage
| Metric | 2023-12-30 | 2023-09-30 |
|---|---:|---:|
| **Net cash** (cash+securities − total debt) | **+64,577** | +51,014 |
| Net cash per share | **$4.18** | $3.28 |
| Current ratio | **1.073x** | 0.988x |
| Working capital | **+$9,719M** | −$1,742M |
| Total debt / equity | 1.46x | 1.79x |
| Equity / total assets | 21.0% | 17.6% |

**Interpretation:**
- **Net cash rebuilt by ~$13.6B in one quarter** (from $51.0B to $64.6B). The company is deleveraging *and* accumulating simultaneously.
- The current ratio crossed back above 1.0x for the first time in the observable window, driven by a **$4.5B payables drawdown and a $4.0B commercial-paper paydown** — i.e., Apple is voluntarily shortening its funding and paying suppliers faster. This is the balance-sheet signature of a cash-rich company, not a stressed one.
- **Equity jumped 19.2% sequentially** — an unusual outcome given ~$20B of buybacks normally *reduce* equity. The drivers are $33.9B of quarterly net income (less $20.1B buyback and $3.8B dividends) plus a $2.07B improvement in AOCI (see §7).
- **Maturity ladder is clean:** only $9.94B of term debt comes due in the next twelve months, $10.78B in year two, $12.27B in year three, against $172.6B of liquid securities. **There is no refinancing cliff and no liquidity risk in this capital structure.** Undiscounted operating-lease obligations total $13.8B.

---

## 5. Cash Flow & Capital Allocation (Q1 FY24 vs Q1 FY23)

| Line ($M) | Q1 FY24 | Q1 FY23 | Δ % |
|---|---:|---:|---:|
| **Operating cash flow** | **39,895** | 34,005 | **+17.3%** |
| Capex (PP&E) | 2,392 | 3,787 | −36.8% |
| **Free cash flow** | **37,503** | 30,218 | **+24.1%** |
| Investing cash flow | +1,927 | −1,445 | +$3,372M |
| Financing cash flow | (30,585) | (35,563) | −$4,978M outflow |
| Buybacks | 20,139 | 19,475 | +3.4% |
| Dividends paid | 3,825 | 3,768 | +1.5% |
| **Total shareholder return** | **23,964** | 23,243 | +3.1% |
| SBC tax withholding (net share settlement) | 2,591 | 2,316 | +11.9% |
| Cash taxes paid | **7,255** | 828 | **+776%** |
| Purchases of AFS securities | 9,780 | 5,153 | +89.8% |
| Maturities/calls of AFS securities | 13,046 | 7,127 | +83.1% |
| Commercial paper repayments (net) | (3,984) | (8,214) | −51.5% |
| **Net change in cash** | **+11,237** | −3,003 | — |

### Derived quality metrics
| Metric | Q1 FY24 | Q1 FY23 |
|---|---:|---:|
| FCF margin | **31.4%** | 25.8% |
| CFO / net income | **1.18x** | 1.13x |
| FCF / net income | **1.11x** | 1.01x |
| Shareholder return / FCF | **63.9%** | 76.9% |
| Capex / revenue | 2.0% | 3.2% |

**Interpretation — this is the strongest part of the print:**
1. **Cash taxes paid exploded from $0.83B to $7.26B (+$6.4B).** Despite that $6.4B cash headwind, operating cash flow still rose $5.9B. **Excluding the tax-timing swing, underlying operating cash generation improved by roughly $12B year over year.** Do not read the 17.3% CFO growth as the ceiling — the underlying number is better.
2. **Capex fell 36.8% to $2.39B** — the lowest in the observable record — pushing FCF growth to 24.1%, roughly double revenue growth. AAPL remains an extraordinarily asset-light business (2.0% of revenue).
3. **Buybacks re-accelerated.** FY2023 full-year repurchases *decelerated* to $77.6B from $89.4B in FY2022, then Q1 FY2024 accelerated to $20.1B (+3.4% y/y). Management is leaning back into the buyback.
4. **Net securities portfolio runoff reversed into accumulation** — $13.0B of maturities vs $9.8B of purchases, plus a $4.0B commercial-paper paydown. Cash is being *parked*, not deployed into M&A. Combined with $13.6B of net-cash build, this signals no large acquisition is imminent and supports continued large buybacks.
5. **Payout is conservative relative to capacity:** total shareholder return = 63.9% of quarterly FCF, and dividends alone are only **11.3% of net income** ($3,825M / $33,916M). There is substantial unused dividend capacity.

---

## 6. Multi-Year Financial History (FY2021–FY2023, fiscal years ended late September)

*Net income derived as pretax income − income tax expense (matches reported figures).*

| $M unless noted | FY2021 | FY2022 | FY2023 | FY21→FY22 | FY22→FY23 |
|---|---:|---:|---:|---:|---:|
| Gross profit | 152,836 | 170,782 | 169,148 | +11.7% | **−1.0%** |
| Pretax income | 109,207 | 119,103 | 113,736 | +9.1% | **−4.5%** |
| Income tax expense | 14,527 | 19,300 | 16,741 | +32.9% | −13.3% |
| Effective tax rate | 13.3% | 16.2% | **14.7%** | +290 bps | −150 bps |
| **Net income (derived)** | **94,680** | **99,803** | **96,995** | +5.4% | **−2.8%** |
| Diluted EPS | $5.61 | $6.11 | $6.13 | +8.9% | **+0.3%** |
| SBC expense | 7,906 | 9,038 | 10,833 | +14.3% | +19.9% |
| **Operating cash flow** | **104,038** | **122,151** | **110,543** | +17.4% | **−9.5%** |
| Capex | 11,085 | 10,708 | 10,959 | −3.4% | +2.3% |
| **Free cash flow** | **92,953** | **111,443** | **99,584** | +19.9% | **−10.6%** |
| Buybacks | 85,971 | 89,402 | 77,550 | +4.0% | **−13.3%** |
| Dividends | 14,467 | 14,841 | 15,025 | +2.6% | +1.2% |
| **Total capital returned** | **100,438** | **104,243** | **92,575** | +3.8% | −11.2% |
| Cap return / FCF | 108.1% | 93.5% | 93.0% | — | — |
| CFO / net income | 1.10x | 1.22x | **1.14x** | — | — |
| Investing cash flow | (14,545) | (22,354) | **+3,705** | — | swung positive |
| Financing cash flow | (93,353) | (110,749) | (108,488) | — | — |
| SBC / net income | 8.4% | 9.1% | **11.2%** | — | +210 bps |

### Securities-portfolio behavior (the "hidden" balance-sheet engine)
| $M | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Purchases of AFS debt securities | 109,558 | 76,923 | **29,513** |
| Maturities/prepayments/calls | 59,023 | 29,917 | 39,686 |
| Sales of AFS debt securities | 47,460 | 37,446 | 5,828 |
| Net securities (purchases) / proceeds | **(3,075)** | **(9,560)** | **+16,001** |
| Long-term debt issued | 20,393 | 5,465 | 5,228 |
| Long-term debt repaid | 8,750 | 9,543 | 11,151 |

**Interpretation:**
- **FY2023 was a genuine earnings down-year.** Gross profit fell 1.0%, pretax income fell 4.5%, net income fell 2.8% — yet **diluted EPS still rose 0.3%** because the share count fell. That is the clearest illustration of how much of AAPL's EPS trajectory depends on repurchases; strip out buybacks and FY2023 was negative EPS growth.
- **Q1 FY2024 decisively breaks that trend** (+9.0% gross profit, +13.1% net income, +16.0% EPS). The inflection is real in the data — but it is margin-driven on 2.1% revenue growth, so its durability depends on mix holding.
- **The buyback slowed 13.3% in FY2023** (fewer dollars because the average price was higher — dollar-for-dollar, higher prices buy fewer shares). Q1 FY2024 re-acceleration to $20.1B is a meaningful signal of intent.
- **SBC is quietly compounding:** $7.9B → $9.0B → $10.8B, now **11.2% of net income**. SBC grew 19.9% in a year when net income fell 2.8%. This is a real (if non-cash) dilution offset to the buyback, and it has been rising faster than revenue.
- **The securities portfolio flipped from a $9.6B net buyer in FY2022 to a $16.0B net seller in FY2023.** Apple stopped reinvesting maturities and let the book run off — a deliberate liquidity build of roughly $25.6B of swing versus the prior year, which is exactly what funds the FY2024 buyback re-acceleration.
- **Debt issuance collapsed** from $20.4B (FY21) to $5.2B (FY23) while repayments ran $11.2B — net debt reduction with no need for capital markets.

---

## 7. Other Comprehensive Income, Tax Detail & Items Traders Underrate

**AOCI / unrealized bond losses are healing:** AOCI improved from **−$11,452M (2023-09-30)** to **−$9,378M (2023-12-30)**, a +$2,074M improvement in one quarter. The breakdown in Q1 FY24:
- Unrealized gains on AFS securities arising in period: **+$3,045M**
- FX translation: **+$308M**
- Reclassification out of AOCI (sales): −$75M

**This matters:** Apple's equity book has been suppressed for two years by mark-to-market losses on a ~$100B+ bond portfolio. As those losses unwind (with falling market yields), reported equity rises *without any operating improvement*. This directly boosts book value per share and any valuation metric anchored on equity. It is a mechanical tailwind for FY2024 that is not in consensus EPS but is in book value.

**Tax watch items:**
- Foreign income tax expense fell from $12,072M (FY22) to $9,419M (FY23), while foreign pretax income *rose* ($71.3B → $72.9B). The foreign effective rate dropped from 16.9% to 12.9%.
- Federal tax expense rose $5,625M (FY22) → $5,801M (FY23) on *lower* US pretax income (US pretax = 119,103 − 71,300 = $47.8B in FY22 vs 113,736 − 72,900 = $40.8B in FY23) — i.e., **the US effective rate rose from ~11.8% to ~14.2%.** That is an adverse mix/regulatory trend worth flagging.
- Deferred tax asset valuation allowance grew $7,530M → $8,374M (+11.2%); gross DTAs grew $29,206M → $32,743M. Deferred tax liabilities $7,139M → $7,118M. Net DTA position **improved** $15,375M → $17,852M.
- **Risk:** the FY2024–FY2025 tax rate is the least predictable line in the model. The FY2023 rate of 14.7% is well below the 21% statutory rate and is dependent on foreign profit sourcing (64% of pretax) and R&D/foreign tax credits ($8.3B carryforwards, of which $3.0B research, $5.2B foreign). Any OECD Pillar Two or US international tax change hits EPS directly, with no operating offset.

**Non-operating swing:** Q1 FY24 other income/expense was only −$50M vs −$393M a year earlier. Rising interest income on a $172.6B securities book is now nearly fully offsetting ~$108B of debt service. At current rates this line should stay close to neutral-to-positive — a small but real EPS tailwind versus FY2023.

**Deferred revenue:** $12,100M → $12,500M (total), current portion $8,061M → $8,264M. Revenue recognized from prior deferred balances was $3,500M in Q1 FY24 vs $3,400M prior year. Modest but steady — consistent with a Services business whose backlog is growing slowly in dollar terms, not accelerating.

---

## 8. Insider Transactions

**UNAVAILABLE.** The vendor explicitly reports no authorized point-in-time insider-transactions archive for AAPL as of 2024-02-16. I have **not** inferred, estimated, or fabricated any insider buying or selling. Any insider-activity claim about AAPL in this window must come from a Form 4 primary source, which is outside the tools provided. Treat this as a genuine information gap rather than a signal.

---

## 9. Actionable Insights for Traders

**Bull case grounded in this data:**
1. **The margin inflection is the trade.** +291 bps of gross margin on 2.1% revenue growth, with COGS *down* 3.1% in dollars, drove +12.1% operating income and +16.0% EPS. If gross margin holds above ~45%, current EPS run-rate (~$8.72 annualized from $2.18) is defensible even on flat units.
2. **Cash generation is better than headline.** CFO +17.3% *despite* a $6.4B increase in cash taxes paid. Underlying operating cash improvement is roughly $12B y/y. FCF margin expanded 560 bps to 31.4% and FCF/net income is 1.11x — accrual quality is excellent.
3. **Net cash rebuilt $13.6B in a quarter to $64.6B ($4.18/share).** No maturity cliff (only $9.9B due in 12 months). Zero balance-sheet risk; total optionality for buybacks.
4. **Buyback re-acceleration confirmed:** FY2023 slowed to $77.6B (−13.3%), Q1 FY2024 rebounded to $20.1B (+3.4% y/y), and shares fell 0.6% in the quarter and a further 18.3M by 2024-01-19. Buybacks alone contribute ~3 points of EPS growth per year at this pace.
5. **AOCI healing (+$3.0B unrealized gains in the quarter) is a mechanical book-value tailwind** that consensus EPS models ignore.
6. **Dividend is trivially covered** — 11.3% of net income, $0.24/qtr (+4.3% y/y). Room to raise substantially if management chooses.

**Bear case grounded in this data:**
1. **Revenue growth is 2.1%. That is the whole story.** A margin-led beat on 2% top-line growth is low quality and mean-reverting if mix normalizes or input costs rebound.
2. **FY2023 was an outright down-year** (gross profit −1.0%, net income −2.8%). One quarter does not erase a full year of decline. The burden of proof is on Q2 FY2024 to show the margin level holds.
3. **R&D fell 0.2% y/y in nominal dollars** while SG&A rose 2.7%. For a company whose narrative depends on a new product cycle, flat R&D is a yellow flag — either efficiency or under-investment, and the data cannot distinguish.
4. **64% of pretax income is foreign, and the tax rate is the model's weakest link.** Foreign tax expense already fell $2.7B in FY23 (a rate benefit, not an operating one); the US effective rate *rose* from ~11.8% to ~14.2%. Global minimum-tax regimes are a direct EPS headwind with no operating offset.
5. **~20-25% of EPS growth is buyback math, not business improvement** (shares −2.5% vs EPS +16.0%). If the stock re-rates higher, dollar-for-dollar buybacks buy fewer shares and that contribution compresses — as it already did in FY2023 (−13.3% buyback dollars).
6. **SBC is compounding at 11.2% of net income and grew 19.9% in a down-earnings year** — a growing dilution offset that understates true compensation cost.
7. **Cash is being parked, not deployed** ($13.0B maturities vs $9.8B purchases; commercial paper cut 67%). No accretive M&A, no incremental growth investment — capital return is the entire strategy.

**Specific things to watch in the next print (Q2 FY2024):**
- **Gross margin ≥45%** — the single most important number. Sub-44% invalidates the Q1 inflection.
- **Revenue growth re-accelerating above ~4%** — needed to convert the margin story into a growth story.
- **Cash taxes normalizing** — Q1's $7.26B was abnormally high vs $0.83B; if it reverts, CFO growth will look even larger (and conversely, don't extrapolate the tax drag).
- **Buyback pace sustaining ≥$20B/quarter** — confirms the FY2023 slowdown was price-driven, not policy-driven.
- **R&D line** — a return to growth would signal a real product-cycle investment ramp.
- **AOCI continuing to improve** — a quiet book-value tailwind.

**Positioning read from the data alone:** This is a **high-quality, cash-compounding, deleveraging franchise currently delivering margin-driven rather than volume-driven earnings growth.** The balance sheet (net cash $64.6B, current ratio 1.07x, no maturity cliff) and cash conversion (FCF/net income 1.11x) make it a low-risk fundamental profile. The valuation question cannot be answered with the tools provided — no price data was returned — so any long/short sizing must be decided by the desk against live multiples.

---

## 10. Key Points Summary Table

| Category | Metric | Value | Read-through |
|---|---|---:|---|
| **Reporting** | Latest 10-Q period | Q ended 2023-12-30, filed 2024-02-02 | Point-in-time complete through 2024-02-16 |
| **Growth** | Q1 FY24 revenue | $119.575B (+2.1% y/y) | Growth is slow; the story is not top-line |
| **Growth** | Q1 FY24 operating income | $40.373B (+12.1% y/y) | Extreme operating leverage |
| **Growth** | Q1 FY24 net income | $33.916B (+13.1% y/y) | — |
| **Growth** | Q1 FY24 diluted EPS | $2.18 (+16.0% y/y) | ~2.9 pts from buybacks |
| **Margins** | Gross margin | 45.87% (+291 bps y/y) | ★ Core driver; must hold ≥45% |
| **Margins** | Operating margin | 33.76% (+302 bps y/y) | — |
| **Margins** | Net margin | 28.36% (+275 bps y/y) | — |
| **Costs** | COGS y/y | $64.720B (−3.1%) | COGS fell in dollars on higher revenue |
| **Costs** | R&D y/y | $7.696B (−0.2%) | Yellow flag: flat in nominal dollars |
| **Costs** | SBC / net income (FY23) | 11.2% (from 8.4% FY21) | Rising dilution offset |
| **Cash flow** | Q1 FY24 CFO | $39.895B (+17.3%) | Despite +$6.4B cash taxes paid |
| **Cash flow** | Q1 FY24 FCF | $37.503B (+24.1%) | FCF margin 31.4% (+560 bps) |
| **Cash flow** | CFO / net income | 1.18x | Excellent accrual quality |
| **Cash flow** | Cash taxes paid | $7.255B vs $0.828B y/y | One-off timing; do not extrapolate |
| **Capex** | Q1 FY24 capex | $2.392B (−36.8% y/y) | 2.0% of revenue — asset-light |
| **Balance sheet** | Cash + securities (ex-restricted) | $172.575B | +6.5% in the quarter |
| **Balance sheet** | Total debt (CP + term debt) | $107.998B | −2.8% in the quarter |
| **Balance sheet** | **Net cash** | **$64.577B ($4.18/share)** | +$13.6B in one quarter |
| **Balance sheet** | Current ratio | 1.073x (from 0.988x) | Crossed back above 1.0x |
| **Balance sheet** | Debt / equity | 1.46x (from 1.79x) | Deleveraging |
| **Balance sheet** | Equity | $74.100B (+19.2% q/q) | Net income + AOCI healing |
| **Balance sheet** | Debt due next 12 months | $9.943B | No refinancing cliff |
| **Deferred rev.** | Contract liability | $12.500B (from $12.100B) | +3.3% — steady, not accelerating |
| **Capital return** | Q1 FY24 buybacks | $20.139B (+3.4%) | Re-accelerated after FY23 −13.3% |
| **Capital return** | Q1 FY24 dividends | $3.825B; $0.24/sh (+4.3%) | Only 11.3% of net income |
| **Capital return** | Total return / FCF | 63.9% | Conservative vs history (~93-108%) |
| **FY2023** | Gross profit | $169.148B (−1.0%) | FY23 was a down-year |
| **FY2023** | Net income (derived) | $96.995B (−2.8%) | EPS +0.3% only via buybacks |
| **FY2023** | FCF | $99.584B (−10.6%) | Capital return was 93% of FCF |
| **FY2023** | Effective tax rate | 14.7% | Well below 21% statutory |
| **Geography** | Foreign / total pretax income (FY23) | 64.1% ($72.9B / $113.7B) | FX, tax & regulatory sensitivity |
| **AOCI** | Balance | −$9.378B (from −$11.452B) | +$3.045B AFS gains in Q1 — book value tailwind |
| **Insider** | Transactions | **UNAVAILABLE** | No data; not inferred |
| **Valuation** | Price / multiples | **NOT RETURNED** | Cannot compute P/E, EV/EBITDA, yield |