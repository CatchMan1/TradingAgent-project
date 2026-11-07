# AAPL (Apple Inc.) — Fundamental Research Report
**As of 2024-01-09 | Fiscal year ends late September | All figures USD millions unless noted**
**Source: point-in-time SEC EDGAR facts filtered by actual acceptance timestamp**

---

## 1. Executive Summary

**What the data supports:** Apple's latest hard financials available on 2024-01-09 are the **FY2023 Form 10-K (FY ended 2023-09-30, accepted 2023-11-03)** plus interim 10-Q cash-flow data through **Q3 FY2023 (period ended 2023-07-01, accepted 2023-08-04)**. No filing after 2023-11-03 exists in the archive, so **Q1 FY2024 (December-quarter) results are NOT yet public at this date** — this is the key information gap and the nearest catalyst.

**Three-sentence thesis:**
1. **Apple is a high-margin, cash-gushing franchise with stalled top-line growth.** FY2023 revenue fell **-2.8% to $383.3B**, yet gross margin hit a cycle high of **44.1%** and operating margin held at **29.8%** — evidence of a richer Services mix and pricing power offsetting hardware softness.
2. **EPS growth is now almost entirely financial engineering.** FY2023 net income fell **-2.8%** but diluted EPS still rose **+0.3% to $6.13** purely because the share count shrank **-2.5%**; buybacks ($77.6B) plus dividends ($15.0B) absorbed **93% of free cash flow**.
3. **The balance sheet is fortress-grade but no longer building cash:** **~$162.1B** of cash and marketable securities against **~$111.1B** of debt (**net cash ≈ $51B**), with operating cash flow decelerating **-9.5%** in FY2023 — the single most important fundamental trend to monitor into the next print.

**Stance implied by fundamentals:** Quality/defensive long, but *not* a growth re-acceleration story on this data set. The stock requires a multiple-based re-rating case (Services mix + capital return) rather than an earnings-growth case. **This toolset contains no price data, so no P/E or FCF yield can be computed** — see §9 for the sensitivity framework to apply your own quote.

---

## 2. Company Profile & Data Scope

| Item | Detail |
|---|---|
| Entity | Apple Inc. (CIK 0000320193) |
| Ticker | **AAPL** (Nasdaq) |
| Fiscal year | 52/53-week year ending last Saturday of September |
| FY2023 period end | 2023-09-30 (10-K accepted 2023-11-03 02:08 UTC) |
| Latest interim | Q3 FY2023, period ended 2023-07-01 (10-Q accepted 2023-08-04) |
| Shares outstanding | **15,552.8M** as of 2023-10-20 (cover page); 15,550.1M at 2023-09-30 |
| Public float (market value) | **$2.591 trillion** at 2023-03-31 (10-K cover) |
| Auditor-grade filings used | 10-K FY2021–FY2023; 10-Q for 9M FY2023, 6M FY2023, 3M FY2023 |
| **Not available in this toolset** | Revenue by segment/product, gross margin by line, geographic split, guidance, current share price, consensus estimates, insider Form 4s (§8) |

**Important methodological note:** this vendor exposes *tagged XBRL facts*, not the MD&A narrative. Segment and product-line revenue tags (iPhone, Mac, iPad, Wearables, Services) are absent from the returned set, so product-level mix cannot be quantified here — only inferred from margin behavior.

---

## 3. Income Statement — Three-Year History (FY2021 → FY2023)

Revenue is **derived** as Cost of Goods & Services Sold + Gross Profit (the vendor did not return a `Revenues` tag, but the two components reconcile exactly and are internally consistent with every balance-sheet and cash-flow identity).

