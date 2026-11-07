# AAPL — Fundamental Research Report
**As of 2024-01-17 | Source: SEC XBRL facts (point-in-time, acceptance-time filtered) + vendor fundamental feed**

---

## 0. Data Provenance & Important Limitations (read first)

| Item | Status |
|---|---|
| Latest complete fiscal year | **FY2023, ended 2023-09-30** (10-K accepted 2023-11-03, accn 0000320193-23-000106) |
| Latest interim filings available | 10-Q for Q1 FY23 (Dec-22), Q2 FY23 (Apr-23), Q3 FY23 (Jul-23) — **cash-flow deltas only** |
| **Q1 FY2024 (Dec-2023 quarter)** | **NOT in the feed.** AAPL had not yet reported as of 2024-01-17. This is the single largest information gap; consensus expects the print in early February 2024. Do not assume Q1 FY24 numbers. |
| Quarterly income-statement / balance-sheet data | The vendor returned only **annual periods** for the income statement; the "quarterly" request resolved to the same FY21–FY23 annual facts. No quarterly P&L granularity is available. |
| Company profile, segment/product revenue split, unit shipments | **Not provided** by the vendor feed. Qualitative statements below are flagged as external context. |
| Price, market cap, consensus estimates, valuation multiples | **Not provided** by the tools. Absolute valuation multiples cannot be computed from tool data. |
| **Insider transactions** | **DATA_UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for AAPL. No insider buying/selling is asserted anywhere in this report. |

---

## 1. Company Snapshot

- **Identity:** Apple Inc. (AAPL), the world's largest consumer-technology franchise by market value, reporting on a **52/53-week fiscal year ending late September**.
- **Business model (external context, not from feed):** two reported segments — **Products** (iPhone, Mac, iPad, Wearables/Home/Accessories) and **Services** (App Store, iCloud, Apple Music/TV+, advertising, AppleCare, payments). Services carries structurally higher gross margin than hardware, making the product mix the dominant driver of consolidated gross margin.
- **Share count:** **15,550,061 thousand shares outstanding at 2023-09-30**; 15,552,752K as of the 2023-10-20 cover date. Authorized: 50.4bn shares; par $0.00001.
- **Float:** Entity public float **$2,591.165bn** as of 2023-03-31.
- **Dividend:** $0.94/share declared in FY2023 (vs $0.90 FY22, $0.85 FY21) — 11 consecutive years of increase implied by the trend.

---

## 2. Income Statement — FY2021 → FY2023

All figures USD millions, fiscal years ended late September.

| Line item | FY2021 | FY2022 | FY2023 | YoY (23 vs 22) |
|---|---:|---:|---:|---:|
| Net sales (derived: GP + COGS) | **365,817** | **394,328** | **383,285** | **−2.80%** |
| Cost of goods & services sold | 212,981 | 223,546 | 214,137 | −4.21% |
| **Gross profit** | **152,836** | **170,782** | **169,148** | −0.96% |
| Gross margin % | 41.78% | 43.31% | **44.13%** | +82 bps |
| Operating expenses (total) | 43,887 | 51,345 | 54,847 | +6.82% |
| Opex % of revenue | 12.00% | 13.02% | 14.31% | +129 bps |
| **Operating income** | **108,949** | **119,437** | **114,301** | **−4.30%** |
| Operating margin % | 29.78% | 30.29% | **29.82%** | −47 bps |
| Non-operating income/(expense) | +258 | −334 | −565 | worsening |
| Interest expense | 2,645 | 2,931 | **3,933** | +34.2% |
| Investment income (interest & dividend) | 2,843 | 2,825 | 3,750 | +32.7% |
| Pre-tax income | 109,207 | 119,103 | **113,736** | −4.51% |
| Income tax expense | 14,527 | 19,300 | 16,741 | −13.3% |
| **Effective tax rate** | 13.3% | 16.2% | **14.7%** | −150 bps |
| **Net income** | **94,680** | **99,803** | **96,995** | **−2.81%** |
| Net margin % | 25.88% | 25.31% | 25.31% | flat |
| **EPS diluted** | **$5.61** | **$6.11** | **$6.13** | **+0.33%** |
| EPS basic | $5.67 | $6.15 | $6.16 | +0.16% |
| Diluted shares (implied: NI / diluted EPS) | ~16,877M | ~16,334M | ~15,823M | **−3.1%** |
| Comprehensive income | 95,249 | 88,531 | 96,652 | +9.2% |

