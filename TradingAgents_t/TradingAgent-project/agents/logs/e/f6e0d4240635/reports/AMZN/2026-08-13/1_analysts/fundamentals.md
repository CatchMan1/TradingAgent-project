# AMZN — Fundamental Research Report
**Amazon.com, Inc. (NASDAQ: AMZN)** | Point-in-time analysis as of **2026‑08‑13**
Primary source: point-in-time SEC XBRL facts, latest filing **Form 10‑Q accepted 2026‑07‑31** (period ended 2026‑06‑30), i.e. the Q2‑2026 report is ~2 weeks old — the freshest fundamental catalyst available.

---

## 1. What changed this week (the news the numbers contain)

- **Q2 2026 10‑Q was accepted 2026‑07‑31** (accession 0001018724‑26‑000026). Every figure below is what was public as of today; nothing after 2026‑07‑31 is reflected.
- The prior 10‑Q (Q1 2026, period 2026‑03‑31) was accepted 2026‑04‑30.
- The dominant new facts in this filing: (a) a **$50.5B non‑cash mark‑up on non‑marketable equity securities** in Q2 alone, (b) a **step‑change in capex** (~27% of revenue), and (c) **$64B of incremental long‑term debt** in six months.
- **Insider transactions: DATA UNAVAILABLE.** The data package has no authorized point‑in‑time insider archive for AMZN. I will not infer or fabricate insider activity; treat this as an open gap for the desk.

---

## 2. Company profile and structure

- **Issuer:** Amazon.com, Inc. (CIK 1018724), fiscal year = calendar year, 10‑Q/10‑K filer.
- **Operating segments:** the XBRL tag `NumberOfOperatingSegments = 3` for H1 2026, consistent with the three‑reportable‑segment structure (**North America retail, International retail, AWS**). Segment-level revenue and operating income are *not* in the returned fact set — a genuine analytical gap.
- **Share base:** 10,783M shares outstanding at 2026‑06‑30; 10,786.3M as of the 2026‑07‑22 cover date. Authorized 100B; par $0.01. No dividends (no dividend tags), and no share‑repurchase line appears in the financing section — capital is going to capex, M&A and debt service instead.
- **Latest activity mix (inferred from tags):** large inorganic activity — `PaymentsToAcquireBusinessesNetOfCashAcquired` of **$39.8B in H1 2026** and **$42.0B TTM**, plus a private‑equity investment book that revalued violently upward.

---

## 3. Income statement — revenue growth is accelerating, and so is operating leverage

*Note on methodology:* the direct revenue tag was not present in the returned rows, so revenue is **derived exactly** as `Total CostsAndExpenses + OperatingIncomeLoss` (arithmetically identical under US GAAP presentation). This is validated by the prior‑year periods reconciling to the historically reported $167.70B (Q2 2025) and $323.37B (H1 2025).

| $ millions | Q2 2026 | Q2 2025 | YoY | Q1 2026* | H1 2026 | H1 2025 | YoY |
|---|---|---|---|---|---|---|---|
| Revenue (derived) | **200,606** | 167,702 | **+19.6%** | 181,519 | **382,125** | 323,369 | **+18.2%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 87,463 | 183,241 | 157,785 | +16.1% |
| Gross profit | 104,828 | 86,893 | +20.6% | 94,056 | 198,884 | 165,584 | +20.1% |
| **Gross margin** | **52.3%** | 51.8% | +45 bps | 51.8% | **52.1%** | 51.2% | +85 bps |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 157,667 | 330,812 | 285,793 | +15.8% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** | 23,852 | **51,313** | 37,576 | **+36.6%** |
| **Operating margin** | **13.7%** | 11.4% | +225 bps | 13.1% | **13.4%** | 11.6% | +180 bps |
| Non‑operating income | **53,396** | 1,686 | n.m. | 15,982 | **69,378** | 4,960 | n.m. |
| Pre‑tax income | 80,857 | 20,857 | +288% | 39,834 | 120,691 | 42,536 | +184% |
| Income tax | 18,199 | 2,678 | +580% | 9,560 | 27,759 | 7,231 | +284% |
| **Net income** | **62,647** | 18,164 | **+245%** | 30,255 | **92,902** | 35,291 | **+163%** |
| Diluted EPS | **$5.75** | $1.68 | +242% | $2.78 | **$8.53** | $3.27 | +161% |
| Diluted shares (implied) | ~10,895M | ~10,812M | +0.8% | ~10,885M | ~10,891M | ~10,793M | +0.9% |

