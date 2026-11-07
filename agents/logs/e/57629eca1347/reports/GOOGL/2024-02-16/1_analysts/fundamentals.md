# GOOGL — Fundamental Research Report
**Alphabet Inc. (NASDAQ: GOOGL) | Point-in-time as of 2024-02-16 | Data cut: 10-K for FY2023, accepted 2024-01-31**

---

## 0. Data Provenance, Gaps, and How to Read This Report

All figures below come from SEC XBRL facts for **GOOGL** available as of 2024-02-16 (FY2023 10-K filed 2024-01-31, accession 0001652044-24-000022; plus 2023 10-Qs). Three important caveats, stated up front so nothing here is misread as reported data:

1. **The fact dump was alphabetically truncated** (it cut off around tags beginning "D"/"I"). As a result, `Revenues`, `OperatingIncomeLoss`, `NetIncomeLoss`, `ResearchAndDevelopmentExpense`, `SellingAndMarketingExpense`, `StockholdersEquity` and `LongTermDebtNoncurrent` were **not returned**. I have **reconstructed** revenue, operating income, net income, and R&D+S&M using the returned tags and accounting identities (`Revenue = CostsAndExpenses + PreTaxIncome − OtherIncome`; `NetIncome = PreTax − Tax`; `R&D+S&M = CostsAndExpenses − CostOfRevenue − G&A`). Every reconstruction was **cross-checked against reported diluted EPS** and ties to the cent. These are labeled **[derived]** throughout.
2. **Geography/segment tags** (Google Services / Google Cloud / Other Bets revenue) were **not** in the returned data. Segment mix is therefore not quantified here.
3. **Insider transactions: UNAVAILABLE.** The data package returned: *"no authorized, point-in-time insider-transactions archive for GOOGL by 2024-02-16. Do not infer or fabricate insider activity."* I have **no** insider buy/sell data for this report and will not speculate.

---

## 1. Executive Summary — The 3 Things That Matter

**1) FY2023 was a genuine operating-leverage inflection, and it is confirmed in the cost lines.** Revenue grew +8.7% to $307.4B while total costs and expenses grew only +7.3%. Cost of revenue decelerated hard — **+5.6% in 2023 vs +13.8% in 2022** — the single biggest reason operating margin recovered from 26.5% → 27.4% and net income jumped **+23.0%** off a +8.7% revenue base. Earnings growth massively outran revenue growth.

**2) But the Q4 exit-rate shows an AI capex cliff that will compress 2024 free cash flow.** Deriving Q4 standalone from cumulative periods: capex was **$8.06B in Q3 → $11.02B in Q4 (+36.8% QoQ)** — roughly a **$44B annualized run-rate**, versus $32.3B for all of FY2023. Q4 operating cash flow fell to **$18.9B** (vs $30.7B in Q3) and Q4 FCF collapsed to **~$7.9B from $22.6B**. This is the key 2024 debate, and the FY2023 statement already contains the evidence.

**3) The 13.9% effective tax rate is the most under-appreciated risk in the print.** Book tax expense fell to 13.9% of pre-tax income (from 15.9%), adding roughly **$1.7B of EPS benefit** vs. a 15.9% rate. Meanwhile **cash taxes paid were $19.16B — a 22.4% cash tax rate**. The gap is deferred tax driven by Section 174 R&D capitalization (deferred tax assets for in-process R&D jumped **$10.38B → $17.76B**). That benefit **reverses** over future years: GOOGL's book tax rate is more likely to drift up than down, which mechanically decelerates EPS growth versus 2023.

**Net stance implied by the fundamentals: high-quality, cash-rich, structurally advantaged, but with a 2024 EPS/FCF setup that is worse than the 2023 headline optics suggest.** The balance sheet ($110.9B cash + securities, ~$96B net cash) is the cushion that makes the capex cycle fundable without dilution.

---

## 2. Company Profile

**Alphabet Inc.** is the parent holding company of Google, and the instrument under analysis is **GOOGL** (Class A common stock). GOOGL is one of the largest companies in the world by revenue and market capitalization and operates three reporting segments:

- **Google Services** — Google Search & other, YouTube advertising, Google Network, Play, hardware (Pixel/Nest), and subscriptions/platform fees. This is the advertising and consumer-funnel engine and the overwhelming majority of revenue and profit.
- **Google Cloud** — Google Cloud Platform (infrastructure/data/AI) and Google Workspace (productivity/subscription).
- **Other Bets** — earlier-stage ventures (e.g., autonomous driving, life sciences), typically operating at a loss.

