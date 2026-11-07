# GOOGL — Fundamental Research Report
**Company:** Alphabet Inc. (NASDAQ: GOOGL, Class A) | **As-of date:** 2026-08-20
**Latest filing in vendor package:** 10-Q for the period ended 2026-06-30, accepted 2026-07-23 (accn 0001652044-26-000071); FY2025 10-K accepted 2026-02-05 (accn 0001652044-26-000018).

---

## 1. Bottom line up front

1. **Operating momentum is genuinely strong.** Derived revenue for Q2 2026 was **$119.8B (+24.2% YoY)** and operating income **$40.77B (+30.4% YoY)**, with operating margin expanding to **34.0%** from 32.4%. H1 2026 revenue **$229.7B (+23.1%)**, operating income **$80.5B (+30.0%)**.
2. **But headline earnings are ~65–70% non-operating.** Q2 net income of **$112.2B** includes **$99.0B of equity-securities fair-value/realized gains** in other income; H1 gains totaled **$135.9B** vs **$11.0B** in H1 2025. Reported diluted EPS of **$9.11** (Q2) and **$14.24** (H1) is not a proxy for earning power — my "operating-only" reconstruction implies roughly **$2.61** and **$5.29** respectively (still +16% and +21% YoY — healthy, just not +294%).
3. **The capital-intensity regime has changed abruptly.** H1 2026 capex **$80.6B (+103% YoY)** against CFO of **$84.9B**; **Q2 free cash flow turned negative (~–$5.9B)**, first time in the data. Capex incurred-but-unpaid jumped to **$29.1B** (from $15.1B at FY25-end), implying more cash outflow ahead — accrual-basis H1 capex is ~$94.6B and accrual FCF is roughly **–$9.8B**.
4. **Funding mix flipped from shrinkage to expansion.** H1 2026: **$0 buybacks** (vs $28.3B in H1 2025), **$30.5B common stock issued** (+142M shares, +1.2% dilution), **$19.1B convertible preferred issued (2026-06-05)**, **$56.2B gross debt raised** (carrying debt $49.1B → $101.1B), plus **$3.8B minority-interest proceeds**. Total assets +54.9% in six months.
5. **Balance sheet remains fortress-grade:** cash + short-term investments **$242.5B** vs total debt ~$103.7B → **net cash ≈ $139B**, even after the raise. Liquidity is not the issue; returns on the spend and FCF recovery are.

**Trading stance implied by the data:** fundamentals support the *operating* story (revenue acceleration, gross-margin expansion, Cloud/AI-era reinvestment); the *reported* EPS and any screener-based P/E are distorted. Risk is asymmetric around (a) reversal of investment marks, (b) depreciation catch-up as capex converts to D&A, (c) negative FCF persistence.

---

## 2. Company profile & data scope

Alphabet Inc. is the parent of Google (Google Services: Search/YouTube advertising, subscriptions-platforms-devices; Google Cloud) and Other Bets. **Note on scope:** the configured fundamental vendor returned only point-in-time SEC XBRL facts — **no profile narrative, no segment revenue tables, no valuation multiples, no price data, and no insider-transaction archive** ("DATA_UNAVAILABLE" for insider transactions; I will not infer insider activity). Segment-level revenue (Search vs Cloud vs YouTube) and R&D/S&M line detail sit in tags alphabetically beyond the vendor's returned row window, so several figures below are **derived** and labelled as such.

---

## 3. Income statement — Q2 2026 and H1 2026

All figures $B. Revenue derived as `OperatingIncomeLoss + CostsAndExpenses` (validated: this method reproduces Q2 2025 revenue of $96.43B exactly vs. reported GAAP).

