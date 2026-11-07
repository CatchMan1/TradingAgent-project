# GOOGL — Fundamental Deep Dive (Point-in-Time: 29 July 2026)

**Company:** Alphabet Inc. — Class A common stock, ticker **GOOGL**
**Latest filing in dataset:** Form 10-Q, period ended **30 June 2026**, accepted **2026-07-23** (accn 0001652044-26-000071); prior 10-K for FY2025 accepted **2026-02-05** (accn 0001652044-26-000018).

> **Data provenance note:** All figures below are point-in-time SEC XBRL facts (public on or before 2026-07-29). The dataset does not return a raw `Revenue` line, a market price, or insider-transaction records. Revenue and R&D are therefore **derived arithmetically** from `CostsAndExpenses + OperatingIncomeLoss` and `CostsAndExpenses − CostOfRevenue − G&A` respectively and are labelled as such. Insider transactions: **DATA UNAVAILABLE** for GOOGL in this archive — no insider activity is asserted or inferred.

---

## 1. Executive Summary — the five things that matter

1. **Headline profitability is being driven by investment markups, not operations.** Q2 2026 net income was **$112.19B** vs $28.20B a year ago (+298%), but **$97.98B of the $138.75B pretax income came from non-operating income** — almost entirely realized/unrealized gains on equity securities (FV-NI gain of **$99.03B** in the quarter). Operating income was $40.77B. Strip the gains and Q2 core EPS is roughly **$2.65–2.70 vs $9.11 reported**.
2. **The core business is genuinely accelerating.** Derived revenue **$119.80B in Q2 (+24.2% YoY)** and **$229.69B in H1 (+23.1%)**; operating income **+30.4% / +30.0%**; operating margin expanded ~190bp to **34.0% (Q2)** and **35.0% (H1)**. Cost of revenue grew slower than revenue (+17.7% in Q2), which is the signature of operating leverage.
3. **Free cash flow has broken.** H1 2026 capex **$80.60B (+103% YoY)**, capex/revenue **35.1%**. H1 FCF (OCF − capex) collapsed **−82% to $4.26B**, and **Q2 2026 FCF was NEGATIVE at −$5.86B** (vs +$5.30B in Q2 2025). `CapitalExpendituresIncurredButNotYetPaid` of **$29.11B** (vs $10.64B) implies more cash outflow queued.
4. **The balance sheet was re-engineered in six months.** Total assets **$595.28B → $921.98B (+54.9%)**. Debt carrying value **$49.09B → $101.09B (+106%)**; **$30.50B of common stock issued** (a first for Alphabet); **$19.06B of convertible preferred issued** (5 June 2026); **buybacks went to $0** (vs $28.31B in H1 2025). Net cash is still large (~**$138.8B**) but the capital-allocation regime has changed decisively.
5. **Earnings quality carries a visible tax and valuation tail.** Net deferred tax liabilities ballooned **$0.92B → $22.82B**, and non-marketable equity securities (no readily determinable fair value) rose **$64.09B → $124.26B** with cumulative upward revaluations of **$85.73B**. This is a mark-to-model asset base that can reverse violently and will eventually attract tax.

---

## 2. Company Profile

Alphabet Inc. is the parent of Google (Google Services: Search, YouTube ads, Google Network, subscriptions/devices; Google Cloud) plus Other Bets. It reports as a single SEC registrant (CIK 1652044) with Class A (GOOGL), Class B and Class C shares. Authorized capital is 300B shares; **12,230M shares outstanding at 30 June 2026** (vs 12,088M at 31 Dec 2025, **+1.17%**), par $0.001. The company pays a quarterly dividend (raised to **$0.22** from $0.21; H1 declared **$0.43** vs $0.41).

What is different about this profile versus the historical Alphabet: it is now (a) a heavy issuer of debt, (b) an issuer of **convertible preferred stock**, (c) an issuer of **common equity**, and (d) no longer a net buyer of its own shares. That is the balance-sheet fingerprint of an aggressive, externally financed AI-infrastructure build-out with strategic third-party capital participation (minority proceeds of **$3.76B** in H1 support this).

---

## 3. Income Statement — Q2 and H1 2026 (derived revenue)

All $ millions. Revenue derived as `CostsAndExpenses + OperatingIncomeLoss`.

