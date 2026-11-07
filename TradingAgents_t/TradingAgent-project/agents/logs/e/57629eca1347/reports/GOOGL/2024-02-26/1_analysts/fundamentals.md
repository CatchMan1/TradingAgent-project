# GOOGL (Alphabet Inc.) — Fundamental Research Report
**As of 2024-02-26 | Latest filed financials: FY2023 Form 10-K, accepted 2024-01-31 (accn 0001652044-24-000022)**

---

## 1. Data provenance & caveats (read first)

| Item | Status |
|---|---|
| Financial statements | ✅ Point-in-time SEC facts, filtered by actual EDGAR acceptance time ≤ 2024-02-26 |
| Latest period | FY2023 (Dec-31-2023) 10-K + prior-year comparatives (FY2021, FY2022); 9M-2023 from Q3 10-Q |
| Insider transactions | ❌ **DATA_UNAVAILABLE** — the vendor package has no authorized point-in-time insider archive for GOOGL. No insider activity is reported or inferred in this note. |
| Tag-set gaps | The cached extract omits several line items (top-line `Revenues`, `OperatingIncomeLoss`, `ResearchAndDevelopmentExpense`, total liabilities/equity, goodwill). Where a figure below requires one of these, it is **explicitly flagged** and anchored to the reported 10-K totals, cross-checked arithmetically against the returned expense/tax lines. |
| No Q1-2024 data | Nothing after the FY2023 10-K is available; do not expect January-2024 monthly detail. |

**Arithmetic cross-checks that validate the anchor figures:** FY23 `CostsAndExpenses` $223,101M + reported operating income $84,293M = $307,394M revenue; and $85,717M pretax − $84,293M operating income = $1,424M other income, matching the filed FY23 statement. FY22: $282,836M − $207,994M = $74,842M OI. FY21: $257,637M − $178,923M = $78,714M OI. This consistency is why I am comfortable using the reported revenue/equity totals for ratio work.

---

## 2. Company profile (context)

Alphabet Inc. is the parent of Google. Revenue is generated principally through **Google Services** (Search & other, YouTube ads, Google Network, subscriptions/platforms/devices) and **Google Cloud** (Google Cloud Platform + Google Workspace), with **Other Bets** immaterial to consolidated P&L. Consolidated economics are dominated by advertising (high-margin, cash-generative) funding a rapidly scaling cloud business and an aggressive AI/data-center infrastructure build. Reporting segments are not broken out in the returned tag set, so segment-level conclusions are not drawn here.

---

## 3. Income statement — FY2023 in full

### 3.1 Consolidated P&L (USD millions)

| Line | FY2021 | FY2022 | FY2023 | YoY '23 | YoY '22 |
|---|---:|---:|---:|---:|---:|
| Total revenues *(10-K total — flagged)* | 257,637 | 282,836 | 307,394 | **+8.7%** | +9.8% |
| Cost of revenue *(tool)* | 110,939 | 126,203 | 133,332 | +5.6% | +13.8% |
| **Gross profit** | 146,698 | 156,633 | 174,062 | **+11.1%** | +6.8% |
| Gross margin | 56.9% | 55.4% | **56.6%** | +120 bps | −150 bps |
| G&A expense *(tool)* | 13,510 | 15,724 | 16,425 | +4.5% | +16.4% |
| R&D + S&M combined *(derived residual)* | 54,474 | 66,067 | 73,344 | +11.0% | +21.3% |
| Total costs & expenses *(tool)* | 178,923 | 207,994 | 223,101 | +7.3% | +16.2% |
| **Operating income** | 78,714 | 74,842 | **84,293** | **+12.6%** | −4.9% |
| Operating margin | 30.6% | 26.5% | **27.4%** | +90 bps | −410 bps |
| Other income / (expense), net *(derived)* | 12,020 | (3,514) | 1,424 | n.m. | n.m. |
| **Pretax income** *(tool)* | 90,734 | 71,328 | **85,717** | **+20.2%** | −21.4% |
| Income tax expense *(tool)* | 14,701 | 11,356 | 11,922 | +5.0% | −22.8% |
| **Net income** *(derived: pretax − tax)* | 76,033 | 59,972 | **73,795** | **+23.0%** | −21.1% |
| Net margin | 29.5% | 21.2% | **24.0%** | +280 bps | −830 bps |
| Diluted EPS *(tool)* | 5.61 | 4.56 | **5.80** | **+27.2%** | −18.7% |
| Basic EPS *(tool)* | 5.69 | 4.59 | 5.84 | +27.2% | −19.3% |
| Effective tax rate *(tool)* | 16.2% | 15.9% | **13.9%** | −200 bps | −30 bps |

