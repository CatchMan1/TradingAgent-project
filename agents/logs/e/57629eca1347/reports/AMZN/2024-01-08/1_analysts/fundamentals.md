# AMZN — Fundamental Deep Dive
**As of 2024-01-08 | Instrument: AMZN (Amazon.com, Inc.)**

---

## 0. Critical Data-Vintage Note (read first)

All fundamentals below are **point-in-time SEC facts with EDGAR acceptance timestamps ≤ 2024-01-08**. The most recent filing available is the **Q3 2023 Form 10-Q, accepted 2023-10-27** (accession 0001018724-23-000018). Therefore:

- The **latest reported period is the quarter ended 2023-09-30**, with 9M-2023 and prior-year comparatives.
- **Q4/FY2023 results (reported Feb 1, 2024) are NOT in this dataset.** We are sitting in the gap between the Q3 print and the Q4 print (~3 weeks out) — the single most important framing point for a trader.
- Insider transactions: **DATA_UNAVAILABLE** — no authorized, point-in-time insider archive exists for AMZN by 2024-01-08. No insider conclusions should be drawn; none are fabricated here.
- No price/valuation feed is provided by these tools, so **no P/E, EV/EBITDA, or FCF-yield multiples are quoted**.

---

## 1. Company Profile

**Amazon.com, Inc. (AMZN)** is the world's largest e-commerce and cloud-infrastructure company, organized into **three operating segments** (confirmed in the filing: `NumberOfOperatingSegments = 3`):

1. **North America** — online and physical retail, third-party marketplace (1P + 3P), Prime subscription, advertising, logistics/fulfillment-as-a-service.
2. **International** — the same retail/marketplace/advertising model across Europe, Japan, and other geographies; historically lower-margin and longer to break even.
3. **Amazon Web Services (AWS)** — cloud compute, storage, database, and AI/ML infrastructure and services; the company's profit engine and highest-margin business.

Supporting engines: **advertising** (high-margin, embedded in retail segments), **devices** (Echo, Kindle, Fire), **Prime Video / MGM content**, and a large **equity-investment portfolio** (Rivian, etc.), which creates non-operating earnings volatility.

**Key structural characteristics visible in the data:** ~$405B of 9M revenue, enormous fixed-cost base (D&A run-rate ~$46B/yr, operating-lease liability $73.9B), heavy but now *declining* capital intensity, negligible buybacks, and a growing cash pile plus investment-securities book (~$99B of cash + marketable securities).

---

## 2. Income Statement — The Margin Inflection Is the Story

### Q3 2023 vs Q3 2022 (three months ended Sept 30)

| $M | Q3 2022 | Q3 2023 | YoY |
|---|---|---|---|
| Revenue (COGS + opex + op income, derived) | 127,101 | 143,083 | **+12.6%** |
| Cost of goods & services | 70,268 | 75,022 | +6.8% |
| *COGS % of revenue* | *55.3%* | *52.4%* | **−290 bps** |
| Marketing | 11,014 | 10,551 | −4.2% |
| *Marketing % of revenue* | *8.67%* | *7.37%* | −130 bps |
| G&A | 3,061 | 2,561 | −16.3% |
| *G&A % of revenue* | *2.41%* | *1.79%* | −62 bps |
| Total costs & expenses | 124,576 | 131,895 | +5.9% |
| **Operating income** | **2,525** | **11,188** | **+343%** |
| *Operating margin* | *1.99%* | *7.82%* | **+583 bps** |
| Interest expense | 617 | 806 | +30.6% |
| Interest/investment income | 277 | 776 | +180% |
| Non-operating income/(expense) | +419 | +1,001 | — |
| Pretax income | 2,944 | 12,189 | +314% |
| Tax | 69 | 2,306 | — |
| *Effective tax rate* | *2.3%* | *18.9%* | +1,660 bps |
| **Net income** | **2,872** | **9,879** | **+244%** |
| *Net margin* | *2.26%* | *6.90%* | +464 bps |
| Diluted EPS | $0.28 | **$0.94** | +236% |
| Diluted shares | ~10,190M | ~10,510M | +3.1% |

