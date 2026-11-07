# GOOGL — Alphabet Inc. | Fundamental Deep-Dive
**Data as of:** 2026-08-04 | **Freshest filing:** Q2 FY2026 Form 10-Q, accepted 2026-07-23 01:15 UTC (accn 0001652044-26-000071) | Prior 10-K filed 2026-02-05

---

## 1. Executive Summary — the one thing that changed this quarter

Alphabet's Q2 FY2026 print is **two companies in one income statement**:

1. **An operating business that is accelerating** — revenue grew ~24% y/y, operating margin expanded ~160bp y/y to **34.0%**, and operating income rose **30.4% y/y**. Cash flow from operations rose **32.8%**.
2. **A balance sheet that has been radically re-levered and re-deployed into AI infrastructure and private equity stakes** — H1 capex of **$80.6B** (35.1% of revenue), **$109.5B of gross new capital raised in six months** (debt + common stock + convertible preferred + minority interests), **zero share repurchases** (vs. $28.3B in H1 2025), and **$99.0B of pre-tax mark-to-market equity gains in Q2 alone** that produced reported diluted EPS of $9.11 versus a "clean" operating EPS of roughly **$2.7**.

**Reported EPS is not usable as a run-rate.** Roughly **71% of Q2 pre-tax income** came from non-cash equity revaluations. Traders should underwrite the business on **operating income, operating margin, and free cash flow** — and on those three, the picture is: strong and improving top line, expanding margins, but **free cash flow effectively collapsed to ~zero** (and went negative in Q2).

---

## 2. Company Profile & Segment Context

