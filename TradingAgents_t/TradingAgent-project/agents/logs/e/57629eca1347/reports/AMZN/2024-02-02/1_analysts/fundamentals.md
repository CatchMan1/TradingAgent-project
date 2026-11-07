# AMZN — Fundamental Deep Dive (Point-in-Time Report)

**Security:** AMZN (Amazon.com, Inc., Nasdaq)
**Report date / "as-of":** 2024-02-02
**Primary source document:** FY2023 Form 10-K, accession `0001018724-24-000008`, filed **2024-02-02 04:48:30 UTC** (i.e., the annual report on Form 10-K became public on the report date, the morning after the Q4/FY23 release). All facts below are filtered so that only data **publicly available by 2024-02-02** is used — there is no look-ahead.

---

## 1. Data provenance & availability caveats (read first)

| Item | Status |
|---|---|
| Income statement, balance sheet, cash-flow facts | ✅ Available — FY2021, FY2022, FY2023 (10-K) + select 10-Q (Q2'23, Q3'23 filings) comparison periods |
| Revenue line item | ⚠️ **Not directly tagged** in the vendor dataset; **derived** as `CostsAndExpenses + OperatingIncomeLoss` (arithmetically exact and internally consistent) |
| Total stockholders' equity / retained earnings / goodwill / inventory / PP&E / segment (NA, Int'l, AWS) detail | ❌ Not returned by the data vendor — **not estimated or fabricated** below |
| Intra-year quarterly granularity | ⚠️ Only FY periods + 10-Q **cumulative** (9M/Q3) cash-flow data are tagged |
| **Insider transactions** | ❌ **DATA_UNAVAILABLE** — the vendor has no authorized, point-in-time insider archive for AMZN. **No insider buying/selling signal is included, and none should be inferred.** |
| Share price / market cap / consensus estimates | ❌ Not a fundamental-data field — multiples below are expressed with the price as an explicit variable |

---

## 2. Company profile (context)

Amazon.com, Inc. is a global technology and e-commerce conglomerate with **3 operating segments** (confirmed in the filing: `NumberOfOperatingSegments = 3`): **North America**, **International**, and **Amazon Web Services (AWS)**. Revenue streams span online and physical retail, third-party seller services (commissions, fulfillment, advertising), subscription services (Prime), advertising, and AWS cloud infrastructure. Scale at FY23: **~$574.8B revenue**, **~10.39B shares outstanding** (10,387,381,291 as of 2024-01-24), **$527.9B total assets**.

---

## 3. Income statement — FY2023 vs FY2022 vs FY2021 ($ millions)

| Line item | FY2021 | FY2022 | FY2023 | YoY '23 |
|---|---:|---:|---:|---:|
| Revenue (derived) | 469,822 | 513,983 | **574,785** | **+11.8%** |
| Cost of goods & services | 272,344 | 288,831 | 304,739 | +5.5% |
| **Gross profit** | 197,478 | 225,152 | **270,046** | **+19.9%** |
| Gross margin | 42.0% | 43.8% | **47.0%** | +317 bp |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| **Operating income** | 24,879 | 12,248 | **36,852** | **+200.9%** |
| **Operating margin** | 5.30% | 2.38% | **6.41%** | +403 bp |
| Interest expense | 1,809 | 2,367 | 3,182 | +34.4% |
| Interest & investment income | 448 | 989 | 2,949 | +198% |
| Non-operating income/(expense) | 13,272 | (18,184) | 705 | n.m. |
| Pre-tax income | 38,151 | (5,936) | 37,557 | n.m. |
| Income tax (benefit) | 4,791 | (3,217) | 7,120 | n.m. |
| **Net income** | 33,364 | (2,722) | **30,425** | n.m. |
| Net margin | 7.10% | (0.53)% | **5.29%** | +582 bp |
| **Diluted EPS** | 3.24 | (0.27) | **2.90** | n.m. |
| Basic EPS | 3.30 | (0.27) | 2.95 | n.m. |
| Diluted shares (derived: NI ÷ EPS) | ~10,297 | n.m. | **~10,491** | +1.4% (basic shares 10,242→10,383) |

**Non-GAAP build (derived):**

| Metric | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| EBITDA proxy (Op. income + D&A) | 59,312 | 54,169 | **85,515** |
| EBITDA margin | 12.6% | 10.5% | **14.9%** |
| EBITDA less SBC | 46,555 | 34,548 | **61,492** |
| SBC as % of revenue | 2.71% | 3.82% | **4.18%** |
| D&A as % of revenue | 7.33% | 8.16% | **8.47%** |

