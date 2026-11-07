# GOOGL (Alphabet Inc.) — Fundamental Deep-Dive
**As of 2026-07-29 | Latest filed financials: Q2 2026 Form 10-Q (period ended 2026-06-30), EDGAR-accepted 2026-07-23 | FY2025 Form 10-K accepted 2026-02-05 (CIK 1652044)**

---

## 0. Data provenance & method notes (read first)

- All figures below are **point-in-time SEC XBRL facts** filtered by actual EDGAR acceptance timestamp (nothing filed after 2026-07-23 is used). Reporting entity = **Alphabet Inc. (GOOGL)**.
- The vendor fact set returned **alphabetically truncated tag lists** (roughly A–D/F range). Consequently certain standard line items (Revenue, R&D, Sales & Marketing, Total Liabilities, Retained Earnings, Goodwill, PP&E net, Long-Term Debt split) were **not** returned. I have **derived Revenue** as `OperatingIncomeLoss + CostsAndExpenses`, a method that reproduces actual reported figures exactly for H1 2025 ($186,662M) — a validated cross-check.
- Where I derive figures, they are labeled **[derived]**.
- **Insider transactions: UNAVAILABLE.** The data package has no authorized point-in-time insider archive for GOOGL. No insider activity is inferred or fabricated below.

---

## 1. Executive summary — the five things that matter

1. **Core business is accelerating hard.** Q2 2026 revenue **[derived]** ≈ **$119.80B** (+24.2% YoY), H1 revenue ≈ **$229.69B** (+23.1% YoY). Operating income $40.77B in Q2 (+30.4% YoY), operating margin **34.0%** vs 32.4% a year ago. Gross margin expanded ~210bp YoY to 61.6%.
2. **GAAP EPS is heavily inflated by non-cash gains.** $9.11 diluted EPS in Q2 2026 vs $2.31 LY. **$99.03B of equity-securities fair-value gains** hit non-operating income in Q2 ($135.95B in H1). Roughly **~71% of Q2 EPS and ~63% of H1 EPS is mark-to-market, not operations** — reversal risk is real.
3. **Free cash flow has collapsed.** CFO $84.86B vs capex **$80.60B** → **H1 FCF of only $4.26B** (vs $24.25B H1 2025, **−82%**). Capex/revenue = **35.1%** vs 21.2% LY. Plus **$29.1B of capex incurred but unpaid** at 6/30/26 (vs $15.1B at FY25-end) — cash capex will run hot in Q3.
4. **Capital allocation flipped from returning cash to raising it.** Buybacks: **$0 in H1 2026** (vs $28.31B in H1 2025). Instead GOOGL raised **~$109.5B gross**: $56.23B debt, $30.50B common stock, **$19.06B convertible preferred (issued 2026-06-05)**, $3.76B minority interests. Share count **rose** 12,088M → 12,230M (+1.2%). Total debt doubled to **$101.09B**; interest expense up ~6x to $1.81B in H1.
5. **Balance sheet still fortress-like.** Cash + short-term investments **$242.47B** vs debt $101.09B → **net cash ≈ $141.4B** (before $20.6B of lease liabilities and $18.0B preferred). Liquidity is not a concern; *return on* that liquidity is.

**Net read:** an excellent operating quarter wrapped in a low-quality earnings headline and a genuinely large negative free-cash-flow inflection. Trading implication: expect the market to focus on **capex/FCF trajectory and the AI monetization narrative**, not the $9.11 EPS print.

---

## 2. Income statement — quarterly reconstruction

**[derived] all revenue/gross profit/opex figures reconstructed from `CostsAndExpenses` + `OperatingIncomeLoss` + `CostOfRevenue` + `GeneralAndAdministrativeExpense`; USD millions**

