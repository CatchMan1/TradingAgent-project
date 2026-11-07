# AMZN — Fundamental Research Report
**Amazon.com, Inc. | As of 2026-08-27 (point-in-time)**
**Primary source: SEC EDGAR facts accepted through 2026-08-27. Latest filing: Form 10-Q (accn 0001018724-26-000026), filed 2026-07-31 for the quarter ended 2026-06-30. Prior 10-Q: 0001018724-26-000014, filed 2026-04-30 (Q1 2026).**

---

## 0. Data provenance, freshness and limitations (read first)

| Item | Status |
|---|---|
| Latest financial filing | **Q2 2026 10-Q, filed 2026-07-31** — i.e. ~4 weeks before today. **No new SEC filing landed in the past week** (Aug 20–27). The "past week" window is therefore informationally quiet; all analysis below reflects the Q2 print plus the Q1 10-Q comparatives. |
| Statement periods available | Q2 2026 (3m & 6m), Q1 2026, and prior-year comparatives (Q2 2025, H1 2025). |
| `freq=annual` requests | Returned **identical** point-in-time fact sets — the vendor does not expose pre-2026 fiscal-year statements for AMZN. Where I need a trailing-twelve-month (TTM) figure, it is computed as *12 months ended 2026-06-30* (a directly reported 10-Q figure where tagged). |
| Revenue | The `RevenueFromContractWithCustomer` tag was **not returned**. Revenue below is **derived exactly** as `CostsAndExpenses + OperatingIncomeLoss`, which I validated against known prior-year actuals (Q2-25 = $167,702M, H1-25 = $323,369M — both tie out to the cent). Treat derived revenue as reliable but label-driven. |
| Insider transactions | **DATA UNAVAILABLE.** The news-data vendor has no authorized point-in-time insider archive for AMZN as of 2026-08-27. I will **not** infer or fabricate insider activity. This is a genuine information gap, not a "no transactions" signal. |
| Price / market data | No price, market-cap or consensus tools were provided. **No valuation multiples are computed** below; I supply the earnings/cash-flow run-rates a valuation agent needs to combine with price. |
| Total shareholders' equity / retained earnings / PP&E / goodwill | Tags not returned. I include a labelled estimate rather than asserting a precise figure. |

---

## 1. Company profile (from returned fact set)

- **Identity confirmed:** Amazon.com, Inc. (CIK 0001018724), a single registrant with **3 operating segments** (`NumberOfOperatingSegments = 3`) — North America, International, and AWS.
- **Share structure:** 10.0B shares authorized; 11.298B issued / **10.783B outstanding** at 2026-06-30; **10,786,313,572** outstanding as of the 2026-07-22 record date. Par $0.01. No treasury/buyback or dividend tags returned — consistent with AMZN's long-standing zero-dividend, zero-buyback policy.
- **Diluted share count (EPS-derived):** Q2-26 ≈ 10,895M vs Q2-25 ≈ 10,812M → **~0.8% YoY dilution**, mild.
- **Geographic/currency:** material FX translation exposure (AOCI FX component −$1,563M in H1-26 vs +$4,849M in H1-25), so the USD strengthening/weakening backdrop is a real reported-earnings variable.

---

## 2. Income statement — the operating story (derived revenue)

### 2.1 Quarterly and half-year reconstruction ($M)

| $ millions | Q1 2025 | Q2 2025 | H1 2025 | Q1 2026 | Q2 2026 | H1 2026 |
|---|---:|---:|---:|---:|---:|---:|
| **Revenue (derived)** | **155,667** | **167,702** | **323,369** | **181,519** | **200,606** | **382,125** |
| Cost of goods & services | 76,976 | 80,809 | 157,785 | 87,463 | 95,778 | 183,241 |
| COGS % of revenue | 49.4% | 48.2% | 48.8% | 48.2% | 47.7% | 48.0% |
| Marketing | 9,763 | 11,416 | 21,179 | 10,314 | 11,698 | 22,012 |
| G&A | 2,628 | 2,965 | 5,593 | 2,587 | 2,788 | 5,375 |
| Other operating (fulfillment, tech & infra, D&A, etc.) | 47,895 | 53,341 | 101,236 | 57,303 | 62,881 | 120,184 |
| **Total costs & expenses** | **137,262** | **148,531** | **285,793** | **157,667** | **173,145** | **330,812** |
| **Operating income** | **18,405** | **19,171** | **37,576** | **23,852** | **27,461** | **51,313** |
| **Operating margin** | **11.8%** | **11.4%** | **11.6%** | **13.1%** | **13.7%** | **13.4%** |
| YoY revenue growth | — | — | — | **+16.6%** | **+19.6%** | **+18.2%** |
| YoY operating income growth | — | — | — | **+29.6%** | **+43.2%** | **+36.6%** |

