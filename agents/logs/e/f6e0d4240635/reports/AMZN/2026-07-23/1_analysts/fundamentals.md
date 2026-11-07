# AMZN — Fundamental Research Report
**Company:** Amazon.com, Inc. (AMZN) | **Analysis date:** 2026-07-23
**Primary sources:** Form 10-Q for Q1 2026 (period ended 2026-03-31, accepted 2026-04-30, acc. 0001018724-26-000014) and Form 10-K for FY2025 (filed 2026-02-06, acc. 0001018724-26-000004), plus a Q3 2025 10-Q slice (accepted 2025-10-31). All figures are point-in-time SEC XBRL facts, USD.
**Data caveats up front:** (1) The latest filed period is **Q1 2026 (March quarter)** — the June-2026 quarter is **not yet in the dataset**, and Amazon's Q2 print would historically land in the last week of July, i.e. imminently (calendar inference, not a data fact). (2) **Insider transactions: DATA_UNAVAILABLE** — the data package has no authorized insider archive for AMZN as of 2026-07-23; nothing below should be read as insider activity. (3) Full-year *revenue* and *net income* line items were not returned in the annual slice, so some FY aggregates are shown as trailing-twelve-month (TTM Apr-2025→Mar-2026) or derived and are labelled as such.

---

## 1. Company profile (as evidenced in the filings)
- **Structure:** Three operating segments are reported in the Q1 2026 10-Q (`NumberOfOperatingSegments = 3`) — the standard North America / International / AWS split.
- **Revenue model:** `RevenueFromContractWithCustomerExcludingAssessedTax` is the single revenue line ($181.5B in Q1 2026), i.e. a consolidated contract-revenue presentation; the mix (online stores, third-party seller services, advertising, subscription, AWS) is disclosed in the 10-Q text but not as separate XBRL facts in this slice.
- **Cost skeleton (Q1 2026, $M):** cost of goods & services sold 87,463; marketing 10,314; G&A 2,587; other operating expense, net 447; total costs & expenses 157,667. The residual (≈56,856) is fulfilment + technology & content — the two lines that house AWS infrastructure, AI compute and logistics.
- **Advertising:** advertising *expense* rose 20.3B (FY23) → 21.4B (FY24) → 23.5B (FY25) per the 10-K.
- **Capital return:** No treasury-stock, buyback or dividend tags appear anywhere in the dataset — consistent with Amazon's long-standing zero-dividend, zero-buyback policy.
- **Share count:** 10,754M shares outstanding at 2026-03-31; 10,757.1M as of 2026-04-22 (`EntityCommonStockSharesOutstanding`). Diluted weighted average ≈10,883M (derived: 30,255/2.78).

This is a **hyper-capex, AI-infrastructure-led growth company that has crossed into GAAP-profitability at scale**, and in Q1 2026 it began funding that buildout with **large-scale debt issuance** for the first time in years. That is the central fundamental story.

---

## 2. Q1 2026 income statement — strong operations, flattered by a mark-up

| $M unless noted | Q1 2026 | Q1 2025 | Δ |
|---|---|---|---|
| Revenue | 181,519 | 155,667 | **+16.6%** |
| Cost of goods & services | 87,463 | 76,976 | +13.6% |
| Gross profit (derived) | **94,056** | **78,691** | **+19.5%** |
| Gross margin | **51.8%** | 50.6% | +120 bps |
| Marketing | 10,314 | 9,763 | +5.6% |
| G&A | 2,587 | 2,628 | −1.6% |
| Total costs & expenses | 157,667 | 137,262 | +14.9% |
| **Operating income** | **23,852** | **18,405** | **+29.6%** |
| Operating margin | **13.1%** | 11.8% | +130 bps |
| Interest expense | 800 | 541 | +47.9% |
| Investment income | 1,135 | 1,066 | +6.5% |
| Other non-operating income | **15,647** | 2,749 | +469% |
| Non-operating income, net | 15,982 | 3,274 | +388% |
| Pre-tax income | 39,834 | 21,679 | +83.7% |
| Income tax | 9,560 | 4,553 | +110% |
| Effective tax rate | **24.0%** | 21.0% | +300 bps |
| **Net income** | **30,255** | **17,127** | **+76.7%** |
| Diluted EPS | **$2.78** | $1.59 | +74.8% |
| Basic EPS | $2.82 | $1.62 | +74.1% |

