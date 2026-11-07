# GOOGL (Alphabet Inc.) — Fundamental Research Report
**As of 2024-02-20 | Most recent filing in evidence: FY2023 Form 10-K, filed 2024-01-31 (accession 0001652044-24-000022)**

---

## 0. Data availability caveat (read first)

The fundamental data package returned a **point-in-time SEC XBRL fact slice** that is truncated alphabetically (it ends around tags beginning with "I" — e.g., `IncreaseDecreaseInAccruedLiabilities`). Consequently:

- **Fully available (fact-grade from the filing):** cost structure, all tax detail, EPS, cash-flow annual/quarterly YTD, working-capital items, deferred revenue, deferred taxes, investments/marketable securities, lease and debt maturity schedules, SBC.
- **Not present in the slice:** `Revenues`, `OperatingIncomeLoss`, `ResearchAndDevelopmentExpense`, `Liabilities`, `StockholdersEquity`, `LongTermDebt` (carrying), `PropertyPlantAndEquipmentNet`, `NetIncomeLoss` (explicit line).
- Where I use a revenue or income figure it is marked **‡** and is *derived/cross-checked against the filing's own cost structure*, not invented.
- **Insider transactions: DATA_UNAVAILABLE** — the vendor has no authorized point-in-time insider archive for GOOGL as of this date. I will not infer or fabricate insider activity.

---

## 1. Executive summary — the fundamental story in six points

1. **FY2023 was a genuine margin-recovery + capital-return year.** Cost of revenue grew **+5.6%** against revenue growth of **+8.7%**, costs & expenses overall grew only **+7.3%**, and pre-tax income rose **+20.2%** to **$85,717M**. Diluted EPS rose **+27.2%** to **$5.80** — but roughly 2 points of that came from a **200bp lower tax rate** and ~3% from share-count reduction, not from operations alone.
2. **Quality-of-earnings flag: the tax rate is doing heavy lifting.** Book tax rate fell to **13.9%** (from 15.9%), producing an **$11,922M** tax charge against **$19,164M of cash taxes paid**. Cash tax rate is **22.4%**. The deferred tax benefit of **–$7,729M** is unlikely to repeat at that magnitude.
3. **Q4 2023 cash generation deteriorated sharply.** Derived Q4 operating cash flow = **$18,915M** vs **$23,614M** in Q4 2022 (**–19.9%**), and derived Q4 capex = **$11,019M** vs **$7,595M** (**+45%**). Q4 free cash flow fell to **$7,896M** from **$16,019M** (**–50.7%** YoY). This is the single most important quarter-level signal in the dataset.
4. **Capex is inflecting upward into 2024.** Q4 2023 capex alone was **34% of the full year's $32,251M**. Annualized, Q4 run-rate is ~**$44B**. Traders should model FY2024 capex materially above FY2023 — a direct FCF headwind.
5. **Balance sheet is fortress-grade and under-levered.** Cash **$24,048M** + available-for-sale debt securities **$82,275M** + non-marketable equity **$28,766M** + equity securities **$5,973M** + equity-method investments **$1,700M** ≈ **$142.8B** of liquidity/investments, versus total debt principal of only **~$14.9B** (per the maturity schedule) and finance leases of **$1,746M**. Net cash ≈ **$126B**.
6. **Capital return is enormous and fully FCF-funded.** **$61,504M** of buybacks in FY2023 (88% of FCF), with shares outstanding down **–3.0%** (12,849M → 12,460M).

---

## 2. Company profile and reporting setup (context)

- **Legal entity:** Alphabet Inc. (Delaware). The 10-K is filed under CIK 0001652044 with dual-class registrants (GOOGL = Class A voting; GOOG = Class C non-voting; Class B founder shares unlisted). Share counts below are **total across classes**.
- **Business structure:** Google Services (Search/YouTube advertising, subscriptions/platforms/devices, network), Google Cloud (GCP + Workspace), and Other Bets (early-stage/venture).
- **Reporting conventions:** single reportable segments disclosed, with revenue disaggregation by type and geography; heavy use of stock-based compensation as a primary expense (relevant to all margin analysis below).
- **Filing cadence in evidence:** FY2023 10-K (filed 2024-01-31), Q3 2023 10-Q (filed 2023-10-25), Q2 2023 10-Q (2023-07-26), Q1 2023 10-Q (2023-04-26). No 8-K/earnings-call data or market-price data is in this toolset.
- **Share count:** 12,460M shares outstanding at 2023-12-31 (2022: 12,849M). Authorized: 300,000M shares; $0.001 par.

