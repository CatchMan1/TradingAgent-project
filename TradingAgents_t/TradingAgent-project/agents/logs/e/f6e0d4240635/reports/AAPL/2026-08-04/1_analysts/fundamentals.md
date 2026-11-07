# AAPL — Fundamental Deep Dive (as of 2026-08-04)

**Company:** Apple Inc. (AAPL) · **Latest filing in the point-in-time cache:** Form 10-Q for the quarter ended **2026-06-27**, accepted **2026-07-31 14:01 UTC** (accession 0000320193-26-000020) — i.e., **4 days old at the analysis date**. This is the freshest fundamental information available; there has been no newer filing.

---

## 1. Data provenance & explicit limitations

| Item | Status |
|---|---|
| Source | Point-in-time SEC XBRL facts (10-Q filed 2026-07-31; prior 10-Qs filed 2026-05-01, 2026-01-30; 10-K filed 2025-10-31) |
| Periods covered | Q3 FY26 (ended 6/27/26), Q2 FY26 (3/28/26), Q1 FY26 balance sheet, FY2023–FY2025 annual cash-flow aggregates |
| Price / market cap / valuation multiples | **Not available from these tools.** No P/E, EV/EBITDA or yield can be computed reliably. All analysis below is business-model/earnings based. |
| Insider transactions | **DATA_UNAVAILABLE** — the vendor has no authorized point-in-time insider-transaction archive for AAPL. **No insider activity is inferred or fabricated.** Treat this as a governance-information gap, not as "no insider selling." |
| Full FY2025 income statement / OCF | Not present in the retrieved slice (only FY25 financing −$120,686M and investing +$15,195M are in the 10-K extract). TTM figures are therefore built from 9M FY26 annualized run-rates, labeled as such. |
| FY26 detail not tagged | Segment/product-line revenue, geographic mix, gross-margin-by-line, and buyback share counts are **not** in the XBRL slice. |

> **Important sign convention note:** the XBRL working-capital tags use *negative = cash use from an increase in the asset*. All interpretation below already accounts for this.

---

## 2. Company profile (context for the numbers)

Apple Inc. designs, manufactures and markets smartphones (iPhone), personal computers (Mac), tablets (iPad), wearables/home/accessories (Watch, AirPods, Vision), and derives a large and growing profit pool from **Services** (App Store, iCloud, advertising, Apple Music/TV+, payments, licensing). The model is characterized by:
- Outsourced manufacturing (concentrated assembly partner base), extreme asset-lightness (**capex only 1.9% of revenue in 9M FY26**),
- A hardware installed base that monetizes via high-margin recurring Services,
- Massive free cash flow returned through buybacks + dividends,
- A deliberately leveraged-but-net-cash balance sheet.

The FY26 data show **all four of these pillars intensifying simultaneously** — which is the core of the story below.

---

## 3. Income statement: growth re-accelerated AND gross margin broke 50%

### 3.1 Q3 FY26 (quarter ended 2026-06-27) vs Q3 FY25

| Line ($M) | Q3 FY26 | Q3 FY25 | Δ % | % of rev FY26 |
|---|---:|---:|---:|---:|
| Revenue | **109,417** | 94,036 | **+16.4%** | 100.0% |
| Cost of goods & services | 54,647 | 50,318 | +8.6% | 49.9% |
| **Gross profit** | **54,770** | 43,718 | **+25.3%** | **50.1%** |
| R&D | 11,729 | 8,866 | **+32.3%** | 10.7% |
| SG&A (S&M 5,034 + G&A 2,312) | 7,346 | 6,650 | +10.5% | 6.7% |
| Total operating expenses | 19,075 | 15,516 | +22.9% | 17.4% |
| **Operating income** | **35,695** | 28,202 | **+26.6%** | **32.6%** |
| Non-operating inc/(exp) | +572 | (171) | n.m. | 0.5% |
| Pre-tax income | 36,267 | 28,031 | +29.4% | 33.1% |
| Tax | 6,478 | 4,597 | +40.9% | 5.9% |
| **Net income** | **29,789** | 23,434 | **+27.1%** | **27.2%** |
| **EPS diluted** | **$2.02** | $1.57 | **+28.7%** | — |
| EPS basic | $2.03 | $1.57 | +29.3% | — |

