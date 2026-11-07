# AMZN — Fundamental Research Report
**As of 2023-12-29 | Company: Amazon.com, Inc. | Ticker: AMZN**

---

## 1. Data provenance & caveats (important for interpretation)

- All figures below are drawn from AMZN's **point-in-time SEC filings** in the data package — principally the **Q3 2023 Form 10-Q (period ended 2023-09-30, filed 2023-10-27)** and the **Q2 2023 10-Q (filed 2023-08-04)**. Annual-frequency requests returned the same 10-Q fact set (no full-FY 10-K facts for FY2022 totals are present in this package).
- **Revenue is not reported as a standalone tagged line** in this dataset. I have **derived revenue arithmetically** where valid using the accounting identity **Revenue = Operating Income + Costs & Expenses**. This derivation reconciles precisely with AMZN's known reported net sales (e.g., 9M-2023 ≈ $404.8B; Q3-2023 ≈ $143.1B), so it is reliable. Derived values are flagged "(derived)."
- **Insider transactions: DATA UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for AMZN by 2023-12-29. No insider buying/selling is inferred or fabricated.
- Currency: **USD**. Values below are in **$ millions** unless noted.

---

## 2. Company profile

**Amazon.com, Inc. (AMZN)** is a global technology and e-commerce conglomerate. Per the filings, the company reports **three operating segments** (`NumberOfOperatingSegments = 3`): **North America, International, and Amazon Web Services (AWS)**. Its business spans online and physical retail, third-party seller marketplaces, advertising, subscription services (Prime), logistics/fulfillment, and cloud computing (AWS) — the latter being the primary profit engine. The company is a heavy, sustained investor in fulfillment, data-center, and technology infrastructure, and carries large operating- and finance-lease obligations reflecting its physical footprint.

---

## 3. Income statement — a clear profitability inflection

Derived revenue vs. reported profitability reveals a decisive margin turnaround story, driven by cost discipline, fulfillment/logistics efficiency, and a rebound in high-margin businesses.

### 3.1 Revenue (derived)
| Period | Revenue (derived) | YoY growth |
|---|---|---|
| Q3 2023 (Jul–Sep) | **$143,083M** | +12.6% vs Q3 2022 ($127,101M) |
| 9M 2023 (Jan–Sep) | **$404,824M** | +11.0% vs 9M 2022 ($364,779M) |

### 3.2 Profitability
| Metric | Q3 2023 | Q3 2022 | 9M 2023 | 9M 2022 |
|---|---|---|---|---|
| Cost of goods & services sold | 75,022 | 70,268 | 212,186 | 203,191 |
| **Gross profit (derived)** | **68,061** | 56,833 | **192,638** | 161,588 |
| Gross margin (derived) | **47.6%** | 44.7% | **47.6%** | 44.3% |
| Operating income | **11,188** | 2,525 | **23,643** | 9,511 |
| Operating margin | **7.8%** | 2.0% | **5.8%** | 2.6% |
| Pretax income | 12,189 | 2,944 | 23,871 | (4,974) |
| Income tax expense | 2,306 | 69 | 4,058 | (1,990) |
| **Net income** | **9,879** | 2,872 | **19,801** | (3,000) |
| Diluted EPS | **$0.94** | $0.28 | **$1.89** | $(0.29) |

**Key takeaways:**
- **Operating income nearly tripled YoY** in Q3 ($11.2B vs $2.5B) and rose **~2.5x** over 9M. Operating margin expanded ~580 bps YoY in Q3 to 7.8%.
- **Gross margin expanded ~300 bps** to 47.6%, evidencing fulfillment/logistics efficiencies and mix shift toward AWS/advertising.
- **Net income swung to +$19.8B (9M) from a −$3.0B loss** a year earlier. Note the 2022 loss was heavily distorted by a **−$14,485M nonoperating loss** (largely mark-to-market on equity investments such as Rivian), versus a **+$228M nonoperating result in 9M 2023** — a ~$14.7B swing that flatters the YoY comparison, so the *operating* improvement is the more durable signal.
- **Effective tax rate** normalized to ~17% in 9M 2023 vs a distorted negative rate in 2022.

### 3.3 Operating expense detail (9M)
| Expense line | 9M 2023 | 9M 2022 | Note |
|---|---|---|---|
| Marketing | 31,468 | 29,420 | +7%; growing slower than revenue → operating leverage |
| G&A | 8,806 | 8,558 | roughly flat |
| Stock-based comp | 17,704 | 14,015 | +26%; rising SBC is a dilution watch item |
| D&A | 34,843 | 29,236 | +19%; reflects past capex; a large fixed cost drag |

