# AMZN (Amazon.com, Inc.) — Fundamental Deep-Dive Report
**As of:** 2026-08-05 | **Most recent filing available:** Form 10-Q for Q2 2026 (period ended 2026-06-30), accepted 2026-07-31 (accn 0001018724-26-000026)

---

## 1. Data Provenance & Scope (read first)

- **Vendor extract:** point-in-time SEC XBRL facts, filtered by EDGAR acceptance time. The extract contains the **Q2 2026 10-Q and its FY2025/Q1-2026 comparatives only** — no FY2025 10-K line items, no segment P&L detail, no FY2024 figures beyond rolling comparatives.
- **Revenue is derived** (the vendor did not surface a revenue tag): `Revenue = OperatingIncomeLoss + CostsAndExpenses`. This derivation reconciles exactly to reported AMZN figures for the prior-year comparatives (Q2 2025 → $167,702M; H1 2025 → $323,369M), so I have high confidence in the 2026 numbers derived the same way.
- **Insider transactions: DATA_UNAVAILABLE.** The package has no authorized insider archive for AMZN as of 2026-08-05. I will not infer or fabricate insider activity.
- **No market price / share count-based valuation data** is in the extract, so I do **not** quote P/E, EV/EBITDA or price targets.
- Two XBRL tags in the extract are internally inconsistent (see §7 — "Flags"); I treat them as **data-quality caveats, not conclusions**.

---

## 2. Company Profile

Amazon.com, Inc. (NASDAQ: **AMZN**) operates three reportable segments (`NumberOfOperatingSegments = 3`, confirmed in the Q2 2026 filing): **North America**, **International**, and **Amazon Web Services (AWS)**. Revenue is a blend of online and physical stores, third-party seller services, advertising, subscription services, and cloud/infrastructure (AWS). The Q2 2026 filing also confirms an **energy-derivatives program of 270 million MWh notional in H1 2026** — a direct read-through to the scale of data-center power procurement supporting the AI/cloud build-out.

Basic share count: **10,783M outstanding (2026-06-30)**; **10,786.3M as of 2026-07-22**; diluted ~**10,895M** (implied from Q2 2026 EPS).

---

## 3. Income Statement — Revenue Acceleration + Real Operating Leverage

All figures **$ millions**, derived as described above.

| Metric | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 | Q2 YoY | H1 2025 | H1 2026 | H1 YoY |
|---|---|---|---|---|---|---|---|---|
| Revenue | 155,667 | 167,702 | 181,519 | **200,606** | **+19.6%** | 323,369 | **382,125** | **+18.2%** |
| COGS | 76,976 | 80,809 | 87,463 | 95,778 | +18.5% | 157,785 | 183,241 | +16.1% |
| Gross profit | 78,691 | 86,893 | 94,056 | 104,828 | +20.6% | 165,584 | 198,884 | +20.1% |
| **Gross margin** | 50.6% | 51.8% | 51.8% | **52.3%** | +50 bp | 51.2% | 52.1% | +90 bp |
| Marketing | 9,763 | 11,416 | 10,314 | 11,698 | +2.5% | 21,179 | 22,012 | +3.9% |
| G&A | 2,628 | 2,965 | 2,587 | 2,788 | −6.0% | 5,593 | 5,375 | −3.9% |
| **Operating income** | 18,405 | 19,171 | 23,852 | **27,461** | **+43.2%** | 37,576 | **51,313** | **+36.6%** |
| **Operating margin** | 11.8% | 11.4% | 13.1% | **13.7%** | +230 bp | 11.6% | **13.4%** | +180 bp |
| Nonoperating income | — | 1,686 | 15,982 | **53,396** | n.m. | 4,960 | **69,378** | n.m. |
| Pretax income | — | 20,857 | 39,834 | 80,857 | +288% | 42,536 | 120,691 | +184% |
| Tax | — | 2,678 | 9,560 | 18,199 | — | 7,231 | 27,759 | — |
| Effective tax rate | — | 12.8% | 24.0% | 22.5% | — | 17.0% | **23.0%** | +600 bp |
| **Net income** | 17,127 | 18,164 | 30,255 | **62,647** | +245% | 35,291 | **92,902** | +163% |
| **Diluted EPS** | ~1.59 | 1.68 | 2.78 | **5.75** | +242% | 3.27 | **8.53** | +161% |
| SBC | — | 6,534 | 4,032 | 6,038 | −7.6% | 10,223 | 10,070 | −1.5% |

### 3a. The headline number is NOT the operating number — decompose it

