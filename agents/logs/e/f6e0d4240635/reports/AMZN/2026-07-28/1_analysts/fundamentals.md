# AMZN — Fundamental Research Report
**As of 2026-07-28 | Latest filed data: Q1 FY2026 10-Q (period ended 2026-03-31, accepted 2026-04-30); FY2025 10-K (filed 2026-02-06)**

---

## 1. Company Profile & Data Provenance

**Amazon.com, Inc. (AMZN)** — the global e-commerce, logistics, cloud infrastructure (AWS), advertising, and devices/services conglomerate. The Q1 FY2026 10-Q explicitly reports **`NumberOfOperatingSegments = 3`**, consistent with the current reporting structure (North America, International, AWS).

All figures below are **point-in-time SEC XBRL facts** filtered by actual EDGAR acceptance timestamp, so nothing here is look-ahead biased. Two important caveats on data quality:

- **Insider transactions: DATA UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for AMZN as of 2026-07-28. I will not infer or fabricate insider activity. Treat Form-4 flow as an open information gap.
- **Statement-level truncation:** the vendor returned facts as a flat tag list rather than a fully aggregated statement. Some line items (e.g., FY2025 total revenue, technology & content expense) were not exposed before truncation. Where I derive a figure, I label it **(derived)** and show the arithmetic so it is auditable.

---

## 2. Q1 FY2026 Income Statement — The Core Picture

| Metric ($M) | Q1 2026 | Q1 2025 | YoY |
|---|---|---|---|
| Revenue | **181,519** | 155,667 | **+16.6%** |
| Cost of goods & services | 87,463 | 76,976 | +13.6% |
| **Gross profit** | **94,056** | 78,691 | **+19.5%** |
| Gross margin | **51.8%** | 50.6% | +120 bps |
| Marketing | 10,314 | 9,763 | +5.6% |
| G&A | 2,587 | 2,628 | −1.6% |
| Total costs & expenses | 157,667 | 137,262 | +14.9% |
| **Operating income** | **23,852** | 18,405 | **+29.6%** |
| Operating margin | **13.14%** | 11.82% | +132 bps |
| Non-operating income | **15,982** | 3,274 | +388% |
| Interest income | 1,135 | 1,066 | +6.5% |
| Interest expense | 800 | 541 | **+47.9%** |
| Pretax income | 39,834 | 21,679 | +83.7% |
| Tax | 9,560 | 4,553 | +110% |
| Effective tax rate | 24.0% | 21.0% | +300 bps |
| **Net income** | **30,255** | 17,127 | **+76.7%** |
| Diluted EPS | **$2.78** | $1.59 | +74.8% |
| Diluted shares (derived) | ~10,883M | ~10,772M | +1.0% |

### ⚠️ Critical earnings-quality flag
**$15.98B of non-operating income = 40.1% of net income.** The drivers, per the XBRL detail:

- `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount` = **+$12,328M** (vs just $37M a year ago)
- `EquitySecuritiesFvNiGainLoss` = **−$883M** (mark-to-market losses on listed equity stakes)
- `OtherNonoperatingIncomeExpense` = +$15,647M; FX transaction gain +$160M

This is a **non-cash, mark-to-model revaluation of a private equity stake** (the pattern — a ~$32B step-up in carrying value — is consistent with a large private AI-related holding). It flowed through `IncomeLossFromContinuingOperationsBeforeIncomeTaxes` and inflated the 24% effective tax rate and the deferred tax line (`DeferredIncomeTaxExpenseBenefit` $12,798M in the quarter).

**Clean (operating) EPS, derived:** (23,852 + 1,135 − 800) × (1 − 0.24) ÷ 10,883 ≈ **$1.69** vs ~$1.39 for Q1 2025 → **~+21% core EPS growth**, versus the +75% headline. Still healthy, but roughly a third of the headline number is investment marks.

---

## 3. Cash Flow — The Central Tension of the Thesis

| $M | Q1 2026 | Q1 2025 | TTM (Apr'25–Mar'26) | FY2025 | FY2024 | FY2023 |
|---|---|---|---|---|---|---|
| Operating cash flow | 26,032 | 17,015 | **148,531** | 139,514 | 115,877 | 84,946 |
| CapEx (productive assets) | **44,203** | 25,019 | **151,003** | 131,819 | 82,999 | 52,729 |
| **Free cash flow (derived)** | **−18,171** | −8,004 | **−2,472** | **+7,695** | **+32,878** | **+32,217** |
| Investing cash flow | −64,212 | −29,803 | −176,954 | −142,545 | −94,342 | −49,833 |
| Financing cash flow | +52,767 | −47 | +62,475 | +9,661 | −11,812 | −15,879 |

