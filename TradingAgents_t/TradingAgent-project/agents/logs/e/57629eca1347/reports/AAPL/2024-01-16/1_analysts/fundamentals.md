# AAPL — Fundamental Research Report (point-in-time: 16 Jan 2024)

**Company:** Apple Inc. (AAPL)
**Data cut-off:** SEC filings accepted on or before 2024-01-16
**Latest complete financials:** FY2023 Form 10-K (fiscal year ended 2023-09-30, filed/accepted 2023-11-03, accession 0000320193-23-000106)
**Latest interim filings:** FY2023 Q1/Q2/Q3 10-Qs (last accepted 2023-08-04, period ended 2023-07-01)

> **Critical timing note for traders:** Apple's **December-quarter (FQ1 2024) 10-Q had not yet been filed as of 2024-01-16.** Every figure below is therefore as of 2023-09-30 at the latest. The next fundamental reset for AAPL is the FQ1'24 release (Apple's historical cadence puts this in the second half of January / first days of February). Do not treat the FY23 numbers as describing current-quarter momentum.

---

## 1. Data provenance and what is / isn't available

| Item | Status |
|---|---|
| FY2021–FY2023 full income statement, balance sheet, cash flow | ✅ Available (10-K) |
| FY2023 YTD interim cash flow (Q1, H1, 9M) | ✅ Available (10-Q), **cumulative not discrete** |
| Discrete quarterly revenue/earnings by quarter | ❌ Not tagged in this package |
| Product vs. Services split, geographic segment split | ❌ Not in this package |
| R&D vs. SG&A split within opex | ❌ Not tagged (only total opex) |
| Share price, market cap, consensus estimates, estimates revisions | ❌ No price/estimate data in toolset |
| Insider transactions | ❌ **DATA_UNAVAILABLE** — no authorized point-in-time insider archive for AAPL. No insider inference is made in this report. |

All ratios below are my calculations from the raw XBRL tags returned by the tools; company headline numbers are cross-checked for internal consistency (revenue = COGS + gross profit, assets = liabilities + equity, current-asset components sum to total current assets — all tie).

---

## 2. Company profile (as reflected in the FY2023 10-K structure)

Apple designs, manufactures and markets smartphones, personal computers, tablets, wearables and accessories, and sells a range of related services. The FY2023 filing shows the classic Apple financial architecture:

- **Extremely capital-light:** capex of only **$10.96B on $383.3B of revenue (2.9% of sales)**. PP&E net of accumulated depreciation is small relative to the balance sheet; the asset base is cash, receivables and marketable securities.
- **Negative working capital:** current assets $143.6B vs. current liabilities $145.3B → **working capital of –$1.74B**, current ratio **0.99**. This is a structural feature (supplier-funded inventory, deferred revenue), not distress — see §6.
- **Very large deferred-revenue/deferred-tax footprint:** total contract liabilities **$12.10B** ($8.06B current); deferred tax assets (net) **$24.37B**; unrecognized SBC **$18.6B**.
- **Shareholder-return machine:** cumulative FY21–FY23 buybacks **$246.9B** plus dividends **$44.4B** = **$291.3B** returned in three years.

---

## 3. Income statement — three-year history (FY ends late Sept)

| $M unless noted | FY2021 | FY2022 | FY2023 | FY23 YoY |
|---|---|---|---|---|
| Cost of goods & services sold | 212,981 | 223,546 | 214,137 | –4.2% |
| **Total net revenue** (derived) | **365,817** | **394,328** | **383,285** | **–2.8%** |
| **Gross profit** | **152,836** | **170,782** | **169,148** | –1.0% |
| Gross margin % | 41.78% | 43.32% | **44.13%** | +81 bp |
| Operating expenses | 43,887 | 51,345 | 54,847 | +6.8% |
| Opex % of revenue | 12.0% | 13.0% | 14.3% | +1.3 pp |
| **Operating income** | **108,949** | **119,437** | **114,301** | –4.3% |
| Operating margin % | 29.78% | 30.29% | 29.82% | –47 bp |
| Interest & dividend income | 2,843 | 2,825 | 3,750 | +32.7% |
| Interest expense | 2,645 | 2,931 | 3,933 | +34.2% |
| Non-operating income/(expense) | 258 | (334) | (565) | worse |
| Pre-tax income | 109,207 | 119,103 | 113,736 | –4.5% |
| Income tax expense | 14,527 | 19,300 | 16,741 | –13.3% |
| **Effective tax rate** | 13.3% | 16.2% | **14.7%** | –1.5 pp |
| **Net income** | **94,680** | **99,803** | **96,995** | –2.8% |
| Net margin % | 25.9% | 25.3% | 25.3% | flat |
| Diluted EPS | 5.61 | 6.11 | **6.13** | +0.3% |
| Basic EPS | 5.67 | 6.15 | 6.16 | +0.2% |
| SBC expense | 7,906 | 9,038 | 10,833 | +19.9% |
| Diluted share count (M) | ~16,880 | ~16,330 | **~15,824** | –3.1% |

### What the income statement is actually telling you

1. **Revenue is contracting but margins are expanding.** This is the single most important cross-current in the name. Gross margin rose 81 bp to **44.13%** on *falling* revenue — consistent with mix shifting toward higher-margin Services/software and away from hardware units. Operating margin held essentially flat (29.82%) despite opex growing 6.8% and opex intensity rising to 14.3% of sales.
2. **EPS growth is now entirely buyback-driven, not earnings-driven.** Net income fell 2.8% in FY23, yet diluted EPS *rose* 0.3% because the diluted share count fell ~3.1%. Trailing EPS quality is therefore highly dependent on the capital-return program continuing at scale.
3. **The 53-week distortion.** FY2023 spanned 2022-09-25 → 2023-09-30 = **371 days** vs. **364 days** in FY2022 (computable directly from the tag date ranges). The extra week, at roughly $7.2B/week of FY23 revenue, *flattered* FY23 revenue by roughly **1.9 pp**. On a per-week basis revenue fell **~4.6%** (FY23 $7,232M/wk vs. FY22 $7,583M/wk), i.e. the underlying decline is materially worse than the headline –2.8%. Adjust for this when framing "is the revenue decline stabilizing."
4. **Interest is now a two-sided, and roughly offsetting, swing factor.** Interest expense +34% (rising rates on ~$111B of debt) and investment income +33% (on ~$162B of cash/securities) nearly cancel; net non-operating was only –$565M on $113.7B pretax. Duration management, not P&L level, is the exposure.
5. **SBC is compounding faster than revenue or earnings** (+19.9% y/y, 2.8% of revenue, 9.5% of operating income). GAAP EPS is after this, but the $18.6B of unrecognized SBC is a future dilution/expense overhang that buybacks must absorb.

---

## 4. Balance sheet at 2023-09-30 (with FY22 comparison)

| $M | 2022-09-24 | 2023-09-30 | Change |
|---|---|---|---|
| Cash & cash equivalents | 23,646 | **29,965** | +6,319 |
| Marketable securities — current (derived) | 24,658 | **31,590** | +6,932 |
| Accounts receivable, net | 28,184 | **29,508** | +4.7% |
| Nontrade (vendor) receivables | 32,748 | **31,477** | –3.9% |
| Inventory, net | 4,946 | **6,331** | +28.0% |
| Other current assets | 21,223 | **14,695** | –30.8% |
| **Total current assets** | **135,405** | **143,566** | +6.0% |
| Marketable securities — non-current (AFS debt, FV) | n/a | **100,544** | — |
| PP&E + other noncurrent (incl. operating lease ROU 10,661) | 217,350 | **209,017** | –3.8% |
| **Total assets** | **352,755** | **352,583** | flat |
| Accounts payable | 64,115 | **62,611** | –2.3% |
| Commercial paper | 9,982 | **5,985** | –40.0% |
| Current portion of term debt | 11,128 | **9,822** | –11.7% |
| Other current liabilities | 54,293 | **50,010** | –7.9% |
| **Total current liabilities** | **153,982** | **145,308** | –5.6% |
| Long-term term debt | 98,959 | **95,281** | –3.7% |
| Other noncurrent liabilities | 49,142 | **49,848** | +1.4% |
| **Total liabilities** | **302,083** | **290,437** | –3.9% |
| **Shareholders' equity** (derived) | **50,672** | **62,146** | +22.6% |

### Key balance-sheet readings

- **Net cash position: ~$51.0B.** Total cash + marketable securities = 29,965 + 31,590 + 100,544 = **$162,099M**; total debt = 5,985 + 9,822 + 95,281 = **$111,088M** → **net cash $51,011M**. Debt fell **$8,981M** y/y while the securities book barely moved — i.e. FY23's FCF surplus went to buybacks/dividends, not to deleveraging for its own sake.
- **Liquidity is thin on a current-ratio basis but backed by $161B of liquid assets.** Current ratio 0.99, quick ratio **0.945**, working capital **–$1.74B**. Watch this: it means Apple's *operating* liquidity buffer is small, and it funds itself via the securities portfolio (of which only $31.6B is current). Any scenario where buybacks are funded from cash while securities are locked in the >1yr bucket would be a real funding-cost signal.
- **Inventory +28% y/y to $6.33B** while revenue fell 2.8%. In dollar terms small ($1.4B), but it is the only line in the pack pointing to channel/ demand softness. Inventory turns still very high at **33.8×** (COGS/inventory), inventory days **10.8**.
- **Equity rebuilt +22.6%** to $62.1B because net income ($97.0B) exceeded total capital returned ($92.6B) for the first time in years — the buyback no longer fully retires earnings. That is a subtle positive: book equity is no longer being consumed.
- **Debt maturity ladder is comfortable:** $9.94B due in 12 months, then $10.78B / $12.27B / $9.79B / $7.80B, with **$56.0B beyond year five** — refinancing is heavily back-ended. Operating leases $13.84B undiscounted; finance leases only $1.43B.

---

## 5. Cash flow and capital returns

| $M | FY2021 | FY2022 | FY2023 | FY23 YoY |
|---|---|---|---|---|
| **Cash from operations** | 104,038 | 122,151 | **110,543** | –9.5% |
| Capex (PP&E) | (11,085) | (10,708) | **(10,959)** | +2.3% |
| **Free cash flow** (derived) | **92,953** | **111,443** | **99,584** | **–10.6%** |
| FCF margin | 25.4% | 28.3% | **26.0%** | –2.3 pp |
| FCF / net income | 98.2% | 111.7% | **102.7%** | — |
| D&A | 11,284 | 11,104 | 11,519 | +3.7% |
| SBC (non-cash add-back) | 7,906 | 9,038 | 10,833 | +19.9% |
| Net investing cash flow | (14,545) | (22,354) | **+3,705** | swung positive |
| Net financing cash flow | (93,353) | (110,749) | **(108,488)** | — |
| **Buybacks** | 85,971 | 89,402 | **77,550** | –13.2% |
| Dividends paid | 14,467 | 14,841 | **15,025** | +1.2% |
| **Total returned** | **100,438** | **104,243** | **92,575** | –11.2% |
| Total returned / FCF | 108.1% | 93.5% | **93.0%** | — |
| DPS declared | 0.85 | 0.90 | **0.94** | +4.4% |
| Cash taxes paid | 25,385 | 19,573 | **18,679** | –4.6% |
| Net change in cash | (3,860) | (10,952) | **+5,760** | — |

### Cash-flow quality and capital-allocation read

- **FCF conversion is exemplary: 102.7% of net income in FY23 (111.7% in FY22).** There is essentially no accrual-quality red flag in the cash-flow statement — earnings are cash earnings, and cash taxes paid ($18.7B) were actually *above* the tax charge ($16.7B).
- **But FCF fell 10.6% y/y and CFO fell 9.5%** — a faster decline than net income (–2.8%). Drivers visible in the tags: receivables absorbed cash (+$1.69B AR use, plus other operating assets +$5.68B), and the operating-liability tailwind shrank from +$6.11B to +$3.03B. Working capital stopped being a source of cash.
- **Buybacks were cut 13.2% to $77.6B** — still enormous (20% of revenue, 78% of FCF), but the *rate of increase* in repurchases has clearly peaked (FY21 $86.0B → FY22 $89.4B → FY23 $77.6B). Since EPS growth is now buyback-dependent, this deceleration matters for the EPS trajectory more than for the cash-flow statement.
- **Total payout at 93% of FCF** is the sustainable ceiling. There is no dividend-increase risk (payout is ~15.5% of FCF), but there is also no room to *increase* the combined return without either higher FCF or drawing on the $51B net cash.
- **Investing flipped positive (+$3.71B)** purely from securities maturity management (proceeds from maturities $39.7B vs. purchases $29.5B and sales $5.8B) — a portfolio roll-down, not an asset sale.

### FY2023 interim (10-Q) trend — the cadence *inside* the year

| $M (cumulative) | 9M FY2022 | 9M FY2023 | Change |
|---|---|---|---|
| CFO | 98,024 | 88,945 | –9.3% |
| Investing CF | (21,137) | +1,311 | swung |
| Financing CF | (83,955) | (85,335) | –1.6% |
| Buybacks | 64,974 | 56,547 | –13.0% |
| Dividends | 11,138 | 11,267 | +1.2% |
| Capex | 7,419 | 8,796 | +18.6% |

| Q1-only (Oct–Dec) | FQ1 2022 | FQ1 2023 |
|---|---|---|
| CFO | 46,966 | **34,005 (–27.6%)** |

FQ1 FY23 was a **very weak cash quarter** (–27.6% CFO) that subsequently normalized; capex is running +18.6% ahead, which is worth watching as a possible early signal of AI/datacenter-related or retail investment. FQ1 FY24 (the Dec-2023 quarter) is the missing data point that would confirm or refute the stabilization thesis.

---

## 6. Efficiency, leverage and working-capital diagnostics (derived)

| Metric | FY2023 | Comment |
|---|---|---|
| ROE (avg equity) | **~172%** | Flattered by a thin equity base; not a capital-efficiency signal in isolation |
| ROA | **27.5%** | Genuinely exceptional on a $352.6B asset base |
| EBITDA (derived) | **$125.8B** | Op income 114.3 + D&A 11.5 |
| Net debt / EBITDA | **negative ~0.41× (net cash)** | $51.0B net cash |
| Total debt / equity | 1.79× | Gross; net cash |
| Interest coverage (EBIT/int. exp.) | **29.1×** | No solvency concern |
| Inventory days | 10.8 | Up from ~8.1 in FY22 |
| DSO (AR + vendor receivables) | **58.1 days** | 53.1 in FY22 |
| DPO | **106.7 days** | 104.7 in FY22 |
| **Cash conversion cycle** | **≈ –37.8 days** | Supplier-funded; negative CCC is structural |

The **–38 day cash conversion cycle** is the mechanism behind the sub-1.0 current ratio and the huge FCF: Apple collects from customers and its vendor receivables in ~58 days while paying suppliers in ~107 days. This is a durable competitive advantage, but it also means the current ratio is a *misleading* liquidity metric — the correct liquidity frame is $162B of cash and securities against $111B of debt.

---

## 7. Tax and contingent items (often the surprise factor for AAPL)

- **FY23 ETR 14.7%** (FY22 16.2%). The bridge: 21% statutory on $113.7B pretax = $23.9B, less a **–$5.74B foreign rate differential**, less –$1.12B excess SBC benefit, less –$1.21B R&D credits, plus $1.12B state/local — landing at $16.74B.
- **64.1% of pretax income was foreign** ($72.9B of $113.7B) — the ETR is structurally dependent on non-US taxation and on the FDII benefit, which was **$0 in FY23** (down from $296M in FY22 and $1.37B in FY21). Removing the FDII cushion is a slow upward pressure on the rate.
- **Tax contingency to flag:** the 10-K discloses **$4.5B of unrecognized tax benefits that could be settled/reduced within 12 months** — a plausible discrete charge/ cash-tax event. Deferred-tax valuation allowance also rose to $8.37B (from $7.53B).
- **Deferred revenue** grew again in absolute recognition terms ($8.2B of prior deferred revenue recognized in FY23 vs. $7.5B in FY22), while the total contract-liability balance slipped to $12.10B from $12.40B. Modest, but directionally a mild negative for Services backlog.

---

## 8. Fundamental synthesis — the bull case and the bear case, from the data

**Supportive of the stock (evidence-based):**
1. Gross margin **expanded 81 bp on declining revenue** → mix is improving, pricing power intact. (FY21 41.8% → FY22 43.3% → FY23 44.1%.)
2. **FCF of $99.6B** at a 26% margin, 103% conversion of net income — cash generation is intact and high-quality; no accrual games visible.
3. **$51B net cash** and a back-ended maturity ladder ($56B due after FY2028) → essentially zero refinancing risk, and the capacity to *keep* returning ~$90–100B/yr without leverage.
4. **Negative 38-day cash conversion cycle** and 27.5% ROA — the business model remains structurally superior.
5. Equity rebuilt 22.6% to $62.1B; net income now exceeds total capital returned — a genuinely healthier balance sheet than a year ago.

**Against the stock (evidence-based):**
1. **Revenue –2.8%, and roughly –4.6% underlying** once the 53rd week is stripped out. This is a decelerating top line.
2. **Net income –2.8%, operating income –4.3%; EPS growth (+0.3%) exists only because of a 3.1% smaller share count** — and buybacks were *cut 13.2%* in FY23.
3. **Opex intensity up 1.3 pp to 14.3%** and SBC up 19.9% — the cost base is growing faster than revenue, and the 29.8% operating margin is now being defended, not expanded.
4. **Working capital has flipped from a cash source to a cash use** (CFO –9.5% vs. net income –2.8%); inventory +28%.
5. **Payout already at 93% of FCF** — the capital-return lever that has been supporting EPS is close to its limit absent FCF re-acceleration.
6. **$4.5B unrecognized tax benefit** exposure within 12 months and a zeroed FDII benefit → ETR drift risk upward from 14.7%.
7. Current ratio 0.99 / working capital –$1.7B: little room for operating missteps without tapping the securities book.

**Net:** the FY23 data describes a **high-quality, cash-rich, margin-resilient but top-line-contracting** business whose per-share growth is now dependent on capital return. The setup is "quality defensive with an EPS-growth air pocket," not "growth compounder." The entire near-term fundamental debate hinges on the FQ1'24 (Dec-2023 quarter) print, which is **not yet in the data** — a trader taking a position as of 2024-01-16 is explicitly trading into that event blind on fundamentals.

---

## 9. Specific, actionable insights

1. **Treat FY23 revenue as ~–4.6%, not –2.8%.** If you are building a growth model off the 10-K headline, you are ~2 pp too optimistic on underlying demand. Rebase any DCF/exit-multiple work on the per-week figure.
2. **Watch the buyback dollar line, not just EPS, in FQ1'24.** FY23 buybacks fell to $77.6B from $89.4B. If the Dec-quarter repurchase pace is again below ~$20B/quarter, the buyback-driven EPS bridge thins materially — a legitimate reason to fade multiple expansion.
3. **Gross margin is the cleanest tell.** A 44%+ gross margin with negative revenue growth means mix is working. If FQ1'24 shows gross margin *falling* alongside revenue decline, the entire "services-mix rescue" thesis breaks — that combination would be the most negative possible data point.
4. **Set a flag at $6.33B inventory.** Inventory +28% on –3% revenue is the only line showing demand stress. A further build in FQ1'24 (into the seasonally strongest quarter) would be a tangible warning.
5. **The tax line is a live, underpriced event risk.** $4.5B of unrecognized benefits could reverse within 12 months → up to ~$0.28/share of EPS. Size positions knowing a discrete ~0.7%-of-revenue charge could land in any quarter.
6. **Liquidity framing: use $162B vs. $111B, not the current ratio.** Anyone screening AAPL on a 0.99 current ratio is being misled; the negative cash-conversion-cycle structure makes that metric non-diagnostic.
7. **Position sizing into the FQ1'24 event:** the fundamentals you can verify (FCF, net cash, margins) are strong and the ones you cannot (Dec-quarter revenue, guidance, China, Services growth) are the swing factors. Expect the event, not the FY23 10-K, to set the next 10–15% of price action.

---

## 10. Key data summary table

| Category | Metric | Value | Period / As of | Read |
|---|---|---|---|---|
| **Scale** | Total net revenue | $383,285M | FY2023 | –2.8% y/y (≈–4.6% per-week adj.) |
| | Net income | $96,995M | FY2023 | –2.8% y/y |
| | Diluted EPS | $6.13 | FY2023 | +0.3% (buyback-driven) |
| **Margins** | Gross margin | 44.13% | FY2023 | +81 bp — expanding on falling sales ✅ |
| | Operating margin | 29.82% | FY2023 | –47 bp — defended |
| | Net margin | 25.3% | FY2023 | flat y/y |
| | Opex / revenue | 14.3% | FY2023 | +1.3 pp — cost creep ⚠️ |
| **Cash** | Cash from operations | $110,543M | FY2023 | –9.5% y/y ⚠️ |
| | Capex | $10,959M | FY2023 | 2.9% of revenue (capital-light) |
| | Free cash flow | $99,584M | FY2023 | –10.6% y/y; 26.0% margin |
| | FCF / net income | 102.7% | FY2023 | Excellent earnings quality ✅ |
| | Cash taxes paid | $18,679M | FY2023 | > tax expense $16,741M |
| **Balance sheet** | Total assets | $352,583M | 2023-09-30 | flat y/y |
| | Cash + marketable securities | $162,099M | 2023-09-30 | Liquid fortress ✅ |
| | Total debt | $111,088M | 2023-09-30 | –$8,981M y/y |
| | Net cash | **$51,011M** | 2023-09-30 | Net-cash; negligible refi risk ✅ |
| | Shareholders' equity | $62,146M | 2023-09-30 | +22.6% y/y (rebuilt) |
| | Current ratio | 0.99 | 2023-09-30 | Structural, not distress |
| | Working capital | –$1,742M | 2023-09-30 | Little operating buffer ⚠️ |
| **Working capital** | Inventory | $6,331M | 2023-09-30 | **+28.0% y/y** — demand tell ⚠️ |
| | Accounts receivable | $29,508M | 2023-09-30 | +4.7% y/y |
| | Accounts payable | $62,611M | 2023-09-30 | –2.3% y/y |
| | Cash conversion cycle | ≈ –37.8 days | FY2023 | Supplier-funded ✅ |
| **Returns to holders** | Buybacks | $77,550M | FY2023 | **–13.2% y/y** ⚠️ |
| | Dividends paid | $15,025M | FY2023 | +1.2%; DPS $0.94 (+4.4%) |
| | Total capital returned | $92,575M | FY2023 | = **93.0% of FCF** (at ceiling) |
| | Diluted shares | ~15,824M | FY2023 | –3.1% y/y |
| **Tax** | Effective tax rate | 14.7% | FY2023 | Down from 16.2%; FDII benefit $0 |
| | Unrecognized tax benefit at risk | $4,500M | next 12 mo | Discrete charge risk ⚠️ |
| **Leverage/quality** | ROA | 27.5% | FY2023 | Exceptional ✅ |
| | ROE (avg equity) | ~172% | FY2023 | Flattered by thin equity |
| | Interest coverage | 29.1× | FY2023 | No solvency concern |
| | SBC expense | $10,833M | FY2023 | +19.9% y/y; $18.6B unrecognized ⚠️ |
| **Interim trend** | 9M FY23 CFO | $88,945M | 9M to 2023-07-01 | –9.3% y/y |
| | 9M FY23 buybacks | $56,547M | 9M to 2023-07-01 | –13.0% y/y |
| | FQ1 FY23 CFO | $34,005M | Oct–Dec 2022 | –27.6% — weak start to FY23 |
| **Missing / critical** | FQ1 FY2024 (Dec-2023 qtr) results | **Not filed as of 2024-01-16** | — | **Next fundamental reset — expected late Jan/early Feb 2024** |
| | Insider transactions | **DATA_UNAVAILABLE** | — | No authorized point-in-time archive; no inference made |
| | Product/Services & geographic mix, R&D vs SG&A, price/multiples | **Not in package** | — | Must be sourced separately |