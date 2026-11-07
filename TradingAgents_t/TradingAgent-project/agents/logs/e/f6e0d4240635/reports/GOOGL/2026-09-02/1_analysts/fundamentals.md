# GOOGL — Alphabet Inc. | Fundamental Deep Dive
**As of:** 2026-09-02 | **Latest filing in window:** Q2 2026 Form 10-Q (filed 2026-07-23) | **Prior filings:** Q1 2026 10-Q (2026-04-30), FY2025 10-K (2026-02-05)

> **Data provenance note (important):** All figures below are SEC XBRL facts filtered by actual EDGAR acceptance time. The returned fact window does **not** include a standalone `Revenues` tag, total liabilities, total stockholders' equity, goodwill, or R&D as a separate line. Revenue has therefore been **derived arithmetically as `Costs and Expenses + Operating Income`** — a derivation I validated against Q2 2025 and Q1 2025 (derived $96,428M and $90,234M, matching the periods' reported revenue exactly). Items that could not be retrieved are explicitly flagged rather than estimated. No new SEC filing occurred in the trailing 7 days.

---

## 1. Executive summary — the six things that matter

1. **Operating momentum is genuinely strong and accelerating.** 1H2026 revenue ≈ **$229.7B, +23.1% YoY** (Q1 +21.8%, Q2 +24.2%). Operating income **$80.5B, +30.0%**, operating margin **35.0% vs 33.1%**, gross margin **62.0% vs 59.6%**. Margin *expansion* occurred despite depreciation rising **+43%** — a high-quality signal.
2. **Headline EPS is heavily distorted by non-operating investment gains.** 1H2026 diluted EPS **$14.24 vs $5.12**, but non-operating income was **$135.7B** (vs $13.8B), of which **$135.9B** is `EquitySecuritiesFvNiGainLoss`. My operating-income-based "core" EPS is roughly **$5.3**, i.e. **~63% of reported EPS is non-core**. Q2's reported **+294% EPS growth** collapses to roughly **+16%** on a core basis.
3. **Free cash flow has inverted.** 1H2026 CFO **$84.9B (+32.8%)** vs capex **$80.6B (+103%)** → FCF **$4.3B vs $24.3B (-82%)**. Q2 2026 standalone FCF was **negative ≈ -$5.9B** (CFO $39.1B − capex $44.9B). Capex is now **35.1% of revenue** (was 21.2%), and **$29.1B** of capex was incurred-but-unpaid at quarter-end — cash capex will rise further in 2H.
4. **The balance sheet was pre-funded with an unprecedented equity/debt raise.** 1H2026: **$56.2B net debt proceeds**, **$30.5B common stock issuance**, **$19.1B convertible preferred issuance** (2026-06-05), **$3.8B subsidiary minority proceeds**. Gross debt **$101.1B (+106% YTD)**. Cash + short-term investments **$242.5B**, leaving **net cash ≈ $141.4B** — still fortress-like.
5. **Shareholder returns rotated hard from buybacks to AI capex/M&A.** Buybacks: **$0 in 1H2026 vs $28.3B in 1H2025**. Dividend continued and rose to **$0.22/qtr** (1H $0.43 vs $0.41), cost $5.2B — only ~3% of reported earnings.
6. **Balance-sheet composition signals a large strategic transaction.** Gross finite-lived intangibles jumped **$2.47B → $10.59B**, intangible amortization **$246M → $545M**, deferred tax liabilities **$0.9B → $22.8B**, and private (Level 3) equity securities **$64.1B → $124.3B**. Combined with the equity/preferred issuance, this is consistent with one or more large acquisitions plus remeasurement of a pre-existing equity stake. *(Inference from disclosed tags; goodwill is not in the returned window and is unverified.)*

---

## 2. Company profile

**Alphabet Inc.** is the Delaware-incorporated, Mountain View–headquartered parent of Google. It reports three segments — **Google Services** (Search and other advertising, YouTube ads, subscriptions/platforms/devices), **Google Cloud** (infrastructure, platform, and collaboration/enterprise AI offerings), and **Other Bets** (long-horizon ventures such as autonomous driving and life sciences). Dual-class structure: **GOOGL** (Class A, 1 vote) and GOOG (Class C, no vote). As of 2026-06-30: **12.230B shares outstanding** across classes, 300B shares authorized, $0.001 par.