| Line (derived) | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---|---|---|---|---|---|
| Revenue | **119,796** | 96,428 | **+24.2%** | **229,692** | 186,662 | **+23.1%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| Gross profit | 73,853 | 57,389 | +28.7% | 142,478 | 111,262 | +28.1% |
| Gross margin | 61.6% | 59.5% | +210bp | 62.0% | 59.6% | +240bp |
| R&D (derived) | ~16,622 | ~10,909 | n/m | **51,260** | 40,637 | +26.1% |
| G&A | 6,461 | 5,209 | +24.0% | 10,752 | 8,748 | +22.9% |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 149,226 | 124,785 | +19.6% |
| **Operating income** | **40,770** | 31,271 | **+30.4%** | **80,466** | 61,877 | **+30.0%** |
| Operating margin | 34.0% | 32.4% | +160bp | 35.0% | 33.1% | +190bp |
| Non-operating income | **97,983** | 2,662 | n/m | **135,699** | 13,845 | n/m |
| — of which equity FV-NI gains | **99,031** | 1,286 | n/m | **135,946** | 11,044 | n/m |
| Interest income / interest expense | 1,430 / 1,278 | 1,050 / 261 | +36% / +390% | 2,811 / 1,811 | 2,051 / 295 | +37% / **+514%** |
| Pretax income | **138,753** | 33,933 | +309% | 216,165 | 75,722 | +185% |
| Tax | 26,560 | 5,737 | — | 41,394 | 12,986 | — |
| Effective tax rate | 19.1% | 16.9% | +220bp | 19.1% | 17.1% | +200bp |
| **Net income** | **112,193** | 28,196 | **+298%** | **174,771** | 62,736 | **+179%** |
| Net income to common | 112,107 | 28,196 | +298% | 174,685 | 62,736 | +178% |
| **EPS diluted** | **$9.11** | $2.31 | **+294%** | **$14.24** | $5.12 | **+178%** |
| EPS basic | $9.23 | $2.33 | +296% | $14.41 | $5.16 | +179% |

**Key read-throughs**

- **Operating leverage is real.** Gross margin +240bp in H1 while capex nearly doubled — depreciation has not yet hit the P&L in force (see §5), so this margin expansion is partly *pre-depreciation*.
- **The "core" earnings picture.** Excluding equity investment gains (tax-effected at 19.1%), H1 2026 core net income ≈ **$65.1B**, or **~$5.35–5.40/share**, versus ~$4.35–4.40 in H1 2025 → **core EPS growth ~+23%**. That is excellent, but it is one-quarter of the reported headline growth rate.
- **Interest expense is compounding fast** (+514% YoY to $1.81B in H1) as debt doubled. On the new ~$101B debt base this line annualises toward $5–6B, a direct EPS headwind of roughly $0.35–0.40/share/quarter gross.
- **Share-based compensation is rising aggressively:** $15.20B H1 (+32% YoY; Q2 $8.00B, +33%), i.e. **~6.6% of revenue in Q2** vs 6.2% a year ago. Combined with +1.17% share count, dilution is a persistent quality drag on per-share metrics.
- **Revenue recognition backlog:** contract liabilities rose to $10.10B (from $8.60B) and $4.90B of H1 revenue came from the opening contract-liability balance — consistent with a strong Cloud/committed-contract book.

---

## 4. Balance Sheet — a step-change in scale and leverage

| Item ($M) | 30 Jun 2026 | 31 Dec 2025 | Change |
|---|---|---|---|
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| **Cash + short-term investments** | **242,474** | 126,843 | **+91.2%** |
| — AFS debt securities (FV) | 99,500 | — | — |
| Accounts receivable, net | 69,175 | 62,886 | +10.0% |
| Current assets | 343,524 | 206,038 | +66.7% |
| **Non-marketable equity securities (no RDFV)** | **124,259** | 64,094 | **+93.9%** |
| — cumulative upward revaluation | 85,732 | 44,485 | +92.7% |
| — cumulative downward revaluation | (9,115) | (8,820) | — |
| **Total assets** | **921,983** | 595,281 | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| Employee-related liabilities | 15,086 | 17,546 | −14.0% |
| Loss contingency accrual (current) | 17,356 | 15,594 | +11.3% |
| Income taxes payable (curr. + noncurr.) | 16,539 | 10,054 | +64.5% |
| **Debt carrying value** | **101,085** | 49,085 | **+105.9%** |
| — unamortized discount/costs | (921) | (542) | — |
| Operating lease liability | 18,037 | 15,954 | +13.1% |
| Finance lease liability | 2,590 | 2,500 | +3.6% |
| **Net deferred tax liability** | **22,819** | 919 | **~25x** |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| AOCI | (2,285) | (1,916) | — |
| Convertible preferred stock | 18,023 | 0 | new |
| Shares outstanding | 12,230 | 12,088 | +1.17% |
| **Implied net cash (cash+ST inv − debt − fin. leases)** | **~138,799** | ~75,000 | +85% |
| **Implied common equity (derived, ≈assets − liabilities)** | **~600,000** | ~415,000 | +~45% |

