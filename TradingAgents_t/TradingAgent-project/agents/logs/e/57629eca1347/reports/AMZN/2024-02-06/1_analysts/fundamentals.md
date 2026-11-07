# AMZN — Fundamental Research Report
**As of 2024-02-06 | Company: Amazon.com, Inc. | Latest public filing in dataset: FY2023 Form 10-K accepted 2024-02-02 (accession 0001018724-24-000008)**

---

## 1. What is new and why it matters (point-in-time)

The single most important fact for a trader on 2024-02-06 is that **Amazon's fiscal 2023 Form 10-K hit EDGAR on 2024-02-02**, i.e. four days before today's date. Every figure below is post-print and reflects the first full audited look at FY2023 (year ended 2023-12-31). Nothing in this dataset pre-dates that filing in a way that is stale — the FY2021/FY2022 comparatives are restated as presented within the same FY2023 10-K, so they are internally consistent.

Three facts define the FY2023 story:
1. **Free cash flow flipped from deeply negative to strongly positive** ($32.2B in FY2023 vs. –$16.9B in FY2022).
2. **Operating margin expanded ~400bp to 6.4%**, driven by cost-of-sales leverage, not by cutting the tech/fulfillment bucket.
3. **The balance sheet de-risked**: long-term debt down 13%, zero new long-term issuance, cash + marketable securities of ~$144B against ~$70B of debt and finance leases.

---

## 2. Income statement — revenue and the margin inflection

**Revenue is not a direct tag in this extract, so it is derived and cross-checked:** Revenue = `CostsAndExpenses` + `OperatingIncomeLoss`. This yields $574.785B (FY23), $513.983B (FY22), $469.822B (FY21), which tie exactly to Amazon's reported net sales in the FY2023 10-K. Treat revenue below as derived-but-verified.

| $M | FY2021 | FY2022 | FY2023 | YoY '23 |
|---|---|---|---|---|
| Revenue (derived) | 469,822 | 513,983 | 574,785 | **+11.8%** |
| Cost of goods & services | 272,344 | 288,831 | 304,739 | +5.5% |
| Gross profit | 197,478 | 225,152 | 270,046 | +19.9% |
| Gross margin | 42.0% | 43.8% | **47.0%** | +320bp |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| Marketing expense | 32,551 | 42,238 | 44,370 | +5.0% |
| G&A expense | 8,823 | 11,891 | 11,816 | –0.6% |
| Advertising expense (separate tag) | 16,900 | 20,600 | 20,300 | –1.5% |
| **Operating income** | 24,879 | 12,248 | **36,852** | **+200.9%** |
| Operating margin | 5.30% | 2.38% | **6.41%** | +403bp |
| Non-operating income/(expense) | 13,272 | (18,184) | 705 | n.m. |
| Pre-tax income | 38,151 | (5,936) | 37,557 | n.m. |
| Income tax | 4,791 | (3,217) | 7,120 | n.m. |
| **Net income** | 33,364 | (2,722) | **30,425** | n.m. |
| Net margin | 7.10% | –0.53% | **5.29%** | — |
| Diluted EPS | $3.24 | $(0.27) | **$2.90** | n.m. |

**Key structural read-throughs:**

