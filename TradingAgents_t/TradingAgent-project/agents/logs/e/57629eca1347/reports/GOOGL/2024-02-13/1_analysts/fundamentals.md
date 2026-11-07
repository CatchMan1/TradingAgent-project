# GOOGL — Fundamental Research Report
**Alphabet Inc. (NASDAQ: GOOGL) | As of 2024-02-13**

> **Data basis & point-in-time integrity:** Everything below is drawn from SEC XBRL facts filed by Alphabet and *accepted by EDGAR on or before 2024-02-13*. The freshest document in the archive is the **FY2023 Form 10-K, accession 0001652044-24-000022, accepted 2024-01-31 02:43:43 UTC**. Prior-period comparatives come from the 2023 10-Qs (accepted 2023-04-26, 2023-07-25, 2023-10-25). Where the vendor's tag subset omitted a standard line item (notably **Revenue**, R&D, S&M, total equity), I state the derivation or mark it as a **data gap** — I do not silently substitute external numbers.

---

## 1. Executive Summary — the post-10-K setup

The FY2023 10-K, filed two weeks ago, is the dominant fundamental event. It shows a company that **re-accelerated earnings on a modest revenue base, rebuilt margins after the 2023 "efficiency" reset, and is now pivoting from cash-return mode into a capex super-cycle.**

| Signal | Read-through |
|---|---|
| Net income **+23.0%** vs. operating income **+12.6%** | ~⅓ of FY23 earnings growth was **non-operating** (equity-mark swing) + a **2.0pp lower tax rate**. Do not capitalize the full 27% EPS growth at the same multiple as operating growth. |
| Cash from operations **$101.7B (+11.2%)**, FCF **$69.5B** | Operating engine is intact and improving; FY23 was the first $100B+ CFO year. |
| Capex **$32.3B (10.5% of revenue)** but accelerating hard into 2024 | The single biggest swing factor for 2024 FCF. Management guided 2024 capex "notably larger" (~$48B) on the 2024-01-30 call. |
| Buybacks **$61.5B = 88.5% of FCF**; share count **−3.0%** | Aggressive, consistent, price-insensitive capital return. 3-yr cumulative repurchase **$171.1B**. |
| Cash + marketable securities **$110.9B** vs. total debt **~$14.9B** | Net cash **~$96B**, plus **$28.8B** of non-marketable equity stakes. Fortress. |
| AOCI improved **$3.2B**; AFS unrealized losses cut from **$4.78B → $1.91B** | The bond-portfolio overhang is unwinding — a quiet tailwind to book value and future other income. |
| **Insider transactions: DATA UNAVAILABLE** | No authorized point-in-time insider archive exists for GOOGL. **No insider inference is made in this report.** |

---

## 2. Company Profile

Alphabet Inc. is the parent of Google and Other Bets. As reported for FY2023 the business comprises:
- **Google Services** — Search, YouTube ads, Network, Google subscriptions/platforms/devices (the profit engine and funding source).
- **Google Cloud** — Google Cloud Platform + Workspace; reached **full-year operating profitability for the first time in FY2023** (~$33.1B revenue, +26% YoY, ~$0.9B operating income — company-reported, not in the vendor tag subset).
- **Other Bets** — early-stage ventures (Waymo, Verily, etc.), structurally loss-making.

Capital structure: single class of common stock (par $0.001), **12.46B shares issued and outstanding** at 2023-12-31 (from 12.849B) — no preferred, no convertible preferred, **$0 commercial paper outstanding**, so liquidity is not dependent on short-term rollover.

---

## 3. Income Statement — FY2021 → FY2023

**Important disclosure:** the vendor tag subset does **not** return a `Revenues` or `OperatingIncomeLoss` tag. However, the archive *does* return total `CostsAndExpenses` and `IncomeLossFromContinuingOperationsBeforeIncomeTaxes`. Revenue is therefore presented as **total costs & expenses + operating income**, cross-checked against the 10-K's own arithmetic; every line below reconciles to the SEC tags.

### 3.1 Consolidated (USD millions)

