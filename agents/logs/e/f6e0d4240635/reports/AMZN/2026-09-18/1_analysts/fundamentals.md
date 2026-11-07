# AMZN — Fundamental Research Report
**As of 2026-09-18 | Last SEC filing in the dataset: Form 10-Q, accepted 2026-07-31 (period ended 2026-06-30)**

---

## 0. Data provenance & caveats (read first)

- All figures below come from point-in-time SEC XBRL facts. The most recent 10-Q (filed 2026-07-31) is the latest fundamental disclosure — **no new filing or fundamental event occurred in the last 7 days**, so this report is a deep read of the Q2 2026 report plus trailing-twelve-month (TTM) roll-ups.
- The raw feed did not surface a "Revenues" tag directly, so **revenue is derived** as `CostsAndExpenses + OperatingIncomeLoss`. This method reproduces Amazon's reported Q2 2025 revenue ($167.70B) exactly, so the derivation is reliable.
- **Insider transactions: DATA UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for AMZN. No insider buying/selling is inferred or fabricated here; treat this as a genuine information gap, not a neutral signal.
- Segment-level (North America / International / AWS) P&L is not in the retrieved facts; the filing confirms **3 operating segments** but does not expose the split in this dataset.

---

## 1. Company profile (context)

Amazon.com, Inc. is a global technology and retail conglomerate operating through three reportable segments: **North America**, **International**, and **Amazon Web Services (AWS)**. Revenue pools include online stores, third-party seller services (marketplace commissions, fulfillment, shipping), advertising services, subscription services (Prime), physical stores, and AWS cloud/compute/AI infrastructure. The company is simultaneously (a) a high-volume, low-margin logistics/retail operator and (b) a high-margin cloud and advertising business — which is why consolidated margin mix shifts matter more than headline revenue.

What the 2026 filings make unmistakable is a third identity layered on top: **a very large-scale capital allocator and principal investor**, with a $122.3B portfolio of equity securities without readily determinable fair value and an annualized capex run-rate approaching $200B.

---

## 2. Income statement — Q2 2026 and H1 2026

### 2.1 Derived P&L ($ billions)

| Line | Q2 2025 | Q2 2026 | Δ y/y | H1 2025 | H1 2026 | Δ y/y |
|---|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | 167.70 | 200.61 | **+19.6%** | 323.37 | 382.13 | **+18.2%** |
| Cost of goods & services | 80.81 | 95.78 | +18.5% | 157.79 | 183.24 | +16.1% |
| Gross profit | 86.89 | 104.83 | +20.6% | 165.58 | 198.88 | +20.1% |
| Gross margin | 51.8% | **52.3%** | +50 bp | 51.2% | **52.0%** | +80 bp |
| Marketing | 11.42 | 11.70 | +2.5% | 21.18 | 22.01 | +3.9% |
| G&A | 2.97 | 2.79 | −6.0% | 5.59 | 5.38 | −3.9% |
| Total costs & expenses | 148.53 | 173.15 | +16.6% | 285.79 | 330.81 | +15.8% |
| **Operating income** | 19.17 | **27.46** | **+43.2%** | 37.58 | **51.31** | **+36.6%** |
| Operating margin | 11.4% | **13.7%** | +230 bp | 11.6% | **13.4%** | +180 bp |
| Non-operating income/(expense) | 1.69 | **53.40** | nm | 4.96 | **69.38** | nm |
| Pre-tax income | 20.86 | 80.86 | +287% | 42.54 | 120.69 | +184% |
| Income tax | 2.68 | 18.20 | — | 7.23 | 27.76 | — |
| Effective tax rate | 12.8% | **22.5%** | +970 bp | 17.0% | **23.0%** | +600 bp |
| **Net income** | 18.16 | **62.65** | **+245%** | 35.29 | **92.90** | +163% |
| Net margin | 10.8% | 31.2% | — | 10.9% | 24.3% | — |
| **Diluted EPS** | $1.68 | **$5.75** | +242% | $3.27 | **$8.53** | +161% |
| Diluted shares (implied) | ~10,810M | ~10,895M | +0.8% | ~10,793M | ~10,891M | +0.9% |

