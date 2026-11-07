# AMZN — Fundamental Deep Dive (Point-in-Time as of 2026-09-01)

**Issuer:** Amazon.com, Inc. (AMZN) · **Latest filing in the dataset:** Form 10-Q for the quarter ended **2026-06-30**, filed/accepted **2026-07-31** (accession 0001018724-26-000026). Prior 10-Q (Q1 2026) accepted 2026-04-30. Shares outstanding **10,786,313,572** as of 2026-07-22.
**Reported segments:** 3 operating segments (confirmed by `NumberOfOperatingSegments = 3` — i.e., North America, International, AWS). Segment-level revenue/operating income is **not** present in the returned dataset; only consolidated figures are available.

> **Data caveat up front:** the tools return a point-in-time SEC XBRL fact cache. There is **no price, market cap, consensus, guidance, or segment detail** in it, so no valuation multiples can be computed here. Insider transactions are **explicitly unavailable** (see §9). All ratios below are computed by me from the raw tagged facts; anything estimated is labeled.

---

## 1. The single most important thing in this dataset: earnings quality

Headline Q2 2026 results look spectacular — **EPS $5.75**, net income **$62.6B**. But the driver is **not** retail or AWS operations. It is a non-cash revaluation of a private equity holding.

| Driver (Q2 2026, $M) | Value |
|---|---|
| Non-operating income/(expense), net | **+53,396** |
| of which investment income (interest) | +1,295 |
| of which interest expense | (1,314) |
| → implied "other" non-operating income | **≈ +53,415** |
| Equity securities w/o readily determinable FV — **upward price adjustment, Q2 alone** | **+50,486** |
| Same, H1 2026 cumulative | **+62,814** |
| Carrying value of equity securities w/o readily determinable FV: 2025-12-31 → 2026-06-30 | **$16,200 → $122,300 (+$106.1B)** |

**Interpretation:** ~$50B of Q2's $80.9B pretax income came from marking up a private investment (magnitude and timing are consistent with a large AI-lab stake). This is (a) non-cash, (b) not tax-efficient in cash terms (cash taxes paid in Q2 were only $2.66B against $18.2B of book tax, with **deferred tax expense of $17.7B in Q2 / $30.5B in H1**), and (c) **reversible**.

**"Core" earnings rebuild:**

| $M | Q2 2026 | H1 2026 |
|---|---|---|
| Reported pretax income | 80,857 | 120,691 |
| Less: non-operating income, net | (53,396) | (69,378) |
| **Core pretax (≈ operating income + net interest)** | **27,442** | **51,629** |
| Core net income @ 23% tax (approx.) | ~21,100 | ~39,750 |
| **Core diluted EPS (approx.)** | **~$1.95** | **~$3.65** |
| Reported diluted EPS | **$5.75** | **$8.53** |

**So roughly 70% of Q2 2026 reported net income was non-operating.** Any trader anchoring on the $5.75 print or on a trailing P/E built from it is mispricing the business.

---

## 2. Income statement — the operating business is genuinely accelerating

Derived revenue (Revenue = OperatingIncome + CostsAndExpenses; consistent across all periods):

| $M | Q2 2026 | Q2 2025 | Δ y/y | H1 2026 | H1 2025 | Δ y/y |
|---|---|---|---|---|---|---|
| Revenue | **200,606** | 167,702 | **+19.6%** | **382,125** | 323,369 | **+18.2%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 183,241 | 157,785 | +16.1% |
| **Gross profit** | **104,828** | 86,893 | +20.6% | **198,884** | 165,584 | +20.1% |
| Gross margin | **52.3%** | 51.8% | +0.4pp | 52.1% | 51.2% | +0.9pp |
| Marketing | 11,698 | 11,416 | +2.5% | 22,012 | 21,179 | +3.9% |
| G&A | 2,788 | 2,965 | −6.0% | 5,375 | 5,593 | −3.9% |
| D&A | 19,988 | 15,227 | **+31.3%** | 38,933 | 29,489 | **+32.0%** |
| SBC (allocated) | 6,038 | 6,534 | **−7.6%** | 10,070 | 10,223 | −1.5% |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 330,812 | 285,793 | +15.8% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** | **51,313** | 37,576 | **+36.6%** |
| **Operating margin** | **13.7%** | 11.4% | **+2.3pp** | 13.4% | 11.6% | **+1.8pp** |
| Interest expense | 1,314 | 516 | **+155%** | 2,114 | 1,057 | +100% |
| Investment income | 1,295 | 1,085 | +19% | 2,430 | 2,151 | +13% |
| Non-operating income, net | 53,396 | 1,686 | 31.7x | 69,378 | 4,960 | 14.0x |
| Pretax income | 80,857 | 20,857 | +288% | 120,691 | 42,536 | +184% |
| Tax | 18,199 | 2,678 | — | 27,759 | 7,231 | — |
| Effective tax rate | 22.5% | 12.8% | — | 23.0% | 17.0% | — |
| **Net income** | **62,647** | 18,164 | +245% | **92,902** | 35,291 | +163% |
| Diluted EPS | **5.75** | 1.68 | — | **8.53** | 3.27 | — |
| Diluted shares (implied) | ~10,895M | ~10,810M | +0.8% | ~10,895M | ~10,793M | +0.9% |

