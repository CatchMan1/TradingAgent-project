# GOOGL — Alphabet Inc.: Fundamental Deep-Dive
**As of 2026-09-24 | Latest filed period: Q2 FY2026 (quarter ended 2026-06-30), 10-Q accepted 2026-07-23**

---

## 0. Data provenance and how to read this report

All figures below come from a point-in-time SEC XBRL tag extract (10-Q acc. 0001652044-26-000071, filed 2026-07-23; 10-K acc. 0001652044-26-000018, filed 2026-02-05; Q1-26 10-Q acc. 0001652044-26-000048, filed 2026-04-30). Three limitations matter for how you use this note:

1. **The vendor feed is truncated alphabetically at roughly the "F/G" tags.** Explicit `Revenues`, `ResearchAndDevelopmentExpense`, `SellingAndMarketingExpense`, `StockholdersEquity`, `Goodwill`, and `PropertyPlantAndEquipmentNet` lines were **not returned**. Where revenue or R&D+S&M is shown, it is **derived by accounting identity** (`Revenue = CostsAndExpenses + OperatingIncomeLoss`; `R&D+S&M = CostsAndExpenses − CostOfRevenue − G&A`) and is labeled as derived. Those derivations are internally consistent across all four quarters and tie to operating income.
2. **Insider transaction data is unavailable** in this data package. No insider buying or selling is reported, inferred, or estimated anywhere in this note.
3. **No price/quote data was provided**, so no P/E, EV/EBITDA, or price-target math is asserted. Multiples are left to the reader using the normalized EPS figures supplied.

---

## 1. Executive summary — the five things that matter

| # | Finding | Evidence |
|---|---|---|
| 1 | **Revenue growth has accelerated to ~24% YoY and gross margin is expanding** — unusual at this scale | Derived Q2-26 revenue **$119.8B vs $96.4B (+24.2%)**; Q1-26 +21.8%. Gross margin **61.6% vs 59.5%** |
| 2 | **Core operating leverage is real, but reported EPS is dominated by a one-time equity mark** | Q2-26 operating income **$40.77B, +30.4%** (34.0% margin vs 32.4%). But **$99.0B of equity-securities gains** flowed through non-operating income, producing $9.11 diluted EPS vs ~**$2.61 "clean"** |
| 3 | **Free cash flow has effectively collapsed** — the AI capex cycle is consuming the entire business | 1H-26 capex **$80.6B vs $39.6B (+103%)**, = **35.1% of revenue**. 1H-26 FCF **$4.3B vs $24.3B**; **Q2-26 FCF was NEGATIVE ~$5.9B** |
| 4 | **Capital allocation regime has flipped: buybacks → issuance** | Buybacks **$0 in 1H-26 vs $28.3B in 1H-25**. New: **$56.2B debt**, **$30.5B common stock**, **$19.1B convertible preferred**, **$3.8B minority** |
| 5 | **The balance sheet has been transformed** — total assets **+54.9% in six months** | Assets **$921.98B vs $595.28B**. Intangibles gross +$8.1B, deferred tax liability +$21.9B, private-stake book value +$60.2B, debt +$52.0B |

**Stance:** fundamentals are *operationally* the strongest in years, but *earnings quality* and *cash conversion* have deteriorated sharply. This is a "trust the revenue line, discount the EPS line, and underwrite the capex" setup.

---

## 2. Company profile

**Alphabet Inc. (GOOGL — Class A common).** Global technology holding company. Revenue is generated through Google Services (Search & other, YouTube ads, Google Network, subscriptions/devices/Play, plus advertising-adjacent commerce), Google Cloud (infrastructure, data, AI platforms, Workspace), and Other Bets (early-stage ventures). Segment-level revenue and operating income were **not** included in this data pull — segment analysis is not possible from this feed and is not asserted here. Alphabet pays a quarterly cash dividend ($0.21 in Q1-26, $0.22 in Q2-26) and, through 1H-25, was a large-scale repurchaser; both policies changed materially in 1H-26 (see §7).

