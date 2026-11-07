# AMZN — Fundamental Research Report (as of 2024‑01‑04)

**Instrument:** AMZN — Amazon.com, Inc.
**Data basis:** Point‑in‑time SEC facts with EDGAR acceptance timestamps ≤ 2024‑01‑04. Every figure below is traceable to a filing accepted on or before that date.

> **Critical point‑in‑time caveat:** The most recent filing visible as of 2024‑01‑04 is the **Q3 2023 10‑Q (filed/accepted 2023‑10‑27, accn 0001018724‑23‑000018)**. Q4/FY2023 results (announced early Feb 2024) are **not** in the dataset. Any analysis of "the last week" therefore reflects a quiet filing window — no new financial statements, no 8‑K, and **no insider‑transaction archive is available** for AMZN in this data package.

---

## 1. Executive summary — what the numbers say

AMZN's fundamentals are in the middle of a **violent, verifiable profitability inflection**, and the balance sheet has simultaneously de‑risked. Three facts dominate:

1. **Operating leverage is real and large.** Q3 2023 operating income was **$11.19B (7.8% margin)** vs **$2.53B (2.0%)** in Q3 2022 — a **+343% YoY** increase on only **+12.6%** revenue growth. Nine‑month 2023 operating income of **$23.64B** already beat the **full‑year 2022** total (derived TTM $26.4B vs FY22 $12.2B).
2. **Free cash flow inflected by ~$34B in nine months.** 9M 2023 FCF = **+$4.34B** vs **–$29.47B** in 9M 2022, driven by OCF of **$42.48B (+142% YoY)** *and* capex cut to **$38.14B (–19% YoY)**. TTM FCF = **+$16.9B**.
3. **The balance sheet is now net cash.** Cash + marketable securities **$99.5B** vs long‑term debt **$67.1B** + finance leases **$12.5B** = **~$20B net cash**, with equity up **25%** since 2022 year‑end to **~$183B** and **zero** share repurchases / **zero** new long‑term debt issued in 2023.

The bear counter‑point is equally specific: the margin expansion is **cost‑driven, not mix‑driven**, FCF is still only **3.1% of TTM revenue**, the **current ratio is 0.98** (current liabilities exceed current assets), stock‑based comp is **accelerating (+26% YoY)**, and **purchase obligations of $284.4B** sit off‑balance‑sheet. The Q4 print ~5 weeks out is the binary event.

---

## 2. Company profile and business model

Amazon.com, Inc. operates three reportable segments — the 10‑Q explicitly tags `NumberOfOperatingSegments = 3` — conventionally North America, International, and Amazon Web Services, plus material "other" revenue lines (advertising, subscription services, third‑party seller services) that are disclosed but are not broken out in the tag set returned here.

Structural characteristics visible in the *reported* data:

- **Scale with thin net margins but enormous gross cash generation.** 9M 2023 revenue $404.8B produced net income $19.8B (4.9% net margin) yet **operating cash flow of $42.5B** — i.e. OCF ran at **2.15x net income** because non‑cash depreciation and amortization is **$34.8B** for nine months (**$47.5B TTM**).
- **Asset‑heavy, lease‑heavy fulfillment/cloud model.** Operating lease liabilities **$73.9B**; finance lease liabilities **$12.5B**; operating lease ROU assets **$70.8B**; finance lease ROU assets (pre‑amortization) **$62.7B**. Depreciation + finance‑lease ROU amortization are the dominant non‑cash charges.
- **Scale‑driven working capital machine, currently unwinding.** Accounts payable fell to **$72.0B** (from $79.6B at 12/31/22) and accrued liabilities to **$58.8B** (from $62.6B) — a genuine cash headwind inside the 9M 2023 cash flow statement (see §6).
- **Share‑based compensation is a first‑order cost.** $17.70B in 9M 2023 (4.4% of revenue), 10‑Q‑disclosed **unrecognized** SBC of **$23.3B**.