**Quarterly trajectory (2026):**

| Metric | Q1 2026 | Q2 2026 | QoQ |
|---|---|---|---|
| Revenue | 181,519 | 200,606 | **+10.5%** |
| Operating income | 23,852 | 27,461 | +15.1% |
| Operating margin | 13.1% | 13.7% | +0.55pp |
| Net income | 30,255 | 62,647 | +107% |
| Diluted EPS | 2.78 | 5.75 | — |

**Read-through:** revenue growth **accelerated** from +16.6% (Q1'26) to **+19.6%** (Q2'26) against still-elevated comps, while operating margin **expanded** sequentially and by 230bp y/y. This is the strongest combination in the dataset: volume + mix + cost discipline. Note the *operating leverage* signature — marketing +2.5% and G&A **−6.0%** against +19.6% revenue, and SBC *down* 7.6% y/y. That is genuine expense discipline, not accounting.

**The offset:** D&A +31% y/y (a direct consequence of the capex surge — see §5) and interest expense +155% y/y (a direct consequence of the debt surge — see §4). Both will keep climbing mechanically.

**Note on revenue growth:** the 18–20% headline is partly inorganic. `PaymentsToAcquireBusinessesNetOfCashAcquired` = **$39,767M in H1 2026** ($15,408M in Q1, **$24,359M in Q2**) vs just $1,652M in H1 2025. A ~$40B of M&A spend in six months can add low-to-mid single digits of inorganic growth. **Organic growth is therefore likely closer to ~13–16%** — still strong, but materially below the headline. Segment detail would be needed to size this precisely and is not in the dataset.

---

## 3. Balance sheet — a step-change in size, funded by debt and paper gains

| $M | 2025-12-31 | 2026-06-30 | Δ |
|---|---|---|---|
| Cash & equivalents | 78,213* / 86,810 | 78,213 | — |
| Available-for-sale debt securities | 45,800 | **97,900** | **+113.8%** |
| **Cash + AFS securities** | ~132,610 | **~176,113** | **+43,503** |
| Accounts receivable, net | 67,729 | 88,092 | +30.1% |
| Inventory, net | 38,325 | 38,184 | −0.4% |
| **Current assets** | 229,083 | **249,264** | +8.8% |
| Equity securities w/o readily determinable FV | 16,200 | **122,300** | **+655%** |
| Operating lease ROU asset | 86,054 | 92,743 | +7.8% |
| **Total assets** | **818,042** | **1,095,689** | **+33.9%** |
| Accounts payable | 121,909 | **147,440** | +20.9% |
| Accrued liabilities | 75,520 | 73,406 | −2.8% |
| LT debt — current portion | 2,748 | 3,330 | +21.2% |
| Operating lease liability — current | 12,655 | 13,745 | +8.6% |
| **Current liabilities** | 218,005 | **241,274** | +10.7% |
| **LT debt — noncurrent** | 65,648 | **128,894** | **+96.3%** |
| Operating lease liability — noncurrent | 76,597 | 82,575 | +7.8% |
| Finance lease liability — noncurrent | 10,742 | 11,763 | +9.5% |
| Deferred revenue (contract liability) — current / non-current | 20,576 / 4,400 | 20,428 / 4,500 | flat |
| Common stock + APIC | 140,136 | 149,732 | +6.8% |
| AOCI | 28,230 | **66,287** | **+134.8%** |

