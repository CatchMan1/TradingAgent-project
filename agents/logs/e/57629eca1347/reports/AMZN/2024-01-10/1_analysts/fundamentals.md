# AMZN — Fundamental Research Report
**Amazon.com, Inc. (AMZN)** | Analysis date: **2024-01-10** | Reporting currency: USD

---

## 1. Data Provenance & Important Caveats (read first)

| Item | Status |
|---|---|
| Latest SEC filing in feed | **Form 10-Q for period ended 2023-09-30**, accepted **2023-10-27** (accn 0001018724-23-000018) |
| Prior 10-Q in feed | 10-Q for period ended 2023-06-30, accepted 2023-08-04 |
| Q4 2023 / FY2023 results | **Not yet reported as of 2024-01-10** — no Q4 data exists in the point-in-time feed. This is a pre-earnings report. |
| Revenue line item | **Not present as an XBRL tag in this feed.** Revenue below is **derived** as `CostsAndExpenses + OperatingIncomeLoss` (validated against multiple known periods). Flagged as *derived* throughout. |
| Segment-level revenue / AWS detail | **Not in feed.** Only `NumberOfOperatingSegments = 3` is confirmed. |
| Buyback / share repurchase | Zero in every period from 2022-07-01 onward (`PaymentsForRepurchaseOfCommonStock = 0`). |
| **Insider transactions** | **DATA UNAVAILABLE.** The vendor has no authorized point-in-time insider-transaction archive for AMZN as of 2024-01-10. No inference made — treat insider signal as a known data gap, not as "no activity." |
| Price / valuation multiples | No price data in feed — P/E, EV/EBITDA, FCF yield cannot be computed here. |

---

## 2. Company Profile

Amazon.com, Inc. is a global technology and e-commerce conglomerate operating **three reportable segments** (confirmed: `NumberOfOperatingSegments = 3`):

1. **North America** — online and physical retail, third-party marketplace, advertising, Prime subscriptions, devices.
2. **International** — the same retail/marketplace model across non-US geographies, historically lower-margin and structurally challenged in several markets.
3. **Amazon Web Services (AWS)** — cloud infrastructure, database, analytics, AI/ML services; the highest-margin and highest-cash-generating business and the primary swing factor in consolidated profitability.

**Business model characteristics evident in the financials:**
- **Massive scale with thin reported margins** but very high asset velocity — 9M2023 revenue of ~$405B (derived) against only $487B of total assets.
- **Extremely capital-intensive**: $54.7B TTM capex, plus $73.9B of operating lease liabilities and $12.5B of finance lease liabilities — a "capex + leases" model for fulfillment, data centers, and logistics.
- **Working-capital-funded operations**: $72.0B of accounts payable and $58.8B of accrued liabilities fund inventory and receivables. This is a structural, negative-working-capital engine, but it is seasonal (AP peaks at year-end) and it *reversed* sharply through 2023 — a key cash flow dynamic analyzed in §5.
- **Heavy stock-based compensation**: $17.7B in 9M2023 alone, with $23.3B of unrecognized RSU expense outstanding.

---

## 3. Income Statement Analysis

### 3.1 Derived revenue and profitability (all $ millions)

| Period | Revenue (derived) | YoY | COGS | Gross Profit | GM% | Op. Income | Op. Margin | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|---|---|---|
| **Q3 2023** (Jul–Sep) | **143,083** | **+12.6%** | 75,022 | 68,061 | **47.6%** | **11,188** | **7.82%** | 9,879 | **0.94** |
| Q3 2022 (Jul–Sep) | 127,101 | — | 70,268 | 56,833 | 44.7% | 2,525 | 1.99% | 2,872 | 0.28 |
| **9M 2023** (Jan–Sep) | **404,824** | **+11.0%** | 212,186 | 192,638 | **47.6%** | **23,643** | **5.84%** | 19,801 | **1.89** |
| 9M 2022 (Jan–Sep) | 364,779 | — | 203,191 | 161,588 | 44.3% | 9,511 | 2.61% | (3,000) | (0.29) |
| H1 2023 (Jan–Jun) | 261,741 | +10.1% | 137,164 | 124,577 | 47.6% | 12,455 | 4.76% | 9,922 | — |
| H1 2022 (Jan–Jun) | 237,678 | — | 132,923 | 104,755 | 44.1% | 6,986 | 2.94% | (5,872) | — |
| **TTM** (Oct 2022–Sep 2023) | **~554,000** | — | — | — | ~47% | **26,381** | **4.76%** | **20,079** | — |

