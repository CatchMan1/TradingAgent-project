# AMZN — Fundamental Deep Dive
**Report date: 2026-08-07 | Company: Amazon.com, Inc. (AMZN) | Latest filing: Q2 FY2026 Form 10-Q, filed 2026-07-31 (accession 0001018724-26-000026)**

---

## 0. Data provenance, scope and hard limitations (read first)

| Item | Status |
|---|---|
| Point-in-time SEC XBRL facts, filtered by EDGAR acceptance timestamp ≤ 2026-08-07 | ✅ Available (Q2 FY26 10-Q filed 07/31/26; Q1 FY26 10-Q filed 04/30/26) |
| Income statement, balance sheet, cash flow detail | ✅ Available **quarterly**, 4–6 periods (Q1'25 → Q2'26) |
| Multi-year annual history (FY2023–FY2025 full-year statements) | ❌ **Not returned** — the vendor's `annual` pull returned the same quarterly XBRL fact set. I will not fabricate annual history. |
| Segment-level P&L (North America / International / AWS) | ❌ Not in fact set (only `NumberOfOperatingSegments = 3`) |
| Revenue line item | ⚠️ Tag absent; **derived** as `CostsAndExpenses + OperatingIncomeLoss`. Method validated against Q2'25 and H1'25 actuals (matches reported Amazon revenue of $167.7B / $323.4B) |
| **Insider transactions** | ❌ `DATA_UNAVAILABLE` — the data package has **no authorized point-in-time insider archive for AMZN**. **No insider inference is made or should be read into this report.** |
| Share price / market cap / multiples | ❌ Not in this tool set; earnings-base anchors provided instead |

---

## 1. Executive summary — what changed this week

AMZN filed its Q2 FY2026 10-Q on **2026-07-31**, and the print is a **tale of two companies**:

1. **The operating business is accelerating and gaining margin leverage.** Derived Q2'26 revenue was **~$200.6B (+19.6% y/y)**, operating income **$27.46B (+43% y/y)**, operating margin **13.7% vs 11.4%**. Gross margin expanded to **52.3%**. Opex grew only 14.2% against 19.6% revenue growth.
2. **Reported EPS is dominated by non-operating investment marks, not operations.** Q2'26 GAAP diluted EPS was **$5.75 vs $1.68**, but **$53.4B of the $80.9B pretax income was non-operating**, including a **$50.49B upward price adjustment on non-marketable equity securities**. Core (operating-only) EPS was roughly **$2.0**. **~65% of reported Q2 EPS is a mark, not cash flow.**
3. **The balance sheet has been levered up aggressively to fund an AI capex cycle and M&A.** Long-term debt rose from **$68.8B → $133.0B (+$64.2B, +93%)** in six months. Interest expense **doubled y/y** in Q2. Capex hit **$54.2B in a single quarter** and **$173.0B trailing twelve months** — greater than TTM operating cash flow of **$161.4B**.
4. **Free cash flow is negative.** H1'26 FCF ≈ **–$27.0B** vs **–$7.7B** in H1'25. TTM FCF ≈ **–$11.6B**. This is a deliberate, debt-and-OCI-funded reinvestment phase, not a demand problem.
5. **A new ~$122B private-investment asset has appeared on the balance sheet** (from $16.2B at 12/31/25), of which **$62.8B of gains were recognized in H1 earnings**. This is now ~11% of total assets and the single largest swing factor in reported EPS — and it is a **non-cash, valuation-opinion-driven** number.

**Net:** fundamentally the *operating* franchise is the strongest it has ever been (record margins at record scale), but **earnings quality has deteriorated sharply** and **financial risk has risen via debt-funded capex**. Position sizing should respect that gap.

---

## 2. Company profile

Amazon.com, Inc. operates **three reportable segments** (confirmed: `NumberOfOperatingSegments = 3`): **North America**, **International**, and **Amazon Web Services (AWS)**. Revenue streams span online and physical retail, third-party seller services (1P/3P marketplace, fulfillment, ads), subscription (Prime), advertising, and AWS cloud infrastructure plus a growing custom-silicon (Trainium/Inferentia) and AI-platform business. The company is a serial investor in private AI/technology companies, and — as of Q2 FY26 — that investment book has become financially material, generating more earnings volatility than the retail or cloud segments.

