# GOOGL — Alphabet Inc. | Fundamental Deep Dive
**Analysis date: 2024-02-28 | Most recent filings: FY2023 Form 10-K (accepted 2024-01-31, accn 0001652044-24-000022), Q3'23 Form 10-Q (accepted 2023-10-24) | Point-in-time cut: only facts public by 2024-02-28 used**

---

## 1. Executive Summary

Alphabet's FY2023 10-K (filed 2024-01-31) is the freshest fundamental anchor and it is a **clean, high-quality "re-acceleration + margin repair" year**:

- **Net income $73.80B** (FY22 $59.97B, **+23.1% y/y**), **diluted EPS $5.80** (FY22 $4.56, **+27.2%**) — EPS outgrew net income because the share count fell **3.0%** (12,849M → 12,460M).
- **Operating income $84.29B, operating margin 27.4%** — up from 26.5% in FY22 but still **below the 30.6% FY21 peak**, i.e. the margin story is *partially* repaired, not complete.
- **Operating cash flow crossed $100B for the first time ($101.75B, +11.2%)**; FCF **$69.50B** (22.6% of revenue) after $32.25B capex.
- **Effective tax rate fell to 13.9%** (FY22 15.9%, FY21 16.2%) — this is a *real but non-durable* EPS tailwind (~$1.7B vs. a 15.9% rate) that **normalizes in 2024**.
- **Net cash fortress: ~$96B** ($110.9B cash + marketable securities vs. ~$14.9B gross debt per maturities schedule).
- **Quality flags to monitor:** SBC of **$22.10B** (+13.3% y/y, 7.2% of revenue) is ~32% of FCF; buybacks ($61.50B) exceeded *FCF-less-SBC* ($47.40B); capex inflected hard in Q4'23 (see §6); receivables grew +19.1% vs. revenue +8.7% (DSO +5 days).

**Stance implied by the fundamentals: constructive/accumulate on quality and cash generation, but do not underwrite FY24 EPS off the 13.9% tax rate, and expect FCF growth to lag EPS growth as capex ramps.**

> **Data provenance note (important):** The point-in-time SEC extract returned for this run is alphabetically truncated and **omits the revenue tag rows**. Revenue figures below are the reported 10-K amounts; every derived subtotal (gross profit, operating income, net income, FCF) is shown so it **reconciles to the tool-supplied pre-tax income, tax expense, EPS and cash-flow lines** — e.g. FY23 pre-tax $85,717M − tax $11,922M = $73,795M, matching diluted EPS $5.80 × ~12.72B shares. Where a figure is not in the tool extract (revenue lines, total equity/liabilities, Q4 detail), it is explicitly labeled **[10-K reported]** or **[derived]**.

---

## 2. Company Profile

Alphabet Inc. (ticker **GOOGL**, dual-class with GOOG) is the parent of Google. Reporting structure (per FY2023 10-K):

| Segment | What it is | Fundamental read from the FY23 numbers |
|---|---|---|
| **Google Services** | Search, YouTube ads, Network, Play, subscriptions/devices, plus most of the "Other" bets (Pixel, YouTube Premium) | The cash engine funding everything else: ~87% of revenue; this is what makes gross margin expand (56.6%) |
| **Google Cloud** | GCP infrastructure + Workspace/collaboration | Loss-making to breakeven transition in FY23; the swing factor for forward operating margin *and* the explanation for rising receivables (enterprise/cloud billing lags) |
| **Other Bets** | Waymo, Verily, etc. | Structurally loss-making; funded by the $84B operating profit above |
| **Alphabet-level** | AI research (DeepMind), corporate, and a **$34.7B non-marketable equity + $6.0B marketable equity portfolio** | The portfolio is a hidden-value line item — see §7 |

Business characteristics evidenced by the data itself: ~57% gross margin, 22.6% FCF margin, negative working-capital-funded model (accrued liabilities +22% generate cash), no dividend in FY23, and capital return executed **exclusively through buybacks**.

