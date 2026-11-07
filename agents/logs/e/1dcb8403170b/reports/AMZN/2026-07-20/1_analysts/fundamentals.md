# AMZN — Comprehensive Fundamental Report
**Company:** Amazon.com, Inc. (AMZN) | **Analysis date:** 2026-07-20 | **Latest filing in dataset:** 10-Q for Q1 2026, accepted 2026-04-30 (accn 0001018724-26-000014); 10-K for FY2025, accepted 2026-02-06 (accn 0001018724-26-000004)

---

## 0. Data provenance & important caveats (read first)

| Item | Status |
|---|---|
| Financial statements (income, balance sheet, cash flow; FY2023–FY2025 + Q1 2025/Q1 2026) | ✅ Retrieved from point-in-time SEC facts (10-K + 10-Q) |
| Quarterly income-statement history beyond Q1 2025 / Q1 2026 | ⚠️ Only two comparable quarters were present in the vendor fact set — no Q2–Q4 2025 quarterly P&L lines |
| Full-year revenue line for FY2025 | ⚠️ Not present in retrieved tag set (only total `CostsAndExpenses`). FY2025 **net income of ~$77.7B is derived** from the TTM identity and flagged as derived |
| Insider transactions | ❌ **DATA_UNAVAILABLE** — the vendor has no authorized point-in-time insider archive for AMZN. **No insider activity is inferred or fabricated in this report** |
| Q2 2026 results | ⚠️ Not yet reported as of 2026-07-20 → **imminent catalyst (late-July print)** |

All figures in USD millions unless stated. Balance sheet as of **2026-03-31**.

---

## 1. Company profile & structural snapshot

- **Business:** Three reportable segments (`NumberOfOperatingSegments = 3`): **North America**, **International**, and **AWS** — retail/e-commerce marketplaces, Prime subscription + advertising, third-party seller services, logistics, and cloud/AI infrastructure.
- **Shares outstanding:** 10,754M (2026-03-31); 10,757.1M (2026-04-22 cover date). Diluted ≈ 10,883M (implied: $30,255M NI / $2.78 diluted EPS); basic ≈ 10,729M.
- **Shares issued:** 11,269M vs. authorized 100,000M (par $0.01) → treasury stock program clearly active historically.
- **Common equity (derived as residual, reconciles cleanly):** ≈ **$433.9B** at 3/31/26 vs ≈ **$403.5B** at 12/31/25. Retained earnings ≈ $265B; APIC $143,979M; AOCI $24,868M.
- **Book value/share:** ≈ **$40.4** (433,956 / 10,754).
- **TTM ROE:** ≈ **21.7%** (TTM NI $90,798M ÷ avg. equity $418.7B).

---

## 2. Latest quarter (Q1 2026, three months to 2026-03-31) — the core of the story

| Metric ($M) | Q1 2026 | Q1 2025 | YoY |
|---|---:|---:|---:|
| Revenue | **181,519** | 155,667 | **+16.6%** |
| Cost of goods & services | 87,463 | 76,976 | +13.6% |
| **Gross profit** | **94,056** | 78,691 | **+19.5%** |
| Gross margin | **51.8%** | 50.6% | +120 bps |
| Marketing | 10,314 | 9,763 | +5.6% |
| G&A | 2,587 | 2,628 | **−1.6%** |
| Other operating expense, net | (447) | (308) | worse |
| Total costs & expenses | 157,667 | 137,262 | +14.9% |
| **Operating income** | **23,852** | 18,405 | **+29.6%** |
| **Operating margin** | **13.14%** | 11.82% | **+132 bps** |
| Interest expense | (800) | (541) | **+47.9%** |
| Interest/investment income | 1,135 | 1,066 | +6.5% |
| **Other non-operating income** | **15,647** | 2,749 | **+469%** |
| Non-operating income, net | 15,982 | 3,274 | +388% |
| Pre-tax income | 39,834 | 21,679 | +83.7% |
| Income tax | 9,560 | 4,553 | ETR **24.0%** vs 21.0% |
| Equity-method loss | (19) | +1 | — |
| **Net income** | **30,255** | 17,127 | **+76.6%** |
| Net margin | 16.7% | 11.0% | +570 bps |
| **Diluted EPS** | **$2.78** | $1.59 | **+74.8%** |
| Basic EPS | $2.82 | $1.62 | +74.1% |
| SBC | 4,032 | 3,689 | +9.3% |
| D&A | 18,945 | 14,262 | **+32.8%** |
| Comprehensive income | 26,893 | 16,247 | +65.5% |