**Operating takeaway:** this is a genuinely strong core quarter. Revenue accelerated to ~19.6% growth while total costs grew only 16.6% — a ~300 bp positive spread. Cost of sales grew *slower* than revenue (18.5% vs 19.6%), marketing was nearly flat (+2.5%) despite 19.6% revenue growth (marketing fell to 5.8% of sales from 6.8%), and G&A actually declined. That is textbook operating leverage, not accounting noise.

### 2.2 The critical quality-of-earnings issue: $62.8B of non-cash mark-ups

Reported net income is **massively inflated by revaluation gains on non-marketable equity securities** (equity securities without readily determinable fair value):

- Q2 2026 upward price adjustment: **$50.49B** (vs $0.05B in Q2 2025)
- H1 2026 upward price adjustment: **$62.81B** (vs $0.09B in H1 2025)
- H1 2026 non-operating income of $69.38B is composed of: the $62.81B mark-up, investment income $2.43B, equity FV gains $0.45B, FX gains $0.39B, less interest expense $2.11B and warrant fair-value losses $1.05B.

**Adjusting for this (at the 22.5% Q2 / 23.0% H1 effective tax rate):**

| Metric | Reported | Ex-mark-to-market (est.) | y/y on core basis |
|---|---:|---:|---:|
| Q2 2026 net income | $62.65B | **~$23.5B** | +29% vs $18.16B |
| Q2 2026 diluted EPS | $5.75 | **~$2.16** | +29% vs $1.68 |
| H1 2026 net income | $92.90B | **~$44.5B** | +26% vs $35.29B |
| H1 2026 diluted EPS | $8.53 | **~$4.09** | +25% vs $3.27 |

This is the single most important number in the report. **Headline EPS growth of +242% collapses to roughly +25–29% on a core basis** — still excellent, but a completely different valuation conversation. Any screen, model, or consensus comparison using GAAP TTM EPS is distorted upward by an amount that will not recur unless the underlying private stakes appreciate again.

Corroborating detail: the carrying value of non-marketable equity securities jumped from **$16.20B (12/31/25) to $122.30B (6/30/26)** — a $106.1B increase, only $62.8B of which was mark-up; the remainder reflects purchases (large strategic/AI-related stakes) and possibly acquired positions.

### 2.3 Deferred tax tell
H1 2026 **deferred tax expense of $30.49B** against total tax expense of $27.76B, while **cash taxes paid were only $3.98B**. The mark-ups create book gains without immediate tax, so a deferred tax liability builds. Two implications:
1. Cash flow is *not* burdened — the earnings are non-cash and so is most of the tax.
2. But the balance sheet gain is unrealizable without a taxable liquidity event; the $122.3B asset is a mark, not money.

### 2.4 Cost-structure acceleration to watch
- **D&A: $19.99B in Q2 2026 (+31.3% y/y)**; $38.93B in H1 (+32.0%); **TTM $75.20B**. Depreciation alone was $13.87B in Q2 (+42% y/y).
- This is the mechanical pass-through of the capex surge and it is now visibly compressing the operating margin trajectory. Every additional $100B of annualized capex eventually adds roughly $15–20B of annual D&A.
- **Interest expense: $1.31B in Q2 (+155% y/y)**, $2.11B H1 (+100%), driven by the debt build below.
- **SBC: $6.04B in Q2 (−7.6% y/y)**, $10.07B H1 (−1.5%) — a genuine positive, and unrecognized SBC of $24.8B gives ~4 years of forward visibility. Share count grew only 0.9% y/y.

---

## 3. Balance sheet — a transformed capital structure

| Item ($B) | 12/31/2025 | 6/30/2026 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 86.81 | 78.21 | −10.0% |
| Marketable (AFS) securities | 45.80 | 97.90 | +113.8% |
| **Total liquid assets** | **132.61** | **176.11** | **+32.8%** |
| Accounts receivable, net | 67.73 | 88.09 | +30.1% |
| Inventory, net | 38.33 | 38.18 | −0.4% |
| Current assets | 229.08 | 249.26 | +8.8% |
| **Total assets** | **818.04** | **1,095.69** | **+33.9%** |
| Accounts payable | 121.91 | 147.44 | +21.0% |
| Accrued liabilities | 75.52 | 73.41 | −2.8% |
| Current liabilities | 218.01 | 241.27 | +10.7% |
| Long-term debt (noncurrent) | 65.65 | 128.89 | **+96.3%** |
| **Total long-term debt** | **68.84** | **132.99** | **+93.2%** |
| Finance lease liabilities | 12.29 | 13.45 | +9.4% |
| Operating lease liabilities | 89.25 | 96.32 | +7.9% |
| Non-marketable equity securities | 16.20 | **122.30** | **+655%** |
| AOCI | 28.23 | 66.29 | +$38.06B |
| Additional paid-in capital | 140.02 | 149.62 | +6.9% |
| Shares outstanding | 10,731M | 10,783M | +0.5% |
| **Current ratio** | 1.051x | **1.033x** | −1.8% |
| Liquid assets / current liabilities | 0.608x | 0.730x | +20% |