**Interpretation:** Revenue growth accelerated to double digits (+12.6%) *while* cost growth was held to +5.9% — classic operating leverage. Cost discipline is broad-based: COGS, marketing, and G&A all declined as a % of sales. The tax line normalized (Q3'22's 2.3% rate was an anomaly from a tax benefit), so net income growth (+244%) is *lower* quality-adjusted than operating income growth (+343%) — but operating income is the cleaner signal: **+$8.66B of incremental quarterly operating profit on +$15.98B of incremental revenue = a 54% incremental operating margin.** That is an extraordinary flow-through and confirms the 2022 "cost-to-serve + AWS optimization" headwind has reversed.

### 9M 2023 vs 9M 2022 (nine months ended Sept 30)

| $M | 9M 2022 | 9M 2023 | YoY |
|---|---|---|---|
| Revenue (derived) | 364,779 | 404,824 | **+11.0%** |
| Cost of goods & services | 203,191 | 212,186 | +4.4% |
| *COGS % of revenue* | *55.7%* | *52.4%* | −330 bps |
| Fulfillment/tech/content/F&A (implied) | 152,077 | 168,995 | +11.1% |
| Marketing | 29,420 | 31,468 | +7.0% |
| G&A | 8,558 | 8,806 | +2.9% |
| Total costs & expenses | 355,268 | 381,181 | +7.3% |
| **Operating income** | **9,511** | **23,643** | **+149%** |
| *Operating margin* | *2.61%* | *5.84%* | **+323 bps** |
| Interest expense | 1,673 | 2,469 | +47.6% |
| Investment income | 544 | **2,048** | +276% |
| Non-operating income/(expense) | **−14,485** | **+228** | swing +$14.7B |
| Pretax income | −4,974 | 23,871 | swing |
| Tax | −1,990 | 4,058 | — |
| **Net income** | **−3,000** | **19,801** | swing +$22.8B |
| Diluted EPS | $(0.29) | **$1.89** | swing |
| SBC | 14,015 | 17,704 | +26.3% |
| D&A | 29,236 | 34,843 | +19.2% |

**Two distinct profit drivers — separate them:**
1. **Operating (repeatable):** +$14.1B of YoY operating income, margin +323 bps.
2. **Non-operating (non-repeatable):** +$14.7B swing from non-operating income, driven by the **Rivian/equity-securities mark-to-market reversal** — 9M'22 included a **−$11.3B** equity-securities FV loss plus **−$11.5B** marketable-securities unrealized loss, while 9M'23 shows a **+$1.0B** equity gain. **A trader should not extrapolate the 9M net-income swing; the durable driver is operating margin.**