| Metric | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---|---|---|---|---|---|
| Revenue (derived) | 119.80 | 96.43 | **+24.2%** | 229.69 | 186.66 | **+23.1%** |
| Cost of revenue | 45.94 | 39.04 | +17.7% | 87.21 | 75.40 | +15.7% |
| Gross profit (derived) | 73.85 | 57.39 | +28.7% | 142.48 | 111.26 | +28.1% |
| **Gross margin** | **61.6%** | 59.5% | +210bp | **62.0%** | 59.6% | +240bp |
| Opex ex-COGS (derived) | 33.08 | 26.12 | +26.7% | 62.01 | 49.39 | +25.6% |
| of which G&A | 6.46 | 5.21 | +24.0% | 10.75 | 8.75 | +22.9% |
| **Operating income** | **40.77** | 31.27 | **+30.4%** | **80.47** | 61.88 | **+30.0%** |
| **Operating margin** | **34.0%** | 32.4% | +160bp | **35.0%** | 33.2% | +180bp |
| Nonoperating income | **97.98** | 2.66 | n.m. | **135.70** | 13.85 | n.m. |
| — equity securities FV gains | 99.03 | 1.29 | n.m. | 135.95 | 11.04 | n.m. |
| — interest income | 1.43 | 1.05 | +36% | 2.81 | 2.05 | +37% |
| — interest expense | 1.28 | 0.26 | **+390%** | 1.81 | 0.30 | **+514%** |
| Pre-tax income | 138.75 | 33.93 | +309% | 216.17 | 75.72 | +185% |
| Tax | 26.56 | 5.74 | — | 41.39 | 12.99 | — |
| **Effective tax rate** | **19.1%** | 16.9% | +220bp | **19.1%** | 17.1% | +200bp |
| Net income | **112.19** | 28.20 | +298% | **174.77** | 62.74 | +179% |
| Net income to common | 112.11 | 28.20 | — | 174.69 | 62.74 | — |
| Diluted EPS | **$9.11** | $2.31 | +294% | **$14.24** | $5.12 | +178% |
| Diluted shares (derived) | ~12,306M | ~12,206M | +0.8% | ~12,272M | ~12,255M | +0.1% |

**Sequential read:** Q1 2026 revenue $109.9B (+21.8% YoY), operating income $39.70B (36.1% margin), opex $28.93B. Q2 revenue accelerated ~9% QoQ but **operating margin declined ~210bp QoQ (36.1% → 34.0%)** as opex grew ~14% QoQ — the first sign that the AI/infra build is beginning to bite into margin.

**Cost structure observations**
- **Gross margin is the engine**: +210–240bp YoY. Cost of revenue (which includes traffic acquisition and content costs) grew only 15.7% vs revenue +23.1% — a favorable mix/scale signal.
- **Opex is growing faster than revenue in Q2** (+26.7% vs +24.2%). Margin expansion is entirely a gross-margin story; if gross margin normalizes, operating margin compresses.
- **Stock-based comp: $8.00B in Q2 (+33% YoY), $15.20B H1 (+32%)** — 6.7% of revenue vs 6.2% a year ago. Any "non-GAAP" EPS adds this back; it is a real ~$30B+/yr dilution cost, partially offsetting the buyback halt.
- **D&A: $14.62B H1 2026 (+47% YoY)** — depreciation $13.59B (+43%), intangible amortization $0.55B (from $0.25B), finance-lease ROU amortization $0.49B. **Critically, H1 capex of $80.6B is ~8x quarterly depreciation**, so depreciation is structurally set to accelerate sharply over the next 4–8 quarters — a mechanical margin headwind the current 34–35% operating margin does not yet reflect. (Amortization of existing finite-lived intangibles is guided at ~$1.30B for the next twelve months; gross finite-lived intangibles jumped from $2.47B to $10.59B, implying acquisition activity.)

---

## 4. Earnings quality — separating the two businesses

The **investment portfolio has become a larger P&L driver than the operating business** in reported terms. Reconstruction of "operating-only" earnings (stripping equity-securities FV/realized gains and taxing at the reported rate):

| | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|
| Reported diluted EPS | $9.11 | $2.31 | $14.24 | $5.12 |
| Non-operating ex-gains | (1.05) | +1.38 | (0.25) | +2.80 |
| Pre-tax, operating-only | 39.72 | 33.05 | 80.22 | 64.68 |
| Operating-only net income | ~32.1 | ~27.5 | ~64.9 | ~53.6 |
| **Operating-only EPS (est.)** | **~$2.61** | ~$2.25 | **~$5.29** | ~$4.38 |
| **Operating-only EPS growth** | **+16%** | — | **+21%** | — |
| Operating-only EPS ex-SBC (est.) | ~$3.14 | ~$2.66 | ~$6.29 | ~$5.15 |
| Ex-SBC growth | **+18%** | — | **+22%** | — |

**Interpretation:** the underlying franchise is compounding EPS at a **high-teens/low-20s** rate — excellent for a company of this size. The other **~$6.50 of Q2's $9.11 and ~$9.00 of H1's $14.24 comes from investment revaluations** that are non-recurring in nature and mark-to-market reversible. Traders anchoring on the $9.11 print, or on a resulting single-digit P/E, are anchoring on the wrong number.

**Corroborating balance-sheet evidence of the revaluation:**
- Non-marketable equity securities carried at fair value: **$64.1B → $124.3B** (+$60.2B in six months); cumulative *upward* adjustments $44.5B → **$85.7B** (+$41.2B), cumulative downward adjustments $8.8B → $9.1B.
- **Deferred tax liabilities $0.92B → $22.82B** (+$21.9B) — the tax bill on unrealized gains is being booked but not paid.
- Deferred tax assets collapsed $9.11B → $1.45B; the H1 cash-flow statement carries a **+$27.5B deferred-tax add-back**, i.e., **~66% of the $41.4B tax provision is non-cash**.

---

## 5. Balance sheet — a 55% expansion in two quarters

| $B | 2026-06-30 | 2025-12-31 | Δ |
|---|---|---|---|
| Cash & equivalents | 55.91 | 30.71 | +82% |
| Cash + short-term investments | **242.47** | 126.84 | **+91%** |
| AFS debt securities (FV) | 99.50 | — | — |
| Accounts receivable, net | 69.18 | 62.89 | +10.0% |
| — allowance / gross AR | 1.44% | 1.47% | improving |
| Current assets | 343.52 | 206.04 | +66.7% |
| **Total assets** | **921.98** | **595.28** | **+54.9%** |
| Accounts payable | 20.26 | 12.20 | +66% |
| Accrued liabilities | 73.01 | 55.56 | +31.4% |
| Accrued income taxes, current | 5.23 | 0.52 | +900% |
| Loss contingency accrual, current | 17.36 | 15.59 | +11.3% |
| Deferred revenue (contract liability) | 10.10 | 8.60 | +17.4% |
| Deferred tax liabilities, net | 22.82 | 0.92 | +2,380% |
| **Debt carrying amount** | **101.09** | 49.09 | **+106%** |
| Finance lease liabilities | 2.59 | 2.50 | +3.6% |
| Operating lease liabilities | 18.04 | 15.95 | +13.1% |
| Convertible preferred stock | 18.02 | 0.00 | new |
| Common stock + APIC | 131.37 | 93.13 | +38.24 |
| AOCI | (2.29) | (1.92) | — |
| Shares outstanding | 12,230M | 12,088M | +1.2% |

**Key reads**
- **Net cash ≈ $139B** (cash+investments $242.5B less debt $101.1B, ignoring $2.6B finance leases and $18.0B preferred). Leverage is a strategy choice, not distress — but debt **doubled in six months** and interest expense is up **5–6x YoY** ($1.28B in Q2 alone, annualizing ~$5.1B).
- **Working capital quality is fine**: receivables +10% vs revenue +23% YoY means DSOs *improved* (~52 days); allowance held at ~1.4% of gross AR. Accrued liabilities +31% and AP +66% look like capex/infra accruals, consistent with the $29.1B capex-incurred-not-paid spike.
- **AFS portfolio credit quality is strong**: unrealized-loss positions total $53.2B with accumulated losses of only **$0.42B (0.8%)**; losses >12 months are just $0.15B. Mark-to-market risk in the bond book is trivial; the risk is concentrated in the **private/non-marketable equity book**.
- **Preferred stock + dividends-in-excess-of-retained-earnings**: the $18.0B convertible preferred (issued 2026-06-05, $86M preferred dividends in H1) is unprecedented for this capital structure, and the recurring "dividends in excess of retained earnings" adjustment ($5.25B charged to APIC in H1 2026, $5.06B in H1 2025) implies **retained earnings are effectively exhausted** — a legacy of multi-year buybacks plus the young dividend. Book equity is therefore no longer a clean cushion metric; do not rely on P/B.
- **Data gap:** total liabilities and total stockholders' equity tags were beyond the vendor's returned row window; ROE/book value could not be computed directly and are deliberately omitted rather than estimated.