---

## 3. Income statement — quarterly reconstruction

All revenue, gross profit, R&D+S&M, and gross margin figures are **derived** (see §0); the USD cost/income lines are as filed.

| $ millions | Q1-25 | Q2-25 | Q1-26 | Q2-26 | Q2 YoY |
|---|---:|---:|---:|---:|---:|
| Revenue (derived) | 90,234 | 96,428 | 109,896 | **119,796** | **+24.2%** |
| Cost of revenue (filed) | 36,361 | 39,039 | 41,271 | **45,943** | +17.7% |
| Gross profit (derived) | 53,873 | 57,389 | 68,625 | **73,853** | +28.7% |
| *Gross margin* | *59.7%* | *59.5%* | *62.4%* | ***61.6%*** | *+210 bp* |
| R&D + S&M (derived) | 19,728 | 20,909 | 24,638 | **26,622** | +27.3% |
| *% of revenue* | *21.9%* | *21.7%* | *22.4%* | *22.2%* | *+50 bp* |
| G&A (filed) | 3,539 | 5,209 | 4,291 | **6,461** | +24.0% |
| Total costs & expenses (filed) | 59,628 | 65,157 | 70,200 | **79,026** | +21.3% |
| **Operating income (filed)** | **30,606** | **31,271** | **39,696** | **40,770** | **+30.4%** |
| *Operating margin* | *33.9%* | *32.4%* | *36.1%* | ***34.0%*** | *+160 bp* |
| Non-operating income (filed) | 37,716 | 2,662 | 37,716 | **97,983** | n.m. |
| *of which equity-securities gains* | *9,758* | *1,286* | *36,915* | ***99,031*** | *n.m.* |
| Pre-tax income (filed) | 77,412 | 33,933 | 77,412 | **138,753** | +309% |
| Tax (filed) | 15,834 | 5,737 | 15,834 | **26,560** | +363% |
| *Effective tax rate* | *20.5%* | *16.9%* | *20.5%* | *19.1%* | *+220 bp* |
| **Net income (filed)** | **61,578** | **28,196** | **61,578** | **112,193** | **+298%** |
| Diluted EPS (filed) | ~5.13 | 2.31 | ~5.13 | **9.11** | +294% |
| SBC (filed) | 5,500 | 6,000 | 7,200 | **8,000** | +33.3% |
| *SBC % of revenue* | *6.1%* | *6.2%* | *6.6%* | *6.7%* | *+50 bp* |

**Half-year comparison (filed where noted):**

| $ millions | 1H-25 | 1H-26 | % chg |
|---|---:|---:|---:|
| Revenue (derived) | 186,662 | **229,692** | **+23.0%** |
| Cost of revenue | 75,400 | 87,214 | +15.7% |
| Gross profit (derived) | 111,262 | 142,478 | +28.1% |
| R&D + S&M (derived) | 40,637 | 51,260 | +26.1% |
| G&A | 8,748 | 10,752 | +22.9% |
| **Operating income** | **61,877** | **80,466** | **+30.0%** |
| Operating margin | 33.1% | **35.0%** | +190 bp |
| Non-operating income | 13,845 | 135,699 | n.m. |
| Pre-tax income | 75,722 | 216,165 | +185% |
| Tax / ETR | 12,986 / 17.1% | 41,394 / **19.1%** | +200 bp |
| **Net income** | **62,736** | **174,771** | **+179%** |
| Diluted EPS | 5.12 | **14.24** | +178% |
| SBC | 11,500 | 15,200 | +32.2% |
| Depreciation (filed) | 9,485 | 13,586 | +43.2% |
| Amortization of intangibles | 246 | 545 | +122% |
| Net interest income (int. income − int. exp.) | 1,756 | 1,000 | −43% |

### 3.1 Income statement interpretation