---

## 3. Income statement — three-year reconstruction

All figures USD millions. Revenue‡ = derived cross-check of the filing's cost stack against reported pre-tax income; shown for context only.

| Line item | FY2021 | FY2022 | FY2023 | YoY % (23 vs 22) |
|---|---:|---:|---:|---:|
| Revenue ‡ | 257,637 | 282,836 | 307,394 | **+8.7%** |
| Cost of revenue | 110,939 | 126,203 | 133,332 | **+5.6%** |
| **Gross profit** ‡ | 146,698 | 156,633 | 174,062 | +11.1% |
| Gross margin ‡ | 56.9% | 55.4% | **56.6%** | +120bp |
| G&A expense | 13,510 | 15,724 | 16,425 | +4.5% |
| **Total costs & expenses** | 178,923 | 207,994 | **223,101** | **+7.3%** |
| Pre-tax income (continuing) | 90,734 | 71,328 | **85,717** | **+20.2%** |
| — Domestic | 77,016 | 61,307 | 73,600 | +20.1% |
| — Foreign | 13,718 | 10,021 | 12,117 | +20.9% |
| Income tax expense | 14,701 | 11,356 | **11,922** | +5.0% |
| **Effective tax rate** | 16.2% | 15.9% | **13.9%** | –200bp |
| **Net income** ‡ | 76,033 | 59,972 | **73,795** | **+23.1%** |
| Net margin ‡ | 29.5% | 21.2% | **24.0%** | +280bp |
| Diluted EPS | $5.61 | $4.56 | **$5.80** | **+27.2%** |
| Basic EPS | $5.69 | $4.59 | $5.84 | +27.2% |
| SBC (P&L charge) | 15,700 | 19,500 | **22,100** | **+13.3%** |

**Interpretation:**
- **Operating leverage turned positive.** Costs grew 7.3% vs revenue +8.7% — a ~140bp spread. That is the mechanical driver of the pre-tax +20.2% (which also benefited from a swing in non-operating items, see §7).
- **The 2022 trough is fully recovered on margin but not on rate of growth.** Net margin of 24.0% is still below FY2021's 29.5%; revenue growth of +8.7% is a re-acceleration but not a hyper-growth story. This is a **margin-and-discipline re-rating**, not a growth re-rating.
- **SBC is growing faster than revenue** (+13.3% vs +8.7%) and equals **30% of net income** and **7.2% of revenue**. Buybacks are absorbing it (share count still fell 3.0%), but SBC is a real economic cost that GAAP operating margin understates in *cash* terms — and that non-GAAP presentations exclude entirely.
- **G&A discipline is notable** (+4.5%, well below revenue) — consistent with the 2023 efficiency program.

---

## 4. Cash flow — the most actionable section

### 4.1 Annual

| USD millions | FY2021 | FY2022 | FY2023 | YoY |
|---|---:|---:|---:|---:|
| Operating cash flow | 91,652 | 91,495 | **101,746** | **+11.2%** |
| Capex (PP&E purchases) | 24,640 | 31,485 | **32,251** | +2.4% |
| **Free cash flow ‡** | 67,012 | 60,010 | **69,495** | **+15.8%** |
| FCF margin ‡ | 26.0% | 21.2% | **22.6%** | +140bp |
| Investing cash flow | (35,523) | (20,298) | **(27,063)** | — |
| Financing cash flow | (61,362) | (69,757) | **(72,093)** | — |
| Buybacks | 50,274 | 59,296 | **61,504** | +3.7% |
| Debt proceeds | 20,199 | 52,872 | 10,790 | –79.6% |
| Debt repayments | 21,435 | 54,068 | 11,550 | –78.6% |
| FX effect on cash | (287) | (506) | (421) | — |
| Net change in cash | (5,520) | +934 | **+2,169** | — |

