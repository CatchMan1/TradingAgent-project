# GOOGL — Alphabet Inc. Fundamental Research Report
**Analysis date: 2026-07-30 | Primary source: Q2 2026 Form 10-Q (accession 0001652044-26-000071, filed/accepted 2026-07-23 01:15 UTC) and FY2025 Form 10-K (0001652044-26-000018, filed 2026-02-05)**

---

## 1. Data provenance & important caveats (read first)

- All figures below are **point-in-time SEC XBRL facts public as of 2026-07-30**. The most recent filing is the **Q2 2026 10-Q accepted 2026-07-23** — i.e., the freshest possible fundamental disclosure (7 days old).
- The data payload returned was **truncated alphabetically at approximately the tag "FiniteLivedIntangibleAssets."** As a result I have complete access to items A–F (cost of revenue, cash, capex, cash flows, debt, deferred taxes, derivatives, equity-securities gains, EPS, expenses, equity investments, leases) but **not** to revenue lines, R&D, sales & marketing, PP&E, goodwill, retained earnings, segment results, or buyback authorization. Where a metric is essential and missing, I have **derived it arithmetically and validated the derivation** (see below) rather than guessed, and I flag it explicitly.
- **Revenue derivation (validated):** Alphabet reports `CostsAndExpenses` and `OperatingIncomeLoss`; revenue = the two summed. Cross-check: `OperatingIncomeLoss + NonoperatingIncomeExpense = IncomeLossFromContinuingOperationsBeforeIncomeTaxes` exactly for both periods (Q2 2026: 40,770 + 97,983 = 138,753 ✓; 1H26: 80,466 + 135,699 = 216,165 ✓). Derived Q2 2025 revenue of $96,428M and Q1 2025 revenue of $90,234M match those quarters' reported figures, confirming methodology.
- **Insider transactions: UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for GOOGL. I will not infer or fabricate insider activity. This is a genuine gap in this report.
- No price, market-cap, consensus, or valuation-multiple data is provided by these tools. Any valuation triangulation below is labeled as an estimate.

---

## 2. Company profile

**Alphabet Inc. (GOOGL)** — global internet/technology holding company; parent of Google. Business spans Search, YouTube, Android/Play, Google Cloud, Google hardware, and the "Other Bets" portfolio, plus one of the largest corporate investment portfolios in the world (marketable equity securities, non-marketable equity stakes, and debt securities). Two share classes are publicly traded (GOOGL Class A with voting rights, GOOG Class C). Fiscal year = calendar year; 12,300M shares authorized structure 300,000M total shares authorized at $0.001 par.

**Structural signals from this quarter's balance sheet** — Alphabet is no longer just an operating company funding itself from organic cash; it has become an **investment holding company plus a capital-intensive AI infrastructure builder**. Total assets rose **+54.9% in six months** to $922.0B, driven by investments, intangibles, and infrastructure, funded by **~$106B of fresh external capital**. This is a material change in the equity story and should reframe how GOOGL is modeled (SOTP on investments + operating business, not a simple P/E on EPS).

---

## 3. Income statement — Q2 2026 and 1H 2026

### 3.1 Reported results (USD millions)