*Cash and equivalents at 12/31/25 shown as $86,810; the $78,213 line is the 6/30/26 balance.

**Liquidity ratios (6/30/26):**
- **Current ratio: 1.03x** (249,264 / 241,274) — tight, and structurally so for Amazon (negative working capital model).
- **Quick ratio: 1.10x** (cash 78,213 + AFS 97,900 + AR 88,092 = 264,205 / 241,274).
- Supplier-funded working capital: AP + accrued = **$220.8B** vs AR + inventory = **$126.3B** → the model still runs on ~$95B of net trade float. A deterioration in payment terms is a live liquidity variable.

**Total debt (carrying)**: $3,330M current + $128,894M noncurrent = **$132.2B**, plus **operating leases $96.3B** and **finance leases $13.5B** → **~$242B** of debt + lease obligations. Net of $176.1B cash/AFS: **~$66B net debt ex-leases; ~$66–176B including leases** depending on treatment.

**Estimated book equity (derived, not reported):** total assets of $1,095.7B less current liabilities of $241.3B and identifiable non-current liabilities of $227.7B (debt + leases + deferred revenue) leaves roughly **$560–580B** of equity after allowing for unlisted deferred-tax/other long-term liabilities. **Book value ≈ $52–54/share (ESTIMATE).** At ~$570B equity, TTM reported ROE is ~24% (inflated by markups); **core ROE is ~14–15%**.

**Two balance-sheet flags:**
1. **Assets +34% in six months** ($818B → $1,096B). This is dominated by the $106B equity-securities markup, ~$98B of H1 capex, and ~$40B of acquisitions — not by organic working capital.
2. **AOCI +$38.1B in H1** (28,230 → 66,287). The dataset only shows a **−$1.6B FX translation** component, so ~$38B of the OCI swing is *not* explained by the disclosed FX line — consistent with unrealized gains on the enlarged AFS securities book (`DebtSecuritiesAvailableForSaleUnrealizedGainLoss` of $92.0B YTD is tagged). **Treat the AOCI swing and the AFS revaluation as one lumpy, rate/market-sensitive item that can reverse.** This is a data-quality soft spot worth flagging to any model built off book value.

---

## 4. Debt & commitments — the capex is being borrowed, and the forward book is enormous

**Debt raised (cash flow, $M):**

| | H1 2026 | H1 2025 | TTM (Jul'25–Jun'26) |
|---|---|---|---|
| LT debt issued | **66,998** | 746 | **81,925** |
| LT debt repaid | (2,752) | (2,751) | (5,022) |
| ST debt issued | 15,386 | 3,908 | 20,798 |
| ST debt repaid | (15,682) | (3,474) | (20,634) |
| **Net financing inflow** | **+62,913** | (2,586) | **+75,160** |

This is a **strategic shift**: Amazon historically funded itself almost entirely from operating cash flow. Over the trailing year it has raised **~$82B of term debt** and ~$21B of short-term paper. Long-term debt nearly doubled in six months.

**Contractual obligations (6/30/26):**

| Bucket | $M |
|---|---|
| **Total contractual obligations** | **650,034** |
| Due in remainder of FY2026 | 42,752 |
| Due in next twelve months | 78,084 |
| Due in second year | 53,406 |
| Due in third year | 46,767 |
| Due in fourth year | 42,219 |
| Operating lease payments due (undiscounted) | 116,350 |
| Finance lease payments due (undiscounted) | 16,660 |

**$650B of commitments** — against ~$800B of annualized revenue. This is the clearest evidence in the dataset that management has converted AMZN into a **contracted, capital-intensive compute build-out** (AI/servers/data centers/content), which raises both the growth ceiling and the operating-risk floor: much of this spend is contracted and therefore slow to flex if demand disappoints.

---

## 5. Cash flow — record operating cash, and *negative* free cash flow

