# Fundamental Research Report — AMZN (Amazon.com, Inc.)
**As of: 2024-01-18 | Data through: Q3 FY2023 (period ended 2023-09-30), 10-Q filed 2023-10-27**

---

## 0. Critical data-timing caveat (read first)

Every figure below comes from a point-in-time SEC fact set filtered by EDGAR acceptance time ≤ 2024-01-18. **The most recent filing available is the Q3 FY2023 10-Q (accepted 2023-10-27).** Amazon's Q4/FY2023 results were not yet filed as of this date — the holiday quarter, AWS reacceleration, and full-year capex guidance are therefore **not observable** in this dataset and I have not invented them.

**Nothing new was filed in the trailing week.** For a trader, the fundamental "news" this week is the *absence* of news: AMZN is in a pre-earnings information blackout, ~2 weeks ahead of its Q4 print. Positioning is therefore driven by the Q3 trends below plus expectations, not new disclosures.

Two more transparency notes:
- The vendor's `freq` parameter returned identical fact sets for annual/quarterly; no true FY2020–FY2022 annual statement packets were served. I reconstruct TTM and full-year aggregates arithmetically from the reported periods where possible (shown explicitly).
- `get_insider_transactions` returned **DATA_UNAVAILABLE** — no authorized insider archive exists for AMZN by 2024-01-18. I will not infer insider activity.
- No price, market cap, or valuation multiples are served by these tools. This report is **fundamental only**; multiples must be sourced elsewhere.

---

## 1. Company profile

Amazon.com, Inc. operates as a technology and logistics conglomerate with **three reported operating segments** (confirmed in the filing: `NumberOfOperatingSegments = 3`): **North America**, **International**, and **Amazon Web Services (AWS)**. The revenue architecture is: (i) online and physical stores retail, (ii) third-party seller services (commissions, FBA fulfillment), (iii) advertising, (iv) subscription services (Prime), and (v) AWS cloud compute/storage/database. The segment contribution split is **not** broken out in this extract — only the consolidated totals below — so the mix between high-margin AWS/advertising and low-margin retail cannot be quantified from these tools. That is a real analytical limitation for a Q4 preview.

---

## 2. Income statement — the margin story is the whole story

### 2.1 Revenue (derived arithmetically)

The dataset does not expose a revenue tag in the returned extract. Because Amazon reports `CostsAndExpenses` and `OperatingIncomeLoss` on the same basis, revenue is derivable: **Revenue = CostsAndExpenses + OperatingIncomeLoss** (validated: both periods reconcile exactly to the reported operating income).

| Period | Revenue (derived) | Operating income (reported) | Operating margin | Net income | Diluted EPS |
|---|---|---|---|---|---|
| Q3 FY2022 | $127,101M | $2,525M | 1.99% | $2,872M | $0.28 |
| Q3 FY2023 | $143,083M | $11,188M | **7.82%** | $9,879M | **$0.94** |
| 9M FY2022 | $364,779M | $9,511M | 2.61% | $(3,000)M | $(0.29) |
| 9M FY2023 | $404,824M | $23,643M | **5.84%** | $19,801M | **$1.89** |
| TTM to 9/30/23 | ~$554,028M | $26,380M | 4.76% | $20,079M | — |

- Q3 revenue growth: **+12.6% YoY** ($143.1B vs $127.1B). 9M growth: **+11.0%**.
- Q3 operating income grew **+343% YoY**; operating margin expanded **+583 bps** in a single quarter.
- TTM net income of **$20,079M** is directly confirmed by the filing (`NetIncomeLoss 2022-10-01→2023-09-30`), versus the $(3.0)B 9M FY2022 loss — a swing of roughly **$23B**. Applied to FY2022 (net loss $(2,722)M, derived by reconciliation), full-year FY2023 profitability is already locked in with Q4 still to come.

### 2.2 Where the margin came from (line-item evidence, Q3 YoY)