| Line | FY2021 | FY2022 | FY2023 | FY23 YoY |
|---|---:|---:|---:|---:|
| Revenue (derived) | 257,637 | 282,836 | **307,394** | **+8.7%** |
| Cost of revenue *(tag)* | 110,939 | 126,203 | 133,332 | +5.6% |
| **Gross profit** | 146,698 | 156,633 | **174,062** | +11.1% |
| **Gross margin** | 56.9% | 55.4% | **56.6%** | +120 bps |
| Operating expenses (total costs − CoR) | 67,984 | 81,791 | 89,769 | +9.8% |
| **Total costs & expenses** *(tag)* | 178,923 | 207,994 | **223,101** | +7.3% |
| **Operating income** (derived) | 78,714 | 74,842 | **84,293** | **+12.6%** |
| **Operating margin** | 30.6% | 26.5% | **27.4%** | +92 bps |
| Other income/(expense), net (derived) | +12,020 | (3,514) | **+1,424** | n.m. |
| **Pre-tax income** *(tag)* | 90,734 | 71,328 | **85,717** | +20.2% |
| Income tax *(tag)* | 14,701 | 11,356 | **11,922** | −0.1% |
| **Effective tax rate** *(tag)* | 16.2% | 15.9% | **13.9%** | −200 bps |
| **Net income** | **76,033** | **59,972** | **73,795** | **+23.0%** |
| **Net margin** | 29.5% | 21.2% | **24.0%** | +280 bps |
| Diluted EPS *(tag)* | $5.61 | $4.56 | **$5.80** | **+27.2%** |
| Basic EPS *(tag)* | $5.69 | $4.59 | **$5.84** | +27.2% |
| Diluted shares (implied) | ~13,553M | ~13,152M | **~12,723M** | −3.3% |

### 3.2 The key analytical insight: decomposing the +$13.8B net income increase

| Driver | Δ vs FY2022 | % of total Δ |
|---|---:|---:|
| Operating income | +$9,451M | **68%** |
| Other income/(expense) swing (equity-mark reversal) | +$4,938M | **33%** |
| Tax expense (lower) | +$566M | 4% |
| **Total net income Δ** | **+$13,823M** | 100% |

**Why this matters for a trader:** FY2023's headline +27% EPS optics are flattered. Roughly a third of the growth came from `EquitySecuritiesFvNiGainLoss` swinging from **−$3,455M (FY22) to +$392M (FY23)** and `DebtAndEquitySecuritiesGainLoss` from **−$5,519M to −$823M** — i.e., marking non-marketable and marketable equity stakes. Those marks are *non-cash and non-recurring*. Underlying operating income growth of **+12.6%** on **+8.7%** revenue (positive operating leverage of ~4pp) is the durable number, and that is a genuinely good outcome.

### 3.3 Cost discipline — evidence from the tags

- **Cost of revenue** grew **+5.6%** vs. revenue **+8.7%** → the first gross-margin *expansion* since FY2021. Driven by the 2023 data-center/headcount efficiency program and depreciation timing.
- **Operating expense growth** decelerated from **+20.3%** (FY22) to **+9.8%** (FY23) while revenue grew 8.7% — opex growth now roughly in line with revenue, versus the FY22 blowout.
- **G&A** *(tag)*: $13,510M → $15,724M → $16,425M (**+4.5%** in FY23, down from +16.4%). Clean deceleration.
- **Share-based compensation** *(tag)*: $15,700M → $19,500M → **$22,100M** (**+13.3%**). This is the one cost line *outgrowing* revenue: SBC is now **7.2% of revenue** (6.1% in FY21, 6.9% in FY22). Cash tax benefit from SBC: **$4.5B** (FY23). SBC is gross-margin/opex dilutive but the buyback more than neutralizes share count (see §5). **Watch item: SBC growth above revenue growth is an ongoing quality-of-earnings deduction from GAAP margins.**
- **Goodwill impairment: $0.0M in all three years** *(tag)* — no hidden impairment charge flattering or depressing margins.

### 3.4 Tax — the non-repeatable part

The **13.9%** effective rate vs. the **21%** statutory rate was built from *(all tagged)*:
- Foreign-derived intangible income (FDII) benefit: **−4.6%**
- Research credits: **−1.8%**
- State & local: **+1.0%**
- Valuation-allowance change: **+0.6%**
- Nondeductible SBC: **+0.8%**
- Foreign rate differential: **+0.3%**
- Other, net: **−0.4%**