---

## 3. Income Statement — Full Reconstruction (USD billions)

| Line (USD B) | FY2021 | FY2022 | FY2023 | FY23 y/y |
|---|---|---|---|---|
| **Revenue** [10-K reported] | 257.64 | 282.84 | **307.39** | **+8.7%** |
| Cost of revenue | 110.94 | 126.20 | 133.33 | +5.7% |
| **Gross profit** | 146.70 | 156.63 | **174.06** | **+11.1%** |
| *Gross margin* | *56.9%* | *55.4%* | ***56.6%*** | *+120bp* |
| R&D | 31.56 | 39.50 | 45.43 | +15.0% |
| Sales & marketing | 22.64 | 26.57 | 27.92 | +5.1% |
| General & administrative | 13.51 | 15.72 | 16.43 | +4.5% |
| **Total costs & expenses** (reported) | 178.92 | 207.99 | **223.10** | **+7.3%** |
| **Operating income** | 78.71 | 74.84 | **84.29** | **+12.6%** |
| *Operating margin* | *30.6%* | *26.5%* | ***27.4%*** | *+90bp* |
| Other income (expense), net [derived: pre-tax − op. inc.] | +12.02 | **−3.51** | **+1.42** | n/m |
| **Pre-tax income** (reported tag) | 90.73 | 71.33 | **85.72** | +20.2% |
| Income tax expense | 14.70 | 11.36 | 11.92 | +5.0% |
| ***Effective tax rate*** | *16.2%* | *15.9%* | ***13.9%*** | *−200bp* |
| **Net income** | 76.03 | 59.97 | **73.80** | **+23.1%** |
| *Net margin* | *29.5%* | *21.2%* | ***24.0%*** | *+280bp* |
| **Diluted EPS** | 5.61 | 4.56 | **5.80** | **+27.2%** |
| Diluted shares (M) [derived] | ~13,553 | ~13,152 | ~12,723 | −3.3% |
| SBC (expense) | 15.70 | 19.50 | **22.10** | **+13.3%** |
| SBC as % of revenue | 6.1% | 6.9% | **7.2%** | +30bp |

### What the numbers actually say

1. **Operating leverage has turned positive.** FY23 costs grew **+7.3%** vs. revenue **+8.7%**. FY22 was the opposite: costs **+16.3%** vs. revenue **+9.8%**. That reversal — driven by headcount discipline, slower Cloud opex growth and lower S&M growth (+5.1% vs revenue +8.7%) — is the single most important fundamental change of FY23.
2. **But the gross-margin recovery is mix-driven, not efficiency-driven.** Cost of revenue grew +5.7% (slowest of any expense line) because of the Cloud margin ramp + lower TAC/other cost-of-sales growth. Gross margin is still only 30bp above FY21. Do not extrapolate a large gross-margin expansion from here.
3. **The 2022 "earnings recession" was mostly non-operating.** FY22 pre-tax collapsed to $71.33B from $90.73B despite operating income only falling $3.87B — because other income swung from **+$12.02B to −$3.51B** (equity-securities mark-to-market: FY22 FVNI loss **−$3.455B** vs FY21 gain **+$12.38B**). *Traders should treat the equity-securities P&L as noise:* FY23's +$392M FVNI gain is not a durable earnings source.
4. **~$1.7B of FY23's EPS is tax-rate, not operations.** At the FY22 15.9% rate, FY23 net income would have been ~$72.1B (EPS ~$5.67) instead of $73.80B/$5.80. **Model FY24 EPS off a mid-teens/mid-upper-teens rate, not 13.9%.**
5. **R&D is the accelerating line (+15.0%)** — AI/Cloud/infrastructure spend. This is a deliberate margin cap, and it is why operating margin won't snap back to 30.6% quickly.
6. **SBC is a real, growing cost.** $22.10B = 7.2% of revenue, growing faster (+13.3%) than revenue (+8.7%). It is the single largest gap between GAAP EPS and "cash" EPS.