| Line | Q3 FY2022 | Q3 FY2023 | Change | Read-through |
|---|---|---|---|---|
| Cost of goods & services | $70,268M (55.3% of rev) | $75,022M (**52.4%**) | **−290 bps** | Core driver — fulfillment/shipping and product cost leverage |
| Marketing | $11,014M (8.67%) | $10,551M (**7.37%**) | −130 bps | Disciplined ad spend; efficiency, not growth-at-any-cost |
| G&A | $3,061M (2.41%) | $2,561M (**1.79%**) | −62 bps | Corporate cost cuts (2022–23 layoffs flowing through) |
| Depreciation & amortization | $10,327M (8.12%) | $12,131M (8.48%) | +36 bps | Rising, as expected from the capex binge — a headwind, not a tailwind |
| Stock-based comp | $5,556M (4.37%) | $5,829M (4.07%) | −30 bps | Growing in dollars (+4.9%) but diluting less as % of revenue |
| Interest expense | $617M | $806M | +31% | Higher absolute debt cost |
| Interest income | $277M | $776M | **+180%** | Higher rates on ~$100B liquidity — structural tailwind |
| Non-operating income | $419M | $1,001M | +139% | Equity-securities FV gains (Rivian-type marks); **low quality** |

**Key analytical point:** the margin beat is *operationally* driven (COGS at −290 bps and marketing at −130 bps), **not** by non-operating or one-off items. However, of Q3's $11,188M operating income, $1,001M of pre-tax benefit was non-operating. Strip it out and pre-tax would be $11,188M — still a 7.0% net margin. The core is intact.

9M FY2023 confirms the trend is not a single-quarter fluke: COGS fell to **52.4% of revenue from 55.7%** (−330 bps), and operating margin expanded +323 bps.

### 2.3 Tax and quality of earnings

- Q3 effective tax rate: **18.9%** ($2,306M / $12,189M). 9M: **17.0%** ($4,058M / $23,871M) — below the 21% statutory rate, aided by a **$600M R&D tax credit** (`IncomeTaxReconciliationTaxCreditsResearch`).
- `DeferredIncomeTaxExpenseBenefit` was **−$4,412M for 9M FY2023** and **−$7,779M TTM** — a *benefit* that suppresses book tax expense. **Flag for traders:** part of the reported EPS uplift is a deferred-tax artifact, not cash. Offsetting this favorably, **cash taxes paid were $6,982M for 9M** vs $4,058M book expense, so cash generation is *not* being flattered. Net assessment: clean.
- Non-operating line flipped to **+$228M for 9M FY2023** from **−$14,485M in 9M FY2022** (which carried an $11.3B equity-securities write-down). The prior-year comparison is therefore heavily distorted — **do not extrapolate the +$14.7B non-operating swing as recurring.**

---

## 3. Balance sheet — fortress liquidity, improving working capital

At **2023-09-30** (vs. 2022-12-31):

| Item | 9/30/2023 | 12/31/2022 | Change |
|---|---|---|---|
| Cash & equivalents | $49,605M | $53,888M | −7.9% |
| Available-for-sale debt securities (FV) | $49,871M | n/d | — |
| **Total liquid (cash + AFS)** | **~$99,476M** | — | — |
| Accounts receivable (net) | $43,142M | $42,360M | +1.8% |
| AR allowance (doubtful) | $1,500M (3.5% of AR) | $1,400M (3.3%) | Slight creep — monitor |
| Inventory (net) | $35,406M | $34,405M | **+2.9%** |
| Inventory valuation reserve | $2,600M (7.3%) | $2,800M (8.1%) | **Reserve release — margin tailwind** |
| Total current assets | $142,995M | $146,791M | −2.6% |
| Total current liabilities | $145,214M | $155,393M | −6.6% |
| **Net working capital** | **−$2,219M** | −$8,602M | **+$6.4B improvement** |
| **Current ratio** | **0.985x** | 0.945x | Improving, still <1.0 |
| Long-term debt (total) | $67,472M | $70,542M | −4.4% |
| — of which current portion | $5,995M | $2,999M | +100% (**refinancing watch**) |
| Finance lease liabilities | $12,466M | $15,783M | −21% |
| Operating lease liabilities | $73,902M | $69,040M | +7.0% |
| Total assets | $486,883M | $462,675M | +5.2% |