\*Q1 2026 is derived by subtraction (H1 less Q2), so it embeds rounding; treat as directional.

### The single most important analytical point: earnings quality
- Of **$62.6B Q2 net income, $50.5B came from an "upward price adjustment" on equity securities without a readily determinable fair value** (`EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment` = $50,486M in Q2; **$62,814M in H1**). Add $1.3B of realized/FV gains on marketable equity and $1.3B of unrealized gains on marketable securities, and essentially **100% of non‑operating income was mark‑to‑market**, not interest.
- The mark is **non‑cash and non‑recurring in nature**. It also drove **$17.7B of Q2 deferred tax expense** (deferred tax for H1 = $30.5B; TTM = $41.4B), which is why the tax line exploded.
- **Strip the mark:** Q2 pre‑tax "core" income ≈ operating income of $27,461M; at the implied ~24.9% residual tax rate, core net income ≈ **$21.3B**, core diluted EPS ≈ **$1.95**, i.e. **~+16% YoY** rather than the +242% headline.
- **Trading implication:** any screen, EPS surprise model, or P/E calculation using GAAP EPS is misleading by a factor of ~3x this quarter. Trade the operating line; discount the headline beat.

### Why core EPS (+16%) lags operating income (+43%): the tax‑rate shock
Q2 2025 effective tax rate was **12.8%** ($2,678M / $20,857M). On the pre‑mark base, Q2 2026's residual rate is roughly **24.9%**. Holding the prior 12.8% rate, core EPS would have been ≈ **$2.20 (+31% YoY)**. The ~12pp tax‑rate step‑up is the main bridge between +43% operating income and +16% core EPS — a structural headwind to model for the rest of the year, not a one‑off distortion.

### Operating expense detail (efficiency check)
| $ millions | H1 2026 | H1 2025 | YoY | Comment |
|---|---|---|---|---|
| Depreciation & amortization | 38,933 | 29,489 | **+32.0%** | Direct consequence of the capex ramp |
| Marketing | 22,012 | 21,179 | +3.9% | Sharp deceleration vs +18% revenue = leverage |
| G&A | 5,375 | 5,593 | **−3.9%** | Absolute cost cut |
| Share‑based comp | 10,070 | 10,223 | **−1.5%** | Flat/declining despite 18% growth — high quality |
| Operating lease cost | 8,035 | 6,666 | +20.5% | Logistics/AI datacenter footprint |
| Interest expense (non‑op) | 2,114 | 1,057 | **+100%** | Q2 alone: $1,314M vs $516M (+155%) |
| Interest/investment income | 2,430 | 2,151 | +13.0% | Now barely above interest expense |
| Net income (TTM) | 135,281 | 70,623 | +91.6% | mark‑to‑market inflated |

Key read‑through: **revenue grew 18%, total costs 16%, D&A 32% — yet operating income grew 37%.** That is genuine mix/leverage (higher‑margin AWS/ads, cost discipline in marketing and G&A, flat SBC), not accounting. It is the bull case in one line.

---

## 4. Balance sheet — still liquid, but the shape has changed materially

