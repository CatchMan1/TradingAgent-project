# GOOGL (Alphabet Inc.) — Fundamental Deep-Dive
### Point-in-time data compiled 2026-08-25 | Most recent SEC filing: Q2 2026 Form 10-Q, accepted 2026-07-23

---

## 1. Data Provenance & Limitations (read first)

| Item | Status |
|---|---|
| Financial statements (income, balance sheet, cash flow) | ✅ Retrieved from SEC-fact cache, Q2 2026 10-Q filed 2026-07-23 (accn 0001652044-26-000071) plus FY2025 10-K filed 2026-02-05 |
| Company profile / segment revenue | ⚠️ Not present in returned tag set — no segment-level or product-line revenue tags were available |
| Price / market cap / valuation multiples | ❌ Not provided by tools — **no P/E, P/S or EV multiples can be computed**; do not rely on any such figure in this report |
| Insider transactions | ❌ **DATA_UNAVAILABLE** — vendor has no authorized point-in-time insider archive for GOOGL. No insider activity is reported or inferred here |
| Revenue line items | ⚠️ `Revenues` tag not returned; revenue **derived arithmetically** as `CostsAndExpenses + OperatingIncomeLoss` (validated: derived Q2'25 revenue $96.43B matches reported Alphabet revenue) |
| Acquisition line items | ⚠️ Not returned; ~$36.4B of investing outflow is un-itemized and inferred to be M&A (see §6) |

All figures in USD millions unless stated. Q2 2026 = quarter ended 2026-06-30.

---

## 2. Company Profile (as resolved)

**Alphabet Inc.** — ticker **GOOGL** (Class A common). Holding company for Google and Other Bets: Google Services (Search & other advertising, YouTube ads, Android, Chrome, Google Play, devices, subscriptions/cloud-adjacent consumer), Google Cloud (infrastructure + Workspace/enterprise AI), and Other Bets (long-horizon ventures). Revenue is predominantly advertising plus a fast-growing cloud and subscriptions base; the company also carries an unusually large investment portfolio of marketable and *non-marketable* equity securities, which is materially relevant to 2026 results (see §5).

---

## 3. Executive Summary — 6 findings that matter

1. **Core business re-accelerated.** Derived 1H26 revenue **$229,692M, +23.1% YoY**; Q2'26 revenue **$119,796M, +24.2% YoY** vs Q1'26 **+21.8%**. Growth is accelerating sequentially, not decelerating.
2. **Operating leverage improved.** 1H26 operating margin **35.0%** vs **33.1%**; gross margin **62.0%** vs **59.6%** (+240bp). Q2'26 operating margin 34.0% (vs 32.4%), though down ~210bp sequentially from Q1'26's 36.1%.
3. **Reported EPS is heavily — and unsustainably — inflated.** 1H26 pre-tax income $216,165M included **$135,803M of gains on debt & equity securities (62.8% of pre-tax income)**. Q2'26 net income $112,193M vs $28,196M (+298%) and diluted EPS $9.11 vs $2.31. **Ex-securities-gains, 1H26 EPS is ≈$5.30 vs ≈$4.35 — up ~22%, i.e. in line with revenue, not up 178%.**
4. **Free cash flow has inflected sharply negative.** Q2'26 FCF = **–$5,855M** (Q2'25: +$5,301M). 1H26 FCF **$4,261M vs $24,254M (–82%)** as capex **doubled to $80,598M (+103% YoY)**, reaching **37.5% of Q2 revenue**.
5. **Capital structure was transformed in six months.** Gross capital raised **$109.5B** (debt +$56.2B, common stock +$30.5B, convertible preferred +$19.1B, minority +$3.8B). Long-term debt carrying value **doubled to $101,085M**; total assets **+54.9% to $921,983M**; **buybacks went to zero** ($0 vs $28,306M in 1H25).
6. **Balance sheet remains fortress-grade.** Cash + short-term investments **$242,474M** vs debt $101,085M → **net cash ≈ +$141B**; 1H26 operating cash flow **$84,859M (+32.8%)**; interest coverage ~44x.

**Net read:** fundamentally strong and accelerating core with genuinely improving margins, but the equity story in 2026 is being carried by non-cash revaluations while the cash-generation profile is being deliberately re-levered toward AI infrastructure. Traders must separate the two.