`EntityCommonStockSharesOutstanding` as of **2026-07-22**: **10,786,313,572** shares. Shares issued 11.298B, outstanding 10.783B (≈515M treasury).

---

## 3. Income statement — Q2 FY2026 (Apr–Jun 2026) and sequential build

### 3.1 Derived P&L (all $B)

| Line | Q2 FY26 | Q2 FY25 | Δ y/y | Q1 FY26 | Q1 FY25 | Δ y/y |
|---|---:|---:|---:|---:|---:|---:|
| **Revenue** (derived) | **200.61** | 167.70 | **+19.6%** | 181.52 | 155.67 | **+16.6%** |
| Cost of goods & services | 95.78 | 80.81 | +18.5% | 87.46 | 76.98 | +13.6% |
| **Gross profit** | **104.83** | 86.89 | **+20.7%** | 94.06 | 78.69 | +19.5% |
| **Gross margin** | **52.3%** | 51.8% | +50bp | 51.8% | 50.5% | +130bp |
| Total costs & expenses | 173.15 | 148.53 | +16.6% | 157.67 | 137.26 | +14.9% |
| **Operating income** | **27.46** | 19.17 | **+43.2%** | 23.85 | 18.41 | +29.6% |
| **Operating margin** | **13.7%** | 11.4% | **+230bp** | 13.1% | 11.8% | +130bp |
| Non-operating income | **53.40** | 1.69 | nm | **15.98** | 3.27 | nm |
| Pretax income | **80.86** | 20.86 | +288% | 39.83 | 21.68 | +84% |
| Income tax | 18.20 | 2.68 | nm | 9.56 | 4.55 | nm |
| **Effective tax rate** | **22.5%** | 12.8% | +970bp | **24.0%** | 21.0% | +300bp |
| **Net income** | **62.65** | 18.16 | **+245%** | 30.26 | 17.13 | +77% |
| Diluted EPS | **$5.75** | $1.68 | +242% | $2.78 | $1.62 | +72% |
| Basic EPS | $5.82 | $1.71 | | $2.82 | $1.61 | |
| Diluted shares (implied) | ~10.90B | ~10.81B | +0.8% | ~10.89B | | |

### 3.2 H1 FY2026 aggregate

| Line | H1 FY26 | H1 FY25 | Δ |
|---|---:|---:|---:|
| Revenue | **382.13** | 323.37 | **+18.2%** |
| Gross profit | 198.88 | 165.58 | +20.1% |
| Gross margin | 52.1% | 51.2% | +90bp |
| Operating income | **51.31** | 37.58 | **+36.6%** |
| Operating margin | **13.4%** | 11.6% | **+180bp** |
| Non-operating income | **69.38** | 4.96 | nm |
| Pretax income | 120.69 | 42.54 | +184% |
| Tax | 27.76 | 7.23 | +284% |
| Effective tax rate | **23.0%** | **17.0%** | +600bp |
| Net income | **92.90** | 35.29 | +163% |
| Diluted EPS | **$8.53** | $3.27 | +161% |

### 3.3 Operating expense detail (where the leverage is coming from)

| Item | Q2 FY26 | Q2 FY25 | Δ | H1 FY26 | H1 FY25 | Δ |
|---|---:|---:|---:|---:|---:|---:|
| Marketing | 11.70 | 11.42 | +2.5% | 22.01 | 21.18 | +3.9% |
| G&A | 2.79 | 2.97 | **–6.0%** | 5.38 | 5.59 | **–3.9%** |
| Share-based comp | 6.04 | 6.53 | **–7.6%** | 10.07 | 10.22 | **–1.5%** |
| D&A (total) | 19.99 | 15.23 | **+31.3%** | 38.93 | 29.49 | **+32.0%** |
| — of which depreciation | 13.87 | 9.77 | +42.0% | 26.70 | 18.82 | +41.9% |
| Operating lease cost | 4.12 | 3.43 | +20.2% | 8.04 | 6.67 | +20.6% |
| Interest expense | 1.31 | 0.52 | **+154.7%** | 2.11 | 1.06 | **+100.0%** |
| Interest income | 1.30 | 1.09 | +19.4% | 2.43 | 2.15 | +13.0% |