| Metric | FY2021 | FY2022 | FY2023 | FY23 YoY |
|---|---|---|---|---|
| **Revenue** (derived) | 365,817 | 394,328 | **383,285** | **-2.8%** |
| Cost of goods & services sold | 212,981 | 223,546 | 214,137 | -4.2% |
| **Gross profit** | 152,836 | 170,782 | **169,148** | -1.0% |
| **Gross margin %** | 41.78% | 43.31% | **44.13%** | **+82 bps** |
| Research & development + SG&A (total OpEx) | 43,887 | 51,345 | **54,847** | **+6.8%** |
| OpEx % of revenue | 12.00% | 13.02% | **14.31%** | +129 bps |
| **Operating income** | 108,949 | 119,437 | **114,301** | -4.3% |
| **Operating margin %** | 29.78% | 30.29% | **29.82%** | -47 bps |
| Interest & investment income (net non-operating) | +258 | -334 | **-565** | worsened |
| Interest expense | 2,645 | 2,931 | **3,933** | +34.2% |
| Investment income (interest & dividend) | 2,843 | 2,825 | **3,750** | +32.7% |
| Pre-tax income | 109,207 | 119,103 | **113,736** | -4.5% |
| Income tax expense | 14,527 | 19,300 | **16,741** | -13.3% |
| **Effective tax rate** | 13.3% | 16.2% | **14.7%** | -150 bps |
| **Net income** | 94,680 | 99,803 | **96,995** | **-2.8%** |
| **Net margin %** | 25.88% | 25.31% | **25.31%** | flat |
| **Diluted EPS** | $5.61 | $6.11 | **$6.13** | **+0.3%** |
| Basic EPS | $5.67 | $6.15 | **$6.16** | +0.2% |
| Implied diluted shares | ~16,879M | ~16,334M | **~15,823M** | **-3.1%** |
| Dividends declared per share | $0.85 | $0.90 | **$0.94** | +4.4% |

### Reading the income statement
- **Margin expansion is the standout.** Gross margin rose **+235 bps over two years** (41.8% → 44.1%) *while revenue declined*. Because hardware COGS fell faster than revenue (-4.2% vs -2.8%), the only credible explanation is **mix shift toward higher-margin Services** and/or favorable component costs. This is the highest-quality line in the entire report.
- **Operating leverage has turned negative.** OpEx grew **+6.8%** against **-2.8%** revenue in FY2023 (after +17.0% OpEx growth vs +7.8% revenue in FY2022). This is the classic late-cycle signature: the company keeps investing (R&D for silicon/AI/headset) while the top line stalls. OpEx intensity has risen **231 bps in two years**.
- **EPS is a buyback artifact.** Trailing EPS growth of +8.9% → +0.3% decoupled from net income of +5.4% → -2.8%. Strip out the **-3.1%** share-count reduction and FY2023 EPS would have been ~$5.94 (-2.8%). **Any trailing P/E multiple is being applied to an EPS figure that only holds up because of repurchases.**
- **Tax tailwind:** FY2023's effective rate of 14.7% (vs 16.2%) added roughly **$1.7B / ~$0.11 EPS** — one-time in character (lower foreign rate differential at -$5.74B, plus $1.12B R&D credits). Do not annualize it. Note FY2021 was 13.3%, so rates are volatile; the 21% statutory rate implies sustained offshore benefit.
- **Foreign vs domestic:** FY2023 pre-tax foreign income **$72.9B** vs total pre-tax **$113.7B** — **64% of profit is earned outside the US**, i.e., structurally exposed to FX and international tax regimes.

---

## 4. Balance Sheet — Fortress, Net Cash, Improving Liquidity