*Revenue derived as `CostsAndExpenses + OperatingIncomeLoss`; TTM revenue uses Q4 2022 of ~$149.2B (derived from the reported FY2022 total, which is outside this feed).*

### 3.2 The single most important fundamental fact: **gross margin inflected hard**

- Gross margin expanded from **44.3% → 47.6%** over the first nine months (+329 bps), and **44.7% → 47.6%** in Q3 alone (+290 bps).
- Operating margin **more than doubled**, from 2.61% → 5.84% over nine months, and from 1.99% → 7.82% in Q3.
- That is roughly **+$13.0B of incremental gross profit and +$14.1B of incremental operating income on $40.0B of incremental revenue** — i.e., an **incremental operating margin of ~35%**. This is the signature of operating leverage, not volume growth: cost-of-sales growth (+4.4% yoy in 9M) was *far* below revenue growth (+11.0%).

### 3.3 Where the operating expense leverage came from (disclosed line items)

| Line item | 9M 2023 | 9M 2022 | YoY | % of revenue '23 | % of revenue '22 |
|---|---|---|---|---|---|
| Cost of goods & services | 212,186 | 203,191 | +4.4% | 52.4% | 55.7% |
| Marketing | 31,468 | 29,420 | +7.0% | 7.78% | 8.07% |
| G&A | 8,806 | 8,558 | +2.9% | 2.18% | 2.35% |
| **Total costs & expenses** | **381,181** | **355,268** | **+7.3%** | **94.2%** | **97.4%** |

- **Total cost growth of +7.3% against +11.0% revenue growth** is the entire margin story. Costs decelerated well below revenue for the first time in the post-2021 era.
- Q3 2023 is even sharper: **marketing down 4.2% yoy** ($10,551 vs $11,014) and **G&A down 16.3% yoy** ($2,561 vs $3,061) — outright absolute declines. This is discipline, not just leverage.
- Note total costs & expenses are 94.2% of revenue — the consolidated business still runs on a **~5–8% operating margin**, so small percentage changes in cost lines dominate earnings. Sensitivity is very high: **a 100 bp move in consolidated operating margin on ~$554B TTM revenue = ~$5.5B of operating income.**

### 3.4 Below-the-line: the 2022 distortion is gone

| Item | 9M 2023 | 9M 2022 | Delta |
|---|---|---|---|
| Operating income | 23,643 | 9,511 | +14,132 |
| Nonoperating income (expense) | **+228** | **(14,485)** | **+14,713** |
| — of which equity securities FV gains/losses | +1,000 | **(11,300)** | +12,300 |
| Interest expense | (2,469) | (1,673) | +47.6% worse |
| Investment income (interest) | 2,048 | 544 | +276% |
| Pre-tax income | 23,871 | (4,974) | +28,845 |
| Income tax expense | (4,058) | +1,990 (benefit) | — |
| Net income | **19,801** | **(3,000)** | +22,801 |

**Critical insight:** 2022's reported loss was largely **non-operating** (an $11.3B mark-to-market loss on equity securities — the Rivian stake). The 2023 rebound is therefore **two independent improvements**: (a) genuine operating-margin expansion of ~$14.1B, and (b) the disappearance of a ~$14.7B non-operating drag. Only (a) is durable and repeatable — traders should not extrapolate the full $22.8B swing.

