I have a comprehensive fact base now. Note: the vendor's insider-transaction archive returned no data for GOOGL, and some tags were truncated by the feed — I derive those and label them as such.

---

# GOOGL — Alphabet Inc. | Fundamental Deep Dive
**As of: 2026-09-01 | Latest filing in the fact set: Q2 2026 Form 10-Q, accepted 2026-07-23 (accn 0001652044-26-000071); prior FY2025 Form 10-K accepted 2026-02-05**

## 1. Executive summary

Alphabet's fundamentals have bifurcated sharply. The **operating business is accelerating and expanding margins** (H1 2026 revenue +23.1% YoY, operating income +30.0%, operating margin 35.0% vs 33.1%), while the **financial statements are being distorted by (a) an extraordinary $135.8B of pre-tax investment gains and (b) a capital-intensity shock** — H1 capex of $80.6B (+103% YoY) that pushed **Q2 2026 free cash flow to roughly –$5.9B**. To fund this, Alphabet raised **~$56.2B of debt, $19.1B of convertible preferred and $30.5B of common equity in H1 2026** and **stopped buying back stock entirely ($0 vs $28.3B in H1 2025)**.

Reported diluted EPS of **$9.11 in Q2 2026** (vs $2.31) is *not* an earnings number a trader should capitalize. Stripping investment gains, **core EPS was ~$2.66 in Q2 (+~20% YoY)** and **~$5.29 in H1 (+~22% YoY)** — still excellent, but a fraction of the headline.

---

## 2. Company profile & data caveats

**Alphabet Inc. (GOOGL)** — parent of Google. Reportable segments: **Google Services** (Search & other, YouTube ads, Google Network, subscriptions/platforms/devices), **Google Cloud** (infrastructure + Workspace + AI platforms), and **Other Bets** (Waymo and other long-horizon ventures). Revenue is predominantly advertising plus a fast-growing cloud/subscription mix; consolidated results increasingly reflect AI datacenter buildout (depreciation, energy, TPU/GPU) and a large venture/equity investment portfolio.

**Caveats for this report (read before trading):**
- The configured data vendor returns **point-in-time SEC XBRL facts only** — no narrative MD&A, no segment-level tags, no price/valuation data, and **no insider-transaction archive** (explicitly `DATA_UNAVAILABLE` for GOOGL; no insider activity is inferred or fabricated here).
- The fact feed was **alphabetically truncated** on several pulls, so certain standard tags (e.g., full-year `Revenues`, `OperatingIncomeLoss` for FY2023–FY2025, 6/30/2026 `Liabilities`/`StockholdersEquity`) were not directly returned. Where noted, I **derive** them from identities that tie exactly (Revenue = `CostsAndExpenses` + `OperatingIncomeLoss`) and flag estimates.
- **No new filing occurred in the past calendar week** — the information set "as of 2026-09-01" is effectively the Q2 2026 10-Q (filed 2026-07-23).

---

## 3. Income statement — the operating engine is strong

All figures $M. Q2/H1 2026 from the 10-Q; prior-year comparatives from prior filings. Revenue is derived as Costs & Expenses + Operating income (identity verified against reported Q1 2026 `Revenues` of $109,896M).