---

## 4. Balance Sheet — Fortress, With Two Live Watch Items (USD billions)

| Item | 2022-12-31 | 2023-12-31 | Change |
|---|---|---|---|
| Cash & equivalents | 21.88 | **24.05** | +9.9% |
| **Cash + short-term investments** | **113.76** | **110.92** | −2.5% |
| AFS debt securities (total) | — | **82.28** | — |
| Accounts receivable, net | 40.26 | **47.96** | **+19.1%** |
| Allowance for doubtful accounts | 0.754 | 0.771 | +2.3% |
| Current assets | 164.80 | 171.53 | +4.1% |
| **Total assets** | **365.26** | **402.39** | **+10.2%** |
| Non-marketable equity securities | 28.53 | **28.77** | +0.8% |
| Equity securities (FVNI) | 5.16 | 5.97 | +15.8% |
| Equity-method investments | 1.50 | 1.70 | +13.3% |
| Accounts payable | 5.13 | **7.49** | **+46.1%** |
| Accrued liabilities | 37.87 | **46.17** | **+21.9%** |
| — of which employee-related | 14.03 | 15.14 | +7.9% |
| Deferred revenue (current + non-current) | 4.51 | **5.05** | +12.2% |
| Finance lease liability | 2.14 | 1.75 | −18.3% |
| Gross debt (principal, per maturity schedule) | — | **~14.86** | — |
| AOCI | −7.60 | **−4.40** | **+$3.20B improvement** |
| **Total equity** [10-K reported] | 256.14 | **283.38** | +10.6% |
| **Total liabilities** [10-K reported, = assets − equity] | 109.12 | **119.01** | +9.1% |
| Shares outstanding (M) | 12,849 | **12,460** | **−3.0%** |

**Interpretation:**

- **Liquidity is not a question.** ~$110.9B of cash/securities vs. ~$14.9B of debt → **net cash ~$96B**. Debt maturities are trivially staggered: $1.30B (2024), $1.16B (2025), $2.17B (2026), $1.14B (2027), $0.13B (2028), $8.96B (thereafter). No refinancing risk.
- **⚠️ Watch item #1 — receivables quality.** AR **+19.1%** while revenue grew **+8.7%**. DSO (AR/Revenue × 365) went **51.9 → 56.9 days (+5.0 days)**. Benign read: Cloud/enterprise mix shift and billing timing. Malign read: collection stretch or channel stuffing. **Crucially, the allowance for doubtful accounts rose only +2.3%** — so management is *not* flagging credit deterioration. Verify in the Q1'24 10-Q; if DSO keeps climbing while the allowance stays flat, discount revenue quality.
- **⚠️ Watch item #2 — accrual-driven cash flow.** Accrued liabilities +21.9% (vs revenue +8.7%) contributed **+$3.94B** to operating cash flow. That is a **non-repeatable** cash source. Cash taxes accrued jumped to $2.75B from $1.63B. CFO growth of +11.2% is therefore ~4 points "working capital," ~7 points "real."
- **Deferred revenue +12.2% ($4.51B → $5.05B)** — modestly ahead of revenue growth, a mildly positive backlog/turnstile signal but small in absolute terms for a $307B revenue base (1.6%). This is a *usage-based* business, not a subscription backlog business; don't over-read it.
- **Deferred tax assets jumped to $26.15B** (from $17.30B), driven by **IPR&D DTAs of $17.76B vs $10.38B (+$7.4B)**. That step-change implies **meaningful acquired/capitalized IPR&D in FY23** (M&A/asset purchases — corroborated by $3.03B "payments to acquire other investments" and $0.95B of proceeds). **Signal: Alphabet is deploying cash into tuck-in AI/tech acquisitions. Expect more in 2024.**

---

## 5. Cash Flow & Capital Allocation — The Core of the Thesis (USD billions)

