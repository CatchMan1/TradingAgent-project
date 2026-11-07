# GOOGL — Fundamental Research Report
**Company:** Alphabet Inc. (`GOOGL`) · **Analysis date:** 2026-07-28 · **Most recent filing in window:** 10-Q filed 2026-07-23 for the quarter ended 2026-06-30 (Q2 FY2026); prior 10-K filed 2026-02-05 for FY2025

---

## 1. Data basis and important caveats (read first)

| Item | Status |
|---|---|
| Source | Point-in-time SEC XBRL facts (acceptance-timestamp filtered ≤ 2026-07-28) |
| Periods available | Q1–Q2 FY2026, Q1–Q2 FY2025, plus FY2023–FY2025 cash-flow and debt-maturity tags |
| **Revenue** | Not present as a discrete tag in the retrieved window — **derived** as `OperatingIncomeLoss + CostsAndExpenses` (Alphabet's standard P&L has no other operating line above operating income). Treated as exact to within rounding. |
| Tags past "F" (Goodwill, PP&E, Retained Earnings, Stockholders' Equity, R&D, Revenues, Segment data) | Truncated by the data extract — **not available**. Ratios requiring total equity, book value, PP&E or segment mix **cannot be computed** and are flagged as such. |
| Share price / market cap | Not available in this fact set → no P/E, P/B, EV/EBITDA multiple can be computed. |
| **Insider transactions** | `DATA_UNAVAILABLE` — the vendor has no authorized point-in-time insider archive for GOOGL. **No insider buying/selling is asserted or inferred in this report.** |

All figures below are USD millions unless stated.

---

## 2. Company profile (identity confirmed: Alphabet Inc.)

Alphabet is the parent of Google, organized around three reporting pillars (segment P&L was not in the retrieved fact window, so mix is described qualitatively):

- **Google Services** — Search & other (incl. AI Overviews/AI Mode monetization), YouTube ads, Google Network, subscriptions/platforms/devices (Google One, YouTube Premium, Play, Pixel), plus Chrome/Android/Maps.
- **Google Cloud** — Google Cloud Platform (compute, storage, data/analytics, AI/TPU capacity rental) and Google Workspace; the fastest-growing and most capex-intensive pillar.
- **Other Bets** — Waymo, Verily, Isomorphic Labs, Wing, and other early-stage ventures.

Strategic framing evident from the financials: the company is in a **maximum-investment AI cycle** — capex, depreciation, headcount-related SBC, and third-party AI/cloud infrastructure commitments are all rising sharply, funded increasingly with **external capital** rather than internal free cash flow for the first time in its history as a public company.

---

## 3. Income statement: strong operating momentum, but earnings are dominated by investment marks

### 3.1 Q2 FY2026 and first-half results

| USD M | Q2 2026 | Q2 2025 | Δ | H1 2026 | H1 2025 | Δ |
|---|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | 119,796 | 96,428 | **+24.2%** | 229,692 | 186,662 | **+23.0%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| **Gross profit** | 73,853 | 57,389 | +28.7% | 142,478 | 111,262 | +28.1% |
| Gross margin | **61.7%** | 59.5% | +220 bp | **62.0%** | 59.6% | +240 bp |
| SBC (total) | 8,000 | 6,000 | +33.3% | 15,200 | 11,500 | +32.2% |
| G&A | 6,461 | 5,209 | +24.0% | 10,752 | 8,748 | +22.9% |
| Amortization of intangibles | 367 | 124 | +196% | 545 | 246 | +122% |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 149,226 | 124,785 | +19.6% |
| **Operating income** | 40,770 | 31,271 | **+30.4%** | 80,466 | 61,877 | **+30.0%** |
| Operating margin | **34.0%** | 32.4% | +160 bp | **35.0%** | 33.2% | +180 bp |
| **Non-operating income** | **97,983** | 2,662 | n.m. | **135,699** | 13,845 | +880% |
| Pretax income | 138,753 | 33,933 | +309% | 216,165 | 75,722 | +185% |
| Tax expense | 26,560 | 5,737 | +363% | 41,394 | 12,986 | +219% |
| Effective tax rate | 19.1% | 16.9% | +220 bp | 19.1% | 17.1% | +200 bp |
| **Net income** | **112,193** | 28,196 | +298% | **174,771** | 62,736 | +179% |
| Net income to common | 112,107 | 28,196 | — | 174,685 | 62,736 | — |
| **Diluted EPS** | **9.11** | 2.31 | +294% | **14.24** | 5.12 | +178% |
| Basic EPS | 9.23 | 2.33 | — | 14.41 | 5.16 | — |
| Diluted shares (implied) | ~12,306 | ~12,206 | +0.8% | ~12,266 | ~12,253 | +0.1% |

**Sequential read-through (Q1 → Q2 2026):** revenue 109,896 → 119,796 (**+9.0% q/q**); operating income 39,696 → 40,770 (+2.7%); operating margin 36.1% → 34.0% (−210 bp q/q — cost growth front-running revenue, consistent with depreciation from the capex ramp).

### 3.2 The single most important analytical point: earnings quality

- **62.8% of H1 2026 pretax income ($135,699M of $216,165M) came from non-operating items**, essentially all equity-securities gains:
  - `EquitySecuritiesFvNiGainLoss` H1 2026 = **$135,946M** (Q2 alone $99,031M; Q1 $36,915M)
  - `DebtAndEquitySecuritiesGainLoss` = $135,803M vs $11,411M in H1 2025
  - `EquitySecuritiesFvNiUnrealizedGainLoss` = $21,531M — i.e., most of the gain is **realized or remeasurement-driven**, not just Q2 mark-to-market
  - Private-stake revaluation confirmed on the balance sheet: cumulative **upward** adjustments on non-marketable equity securities rose from **$44,485M → $85,732M** (+$41.2B in six months)
- **Core, operating EPS**: applying the 19.1% tax rate to operating income gives **~$5.31/share in H1 2026** (Q2 ~$2.69) vs **~$4.19** in H1 2025 (**+27% YoY**). Headline $14.24 is **~2.7x** the operating figure.
- Tax/balance-sheet corroboration that the gains are real but **deferred-tax-heavy**: deferred tax liabilities jumped **$919M → $22,819M** (+$21.9B), deferred taxes in the cash-flow statement swung **−$1,596M → +$27,538M**, and the ETR rose 200 bp.
- **Trading implication:** any P/E computed on trailing headline EPS will look extraordinarily cheap and is **not comparable** to history. Valuation work on GOOGL right now must be done on operating income / operating EPS / EBITDA, with investment gains treated as a separate, non-recurring, mark-to-market asset bucket that can reverse.

### 3.3 What the operating numbers say

- Revenue +23–24% YoY at ~$230B half-year scale is a **step-up in organic growth**, not a normalization.
- **Gross margin expanded 240 bp** despite $13,586M of depreciation (+43% YoY) flowing largely through cost of revenue — evidence that AI/cloud revenue is presently outrunning the cost of serving it (i.e., positive incremental AI unit economics so far).
- **Operating leverage is intact**: costs +19.6% vs revenue +23.0% → operating margin +180 bp to 35.0%, operating income +30%.
- **Watch item — SBC**: $15.2B in H1 (+32%), which is 6.6% of revenue (vs 6.2%) and 18.9% of operating income. SBC growth is accelerating faster than headcount-driven cost lines and is a real, recurring dilution cost.
- **Deferred revenue** rose to $10,100M from $8,600M (+17.4%), and $4.9B of H1 revenue came from the opening contract-liability balance — a healthy forward-demand indicator (consistent with Cloud backlog growth).
- Receivables discipline: AR +10.0% ($62,886M → $69,175M) against +23% revenue → DSO ≈ **52 days**, no channel-stuffing signal.

---

## 4. Balance sheet: a $327B six-month expansion, largely externally funded

| USD M | 2026-06-30 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| **Cash + short-term investments** | **242,474** | **126,843** | **+91.2%** |
| AFS debt securities (fair value) | 99,500 | n/a | — |
| Accounts receivable, net | 69,175 | 62,886 | +10.0% |
| **Total current assets** | **343,524** | **206,038** | **+66.7%** |
| Non-marketable equity securities (no RDFV) | 124,259 | 64,094 | +93.9% |
| Finite-lived intangibles, gross | 10,585 | 2,467 | **+329%** |
| **Total assets** | **921,983** | **595,281** | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| Accrued income taxes (current + noncurrent) | 16,539 | 10,054 | +64.5% |
| Deferred tax liabilities | 22,819 | 919 | +2,383% |
| **Debt (carrying)** | **101,085** | **49,085** | **+106.0%** |
| Finance lease liabilities | 2,590 | 2,500 | +3.6% |
| Operating lease liabilities | 18,037 | 15,954 | +13.1% |
| **Convertible preferred stock** | **18,023** | 0 | new |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| AOCI | (2,285) | (1,916) | −369 |
| Loss contingency accruals (current) | 17,356 | 15,594 | +11.3% |
| Deferred revenue | 10,100 | 8,600 | +17.4% |
| Shares outstanding (M) | 12,230 | 12,088 | +1.17% |

**Key reads:**

1. **Net cash remains strongly positive**: $242,474M liquidity vs $101,085M debt + $2,590M finance leases = **~$138.8B net cash** (vs ~$75.3B at year-end). Leverage is not a solvency issue — annualized interest of ~$3.6B against $80B+ of H1 operating income implies **~44x interest coverage** and ~1.2x debt/EBIT. The jump in debt ($49B → $101B) is a deliberate, cheap financing decision (~3.5% average implied cost), not distress.
2. **A brand-new $18.0B convertible preferred** was issued on **2026-06-05** (proceeds $19,063M) and $86M of preferred dividends were paid in Q2. This is an unusual instrument for GOOGL — it sits senior to common, adds a fixed charge, and creates potential future dilution. **The cost of this capital is materially above the ~3.5% debt cost** — worth digging into the 10-Q exhibit for the coupon/conversion terms (not in the retrieved facts).
3. **Evidence of M&A**: gross finite-lived intangibles tripled ($2.467B → $10.585B) with only $545M of H1 amortization → roughly **$8B of newly acquired intangibles**. Combined with total asset growth well beyond cash-attributable items, this points to an acquisition (goodwill tags were truncated; **confirm in the 10-Q/8-K**). Amortization guidance is now $1,304M next-twelve-months and ~$1.05–1.15B/yr for the following three years.
4. **Deferred tax liability of $22.8B is a future cash-tax overhang** on unrealized appreciation of the $124B private-investment book. It does not affect FCF today but caps how much of the investment gain is truly "available."
5. **AFS securities pressure**: $53.2B of the $99.5B debt portfolio is in an unrealized-loss position (accumulated loss only $416M) — duration/rate sensitivity, not credit risk. Investment portfolio remains overwhelmingly high-quality.
6. **Legal/regulatory accruals rose to $17,356M** (+$1.8B) — meaningful, and a reminder that regulatory remedies are an ongoing cash cost.
7. **Dilution**: +142M shares (+1.17%) in six months, plus $18B of convertible preferred. Buyback was **zero**, so net share count is now rising for the first time in years.

---

## 5. Cash flow: the story of the quarter is a collapsed free cash flow

| USD M | H1 2026 | H1 2025 | Δ |
|---|---:|---:|---:|
| **Operating cash flow** | **84,859** | 63,897 | **+32.8%** |
| Capex (cash, PP&E) | **80,598** | 39,643 | **+103.3%** |
| **Free cash flow (CFO − capex)** | **4,261** | **24,254** | **−82.4%** |
| Capex / revenue | **35.1%** | 21.2% | +1,390 bp |
| Capex incurred but unpaid (period-end) | 29,113 | 10,635 | +$18.5B |
| Depreciation | 13,586 | 9,485 | +43.2% |
| Stock-based comp | 15,200 | 11,500 | +32.2% |
| Purchases of other (private) investments | 22,051 | 2,312 | +854% |
| Purchases of marketable securities | 76,480 | 39,870 | +91.8% |
| Sales/maturities of marketable securities | 66,696 | 40,930 | +62.9% |
| **Investing cash flow** | **(145,822)** | (40,738) | −258% |
| Debt issuance | 56,226 | 31,378 | +79.2% |
| Debt repayment | (5,253) | (18,397) | −71.4% |
| **Common stock issued** | **30,499** | 0 | new |
| **Convertible preferred issued** | **19,063** | 0 | new |
| Minority-interest proceeds (subsidiary raises) | 3,758 | 400 | n.m. |
| **Share repurchases** | **0** | **(28,306)** | **−100%** |
| Dividends paid | (5,231) | (4,977) | +5.1% |
| **Financing cash flow** | **+86,320** | (26,033) | n.m. |
| Net change in cash | **+25,203** | (2,430) | n.m. |

**Derived quarterly cash-flow profile:**

| USD M | Q2 2026 | Q1 2026 | Q2 2025 |
|---|---:|---:|---:|
| CFO | 39,069 | 45,790 | 27,747 |
| Capex | 44,924 | 35,674 | 22,446 |
| **FCF** | **(5,855)** | **10,116** | 5,301 |
| Investing CF | (82,433) | (63,389) | n.m. |
| Financing CF | +61,243 | +25,077 | n.m. |

**Interpretation:**

- **Q2 2026 was the first quarter in Alphabet's history with negative free cash flow** on this dataset (CFO $39.1B vs capex $44.9B = **−$5.9B**). Including the $18.5B build in accrued-but-unpaid capex, H1 capex *incurred* is closer to **~$99B** — i.e., the forward run-rate commitment is even higher than the cash figure.
- The company plugged the gap with **$109.5B of gross external capital in six months** (debt $56.2B + common $30.5B + convertible preferred $19.1B + subsidiary minority $3.8B) and simultaneously **halted buybacks entirely** (0 vs $28.3B in H1 2025). This is a textbook "growth-over-return-of-capital" pivot.
- Operating cash flow itself is **excellent** (+32.8%, growing faster than revenue thanks to SBC add-backs of $15.2B and a $27.5B deferred-tax add-back). The FCF problem is purely a **capex-intensity** problem, not a demand or collection problem.
- **Price marker (inference, treat cautiously):** 142M new shares for $30,499M of proceeds implies a **blended ~$215/share**, though SBC-related issuance in the same bucket means the actual offering price was likely higher. Directionally: equity was marketed in the ~$215+ area during H1 2026.
- Dividend: $0.22/quarter in Q2 2026 vs $0.21 (+4.8%); H1 declared $0.43 vs $0.41. Modest, and now competing with a preferred dividend and a heavy capex program. Payout remains low — no dividend-cut risk.

---

## 6. Insider transactions

**Not available.** The vendor explicitly returned `DATA_UNAVAILABLE`: there is no authorized, point-in-time insider-transactions archive for GOOGL as of 2026-07-28. I will not infer, estimate, or fabricate insider activity. Anyone acting on this report should independently check Form 4 filings for the June–July 2026 window (particularly around the 2026-06-05 convertible preferred issuance and any concurrent secondary), and should note that zero buybacks plus a large equity issuance is a management signal worth weighing against insider behavior.

---

## 7. Risk register (ranked by likely impact on the equity)

| # | Risk | Evidence / magnitude | What would confirm or refute it |
|---|---|---|---|
| 1 | **AI capex digestion / FCF disappointment** | Capex $80.6B in H1, 35.1% of revenue, +103% YoY; Q2 FCF −$5.9B; capex-incurred-unpaid $29.1B | Q3 capex guide; Cloud backlog disclosure; whether depreciation growth outruns gross profit |
| 2 | **Earnings-quality reversal** | $135.7B H1 non-operating gains; $124.3B private-stake book with $85.7B cumulative upward marks; $22.8B DTL | Mark-to-market in a down private-market tape; any impairment/negative remeasurement quarter would create a large headline EPS miss |
| 3 | **Dilution / capital-structure shift** | +1.17% shares, $18.0B convertible preferred at likely mid-single-digit economics, buybacks at zero | Terms of the June 5 preferred; resumption (or not) of buybacks in Q3 |
| 4 | **Rising cost structure** | SBC +32%, depreciation +43%, interest expense $1,811M vs $295M (+514%) | Operating margin trajectory (Q2 already −210 bp q/q) |
| 5 | **Regulatory / legal** | Loss contingency accruals $17.4B (+$1.8B in 6 months) | 10-Q legal proceedings update; remedies in US/EU antitrust matters |
| 6 | **Rate/duration risk on investment book** | $53.2B AFS in unrealized-loss position (accumulated loss $416M) | Sensitivity in 10-Q Item 3 |

---

## 8. Actionable conclusions for traders

**Bull case (operating fundamentals are genuinely accelerating):**
1. Revenue growth re-accelerated to **+23–24% YoY** at ~$460B annualized run-rate, with **gross margin +240 bp** and **operating margin +180 bp to 35.0%**. Operating income grew **+30%**. This is the highest-quality part of the print and it is not a one-quarter artifact (Q1 2026 operating margin was 36.1%).
2. Q2 operating EPS ~$2.69 (+27% YoY) and H1 ~$5.31 — even on a **core, ex-investment-gains** basis the business is compounding at a high-20s rate.
3. Balance sheet strength is unimpaired: **~$139B net cash**, 44x interest coverage, $242B of liquidity. The debt raise is opportunistic.
4. Forward demand signals positive: deferred revenue +17.4%, $4.9B recognized from opening contract liabilities, DSO stable at ~52 days.

**Bear case (don't buy the headline EPS):**
1. **~63% of H1 net income is non-operating investment marks.** Headline EPS of $14.24 (and any trailing-twelve-month multiple derived from it) materially overstates sustainable earnings power. A private-market markdown quarter would produce a violent optical earnings decline with no change in the operating business.
2. **Free cash flow has effectively gone to zero** (H1 $4.3B, Q2 −$5.9B) and the company is now **funding itself externally** — $109.5B of gross capital raised, buybacks cut to zero, plus a new preferred layer. FCF-based valuation models need a materially higher capex assumption for FY2026–27.
3. **Dilution has turned positive** for the first time in years (+1.17% shares plus a convertible preferred), reducing the per-share compounding that historically supported the multiple.

**Concrete positioning framework:**
- **Valuation:** Value GOOGL on **operating income / operating EPS / EBITDA**, explicitly excluding the equity-securities line, and then add a separately-marked (and possibly discounted, say 20–30% for tax and illiquidity) value for the $124B private-stake book. Do **not** use headline P/E — it is distorted by ~2.7x.
- **Catalyst to watch (next 1–2 quarters):** whether capex growth decelerates (capex/revenue below 30%) while revenue growth holds >20%. If both happen, FCF inflects hard upward and the stock re-rates on FCF — the highest-conviction long setup. If capex keeps doubling and growth decelerates below 20%, the FCF-compression narrative dominates.
- **Near-term risk events:** Q3 FY2026 print (expect late Oct 2026) for capex guide and Cloud margin; any 8-K/10-Q detail on the **June 5 convertible preferred terms** and the **~$8B intangible acquisition**; quarterly mark-to-market of the private book.
- **Hedge idea:** the investment-gain distortion creates an asymmetry — long-dated call spreads capture the operating compounding, while the risk of a mark-to-market EPS shock argues against outsized short-dated call buying into the print.
- **Information gap to close before sizing:** insider Form 4 activity (vendor unavailable) and segment-level margins (not in this fact window).

---

## 9. Key facts summary table

| Category | Metric | Value / Observation | Signal |
|---|---|---|---|
| **Filing** | Latest 10-Q | Filed 2026-07-23, period end 2026-06-30 | Fresh, within window |
| **Growth** | Q2 revenue (derived) | $119,796M, **+24.2% YoY**; Q1 $109,896M (+9.0% q/q) | Strongly bullish |
| **Growth** | H1 revenue | $229,692M, +23.0% YoY | Strongly bullish |
| **Margins** | Gross margin | 62.0% H1 (+240 bp); Q2 61.7% | Bullish (AI unit economics working) |
| **Margins** | Operating margin | 35.0% H1 (+180 bp); Q2 34.0% (−210 bp q/q) | Bullish but decelerating q/q |
| **Profit** | Operating income | H1 $80,466M, **+30.0%**; Q2 $40,770M, +30.4% | Bullish |
| **Profit** | Net income / diluted EPS | H1 $174,771M / **$14.24**; Q2 $112,193M / $9.11 | **Distorted — do not annualize** |
| **Earnings quality** | Non-operating income | H1 **$135,699M** (62.8% of pretax) — equity-securities gains | **Bearish on headline quality** |
| **Earnings quality** | Core operating EPS (est.) | ~$5.31 H1 (+27% YoY); ~$2.69 Q2 | Bullish, and the right comparison base |
| **Tax** | Effective rate | 19.1% vs 17.1%; deferred tax liability $919M → **$22,819M** | Future cash-tax overhang |
| **Balance sheet** | Total assets | $921,983M vs $595,281M (+54.9% in 6 months) | Expansion / M&A |
| **Balance sheet** | Cash + ST investments | **$242,474M** (+91%) | Fortress |
| **Balance sheet** | Total debt | $101,085M (+106%) + $2,590M finance leases | Levering up deliberately |
| **Balance sheet** | Net cash | **~+$138,799M**; interest coverage ~44x | No solvency risk |
| **Balance sheet** | Non-marketable equity securities | $124,259M (+94%); cumulative up-marks $85,732M | Hidden asset, but volatile earnings |
| **Balance sheet** | Convertible preferred | **$18,023M new** (issued 2026-06-05); $86M dividends paid in Q2 | New senior claim + dilution risk |
| **Balance sheet** | Shares outstanding | 12,230M vs 12,088M (**+1.17%**) | Dilution has turned positive |
| **Cash flow** | Operating cash flow | H1 $84,859M, **+32.8%** | Bullish |
| **Cash flow** | Capex | H1 $80,598M, **+103%**; 35.1% of revenue; $29,113M incurred-unpaid | **Key bear vector** |
| **Cash flow** | Free cash flow | H1 $4,261M (−82%); **Q2 −$5,855M (negative)** | **Key bear vector** |
| **Capital allocation** | Buybacks | **$0** vs $28,306M in H1 2025 | Regime change |
| **Capital allocation** | Capital raised H1 | Debt $56,226 + common $30,499 + pref $19,063 + minority $3,758 = **~$109.5B** | Regime change |
| **Capital allocation** | Dividend | $0.22/qtr (vs $0.21); H1 cash $5,231M | Stable, low |
| **Capital allocation** | Private-investment purchases | $22,051M vs $2,312M (+854%) | Aggressive AI ecosystem investing |
| **Forward demand** | Deferred revenue | $10,100M vs $8,600M (+17.4%); $4.9B recognized from opening balance | Bullish |
| **Costs** | SBC | $15,200M (+32.2%); 6.6% of revenue | Watch |
| **Costs** | Depreciation | $13,586M (+43.2%); NTM intangible amortization $1,304M | Rising drag |
| **Costs** | Interest expense | $1,811M vs $295M (+514%) | Rising but manageable |
| **Legal** | Loss contingency accruals | $17,356M (+$1,762M) | Watch |
| **Liquidity risk** | AFS unrealized-loss position | $53,239M notional, $416M accumulated loss | Rate risk, not credit |
| **Insider** | Transactions | **DATA UNAVAILABLE** — no archive authorized | Cannot assess |
| **Implied price marker** | Equity issuance | $30,499M / +142M shares ≈ **~$215 blended** (inference only) | Rough trading-range anchor |

**Bottom line:** GOOGL's *operating* business is performing better than at any point in its history on this dataset — 23–24% revenue growth, 35% operating margins, +30% operating income. The *reported* numbers, however, are dominated by $135.7B of non-operating investment gains, and the *cash* story has inverted: Q2 2026 free cash flow was negative, capex is running at 35% of revenue, buybacks are at zero, and the company raised ~$110B externally including a new $18B convertible preferred. Trade the operating trend; do not underwrite the headline EPS. The decisive variable for the next 6–12 months is whether capex intensity peaks while revenue growth holds above 20% — that combination would turn the current FCF squeeze into a powerful FCF inflection.