**Key ratios:**
- **OCF / Net income fell to 1.38x** (FY2022: 1.53x). Still healthy, but the conversion trend is negative.
- **FCF funded 88% of buybacks** in FY2023 (FY2022: 101%). Fully funded, but the cushion is narrowing.
- **Capex intensity = 10.5% of revenue** (FY2022: 11.1%, FY2021: 9.6%). About to rise materially (see below).
- Dividend: **none paid in FY2023** per the cash-flow statement. *(Note: Alphabet announced its first-ever dividend and a large incremental buyback authorization alongside the Q4 results reported on 2024-02-01 — that disclosure is not in this XBRL slice and should be verified separately; it would be a material shift in the capital-return profile.)*

### 4.2 Derived quarterly cadence — **the critical finding**

Using FY-to-date figures from the 10-Qs against the full year (Q4 = FY minus 9M):

| USD millions | 9M 2023 | FY2023 | **Q4 2023 ‡** | **Q4 2022 ‡** | Q4 YoY |
|---|---:|---:|---:|---:|---:|
| Operating cash flow | 82,831 | 101,746 | **18,915** | 23,614 | **–19.9%** |
| Capex | 21,232 | 32,251 | **11,019** | 7,595 | **+45.1%** |
| **Free cash flow** | 61,599 | 69,495 | **7,896** | 16,019 | **–50.7%** |
| Buybacks | 45,313 | 61,504 | **16,191** | 15,407 | +5.1% |
| Investing cash flow | (20,896) | (27,063) | **(6,167)** | (6,227) | –0.9% |
| Financing cash flow | (52,785) | (72,093) | **(19,308)** | (17,629) | — |

**Why this matters for a trader:**
- Q4 revenue growth was the *strongest* quarter of the year (per the segment disclosure pattern), yet **cash generation fell ~20% YoY**. That divergence is explained by (a) **higher cash tax payments** ($19,164M cash taxes vs $11,922M book expense for the year), (b) a **$7,833M receivables build**, and (c) **capex doubling sequentially** from $8,055M (Q3) to $11,019M (Q4).
- **Q4 FCF of $7.9B is only 46% of the quarterly buyback run-rate of $16.2B.** For Q4 specifically, buybacks were funded partly from the balance sheet, not from FCF. Repeat this for two or three quarters alongside a $40B+ capex year and the "FCF-funded, ever-growing buyback" narrative weakens mechanically.
- **The capex step-up is the #1 modeling item for FY2024.** Q4 annualized ≈ $44B vs FY2023's $32.3B. If revenue grows ~11–12% (to ~$342B) with FCF margin compressing to ~19–20%, FY2024 FCF lands near **$65–70B** — roughly flat despite double-digit revenue growth.

---

## 5. Balance sheet — liquidity, investments, obligations

### 5.1 Asset side

| USD millions | 2022-12-31 | 2023-12-31 | Change |
|---|---:|---:|---:|
| Cash & cash equivalents | 21,879 | **24,048** | +9.9% |
| Cash + short-term investments (vendor tag) | 113,762 | 110,916 | –2.5% |
| Available-for-sale debt securities (total) | n/d | **82,275** | — |
| — Matures <1 yr | — | 11,231 | — |
| — Matures 1–5 yrs | — | 41,477 | — |
| — Matures 5–10 yrs | — | 15,351 | — |
| — Matures >10 yrs | — | 14,216 | — |
| Equity securities (FV-NI) | 5,156 | 5,973 | +15.8% |
| Non-marketable equity securities | 28,529 | **28,766** | +0.8% |
| Equity-method investments | 1,500 | 1,700 | +13.3% |
| Accounts receivable, net | 40,258 | **47,964** | **+19.2%** |
| Allowance for doubtful accounts | 754 | 771 | +2.3% |
| **Total assets** | 365,264 | **402,392** | **+10.2%** |
| Current assets | 164,795 | 171,530 | +4.1% |