| Line item | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 | Q2 YoY | H1 2025 | H1 2026 | H1 YoY |
|---|---|---|---|---|---|---|---|---|
| Revenue **[derived]** | 90,234 | 96,428 | 109,896 | **119,796** | **+24.2%** | 186,662 | **229,692** | **+23.1%** |
| Cost of revenue | 36,361 | 39,039 | 41,271 | 45,943 | +17.7% | 75,400 | 87,214 | +15.7% |
| Gross profit **[derived]** | 53,873 | 57,389 | 68,625 | 73,853 | +28.7% | 111,262 | 142,478 | +28.1% |
| **Gross margin** | 59.7% | 59.5% | **62.4%** | 61.6% | +210bp | 59.6% | **62.0%** | +240bp |
| G&A (reported) | 3,539 | 5,209 | 4,291 | 6,461 | +24.0% | 8,748 | 10,752 | +22.9% |
| R&D + S&M + other opex **[derived]** | 19,728 | 20,909 | 24,638 | 26,622 | +27.3% | 40,637 | 51,260 | +26.1% |
| Total costs & expenses | 54,628 | 65,157 | 70,200 | 79,026 | +21.3% | 124,785 | 149,226 | +19.6% |
| **Operating income** | 30,606 | 31,271 | 39,696 | **40,770** | **+30.4%** | 61,877 | **80,466** | **+30.0%** |
| **Operating margin** | 33.9% | 32.4% | **36.1%** | 34.0% | +160bp | 33.1% | **35.0%** | +190bp |
| Non-operating income | 11,183 | 2,662 | 37,716 | **97,983** | n.m. | 13,845 | **135,699** | n.m. |
| — of which equity FV gains | 9,758 | 1,286 | 36,915 | **99,031** | n.m. | 11,044 | **135,946** | n.m. |
| — interest income | 1,001 | 1,050 | 1,381 | 1,430 | +36% | 2,051 | 2,811 | +37% |
| — interest expense | 34 | 261 | 533 | 1,278 | +390% | 295 | 1,811 | +514% |
| Pre-tax income | 41,789 | 33,933 | 77,412 | **138,753** | +309% | 75,722 | **216,165** | +185% |
| Tax expense | 7,249 | 5,737 | 14,834 | 26,560 | +363% | 12,986 | 41,394 | +219% |
| Effective tax rate | 17.3% | 16.9% | 19.2% | **19.1%** | +220bp | 17.1% | **19.1%** | +200bp |
| Net income | 34,540 | 28,196 | 62,578 | **112,193** | +298% | 62,736 | **174,771** | +179% |
| **Diluted EPS** | $2.81 | $2.31 | $5.13 | **$9.11** | +294% | $5.12 | **$14.24** | +178% |
| Diluted shares (M) **[derived]** | 12,200 | 12,206 | 12,300 | 12,306 | +0.8% | 12,254 | 12,272 | +0.1% |

**Observations that matter for a trader:**
- **Sequential deceleration in margin, not in growth.** Q2 revenue rose +9.0% QoQ, but cost of revenue rose **+11.3% QoQ** and gross margin slipped 80bp vs Q1 (62.4% → 61.6%). Operating margin fell 210bp QoQ (36.1% → 34.0%). This is the first visible fingerprint of the **depreciation/hosting ramp** from the AI capex surge — Q1 2026 was likely the peak margin print for this cycle.
- **Operating leverage still clearly positive YoY** (op income +30% on revenue +24%), so the cost story is "spending more, still earning more" — not deterioration.
- **Tax rate step-up** from ~17% to 19.1% is a ~$4-5B/yr headwind at current pre-tax levels; part of this is tax on the equity gains and the new $22.8B deferred tax liability.

---

## 3. Earnings quality — the single most important adjustment

| Metric | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 |
|---|---|---|---|---|
| Diluted EPS (GAAP) | $2.31 | $9.11 | $5.12 | $14.24 |
| Approx. after-tax EPS from equity FV gains **[derived: gain × (1−ETR) ÷ diluted shares]** | ~$0.09 | **~$6.51** | ~$0.75 | **~$8.94** |
| **"Operating-only" EPS proxy [derived: op income × (1−ETR) ÷ shares]** | **~$2.13** | **~$2.68** | ~$4.27 | **~$5.30** |
| Operating-EPS proxy growth YoY | — | **+26%** | — | **+24%** |
| Share of GAAP EPS from non-operating gains | 4% | **71%** | 15% | **63%** |

**Actionable interpretation:** the correct "core" run-rate is **~$2.65–2.70/quarter** of operating EPS, growing mid-20s% — that is a very good number and supports the *operating* thesis. The $9.11 headline is **not** a valuation anchor. Any sell-side "annualizing $36 of EPS" math is wrong. Conversely, if private-market AI/space valuations compress, this $136B of gains reverses through the P&L and produces ugly comparatives — the offsetting cushion is the **$22.8B deferred tax liability** already booked against those marks.

---

## 4. Balance sheet — scale-up, leverage-up, still net-cash-rich

**All values USD millions, reported tags**