- **Top line is accelerating, not decelerating.** Sequential revenue went $90.2B → $96.4B → $109.9B → $119.8B. The Q2-26 YoY rate (+24.2%) is above Q1-26 (+21.8%). For a company of this size this is the single most important data point in the file.
- **Cost of revenue is growing ~7 points slower than revenue** (+17.7% vs +24.2%). That is genuine gross-margin expansion (59.5% → 61.6%), i.e., the incremental revenue is higher-margin than the base — consistent with a mix shift toward higher-value compute/cloud/AI offerings and away from low-margin traffic-acquisition spend. *This is the strongest bull argument in the dataset.*
- **Discretionary opex is re-accelerating.** R&D+S&M grew +27.3% in Q2, faster than revenue, and G&A jumped +24% with G&A at 5.4% of revenue vs 3.9% in Q1-26 — a 150 bp sequential step-up that is unusual and may include transaction/integration costs (see §4 on the acquisition signature). Watch this line: if G&A stays elevated, some of the margin story is one-off.
- **Operating leverage is still decisively positive:** operating income +30.4% vs revenue +24.2%, margin +160 bp YoY. 1H-26 margin of 35.0% is the high-water mark in the visible history.
- **The EPS line is not the operating business.** Q2-26 non-operating income of $98.0B (of which $99.0B equity-securities marks) exceeded operating income by 2.4x. Reported diluted EPS of $9.11 is roughly **3.5x** the underlying operating earnings power.

### 3.2 Normalized ("clean") earnings — the number to actually use

Stripping equity-securities marks (`DebtAndEquitySecuritiesGainLoss`), applying the reported ETR, and using diluted share counts implied by reported EPS:

| | Q2-25 | Q2-26 | 1H-25 | 1H-26 |
|---|---:|---:|---:|---:|
| Pre-tax income | 33,933 | 138,753 | 75,722 | 216,165 |
| Less: equity-securities gains | (1,286) | (99,031) | (11,411) | (135,803) |
| Adjusted pre-tax | 32,647 | 39,722 | 64,311 | 80,362 |
| Tax @ reported ETR | 16.9% | 19.1% | 17.1% | 19.1% |
| **Adjusted net income** | **~27,130** | **~32,135** | **~53,314** | **~65,013** |
| Diluted shares (implied) | ~12,206 | ~12,313 | ~12,253 | ~12,344 |
| **Adjusted diluted EPS** | **~$2.22** | **~$2.61** | **~$4.35** | **~$5.27** |
| Growth | — | **+17.5%** | — | **+21.1%** |

**Read-through:** the true earnings growth rate is ~**18–21%**, not the ~180–300% reported. Still excellent — but it means any valuation work anchored on "trailing EPS of ~$14–19" is overstating earnings power by ~2.7–3.5x. Annualizing 1H-26 adjusted EPS gives ~**$10.5** as the run-rate earnings base; Q2's $2.61 × 4 = **$10.44**.

Two further quality-of-earnings flags:
- **Tax rate crept up** from 16.9% → 19.1% (Q2) and 17.1% → 19.1% (1H), a ~220 bp headwind. 1H-26 includes a **$27.5B deferred tax charge** (`DeferredIncomeTaxesAndTaxCredits` = +27,538 vs −1,596 in 1H-25) — a non-cash item consistent with acquired intangibles being booked gross with a DTL.
- **SBC is growing 32–33% YoY**, faster than revenue, and now runs at **6.7% of revenue (~$32B annualized)**. Buybacks previously offset this; with buybacks at zero in 1H-26, share count rose from **12.088B to 12.230B** — i.e., **net dilution is back**. This is a real, recurring cost to per-share value.

---

## 4. Balance sheet — 6/30/26 vs 12/31/25