| $ millions | 2026‑06‑30 | 2025‑12‑31 | Change |
|---|---|---|---|
| Cash & equivalents | 78,213 | 86,810 | −8,597 |
| Marketable (AFS) securities | 97,900 | 45,800 | **+52,100** |
| **Cash + securities** | **176,113** | 132,610 | **+43,503** |
| Accounts receivable, net | 88,092 | 67,729 | **+30.1%** |
| Inventory, net | 38,184 | 38,325 | −0.4% |
| **Non‑marketable equity securities** | **122,300** | **16,200** | **+106,100 (+655%)** |
| Total current assets | 249,264 | 229,083 | +8.8% |
| **Total assets** | **1,095,689** | **818,042** | **+277,647 (+33.9%)** |
| Accounts payable | 147,440 | 121,909 | +20.9% |
| Accrued liabilities | 73,406 | 75,520 | −2.8% |
| Current liabilities | 241,274 | 218,005 | +10.7% |
| Long‑term debt (total) | **132,995** | 68,836 | **+64,159 (+93%)** |
| — of which current | 3,330 | 2,748 | +21% |
| Finance lease liabilities | 13,451 | 12,286 | +9.5% |
| Operating lease liabilities | 96,320 | 89,252 | +7.9% |
| Contract liabilities (deferred revenue) | 24,928 | 25,000 | −0.3% |
| AOCI | 66,287 | 28,230 | **+38,057** |
| Additional paid‑in capital | 149,619 | 140,024 | +9,595 |
| Shares outstanding | 10,783M | 10,731M | +52M (+0.5%) |

**Ratios / derived observations**
- **Current ratio 1.03x** (249,264 / 241,274) — thin, but Amazon runs negative working capital by design; $45B quarterly operating cash flow covers the $78.1B of contractual obligations due within 12 months (2.6x coverage on one quarter of OCF).
- **Gross debt + leases:** $132,995M LT debt + $13,451M finance leases + $96,320M operating leases = **$242.8B**, vs $176.1B of cash+securities → **net debt ≈ $66.7B**, up from ≈ **$37.8B** at 2025‑12‑31 (net debt more than +$29B in six months).
- **Total contractual obligations: $650.0B** at 2026‑06‑30 (up from a $464.9M "remainder of FY2026" figure at Q1; total grew from $634B-ish trajectory), of which **$78.1B is due within 12 months**. This is largely leases and content/power/capex purchase commitments — a genuine fixed‑cost ratchet if demand disappoints.
- **Stockholders' equity cannot be read directly** from the returned fact set (retained earnings and PP&E lines were not in the payload). It is bounded above by assets less identified liabilities ≈ **$627B**, and its growth in H1 is explained by $92.9B of net income, $38.1B of AOCI gains and $9.6B of APIC/SBC. I will not publish a precise ROE given the missing denominators.
- **Watch item — receivables:** AR +30.1% vs revenue +18.2%. Some of this is mix (advertising and AWS bill in arrears) and some may be timing, but a 12pp gap is the kind of divergence that precedes a receivables write‑down discussion. Allowance rose modestly ($2.4B → $2.8B), which is proportionate.
- **Watch item — inventory:** flat at $38.2B on 18% revenue growth, with valuation reserves *down* ($3.3B → $3.0B). This is a clean, well‑managed 1P inventory position and argues against a margin‑resetting clearance event.

### The $122.3B investment book is now a balance‑sheet pillar
Non‑marketable equity securities went from **$16.2B to $122.3B** — now **11.2% of total assets** and plausibly a large fraction of book equity. Practical consequences for traders:
1. **Reported book value, ROE and P/B are no longer clean operating measures** — they're partly a venture‑style mark. If that asset marks down, GAAP EPS and book value take a large hit with zero cash effect.
2. Conversely, the **+$50.5B Q2 mark implies the fair value of the underlying holdings is now validated at a much higher level** — real embedded value, but illiquid.
3. `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` also matters for the **warrant/derivative lines** (FairValueAdjustmentOfWarrants −$1,449M in Q2) — a growing, noisy non‑operating bucket. Anyone modeling "clean" EPS must strip **non‑operating income entirely** ($69.4B H1 2026 vs $5.0B H1 2025).

---

## 5. Cash flow — the capex supercycle is the real story