Q2 2026's $53.4B of nonoperating income is overwhelmingly **non-cash mark-ups on equity investments**:

- `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment`: **$50,486M in Q2 2026**, **$62,814M in H1 2026** (vs **$49M** in Q2 2025 and **$86M** in H1 2025).
- `EquitySecuritiesFvNiGainLoss`: +$1,300M Q2 / +$454M H1.
- Offsets: `FairValueAdjustmentOfWarrants` **−$1,449M** Q2 / −$1,051M H1; interest expense **$1,314M** Q2 (vs $516M a year ago, **+155%**); interest income $1,295M Q2.

**Ex-mark "core" earnings (my calculation, 22.5% tax on the delta):**

| | Q2 2026 | Q2 2025 | Change | H1 2026 | H1 2025 | Change |
|---|---|---|---|---|---|---|
| Pretax, as reported | 80,857 | 20,857 | +288% | 120,691 | 42,536 | +184% |
| Less: non-marketable equity mark-ups | (50,486) | (49) | — | (62,814) | (86) | — |
| Less: marketable equity MTM | (1,300) | (393) | — | (454) | (188) | — |
| **Core pretax** | **29,071** | **20,415** | **+42.4%** | **57,423** | **42,262** | **+35.9%** |
| **Core net income (~22.5–23% tax)** | **~22,530** | **~18,164** | **+24%** | **~44,000** | **~35,291** | **+25%** |
| **Core diluted EPS** | **~2.07** | **~1.68** | **+23%** | **~4.04** | **~3.27** | **+24%** |

**Actionable takeaway:** AMZN's *operating* story is genuinely strong and accelerating — Q2 operating income +43% on revenue +19.6%, with operating margin printing a record 13.7%. But **~62% of Q2 GAAP EPS ($5.75) and ~52% of H1 GAAP EPS ($8.53) is a non-cash investment revaluation** that can reverse. Any screen or consensus comparison using GAAP EPS is distorted; use ~$2.07 (Q2) / ~$4.04 (H1) as the run-rate earnings base.

### 3b. Why operating leverage is real, not accounting
- **Marketing fell to 5.83% of revenue** (from 6.81% in Q2 2025) — growth is being pulled by demand/AWS, not paid acquisition.
- **G&A declined in absolute dollars** (−6.0% YoY).
- **SBC is flat to down** (H1: $10,070M vs $10,223M) despite 18% revenue growth — notable discipline; total unrecognized SBC $24.8B.
- Revenue is compounding **sequentially faster than last year**: Q2/Q1 = **+10.5%** in 2026 vs **+7.7%** in 2025.
- Offset/risk: **D&A is ramping hard** — Q2 2026 depreciation $13,869M (+42% YoY), total D&A $19,988M (+31% YoY); TTM D&A **$75,200M** (+28.4%). The capex wave in §6 becomes a P&L headwind in 2027+.

---

## 4. Balance Sheet — $1 Trillion Asset Base, Debt Nearly Doubled

| Item ($M) | 2025-12-31 | 2026-06-30 | Change |
|---|---|---|---|
| Cash & equivalents | 86,810 | 78,213 | −9.9% |
| Marketable (AFS) securities | 45,800 | 97,900 | **+113.8%** |
| **Cash + AFS liquidity** | **132,610** | **176,113** | **+32.8%** |
| Accounts receivable, net | 67,729 | 88,092 | +30.1% |
| Inventory, net | 38,325 | 38,184 | −0.4% |
| Current assets | 229,083 | 249,264 | +8.8% |
| Equity securities w/o RDFV | 16,200 | **122,300** | **+655%** |
| Operating lease ROU asset | 86,054 | 92,743 | +7.8% |
| **Total assets** | **818,042** | **1,095,689** | **+33.9%** |
| Accounts payable | 121,909 | 147,440 | +21.0% |
| Accrued liabilities | 75,520 | 73,406 | −2.8% |
| Current liabilities | 218,005 | 241,274 | +10.7% |
| Long-term debt — current | 2,748 | 3,330 | +21.2% |
| Long-term debt — noncurrent | 65,648 | 128,894 | **+96.3%** |
| **Total debt** | **68,396** | **132,224** | **+93.3%** |
| Operating lease liability | 89,252 | 96,320 | +7.9% |
| Finance lease liability | 12,286 | 13,451 | +9.5% |
| AOCI | 28,230 | 66,287 | +38,057 |
| Additional paid-in capital | 140,024 | 149,619 | +6.9% |
| Shares outstanding (M) | 10,731 | 10,783 | +0.5% |