**Actionable read:** this is the highest-quality part of the print. Revenue growth **accelerated** (16.6% → 19.6%) on a $200B+ quarterly base, *and* operating margin expanded **+230bps YoY in Q2** (11.4% → 13.7%). Margin expansion came from **every** line: COGS −50bps, and — most importantly — **discretionary opex was cut in absolute terms**:

- **Marketing expense +2.5% YoY in Q2** (vs +19.6% revenue) and **+3.9% in H1** → ~100bps of margin.
- **G&A −6.0% YoY in Q2**, **−3.9% in H1** → headcount/corporate cost discipline.
- **Stock-based comp −7.6% YoY in Q2** ($6,038M vs $6,534M) and −1.5% in H1. A declining SBC line at a mega-cap tech company is unusual and is a real, high-quality earnings tailwind (and removes a common bear criticism).
- The "other operating" catch-all grew **+17.9% in Q2 / +18.7% in H1 — below revenue** despite absorbing a **+31% surge in depreciation & amortization**. Ex-D&A, core fulfillment/tech cost growth is running meaningfully below revenue: genuine operating leverage.

### 2.2 The depreciation wave — the key forward margin risk

| $ millions | Q2 2025 | Q2 2026 | YoY | H1 2025 | H1 2026 | YoY | TTM 6/30/26 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Depreciation & amortization | 15,227 | **19,988** | **+31.3%** | 29,489 | **38,933** | **+32.0%** | **75,200** |
| of which pure depreciation | 9,766 | 13,869 | +42.0% | 18,822 | 26,703 | +41.9% | n/a |

Pure depreciation is growing **~42% YoY** — the mechanical consequence of the AI/data-center capex being placed in service. D&A is already **10.0% of revenue** (Q2-26) vs 9.1% a year ago. **At current run-rates, D&A alone consumes ~2 full points of operating margin per year of growth**; the Q2 margin beat was achieved *despite* this. This is the single number to monitor: if revenue growth decelerates below ~15% while depreciation keeps compounding at 30%+, margin expansion reverses.

---

## 3. Earnings quality — the non-operating distortion is enormous

This is the most important analytical adjustment a trader must make on AMZN right now.

| $ millions | Q1 2025 | Q2 2025 | H1 2025 | Q1 2026 | Q2 2026 | H1 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Operating income | 18,405 | 19,171 | 37,576 | 23,852 | 27,461 | 51,313 |
| **Non-operating income (expense)** | 3,274 | **1,686** | **4,960** | 15,982 | **53,396** | **69,378** |
| Pre-tax income | 21,665 | 20,857 | 42,536 | 39,845 | 80,857 | 120,691 |
| Income tax | 4,553 | 2,678 | 7,231 | 9,560 | 18,199 | 27,759 |
| Effective tax rate | 21.0% | 12.8% | 17.0% | 24.0% | 22.5% | **23.0%** |
| **Net income** | **17,127** | **18,164** | **35,291** | **30,255** | **62,647** | **92,902** |
| Diluted EPS | 1.58 | 1.68 | 3.27 | 2.78 | **5.75** | **8.53** |

**Bridge of H1-26 non-operating income ($69,378M):**

