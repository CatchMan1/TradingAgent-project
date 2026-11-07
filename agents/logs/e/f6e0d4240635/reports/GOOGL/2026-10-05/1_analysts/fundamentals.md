# GOOGL — Fundamental Deep Dive (point-in-time: 2026-10-05)

**Ticker:** GOOGL | **Company:** Alphabet Inc. (SEC CIK 0001652044)

---

## 1. Bottom line

- **No new fundamental data this week.** The most recent filing in the vendor's point-in-time archive is the **Q2 2026 Form 10-Q, accepted 2026-07-23**. Nothing new was accepted between 2026-09-28 and 2026-10-05. This report is therefore a re-underwriting of the Q2 print, not a reaction to fresh news.
- **Operating momentum is exceptional and accelerating.** Derived revenue was **$119.8B in Q2 2026 (+24.2% y/y)** after **$109.9B in Q1 (+21.8%)**; H1 revenue **$229.7B (+23.1%)**. Gross margin expanded ~215bp y/y to 61.6% and operating margin ~160bp to 34.0%.
- **But GAAP EPS is badly distorted.** Q2 diluted EPS of **$9.11** includes a **$99.0B non-operating equity-securities gain**; H1 non-operating income was **$135.7B vs $13.8B** a year ago. Our **core (ex-investment gains) EPS is ~$2.60 for Q2 and ~$5.27 for H1**, up ~17% and ~20% y/y respectively — good, but nowhere near the headline.
- **The cash-flow story has inverted.** H1 operating cash flow rose 32.8% to **$84.9B**, but capex doubled to **$80.6B**, leaving **free cash flow of just $4.3B (-82% y/y)**; Q2 FCF was **negative ~$5.9B**. Capex is now **35% of revenue** and capex incurred-but-unpaid jumped to **$29.1B**, pointing to further acceleration.
- **The balance sheet was re-levered and diluted to fund the build/acquisitions.** Gross debt rose **+106% to $101.1B**, common stock was issued for **$30.5B**, **$19.1B of convertible preferred** was sold, and buybacks went to **zero** (vs $28.3B in H1 2025). Liquidity remains enormous: **$242.5B cash + short-term investments vs $101.1B debt = ~$141B net cash**.

**Stance:** fundamentally strong franchise, but this is a **"show-me" period on capex discipline and FCF**. Trade the core numbers, not the GAAP EPS headline; the Q3 print (expected late October) is the next real catalyst.

---

## 2. Data provenance and gaps

| Filing | Period | Filed / accepted | Accession |
|---|---|---|---|
| Form 10-K | FY2025 | 2026-02-05 | 0001652044-26-000018 |
| Form 10-Q | Q1 2026 | 2026-04-30 | 0001652044-26-000048 |
| Form 10-Q | Q2 2026 | 2026-07-23 | 0001652044-26-000071 |

**Important limitations (do not gloss over these):**
- **Insider transactions: DATA_UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for GOOGL. There is **no insider buying/selling signal** in this report — treat insider sentiment as *unknown*, not neutral, and do not infer it.
- **No market price / valuation multiples** were returned by the toolset. Per-share metrics below are given so the prevailing quote can be applied.
- Segment-level revenue (Google Services / Google Cloud / Other Bets) was **not** returned in the field set. Segment commentary is qualitative and flagged as inference.
- Full FY2023–FY2025 income statements were not returned in the capped field set. Revenue for the reported periods below is **derived exactly** from the identity `Revenue = CostsAndExpenses + OperatingIncomeLoss`; FY-level history is limited to the cash-flow/capex items that were returned.

---

## 3. Company profile and business model

Alphabet Inc. is the parent of Google and one of the world's largest advertising and cloud-computing companies. It reports three segments — **Google Services** (Search, YouTube ads, subscriptions/platforms/devices, including Android, Play and Pixel), **Google Cloud** (infrastructure, data analytics, AI/workspace), and **Other Bets** (e.g., Waymo, Verily and other long-dated ventures). The economic engine is advertising, with Cloud as the second profit pool and a growing subscription/device layer.

