# AMZN — Fundamental Deep Dive (point-in-time as of 2026-08-11)

**Instrument:** AMZN (Amazon.com, Inc.)
**Primary source:** Q2-2026 Form 10-Q, period ended 2026-06-30, accepted 2026-07-31 02:11 UTC (accn 0001018724-26-000026), plus Q1-2026 10-Q (accepted 2026-04-30). All facts below are filtered to information actually public by 2026-08-11.
**Caveats:** (1) The revenue line item is *derived* as `Total costs and expenses + Operating income` (Amazon's own statement arithmetic) because the revenue tag was not in the cached tag set — the derivation is validated against Q2-2025 (derived $167.7B vs. reported ~$167.7B). (2) No price/market-cap data is available in this tool set, so no valuation multiples are computed. (3) **Insider-transactions data is unavailable for AMZN** in this data package — I will not infer or fabricate insider activity.

---

## 1. Company profile (as reflected in the filings)

Amazon.com, Inc. is a global technology and retail conglomerate reporting **3 operating segments** (`NumberOfOperatingSegments = 3`, unchanged): **North America retail/marketplace**, **International retail/marketplace**, and **Amazon Web Services (AWS)** cloud. Revenue streams embedded in the cost/expense structure include: online and physical stores, third-party seller services, subscription services (Prime), **advertising**, and **AWS** (compute, storage, database, AI/ML). The company also carries a very large *investment* portfolio (marketable securities plus non-marketable equity stakes), which has become a first-order earnings driver — see §4 and §8.

Capital intensity has structurally changed: the company is now in a capex/AI-infrastructure and M&A build-out phase, funded partly with new debt rather than internally generated cash (§6–§7).

---

## 2. Headline results — Q2 2026 and 1H 2026 (US$M)

| Metric | Q2 2026 | Q2 2025 | y/y | 1H 2026 | 1H 2025 | y/y |
|---|---|---|---|---|---|---|
| Revenue (derived) | **200,606** | 167,702 | **+19.6%** | **382,125** | 323,369 | **+18.2%** |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 330,812 | 285,793 | +15.8% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** | **51,313** | 37,576 | **+36.6%** |
| Operating margin | **13.7%** | 11.4% | +2.3pt | **13.4%** | 11.6% | +1.8pt |
| Non-operating income | **53,396** | 1,686 | nm | **69,378** | 4,960 | nm |
| Pre-tax income | 80,857 | 20,857 | +288% | 120,691 | 42,536 | +184% |
| Tax expense | 18,199 | 2,678 | — | 27,759 | 7,231 | — |
| Effective tax rate | 22.5% | 12.8% | — | 23.0% | 17.0% | — |
| **Net income** | **62,647** | 18,164 | **+245%** | **92,902** | 35,291 | **+163%** |
| Diluted EPS | **$5.75** | $1.68 | +242% | **$8.53** | $3.27 | +161% |
| Basic EPS | $5.82 | $1.71 | — | $8.64 | $3.32 | — |

Q1-2026 implied (1H less Q2): revenue **$181,519M** (+16.6% y/y), operating income **$23,852M** (13.1% margin), net income $30,255M.

**Two clean, distinct stories are embedded here:**
1. **Operating momentum is accelerating** — revenue growth went 16.6% (Q1-26) → 19.6% (Q2-26), and operating income grew +36.6% in 1H despite a 15.8% expense increase. That is genuine operating leverage.
2. **Reported net income/EPS is dominated by non-cash investment mark-ups, not operations** — see below.

---

## 3. Quality of earnings — the single most important trading insight

`NonoperatingIncomeExpense` was **$53,396M in Q2-2026 (66% of pre-tax income)** and **$69,378M in 1H-2026**, versus $1,686M/$4,960M a year earlier. The driver is disclosed: `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount` of **$50,486M in Q2-2026** and **$62,814M in 1H-2026** (vs. $49M/$86M in the prior-year periods). Other fair-value items were modestly negative (`FairValueAdjustmentOfWarrants` −$1,449M in Q2).

**Operating-only EPS reconstruction (taxed at the 22.5% reported rate, on ~10.9B diluted shares):**

| | Q2 2026 | 1H 2026 |
|---|---|---|
| Operating income | 27,461 | 51,313 |
| Less tax @22.5–23% | (6,179) | (11,802) |
| After-tax operating income | ~21,282 | ~39,511 |
| **"Core" EPS (est.)** | **~$1.95** | **~$3.63** |
| Reported diluted EPS | $5.75 | $8.53 |
| **Non-operating contribution to EPS** | **~$3.80 (66%)** | **~$4.90 (57%)** |

**Actionable:** headline EPS (+242% y/y) is *not* an operating result. Do not extrapolate it. Amazon elected fair value treatment for a large non-marketable equity book, so **mark-ups and mark-downs both flow through the income statement**, making GAAP EPS structurally volatile and creating brutal comparability problems for consensus models built off GAAP. Trade the operating line (revenue growth, operating income, margin); treat non-operating gains as a separate, non-cash, reversible NAV item.

**Magnitude check on reversal risk:** the carrying value of `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` is **$122,300M at 2026-06-30** (from $16,200M at 2025-12-31). A 20% markdown of that book would be ≈ **−$24.5B pre-tax ≈ −$2.2/share** — roughly one quarter of a "core" year of earnings, in a single print.

---

## 4. Cost structure and margin drivers (Q2 2026 vs Q2 2025, US$M)

| Line | Q2 2026 | % rev | Q2 2025 | % rev | y/y |
|---|---|---|---|---|---|
| Cost of goods & services | 95,778 | 47.7% | 80,809 | 48.2% | +18.5% |
| Implied gross profit | **104,828** | **52.3%** | 86,893 | 51.8% | +20.6% |
| Marketing | 11,698 | 5.8% | 11,416 | 6.8% | +2.5% |
| G&A | 2,788 | 1.4% | 2,965 | 1.8% | −6.0% |
| Share-based comp (all functions) | 6,038 | 3.0% | 6,534 | 3.9% | −7.6% |
| Depreciation & amortization | 19,988 | 10.0% | 15,227 | 9.1% | +31.3% |
| Operating lease cost | 4,118 | 2.1% | 3,426 | 2.0% | +20.2% |
| Interest expense | 1,314 | 0.7% | 516 | 0.3% | **+155%** |
| Interest income | 1,295 | 0.6% | 1,085 | 0.6% | +19.4% |

Key reads:
- **Margin expansion is mix- and discipline-driven** (gross margin +0.5pt, marketing down 1.0pt as % of sales, G&A and SBC down) — not from cost deferral. SBC *declining* in absolute terms is unusual and a positive quality signal.
- **D&A is ramping hard** (+31% y/y; 1H-26 $38,933M vs $29,489M; TTM $75,200M) as prior capex enters service. With TTM capex of $173,028M, D&A growth is a *locked-in* future headwind to margins.
- **Net interest has flipped negative in Q2-2026** ($1,295M income vs $1,314M expense = −$19M). For years interest income was a tailwind; the debt build (§7) has neutralized it. Annualized interest expense run-rate is now ≈ $5.3B vs ≈ $2.1B in Q2-2025.

---

## 5. Cash flow — the capex supercycle and negative free cash flow

| US$M | Q2 2026 | Q2 2025 | 1H 2026 | 1H 2025 | TTM (Jul-25→Jun-26) | Prior TTM |
|---|---|---|---|---|---|---|
| Operating cash flow | **45,387** | 32,515 | **71,419** | 49,530 | **161,403** | 121,137 (+33%) |
| Capex (productive assets) | **54,208** | 32,183 | **98,411** | 57,202 | **173,028** | 107,656 (+61%) |
| **Free cash flow** | **−8,821** | +332 | **−26,992** | −7,672 | **−11,625** | +13,481 |
| FCF after finance-lease principal | — | — | — | — | ~−13,224 | — |
| Capex / revenue | **27.0%** | 19.2% | 25.8% | 17.7% | ~23% (est.) | ~15% |
| Acquisitions, net of cash | 24,359 | 1,700 | 39,767 | 1,652 | **41,956** | 4,809 |
| Investing cash flow | −79,245 | −39,424 | −143,457 | −69,227 | **−216,775** | −123,569 |
| Financing cash flow | +10,146 | −2,539 | **+62,913** | −2,586 | **+75,160** | −8,652 |
| D&A | 19,988 | 15,227 | 38,933 | 29,489 | 75,200 | 58,562 |
| Cash taxes paid | 2,655 | 4,761 | 3,978 | 5,638 | 6,635 | 11,788 |

**Actionable insights:**
- **AMZN is now FCF-negative on a trailing basis (−$11.6B TTM) and −$27.0B in 1H-2026.** Operating cash flow growth (+33% TTM) is being more than consumed by capex growth (+61% TTM). Any model or narrative anchored on "AMZN FCF machine" is stale — the correct frame for the next several quarters is *capex cycle intensity and returns on AI infrastructure*, not FCF yield.
- **Cash taxes are running far below book tax.** TTM tax expense (incl. deferred) is huge but cash taxes were only $6.6B TTM vs. $11.8B in the prior TTM — because the equity mark-ups create **deferred** tax ($41,441M deferred tax expense TTM). Optically high tax rates on marked-up gains are largely non-cash.
- **M&A step-change:** $39.8B of business acquisitions in 1H-2026 ($24.4B in Q2 alone) vs. $1.7B a year ago. This is a major, under-appreciated capital-allocation shift — diligence item: what was bought, at what multiple, and how much goodwill/intangibles hit the balance sheet.
- Working capital was a *use* of cash: AR/other operating assets $21,409M and accrued liabilities −$6,069M TTM, partially offset by payables growth.

---

## 6. Balance sheet — $1.1 trillion in assets, debt-funded growth

**Balance sheet (US$M):**

| Item | 2026-06-30 | 2025-12-31 | Δ |
|---|---|---|---|
| **Total assets** | **1,095,689** | 818,042 | **+34.0%** |
| Current assets | 249,264 | 229,083 | +8.8% |
| Cash & equivalents | 78,213 | 86,810 | −9.9% |
| Marketable (AFS) securities | 97,900 | 45,800 | **+113.8%** |
| Inventories | 38,184 | 38,325 | −0.4% |
| Accounts receivable, net | 88,092 | 67,729 | **+30.1%** |
| Non-marketable equity securities (no RDFV) | **122,300** | 16,200 | **+$106.1B** |
| **Current liabilities** | **241,274** | 218,005 | +10.7% |
| Accounts payable | 147,440 | 121,909 | +21.0% |
| Accrued liabilities | 73,406 | 75,520 | −2.8% |
| Long-term debt (incl. current $3,330) | **132,995** | 68,836 | **+93.2%** |
| Finance lease liabilities | 13,451 | 12,286 | +9.5% |
| Operating lease liabilities | 96,320 | 89,252 | +7.9% |
| AOCI | 66,287 | 28,230 | **+$38.1B** |
| APIC | 149,619 | 140,024 | +9,621 |
| Shares outstanding | **10,783.0M** | 10,731.0M | +52.0M (0.5% dilution) |
| Shares outstanding (2026-07-22) | 10,786.3M | — | — |

Derived liquidity/leverage metrics:
- **Liquid assets:** cash $78,213M + AFS $97,900M ≈ **$176.1B** (plus restricted/other cash of $80,927M per the cash-flow reconciliation).
- **Gross debt:** LT debt $132,995M + short-term borrowings within current liabilities ≈ **$136B** (from ~$69B at YE-2025 — roughly **doubled in six months**).
- **Total debt + lease obligations:** $132,995 + $13,451 + $96,320 ≈ **$242.8B**.
- **Current ratio:** 249,264 / 241,274 = **1.03** (from 1.05) — thinner, though absolute liquidity remains exceptional.
- **Estimated stockholders' equity ≈ $520–530B** (not a directly reported tag in this data set; triangulated from assets less current liabilities, debt and lease obligations, plus earnings/AOCI roll-forward). Book value ≈ **$48–49/share**. Gross debt/equity ≈ 26%; lease-adjusted ≈ 46%.
- **Contractual obligations total $650,034M** at 6/30/26, with $42,752M due in the remainder of FY2026 and $78,084M within the next twelve months — a meaningful fixed-charge layer (mostly leases, content, and cloud capacity commitments).

**Signal:** payables +21% and AR +30% (faster than revenue) with flat inventory ($38.2B) — working-capital efficiency plus favorable supplier terms (negative working capital still working), but also a sign that a chunk of "growth" funding comes from vendor float. Allowance for doubtful accounts rose to $2.8B (from $2.4B).

**Unresolved diligence item:** AOCI rose **+$38.1B in six months** (to $66,287M) while gross unrealized gains on AFS securities were only **$7M** and FX translation was **−$1,563M**. The tag set does not cleanly explain the swing — flag for the 10-Q MD&A/equity-statement review; it does not appear to have run through the income statement.

---

## 7. Capital allocation

1. **Organic capex is the dominant use of capital:** $98.4B in 1H-2026 (25.8% of revenue), TTM $173.0B (+61% y/y) — consistent with an aggressive AI/data-center, logistics and custom-silicon build-out.
2. **Debt is funding the gap:** TTM long-term debt issued **$81,925M** ($66,998M in 1H-2026) plus $20,798M of short-term borrowings, against repayments of $5,022M LT / $20,634M ST. Long-term debt nearly doubled sequentially — a clear regime change from the 2023–2025 deleveraging.
3. **M&A re-activated:** $41,956M TTM, $39,767M in 1H-2026.
4. **No buyback, no dividend** (no treasury-purchase or dividend tags present; cash-financing outflow is debt-driven). Dilution from SBC is modest: +52M shares in six months (+0.5%), and unrecognized SBC is **$24.8B**.

---

## 8. Portfolio / NAV optionality

- **Non-marketable equity securities:** **$122,300M** at 6/30/26 vs **$16,200M** at 12/31/25. The $50.5B Q2 and $62.8B 1H upward adjustments point to one or more large private holdings that were massively revalued in 1H-2026 — the profile is consistent with a large private **AI/technology stake** (Amazon is a well-known strategic investor in AI model developers), though the tagging does not name the counterparty.
- **Marketable securities doubled** to $97,900M (all within one year: $96,471M), i.e., Amazon has parked ~$96B in short-duration instruments — dry powder + rate-sensitive income.
- **Trading implication:** this book is a **hidden NAV layer worth ~$11+/share (marketable) plus ~$11+/share (non-marketable, at carrying value)** — combined ≈ 15–20% of book equity. It is also the source of earnings noise. Catalysts that crystallize value (IPOs, secondary marks, strategic transactions) are asymmetric upside; further mark-ups keep inflating GAAP EPS; mark-downs are a live, quantifiable downside to reported numbers.

---

## 9. Insider transactions

**DATA_UNAVAILABLE.** The B-project data package contains **no authorized, point-in-time insider-transactions archive for AMZN as of 2026-08-11**. I have not estimated or inferred any insider buying/selling. This is a genuine information gap in this report: **do not read the absence as neutral or bearish/bullish** — it is simply unavailable from this source and should be sourced separately (Forms 3/4/5) before drawing conclusions on management conviction.

---

## 10. Actionable trading framework for AMZN

**Bull case — supported by the filings**
- Revenue growth **accelerating** (16.6% → 19.6% y/y) at a scale of ~$200B/quarter.
- Operating income **+43% y/y** with margin at a record 13.7%; gross margin +0.5pt, marketing/G&A/SBC all improving as % of revenue.
- OCF +33% TTM to $161.4B — the core franchise is throwing off more cash than ever.
- ~$176B of liquid assets; interest coverage still comfortable; lease-adjusted leverage ~46% of equity.
- $122B private-equity book + $98B marketable securities = material embedded NAV optionality.

**Bear case / what breaks the trade**
- **Negative FCF** (−$27.0B 1H-26; −$11.6B TTM) and capex at 27% of revenue with no sign of a cap in the filings. If AI-infrastructure monetization lags, the market reprices the capex, not the earnings.
- **Debt doubled to ~$136B in six months**; interest expense +155% y/y; net interest flipped negative. Continued issuance implies rising fixed charges against a still-unproven capex return stream.
- **Earnings quality:** ~60–66% of recent pre-tax income is non-cash mark-ups on private securities; the same mechanism can reverse and the book is now $122B large.
- **D&A inflection** (+31% y/y, TTM $75.2B vs capex $173.0B) is a mechanical future margin headwind.
- Current ratio compressed to 1.03; $78B of contractual obligations due within 12 months.
- $39.8B of 1H-2026 M&A carries integration/impairment risk and is not yet explained in the tag data.

**Concrete positioning guidance**
1. **Judge AMZN on operating income, revenue growth and segment mix — not on EPS.** Expect GAAP EPS to be dominated by mark-to-market swings for the next several quarters; size any earnings-based options trade off core EPS (~$1.95 in Q2-26) rather than $5.75.
2. **Watch the Q3-2026 10-Q (expected late October 2026) for four numbers:** capex, debt issued, the revaluation of the $122.3B non-marketable book, and any change in the $650B contractual-obligation stack. A second consecutive quarter of >$50B capex with negative FCF is the key risk trigger.
3. **Stay long the operating-leveraging leg, hedge the mark-to-market leg.** A paired view (long operating momentum / short GAAP-EPS-expectations) is the cleanest expression.
4. **Credit metrics now matter for equity:** track gross debt (~$136B), lease-adjusted obligations (~$243B), interest expense run-rate (~$5.3B annualized) and cash taxes ($6.6B TTM) — a ratings action or wider CDS would compress the multiple.
5. **Treat valuation as out of scope here** — this tool set provides no price data; a market-data-equipped agent should combine these fundamentals with price/multiple work before any final call.

---

## 11. Key figures summary table

| Category | Metric | Value | Reference point | Read-through |
|---|---|---|---|---|
| Latest filing | Form 10-Q, period | Q2 FY2026, ended 2026-06-30 | accepted 2026-07-31 | Fresh, post-earnings data |
| Segments | Operating segments | 3 (NA, Int'l, AWS) | unchanged | — |
| Revenue (derived) | Q2 2026 | $200,606M | $167,702M Q2-25 | **+19.6% y/y, accelerating** |
| Revenue (derived) | 1H 2026 | $382,125M | $323,369M | +18.2% y/y |
| Operating income | Q2 2026 | $27,461M | $19,171M | **+43.2% y/y** |
| Operating margin | Q2 2026 | 13.7% | 11.4% | +2.3pt — record zone |
| Non-operating income | Q2 2026 | $53,396M | $1,686M | **66% of pre-tax income, non-cash marks** |
| Private equity mark-up | 1H 2026 | $62,814M | $86M | The EPS story, not operations |
| Net income | Q2 2026 | $62,647M | $18,164M | +245% (mostly non-operating) |
| Diluted EPS | Q2 2026 | $5.75 | $1.68 | Core (ex-marks, est.) ~**$1.95** |
| Diluted EPS | 1H 2026 | $8.53 | $3.27 | Core (ex-marks, est.) ~**$3.63** |
| Operating cash flow | TTM | $161,403M | $121,137M | +33% y/y |
| Capex | TTM | $173,028M | $107,656M | **+61%; 25.8% of 1H revenue** |
| Free cash flow | TTM | **−$11,625M** | +$13,481M | **Now negative** |
| Free cash flow | 1H 2026 | **−$26,992M** | −$7,672M | Deteriorating |
| Acquisitions | 1H 2026 | $39,767M | $1,652M | M&A regime change |
| Total assets | 2026-06-30 | $1,095,689M | $818,042M | +34% in 6 months |
| Non-marketable equity | 2026-06-30 | $122,300M | $16,200M | +$106B — NAV + EPS volatility |
| Cash + AFS securities | 2026-06-30 | $176,113M | $132,610M | Liquidity strong |
| Long-term debt (incl. current) | 2026-06-30 | $132,995M | $68,836M | **+93% — debt-funded capex** |
| Leases (op + fin) | 2026-06-30 | $109,771M | $101,538M | Rising fixed charges |
| Interest expense | Q2 2026 | $1,314M | $516M | +155%; **net interest now negative** |
| Contractual obligations | 2026-06-30 | $650,034M | — | $78.1B due <12 months |
| Current ratio | 2026-06-30 | 1.03x | 1.05x | Thinner, still adequate |
| Est. book value/share | 2026-06-30 | ~$48–49 | — | Est. from tag triangulation |
| Shares outstanding | 2026-07-22 | 10,786.3M | 10,731.0M (YE25) | +0.5% dilution; no buyback |
| Insider transactions | — | **UNAVAILABLE** | — | Do not infer; source separately |

**Bottom line on AMZN:** an outstanding *operating* quarter — accelerating revenue, a 13.7% operating margin, +43% operating income — wrapped in a *low-quality* GAAP print dominated by a $50.5B non-cash private-equity mark-up, and financed by a capex supercycle that has turned free cash flow negative and roughly doubled debt in six months. Trade the operating leverage; discount the EPS headline; and watch capex, debt issuance, and the $122B mark-to-model book as the three swing factors into the Q3-2026 print.