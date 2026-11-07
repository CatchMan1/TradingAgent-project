# AMZN — Fundamental Deep Dive
**Amazon.com, Inc. | Analysis date: 2026-09-22 | Anchor filing: Q2 2026 Form 10-Q (period ended 6/30/2026), accepted 2026-07-31**

---

## 1. Scope, provenance, and what is *not* in this data set

This report is built entirely from the point-in-time SEC XBRL extract available to the tools as of 2026-09-22. That has three important consequences:

- **No new filings in the past week.** The most recent accepted document in the package is the Q2 2026 10-Q (accepted 2026-07-31 02:11 UTC). There is no 8-K, earnings release, Form 4, or Q3 pre-announcement inside the window. The "current" fundamental picture is therefore the 6/30/2026 balance sheet and the 1H26 income/cash-flow statement.
- **Revenue is not a tagged line in the extract** (the feed is truncated alphabetically before the revenue tag). I derive it from the XBRL identity **Revenue = CostsAndExpenses + OperatingIncomeLoss**, which reconciles exactly across every period. All revenue, gross profit, and margin figures below are *derived* on that basis and are marked as such.
- **Not available:** company profile/segment P&L (only `NumberOfOperatingSegments = 3` is tagged), R&D expense, headcount, total stockholders' equity/retained earnings, FY2025 annual comparatives, buyback/dividend line items, share price, market cap, consensus estimates, and **insider transactions** (`DATA_UNAVAILABLE` — no authorized point-in-time archive; I make no inference about insider buying or selling).

---

## 2. Headline: a genuinely strong operating quarter wrapped around a very noisy GAAP number

| $M unless noted | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 | Q2 y/y |
|---|---:|---:|---:|---:|---:|
| Revenue (derived) | 155,667 | 167,702 | 181,519 | 200,606 | **+19.6%** |
| Gross profit (derived) | 78,691 | 86,893 | 94,056 | 104,828 | +20.7% |
| Gross margin | 50.6% | 51.8% | 51.8% | **52.3%** | +45 bp |
| Operating income | 18,405 | 19,171 | 23,852 | 27,461 | **+43.2%** |
| Operating margin | 11.8% | 11.4% | 13.1% | **13.7%** | +226 bp |
| Non-operating income | 2,174 | 1,686 | 15,982 | 53,396 | n.m. |
| Pre-tax income | 21,659 | 20,857 | 39,834 | 80,857 | +287.7% |
| Tax | 4,553 | 2,678 | 9,560 | 18,199 | — |
| Effective tax rate | 21.0% | **12.8%** | 24.0% | **22.5%** | +970 bp |
| Net income | 17,127 | 18,164 | 30,255 | 62,647 | +244.9% |
| Diluted EPS | 1.59 | 1.68 | 2.78 | **5.75** | +242% |
| **Adj. EPS (ex private-stake marks, est.)** | ~1.59 | ~1.68 | **~1.91** | **~2.16** | **+29%** |

**1H26 vs 1H25:** revenue $382,125M vs $323,369M (**+18.2%**); operating income $51,313M vs $37,576M (**+36.6%**); operating margin **13.4% vs 11.6% (+185 bp)**; net income $92,902M vs $35,291M; diluted EPS $8.53 vs $3.27.

**Cost-line proof that the margin expansion is real, not mix-driven or one-off:**
- 1H26 cost of sales +16.1% ($183.2B vs $157.8B) vs revenue +18.2% → **gross margin +85 bp**.
- 1H26 operating expense ex-COGS +15.3% ($147.6B vs $128.0B) while revenue +18.2% → **opex ratio 38.6% vs 39.6%, −100 bp**.
- Marketing expense +3.9% only ($22.0B vs $21.2B); marketing is now **5.8% of revenue vs 6.8%**.
- G&A **−3.9%** ($5.4B vs $5.6B); **1.39% of revenue vs 1.77%**.
- SBC **$10.07B vs $10.22B (−1.5%)** despite 18% revenue growth — stock comp is deleveraging (2.6% of revenue). Unrecognized SBC $24.8B.

