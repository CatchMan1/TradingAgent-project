# AMZN — Fundamental Research Report
**As of 2024-02-26 | Company: Amazon.com, Inc. | Primary source: FY2023 Form 10-K (filed 2024-02-02, accn 0001018724-24-000008) + Q3-2023 10-Q (filed 2023-10-27)**

---

## 0. Data provenance & caveats (read first)

- All figures below are **point-in-time SEC facts accepted on or before 2024-02-26**. The only filings represented are the **FY2023 10-K (accepted 2024-02-02)** and the **Q3-2023 10-Q (accepted 2023-10-27)**. No new filing landed in the last week of the window; the 10-K is the freshest fundamental document (24 days old).
- **Insider transaction data: UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for AMZN at this date. I am explicitly **not** inferring or fabricating insider buying/selling. Treat Form 4 activity as a blind spot for this report.
- The delivered XBRL extract is **truncated alphabetically** (it ends near `IntangibleAssets…`/`OperatingLeaseLiabilityNoncurrent`), so several tags were **not delivered**: `Revenues`, `Inventory`, `PropertyPlantAndEquipmentNet`, `RetainedEarnings`, `StockholdersEquity`, and segment revenue detail. Where I need these, I **derive them arithmetically from delivered tags** and label the derivation. I do **not** backfill from memory.
- **Revenue is derived, not directly tagged**: Amazon's income statement identity holds exactly — `Revenue = OperatingIncomeLoss + CostsAndExpenses`. Cross-checks tie to the dollar for all three years, so the derived series is reliable.

---

## 1. Company profile & business model

Amazon operates **three reporting segments** (`NumberOfOperatingSegments = 3`): **North America**, **International**, and **Amazon Web Services (AWS)**. The structural economics visible in the delivered data:

| Attribute | Evidence from filings |
|---|---|
| Scale | Derived FY2023 revenue **$574.8B**, +11.8% YoY |
| Mix shift to high-margin revenue | Gross margin up **+318 bp to 47.0%** in one year; non-retail (AWS, advertising, third-party seller services, Prime subscriptions) is the driver — advertising costs disclosed at **$20.3B** (a cost, flat YoY) imply a large and maturing ads business |
| Heavy fixed-asset/lease base | Capex **$52.7B**; operating lease liabilities **$75.6B**; operating lease payments **$10.5B**; finance lease liabilities **$12.1B** |
| Deferred revenue ("backlog" proxy) | Contract liabilities **$20.6B, +28.0% YoY** (current $15.2B, noncurrent $5.7B **+96.6%**); **$12.4B of 2023 revenue** came from the opening contract-liability balance |
| Public float (size reference) | **$1.184 trillion** as of 2023-06-30 (`EntityPublicFloat`) — 8 months stale at this date |
| Shares outstanding | **10,383M** at 2023-12-31; **10,387.4M** at 2024-01-24; 10,898M issued (so ~515M treasury) |

---

## 2. Income statement — FY2021 → FY2023 (reconstructed)

All figures USD millions. Revenue derived as `OperatingIncomeLoss + CostsAndExpenses`.