Alphabet Inc. (GOOGL) is the parent of Google, organized around **Google Services** (Search, YouTube, Android, Chrome, Maps, Play, devices, subscriptions), **Google Cloud** (infrastructure, Workspace, and enterprise AI/TPU capacity), and **Other Bets** (Waymo, Verily, Wing, etc.), plus a large **investment portfolio** (Alphabet's "Other" line, non-marketable equity securities, and a marketable securities book).

*Note on segment detail:* the vendor's point-in-time SEC fact set returned for this analysis contains consolidated tags only — **no segment revenue table, no R&D line, no goodwill, no retained earnings**. Segment-level commentary below is therefore inferred from consolidated line items and flagged as such. See §9 Data Gaps.

---

## 3. Income Statement — Q2 FY2026 vs Q2 FY2025 (USD millions, derived from SEC tags)

| Line (derived) | Q2 FY2026 | % of rev | Q2 FY2025 | % of rev | y/y |
|---|---:|---:|---:|---:|---:|
| Revenue (= CostsAndExpenses + OperatingIncomeLoss) | **119,796** | 100.0% | 96,428 | 100.0% | **+24.2%** |
| Cost of revenue | 45,943 | 38.4% | 39,039 | 40.5% | +17.7% |
| Gross profit | 73,853 | 61.6% | 57,389 | 59.5% | +28.7% |
| R&D + S&M (residual) | 26,622 | 22.2% | 20,716 | 21.5% | +28.5% |
| General & administrative | 6,461 | 5.4% | 5,402 | 5.6% | +19.6% |
| **Operating income** | **40,770** | **34.0%** | 31,271 | 32.4% | **+30.4%** |
| Other income (expense), net | 97,983 | n/m | 2,662 | n/m | +3,581% |
| Pre-tax income | 138,753 | n/m | 33,933 | n/m | +309% |
| Income tax | 26,560 | 19.1% ETR | 5,737 | 16.9% ETR | +363% |
| **Net income** | **112,193** | n/m | 28,196 | n/m | +298% |
| Net income to common | 112,107 | | 28,196 | | |
| **Diluted EPS** | **$9.11** | | $2.31 | | +294% |
| Basic EPS | $9.23 | | $2.33 | | |
| SBC (allocated) | 8,000 | 6.7% | 6,000 | 6.2% | +33% |
| Depreciation | (H1: 13,586) | | (H1: 9,485) | | H1 +43% |

### 3a. The composition of "Other income" — critical for trading

| Component (Q2 FY2026) | USD m |
|---|---:|
| Net gain on equity securities (FV-NI, incl. private-stake upward revaluations) | **99,031** |
| Interest income | 1,430 |
| Interest expense | (1,278) |
| FX/other | (160) |
| **Total non-operating income** | **97,983** |

**Clean (ex-investment-gain) earnings reconstruction:**

| | Q2 FY2026 | Q2 FY2025 | y/y |
|---|---:|---:|---:|
| Operating income | 40,770 | 31,271 | +30.4% |
| + net interest & FX | (8) | 720 | n/m |
| = Pre-tax, ex-equity gains | ~40,762 | ~31,991 | +27.4% |
| × (1 − ETR) | ~32,976 | ~26,584 | +24.0% |
| **Clean diluted EPS (est., ~12.27B dil. sh.)** | **~$2.69** | **~$2.17** | **~+24%** |

**Read-through:** clean EPS growth (~+24%) ≈ revenue growth (~+24%), with a modest positive operating-leverage kicker offset by higher interest expense and SBC. This is a high-quality, non-AI-hype operating result — but it is **a ~$2.7 quarterly earnings power story, not a $9-plus story.**

### 3b. H1 FY2026 vs H1 FY2025

| | H1 FY2026 | H1 FY2025 | y/y |
|---|---:|---:|---:|
| Revenue | **229,692** | 186,662 | **+23.1%** |
| Operating income | **80,466** | 61,877 | **+30.0%** |
| Operating margin | **35.0%** | 33.1% | +190bp |
| Non-operating income | 135,699 | 13,845 | +880% |
| Net income | **174,771** | 62,736 | +178% |
| Diluted EPS | **$14.24** | $5.12 | +178% |
| Equity FV-NI gains (pre-tax) | 135,946 | 11,044 | +1,131% |

Q1 FY2026 standalone: revenue ~**109,896**, operating income ~**39,696** (36.1% margin), net income ~**62,578**, equity gains ~36,915. So **Q2 operating margin (34.0%) slipped ~210bp sequentially from Q1 (36.1%)** — the first tangible sign of depreciation/AI-cost drag. Watch this.

---

## 4. Cash Flow — where the real story is

| H1 (USD m) | FY2026 | FY2025 | y/y |
|---|---:|---:|---:|
| Cash from operations | **84,859** | 63,897 | +32.8% |
| Purchases of PP&E (capex) | **(80,598)** | (39,643) | **+103%** |
| **Free cash flow (derived)** | **4,261** | 24,254 | **−82%** |
| FCF margin | **1.9%** | 13.0% | −1,110bp |
| Capex / revenue | **35.1%** | 21.2% | +1,390bp |
| Purchases of other (equity) investments | (22,051) | (2,312) | +854% |
| Purchases of marketable securities, net of maturities | (9,784) | +1,060 | n/m |
| **Investing cash flow** | **(145,822)** | (40,738) | +258% |
| Debt issued (net) | **+56,226** | +31,378 | +79% |
| Common stock issued | **+30,499** | 0 | n/m |
| Convertible preferred issued (2026-06-05) | **+19,063** | 0 | n/m |
| Minority interest proceeds | +3,758 | 400 | +840% |
| Debt repayments | (5,253) | (18,397) | −71% |
| Dividends paid | (5,231) | (4,977) | +5.1% |
| **Share repurchases** | **0** | (28,306) | **−100%** |
| **Financing cash flow** | **+86,320** | (26,033) | n/m |

### 4a. Quarterly FCF decomposition — the alarm bell

| | Q1 FY2026 | Q2 FY2026 |
|---|---:|---:|
| CFO | 45,790 | 39,069 |
| Capex | (35,674) | **(44,924)** |
| **FCF** | **+10,116** | **(5,855)** |

**Q2 FY2026 appears to be the first quarter of negative free cash flow in Alphabet's modern history.** Two forward indicators say Q3 gets worse before it gets better:

- **Capex incurred but not yet paid: $29,113M at 6/30/26**, up from $10,635M a year earlier (+174%) and $15,090M at 12/31/25 → a large accrued capex liability that will convert to cash outflow in Q3.
- Capex trend: Q1 $35.7B → Q2 $44.9B (+25.9% q/q). Annualized run-rate is now **>$160B**, versus ~$80B implied for H1 2025 annualized.

**Actionable:** model FY2026 FCF in the low-single-digit billions at best, possibly negative in H2 if capex keeps compounding. Any valuation framework anchored on historical FCF multiples is broken for 2026–2027. The correct frame is capex-normalized earnings power post-2028, or EV/EBIT on operating income.

---

## 5. Balance Sheet — a fortress that is being spent, and levered for the first time

| (USD m) | 2026-06-30 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 55,911 | 30,708 | +82% |
| **Cash + short-term investments** | **242,474** | 126,843 | **+91%** |
| Available-for-sale debt securities | 99,500 | n/a | — |
| Accounts receivable, net | 69,175 | 62,886 | +10.0% |
| Current assets | 343,524 | 206,038 | +66.7% |
| **Total assets** | **921,983** | 595,281 | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| **Total debt (carrying, face)** | **101,085** | 49,085 | **+106%** |
| Finance lease liabilities | 2,590 | 2,500 | +3.6% |
| Operating lease liabilities | 18,037 | 15,954 | +13.1% |
| Deferred income tax liabilities | **22,819** | 919 | +2,383% |
| Non-marketable equity securities (no ready FV) | **124,259** | 64,094 | **+94%** |
| — cumulative upward adjustments | 85,732 | 44,485 | +93% |
| — cumulative downward adjustments | (9,115) | (8,820) | +3.3% |
| Convertible preferred stock | **18,023** | 0 | new |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| AOCI | (2,285) | (1,916) | — |
| Shares outstanding (m) | **12,230** | 12,088 | +1.17% |
| Legal/contingency accrual (current) | **17,356** | 15,594 | +11.3% |

### Key balance-sheet reads

- **Still net-cash, but the direction is unambiguous.** Gross debt $101.1B + leases $20.6B = ~$121.7B of obligations against $242.5B of liquid assets → **~$121B net cash**. That is comfortable. But debt **doubled in six months**, interest expense **quintupled y/y** ($261M → $1,278M in Q2), and deferred tax liabilities jumped **$21.9B** — the direct consequence of marking up the private-equity book (taxes will eventually be owed if/when gains are realized or as book-tax differences reverse).
- **The equity raise is the single most important governance signal.** Alphabet issued **$30.5B of common stock** and **$19.0B of convertible preferred** in a six-month window while **suspending buybacks entirely**. A company with a $120B net cash pile that raises equity is telling you the forward capital requirement (AI data centers, TPU capacity, power, and strategic AI investments) is **larger than internally generated cash flow**. This is a structural re-rating of Alphabet's capital-return profile: from ~100% FCF returner to net capital consumer.
- **Dilution:** shares +1.17% in six months from the equity issuance, plus a **$19B convertible preferred overhang** (derivative liabilities rose from $379M to $1,958M, consistent with embedded conversion/warrant features). Assume 1.5–2.5% annual dilution for modeling.
- **Private-asset mark risk cuts both ways.** $124.3B of non-marketable equity (Family FV-NI) with $85.7B of cumulative upward marks. Those marks flow **through the income statement** because AOCI is only −$2.3B. A down-round environment in private AI names would produce **large reported earnings hits with no cash impact** — the mirror image of Q2. Both directions will create violent headline-EPS volatility.
- **Litigation:** current contingency accrual $17.4B (+$1.8B in six months), with a $3.0B payment made in Q3 2025 (regulatory/antitrust). Ongoing legal drag is real but fully provided for and manageable relative to $80B+ of H1 operating income.
- **Working capital quality:** AR +10% against revenue +24% y/y (DSO ≈ 52 days) — collections are tight. Deferred revenue $10.1B (+17%) versus revenue +24% — bookings growth slightly lagging billings growth; not alarming, but softer than the top line.
- **SF gross intangibles jumped from $2.5B → $10.6B** and amortization rose 2.2x y/y ($246M → $545M) — evidence of **acquired technology/IP** in H1 FY2026, funded out of the debt/equity raise. Amortization schedule: $1.30B next 12 months, $1.14B, $1.10B, $1.06B in years 2–4.

---

## 6. Financial History & Multi-Year Trend (what the tag set supports)

| Metric (USD m) | FY2023 | FY2024 | FY2025 | H1 FY2026 |
|---|---:|---:|---:|---:|
| Financing cash flow (10-K disclosed) | (72,093) | (79,733) | (37,388) | **+86,320** |
| Capex accrued but unpaid (year-end) | 7,435 | 10,326 | 15,090 | 29,113 (6/30) |
| Finance lease principal payments | 705 | 405 | 1,988 | 840 (H1) |
| Revenue | n/a* | n/a* | n/a* | 229,692 |
| Operating income | n/a* | n/a* | n/a* | 80,466 |
| Diluted EPS | n/a* | n/a* | n/a* | 14.24 |

\*The returned point-in-time fact set did not include FY2023–FY2025 income-statement line items (the vendor's response was truncated to the same tag subset for all three statement types). The three identifiable multi-year series above tell one consistent story: **capex accruals compounding ~40–45%/yr for three straight years, while financing flows swung from −$72B/−$80B of shareholder returns (2023–2024) to −$37B (2025) to +$86B of net capital raising (H1 2026).** That is the multi-year arc: *shareholder-return machine → AI infrastructure capital sink.*

For context on the LTM trend that *is* verifiable: H1 revenue +23.1%, H1 operating income +30.0%, H1 CFO +32.8%, H1 capex +103%. Momentum is positive at the top of the P&L and negative at the bottom of the cash flow statement.

---

## 7. Insider Transactions

**DATA UNAVAILABLE.** The vendor's data package contains **no authorized, point-in-time insider-transactions archive for GOOGL as of 2026-08-04**. This is a genuine data gap for this analysis — no inference about insider buying or selling has been made and none should be drawn from this report. Treat insider sentiment in GOOGL as **unknown** for this week's work.

---

## 8. Actionable Trading Insights

**Constructive (buy-side / long-bias support):**
1. **The core franchise is accelerating, not decelerating.** +24% revenue and +30% operating income with margin *expansion* while absorbing a 43% y/y increase in depreciation is genuinely impressive operating leverage. If margins are still expanding with depreciation up 43%, the AI buildout is monetizing faster than it is costing.
2. **Gross margin improvement is the tell.** Cost of revenue fell from 40.5% → 38.4% of revenue y/y despite the depreciation surge — consistent with high-margin Cloud/AI compute revenue scaling faster than infrastructure cost. This is the single best quality signal in the print.
3. **Balance sheet risk is not a near-term concern.** ~$121B net cash, 44x interest coverage (H1 operating income / H1 interest), AA-tier access to capital. The debt raise is opportunistic, not distress-driven.
4. **Huge embedded asset value not in operating earnings.** $124.3B of private stakes (with $85.7B of unrealized appreciation) plus $242B of liquid assets. Sum-of-the-parts support exists beneath the operating business — and this is a live source of positive EPS surprises.

**Cautions (sell-side / risk-management):**
1. **Do not annualize reported EPS.** Q2 diluted EPS $9.11 → H1 $14.24. An LTM P/E built on this will look absurdly cheap and is **wrong**. Use ~$2.7/qtr (~$11 annualized) clean operating EPS as the base, and treat equity revaluations as a separate, mark-to-market investment line.
2. **Negative FCF in Q2 and $29.1B of accrued-but-unpaid capex.** H2 FY2026 FCF will likely be negative or near zero. Any catalyst that forces capex discipline (or a credit-market wobble) is the biggest swing factor for the stock.
3. **Buyback cessation + $30.5B equity + $19B converts = a structural bid withdrawal.** The historical ~1–2%/yr share-count shrink is now **share-count growth**. That removes a reliable EPS tailwind and signals management sees higher-return uses for cash (AI capacity) — bullish if right, dilutive if ROI disappoints.
4. **Sequential margin compression Q1→Q2 (36.1% → 34.0%).** Watch this line item above all others next quarter. A second sequential decline, combined with rising depreciation and interest, would be the first crack in the operating-leverage narrative.
5. **Mark-to-market volatility is now a headline-EPS feature.** $136B of H1 pre-tax equity gains inflate the tax line ($41.4B, 19.1% ETR vs 17.1%) and create a $22.8B deferred tax liability. A risk-off move in private AI valuations could produce a multi-tens-of-billions reported loss quarter with zero cash impact — expect headline-driven drawdowns.
6. **Legal overhang:** $17.4B contingency accrual, +$1.8B in H1. Ongoing but provided for.

**Watchlist for the next 90 days (ranked):**
1. Q3 capex dollars (does it exceed $50B/quarter?) and FY guidance.
2. Q3 operating margin — is sequential compression transitory or a trend?
3. Any resumption of share repurchases (bullish signal on capital discipline) or further equity/convert issuance (bearish signal on capital need).
4. Deferred tax liability and the private-portfolio marks (both directions).
5. Cloud/AI backlog via deferred revenue (currently +17% y/y vs revenue +24%).

---

## 9. Data Gaps & Methodological Notes (read before trading on this)

- **Revenue is derived, not reported:** `CostsAndExpenses + OperatingIncomeLoss`. It reconciles cleanly across Q1/Q2 and H1 for both years, but it is a derivation, not the reported top line.
- **No segment data** (Google Services / Cloud / Other Bets), **no R&D line**, **no goodwill**, and **no retained earnings** were present in the returned fact set.
- **FY2023–FY2025 income statement history was not returned** in usable form; multi-year trends are limited to the capex-accrual and financing-cash-flow series from the FY2025 10-K.
- **No price, market cap, share price, or consensus estimate data** was available from these tools — **no valuation multiples or price targets are expressed in this report by design.** All conclusions are fundamental, not price-based.
- **Insider transaction data: unavailable** (see §7).
- "Clean EPS" figures are **my reconstructions** (operating income + net interest, taxed at the reported ETR, divided by derived diluted shares of ~12.27B). They are estimates to isolate the operating business and should not be treated as GAAP or management-adjusted figures.
- Periodicity caveat: capital-intensive companies show large intra-year seasonal swings; H1 figures should not be doubled blindly for full-year estimates given the $29.1B capex accrual sitting at the half-year mark.

---

## 10. Key Points Summary

| Category | Metric / Fact | Value | Signal | Trading Implication |
|---|---|---|---|---|
| **Growth** | Q2 FY26 revenue (derived) | $119.8B, **+24.2% y/y** | 🟢 Strong | Core franchise accelerating |
| **Growth** | H1 FY26 revenue | $229.7B, +23.1% y/y | 🟢 Strong | Consistent, not a one-quarter spike |
| **Profitability** | Q2 operating income | $40.77B, +30.4% y/y | 🟢 Strong | Operating leverage intact |
| **Profitability** | Q2 operating margin | **34.0%** vs 32.4% y/y | 🟢 Expanding | Beats depreciation headwind |
| **Profitability** | Q2 margin vs Q1 FY26 | 34.0% vs 36.1% | 🟡 Watch | First sequential compression — key Q3 test |
| **Margins** | Cost of revenue % of revenue | 38.4% vs 40.5% y/y | 🟢 Improving | Best quality signal in the print |
| **Reported EPS** | Q2 diluted EPS | **$9.11** vs $2.31 | 🔴 Distorted | ~71% of pre-tax income is non-cash equity marks |
| **Clean EPS** | Q2 est. ex-equity-gains diluted EPS | **~$2.69** vs ~$2.17 (+24%) | 🟢 Solid | Use THIS as the earnings base |
| **Earnings quality** | Q2 non-operating income / pre-tax income | $97.98B of $138.75B (70.6%) | 🔴 Low quality | Ignore headline EPS beats/misses |
| **Capex** | H1 FY26 PP&E purchases | **$80.6B, +103% y/y** | 🔴 Massive | 35.1% of revenue vs 21.2% |
| **Capex** | Q2 capex alone | $44.9B (+25.9% q/q) | 🔴 Accelerating | Annualizing >$160B |
| **Capex** | Accrued but unpaid capex at 6/30 | **$29.1B** vs $10.6B y/y | 🔴 Leading indicator | Q3 capex & outflow will be larger |
| **Cash flow** | H1 operating cash flow | $84.9B, +32.8% y/y | 🟢 Strong | Cash earnings still excellent |
| **Cash flow** | H1 free cash flow | **$4.26B vs $24.25B (−82%)** | 🔴 Collapsed | FCF margin 1.9% vs 13.0% |
| **Cash flow** | Q2 free cash flow | **−$5.86B** | 🔴 Negative | Likely first negative FCF quarter in company history |
| **Capital return** | H1 share repurchases | **$0 vs $28.3B** | 🔴 Halted | EPS tailwind removed |
| **Capital return** | H1 dividends | $5.23B (+5.1%); $0.22/qtr declared | 🟡 Modest | Immaterial yield; still growing |
| **Financing** | Gross capital raised H1 | **$109.5B** (debt $56.2B, common $30.5B, converts $19.1B, NCI $3.8B) | 🔴 Regime change | Net capital consumer, not returner |
| **Leverage** | Total debt | $101.1B vs $49.1B (+106% in 6 mo) | 🟡 Rising fast | Interest expense 5x y/y ($261M→$1,278M) |
| **Liquidity** | Cash + ST investments | **$242.5B** (+91%) | 🟢 Fortress | ~$121B net cash; no solvency risk |
| **Dilution** | Shares outstanding | 12,230M vs 12,088M (+1.17%) | 🟡 Dilutive | Plus $19B convertible preferred overhang |
| **Asset value** | Non-marketable equity securities | **$124.3B** vs $64.1B (+94%) | 🟢 Hidden value | $85.7B cumulative unrealized gains |
| **Asset value** | H1 equity FV-NI gains (pre-tax) | **$135.9B** | 🟡 Two-way risk | Flows through income (not OCI); reversible |
| **Tax** | Deferred tax liability | $22.8B vs $0.9B | 🟡 Consequence | Built on unrealized investment gains |
| **Tax** | Effective tax rate | 19.1% vs 17.1% | 🔴 Headwind | Raise in ETR compresses clean EPS |
| **Compensation** | SBC (H1) | $15.2B, 6.6% of revenue | 🟡 Elevated | Q2 SBC +33% y/y to $8.0B |
| **Working capital** | AR growth vs revenue growth | +10% vs +24% | 🟢 Healthy | DSO ~52 days; tight collections |
| **Forward demand** | Deferred revenue | $10.1B, +17% y/y | 🟡 Lagging | Slower than revenue growth |
| **Legal** | Contingency accrual (current) | $17.4B, +$1.8B in H1 | 🟡 Overhang | Provided for; $3.0B paid in Q3 FY25 |
| **Insider activity** | Insider transactions | **DATA UNAVAILABLE** | ⚪ Unknown | Do not infer; gap in dataset |

---

### Bottom line for the trader

GOOGL's operating engine is firing on all cylinders — **+24% revenue, +30% operating income, expanding margins, +33% operating cash flow.** The market narrative around AI monetization is being validated in the P&L. But the **capital intensity and capital-structure pivot of the last six months is the dominant new fact**: capex doubling, FCF going to zero (and negative in Q2), buybacks eliminated, $105B+ raised externally, dilution turning positive, and reported earnings now hostage to mark-to-market swings on a $124B private-asset book.

**Trade the operating line, discount the headline EPS, and treat free cash flow and capital-return policy as the primary risk monitors through FY2026.**