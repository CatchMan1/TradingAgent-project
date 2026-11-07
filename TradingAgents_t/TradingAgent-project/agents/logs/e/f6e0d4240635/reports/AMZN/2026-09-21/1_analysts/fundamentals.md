# AMZN — Fundamental Research Report
**Amazon.com, Inc. (NASDAQ: AMZN)**
**As-of date:** 2026-09-21 | **Latest filed period:** Q2 2026 (10-Q filed 2026-07-31) | **Currency:** USD

---

## 0. Data Provenance & Caveats (read first)

This report is built **exclusively from point-in-time SEC XBRL facts** available by 2026-09-21 (B-project cache, accession `0001018724-26-000026` for Q2 FY2026, `0001018724-26-000014` for Q1 FY2026).

| Limitation | Impact |
|---|---|
| Only **two balance-sheet dates** in cache (2025-12-31, 2026-06-30) | No multi-year balance-sheet trend |
| Only **H1/Q2 FY2026 vs H1/Q2 FY2025** income data | No FY2022–FY2025 full-year statements were returned; annual requests returned the same quarterly shard |
| Revenue tag (`Revenues`) not in extract | Revenue **derived** as `CostsAndExpenses + OperatingIncomeLoss` (arithmetic identity, reliable) |
| No price/market-cap data | **No P/E, EV/EBITDA, or price target** is presented — I will not fabricate them |
| Insider transactions | **DATA_UNAVAILABLE** — no authorized archive for AMZN by 2026-09-21. No insider activity is inferred or fabricated anywhere in this report. |

---

## 1. Company Profile

Amazon.com, Inc. is a global technology and e-commerce conglomerate. The Q2 FY2026 filing confirms **3 reportable operating segments** (`NumberOfOperatingSegments = 3`), consistent with its long-standing structure:

1. **North America** — online stores, physical stores, third-party seller services (1P + 3P marketplace), Prime subscriptions, advertising.
2. **International** — same commerce stack across non-US geographies.
3. **Amazon Web Services (AWS)** — cloud infrastructure, database, analytics, AI/ML compute and platform services.

**Economic engine (as evidenced by the numbers in this filing):**
- Very high **gross margin (52.3% in Q2 FY2026)** despite a low-margin retail base → the mix is increasingly weighted to 3P fees, advertising, and AWS.
- Enormous **negative working-capital cycle** (DPO ~140 days vs DSO ~40 days, computed below) → structural, interest-free funding.
- A business now being re-tooled around **AI infrastructure**: capex is running at **27% of revenue**, debt has roughly doubled, and **$650B of contractual obligations** sit on the balance sheet.

---

## 2. Q2 & H1 FY2026 Income Statement (derived where necessary)

| Metric ($M) | Q2 FY2026 | Q2 FY2025 | YoY | H1 FY2026 | H1 FY2025 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| **Revenue** (derived) | **200,606** | 167,702 | **+19.6%** | **382,125** | 323,369 | **+18.2%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 183,241 | 157,785 | +16.1% |
| **Gross profit** | **104,828** | 86,893 | **+20.6%** | **198,884** | 165,584 | **+20.1%** |
| Gross margin | **52.26%** | 51.81% | +45 bps | **52.05%** | 51.21% | +84 bps |
| Marketing | 11,698 | 11,416 | +2.5% | 22,012 | 21,179 | +3.9% |
| G&A | 2,788 | 2,965 | −6.0% | 5,375 | 5,593 | −3.9% |
| Other operating costs (fulfillment, tech/content) — implied | 62,881 | 53,341 | +17.9% | 120,184 | 101,236 | +18.7% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** | **51,313** | 37,576 | **+36.6%** |
| **Operating margin** | **13.69%** | 11.43% | **+226 bps** | **13.43%** | 11.62% | **+181 bps** |
| Interest income | 1,295 | 1,085 | +19.4% | 2,430 | 2,151 | +13.0% |
| Interest expense | (1,314) | (516) | **+154.7%** | (2,114) | (1,057) | **+100.0%** |
| Non-operating income/(expense), net | **53,396** | 1,686 | n.m. | **69,378** | 4,960 | n.m. |
| Pre-tax income | 80,857 | 20,857 | +287.7% | 120,691 | 42,536 | +183.7% |
| Tax expense | 18,199 | 2,678 | +579.6% | 27,759 | 7,231 | +283.9% |
| Effective tax rate | 22.5% | 12.8% | — | 23.0% | 17.0% | — |
| **Net income** | **62,647** | 18,164 | **+244.9%** | **92,902** | 35,291 | **+163.2%** |
| Diluted EPS | **$5.75** | $1.68 | +242.3% | **$8.53** | $3.27 | +160.9% |
| Diluted shares (derived) | ~10,895 | ~10,812 | +0.8% | ~10,891 | ~10,793 | +0.9% |