Capital structure detail from the filing: **300B shares authorized at $0.001 par**, with **12.230B shares outstanding at 2026-06-30** across Class A (GOOGL, one vote), Class B (insider, super-voting) and Class C (GOOG, no vote). The dual-class structure keeps founder control durable and is relevant to any activist/thesis-change scenario.

What the numbers say about the current operating model:
- Revenue growth of **~22–24%** on a ~$230B half-year base is well above the mature-advertising-company template and implies Cloud/AI and/or pricing strength; mix cannot be verified from this feed.
- Gross margin above 60% alongside **depreciation +43% y/y** and **cost of revenue +17.7%** indicates the AI compute build is being absorbed without gross-margin erosion so far.
- **SBC of $15.2B in H1 (+32% y/y, 6.6% of revenue)** and **G&A +23% y/y** show the opex side is also inflating.

---

## 4. Q2 2026 income statement (derived where noted)

| $B unless stated | Q2 2025 | Q1 2026 | Q2 2026 | Q2 y/y |
|---|---:|---:|---:|---:|
| Revenue (derived) | 96.4 | 109.9 | **119.8** | **+24.2%** |
| Cost of revenue | 39.0 | 41.3 | 45.9 | +17.7% |
| Gross profit | 57.4 | 68.6 | 73.9 | +28.7% |
| **Gross margin** | 59.5% | 62.4% | **61.6%** | **+215bp** |
| Operating expenses | 26.1 | 28.9 | 33.1 | +26.7% |
| — G&A | 5.2 | 4.3 | 6.5 | +24.0% |
| Operating income | 31.3 | 39.7 | **40.8** | **+30.4%** |
| **Operating margin** | 32.4% | 36.1% | **34.0%** | **+160bp** |
| Non-operating income | 2.7 | 37.7 | **98.0** | n/m |
| Pre-tax income | 33.9 | 77.4 | 138.8 | +309% |
| Tax | 5.7 | 14.8 | 26.6 | — |
| **Effective tax rate** | 16.9% | 19.2% | **19.1%** | +220bp |
| Net income | 28.2 | 62.6 | 112.2 | +298% |
| Diluted EPS ($) | 2.31 | 5.13 | **9.11** | +294% |
| **Core EPS ex-investment gains ($)** | **2.22** | **2.66** | **~2.60** | **+17%** |
| SBC | 6.0 | 7.2 | 8.0 | +33% |
| Diluted shares (M, implied) | 12,206 | ~12,300 | ~12,306 | +0.8% |

**Actionable reads:**
- **Operating leverage is real:** gross profit grew 28.7% on 24.2% revenue growth; operating income grew 30.4%. Cost of revenue growth (17.7%) lagged revenue by ~650bp.
- **Q2 margins dipped sequentially (36.1% → 34.0%) because opex stepped up 14.4% q/q**, led by G&A (+50.6% q/q, +$2.2B). The **loss-contingency accrual rose from $15.6B to $17.4B** in H1 — consistent with at least **~$1.8B of net legal/regulatory charge**, most likely in Q2 G&A. Adding that back, Q2 operating margin is ~35.5% and core EPS ~**$2.72**.
- **Tax is a new headwind:** 19.1% vs 16.9% a year ago, driven substantially by deferred tax on the investment mark-ups (deferred tax liabilities rose from $0.9B to $22.8B). Core net margin compressed to ~26.8% from ~28.1% despite better operating margins.
- **Interest expense went from $0.26B to $1.28B in Q2 (+390% y/y)** as debt doubled; interest income of $1.43B still covers it.

---

## 5. Earnings quality: the $99B question

This is the single most important analytical issue in the print.