- **Gross margin is the engine.** Cost of sales fell from 58.0% of revenue (FY21) to 56.2% (FY22) to **53.0% (FY23)**. That is ~$12B+ of annualized cost-of-sales leverage — consistent with fulfillment-network regionalization, lower per-unit logistics cost, and the mix contribution of high-margin AWS and advertising.
- **Operating leverage is real, but not from the big bucket.** Total opex ex-COGS was $233.2B = 40.6% of revenue vs. 41.4% in FY22. Marketing grew only 5.0% and G&A was flat/slightly down; the combined "fulfillment + technology & content + other" residual was $177.0B (30.8% of revenue) vs. 30.9% in FY22 — i.e. **flat as a percentage**. So the entire margin gain came from gross margin plus marketing/G&A discipline, while Amazon kept spending on technology/content. This is a durable-quality signal rather than a one-off cost cut.
- **Earnings quality caveat on non-operating lines.** FY2022's pre-tax loss of –$5.9B was overwhelmingly a mark-to-market artifact: equity securities FVNI swung –$13.6B in FY22 vs. +$11.6B in FY21 (the Rivian stake) and +$1.0B in FY23. Strip that out and FY2022 operating performance ($12.2B OI) was weak but profitable. For FY2023, operating income of $36.9B was ~98% of pre-tax income — **clean, operations-driven earnings**.
- **Interest: now near-neutral.** Interest expense $3,182M (FY23 vs. $2,367M) is almost fully offset by interest income $2,949M (vs. $989M). Higher rates are a two-sided exposure; the net drag alongside finance-lease interest ($304M) is small.
- **Tax rate is normalizing upward**: effective rate 12.6% (FY21) → 54.2% (FY22, on a small pre-tax base) → **19.0% FY23** ($7,120M / $37,557M). Deferred tax was still a –$5,876M benefit, and **cash taxes paid were $11,179M** — i.e. cash tax rate ~29.8% of pre-tax book income. Tax is becoming a real cash cost, a headwind to incremental EPS.
- Segments: the 10-K confirms **3 operating segments** (North America, International, AWS); segment-level revenue/operating income is not exposed in this extract.
- Advertising expense line ($20,300M) is a disclosure of Amazon's own ad spend, and it *declined* 1.5% — worth distinguishing from advertising *revenue* (a high-margin segment that this dataset does not break out).

---

## 3. Cash flow — the headline of the print

| $M | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Operating cash flow | 46,327 | 46,752 | **84,946** (+81.7%) |
| Capex (productive assets) | (61,053) | (63,645) | **(52,729)** (–17.2%) |
| **Free cash flow** | **(14,726)** | **(16,893)** | **+32,217** |
| FCF margin | –3.1% | –3.3% | **+5.6%** |
| Capex / revenue | 13.0% | 12.4% | **9.2%** |
| D&A | 34,433 | 41,921 | 48,663 |
| SBC | 12,757 | 19,621 | **24,023** |
| Investing cash flow | (58,154) | (37,601) | (49,833) |
| Financing cash flow | 6,291 | 9,718 | **(15,879)** |
| FX effect on cash | (364) | (1,093) | 403 |
| Net change in cash | (5,900) | 17,776 | 19,637 |

This is a **~$49B year-over-year swing in free cash flow** — the single strongest fundamental catalyst in the dataset. Two drivers, both structural:
- **Operating cash flow +$38.2B** on higher operating income, higher D&A (+$6.7B), higher SBC (+$4.4B), and working-capital help from deferred revenue (+$4,578M) and payables (+$5,381M). Offsets: receivables/other operating assets a $8,348M use, accrued liabilities a $2,428M use, other non-current assets a $12,265M use.
- **Capex down $10.9B** to $52.7B (9.2% of revenue) while D&A rose to $48.7B — capex/D&A is now **1.08x vs 1.52x in FY2022**, meaning the hyper-investment phase is normalizing and the depreciation tailwind is shrinking toward neutral.

**Intra-year acceleration (derived from 10-Q facts in the same dataset):** 9M2023 OCF was $42,481M; FY2023 OCF $84,946M implies **~$42.5B of operating cash flow was generated in Q4 alone** — roughly equal to the first nine months combined. Likewise 9M capex $38,141M vs. FY $52,729M implies **Q4 capex ~$14.6B** and **Q4-only FCF ~$27.9B**. The quarterly cash trajectory is steeply improving, which is the number the market re-rated on.

**Cash-flow-derived EBITDA proxy** (Operating income + D&A + SBC): $24,879 + 34,433 + 12,757 = $72.1B (15.3% margin) in FY21 → $73.8B (14.4%) in FY22 → **$109.5B (19.1%) in FY23**. Adjusted cash earnings power expanded ~$35.7B in one year.

**Conservative lenses traders should keep handy:**
- FCF less finance-lease principal ($4,384M) = **$27.8B**.
- FCF less all SBC ($24,023M) = **~$8.2B** — the true "shareholder" FCF after compensating employees in stock.
- FCF per share = **$3.10** ($32,217M / 10,383M shares) vs. diluted EPS of $2.90.

---

## 4. Balance sheet — liquidity, leverage and deferred revenue

