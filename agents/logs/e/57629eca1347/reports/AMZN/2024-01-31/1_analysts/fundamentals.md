# AMZN — Fundamental Research Report
**Point-in-time: 2024-01-31** | Company: Amazon.com, Inc. (ticker **AMZN**)
**Latest data available: Form 10-Q for the quarter ended 2023-09-30 (filed 2023-10-27) — i.e., Q3 FY2023 is the most recent reported period as of the analysis date.**

---

## 1. Data provenance & critical timing caveat (read first)

| Item | Status |
|---|---|
| Source | B-project cached SEC filing facts, filtered by actual EDGAR acceptance timestamp ≤ 2024-01-31 |
| Latest 10-Q in dataset | Q3 FY2023, period end **2023-09-30**, filed **2023-10-27**, accession `0001018724-23-000018` |
| Prior 10-Q in dataset | Q2 FY2023, period end 2023-06-30, filed 2023-08-04, accession `0001018724-23-000012` |
| FY2023 10-K | **NOT YET FILED** as of 2024-01-31 — Q4/FY2023 results are the imminent catalyst |
| Annual (10-K) history | Not present in this snapshot; annual-frequency requests return the same 10-Q dataset. Multi-year history is limited to FY2022 comparatives embedded in the 2022/2023 10-Qs |
| Insider transactions | **DATA_UNAVAILABLE** — no authorized point-in-time insider archive exists for AMZN by 2024-01-31. No inference made below |
| Market price / valuation multiples | Not provided by these tools — no P/E, EV/EBITDA or price targets are asserted in this report |

**Consequence for a trader:** everything below is a *lagged* fundamental picture (through September 2023) plus the extremely strong forward signal that the Q4/FY2023 release — historically AMZN's largest profit quarter — was unreported on 2024-01-31. Treat the Q3 trend rates below as the setup, and the pending Q4 print as binary event risk.

---

## 2. Company profile

Amazon.com, Inc. (NASDAQ: **AMZN**), SEC CIK 0001018724, files on a calendar fiscal year (Dec 31). Per the Q3 FY2023 10-Q, the company reports **3 operating segments**: North America, International, and Amazon Web Services (AWS) — Amazon first split AWS into a standalone reported segment in Q1 FY2023, a change that materially improved transparency into the profit engine. Business lines: online and physical stores, third-party marketplace, Prime subscription, advertising, and AWS cloud infrastructure. Segment-level revenue and operating income were **not included in the extracted fact set** (data gap, §12).

Share data: 10,330.0M shares outstanding at 2023-09-30; **10,334.3M as of 2023-10-18**; 10,242M at 2022-12-31; 100B shares authorized; $0.01 par.

---

## 3. Income statement — the inflection is the whole story

Revenue is not separately tagged in this dataset; it is derived as `CostsAndExpenses + OperatingIncomeLoss`, which reconciles exactly to reported net sales.

### 3.1 Quarterly and year-to-date P&L

| $M unless noted | Q3 FY23 (Jul–Sep 23) | Q3 FY22 | YoY | 9M FY23 | 9M FY22 | YoY |
|---|---|---|---|---|---|---|
| Net sales (derived) | **143,083** | 127,101 | **+12.6%** | **404,824** | 364,779 | **+11.0%** |
| Cost of sales | 75,022 | 70,268 | +6.8% | 212,186 | 203,191 | +4.4% |
| COGS % of sales | 52.44% | 55.28% | −284 bp | 52.41% | 55.70% | −329 bp |
| Marketing | 10,551 | 11,014 | −4.2% | 31,468 | 29,420 | +7.0% |
| Marketing % of sales | 7.37% | 8.67% | −130 bp | 7.77% | 8.06% | −29 bp |
| G&A | 2,561 | 3,061 | −16.3% | 8,806 | 8,558 | +2.9% |
| G&A % of sales | 1.79% | 2.41% | −62 bp | 2.18% | 2.35% | −17 bp |
| Fulfillment + tech/content + other (residual) | 43,761 | 40,233 | +8.8% | 128,721 | 114,099 | +12.8% |
| Total costs & expenses | 131,895 | 124,576 | +5.9% | 381,181 | 355,268 | +7.3% |
| **Operating income** | **11,188** | 2,525 | **+343%** | **23,643** | 9,511 | **+149%** |
| **Operating margin** | **7.82%** | 1.99% | **+583 bp** | **5.84%** | 2.61% | **+323 bp** |
| Interest expense | (806) | (617) | +30.6% | (2,469) | (1,673) | +47.6% |
| Investment income | 776 | 277 | +180% | 2,048 | 544 | +276% |
| Other non-operating, net | 1,001 | 419 | +139% | 228 | (14,485) | n.m. |
| Pretax income | 12,189 | 2,944 | +314% | 23,871 | (4,974) | n.m. |
| Income tax | 2,306 | 69 | n.m. | 4,058 | (1,990) | n.m. |
| Effective tax rate | 18.9% | 2.3% | — | 17.0% | n.m. | — |
| Equity-method losses | (4) | (3) | — | (12) | (16) | — |
| **Net income** | **9,879** | 2,872 | **+244%** | **19,801** | **(3,000)** | n.m. |
| **Net margin** | **6.90%** | 2.26% | +464 bp | **4.89%** | −0.82% | +571 bp |
| Diluted EPS | $0.94 | $0.28 | +236% | $1.89 | $(0.29) | n.m. |
| Diluted shares (derived) | ~10,510M | ~10,257M | +2.5% | ~10,477M | ~10,345M | +1.3% |