### Q1 FY2026 (derived by subtraction — H1 less Q2)

| Metric ($M) | Q1 FY2026 | Q1 FY2025 | YoY |
|---|---:|---:|---:|
| Revenue | 181,519 | 155,667 | +16.6% |
| Gross profit | 94,056 | 78,691 | +19.5% |
| Gross margin | **51.82%** | 50.55% | +127 bps |
| Operating income | 23,852 | 18,405 | +29.6% |
| Operating margin | **13.14%** | 11.82% | +132 bps |
| Pre-tax income | 39,834 | 21,679 | +83.7% |
| Net income | 30,255 | 17,127 | +76.7% |
| Diluted EPS | $2.78 | $1.59 | +74.8% |

### Key operating observations
- **Revenue acceleration:** +16.6% (Q1) → **+19.6% (Q2)**. Sequential acceleration of ~300 bps into Q2 is a genuinely bullish operating signal for a company at a >$800B revenue run-rate ($802B annualized on Q2).
- **Margin expansion is gross-margin-led, not cost-cutting-led.** Other operating costs grew 17.9% (slightly *below* revenue growth) and marketing grew only 2.5% — i.e., **~1,000 bps of operating leverage vs. revenue in marketing**. But nearly all of the 226 bps of Q2 operating-margin expansion came from gross margin (+45 bps) plus marketing/G&A leverage (~115 bps).
- **SBC discipline:** $6,038M in Q2 FY2026 vs. $6,534M (−7.6%); H1 $10,070M vs. $10,223M (−1.5%), or **2.6% of revenue**. Unrecognized future SBC of $24.8B.
- **Interest expense has doubled** (+100% H1, +155% Q2) and will keep climbing given the debt issued (see §5). It is still trivial versus operating income (~5% of Q2 OI), but the trend line matters.

---

## 3. ⚠️ Earnings Quality — The Single Most Important Fact in This Report

**Reported EPS massively overstates recurring earnings power.**

The filing discloses a **$62,814M upward revaluation** of equity securities **without readily determinable fair value** in H1 FY2026, of which **$50,486M hit in Q2 alone**. Correspondingly:

| Item ($M) | 2025-12-31 | 2026-06-30 | Change |
|---|---:|---:|---:|
| Equity securities w/o readily determinable FV | **16,200** | **122,300** | **+$106.1B (+655%)** |
| Upward price adjustments, H1 FY2026 | — | **62,814** | (Q2: 50,486) |
| Upward price adjustments, H1 FY2025 | 86 | — | — |

This is a **non-cash, mark-to-model revaluation of a private equity holding** — not operating profit. It is booked in `NonoperatingIncomeExpense`, and it is **tax-deferred** (see §6).

### Normalized (ex-revaluation) results

