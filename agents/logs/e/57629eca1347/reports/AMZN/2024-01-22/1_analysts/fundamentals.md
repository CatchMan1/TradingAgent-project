# AMZN (Amazon.com, Inc.) — Fundamental Research Report
**Analysis date:** 2024-01-22 | **Ticker:** AMZN | **Fiscal data through:** Q3 2023 (period ended 2023-09-30, 10-Q accepted 2023-10-27)

---

## 1. Critical data-availability caveat (read first)

- **The most recent fundamental data available in this environment is the Q3 2023 10-Q (period ended 2023-09-30, filed/accepted 2023-10-27).** AMZN had **not yet reported Q4/FY2023** as of 2024-01-22. All figures below are therefore *point-in-time through the September quarter* and carry roughly one quarter of lag versus the trading date.
- Requests for **annual** statements returned the same 10-Q fact set; the cache **does not contain 10-K facts** for AMZN. Consequently full-year 2020–2022 income statements/cash flows are not retrievable from the tools. Where I compute multi-period figures I state the arithmetic explicitly.
- **Insider transactions: DATA UNAVAILABLE.** The vendor has no authorized point-in-time insider-transactions archive for AMZN as of 2024-01-22. **No insider buying/selling should be inferred** — I have not fabricated any.
- Revenue is **not directly present** in the returned tag set; I derive it as `CostsAndExpenses + OperatingIncomeLoss` (this arithmetic reproduces Amazon's reported revenue exactly).
- Items flagged **[not tool-sourced]** come from general knowledge and are marked so traders can weight them accordingly.

---

## 2. Company profile

Amazon.com, Inc. (AMZN) is a global technology and e-commerce conglomerate reporting **3 operating segments** (`NumberOfOperatingSegments = 3`, confirmed in the data):
1. **North America** — online stores, physical stores, third-party seller services, advertising, subscription (Prime), devices.
2. **International** — same categories outside North America.
3. **Amazon Web Services (AWS)** — cloud compute, storage, database, AI/ML infrastructure and services.

Structural characteristics visible in the filings:
- **Extremely high operating leverage business** converting from a low-margin retail/logistics base into a high-margin mix of AWS + advertising, with a massive owned fulfillment/logistics and data-center asset base (leases of ~$88.8B operating + $14.6B finance; PP&E intensity ~9–13% of revenue).
- **Equity-funded compensation model**: APIC rose **$17,645M** in 9M 2023 vs. SBC expense of **$17,704M** — essentially all book-equity growth ex-earnings comes from stock issuance; **zero share repurchases in 2023** and **no dividend**.
- **Contract-heavy, prepaid-ish cash cycle**: negative-to-low working capital dependence (heavy AP/accruals), large customer prepayments ($14.4B deferred revenue current).

---

## 3. Income statement — the margin inflection is the story

### 3.1 Q3 2023 vs. Q3 2022 (single quarter)

| Metric ($M) | Q3 2023 | Q3 2022 | Δ |
|---|---:|---:|---:|
| Revenue (derived) | **143,083** | 127,101 | **+12.6%** |
| Cost of goods & services | 75,022 | 70,268 | +6.8% |
| **Gross profit** (derived) | 68,061 | 56,833 | +19.8% |
| **Gross margin** | **47.6%** | 44.7% | **+2.9 pts** |
| Marketing | 10,551 | 11,014 | −4.2% |
| G&A | 2,561 | 3,061 | −16.3% |
| Total costs & expenses | 131,895 | 124,576 | +5.9% |
| **Operating income** | **11,188** | 2,525 | **+343%** |
| **Operating margin** | **7.82%** | 1.99% | **+5.8 pts** |
| Interest expense | 806 | 617 | +30.6% |
| Investment income (interest) | 776 | 277 | +180% |
| Non-operating income/(expense) | 1,001 | 419 | +139% |
| Pre-tax income | 12,189 | 2,944 | +314% |
| Tax | 2,306 | 69 | — |
| **Net income** | **9,879** | 2,872 | **+244%** |
| **Diluted EPS** | **$0.94** | $0.28 | +236% |
| D&A | 12,131 | 10,327 | +17.5% |
| SBC | 5,829 | 5,556 | +4.9% |

**Insight:** Revenue grew 12.6% while total costs grew only 5.9% — a classic operating-leverage release. Incremental revenue of ~$16.0B produced ~$8.7B of incremental operating income (~54% incremental margin). Marketing spend *declined* YoY and G&A fell 16%, evidence of the 2022–2023 cost-restructuring program (fulfillment regionalization, headcount rationalization) flowing fully into the P&L.

### 3.2 Nine months ended 2023-09-30 vs. 2022

| Metric ($M) | 9M 2023 | 9M 2022 | Δ |
|---|---:|---:|---:|
| Revenue (derived) | **404,824** | 364,779 | **+11.0%** |
| COGS | 212,186 | 203,191 | +4.4% |
| **Gross margin** | **47.6%** | 44.3% | +3.3 pts |
| Marketing | 31,468 | 29,420 | +7.0% |
| G&A | 8,806 | 8,558 | +2.9% |
| Total costs & expenses | 381,181 | 355,268 | +7.3% |
| **Operating income** | **23,643** | 9,511 | **+149%** |
| **Operating margin** | **5.84%** | 2.61% | **+3.2 pts** |
| Interest expense | 2,469 | 1,673 | +47.6% |
| Investment income (interest) | 2,048 | 544 | +276% |
| Non-operating income/(expense) | 228 | **(14,485)** | NM |
| Pre-tax income | 23,871 | (4,974) | NM |
| Tax | 4,058 | (1,990) | — |
| **Net income** | **19,801** | (3,000) | NM |
| **Diluted EPS** | **$1.89** | $(0.29) | NM |
| **Net margin** | **4.89%** | (0.82%) | — |
| D&A | 34,843 | 29,236 | +19.2% |
| SBC | 17,704 | 14,015 | **+26.3%** |
| Effective tax rate | 17.0% | NM | — |
| EBIT/interest coverage | **9.6x** | 5.7x | +3.9x |

**Key swing factor beyond operations:** the **$14.7B YoY improvement in non-operating results**, driven by mark-to-market on equity securities — `EquitySecuritiesFvNiGainLoss` was **+$1.0B in 9M 2023 vs. −$11.3B in 9M 2022** (the Rivian-type stake writedowns stopped reversing). Traders should **strip this out**: of the ~$22.8B swing in pre-tax income, ~$14.7B is non-operating and ~$8.1B (pre-tax) is genuinely operating. Operating income still more than doubled, so the quality is decent — but the optics overstate the improvement.

**Interest dynamics:** interest expense rose 47.6% (higher rates on a smaller debt stack), but investment income rose 276% as the cash/securities portfolio repriced to market yields. Net interest was only **−$421M in 9M 2023 vs. −$1,129M in 9M 2022** — a modest tailwind, and a structural positive if rates stay elevated given ~$99B of liquidity.

### 3.3 Trailing-twelve-month (Oct 2022 – Sep 2023) — directly reported windows

| Metric ($M) | TTM to 9/30/2023 |
|---|---:|
| Net income (`NetIncomeLoss`) | **20,079** |
| Operating cash flow | **71,654** |
| Capex (purchases of PP&E) | **54,733** |
| **Free cash flow (OCF − capex)** | **≈ 16,921** |
| D&A | 47,528 |
| Cash taxes paid | 8,677 |
| Deferred tax benefit | (7,779) |
| Revenue ≈ | **~554,000** *(derived; assumes Q4'22 revenue of ~$149.2B — [not tool-sourced])* |
| TTM diluted EPS ≈ | **~$1.95** *(derived: $20,079M / ~10.3B shares)* |

**Insight:** TTM operating cash flow of **$71.7B** against capex of **$54.7B** yields ~$16.9B of FCF. Compare with the *prior* TTM window (Oct 2021–Sep 2022): OCF **$39,665M** and capex **$65,988M** → **FCF of −$26,323M**. That is a **~$43B YoY FCF swing** — the single most important fundamental change at AMZN over the last four quarters. *(Amazon's own reported TTM FCF metric, which nets asset-sale proceeds and incentives, was ~$21.4B — [not tool-sourced]; the $16.9B gross figure above is the more conservative, tool-derived number.)*

---

## 4. Cash flow analysis

### 4.1 Nine months 2023 vs. 2022

| $M | 9M 2023 | 9M 2022 | Δ |
|---|---:|---:|---:|
| Operating cash flow | **42,481** | 17,579 | **+142%** |
| Capex (purchases of PP&E) | **38,141** | 47,053 | **−19%** |
| **FCF (OCF − capex)** | **4,340** | (29,474) | **+33,814** |
| Investing cash flow | (37,232) | (26,780) | worse |
| Financing cash flow | (9,133) | +9,632 | flipped negative |
| FX effect on cash | (288) | (1,730) | — |
| **Net change in cash** | **(4,172)** | (1,299) | — |

Q3 2023 standalone: OCF **$21,217M**, capex **$12,479M** → **Q3 FCF ≈ $8,738M**. Q3 OCF was 2.15× net income — healthy conversion.

**Capex discipline is the second engine of the FCF story:** capex fell 19% YoY to $38.1B (9.4% of revenue vs. 12.9%), a deliberate post-2022 pullback in fulfillment-network expansion, partly offset by rising AI/data-center investment. **Watch whether this capex cut is a one-off air-pocket or a new regime** — AWS/AI capacity needs are a natural re-acceleration force.

**Financing flipped to −$9.1B** from +$9.6B: management is now **repaying** debt (maturities of short-term debt $19.3B, long-term repayments $3.4B) rather than issuing, and **repurchased $0 of stock** in 2023 (vs. $6.0B in 9M 2022, all in H1 2022). Capital is being deleveraged and internally funded.

### 4.2 Quality-of-earnings flags
- **SBC is 4.4% of revenue** (9M 2023) and up 26% YoY — a real, recurring economic cost. `EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized = $23.3B` at 9/30/2023 = a multi-year dilution pipeline. Non-GAAP EPS that excludes SBC overstates economics by roughly $1.70/share annualized.
- **Deferred tax benefit of −$7,779M** in the TTM window is a large non-cash earnings and cash-tax support; cash taxes ($8.7B TTM) are running well below book tax expense. The 17.0% effective rate (9M 2023) reflects R&D credits ($600M) and stock-comp windfalls; a normalization toward 20–25% is a medium-term EPS headwind.
- Working capital was a **drag** in 2023 (accrued liabilities −$9,022M; AR/other assets +$10,364M in 9M 2023 offsetting the earnings growth) — i.e., the OCF surge would have been even larger without WC normalization. Conversely, 2022's WC build was the reverse.
- **Asset impairment charges** modest at $420M (9M 2023) — restructuring writedowns are largely done.

---

## 5. Balance sheet — fortress liquidity, shrinking debt, lease-heavy

### 5.1 Comparison: 2023-09-30 vs. 2022-12-31

| $M | 9/30/2023 | 12/31/2022 | Δ |
|---|---:|---:|---:|
| Cash & cash equivalents | **49,605** | 53,888 | −4,283 |
| Marketable (AFS) debt securities, FV | **49,871** | n/a | — |
| Accounts receivable (net) | 43,420 | 42,360 | +2.5% |
| Inventory (net) | 35,406 | 34,405 | +2.9% |
| **Current assets** | **142,995** | 146,791 | −2.6% |
| **Total assets** | **486,883** | 462,675 | +5.2% |
| Accounts payable | 72,004 | 79,600 | **−9.5%** |
| Accrued liabilities | 58,812 | 62,566 | −6.0% |
| **Current liabilities** | **145,214** | 155,393 | −6.6% |
| Long-term debt — current | 5,995 | 2,999 | +99.9% |
| Long-term debt — noncurrent | 61,098 | 67,150 | −9.0% |
| Finance lease liabilities | 12,466 | 15,783 | −21.0% |
| Operating lease liabilities | 73,902 | 69,040 | +7.0% |
| Deferred revenue (contract liability, current) | 14,398 | 13,227 | +8.9% |
| APIC | 92,711 | 75,066 | +23.5% (SBC) |
| AOCI | (5,003) | (4,487) | −516 |
| Shares outstanding | 10,330M | 10,242M | +0.86% |
| Shares issued / treasury | 10,845M / 515M | 10,757M / 515M | — |
| Shares outstanding (10/18/2023) | 10,334.0M | — | — |

**Derived balance-sheet quality metrics (9/30/2023):**
- **Current ratio: 0.98x** (142,995 / 145,214) — a *negative working capital* model by design (supplier-financed). Not a liquidity concern given the securities portfolio, but a sensitivity: **AP fell 9.5%** (the vendor-financing unwind is a cash *use* going forward).
- **Total liquidity: ~$99.5B** (cash $49.6B + AFS securities $49.9B at fair value; amortized cost $50.4B → only **$506M unrealized loss**, immaterial).
- **Debt-like obligations:** funded debt ~$67.1B + finance leases $12.5B = ~$79.6B → **net cash position of ~$20B ex-operating leases.** Including operating leases ($73.9B), gross obligations ~$153.9B.
- **Stockholders' equity ≈ $182.9B** *(derived: FY2022 equity of $146.0B + 9M 2023 net income $19.8B + SBC-driven APIC ~$17.6B − AOCI $0.5B ≈ $182.9B; FY2022 equity base is [not tool-sourced])*. **Book value/share ≈ $17.70.** Liabilities/equity ≈ **1.66x** — moderate.
- **Debt maturity ladder is comfortable:** only **$5,995M** of funded debt is current, fully covered ~8× by the securities portfolio maturing within one year ($43.1B at fair value).
- **Lease obligations heading the other way:** operating lease payments due rose to **$88.8B** (+$7.5B YoY) and the weighted-average discount rate rose to **3.2%** from 2.8% — a slow, structural drag as leases reprice. Finance lease liabilities fell 21% as prior obligations amortize.
- **Total contractual obligations: $284.4B** at 9/30/2023 (incl. $9.9B due in the remainder of FY2023, $35.7B in the next twelve months). Much of this is **AWS capacity and content purchase commitments** — a genuine fixed-cost risk if cloud demand decelerates, but also a signal of forward demand.

---

## 6. Shareholder returns, dilution, and capital allocation

| Item | 9M 2023 | 9M 2022 |
|---|---:|---:|
| Share repurchases | **$0** | $6,000M |
| Dividends | **$0** | $0 |
| LT debt issuance | **$0** | $12,931M |
| ST debt net | net repay | net borrow |
| SBC expense | $17,704M | $14,015M |
| Share count growth | +0.86% (9 mo.) | — |

**Insights:**
- **No buyback and no dividend.** All equity appreciation must come from per-share earnings growth. With SBC up 26% and ~$23.3B of unrecognized comp, annual dilution is running at roughly **1.3–1.7%**, consuming a good portion of net-income-per-share growth. **A buyback announcement is the most obvious un-priced catalyst** once FCF is sustainably positive — management has the balance sheet for it (~$99B liquidity, net cash) and has historically used buybacks opportunistically (2022 program completed in H1 2022).
- **Deleveraging is deliberate:** zero LT issuance in 2023, active bond and lease repayment. Fine, but it also means management is not yet signaling capital-return priority.

---

## 7. Insider transactions

**No data.** The vendor reports: *"the B-project data package has no authorized, point-in-time insider-transactions archive for AMZN by 2024-01-22."* I will not infer or fabricate insider activity. Any statement about insider buying/selling should be sourced independently before acting.

---

## 8. Trend synthesis — what the numbers say about AMZN's trajectory

1. **Margin regime change is real and broad-based.** Operating margin went 1.99% (Q3'22) → 7.82% (Q3'23); gross margin +2.9 pts to 47.6%; marketing and G&A both contracted in absolute dollars. This is not just AWS mix — it is fulfillment/logistics productivity + headcount discipline.
2. **Revenue growth is *re-accelerating* modestly** (Q3 +12.6% vs. 9M +11.0%), implying H1 2023 grew ~10%. Operating leverage on an accelerating top line is the most powerful combination for a mega-cap.
3. **Cash generation inflected hard:** TTM OCF $71.7B, TTM FCF $16.9B vs. −$26.3B a year earlier; capex down 19% YoY.
4. **Balance sheet is a non-issue** — ~$99.5B liquidity, net cash ex-leases, no meaningful near-term maturities, only $5,995M current debt.
5. **Earnings quality is mixed:** ~$14.7B of the pre-tax swing is non-operating mark-to-market, SBC is rising fast, and deferred taxes flatter cash EPS. Underlying operating improvement is genuine (~$8.1B pre-tax incremental) but smaller than the headline +$22.8B.
6. **Valuation is demanding on trailing numbers.** With TTM diluted EPS of ~$1.95, AMZN screens at a very high trailing P/E; the entire bull case depends on forward EPS compounding via margin expansion, not on multiple re-rating.

---

## 9. Actionable insights for traders

**Constructive / upside drivers**
- **Buy the margin-compounding thesis, not the revenue story.** Each 100 bps of additional operating margin on a ~$570B revenue base is worth ~$5.7B pre-tax — roughly $0.42/share. Margin expansion from 5.8% (9M) toward 8–9% is the highest-conviction lever.
- **FCF inflection supports a capital-return catalyst.** With TTM FCF positive and capex disciplined, watch for (a) buyback reinstatement, (b) debt paydown completing, (c) any disclosure of AI-driven capex re-acceleration (a negative for FCF, positive for revenue durability). A buyback announcement would mechanically lift EPS and is not in consensus models built off 2023's zero-repurchase run-rate.
- **Net cash + $99.5B liquidity = downside cushion.** Little financial risk in a growth scare; the equity is an operating-leverage instrument, not a credit story.
- **AWS reacceleration is the multiple driver.** With AWS the dominant profit pool, any evidence of cloud growth re-accelerating (AI workloads) re-rates the whole company. Q3 operating income of $11.2B implies AWS remains the majority of segment profit.

**Cautions / risks to underwrite**
- **Q4 2023 reporting is an imminent binary event.** As of 2024-01-22 the market had no Q4 data in this dataset; the FY2023 10-K and Q4 print land shortly after **[not tool-sourced: Amazon guided Q4'23 revenue to ~$160–167B and operating income to ~$7–11B]**. Position sizing should respect event risk; the margin trajectory in Q4 is what matters, not the revenue print.
- **Non-operating gains are not repeatable.** Do not annualize the +$228M 9M non-operating line or the mark-to-market swing; equity-stake volatility (Rivian-type) cuts both ways.
- **SBC dilution ~1.5%/yr plus a possible tax-rate normalization to 20–25%** are structural EPS headwinds — model them explicitly.
- **Accounts payable down 9.5% and accrued liabilities down 6%** mean the working-capital tailwind that flattered 2023 OCF may partially reverse; scrutinize OCF ex-WC.
- **$284.4B of contractual obligations**, including AWS capacity/purchase commitments, is a fixed-cost ratchet. If cloud or retail demand softens, that converts from growth investment to margin drag faster than the market expects.
- **Operating lease liabilities +7% and discount rates rising to 3.2%** will increase rent expense on renewal — a slow margin headwind, particularly in physical retail/logistics.

**Positioning summary:** The fundamental setup through Q3 2023 is the best AMZN has shown in years — accelerating revenue, a step-change in margins, and a $43B FCF swing. The offset is that the equity is priced for continuation of that path with no current capital return and rising SBC. **Net: fundamentally constructive with high sensitivity to the imminent Q4 print and to AWS growth commentary.** Use the Q4 report as the confirmation/invalidation point for the margin thesis rather than pre-positioning heavily into it.

---

## 10. Key points summary table

| Category | Metric | Value | Context / Read-through |
|---|---|---|---|
| **Data vintage** | Latest filed period | Q3 2023 (10-Q accepted 2023-10-27) | ~1 quarter lag; Q4/FY2023 not yet reported as of 2024-01-22 |
| **Profile** | Segments | 3 (North America, International, AWS) | Multi-segment; AWS = dominant profit pool |
| **Revenue** | Q3 2023 (derived) | $143,083M | +12.6% YoY — re-accelerating vs. 9M +11.0% |
| **Revenue** | 9M 2023 (derived) | $404,824M | +11.0% YoY |
| **Revenue** | TTM to 9/30/23 (est.) | ~$554B | Derived; Q4'22 base not tool-sourced |
| **Profitability** | Q3 2023 operating income | $11,188M (7.82% margin) | vs. 1.99% in Q3'22 — +5.8 pts |
| **Profitability** | 9M 2023 operating income | $23,643M (5.84%) | vs. 2.61% in 9M'22 — +3.2 pts |
| **Profitability** | 9M 2023 net income | $19,801M (4.89% net margin) | vs. −$3,000M in 9M'22 |
| **EPS** | Q3 2023 diluted | $0.94 | vs. $0.28 |
| **EPS** | 9M 2023 diluted | $1.89 | vs. −$0.29 |
| **EPS** | TTM diluted (derived) | ~$1.95 | $20,079M / ~10.3B shares |
| **Gross margin** | Q3 2023 | 47.6% | +2.9 pts YoY |
| **Earnings quality** | Non-operating swing 9M YoY | +$14.7B | Equity mark-to-market (+$1.0B vs −$11.3B); NOT repeatable |
| **Earnings quality** | SBC 9M 2023 | $17,704M (4.4% of rev) | +26% YoY; $23.3B unrecognized comp |
| **Earnings quality** | Effective tax rate 9M 2023 | 17.0% | Flattered by R&D credits / windfalls; normalizes higher |
| **Cash flow** | 9M 2023 OCF | $42,481M | +142% YoY |
| **Cash flow** | 9M 2023 capex | $38,141M (9.4% of rev) | −19% YoY (12.9% of rev prior) |
| **Cash flow** | 9M 2023 FCF | +$4,340M | vs. −$29,474M — $33.8B swing |
| **Cash flow** | TTM OCF / capex / FCF | $71,654M / $54,733M / **$16,921M** | vs. −$26,323M FCF prior TTM → ~$43B swing |
| **Balance sheet** | Total assets (9/30/23) | $486,883M | +5.2% YTD |
| **Balance sheet** | Cash + AFS securities | **~$99,476M** | AFS unrealized loss only $506M |
| **Balance sheet** | Current ratio | 0.98x | Negative-WC model by design |
| **Balance sheet** | Funded debt (current + LT) | $67,093M | LT noncurrent −9.0% YTD; deleveraging |
| **Balance sheet** | Finance / operating leases | $12,466M / $73,902M | Operating lease +7%; discount rate 2.8%→3.2% |
| **Balance sheet** | Net debt ex-operating leases | **~−$20B (net cash)** | Liquidity far exceeds funded debt |
| **Balance sheet** | Stockholders' equity (derived) | ~$182.9B; BVPS ~$17.70 | Liabilities/equity ~1.66x |
| **Obligations** | Total contractual obligations | $284,407M | $35,712M due in next 12 months |
| **Capital return** | Buybacks 9M 2023 | $0 | vs. $6,000M in 9M 2022 — potential catalyst |
| **Capital return** | Dividend | None | — |
| **Dilution** | Shares out | 10,330M (9/30/23); 10,334M (10/18/23) | +0.86% in 9 months |
| **Coverage** | EBIT / interest 9M 2023 | 9.6x | vs. 5.7x prior year |
| **Insider activity** | — | **DATA UNAVAILABLE** | Not fabricated; no archive for AMZN at 2024-01-22 |
| **Key catalyst** | Q4/FY2023 results | Pending as of 2024-01-22 | Binary event for the margin thesis |
| **Bottom line** | — | **Constructive, event-sensitive** | Own the margin/FCF inflection; size for Q4 event risk; model dilution & tax normalization |