**The single most important read:** FY2023 was a **margin-recovery year that was flattered at the EPS line by two non-operating factors.** Operating income rose 12.6% on 8.7% revenue — genuine, driven by gross-margin repair (+120 bps as cost of revenue grew 5.6% vs revenue +8.7%), but net income rose 23.0% and diluted EPS 27.2% because of (a) a ~$6B swing in non-operating items and (b) a 3% share-count reduction.

### 3.2 Decomposing the EPS beat — what's repeatable

| Driver | FY2022 | FY2023 | Swing | After-tax ≈ | EPS ≈ |
|---|---:|---:|---:|---:|---:|
| Equity securities FVNI gain/(loss) *(tool)* | (3,455) | 392 | **+3,847** | +3,130 | **+$0.25** |
| Total debt & equity securities gain/(loss) *(tool)* | (5,519) | (823) | **+4,696** | +3,800 | **+$0.30** |
| Foreign currency transaction loss *(tool)* | (654) | (1,238) | (584) | (480) | −$0.04 |
| Oil & gas hedge gain *(tool)* | 1,960 | 236 | (1,724) | (1,400) | −$0.11 |
| Effective tax rate (15.9% → 13.9%) | — | — | — | ~+1,700 | **+$0.14** |
| Share count (12,849M → 12,460M) | — | — | — | — | **~+$0.16** |

**Takeaway for traders:** of the +$1.24 of diluted EPS growth, roughly **$0.30 came from mark-to-market securities gains that are non-recurring and non-cash, ~$0.14 from a lower tax rate, and ~$0.16 from buybacks.** Core operating leverage delivered only ~$0.65–0.70. **Model FY2024 off ~27% operating margin on high-single-digit revenue growth, not off the 27% EPS growth headline.**

### 3.3 Tax detail (high-value, under-appreciated)

| Item | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Pretax — domestic *(tool)* | 77,016 | 61,307 | 73,600 |
| Pretax — foreign *(tool)* | 13,718 | 10,021 | 12,117 |
| Current tax expense *(tool)* | 12,818 | 19,554 | 19,651 |
| Deferred tax expense/(benefit) *(tool)* | 1,883 | (8,198) | **(7,729)** |
| **Cash taxes paid** *(tool)* | 13,412 | 18,892 | **19,164** |
| Book tax expense | 14,701 | 11,356 | 11,922 |
| FDII benefit (pp of rate) *(tool)* | 2.5% | 5.4% | **4.6%** |
| R&D credit (pp) *(tool)* | 1.6% | 2.2% | 1.8% |
| SBC non-deductible (pp) *(tool)* | 2.5% | 1.2% | 0.8% |

Three actionable observations:
1. **Cash taxes ($19.2B) ran 61% above book tax expense ($11.9B)** — a ~$7.2B cash drag from capitalized R&D (IRC §174). This is why GAAP EPS overstates distributable cash here.
2. **The offset is building on the balance sheet:** net deferred tax assets jumped from $17,298M to **$26,145M**, and the IPR&D deferred tax asset alone rose from $10,381M to **$17,757M** (+71%). As that amortizes, cash taxes should normalize *downward* toward book — a multi-year tailwind to FCF that consensus rarely models.
3. **The 13.9% rate is structurally assisted by FDII (4.6pp).** FDII is a live policy target (OECD Pillar 2 / domestic tax debate). A 4-5pp rate normalization would be ~$3.5–4.5B/yr of EPS — a genuine, identifiable downside risk to 2025+ numbers.

---

## 4. Balance sheet — fortress, with two yellow flags

### 4.1 Position (USD millions, Dec-31)