**Two things a trader must not misread:**
1. **FY23 net income ($30.4B) is still *below* FY21 ($33.4B)** despite revenue +22% — because FY21 was flattered by **$11.6B of unrealized gains on equity securities** (Rivian) while FY22 absorbed a **–$13.6B** mark. FY23's non-operating swing was only **+$1.0B**. On operating income, FY23 is the best year in the dataset (+48% vs FY21).
2. **Roughly $5.9B of FY23 net income is non-cash deferred-tax benefit** (`DeferredIncomeTaxExpenseBenefit = –5,876`), while **cash taxes paid jumped 85% to $11,179M** (vs book tax of $7,120M). The tax tailwind that boosted FY22's loss-reduction is now reversing.

---

## 4. Cost structure & margin bridge (FY22 → FY23, $ millions)

| Component | FY2022 | FY2023 | Δ | % of revenue '23 |
|---|---:|---:|---:|---:|
| Cost of goods & services | 288,831 | 304,739 | +15,908 | 53.0% |
| Fulfillment / tech & content | *not tagged* | *not tagged* | — | — |
| Marketing expense | 42,238 | 44,370 | +2,132 | 7.72% |
| — of which advertising | 20,600 | 20,300 | **–300** | 3.5% |
| G&A | 11,891 | 11,816 | **–75** | 2.06% |
| D&A | 41,921 | 48,663 | +6,742 | 8.47% |
| SBC | 19,621 | 24,023 | +4,402 | 4.18% |
| **Operating income** | **12,248** | **36,852** | **+24,604** | 6.41% |

**Bridge:** +$44.9B gross profit (mix/AWS + cost-of-sales leverage, 53.0% vs 56.2% of revenue) minus +$20.3B of operating expense (only +9.5%, well below 11.8% revenue growth and way below 19.9% gross-profit growth) ⇒ **+$24.6B operating income**. Notable: **advertising expense fell in absolute terms for the first time in the dataset** (20,600 → 20,300) and G&A was cut slightly — hard cost discipline, not just volume leverage. Also absent in FY23: the **$1.1B asset impairments** and the **–$480M contract-termination loss** booked in FY22.

---

## 5. Cash flow & free cash flow ($ millions)

| | FY2021 | FY2022 | FY2023 | YoY |
|---|---:|---:|---:|---:|
| Net cash from operating activities | 46,327 | 46,752 | **84,946** | **+81.7%** |
| Capex (productive assets) | (61,053) | (63,645) | **(52,729)** | **–17.2%** |
| **Free cash flow** | **(14,726)** | **(16,893)** | **+32,217** | **+49.1B swing** |
| FCF margin | (3.1)% | (3.3)% | **5.6%** | +8.9 pt |
| Finance-lease principal repayments | (11,163) | (7,941) | (4,384) | –44.8% |
| FCF after finance-lease principal | (25,889) | (24,834) | **27,833** | n.m. |
| Net cash from investing | (58,154) | (37,601) | (49,833) | +32.5% out |
| Net cash from financing | +6,291 | +9,718 | **(15,879)** | n.m. |
| Net change in cash (incl. FX) | (5,900) | 17,776 | **+19,637** | +10.5% |
| OCF / net income | 1.39x | n.m. | **2.79x** | — |
| Capex / revenue | 13.0% | 12.4% | **9.2%** | –320 bp |
| Capex / D&A | 1.77x | 1.52x | **1.08x** | — |

**Derived from 10-Q cumulative data (cash-flow only):**

| Period | OCF | Capex |
|---|---:|---:|
| 9M 2022 (Jan–Sep) | 17,579 | 47,053 |
| **9M 2023 (Jan–Sep)** | **42,481** | **38,141** |
| Q3 2023 (Jul–Sep) | 21,217 | 12,479 |
| **Q4 2023 implied (FY – 9M)** | **42,465** | **14,588** |
| Q4 2022 implied | 29,173 | 16,592 |

**Read-through:** Q4 alone generated **~$42.5B of OCF (+45.6% y/y)** — half the year's operating cash flow. FY23 FCF of **$32.2B** is the first positive FCF in three years, but **~$10.9B of the $49.1B FCF swing came from *lower* capex, not operations**. Confirm durable FCF only if capex stays ≤ ~$55–60B in 2024; a re-acceleration to FY22 levels (≈$64B) would mechanically cut FCF by ~$11B. Capex/D&A at 1.08x (vs 1.52x) says the asset base is now barely growing faster than depreciation — a maintenance-phase signature.

