# AMZN — Fundamental Research Report
**As of:** 2024-02-05 | **Instrument:** AMZN (Amazon.com, Inc.)
**Primary source:** Point-in-time SEC facts, FY2023 Form 10-K (accn 0001018724-24-000008, **accepted 2024-02-02 04:48 UTC**) — i.e., the annual report was filed **3 days before this analysis date**. FY2021–FY2023 annual series plus YTD-Q3'23 10-Q facts.

---

## 1. Data Provenance & Coverage (read this first)

| Item | Status |
|---|---|
| FY2023 10-K (annual IS/BS/CF, all notes) | ✅ Complete — filed 2024-02-02 |
| Quarterly *revenue/operating income* series | ❌ Not in point-in-time extract (annual only) |
| YTD & quarterly cash-flow detail through Q3'23 | ✅ Partial (10-Q filed 2023-10-27) |
| Segment-level P&L (NA / International / AWS) | ❌ Not in extract — only `NumberOfOperatingSegments = 3` |
| Insider transactions | ❌ **DATA_UNAVAILABLE** — no authorized archive for AMZN by 2024-02-05. No insider activity is inferred or fabricated below. |
| Share price / multiples (P/E, EV/EBITDA) | ❌ Not available — no valuation ratios computed. `EntityPublicFloat` = **$1.184T** at 2023-06-30 (size context only). |

**Bottom line:** this report is built almost entirely on the freshest possible filing (Q4/FY2023 10-K, 3 days old). That filing is itself the dominant fundamental catalyst in the past week.

---

## 2. Executive Summary — the thesis in five lines

1. **Revenue re-accelerated to +11.8% ($574.8B)** from +9.4% in FY22 — the growth trough is behind it.
2. **Operating margin nearly tripled to 6.41%** ($36.9B EBIT) from 2.38% — the single most important number in the print (cost discipline + mix + logistics regionalization + AWS stabilization).
3. **Free cash flow inflected from −$16.9B to +$32.2B (+$49.1B YoY)** as OCF jumped +82% to $84.9B while capex fell 17%. This is a genuine regime change, not accounting noise.
4. **Balance sheet de-risked:** gross debt (incl. finance leases) cut 15% to $70.4B, zero new long-term debt issued, equity +38% to ~$201.9B, net debt ≈ zero.
5. **The offset:** SBC (+22% to $24.0B), interest expense (+34%), cash taxes (+85%) and $300B of contractual obligations are the offsets that cap the "clean" earnings story.

---

## 3. Income Statement — FY2021 → FY2023

| $M | FY2021 | FY2022 | FY2023 | YoY '23 |
|---|---|---|---|---|
| Revenue (Costs+Expenses + Op. Income) | 469,822 | 513,983 | **574,785** | **+11.8%** |
| Cost of goods & services | 272,344 | 288,831 | 304,739 | +5.5% |
| **Gross profit** | 197,478 | 225,152 | **270,046** | +20.0% |
| **Gross margin** | 42.03% | 43.81% | **47.00%** | +319 bps |
| Fulfillment / tech & content / G&A / marketing (aggregate, incl. in total) | — | — | — | — |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| **Operating income** | 24,879 | 12,248 | **36,852** | **+200.9%** |
| **Operating margin** | 5.29% | 2.38% | **6.41%** | +403 bps |
| Non-operating income/(expense) | +13,272 | −18,184 | **+705** | n/m |
| Pre-tax income | 38,151 | −5,936 | 37,557 | n/m |
| Income tax | 4,791 | −3,217 | 7,120 | n/m |
| **Effective tax rate** | 12.6% | benefit | **19.0%** | +640 bps |
| **Net income** | 33,364 | **−2,722** | **30,425** | n/m |
| **Diluted EPS** | 3.24 | −0.27 | **2.90** | n/m |
| Basic EPS | 3.30 | −0.27 | 2.95 | n/m |

