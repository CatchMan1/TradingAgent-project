# AMZN — Fundamental Research Report
**Company:** Amazon.com, Inc. (AMZN) · **Analysis date:** 2024-02-13
**Primary source:** FY2023 Form 10-K (accession 0001018724-24-000008, filed/accepted 2024-02-02), plus YTD-9M FY2023 Form 10-Q (filed 2023-10-27) for intra-year derivation. All figures below are point-in-time and only reflect facts *publicly accepted by 2024-02-13*.

---

## 1. Data provenance, scope, and limitations (read first)

| Item | Status |
|---|---|
| FY2021 / FY2022 / FY2023 annual P&L, balance sheet, cash flow | ✅ Full detail from 10-K |
| Q1–Q3 2023 *YTD* (9-month) cash flow | ✅ From Q3 10-Q (2023-10-27) |
| Q4 2023 standalone results | ⚠️ Not a separate XBRL tag in the extract — **derived** where possible (10-K FY minus 9M 10-Q YTD) |
| Net sales line item | ⚠️ Tag not returned in extract (alphabetical truncation). **Derived arithmetically** as `CostsAndExpenses + OperatingIncomeLoss` — verified to reconcile to reported totals for all three years |
| Inventory / property & equipment / retained earnings lines | ⚠️ Not returned in extract; not estimated |
| Insider transactions | ❌ **DATA_UNAVAILABLE** — no authorized point-in-time insider archive for AMZN. No insider inference is made anywhere in this report |

**Derivation check (validates the revenue method):** FY23 $537.933B + $36.852B = **$574.785B**; FY22 $501.735B + $12.248B = **$513.983B**; FY21 $444.943B + $24.879B = **$469.822B**. These tie exactly to AMZN's reported net sales.

---

## 2. Company profile (as of the FY2023 10-K)

Amazon reports **three operating segments** (`NumberOfOperatingSegments` = 3):

1. **North America** — online & physical stores, third-party seller services (1P/3P retail, FBA), Prime subscriptions, advertising, devices.
2. **International** — same portfolio outside North America (historically lower-margin/loss-making, now approaching breakeven).
3. **AWS** — compute, storage, database, analytics, ML/AI (SageMaker, Bedrock, Trainium/Inferentia silicon), plus a large backlog of committed enterprise contracts.

**Structural facts from the filing:**
- Common stock: $0.01 par; 100B shares authorized; **10,898M issued / 10,383M outstanding** at 2023-12-31; **10,387,381,291 shares outstanding as of 2024-01-24**.
- **Public float of $1.1837 trillion as of 2023-06-30** — a hard, filing-based valuation anchor (note: stale by ~7 months; use only as an order-of-magnitude reference).
- **No dividend. Zero share repurchases in FY2023** (vs. $6.0B in FY2022, $0 in FY2021) — capital allocation remains fully reinvestment-led.
- 1.6B shares reserved for future issuance; $18.3B of unrecognized SBC cost at year-end.

---

## 3. Income statement — the margin inflection is the whole story

### 3.1 Three-year P&L (USD billions, FY, from 10-K)

| Line | FY2021 | FY2022 | FY2023 | YoY '23 |
|---|---:|---:|---:|---:|
| Net sales (derived) | 469.822 | 513.983 | **574.785** | **+11.8%** |
| Cost of goods & services sold | 272.344 | 288.831 | 304.739 | +5.5% |
| **Gross profit** | **197.478** | **225.152** | **270.046** | **+19.9%** |
| Gross margin | 42.03% | 43.81% | **46.98%** | +317 bps |
| Total costs & expenses | 444.943 | 501.735 | 537.933 | +7.2% |
| **Operating income** | **24.879** | **12.248** | **36.852** | **+200.9%** |
| **Operating margin** | 5.30% | 2.38% | **6.41%** | +403 bps |
| Non-operating income/(expense) | 13.272 | (18.184) | 0.705 | n.m. |
| Pretax income | 38.151 | (5.936) | **37.557** | n.m. |
| Income tax | 4.791 | (3.217) | 7.120 | +321% |
| Effective tax rate | 12.6% | 54.2% (benefit) | **19.0%** | +640 bps |
| **Net income** | **33.364** | **(2.722)** | **30.425** | n.m. |
| Net margin | 7.10% | (0.53%) | **5.29%** | +582 bps |
| **Diluted EPS** | **$3.24** | **$(0.27)** | **$2.90** | n.m. |
| Basic EPS | $3.30 | $(0.27) | $2.95 | n.m. |

