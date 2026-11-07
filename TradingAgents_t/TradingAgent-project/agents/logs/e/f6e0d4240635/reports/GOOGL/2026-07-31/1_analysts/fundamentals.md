# GOOGL — Alphabet Inc.: Fundamental Deep-Dive
### Point-in-time analysis as of 2026-07-31 (latest filed data: 10‑Q for Q2 FY2026, filed 2026‑07‑23)

---

## 1. Data provenance, scope and caveats (read first)

| Item | Detail |
|---|---|
| Primary source | SEC filings cache, filtered by EDGAR acceptance timestamp ≤ 2026‑07‑31 |
| Latest periodic filing | Q2 FY2026 Form 10‑Q, accession 0001652044‑26‑000071, accepted 2026‑07‑23 01:15 UTC |
| Prior filing in window | Q1 FY2026 Form 10‑Q, accession 0001652044‑26‑000048, accepted 2026‑04‑30 |
| Annual anchor | FY2025 Form 10‑K, accession 0001652044‑26‑000018, accepted 2026‑02‑05 |
| Insider transactions | **DATA_UNAVAILABLE** — the vendor package contains no authorized point-in-time insider-transaction archive for GOOGL. No inference or fabrication is made below. |
| Price / market data | Not provided by these tools. **All ratios below are flow- and book-based; no P/E, P/S, EV/EBITDA or P/B multiples are asserted** because no price was available. |
| Derived lines | The vendor did not surface a discrete `Revenues` tag. Revenue is therefore **derived arithmetically** as `CostsAndExpenses + OperatingIncomeLoss`, and the R&D + Sales & Marketing combined line as `CostsAndExpenses − CostOfRevenue − GeneralAndAdministrativeExpense`. These reconciliations are shown explicitly. |

---

## 2. Company profile (as identified)

Alphabet Inc. (NASDAQ: GOOGL / GOOG) is the parent of Google — the world's largest internet advertising business — plus Google Cloud, YouTube, Google Search/Android/Chrome/Play, and the "Other Bets" portfolio. The company also runs one of the largest corporate venture/investment books in the world: **$124.3B of equity securities without readily determinable fair value** at 2026‑06‑30, which in H1 FY2026 produced a **$135.9B pre-tax mark-to-market gain**. In H1 FY2026 the company also (a) doubled capex, (b) halted buybacks entirely, and (c) raised ~$109B of gross debt + equity + preferred capital — a decisive pivot toward AI-infrastructure funding. *(Segment-level revenue splits were not returned by the tools; the analysis below is consolidated.)*

---

## 3. Income statement — Q2 and H1 FY2026

### 3.1 Derived revenue and growth

| $M | Q2 FY2026 | Q2 FY2025 | YoY | H1 FY2026 | H1 FY2025 | YoY |
|---|---|---|---|---|---|---|
| Costs and expenses | 79,026 | 65,157 | +21.3% | 149,226 | 124,785 | +19.6% |
| Operating income | 40,770 | 31,271 | +30.4% | 80,466 | 61,877 | +30.0% |
| **Revenue (derived)** | **119,796** | **96,428** | **+24.2%** | **229,692** | **186,662** | **+23.1%** |
| *Q1 implied revenue* | *109,896* | *90,234* | *+21.8%* | — | — | — |

**Key insight: revenue growth is *accelerating*** — Q1 +21.8% → Q2 +24.2% YoY, and +9.0% sequentially. This is the single most important fundamental datapoint in the package: a company at this scale inflecting upward, not decelerating.

### 3.2 Margin structure

