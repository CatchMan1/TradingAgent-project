# GOOGL (Alphabet Inc.) — Fundamental Deep Dive
**Analysis date: 2026-08-12 | Latest filing available: Form 10-Q filed 2026-07-23 (accn 0001652044-26-000071) for the quarter ended 2026-06-30; 10-K filed 2026-02-05 for FY2025**

---

## 1. Data provenance and caveats (read first)

- All figures below come from point-in-time SEC XBRL facts filtered by **actual EDGAR acceptance timestamp**, so nothing post-dates 2026-08-12. No restatements or look-ahead leakage.
- **The vendor feed returned an alphabetically truncated tag set (A–F).** Revenue, segment revenue, goodwill, total liabilities, total stockholders' equity, and the full FY2025 income statement were **not surfaced**. Where I state revenue, it is **derived arithmetically** from `CostsAndExpenses + OperatingIncomeLoss` (an identity, high confidence). Equity and current liabilities are **estimates** and labeled as such.
- **Insider-transaction data is explicitly unavailable** in the archive for GOOGL as of 2026-08-12. I will not infer or fabricate insider activity. Treat the absence of insider signal as a gap, not a bullish or bearish input.
- All $ figures in **USD millions** unless noted.

---

## 2. Company profile

Alphabet Inc. (ticker **GOOGL**) is the parent of Google — Google Services (Search, YouTube, Android, Chrome, Play, hardware, subscriptions), Google Cloud, and Other Bets, plus a large portfolio of equity investments. The 2026 filings show a company whose **operating model is unchanged but whose balance sheet has been radically transformed** by AI infrastructure build-out and by a very large investment/acquisition program.

---

## 3. Headline P&L: Q2 2026 and H1 2026

### 3.1 Reconstructed income statement (derived revenue in bold-italic)

| Line item | Q2 2026 | Q2 2025 | YoY | Q1 2026 | QoQ | H1 2026 | H1 2025 | YoY |
|---|---|---|---|---|---|---|---|---|
| ***Revenue (derived)*** | ***119,796*** | ***96,428*** | **+24.2%** | ***109,896*** | **+9.0%** | ***229,692*** | ***186,662*** | **+23.0%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 41,271 | +11.3% | 87,214 | 75,400 | +15.7% |
| Gross profit | 73,853 | 57,389 | +28.7% | 68,625 | +7.6% | 142,478 | 111,262 | +28.1% |
| **Gross margin** | **61.6%** | 59.5% | +210bp | 62.4% | −80bp | 62.0% | 59.6% | +240bp |
| G&A | 6,461 | 5,209 | +24.0% | 4,291 | +50.6% | 10,752 | 8,748 | +22.9% |
| Other opex (R&D + S&M, derived) | 26,622 | 20,909 | +27.3% | 24,638 | +8.1% | 51,260 | 40,637 | +26.1% |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 70,200 | +12.6% | 149,226 | 124,785 | +19.6% |
| **Operating income** | **40,770** | **31,271** | **+30.4%** | **39,696** | **+2.7%** | **80,466** | **61,877** | **+30.0%** |
| **Operating margin** | **34.0%** | 32.4% | +160bp | **36.1%** | **−210bp** | 35.0% | 33.1% | +190bp |
| Non-operating income | 97,983 | 2,662 | n.m. | 37,716 | n.m. | 135,699 | 13,845 | n.m. |
| Pre-tax income | 138,753 | 33,933 | +309% | 77,412 | +79% | 216,165 | 75,722 | +185% |
| Tax expense | 26,560 | 5,737 | +363% | 14,834 | — | 41,394 | 12,986 | +219% |
| **Effective tax rate** | **19.1%** | 16.9% | +220bp | 19.2% | — | 19.1% | 17.1% | +200bp |
| Net income | 112,193 | 28,196 | +298% | 62,578 | +79% | 174,771 | 62,736 | +179% |
| Net income to common | 112,107 | 28,196 | +298% | 62,578 | — | 174,685 | 62,736 | +178% |
| **Diluted EPS** | **$9.11** | $2.31 | +294% | **$5.13** | +78% | **$14.24** | $5.12 | +178% |
| Diluted shares (derived, M) | 12,306 | 12,206 | +0.8% | ~12,230 | — | 12,267 | 12,253 | +0.1% |