| Item | 2025-12-31 | 2026-06-30 | Δ | Δ% |
|---|---|---|---|---|
| **Total assets** | 595,281 | **921,983** | +326,702 | **+54.9%** |
| Current assets | 206,038 | 343,524 | +137,486 | +66.7% |
| Cash & equivalents | 30,708 | 55,911 | +25,203 | +82.1% |
| **Cash + short-term investments** | 126,843 | **242,474** | +115,631 | **+91.2%** |
| Available-for-sale debt securities | n/a | 99,500 | — | — |
| Accounts receivable, net | 62,886 | 69,175 | +6,289 | +10.0% |
| Allowance for doubtful accounts | 924 | 995 | +71 | 1.4% of AR |
| **Non-marketable equity securities** | 64,094 | **124,259** | +60,165 | **+93.9%** |
| — cumulative upward revaluations | 44,485 | 85,732 | +41,247 | +92.7% |
| — cumulative downward adjustments | (8,820) | (9,115) | −295 | — |
| Finite-lived intangibles, gross | 2,467 | **10,585** | +8,118 | **+329%** |
| **Total debt (carrying amount)** | 49,085 | **101,085** | +52,000 | **+105.9%** |
| Convertible preferred stock | 0 | **18,023** | +18,023 | new |
| Common stock + APIC | 93,126 | 131,371 | +38,245 | +41.1% |
| AOCI | (1,916) | (2,285) | −369 | — |
| **Deferred tax liabilities, net** | 919 | **22,819** | +21,900 | **+2,383%** |
| Deferred tax assets, net | 9,113 | 1,448 | −7,665 | −84.1% |
| Accounts payable | 12,200 | 20,258 | +8,058 | +66.0% |
| Accrued liabilities | 55,557 | 73,014 | +17,457 | +31.4% |
| Employee-related liabilities | 17,546 | 15,086 | −2,460 | −14.0% |
| Accrued income taxes, current | 523 | 5,233 | +4,710 | +901% |
| Loss contingency accrual (current) | 15,594 | **17,356** | +1,762 | +11.3% |
| Operating lease liability | 15,954 | 18,037 | +2,083 | +13.1% |
| Finance lease liability | 2,500 | 2,590 | +90 | +3.6% |
| Contract liabilities (deferred revenue) | 8,600 | 10,100 | +1,500 | +17.4% |
| Shares outstanding (M) | 12,088 | **12,230** | +142 | +1.2% |

**Key reads:**
- **Liquidity is not the issue; allocation is.** Net cash ≈ **$141.4B** ($242.5B liquid vs $101.1B debt). Add $18.0B preferred and $20.6B of leases and it is still ~$103B net cash. This is why the debt raise is not a credit event — it's arbitrage on a balance sheet that was arguably *under*-levered.
- **The $22.8B deferred tax liability** is the tell that the equity gains are unrealized: $27.5B of deferred tax expense ran through the cash-flow tax line in H1 (vs a $1.6B *benefit* LY). Cash taxes are rising too (accrued income taxes current $523M → $5,233M).
- **Working capital flattered CFO**: AP +$8.06B, accrued liabilities +$17.46B, accrued taxes +$4.71B vs AR only +$6.29B. The $29.1B of unpaid capex sitting in payables/accruals is a **reversal risk to Q3 CFO** even as the cash capex outflow accelerates.
- **Intangibles gross tripling (+$8.1B)** plus **$22.05B of "other investments" purchased** (vs $2.31B LY) indicates a materially more aggressive M&A / strategic-stake year. Confirm in the 10-Q notes what was acquired — this is the most under-appreciated item in the release.
- **Loss contingency accrual of $17.4B** (up $1.76B) remains a live regulatory/legal overhang; the FY25 10-K disclosed $3.0B of payments in Q3 2025.
- Debt maturity ladder at FY25-end (pre-raise): $2.0B due within 12 months, minimal through 2029, **$36.1B beyond year five** — the new issuance should be assumed to be long-dated, so refinancing risk ≈ nil.

---

## 5. Cash flow — the crux of the debate

**USD millions, six months ended June 30**