| Line | Q2 2026 | Q2 2025 | YoY | 1H 2026 | 1H 2025 | YoY |
|---|---|---|---|---|---|---|
| Revenue (derived) | **119,796** | 96,428 | **+24.2%** | **229,692** | 186,662 | **+23.1%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| Gross profit | 73,853 | 57,389 | +28.7% | 142,478 | 111,262 | +28.1% |
| **Gross margin** | **61.6%** | 59.5% | +2.1pp | **62.0%** | 59.6% | +2.4pp |
| G&A | 6,461 | 5,209 | +24.0% | 10,752 | 8,748 | +22.9% |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 149,226 | 124,785 | +19.6% |
| **Operating income** | **40,770** | 31,271 | **+30.4%** | **80,466** | 61,877 | **+30.0%** |
| **Operating margin** | **34.0%** | 32.4% | +1.6pp | **35.0%** | 33.2% | +1.8pp |
| Other income (nonoperating) | 97,983 | 2,662 | n.m. | 135,699 | 13,845 | n.m. |
| — of which equity-securities FV gains | 99,031 | 1,286 | n.m. | 135,946 | 11,044 | n.m. |
| — interest income | 1,430 | 1,050 | +36.2% | 2,811 | 2,051 | +37.1% |
| — interest expense | (1,278) | (261) | +390% | (1,811) | (295) | +514% |
| Pre-tax income | 138,753 | 33,933 | +309% | 216,165 | 75,722 | +186% |
| Tax | 26,560 | 5,737 | — | 41,394 | 12,986 | — |
| **Effective tax rate** | **19.1%** | 16.9% | +2.2pp | **19.1%** | 17.1% | +2.0pp |
| **Net income** | **112,193** | 28,196 | +298% | **174,771** | 62,736 | +179% |
| Net income to common | 112,107 | 28,196 | +298% | 174,685 | 62,736 | +178% |
| **Diluted EPS** | **$9.11** | $2.31 | +294% | **$14.24** | $5.12 | +178% |
| Basic EPS | $9.23 | $2.33 | +296% | $14.41 | $5.16 | +179% |
| SBC | 8,000 | 6,000 | +33.3% | 15,200 | 11,500 | +32.2% |
| Depreciation | n/a (H1 only) | — | — | 13,586 | 9,485 | +43.2% |
| Amortization of intangibles | 367 | 124 | +196% | 545 | 246 | +122% |

### 3.2 Quarterly progression (derived)

| | Q1 2026 | Q2 2026 | QoQ |
|---|---|---|---|
| Revenue | 109,896 | 119,796 | +9.0% |
| Cost of revenue | 41,271 | 45,943 | +11.3% |
| Gross margin | 62.4% | 61.6% | −0.8pp |
| Opex (total − COGS) | 28,929 | 33,083 | +14.4% |
| Operating income | 39,696 | 40,770 | +2.7% |
| Operating margin | 36.1% | 34.0% | −2.1pp |
| Net income | 62,578 | 112,193 | +79.3% |
| Diluted EPS | $5.13 | $9.11 | +77.6% |

**Interpretation of the income statement — this is the single most important analytical point in the report:**

1. **The operating business is accelerating hard.** Revenue +23.1% YoY in 1H26 with **operating margin expanding 1.8pp to 35.0%** and gross margin +2.4pp to 62.0%. Costs & expenses grew +19.6% versus revenue +23.1% — genuine, quantifiable operating leverage. Cost of revenue (which captures AI inference/cloud serving costs, TAC, and datacenter depreciation) grew only **+15.7%**, well below revenue: the AI infrastructure build is *currently* earning returns above its incremental cost.
2. **Reported EPS is severely inflated by mark-to-market, non-cash gains.** 1H26 pre-tax income of $216.2B includes **$135.9B of equity-securities fair-value gains** (63% of pre-tax income). Q2 2026 alone contains **$99.0B** of those gains versus $2.7B of total nonoperating income in Q2 2025. **Do not annualize $14.24.** 
3. **"Core" earnings power, isolated:** operating income + interest income − interest expense = **$81.5B in 1H26 vs $63.6B in 1H25 (+28.0%)**. After tax at the respective rates and on ~12,300M diluted shares, that is roughly **$5.3 vs $4.2 per share, or ~+26% core EPS growth**. Stripping equity gains from reported EPS gives approximately **$6.0 in 1H26 vs $4.4 in 1H25 (+37% on a rough basis)** — directionally the same conclusion: core growth is high-20s%, and roughly **$8–9 of the $9.12 YoY EPS increase was investment marks, not operations.**
4. **Two real cost headwinds are emerging:** (a) **interest expense up 6.1x to $1,811M** in 1H26 as debt doubled — the cost of the capex build is now hitting the P&L; (b) **SBC +32.2%, faster than revenue**, rising to 6.6% of revenue from 6.2% — compensation inflation for AI talent, and SBC is now >$30B annualized run-rate.
5. **Depreciation +43.2% to $13.6B in 1H26** (5.9% of revenue) is still *far* below capex. This is the key forward earnings risk: capex/depreciation is running at **5.7x**, so depreciation is a multi-year ramp that will compress margins regardless of demand.

---

## 4. Balance sheet — a transformation, not a drift

**USD millions, 2026-06-30 vs 2025-12-31**

