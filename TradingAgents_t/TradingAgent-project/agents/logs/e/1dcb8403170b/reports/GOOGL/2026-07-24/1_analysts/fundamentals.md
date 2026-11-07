# GOOGL (Alphabet Inc.) — Fundamental Deep-Dive Report
**Analysis date: 2026-07-24 | Latest filing vintage: Q2 2026 Form 10-Q, accepted 2026-07-23 (accn 0001652044-26-000071); FY2025 Form 10-K accepted 2026-02-05 (accn 0001652044-26-000018)**

---

## 0. Data scope, method, and caveats (read first)

**What I have:** point-in-time SEC XBRL facts for GOOGL, filtered by actual EDGAR acceptance timestamp, through the 10-Q filed **yesterday (2026-07-23)**. This means the Q2 2026 print is *one day old* — a fresh information window.

**What the vendor slice did not return (important):** the fact set I received is truncated alphabetically (~through "FiniteLivedIntangibleAssets"). Consequently I do **not** have: revenue tag lines (segment detail, Google Search/YouTube/Cloud/Other Bets), R&D and sales & marketing lines individually, PP&E/goodwill, retained earnings, total liabilities/equity lines, or full-year income-statement history. I have therefore **derived revenue** from `CostsAndExpenses + OperatingIncomeLoss` (a standard XBRL identity, and it reconciles exactly to reported prior-year revenue). I also could not obtain full balance-sheet line items, so several ratios below are labeled **estimated** with the build-up shown. **Insider-transaction data is explicitly unavailable** in this data package — I will not infer or fabricate insider activity.