| $ millions | 12/31/25 | 6/30/26 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 30,708 | **55,911** | +82.1% |
| **Cash + short-term investments** | **126,843** | **242,474** | **+91.2%** |
| Accounts receivable, net | 62,886 | 69,175 | +10.0% |
| Available-for-sale debt securities | n/a | **99,500** | — |
| Equity securities w/o readily determinable FV | 64,094 | **124,259** | +93.9% |
| **Current assets** | **206,038** | **343,524** | **+66.7%** |
| **Total assets** | **595,281** | **921,983** | **+54.9%** |
| Accounts payable | 12,200 | 20,258 | +66.0% |
| Accrued liabilities | 55,557 | 73,014 | +31.4% |
| Accrued income taxes – current | 523 | 5,233 | 10.0x |
| Contract liability – current (deferred revenue) | 6,578 | 7,154 | +8.8% |
| Employee-related liabilities | 17,546 | 15,086 | −14.0% |
| Loss contingency accrual – current | 15,594 | **17,356** | +11.3% |
| Commercial paper | 0 | 0 | — |
| **Debt, gross carrying amount** | **49,085** | **101,085** | **+106.0%** |
| Unamortized discount & issuance costs | (542) | (921) | — |
| Operating lease liability | 15,954 | 18,037 | +13.1% |
| Finance lease liability | 2,500 | 2,590 | +3.6% |
| Deferred income tax liabilities, net | 919 | **22,819** | 24.8x |
| Accrued income taxes – noncurrent | 9,531 | 11,306 | +18.6% |
| **Convertible preferred stock (non-redeemable)** | **0** | **18,023** | **new** |
| Common stock + APIC | 93,126 | 131,371 | +41.1% |
| AOCI | (1,916) | (2,285) | — |
| Shares outstanding | 12.088B | **12.230B** | +1.2% |
| Contract liability – noncurrent | 8,600 | 10,100 | +17.4% |

**Derived liquidity metrics:** current ratio ≈ **2.4x** (current assets $343.5B vs disclosed current liabilities aggregating ≈$142B — note the current portion of operating leases was not exposed in this pull, so treat as approximate). Working capital ≈ **+$201B**. Net cash (cash + ST investments − gross debt) ≈ **+$141B**. Interest coverage: 1H-26 operating income $80.5B ÷ interest expense $1.81B ≈ **44x**.

### 4.1 Balance sheet interpretation

- **This is not a steady-state balance sheet; it is a post-transaction balance sheet.** Five independent signatures point to a material business combination (or a package of them) plus major strategic investments closing in 1H-26:
 1. **Finite-lived intangibles gross: $2,467M → $10,585M** (+$8.1B), with amortization expense tripling ($124M → $367M per quarter) and forward amortization guided by the disclosed schedule ($1,304M next 12 months, then ~$1.14B, ~$1.10B, ~$1.06B).
 2. **Deferred tax liabilities: $0.9B → $22.8B** — the textbook footprint of booking acquired intangibles at fair value with a simultaneous DTL.
 3. **Convertible preferred stock: $0 → $18.0B** (issued 2026-06-05; proceeds $19.06B, of which $19.0B on that date) with **$86M of preferred dividends** in Q2-26.
 4. **Common stock issued for cash: $30.5B** (`ProceedsFromIssuanceOfCommonStock`, zero in 1H-25) plus **$3.76B from minority shareholders**.
 5. **Derivative liabilities: $0.38B → $1.96B**, consistent with hedges/convert structures around the new instruments.
 *The feed does not identify the counterparty or the purchase price, so I do not name a target. The size of the equity raise (>$50B of new common + preferred) implies a very large ticket.*