| $M | 2021-12-31 | 2022-12-31 | 2023-12-31 |
|---|---|---|---|
| Cash & equivalents | 36,477* | 53,888 | **73,387** |
| + AFS debt securities (fair value) | n/a | n/a | **70,919** |
| Total cash + marketable securities | — | — | **~144,306** |
| Accounts receivable (net) | — | 42,360 | 52,253 (+23.4%) |
| Allowance for doubtful accounts | 1,100 | 1,400 | 1,700 |
| Accounts payable | 79,600 | 79,600 | 84,981 (+6.8%) |
| Accrued liabilities (current) | — | 62,566 | 64,709 |
| Contract liabilities (deferred revenue), total | — | 16,100 | **20,600 (+28.0%)** |
| — current / non-current | — | 13,227 / 2,900 | 15,227 / **5,700 (+96.6%)** |
| Long-term debt (carrying) | — | 67,150 | **58,314 (–13.2%)** |
| Finance lease liabilities | — | 15,783 | 12,109 |
| Operating lease liabilities | — | 69,040 | **75,639** |
| Total assets | 420,549 | 462,675 | **527,854** |
| Current assets | — | 146,791 | 172,351 |
| APIC | — | 75,066 | 99,025 |
| AOCI | — | (4,487) | (3,040) |
| Shares outstanding | — | 10,242M | **10,383M** |

\*FY2021 shown as cash + restricted cash in the dataset's cash-flow reconciliation ($36,477M); FY22/FY23 cash-only figures ($53,888M / $73,387M) are `CashAndCashEquivalentsAtCarryingValue`.

**Reads:**
- **Net cash position ~$73.9B**: cash + AFS securities $144.3B vs. debt $58.3B + finance leases $12.1B = $70.4B. Even including operating leases ($75.6B liability / $90.8B undiscounted), leverage is comfortable. Note the marketable-securities portfolio is laddered short: **$65.2B matures within one year**, so liquidity is genuinely accessible, not duration-locked (unrealized portfolio loss is de minimis: $71,265M amortized cost vs. $70,919M fair value).
- **Deferred revenue is the forward-looking gem**: non-current contract liabilities nearly doubled (+96.6% to $5,700M) and total deferred revenue rose 28.0%. Growth in long-dated deferred revenue is the closest available proxy for **committed cloud/AI contract backlog**. $12.4B of FY2023 revenue was recognized from the opening deferred balance.
- **Receivables growing faster than revenue (23.4% vs. 11.8%)** — a mild yellow flag worth monitoring (advertising and third-party seller receivables mix), though the allowance/write-off ratio is stable (write-offs $1,600M vs. $1,700M allowance).
- **Payables growth (+6.8%) lagged revenue (+11.8%)** for the first time in the dataset — Amazon has largely exhausted the "grow into payables" working-capital lever; the FY23 cash-flow beat came from profit and capex, not from stretching suppliers further.
- **Equity build**: APIC rose $23,959M (FY22: $75,066M → FY23: $99,025M), the largest component of which is the $24,023M SBC charge. Retained earnings and total stockholders' equity are **not in this extract** (see gaps) so ROE cannot be computed from the returned data.

**Debt maturity profile (face, $M)** — total long-term maturities **$67,182M**, well-laddered: $8,500 (next 12m), $5,286 (yr2), $3,146 (yr3), $8,750 (yr4), $2,250 (yr5), **$39,250 (after yr 5 = 58%)**. Total contractual obligations are $300,409M, with $39,345M due in the next 12 months and $157,824M after year five (dominated by operating leases and content/purchase commitments). Refinancing risk is low; Amazon issued **zero** long-term debt in FY2023 (vs. $21,166M in FY2022) and repaid $3,676M.

---

## 5. Capital allocation, dilution and insider signal

- **No buybacks in FY2023** ($0 repurchased; $6,000M in FY2022). Despite $32.2B of FCF, 100% of it plus balance-sheet cash went to capex, debt reduction, and leases. Capital return is a *latent* catalyst, not a current one.
- **Dilution is the hidden tax**: shares outstanding 10,242M → 10,383M (+141M, +1.4% YoY), with 1.6B shares reserved for future issuance and **$18.3B of unrecognized SBC cost** still to be expensed. SBC of $24,023M equals 4.2% of revenue and 79% of net income. SBC grew +22.4% YoY vs. revenue +11.8% — growing faster than the business, and a real drag on per-share value creation.
- **Share count as of 2024-01-24: 10,387,381,291** (post year-end, already higher than the 2023-12-31 count) — use this for any per-share work.
- **Public float was $1.1837T at 2023-06-30.**
- **Insider transactions: NOT AVAILABLE.** The vendor explicitly reports no authorized, point-in-time insider-transactions archive for AMZN as of 2024-02-06. **No insider buying or selling inference should be drawn — none is fabricated here.** This is a genuine blind spot in this report.