### 🔑 Earnings-quality insight (most actionable item)
**~$12.3B of the $15.6B non-operating gain is a mark-to-market revaluation of equity securities without readily determinable fair value** (`UpwardPriceAdjustmentAnnualAmount = 12,328`, vs just $37M in Q1 2025). Corroborating evidence:
- `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` exploded from **$16.2B → $48.1B** in one quarter (+$31.9B), combining the revaluation plus new investment (see §4).
- Non-cash, non-recurring-ish, and **not** driven by retail/AWS operations.

**De-marked EPS math:** after-tax impact ≈ $15,647M × (1 − 24.0%) ≈ **$11.9B ≈ $1.09/share**. Strip it out and "core" diluted EPS ≈ **$1.67–1.70**, still **~+20% YoY** — but that is a materially different headline than +75%. *Traders should treat the $2.78 print as roughly one-third non-operating.*

### What was genuinely good
1. **Revenue acceleration to +16.6%** — the fastest visible growth rate in the dataset.
2. **Gross margin +120 bps** on a mix shift, and **marketing fell to 5.7% of revenue** (from 6.3%) while revenue grew 16.6% — unusually strong operating leverage.
3. **G&A declined in absolute dollars.**
4. **Operating income +29.6%** with margin **+132 bps** → this is the highest-quality line in the quarter.

### What got worse
1. **Interest expense +48%** ($800M vs $541M) — and long-term debt nearly **doubled** during the quarter (see §4), so this drag compounds from a ~$3.5–4B annualized run-rate vs ~$2.2B prior.
2. **Effective tax rate up 300 bps to 24.0%.**
3. **D&A +32.8%** — depreciation on the AI/cloud buildout is arriving.
4. **Equity-method investments turned negative**; FX gain ($160M) was the only offset.

---

## 3. Annual income-statement history (10-K series)

| $M | FY2023 | FY2024 | FY2025 | Trend |
|---|---:|---:|---:|---|
| Total costs & expenses | 537,933 | 569,366 | **636,949** | +5.8%, then **+11.9%** (re-acceleration) |
| SBC | 24,023 | 22,011 | **19,467** | **−18.9% over 2 yrs** — durable margin tailwind |
| Advertising expense | 20,300 | 21,400 | **23,500** | +9.8% (revenue-generating spend) |
| Net income (derived for FY2025) | n/a | n/a | **≈77,670** *(derived: TTM 90,798 − Q1'26 30,255 + Q1'25 17,127)* | — |
| Comprehensive income | 31,872 | 62,254 | **105,934** | +70% in FY2025 |
| **OCI component** (comprehensive − NI) | — | — | **≈+28,264** | Large unrealized investment/AFS gains — corroborates the mark-up theme |
| D&A | — | — | 55,373 (TTM to 3/25) → **70,439 (TTM to 3/26)** | **+27.2%** |
| Net income, TTM | — | 65,944 (TTM to 3/25) | **90,798 (TTM to 3/26)** | **+37.7%** |
| Contract liability revenue recognized | — | — | 17,400 | Deferred-revenue base $25.0B |