| $M | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | TTM (Jul'25–Jun'26) |
|---|---|---|---|---|---|
| Operating cash flow | 45,387 | 32,515 | **71,419** | 49,530 | **161,403** |
| Capex (productive assets) | (54,208) | (32,183) | **(98,411)** | (57,202) | **(173,028)** |
| **Free cash flow** | **(8,821)** | **+332** | **(26,992)** | (7,672) | **(11,625)** |
| Business acquisitions, net | (24,359) | (1,700) | (39,767) | (1,652) | (41,956) |
| Purchases of marketable securities | (26,006) | (17,797) | (49,262) | (31,130) | (72,902) |
| Sale/maturity of marketable securities | 24,196 | 11,441 | 41,882 | 19,178 | 67,090 |
| **Investing cash flow** | **(79,245)** | (39,424) | **(143,457)** | (69,227) | **(216,775)** |
| Financing cash flow | +10,146 | (2,539) | **+62,913** | (2,586) | +75,160 |
| Net change in cash (incl. FX) | (23,765) | (8,440) | (9,179) | (20,859) | +19,474 |

**This is the crux of the investment debate:**

- **Operating cash flow is exceptional and accelerating:** H1 +44% y/y, TTM **$161.4B**.
- **Capex is exploding faster:** H1 **+72%** y/y ($57.2B → $98.4B); Q2 alone was **$54.2B**, i.e. a **~$217B annualized run-rate**, ~27% of quarterly revenue.
- **FCF is negative on every horizon:** −$8.8B (Q2), −$27.0B (H1), −$11.6B (TTM). The company is now **using the capital markets to plug the gap** ($62.9B of net financing in H1).
- **Cash conversion quality is fine** if you strip the markups: OCF / *core* net income ≈ 1.8x. OCF / *reported* net income = 0.77x — that gap is the non-cash revaluation doing its work, not a cash-flow problem.
- D&A of **$75.2B TTM** (+32% y/y) is the lagging shadow of this capex; expect it to keep compressing reported margins for several quarters even as cash margins hold.
- **No shareholder returns**: zero buyback and zero dividend lines appear in financing. Share count rose 0.5% in six months (10,731M → 10,783M). SBC is being offset only by dilution, not repurchases.