**The single most important thing in these numbers: the headline is not the business.** $135.9B of pre-tax non-operating income hit the P&L in H1 2026 (`EquitySecuritiesFvNiGainLoss` = 135,946; `DebtAndEquitySecuritiesGainLoss` = 135,803). Strip it out and you get the real operating trajectory.

### 3.2 Core earnings bridge (ex-equity-mark-to-market) — the numbers traders should actually use

| Metric | Q2 2026 | Q2 2025 | YoY | Q1 2026 | H1 2026 | H1 2025 | YoY |
|---|---|---|---|---|---|---|---|
| Pre-tax income (reported) | 138,753 | 33,933 | — | 77,412 | 216,165 | 75,722 | — |
| Less: equity securities gains | (99,031) | (1,286) | — | (36,915) | (135,946) | (11,044) | — |
| **Core pre-tax income** | **39,722** | **32,647** | **+21.7%** | **40,497** | **80,219** | **64,678** | **+24.0%** |
| Core net income (at 19.1%/17.1% ETR) | ~32,116 | ~27,128 | +18.4% | ~32,762 | ~64,897 | ~53,618 | +21.0% |
| **Core diluted EPS (est.)** | **~$2.61** | **~$2.22** | **+17.4%** | **~$2.68** | **~$5.29** | **~$4.38** | **+20.8%** |

**Actionable read:** the underlying franchise grew core EPS ~17–21%, not 294%. But that is *still* an excellent growth rate for a $2.5T+ company, and Q2 core EPS *declined sequentially* ($2.61 vs $2.68) despite revenue +9.0% QoQ — the cost ramp (AI infrastructure, depreciation, SBC) is arriving faster than revenue.

---

## 4. Operating quality: what is actually driving the P&L

