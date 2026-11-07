# AMZN — Fundamental Deep Dive (data as of 2026‑08‑20)

**Primary source:** Amazon.com, Inc. Form 10‑Q for the quarter ended **2026‑06‑30**, filed **2026‑07‑31** (accession 0001018724‑26‑000026); prior-period comparisons from the 10‑Q filed 2026‑04‑30 (accession 0001018724‑26‑000014). All figures are point‑in‑time SEC facts available on or before 2026‑08‑20.

---

## 1. Executive summary — what the numbers actually say

1. **The core business is compounding faster than at any point in recent memory.** H1'26 revenue was **$382.1B (+18.2% YoY)** and Q2'26 revenue **$200.6B (+19.6% YoY, accelerating from +16.6% in Q1'26)**.
2. **Operating leverage is real.** Q2'26 operating income **$27.5B, +43.2% YoY**, with operating margin expanding **11.4% → 13.7%** (+231 bp). H1'26 op margin 13.4% vs 11.6%.
3. **But headline EPS is heavily flattered by a non-cash revaluation.** Q2'26 non‑operating income was **$53.4B**, of which **$50.5B** is an "upward price adjustment" on equity securities with no readily determinable fair value (H1'26: **$62.8B**). Diluted EPS of **$5.75** implies underlying/core EPS of only **≈$2.18**. Traders must separate these.
4. **Amazon is now a negative-free-cash-flow company.** TTM capex **$173.0B** vs TTM operating cash flow **$161.4B** → **TTM FCF −$11.6B** (vs **+$13.5B** in the prior TTM period). Q2'26 capex alone was **$54.2B = 27.0% of quarterly revenue**.
5. **The capex supercycle is being debt-funded.** Total debt nearly **doubled in six months** ($68.8B → $133.0B); TTM long-term debt issuance **$81.9B**; interest expense **+100% YoY** in H1 and **+155%** in Q2.
6. **Balance sheet is still liquid and profitable, not stressed.** Cash + marketable securities **$176.1B**; net cash positive ex-leases; interest coverage ~21x. This is an investment cycle, not a solvency story.

**Net read:** fundamentally improving operations masked/diluted by a capital-intensity shock and a very noisy P&L. The right signal to trade is **operating income and AWS/capex commentary**, not GAAP EPS.

---

## 2. Company profile & reporting structure

Amazon.com, Inc. (AMZN) is a global technology and logistics conglomerate spanning (a) online and physical retail plus third‑party marketplace, (b) Prime subscription, advertising and other monetization services, (c) Amazon Web Services (cloud compute, storage, database, AI/ML infrastructure and services), and (d) devices/content. The 10‑Q explicitly confirms **3 operating segments** (`NumberOfOperatingSegments = 3`): **North America, International, Amazon Web Services**. Segment-level revenue/operating-income tables were **not** included in the data package, so the segment analysis below is limited to group-level inference (capex, leases, power contracts, AI-related equity positions).

Two structural data points confirm the "AI infrastructure build-out" thesis:
- **Energy derivatives:** notional **270 million MWh** of electricity contracts in H1'26, with derivative assets jumping **$112M → $705M** — power procurement at data-center scale.
- **Non-marketable equity securities** exploded **$16.2B → $122.3B** in six months, with **$62.8B of upward revaluations recognized through income**. That is a concentrated, model-valued AI-related asset equal to **11.2% of total assets**.

---

## 3. Income statement analysis (derived)

*Note: the vendor dataset carries no `Revenues` tag. Revenue below is derived as `CostsAndExpenses + OperatingIncomeLoss`, which ties exactly to reported costs and margins.*