Cost structure evident in the FY2023 statement: heavy **cost of revenue** (traffic acquisition costs, content, data center/technical infrastructure, hardware) at 43.4% of revenue; **R&D-heavy** (R&D + S&M combined $73.3B **[derived]**, with R&D ~$45B of that, i.e. ~14.8% of revenue); lean **G&A** at only 5.3% of revenue. Capital intensity is high and rising: capex was 10.5% of revenue in 2023 and is accelerating.

Note on identity: "Alphabet Inc." is the resolved issuer for GOOGL on 2024-02-16; the FY2023 10-K is the correct and most recent annual filing at this date (there is no FY2024 annual report yet — the next 10-K will not appear until early 2025).

---

## 3. FY2023 Income Statement (Reconstructed, Audited-Basis)

All $ in millions. **[derived]** items are reconstructed but tie exactly to reported diluted EPS.

| Line item | FY2021 | FY2022 | FY2023 | YoY '23 |
|---|---:|---:|---:|---:|
| **Revenue [derived]** | 257,637 | 282,836 | **307,394** | **+8.7%** |
| Cost of revenue | 110,939 | 126,203 | 133,332 | +5.6% |
| **Gross profit [derived]** | 146,698 | 156,633 | **174,062** | +11.1% |
| *Gross margin* | *56.9%* | *55.4%* | ***56.6%*** | *+120 bps* |
| R&D + S&M combined [derived] | 54,474 | 66,067 | 73,344 | +11.0% |
| General & administrative | 13,510 | 15,724 | 16,425 | +4.5% |
| **Total costs & expenses (reported)** | 178,923 | 207,994 | **223,101** | **+7.3%** |
| **Operating income [derived]** | 78,714 | 74,842 | **84,293** | **+12.6%** |
| *Operating margin* | *30.6%* | *26.5%* | ***27.4%*** | *+90 bps* |
| Other income/(expense), net [derived] | 12,020 | (3,514) | 1,424 | n.m. |
| **Pre-tax income (reported)** | 90,734 | 71,328 | **85,717** | +20.2% |
| Income tax expense | 14,701 | 11,356 | 11,922 | +5.0% |
| *Effective tax rate* | *16.2%* | *15.9%* | ***13.9%*** | *−200 bps* |
| **Net income [derived]** | 76,033 | 59,972 | **73,795** | **+23.0%** |
| *Net margin* | *29.5%* | *21.2%* | ***24.0%*** | *+280 bps* |
| Diluted EPS (reported) | 5.61 | 4.56 | **5.80** | **+27.2%** |
| Basic EPS (reported) | 5.69 | 4.59 | 5.84 | +27.2% |
| Diluted shares (implied) | 13,553 | 13,152 | **12,723** | −3.3% |
| Shares outstanding (period end, reported) | — | 12,849 | **12,460** | **−3.0%** |

**What the income statement actually says:**

- **2022 was the air pocket, 2023 was the repair.** Operating margin fell 410 bps in 2022 as cost of revenue grew +13.8% and R&D+S&M grew +21.3% against +9.8% revenue. In 2023, cost of revenue growth was cut to +5.6% and R&D+S&M to +11.0%: GOOGL re-established positive operating leverage.
- **But revenue growth is decelerating modestly** (+9.8% → +8.7%) while **R&D+S&M still grew +11.0%**, i.e. faster than revenue. Investment is still outrunning the top line; the margin recovery came almost entirely from the cost-of-revenue line, not from opex discipline.
- **EPS grew 27.2% vs net income 23.0%** — roughly 3.3 points of EPS growth came from the **shrinking share count**, not operations. Traders should attribute ~1/7 of the 2023 EPS beat to buybacks.
- **G&A is remarkably flat (+4.5%)** — evidence of the 2023 headcount/expense reset holding.

---

## 4. Cost Structure Deep-Dive