### The single most important item: a $12.3B non-cash mark-up
- `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount` = **$12,328M in Q1 2026 vs $37M in Q1 2025**.
- Correspondingly, the carrying value of non-marketable equity securities (`EquitySecuritiesWithoutReadilyDeterminableFairValueAmount`) jumped **$16.2B → $48.1B** in one quarter (+197%), while `OtherAssetsNoncurrent` rose $122.6B → $151.8B.
- That gain flows through "other non-operating income" and is the dominant driver of the 388% non-operating swing and of the 76.7% EPS growth.

**Normalised view (my estimate, using the 24.0% effective rate):** strip the $12.3B gain and Q1 2026 pre-tax income is ≈**$27.5B** (+26.9% y/y), net income ≈**$20.9B**, EPS ≈**$1.92** (+≈21% y/y). Also present but smaller: an $883M mark-*down* on marketable equity securities (`EquitySecuritiesFvNiGainLoss`) and a $398M warrant fair-value adjustment.

**Trader takeaway:** Q1 2026 headline EPS of $2.78 is roughly **$0.80–0.86 of one-off, mark-to-model equity gains**. The *operating* story is still excellent — +29.6% operating income on +16.6% revenue, +130bps operating margin — but anyone extrapolating the printed $2.78 is over-earning the quarter. Also note this asset is now a **$48B+ volatile, valuation-marked stake** that can reverse just as violently in a risk-off AI tape.

### Opex leverage detail
Marketing grew just 5.6% and G&A fell 1.6% against 16.6% revenue growth — genuine cost discipline in overheads. The offset: implied fulfilment + tech/content + other rose ≈19.5% (≈31.3% of revenue vs 30.6%), i.e. **the capex/AI build is now visible in the P&L as depreciation**. Depreciation alone went $9,056M → $12,834M (+41.7%); total D&A $14,262M → $18,945M (+32.8%). This is the mechanism by which the $150B capex programme will compress future margins.

---

## 3. Multi-year history (annual, from the 10-K/10-Q facts)

| $M | FY2023 | FY2024 | FY2025 | TTM (Apr-25→Mar-26) |
|---|---|---|---|---|
| Operating cash flow | 84,946 | 115,877 | 139,514 | **148,531** |
| Capex (productive assets) | 52,729 | 82,999 | 131,819 | **151,003** |
| **FCF (OCF − capex)** | **32,217** | **32,878** | **7,695** | **−2,472** |
| Investing cash flow | −49,833 | −94,342 | −142,545 | −176,954 |
| Financing cash flow | −15,879 | −11,812 | +9,661 | **+62,475** |
| Total costs & expenses | 537,933 | 569,366 | 636,949 | — |
| D&A | — | — | — | 70,439 (vs 55,373 prior TTM) |
| Net income | — | — | — | **90,798** (vs 65,944 prior TTM, +37.7%) |
| SBC expense | 24,023 | 22,011 | 19,467 | — |
| Advertising expense | 20,300 | 21,400 | 23,500 | — |
| LT debt issued | 0 | 0 | 15,673 | 68,368 |
| Comprehensive income | 31,872 | 62,254 | 105,934 | — |

**Read-through:** three straight years of accelerating capex (+57%, +59%, +62% y/y) have now fully consumed operating cash flow. **TTM free cash flow is negative (−$2.5B) for the first time in the modern Amazon era**, versus +$32.9B in FY2024. Meanwhile net income is compounding (+37.7% TTM) and SBC is falling (24.0B → 22.0B → 19.5B, a real quality improvement — dilution is decelerating).

---

## 4. Cash flow deep-dive — the capex and financing story

**Q1 2026 alone ($M):**
- Operating: **+26,032** (vs +17,015 in Q1 2025, **+53.0%**)
- Capex: **44,203** (vs 25,019, **+76.7%**)
- **Q1 FCF = −18,171** (vs −8,004 in Q1 2025)
- Acquisitions: **15,408** (`PaymentsToAcquireBusinessesNetOfCashAcquired`, vs −48 in Q1 2025) — a step-change in M&A; goodwill rose only $1.7B, so much of this likely sits in the equity-securities/other-asset lines rather than as consolidated goodwill.
- Marketable securities purchases 23,256 / sales & maturities 17,686 (treasury churn).
- **Long-term debt issued: 53,441** in a single quarter (vs 746 a year earlier). Short-term debt issued 6,018, repaid 6,109.