| Component | H1 2026 | H1 2025 |
|---|---:|---:|
| Upward revaluation of **non-marketable equity securities** | **62,814** | 86 |
| Interest & investment income | 2,430 | 2,151 |
| Interest expense | (2,114) | (1,057) |
| FX transaction gains | 387 | 68 |
| Warrant fair-value adjustment | (1,051) | (212) |
| Marketable equity securities FV-NI gains | 454 | 188 |
| Unrealized gain on marketable securities | 430 | 250 |
| **Identified subtotal** | **63,350** | 1,474 |
| Residual (unbridged — likely realized gains on equity sales / other) | ~6,028 | ~3,486 |
| **Reported non-operating income** | **69,378** | **4,960** |

**Two-thirds of Q2-26 net income and most of the H1-26 jump is a non-cash mark-to-model revaluation of private equity stakes.** Specifically:

- `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment`: **$50,486M in Q2-26 alone, $62,814M in H1-26** (vs $49M in Q2-25).
- The carrying value of **non-marketable equity securities exploded from $16.2B (12/31/25) to $122.3B (6/30/26)** — now **11.2% of total assets**. A ~$106B, illiquid, model-valued asset that did not exist on the balance sheet six months ago.

**"Core EPS" — stripping non-operating income (same effective tax rate applied):**

| | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 |
|---|---:|---:|---:|---:|
| Pre-tax ex-non-operating (= operating income) | 19,171 | 27,461 | 37,576 | 51,313 |
| Tax @ effective rate | 12.8% | 22.5% | 17.0% | 23.0% |
| Core net income | 16,722 | **21,286** | 31,188 | **39,511** |
| Diluted shares (M) | 10,812 | 10,895 | 10,791 | 10,893 |
| **Core EPS** | **$1.55** | **$1.95** | **$2.89** | **$3.63** |
| YoY core EPS growth | — | **+26%** | — | **+26%** |

**So: reported EPS grew +242% YoY in Q2, but the underlying operating business grew core EPS +26%.** The +26% is still excellent — it just needs to be seen at the right magnitude. Anyone anchoring on a "5.75 quarterly EPS × 4 = $23 annualized" multiple will misprice AMZN by a wide margin.

**Tax anomaly to flag:** H1-26 tax expense of $27,759M was **88% deferred** (`DeferredIncomeTaxExpenseBenefit` = $30,489M), while **cash taxes paid were only $3,978M**. The deferred charge is largely the book/tax basis difference created by the private-equity marks. Cash tax generation remains a genuine, durable advantage (TTM cash taxes $6,635M vs net income $135B), but the **ETR has structurally risen from 17% to 23%** and deferred tax liabilities have ballooned — the tax shield is being consumed.

---

## 4. Cash flow — the capex supercycle, and FCF has turned negative

| $ millions | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 | TTM 6/30/25 | **TTM 6/30/26** |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash flow | 32,515 | **45,387** | 49,530 | **71,419** | 121,137 | **161,403** |
| Capex (`PaymentsToAcquireProductiveAssets`) | 32,183 | **54,208** | 57,202 | **98,411** | 107,656 | **173,028** |
| **Free cash flow** | **+332** | **(8,821)** | **(7,672)** | **(26,992)** | **+13,481** | **(11,625)** |
| Capex / revenue | 19.2% | **27.0%** | 17.7% | **25.8%** | 16.7%e | **~24%e** |
| Acquisitions (net of cash) | 1,700 | **24,359** | 1,652 | **39,767** | 4,809 | **41,956** |
| Net investing cash flow | (39,424) | (79,245) | (69,227) | **(143,457)** | (123,569) | **(216,775)** |
| Net financing cash flow | (2,539) | 10,146 | (2,586) | **+62,913** | (8,652) | **+75,160** |
| D&A (cash-flow stmt) | 15,227 | 19,988 | 29,489 | 38,933 | 58,562 | 75,200 |
| SBC | 6,534 | 6,038 | 10,223 | 10,070 | n/a | n/a |

**Three simultaneous claims on cash, all record-sized:**
1. **Capex up 72% YoY to $98.4B in six months**, $173.0B TTM — roughly **24% of revenue**. This is no longer "investment"; it is a capital-intensity regime change for AMZN.
2. **M&A up 24x to $39.8B in H1-26** ($24.4B in Q2 alone) — Amazon is buying growth inorganically for the first time at scale.
3. **Shareholder returns remain zero** (no buyback/dividend tags), so **100% of the funding gap is debt-financed**.