**Company financial history (from filings in the dataset):** FY2022 was the trough — 9M 2022 revenue $364.8B, operating income $9.51B (2.6%), **net loss –$3.0B**, EPS –$0.29, distorted by a **–$14.49B non‑operating loss** (mark‑to‑market on equity securities, largely Rivian) and a **–$11.3B equity‑securities FV loss**. 2023 flipped the sign on both operating and non‑operating lines: 9M 2023 non‑operating income **+$0.23B**, with Q3 2023 alone **+$1.00B** including **+$1.20B** of equity‑securities gains.

---

## 3. Income statement deep dive (Q3 2023 + 9M 2023 + TTM)

Revenue is not returned as a standalone `Revenues` tag in this extract, but is **exactly derivable** as `CostsAndExpenses + OperatingIncomeLoss` (verified against reported figures):

| $ millions | Q3 2023 | Q3 2022 | Δ | 9M 2023 | 9M 2022 | Δ | TTM (Q4'22–Q3'23) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | 143,083 | 127,101 | +12.6% | 404,824 | 364,779 | +11.0% | 554,028 |
| Cost of goods & services | 75,022 | 70,268 | +6.8% | 212,186 | 203,191 | +4.4% | n/a |
| **Gross margin %** | 47.6% | 44.7% | +2.9pp | 47.6% | 44.3% | +3.3pp | n/a |
| Marketing | 10,551 | 11,014 | –4.2% | 31,468 | 29,420 | +7.0% | n/a |
| G&A | 2,561 | 3,061 | –16.3% | 8,806 | 8,558 | +2.9% | n/a |
| Total costs & expenses | 131,895 | 124,576 | +5.9% | 381,181 | 355,268 | +7.3% | n/a |
| **Operating income** | **11,188** | **2,525** | **+343%** | **23,643** | **9,511** | **+149%** | **26,380** |
| **Operating margin** | **7.82%** | **1.99%** | +5.83pp | **5.84%** | **2.61%** | +3.23pp | **4.76%** |
| Interest expense | 806 | 617 | +30.6% | 2,469 | 1,673 | +47.6% | ~3,163 |
| Investment income | 776 | 277 | +180% | 2,048 | 544 | +276% | ~2,493 |
| Non‑operating income/(expense) | 1,001 | 419 | +139% | 228 | (14,485) | n/m | n/m |
| Pre‑tax income | 12,189 | 2,944 | +314% | 23,871 | (4,974) | n/m | n/a |
| Income tax | 2,306 | 69 | n/m | 4,058 | (1,990) | n/m | n/a |
| **Net income** | **9,879** | **2,872** | **+244%** | **19,801** | **(3,000)** | n/m | **20,079** |
| **Diluted EPS** | **$0.94** | **$0.28** | +236% | **$1.89** | –$0.29 | n/m | **~$1.91** |
| Diluted shares (implied) | ~10,510 | ~10,257 | +2.5% | ~10,476 | ~10,345 | +1.3% | ~10,510 |

**Key reads:**

- **Margin expansion is cost‑side, and broad‑based.** COGS grew **+4.4%** against **+11.0%** revenue (330bp of gross‑margin expansion). Marketing actually *declined* **–4.2%** YoY in Q3. G&A fell **–16.3%** in Q3. Total costs grew **+7.3%** vs revenue **+11.0%** — a 370bp operating‑leverage tailwind, the single most important number in this report.
- **Sequential momentum, not a one‑off.** 9M operating margin of 5.84% contains Q3 at 7.82%, implying H1 2023 was roughly **4.9%** — so Q3 was the best quarter of the year and the trend is upward, not a base effect.
- **Interest is now essentially neutral.** 9M 2023 interest expense $2.47B vs investment income $2.05B → **net interest cost only ~$420M**, versus net cost ~$1.13B in 9M 2022. Higher rates are helping the $99.5B securities pile faster than they hurt the fixed‑rate debt.
- **Tax rate normalized.** 9M 2023 effective rate **17.0%** ($4.06B on $23.87B pre‑tax) vs a **benefit** in 2022. Cash taxes paid rose to **$6.98B** from $4.34B. Future EPS growth will carry a real tax load — model 17–21%, not the 2022 anomaly.
- **Quality of the non‑operating line has improved but is still mark‑to‑market noise.** Q3 2023's +$1.00B included **+$1.20B** of equity‑securities FV gains and **–$94M** FX. Traders should strip **+$1.2B** (≈**$0.09–0.11 of EPS**) from Q3 as non‑recurring.