- **Private-stake exposure is now enormous and marked upward.** `EquitySecuritiesWithoutReadilyDeterminableFairValue` = **$124.3B, or 13.5% of total assets**, up from $64.1B. Cumulative **upward** adjustments rose $44.5B → **$85.7B** while cumulative downward adjustments were flat ($8.8B → $9.1B). Level-3, model-priced assets of this magnitude are a valuation and disclosure risk; they are also the likely source of a portion of the P&L gains (though the $135.9B 1H-26 gain cannot be fully explained by the +$41B cumulative revaluation, suggesting a realized/IPO-type event on a marketable position that the truncated tag set does not isolate).
- **Debt doubled to $101.1B**, but it remains cheap and comfortably serviced: interest expense is 1.6% of revenue in Q2 (1,278/119,796) and coverage is 44x. **The maturity ladder from the 10-K is benign**: $2.0B due in 12 months, $1.0B yr-2, $2.7B yr-3, $1.8B yr-4, $5.5B yr-5, and $36.1B beyond year five.
- **Deferred revenue is growing slower than revenue** (+8.8% current, +17.4% noncurrent), which is a mild negative read on forward-booked commitments relative to the 24% top-line growth — worth watching in the cloud business.
- **Legal/regulatory accruals are rising**: loss-contingency current accrual **$17.4B** (+11.3%), and the FY2025 10-K discloses **$3.0B of contingency payments** in Q3-25. This is a persistent, non-trivial drag.
- **AR grew only +10% against +23% revenue** → DSO of ~53 days (Q2-26 revenue basis) is stable-to-improving. No receivables-quality problem. Allowance for doubtful accounts is immaterial ($995M on $69.2B AR, 1.4%).

---

## 5. Cash flow — the crux of the thesis

| $ millions | 1H-25 | 1H-26 | Change |
|---|---:|---:|---:|
| **Operating cash flow** | **63,897** | **84,859** | **+32.8%** |
| Capex (cash, PP&E purchases) | (39,643) | **(80,598)** | **+103.3%** |
| *Capex as % of revenue* | *21.2%* | ***35.1%*** | *+1,390 bp* |
| **Free cash flow** | **24,254** | **4,261** | **−82.4%** |
| *FCF margin* | *13.0%* | *1.9%* | *−1,110 bp* |
| Acquisitions of marketable securities | (39,870) | (76,480) | +91.8% |
| Sales/maturities of marketable securities | 40,930 | 66,696 | +62.9% |
| Purchases of other investments | (2,312) | **(22,051)** | 9.5x |
| **Investing cash flow** | **(40,738)** | **(145,822)** | 3.6x |
| Proceeds from debt | 31,378 | **56,226** | +79.2% |
| Repayments of debt/lease obligations | (18,397) | (5,253) | −71.4% |
| **Repurchases of common stock** | **(28,306)** | **0** | **−100%** |
| Dividends paid | (4,977) | (5,231) | +5.1% |
| Issuance of common stock | 0 | **30,499** | new |
| Issuance of convertible preferred | 0 | **19,063** | new |
| Proceeds from minority shareholders | 400 | 3,758 | 9.4x |
| **Financing cash flow** | **(26,033)** | **+86,320** | n.m. |
| FX effect on cash | 444 | (154) | — |
| **Net change in cash** | **(2,430)** | **+25,203** | n.m. |
| Capex incurred but **not yet paid** (period end) | 10,635 | **29,113** | 2.7x |

**Quarterly cash-flow bridge (derived from cumulative filings):**

| $ millions | Q1-25 | Q2-25 | Q1-26 | Q2-26 |
|---|---:|---:|---:|---:|
| CFO | 36,150 | 27,747 | 45,790 | **39,069** |
| Capex | (17,197) | (22,446) | (35,674) | **(44,924)** |
| **FCF** | **18,953** | **5,301** | **10,116** | **(5,855)** |

**Historical financing/FCF trajectory (10-K):** financing cash flow was **−$72.1B (FY23)**, **−$79.7B (FY24)**, **−$37.4B (FY25)** — a three-year pattern of massive capital return. Unpaid capex accruals: **$7.4B (FY23) → $10.3B (FY24) → $15.1B (FY25) → $29.1B (1H-26)** — an unambiguous, escalating infrastructure commitment.

### 5.1 Cash flow interpretation