**Key insight #1 — operating income tripled (+201%) while revenue grew 11.8%.** This is the single most important fact in the dataset. The FY2022 collapse (op margin 2.38%) was fully reversed and exceeded (6.41% vs. 5.30% in FY2021). Operating leverage came from *cost growth (7.2%) running at ~60% of revenue growth (11.8%)*.

**Key insight #2 — gross margin expanded 317 bps to 46.98%.** COGS grew only 5.5% against 11.8% revenue growth. Drivers visible in the data: (a) mix shift toward high-margin **third-party seller services + advertising + AWS**, (b) fulfillment/logistics cost efficiency after the 2023 regionalization overhaul, (c) declining unit cost of AWS infrastructure as capex digestion kicked in. Gross profit dollars rose $44.9B (+19.9%) — this, not opex cuts, supplied the majority of the operating income increase.

### 3.2 Cost structure decomposition (USD billions; % of derived revenue)

| Cost line | FY2021 | % rev | FY2022 | % rev | FY2023 | % rev |
|---|---:|---:|---:|---:|---:|---:|
| COGS (products + services) | 272.344 | 57.97% | 288.831 | 56.19% | 304.739 | **53.02%** |
| All other operating costs* | 172.599 | 36.73% | 212.904 | 41.42% | 233.194 | **40.57%** |
| — Depreciation & amortization | 34.433 | 7.33% | 41.921 | 8.16% | 48.663 | **8.47%** |
| — Share-based compensation | 12.757 | 2.72% | 19.621 | 3.82% | 24.023 | **4.18%** |
| — Marketing | 32.551 | 6.93% | 42.238 | 8.22% | 44.370 | 7.72% |
| — Advertising (promotional) | 16.900 | 3.60% | 20.600 | 4.01% | 20.300 | 3.53% |
| — G&A | 8.823 | 1.88% | 11.891 | 2.31% | 11.816 | **2.06%** |
| — Operating lease cost | 7.199 | 1.53% | 8.847 | 1.72% | 10.550 | 1.84% |
| — Finance lease ROU amortization | 9.857 | 2.10% | 6.097 | 1.19% | 5.899 | 1.03% |
| — Amortization of intangibles | 0.512 | 0.11% | 0.604 | 0.12% | 0.706 | 0.12% |

\*Derived: `CostsAndExpenses − COGS`.

**Reading the structure:**
- **G&A is flat in dollars ($11.82B vs $11.89B) and fell to 2.06% of revenue** — hard evidence of the 2023 corporate cost reduction (27k layoffs, hiring freeze). This is a rare structural opex cut at Amazon, not a one-off.
- **Marketing fell as a % of revenue (8.22% → 7.72%)** despite dollar growth — media efficiency.
- **D&A is the structural headwind: 8.47% of revenue and rising** (+$6.7B, +16.1% YoY) as the 2021–22 capex binge depreciates. This will keep climbing in 2024 regardless of demand.
- **SBC is a real, growing cost: $24.0B, 4.18% of revenue**, up 22.4% YoY and 88% since 2021. Non-GAAP op margin overstates cash economics by roughly this amount.

### 3.3 The non-operating swing — a fading EPS tailwind

| Item | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Non-operating income/(expense) | 13.272 | (18.184) | 0.705 |
| — Equity securities FV gains/(losses) (e.g., Rivian stake) | 11.600 | (13.600) | 1.000 |
| — Marketable securities unrealized G/L | 11.526 | (13.870) | 0.984 |
| — Interest income | 0.448 | 0.989 | **2.949** |
| — Interest expense | 1.809 | 2.367 | **3.182** |
| — FX transaction G/L | (0.055) | (0.340) | 0.065 |
| Net interest (income − expense) | (1.361) | (1.378) | **(0.233)** |

**Critical for 2024 modeling:** in FY2021 and FY2022, non-operating items *dominated* EPS (contributing +$13.3B then −$18.2B). In FY2023 the swing factor evaporated to just +$0.705B. **The $18.9B YoY improvement in non-operating income accounted for ~all of the pretax improvement beyond operations** — meaning FY2024 EPS growth must now come *purely from operating margin*, with no "Rivian mark" cushion. Conversely, downside risk: a renewed mark-to-market loss on equity stakes would hit reported EPS with no cash impact. Interest is now roughly self-funding (income $2.95B vs expense $3.18B), a big improvement from 2021 (−$1.36B net drag).