This is textbook operating leverage: every major cost line grew slower than revenue, with the largest discipline in marketing and G&A. That is the single most important fundamental fact in the package.

---

## 3. Earnings quality — the $62.8B item traders must strip out

1H26 non-operating income was **$69.4B vs $5.0B** a year earlier. The driver is disclosed explicitly:

- `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment`: **$62,814M in 1H26** ($50,486M in Q2 alone), versus $86M in 1H25.
- The carrying value of non-marketable equity securities jumped from **$16.2B (12/31/25) to $122.3B (6/30/26)** — a **+$106.1B** move and now **~11% of total assets**.
- Other non-operating noise: equity securities FV gain $1.3B in Q2, warrant FV *loss* of $1.4B in Q2 (vs −$0.6B), FX gain $0.2B, interest income $1.3B, interest expense $1.3B.

**Tax-effected adjustment (assuming the ~22.5% Q2 effective rate):**

| | Reported | Less: mark-up × (1−tax) | Adjusted |
|---|---:|---:|---:|
| Q2 2026 net income | $62,647M | −$39,113M | **$23,534M** |
| Q2 2026 diluted EPS | $5.75 | −$3.59 | **~$2.16** |
| 1H26 net income | $92,902M | −$48,367M | **$44,535M** |
| 1H26 diluted EPS | $8.53 | −$4.44 | **~$4.09** |

**Read-through:**
- Adjusted EPS still grew **~29% y/y in Q2** and **~25% in 1H26**, and that is *after* absorbing a ~970 bp higher tax rate and a 2.5x increase in interest expense. Underlying earnings power is accelerating.
- But **annualizing the $8.53 1H EPS (~$17.06) overstates run-rate earnings by roughly 2x** versus the ~$8.20 adjusted 1H run-rate. Any screen, model, or narrative that capitalizes the GAAP number is wrong.
- **The mark is reversible.** A 10% markdown on the $122.3B book = **~$12.2B pre-tax / ~$0.87 per diluted share**. A 25% markdown = ~$2.18/share. This is now a material, recurring-volatility P&L item, and it sits on Level 3 / transaction-based valuations, not observable prices.
- Timing matters: Q2 carried **80% of the 1H mark-up** ($50.5B of $62.8B). Q1 was already flattered by $12.3B. Do not extrapolate the Q2 step-up.

---

## 4. Cash flow — the capex super-cycle has turned FCF negative

| $M | 1H 2025 | 1H 2026 | TTM Jun-25 | TTM Jun-26 |
|---|---:|---:|---:|---:|
| Operating cash flow | 49,530 | **71,419** | 121,137 | **161,403** |
| Capex (productive assets) | 57,202 | **98,411** | 107,656 | **173,028** |
| **Free cash flow** | **(7,672)** | **(26,992)** | **+13,481** | **(11,625)** |
| Acquisitions, net of cash | 1,652 | **39,767** | 4,809 | **41,956** |
| FCF after acquisitions | (9,324) | **(66,759)** | 8,672 | **(53,581)** |
| D&A | 29,489 | 38,933 | 58,562 | 75,200 |
| SBC | 10,223 | 10,070 | — | — |

**Key observations:**
- OCF growth is excellent: **+44% in 1H26**, **+33% TTM**. Q2 OCF alone was $45.4B (+40% y/y).
- Capex grew **+72% in 1H26** and **+61% TTM**, reaching **25.8% of 1H26 revenue vs 17.7%** a year ago. Capex is **2.5x D&A**, i.e. the asset base is still compounding fast — depreciation is a 2027+ headwind, not yet a 2026 one.
- The company is now **FCF-negative on a TTM basis (−$11.6B)** and **−$67B after M&A in 1H26 alone.** This is the core bear argument and the reason the balance sheet is being levered.
- **OCF quality check:** the $62.8B mark-up is *excluded* from OCF (it is non-cash, non-operating), so OCF is not inflated by the marks. However, cash taxes paid were only **$3,978M against $27,759M of book tax expense in 1H26** (~14% cash realization), with deferred tax expense of **$30,489M**. Roughly **$24B of tax deferral** is embedded in 1H26 OCF and will normalize over time. Adjusted for that, 1H26 OCF conversion is closer to $47B — still solid versus $44.5B adjusted net income, but not the 1.6x headline conversion.
- Adjusted OCF ($71.4B) still does not cover capex ($98.4B). **The funding gap is structural until capex growth decelerates.**