**Effective tax rate** rose to **17.0%** (9M) and **18.9%** (Q3) from a net benefit in 2022 — a real headwind to EPS growth as profitability normalizes. Cash taxes paid ($6,982M, 9M) substantially exceed book tax expense ($4,058M) because the deferred tax line is a $4,412M benefit — a quality-of-earnings nuance.

**Interest is now roughly neutral:** 9M2023 interest expense $2,469M vs. interest income $2,048M. Q3 2023 was nearly exactly offsetting ($806M expense vs. $776M income). Rising rates are now a **tailwind to the ~$99B liquid asset pile** roughly matching the cost of the debt stack.

---

## 4. Segment Detail — Data Gap

The feed confirms **3 operating segments** but provides **no segment revenue or segment operating income**. This is the most material analytical blind spot: AMZN's consolidated margin is a blend of a low-single-digit-margin retail business and a high-margin cloud business, and the feed **cannot** tell you which one drove the +329 bps gross margin expansion.

**Actionable implication:** the Q4/FY2023 10-K (pending, expected early February 2024) is the first document that will let you attribute the margin expansion between AWS, North America retail, and advertising. Until then, treat the "AWS reacceleration" narrative as **unverified by this dataset**.

---

## 5. Cash Flow — The FCF Inflection (the second key fact)

### 5.1 Operating and free cash flow ($ millions)

| Period | OCF | YoY | Capex (purchases of productive assets) | YoY | **FCF (OCF – capex)** |
|---|---|---|---|---|---|
| **Q3 2023** | **21,217** | **+86.0%** | 12,479 | **−23.8%** | **+8,738** |
| Q3 2022 | 11,404 | — | 16,378 | — | (4,974) |
| **9M 2023** | **42,481** | **+141.6%** | 38,141 | **−18.9%** | **+4,340** |
| 9M 2022 | 17,579 | — | 47,053 | — | (29,474) |
| **TTM (Oct'22–Sep'23)** | **71,654** | **+80.6%** | 54,733 | **−17.1%** | **+16,921** |
| Prior TTM (Oct'21–Sep'22) | 39,665 | — | 65,988 | — | (26,323) |

**The TTM free cash flow swing is +$43.2B year over year** — from −$26.3B to +$16.9B. This is the cleanest, most tradable fundamental fact in the dataset. It is driven by **both** sides of the equation simultaneously:
- OCF up **+80.6%** (earnings + non-cash add-backs).
- Capex **down −17.1%** — Amazon is harvesting the 2021–2022 fulfillment/warehouse buildout.

Capex intensity fell from **12.9% of revenue (9M 2022) to 9.4% of revenue (9M 2023)** — roughly **350 bps of revenue released to free cash flow**.

### 5.2 The D&A / capex crossover

| Metric | 9M 2023 | 9M 2022 | YoY |
|---|---|---|---|
| Depreciation & amortization | **34,843** | 29,236 | **+19.2%** |
| Capex | 38,141 | 47,053 | **−18.9%** |
| Capex / D&A | **1.09x** | 1.61x | — |

D&A is growing ~19% while capex falls ~19% — the two lines are converging. The capex/D&A ratio collapsing from 1.61x to 1.09x is precisely the mechanic that generates the FCF inflection. **When capex falls below D&A, reported FCF overstates sustainable FCF**, because the asset base is depreciating faster than it is being replenished. Traders should watch for capex reacceleration (AI/data-center build) as the **single largest threat** to the 2024 FCF story.

### 5.3 Quality-of-cash caveat: SBC

| Metric | Value |
|---|---|
| SBC, 9M 2023 | **17,704** (4.37% of revenue) |
| SBC, 9M 2022 | 14,015 (3.84% of revenue) |
| SBC annualized run-rate | **~23,600** |
| Unrecognized RSU cost (9/30/23) | **23,300** |
| TTM FCF | 16,921 |
| **TTM FCF less SBC run-rate** | **≈ (6,700)** |