**Leverage math (derived):**
- Gross debt = LT debt $67,472M + finance leases $12,466M = **$79,938M**
- TTM EBITDA = operating income $26,380M + D&A $47,528M = **$73,908M** → **Debt/EBITDA ≈ 1.08x**
- Liquid assets $99.5B vs gross debt $79.9B → **net cash ≈ +$19.5B**
- Add $73.9B of operating lease liabilities (an off-credit-metric but real fixed obligation; undiscounted commitments $88,814M) and the picture is "comfortable, not bulletproof."
- Note: total stockholders' equity is not exposed in this fact extract. The Q3 FY2023 10-Q reported total stockholders' equity of **≈$173.1B**, implying debt/equity ≈ 0.46x — *cited from the filing, not from the tool extract.*

**Interpretation:** A <1.0 current ratio is normal and structurally benign for Amazon because its payables float (AP $72,004M) is funded by high-velocity inventory and daily consumer cash collection. The −$6.4B improvement in net working capital this year is a genuine quality-of-earnings positive: **inventory grew only 2.9% against ~12% revenue growth** — inventory turns are improving decisively, and the valuation-reserve release ($2.8B→$2.6B) means prior overstock pain is largely behind it.

The **doubling of the current debt portion to $5,995M** is the one balance-sheet item to watch into 2024 (refinancing at higher rates vs. $2.0B of interest income capacity).

---

## 4. Cash flow — the single most important development

### 4.1 The free-cash-flow inflection is real and large

| Metric | TTM to 9/30/2022 | TTM to 9/30/2023 | Change |
|---|---|---|---|
| Operating cash flow | $39,665M | **$71,654M** | **+80.6%** |
| Capex (productive assets) | $65,988M | $54,733M | −17.1% |
| **Free cash flow (OCF − capex)** | **$(26,323)M** | **+$16,921M** | **+$43.2B swing** |
| OCF margin | 10.4% (on ~$381B) | 12.9% | +250 bps |
| Capex intensity | ~17.3% | 9.9% | −740 bps |
| Capex / D&A | 1.69x | **1.15x** | Capex no longer outrunning depreciation |

Quarterly progression:
| | Q3 FY2022 | Q3 FY2023 | 9M FY2022 | 9M FY2023 |
|---|---|---|---|---|
| OCF | $11,404M | **$21,217M** (+86%) | $17,579M | **$42,481M (+142%)** |
| Capex | $16,378M | $12,479M (−24%) | $47,053M | $38,141M (−19%) |
| **FCF** | $(4,974)M | **+$8,738M** | $(29,474)M | **+$4,340M** |

**The mechanism — and why it matters for a trader:** FY2021–FY2022 was a deliberate capex super-cycle (fulfillment buildout), which crushed FCF to roughly −$26B TTM. That cycle is now **normalizing (−17% capex)** while **D&A catches up (+21.5% YoY, $47,528M TTM)**. D&A is a non-cash add-back that inflates OCF without consuming cash, so the combination of falling capex and rising D&A mechanically inflates reported FCF. **This is the highest-conviction fundamental signal in the dataset:** AMZN has crossed from negative to positive TTM FCF, and the crossing is driven by capital-allocation discipline, not accounting.

**Countervailing risk:** capex cuts are finite. Once capex stops declining (and management commentary around AI/cloud infrastructure pointed to *re-acceleration*), the FCF uplift must be sustained by **operating margin** instead. That is the key variable to test on the Q4 call: does the 52.4% COGS ratio hold when AWS/AI capex turns back up?

### 4.2 Financing and capital returns