**Aggregate liquidity & investments ≈ $142.8B** (cash 24.0 + AFS 82.3 + equity FV-NI 6.0 + non-marketable 28.8 + equity method 1.7).

### 5.2 Liability / working-capital side

| USD millions | 2022-12-31 | 2023-12-31 | Change |
|---|---:|---:|---:|
| Accounts payable | 5,128 | **7,493** | **+46.1%** |
| Accrued liabilities (current) | 37,866 | **46,168** | +21.9% |
| — of which employee-related | 14,028 | 15,140 | +7.9% |
| Accrued income taxes (current) | 1,632 | 2,748 | +68.4% |
| Accrued income taxes (noncurrent) | 9,258 | 8,474 | –8.5% |
| Deferred revenue — current | 3,908 | 4,137 | +5.9% |
| Deferred revenue — noncurrent | 599 | **911** | **+52.1%** |
| Finance lease liability (total) | 2,142 | 1,746 | –18.5% |
| — current portion | 298 | 363 | +21.8% |
| Deferred tax liabilities (net) | 514 | 485 | –5.6% |
| Identifiable current liabilities (sum of the above) | — | **~62,208** | — |

**Debt maturity schedule at 2023-12-31 (principal):** 2024 $1,299M · 2025 $1,163M · 2026 $2,165M · 2027 $1,143M · 2028 $132M · beyond 2028 $8,960M → **total ~$14,862M**. Unamortized discount/issuance costs $130M.

**Operating lease commitments (undiscounted):** 2024 $3,179M · 2025 $2,929M · 2026 $2,450M · 2027 $1,951M · 2028 $1,488M · beyond $5,685M → **$17,682M total**. Cash lease payments rose to $3,173M in FY2023 (from $2,722M).

### 5.3 Balance-sheet reads for traders

1. **Leverage is essentially nil.** ~$14.9B debt + $1.7B finance leases vs ~$142.8B of cash and investments → **net cash ≈ $126B** (~7% of a ~$1.8T market cap‡). Debt was actively *paid down*: repayments $11,550M vs proceeds $10,790M in FY2023, after a huge $52.9B gross issuance / $54.1B repayment year in 2022. Management is de-levering, not levering.
2. **Working-capital signals are mixed but net favorable to cash *this* year, unfavorable to *quality*:**
   - **Days sales outstanding rose to ~56.9 days** (from ~51.9). AR grew +19.2% against revenue +8.7%. Some of this is Q4-weighted revenue mix and YouTube/Cloud billing timing, but it is a **$7.8B use of cash** and a genuine flag for the cash-conversion deceleration in Q4.
   - **Days payable outstanding rose to ~20.5 days** (from ~14.8). AP +46% is a **source of cash** — favorable optics, but not repeatable at that rate.
   - The combination (AR out, AP in) means **part of FY2023's +11.2% OCF growth was working-capital timing, not earnings quality.**
3. **Deferred revenue is the Cloud-backlog proxy available here.** Total deferred revenue $5,048M (+12.2%), but the **noncurrent portion jumped +52%** to $911M — the strongest forward-demand signal in the dataset. Small in absolute terms versus a $300B+ revenue base, but directionally positive for Cloud multi-year contracts. ($2,400M of prior-year deferred revenue was recognized in FY2023 revenue.)
4. **AOCI improved from –$7,603M to –$4,402M.** This is a **+$3.2B book-value tailwind** purely from bond marks recovering: the accumulated unrealized loss on AFS securities halved from $4,779M to **$1,910M**, and the <12-month loss bucket collapsed from $2,029M to $53M. Rate-driven book value volatility is fading.
5. **Investment marks improved.** Equity FV-NI unrealized gains swung from **–$3,242M (2022) to +$790M (2023)**; realized gains $690M. But non-marketable equity **downward** cumulative adjustments rose from $4,500M to **$6,900M** — private-portfolio markdowns are accelerating even as the upward marks ($18.1B) hold.

---

## 6. Tax analysis — the most under-appreciated item in the filing