### What the P&L is actually telling you

1. **Revenue has rolled over but margins have not.** FY23 net sales fell 2.8% — the first annual decline since FY2019 — yet **gross margin expanded 82 bps to a record 44.13%**. That is the signature of a **mix shift toward Services and away from low-margin hardware**, plus benign input/component costs. This is a quality-of-revenue improvement, not deterioration, and it is the most bullish line in the entire filing set.
2. **Opex is now absorbing the margin gift.** Opex grew 6.8% against a 2.8% revenue decline; opex intensity rose from 13.0% to 14.3%. Net result: operating margin compressed 47 bps to 29.82%, and operating income fell 4.3% — worse than the revenue decline.
3. **EPS was rescued by the buyback, not by operations.** Headline EPS rose +0.33% while net income fell −2.81%. The entire gap is a **~3.1% reduction in diluted shares**. Strip the buyback and FY23 was an earnings-decline year. Traders should treat AAPL's EPS growth as *engineered* until revenue re-accelerates.
4. **Tax tailwind is real but finite.** ETR fell from 16.2% to 14.7%, worth roughly **$1.7bn** of net income (~$0.11 EPS) versus a constant 16.2% rate. Drivers visible in the tax footnote: FDII benefit fell to zero ($296m FY22 → $0), foreign rate differential widened to −$5,744m (a *benefit*), R&D credits $1,212m, and the SBC excess tax benefit shrank to $1,120m from $1,871m. **The SBC tax benefit is shrinking as the stock appreciates less — that is a structural headwind to the tax rate going forward.**
5. **Interest expense outgrew investment income.** Interest expense +34% to $3,933m on a *declining* debt balance tells you the low-coupon debt stack is rolling into a higher-rate world. Net interest swung to roughly −$183m. Non-operating expense of −$565m is now a modest but persistent drag.
6. **2-year track record:** revenue CAGR FY21→FY23 = **+2.4%/yr**; EPS CAGR = **+4.5%/yr**. This is a low-single-digit grower trading on a premium multiple — the setup demands Services re-acceleration.

---

## 3. Balance Sheet — 2023-09-30 vs 2022-09-24

USD millions.

| Item | 2022-09-24 | 2023-09-30 | Change |
|---|---:|---:|---:|
| Cash & cash equivalents | 23,646 | **29,965** | +26.7% |
| Marketable securities, non-current (AFS) | — | **100,544** | — |
| Accounts receivable, net | 28,184 | 29,508 | +4.7% |
| Nontrade receivables, current | 32,748 | 31,477 | −3.9% |
| Inventory, net | 4,946 | **6,331** | **+28.0%** |
| Other current assets | 21,223 | 14,695 | −30.8% |
| **Total current assets** | **135,405** | **143,566** | +6.0% |
| **Total assets** | **352,755** | **352,583** | −0.05% |
| Accounts payable | 64,115 | 62,611 | −2.3% |
| Commercial paper | 9,982 | **5,985** | −40.0% |
| Long-term debt — current | 11,128 | 9,822 | −11.7% |
| Long-term debt — non-current | 98,959 | 95,281 | −3.7% |
| **Total debt (CP + LTD)** | **120,069** | **111,088** | **−7.5%** |
| Other accrued liabilities, current | 54,293 | 50,010 | −7.9% |
| Deferred revenue (current) | 7,912 | 8,061 | +1.9% |
| Deferred revenue (total) | 12,400 | 12,100 | −2.4% |
| **Total current liabilities** | **153,982** | **145,308** | −5.6% |
| **Total liabilities** | **302,083** | **290,437** | −3.9% |
| **Shareholders' equity (derived)** | **50,672** | **62,146** | **+22.6%** |

### Balance-sheet diagnostics