**Trailing-twelve-month (2022-10-01 → 2023-09-30) anchors:** net income **$20,079M**; OCF **$71,654M**; capex **$54,733M**; D&A **$47,528M**; cash taxes **$8,677M**; deferred tax benefit **$(7,779)M**.

### 3.2 The margin bridge (where the +583 bp came from)

1. **Cost of sales leverage: −284 bp (Q3).** COGS grew 6.8% against 12.6% revenue growth. This is the single largest driver — the 2022 overcapacity/fulfillment-network buildout is being absorbed, and it is amplified by mix (AWS + advertising carry structurally higher gross margin, and AWS became a disclosed segment in 2023).
2. **Marketing discipline: −130 bp.** Absolute marketing dollars *fell* 4.2% YoY in Q3 — the clearest evidence of post-2022 cost discipline ("do more with less"). Note the 9M figure shows only −29 bp, meaning most of the marketing savings were realized in H2 (Q1 FY23 had heavy AWS/retail efficiency work).
3. **G&A: −62 bp**, absolute dollars down 16.3%.
4. **Residual bucket (fulfillment, tech & content, other) is the drag:** it grew 8.8% in Q3 vs 12.6% revenue — still positive deleverage on that line, and 12.8% growth for 9M, *outpacing* revenue's 11.0%. Translation: **technology & content spend (AWS infrastructure + Prime video) and fulfillment wage/network costs are the growth engines and the margin ceiling at the same time.**

### 3.3 Below-the-line dynamics — a subtle but real improvement

- **Net interest turned constructive.** 9M FY23 interest expense $2,469M (+47.6%) vs investment income $2,048M: a net drag of only **$(421)M** versus **$(1,129)M** in 9M FY22. Higher rates are now a *two-sided* item for AMZN because its ~$99B cash/securities pile earns float while gross debt falls.
- **Q3 interest coverage 13.9x** (op income / interest expense); 9M 9.6x. Up from 4.1x in Q3 FY22. This is the single best summary statistic of the turnaround.
- **Tax normalization.** The 2.3% Q3 FY22 rate was an artifact of a near-zero pretax base. A **17.0% 9M FY23 rate** and 18.9% Q3 rate are the "new normal" — and a headwind, because going forward incremental pretax dollars are taxed at ~19% rather than ~2%.

---

## 4. Cash flow statement — FCF has gone from deeply negative to structurally positive

| $M | Q3 FY23 | Q3 FY22 | 9M FY23 | 9M FY22 | TTM (Oct22–Sep23) | FY (Oct21–Sep22) |
|---|---|---|---|---|---|---|
| Operating cash flow | **21,217** | 11,404 | **42,481** | 17,579 | **71,654** | 39,665 |
| Capex (productive assets) | (12,479) | (16,378) | (38,141) | (47,053) | **(54,733)** | (65,988) |
| **Free cash flow (derived)** | **8,738** | **(4,974)** | **4,340** | (29,474) | **16,921** | **(26,323)** |
| FCF margin | 6.1% | −3.9% | 1.1% | −8.1% | ~3.1% | −5.1% |
| Capex % of revenue | 8.7% | 12.9% | 9.4% | 12.9% | ~9.9% | ~12.8% |
| OCF margin | 14.8% | 9.0% | 10.5% | 4.8% | ~12.9% | — |
| Investing cash flow | (11,753) | (15,608) | (37,232) | (26,780) | (48,053) | (39,360) |
| Financing cash flow | (8,948) | 3,016 | (9,133) | 9,632 | (9,047) | 6,532 |
| Net change in cash incl. FX | 14 | (2,522) | (4,172) | (1,299) | +14,903 | +5,001 |