**Key readings:**

1. **Liquidity is adequate but thin on a current-ratio basis (1.03x).** The mitigation is that inventory is only 15% of current assets and the portfolio is $176B of cash + near-cash AFS. Against $241B of current liabilities this is tight relative to Amazon's historical norms and is being deliberately run that way to fund capex.
2. **Amazon levered up aggressively.** Long-term debt nearly doubled in six months (+$64.2B). Over the TTM to June 2026 gross LT debt issuance was **$81.93B** with only $5.02B repaid. Interest expense has already doubled y/y. This is a **structurally new credit profile** versus the 2021–2025 deleveraging era.
3. **Net debt is still negative** (net cash): ~$133.0B debt + $13.5B finance leases = ~$146.5B vs $176.1B liquid → roughly **$30B net cash**. The trajectory, not the level, is the issue.
4. **Payables up $25.5B (+21%)** — vendor financing is again a meaningful funding source and a working-capital tailwind to operating cash flow. This is reversible in a demand slowdown and should be haircut when judging OCF quality.
5. **AOCI rose $38.1B to $66.3B.** This is a large book-value addition that never touched income. Notably, the AFS portfolio is at par (gross unrealized gains just $7M, losses $67M), so this AOCI move is **not** from bond marks — composition needs to be read in the 10-Q footnotes. Treat it as non-cash book value, not distributable value.
6. **Contract liabilities (deferred revenue) were flat**: $24.93B total at 6/30/26 vs $25.00B at 12/31/25 (current $20.43B vs $20.58B). For a business growing ~19%, flat deferred revenue is a mild watch item on subscription/Prime and prepaid AWS commitments.
7. **Commitments are enormous**: total contractual obligations **$650.0B**, of which **$78.1B due in the next twelve months** (plus $14.8B operating lease and $1.8B finance lease payments within a year).

---

## 4. Cash flow — the capex shock and negative free cash flow

| Item ($B) | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 | TTM Jun-25 | TTM Jun-26 |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash flow | 32.52 | **45.39** | 49.53 | **71.42** | 121.14 | **161.40** |
| Capex (productive assets) | 32.18 | **54.21** | 57.20 | **98.41** | 107.66 | **173.03** |
| **Free cash flow** | **+0.33** | **−8.82** | **−7.67** | **−26.99** | **+13.48** | **−11.63** |
| Business acquisitions, net | 1.70 | 24.36 | 1.65 | 39.77 | 4.81 | 41.96 |
| Investing cash flow | −39.42 | −79.25 | −69.23 | −143.46 | −123.57 | −216.78 |
| Financing cash flow | −2.54 | +10.15 | −2.59 | +62.91 | −8.65 | +75.16 |
| D&A | 15.23 | 19.99 | 29.49 | 38.93 | 58.56 | 75.20 |
| Cash taxes paid | 4.76 | 2.66 | 5.64 | 3.98 | 11.79 | 6.64 |

**This is the defining fundamental story of the period.**