**This is essential:** SBC is added back to operating cash flow. On a fully-loaded basis (treating stock comp as the real compensation expense it is), **AMZN's TTM free cash flow is still approximately negative $6–7B.** The FCF "inflection" is genuine on a reported basis, but the business has not yet crossed into positive fully-loaded FCF. SBC is also rising faster than revenue (+53 bps of revenue yoy), and unrecognized RSU expense equals roughly **four quarters** of current run-rate.

### 5.4 Working capital and its seasonality (avoid a common misread)

| Balance | 2023-09-30 | 2022-12-31 | Change |
|---|---|---|---|
| Accounts payable | **72,004** | 79,600 | **−7,596** |
| Accrued liabilities | 58,812 | 62,566 | −3,754 |
| Inventory | 35,406 | 34,405 | +1,001 |
| Accounts receivable | 43,420 | 42,360 | +1,060 |
| Contract liabilities (current + noncurrent) | 17,098 | 16,100 | +998 |

Cash flow statement confirmation: `IncreaseDecreaseInAccruedLiabilities` **−9,022** and `IncreaseDecreaseInAccountsReceivableAndOtherOperatingAssets` **−10,364** (a use of cash) in 9M2023.

**Caution:** the $7.6B AP decline looks alarming but is **substantially seasonal** — Amazon's payables peak at the Q4 holiday build and unwind through Q1–Q3. Because this pattern repeats annually, the **yoy OCF comparison (9M vs 9M) is clean and the +141.6% growth is apples-to-apples.** Do not annualize the Q4 payables rebuild as a permanent cash source.

### 5.5 Financing and investing flows

| Item | 9M 2023 | 9M 2022 | TTM (Oct'22–Sep'23) |
|---|---|---|---|
| Operating cash flow | 42,481 | 17,579 | 71,654 |
| Investing cash flow | **(37,232)** | (26,780) | (48,053) |
| Financing cash flow | **(9,133)** | +9,632 | (9,047) |
| Net change in cash + restricted | (4,172) | (1,299) | +14,903 |
| Long-term debt issued | **0** | 12,931 | 8,235 |
| Long-term debt repaid | (3,386) | (1) | (4,643) |
| Short-term debt proceeds / repayments | 17,395 / (19,339) | 30,946 / (21,757) | 28,002 / (35,136) |
| Share repurchases | **0** | (6,000) | **0** |
| Business acquisitions | 3,829 | 6,600 | 5,545 |

Amazon has moved to **gross deleveraging**: zero new long-term bond issuance in 9M2023, $3.4B of long-term debt retired, and net short-term commercial paper paydown of ~$1.9B. Financing is now a **$9.1B outflow** versus a $9.6B inflow in 9M2022. Management is de-risking the balance sheet rather than funding growth with debt — consistent with a maturing, cash-generative posture.

---

## 6. Balance Sheet, Liquidity, and Leverage (as of 2023-09-30)

| Item | 2023-09-30 | 2022-12-31 | Change |
|---|---|---|---|
| Cash & equivalents | 49,605 | 53,888 | −4,283 |
| Marketable securities (AFS, fair value) | **49,871** | ~ | — |
| **Total liquid assets (cash + AFS)** | **~99,476** | — | — |
| Accounts receivable | 43,420 | 42,360 | +1,060 |
| Inventory | 35,406 | 34,405 | +1,001 |
| **Current assets** | **142,995** | 146,791 | −3,796 |
| **Current liabilities** | **145,214** | 155,393 | **−10,179** |
| **Total assets** | **486,883** | 462,675 | **+24,208** |
| Long-term debt — current | 5,995 | 2,999 | +2,996 |
| Long-term debt — noncurrent | 61,098 | 67,150 | −6,052 |
| **Total long-term debt** | **67,093** | 70,149 | **−3,056** |
| Finance lease liabilities | 12,466 | 15,783 | −3,317 |
| **Total debt + finance leases** | **79,559** | 85,932 | **−6,373** |
| Operating lease liabilities | 73,902 | 69,040 | **+4,862** |
| Operating lease ROU asset | 70,758 | 66,123 | +4,635 |
| APIC | 92,711 | 75,066 | +17,645 |
| AOCI | (5,003) | (4,487) | −516 |