| $M | Q2'26 | Q2'25 | YoY | Q1'26 | H1'26 | H1'25 | YoY |
|---|---|---|---|---|---|---|---|
| Revenue (derived) | 200,606 | 167,702 | **+19.6%** | 181,519 | 382,125 | 323,369 | **+18.2%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 87,463 | 183,241 | 157,785 | +16.1% |
| Gross profit | 104,828 | 86,893 | +20.6% | 94,056 | 198,884 | 165,584 | +20.1% |
| **Gross margin** | **52.3%** | 51.8% | +45 bp | 51.8% | **52.1%** | 51.2% | +84 bp |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 157,667 | 330,812 | 285,793 | +15.8% |
| G&A | 2,788 | 2,965 | **−6.0%** | 2,587 | 5,375 | 5,593 | −3.9% |
| Marketing | 11,698 | 11,416 | +2.5% | 10,314 | 22,012 | 21,179 | +3.9% |
| Operating lease cost | 4,118 | 3,426 | +20.2% | 3,917 | 8,035 | 6,666 | +20.5% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** | 23,852 | **51,313** | 37,576 | **+36.6%** |
| **Operating margin** | **13.7%** | 11.4% | +231 bp | 13.1% | **13.4%** | 11.6% | +181 bp |
| Interest expense | 1,314 | 516 | **+155%** | 800 | 2,114 | 1,057 | **+100%** |
| Interest income | 1,295 | 1,085 | +19% | 1,135 | 2,430 | 2,151 | +13% |
| Other non-operating (equity revaluations, FX, warrants) | 53,396 | 1,686 | nm | 15,982 | **69,378** | 4,960 | nm |
| Pre-tax income | 80,857 | 20,857 | +288% | 39,834 | 120,691 | 42,536 | +184% |
| Income tax expense | 18,199 | 2,678 | +580% | 9,560 | 27,759 | 7,231 | +284% |
| **Effective tax rate** | 22.5% | 12.8% | — | 24.0% | **23.0%** | 17.0% | — |
| **Net income** | **62,647** | 18,164 | +245% | 30,255 | **92,902** | 35,291 | +163% |
| Diluted EPS | **$5.75** | $1.68 | +242% | $2.78 | **$8.53** | $3.27 | +161% |

### Earnings-quality work (the most important adjustment)

| $M | Q2'26 | H1'26 |
|---|---|---|
| Non-marketable equity "upward price adjustment" | 50,486 | 62,814 |
| After-tax (@23%) | ~38,874 | ~48,367 |
| **Net income excluding revaluation** | **~23,773** | **~44,535** |
| **Implied "core" diluted EPS** | **≈$2.18** | **≈$4.09** |
| Reported diluted EPS | $5.75 | $8.53 |
| **Reported vs core EPS inflation** | **+164%** | **+109%** |
| **Core EPS growth YoY** | **≈+30%** | **≈+25%** |

Additional P&L observations:
- **Cash taxes are running far below book tax.** H1'26 income taxes paid **$3.98B** vs tax expense **$27.76B**; deferred tax expense **$30.5B** in H1. The gap is largely the non-cash equity gain creating a deferred tax liability — i.e., **no cash cost today**, but a future tax liability.
- **G&A actually declined** (−6% Q2) — genuine cost discipline.
- **Depreciation & amortization: $19.99B in Q2'26 (+31.3% YoY)** and **$38.9B in H1 (+32.0%)**; D&A is now **10.0% of revenue** vs 9.1% a year ago. This is the leading edge of the capex wave hitting the P&L — a structural margin headwind for 2026‑2027.
- **SBC**: $6.04B Q2'26 / $10.07B H1'26 (flattish YoY, muted vs revenue growth); **$24.8B of unrecognized SBC** remains.
- **Interest expense growth (+155% YoY)** now outpaces interest income growth — net interest income is becoming a smaller contributor. Q2'26 net interest was roughly **−$19M** (essentially breakeven), versus **+$569M** in Q2'25.

---

## 4. Balance sheet