| $M | Q2 2026 | Q2 2025 | YoY | Q1 2026 | Q1 2025 | YoY |
|---|---|---|---|---|---|---|
| Revenue | **119,796** | 96,428 | **+24.2%** | **109,896** | 90,234 | **+21.8%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 41,271 | 36,361 | +13.5% |
| Gross profit | **73,853** | 57,389 | +28.7% | 68,625 | 53,873 | +27.4% |
| Gross margin | **61.7%** | 59.5% | +2.2pp | 62.4% | 59.7% | +2.7pp |
| R&D | n/d (see note) | ~14,737 | — | 17,032 | 13,556 | +25.6% |
| Sales & marketing | n/d | ~6,172 | — | 7,606 | 6,172¹ | +23.2% |
| G&A | 6,461 | 5,209 | +24.0% | 4,291 | 3,539 | +21.2% |
| R&D + S&M combined (derived) | **26,622** | 20,909 | +27.3% | 24,638 | 19,728 | +24.9% |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 70,200 | 59,628 | +17.7% |
| **Operating income** | **40,770** | 31,271 | **+30.4%** | **39,696** | 30,606 | **+29.7%** |
| Operating margin | **34.0%** | 32.4% | +1.6pp | 36.1% | 33.9% | +2.2pp |
| Other income (expense), net | **97,983** | 2,662 | n/m | **37,716** | 11,183 | n/m |
| Pre-tax income | 138,753 | 33,933 | +309% | 77,412 | 41,789 | +85.2% |
| Income tax | 26,560 | 5,737 | — | 14,834 | 7,249 | — |
| Effective tax rate | **19.1%** | 16.9% | +2.2pp | **19.2%** | 17.3% | +1.9pp |
| Net income | **112,193** | 28,196 | +298% | 62,578 | 34,540 | +81.2% |
| Diluted EPS | **$9.11** | $2.31 | +294% | $5.11 | $2.81 | +82% |
| **Core EPS (est., ex-investment gains)** | **~$2.66** | ~$2.22 | **+~20%** | **~$2.62** | ~$2.13 | +~23% |

¹Q1 2025 S&M = 6,172 (reported). Q2 spike-line items for R&D/S&M are not separately available in the truncated feed; the combined figure ties exactly (Total C&E – COGS – G&A).

**H1 aggregates:**

| $M | H1 2026 | H1 2025 | YoY | H1 2024 | H1 2025 vs 2024 |
|---|---|---|---|---|---|
| Revenue | **229,692** | 186,662 | **+23.1%** | 165,281 | +12.9% |
| Gross profit | 142,478 | 111,262 | +28.1% | 96,062 | +15.8% |
| Gross margin | 62.0% | 59.6% | +2.4pp | 58.1% | — |
| G&A | 10,752 | 8,748 | +22.9% | 6,184 | +41.5% |
| SBC (total) | **15,200** | 11,500 | **+32.2%** | 11,200 | +2.7% |
| Operating income | **80,466** | 61,877 | **+30.0%** | 52,897 | +17.0% |
| Operating margin | **35.0%** | 33.1% | +1.9pp | 32.0% | — |
| Investment gains (debt & equity) | **135,803** | 11,411 | n/m | 757 | n/m |
| Net income | 174,771 | 62,736 | +178.6% | 47,281 | +32.7% |
| Diluted EPS | $14.24 | $5.12 | +178% | $3.78 | +35% |

**Interpretation for traders:**
- **Revenue growth has re-accelerated decisively**: Q2 2024→Q2 2025 was +13.8%; Q2 2025→Q2 2026 is **+24.2%**. Two-year stacked growth in Q2 is ~41%. This is a genuine re-rating of the top line, not a comp illusion.
- **Gross margin is *expanding* 2+ points despite the AI buildout**, i.e., the incremental compute is currently being monetized above its fully-loaded cost. This is the single most important bullish datapoint in the release, because the bear case has been "AI capex is margin-dilutive."
- **Operating leverage is positive**: opex (COGS + G&A + R&D/S&M) grew 21.3% in Q2 vs revenue +24.2%.
- **SBC inflation is a real but manageable headwind**: +32% YoY ($15.2B in H1 = 6.6% of revenue vs 6.2%).
- **Tax rate has structurally stepped up** (19.1%–19.2% in 2026 vs 16.9%–17.3% in 2025 and 13.9% FY2023) — a ~2pp EPS headwind that should be modeled into 2026–2027.

### 3.1 The earnings-quality bridge — do not capitalize reported EPS

| $M | H1 2026 | H1 2025 |
|---|---|---|
| Reported net income | 174,771 | 62,736 |
| Less: pre-tax investment gains | (135,803) | (11,411) |
| Tax on gains @ effective rate | +25,940 | +1,951 |
| **Core net income (est.)** | **~64,908** | **~53,276** |
| **Core diluted EPS (est.)** | **~$5.29** | **~$4.35** |
| Core EPS growth | **+~22%** | — |

Reported EPS overstates core profitability by **~2.7x in H1 2026**. The offsetting tell: **cash flow from operations ($84.9B) was less than half of net income ($174.8B)**, precisely because $135.8B of the "earnings" was non-cash mark-to-market.