**Derived Q3 metrics:**
- Gross margin **50.06%** vs 46.49% → **+357 bp YoY**
- Operating margin **32.62%** vs 29.99% → **+263 bp**
- Net margin **27.22%** vs 24.92% → **+230 bp**
- Effective tax rate **17.86%** vs 16.40% → **+146 bp headwind**
- R&D intensity **10.72%** vs 9.43% → +129 bp

### 3.2 Nine months FY26 (2025-09-28 → 2026-06-27) vs nine months FY25

| Line ($M) | 9M FY26 | 9M FY25 | Δ % | Margin FY26 | Margin FY25 |
|---|---:|---:|---:|---:|---:|
| Revenue | **364,357** | 313,695 | **+16.2%** | — | — |
| Cost of goods & services | 185,575 | 166,835 | +11.2% | 50.9% | 53.2% |
| **Gross profit** | **178,782** | 146,860 | **+21.7%** | **49.07%** | 46.82% |
| R&D | 34,035 | 25,684 | **+32.5%** | 9.34% | 8.19% |
| SG&A | 22,315 | 20,553 | +8.6% | 6.12% | 6.55% |
| Total opex | 56,350 | 46,237 | +21.9% | 15.47% | 14.74% |
| **Operating income** | **122,432** | 100,623 | **+21.7%** | **33.60%** | 32.08% |
| Non-operating inc/(exp) | +670 | (698) | n.m. | 0.2% | (0.2%) |
| Pre-tax income | 123,102 | 99,925 | +23.2% | 33.79% | 31.85% |
| Tax | 21,638 | 15,381 | **+40.7%** | 17.58% | 15.39% |
| **Net income** | **101,464** | 84,544 | **+20.0%** | **27.85%** | 26.95% |
| **EPS diluted** | **$6.88** | $5.62 | **+22.4%** | — | — |
| Diluted shares (implied) | ~14,748M | ~15,043M | −2.0% | — | — |

### 3.3 The single most important analytical nuance

**All of the operating-margin expansion came from gross margin — not from operating leverage.**

- Gross margin: **+225 bp** (9M) / **+357 bp** (Q3)
- Operating expenses grew **faster** than revenue: **+21.9% vs +16.2%** (9M); **+22.9% vs +16.4%** (Q3)
- Operating margin therefore expanded only **+152 bp** (9M) / **+263 bp** (Q3)

This is a **fragility**, and it is the key swing factor for the next two quarters: if gross margin normalizes toward the high-40s while R&D keeps compounding at 30%+, operating margin compresses quickly. For scale: **each 100 bp of gross margin at the current annualized revenue run-rate (~$486B) is ≈ $4.9B pre-tax ≈ $0.28 of EPS.**

**Why gross margin likely expanded:** mix shift toward Services (structurally ~70%+ GM), plus favorable component/memory pricing locked in earlier, plus a weaker-cost environment versus the prior-year tariff/component headwind. The persistence of a 50% GM is the #1 question for the October print.

### 3.4 Quarterly build (Q1–Q3 FY26, derived)

| Metric ($M) | Q1 FY26 | Q2 FY26 | Q3 FY26 |
|---|---:|---:|---:|
| Gross profit | 69,231* | 54,781 | 54,770 |
| Pre-tax income | 51,002* | 35,833 | 36,267 |
| EPS diluted | $2.84* | $2.01 | $2.02 |
| Net income (Q3 only) | — | — | 29,789 |

\*Derived as (6M total − Q2). Six-month (Q1+Q2) totals: revenue **254,940**, net income **71,675**, EPS diluted **$4.85**.

**Read-through:** Q2 FY26 pre-tax of $35.8B and Q3 FY26 of $36.3B are essentially flat sequentially — **the June quarter did not deleverage off the March quarter**, which is seasonally unusual (June is normally the softest quarter). That is a genuinely bullish data point on both demand and cost.

---

## 4. Balance sheet: deleveraging, net cash build, and two loud "investment-mode" signals

### 4.1 Balance sheet ($M)