**Tax:** effective rate normalized to **19.0%** (from 12.6% in FY2021), with cash taxes paid jumping to **$11.179B** (+85% YoY) from $6.035B. FY2023 benefited from $2.362B of tax credits and $1.429B of FDII benefit; there was also a $0.6B prior-year benefit. Watch: the deferred tax asset for **IPR&D nearly doubled to $14.8B from $6.8B**, and net deferred tax assets rose to $45.8B — a signal of significant intangible/acquired-IP investment (AI-related), but also a source of future rate volatility.

---

## 4. Cash flow — the FCF inflection, and the Q4 acceleration

### 4.1 Annual cash flow (USD billions)

| Item | FY2021 | FY2022 | FY2023 | YoY |
|---|---:|---:|---:|---:|
| **Operating cash flow** | 46.327 | 46.752 | **84.946** | **+81.7%** |
| CFO margin (% of sales) | 9.86% | 9.10% | **14.78%** | +568 bps |
| Purchases of productive assets (capex) | (61.053) | (63.645) | **(52.729)** | −17.2% |
| Capex % of revenue | 13.00% | 12.38% | **9.17%** | −321 bps |
| **Free cash flow (CFO − capex)** | **(14.726)** | **(16.893)** | **+32.217** | **+$49.1B swing** |
| Capex / D&A | 1.77× | 1.52× | **1.08×** | — |
| Investing cash flow | (58.154) | (37.601) | (49.833) | — |
| Financing cash flow | 6.291 | 9.718 | **(15.879)** | n.m. |
| Net change in cash (incl. FX) | (5.900) | 17.776 | 19.637 | — |
| CFO / net income | 1.39× | n.m. | **2.79×** | — |

**Key insight #3 — the two-sided FCF engine.** FY2023 FCF flipped from **−$16.9B to +$32.2B**, a $49B swing, delivered by *both* levers simultaneously: CFO +$38.2B (+81.7%) **and** capex −$10.9B (−17.2%). Capex is now only **1.08× D&A** — i.e., Amazon is spending barely above maintenance for the first time in years, meaning the 2021–22 buildout is being *harvested*. This is the highest-quality earnings/FCF data point in the entire dataset.

**Key insight #4 — cash conversion is exceptional.** CFO of $84.9B against net income of $30.4B = **2.79×**, driven by $48.7B D&A, $24.0B SBC, and $8.3B of non-cash/working-capital effects. Even haircutting SBC ($24.0B) fully, "cash-clean" FCF would be ~$8.2B — thin but positive, a massive improvement from −$16.9B. Note that FCF of $32.2B includes heavy non-cash SBC and D&A add-backs; **capex net of the $24B stock-comp expense is the honest reinvestment bar**.

**Key insight #5 — Q4 2023 was a blowout quarter for cash (derived).**
- Q4 CFO = FY $84.946B − 9M $42.481B = **$42.465B** — i.e., **one quarter produced 50% of full-year operating cash flow**, and 2.0× the entire first nine months.
- Q4 capex = $52.729B − $38.141B = **$14.588B** — i.e., **27.7% of the year's capex in one quarter, and above the 9M average of $12.7B/quarter.** Annualized, Q4 capex = ~$58B.
- **Implication:** Q4 CFO of $42.5B annualizes to ~$170B; even at half that run-rate, FY2024 FCF is structurally far above FY2023. **But the Q4 capex step-up is the single biggest 2024 risk** — if the $14.6B/quarter pace persists or accelerates (AI/data-center/Anthropic), the FCF inflection slows materially.

### 4.2 Capital structure activity
- **No long-term debt issued in FY2023** (vs. $21.166B FY2022, $19.003B FY2021).
- LT debt repaid $3.676B; **short-term borrowings net −$7.548B** ($18.129B drawn vs. $25.677B repaid).
- Finance lease principal payments $4.384B (vs. $7.941B FY2022) — deliberate deleveraging of the lease book.
- **$0 buybacks, $0 dividends.** Financing outflow of $15.879B is entirely debt/lease paydown.

---

## 5. Balance sheet — Amazon is now net-cash

### 5.1 Balance sheet (USD billions, as of 12-31)