---

## 4. Balance sheet — asset base up 55% in six months, and now levered

| $M | 6/30/2026 | 3/31/2026 | 12/31/2025 | Δ 6mo |
|---|---|---|---|---|
| Cash & equivalents | 55,911 | 38,063 | 30,708 | +82% |
| **Cash + short-term investments** | **242,474** | 126,840 | 126,843 | **+91%** |
| AFS debt securities (fair value) | 99,500 | 82,733 | 89,822 | +10.8% |
| Non-marketable equity securities (no RDFV) | **124,259** | 101,346 | 64,094 | **+94%** |
| Accounts receivable, net | 69,175 | 62,999 | 62,886 | +10.0% |
| Total current assets | 343,524 | 213,753 | 206,038 | +67% |
| **Total assets** | **921,983** | 703,919 | 595,281 | **+54.9%** |
| Accounts payable | 20,258 | n/a | 12,200 | +66% |
| Accrued liabilities | 73,014 | 63,019 | 55,557 | +31.4% |
| Employee-related liabilities | 15,086 | 13,947 | 17,546 | -14.0% |
| Income taxes payable (current) | 5,233 | 3,905 | 523 | +900% |
| **Total liabilities** | n/a (est. ~286,000) | **225,173** | **180,016** | — |
| **Total stockholders' equity** | n/a (est. ~636,000) | **478,746** | **415,265** | — |
| Debt (carrying amount) | **101,085** | 80,305 | 49,085 | **+106%** |
| Finance lease liabilities | 2,590 | 2,214 | 2,500 | +3.6% |
| Operating lease liabilities | 18,037 | 16,161 | 15,954 | +13.1% |
| Deferred tax liabilities, net | **22,819** | n/a | 919 | +2,383% |
| Deferred revenue / contract liabilities | 10,100 | 9,800 | 8,600 | +17.4% |
| Loss contingency accruals (current) | 17,356 | 15,551 | 15,594 | +11.3% |
| AOCI | (2,285) | (2,180) | (1,916) | — |
| Common stock + APIC | 131,371 | n/a | 93,126 | +41.1% |
| Shares outstanding (M) | **12,230** | n/a | 12,088 | +1.2% |
| Convertible preferred (carrying) | **18,023** | 0 | 0 | new |
| Liquidity: cash+ST inv less total debt | **~141,389** | 46,535 | 77,758 | +82% |

*6/30/2026 liabilities and equity were not directly returned by the truncated feed. Equity is estimated at ~$636B by rolling forward Q1 equity ($478.7B) for Q2 net income +112.2, common issuance +30.5, preferred +19.1, minority +0.6, dividends −2.7, OCI ~−0.1; liabilities are the residual of total assets. Treat both as approximations; Q1 figures are exact.*

**Balance-sheet reads:**
- **Still net-cash, but the cushion is now partly borrowed.** Gross debt doubled to $101.1B in six months; debt/assets = 11.0%. Net liquidity of ~$141B (≈$123B after the $18.0B preferred) remains ample versus ~$80B/quarter of capex.
- **Asset inflation is mostly mark-to-market, not operations.** Non-marketable equity securities nearly doubled to $124.3B, with cumulative *upward* fair-value adjustments rising from $44.5B to **$85.7B** and the "cash + short-term investments" line jumping $115.6B in six months — a revaluation event (observable transaction in a private holding), not cash generation.
- **The $22.8B net deferred tax liability (from $0.9B) is the tax footprint of those unrealized gains.** It is a future cash-tax claim, not a financing liability — but it explains why the tax rate is climbing even as reported EPS soars.
- **Accrued liabilities +$17.5B, AP +$8.1B, taxes payable +$4.7B** in Q2 point to a large capex/accrual build (see §5) rather than operational stress.
- **Working capital is healthy**: receivables +10% against revenue +24% → receivables days *improved* (~52.6 days vs ~50.6 in Q2 2024 is roughly flat; no channel-stuffing signal).
- **Legacy legal overhang**: $17.4B of current loss-contingency accruals (regulatory/antitrust-type) — a live but contained tail risk.