**Takeaway:** margin expansion is real and multi-year, and the SBC glide path (−$4.6B since FY2023) has been a genuine tailwind — but note that in Q1 2026 **SBC ticked back up +9.3% YoY to $4,032M**, which could mark the end of that tailwind. Remaining unrecognized SBC = **$14.4B**, so dilution/cost persists.

---

## 4. Balance sheet (2026-03-31 vs 2025-12-31) — the balance sheet has changed character

| $M | 3/31/2026 | 12/31/2025 | Change |
|---|---:|---:|---:|
| Cash & equivalents | **101,816** | 86,810 | +15,006 |
| Marketable securities (AFS) | 42,200 | 45,800 | −3,600 |
| **Total cash + securities** | **144,016** | 132,610 | **+11,406** |
| Accounts receivable, net | 75,532 | 67,729 | +7,803 |
| Inventory, net | 36,534 | 38,325 | −1,791 ✅ |
| Inventory valuation reserve | 2,800 | 3,300 | improved |
| Total current assets | 255,155 | 229,083 | +11.4% |
| **Total assets** | **916,630** | 818,042 | **+12.1%** |
| Accounts payable | 124,749 | 121,909 | +2,840 |
| Accrued liabilities | 71,120 | 75,520 | −4,400 |
| Contract liabilities (current) | 20,887 | 20,576 | +311 |
| Total current liabilities | 216,756 | 218,005 | −0.6% |
| **Long-term debt (total)** | **122,632** | 68,836 | **+78.2%** |
| — current portion | 2,832 | 2,748 | — |
| — non-current | **119,074** | 65,648 | **+81.4%** |
| Operating lease liabilities (non-current) | 79,067 | 76,597 | +2,470 |
| Finance lease liabilities (non-current) | 11,747 | 10,742 | +1,005 |
| Other non-current liabilities | 48,072 | 35,985 | **+33.6%** |
| Equity (derived residual) | **433,956** | 403,477 | +30,479 |
| Equity securities w/o readily determinable FV | **48,100** | 16,200 | **+197%** |

**Derived ratios:**
- **Current ratio: 1.18x** (255,155 / 216,756) — normal for Amazon's negative-working-capital-retail model.
- **Debt/equity: ~28%** (122,632 / 433,956); including all leases **~52%**.
- **Net debt (incl. leases, net of cash+securities): ~$83.6B** — still very manageable.
- **Cash + securities of $144.0B** with **$119.0B maturing within 1 year** → high-quality, highly liquid liquidity pool.

**🚩 The single biggest balance-sheet development:** Amazon borrowed **aggressively** in Q1 2026. `ProceedsFromIssuanceOfLongTermDebt` = **$53,441M in one quarter** — vs $15,673M for *all of FY2025*, and **$0 in both FY2023 and FY2024**. Long-term debt went from $68.8B to $122.6B. That is a regime change: the AI capex cycle is now being **debt-financed**, not just cash-financed. Watch credit metrics, and watch that interest expense line.

---

## 5. Cash flow & capital allocation — FCF has turned negative

| $M | FY2023 | FY2024 | FY2025 | TTM (4/25–3/26) | Q1 2026 |
|---|---:|---:|---:|---:|---:|
| Operating cash flow | 84,946 | 115,877 | **139,514** | **148,531** | 26,032 |
| Capex (productive assets) | 52,729 | 82,999 | **131,819** | **151,003** | **44,203** |
| **Free cash flow** | **32,217** | **32,878** | **7,695** | **(2,472)** | **(18,171)** |
| Net investing cash flow | (49,833) | (94,342) | (142,545) | (176,954) | **(64,212)** |
| Net financing cash flow | (15,879) | (11,812) | **+9,661** | **+62,475** | **+52,767** |
| Acquisitions/investments (businesses) | — | 3,680 | — | 19,297 | **15,408** |
| Marketable securities, net | — | — | — | — | −5,570 |
| Cash taxes paid | — | — | — | 8,741 | 1,323 |
| Deferred tax expense | — | — | — | **23,761** | 12,798 |