Segment-level revenue, headcount, and backlog were **not present** in the returned fact window and are deliberately not estimated. Contract liabilities (**$10.10B vs $8.60B, +17.4%**) are the best available proxy for forward-booked/committed revenue and point to healthy Cloud demand.

---

## 3. Income statement — derived and analyzed

### 3.1 Period reconstruction ($M)

| Line (derived) | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 | 1H2025 | 1H2026 | 1H YoY |
|---|---:|---:|---:|---:|---:|---:|---:|
| Revenue | 90,234 | 96,428 | 109,896 | 119,796 | 186,662 | 229,692 | **+23.1%** |
| Cost of revenue | 36,361 | 39,039 | 41,271 | 45,943 | 75,400 | 87,214 | +15.7% |
| Gross profit | 53,873 | 57,389 | 68,625 | 73,853 | 111,262 | 142,478 | +28.1% |
| Gross margin | 59.7% | 59.5% | 62.5% | 61.7% | 59.6% | **62.0%** | +240 bp |
| Other opex (R&D+S&M+G&A) | 23,267 | 26,118 | 29,143 | 33,083 | 49,385 | 62,012 | +25.6% |
| of which G&A | 3,539 | 5,209 | 4,291 | 6,461 | 8,748 | 10,752 | +22.9% |
| Total costs & expenses | 59,628 | 65,157 | 70,400 | 79,026 | 124,785 | 149,226 | +19.6% |
| **Operating income** | 30,606 | 31,271 | 39,696 | 40,770 | 61,877 | **80,466** | **+30.0%** |
| Operating margin | 33.9% | 32.4% | 36.1% | 34.0% | 33.1% | **35.0%** | +190 bp |
| Non-operating income | 11,183 | 2,662 | 37,716 | 97,983 | 13,845 | **135,699** | — |
| Pre-tax income | 41,789 | 33,933 | 77,412 | 138,753 | 75,722 | 216,165 | +185% |
| Tax | 6,249 | 5,737 | 14,834 | 26,560 | 12,986 | 41,394 | — |
| Effective tax rate | 15.0% | 16.9% | 19.2% | 19.1% | 17.1% | **19.1%** | +200 bp |
| **Net income** | 35,540 | 28,196 | 62,578 | 112,193 | 63,736 | **174,771** | +174% |
| Diluted EPS | 2.81 | 2.31 | 5.13 | 9.11 | 5.12 | **14.24** | +178% |
| Basic EPS | — | 2.33 | — | 9.23 | 5.16 | 14.41 | — |

### 3.2 Quality-of-earnings bridge

| Metric | 1H2025 | 1H2026 | Comment |
|---|---:|---:|---|
| Reported net income | 63,736 | 174,771 | +174% |
| Less: non-operating income (after 19.1% tax) | (11,214) | (109,780) | 81% of 1H2026 pretax profit |
| **Core net income (approx.)** | **52,522** | **64,991** | **+23.7%** |
| **Core diluted EPS (approx.)** | **~4.29** | **~5.30** | **+23.6%** |
| Reported diluted EPS | 5.12 | 14.24 | +178% |
| **Non-core share of reported EPS** | **16%** | **63%** | pivotal |

**Key detail:** of the **$135.9B** `EquitySecuritiesFvNiGainLoss`, only **$0.84B realized** and **$21.5B unrealized** are itemized — **~$113.6B is unexplained by the realized/unrealized tags**. That pattern strongly suggests a **one-off step-acquisition remeasurement gain**, not mark-to-market on liquid securities. Traders should model it as **zero in forward periods**.

### 3.3 Cost and investment dynamics

- **SBC: $15.20B vs $11.50B (+32.2%)**, now **6.6% of revenue** and **18.9% of operating income**. Q2 alone $8.00B. Real dilution, not just an accounting line.
- **Depreciation: $13.59B vs $9.49B (+43.2%)** — 5.9% of revenue vs 5.1%. The AI datacenter build is now hitting the P&L.
- **Interest expense: $1.81B vs $0.30B (+514%)** on the doubled debt load, partly offset by interest income **$2.81B vs $2.05B**; net interest income still **+$1.0B**.
- **G&A spiked +50.6% QoQ** ($4.29B → $6.46B) — worth questioning on the Q3 call; likely transaction/integration costs.
- **Q2 operating margin compressed 209 bp QoQ** (36.1% → 34.0%) as cost of revenue (+11.3% QoQ) and opex (+13.5% QoQ) outgrew revenue (+9.0% QoQ). This is the single most important trend to monitor.