- **Operating cash flow is accelerating hard**: TTM $161.4B, +33.3% y/y; Q2 alone +39.6% y/y. Cash conversion remains excellent.
- **But capex is outrunning it**: TTM capex $173.0B, +60.7% y/y. Q2 2026 capex of $54.21B equals **27.0% of quarterly revenue** and rose 22.6% sequentially from Q1's $44.20B. H1 capex was 25.8% of revenue.
- **FCF has swung from +$13.5B to −$11.6B on a TTM basis**, and to −$27.0B in H1 2026 alone.
- **The gap is being funded with debt and asset sales**, not equity: +$81.9B LT debt issuance, +$20.8B short-term borrowings, offset by $5.0B LT and $20.6B ST repayments TTM; plus $67.1B of marketable securities sales/maturities net of $72.9B purchases.
- **$42.0B of TTM business acquisitions** (including $24.4B in Q2 2026 alone) is a second, often-overlooked cash drain and explains part of the AR (+30%) and goodwill growth. This is a materially more acquisitive Amazon than the 2023–2025 pattern ($1.7B in H1 2025).

**Interpretation for traders:** Amazon has entered a classic "invest through the P&L" phase. Historically, this pattern (2021–2022) preceded a multi-quarter FCF drought and a de-rating, then a powerful FCF recovery once capex plateaued. The bull case requires that the AI/cloud build converts to AWS revenue before D&A and interest overwhelm operating leverage; the bear case is that the conversion lags by 4–8 quarters.

---

## 5. Insider activity

**No data available.** The configured vendor returned: *"the B-project data package has no authorized, point-in-time insider-transactions archive for AMZN by 2026-09-18. Do not infer or fabricate insider activity."*

Traders should source Form 4s directly. This report makes **no** directional inference from insider behavior — an absence of data is not an absence of selling.

---

## 6. Synthesis: what the fundamentals actually say

**Genuinely bullish evidence**
1. Revenue growth **accelerated** to +19.6% y/y in Q2 (from ~16.6% in Q1 2026), with Q2 revenue +10.5% q/q.
2. Operating income +43% y/y on a 13.7% margin — **+230 bp of margin expansion** — achieved with marketing nearly flat and G&A down. This is real operating leverage, not cost deferral.
3. Gross margin at a record 52.3%, up 50 bp y/y, despite a retail-heavy mix.
4. OCF +33% TTM; cash taxes are unusually low ($6.6B TTM) and SBC is flat-to-down with only 0.9% dilution.
5. A $122.3B strategic equity portfolio (up from $16.2B) is a substantial off-income-statement asset base and an option on the AI ecosystem.

**Genuinely bearish / risk evidence**
1. **Earnings quality is poor at the headline level**: ~$62.8B of the $92.9B H1 net income is a non-cash, non-recurring mark-up. Core EPS growth is ~25%, not ~161%.
2. **TTM FCF is negative (−$11.6B) for the first time in this cycle**, with H1 capex +72% y/y and Q2 capex at 27% of revenue. Depreciation is already +31% y/y and will keep climbing.
3. **Debt doubled in six months** ($68.8B → $133.0B), interest expense +155% y/y, current ratio 1.03x, and $78.1B of contractual obligations due within 12 months.
4. **$106B of balance-sheet expansion in non-marketable equity** is marked, not monetized, and is exposed to reversal. A 20% mark-down would erase ~$24B pre-tax of book value and produce a headline loss quarter.
5. **Deferred revenue flat y/y** and the absence of the AWS/segment split in this dataset leave a key growth vector unverified.
6. **No insider data** — a monitoring gap, not a confirmed negative.

**Actionable framing for a trading decision**
- **Do not value AMZN off headline TTM GAAP EPS.** Normalize to ~$4.09 H1 core EPS (annualized ~$8.20) and use EV/EBIT on $51.3B H1 operating income (annualized ~$102.6B) rather than P/E.
- **The single highest-information variable is the Q3 2026 print (expected late October 2026)**: specifically (a) whether capex guidance steps up again from the ~$197B annualized Q2 run-rate, (b) whether AWS/AI revenue growth re-accelerates to justify it, and (c) whether deferred revenue and RPO inflect. A capex guide-up with flat backlog is the bearish combination; a capex plateau with accelerating AWS is the bullish one.
- **Watch the debt trajectory as a leading indicator.** At the current pace (+$64B in six months), Amazon could add another $60–100B of gross debt before year-end 2026. Credit spreads and any rating commentary will move before the equity does.
- **Expect enormous GAAP earnings volatility that is unrelated to operations.** Any quarter can post a multi-tens-of-billions swing from private-stake marks (both directions). Options-implied moves around earnings will remain elevated for reasons that have nothing to do with retail or cloud.
- **Near-term asymmetry:** operating momentum and margin expansion argue against short exposure; negative FCF and doubled leverage argue against paying a premium multiple. The risk/reward is most attractive on weakness driven by FCF/leverage headlines rather than by operating-metric deterioration.