**EBITDA / leverage math (approximate):** TTM operating income ≈ $96B (H1'26 $51.3B + estimated H2'25 ~$45B implied by TTM net income of $135.3B less H1'26 $92.9B), plus D&A $75.2B → **TTM EBITDA ≈ $170B**. Against ~$66B net debt (ex-leases) that is **~0.4x** — investment-grade, comfortable. Even on a gross-debt-plus-leases basis (~$242B) it is **~1.4x**. **Leverage is not the risk; the risk is the return on the $173B/yr of capex.**

---

## 6. Working capital & operating detail (quality checks)

| Check | 6/30/26 | 12/31/25 | Read |
|---|---|---|---|
| AR, net | 88,092 | 67,729 | +30% — faster than 6-mo revenue growth; partly seasonal (H1 vs Q4), partly the mix shift toward AWS/ads/advertising receivables |
| AR allowance | 2,800 | 2,400 | +16.7% vs AR +30% → **reserve coverage declining** (3.2% of AR vs 3.5%); minor but worth monitoring |
| AR days (Q2 rev) | 40.0 | — | Healthy |
| Inventory | 38,184 | 38,325 | **Flat** on +18% revenue → real inventory efficiency, no channel stuffing signal |
| Inventory valuation reserves | 3,000 | 3,300 | **Down 9%** — consistent with healthy sell-through |
| AP | 147,440 | 121,909 | +21% — supplier float expanding, funding the build-out |
| Deferred revenue (total) | 24,928 | 25,000 | Flat; $15.2B recognized into revenue in H1 |
| Unrecognized SBC | 24,800 | — | ~2.5 years of forward expense at current run-rate |

---

## 7. Trend summary — what actually changed in the last 6–12 months

1. **Operating re-acceleration + margin expansion simultaneously.** Revenue +19.6% y/y in Q2 with operating margin up 230bp. Historically AMZN trades growth for margin or vice versa; getting both is the bullish signal.
2. **A capital-markets regime change.** First meaningful debt raise in years ($82B TTM), interest expense +155% y/y. AMZN is now a levered infrastructure builder.
3. **A large, opaque private-AI equity position is now ~11% of total assets** ($122.3B) and swung reported EPS by ~$3.80/share in Q2 alone. This introduces an entirely new, low-transparency earnings-volatility channel.
4. **FCF inflection downward.** Q2 2025 was roughly FCF-neutral (+$0.3B); Q2 2026 is −$8.8B. The company is deliberately trading near-term FCF for compute capacity.
5. **Inorganic contribution rising:** ~$40B of H1 acquisitions vs $1.7B a year prior.

---

## 8. Actionable conclusions for traders

**Bullish (evidence-based):**
- **Core operating momentum is the best in the dataset**: revenue +19.6%, operating income +43.2%, operating margin 13.7% (+2.3pp). Expense discipline is real (marketing +2.5%, G&A −6%, SBC −7.6% against ~20% revenue growth). If Q3 holds double-digit organic growth with ≥13% operating margin, the *operating* earnings power is being under-appreciated by anyone looking only at the noisy GAAP EPS.
- **Balance sheet is not a constraint.** ~$176B cash + AFS, ~0.4x net leverage ex-leases, EBITDA ~$170B TTM. The debt raise is opportunistic scale, not distress.
- **Inventory and reserves are clean.** No sign of demand pull-forward or write-down pressure.
- **D&A will lag capex**, so GAAP operating margin has a mechanical tailwind from… actually the reverse: it's a headwind. But CFO should keep compounding as the capex converts to revenue.

**Bearish / risk-managed:**
- **Do not pay a multiple on $5.75 of Q2 EPS.** ~70% of it was a non-cash private-stake markup. **Core Q2 EPS is ~$1.95; core H1 is ~$3.65.** Any screen or sell-side model built on reported TTM EPS of ~$12+ is overstating recurring earnings by roughly 2x.
- **FCF is negative and worsening** (−$27B H1, −$11.6B TTM) with capex at a ~$217B annualized run-rate. If capex guides higher again, the FCF story stays broken regardless of operating strength.
- **The $122.3B private equity position is the single largest swing factor in reported results.** A down-round or valuation reset in private AI would produce a large non-cash charge and a violent headline-EPS miss. There is no mark-to-market transparency.
- **Current ratio 1.03x and $650B of contractual obligations** reduce financial flexibility meaningfully versus the pre-2025 AMZN profile.
- **Inorganic growth muddies the read:** ~$40B of H1 M&A means headline growth overstates organic momentum by a low-to-mid single digit amount.

**Suggested framing for a position:** trade AMZN on **operating income, operating margin, and OCF** — *not* on GAAP EPS or trailing FCF. The two cleanest live indicators to monitor next quarter are (1) Q3 operating margin vs the 13.7% Q2 print, and (2) quarterly capex vs the $54.2B Q2 print. A margin hold plus a capex plateau would be strongly bullish (FCF inflects); a margin hold plus another capex step-up keeps the stock reliant on narrative. **Strip out all non-operating income before valuing.**

---

## 9. Insider transactions

**DATA UNAVAILABLE.** The news/filings vendor has **no authorized point-in-time insider-transaction archive for AMZN as of 2026-09-01**. No insider buying or selling can be reported, and per instruction none has been inferred or fabricated. Treat insider sentiment as **unknown — not as neutral**. This is a genuine information gap and should be sourced separately (Form 4 filings) before weighting it in a decision.

---

## 10. Gaps & caveats a trader should know

| Gap | Impact |
|---|---|
| No price / market cap / EV | Valuation multiples (P/E, EV/EBITDA, FCF yield) **cannot** be computed from these tools |
| No segment revenue or segment operating income | Cannot isolate AWS margin — the most important driver of AMZN's valuation |
| No guidance, backlog/RPO, or capex plan | The capex trajectory is the key swing factor and is unobservable here |
| No insider data | Governance/sentiment signal missing |
| AOCI swing ($+38B) only partly explained by disclosed FX (−$1.6B) | Book value and comprehensive income are less reliable than the income statement |
| Book equity (~$560–580B) is a **derived estimate**, not a reported tag | ROE/book-value ratios carry model risk |
| Revenue is derived (OperatingIncome + CostsAndExpenses), not a tagged line | Arithmetic is internally consistent across all 6 periods, but is a reconstruction |

---

## Key Points Summary

| Category | Metric | Value | Signal |
|---|---|---|---|
| **Latest filing** | Form 10-Q, quarter ended 2026-06-30 | Filed 2026-07-31 | Fresh (~1 month old) |
| **Segment count** | Operating segments | 3 (NA, Int'l, AWS) | Segment detail not disclosed in dataset |
| **Growth** | Q2 2026 revenue | $200.6B, **+19.6% y/y** | Accelerating vs Q1 +16.6% |
| **Growth** | H1 2026 revenue | $382.1B, **+18.2% y/y** | Partly inorganic (~$40B M&A) |
| **Profitability** | Q2 2026 operating income | $27.5B, **+43.2% y/y** | Genuine operating leverage |
| **Profitability** | Q2 2026 operating margin | **13.7%** (vs 11.4%) | +230bp y/y, +55bp q/q |
| **Profitability** | H1 2026 operating margin | 13.4% (vs 11.6%) | +180bp |
| **Margins** | Gross margin Q2 2026 | 52.3% (vs 51.8%) | Modest, steady expansion |
| **Earnings quality** | Reported Q2 diluted EPS | **$5.75** | ~70% from non-operating |
| **Earnings quality** | **Core Q2 diluted EPS (est.)** | **~$1.95** | The number that actually recurs |
| **Earnings quality** | H1 core diluted EPS (est.) | ~$3.65 vs reported $8.53 | Non-op income $69.4B of $120.7B pretax |
| **Non-cash item** | Private equity securities revaluation | +$50.5B (Q2), +$62.8B (H1) | Reversible; low transparency |
| **Non-cash item** | Carrying value of that stake | $16.2B → **$122.3B** | ~11% of total assets |
| **Cash generation** | TTM operating cash flow | **$161.4B** | +44% y/y on H1 basis |
| **Capex** | TTM capex | **$173.0B** | H1 +72% y/y; Q2 $54.2B (~$217B annualized) |
| **FCF** | Q2 / H1 / TTM | **−$8.8B / −$27.0B / −$11.6B** | Negative and widening |
| **Debt** | LT debt noncurrent | $65.6B → **$128.9B** (+96%) | Structural regime change |
| **Debt** | TTM LT debt issued | $81.9B | Funding the capex gap |
| **Cost of debt** | Q2 interest expense | $1.314B, **+155% y/y** | Rising drag on GAAP EPS |
| **Liquidity** | Cash + AFS securities | **~$176.1B** | AFS up +114% to $97.9B |
| **Liquidity** | Current ratio | **1.03x** | Tight; supplier-float dependent |
| **Leverage** | Net debt ex-leases / TTM EBITDA | ~$66B / ~$170B ≈ **0.4x** | Comfortable; not the risk |
| **Commitments** | Total contractual obligations | **$650.0B** | $78.1B due in next 12 months |
| **Leases** | Operating + finance lease liabilities | $109.8B | $116.4B / $16.7B undiscounted payments |
| **Working capital** | Inventory | $38.2B, **flat y/y** on +18% revenue | Clean; no channel stuffing |
| **Working capital** | Inventory valuation reserves | $3.3B → $3.0B (−9%) | Healthy sell-through |
| **Working capital** | AR allowance / AR | 3.2% of AR (vs 3.5%) | Slight coverage decline |
| **Capital return** | Buyback / dividend | **Zero** | Shares +0.5% in 6 months |
| **Comp** | SBC H1 2026 | $10.1B (−1.5% y/y) | Unrecognized $24.8B |
| **Assets** | Total assets | $818.0B → **$1,095.7B** | +33.9% in six months |
| **Est. equity** | Book value (derived, est.) | ~$560–580B (~$52–54/sh) | Estimate — not a reported tag |
| **Returns** | Core ROE (est.) | ~14–15% | vs ~24% reported (markup-inflated) |
| **Insider activity** | Buy/sell | **DATA UNAVAILABLE** | Unknown ≠ neutral |
| **Valuation** | P/E, EV/EBITDA, FCF yield | **Not computable** | No price data in toolset |

**Bottom line on AMZN:** the *operating* franchise is performing better than at any point in this dataset — accelerating revenue with real margin expansion and disciplined opex. The *reported* numbers, however, are being distorted by a ~$63B non-cash private-AI revaluation, and the *cash* story has inverted: TTM FCF is −$11.6B because capex has roughly tripled to a ~$217B annualized run-rate, funded increasingly with debt. Value AMZN on operating income (Q2 $27.5B, 13.7% margin, +43% y/y) and on the capex plateau question, not on the $5.75 headline EPS.