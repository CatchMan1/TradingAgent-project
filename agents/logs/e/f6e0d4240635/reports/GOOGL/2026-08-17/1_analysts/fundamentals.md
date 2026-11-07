# GOOGL — Alphabet Inc. Fundamental Research Report
**Analysis date: 2026-08-17 | Latest data: Q2 FY2026 10-Q, accepted 2026-07-23 | FY2025 10-K accepted 2026-02-05**

---

## 0. Executive Summary

The most recent filings (Q2 FY2026, quarter ended 2026-06-30) show Alphabet at an inflection point that cuts two ways:

- **Operationally excellent:** derived revenue of **$119.8B in Q2 2026, +24.2% YoY** (H1: **$229.7B, +23.1%**), with **gross margin up ~215–240bp** and **operating margin up ~90–190bp** to **34.0% (Q2) / 35.0% (H1)**. Operating income grew **+30.4% YoY in Q2** and **+30.0% in H1** — faster than revenue.
- **Earnings quality is poor at the headline level:** H1 2026 GAAP net income of **$174.8B** includes **$135.9B of non-operating equity-securities gains** (mark-to-market / observable-transaction revaluations). **~78% of H1 net income is non-operating and largely non-cash.** Reported diluted EPS of **$14.24 (H1)** / **$9.11 (Q2)** massively overstates run-rate earnings power; my estimate of "core" (ex-investment-gain) EPS is roughly **$5.29 (H1)** and **$2.60 (Q2)**, still **+21–20% YoY**.
- **The balance sheet has been transformed in six months:** total assets **$595.3B → $922.0B (+54.9%)**. Debt doubled to **$101.1B**, **$19.1B of convertible preferred** was issued in June 2026 (first-ever), **$30.5B of common stock** was issued, buybacks went to **zero**, and capex **more than doubled**.
- **Free cash flow has collapsed:** H1 2026 FCF **$4.26B vs $24.25B** (-82%); **Q2 2026 FCF was approximately –$5.9B**. Capex/revenue hit **37.5%** in Q2.

**Bottom line for traders: the operating business is accelerating, but the equity story has shifted from "capital-return compounder" to "levered, equity-funded AI capex cycle with temporarily negative free cash flow and inflated GAAP EPS."** Value GOOGL off operating income and core EPS, not off the $14.24 headline.

---

## 1. Data Provenance and Limitations (read first)

The fundamental dataset returned for GOOGL is a point-in-time SEC XBRL fact set. Three important caveats:

1. **Revenue is not directly present** in the returned tag set. I derived it as `Revenue = CostsAndExpenses + OperatingIncomeLoss` (equivalent to CostOfRevenue + R&D + S&M + G&A + OpInc). This method reproduces known historical values exactly (H1 2025 → $186.66B; Q2 2025 → $96.43B), so I treat the derived 2026 figures as reliable.
2. **Several balance-sheet tags are truncated** in the returned extract (goodwill, net PP&E, total stockholders' equity, total liabilities, and the acquisitions line in investing cash flow are not shown). I have **not** estimated or fabricated those figures; where a metric depends on them (e.g., debt/equity, book value, exact acquisition spend), I say so.
3. **Insider transactions: DATA UNAVAILABLE.** The vendor reports no authorized point-in-time insider-transaction archive for GOOGL as of 2026-08-17. **No insider buying/selling is inferred or reported here.** Treat this as an open information gap, not as evidence of absence of insider activity.

---

## 2. Company Profile

Alphabet Inc. (NASDAQ: GOOGL — Class A common; Class C trades as GOOG). Alphabet is the parent of Google, organized around Google Services (Search & other, YouTube ads, Google Network, subscriptions/platforms/devices), Google Cloud (Google Cloud Platform + Google Workspace), and Other Bets (early-stage ventures). The consolidated financials reviewed here are Alphabet-level; the returned tag set does **not** contain segment-level revenue or operating income, so segment mix cannot be quantified from this data. *(Profile items here are identity/context; all figures below are from the filings.)*

---

## 3. Income Statement — Q2 FY2026 and H1 FY2026

### 3.1 Derived quarterly progression ($ millions)

| Metric | Q1 2025 | Q2 2025 | H1 2025 | Q1 2026 | Q2 2026 | H1 2026 |
|---|---|---|---|---|---|---|
| Revenue (derived) | 90,234 | 96,428 | 186,662 | 109,896 | 119,796 | 229,692 |
| Cost of revenue | 36,361 | 39,039 | 75,400 | 41,271 | 45,943 | 87,214 |
| Gross profit (derived) | 53,873 | 57,389 | 111,262 | 68,625 | 73,853 | 142,478 |
| **Gross margin** | 59.7% | 59.5% | 59.6% | 62.4% | **61.7%** | **62.0%** |
| Operating income | 30,606 | 31,271 | 61,877 | 39,696 | 40,770 | 80,466 |
| **Operating margin** | 33.9% | 32.4% | 33.1% | 36.1% | **34.0%** | **35.0%** |
| G&A expense | 3,539 | 5,209 | 8,748 | 4,291 | 6,461 | 10,752 |
| SBC (allocated) | 5,500 | 6,000 | 11,500 | 7,200 | 8,000 | 15,200 |
| Depreciation | n/d | n/d | 9,485 | n/d | n/d | 13,586 |
| Interest income | 1,001 | 1,050 | 2,051 | 1,381 | 1,430 | 2,811 |
| Interest expense | 34 | 261 | 295 | 533 | 1,278 | 1,811 |
| Non-operating income | 11,183 | 2,662 | 13,845 | 37,716 | 97,983 | 135,699 |
| Pre-tax income | 41,789 | 33,933 | 75,722 | 77,412 | 138,753 | 216,165 |
| Tax expense | 7,249 | 5,737 | 12,986 | 14,834 | 26,560 | 41,394 |
| **Effective tax rate** | 17.3% | 16.9% | 17.1% | 19.2% | **19.1%** | **19.1%** |
| **Net income** | 34,540 | 28,196 | 62,736 | 62,578 | 112,193 | 174,771 |
| Diluted EPS | $2.81 | $2.31 | $5.12 | ~$5.13 | **$9.11** | **$14.24** |
| Basic EPS | — | $2.33 | $5.16 | — | $9.23 | $14.41 |

*(Q1 figures derived as H1 minus Q2; Q2 2026 diluted share count ≈12.31B, H1 ≈12.27B.)*

### 3.2 What actually drove the quarter

**Revenue +24.2% YoY (Q2) / +23.1% (H1), with acceleration from +21.8% in Q1 to +24.2% in Q2 (+9.0% QoQ).** This is the strongest growth signal in the dataset, and it is corroborated by:
- **Deferred revenue (contract liabilities) $10.10B vs $8.60B** at 2025-12-31 (**+17.4%**), with $4.9B of H1 revenue recognized from the opening contract-liability balance — a hard, cash-backed forward-demand indicator.
- **Accounts receivable $69.18B vs $62.89B (+10.0%)** — growing *slower* than revenue (+23%), i.e. collections/DSO improved, and this is not a receivables-stuffing quarter. Allowance for doubtful accounts is only $995M (1.4% of AR).

**Margins expanded despite AI infrastructure cost pressure.** Gross margin improved to 61.7% from 59.5% (+215bp) and operating margin to 34.0% from 32.4% (+160bp). Cost of revenue grew only **+17.7%** YoY in Q2 versus revenue +24.2% — the single most bullish operating datapoint in the file.

**But two cost lines are inflating fast and are structural, not one-off:**
- **Depreciation $13.59B in H1 (+43.2% YoY)** — the front edge of the capex wave. With $80.6B of H1 capex and $29.1B of capex *incurred but not yet paid*, depreciation growth will re-accelerate materially into 2027.
- **SBC $8.00B in Q2 (+33.3% YoY)**, now **6.7% of revenue** (H1: $15.2B, 6.6% of revenue) versus 6.2% a year ago. G&A also rose +24.0% in Q2.

**Interest expense exploded: $1,278M in Q2 vs $261M (+390%)** and $1.81B in H1 vs $0.30B. This is the direct P&L cost of the debt-funded capex program. Coverage is still trivial (EBIT/interest ≈ 32x), but the trajectory is what matters.

**Effective tax rate rose to 19.1% from 16.9–17.1%** — a ~220bp headwind that will persist as book (not cash) investment gains accrue deferred tax.

---

## 4. Earnings Quality — the single most important analytical adjustment

| $ millions | H1 2026 | H1 2025 | Q2 2026 | Q2 2025 |
|---|---|---|---|---|
| Operating income | 80,466 | 61,877 | 40,770 | 31,271 |
| Non-operating income, total | 135,699 | 13,845 | 97,983 | 2,662 |
| — of which equity securities FVNI gains | **135,946** | 11,044 | **99,031** | 1,286 |
| — of which realized gains on equity sec. | 836 | 435 | 278 | 217 |
| — of which unrealized (marketable) | 21,531 | 1,088 | 21,399 | 853 |
| Reported net income | 174,771 | 62,736 | 112,193 | 28,196 |
| **Non-operating share of net income** | **77.6%** | 22.1% | **87.3%** | 9.4% |
| **Est. core pre-tax (op income + other, ex-FVNI gains)** | ~80,219 | ~64,678 | ~39,570 | ~31,858 |
| **Est. core net income** | ~64,900 | ~53,600 | ~32,000 | ~26,500 |
| **Est. core diluted EPS** | **~$5.29** | ~$4.38 | **~$2.60** | ~$2.17 |
| **Core EPS growth YoY** | **+20.8%** | — | **+19.8%** | — |

**Interpretation:** $135.9B of H1 pre-tax income came from equity-securities revaluation. The tell-tale corroboration is on the balance sheet:
- **Non-marketable equity securities rose from $64.09B to $124.26B** (+$60.2B in six months).
- **Cumulative *upward* price adjustments on those stakes jumped from $44.49B to $85.73B (+$41.2B)** — i.e., a wave of "observable transactions" (new funding rounds, secondary marks, or liquidity events) re-rated Alphabet's private portfolio.
- **Deferred income tax liabilities jumped from $0.92B to $22.82B (+$21.9B)** — book gains recognized with essentially no current cash tax.
- Cash flow confirms: **deferred income taxes add-back was +$27.54B in H1 2026 vs –$1.60B in H1 2025.**

**Trader takeaway:** Do not annualize $14.24. Core run-rate is roughly **$10.6–11.0 of annualized EPS** (2× the ~$5.29 H1 core), with Q3/Q4 seasonally stronger. The GAAP-vs-core gap of ~$9/share is a mark-to-market artifact that can reverse violently if private/public tech valuations de-rate — and it is a *non-cash* gain that will never appear in FCF.

---

## 5. Balance Sheet — a $327B transformation in six months

| $ millions | 2025-12-31 | 2026-06-30 | Δ |
|---|---|---|---|
| **Total assets** | **595,281** | **921,983** | **+326,702 (+54.9%)** |
| Current assets | 206,038 | 343,524 | +137,486 (+66.7%) |
| Cash & equivalents | 30,708 | 55,911 | +25,203 |
| **Cash + short-term investments** | **126,843** | **242,474** | **+115,631 (+91.2%)** |
| AFS debt securities | — | 99,500 | — |
| Accounts receivable, net | 62,886 | 69,175 | +6,289 (+10.0%) |
| Non-marketable equity securities | 64,094 | 124,259 | +60,165 (+93.9%) |
| Finite-lived intangibles, gross | 2,467 | 10,585 | +8,118 (+329%) |
| Accounts payable | 12,200 | 20,258 | +8,058 (+66.0%) |
| Accrued liabilities | 55,557 | 73,014 | +17,457 (+31.4%) |
| Employee-related liabilities | 17,546 | 15,086 | –2,460 |
| Accrued income taxes, current | 523 | 5,233 | **+4,710 (+900%)** |
| Accrued income taxes, non-current | 9,531 | 11,306 | +1,775 |
| **Total debt (carrying)** | **49,085** | **101,085** | **+52,000 (+105.9%)** |
| Debt discount/issuance costs | (542) | (921) | — |
| Finance lease liabilities | 2,500 | 2,590 | +90 |
| Operating lease liabilities | 15,954 | 18,037 | +2,083 |
| **Convertible preferred stock** | **0** | **18,023** | **+18,023 (new)** |
| Common stock + APIC | 93,126 | 131,371 | +38,245 (+41.1%) |
| AOCI | (1,916) | (2,285) | –369 |
| Shares outstanding (M) | 12,088 | 12,230 | +142 (+1.17%) |
| Loss contingency accrual, current | 15,594 | 17,356 | +1,762 |

### 5.1 How the balance sheet was funded — and what it implies

Financing activities swung from **–$26.0B (H1 2025)** to **+$86.3B (H1 2026)**. Sources in H1 2026:
- **Debt proceeds $56.23B** (vs $31.38B), net of only **$5.25B of repayments** (vs $18.40B) → net debt +$52B.
- **Common stock issuance $30.50B** — historically *zero* for Alphabet. This is the most under-appreciated datapoint in the file: 142M new shares at an implied **~$215 average gross price**, consistent with a large equity-funded strategic transaction.
- **Convertible preferred issuance $19.06B gross / $18.02B carrying, dated 2026-06-05** — Alphabet's first-ever preferred. This sits *ahead* of common and pays $86M of dividends in a partial quarter.
- **Minority-shareholder contributions $3.76B** (vs $0.40B) — external capital into a consolidated subsidiary.
- Total gross capital raised in six months: **~$109.6B**, on top of $84.9B operating cash flow.

Meanwhile **investing outflow was $145.8B** (vs –$40.7B). Identifiable pieces: **capex $80.60B**, **purchases of other investments $22.05B**, net marketable securities purchases ~$9.8B, other investing $1.4B. That leaves roughly **~$32B of investing outflow not visible in the returned tag set** — most plausibly **acquisitions, net of cash acquired**, i.e. a material M&A event, consistent with the 329% jump in finite-lived intangibles ($2.47B → $10.59B) and the equity issuance. *This is an inference from the cash-flow arithmetic, not a directly reported line — verify against the 10-Q investing section before trading on it.*

### 5.2 Liquidity and leverage

- **Net cash position ≈ $138.8B** (cash + ST investments $242.5B – debt $101.1B – finance leases $2.6B). Alphabet remains comfortably net-cash even after doubling debt.
- **Gross debt grew 106% in six months; interest expense grew 390% YoY in Q2.** Blended implied cost of the H1 debt is ~4.8% annualized — the new paper is expensive relative to the legacy stack.
- **Current assets $343.5B (+66.7%)** dwarf current obligations; adding up the visible current liabilities (~$125B of AP, accrued, employee, taxes, contract liabilities, lease current) implies a current ratio around **2.5–2.8x**, but **total liabilities/equity could not be verified** from the truncated tag set.
- **Accrued income taxes current +900% to $5.23B** signals a step-up in near-term cash tax payments.
- **Loss contingency accrual of $17.36B** (up from $15.59B) is a large, growing legal/regulatory provision — consistent with ongoing antitrust/regulatory exposure. The FY2025 10-K also discloses a **$3.0B contingency payment in Q3 2025**.

---

## 6. Cash Flow and Capital Allocation — the regime change

| $ millions | H1 2025 | H1 2026 | Δ | Q2 2025 | Q2 2026 |
|---|---|---|---|---|---|
| Operating cash flow | 63,897 | **84,859** | +32.8% | 27,747 | 39,069 |
| OCF margin (derived rev.) | 34.2% | 36.9% | +270bp | 28.8% | 32.6% |
| **Capex (PP&E purchases)** | 39,643 | **80,598** | **+103.3%** | 22,446 | **44,924** |
| **Capex / revenue** | 21.2% | **35.1%** | +1,390bp | 23.3% | **37.5%** |
| **Free cash flow (OCF – capex)** | **24,254** | **4,261** | **–82.4%** | **5,301** | **–5,855** |
| **FCF margin** | 13.0% | **1.9%** | –1,110bp | 5.5% | **–4.9%** |
| Share repurchases | 28,306 | **0** | –100% | 13,238 | **0** |
| Dividends paid | 4,977 | 5,231 | +5.1% | 2,543 | 2,689 |
| Dividends per share declared | $0.41 | $0.43 | +4.9% | $0.21 | $0.22 |
| Capex incurred, not yet paid | 10,635 | **29,113** | +173.8% | — | — |

**Four conclusions:**

1. **Q2 2026 FCF was negative (~–$5.9B)** — the first clearly negative quarter in the dataset. H1 FCF fell **82%** to $4.26B against some ~$2.6T of implied market value; annualized H1 FCF yield is well under 0.5%.
2. **Buybacks were suspended entirely ($0 in both Q1 and Q2 2026 vs $28.3B in H1 2025).** Combined with a 1.17% increase in share count (+142M), the **multi-year ~2%/yr share-count tailwind has flipped to a ~1%+ headwind**. This removes a mechanical EPS driver that investors have relied on since 2015.
3. **Capex is not finished.** The **$29.1B of capex incurred but not yet paid** (vs $10.6B a year ago) is a forward indicator: Q3 2026 capex plausibly exceeds $45B, and full-year capex should comfortably exceed $170B. **Depreciation will follow with a lag, pressuring 2027 operating margins.**
4. **Dividend growth was cut to a token pace (+4.9% per share)** — consistent with capital being redirected to infrastructure and M&A.

---

## 7. Risk Register (what would change the thesis)

| # | Risk | Evidence in the data | Materiality |
|---|---|---|---|
| 1 | **Negative/compressed FCF** | Q2 2026 FCF –$5.9B; H1 FCF $4.3B (–82%) | High — valuation support weakens; removes buyback bid |
| 2 | **Depreciation cliff** | H1 depreciation +43% YoY on $80.6B H1 capex; $29.1B capex accrued unpaid | High — hits 2027 EPS |
| 3 | **Earnings quality / reversal risk on marks** | 77.6% of H1 NI non-operating; $135.9B FVNI gains; $60.2B of the gain sits in *non-marketable* marks ($41.2B cumulative upward adjustment added in 6 months) | High — a private-tech de-rating reverses reported EPS |
| 4 | **Leverage and preferred seniority** | Debt +106% to $101.1B; interest expense +390% YoY; $18.0B convertible preferred ahead of common | Medium — coverage still ~32x, but trend is new |
| 5 | **Tax** | ETR 17.1% → 19.1%; DTL $0.9B → $22.8B; accrued current tax +900% | Medium |
| 6 | **Dilution** | Shares 12.088B → 12.230B; SBC +33% YoY at 6.7% of revenue; preferred converts | Medium |
| 7 | **Legal/regulatory** | Loss contingency accrual $17.36B and rising; $3.0B contingency payment Q3 2025 | Medium–High (tail) |
| 8 | **Unverified M&A / capital deployment** | ~$32B of unexplained investing outflow; intangibles +329%; $30.5B equity raise | Medium — needs 10-Q confirmation |
| 9 | **Information gaps** | Segment data, goodwill, PP&E, total equity, and insider transactions unavailable | Medium — do not assume |

---

## 8. Actionable Insights for Traders

**Valuation discipline**
1. **Reject the $14.24 headline EPS.** Anchor on **core EPS of ~$5.29 (H1) ≈ $10.6 annualized**, growing ~20%. Any screen or model using GAAP TTM EPS (which now embeds $135.9B of marks) will show GOOGL at a spuriously low multiple. Conversely, a screen using FCF will show it at a spuriously *high* multiple. **Use EV/EBIT: operating income is the cleanest number in this filing, growing +30%.**
2. Model **2027 depreciation** deliberately: H1 depreciation of $13.6B on a capex base running at ~$170B+/yr annualized implies a multi-year step-up. A 500bp increment to depreciation/revenue erases most of the 2026 margin gains.

**Near-term catalysts / checkpoints**
3. **Q3 2026 print (late Oct 2026):** three things to watch, in order — (a) **capex guidance and whether FCF turns positive again**, (b) **revenue growth holding >20%**, (c) **depreciation guidance**. Capex above ~$50B in the quarter with flat FCF is a de-rating risk; capex discipline plus 20%+ growth is a re-rating setup.
4. **Watch the marks line.** If Q3 shows a *negative* equity-securities line, reported EPS could print dramatically below consensus even if the core business beats — a classic asymmetric short-term setup in the wrong direction. Trade the operating line, expect headline volatility.
5. **Deferred revenue ($10.1B, +17.4%)** is the best real-time proxy for Cloud/backlog demand; it is a cleaner signal than bookings commentary.

**Capital structure / flows**
6. **Buyback suspension + equity issuance changes the marginal buyer.** With no corporate bid and a rising share count, GOOGL is now more sensitive to flows and to private-market tech valuations (via the mark-to-market channel) than at any point in the last decade.
7. **$242B of liquidity and ~$139B net cash** means Alphabet is not financially constrained — the bear case is *return-on-capital*, not solvency. Do not short this on balance-sheet grounds.
8. **Preferred + conv-cap structure** introduces a small senior claim and potential future dilution; monitor conversions if the stock rallies hard.

**Positioning summary:** *Constructive on the operating business (accelerating 24% growth, 35% operating margin, expanding gross margin); cautious on the equity's earnings quality and free cash flow. The stock is a "growth-with-a-capex-problem" story rather than a "cash-return" story for the next 4–6 quarters. Preferred expression: own it on operating-multiple support, size down for headline-EPS volatility, and avoid models that use GAAP EPS or trailing FCF without normalization.*

---

## 9. Key Data Summary Table

| Category | Metric | Value | Context / Signal |
|---|---|---|---|
| **Identity** | Company / ticker | Alphabet Inc. / **GOOGL** | Point-in-time as of 2026-08-17 |
| **Filing** | Latest 10-Q | Acc. 2026-07-23, period end 2026-06-30 | FY2025 10-K acc. 2026-02-05 |
| **Growth** | Q2 2026 revenue (derived) | $119,796M | **+24.2% YoY**, +9.0% QoQ |
| **Growth** | H1 2026 revenue (derived) | $229,692M | **+23.1% YoY** |
| **Growth** | Deferred revenue | $10,100M | +17.4% vs 2025-12-31 (forward demand) |
| **Profitability** | Q2 operating income | $40,770M | **+30.4% YoY** |
| **Profitability** | H1 operating income | $80,466M | +30.0% YoY; 35.0% margin |
| **Profitability** | Q2 gross margin | 61.7% | +215bp YoY |
| **Profitability** | Q2 operating margin | 34.0% | +160bp YoY |
| **Earnings quality** | H1 net income | $174,771M | 77.6% from non-operating investment gains |
| **Earnings quality** | H1 equity securities FVNI gains | $135,946M | Largely non-cash mark-to-market |
| **Earnings quality** | H1 / Q2 diluted EPS (reported) | $14.24 / $9.11 | Not representative of run-rate |
| **Earnings quality** | Est. core diluted EPS (H1 / Q2) | **~$5.29 / ~$2.60** | **+20.8% / +19.8% YoY** |
| **Costs** | H1 depreciation | $13,586M | +43.2% YoY (capex wave) |
| **Costs** | Q2 SBC | $8,000M | +33.3% YoY; 6.7% of revenue |
| **Costs** | Q2 interest expense | $1,278M | +390% YoY |
| **Tax** | Effective tax rate | 19.1% | Up from 16.9–17.1% |
| **Cash flow** | H1 operating cash flow | $84,859M | +32.8% YoY; 36.9% of revenue |
| **Cash flow** | H1 capex | $80,598M | **+103.3% YoY; 35.1% of revenue** |
| **Cash flow** | H1 free cash flow | **$4,261M** | **–82.4% YoY; ~1.9% margin** |
| **Cash flow** | Q2 free cash flow | **≈ –$5,855M** | First clearly negative quarter in dataset |
| **Cash flow** | Capex incurred, unpaid | $29,113M | +173.8% → Q3 capex > $45B likely |
| **Capital return** | H1 buybacks | **$0** | vs $28,306M in H1 2025 (suspended) |
| **Capital return** | H1 dividends | $5,231M | $0.43/sh declared (+4.9%); annualized ~$0.88 |
| **Balance sheet** | Total assets | $921,983M | **+54.9% in six months** |
| **Balance sheet** | Cash + ST investments | $242,474M | +91.2%; +$115.6B |
| **Balance sheet** | Total debt (carrying) | $101,085M | **+105.9%** |
| **Balance sheet** | Net cash (est.) | **≈ $138,800M** | Still strongly net-cash |
| **Balance sheet** | Convertible preferred | $18,023M | New, issued 2026-06-05 ($19.0B gross) |
| **Balance sheet** | Non-marketable equity securities | $124,259M | +93.9%; cumulative upward marks $85.7B |
| **Balance sheet** | Deferred tax liabilities | $22,819M | From $919M — tax on book gains |
| **Balance sheet** | Loss contingency accrual | $17,356M | Legal/regulatory; +11.3% |
| **Dilution** | Shares outstanding | 12,230M | +142M (+1.17%); common issued for $30.5B |
| **Insider data** | Insider transactions | **UNAVAILABLE** | No authorized archive — not inferred |
| **Data gaps** | Segment revenue, goodwill, PP&E, total equity, M&A line | Not in returned tag set | Verify against 10-Q before acting |

---

**Disclaimer:** Figures are derived from point-in-time SEC XBRL facts disclosed on or before 2026-08-17. Revenue, gross profit, quarterly Q1 splits, and core EPS are computed from disclosed tags (methodology stated in §3); all other line items are as reported. Items flagged as inferences (acquisition spend, current ratio, average issuance price) should be verified against the primary 10-Q. No insider-transaction conclusions are drawn because the data is unavailable.