| Metric | Q2 FY2026 reported | Less $50,486M pre-tax gain (at 22.5% tax) | **Q2 FY2026 core** | Q2 FY2025 | Core YoY |
|---|---:|---:|---:|---:|---:|
| Pre-tax income | 80,857 | (50,486) | **30,371** | 20,857 | **+45.6%** |
| Net income | 62,647 | (39,127) | **23,520** | 18,164 | **+29.5%** |
| Diluted EPS | **$5.75** | (~$3.59) | **~$2.16** | $1.68 | **+28.6%** |
| Net margin | 31.2% | — | **11.7%** | 10.8% | +90 bps |

| Metric | H1 FY2026 reported | Less $62,814M pre-tax gain (at 23%) | **H1 FY2026 core** | H1 FY2025 | Core YoY |
|---|---:|---:|---:|---:|---:|
| Pre-tax income | 120,691 | (62,814) | **57,877** | 42,536 | **+36.1%** |
| Net income | 92,902 | (48,367) | **44,535** | 35,291 | **+26.2%** |
| Diluted EPS | **$8.53** | (~$4.44) | **~$4.09** | $3.27 | **+25.1%** |

| TTM (Jul-2025 → Jun-2026) | Reported | Normalized |
|---|---:|---:|
| Net income | $135,281M | **~$86,914M** |
| Diluted EPS (on ~10,891M sh) | **$12.42** | **~$7.98** |
| **Overstatement** | — | **+$4.44/sh (+56%)** |

**Actionable conclusion:** any screen or headline multiple computed on AMZN's reported TTM EPS ($12.42) is **~36% too cheap** on a P/E basis versus normalized EPS (~$7.98). Conversely, core EPS growth of **+25% to +29%** is a better representation of the franchise trajectory and is still best-in-class at this scale.

**Second-order risk:** the $122.3B non-marketable equity position now equals **~11% of total assets** and is carried at a valuation that just increased 7.5x in six months. A reversal (private-market markdown, IPO repricing) would create a **multi-tens-of-billions GAAP earnings air pocket** with no cash impact — a classic source of headline-EPS volatility and multiple compression.

---

## 4. Balance Sheet (2026-06-30 vs. 2025-12-31)

| $M | 2026-06-30 | 2025-12-31 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 78,213 | 86,810 | −9.9% |
| Available-for-sale debt securities | 97,900 | 45,800 | **+113.8%** |
| **Total cash + marketable securities** | **176,113** | 132,610 | **+32.8%** |
| Accounts receivable, net | 88,092 | 67,729 | **+30.1%** |
| Inventory, net | 38,184 | 38,325 | −0.4% |
| **Total current assets** | **249,264** | 229,083 | +8.8% |
| **Total assets** | **1,095,689** | 818,042 | **+33.9%** |
| Accounts payable | 147,440 | 121,909 | +20.9% |
| Accrued liabilities | 73,406 | 75,520 | −2.8% |
| **Total current liabilities** | **241,274** | 218,005 | +10.7% |
| Long-term debt (incl. current portion) | **132,995** | 68,836 | **+93.2%** |
| — of which current | 3,330 | 2,748 | +21.2% |
| — of which non-current | 128,894 | 65,648 | +96.3% |
| Finance lease liabilities | 13,451 | 12,286 | +9.5% |
| Operating lease liabilities | 96,320 | 89,252 | +7.9% |
| Deferred revenue (current + non-current) | 24,928 | 24,976 | flat |
| AOCI | 66,287 | 28,230 | **+$38.1B** |

### Liquidity & leverage read
| Ratio | 2026-06-30 |
|---|---:|
| Current ratio | **1.033x** (249,264 / 241,274) |
| Quick ratio | **0.875x** ((249,264 − 38,184) / 241,274) |
| Cash + securities / current liabilities | **0.73x** |
| Gross debt (LT debt + finance leases) | **$146.4B** |
| Net debt (gross debt − cash − securities) | **−$29.7B → net cash** |
| Net debt excluding securities | **+$55.3B** |
| **Debt increase in 6 months** | **+$64.2B** |