| Item | 2022 | 2023 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 53.888 | **73.387** | +36.2% |
| Accounts receivable, net | 42.360 | 52.253 | +23.4% |
| **Total current assets** | **146.791** | **172.351** | **+17.4%** |
| **Total assets** | **462.675** | **527.854** | **+14.1%** |
| Accounts payable | 79.600 | 84.981 | +6.8% |
| Accrued liabilities | 62.566 | 64.709 | +3.4% |
| Contract liabilities (deferred revenue), total | 16.100 | **20.606** | **+28.0%** |
| — current | 13.227 | 15.227 | +15.1% |
| — noncurrent | 2.900 | 5.700 | **+96.6%** |
| Operating lease liability (total) | 69.040 | 75.639 | +9.6% |
| — current | 7.458 | 8.419 | +12.9% |
| Finance lease liability (total) | 15.783 | 12.109 | −23.3% |
| Long-term debt (carrying) | 67.150 | **58.314** | **−13.2%** |
| Common stock + APIC | 75.174 | 99.134 | +31.9% |
| — Additional paid-in capital | 75.066 | **99.025** | +31.9% |
| Accumulated other comprehensive loss | (4.487) | (3.040) | +$1.45B |
| Shares outstanding (M) | 10,242 | 10,383 | +1.4% |

### 5.2 Derived liquidity & leverage metrics

| Metric | 2022 | 2023 | Comment |
|---|---:|---:|---|
| Cash + marketable securities | ~54.0* | **~73.4+** | cash up $19.5B |
| Total debt + finance leases | 82.933 | **70.423** | −$12.5B (−15.1%) |
| **Net debt / (net cash)** | **+29.045** | **(2.964)** | **flipped to net cash** |
| Cash / total assets | 11.6% | 13.9% | |
| Current ratio | 1.32× | 1.31× | stable |
| Working capital | 14.775 | 22.150 | +$7.4B |
| ROE (NI / est. equity ~201.9) | n.m. | **~15.1%** | vs. negative in FY22 |
| ROA | (0.59%) | **5.76%** | |
| Approx. ROIC (NOPAT/invested capital) | ~5.4% | **~15.0%** | 19% tax-effected op income |
| Allowance for doubtful AR | 1.400 (3.3% of AR) | 1.700 (3.3% of AR) | stable credit quality |

\*Marketable-securities line item not separately returned in the extract; cash-and-equivalents only shown for strict accuracy.

**Key insight #6 — the balance sheet flipped from $29.0B net debt to ~$3.0B net cash in twelve months**, on combined debt paydown (−$12.5B) and cash build (+$19.5B). Combined with the $32.2B FCF, this creates genuine strategic optionality that did not exist a year ago: capacity to fund the AI capex cycle (Anthropic, Trainium, data centers), resume buybacks, or initiate a dividend — **none of which are in the reported numbers yet, and all of which are un-priced catalysts**.

**Key insight #7 — deferred revenue (contract liabilities) +28%, with the *non-current* portion nearly doubling (+96.6% to $5.7B).** This is the clearest evidence of multi-year enterprise commitment growth at AWS — long-dated prepaid/committed contracts. Watch this line as a leading indicator of AWS backlog conversion.

**Caveat on leverage:** the off-balance-sheet-ish obligations are large. **Total contractual obligations = $300.409B**, of which only $39.345B (13.1%) is due within 12 months and **$157.824B (52.5%) is due beyond five years**. Undiscounted operating lease payments total $90.777B (vs. $75.639B carrying), and LT debt maturities run $8.5B (yr 1), $5.286B (yr 2), $3.146B (yr 3), $8.75B (yr 4), $2.25B (yr 5), $39.25B (beyond 5 yrs). **The maturity wall is comfortably distant and back-end loaded** — no near-term refinancing risk, especially with $73.4B cash.

---

## 6. Insider transactions

**DATA_UNAVAILABLE.** The data package contains no authorized, point-in-time insider-transactions archive for AMZN as of 2024-02-13. No insider buying, selling, or 10b5-1 activity is inferred or fabricated here. Traders should source Form 4 data directly; the only filing-adjacent capital signals available in this dataset are: **(1) zero buybacks in FY2023**, **(2) $24.0B of SBC (+22% YoY) with 1.4% net share growth**, and **(3) 1.6B shares reserved for future issuance** — i.e., management is being compensated in equity while not repurchasing stock, a mild dilution headwind to per-share metrics.

---

## 7. Fundamental risks (ordered by materiality to the next 12 months)