---

## 4. Income Statement Analysis

### 4.1 Derived revenue and margin build (USD millions)

| Metric | Q1'25 | Q2'25 | 1H'25 | Q1'26 | Q2'26 | 1H'26 | 1H YoY |
|---|---|---|---|---|---|---|---|
| Revenue (derived) | 90,234 | 96,428 | 186,662 | 109,896 | 119,796 | **229,692** | **+23.1%** |
| Cost of revenue | 36,361 | 39,039 | 75,400 | 41,271 | 45,943 | 87,214 | +15.7% |
| Gross profit | 53,873 | 57,389 | 111,262 | 68,625 | 73,853 | **142,478** | +28.1% |
| Gross margin | 59.7% | 59.5% | 59.6% | 62.4% | 61.7% | **62.0%** | +240bp |
| Opex (R&D+S&M+G&A, derived) | 23,267 | 26,118 | 49,385 | 28,929 | 33,083 | 62,012 | +25.6% |
| Opex % of revenue | 25.8% | 27.1% | 26.5% | 26.3% | 27.6% | 27.0% | +50bp |
| G&A (reported) | 3,539 | 5,209 | 8,748 | 4,291 | 6,461 | 10,752 | +22.9% |
| Operating income | 30,606 | 31,271 | 61,877 | 39,696 | 40,770 | **80,466** | **+30.0%** |
| Operating margin | 33.9% | 32.4% | 33.1% | 36.1% | 34.0% | **35.0%** | +190bp |
| Non-operating income | 11,183 | 2,662 | 13,845 | 37,716 | 97,983 | **135,699** | ~10x |
| Pre-tax income | 41,789 | 33,933 | 75,722 | 77,412 | 138,753 | **216,165** | +185% |
| Tax | — | 5,737 | 12,986 | 14,834 | 26,560 | 41,394 | +219% |
| Effective tax rate | — | 16.9% | 17.1% | — | 19.1% | **19.1%** | +200bp |
| Net income | 34,540 | 28,196 | 62,736 | 62,578 | 112,193 | **174,771** | +179% |
| Diluted EPS | ~2.81 | 2.31 | 5.12 | ~5.13 | **9.11** | **14.24** | +178% |

### 4.2 Quality of earnings — the single most important adjustment

| USD millions | 1H'25 | 1H'26 |
|---|---|---|
| Pre-tax income | 75,722 | 216,165 |
| Less: gains on debt & equity securities | (11,411) | (135,803) |
| Pre-tax ex-securities gains | 64,311 | **80,362** |
| After tax (17.1% / 19.1%) | 53,314 | 65,013 |
| Diluted shares (M) | 12,261 | 12,273 |
| **Normalized diluted EPS** | **$4.35** | **$5.30 (+21.8%)** |
| Reported diluted EPS | $5.12 | $14.24 (+178%) |

- **~62% of 1H26 pre-tax profit and roughly 63% of reported EPS came from securities marks**, not operations. Note that pre-tax ex-securities ($80,362M) is essentially identical to operating income ($80,466M) — net interest + FX netted to roughly –$104M, meaning the company's interest income no longer offsets interest expense now that debt has doubled.
- Within the equity-securities gain: 1H26 unrealized **$21,531M**, realized **$836M**, with a far larger residual (~$113.6B of the $135.9B `EquitySecuritiesFvNiGainLoss`) consistent with **upward revaluation of non-marketable holdings**. Supporting evidence: carrying value of securities *without readily determinable fair value* rose **$64,094M → $124,259M (+$60,165M)** in six months and cumulative upward price adjustments rose **$44,485M → $85,732M**. The remainder is plausibly mark-ups on listed equity stakes (classified separately from unrealized gains in the income statement). *(Classification is inference; the aggregate securities gain is reported.)*
- **Implication:** reported EPS is a poor proxy for earnings power and will swing violently with private-AI and public-market valuations. Expect equally violent *negative* marks in a down market.

### 4.3 Cost-side pressure points