| $M | 2026‑06‑30 | 2025‑12‑31 | Δ |
|---|---|---|---|
| Cash & equivalents | 78,213 | 86,810 | −8,597 |
| Marketable securities (AFS) | 97,900 | 45,800 | **+52,100** |
| **Total cash + securities** | **176,113** | **132,610** | **+43,503** |
| Accounts receivable (net) | 88,092 | 67,729 | **+30.1%** |
| Allowance for doubtful accounts | 2,800 | 2,400 | +16.7% (3.2% of AR) |
| Inventory | 38,184 | 38,325 | **−0.4%** |
| Current assets | 249,264 | 229,083 | +8.8% |
| **Total assets** | **1,095,689** | **818,042** | **+33.9%** |
| Accounts payable | 147,440 | 121,909 | +20.9% |
| Accrued liabilities | 73,406 | 75,520 | −2.8% |
| Current liabilities | 241,274 | 218,005 | +10.7% |
| Long-term debt (current + non-current) | **132,224** | 68,396 | **+93.3%** |
| Long-term debt (aggregate tag) | 132,995 | 68,836 | +93.2% |
| Finance lease liabilities | 13,451 | 12,286 | +9.5% |
| Operating lease liabilities | **96,320** | 89,252 | +7.9% |
| Contract liabilities (deferred revenue) | 24,928 | 25,000 | −0.3% |
| Non-marketable equity securities | **122,300** | 16,200 | **+654.9%** |
| AOCI | 66,287 | 28,223 | **+38,064** |
| Additional paid-in capital | 149,619 | 140,024 | +9,595 |
| Shares outstanding (M) | 10,783 | 10,731 | +0.5% |

**Key balance-sheet takeaways**
- **Current ratio 1.03x** (249,264/241,274), down from 1.05x — thinner but adequate for a company with Amazon's negative working-capital cycle.
- **The $277.6B asset increase in six months decomposes into: ~$106B non-marketable equity revaluation, ~$64B new debt, ~$52B securities build (+$98.4B gross capex), plus AOCI.** This is a balance sheet transformed in half a year.
- **Receivables are the item to watch:** +30.1% in six months vs +19.6% revenue growth. Q2'26 AR represents ~40 days of quarterly revenue vs ~30 days at 6/30 year-end levels (seasonal, but the growth rate warrants monitoring for AWS/advertising collection and channel mix).
- **Inventory flat while revenue grew ~19%** — an unambiguous efficiency positive.
- **Leverage (derived, labeled as an estimate since total liabilities are not disclosed in the dataset):** with equity estimated at roughly **$460–470B** (APIC $149.6B + AOCI $66.3B + accumulated retained earnings of roughly $250B, no meaningful buybacks historically), implied total liabilities ≈ **$630B** and **debt/equity ≈ 1.3x**. Including the $96.3B of operating leases, adjusted leverage is materially higher.

---

## 5. Cash flow, capex and financing — the crux of the thesis

| $M | Q2'26 | Q2'25 | H1'26 | H1'25 | TTM (Jul'25–Jun'26) | Prior TTM |
|---|---|---|---|---|---|---|
| Operating cash flow | 45,387 | 32,515 | **71,419** | 49,530 | **161,403** | 121,137 |
| Capex (productive assets) | (54,208) | (32,183) | **(98,411)** | (57,202) | **(173,028)** | (107,656) |
| **Free cash flow** | **(8,821)** | +332 | **(26,992)** | (7,672) | **(11,625)** | **+13,481** |
| Business acquisitions (net of cash) | (24,359) | (1,700) | **(39,767)** | (1,652) | (41,956) | (4,809) |
| Purchases of marketable securities | (26,006) | (17,797) | (49,262) | (31,130) | (72,902) | (46,731) |
| Proceeds from LT debt issuance | 13,557 | 0 | **66,998** | 746 | **81,925** | 746 |
| Proceeds from ST debt | 9,368 | 2,093 | 15,386 | 3,908 | 20,798 | 8,187 |
| LT debt repayments | (2,752) | (2,751) | (2,752) | (2,751) | (5,022) | (7,434) |
| Net investing cash flow | (79,245) | (39,424) | (143,457) | (69,227) | (216,775) | (123,569) |
| Net financing cash flow | +10,146 | (2,539) | **+62,913** | (2,586) | **+75,160** | (8,652) |