---

## 4. Cost structure and the "why" of the margin story

The dataset quantifies three levers:

1. **Fulfillment/network efficiency:** COGS intensity fell from 55.7% of revenue (9M 2022) to **52.4%** (9M 2023).
2. **Discretionary spend discipline:** marketing down to **7.8%** of revenue (from 8.1%) and, in Q3 alone, down **–4.2%** in absolute dollars while revenue grew 12.6%.
3. **Headcount/overhead leverage:** G&A down **–16.3%** YoY in Q3 and **–$500M** absolute; asset impairment charges of only **$420M** in 9M 2023 vs $350M prior year, and a **$200M** contract‑termination loss vs **$300M** — i.e. the 2022–23 restructuring charges are largely behind.

**Depreciation is the swing factor to watch:** D&A rose to **$34.84B (9M 2023)** from $29.24B (+19%), and TTM D&A is **$47.53B**. Capex cuts reduce *cash* outflows immediately but depreciation keeps rising — meaning **reported operating margin flatters the cash story less than the OCF story flatters reported EPS**. This is why OCF (+142%) outran net income (+244% off a negative base).

**SBC: the dilution tax.** 9M 2023 SBC **$17.70B** (+26.3% YoY) = **4.4% of revenue** and **89% of net income**. Non‑vested unrecognized SBC is **$23.3B**. Diluted share count rose **+2.5%** YoY in Q3 (basic EPS $0.96 vs diluted $0.94). This is a recurring, real economic cost that optically inflates operating margin (SBC sits inside COGS/opex).

---

## 5. Balance sheet and solvency (as of 2023‑09‑30)

| $ millions | 2023‑09‑30 | 2022‑12‑31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 49,605 | 53,888 | –7.9% |
| Marketable securities (AFS, FV) | 49,871 | n/a in extract | — |
| **Cash + securities** | **~99,476** | — | — |
| Accounts receivable, net | 43,420 | 42,360 | +2.5% |
| Inventory, net | 35,406 | 34,405 | +2.9% |
| **Current assets** | **142,995** | **146,791** | –2.6% |
| **Total assets** | **486,883** | **462,675** | +5.2% |
| Accounts payable | 72,004 | 79,600 | –9.5% |
| Accrued liabilities | 58,812 | 62,566 | –6.0% |
| Current portion of LTD | 5,995 | 2,999 | +99.9% |
| Finance lease liability – current | 2,385 | 4,397 | –45.8% |
| **Current liabilities** | **145,214** | **155,393** | –6.6% |
| Long‑term debt (noncurrent) | 61,098 | 67,150 | –9.0% |
| Finance lease liability – noncurrent | 10,081 | 11,386 | –11.5% |
| Operating lease liability (total) | 73,902 | 69,040 | +7.0% |
| Deferred revenue – current | 14,398 | 13,227 | +8.9% |
| **Total stockholders' equity (derived from components)** | **~182,973** | **146,043** | **+25.3%** |

**Solvency / leverage diagnostics (computed):**

- **Net cash position: ~+$20.0B** (cash + securities $99.5B minus LTD $67.1B minus finance leases $12.5B). Even on a strict debt basis AMZN is **net cash**, which is unusual for a company carrying $74B of lease liabilities.
- **Gross debt + finance leases / equity: 43.5%** ($79.6B / $183.0B).
- **Lease‑adjusted gross obligations: ~$153.5B** including $73.9B operating leases — still only ~0.28x TTM revenue and ~2.1x TTM EBITDA.
- **EBITDA (TTM): ~$73.9B** (op income $26.4B + D&A $47.5B). **Net debt / EBITDA is negative**; **interest coverage ~8.3x** on TTM interest of ~$3.16B.
- **Current ratio 0.98** — technically below 1.0. In Amazon's case this is a function of a payables‑funded model, not distress, but it means liquidity is a "flow" story (quarterly OCF of $21.2B) rather than a "stock" cushion story.
- **Inventory efficiency improving:** inventory up only **+2.9%** against **+11.0%** revenue growth, with valuation reserves *reduced* to **$2.60B** from $2.80B and doubtful‑account allowance stable at $1.5B. No hidden inventory/credit deterioration.
- **Deferred revenue (contract liabilities)** rose to **$14.40B** current / $2.70B non‑current; **$10.9B** of prior deferred revenue was recognized in 9M 2023 — a forward‑demand signal tied to AWS/subscriptions.