| Item | H1 2025 | H1 2026 | Δ% |
|---|---|---|---|
| **Cash from operations** | 63,897 | **84,859** | **+32.8%** |
| Payments for PP&E (capex) | 39,643 | **80,598** | **+103.3%** |
| **Free cash flow [derived]** | **24,254** | **4,261** | **−82.4%** |
| Capex / revenue **[derived]** | 21.2% | **35.1%** | +1,390bp |
| FCF / revenue **[derived]** | 13.0% | **1.9%** | −1,110bp |
| Capex incurred but unpaid (period-end) | 10,635 | **29,113** | +173.7% |
| Depreciation (reported) | 9,485 | 13,586 | +43.2% |
| Amortization of intangibles | 246 | 545 | +121.5% |
| Share-based compensation | 11,500 | **15,200** | **+32.2%** |
| Purchases of marketable securities | (39,870) | (76,480) | +91.8% |
| Purchases of other investments | (2,312) | **(22,051)** | +854% |
| **Net investing cash flow** | (40,738) | **(145,822)** | +258% |
| Debt issued, net of costs | 31,378 | **56,226** | +79.2% |
| Debt repayments + finance-lease principal | (18,397) | (5,253) | −71.4% |
| **Common stock issued** | **0** | **30,499** | new |
| **Convertible preferred issued** | **0** | **19,063** | new |
| Minority interests raised | 400 | 3,758 | +840% |
| **Share repurchases** | **(28,306)** | **0** | **−100%** |
| Dividends paid | (4,977) | (5,231) | +5.1% |
| **Net financing cash flow** | (26,033) | **+86,320** | sign flip |
| FX effect | 444 | (154) | — |
| **Net change in cash** | (2,430) | **+25,203** | sign flip |

**Reads:**
- **CFO quality is decent but flattered** (+32.8%, vs revenue +23.1%; the gap is SBC +$3.7B and working-capital build, both non-durable).
- **Depreciation of $13.6B against $80.6B of H1 capex** implies the D&A line will multiply over the next 4–8 quarters. Every dollar of that hits gross profit. This is the mechanism behind the QoQ margin slippage already visible.
- **SBC +32% to $15.2B** — GAAP opex is being propped up in growth terms by stock comp growing faster than revenue. Ex-SBC operating margin would look even better, but dilution/optics are a real cost.
- **Gross external capital raised ≈ $109.5B in six months** ($56.2B debt + $30.5B common + $19.1B convertible preferred + $3.8B minorities). Reported net financing inflow was $86.3B; the ~$12B gap is dividends, debt repayments, finance-lease principal and (likely) RSU tax-withholding not itemized in the returned tags. Either way: **Alphabet became a net issuer of capital for the first time in its modern history.**
- **The $4.3B FCF number is the bear's exhibit A.** A company earning $175B of net income in six months generating $4B of free cash is not "cheap" on FCF multiples — it is a capex story. Bulls must argue the $80.6B is pre-revenue infrastructure with a 2027–28 payoff.

---

## 6. Capital structure changes — what the June 2026 raises imply

| Instrument | Amount | Read |
|---|---|---|
| Senior debt | $56.2B gross issued, $5.3B repaid → total debt **$101.1B** | Interest expense annualizing near **$7–8B** at current run-rate ($1.28B in Q2 alone). Cheap, long-dated, non-dilutive. Sensible. |
| **Common stock issuance** | **$30.5B** (0 in H1 2025) | Highly unusual for Alphabet. Dilutive (share count +1.2%), and it *replaces* the buyback that was running $56B/yr. Signal: management sees the equity as a funding currency and places a high cost on it. |
| **Convertible preferred** | **$19.06B issued 2026-06-05**, carrying value $18.02B | Preferred dividends of **$86M** recognized in Q2 (only since June 5) — prorated, this is a mid-single-digit annualized yield, i.e., an expensive-ish hybrid. Conversion features imply future dilution if the stock rallies. Also **changes the capital-structure ranking for common holders for the first time.** |
| Minority interests | $3.8B raised | Consistent with project/JV-level co-investment in infrastructure — a way to fund capex off-balance-sheet-ish while retaining control. |
| Buyback | **$0** | The single clearest management signal in the filing: cash is being redirected to capex/M&A, not to shareholders. |
| Dividend | $0.22/qtr (from $0.21); $5.23B paid H1 | Token; yield is immaterial. Growth rate (+4.8% per share) is well below earnings growth. |

**Trading implication:** the equity/preferred issuance is a **structural change** — it caps the multiple-expansion case that buybacks historically supported. Watch whether the buyback resumes in Q3 (a resume = management signaling the capex peak is near; a continued zero = free-cash-flow discipline is genuinely gone for the cycle).

---

## 7. Investment portfolio & mark-to-market exposure