| Item | 2026-06-27 | 2026-03-28 | 2025-09-27 | Δ vs FY25 end |
|---|---:|---:|---:|---:|
| Cash & equivalents | 39,544 | 45,572 | 35,934 | +3,610 |
| Marketable securities — current | 22,855 | n/a | 18,763 | +4,092 |
| Accounts receivable | 31,398 | 30,339 | 39,777 | −8,379 |
| Non-trade receivables | 27,509 | 23,172 | 33,318 | −5,809 |
| **Inventory** | **11,092** | 6,747 | 5,718 | **+5,374 (+94.0%)** |
| — raw materials & parts | **7,645** | n/a | 2,124 | **+5,521 (+260%)** |
| — finished goods | 3,447 | n/a | 3,594 | −147 |
| Other current assets | 17,420 | 15,349 | 14,585 | +2,835 |
| **Total current assets** | **149,818** | 144,114 | 147,957 | +1,861 |
| Marketable securities — noncurrent | 84,118 | n/a | 77,723 | +6,395 |
| Other noncurrent assets | 77,557 | 77,430 | 72,634 | +4,923 |
| **Total noncurrent assets** | **233,448** | 226,968 | 211,284 | +22,164 |
| **TOTAL ASSETS** | **383,266** | 371,082 | **359,241** | **+24,025** |
| Accounts payable | 64,525 | n/a | 69,860 | −5,335 |
| Commercial paper | 1,997 | n/a | 7,979 | −5,982 |
| Current LTD | 11,007 | 8,310 | 12,350 | −1,343 |
| Other current liabilities | 62,259 | n/a | 66,387 | −4,128 |
| **Total current liabilities** | **149,326** | 134,641 | 165,631 | −16,305 |
| Long-term debt (noncurrent) | 71,340 | 74,404 | 78,328 | −6,988 |
| Other noncurrent liabilities | 55,080 | n/a | 41,549 | +13,531 |
| **TOTAL LIABILITIES** | **275,746** | 264,591 | 285,508 | −9,762 |
| **Shareholders' equity** | **107,520** | 106,491 | **73,733** | **+33,787 (+45.8%)** |
| Shares outstanding (M) | 14,608.96 | — | 14,773.26 | −164.3M (−1.11%) |
| Shares outstanding 2026-07-17 (cover page) | **14,594.18** | — | — | — |

### 4.2 Liquidity, leverage, net cash

| Metric | 2026-06-27 | 2025-09-27 | Change |
|---|---:|---:|---:|
| Total debt (CP + current LTD + LT LTD) | 84,344 | 98,657 | **−14,313** |
| Cash + all marketable securities | 146,517 | 132,420 | +14,097 |
| **Net cash** | **62,173** | 33,763 | **+28,410** |
| Current ratio | **1.003x** | 0.893x | +0.11x |
| Debt / equity | **0.78x** | 1.34x | −0.56x |
| Equity / total assets | **28.1%** | 20.5% | +760 bp |

**This is a materially de-risked balance sheet.** Apple entered FY26 with a sub-0.9 current ratio (a perennial liquidity talking point) and has pushed it to parity. Debt is down $14.3B in nine months **with zero new long-term debt issued** (`ProceedsFromIssuanceOfLongTermDebt` = **$0** for 9M FY26, versus $4,481M in 9M FY25). Net cash rose $28.4B in nine months.

### 4.3 Signal #1 — the inventory build (the loudest leading indicator)

- Total inventory **+64% in a single quarter** ($6,747M → $11,092M) and **+94%** versus FY25 year-end.
- The entire move is **raw materials and purchased parts, +260%** to $7,645M. **Finished goods actually declined** ($3,594M → $3,447M).

Interpretation: this is a **component/parts pipeline build, not unsold-product stuffing**. That is the classic signature of a **large new-product ramp** (next-gen iPhone cycle, an AI/edge device, or a foldable/form-factor transition) where Apple is securing supply ahead of volume. Two implications for traders:
- **Bullish if** the following quarter's revenue accelerates again into the September quarter (Q4 is Apple's second-largest quarter) — it means Apple is buying share of constrained components.
- **Bearish if** Q4 revenue does not re-accelerate — then ~$7.6B of parts inventory sits on the balance sheet and write-down risk becomes real, plus it will reverse as a cash-flow headwind.

### 4.4 Signal #2 — a step-change in intangible assets (unclosed disclosure gap)

| Item | 2026-06-27 | 2025-09-27 | Change |
|---|---:|---:|---:|
| Intangibles, gross | 38,220 | 24,950 | **+13,270** |
| Accumulated amortization | (12,803) | (11,649) | +1,154 |
| **Intangibles, net** | **25,417** | 13,301 | **+12,116** |