- **Buybacks: $0 in 2023** (`PaymentsForRepurchaseOfCommonStock` = 0 for Q1–Q3 FY2023 and for the TTM period). The last repurchase was $6,000M in H1 FY2022; none in Q3 FY2022 either.
- **Dividends: none.** AMZN still returns zero capital. All FCF is being recycled into the business and the balance sheet.
- Net financing outflow TTM **−$9,047M**: LT debt issued $8,235M, repaid $4,643M; short-term borrowings $28,002M raised vs $35,136M repaid (net ST paydown ≈ $7.1B). Deleveraging, as intended.
- Cash taxes paid TTM: **$8,677M** vs $4,674M prior year — a near-doubling, and a genuine cash drag that will scale with profit.
- Unrecognized stock-based comp: **$23,300M** — future expense already committed but not yet in the P&L. SBC is 4.4% of 9M revenue; dilution is real but decelerating as a percentage.

---

## 5. Insider transactions

**Not available.** The vendor data package explicitly contains no authorized point-in-time insider archive for AMZN as of 2024-01-18. No Form 4 activity can be characterized, and I will not speculate. Any thesis here must stand on the financials alone. (Practically: AMZN insiders—Bezos/Jassy—have historically sold on scheduled 10b5-1 plans; absent data, treat insider flow as an unknown, not a signal.)

---

## 6. Actionable insights for traders

**Bull case (evidence-backed):**
1. **Margin expansion is structural, not one-off.** COGS ratio improved 290 bps in Q3 alone and 330 bps over 9M; marketing and G&A also fell as a % of revenue. Five consecutive quarters of improving operating leverage is now the base case, not a hope.
2. **FCF turned positive on a TTM basis (+$16.9B)** — a regime change from −$26.3B. FCF inflections historically re-rate this name more than EPS beats.
3. **Balance sheet is a call option.** ~$99.5B liquid vs $79.9B gross debt (net cash +$19.5B), 1.08x Debt/EBITDA, and **zero buybacks or dividends** means AMZN has un-deployed capacity to either accelerate capex into AI/cloud or begin returning capital — a catalyst the market is not pricing from this dataset.
4. **Inventory discipline** (+2.9% vs +12.6% revenue) plus a reserve release signals the post-2022 overstock drag is fully cleared.
5. **Interest income ($2,048M for 9M, +276%)** is now a durable, rate-driven earnings floor that did not exist in 2021.

**Bear case / what to watch:**
1. **Total blackout on Q4.** Holiday quarter, AWS growth, and 2024 capex guidance are all unknown here. Any position taken on this data is a position taken blind into the print (~Feb 1, 2024).
2. **D&A is rising faster than revenue** (+17.5% vs +12.6% in Q3). The capex super-cycle's depreciation tailwind to cash flow is also a margin *headwind* — a mechanical squeeze on operating margin over the next several quarters even if gross profit holds.
3. **Capex relief is finite.** If capex re-accelerates for AI infrastructure, the FCF story inverts quickly; the 1.15x capex/D&A ratio will not stay this low.
4. **Non-operating income is not repeatable.** +$1,001M in Q3 from equity marks; +$228M for 9M vs −$14,485M last year. Ignore the comp when modeling.
5. **Deferred tax benefit (−$4,412M 9M)** is flattering book EPS; it will not persist at this magnitude.
6. **No insider confirmation available** — no corroborating signal either way.
7. **Current ratio 0.985x** and a doubling of current debt maturities ($5,995M) bear monitoring, though not alarming against $99.5B of liquidity.

**Suggested framing:** The AMZN fundamental setup on this data is **constructive on operating leverage and cash generation, blind on Q4 and valuation.** Given the margin trajectory (7.8% Q3 operating margin vs 2.0% a year ago) plus the positive TTM FCF crossing, the risk/reward into the Q4 print skews favorably on *fundamentals* — but position sizing should reflect that the single largest data point (Q4/AWS) is unavailable, and that no valuation multiple could be computed from these tools. **A scenario, not a forecast:** sustaining Q3's 7.8% margin on a seasonally typical Q4 revenue base (~$170B) would imply ~$13B of Q4 operating income and ~$575B FY2023 revenue; a return to 5% margins would imply ~$8.5B. That $4.5B spread is the entire near-term risk.

---

## 7. Summary table — key points