---

## 4. Balance sheet — liquidity, leverage, and what changed

| Item ($M) | 2025-12-31 | 2026-06-30 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 30,708 | 55,911 | +82.1% |
| Cash + short-term investments | 126,843 | **242,474** | +91.2% |
| Accounts receivable, net | 62,886 | 69,175 | +10.0% |
| Allowance for doubtful accounts | 924 | 995 | +7.7% (0.9%→1.4% of AR) |
| **Total current assets** | 206,038 | 343,524 | +66.7% |
| AFS debt securities | n/a in window | 99,500 | — |
| Equity securities w/o readily determinable FV (Level 3) | 64,094 | **124,259** | **+93.9%** |
| — cumulative upward revaluation | 44,485 | 85,732 | +92.7% |
| — cumulative downward revaluation | 8,820 | 9,115 | +3.3% |
| Gross finite-lived intangibles | 2,467 | 10,585 | +329% |
| **Total assets** | 595,281 | **921,983** | **+54.9%** |
| Accounts payable | 12,200 | 20,258 | +66.0% |
| Accrued liabilities | 55,557 | 73,014 | +31.4% |
| Employee-related liabilities | 17,546 | 15,086 | -14.0% |
| Contract liabilities (total) | 8,600 | 10,100 | +17.4% |
| Loss contingency accrual (current) | 15,594 | 17,356 | +11.3% |
| **Debt (carrying)** | **49,085** | **101,085** | **+106.0%** |
| Deferred income tax liabilities, net | 919 | 22,819 | +2,383% |
| Accrued income taxes, noncurrent | 9,531 | 11,306 | +18.6% |
| Operating lease liability | 15,954 | 18,037 | +13.1% |
| Finance lease liability | 2,500 | 2,590 | +3.6% |
| AOCI | (1,916) | (2,285) | wider loss |
| Common stock + APIC | 93,126 | 131,371 | +41.1% |
| Shares outstanding (M) | 12,088 | 12,230 | +1.2% |

**Derived leverage/liquidity:**
- **Net cash = $242.5B − $101.1B = +$141.4B** (2.4x gross-debt coverage by liquid investments).
- Gross debt / annualized CFO (≈$169.7B) ≈ **0.6x** — conservative.
- Current ratio ≈ **2.3–2.4x** (approx.; current portion of operating leases not in window).
- **Total liabilities and total stockholders' equity were not returned in the fact window — book value and ROE cannot be verified from this data.** Do not assume figures.
- **AFS unrealized losses are trivially small**: $53.2B of securities in a loss position carry only **$0.42B** accumulated loss (~0.8% of the $99.5B portfolio), with $49.4B of that in the <12-month bucket. Duration/rate risk is immaterial.
- **Private-investment marks are now 13.5% of total assets** and more than doubled in six months. The **$22.8B deferred tax liability** is the embedded tax cost on those unrealized gains — a real claim on future cash if positions are monetized.

**Debt maturity profile (as disclosed at 2025-12-31, pre-2026 issuance):** $2.0B (2026), $1.0B (2027), $2.68B (2028), $1.76B (2029), $5.5B (2030), $36.1B beyond 2030. **No refinancing cliff**; the $52B of 2026 issuance extends duration rather than plugging a wall.

---

## 5. Cash flow — the story of the quarter

