# GOOGL — Fundamental Deep Dive
**Company:** Alphabet Inc. (Class A) · **Ticker:** GOOGL · **Analysis date:** 2026-09-21
**Latest filing in the dataset:** Q2 2026 Form 10-Q, accepted 2026-07-23 (period ended 2026-06-30). FY2025 Form 10-K accepted 2026-02-05.

> **Data note up front:** The fundamental feed returns a fixed alphabetical window of XBRL tags and truncates before the revenue, segment, R&D, total-liabilities and total-equity lines. I therefore **derived revenue as `Costs and Expenses + Operating Income`** (a method that reconciles exactly to reported Q2 2025/H1 2025 Alphabet totals of $96,428M and $186,662M), and I label all derived/estimated figures as such. No market price was available, so no valuation multiples are asserted. Insider data was returned as **unavailable** and is not inferred.

---

## 1. Executive summary

| Signal | Reading | Why it matters |
|---|---|---|
| **Core operating momentum** | Revenue **+24.2% YoY** in Q2'26, **+23.0%** in H1'26; operating income **+30.4% / +30.0%**; operating margin **34.0% / 35.0%** | Genuine, accelerating operating leverage — the strongest part of the story |
| **Reported EPS is not the operating EPS** | Q2'26 diluted EPS **$9.11**, but **~$6.51/share** is after-tax mark-to-market gain on equity securities | Capitalizing $9.11 would overpay by roughly 3.4x on earnings power |
| **Earnings quality** | **62.8%** of H1'26 pre-tax income ($135.7B of $216.2B) came from non-operating investment gains | Non-recurring, reversible, and outside management control |
| **Free cash flow inflection** | H1'26 FCF **$4.3B vs $24.3B** (-82%); **Q2'26 FCF negative (-$6.9B)** | The single most important change in the fundamental picture |
| **Capex super-cycle** | H1'26 capex **$80.6B (+103% YoY) = 35.1% of revenue**; capex/depreciation **5.9x** | Depreciation cliff lands in 2027; margin risk is deferred, not absent |
| **Balance sheet** | Net cash **~$139B**; debt $101.1B (+106%); liabilities ~32% of assets | Capacity to fund the build-out without distress |
| **Capital allocation pivot** | Buybacks **$0 vs $28.3B** in H1'25; **$30.5B common + $19.0B convertible preferred** issued; share count +1.2% | Historic shift from returning capital to issuing it — dilution and a signal |
| **Insider activity** | **Data unavailable** | Cannot be used as a signal either way |

**Bottom line:** GOOGL's *operating* business is compounding faster than at any point in the dataset (revenue +24%, operating income +30%, gross margin +210bp). But the headline income statement and EPS are dominated by a **$136B half-year revaluation of equity stakes** that is non-cash, illiquid in part, and fully reversible. Simultaneously, the company has crossed into a **negative quarterly free-cash-flow regime** and, for the first time, is **issuing equity rather than retiring it**. Traders should underwrite GOOGL on operating income, core EPS (~$2.68 in Q2) and forward FCF — not on the $9.11 print.

---

## 2. Company profile

Alphabet Inc. is the parent of Google and is organized into:
- **Google Services** — Search, YouTube advertising, subscriptions/platforms/devices, and the Google network.
- **Google Cloud** — enterprise cloud infrastructure (Google Cloud Platform), Workspace, and AI/enterprise offerings.
- **Other Bets** — earlier-stage businesses (autonomous driving, life sciences, etc.), funded partly by external minority capital (see §5.2).

The financial signature in this dataset is consistent with a **hyperscale AI infrastructure build-out**: capex up 103% YoY, purchased "other investments" up 9.5x, finite-lived intangibles gross up 4.3x ($2.47B → $10.59B), interest expense up 5x to support $101B of debt, and a large, concentrated equity-investment portfolio ($124.3B of securities without readily determinable fair value, plus $99.5B of available-for-sale debt securities).