### 3.4 Interest & investments
- **Interest expense** rose to **$2,469M (9M 2023)** from $1,673M — higher rates on the debt stack.
- **Interest/investment income** surged to **$2,048M** from $544M, largely **offsetting** interest expense — a meaningful cushion from the ~$99B cash+securities balance.
- **Equity securities FV gains** of **+$1,000M (9M 2023)** vs −$11,300M (9M 2022) — the swing driver cited above.

---

## 4. Balance sheet — liquid, deleveraging, lease-heavy

**As of 2023-09-30 (vs 2022-12-31):**
| Item | 2023-09-30 | 2022-12-31 |
|---|---|---|
| Cash & equivalents | 49,605 | 53,888 |
| Marketable securities (AFS, FV) | 49,871 | — |
| **Cash + marketable securities** | **~99,476** | — |
| Accounts receivable (net) | 43,420 | 42,360 |
| Inventory (net) | 35,406 | 34,405 |
| **Total current assets** | 142,995 | 146,791 |
| **Total assets** | **486,883** | 462,675 |
| Accounts payable | 72,004 | 79,600 |
| Accrued liabilities | 58,812 | 62,566 |
| **Total current liabilities** | 145,214 | 155,393 |
| Long-term debt (total) | **67,472** | 70,542 |
| — of which noncurrent | 61,098 | 67,150 |
| Operating lease liabilities | 73,902 | 69,040 |
| — of which noncurrent | 65,810 | 61,582 |
| Finance lease liabilities | 12,466 | 15,783 |

**Key takeaways:**
- **Highly liquid:** ~**$99.5B** in cash + marketable securities comfortably covers **~$67.5B of debt** → a **net cash position** (before leases).
- **Current ratio ≈ 0.99** (142,995 / 145,214), improved from **0.94** at YE2022 (146,791 / 155,393). AMZN's negative working-capital model (large AP) is a structural feature, not distress.
- **Deleveraging:** long-term debt **fell to $67.5B from $70.5B**, and finance-lease liabilities dropped to $12.5B from $15.8B — consistent with debt repayment and lease maturation.
- **Lease obligations are large** (operating $73.9B + finance $12.5B ≈ **$86.4B**) — a real fixed-cost commitment layered on top of reported debt. Total undiscounted operating-lease payments are **$88.8B**; the weighted-average discount rate ticked up to **3.2%** from 2.8%.
- **Book equity (approx.):** not itemized as a single tag in the dataset; components shown include Additional Paid-In Capital of **$92,711M** (up from $75,066M, reflecting heavy SBC issuance) and AOCI of **−$5,003M**. Approximate total stockholders' equity is ~$180–185B (derived from assets minus identifiable liabilities) — note this is an estimate.
- **Share count:** 10,330M basic shares outstanding (2023-09-30), up from 10,242M at YE2022 and 10,334M as of 2023-10-18 — modest dilution from SBC.

---

## 5. Cash flow — strong, self-funding, FCF turning positive

| Cash flow metric | TTM (Oct 2022–Sep 2023) | 9M 2023 | 9M 2022 |
|---|---|---|---|
| **Operating cash flow (OCF)** | **71,654** | **42,481** | 17,579 |
| Capex (purchases of productive assets) | 54,733 | 38,141 | 47,053 |
| **Free cash flow (OCF − capex)** | **~16,921** | **~4,340** | (29,474) |
| Investing cash flow | (48,053) | (37,232) | (26,780) |
| Financing cash flow | (9,047) | (9,133) | 9,632 |

**Key takeaways:**
- **Operating cash flow nearly 2.4x'd** YoY over 9M ($42.5B vs $17.6B) — the clearest evidence of the earnings-quality turnaround.
- **Capex is moderating** (9M 2023 $38.1B vs $47.1B in 9M 2022, ~19% lower). Combined with rising OCF, **TTM free cash flow has swung firmly positive (~$16.9B)**, versus deeply negative FCF in the year-ago period (9M 2022 FCF was ~−$29.5B).
- Quarterly OCF cadence is strong: Q1 ~$4.8B, Q2 $16.5B, Q3 $21.2B — sequentially accelerating.
- Operating-lease payments of $7.7B (9M) and finance-lease principal of $3.6B (9M) are recurring cash outflows to monitor.

---

## 6. Capital allocation

- **No share repurchases in 2023:** `PaymentsForRepurchaseOfCommonStock = $0` for every 2023 YTD period (vs ~$6.0B in 9M 2022). AMZN effectively **paused buybacks** and is directing cash to debt paydown and operations.
- **Debt repaid, not raised:** 9M 2023 saw **$0 long-term debt issuance**, **$3,386M LTD repaid**, and net short-term debt reduction (proceeds $17.4B vs repayments $19.3B). Financing outflow of −$9.1B reflects deliberate **balance-sheet deleveraging** — a shareholder-friendly shift in capital discipline.
- Heavy ongoing **capex + SBC** remain the primary uses of capital.