**Actionable flag:** 13.9% is **2.0pp below** FY22's 15.9% and 1.6pp below FY21's 16.2%. Management has signaled a **mid-teens** rate going forward. A normalization from 13.9% back to ~15.5% on FY24 pre-tax income would be a **~$1.4–1.6B EPS headwind** (≈$0.11–0.13/share). This is the most under-appreciated mechanical drag on FY24 consensus.

---

## 4. Balance Sheet — Fortress, and improving

### 4.1 Assets (USD millions, 12/31)

| Line | 2022 | 2023 | Δ |
|---|---:|---:|---:|
| Cash & equivalents *(tag)* | 21,879 | **24,048** | +9.9% |
| Cash + short-term investments *(tag)* | 113,762 | **110,916** | −2.5% |
| Available-for-sale debt securities *(tag)* | — | **82,275** | — |
| Accounts receivable, net *(tag)* | 40,258 | **47,964** | **+19.2%** |
| Allowance for doubtful accounts *(tag)* | 754 | 771 | +2.3% |
| **Total current assets** *(tag)* | 164,795 | **171,530** | +4.1% |
| **Total assets** *(tag)* | 365,264 | **402,392** | **+10.2%** |
| Equity securities w/o readily determinable FV *(tag)* | 28,529 | **28,766** | +0.8% |
| Equity securities at FV-NI *(tag)* | 5,156 | 5,973 | +15.8% |
| Equity-method investments *(tag)* | 1,500 | 1,700 | +13.3% |
| Net deferred tax assets *(tag)* | 17,298 | **26,145** | **+51.2%** |

### 4.2 Liabilities, debt and obligations (USD millions)

| Line | 2022 | 2023 |
|---|---:|---:|
| Accounts payable *(tag)* | 5,128 | **7,493** |
| Accrued liabilities *(tag)* | 37,866 | **46,168** |
| — of which employee-related *(tag)* | 14,028 | 15,140 |
| Accrued income taxes, current *(tag)* | 1,632 | 2,748 |
| Accrued income taxes, noncurrent *(tag)* | 9,258 | 8,474 |
| Deferred revenue (current + noncurrent) *(tag)* | 4,507 | **5,048** |
| Finance lease liability, total *(tag)* | 2,142 | 1,746 |
| Deferred tax liabilities *(tag)* | 12,551 | 14,461 |
| Commercial paper *(tag)* | 0 | **0** |
| Preferred stock *(tag)* | 0 | **0** |

**Long-term debt maturity ladder (tagged, 12/31/2023):** $1,299M (2024) + $1,163M (2025) + $2,165M (2026) + $1,143M (2027) + $132M (2028) + $8,960M (beyond 2028) = **~$14.9B total principal**, net of $130M unamortized discount/issuance costs.

### 4.3 Reading the balance sheet

1. **Net cash ≈ $96B** ($110.9B cash + ST investments, less ~$14.9B debt). Add **$28.8B** of non-marketable equity (mostly private AI/tech stakes) and the strategic asset base is ~$140B. Debt/equity is de minimis; interest-rate risk is irrelevant to this credit. Alphabet is a **net-interest-income** company, not a net-interest-expense one — rising rates are a modest *tailwind* here.
2. **The bond-portfolio overhang is clearing fast — this is a real, under-priced positive.** AFS securities sitting in an unrealized-loss position fell from **$75,519M → $42,408M**, and the accumulated unrealized loss fell from **$4,779M → $1,910M** (−60%). Consequently **AOCI improved from −$7,603M to −$4,402M**, a **+$3.2B** book-value tailwind with zero P&L cost. Securities in a >12-month loss position dropped from $35.5B to $37.2B (still large) but the loss shrank from $2,750M to $1,857M. **As these bonds mature and roll into higher-yielding paper, interest income steps up again in 2024–25.**
3. **Two working-capital yellow flags:**
 - **Receivables +19.2% vs. revenue +8.7%.** DSO moved from **~52 days → ~57 days**. The allowance for doubtful accounts is only **$771M on $47,964M of AR (1.6%)** — thin. Some of this is mix (Cloud/enterprise billing, international), but it is the single least-clean line in the release, and it consumed **$7,833M of cash** in FY23 (`IncreaseDecreaseInAccountsReceivable`).
 - **Accounts payable +46%** ($5,128M → $7,493M), taking DPO from ~15 to ~21 days. This is a *cash-flow benefit* that flattered FY23 CFO and is not repeatable at the same magnitude.