- **CFO +32.8% is the cleanest confirmation that the operating business is genuinely accelerating.** It outpaces even revenue growth, which is what you want to see.
- **But capex has more than doubled and now eats 103% of CFO.** FCF of $4.3B on $229.7B of revenue (1.9% margin) is a different company than the 13% FCF-margin business of 1H-25. **Q2-26 was FCF-negative (~−$5.9B)** — the first clearly negative quarter in the visible record.
- **The $29.1B of capex incurred but unpaid is the tell for Q3.** Cash capex will likely run *above* the P&L-accrued level in Q3-26 as these payables settle. Do not assume Q2 is the peak.
- **CFO/NI = 0.49** is not a red flag about collections; it is the mechanical result of $135.9B of non-cash equity gains in net income. Normalizing for that, cash conversion is healthy.
- **The financing side is the story.** Alphabet borrowed $56.2B, issued $30.5B of stock and $19.1B of convertible preferred, took $3.8B from minority holders, paid zero buybacks, and still only grew cash by $25B. Cash + investments rose $115.6B, but **$83B of that came from financing, not operations.** This is a company funding an investment super-cycle externally rather than internally — a marked departure from the 2023–25 regime.

---

## 6. Financial history summary

| Metric | FY2023 (10-K) | FY2024 (10-K) | FY2025 (10-K) | 1H-25 | 1H-26 |
|---|---:|---:|---:|---:|---:|
| Financing cash flow | −72,093 | −79,733 | −37,388 | −26,033 | **+86,320** |
| Capex incurred, unpaid (YE) | 7,435 | 10,326 | 15,090 | 10,635 | **29,113** |
| Finance lease principal payments | 705 | 405 | 1,988 | 302 | 840 |
| Revenue (derived, where available) | n/a | n/a | n/a | 186,662 | **229,692** |
| Operating income (filed) | n/a | n/a | n/a | 61,877 | **80,466** |
| Operating margin | n/a | n/a | n/a | 33.1% | **35.0%** |
| Net income (filed) | n/a | n/a | n/a | 62,736 | **174,771** |
| Diluted EPS (filed) | n/a | n/a | n/a | 5.12 | **14.24** |
| Adjusted diluted EPS (est.) | n/a | n/a | n/a | ~4.35 | **~5.27** |
| CFO | n/a | n/a | n/a | 63,897 | **84,859** |
| FCF | n/a | n/a | n/a | 24,254 | **4,261** |
| Dividends/share | n/a | n/a | ~0.84 | 0.41 | **0.43** |
| Shares outstanding (period end) | n/a | n/a | 12.088B | n/a | **12.230B** |

*Full-year revenue/operating income tags for FY23–FY25 were not exposed by this feed; the annual columns are therefore limited to the cash-flow and leasing items that were returned. I have not estimated the missing annual P&L lines.*

---

## 7. Capital allocation and financing strategy — the regime change

Four discrete decisions in 1H-26 tell you how management is prioritizing capital:

1. **Buybacks went to exactly zero** (from $28.3B in 1H-25, and $15.1B in Q1-25 alone). Every dollar of repurchase capacity was redirected.
2. **Dividends continued and were raised** ($0.41 → $0.43 per share for 1H; $0.21 → $0.22 quarterly). Cost: $5.2B in 1H-26, an implied ~$10.5B annualized — roughly **6% of adjusted net income**, so coverage is not in question. But the tag `AdjustmentsToAdditionalPaidInCapitalDividendsInExcessOfRetainedEarnings` ($5,252M in 1H-26) hints at a reclassification/retained-earnings constraint worth monitoring in the 10-Q text.
3. **Debt was doubled** ($49.1B → $101.1B), with $56.2B raised and only $5.3B repaid. At 44x coverage this is opportunistic, not distress — but it does convert a net-cash-funded equity story into one with a growing fixed charge ($1.28B/quarter and rising).
4. **Equity was issued at scale, including a novel $19B convertible preferred** carrying $86M/quarter of preferred dividends (a ~1.8% implied coupon) with conversion/dilution optionality. Combined with $30.5B of common and net share count **up 1.2%**, per-share value is now being diluted rather than accreted — the reverse of the 2023–25 pattern.