**This is the single most important number set in the report.**

1. **CapEx is compounding violently:** 52.7 → 83.0 → 131.8 → 151.0 (TTM). Q1 2026 alone at $44.2B is **+77% YoY and ~$177B annualized** — implying FY2026 CapEx could exceed $190–200B.
2. **FCF has gone negative on a TTM basis (−$2.5B)** for the first time in this dataset's history outside of a heavy-investment trough. OCF growth (+6.5% TTM) is no longer covering investment.
3. **It is debt-funded.** Financing swung from −$47M to **+$52,767M** in a single quarter. `ProceedsFromIssuanceOfLongTermDebt` = **$53,441M in Q1 2026 alone**, versus $15,673M for the entirety of FY2025 and **$0 in FY2023 and FY2024**.
4. **Off-balance-sheet pipeline:** `CapitalExpendituresIncurredButNotYetPaid` = **$27,000M at 12/31/2025** (up from $16,800M) — CapEx incurred but not yet cash-settled, i.e., more outflow queued.

**Read-through:** Management is pre-committing enormous capital to AI compute/data centers/energy/logistics. The market will price this either as a widening moat (AWS reacceleration) or as peak-cycle misallocation. The fundamentals as reported are **operationally strong, cash-flow negative, and increasingly levered**.

---

## 4. Balance Sheet — Still Strong, But Leverage Inflected

| $M | 2026-03-31 | 2025-12-31 | Change |
|---|---|---|---|
| Cash & equivalents | 101,816 | 86,810 | +15,006 |
| Available-for-sale securities | 42,200 | 45,800 | −3,600 |
| **Total liquid (derived)** | **144,016** | 132,610 | +11,406 |
| Accounts receivable, net | 75,532 | 67,729 | +7,803 |
| Inventory, net | 36,534 | 38,325 | **−1,791** |
| Current assets | 255,155 | 229,083 | +26,072 |
| Other non-current assets | **151,827** | 122,607 | **+29,220** |
| **Total assets** | **916,630** | 818,042 | **+98,588** |
| Accounts payable | 124,749 | 121,909 | +2,840 |
| Accrued liabilities | 71,120 | 75,520 | −4,400 |
| Current liabilities | 216,756 | 218,005 | −1,249 |
| **Long-term debt (total)** | **122,632** | 68,836 | **+53,796** |
| — of which non-current | 119,074 | 65,648 | +53,426 |
| Finance lease liabilities | 13,325 | 12,286 | +1,039 |
| Operating lease liabilities | 91,617 | 89,252 | +2,365 |
| Other non-current liabilities | 48,072 | 35,985 | +12,087 |
| **Equity (derived)** | **~441,914** | ~411,065 | +30,849 |

**Key observations:**

- **Total assets jumped $98.6B in one quarter.** ~$29B of that is the non-current asset revaluation (non-marketable equity securities: **$16.2B → $48.1B**), ~$44B is CapEx, the rest working capital.
- **Long-term debt nearly doubled (+78%) in 90 days.** Interest expense already rising +48% YoY; at a ~$120B+ debt base, every 100 bps on refinancing is ~$700–900M/yr of incremental pre-tax drag — immaterial against $24B quarterly operating income, but the *direction* matters.
- **Adjusted leverage (derived):** Debt + finance leases + operating leases = 122,632 + 13,325 + 91,617 = **$227.6B** against $144.0B liquid = **net debt ≈ $83.6B**. Ex-lease net cash is roughly **+$8B** (i.e., essentially neutral). Amazon is no longer a net-cash fortress.
- **Working capital is healthy:** inventory down 4.7% sequentially while revenue grew; inventory valuation reserves *fell* ($3.3B → $2.8B), signaling no obsolescence build. AR up 11.5% QoQ (normal Q4→Q1 seasonality); allowance $2.6B = 3.4% of gross AR, +20 bps QoQ — watch item, not a problem.
- **AOCI fell $28,230M → $24,868M**, driven by −$2,511M AFS mark-to-market and −$764M FX — reflects rate/curve pressure on the securities portfolio.
- **Remaining performance obligation:** contract liabilities flat at $25.0B ($20.9B current + $4.4B non-current); $9.4B of it recognized as revenue in Q1.

### 🚨 Contractual obligations: $569.3B
`ContractualObligation` at 2026-03-31 = **$569,280M**, with maturities: remainder of FY $46.5B, next 12 months $57.1B, year 2 $48.9B, year 3 $40.4B, year 4 $38.6B. This is a **~$57B/yr call on liquidity from purchase commitments alone** (AI capacity, energy, content, logistics). It is *not* on the balance sheet as debt but is economically senior to equity in a demand shock. Combined with $110.1B of undiscounted operating lease payments, the fixed-charge stack is now ~$125B/yr versus $148.5B TTM operating cash flow. **This is the tightest coverage ratio Amazon has carried in a decade.**