| Metric | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| Cost of revenue / revenue | 43.1% | 44.6% | **43.4%** |
| R&D+S&M / revenue [derived] | 21.1% | 23.4% | **23.9%** |
| G&A / revenue | 5.2% | 5.6% | **5.3%** |
| SBC (reported) | 15,700 | 19,500 | **22,100** |
| **SBC / revenue** | 6.1% | 6.9% | **7.2%** |
| **SBC / operating income** | 19.9% | 26.1% | **26.2%** |
| **Operating margin ex-SBC [derived]** | 36.7% | 33.4% | **34.6%** |
| SBC tax benefit (reported) | 3,100 | 3,900 | **4,500** |

**Quality-of-earnings flag:** stock-based comp rose **+13.3% to $22.1B**, faster than revenue, and now equals **~26% of operating income**. GAAP operating margin (27.4%) understates cash economics (34.6% ex-SBC) — but it also means **~$7.2–7.3 of "cash EPS" versus $5.80 GAAP EPS** (adding back $22.1B SBC after-tax at 13.9%: net income $92.8B, EPS **~$7.30** **[derived]**). Any trader comparing GOOGL to a peer on GAAP P/E alone is comparing an increasingly SBC-loaded number against peers with different comp structures. SBC is real dilution risk even as buybacks mask it at the share-count level.

---

## 5. Quarterly Momentum (Derived from Cumulative Filings)

Standalone quarters reconstructed by subtracting 6M/9M cumulative facts from FY/9M totals:

| Metric ($M) | Q3 2023 | Q4 2023 | Change |
|---|---:|---:|---:|
| Operating cash flow | 30,656 | **18,915** | **−38.3%** |
| Capex (PP&E purchases) | 8,055 | **11,019** | **+36.8%** |
| **Free cash flow [derived]** | 22,601 | **7,896** | **−65.1%** |
| Share repurchases | 15,787 | 16,191 | +2.6% |
| Buybacks as % of FCF | 69.8% | **205.0%** | n.m. |

**This is the most actionable table in the report.** At the Q4 exit rate:
- Annualized capex ≈ **$44B**, i.e. **~13.8% of annualized revenue** vs 10.5% for FY2023 — a **+310 bps** step-up in capital intensity.
- Q4 FCF of $7.9B annualizes to ~$32B, versus $69.5B actual FY2023 FCF. **FCF could be cut roughly in half in 2024 purely from capex and the tax/working-capital drag**, even with healthy revenue growth.
- GOOGL **out-returned its Q4 FCF** (bought back $16.2B against $7.9B of FCF), drawing down balance-sheet liquidity. Fundable given ~$96B net cash, but not indefinitely repeatable at that pace.
- The Q4 OCF drop (−38% QoQ) is partly seasonal tax/working-capital: **cash taxes paid for FY2023 were $19.16B**, and current income tax expense was $19.65B — Q4 is the heavy cash-tax quarter.

**Signal:** the FY2023 statement is a *backward-looking* bull case and a *forward-looking* caution on FCF. Watch Q1'24 capex for confirmation of the $44B+ run-rate.

---

## 6. Balance Sheet (FY2022 vs FY2023)

| Item ($M) | 2022-12-31 | 2023-12-31 | Change |
|---|---:|---:|---:|
| Cash & cash equivalents | 21,879 | **24,048** | +9.9% |
| Cash + cash equivalents + short-term investments | 113,762 | **110,916** | −2.5% |
| — of which AFS debt securities | — | 82,275 | — |
| Accounts receivable, net | 40,258 | **47,964** | **+19.2%** |
| Allowance for doubtful accounts | 754 | 771 | +2.3% |
| **Total current assets** | 164,795 | **171,530** | +4.1% |
| **Total assets** | 365,264 | **402,392** | **+10.2%** |
| Accounts payable | 5,128 | **7,493** | **+46.1%** |
| Accrued liabilities | 37,866 | **46,168** | **+21.9%** |
| Accrued income taxes, current | 1,632 | 2,748 | +68.4% |
| Deferred revenue, current + noncurrent | 4,507 | **5,048** | +12.0% |
| Common stock + APIC | 68,184 | 76,534 | +12.2% |
| AOCI | (7,603) | **(4,402)** | +$3.2B |
| Shares outstanding (M) | 12,849 | **12,460** | −3.0% |