- **Stock-based compensation: 1H26 $15,200M vs $11,500M (+32.2%)** — faster than revenue. SBC is now **6.6% of revenue** (6.2% in 1H25). Q2'26 alone $8,000M. This is a real dilution/free-cash-flow drag, not just a GAAP item (offset by the buyback halt — see §6).
- **Depreciation: 1H26 $13,586M vs $9,485M (+43.2%)** — the first visible wave of AI-capex depreciation. Given 1H26 capex of $80,598M plus $29,113M incurred-but-unpaid, **depreciation growth will accelerate materially in H2'26 and FY2027** and is the primary structural threat to the current gross-margin expansion.
- **Interest expense: 1H26 $1,811M vs $295M (+514%)**, Q2'26 $1,278M vs $261M. Direct consequence of the debt doubling; run-rate is now ~$5B+/yr.
- **Tax rate: 19.1% vs 17.1%** (+200bp) — partly driven by the taxable/unrealized gains and a **deferred tax liability that jumped from $919M to $22,819M**.

---

## 5. Balance Sheet — a six-month transformation

| USD millions | 2025-12-31 | 2026-06-30 | Change |
|---|---|---|---|
| Cash & equivalents | 30,708 | 55,911 | +82.1% |
| Cash + short-term investments | 126,843 | **242,474** | **+91.2%** |
| Accounts receivable, net | 62,886 | 69,175 | +10.0% |
| Total current assets | 206,038 | 343,524 | +66.7% |
| Non-marketable equity securities | 64,094 | 124,259 | +93.9% |
| **Total assets** | **595,281** | **921,983** | **+54.9%** |
| Accounts payable | 12,200 | 20,258 | +66.0% |
| Accrued liabilities | 55,557 | 73,014 | +31.4% |
| Deferred revenue (current / total) | 6,578 / 8,600 | 7,154 / 10,100 | +8.8% / +17.4% |
| **Long-term debt (carrying)** | **49,085** | **101,085** | **+105.9%** |
| Deferred income tax liabilities | 919 | 22,819 | ~25x |
| Operating lease liability | 15,954 | 18,037 | +13.1% |
| Finance lease liability | 2,500 | 2,590 | +3.6% |
| Loss-contingency accrual (current) | 15,594 | 17,356 | +11.3% |
| Convertible preferred stock | 0 | 18,023 | new |
| Common stock + APIC | 93,126 | 131,371 | +41.1% |
| AOCI | (1,916) | (2,285) | worse |
| Shares outstanding (M) | 12,088 | 12,230 | **+142M (+1.2%)** |

**Observations**
- **Net cash position ≈ +$141.4B** (cash+ST investments less debt), plus $18.0B of operating-lease capacity consumed and $2.6B of finance leases. Liquidity is not a constraint at any plausible capex scenario.
- **Debt more than doubled in six months.** Unamortized discount/issuance costs rose to –$921M, indicating a large new issuance program. Maturity ladder from the last 10-K showed only $2.0B due in the next 12 months and $36.1B beyond year five — so the new debt is long-dated.
- **Deferred tax liability of $22.8B** is the tax accrual on unrealized investment gains. This is a *reversible* liability: a decline in those marks would reverse both the gains and this liability, producing optically poor GAAP tax lines and negative non-operating income in the same quarter.
- **$18.0B convertible preferred issued June 2026** (proceeds $19,063M; the $86M preferred dividend in Q2 confirms it is now paying). This is a **new, senior claim ahead of common** and a future dilution overhang. Alongside $30.5B of *common stock issuance* — unprecedented for Alphabet — it implies a large capital-consuming transaction or co-investment was funded in 1H26.
- **Working capital is not stretching:** receivables +10% against revenue +23% (strong collection/DSo improvement), and deferred revenue +17% (solid forward bookings, though modest relative to revenue growth).
- **Legal accruals up $1.76B to $17.4B** — regulatory/antitrust exposure remains a live, growing liability.

---

## 6. Cash Flow — the real story of 2026

| USD millions | Q1'25 | Q2'25 | 1H'25 | Q1'26 | Q2'26 | 1H'26 | 1H YoY |
|---|---|---|---|---|---|---|---|
| Operating cash flow | 36,150 | 27,747 | 63,897 | 45,790 | 39,069 | **84,859** | **+32.8%** |
| Capex (PP&E purchases) | 17,197 | 22,446 | 39,643 | 35,674 | 44,924 | **80,598** | **+103.3%** |
| **Free cash flow** | 18,953 | 5,301 | 24,254 | 10,116 | **(5,855)** | **4,261** | **–82.4%** |
| Capex / revenue | 19.1% | 23.3% | 21.2% | 32.5% | **37.5%** | 35.1% | +1,390bp |
| Capex / OCF | 47.6% | 80.9% | 62.0% | 77.9% | **115.0%** | 95.0% | +3,300bp |