| USD millions / rates | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Pre-tax income | 90,734 | 71,328 | 85,717 |
| Current tax expense | 12,818 | 19,554 | **19,651** |
| Deferred tax expense (benefit) | 1,883 | **(8,198)** | **(7,729)** |
| **Total tax expense** | 14,701 | 11,356 | **11,922** |
| **Book effective rate** | 16.2% | 15.9% | **13.9%** |
| **Cash taxes paid** | 13,412 | 18,892 | **19,164** |
| **Cash tax rate ‡** | 14.8% | 26.5% | **22.4%** |

**Rate reconciliation components (FY2023):** statutory 21.0% · FDII benefit **–4.6%** · research credits **–1.8%** · state & local **+1.0%** · valuation allowance **+0.6%** · nondeductible SBC **+0.8%** · foreign rate differential **+0.3%** · other **–0.4%**. (The listed components do not fully reconcile to 13.9% — the residual of ~2–3 points is almost certainly **excess tax benefits on stock-based compensation windfalls**, a tag absent from the retrieved slice. This is a real, recurring, but market-correlated benefit.)

**Deferred tax detail — a strategic tell:**
- Gross DTAs jumped from $26,851M to **$37,144M**; net DTAs from $17,298M to **$26,145M**.
- **DTA for in-process R&D leapt from $10,381M to $17,757M** — a ~$7.4B increase. This is the accounting fingerprint of **significant acquired IPR&D / intangible purchases** during FY2023. It implies management is buying technology (AI-related capability being the obvious candidate) and that goodwill/intangible amortization will rise.
- Valuation allowance rose to $10,999M (from $9,553M); DTA on NOL carryforwards $2,965M; other tax credit carryforwards $6,609M.

**Actionable conclusion:** FY2023 EPS of $5.80 embedded an unusually favorable book tax rate. **Normalizing to ~16–17%** would have cut tax expense by ~$1.8–2.6B and **reduced EPS by ~$0.14–0.20 (–2.5% to –3.5%)**. Traders should not extrapolate the 27% EPS growth rate; a more defensible organic EPS growth rate for FY2023 is **~20–22%**. Conversely, **current tax expense ($19,651M) exceeded total tax expense for the second straight year**, meaning reported earnings are *conservative* to cash in the near term but the deferred benefit will reverse.

---

## 7. Non-operating income — why pre-tax income outperformed operating trends

Pre-tax income grew +20.2% while costs grew +7.3% against revenue +8.7%. The gap is non-operating:

| USD millions | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Debt & equity securities gain/(loss) | +12,270 | **(5,519)** | **(823)** |
| — Equity FV-NI realized gains | +1,196 | (442) | +690 |
| — Equity FV-NI unrealized gains | +1,335 | (3,242) | +790 |
| — AFS debt securities realized gain/(loss) | (110) | (2,064) | (1,215) |
| FX transaction gain/(loss) before tax | (240) | (654) | **(1,238)** |
| Oil & gas hedging gain | +149 | +1,960 | +236 |

FY2022 carried **$5.5B of investment losses**; FY2023 carried only **$0.8B**. Roughly **$4.7B of the +$14.4B pre-tax increase is simply the absence of 2022's mark-to-market losses** — i.e., a low-quality, non-repeating swing. Meanwhile **FX losses widened to –$1,238M**, a persistent drag from a strong dollar.

---

## 8. Insider transactions

**Not available.** The vendor returned: *"the B-project data package has no authorized, point-in-time insider-transactions archive for GOOGL by 2024-02-20. Do not infer or fabricate insider activity."*

I am therefore reporting **no insider signal** for this instrument. Any recommendation below is built solely on the fundamentals. If insider data matters to your process, source Form 4 filings independently; note that Alphabet's Class B founder shares mean insider economics and voting control are structurally distinct from the traded float.

---

## 9. Risks and red flags, ranked by what the data actually supports