**Off‑balance‑sheet:** **purchase obligations of $284.4B** at 9/30/2023, with **$35.71B due in the next twelve months** and **$8.91B in the remainder of FY2023**. This is enormous relative to equity and is the main structural commitment risk (cloud/content capacity contracts). It is *not* debt, but it is contractual.

**Near‑term maturities are trivially covered:** LTD current $5.99B + finance leases $2.18B (next 12m) + operating leases $9.98B (next 12m) ≈ **$18.2B** against **$99.5B** of cash/securities.

---

## 6. Cash flow — the real inflection

| $ millions | Q3 2023 | Q3 2022 | 9M 2023 | 9M 2022 | TTM Q3'23 | TTM Q3'22 |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash flow | 21,217 | 11,404 | 42,481 | 17,579 | **71,654** | 39,665 |
| Capex (productive assets) | 12,479 | 16,378 | 38,141 | 47,053 | **54,733** | 65,988 |
| **Free cash flow** | **8,738** | **(4,974)** | **4,340** | **(29,474)** | **16,921** | **(26,323)** |
| Investing cash flow | (11,753) | (15,608) | (37,232) | (26,780) | (48,053) | (39,360) |
| Financing cash flow | (8,948) | 3,016 | (9,133) | 9,632 | (9,047) | 6,532 |
| SBC (non‑cash add‑back) | 5,829 | 5,556 | 17,704 | 14,015 | 23,155 | — |
| D&A (non‑cash add‑back) | 12,131 | 10,327 | 34,843 | 29,236 | 47,528 | 39,103 |

**What moved OCF from $17.6B to $42.5B (9M YoY):** net income swung **+$22.8B** and D&A added **+$5.6B**, which *more than offset* a **$9.0B** accrued‑liability drag, a **$10.4B** receivables/other‑asset drag, and a **$7.6B** payables decline. In other words: **the earnings recovery, not working capital, drove the OCF surge** — a higher‑quality composition. If payables/accruals stabilize or rebuild in 2024, OCF gets a *second* leg.

**What moved FCF by +$33.8B:** **+$24.9B** from OCF and **+$8.9B** from lower capex. **The capex cut is a one‑time lever that cannot repeat.** This is the single most important forward risk: 2024 AI/datacenter build‑out re‑acceleration would compress FCF even while earnings rise.

**Cash conversion diagnostics:** TTM OCF/net income **3.57x**; TTM FCF/revenue **3.1%**; TTM FCF/net income **0.84x**. FCF is improving but still **thin** relative to a $554B revenue base and $20.1B of net income — AMZN is not yet a cash‑cow, it is a cash‑*im*proving story.

---

## 7. Capital allocation and financing

- **No buybacks.** `PaymentsForRepurchaseOfCommonStock` = **$0** in Q3 2023, 9M 2023, and all of FY-to-date 2023 — versus **$6.0B** in 9M 2022. Buyback capacity remains unused (a latent EPS lever if ever activated).
- **Debt reduction, not issuance.** 9M 2023: **$0** proceeds from long‑term debt (vs $12.93B in 9M 2022); **$3.39B** LTD repaid; **$19.34B** short‑term repaid vs **$17.40B** drawn (net –$1.94B). TTM proceeds from LT debt $8.24B all occurred in Q4 2022.
- **Finance leases shrinking:** liabilities down to $12.47B from $15.78B; principal payments $3.61B in 9M 2023 and $5.25B TTM — an actual *cash* outflow, unlike operating leases.
- **M&A minimal:** `PaymentsToAcquireBusinessesNetOfCashAcquired` only appears in the June‑2023 filing ($3.83B 1H 2023, $5.55B trailing twelve months to 6/30/23) — i.e., bolt‑ons (One Medical/roomba‑scale), not transformative deals.
- **Net effect:** AMZN is self‑funding, deleveraging, and accumulating cash. Equity rose **+$36.9B** in nine months (retained earnings + APIC from SBC).