| Item ($M) | 1H2025 | 1H2026 | Δ |
|---|---:|---:|---:|
| **Operating cash flow** | 63,897 | **84,859** | **+32.8%** |
| Capex (PP&E purchases) | 39,643 | **80,598** | **+103.3%** |
| **Free cash flow** | **24,254** | **4,261** | **-82.4%** |
| FCF margin | 13.0% | **1.9%** | -1,110 bp |
| Capex / revenue | 21.2% | **35.1%** | +1,390 bp |
| Capex incurred but unpaid (period-end) | 10,635 | 29,113 | +173.8% |
| Purchases of marketable securities | 39,870 | 76,480 | +91.8% |
| Purchases of other (incl. private) investments | 2,312 | 22,051 | +853.7% |
| Net investing cash flow | (40,738) | (145,822) | +258% |
| Debt proceeds, net | 31,378 | 56,226 | +79.2% |
| Debt repayments | 18,397 | 5,253 | -71.4% |
| Common stock issuance | 0 | **30,499** | n/a |
| Convertible preferred issuance | 0 | **19,063** | n/a |
| Subsidiary minority proceeds | 400 | 3,758 | +840% |
| **Share repurchases** | **28,306** | **0** | **-100%** |
| Dividends paid | 4,977 | 5,231 | +5.1% |
| Net financing cash flow | (26,033) | **+86,320** | swing |
| Net change in cash | (2,430) | +25,203 | — |

**Quarterly split (derived):**

| | Q1 2026 | Q2 2026 |
|---|---:|---:|
| CFO | 45,790 | 39,069 |
| Capex | 35,674 | 44,924 |
| **FCF** | **+10,116** | **−5,855** |
| Capex / revenue | 32.5% | **37.5%** |

**Interpretation:** Cash generation is intact and improving operationally (+33% CFO), but the **entire FCF pool plus external capital is being recycled into infrastructure and investments**. Annualizing 1H capex implies **~$160B of 2026 capex**, and the $29.1B of accrued-but-unpaid capex means reported cash capex likely undershoots economic capex in 1H. A **negative FCF quarter** at Alphabet is a regime change for valuation models built on FCF-based multiples and for the buyback narrative.

---

## 6. Capital allocation — a structural shift

| | 1H2025 | 1H2026 | Signal |
|---|---:|---:|---|
| Buybacks | 28,306 | **0** | Multi-year share-shrink machine **halted** |
| Dividends | 4,977 | 5,231 | Maintained; DPS $0.41 → $0.43 |
| Preferred dividends | 0 | 86 | New claim introduced (June issuance) |
| Capex | 39,643 | 80,598 | Capex now the dominant use of capital |
| Acquisitions/other investments | ~2,300 | ~22,000 | Step-up in strategic deployment |
| External capital raised | ~700 | **109,600** | Debt + common + preferred + minorities |

**Payout math:** $5.23B dividends = **3.0% of reported net income** but **8.0% of core net income** — still comfortably covered. Buyback authorization is presumably intact but operationally dormant; **resumption (or lack thereof) at Q3 is a catalyst**.

**Dilution:** shares +142M (+1.2%) in six months via the $30.5B issuance and SBC; diluted count ~12.3B. Add the **$19.1B convertible preferred** and future dilution is a live overhang not present in Alphabet's historical model.

---

## 7. What the data implies about 1H2026 strategic activity

Four independent tags corroborate a major transaction, and I flag this as **inference, not disclosed fact**:
1. **$30.5B common stock issued** — Alphabet has not historically issued primary equity.
2. **$19.1B convertible preferred issued 2026-06-05** — first-of-its-kind for the company; $18.0B carrying value at quarter-end (≈5.4% issuance cost/discount).
3. **Gross finite-lived intangibles +$8.1B** and amortization +122% YoY — acquired intangibles entering the P&L.
4. **$135.9B fair-value gain with only $22.4B itemized as realized/unrealized** — the signature of remeasuring a previously held equity interest upon consolidation.

**Trading implication:** the $113.6B residual gain is almost certainly **non-recurring and non-cash**. Any screen or model using trailing GAAP EPS will value GOOGL at a misleadingly low multiple. Conversely, the acquired intangibles will create a **recurring amortization drag** in 2H2026 and beyond (disclosed forward amortization: $747M remainder of FY2026, $1.30B in the next twelve months, $1.14B/$1.10B/$1.06B in years 2–4).

---

## 8. Risks — ranked by materiality