---

## 6. Cash flow — the FCF inflection is the single most important fundamental fact

| $B | Q1 2026 | Q2 2026 | H1 2026 | H1 2025 | YoY |
|---|---|---|---|---|---|
| Operating cash flow | 45.79 | 39.07 | **84.86** | 63.90 | **+32.8%** |
| Capex (cash) | 35.67 | 44.92 | **80.60** | 39.64 | **+103%** |
| **Free cash flow** | **+10.12** | **(5.86)** | **+4.26** | +24.25 | **–82%** |
| Capex / CFO | 78% | 115% | **95%** | 62% | +33pt |
| Investing cash flow | (63.39) | (82.43) | (145.82) | (40.74) | +258% |
| Financing cash flow | +25.08 | +61.24 | **+86.32** | (26.03) | n.m. |
| — debt proceeds / (repayments) | 31.38 / (1.48) | 24.85 / (3.77) | **+56.23 / (5.25)** | 31.38 / (18.40) | — |
| — common stock issued | 0.00 | 30.50 | **30.50** | 0.00 | — |
| — convertible preferred issued | 0.00 | 19.06 | **19.06** | 0.00 | — |
| — buybacks | 0.00 | 0.00 | **0.00** | (28.31) | **–100%** |
| — dividends paid | 2.54 | 2.69 | (5.23) | (4.98) | +5% |
| — minority-interest proceeds | 3.20 | 0.56 | 3.76 | 0.40 | +840% |
| FX effect on cash | — | — | (0.15) | +0.44 | — |
| Net change in cash | — | — | **+25.20** | (2.43) | — |

**Interpretation and actionable detail**
1. **Cash flow quality is high but FCF is gone.** CFO +32.8% with a $27.5B non-cash deferred-tax add-back built in — i.e., CFO is *flattered* by non-cash items tied to investment marks. Even so, capex of 95% of CFO means **the company is currently self-funding capex almost exactly to zero FCF**.
2. **Accrual capex is worse than cash capex.** Capex incurred-but-not-yet-paid: $29.11B at 6/30/26 vs $15.09B at FY25-end and $10.64B at 6/30/25. Adjusting, H1 accrual capex ≈ **$94.6B** and accrual FCF ≈ **–$9.8B**. The Q3/Q4 cash capex print should be expected to *rise* again.
3. **Funding is explicit and disclosed, not accidental.** $30.5B equity, $19.1B convertible preferred, $56.2B debt, $3.8B minority capital = **~$109.6B of external capital in six months**, alongside the first **zero-buyback half since buybacks began**. That is a deliberate pivot from "return capital + shrink share count" to "raise capital + fund buildout." For shareholders this is the single biggest regime change in the package: the historic buyback EPS tailwind is *now a headwind* (+142M shares, +1.2%).
4. **Investing outflows beyond capex:** $76.5B marketable securities purchased and $22.1B of "other investments" purchased (vs $2.3B H1 2025) — the latter is consistent with a step-up in strategic/AI-ecosystem stakes, matching the non-marketable equity jump.
5. **Dividend is symbolic:** $0.22/share quarterly ($0.43 H1, annualizing ~$0.88) with only 5% growth; it is not a valuation support mechanism at this payout level, but the continued increase signals confidence.
6. **Legal/regulatory:** loss-contingency accruals of **$17.36B current** (+11.3% since YE25), with $3.0B of payments made in Q3 2025. This is a live, material liability to monitor alongside any margin compression.