**Read-through:** the margin story is being driven by **revenue scaling faster than the fixed cost base** (G&A down outright, marketing nearly flat, SBC down y/y — a genuinely rare combination for Amazon). Offsetting that: **depreciation is compounding at ~32–42%** as the capex program hits the P&L, and **interest expense has doubled**. Watch for D&A growth eventually outrunning gross-margin expansion — that is the structural bear case for 2027 margins.

### 3.4 Quality of earnings — the single most important analysis in this report

Q2 FY26 non-operating income of **$53.40B** broke down as:
- **$50.49B** upward price adjustment on equity securities *without readily determinable fair value* (private-company marks)
- $1.30B equity securities fair-value gains (Level 1/2)
- $1.32B marketable-securities unrealized gains
- $1.31B interest income, less $1.31B interest expense (roughly a wash)
- $0.23B FX gains, less $1.45B warrant fair-value adjustment

**"Core" reconstruction (stripping all investment marks):**

| | Q2 FY26 | Q2 FY25 | H1 FY26 | H1 FY25 |
|---|---:|---:|---:|---:|
| Operating income | 27.46 | 19.17 | 51.31 | 37.58 |
| Net interest | –0.02 | +0.57 | +0.32 | +1.09 |
| FX / warrants | –1.22 | –0.07 | –0.66 | –0.14 |
| **Core pretax** | **26.22** | 19.67 | **50.97** | 38.53 |
| Core tax @ ~23% / 17% | 6.03 | 3.34 | 11.72 | 6.55 |
| **Core net income** | **~20.2** | ~16.3 | **~39.3** | ~32.0 |
| **Core diluted EPS** | **~$1.86–2.00** | ~$1.51 | **~$3.6** | ~$3.02 |

**Conclusion: reported Q2 EPS of $5.75 overstates underlying earnings power by roughly 3x this quarter.** Core EPS growth is still a very healthy **~+20–23% y/y**, but anyone screening on the GAAP $5.75 print, TTM EPS, or "earnings surprise" magnitude is being misled. **The $62.8B H1 mark alone contributes roughly $48B after-tax, i.e. ~45% of H1 net income and ~$4.45 of the $8.53 H1 diluted EPS.**

**Actionable:** If you are modeling forward EPS, treat the **$8.0/yr-ish core run-rate** (Q2 core ~$2.0 × 4) as the true cash-earnings base and treat the investment marks as a separate, highly volatile NAV line. A reversal quarter (private AI marks down 20–30%) could produce a **GAAP EPS miss of $8–12 in a single quarter** with zero operating deterioration — a mechanical, headline-driven drawdown opportunity.

---

## 4. Balance sheet — leverage-up, AI buildout, and a new $122B asset

### 4.1 Balance sheet ($B)