Gross intangibles grew **+53% in nine months**. **This is not reconcilable with the cash-flow items captured in the retrieved extract.** Cash investing outflows total only **$18,811M** for 9M FY26, of which identifiable items are: AFS purchases −$48,752M, AFS sales +$12,016M, AFS maturities +$26,504M, capex −$6,799M, other +$1,780M → a **−$15,251M** subtotal, leaving only **~−$3,560M of unreconciled investing outflow** (versus ~−$1,950M in the prior-year period). 

**Actionable:** the delta between the ~$13.3B gross-intangible increase and the ~$3.6B residual cash outflow is either (a) an M&A/asset purchase whose cash consideration isn't tagged in this slice, (b) capitalized content/licensing additions, or (c) a reclassification. **This must be confirmed in the 10-Q notes (~Item 1, Intangible Assets / Business Combinations) before sizing any position on it** — but the presence of a large, debt-free, cash-flow-funded asset addition is a genuine strategic signal: Apple is buying capability, not just buying back stock.

### 4.5 Equity nearly jumped 46% in nine months — why it matters

Equity rose from $73,733M to $107,520M. Bridge (9M FY26):
- Net income **+101,464**
- Buybacks **−62,094**
- Dividends **−11,778**
- SBC tax withholding **−6,462**
- Stock/APIC from SBC **+7,134** ($93,568M → $100,702M)
- AOCI **+1,063** (−5,571 → −4,508)

Net effect: ~$29.3B of the $33.8B is explainable from the tagged lines, with the remainder from grant/dividend timing. **The important consequence:** ROE is now computed on a much larger, less-levered equity base, and the annualized ROE of ~149% (annualized 9M net income $135,285M ÷ average equity $90,627M) will **mechanically fall** as equity compounds — a subtle reason not to extrapolate trailing per-share growth.

---

## 5. Cash flow & capital allocation: the strongest part of the story

### 5.1 Cash flow ($M)

| Item | 9M FY26 | 9M FY25 | Δ % |
|---|---:|---:|---:|
| **Operating cash flow** | **116,996** | 81,754 | **+43.1%** |
| Capex (PP&E) | (6,799) | (9,473) | **−28.2%** |
| **Free cash flow (OCF − capex)** | **110,197** | 72,281 | **+52.5%** |
| Investing cash flow (total) | (18,811) | +17,782 | n.m. |
| Financing cash flow (total) | (94,575) | (93,210) | −1.5% |
| Net change in cash | +3,610 | +6,326 | −42.9% |
| D&A | 9,973 | 8,571 | +16.4% |
| Stock-based comp | 10,523 | 9,680 | +8.7% |
| Income taxes paid | 26,555 | 37,332 | **−28.9%** |
| Buybacks | **62,094** | 70,579 | **−12.0%** |
| Dividends paid | 11,778 | 11,559 | +1.9% |
| SBC tax withholding | 6,462 | 5,719 | +13.0% |
| LT debt repaid | 8,146 | 9,682 | −15.9% |
| Net short-term debt repaid | 5,911 | 5,690 | +3.9% |

### 5.2 Working-capital drivers inside OCF

Positive (sources): other operating assets +16,266; other operating liabilities +10,016; inventory effect +5,461 (per the tag convention this reflects a decrease, but note the **balance-sheet** inventory rose — the schedule likely nets supplier prepayments/reclassifications; treat with care).
Negative (uses): accounts receivable −8,316; other receivables −5,671; accounts payable **−5,203**.

**Quality assessment:** OCF/net income = **1.15x** (116,996/101,464) versus **0.97x** in 9M FY25. Cash conversion has improved sharply. However, ~$26B of the OCF benefit came from "other" working-capital lines rather than core receivables/payables — and **accounts payable fell $5.2B while COGS rose 11%**, i.e., supplier terms tightened or Apple prepaid. That is a **medium-term headwind to future OCF growth**, and it partially explains why cash grew only $3.6B despite $110B of FCF (the rest went to buybacks, dividends, debt repayment, and AFS securities purchases: AFS purchases of **$48,752M** vs **$17,591M** a year ago — Apple is deploying cash into its own securities portfolio at ~2.8x the prior-year pace).

Also worth flagging: **income taxes paid fell 28.9%** to $26,555M even as pre-tax income rose 23.2%. That is a large timing/tax-planning divergence from the 17.6% book ETR and is worth a footnote check — cash tax favorability this year can mean a **cash tax catch-up next year**.