**Analysis**

- **Liquidity is not a constraint.** $242.5B of cash and short-term investments covers total debt (~$103.7B incl. finance leases) **2.3x**. Implied book value per share ≈ **$49** (~$48 common + ~$1.50 preferred), up sharply on retained earnings plus issuance.
- **But the financing mix has shifted from internally funded to externally funded.** Debt +$52.0B, common equity +$30.5B, convertible preferred +$19.1B, minority interests +$3.76B in six months. Only a company seeing an enormous, time-limited AI opportunity would both double leverage and issue equity at scale.
- **The preferred is cheap capital:** $19.06B raised with only **$86M** of preferred dividends in the quarter → an implied coupon of **~1.8% annualised**. Either a very low-coupon convertible structure or capital provided by a strategic partner in an infrastructure vehicle.
- **Asset-side composition is the red flag.** ~$124B of the balance sheet is non-marketable equity carried at model-derived fair value, with **$85.7B of cumulative upward marks** accumulated. Meanwhile the **$22.8B net DT liability** is the tax bill attached to those marks.
- **AFS securities were extended in duration:** fair-value loss positions under 12 months jumped to **$49.35B** (from $6.52B) with $266M of unrealised loss, and 5–10 yr plus >10 yr tranches now total **$32.1B** within a $99.5B book — a rate-risk sensitivity that did not exist at year-end.
- **Working capital is being stretched, not squeezed:** AP +66%, accrued liabilities +31%, taxes payable +65% — a modest but real source of cash that flatters H1 OCF.
- **Legal/regulatory reserves are large and growing:** $17.36B current loss-contingency accrual (+$1.76B in six months), on top of $3.0B paid out in Q3 2025 per the 10-K.

---

## 5. Cash Flow — the most important table in this report

| $M | H1 2026 | H1 2025 | Change |
|---|---|---|---|
| **Operating cash flow** | **84,859** | 63,897 | **+32.8%** |
| Capex (PP&E purchases) | **(80,598)** | (39,643) | **+103.3%** |
| **Free cash flow (OCF − capex)** | **4,261** | 24,254 | **−82.4%** |
| Purchases of marketable securities | (76,480) | (39,870) | +91.8% |
| Sales/maturities of marketable securities | 66,696 | 40,930 | +62.9% |
| Purchases of other investments | (22,051) | (2,312) | ~9.5x |
| **Investing cash flow** | **(145,822)** | (40,738) | ~3.6x |
| Debt issued, net | 56,226 | 31,378 | +79.2% |
| Debt repayments | (5,253) | (18,397) | −71.5% |
| **Common stock issued** | **30,499** | 0 | new |
| **Convertible preferred issued** | **19,063** | 0 | new |
| Minority interest proceeds | 3,758 | 400 | ~9.4x |
| Dividends paid | (5,231) | (4,977) | +5.1% |
| **Share repurchases** | **0** | (28,306) | **−100%** |
| **Financing cash flow** | **+86,320** | (26,033) | flip |
| Net change in cash | +25,203 | (2,430) | — |

**Quarterly detail:**
- Q2 2026 OCF **$39,069M**; capex **$44,924M** → **FCF −$5,855M** (Q2 2025: +$5,301M).
- Q1 2026 OCF **$45,790M**; capex **$35,674M** → FCF **+$10,116M**.
- Depreciation H1 was only **$13,586M** (vs $9,485M, +43%) — i.e. **D&A equals just 17% of H1 capex**. A very large depreciation wave is contractually coming, which will compress margins and FCF further in 2027+ unless revenue compounds at similar pace.
- `CapitalExpendituresIncurredButNotYetPaid` **$29,113M** vs $10,635M a year ago: capex is *running ahead of cash payments*, so reported capex still understates the committed build.

**Interpretation:** Alphabet is running a **self-funded-plus-external-capital AI infrastructure super-cycle**. OCF growth (+33%) is excellent, but it is fully absorbed — and then some — by capex. The "cash machine" narrative has, for now, been replaced by "capex machine, funded with debt and equity."

---