*Segment-level revenue and Cloud backlog figures were not returned by the feed and are not estimated here.*

---

## 3. Income statement — Q2 2026 and H1 2026

### Table 1 — Income statement summary ($M unless noted)

| Line item | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | **119,796** | 96,428 | **+24.2%** | **229,692** | 186,662 | **+23.0%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| **Gross profit** | **73,853** | 57,389 | +28.7% | **142,478** | 111,262 | +28.1% |
| **Gross margin** | **61.6%** | 59.5% | +210 bp | **62.0%** | 59.6% | +240 bp |
| Operating expenses (derived) | 33,083 | 26,118 | +26.7% | 62,012 | 49,385 | +25.6% |
| G&A (reported) | 6,461 | 5,209 | +24.0% | 10,752 | 8,748 | +22.9% |
| **Operating income** | **40,770** | 31,271 | **+30.4%** | **80,466** | 61,877 | **+30.0%** |
| **Operating margin** | **34.0%** | 32.4% | +160 bp | **35.0%** | 33.1% | +188 bp |
| Non-operating income | **97,983** | 2,662 | +3,581% | **135,699** | 13,845 | +880% |
| — of which equity securities FV gains | 99,031 | 1,286 | n.m. | 135,946 | 11,044 | n.m. |
| Interest expense (non-op.) | 1,278 | 261 | +390% | 1,811 | 295 | +514% |
| Interest income | 1,430 | 1,050 | +36.2% | 2,811 | 2,051 | +37.1% |
| Pre-tax income | **138,753** | 33,933 | +309% | **216,165** | 75,722 | +185% |
| Income tax | 26,560 | 5,737 | +363% | 41,394 | 12,986 | +219% |
| **Effective tax rate** | **19.1%** | 16.9% | +220 bp | **19.1%** | 17.1% | +200 bp |
| **Net income** | **112,193** | 28,196 | **+298%** | **174,771** | 62,736 | **+179%** |
| Net income to common | 112,107 | 28,196 | +298% | 174,685 | 62,736 | +178% |
| **Diluted EPS** | **$9.11** | $2.31 | **+294%** | **$14.24** | $5.12 | **+178%** |
| Basic EPS | $9.23 | $2.33 | +296% | $14.41 | $5.16 | +179% |
| Allocated SBC | 8,000 | 6,000 | +33.3% | 15,200 | 11,500 | +32.2% |
| SBC % of revenue | 6.7% | 6.2% | +46 bp | 6.6% | 6.2% | +46 bp |

### 3.1 Revenue and margin — the genuinely bullish core