---

## 5. Cash flow — the story of the quarter: negative free cash flow

| $M | H1 2026 | H1 2025 | YoY | Q2 2026 (derived) | Q2 2025 |
|---|---|---|---|---|---|
| **Operating cash flow** | **84,859** | 63,897 | **+32.8%** | **39,069** | 27,747 |
| Capex (cash paid for PP&E) | **(80,598)** | (39,643) | **+103%** | **(44,924)** | (21,846) |
| **Free cash flow** | **4,261** | 24,254 | **–82.4%** | **(5,855)** | **5,901** |
| FCF margin | 1.9% | 13.0% | –11.1pp | **–4.9%** | 6.1% |
| Capex / revenue | **35.1%** | 21.2% | +13.9pp | **37.5%** | 22.7% |
| Investing cash flow | (145,822) | (40,738) | n/m | (82,433) | (24,544) |
| Financing cash flow | **+86,320** | (26,033) | n/m | **+61,543** | (5,832) |
| Net change in cash | +25,203 | (2,430) | n/m | +17,848 | (1,704) |

**Financing detail (H1 2026 vs H1 2025, $M):**

| Item | H1 2026 | H1 2025 |
|---|---|---|
| Proceeds from debt | **56,226** | 31,378 |
| Repayments of debt/leases | (5,253) | (18,397) |
| **Proceeds from common stock issuance** | **30,499** | 0 |
| **Proceeds from convertible preferred issuance (6/5/2026)** | **19,063** | 0 |
| Minority shareholder contributions | 3,758 | 400 |
| **Share repurchases** | **0** | **(28,306)** |
| Dividends paid | (5,231) | (4,977) |
| Other financing | (686) | (400) |
| *(Implied share-settlement/tax withholding, not in feed)* | ~(12,056) | ~(5,731) |

**Other cash items:** purchases of other (non-marketable) investments **$22,051M vs $2,312M** (+854%) — capital deployment outside the core business; marketable securities net purchases $9,784M; capex *incurred but not yet paid* **$29,113M at 6/30/2026 vs $10,635M a year earlier** (+174%).

**Interpretation — this is the crux:**
1. **Operating cash conversion is excellent** (OCF/operating income = 105%); the business is generating cash at a record pace in absolute terms.
2. **Every dollar of that improvement, and more, is being reinvested**: capex is running at ~37.5% of revenue and, at the Q2 run-rate, **~$180B annualized** vs ~$52B in FY2024.
3. **The pipeline implies Q3 capex will not fall**: $29.1B of capex was already incurred-but-unpaid at quarter-end, so Q3 cash capex likely ≥$45B. Model FY2026 capex near **$170–185B** and **FCF at or below zero for the full year** absent a revenue surprise.
4. **Capital allocation regime change**: buyback went from $28.3B (H1 2025) to **zero**, replaced by **net issuance** of $30.5B common + $19.1B convertible preferred + $56.2B debt. Shares outstanding rose from 12,088M to 12,230M. This is a **dilution and capital-structure risk that did not exist in Alphabet's profile a year ago**, and it is the most under-priced item in these statements.

---

## 6. Investment portfolio & mark-to-market risk

| $M | 6/30/2026 | 3/31/2026 | 12/31/2025 |
|---|---|---|---|
| Equity securities w/o readily determinable FV | 124,259 | 101,346 | 64,094 |
| Cumulative upward FV adjustments | 85,732 | 80,792 | 44,485 |
| Cumulative downward FV adjustments | 9,115 | 8,935 | 8,820 |
| FV-NI realized gains (period) | 836 | 496 | 778 (FY25) |
| FV-NI unrealized gains (period) | 21,531 | 105 | 1,907 (FY25) |
| **Total debt & equity securities gain (period)** | **135,803** | 36,804 | 24,620 (FY25) |