---

## 7. Trend/history context available in the package

- FY2023/FY2024/FY2025 financing cash flows: **–$72.1B / –$79.7B / –$37.4B** — the classic buyback-heavy profile, which reversed to **+$86.3B in H1 2026 alone**. That single comparison quantifies the capital-allocation regime change.
- Finance-lease principal payments: $0.71B (2023) → $0.41B (2024) → $1.99B (2025) → $0.84B in H1 2026 — infrastructure leasing is scaling.
- Capex incurred-not-paid: $7.44B (2023) → $10.33B (2024) → $15.09B (2025) → $29.11B at 6/30/26 — a clean, monotonic acceleration in the capex pipeline.
- Debt maturity ladder at YE25: $2.0B (2026), $1.0B (2027), $2.68B (2028), $1.76B (2029), $5.5B (2030), $36.1B thereafter — well-laddered, no refinancing wall, though the 2026 issuance materially lengthens the profile.
- Operating lease commitments: $21.3B undiscounted ($3.50B next 12 months); finance leases $2.92B. Data-center/office commitments are manageable against $242B liquidity.

---

## 8. Principal risks and watch items (ranked)

| # | Risk | Evidence | What to watch |
|---|---|---|---|
| 1 | **Earnings quality / reversal risk** — reported EPS is largely mark-to-market | $135.9B H1 equity gains vs $80.5B operating income; $22.8B DTL created | Any Q3 mark-down; AOCI; the private-equity fair-value footnote |
| 2 | **Negative FCF becoming structural** | Q2 FCF –$5.9B; capex 115% of CFO; $29.1B accrued capex | Q3 capex and CFO; FY capex guidance |
| 3 | **Depreciation catch-up** | H1 D&A $14.6B vs capex $80.6B (8:1) | D&A growth vs revenue growth; operating margin path |
| 4 | **Opex outgrowing revenue** | Q2 opex +26.7% vs revenue +24.2%; margin –210bp QoQ | R&D/S&M lines; headcount commentary |
| 5 | **Financing/dilution dependence** | $109.6B raised in H1; zero buybacks; +1.2% share count; interest expense +390% | New debt/preferred issuance; buyback resumption |
| 6 | **Tax rate step-up** | 17.1% → 19.1% ETR | Q3 ETR; OECD/global minimum tax effects |
| 7 | **Legal/regulatory** | $17.4B loss-contingency accrual, +11% in 6 months | Antitrust remedies, EU/US actions |
| 8 | **Data/analytics risk** | No insider-transaction archive; no segment or valuation data supplied | Obtain segment revenue split before sizing positions |

---

## 9. Actionable conclusions for traders

- **Do not use the $9.11/$14.24 prints to compute P/E.** On my operating-only reconstruction, run-rate EPS is ~$2.61 (Q2) / ~$5.29 (H1) — roughly a third of headline. Any screen showing a mid-single-digit P/E on GOOGL after this quarter is an artifact of the investment marks.
- **Positive, defensible signal:** revenue +24%, gross margin +210bp, operating income +30%, DSOs improving, AFS book essentially unimpaired, net cash ~$139B. The franchise is accelerating, not decelerating.
- **Negative, equally concrete signal:** Q2 FCF negative, capex/cfo at 95%, buyback at zero, share count rising, preferred + debt + equity issuance, interest expense up 5x, and a $29B accrued-capex overhang. Free cash flow per share — the metric that historically drove this equity — is now declining.
- **Highest-conviction near-term catalyst set:** (a) Q3 2026 capex/CFO spread and whether FCF returns positive; (b) the trajectory of D&A and operating margin as capex capitalizes; (c) any fair-value mark-down on the $124B non-marketable book; (d) buyback resumption, which would be a strong signal that management views the buildout as fully funded.
- **Positioning logic:** treat the operating business as a high-teens/low-20s EPS compounder with a fortress balance sheet, and treat the $136B of H1 investment gains as a **separate, non-repeatable, reversible** item that should be excluded from valuation but included in balance-sheet/quality analysis. Volatility around reported EPS will be large and driven by marks, not operations — size positions accordingly and prefer operating-metric comparisons for entry/exit.