| Metric | 2022-09-24 | **2023-09-30** | Change |
|---|---|---|---|
| Cash and cash equivalents | 23,646 | **29,965** | +26.7% |
| Marketable securities – current (derived) | 24,658 | **31,590** | +28.1% |
| Marketable securities – noncurrent (AFS) | n/t | **100,544** | — |
| Restricted marketable securities | 12,700 | **13,800** | +8.7% |
| **Total cash + marketable securities** | — | **≈162,099** | — |
| Accounts receivable | 28,184 | **29,508** | +4.7% |
| Vendor non-trade receivables | 32,748 | **31,477** | -3.9% |
| Inventories | 4,946 | **6,331** | **+28.0%** |
| Other current assets | 21,223 | **14,695** | -30.8% |
| **Total current assets** | 135,405 | **143,566** | +6.0% |
| PP&E, net | 42,117 | **43,715** | +3.8% |
| Other noncurrent assets | 54,428 | **64,758** | +19.0% |
| **Total assets** | 352,755 | **352,583** | flat |
| Accounts payable | 64,115 | **62,611** | -2.3% |
| Current term debt | 11,128 | **9,822** | -11.7% |
| Commercial paper | 9,982 | **5,985** | **-40.0%** |
| Other current liabilities | 60,845 | **58,829** | -3.3% |
| **Total current liabilities** | 153,982 | **145,308** | -5.6% |
| Long-term debt (noncurrent) | 98,959 | **95,281** | -3.7% |
| **Total term debt + CP** | 120,069 | **111,088** | **-7.5%** |
| Operating lease liability | 11,470 | **11,818** | +3.0% |
| **Total liabilities** | 302,083 | **290,437** | -3.8% |
| **Shareholders' equity** | 50,672 | **62,146** | **+22.6%** |
| **Current ratio** | 0.879x | **0.988x** | improving |
| **Debt / equity** | 2.37x | **1.79x** | deleveraging |

### Reading the balance sheet
- **Net cash ≈ $51B** (162.1B liquid vs 111.1B debt, ex-leases). Add back restricted securities and the position is comfortably net cash even including $11.8B of operating leases. Liquidity is not remotely a constraint.
- **Deleveraging is deliberate:** gross debt down **-7.5% ($9.0B)** in FY2023, with **commercial paper cut 40%** — Apple is terming out short paper as rates rose. Debt is exceptionally well-laddered, which materially reduces refinancing risk:
  - Due next 12 months: **$9.94B** (7.6% of term debt)
  - Yr 2: $10.78B | Yr 3: $12.27B | Yr 4: $9.79B | Yr 5: $7.80B
  - **Beyond 5 years: $56.00B (56% of the stack)** — long duration locked in pre-2022, so interest expense (+34% to $3.93B) is a modest, manageable drag.
- **Current ratio improved to 0.988x** from 0.879x — still technically below 1.0, but for Apple this is a *feature* of working-capital efficiency (negative cash conversion cycle: AP of $62.6B vs inventory of $6.3B), not a liquidity stress signal.
- **Inventory +28% is the one yellow flag on this statement.** A 28% build against a 2.8% revenue decline implies either (a) new product ramp (headset, iPhone 15 launch inventory), or (b) channel demand softness. **Check the December-quarter disclosure to distinguish these.**
- **Receivables quality:** AR +4.7% on -2.8% revenue lifts DSO from ~26.1 to ~28.1 days — small but directionally consistent with slower collections. Vendor non-trade receivables fell -3.9% (a *leading* indicator of manufacturing/component purchase volume — mildly cautious).
- **Equity +22.6% to $62.1B** despite $77.6B of buybacks is a striking testament to earnings power; ROE on average equity is **~172%**, one of the highest in large-cap markets.

---

## 5. Cash Flow — The Core of the Investment Case

| Metric | FY2021 | FY2022 | FY2023 | FY23 YoY |
|---|---|---|---|---|
| **Operating cash flow** | 104,038 | 122,151 | **110,543** | **-9.5%** |
| OCF margin (% of revenue) | 28.4% | 31.0% | **28.8%** | -216 bps |
| Capex (PP&E purchases) | 11,085 | 10,708 | **10,959** | +2.3% |
| Capex % of revenue | 3.03% | 2.72% | **2.86%** | +14 bps |
| **Free cash flow** | 92,953 | 111,443 | **99,584** | **-10.6%** |
| **FCF margin** | 25.4% | 28.3% | **26.0%** | -228 bps |
| **Share repurchases** | 85,971 | 89,402 | **77,550** | -13.3% |
| **Dividends paid** | 14,467 | 14,841 | **15,025** | +1.2% |
| SBC tax withholding (net share settlement) | 6,556 | 6,223 | **5,431** | -12.7% |
| **Total shareholder returns (buyback+div)** | 100,438 | 104,243 | **92,575** | -11.2% |
| **Returns as % of FCF** | 108% | 94% | **93%** | — |
| Share-based compensation (non-cash) | 7,906 | 9,038 | **10,833** | **+19.9%** |
| Depreciation & amortization | 11,284 | 11,104 | **11,519** | +3.7% |
| Income taxes paid, net | 25,385 | 19,573 | **18,679** | -4.6% |
| Investing cash flow | -14,545 | -22,354 | **+3,705** | flipped positive |
| Financing cash flow | -93,353 | -110,749 | **-108,488** | — |
| Net change in cash (incl. FX) | -3,860 | -10,952 | **+5,760** | — |