1. **Capex re-acceleration (highest).** Q4 2023 capex of $14.6B (derived) is 15% above the 9M average quarter. A full-year 2024 capex run-rate above ~$60B would consume most of the FCF windfall and could re-compress FCF to near zero if CFO growth stalls. The FY2023 FCF boom is *partly* a capex-holiday artifact (capex/D&A = 1.08×), not purely an earnings story.
2. **D&A creep.** D&A already 8.47% of revenue and rising with the 2021–22 asset base plus new AI capex. Every incremental $10B of capex adds ~$1.5–2B of annual D&A within 3–5 years — a mechanical drag on the operating margin Amazon just fixed.
3. **No more non-operating cushion.** FY2023's EPS included a $18.9B non-operating swing vs. FY2022. FY2024 has no such comparable benefit. Operating margin must carry 100% of the growth.
4. **SBC dilution and the absence of buybacks.** $24.0B SBC = 4.18% of revenue; shares +1.4%/yr. Buybacks are the obvious offset but have not begun.
5. **Regulatory.** The FTC's monopolization suit (filed Sept 2023) and EU DMA obligations create long-tail structural risk to the third-party/ads flywheel that drives the gross-margin expansion.
6. **AWS/AI competitive intensity.** Azure and GCP AI workloads could force pricing or drive up infrastructure spend ahead of revenue (visible as rising IPR&D deferred tax assets, $14.8B).
7. **Consumer/retail elasticity.** AR +23% and contract liabilities +28% are healthy, but a weak consumer would hit the high-margin 3P/ads mix that is doing the margin work.
8. **Tax rate drift.** 19.0% in FY2023 is favorable (tax credits $2.36B, FDII $1.43B, prior-year $0.6B). Normalization toward the 21% statutory rate would be a ~$0.7B EPS headwind.

---

## 8. Actionable insights for traders

**Bull case (high conviction, evidence-based):**
- **The margin story is real and mechanical, not narrative.** Op margin 2.38% → 6.41% (+403 bps) with COGS/revenue falling 317 bps and G&A dollars *flat*. Cost growth (7.2%) at 61% of revenue growth (11.8%) is the definition of operating leverage. Trade this as a **multiple-expansion** story: each 100 bps of op margin at $575B revenue ≈ $5.75B of operating income ≈ ~$4.6B of net income ≈ **~$0.45 of EPS per 100 bps**.
- **FCF is the cleanest catalyst.** $49B YoY FCF swing combined with a net-cash balance sheet. Historically AMZN re-rates on FCF inflections, not EPS. Use **CFO margin (14.78%, +568 bps)** and **capex/revenue (9.17%, −321 bps)** as the two variables that must hold for the thesis.
- **Net cash (~$3.0B) + $73.4B liquidity** creates un-modeled optionality: buyback resumption is a near-term positive surprise that has not happened in 3 quarters (zero in FY2023 vs. $6B in FY2022).
- **Deferred revenue +28% (non-current +97%)** is early-cycle evidence for AWS reacceleration into 2024 — position early on this leading indicator.

**Bear case / triggers to reduce exposure:**
- **Watch quarterly capex.** Q4'23 capex of $14.6B (derived) vs. $12.7B 9M average. Two consecutive quarters above ~$16B puts FY2024 FCF below ~$20B and breaks the re-rating thesis.
- **Do not pay for non-operating gains.** Equity-securities MTM was only +$1.0B in FY2023 vs. +$11.6B FY2021. A renewed mark-to-market loss (e.g., Rivian, private AI stakes) hits reported EPS at zero cash cost.
- **SBC-adjusted FCF is thin (~$8B ex-SBC)**, so valuation support rests on GAAP-plus-go-forward-margin, not on current cash yield.