| Metric | 2023-09-30 | Interpretation |
|---|---:|---|
| Current ratio | **0.99x** | Structurally <1.0 — normal for Apple, which funds itself with cheap working-capital float; not a liquidity concern |
| Working capital | **−$1,742m** | Negative, offset by $130bn+ of liquid securities |
| Total debt / equity | **1.79x** | Down sharply from 2.37x |
| Net cash proxy (cash + non-current AFS 130,509 − total debt 111,088) | **+$19,421m** | Net cash positive |
| Inventory / revenue | 1.65% | Up 28% YoY into the iPhone 15 launch quarter — **watch for channel-inventory commentary on the Q1 FY24 call** |
| Equity / assets | 17.6% | Low, but ARPU-accretive; ROE is optically extreme |

**Three things that matter here:**

- **Deleveraging is the story.** Total debt down **$9.0bn (−7.5%)**, commercial paper cut 40%, and equity up $11.5bn despite $92.6bn of shareholder returns — that is only possible because free cash flow is enormous. This is a fortress balance sheet by any measure.
- **Derived equity of $62,146m validates the buyback thesis.** Apple is returning ~93% of FCF while still growing book equity 22.6%. Buybacks are being funded entirely out of cash generation, not leverage.
- **⚠️ Note on the net-cash figure:** the vendor feed does **not** include Apple's ~$31.6bn of *current* marketable securities, and separately shows **$13,800m of restricted AFS securities** (escrow/legal-restricted, up from $12,700m). True net cash is somewhat higher than the $19.4bn proxy above. Do not quote a precise net-cash number off this feed alone.

---

## 4. Cash Flow Statement — the core of the AAPL thesis

USD millions, fiscal years.

| Item | FY2021 | FY2022 | FY2023 | YoY |
|---|---:|---:|---:|---:|
| **Operating cash flow** | **104,038** | **122,151** | **110,543** | **−9.5%** |
| Capital expenditures | (11,085) | (10,708) | (10,959) | +2.3% |
| **Free cash flow (derived)** | **92,953** | **111,443** | **99,584** | **−10.6%** |
| FCF margin | 25.4% | 28.3% | **26.0%** | −230 bps |
| FCF / net income | 0.98x | 1.12x | **1.03x** | — |
| Acquisitions of AFS debt securities | (109,558) | (76,923) | (29,513) | −61.6% |
| Sales of AFS debt securities | 47,460 | 37,446 | 5,828 | −84.4% |
| Maturities/prepayments of AFS | 59,023 | 29,917 | 39,686 | +32.7% |
| **Investing cash flow** | **(14,545)** | **(22,354)** | **+3,705** | swing to inflow |
| **Share repurchases** | **(85,971)** | **(89,402)** | **(77,550)** | −13.3% |
| Dividends paid | (14,467) | (14,841) | (15,025) | +1.2% |
| **Total shareholder returns** | **100,438** | **104,243** | **92,575** | **−11.2%** |
| SBC tax withholding | (6,556) | (6,223) | (5,431) | −12.7% |
| Proceeds from LT debt issuance | 20,393 | 5,465 | 5,228 | −4.3% |
| Repayments of LT debt | (8,750) | (9,543) | (11,151) | +16.9% |
| **Financing cash flow** | **(93,353)** | **(110,749)** | **(108,488)** | — |
| Net change in cash (incl. FX) | (3,860) | (10,952) | **+5,760** | positive swing |

### Nine-month FY2023 trend (from 10-Q, cumulative through 2023-07-01)

| Metric | 9M FY2022 | 9M FY2023 | YoY |
|---|---:|---:|---:|
| Operating cash flow | 98,024 | **88,945** | **−9.3%** |
| Capex | (7,419) | (8,796) | +18.6% |
| FCF (derived) | 90,605 | **80,149** | **−11.5%** |
| Repurchases | 64,974 | 56,547 | −13.0% |
| Dividends | 11,138 | 11,267 | +1.2% |

### Cash-flow interpretation