---

## 8. Insider transactions

**Not available.** The vendor explicitly returned `DATA_UNAVAILABLE` — there is **no authorized point‑in‑time insider‑transaction archive for AMZN as of 2024‑01‑04**. I will not infer, estimate, or fabricate insider buying/selling. Treat the absence of insider data as a genuine information gap for this report, and do not read the silence as either bullish or bearish.

---

## 9. Actionable insights for traders

**Bull case (evidence‑backed):**
1. **Operating margin is inflecting faster than revenue** — 7.82% in Q3 vs 1.99% a year ago; 5.84% for 9M. Every 100bp of margin on a ~$570B annualized revenue base is worth **~$5.7B** of operating income. Consensus underestimation of margin durability is the primary upside risk for shorts.
2. **The FCF story has genuinely turned** — 9M FCF +$4.3B vs –$29.5B; TTM $16.9B; Q3 alone $8.7B. FCF inflections of this shape historically re‑rate the multiple before EPS revisions fully catch up.
3. **Balance sheet is net cash** (~$20B) with **interest coverage 8.3x**, no new debt issued in 2023, and buyback capacity entirely unused.
4. **Working capital is a coiled spring** — payables –$7.6B and accrued –$3.8B since 12/31/22 are *already* absorbed in the OCF figures; stabilization in 2024 would add incremental OCF on top of earnings.
5. **Non‑operating drag is gone** — the –$14.5B equity‑mark loss in 9M 2022 has flipped to +$0.2B, removing a huge YoY EPS comparison distortion (headline EPS growth is "real" this year).

**Bear case / risk checklist (evidence‑backed):**
1. **The capex lever is exhausted.** 9M capex $38.1B is already –19% YoY and TTM is $54.7B. If 2024 capex re‑accelerates for AI infrastructure, **TTM FCF of $16.9B can compress quickly** — FCF is only 3.1% of revenue, so a $10B capex swing is ~60% of TTM FCF.
2. **Depreciation is still compounding** (+19% YoY to $34.8B) — future margin math gets harder as the asset base depreciates.
3. **SBC +26% YoY ($17.7B, 89% of net income), $23.3B unrecognized** — dilution of ~1–2.5%/yr and an embedded margin cost.
4. **Current ratio 0.98** and **$284.4B of purchase obligations** ($35.7B within 12 months) mean the model depends on continuous cash generation; a demand shock would hit liquidity optics hard.
5. **Margin expansion is cost‑cut‑led, not mix‑led.** Cost discipline has a ceiling; revenue growth of +11–12.6% must hold to keep the operating‑leverage flywheel turning.
6. **Tax normalization** — 17% effective rate now vs a benefit in 2022 — is a permanent headwind to EPS growth rates.
7. **Timing risk:** the Q4/FY2023 print (~early Feb 2024) is the first test of whether Q3's 7.8% margin and $8.7B FCF were structural. Positioning into that event on the basis of Q3 data alone is event risk.

**Specific metrics to monitor in the next filing:**
- **Operating margin ≥6.5%** for Q4 (i.e., no margin give‑back on the holiday quarter) — the single cleanest confirmation signal.
- **Capex trajectory:** Q4 capex >$16B would imply 2024 re‑acceleration and should be treated as an FCF negative.
- **Payables/accrued balance:** any rebuild = incremental OCF; continued decline = another $5–10B headwind.
- **D&A growth** vs operating income growth (the "quality of margin" ratio).
- **SBC as % of revenue** — a rise above ~5% would erode the credibility of the margin story.
- **Net interest line** — currently ~neutral; watch for investment income decaying if short rates fall.
- **Securities portfolio** ($49.9B AFS, FV vs $50.4B amortized cost) — small unrealized loss; AOCI –$5.0B. Rising rates create mark‑to‑market noise in OCI, not P&L.

**Valuation inputs (no price feed available):** with TTM diluted EPS **~$1.91**, TTM EBITDA **~$73.9B**, TTM FCF **~$16.9B**, TTM revenue **~$554.0B**, and equity **~$183B**, an investor can frame AMZN on P/E, EV/EBITDA, or FCF yield using their own price. The relevant conclusion from the fundamentals alone: **the earnings and cash‑flow denominators are rising fast while the share count is roughly flat and net debt is negative — the direction of travel in every fundamental metric is favorable, but FCF‑based valuation remains sensitive to a single capex decision.**