**Result: TTM FCF swung from +$13.5B to −$11.6B in twelve months (−$25.1B swing).** Q2-26 was the first quarter in years with **negative quarterly FCF (−$8.8B)**. Note that OCF itself is *excellent* (+44% H1) — it's still not enough. **The bull case for AMZN now requires tolerating a negative FCF trough; the bear case writes itself from this table.**

Working capital was a modest OCF tailwind (AR/other assets +$13.95B, offset by accrued liabilities −$10.06B and contract liabilities +$0.07B in H1-26), so OCF quality is acceptable but not boosted by unsustainable payables stretching — AP actually rose only 20.9% vs revenue +18%.

---

## 5. Balance sheet — a $278B asset expansion in six months

| $ millions | 12/31/2025 | 06/30/2026 | Δ | Δ% |
|---|---:|---:|---:|---:|
| Cash & equivalents | 86,810 | 78,213 | (8,597) | −9.9% |
| Marketable (AFS) securities | 45,800 | **97,900** | +52,100 | **+113.8%** |
| **Cash + AFS liquidity** | **132,610** | **176,113** | +43,503 | +32.8% |
| Accounts receivable, net | 67,729 | 88,092 | +20,363 | **+30.1%** |
| Inventory, net | 38,325 | 38,184 | (141) | −0.4% |
| **Total current assets** | **229,083** | **249,264** | +20,181 | +8.8% |
| Non-marketable equity securities | 16,200 | **122,300** | **+106,100** | **+655%** |
| Operating lease ROU asset | 86,054 | 92,743 | +6,689 | +7.8% |
| **Total assets** | **818,042** | **1,095,689** | **+277,647** | **+33.9%** |
| Accounts payable | 121,909 | 147,440 | +25,531 | +20.9% |
| Accrued liabilities | 75,520 | 73,406 | (2,114) | −2.8% |
| **Total current liabilities** | **218,005** | **241,274** | +23,269 | +10.7% |
| Long-term debt (total) | 68,836 | **132,995** | **+64,159** | **+93.2%** |
| — of which current portion | 2,748 | 3,330 | +582 | +21.2% |
| — of which non-current | 65,648 | 128,894 | +63,246 | +96.3% |
| Finance lease liability | 12,286 | 13,451 | +1,165 | +9.5% |
| Operating lease liability | 89,252 | 96,320 | +7,068 | +7.9% |
| **Total lease obligations** | **101,538** | **109,771** | +8,233 | +8.1% |
| Additional paid-in capital | 140,024 | 149,619 | +9,595 | +6.9% |
| Accumulated OCI | 28,230 | **66,287** | +38,057 | **+134.8%** |

### Liquidity and leverage read

| Metric | Value | Comment |
|---|---:|---|
| Current ratio | **1.033x** (was 1.051x) | Thin, but characteristic of AMZN's negative-working-capital retail model |
| Cash + AFS vs total current liabilities | 176,113 / 241,274 = **0.73x** | Adequate only because OCF is $45B/quarter |
| Total debt + leases | **242,766** | Was 171,925 at 12/31/25 (+41%) |
| Less: cash + AFS | (176,113) | |
| **Net debt (est.)** | **~66,653** | vs ~39,315 at 12/31/25 |
| **Annualised EBITDA proxy** (H1 op income ×2 + H1 D&A ×2) | **~180,492** | Operating income 51,313×2 + D&A 38,933×2 |
| **Net debt / EBITDA proxy** | **~0.37x** | Very low. Leverage is *not* a near-term solvency concern |
| Interest expense, Q2 | 1,314 vs 516 (+155% YoY) | |
| Net interest income, Q2 | 1,295 − 1,314 = **−19** | **AMZN has flipped from net interest income to net interest expense** — a genuine, new EPS headwind |
| Deferred revenue (contract liabilities) | 24,928 (20,428 current + 4,500 non-current) | $15.2B recognised in H1-26; modest for a company with AWS backlog |
| Disclosed contractual obligations | **650,034** total; **78,084 due ≤12m**; 53,406 yr-2; 46,767 yr-3; 42,219 yr-4 | Includes leases, debt and purchase obligations. Watch the off-balance-sheet purchase commitments (mostly AI compute & inventory) |