| Line item | FY2021 | FY2022 | FY2023 | YoY '23 |
|---|---:|---:|---:|---:|
| **Net sales (derived)** | **469,822** | **513,983** | **574,785** | **+11.8%** |
| Cost of goods & services | 272,344 | 288,831 | 304,739 | +5.5% |
| **Gross profit** | **197,478** | **225,152** | **270,046** | **+19.9%** |
| *Gross margin* | *42.0%* | *43.8%* | *47.0%* | *+318 bp* |
| Marketing (S&M) | 32,551 | 42,238 | 44,370 | +5.1% |
| G&A | 8,823 | 11,891 | 11,816 | -0.6% |
| Fulfillment + Tech & content + Other opex (derived residual) | 131,225 | 158,775 | 177,008 | +11.5% |
| **Total costs & expenses** | **444,943** | **501,735** | **537,933** | **+7.2%** |
| **Operating income** | **24,879** | **12,248** | **36,852** | **+200.9%** |
| *Operating margin* | *5.29%* | *2.38%* | *6.41%* | *+403 bp* |
| Interest expense | 1,809 | 2,367 | 3,182 | +34.4% |
| Interest & investment income | 448 | 989 | 2,949 | +198% |
| Nonoperating income/(expense), total | 13,272 | (18,184) | 705 | n.m. |
| Pretax income | 38,151 | (5,936) | 37,557 | n.m. |
| Income tax | 4,791 | (3,217) | 7,120 | n.m. |
| *Effective tax rate* | *12.6%* | *n.m. (benefit)* | *19.0%* | *+640 bp* |
| **Net income** | **33,364** | **(2,722)** | **30,425** | **n.m.** |
| *Net margin* | *7.10%* | *-0.53%* | *5.29%* | *+582 bp* |
| **Diluted EPS** | **$3.24** | **($0.27)** | **$2.90** | n.m. |
| Diluted share count (implied) | ~10,298M | ~10,189M | ~10,493M | +3.0% |
| D&A | 34,433 | 41,921 | 48,663 | +16.1% |
| Share-based comp | 12,757 | 19,621 | 24,023 | +22.4% |

### The single most important read: earnings quality has structurally improved
- FY2023 **operating income ($36.9B) is 48% above FY2021 ($24.9B)** — yet headline net income ($30.4B) is *below* FY2021 ($33.4B). The gap is entirely non-operating: FY2021 carried **+$11.6B** of unrealized equity-security gains (mark-to-market, Rivian-era) vs **−$13.6B** in FY2022 and only **+$1.0B** in FY2023.
- **Translation:** the 2021 profit was part-mark-to-market; the 2023 profit is ~98% operating-driven. This is a materially higher-quality earnings base and supports a higher multiple on the same nominal EPS.
- **But:** the tax tailwind is spent. Effective rate moved 12.6% → 19.0%; the FY2023 rate already reflects $1,429M FDII benefit, $2,362M credits, offset by $1,307M state taxes and $1,047M SBC shortfalls. 2024+ EPS growth must come from operating leverage, not tax.

### Margin bridge details
- Gross margin +318 bp is the whole story; every opex line grew slower than revenue (Marketing +5.1%, G&A −0.6%, residual opex +11.5% vs revenue +11.8%).
- **Operating leverage is real and accelerating into Q4:** FY operating margin of 6.41% implies a very strong H2 — Q4-2023 operating income must have been well above the 9M run rate given the FY total (tools supply only the annual figure; quarterly IS detail is not in the extract).
- **Interest expense is a growing drag**: +34.4% in 2023 on top of +30.8% in 2022 (+76% cumulatively), as fixed-rate debt reprices. Net interest is now roughly neutral (income $2.9B vs expense $3.2B); **EBIT/interest coverage = 11.6x** (vs 5.2x in 2022, 13.8x in 2021).

---

## 3. Cash flow — the FCF inflection is the trade

| USD millions | FY2021 | FY2022 | FY2023 | Δ '22→'23 |
|---|---:|---:|---:|---:|
| Cash from operations | 46,327 | 46,752 | **84,946** | **+38,194 (+81.7%)** |
| Purchases of PP&E (capex, gross) | 61,053 | 63,645 | **52,729** | **−10,916 (−17.1%)** |
| **Free cash flow (OCF − capex)** | **(14,726)** | **(16,893)** | **+32,217** | **+49,110** |
| *FCF margin* | *-3.1%* | *-3.3%* | *+5.6%* | *+890 bp* |
| *OCF margin* | *9.9%* | *9.1%* | *14.8%* | *+568 bp* |
| *Capex intensity (capex/revenue)* | *13.0%* | *12.4%* | *9.2%* | *−323 bp* |
| Investing cash flow | (58,154) | (37,601) | (49,833) | −12,232 |
| Financing cash flow | +6,291 | +9,718 | **(15,879)** | swing to outflow |
| Marketable securities: purchases / sales+maturities | (60,157)/59,384 | (2,565)/31,601 | (1,488)/5,627 | — |
| Finance lease principal payments | 11,163 | 7,941 | 4,384 | −3,557 |
| Share repurchases | 0 | 6,000 | **0** | — |
| LT debt issued / repaid | 19,003 / 1,590 | 21,166 / 1,258 | **0** / 3,676 | — |
| ST debt proceeds / repayments | 7,956 / 7,753 | 41,553 / 37,554 | 18,129 / 25,677 | — |