| Item | 2026-06-30 | 2025-12-31 | Δ | 2026-03-31 |
|---|---:|---:|---:|---:|
| Cash & equivalents | 78.21 | 86.81 | –8.60 | 104.69 (total cash+restricted) |
| Available-for-sale debt securities | **97.90** | 45.80 | **+52.10** | — |
| Accounts receivable (net) | 88.09 | 67.73 | **+20.36 (+30.1%)** | — |
| Inventory (net) | 38.18 | 38.33 | –0.14 | — |
| **Current assets** | **249.26** | 229.08 | +20.18 | — |
| **Equity securities w/o readily determinable FV** | **122.30** | 16.20 | **+106.10** | — |
| Operating lease ROU asset | 92.74 | 86.05 | +6.69 | — |
| **Total assets** | **1,095.69** | 818.04 | **+277.65 (+33.9%)** | — |
| Accounts payable | **147.44** | 121.91 | **+25.53 (+20.9%)** | — |
| Accrued liabilities | 73.41 | 75.52 | –2.11 | — |
| **Current liabilities** | **241.27** | 218.01 | +23.26 | — |
| Long-term debt — current | 3.33 | 2.75 | +0.58 | — |
| **Long-term debt — noncurrent** | **128.89** | 65.65 | **+63.25** | — |
| **Total long-term debt** | **133.00** | 68.84 | **+64.16 (+93.2%)** | — |
| Operating lease liability (total) | 96.32 | 89.25 | +7.07 | — |
| Finance lease liability (total) | 13.45 | 12.29 | +1.17 | — |
| AOCI | **66.29** | 28.23 | **+38.06** | — |
| Additional paid-in capital | 149.62 | 140.02 | +9.60 | — |
| Shares outstanding | 10.783B | 10.731B | +0.5% | — |
| Contract liabilities (current + noncurrent) | 24.88 | 25.00 | –0.12 | — |

**Key observations:**

- **Total assets crossed $1.1 trillion, up 33.9% in six months.** Roughly **$106B of that growth is a revaluation of private equity stakes**, not operating assets — a critical distinction for anyone computing asset turns or ROA.
- **Liquidity re-allocation:** cash down $8.6B but AFS securities up $52.1B — the company is funding out of short-duration paper while cash burns. Total cash + AFS = **$176.1B**, essentially all of the AFS book matures **within one year ($96.5B)** and carries a gross unrealized loss of only **$67M** — i.e., this is a treasury ladder, not a duration bet.
- **Net debt position:** debt $133.0B + finance leases $13.5B = $146.4B vs cash+AFS $176.1B → still **~$29.7B net cash**, before counting **$96.3B of operating lease liabilities**. Balance sheet remains investment-grade-comfortable, but the direction of travel (+$64B debt in 6 months) is the story.
- **Working capital is being used as a funding source:** AP +$25.5B (+21%) while inventory is flat and revenue is +19.6%. Receivables +30.1% is faster than revenue (AWS/ads mix + linearity) — worth monitoring but not alarming given the **allowance for doubtful accounts only moved $2.40B → $2.80B** on a $88.1B book (3.2% coverage, slightly up from 3.5%→ 3.2%… actually down as a % of AR, i.e. modestly less conservative). Inventory reserves *declined* $3.30B → $3.00B — a small mark of confidence in sell-through.
- **AOCI +$38.06B in H1** while FX translation OCI was **–$1.56B**. So the AOCI build is *not* currency — it is unrealized gains (securities/investment-related) parking directly in equity, bypassing the income statement. That means **book value is now partially exposed to the same mark-to-market risk as EPS.**
- **Employee SBC not yet recognized: $24.8B** — a real future expense headwind.

### 4.2 The investment book — the new "third business"

`EquitySecuritiesWithoutReadilyDeterminableFairValueAmount`: **$16.2B → $122.3B (+$106.1B, +655%)** in six months.

Components of that move:
- **+$62.81B** recognized as **upward price adjustments in H1 earnings** ($12.33B in Q1, $50.49B in Q2)
- **~$39.77B** of cash used for **business acquisitions in H1** ($15.41B Q1, $24.36B Q2) — plus additional equity-stake purchases
- A small positive from marketable-securities/other items

**Interpretation for traders:** AMZN has effectively become a **levered, concentrated late-stage AI venture investor at scale**. $122B of Level-3 assets is ~**11% of total assets** and ~**$11.3/share**. Marks of this kind are:
- Non-cash, unauditable-by-outsiders, and lagged relative to private funding rounds
- Capable of generating multi-billion-dollar EPS swings in either direction
- **Correlated with the same AI narrative that drives the stock** → this is *not* diversification; it is **beta amplification on the AI theme in both reported earnings and book value.**