**Forward pipeline / commitments (all at 2026-03-31):**
- `CapitalExpendituresIncurredButNotYetPaid`: **$27.0B at 12/31/2025 vs $16.8B at 12/31/2024 (+61%)** → capex is accelerating, not peaking.
- `ContractualObligation` (total purchase/other commitments): **$569.3B**, of which **$57.1B due within 12 months**.
- Operating-lease payments due: **$110.1B** undiscounted ($13.9B next 12 months); new operating ROU assets added in TTM: **$21.8B vs $16.0B prior (+36.6%)** → leased data-centre/warehouse footprint expanding fast.
- Finance-lease payments due: $16.5B undiscounted.
- Contract liabilities (deferred revenue): $25.0B total ($20.9B current, $4.4B non-current); $9.4B of Q1 revenue was released from prior deferred balances.

**Capex intensity:** Q1 2026 capex was **24.4% of quarterly revenue** (44,203/181,519). This is the number that determines whether AMZN is a $32B-FCF machine again by 2027 or a leveraged infrastructure builder for longer.

---

## 5. Balance sheet and liquidity (2026-03-31 vs 2025-12-31)

| $M | 2026-03-31 | 2025-12-31 | Δ |
|---|---|---|---|
| Cash & equivalents | 101,816 | 86,810 | +17.3% |
| AFS debt securities (fair value, total portfolio) | 128,509 | 106,493 | +20.7% |
| Accounts receivable, net | 75,532 | 67,729 | +11.5% |
| Inventory, net | 36,534 | 38,325 | −4.7% |
| Total current assets | 255,155 | 229,083 | +11.4% |
| Total current liabilities | 216,756 | 218,005 | −0.6% |
| **Working capital** | **+38,399** | **+11,078** | — |
| Current ratio | 1.18x | 1.05x | improving |
| Long-term debt (total) | **122,632** | **68,836** | **+78.2%** |
| — of which non-current | 119,074 | 65,648 | +81.4% |
| Finance lease liabilities | 13,325 | 12,286 | +8.5% |
| Operating lease liabilities | 91,617 | 89,252 | +2.7% |
| Other non-current liabilities | 48,072 | 35,985 | +33.6% |
| Other non-current assets | 151,827 | 122,607 | +23.9% |
| Goodwill | 23,449 | 23,273 | +0.8% |
| **Total assets** | **916,630** | **818,042** | **+12.1%** |
| **Shareholders' equity (derived: assets − liabilities)** | **≈438,356** | **≈407,877** | **+7.5%** |

**Derived capital-structure and return metrics (my calculation):**
- **ROE (TTM NI / period-end equity):** 90,798 / 438,356 ≈ **20.7%**
- **ROA:** 90,798 / 916,630 ≈ **9.9%**
- **Debt/equity (funded debt only):** 125,464 / 438,356 ≈ **0.29x**
- **Debt/equity including all leases:** (125,464 + 13,325 + 91,617) / 438,356 ≈ **0.53x**
- **Net debt ex-leases:** ~125.5B debt − ~$132B cash + near-term securities ≈ **net cash near zero** (a quarter ago this was a ~$60B net cash position)
- **Tangible book:** ~$415B
- **Interest coverage (Q1):** operating income 23,852 / interest 800 ≈ **29.8x** — comfortable.
- **Equity reconciliation validates the estimate:** Dec-25 equity 407.9B + Q1 net income 30.3B + SBC 4.0B − AOCI change 3.4B ≈ 438.9B vs derived 438.4B. Tight — the ~$438B equity figure is reliable.
- **AOCI:** +24,868M at 3/31/26 (from effectively nil at 12/31/24) — a large unrealized-gain cushion in the investment portfolio that swings reported equity and comprehensive income.

**Liquidity judgement:** ~$136B of current cash+securities against $216.8B of current liabilities and $57.1B of commitments due within 12 months — ample. Amazon has also just demonstrated deep, cheap access to the IG bond market ($53.4B in one quarter). Balance-sheet risk is not solvency; it is **multiple compression from a rising interest burden and a shifting "equity story" from FCF compounder to capital-intensive builder**.

---

## 6. Quality-of-earnings and tax flags

