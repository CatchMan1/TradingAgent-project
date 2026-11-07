# AMZN (Amazon.com, Inc.) — Fundamental Research Report
**Point-in-time as of 2024-02-27 | Latest financials: FY2023 Form 10-K (accepted 2024-02-02, accn 0001018724-24-000008)**

---

## 0. Data coverage & limitations (read first)

| Requested | Status | Notes |
|---|---|---|
| Comprehensive fundamentals | ✅ | Point-in-time SEC XBRL facts, FY2021–FY2023, filtered by EDGAR acceptance time |
| Income statement | ⚠️ Partial | Only **annual (10-K)** period facts returned; no discrete quarterly P&Ls in the archive. "Revenues" is not directly tagged — derived below as *OperatingIncomeLoss + CostsAndExpenses* and cross-checked against reported segment math |
| Balance sheet | ✅ | 12/31/2022 and 12/31/2023 (plus some 2021 items) |
| Cash flow | ✅ | FY2021–FY2023 annual; FY2023 contains 9M-2023 10-Q facts |
| Insider transactions | ❌ **UNAVAILABLE** | Vendor has no authorized point-in-time insider archive for AMZN. **No insider activity is inferred or fabricated** — treat insider signal as *missing*, not *neutral* |

All figures below are **GAAP, USD, as-reported by AMZN in its FY2023 10-K**. Items marked "derived" are calculated by me from tagged line items.

---

## 1. Company profile

Amazon.com, Inc. (AMZN), SEC CIK 0001018724, files a **3-segment** structure (`NumberOfOperatingSegments = 3`) under US GAAP. The business is a globally scaled, vertically integrated platform spanning:

- **Online & physical retail** (1P product sales, Whole Foods/physical stores)
- **Third-party seller services** (1P/3P marketplace, fulfillment/FBA, advertising, subscriptions/Prime)
- **AWS** (cloud compute, storage, database, AI/ML infrastructure and services)

Distinctive fundamental characteristics visible in the filings:
- **Massive internally funded capital program**: $52.7B of productive-asset purchases in FY2023, $177.2B cumulative over FY2021–FY2023 — capex is the single largest discretionary use of cash.
- **Heavy operating-lease footprint**: $75.6B operating lease liability + $90.8B undiscounted lease commitments (fulfillment centers, data centers, offices).
- **SBC-intensive compensation model**: $24.0B of stock-based comp in FY2023 (4.2% of revenue), with $18.3B of unrecognized SBC cost outstanding.
- **Aggressive reinvestment, thin reported margins historically** now inflecting sharply upward (see §3).

Scale markers from the 10-K: 10,387,381,291 shares outstanding at 2024-01-24; 1.6B shares reserved for future issuance; public float of **$1.184 trillion at 2023-06-30** (stale — 8 months old — and only a size anchor, not a current market cap).

---

## 2. Income statement — three-year annual history