**Interpretation:** liquidity is comfortable — **$96.5B of the $97.9B securities portfolio matures within one year**, so it is effectively cash. But the *direction* is unmistakable: Amazon added **$64B of debt in six months** and issued **$67.0B of long-term debt in H1** ($82B over the trailing year) to fund capex and M&A. Net cash of ~$30B is thin relative to a **$650B contractual-obligation book** and a ~$217B annualized capex run-rate.

### Working-capital efficiency (Q2 FY2026 annualized)
| Metric | Calculation | Result |
|---|---|---:|
| Days sales outstanding | 88,092 / 200,606 × 91 | **40.0 days** |
| Days inventory outstanding | 38,184 / 95,778 × 91 | **36.3 days** |
| Days payable outstanding | 147,440 / 95,778 × 91 | **140.1 days** |
| **Cash conversion cycle** | 40.0 + 36.3 − 140.1 | **−63.8 days** |

A ~64-day negative cash-conversion cycle is the structural moat that lets Amazon fund inventory with suppliers' money. **Watch AP (+20.9%) growing slower than AR (+30.1%)** — if that reverses, the working-capital tailwind that flatters operating cash flow shrinks.

### Hidden balance-sheet items traders should monitor
- **AOCI +$38.1B in H1 FY2026** (from $28.2B to $66.3B), while FX translation was only **−$1.56B**. The remainder (~+$39.6B) is unrealized investment/securities-related and is *not* in net income. It inflates book value without cash generation. (Note the disclosed AFS unrealized gain is only $7M, so the bulk of this OCI is not from the liquid bond portfolio — flag for the 10-Q footnotes.)
- **Purchase/contractual obligations of $650,034M**, with **$78,084M due within 12 months**, $53,406M in year 2, $46,767M in year 3, $42,219M in year 4, and **~$387B beyond year 4**. This is the clearest quantitative fingerprint of multi-year AI compute/chip/content commitments. It is an off-balance-sheet claim senior in practical priority to buybacks.

---

## 5. Cash Flow & Capex — The Bear Case Lives Here

| $M | Q2 FY2026 | Q2 FY2025 | H1 FY2026 | H1 FY2025 | TTM Jun-26 | TTM Jun-25 |
|---|---:|---:|---:|---:|---:|---:|
| **Operating cash flow** | **45,387** | 32,515 | **71,419** | 49,530 | **161,403** | 121,137 |
| Capex (productive assets) | **(54,208)** | (32,183) | **(98,411)** | (57,202) | **(173,028)** | (107,656) |
| **Free cash flow** | **(8,821)** | **+332** | **(26,992)** | (7,672) | **(11,625)** | **+13,481** |
| Acquisitions of businesses | (24,359) | (1,700) | **(39,767)** | (1,652) | (41,956) | (4,809) |
| Purchases of marketable securities | (26,006) | (17,797) | (49,262) | (31,130) | (72,902) | (46,731) |
| Proceeds from sale/maturity of securities | 24,196 | 11,441 | 41,882 | 19,178 | 67,090 | 30,924 |
| Net investing cash flow | (79,245) | (39,424) | (143,457) | (69,227) | (216,775) | (123,569) |
| LT debt issued | 13,557 | 0 | **66,998** | 746 | **81,925** | 746 |
| ST debt, net | (205) | +701 | (296) | +436 | +164 | +286 |
| Net financing cash flow | +10,146 | (2,539) | **+62,913** | (2,586) | **+75,160** | (8,652) |
| Net change in cash | (23,765) | (8,440) | (9,179) | (20,859) | +19,474 | (10,220) |

### The three numbers that define the current setup