- H1 2026 non-operating income: **$135.7B**, of which **equity-securities gains $135.9B** (vs $11.0B in H1 2025). Q2 alone: **$99.0B**.
- **It is non-cash.** Cash flow shows only **$1.67B of proceeds from sale/maturity of other investments** in H1. Nothing was monetized at scale.
- Balance-sheet corroboration: **equity securities without readily determinable fair value rose from $64.1B to $124.3B (+94%)**, with cumulative upward fair-value adjustments rising from **$44.5B to $85.7B (+$41.2B)**, plus **$22.1B of new "other investment" purchases** (vs $2.3B in H1 2025).
- **Deferred tax liabilities jumped from $0.9B to $22.8B** — management is providing for tax on these gains, i.e., they are not treated as tax-free.
- Non-marketable stakes are marked to fair value through the income statement, so **this line will be volatile in both directions** and is not a valuation anchor for the operating business.

**Trading implication:** any screen showing GOOGL at a mid-single-digit P/E on Q2 EPS ($9.11 annualized ≈ $36) is mechanically wrong. Use **~$10.5–11.5 of 2026 core EPS** as the earnings base (H1 core $5.27 × 2, plus modest H2 growth), and value the investment portfolio separately at a discount to its $124B+ carrying value.

---

## 6. Balance sheet: bigger, stronger, and more levered

| $B | 2025-12-31 | 2026-06-30 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 30.7 | 55.9 | +82% |
| Cash + short-term investments | 126.8 | **242.5** | **+91%** |
| Accounts receivable, net | 62.9 | 69.2 | +10% |
| Current assets | 206.0 | 343.5 | +67% |
| **Total assets** | 595.3 | **922.0** | **+54.9%** |
| Accounts payable | 12.2 | 20.3 | +66% |
| Accrued liabilities | 55.6 | 73.0 | +31% |
| **Debt (carrying)** | 49.1 | **101.1** | **+106%** |
| Deferred tax liabilities | 0.9 | 22.8 | +2,383% |
| Operating lease liabilities | 16.0 | 18.0 | +13% |
| Finance lease liabilities | 2.5 | 2.6 | +4% |
| Contract liabilities (deferred revenue) | 8.6 | 10.1 | +17% |
| Loss contingency accrual (current) | 15.6 | 17.4 | +11% |
| **Equity securities w/o readily determinable FV** | 64.1 | **124.3** | **+94%** |
| Convertible preferred stock | 0.0 | **18.0** | new |
| Common stock + APIC | 93.1 | 131.4 | +41% |
| AOCI | (1.9) | (2.3) | — |
| Shares outstanding (B) | 12.088 | 12.230 | +1.2% |

**Liquidity and leverage:**
- **Net cash = $242.5B − $101.1B = ~$141.4B**; even including $20.6B of lease liabilities, net cash is **~$121B**.
- Current ratio ≈ **2.6–2.8x** (current assets $343.5B vs estimated current liabilities of ~$125–135B, including $73.0B accrued liabilities, $20.3B AP, $15.1B employee liabilities, $7.2B contract liabilities and $5.2B current tax).
- Gross debt/EBITDA ≈ **0.5x**; net cash/EBITDA ≈ **−0.75x**. Interest coverage ~**44x** (H1 operating income $80.5B / interest $1.8B). Balance-sheet risk is low; **capital-allocation risk is the issue, not solvency**.
- **$53.2B of AFS debt securities sit in an unrealized-loss position**, but accumulated unrealized loss is only $0.4B — a rate-duration nuisance, not a credit problem.

---

## 7. Cash flow and capital allocation: the regime change