**Cost items to monitor:** SBC grew 26% YoY ($17.7B, 4.37% of revenue vs 3.84% in 9M'22) — dilution is running ~$23.6B/yr and is a real, non-cash drag on per-share value. D&A grew 19% ($34.8B) — the amortization of the 2021–22 capex binge now inflates operating expenses even as *cash* capex falls, which is exactly why margins can expand while D&A rises.

**Deferred tax** was a **−$4,412M** benefit in 9M'23 (vs −$4,781M) — a recurring tailwind to net income (roughly 18% of 9M pretax income). Cash taxes paid were $6,982M.

**EPS bridge:** diluted EPS $1.89 vs $0.94 in Q3 alone. Share count up 3.1% YoY (no buyback offset) — AWS/retail growth is not yet flowing through at full per-share leverage.

---

## 3. Balance Sheet — Fortress Liquidity, Deleveraging, Negative Net Debt

### As of 2023-09-30 vs 2022-12-31

| $M | 12/31/2022 | 9/30/2023 | Change |
|---|---|---|---|
| Cash & cash equivalents | 53,888 | 49,605 | −4,283 |
| Marketable securities (AFS, fair value) | — | 49,871 | — |
| **Cash + securities** | — | **~99,476** | — |
| Accounts receivable (net) | 42,360 | 43,420 | +1,060 |
| Inventory (net) | 34,405 | 35,406 | +1,001 |
| **Total current assets** | 146,791 | 142,995 | −3,796 |
| Operating lease ROU asset | 66,123 | 70,758 | +4,635 |
| Finance lease ROU asset (gross) | 68,000 | 62,700 | −5,300 |
| **Total assets** | 462,675 | **486,883** | **+24,208** |
| Accounts payable | 79,600 | 72,004 | −7,596 |
| Accrued liabilities | 62,566 | 58,812 | −3,754 |
| Current portion LTD | 2,999 | 5,995 | +2,996 |
| Finance lease liability – current | 4,397 | 2,385 | −2,012 |
| Operating lease liability – current | 7,458 | 8,092 | +634 |
| **Total current liabilities** | 155,393 | **145,214** | **−10,179** |
| Long-term debt (noncurrent) | 67,150 | 61,098 | −6,052 |
| **Total long-term debt** | 70,542 | **67,472** | −3,070 |
| Finance lease liability – noncurrent | 11,386 | 10,081 | −1,305 |
| Operating lease liability – noncurrent | 61,582 | 65,810 | +4,228 |
| Deferred revenue (current + noncurrent) | 16,100 | 17,098 | +998 |
| APIC | 75,066 | 92,711 | +17,645 |
| AOCI | −4,487 | −5,003 | −516 |
| Shares outstanding | 10,242M | **10,330M** | +0.9% |

**Liquidity & leverage:**
- **Current ratio = 142,995 / 145,214 = 0.985** — technically working-capital negative (**−$2.2B**), but this is *structural and intentional* for Amazon: negative cash-conversion cycles funded by payables. It is **not** a distress signal; liquidity is $99.5B of cash+securities.
- **Gross debt (LTD $67.5B + finance leases $12.5B) = $79.9B** vs **cash+securities $99.5B ⇒ net cash position of ~+$19.6B.** Amazon is a net-cash company.
- **Total obligations incl. operating leases** = $79.9B + $73.9B = **~$153.8B**, dwarfing book equity. Operating leases are overwhelmingly real estate/fulfillment/logistics, largely matched by revenue-generating assets — but they are true fixed costs.
- **Book equity (derived)** ≈ $183B = $146.0B (12/31/22) + $19.8B net income + $17.6B APIC increase − $0.5B AOCI. **ROE (TTM net income $20.1B / ~$183B) ≈ 11.0%.**
- **Working capital released:** AP fell $7.6B and accrued liabilities fell $3.8B — i.e., Amazon *paid down* supplier float in 2023, a $10.4B cash headwind that is nonetheless a **quality-of-earnings positive** (less reliance on stretching payables to fund operations). Inventory valuation reserves fell $2.8B → $2.6B, consistent with healthier inventory.

**Forward-looking signals on the balance sheet:**
- **Contractual obligations (purchase commitments) = $284,407M** at 9/30/23, of which **$35.7B due within 12 months**, $28.4B yr-2, $23.8B yr-3, $26.6B yr-4. These are largely **AWS capacity/AI infrastructure and digital-content commitments** — a credible forward demand signal but also a hard cost floor if demand softens.
- **Deferred revenue (customer contract liabilities) $17.1B**, with **$10.9B of 9M'23 revenue recognized from prior-period deferred balances** — a recurring, high-visibility AWS/Prime backlog.

---

## 4. Cash Flow — Cash EPS Now Confirming Accounting EPS

### Q3 and 9M comparison

| $M | Q3 2022 | Q3 2023 | 9M 2022 | 9M 2023 | TTM (Oct'22–Sep'23) |
|---|---|---|---|---|---|
| Net income | 2,872 | 9,879 | −3,000 | 19,801 | **20,079** |
| D&A | 10,327 | 12,131 | 29,236 | 34,843 | **47,528** |
| SBC | 5,556 | 5,829 | 14,015 | 17,704 | — |
| Deferred taxes | −825 | −1,196 | −4,781 | −4,412 | **−7,779** |
| **Operating cash flow** | **11,404** | **21,217** | **17,579** | **42,481** | **71,654** |
| Capex (productive assets) | 16,378 | 12,479 | 47,053 | 38,141 | **54,733** |
| **Free cash flow** | **(4,974)** | **8,738** | **(29,474)** | **4,340** | **16,921** |
| Capex / revenue | 12.9% | 8.7% | 12.9% | 9.4% | ~9.9% |
| Acquisitions | 0.3 | — | 6,600 | 3,829 | 5,545 |
| LT debt issued | 0.1 | **0** | 12,931 | **0** | 8,235 |
| LT debt repaid | 0 | **0** | 0.001 | 3,386 | 4,643 |
| Short-term debt raised/(repaid), net | +4.4 | −7.9 | +9.2 | −1.9 | −7.1 |
| Buybacks | **0** | **0** | **6,000** | **0** | **0** |
| **Financing cash flow** | +3,016 | **−8,948** | +9,632 | **−9,133** | **−9,047** |
| **Investing cash flow** | −15,608 | −11,753 | −26,780 | −37,232 | **−48,053** |

**Five conclusions a trader must internalize:**

1. **FCF has inflected decisively.** TTM FCF = **+$16.9B**; 9M'23 FCF = **+$4.3B vs −$29.5B in 9M'22** (a **$33.8B swing**). Q3'23 alone printed **+$8.7B FCF vs −$5.0B** in Q3'22. The "Amazon never generates FCF" narrative is now empirically dead on a TTM basis.
2. **The FCF swing is driven by BOTH sides:** OCF +142% (9M: $17.6B→$42.5B) **and** capex −19% ($47.1B→$38.1B). Capex intensity fell from 12.9% to 9.4% of revenue. **The durability question is whether capex cuts persist** — rising AI/AWS infrastructure commitments ($35.7B due within 12 months of purchase obligations) argue capex may re-accelerate from here, capping FCF upside.
3. **Cash conversion quality is high but flattered by non-cash items:** TTM D&A $47.5B + deferred-tax benefit $7.8B are ~$55B of non-cash addbacks against $20.1B of net income. Note **accrued liabilities fell $9.0B and AR/other assets absorbed $10.4B in 9M'23** — i.e., working capital was a *drag*, so the $42.5B OCF is **not** working-capital-engineered; it is earnings + non-cash driven. **This is high-quality operating cash flow.**
4. **Deleveraging is unambiguous:** zero LT debt issued in 2023, $3.4B repaid, net short-term debt reduced $1.9B, finance lease liabilities cut $3.7B, and **zero share repurchases in all of 2023** (2022 9M had $6.0B). Capital is being retained for AWS/AI capex and debt reduction — not returned. **No buyback support for the stock price; no dividend.**
5. **Investing outflow widened to −$48.1B TTM** even as capex fell, because securities purchases/sales churn ($1.3B purchases, $9.7B maturities) and $5.5B of acquisitions — Amazon is still an acquirer (one medical/healthcare and content-related deals historically). Watch for further M&A as FCF builds.

---

## 5. Financial History / Trend Narrative (from the tag history available)

| Metric | 9M 2022 | FY 2022 (Q4 implied) | 9M 2023 | Direction |
|---|---|---|---|---|
| Revenue | $364.8B | +Q4 ≈ seasonal peak | $404.8B (+11.0%) | **Re-accelerating** |
| Operating margin | 2.61% | ~1.8% (Q4'22 weakness) | **5.84%** | **Sharp expansion** |
| Net income | −$3.0B | — | **+$19.8B** | **Swing to profit** |
| Diluted EPS | −$0.29 | — | **$1.89** | Swing |
| OCF | $17.6B | — | **$42.5B** | +142% |
| Capex | $47.1B | — | $38.1B | **−19% (discipline)** |
| FCF | −$29.5B | — | **+$4.3B** | **Inflection** |
| Total debt (LTD) | 67,150 (12/31/22) | — | 61,098 | **Down $6.1B** |
| Shares out | 10,242 (12/31/22) | — | 10,330 | +0.9% (dilutive) |
| SBC | $14.0B | — | $17.7B (+26%) | **Rising drag** |

**The arc:** 2022 was Amazon's cost-crater year — over-built fulfillment capacity, a 100M+ sq ft footprint, AWS optimization by customers, inflation, and a −$11.3B Rivian mark. Management then executed: **regionalized the US fulfillment network, cut ~27k corporate roles, slowed capex, and let AWS optimization lap.** The 9M'23 data proves the execution worked: **+323 bps of operating margin, +$14.1B of operating income, and a $33.8B FCF swing in nine months.** This is one of the cleanest large-cap margin-inflection stories in the market — and the equity already reflected a good deal of it by January 2024.

---

## 6. What Is NOT in the Data (explicit gaps)

- **Q4 2023 / FY2023 results** (reported 2024-02-01, after the as-of date). No holiday-quarter read, no FY23 10-K.
- **Segment-level revenue and operating income** (NA / International / AWS) — the 10-Q tags returned do not include segment disclosures. Cannot quantify AWS margin or AWS growth from this dataset.
- **Revenue line item tag** — revenue above is **derived** as `Total costs & expenses + Operating income` (verified: Q3'23 $131,895 + $11,188 = $143,083; 9M'23 $381,181 + $23,643 = $404,824). This is arithmetic, not an estimate.
- **Insider transactions** — **DATA_UNAVAILABLE** by explicit vendor response. No inference made.
- **Price, market cap, valuation multiples, consensus estimates, short interest.**
- **Fulfillment / technology & content / physical-store expense lines** — only aggregate COGS, marketing, G&A, SBC, D&A, lease costs are tagged.

---

## 7. Actionable Insights for Traders

**Bias: constructive on fundamentals, with asymmetric event risk into the Q4 print.**

1. **The margin story is real and confirmed in cash, not just accruals.** +583 bps of Q3 operating margin with FCF turning positive ($8.7B) is the strongest datapoint in the set. Any pullback that prices AMZN as a low-margin retailer is an opportunity. **Supporting evidence:** COGS −290 bps, marketing −130 bps, G&A −62 bps as % of revenue, all simultaneously.

2. **Do not underwrite the +244% Q3 net income growth or the 9M net-income swing as recurring.** Roughly $14.7B of the 9M YoY improvement came from **non-operating items** (Rivian/equity marks: −$11.3B loss in 9M'22 → +$1.0B gain in 9M'23). Strip those out and the true operating improvement is +$14.1B — still excellent, but half the headline. **Model off operating income, not EPS.**

3. **Capex is the swing factor for FY24 FCF — and it is likely to re-accelerate.** Capex fell 19% YoY to 9.4% of revenue, which is *the* reason FCF turned positive. But **$284.4B of purchase obligations, with $35.7B due inside 12 months**, points to AWS/AI capacity build. **Trade implication:** if Q4 commentary signals capex re-acceleration for AI, expect FCF estimates to be cut even with revenue beats — that is a margin-multiple risk, not an earnings risk.

4. **Balance sheet is a genuine downside cushion: ~$99.5B cash+securities vs $79.9B gross debt = net cash ~$19.6B**, plus $17.1B deferred revenue. Amazon can fund an AI capex cycle without equity issuance or rating pressure. **Low financial risk.**

5. **No shareholder-return floor.** Zero buybacks in 2023 (vs $6.0B in 9M'22), zero dividends, share count still up 0.9% YoY, and SBC up 26% to $17.7B (~$23.6B annualized). **Per-share value accrues only through operating growth.** This magnifies beta to sentiment.

6. **Watch the tax rate normalization.** Q3'23 effective rate 18.9% vs 2.3% in Q3'22 (which had a one-off benefit). 9M'23 rate 17.0% on a −$4.4B deferred-tax benefit. Any further rate normalization is a ~$1–2B/yr EPS headwind that consensus may under-model.

7. **Interest is now a tailwind, not a headwind.** Investment income surged to $2,048M (9M'23) from $544M, nearly offsetting $2,469M of interest expense. The 2022 rate shock has fully annualized; net interest is roughly neutral. Deleveraging ($67.5B LTD, down from $70.5B) means this stays neutral-to-positive.

8. **Pre-earnings positioning (the operative call for 2024-01-08):** In ~3 weeks AMZN reports the holiday quarter — the seasonally largest revenue and operating-profit quarter, and the first with a full lapping of the cost cuts. **Given that the Q3 data already showed +12.6% revenue growth and 7.8% operating margin, the risk into the print is a "good but not good enough" multiple compression, not a fundamental break.** The evidence supports owning the fundamental trend and sizing for gap risk rather than chasing.

9. **Key falsifiers to monitor:** (a) AWS growth re-decelerating while capex re-accelerates; (b) COGS % of revenue ticking back above ~53%; (c) marketing as % of revenue rising back above ~8% (indicates demand softness requiring spend); (d) FCF reverting negative on capex; (e) APIC growth outpacing revenue growth (SBC acceleration).

---

## 8. Key Points Summary

| Category | Metric | Latest (as of 2023-09-30) | Prior / Compare | Read-Through |
|---|---|---|---|---|
| **Data vintage** | Latest filing | Q3'23 10-Q, accepted 2023-10-27 | Q4'23 NOT yet reported (due 2024-02-01) | Pre-earnings window |
| **Profile** | Segments | 3 (North America, International, AWS) | — | AWS = profit engine; segment detail not tagged |
| **Scale** | 9M'23 revenue (derived) | $404,824M | $364,779M (9M'22) | **+11.0% YoY** |
| **Growth** | Q3'23 revenue (derived) | $143,083M | $127,101M (Q3'22) | **+12.6% YoY, re-accelerating** |
| **Profitability** | Q3'23 operating income | $11,188M (7.82% margin) | $2,525M (1.99%) | **+343%; +583 bps** |
| **Profitability** | 9M'23 operating income | $23,643M (5.84% margin) | $9,511M (2.61%) | **+149%; +323 bps** |
| **Cost discipline** | COGS % of rev (Q3) | 52.4% | 55.3% | **−290 bps** |
| **Cost discipline** | Marketing % of rev (Q3) | 7.37% | 8.67% | −130 bps |
| **Earnings** | Q3'23 diluted EPS | $0.94 | $0.28 | +236% |
| **Earnings** | 9M'23 diluted EPS | $1.89 | $(0.29) | Swing; includes non-op gains |
| **Earnings quality** | 9M'23 non-operating | +$228M | −$14,485M | **+$14.7B swing = Rivian/equity marks (non-recurring)** |
| **Tax** | Q3'23 effective rate | 18.9% | 2.3% | Normalization = EPS headwind |
| **Cash generation** | TTM OCF | $71,654M | — | Strong |
| **Cash generation** | 9M'23 OCF | $42,481M | $17,579M | **+142%** |
| **Capex** | 9M'23 capex | $38,141M (9.4% of rev) | $47,053M (12.9%) | **−19%; FCF enabler** |
| **FCF** | TTM FCF | +$16,921M | — | Positive |
| **FCF** | 9M'23 FCF | +$4,340M | $(29,474)M | **+$33.8B swing** |
| **FCF** | Q3'23 FCF | +$8,738M | $(4,974)M | Inflection |
| **Balance sheet** | Cash + securities | ~$99,476M | $53,888M cash (12/31/22) | **Fortress liquidity** |
| **Balance sheet** | Total LTD | $67,472M | $70,542M | **Deleveraging −$3,070M** |
| **Balance sheet** | Net debt/(cash) | **~$(19.6)B net cash** | — | No solvency risk |
| **Balance sheet** | Current ratio | 0.985 | 0.945 | Negative WC = structural, funded by payables |
| **Leases** | Operating + finance lease liab. | $85,368M | $86,109M | Large fixed-cost base |
| **Commitments** | Purchase obligations | $284,407M ($35.7B <12mo) | — | **AI/AWS spend signal + cost floor** |
| **Backlog** | Deferred revenue | $17,098M | $16,100M | $10.9B recognized in 9M'23 |
| **Capital return** | Buybacks 2023 | **$0** | $6,000M (9M'22) | **No price support / no dividend** |
| **Dilution** | Shares outstanding | 10,330M | 10,242M | +0.9%; no buyback offset |
| **Dilution** | SBC | $17,704M (9M'23) | $14,015M | **+26%; 4.4% of revenue** |
| **Returns** | ROE (TTM NI / derived equity) | ~11.0% | — | Recovering |
| **Insider activity** | Transactions | **DATA_UNAVAILABLE** | — | **No conclusion drawn** |
| **Valuation** | Multiples | **NOT AVAILABLE** (no price feed) | — | Not assessed |
| **Stance** | Fundamental bias | **Constructive** | — | Margin+FCF inflection confirmed in cash |
| **Stance** | Primary risk | Q4 print 2024-02-01; capex re-acceleration for AI | — | Own trend, size for gap risk |

---

**Bottom line on AMZN:** The Q3 2023 data — the freshest fundamentals legitimately available on 2024-01-08 — documents a genuine, cash-confirmed inflection: **+12.6% revenue growth, +583 bps of operating margin, and the first positive quarterly FCF in over a year**, backed by a ~$99.5B liquidity pool and a net-cash balance sheet. The three things a trader must discount are (1) **non-operating equity marks flatter the 9M net-income swing**, (2) **the FCF recovery rests on a 19% capex cut that $284B of purchase obligations suggest will reverse**, and (3) **there is zero buyback/dividend support and ~4.4% revenue dilution from SBC**. Fundamentals support the long side; the Feb 1 Q4 print, not this dataset, is the next real information event.