**This is the largest swing factor in reported results and the least predictable.** H1 2026 gains of $135.8B compare with $24.6B for all of FY2025 and $2.7B in FY2024. The mechanics (observable-transaction revaluations of non-marketable holdings, plus realized gains) mean:
- Gains are **non-recurring, non-cash and reversible**. A single down-round or IPO repricing could flip this line to a multi-tens-of-billions *loss* and crater headline EPS with zero change to the operating business.
- Traders should treat this line as **"other, ignore"** for valuation and as a **sentiment catalyst** (both directions) for headlines.
- Note the asymmetry: $85.7B of cumulative upward marks sit against only $9.1B of downward marks — the portfolio's carrying value is heavily mark-up dependent.

---

## 7. Multi-year history (from FY2025 and FY2024 10-K facts)

| $M | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Cost of revenue | 133,332 | 146,306 | 162,535 |
| Total costs & expenses | 223,101 | 237,628 | 273,797 |
| SBC (total) | 22,100 | 22,800 | **27,100** |
| Investment gains (debt & equity) | (823) | 2,671 | **24,620** |
| Comprehensive income | 76,996 | 99,720 | **135,054** |
| Basic EPS | $5.84 | $8.13 | **$10.91** |
| Diluted EPS | $5.80 | $8.04 | **$10.81** |
| Effective tax rate | 13.9% | 16.4% | 16.8% |
| Deferred tax provision | (7,729) | (5,256) | **+8,250** |
| Current tax provision | 19,651 | 24,953 | 18,406 |
| Financing cash flow | (72,093) | (79,733) | **(37,388)** |
| Capex incurred but unpaid (YE) | 7,435 | 10,326 | 15,090 |
| Cash + ST investments (YE) | 110,916 | 95,657 | 126,843 |
| Total assets (YE) | 402,392 | 450,256 | 595,281 |
| Liabilities (YE) | 119,013 | n/a | 180,016 |
| Shares outstanding (YE, M) | n/a | 12,088¹ | 12,088 |

¹12,088M at 12/31/2025 per the Q2 2026 10-Q comparative.

**Trajectory read:** cost base growing ~15%/yr while revenue growth was ~12–14% through 2025; **2026 marks the inflection where revenue growth (+23%) overtook cost growth (+21%)** — the first clear positive operating-leverage year since the AI capex cycle began. Buybacks collapsed from ~$72–80B/yr (FY2023–FY2024) to $37.4B (FY2025) to **$0 (H1 2026)** — a four-year capital-return retreat that mirrors the capex ramp.

---

## 8. Segment/backlog and other datapoints available

- **Remaining performance obligation: $467,600M at 3/31/2026** (latest available; Q2 figure not in truncated feed). This is contracted, not-yet-recognized revenue — >2x annualized revenue, implying a very large committed backlog (consistent with a hyperscale Cloud/AI contracts cycle). *This is the strongest forward-looking datapoint in the entire fact set* — but it is a Q1 number and should be refreshed from the Q2 10-Q text before acting.
- **Deferred revenue $10.1B** (+17% since year-end), with $4.9B of H1 2026 revenue recognized from the opening contract-liability balance.
- **Finite-lived intangibles gross jumped from $2.47B to $10.59B** (net ~$8.9B) between 12/31/2025 and 6/30/2026, with amortization running $545M in H1 (guidance: **$1,304M next 12 months, $747M remainder of FY2026**). Combined with $22.1B of "other investments" purchases, this signals **material inorganic capital deployment in Q1–Q2 2026** that is not itemized in the tags available.
- **Segment-level revenue/operating income: not available** in this feed (no `StatementBusinessSegmentsAxis` members returned). A trader should pull the 10-Q segment table directly — specifically Google Cloud margin and Search & other growth — before sizing a position.
- **Insider transactions: DATA_UNAVAILABLE.** The vendor explicitly has no authorized point-in-time insider archive for GOOGL. **No insider buying or selling is reported or implied in this note.** (This is a genuine information gap; do not substitute inference.)

---

## 9. Red flags & diligence checklist