### The 2023 FCF swing is a *two-sided* story, and both sides are durable
1. **Cost side:** capex cut 17% (−$10.9B) as fulfillment/network buildout normalizes. Capex intensity fell from 12.4% to 9.2% of revenue.
2. **Operating side:** OCF +82% (+$38.2B). Part is genuine margin expansion (operating income +$24.6B), part is non-cash (D&A $48.7B, SBC $24.0B).
3. **Note the working-capital headwind** that *suppressed* OCF: AR/other operating assets **−$8.3B**, accrued liabilities **−$2.4B**, other noncurrent assets **−$12.3B**, partially offset by deferred revenue **+$4.6B** and a **−$5.9B** non-cash deferred-tax benefit. Cash flow was *not* flattered by stretching payables — that's a quality positive.

### Quarterly reconstruction — this is the caution flag (derived: FY minus 9M 10-Q)

| USD millions | Q3-2022 | 9M-2022 | Q3-2023 | 9M-2023 | Q4-2023 (derived) |
|---|---:|---:|---:|---:|---:|
| OCF | 11,404 | 17,579 | 21,217 | 42,481 | **42,465** |
| Capex | 16,378 | 47,053 | 12,479 | 38,141 | **14,588** |
| **FCF** | **(4,974)** | **(29,474)** | **+8,738** | **+4,340** | **+27,877** |
| TTM FCF (as of period end) | — | — | **16,921** | 16,921 | **32,217** |
| Investing CF | (15,608) | (26,780) | (11,753) | (37,232) | (12,601) |
| Financing CF | +3,016 | +9,632 | (8,948) | (9,133) | (6,746) |

**Actionable observation:** **86.5% of full-year 2023 FCF ($27.9B of $32.2B) was generated in Q4 alone.** Q4 is the seasonal cash peak (holiday receivables collection, payables build, Prime sign-ups). **Q1 is structurally Amazon's weakest cash quarter** — with the 10-K now the last filing, the next fundamental datapoint (10-Q, ~late April 2024) is at meaningful risk of showing a *sequential collapse* in FCF. Traders should pre-position for that optics risk rather than extrapolate the Q4 run rate.

---

## 4. Balance sheet — fortress, with a large lease stock

| USD millions | 2021-12-31 | 2022-12-31 | 2023-12-31 | YoY |
|---|---:|---:|---:|---:|
| Cash & equivalents | n/d | 53,888 | **73,387** | +36.2% |
| Marketable securities (AFS, fair value) | n/d | n/d | **70,919** | n/d |
| **Cash + securities** | n/d | n/d | **~144,306** | n/d |
| Accounts receivable, net | n/d | 42,360 | 52,253 | +23.4% |
| Allowance for doubtful accounts | 1,100 | 1,400 | 1,700 | +21.4% (write-offs 1,600) |
| **Total current assets** | n/d | 146,791 | **172,351** | +17.4% |
| Total assets | 420,549 | 462,675 | **527,854** | +14.1% |
| Accounts payable | n/d | 79,600 | 84,981 | +6.8% |
| Accrued expenses & other current | n/d | 62,566 | 64,709 | +3.4% |
| Employee-related liabilities | n/d | 7,700 | 7,700 | 0.0% |
| Contract liabilities (total) | n/d | 16,100 | 20,600 | +28.0% |
| — current / noncurrent | — | 13,227 / 2,900 | 15,227 / 5,700 | +15.1% / +96.6% |
| Long-term debt (carrying) | n/d | 67,150 | **58,314** | **−13.2%** |
| Finance lease liabilities | n/d | 15,783 | 12,109 | −23.3% |
| Operating lease liabilities | n/d | 69,040 | **75,639** | +9.6% |
| Deferred tax assets, net | n/d | 34,509 | 45,788 | +32.7% |
| Finite-lived intangibles, net | n/d | 4,950 | 6,540 | +32.1% |
| APIC | n/d | 75,066 | 99,025 | +31.9% |
| AOCI | (4,487) | (4,487) | (3,040) | improving |