## 6. Earnings Quality Scorecard — what to discount

| Issue | Evidence | Trader takeaway |
|---|---|---|
| Operating income is only 29% of Q2 pretax income | Operating $40.77B vs non-operating $97.98B | **Use ex-gains EPS.** Headline P/E is misleading by ~3–4x on the earnings denominator |
| Gains are largely mark-to-model | Non-marketable equity $124.3B, cumulative upward marks $85.7B | Subject to reversal; a down-round quarter could produce a GAAP loss despite record operations |
| Deferred tax liability $22.8B | vs $0.92B at YE25 | Cash tax/rate friction ahead; DTL is the tax on unrealised gains |
| Effective tax rate drift | 19.1% vs 16.9% | −2.2pt headwind structurally, separate from the new interest burden |
| SBC rising faster than revenue | $15.2B H1, +32% YoY | Real economic cost; ~6.6% of revenue |
| Share count up 1.17% in 6 months | 12,088M → 12,230M | First non-trivial dilution in years; convert preferred adds future dilution |
| Buyback eliminated | $0 vs $28.3B | Removes the historical EPS floor/accretion engine |
| AP and taxes payable up sharply | AP +66%, taxes payable +65% | ~$10–12B of H1 OCF benefit is working-capital timing |
| Loss contingency $17.4B | +$1.76B in 6 months | Regulatory/antitrust tail risk is live and sized |

---

## 7. Growth Drivers, Catalysts and Risks

**Positive drivers visible in the data**
- Revenue +23–24% at ~$120B quarterly scale — extraordinary for a company this size; acceleration from H1 2025's base.
- Gross margin expansion of 240bp with cost of revenue growth (+16%) at two-thirds the revenue rate → mix shift toward higher-margin compute/cloud/ads efficiency.
- Contract liabilities $10.1B (+17%) and $4.9B recognised from backlog: forward revenue visibility improving.
- Operating margin at 34–35% — record territory — despite SBC and infrastructure spend stepped up.
- Balance sheet capacity remains enormous (~$139B implied net cash; 2.3x debt coverage): the build-out is fundable without distress.

**Risks the data makes concrete**
- **FCF squeeze / capex funding risk:** a negative Q2 FCF quarter with $29.1B of capex incurred-but-unpaid. If revenue decelerates while capex doesn't, capital raises become recurring.
- **Depreciation cliff:** D&A at 17% of capex means margin compression is deferred, not avoided.
- **Mark-to-model volatility:** $124B of level-3-ish equity assets can swing reported EPS by several dollars per share in either direction.
- **Leverage/interest:** debt +106% and interest expense +514% in H1.
- **Legal:** $17.4B current contingency accrual and rising.
- **Rate/duration risk:** $49.4B of AFS securities sitting in sub-12-month unrealised loss positions.
- **Data limitation:** no insider-transaction archive is available for GOOGL here, so no read on management/insider conviction can be given. This should be sourced separately before acting.

---

## 8. Actionable Framework for Traders

1. **Trade the core, ignore the headline.** Anchor valuation on core EPS: H1 2026 ≈ **$5.35–5.40** (≈$10.7–10.8 annualised at current trajectory, before further gains). Reported $14.24 H1 EPS is not a valuation input. Any screener showing an ultra-low P/E on GOOGL right now is using inflated GAAP earnings.
2. **Watch FCF, not EPS, as the catalyst variable.** Q2 FCF −$5.9B is the single most important line in the filing. Q3 (reporting late October 2026) needs capex ≤ ~$42–45B and OCF ≥ ~$45B for FCF to turn positive again. A second consecutive negative FCF quarter is the most likely trigger for a de-rating of the "cash-compounder" multiple.
3. **Confirm the core engine is intact.** The bull case needs H1's +23% revenue and 35% operating margin to persist. If revenue growth holds ≥20% and operating margin stays ≥33% while capex is digested, the core is compounding at 25%+ and the stock is fundamentally supported. If margin slips below ~32% *and* growth decelerates, the capex is not earning its cost of capital.
4. **Respect the asset-value optionality but do not pay full price for it.** The $124B non-marketable portfolio at $85.7B of cumulative marks is real economic value (AI/space/tech private stakes) but illiquid. Ascribing it at a haircut (say 30–50%) is prudent; the DT liability means ~20% of any realisation goes to tax.
5. **Capital structure signals management conviction.** Issuing $30.5B of common stock and $19.1B of convertible preferred while suspending buybacks is a strong statement that management believes the marginal return on AI infrastructure exceeds the cost of equity. Historically, GOOGL issuing equity would be a warning; here it reads as aggressive, opportunity-driven funding — but it lowers per-share compounding versus the 2023–25 buyback era.
6. **Dividend is a small signal.** $0.22/quarter, +4.8% — continued commitment, immaterial to total return.
7. **Positioning implication:** the fundamentals support a *constructive* but *quality-adjusted* stance — strong operating momentum and fortress liquidity argue for upside; collapsing FCF, doubling leverage, a $22.8B DT liability and a $124B mark-to-model asset base argue for a discounted multiple and tight risk controls around the Q3 print.