- **Non-marketable equity (private) portfolio: $124.3B book value**, up from $64.1B, with **$85.7B of cumulative upward revaluations** and only $9.1B of cumulative write-downs. Supported by **$41.2B of upward marks added in H1 2026** and **$22.1B of new cash invested**.
- **AFS debt portfolio: $99.5B** — maturities $16.7B (<1y), $50.9B (1–5y), $15.3B (5–10y), $16.6B (>10y). Total unrealized loss position $416M on $53.2B of securities in a loss position (**~0.8%** — trivially small, but the $49.4B in the "<12 months" bucket means rate/credit duration risk is concentrated in recently purchased paper).
- **Derivatives:** assets $1.70B, liabilities $1.96B (up from $0.73B/$0.38B) — likely FX hedges on the larger non-USD funding. Watch that net liability of $0.26B vs $0.35B net asset a year ago.
- **The key risk:** a private-AI valuation reset (any of the large model labs, space, or robotics names Alphabet holds) would flow straight through the P&L at ~$100B+ scale. That is a **swing factor larger than annual operating income**. The $22.8B deferred tax asset/liability reclassification partly nets this.

---

## 8. Insider transactions

**DATA UNAVAILABLE.** No authorized, point-in-time insider-transaction archive exists for GOOGL in this data package. Per data-integrity instructions, I am not inferring, estimating, or characterizing insider buying/selling. Treat insider signal as **neutral/unobserved** for this report.

---

## 9. Risk register

| Risk | Evidence in the filings | Severity |
|---|---|---|
| **FCF compression / capex overrun** | FCF $4.26B vs $24.25B (−82%); capex/revenue 35.1%; $29.1B unpaid capex | **High** |
| **Non-repeatable earnings** | $135.9B H1 equity FV gains = 63% of EPS; $99.0B in Q2 alone | **High** |
| **Depreciation ramp into margins** | D&A $13.6B vs capex $80.6B; Q2 GM −80bp QoQ, op margin −210bp QoQ | **High** |
| **Dilution / capital-structure change** | $30.5B common issued, $19.1B convertible preferred, shares +1.2%, buybacks $0, preferred dividends now $86M/qtr | Medium-High |
| **Deferred tax / cash tax step-up** | DTL net $0.9B → $22.8B; deferred tax expense $27.5B; ETR 17.1% → 19.1% | Medium |
| **Leverage ramp** | Debt $49.1B → $101.1B; interest expense +514%; net interest income *fell* to $1.0B from $1.76B despite more cash | Medium |
| **Legal/regulatory** | Loss contingency accrual $17.36B current | Medium |
| **Private-asset mark volatility** | $124.3B non-marketable equity; $85.7B cumulative upward marks | Medium |
| **Working-capital reversal** | AP +$8.1B, accrued liab +$17.5B, taxes +$4.7B vs AR +$6.3B | Medium |
| **Concentration/opacity** | Revenue is aggregated; segment detail not in returned data | Low-Medium |

**Genuine mitigants:** $242.5B liquid assets; net cash ~$141B; AFS unrealized losses only $416M; operating income +30% YoY with expanding gross margins; contract liabilities +17.4% (deferred revenue/backlog building); long-dated debt ladder with $36.1B due beyond five years.

---

## 10. Actionable insights for a trader over the next 1–3 months

1. **Do not trade the $9.11 headline EPS.** If the stock gaps on the print, the *durable* number is ~$2.68/qtr operating EPS growing mid-20s% — that argues for a mid-20s forward operating-earnings growth multiple, not a 9-handle. Anchor any valuation work on operating income ($40.8B/qtr, annualizing ~$163B) and on FCF *after* capex normalizes.
2. **Make capex the primary monitorable.** Q3/Q4 guide risk is asymmetric: with $29.1B of already-incurred-but-unpaid capex, **Q3 cash capex likely steps up sequentially**. A FY2026 capex frame of roughly **$170–190B** is consistent with H1 actual + unpaid backlog + typical seasonality (analyst estimate, not a filed figure). If management guides capex above that, expect FCF-based de-rating; if it guides capex flat-to-down, expect an immediate re-rating.
3. **Watch the buyback line as a sentiment switch.** Zero repurchases while raising $30.5B of common equity is the most shareholder-unfriendly combination in the filing. **A resumption of repurchases in Q3 is a strong positive catalyst** (signals capex peak / cash-return normalization); **a second quarter at zero combined with more equity issuance is a structural negative** for multiple support.
4. **Position for margin deceleration, not revenue deceleration.** Revenue is accelerating (+24% YoY). The risk is the mechanical drag of $13.6B D&A against $80.6B capex. If Q3 operating margin prints below ~33%, the "AI spend is deleveraging" bear case takes hold. Conversely op margin ≥35% with revenue ≥+23% would be a powerful bull confirmation.
5. **Treat the equity-gain line as a volatility source, both ways.** $136B of H1 gains created a $22.8B DTL and $41.2B of new upward marks. Any private-market funding-round reset produces a headline loss quarter — an opportunity to buy the *operating* business into a GAAP optics selloff, and equally a reason not to pay up on "earnings momentum."
6. **Dividend/payout math is irrelevant to the thesis** ($5.23B H1, $0.88/yr annualized) — ignore it as a valuation input; it exists only as a signaling device now.
7. **Insider signal: unavailable.** Do not let any third party attribute insider buying/selling to this period based on this dataset.