**Liquidity & leverage:**
- **Net cash position (excluding leases): ~+$73.9B** — debt $58.3B + finance leases $12.1B = $70.4B against $144.3B cash + securities. Unambiguously fortress-grade.
- **Including leases:** operating lease liabilities of **$75.6B** (undiscounted commitments **$90.8B**, up from $81.3B) plus finance leases **$12.1B** ⇒ total obligation stack ~$146B, i.e., roughly cash-equivalent. Lease-adjusted, Amazon is roughly **neutral**, not net cash.
- **Current ratio ≈ 1.0x.** Identifiable current obligations: AP $85.0B + accrued $64.7B + current LTD $8.5B + current leases $10.5B ≈ **$168.6B** vs current assets **$172.4B**. Note deferred revenue/contract liabilities and employee liabilities are components of the accrued line and must not be double-counted. Conclusion: **no liquidity risk, but no liquidity cushion either** — Amazon runs intentionally thin working capital and relies on operating cash generation.
- **Debt maturity ladder (LT debt principal, at 12/31/23):** 2024 $8,500M → 2025 $5,286M → 2026 $3,146M → 2027 $8,750M → 2028 $2,250M → beyond $39,250M. Total scheduled ~$67.2B. **Well-laddered, no refinancing wall**; 2024 maturities (~$8.5B) are covered >8x by cash alone.
- **Finance lease payments due:** 2024 $2,292M; 2025 $1,471M; 2026 $1,369M; 2027 $1,123M; 2028 $1,022M; beyond $6,829M (total $14.1B).
- **Operating lease payments due:** 2024 $11,229M; 2025 $9,922M; 2026 $9,156M; 2027 $8,321M; 2028 $7,546M; beyond $44,603M.
- **Total contractual obligations: $300.4B**, of which **$39.3B due within 12 months** (PP&E purchase commitments + digital content + leases). This is the forward capex/spend signal — see risks.

**Derived return metrics (equity tag not delivered, so ROE is not computable):**
- **ROA** (net income / avg assets): 2023 **6.1%**; 2022 -0.6%.
- **Cash return on assets** (FCF / total assets): **6.1%** in 2023 vs -3.7% in 2022.
- **Pre-tax ROIC proxy** (NOPAT at 19% tax / (debt + finance leases + op leases + book equity)) cannot be cleanly closed without the equity tag; directionally, note NOPAT ≈ **$29.9B** (36,852 × 0.81) vs an invested capital base dominated by $75.6B of operating leases — lease-adjusted ROIC is materially lower than the headline 6.4% operating margin suggests.

---

## 5. Capital allocation & dilution

- **No share repurchases in FY2023** (vs **$6.0B** in FY2022). No dividend, ever.
- **No long-term debt issued in FY2023** (first zero-issuance year in the visible window; $19.0B in 2021, $21.2B in 2022). Net short-term debt **−$7.5B** (18,129 proceeds vs 25,677 repayments). Net debt reduction ≈ **$11.2B** gross.
- **Primary "return of capital" in 2023 was debt paydown + reinvestment**, not shareholder returns. Financing CF swung from +$9.7B (2022) to **−$15.9B** (2023) — a $25.6B reduction in external funding dependence.
- **Dilution is the hidden tax on EPS:** SBC **$24.0B = 4.18% of revenue**, up from $19.6B (3.82%) and $12.8B (2.72%). Shares outstanding +1.38% YoY; diluted count +3.0%. With zero buybacks, **~1.4%/yr share creep persists**, and **$18.3B of unrecognized SBC** remains to be expensed (plus 1,600M shares reserved for future issuance = 15.4% of shares outstanding). Reported EPS understates economic dilution.