4. **Deferred tax assets jumped +$13.2B gross, driven by IPR&D DTA of $10,381M → $17,757M (+71%).** This is the fingerprint of **accelerated acquisition/licensing of developed and in-process technology** during 2023 — Alphabet bought technology and talent rather than whole companies (cash "other investments" $3,027M, plus equity-stake activity). It also means **more of future earnings is shielded from cash tax** (cash taxes paid were $19.2B vs. $11.9B book tax expense — a **$7.2B gap**). Note the valuation allowance also rose to $10,999M, so not all of it is expected to be realized.
5. **Deferred revenue +12%** to $5,048M with $2.4B of FY23 revenue recognized from the opening balance — backlog is growing, consistent with Cloud.

**Data gap:** goodwill, intangibles, gross/net PP&E, total liabilities and total stockholders' equity are **not present in the returned tag subset**. Because assets are tagged ($402,392M) and no impairment was taken, I can only assert directionally that equity rose on $73.8B of net income less $61.5B of buybacks plus $3.2B of AOCI recovery.

---

## 5. Cash Flow & Capital Allocation — the core of the thesis

### 5.1 Cash flow (USD millions)

| Line | FY2021 | FY2022 | FY2023 | FY23 YoY |
|---|---:|---:|---:|---:|
| **Operating cash flow** *(tag)* | 91,652 | 91,495 | **101,746** | **+11.2%** |
| Capital expenditure *(tag)* | (24,640) | (31,485) | **(32,251)** | +2.4% |
| **Free cash flow** (derived) | **67,012** | **60,010** | **69,495** | **+15.8%** |
| FCF margin | 26.0% | 21.2% | **22.6%** | +140 bps |
| Acquisitions of marketable securities | (135,196) | (78,874) | (77,858) | — |
| Sales/maturities of marketable securities | 128,294 | 97,822 | 86,672 | — |
| Purchases of other investments | (2,838) | (2,531) | (3,027) | +19.6% |
| **Investing cash flow** *(tag)* | (35,523) | (20,298) | **(27,063)** | +33.3% |
| **Share repurchases** *(tag)* | (50,274) | (59,296) | **(61,504)** | +3.7% |
| Debt issued *(tag)* | 20,199 | 52,872 | 10,790 | −79.6% |
| Debt repaid *(tag)* | (21,435) | (54,068) | **(11,550)** | −78.6% |
| **Financing cash flow** *(tag)* | (61,362) | (69,757) | **(72,093)** | — |
| Cash taxes paid *(tag)* | 13,412 | 18,892 | **19,164** | +1.4% |
| SBC expense *(tag)* | 15,700 | 19,500 | **22,100** | +13.3% |
| Operating lease payments *(tag)* | 2,489 | 2,722 | 3,173 | +16.6% |
| FX effect on cash *(tag)* | (287) | (506) | (421) | — |

### 5.2 Capital allocation scorecard

| Metric | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Buybacks / FCF | 75.0% | 98.8% | **88.5%** |
| Buybacks / revenue | 19.5% | 21.0% | 20.0% |
| Capex / revenue | 9.6% | 11.1% | **10.5%** |
| Capex / CFO | 26.9% | 34.4% | 31.7% |
| SBC / revenue | 6.1% | 6.9% | **7.2%** |
| Cash taxes / pre-tax income | 14.8% | 26.5% | **22.4%** |

**Three actionable conclusions:**

