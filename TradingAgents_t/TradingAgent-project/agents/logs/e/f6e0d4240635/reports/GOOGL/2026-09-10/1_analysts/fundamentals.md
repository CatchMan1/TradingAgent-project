# GOOGL — Alphabet Inc. | Fundamental Research Report
**As of:** 2026-09-10 | **Latest filed period:** Q2 2026 (quarter ended 2026-06-30), Form 10-Q accepted 2026-07-23 | **FY2025 10-K:** accepted 2026-02-05

---

## 1. Executive Summary

GOOGL's most recent filing shows a company in the middle of a **violent capital-intensity regime change**, layered on top of an **accelerating core operating business**:

- **Revenue growth accelerated to +24.2% YoY in Q2 2026** (vs +21.8% in Q1 2026), with H1 2026 revenue of **~$229.7B** (+23.1%).
- **Core operating leverage is still positive**: H1 operating income +30.0% to **$80.5B**, operating margin **35.0%** (+188 bps YoY), gross margin **62.0%** (+242 bps).
- **Headline EPS is almost entirely an investment-marking artifact.** H1 2026 net income of **$174.8B** includes **~$135.9B of equity-securities gains** booked through non-operating income. Q2 2026 is worse: **$98.0B of $112.2B** net income came from non-operating items (**~87%**). Reported diluted EPS of **$9.11** in Q2 is *not* an operating earnings number.
- **Free cash flow has broken down.** H1 2026 FCF = **$4.26B vs $24.25B** a year ago (**−82%**). **Q2 2026 FCF was negative at −$5.86B** — capex ($44.9B) exceeded operating cash flow ($39.1B) for the first time in the dataset.
- **Capital allocation has flipped from return-of-capital to raise-capital.** Buybacks went from **$28.3B in H1 2025 to exactly $0 in H1 2026**; the company instead raised **$56.2B of debt, $30.5B of common equity, $19.1B of convertible preferred, and $3.8B from minority holders** in six months. Net debt capacity is still large ($141B net cash), but leverage and dilution are moving in the wrong direction.
- **The balance sheet doubled in size in six months**: total assets **$595.3B → $922.0B (+54.9%)**, driven by cash/securities (+$115.6B), private equity stakes (+$60.2B), capex, and a **$21.9B jump in deferred tax liabilities**.

**Bottom line:** Operationally this is a *stronger-than-expected* franchise; financially it is a *lower-quality earnings print* with a *negative-FCF capex super-cycle* funded by debt and equity. Traders should separate the operating signal (bullish) from the earnings-quality and cash-flow signal (bearish/volatility-inducing).

---

## 2. Data Provenance & Important Caveats