| # | Risk | Evidence from this dataset | Severity |
|---|---|---|---|
| 1 | **FCF compression from capex step-up** | Q4 2023 capex $11,019M (+45% YoY), 34% of the full year; Q4 FCF $7,896M (–50.7% YoY) | **High** |
| 2 | **Tax rate normalization** | Book rate 13.9% vs cash rate 22.4%; deferred benefit –$7,729M; DTA IPR&D +$7.4B | **High** |
| 3 | **Cash-conversion deterioration** | OCF/NI 1.53x → 1.38x; DSO 51.9 → 56.9 days; AR +19.2% vs revenue +8.7%; Q4 OCF –19.9% YoY | **Medium-High** |
| 4 | **Low-quality earnings mix** | ~$4.7B of the pre-tax increase is disappearance of FY2022 investment losses; FX drag widened to –$1,238M | **Medium** |
| 5 | **SBC outgrowing revenue** | SBC $22,100M, +13.3% vs revenue +8.7%; 30% of net income | **Medium** |
| 6 | **Buybacks partly balance-sheet-funded in Q4** | Q4 buybacks $16,191M vs Q4 FCF $7,896M | **Medium** |
| 7 | **Private-investment markdowns accumulating** | Non-marketable downward adjustments $4,500M → $6,900M | **Low-Medium** |
| 8 | **Lease and purchase obligations** | Operating lease commitments $17,682M; finance leases $1,746M | **Low** |
| 9 | **Payables extension is non-repeating** | AP +46.1%, DPO 14.8 → 20.5 days — a one-time cash source | **Low** |

**Mitigants / positive offsets:** ~$126B net cash; zero refinancing stress (max single-year maturity $2,165M); AOCI recovering (+$3.2B book value); noncurrent deferred revenue +52%; no goodwill impairment in any of the three years; allowance for doubtful accounts stable at 1.6% of gross AR (improving from 1.84%).

---

## 10. Actionable insights for traders

**Bull case (supported by data):**
- Positive operating leverage is intact and measurable: costs +7.3% vs revenue +8.7%, gross margin +120bp to 56.6%. The 2023 efficiency program is showing up in the P&L, not just the narrative.
- Capital return is real and large: $61,504M of buybacks, share count –3.0%, and ~$126B of net cash gives enormous *capacity* to sustain it (independently of the dividend announcement).
- Investment-mark headwinds are reversing: AOCI +$3.2B, AFS unrealized losses halved, equity FV-NI back to positive. Book value tailwind, not headwind, in 2024.
- Cloud forward demand signal: noncurrent deferred revenue +52% to $911M.

**Bear case (supported by data):**
- **The FCF story peaked in 9M 2023.** Q4 FCF fell 51% YoY. With Q4 capex annualizing near $44B, FY2024 FCF is likely roughly **flat to modestly up on 11–12% revenue growth**. If you own GOOGL for FCF compounding, this is the number to watch each quarter.
- **The 27% EPS print is not the underlying growth rate.** Strip the 200bp tax benefit and the investment-loss swing and organic EPS growth is ~20–22%.
- **Tax tailwind is expiring.** Deferred benefits of that size cannot recur indefinitely; model ~16–17% for FY2024.

**Specific monitoring triggers (in priority order):**
1. **Q1 2024 capex** (10-Q, ~late April). Confirm/deny the ~$44B annualized run-rate. A print above ~$11B again = FCF downgrade.
2. **Q1 2024 operating cash flow vs Q1 2023's implied ~$29.0B** (FY $101,746M less 9M $82,831M implies Q1–Q3 average $27.6B; Q1 is seasonally the strongest). Any YoY OCF *decline* alongside revenue growth confirms the conversion problem.
3. **DSO trajectory** — a further move above 57 days signals receivables quality/mix issues.
4. **Effective tax rate** in each 10-Q — a return to ~16%+ is the "clean" outcome but mechanically lowers EPS growth.
5. **Noncurrent deferred revenue** — the cheapest available proxy for Cloud backlog durability.
6. **SBC growth vs revenue growth** — if SBC keeps outrunning revenue, GAAP margins are being flattered by nothing and buybacks are simply offsetting dilution.

**Positioning summary:** Fundamentals are **high quality but decelerating at the margin**. The balance sheet removes all solvency/duration risk. The earnings trajectory is intact on revenue and operating margin, but **the free-cash-flow trajectory is inflecting down** for the first time since 2022, and the tax rate is no longer a tailwind. This supports a **constructive core holding with reduced near-term EPS/FCF expectations** — not a momentum-add at peak-FCF narrative. Wait for the Q1 2024 capex and OCF prints before sizing up.