---

## 5. Balance sheet — transformed in six months, but comfortably liquid

| $M | 12/31/2025 | 6/30/2026 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 86,810 | 78,213 | −8,597 |
| Available-for-sale securities | 45,800 | 97,900 | **+52,100** |
| **Cash + securities** | **132,610** | **176,113** | **+43,503** |
| Accounts receivable, net | 67,729 | 88,092 | +20,363 |
| Inventory | 38,325 | 38,184 | −141 |
| Total current assets | 229,083 | 249,264 | +20,181 |
| Accounts payable | 121,909 | 147,440 | +25,531 |
| Total current liabilities | 218,005 | 241,274 | +23,269 |
| **Current ratio** | **1.05x** | **1.03x** | −0.02x |
| Long-term debt (current + non-current) | 68,836 | **132,995** | **+64,159 (+93%)** |
| Finance lease liabilities | 12,286 | 13,451 | +1,165 |
| Operating lease liabilities | 89,252 | 96,320 | +7,068 |
| Non-marketable equity securities | 16,200 | **122,300** | **+106,100** |
| Total assets | 818,042 | 1,095,689 | **+277,647 (+34%)** |
| AOCI | 28,230 | 66,287 | +38,057 |
| Additional paid-in capital | 140,024 | 149,619 | +9,595 |
| Shares outstanding | 10,731M | 10,783M | +0.5% |

**Liquidity and coverage — no distress signals:**
- **Net cash position: ~$29.7B** (cash + AFS $176.1B less debt + finance leases $146.4B), down from ~$51.5B at year-end but still positive.
- Of the $97.9B AFS portfolio, **$96.5B matures within one year** — it is functionally cash. The 1.03x current ratio is therefore not a liquidity constraint.
- **Total debt / TTM OCF = 0.91x.** Interest coverage: **24.3x** in 1H26 (operating income $51.3B / interest $2.1B) and **20.9x** in Q2. Interest expense did double y/y ($2,114M vs $1,057M in 1H; $1,314M vs $516M in Q2), and will keep climbing with the new debt, but it remains ~4% of operating income.
- **Working-capital economics remain a moat:** AP of $147.4B covers **85% of a full quarter of total costs** ($173.1B). Receivables of $88.1B represent ~40 days of revenue; inventory ~36 days of COGS. Supplier financing, not equity, funds the working capital.
- AR grew **+30%** vs revenue +18% — worth watching, but consistent with a mix shift toward advertising/cloud receivables and a $24.4B Q2 acquisition. Inventory was flat y/y, a genuinely good signal on retail efficiency.
- The **+$38.1B AOCI increase** is not explained by the tagged AFS data (the AFS portfolio shows only ~$60M of net unrealized loss at 6/30/26, and FX translation was −$1.6B in 1H26). Flag this as an item to reconcile in the 10-Q text; do not build a thesis on it.

---

## 6. Capital deployment — the real story behind the debt raise

Three uses of capital dominate 1H26:

1. **Capex: $98.4B** in six months, $173.0B TTM.
2. **Business acquisitions: $39.8B** in six months ($15.4B in Q1 + **$24.4B in Q2**), versus just $1.7B in 1H25 and $4.8B TTM a year ago.
3. **Non-marketable equity investments:** beginning book $16.2B + $62.8B of upward marks = $79.0B; ending book $122.3B implies **~$43B of net new private-equity deployment** in 1H26 (residual, net of any downward adjustments or disposals).