1. **FCF fell 10.6% to $99.6bn — the same magnitude as the operating-income decline (−4.3%) plus working-capital drag.** FCF/NI of 1.03x confirms earnings are cash-backed; there is no accrual-quality red flag. But the direction is down.
2. **Payout is at the ceiling: 93% of FY23 FCF went out the door as buybacks + dividends ($92,575m / $99,584m).** This is the single most important constraint on the stock. With net cash only ~$19–50bn and payout already at 93%, **the buyback cannot be the EPS-growth engine it was in FY23 without re-levering or a revenue re-acceleration.** That is the mechanical reason FY24 EPS growth risk is asymmetric.
3. **Buybacks were actively slowed:** −13.3% YoY in FY23 and −13.0% in the 9M comparison. Management throttled repurchases as the stock rose and FCF fell. Read this as a signal, not noise.
4. **Portfolio repositioning is visible and credit-positive:** AFS purchases fell 62% to $29.5bn while maturities rose 33% and sales collapsed 84%. Apple let the securities book roll off and **swung investing to a +$3.7bn inflow** — the first investing inflow in years. Combined with a $3.0bn net debt paydown, cash rose **+$5.76bn** despite 93% FCF payout. Capital allocation discipline is intact.
5. **Capex is remarkably low at 2.86% of revenue** ($10,959m). Apple's asset-light, outsourced-manufacturing model is what produces a 26% FCF margin. Rising capex (+2.3% FY23, +18.6% in 9M FY23) is worth monitoring — likely AI datacenter and silicon investment.

---

## 5. Capital Allocation, Dilution & Share-Based Comp

| Metric | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Diluted shares (implied, M) | ~16,877 | ~16,334 | ~15,823 |
| Shares outstanding EOY (M) | — | 15,943.4 | **15,550.1** |
| Shares repurchased ($M) | 85,971 | 89,402 | 77,550 |
| SBC expense ($M) | 7,906 | 9,038 | **10,833** |
| SBC % of revenue | 2.16% | 2.29% | **2.83%** |
| SBC tax benefit ($M) | 4,056 | 4,002 | 3,421 |
| Unrecognized SBC cost at YE ($M) | — | — | **$18,600m** |
| Dividends declared/share | $0.85 | $0.90 | $0.94 |

- **Net share reduction: 2.47%** in FY23 (15,943.4M → 15,550.1M).
- **SBC is rising faster than revenue** (2.83% of sales vs 2.29%) and there is **$18.6bn of unrecognized SBC cost** to amortize — a multi-year dilution headwind that offsets part of the buyback. Net buyback "efficiency" is therefore lower than the headline $77.6bn suggests.
- $10.8bn of SBC versus $77.6bn of buybacks means roughly **14% of the repurchase is simply offsetting employee issuance.**

---

## 6. Insider Transactions

**NOT AVAILABLE.** The insider-transactions archive for AAPL is not authorized in this point-in-time package. No insider buying or selling is reported, inferred, or estimated. Anyone relying on this report should source Form 4 activity independently before drawing conclusions about management sentiment.

---

## 7. Quality, Efficiency & Risk Metrics

| Metric | FY2023 | FY2022 | Comment |
|---|---:|---:|---|
| ROE (NI / derived equity) | **156.1%** | 197.0% | Optically extreme; not a comparable quality signal |
| ROA (NI / assets) | **27.5%** | 28.3% | Best-in-class for a company this size |
| Gross margin | **44.1%** | 43.3% | Record; Services mix |
| Operating margin | 29.8% | 30.3% | Peak-ish; opex creep |
| Net margin | 25.3% | 25.3% | Flat, remarkably stable |
| FCF margin | **26.0%** | 28.3% | Declining |
| FCF conversion (FCF/NI) | 1.03x | 1.12x | Healthy |
| Debt/equity | **1.79x** | 2.37x | Rapidly deleveraging |
| Effective tax rate | 14.7% | 16.2% | Unusually low; see watch items |
| Deferred revenue (total) | $12.1bn | $12.4bn | −2.4% — mild services-book deceleration signal |
| Inventory growth vs revenue growth | +28.0% vs −2.8% | — | **Divergence worth questioning** |