| $ millions | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | **TTM (Jul‑25→Jun‑26)** | Prior TTM |
|---|---|---|---|---|---|---|
| Operating cash flow | 45,387 | 32,515 | 71,419 | 49,530 | **161,403** | 121,137 (+33.2%) |
| Capex (productive assets) | 54,208 | 32,183 | 98,411 | 57,202 | **173,028** | 107,656 (+60.7%) |
| **Free cash flow (OCF − capex)** | **−8,821** | +332 | **−26,992** | −7,672 | **−11,625** | +13,481 |
| Capex / revenue | **27.0%** | 19.2% | **25.8%** | 17.7% | — | — |
| Acquisitions (net of cash) | 24,359 | 1,700 | 39,767 | 1,652 | **41,956** | 4,809 |
| Investing cash flow | −79,245 | −39,424 | −143,457 | −69,227 | −216,775 | −123,569 |
| Financing cash flow | +10,146 | −2,539 | **+62,913** | −2,586 | **+75,160** | −8,652 |
| — LT debt issued | 13,557 | 0 | 66,998 | 746 | **81,925** | 746 |
| — ST debt issued / repaid | 9,368 / 9,573 | 2,093 / 1,392 | 15,386 / 15,682 | 3,908 / 3,474 | 20,798 / 20,634 | — |
| LT debt repaid | 2,752 | 2,751 | 2,752 | 2,751 | 5,022 | 7,434 |
| Finance lease principal | 395 | 411 | 863 | 821 | 1,599 | 1,556 |
| Net change in cash (incl. FX) | −23,765 | −8,440 | −9,179 | −20,859 | +19,474 | −10,220 |