**Suggested framing:** AMZN screens as a **margin‑inflection / FCF‑turnaround** situation with a fortress balance sheet and un‑utilized buyback capacity, but with **asymmetric event risk around the pending Q4 print** and a **structurally fragile FCF base** (3.1% margin) dependent on continued capex restraint. Size positions accordingly; a pre‑print estimate of a "worst realistic case" is a 2024 capex re‑acceleration that halves TTM FCF.

---

## 10. Explicit data gaps in this extract

- Q4/FY2023 financials (not yet filed as of 2024‑01‑04).
- Standalone revenue, fulfillment, technology & content, and segment (NA/Int'l/AWS) lines — not returned in the tag set; revenue here is *derived* from CostsAndExpenses + OperatingIncomeLoss (cross‑checked three ways).
- Insider transactions: **explicitly unavailable**.
- Price, market cap, consensus estimates, and guidance: not provided by the tools used.

---

## Key points summary

| Category | Metric / Fact | Value | Interpretation |
|---|---|---|---|
| **Latest filing** | Q3 2023 10‑Q | Accepted 2023‑10‑27 | Q4/FY23 not yet reported as of 2024‑01‑04 |
| **Growth** | Q3 2023 revenue (derived) | $143.08B, +12.6% YoY | Reacceleration vs 9M trend of +11.0% |
| **Profitability** | Q3 2023 operating income | $11.19B, **7.82% margin** | vs 1.99% in Q3 2022 (+5.83pp) |
| **Profitability** | 9M 2023 operating income | $23.64B, 5.84% margin | vs $9.51B / 2.61% in 9M 2022 |
| **TTM** | Operating income / margin | $26.38B / 4.76% | vs FY2022 full‑year $12.25B |
| **Bottom line** | Q3 2023 net income / EPS | $9.88B / $0.94 | +244% YoY; includes ~$1.2B equity gains |
| **Bottom line** | 9M 2023 net income / EPS | $19.80B / $1.89 | vs –$3.0B / –$0.29 in 9M 2022 |
| **Cash generation** | Q3 2023 OCF | $21.22B (+86% YoY) | 9M OCF $42.48B (+142%) |
| **Cash generation** | TTM OCF | $71.65B | 3.57x TTM net income |
| **Capex** | 9M 2023 / TTM | $38.14B (–19%) / $54.73B | Discretionary lever largely spent |
| **FCF** | Q3 2023 / 9M 2023 / TTM | +$8.74B / +$4.34B / +$16.92B | vs –$4.97B / –$29.47B / –$26.32B prior |
| **Liquidity** | Cash + marketable securities | $99.48B | vs LTD $67.1B + fin. leases $12.5B |
| **Leverage** | Net debt / EBITDA | **Net cash ~$20B**; coverage 8.3x | Debt/equity 43.5% gross |
| **Working capital** | Current ratio | 0.98 | Payables/accruals down $9.0B YTD |
| **Leases** | Operating + finance lease liabilities | $73.9B + $12.5B | Lease‑adjusted obligations ~$153.5B |
| **Off‑balance‑sheet** | Purchase obligations | $284.4B ($35.7B <12m) | Largest structural commitment |
| **Dilution** | SBC 9M 2023 / unrecognized | $17.70B (+26%) / $23.3B | 4.4% of revenue; diluted shares +2.5% YoY |
| **Capital returns** | Buybacks / new LT debt (9M 2023) | $0 / $0 | Capacity unused; debt being repaid |
| **Equity** | Stockholders' equity | ~$183.0B, +25.3% YTD | Retained earnings-driven |
| **Insider activity** | Data | **UNAVAILABLE** | No archive in vendor; not inferred |
| **Key catalyst** | Q4/FY2023 earnings | ~Early Feb 2024 | Confirmation or rejection of 7.8% margin |
| **Primary risk** | 2024 capex re‑acceleration | TTM FCF only 3.1% of revenue | A $10B capex swing ≈ 60% of TTM FCF |