**Critical reads:**
1. **Capex super-cycle:** FY2023 $52.7B → FY2024 $83.0B → FY2025 $131.8B → **TTM $151.0B**. Q1 2026 alone was **$44.2B, +76.7% YoY**, or **24.4% of revenue**. `CapitalExpendituresIncurredButNotYetPaid` jumped $16.8B (FY24) → **$27.0B (FY25)** — accrued-not-yet-paid capex is *still* rising, meaning reported cash capex likely keeps climbing into H2 2026.
2. **TTM FCF is NEGATIVE (−$2.5B)** — the first negative FCF print in the dataset, versus +$32.2B in FY2023. OCF growth (+6.5% YoY on the TTM) no longer covers capex. **This is THE valuation debate for AMZN right now.**
3. **Financing flipped from −$15.9B (FY23) → +$9.7B (FY25) → +$62.5B TTM** — the company is now a net borrower to fund growth.
4. **Cash taxes ($8.7B TTM) are a fraction of book tax expense** (deferred tax expense $23.8B TTM, $12.8B in Q1'26 alone). Book income ≫ taxable income, largely because mark-to-market investment gains and SBC are non-cash for tax. **Do not treat the $30.3B quarterly net income as cash earnings.**
5. Diligence check: `IncreaseDecreaseInAccruedLiabilities` = **−$9,003M TTM / −$8,045M in Q1'26** — a working-capital headwind inside OCF.

---

## 6. Forward obligations — an enormous, escalating commitment stack

At 2026-03-31, **total contractual obligations = $569,280M** (up from $14,962M in the *other* commitments line at 9/30/25 — but the headline total is the number that matters here):

| Maturity bucket | $M |
|---|---:|
| Remainder of FY2026 | 46,489 |
| Next 12 months | 57,065 |
| Year 2 | 48,945 |
| Year 3 | 40,355 |
| Year 4 | 38,566 |
| Other commitments, remainder FY | 2,608 |

Plus:
- **Operating lease payments:** $110,135M undiscounted (liability $91,617M; next-12m $13,867M) — warehouses, offices, data centers.
- **Finance lease payments:** $16,496M undiscounted (next-12m $1,742M).
- **Unrecognized SBC:** $14,400M.
- **LT debt maturities (per FY2025 10-K):** $2.75B (Y1), $8.83B (Y2), $4.75B (Y3), $3.0B (Y4), $4.5B (Y5), **$45.0B after Y5** — well-laddered, no near-term wall (though Q1 2026's $53.4B issuance will need to be re-laddered in the next 10-Q).

**Interpretation:** $569B of contracted obligations ≈ 78% of TTM revenue-equivalent scale. This is overwhelmingly **AI/data-center/compute purchase commitments**. It is simultaneously (a) the bull case (contracted AI demand/backlog, AWS capacity lock-in) and (b) the bear case (fixed cost rigidity if AI demand digests).

---

## 7. Insider transactions

**Not available.** The vendor returned `DATA_UNAVAILABLE` — no authorized point-in-time insider-transactions archive exists for AMZN by 2026-07-20. **No insider buying or selling is reported, assumed, or inferred here.** Traders should source Form 4 data independently (SEC EDGAR) before drawing any conclusion about management sentiment.

---

## 8. Actionable insights for traders

### Bull setup (evidence-backed)
1. **Operating leverage is real and accelerating.** Operating income +29.6% YoY on revenue +16.6%, margin +132 bps to 13.14%, gross margin +120 bps, G&A down in dollars, marketing down 59 bps as % of revenue. Q1 2026 was a *high-quality* operating quarter beneath a noisy headline.
2. **TTM net income +37.7%** ($65.9B → $90.8B), TTM ROE ~21.7%, equity +$30.5B in a single quarter.
3. **Fortress liquidity:** $144.0B cash + marketable securities; net debt (incl. all leases) only ~$84B against a $434B equity base.
4. **SBC down $4.6B over two years** and inventory down $1.8B QoQ with lower valuation reserves — clean working capital.
5. **$569B of contracted obligations** supports the multi-year AI/AWS revenue thesis.

### Bear setup (evidence-backed)
1. **TTM FCF is negative (−$2.5B)** and deteriorating: capex $151.0B TTM vs. OCF $148.5B TTM. Capex/revenue at 24.4% in Q1.
2. **~39% of Q1 2026 pre-tax income was non-operating mark-to-market** ($12.3B equity revaluation). Trailing P/E on reported EPS is materially *understated*. Use **~$1.67–1.70** as the clean Q1 EPS, not $2.78.
3. **Debt-funded capex is new and rising:** LTD $68.8B → $122.6B in one quarter; interest expense +48% YoY and set to compound (~$3.5–4B annualized).
4. **D&A +32.8% YoY** — the depreciation cliff from the buildout is now hitting the P&L; expect continued margin friction even if gross margins hold.
5. **Accrued capex +61% to $27.0B** and an un-laddered $53.4B new debt stack imply **more capex and possibly more issuance ahead**.
6. **ETR up to 24.0%** from 21.0% — a 300 bps tax headwind to EPS.
7. **SBC inflected higher (+9.3% YoY in Q1'26)** — the multi-year margin tailwind may be exhausted.

### Near-term catalysts & watch items
| Catalyst | Timing | Watch |
|---|---|---|
| **Q2 2026 earnings / 10-Q** | Imminent (late July 2026; not in dataset as of 2026-07-20) | FY26 capex guide (does it exceed $151B TTM?); AWS growth; operating margin hold above 13%; **any further mark-to-market on the $48.1B non-marketable portfolio**; interest expense run-rate; new debt issuance/laddering |
| Anthropic-style AI investment marks | Quarterly, lumpy | $12.3B gain this quarter — a *loss* of similar magnitude is entirely possible in a down round; huge EPS swing factor |
| Debt markets / credit spreads | Ongoing | $53.4B Q1 issuance needs refinancing; rising rates hit both interest expense and AOCI (Q1 AOCI −$3.4B) |
| FCF inflection | FY2027 at earliest | Need OCF growth > capex growth; watch accrued-capex ($27.0B) conversion |

### Positioning framework
- **For long-term/quality-growth buyers:** the operating engine is arguably the strongest it has ever been (13.1% operating margin at a $181.5B quarterly revenue base). Accumulate on FCF-scared pullbacks; the FCF trough is a *cyclical* Capex story, not a demand problem — revenue accelerated to +16.6%.
- **For event/momentum traders:** the imminent Q2 print is a coin-flip on two idiosyncratic lines — (a) capex guidance and (b) mark-to-market swings. **Do not underwrite continuation of the $2.78 EPS run-rate.** A $2.78-style print with a $1.67 core means the stock's reaction will hinge on whether the market focuses on "operating income +29.6%" or "FCF negative."
- **For credit/risk-aware traders:** leverage is still low (28% D/E) but the *direction of travel* is unmistakable — watch the pace of long-term debt issuance and the after-Y5 $45B maturity wall being re-laddered.
- **Key falsifier to watch:** if Q2 2026 shows revenue growth decelerating *while* capex guidance rises again *and* a negative mark-to-market, the FCF-negative + debt-funded + earnings-quality triple becomes a genuine de-rating trigger rather than a headline quirk.

---

## 9. Summary table — key points

| Category | Metric | Value | Read |
|---|---|---|---|
| **Latest quarter** | Revenue (Q1'26) | $181,519M, +16.6% YoY | 🟢 Accel. growth |
| | Operating income | $23,852M, +29.6% YoY | 🟢 Best-quality line |
| | Operating margin | 13.14% (+132 bps) | 🟢 Expanding |
| | Gross margin | 51.8% (+120 bps) | 🟢 Mix/leverage |
| | Diluted EPS | $2.78 (+74.8%) | 🟡 ~$1.09/share non-operating |
| | **Clean EPS est.** | **~$1.67–1.70** | 🟢 Still ~+20% YoY |
| | Other non-operating income | $15,647M (incl. $12,328M MTM) | 🔴 Non-recurring / non-cash |
| | Non-marketable equity securities | $48.1B (from $16.2B) | 🟡 Lumpy MTM risk both ways |
| | Interest expense | $800M, +48% | 🔴 Compounding drag |
| | Effective tax rate | 24.0% (vs 21.0%) | 🔴 300 bps EPS headwind |
| | D&A | $18,945M, +32.8% | 🔴 Capex depreciation arriving |
| | SBC | $4,032M, +9.3% | 🟡 Tailwind may be ending |
| **Annual** | Costs & expenses FY25 | $636,949M, +11.9% | 🟡 Re-accelerating |
| | SBC FY23→FY25 | $24,023M → $19,467M | 🟢 −18.9% |
| | Net income TTM | $90,798M, +37.7% | 🟢 |
| | FY2025 net income (derived) | ≈$77,670M | 🟡 Derived, not disclosed |
| | OCI FY2025 | ≈+$28,264M | 🟡 Large unrealized gains |
| | D&A TTM | $70,439M, +27.2% | 🔴 |
| **Cash flow** | OCF TTM | $148,531M | 🟢 |
| | **Capex TTM** | $151,003M | 🔴 24.4% of Q1 revenue |
| | Q1'26 capex | $44,203M, +76.7% | 🔴 Accelerating |
| | **FCF TTM** | **−$2,472M** | 🔴 **Negative** |
| | FY FCF (23/24/25) | 32,217 / 32,878 / **7,695** | 🔴 Collapsing |
| | Accrued-not-yet-paid capex | $27.0B (FY25) vs $16.8B | 🔴 More capex coming |
| | Cash taxes TTM | $8,741M | 🟡 ≪ book tax |
| | Deferred tax expense TTM | $23,761M | 🟡 Book≫taxable income |
| **Balance sheet** | Cash + securities | $144,016M | 🟢 Fortress |
| | Total assets / equity | $916,630M / ~$433,956M | 🟢 |
| | **Long-term debt** | **$122,632M (+78% QoQ)** | 🔴 Regime change |
| | LTD issued Q1'26 | $53,441M (vs $15,673M all FY25, $0 in FY23/24) | 🔴 Debt-funded capex |
| | Debt/equity | ~28% (52% incl. leases) | 🟢 Still modest |
| | Net debt incl. leases | ~$83.6B | 🟢 Manageable |
| | Current ratio | 1.18x | 🟡 Amazon-normal |
| | Inventory | $36,534M, −$1,791M QoQ | 🟢 |
| | Book value/share | ~$40.4 | 🟢 |
| | TTM ROE | ~21.7% | 🟢 |
| **Obligations** | Total contractual obligations | **$569,280M** | 🟡 AI commitment scale |
| | Next 12 months | $57,065M | 🟡 |
| | Operating lease payments (undisc.) | $110,135M | 🟡 |
| | Unrecognized SBC | $14,400M | 🟡 |
| | LTD due after Year 5 | $45,000M | 🟡 Watch re-laddering |
| **Segments** | Reportable segments | 3 (NA, Int'l, AWS) | — |
| **Insider** | Transactions | **DATA UNAVAILABLE — not inferred** | ⚪ |
| **Catalyst** | Q2 2026 results | Imminent / not yet filed | 🔴 Event risk |
| **Bottom line** | | Operating engine at record strength, but FCF negative, capex accelerating, earnings boosted ~⅓ by non-cash marks, and funded increasingly by debt | 🟡 **Constructive on operations, cautious on reported EPS quality & FCF** |