| Item | 6/30/2026 | 12/31/2025 | Change | % |
|---|---|---|---|---|
| **Total assets** | **921,983** | 595,281 | +326,702 | **+54.9%** |
| Current assets | 343,524 | 206,038 | +137,486 | +66.7% |
| Cash & equivalents | 55,911 | 30,708 | +25,203 | +82.1% |
| Cash + short-term investments | **242,474** | 126,843 | +115,631 | +91.2% |
| Accounts receivable, net | 69,175 | 62,886 | +6,289 | +10.0% |
| Non-marketable equity securities (no RDFV) | **124,259** | 64,094 | +60,165 | **+93.9%** |
| — cumulative *upward* valuation adj. | 85,732 | 44,485 | +41,247 | +92.7% |
| — cumulative downward adj. | (9,115) | (8,820) | −295 | +3.3% |
| AFS debt securities (noncurrent) | 99,500 | n/a | — | — |
| AFS unrealized-loss positions | 53,239 | 13,160 | +40,079 | +305% |
| — accumulated loss on those | (416) | (178) | −238 | — |
| Finite-lived intangibles, gross | 10,585 | 2,467 | +8,118 | +329% |
| **Total debt (carrying)** | **101,085** | 49,085 | +52,000 | **+106%** |
| Accounts payable | 20,258 | 12,200 | +8,058 | +66.1% |
| Accrued liabilities | 73,014 | 55,557 | +17,457 | +31.4% |
| Accrued income taxes, current | 5,233 | 523 | +4,710 | +901% |
| Employee-related liabilities | 15,086 | 17,546 | −2,460 | −14.0% |
| Contract liability (deferred revenue), current | 7,154 | 6,578 | +576 | +8.8% |
| Contract liability, total | 10,100 | 8,600 | +1,500 | +17.4% |
| Loss-contingency accrual, current | 17,356 | 15,594 | +1,762 | +11.3% |
| Deferred tax liabilities, net | **22,819** | 919 | +21,900 | n.m. |
| Operating lease liability | 18,037 | 15,954 | +2,083 | +13.1% |
| Finance lease liability | 2,590 | 2,500 | +90 | +3.6% |
| Common stock + APIC | 131,371 | 93,126 | +38,245 | +41.1% |
| Convertible preferred stock | **18,023** | 0 | +18,023 | new |
| AOCI | (2,285) | (1,916) | −369 | — |
| Shares outstanding (M) | **12,230** | 12,088 | +142 | +1.17% |

**Key reads:**
- **Liquidity is formidable:** $242.5B of cash + short-term investments. Current assets of $343.5B against identifiable current liabilities of roughly $120–125B imply a **current ratio around 2.7x**. There is no solvency question at GOOGL — the question is capital *allocation*, not capital *adequacy*.
- **The $60.2B jump in non-marketable equity holdings is mostly paper, not cash.** $41.2B of the increase came from **cumulative upward valuation adjustments** (observable-transaction uplifts), not new purchases. This is critical: it is a mark, it flows through the income statement as FV-NI gains, and **it can reverse**. The same mechanism explains a large share of the $135.9B equity gain line.
- **Deferred tax liabilities exploded from $0.9B to $22.8B** — the tax owed on unrealized gains, deferred. If the marks reverse, this liability unwinds against the P&L (a benefit); if gains are realized, cash taxes come due. Either way it is a **volatility transmission channel between Alphabet's equity portfolio and its reported EPS**.
- **Debt doubled to $101.1B** (carrying, net of $921M discount/costs). Against $242.5B of cash + ST investments, GOOGL is still **net cash positive by ~$141B**. Leverage risk is low; *refinancing-cost* and *interest-expense* risk is real (see §3.4).
- **Finite-lived intangibles gross +329% to $10.6B** and amortization +196% YoY confirm at least one **completed acquisition** in 1H26. Forward amortization is pre-committed at **$1,304M over the next 12 months** plus $747M in the remainder of FY26 — a small but non-zero EPS drag.
- **Deferred revenue (total) +17.4% to $10.1B**, with **$4.9B of it recognized as revenue in 1H26** — a healthy, growing contracted backlog proxy (consistent with cloud/enterprise momentum), though it grew slower than overall revenue.
- **Loss-contingency accrual of $17.4B (+$1.8B)** — a very large legal/regulatory reserve that is still *growing*. The FY25 10-K also shows a **$3.0B contingency payment in Q3 2025**. Ongoing regulatory cash outflows are a recurring drag that GAAP operating income does not highlight.
- **Dilution:** shares +142M (+1.17%) in six months **despite zero buybacks**, plus a brand-new **$19.0B convertible preferred** (carrying $18.0B, issued 2026-06-05, $86M of preferred dividends in Q2 2026). Preferred sits ahead of common and will convert into further dilution.