**Interpretation:** management is behaving as if the AI infrastructure opportunity has a higher marginal return than its own stock. That is a defensible strategic bet, but it removes the buyback bid that historically supported the multiple, adds leverage, and makes the equity a *capex-execution* story rather than a *capital-return* story.

---

## 8. Insider transactions

**No data available.** The vendor package contains no authorized, point-in-time insider-transactions archive for GOOGL as of 2026-09-24. **No insider buying or selling is inferred, estimated, or fabricated in this report.** Treat the insider signal as *absent* rather than neutral — do not read it as either confirmation or warning.

---

## 9. Actionable insights for traders

**What the data supports (high confidence):**
1. **Own the revenue/operating-income trajectory.** +23–24% revenue with +160–190 bp of operating margin expansion and +30% operating income is a rare combination at this scale. If you are modeling GOOGL, model **operating income of ~$160B annualized** (1H-26 $80.5B × 2) and revenue of **~$460B annualized**, not the reported net income line.
2. **Do not underwrite reported EPS.** Q2-26 EPS of $9.11 contains ~$6.50 of mark-to-market gains. Any screen, consensus comparison, or P/E computed on GAAP EPS is measuring a securities portfolio, not the search/cloud franchise. Use **~$10.4–10.6 annualized adjusted EPS** as the earnings base.
3. **The FCF story is broken for now — price it.** FCF fell 82% to $4.3B and Q2 was negative. With $29.1B of unpaid capex rolling into Q3, **expect FY26 FCF to be the lowest in years**. Any DCF or FCF-yield-based valuation must use a multi-year capex normalization assumption, and the burden of proof is on management to show a return on this spend (watch for cloud backlog/deferred revenue acceleration — currently *only* +8.8% current / +17.4% noncurrent, which is not yet validating the spend).
4. **Watch the dilution math.** SBC +32% YoY at 6.7% of revenue, zero buybacks, share count +1.2%, plus $18B of convertible preferred. Net dilution of ~1.5–2.5%/yr is a direct haircut to per-share compounding.
5. **The balance sheet is now a source of both cushion and complexity.** Net cash of ~$141B and 44x interest coverage mean no solvency risk. But $124B of Level-3 private stakes (13.5% of assets) and $22.8B of new DTLs mean book value is soft and future marks will be volatile in *both* directions — a source of EPS noise for at least the next several quarters.

**Specific things to check next (catalysts / falsifiers):**
- **Q3-26 10-Q (due ~late Oct 2026):** (a) does capex/revenue peak above 35%? (b) does G&A stay at ~5.4% of revenue or revert to ~3.9%? (c) does the current contract liability (deferred revenue) growth re-accelerate above 15%? (d) any disclosure naming the 1H-26 acquisition and its purchase price allocation — this is the single largest information gap in the file.
- **Capex guide vs. CFO:** if FY26 capex lands below ~$160B, the FCF inflection is earlier than feared and the equity re-rates; if above ~$180B, FCF stays near zero into 2027.
- **Buyback resumption:** any restart would be a strong signal that management sees the capex peak, and would reverse the dilution headwind.
- **Convertible preferred terms** (conversion price, dividend step-ups) — not in this feed, but material to diluted share count.
- **Private-stake marks:** a single down-round or IPO revaluation can swing EPS by tens of billions. Treat any quarter's GAAP EPS with suspicion in both directions.

**Net assessment:** *Operationally bullish, financially cautious.* The franchise is accelerating and margins are expanding — that is the durable signal. But reported earnings are ~70% non-operating, free cash flow has gone to near-zero, and the company has switched from returning ~$80B/yr to raising ~$110B in six months. A trader should be **constructive on the operating trend but demand a wider margin of safety than the GAAP P/E implies**, and should treat the equity as levered to AI-capex ROI rather than to search advertising.

---

## 10. Key points summary table