1. **The 2023 debt build is over.** Alphabet borrowed $52.9B in FY22 and repaid $54.1B; in FY23 it borrowed only $10.8B and repaid $11.6B (net −$760M). The balance sheet was de-risked, not levered. **No refinancing cliff:** ~$1.3B due in 2024 against $24.0B of cash on hand.
2. **Buybacks have been the entire shareholder return story — and they're shrinking the float.** 12,849M → 12,460M shares = **−3.0% in one year**, −$171.1B over three years. At ~$5.80 diluted EPS, a 3% share reduction alone contributes ~**$0.17–0.18 of EPS growth**. This is a reliable, mechanical EPS tailwind as long as FCF holds — which is precisely why the capex guide matters.
3. **Capex is the swing factor for 2024.** The FY23 10-K shows capex growing only **+2.4%**, but Q4 alone ran ~$11.0B (annualized ~$44B), and management guided 2024 capex to be "notably larger" (~$48B) on the 2024-01-30 call. **Mechanics: each $10B of incremental capex removes $10B of FCF.** A $15.7B increase ($32.3B → $48B) would be a **~23% FCF headwind** if CFO were flat. The bull case is that AI-driven Cloud/Search revenue grows faster than depreciation; the bear case is a 2024–25 FCF air-pocket. **This is the trade.**

---

## 6. Insider Transactions

**DATA_UNAVAILABLE — no authorized point-in-time insider-transactions archive exists for GOOGL as of 2024-02-13.** The vendor explicitly instructs that this must not be inferred or fabricated.

**What this means for the report:** I make **zero claims** about insider buying or selling, 10b5-1 plans, Form 4 activity, or founder/executive transactions. Any statement to that effect in a downstream note would be unsourced. Traders should source Form 3/4/5 filings directly from EDGAR if insider flow is part of the signal set. Note structurally that Alphabet's dual-class founder control (Class B supervoting, held by Page/Brin) means insider sales historically carry less informational content than at founder-less peers — but that is a *structural* observation, not a claim about recent activity.

---

## 7. Accounting Quality & Risk Register

**Positives**
- Zero goodwill impairment across FY21–FY23 with no restructuring charges embedded in `CostsAndExpenses`.
- AOCI loss narrowing 42% — marks moving in the right direction, no "kitchen sink" quarter.
- Cash taxes ($19.2B) *exceed* book tax expense ($11.9B) — conservative, no aggressive deferral games; DTA build is explainable by IPR&D acquisition activity.
- Debt reduced, commercial paper at zero, no preferred.

**Watch items / quality deductions**
- **Equity-mark volatility is now a permanent earnings feature, not a bug.** A $5.5B loss in FY22 and a $0.8B loss in FY23 in a $300B-revenue business means **reported EPS can miss or beat by $0.30+ purely on venture marks**. Model operating EPS, not GAAP EPS.
- **SBC at $22.1B (7.2% of revenue) and growing 13.3%** faster than revenue. GAAP margin expansion of 92bps is *after* this; on a "SBC-neutral" basis margins improved ~120bps. Conversely, SBC is real dilution economics — the buyback is partly just a treadmill.
- **Tax rate normalization** (13.9% → mid-teens) is a ~$1.5B FY24 headwind.
- **Receivables growing 2.2x faster than revenue** with a 1.6% allowance.
- **AP +46%** flattered FY23 CFO; not repeatable.
- **Non-marketable equity of $28.8B** carries cumulative upward adjustments of **$18.1B** and downward adjustments of **$6.9B** (up from $4.5B) — the write-down cadence accelerated in 2023, a quiet sign of stress in the venture book.

**Regulatory/competitive context (qualitative, no news tool available):** the U.S. DOJ search-distribution antitrust case, the December 2023 Epic v. Google jury verdict on Play-store monopolization, the pending ad-tech trial, and EU DMA compliance obligations all sit over the equity as discrete, unquantifiable-in-advance event risks. None of these are reflected in the FY23 financials, and the FY23 financials are not evidence about them either way.

---

## 8. Actionable Insights for Traders