| # | Flag | Evidence | Why it matters |
|---|---|---|---|
| 1 | **Negative quarterly FCF** | Q2 2026 FCF ≈ –$5.9B; H1 FCF $4.3B vs $24.3B | Breaks the core bull thesis of "cash machine"; FCF-based valuation multiples become undefined/negative |
| 2 | **Capex at 37.5% of revenue, rising** | H1 capex $80.6B (+103%); $29.1B incurred-unpaid | Q3 capex likely ≥$45B; FY26 ~$170–185B; depreciation drag intensifies in 2027 |
| 3 | **Buyback fully halted + equity/preferred issuance** | $0 repurchases vs $28.3B; +$30.5B common, +$19.1B convertible preferred; shares 12,088M → 12,230M | Structural change in shareholder-return profile; dilution and preferred dividend ($86M/qtr) overhang; conversion terms unknown |
| 4 | **Earnings quality: $135.8B of investment gains** | 78% of H1 pre-tax income | Reported EPS $14.24 vs core ~$5.29; reversal risk is large and unhedgeable from outside |
| 5 | **Portfolio marks are asymmetric** | Upward cumulative marks $85.7B vs downward $9.1B | Concentrated exposure to one/few private holdings; a repricing hits both EPS and book value |
| 6 | **Debt doubled in 6 months** | $49.1B → $101.1B; interest expense $1.8B H1 vs $0.3B | Still trivial vs earnings (44x coverage) but the *trend* is new; watch credit ratings commentary |
| 7 | **Tax rate step-up** | 19.1% vs 16.9%; DTL $0.9B → $22.8B | ~2pp structural EPS headwind; deferred tax on unrealized gains will become cash tax on realization |
| 8 | **Legal/regulatory accruals** | $17.4B current loss-contingency accrual (+11% in 6mo) | Binary headline risk |
| 9 | **SBC re-acceleration** | +32% YoY, 6.6% of revenue | Erodes per-share economics precisely as buybacks stop |

---

## 10. Actionable trading implications

**What the data supports:**
- **Long-operating-fundamentals / short-headline-EPS expression.** The operating franchise is the best it has been in three years: revenue +24%, gross margin +2.2pp, operating margin 34–35%, RPO ~$468B. Any sell-off driven by "EPS miss vs. inflated consensus" (i.e., a quarter without a large investment gain, producing "EPS of $2.60 vs $9.11 prior year") is a **fundamental-buying opportunity, not a deterioration signal**. Expect exactly this optical distortion in Q3/Q4 2026 comparatives.
- **Conversely, an EPS "beat" driven by further equity marks should be faded**, not chased. Position sizing should be done off core EPS (~$5.29 H1, ~$10.6–11.0 annualized run-rate, +~20% growth) and off **EBITDA/capex-adjusted cash returns**, not GAAP EPS.
- **The single most important number to monitor next is capex guidance and the FCF inflection.** If capex/revenue holds at ~37% and revenue keeps compounding at >20%, FCF turns positive again in 2027 and the stock can re-rate on "AI capex is now harvesting." If capex outruns revenue, the financing treadmill ($56B debt + $49B equity/preferred already) becomes a multiple-compression story.
- **Watch for dilution mechanics.** A $19.0B convertible preferred issued 6/5/2026 with unknown conversion terms is a hard ceiling on per-share upside until the terms are read. Combined with zero buybacks, share count is now a *headwind* rather than a tailwind — a genuine regime change for GOOGL.
- **Balance-sheet optionality remains a positive:** ~$141B net cash (≈$123B post-preferred) against ~$180B annualized capex means Alphabet can self-fund roughly 2/3 of its build without new capital markets access. That caps downside from a financing shock.

**Suggested framing (no price data available, so no target):**
- **Bull case (evidence-based):** sustained >20% revenue growth + gross-margin expansion + $468B backlog → operating income compounding ~30%, capex peaks in 2027, FCF inflects, buybacks resume. Reported EPS wildly understates the franchise.
- **Base case:** revenue +18–22%, operating margin 33–35%, FY2026 FCF ≈ $0–15B, continued external financing, shares drift 1–2% higher per year, GAAP EPS dominated by marks.
- **Bear case:** capex/revenue >40% with decelerating cloud bookings, investment marks reverse (a $30–50B swing), tax rate to 20%+, further equity issuance → both EPS and FCF disappoint simultaneously.

**Next catalysts to check (in order):** (1) Q3 2026 10-Q — capex, FCF, RPO refresh, segment margin, buyback status; (2) convertible preferred terms (conversion price, dividend, dilution); (3) disclosure of the private-holding(s) driving the $136B gain; (4) debt issuance pace/credit rating actions; (5) any resumption of repurchases.