### Reading the cash flow statement
- **Cash generation is decelerating faster than earnings.** OCF -9.5% vs net income -2.8% is a **~670 bps negative divergence** — a genuine quality-of-earnings watch item. Working capital was a drag: other operating liabilities contributed only **+$3.03B** vs **+$6.11B** in FY2022 (accruals normalizing), while AR consumed **$1.69B**.
- **Capital return is running at 93% of FCF** — objectively high, but note it *fell* from 94% and 108%, i.e., Apple quietly **right-sized buybacks down 13.3%** to $77.6B. That is prudent capital discipline, not distress, and leaves ~$7B of annual FCF buffer.
- **SBC +19.9% to $10.83B is the biggest soft spot.** SBC has grown from **2.16% → 2.83% of revenue in two years** — i.e., a portion of that "44% gross margin" and "flat net margin" is being paid for in dilution that the $77.6B buyback exists partly to neutralize. $18.6B of unrecognized SBC remains to be expensed. **Adjust FCF downward if you run a dilution-adjusted model.**
- **Investing turned positive (+$3.70B)** for the first time in three years because Apple **stopped net-adding to its securities portfolio**: purchases of AFS debt collapsed to **$29.5B from $76.9B**, while $39.7B matured and $5.8B were sold. This is a portfolio roll-off, not a business investment signal — capex stayed flat at ~$11.0B (2.9% of revenue), confirming Apple remains **asset-light**.
- **Taxes paid ($18.7B) exceed tax expense ($16.7B)** — cash taxes running hot relative to the P&L, consistent with the one-time nature of the low effective rate (see §3).

---

## 6. Interim Trend — 9M FY2023 vs 9M FY2022 (the most recent intra-year read)

| Metric (nine months ended) | 9M FY2022 (to 2022-06-25) | **9M FY2023 (to 2023-07-01)** | YoY |
|---|---|---|---|
| Operating cash flow | 98,024 | **88,945** | **-9.3%** |
| Investing cash flow | -21,137 | **+1,311** | flipped |
| Financing cash flow | -83,955 | **-85,335** | -1.6% |
| Share repurchases | 64,974 | **56,547** | -13.0% |
| Dividends paid | 11,138 | **11,267** | +1.2% |
| Capex | 7,419 | **8,796** | **+18.6%** |
| AFS debt purchased | 70,178 | **20,956** | -70.1% |

**Derived Q4 FY2023 (quarter ended 2023-09-30)** — annual less 9M:
- OCF **$21.6B** vs Q4 FY2022 **$24.1B** → **-10.5%**
- Capex **$2.2B**; Buybacks **$21.0B**; Dividends **$3.8B**
- Investing **+$2.4B**; Financing **-$23.2B**

**Derived Q1 FY2023 (December 2022 quarter, from 10-Q accepted 2023-02-03)** — the most recent December-quarter comparable:
- OCF **$34.0B** vs Q1 FY2022 **$47.0B** → **-27.6%**
- Investing -$1.4B; Financing -$35.6B

**Interpretation:** the December quarter is Apple's largest and most seasonally important. The **-27.6% OCF collapse in Q1 FY2023** was the single worst interim data point in the set — a supply-constrained/soft-demand quarter. Base effects for the upcoming December-quarter comparison are therefore **easy on cash flow** but the *trend* of -9% to -10% OCF decline across Q4 FY2023 and 9M FY2023 says the recovery is not yet visible in the hard data. **Capex +18.6% year-over-year through 9M is the one genuinely expansionary signal in the interim data.**