---

## 6. Tax, deferred tax, and intangibles (forward-looking tells)

- **Deferred tax assets, net: $45.8B** (+32.7%), gross DTA $50.6B against a modest $4.8B valuation allowance (up from $4.4B) — management still expects to realize the bulk of it, consistent with sustained US profitability (`IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic` = **+$32.3B** in 2023 vs **−$8.2B** in 2022 and +$35.9B in 2021; foreign pre-tax +$5.2B, up from +$2.3B).
- **IPR&D deferred tax asset jumped from $6.8B to $14.8B (+117%)** — a strong signal of **acquisition activity/intangible capitalization** in 2023 that does not appear in the investing section's marketable-securities lines. Intangibles gross rose $8.3B → $10.1B; finite-lived net $5.0B → $6.5B; DTL on PP&E rose $9.0B → $12.5B.
- **Amortization runway:** $715M (2024), $631M, $563M, $552M, $534M, then $3,545M beyond — a growing but manageable non-cash drag.
- **Cash taxes $11.2B vs book tax $7.1B** — Amazon is now a full cash taxpayer; the "low-tax growth company" era is over. 2024+ tax rate anchors at ~19–21%.

---

## 7. Insider transactions

**UNAVAILABLE.** The data vendor explicitly reports no authorized point-in-time insider-transactions archive for AMZN as of 2024-02-26. I have not inferred, estimated, or fabricated any Form 4 activity. Any insider read must come from a different data source; it is a genuine gap in this report, not a null result.

---

## 8. Valuation framing (deliberately price-agnostic)

No price series was supplied, so I will not fabricate a multiple. For calibration only, using the last disclosed **public float of $1.184T (2023-06-30)**:

| Metric | FY2023 | Implied multiple on stale float |
|---|---:|---:|
| Net income | $30,425M | ~38.9x |
| Free cash flow | $32,217M | ~36.7x |
| Operating income | $36,852M | ~32.1x |
| OCF | $84,946M | ~13.9x |

**Interpretation:** on that (stale) reference point, AMZN is priced as a **~37–39x earnings / ~37x FCF** asset. That multiple is only defensible if the 2023 FCF inflection *continues* — i.e., if capex intensity stays near 9% of revenue and margins keep expanding. **The entire valuation debate reduces to one question: is the 2023 capex cut permanent, or is it the trough before an AI/cloud capex reacceleration?** The data provide ammunition for the bear side (see below).

---

## 9. Actionable insights for traders

**Bull case — supported by the data**
1. **Earnings quality transformation.** Operating income +200.9% to $36.9B, the highest ever, with operating margin +403 bp to 6.41%. The FY2023 profit is ~98% operating vs ~65% in FY2021 (which was inflated by $11.6B of mark-to-market gains). Re-rating justification is fundamentally sound, not narrative.
2. **Structural gross-margin expansion, not one-off cost cuts.** +318 bp in gross margin with marketing growing only +5.1% and G&A −0.6% — classic mix shift toward AWS/ads/3P/subs. This is the most durable line in the model.
3. **First positive FCF since 2020: +$32.2B vs −$16.9B**, a $49.1B swing. Balance sheet is net cash ~$74B ex-leases, debt down 13.2% YoY, zero LT issuance needed, no refinancing wall until 2027 ($8.75B).
4. **Demand signal in deferred revenue:** contract liabilities +28.0% to $20.6B, with the noncurrent piece nearly **doubling** (+96.6%) — that is committed, multi-year revenue (AWS commitments/Prime), i.e., visibility improving.
5. **Interest-rate tailwind turning:** interest income +198% to $2.9B, nearly offsetting the $3.2B interest expense. Coverage 11.6x.