**Estimating the missing equity figure** (retained earnings tag not returned): cash + AFS + AR + inventory + non-marketable equity + ROU assets + small items ≈ **$534B** of the $1,095.7B asset base, implying **~$561B of PP&E + goodwill + intangibles + other assets** — up from ~$461B at 12/31/25, i.e. **~$100B of long-lived asset growth in six months** (consistent with $98.4B capex less $38.9B D&A plus acquisition goodwill). Shareholders' equity is therefore roughly **$450–500B in my estimate** (label as estimate, not filed fact). At ~$470B equity and a ~$40B "core" annualised post-tax earnings run-rate (H1 $39.5B ×2), book returns look modest — but AMZN's equity base is now materially inflated by the $122B of revalued private stakes, so ROE is a **noisy, low-signal metric here.**

**AOCI +$38B** is the third leg of the revaluation story: unrealised gains on marketable securities and the private marks are flowing through equity, not just the P&L. $66B of AOCI (6.0% of assets) is a new swing factor in book value.

---

## 6. Capital allocation and funding — the strategic pivot

| $ millions | H1 2025 | H1 2026 | TTM 6/30/26 |
|---|---:|---:|---:|
| Proceeds from LT debt issuance | 746 | **66,998** | **81,925** |
| Proceeds from ST debt | 3,908 | 15,386 | 20,798 |
| Repayments of LT debt | 2,751 | 2,752 | 5,022 |
| Repayments of ST debt | 3,474 | 15,682 | 20,634 |
| Finance lease principal payments | 821 | 863 | 1,599 |
| **Net debt raised** | **~+2,400** | **~+62,900** | **~+75,200** |
| Marketable securities purchased | 31,130 | 49,262 | 72,902 |
| Marketable securities sold/matured | 19,178 | 41,882 | 67,090 |

**Interpretation:** Amazon has shifted from "self-funding cash machine" to "levered AI-infrastructure investor" in exactly two quarters. Long-term debt **nearly doubled (+93%)**, $82B of bonds issued in twelve months, while $72.9B of securities were purchased and $42.0B spent on acquisitions. **This is the clearest strategic signal in the entire dataset** — management is willing to lever the balance sheet at scale to fund AI/compute capacity and inorganic expansion. It is defensible at 0.4x net-debt/EBITDA, but it changes the risk profile: AMZN now has a funding-cost sensitivity it hasn't had since the 2022 drawdown.

---

## 7. Insider transactions

**UNAVAILABLE — no data.** The configured news-data vendor has **no authorized, point-in-time insider-transactions archive for AMZN as of 2026-08-27**. Per instruction, I have made **no inference** about insider buying or selling, and no directional conclusion should be drawn from this section. If insider flow matters to your thesis, it must be sourced independently (Form 4 filings) before acting. Note also that AMZN's insider profile is historically dominated by scheduled 10b5-1 sales by the founder and pre-scheduled RSU vesting sales — a pattern this dataset cannot confirm or deny for the current period.

---

## 8. Red flags / watch list (ranked by importance)

1. **Negative TTM free cash flow (−$11.6B) and first negative FCF quarter (−$8.8B).** If capex stays at ~$54B/quarter while OCF runs ~$45B, the FCF hole widens each quarter. **Trigger to monitor:** any guidance suggesting capex >$220B for FY26.
2. **Reported EPS is ~3x overstated relative to core earnings.** $50.5B of the $62.6B Q2 net income came from marking private equity stakes. These marks can reverse. The $122.3B non-marketable book value is 11% of assets and 6.5% of revenue — illiquid and model-priced.
3. **Depreciation compounding at +42% YoY.** The margin story inverts if revenue growth dips below mid-teens.
4. **Debt load doubling; net interest income → net interest expense.** Q2 net interest was −$19M vs +$569M a year ago. Small now, but structurally worsening as $133B of debt reprices.
5. **AR +30.1% in six months vs revenue +18%** — a modest receivables build; allowance ratio actually *improved* (3.2% vs 3.5%), so this reads as mix (more AWS/ads) rather than credit stress. Downgrade to "monitor."
6. **AOCI +135% to $66.3B** — book value increasingly driven by mark-to-market swings rather than retained operating profit.
7. **$650B of disclosed contractual obligations** with $78B due within 12 months — fine against $176B liquidity, but this is a step-change in committed outflows.
8. **Effective tax rate 17% → 23%**, and 88% of H1 tax was deferred/non-cash. Cash-tax advantage still real but narrowing.