| $B | H1 2025 | H1 2026 | Change |
|---|---:|---:|---:|
| Operating cash flow | 63.9 | **84.9** | +32.8% |
| Capex (PP&E purchases) | 39.6 | **80.6** | **+103.3%** |
| **Free cash flow** | **24.3** | **4.3** | **−82.4%** |
| Capex / revenue | 21.2% | **35.1%** | +1,390bp |
| FCF margin | 13.0% | 1.9% | −1,110bp |
| Share repurchases | 28.3 | **0.0** | −100% |
| Ordinary dividends | 5.0 | 5.2 | +5% |
| Debt issued (net of costs) | 31.4 | **56.2** | +79% |
| Debt repaid | 18.4 | 5.3 | −71% |
| Common stock issued | 0.0 | **30.5** | new |
| Convertible preferred issued | 0.0 | **19.1** | new |
| Minority-interest proceeds | 0.4 | 3.8 | +840% |
| Investing cash flow | (40.7) | **(145.8)** | worse |
| Financing cash flow | (26.0) | **+86.3** | swing |

**Quarterly FCF decomposition:**

| $B | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 |
|---|---:|---:|---:|---:|
| OCF | 36.2 | 27.7 | 45.8 | 39.1 |
| Capex | 17.2 | 22.4 | 35.7 | **44.9** |
| **FCF** | **19.0** | **5.3** | **10.1** | **(5.9)** |

**Actionable reads:**
- **Capex is compounding ~100% y/y and is now 6.6x quarterly depreciation** ($44.9B vs ~$6.8B). **Capex incurred but not yet paid rose from $10.6B to $29.1B**, a leading indicator that Q3 capex likely exceeds Q2's $44.9B.
- **Management funded the gap externally, not from cash flow**: $56.2B debt + $30.5B equity + $19.1B convertible preferred + $3.8B minority proceeds = **~$109.6B raised in six months**. For a company that repurchased $28.3B of stock in the prior-year half, this is a complete capital-allocation reversal.
- **Buybacks at zero and share count up 142M (+1.2%)** means the historical EPS tailwind from shrinking the float is gone; SBC and deal-related issuance now grow the count.
- **The $19.1B convertible preferred (issued 2026-06-05)** carries ~$86M of dividends in roughly one month of accrual, implying a **~6.5–7% annualized coupon**, and is **convertible** — a real future dilution overhang whose conversion terms are not in the returned data.
- Dividends were **raised to $0.22/qtr** (from $0.21): annualized **$0.88/share**, ~8% of core net income. The dividend is safe but is no longer the marginal use of cash.

---

## 8. Financial history: what the multi-year markers show

| Marker | 2023 | 2024 | 2025 | H1 2026 |
|---|---:|---:|---:|---:|
| Capex incurred but not yet paid ($B) | 7.4 | 10.3 | 15.1 | **29.1** |
| Financing cash flow ($B) | (72.1) | (79.7) | (37.4) | **+86.3** |
| Finance-lease principal payments ($B) | 0.71 | 0.41 | 1.99 | 0.84 |

- The **capex accrual line has grown ~4x in three years**, confirming this is a multi-year infrastructure program, not a one-quarter spike.
- The **financing swing from −$37.4B (FY2025) to +$86.3B (H1 2026)** is the cleanest evidence of the regime change: Alphabet went from returning capital to raising it.
- Debt maturity profile as of 2025-12-31 ($B): **2.0 due within 12 months, 1.0 in yr 2, 2.7 in yr 3, 1.8 in yr 4, 5.5 in yr 5, 36.1 after yr 5** — before the 2026 issuance. Near-term refinancing risk is negligible; the new debt lengthens the stack.
- H1 2025 → H1 2026 trajectory: revenue **+23.1%**, operating income **+30.0%**, operating margin **33.2% → 35.0%**, OCF **+32.8%**, capex **+103%**, FCF **−82%**. That single line summarizes the bull and bear case.

---

## 9. Valuation framing (price-independent)

Because no quote was provided, here is the arithmetic a trader should apply:

- **Core EPS base:** H1 2026 core **$5.27**; annualized **~$10.5**; with 8–10% H2 progression, **~$11.0–11.5** is a reasonable 2026 core run-rate.
- **GAAP EPS is not usable:** Q2 $9.11 included ~$8.05/share of after-tax investment gains (99.0 × 0.809 / 12.3 ≈ $6.51… plus Q1's gains make H1 GAAP $14.24 vs core $5.27).
- **EBITDA run-rate:** H1 operating income $80.5B + D&A $14.1B = **$94.6B**, or **~$189B annualized**; adding back SBC ($15.2B H1) gives **~$220B annualized adjusted EBITDA**.
- **Enterprise value adjustment:** subtract **~$141B net cash** and add **~$18B preferred**; the **$124B non-marketable equity portfolio** is an asset that screens rarely capture.
- **Core ROA:** annualized core net income (~$130B) / average assets ($758.6B) ≈ **17%** — still elite for a company this capital-intensive.

---

## 10. Risks and red flags

1. **FCF compression / capex super-cycle.** Q2 FCF negative; capex 35% of revenue and accelerating (unpaid capex $29.1B). If 2026 capex lands near $180B against ~$180B OCF, **FY2026 FCF could be ~zero**. Depreciation (+43% y/y) will be a multi-year margin headwind (~$30B/yr of incremental depreciation for every $180B of 6-year-life capex).
2. **External financing and dilution.** +$52B debt, +$30.5B equity, +$19.1B convertible preferred, +142M shares, SBC +32%. The convertible's terms are the key unknown for fully diluted share count.
3. **Earnings quality.** 63% of H1 pre-tax income ($135.9B of $216.2B) came from non-cash investment revaluations. A down-round in a private holding would hit the P&L just as violently in reverse.
4. **Concentration/opacity of the investment book.** $124.3B of non-marketable equity plus $22.1B of new "other investments" in H1 — with no counterparty disclosure in the returned data. This is a large, mark-to-model exposure.
5. **Tax rate step-up.** 19.1% vs 16.9% cuts core EPS growth by roughly 2.5 points; further mix/legislative pressure is possible.
6. **Legal/regulatory.** Loss-contingency accrual $17.4B (+11% in six months); $3.0B was paid in Q3 2025 per the FY2025 10-K. Antitrust/regulatory remedies remain a tail risk to the advertising franchise.
7. **Information vacuum.** 10+ weeks since the last filing, no insider data, no segment data. Event risk into the Q3 report is elevated.
8. **No buyback bid.** With repurchases at zero, a key historical source of downside support is absent.

---

## 11. What would change the thesis

**Bull confirmations to watch:**
- Q3 capex **below** Q2's $44.9B, or explicit guidance that 2027 capex growth decelerates → FCF trough signature.
- **Buyback resumption** (any authorization restart) → management signaling the investment peak.
- Cloud/AI revenue acceleration with stable 60%+ gross margin and 34%+ operating margin.
- Realization/monetization of part of the $124B private portfolio (cash proceeds, not marks).
- Clarity that the $30.5B stock + $19.1B preferred were deployed into accretive assets with disclosed returns.

**Bear confirmations:**
- Q3 capex >$50B and another negative FCF quarter.
- Further equity/preferred issuance, or conversion terms that imply >2% dilution.
- A down-mark on the investment book.
- Gross margin slipping below ~60% as depreciation ramps.
- Operating margin below ~33% on legal/AI opex.

---

## 12. Trader playbook

- **Do not trade the headline.** Q2 GAAP EPS $9.11 vs core ~$2.60; H1 $14.24 vs ~$5.27. Rebuild models on core EPS and EBITDA.
- **Anchor on the Q3 print (expected late October).** The three numbers that matter, in order: **capex**, **FCF**, **Cloud growth**. A capex number below ~$45B with intact growth is the cleanest long trigger; a >$50B print with negative FCF likely caps the multiple regardless of revenue.
- **Watch the capital-return queue.** Zero buybacks + rising share count is a sentiment negative; a restart is a high-quality positive surprise.
- **Treat the $135.9B investment gain as a sum-of-the-parts item, not earnings.** Apply a discount to the $124B private portfolio for illiquidity and tax (DTL already $22.8B).
- **Position sizing:** with no filings for 10 weeks and no insider signal available, gap risk into Q3 is real. Consider expressing views via options around the print rather than outright directional size.
- **For long-term holders:** the franchise is compounding revenue at 22–24% with 35% operating margins and $141B net cash. The debate is purely whether ~$80–90B of half-year capex earns an adequate return. Evidence of a capex plateau — not the current quarter's revenue — is what re-rates the stock.

---

## 13. Key points summary

| Category | Metric | Value | Signal |
|---|---|---|---|
| Freshness | Latest SEC filing | Q2 2026 10-Q, accepted 2026-07-23 | Neutral — 10-week information vacuum |
| Growth | Q2 2026 revenue | $119.8B, **+24.2% y/y** | Bullish |
| Growth | H1 2026 revenue | $229.7B, **+23.1% y/y** | Bullish |
| Profitability | Q2 gross margin | 61.6% (+215bp y/y) | Bullish |
| Profitability | Q2 operating margin | 34.0% (+160bp y/y) | Bullish |
| Profitability | H1 operating margin | 35.0% (vs 33.2%) | Bullish |
| Earnings quality | H1 non-operating income | $135.7B, of which $135.9B equity gains | **Bearish — non-cash** |
| Earnings | Q2 GAAP diluted EPS | $9.11 | Misleading |
| Earnings | Q2 **core** EPS (ex-gains) | **~$2.60 (+17% y/y)** | Modestly bullish |
| Earnings | H1 core EPS | **~$5.27 (+20% y/y)** | Bullish |
| Tax | Effective tax rate | 19.1% (vs 16.9%) | Bearish |
| Cash flow | H1 operating cash flow | $84.9B (+32.8%) | Bullish |
| Cash flow | H1 capex | $80.6B (+103%) | **Bearish** |
| Cash flow | H1 free cash flow | $4.3B (**−82%**) | **Bearish** |
| Cash flow | Q2 free cash flow | **−$5.9B** | **Bearish** |
| Capex | Capex / revenue | 35.1% (vs 21.2%) | Bearish |
| Capex | Capex incurred, unpaid | $29.1B (vs $10.6B) | Bearish — more capex coming |
| Balance sheet | Cash + ST investments | $242.5B | Bullish |
| Balance sheet | Gross debt | $101.1B (+106% in 6M) | Neutral — still net cash |
| Balance sheet | Net cash | **~$141.4B** | Bullish |
| Balance sheet | Total assets | $922.0B (+54.9% in 6M) | Neutral |
| Investments | Non-marketable equity | $124.3B (+94%) | Neutral/opaque |
| Capital return | Buybacks H1 2026 | **$0** (vs $28.3B) | Bearish |
| Capital return | Dividend | $0.22/qtr, $0.88 annualized | Neutral |
| Dilution | Shares outstanding | 12.230B (+1.2% in 6M) | Mildly bearish |
| Dilution | Convertible preferred | $18.0B issued 2026-06-05 | Bearish overhang |
| Leverage | Interest expense Q2 | $1.28B (+390% y/y) | Watch item |
| Legal | Loss contingency accrual | $17.4B (+11%) | Bearish |
| Insider | Insider transactions | **Data unavailable** | Unknown — not neutral |
| Valuation | 2026 core EPS base | **~$10.5–11.5** | Use instead of GAAP |
| Valuation | Annualized adj. EBITDA | ~$189B GAAP / ~$220B incl. SBC | Input for EV multiples |

**Net assessment:** GOOGL's operating business is firing on all cylinders — accelerating revenue, expanding gross and operating margins, and a fortress net-cash position. The offset is a capital-allocation regime that has turned aggressively expansionary, producing negative quarterly FCF, $100B+ of debt, a new $18B convertible, and zero buybacks. The stock's next move will be decided less by demand and more by whether management demonstrates a capex plateau. Until then, the fundamental picture is **"great company, uncertain cash return"** — own it for the franchise, but underwrite it on core EPS (~$10.5–11.5) and FCF, not the $9.11 quarterly GAAP headline.