`Revenues` derived as OperatingIncomeLoss + CostsAndExpenses (FY21/22/23 = 469,822 / 513,983 / 574,785; this ties exactly to AMZN's reported net sales).

| $ millions | FY2021 | FY2022 | FY2023 | YoY FY23 |
|---|---:|---:|---:|---:|
| **Net sales (derived)** | **469,822** | **513,983** | **574,785** | **+11.8%** |
| Cost of goods & services | 272,344 | 288,831 | 304,739 | +5.5% |
| Gross profit (derived) | 197,478 | 225,152 | 270,046 | +19.9% |
| **Gross margin** | 42.0% | 43.8% | **47.0%** | +320 bps |
| Marketing expense | 32,551 | 42,238 | 44,370 | +5.0% |
| G&A expense | 8,823 | 11,891 | 11,816 | -0.6% |
| Advertising expense (incremental, per 10-K disclosure)* | 16,900 | 20,600 | 20,300 | -1.5% |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| **Operating income** | **24,879** | **12,248** | **36,852** | **+200.9%** |
| **Operating margin** | 5.30% | 2.38% | **6.41%** | +403 bps |
| Interest expense | 1,809 | 2,367 | 3,182 | +34.4% |
| Investment income (interest) | 448 | 989 | 2,949 | +198% |
| Non-operating income/(expense), net | 13,272 | (18,184) | 705 | n.m. |
| Pre-tax income | 38,151 | (5,936) | 37,557 | n.m. |
| Income tax expense/(benefit) | 4,791 | (3,217) | 7,120 | n.m. |
| **Net income** | **33,364** | **(2,722)** | **30,425** | n.m. |
| **Diluted EPS** | $3.24 | $(0.27) | $2.90 | n.m. |
| Basic EPS | $3.30 | $(0.27) | $2.95 | n.m. |
| D&A (cash-flow statement) | 34,433 | 41,921 | 48,663 | +16.1% |
| SBC (allocated) | 12,757 | 19,621 | 24,023 | +22.4% |

*\*AdvertisingExpense is an incremental disclosure (production/content/other marketing), not additive to MarketingExpense.*

**Non-operating line is the key FY2022 distortion:** FY2022's $(18.2)B non-operating loss vs. +$13.3B in FY2021 and +$0.7B in FY2023 is dominated by equity-securities mark-to-market (`EquitySecuritiesFvNiUnrealizedGainLoss`: +$11.6B → **$(13.6)B** → +$1.0B). The Rivian stake revaluation alone explains the GAAP net loss in FY2022 — **not** operating deterioration. FY2023 earnings are therefore *cleaner quality* than FY2021's.

**Geographic pre-tax split (durable profit engine):** US pre-tax income $32,328M; foreign $5,229M (vs. $2,289M in FY2022, +128%) — international profitability is inflecting.

---

## 3. The core fundamental story: margin inflection

Three consecutive years of data show a decisive shift from growth-at-any-cost to cost-discipline + mix:

1. **Revenue growth decelerated** from +19.2% (FY22: 513,983/... vs FY21 469,822) — actually FY2022 +9.4%, FY2023 +11.8% — re-accelerating modestly.
2. **Yet operating income nearly tripled** (+200.9%) in FY2023 because cost growth (+7.2%) ran ~470bps *below* revenue growth (+11.8%).
3. **Gross margin +320bps to 47.0%** — cost of goods grew only 5.5% on 11.8% revenue growth, consistent with: (a) regionalization/fulfillment-efficiency gains, (b) mix shift toward higher-margin 3P seller services, advertising and AWS, (c) lapping FY2022 overcapacity and $1.1B of asset impairments (FY2022 `AssetImpairmentCharges` $1.1B; zero impairment in FY2023).
4. **Opex leverage in marketing** (+5.0% vs revenue +11.8%) and **G&A actually declining** (-0.6%) — headcount/overhead discipline shows up directly in the P&L.
5. **Depreciation is the brake, not the accelerator:** D&A rose 16.1% (faster than revenue), a lagged consequence of the FY2021–22 capex boom. This is why ROA remains only ~6%.
6. **Interest burden is now near-neutral:** interest expense $3,182M vs. interest income $2,949M (+198% y/y as the cash+T-bill pile grew). Net interest drag only ~$233M — a major swing factor vs. FY2021's $1.36B drag.

---

## 4. Balance sheet (12/31/2023) — fortress liquidity

| $ millions | 12/31/2022 | 12/31/2023 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 53,888 | **73,387** | +36.2% |
| Marketable securities (AFS debt, fair value) | n/a in cache | **70,919** | — |
| **Total cash + securities (derived)** | — | **~144,306** | — |
| Accounts receivable, net | 42,360 | 52,253 | +23.4% |
| Allowance for doubtful accounts | 1,400 | 1,700 | +21.4% |
| Current assets | 146,791 | 172,351 | +17.4% |
| **Total assets** | **462,675** | **527,854** | **+14.1%** |
| Accounts payable | 79,600 | 84,981 | +6.8% |
| Accrued liabilities | 62,566 | 64,709 | +3.4% |
| Contract liabilities (unearned revenue), current | 13,227 | 15,227 | +15.1% |
| **Total current liabilities (derived)** | — | **164,917** | — |
| Long-term debt (carrying) | 67,150 | **58,314** | **-13.2%** |
| Finance lease liabilities | 15,783 | 12,109 | -23.3% |
| Operating lease liabilities | 69,040 | 75,639 | +9.6% |
| Contract liabilities, non-current | 2,900 | 5,700 | +96.6% |
| Additional paid-in capital | 75,066 | 99,025 | +31.9% |
| AOCI | (4,487) | (3,040) | improving |
| **Total stockholders' equity (derived)** | **146,043** | **~201,875** | **+38.2%** |
| Total liabilities (derived) | 316,632 | ~325,979 | +2.9% |
| Shares outstanding | 10,242 | 10,383 | +1.4% |

(Equity/liabilities derived from Assets less the stated equity components; the current-liability sum reconciles exactly to AP + accrued + unearned revenue, consistent with AMZN's presentation.)

**Liquidity & leverage diagnostics (all derived):**

| Metric | Value | Read |
|---|---:|---|
| Current ratio | 172,351 / 164,917 = **1.05x** | Thin but structurally normal for AMZN (negative working-capital retail model) |
| Working capital | **+$7.4B** | Positive, thin |
| Gross debt (bonds + finance leases) | $70,423 | Down from $82,933 (-15.1%) |
| **Net cash position** | **~+$73.9B** | Cash+securities $144.3B minus debt $70.4B |
| Debt / equity | 28.9% (34.9% incl. finance leases) | Conservative |
| Interest coverage (EBIT/interest) | 36,852 / 3,182 = **11.6x** | Strong; was 5.2x in FY2022 |
| Equity ratio | 38.2% | Up from 31.6% |

**Key point for traders:** AMZN is **net-cash by roughly $74B** and has ~2.0x coverage of all debt from a single year's operating cash flow. Balance-sheet risk is not a thesis variable here; **capital allocation and capex are.**

**Contract liabilities (unearned revenue) +27.9% to $20.6B** and the $12.4B of FY2023 revenue recognized from the opening contract-liability balance are healthy forward-demand indicators (Prime subscriptions, AWS prepayments).

---

## 5. Cash flow — the standout improvement

| $ millions | FY2021 | FY2022 | FY2023 | YoY |
|---|---:|---:|---:|---:|
| **Operating cash flow** | 46,327 | 46,752 | **84,946** | **+81.7%** |
| Purchases of productive assets (capex) | (61,053) | (63,645) | **(52,729)** | **-17.2%** |
| **Free cash flow (derived)** | **(14,726)** | **(16,893)** | **+32,217** | **n.m. (swing of ~$49B)** |
| Investing cash flow, net | (58,154) | (37,601) | (49,833) | — |
| Financing cash flow, net | +6,291 | +9,718 | **(15,879)** | deleveraging |
| Buybacks | 0 | (6,000) | **0** | none in FY2023 |
| Long-term debt issued | 19,003 | 21,166 | **0** | no new bonds |
| Long-term debt repaid | (1,590) | (1,258) | (3,676) | — |
| Short-term debt, net | +203 | +3,999 | (7,548) | paydown |
| Finance lease principal | (11,163) | (7,941) | (4,384) | shrinking |
| Operating lease payments | (6,722) | (8,633) | (10,453) | +21% |
| Taxes paid, net | 3,688 | 6,035 | **11,179** | +85% |
| Cash taxes / pre-tax income | 9.7% | n.m. | **29.8%** | normalizing |

**Interpretation:**
- **FCF swung ~+$49B in one year** to $32.2B — the single most important fundamental datapoint in this dataset. Drivers: OCF +$38.2B (working-capital-neutral; driven by operating income + D&A) and capex **-17.2%**.
- **Cash conversion is excellent:** OCF/net income = **2.79x**, consistent with a capital-intensive, high-D&A business; OCF less capex still covers net income 1.06x.
- **Capex intensity fell to 9.2% of revenue** (FY2021 13.0%, FY2022 12.4%). This is the margin/FCF lever — but note it is *cyclical posture*, not a permanent reset: AWS/AI infrastructure demand argues capex re-accelerates (not in this dataset; monitor Q1'24 10-Q).
- **Zero buybacks and zero new long-term debt in FY2023** while repaying $15.9B net in financing — disciplined deleveraging funded entirely by operations. The $6.0B repurchased in FY2022 was the only buyback in three years.
- **Taxes paid nearly doubled to $11.2B** and the effective rate rose to ~19.0% (7,120/37,557). The FY2022 benefit of $(3.2)B was driven by a $(8.1)B deferred tax benefit — a one-off. **Expect a structurally higher cash tax rate going forward** — a mild headwind to EPS growth that some models underweight.

**Cash flow quality note:** FY2023 OCF benefited from a $4.6B increase in contract liabilities (vs. $2.2B in FY2022) and was *dragged* by a $(2.4)B change in accrued liabilities and $(12.3B) increase in other non-current assets (`IncreaseDecreaseInOtherNoncurrentAssets` 12,265). So the $84.9B is not working-capital-inflated — a high-quality number.

---

## 6. Returns, dilution, and capital efficiency

| Metric | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| ROE (net income / avg equity) | 24.1% | -1.8% | **~17.5%** |
| ROA (net income / avg assets) | 8.4% | -0.6% | **~6.1%** |
| ROIC proxy (EBIT×(1-19%) / avg (debt+equity)) | ~10.5% | ~3.9% | **~11.9%** |
| SBC / revenue | 2.7% | 3.8% | **4.2%** |
| SBC / operating income | 51% | 160% | **65%** |
| Shares outstanding growth | — | +1.4% (net of $6B buyback) | **+1.4%** |
| Unrecognized SBC (years to amortize) | — | — | **$18.3B** |

- ROE of ~17.5% and ROIC ~11.9% are respectable but remain **below the ~13–15% WACC-plus bar** that a high-multiple name needs to justify reinvestment. The FY2023 improvement is real but mostly margin-recovery, not yet capital-efficiency expansion.
- **SBC at $24.0B (+22.4%) growing 2x faster than revenue is the sharpest GAAP-vs-"true earnings" gap.** Real dilution (~1.4%/yr) plus $18.3B of unrecognized SBC means GAAP EPS overstates distributable owner earnings by a material amount. Adjusted for SBC, FY2023 "owner earnings" would be roughly $32.2B FCF − $24.0B SBC ≈ **$8B** — the single most important caution in this report, and the number bears should focus on.
- **No buyback in FY2023** means dilution is running at full rate. Watch for any buyback authorization reinstatement as a catalyst.

---

## 7. Off-balance-sheet and contractual obligations (12/31/2023)

Total contractual obligations **$300.4B**, of which lease and debt schedule detail is tagged:

| Obligation | Total | <1 yr | 1–2 yr | 2–3 yr | 3–4 yr | 4–5 yr | >5 yr |
|---|---:|---:|---:|---:|---:|---:|---:|
| Operating leases (undiscounted) | 90,777 | 11,229 | 9,922 | 9,156 | 8,321 | 7,546 | 44,603 |
| Finance leases (undiscounted) | 14,106 | 2,292 | 1,471 | 1,369 | 1,123 | 1,022 | 6,829 |
| Long-term debt principal | 63,170 | 8,500 | 5,286 | 3,146 | 8,750 | 2,250 | 39,250 |
| **Total contractual obligations** | **300,409** | 39,345 | 30,863 | 25,713 | 28,398 | 18,266 | 157,824 |

- **$157.8B (53%) falls due after year 5** — a long-dated, inflation-friendly liability profile. The operating-lease (>5yr) bucket is the largest single category.
- **$39.3B due within 12 months** vs. $144.3B of cash + marketable securities and $84.9B annual OCF → **comfortable ~3.7x coverage of near-term obligations from liquid assets alone.**
- The ~$132B of *unallocated* purchase obligations (300,409 − 90,777 − 14,106 − 63,170) represents committed content (sports/NFL, video), capacity, and energy purchases — a real fixed-cost risk if AWS/retail demand softens.
- Finite-lived intangibles amortization: **$715M (FY24), $631M, $563M, $552M, $534M, then $3,545M thereafter** — small and declining, no impairment overhang. Indefinite-lived intangibles flat at $1,147M (no impairment taken in FY2023; FY2022 saw $1.1B of impairments).

---

## 8. Insider transactions

**NOT AVAILABLE.** The vendor's news/insider archive contains no authorized, point-in-time insider-transaction record for AMZN as of 2024-02-27. I will not infer or fabricate insider activity. **Treat this as an information gap in the report, not as evidence of absence of insider selling.** Traders should source Form 4s independently (EDGAR, CIK 0001018724) — particularly Bezos's pre-announced 10b5-1 selling plan, which is a routine but sentiment-relevant supply factor that this dataset cannot confirm or quantify.

---

## 9. Risk register (evidence-based, from the filings)

| Risk | Evidence in the data | Severity |
|---|---|---|
| **Capex re-acceleration kills the FCF story** | Capex already $52.7B (9.2% of sales); AWS/AI demand requires buildout; FY21–22 shows FCF can swing to **-$16.9B** | **High** |
| **SBC dilution / GAAP vs. owner earnings gap** | $24.0B SBC, 4.2% of revenue, +22.4% y/y; $18.3B unrecognized; no buyback to offset | **High** |
| **Effective tax rate normalization** | FY22 effective rate was a benefit; FY23 taxes paid +85% to $11.2B, rate ~19%; $4.8B valuation allowance still on books | Medium |
| **Fixed obligations** | $300.4B contractual; $39.3B <1yr; $132B purchase/content commitments | Medium |
| **Equity-mark-to-market earnings noise** | ±$1–14B swings in `EquitySecuritiesFvNiUnrealizedGainLoss` contaminated FY21/FY22 GAAP EPS | Medium (headline risk) |
| **Lease/fixed-cost operating leverage** | Operating lease liability +9.6% to $75.6B; opex payments +21% y/y | Medium |
| **Interest expense trend** | $1.8B → $2.4B → $3.2B (though offset by $2.9B interest income) | Low |
| **Goodwill/intangibles** | Small ($10.1B gross); no FY23 impairment | Low |
| **Liquidity/solvency** | Net cash ~+$74B; 11.6x interest cover | **Minimal** |

---

## 10. Actionable insights for traders

1. **The FY2023 10-K is a bullish fundamental print, and the market-visible catalyst is already out (filed 2024-02-02).** The single most tradeable line is **FCF of +$32.2B vs. -$16.9B a year ago** — a ~$49B swing. Any narrative that "Amazon doesn't make money" is now factually stale as of this filing.

2. **Trade the capex pendulum, not the revenue line.** Revenue growth (+11.8%) is unremarkable; the entire margin story rests on capex falling 17.2% while gross margin rose 320bps. **The asymmetric risk is capex guidance moving back up** (FY24 AI/AWS infrastructure). Watch the Q1'24 10-Q capex line as the first falsifier — if capex/revenue climbs back above ~11%, the FCF run-rate compresses fast given $48.7B of D&A already in the base.

3. **Quality-check the EPS: on a SBC-adjusted basis FY2023 owner earnings are ~$8B, not $30.4B.** If you are underwriting AMZN on a GAAP EPS multiple, you are overpaying. Position sizing should reflect that $24B of annual comp is paid in stock (~1.4%/yr dilution) with no buyback offset. **A buyback authorization is the highest-conviction re-rating catalyst that is currently absent.**

4. **Balance sheet is a non-issue and actually a put under the stock.** ~$144B cash+securities, ~$70B gross debt (down 15%), net cash ~+$74B, 11.6x interest coverage, zero new LT debt issued in FY2023. AMZN can fund a full capex super-cycle without external capital. Do not short this on leverage/liquidity concerns.

5. **Deleveraging + prime-demand indicators support a "quality compounder" framing:** contract liabilities (unearned revenue) +27.9% to $20.6B, foreign pre-tax income +128%, G&A -0.6%. These are the leading indicators of durable, mix-driven margin expansion rather than one-off cost cuts.

6. **Watch the tax line for an EPS air-pocket.** Cash taxes jumped 85% to $11.2B and the FY2022 GAAP benefit ($(3.2)B tax expense, $(8.1)B deferred) will not recur. Consensus models that anchor to FY2023's ~19% effective rate should be fine; models that carry forward any benefit are too high.

7. **Do not act on insider signals from this report** — the data is missing. Independently verify Form 4 flow before assuming management confidence or supply pressure.

**Bottom line: fundamentals are in a clear upcycle (margin +403bps, operating income +201%, FCF +$49B swing, net cash $74B), but the re-rating case now depends entirely on capex discipline holding and on management addressing $24B of SBC dilution. The filing is a "buy the quality of the cash flow, rent the margin" setup — long bias justified by the data, but with an explicit stop on capex re-acceleration.**

---

## 11. Key points summary table

| Category | Metric | FY2021 | FY2022 | FY2023 | Assessment |
|---|---|---:|---:|---:|---|
| **Scale** | Net sales (derived, $M) | 469,822 | 513,983 | 574,785 | Growth +11.8% (FY23) |
| **Growth** | Revenue YoY | — | +9.4% | +11.8% | Modest re-acceleration |
| **Profitability** | Gross margin | 42.0% | 43.8% | **47.0%** | +320bps — strong |
| **Profitability** | Operating income ($M) | 24,879 | 12,248 | **36,852** | +201% — inflection |
| **Profitability** | Operating margin | 5.30% | 2.38% | **6.41%** | +403bps |
| **Earnings** | Net income ($M) | 33,364 | (2,722) | 30,425 | FY22 loss = Rivian MTM, not ops |
| **Earnings** | Diluted EPS | $3.24 | $(0.27) | $2.90 | Below FY21 peak on higher SBC/D&A |
| **Cash flow** | Operating cash flow ($M) | 46,327 | 46,752 | **84,946** | +81.7% |
| **Cash flow** | Capex ($M) | (61,053) | (63,645) | **(52,729)** | -17.2% |
| **Cash flow** | **Free cash flow ($M)** | (14,726) | (16,893) | **+32,217** | **~$49B swing — the headline** |
| **Cash flow** | FCF margin | -3.1% | -3.3% | **+5.6%** | Turnaround |
| **Cash flow** | Capex / revenue | 13.0% | 12.4% | **9.2%** | The margin lever |
| **Liquidity** | Cash + marketable securities ($M) | — | — | **~144,306** | Fortress |
| **Leverage** | Long-term debt ($M) | — | 67,150 | **58,314** | -13.2% |
| **Leverage** | Net cash ($M, derived) | — | — | **~+73,883** | Net cash |
| **Leverage** | Interest coverage | 13.8x | 5.2x | **11.6x** | Strong |
| **Returns** | ROE | 24.1% | -1.8% | **~17.5%** | Recovering |
| **Returns** | ROA | 8.4% | -0.6% | **~6.1%** | Depressed by capex base |
| **Returns** | ROIC proxy | ~10.5% | ~3.9% | **~11.9%** | Still near cost of capital |
| **Dilution** | SBC ($M) | 12,757 | 19,621 | **24,023** | 4.2% of revenue — key risk |
| **Dilution** | Shares out (M) | — | 10,242 | 10,383 | +1.4%, no buyback |
| **Capital return** | Buybacks ($M) | 0 | 6,000 | **0** | Absent |
| **Tax** | Cash taxes paid ($M) | 3,688 | 6,035 | **11,179** | +85%, normalizing |
| **Obligations** | Total contractual ($M) | — | — | **300,409** | $39.3B due <1yr, covered 3.7x |
| **Insider** | Transactions | — | — | **DATA UNAVAILABLE** | Information gap — not neutral |

---

*Prepared 2024-02-27 from point-in-time SEC XBRL facts (FY2023 10-K, accepted 2024-02-02, accn 0001018724-24-000008). Quarterly income-statement detail and insider-transaction archives were not available from the configured vendor for this instrument/date; no figures beyond tagged filings were inferred or estimated as reported values. Derived metrics are labeled as such.*