---

## 7. Insider transactions

**Unavailable.** The data package contains no authorized point-in-time insider-transaction archive for AMZN as of 2023-12-29. No insider activity is reported, and none should be inferred. Traders should source insider data (Form 4 filings) separately if required.

---

## 8. Actionable insights & trading implications

1. **The core thesis is a genuine margin/profitability inflection, not just an investment-markup artifact.** Gross margin +300 bps and operating margin +580 bps (Q3) are driven by fulfillment efficiency and mix, evidenced by operating income tripling. This supports a **constructive/positive fundamental bias** on AMZN.

2. **Free cash flow has inflected positive (~$17B TTM) for the first time in this cycle.** Historically, sustained positive FCF regimes have preceded valuation re-rating for AMZN. This is a key bullish validation signal.

3. **Watch the quality of the earnings beat:** part of the YoY net-income swing came from the **~$14.7B nonoperating swing** (Rivian/equity marks). Traders should focus on **operating income and OCF** as the durable metrics — both are strongly positive and improving, so the bull case survives even excluding one-time marks.

4. **Balance sheet is a source of strength / downside cushion:** ~$99.5B cash+securities vs ~$67.5B debt (net cash), improving current ratio, and active deleveraging. Limits solvency risk and funds continued investment without new debt.

5. **Risk factors to weigh:** (a) **Capex remains elevated** (~$55B TTM); any re-acceleration could pressure FCF; (b) **rising SBC** ($17.7B 9M, +26% YoY) and modest dilution; (c) **~$86B of lease obligations** add fixed-cost rigidity; (d) rising interest expense ($2.5B 9M) amid higher-for-longer rates; (e) heavy reliance on AWS/advertising for profit — segment mix matters.

6. **Positioning:** Fundamentals favor **long/overweight bias into the Q4-2023 print** given accelerating OCF, positive FCF, margin expansion, and no buyback/dividend cash drain. Key catalysts to monitor: Q4 holiday retail results, AWS growth/reacceleration, advertising momentum, and whether capex guidance stays disciplined. Key risk event: a capex re-acceleration or AWS deceleration.

7. **Data gaps for the trader to fill externally:** standalone **revenue by segment** and **AWS/advertising split** are not tagged here (revenue only derivable in aggregate); **insider activity** is unavailable; and **full-FY 2022 annual totals** are not in this package. These should be sourced from the FY2022 10-K and Form 4 filings.

---

## 9. Key points summary table

| Category | Metric | Value | Trend / Interpretation |
|---|---|---|---|
| Identity | Company | Amazon.com, Inc. (AMZN) | 3 segments: N. America, Intl, AWS |
| Revenue (derived) | Q3 2023 | $143,083M | +12.6% YoY |
| Revenue (derived) | 9M 2023 | $404,824M | +11.0% YoY |
| Profitability | Q3 2023 operating income | $11,188M (7.8% margin) | vs $2,525M (2.0%) — tripled |
| Profitability | 9M 2023 operating income | $23,643M (5.8% margin) | vs $9,511M (2.6%) |
| Profitability | Q3 2023 net income | $9,879M | vs $2,872M |
| Profitability | 9M 2023 net income | $19,801M | vs −$3,000M (swing; aided by $14.7B nonop swing) |
| Profitability | Gross margin (derived, 9M) | 47.6% | +330 bps YoY |
| Per share | Diluted EPS 9M 2023 | $1.89 | vs −$0.29 |
| Earnings quality | SBC (9M 2023) | $17,704M | +26% YoY — dilution watch |
| Earnings quality | D&A (9M 2023) | $34,843M | +19% YoY |
| Cash flow | TTM OCF | $71,654M | Strong; 9M OCF 2.4x YoY |
| Cash flow | TTM Capex | $54,733M | Moderating (9M −19% YoY) |
| Cash flow | TTM Free cash flow | ~$16,921M | Swung positive from deeply negative |
| Balance sheet | Cash + securities | ~$99,476M | Very liquid |
| Balance sheet | Total long-term debt | $67,472M | Down from $70,542M (deleveraging) |
| Balance sheet | Current ratio | ~0.99 | Improved from 0.94 |
| Balance sheet | Lease obligations | ~$86.4B | Large fixed-cost commitment |
| Capital allocation | Buybacks 9M 2023 | $0 | Paused; cash to debt paydown |
| Capital allocation | LTD issued 9M 2023 | $0 | Repaid $3,386M; net debt down |
| Insider activity | Transactions | **Unavailable** | No authorized archive; do not infer |

---
*Prepared from point-in-time SEC fact data (Q3-2023 10-Q filed 2023-10-27; Q2-2023 10-Q filed 2023-08-04). Revenue and gross profit are arithmetically derived; all other figures are as reported. This is fundamental research, not investment advice.*