1. **Capex is 27.0% of revenue** (Q2: $54,208M / $200,606M) vs. 19.2% a year ago. H1 capex **+72% YoY**. Trailing capex **$173.0B**.
2. **FCF is negative on every measure**: −$8.8B (Q2), −$27.0B (H1), **−$11.6B (TTM)** — a **$25.1B YoY swing** from +$13.5B.
3. **Capex now exceeds adjusted EBITDA.** Q2 FY2026: OI $27,461M + D&A $19,988M + SBC $6,038M = **$53,487M adj. EBITDA**, versus **$54,208M capex → capex = 101% of adj. EBITDA** (Q2 FY2025: 79%). Annualized, that is ~$214B of EBITDA against ~$217B of capex. **Amazon is currently investing 100% of its pre-tax, pre-interest cash generation.**

### Cash-flow quality flag (important)
**Deferred income tax expense** was **$30,489M in H1 FY2026** vs. **$518M in H1 FY2025** (Q2: $17,691M vs. $11M); TTM **$41,441M**. Cash taxes paid actually *fell* to **$3,978M** (H1) from $5,638M. Because deferred tax is a **non-cash add-back in operating cash flow**, a large part of the $41.4B TTM deferred-tax add-back is the mirror image of the non-cash investment revaluation that was *excluded* from OCF. 

> **Deferred-tax-adjusted TTM OCF ≈ $161,403M − $41,441M ≈ $120.0B**, and **adjusted TTM FCF ≈ −$53.0B.** Operating cash flow is not fabricated, but it is **materially flattered** by a non-cash tax item tied to a paper gain. Traders should not extrapolate the +33% OCF growth at face value.

### Depreciation ramp = the coming margin headwind
D&A rose **+29%** TTM ($75,200M vs. $58,562M) and **+31%** in Q2 ($19,988M vs. $15,227M). With capex at 27% of revenue, D&A growth will *accelerate* for several quarters. **The 13.7% operating margin is likely a peak-ish level, not a floor**, unless gross margin keeps expanding fast enough to offset it. This is the key debate for the next 2–4 quarters.

---

## 6. Segment & Revenue-Mix Intelligence (and its limits)

The filing confirms **3 operating segments** but the point-in-time extract does **not** include the segment revenue/operating-income table. What can be inferred with confidence:

| Inference | Evidence |
|---|---|
| Mix shift toward high-margin revenue (AWS/ads/3P) | Gross margin +84 bps H1 YoY to 52.05%, while total COGS grew 16.1% vs. revenue +18.2% |
| Retail/fulfillment costs scaling sub-linearly | "Other operating costs" +18.7% H1 vs. revenue +18.2%; Q2 +17.9% vs. +19.6% |
| Advertising/Prime monetization strong | Marketing spend up only **2.5%** in Q2 while revenue rose 19.6% — demand-pull, not spend-pull |
| AWS capex intensity is the swing factor | Capex +72% H1 with only ~19% revenue growth; the delta is infrastructure |
| Deferred revenue flat at ~$25.0B | Backlog/committed revenue growth is NOT visible in deferred revenue; the growth is in the **$650B contractual obligation** line instead |

**Note:** $15.2B of the $25.0B deferred revenue balance was recognized as revenue in H1 FY2026, indicating a healthy ~7-month average duration of prepaid/committed balances.

---

## 7. Insider Transactions

**Not available.** The data package returned: *"no authorized, point-in-time insider-transactions archive for AMZN by 2026-09-21."*

I will not infer, estimate, or fabricate insider buying/selling. **Treat insider signal as neutral/unknown** for this analysis. The only ownership-adjacent hard fact available is share count: **10,783M shares outstanding at 2026-06-30** (10,786.3M as of 2026-07-22), up **+0.5%** from 10,731M at 2025-12-31 — i.e., **net dilution, no evidence of a debt-funded buyback**. Capital is going to capex, M&A, and equity stakes, not repurchases.

---

## 8. Synthesis: What the Fundamentals Are Actually Saying