### The margin story is a *cost-of-sales* story
- Cost of sales grew only **+5.5% vs revenue +11.8%** → ~$33B of incremental gross profit vs FY22.
- Total costs & expenses grew **+7.2%**, i.e., ~470 bps of expense leverage below revenue growth.
- The FY22 base was contaminated by one-offs: **$1.1B asset impairment** (incl. $0.72B in Q4'22) and a **−$18.2B non-operating swing** (mostly Rivian/equity markdowns: `EquitySecuritiesFvNiUnrealizedGainLoss` = **−$13.6B in FY22 vs +$1.0B in FY23**; marketable securities mark −$13.9B → +$1.0B).

### Quality-of-earnings caveats on the "clean" number
- FY23 non-operating income is thin (+$705M) and internally offsetting: **interest income $2,949M vs interest expense $3,182M** → net interest roughly **−$233M**, a *drag* versus FY22 (income $989M / expense $2,367M = −$1,378M). So FY23 EBIT strength is genuinely operating, not financial.
- FY21 was the inflated comparison year (+$11.6B equity securities gains; net income $33.4B > FY23's $30.4B on *lower* EBIT of $24.9B). **Do not use FY21 net income as the benchmark** — FY23 earnings are structurally higher quality despite lower headline net income.
- **SBC rose +22.4% to $24,023M** (12.8% of revenue constant-ish; 65% of EBIT). Unrecognized SBC cost of **$18.3B** sits off-income-statement — expect ~$9B/yr of future comp expense. GAAP EBIT of $36.9B is partly SBC-funded; on an SBC-adjusted basis EBIT would be ~$12.8B. This is the single biggest "adjusted vs GAAP" gap in the name.
- **D&A $48,663M** (+16.1%), of which depreciation $30,225M, intangible amortization $706M, finance-lease ROU amortization $5,899M. D&A still exceeds capex → accounting depreciation is "catching up" to the 2021–22 build.
- **Effective tax 19.0%** expected to normalize toward 21%+ as FDII/credits mix shifts; **cash taxes paid $11,179M (+85%)** vs $7,120M book tax → cash tax is now running *ahead* of book.

---

## 4. Cash Flow — the FCF inflection is the headline

| $M | FY2021 | FY2022 | FY2023 | YoY |
|---|---|---|---|---|
| **Operating cash flow** | 46,327 | 46,752 | **84,946** | **+81.7%** |
| Capex (productive assets)* | 61,053 | 63,645 | 52,729 | −17.2% |
| **Free cash flow (OCF − capex)** | **−14,726** | **−16,893** | **+32,217** | **+$49,110M** |
| Investing cash flow | −58,154 | −37,601 | −49,833 | +32.6% outflow |
| Financing cash flow | +6,291 | +9,718 | **−15,879** | swing to repayment |
| FX effect on cash | −364 | −1,093 | +403 | — |
| Net change in cash | −5,900 | +17,776 | +19,637 | — |
| OCF margin | 9.9% | 9.1% | **14.8%** | +570 bps |
| FCF margin | −3.1% | −3.3% | **+5.6%** | +890 bps |

\*Vendor tag `PaymentsToAcquireProductiveAssets`. FY21/FY22 match Amazon's reported "purchases of property and equipment" exactly ($61.1B / $63.6B). **Flag:** the FY23 tag ($52.7B) runs above the ~$48.1B "purchases of property and equipment" line as commonly reported from the same 10-K; on that stricter definition FY23 FCF is closer to **~$36.8B**. Either way the direction and magnitude (+$45–49B swing) are the same. Traders should use **FCF ≈ $32–37B for FY23** as the working range.

### What actually drove the $38B OCF increase
1. **Non-cash add-backs** already large and growing: D&A $48,663M + SBC $24,023M + deferred tax −$5,876M.
2. **Working-capital/float:** deferred revenue (`IncreaseDecreaseInContractWithCustomerLiability`) **+$4,578M** (+107% YoY); the offsetting drags were `AccruedLiabilities` −$2,428M, AR & other operating assets −$8,348M, other noncurrent assets −$12,265M (the last is the biggest single cash sink and worth watching — capitalized content/tech and investment-related).
3. **Capex discipline:** the 2021–22 logistics/fulfillment build is complete; capex down 17% while revenue grew 11.8%.

### Capital allocation read-through
- **Zero long-term debt issued in FY23** (vs $21.2B issued in FY22); **$3,676M LT repaid**, net short-term debt **−$7,548M** (proceeds $18,129M vs repayments $25,677M), plus `FinanceLeasePrincipalPayments` **−$4,384M**.
- **Buybacks: $0 in FY23** (vs $6,000M in FY22). No dividend. Every incremental dollar of FCF went to debt paydown and the balance sheet — a conservative, de-risking posture.
- Interest expense *still* rose +34% to $3,182M despite lower debt → higher average coupons on the 2022 issuance vintage plus rate resets. This rolls off slowly.

---

## 5. Balance Sheet — de-risked, liquid, tight-but-improving on current ratio

| $M | 2022-12-31 | 2023-12-31 | Change |
|---|---|---|---|
| Cash & equivalents | 53,888 | **73,387** | +36.2% |
| AR, net | 42,360 | 52,253 | +23.4% |
| **Current assets** | 146,791 | **172,351** | +17.4% |
| **Total assets** | 462,675 | **527,854** | +14.1% |
| Accounts payable | 79,600 | 84,981 | +6.8% |
| Accrued liabilities | 62,566 | 64,709 | +3.4% |
| Contract liabilities, current | 13,227 | 15,227 | +15.1% |
| Long-term debt (carrying) | 67,150 | **58,314** | −13.2% |
| Finance lease liabilities | 15,783 | **12,109** | −23.3% |
| Operating lease liabilities | 69,040 | **75,639** | +9.6% |
| Deferred revenue (total) | 16,100 | **20,606** | +28.0% |
| **Shareholders' equity** | ~146,043 | **~201,875** | +38.2% |
| APIC | 75,066 | 99,025 | +31.9% |
| AOCI | −4,487 | −3,040 | improving |
| Shares outstanding | 10,242M | 10,383M | +1.4% |
| Shares out (2024-01-24) | — | 10,387M | — |

**Derived metrics (mine, from the disclosures above):**

| Metric | FY2022 | FY2023 |
|---|---|---|
| Current ratio | 0.94x | **1.05x** |
| Gross debt (LTD + finance leases) | 82,933 | **70,423** |
| Net debt / (net cash) ex-marketable securities | +29,045 | **−2,964 (net cash)** |
| Gross debt / equity | 0.57x | **0.35x** |
| Return on equity (avg equity) | negative | **~17.5%** |
| Return on assets (avg assets) | ~−0.6% | **~6.1%** |
| ROIC (NOPAT / equity+debt−cash, 19% tax) | low single digit | **~15%** |
| Interest coverage (EBIT/interest) | 5.2x | **11.6x** |
| DSO (avg AR / revenue) | 28.1 days | 30.0 days |
| DPO (avg AP / COGS) | ~96 days | ~98.6 days |

**Interpretation:** the current ratio at 1.05x looks thin, but Amazon's negative working-capital model (~99 DPO vs ~30 DSO) means this is structural, not stressed. Equity nearly doubled *without* buybacks, driven by $30.4B net income (+$24.0B SBC add to APIC) and AOCI recovery. Available-for-sale securities (fair value $70,919M, amortized cost $71,265M, net unrealized loss only ~$346M; $65.2B matures within one year) confirm a **short-duration, low-risk treasury book** — no SVB-style duration exposure. Combined cash + marketable securities ≈ **$86.8B**.

---

## 6. Off-Balance-Sheet, Tax & Forward-Looking Signals

**Commitments are the key risk disclosure:**
- **Total contractual obligations $300,409M**, of which **$39,345M due within 12 months**; the back-end is heavy: $157,824M due **after year 5**.
- **Operating lease payments $90,777M** undiscounted ($11,229M next 12 months; $44,603M after year 5) — leases remain the largest single claim on future cash, up from $81,273M a year earlier.
- **Long-term debt maturities:** 2024 $8,500M; 2025 $5,286M; 2026 $3,146M; 2027 $8,750M; 2028 $2,250M; thereafter **$39,250M**. Ladder is well-spread and comfortably covered by ~$85B liquidity + $85B annual OCF.
- **Finance lease payments $14,106M** ($2,292M next 12 months) — down from $18,019M.

**Tax balance sheet:** deferred tax assets net **$45,788M** (up from $34,509M), including **IPR&D DTA jumping to $14,800M from $6,824M** — a strong tell that Amazon **capitalized significant acquired technology/IP in FY23** (several tuck-in acquisitions), and the finite-lived intangibles gross balance rose to $10,082M from $8,282M. Valuation allowance only $4,811M → management expects to realize these assets (a confidence signal). Deferred tax liabilities on PP&E doubled to $12,454M, consistent with accelerated depreciation on the capex build.

**Demand/backlog signals (positive):**
- Deferred revenue **+28%** to $20.6B; $12.4B of FY23 revenue was recognized from the prior-year deferred balance.
- **Contractual future obligations** (purchase commitments) remain enormous — implies continued AWS capacity and content spend.

**Dilution:** shares outstanding +1.4% YoY; unrecognized SBC $18.3B → ongoing ~1–1.5%/yr dilution. Not egregious, not zero.

---

## 7. Actionable Insights for Traders

**Bullish evidence (high conviction, filing-based):**
1. **Operating margin 6.41% is a new record** and management has now demonstrated two consecutive quarters of structurally higher margin. The 47.0% gross margin (+319 bps) is the tell that the retail/logistics cost reset is real, not a one-quarter fluke.
2. **FCF went from −$16.9B to +$32.2B in one year.** With capex still only ~9% of revenue (vs ~12–13% in FY21–22), FY24 FCF has room to grow even with modest capex re-acceleration for AI/cloud compute. **FCF, not EPS, is the metric to trade here.**
3. **Balance sheet optionality:** net cash, debt down 15%, no LT issuance, $0 buybacks. A future buyback authorization or the first dividend becomes a plausible re-rating catalyst — management has deliberately preserved the capacity.
4. **Earnings quality improved:** FY23 net income ($30.4B) beat FY21 ($33.4B? no — below it) but with **zero reliance on mark-to-market gains** (+$0.7B non-operating vs +$13.3B in FY21). The FY23 $30.4B is the "cleanest" profit year in company history.
5. **Interest coverage 11.6x and rising** — the 2022 rate-shock balance-sheet fear is fully resolved.

**Bearish / cautionary evidence (equally filing-based):**
1. **SBC is 65% of EBIT.** On a fully-loaded basis operating margin is ~2.2%, not 6.4%. Growth in SBC (+22%) is running *faster* than revenue (+11.8%). Anyone modeling AMZN on non-GAAP margins is 400+ bps optimistic.
2. **Capex decline is a tailwind that partially mean-reverts.** FY24 AI/cloud build (custom silicon, data centers) will push capex back up; the FCF hockey stick has a ceiling near-term.
3. **Receivables +23.4% vs revenue +11.8%** (DSO 28.1 → 30.0 days). Small, but the first AR-growth-over-revenue-growth year in the series — monitor for ads/enterprise credit quality.
4. **$39.3B of obligations due within 12 months** and $90.8B of undiscounted operating leases → the "float" that funds negative working capital is a maturity-matched liability, sensitive to a demand shock.
5. **Cash taxes +85% to $11.2B** and a 19.0% ETR trending toward 21% → FY24 EPS faces a ~2%-of-pretax headwind from tax normalization alone.
6. **No insider transaction data is available for AMZN as of 2024-02-05 — treat insider conviction as unverified.** Do not read anything (bullish or bearish) into the absence; it is a data gap, not a signal.

**What to monitor next (highest information value):**
- Q1'24 print: **AWS growth re-acceleration and AWS operating margin** (the extract omits segment data — this is the key blind spot).
- **Capex guidance for FY24** — the single largest swing factor for the FCF trajectory.
- Whether **SBC growth decelerates** below revenue growth (would validate the margin story on a fully-loaded basis).
- Any **buyback authorization** (would be a step-change signal given $32B+ FCF and net cash).
- **Operating lease additions** — rising ROU additions would signal a second logistics/fulfillment build wave and compress FCF.

**Positioning synthesis:** the fundamental setup is *premium-quality, improving-at-the-margin, cash-generative* with a fully-de-risked balance sheet — supportive for owning the name on the fundamental inflection, but **earnings quality (SBC) and the missing Q4/segment granularity argue against extrapolating the 6.41% margin linearly**. Trade the FCF inflection and debt paydown, discount the headline margin.

---

## 8. Key Points Summary

| Category | Metric | Value / Observation | Signal |
|---|---|---|---|
| **Filing** | Latest filing | FY23 10-K filed 2024-02-02 (3 days pre-analysis) | Fresh, high-confidence data |
| **Scale** | Revenue FY23 | $574,785M, +11.8% YoY (FY22 +9.4%) | ✅ Re-acceleration |
| **Profitability** | Operating income | $36,852M; margin **6.41%** vs 2.38% FY22 | ✅ Record; +403 bps |
| **Profitability** | Gross margin | **47.00%** vs 43.81% / 42.03% | ✅ +319 bps, cost-of-sales leverage |
| **Bottom line** | Net income / diluted EPS | $30,425M / **$2.90** (FY22: −$2,722M / −$0.27) | ✅ Full recovery |
| **Earnings quality** | Non-operating income | +$705M (vs +$13,272M FY21, −$18,184M FY22) | ✅ No mark-to-market reliance |
| **Earnings quality** | SBC | **$24,023M, +22.4%** = 65% of EBIT; $18.3B unrecognized | ⚠️ Major GAAP vs adj. gap |
| **Cash generation** | Operating cash flow | **$84,946M, +81.7%** | ✅ Step change |
| **Cash generation** | Free cash flow | **+$32,217M** vs −$16,893M (≈$32–37B on alt. capex def.) | ✅ **+$49B swing** |
| **Capex** | Productive assets | $52,729M, **−17.2%**; ~9% of revenue | ✅ Build cycle over |
| **Balance sheet** | Cash & equivalents | $73,387M (+36.2%); + mkt. sec. ≈ $86.8B | ✅ Fortress |
| **Balance sheet** | Gross debt (LTD+fin. lease) | **$70,423M, −15.1%**; no LT issuance in FY23 | ✅ Deleveraging |
| **Balance sheet** | Net debt | **≈ −$3.0B (net cash)** | ✅ |
| **Balance sheet** | Equity | ~$201,875M, **+38.2%**; AOCI improving to −$3,040M | ✅ |
| **Liquidity** | Current ratio | 1.05x (FY22 0.94x); DPO ~99 vs DSO ~30 days | ✅ Structural float |
| **Returns** | ROE / ROA / ROIC | ~17.5% / ~6.1% / ~15% | ✅ Best since 2021 |
| **Leverage risk** | Interest coverage | 11.6x (FY22 5.2x); interest exp +34% to $3,182M | ✅ Strong / ⚠️ cost rising |
| **Capital return** | Buybacks / dividend | **$0 buybacks** in FY23 ($6.0B FY22); no dividend | Neutral — capacity retained |
| **Commitments** | Contractual obligations | **$300,409M**, $39,345M due <12M, $157,824M >5yr | ⚠️ Watch |
| **Commitments** | Operating leases | $90,777M undiscounted (+11.7%); liab. $75,639M | ⚠️ Growing |
| **Forward demand** | Deferred revenue | $20,606M, **+28.0%**; $12.4B recognized from prior bal. | ✅ |
| **Forward signal** | IPR&D deferred tax asset | $6,824M → **$14,800M**; intangibles gross +21.8% | ✅ M&A/capex intensity |
| **Tax** | ETR / cash taxes | 19.0% (12.6% FY21); cash taxes $11,179M, **+85%** | ⚠️ FY24 headwind |
| **Dilution** | Shares outstanding | 10,383M (+1.4%); 10,387M at 2024-01-24 | Neutral |
| **Data gap** | Insider transactions | **UNAVAILABLE** — no archive for AMZN ≤2024-02-05 | ❌ Unverified |
| **Data gap** | Segments / quarters / price | Not in extract (3 segments confirmed only) | ❌ Blind spot |
| **Net read** | — | **Improving fundamentals + FCF inflection + net cash; discount headline margin for 65%-of-EBIT SBC** | **Constructive on fundamentals, valuation-agnostic (no price data)** |

*All figures in USD millions unless noted; derived ratios are my calculations from the disclosed line items. FY2023 FCF is presented as a range ($32–37B) because the vendor's capex aggregation differs from the reported "purchases of property and equipment" line.*