---

## 9. Key Metrics Summary Table

| Category | Metric | Value | Context / Signal |
|---|---|---|---|
| Reporting | Latest filing | 10-Q, period 2026-06-30, filed 2026-07-23 | Point-in-time, fresh (<1 week) |
| Scale | Q2 2026 revenue (derived) | $119.80B | +24.2% YoY |
| Scale | H1 2026 revenue (derived) | $229.69B | +23.1% YoY |
| Profitability | Q2 operating income / margin | $40.77B / 34.0% | +30.4% YoY, +160bp |
| Profitability | H1 operating income / margin | $80.47B / 35.0% | +30.0% YoY, +190bp |
| Profitability | H1 gross margin | 62.0% | +240bp YoY |
| Earnings | Q2 net income | $112.19B | +298% YoY (gain-inflated) |
| Earnings | H1 net income / diluted EPS | $174.77B / $14.24 | +179% / +178% YoY |
| **Earnings quality** | **Q2 non-operating income** | **$97.98B (71% of pretax)** | **Equity gains $99.03B — exclude** |
| **Earnings quality** | **Est. core H1 EPS (ex-gains)** | **~$5.35–5.40** | **~+23% YoY — the real growth rate** |
| Earnings quality | SBC (H1) | $15.20B | +32% YoY; 6.6% of Q2 revenue |
| Tax | Effective tax rate | 19.1% | +220bp YoY |
| Cash flow | H1 OCF | $84.86B | +32.8% YoY |
| Cash flow | H1 capex | $80.60B | +103.3% YoY; 35.1% of revenue |
| **Cash flow** | **H1 FCF** | **$4.26B** | **−82.4% YoY** |
| **Cash flow** | **Q2 2026 FCF** | **−$5.86B** | **Negative quarter — key watch item** |
| Cash flow | Capex incurred, unpaid | $29.11B | vs $10.64B LY — more outflow queued |
| Cash flow | Depreciation (H1) | $13.59B | Only 17% of capex → future margin drag |
| Balance sheet | Total assets | $921.98B | +54.9% in 6 months |
| Balance sheet | Cash + short-term investments | $242.47B | +91.2%; 2.3x debt |
| Balance sheet | Total debt (carrying) | $101.09B | +105.9%; interest expense +514% |
| Balance sheet | Net cash (implied) | ~$138.8B | Still a fortress |
| Balance sheet | Non-marketable equity | $124.26B | +93.9%; $85.73B cumulative up-marks |
| Balance sheet | Net deferred tax liability | $22.82B | ~25x increase — tax tail on marks |
| Balance sheet | Implied common equity / BVPS | ~$600B / ~$49 | ~22% ex-gains annualised ROE |
| Balance sheet | Shares outstanding | 12,230M | +1.17% in 6 months |
| Capital returns | H1 buybacks | $0 | vs $28.31B LY — suspended |
| Capital returns | H1 dividends / DPS | $5.23B / $0.43 | DPS raised to $0.22/qtr |
| Capital raising | H1 debt issued / common / preferred | $56.23B / $30.50B / $19.06B | Preferred coupon ~1.8% annualised |
| Contingencies | Loss contingency accrual (current) | $17.36B | +$1.76B in 6 months |
| Insider activity | GOOGL insider transactions | **DATA UNAVAILABLE** | Not inferable — source separately |
| Market data | Price / market cap / multiples | **Not in dataset** | Apply externally to core EPS |

**Bottom line for GOOGL:** operationally the strongest Alphabet has ever been at the revenue and operating-margin line; financially the most leveraged and least cash-generative it has been in a decade; and on a reported basis the most distorted by investment markups. Trade the operating momentum (+23% revenue, 35% margins), but price it on **core EPS (~$10.7–10.8 annualised) and FCF** — and treat a second consecutive negative-FCF quarter as the primary risk signal.