---

## 6. Balance sheet ($ millions, 12/31)

| | 2021 | 2022 | 2023 | Δ '23 |
|---|---:|---:|---:|---:|
| Cash & equivalents | — | 53,888 | **73,387** | +36.2% |
| Marketable securities (AFS, fair value) | — | — | **70,919** | n/a |
| **Cash + securities** | — | — | **144,306** | — |
| Accounts receivable, net | — | 42,360 | **52,253** | +23.4% |
| Current assets | — | 146,791 | **172,351** | +17.4% |
| **Total assets** | 420,549 | 462,675 | **527,854** | **+14.1%** |
| Accounts payable | — | 79,600 | **84,981** | +6.8% |
| Accrued liabilities | — | 62,566 | **64,709** | +3.4% |
| Unearned revenue (cur. + non-cur.) | — | 16,127 | **20,927** | +29.8% |
| Operating lease liabilities | — | 69,040 | **75,639** | +9.6% |
| Finance lease liabilities | — | 15,783 | **12,109** | –23.3% |
| Debt (carrying amount) | — | 67,150 | **58,314** | **–13.2%** |
| Current liabilities (derived: AP + accrued + unearned) | — | 154,757 | **164,917** | +6.6% |
| Deferred tax assets, net | — | 34,509 | **45,788** | +32.7% |
| — of which IPR&D DTA | — | 6,824 | **14,800** | **+117%** |
| Net deferred tax liability position | — | 7,513 | **13,197** | +75.7% |

**Liquidity & leverage (derived):**

| Metric | 2023 |
|---|---|
| Current ratio | 172,351 / 164,917 = **1.05x** |
| Quick assets (cash + securities + AR) / CL | 196,559 / 164,917 = **1.19x** |
| Working capital | **+$7.4B** (thin but positive) |
| Debt + finance leases / total assets | 70,423 / 527,854 = **13.3%** |
| **Net cash (cash+securities – debt – finance leases)** | **+$73.9B** |
| Net cash incl. operating leases | 144,306 – 146,062 = **–$1.8B (≈neutral)** |
| EBIT / interest expense | **11.6x** |
| EBITDA / interest expense | **26.9x** |
| ROA (NI ÷ avg assets) | **6.14%** |
| Asset turnover | **1.16x** |
| DSO (AR ÷ revenue × 365) | **33.2 days** (2022: 30.1) |
| DPO (COGS ÷ AP × 365) | **101.8 days** (2022: 100.6) |

**Interpretation:** Amazon is in a **net-cash position of ~$74B** on financial debt and **essentially lease-neutral** once $75.6B of operating-lease liabilities are capitalized. Debt was reduced 13% with **zero long-term debt issued in 2023**. Offsetting risks: (a) **AR grew 23.4% vs revenue +11.8%** (DSO +3.1 days) — watch receivables quality, though the allowance is only 1.6% of gross AR ($1.7B) and write-offs were $1.6B; (b) **unfunded lease/purchase commitments are large**: undiscounted operating leases **$90.8B**, total contractual obligations **$300.4B**, with **$39.3B due within 12 months**; (c) **IPR&D deferred-tax assets doubled to $14.8B** — evidence of acquisition activity in 2023 (accounting artifact of purchase accounting, not organic growth).

---

## 7. Capital allocation & financing

| | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| LT debt issued | 19,003 | 21,166 | **0** |
| LT debt repaid | 1,590 | 1,258 | 3,676 |
| ST debt issued | 7,956 | 41,553 | 18,129 |
| ST debt repaid | 7,753 | 37,554 | 25,677 |
| Share repurchases | **0** | 6,000 | **0** |
| Dividends | 0 | 0 | **0** |
| Capex | 61,053 | 63,645 | 52,729 |
| SBC (non-cash comp) | 12,757 | 19,621 | 24,023 |
| Unrecognized SBC (unvested, 12/31/23) | — | — | **18,300** |

**Takeaway:** FY23 capital allocation was **deleveraging + liquidity build**, not shareholder returns: no buyback, no dividend, no new LT debt, +$19.6B of cash. With **$73.9B net cash**, **$84.9B annual OCF**, and **$18.3B of unrecognized SBC** still to be expensed, the balance sheet has ample headroom — but investors get **zero direct cash return** and absorb **~1.4% annual share growth** from stock compensation.