**Bear case / risk controls — supported by the data**
1. **Q4-loaded FCF is a trap for momentum chasers.** 86.5% of FY2023 FCF came in Q4. Q1 seasonality plus the fact that the 10-K is the last filing means the next print (~late April 2024) can show a dramatic sequential FCF drop with no deterioration in the business. **Do not extrapolate the Q4 FCF run rate.**
2. **Capex reacceleration risk is live and quantifiable.** Q4-2023 capex alone was **$14.6B** — annualized **~$58B**, above the full-year $52.7B. Combined with **$39.3B of contractual obligations due within 12 months** (out of $300.4B total), the 2024 capex line is more likely to rise than fall. A capex guide-up re-breaks the FCF math that supports a ~37x FCF multiple.
3. **Tax tailwind exhausted.** Effective rate 12.6% → 19.0%; cash taxes $11.2B > book tax $7.1B. No more rate-driven EPS upside.
4. **Dilution + no buyback.** SBC 4.18% of revenue, +1.38% share count, zero repurchases, $18.3B unrecognized SBC pending. Reported EPS overstates per-share economics by ~1.5%/yr.
5. **Interest expense compounding.** +76% over two years to $3.2B; coverage still ample at 11.6x but the direction is negative, and $39.3B of debt matures beyond 2028 at unknown future rates.
6. **Working-capital drag persists.** The $12.3B outflow in "other noncurrent assets" and $8.3B in AR/other are recurring structural cash consumers — OCF quality is good, but it isn't frictionless.

**Concrete positioning ideas**
- **Favor the multi-quarter margin-compounding thesis over the single-quarter FCF headline.** The margin data (+318 bp GM, +403 bp OM) is the highest-confidence signal in the dataset.
- **Treat any Q1-2024 FCF disappointment as a seasonality artifact, not a thesis break** — but require Q1 *gross margin* ≥46% and *operating margin* ≥6% to confirm the thesis is intact. Those are the two cleanest diagnostic lines in this dataset.
- **Set a hard invalidation trigger on capex:** if FY2024 capex guidance materially exceeds $60B (i.e., above the Q4 annualized run rate) with no matching acceleration in AWS/ads revenue growth, the FCF-inflection thesis is broken and a ~37x FCF multiple is indefensible.
- **Monitor contract liabilities (deferred revenue) as the leading demand indicator** — a deceleration below ~15% YoY growth would precede reported revenue deceleration by 1–2 quarters.
- **Insider signal is a blind spot** — do not treat absence of data as absence of selling; source it independently before sizing.

**Catalyst calendar:** Next fundamental datapoint is the Q1-2024 10-Q (~late April 2024). FY2023 10-K (2024-02-02) is fully digested.

---

## 10. Key points summary