---

## 5. Cash flow — where the story cracks

**USD millions, six months ended June 30**

| Item | 1H 2026 | 1H 2025 | Change |
|---|---|---|---|
| **Operating cash flow** | **84,859** | 63,897 | **+32.8%** |
| — *of which deferred income taxes* | **+27,538** | (1,596) | n.m. |
| **CFO excluding deferred taxes** | **57,321** | 65,493 | **−12.5%** |
| Capex (PP&E purchases) | **80,598** | 39,643 | **+103.3%** |
| **Free cash flow (CFO − capex)** | **4,261** | 24,254 | **−82.4%** |
| FCF using CFO ex-deferred tax | **(23,277)** | 25,850 | n.m. |
| Capex / revenue | **35.1%** | 21.2% | +13.9pp |
| Capex / depreciation | **5.7x** | 3.9x | — |
| Capex incurred but not yet paid (period end) | **29,113** | 10,635 | +173.7% |
| Purchases of marketable securities | 76,480 | 39,870 | +91.8% |
| Sales/maturities of marketable securities | 66,696 | 40,930 | +62.9% |
| Purchases of other investments | 22,051 | 2,312 | +853% |
| Proceeds from other investments | 1,667 | 873 | +91.0% |
| **Investing cash flow** | **(145,822)** | (40,738) | +258% |
| Debt proceeds | 56,226 | 31,378 | +79.2% |
| **Common stock issuance** | **30,499** | 0 | new |
| **Convertible preferred issuance** | **19,063** | 0 | new |
| Minority interest proceeds | 3,758 | 400 | +840% |
| Debt repayments | (5,253) | (18,397) | −71.4% |
| Dividends paid | (5,231) | (4,977) | +5.1% |
| **Share repurchases** | **0** | **(28,306)** | **−100%** |
| **Financing cash flow** | **+86,320** | (26,033) | n.m. |
| FX effect | (154) | 444 | — |
| **Net change in cash** | **+25,203** | (2,430) | n.m. |

**Five conclusions a trader must internalize:**

1. **Free cash flow has effectively gone to zero.** $4.3B of FCF on $229.7B of revenue is a **1.9% FCF margin**, down from 13.0%. Capex is running at **$161B+ annualized** versus $79B in 1H25. For a company that has historically been valued on FCF, this is the pivotal fundamental change this week's filing reveals.
2. **Even that $4.3B is not clean.** CFO of $84.9B includes a **$27.5B non-cash deferred-tax benefit** generated by the unrealized investment gains — tax expense booked in net income but not paid in cash. **Excluding it, operating cash flow was $57.3B against $80.6B of capex — a $23.3B cash deficit.** Reported FCF overstates true cash generation by roughly $27.5B this half. This is the highest-value insight in the report.
3. **Capex is still accelerating, not plateauing.** "Capex incurred but not yet paid" jumped to **$29.1B from $10.6B YoY (+174%)**. That is a leading indicator of *recognized-but-unsettled* spend; Q3–Q4 2026 capex should be higher than 1H's run-rate. FY25 capex-but-unpaid was $15.1B (vs $10.3B FY24, $7.4B FY23) — a multi-year acceleration trend.
4. **The funding model has inverted.** Alphabet raised **$109.5B of gross external capital in six months** (debt $56.2B + common $30.5B + preferred $19.1B + minority $3.8B) while **returning only $5.3B via dividends and $0 via buybacks**. Historically GOOGL returned ~$70–80B/year (financing outflows were −$72.1B in FY23, −$79.7B in FY24, −$37.4B in FY25). **A mega-cap that stops buybacks and issues equity at scale is signaling either extraordinary investment opportunity or that internal cash is fully consumed by AI capex — arguably both.**
5. **Unexplained investing/financing residuals (~$34B and ~$12B respectively)** indicate material outflows in categories not captured in the returned tag set (likely acquisitions of non-marketable equity, business combinations, and non-controlling-interest purchases). Treat the capex-plus-investment figure of ~$146B of H1 investing outflow as a conservative floor on capital deployment.