---

## 9. Actionable trading conclusions

**The fundamental picture is: exceptional operating momentum, deteriorating cash conversion, and a reported-earnings number that requires heavy adjustment.**

**Bull case (evidence-backed):**
- Revenue growth **re-accelerated** to +19.6% YoY on a $200B quarter — rare at this scale; H1 op income +36.6%.
- Operating margin +230bps YoY driven by *all* cost lines, and **absolute declines in marketing (−6% G&A, SBC −7.6%)** — this is structural cost discipline, not one-time.
- **Core EPS (ex-investment marks) +26% YoY** in both Q2 and H1 — a durable ~25% earnings compounder.
- Balance sheet is genuinely strong: **net debt/EBITDA ≈ 0.37x**, $176B liquidity, $161B TTM OCF.
- Valuation-sensitive buyers should note the equity is now backed by $122B of appreciated AI-ecosystem stakes — real optionality if those companies keep marking up, a real air-pocket if they don't.

**Bear case (evidence-backed):**
- **FCF is negative and worsening.** −$27.0B in H1-26 vs −$7.7B in H1-25; TTM −$11.6B vs +$13.5B. Capex at 27% of revenue with no buyback/dividend cushion.
- Reported EPS is **not** representative; a screen-based or headline-print buyer is mis-sizing the multiple.
- Depreciation +42% YoY is a **pre-committed margin headwind** for the next 4–8 quarters regardless of demand.
- Debt +93% in six months and $42.0B of M&A signal a management stance that is willing to lever into the cycle at the top.

**Positioning implications:**
- **Do not anchor on reported EPS.** Use **core EPS ~$1.95/qtr (Q2-26)** → **~$7.80 annualised** for multiple work; treat the investment marks as a separate mark-to-market overlay on book value.
- **The single most important forward indicator is quarterly capex vs OCF.** A quarter where capex decelerates *and* revenue growth holds ≥17% would be the highest-conviction bullish catalyst (FCF trough confirmation). Conversely, capex stepping above ~$60B/qtr with revenue growth <15% is the bear trigger.
- **Leverage is not the risk; the FCF trajectory is.** 0.4x net debt/EBITDA gives management years of runway — which also means the market may tolerate negative FCF longer than bears expect.
- **Risk asymmetry:** the downside from reversing private-equity marks (up to ~$122B carrying value) is far larger in magnitude than the downside from operating performance, and it is entirely outside management's operating control.
- **Catalyst calendar:** next 10-Q (~late Oct 2026) covering Q3-26 — watch capex guidance, D&A run-rate, AWS growth, and whether H2 FCF turns positive on retail seasonal working capital.

---

## 10. Key metrics summary table