**1H26 cash flow structure (USD millions):**

| Line | 1H'26 | 1H'25 |
|---|---|---|
| Operating | **+84,859** | +63,897 |
| Investing | **–145,822** | –40,738 |
| — Capex | (80,598) | (39,643) |
| — Net marketable securities | (9,784) | +1,060 |
| — Other investments (net) | (20,384) | (1,439) |
| — Other investing | +1,359 | +363 |
| — *Un-itemized residual (inferred M&A)* | **≈(36,415)** | ≈(1,079) |
| Financing | **+86,320** | –26,033 |
| — Debt proceeds | +56,226 | +31,378 |
| — **Common stock issued** | **+30,499** | 0 |
| — Convertible preferred | +19,063 | 0 |
| — Minority interests | +3,758 | +400 |
| — Dividends paid | (5,231) | (4,977) |
| — **Share repurchases** | **0** | **(28,306)** |
| — Debt/lease repayments | (5,253) | (18,397) |
| FX on cash | (154) | +444 |

**Key conclusions**
1. **Q2'26 was the first quarterly FCF deficit.** OCF of $39.1B was fully consumed — and then some — by $44.9B of capex. For a business that generated $24B of 1H25 FCF, this is a regime change and the primary valuation risk in the name.
2. **The buyback is gone.** $0 in 1H26 vs $28.3B in 1H25. FY2025 buybacks were already slowing (financing outflow –$37.4B in FY25 vs –$79.7B in FY24). Capital allocation has fully rotated to AI infrastructure.
3. **They are funding capex with external capital, not internal cash.** ~$109.5B raised in six months across four instruments. This is the single clearest signal that management expects capex to remain elevated for multiple years, and it introduces dilution (common +142M shares, plus $18.0B convertible preferred) where buybacks previously reduced share count.
4. **Capex commitments are still building:** capex incurred but not yet paid rose to **$29,113M** from $10,635M (+174%). That is contracted spend that will hit Q3/Q4 cash flow — **do not assume $44.9B/quarter is the peak**.
5. **~$36.4B of investing outflow is un-itemized** in the returned fact set; combined with $30.5B of common stock issuance, this is consistent with a large stock-and-cash-funded acquisition or equity investment during 1H26. *(Inferred, not directly reported — treat as a hypothesis to verify against the 10-Q/10-K full text.)*
6. Dividend policy intact and still growing: $0.21 → $0.22 per quarter ($0.43 declared for 1H26 vs $0.41 in 1H25). Payout is trivially small (~$10B/yr vs $84.9B 1H OCF) — the dividend is symbolic, not a support for the stock.

---

## 7. Financial History & Trajectory

| | FY2023 | FY2024 | FY2025 | 1H2026 (annualized) |
|---|---|---|---|---|
| Financing cash flow (USD M) | (72,093) | (79,733) | (37,388) | +86,320 → **+172,640** |
| Finance-lease principal paid | 705 | 405 | 1,988 | 840 |
| Capex incurred but unpaid, year-end | 7,435 | 10,326 | 15,090 | **29,113** |
| LT debt due next 12 months (last reported) | — | — | 2,000 | — |
| LT debt due after year 5 (last reported) | — | — | 36,145 | — |

**Trajectory read:** three consecutive years of large financing outflows (buybacks) through FY2025 have flipped to a **massive inflow** in 2026. The unpaid-capex balance has compounded at ~30–40%/yr for three years and is now growing faster than ever — a leading indicator that the capex ramp is not finished. The FY2025 debt maturity profile ($2.0B due within 12 months vs $36.1B beyond year five) argues the new debt is long-dated and rollover risk is negligible.

---

## 8. Insider Transactions

**Not available.** The data vendor returned `DATA_UNAVAILABLE` — there is no authorized, point-in-time insider-transactions archive for GOOGL as of 2026-08-25. **No insider buying or selling is reported, and none has been inferred or fabricated.** Any insider-flow claim made elsewhere about this ticker should be treated as unverified for this window. (Form 4 data would have to be sourced from EDGAR directly.)