| Category | Metric | Value | Signal |
|---|---|---:|---|
| **Growth** | Q2-26 revenue (derived) | $119.80B, **+24.2% YoY** | 🟢 Accelerating |
| | 1H-26 revenue (derived) | $229.69B, +23.0% YoY | 🟢 |
| | Q2-26 gross margin | 61.6% (vs 59.5%) | 🟢 +210 bp |
| **Profitability** | Q2-26 operating income | $40.77B, **+30.4%** | 🟢 Leverage |
| | Operating margin | 34.0% (1H: 35.0%) | 🟢 Multi-year high |
| | R&D+S&M % revenue | 22.2% (stable) | 🟡 Re-accelerating |
| | G&A % revenue | 5.4% (vs 3.9% Q1) | 🔴 Unexplained step-up |
| **Earnings quality** | Reported Q2 diluted EPS | $9.11 | 🔴 3.5x clean |
| | Adjusted Q2 diluted EPS (est.) | **~$2.61, +17.5%** | 🟡 Solid but slower |
| | Adjusted 1H EPS (est.) | ~$5.27, +21.1% | 🟡 |
| | Equity-securities gains in 1H | **$135.8B** | 🔴 Non-cash, non-recurring |
| | Effective tax rate | 19.1% (vs 16.9%) | 🔴 +220 bp headwind |
| **Cash flow** | 1H-26 CFO | $84.86B, **+32.8%** | 🟢 Best-in-class |
| | 1H-26 capex | **$80.60B, +103%** (35.1% of rev) | 🔴 Super-cycle |
| | 1H-26 FCF | **$4.26B vs $24.25B (−82%)** | 🔴 Collapse |
| | Q2-26 FCF | **≈ −$5.86B** | 🔴 Negative |
| | Unpaid capex at 6/30 | **$29.11B** | 🔴 Q3 cash drag |
| **Balance sheet** | Total assets | **$921.98B (+54.9% in 6 mo)** | 🟡 Transformed |
| | Cash + ST investments | $242.47B | 🟢 |
| | Gross debt | $101.09B (+106%) | 🟡 Doubled |
| | Net cash | **≈ +$141B** | 🟢 |
| | Interest coverage (1H) | ~44x | 🟢 |
| | Current ratio (approx.) | ~2.4x | 🟢 |
| | Private equity stakes (Level 3) | **$124.26B = 13.5% of assets** | 🔴 Mark-to-model risk |
| | Deferred tax liabilities | $22.82B (vs $0.92B) | 🟡 Acquisition footprint |
| | Convertible preferred | **$18.02B (new)** | 🟡 New claim/dilution |
| **Capital allocation** | Buybacks 1H-26 | **$0 vs $28.31B** | 🔴 Support removed |
| | Common stock issued 1H-26 | **$30.50B** | 🔴 Dilution |
| | Dividends 1H-26 | $5.23B (≈6% of adj. NI) | 🟢 Well covered |
| | Shares outstanding | 12.230B (+1.2% in 6 mo) | 🔴 Net dilution |
| | SBC 1H-26 | $15.20B, +32.2% (6.7% of rev) | 🔴 Rising |
| **Balance/other** | Loss contingency accrual (current) | $17.36B (+11.3%) | 🔴 Legal overhang |
| | AR / DSO | $69.18B / ~53 days | 🟢 Clean |
| | Deferred revenue growth | +8.8% current / +17.4% noncurrent | 🟡 Lags revenue |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | ⚪ Not assessable |

---

*Prepared from SEC XBRL facts publicly accepted on or before 2026-09-24. Revenue, gross profit, and R&D+S&M are derived by accounting identity because those tags were not exposed by the data feed; all other figures are as filed. Adjusted EPS is an analyst-constructed normalization (stripping equity-securities marks at the reported tax rate) and is not a company-reported non-GAAP measure. No insider data, price data, segment data, or full-year P&L data was available; nothing in those areas is estimated or asserted.*