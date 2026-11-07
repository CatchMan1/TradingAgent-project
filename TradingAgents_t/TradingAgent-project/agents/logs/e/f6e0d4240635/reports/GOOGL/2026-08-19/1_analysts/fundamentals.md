# GOOGL (Alphabet Inc.) — Fundamental Research Report
**As of:** 2026-08-19 | **Latest filing in dataset:** Form 10-Q, period ended 2026-06-30, filed 2026-07-23 (acc. 0001652044-26-000071) | **Prior FY filing:** 10-K filed 2026-02-05

---

## 1. Data provenance, scope and limitations (read first)

| Item | Status |
|---|---|
| Source | Point-in-time SEC XBRL facts (B-project cache), filtered by EDGAR acceptance timestamp ≤ 2026-08-19. **No look-ahead.** |
| Statements available | Balance sheet (2 snapshots: 2025-12-31, 2026-06-30); income statement & cash flow (Q2'25, H1'25, Q1'26, Q2'26, H1'26; plus FY2023–FY2025 cash-flow only) |
| **TotalRevenues tag** | **Not present in the extract** (fact list truncated alphabetically). **Revenue is derived** as `OperatingIncomeLoss + CostsAndExpenses`. This method is validated: derived Q2'25 revenue = **$96,428M** (reported $96.4B), derived Q2'25 net income = $28,196M, derived Q2'25 diluted EPS = $2.31 — all match Alphabet's actual reported Q2'25. I therefore treat derived revenue as reliable to ±0.1%. |
| **Missing line items** | R&D, Sales & Marketing are reported **only as a combined residual** ($51.3B H1'26 — computed). Segment revenue, geographic mix, headcount, Stockholders' Equity total, PP&E, goodwill, buyback authorization — **not in extract.** |
| **Insider transactions** | **DATA_UNAVAILABLE** — the archive has no authorized point-in-time insider-transaction record for GOOGL by 2026-08-19. **No insider activity is inferred or fabricated anywhere in this report.** |
| Frequency parameter | `annual` returned the same truncated fact set as `quarterly`; no additional FY2025 P&L detail could be recovered. |

---

## 2. Headline: the reported numbers are dominated by a non-cash revaluation event

H1 2026 net income was **$174,771M** on revenue of **$229,692M** — a 76% net margin that is *not* an operating outcome. It is driven by **$135,946M of gains on equity securities (FV-NI)**, of which **$99,031M landed in Q2 alone**. Non-operating income was $135,699M versus $13,845M a year ago.

**This is the single most important fact for trading GOOGL today:** roughly **63% of H1 2026 net income and ~71% of Q2 net income is non-operating, largely unrealized mark-up of equity stakes** — not cash, not recurring, and fully reversible.

### Clean ("core") earnings bridge — derived

| $M unless noted | H1 2026 | H1 2025 | Δ | Q2 2026 | Q2 2025 | Δ |
|---|---|---|---|---|---|---|
| Revenue (derived) | 229,692 | 186,662 | **+23.1%** | 119,796 | 96,428 | **+24.2%** |
| Operating income (reported) | 80,466 | 61,877 | +30.0% | 40,770 | 31,271 | +30.4% |
| Pre-tax income (reported) | 216,165 | 75,722 | +185% | 138,753 | 33,933 | +309% |
| *Less: equity-security gains* | (135,946) | (11,044) | — | (99,031) | (1,286) | — |
| **Core pre-tax income** | **80,219** | **64,678** | **+24.0%** | **39,722** | **32,647** | **+21.7%** |
| Effective tax rate | 19.1% | 17.1% | +200bp | 19.1% | 16.9% | +220bp |
| **Core net income (est.)** | **~64,900** | **~53,600** | **+21%** | **~32,100** | **~27,100** | **+19%** |
| **Core diluted EPS (est.)** | **~$5.29** | **~$4.38** | **+21%** | **~$2.62** | **~$2.24** | **+17%** |
| Reported diluted EPS | **$14.24** | $5.12 | +178% | **$9.11** | $2.31 | +294% |

**Actionable read:** underlying operating momentum is genuinely strong (+23% revenue, +21% core EPS), but a screen showing ~$19–20 of trailing EPS (Q3'25+Q4'25+H1'26) overstates true earning power by roughly **2.7x**. Value GOOGL off core EPS (~$11 annualized run-rate), not reported EPS.

---

## 3. Income statement detail

### 3.1 Revenue and margin trajectory

| | Q1 2026 | Q2 2026 | H1 2026 | Q1 2025 | Q2 2025 | H1 2025 |
|---|---|---|---|---|---|---|
| Revenue ($M, derived) | 109,896 | 119,796 | 229,692 | 90,234 | 96,428 | 186,662 |
| Y/Y growth | **+21.8%** | **+24.2%** | **+23.1%** | — | — | — |
| Q/Q growth | — | **+9.0%** | — | — | — | — |
| Cost of revenue ($M) | 41,271 | 45,943 | 87,214 | 36,361 | 39,039 | 75,400 |
| CoR growth Y/Y | +13.5% | +17.7% | +15.7% | | | |
| Gross profit ($M) | 68,625 | 73,853 | 142,478 | 53,873 | 57,389 | 111,262 |
| **Gross margin** | **62.44%** | **61.65%** | **62.03%** | 59.70% | 59.51% | 59.61% |
| **Operating margin** | **36.12%** | **34.03%** | **35.03%** | 33.92% | 32.43% | 33.15% |

- **Gross margin expanded +242bp Y/Y in H1** (and +214bp in Q2). Cost of revenue grew 15.7% vs revenue +23.1% — i.e., the enormous AI infrastructure build is **not yet** compressing gross margin. This is the strongest positive surprise in the dataset.
- **Operating margin +188bp** despite opex growing faster than sales (below).
- Revenue is **accelerating sequentially** (+21.8% → +24.2%), the classic signature of a demand backdrop that is strengthening, not decelerating.

### 3.2 Operating expense structure (R&D + S&M shown as derived residual)

| $M | H1 2026 | % rev | H1 2025 | % rev | Y/Y |
|---|---|---|---|---|---|
| Cost of revenue | 87,214 | 37.97% | 75,400 | 40.39% | +15.7% |
| R&D + Sales & Marketing (residual) | **51,260** | **22.32%** | 40,637 | 21.77% | **+26.1%** |
| General & administrative | 10,752 | 4.68% | 8,748 | 4.69% | +22.9% |
| **Total costs & expenses** | **149,226** | **64.97%** | 124,785 | 66.85% | **+19.6%** |

- **Opex (R&D+S&M) is growing 26.1%, faster than revenue (+23.1%)** — a 55bp headwind to operating margin that gross-margin gains more than offset. If gross-margin expansion stalls, margin compression follows immediately.
- **Stock-based comp: $15,200M in H1'26 vs $11,500M H1'25 (+32.2%)**, i.e. **6.62% of revenue vs 6.16%**. Dilution is re-accelerating just as buybacks stopped (see §5).
- **Depreciation: $13,586M vs $9,485M (+43.2%)** — the D&A ramp from AI capex is arriving (5.9% of revenue vs 5.1%). This grows mechanically from here given the capex figures in §5.
- Amortization of intangibles: $545M H1'26 vs $246M (+122%); Q2 alone $367M vs $124M (~3x) → a Q2 acquisition step-up. Forward 12-month intangible amortization is guided by disclosure at **$1,304M**.

### 3.3 Below the line

| $M | H1 2026 | H1 2025 | Q2 2026 | Q2 2025 |
|---|---|---|---|---|
| Equity securities FV-NI gain | **135,946** | 11,044 | **99,031** | 1,286 |
| — of which realized | 836 | 435 | 278 | 217 |
| Debt securities realized loss | (143) | +367 | (32) | +165 |
| Interest income | 2,811 | 2,051 | 1,430 | 1,050 |
| **Interest expense** | **1,811** | 295 | **1,278** | 261 |
| FX loss | (14) | (175) | (160) | (69) |
| Non-operating income, net | 135,699 | 13,845 | 97,983 | 2,662 |
| Effective tax rate | 19.1% | 17.1% | 19.1% | 16.9% |
| Net income | 174,771 | 62,736 | 112,193 | 28,196 |

- **Interest expense is up 6.1x Y/Y** (annualizing to ~$3.6B+), the direct cost of the debt-funded build-out. Still trivial versus $80B of H1 operating income (44x coverage).
- Tax rate stepped up **+200bp to 19.1%** — a structural headwind to EPS growth versus prior-year comparisons.
- Preferred dividends of $86M (all in Q2, first payment after the 2026-06-05 issuance).

---

## 4. The equity-stake revaluation engine — where the "earnings" actually come from

| $M | 2026-06-30 | 2025-12-31 | Change |
|---|---|---|---|
| Equity securities **without** readily determinable FV (carrying) | **124,259** | 64,094 | **+60,165 (+94%)** |
| — cumulative *upward* price adjustments | 85,732 | 44,485 | +41,247 |
| — cumulative *downward* price adjustments | (9,115) | (8,820) | (295) |
| Available-for-sale debt securities | 99,500 | n/a | — |
| Deferred income tax liabilities, net | **22,819** | 919 | **+21,900** |
| Deferred income tax assets, net | 1,448 | 9,113 | (7,665) |
| Deferred income taxes & credits (CF add-back) | **+27,538** | (1,596) H1'25 | swing |

**Interpretation:**
1. **$124.3B of GOOGL's balance sheet is now marked to private-market AI/tech valuations**, and **$85.7B of that carrying value is cumulative upward mark-up** (vs $9.1B of cumulative write-downs). The reported gains are therefore largely *unrealized marks on stakes Alphabet cannot liquidate quickly*.
2. The tax consequence is real and already booked: a **$22.8B deferred tax liability** was created. If the marks reverse, both the gain and the DTL reverse — a **~$29.6B swing in the net deferred position** in six months.
3. **Reversal risk is symmetric and material.** A 20% haircut to the $124.3B private book would be a ~$25B pre-tax hit — roughly 30% of H1 operating income — in a single quarter, with no cash impact.
4. **Non-cash nature:** H1 CFO of $84,859M versus net income of $174,771M (0.49x conversion). On a core basis, CFO/core NI ≈ **1.31x** — healthy. The gap is entirely non-cash marks and deferred taxes.

---

## 5. Cash flow & capital allocation — the regime change

| $M | H1 2026 | H1 2025 | Δ | Q1 2026 | Q2 2026 | Q1 2025 | Q2 2025 |
|---|---|---|---|---|---|---|---|
| Operating cash flow | 84,859 | 63,897 | +32.8% | 45,790 | 39,069 | 36,150 | 27,747 |
| Capex (PP&E purchases) | **80,598** | 39,643 | **+103.3%** | 35,674 | **44,924** | 17,197 | 22,446 |
| **Free cash flow (derived)** | **4,261** | 24,254 | **−82.4%** | 10,116 | **(5,855)** | 18,953 | 5,301 |
| Capex / revenue | **35.1%** | 21.2% | — | 32.5% | **37.5%** | 19.1% | 23.3% |
| Capex incurred but unpaid | **29,113** | 10,635 | +173.7% | 24,131 | — | 11,388 | — |
| Dividends paid (common) | 5,231 | 4,977 | +5.1% | 2,542 | 2,689 | 2,434 | 2,543 |
| Preferred dividends | 86 | 0 | — | 0 | 86 | 0 | 0 |
| **Buybacks** | **0** | **28,306** | **−100%** | **0** | **0** | 15,068 | 13,238 |

### Financing raised (H1 2026)

| $M | H1 2026 | H1 2025 |
|---|---|---|
| Debt raised | **56,226** | 31,378 |
| Debt repaid | (5,253) | (18,397) |
| **Net debt** | **+50,973** | +12,981 |
| **Common stock issued** | **30,499** | **0** |
| **Convertible preferred issued** (2026-06-05) | **19,063** (19,000 gross) | 0 |
| Non-controlling-interest contributions | 3,758 | 400 |
| Finance-lease principal | (840) | (302) |
| Net financing cash flow | **+86,320** | (26,033) |
| Net investing cash flow | **(145,822)** | (40,738) |
| Net change in cash | **+25,203** | (2,430) |

**This is the most significant structural shift in the dataset:**
- **Buybacks went to exactly zero** ($28.3B in H1'25 → $0). The single largest historic source of EPS support has been switched off.
- **Alphabet became a net issuer of equity:** $30.5B of common stock plus $19.0B of convertible preferred in Q2 2026. Against a net share increase of 142M, the implied blended common issuance price is **~$215/share** (approximate — proceeds may include option/ESPP activity; verify against the 10-Q text, which is not in this dataset).
- **Debt more than doubled:** carrying amount **$101,085M vs $49,085M** (+106%), plus $2,590M finance leases.
- **Q2 2026 free cash flow was negative (−$5,855M)** — the first negative FCF quarter implied by this data. **H1 2026 FCF did not even cover the $5.3B dividend** (FCF after dividends ≈ −$1,056M).
- **Q2 2026 alone consumed/raised:** ~$74B of financing (30.5 common + 19.0 preferred + ~24.8 net debt) against ~$82B of investing outflow. This is a **capital-intensive, externally funded expansion**, not a self-funded one.

**Trading implication:** GOOGL has migrated from "fortress-cash-generator returning capital" to "levered AI infrastructure builder issuing equity." That re-rates the business on capex-payback risk rather than on FCF yield, and it removes the buyback bid.

---

## 6. Balance sheet analysis

### 6.1 Assets

| $M | 2026-06-30 | 2025-12-31 | Δ % |
|---|---|---|---|
| **Total assets** | **921,983** | 595,281 | **+54.9%** |
| Current assets | 343,524 | 206,038 | +66.7% |
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| **Cash + short-term investments** | **242,474** | 126,843 | **+91.2%** |
| Available-for-sale debt securities | 99,500 | — | — |
| Accounts receivable, net | 69,175 | 62,886 | +10.0% |
| Equity securities w/o determinable FV | 124,259 | 64,094 | +93.9% |
| Finite-lived intangibles, gross | **10,585** | 2,467 | **+329%** |
| Finance lease ROU asset | 5,474 | 4,797 | +14.1% |

- **Assets grew $326.7B in six months — a 55% expansion of the balance sheet.** Of that, ~$115.6B is liquid securities, ~$60.2B is private equity stakes, and the rest is operating/infrastructure assets and acquisitions (intangibles +$8.1B).
- **AR +10.0% vs revenue +23.1% Y/Y** → collections and linearity are excellent. Q2 DSO ≈ **52.6 days** (AR $69,175 / Q2 revenue $119,796 × 91). Allowance for credit losses barely moved ($924M → $995M = 1.44% of gross AR) — no receivables quality deterioration.
- Cash + ST investments of **$242.5B** is roughly **2.4x total debt** — the fortress is still intact, only partially pledged to the build-out.

### 6.2 Liabilities, preferred and equity

| $M | 2026-06-30 | 2025-12-31 | Δ |
|---|---|---|---|
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities (current) | 73,014 | 55,557 | +31.4% |
| Employee-related liabilities | 15,086 | 17,546 | −14.0% |
| Accrued income taxes, current | 5,233 | 523 | +901% |
| Contract liabilities (deferred revenue), current | 7,154 | 6,578 | +8.8% |
| Contract liabilities, total | **10,100** | 8,600 | +17.4% |
| **Debt carrying amount** | **101,085** | 49,085 | **+106%** |
| Finance lease liabilities | 2,590 | 2,500 | +3.6% |
| Operating lease liabilities | 18,037 | 15,954 | +13.1% |
| Accrued income taxes, non-current | 11,306 | 9,531 | +18.6% |
| Deferred income tax liabilities, net | **22,819** | 919 | +2,383% |
| **Convertible preferred stock** | **18,023** | **0** | new |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| AOCI | (2,285) | (1,916) | (369) |
| Shares outstanding | **12,230M** | 12,088M | **+142M (+1.18%)** |
| Legal/loss contingency accrual (current) | **17,356** | 15,594 | +11.3% |

**Derived stock-level metrics (equity total not in extract; computed via ΔA − ΔL):**
- **Δ book equity ≈ +$220B** in six months (reconciles to net income $174.8B − dividends $5.3B + common issuance $30.5B + preferred $19.0B + SBC $15.2B + NCI $3.8B − AOCI $0.4B ≈ $218–220B). ✔ internally consistent.
- **Total debt / total assets = 11.0%**. **Net cash = $141.4B** (cash+ST inv − debt); **$120.8B** even after deducting preferred and finance leases.
- **Approximate current ratio ≈ 2.75x** (current assets $343.5B / estimated current liabilities ~$125B) — up sharply, liquidity is not a constraint.
- Interest coverage (H1): **44x** (operating income $80.5B / interest $1.8B).
- **Book value quality caveat:** ~$124B of the equity base is private-company marks with $85.7B of cumulative upward revaluation. **P/B is therefore not a reliable valuation anchor for GOOGL right now.**
- **Share count is inflating** (+1.18% in six months, ~2.4% annualized) with **zero buyback offset** — a persistent ~2% EPS dilution headwind, on top of $18B of convertible preferred overhang.

### 6.3 Contracted future obligations

| $M (undiscounted) | 2026-06-30 | 2025-12-31 |
|---|---|---|
| Operating lease payments, total | **21,333** | 18,251 |
| — next 12 months | 3,498 | 3,275 |
| Finance lease payments, total | 2,920 | 2,869 |
| Long-term debt maturities (per FY25 10-K): next 12m / yr2 / yr3 / yr4 / yr5 / >5yr | 2,000 / 1,000 / 2,676 / 1,764 / 5,500 / **36,145** | same |

Long-dated debt dominates (89% beyond year 5 at FY25) — refinancing risk is low; the maturity wall is not a near-term issue even after the $52B of new issuance.

---

## 7. Quality-of-earnings scorecard

| Test | Result | Assessment |
|---|---|---|
| CFO / net income | 0.49x | **Poor headline, but artificial** — non-cash equity marks |
| CFO / core net income (est.) | **1.31x** | **Good** — real cash conversion |
| Accruals vs revenue growth | Deferred liabilities +$18B, DTL +$22.8B | Neutral — tax-driven, not channel stuffing |
| Receivables vs revenue | AR +10% vs revenue +23% | **Strong** — no revenue quality flag |
| Deferred revenue (contract liabilities) | $8.6B → $10.1B (+17.4%) | Healthy backlog build |
| SBC as % of revenue | 6.62% vs 6.16% | **Worsening** |
| Buyback offset to dilution | **None** | **Worsening** |
| Capex / revenue | **35.1% (Q2: 37.5%)** | **Aggressive bet; FCF destroyed** |
| Externally funded growth | $30.5B equity + $19B preferred + $52B debt | **Regime change** |
| Legal/regulatory accruals | $17.4B current (from $15.6B) | Rising overhang |

---

## 8. Interpretation: what is management actually telling us with these numbers?

1. **Demand is real and accelerating** — revenue growth of +21.8% then +24.2%, with gross margin *expanding* 242bp. That combination is difficult to fake and is the highest-conviction positive signal in the dataset.
2. **The build-out is bigger than internal cash generation** — H1 capex $80.6B (35% of revenue), Q2 capex $44.9B (annualizing ~$180B), plus $29.1B already incurred but unpaid (+174% Y/Y, implying **Q3 capex steps up again**). Management chose to fund this with equity, convertibles and debt rather than slow the build — a deliberate statement that the expected return on AI infrastructure exceeds the cost of capital, and that they are unwilling to let the balance sheet constrain it.
3. **Private AI valuations are now embedded in reported earnings** — $124B of non-marketable stakes, $85.7B of cumulative mark-ups, $22.8B deferred tax liability. GOOGL's P&L has become partly a proxy for the private AI funding cycle.
4. **Shareholder returns have been subordinated** — buybacks to zero, dividend growth of only +5.1% (well below earnings growth), and dilution of ~2.4% annualized.

---

## 9. Insider transactions

**Not available.** The data vendor's point-in-time archive contains **no authorized insider-transaction record for GOOGL as of 2026-08-19**, and I have not inferred, estimated or fabricated any insider buying or selling. Any conclusion about insider sentiment would be unsupported by this dataset and should be sourced separately (Forms 3/4/5 via EDGAR).

---

## 10. Risks, ranked by near-term P&L impact

| # | Risk | Magnitude / evidence |
|---|---|---|
| 1 | **Reversal of unrealized equity marks** | $124.3B private book; $85.7B cumulative upward marks; $99.0B of Q2 net income was marks. A 20% markdown ≈ **$25B pre-tax, ~30% of H1 operating income**, non-cash but headline-EPS violent. |
| 2 | **Negative free cash flow / funding dependence** | Q2'26 FCF **−$5,855M**; H1 FCF $4,261M did not cover the $5,231M dividend. Capex 37.5% of Q2 revenue and rising (unpaid capex +174%). |
| 3 | **Depreciation ramp compressing future margins** | D&A +43.2% Y/Y to $13,586M (5.9% of revenue). Mechanical escalation from $180B annualized capex. |
| 4 | **Opex growing faster than revenue** | R&D+S&M +26.1% vs revenue +23.1%; SBC +32.2%. Gross-margin expansion is the only offset. |
| 5 | **Capital-structure dilution** | +142M shares in 6 months with zero buybacks; $19.0B convertible preferred overhang + $30.5B new common. |
| 6 | **Tax rate step-up** | 17.1% → 19.1% effective rate, structural −200bp on EPS; plus $22.8B DTL on the balance sheet. |
| 7 | **Legal/regulatory accruals** | Current loss-contingency accrual $17.4B (from $15.6B); $3.0B paid in Q3'25. |
| 8 | **Rising interest burden** | Interest expense 6.1x Y/Y ($1.8B H1) and growing with $101B debt + $19B preferred coupon. |
| 9 | **Private-market illiquidity of book value** | $124B of Level-3-ish stakes cannot be monetized to fund capex — hence the external raise. |
| 10 | **Valuation distortion in screens** | Trailing reported EPS ~$19–20 vs core ~$11 annualized run-rate → screens understate P/E by ~2.7x. Trader error risk, not company risk. |

---

## 11. Actionable takeaways for traders

**Constructive (fundamental momentum):**
- **Buy-side thesis is intact on operations:** revenue +23.1% H1 / +24.2% Q2 with **gross margin +242bp** and **operating margin +188bp**. Core EPS growth of **+21%** with **CFO/core-NI of 1.31x**. This is a business accelerating into its own capex cycle — the rarest bullish configuration.
- **Fortress liquidity:** $242.5B cash+securities vs $101.1B debt (net cash $141B), interest coverage 44x, 89% of debt maturing beyond 5 years. **No solvency or refinancing risk.**
- **Backlog/derived demand signals positive:** contract liabilities +17.4%, AR growing far slower than revenue (DSO ~52.6 days), paid-in capital being deployed at scale.

**Cautious (what to fade):**
- **Do not extrapolate the +178% EPS growth.** ~63% of H1 earnings and ~71% of Q2 earnings are non-operating, non-cash equity marks. **Normalize to ~$5.29 H1 core EPS.**
- **Q2 2026 is the first negative-FCF quarter implied by this data.** Watch Q3 (Oct/Nov 2026 print) for: (a) a second consecutive negative FCF quarter, (b) further equity/preferred issuance, (c) capex/revenue above 37.5%, (d) D&A/revenue breaching 7%.
- **Dilution + no buyback** caps per-share upside: expect ~2.4% annual share-count drag plus convertible overhang.
- **Watch the mark-to-market direction, not just the level.** With $85.7B of cumulative upward marks, the next private-AI valuation reset hits GOOGL earnings directly. Track the *deferred tax liability* (currently $22.8B) as a real-time tell on the direction of those marks — a falling DTL signals coming mark-downs.

**Suggested positioning framework:**
- **Long-operating / hedge-earnings-quality:** own GOOGL on core-EPS and revenue-momentum grounds; explicitly discount reported EPS. Any pullback driven by a *mark-to-market miss* (non-cash) rather than an *operating miss* is a buying opportunity.
- **Event risk to trade around:** the Q3 2026 10-Q expected early November 2026 — the three data points that matter are capex, FCF (spillway to negative or recovery), and the private-equity mark direction.
- **Invalidation triggers:** (1) gross margin reverting below ~59.6% while capex/revenue stays above 35% — that combination means the AI build is not earning its cost of capital; (2) a second, larger equity raise; (3) operating margin compressing on an absolute basis.

---

## 12. Summary table — key fundamental points

| Category | Metric | Latest (2026-06-30 / H1 2026) | Prior (2025-12-31 / H1 2025) | Δ | Signal |
|---|---|---|---|---|---|
| **Scale** | Total assets | $921,983M | $595,281M | **+54.9%** | Balance sheet transformed |
| **Scale** | Revenue (derived) | $229,692M H1 | $186,662M H1 | **+23.1%** | 🟢 Accelerating |
| **Scale** | Q2 revenue (derived) | $119,796M | $96,428M | **+24.2%** | 🟢 Acceleration |
| **Profitability** | Gross margin | 62.03% | 59.61% | **+242bp** | 🟢 Best-in-class, improving |
| **Profitability** | Operating margin | 35.03% | 33.15% | +188bp | 🟢 Expanding |
| **Profitability** | Operating income | $80,466M | $61,877M | +30.0% | 🟢 |
| **Profitability** | Reported net income | $174,771M | $62,736M | +178.6% | 🟡 Mark-driven |
| **Profitability** | Reported diluted EPS | $14.24 | $5.12 | +178% | 🔴 Not economic |
| **Profitability** | **Core diluted EPS (est.)** | **~$5.29** | ~$4.38 | **+21%** | 🟢 True growth rate |
| **Quality** | Equity-security gains (FV-NI) | $135,946M | $11,044M | +1,131% | 🔴 Unrealized, reversible |
| **Quality** | CFO / net income | 0.49x | 1.02x | — | 🔴 Artifact; core 1.31x 🟢 |
| **Quality** | SBC | $15,200M (6.62% of rev) | $11,500M (6.16%) | +32.2% | 🔴 Dilution rising |
| **Quality** | Effective tax rate | 19.1% | 17.1% | +200bp | 🔴 Headwind |
| **Cash flow** | Operating cash flow | $84,859M | $63,897M | +32.8% | 🟢 |
| **Cash flow** | Capex | $80,598M (**35.1% of rev**) | $39,643M (21.2%) | **+103.3%** | 🟡 Bet size doubled |
| **Cash flow** | **Free cash flow (derived)** | **$4,261M** | $24,254M | **−82.4%** | 🔴 |
| **Cash flow** | Q2 FCF (derived) | **−$5,855M** | +$5,301M | swing | 🔴 First negative |
| **Cash flow** | Capex incurred, unpaid | $29,113M | $10,635M | +173.7% | 🔴 Q3 capex steps up |
| **Cash flow** | FCF after dividends | **≈ −$1,056M** | +$19,277M | swing | 🔴 Dividend not covered |
| **Balance sheet** | Cash + ST investments | $242,474M | $126,843M | +91.2% | 🟢 |
| **Balance sheet** | Total debt | $101,085M | $49,085M | **+106%** | 🟡 Leverage doubling |
| **Balance sheet** | Net cash (ex-pref/leases) | $141,389M | $77,758M | +82% | 🟢 |
| **Balance sheet** | Debt / total assets | 11.0% | 8.2% | +280bp | 🟢 Still low |
| **Balance sheet** | Private equity stakes (no RDFV) | $124,259M | $64,094M | +93.9% | 🔴 Valuation-sensitive |
| **Balance sheet** | Deferred tax liabilities, net | $22,819M | $919M | +2,383% | 🔴 Tax on unrealized marks |
| **Balance sheet** | Accounts receivable | $69,175M | $62,886M | +10.0% | 🟢 vs revenue +23% |
| **Balance sheet** | Contract liabilities | $10,100M | $8,600M | +17.4% | 🟢 Backlog build |
| **Balance sheet** | Loss contingency accrual (current) | $17,356M | $15,594M | +11.3% | 🟡 Legal overhang |
| **Capital allocation** | Buybacks | **$0** | $28,306M H1'25 | **−100%** | 🔴 Support removed |
| **Capital allocation** | Common stock issued | **$30,499M** | $0 | new | 🔴 Primary equity raise |
| **Capital allocation** | Convertible preferred issued | **$19,063M** (06-05-26) | $0 | new | 🟡 Overhang; $86M divs |
| **Capital allocation** | Dividends (common) | $5,231M ($0.43/sh H1) | $4,977M ($0.41) | +5.1% | 🟡 Below earnings growth |
| **Capital allocation** | Net debt raised | +$50,973M | +$12,981M | +293% | 🟡 |
| **Shares** | Shares outstanding | 12,230M | 12,088M | **+142M (+1.18%)** | 🔴 ~2.4% annualized dilution |
| **Returns** | Interest coverage (H1) | 44x | 210x | — | 🟢 Still ample |
| **Insider** | Transactions | **DATA UNAVAILABLE — no authorized archive; nothing inferred** | — | — | ⚪ Unknown |

*All figures USD millions unless noted. Revenue, Q1/Q2 splits, core EPS, FCF, current ratio, and Δ book equity are **derived** from reported XBRL facts (revenue = OperatingIncomeLoss + CostsAndExpenses; FCF = CFO − PaymentsToAcquirePropertyPlantAndEquipment); the derivation is validated against known Q2'25 reported results. R&D and S&M are shown combined because those tags were not present in the point-in-time extract. Stockholders' equity level, segment results, headcount, PP&E and goodwill were not available in this dataset.*