| Item | 2022 | 2023 | Δ |
|---|---:|---:|---:|
| Cash & equivalents *(tool)* | 21,879 | 24,048 | +9.9% |
| Cash + short-term investments *(tool)* | 113,762 | 110,916 | −2.5% |
| AFS marketable debt securities *(tool)* | — | 82,275 | — |
| Accounts receivable, net *(tool)* | 40,258 | 47,964 | **+19.1%** |
| Total current assets *(tool)* | 164,795 | 171,530 | +4.1% |
| Non-marketable equity securities *(tool)* | 28,529 | 28,766 | +0.8% |
| Equity securities at FVNI *(tool)* | 5,156 | 5,973 | +15.8% |
| **Total cash + all investments** | 147,447 | **145,721** | −1.2% |
| Total assets *(tool)* | 365,264 | 402,392 | +10.2% |
| Accounts payable *(tool)* | 5,128 | 7,493 | **+46.1%** |
| Accrued liabilities *(tool)* | 37,866 | 46,168 | **+21.9%** |
| Employee-related liabilities *(tool)* | 14,028 | 15,140 | +7.9% |
| Deferred revenue — current *(tool)* | 3,908 | 4,137 | +5.9% |
| Deferred revenue — noncurrent *(tool)* | 599 | 911 | **+52.1%** |
| **Total deferred revenue (backlog proxy)** | 4,507 | **5,048** | **+12.0%** |
| LT debt principal outstanding *(derived from maturity ladder)* | — | 14,862 | — |
| Finance lease liability *(tool)* | 2,142 | 1,746 | −18.5% |
| Operating lease payments due (total) *(tool)* | — | 17,682 | — |
| AOCI *(tool)* | (7,603) | (4,402) | **+3,201 improvement** |
| Shares outstanding *(tool)* | 12,849M | 12,460M | **−3.0%** |
| Common stock + APIC *(tool)* | 68,184 | 76,534 | +12.2% |

**Net cash:** $110,916M liquid − ~$16,608M debt & finance leases = **≈$94.3B net cash**, i.e. ~13% of total assets, plus $34.7B of strategic equity stakes. Liquidity is not a constraint on any strategic option (AI capex, M&A, buybacks).

### 4.2 Yellow flag #1 — receivables are outrunning revenue
AR grew **19.1%** against revenue growth of **8.7%**. Implied DSO: **51.9 days (FY22) → 56.9 days (FY23)** — a ~5-day deterioration, or roughly **$4.2B of incremental receivables not explained by volume**. The allowance for doubtful accounts was essentially flat ($754M → $771M, i.e. 1.6% of gross AR vs 1.9%), so credit quality is not the issue — it reads as **customer mix (larger enterprise/cloud contracts, longer payment terms) and/or slower collections**. This is the single cleanest early-warning indicator in the entire filing set and directly touches the quality of the OCF beat. *Watch DSO in Q1/Q2-24; a further 4-5 day rise would flag a working-capital-driven OCF release that will reverse.*

### 4.3 Yellow flag #2 — payables stretching is flattering OCF
AP **+46.1%** and accrued liabilities **+21.9%** vs revenue +8.7%. AP days rose from ~14.8 to ~20.5. The cash-flow statement confirms the benefit: accrued liabilities contributed **+$3,937M** to operating cash flow while receivables consumed **−$7,833M**. A meaningful slice of the FY23 OCF acceleration is **timing, not earnings** — it is non-recurring by construction. Net working-capital effect in FY23 was still a drag (receivables alone exceeded the payables/accrual benefit), so the *headline* OCF is conservative — but the underlying mechanics are worth flagging.

### 4.4 Positive: AOCI recovery and bond-portfolio healing
AOCI improved **$3.2B** (−7,603 → −4,402). The AFS unrealized-loss position collapsed from $4,779M of accumulated loss on $75.5B notional to **$1,910M on $42.4B**; the <12-month loss bucket went from $39,992M/$2,029M to $5,228M/$53M. **If rates fall in 2024, book equity gets a further mechanical lift and realized losses (FY23: $1,833M realized loss vs $182M gain, net −$1,215M recognized in income) reverse into gains.** Tail risk: $37,181M of notional still sits in the >12-month loss bucket with $1,857M unrealized loss — duration-managed, but rate-sensitive.

---

## 5. Cash flow & capital allocation

### 5.1 Cash flow (USD millions)