---

## 5. Multi-Year Financial History

| $M | FY2023 | FY2024 | FY2025 | TTM (Mar'26) |
|---|---|---|---|---|
| Costs & expenses | 537,933 | 569,366 | **636,949** | — |
| Operating income (derived: revenue − costs) | 36,852 | 68,593 | not exposed¹ | — |
| Net income (derived²) | 30,425 | 59,248 | **77,670** | **90,798** |
| Operating cash flow | 84,946 | 115,877 | 139,514 | 148,531 |
| CapEx | 52,729 | 82,999 | 131,819 | 151,003 |
| D&A | — | — | 65,756² | 70,439 |
| SBC | 24,023 | 22,011 | **19,467** | — |
| Advertising expense (P&L, i.e., Amazon's own marketing) | 20,300 | 21,400 | 23,500 | — |
| Comprehensive income | 31,872 | 62,254 | **105,934** | — |
| Long-term debt issued | **0** | **0** | 15,673 | 68,368 |
| LT debt repaid | 3,676 | 9,182 | 5,021 | 5,021 |

¹ *Not exposed before vendor output truncation. FY2025 revenue = 636,949 + operating income; using the Q1 2026 margin trajectory, FY2025 revenue was roughly the $700–715B range and operating income roughly $70–78B.*
² *Derived from TTM bridge: FY2025 NI = TTM 90,798 − Q1'26 30,255 + Q1'25 17,127 = **77,670**. This bridge is validated by OCF: 148,531 − 26,032 + 17,015 = **139,514**, which exactly matches the FY2025 10-K figure — so the TTM arithmetic is internally consistent.*

**Trend quality — what the history actually says:**

- **Net income: 30.4 → 59.2 → 77.7 → 90.8 (TTM).** ~44% CAGR over three years. Genuine operating leverage, not just accounting.
- **SBC is falling as a share of the P&L:** $24.0B (FY2023) → $22.0B → $19.5B, and Q1 2026 SBC of $4.03B (2.2% of revenue) vs $3.69B a year ago. Modest re-acceleration tied to headcount/grant cycles, but multi-year dilution is structurally improving. Diluted shares +1.0% YoY.
- **Comprehensive income > net income** ($105.9B vs $77.7B in FY2025) due to AOCI recovery — but that reversal has now stalled (AOCI fell in Q1 2026).
- **The leverage inflection is new:** zero LT debt issuance in FY2023 and FY2024, $15.7B in FY2025, then **$53.4B in Q1 2026 alone**. This is a deliberate, board-sanctioned shift in capital structure to fund the AI buildout.

---

## 6. Analytical Synthesis — What Actually Matters for a Trader

**Bull case (evidence-based):**
1. **Revenue acceleration to +16.6%** with gross margin +120 bps and operating margin +132 bps — the mix shift toward AWS + advertising is real and is *offsetting* $70B+ of annual D&A currently hitting the P&L.
2. **Core operating EPS +~21%** even stripping out all investment marks.
3. **D&A of $18.9B in Q1 2026 (+32.9% YoY)** is depreciating capacity that is *already* generating returns — margin expansion alongside a $44B capex quarter is a strong signal the spend is productive, not speculative.
4. **Inventory discipline and reserve releases** argue against a demand cliff in retail.
5. **Interest coverage remains enormous** (operating income $23.9B vs interest $0.8B = ~30x).

**Bear case (evidence-based):**
1. **Negative TTM FCF (−$2.5B) and a −$18.2B FCF quarter**, with CapEx running ~$177B annualized against $57B/yr of contractual purchase commitments — **capit1al intensity is outrunning internally generated cash by a wide margin.**
2. **Debt-funded growth**: LT debt +78% in one quarter. If credit spreads widen or rates move against them, the marginal AI dollar gets more expensive precisely when payback periods are longest.
3. **40% of net income came from a mark-to-model private-equity revaluation** (+$12.3B). This is not repeatable, is not cash, and is *mark-to-model*, meaning it can reverse. Any future "downward price adjustment" flows straight through EPS. **Traders should model FY2026 EPS ex-investment-gains.**
4. **Effective tax rate stepped up to 24.0% from 21.0%** — a 300 bps headwind that cuts ~$1.2B/quarter off the bottom line if sustained.
5. **Q1 2026 OCF/NI conversion of just 0.86x**, dragged by a −$8.0B accrued-liabilities draw and −$16.0B of other non-current asset build. Cash conversion is deteriorating.

**The honest verdict:** AMZN is *operationally* accelerating and *financially* taking on risk simultaneously. The income statement is arguably the best it has ever looked; the cash flow statement is arguably the most strained. The stock's near-term path likely hinges on whether the market rewards AWS/AI margin expansion (bullish) or punishes the negative-FCF, debt-funded capex super-cycle (bearish). **The single most important forward checkpoint is the next 10-Q's CapEx figure and whether TTM FCF stays negative.**

### Actionable positioning notes
- **Do not anchor on the $2.78 Q1 EPS.** Use ~**$1.69** as the clean operating figure for valuation and compare to a ~$1.39 clean base (+21%).
- **Track `ContractualObligation` ($569.3B)** next quarter — a further jump alongside rising debt is the clearest leading indicator of balance-sheet stress.
- **Watch the $48.1B non-marketable equity securities line.** A reversal here is the fastest route to an EPS miss that has nothing to do with operations.
- **Monitor FY2025 revenue/operating income once fully parsed** — the vendor output truncated those exact tags; confirming FY2025 operating income resolves the one material gap in this report.
- **Insider signal is unavailable** (no authorized archive). Do not read the absence as either bullish or bearish — it is a data gap, not a datapoint.

---

## 7. Key Points Summary

| Category | Metric | Value | Read |
|---|---|---|---|
| **Profile** | Company / Ticker | Amazon.com, Inc. / **AMZN** | 3 operating segments (NA, Int'l, AWS) |
| **Profile** | Latest filing used | Q1 FY2026 10-Q, filed 2026-04-30 | Period ended 2026-03-31 |
| **Growth** | Q1 2026 revenue | $181,519M | **+16.6% YoY** — accelerating |
| **Growth** | Q1 2026 operating income | $23,852M | **+29.6% YoY** |
| **Margins** | Q1 2026 operating margin | 13.14% | +132 bps YoY |
| **Margins** | Q1 2026 gross margin | 51.8% | +120 bps YoY |
| **Earnings** | Q1 2026 diluted EPS | $2.78 | +74.8% YoY — **38% is investment marks** |
| **Earnings quality** | Clean operating EPS (derived) | **~$1.69** | +~21% YoY — the real run-rate |
| **Earnings quality** | Non-operating income | $15,982M (40% of NI) | +$12,328M private-equity revaluation — **not repeatable** |
| **Cash flow** | TTM free cash flow (derived) | **−$2,472M** | **Turned negative** (FY2025: +$7.7B) |
| **Cash flow** | Q1 2026 free cash flow | **−$18,171M** | CapEx $44.2B vs OCF $26.0B |
| **Cash flow** | TTM operating cash flow | $148,531M | +6.5% — decelerating vs 20%+ history |
| **Capex** | Q1 2026 CapEx | $44,203M | **+77% YoY**; ~$177B annualized |
| **Capex** | CapEx incurred not yet paid | $27,000M (12/31/25) | Pipeline still building |
| **Leverage** | Long-term debt | $122,632M | **+78% in one quarter** (from $68,836M) |
| **Leverage** | Q1 2026 LT debt issued | $53,441M | vs $0 in FY2023 & FY2024 |
| **Leverage** | Net debt incl. leases (derived) | ~$83,600M | Ex-lease ~net neutral (+$8B) |
| **Liquidity** | Cash + AFS securities | $144,016M | Up $11.4B QoQ |
| **Commitments** | Total contractual obligations | **$569,280M** | ~$57B due within 12 months — key risk metric |
| **Balance sheet** | Total assets / Equity | $916,630M / ~$441,914M | Assets +$98.6B in one quarter |
| **Balance sheet** | Non-marketable equity securities | $16.2B → **$48.1B** | Mark-to-model; reversal risk |
| **Working capital** | Inventory | $36,534M | **−4.7% QoQ** — healthy discipline |
| **Working capital** | AR allowance / gross AR | ~3.4% | +20 bps QoQ — monitor |
| **Tax** | Q1 2026 effective rate | 24.0% | Up 300 bps YoY — EPS headwind |
| **Efficiency** | SBC FY2023→FY2025 | $24.0B → $19.5B | Multi-year dilution improving |
| **History** | Net income FY23→FY25 | $30.4B → $59.2B → $77.7B | ~44% 3-yr CAGR |
| **History** | TTM net income | $90,798M | +17% vs FY2025 |
| **Insider** | Transactions | **DATA UNAVAILABLE** | Not inferable — genuine gap |
| **Data gap** | FY2025 revenue / op income | Not exposed before truncation | Only material analytical gap |
| **Thesis** | Net assessment | **Operationally accelerating, cash-flow negative, leverage inflecting** | Watch next quarter's CapEx + FCF |