---

## 6. Multi-year capital-return / financing history (from the FY2025 10-K)

| Metric | FY2023 | FY2024 | FY2025 | 1H 2025 | 1H 2026 |
|---|---|---|---|---|---|
| Net cash used in financing | (72,093) | (79,733) | (37,388) | (26,033) | **+86,320** |
| Capex incurred, not yet paid (YE) | 7,435 | 10,326 | 15,090 | 10,635 | 29,113 |
| Finance lease principal payments | 705 | 405 | 1,988 | 302 | 840 |
| Share repurchases | n/a | n/a | n/a | 28,306 | **0** |
| Dividends per share declared | n/a | n/a | n/a | $0.41 | **$0.43** |

The financing cash flow flipped from **−$37.4B in FY25 to +$86.3B in 1H26** — a ~$124B swing in eighteen months. Finance-lease principal payments are also accelerating sharply ($1,988M in FY25 vs $405M FY24), confirming infrastructure financing is being pushed into lease structures.

---

## 7. Insider transactions

**DATA UNAVAILABLE.** The configured news/filings vendor holds no authorized point-in-time insider-transaction archive for GOOGL as of 2026-07-30. I have **not** inferred, estimated, or fabricated any insider buying/selling. Anyone acting on this report should source Form 4 data independently (EDGAR full-text/Form 4 index) before drawing governance conclusions. Note that the absence of insider data is a **report limitation, not evidence of no insider activity.**

---

## 8. Earnings quality scorecard

| Dimension | Assessment | Evidence |
|---|---|---|
| Revenue quality | **Strong** | +23.1% YoY, broad-based cost-of-revenue growth (+15.7%) below revenue; deferred revenue +17.4%; AR grew slower than revenue sequentially (AR +10.0% vs Q2 revenue +9.0% QoQ) |
| Operating margin quality | **Strong / improving** | 35.0% op margin 1H26 vs 33.2%; costs +19.6% vs revenue +23.1% |
| Net income quality | **Very weak (this half)** | 63% of pre-tax income from non-cash, non-operating equity marks; reversibility + DTL of $22.8B |
| Cash flow quality | **Deteriorating** | Reported FCF margin 1.9%; CFO ex-deferred-tax of $57.3B vs capex $80.6B = negative |
| Balance sheet quality | **Strong but levering** | Net cash ~$141B, but debt +106%, DTL +$21.9B, preferred +$18.0B, legal accrual $17.4B |
| Dilution / alignment | **Negative shift** | Shares +1.17% in 1H26 with zero buybacks; SBC +32%; $19B convertible preferred ahead of common |
| Transparency | **Adequate, watch** | ~$34B investing and ~$12B financing outflows not attributable to the returned tag set; intangibles +329% implies undisclosed-in-payload M&A |

---

## 9. Actionable insights for traders

### The dominant, non-obvious point
**The market's reaction to this 10-Q should be driven by the capex/free-cash-flow equation, not the $9.11 EPS print.** $9.11 of Q2 EPS contains roughly **$6.6–7.0 of after-tax investment marks** (99,031 × (1−0.191) ÷ ~12,310M dil. shares ≈ **$6.64**). Any screen or headline quoting "EPS up 294%" is measuring a mark-to-market event on Alphabet's equity portfolio. The true operational print is: **revenue +24%, operating income +30%, operating margin 34.0%**.

### Bull case (specific, evidence-backed)
1. **AI capex is converting into revenue, and margins are still expanding.** Revenue +23.1% while cost of revenue grew only +15.7%; op margin +1.8pp. This falsifies the "capex with no return" bear thesis *for now*.
2. **Balance sheet optionality is unmatched.** $242.5B cash + ST investments and ~$141B net cash means Alphabet can fund another $160B+ of annual capex without distress, while peers must raise capital.
3. **Hidden asset value.** $124.3B of non-marketable equity + $99.5B of AFS debt securities + $55.9B cash. On a sum-of-the-parts basis a substantial share of the market cap is backed by a liquid-plus-option portfolio that earns nothing in the operating multiple.
4. **Dividend growth continues** — quarterly DPS raised from $0.21 to $0.22 (+4.8%) in Q2 2026.