**Notable disclosure items from the filing set:**
- **Unrecognized tax benefits:** the company flags that a **$4.5bn decrease in unrecognized tax benefits is "reasonably possible" within 12 months** — i.e., a potential discrete tax charge/reserve release. This is a real swing factor for FY24 EPS that most screens miss.
- **Valuation allowance rose to $8,374m** from $7,530m — growing losses in some foreign jurisdictions.
- **Operating leases:** $13,841m total undiscounted commitments, $11,818m recognized liability, $1,719m due within 12 months. Immaterial at Apple's scale.
- **Debt maturity wall:** $9,943m due in the next 12 months, $10,775m in year 2, $12,265m in year 3, $9,786m in year 4, $7,800m in year 5, $56,003m thereafter. **Well-laddered and comfortably serviceable** — refinancing risk is low, but the ~$40bn maturing in years 2–4 must roll at materially higher coupons than the 2020-vintage issuance, which is why interest expense (+34% YoY) is the fastest-growing line on the P&L.

---

## 8. Actionable Insights for Traders

**Bull case (evidence-based, from the filings):**
1. **Record 44.1% gross margin** despite a 2.8% revenue decline — mix is structurally improving toward Services and the market is unlikely to have fully re-rated that.
2. **$99.6bn FCF, 1.03x cash conversion, net-cash balance sheet, debt down 7.5%** — the downside is a valuation question, never a solvency question.
3. **$18.6bn equity cushion added in FY23** (derived equity +22.6%) while returning 93% of FCF. Compounding intrinsic value regardless of the tape.

**Bear case (evidence-based):**
1. **EPS growth is cosmetic.** +0.33% EPS on −2.81% net income is entirely buyback arithmetic, and **buybacks fell 13.3% YoY with payout already at 93% of FCF.** The lever is nearly exhausted.
2. **Revenue is shrinking and opex is growing** — operating income −4.3%, opex +6.8%. Operating leverage is *negative* right now.
3. **FCF −10.6%**, OCF −9.5%, 9M FY23 OCF −9.3%. The cash engine is decelerating in step with earnings.
4. **Inventory +28% into the launch quarter** with revenue −2.8% — a leading indicator that needs an explanation on the next call.
5. **Tax rate risk cuts both ways:** FY23's 14.7% ETR is historically low, the SBC excess tax benefit is shrinking ($1,871m → $1,120m), and a **$4.5bn unrecognized-tax-benefit adjustment is flagged as reasonably possible.** A normalizing ETR is a direct EPS headwind.

**Concrete positioning guidance:**
- **Do not model FY24 EPS growth off FY23's pattern.** With 93% FCF payout and buybacks slowing, the FY24 EPS bridge requires *earnings* growth. Sensitivity: every 100 bps of ETR normalization on ~$114bn pre-tax ≈ **$1.14bn net income ≈ $0.07–0.08 EPS.**
- **The Q1 FY24 print (early Feb 2024) is the binary event.** The whole thesis hinges on three disclosures this report cannot see: (a) does gross margin hold ≥44%?, (b) does Greater China return to growth?, (c) does the buyback pace re-accelerate? Treat the current data set as the *pre-event* baseline only.
- **Key qualitative catalysts/risks to track (external context, not from vendor data, and not in the filing set):** App Store/antitrust regulatory pressure and the EU Digital Markets Act compliance deadline in **March 2024** (material to the high-margin Services line); the **Masimo/ITC Apple Watch pulse-oximetry dispute**, where an import ban was stayed by an appellate court in late December 2023 with modified watch sales resuming; memory/component pricing; and FX.
- **Insider signal: unavailable.** Weight this as a genuine blind spot rather than as neutral evidence.

**One-line stance:** *High-quality, cash-generative, deleveraging franchise with improving gross margin but a decelerating top line, no remaining buyback headroom, and an unsustainably low tax rate — a "prove-it" quarter setup into the Q1 FY24 print, best expressed as a fundamentals-confirmed, event-driven trade rather than a momentum add.*

---

## 9. Key Points Summary