Combined, that is **~$181B of capital committed in six months** — funded by $71.4B of OCF, **$67.0B of long-term debt issuance** (plus $15.4B short-term, largely rolled), and a $8.6B draw on cash. The 93% increase in long-term debt is not distress; it is deliberate, cheap financing of an infrastructure and strategic-investment build-out. But it does mean **AMZN has shifted from a net-cash-generating self-funder to a leveraged growth spender**, and the market will re-rate it on FCF inflection rather than on EPS.

- Debt maturities are well laddered: $78.1B due within 12 months (mostly commercial paper/short-term), $53.4B in year two, $46.8B in year three, $42.2B in year four — against $176B of liquid assets.
- Share count rose only **+0.5%** in six months and diluted shares are ~10.89B; there is **no evidence of meaningful buybacks** in the extract, and no dividend.

---

## 7. Segment and business context

Only `NumberOfOperatingSegments = 3` is tagged — no segment revenue or profitability is in this package. Qualitatively, AMZN reports **North America, International, and AWS**, plus a large advertising business inside the segment disclosures. The 19.6% Q2 revenue growth is well above AMZN's recent historical run-rate; given the $24.4B Q2 acquisition, **part of that acceleration may be inorganic**, and the extract cannot separate the two. That is the single biggest analytical gap in this report and the first question to resolve from the 10-Q MD&A.

---

## 8. Insider activity

**No data.** The vendor explicitly reports: *"the B-project data package has no authorized, point-in-time insider-transactions archive for AMZN by 2026-09-22. Do not infer or fabricate insider activity."* I therefore make **no** claim about insider buying or selling, and no signal should be read into the absence of Form 4 data.

---

## 9. Actionable conclusions for traders

**Bull case (supported by the data):**
1. **Operating leverage is inflecting hard** — +185 bp of margin on +18% revenue, with marketing and G&A actually shrinking as a share of sales. Operating income grew 43% in Q2 on 20% revenue growth.
2. **Adjusted EPS growth of ~29% y/y** survives a near-doubling of interest expense and a ~970 bp higher tax rate.
3. **Liquidity is ample** — $176B cash + securities, net cash positive, 21–24x interest coverage, 0.91x debt/OCF.
4. **Hidden asset value:** the $122.3B private-equity book is carried at transaction marks and is not in operating earnings; it is a call option on the AI ecosystem, and it has already produced $62.8B of realized-in-book gains in six months.

**Bear case (equally supported):**
1. **FCF is negative** — TTM −$11.6B, 1H26 −$27.0B, −$66.8B after acquisitions. Capex at 25.8% of revenue and rising is the swing factor.
2. **Earnings quality:** $62.8B of the $92.9B 1H26 net income is a non-cash mark. Headline EPS of $8.53 is roughly 2x the adjusted run-rate.
3. **The mark can reverse:** 10% = ~$0.87/share; 25% = ~$2.18/share. And it is Level 3.
4. **Debt doubled** to $133.0B in six months; interest expense +155% y/y in Q2 and rising.
5. **Cash taxes at 14% of book tax** will normalize, removing ~$24B of annualized OCF support.

**How to trade the setup:**
- **Do not use GAAP EPS for valuation.** Use ~$4.09 (1H26 adjusted) or ~$8.2 annualized run-rate, and treat the mark as a separate, marked-to-model asset.
- **The next real catalyst is the Q3 2026 report (late October).** Nothing in this package is newer than 7/31/26. Watch, in order: (a) capex guidance and whether the +72% growth rate is the peak — a plateau is the single largest positive catalyst for FCF and the stock; (b) AWS revenue growth and any disclosure of acquisition contribution to the 19.6% top-line; (c) any additional upward/downward adjustment to the $122.3B private book; (d) new debt issuance and the interest expense trajectory; (e) cash taxes paid versus book expense.
- **Positioning asymmetry:** operating earnings are compounding faster than the multiple can compress, but the FCF hole and the mark-to-model asset cap multiple expansion. A capex-growth rollover would be worth far more than another quarter of mark-ups.
- **Risk triggers to pre-define:** an 8-K for a large new debt raise; a disclosed impairment/downward adjustment on non-marketable securities; a jump in cash taxes toward the 20%+ book rate; current ratio falling below 1.0x (it is 1.03x and dependent on $96.5B of <1-year securities).