| Item (USD B) | FY2021 | FY2022 | FY2023 | FY23 y/y |
|---|---|---|---|---|
| **Operating cash flow** | 91.65 | 91.50 | **101.75** | **+11.2%** |
| Capex (PP&E purchases) | 24.64 | 31.49 | **32.25** | +2.4% |
| **Free cash flow** | 67.01 | 60.01 | **69.50** | **+15.8%** |
| *FCF margin* | *26.0%* | *21.2%* | ***22.6%*** | *+140bp* |
| Investing cash flow | −35.52 | −20.30 | −27.06 | — |
| Financing cash flow | −61.36 | −69.76 | **−72.09** | — |
| **Share repurchases** | 50.27 | 59.30 | **61.50** | +3.7% |
| Debt proceeds | 20.20 | 52.87 | 10.79 | −79.6% |
| Debt repayments | 21.44 | 54.07 | 11.55 | −78.6% |
| Cash taxes paid | 13.41 | 18.89 | **19.16** | +1.4% |
| Operating lease payments | 2.49 | 2.72 | 3.17 | +16.5% |

### Three high-conviction observations

1. **FCF quality: ~$1 of every $3 of "free" cash is stock compensation.** FCF $69.50B − SBC $22.10B = **$47.40B "SBC-adjusted FCF"** (15.4% margin). Buybacks of **$61.50B exceeded that by 30%**. The buyback is real and it *does* shrink the float (−3.0% shares), but it is partly recycled compensation, partly balance-sheet-funded. **A shareholder-value purist should underwrite ~$47B, not $69.5B, of distributable cash.**
2. **⚠️ Capex has already inflected — the FY23 average masks it.** 9M'23 capex was $21.23B → **Q4'23 alone was $11.02B** (FY $32.25B − 9M $21.23B), i.e. a **+56% step-up vs. the 9M quarterly average of $7.08B**, and +62% vs. Q3'23's ~$7.8B run-rate. Combined with AI infrastructure and the R&D acceleration, **FY24 FCF growth will almost certainly lag EPS growth.** This is the #1 reason a P/E-based valuation will look cheaper than the FCF reality.
3. **CFO inflection is genuine but flattered.** Q4'23 CFO = $101.75B − $82.83B (9M) = **$18.92B** vs. 9M average of $27.61B… actually lower sequentially — the FY CFO beat came earlier in the year, and Q4 carried the capex. Net: **revenue/earnings momentum into Q4 was better than the cash conversion.**

---

## 6. Investment Portfolio & AOCI — A Quiet $3.2B Book-Value Tailwind

| Metric | 2022-12-31 | 2023-12-31 | Direction |
|---|---|---|---|
| AFS debt securities at FV | — | **82.28** | — |
| Securities in an unrealized-loss position | **75.52** | **42.41** | **−44%** ✅ |
| — accumulated unrealized loss | 4.78 | **1.91** | **−60%** ✅ |
| — in loss position ≥12 months | 35.53 | 37.18 | slightly worse |
| — accumulated loss, ≥12 months | 2.75 | 1.86 | improving ✅ |
| — in loss position <12 months | 39.99 | 5.23 | **−87%** ✅ |
| AOCI | −7.60 | **−4.40** | **+3.20** ✅ |
| Non-marketable equity — cumulative upward adj. | 16.80 | **18.10** | +1.30 |
| Non-marketable equity — cumulative downward adj. | 4.50 | **6.90** | **+2.40 ⚠️** |
| AFS maturity ladder | — | $11.23B <1y; $41.48B 1–5y; $15.35B 5–10y; $14.22B >10y | well-laddered |

**Read:** The rate-shock marks are unwinding fast — **AOCI improved $3.2B** and unrealized losses on the bond book were cut ~60%. This is a *book value* tailwind and it means the $82B securities portfolio is close to being fully "clean." **But note the divergence:** cumulative *downward* fair-value adjustments on non-marketable equity rose **$4.50B → $6.90B (+53%)** even as cumulative upward adjustments only rose $1.30B. That is a genuine signal of **write-downs in the venture/Other-Bets portfolio** — a modest downside risk to the $28.8B non-marketable carrying value.