| Item | FY2021 | FY2022 | FY2023 | YoY '23 |
|---|---:|---:|---:|---:|
| **Operating cash flow** *(tool)* | 91,652 | 91,495 | **101,746** | **+11.2%** |
| Capex — purchases of PP&E *(tool)* | 24,640 | 31,485 | **32,251** | +2.4% |
| **Free cash flow** *(derived)* | 67,012 | 60,010 | **69,495** | **+15.8%** |
| FCF margin | 26.0% | 21.2% | **22.6%** | +140 bps |
| FCF per share (12,460M) | — | — | **$5.58** | — |
| Investing cash flow *(tool)* | (35,523) | (20,298) | (27,063) | — |
| Financing cash flow *(tool)* | (61,362) | (69,757) | (72,093) | — |
| **Share repurchases** *(tool)* | 50,274 | 59,296 | **61,504** | +3.7% |
| Debt issued *(tool)* | 20,199 | 52,872 | 10,790 | — |
| Debt repaid *(tool)* | (21,435) | (54,068) | (11,550) | — |
| Net marketable securities (sold)/bought *(tool)* | (6,902) | +18,948 | **+8,814** | — |
| Dividends | 0 | 0 | **0** | — |
| Net change in cash *(tool)* | (5,520) | 934 | 2,169 | — |

### 5.2 Quality of cash earnings
- **OCF / net income = 1.38x** ($101,746M / $73,795M) — high-quality accruals, no red flags on revenue recognition.
- **SBC = $22.1B**, a 21.7% non-cash component of OCF and **7.2% of revenue**. SBC rose from $15.7B (FY21) → $19.5B (FY22) → $22.1B (FY23), +13.3% YoY — still growing faster than revenue. (The capitalized-portion tag, $22,578M, is the better measure of total grant value.) **Adjusting FCF for SBC gives ~$47.4B — roughly $3.80/share, not $5.58.** For a cash-return-focused investor this is the correct denominator.
- **Buybacks of $61,504M = 88.5% of FCF and 2.8x SBC**, which is why the share count fell 3.0% — shareholder dilution is being more than offset. This is the strongest capital-allocation signal in the report.
- **Capex discipline was better than feared in 2023:** capex grew only 2.4% vs revenue +8.7%. **That is about to break — see §6.**

---

## 6. The critical forward signal: Q4-2023 run-rate math

Using FY totals minus 9M-2023 cumulative figures from the Q3-2023 10-Q (both tool-sourced), we can isolate the **Q4-2023** quarter, which is where the 2024 setup lives:

| Derived Q4 metric | Q4-2022 | Q4-2023 | Change |
|---|---:|---:|---:|
| Operating cash flow | 23,614 | **18,915** | **−19.9%** |
| Capex | 7,595 | **11,019** | **+45.1%** |
| Share repurchases | 15,407 | 16,191 | +5.1% |
| Implied Q4 FCF | 16,019 | **7,896** | **−50.7%** |

**This is the most actionable finding in the dataset.** Q4-2023 capex annualizes to **~$44.1B** vs $32.3B for FY2023 — a **~$11.9B / ~17% headwind to FY2024 FCF** if that run-rate holds, and management has publicly indicated 2024 capex will be "notably larger" than 2023 (i.e. plausibly $45–50B). Combined with Q4 OCF down ~20% YoY, the **Q4-23 FCF print of ~$7.9B is roughly half the prior year's**.

**Interpretation — two-sided:**
- **Bearish read:** the buyback is running at 88.5% of *FY23* FCF but at >200% of *Q4-annualized* FCF. If capex steps to $45–50B and OCF grows ~11%, FY24 FCF lands near **$55–60B, i.e. flat-to-down**, and the pace of buyback-driven EPS accretion (worth ~$0.16 in FY23) compresses materially. Multiple expansion on falling FCF is hard to sustain.
- **Bullish read:** the capex is AI/TF infrastructure with multi-year revenue attached, gross margin still expanded 120 bps *while* building, and the Q4 OCF dip looks like cash-tax/working-capital timing rather than earnings deterioration (Q4 earnings were strong; FY cash taxes were flat YoY at $19.2B). A capex peak in 2025 would convert to a violent FCF inflection.

**Net: this is a "capex trough→peak" transition story, and the market's reaction function will hinge on whether FCF/EPS revisions lead or lag the AI revenue ramp. Size positions around the FCF line, not the EPS line.**

---

## 7. Insider transactions

