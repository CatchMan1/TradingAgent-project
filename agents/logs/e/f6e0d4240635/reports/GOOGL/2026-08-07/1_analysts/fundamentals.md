# GOOGL — Alphabet Inc. | Fundamental Deep-Dive (point-in-time as of 2026‑08‑07)

**Latest filing in the data set:** Form 10‑Q for the period ended **2026‑06‑30**, EDGAR acceptance **2026‑07‑23 01:15:54 UTC** (accn 0001652044‑26‑000071).
**Prior filing:** 10‑Q for period ended 2026‑03‑31, accepted **2026‑04‑30**; **10‑K for FY2025**, accepted **2026‑02‑05**.

> **Data provenance note:** everything below is derived from the point-in-time SEC-fact extract supplied by the tools. Income-statement, balance-sheet and cash-flow pulls returned the same tag window regardless of `freq`; several tags (revenue by segment, goodwill, total liabilities, retained earnings, S&M and R&D lines) fall outside the returned window. Where I had to **derive** a figure (notably revenue), I show the arithmetic and label it **[derived]**. Nothing here is inferred from outside the tool data except where explicitly marked *[background]*.
>
> **Insider transactions: NOT AVAILABLE.** The vendor returned `DATA_UNAVAILABLE: the B-project data package has no authorized, point-in-time insider-transactions archive for GOOGL by 2026-08-07.` **No insider buying/selling is reported or inferred in this note.** Treat insider flow as an open data gap and source it separately before acting.

---

## 1. Bottom line (what matters for a trade today)

1. **Top line re-accelerated hard.** Q2 2026 revenue **$119.8B, +24.2% y/y** [derived]; H1 2026 **$229.7B, +23.1% y/y** [derived]. That is the strongest growth profile in the visible history and is the single most important fundamental datapoint in this filing.
2. **Operating leverage is real but modest, and the tax rate ate part of it.** Q2 operating margin **34.0%** (vs 32.4%), H1 **35.0%** (vs 33.1%); operating income **+30.4% y/y** in Q2. But the effective tax rate stepped up to **19.1%** from **17.1%**, so **"core" EPS growth is ~+24%**, roughly in line with revenue — not above it.
3. **The reported GAAP numbers are heavily distorted by a non-cash investment revaluation.** H1 2026 includes **$135.8B of pre-tax debt/equity-securities gains** (equity FV-NI gain $135.9B), driving GAAP H1 EPS of **$14.24** and Q2 EPS of **$9.11**. Strip those out and **core H1 EPS is ≈$5.37** and **Q2 ≈$2.69** (my derivation). **Do not screen GOOGL on the reported $9.11/"$36 annualized" EPS.**
4. **Free cash flow has inverted — this is the bear case, and it is now a fact, not a forecast.** H1 2026 capex **$80.6B** (+103% y/y) vs CFO **$84.9B** → **H1 FCF ≈ $4.3B** (vs $24.2B in H1 2025). On a standalone Q2 basis, **capex $44.9B exceeded CFO $39.1B → Q2 FCF ≈ –$5.9B [derived]**.
5. **Capital allocation flipped from returning cash to raising it.** H1 2026: **buybacks $0** (vs $28.3B in H1 2025), **+$56.2B debt issued**, **+$30.5B common stock issued**, **+$19.1B convertible preferred issued (5 Jun 2026)**, **+$3.8B minority proceeds**, dividends paid $5.2B. Share count rose to **12,230M from 12,088M** (+1.2% in six months). Interest expense **+514% y/y** (H1 $1.81B vs $0.30B).
6. **Balance sheet is still a fortress, but the direction of travel matters.** Cash + short-term investments **$242.5B** vs debt carrying **$101.1B** + finance leases $2.6B → **≈$139B net cash**. Total assets **$922.0B, +55% in six months** (from $595.3B), including non-marketable equity securities **$124.3B** (from $64.1B) and finite-lived intangibles **$10.6B** (from $2.5B, suggesting an ~$8B intangible acquisition — goodwill is outside the returned window and cannot be confirmed).