| Item | Detail |
|---|---|
| Source | Point-in-time SEC fundamental facts, filtered by actual EDGAR acceptance timestamp |
| Latest filing | 10-Q, accession 0001652044-26-000071, accepted **2026-07-23** |
| Prior 10-Q | Accession 0001652044-26-000048, accepted **2026-04-30** |
| FY2025 10-K | Accession 0001652044-26-000018, accepted **2026-02-05** |
| Fiscal year | Calendar year (Dec 31) |
| **Known data limitation** | The vendor's tag set is **truncated alphabetically** (roughly through "Finite…"/"Operating…"). Direct tags for **Revenues, R&D expense, sales & marketing, PP&E, goodwill, stockholders' equity, long-term debt split, and shares-based market data were not returned.** |
| Derived line items | **Revenue is derived exactly** as `CostsAndExpenses + OperatingIncomeLoss` (an accounting identity in Alphabet's P&L). R&D + S&M is derived as `Total costs − Cost of revenue − G&A`. These are labeled "derived" throughout. |
| **Not available** | Share price, market cap, P/E, EV, consensus estimates, segment revenue, and **insider transactions** (explicitly returned as `DATA_UNAVAILABLE` — no authorized point-in-time archive; no insider activity is inferred or fabricated). |

---

## 3. Company Profile

Alphabet Inc. is the parent of Google and is listed under **GOOGL** (Class A common stock; Class C trades as GOOG). The company monetizes internet search and advertising, YouTube advertising and subscriptions, Google Cloud (infrastructure and enterprise AI/software), Google Play and hardware, and a portfolio of "Other Bets" ventures. Its cost structure is increasingly dominated by **AI compute infrastructure** — servers, data centers, networking, and energy — which is the direct cause of the capex explosion documented in Section 7. *(Profile is contextual; all financial figures below are tool-derived.)*

---

## 4. Income Statement — Q2 and H1 2026

### 4.1 Headline table ($ millions)

| Metric | Q2 2026 | Q2 2025 | Δ YoY | H1 2026 | H1 2025 | Δ YoY |
|---|---:|---:|---:|---:|---:|---:|
| Revenue *(derived)* | **119,796** | 96,428 | **+24.2%** | **229,692** | 186,662 | **+23.1%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| Gross profit *(derived)* | **73,853** | 57,389 | **+28.7%** | **142,478** | 111,262 | **+28.1%** |
| Gross margin | **61.6%** | 59.5% | +212 bps | **62.0%** | 59.6% | +242 bps |
| R&D + S&M *(derived, combined)* | 26,622 | 20,909 | +27.3% | 51,260 | 40,637 | +26.1% |
| G&A | 6,461 | 5,209 | +24.0% | 10,752 | 8,748 | +22.9% |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 149,226 | 124,785 | +19.6% |
| **Operating income** | **40,770** | 31,271 | **+30.4%** | **80,466** | 61,877 | **+30.0%** |
| **Operating margin** | **34.0%** | 32.4% | +160 bps | **35.0%** | 33.2% | +188 bps |
| Non-operating income | **97,983** | 2,662 | +3,580% | **135,699** | 13,845 | +880% |
| Pre-tax income | 138,753 | 33,933 | +308.9% | 216,165 | 75,722 | +185.5% |
| Income tax | 26,560 | 5,737 | +362.9% | 41,394 | 12,986 | +218.8% |
| Effective tax rate | **19.1%** | 16.9% | +220 bps | **19.1%** | 17.1% | +200 bps |
| **Net income** | **112,193** | 28,196 | **+297.9%** | **174,771** | 62,736 | **+178.6%** |
| Net income to common | 112,107 | 28,196 | +297.6% | 174,685 | 62,736 | +178.4% |
| **Diluted EPS** | **$9.11** | $2.31 | +294.4% | **$14.24** | $5.12 | +178.1% |
| Basic EPS | $9.23 | $2.33 | +296.1% | $14.41 | $5.16 | +179.3% |

**Q1 2026 derived for trend continuity:** Revenue **$109,896** (+21.8% YoY), operating income **$39,696** (36.1% margin), non-operating income **$37,716**, net income **$62,578**, diluted EPS **$5.13**.

### 4.2 What the operating numbers actually say (bullish)

1. **Revenue is re-accelerating, not decelerating.** Q1 +21.8% → Q2 +24.2% YoY; Q2 revenue rose **+9.0% sequentially** ($109.9B → $119.8B). For a business of this size, that is a genuine demand signal.
2. **Gross margin expansion of 212–242 bps is the standout.** Cost of revenue grew only +15.7% against +23.1% revenue growth in H1. That implies pricing/mix (cloud, AI-enabled products, higher ad yield) is currently outrunning AI compute depreciation. **This is the single most important competitive datapoint in the filing.**
3. **Operating leverage is real but narrowing.** H1 operating margin +188 bps, but Q2 +160 bps vs Q1 +220 bps. R&D+S&M grew +27.3% in Q2, faster than revenue (+24.2%), and D&A rose **+43.2% in H1** ($13.59B vs $9.49B). *The margin tailwind is being eaten by the capex cycle quarter by quarter.*
4. **G&A is well controlled** at +22.9%, slightly below revenue growth.

### 4.3 What the headline EPS does *not* say (bearish / quality warning)

| Earnings-quality decomposition ($M) | H1 2026 | H1 2025 |
|---|---:|---:|
| Equity securities gains (FV-NI) | **135,946** | 11,044 |
| — of which unrealized | 21,531 | 1,088 |
| — of which realized | 836 | 435 |
| Interest income | 2,811 | 2,051 |
| Interest expense | (1,811) | (295) |
| FX / other | (14) | (175) |
| **Total non-operating income** | **135,699** | **13,845** |
| Non-operating as % of pre-tax income | **62.8%** | 18.3% |
| Non-operating as % of net income | **77.6%** | 22.1% |

**Critical observations:**
- **~78% of H1 2026 net income and ~87% of Q2 2026 net income is non-operating.** Strip it out and Q2 2026 "core" net income is roughly **$32.9B** (operating income × (1 − 19.1%)), versus **$26.0B** in Q2 2025 — still a healthy **+26%**, but a fraction of the reported +298%.
- There is a **discrepancy inside the gain disclosure**: total equity-securities gain of $135.9B vs only $21.5B unrealized + $0.8B realized = $22.4B accounted for. The gap (~$113.5B) suggests a **large one-time remeasurement/consolidation event** (e.g., a stake revaluation or step-acquisition) rather than ordinary mark-to-market. **This is non-recurring in nature and should be fully excluded from run-rate earnings.**
- **Tax rate stepped up 200 bps to 19.1%.** Of the $41.4B H1 tax charge, **$27.5B was deferred** (vs a $1.6B deferred *benefit* last year) — i.e., two-thirds of the tax expense is non-cash, tied to unrealized investment gains and accelerated depreciation. Cash taxes are lower than the P&L suggests, but the higher structural rate is a genuine EPS headwind.
- **SBC is growing faster than revenue**: $15.2B vs $11.5B (**+32.2%**), or **6.6% of revenue** vs 6.2%. Combined with +1.2% share count growth, per-share value capture is diluting at the margin.

---

## 5. Balance Sheet — A Doubling in Six Months

### 5.1 Comparative balance sheet ($ millions)

| Line item | 2026-06-30 | 2025-12-31 | Change | % |
|---|---:|---:|---:|---:|
| Cash & equivalents | 55,911 | 30,708 | +25,203 | +82.1% |
| **Cash + short-term investments** | **242,474** | 126,843 | **+115,631** | **+91.2%** |
| Available-for-sale debt securities | 99,500 | n/a | — | — |
| Accounts receivable, net | 69,175 | 62,886 | +6,289 | +10.0% |
| **Current assets** | **343,524** | 206,038 | **+137,486** | **+66.7%** |
| Equity securities w/o readily determinable FV | **124,259** | 64,094 | **+60,165** | **+93.9%** |
| — cumulative upward adjustment | 85,732 | 44,485 | +41,247 | +92.7% |
| — cumulative downward adjustment | (9,115) | (8,820) | −295 | −3.3% |
| **Total assets** | **921,983** | 595,281 | **+326,702** | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +8,058 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +17,457 | +31.4% |
| Accrued income taxes, current | 5,233 | 523 | +4,710 | +900.6% |
| Employee-related liabilities | 15,086 | 17,546 | −2,460 | −14.0% |
| Loss contingency accrual, current | 17,356 | 15,594 | +1,762 | +11.3% |
| Contract liabilities (deferred revenue) | 10,100 | 8,600 | +1,500 | +17.4% |
| **Debt (carrying)** | **101,085** | 49,085 | **+52,000** | **+106.0%** |
| Deferred tax liabilities, net | **22,819** | 919 | +21,900 | +2,383% |
| Deferred tax assets, net | 1,448 | 9,113 | −7,665 | −84.1% |
| Operating lease liability | 18,037 | 15,954 | +2,083 | +13.1% |
| Finance lease liability | 2,590 | 2,500 | +90 | +3.6% |
| Accrued income taxes, noncurrent | 11,306 | 9,531 | +1,775 | +18.6% |
| **Convertible preferred stock** | **18,023** | 0 | +18,023 | n/m |
| Common stock + APIC | 131,371 | 93,126 | +38,245 | +41.1% |
| AOCI | (2,285) | (1,916) | −369 | −19.3% |
| **Shares outstanding (M)** | **12,230** | 12,088 | +142 | +1.17% |

### 5.2 Liquidity and leverage — still strong, but deteriorating fast

| Leverage / liquidity metric | 2026-06-30 | 2025-12-31 |
|---|---:|---:|
| Cash + ST investments | $242.5B | $126.8B |
| Total debt (carrying) | $101.1B | $49.1B |
| **Net cash (cash+ST inv − debt)** | **+$141.4B** | +$77.8B |
| Net cash less leases & preferred | ~+$102.8B | ~+$59.3B |
| Debt / cash+ST investments | 0.42x | 0.39x |
| Interest expense (H1) | $1,811M | $295M |
| Operating income / interest expense | **44.4x** | 209.8x |

**Read:** Net cash *improved* to $141B because the company raised more than it spent — but that is a financing-driven improvement, not an operating one. **Interest expense rose 6.1x YoY**, and interest coverage fell from ~210x to ~44x. Still investment-grade-cushioned, but the direction of travel is unambiguous.

### 5.3 Three balance-sheet flags a trader must not ignore

1. **The $60.2B jump in private ("no readily determinable fair value") equity securities**, with cumulative upward adjustments up $41.2B, is the source of much of the reported gain. **This is Level 3 valuation — opaque, mark-to-model, and potentially reversible.** It is also why deferred tax liabilities ballooned $21.9B and deferred tax assets collapsed 84%. If private-market marks compress, the P&L and the deferred tax line reverse together.
2. **Working-capital liabilities are inflating much faster than revenue**: AP +66%, accrued liabilities +31%, current income taxes payable +901%. Some is timing (accrued capex — see below), but it flatters reported operating cash flow and warrants scrutiny of the Q3 cash conversion.
3. **Legal accruals are creeping up** ($15.6B → $17.4B current loss contingency; the FY2025 10-K discloses a **$3.0B contingency payment in Q3 2025**). This is a recurring, non-operating drag with tail risk.

### 5.4 Investment portfolio marks — early stress signal

| AFS debt securities in unrealized loss | 2026-06-30 | 2025-12-31 |
|---|---:|---:|
| Securities in loss position | $53,239M | $13,160M |
| Accumulated unrealized loss | $416M | $178M |
| — in loss < 12 months | $49,351M | $6,522M |
| — in loss > 12 months | $3,888M | $6,638M |

The **4x increase in the dollar value of bonds trading below cost** (concentrated in positions held <12 months) points to a **rates-driven mark-to-market headwind** in Q2/Q3 2026. AOCI is still only −$2.3B, so it is not yet material to book value — but it removes a source of non-operating income that has flattered EPS.

---

## 6. Cash Flow — The Most Important Section

### 6.1 Cash flow statement ($ millions)

| Item | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | Δ H1 |
|---|---:|---:|---:|---:|---:|
| **Operating cash flow** | **39,069** | 27,747 | **84,859** | 63,897 | **+32.8%** |
| Capex (PP&E purchases) | (44,924) | (22,446) | **(80,598)** | (39,643) | **+103.3%** |
| **Free cash flow** | **(5,855)** | **+5,301** | **4,261** | **24,254** | **−82.4%** |
| Purchases of marketable securities | n/d | n/d | (76,480) | (39,870) | +91.8% |
| Sales/maturities of marketable securities | n/d | n/d | 66,696 | 40,930 | +62.9% |
| Purchases of other investments | n/d | n/d | **(22,051)** | (2,312) | **+853.7%** |
| **Investing cash flow** | n/d | n/d | **(145,822)** | (40,738) | +258.0% |
| Debt proceeds, net | n/d | n/d | +56,226 | +31,378 | +79.2% |
| Debt repayments | n/d | n/d | (5,253) | (18,397) | −71.4% |
| Common stock issuance | — | — | **+30,499** | 0 | n/m |
| Convertible preferred issuance | — | — | **+19,063** | 0 | n/m |
| Minority interest proceeds | n/d | n/d | +3,758 | +400 | +839.5% |
| **Share repurchases** | **0** | 13,238 | **0** | **(28,306)** | **n/m** |
| Dividends paid | (2,689) | (2,543) | (5,231) | (4,977) | +5.1% |
| **Financing cash flow** | n/d | n/d | **+86,320** | (26,033) | n/m |
| FX effect on cash | n/d | n/d | (154) | 444 | n/m |
| **Net change in cash** | n/d | n/d | **+25,203** | (2,430) | n/m |

### 6.2 The FCF inflection ($ millions, derived)

| | Q1 2026 | Q2 2026 | H1 2026 |
|---|---:|---:|---:|
| Operating cash flow | 45,790 | 39,069 | 84,859 |
| Capex | (35,674) | (44,924) | (80,598) |
| **FCF** | **+10,116** | **−5,855** | **+4,261** |
| FCF margin | 9.2% | **−4.9%** | 1.9% |
| Capex / revenue | 32.5% | **37.5%** | **35.1%** |

**Prior-year comparison:** Q1 2025 FCF +$18,953M (21.0% margin); Q2 2025 +$5,301M (5.5%); H1 2025 $24,254M (13.0%). **Capex/revenue has gone from 21.2% to 35.1% in twelve months.**

### 6.3 Interpretation

- **Operating cash flow quality is fine, arguably good.** CFO grew +32.8%, *faster* than revenue, despite a $135.9B non-cash investment gain being removed in the reconciliation. Adjusted for that gain, **cash conversion against "core" net income of ~$65.1B is ~1.30x** — healthy.
- **The problem is 100% capital deployment.** Capex **more than doubled** (+103%) and "other investments" purchases rose **9.5x** to $22.1B — GOOGL is now writing large equity checks into external AI/infrastructure assets *and* building internally.
- **Q2 2026 is the first negative-FCF quarter in this dataset.** At the H1 run-rate, FY2026 capex annualizes to **~$161B**, versus $39.6B in H1 2025 alone. **Unpaid capex already accrued stands at $29.1B (vs $10.6B a year ago)**, meaning Q3 2026 cash capex will be *higher* than Q3 P&L capex — a mechanical FCF headwind next quarter.
- **The company has responded by changing its capital structure, not its spending.** Over six months: **+$56.2B debt, +$30.5B common equity, +$19.1B convertible preferred, +$3.8B minority capital = ~$109.6B raised**, while **buybacks went to zero** and dividends were maintained (+5%). This is the single clearest signal of management's priorities: *fund the AI build at any cost, including dilution.*

---

## 7. Capital Allocation & Shareholder Returns

| Capital return metric | H1 2026 | H1 2025 | Change |
|---|---:|---:|---:|
| Share repurchases | **$0** | $28,306M | **−100%** |
| Common dividends paid | $5,231M | $4,977M | +5.1% |
| Preferred dividends paid | $86M | $0 | n/m |
| Dividend per share declared (quarterly) | $0.22 | $0.21 | +4.8% |
| H1 DPS declared | $0.43 | $0.41 | +4.9% |
| **Total shareholder returns** | **$5,317M** | $33,283M | **−84.0%** |
| Proceeds from equity issuance | $30,499M | $0 | n/m |
| **Net shareholder return** | **−$44,245M (net issuance)** | +$33,283M | n/m |

**Share count:** 12,088M → 12,230M (**+142M, +1.17%**), plus **$18.0B of convertible preferred** creating additional future dilution. Implied Q2 2026 diluted shares ≈ 12,306M vs 12,206M in Q2 2025.

**Trader takeaway:** The **buyback bid that supported GOOGL's EPS growth in 2023–2025 has been withdrawn**. EPS growth from here must come from operations, not share shrinkage — and it now must also cover a 1%+ diluted share creep plus preferred dividends. This is a **structural multiple-compression risk** that many sell-side models anchored on buybacks will need to revise.

---

## 8. Historical Context (FY2023–FY2025, from 10-K facts available)

| Annual item | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Financing cash flow | −$72,093M | −$79,733M | −$37,388M |
| Capex incurred but not yet paid (year-end) | $7,435M | $10,326M | $15,090M |
| Finance lease principal payments | $705M | $405M | $1,988M |

**Interpretation:** The multi-year pattern of large **negative** financing cash flow (buyback-driven, −$72B to −$80B annually) **collapsed to −$37.4B in FY2025**, then flipped to **+$86.3B in H1 2026 alone**. Simultaneously, accrued-but-unpaid capex has compounded at ~42% annually for two years (**$7.4B → $10.3B → $15.1B → $29.1B at 6/30/26**) — a clean leading indicator that the capex cycle is *still accelerating*, not peaking.

**FY2025 debt maturity profile (as of 12/31/25, from 10-K):** $2.0B due in 12 months, $1.0B in year 2, $2.7B in year 3, $1.8B in year 4, $5.5B in year 5, and **$36.1B after year 5**. The company has substantial long-dated capacity, which explains how it could add $52B of debt in six months with minimal near-term maturity pressure.

**Lease obligations (6/30/26):** Operating lease payments due $21.3B ($3.5B within 12 months); finance leases $2.9B. These are off the "debt" line but are real fixed claims — total fixed obligations ≈ **$101B debt + $24.3B leases + $18.0B preferred = ~$143B**.

---

## 9. Insider Transactions

**DATA UNAVAILABLE.** The vendor explicitly reports: *"the B-project data package has no authorized, point-in-time insider-transactions archive for GOOGL by 2026-09-10."*

- **No insider buying or selling is reported in this analysis, and none should be inferred.**
- Traders should treat this as an information gap, not as a neutral signal. Insider Form 4 activity around a quarter with a **$19B preferred issuance, a $30B equity raise, and a buyback halt** would normally be highly informative — that data must be sourced separately (SEC EDGAR Form 4 filings) before acting.

---

## 10. Risk Factors & What to Monitor

| # | Risk | Evidence in the data | Why it matters for the stock |
|---|---|---|---|
| 1 | **Negative free cash flow / capex super-cycle** | Q2 FCF −$5.9B; capex/revenue 37.5%; accrued unpaid capex $29.1B | Removes the "fortress-FCF" premium; raises duration risk in valuation |
| 2 | **Earnings quality / Level-3 marks** | 78% of H1 net income non-operating; $60B jump in unobservable-FV securities | Future downward marks could reverse reported profits |
| 3 | **Leverage inflection** | Debt +106% in 6 months to $101B; interest expense +514% | Coverage fell from ~210x to ~44x; trajectory is what matters |
| 4 | **Dilution / capital-structure complexity** | +1.17% shares; $19.1B convertible preferred; $30.5B equity issuance; buybacks = $0 | Per-share growth is structurally harder; preferred overhang |
| 5 | **Depreciation ramp compressing margins** | D&A +43.2% in H1; Q2 operating margin −210 bps QoQ (36.1% → 34.0%) | Gross-margin expansion may not persist into H2 2026 |
| 6 | **Tax rate step-up** | 17.1% → 19.1% | ~200 bps permanent EPS headwind (~$2.4B annualized on H1's pre-tax base) |
| 7 | **Legal / regulatory accruals** | Loss contingency $15.6B → $17.4B; $3.0B payment in Q3 2025 | Non-operating, hard-to-model tail risk |
| 8 | **Rates / bond marks** | AFS securities in loss position 4x to $53.2B | Reduces a non-operating income source |
| 9 | **Deferred tax normalization** | Deferred tax liabilities $0.9B → $22.8B; deferred tax expense $27.5B | Non-cash now, but cash tax normalization is a future headwind |

---

## 11. Actionable Trading Implications

Because **no price, market cap, or consensus data is available from these tools**, the following are *fundamental-posture* views and **explicit tripwires**, not price targets.

### 11.1 The core tension to trade
- **Bull leg:** revenue acceleration (+24.2%), gross-margin expansion (+212 bps), operating income +30%, $242B liquidity, 44x interest coverage. This is a business **winning** in AI.
- **Bear leg:** **−82% FCF, negative Q2 FCF, zero buybacks, $110B of new capital raised, debt doubled, EPS 78–87% non-operating, and a margin slope that has already turned down sequentially.**

**Net:** operating fundamentals should support the equity; **cash-flow and capital-structure deterioration should cap multiple expansion and raise realized volatility.** Expect **asymmetric reaction risk around the Q3 2026 print** (expected late October 2026) — a revenue/margin beat with another negative-FCF quarter is a plausible "good news sold" setup.

### 11.2 Specific, measurable tripwires for Q3 2026 (period ends 2026-09-30)

| Tripwire | Bullish threshold | Bearish threshold | Prior reading |
|---|---|---|---|
| Revenue growth YoY | ≥ +24% | < +20% | +24.2% (Q2) |
| Gross margin | ≥ 62% | < 60% | 61.6% (Q2) |
| Operating margin | ≥ 34% | < 32% | 34.0% (Q2) |
| **Free cash flow** | **> $0** | **second consecutive negative quarter** | −$5.9B (Q2) |
| Capex / revenue | ≤ 35% | > 40% | 37.5% (Q2) |
| Buyback resumption | any repurchase announced | still $0 | $0 |
| Deferred tax liability | stabilizes ≤ $23B | > $30B (further L3 marks) | $22.8B |
| Diluted share count | flat/declining | > 12.4B | ~12.3B |

### 11.3 Positioning frameworks
- **Earnings-quality-aware valuation:** Value GOOGL on **operating income or "core" EPS** (H1 run-rate ≈ **$130B annualized** operating-derived net income), *not* on the $14.24 reported H1 EPS. Any screen or screen-derived multiple using reported EPS is **materially misleading** this year.
- **Watch the FCF inflection, not the EPS print.** The single highest-conviction signal for a re-rating is **positive FCF alongside capex/revenue stabilizing below ~35%**. The single highest-conviction de-rating signal is **a third consecutive quarter of rising accrued-but-unpaid capex** (already $29.1B) with no buyback.
- **Optionality/volatility:** with headline EPS this distorted and a preferred/convertible overhang, event-driven traders should favor **volatility structures over directional ones** into the Q3 print.
- **Relative-value angle:** GOOGL's gross-margin expansion while capex doubles is a *positive* read-through for its AI monetization versus peers spending without margin evidence — but its **balance-sheet transformation (debt +106%)** is a *negative* relative read versus cash-rich peers.

### 11.4 What would change the thesis
- **Upgrade:** buyback resumption + positive Q3 FCF + capex guidance discipline + disclosure that the $136B gain is fully one-time.
- **Downgrade:** further debt issuance, a second equity/convert raise, a Level-3 write-down, or two more quarters of negative FCF.

---

## 12. Key Points Summary Table

| Category | Metric | Latest (H1/Q2 2026) | Prior Year | Assessment |
|---|---|---|---:|---|
| **Growth** | Revenue *(derived)* | $229.7B / $119.8B Q2 | $186.7B / $96.4B | 🟢 Accelerating (+23.1% / +24.2%) |
| **Growth** | QoQ revenue | +9.0% | — | 🟢 Strong sequential |
| **Profitability** | Gross margin | 62.0% H1 / 61.6% Q2 | 59.6% / 59.5% | 🟢 +242 / +212 bps |
| **Profitability** | Operating income | $80.5B H1 | $61.9B | 🟢 +30.0% |
| **Profitability** | Operating margin | 35.0% H1 / 34.0% Q2 | 33.2% / 32.4% | 🟢 Expanding, but Q2 < Q1 (36.1%) |
| **Earnings quality** | Non-operating % of net income | 77.6% H1 / ~87% Q2 | 22.1% | 🔴 Extremely distorted |
| **Earnings quality** | Reported diluted EPS | $14.24 H1 / $9.11 Q2 | $5.12 / $2.31 | 🟡 Not operating earnings |
| **Earnings quality** | Core net margin *(derived)* | ~28.3% H1 | ~27.5% | 🟢 Modest real improvement |
| **Cash flow** | Operating cash flow | $84.9B H1 | $63.9B | 🟢 +32.8% |
| **Cash flow** | **Free cash flow** | **$4.3B H1 / −$5.9B Q2** | $24.3B / +$5.3B | 🔴 **−82%; negative in Q2** |
| **Cash flow** | Capex | $80.6B H1 | $39.6B | 🔴 +103.3% |
| **Cash flow** | Capex / revenue | 35.1% H1 / 37.5% Q2 | 21.2% / 23.3% | 🔴 Structural step-up |
| **Balance sheet** | Total assets | $922.0B | $595.3B (12/31/25) | 🟡 +54.9% in 6 months |
| **Balance sheet** | Cash + ST investments | $242.5B | $126.8B | 🟢 Fortress liquidity |
| **Balance sheet** | Total debt | $101.1B | $49.1B | 🔴 +106% |
| **Balance sheet** | Net cash | +$141.4B | +$77.8B | 🟢 Positive, financing-driven |
| **Balance sheet** | Interest expense | $1.81B H1 | $0.30B | 🔴 +514% |
| **Balance sheet** | Interest coverage | 44.4x | ~210x | 🟡 Still ample, sharply lower |
| **Balance sheet** | Deferred tax liabilities | $22.8B | $0.9B | 🔴 Tied to L3 investment marks |
| **Balance sheet** | Convertible preferred | $18.0B | $0 | 🔴 New, dilutive overhang |
| **Capital returns** | Share repurchases | **$0** | $28.3B H1 | 🔴 Buyback bid withdrawn |
| **Capital returns** | Dividends paid | $5.23B H1 ($0.22/qtr) | $4.98B ($0.21/qtr) | 🟢 +5.1% |
| **Capital returns** | Equity issuance | $30.5B common + $19.1B preferred | $0 | 🔴 Net dilution |
| **Dilution** | Shares outstanding | 12,230M | 12,088M | 🔴 +1.17% |
| **Compensation** | SBC | $15.2B H1 (6.6% of rev) | $11.5B (6.2%) | 🟡 Rising faster than revenue |
| **Tax** | Effective rate | 19.1% | 17.1% | 🔴 +200 bps |
| **Legal** | Loss contingency (current) | $17.4B | $15.6B | 🔴 Creeping higher |
| **Investments** | Unobservable-FV securities | $124.3B | $64.1B | 🟡 +93.9%, Level-3 risk |
| **Insider activity** | Form 4 transactions | **DATA UNAVAILABLE** | — | ⚪ Information gap |
| **Valuation** | Price / market cap / multiples | **Not provided by tools** | — | ⚪ Cannot compute |

---

## 13. Final Verdict for Traders

GOOGL's Q2 2026 filing describes a **fundamentally strengthening operating business financing an extraordinarily aggressive infrastructure build with other people's capital.** The demand signal is unambiguous — revenue +24%, gross margin +212 bps, operating income +30% — and $242B of liquidity means there is no solvency question. But the **quality of the reported $174.8B H1 profit is poor (78% non-operating), the Q2 free cash flow is negative, the buyback is gone, debt has doubled, and $110B of new capital was raised in six months.**

**Practical stance:** treat GOOGL as an **operating compounder with a valuation cap and elevated event volatility**, not as the cash-returning mega-cap of 2023–2025. Anchor models on **operating income (~$161B annualized run-rate) and core net income (~$130B annualized)**, not reported EPS. The highest-value datapoints in the next quarter are **FCF, capex/revenue, and whether buybacks return** — in that order.

---

*Report compiled from point-in-time SEC facts publicly accepted by 2026-09-10. Revenue, gross profit, R&D+S&M, core net income, FCF, coverage ratios, and growth rates are derived from disclosed tags and are labeled as such. Insider transaction data was unavailable from the authorized archive and was not estimated. No price or valuation-multiple data was provided by the tools; no price target is implied.*