**Interpretation**
- **Operating cash flow is genuinely strong**: +44% in H1 and +33% on a TTM basis — the earnings engine is throwing off more cash before growth investment.
- **But capex has outrun it.** TTM capex **+60.7%** vs TTM OCF **+33.3%**. Q2'26 annualized capex run-rate ≈ **$217B**. Capex/revenue reached **27.0% in Q2'26** vs 19.2% a year ago and ~17.7% in H1'25.
- **Financing has flipped decisively to debt.** Net financing swung from −$8.7B (prior TTM) to **+$75.2B**, funded almost entirely by **$81.9B of long-term notes plus $20.8B of short-term borrowings**. Net long-term issuance of ~$77B in a single year is unprecedented for AMZN.
- **Strategic deployment is accelerating too**: **$39.8B** of cash for business acquisitions in H1'26 (vs $1.7B a year earlier), plus the **$106B** revaluation-driven growth in non-marketable equity. Amazon is buying/backing AI capacity on both the M&A and the equity-stake route.
- **Watch the operating-lease bucket**: op-lease payments **$15.5B TTM** (+15%), undiscounted commitments **$116.4B**, and the weighted-average discount rate ticked **3.7% → 3.9%** — quietly rising occupancy/power/site cost, and a discount-rate sensitivity to rates.

---

## 6. Commitments and off-balance-sheet items

| $M at 2026‑06‑30 | Amount |
|---|---|
| Total contractual obligations (multi-year purchase/other commitments) | **650,034** |
| Due within next 12 months | **78,084** |
| Due in year 2 | 53,406 |
| Due in year 3 | 46,767 |
| Due in year 4 | 42,219 |
| Remainder of fiscal 2026 | 42,752 |
| Operating lease payments (undiscounted) | 116,350 |
| Finance lease payments (undiscounted) | 16,660 |
| Other commitments (remainder of FY) | 2,145 |

**Total contractual obligations of $650.0B — roughly 60% of total assets and ~1.4x estimated book equity — is the single largest quantitative risk factor in this dataset.** Only **$78.1B** falls due within twelve months, so near-term liquidity is fine, but these commitments (consistent with multi-year AI/data-center capacity, power, and content deals) lock in the capex/supply-cost trajectory well beyond the current year. If AI demand growth decelerates, this is where the operating leverage reverses.

---

## 7. Insider transactions

**DATA_UNAVAILABLE.** The authorized point-in-time insider-transaction archive has no coverage for AMZN as of 2026‑08‑20. I will not infer or fabricate insider activity. Treat insider sentiment as an **information gap** for this report; obtain Form 4 data independently before making any "smart money" argument.

---

## 8. Data limitations you should know about

- **No revenue line item** in the vendor feed — revenue is derived (`CostsAndExpenses + OperatingIncomeLoss`) and ties exactly, but do not mix it with vendor "revenue" prints.
- **No segment-level revenue/operating income**, no balance-sheet `StockholdersEquity`/`Liabilities` totals, no share-repurchase/dividend line items, and no debt-maturity schedule in the package. Equity and total liabilities are therefore **derived estimates**, clearly labeled.
- The `annual` and `quarterly` endpoints returned the **same 10‑Q tag set** — meaning **no FY2025 10‑K facts are present**. Full-year 2025 figures are therefore **not verified** here; FY2025 net income can be inferred at ≈$77.7B (H1'25 $35.3B + H2'25 $42.4B implied from TTM roll-forward), but treat as an inference.
- **No price or market-cap data** was available, so **no P/E, EV/EBITDA, or P/FCF multiples are computed**. Any valuation statement in a downstream model must be sourced separately.

---

## 9. Actionable insights for traders

**Bullish evidence (own the operating story)**
- Revenue growth **accelerating** (16.6% → 19.6% QoQ progression) with **gross margin at 52.3%** and **operating margin +231 bp YoY**. This is the classic Amazon "margin expansion on a reaccelerating top line" setup.
- **Operating income +43% YoY**; Q2'26 $27.5B vs $19.2B. If you model AMZN, model operating income — it is the cleanest single number in this filing.
- **G&A down 6%, inventory flat while revenue +19.6%, OCF +44% H1** — internal efficiency is not being sacrificed for growth.
- **$176.1B of cash + securities** and ~21x interest coverage give enormous headroom to keep funding the build-out without distress.