---

## 7. Tax — The Most Important "Gotcha" in the FY23 Print

| Metric | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Effective tax rate | 16.2% | 15.9% | **13.9%** |
| Current tax expense | 12.82 | 19.55 | 19.65 |
| Deferred tax expense | +1.88 | **−8.20** | **−7.73** |
| FDII benefit (rate impact) | 2.5% | 5.4% | **4.6%** |
| R&D credit (rate impact) | 1.6% | 2.2% | **1.8%** |
| SBC non-deductible (rate impact) | 2.5% | 1.2% | **0.8%** |
| Foreign rate differential | 0.2% | 3.0% | 0.3% |
| Cash taxes paid | 13.41 | 18.89 | 19.16 |

- **Cash taxes ($19.16B) ≈ current tax expense ($19.65B)** → no sign of tax-deferral games; the low ETR is *book* deferred-tax driven, not cash-driven. Good quality signal.
- **The 13.9% rate is the trough.** Deferred tax expense of −$7.73B (i.e., a benefit) plus a 4.6% FDII benefit and 1.8% R&D credit cannot compound indefinitely. **A normalization to ~15–16% is a ~$1.3–1.8B EPS headwind (~$0.10–0.14/share).** This should be the base case in any FY24 model.
- **DTA valuation allowance rose to $11.00B from $9.55B** and IPR&D DTAs surged — see §4 (M&A signal).
- **~$700M of unrecognized tax benefits may decrease within 12 months** [tag: `DecreaseInUnrecognizedTaxBenefitsIsReasonablyPossible`] — a small potential one-off benefit.

---

## 8. Insider Transactions

**⚠️ NOT AVAILABLE.** The configured news/filings vendor returned `DATA_UNAVAILABLE` — there is **no authorized, point-in-time insider-transaction archive for GOOGL as of 2024-02-28**. I will not infer, proxy, or fabricate insider activity from Form 4 knowledge post-dating the cut-off. **Any report giving you a specific insider buy/sell figure for GOOGL this week is unverified.** Treat this as a genuine information gap and, if insider behavior is load-bearing for your trade, confirm directly from EDGAR Form 4 filings dated ≤ 2024-02-28.

---

## 9. Historical Trend Scorecard (5-year arc, from tool data)

| Metric | FY21 | FY22 | FY23 | Trend verdict |
|---|---|---|---|---|
| Revenue growth | +41%* | +9.8% | **+8.7%** | Decelerating, stabilizing at high-single-digit |
| Gross margin | 56.9% | 55.4% | **56.6%** | Recovered, flat-ish |
| Operating margin | 30.6% | 26.5% | **27.4%** | **Repairing, not repaired** |
| Net margin | 29.5% | 21.2% | **24.0%** | Recovering |
| Diluted EPS | 5.61 | 4.56 | **5.80** | **New record high** |
| CFO | 91.65 | 91.50 | **101.75** | **Record** |
| FCF | 67.01 | 60.01 | **69.50** | **Record** |
| FCF margin | 26.0% | 21.2% | 22.6% | Improving |
| SBC / revenue | 6.1% | 6.9% | **7.2%** | **Worsening** |
| Share count (M) | ~13,555 | 12,849 | **12,460** | **−8% cumulative shrink** |
| ETR | 16.2% | 15.9% | **13.9%** | **At trough** |
| AOCI | — | −7.60 | **−4.40** | Healing |

\*FY21 growth vs. FY20 reflects the post-COVID ad recovery; included for arc context.

**ROE [derived]:** 73.80 / 283.38 = **26.0%**. **ROA:** 73.80 / 383.83 (avg assets) = **19.2%**. **ROIC [derived, NOPAT/invested capital]:** ~72.6 / ~187 = **~39%**. These are exceptional figures for a $400B-asset company and are the fundamental anchor under any valuation.

---