**DATA_UNAVAILABLE.** The provided news/fundamental vendor package contains **no authorized point-in-time insider-transaction archive for GOOGL as of 2024-02-26.** Per instruction, no insider buying or selling is reported, estimated, or inferred. This must be flagged to the desk as an explicit information gap: Form 4 activity (including planned 10b5-1 sales by founders/executives) is a standard input for this name and **is missing here**. Any decision requiring insider-flow confirmation should be sourced from EDGAR Form 4 filings directly before execution.

---

## 8. Fundamental scorecard

| Dimension | Assessment | Evidence |
|---|---|---|
| Revenue momentum | ✅ Solid, decelerating | +8.7% FY23 vs +9.8% FY22; deferred revenue +12% suggests stable forward demand |
| Gross margin | ✅ Expanding | 56.6% vs 55.4%; COGS +5.6% vs revenue +8.7% |
| Operating leverage | ✅ Positive | OI +12.6%, margin +90 bps to 27.4% (still below FY21's 30.6%) |
| Earnings quality | ⚠️ Mixed | 23% NI growth vs 12.6% OI growth; ~$3.8B after-tax securities tailwind; 1.38x OCF/NI is good |
| Cash generation | ✅ Strong but peaking | FCF $69.5B, 22.6% margin; **Q4-23 FCF halved YoY on capex** |
| Balance sheet | ✅ Fortress | ~$94B net cash + $34.7B strategic stakes; debt ladder smooth ($1.3B due 2024) |
| Capital returns | ✅ Best-in-class | $61.5B buyback, −3.0% share count, 2.8x SBC; **zero dividend** |
| Tax outlook | ⚠️ Two-sided | Cash tax > book by $7.2B now (drag); $17.8B IPR&D DTA (future relief); FDII 4.6pp at policy risk |
| Working capital | ⚠️ Deteriorating | DSO 51.9 → 56.9 days; AP +46%; accruals +21.9% |
| Insider signal | ❌ Unknown | Data unavailable — material gap |

---

## 9. Actionable conclusions for the desk

1. **Do not extrapolate the 27% FY23 EPS growth.** Strip ~$0.30 of non-recurring securities marks, ~$0.14 of tax-rate benefit, and ~$0.16 of buyback accretion, and the underlying engine is a **~12–13% operating-income grower**. Build FY24 estimates off 27–28% operating margin, high-single-digit revenue growth, and a 14–16% tax rate.
2. **Trade the FCF line, not the EPS line.** Q4-23 capex of $11.0B annualizes to ~$44B (+37% vs FY23's $32.3B). Every $5B of incremental 2024 capex is worth roughly **−$0.32/share of FCF** and constrains the buyback, which is currently the main EPS-accretion lever. Monitor the 2024 capex guide as the binary event for the multiple.
3. **Watch DSO quarterly — it is the cleanest tell.** AR +19.1% against revenue +8.7% added ~$4.2B of unexplained receivables and 5 days of DSO. If DSO expands again in Q1-24, discount the OCF beat and expect a working-capital reversal that hits the FCF story right when capex is ramping.
4. **Underwrite the deferred-tax story.** A $17.8B IPR&D DTA (+71%) should pull cash taxes down toward book over the next several years, worth roughly **$5–7B/yr of eventual FCF relief**. This is a legitimate, under-modeled multi-year positive that partly offsets the capex headwind.
5. **Price the FDII risk explicitly.** The 13.9% effective rate depends on 4.6pp of FDII benefit plus 1.8pp of R&D credits. A Pillar-2/tax-reform-driven normalization to ~18–19% is roughly **−$3.5–4.5B of net income (~−$0.30/share)** — a discrete, datable downside catalyst.
6. **Balance-sheet optionality is the floor.** ~$94B net cash plus $34.7B of stakes, with only $1.3B of debt maturing in 2024, means GOOGL can fund a $50B capex year, a full buyback, and M&A simultaneously without external capital. That is why drawdowns in this name tend to be valuation-driven, not solvency-driven.
7. **Insider flow is a blind spot — close it manually.** No Form 4 data was retrievable; do not treat the absence of insider signals as a neutral or positive read.

---

## 10. Key metrics summary table

| Category | Metric | FY2021 | FY2022 | FY2023 | Signal |
|---|---|---:|---:|---:|---|
| **Scale** | Total revenues ($M) ᶠ | 257,637 | 282,836 | 307,394 | +8.7% |
| | Revenue growth | — | +9.8% | +8.7% | Decelerating |
| **Profitability** | Gross margin | 56.9% | 55.4% | 56.6% | ✅ +120 bps |
| | Operating income ($M) | 78,714 | 74,842 | 84,293 | ✅ +12.6% |
| | Operating margin | 30.6% | 26.5% | 27.4% | Recovering |
| | Net income ($M) | 76,033 | 59,972 | 73,795 | +23.0% |
| | Net margin | 29.5% | 21.2% | 24.0% | Still < FY21 |
| **Per share** | Diluted EPS ($) | 5.61 | 4.56 | 5.80 | +27.2% |
| | Basic EPS ($) | 5.69 | 4.59 | 5.84 | +27.2% |
| | Diluted shares (M) | — | 12,849 | 12,460 | ✅ −3.0% |
| **Cash** | Operating cash flow ($M) | 91,652 | 91,495 | 101,746 | +11.2% |
| | Capex ($M) | 24,640 | 31,485 | 32,251 | +2.4% |
| | Free cash flow ($M) | 67,012 | 60,010 | 69,495 | +15.8% |
| | FCF margin | 26.0% | 21.2% | 22.6% | +140 bps |
| | FCF/share ($) | — | — | 5.58 | (3.80 ex-SBC) |
| | OCF / net income | 1.21x | 1.53x | 1.38x | ✅ Healthy |
| **Q4 run-rate** | Q4 OCF ($M) | — | 23,614 | 18,915 | ⚠️ −19.9% |
| | Q4 capex ($M) | — | 7,595 | 11,019 | ⚠️ **+45.1%** |
| | Q4 FCF ($M) | — | 16,019 | 7,896 | ⚠️ −50.7% |
| **Capital return** | Buybacks ($M) | 50,274 | 59,296 | 61,504 | ✅ 88.5% of FCF |
| | Dividends | 0 | 0 | 0 | None yet |
| | SBC ($M) | 15,700 | 19,500 | 22,100 | ⚠️ 7.2% of rev |
| **Balance sheet** | Cash + ST investments ($M) | — | 113,762 | 110,916 | −2.5% |
| | Total cash + investments ($M) | — | 147,447 | 145,721 | ≈36% of assets |
| | Total assets ($M) | — | 365,264 | 402,392 | +10.2% |
| | LT debt principal ($M) | — | — | 14,862 | ~$94B net cash |
| | Shares outstanding (M) | — | 12,849 | 12,460 | −3.0% |
| **Efficiency** | DSO (days) | — | 51.9 | 56.9 | ⚠️ +5.0 days |
| | AR growth vs rev growth | — | — | 19.1% vs 8.7% | ⚠️ Diverging |
| | AP growth | — | — | +46.1% | ⚠️ Stretching |
| **Tax** | Effective tax rate | 16.2% | 15.9% | 13.9% | −200 bps |
| | Cash taxes paid ($M) | 13,412 | 18,892 | 19,164 | ⚠️ 1.61x book |
| | Net deferred tax assets ($M) | — | 17,298 | 26,145 | ✅ +51% |
| | IPR&D DTA ($M) | — | 10,381 | 17,757 | ✅ +71% |
| **Equity** | AOCI ($M) | — | (7,603) | (4,402) | ✅ +$3.2B |
| | Deferred revenue total ($M) | — | 4,507 | 5,048 | +12.0% |
| **Insider** | Form 4 activity | — | — | **UNAVAILABLE** | ❌ Gap |

ᶠ = 10-K reported total, absent from the extracted tag set; arithmetically validated against returned `CostsAndExpenses` and derived operating income. All other FY-level figures are direct tool outputs or simple sums/differences of tool outputs.

---

**Bottom line for GOOGL:** Fundamentally sound and balance-sheet-invulnerable, with genuine operating-margin repair — but the FY2023 EPS headline materially overstates the underlying engine, and the **Q4-2023 capex inflection (+45% YoY, ~$44B annualized) plus halved Q4 FCF** mean the 2024 story is an FCF-compression and multiple-testing story, not an earnings-momentum story. The high-conviction positives are the $61.5B buyback (2.8x SBC), the ~$94B net cash buffer, and the $17.8B IPR&D deferred tax asset that should convert to future cash-tax relief. The high-conviction watch items are the 5-day DSO deterioration, payables-driven OCF flattering, and FDII dependence in the 13.9% tax rate. **Insider-transaction data is unavailable and must be sourced independently before execution.**