---

## 6. Explicit data gaps (do not over-read this dataset)

1. **No quarterly income statement granularity.** All income-statement facts returned are FY (10-K) periods. Q4 revenue, Q4 operating income, and quarterly margin progression **cannot be computed** from this extract; only cash-flow and selected 10-Q items (9M/quarterly) exist. My Q4 cash-flow figures are *derived* (FY minus 9M) and labeled as such.
2. **Missing balance-sheet lines**: total current liabilities, total liabilities, retained earnings/total equity, inventories, goodwill, property & equipment. Consequently current ratio, ROE, book value per share, and segment ROIC are not computable here.
3. **No price data** is returned by these tools, so P/E, EV/EBITDA, P/FCF multiples cannot be derived in this report. Anchors for the trader to apply: **FY23 diluted EPS $2.90**, **FCF/share $3.10**, **EBITDA-proxy $109.5B**, **10,387M shares out**.
4. **No insider data** (see above).
5. Revenue line is **derived** (verified against reported totals) because the revenue tag is absent from the extract.

---

## 7. Actionable insights for traders

**Bullish evidence (high conviction, directly from the filing):**
1. **FCF regime change is the trade.** +$49B YoY FCF swing to +$32.2B, with ~$27.9B of it generated in Q4 alone. If the capex discipline of FY23 (9.2% of revenue vs. 12.4%) persists for even two quarters, consensus FCF estimates are too low. FCF is now the primary valuation driver for AMZN, and it just inflected.
2. **Gross-margin expansion is structural, not a one-off.** Cost of sales down 320bp in FY23 after 180bp in FY22, while tech/content spend stayed flat as a % of revenue — this is operating leverage from logistics efficiency plus mix, and it should persist into FY24.
3. **Forward-looking backlog signal:** non-current deferred revenue +96.6%, total deferred revenue +28%. Best-in-class evidence that enterprise cloud/AI commitments are inflecting.
4. **Balance sheet optionality:** ~$73.9B net cash, $65.2B of securities maturing inside 12 months, zero new LT debt issued, debt down 13%. This funds AI capex *or* a future buyback without dilution or rating pressure.
5. **Earnings quality improved:** 98% of FY23 pre-tax income came from operations vs. FY22 when a –$13.6B equity mark-to-market masked the operating picture. "Cleaner" earnings deserve a higher multiple.

**Bearish / risk evidence (equally from the data):**
1. **Capex may have bottomed.** Capex fell 17% but D&A rose 16% — the depreciation tailwind is fading (capex/D&A now 1.08x). Any re-acceleration of AI infrastructure spend (the explicitly flagged forward risk) reverses the FCF story quickly, because FCF is levered ~1:1 to capex.
2. **Dilution and SBC are eating the FCF.** +1.4% share count, $24.0B SBC (79% of net income), $18.3B unrecognized. Post-SBC FCF is only ~$8.2B. Per-share value creation is far weaker than headline FCF suggests.
3. **No capital return** — $0 buyback in FY23 limits downside support and signals management still prioritizes reinvestment.
4. **Tax normalization** (12.6% → 19.0% effective; $11.2B cash taxes) and a higher-rate environment cap incremental EPS growth.
5. **Receivables +23.4% vs. revenue +11.8%**, and payables now growing slower than revenue — the working-capital tailwind is largely spent.
6. **Off-balance-sheet-style obligations are large:** operating leases $75.6B (undiscounted $90.8B) and total contractual obligations $300.4B ($39.3B due within 12 months). Cheap-ish but real claims on future FCF.