---

## 8. Quality-of-earnings flags

| Flag | Evidence | Direction |
|---|---|---|
| FCF improvement partly non-operational | Capex –$10.9B of the +$49.1B FCF swing | ⚠️ Watch 2024 capex |
| Cash conversion genuinely strong | OCF/NI = 2.79x; OCF = 14.8% of revenue | ✅ Positive |
| Tax tailwind fading | Cash taxes +85% to $11.2B; effective rate 19.0%; deferred tax benefit –$5.9B | ⚠️ EPS headwind |
| Non-operating volatility | Equity marks: +$11.6B (’21), –$13.6B (’22), +$1.0B (’23) | ⚠️ Unpredictable EPS noise |
| Interest income now near-offsets interest expense | $2,949M vs $3,182M (net cost only $233M vs $1,378M) | ✅ but rate-dependent |
| Revenue visibility | Deferred revenue +29.8% to $20.9B; $12.4B of it recognized in FY23 | ✅ Positive |
| Dilution | Shares 10,242M → 10,383M (+1.4%); SBC 4.2% of revenue | ⚠️ Mild |
| Receivables vs revenue | AR +23.4% vs revenue +11.8% | ⚠️ Monitor |

---

## 9. Actionable takeaways for traders

1. **This is an operating-leverage print, not a revenue print.** Revenue +11.8% produced **operating income +201%** ($12.2B → $36.9B) and **+403 bp of operating margin**. The marginal dollar of revenue dropped through at extremely high incremental margin (~55% incremental operating margin: +$24.6B on +$60.8B). If you are positioned for margin expansion, the FY23 10-K validates the thesis with hard numbers.
2. **Gross margin is the single most important line: 47.0% (+317 bp).** Cost of sales grew only 5.5% against 11.8% revenue growth. Any reversal (e.g., re-acceleration in low-margin retail/fulfillment mix or AI infrastructure depreciation) hits this first. Watch the **COGS/revenue ratio (53.0%)** each quarter.
3. **Free cash flow inflected to +$32.2B from –$16.9B — but ~$10.9B of the swing is lower capex.** Treat FY23 FCF as partly a **capex-holiday artifact**. The single biggest swing factor for 2024 AMZN FCF is the capex line (FY23: $52.7B, 9.2% of revenue; capex/D&A 1.08x). A guided step-up would compress FCF while arguably improving the long-term franchise — a classic "good news/bad news" setup.
4. **Balance-sheet optionality is the underappreciated item:** **+$73.9B net cash**, debt down 13%, zero LT issuance, zero buyback. That is dry powder for either a large buyback initiation, M&A (IPR&D DTA doubling hints at purchase activity), or self-funded AI capex. A capital-return announcement would be a re-rating catalyst; continued silence leaves the cash idle.
5. **Model the tax normalization.** Book tax rate went from a **benefit** in FY22 to a **19.0% charge** in FY23, with cash taxes up 85% to $11.2B. Do not extrapolate FY23 EPS growth without assuming a mid-to-high-teens-to-~20% forward tax rate; the FY22 tax credit will not repeat.
6. **EPS sensitivity for scenario work:** each **+100 bp of operating margin** on FY24 revenue of ~$640B ≈ **+$6.4B operating income ≈ +$5.2B net income ≈ +$0.50/share**. FY23 diluted EPS was $2.90 on a 6.41% margin — an 8% margin scenario implies ~$3.70+ EPS before non-operating items. This is why the stock trades on margin trajectory, not units.
7. **Don't lean on FY23 net income vs FY21:** FY23 NI ($30.4B) is *below* FY21 ($33.4B) purely due to the Rivian equity-mark swing. Compare **operating income** ($36.9B vs $24.9B) and **EBITDA** ($85.5B vs $59.3B) for the true trajectory.
8. **Lease-adjusted leverage is neutral, not net-cash-rich.** On a fully loaded basis (operating leases capitalized), net cash goes from +$73.9B to roughly **–$1.8B**. In a rising-rate/refinancing-stress tape, AMZN is sturdier than levered peers but not immune; $39.3B of contractual obligations fall due within 12 months.
9. **No insider signal is available.** The vendor explicitly has **no point-in-time insider-transactions archive for AMZN as of 2024-02-02**. Do not read management conviction (or lack of it) into this report — that data does not exist here.
10. **Positioning summary:** fundamentals support a **constructive, quality-of-earnings-led long thesis** (margin expansion, positive FCF, net cash, deferred revenue +30%), with the principal near-term risks being (i) capex re-acceleration compressing FCF, (ii) tax-rate normalization, and (iii) receivables/DSO creep. There is **no valuation conclusion in this report** because price/market-cap data was not provided — pair these statements with your own price data (e.g., FY23 diluted EPS $2.90; FCF/share $3.10; net cash/share $7.11) to compute P/E, P/FCF, and EV/FCF.