---

## 10. Key data summary table

| Category | Metric | Value | Period | Read-through |
|---|---|---|---|---|
| **Growth** | Revenue (derived) | $119.80B / $229.69B | Q2 26 / H1 26 | +24.2% / +23.1% YoY — accelerating |
| | Operating income | $40.77B / $80.47B | Q2 26 / H1 26 | +30.4% / +30.0% YoY |
| | Diluted EPS (reported) | $9.11 / $14.24 | Q2 26 / H1 26 | +294% / +178% YoY (marks-driven) |
| | Diluted EPS (operating-only, est.) | ~$2.61 / ~$5.29 | Q2 26 / H1 26 | +16% / +21% YoY — the real trend |
| **Margins** | Gross margin | 61.6% / 62.0% | Q2 26 / H1 26 | +210bp / +240bp — main driver |
| | Operating margin | 34.0% / 35.0% | Q2 26 / H1 26 | +160bp YoY but –210bp QoQ |
| | Effective tax rate | 19.1% | H1 26 | up from 17.1%; ~66% non-cash |
| **Quality** | Equity securities FV gains | $99.03B / $135.95B | Q2 26 / H1 26 | vs $1.29B / $11.04B prior — not operating |
| | SBC | $8.00B / $15.20B | Q2 26 / H1 26 | +33% YoY; 6.7% of revenue |
| | D&A | $14.62B | H1 26 | +47% YoY; 8x behind capex → rising |
| **Cash** | CFO | $84.86B | H1 26 | +32.8% YoY |
| | Capex | $80.60B | H1 26 | +103% YoY; 95% of CFO |
| | **Free cash flow** | **+$4.26B (Q2: –$5.86B)** | H1 26 | **–82% YoY; accrual basis ≈ –$9.8B** |
| | Capex incurred, unpaid | $29.11B | 6/30/26 | vs $15.09B YE25 — more outflow coming |
| **Balance sheet** | Total assets | $921.98B | 6/30/26 | +54.9% in 6 months |
| | Cash + ST investments | $242.47B | 6/30/26 | +91% since YE25 |
| | Total debt (carrying) | $101.09B | 6/30/26 | +106%; net cash ≈ $139B |
| | Convertible preferred | $18.02B | 6/30/26 | New — issued 2026-06-05 |
| | Deferred tax liabilities | $22.82B | 6/30/26 | +$21.9B on unrealized gains |
| | Non-marketable equity at FV | $124.26B | 6/30/26 | from $64.09B; +$41.2B upward adj. |
| | Loss contingency accrual | $17.36B | 6/30/26 | +11.3% since YE25 |
| | Shares outstanding | 12,230M | 6/30/26 | +142M (+1.2%) — dilution, not shrinkage |
| **Capital allocation** | Buybacks | $0 | H1 26 | vs $28.31B H1 25 — **halted** |
| | Common stock issued | $30.50B | H1 26 | First material issuance in the dataset |
| | Debt issued / repaid | $56.23B / $5.25B | H1 26 | Leveraging up deliberately |
| | Dividends | $0.43/sh ($5.23B) | H1 26 | +5% YoY; ~$0.88 annualized |
| **Gaps** | Insider transactions | **Unavailable** | — | Vendor has no point-in-time archive; do not infer |
| | Segment revenue, R&D/S&M, total equity, valuation multiples | Not returned | — | Outside vendor row window; flagged, not estimated |

*Derived figures (revenue, gross profit, opex, operating-only EPS, Q2 standalone cash flows, FCF) were computed from the vendor's reported XBRL facts; the revenue derivation was validated against known prior-year actuals. FY2023–FY2025 comparatives are from the 10-K accepted 2026-02-05. No insider-transaction data was provided and none has been assumed.*