**Three high-signal takeaways:**

1. **The FCF swing is capex-led, not just profit-led.** 9M capex fell **19%** ($47.1B → $38.1B) *while* revenue grew 11% — capex intensity compressed from 12.9% to 9.4% of sales. Q3 capex fell 23.8% YoY. This is a deliberate capex *air-pocket* after the 2021–22 logistics buildout, and it is the most powerful near-term FCF lever management controls.
2. **The capex cut is not yet over.** Q3 FY23 capex of $12,479M is still **1.03x** that quarter's D&A. The asset base is holding steady (capex ≈ D&A) — Amazon is in maintenance-plus mode, not harvest mode. Any commentary on 2024 capex re-acceleration (AWS AI infrastructure) in the pending Q4 print is the key swing factor for the FCF narrative.
3. **Q4 is enormous and is missing from this data.** Derived: Q4 FY22 OCF = $71,654 − $42,481 = **$29,173M**; Q4 FY22 capex = $54,733 − $38,141 = **$16,592M**; **Q4 FY22 FCF ≈ $12,581M** — i.e., ~74% of the entire TTM FCF was generated in the one unreported holiday quarter. A trader at 2024-01-31 is positioning into a quarter that historically delivers the majority of annual FCF.

**Cash flow quality check (9M FY23):** net income 19,801 + D&A 34,843 + SBC 17,704 = 72,348 gross sources, less working-capital drag (AR/other assets +10,364; accrued liabilities −9,022), less deferred tax −4,412, plus other ≈ **42,481**. So **SBC and D&A contribute 1.24x of the operating cash flow** — OCF is not clean earnings; it is a non-cash-charge-funded number. FCF/NI = 16,921/20,079 = **0.84x** TTM.

---

## 5. Balance sheet — fortress liquidity, shrinking debt, growing lease obligations

| $M | 2023-09-30 | 2022-12-31 | Change |
|---|---|---|---|
| Cash & equivalents | 49,605 | 53,888 | −7.9% |
| Marketable securities (AFS, fair value) | 49,871 | n/a in dataset | — |
| **Total cash + securities (derived)** | **~99,476** | — | — |
| Accounts receivable, net | 43,420 | 42,360 | +2.5% |
| Inventory, net | 35,406 | 34,405 | +2.9% |
| **Current assets** | **142,995** | 146,791 | −2.6% |
| **Total assets** | **486,883** | 462,675 | +5.2% |
| Accounts payable | 72,004 | 79,600 | −9.5% |
| Accrued liabilities | 58,812 | 62,566 | −6.0% |
| **Current liabilities** | **145,214** | 155,393 | −6.6% |
| Long-term debt — current portion | 5,995 | 2,999 | +99.9% |
| Long-term debt — noncurrent | 61,098 | 67,150 | −9.0% |
| **Total debt (derived)** | **67,093** | 70,149 | **−4.4%** |
| Finance lease liabilities | 12,466 | 15,783 | −21.0% |
| Operating lease liabilities (total) | 73,902 | 69,040 | +7.0% |
| Contract liabilities — current (deferred revenue) | 14,398 | 13,227 | +8.9% |
| Contract liabilities — noncurrent | 2,700 | 2,900 | −6.9% |
| AOCI | (5,003) | (4,487) | −11.5% |
| Additional paid-in capital | 92,711 | 75,066 | +23.5% |
| Inventory valuation reserves | 2,600 | 2,800 | −7.1% |