**Trade construction implications:**
- The **post-print drift setup is favorable**: a fresh 10-K (Feb 2) revealing a margin + FCF inflection is a fundamental re-rating event, and the data supports staying long into subsequent quarters *unless* capex guidance re-accelerates.
- **Monitor these three items as the thesis tripwires:** (a) quarterly capex trajectory, (b) non-current deferred revenue growth (backlog), (c) SBC growth vs. share count. If capex rises >10% while deferred revenue decelerates, the FCF story breaks — that is the exit signal.
- **Valuation work must be done outside this dataset** (no price feed). Use EPS $2.90 and FCF/share $3.10 as the denominators; a FCF-multiple framework is now more appropriate than a P/E framework given the inflection.
- **Do not read anything into insider flows** — the data is simply unavailable, and absence of data is not evidence of absence of selling.

---

## 8. Key points summary table

| Category | Metric | FY2021 | FY2022 | FY2023 | Signal |
|---|---|---|---|---|---|
| **Scale** | Revenue (derived) | $469.8B | $514.0B | **$574.8B** | +11.8% YoY, re-accelerated |
| **Profit** | Gross margin | 42.0% | 43.8% | **47.0%** | +320bp, structural |
| | Operating income | $24.9B | $12.2B | **$36.9B** | +201% YoY |
| | Operating margin | 5.30% | 2.38% | **6.41%** | +403bp |
| | Net income | $33.4B | $(2.7)B | **$30.4B** | 98% ops-driven in FY23 |
| | Diluted EPS | $3.24 | $(0.27) | **$2.90** | Clean beat vs FY22 |
| **Cash** | Operating cash flow | $46.3B | $46.8B | **$84.9B** | +81.7% |
| | Capex | $61.1B | $63.6B | **$52.7B** | –17.2%, 9.2% of rev |
| | **Free cash flow** | $(14.7)B | $(16.9)B | **+$32.2B** | **~$49B swing — core thesis** |
| | FCF/share / FCF ex-SBC | — | — | $3.10 / ~$8.2B | SBC is the dilution tax |
| | Q4-implied OCF / FCF (derived) | — | — | ~$42.5B / ~$27.9B | Steep intra-year ramp |
| **Balance sheet** | Cash + securities | — | — | **~$144.3B** | $65.2B matures <1yr |
| | LT debt (carrying) | — | $67.2B | **$58.3B** | –13.2%; $0 new LT issued |
| | Net cash (ex-op leases) | — | — | **~$73.9B** | Fortress |
| | Deferred revenue (total) | — | $16.1B | **$20.6B** | +28%; non-current +96.6% |
| | Operating lease liabilities | — | $69.0B | **$75.6B** | Real claim on FCF |
| | Total assets | $420.5B | $462.7B | **$527.9B** | +14.1% |
| **Capital** | SBC | $12.8B | $19.6B | **$24.0B** | 4.2% of rev, +22.4% |
| | Share count | — | 10,242M | **10,383M** (+1.4%) | 10,387.4M @ 1/24/24 |
| | Buybacks | $0 | $6.0B | **$0** | No capital return |
| | Cash taxes paid | $3.7B | $6.0B | **$11.2B** | Tax headwind building |
| | Capex / D&A | 1.77x | 1.52x | **1.08x** | Depreciation tailwind fading |
| **Segments** | Operating segments | — | — | **3** (NA, Int'l, AWS) | Segment P&L not in extract |
| **Data gaps** | Insider transactions | — | — | **UNAVAILABLE** | No inference permitted |
| | Price / multiples | — | — | **Not provided** | Use $2.90 EPS, $3.10 FCF/sh |

**Bottom line for AMZN (as of 2024-02-06):** The FY2023 10-K, filed four days ago, documents a genuine inflection — free cash flow swung from –$16.9B to +$32.2B on a 400bp operating-margin expansion, a 13% debt reduction, and a near-$74B net cash position, with a steeper Q4 ramp than the full-year figures suggest. The offsetting risks are equally concrete: capex appears to have bottomed (capex/D&A at 1.08x), $24.0B of SBC drove 1.4% dilution with no offsetting buyback, and the payables/receivables working-capital tailwind is exhausted. The fundamental case is long-biased on FCF durability, with three tripwires to watch: capex re-acceleration, deferred-revenue deceleration, and SBC growth above revenue growth. Insider transaction data and price/multiple data are not available from these tools, and no conclusions are drawn on either.