**Base case:** operating momentum intact (H1 revenue +23%, op income +30%), balance sheet capacity abundant, but FCF near zero and shareholder returns paused → a **"good business, expensive on cash flow, headline-EPS noise"** regime. Preferred expression: long operating-momentum / short the assumption that GAAP EPS is the run-rate; monitor capex guidance and buyback resumption as the two tradeable catalysts.

---

## 11. Key points summary

| Category | Metric / Fact | Value | Interpretation |
|---|---|---|---|
| Reporting | Latest 10-Q | Q2 2026, period ended 2026-06-30, filed 2026-07-23 | Fresh (6 days old) — high signal |
| Growth | Q2 2026 revenue **[derived]** | **$119.80B, +24.2% YoY** (H1 $229.69B, +23.1%) | Acceleration; core thesis intact |
| Profitability | Q2 operating income / margin | $40.77B, **34.0%** (H1 35.0%) | +160bp YoY, but **−210bp QoQ** |
| Profitability | Q2 gross margin | 61.6% (Q1 62.4%) | +210bp YoY, −80bp QoQ (capex/depreciation) |
| Earnings quality | H1 equity FV gains | **$135.95B** (Q2 $99.03B) | ~63% of H1 EPS — non-recurring |
| Earnings quality | GAAP vs operating EPS | $9.11 vs **~$2.68/qtr** (Q2) | Operating EPS +26% YoY — the real number |
| Cash generation | H1 CFO | $84.86B, +32.8% | Solid, WC-flattered |
| Cash generation | H1 capex / FCF | **$80.60B / $4.26B** | **FCF −82% YoY**; capex 35.1% of revenue |
| Cash generation | Unpaid capex at 6/30/26 | **$29.11B** (vs $15.09B FY25) | Q3 cash capex step-up likely |
| Liquidity | Cash + ST investments | $242.47B (+91% in 6 months) | Fortress |
| Leverage | Total debt / interest expense | **$101.09B (+106%)** / $1.81B (+514%) | Deliberate releveraging, still net-cash |
| Capital structure | Raised in H1 2026 | $56.2B debt + $30.5B common + $19.1B conv. pref. + $3.8B minorities ≈ **$109.5B** | Historic shift to capital-raising |
| Shareholder returns | Buybacks / dividends H1 2026 | **$0** / $5.23B | Buyback halt; shares +1.2% to 12,230M |
| Taxes | ETR / net DTL | 19.1% (from 17.1%) / **$22.82B** (from $0.92B) | Tax on unrealized gains; future drag |
| Investments | Non-marketable equity book | **$124.26B** (+94%); $85.73B cumulative upward marks | Huge mark-to-market swing factor |
| Investments | AFS securities / unrealized losses | $99.50B / $416M (0.4%) | Benign credit/rate exposure |
| Contingencies | Loss accrual (current) | $17.36B (+$1.76B in H1) | Live regulatory/legal overhang |
| Balance sheet | Finite-lived intangibles, gross | $2.47B → **$10.59B** (+329%) | M&A/asset step-up — verify in notes |
| Balance sheet | Contract liabilities | $10.10B (+17.4%) | Deferred revenue/backlog building |
| Cost structure | SBC / depreciation H1 | $15.20B (+32%) / $13.59B (+43%) | Both compounding faster than revenue |
| Insider activity | — | **DATA UNAVAILABLE** | Neutral/unobserved; do not infer |
| Verdict | — | **Constructive on operations; bearish on GAAP EPS quality and near-term FCF** | Trade capex guidance & buyback resumption |