# AMZN — Amazon.com, Inc. | Fundamental Research Report
**Analysis date:** 2024-01-26 | **Latest public filing in data package:** Form 10-Q for period ended 2023-09-30 (accepted 2023-10-27, 02:36 UTC)

---

## 0. Data provenance & caveats (read first)

| Item | Status |
|---|---|
| Filing basis | Q3 FY2023 10-Q (period ended 2023-09-30) + prior-year comparable columns; 6M-2023 comparatives from the Q2 10-Q (filed 2023-08-04) |
| Point-in-time filter | All facts were public on/before 2024-01-26 (verified by EDGAR acceptance timestamps) — **no look-ahead** |
| Q4 FY2023 results | **Not yet public** as of 2024-01-26 (no 8-K/10-K in package). Q4 print is the dominant near-term catalyst and is entirely un-reflected in these numbers |
| Revenue tag | The `Revenues`/`RevenueFromContractWithCustomer` tags were not returned in this vendor extract. **Revenue below is *derived*** as `CostsAndExpenses + OperatingIncomeLoss`, which reconciles exactly to Amazon's income-statement arithmetic (Net sales − Total operating expenses = Operating income). Flagged as (D) throughout |
| Segment detail | Only `NumberOfOperatingSegments = 3` (North America / International / AWS) returned; no segment P&L in extract |
| Stockholders' equity / retained earnings | Tag set truncated before `StockholdersEquity`; equity level not directly available. Components APIC, common stock, AOCI available |
| Insider transactions | **DATA_UNAVAILABLE** — vendor has no authorized point-in-time insider archive for AMZN. No inference made or fabricated |
| Price / valuation multiples | Not in the fundamental package — no P/E, EV/EBITDA or market-cap math is asserted |

---

## 1. Company profile

Amazon.com, Inc. (AMZN) is a global technology and e-commerce conglomerate operating **three reportable segments** (confirmed: `NumberOfOperatingSegments = 3`):

1. **North America** — online and physical retail, third-party seller services (1P + 3P marketplace), advertising, Prime subscription, logistics-as-a-service.
2. **International** — the same retail/marketplace/advertising model across non-US geographies (EUR, JPY, GBP, INR exposure — visible in FX translation losses).
3. **Amazon Web Services (AWS)** — cloud compute, storage, database, and a fast-growing AI/ML infrastructure layer; AWS is the primary profit and capex engine.