**Liquidity & leverage read:**
- **Net cash position is still positive:** $176.1B liquidity vs $132.2B debt = **+$43.9B net cash**. But this is the *first* time in years that net cash has narrowed materially — it was +$64.2B at 2025-12-31.
- **Including leases**, total fixed obligations = $242.0B ($132.2B debt + $96.3B operating leases + $13.5B finance leases). Contractual obligations disclosed at **$650.0B total**, of which **$78.1B due within 12 months** and $42.8B in the remainder of FY2026.
- **Current ratio: 1.03x** (249,264 / 241,274); **quick ratio ~0.87x**. Historically normal for AMZN, but the buffer is thinner than at year-end (1.05x) because cash was redeployed into capex, M&A and securities.
- **Working capital is a funding source, not a drag:** AR +$20.4B but AP +$25.5B — negative working capital continues to subsidize the build-out. Receivables growth (+30%, well ahead of +18% revenue) plus a rising allowance ($2.4B → $2.8B) is worth a second look, but is consistent with an advertising/cloud mix shift.
- **Book equity rose sharply** on $92.9B of H1 net income plus $38.1B of OCI. Equity is not fully disclosed in the extract (total liabilities line isn't surfaced), but a residual upper bound is **~$631B** ($1,095.7B assets less $241.3B current liabilities, $128.9B LT debt, $82.6B noncurrent operating leases, $11.8B noncurrent finance leases, before other noncurrent liabilities).

---

## 5. Cash Flow — Operating Cash Is Exploding; Free Cash Flow Is Negative

| TTM (Jul–Jun, $M) | TTM to 2025-06-30 | TTM to 2026-06-30 | Change |
|---|---|---|---|
| Operating cash flow | 121,137 | **161,403** | **+33.2%** |
| Capex (productive assets) | 107,656 | **173,028** | **+60.7%** |
| **Free cash flow** | **+13,481** | **−11,625** | **−$25.1B swing** |
| Business acquisitions, net of cash | 4,809 | **41,956** | +772% |
| Net investing cash flow | (123,569) | (216,775) | — |
| Net financing cash flow | (8,652) | **+75,160** | — |
| D&A | 58,562 | 75,200 | +28.4% |
| Cash taxes paid | 11,788 | 6,635 | −43.7% |
| Net income | 70,623 | 135,281 | +91.6% |

| H1 comparison ($M) | H1 2025 | H1 2026 | Change |
|---|---|---|---|
| Operating cash flow | 49,530 | 71,419 | **+44.2%** |
| Capex | 57,202 | 98,411 | **+72.0%** |
| **Free cash flow** | **(7,672)** | **(26,992)** | worse |
| Acquisitions | 1,652 | **39,767** | +2,307% |
| LT debt issued | 746 | 66,998 | — |
| ST debt net | +434 | −296 | — |
| LT debt repaid | (2,751) | (2,752) | — |
| Finance lease principal | (821) | (863) | — |
| Net change in cash | (20,859) | (9,179) | improved |

**Quarterly cadence:** Q1 2026 OCF $26,032M / capex $44,203M (FCF **−$18,171M**); Q2 2026 OCF $45,387M / capex $54,208M (FCF **−$8,821M**). Q2's operating cash generation improved 74% sequentially and more than offset half of the capex step-up — a genuinely constructive signal.

**Key insight for traders:** AMZN is funding an **AI infrastructure super-cycle entirely off the income statement and the bond market**, not off FCF. The financial architecture of the story:
1. **Cash taxes paid collapsed to $6.6B TTM vs $11.8B** (deferred tax expense +$41.4B TTM) — accelerated depreciation on capex is shielding cash taxes. This is a *real* cash benefit, but it caps out.
2. **Debt issuance is the marginal funding source** ($82.0B LT + $20.8B ST issued TTM) — interest expense already +155% YoY and will keep climbing as the $129B noncurrent stack reprices.
3. **$42.0B of M&A TTM** (of which $39.8B in H1 2026, $24.4B in Q2 alone) plus **$106B of equity-stake accumulation** — capital is being deployed into AI ecosystem positions, and management is marking those positions up aggressively.

---

## 6. Segment / Operating Detail Available in the Extract

- **Three segments confirmed** (North America, International, AWS); segment-level revenue/operating income is **not present** in the vendor extract. This is the single biggest analytical gap — AWS margin and growth are the swing variables for the whole thesis and must be sourced from the 10-Q/10-K text or the earnings release.
- **Deferred revenue (contract liabilities):** $20,428M current + $4,500M noncurrent = **$24,928M**; $15.2B of H1 2026 revenue came from the opening contract-liability balance — healthy backlog conversion, and roughly flat QoQ (no deterioration in forward-booked demand).
- **Energy derivatives:** $705M derivative assets (from $112M), 270M MWh notional traded in H1 2026 → power hedging for data centers is now a first-order financial exposure.
- **Goodwill/intangibles** are not surfaced in the extract despite $39.8B of H1 acquisitions — a key item to verify (impairment risk if AI assets are marked optimistically).

---

## 7. Flags, Anomalies & Data-Quality Warnings

1. **⚠ ~$38.1B of OCI is unexplained by the disclosed components.** AOCI rose from $28,230M to $66,287M (+$38,057M) while the extract shows FX translation of only **−$1,563M** and `MarketableSecuritiesUnrealizedGainLoss` of just **+$430M**. Combined with the **$106.1B increase in equity securities without readily determinable fair value** (16,200 → 122,300) *and* $62.8B of income-statement mark-ups, the most coherent reading is that **a large strategic (AI-ecosystem) equity position was revalued, with one portion routed through the P&L (~$63B) and another through OCI (~$38–40B)**. Net effect: **~$100B+ of the $278B increase in total assets is investment revaluation, not operating asset creation.** Verify against the 10-Q equity statement before underwriting book value.
2. **⚠ `DebtSecuritiesAvailableForSaleUnrealizedGainLoss` = $92,000M for H1 2026** (and $39,500M for FY2025) is **incompatible** with the balance-sheet AFS disclosure (gross unrealized gain of **$7M**, loss of $67M, against $97.9B of AFS securities). Treat this tag as mis-mapped/erroneous. Do not model it.
3. **GAAP EPS quality:** ~52% of H1 2026 EPS is non-cash mark-ups. Model on ~$4.04 H1 core EPS.
4. **Tax rate normalization:** effective rate 23.0% H1 2026 vs 17.0% H1 2025 — a structural headwind to reported EPS growth even before the mark-ups.
5. **Insider data unavailable** — no authorized archive. Cannot assess management conviction/selling. Flag for the next agent to source from Form 4s.
6. **No annual (10-K) history in the extract** — I cannot build a multi-year margin or segment table. My longest clean series is 4 quarters + 2 H1 staircases.

---

## 8. Actionable Conclusions for Traders

**Bull case (evidence-based):**
- Revenue growth **accelerating** to +19.6% YoY on a ~$800B annualized run-rate — remarkable at this scale; Q2/Q1 sequential +10.5% vs +7.7% a year ago.
- **Operating margin break-out: 13.7% in Q2, 230 bp of YoY expansion**, with gross margin at 52.3% and marketing/G&A falling as a % of revenue. Operating income +43% YoY on +20% revenue = true operating leverage.
- **Operating cash flow +44% YoY in H1** to $71.4B, with cash taxes down 44% — the cash engine is accelerating faster than the P&L.
- $43.9B net cash, $176B liquidity, deferred revenue stable at $24.9B → no near-term funding stress.
- SBC flat-to-down while revenue grows 18% → genuine per-share value creation.

**Bear case / risks to underwrite:**
- **FCF has turned negative (−$26.99B in H1; −$11.6B TTM) and capex is up 72% YoY.** At a $173B TTM capex run-rate, capex is now **>107% of operating cash flow**. If AI demand signals soften, the depreciation tail (already +31% YoY) crushes margins for 4–8 quarters regardless of revenue.
- **Total debt doubled to $132.2B in six months** and interest expense is +155% YoY. Adding leases, fixed obligations are $242B. Refinancing risk is low today, but the trend is un-Amazon-like.
- **Earnings quality:** GAAP EPS is majority non-cash marks. A single downward revaluation of the ~$122B non-marketable equity book would create a violent reported-EPS air pocket — and the same book value is now $66.3B AOCI-dependent.
- **Receivables +30% vs revenue +18%**, allowance up 17% — monitor for advertising/cloud collection slippage.
- **$42B of unexplained-scale M&A in 12 months** — integration and goodwill impairment risk is not yet testable from this extract.

**What I would monitor into the next print (Q3 2026):**
1. Operating margin — does it hold >13%? A print below 12.5% breaks the leverage narrative.
2. Capex guidance vs the $173B TTM trend — any *cut* is bullish for FCF, any *raise* without revenue acceleration is bearish.
3. Interest expense line (>$1.3B/qtr and rising) and any further debt issuance.
4. Any reversal/lower mark on the equity-securities book.
5. Segment disclosure for AWS — the extract cannot answer the most important question; get it from the filing text.

**Bottom line:** Fundamentally, **AMZN's operating engine is the strongest it has been — accelerating top line, record operating margin, cash-tax-shielded operating cash flow, and flat SBC.** The accounting is doing a lot of the talking on the bottom line, and the balance sheet is being levered aggressively to fund an AI capex super-cycle that has already pushed FCF negative. **Trade the operating margin and OCF lines, not the GAAP EPS line.** Insiders and valuation remain unassessable with the tools available; the next agent should source Form 4s and current pricing before sizing a position.

---

## 9. Key-Points Summary Table

| Category | Metric | Latest (Q2 2026 / 2026-06-30) | Prior-year / Prior-period | Direction | Trader Read |
|---|---|---|---|---|---|
| Income | Revenue | $200,606M | $167,702M (Q2 2025) | **+19.6% YoY** | Acceleration > Q1's +16.6% |
| Income | Gross margin | 52.3% | 51.8% | +50 bp | Mix shift to AWS/ads |
| Income | Operating income | $27,461M | $19,171M | **+43.2%** | True operating leverage |
| Income | Operating margin | 13.7% | 11.4% | **+230 bp** | Record-level; watch D&A drag |
| Income | GAAP diluted EPS | $5.75 | $1.68 | +242% | **Majority is non-cash marks** |
| Income | Core EPS (ex-mark, est.) | ~$2.07 | ~$1.68 | **+23%** | The real run-rate |
| Income | H1 2026 GAAP EPS | $8.53 | $3.27 | +161% | Core H1 ≈ $4.04 (+24%) |
| Income | Non-marketable equity mark-up | $50,486M (Q2) | $49M | n.m. | $62.8B in H1; reversible |
| Income | Effective tax rate (H1) | 23.0% | 17.0% | +600 bp | Structural EPS headwind |
| Income | SBC (H1) | $10,070M | $10,223M | −1.5% | Discipline; $24.8B unrecognized |
| Balance sheet | Total assets | $1,095,689M | $818,042M (YE25) | **+33.9%** | ~$100B+ is revaluation |
| Balance sheet | Cash + AFS | $176,113M | $132,610M | +32.8% | Ample liquidity |
| Balance sheet | Total debt | $132,224M | $68,396M | **+93.3%** | Leverage step-change |
| Balance sheet | Net cash | +$43,889M | +$64,214M | Narrowing | Still positive, trending down |
| Balance sheet | Equity securities w/o RDFV | $122,300M | $16,200M | +655% | Largest single risk factor |
| Balance sheet | AOCI | $66,287M | $28,230M | +$38.1B | ~$38B unexplained (§7) |
| Balance sheet | Current ratio | 1.03x | 1.05x | Stable | Thin but normal for AMZN |
| Cash flow | OCF (H1) | $71,419M | $49,530M | **+44.2%** | Cash engine accelerating |
| Cash flow | Capex (H1) | $98,411M | $57,202M | **+72.0%** | AI super-cycle |
| Cash flow | FCF (H1) | −$26,992M | −$7,672M | Worse | **The core bear argument** |
| Cash flow | FCF (TTM) | −$11,625M | +$13,481M | Negative | Capex > OCF (107%) |
| Cash flow | D&A (TTM) | $75,200M | $58,562M | +28.4% | Depreciation wave building |
| Cash flow | Cash taxes paid (TTM) | $6,635M | $11,788M | −43.7% | Real cash shield from capex |
| Cash flow | M&A (TTM) | $41,956M | $4,809M | +772% | Integration/impairment unknown |
| Cash flow | Interest expense (Q2) | $1,314M | $516M | **+155%** | Rising debt cost |
| Other | Deferred revenue | $24,928M | ~flat QoQ | Stable | No demand deterioration |
| Other | Contractual obligations (12 mo) | $78,084M | — | — | Manageable vs $71B H1 OCF |
| Other | Diluted shares (implied) | ~10,895M | — | +0.5% | Negligible dilution |
| Data gaps | Insider transactions | **UNAVAILABLE** | — | — | Must source Form 4s elsewhere |
| Data gaps | Segment (AWS) P&L | **NOT IN EXTRACT** | — | — | Critical missing variable |
| Data gaps | Market price / valuation | **NOT IN EXTRACT** | — | — | No multiples quoted |