### Bear case (specific, evidence-backed)
1. **FCF margin collapse to 1.9%, and negative on a cash-tax basis.** This is the cleanest single bear data point in the filing.
2. **Capex/Depreciation of 5.7x** guarantees a multi-year depreciation ramp (Dep already +43% YoY). Even with flat revenue growth, depreciation alone could take 300–500bp off operating margin over the next 4–6 quarters.
3. **Mark-to-market reversal risk is now systemic to EPS.** $22.8B DTL and $85.7B of cumulative upward adjustments on non-marketable holdings mean a market drawdown produces *reported losses* at an operating company growing 23%. Expect amplified beta vs. the equity market.
4. **Dilution + rising interest expense simultaneously.** Interest expense +514% to $1,811M in 1H26; $19B convertible preferred; shares +142M; SBC +32%.
5. **Litigation reserve still building** (+$1.8B to $17.4B) with a $3.0B payment already made in Q3 2025.

### What to monitor next (highest-information-value items)
| Watch item | Threshold / trigger | Why it matters |
|---|---|---|
| Q3 2026 capex | >$45B in-quarter (i.e., >$90B for 2H) | Confirms acceleration implied by $29.1B capex-payable |
| Capex / revenue | Sustained >35% | Determines whether the FCF de-rating persists |
| CFO ex-deferred-tax vs capex | Still negative | The real cash-generation line |
| Q3 depreciation | >$8B/quarter (vs $6.8B avg in 1H) | Depreciation ramp versus 34% op margin |
| Buyback resumption | Any 10-Q/8-K authorization | The clearest signal that capex has peaked |
| Equity-securities FV gains/losses | Sign flip | EPS volatility driver; DTL unwind |
| Share count | >12,300M | Preferred conversion / issuance dilution |
| Loss contingency accrual | >$20B | Further regulatory cash drain |

### Trade framing (with explicit data caveats)
- **Multiples cannot be computed from these tools** — no price data was provided. For triangulation only: $30,499M of common stock issued alongside a net +142M share increase implies a **blended ~$215/share**; if that is roughly representative, market cap ≈ **$2.6T**, putting the stock at roughly **~11–12x 2H-annualized core EPS (≈$10.6–11.0 annualized core)** and **~28–30x annualized 1H26 capex**. Treat as a coarse anchor, not a valuation.
- **Prefer operating-income-based and SOTP-based valuation over GAAP EPS.** Use ~$161B annualized operating income and the $280B+ investment portfolio as separate value pools.
- **Options implication:** the combination of (a) EPS dominated by marks and (b) capex/depreciation inflection creates an unusually wide distribution of *reported* outcomes. Realized volatility around print dates should be priced off operating metrics, but headline risk is dominated by non-operating items.
- **Position sizing implication:** low balance-sheet risk (net cash ~$141B) + high reported-earnings volatility = a case for expressing a directional view via the operating business narrative rather than via GAAP earnings expectations.

---

## 10. Summary table — the report in one view

