# AMZN — Fundamental Research Report
**Company:** Amazon.com, Inc. (AMZN)
**Analysis date:** 2024‑01‑05 (point‑in‑time)
**Latest financials available:** Q3 FY2023 (period ended 2023‑09‑30), 10‑Q accepted **2023‑10‑27** (`0001018724-23-000018`)

---

## 1. Methodology & Data Provenance (read first)

All figures below are pulled from point‑in‑time SEC facts filtered by **actual EDGAR acceptance time** as of 2024‑01‑05. This has three important consequences for a trader:

1. **Q4 FY2023 / full‑year 2023 results do not exist yet.** Amazon typically reports Q4 in early February; as of today the most recent hard filing is the Q3 10‑Q from 2023‑10‑27. Anyone quoting "FY2023 revenue of $575B" today is using *forward* information. This report stays strictly at Q3'23 and prior.
2. **There have been no new filings in the past week.** The fundamental picture is static versus the last ~10 weeks; the next fundamental catalyst is the Q4 print (historically the first week of February).
3. The tool's tag output is **truncated on revenue lines**, so I **derived revenue arithmetically** where needed: `Revenue = CostsAndExpenses + OperatingIncomeLoss`. This reconciles exactly to reported figures (e.g., Q3'23: $131,895M + $11,188M = **$143,083M**; 9M'23: $381,181M + $23,643M = **$404,824M**). Items I could not source from the toolset are explicitly flagged. **Insider transactions were unavailable** (vendor has no authorized point‑in‑time insider archive for AMZN) — I did not infer or fabricate any insider activity.

---

## 2. Company Profile & Business Model

Amazon is the world's largest e‑commerce and cloud infrastructure company, reporting **three operating segments** (confirmed: `NumberOfOperatingSegments = 3` in the 10‑Q):

| Segment | What it is | Economics |
|---|---|---|
| **North America** | Retail, marketplace, ads, Prime, devices, logistics | Low‑margin, now inflecting positive on cost discipline |
| **International** | Same, ex‑North America | Historically loss‑making, approaching breakeven |
| **AWS** | Cloud compute/storage/database/AI (EC2, S3, SageMaker, Bedrock, Trainium/Inferentia) | The profit engine — structurally 25‑30% operating margins |

The key structural insight: **consolidated profitability is a tug‑of‑war between AWS margin dollars and retail margin drag.** Advertising (high margin, largely inside NA/Intl) is the second profit pillar and is the primary driver of the enormous segment margin swing shown below.

---

## 3. Income Statement: The Margin Inflection Is Real and Large

Derived figures (USD millions; revenue derived as Costs + Operating Income):

| | Q3'23 | Q3'22 | Δ y/y | 9M'23 | 9M'22 | Δ y/y |
|---|---:|---:|---:|---:|---:|---:|
| **Revenue (derived)** | **143,083** | **127,101** | **+12.6%** | **404,824** | **364,779** | **+11.0%** |
| Cost of goods & services | 75,022 | 70,268 | +6.8% | 212,186 | 203,191 | +4.4% |
| **Gross profit** | **68,061** | **56,833** | **+19.8%** | **192,638** | **161,588** | **+19.2%** |
| **Gross margin** | **47.6%** | 44.7% | +290 bp | **47.6%** | 44.3% | +330 bp |
| Marketing | 10,551 | 11,014 | −4.2% | 31,468 | 29,420 | +7.0% |
| G&A | 2,561 | 3,061 | −16.3% | 8,806 | 8,558 | +2.9% |
| Total costs & expenses | 131,895 | 124,576 | +5.9% | 381,181 | 355,268 | +7.3% |
| **Operating income** | **11,188** | **2,525** | **+343%** | **23,643** | **9,511** | **+149%** |
| **Operating margin** | **7.8%** | 2.0% | +584 bp | **5.8%** | 2.6% | +323 bp |
| D&A | 12,131 | 10,327 | +17.5% | 34,843 | 29,236 | +19.2% |
| Stock‑based comp | 5,829 | 5,556 | +4.9% | 17,704 | 14,015 | +26.3% |
| Interest expense | 806 | 617 | +30.6% | 2,469 | 1,673 | +47.6% |
| Investment income | 776 | 277 | +180% | 2,048 | 544 | +276% |
| Non‑operating income/(expense) | 1,001 | 419 | — | 228 | (14,485) | n/m |
| Pre‑tax income | 12,189 | 2,944 | +314% | 23,871 | (4,974) | n/m |
| Tax | 2,306 | 69 | — | 4,058 | (1,990) | — |
| **Net income** | **9,879** | **2,872** | **+244%** | **19,801** | **(3,000)** | **n/m** |
| **Diluted EPS** | **$0.94** | $0.28 | +236% | **$1.89** | $(0.29) | n/m |