**Derived revenue check:** Q2 2026 = 79,026 + 40,770 = **$119,796M**; Q2 2025 = 65,157 + 31,271 = **$96,428M** (matches actual reported Q2'25 revenue). Identity holds — derivation is reliable.

---

## 1. Headline: a blow-out optical quarter layered on a genuinely strong operating quarter — and a capital-allocation regime change

Alphabet's Q2 2026 results (quarter ended 2026-06-30, filed 2026-07-23) contain **three separate stories** that must be separated:

| Story | Magnitude | Character |
|---|---|---|
| ① Core operating acceleration | Revenue +24.2% y/y, operating margin 34.0% (+160bps), gross margin 61.7% (+220bps) | Genuine, cash-generating |
| ② Non-cash investment marks | $99.0B securities gain in one quarter; net income $112.2B; GAAP diluted EPS $9.11 | Optical, non-cash, non-recurring-quality |
| ③ Capital-structure transformation | Debt +$52.0B to $101.1B, $19.1B convertible preferred, $30.5B common issuance, **buybacks to zero**, H1 FCF −82% y/y | Structural, forward-looking, mixed |

**Core (ex-investment-gain) diluted EPS was ≈$2.61 in Q2 2026 vs ≈$2.22 in Q2 2025 (+17.5%) — not $9.11.** Any headline reaction to $9.11 vs. a consensus number built on operating EPS is mechanically mis-calibrated. This is the single most actionable observation in this report.

---

## 2. Company profile (context, not tool-sourced)

Alphabet Inc. (GOOGL = Class A shares; Class C = GOOG) is the parent of Google and is organized around **Google Services** (Search & other, YouTube ads, Network, subscriptions/devices/Play), **Google Cloud** (infrastructure + Workspace + AI/TPU), and **Other Bets** (incl. Waymo, Verily, Wing). Alphabet also holds one of the largest strategic equity-investment portfolios in tech (marketable stakes plus **non-marketable** private holdings — the balance sheet shows $124.3B of equity securities *without* readily determinable fair value, plus $99.5B of available-for-sale debt securities). Business model economics: near-zero marginal-cost ad auctions and subscription rails funding an increasingly capital-intensive AI compute, model, and cloud stack. *Business-mix revenue splits and segment margins could not be verified from this fact set and should be pulled from the 10-Q segment note.*

---

## 3. Income statement analysis

### 3.1 Q2 2026 vs Q2 2025 ($M, Apr–Jun)

| Line | Q2 2026 | Q2 2025 | Δ |
|---|---|---|---|
| Revenue (derived) | **119,796** | 96,428 | **+24.2%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% |
| Gross profit | 73,853 | 57,389 | +28.7% |
| Gross margin | **61.7%** | 59.5% | +220 bps |
| Opex ex-COGS (R&D+S&M+G&A) | 33,083 | 26,118 | +26.7% |
| of which G&A | 6,461 | 5,209 | +24.0% |
| Operating income | **40,770** | 31,271 | **+30.4%** |
| Operating margin | **34.0%** | 32.4% | +160 bps |
| Non-operating income | 97,983 | 2,662 | n/m |
| — equity securities gains, net | 99,031 | 1,286 | n/m |
| — interest income | 1,430 | 1,050 | +36.2% |
| — interest expense | (1,278) | (261) | +390% |
| Pre-tax income | 138,753 | 33,933 | +309% |
| Tax | 26,560 | 5,737 | — |
| Effective tax rate | **19.1%** | 16.9% | +220 bps |
| Net income | **112,193** | 28,196 | +298% |
| Net income to common | 112,107 | 28,196 | — |
| Diluted EPS | **$9.11** | $2.31 | +294% |
| Basic EPS | $9.23 | $2.33 | — |
| Diluted shares (implied) | ~12,306M | ~12,206M | +0.8% |
| SBC (allocated) | 8,000 | 6,000 | +33.3% |

### 3.2 H1 2026 vs H1 2025 ($M)

| Line | H1 2026 | H1 2025 | Δ |
|---|---|---|---|
| Revenue (derived) | **229,692** | 186,662 | **+23.1%** |
| Cost of revenue | 87,214 | 75,400 | +15.7% |
| Gross margin | 62.0% | 59.6% | +240 bps |
| Total costs & expenses | 149,226 | 124,785 | +19.6% |
| Operating income | **80,466** | 61,877 | **+30.0%** |
| Operating margin | **35.0%** | 33.1% | +190 bps |
| Non-operating income | 135,699 | 13,845 | +880% |
| Pre-tax income | 216,165 | 75,722 | +185% |
| Tax / ETR | 41,394 / **19.1%** | 12,986 / 17.1% | +200 bps |
| Net income | **174,771** | 62,736 | +179% |
| Diluted EPS | **$14.24** | $5.12 | +178% |
| SBC | 15,200 | 11,500 | +32.2% |
| D&A (depreciation + amort.) | 14,131 | 9,731 | +45.2% |
| Interest expense | 1,811 | 295 | +514% |

**Implied quarterly cadence (derived):**

| $M | Q1 2026 | Q2 2026 | Q1 2025 | Q2 2025 |
|---|---|---|---|---|
| Revenue | 109,896 | 119,796 | 90,234 | 96,428 |
| y/y growth | +21.8% | +24.2% | — | — |
| Operating income | 39,696 | 40,770 | 30,606 | 31,271 |
| Operating margin | 36.1% | 34.0% | 33.9% | 32.4% |
| Opex ex-COGS | 34,638 | 33,083 | 19,728 | 26,118 |
| y/y opex growth | **+75.6%** | +26.7% | — | — |

**Key inference:** Q1 2026 carried an anomalously large opex step-up (+75.6% y/y, roughly $14.9B above trend) yet *still* expanded operating margin to 36.1% on 21.8% revenue growth. That pattern is consistent with a large one-time charge inside "other" opex (legal accrual / settlement / restructuring) that revenue growth simply overwhelmed. Q2 normalized back to +26.7%. **Traders should confirm the Q1 anomaly in the 10-Q MD&A before annualizing margins** — if it was a one-off, underlying margin power is ~35–36%, i.e., better than the 35.0% H1 print.

### 3.3 Quality-of-earnings: separating the $99B mark

| Q2 2026 bridge ($M) | |
|---|---|
| Operating income | 40,770 |
| + interest income | 1,430 |
| − interest expense | (1,278) |
| ± other non-operating | (1,200) |
| **= pre-tax ex-securities gains** | **39,722** |
| × (1 − 19.1%) | **≈32,135 net** |
| ÷ diluted shares 12,306M | **≈$2.61 core EPS** |

- Q2 2025 core EPS ≈ **$2.22** (pre-tax 33,933 − 1,286 = 32,647, taxed at 16.9%). **Core growth = +17.5%.**
- H1 2026 core EPS ≈ **$5.30** vs H1 2025 ≈ **$4.35** → **+21.9%**.
- **96% of Q2 2026 pre-tax income (99,031 / 138,753 = 71%... of pre-tax; and $99.0B of $112.2B, or 88% of net income) came from non-operating investment marks.** That is the definition of a low-quality headline.

**Composition of the $99.0B Q2 gain (decomposition):**

| Component | Q2 2026 | H1 2026 |
|---|---|---|
| Total equity securities FV-NI gain | 99,031 | 135,946 |
| — unrealized (marketable) | 21,399 | 21,531 |
| — realized | 278 | 836 |
| — residual (private/non-marketable upward adjustments & related) | **~77,354** | **~113,579** |
| "Debt and equity securities gain, net" (income stmt) | — | 135,803 |
| Increase in *cumulative* upward FV adjustment on non-marketable equity | — | **+41,247** (44,485 → 85,732) |

The residual (~$77B in Q2) is larger than the observed change in the cumulative upward-adjustment balance (+$41.2B in H1). **This gap must be resolved from the 10-Q equity-securities note** — it likely reflects an observable-price/IPO-type event on a previously non-marketable holding, or a migration of holdings between measurement categories. Practically: *there is a specific private asset that re-rated by tens of billions in Q2 2026.* Identifying it is the highest-value research task on this name right now, because it determines whether marks are repeatable, already exhausted, or reversible.

**Deferred-tax smoking gun:** net deferred tax liabilities exploded from **$919M (12/31/25) → $22,819M (6/30/26)** and ETR rose to 19.1%. Alphabet booked ~$22B of future tax on these unrealized marks. Translation: **the gains are unrealized; the tax is largely non-cash today but is a real future claim**, and the ETR will stay elevated (~19%) while mark activity persists.

---

## 4. Balance sheet: from net-cash fortress to levered AI platform

### 4.1 Balance-sheet snapshot ($M)

| Item | 2026-06-30 | 2025-12-31 | Δ |
|---|---|---|---|
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| **Cash + short-term investments** | **242,474** | 126,843 | **+91.2%** |
| Available-for-sale debt securities | 99,500 | n/a | — |
| Equity securities w/o readily determinable FV (private) | **124,259** | 64,094 | **+93.9%** |
| — cumulative upward adjustments | 85,732 | 44,485 | +41,247 |
| — cumulative downward adjustments | (9,115) | (8,820) | −295 |
| Accounts receivable, net | 69,175 | 62,886 | +10.0% |
| Allowance for doubtful accounts | 995 | 924 | — |
| Total current assets | 343,524 | 206,038 | +66.7% |
| **Total assets** | **921,983** | 595,281 | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| Employee-related liabilities | 15,086 | 17,546 | −14.0% |
| Accrued income taxes (current / noncurrent) | 5,233 / 11,306 | 523 / 9,531 | n/m |
| Contract liabilities (total / current) | 10,100 / 7,154 | 8,600 / 6,578 | +17.5% |
| **Total debt (carrying)** | **101,085** | 49,085 | **+106.0%** |
| Operating lease liabilities | 18,037 | 15,954 | +13.1% |
| Finance lease liabilities | 2,590 | 2,500 | +3.6% |
| Net deferred tax liabilities | 22,819 | 919 | +2,383% |
| Litigation/loss contingency accrual (current) | **17,356** | 15,594 | +11.3% |
| Convertible preferred (non-redeemable) | **18,023** | 0 | new |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| AOCI | (2,285) | (1,916) | — |
| Shares outstanding | **12,230M** | 12,088M | **+1.18%** |
| Derivative assets / liabilities | 1,702 / 1,958 | 732 / 379 | n/m |

### 4.2 Derived liquidity and leverage (estimated)

- **Net cash position ≈ $138.8B** = (242,474 cash+ST inv) − 101,085 debt − 2,590 finance leases. Still a net-cash company — but net cash barely moved despite $86.3B of gross financing inflows, because H1 capex + investment purchases consumed them.
- **Current ratio ≈ 2.7x** (est.): current assets $343.5B ÷ ~$127B current liabilities (AP 20.3 + accrued 73.0 + employee 15.1 + commissions 0.8 + tax 5.2 + deferred rev 7.2 + op lease current 3.5 + fin lease 0.4 + current LTD ~2.0). Up from ~2.1x at 12/31/25.
- **Total equity ≈ $600–630B (est.)** vs ~$406B at 12/31/25 (total assets 595.3 less est. liabilities ~189). Build-up sensitivity means treat as directional only. Equity rose ~$200B+ in six months — roughly $175B net income plus $18B preferred plus issuance.
- **Debt/equity ≈ 16%** (est.), up from ~12%. **Debt/EBITDA:** annualizing Q2 operating income ($163B) plus D&A (~$28–30B) ⇒ ~$190B+ EBITDA vs $101B debt ≈ **0.5x** — still conservative.
- **Cash + investments + private portfolio = $366.7B** vs $121.7B of total debt + leases. Balance-sheet optionality is exceptional.
- **AR quality:** receivables +10.0% vs revenue +24.2% y/y ⇒ **DSO ≈ 52.5 days** (69,175 ÷ [119,796/91]); allowance only **1.44%** of AR. Collections are not a concern; this is a clean working-capital picture.
- **Contract liabilities (deferred revenue) +17.5% y/y** and $4.9B recognized from the opening balance in H1 — a solid forward-demand indicator for Cloud/subscriptions, though it grew slower than revenue (watch Cloud RPO commentary in the 10-Q).

---

## 5. Cash flow: the real story — free cash flow just went negative in Q2

### 5.1 H1 2026 vs H1 2025 ($M)

| Line | H1 2026 | H1 2025 | Δ |
|---|---|---|---|
| **Operating cash flow** | **84,859** | 63,897 | **+32.8%** |
| **Capex (PP&E purchases)** | **(80,598)** | (39,643) | **+103.3%** |
| **Free cash flow (derived)** | **4,261** | 24,254 | **−82.4%** |
| Capex incurred but **not yet paid** (period-end) | **29,113** | 10,635 | +173.7% |
| Purchases of marketable securities | (76,480) | (39,870) | — |
| Sales/maturities of marketable securities | 66,696 | 40,930 | — |
| Purchases of other (private) investments | **(22,051)** | (2,312) | +854% |
| Proceeds from other investments | 1,667 | 873 | — |
| Other investing | (1,359) | (363) | — |
| **Investing cash flow** | **(145,822)** | (40,738) | — |
| Debt proceeds | 56,226 | 31,378 | — |
| Debt repayments | (5,253) | (18,397) | — |
| **Common stock issuance** | **30,499** | 0 | new |
| **Convertible preferred issuance** | **19,063** (incl. $19.0B on 2026-06-05) | 0 | new |
| Minority interest proceeds | 3,758 | 400 | — |
| Dividends paid (common) | (5,231) | (4,977) | +5.1% |
| Dividends paid (preferred) | (86) | 0 | new |
| **Share repurchases** | **0** | **(28,306)** | **−100%** |
| Finance lease principal | (840) | (302) | — |
| **Financing cash flow** | **+86,320** | (26,033) | n/m |
| FX effect | (154) | 444 | — |
| **Net change in cash** | **+25,203** | (2,430) | — |

### 5.2 Quarterly split — the number that matters

| $M | Q1 2026 | Q2 2026 | Q1 2025 | Q2 2025 |
|---|---|---|---|---|
| Operating cash flow | 45,790 | **39,069** | 36,150 | 27,747 |
| Capex | (35,674) | **(44,924)** | (17,197) | (22,446) |
| **Free cash flow** | **10,116** | **(5,855)** | 18,953 | 5,301 |
| Capex / revenue | 32.5% | **37.5%** | 19.1% | 23.3% |

**Alphabet generated negative free cash flow of $5.9B in Q2 2026 — the first materially negative quarter of this cycle — while operating cash flow actually grew 40.8% y/y.** Capex run-rate ($44.9B in one quarter ≈ **$180B annualized**) has decoupled from cash generation. Add the $29.1B of capex accrued but unpaid at 6/30 (vs $10.6B a year earlier) and **H2 cash capex will exceed reported H1 capex** — the cash burn is understated by the P&L-adjacent optics.

### 5.3 Capital-allocation regime change (the structural insight)

In six months Alphabet:
1. **Doubled gross debt** to $101.1B (largest debt build in company history);
2. **Issued $19.1B of convertible preferred** on 2026-06-05 — a first for the company, now carrying $86M of quarterly preferred dividends;
3. **Issued $30.5B of common stock** (shares out +142M, +1.18%) — ending a decade of shrinking share count;
4. **Cut buybacks to zero** (from $28.3B in H1 2025);
5. **Raised the common dividend** to $0.22/qtr ($0.43 in H1, +4.8% y/y; $0.88 annualized) — barely a gesture ($5.2B, ~3% of core earnings);
6. **Spent $22.1B on "other investments"** (private/AI stakes) — 10x the prior-year pace — while its private portfolio simultaneously re-rated ~$41B upward.

Read-through: management is **funding an AI arms race with external capital rather than internal cash flow**, and is choosing strategic ownership stakes over buybacks. For equity holders this is dilutive at the margin but preserves enormous optionality if the AI investments compound. It also makes GOOGL newly rate-sensitive and FCF-sensitive after 20 years of being neither.

---

## 6. Multi-year context available from the FY2025 10-K facts

| $M | 2023 | 2024 | 2025 |
|---|---|---|---|
| Financing cash flow | (72,093) | (79,733) | (37,388) |
| Capex incurred but not yet paid (year-end) | 7,435 | 10,326 | 15,090 |
| Finance lease principal payments | 705 | 405 | 1,988 |

The capex-accrual ramp (7.4 → 10.3 → 15.1 → **29.1** at 6/30/26) is the cleanest available multi-year evidence that the capital-intensity inflection is real, accelerating, and *not* a one-quarter artifact. Financing outflow shrank in 2025 (−$37.4B vs −$79.7B) before flipping to a **+$86.3B inflow** in H1 2026 — the direction change is the signal.

---

## 7. Risks and red flags

1. **Optical-EPS trap (highest immediate risk).** 88% of Q2 net income was non-cash mark-to-market. If the market or a mechanical screen capitalizes $9.11 × 4 = $36.44 of "earnings," valuation gets nonsense-rich; if it strips it entirely, it ignores a real $124B asset. Both are wrong — the asset is real, the earnings are not recurring.
2. **Mark-to-market reversal risk is now two-sided and material.** $124.3B of private securities with $85.7B of *cumulative upward* adjustments sit on the books, marked through the income statement. A 20% private-AI valuation reset would produce a **~$25B non-cash EPS hit** (≈$2/share) — and a similar upside if marks continue. **GOOGL's GAAP EPS has become a levered proxy on private AI valuations.**
3. **Negative FCF + rising debt + zero buyback.** If capex holds at ~$180B annualized against ~$170–180B of OCF, Alphabet is structurally FCF-negative. That justifies a lower multiple on *cash* earnings than the historical franchise and creates credit-rating/refinancing headlines ($2.0B matures in the next 12 months; $36.1B beyond year five, per the FY25 10-K maturity ladder).
4. **Share count now grows:** +1.18% in six months (issuance + SBC $15.2B/半年 = 6.6% of revenue). Per-share growth is being diluted for the first time in years.
5. **Legal overhang:** $17.4B current litigation accrual (+11.3% in six months), with $3.0B of contingency payments disclosed in Q3 2025. Further adverse antitrust/regulatory outcomes are a live EPS and business-model variable.
6. **Tax rate step-up** to 19.1% (from 16.9%) is a ~220bps structural headwind on all future earnings; $22.8B deferred tax liability will unwind into cash taxes as marks are realized.
7. **Opex intensity:** the Q1 2026 opex anomaly (+75.6% y/y) needs explanation; if it was recurring investment rather than one-off, H2 margins compress.
8. **AFS mark noise (minor):** $416M unrealized losses on $53.2B of positions (93% under 12 months) — immaterial to capital but a small AOCI drag.
9. **No insider data available** — cannot assess management/insider conviction; do not assume either way.

**Positive offsets:** FX hedges flip from −$60M (12/31/25) to **+$614M** of gains to be reclassified into income over the next 12 months (a modest revenue/income tailwind vs. a headwind a year ago); operating momentum is broad (+24% revenue with margin expansion is rare at this scale); net cash of ~$139B plus $366.7B total liquid+strategic assets; DSO improving; deferred revenue +17.5%.

---

## 8. Actionable trading insights

1. **Fade any headline-EPS-driven gap.** Core Q2 EPS is ~$2.61 (my derivation: operating $40,770M + net interest, taxed at 19.1%, ÷12,306M diluted shares). Compare sell-side/core expectations to that, not $9.11. Watch for the company's own non-GAAP framing in the 10-Q/8-K — if management highlights "excluding investment gains," the market will converge to core.
2. **Trade the FCF narrative before the EPS narrative.** Negative Q2 FCF (−$5.9B) with $29.1B of unpaid capex is the most likely bear catalyst. Key monitorable: Q3 capex/revenue ratio (37.5% in Q2). Any commentary capping 2026 capex is a bullish re-rating trigger for the *multiple*; any raise is a de-rating trigger regardless of revenue growth.
3. **Own the operating franchise, hedge the marks.** Revenue +24.2% with gross margin +220bps and operating margin +160bps is unambiguous share-gain/monetization evidence. A structure that isolates core earnings (e.g., owning GOOGL against a private-AI-valuation hedge) is the logically consistent expression.
4. **Quantify the private-portfolio identity.** Highest-value next step: read the Q2 10-Q equity-securities note to identify the ~$77B Q2 residual gain source (a re-rated non-marketable holding). If it was a one-time valuation event now fully marked, forward earnings normalize hard; if it was a partial markup with more marks pending, momentum persists.
5. **Watch credit, not equity, first.** $101B debt, $18B convertible preferred, and $0 buybacks change the marginal buyer base. A rating-agency comment or further large issuance would pressure the equity even with operations intact.
6. **Dilution math for models:** diluted shares 12,306M (Q2) vs 12,206M (Q2'25). Use +1.5–2.0% annual dilution for 2026–27, plus the $86M/qtr preferred dividend as a senior claim on ~$19B of new capital.
7. **Asymmetry skew:** two-sided mark volatility + structurally lower FCF + intact operating momentum ⇒ favour **options structures over naked directional risk** around the next two prints.
8. **Insider/flow blind spot:** no insider-transaction archive exists for GOOGL in this data package. Do not treat insider silence as signal; source it separately before drawing conclusions.

---

## 9. Key points summary table

| Category | Metric | Latest (Q2/H1 2026) | Prior (Q2/H1 2025) | Δ / Note | Trader read |
|---|---|---|---|---|---|
| Filing event | Q2 2026 10-Q accepted | 2026-07-23 | — | 1 day before analysis date | Fresh information; thin post-print window |
| Revenue (derived) | Q2 revenue | $119,796M | $96,428M | **+24.2%** | Genuine acceleration |
| Revenue (derived) | H1 revenue | $229,692M | $186,662M | +23.1% | Broad strength |
| Gross margin | Q2 | 61.7% | 59.5% | +220 bps | Mix/AI efficiency improving |
| Operating income | Q2 | $40,770M | $31,271M | **+30.4%** | Operating leverage |
| Operating margin | Q2 / H1 | 34.0% / 35.0% | 32.4% / 33.1% | +160 / +190 bps | Core story |
| Opex ex-COGS | Q1 2026 anomaly | $34,638M (+75.6%) | $19,728M | Investigate 10-Q | Possible Q1 one-off charge |
| Non-operating income | Q2 | $97,983M | $2,662M | 81.8% of revenue | Optical distortion |
| Equity securities gains | Q2 / H1 | $99,031M / $135,946M | $1,286M / $11,411M | ~88% of Q2 net income | Non-cash, non-recurring quality |
| Core EPS (derived, ex-gains) | Q2 / H1 | ≈$2.61 / ≈$5.30 | ≈$2.22 / ≈$4.35 | **+17.5% / +21.9%** | Benchmark vs consensus |
| GAAP diluted EPS | Q2 / H1 | $9.11 / $14.24 | $2.31 / $5.12 | +294% / +178% | Do not capitalize |
| Effective tax rate | Q2 / H1 | 19.1% | 16.9% / 17.1% | +220 bps | Structural headwind |
| Net deferred tax liability | 6/30/26 | $22,819M | $919M (12/31/25) | +2,383% | Tax on unrealized marks |
| SBC | Q2 / H1 | $8,000M / $15,200M | $6,000M / $11,500M | +33% / +32% | 6.6% of H1 revenue |
| D&A | H1 | $14,131M | $9,731M | +45.2% | Rising with capex |
| Operating cash flow | H1 | $84,859M | $63,897M | +32.8% | Cash engine intact |
| Capex | H1 / Q2 | $80,598M / $44,924M | $39,643M / $22,446M | **+103% / +100%** | ~$180B annualized run-rate |
| Capex / revenue | Q2 | 37.5% | 23.3% | +1,420 bps | Capital intensity shock |
| **Free cash flow** | H1 / Q2 | **$4,261M / −$5,855M** | $24,254M / +$5,301M | **−82% / negative** | Primary bear catalyst |
| Capex incurred, unpaid | 6/30/26 | $29,113M | $10,635M | +173.7% | H2 cash capex higher |
| Cash + ST investments | 6/30/26 | $242,474M | $126,843M | +91.2% | Funded by issuance |
| Total debt | 6/30/26 | $101,085M | $49,085M | **+106%** | Leverage regime change |
| Convertible preferred | 6/30/26 | $18,023M | $0 | New, 2026-06-05 | First-ever; $86M/qtr dividend |
| Common stock issued | H1 2026 | $30,499M | $0 | New | Dilution, +142M shares |
| Share count | 6/30/26 | 12,230M | 12,088M (12/31/25) | +1.18% | Buyback era paused |
| Buybacks | H1 2026 | $0 | $28,306M | −100% | Removes support bid |
| Dividends | Q2 per share / H1 paid | $0.22 / $5,231M | $0.21 / $4,977M | +4.8% | ~3% of core earnings |
| Private equity portfolio (no RDFV) | 6/30/26 | $124,259M | $64,094M | +93.9% | Forward EPS volatility source |
| — cumulative upward marks | 6/30/26 | $85,732M | $44,485M | +$41,247M | Reversal risk |
| Contract liabilities | 6/30/26 | $10,100M | $8,600M | +17.5% | Forward demand (Cloud) |
| Accounts receivable | 6/30/26 | $69,175M | $62,886M | +10.0% | DSO ~52.5d; quality fine |
| Allowance / AR | 6/30/26 | 1.44% | 1.47% | Stable | Clean |
| Litigation accrual (current) | 6/30/26 | $17,356M | $15,594M | +11.3% | Regulatory overhang |
| Net cash (est.) | 6/30/26 | ≈$138.8B | ≈$73.7B | Rising but slower than debt | Still fortress-like |
| Current ratio (est.) | 6/30/26 | ≈2.7x | ≈2.1x | Improving | Ample liquidity |
| Debt/equity (est.) | 6/30/26 | ≈16% | ≈12% | Rising | Low absolute leverage |
| Total assets | 6/30/26 | $921,983M | $595,281M | **+54.9%** | Marks + issuance + cash |
| Insider transactions | — | **Data unavailable** | — | Vendor has no archive | Do not infer |
| Valuation | Price-dependent | Not computable from fact set | — | Use core EPS ≈$10.4–10.6 annualized | Anchor on core, not GAAP |

---

### Bottom line for traders
GOOGL's Q2 2026 is a **fundamentally strong operating quarter (revenue +24%, operating margin 34%, OCF +41%) wrapped in a spectacularly noisy GAAP print (+$99B non-cash marks) and delivered alongside a historic capital-structure pivot** (debt ×2, first convertible preferred, first common issuance, buybacks to zero, negative Q2 FCF). The correct analytical anchor is **core EPS ≈$2.61 (Q2) / ≈$5.30 (H1), growing ~18–22%**, funded by a business with improving gross and operating margins — but now consuming more cash than it generates at the capex line while carrying $124B of income-statement-marked private assets that make future GAAP EPS inherently volatile in both directions. Trade the capex/FCF trajectory and the private-mark identity; do not trade the $9.11 headline.