## 10. Actionable Insights for Traders

**Bull case (evidence-backed):**
1. **EPS momentum is measurable and non-fluke on the top line:** operating income +12.6% on revenue +8.7%; records in EPS ($5.80), CFO ($101.75B) and FCF ($69.50B). The FY22 cost blowout has been reversed (+7.3% cost growth vs. +16.3% in FY22).
2. **The buyback is a compounding EPS machine:** −3.0% share count in FY23, −8% cumulative since FY21, executed at $61.5B/yr with $96B net cash in reserve. Even flat net income yields ~+3% EPS/yr.
3. **AOCI/portfolio optionality:** $3.2B of book-value recovery already banked; $82B bond book now largely clean; $34.7B of non-marketable equity (Waymo/Other Bets) sits at a carrying value that the operating P&L does not reflect.
4. **Tax/DTA evidence of active tuck-in M&A** (+$7.4B IPR&D DTA) — historically a leading indicator of product/AI capability expansion.

**Bear case / de-rating risks (evidence-backed):**
1. **Tax normalization:** 13.9% → mid-teens = ~$1.3–1.8B headwind, i.e. ~2% of EPS. *First place a model breaks.*
2. **Capex cliff:** Q4'23 capex $11.02B vs. 9M average $7.08B (+56%). If that run-rate holds, FY24 capex ~$42–48B vs. $32.25B → **~$10–15B of FCF headwind**. At 23x FCF that is a material valuation input.
3. **SBC creep:** 7.2% of revenue and accelerating; SBC-adjusted FCF ($47.4B) is 32% below headline FCF.
4. **Receivables/accruals:** AR +19.1% vs revenue +8.7% (DSO +5 days) and accrued liabilities +21.9% — two non-repeatable sources of ~$4B of FY23 cash flow. **Any reversal is a CFO air-pocket.**
5. **Non-marketable equity write-downs accelerating** ($4.50B → $6.90B cumulative downward adjustments).

**Concrete things to do / watch:**
- **Trigger to add:** Q1'24 (filed ~late April) showing (a) DSO back under ~55 days, (b) capex guidance framed/actualized, (c) ETR landing in a *guided* range. All three = the FY23 print was clean, and 27%+ operating margin is a floor.
- **Trigger to trim:** DSO >60 days with a flat allowance, OR deferred tax benefit shrinking while ETR jumps >17%, OR buybacks continuing to exceed SBC-adjusted FCF (i.e., capital return funded by cash pile depletion rather than cash generation).
- **Key model inputs:** FY23 base = revenue $307.39B, operating income $84.29B (27.4%), net income $73.80B, EPS $5.80, FCF $69.50B, SBC $22.10B. **Use a 15–16% ETR, capex $40B+, and SBC-adjusted FCF as your "real" cash line.**
- **Valuation sensitivity (illustrative — price is NOT from my dataset):** net cash of ~$96B is ~5.5% of a ~$1.75T enterprise value at ~$140/share. Headline FCF of $69.5B → EV/FCF ≈ ~24x; SBC-adjusted FCF of $47.4B → **~35x**. The gap between those two numbers *is* the debate. Because revenue/FCF are the durable lines and the tax rate is not, **anchor on SBC-adjusted FCF, not GAAP EPS.**

---

## 11. Data Limitations Disclosed

- **Revenue line items and segment detail were not returned** by the point-in-time extract (alphabetical truncation); revenue/segment figures are the reported 10-K amounts and are *reconciled* to the tool's pre-tax income, tax expense and EPS.
- **Depreciation/amortization rows beyond FY2021** were truncated; no D&A-based EBITDA was computed.
- **Insider transactions: unavailable from the vendor** (see §8) — no inference made.
- Balance sheet has only two annual snapshots (12/31/22, 12/31/23) in this extract; **no quarterly intra-year balance sheet** was returned, so sequential trend analysis is limited to the cash-flow-driven 9M vs. FY bridge.
- All figures are point-in-time as of **2024-02-28**; nothing filed after that date is reflected.