**What the trader should take away:**

- **Revenue growth re‑accelerated to +12.6% y/y** in Q3'23 from ~+11% in the first half. This is not a cost‑only story — unit growth plus advertising plus AWS re‑acceleration all contributed.
- **The cost structure is the story.** Total costs grew +5.9% against revenue +12.6% → ~670 bp of negative expense leverage in one quarter. This is the payoff from the 2022‑23 fulfillment‑network regionalization, headcount reductions, and the ~$40B+ of cost actions management flagged through 2023.
- **G&A down 16.3% y/y** is a direct fingerprint of the corporate headcount cuts — a one‑time level reset, not a repeatable annual tailwind.
- **SBC growth (+26% for 9M) is nearly 2.5x revenue growth** — real dilution, but comparatively modest against a $1.5T equity base. Note `EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized = $23.3B` at 9/30/23, which is embedded future expense and a permanent governance/quality irritant.
- **D&A is growing ~19%, faster than revenue** — the 2020‑22 capex wave is now hitting the P&L. This is the single biggest headwind to further margin expansion in 2024 and is why AWS margins matter more than retail margins from here.
- **Interest expense nearly doubled y/y** ($1.67B→$2.47B for 9M) as the 2022 debt issuance repriced higher; this is now largely offset by **$2.05B of investment income** earned on the ~$99B cash/securities pile. Net interest is roughly neutral — a quiet but meaningful improvement versus 2022.
- **The 2022 base was distorted** by **−$11.3B** of equity‑securities fair‑value losses (Rivian) and **−$11.5B** of marketable‑securities unrealized losses in 9M'22. By contrast, 9M'23 includes a **+$1.0B** equity gain (Q3 alone: +$1.2B). **Strip these out and the underlying improvement is still dramatic** — operating income is the clean proof, not net income.

**Effective tax rate:** 18.9% in Q3'23, 17.0% for 9M'23 — normalized and sustainable near the high‑teens/low‑20s. No tax‑rate tailwind left to lean on.

---

## 4. Cash Flow: The Most Important Line in the Whole Report

**Trailing twelve months (Oct 1, 2022 – Sep 30, 2023):**

| Metric | TTM | 9M'23 | 9M'22 |
|---|---:|---:|---:|
| Operating cash flow | **71,654** | 42,481 | 17,579 |
| Capex (`PaymentsToAcquireProductiveAssets`) | **(54,733)** | (38,141) | (47,053) |
| **Free cash flow** | **16,921** | **4,340** | **(29,474)** |
| Investing cash flow | (48,053) | (37,232) | (26,780) |
| Financing cash flow | (9,047) | (9,133) | +9,632 |
| Net change in cash | +14,903 | (4,172) | (1,299) |

**Q3'23 alone:** OCF $21,217M vs $11,404M (+86% y/y); capex $12,479M vs $16,378M (−24%); **Q3 FCF $8,738M**.

**Why this matters more than EPS:**
- Amazon swung from **−$29.5B FCF in 9M'22 to +$4.3B in 9M'23** — a ~$34B swing in nine months. On a TTM basis FCF is **+$16.9B** versus deeply negative a year prior. This is the single cleanest evidence that the "growth‑at‑all‑cost" era ended.
- **Capex is being cut, not just optimized:** 9M'23 capex $38.1B vs $47.1B (−18.9%), and capex intensity fell from **12.9% of revenue to 9.4%**. Management signaled a lower 2023/2024 capex envelope, redirecting spend toward AI infrastructure.
- **Operating cash flow is up 142% y/y for 9M** — driven by profit, but note it is *helped* by working capital: `IncreaseDecreaseInAccruedLiabilities` was **−$9.0B** (a drag) while receivables/other assets were a **+$10.4B** contributor. Some of this is real cash conversion quality (AP discipline, inventory velocity); some is timing that can reverse in Q4. Watch AP: **$72.0B at 9/30/23 vs $79.6B at 12/31/22 — a $7.6B decline** that *helped* near‑term FCF but signals less supplier‑financing cushioning ahead.

---

## 5. Balance Sheet: Strong, Liquid, and Deleveraging