1. **Capex-to-FCF conversion risk (highest).** Capex 35% of revenue, Q2 FCF negative, $29.1B accrued capex still to pay. If AI monetization lags, depreciation (+43% already) compresses margins and FCF stays depressed. Watch Q2's 209 bp QoQ margin compression as the early warning.
2. **Earnings-quality / multiple distortion.** 63% of 1H EPS is non-operating. A mark-to-market reversal or a smaller step-up gain in 2H would produce a jarring headline "earnings decline" even with stable operations.
3. **Private-mark concentration.** $124.3B (13.5% of assets) in Level 3 equity securities with $85.7B of cumulative upward revaluation. Model-based, illiquid, and a source of non-operating volatility. $22.8B deferred tax liability attached.
4. **Dilution and capital structure complexity.** Buyback paused, +1.2% share count, $19.1B convertible preferred with conversion terms not in the window. New claims rank ahead of common.
5. **Regulatory/legal.** Loss contingency accrual **$17.4B (+11.3%)**; the 10-K discloses a **$3.0B legal payment in Q3 2025**. Ongoing antitrust/privacy exposure remains a structural, not tail, risk.
6. **Rate/duration risk in the securities book.** Currently minor ($0.42B accumulated loss on $99.5B), but a $242B liquid portfolio means interest income ($2.8B in 1H) is now a modest earnings sensitivity to rate cuts.
7. **Data blind spots.** Segment mix, Cloud backlog, R&D intensity, goodwill, and total equity are unavailable — a segment-level thesis cannot be validated with this dataset.

---

## 9. Actionable conclusions for traders

**Directional view: fundamentally strong core, optically cheap headline, deteriorating cash conversion.** The operating business is performing better than at any point in the dataset (revenue +23%, gross margin +240 bp, operating margin +190 bp *despite* a 43% depreciation increase). But three things argue for discipline on entry and position sizing:

1. **Re-base valuation on core EPS (~$5.30 for 1H; ~$10.60 annualized run-rate), not GAAP $14.24.** Any "cheap P/E" screen on trailing GAAP is false. Also normalize for the higher 19.1% tax rate (vs 17.1%) and the +32% SBC step-up.
2. **Treat FCF as the swing factor for the multiple.** FCF margin of 1.9% vs 13.0% is the single largest change in the equity story. A credible path to positive Q3 FCF (capex discipline or CFO acceleration) is the bull catalyst; a second consecutive negative-FCF quarter likely pressures the stock regardless of revenue beats.
3. **Expect a noisy Q3 print.** With no repeat step-up gain modeled, consensus GAAP EPS must fall sharply QoQ (Q2's $9.11 → likely low-to-mid single digits). Headline "EPS collapse" headlines will be mechanical, not operational. Position ahead of that narrative, and trade the **core operating line and capex/FCF commentary**.

**Bull setup:** revenue growth accelerating (21.8% → 24.2%), margins expanding on scale, $141B net cash, $242B liquidity, contract liabilities +17%, and a private portfolio ($124B, up 94%) whose value is not reflected in operating earnings. Debt raise was pre-funding, not distress.

**Bear setup:** capex at 37.5% of Q2 revenue with negative Q2 FCF, buybacks at zero, share count rising, a new $19B preferred claim, $22.8B of deferred tax on unrealized marks, and 63% of reported earnings non-recurring. The company is now capital-hungry at exactly the moment its historic capital-return flywheel has stopped.

**Specific monitoring checklist into Q3 2026 (late October):**
- Q3 capex and any 2026/2027 capex framework (is $160B+ the new run-rate?)
- Q3 FCF sign; movement in "capex incurred but not yet paid" ($29.1B)
- Operating margin trajectory (34.0% in Q2 vs 36.1% in Q1)
- Cloud growth and contract liabilities ($10.1B)
- Any buyback resumption; diluted share count and preferred conversion terms
- Size/nature of any further fair-value gains; whether the $113.6B residual is confirmed one-time
- Legal accrual direction ($17.4B)

---

## 10. Data limitations (explicit)

| Item | Status |
|---|---|
| Insider transactions | **UNAVAILABLE** — the data package has no authorized point-in-time insider archive for GOOGL. No inference made; none should be drawn. |
| Revenue | **Derived** (Costs & Expenses + Operating Income); validated exactly against Q1/Q2 2025 |
| Total liabilities, total stockholders' equity, goodwill | **Not in returned window** — book value, ROE, and goodwill-adjusted leverage unverified |
| Segment revenue/margins, Cloud backlog, headcount, R&D line | **Not in returned window** |
| New filings in trailing 7 days | **None**; latest is the Q2 2026 10-Q accepted 2026-07-23 |
| Convertible preferred terms (conversion price, dividend rate) | **Not in returned window** |

---

## 11. Key points summary table

| Category | Metric | 1H2025 | 1H2026 | Change | Read-through |
|---|---|---:|---:|---:|---|
| **Growth** | Revenue (derived, $M) | 186,662 | 229,692 | **+23.1%** | Acceleration: Q1 +21.8%, Q2 +24.2% |
| **Growth** | Q2 revenue ($M) | 96,428 | 119,796 | +24.2% | +9.0% QoQ |
| **Profitability** | Gross margin | 59.6% | 62.0% | +240 bp | Scale + mix, despite depreciation |
| **Profitability** | Operating income ($M) | 61,877 | 80,466 | **+30.0%** | Margin +190 bp to 35.0% |
| **Profitability** | Q2 operating margin | 32.4% | 34.0% | +157 bp YoY | **−209 bp QoQ** — watch item |
| **Quality** | Non-operating income ($M) | 13,845 | 135,699 | +880% | 81% of pretax profit |
| **Quality** | Equity FV gain ($M) | 11,044 | 135,946 | nm | ~$113.6B not itemized → one-time |
| **Quality** | Reported diluted EPS | 5.12 | 14.24 | +178% | Heavily inflated |
| **Quality** | **Core diluted EPS (est.)** | **~4.29** | **~5.30** | **+23.6%** | The number to model |
| **Quality** | Non-core share of EPS | 16% | **63%** | +47 pt | GAAP multiple is misleading |
| **Tax** | Effective tax rate | 17.1% | 19.1% | +200 bp | Structural EPS headwind |
| **Costs** | SBC ($M) | 11,500 | 15,200 | +32.2% | 6.6% of revenue; dilution |
| **Costs** | Depreciation ($M) | 9,485 | 13,586 | +43.2% | AI fleet hitting P&L |
| **Costs** | Interest expense ($M) | 295 | 1,811 | +514% | Stemmed by $2.81B interest income |
| **Cash** | Operating cash flow ($M) | 63,897 | 84,859 | +32.8% | Healthy |
| **Cash** | Capex ($M) | 39,643 | 80,598 | **+103.3%** | 35.1% of revenue |
| **Cash** | **Free cash flow ($M)** | **24,254** | **4,261** | **−82.4%** | FCF margin 1.9% |
| **Cash** | Q2 2026 FCF ($M) | — | **−5,855** | nm | First negative-FCF quarter |
| **Cash** | Capex incurred, unpaid ($M) | 10,635 | 29,113 | +173.8% | 2H cash capex to rise |
| **Balance sheet** | Cash + ST investments ($M) | — | 242,474 | +91% YTD | Massive pre-funding |
| **Balance sheet** | Gross debt ($M) | — | 101,085 | +106% YTD | Net cash still +$141.4B |
| **Balance sheet** | Total assets ($M) | — | 921,983 | +54.9% YTD | +$326.7B in 6 months |
| **Balance sheet** | Private equity securities ($M) | — | 124,259 | +93.9% YTD | 13.5% of assets; illiquid |
| **Balance sheet** | Deferred tax liabilities ($M) | — | 22,819 | from 919 | Tax on unrealized gains |
| **Balance sheet** | Contract liabilities ($M) | — | 10,100 | +17.4% YTD | Forward-demand positive |
| **Balance sheet** | Legal accrual, current ($M) | — | 17,356 | +11.3% YTD | Structural regulatory risk |
| **Returns** | Buybacks ($M) | 28,306 | **0** | −100% | Share-shrink engine stopped |
| **Returns** | Dividends ($M) | 4,977 | 5,231 | +5.1% | 8.0% of core earnings |
| **Returns** | Diluted shares (M, approx.) | ~12,253 | ~12,267 | +0.1% | Plus $19.1B preferred overhang |
| **Returns** | Shares outstanding (M) | — | 12,230 | +1.2% YTD | Issuance + SBC |
| **Returns** | Adjusted ROA (annualized, est.) | — | ~17.1% | — | Reported ROA ~46% is inflated |
| **Insider** | Insider transactions | — | **N/A** | — | Data unavailable; not inferred |
| **Verdict** | **Stance** | — | **Constructive on operations / cautious on FCF-compounded valuation** | — | Trade core EPS, capex, and Q3 FCF — not headline GAAP |