| $M | Q2 FY2026 | Q2 FY2025 | Δ | H1 FY2026 | H1 FY2025 | Δ |
|---|---|---|---|---|---|---|
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| Gross profit | 73,853 | 57,389 | +28.7% | 142,478 | 111,262 | +28.1% |
| *Gross margin* | *61.7%* | *59.5%* | *+216 bp* | *62.0%* | *59.6%* | *+240 bp* |
| R&D + Sales & Mktg (derived) | 26,622 | 20,909 | +27.3% | 51,260 | 40,637 | +26.1% |
| G&A | 6,461 | 5,209 | +24.0% | 10,752 | 8,748 | +22.9% |
| Total costs | 79,026 | 65,157 | +21.3% | 149,226 | 124,785 | +19.6% |
| **Operating margin** | **34.0%** | **32.4%** | **+160 bp** | **35.0%** | **33.2%** | **+188 bp** |

**Insight:** Gross margin expanded ~220–240 bp despite AI-serving costs, because cost of revenue (+15.7%) grew far slower than revenue (+23.1%). Operating leverage is genuine. **But note the sequential decay:** Q1 FY2026 operating margin was **36.1%**, Q2 slipped to **34.0%** — a 210 bp compression quarter-on-quarter as opex (R&D + S&M +27% YoY) and D&A ramped. Trend matters for H2 estimates: expect a 33–35% consolidated operating margin band unless capex depreciation steps up faster.

### 3.3 Below the operating line — the $135.9B elephant

| $M | Q2 FY2026 | Q2 FY2025 | H1 FY2026 | H1 FY2025 |
|---|---|---|---|---|
| Operating income | 40,770 | 31,271 | 80,466 | 61,877 |
| Nonoperating income (expense) | **97,983** | 2,662 | **135,699** | 13,845 |
| — of which equity securities FV-NI gain/(loss) | **99,031** | 1,286 | **135,946** | 11,411 |
| — of which realized gains | 278 | 217 | 836 | 435 |
| — of which unrealized gains (readily-determinable) | 21,399 | 853 | 21,531 | 1,088 |
| — of which *non-marketable revaluation (residual)* | **≈77,354** | ≈216 | **≈113,579** | ≈9,888 |
| — interest income | 1,430 | 1,050 | 2,811 | 2,051 |
| — interest expense | (1,278) | (261) | (1,811) | (295) |
| Pre-tax income | 138,753 | 33,933 | 216,165 | 75,722 |
| Tax expense (effective rate) | 26,560 (19.1%) | 5,737 (16.9%) | 41,394 (19.1%) | 12,986 (17.1%) |
| Net income | 112,193 | 28,196 | 174,771 | 62,736 |
| **Diluted EPS** | **$9.11** | **$2.31** | **$14.24** | **$5.12** |
| Diluted shares (implied) | ~12,306M | ~12,206M | ~12,264M | ~12,253M |

**This is the crux of the report. ~78% of H1 FY2026 net income ($135.9B of $174.8B) is non-cash, mark-to-market revaluation of the investment portfolio.** Corroborating balance-sheet evidence:

- Equity securities without readily determinable fair value: **$64,094M → $124,259M** (+$60.2B in six months)
- Cumulative *upward* price adjustments on those securities: **$44,485M → $85,732M** (+$41.2B)
- Cumulative downward adjustments: $8,820M → $9,115M
- Deferred income tax liabilities (net): **$919M → $22,819M** (+$21.9B) and the cash-flow statement shows a **$27,538M deferred-tax add-back**, i.e. the gain is taxed on paper only, as a deferred liability. **No cash was received.**

### 3.4 Normalizing earnings — "core" run-rate (analyst estimate)

Stripping all equity-securities FV-NI gains and applying the reported effective tax rate:

| Estimate | Q2 FY2026 | Q2 FY2025 | YoY | H1 FY2026 | H1 FY2025 | YoY |
|---|---|---|---|---|---|---|
| Core pre-tax income (op income + nonop excl. equity gains) | 39,722 | 32,647 | +21.7% | 80,219 | 64,311 | +24.7% |
| Core tax rate assumed | 19.1% | 16.9% | | 19.1% | 17.1% | |
| **Core net income** | **~32,135** | **~27,129** | **+18.5%** | **~64,897** | **~53,314** | **+21.7%** |
| Diluted shares | ~12,306M | ~12,206M | | ~12,264M | ~12,253M | |
| **Core diluted EPS** | **~$2.61** | **~$2.22** | **+17.6%** | **~$5.29** | **~$4.35** | **+21.6%** |