| Category | Metric | Latest (Q2 2026 / 6-30-26) | Prior comparison | Direction |
|---|---|---|---|---|
| **Growth** | Revenue (derived) | $200,606M | $167,702M (Q2-25) → **+19.6% YoY** | 🟢 Accelerating (Q1 was +16.6%) |
| **Profitability** | Operating income | $27,461M | $19,171M → **+43.2% YoY** | 🟢 |
| | Operating margin | **13.7%** | 11.4% → +230bps | 🟢 |
| | H1 operating margin | 13.4% ($51,313M) | 11.6% → +180bps | 🟢 |
| | COGS as % of revenue | 47.7% | 48.2% → −50bps | 🟢 |
| | Marketing as % of revenue | 5.83% | 6.81% → −98bps | 🟢 |
| | G&A as % of revenue | 1.39% | 1.77% → −38bps | 🟢 |
| | SBC | $6,038M | $6,534M → **−7.6% YoY** | 🟢 |
| **Cost headwind** | D&A | $19,988M (**+31.3% YoY**) | Pure depreciation **+42.0%** | 🔴 |
| **Earnings** | Reported diluted EPS | **$5.75** | $1.68 → +242% | 🟡 Distorted |
| | **Core EPS ex-investment gains (my calc)** | **~$1.95** | ~$1.55 → **+26%** | 🟢 |
| | Net income | $62,647M | $18,164M | 🟡 81% non-operating |
| | H1 net income / EPS | $92,902M / $8.53 | $35,291M / $3.27 | 🟡 |
| | Non-operating income | $53,396M | $1,686M | 🔴 Non-cash marks $50,486M |
| | Effective tax rate (H1) | 23.0% | 17.0% | 🔴 |
| | Cash taxes paid (H1) | $3,978M | $5,638M | 🟢 Still advantaged |
| **Cash flow** | Operating cash flow (Q2) | $45,387M | $32,515M → +39.6% | 🟢 |
| | Capex (Q2) | $54,208M | $32,183M → **+68.4%** | 🔴 |
| | **Free cash flow (Q2)** | **−$8,821M** | +$332M | 🔴 |
| | FCF H1-26 | **−$26,992M** | −$7,672M | 🔴 |
| | **TTM FCF (6/30/26)** | **−$11,625M** | +$13,481M | 🔴 Deteriorating |
| | TTM OCF / TTM capex | $161,403M / $173,028M | $121,137M / $107,656M | 🔴 Capex > OCF |
| | Capex intensity (Q2) | **27.0% of revenue** | 19.2% | 🔴 |
| | Acquisitions H1-26 | $39,767M | $1,652M → **~24x** | 🟡 |
| **Balance sheet** | Total assets | **$1,095,689M** | $818,042M (+33.9% in 6m) | 🟡 |
| | Cash + marketable securities | **$176,113M** | $132,610M (+32.8%) | 🟢 |
| | Total debt | **$132,995M** | $68,836M (**+93.2%**) | 🔴 |
| | Total lease obligations | $109,771M | $101,538M | 🟡 |
| | Net debt (est.) | ~$66,653M | ~$39,315M | 🔴 |
| | Net debt / EBITDA proxy | **~0.37x** | ~0.2x | 🟢 Still low |
| | Current ratio | 1.033x | 1.051x | 🟡 |
| | Non-marketable equity securities | **$122,300M** (11.2% of assets) | $16,200M (**+655%**) | 🟡 Valuation risk |
| | AOCI | $66,287M | $28,230M (+135%) | 🟡 |
| | Accounts receivable | $88,092M (+30.1% in 6m) | $67,729M | 🟡 |
| | Inventory | $38,184M (flat) | $38,325M | 🟢 |
| | Net interest income (Q2) | **−$19M** | +$569M | 🔴 Flipped to expense |
| **Funding** | LT debt issued (TTM) | $81,925M | ~$746M/H1-25 | 🔴 |
| | Net financing cash flow H1-26 | **+$62,913M** | −$2,586M | 🔴 |
| **Structure** | Shares outstanding | 10,783M | 10,731M (+0.5%) | 🟡 Mild dilution |
| | Operating segments | 3 | — | — |
| | Dividends / buybacks | **None** | None | 🟡 |
| **Commitments** | Total contractual obligations | **$650,034M** | — | 🟡 |
| | Due within 12 months | $78,084M | — | 🟢 Covered by $176B liquidity |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | — | ⚪ No signal |
| **Valuation** | Multiples | **Not computed** — no price data provided | — | ⚪ Use core EPS ~$1.95/qtr |

**Bottom line for traders:** AMZN's *operating* engine is the strongest it has been — accelerating 19.6% revenue growth with 230bps of margin expansion built on real cost discipline (falling marketing, G&A and SBC in absolute terms), producing **+26% core EPS growth**. But the *financial* profile has changed character in two quarters: **FCF is negative, debt has nearly doubled, capex is 27% of revenue, and 81% of Q2 net income is a non-cash revaluation of private AI stakes.** Trade the core operating acceleration (real, verified) while sizing against the negative-FCF/debt-funded capex cycle (also real, verified) — and never quote reported EPS without the ex-marks adjustment.