### 5.3 Capital-allocation pivot — the most under-appreciated signal

| Capital return ($M) | 9M FY26 | 9M FY25 | Δ |
|---|---:|---:|---:|
| Buybacks | 62,094 | 70,579 | **−8,485 (−12.0%)** |
| Dividends | 11,778 | 11,559 | +219 |
| **Total returned** | **73,872** | **82,138** | **−8,266 (−10.1%)** |
| FCF | 110,197 | 72,281 | +37,916 |
| **Payout ratio of FCF** | **67.0%** | **113.6%** | −46.6 pt |

**Apple cut gross buybacks 12% while free cash flow rose 52%, dropping its FCF payout ratio from 114% to 67%.** That is a deliberate ~$38B annualized increase in retained liquidity. Combined with (a) the +$13.3B gross intangible step-up, (b) zero new debt issuance, and (c) the $7.6B raw-material pipeline build, the coherent read is: **Apple is accumulating financial and physical capacity for a large capital deployment — an acquisition, a product-category launch, or a supply-chain commitment.** 

**Trade implication:** this is a *positive optionality* signal, but a *negative* signal for near-term EPS-per-share accretion, because buyback-driven share-count reduction (a 2.0% tailwind in 9M FY26) is decelerating. Note the EPS math: 9M net income **+20.0%** but EPS **+22.4%** — only ~2.4 pts from buybacks. If buybacks keep shrinking, EPS growth converges to net-income growth.

**Dividend:** declared DPS $0.79 for 9M FY26 vs $0.76 (+3.9%); Q3 alone $0.27 vs $0.26 (+3.8%). Growth in line with inflation, no acceleration signal.

---

## 6. Returns, efficiency, and quality scorecard

| Metric | 9M FY26 (annualized where noted) | 9M FY25 | Comment |
|---|---:|---:|---|
| Gross margin | 49.07% (Q3: 50.06%) | 46.82% | Record territory; mean-reversion risk |
| Operating margin | 33.60% (Q3: 32.62%) | 32.08% | Expansion purely GM-driven |
| Net margin | 27.85% | 26.95% | Tax rate working against it |
| Effective tax rate | 17.58% | 15.39% | +219 bp headwind |
| OCF / net income | 1.15x | 0.97x | Quality improved |
| FCF margin | **30.2%** (110,197/364,357) | 23.0% | Exceptional |
| Capex / revenue | **1.87%** | 3.02% | Asset-lightness increasing |
| ROE (annualized) | **~149%** | — | On a rapidly growing equity base |
| Asset turnover (annualized) | ~1.31x | — | — |
| Inventory turnover (9M, on COGS) | ~22x | — | Watch the parts build |
| Revenue per $ of equity | ~4.5x annualized | — | Extreme capital efficiency |
| Annualized revenue run-rate (9M × 4/3) | **~$485.8B** | ~$418.3B | Q4 seasonally stronger ⇒ FY26 likely above this |
| Annualized net income run-rate | **~$135.3B** | ~$112.7B | — |

---

## 7. What is working — and what would break the thesis

### Bullish evidence (strong, fresh, filing-level)
1. **Growth re-acceleration at enormous scale:** +16.2% revenue growth on a $364B nine-month base. For a company of this size, that is roughly 3x the growth rate of the prior cycle era.
2. **Gross margin broke 50%** in the June quarter (50.06%, +357 bp YoY) — the clearest evidence of Services mix and pricing power.
3. **June quarter did not deleverage sequentially:** Q2 pre-tax $35.8B → Q3 pre-tax $36.3B. Normally Q3 is the seasonal trough.
4. **Free cash flow +52.5% to $110.2B in nine months**, with capex *falling* 28%.
5. **Net cash up $28.4B to $62.2B**, current ratio to 1.00x, debt down $14.3B, zero new long-term issuance.
6. **Parts inventory +260%** — a leading indicator of a major product ramp.
7. **R&D +32.5%** to 9.3% of revenue — the largest investment step-up in years, consistent with AI/silicon investment.
8. **Share count down 1.11%** in nine months; diluted shares implied ~14,748M.