1. **Non-cash equity mark-up is the biggest single P&L item** ($12.3B pre-tax, ~26% of pre-tax income). Non-repeatable in direction; can reverse.
2. **Cash taxes are dramatically below book taxes.** Q1 2026: tax provision $9,560M of which **$12,798M was deferred** and only **$1,323M cash taxes paid**. TTM: deferred tax expense **$23,761M** vs cash taxes paid **$8,741M**. This is why OCF ($148.5B) so far exceeds net income ($90.8B). It is a *real* cash-flow benefit (accelerated depreciation on $150B of capex) — but it is a **deferral, not a permanent saving**, and it phases down as capex growth decelerates.
3. **Accrued liabilities are draining cash:** TTM change −$9,003M; Q1 2026 −$8,045M. Combined with a $14,330M TTM build in receivables/other operating assets, working capital was a meaningful TTM headwind (partly offset by +$11,537M from payables).
4. **SBC quality is improving** (19.5B FY25 vs 24.0B FY23) with $14.4B of unrecognised expense remaining.
5. **Inventory reserves fell** $3.3B → $2.8B and inventory declined QoQ — no inventory-quality issue in this quarter; AR allowance ticked up $2.4B → $2.6B on 11.5% AR growth (normal).
6. **Payables stretch:** AP days ≈130 (AP 124,749 / COGS 87,463 × 91) vs AR days ≈38 — Amazon still funds itself on supplier float, unchanged in character.

---

## 7. Insider transactions
**DATA_UNAVAILABLE.** The configured news/fundamental vendor has **no authorized point-in-time insider-transactions archive for AMZN as of 2026-07-23**. I will not infer or fabricate insider buying/selling. Treat the absence of insider data as a genuine information gap in this report, not as a neutral signal.

---

## 8. Actionable conclusions for traders