| Category | Data point | Value / Finding | Signal |
|---|---|---|---|
| **Data cutoff** | Latest filing | FY2023 10-K, accepted 2023-11-03 | ⚠️ Q1 FY24 unreported as of 2024-01-17 |
| **Revenue** | FY2023 net sales | $383,285m, **−2.80% YoY** | 🔴 Top-line contraction |
| **Revenue trend** | FY21→FY23 CAGR | +2.4%/yr | 🟡 Low growth |
| **Gross margin** | FY2023 | **44.13%** (record; +82 bps) | 🟢 Mix shift to Services |
| **Opex** | FY2023 | $54,847m, **+6.82%**; 14.31% of sales | 🔴 Negative operating leverage |
| **Operating income** | FY2023 | $114,301m, **−4.30%**; 29.82% margin | 🔴 Declining |
| **Net income** | FY2023 | $96,995m, −2.81%; 25.31% margin | 🟡 Stable margin, falling dollars |
| **EPS diluted** | FY2023 | $6.13, **+0.33%** on −2.81% NI | 🔴 Buyback-engineered |
| **Diluted shares** | FY23 vs FY22 | 15,823M vs 16,334M (−3.1%) | 🟡 Buyback offset by SBC |
| **Effective tax rate** | FY2023 | **14.7%** (vs 16.2% FY22) | 🔴 Unsustainably low; $4.5bn UTB risk flagged |
| **Operating cash flow** | FY2023 | $110,543m, **−9.5%** | 🔴 Decelerating |
| **Free cash flow** | FY2023 | **$99,584m** (−10.6%); 26.0% margin | 🟢 Enormous, but shrinking |
| **FCF conversion** | FY2023 | 1.03x net income | 🟢 High earnings quality |
| **Capex** | FY2023 | $10,959m (2.86% of sales) | 🟢 Asset-light model |
| **Payout ratio (FCF)** | FY2023 | **92.96%** ($92,575m / $99,584m) | 🔴 Buyback lever exhausted |
| **Buybacks** | FY2023 | $77,550m, **−13.3% YoY** | 🔴 Management throttling |
| **Dividends** | FY2023 | $15,025m paid; $0.94/share declared | 🟢 11th straight raise |
| **Cash & equivalents** | 2023-09-30 | **$29,965m** (+26.7%) | 🟢 |
| **Non-current AFS securities** | 2023-09-30 | $100,544m | 🟢 Deep liquidity |
| **Total debt** | 2023-09-30 | **$111,088m** (−7.5%); CP cut 40% | 🟢 Deleveraging |
| **Net cash (proxy)** | 2023-09-30 | **+$19,421m** (excludes ~$31.6bn current AFS) | 🟢 Net-cash positive |
| **Debt/equity** | 2023-09-30 | **1.79x** (from 2.37x) | 🟢 Improving fast |
| **Current ratio** | 2023-09-30 | 0.99x; WC −$1,742m | 🟡 Structural, not a concern |
| **Shareholders' equity** | 2023-09-30 | **$62,146m**, +22.6% | 🟢 |
| **Inventory** | 2023-09-30 | $6,331m, **+28.0%** vs revenue −2.8% | 🔴 Watch channel inventory |
| **Deferred revenue** | 2023-09-30 | $12,100m, −2.4% | 🟡 Services book soft |
| **SBC expense** | FY2023 | $10,833m (2.83% of sales); $18.6bn unrecognized | 🔴 Rising dilution offset |
| **ROA** | FY2023 | 27.5% | 🟢 Best-in-class |
| **Interest expense** | FY2023 | $3,933m, **+34.2%** | 🔴 Refinancing at higher rates |
| **Debt maturities** | Next 12m / Yr2 / Yr3 | $9,943m / $10,775m / $12,265m | 🟢 Well-laddered |
| **Insider transactions** | — | **DATA UNAVAILABLE** | ⚪ Blind spot — source Form 4s externally |
| **Next catalyst** | Q1 FY2024 results | Expected early Feb 2024 (not in data) | 🟡 Binary event |

---

*Prepared from point-in-time SEC XBRL facts accepted on or before 2024-01-17. All derived figures (net sales, equity, FCF, ratios, diluted shares) are computed from reported line items and are labeled as derived. Qualitative market/regulatory commentary is external context and is not sourced from the vendor feed. Insider-transaction data was unavailable and no inference has been made.*