**Actionable framing:** headline H1 EPS of **$14.24** vs core **≈$5.29** — headline overstates sustainable earnings by roughly **2.7x**. Any screen, consensus comparison, or "beat" narrative anchored on reported EPS is contaminated. Traders should track and trade the **+22% core EPS / +24% revenue / 34–35% operating-margin** engine, and treat the mark-to-market as a separate, volatile "investment book" mark (it can reverse violently — the company's own cumulative *downward* adjustments of $9.1B show the book is two-way).

Also worth noting: the interest-expense line exploded **+514% YoY (H1: $295M → $1,811M)**, a direct consequence of the debt ramp described below. Net interest income is still positive ($1.0B in H1) but the gap is closing fast.

---

## 4. Balance sheet — transformed in six months

| $M | 2026-06-30 | 2025-12-31 | Change |
|---|---|---|---|
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| **Cash + short-term investments** | **242,474** | **126,843** | **+91.2%** |
| Accounts receivable (net) | 69,175 | 62,886 | +10.0% |
| Current assets | 343,524 | 206,038 | +66.7% |
| AFS debt securities (noncurrent) | 99,500 | n/d | — |
| Equity securities w/o readily determinable FV | 124,259 | 64,094 | +93.9% |
| PP&E incl. finance-lease ROU (gross) | n/d | n/d | capex-driven |
| **Total assets** | **921,983** | **595,281** | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| Employee-related liabilities | 15,086 | 17,546 | −14.0% |
| Income taxes payable (current) | 5,233 | 523 | +900% |
| Income taxes payable (noncurrent) | 11,306 | 9,531 | +18.6% |
| Contract liabilities (current) | 7,154 | 6,578 | +8.8% |
| **Total debt (carrying)** | **101,085** | **49,085** | **+105.9%** |
| Operating lease liabilities | 18,037 | 15,954 | +13.1% |
| Finance lease liabilities | 2,590 | 2,500 | +3.6% |
| Deferred income tax liabilities (net) | 22,819 | 919 | +2,383% |
| Convertible preferred stock | 18,023 | 0 | new |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| AOCI | (2,285) | (1,916) | wider |
| Shares outstanding | 12,230M | 12,088M | **+1.18%** |
| Legal/loss contingency accrual (current) | 17,356 | 15,594 | +11.3% |

**Liquidity & leverage:** Net cash position = cash + ST investments $242,474M − total debt $101,085M = **+$141.4B net cash**; still **+$120.8B net cash** even after including $20.6B of lease liabilities. Gross debt more than doubled but remains trivially covered: annualized operating income (~$160.9B) is ~1.6x *total* debt. Current ratio is roughly 3x (approximate, since the vendor did not return a single `LiabilitiesCurrent` total; AP + accrued + employee + current taxes + contract liabilities + current lease portions ≈ $95–110B vs current assets $343.5B). **No balance-sheet stress whatsoever.**

**Two items that matter more than the leverage:**
1. **Deferred tax liability +$21.9B** — the paper gains have created a real future tax claim. This is unrecorded-in-EPS economic cost.
2. **Legal contingency accrual $17.4B, up $1.8B in six months** (and $3.0B of contingency payments were made in Q3 FY2025 per the 10‑K). Regulatory/antitrust overhang is being *added to*, not released.

Also: **finite-lived intangibles (gross) jumped $2,467M → $10,585M** — the company spent roughly **$8.1B** on acquired intangibles in H1, i.e. meaningful M&A activity resumed. Forward amortization: $1,304M next 12 months, $1,142M / $1,096M / $1,055M in the following years.

---

## 5. Cash flow — the real story: capex doubled, FCF collapsed

| $M | Q2 FY2026 | Q2 FY2025 | H1 FY2026 | H1 FY2025 | YoY |
|---|---|---|---|---|---|
| Operating cash flow | 39,069 | 27,747 | **84,859** | 63,897 | **+32.8%** |
| Capex (PP&E purchases) | (44,924) | (22,446) | **(80,598)** | (39,643) | **+103.3%** |
| **Free cash flow** | **(5,855)** | **+5,301** | **4,261** | **24,254** | **−82.4%** |
| OCF margin | 32.6% | 28.8% | 36.9% | 34.2% | +270 bp |
| Capex / revenue | **37.5%** | 23.3% | **35.1%** | 21.2% | +1,390 bp |
| Depreciation | n/d | n/d | 13,586 | 9,485 | +43.2% |
| Amortization of intangibles | 367 | 124 | 545 | 246 | +121.5% |
| Stock-based comp | 8,000 | 6,000 | 15,200 | 11,500 | +32.2% |
| Investing cash flow | n/d | n/d | (145,822) | (40,738) | nm |
| Financing cash flow | n/d | n/d | **+86,320** | (26,033) | nm |
| Dividends paid | n/d | n/d | 5,231 | 4,977 | +5.1% |
| Buybacks | — | — | **0** | 28,306 | **−100%** |
| Debt issued (net) | — | — | 56,226 | 31,378 | +79.2% |
| Debt repaid | — | — | 5,253 | 18,397 | −71.5% |

**Three findings, in order of importance:**

1. **Q2 FY2026 free cash flow was NEGATIVE (−$5.9B)** — the first time in this dataset. H1 FCF of $4.3B is down 82% YoY while revenue rose 23%. Operating cash flow growth of +32.8% is excellent and cash conversion is healthy (OCF / core net income = **131%**), but it is now fully consumed — and then some — by AI infrastructure buildout.
2. **Capex run-rate is ~$90B/quarter-adjacent**: H1 $80.6B, with Q2 alone at $44.9B. Additionally, **capex incurred but not yet paid was $29,113M at 6/30/26** (vs $10,635M a year earlier) — a 2.7x jump in accrual-based commitments, meaning Q3 cash capex will *not* fall below the Q2 level even if new orders slow. FY2026 capex of ~$170–180B is a reasonable extrapolation of current trajectory vs ~$91B implied for FY2025 (FY2025 capex-incurred-not-paid $15,090M vs FY2024 $10,326M vs FY2023 $7,435M confirms the multi-year escalation).
3. **Depreciation +43% YoY** is the leading indicator that the buildout is starting to *cost* P&L. Expect D&A to keep climbing at 40%+ for several quarters; this is the mechanism by which today's capex becomes tomorrow's margin compression.

---

## 6. Capital allocation — a regime change traders must price

The H1 FY2026 financing statement documents a wholesale shift:

| Capital action | H1 FY2026 | H1 FY2025 | Interpretation |
|---|---|---|---|
| Common stock buybacks | **$0** | $28,306M | **Buyback program halted** |
| Common stock issuance (proceeds) | **$30,499M** | $0 | Equity issuance — dilution |
| Convertible preferred issuance | **$19,063M** (closed 2026‑06‑05) | $0 | New $19B convertible preferred (carrying $18,023M); preferred dividends $86M |
| Minority-shareholder proceeds (subsidiary/JV stakes) | $3,758M | $400M | Non-wholly-owned AI/infra vehicles |
| Net debt issuance | $56,226M | $31,378M | Leverage doubling |
| Dividends | $5,231M ($0.43/sh H1; $0.22 in Q2) | $4,977M ($0.41/sh) | +4.9% DPS — modest, maintained |

**Net effect: shares outstanding rose from 12,088M to 12,230M (+1.18%), and diluted share count is drifting up (basic→diluted spread 1.3% on reported EPS).** The company that returned ~$28B/quarter in buybacks a year ago is now *issuing* equity, preferred, and debt simultaneously.

**Why this matters for a trader:** buybacks have historically been a mechanical bid under GOOGL shares. That bid is **zero** right now, at the exact moment the company is issuing paper into the market. This is a real technical/fundamental headwind that is *not* visible in the reported earnings beat. Mitigants: the raise was massively oversubscribed-looking in scale (~$109B gross of new capital in six months with only +1.2% share count growth), the balance sheet has net cash of $141B, and the proceeds are being deployed into depreciating-but-revenue-generating assets rather than acquisitions at silly multiples. Whether that is accretive depends on AI cloud returns — the key swing factor for 2027 EPS.

---

## 7. Insider transactions

**Unavailable.** The data package contains no authorized point-in-time insider-transaction archive for GOOGL as of 2026‑07‑31. This report makes **no** claim about insider buying or selling, directionality, or magnitude. Traders should source Form 4 data independently rather than assume anything from this report.

---

## 8. Derived operating/quality scorecard

| Metric | H1 FY2026 | H1 FY2025 | Read |
|---|---|---|---|
| Revenue growth | +23.1% | — | Accelerating (Q1 +21.8% → Q2 +24.2%) |
| Gross margin | 62.0% | 59.6% | +240 bp ✓ |
| Operating margin | 35.0% | 33.2% | +188 bp ✓ (but 36.1% in Q1 → 34.0% in Q2) |
| OCF margin | 36.9% | 34.2% | +270 bp ✓ |
| FCF margin | 1.9% | 13.0% | ✗ Severe capex drag |
| OCF / core net income | ~131% | ~120% | ✓ High-quality cash earnings |
| OCF / reported net income | ~49% | ~102% | ✗ MTM distortion |
| Reported diluted EPS | $14.24 | $5.12 | +178% (contaminated) |
| **Core diluted EPS (est.)** | **~$5.29** | **~$4.35** | **+21.6%** (the number that matters) |
| SBC / revenue | 6.6% | 6.2% | Rising — dilution pressure |
| D&A / revenue | 6.2% | 5.2% | Rising — future margin headwind |
| Net cash (cash+ST inv. − debt) | +$141.4B | — | ✓ Fortress |
| Shares outstanding | 12,230M | 12,088M | ✗ +1.18% dilution |
| Tax rate | 19.1% | 17.1% | +200 bp headwind |

---

## 9. Actionable insights & trade framework

**Bull case (fundamental, evidence-based):**
- Revenue growth **accelerating to +24.2% YoY** at a ~$460B annualized run-rate; Q2 +9.0% sequentially.
- Gross margin **+216 bp YoY** and operating margin **+160 bp YoY** despite an unprecedented AI cost build — operating leverage is real.
- Operating cash flow **+32.8% YoY** and OCF/cash-earnings conversion of 131% — the core franchise is generating more cash than ever.
- **Net cash of $141B** after the entire capex and debt program; leverage is a deliberate, cheap, fully covered choice, not distress.
- The investment book is now carried at **$124.3B** with $85.7B cumulative upward marks — a hidden asset whose value is not in the operating multiple.

**Bear case / key risks:**
- **Earnings quality is the headline risk.** ~78% of H1 net income is non-cash revaluation. Reported EPS $14.24 vs core ~$5.29. A reversal quarter in the private-mark book (remember $9.1B of cumulative downward adjustments already exist) would produce a violent headline miss with **zero** change to the business. Deferred tax of $22.8B is a real claim on future cash.
- **Free cash flow is effectively zero-adjacent**: H1 FCF $4.3B, −82% YoY; Q2 FCF **negative $5.9B**. With $29.1B of capex incurred but unpaid, Q3 will be capex-heavy again.
- **Buyback = $0** while issuing $30.5B common + $19.1B convertible preferred. Share count +1.18%. The historical buyback bid is gone.
- **Depreciation +43%** and rising; capex/revenue at 35–37% is a multi-year margin gravity well.
- **Legal accrual $17.4B, still growing**; regulatory/antitrust tail risk not resolved.
- **Tax rate +200 bp**; interest expense **+514%** YoY and rising with the new debt stack.

**Concrete positioning ideas (fundamentals-driven, no price levels asserted):**
1. **Trade the core, not the headline.** Anchor valuation work on core EPS ~$5.29 H1 (≈$10.6 annualized) and core pre-tax ~$80.2B H1 — not the $14.24 reported. If the market is capitalizing headline EPS, that is a short-side mispricing risk; if it is capitalizing core, the setup is constructive.
2. **Underwrite the capex number, not the EPS number.** The single highest-information datapoint at Q3 FY2026 (expected ~late Oct 2026, 10‑Q) is the quarterly capex and the "capex incurred but not yet paid" balance. A sequential decline in capex *and* that accrual would be a **material positive re-rating catalyst** (FCF restoration + margin relief). Continued escalation above ~$45B/quarter with negative FCF would justify multiple compression regardless of revenue growth.
3. **Watch the buyback line.** Any resumption of repurchases in the Q3 cash-flow statement would signal management believes the capex peak is behind it — historically a strong signal. A second consecutive zero, alongside further equity/preferred issuance, is a persistent supply overhang.
4. **Monitor mark-to-market asymmetry.** Track the "equity securities without readily determinable fair value" balance and cumulative upward-adjustment line each quarter. A flattening of upward marks mechanically removes the growth rate of reported EPS — expect optically brutal YoY comps from Q1 FY2027 onward.
5. **Prefer owning volatility into the Q3 print.** The distribution of outcomes around "capex trajectory × mark-to-market direction" is unusually wide relative to the stability of the underlying +24% revenue engine.

---

## 10. Monitoring checklist for the next 90 days

| Priority | Metric | Where | Bullish trigger | Bearish trigger |
|---|---|---|---|---|
| 1 | Quarterly capex + capex-incurred-not-yet-paid | 10‑Q cash flow / PP&E note | Capex <$40B/qtr and accrual falls from $29.1B | Capex >$45B/qtr, accrual above $29.1B |
| 2 | Free cash flow | 10‑Q | FCF back above ~$15B/qtr | Second consecutive negative-FCF quarter |
| 3 | Buyback line | Financing activities | Any repurchase >$0 | $0 again + more equity/preferred issuance |
| 4 | Revenue growth & operating margin | Income statement | Growth ≥+23%, margin ≥35% | Growth <+20% or margin <33% |
| 5 | Equity-securities marks | Nonoperating income + BS | Continued upward adjustments | Reversal / impairment of non-marketable book |
| 6 | D&A growth | Cash flow | <+30% YoY | >+50% YoY (capex hitting P&L) |
| 7 | Diluted share count | Cover page | Flat or falling | Further +1%+ increases |
| 8 | Legal contingency accrual | Balance sheet | Release / settlement | Further increases above $17.4B |
| 9 | Insider Form 4 activity | **External source required** | — | — (not covered by this data) |

---

## 11. Summary table

| Category | Metric | Latest (H1 FY2026 / 2026‑06‑30) | Prior comparable | YoY change | Assessment |
|---|---|---|---|---|---|
| **Filing anchor** | Latest 10‑Q accepted | 2026‑07‑23 (Q2 FY2026) | 2026‑04‑30 (Q1) | — | Fully current |
| **Revenue (derived)** | H1 revenue | $229,692M | $186,662M | **+23.1%** | ✓ Accelerating (Q2 +24.2% vs Q1 +21.8%) |
| Revenue | Q2 revenue (derived) | $119,796M | $96,428M | +24.2% | ✓ Strong |
| **Profitability** | Gross margin | 62.0% | 59.6% | +240 bp | ✓ |
| Profitability | Operating income | $80,466M | $61,877M | +30.0% | ✓ |
| Profitability | Operating margin | 35.0% (Q1 36.1% → Q2 34.0%) | 33.2% | +188 bp | ✓ but decelerating sequentially |
| **Earnings quality** | Reported net income | $174,771M | $62,736M | +178% | ✗ 78% from non-cash marks |
| Earnings quality | Equity securities FV-NI gain | $135,946M | $11,411M | nm | ✗ Non-cash, reversible |
| Earnings quality | **Core net income (est.)** | **~$64,897M** | ~$53,314M | **+21.7%** | ✓ The real engine |
| EPS | Reported diluted EPS | $14.24 | $5.12 | +178% | ✗ Contaminated |
| EPS | **Core diluted EPS (est.)** | **~$5.29** | ~$4.35 | **+21.6%** | ✓ |
| **Cash flow** | Operating cash flow | $84,859M | $63,897M | +32.8% | ✓ |
| Cash flow | Capex (PP&E) | $80,598M | $39,643M | **+103.3%** | ✗ 35.1% of revenue |
| Cash flow | **Free cash flow** | **$4,261M** (Q2: −$5,855M) | $24,254M | **−82.4%** | ✗ Critical watch item |
| Cash flow | Capex incurred, unpaid | $29,113M | $10,635M | +174% | ✗ Committed future outflow |
| **Balance sheet** | Total assets | $921,983M | $595,281M (12/31/25) | +54.9% | ✓/⚠ MTM-driven |
| Balance sheet | Cash + ST investments | $242,474M | $126,843M | +91.2% | ✓ |
| Balance sheet | Total debt | $101,085M | $49,085M | +105.9% | ⚠ Deliberate leverage-up |
| Balance sheet | **Net cash** | **+$141,400M** | +$77,758M | — | ✓ Fortress |
| Balance sheet | Deferred tax liability (net) | $22,819M | $919M | +2,383% | ⚠ Tax on paper gains |
| Balance sheet | Legal contingency accrual | $17,356M | $15,594M | +11.3% | ⚠ Regulatory overhang |
| **Capital returns** | Buybacks | **$0** | $28,306M | −100% | ✗ Buyback bid removed |
| Capital returns | Common stock issued | $30,499M | $0 | new | ⚠ Dilution |
| Capital returns | Convertible preferred issued | $19,063M (closed 6/5/26) | $0 | new | ⚠ Potential future dilution |
| Capital returns | Dividends | $5,231M ($0.43/sh) | $4,977M ($0.41/sh) | +4.9% | Neutral |
| Capital returns | Shares outstanding | 12,230M | 12,088M | +1.18% | ✗ Dilutive |
| **Other** | SBC | $15,200M (6.6% of revenue) | $11,500M (6.2%) | +32.2% | ⚠ |
| Other | Depreciation | $13,586M | $9,485M | +43.2% | ⚠ Future margin drag |
| Other | Effective tax rate | 19.1% | 17.1% | +200 bp | ⚠ |
| Other | Interest expense | $1,811M | $295M | +514% | ⚠ Rising with debt |
| **Insider transactions** | Form 4 data | **DATA_UNAVAILABLE** | — | — | Not assessable — do not infer |

**Bottom line:** GOOGL's *operating* business is the strongest it has been in this dataset — 24% revenue growth that is accelerating, +190 bp of operating margin, and +33% operating cash flow. But the *reported* earnings are dominated by a $135.9B non-cash revaluation, free cash flow has collapsed to near zero (negative in Q2), buybacks have stopped while equity, preferred and debt are being issued, and depreciation is compounding at +43%. The trade is a two-variable problem: **capex discipline (FCF + margin) versus mark-to-market persistence (headline EPS)**. Position on core earnings; do not pay for the reported number — and source insider data externally, as it is absent here.