**Key monitoring dashboard (next 2 quarters):**
1. Quarterly CFO ≥ ~$25B (vs. $18B average ex-Q4).
2. Quarterly capex ≤ ~$15B.
3. Operating margin ≥ 6.5% (Q4'23 run-rate ~7.8%).
4. Non-current contract liabilities > $5.7B (sequential growth = AWS backlog).
5. First buyback authorization in FY2024 (none in FY2023).
6. Cash taxes paid trajectory ($11.2B in FY2023 — models assuming 15% should haircut EPS ~4%).

---

## 9. Key metrics summary table

| Category | Metric | FY2021 | FY2022 | FY2023 | Assessment |
|---|---|---:|---:|---:|---|
| **Scale** | Net sales (derived, $B) | 469.8 | 514.0 | 574.8 | +11.8% YoY |
| **Growth** | Revenue growth | — | +9.4% | **+11.8%** | Acceleration |
| **Profitability** | Gross margin | 42.0% | 43.8% | **47.0%** | +317 bps, structural mix |
| | Operating income ($B) | 24.9 | 12.2 | **36.9** | +201% YoY |
| | Operating margin | 5.30% | 2.38% | **6.41%** | +403 bps |
| | Net income ($B) | 33.4 | (2.7) | **30.4** | Recovered |
| | Net margin | 7.10% | (0.53%) | **5.29%** | Fully recovered ex-MTM |
| | Diluted EPS | $3.24 | $(0.27) | **$2.90** | 90% of FY21 peak |
| **Cost discipline** | G&A ($B / % rev) | 8.8 / 1.88% | 11.9 / 2.31% | 11.8 / **2.06%** | Flat dollars — genuine cut |
| | Marketing % rev | 6.93% | 8.22% | 7.72% | Efficiency |
| | SBC ($B / % rev) | 12.8 / 2.72% | 19.6 / 3.82% | 24.0 / **4.18%** | Rising drag |
| | D&A % rev | 7.33% | 8.16% | **8.47%** | Rising headwind |
| **Cash** | CFO ($B) | 46.3 | 46.8 | **84.9** | +81.7% |
| | CFO margin | 9.86% | 9.10% | **14.78%** | +568 bps |
| | Capex ($B) / % rev | 61.1 / 13.0% | 63.6 / 12.4% | 52.7 / **9.17%** | Deleveraging spend |
| | **FCF ($B)** | (14.7) | (16.9) | **+32.2** | **+$49.1B swing** |
| | Capex / D&A | 1.77× | 1.52× | **1.08×** | Near maintenance |
| | CFO / net income | 1.39× | n.m. | **2.79×** | Excellent conversion |
| | Q4'23 CFO (derived) | — | — | **42.5** | 50% of FY in one quarter |
| | Q4'23 capex (derived) | — | — | **14.6** | **Key 2024 risk** |
| **Balance sheet** | Cash ($B) | 36.5* | 53.9 | **73.4** | +36% |
| | LT debt ($B) | — | 67.2 | **58.3** | −13% |
| | Debt + fin. leases | — | 82.9 | **70.4** | −$12.5B |
| | **Net debt / (cash)** | — | **+29.0** | **(3.0)** | **Flipped to net cash** |
| | Total assets ($B) | 420.5 | 462.7 | **527.9** | +14.1% |
| | Contract liabilities ($B) | — | 16.1 | **20.6** | +28% (noncurrent +97%) |
| | Contractual obligations | — | — | **300.4** | 52.5% beyond 5 yrs |
| **Returns / capital** | ROE | 9.5% | n.m. | **~15.1%** | Restored |
| | ROA | 7.9% | (0.6%) | **5.76%** | Restored |
| | Approx. ROIC | ~7.3% | ~5.4% | **~15.0%** | Strong inflection |
| | Buybacks | $0 | $6.0B | **$0** | Unused lever |
| | Dividend | None | None | **None** | Unused lever |
| | Shares out (M) | — | 10,242 | 10,383 | +1.4% dilution |
| **Tax** | Effective rate | 12.6% | 54.2% ben. | **19.0%** | Normalizing |
| | Cash taxes paid ($B) | 3.69 | 6.04 | **11.18** | +85% |
| **Valuation anchor** | Public float (2023-06-30) | — | — | **$1.184T** | Filing-based, stale |
| **Insider data** | Transactions | — | — | — | **UNAVAILABLE** |

\*2021 cash shown as cash & equivalents + restricted ($36.477B per cash-flow reconciliation).

---

## 10. Bottom line for the trader

AMZN's FY2023 10-K (filed 2024-02-02) documents a **genuine, broad-based fundamental inflection**: revenue growth *accelerated* to 11.8% while cost growth decelerated to 7.2%, producing a **+403 bps operating margin expansion, a tripling of operating income, and a $49B swing to positive FCF** — accompanied by a **balance sheet flip from $29B net debt to ~$3B net cash**. These are hard, reconciled, cash-backed facts, not management narrative.

The two things to underwrite before adding exposure are (1) **capex discipline**, where the derived Q4 2023 step-up to $14.6B is a warning that the FCF holiday may close, and (2) **the absence of any non-operating cushion** — FY2023 EPS was flattered by a $18.9B non-operating swing versus FY2022 that has now reversed, so FY2024 must be earned entirely on operating margin. Upside optionality is real and un-priced: **$73.4B cash, ~$3B net cash, zero buybacks in FY2023, and a $300B contractual obligation base that is only 13% due within a year.** Insider flow cannot be assessed (data unavailable) — do not substitute an assumption.