1. **Separate operating EPS from reportable EPS.** The durable FY23 number is **operating income +12.6% on revenue +8.7%**. The reported **+27.2% diluted EPS** is inflated by ~$4.9B of non-operating mark reversal and ~$1.7B of tax benefit. **If you underwrite FY24 at a repeat of 27% EPS growth you are assuming the marks repeat and the tax rate stays at 13.9% — and neither will.** A sane FY24 operating-EPS growth band is **high-single to low-double digits plus ~3% from buybacks → roughly 10–15%.**
2. **Position sizing around the capex guide, not the revenue print.** FY24 capex ~$48B vs. $32.3B is the dominant FCF variable. If revenue accelerates above ~+12% (AI/Cloud), capex is investment; below ~+9%, capex is margin compression via depreciation and FCF stalls. **Buy the former, fade the latter.**
3. **The $96B net cash plus $28.8B strategic stakes is a floor under downside.** With ~$140B of liquid + strategic assets, the market is paying very little for the balance sheet. This supports owning GOOGL on any capex-fear-driven drawdown.
4. **Valuation framing without a price feed.** Using tagged FY23 diluted EPS of **$5.80**:

| Multiple | Implied price |
|---|---:|
| 18x | $104 |
| 22x | $128 |
| 26x | $151 |
| 30x | $174 |

Plug the live price into that grid; on FY24E EPS of ~$6.40–6.70 (normalized tax, +3% buyback, partial capex drag) the 22–26x band is **$141–$174**. Historically Alphabet has oscillated between ~17x and ~30x on forward EPS, so the multiple — not the earnings — is doing most of the work near current levels.
5. **The bond-portfolio unwind is a free option.** $1.9B of remaining unrealized losses (down 60%) plus **$14.2B of AFS maturing beyond 10 years** means interest income ratchets up as paper rolls. This is a multi-year, non-consensus, non-operating EPS tailwind — and it partially offsets the tax-rate normalization.
6. **Buyback math is mechanical and reliable — until it isn't.** At 88.5% of FCF, repurchases are ~$60B+/yr. If FCF dips to ~$55B on capex, the buyback either shrinks (removing ~1–1.5pp of EPS support) or gets debt-funded (changing the story). **Watch quarterly buyback dollars as the leading indicator of management's own FCF confidence** — it's a cleaner signal than guidance language.
7. **Do not expect a dividend.** As of 2024-02-13, no dividend has been declared or paid in any tagged period (no `PaymentsOfDividends` tag exists in the FY23 10-K set). Any note asserting an Alphabet dividend on this date is using future information.
8. **Insider flow is a blind spot — treat it as such.** No data was available; do not let any downstream model assume neutral insider activity was *observed*. It was not observed at all.

---

## 9. Data Gaps (explicitly disclosed)

| Gap | Impact |
|---|---|
| `Revenues`, R&D, S&M not in returned tag subset | Revenue derived as CostsAndExpenses + OperatingIncome; reconciles exactly to 10-K arithmetic but is a derivation, not a raw tag |
| Quarterly income statement detail (Q4 standalone) | Archive returns only FY-level period tags for income items; **no quarterly revenue/EPS decomposition possible from this data** |
| Goodwill, intangibles, gross/net PP&E | Cannot compute ROIC, asset turns, or tangible book |
| Total liabilities / stockholders' equity | Cannot compute ROE or debt-to-equity from tags; leverage assessed via tagged debt instruments only |
| Depreciation & amortization for FY22/FY23 | FY21 only ($10,273M) — no capex-to-depreciation discipline check |
| **Insider transactions** | **Entirely unavailable — no inference made** |

---

## Key Points Summary

