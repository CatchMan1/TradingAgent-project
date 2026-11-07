# AMZN — Fundamental Research Report
**Amazon.com, Inc. (AMZN)** · Point-in-time SEC data public as of **2026-07-24** · Most recent filing: **Q1 FY2026 Form 10-Q, accepted 2026-04-30** (accn 0001018724-26-000014); most recent 10-K accepted **2026-02-06**

> **Data-scope note (important for the reader):** All figures below are drawn from the point-in-time SEC fact cache. The dataset returned did **not** contain: a company-profile/segment narrative, price/market-cap data, a net PP&E line, a FY2025 revenue or FY net-income tag, or any insider-transaction archive (**the insider-transactions tool explicitly returned DATA_UNAVAILABLE for AMZN — no insider buying/selling is reported here, and none should be inferred**). Items I derived arithmetically are labelled (derived).

---

## 1. Company snapshot

Amazon is a three-reporting-segment company (`NumberOfOperatingSegments = 3` per the Q1 FY2026 10-Q: North America, International, and AWS). It is a scale platform spanning (a) online and physical retail plus third-party marketplace, (b) advertising (ad spend tag: $20.3B → $21.4B → $23.5B in 2023/2024/2025 — a proxy for the ads business's own promotional spend), (c) subscription services, and (d) AWS cloud/AI infrastructure, whose build-out now dominates the capital-allocation story.

- **Shares outstanding:** 10,754M (2026-03-31); 10,757M (2026-04-22 cover date)
- **Diluted shares (derived):** ~10,883M (Q1 FY2026 net income ÷ diluted EPS), up ~1.0% yoy from ~10,772M
- **Dividends / buybacks:** none evidenced — financing flows are net cash *inflows* from debt issuance; no treasury-purchase line items appear. Share count is creeping up on stock comp, though SBC is structurally declining (see §4).

---

## 2. Q1 FY2026 income statement (Jan–Mar 2026) vs Q1 FY2025

| $M | Q1 FY2026 | Q1 FY2025 | Δ yoy |
|---|---:|---:|---:|
| Revenue | **181,519** | 155,667 | **+16.6%** |
| Cost of goods & services | 87,463 | 76,976 | +13.6% |
| **Gross profit (derived)** | **94,056** | 78,691 | **+19.5%** |
| Gross margin | 51.8% | 50.6% | +1.2 pt |
| Marketing | 10,314 | 9,763 | +5.6% |
| G&A | 2,587 | 2,628 | −1.6% |
| Total costs & expenses | 157,667 | 137,262 | +14.9% |
| **Operating income** | **23,852** | 18,405 | **+29.6%** |
| **Operating margin** | **13.1%** | 11.8% | +1.3 pt |
| Interest expense | 800 | 541 | +47.9% |
| Investment income | 1,135 | 1,066 | +6.5% |
| Other non-operating income | **15,647** | 2,749 | +469% |
| Non-operating income, net | 15,982 | 3,274 | +388% |
| Pre-tax income | 39,834 | 21,679 | +83.8% |
| Income tax | 9,560 | 4,553 | +110% |
| Effective tax rate | 24.0% | 21.0% | +3.0 pt |
| **Net income** | **30,255** | 17,127 | **+76.7%** |
| Net margin | 16.7% | 11.0% | +5.7 pt |
| **Diluted EPS** | **$2.78** | $1.59 | **+74.8%** |
| Basic EPS | $2.82 | $1.62 | +74.1% |

*(Derived shares above; all other values are as-filed tags.)*

### The single most important earnings insight: reported EPS is heavily non-operational
- `OtherNonoperatingIncomeExpense` was **$15.65B** in Q1 FY2026 vs $2.75B a year ago.
- `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount` = **$12.33B** in Q1 FY2026 — a **non-cash upward revaluation of a non-marketable equity stake** (vs just $37M in Q1 FY2025).
- Corroborating balance-sheet proof: equity securities without readily determinable fair value jumped from **$16.2B (12/31/25) to $48.1B (3/31/26)**, i.e. +$31.9B in one quarter, and `DeferredIncomeTaxExpenseBenefit` spiked to **$12.80B** (vs $0.51B) — the deferred tax on a book gain that is not yet taxable.
- **Stripped of the ~$12.3B pre-tax revaluation (tax-effected at ~24%), "core" net income ≈ $20.9B and core EPS ≈ $1.92** — still **~+21% yoy** versus $1.59, but ~31% below the $2.78 headline.
- **Traders should model this as a swing factor in both directions.** A comparable mark-*down* in a future quarter would hit reported EPS by a similar magnitude; headline EPS is no longer a clean read on operating momentum. Operating income (+29.6%, margin 13.1%) is the cleaner signal.

---

## 3. Balance sheet — a step-change in size and leverage

| $M | 2026-03-31 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 101,816 | 86,810 | +15,006 |
| Marketable debt securities (AFS) | 42,200 | 45,800 | −3,600 |
| Accounts receivable, net | 75,532 | 67,729 | +7,803 |
| Inventory, net | 36,534 | 38,325 | −1,791 |
| **Total current assets** | **255,155** | 229,083 | **+26,072** |
| Other assets, non-current | 151,827 | 122,607 | +29,220 |
| Goodwill | 23,449 | 23,273 | +176 |
| Operating lease ROU asset | 88,741 | 86,054 | +2,687 |
| **Total assets** | **916,630** | 818,042 | **+98,588** |
| Accounts payable | 124,749 | 121,909 | +2,840 |
| Accrued liabilities | 71,120 | 75,520 | −4,400 |
| Contract liabilities – current | 20,887 | 20,576 | +311 |
| **Total current liabilities** | **216,756** | 218,005 | −1,249 |
| Long-term debt (total) | **122,632** | 68,836 | **+53,796** |
| — non-current portion | 119,074 | 65,648 | +53,426 |
| — current portion | 2,832 | 2,748 | +84 |
| Operating lease liability (total) | 91,617 | 89,252 | +2,365 |
| Finance lease liability (total) | 13,325 | 12,286 | +1,039 |
| Other non-current liabilities | 48,072 | 35,985 | +12,087 |
| **Total stockholders' equity (derived)** | **441,188** | 410,625 | **+30,563 (+7.4%)** |

**Liquidity & solvency reads**
- **Current ratio: 1.18x** (255,155 / 216,756) vs **1.05x** at 12/31/25 — a clear liquidity improvement.
- **Cash + marketable securities = $144.0B** against **$122.6B of debt** → still a **net-cash position (~+$21.4B)** on a debt-only basis.
- Including leases, **adjusted debt ≈ $227.6B** (debt + operating + finance leases) → **net debt ≈ $83.6B**. Still modest versus a $441B equity base, but the direction of travel matters.
- **Debt/equity (debt only): 0.28x**; equity/assets = 48.1%.
- Long-term debt **rose 78% in a single quarter** ($68.8B → $122.6B). This is the biggest structural change in the filing set.
- Aggregate `ContractualObligation` at 3/31/26 = **$569.3B**, of which $57.1B due within twelve months, plus $46.5B of purchase-type commitments due in the remainder of FY2026.

---

## 4. Cash flow — the capex super-cycle has flipped free cash flow negative

### Q1 FY2026 vs Q1 FY2025, and trailing-twelve-month

| $M | Q1 FY2026 | Q1 FY2025 | TTM (Apr'25–Mar'26) | TTM (Apr'24–Mar'25) |
|---|---:|---:|---:|---:|
| Cash from operations | **26,032** | 17,015 | **148,531** | 113,903 |
| Capex (productive assets) | **44,203** | 25,019 | **151,003** | 93,093 |
| **Free cash flow (derived)** | **(18,171)** | (8,004) | **(2,472)** | **20,810** |
| Depreciation & amortization | 18,945 | 14,262 | 70,439 | 55,373 |
| Purchases of marketable securities | 23,256 | 13,333 | 64,693 | 37,373 |
| Sales/maturities of securities | 17,686 | 7,737 | 54,335 | 22,748 |
| Business acquisitions, net of cash | **15,408** | (48) | 19,297 | 3,680 |
| Long-term debt issued | **53,441** | 746 | 68,368 | 746 |
| Long-term debt repaid | 0 | 0 | 5,021 | 8,852 |
| Short-term debt, net | (91) | (267) | 1,070 | (119) |
| **Investing cash flow** | **(64,212)** | (29,803) | (176,954) | (106,283) |
| **Financing cash flow** | **+52,767** | (47) | **+62,475** | (10,603) |
| Operating lease payments | 4,315 | 3,562 | 15,791 | 12,571 |
| Taxes paid, net | 1,323 | 877 | 8,741 | 12,727 |

**Three actionable cash-flow conclusions**

1. **Capex is now larger than operating cash flow.** Q1 capex of **$44.2B** = **24.4% of revenue** and **+76.7% yoy**, while CFO was only $26.0B. TTM capex **$151.0B > TTM CFO $148.5B** → **TTM FCF ≈ −$2.5B**. Two years ago (FY2023) FCF was ~$32B. The company is funding an AI/cloud infrastructure build with debt rather than internal cash.
2. **The funding mix has rotated from equity-like self-funding to levered funding.** Financing swung from **−$10.6B TTM (prior year)** to **+$62.5B TTM**, essentially all long-term debt issuance (+$68.4B TTM, of which **$53.4B in Q1 alone**). Interest expense is already responding: **+47.9% yoy** to $800M/quarter, and it will keep climbing as the new $54B tranche seasons.
3. **Depreciation is the next margin headwind.** D&A of $18.9B in Q1 (+32.8% yoy) is growing roughly half as fast as capex; capex/D&A on a TTM basis is **2.14x**, so depreciation growth is locked in for several quarters. Also note `CapitalExpendituresIncurredButNotYetPaid` rose from **$16.8B (FY2024) to $27.0B (FY2025)** — accrued but unpaid capex is inflating, meaning reported capex will keep running hot.

**Working-capital quality caveat:** CFO ($26.0B) trailed net income ($30.3B) because earnings were flattered by non-cash gains and because accrued liabilities fell **$8.0B** in the quarter while receivables rose ~$7.8B. Cash conversion (CFO/NI) of **0.86x** in Q1 is soft versus the **1.64x** TTM ratio.

---

## 5. Multi-year financial history (10-K suite)

| $M | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Total costs & expenses | 537,933 | 569,366 | **636,949** |
| — yoy | — | +5.8% | **+11.9%** |
| Stock-based comp | 24,023 | 22,011 | **19,467** |
| Advertising expense (Amazon's own) | 20,300 | 21,400 | 23,500 |
| Cash from operations | 84,946 | 115,877 | **139,514** |
| Capex (productive assets) | 52,729 | 82,999 | **131,819** |
| **FCF (derived)** | **32,217** | **32,878** | **7,695** |
| Investing cash flow | (49,833) | (94,342) | **(142,545)** |
| Financing cash flow | (15,879) | (11,812) | **+9,661** |
| Long-term debt issued | 0 | 0 | 15,673 |
| Operating lease payments | 10,453 | 12,341 | 15,038 |
| Finance lease principal paid | 4,384 | 2,043 | 1,557 |
| Comprehensive income | 31,872 | 62,254 | **105,934** |
| Capex incurred but unpaid (year-end) | n/a | 16,800 | 27,000 |

**Trend observations**
- **Cost growth re-accelerated** to +11.9% in FY2025 after +5.8% in FY2024 — the infrastructure/AI build is now visible in the expense base, not just the capex line.
- **FCF has collapsed ~76%** from $32.9B (FY2024) to $7.7B (FY2025) and is negative on a TTM basis.
- **SBC is falling meaningfully** (−19% from FY2023's $24.0B to FY2025's $19.5B), a genuine per-share earnings tailwind and a credible offset to creeping share count. Unrecognized SBC at 3/31/26: **$14.4B**.
- **Comprehensive income compounded fast** ($31.9B → $62.3B → $105.9B), though Q1 FY2026 AOCI *fell* from $28.2B to $24.9B on AFS unrealized losses (−$2.5B) and FX translation (−$0.8B) — a reminder that the AFS portfolio and a strong dollar are live P&L/OCI variables.

---

## 6. Capital-structure detail that affects forward risk

- **Debt maturity ladder as of 12/31/25:** $2.75B (next 12m), $8.83B (yr 2), $4.75B (yr 3), $3.00B (yr 4), $4.50B (yr 5), **$45.0B after yr 5** — a well-laddered legacy profile, now being layered with fresh Q1 FY2026 issuance (maturity schedule of the new $54B not disclosed in the returned dataset).
- **Operating leases:** $110.1B undiscounted, $13.9B due within 12 months; weighted-average discount rate 3.8% (vs 3.7% at year-end). Finance leases: $16.5B undiscounted.
- **Debt securities portfolio is conservative:** AFS fair value $128.5B including cash-equivalent holdings, of which **$119.0B matures within one year**; gross unrealized gains only $18M vs losses $58M — minimal rate risk.
- **Q1 FY2026 acquisitions of $15.4B** were the largest in company history, yet goodwill rose only **$176M** while equity-method investments rose $264M and non-marketable equity securities rose $31.9B. **The $15.4B outlay was therefore largely not a conventional goodwill-generating acquisition** — reconcile before extrapolating M&A multiples. This is a genuine open item for anyone modelling inorganic growth.

---

## 7. Derived performance & quality metrics

| Metric | Value | Basis |
|---|---:|---|
| TTM net income | $90,798M | Apr'25–Mar'26 |
| Approx. TTM diluted EPS (derived) | **~$8.35–8.40** | TTM NI ÷ ~10.88B diluted shares |
| ROE (TTM, derived) | **~21.3%** | NI ÷ avg equity ($441.2B / $410.6B) |
| ROA (TTM, derived) | **~10.5%** | NI ÷ avg total assets |
| TTM CFO / net income | 1.64x | — |
| Q1 CFO / net income | 0.86x | — |
| Capex / revenue (Q1 FY2026) | 24.4% | — |
| Capex / D&A (TTM) | 2.14x | — |
| Cash + securities / total debt | 1.17x | — |
| Net debt incl. leases (derived) | ~$83.6B | — |

> **No valuation multiples are provided here.** The tool set returned no price, market-cap, or EV data for AMZN as of 2026-07-24, so P/E, EV/EBITDA and FCF-yield cannot be computed responsibly. Apply the ~$8.4 TTM EPS and the statements above to your own price feed.

---

## 8. Actionable takeaways for traders

**Bull case (evidence-based)**
1. **Operating leverage is real and accelerating:** revenue +16.6% with operating income +29.6% and operating margin expanding 130bp to **13.1%**. Gross margin up 120bp to 51.8%. Marketing grew just 5.6% and G&A fell — expense discipline at the corporate line is intact.
2. **Balance-sheet capacity is not a constraint:** $144B cash+securities, net cash versus debt, current ratio improved to 1.18x, and the market just absorbed $53B of new AMZN paper in one quarter — access to capital is unambiguously open.
3. **SBC is shrinking** (−19% since FY2023) and share count grew only ~1% yoy, so per-share compounding is clean.
4. **A hidden asset base is being revalued upward** — non-marketable equity holdings went $16.2B → $48.1B in one quarter, with a $12.3B recognized gain. Even if you exclude the gain from earnings, the balance sheet now carries ~$48B of such stakes whose future marks are optionality (in *either* direction).
5. **Q1 deferred revenue** of $9.4B recognized from prior contract liabilities and $25.3B total contract liabilities signal a durable backlog.

**Bear case / risks to underwrite**
1. **Negative TTM free cash flow (−$2.5B)** with capex at 24% of revenue and +77% yoy. FCF-based valuation support has effectively disappeared for now; the market is paying for a build-out with an unknowable payback period.
2. **Leverage inflection:** long-term debt +78% in one quarter, interest expense +48% yoy and rising. TTM financing inflow of +$62.5B versus −$10.6B a year earlier is a regime change, not a blip.
3. **Depreciation torque:** D&A +33% yoy and capex/D&A at 2.14x means reported margins face mechanical compression for several quarters even if revenue holds.
4. **Earnings quality:** ~31% of Q1 EPS came from a non-cash equity mark. Expect quarter-to-quarter EPS volatility unrelated to operations, and expect the sell-side "beat/miss" framing to be noisy.
5. **Tax rate stepped up** to 24.0% from 21.0% — a persistent headwind to EPS growth relative to prior-year comps.
6. **FX and securities drags visible in OCI:** AOCI fell $3.4B in the quarter despite record earnings.

**What to monitor next (highest information value)**
- Q2 FY2026 (10-Q ~late July/Aug 2026): (a) does capex growth decelerate from +77%, (b) does CFO/capex turn positive again, (c) the trajectory of the equity-securities fair-value marks, (d) interest expense run-rate on the new debt, (e) whether the 13%+ operating margin holds as depreciation ramps.
- Any 8-K/footnote disclosure on the **$15.4B Q1 acquisition** and on the identity of the **$12.3B revalued stake** — both are material and both are underspecified in the fact set.
- **Insider transactions: unavailable in this dataset.** Do not assume insider buying or selling either way; verify via Form 4 filings directly before any signal is drawn.

---

## 9. Key points summary

| Category | Metric / Fact | Value | Read-through |
|---|---|---|---|
| **Latest filing** | Q1 FY2026 10-Q | Accepted 2026-04-30 | Most current fundamental anchor |
| **Growth** | Revenue yoy | +16.6% to $181.5B | Re-acceleration; strongest in the dataset |
| **Profitability** | Operating income / margin | $23.85B / 13.1% | +29.6% yoy; margin +130bp |
| **Profitability** | Diluted EPS | $2.78 (+74.8%) | Inflated by non-cash gain |
| **Quality of earnings** | Non-marketable equity revaluation gain | $12.33B pre-tax | Core EPS ≈ **$1.92** (+21% yoy) |
| **Capex** | Q1 capex / TTM capex | $44.2B (+77%) / $151.0B | 24.4% of revenue |
| **Free cash flow** | TTM FCF (derived) | **≈ −$2.5B** | Negative; FY2025 FCF only $7.7B vs $32.9B FY2024 |
| **Cash generation** | TTM CFO | $148.5B | Now < capex |
| **Financing** | Q1 LT debt issued / LT debt outstanding | $53.4B / $122.6B | Debt +78% q/q; leverage regime change |
| **Interest** | Q1 interest expense | $800M (+47.9%) | Rising with new issuance |
| **Liquidity** | Cash + securities / current ratio | $144.0B / 1.18x | Strong; improved from 1.05x |
| **Solvency** | Debt/equity; net debt incl. leases | 0.28x; ~$83.6B | Still comfortable |
| **Equity** | Stockholders' equity (derived) | $441.2B (+7.4% q/q) | ROE ~21% TTM |
| **Leases** | Operating lease liability / next-12m payments | $91.6B / $13.9B | Material off-balance-sheet-style obligation now on BS |
| **SBC** | FY2025 SBC / unrecognized | $19.5B / $14.4B | −19% since FY2023 — a tailwind |
| **M&A** | Q1 business acquisitions | $15.4B | Largest ever, but goodwill only +$176M — unresolved |
| **Commitments** | Total contractual obligations | $569.3B ($57.1B <12m) | Large fixed-cost base |
| **Insider activity** | Form 4 data | **UNAVAILABLE** | No signal available; do not infer |
| **Valuation** | Price / market cap / multiples | **Not provided by tools** | Use ~$8.4 TTM EPS in your own model |

**Bottom line for AMZN:** operating fundamentals are the strongest in the dataset — 16.6% revenue growth, 13.1% operating margin, +30% operating income — but the company has simultaneously entered a debt-funded capex super-cycle that has erased free cash flow (TTM ≈ −$2.5B), lifted long-term debt 78% in one quarter, and produced a headline EPS print that is roughly one-third non-cash. The tradable tension is: **excellent operating momentum and unconstrained liquidity versus zero FCF, a rising depreciation and interest drag, and a widening dispersion between reported and core earnings.** Position sizing should reflect that the reported EPS series is now structurally volatile for reasons unrelated to the business.