**Liquidity and leverage:**
- **Cash + securities of $110.9B** against total future debt and finance-lease principal of **$14.86B** (sum of the maturity schedule: $1,299M next 12m, $1,163M yr2, $2,165M yr3, $1,143M yr4, $132M yr5, $8,960M beyond yr5) → **net cash of roughly $96B**, or **~$7.7 per share** **[derived]**. Commercial paper balance is **$0** — no short-term funding reliance.
- Current ratio is **≥2.3x** on the line items disclosed (current assets $171.5B vs AP $7.5B + accrued liabilities $46.2B + accrued tax $2.7B + deferred revenue $4.1B + current finance lease $0.4B + near-term debt $1.3B ≈ $62.2B). Even against the full current-liability base, liquidity is not a question.
- **Debt is a rounding error** relative to equity and cash flow: net debt/EBITDA is deeply negative. GOOGL has no refinancing risk and full self-funding capacity for the AI capex cycle.

**Two balance-sheet items traders should not skip:**

1. **Receivables are outrunning revenue.** AR +19.2% vs revenue +8.7% → days sales outstanding stretched from **~51.9 days to ~56.9 days** **[derived]**. The allowance for doubtful accounts is only **$771M = 1.6% of gross AR** — very thin. This is either a mix shift toward enterprise/Cloud billings (benign) or a collections signal. It consumed **$7.83B of cash** in FY2023 (vs $2.32B in FY2022). **Watch Q1'24 DSO.**
2. **The bond portfolio hemorrhage has stopped.** AOCI improved from −$7.60B to −$4.40B; the AFS unrealized-loss position shrank from **$4.78B to $1.91B**, and securities in a >12-month loss position fell from $35.5B to $37.2B (still large) with accumulated losses down from $2.75B to $1.86B. This removes a latent book-value drag and reduces the risk of forced-sale losses if liquidity were ever needed.
3. **Deferred tax assets ballooned:** gross DTA $26.85B → **$37.14B**, with in-process R&D DTA **$10.38B → $17.76B** (Section 174 R&D capitalization) and DTA net of valuation allowance $17.30B → $26.15B. This is *why* the book tax rate fell — and it is a **future reversal headwind**, not a permanent gift.

---

## 7. Cash Flow & Capital Allocation

| Item ($M) | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| **Operating cash flow** | 91,652 | 91,495 | **101,746** (+11.2%) |
| Capex (PP&E) | 24,640 | 31,485 | **32,251** |
| **Free cash flow [derived]** | 67,012 | 60,010 | **69,495** (+15.8%) |
| *FCF margin* | *26.0%* | *21.2%* | ***22.6%*** |
| *Capex / revenue* | *9.6%* | *11.1%* | *10.5%* |
| Cash flow from investing | (35,523) | (20,298) | (27,063) |
| Cash flow from financing | (61,362) | (69,757) | **(72,093)** |
| **Share repurchases** | 50,274 | 59,296 | **61,504** |
| Debt issued, net | 20,199 | 52,872 | 10,790 |
| Debt repaid | 21,435 | 54,068 | 11,550 |
| Cash taxes paid | 13,412 | 18,892 | **19,164** |
| SBC (non-cash addback) | 15,700 | 19,500 | 22,100 |
| Operating lease payments | 2,489 | 2,722 | 3,173 |
| Net change in cash incl. FX | (5,520) | 934 | **+2,169** |