**Actionable:** Anyone hedging or shorting AMZN should understand they are short an AI-venture NAV *inside* the equity. Conversely, if private AI valuations keep stepping up, AMZN can "beat" on EPS indefinitely without operating improvement — a structural tailwind to headline numbers that momentum strategies can exploit.

---

## 5. Cash flow — capex has overwhelmed cash generation

### 5.1 Cash flow statement ($B)

| Item | Q2 FY26 | Q2 FY25 | H1 FY26 | H1 FY25 | TTM (Jul'25–Jun'26) |
|---|---:|---:|---:|---:|---:|
| **Operating cash flow** | **45.39** | 32.52 | **71.42** | 49.53 | **161.40** |
| Purchases of productive assets (capex) | **54.21** | 32.18 | **98.41** | 57.20 | **173.03** |
| **Free cash flow (OCF – capex)** | **–8.82** | +0.33 | **–26.99** | –7.67 | **–11.63** |
| Acquisitions, net of cash | **24.36** | 1.70 | **39.77** | 1.65 | **41.96** |
| Purchases of marketable securities | 26.01 | 17.80 | 49.26 | 31.13 | 72.90 |
| Proceeds from sale/maturity of securities | 24.20 | 11.44 | 41.88 | 19.18 | 67.09 |
| **Investing cash flow** | **–79.25** | –39.42 | **–143.46** | –69.23 | **–216.78** |
| LT debt issued | 13.56 | 0.00 | **66.998** | 0.75 | **81.93** |
| LT debt repaid | 2.75 | 2.75 | 2.75 | 2.75 | 5.02 |
| ST debt, net | –0.21 | +0.70 | –0.30 | +0.43 | +1.64 |
| Finance lease principal | 0.40 | 0.41 | 0.86 | 0.82 | 1.60 |
| **Financing cash flow** | **+10.15** | –2.54 | **+62.91** | –2.59 | **+75.16** |
| FX effect on cash | –0.05 | +1.01 | –0.05 | +1.42 | –0.31 |
| **Net change in cash** | **–23.77** | –8.44 | **–9.18** | –20.86 | **+19.47** |
| Cash taxes paid | 2.66 | 4.76 | **3.98** | 5.64 | **6.64** |
| Operating lease payments | 3.49 | 3.76 | 7.80 | 7.32 | 15.52 |

### 5.2 What this tells you

1. **Capex is running at a ~$200B+ annualized pace** (Q2 alone $54.2B; +68% y/y; H1 $98.4B, +72% y/y; TTM $173.0B, +61% y/y). This is the largest capital program in corporate history outside of utilities/state projects, and it is **still accelerating**.
2. **Operating cash flow growth (+39.6% y/y in Q2, +44% in H1) is excellent but structurally insufficient.** OCF/capex coverage is **0.72x** in H1'26 vs 0.87x in H1'25.
3. **The gap is being closed with debt, working capital, and low cash taxes.** H1 cash taxes of **$3.98B** on **$120.7B of pretax income (3.3%)** is a massive cash-flow subsidy — a function of the non-cash equity marks (deferred tax) plus depreciation shields. **This is the quality-of-cash-flow red flag on the *other* side of the ledger: OCF is flattered by a $23.9B gap between book tax expense ($27.76B) and cash taxes ($3.98B).** Normalize cash taxes toward book and H1 OCF would be ~$47–48B, not $71.4B.
4. **Deferred tax expense of $30.49B in H1** (vs $0.52B a year ago) confirms the earnings are accruing tax liabilities that will eventually be paid — largely tied to the investment marks and accelerated depreciation.
5. **Acquisitions are back at scale:** $39.8B in six months vs $1.7B a year ago. Combined with the equity-investment ramp, AMZN is buying growth in AI.
6. **Financing has flipped from a modest drag to a $75B inflow TTM.** AMZN is now a **net issuer of debt for the first time in years.**

---

## 6. Contractual obligations and forward commitments — the $650B number