Structural characteristics visible directly in the filings:
- **Negative working-capital business model**: 92.6 days of payables vs 29.3 days of receivables + 45.6 days of inventory → **cash conversion cycle ≈ −17.7 days**. Suppliers fund the retail flywheel.
- **Heavy fixed-asset and lease intensity**: $54.7B TTM capex; $73.9B operating lease liability + $12.5B finance lease liability; 88.8B of undiscounted future operating-lease payments.
- **Large non-operating investment book**: $49.9B available-for-sale debt securities plus equity stakes marked to fair value (Rivian-type marks drove −$11.3B in 9M22, +$2.4B swing items in Q3 23).
- **Three-year shareholder-return posture**: $6.0B of buybacks executed in H1 2022, then **$0 in every quarter from Q3 2022 through Q3 2023** (confirmed: `PaymentsForRepurchaseOfCommonStock = 0` for Q3'22, Q4'22, Q1'23, Q2'23, Q3'23).

---

## 2. Income statement — the margin story is the whole story

### Q3 FY2023 (Jul–Sep) vs Q3 FY2022

| $M | Q3 2023 | Q3 2022 | Δ % |
|---|---:|---:|---:|
| Revenue (D) | **143,083** | **127,101** | **+12.6%** |
| Cost of goods & services | 75,022 | 70,268 | +6.8% |
| **Gross profit (D)** | **68,061** | **56,833** | **+19.8%** |
| Gross margin (D) | **47.6%** | **44.7%** | +287 bps |
| Marketing | 10,551 | 11,014 | **−4.2%** |
| G&A | 2,561 | 3,061 | **−16.3%** |
| Total costs & expenses | 131,895 | 124,576 | +5.9% |
| **Operating income** | **11,188** | **2,525** | **+343%** |
| Operating margin | **7.82%** | **1.99%** | +583 bps |
| Interest expense | 806 | 617 | +30.6% |
| Interest & investment income | 776 | 277 | +180% |
| Non-operating income, net | 1,001 | 419 | +139% |
| Pre-tax income | 12,189 | 2,944 | +314% |
| Tax | 2,306 | 69 | ETR 18.9% vs 2.3% |
| **Net income** | **9,879** | **2,872** | **+244%** |
| Net margin | 6.90% | 2.26% | +464 bps |
| **Diluted EPS** | **$0.94** | **$0.28** | +236% |
| Diluted shares (implied) | ~10,509M | ~10,257M | +2.5% |
| D&A | 12,131 | 10,327 | +17.5% |
| Stock-based comp | 5,829 | 5,556 | +4.9% |

### Nine months FY2023 vs Nine months FY2022

| $M | 9M 2023 | 9M 2022 | Δ % |
|---|---:|---:|---:|
| Revenue (D) | **404,824** | **364,779** | **+11.0%** |
| COGS | 212,186 | 203,191 | +4.4% |
| Gross profit (D) | 192,638 | 161,588 | +19.2% |
| Gross margin (D) | 47.6% | 44.3% | +329 bps |
| Total costs & expenses | 381,181 | 355,268 | +7.3% |
| **Operating income** | **23,643** | **9,511** | **+149%** |
| Operating margin | **5.84%** | **2.61%** | +323 bps |
| Interest expense | 2,469 | 1,673 | +47.6% |
| Investment income | 2,048 | 544 | +276% |
| Non-operating income/(expense) | **+228** | **−14,485** | n/m (equity marks) |
| Pre-tax income | 23,871 | (4,974) | n/m |
| Tax | 4,058 | (1,990) | ETR 17.0% |
| **Net income** | **19,801** | **(3,000)** | n/m |
| Net margin | 4.89% | (0.82%) | +571 bps |
| **Diluted EPS** | **$1.89** | **$(0.29)** | n/m |
| D&A | 34,843 | 29,236 | +19.2% |
| SBC | 17,704 | 14,015 | **+26.3%** |
| Marketing | 31,468 | 29,420 | +7.0% |
| G&A | 8,806 | 8,558 | +2.9% |

**Interpretation / actionable read-throughs**

1. **Revenue growth accelerated modestly (11.0% 9M → 12.6% in Q3 alone), while total cost growth decelerated (7.3% → 5.9%).** That combination is why Q3 operating income grew 343% off a 12.6% revenue base. The Q3 exit-rate operating margin of 7.8% is the single most important number in the package — it is roughly 2.5x the 9M average and implies the margin ramp steepened sequentially through 2023.
2. **The margin is *self-help*, not price.** COGS fell 480 bps as a share of revenue (55.3% → 52.4% in Q3) while marketing (−4.2% y/y) and G&A (−16.3% y/y) were cut outright. This is regionalization/fulfilment-cost efficiency plus headcount discipline — levers that are already in the reported numbers, which is a higher-quality signal than a purely mix-driven beat.
3. **Watch SBC: +26.3% y/y in 9M23 vs revenue +11.0%.** Stock comp is growing faster than the business and faster than cash opex. $23.3B of unrecognized SBC cost remains to be expensed (from the 10-Q). This is real dilution: shares outstanding rose 10,242M → 10,330M (+0.86% in 9 months) and diluted count rose ~2.5% y/y. GAAP EPS is flattered less than the opex cuts imply; adjusted-margin bulls should haircut for this.
4. **Net interest is no longer a headwind — it flipped to a tailwind.** Q3 interest income $776M nearly offsets $806M of interest expense (net cost $30M vs $340M a year ago). With $99.5B of cash + marketable securities and declining debt, investment income is now a structural earnings contributor (~$2.0B in 9M23 vs $544M).
5. **Non-operating noise is large.** 9M22 included −$11.3B of equity-securities fair-value losses (mark-to-market on growth-equity stakes); 9M23 has +$1.0B gains plus +$1.0B of AFS unrealized gains. Exclude both when modeling — the operating line is the clean signal.
6. **Tax rate normalized to ~17–19%.** After a 2022 tax *benefit*, AMZN is now a full cash taxpayer: $6.98B of cash taxes paid in 9M23 vs $4.34B in 9M22, and $8.68B TTM. Rising cash taxes are a genuine FCF drag to keep in mind for 2024.

---

## 3. Cash flow — the FCF inflection is the strongest fundamental in the dataset

### Trailing-twelve-months (2022-10-01 → 2023-09-30), with the prior TTM as comparison

| $M (TTM) | TTM to 9/30/2023 | TTM to 9/30/2022 | Δ |
|---|---:|---:|---:|
| **Operating cash flow** | **71,654** | **39,665** | **+80.6%** |
| Capex (productive assets) | 54,733 | 65,988 | **−17.1%** |
| **Free cash flow (OCF − capex)** | **+16,921** | **−26,323** | **+43,244** |
| Investing cash flow | (48,053) | (39,360) | −8,693 |
| Financing cash flow | (9,047) | +6,532 | −15,579 |
| FX effect | +349 | (1,836) | +2,185 |
| Net change in cash | +14,903 | +5,001 | +9,902 |
| Net income (TTM) | 20,079 | 11,323 | +77.3% |
| D&A (TTM) | 47,528 | 39,103 | +21.5% |
| Deferred tax (TTM) | (7,779) | (8,404) | — |

### Nine months FY2023 vs FY2022

| $M | 9M 2023 | 9M 2022 |
|---|---:|---:|
| Operating cash flow | **42,481** | **17,579** (+141.7%) |
| Capex | 38,141 | 47,053 (−18.9%) |
| **FCF** | **+4,340** | **(29,474)** |
| Investing | (37,232) | (26,780) |
| Financing | (9,133) | +9,632 |
| LT debt issued / repaid | 0 / 3,386 | 12,931 / 1 |
| ST debt proceeds / repayments | 17,395 / 19,339 | 30,946 / 21,757 |
| **Share repurchases** | **0** | 6,000 |
| Operating lease payments | 7,687 | 6,268 |
| Finance lease principal | 3,605 | 6,301 |

### Q3 FY2023 standalone

| $M | Q3 2023 | Q3 2022 |
|---|---:|---:|
| Operating cash flow | **21,217** | 11,404 |
| Capex | 12,479 | 16,378 |
| **FCF** | **+8,738** | **(4,974)** |
| Financing | (8,948) | +3,016 |
| Net change in cash | +14 | (2,522) |

**Interpretation**

- **The FCF swing is ~$43B in one year** (−$26.3B → +$16.9B TTM). Two engines: OCF +$32B and capex −$11.3B. Q3 alone generated $8.7B of FCF versus a $5.0B outflow a year earlier.
- **Capex discipline is deliberate and quantified**: 9M23 capex of $38.1B is 18.9% below 9M22's $47.1B, and the TTM capex/D&A ratio is 1.15x — i.e., AMZN is now roughly maintaining, not aggressively out-building, its asset base. **Risk:** the eventual re-acceleration of AI/cloud capex (AWS) is the single biggest lever that could reverse the FCF story. Q4 guidance/2024 capex commentary is the key unknown at this date.
- **Quality check on OCF**: OCF is *not* being propped up by working capital. Both `IncreaseDecreaseInAccruedLiabilities` (−$9.0B) and `IncreaseDecreaseInAccountsReceivableAndOtherOperatingAssets` (−$10.4B drag) were *negative* contributors in 9M23, while AP fell $79.6B → $72.0B. **Cash earnings, not balance-sheet stretching, drove the increase.** That is a high-quality print.
- **Deferred tax of −$7.8B TTM flatters OCF** (non-cash; the add-back exceeds the tax expense). Strip it and the OCF improvement is smaller but still large.
- **No capital returns.** Despite $16.9B TTM FCF and buyback authorization, repurchases were $0 for five straight quarters. Cash went to debt reduction and liquidity. If Q4 confirms FCF durability, the buyback restart is an obvious, un-priced optionality.

---

## 4. Balance sheet — de-risking, with a lease-heavy liability structure

| $M | 2023-09-30 | 2022-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 49,605 | 53,888 | −7.9% |
| AFS marketable securities (FV) | 49,871 | n/a in extract | — |
| Accounts receivable | 43,420 | 42,360 | +2.5% |
| Inventory | 35,406 | 34,405 | +2.9% |
| **Total current assets** | **142,995** | **146,791** | **−2.6%** |
| **Total assets** | **486,883** | **462,675** | **+5.2%** |
| Accounts payable | 72,004 | 79,600 | −9.5% |
| Accrued liabilities | 58,812 | 62,566 | −6.0% |
| Contract liabilities (deferred revenue) | 16,098 (14,398 cur + 2,700 non-cur) | 16,127 | −0.2% |
| **Total current liabilities** | **145,214** | **155,393** | **−6.6%** |
| Long-term debt (total) | 67,472 (5,995 cur + 61,098 non-cur) | 70,542 | −4.4% |
| Finance lease liabilities | 12,466 (2,385 cur + 10,081 non-cur) | 15,783 | −21.0% |
| Operating lease liabilities | 73,902 (8,092 cur + 65,810 non-cur) | 69,040 | +7.1% |
| Additional paid-in capital | 92,711 | 75,066 | +23.5% |
| AOCI | (5,003) | (4,487) | −11.5% |
| Shares outstanding | 10,330M | 10,242M | +0.86% |
| Inventory valuation reserves | 2,600 | 2,800 | −7.1% |
| Allowance for doubtful AR | 1,500 | 1,400 | +7.1% |

**Derived liquidity & leverage metrics**

| Metric | 2023-09-30 | 2022-12-31 | Read |
|---|---:|---:|---|
| Current ratio | **0.985x** | 0.945x | Improving, still <1.0 (normal for AMZN) |
| Working capital | **−$2,219M** | −$8,602M | Deficit narrowed 74% |
| Cash + AFS securities | **$99,476M** | — | 20.4% of total assets |
| Total debt incl. finance leases | **$79,938M** | $86,325M | −7.4% |
| **Net cash position** | **+$19,538M** | — | Net *cash*, not net debt |
| Cash + securities / current liabilities | 68.5% | — | Strong short-term coverage |
| Operating lease asset (ROU) | 70,758 | 66,123 | +7.0% |

**Interpretation**

- **The balance sheet is now net-cash-positive.** $67.5B of funded debt plus $12.5B of finance leases against $99.5B of cash and AFS securities implies ~$19.5B of net cash — a decisive shift from the levered 2022 position. Funded debt fell $3.1B and finance leases fell $3.3B in nine months, and **no new long-term debt was issued in 2023** (`ProceedsFromIssuanceOfLongTermDebt = 0` for 9M23 and Q3'23).
- **Current liabilities shrinking 6.6% while current assets fell only 2.6% is the working-capital release that helped OCF.** But note AP −9.5% and accrued −6.0% mean AMZN paid suppliers faster / accrued less — a *sustainable* choice only if cash generation holds. If Q4 revenue re-accelerates, AP will have to rebuild, creating an OCF headwind.
- **The real obligation is leases, not bonds.** Undiscounted operating-lease payments total **$88.8B** (vs. $73.9B on balance sheet; $14.9B of undiscounted interest), plus $14.6B undiscounted finance leases. **Total contractual obligations: $284.4B**, of which only **$35.7B is due in the next twelve months** and $8.9B in the remainder of FY2023. Weighted-average operating-lease discount rate rose 2.8% → 3.2%, a mild headwind for new leases.
- **Deferred revenue is flat ($16.1B) and $10.9B of it was recognized as revenue in 9M23** — Prime/ subscription demand is stable, not accelerating, on this metric.
- **APIC +$17.6B in nine months against $17.7B of SBC expense** confirms the equity build is entirely compensation-driven; there is no equity issuance. AOCI worsened $516M on FX translation (−$738M in 9M23) — a small dollar-strength drag.
- **Equity level:** `StockholdersEquity` was not returned in this extract. Don't rely on ROE from this package; use ROA instead: TTM net income $20,079M / total assets $486,883M ≈ **4.1% ROA** (vs ~2.4% a year earlier).

---

## 5. Efficiency & unit economics (derived)

| Metric (9M FY2023, 273 days) | Value | Formula |
|---|---:|---|
| Days sales outstanding | **29.3 days** | AR 43,420 / daily revenue 1,483 |
| Days inventory outstanding | **45.6 days** | Inv 35,406 / daily COGS 777 |
| Days payables outstanding | **92.6 days** | AP 72,004 / daily COGS 777 |
| **Cash conversion cycle** | **−17.7 days** | DSO + DIO − DPO |
| Operating leverage | Revenue +11.0% vs total costs +7.3% | +370 bps of spread |
| Capex / D&A (TTM) | 1.15x | Maintenance-mode investment |
| Interest coverage (9M, EBIT/interest) | **9.6x** | 23,643 / 2,469 (was 5.7x) |
| Implied diluted shares (9M) | ~10,477M | 19,801 / 1.89 |
| Inventory reserve / inventory | 7.3% | 2,600 / 35,406 (down from 8.1%) |

The declining inventory reserve ratio and 2.9% inventory growth against 11% revenue growth confirm AMZN is **not stuffing the channel** — inventory turns improved, which supports the gross-margin expansion as genuine rather than provision-release-driven.

---

## 6. Fundamental scorecard: what is bullish, what is at risk

**Bullish (evidence-backed)**
1. Operating margin expanded **+583 bps y/y in Q3** to 7.82%; 9M margin 5.84% vs 2.61%.
2. **FCF swung +$43.2B TTM** to +$16.9B; Q3 FCF +$8.7B vs −$5.0B.
3. **OCF +80.6% TTM** with negative working-capital contributions — high earnings quality.
4. **Net cash position of ~$19.5B**; funded debt −$3.1B and finance leases −$3.3B in 9 months; zero new LT debt in 2023.
5. **Capex −18.9% y/y** while revenue +11.0% — capital intensity falling.
6. Gross margin +329 bps with no inventory-provision release (reserves down).
7. Net interest cost collapsed to ~$30M in Q3 from $340M; $2.0B of investment income in 9M23.
8. Negative cash conversion cycle (−17.7 days) still funds growth at zero cost.
9. **$0 buybacks for five quarters** = un-deployed balance sheet capacity and latent EPS support if FCF persists.

**Bearish / risks (evidence-backed)**
1. **SBC +26.3% y/y**, ~2.5x revenue growth; **$23.3B of unrecognized SBC yet to be expensed**; diluted shares +2.5% y/y.
2. **Capex re-acceleration risk** (AWS/AI): the entire FCF story rests on $54.7B TTM capex staying low. Any 2024 capex guide-up reverses it.
3. **Cash taxes rising**: $6.98B in 9M23 vs $4.34B; 17.0% ETR now a permanent FCF drag vs the 2022 tax benefit.
4. **Working capital is a source that can reverse**: AP −$9.5%, accrued liab −$6.0% y/y; a revenue re-acceleration forces AP rebuild and an OCF drag.
5. **Revenue growth still low-double-digit** (11.0% 9M, 12.6% Q3) — the multiple depends on AWS re-acceleration, which **cannot be verified** from this package (no segment data).
6. **Obligation wall of $284.4B** total contractual commitments; $88.8B undiscounted operating leases; discount rate up 2.8% → 3.2%.
7. **Deferred revenue flat y/y** ($16.1B) — subscription/marketplace backlog not building.
8. **Non-operating earnings are mark-to-market and volatile** (equity gains/losses: −$11.3B in 9M22, +$2.4B in Q3 23) — a repeat of 2022 would dent EPS even with operations intact.
9. **FX drag persists**: −$738M translation in 9M23, AOCI worsened $516M.

---

## 7. Positioning framework for traders (as of 2024-01-26)

- **The setup is a "margin-and-FCF-inflection" trade, not a growth trade.** Reported data support paying for durable ~7–8% operating margins and a real FCF number, not for a return to 20%+ revenue growth.
- **Event risk is imminent and asymmetric to the *guidance*, not the quarter.** Fiscal Q4 2023 (the holiday quarter) results were not public on 2024-01-26. Every number in this report is a Q3 exit-rate. A Q4 beat with 2024 capex guided higher is the classic "good quarter, bad tape" outcome for AMZN; a Q4 beat with capex held near $55B and a buyback restart is the bull case.
- **Key monitoring items for the next print:** (a) 2024 capex guide vs the $54.7B TTM run-rate; (b) AWS margin and growth (unavailable here); (c) SBC growth vs revenue; (d) AP/accrual rebuild as a working-capital swing; (e) cash tax rate trend; (f) any resumption of `PaymentsForRepurchaseOfCommonStock`.
- **Quality of earnings is good but not pristine** — price it as ~$17B FCF with a −$7.8B deferred-tax add-back and +~$24B of SBC removed from OCF. Fully-loaded owner earnings run well below headline FCF.
- **Balance-sheet optionality is genuine**: ~$19.5B net cash plus $99.5B gross liquidity against $35.7B of near-term obligations gives management room for buybacks, debt paydown, or a capex surge without financing risk.

---

## 8. Key data summary table

| Category | Metric | Value | Period | Signal |
|---|---|---|---|---|
| **Scale** | Revenue (D) | $143,083M | Q3 FY23 | +12.6% y/y |
| | Revenue (D) | $404,824M | 9M FY23 | +11.0% y/y |
| | Segments | 3 (NA / Intl / AWS) | — | Segment P&L not in package |
| **Profitability** | Gross margin (D) | 47.6% | Q3 FY23 | vs 44.7% (+287 bps) |
| | Operating income | $11,188M | Q3 FY23 | +343% y/y |
| | Operating margin | 7.82% | Q3 FY23 | vs 1.99% (+583 bps) |
| | Operating margin | 5.84% | 9M FY23 | vs 2.61% (+323 bps) |
| | Net income | $9,879M | Q3 FY23 | +244% y/y |
| | Net income | $19,801M | 9M FY23 | vs $(3,000)M |
| | Net margin | 4.89% | 9M FY23 | vs (0.82%) |
| | Diluted EPS | $0.94 / $1.89 | Q3 / 9M FY23 | vs $0.28 / $(0.29) |
| | Effective tax rate | 18.9% / 17.0% | Q3 / 9M FY23 | Normalized, cash taxpayer |
| **Cash generation** | Operating cash flow | $21,217M / $42,481M / $71,654M | Q3 / 9M / TTM | TTM +80.6% y/y |
| | Capex | $12,479M / $38,141M / $54,733M | Q3 / 9M / TTM | TTM −17.1% y/y |
| | **Free cash flow** | **$8,738M / $4,340M / $16,921M** | Q3 / 9M / TTM | TTM swing +$43.2B |
| | Deferred tax add-back | $(7,779)M | TTM | Inflates OCF |
| | Cash taxes paid | $6,982M / $8,677M | 9M / TTM | Up from $4,340M |
| | Buybacks | **$0** | 5 straight quarters | Capital return paused |
| **Balance sheet** | Total assets | $486,883M | 9/30/23 | +5.2% YTD |
| | Cash + AFS securities | $99,476M | 9/30/23 | 20.4% of assets |
| | Funded debt | $67,472M | 9/30/23 | −$3.1B YTD; $0 issued in '23 |
| | Finance leases | $12,466M | 9/30/23 | −21.0% YTD |
| | Operating leases | $73,902M | 9/30/23 | +7.1% YTD; $88.8B undiscounted |
| | **Net cash / (debt)** | **+$19,538M** | 9/30/23 | Net cash positive |
| | Current ratio | 0.985x | 9/30/23 | vs 0.945x |
| | Working capital | $(2,219)M | 9/30/23 | Deficit −74% YTD |
| | Cash conversion cycle | −17.7 days | 9M FY23 | Supplier-funded model |
| | Total contractual obligations | $284,407M | 9/30/23 | $35.7B due <12 months |
| | Shares outstanding | 10,330M | 9/30/23 | +0.86% YTD dilution |
| **Cost structure** | Stock-based comp | $5,829M / $17,704M | Q3 / 9M | +26.3% y/y in 9M |
| | Unrecognized SBC | $23,300M | 9/30/23 | Future expense overhang |
| | D&A | $12,131M / $34,843M | Q3 / 9M | +19.2% y/y in 9M |
| | Marketing | $10,551M | Q3 | −4.2% y/y (discipline) |
| | G&A | $2,561M | Q3 | −16.3% y/y (discipline) |
| | Interest expense / income | $806M / $776M | Q3 | Near-zero net interest cost |
| | Interest coverage | 9.6x | 9M FY23 | vs 5.7x |
| | ROA (TTM NI / assets) | 4.1% | TTM | vs ~2.4% prior TTM |
| **Non-operating** | Equity securities FV gain/(loss) | +$1,200M / +$1,000M | Q3 / 9M | vs −$11,300M in 9M22 |
| | AFS unrealized gain | +$1,196M | Q3 | vs +$1,039M |
| **Data gaps** | Insider transactions | **UNAVAILABLE** | — | No authorized archive; not inferred |
| | Q4 FY23 results | **NOT PUBLIC** | — | Dominant near-term catalyst |
| | Segment revenue/op income | **NOT IN EXTRACT** | — | AWS mix unverifiable |
| | Stockholders' equity / retained earnings | **NOT IN EXTRACT** | — | Use ROA, not ROE |
| | Price / valuation multiples | **NOT IN PACKAGE** | — | No P/E or EV/EBITDA asserted |

---

### Bottom line for the desk
AMZN's reported fundamentals through Q3 FY2023 describe a **completed cost-efficiency cycle, not a still-improving one**: operating margin tripled to 7.8%, TTM FCF swung $43B into positive territory, and the balance sheet flipped to ~$19.5B net cash with zero new long-term debt. The offsets are equally concrete — SBC compounding at 26%, a $23.3B unrecognized comp overhang, a capex trough that is a *choice* rather than a structural decline, rising cash taxes, and no capital returns for five quarters. **Everything material hinges on the Q4 FY2023 print and its 2024 capex framework, neither of which is in this data package.** Trade the confirmed margin/FCF inflection; do not underwrite an AWS re-acceleration or a buyback that the filings do not yet evidence.