### Bull case (well-supported by the data)
- **Revenue re-accelerated to +19.6%** at a $200.6B quarterly base — rare and powerful at this scale.
- **Operating income +43% YoY**, margin +226 bps to 13.69%; H1 OI +36.6%. This is real operating leverage, not accounting.
- **Gross margin +84 bps H1 / +45 bps Q2**, with marketing up only 2.5% and G&A down 6% — evidence of advertising/AWS/3P mix shift.
- **Core EPS +25–29% YoY** even after stripping the one-time gain.
- **$176B of liquidity**, net-cash position, and a **−64 day cash conversion cycle**.
- A **$122.3B stake portfolio** (from $16.2B) that has already produced $62.8B of paper gains — optionality on the AI ecosystem, and a source of future liquidity.

### Bear case (also well-supported)
- **Negative FCF**: −$11.6B TTM, −$27.0B H1. Capex is **101% of adjusted EBITDA**.
- **Debt +$93% in six months** to $133.0B; **$82B issued TTM**. Net cash is only ~$30B against **$650B of contractual obligations**.
- **Reported EPS is 56% above normalized EPS** ($12.42 vs. ~$7.98 TTM), and the gap is a single private-asset mark.
- **OCF quality**: $41.4B TTM deferred-tax add-back means adjusted FCF is closer to **−$53B**.
- **D&A +29–31% and accelerating** → operating-margin compression risk over the next 2–4 quarters.
- **No buyback, +0.5% dilution**, and interest expense up 100–155% YoY.
- **$39.8B of cash M&A in H1** plus $24.4B in Q2 alone — integration and capital-allocation risk at exactly the moment free cash flow is negative.

### The central tension for a trader
Amazon is simultaneously delivering **best-in-class operating momentum (+43% OI growth)** and **its worst cash-flow profile in years (−$11.6B FCF, 27% capex/revenue, debt doubling)**. Historically, the market has rewarded Amazon for exactly this trade-off — sacrificing near-term FCF for a larger future profit pool. The **risk is different this cycle**: the funding is now **debt**, the commitments are **$650B**, and the earnings beat is **partly a private-market mark**. That combination means the stock is likely to trade on **capex guidance and AWS/AI revenue disclosure**, not on the GAAP EPS print.

---

## 9. Actionable Insights for Traders

| # | Insight | Evidence | Action |
|---|---|---|---|
| 1 | **Do not use reported TTM EPS ($12.42).** Normalize to **~$7.98** (~$4.44/sh of the TTM figure is a non-cash private-stake mark). | `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment` $62,814M H1-26 | Re-run any valuation screen on normalized EPS; the stock is ~56% more expensive than headline multiples imply. |
| 2 | **Core growth is genuinely strong — buy the operations, not the print.** | Core EPS +28.6% Q2, +25.1% H1; OI +43.2% Q2 | Favor owning AMZN over peers on operating momentum; size positions on core EPS beats/misses, which are cleaner signals than GAAP. |
| 3 | **Capex is the swing factor.** 27.0% of revenue in Q2 (vs 19.2%), capex = 101% of adj. EBITDA. | `PaymentsToAcquireProductiveAssets` $54,208M Q2 / $98,411M H1 | Any guidance **increase** in capex without matching AWS revenue acceleration should be traded as a negative; a **capex plateau** with revenue +19% is the bull trigger. |
| 4 | **FCF is negative and under-reported.** Adjusted TTM FCF ≈ **−$53B** after removing the $41.4B deferred-tax add-back. | OCF $161.4B − deferred tax $41.4B − capex $173.0B | Use adjusted FCF, not reported OCF (+33% YoY), for quality-of-earnings work. |
| 5 | **Leverage is the new risk factor.** Debt +93% to $133.0B; $82B issued TTM; net cash only ~$30B. | `LongTermDebt` $132,995M; `ProceedsFromIssuanceOfLongTermDebt` $81,925M TTM | Watch credit spreads and any further large issuance; rising rates now hit a company that just relevered. Interest expense already +155% YoY. |
| 6 | **Margin peak risk from D&A.** D&A +31% Q2, and 27% capex intensity guarantees acceleration. | `DepreciationDepletionAndAmortization` $19,988M Q2 | Expect 2027 operating-margin compression vs. the 13.7% Q2 level; fade margin-expansion extrapolations. |
| 7 | **Balance-sheet optionality is real but illiquid.** $122.3B non-marketable equity + $176B cash/securities. | Balance sheet 2026-06-30 | Optionality supports the equity; but the same $122.3B is a **volatility source** if private marks reset. |
| 8 | **$650B of commitments caps capital returns.** $78.1B due within 12 months; ~$387B beyond year 4. | `ContractualObligation` $650,034M | Do not model meaningful buybacks; +0.5% share growth confirms this. Dividend/buyback catalysts are low-probability. |
| 9 | **Working capital is a hidden asset — monitor it.** CCC ≈ −64 days (DPO 140 vs DSO 40). | Derived from AR/Inventory/AP and Q2 COGS | A rise in DSO or fall in DPO would remove an OCF tailwind precisely when FCF is already negative. Early warning indicator. |
| 10 | **Insider data unavailable — do not read a signal.** | Tool returned DATA_UNAVAILABLE | Treat as neutral; rely on 13F/Form 4 directly if required. |