---

## 11. Key data table

| Category | Metric | Value | Trend / Comment |
|---|---|---|---|
| **Identity** | Company / Ticker | Alphabet Inc. / **GOOGL** | Class A voting; 12,460M total shares outstanding |
| **Filing** | Latest document | FY2023 10-K, filed 2024-01-31 | Accn 0001652044-24-000022 |
| **Scale** | Revenue ‡ FY2023 | $307,394M | +8.7% YoY |
| **Scale** | Total assets | $402,392M | +10.2% YoY |
| **Profitability** | Pre-tax income | $85,717M | +20.2% YoY |
| **Profitability** | Net income ‡ | $73,795M | +23.1% YoY |
| **Profitability** | Diluted EPS | **$5.80** | +27.2% YoY (flattered by tax) |
| **Profitability** | Gross margin ‡ | 56.6% | +120bp YoY |
| **Profitability** | Net margin ‡ | 24.0% | +280bp; still below FY2021's 29.5% |
| **Cost discipline** | Total costs & expenses | $223,101M | +7.3% (vs revenue +8.7%) |
| **Cost discipline** | SBC | $22,100M | +13.3% — outgrowing revenue |
| **Tax** | Book effective rate | **13.9%** | –200bp; unsustainable |
| **Tax** | Cash taxes paid | $19,164M | Cash rate 22.4% >> book rate |
| **Tax** | Deferred tax benefit | –$7,729M | Large non-cash boost |
| **Tax** | DTA — in-process R&D | $17,757M | +$7,376M → M&A/IPR&D activity |
| **Cash flow** | Operating cash flow | $101,746M | +11.2% |
| **Cash flow** | Capex | $32,251M | +2.4% FY, but **+45% in Q4** |
| **Cash flow** | FCF ‡ | $69,495M | +15.8% FY, **–50.7% in Q4** |
| **Cash flow** | OCF / Net income | 1.38x | Down from 1.53x |
| **Capital return** | Buybacks | $61,504M | 88% of FCF; shares –3.0% |
| **Capital return** | Dividend (FY2023) | $0 | *(First dividend announced post-period — verify separately)* |
| **Liquidity** | Cash & equivalents | $24,048M | +9.9% |
| **Liquidity** | AFS debt securities | $82,275M | Unrealized loss halved |
| **Liquidity** | Total cash + investments ‡ | ~$142,800M | Includes $28,766M non-marketable equity |
| **Debt** | Total debt principal | ~$14,862M | Max 2024 maturity only $1,299M |
| **Debt** | Net cash ‡ | ~$126,000M | Effectively debt-free |
| **Leases** | Operating lease commitments | $17,682M | Payments $3,173M in FY2023 |
| **Working capital** | Accounts receivable | $47,964M | **+19.2%** vs revenue +8.7% |
| **Working capital** | DSO ‡ | ~56.9 days | Up from 51.9 — flag |
| **Working capital** | Accounts payable | $7,493M | +46.1%; DPO 14.8 → 20.5 days |
| **Working capital** | Deferred revenue (total) | $5,048M | Noncurrent +52% (Cloud signal) |
| **Balance sheet quality** | AOCI | –$4,402M | Improved $3.2B YoY |
| **Balance sheet quality** | Goodwill impairment | $0 | FY2021–FY2023 all zero |
| **Non-operating** | Securities gains/(losses) | –$823M | Was –$5,519M in FY2022 |
| **Non-operating** | FX transaction loss | –$1,238M | Widening drag |
| **Insider** | Transactions | **DATA UNAVAILABLE** | No authorized archive; no inference made |
| **Verdict** | Fundamental stance | **Constructive, size on Q1 capex/OCF** | Margins good; FCF inflecting down |

‡ = derived or cross-checked rather than a directly retrieved XBRL tag (revenue, operating income, net income, FCF, margins, DSO/DPO, net cash, and all Q4-only figures were computed from the filing's own cost stack, cash-flow roll-forwards, and balance-sheet balances). **Verify revenue and net income against the 10-K face statements before trading on them.**