**Positives**
1. **Revenue acceleration.** Q2 +24.2% YoY vs Q1 +21.8% YoY — accelerating, not decelerating. H1 revenue $229.7B → ~$480B annualized run-rate.
2. **Gross margin expansion (+210bp YoY in Q2)** even as depreciation surged 43% YoY ($13,586M H1'26 vs $9,485M). Cost of revenue grew only +17.7% vs revenue +24.2% — evidence of AI-serving efficiency and mix.
3. **Operating leverage intact YoY:** operating income +30.4% vs revenue +24.2%.
4. **Depreciation still only 5.9% of revenue** (H1'26: 13,586 / 229,692). There is a *lot* of depreciation still to come as the capex wave converts — that is the forward risk to the 34% operating margin.

**Negatives / warnings**
1. **Sequential operating margin compression: 36.1% (Q1) → 34.0% (Q2) = −210bp.** Other opex (R&D + S&M) grew 8.1% QoQ and 27.3% YoY — faster than revenue. G&A +50.6% QoQ is the largest relative jump.
2. **Effective tax rate stepped up to 19.1% from 16.9%** and has been stable at ~19.1% for two consecutive quarters. That is a ~220bp permanent headwind to EPS growth and is corroborated by a **$30.0B swing in net deferred tax** (deferred tax liabilities $919M → $22,819M; deferred tax assets $9,113M → $1,448M) — fair-value step-ups and unrealized gains creating future taxable temporary differences.
3. **SBC re-accelerating: $8,000M in Q2 (+33% YoY), $15,200M H1 (+32%).** SBC is now ~12.7% of revenue. Combined with the buyback pause, this means **dilution is back** (see §7).

---

## 5. Balance sheet: a complete transformation in six months

| Item | 2026-06-30 | 2025-12-31 | Change |
|---|---|---|---|
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| **Cash + short-term investments** | **242,474** | **126,843** | **+91.2%** |
| Accounts receivable (net) | 69,175 | 62,886 | +10.0% |
| Current assets | 343,524 | 206,038 | +66.7% |
| **Total assets** | **921,983** | **595,281** | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| Accrued income taxes (current) | 5,233 | 523 | +900% |
| **Total debt (carrying)** | **101,085** | **49,085** | **+105.9%** |
| Deferred tax liabilities (net) | 22,819 | 919 | n.m. |
| Deferred tax assets (net) | 1,448 | 9,113 | −84.1% |
| **Non-marketable equity securities** | **124,259** | **64,094** | **+93.9%** |
| Cumulative upward revaluations of those stakes | 85,732 | 44,485 | +92.7% |
| Available-for-sale debt securities | 99,500 | n/a | — |
| **Convertible preferred stock (new)** | **18,023** | **0** | new |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| AOCI | (2,285) | (1,916) | worse |
| Operating lease liability | 18,037 | 15,954 | +13.1% |
| Finance lease liability | 2,590 | 2,500 | +3.6% |
| Contract liabilities (deferred revenue) | 10,100 | 8,600 | +17.4% |
| **Loss contingency accruals (current)** | **17,356** | **15,594** | **+11.3%** |
| Shares outstanding (M) | 12,230 | 12,088 | +1.2% |
| Finite-lived intangibles (gross) | 10,585 | 2,467 | +329% |

**Interpretation — the company did something very large.** The evidence stack is unambiguous:
- Cash paid for acquisitions is an **implied residual of ~$36.3B in H1 2026** (investing-activities reconciliation below) vs ~$1.1B in H1 2025.
- Intangibles gross **+$8.1B**, deferred tax liability **+$21.9B**, non-marketable equity **+$60.2B**, and a **$135.9B non-operating gain** recognized across Q1 ($36.9B) and Q2 ($99.0B).
- Financed by **$56.2B debt, $30.5B common stock, $19.1B convertible preferred (issued 2026-06-05), and $3.8B minority proceeds.**

**This is a consolidation/mark-up event, not organic earnings.** The consequence for traders: GAAP book value and GAAP EPS are now dominated by marks that are non-cash, partly illiquid (equity securities without readily determinable fair value = $124.3B), and reversible.

**Liquidity/leverage is still pristine, despite the borrowing binge:**
- Cash + ST investments $242.5B vs total debt $101.1B → **net cash ≈ $141.4B**.
- Debt/estimated equity ≈ 16%. Net cash / estimated equity ≈ 22%.
- Current ratio ≈ 2.7x (est.). Alphabet is not remotely constrained.

**Estimated equity (not in feed — treated as an estimate):** ~$620–640B at 6/30/26, up from ~$385–400B at 12/31/25, consistent with net income +$174.8B, +$30.5B common issuance, +$19.1B preferred, +$14.8B SBC, −$5.2B dividends. Book value ≈ **$50/share** including the $18B preferred claim.

---

## 6. Cash flow: the most important section in this report

### 6.1 Cash flow reconstruction

| Item | Q2 2026 | Q1 2026 | H1 2026 | H1 2025 | YoY |
|---|---|---|---|---|---|
| Operating cash flow | 39,069 | 45,790 | **84,859** | 63,897 | **+32.8%** |
| Capital expenditures (PP&E) | (44,924) | (35,674) | **(80,598)** | (39,643) | **+103.3%** |
| **Free cash flow** | **(5,855)** | **10,116** | **4,261** | **24,254** | **−82.4%** |
| FCF margin (% of revenue) | −4.9% | 9.2% | **1.9%** | 13.0% | −1,110bp |
| Capex / revenue | 37.5% | 32.5% | **35.1%** | 21.2% | +1,390bp |
| Investing cash flow | — | — | (145,822) | (40,738) | +258% |
| Financing cash flow | — | — | +86,320 | (26,033) | n.m. |
| FX effect | — | — | (154) | +444 | — |
| Net change in cash | — | — | +25,203 | (2,430) | — |

**→ Q2 2026 is the first quarter in the modern Alphabet era with negative free cash flow.** That is the headline the market will re-rate on, and it is fully verified by SEC facts, not inference.

**Investing-activities reconciliation (proves the acquisition):**
`−80,598 (PP&E) −76,480 (marketable securities bought) +66,696 (sold/matured) −22,051 (other investments bought) +1,667 (other investments sold) +1,359 (other) = −109,545` vs reported `−145,822` → **residual ≈ −$36.3B of acquisitions, net of cash acquired.** (H1 2025 equivalent: only ~−$1.1B.)

**Accrued-but-unpaid capex is a leading indicator and it is screaming:** $29,113M at 6/30/26 vs $15,090M for all of FY2025 and $24,131M at 3/31/26. Contracted-but-unpaid spend is growing faster than cash capex → **H2 2026 capex will be higher than the $80.6B H1 run-rate.** Annualizing H1 gives ~$161B; annualizing Q2 alone gives ~$180B.

### 6.2 Quality-of-earnings flag inside operating cash flow

H1 2026 OCF of $84,859M ties out only because of very large non-cash addbacks:
- Depreciation +13,586
- SBC +15,200
- **Deferred income taxes +27,538** (vs **−1,596** in H1 2025 — a $29.1B swing)
- Amortization of intangibles +545, lease amortization ~+485
- Less: $135.9B equity gains removed, and working capital drags (IncreaseDecreaseInOtherOperatingAssets −9,950, taxes payable +8,304)

**Deferred tax of $27.5B added back means book tax expense massively exceeds cash tax paid. That will reverse.** Combined with accrued income taxes current jumping from $523M to $5,233M, a step-up in cash tax payments is a live 2027 headwind to OCF. **Do not extrapolate the +32.8% OCF growth.**

---

## 7. Capital allocation: a visible regime change

| Capital allocation item | H1 2026 | H1 2025 | Change |
|---|---|---|---|
| **Share repurchases** | **$0** | $28,306 | **Buyback fully halted** |
| Cash dividends | 5,231 | 4,977 | +5.1% |
| DPS declared | $0.43 ($0.22 Q2, up from $0.21) | $0.41 | +4.9% |
| Preferred dividends | 86 | 0 | new |
| Debt issued (net of costs) | 56,226 | 31,378 | +79.2% |
| Debt repaid | 5,253 | 18,397 | −71.4% |
| Common stock issued | 30,499 | 0 | new |
| Convertible preferred issued | 19,063 (19,000 on 2026-06-05) | 0 | new |
| Minority interest proceeds | 3,758 | 400 | +840% |
| Finance lease principal | 840 | 302 | +178% |

**Three actionable conclusions:**
1. **The buyback — Alphabet's largest historical EPS lever — is gone.** Net share count rose from 12,088M to 12,230M (+1.2%) in six months, and diluted shares +0.8% YoY, despite $8.0B/quarter of SBC. The EPS tailwind from shrinkage is over; you now have ~1.5–2% annual dilution.
2. **Implied common issuance price ≈ $215/share** ($30,499M / ~142M net new shares). Flag as an inference: if any of the $30.5B is option proceeds, the true issuance price is higher. It nonetheless brackets where stock consideration was struck in H1 2026.
3. **A new $18.0B convertible preferred claim sits ahead of common**, carrying $86M of dividends in a partial quarter. Dilution/overhang risk if the conversion strike is approached, plus a small permanent preferred dividend drain.

---

## 8. Forward-looking signals embedded in the data

| Signal | Evidence | Implication |
|---|---|---|
| Capex still ramping | Accrued capex $29.1B (record); Q2 capex +100% YoY | FCF likely negative again in Q3/Q4 2026 |
| Depreciation cliff ahead | Dep +43% YoY on $80.6B H1 capex at only 5.9% of revenue | Operating margin 34% is at risk over 4–8 quarters |
| Tax rate reset higher | ETR 19.1% (two straight quarters) vs 16.9% | ~$0.10–0.15/quarter core EPS headwind |
| Deferred tax normalization | +$27.5B DT addback in OCF | Future cash-tax step-up, OCF quality risk |
| Intangible amortization ramp | Schedule: remainder-FY26 $747M, FY27 $1,304M, FY28 $1,142M, FY29 $1,096M, FY30 $1,055M | Small (~$1.3B/yr) but permanent P&L drag from the acquisition |
| Debt maturity profile (as of 12/31/25) | $2.0B (NTM), $1.0B, $2.68B, $1.76B, $5.5B, $36.1B (>5yr) | The new 2026 debt largely pushed maturities out; refinancing risk minimal |
| Lease commitments | Operating $21.3B undiscounted; finance $2.9B | Fixed-cost leverage, ~$3.5B/yr op-lease cash |

---

## 9. Contingencies and other watch items

- **Loss contingency accruals (current): $17,356M**, up from $15,594M. This is a large, growing regulatory/antitrust/legal reserve; the FY2025 10-K also discloses $3.0B of contingency payments made in Q3 FY2025. Legal overhang is persistent and material.
- **AFS securities portfolio marks:** $53,239M of securities in an unrealized-loss position, $416M accumulated loss (widened from $178M at year-end; long-duration bucket >12 months: $3,888M position / $150M loss). Immaterial to capital, but the **$49.4B in the <12-month loss bucket** signals recent rate moves — a rate-driven AOCI drag is plausible.
- **Non-marketable equity $124.3B** with $85.7B of cumulative upward revaluations and $9.1B downward. If any of these marks (or the consolidated AI asset's implied valuation) resets, GAAP earnings can swing by tens of billions in a single quarter — **in either direction**. This is now a genuine, second-order "earnings volatility" factor for GOOGL that did not exist before.
- **Interest expense: $1,278M in Q2 (+389% YoY)** and $1,811M H1. Trivial vs operating income ($40.8B), but the trend matters if debt keeps doubling.
- **Receivables quality fine:** allowance/AR 1.44% (vs 1.47% at year-end); DSO ≈ 53 days (improved from ~61).
- **Contract liabilities (deferred revenue) +17.4%** to $10.1B, and $4.9B of H1 revenue was recognized from the opening contract-liability balance — healthy Cloud/committed-contract backdrop.

---

## 10. Trading implications (specific and actionable)

**Bull case, evidence-based**
1. Revenue growth *accelerated* to +24.2% YoY with gross margin +210bp — the AI monetization is showing up in the top line, not just the narrative.
2. Net cash position of **~$141B** after funding a ~$36B acquisition and doubling debt. Balance-sheet optionality is intact; no solvency/leverage risk.
3. Core EPS growth of ~17–21% is achievable on ~20x forward core earnings (at the ~$215 implied issuance price, ~20x annualized core earnings and ~5.5x annualized revenue). Not expensive for this growth profile.
4. $242B of liquid assets means the capex program is self-fundable without equity dilution going forward.

**Bear case, evidence-based**
1. **Q2 2026 free cash flow was negative (−$5.9B), and H1 FCF fell 82% YoY to $4.3B.** With accrued capex at a record $29.1B, Q3 will likely be worse. The market has historically capitalized GOOGL on FCF; that anchor is temporarily broken.
2. **Headline EPS is unusable.** Anyone screening on "$9.11 quarterly EPS" or a ~6x P/E is looking at $136B of non-cash marks. When those marks stop (or reverse), GAAP EPS collapses toward the ~$2.60/quarter core run-rate.
3. **Buyback eliminated (−$28.3B YoY)** while SBC grows +32% — the share count is now rising, ending a decade of EPS support.
4. **Sequential operating margin compression (−210bp) with depreciation set to ramp hard from 5.9% of revenue** is the most likely source of a negative guidance surprise.
5. **Tax rate reset to 19.1%** from 16.9%, plus a $27.5B deferred-tax addback that flatters OCF and will revert.

**How I would position/trade around this**
- **Benchmark against core EPS (~$2.60/quarter, ~$10.50–11.00 annualized run-rate and rising), not GAAP.** Rebuild any model on the §3.2 bridge. Consensus numbers that lean on GAAP will look catastrophically wrong in both directions.
- **Treat FCF as a "2027–2028 story," not a 2026 metric.** If the stock sells off on negative FCF prints, that is a duration mismatch rather than a business deterioration — but only if revenue growth holds ≥20% and gross margin holds ≥60%. If *both* revenue growth decelerates below ~18% **and** FCF stays negative, that is a genuine de-rating trigger.
- **Key monitoring triggers for the next 1–2 quarters:** (a) Q3 revenue growth vs the +24.2% Q2 bar; (b) operating margin vs 34.0% — a print below ~32% is the bear signal; (c) capex guidance and the accrued-capex balance ($29.1B) — a further step-up is a negative; (d) any resumption of buybacks (strongly bullish signal that capex has peaked); (e) any reversal/impairment disclosure against the $124.3B non-marketable equity or the newly consolidated intangible base; (f) any change to the 19.1% tax rate.
- **Watch the preferred.** $18.0B of convertible preferred is a new capital-structure element. Confirm the conversion terms in the 10-Q — if the strike is near spot, add dilution to share-count models.
- **Insider signal is blank.** No authorized insider-transaction archive exists for GOOGL at this date. Do not read the absence as bullish or bearish; substitute 13F/Form 4 confirmation if another desk can source it.

---

## 11. Key summary table

| Category | Metric | Latest (Q2/H1 2026) | Prior-year comparable | Read |
|---|---|---|---|---|
| Scale | Revenue (derived), Q2 | $119,796M | $96,428M | **+24.2% YoY — accelerating** |
| Scale | Revenue (derived), H1 | $229,692M | $186,662M | +23.0% YoY; ~$480B run-rate |
| Profitability | Gross margin, Q2 | 61.6% | 59.5% | +210bp — efficiency |
| Profitability | Operating margin, Q2 | 34.0% | 32.4% | +160bp YoY but **−210bp QoQ** |
| Profitability | Operating margin, H1 | 35.0% | 33.1% | +190bp |
| Earnings | GAAP diluted EPS, Q2 | $9.11 | $2.31 | Distorted by $99.0B equity gains |
| Earnings | **Core diluted EPS (est.), Q2** | **~$2.61** | **~$2.22** | **+17.4% — the real number** |
| Earnings | Core diluted EPS (est.), H1 | ~$5.29 | ~$4.38 | +20.8% |
| Earnings | Non-operating equity gains, H1 | $135,946M | $11,044M | Non-cash; 63% of pre-tax income |
| Tax | Effective tax rate | 19.1% | 16.9% | +220bp structural headwind |
| Cash | Operating cash flow, H1 | $84,859M | $63,897M | +32.8%, flattered by $27.5B deferred tax |
| Cash | Capex, H1 | $80,598M | $39,643M | **+103.3%** |
| Cash | **Free cash flow, H1** | **$4,261M** | **$24,254M** | **−82.4% — critical negative** |
| Cash | **Free cash flow, Q2** | **−$5,855M** | positive | **First negative FCF quarter** |
| Cash | Capex / revenue, H1 | 35.1% | 21.2% | +1,390bp |
| Cash | Accrued but unpaid capex | $29,113M | $15,090M (FY25) | Capex still ramping |
| Balance sheet | Total assets | $921,983M | $595,281M (12/31/25) | **+54.9% — acquisition-driven** |
| Balance sheet | Cash + ST investments | $242,474M | $126,843M | +91.2% |
| Balance sheet | Total debt | $101,085M | $49,085M | **+105.9%** |
| Balance sheet | Net cash (est.) | ~$141,400M | ~$77,800M | Strengthened despite borrowing |
| Balance sheet | Non-marketable equity | $124,259M | $64,094M | +93.9%; illiquid, mark-sensitive |
| Balance sheet | Net deferred tax | −$21,371M (liability) | −$8,194M assets | $30.0B adverse swing |
| Balance sheet | Convertible preferred | $18,023M | $0 | New senior claim; dilution watch |
| Balance sheet | Shares outstanding | 12,230M | 12,088M | **+1.2% — dilution resumed** |
| Capital return | Buybacks, H1 | **$0** | $28,306M | **Regime change** |
| Capital return | Dividends, H1 | $5,231M | $4,977M | +5.1%; DPS $0.22/qtr (+4.9%) |
| Investment | Cash acquisitions, H1 (implied) | ~$36,300M | ~$1,100M | Major consolidation event |
| Risk | Loss contingency accruals | $17,356M | $15,594M | +11.3% legal/regulatory overhang |
| Data gap | Insider transactions | **Unavailable** | — | Not a signal; do not infer |

**Bottom line for the desk:** GOOGL's *operating* engine is stronger than at any point in this dataset — 24% revenue growth, gross margin expansion, 30% operating income growth, and a fortress net-cash balance sheet. But the *reported* numbers are now heavily distorted by a >$36B acquisition/consolidation event, $136B of non-cash equity revaluations, a $18B convertible preferred, a doubled debt load, a halted buyback, and a capex program so large that **free cash flow turned negative in Q2 2026**. Price the equity off core EPS (~$2.61/qtr and growing ~17–20%) and treat free cash flow as a 2027–28 optionality, not a 2026 valuation input — while flagging sequential margin compression, the 19.1% tax rate, and the return path of the buyback as the three highest-signal items to monitor next quarter.