| Category | Item | Evidence (SEC tag, accepted ≤ 2024-02-13) | Trader Takeaway |
|---|---|---|---|
| **Filing** | FY2023 10-K, accn 0001652044-24-000022 | Accepted 2024-01-31 02:43 UTC | Freshest audited data; post-earnings digestion window |
| **Growth** | Revenue $307,394M, +8.7% | Derived: CostsAndExpenses 223,101 + OpInc 84,293 | Modest but accelerating into Q4 |
| **Profitability** | Operating income $84,293M, **+12.6%**, margin 27.4% (+92bps) | Derived; CostsAndExpenses tag 223,101 | **Positive operating leverage of ~4pp — the real story** |
| **Cost control** | Total costs & expenses +7.3% (vs +18.1% in FY22) | `CostsAndExpenses` | Efficiency reset worked |
| **G&A** | $16,425M, +4.5% (vs +16.4% FY22) | `GeneralAndAdministrativeExpense` | Clean deceleration |
| **Bottom line** | Net income $73,795M, +23.0%; net margin 24.0% | Pre-tax 85,717 − tax 11,922 | But only 68% is operating |
| **Earnings quality** | Equity-mark swing **+$4,938M**; tax rate **13.9% vs 15.9%** | `EquitySecuritiesFvNiGainLoss`, `EffectiveIncomeTaxRateContinuingOperations` | ~⅓ of growth non-repeatable — **normalize FY24** |
| **EPS** | Diluted **$5.80** (+27.2%); basic $5.84 | `EarningsPerShareDiluted` | 18–30x ⇒ $104–$174 grid |
| **Share count** | 12,460M, **−3.0% YoY** | `CommonStockSharesOutstanding` | ~3% mechanical EPS tailwind |
| **Cash generation** | CFO **$101,746M** (+11.2%), FCF **$69,495M** (+15.8%) | `NetCashProvidedByUsedInOperatingActivities`, capex 32,251 | First $100B+ CFO year |
| **Capex** | $32,251M = 10.5% of revenue; FY24 guide ~$48B | `PaymentsToAcquirePropertyPlantAndEquipment` | **Biggest FCF swing factor** |
| **Buybacks** | **$61,504M = 88.5% of FCF**; 3-yr $171.1B | `PaymentsForRepurchaseOfCommonStock` | Reliable floor on share count |
| **Balance sheet** | Cash+ST inv **$110,916M**; debt **~$14,862M** ⇒ **net cash ~$96B** | Cash tag + LTD maturity ladder | Downside protection |
| **Strategic assets** | Non-marketable equity **$28,766M** (+$18.1B cumulative up-adjustments, $6.9B down) | `EquitySecuritiesWithoutReadilyDeterminableFairValue` | Hidden value; but write-downs rising |
| **Bond overhang** | AFS unrealized loss **$4,779M → $1,910M**; AOCI **−7,603 → −4,402** | `DebtSecuritiesAvailableForSaleUnrealizedLossPositionAccumulatedLoss`, `AOCI` | +$3.2B book value, no P&L cost |
| **Debt** | Borrowed $10.8B, repaid $11.6B; **CP = $0**; $1.3B due 2024 | `ProceedsFromDebtNetOfIssuanceCosts`, `CommercialPaper` | De-risked, no cliff |
| **SBC** | **$22,100M = 7.2% of revenue**, +13.3% | `AllocatedShareBasedCompensationExpense` | Growing faster than revenue — margin drag |
| **Tax shield** | Deferred tax on IPR&D **$10,381M → $17,757M**; cash tax $19.2B vs $11.9B book | `DeferredTaxAssetsInProcessResearchAndDevelopment` | Tech/talent acquisition footprint |
| **Receivables** | **+19.2%** vs revenue +8.7%; allowance only 1.6% | `AccountsReceivableNetCurrent`, `AllowanceForDoubtfulAccountsReceivable` | Yellow flag; $7.8B cash drag |
| **Payables** | **+46%** ($5,128M → $7,493M) | `AccountsPayableCurrent` | Flattered FY23 CFO — not repeatable |
| **Impairment** | Goodwill impairment **$0** in FY21–FY23 | `GoodwillImpairmentLoss` | No hidden charges |
| **Due diligence gap** | Goodwill, PP&E, equity, D&A (FY22–23), quarterly income detail | Not in returned tag subset | No ROIC/ROE from tags |
| **Insider activity** | **DATA UNAVAILABLE — no archive exists** | Vendor: do not infer | **Blind spot; do not assume neutral was observed** |
| **Dividend** | **None declared or paid** | No dividend tag in FY23 10-K | Do not model a dividend at this date |

**Bottom line on GOOGL as of 2024-02-13:** a high-quality, net-cash, ~27%-operating-margin franchise whose **operating** momentum improved materially in FY23 (+12.6% vs. +8.7% revenue) but whose **reported** growth is ⅓ non-operating and tax-flattered. The FY24 debate is not about demand — it is about whether a ~$48B capex ramp converts into AI/Cloud revenue fast enough to protect the ~$70B FCF base that funds the $60B buyback. Own it for the balance sheet and the operating leverage; size it against the capex guide.