**Bearish / de-rating evidence (respect the capital cycle)**
- **TTM FCF is −$11.6B** (from +$13.5B) and Q2'26 was the first quarter in over a year with negative FCF. Capex run-rate ~$217B. FCF-based valuation frameworks break down here.
- **Debt nearly doubled in six months** and interest expense is compounding at +100–155%. Refinancing and rate sensitivity now matter for AMZN in a way they haven't historically.
- **Earnings quality is the biggest trap:** ~64% of Q2'26 net income is a non-cash mark-up of a $122.3B illiquid equity stake. Headline EPS beat ($5.75 vs ~$2.18 core) will look spectacular but is not repeatable or cash-generative, and **is reversible** if those private marks reset. Expect the market to punish any quarter where revaluations reverse.
- **$650B of contractual obligations** + **$96.3B operating leases** + D&A growing 31% = a fixed-cost base that turns on management if revenue growth dips below ~15%.
- **Receivables +30% vs revenue +19.6%** — a legitimate yellow flag for collections/mix.
- The **$38.1B H1'26 OCI gain** (comprehensive income $131.0B vs net income $92.9B) is a second large, unexplained-by-AFS mark embedded in AOCI ($66.3B = ~14% of estimated book equity). If it's mark-to-model, it's a second reversal channel.