| Obligation | 2026-06-30 | 2026-03-31 / 2025-12-31 |
|---|---:|---:|
| **Total contractual obligation** | **$650.03B** | — |
| Due in remainder of FY2026 | $42.75B | $46.49B (Q1) |
| Due next twelve months | $78.08B | — |
| Due in year 2 | $53.41B | — |
| Due in year 3 | $46.77B | — |
| Due in year 4 | $42.22B | — |
| Operating lease payments due (undiscounted) | $116.35B | $106.91B (YE25) |
| Finance lease payments due (undiscounted) | $16.66B | $14.92B (YE25) |
| Other commitments, remainder of FY | $2.15B | $2.61B (Q1) |
| Energy derivative notional purchased (H1'26) | **270 million MWh** | — |

**Insight:** The **$650B contractual obligation** — overwhelmingly **purchase commitments for compute, chips, and power** — is the forward demand signal *and* the forward risk. **$78B due within twelve months** must be funded from operating cash flow that is currently fully consumed by capex. The **270 million MWh of energy derivative notional transacted in a single half-year** is direct, quantified evidence of the scale of the datacenter power buildout — a data point almost nobody screens for, and a strong corroborator that the capex is capacity-driven, not speculative.

**Trading implication:** AMZN has ~2.5–3 years of visibility on contracted capacity spend. That argues the **capex ramp is durable (bearish for near-term FCF, bullish for 2028+ revenue inflections)** and that **management is unlikely to guide capex down materially** — meaning any "capex discipline" rally is a low-probability catalyst.

---

## 7. Insider transactions

**Not available.** The data package contains **no authorized, point-in-time insider-transactions archive for AMZN as of 2026-08-07**, and the tool explicitly returns `DATA_UNAVAILABLE` with instructions not to infer or fabricate. **This report therefore makes no claim — bullish or bearish — about insider buying or selling.** Any assessment of insider conviction must be sourced separately (Form 4 filings on EDGAR) before being used in a trading decision.

---

## 8. Fundamental scorecard: bull case vs. bear case

### 🟢 Bull case (operating fundamentals)
- **Revenue +19.6% y/y at $200B+/quarter scale** — accelerating from +16.6% in Q1. Few companies of this size have ever re-accelerated.
- **Operating margin 13.7%, +230bp y/y**, on genuine cost discipline: G&A **–6%**, SBC **–8%**, marketing **+2.5%** vs revenue **+19.6%**.
- **Gross margin 52.3%** — mix shift toward AWS, advertising, and third-party services continues.
- **Net cash position ~$29.7B** even after $64B of new debt; interest coverage **20.9x** in Q2.
- **Cash + AFS of $176.1B** is ample liquidity against $78B of near-term obligations.
- **Contractual obligations of $650B** and 270 GWh-scale energy contracting = multi-year demand visibility.
- **Equity investment book ($122.3B)** is an unappreciated, embedded AI-venture NAV.

### 🔴 Bear case (quality and funding)
- **~65% of Q2 EPS and ~45% of H1 EPS is non-cash investment revaluation**, not operations. Core EPS ~$2.0 vs $5.75 reported.
- **FCF is negative: –$27.0B in H1, –$11.6B TTM.** Capex +72% y/y with no sign of deceleration.
- **Debt +93% in six months; interest expense +155% y/y in Q2.** Direction of travel matters even from a strong starting point.
- **Cash taxes at 3.3% of pretax income** flatter OCF; deferred tax expense of $30.5B is a future cash claim.
- **Effective tax rate up 600bp to 23%** — a persistent earnings headwind.
- **AOCI +$38B / investment marks in equity** mean book value shares the same mark-to-market fragility as EPS.
- **11% of total assets are Level-3 private marks.** A funding-round reset in private AI would hit EPS and book value simultaneously — and the stock trades with the same narrative.

---

## 9. Specific, actionable insights for traders

1. **Anchor on core EPS, not GAAP EPS.** Use **~$2.0/quarter core** (~$8.0 annualized) as the valuation base. If consensus is built on the GAAP $5.75-style print, **forward estimates are materially too high and a "beat" driven by marks should be faded, not chased.**
2. **Trade the mark-to-market asymmetry.** Because $122B of private marks are non-cash and staged, **any private-AI valuation reset produces a huge GAAP miss with no operating change.** Consider: this creates a *mechanical* buy-the-dip setup on a headline EPS miss, and conversely a *sell-premium* setup after a mark-driven beat. Watch for announcements of new private AI funding rounds as a leading indicator of AMZN's next GAAP "beat."
3. **Monitor the FCF trajectory as the primary fundamental variable.** The single number to track each quarter is **OCF minus capex**. Q2 was **–$8.8B**. Improvement toward breakeven (management guiding capex discipline, or OCF acceleration) is the highest-conviction re-rating catalyst. Continued deterioration on rising debt is the highest-conviction de-rating catalyst.
4. **Watch depreciation vs. gross-margin expansion.** Depreciation grew **+42% y/y** in Q2. As the $173B TTM capex base depreciates (mostly 5–6 year server lives), D&A grows ~$30–35B/yr. **Gross-margin expansion must exceed +~150bp/yr just to hold operating margin flat from 2027.** This is the core of the medium-term argument.
5. **Interest expense is now a monitorable line item.** $1.31B/quarter and doubling y/y. If debt reaches ~$180–200B, interest expense approaches $8–10B/yr and begins to matter to core EPS at the margin. Also flag: **any credit-rating action** would be a genuine, non-narrative shock for a company that has been AAA-adjacent for a decade.
6. **Watch receivables quality.** AR +30.1% vs revenue +19.6%, with allowance coverage easing to ~3.2% of gross AR. If DSO keeps expanding for two more quarters, suspect channel/mix stress in AWS/ads rather than a one-off.
7. **Watch contract liabilities ($24.88B, down slightly) vs. contractual obligations ($650B, up).** A rising obligation book with flat deferred revenue means the commitments are *purchase*-side (AMZN buying compute/power), not *customer*-side prepayments. That is a **risk-transfer onto AMZN's balance sheet** — bullish for the AI suppliers, leverage risk for AMZN.
8. **Data gap to close before trading:** (a) EDGAR Form 4 insider activity, (b) FY2025 annual statements for a multi-year margin/capex trend, (c) segment-level AWS vs. retail operating income, (d) the Q2 10-Q's disclosure naming/valuing the private equity holdings. **The most recent 10-Q should be read in full for the Level-3 valuation methodology note before sizing a position around the investment book.**

---

## 10. Key metrics summary table

| Category | Metric | Value | Period | Trend / Signal |
|---|---|---|---:|---|
| **Growth** | Revenue | $200.61B | Q2 FY26 | 🟢 +19.6% y/y (accel. from +16.6% in Q1) |
| | Revenue | $382.13B | H1 FY26 | 🟢 +18.2% y/y |
| **Profitability** | Gross margin | 52.3% | Q2 FY26 | 🟢 +50bp y/y |
| | Operating income | $27.46B | Q2 FY26 | 🟢 +43.2% y/y |
| | Operating margin | 13.7% | Q2 FY26 | 🟢 +230bp y/y |
| | Operating margin | 13.4% | H1 FY26 | 🟢 +180bp y/y |
| | Net income (GAAP) | $62.65B | Q2 FY26 | ⚠️ +245% but mark-driven |
| | Diluted EPS (GAAP) | $5.75 | Q2 FY26 | ⚠️ ~65% from investment marks |
| | **Diluted EPS (core est.)** | **~$1.86–2.00** | Q2 FY26 | 🟢 ~+20–23% y/y, high quality |
| | Effective tax rate | 22.5% / 23.0% | Q2 / H1 FY26 | 🔴 +970bp / +600bp y/y |
| **Earnings quality** | Non-operating income | $53.40B (66% of pretax) | Q2 FY26 | 🔴 Investment marks dominate |
| | Non-operating income | $69.38B (57% of pretax) | H1 FY26 | 🔴 |
| | Upward mark on private equity | $50.49B / $62.81B | Q2 / H1 FY26 | 🔴 Non-cash, Level 3 |
| **Cash flow** | Operating cash flow | $45.39B / $71.42B / $161.40B | Q2'26 / H1'26 / TTM | 🟢 +39.6% y/y in Q2 |
| | Capex | $54.21B / $98.41B / $173.03B | Q2'26 / H1'26 / TTM | 🔴 +68% y/y, accelerating |
| | **Free cash flow** | **–$8.82B / –$26.99B / –$11.63B** | Q2'26 / H1'26 / TTM | 🔴 Negative and widening |
| | Cash taxes paid | $3.98B (3.3% of pretax) | H1 FY26 | ⚠️ Flatters OCF; reverses later |
| | Deferred tax expense | $30.49B | H1 FY26 | 🔴 vs $0.52B LY |
| | Acquisitions, net | $39.77B | H1 FY26 | 🟡 vs $1.65B LY — M&A re-acceleration |
| **Balance sheet** | Total assets | $1,095.69B | 6/30/26 | 🟢 +33.9% in 6 months |
| | Cash + AFS securities | $176.11B | 6/30/26 | 🟢 Ample liquidity |
| | Total long-term debt | $133.00B | 6/30/26 | 🔴 +$64.16B (+93%) in 6 months |
| | Finance lease liabilities | $13.45B | 6/30/26 | 🔴 +$1.17B |
| | Operating lease liabilities | $96.32B | 6/30/26 | 🟡 +$7.07B |
| | **Net cash (debt + fin. leases)** | **~+$29.7B** | 6/30/26 | 🟢 Still net cash, but eroding fast |
| | Equity securities w/o ready FV | $122.30B (11% of assets) | 6/30/26 | ⚠️ +$106.10B — new risk concentration |
| | AOCI | $66.29B | 6/30/26 | ⚠️ +$38.06B in H1, bypasses P&L |
| | Inventory | $38.18B | 6/30/26 | 🟢 Flat vs revenue +19.6% (efficient) |
| | Accounts receivable | $88.09B | 6/30/26 | 🟡 +30.1%, faster than revenue |
| | Accounts payable | $147.44B | 6/30/26 | 🟡 +20.9% — funding source |
| **Leverage / coverage** | Interest expense | $1.31B / $2.11B | Q2 / H1 FY26 | 🔴 +155% / +100% y/y |
| | Interest coverage (op income/interest) | 20.9x / 24.3x | Q2 / H1 FY26 | 🟢 Strong but falling |
| **Commitments** | Total contractual obligations | $650.03B | 6/30/26 | ⚠️ ~$78.08B due <12 months |
| | Energy derivative notional (H1) | 270 million MWh | H1 FY26 | 🟢 Confirms AI power buildout |
| | SBC unrecognized | $24.80B | 6/30/26 | 🟡 Future expense headwind |
| **Capital structure** | Shares outstanding | 10.783B | 6/30/26 | 🟢 +0.5% in 6 months (minimal dilution) |
| | Shares outstanding (cover) | 10,786,313,572 | 7/22/26 | — |
| **Segments** | Reportable segments | 3 | H1 FY26 | NA / Int'l / AWS |
| **Insider activity** | — | **DATA UNAVAILABLE** | — | ❌ No authorized archive; not inferred |

---

### Bottom line for the desk

**AMZN's operating engine has never been stronger — 19.6% growth, 13.7% operating margins, and genuine cost discipline at $200B/quarter scale.** But **the reported numbers are now materially decoupled from the operating reality**: ~65% of Q2 EPS is a non-cash private-equity mark, free cash flow is **negative $27B year-to-date**, and long-term debt has **nearly doubled in six months** to fund the largest capex program in the company's history. **Underwrite AMZN on core EPS (~$8 annualized) and the FCF bridge, treat the $122B private-mark book as a separate NAV swing factor, and treat rising depreciation plus a 23% tax rate as the structural 2027 margin risk.** The next 10-Q's Level-3 valuation note and insider Form 4s are the two gaps to close before sizing.