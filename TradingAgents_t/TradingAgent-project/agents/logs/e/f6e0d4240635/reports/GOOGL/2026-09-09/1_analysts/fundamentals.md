# GOOGL — Alphabet Inc. Fundamental Research Report
**As of 2026-09-09 | Latest filing in scope: Q2 2026 Form 10-Q (accepted 2026-07-23) | FY2025 Form 10-K (accepted 2026-02-05)**

---

## 1. Executive Summary

GOOGL enters September 2026 in the middle of the most aggressive capital-allocation pivot in its history. The operating business is accelerating — H1 2026 revenue grew **+23.1% YoY** to **$229.7B**, gross margin expanded **+240bp to 62.0%**, and operating income rose **+30.0% to $80.5B** — but the company is spending at a pace that has temporarily broken the free-cash-flow machine: **H1 capex doubled to $80.6B (+103% YoY)**, H1 free cash flow collapsed **-82% to $4.3B**, and **Q2 2026 standalone FCF turned negative (-$5.9B)**.

Headline GAAP EPS of **$14.24 (H1)** is *not* an operating number. It includes roughly **$135.7B of non-operating gains**, overwhelmingly mark-to-market appreciation on equity securities (equity-securities FV gains of $135.9B). Core, operating-derived EPS is approximately **$5.37**, up ~25% YoY — still excellent, but less than half the headline figure. Screening GOOGL on GAAP P/E today would materially misprice the stock.

To fund the build-out, Alphabet has reversed its capital-return stance: **buybacks went to zero** (vs. $28.3B in H1 2025) while it raised **$56.2B of debt**, **$30.5B of common equity**, **$19.1B of convertible preferred**, and **$3.8B from minority investors**. The balance sheet is still a fortress (**$242.5B cash + short-term investments vs. $101.1B debt = ~$141B net cash**), but gross debt doubled in six months and interest expense rose 5x.

**Net stance: fundamentally strong operating franchise, deteriorating cash conversion, and a large valuation-quality trap in GAAP earnings. The tradable variable for the next two quarters is capex discipline and FCF inflection, not revenue growth.**

---

## 2. Data Provenance & Important Limitations

Before the analysis, what the data does and does not support:

- **Available:** point-in-time SEC XBRL facts from the Q2 2026 10-Q and FY2025 10-K: income statement, balance sheet, cash flow, share count, debt, leases, tax items, investment marks.
- **Not available from the vendor:** company profile, market capitalization, share price, P/E, EV/EBITDA, segment revenue breakdown (Google Search / YouTube / Cloud / Other Bets), headcount, or management guidance. **No valuation multiple is asserted in this report.**
- **Insider transactions: DATA_UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for GOOGL as of 2026-09-09. No insider buying/selling is inferred.
- **Revenue is derived**, not directly tagged in the returned data. It is computed from the accounting identity: `Revenue = CostsAndExpenses + OperatingIncomeLoss`. This reconstructs exactly to reported totals and is internally consistent across all periods (cross-checked against cost-of-revenue and operating-income lines), but should be understood as derived.
- Only **H1 2025 vs. H1 2026** and **Q2 2025 vs. Q2 2026** income-statement comparatives are available. Multi-year income history (2023/2024) was not returned; multi-year cash-flow and capex history is available and used.

---

## 3. Company Profile (qualitative; context only)

Alphabet Inc. is the parent of Google, organized around Google Services (Search, YouTube, Android, Chrome, Play, Maps, devices), Google Cloud (infrastructure, Workspace, AI platform), and Other Bets. Its economic engine is advertising, with cloud and subscription/device revenue as the growth and diversification layer. The company operates one of the largest owned AI compute fleets in the world, and the 2026 financials show a strategic shift toward monetizing that fleet (cloud/AI infrastructure) while simultaneously funding it at hyperscale. *This paragraph is qualitative background; all figures below are from the filings.*

---

## 4. Income Statement — H1 and Q2 2026