**Net read:** a genuine demand acceleration funding an unprecedented AI capex cycle out of debt, equity and asset markups rather than out of cash flow. The equity story has migrated from "margin expansion + buyback" to **"growth + balance-sheet capacity + investment NAV."** That reprices the stock on capex-conversion and asset value, not on FCF yield.

---

## 2. Company profile and instrument identity

- **Issuer / ticker:** Alphabet Inc. — **GOOGL** (Class A common; Class B and Class C outstanding in a triple-class structure). Authorized shares **300,000,000,000**, par **$0.001**.
- **Shares outstanding:** **12,230M** at 2026‑06‑30 vs **12,088M** at 2025‑12‑31 (issued = outstanding; no treasury disclosure in window).
- **Business (background, not from the tools):** Google Services (Search, YouTube, Android, Chrome, Play, devices, subscriptions/platforms), Google Cloud, and Other Bets (Waymo, Verily, etc.). **Segment-level revenue is not present in the returned tag window** — I cannot quantify Cloud vs Search vs YouTube mix from this extract, and I will not guess it.
- **Capital return:** quarterly dividend declared **$0.22** (Q2 2026) vs **$0.21** (Q2 2025); H1 declared **$0.43** vs **$0.41** (+4.9%). Ordinary dividends paid H1 2026 **$5.231B**; preferred dividends **$86M** (one partial quarter, post-issuance).

---

## 3. Income statement — Q2 and H1 2026