| Category | Metric | FY2021 | FY2022 | FY2023 | Read-through |
|---|---|---:|---:|---:|---|
| **Scale** | Net sales (derived) | 469,822 | 513,983 | 574,785 | +11.8% YoY, reaccelerating |
| **Growth** | Revenue YoY | — | +9.4% | +11.8% | Growth inflected up |
| **Margin** | Gross margin | 42.0% | 43.8% | 47.0% | +318 bp — mix shift, durable |
| **Margin** | Operating margin | 5.29% | 2.38% | 6.41% | Record; +403 bp YoY |
| **Profit** | Operating income | 24,879 | 12,248 | 36,852 | +200.9% YoY |
| **Profit** | Net income | 33,364 | (2,722) | 30,425 | Record operating-driven profit |
| **Profit** | Diluted EPS | $3.24 | ($0.27) | $2.90 | Below 2021 on EPS despite higher op income |
| **Quality** | Nonoperating income | +13,272 | (18,184) | +705 | Mark-to-market noise now negligible |
| **Quality** | Effective tax rate | 12.6% | n.m. | 19.0% | Tax tailwind exhausted |
| **Cash** | Operating cash flow | 46,327 | 46,752 | 84,946 | +81.7% YoY |
| **Cash** | Capex (gross PP&E) | 61,053 | 63,645 | 52,729 | −17.1% YoY |
| **Cash** | **Free cash flow** | **(14,726)** | **(16,893)** | **+32,217** | **+$49.1B swing — the core thesis** |
| **Cash** | FCF / revenue | -3.1% | -3.3% | +5.6% | Inflection confirmed for FY23 |
| **Cash** | Q4-only FCF (derived) | n/d | n/d | 27,877 | **86.5% of FY FCF — seasonality risk** |
| **Cash** | Q4 capex (derived) | n/d | n/d | 14,588 | Annualizes ~$58B → 2024 capex risk |
| **Balance sheet** | Cash + securities | n/d | n/d | ~144,306 | Fortress liquidity |
| **Balance sheet** | LT debt (carrying) | n/d | 67,150 | 58,314 | −13.2%; zero LT issuance in '23 |
| **Balance sheet** | Net cash (ex-leases) | n/d | n/d | ~+73,900 | Strongly positive |
| **Balance sheet** | Operating lease liabilities | n/d | 69,040 | 75,639 | Lease-adjusted leverage ≈ neutral |
| **Balance sheet** | Current ratio | n/d | n/d | ~1.0x | Intentionally thin; no cushion |
| **Balance sheet** | Net PP&E-related DTL | n/d | 9,039 | 12,454 | Capex/depreciation timing |
| **Obligations** | Contractual obligations | n/d | n/d | 300,409 | $39.3B due <12 mo — spend signal |
| **Demand** | Contract liabilities (deferred rev) | n/d | 16,100 | 20,600 | +28%; noncurrent +96.6% |
| **Demand** | Revenue from opening deferred rev | n/d | n/d | 12,400 | High backlog conversion |
| **Capital return** | Buybacks | 0 | 6,000 | 0 | None in 2023 |
| **Capital return** | Dividends | 0 | 0 | 0 | Never paid |
| **Dilution** | SBC expense | 12,757 | 19,621 | 24,023 | 4.18% of revenue; ~1.4%/yr creep |
| **Dilution** | Unrecognized SBC | n/d | n/d | 18,300 | Future expense overhang |
| **Dilution** | Shares outstanding | n/d | 10,242 | 10,383 | +1.38% YoY |
| **Leverage** | EBIT / interest | 13.8x | 5.2x | 11.6x | Recovered; interest +76% over 2 yrs |
| **Returns** | ROA | n/d | -0.6% | 6.1% | Recovering strongly |
| **Returns** | FCF / total assets | n/d | -3.7% | 6.1% | Cash generation restored |
| **Tax** | Cash taxes paid | 3,688 | 6,035 | 11,179 | Now a full cash taxpayer |
| **Tax** | IPR&D deferred tax asset | n/d | 6,824 | 14,800 | Signals acquisitions/intangible build |
| **Valuation** | Public float (2023-06-30) | — | — | $1.184T | ~38.9x NI / ~36.7x FCF (stale) |
| **Insider** | Form 4 activity | — | — | **UNAVAILABLE** | Explicit data gap — not a null result |

**Bottom line:** AMZN's FY2023 10-K documents a genuine, structurally-supported operating inflection — gross margin +318 bp, operating income +201%, and the first positive free cash flow since 2020 (+$32.2B vs −$16.9B). Earnings quality is materially higher than 2021 because the profit is now operating-driven rather than mark-to-market. The risk is *not* the business; it is the **fragility of extrapolating a Q4-loaded, capex-assisted FCF number** (86.5% of FCF came from one quarter, and Q4 capex annualizes above the full-year figure against $39.3B of near-term contractual commitments). Trade the margin compounding, fade the FCF extrapolation, and watch gross margin (≥46%) and operating margin (≥6%) as the two cleanest confirmation/invalidation signals for the next 10-Q.