### 6.1 Liquidity — reported ratio looks tight, reality is comfortable

- **Current ratio = 142,995 / 145,214 = 0.99x** — below 1.0. On a textbook screen this looks like a liquidity problem.
- **Quick ratio = (142,995 − 35,406) / 145,214 = 0.74x.**
- **But:** ~$99.5B of that current asset base is cash and market-grade securities, of which **$43.1B matures within one year** and only $1.0B is beyond 10 years — a very short-duration, high-quality liquidity book. A sub-1.0 current ratio is a **structural feature of the negative-working-capital retail model**, not distress.

### 6.2 Leverage — fortress balance sheet

| Metric | Value |
|---|---|
| Gross debt + finance leases | 79,559 |
| Less: cash + AFS | (99,476) |
| **Net debt** | **≈ (19,900) — net cash** |
| TTM EBITDA (op. income 26,381 + D&A 47,528) | **73,909** |
| **Gross debt / EBITDA** | **≈ 1.08x** |
| **Net debt / EBITDA** | **negative (net cash)** |
| 9M interest coverage (op. income / interest expense) | **9.6x** |

Near-zero net leverage with 9.6x interest coverage. **There is essentially no solvency or refinancing risk in AMZN** based on this dataset — which means credit-oriented downside scenarios are off the table and the equity story is purely about earnings power and cash conversion.

### 6.3 The lease liability is the real "hidden debt"

Operating lease liabilities of **$73.9B** nearly match the $67.1B of long-term debt. Combined obligations = **$153.5B**, which would be **2.1x EBITDA** if capitalized — still modest, but a large part of the current-liability squeeze. Undiscounted operating lease payments total **$88.8B** ($3.2B remainder of FY23, $10.0B in the next twelve months, $9.4B year two). The **weighted-average discount rate rose from 2.8% to 3.2%**, expanding the liability (+$4.9B) with no economic change — a rate-driven, non-cash drag worth noting.

### 6.4 Contractual obligations

| Bucket | Amount (9/30/23) |
|---|---|
| Total contractual obligations | **284,407** |
| Due next twelve months | **35,712** |
| Remainder of FY2023 | 8,914 |
| Year 2 | 28,429 |
| Year 3 | 23,789 |
| Year 4 | 26,581 |
| Purchase & other commitments (remainder of FY) | 1,415 |

---

## 7. Capital Allocation and Dilution

| Metric | 9M 2023 | 9M 2022 |
|---|---|---|
| Share repurchases | **$0** | $6,000M |
| SBC | 17,704 | 14,015 |
| Shares outstanding (period end) | 10,330M | 10,242M (12/31/22) |
| Shares issued | 10,845M | 10,757M (12/31/22) |
| Shares outstanding (10/18/23 cover date) | **10,334.0M** | — |

- **Zero buybacks for six consecutive quarters.** Amazon has entirely redirected cash from repurchases to debt reduction and internal investment.
- Dilution is **modest but persistent**: shares outstanding +0.86% in nine months, roughly **+1.1–1.2% annualized**. SBC of $17.7B (4.4% of revenue) against a ~$1T+ market cap implies roughly a 1.5–2% annual gross grant; net dilution is under 1% because of forfeitures and the absence of new large grants at the current scale.
- **Catalyst to watch:** with FCF turning positive and net cash at ~$20B, a **new buyback authorization** is a plausible re-rating event. Its absence is arguably the clearest sign management still prioritizes investment (AI, logistics, AWS capacity) over shareholder returns.

---

## 8. Returns and Efficiency