---

## 7. Profitability, Efficiency & Quality Scorecard

| Metric | FY2021 | FY2022 | FY2023 | Assessment |
|---|---|---|---|---|
| Gross margin | 41.78% | 43.31% | 44.13% | **Improving — best in set** |
| Operating margin | 29.78% | 30.29% | 29.82% | Stable, high |
| Net margin | 25.88% | 25.31% | 25.31% | Stable, high |
| ROE (avg equity) | — | ~203% | **~172%** | Exceptional |
| OCF / net income | 1.10x | 1.22x | **1.14x** | Healthy accrual quality |
| FCF / net income | 0.98x | 1.12x | **1.03x** | Healthy |
| Capex intensity | 3.03% | 2.72% | **2.86%** | Asset-light |
| SBC / revenue | 2.16% | 2.29% | **2.83%** | **Deteriorating** |
| Effective tax rate | 13.3% | 16.2% | **14.7%** | Volatile, beneficial |
| Net cash | — | ≈ low | **≈$51B** | Fortress |
| FCF per share | $5.51 | $6.82 | **$6.40** | -6.2% |
| Book value per share | — | $3.18 | **$4.00** | +25.8% |

---

## 8. Insider Transactions

**DATA UNAVAILABLE — no conclusion possible.** The authorized point-in-time archive contains no insider-transaction (Form 4) records for AAPL as of 2024-01-09. Per data-integrity rules, **no inference about insider buying or selling is drawn or should be drawn from this report.** If insider signal is required for the trade decision, it must be sourced separately; treat any third-party claim of specific insider activity as unverified against this toolset.

---

## 9. Valuation Framework (price-dependent — no quote in this toolset)

I cannot compute P/E, EV/EBITDA, or FCF yield because **no share price is available in this data package.** The trader should apply their own quote to these anchors:

| Anchor (FY2023, diluted) | Value |
|---|---|
| Diluted EPS | **$6.13** |
| FCF per share | **$6.40** |
| Book value per share | **$4.00** |
| Dividends per share | **$0.94** (payout ~15%) |
| Diluted shares | ~15,823M (15,552.8M at 2023-10-20) |

**Rules of thumb to apply:**
- `P/E = Price ÷ $6.13` → at $180 = **29.4x**; at $195 = **31.8x**; at $150 = **24.5x**
- `FCF yield = $6.40 ÷ Price` → at $180 = **3.56%**; at $150 = **4.27%**
- `EV = Market cap ÷ 1,000 × Price − ~$51B net cash` (net cash *reduces* EV below market cap)
- `EV/FCF ≈ (Market cap − $51B) ÷ $99.6B`
- **Consensus 10-yr Treasury comparison is essential** given the 3.5% FCF yield implied — the duration/quality premium is the entire bull case.

**Critical caveat:** because EPS growth is now buyback-driven (§3), trailing P/E is *understated* relative to economic earnings growth. The correct lens is **EV/FCF and organic revenue growth**, not P/E. On this data, a multiple north of ~28x FCF requires the market to price **re-acceleration in Services/hardware that has not yet appeared in the filings.**

---

## 10. Risks & Catalysts

**Fundamental risks (evidenced by the data):**
1. **Revenue contraction:** -2.8% in FY2023 after +7.8% in FY2022 — the growth engine has stalled at $383B.
2. **Negative operating leverage:** OpEx +6.8% vs revenue -2.8%; OpEx intensity +231 bps in two years. If revenue doesn't inflect, margins compress from here.
3. **EPS quality:** +0.3% EPS on -2.8% net income means **any slowdown in buyback capacity mechanically stalls EPS growth**. Returns are already 93% of FCF.
4. **Cash-flow deceleration:** OCF -9.5% FY2023, -9.3% 9M, -10.5% in derived Q4 — three consecutive negative reads.
5. **Tax rate mean-reversion:** 14.7% vs 21% statutory; a normalization to FY2022's 16.2% would have cut FY2023 EPS by roughly **$0.10–0.11**.
6. **SBC creep:** +19.9% to $10.83B, $18.6B still unrecognized — understated dilution.
7. **Inventory build:** +28% against falling revenue; refine with the next 10-Q.
8. **Concentration:** 64% of pre-tax profit is foreign — FX and international tax/regulatory exposure.
9. **Balance-sheet optics:** current ratio 0.988x — not a risk for Apple, but screens poorly.