| USD millions | 2023‑09‑30 | 2022‑12‑31 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 49,605 | 53,888 | −4,283 |
| Marketable securities (AFS, fair value) | 49,871 | n/a (tag truncated) | — |
| **Cash + securities** | **~99,476** | ~94,000 (approx.) | +~5,500 |
| Accounts receivable, net | 43,420 | 42,360 | +1,060 |
| Inventory, net | 35,406 | 34,405 | +1,001 |
| **Total current assets** | **142,995** | **146,791** | −3,796 |
| **Total assets** | **486,883** | **462,675** | +24,208 |
| Accounts payable | 72,004 | 79,600 | −7,596 |
| Accrued liabilities | 58,812 | 62,566 | −3,754 |
| **Total current liabilities** | **145,214** | **155,393** | −10,179 |
| Long‑term debt (noncurrent) | 61,098 | 67,150 | −6,052 |
| Long‑term debt (current) | 5,995 | 2,999 | +2,996 |
| **Total debt** | **67,093** | **70,149** | −3,056 |
| Operating lease liabilities | 73,902 | 69,040 | +4,862 |
| Finance lease liabilities | 12,466 | 15,783 | −3,317 |
| Additional paid‑in capital | 92,711 | 75,066 | +17,645 |
| AOCI | (5,003) | (4,487) | −516 |
| Shares outstanding | 10,330 | 10,242 | +88 |

**Liquidity / solvency read‑through:**

- **Net cash ex‑leases: +$32.4B** (cash + securities − debt). Even including **$86.4B** of lease obligations, leverage is low relative to ~$78B annualized EBITDA‑equivalent.
- **Current ratio is 0.985x** — technically below 1.0. Do **not** read this as distress: Amazon's current liabilities are dominated by non‑interest‑bearing payables and accrued expenses, and its $99B securities portfolio is largely short‑duration liquid (43.1B of AFS matures within one year). It is a deliberate, structurally negative working‑capital model.
- **Refinancing ladder is light:** contractual obligations due in the next twelve months of **$35.7B**, second year $28.4B, third year $23.8B, against $99B of liquidity and ~$71B TTM OCF. No liquidity event risk.
- **Equity is being built the right way:** APIC rose **$17.6B in nine months** (stock issuance/comp), while AOCI worsened only $0.5B. Book value ≈ **$17–18/share** (derived).
- **Deleveraging is genuine:** total debt down $3.1B and finance leases down $3.3B while the cash/securities pile grew — a rare combination of FCF generation *and* balance‑sheet repair.

---

## 6. Capital Allocation: The Signal Is the Absence of Buybacks

| USD millions | 9M'23 | 9M'22 | TTM (Oct'22–Sep'23) |
|---|---:|---:|---:|
| Share repurchases | **0** | **6,000** | **0** |
| Long‑term debt issued | 0 | 12,931 | 8,235 |
| Long‑term debt repaid | (3,386) | (1) | (4,643) |
| Short‑term debt proceeds | 17,395 | 30,946 | 28,002 |
| Short‑term debt repayments | (19,339) | (21,757) | (35,136) |
| Commercial paper/ST net | (1,944) | +9,189 | (7,134) |
| Financing cash flow | **(9,133)** | +9,632 | (9,047) |

- **Zero buybacks for four consecutive quarters** after $6.0B in H1'22. Capital is being recycled into **capex (AI/AWS/logistics) and debt reduction**, not shareholder returns. Amazon pays no dividend.
- **Short‑term debt is being actively wound down**: TTM gross ST borrowings of $28.0B against $35.1B of repayments. The ~$17.4B of 9M'23 ST issuance against $19.3B of repayments reflects normal commercial‑paper churn, not new leverage.
- Net implication: **share count will keep creeping up via SBC (~+88M shares in 9 months, ~1.0% annualized dilution)** — modest, but it means per‑share metrics lag consolidated growth by roughly a point.

---

## 7. Operating Quality Checks

| Check | Evidence | Verdict |
|---|---|---|
| Gross margin trend | 44.3% → 47.6% y/y (9M) | ✅ Durable mix shift toward ads/AWS/3P fees |
| Opex discipline | Costs +5.9% vs revenue +12.6% (Q3) | ✅ Genuine, but G&A reset is one‑time |
| D&A trajectory | +19% y/y, faster than revenue | ⚠️ Structural headwind into 2024 |
| Working capital | Accrued liab **−$9.0B** drag; AR/other **+$10.4B** benefit | ⚠️ Mixed; not all repeatable |
| Receivables quality | Allowance $1.5B on $43.4B AR (3.5%); AR +2.5% vs revenue +12.6% | ✅ Conservative, DSO improving |
| Inventory | $35.4B, +2.9% y/y vs revenue +12.6%; reserves **cut** $2.8B→$2.6B | ✅ Right‑sized, healthy turns (~8x) |
| Payables | AP −$7.6B since year‑end | ⚠️ Supplier terms tightening / cash‑paid earlier |
| Contract liabilities (backlog proxy) | Current $14.4B (from $13.2B); **$10.9B** of 9M revenue recognized from opening balance | ✅ Healthy AWS/Prime prepaid pipeline |
| Impairments | $0.42B 9M'23 vs $0.35B 9M'22 | ✅ De minimis |
| Diluted vs basic EPS gap | $1.89 vs $1.93 (2.1% dilution) | ⚠️ Manageable |