| Metric | Calculation | Result |
|---|---|---|
| ROA (TTM) | 20,079 / 486,883 | **4.1%** |
| Pre-tax ROIC (TTM, approx.) | 26,381 / (equity ~192,900 + debt 79,559 − cash 99,476) | **~15.2%** |
| Capex intensity (TTM) | 54,733 / ~554,000 | **9.9%** (vs. 12.9% in 9M22) |
| SBC / revenue | 17,704 / 404,824 | **4.37%** |
| FCF margin (TTM) | 16,921 / ~554,000 | **3.05%** |
| Asset turnover (TTM) | ~554,000 / 486,883 | **1.14x** |
| Revenue per dollar of equity (TTM) | ~554,000 / 192,900 | **2.87x** |

*Note: stockholders' equity is partially inferred (retained earnings line is absent from the feed); APIC of $92.7B and AOCI of −$5.0B are directly observed. Treat ROE/ROIC as directional.*

**Interpretation:** ROA of 4.1% on a 1.14x asset-turnover, low-margin base is the mathematical signature of a high-volume, low-margin retailer — but the **direction of travel matters far more than the level**. A ~15% pre-tax return on invested capital for a business of this scale, funded largely by supplier float, is structurally attractive and improving as capex normalizes.

---

## 9. Actionable Insights for Traders

**1. The thesis is margin expansion, and it is measured, not narrative.** Gross margin +329 bps and operating margin +323 bps over nine months, with total costs growing 7.3% against 11.0% revenue growth. *Evidence to trade on:* Q3 alone delivered 7.82% consolidated operating margin versus 1.99% a year earlier. **Watch the Q4 2023 print for whether consolidated operating margin holds above ~5%** — that is the line that separates "one-off cost discipline" from a durable re-rating.

**2. Q4 2023 has a remarkably easy comparison — but expectations are the risk.** Deriving Q4 2022 from TTM and 9M figures: Q4 2022 operating income was only **~$2.7B (~1.8% margin)** and net income just **~$278M**. A repeat of Q3's 7.8% margin on a holiday quarter would produce an enormous yoy delta. **The comp is not the question; the question is how much of it is already in the price.** Position sizing, not direction, is the risk.

**3. Free cash flow inflected by +$43B — but the quality is mixed.** TTM FCF went from −$26.3B to +$16.9B. However, **SBC of ~$23.6B annualized exceeds TTM FCF of $16.9B.** On a fully-loaded basis AMZN is still burning cash. Trade the reported FCF trajectory (improving, visible, mechanical) but do not underwrite a "cash machine" narrative yet.

**4. The capex/D&A crossover is the mechanism and the risk.** Capex/D&A fell from 1.61x to 1.09x. FCF is being manufactured by cutting capex (−18.9%) while D&A compounds (+19.2%). **Any reacceleration of capex — AI infrastructure, AWS capacity — compresses 2024 FCF immediately**, because capex is a dollar-for-dollar hit while the revenue it supports lags by years. This is the highest-probability negative surprise.

**5. Balance sheet risk is off the table; the equity is a pure earnings-beta instrument.** Net cash of ~$20B, gross debt/EBITDA of ~1.1x, 9.6x interest coverage, zero new bond issuance in 9M2023, and $3.4B of debt retired. Interest income ($2,048M, 9M) now offsets interest expense ($2,469M). This removes credit-driven downside scenarios and increases the sensitivity of the equity to margin surprises.

**6. No buyback is a live catalyst.** Six straight quarters of zero repurchases while generating $16.9B of TTM FCF and holding ~$99B of liquid assets. A new authorization would be a clean, unambiguously positive signal. Its continued absence signals continued heavy investment intent.

**7. The 2022 comparison is contaminated — model 2023–24 off operating income, not net income.** The +$22.8B 9M net income swing decomposes into ~$14.1B of real operating improvement and ~$14.7B of non-operating swing (an $11.3B equity mark in 2022 that did not recur). **Two-thirds of the reported earnings recovery is non-operating and non-repeating.** Analysts anchoring on net income growth rates will overstate durability; anchor on operating income (+148.6% yoy in 9M, from a depressed base).

**8. Tax rate normalization is a quiet EPS headwind.** Effective rate moved from a net benefit in 2022 to 17.0% (9M) / 18.9% (Q3) in 2023, with cash taxes of $6,982M exceeding book expense of $4,058M. Expect the tax line to keep working against reported EPS growth.