**Catalysts to monitor (not yet in the data set):**
- **Q1 FY2024 (December-quarter) results — not filed as of 2024-01-09.** Apple has historically reported this quarter in late January/early February. This is the **dominant near-term event**: it resets the OCF-decline narrative, clarifies the inventory build, and is compared against an easy Q1 FY2023 base (OCF -27.6%).
- Any new buyback authorization (FY2023 program and remaining capacity are not disclosed in this tag set).
- Trend in SBC as % of revenue and in the effective tax rate.
- Whether investing cash flow stays positive (securities roll-off) — a signal of portfolio maturity, not strategy.

---

## 11. Actionable Insights for Traders

1. **Own it for quality, not growth.** The evidence supports a defensive, cash-return-driven position: 44.1% gross margin, 26% FCF margin, $51B net cash, 172% ROE. Nothing in these filings supports paying for re-acceleration yet.
2. **Do not extrapolate the FY2023 EPS beat.** $6.13 was manufactured by a 3.1% share-count cut and a one-time 14.7% tax rate. Underlying net income **fell 2.8%**. Model FY2024 EPS growth as modest-positive only if buybacks continue near $78B.
3. **Watch OCF, not EPS, as your primary signal.** FY2023 OCF -9.5%, 9M -9.3%, Q4 -10.5%. **A return to positive OCF growth in the December-quarter filing is the fundamental trigger to add; another negative print confirms deceleration and argues for trimming.**
4. **The balance sheet gives management enormous optionality** — $51B net cash plus $99.6B annual FCF funds either a larger buyback, M&A, or a dividend step-up. Any of these is an upside catalyst not currently in the reported numbers.
5. **Margin defensibility is the bull case.** Gross margin rose 235 bps in two years *while revenue fell* — that is pricing power plus Services mix. If the next 10-Q shows gross margin ≥44%, the quality thesis is intact regardless of the revenue line.
6. **Use negative sentiment around the revenue decline as an entry mechanism, but demand a valuation cushion.** With a ~3.5% FCF yield at $180 and flat-to-down organic earnings, you are paying a premium for certainty. Size accordingly.
7. **Explicit data gaps to fill before trading:** (a) current price and consensus estimates, (b) insider Form 4 activity (§8 unavailable), (c) segment/product revenue mix, (d) the Q1 FY2024 filing. This report covers fundamentals only — it is **not** a complete trade thesis.

---

## 12. Key Points Summary Table