**Liquidity & leverage:**
- **Current ratio 0.985x** (142,995/145,214), improved from 0.945x at 12/31/22. AMZN runs a deliberately sub-1.0 current ratio funded by negative working capital — see the cash-conversion-cycle math below. Not a solvency concern.
- **Net cash position: +$19.9B** (cash+securities $99.5B vs total debt $67.1B + finance leases $12.5B = $79.6B).
- **However, on a fully-loaded basis** (including $73.9B of operating lease liabilities, which are off the debt line but economically debt-like for a company with a massive logistics/property footprint): net obligations = 67,093 + 12,466 + 73,902 − 99,476 = **+$54.0B**. Leases are ~52% of the fully-loaded obligation stack — this is the balance sheet's most under-appreciated feature.
- **Debt / TTM OCF = 0.94x.** Debt / TTM EBITDA (op income 20,079-equiv + D&A 47,528 ≈ $68B) ≈ **0.99x**. Leverage is not a risk at AMZN; the question is purely returns on incremental capital.
- **Debt / equity ≈ 35%** using an implied equity base of **~$191B** (derived: total assets $486,883 less current liabilities $145,214, debt $61,098, operating lease noncurrent $65,810, finance lease noncurrent $10,081 = $204,680, less other non-current liabilities/deferred taxes which are not itemized in this fact set, ≈$13–14B → **~$191B**). Book value ≈ **$18.5/share**.

**Working capital efficiency (9M FY23, 273 days):**
- Days inventory outstanding: **45.6** (35,406 ÷ daily COGS of $777M)
- Days sales outstanding: **29.3** (43,420 ÷ daily revenue of $1,483M)
- Days payable outstanding: **92.7** (72,004 ÷ daily COGS)
- **Cash conversion cycle: −17.8 days.** AMZN is funded by suppliers. This is a genuine structural competitive advantage: >$72B of payables finance inventory carries zero interest cost.
- *Risk flag:* AP fell 9.5% and accrued liabilities fell 6.0% during 9M FY23 — a **$(9.0)B cash use** from accrued liabilities. Part of the 2023 OCF strength came despite this; but a continued unwind of the payables float (e.g., from supplier-payment-term pressure or a demand deceleration) would be an OCF headwind.

**Lease escalation watch:** operating lease liability rose $4.9B (+7.0%) while the weighted-average discount rate rose from 2.8% to 3.2% — i.e., the liability would have grown even more at a constant rate. Undiscounted operating lease payments total **$88.8B** (of which $3.2B Oct–Dec 23, $10.0B in the next 12 months). Finance lease undiscounted payments $14.6B.

**Purchase / contractual obligations (as of 2023-09-30):** total **$284,407M**, of which **$8,914M** in Q4 FY23, **$35,712M** in the next twelve months, $28,429M year 2, $23,789M year 3, $26,581M year 4, and **~$161B beyond year 4**. These are largely AWS capacity, digital content, and logistics commitments — real, largely non-cancellable, and the biggest reason a demand shock would be slow to show in margins.

---

## 6. Capital allocation, dilution, and shareholder returns

| $M | Q3 FY23 | 9M FY23 | 9M FY22 | FY (Oct21–Sep22) |
|---|---|---|---|---|
| Share repurchases | **0** | **0** | 6,000 | 6,000 |
| Dividends | **0** | **0** | 0 | 0 |
| LT debt issued | 0 | **0** | 12,931 | 13,131 |
| LT debt repaid | 0 | 3,386 | 1 | 1,002 |
| Short-term debt borrowed | 216 | 17,395 | 30,946 | 33,613 |
| Short-term debt repaid | 8,095 | 19,339 | 21,757 | 24,416 |
| Finance lease principal payments | 1,005 | 3,605 | 6,301 | 8,561 |
| Acquisitions, net of cash | — | 3,829 | 6,600 | 7,635 |
| Marketable securities purchased | 219 | 1,053 | 2,332 | 10,598 |
| Marketable securities sold/matured | 1,393 | 4,059 | 25,918 | 38,455 |