**Bull case (operationally supported by the data):**
- Revenue +16.6% and operating income +29.6% y/y simultaneously — **margin expansion on top of re-acceleration** is the rarest combination in mega-cap tech. Gross margin +120bps, operating margin +130bps.
- Overheads are being controlled (marketing +5.6%, G&A −1.6%) — the 2022–23 cost reset is durable.
- SBC declining, share count flat-to-up minimally, no buyback needed to support EPS.
- Cash-generation engine is intact at the operating line: TTM OCF $148.5B (+28% vs FY2024's $115.9B), Q1 OCF +53% y/y.
- The $48B non-marketable equity portfolio is an **unrecognised asset** that has just proven it can be marked up by eight figures in a single quarter; in an AI-upside tape this is optionality, not a liability.
- Balance sheet can carry the build: 0.29x funded-debt/equity, 29.8x interest coverage, ~$136B liquid.

**Bear case (also supported by the data):**
- **FCF has gone negative on a TTM basis (−$2.5B)** and Q1 FCF was −$18.2B. Capex at 24.4% of quarterly revenue with accrued-but-unpaid capex up 61% y/y says the trough is *ahead*, not behind.
- **$53.4B of new long-term debt in one quarter**, doubling LT debt to $122.6B in 90 days. Leverage is still modest, but the *trajectory* is what re-rates a compounder into a cyclical.
- **Headline EPS is inflated ~30%** by a mark-to-model gain. If a screening model or a sell-side whisper number anchors on $2.78, the "beat" quality is easy to challenge.
- Depreciation +41.7% y/y is the leading indicator that the enormous capex base will compress operating margin in 2026–27 unless AWS/AI revenue absorbs it.
- $569B of contractual obligations and $110B of lease payments lock in future cash outflows regardless of demand.
- Effective tax rate rising (21.0% → 24.0%) and deferred-tax benefits are finite.

**Specific things to do with this:**
1. **Do not anchor to $2.78.** Model Q1 2026 "core" EPS at ~$1.90–1.95 (my estimate) and require the Q2 print to show *operating* income growth above ~20% y/y to maintain the growth thesis.
2. **Watch three lines in the imminent Q2 2026 filing** (period ending 2026-06-30 — not yet in the dataset): (a) capex guidance vs the $151B TTM run-rate; (b) whether long-term debt rises again from $122.6B; (c) whether the non-marketable equity stake stays near $48.1B or reverses.
3. **FCF inflection is the trade.** The stock's narrative hinges on OCF − capex turning positive. FY2025 was +$7.7B; TTM is −$2.5B. A single quarter of capex discipline (or faster AWS monetisation) would be the highest-conviction positive catalyst available.
4. **Position sizing around the print:** earnings are due imminently by calendar convention, and the setup is asymmetric in *narrative* terms — the operating beat is priced by bulls, while the capex/debt/FCF drag and the one-off gain are the under-appreciated items.
5. **Treat insider signal as unknown.** With no insider archive available, do not read management conviction from this report.

---

## 9. Key points summary

| Category | Metric | Value | Period / As-of | Signal |
|---|---|---|---|---|
| Scale | Revenue | $181,519M | Q1 2026 | +16.6% y/y |
| Scale | Total assets | $916,630M | 2026-03-31 | +12.1% QoQ |
| Profitability | Gross margin | 51.8% | Q1 2026 | +120 bps y/y |
| Profitability | Operating income | $23,852M (13.1% mgn) | Q1 2026 | +29.6% y/y |
| Profitability | Net income | $30,255M | Q1 2026 | +76.7% y/y (flattered) |
| Profitability | Diluted EPS | $2.78 | Q1 2026 | ~$1.92 ex-mark-up (est.) |
| Profitability | ROE (TTM NI / equity) | ≈20.7% | 2026-03-31 | Strong |
| Profitability | ROA | ≈9.9% | 2026-03-31 | Strong |
| **Quality of earnings** | Non-marketable equity mark-up | **+$12,328M pre-tax** | Q1 2026 | **One-off, inflates EPS ~30%** |
| Quality of earnings | Non-marketable equity carrying value | $48,100M (from $16,200M) | 2026-03-31 | +197% QoQ; volatile |
| Quality of earnings | Deferred tax expense / cash tax paid | $12,798M / $1,323M | Q1 2026 | Cash-tax shield, temporary |
| Quality of earnings | SBC expense | $19,467M (FY25) | FY2025 | Declining; positive |
| Cash flow | Operating cash flow (TTM) | $148,531M | Apr-25→Mar-26 | +30% vs TTM prior |
| Cash flow | Capex (TTM) | $151,003M | Apr-25→Mar-26 | +62% y/y |
| **Cash flow** | **Free cash flow (TTM)** | **−$2,472M** | Apr-25→Mar-26 | **Negative; key risk** |
| Cash flow | Q1 2026 FCF | −$18,171M | Q1 2026 | Capex 24.4% of revenue |
| Cash flow | Capex incurred not yet paid | $27,000M (vs $16,800M) | 2025-12-31 | +61%; acceleration ahead |
| Balance sheet | Cash & equivalents | $101,816M | 2026-03-31 | +17.3% QoQ |
| Balance sheet | AFS debt securities (FV) | $128,509M | 2026-03-31 | Liquidity buffer |
| Balance sheet | Long-term debt | $122,632M | 2026-03-31 | **+78% QoQ** |
| Balance sheet | LT debt issued in quarter | $53,441M | Q1 2026 | vs $746M a year ago |
| Balance sheet | Finance + operating leases | $104,942M | 2026-03-31 | Structural obligation |
| Balance sheet | Shareholders' equity (derived) | ≈$438,356M | 2026-03-31 | +7.5% QoQ |
| Leverage | Funded debt / equity | ≈0.29x | 2026-03-31 | Manageable, rising |
| Leverage | Total debt incl. leases / equity | ≈0.53x | 2026-03-31 | Moderate |
| Leverage | Interest coverage | ≈29.8x | Q1 2026 | Comfortable |
| Liquidity | Current ratio | 1.18x (WC +$38.4B) | 2026-03-31 | Improved from 1.05x |
| Commitments | Total contractual obligations | $569,280M | 2026-03-31 | $57.1B due <12M |
| Commitments | Operating lease payments due | $110,135M | 2026-03-31 | $13.9B next 12M |
| Commitments | Contract liabilities (deferred rev.) | $25,000M | 2026-03-31 | $9.4B recognised in Q1 |
| Capital return | Dividends / buybacks | None evident | — | No treasury/dividend facts |
| Shares | Shares outstanding | 10,754M (10,757.1M @ 4/22/26) | 2026-03-31 | Diluted ~10,883M |
| Acquisitions | Cash paid for businesses | $15,408M | Q1 2026 | Step-change M&A |
| Insider | Insider transactions | **DATA UNAVAILABLE** | 2026-07-23 | No archive; not inferred |
| Catalyst | Next reportable period | Q2 2026 (Jun-30 qtr) **not yet filed** | — | Imminent by calendar convention |

**Bottom line on AMZN:** the operating business is performing at its best level in years — mid-teens revenue growth *with* 130bps of operating-margin expansion and genuine overhead leverage. But the reported bottom line is ~30% flattered by a non-cash equity mark-up, free cash flow has turned negative, and the company has just switched on $53B/quarter of debt financing to fund a capex programme that is still accelerating. Trade the operating strength, but discount the EPS headline and size for the FCF/leverage narrative risk into the imminent Q2 print.