---

## 11. Key points summary table

| Category | Item | Value | Read |
|---|---|---|---|
| **Growth** | Q2 2026 revenue | $119.80B, **+24.2% YoY** | Re-acceleration (Q2'25 was +13.8%) |
| | H1 2026 revenue | $229.69B, +23.1% | Best growth since 2021 |
| | RPO (3/31/26) | **$467.6B** | Very large contracted backlog |
| **Profitability** | Q2 operating income | $40.77B, +30.4%; margin **34.0%** | Positive operating leverage |
| | H1 operating margin | 35.0% (vs 33.1%) | +1.9pp |
| | Gross margin | 62.0% (vs 59.6%) | AI costs not dilutive yet |
| **Earnings quality** | H1 investment gains | **$135.80B pre-tax** | 78% of pre-tax income; non-cash, reversible |
| | Reported diluted EPS H1/Q2 | $14.24 / $9.11 | Do **not** capitalize |
| | Core EPS (est.) H1/Q2 | ~$5.29 / ~$2.66 | +~22% / +~20% YoY — the real number |
| | Effective tax rate | 19.1–19.2% (vs 16.9%) | ~2pp structural headwind |
| **Cash flow** | H1 operating cash flow | $84.86B (+32.8%) | Strong conversion (105% of op income) |
| | H1 capex | **$80.60B (+103%)**; 35.1% of revenue | Investment super-cycle |
| | H1 free cash flow | **$4.26B (–82%)** | **Q2 FCF ≈ –$5.9B** |
| | Capex incurred, unpaid | $29.11B (+174%) | Q3 capex ≥$45B |
| **Capital allocation** | Buybacks H1 2026 | **$0** (vs $28.31B) | Halted |
| | Equity / preferred / debt raised | **$30.50B / $19.06B / $56.23B** | Regime change; dilution risk |
| | Dividends | $5.23B; $0.22/qtr (+4.8%) | Growing modestly |
| **Balance sheet** | Total assets | **$921.98B** (+54.9% in 6mo) | Inflated by marks + raises |
| | Cash + ST investments | $242.47B | Record liquidity |
| | Total debt (carrying) | $101.09B (2.1x since YE); + leases $20.6B | Doubled but only 11% of assets |
| | Liquidity − debt | ~$141.4B net cash | ~2/3 of annualized capex self-funded |
| | Deferred tax liability | $22.82B (from $0.92B) | Tax on unrealized gains |
| | Non-marketable equity | $124.26B (+94%); up-marks $85.7B vs down $9.1B | Concentrated, asymmetric mark risk |
| | Loss contingency accruals | $17.36B current | Legal overhang |
| | Shares outstanding | 12.230B (from 12.088B) | Now dilutive, not accretive |
| **History** | FY23/24/25 diluted EPS | $5.80 / $8.04 / $10.81 | ~30%/yr |
| | FY23/24/25 total costs | $223.1B / $237.6B / $273.8B | Cost growth 15%/yr, now < revenue growth |
| | FY23/24/25 SBC | $22.1B / $22.8B / $27.1B | Re-accelerating |
| | FY23/24/25 buyback+financing | –$72.1B / –$79.7B / –$37.4B | Capital return winding down |
| **Gaps** | Insider transactions | **DATA_UNAVAILABLE** | No insider data exists in feed; nothing inferred |
| | Segment revenue/margins, price/valuation, FY25 & FY26 revenue totals | Not returned | Pull from 10-Q text / other sources |

**Bottom line for GOOGL:** the operating business is executing at its strongest pace in years (accelerating revenue, expanding gross and operating margins, $468B backlog), but **the reported numbers are not the operating numbers** — $135.8B of reversible investment gains inflate EPS by ~2.7x, while a $180B annualized capex program has turned free cash flow negative at the quarter level and forced Alphabet into net issuance of debt, common equity and convertible preferred while halting buybacks. Trade the core earnings trajectory (~+20%), size against the FCF/capex inflection and the preferred-dilution terms, and treat investment marks as noise with two-way headline risk.