### Bearish / watch items (equally specific)
1. **No operating leverage.** Opex +21.9% > revenue +16.2%. Margin expansion is 100% gross-margin dependent. **A 100 bp GM give-back ≈ $4.9B pre-tax ≈ $0.28 EPS.**
2. **Gross margin of 50%+ is a cyclical high.** Memory/component cost inflation and tariff/trade friction are the two most likely causes of a 200–300 bp reversal. This is the single biggest risk in the report.
3. **Tax rate normalization:** ETR 15.39% → 17.58%. Net income grew 20.0% vs pre-tax 23.2% — a 320 bp drag from tax alone.
4. **Buyback deceleration** (−12% YoY) removes ~2 pts of EPS growth and signals a capital-allocation pivot whose target is undisclosed.
5. **Deferred revenue / contract liability growth lagging:** total contract liability $14,900M vs $13,700M (**+8.8%**); current portion $9,538M vs $9,055M (+5.3%). Both grow far slower than total revenue (+16.2%) — a soft signal on **Services bookings momentum**, and worth watching because Services is the margin engine.
6. **Accounts payable down $5.2B** on rising COGS — tightening supplier terms / prepayment, a forward OCF headwind.
7. **Cash taxes paid fell 28.9%** while pre-tax income rose 23.2% — likely timing; expect reversal.
8. **Inventory write-down risk** if Q4 revenue does not accelerate.
9. **Unreconciled ~$13.3B gross intangible increase** — disclosure gap; verify in the 10-Q notes before treating as a positive.
10. **Information gaps that should reduce conviction:** no insider-transaction data, no segment/geographic detail, no price data for valuation. A trader cannot currently confirm whether the strong fundamentals are already priced.

---

## 8. Actionable conclusions for a trader

**Directional read (fundamentals only): constructive, with one specific point of fragility.**

1. **The fundamental momentum is real and fresh.** The 10-Q is four days old and shows the best combination of growth and margin in the dataset. There is **no stale-data excuse** to fade this — but equally, **no valuation tool available** to tell you if it's priced. Anyone taking a view here is taking a business-quality view, not a value view.

2. **The trade to express is a gross-margin trade, not a revenue trade.** Revenue growth has been rock-steady at ~16% across the nine months. The variable that moved is gross margin (+225 to +357 bp). **Position sizing should be driven by your view on GM sustainability**, because that's where 100% of the incremental operating leverage has come from. Going long here is implicitly a bet that a 50% GM holds.

3. **Set the monitoring tripwires now (before the late-October FY26 Q4 print):**
   - **Bullish confirmation:** Q4 FY26 gross margin ≥ 49%, revenue growth ≥ 16%, inventory building *alongside* accelerating revenue, R&D still >25% growth. → thesis intact, add.
   - **Bearish trigger #1:** Gross margin < 48% → operating margin compresses despite revenue growth. Exit/reduce.
   - **Bearish trigger #2:** Inventory above ~$11B *without* a corresponding September-quarter revenue acceleration → parts write-down risk. Reduce.
   - **Bearish trigger #3:** Total contract liability growth decelerating below +5% → Services bookings problem. Reassess the margin-durability assumption.
   - **Neutral/watch:** Buyback pace. If buybacks re-accelerate back above ~$25B/quarter, the capital-allocation pivot was tactical (bullish for EPS). If Apple announces a large acquisition, re-underwrite entirely.

4. **Cross-check the buyback price (inference, low confidence):** $62,094M of repurchases against a net share reduction of 164.3M (14,773.26M → 14,608.96M), while ~57.8M dilutive SBC shares were issued, implies **gross repurchases of roughly 220M shares at an average of roughly $280**. This should be treated only as a rough sanity anchor in the absence of any price feed in these tools — not as a fair-value estimate.

5. **Balance-sheet optionality is a genuine second leg of the story.** $62B net cash, rising $28B in nine months, with zero new debt issuance and a 12% buyback cut, is a company loading the spring. Historically this has preceded a capital deployment announcement. **A long-volatility stance (rather than a pure directional long) is arguably better supported by this evidence than a leveraged directional bet**, because the near-term EPS math is deteriorating (buybacks down, tax rate up) while the medium-term optionality is improving.

6. **Do not act on insider signals — there are none available.** The absence of an authorized insider archive is a data gap. Explicitly avoid reading "no reported insider sales" as insider confidence.

---

## 9. Key points summary table