- **Zero capital returned to shareholders** for five consecutive quarters (buybacks stopped after Q2 FY22's $3.3B; nothing in FY23). Capital is going entirely into capex, debt reduction, and acquisitions (iBuy/MGM-style content and healthcare deals — $3.8B in 9M FY23).
- **Gross long-term debt issuance is zero in FY2023** and LT debt has been repaid. AMZN has shifted from a net issuer (2021–22) to a net de-leverer. Short-term commercial paper is being churned but net-reduced.
- **Dilution is real but modest:** shares outstanding 10,242M → 10,330M in nine months (+0.86%), annualizing to ~1.1%. SBC was **$17,704M in 9M FY23 (+26% YoY)** — that is **4.4% of revenue** and ~89% of net income. Per-share economics are being diluted by roughly 1% a year while income grows far faster, so EPS growth (diluted 9M $1.89 vs basic $1.93) captures most but not all of the earnings power.
- **Unrecognized SBC of $23.3B** at 2023-09-30 — a pre-committed future expense over the next several years. Investors valuing AMZN on P/E should be adding this back or explicitly discounting for it.

---

## 7. Earnings quality — four specific flags

1. **Q3 FY23 non-operating income of $1,001M included a $1,200M gain on equity securities** (`EquitySecuritiesFvNiGainLoss` = +$1,200M for Q3, +$1,000M for 9M). Stripping the non-operating line, Q3 pretax would be ~$11,188M and, at a 19% rate, net ~$9.1B vs $9.879B reported — **~8% of Q3 net income was non-operating, non-cash, mark-to-market noise**. For 9M the effect is trivial (non-op only $228M) because Q1–Q2 had offsetting losses. Do not annualize Q3's $0.94 diluted EPS without this adjustment.
2. **Deferred tax is a benefit, not an expense:** $(4,412)M for 9M FY23 and $(7,779)M TTM. Strong deferred-tax benefits mean reported net income is running *above* cash-tax reality in prior periods — but cash taxes paid rose 61% YoY to $6,982M in 9M FY23 as current tax expense ($8,470M implied) caught up. Expect the tax line to keep normalizing upward.
3. **OCF is heavily non-cash-funded:** D&A $34,843M + SBC $17,704M = $52.5B of the $42.5B 9M OCF. FCF/NI of 0.84x is respectable but not stellar for a company with $47.5B of TTM D&A.
4. **Impairments remain small and improving:** $420M in 9M FY23 (vs $350M 9M FY22), plus a $200M loss on contract termination (vs $300M). Asset-impairment risk in the physical-store/Grocery and Project Kuiper-type bets is *not* currently a material P&L item. Inventory reserves declining ($2.8B → $2.6B) and a stable bad-debt allowance ($1.4B → $1.5B) confirm healthy underlying asset quality — no signs of channel stuffing or receivable aging stress (DSO flat at 29 days).

---

## 8. Insider transactions

**Not available.** The data package contains no authorized, point-in-time insider-transaction archive for AMZN as of 2024-01-31. **No insider buying or selling is asserted, inferred, or estimated in this report.** Any claim of insider activity for AMZN around this date would be fabricated and should be treated as such by the reader. This is a genuine gap in the evidence base — a trader should source Form 4 data independently before weighting insider signal.

---

## 9. Actionable insights for traders — what the fundamentals actually say

### A. The core thesis is intact and quantified: margin, not growth, is the driver
Revenue grew **+11.0%** for 9M FY23, but operating income grew **+149%** and Q3 operating income grew **+343%**. Only **+323 bp of 9M margin expansion** was needed to almost triple operating profit. Concretely: COGS leverage (−329 bp) plus marketing/G&A discipline (−46 bp combined) explains essentially all of it. **Positioning implication:** AMZN is now a *margin-leverage* story. That means the stock is far more sensitive to the incremental margin trajectory than to a percentage point of revenue growth. Watch the residual cost bucket (fulfillment + tech & content), which grew 12.8% in 9M — faster than revenue. If that line decelerates below revenue growth, margins expand again; if AWS AI capex re-accelerates it, the 2024 margin runway narrows.

### B. FCF inflection is the cleanest, most under-priced fact in this dataset
FY(Oct21–Sep22) FCF **−$26.3B** → TTM(Oct22–Sep23) FCF **+$16.9B**, a **$43B swing in four quarters**, driven **19% capex reduction** on **11% revenue growth**. Q3 FY23 alone produced **+$8.7B FCF** versus **−$5.0B** a year earlier. **Implication:** the "Amazon burns cash" bear case is empirically dead as of this data. Any further capex discipline (or even flat capex into 2024) converts ~100% of incremental OCF growth into FCF.

### C. The single biggest event risk: the unreported Q4/FY2023 quarter carries the majority of annual FCF
Derived Q4 FY22 FCF was **~$12,581M — 74% of the entire TTM FCF.** As of 2024-01-31 that quarter is *not in the data*. **Implication:** the market is pricing AMZN without the most profitable quarter of the year in the trailing numbers. A constructive Q4 print (especially any 2024 capex guidance) is an asymmetric catalyst; a capex re-acceleration guide is the primary downside vector, because it would immediately compress the FCF multiple that the stock is currently being re-rated on.

### D. Balance sheet is a non-issue — use it as a floor, not a risk
Net cash of **+$19.9B** on cash+securities of **~$99.5B** vs debt of $67.1B; debt/OCF **0.94x**; interest coverage **13.9x** in Q3; LT debt issuance **$0** in FY23; negative **−17.8 day** cash conversion cycle funded by $72B of payables. **Implication:** there is no refinancing, liquidity, or solvency angle here. Do not pay for balance-sheet risk in AMZN; the only legitimate leverage concern is the **$73.9B operating lease** stack plus **$284B of contractual purchase obligations**, which are demand-cycle risks, not credit risks.

### E. Dilution + zero buyback = a per-share growth haircut you must model
SBC of **$17,704M (9M, +26% YoY, 4.4% of revenue)**, **$23.3B unrecognized**, shares +0.86% in nine months, **$0 buybacks and $0 dividends** for five quarters. Diluted EPS ($1.89) trails basic ($1.93) by 2%. **Implication:** the earnings *power* is growing faster than EPS. Any bull case built on EPS alone understates operating improvement by ~1%/yr — and any valuation model using GAAP EPS without an SBC adjustment overstates owner earnings by roughly 20–25%.

### F. Watch these five specific line items as leading indicators
1. **Marketing expense in absolute dollars.** Q3 FY23 fell 4.2% YoY — an extreme efficiency signal. If it re-accelerates, growth is being bought back.
2. **Accrued liabilities.** Down $9.0B in 9M FY23 = a cash drain that OCF overcame. A second consecutive decline signals payables/accrual unwind.
3. **Capex ÷ D&A (currently 1.03x in Q3).** Below 1.0x = FCF harvest; above 1.2x = margin/FCF compression ahead.
4. **Deferred revenue.** Contract liabilities +8.9% to $14.4B with $10.9B recognized from the opening balance in 9M — a clean read on Prime/AWS backlog health.
5. **Interest expense vs. investment income spread.** Now only a $(421)M 9M drag; with debt falling and $99B of earning assets, this could flip to a *net contributor* — a quiet, durable EPS tailwind.

### G. Fade the "asset impairment" bear case
Impairments of only $420M (9M) against $486.9B of assets (0.09%), declining inventory reserves, and a stable $1.5B bad-debt allowance indicate no hidden asset-quality problem in the retail or device books. The risk sits in *future* obligations (leases and purchase commitments), not in existing asset carrying values.

---

## 10. Risks to the constructive read

| Risk | Evidence in data | Potential impact |
|---|---|---|
| **Q4 capex re-acceleration** (AWS/AI build) | Capex still 1.03x D&A; $284.4B contractual obligations, ~$161B beyond year 4 | Directly compresses the FCF that is driving the re-rating |
| **Residual cost bucket outgrowing revenue** | Fulfillment/tech/content/other +12.8% (9M) vs revenue +11.0% | Caps margin expansion at Q3's 7.8% op margin |
| **Tax normalization** | 17.0% 9M FY23 rate vs 2.3% Q3 FY22; cash taxes +61% YoY | Each 500 bp of rate = ~$1.2B/yr of net income at current pretax run-rate |
| **Working-capital unwind** | Accrued liabilities −$9.0B, AP −$9.5% in 9M FY23 | OCF headwind independent of earnings |
| **Dilution** | Shares +0.86% in 9M; SBC $17.7B (+26%) | ~1%/yr EPS leakage; $23.3B unrecognized overhang |
| **Disclosure gap** | No segment P&L, no Q4, no price data in this dataset | Cannot verify AWS vs. retail margin attribution — a genuine analytical blind spot |
| **FX** | Q3 other comprehensive income −$1,388M translation loss; comprehensive income $8,556M < net income $9,879M | Reported margins understate/overstate depending on USD |
| **Lease + commitment load** | $73.9B op leases + $12.5B finance leases + $284.4B purchase obligations | Slow-to-adjust cost base in a demand downturn |

---

## 11. Bottom line for a trader at 2024-01-31

The last *reported* fundamentals show AMZN in the sharpest operating-margin inflection in its history: **Q3 FY23 operating margin 7.82% vs 1.99%** a year prior, **9M operating income $23.6B vs $9.5B**, **net income $19.8B vs a $(3.0)B loss**, **TTM FCF swung from −$26.3B to +$16.9B**, and **interest coverage of 13.9x** with net cash on the balance sheet. Those are facts, not narrative. The bull case is *capex discipline + COGS leverage + marketing/G&A austerity*, and it is already visible in the income statement and cash flow statement. The bear case is not solvency, not demand collapse, and not asset quality — it is **capex re-acceleration compressing the FCF multiple**, plus the mechanical **tax normalization** and **~1%/yr SBC dilution** that make EPS grow slower than the underlying business. And the largest single swing factor — Q4 FY2023, which historically generated ~74% of trailing annual FCF — is **not yet in the data**. Position for a margin-leverage confirmation, hedge for a capex-guidance surprise.

---

## 12. Key data table

| Category | Metric | Value | Period | Signal |
|---|---|---|---|---|
| **Identity** | Ticker / entity | **AMZN** / Amazon.com, Inc. (CIK 0001018724) | — | Confirmed, no substitution |
| Filing | Latest filed | 10-Q, Q3 FY2023 (accn 0001018724-23-000018) | Filed 2023-10-27 | Q4/FY23 10-K **not yet filed** |
| Segments | Reported operating segments | **3** | 9M FY23 | AWS broken out for first time in 2023 |
| **Growth** | Revenue (derived) | **$143,083M** | Q3 FY23 | **+12.6% YoY** |
| Growth | Revenue (derived) | **$404,824M** | 9M FY23 | **+11.0% YoY** |
| Growth | Revenue YoY (est. TTM) | ~$554B annualized run-rate | TTM Oct22–Sep23 | Requires derived Q4 FY22 revenue |
| **Profitability** | Operating income | **$11,188M** | Q3 FY23 | **+343% YoY** |
| Profitability | Operating margin | **7.82%** | Q3 FY23 | **+583 bp YoY** |
| Profitability | Operating income | **$23,643M** | 9M FY23 | +149% YoY |
| Profitability | Operating margin | **5.84%** | 9M FY23 | +323 bp YoY (2.61% prior) |
| Profitability | Net income | **$9,879M** | Q3 FY23 | +244% YoY |
| Profitability | Net margin | **6.90%** | Q3 FY23 | +464 bp YoY |
| Profitability | Net income | **$19,801M** | 9M FY23 | vs $(3,000)M loss in 9M FY22 |
| Profitability | Net income (TTM) | **$20,079M** | Oct22–Sep23 | — |
| Per share | Diluted EPS | **$0.94** / **$1.89** | Q3 / 9M FY23 | vs $0.28 / $(0.29) |
| Per share | Diluted shares (derived) | ~10,510M | Q3 FY23 | +2.5% YoY |
| Cost structure | COGS % of revenue | **52.44%** | Q3 FY23 | −284 bp YoY (key driver) |
| Cost structure | Marketing / revenue | 7.37% | Q3 FY23 | −130 bp; absolute $ −4.2% YoY |
| Cost structure | G&A / revenue | 1.79% | Q3 FY23 | −62 bp; absolute $ −16.3% YoY |
| Below the line | Interest expense | $806M / $2,469M | Q3 / 9M FY23 | +30.6% / +47.6% YoY |
| Below the line | Investment income | $776M / $2,048M | Q3 / 9M FY23 | +180% / +276% YoY |
| Below the line | Net interest spread | **$(421)M** | 9M FY23 | Improved from $(1,129)M |
| Below the line | Effective tax rate | **17.0%** | 9M FY23 | Normalized from ~2% (tax headwind) |
| **Cash flow** | Operating cash flow | **$21,217M** / **$42,481M** | Q3 / 9M FY23 | +86% / +142% YoY |
| Cash flow | Capex | **$12,479M** / **$38,141M** | Q3 / 9M FY23 | **−23.8% / −19.0% YoY** |
| Cash flow | **Free cash flow (derived)** | **$8,738M** / **$4,340M** | Q3 / 9M FY23 | vs $(4,974)M / $(29,474)M |
| Cash flow | TTM FCF | **$16,921M** | Oct22–Sep23 | vs **$(26,323)M** prior year |
| Cash flow | Capex / revenue | 8.7% / 9.4% | Q3 / 9M FY23 | Down from 12.9% |
| Cash flow | D&A | $12,131M / $34,843M (TTM $47,528M) | Q3 / 9M FY23 | +17.5% / +19.2% YoY |
| Cash flow | Q4 FY22 FCF (derived) | **~$12,581M** | Oct–Dec 22 | ~74% of TTM FCF — **unreported** |
| **Balance sheet** | Total assets | **$486,883M** | 2023-09-30 | +5.2% vs 2022-12-31 |
| Balance sheet | Cash + AFS securities | **~$99,476M** | 2023-09-30 | Cushion |
| Balance sheet | Total debt | **$67,093M** | 2023-09-30 | **−4.4%** in 9M |
| Balance sheet | Finance lease liabilities | $12,466M | 2023-09-30 | −21.0% |
| Balance sheet | Operating lease liabilities | **$73,902M** | 2023-09-30 | **+7.0%** (hidden leverage) |
| Balance sheet | **Net cash position** | **+$19,917M** | 2023-09-30 | Debt-only basis |
| Balance sheet | Net obligations (incl. leases) | ~$54,000M | 2023-09-30 | Fully-loaded view |
| Balance sheet | Current ratio | **0.985x** | 2023-09-30 | Up from 0.945x |
| Balance sheet | Implied stockholders' equity | **~$191,000M** (derived) | 2023-09-30 | BV ≈ $18.5/share |
| Balance sheet | Debt / TTM OCF | **0.94x** | 2023-09-30 | Very low |
| Balance sheet | Interest coverage | **13.9x** (Q3) / 9.6x (9M) | FY23 | Up from 4.1x (Q3 FY22) |
| Efficiency | Cash conversion cycle | **−17.8 days** | 9M FY23 | DIO 45.6 / DSO 29.3 / DPO 92.7 |
| Efficiency | DSО / DPO | 29.3 / 92.7 days | 9M FY23 | Supplier-funded model |
| Commitments | Total contractual obligations | **$284,407M** | 2023-09-30 | $35,712M due <12 mo |
| Commitments | Op + finance lease (undiscounted) | $88,814M + $14,574M | 2023-09-30 | Slow-to-adjust cost base |
| Deferred revenue | Contract liabilities (current) | $14,398M | 2023-09-30 | +8.9%; $10.9B recognized in 9M |
| **Capital return** | Buybacks / dividends | **$0 / $0** | 9M FY23 | Fifth straight quarter of zero |
| Capital return | LT debt issued | **$0** | 9M FY23 | Net de-leverer |
| Capital return | Acquisitions (net of cash) | $3,829M | 9M FY23 | vs $6,600M prior |
| Dilution | Shares outstanding | **10,330.0M** (10,334.3M @ 10/18/23) | 2023-09-30 | +0.86% in 9 months |
| Dilution | Share-based comp | **$17,704M** (Q3 $5,829M) | 9M FY23 | **4.4% of revenue; +26% YoY** |
| Dilution | Unrecognized SBC | **$23,300M** | 2023-09-30 | Future expense overhang |
| Quality | Non-operating income incl. $1,200M equity gain | $1,001M | Q3 FY23 | ~8% of Q3 net income is non-op |
| Quality | Deferred tax expense/(benefit) | $(4,412)M (TTM $(7,779)M) | 9M FY23 | Benefit inflating NI |
| Quality | Cash taxes paid | $6,982M (TTM $8,677M) | 9M FY23 | **+61% YoY** |
| Quality | Impairments | $420M | 9M FY23 | Only 0.09% of assets |
| Quality | Inventory / bad-debt reserves | $2,600M / $1,500M | 2023-09-30 | Both stable-to-better |
| Quality | AOCI | $(5,003)M | 2023-09-30 | FX drag; Q3 comprehensive income < NI |
| **Insider** | Transactions | **DATA UNAVAILABLE — not inferred** | — | Evidence gap |
| **Valuation** | Price / multiples | **Not available from tools — not asserted** | — | — |