**Revenue is derived** as `CostsAndExpenses + OperatingIncomeLoss` (Alphabet's presentation: Revenues − Costs and expenses = Operating income). This method reproduces the known Q2 2025 figure exactly ($65,157 + $31,271 = $96,428M), which validates it.

| $M unless noted | Q2 2026 | Q2 2025 | y/y | H1 2026 | H1 2025 | y/y |
|---|---:|---:|---:|---:|---:|---:|
| Revenue **[derived]** | **119,796** | 96,428 | **+24.2%** | **229,692** | 186,662 | **+23.1%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| Gross profit **[derived]** | 73,853 | 57,389 | +28.7% | 142,478 | 111,262 | +28.1% |
| **Gross margin** | **61.6%** | 59.5% | +2.1 pt | **62.0%** | 59.6% | +2.4 pt |
| G&A | 6,461 | 5,209 | +24.0% | 10,752 | 8,748 | +22.9% |
| R&D + S&M (combined) **[derived]** | 26,622 | 20,909 | +27.3% | 51,260 | 40,637 | +26.1% |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 149,226 | 124,785 | +19.6% |
| **Operating income** | **40,770** | 31,271 | **+30.4%** | **80,466** | 61,877 | **+30.0%** |
| **Operating margin** | **34.0%** | 32.4% | +1.6 pt | **35.0%** | 33.1% | +1.9 pt |
| Interest income | 1,430 | 1,050 | +36.2% | 2,811 | 2,051 | +37.1% |
| Interest expense | (1,278) | (261) | +390% | (1,811) | (295) | **+514%** |
| Equity securities FV‑NI gain | 99,031 | 1,286 | n.m. | 135,946 | 11,044 | n.m. |
| Debt & equity securities gain (total) | — | — | — | 135,803 | 11,411 | n.m. |
| Non-operating income, net | 97,983 | 2,662 | n.m. | 135,699 | 13,845 | n.m. |
| Pre-tax income | 138,753 | 33,933 | +309% | 216,165 | 75,722 | +185% |
| Income tax | 26,560 | 5,737 | +363% | 41,394 | 12,986 | +219% |
| **Effective tax rate** | **19.1%** | 16.9% | +2.2 pt | **19.1%** | 17.1% | +2.0 pt |
| **Net income** | **112,193** | 28,196 | +298% | **174,771** | 62,736 | +179% |
| Net income to common | 112,107 | 28,196 | +298% | 174,685 | 62,736 | +178% |
| **Diluted EPS** | **$9.11** | $2.31 | +294% | **$14.24** | $5.12 | +178% |
| Basic EPS | $9.23 | $2.33 | — | $14.41 | $5.16 | — |
| Diluted shares (implied) | ~12,306M | ~12,206M | +0.8% | ~12,267M | ~12,253M | +0.1% |
| **SBC expense** | **8,000** | 6,000 | **+33.3%** | **15,200** | 11,500 | **+32.2%** |
| SBC % of revenue | 6.7% | 6.2% | +0.5 pt | 6.6% | 6.2% | +0.4 pt |

Also derived (Q1 2026, from H1 less Q2): revenue **$109.9B (+21.8%)**, operating income **$39.7B (+29.7%)**, operating margin **36.1%** (vs 33.9%), GAAP diluted EPS **$5.13** vs $2.81.

**Interpretation**
- **Gross margin is expanding (+2.4 pt in H1)** even as cost of revenue grows 16% — the AI/cloud mix and efficiency story is showing up in the gross line. Commentary that margins would compress from AI compute is, so far, not visible here.
- **Opex discipline is decent but not exceptional:** combined R&D + S&M +$10.6B (+26%) is *faster* than revenue (+23%). G&A +23%. So the entire margin gain comes from the **gross line**, not from opex leverage.
- **SBC +32% y/y, 6.6% of revenue** — a real economic cost and a dilution vector that non-GAAP presentations strip out.

---

## 4. Earnings quality: reported vs "core"

The H1 2026 P&L is contaminated by a very large, non-cash investment revaluation. My estimate of "core" (operating) earnings excludes securities gains but retains net interest:

| $M unless noted | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---:|---:|---:|---:|
| Operating income | 40,770 | 31,271 | 80,466 | 61,877 |
| + net interest income | 152 | 789 | 1,000 | 1,756 |
| Core pre-tax **[derived]** | 40,922 | 32,060 | 81,466 | 63,633 |
| Tax at reported ETR | 19.1% / 16.9% | | 19.1% / 17.1% | |
| Core net income **[derived]** | 33,106 | 26,642 | 65,905 | 52,752 |
| Diluted shares | ~12,306M | ~12,206M | ~12,267M | ~12,253M |
| **Core diluted EPS [derived]** | **≈$2.69** | **≈$2.18** | **≈$5.37** | **≈$4.31** |
| **Core EPS growth** | **+23.2%** | | **+24.6%** | |
| Reported diluted EPS | $9.11 | $2.31 | $14.24 | $5.12 |
| **Reported ÷ core (inflation factor)** | **3.4×** | 1.06× | **2.7×** | 1.19× |

**Why this matters:** any screener, chart, or "P/E" built on reported EPS is showing GOOGL at roughly **one third** of its true earnings multiple. Conversely, momentum screeners reading "+294% EPS growth" are reading a mark-to-market, not a business.

**Composition of the gain — and a flag:** the reported tags do not fully reconcile. H1 2026 equity FV‑NI gain is **$135.9B**, but disclosed sub-components are only **$21.5B unrealized + $0.8B realized**, and the balance-sheet carrying value of non-marketable equity securities rose only **$60.2B** (to $124.3B) with cumulative *upward* fair-value adjustments rising **$41.2B** (to $85.7B) against $22.1B of purchases. In other words, **the bulk of the gain sits outside the disclosed realized/unrealized split** — very likely measurement-alternative (observable-price) adjustments on non-marketable holdings. **A trader should confirm the composition in the 10‑Q notes before underwriting any NAV-based thesis on the $124.3B non-marketable book.**

**Accrual quality (core basis):** CFO $84.9B ÷ core net income $65.9B = **1.29×** — healthy cash conversion of operating earnings. (On a reported basis it looks terrible, 0.49×, purely because of the non-cash gain.)

---

## 5. Balance sheet

| $M | 2026‑06‑30 | 2025‑12‑31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| Cash + short-term investments | **242,474** | 126,843 | **+91.2%** |
| Available-for-sale debt securities | 99,500 | n/a | — |
| Accounts receivable, net | 69,175 | 62,886 | +10.0% |
| Current assets | **343,524** | 206,038 | +66.7% |
| **Total assets** | **921,983** | 595,281 | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| Employee-related liabilities | 15,086 | 17,546 | –14.0% |
| Accrued income taxes, current | 5,233 | 523 | **+900%** |
| Accrued income taxes, noncurrent | 11,306 | 9,531 | +18.6% |
| Commercial paper | 0 | 0 | — |
| Deferred revenue (total) | 10,100 | 8,600 | +17.4% |
| **Debt carrying amount** | **101,085** | 49,085 | **+106.0%** |
| Finance lease liabilities | 2,590 | 2,500 | +3.6% |
| Operating lease liabilities | 18,037 | 15,954 | +13.1% |
| **Deferred income tax liabilities** | **22,819** | 919 | **+2,382%** |
| Legal / loss contingency accrual (current) | 17,356 | 15,594 | +11.3% |
| Derivative liabilities | 1,958 | 379 | +417% |
| Convertible preferred stock | **18,023** | 0 | new |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| AOCI | (2,285) | (1,916) | wider loss |
| Non-marketable equity securities | **124,259** | 64,094 | **+93.9%** |
| Finite-lived intangibles, gross | 10,585 | 2,467 | **+329%** |

**Key observations**
- **Liquidity is enormous:** $242.5B cash + ST investments, of which $99.5B is AFS debt securities (maturity ladder: $16.7B <1yr, $50.9B 1–5yr, $15.3B 5–10yr, $16.6B >10yr). Unrealized loss position **$53.2B carrying / $416M accumulated loss** — a mark-to-market drag if rates rise, but immaterial relative to equity.
- **Net cash ≈ $139B** (242.5 minus 101.1 debt and 2.6 finance leases), or **≈$128B** if the $19.0B preferred is treated as debt-like. **Still net cash, but leverage doubled in six months.**
- **The $22.8B deferred tax liability is the tax bill waiting on the investment gains.** Any monetization of stakes triggers cash tax; conversely, unwinding marks would release it. This is a real, disclosed offset to "asset value" bulls.
- **Legal accruals of $17.4B** (up $1.8B) plus a $3.0B contingency payment disclosed in the FY2025 10‑K — regulatory/antitrust overhang remains a live line item, not a tail risk.
- **Asset growth of $327B in two quarters is not organic operating growth.** Visible drivers: the capital raise (~$106B of debt/equity/preferred), $174.8B of net income (of which ~$136B pre-tax non-cash marks), $80.6B of capex, and ~$8B of acquired intangibles. Goodwill is outside the returned window — **confirm whether a business combination occurred.**
- Working capital: AP +66% and accrued liabilities +31% outpace AR +10% — consistent with a capex/payables build rather than receivables stuffing. Receivables allowance only $995M on $69.2B AR (1.4%) — no credit deterioration signal.

---

## 6. Cash flow — the capex supercycle and the financing pivot

| $M | H1 2026 | H1 2025 | y/y | Q2 2026 [derived] | Q1 2026 |
|---|---:|---:|---:|---:|---:|
| **Operating cash flow** | **84,859** | 63,897 | **+32.8%** | 39,069 | 45,790 |
| Purchases of PP&E (capex) | **(80,598)** | (39,643) | **+103.3%** | (44,924) | (35,674) |
| **Free cash flow [derived]** | **≈4,261** | 24,254 | **–82.4%** | **≈(5,855)** | 10,116 |
| Purchases of marketable securities | (76,480) | (39,870) | +91.8% | — | (31,041) |
| Sales/maturities of marketable securities | 66,696 | 40,930 | +62.9% | — | 38,001 |
| Purchases of other investments | (22,051) | (2,312) | +854% | — | (906) |
| **Investing cash flow** | **(145,822)** | (40,738) | +258% | — | (63,389) |
| Debt issued, net of costs | **56,226** | 31,378 | +79.2% | — | 31,379 |
| Common stock issued | **30,499** | 0 | n.m. | — | 0 |
| **Convertible preferred issued** | **19,063** | 0 | n.m. | — | 0 |
| Minority interest proceeds | 3,758 | 400 | +840% | — | 3,200 |
| Ordinary dividends paid | (5,231) | (4,977) | +5.1% | — | (2,542) |
| **Share repurchases** | **0** | (28,306) | **–100%** | — | **0** |
| Debt & lease repayments | (5,253) | (18,397) | –71.4% | — | (1,477) |
| Finance lease principal | (840) | (302) | +178% | — | (522) |
| **Financing cash flow** | **+86,320** | (26,033) | n.m. | — | +25,077 |
| FX effect on cash | (154) | 444 | — | — | — |
| **Net change in cash** | **+25,203** | (2,430) | n.m. | — | — |

Non-cash / supplemental:
- **Depreciation H1 2026 $13,586M vs $9,485M (+43.2%)** — the depreciation wave from prior capex is arriving and will keep building.
- Amortization of intangibles **$545M vs $246M**; finance-lease ROU amortization **$485M vs $208M**.
- **Capex incurred but not yet paid: $29,113M** at 6/30/26 vs $10,635M a year earlier (FY2025 full-year: $15,090M). This is contracted but unpaid spend — **it mechanically depresses near-term reported FCF even at flat run-rate capex** and implies the capex number keeps going up.
- FY2025 10‑K anchors: financing outflow **–$37.4B (FY25)** vs **–$79.7B (FY24)** and **–$72.1B (FY23)**; finance lease principal payments $0.71B / $0.41B / $1.99B for FY23/24/25.

**Interpretation for traders**
- **The FCF narrative has broken.** H1 FCF $4.3B on $229.7B of revenue = **1.9% FCF margin**, versus 13.0% a year ago. Q2 was outright negative. At the H1 capex run-rate (~$161B annualized, and Q2 annualizes to ~$180B), **FY2026 FCF is likely to be negligible or negative unless CFO keeps compounding at 30%+.** Any model anchored on historical FCF multiples is wrong for this regime.
- **Funding is now explicit and external:** $56.2B new debt + $30.5B equity + $19.1B convertible preferred + $3.8B minority = **~$110B raised in six months**, with buybacks cut to zero. This is a classic late-cycle-capex-capital-structure signal: **dilution and interest cost in exchange for capacity.**
- **CFO is holding up (+32.8%)** despite working-capital drags, driven by core profitability plus non-cash addbacks. Note the tax line: `IncreaseDecreaseInIncomeTaxes +$8.3B` was a cash *use*.

---

## 7. What changed in this week's/this filing's information set

| Item | Prior signal | Current signal | Direction |
|---|---|---|---|
| Revenue growth | ~+22% (Q1'26) | **+24.2% (Q2'26)** | Improving |
| Operating margin | 33.9% (Q1'25) | **34.0% Q2 / 36.1% Q1'26** | Improving |
| Effective tax rate | 17.1% (H1'25) | **19.1% (H1'26)** | Negative for EPS |
| Capex intensity | $39.6B/H1'25 | **$80.6B/H1'26 (+103%)** | Major negative for FCF |
| FCF | $24.3B H1'25 | **$4.3B H1'26** | Major negative |
| Buybacks | $28.3B H1'25 | **$0** | Negative for EPS/support |
| Debt | $49.1B | **$101.1B** | Leverage up |
| Share count | 12,088M | **12,230M** | Dilutive |
| Investment marks | $64.1B non-marketable | **$124.3B + $135.8B P&L gain** | Huge NAV uplift, no cash |
| Depreciation | $9.5B H1'25 | **$13.6B H1'26** | Margin headwind ahead |
| Dividend | $0.21/qtr | **$0.22/qtr (+4.8%)** | Modestly positive |

---

## 8. Actionable insights

**Bull thesis (data-supported)**
- **Demand is accelerating, not decelerating:** +24.2% y/y in Q2 with **gross margin up 210bp**. If the Q2 run-rate holds, revenue annualizes above **$475B**. This is the strongest evidence in the filing.
- **Operating income is compounding at ~30% y/y** with the incremental margin accruing from the gross line — the AI/cloud monetization is landing above the cost curve so far.
- **$242.5B liquidity + ~$139B net cash** means the capex cycle is *pre-funded*, not liquidity-constrained. There is no solvency debate here; the debate is returns on capital.
- **$124.3B of non-marketable equity securities** (plus $99.5B AFS) is an under-appreciated call option on the AI ecosystem; cumulative upward adjustments of $85.7B show real marks, not just cost.
- **Tax/ETR normalization** and rising depreciation will be partly offset by interest income (+37%) on the enlarged cash pile.

**Bear thesis (data-supported)**
- **FCF ~zero, Q2 negative, and capex-incurred-not-paid of $29.1B means more outflow is already committed.** If CFO growth decelerates to ~15% while capex keeps compounding, FY2027 FCF stays structurally suppressed.
- **The reported earnings are 2.7×–3.4× core earnings.** Any de-rating catalyst that forces the market to re-anchor on core EPS is a mechanical headwind; conversely, if the marks reverse, GAAP EPS collapses.
- **Capital allocation regime change:** buyback to zero, $30.5B of share issuance (+1.2% count), $19.1B convertible preferred (an option-like overhang), interest expense +514%. This removes a decade-long EPS tailwind.
- **$22.8B deferred tax liability** stands between the asset marks and realized value.
- **$17.4B legal accrual** with $3.0B paid in Q3 FY2025 shows regulatory outcomes are cash events.

**Concrete trade construction ideas from this filing**
1. **Anchor valuation on core EPS, not GAAP.** Core H1 2026 ≈ **$5.37**; a ~$10.7 annualized core run-rate (before seasonality) is the honest denominator. Reported H1 $14.24 is not.
2. **Make FCF the swing factor.** Watch two lines each quarter: (a) `Purchases of PP&E` vs (b) `Operating cash flow`. Until CFO exceeds quarterly capex ($44.9B in Q2), the market must fund the capex with balance sheet and issuance — a structurally lower multiple than an FCF-funded model.
3. **Watch for a buyback resumption.** Zero repurchases with $55.9B of cash and a freshly raised $110B is a **deliberate signal**. A reinstated authorization would be an unambiguously bullish capital-allocation event; continued issuance would be the opposite.
4. **Watch the convertible-preferred terms.** $18.0B carrying value issued 5 Jun 2026 — conversion price and dividend rate determine a real EPS dilution path (preferred dividends currently only $86M, one month). Get the terms before sizing.
5. **Watch the deferred tax liability ($22.8B).** A monetization of stakes (secondary sale/IPO lockup) converts NAV into cash but triggers tax; a step-down in DTL from a mark reversal would be the tell that the $135.8B gain is unwinding.
6. **Watch depreciation.** +43% y/y in H1 with $80.6B of H1 capex and $29.1B unpaid means D&A likely compounds 30–40% through 2027 — a direct gross-margin headwind that must be outpaced by revenue.
7. **Do not act on insider flow** — the data is unavailable in this environment; sourcing it elsewhere is a prerequisite for any conviction trade that depends on management signaling.

**Risk checklist / falsifiers**
- Two consecutive quarters of revenue growth below ~15% would invalidate the demand-acceleration leg.
- Gross margin rolling over while capex keeps rising = the worst case (both numerator and denominator against you).
- Any large realized loss or write-down in the $124.3B non-marketable book (downward adjustments already $9.1B cumulative).
- Further equity/preferred issuance at scale → dilution spiral narrative.
- Dividend growth cut to flat (currently +4.8%) would signal capital discipline re-prioritization toward capex.

---

## 9. Data gaps and caveats (read before trading)

1. **Insider transactions: unavailable.** Vendor has no authorized point-in-time archive for GOOGL as of 2026‑08‑07. No inference made.
2. **Segment revenue (Search/YouTube/Cloud/Other Bets), R&D as a standalone line, S&M as a standalone line, goodwill, total liabilities, retained earnings, and total stockholders' equity are outside the returned tag window.** Revenue was **derived** (validated against Q2 2025), and R&D+S&M is a combined residual. Segment mix cannot be assessed from this extract.
3. **Cash-flow line items do not fully foot to reported subtotals** (investing items sum to ≈–$112.1B vs reported –$145.8B; financing items to ≈+$98.4B vs reported +$86.3B). The extract is incomplete — treat the itemization as directional and the subtotals as authoritative.
4. **The $135.8B H1 2026 securities gain does not reconcile to the disclosed sub-tags or to balance-sheet movement.** Confirm composition in the 10‑Q notes before using it for NAV work.
5. **No price data was available**, so no P/E, EV/EBITDA, or FCF-yield can be computed here. Provide core EPS ($5.37 H1) and GAAP EPS ($14.24 H1) levels to whoever does the multiple work.
6. All figures are **point-in-time** as of the EDGAR acceptance timestamps shown; the FY2025 10‑K figures used (capex-incurred-not-paid, lease schedules, FY financing flows) are the only full-year values present in the window.

---

## 10. Summary table — key points

| Category | Metric | Value | Signal / Takeaway |
|---|---|---|---|
| **Identity** | Ticker / issuer | **GOOGL** / Alphabet Inc. | Class A share of a triple-class structure |
| **Filing** | Latest | 10‑Q, period **2026‑06‑30**, accepted **2026‑07‑23** | Freshest data in window |
| **Growth** | Q2 2026 revenue **[derived]** | **$119.8B, +24.2% y/y** | **Acceleration — strongest in visible history** |
| **Growth** | H1 2026 revenue **[derived]** | **$229.7B, +23.1% y/y** | Broad-based scale-up |
| **Margins** | Q2 op. margin | **34.0%** (vs 32.4%) | +160bp of operating leverage |
| **Margins** | H1 gross margin | **62.0%** (vs 59.6%) | Entire margin gain comes from gross line |
| **Profit** | Q2 operating income | **$40.77B, +30.4% y/y** | Core engine compounding ~30% |
| **Profit** | H1 GAAP net income | **$174.8B** | Includes **$135.8B pre-tax securities gains** |
| **Quality** | Reported vs core EPS (H1) | **$14.24 vs ≈$5.37** | Reported EPS is **2.7× core**; don't screen on it |
| **Quality** | Q2 EPS reported vs core | **$9.11 vs ≈$2.69** | **3.4× inflation** |
| **Quality** | Core EPS growth (H1) | **≈+24.6%** | In line with revenue; tax rate offset the margin gain |
| **Tax** | Effective tax rate | **19.1%** (from 17.1%) | –2pt EPS headwind |
| **Cash flow** | H1 operating cash flow | **$84.9B, +32.8%** | Healthy |
| **Cash flow** | H1 capex | **$80.6B, +103%** | **Doubled y/y** |
| **Cash flow** | H1 free cash flow **[derived]** | **≈$4.3B vs $24.3B** | **–82%; FCF margin 1.9%** |
| **Cash flow** | Q2 free cash flow **[derived]** | **≈–$5.9B** | **Capex > CFO in the quarter** |
| **Capex pipeline** | Capex incurred but not paid | **$29.1B** (vs $10.6B) | More outflow already committed |
| **Depreciation** | H1 depreciation | **$13.6B, +43.2%** | Rising D&A headwind into 2027 |
| **Capital return** | Buybacks H1 2026 | **$0** (vs $28.3B) | **Repurchase program halted** |
| **Capital return** | Dividend / quarter | **$0.22** (+4.8%) | Modest, sustained |
| **Financing** | Debt issued H1 2026 | **$56.2B** (net of costs) | Leverage doubled |
| **Financing** | Common stock issued | **$30.5B** | Dilution; shares +1.2% to 12,230M |
| **Financing** | Convertible preferred | **$19.1B issued 2026‑06‑05** | New $18.0B instrument — get conversion terms |
| **Financing** | Interest expense H1 | **$1.81B, +514%** | Cost of the new debt is arriving |
| **Balance sheet** | Cash + ST investments | **$242.5B** (+91%) | Massive liquidity buffer |
| **Balance sheet** | Total debt (carrying) | **$101.1B** (+106%) | Net cash **≈$139B** still |
| **Balance sheet** | Total assets | **$922.0B, +55% in 6M** | Capital raise + marks + capex |
| **Balance sheet** | Non-marketable equity securities | **$124.3B** (from $64.1B) | Large embedded NAV / call option |
| **Balance sheet** | Deferred tax liability | **$22.8B** (from $0.9B) | Tax bill on the marks |
| **Risk** | Legal/loss contingency accrual | **$17.4B** (+$1.8B) | Regulatory cash events continue |
| **Risk** | SBC expense H1 | **$15.2B, +32% (6.6% of revenue)** | Real cost; a dilution vector |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | **Do not infer — source elsewhere** |
| **Stance implied by data** | — | **Constructive on demand, cautious on FCF/capital allocation** | Own the growth and liquidity; demand proof that capex converts to FCF before paying an FCF-based multiple |