---

## 10. Key points summary

| Area | Key data point (as of 6/30/26) | Read-through / action |
|---|---|---|
| Filing anchor | Q2 2026 10-Q, accepted 2026-07-31; no newer SEC filing in the past week | Fundamentals are 7+ weeks stale; trade off Q3 print, not this data |
| Revenue (derived) | Q2 $200.6B (+19.6% y/y); 1H $382.1B (+18.2%) | Growth accelerating Q1→Q2, but may include $24.4B Q2 acquisition — verify organic |
| Operating income | Q2 $27.5B (+43.2%); 1H $51.3B (+36.6%) | Genuine operating leverage; the cleanest bullish signal |
| Operating margin | Q2 13.7% vs 11.4%; 1H 13.4% vs 11.6% (+185 bp) | Cost discipline across COGS, marketing (−100 bp of sales), G&A (−38 bp) |
| GAAP EPS | Q2 $5.75; 1H $8.53 | **Not run-rate** — inflated by non-cash marks |
| Adjusted EPS (est.) | Q2 ~$2.16 (+29%); 1H ~$4.09 (+25%) | Use this for valuation and for judging beats/misses |
| Non-cash mark-up | $50.5B in Q2, $62.8B in 1H26 on private equity stakes | 10% reversal ≈ $0.87/share; 25% ≈ $2.18/share |
| Private equity book | $122.3B vs $16.2B at 12/31/25 (+$106.1B); ~11% of assets | Hidden asset *and* Level-3 volatility source; ~$43B net new money deployed |
| Operating cash flow | 1H $71.4B (+44%); TTM $161.4B (+33%) | Strong, but includes ~$24B tax deferral (cash tax $4.0B vs $27.8B book) |
| Capex | 1H $98.4B (+72%); TTM $173.0B (+61%); 25.8% of 1H revenue | The swing variable; watch for a growth-rate plateau as the bull catalyst |
| Free cash flow | TTM −$11.6B (vs +$13.5B); 1H −$27.0B; −$66.8B after M&A | Core bear point; structurally negative until capex decelerates |
| Debt | LT debt $133.0B (+93% in 6 mo); total incl. finance leases $146.4B | Deliberate, cheap funding — but interest expense +155% y/y in Q2 |
| Net cash | ~$29.7B (cash + AFS $176.1B less debt $146.4B), down from $51.5B | Still net cash; no solvency concern |
| Coverage / liquidity | Interest coverage 24.3x (1H); current ratio 1.03x; $96.5B of AFS matures <1 yr | Ample liquidity despite thin current ratio |
| Working capital | AP $147.4B = 85% of a quarter of total costs; inventory flat y/y; AR +30% | Supplier-funded model intact; AR growth bears watching |
| Capital deployment | $98.4B capex + $39.8B acquisitions + ~$43B private investments in 1H26 | ~$181B committed in six months — an infrastructure/strategic arms race |
| SBC / dilution | SBC $10.07B (−1.5% y/y); diluted shares ~10.89B; count +0.5% in 6 mo | Comp leverage improving; no meaningful buyback visible |
| Insider activity | **DATA_UNAVAILABLE** — no authorized archive | No signal; do not infer buying or selling |
| Next catalyst | Q3 2026 results/10-Q, expected late October 2026 | Focus: capex guide, AWS growth, organic vs acquired revenue, new marks, debt |

**Bottom line:** AMZN's *operating* engine is the strongest it has been in this data set — 18% growth with 185 bp of margin expansion and 43% operating-income growth. But the *reported* earnings are roughly half mark-up, free cash flow has turned negative, and the balance sheet has been levered by ~$64B in six months to fund an extraordinary capex and strategic-investment program. Underwrite the operating trend, discount the GAAP EPS, and treat capex deceleration plus mark-to-model stability as the two variables that determine the next leg.