---

## 8. Valuation Context

⚠️ **The toolset contains no market‑price, estimate, or consensus data.** The ratios below use an **assumed reference price of ~$145** (approximate AMZN level in early January 2024) purely to make the fundamentals comparable to a trading decision — **verify the price independently before acting.**

- Shares outstanding: **10.330B** (10.334B as of 2023‑10‑18) → implied market cap ≈ **$1.50T**
- Net cash: **+$32.4B** → implied EV ≈ **$1.47T**
- TTM net income **$20.1B** → **P/E ≈ 75x**
- TTM FCF **$16.9B** → **P/FCF ≈ 89x**
- Annualized 9M'23 EBITDA ($58.5B × 4/3 ≈ $78.0B) → **EV/EBITDA ≈ 18.8x**
- Annualized 9M'23 diluted EPS ($1.89 × 4/3 ≈ $2.52) → **~57x** (Q4 is seasonally the strongest quarter, so a full‑year figure in the high‑$2s to ~$3 is a reasonable build)

**Interpretation:** Amazon is *not* cheap on trailing earnings or trailing FCF — it is priced for **continuation of the margin ramp**, not for the current numbers. The bull case requires FCF to roughly double again in FY2024 as capex stays contained and operating margin holds ≥6%. The bear case is simply that a ~19x EV/EBITDA multiple on peak‑cycle margin momentum leaves no room for a capex re‑acceleration (AI arms race) or an AWS growth wobble. **This is a momentum/estimate‑revision stock, not a value stock.**

---

## 9. Insider Transactions

**DATA_UNAVAILABLE.** The configured vendor has no authorized, point‑in‑time insider‑transactions archive for AMZN as of 2024‑01‑05. No insider buying or selling data was retrieved, and **no inference or estimate should be drawn** from its absence. Treat insider sentiment as unknown for this analysis; do not let it factor into sizing.

---

## 10. Upcoming Catalysts & What Would Change the Thesis

| Date / Window | Event | Why it matters |
|---|---|---|
| **~Early Feb 2024** | **Q4 FY2023 + full‑year results** | The dominant near‑term catalyst. Watch: (1) AWS y/y growth re‑acceleration, (2) Q4 operating margin ≥ Q3's 7.8%, (3) FY2024 capex guide, (4) holiday retail/AWS backlog |
| Ongoing | AWS AI demand (Bedrock, Trainium/Inferentia), Anthropic relationship | Determines whether AWS re‑accelerates to mid‑teens growth |
| Ongoing | Advertising growth & margin mix | The quiet second profit engine; drives NA segment margin |
| Ongoing | Prime/retail unit economics, fulfillment regionalization completion | Whether the ~$40B cost actions are durable or one‑time |
| Risk | FTC antitrust litigation, EU DMA/regulatory actions | Tail risk to marketplace fee take rate |
| Risk | Capex re‑acceleration for AI infrastructure | Directly compresses FCF; the market's biggest fear given today's 89x P/FCF |

---

## 11. Actionable Conclusions

**BULL (base case, supported by the data):** The fundamental inflection is documented and broad‑based. Revenue growth accelerated to +12.6%, gross margin expanded 290 bp, operating income more than quadrupled y/y in Q3, and FCF swung ~$34B in nine months to +$16.9B TTM. The balance sheet carries **+$32.4B net cash** and is actively deleveraging. Momentum in reported fundamentals is *positive and accelerating* — a rare combination to bet against ahead of a seasonally strong Q4 print.

**BEAR (also supported):** Valuation already discounts the ramp (~75x trailing earnings, ~89x trailing FCF, ~19x EV/EBITDA). **D&A is growing ~19% vs revenue ~13%**, SBC is +26%, capex cuts are the main FCF lever (finite), G&A savings are non‑recurring, and payables fell $7.6B — three of the four FCF drivers are one‑time in nature. A single quarter of capex re‑acceleration or AWS deceleration would compress the multiple hard.