---

## 9. Risks & Red Flags (ranked)

| # | Risk | Evidence | Severity |
|---|---|---|---|
| 1 | **FCF compression / capex ROI** | Q2'26 FCF –$5,855M; capex 37.5% of revenue; capex/OCF 115%; unpaid capex +174% | **High** |
| 2 | **Low-quality earnings** | 62.8% of 1H26 pre-tax income from securities gains; normalized EPS $5.30 vs $14.24 reported | **High** |
| 3 | **Rising depreciation** | D&A +43.2% in 1H26; will accelerate on $80.6B capex | **High** |
| 4 | **Dilution / capital structure complexity** | Shares +142M; $18.0B convertible preferred; $30.5B common issued; buyback at zero | Medium-High |
| 5 | **Debt service costs** | Interest expense +514% to $1,811M; debt $101.1B; net interest now a drag | Medium |
| 6 | **SBC growth above revenue** | SBC +32.2% vs revenue +23.1%; 6.6% of revenue | Medium |
| 7 | **Reversible tax position** | DTL $22.8B tied to unrealized gains; tax rate 19.1% (+200bp) | Medium |
| 8 | **Sequential margin slippage** | Q2'26 op margin 34.0% vs Q1'26 36.1% | Medium |
| 9 | **Regulatory/legal** | Accrued contingencies $17.4B, +$1.8B in six months | Medium |
| 10 | **Concentration in private marks** | Non-marketable equity $124.3B = 13.5% of total assets | Medium |

**Offsets / bull case:** revenue acceleration (21.8% → 24.2%), gross margin +240bp, operating margin +190bp, OCF +32.8%, net cash +$141B, interest coverage ~44x, forward bookings (deferred revenue) +17%.

---

## 10. Actionable Insights for Traders

**Do:**
1. **Value the core on operating income, not net income.** Use **1H26 operating income $80,466M (+30% YoY)** and normalized EPS **~$5.30 (+22%)** as the earnings anchor. Reported EPS of $14.24 will not annualize at that level; quarterly EPS will oscillate with private-AI valuations and could see symmetric *negative* marks.
2. **Track three quarterly numbers above all else:** (a) capex dollars, (b) OCF, (c) operating margin. If capex keeps rising while operating margin slips below ~33%, the "AI spend is margin-accretive" narrative breaks and the multiple should compress. If Q3'26 FCF turns positive again on capex deceleration, that is a powerful positive catalyst for a re-rating.
3. **Watch depreciation as the H2'26 swing factor.** +43% in 1H26 with $80.6B of capex booked and $29.1B unpaid. Model depreciation growth well above revenue growth — it caps gross-margin expansion even if unit economics stay healthy.
4. **Monitor the capital-raising cadence.** A fourth funding leg (further debt, equity, or preferred) in H2'26 would confirm capex is being re-forecast upward again — bearish for FCF and per-share metrics, but bullish for suppliers/leverage to the AI theme.
5. **Use the securities portfolio as a volatility signal, not a value driver.** Non-marketable stakes at $124.3B (13.5% of assets) with $85.7B of cumulative upward adjustments: a 10% mark-down would cost ~$12.4B pre-tax (~$1.00/share) plus reversal of the $22.8B DTL.
6. **Respect the reduced shareholder-return support.** No buyback + higher share count removes a multi-year bid that historically absorbed ~1.5–2% of shares annually. Expect EPS-per-share growth to lag net income growth by roughly the dilution rate (~1.2% per half).

**Don't:**
- Don't compare GOOGL's reported P/E or EPS growth to peers this cycle — the $135.8B securities gain distorts both by a wide margin.
- Don't assume the historic "FCF machine" template applies in 2026; FCF yield is currently ~3–4% of what it was, before accounting for the larger share count.
- Don't act on insider signals — no data is available for this instrument in this window.

**Trade framing (evidence-based, not price-based):** the fundamental data support a **constructive stance on the operating business** (accelerating revenue, expanding margins, fortress liquidity) paired with **caution on cash-flow-based valuation**. The de-rating risk is in the FCF/depreciation axis; the upside risk is a capex plateau in H2'26 that restores positive FCF. Both outcomes are resolvable at the Q3'26 print — position for that binary.