---

## 10. Key points summary table

| Category | Metric (as of / for FY2023, filed 2024-02-02) | Value | Signal |
|---|---|---|---|
| Scale | Revenue (derived) | $574,785M (+11.8% y/y) | ✅ Solid double-digit growth |
| Profitability | Gross margin | 47.0% (+317 bp) | ✅ Strongly positive |
| Profitability | Operating income / margin | $36,852M / 6.41% (+403 bp) | ✅ Operating leverage |
| Profitability | Net income / margin | $30,425M / 5.29% | ✅ vs –$2,722M FY22 |
| Per share | Diluted EPS | $2.90 (FY22: –$0.27) | ✅ Recovery |
| Non-GAAP | EBITDA proxy / margin | $85,515M / 14.9% | ✅ vs 10.5% FY22 |
| Cash generation | Operating cash flow | $84,946M (+81.7%) | ✅✅ Exceptional |
| Cash generation | Capex | $52,729M (–17.2%) | ⚠️ FCF boosted by cuts |
| Cash generation | **Free cash flow** | **+$32,217M** (vs –$16,893M) | ✅✅ Multi-year inflection |
| Cash generation | Q4-implied OCF | ~$42,465M (+45.6% y/y) | ✅ Momentum into 2024 |
| Balance sheet | Cash + marketable securities | $144,306M | ✅ |
| Balance sheet | Debt + finance leases | $70,423M (–13.2% debt) | ✅ Deleveraging |
| Balance sheet | Net cash (financial) | +$73,883M | ✅✅ Optionality |
| Balance sheet | Net cash incl. op. leases | ≈ –$1.8B | ➖ Lease-neutral |
| Balance sheet | Current ratio / working capital | 1.05x / +$7.4B | ➖ Thin but positive |
| Leverage | EBIT / interest | 11.6x | ✅ |
| Efficiency | Asset turnover / ROA | 1.16x / 6.14% | ✅ Improving |
| Efficiency | DSO / DPO | 33.2 days / 101.8 days | ⚠️ DSO +3.1 days |
| Cost discipline | Advertising expense | $20,300M (–1.5%) | ✅ First absolute decline |
| Cost discipline | G&A | $11,816M (–0.6%) | ✅ |
| Compensation | SBC / unrecognized SBC | $24,023M / $18,300M | ⚠️ Real dilution cost |
| Capital returns | Buybacks / dividends (FY23) | $0 / $0 | ➖ None |
| Financing | New LT debt issued (FY23) | $0 | ✅ |
| Taxes | Effective rate / cash taxes | 19.0% / $11,179M (+85%) | ⚠️ Tailwind fading |
| Visibility | Deferred revenue | $20,927M (+29.8%) | ✅ |
| Commitments | Total contractual obligations / due <12M | $300,409M / $39,345M | ⚠️ Sizeable |
| Accounting | Net deferred tax liability | $13,197M (+75.7%); IPR&D DTA $14,800M | ⚠️ Acquisition-related |
| Insider activity | AMZN insider transactions | **DATA UNAVAILABLE** | ❔ No signal |
| Segment detail | NA / International / AWS revenue & margin | **Not in dataset** (3 segments confirmed) | ❔ |
| Equity detail | Total equity, retained earnings, goodwill | **Not in dataset** | ❔ |

---

**Bottom line:** The FY2023 10-K (public 2024-02-02) documents AMZN's cleanest fundamental year since 2021 — **revenue +11.8%, operating income tripled, gross margin +317 bp, FCF +$32.2B, net cash +$73.9B, debt down 13%** — while flagging three things a trader must discount for: **FCF was helped by a 17% capex cut**, **the tax rate normalized sharply higher**, and **lease/purchase commitments remain very large ($300B total, $39B due within a year)**. Insider-transaction evidence is explicitly unavailable and is not factored in.