### 4.1 Headline results (derived revenue)

| $B | H1 2025 | H1 2026 | YoY | Q2 2025 | Q2 2026 | YoY |
|---|---|---|---|---|---|---|
| Revenue (derived) | 186.66 | 229.69 | **+23.1%** | 96.43 | 119.80 | **+24.2%** |
| Cost of revenue | 75.40 | 87.21 | +15.7% | 39.04 | 45.94 | +17.7% |
| Gross profit | 111.26 | 142.48 | +28.1% | 57.39 | 73.85 | +28.7% |
| **Gross margin** | **59.6%** | **62.0%** | **+240bp** | **59.5%** | **61.6%** | **+210bp** |
| Operating expenses | 49.39 | 62.01 | +25.6% | 26.12 | 33.08 | +26.7% |
| **Operating income** | **61.88** | **80.47** | **+30.0%** | **31.27** | **40.77** | **+30.4%** |
| **Operating margin** | **33.1%** | **35.0%** | **+190bp** | **32.4%** | **34.0%** | **+160bp** |
| Non-operating income | 13.85 | 135.70 | +880% | 2.66 | 97.98 | n.m. |
| Pre-tax income | 75.72 | 216.17 | +185% | 33.93 | 138.75 | +309% |
| Tax expense | 12.99 | 41.39 | +219% | 5.74 | 26.56 | +363% |
| **Effective tax rate** | **17.1%** | **19.1%** | **+200bp** | **16.9%** | **19.1%** | **+220bp** |
| **Net income** | **62.74** | **174.77** | **+178.6%** | **28.20** | **112.19** | +298% |
| Net income to common | 62.74 | 174.69 | +178% | 28.20 | 112.11 | +298% |
| **Diluted EPS** | **$5.12** | **$14.24** | **+178%** | **$2.31** | **$9.11** | +294% |

**Key read:** the *operating* story is a clean double-beat. Revenue accelerated from +21.8% in Q1 to +24.2% in Q2, and gross margin expanded even as depreciation surged **+43% YoY to $13.6B** and cost of revenue rose. That combination — rising depreciation absorbed while margins still expand — is direct evidence that AI infrastructure is being monetized at a return, not merely built. Q2 is the strongest operating quarter in the dataset.

### 4.2 Cost structure

- **G&A:** $10.75B H1 (+22.9%), $6.46B in Q2 (+24.0%) — growing slightly slower than revenue.
- **R&D + sales/marketing (residual opex):** $51.26B H1 vs. $40.64B (+26.1%); Q2 $26.62B vs. $20.91B (+27.3%). This is the fastest-growing opex bucket and is consistent with AI talent and go-to-market spend.
- **Stock-based compensation:** **$15.20B H1 (+32.2%)**, of which **$8.00B in Q2 alone (+33%)**. SBC is now **6.6% of revenue** (vs. 6.2%), and Q2's $8.0B is a step-function higher than the $7.2B implied for Q1. This is a real economic cost and a dilution source that coexists with the equity issuance discussed below.
- **Depreciation:** $13.59B H1 (+43.2%), 5.9% of revenue vs. 5.1%. Expect this to keep climbing sharply — capex is running at roughly 6x the depreciation rate, so the P&L depreciation drag is still in the early innings.
- **Amortization of intangibles:** $545M H1 vs. $246M (+122%), with $367M in Q2 — signals recent acquisitions/asset purchases. Forward amortization schedule: $747M remainder of FY2026, then ~$1.30B, $1.14B, $1.10B, $1.06B in the following years.
- **Interest expense:** $1.81B H1 vs. $0.30B (+514%); **$1.28B in Q2 alone**. Interest income rose only +37% to $2.81B, so *net* interest income fell to ~$1.0B from ~$1.76B. The new debt is already a P&L item.

### 4.3 Earnings quality — the single most important caveat

H1 2026 non-operating income of **$135.70B** dwarfs operating income of $80.47B. The composition:

- **Equity securities FVNI gains: $135.95B** (H1), of which **$99.03B in Q2 alone**.
- Realized gains on those securities: only $836M H1 / $278M Q2.
- Debt securities AFS: a *loss* of $143M H1.
- Interest income $2.81B, interest expense -$1.81B, FX -$14M.

In other words, **almost the entire non-operating gain is unrealized mark-to-market appreciation on equity stakes**, not cash proceeds. Supporting evidence from the balance sheet: equity securities without readily determinable fair value rose to **$124.26B from $64.09B**, with cumulative *upward* valuation adjustments of **$85.73B** (from $44.49B) against cumulative downward adjustments of $9.12B. A **deferred tax liability of $22.82B** (from $0.92B) was created almost entirely by these marks.

**Actionable implication:** a GAAP-based P/E on H1 annualized EPS (~$28.5) would understate the true multiple by roughly 2.5x. Normalize: strip out the $135.7B pre-tax non-operating gain, add back net interest of ~$1.0B, and tax at 19.1%:

- **H1 2026 core net income ≈ $65.9B**, or **core EPS ≈ $5.37** (diluted; on ~12.28B diluted shares).
- **H1 2025 core net income ≈ $52.7B**, or **~$4.31** — core EPS growth of roughly **+24.5%**, in line with revenue-plus-margin expansion. That is the number to underwrite.