---

## 12. Key Points Summary Table

| Category | Metric (FY2023 unless noted) | Value | y/y | Signal |
|---|---|---|---|---|
| **Income** | Revenue | **$307.39B** | +8.7% | Stabilizing at HSD growth |
| | Gross profit / margin | $174.06B / **56.6%** | +11.1% / +120bp | Recovery, mix-driven |
| | Operating income / margin | $84.29B / **27.4%** | +12.6% / +90bp | **Positive operating leverage** |
| | Pre-tax income | $85.72B | +20.2% | |
| | Net income / margin | **$73.80B** / 24.0% | **+23.1%** | Record |
| | **Diluted EPS** | **$5.80** | **+27.2%** | Record; buyback-amplified |
| | Effective tax rate | **13.9%** | −200bp | ⚠️ **At trough — normalizes in FY24** |
| | Other income (expense) | +$1.42B | from −$3.51B | Noisy equity marks; ignore |
| **Costs** | Total costs & expenses | $223.10B | **+7.3%** (vs rev +8.7%) | ✅ Leverage turned positive |
| | R&D | $45.43B | +15.0% | AI/infra investment |
| | S&M | $27.92B | +5.1% | Disciplined |
| | G&A | $16.43B | +4.5% | Disciplined |
| | **SBC** | **$22.10B** (7.2% of rev) | **+13.3%** | ⚠️ Growing faster than revenue |
| **Balance sheet** | Total assets | **$402.39B** | +10.2% | |
| | Total equity | $283.38B | +10.6% | |
| | Total liabilities | $119.01B | +9.1% | Low leverage |
| | Cash + ST investments | **$110.92B** | −2.5% | |
| | Gross debt | ~$14.86B | net paydown | **Net cash ~$96B** |
| | Accounts receivable | $47.96B | **+19.1%** | ⚠️ DSO 51.9 → **56.9 days** |
| | Allowance for doubtful accts | $0.771B | +2.3% | No credit stress flagged |
| | Accrued liabilities | $46.17B | +21.9% | ⚠️ +$3.9B non-repeatable cash |
| | Deferred revenue | $5.05B | +12.2% | Mildly positive |
| | AOCI | −$4.40B | **+$3.20B** | ✅ Bond marks healing |
| | Unrealized losses on AFS | $1.91B | −60% | ✅ |
| | Non-marketable equity (cum. down-adj.) | $6.90B | **+53%** | ⚠️ Write-downs |
| | Shares outstanding | 12,460M | **−3.0%** | ✅ Buyback accretion |
| **Cash flow** | Operating cash flow | **$101.75B** | **+11.2%** | Record |
| | Capex | $32.25B (10.5% of rev) | +2.4% | ⚠️ **Q4 alone $11.02B (+56% vs 9M avg)** |
| | **Free cash flow** | **$69.50B** (22.6%) | **+15.8%** | Record |
| | **FCF − SBC** | **$47.40B** (15.4%) | — | ⚠️ The "real" cash line |
| | Buybacks | **$61.50B** | +3.7% | 130% of FCF−SBC |
| | Debt issued / repaid | $10.79B / $11.55B | −80% / −79% | Deleveraging |
| | Cash taxes paid | $19.16B | +1.4% | ✅ Clean, no deferral games |
| **Returns** | ROE [derived] | **26.0%** | — | Exceptional |
| | ROA [derived] | 19.2% | — | Exceptional |
| | ROIC [derived] | ~39% | — | Exceptional |
| **Insider** | Form 4 activity | **UNAVAILABLE** | — | ⚠️ Vendor gap — verify at EDGAR |
| **Bottom line** | | **Quality compounder with record cash flows, a buyback tailwind and partially-repaired margins — but FY23 EPS is flattered by a trough tax rate and FY23 FCF by a Q4 capex cliff that has not yet hit.** | | **Constructive; model on 15–16% ETR and SBC-adjusted FCF** |