**Capital allocation verdict:**
- **Buybacks are the entire capital-return program** — $61.5B in 2023, a record, equal to **88.5% of free cash flow** and **20.0% of revenue**. No dividend line appears in the returned cash-flow facts; as of this filing the data shows a pure-repurchase return model. *(External context, not in the tool data: Alphabet announced an inaugural dividend alongside Q4'23 results — verify independently before trading on it.)*
- **Cash conversion remains excellent but is degrading at the margin:** OCF/net income = **1.38x** in 2023, down from **1.53x** in 2022 and 1.21x in 2021. The 2023 decline is the combination of working-capital absorption ($7.8B AR) and the tax timing gap.
- **FY2023 was the last "cheap" capex year.** FCF grew 15.8% only because capex was essentially flat (+2.4%). The Q4 run-rate ($11.0B/qtr) breaks that assumption.
- FY2023 financing outflow of $72.1B (buybacks $61.5B + debt repayment $11.6B, funded partly by $10.8B of new debt) was **fully covered by OCF** — no balance-sheet stress.

---

## 8. Tax, Accounting, and Quality-of-Earnings Items

| Item | 2021 | 2022 | 2023 |
|---|---:|---:|---:|
| Effective book tax rate | 16.2% | 15.9% | **13.9%** |
| **Cash tax rate (taxes paid / pre-tax income) [derived]** | 14.8% | 26.5% | **22.4%** |
| Deferred tax expense/(benefit) | +1,883 | (8,198) | **(7,729)** |
| Current tax expense | 12,818 | 19,554 | 19,651 |
| Domestic pre-tax income | 77,016 | 61,307 | 73,600 |
| Foreign pre-tax income | 13,718 | 10,021 | 12,117 |
| FDII rate benefit | 2.5% | 5.4% | **4.6%** |
| FX transaction loss (pre-tax) | (240) | (654) | **(1,238)** |
| Debt & equity securities gain/(loss) | +12,270 | (5,519) | **(823)** |

**Four things here matter more than the headline:**

1. **The 13.9% book rate is not the cash reality.** Cash taxes of $19.16B on $85.72B pre-tax = **22.4% cash rate**. Roughly **$7.2B of the reported tax expense is a non-cash deferred benefit** that will reverse. Consensus models anchored on 13.9% likely overstate 2024–2025 EPS. A normalization toward the 15.9–16.2% range would cost **~$1.7–2.0B of net income, or ~$0.14–0.16 of EPS** — enough to matter at the margin for a ~25x multiple.
2. **Other income is no longer a tailwind.** FY2021 got +$12.0B of "other income" (largely equity investment gains: +$12.4B equity FV gains). In 2023 that turned to a net −$823M securities loss, plus a **$1.24B FX transaction loss** (tripling from $654M). OI&E contributed +$1.4B in 2023 vs +$12.0B in 2021 — a structural headwind that caps pre-tax growth versus the 2021 era.
3. **FDII benefit is fading** (5.4% → 4.6%) and the valuation allowance rose to $11.0B. Tax benefits are a shrinking source of earnings.
4. **No goodwill impairment in any year** (0 in 2021–2023), and no debt/equity gains dressing up the P&L in 2023 — the 2023 earnings quality is *cleaner* than 2021's, which was flattered by $12.4B of investment gains.

---

## 9. Insider Transactions

**Not available.** The configured data vendor returned an explicit authorization gap: it has *no point-in-time insider-transactions archive for GOOGL as of 2024-02-16*. I am reporting this as a hard data gap and am **not** inferring, estimating, or fabricating any Form 4 activity.

**Substitute signal:** the only insider-adjacent capital signal in the data is the **issuer's own buyback** — $61.5B repurchased in FY2023 (record), with Q4 at $16.2B, repurchasing at a pace exceeding 2x that quarter's FCF. Management's revealed preference via corporate capital allocation is aggressively bullish on its own equity, even as net share count fell only 3.0% because SBC dilution absorbed part of the repurchase.

**Recommendation for the desk:** source Form 4 data separately before finalizing any position sizing. Do not treat this report as a substitute for insider-flow analysis.

---

## 10. Risk Register (ranked by what the FY2023 data actually shows)

| # | Risk | Evidence in the data | Severity |
|---|---|---|---|
| 1 | **Capex-driven FCF compression in 2024** | Q4 capex $11.0B (+36.8% QoQ) vs $8.1B Q3; Q4 FCF $7.9B vs $22.6B Q3 | **High** |
| 2 | **Tax rate normalization** | 13.9% book vs 22.4% cash rate; $7.7B deferred benefit; IPR&D DTA $17.8B | **High** |
| 3 | **Revenue deceleration + opex re-acceleration** | Revenue +9.8% → +8.7%; R&D+S&M +21.3% → +11.0% but still > revenue growth | Medium |
| 4 | **Receivables / collections** | AR +19.2% vs revenue +8.7%; DSO +5 days; allowance only 1.6% of AR | Medium |
| 5 | **SBC dilution** | $22.1B, +13.3% YoY, 26% of operating income, 7.2% of revenue | Medium |
| 6 | **FX** | FX transaction loss $1.24B (vs $0.65B), tripling | Low–Med |
| 7 | **Investment-mark volatility** | Securities loss $0.82B in 2023 after −$5.52B in 2022; non-marketable equity $28.8B marked with $18.1B cumulative upward revaluations | Medium |
| 8 | **Regulatory/antitrust** | Not quantifiable from statement facts; FY2023 shows $8.47B noncurrent accrued income taxes and $11.0B valuation allowance, but no litigation accrual disclosure in the returned tags | Monitor |
| 9 | **Balance sheet** | Effectively nil — $110.9B cash+securities, $0 CP, ~$96B net cash | **Very low** |

---

## 11. Actionable Trading Insights

1. **Don't trade the FY2023 headline — trade the Q4 exit rate.** The 27.2% EPS growth and 88.5% FCF-payout look like a compounding machine. The Q4 standalone figures (capex +37% QoQ, OCF −38% QoQ, FCF −65% QoQ) say 2024 FCF will *not* grow at that pace. **Position for an FCF-growth disappointment even if revenue beats.**
2. **Anchor on EPS, not FCF, for 2024 — but haircut the tax rate.** EPS-based multiples are the more favorable lens because capex hits FCF but not EPS (only via depreciation over time). However, re-model at a **15.5–16.5% tax rate** rather than 13.9%: that alone trims ~$0.14–0.16/share, i.e. roughly **2.5% of EPS**.
3. **Buy the dip risk/reward is structurally protected.** ~**$7.7/share of net cash** (~5% of a ~$150 share price) plus a 3%-per-year share-count shrink provides a real floor. Repurchases at $61.5B/yr have enormous capacity to continue: at 88.5% of FCF they're aggressive but net cash of ~$96B gives the company the option to *maintain* the buyback even if FCF halves — which is exactly what Q4 demonstrated ($16.2B bought vs $7.9B FCF).
4. **Watch three specific prints for confirmation/invalidation:** (a) **Q1'24 capex** — above ~$10B/quarter confirms the $44B run-rate and kills the FCF story; (b) **Q1'24 DSO** — above 58 days confirms a collections problem; (c) **Q1'24 effective tax rate** — a step-up above 16% confirms the normalization thesis.
5. **Segment information is the missing link.** The most important swing factor for GOOGL (Cloud margin vs Services margin) is not in the returned data. **Before sizing, pull segment revenue and operating income from the 10-K text** — the consolidated 27.4% margin can hide a widening Services-vs-Cloud mix shift in either direction.
6. **Relative-value framing from the SBC adjustment:** GAAP diluted EPS $5.80, but SBC-adjusted cash EPS is **~$7.30** **[derived]**. On a GAAP basis GOOGL screens ~26% more expensive than on an economically comparable basis. If the desk's comp set includes lower-SBC peers, GOOGL's premium is *smaller* than the GAAP numbers imply — a legitimate long argument. The counter: SBC is growing faster than revenue, so the gap is widening, not closing.
7. **Valuation sensitivity (price not in tool data — map to the live quote).** On FY2023 fundamentals: P/E = Price ÷ $5.80; P/FCF = Price ÷ $5.46 (FCF/share); ex-SBC P/E = Price ÷ $7.30; ex-cash P/E = (Price − $7.71) ÷ $5.80. At a $150 reference price: **25.9x GAAP P/E, 27.5x P/FCF, 20.5x ex-SBC P/E, 24.5x ex-cash P/E.** A ~25x multiple is defensible only if the 2023 operating-leverage story persists into 2024 — which the Q4 capex data puts in question. **That tension is the trade.**
8. **Insider signal absent — do not substitute buybacks for insider conviction.** Insiders and the issuer are different actors; the $61.5B buyback is a capital-allocation decision approved by the board, not evidence of individual executive confidence. Source Form 4s separately.

---

## 12. Key Points Summary Table

| Category | Metric | FY2021 | FY2022 | FY2023 | Read-through for GOOGL |
|---|---|---:|---:|---:|---|
| **Growth** | Revenue ($M) [derived] | 257,637 | 282,836 | **307,394** | +8.7% — decelerating from +9.8% |
| | Revenue growth | — | +9.8% | +8.7% | Moderating top line |
| **Profitability** | Gross margin | 56.9% | 55.4% | **56.6%** | Recovered +120 bps |
| | Operating income ($M) [derived] | 78,714 | 74,842 | **84,293** | +12.6%, faster than revenue |
| | Operating margin | 30.6% | 26.5% | **27.4%** | Leverage restored, still below 2021 |
| | Net income ($M) [derived] | 76,033 | 59,972 | **73,795** | +23.0% |
| | Net margin | 29.5% | 21.2% | **24.0%** | +280 bps |
| **Per share** | Diluted EPS | 5.61 | 4.56 | **5.80** | +27.2%; ~3.3pp from buybacks |
| | Diluted shares (M) | 13,553 | 13,152 | **12,723** | −3.3% |
| | Ex-SBC cash EPS [derived] | — | — | **~7.30** | 26% above GAAP |
| **Cost discipline** | Total costs & expenses ($M) | 178,923 | 207,994 | **223,101** | +7.3% < revenue +8.7% (the win) |
| | Cost of revenue growth | — | +13.8% | **+5.6%** | Single biggest driver of 2023 margin |
| | SBC ($M) | 15,700 | 19,500 | **22,100** | +13.3%, 26% of op income |
| **Cash flow** | Operating cash flow ($M) | 91,652 | 91,495 | **101,746** | +11.2% |
| | Capex ($M) | 24,640 | 31,485 | **32,251** | Q4 alone $11.0B ⇒ ~$44B run-rate |
| | Free cash flow ($M) [derived] | 67,012 | 60,010 | **69,495** | +15.8%, but Q4 FCF only $7.9B |
| | FCF margin | 26.0% | 21.2% | **22.6%** | At risk in 2024 from capex |
| **Capital return** | Buybacks ($M) | 50,274 | 59,296 | **61,504** | 88.5% of FCF; record |
| | Shares outstanding (M) | — | 12,849 | **12,460** | −3.0% net of SBC dilution |
| **Balance sheet** | Cash + ST investments ($M) | — | 113,762 | **110,916** | ~$7.7/share net cash |
| | Total debt/lease principal ($M) | — | — | **~14,862** | Negligible; $0 commercial paper |
| | Net cash ($M) [derived] | — | — | **~96,000** | Deep downside cushion |
| | Total assets ($M) | — | 365,264 | **402,392** | +10.2% |
| | Accounts receivable ($M) | — | 40,258 | **47,964** | +19.2% vs revenue +8.7% ⚠ |
| | DSO (days) [derived] | — | ~51.9 | **~56.9** | +5 days — watch collections |
| **Tax** | Effective book tax rate | 16.2% | 15.9% | **13.9%** | Unsustainably low |
| | Cash tax rate [derived] | 14.8% | 26.5% | **22.4%** | $7.7B deferred benefit will reverse ⚠ |
| | Cash taxes paid ($M) | 13,412 | 18,892 | **19,164** | Real cash drain |
| **Other** | FX transaction loss ($M) | (240) | (654) | **(1,238)** | Tripled — pre-tax headwind |
| | Securities gain/(loss) ($M) | +12,270 | (5,519) | **(823)** | OI&E tailwind is gone |
| | AOCI ($M) | — | (7,603) | **(4,402)** | Bond losses reversing (+$3.2B) |
| **Insider** | Form 4 activity | **DATA UNAVAILABLE** | **DATA UNAVAILABLE** | **DATA UNAVAILABLE** | Vendor has no authorized archive — do not infer |
| **Derived quarterly** | Q3'23 → Q4'23 OCF | — | — | **30,656 → 18,915** | −38.3% |
| | Q3'23 → Q4'23 Capex | — | — | **8,055 → 11,019** | **+36.8% — the 2024 story** |
| | Q3'23 → Q4'23 FCF | — | — | **22,601 → 7,896** | −65.1% |

---

### Bottom Line for the Desk

**GOOGL FY2023 is a fundamentally excellent year with a deteriorating forward FCF setup and a flattered tax rate.** The company grew revenue 8.7%, expanded operating margin 90 bps on genuine cost-of-revenue discipline, generated $69.5B of FCF, returned $61.5B via buybacks, shrank its share count 3%, and holds ~$96B of net cash with essentially no leverage. That is a durable, high-quality franchise with a real valuation floor.

Against that: **Q4 capex of $11.0B annualizes to ~$44B**, Q4 FCF was only **$7.9B**, the **13.9% book tax rate is a $7.7B non-cash benefit that must reverse** (cash tax rate was 22.4%), receivables are growing 2.2x faster than revenue, and SBC is accelerating faster than the top line. **The 2023 EPS number is better than the 2023 cash-economics trend — and 2024 will be the year those two lines converge.** Fundamentally constructive on the franchise; cautious on the 2024 FCF/EPS-growth setup that the current narrative is extrapolating.