**9. Dilution and SBC are a slow bleed, not a crisis.** Shares outstanding +0.86% in nine months; SBC at 4.37% of revenue and rising 53 bps yoy; $23.3B of unrecognized RSU expense remains. Fully diluted EPS of $0.94 on $9,879M of net income implies ~10.51B diluted shares versus 10.33B basic — a ~1.7% dilution gap on the income statement alone.

---

## 10. Key Risks

| Risk | Evidence from dataset | Severity |
|---|---|---|
| **Capex reacceleration** | Capex/D&A down to 1.09x from 1.61x; FCF is capex-cut-driven, not organic | **High** |
| **SBC-adjusted FCF still negative** | TTM FCF $16,921M vs SBC run-rate ~$23,600M | **Medium-High** |
| **Segment/AWS opacity** | No segment revenue or segment operating income in feed despite 3 confirmed segments | **Medium-High** (analytical) |
| **Thin absolute margins** | Total costs 94.2% of revenue; 100 bps of margin = ~$5.5B of EBIT | **Medium** |
| **Operating lease burden** | $73.9B liability, $88.8B undiscounted payments, discount rate rising 2.8%→3.2% | **Medium** |
| **Negative working capital seasonality** | AP −$7.6B and accrued −$3.8B since 12/31/22 | **Low-Medium** (seasonal) |
| **Tax rate normalization** | Effective rate to 17.0–18.9% from a 2022 net benefit | **Medium** |
| **Non-operating earnings volatility** | Equity securities FV swing of +$12.3B yoy; $753M illiquid equity holdings | **Medium** |
| **Sub-1.0 current ratio optics** | 0.99x current, 0.74x quick — mitigated by $99.5B liquid assets | **Low** |
| **Insider signal unavailable** | Vendor has no authorized insider archive for AMZN at 2024-01-10 | **Data gap** |

---

## 11. Summary Table — Key Points at a Glance