### What would change the thesis
- **Bull confirmation:** Q3 revenue ≥ +18%, operating margin ≥ 13%, capex guidance held flat or lowered, and AWS growth re-accelerating above 25%.
- **Bear confirmation:** capex guidance raised again, another $40B+ debt raise, a markdown in the $122.3B private-equity book, or D&A growth outpacing gross profit growth for two consecutive quarters.
- **Neutral/ambiguous:** continued GAAP EPS beats driven by further upward revaluations — treat as **non-events** for valuation.

---

## 10. Summary Table — Key Fundamentals at a Glance

| Category | Metric | Value | YoY / Change | Signal |
|---|---|---:|---:|---|
| **Scale** | Q2 FY2026 revenue (derived) | $200,606M | **+19.6%** | 🟢 Strong, accelerating |
| **Scale** | H1 FY2026 revenue | $382,125M | +18.2% | 🟢 |
| **Growth** | Q1 → Q2 revenue growth | 16.6% → 19.6% | +300 bps seq. | 🟢 Acceleration |
| **Profitability** | Q2 operating income | $27,461M | **+43.2%** | 🟢 |
| **Profitability** | Q2 operating margin | **13.69%** | +226 bps | 🟢 |
| **Profitability** | H1 operating margin | 13.43% | +181 bps | 🟢 |
| **Profitability** | Q2 gross margin | **52.26%** | +45 bps | 🟢 |
| **Reported EPS** | Q2 diluted EPS | **$5.75** | +242% | 🔴 Low quality |
| **Reported EPS** | H1 diluted EPS | **$8.53** | +161% | 🔴 Low quality |
| **Reported EPS** | TTM diluted EPS | **$12.42** | — | 🔴 Inflated |
| **Core EPS** | Q2 normalized EPS | **~$2.16** | **+28.6%** | 🟢 Genuine |
| **Core EPS** | H1 normalized EPS | **~$4.09** | +25.1% | 🟢 Genuine |
| **Core EPS** | TTM normalized EPS | **~$7.98** | — | 🟢 Reference multiple |
| **One-time item** | H1 non-marketable equity revaluation | **$62,814M** | Q2: $50,486M | ⚠️ Non-cash |
| **One-time item** | Non-marketable equity holdings | **$122,300M** | +655% vs Dec | ⚠️ Concentrated |
| **Cash flow** | TTM operating cash flow | $161,403M | **+33.2%** | 🟡 Flattered by tax |
| **Cash flow** | TTM capex | **$173,028M** | +60.7% | 🔴 |
| **Cash flow** | TTM free cash flow | **−$11,625M** | from +$13,481M | 🔴 Negative |
| **Cash flow** | H1 free cash flow | **−$26,992M** | vs −$7,672M | 🔴 Deteriorating |
| **Cash flow** | Q2 FCF | −$8,821M | vs +$332M | 🔴 |
| **Cash flow** | Capex / revenue (Q2) | **27.0%** | +780 bps | 🔴 Hyper-investment |
| **Cash flow** | Capex / adj. EBITDA (Q2) | **101%** | vs 79% | 🔴 |
| **Cash flow** | TTM deferred tax add-back | $41,441M | vs ~$2,407M | ⚠️ Quality flag |
| **Cash flow** | Adj. TTM FCF (ex deferred tax) | **~−$53.0B** | — | 🔴 |
| **Balance sheet** | Total assets | $1,095,689M | +33.9% (6 mo) | 🟡 |
| **Balance sheet** | Cash + securities | **$176,113M** | +32.8% | 🟢 |
| **Balance sheet** | Long-term debt | **$132,995M** | **+93.2%** | 🔴 Releveraging |
| **Balance sheet** | Gross debt (incl. fin. leases) | $146,446M | +71.5% | 🔴 |
| **Balance sheet** | Net debt (incl. securities) | **−$29,667M** | Net cash | 🟢 |
| **Balance sheet** | Current ratio | **1.03x** | — | 🟡 Tight |
| **Balance sheet** | Quick ratio | 0.875x | — | 🟡 |
| **Balance sheet** | AOCI | $66,287M | +$38,057M | ⚠️ Non-cash BV inflation |
| **Efficiency** | Cash conversion cycle | **−63.8 days** | DPO 140 vs DSO 40 | 🟢 Structural moat |
| **Efficiency** | Inventory | $38,184M | −0.4% | 🟢 Disciplined |
| **Efficiency** | Receivables | $88,092M | +30.1% | 🟡 Watch |
| **Efficiency** | Payables | $147,440M | +20.9% | 🟡 Lagging AR |
| **Costs** | Marketing growth (Q2) | +2.5% | vs rev +19.6% | 🟢 Leverage |
| **Costs** | SBC (H1) | $10,070M | −1.5% | 🟢 2.6% of rev |
| **Costs** | D&A (Q2) | $19,988M | **+31.3%** | 🔴 Rising |
| **Costs** | Interest expense (Q2) | $1,314M | **+154.7%** | 🔴 |
| **Tax** | Effective rate (H1) | 23.0% | vs 17.0% | 🟡 Normalizing |
| **Tax** | Cash taxes paid (H1) | $3,978M | vs $5,638M | ⚠️ Gap vs book tax |
| **Commitments** | Total contractual obligations | **$650,034M** | $78,084M <12 mo | 🔴 Huge |
| **Capital returns** | Share count (Jun-30) | 10,783M | **+0.5%** | 🔴 Dilution, no buyback |
| **M&A** | H1 business acquisitions | **$39,767M** | vs $1,652M | 🟡 Capital deployment |
| **Segments** | Reportable segments | 3 | — | ℹ️ NA / Intl / AWS |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | — | ⚪ Neutral/unknown |
| **Valuation** | Price-based multiples | **NOT AVAILABLE** | — | ⚪ Cannot compute |

---

### Bottom line for a trader
**AMZN's operating business is performing at the top of its historical range** — 19.6% revenue growth, 43% operating-income growth, 13.7% margins, and a −64-day cash-conversion cycle. **But the financial statements carry three distortions that most screens will miss:** (1) **$4.44/share of TTM EPS is a non-cash private-equity mark**, (2) **operating cash flow is boosted by $41.4B of deferred tax**, and (3) **free cash flow is deeply negative (−$11.6B TTM, ~−$53B adjusted) while debt has nearly doubled to $133B against $650B of commitments.**

**Trade the operations long, but underwrite the balance sheet carefully and never anchor on GAAP EPS.** The highest-conviction signal in this dataset is the **capex trajectory (27% of revenue, 101% of adj. EBITDA)** — that single line item will determine whether the current 13.7% operating margin is a launchpad or a peak.