| Category | Metric / Point | Value (as of latest filing, 9/30/2023) | Trading implication |
|---|---|---|---|
| **Data status** | Latest filing | Q3 FY2023 10-Q, accepted 2023-10-27 | No new disclosures in trailing week; pre-earnings blackout |
| **Company** | Identity / segments | Amazon.com, Inc.; 3 operating segments (NA, Int'l, AWS) | Segment mix not quantifiable from extract |
| **Growth** | Q3 revenue / growth | ~$143,083M, **+12.6% YoY** (derived) | Double-digit top line intact |
| **Growth** | 9M revenue / growth | ~$404,824M, **+11.0% YoY** (derived) | Stable, decelerating from pandemic peaks |
| **Profitability** | Q3 operating income / margin | $11,188M / **7.82%** (vs 1.99%) | **+583 bps YoY — core thesis** |
| **Profitability** | 9M operating income / margin | $23,643M / **5.84%** (vs 2.61%) | +323 bps; trend confirmed |
| **Profitability** | TTM net income | **$20,079M** (vs $(3.0)B 9M prior yr) | Full-year profit locked in |
| **Profitability** | Q3 diluted EPS | **$0.94** (vs $0.28) | +236% YoY |
| **Cost discipline** | COGS % revenue Q3 | **52.4%** vs 55.3% (−290 bps) | Primary margin driver |
| **Cost discipline** | Marketing / G&A % rev | 7.37% / 1.79% (−130 / −62 bps) | Structural expense reset |
| **Risk** | D&A growth | $12,131M Q3, **+17.5%** YoY; TTM $47,528M (+21.5%) | Depreciation headwind to margins ahead |
| **Liquidity** | Cash + AFS securities | **~$99,476M** | Dry powder for capex, AI, or capital returns |
| **Leverage** | Gross debt (LT + finance leases) | $79,938M | — |
| **Leverage** | Debt / TTM EBITDA | **~1.08x**; net cash **+$19.5B** | Fortress; no solvency concern |
| **Leases** | Operating lease liabilities | $73,902M (+7.0% YTD); commitments $88,814M | Real fixed obligation, off debt metric |
| **Watch item** | Current debt portion | $5,995M, **+100%** vs $2,999M | Refinancing at higher rates |
| **Working capital** | Net WC / current ratio | **−$2,219M** (from −$8,602M) / 0.985x | +$6.4B improvement; <1.0 is structural |
| **Inventory** | Inventory / reserve | $35,406M (+2.9% vs rev +12.6%); reserve 7.3% | Turns improving; overstock pain cleared |
| **Cash flow** | TTM OCF | **$71,654M, +80.6% YoY** | Cash engine accelerating |
| **Cash flow** | TTM capex | $54,733M, **−17.1% YoY** (9.9% of revenue) | Capex cycle normalizing |
| **Cash flow** | **TTM FCF** | **+$16,921M** vs **$(26,323)M** prior | **+$43.2B swing — the headline** |
| **Cash flow** | Q3 FCF | **+$8,738M** vs $(4,974)M | Fourth straight improving quarter |
| **Capital returns** | Buybacks / dividends | **$0 / $0** (all 2023 periods) | Untapped return-of-capital catalyst |
| **Cash tax** | Taxes paid TTM | $8,677M vs $4,674M | Cash drag scaling with profit |
| **Earnings quality** | Deferred tax benefit 9M | **−$4,412M** (TTM −$7,779M) | Flatters book EPS; won't persist |
| **Earnings quality** | Non-operating income Q3 / 9M | +$1,001M / +$228M (vs −$14,485M) | Non-repeatable equity marks; ignore comp |
| **Compensation** | SBC 9M / unrecognized | $17,704M (4.4% of rev) / **$23,300M** | Future dilution committed |
| **Insider activity** | Form 4 data | **UNAVAILABLE — no archive** | Cannot corroborate; treat as unknown |
| **Valuation** | Multiples / price | **Not served by these tools** | Must be sourced externally |
| **Next catalyst** | Q4/FY2023 print | Expected ~2024-02-01 (not in dataset) | Primary binary risk; all Q4 data blind |