| Category | Metric | Value | Read-through |
|---|---|---|---|
| **Identity** | Ticker / Company | **AMZN** / Amazon.com, Inc. | — |
| **Timeliness** | Latest filing | 10-Q, period ended **2023-09-30**, accepted **2023-10-27** | Q4/FY2023 **not yet reported** at 2024-01-10 |
| **Scale** | Revenue, 9M 2023 (derived) | **$404.8B**, +11.0% yoy | Double-digit growth on a $550B+ base |
| **Scale** | Revenue, TTM (derived) | **~$554B** | — |
| **Growth** | Q3 2023 revenue | **$143.1B**, +12.6% yoy | Reacceleration vs. 9M average |
| **Profitability** | Q3 2023 gross margin | **47.6%** (+290 bps yoy) | Largest single driver of the re-rating |
| **Profitability** | 9M 2023 gross margin | 47.6% (+329 bps yoy) | Consistent, not one-quarter noise |
| **Profitability** | Q3 2023 operating margin | **7.82%** vs 1.99% | +583 bps — step-change |
| **Profitability** | 9M 2023 operating margin | **5.84%** vs 2.61% | +323 bps, delivered |
| **Profitability** | Operating income, 9M 2023 | **$23,643M** vs $9,511M | **+148.6%** — the real earnings story |
| **Profitability** | Net income, 9M 2023 | **$19,801M** vs $(3,000)M | +$22.8B, but $14.7B of it is non-operating |
| **EPS** | Q3 2023 diluted | **$0.94** (vs $0.28) | 9M: **$1.89** (vs −$0.29) |
| **Cost control** | Total costs & expenses, 9M | +7.3% vs +11.0% revenue | **The mechanism of margin expansion** |
| **Cost control** | Q3 marketing / G&A | **−4.2% / −16.3% yoy** | Absolute declines — genuine discipline |
| **Cash flow** | Q3 2023 OCF | **$21,217M**, +86.0% yoy | — |
| **Cash flow** | 9M 2023 OCF | **$42,481M**, +141.6% yoy | — |
| **Cash flow** | TTM OCF | **$71,654M**, +80.6% yoy | — |
| **Capex** | TTM capex | **$54,733M**, −17.1% yoy | Capex/revenue 12.9% → 9.9% |
| **FCF** | TTM FCF (OCF − capex) | **+$16,921M** vs **−$26,323M** | **+$43.2B swing — headline fundamental event** |
| **FCF quality** | TTM FCF less SBC run-rate | **≈ −$6,700M** | Fully-loaded FCF still negative |
| **Capex cycle** | Capex / D&A | **1.09x** vs 1.61x | Crossover approaching; D&A +19.2% |
| **Liquidity** | Cash + marketable securities | **~$99,476M** | $43.1B matures within 1 year |
| **Liquidity** | Current / quick ratio | **0.99x / 0.74x** | Structural, not distressed |
| **Leverage** | Total debt + finance leases | **$79,559M** (−$6,373M ytd) | Deleveraging |
| **Leverage** | Net debt | **≈ $(19,900)M — net cash** | Fortress |
| **Leverage** | Gross debt / TTM EBITDA | **~1.08x** | No solvency risk |
| **Leverage** | Interest coverage (9M) | **9.6x** | Interest income now offsets expense |
| **Hidden leverage** | Operating lease liabilities | **$73,902M** (+$4,862M) | Discount rate 2.8% → 3.2% |
| **Obligations** | Total contractual obligations | **$284.4B**; **$35.7B due <12M** | Manageable vs. cash flows |
| **Capital return** | Buybacks, 9M 2023 | **$0** (six straight quarters) | Potential catalyst if authorized |
| **Dilution** | Shares outstanding | **10,330M**, +0.86% in 9M | ~1.1–1.2% annualized |
| **Comp** | SBC, 9M 2023 | **$17,704M** (4.37% of revenue) | +$3,689M yoy; rising as % of revenue |
| **Comp** | Unrecognized RSU cost | **$23,300M** | ~4 quarters of run-rate |
| **Returns** | ROA (TTM) | **4.1%** | — |
| **Returns** | Pre-tax ROIC (TTM, approx.) | **~15.2%** | Strong for the asset base |
| **Efficiency** | Asset turnover (TTM) | **~1.14x** | Negative-working-capital model |
| **Tax** | Effective tax rate | **17.0% (9M) / 18.9% (Q3)** | Up from a 2022 net benefit — EPS headwind |
| **Interest** | 9M interest expense / income | **$2,469M / $2,048M** | Near-neutral; rates now help |
| **Structure** | Operating segments | **3** (confirmed) | Segment detail **not in feed — key gap** |
| **Insider** | Transactions | **DATA UNAVAILABLE** | No authorized archive; no inference made |
| **Next catalyst** | Q4/FY2023 results | Pending (not yet filed at 2024-01-10) | First segment disclosure of the margin story |
| **Comp base** | Q4 2022 operating income (derived) | **~$2.7B (~1.8% margin)** | **Very easy yoy comp** |

---

### Bottom Line

AMZN enters 2024 with the strongest fundamental setup visible in this dataset since 2020: **revenue +11%, gross margin +329 bps, operating income +149%, TTM free cash flow inflected by +$43B, net cash of ~$20B, and debt/EBITDA of ~1.1x.** The story is real and it is measurable in the filings, not just in narrative.

The two things that temper it are both visible in the same data: **the FCF swing is partly manufactured by an 18.9% capex cut against 19.2% D&A growth** (a convergence that mathematically cannot persist), and **SBC of ~$23.6B annualized still exceeds TTM FCF of $16.9B**, meaning fully-loaded free cash flow remains slightly negative. The most important unknown is the **segment split**, which this dataset does not contain — and which the pending Q4/FY2023 10-K will resolve.

**Position for margin durability and FCF trajectory; hedge the capex-reacceleration and expectations risk. Treat the insider signal as unavailable rather than neutral.**