There is also a two-way risk: these marks are volatile and can reverse through the P&L in a single quarter (Q2's $99B gain is a good example of the magnitude). A risk-off event in private tech valuations would produce a violent GAAP EPS swing unrelated to the core business.

### 4.4 Tax

The effective tax rate rose to **19.1% from 17.1%**, a **+200bp** headwind worth roughly $4.3B on H1 pre-tax income. Part of the increase is mechanical — the large FV gains are taxed at a higher rate than the group average, and the DTL build confirms this. On a core basis the rate still looks like a low-19s run-rate versus high-16s/high-17s historically; traders should model ~19% going forward, not 17%.

---

## 5. Balance Sheet — A Six-Month Transformation

| $B | 2025-12-31 | 2026-06-30 | Change |
|---|---|---|---|
| Cash & equivalents | 30.71 | 55.91 | +82% |
| **Cash + short-term investments** | **126.84** | **242.47** | **+91%** |
| AFS debt securities (LT) | n/a | 99.50 | — |
| Accounts receivable, net | 62.89 | 69.18 | +10.0% |
| **Current assets** | **206.04** | **343.52** | **+66.7%** |
| Equity securities w/o readily determinable FV | 64.09 | 124.26 | +93.9% |
| **Total assets** | **595.28** | **921.98** | **+54.9%** |
| Accounts payable | 12.20 | 20.26 | +66.0% |
| Accrued liabilities | 55.56 | 73.01 | +31.4% |
| Accrued income taxes, current | 0.52 | 5.23 | +901% |
| **Total debt (carrying)** | **49.09** | **101.09** | **+105.9%** |
| Deferred tax liabilities | 0.92 | 22.82 | +2,383% |
| Operating lease liability | 15.95 | 18.04 | +13.1% |
| Finance lease liability | 2.50 | 2.59 | +3.6% |
| Convertible preferred stock (equity) | 0.00 | **18.02** | new |
| Common stock + APIC | 93.13 | 131.37 | +41.1% |
| AOCI | (1.92) | (2.29) | -$0.37B |
| Shares outstanding | 12.088B | 12.230B | +1.17% |
| Deferred revenue (total / current) | 8.60 / 6.58 | 10.10 / 7.15 | +17.4% |

**Five observations that matter:**

1. **Total assets grew $326.7B in six months (+54.9%).** That is not organic; it is the combination of a $115.6B liquidity build, a $60.2B revaluation-plus-purchase of equity stakes, and the capex program. Book value is now heavily marked to market and much less "industrial" than in prior years.
2. **Gross debt doubled to $101.1B**, with $56.2B issued in H1 2026 alone against only $5.3B of repayments. The pre-existing maturity ladder was benign (per the FY2025 10-K: $2.0B in 2026, $1.0B 2027, $2.7B 2028, $1.8B 2029, $5.5B 2030, $36.1B beyond 2030); the new issuance presumably extends duration, but the interest burden is real: run-rate interest expense is now ~$5B/year, up from ~$0.6B.
3. **Convertible preferred of $18.0B was issued around 2026-06-05 ($19.0B gross, $19.06B cash)** with $86M of preferred dividends paid in Q2 (~1.8% annualized on gross proceeds). This is a hybrid instrument — it does not show as debt, but it sits ahead of common and carries conversion dilution.
4. **Deferred revenue +17.4% to $10.1B** (current portion $7.15B) is a positive leading indicator for Cloud/enterprise commitments. Revenue recognized from prior deferred balances was $4.9B in H1.
5. **Legal/regulatory accruals:** loss contingency accrual carrying value rose to **$17.36B from $15.59B (+11%)**, and the FY2025 10-K disclosed $3.0B of payments in Q3 2025. This is a persistent, large liability line that should be monitored for step-ups.

**Allowance for doubtful accounts** rose to $995M (1.44% of AR) from $924M (1.47%) — receivables quality is stable, and AR growth (+10%) lagged revenue growth, implying healthy collections (DSO ~53 days on Q2 revenue).

**Net cash position:** $242.5B liquid assets − $101.1B gross debt = **~$141.4B net cash**; **~$123.4B after treating the $18.0B preferred as quasi-debt**. Still net-cash-rich, but the direction of travel is unambiguous.

---

## 6. Cash Flow — The Core Issue

| $B | H1 2025 | H1 2026 | YoY | Q2 2025 | Q2 2026 |
|---|---|---|---|---|---|
| **Operating cash flow** | **63.90** | **84.86** | **+32.8%** | 27.75 | 39.07 |
| Capex (cash PP&E) | 39.64 | 80.60 | **+103.3%** | 22.45 | 44.92 |
| **Free cash flow** | **24.25** | **4.26** | **-82.4%** | **+5.30** | **-5.86** |
| Capex / revenue | 21.2% | 35.1% | +1,390bp | 23.3% | 37.5% |
| FCF / revenue | 13.0% | 1.9% | -1,110bp | 5.5% | -4.9% |
| Investing cash flow | (40.74) | (145.82) | — | — | — |
| Financing cash flow | (26.03) | **+86.32** | — | — | — |
| Buybacks | 28.31 | **0.00** | -100% | — | — |
| Dividends | 4.98 | 5.23 | +5.1% | — | — |
| Debt issuance, net | 31.38 | 56.23 | +79% | — | — |
| Debt repayments | 18.40 | 5.25 | -71% | — | — |
| Common equity issued | 0.00 | **30.50** | — | — | — |
| Convertible preferred issued | 0.00 | **19.06** | — | — | — |
| Minority proceeds | 0.40 | 3.76 | +839% | — | — |
| Purchases of other investments | 2.31 | 22.05 | +854% | — | — |

**Interpretation:**

- **Operating cash flow is genuinely strong (+32.8%)**, growing faster than revenue and faster than operating income. That rules out receivables games or working-capital stuffing as the driver of earnings — CFO quality is good.
- **Capex is the entire story.** At $80.6B in H1, capex consumed **95% of operating cash flow**; in Q2 it exceeded CFO ($44.9B vs. $39.1B), producing Alphabet's first negative FCF quarter in the dataset. Critically, **capex incurred but not yet paid jumped to $29.1B from $10.6B**, meaning cash capex in Q3 will likely exceed even the Q2 cash number. If Q2's ~$45B/quarter pace holds, FY2026 capex annualizes near **$180B**; even a flat H2 at the H1 level implies **~$161B** for the full year.
- **The funding mix has inverted.** In H1 2025 Alphabet *returned* $33B (buybacks + dividends) and funded itself from cash. In H1 2026 it *raised* ~$109B of external capital (debt + common + preferred + minority) and returned only $5.2B. **Buybacks at exactly $0 vs. $28.3B is the clearest signal management is capital-constrained relative to its investment ambitions.**
- **Share count still rose 1.17%** to 12.230B despite zero buybacks, driven by $30.5B of equity issuance (implies roughly **$215/share average issuance price** on the 142M share increase — a useful market-price anchor) and $15.2B of SBC. Net dilution is running at a low-single-digit annual rate.
- **The $22.05B of "other investments" purchases** (vs. $2.31B) explains part of the balance-sheet expansion and is separate from capex — this is portfolio/AI-ecosystem investing, and it consumes real cash.

---

## 7. Multi-Year History (as available)

Where the vendor provided earlier periods:

| $B | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|
| Financing cash flow | (72.09) | (79.73) | (37.39) | **+86.32** |
| Capex incurred but not yet paid (year-end) | 7.44 | 10.33 | 15.09 | 29.11 (6/30) |
| Finance lease principal payments | 0.71 | 0.41 | 1.99 | 0.84 |

The trajectory is stark: from **-$72B to -$80B of annual cash returned/financed** in 2023–2024, to **-$37B** in 2025 as the build began, to **+$86B of net capital raised** in H1 2026. Capex accruals have compounded at roughly 42% per year for three years. **This is a multi-year, deliberate transformation of the business model's capital intensity — not a one-quarter aberration.** It argues that FCF margins should be modeled structurally lower for as long as the AI build lasts, and that the "cash machine" valuation premium GOOGL historically commanded deserves to be re-examined.

Full-year 2023/2024/2025 income-statement data was not returned by the vendor, so multi-year revenue and EPS CAGR cannot be computed here without fabrication.

---

## 8. Liquidity, Leverage & Solvency

- **Liquidity:** $242.5B cash + short-term investments; $343.5B current assets. Even a full year of $180B capex is coverable without new financing, though management is clearly choosing to pre-fund.
- **Leverage:** gross debt $101.1B against ~$141B net cash. Net leverage is *negative*. Interest coverage is enormous (H1 operating income $80.5B vs. interest $1.8B = ~44x). Even on core earnings, solvency risk is negligible.
- **Refinancing risk:** low, given the cash pile and the pre-2026 maturity ladder being long-dated. But the *rate* on new debt is clearly higher than the legacy book — interest expense up 5x on a 2x debt increase implies a materially higher average coupon.
- **Off-balance-sheet/commitments:** operating lease payments of $21.3B undiscounted (liability $18.0B), finance leases $2.9B undiscounted, plus purchase commitments for compute not itemized in the returned data. The lease liability grew only 13%, so the AI build is largely owned PP&E, not leased.
- **Equity composition:** $18.0B convertible preferred, $131.4B common+APIC, AOCI -$2.3B, and an unknown retained-earnings balance (not returned). Book equity is not derivable in full from the returned data; do not quote a P/B.

---

## 9. Insider Activity

**Not available.** The vendor explicitly reports no authorized point-in-time insider-transactions archive for GOOGL as of 2026-09-09. No conclusion — positive or negative — should be drawn from insider behavior in this report. Any statement about insider buying or selling would be fabricated.

---

## 10. Actionable Insights for Traders

**1. Underwrite the operating business, not the GAAP tape.**
H1 GAAP EPS $14.24 vs. core EPS ~$5.37. Operating income +30%, revenue +24%, gross margin +240bp. The operating franchise is accelerating and margin-expanding *despite* a 43% depreciation increase. If you screen on reported P/E you will conclude GOOGL is far cheaper than it is; if you screen on core P/E you get a normal, fairly-valued mega-cap grower with an unusual capex overhang. **Trade the core number.**

**2. The FCF inflection is the catalyst — watch Q3 capex, not Q3 revenue.**
Q2 FCF was **-$5.9B**, and $29.1B of capex was incurred but unpaid at quarter-end, implying Q3 cash capex likely ≥ Q2. Bull case: capex plateaus in H2, CFO grows ~15%, FCF re-enters positive and the "AI spend is over" narrative flips. Bear case: capex steps up again toward $50B/quarter and FCF stays negative for multiple quarters, forcing more debt/equity and compressing the multiple. **Position sizing should be driven by management's capex commentary, not the revenue print.**

**3. Expect a valuation-quality de-rating risk from the $124B of marked-up private equity stakes.**
Equity securities without readily determinable FV nearly doubled to $124.3B, supported by $85.7B of cumulative upward marks and a $22.8B DTL. Q2 alone contributed $99B of FV gains. This asset is illiquid, model-marked, and can reverse violently. A private-market valuation reset would hit GAAP EPS hard and could force a DTL reversal — a headline-risk event with no cash impact but real multiple implications. **Treat any quarter with a large non-operating gain as lower-quality, and any large non-operating loss as a buying opportunity in the core business.**

**4. Zero buybacks removes a technical bid; dilution is now a headwind.**
Buybacks went from $28.3B (H1 2025) to $0, while the company issued $30.5B of common stock and $19.1B of convertible preferred and ran $15.2B of SBC. Share count rose 1.17% in six months. For a stock that historically relied on aggressive repurchase as a support mechanism, this is a meaningful change in the supply/demand balance. **A resumption of buybacks would be a strong positive signal; continued zero buybacks alongside further equity issuance should be read as a management signal that capital is fully committed to capex.**

**5. Balance-sheet strength is the downside cushion.**
~$141B net cash (~$123B after preferred), 44x interest coverage, $242B of liquid assets. This is not a solvency story. In a drawdown, GOOGL's balance sheet argues for buying weakness rather than avoiding it — the risk is multiple compression, not impairment.

**6. Model a 19% tax rate and a rising depreciation curve.**
The tax rate moved +200bp to 19.1% (a ~$4.3B H1 headwind), and depreciation is +43% with capex at 6x depreciation. The margin expansion achieved in H1 was *despite* these drags; as depreciation catches up over 2027–2028, gross margin could compress unless AI revenue scales proportionally. **The durability of the 62% gross margin is the key medium-term test of whether this capex cycle earns its cost of capital.**

**7. Positive leading indicators worth weighting.**
Deferred revenue +17.4% to $10.1B; accrued liabilities +31% and AP +66% (consistent with a company scrambling to build); AR growing slower than revenue; allowance ratio stable. These support the "demand is real" side of the debate.

**8. Legal overhang.**
Loss contingency accruals of $17.4B (+11% in six months), with $3.0B paid out in a single prior quarter. Not thesis-changing at this balance-sheet size, but a source of episodic headline risk.

### Suggested monitoring checklist for the next 90 days
- Q3 2026 capex dollars and any change to full-year capex framing.
- Whether FCF turns positive; Q3 CFO vs. Q3 cash capex.
- Buyback authorization/resumption (currently zero).
- Further debt or equity issuance (would signal capex is outrunning even this balance sheet).
- Depreciation growth rate vs. revenue growth (margin sustainability).
- Any reversal in equity-securities FV gains and the associated DTL.
- Deferred revenue and Cloud backlog indicators.

---

## 11. Summary Table — Key Fundamentals at a Glance

| Category | Metric | Value / Observation | Signal |
|---|---|---|---|
| **Scale** | H1 2026 revenue (derived) | $229.69B, +23.1% YoY | Positive |
| | Q2 2026 revenue (derived) | $119.80B, +24.2% YoY (accel. from +21.8% in Q1) | **Strongly positive** |
| **Profitability** | H1 gross margin | 62.0%, +240bp YoY | Positive |
| | H1 operating income | $80.47B, +30.0%; margin 35.0% (+190bp) | **Strongly positive** |
| | Q2 operating income | $40.77B, +30.4%; margin 34.0% | Positive |
| **Earnings quality** | H1 GAAP diluted EPS | $14.24 (incl. ~$135.7B non-op gains) | **Low quality — do not screen on it** |
| | H1 core EPS (est., ex-FV gains) | ~$5.37, +~24.5% YoY | Positive, in line with operations |
| | Equity securities FVNI gains | $135.95B H1, $99.03B Q2, mostly unrealized | Volatile, non-cash |
| **Costs** | SBC | $15.20B H1 (+32.2%); 6.6% of revenue | Negative (dilution) |
| | Depreciation | $13.59B H1 (+43.2%); capex ~6x depreciation | Rising drag |
| | Interest expense | $1.81B H1 (+514%); net interest income fell to ~$1.0B | Negative |
| | Effective tax rate | 19.1% vs. 17.1% (+200bp) | Negative |
| **Cash flow** | H1 operating cash flow | $84.86B, +32.8% | **Strongly positive** |
| | H1 capex | $80.60B, +103.3%; 35.1% of revenue | **The central risk** |
| | H1 free cash flow | $4.26B, -82.4% | **Negative** |
| | Q2 2026 free cash flow | **-$5.86B** (first negative quarter in dataset) | **Negative** |
| | Capex incurred but unpaid | $29.11B (vs. $10.64B) | Q3 cash capex likely higher |
| **Balance sheet** | Cash + short-term investments | $242.47B (from $126.84B) | Positive |
| | Total debt | $101.09B (from $49.09B, +106%) | Negative direction |
| | Net cash | ~$141.4B (~$123.4B incl. preferred as quasi-debt) | **Positive / fortress** |
| | Total assets | $921.98B (from $595.28B, +54.9% in 6 months) | Reflects capital intensity |
| | Convertible preferred issued | $18.02B carrying ($19.0B gross, June 2026) | Dilution overhang |
| | Deferred tax liabilities | $22.82B (from $0.92B) | Tied to FV marks |
| | Deferred revenue | $10.10B, +17.4% | Positive leading indicator |
| | Loss contingency accrual | $17.36B, +11% | Legal overhang |
| | Equity securities w/o readily det. FV | $124.26B (from $64.09B) | Illiquid, marked-up |
| **Capital allocation** | Buybacks H1 2026 | **$0** (vs. $28.31B H1 2025) | **Signal: capital fully committed** |
| | Dividends H1 2026 | $5.23B; DPS $0.43 (+4.9%) | Stable, low payout |
| | Common equity issued H1 2026 | $30.50B (implies ~$215/sh) | Dilution, but validates price |
| | Debt issued / repaid H1 2026 | +$56.23B / -$5.25B | Leverage rising |
| | Minority proceeds | $3.76B (+839%) | Funding diversification |
| **Shares** | Shares outstanding | 12.230B (from 12.088B), +1.17% in 6 months | Net dilution |
| | Diluted EPS (Q2) | $9.11 vs. $2.31 | Inflated by marks |
| **Insider activity** | — | **DATA UNAVAILABLE — not inferred** | No signal |
| **Valuation** | Market cap / P/E / EV | **Not provided by vendor — no multiple asserted** | — |
| **Overall** | — | Excellent operating momentum + fortress balance sheet, offset by negative FCF, zero buybacks, rising leverage, and inflated GAAP EPS | **Constructive on business; cautious on cash-flow/valuation optics** |

---

*Prepared from point-in-time SEC XBRL facts public as of 2026-09-09: Q2 2026 Form 10-Q (accepted 2026-07-23, accession 0001652044-26-000071) and FY2025 Form 10-K (accepted 2026-02-05, accession 0001652044-26-000018). Revenue and gross profit are derived from reported cost and operating-income lines. No market-price, valuation, segment, or insider data was available and none has been estimated beyond the explicitly labeled core-EPS and net-cash calculations.*