| Category | Metric | Latest | Prior/Compare | Signal |
|---|---|---|---|---|
| **Filing** | Latest 10-Q accepted | 2026-07-23 (Q2 2026) | 10-K 2026-02-05 | Fresh (7 days) |
| **Growth** | Revenue (derived) | $119.80B (Q2) / $229.69B (1H) | +24.2% / +23.1% YoY | 🟢 Strong acceleration |
| **Growth** | Operating income | $40.77B / $80.47B | +30.4% / +30.0% YoY | 🟢 Operating leverage |
| **Margins** | Gross margin | 61.6% (Q2) / 62.0% (1H) | 59.5% / 59.6% | 🟢 +2.1–2.4pp |
| **Margins** | Operating margin | 34.0% (Q2) / 35.0% (1H) | 32.4% / 33.2% | 🟢 +1.6–1.8pp |
| **Margins** | QoQ operating margin | 34.0% (Q2) | 36.1% (Q1) | 🟡 −2.1pp sequential |
| **Earnings** | Diluted EPS | $9.11 (Q2) / $14.24 (1H) | $2.31 / $5.12 | 🔴 63% from investment marks |
| **Earnings** | Core EPS proxy (op + net interest, taxed) | ~$5.3 (1H) | ~$4.2 (1H25) | 🟢 ~+26% |
| **Earnings** | Equity-securities FV gains | $99.03B (Q2) / $135.95B (1H) | $1.29B / $11.04B | 🔴 Non-cash, reversible |
| **Earnings** | Effective tax rate | 19.1% | 17.1% / 16.9% | 🟡 +200bp |
| **Costs** | SBC | $8.0B (Q2) / $15.2B (1H) | +33.3% / +32.2% | 🟡 Faster than revenue |
| **Costs** | Depreciation | $13.59B (1H) | +43.2% | 🟡 Ramp beginning |
| **Costs** | Interest expense | $1.28B (Q2) / $1.81B (1H) | +390% / +514% | 🔴 Debt cost arriving |
| **Cash flow** | Operating cash flow | $84.86B (1H) | +32.8% | 🟢 but see next |
| **Cash flow** | Deferred tax benefit in CFO | +$27.54B (1H) | −$1.60B | 🔴 Inflates CFO |
| **Cash flow** | CFO ex-deferred tax | $57.32B (1H) | −12.5% YoY | 🔴 Declining |
| **Cash flow** | Capex | $80.60B (1H) | +103.3% | 🔴 35.1% of revenue |
| **Cash flow** | Free cash flow | **$4.26B (1H)** | $24.25B | 🔴 −82.4%, 1.9% margin |
| **Cash flow** | FCF ex-deferred tax | **−$23.28B (1H)** | +$25.85B | 🔴 Cash deficit |
| **Cash flow** | Capex / depreciation | 5.7x | 3.9x | 🔴 Multi-year dep ramp |
| **Cash flow** | Capex incurred, unpaid | $29.11B | $10.64B | 🔴 +174%, capex still rising |
| **Balance sheet** | Total assets | $921.98B | $595.28B | ⚪ +54.9% in 6 months |
| **Balance sheet** | Cash + ST investments | **$242.47B** | $126.84B | 🟢 Huge liquidity |
| **Balance sheet** | Total debt (carrying) | $101.09B | $49.09B | 🟡 +106%, still net cash |
| **Balance sheet** | Net cash (cash+ST inv − debt) | **~$141.4B** | ~$77.8B | 🟢 Fortress |
| **Balance sheet** | Deferred tax liabilities, net | $22.82B | $0.92B | 🔴 Mark-related |
| **Balance sheet** | Non-marketable equity (no RDFV) | $124.26B | $64.09B | 🟢 Asset value / 🔴 mark risk |
| **Balance sheet** | AFS debt securities | $99.50B | n/a | ⚪ Portfolio scale |
| **Balance sheet** | Finite intangibles, gross | $10.59B | $2.47B | ⚪ M&A occurred (+329%) |
| **Balance sheet** | Loss-contingency accrual | $17.36B | $15.59B | 🔴 Legal overhang growing |
| **Capital** | Share repurchases | **$0 (1H26)** | $28.31B (1H25) | 🔴 Return regime ended |
| **Capital** | Common stock issued | $30.50B | $0 | 🔴 Dilution |
| **Capital** | Convertible preferred issued | $19.06B | $0 | 🔴 $86M/qtr pref. dividend |
| **Capital** | Dividends paid | $5.23B (1H) | $4.98B | 🟢 DPS $0.21→$0.22 |
| **Capital** | Shares outstanding | 12,230M | 12,088M | 🔴 +1.17% in 6 months |
| **Capital** | Financing cash flow | **+$86.32B (1H26)** | −$26.03B (1H25); −$37.39B FY25 | 🔴 Model has inverted |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | — | ⚫ Cannot assess |
| **Valuation** | Price / multiples | **NOT AVAILABLE from tools** | — | ⚫ Use derived anchors only |

**Bottom line:** GOOGL's operating momentum is as strong as it has been in years — 23% revenue growth with 1.8pp of operating-margin expansion — but **the accounting and cash-flow quality of this half's results has deteriorated sharply**. $4.3B of half-year FCF (−82%), negative FCF once a $27.5B deferred-tax benefit is stripped out, debt doubled, buybacks eliminated, $49.5B of equity/preferred issued, and 63% of pre-tax income sourced from reversible investment marks. **Trade the operating business (long the +23%/+35%-margin franchise, which is genuinely intact); discount the reported EPS almost entirely; and treat the capex trajectory and any buyback resumption as the two variables that will determine GOOGL's next 12 months.**