**Interpretation — the central tension in the stock right now:**
- **Operating cash flow is compounding at +33% TTM** ($161.4B), an excellent number.
- **But capex is compounding at +61% TTM** ($173.0B) and reached **27% of Q2 revenue**. The result is **negative trailing free cash flow of −$11.6B**, a ~$25B swing from +$13.5B a year ago, and **−$27.0B in H1 2026 alone**.
- The gap has been funded almost entirely with **debt: $81.9B of long‑term notes issued TTM** (vs $0.7B a year earlier) plus $20.8B short‑term. There were **no buybacks in the fact set** and **no dividends**. This is a textbook "fund the build‑out with the balance sheet" phase.
- **Second‑order cost:** depreciation and amortization is already **+32% YoY** (H1: $38.9B) and TTM D&A of $75.2B against TTM capex of $173.0B (2.3x) means the D&A ramp has years left to run. Interest expense **doubled YoY** in H1 and **+155% in Q2**. Both are growing faster than revenue — the margin tailwind has a shelf life, and 2027 consensus needs to carry this.
- **Quality check on the OCF:** the $161.4B TTM OCF is *more* impressive than it looks given that TTM cash taxes paid were only **$6.6B** (vs $11.8B prior TTM) — because tax expense is largely deferred on the investment mark. Conversely, OCF is *less* impressive than it looks in that it benefited from working‑capital swings (accrued liabilities a $6.1B drag, receivables/other assets a $21.4B use — the signs in this feed are not normalized, so I'd only rely on the aggregate OCF figure).

---

## 6. Financial history context

The returned fact set is a **point‑in‑time snapshot centered on the June‑2026 10‑Q plus the March‑2026 10‑Q**, not a multi‑year archive. What can be reconstructed reliably:

- **Revenue trajectory (derived):** Q1 2026 $181.5B → Q2 2026 $200.6B. YoY growth **accelerated from +16.6% in Q1 to +19.6% in Q2** — the strongest trend line in the dataset and the most important single takeaway.
- **Operating margin trajectory:** 11.8% (Q1 2025) → 11.4% (Q2 2025) → 13.1% (Q1 2026) → 13.7% (Q2 2026). Two consecutive quarters of clear expansion; H1 2026 13.4% vs H1 2025 11.6%.
- **TTM windows available** (Jul 2025 – Jun 2026 vs Jul 2024 – Jun 2025): net income $135.3B vs $70.6B; OCF $161.4B vs $121.1B; capex $173.0B vs $107.7B; D&A $75.2B vs $58.6B; SBC (H1 comparison) −1.5%; acquisitions $42.0B vs $4.8B.
- **Not available:** FY2024/FY2025 full‑year totals (the annual request returned the identical snapshot — the vendor has no annual history cached for AMZN here), PP&E/goodwill/retained earnings line items, segment revenue/operating income, Q3 guidance, and any market price/valuation data.

---

## 7. Actionable insights for the trading desk

**Bull case (evidence‑backed)**
1. **Revenue growth inflected upward** (+16.6% → +19.6% YoY) on a ~$780B annualized revenue base — this is the hardest thing to fake and it is the strongest data point in the filing.
2. **Operating leverage is real:** operating income +43% YoY in Q2 with gross margin +45 bps, marketing +4%, G&A −4%, SBC −1.5%. Cost discipline is funding the AI build.
3. **Liquidity is ample:** $176B cash + securities vs $78B of obligations due in 12 months; OCF covers contractual maturities roughly 2x per quarter.
4. **Embedded asset value:** the $122.3B private‑equity book, validated upward by $62.8B of H1 marks, is optionality not visible in operating multiples.

**Bear case / risk map**
1. **Earnings quality:** ~80% of Q2 net income and ~68% of H1 net income is a non‑cash mark. Any compression in that private asset's valuation produces a headline EPS collapse with no cash impact — expect multiple expansion/contraction on noise.
2. **Negative FCF (−$11.6B TTM) and 27% capex intensity** — the market is being asked to underwrite an unproven return on $173B/yr of spend. History (2022) shows how quickly this de‑rates when growth wobbles.
3. **Debt ramp +93% in six months** ($68.8B → $133.0B) with interest expense doubling → rising sensitivity to rates/credit spreads, and rising finance costs are now eating the investment‑income cushion ($2.43B vs $2.11B).
4. **Tax‑rate step‑up** (~12.8% → ~25% core) means even +43% operating income translates to only ~+16% core EPS.
5. **Receivables +30% vs revenue +18%** — monitor for a working‑capital/collection issue.
6. **Fixed‑cost ratchet:** $650B of contractual obligations including $78.1B due within 12 months.

**Concrete things to do / monitor**
- **Trade the operating line, not the EPS line.** Build models on operating income ($27.5B Q2, 13.7% margin) and label the equity mark separately. A "clean EPS" screen on AMZN will show it as wildly expensive/cheap incorrectly.
- **Track `PaymentsToAcquireProductiveAssets` quarterly:** Q2 was $54.2B. A further step‑up in Q3 with flat OCF growth is a de‑rating trigger; a flattening capex curve with 13%+ operating margins is a re‑rating trigger.
- **Track D&A growth (+32%) vs operating income growth (+37%).** The crossover point where D&A growth exceeds operating income growth marks the end of the margin‑expansion narrative.
- **Track the deferred‑tax line:** $30.5B H1 / $41.4B TTM — as the mark unwinds, this reverses and can flatter future GAAP EPS.
- **Watch the $122.3B non‑marketable equity line each quarter.** A 30% markdown ≈ $37B pre‑tax hit to GAAP EPS (≈$2.6–3.0/share) with no cash effect — a buying opportunity if the market panic‑sells it, a real risk if the underlying thesis deteriorates.
- **Insider signal is missing** — the desk should source Form 4s independently before assuming management behavior.

---

## 8. Data quality & gaps (stated for transparency)

| Item | Status |
|---|---|
| Revenue, cost of revenue, operating income, net income, EPS, cash flow, balance sheet | ✅ Full, point‑in‑time, from 10‑Q accepted 2026‑07‑31 |
| Revenue line item | ⚠️ **Derived** as CostsAndExpenses + OperatingIncomeLoss (validated against prior‑year actuals) |
| Segment revenue / segment operating income | ❌ Not in fact set |
| FY2024 / FY2025 full‑year totals, PP&E, goodwill, retained earnings | ❌ Not returned (annual query = same snapshot) |
| Employee count, guidance, consensus, valuation multiples, price data | ❌ Not available |
| Insider transactions | ❌ **DATA_UNAVAILABLE** — no authorized archive; not inferred |
| Q1 2026 quarterly figures | ⚠️ Derived by subtraction (H1 − Q2) |

---

## 9. Key points summary

| Category | Metric / Point | Value | Direction | Trading Read‑Through |
|---|---|---|---|---|
| **Filing** | Latest 10‑Q accepted | 2026‑07‑31 (Q2 2026) | Fresh | Catalyst is ~2 weeks old; fully public |
| **Growth** | Q2 2026 revenue (derived) | $200.6B, +19.6% YoY | ▲ Accelerating (Q1: +16.6%) | Strongest fundamental signal in the dataset |
| **Growth** | H1 2026 revenue | $382.1B, +18.2% YoY | ▲ | Organic + M&A; supports margin story |
| **Profitability** | Q2 operating income | $27.46B, 13.7% margin (+225 bps) | ▲▲ | Genuine operating leverage |
| **Profitability** | H1 operating income | $51.31B, +36.6% YoY, 13.4% margin | ▲▲ | Core thesis intact |
| **Earnings quality** | Q2 non‑operating income | $53.4B (vs $1.7B LY) | ⚠️ | 80% of Q2 net income is a non‑cash mark |
| **Earnings quality** | H1 equity mark‑up (no ready FV) | $62.8B ($50.5B in Q2) | ⚠️ | Strip it: core EPS ≈ $1.95, +16% YoY |
| **EPS** | Q2 diluted EPS / core EPS est. | $5.75 reported / ~$1.95 core | ⚠️ | Headline 3x inflated; models must adjust |
| **Tax** | Q2 effective rate (core) | ~24.9% vs 12.8% LY | ▼ | ~12pp drag; caps EPS growth vs OI growth |
| **Cost control** | Marketing / G&A / SBC (H1 YoY) | +3.9% / −3.9% / −1.5% | ▲ | Best‑in‑class leverage vs +18% revenue |
| **Capex** | Q2 capex | $54.2B = 27.0% of revenue | ▲▲ | Supercycle; 61% TTM growth |
| **Cash flow** | TTM free cash flow | **−$11.6B** (was +$13.5B) | ▼▼ | Key bear argument; OCF +33% can't keep up |
| **Cash flow** | H1 2026 FCF | −$27.0B | ▼▼ | Capex $98.4B vs OCF $71.4B |
| **Financing** | LT debt issued TTM | $81.9B (vs $0.7B LY) | ▲▲ | Build‑out funded with balance sheet |
| **Leverage** | Long‑term debt | $133.0B, +93% in 6 months | ▲▲ | Interest expense +155% in Q2 |
| **Leverage** | Net debt incl. leases (est.) | ≈$66.7B (from ≈$37.8B) | ▲ | Rising but manageable vs $176B liquidity |
| **Liquidity** | Cash + marketable securities | $176.1B | ▲ | Ample; current ratio 1.03x |
| **Assets** | Non‑marketable equity securities | $122.3B (from $16.2B) | ▲▲ | 11.2% of assets; distorts book value/ROE |
| **Working capital** | Receivables | $88.1B, +30.1% in 6 months | ⚠️ | Outpacing revenue; monitor collections |
| **Working capital** | Inventory | $38.2B, −0.4% | ✅ | Clean; supports margin durability |
| **Obligations** | Total contractual obligations | $650.0B ($78.1B < 12 mo) | ⚠️ | Fixed‑cost ratchet; leases/purchase commitments |
| **Capital return** | Buybacks / dividends | None in fact set | — | 100% of capital to capex, M&A, debt |
| **Dilution** | Shares outstanding / unrecognized SBC | +0.5% in 6 mo; $24.8B | ⚠️ | ~1%/yr dilution; SBC flat YoY |
| **Insider** | Form 4 activity | **DATA UNAVAILABLE** | ❓ | Must be sourced externally; not inferred |
| **Bottom line** | Operating business | Accelerating, high‑quality margin expansion | ▲ | Buy the operating trend |
| **Bottom line** | Reported earnings / FCF | Mark‑inflated EPS, negative FCF, heavy debt issuance | ⚠️ | Fade the headline; underwrite capex ROI |

**Net assessment:** AMZN's *operating* fundamentals as of 2026‑08‑13 are the best in the dataset — accelerating 19%+ revenue growth with 43% operating‑income growth and visible cost leverage. But the *reported* results are heavily distorted by a $62.8B non‑cash investment mark, and the underlying cash engine has swung to negative free cash flow while funded by a near‑doubling of debt. The correct posture is to be constructive on the operating line, skeptical of the EPS line, and highly sensitive to the quarterly capex and D&A trajectory.