- **Q1 2026 revenue was $109.9B (+21.8% YoY); Q2 accelerated to $119.8B (+24.2%).** Two consecutive quarters of *acceleration* is the cleanest evidence of demand strength in the report.
- **Gross margin expanded 210–240 bp** despite the AI compute build-out. In a period when depreciation is ramping (H1 depreciation $13.6B, +43% YoY), expanding gross margin implies either strong pricing/ mix (cloud, AI) or operating efficiencies offsetting compute costs. This is the highest-quality line in the income statement.
- **Operating leverage was driven by gross margin, not opex discipline.** Opex grew +26.7% in Q2 (faster than revenue), with G&A +24.0%; the margin expansion came entirely from the 61.6% gross margin. That makes the gross margin line the key variable to monitor.
- **Revenue growth of 23–24% on a ~$460B+ annualized base** (H1'26 annualized $459.4B) is exceptional for a company of this size and supports a premium multiple on *operating* earnings.

### 3.2 The non-operating distortion — the single most important analytical adjustment

- H1 2026 non-operating income of **$135.7B** versus operating income of $80.5B. **62.8% of pre-tax profit came from outside the business.**
- The driver is `EquitySecuritiesFvNiGainLoss` of **$135.9B in H1** (Q2 alone: **$99.0B**), of which $21.5B was unrealized gains on marketable equity and the balance is dominated by revaluation of the portfolio (cumulative upward adjustments on non-marketable equity rose from $44.5B to **$85.7B** in six months).
- **These marks flow through net income**, so reported EPS is hostage to private-company valuations and public equity prices. A reversal would hit GAAP EPS dollar-for-dollar (pre-tax), with no cash impact.

### 3.3 EPS bridge — operating vs reported (derived)

| Measure | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Reported diluted EPS | $9.11 | $2.31 | +294% | $14.24 | $5.12 | +178% |
| Less: after-tax equity FV gains/share | ~$6.51 | ~$0.09 | n.m. | ~$8.94 | ~$0.75 | n.m. |
| **Operating-only EPS (est.)** | **~$2.68** | ~$2.13 | **+26%** | **~$5.29** | ~$4.19 | **+26%** |

**Read-through:** The true operating earnings growth rate is **~26%**, not 294%. That is still an excellent number — but it implies a dramatically different valuation framework. Any screen or model keying off the $9.11 print is overstating run-rate earnings by roughly 3.4x. Note also that Q2 operating EPS absorbs $1.28B of interest expense that did not exist a year ago.

---

## 4. Balance sheet — fortress, but increasingly marked-to-market

### Table 2 — Balance sheet summary ($M)

| Item | 2026-06-30 | 2025-12-31 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| Cash + short-term investments | **242,474** | 126,843 | +91.2% |
| Accounts receivable, net | 69,175 | 62,886 | +10.0% |
| Available-for-sale debt securities | 99,500 | n/a | — |
| Equity securities w/o readily determinable FV | **124,259** | 64,094 | +93.9% |
| Current assets | 343,524 | 206,038 | +66.7% |
| **Total assets** | **921,983** | 595,281 | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| Accrued income taxes, current | 5,233 | 523 | +900% |
| Employee-related liabilities | 15,086 | 17,546 | -14.0% |
| Contract liabilities (total) | 10,100 | 8,600 | +17.4% |
| Loss contingency accrual, current | 17,356 | 15,594 | +11.3% |
| **Debt (carrying)** | **101,085** | 49,085 | **+105.9%** |
| Finance lease liabilities | 2,590 | 2,500 | +3.6% |
| Operating lease liabilities | 18,037 | 15,954 | +13.1% |
| Deferred tax liabilities, net | **22,819** | 919 | **+2,383%** |
| Deferred tax assets, net | 1,448 | 9,113 | -84.1% |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| Convertible preferred stock | **18,023** | 0 | new |
| AOCI | (2,285) | (1,916) | -19.3% |
| Shares outstanding (M) | 12,230 | 12,088 | +1.2% |

### 4.1 Asset composition — a $327B six-month expansion, much of it marks

Total assets rose **$326.7B (+54.9%) in six months**. The identifiable drivers:
1. **~$136B of equity-securities revaluation** (mirror image of the P&L gain) — no cash involved.
2. **$60.2B increase in non-marketable equity** (strategic/AI investments).
3. **$80.6B of capex** (H1 cash outflow).
4. **~$110B of gross new financing** (debt + equity + preferred).

Implication: a meaningful share of the balance sheet now consists of **marked investments whose carrying value is opinion-based or market-correlated**. Of the $922B asset base, ~$224B is cash/investments plus $124B of non-marketable equity — roughly **38% of assets are financial rather than operating**. That is a valuation-risk channel that did not exist at this scale historically.

### 4.2 Debt, liquidity and coverage

- **Debt doubled** to $101.1B; finance leases add $2.6B. Interest expense annualizes to **~$5.1B** (H1 $1.8B vs $0.3B a year ago) — roughly a 5% average cost.
- **Gross cash + ST investments of $242.5B vs $103.7B of debt → net cash ~$139B.** Even after the debt raise, the company remains net-cash by a wide margin.
- **Interest coverage: ~44x** (H1 operating income $80.5B / interest $1.8B). No refinancing or solvency risk.
- **Current ratio ~2.3x (derived)** on ~$343.5B current assets against ~$145–150B of identifiable current liabilities. Working capital is ample.
- Accounts receivable grew only **+10.0%** against **+24.2%** revenue growth — receivables are *not* stretching; implied Q2 DSO ~53 days. A positive quality datapoint (no channel-stuffing signal).

### 4.3 Deferred taxes — a $22.8B future tax bill

The net deferred tax position swung from a **$8.2B net asset to a $21.4B net liability** (DTL $919M → $22,819M; DTA $9,113M → $1,448M). This is the tax on unrealized investment appreciation. Two consequences:
1. **Cash taxes are currently understated relative to book taxes:** H1 cash flow adds back **$27.5B of deferred taxes** against a $41.4B book tax charge. Cash tax paid was therefore only ~$13.9B on $216.2B of pre-tax income.
2. **Realization of gains triggers cash tax** at ~19–21%; the DTL is a credible future cash drag and a reason not to treat the investment gains as fully "free" equity value.
3. Also note **accrued income taxes current jumped to $5.2B from $0.5B** — a ~$4.7B near-term cash tax payment is likely due.

### 4.4 Equity and dilution

Total equity is not returned by the feed, but reconciling identifiable liabilities (~$294–297B) against $922.0B of assets implies **stockholders' equity of roughly $600–630B (derived)**. On that base:
- Debt/equity ~16%; liabilities/assets ~32% — a conservatively financed balance sheet.
- Core (ex-gain) annualized net income of ~$130B on average equity of ~$515B implies **core ROE ~25%** — still elite.
- **Dilution is now a real line item:** shares +1.2% in six months, $30.5B of common stock issued (average ~$215/share implied), plus **$19.0B of convertible preferred** issued 2026-06-05 carrying $18.0B book value and $86M of quarterly preferred dividends. Conversion terms were not in the dataset; treat the preferred as a potential future share overhang.

---

## 5. Cash flow and capital allocation — the major regime change

### Table 3 — Cash flow summary ($M)

| Item | H1 2026 | H1 2025 | Change | Q2 2026 | Q2 2025 |
|---|---:|---:|---:|---:|---:|
| Operating cash flow | **84,859** | 63,897 | +32.8% | 39,069 | 27,747 |
| Capital expenditures | **(80,598)** | (39,643) | +103.3% | (45,924) | (22,446) |
| **Free cash flow (derived)** | **4,261** | **24,254** | **-82.4%** | **(6,855)** | **+5,301** |
| Purchases of other investments | (22,051) | (2,312) | +854% | — | — |
| Net marketable securities purchases | (9,784) | +1,060 | n.m. | — | — |
| **Investing cash flow** | **(145,822)** | (40,738) | 3.6x | — | — |
| Debt proceeds | 56,226 | 31,378 | +79.2% | — | — |
| Debt repayments | (5,253) | (18,397) | -71.4% | — | — |
| **Common stock issued** | **30,499** | 0 | new | — | — |
| **Convertible preferred issued** | **19,063** | 0 | new | — | — |
| Minority capital raised | 3,758 | 400 | +840% | — | — |
| Dividends paid | (5,231) | (4,977) | +5.1% | — | — |
| **Share repurchases** | **0** | **(28,306)** | **-100%** | — | — |
| **Financing cash flow** | **+86,320** | (26,033) | n.m. | — | — |
| FX effect | (154) | 444 | n.m. | — | — |
| **Net change in cash** | **+25,203** | (2,430) | n.m. | — | — |

### 5.1 FCF has effectively gone to zero — the key bear datapoint

- **H1 free cash flow collapsed 82% to $4.3B** (1.9% FCF margin vs 13.0%). **Q2 2026 FCF was negative $6.9B** — the first negative quarter in the dataset.
- **Capex intensity: 38.3% of Q2 revenue** (vs 23.3%), 35.1% for H1 (vs 21.2%). Q1 capex $35.7B, Q2 $45.9B — still *rising* sequentially.
- **Capex/depreciation = 5.9x.** Depreciation was only $13.6B in H1 versus $80.6B of spend. When this asset base turns over, depreciation could plausibly triple from current levels — a **multi-year margin headwind that is not yet in the P&L.** This is the mechanism by which today's 35% operating margin could compress even with healthy revenue growth.
- **Accrued but unpaid capex of $29.1B** (vs $10.6B a year ago, +174%) confirms the cash outflow continues into Q3.
- **OCF quality is flattered by $27.5B of deferred taxes** (§4.3). Adjusting for that, cash generation is even tighter relative to the capital being deployed.

### 5.2 The capital-allocation pivot — the most strategically significant change

- **Buybacks: $28.3B in H1 2025 → $0 in H1 2026.** Management has fully stopped supporting EPS and the share price with repurchases.
- **Yet the company raised equity:** $30.5B common + $19.1B convertible preferred + $3.8B minority capital = **$53.4B of equity-like inflows** in six months, against $5.2B of dividends out.
- **Interpretation:** management is treating its equity as *currency to deploy*, not to retire — consistent with funding an enormous AI infrastructure/strategic-investment program (other-investment purchases up 9.5x to $22.1B; intangibles gross up 4.3x to $10.6B, implying acquisitions).
- **Trading implication:** the historical "buyback bid" that cushioned GOOGL drawdowns is absent. Net share count is *rising* 1.2% per half-year, so per-share metrics now have a modest structural headwind rather than tailwind. If a large strategic deal is behind the raise, event risk is elevated in both directions.

### 5.3 Cash returned to shareholders

- Dividends $5.2B (+5.1%); DPS $0.22 in Q2 vs $0.21 (+4.8%); H1 $0.43 vs $0.41.
- **Payout only ~3.0% of reported net income** (~8% of core earnings). Capital return is immaterial to the thesis now; this is a reinvestment story.

---

## 6. Financial history and trend context

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---:|---:|---:|---:|
| Financing cash flow ($M) | (72,093) | (79,733) | (37,388) | **+86,320** |
| Capex incurred but unpaid, year-end ($M) | 7,435 | 10,326 | 15,090 | 29,113 (6/30) |
| Finance lease principal payments ($M) | 705 | 405 | 1,988 | 840 |

**What the history shows:**
1. **A three-year retreat from shareholder returns** (-$72B → -$80B → -$37B) that culminated in a **full reversal to +$86B of financing inflow** in H1 2026. This is a structural break, not a quarterly quirk.
2. **The capex ramp began in 2025** — accrued capex nearly doubled in FY2025 ($10.3B → $15.1B) before exploding to $29.1B by mid-2026. The build-out is still accelerating.
3. FY2025's 10-K (accepted 2026-02-05) and the Q1 2026 10-Q (accepted 2026-04-30) are the only other point-in-time filings in the window; **no new SEC filing has been accepted in the past week.** The fundamental picture is unchanged since the 2026-07-23 Q2 print.

*Note: full-year FY2023–FY2025 income statements were not returned by the feed (tag truncation), so a five-year revenue/margin history cannot be constructed reliably and is not estimated.*

---

## 7. Insider transactions

**DATA UNAVAILABLE.** The vendor's point-in-time archive contains **no authorized insider-transaction records for GOOGL as of 2026-09-21**. I am explicitly not inferring, estimating, or fabricating insider buying or selling. Any insider-flow-based signal should be treated as absent for this analysis; traders wanting that input must source Form 4 data independently.

---

## 8. Earnings-quality scorecard

| Test | Result | Assessment |
|---|---|---|
| Operating cash flow / net income | 0.49x (H1'26) | **Weak** — depressed by $136B non-cash gains |
| OCF / operating income | 1.05x | Healthy |
| Non-operating share of pre-tax income | 62.8% | **Red flag** — earnings not from operations |
| Revenue growth vs receivables growth | +24.2% vs +10.0% | **Good** — no receivables stretch |
| Gross margin trend | +210 bp YoY | **Good** |
| Capex / depreciation | 5.9x | **Red flag (forward)** — depreciation cliff |
| FCF margin | 1.9% (Q2 negative) | **Red flag** |
| SBC / revenue | 6.6% (rising) | Caution — real dilution cost |
| Cash tax vs book tax | ~$13.9B vs $41.4B | **Caution** — $27.5B deferred, DTL $22.8B |
| Share count | +1.2% in 6 months | **Caution** — dilution replaces buyback |
| Balance sheet leverage | Net cash ~$139B; D/E ~16% | **Strong** |
| Interest coverage | ~44x | **Strong** |

**Net assessment:** high *operating* quality, low *reported-earnings* quality, deteriorating *cash* quality, and an unimpeachable *solvency* position.

---

## 9. Actionable takeaways for traders

1. **Do not capitalize the $9.11 Q2 EPS.** ~71% of it ($6.51) is after-tax mark-to-market gains. Anchor valuation on **operating-only EPS of ~$2.68 (Q2) / ~$5.29 (H1)**, growing ~26% YoY. A screen-based "cheap on P/E" conclusion is a trap; equally, a "P/E of 60" conclusion from core earnings is the honest comparison.

2. **The bull case is operating acceleration, and it is real.** Revenue accelerated from +21.8% (Q1) to +24.2% (Q2), gross margin expanded 210 bp, and operating income grew 30%. If you are long, this — not the investment gains — is what you are underwriting. Watch gross margin as the canary: margin expansion is doing all the work offsetting +26.7% opex growth.

3. **The bear case is the FCF/ depreciation math.** Q2 FCF was **-$6.9B**; capex is 38% of revenue and still rising sequentially; capex is 5.9x depreciation. Even a modest revenue deceleration combined with a tripling depreciation base compresses margins. Position sizing should reflect that the P&L has not yet absorbed this cost.

4. **Treat the investment portfolio as a separate, volatile asset — not as earnings.** $124.3B of non-marketable equity plus $99.5B of AFS securities ≈ 24% of assets. Marks are reversible: a private-markdown cycle would produce *negative* non-operating income of similar magnitude to the 2026 gains, making reported EPS swing violently. This argues for **higher implied volatility around reporting dates** than the operating business alone would justify.

5. **Respect the capital-allocation regime change.** Zero buybacks + $30.5B common + $19.0B convertible preferred + $3.8B minority capital = the company is **selling equity to fund growth**. Historically GOOGL supported its multiple with buybacks; that support is gone and share count is rising. This is a legitimate de-rating argument independent of operating performance, and it also signals management sees unusually large deployment opportunities (or obligations).

6. **The balance sheet buys time — use it as a floor argument.** ~$139B net cash, 44x interest coverage, 32% liabilities/assets. Even a severe FCF drought is survivable for years. This limits downside tail risk from financing and is the strongest counter to the FCF bear case.

7. **Watch the tax line.** $22.8B of deferred tax liabilities and a $5.2B current tax accrual mean **cash taxes are set to normalize upward**. If the company begins monetizing stakes, expect a step-up in cash outflows that further pressures FCF.

8. **Near-term catalyst calendar:** next print is the **Q3 2026 10-Q (likely late October 2026)**. Highest-value items: (a) capex guidance/run-rate, (b) gross margin durability, (c) whether buybacks resume, (d) any reversal in investment marks, (e) Cloud growth/backlog (not available in this feed), (f) convertible preferred conversion terms.

---

## 10. Data limitations (read before acting)

- **Revenue, segment revenue, R&D, sales & marketing, total liabilities, total equity, goodwill, and share-count-by-class were not returned** by the vendor's truncated tag window. Revenue is *derived* and validated against reported Q2'25/H1'25 totals; equity (~$600–630B) and current ratio (~2.3x) are *derived estimates* and should be treated as approximate.
- **No market price or share-price data** — no P/E, EV/EBITDA, or FCF yield is asserted.
- **Insider transactions: unavailable** (see §7).
- **No SEC filing was accepted in the past week**; the analysis reflects the 2026-07-23 Q2 10-Q and 2026-02-05 FY2025 10-K.
- The dataset contains several magnitudes that are far outside Alphabet's historical norms (a $136B half-year investment gain, a $30.5B common stock issuance, a $19B convertible preferred). They are reported as given; if they reflect a vendor mapping issue rather than economic reality, the earnings-quality conclusions would change materially. **Verify against the primary 10-Q before sizing positions.**

---

## Summary table — key points at a glance

| Category | Metric | Value (latest) | vs Prior Year | Signal | Trade implication |
|---|---|---|---|---|---|
| **Growth** | Revenue (derived) | $119.8B (Q2'26) | +24.2% | **Bullish** | Operating acceleration is genuine and improving |
| **Growth** | Revenue (derived) | $229.7B (H1'26) | +23.0% | **Bullish** | ~$459B annualized run-rate |
| **Profitability** | Gross margin | 61.6% (Q2) | +210 bp | **Bullish** | Pricing/mix offsetting compute costs |
| **Profitability** | Operating income | $40.8B (Q2) | +30.4% | **Bullish** | Best-in-class operating leverage |
| **Profitability** | Operating margin | 34.0% (Q2) / 35.0% (H1) | +160 / +188 bp | **Bullish** | But capex depreciation not yet absorbed |
| **Earnings quality** | Reported diluted EPS | $9.11 (Q2) | +294% | **Distorted** | ~71% is mark-to-market gains |
| **Earnings quality** | Operating-only EPS (est.) | ~$2.68 (Q2) | ~+26% | **Solid** | Use this for valuation, not $9.11 |
| **Earnings quality** | Non-op. share of pre-tax income | 62.8% (H1) | from 18.3% | **Red flag** | Gains are non-cash and reversible |
| **Cash flow** | Operating cash flow | $84.9B (H1) | +32.8% | Good | But includes $27.5B deferred-tax add-back |
| **Cash flow** | Capex | $80.6B (H1) | +103.3% | **Caution** | 35.1% of revenue; still rising |
| **Cash flow** | Free cash flow (derived) | $4.3B (H1) / **-$6.9B (Q2)** | -82% / negative | **Bearish** | The core fundamental deterioration |
| **Cash flow** | Capex / depreciation | 5.9x | from ~4.2x | **Red flag (forward)** | Depreciation cliff into 2027 |
| **Balance sheet** | Cash + ST investments | $242.5B | +91.2% | **Strong** | Ample dry powder |
| **Balance sheet** | Total debt | $101.1B | +105.9% | Caution | But net cash ~$139B |
| **Balance sheet** | Deferred tax liabilities | $22.8B | from $0.9B | **Caution** | Future cash tax on unrealized gains |
| **Balance sheet** | Total assets | $922.0B | +54.9% (6 mo.) | Note | ~24% is investment marks |
| **Capital return** | Buybacks | **$0** (H1) | from $28.3B | **Bearish** | Historical price support removed |
| **Capital return** | Common + preferred issued | $30.5B + $19.0B | from $0 | **Bearish/caution** | Dilution; shares +1.2% |
| **Capital return** | Dividends | $5.2B (H1); $0.22/qtr | +5.1% / +4.8% | Neutral | ~3% payout; immaterial to thesis |
| **Solvency** | Interest coverage | ~44x | from ~210x | Strong | No financial stress |
| **Solvency** | Net cash | ~$139B | lower | Strong | Downside cushion |
| **Insider** | Insider transactions | **Unavailable** | — | n/a | No signal; do not infer |
| **Verdict** | — | — | — | **Constructive on operations, cautious on reported earnings & FCF** | Underwrite on operating EPS/FCF; expect elevated EPS volatility from marks |