**How to trade it**
1. **Trade the operating income print, ignore the GAAP EPS headline.** Recompute "core EPS" (≈$2.18 for Q2'26) every quarter and compare it to consensus operating income. A beat driven by equity revaluations should be faded; a beat driven by AWS margin should be bought.
2. **Set an explicit capex/FCF tripwire.** Watch Q3'26 capex vs the ~$54B/quarter pace and the trajectory of TTM FCF. The bull case survives capex up to roughly the current run-rate as long as OCF grows ~30%+; a capex guide-up **without** an offsetting OCF acceleration is the de-rating trigger.
3. **Monitor the debt/financing line every quarter.** Long-term issuance of $82B in TTM plus rising interest expense means a further large raise (or a shift to commercial paper) signals the build-out is outrunning even Amazon's cash generation. Interest expense +150% YoY is unsustainable if it persists for another 2–3 quarters.
4. **Watch D&A as the canary.** D&A is +31% YoY and 10.0% of revenue. If D&A growth continues at 30% while revenue growth slips toward 15%, operating margin expansion reverses mechanically — that is the most likely path to a negative fundamental surprise.
5. **Treat the $122.3B non-marketable equity position as an embedded AI option, and size it as such.** It is worth ~26% of estimated book equity and it moves reported earnings by billions per quarter. Any news flow around that underlying asset is an AMZN P&L event, not just a portfolio event.
6. **Insider data is missing** — don't build a position thesis on insider buying/selling here. Re-verify externally.

**Suggested stance (fundamental, no price input):** **Constructive on the operating business, cautious on the reported-earnings quality and the balance-sheet trajectory.** The optimal expression is long bias with explicit risk controls around the next capex guide and any equity-mark reversal — not an unqualified "EPS beats, buy the stock" reaction.

---

## 10. Key-points summary table

| Category | Metric | Latest (6/30/26 or LTM) | Prior / YoY | Signal |
|---|---|---|---|---|
| **Growth** | Q2'26 revenue (derived) | $200,606M | +19.6% YoY | 🟢 Accelerating |
| | H1'26 revenue | $382,125M | +18.2% YoY | 🟢 |
| | Q1→Q2'26 growth seq. | 181,519 → 200,606 | +10.5% QoQ | 🟢 |
| **Profitability** | Q2'26 operating income | $27,461M | +43.2% YoY | 🟢 |
| | Q2'26 operating margin | 13.7% | +231 bp | 🟢 |
| | H1'26 operating margin | 13.4% | +181 bp | 🟢 |
| | Q2'26 gross margin | 52.3% | +45 bp | 🟢 |
| | Q2'26 G&A | $2,788M | −6.0% YoY | 🟢 Cost discipline |
| **Earnings quality** | Reported Q2'26 diluted EPS | $5.75 | +242% YoY | 🟡 Flattered |
| | Core diluted EPS (ex-revaluation) | **≈$2.18** | ≈+30% YoY | 🟡 True run-rate |
| | Equity "upward price adjustment" | $50.5B (Q2) / $62.8B (H1) | vs $0.05B Q2'25 | 🔴 Non-cash, reversible |
| | H1'26 cash taxes paid vs expense | $3,978M vs $27,759M | 14% of book tax | 🟡 Deferred |
| | Effective tax rate | 23.0% (H1'26) | vs 17.0% | 🟡 |
| **Cash flow** | TTM operating cash flow | $161,403M | +33.3% | 🟢 |
| | TTM capex | $173,028M | +60.7% | 🔴 |
| | **TTM free cash flow** | **−$11,625M** | from +$13,481M | 🔴 |
| | Q2'26 capex / revenue | 27.0% | vs 19.2% | 🔴 |
| | H1'26 business acquisitions | $39,767M | from $1,652M | 🟡 Strategic |
| **Balance sheet** | Cash + marketable securities | $176,113M | +$43,503M | 🟢 |
| | Total debt | $132,224M (agg. $132,995M) | +93.3% in 6M | 🔴 |
| | Finance + operating leases | $13,451M + $96,320M | +9.5% / +7.9% | 🟡 |
| | Current ratio | 1.03x | vs 1.05x | 🟡 |
| | Total assets | $1,095,689M | +33.9% in 6M | 🟡 Revaluation-driven |
| | Non-marketable equity securities | $122,300M | +654.9% in 6M | 🟡 11.2% of assets |
| | AOCI | $66,287M | +$38,064M | 🔴 Mark-to-model risk |
| | Accounts receivable | $88,092M | +30.1% in 6M | 🟡 Watch |
| | Inventory | $38,184M | −0.4% in 6M | 🟢 |
| **Leverage / cost** | H1'26 interest expense | $2,114M | +100% YoY | 🔴 |
| | Q2'26 interest expense | $1,314M | +155% YoY | 🔴 |
| | Interest coverage (EBIT/interest) | ~21x | still strong | 🟢 |
| | TTM D&A | $75,200M | +28.4% | 🟡 Margin headwind |
| **Commitments** | Total contractual obligations | $650,034M | — | 🔴 Key risk |
| | Due within 12 months | $78,084M | — | 🟡 Manageable |
| **Other** | TTM SBC | ~$10.1B (H1) | flat | 🟢 |
| | Unrecognized SBC | $24,800M | — | 🟡 Future dilution |
| | Shares outstanding | 10,783M | +0.5% in 6M | 🟢 |
| | Power contracts (H1'26) | 270M MWh notional | — | 🟡 AI build-out |
| **Gaps** | Insider transactions | **Unavailable** | — | ⚪ No data |
| | Price / valuation multiples | **Unavailable** | — | ⚪ No data |
| | Segment-level P&L | **Unavailable** | — | ⚪ No data |
| | FY2025 10-K facts | **Not in feed** | — | ⚪ Use with caution |

**Bottom line on AMZN:** the operating franchise is performing at its best in years — accelerating revenue, 13.7% operating margins, +43% operating income, strong OCF and a fortress liquidity position. But H1'26 was also the half in which Amazon became a **negative-FCF, debt-funded, $200B+ annual capex company** with **64% of quarterly net income coming from a non-cash mark-up of a single illiquid AI-adjacent equity stake**. Lean on operating income, gross margin and AWS capex commentary; discount the EPS headline; and treat the $650B commitment schedule and the $122B mark-to-model asset as the two swing factors that determine whether this is a multi-year compounding story or an air pocket.