| Category | Metric | FY2021 | FY2022 | FY2023 | Signal |
|---|---|---|---|---|---|
| **Scale** | Revenue ($M, derived) | 365,817 | 394,328 | **383,285** | **Contraction -2.8%** |
| **Growth** | Revenue YoY | +33.3% | +7.8% | **-2.8%** | Stalled |
| **Profitability** | Gross margin | 41.78% | 43.31% | **44.13%** | ✅ Best in set |
| **Profitability** | Operating margin | 29.78% | 30.29% | **29.82%** | ➖ Flat/high |
| **Profitability** | Net margin | 25.88% | 25.31% | **25.31%** | ➖ Flat |
| **Earnings** | Net income ($M) | 94,680 | 99,803 | **96,995** | **-2.8%** |
| **Earnings** | Diluted EPS | $5.61 | $6.11 | **$6.13** | ⚠️ Buyback-driven |
| **Earnings** | Diluted shares (implied, M) | ~16,879 | ~16,334 | **~15,823** | -3.1% |
| **Costs** | OpEx ($M) | 43,887 | 51,345 | **54,847** | ⚠️ +6.8% vs rev -2.8% |
| **Costs** | OpEx % of revenue | 12.00% | 13.02% | **14.31%** | ⚠️ Negative leverage |
| **Tax** | Effective tax rate | 13.3% | 16.2% | **14.7%** | ⚠️ One-time benefit |
| **Cash** | Operating cash flow ($M) | 104,038 | 122,151 | **110,543** | ⚠️ **-9.5%** |
| **Cash** | Capex ($M) | 11,085 | 10,708 | **10,959** | Asset-light (2.9% rev) |
| **Cash** | Free cash flow ($M) | 92,953 | 111,443 | **99,584** | **-10.6%** |
| **Cash** | FCF margin | 25.4% | 28.3% | **26.0%** | ➖ High, declining |
| **Returns** | Buybacks ($M) | 85,971 | 89,402 | **77,550** | -13.3% (disciplined) |
| **Returns** | Dividends ($M) | 14,467 | 14,841 | **15,025** | +1.2% |
| **Returns** | Total return / FCF | 108% | 94% | **93%** | ⚠️ High but sustainable |
| **Returns** | DPS declared | $0.85 | $0.90 | **$0.94** | ✅ 15% payout |
| **Dilution** | SBC ($M) | 7,906 | 9,038 | **10,833** | ⚠️ **+19.9%** |
| **Dilution** | SBC % of revenue | 2.16% | 2.29% | **2.83%** | ⚠️ Rising |
| **Liquidity** | Cash + securities ($M) | — | — | **≈162,099** | ✅ Fortress |
| **Leverage** | Total debt + CP ($M) | — | 120,069 | **111,088** | ✅ **-7.5%** |
| **Leverage** | Net cash ($M) | — | — | **≈51,000** | ✅ Net cash |
| **Leverage** | Debt / equity | — | 2.37x | **1.79x** | ✅ Deleveraging |
| **Leverage** | Current ratio | — | 0.879x | **0.988x** | ➖ Still <1.0 |
| **Leverage** | Debt due >5 yrs | — | — | **$56.0B (56%)** | ✅ Well-laddered |
| **Working cap** | Inventory ($M) | — | 4,946 | **6,331** | ⚠️ **+28%** |
| **Working cap** | DSO (approx. days) | — | 26.1 | **28.1** | ⚠️ Slight slip |
| **Equity** | Shareholders' equity ($M) | — | 50,672 | **62,146** | ✅ +22.6% |
| **Equity** | ROE (avg) | — | ~203% | **~172%** | ✅ Exceptional |
| **Interim** | OCF, 9M YoY | — | — | **-9.3%** | ⚠️ Confirms trend |
| **Interim** | Derived Q4 OCF YoY | — | — | **-10.5%** | ⚠️ Confirms trend |
| **Per share** | FCF per share | $5.51 | $6.82 | **$6.40** | -6.2% |
| **Per share** | Book value per share | — | $3.18 | **$4.00** | +25.8% |
| **Valuation** | P/E | n/a — **no price in toolset** | | **= Price ÷ $6.13** | Apply own quote |
| **Valuation** | FCF yield | n/a — **no price in toolset** | | **= $6.40 ÷ Price** | Apply own quote |
| **Insider** | Form 4 activity | **DATA UNAVAILABLE — no inference drawn** | | | ⛔ Gap |
| **Next event** | Q1 FY2024 results | **Not filed as of 2024-01-09** (last filing 2023-11-03) | | | 🔔 Key catalyst |

**Bottom line:** **AAPL** presents a fortress balance sheet, best-in-cycle gross margins, and near-100% FCF conversion — undermined by a **-2.8% revenue decline, negative operating leverage, buyback-dependent EPS, and a -9.5% operating cash-flow decline**. Fundamentals justify **holding/accumulating on weakness for quality and capital return**, not chasing for growth. The December-quarter filing is the decisive near-term datapoint, and **insider-transaction and price data are absent from this toolset and must be sourced before execution.**