---

## 11. Key Points Summary

| Category | Metric | Value | Signal |
|---|---|---|---|
| **Revenue** | Q2'26 (derived) | $119,796M, +24.2% YoY | 🟢 Accelerating (Q1'26 +21.8%) |
| Revenue | 1H'26 (derived) | $229,692M, +23.1% YoY | 🟢 Strong |
| **Profitability** | 1H'26 gross margin | 62.0% (+240bp) | 🟢 Expanding |
| Profitability | 1H'26 operating margin | 35.0% (+190bp) | 🟢 Expanding |
| Profitability | Q2'26 operating margin | 34.0% (Q1'26: 36.1%) | 🟡 Sequential slippage |
| Profitability | 1H'26 operating income | $80,466M, +30.0% | 🟢 Core engine healthy |
| **Earnings quality** | Securities gains / pre-tax income | $135,803M = **62.8%** | 🔴 Very low quality |
| Earnings quality | Reported 1H'26 diluted EPS | $14.24 (+178%) | 🔴 Inflated |
| Earnings quality | Normalized 1H'26 diluted EPS | **~$5.30 (+21.8%)** | 🟡 In line with revenue |
| **Cash flow** | 1H'26 operating cash flow | $84,859M, +32.8% | 🟢 |
| Cash flow | 1H'26 capex | $80,598M, **+103.3%** | 🔴 Doubling |
| Cash flow | **Q2'26 free cash flow** | **–$5,855M** (Q2'25: +$5,301M) | 🔴 **Negative inflection** |
| Cash flow | Capex/revenue Q2'26 | 37.5% (Q2'25: 23.3%) | 🔴 |
| Cash flow | Capex incurred, unpaid | $29,113M (+174%) | 🔴 More spend coming |
| **Balance sheet** | Cash + ST investments | $242,474M | 🟢 |
| Balance sheet | Long-term debt | $101,085M (+105.9%) | 🟡 Doubled |
| Balance sheet | Net cash | **≈ +$141.4B** | 🟢 Fortress |
| Balance sheet | Total assets | $921,983M (+54.9% in 6M) | 🟡 Transformed |
| Balance sheet | Deferred tax liability | $22,819M (from $919M) | 🟡 Reversible/unrealized |
| Balance sheet | Non-marketable equity | $124,259M (+93.9%) | 🟡 Mark-to-model risk |
| Balance sheet | Shares outstanding | 12,230M (+142M) | 🟡 Dilution |
| **Capital allocation** | 1H'26 gross capital raised | ~$109,546M | 🟡 Debt + equity + preferred |
| Capital allocation | 1H'26 buybacks | **$0** (1H'25: $28,306M) | 🔴 Support removed |
| Capital allocation | Dividend | $0.22/qtr ($0.43 in 1H'26) | 🟢 Growing, immaterial |
| **Costs** | SBC 1H'26 | $15,200M, +32.2% (6.6% of rev) | 🔴 Above revenue growth |
| Costs | Depreciation 1H'26 | $13,586M, +43.2% | 🔴 Capex flow-through |
| Costs | Interest expense 1H'26 | $1,811M (+514%) | 🟡 From debt doubling |
| Costs | Effective tax rate | 19.1% (vs 17.1%) | 🟡 +200bp |
| **Other** | Legal/contingency accruals | $17,356M (+$1.8B) | 🟡 Regulatory overhang |
| Other | Insider transactions | **DATA UNAVAILABLE** | ⚪ No signal possible |
| Other | Valuation multiples | **Not computable** (no price data) | ⚪ Use normalized EPS |
| **Bottom line** | Core operating trend | Accelerating revenue + expanding margins | 🟢 |
| Bottom line | Cash conversion | FCF –82% YoY, negative in Q2 | 🔴 |
| Bottom line | Reported earnings | Dominated by non-cash marks | 🔴 |

**Net verdict: operating fundamentals are as good as they have been in years; the cash-flow and earnings-quality picture is the weakest in the company's modern history. Trade the divergence — own the operating momentum, hedge or underweight the FCF/depreciation and private-mark exposure — and let the Q3'26 capex number be the tiebreaker.**