**Highest‑conviction, evidence‑based views:**
1. **The margin story is real, not accounting.** Operating income is the proof ($23.6B vs $9.5B, 9M) and is *not* contaminated by the 2022 Rivian mark‑to‑market noise. **Buy the fundamental trend.**
2. **FCF is the metric to trade, not EPS.** Track `OCF − capex` quarterly. 9M'23 FCF of $4.3B with Q3 alone at $8.7B means Q4 will be the swing factor; a strong Q4 could put full‑year FCF near $30B+.
3. **Position ahead of, or wait for, the early‑February print.** With no new filings since 2023‑10‑27, there is no informational edge in the interim. Event risk is symmetric and the valuation gives no cushion — **size accordingly, or express the view around the print rather than weeks before it.**
4. **The single number to watch in the Q4 release: FY2024 capex guidance.** It is the highest‑leverage variable for the stock. Capex held ≤$50B → FCF re‑rating and multiple support. Capex guided to $60B+ → FCF math breaks at this multiple.
5. **Do not use insider activity as an input** — no data exists in this dataset.

---

## 12. Key Points Summary

| Category | Metric | Value | Read |
|---|---|---|---|
| **Latest filing** | Form / period / accepted | 10‑Q, Q3 FY23 (2023‑09‑30), accepted 2023‑10‑27 | No new filing in past week; Q4 due ~early Feb 2024 |
| **Scale** | Revenue Q3'23 / 9M'23 (derived) | $143.1B / $404.8B | +12.6% / +11.0% y/y |
| **Growth** | Revenue y/y acceleration | Q3 +12.6% vs H1 ~+11% | ✅ Re‑accelerating |
| **Margins** | Gross margin 9M'23 vs 9M'22 | 47.6% vs 44.3% | ✅ +330 bp |
| **Margins** | Operating margin Q3'23 vs Q3'22 | 7.8% vs 2.0% | ✅ +584 bp |
| **Profitability** | Operating income 9M'23 / Q3'23 | $23.6B / $11.2B | +149% / +343% y/y |
| **Profitability** | Net income 9M'23 vs 9M'22 | $19.8B vs −$3.0B | ✅ Full swing |
| **EPS** | Diluted Q3'23 / 9M'23 | $0.94 / $1.89 | vs $0.28 / −$0.29 |
| **Cash generation** | TTM OCF / capex / FCF | $71.7B / −$54.7B / **+$16.9B** | ✅ FCF positive vs −$29.5B 9M'22 |
| **Capex discipline** | Capex 9M'23 vs 9M'22 | $38.1B vs $47.1B (−18.9%) | Intensity 12.9%→9.4% of revenue |
| **Liquidity** | Cash + securities | ~$99.5B | +$32.4B net of $67.1B debt |
| **Leverage** | Total debt | $67.1B (from $70.1B) | ✅ Deleveraging |
| **Liquidity ratio** | Current ratio | 0.985x | Structurally negative WC; not distress |
| **Returns to holders** | Buybacks 9M'23 / dividend | $0 / none | Capital → capex & debt paydown |
| **Dilution** | Shares out | 10.330B (+88M in 9M) | ~1% SBC dilution; $23.3B unrecognized comp |
| **Cost tailwinds** | G&A y/y Q3 | −16.3% | ⚠️ One‑time headcount reset |
| **Cost headwinds** | D&A y/y / SBC y/y (9M) | +19.2% / +26.3% | ⚠️ Both outgrowing revenue |
| **Working capital** | AP change since 12/31/22 | −$7.6B | ⚠️ Supplier financing cushion shrinking |
| **Backlog proxy** | Contract liabilities current | $14.4B (from $13.2B); $10.9B recognized YTD | ✅ Healthy |
| **Valuation (approx.)** | P/E TTM / P/FCF TTM / EV/EBITDA | ~75x / ~89x / ~19x | ⚠️ Priced for margin ramp; no cushion |
| **Insider activity** | — | **DATA UNAVAILABLE** | Do not infer or use |
| **Key catalyst** | Q4 FY23 + FY24 capex guide | ~Early Feb 2024 | The highest‑leverage variable for the stock |
| **Verdict** | Fundamental trend / valuation | Improving & accelerating / demanding | **Constructive fundamentally; size for event & multiple risk** |

---
*Caveats: (1) Revenue, gross profit, and revenue‑based ratios were **derived** as CostsAndExpenses + OperatingIncomeLoss, which reconciles exactly to reported totals. (2) FY2022 full‑year totals and Q4'22 standalone revenue/operating income are **not present** in this point‑in‑time tag set (they were filed in the Feb‑2023 10‑K), so full‑fiscal‑year comparisons are omitted rather than reconstructed. (3) All valuation ratios use an **assumed ~$145 reference price**; the toolset provides no market price, consensus, or estimate data — verify independently. (4) Insider transaction data was unavailable and was not estimated.*