| Category | Metric | Latest value | Reference | Interpretation / action |
|---|---|--:|--:|---|
| **Freshness** | Latest 10-Q period / filed | Q3 FY26 ended 2026-06-27 / filed 2026-07-31 | — | 4 days old at analysis date; no newer data |
| **Growth** | Q3 FY26 revenue | $109,417M | $94,036M (+16.4%) | Re-acceleration at scale |
| **Growth** | 9M FY26 revenue | $364,357M | $313,695M (+16.2%) | Steady mid-teens |
| **Profitability** | Q3 FY26 gross margin | **50.06%** | 46.49% (+357 bp) | Record territory; key risk |
| **Profitability** | 9M FY26 gross margin | 49.07% | 46.82% (+225 bp) | All margin gains GM-driven |
| **Profitability** | Q3 FY26 operating margin | 32.62% | 29.99% (+263 bp) | Opex grew faster than sales |
| **Profitability** | 9M FY26 operating margin | 33.60% | 32.08% (+152 bp) | No operating leverage |
| **Profitability** | Q3 FY26 net margin | 27.22% | 24.92% (+230 bp) | Tax rate eroding it |
| **Earnings** | Q3 FY26 net income | $29,789M | $23,434M (+27.1%) | Beat revenue growth |
| **Earnings** | 9M FY26 net income | $101,464M | $84,544M (+20.0%) | — |
| **Per share** | Q3 FY26 EPS diluted | $2.02 | $1.57 (+28.7%) | — |
| **Per share** | 9M FY26 EPS diluted | $6.88 | $5.62 (+22.4%) | ~2.4 pt buyback lift |
| **Expense mix** | R&D 9M FY26 | $34,035M (9.34% of rev) | $25,684M (8.19%) (+32.5%) | Largest investment ramp; watch |
| **Expense mix** | SG&A 9M FY26 | $22,315M | $20,553M (+8.6%) | Well controlled |
| **Tax** | 9M FY26 effective tax rate | 17.58% | 15.39% (+219 bp) | Headwind to EPS |
| **Cash flow** | 9M FY26 operating cash flow | $116,996M | $81,754M (+43.1%) | — |
| **Cash flow** | 9M FY26 free cash flow | **$110,197M** | $72,281M (+52.5%) | 30.2% FCF margin |
| **Quality** | OCF / net income | 1.15x | 0.97x | Earnings quality improved |
| **Efficiency** | Capex / revenue | 1.87% | 3.02% | Increasingly asset-light |
| **Balance sheet** | Net cash | **$62,173M** | $33,763M (+$28,410M) | Huge improvement |
| **Balance sheet** | Total debt | $84,344M | $98,657M (−$14,313M) | Deleveraging |
| **Balance sheet** | Current ratio | 1.003x | 0.893x | Crossed parity |
| **Balance sheet** | Debt / equity | 0.78x | 1.34x | Materially de-risked |
| **Balance sheet** | Shareholders' equity | $107,520M | $73,733M (+45.8%) | Compresses forward ROE |
| **Signal** | Inventory | $11,092M (raw materials $7,645M) | $5,718M ($2,124M) | +94% total, +260% parts → product ramp |
| **Signal** | Gross intangibles | $38,220M | $24,950M (+$13,270M) | Acquisition/asset purchase; **verify in notes** |
| **Signal** | Contract liability (deferred rev.) | $14,900M (+8.8%) | $13,700M | Lags revenue — Services watch item |
| **Capital return** | 9M FY26 buybacks | $62,094M | $70,579M (−12.0%) | Payout of FCF fell 114% → 67% |
| **Capital return** | 9M FY26 dividends | $11,778M | $11,559M (+1.9%) | Q3 DPS $0.27 (+3.8%) |
| **Capital return** | Total returned | $73,872M | $82,138M (−10.1%) | Retaining ~$38B/yr more |
| **Share count** | Shares out | 14,594.18M (2026-07-17) | 14,773.26M (2025-09-27) | −1.11% in 9M |
| **Run-rate** | Annualized revenue | ~$485.8B | ~$418.3B | FY26 likely above (Q4 seasonal) |
| **Run-rate** | Annualized net income | ~$135.3B | ~$112.7B | — |
| **Return** | ROE (annualized) | ~149% | — | Falls as equity compounds |
| **Data gap** | Insider transactions | **UNAVAILABLE** | — | Do not infer; lower conviction |
| **Data gap** | Price / valuation multiples | **UNAVAILABLE** | — | Cannot assess whether priced |
| **Bottom line** | Fundamental posture | **Constructive, GM-dependent** | — | Long = bet on 50% GM holding; tripwire at <48% |