---

## 7. Key data summary

| Category | Metric | Value | y/y / period change | Signal |
|---|---|---|---:|---|
| **Growth** | Q2 2026 revenue (derived) | $200.61B | +19.6% | Bullish — accelerating |
| | H1 2026 revenue | $382.13B | +18.2% | Bullish |
| **Profitability** | Q2 2026 operating income | $27.46B | +43.2% | Bullish |
| | Q2 2026 operating margin | 13.7% | +230 bp | Bullish |
| | Q2 2026 gross margin | 52.3% | +50 bp | Bullish |
| | H1 2026 operating margin | 13.4% | +180 bp | Bullish |
| **Earnings quality** | Q2 2026 non-operating income | $53.40B | vs $1.69B | ⚠️ Distortion |
| | H1 2026 equity mark-up gains | $62.81B | vs $0.09B | ⚠️ Non-cash, non-recurring |
| | Q2 2026 GAAP diluted EPS | $5.75 | +242% | ⚠️ Inflated |
| | Q2 2026 core EPS (ex-mark) | ~$2.16 | +29% | Bullish, realistic |
| | H1 2026 core EPS (ex-mark) | ~$4.09 | +25% | Bullish, realistic |
| | H1 2026 effective tax rate | 23.0% | +600 bp | Neutral |
| | H1 2026 cash taxes paid | $3.98B | vs $5.64B | Positive (cash) |
| **Cash generation** | TTM operating cash flow | $161.40B | +33.3% | Bullish |
| | TTM capex | $173.03B | +60.7% | ⚠️ Aggressive |
| | **TTM free cash flow** | **−$11.63B** | from +$13.48B | ⚠️ Bearish |
| | H1 2026 FCF | −$26.99B | from −$7.67B | ⚠️ Bearish |
| | Q2 2026 capex / revenue | 27.0% | +7.8 pts | ⚠️ Peak-cycle intensity |
| | TTM business acquisitions | $41.96B | from $4.81B | ⚠️ Cash drain |
| **Balance sheet** | Total assets | $1,095.69B | +33.9% in 6M | Expanding |
| | Cash + AFS securities | $176.11B | +32.8% in 6M | Strong liquidity |
| | Total long-term debt | $132.99B | +93.2% in 6M | ⚠️ Leveraging up |
| | Net debt (incl. finance leases) | ~−$29.6B (net cash) | narrowing fast | Neutral/⚠️ |
| | Current ratio | 1.033x | −1.8% | ⚠️ Thin |
| | Non-marketable equity securities | $122.30B | +655% in 6M | Option, but mark risk |
| | AOCI | $66.29B | +$38.06B in 6M | Non-cash book value |
| | Deferred revenue (total) | $24.93B | ~flat | ⚠️ Watch item |
| | Contractual obligations | $650.03B | $78.08B due <12M | ⚠️ Commitments |
| **Cost structure** | Q2 2026 D&A | $19.99B | +31.3% | ⚠️ Rising headwind |
| | Q2 2026 interest expense | $1.31B | +154.7% | ⚠️ Rising |
| | Q2 2026 SBC | $6.04B | −7.6% | Positive |
| | Q2 2026 marketing / revenue | 5.8% | −1.0 pt | Positive |
| | Diluted share growth | 10,895M | +0.8% | Positive |
| **Insider** | Insider transactions | **Unavailable** | — | Data gap |
| **Catalyst** | Next report | Q3 2026 (late Oct 2026, expected) | — | Key event |

**Bottom line:** AMZN's *operating* engine is firing on all cylinders — 19.6% revenue growth, +43% operating income, 230 bp of margin expansion, and record gross margin. But the *reported* earnings are being flattered by ~$62.8B of non-cash private-equity marks, while free cash flow has turned negative and leverage has doubled in six months to fund a ~$200B annualized capex program. Trade the operating momentum, but size positions off core EPS (~$2.16 in Q2, ~$4.09 in H1) and EV/EBIT, not the headline $5.75. The Q3 print's capex guide versus AWS/backlog growth is the decisive swing factor.