# AMZN — Fundamental Research Report
**As of 2026-09-24 | Latest public filing in the data set: Form 10-Q for the quarter ended 2026-06-30 (accepted 2026-07-31, accn 0001018724-26-000026)**

---

## 0. Data provenance & scope (read this first)

Everything below is derived from **point-in-time SEC XBRL facts** filtered by actual EDGAR acceptance timestamp. Two filings are represented:

| Filing | Period | Accepted |
|---|---|---|
| 10-Q (FY2026 Q2) | Q2 2026 & H1 2026, plus Q2/H1 2025 comparatives | 2026-07-31 02:11 UTC |
| 10-Q (FY2026 Q1) | Q1 2026, plus Q1 2025 comparative | 2026-04-30 02:48 UTC |

**Important limitations of this extract — I will not fabricate these:**
- **No price, market cap, share-price multiples, consensus estimates, or guidance** are in the vendor package. I therefore cannot compute P/E, EV/EBITDA, or a price target.
- **No annual 10-K facts** are present (only these two 10-Qs and their comparative periods). FY2023/FY2024/FY2025 full-year statements could not be pulled.
- **No segment-level revenue or operating income** — only `NumberOfOperatingSegments = 3` is tagged.
- **Insider transactions: DATA_UNAVAILABLE.** The package contains no authorized, point-in-time insider-transactions archive for AMZN as of 2026-09-24. I have **no basis to characterize insider buying or selling** and will not infer it. Treat any insider narrative you see elsewhere as unverified against this dataset.
- Some tagged values appear **dimensionally mis-tagged** (e.g., `DebtSecuritiesAvailableForSaleUnrealizedGainLoss = $92.0B` for H1 2026 against an AFS portfolio with only $106.6B amortized cost and $7M of unrealized gain at 6/30/26 — mathematically impossible). I exclude such items and flag them rather than use them.
- Revenue is **derived** as `OperatingIncomeLoss + CostsAndExpenses` (both tagged). This reconciles exactly to historical reported Amazon revenue for Q2 2025 ($167,702M) and H1 2025 ($323,369M), so the derivation is reliable.

---

## 1. Company profile

Amazon.com, Inc. (AMZN) is a global technology and logistics conglomerate operating **three reportable segments** (confirmed in the 10-Q via `NumberOfOperatingSegments = 3`):

1. **North America** — online and physical retail, third-party marketplace, advertising, Prime subscriptions, logistics/fulfillment.
2. **International** — the same commerce and advertising model across non-US geographies.
3. **Amazon Web Services (AWS)** — cloud infrastructure, database, analytics, and AI/ML platform services.

The 2026 financials show the company in a **capital-intensity regime shift**: the business has re-accelerated revenue to ~19–20% growth while simultaneously more than doubling its debt load and roughly doubling capex year-over-year to build AI/cloud capacity. It is also carrying a very large, newly revalued private-equity stake that now drives the majority of GAAP earnings.

---

## 2. Headline results — Q2 2026 and H1 2026

### 2.1 Derived income statement ($ millions)

| Line item | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | **200,606** | 167,702 | **+19.6%** | **382,125** | 323,369 | **+18.2%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 183,241 | 157,785 | +16.1% |
| **Gross profit** | **104,828** | 86,893 | +20.6% | **198,884** | 165,584 | +20.1% |
| Gross margin | **52.3%** | 51.8% | +50 bp | **52.0%** | 51.2% | +82 bp |
| Marketing | 11,698 | 11,416 | +2.5% | 22,012 | 21,179 | +3.9% |
| G&A | 2,788 | 2,965 | −6.0% | 5,375 | 5,593 | −3.9% |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 330,812 | 285,793 | +15.8% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** | **51,313** | 37,576 | **+36.6%** |
| Operating margin | **13.69%** | 11.43% | **+226 bp** | **13.43%** | 11.62% | **+181 bp** |
| Interest expense | (1,314) | (516) | +154.7% | (2,114) | (1,057) | +100.0% |
| Interest income | 1,295 | 1,085 | +19.4% | 2,430 | 2,151 | +13.0% |
| **Non-operating income** | **53,396** | 1,686 | n.m. | **69,378** | 4,960 | n.m. |
| Pre-tax income | 80,857 | 20,857 | +287.7% | 120,691 | 42,536 | +183.7% |
| Income tax | 18,199 | 2,678 | +579.6% | 27,759 | 7,231 | +283.9% |
| Effective tax rate | 22.5% | 12.8% | +970 bp | 23.0% | 17.0% | +600 bp |
| **Net income** | **62,647** | 18,164 | +244.9% | **92,902** | 35,291 | +163.2% |
| Diluted EPS | **$5.75** | $1.68 | +242% | **$8.53** | $3.27 | +161% |
| Diluted shares (implied) | ~10,895M | ~10,811M | +0.8% | ~10,891M | ~10,793M | +0.9% |

### 2.2 The single most important fact: earnings are dominated by a non-cash mark-up

| Item | Q2 2026 | H1 2026 |
|---|---:|---:|
| Non-operating income | 53,396 | 69,378 |
| — of which: **upward revaluation of equity securities without readily determinable fair value** | **50,486** | **62,814** |
| Mark-up as % of pre-tax income | **62.4%** | **52.0%** |
| Carrying value of non-marketable equity securities (12/31/25 → 6/30/26) | 16,200 → **122,300** | **+$106.1B in six months** |

This is a **recurring-risk, non-cash fair-value mark on a private equity holding** (the size and timing are consistent with a large AI-lab stake such as Amazon's Anthropic position, though the filing extract does not name the counterparty). It added **$50.5B to Q2 revenue-less income** and is carried at **$122.3B — 11.2% of total assets**.

**Normalized ("core") earnings:**

| | Reported | Less mark-up (after ~23% tax) | Core | Core diluted EPS |
|---|---:|---:|---:|---:|
| Q2 2026 net income | $62,647M | −$39,127M | **~$23,520M** | **~$2.16** |
| Q1 2026 net income | $30,255M | −$9,493M | **~$20,762M** | **~$1.93** |
| H1 2026 net income | $92,902M | −$48,367M | **~$44,535M** | **~$4.09** |
| H1 2025 net income | $35,291M | −$66M | ~$35,225M | ~$3.26 |

**Read-through:** core EPS grew **~+25% YoY** (very healthy), but reported EPS of $8.53 overstates core earnings power by **>2x**. Any P/E computed on the $5.75 quarterly print is mechanically too cheap. This is the #1 adjustment a trader must make.

**Second-order risk:** the mark is symmetric. A 20% markdown of the $122.3B carrying value would cost ~$24.5B pre-tax (~$2.22/share) in a single quarter. Reported EPS for AMZN is now structurally high-beta to one private valuation.

### 2.3 Non-cash tax and cash conversion

| | Q2 2026 | H1 2026 | TTM (Jul-25→Jun-26) |
|---|---:|---:|---:|
| Income tax expense | 18,199 | 27,759 | — |
| Deferred tax expense | 17,691 | **30,489** | **41,441** |
| **Cash taxes paid** | **2,655** | **3,978** | **6,635** |
| Net income | 62,647 | 92,902 | 135,281 |
| Operating cash flow | 45,387 | 71,419 | 161,403 |

Cash taxes are only **14% of book tax expense** — because the gains generating the tax are unrealized. Reported net income ($135.3B TTM) runs **below** operating cash flow ($161.4B TTM), which is a favorable tell, but the gap is much smaller than the $135B earnings number would imply once you strip the mark.

---

## 3. Cost structure and operating leverage — the real bull case

Q2 2026 delivered **226 bp of operating-margin expansion** on 19.6% revenue growth. The mix of that expansion is unusually high quality because it came from **expense discipline, not cost deferral**:

| Ratio (% of revenue) | Q2 2026 | Q2 2025 | Δ | H1 2026 | H1 2025 | Δ |
|---|---:|---:|---:|---:|---:|---:|
| COGS | 47.74% | 48.19% | −45 bp | 47.95% | 48.79% | −84 bp |
| Marketing | 5.83% | 6.81% | **−98 bp** | 5.76% | 6.55% | −79 bp |
| G&A | 1.39% | 1.77% | −38 bp | 1.41% | 1.73% | −32 bp |
| Stock-based comp | 3.01% | 3.90% | −89 bp | 2.64% | 3.16% | −52 bp |
| D&A | **9.96%** | 9.08% | **+88 bp** | **10.19%** | 9.12% | **+107 bp** |

**Key insight:** margin expansion is being achieved *despite* a **+88 bp rise in D&A as a share of revenue** (Q2 D&A $19,988M, +31.3% YoY; H1 $38,933M, +32.0%). That means the underlying operating leverage — driven by advertising/AWS mix and marketing/SBC discipline — is even stronger than the headline. Conversely, **D&A will keep climbing** as the capex wave depreciates, so the D&A headwind (already ~1 pt of margin) intensifies into 2027.

- **Marketing grew only 2.5%** on 19.6% revenue growth — extraordinary leverage, and a sign of brand/Prime flywheel strength rather than bought growth.
- **G&A and SBC both declined in absolute dollars.** SBC not-yet-recognized: **$24.8B** (a real future expense overhang).
- **Interest expense +155% YoY** ($1,314M vs $516M) is the visible cost of the debt-funded build; it is still trivial vs. operating income (interest coverage ~21x in Q2), but the trajectory is steep.

---

## 4. Balance sheet — the big story is the AI investment cycle

### 4.1 Balance sheet ($ millions)

| Item | 6/30/2026 | 12/31/2025 | Change | % |
|---|---:|---:|---:|---:|
| Cash & equivalents | 78,213 | 86,810 | −8,597 | −9.9% |
| Available-for-sale debt securities | 97,900 | 45,800 | +52,100 | +113.8% |
| Accounts receivable (net) | 88,092 | 67,729 | +20,363 | **+30.1%** |
| Inventory (net) | 38,184 | 38,325 | −141 | −0.4% |
| **Current assets** | **249,264** | 229,083 | +20,181 | +8.8% |
| Non-marketable equity securities | 122,300 | 16,200 | +106,100 | +655% |
| Operating lease ROU asset | 92,743 | 86,054 | +6,689 | +7.8% |
| **Total assets** | **1,095,689** | 818,042 | **+277,647** | **+33.9%** |
| Accounts payable | 147,440 | 121,909 | +25,531 | +20.9% |
| Accrued liabilities | 73,406 | 75,520 | −2,114 | −2.8% |
| Long-term debt — current | 3,330 | 2,748 | +582 | +21.2% |
| **Current liabilities** | **241,274** | 218,005 | +23,269 | +10.7% |
| Long-term debt — noncurrent | 128,894 | 65,648 | +63,246 | **+96.3%** |
| **Total debt (ST+LT)** | **136,328** | 71,584 | **+64,744** | **+90.4%** |
| Finance lease liabilities | 13,451 | 12,286 | +1,165 | +9.5% |
| Operating lease liabilities | 96,320 | 89,252 | +7,068 | +7.9% |
| Deferred revenue (contract liabilities) | 24,878 | 26,016 | −1,138 | −4.4% |
| AOCI | 66,287 | 28,230 | +38,057 | +134.8% |
| Additional paid-in capital | 149,619 | 140,024 | +9,595 | +6.9% |
| Shares outstanding | 10,783M | 10,731M | +52M | +0.5% |

### 4.2 Liquidity and leverage

| Metric | 6/30/2026 | 12/31/2025 |
|---|---:|---:|
| Cash + AFS securities | $176,113M | $132,610M |
| Total debt incl. finance leases | $149,779M | $83,870M |
| **Net cash (ex-op leases)** | **+$26,334M** | **+$48,740M** |
| Gross debt + op leases | $246,099M | $173,122M |
| **Net debt (incl. op leases)** | **−$69,986M** | **−$40,512M** |
| Current ratio | **1.03x** | 1.05x |
| Working capital | $7,990M | $11,078M |

- **Leverage is still low in absolute terms.** Using TTM D&A of $75,200M and TTM operating income of roughly $96B (derived), EBITDA ≈ $171B, giving **net debt/EBITDA ≈ 0.4x ex-leases, ~1.4x including operating leases**. This is not a stretched balance sheet.
- **But the direction is clear:** net cash ex-leases fell from +$48.7B to +$26.3B in six months while debt nearly doubled. Gross debt plus leases is up **$73B** in two quarters.
- **Working capital is thin at 1.03x and $8.0B.** Negative-FCF plus thin working capital plus heavy purchase commitments means the company is now dependent on continued capital-markets access — a change from the 2022–2025 net-cash era.
- **Receivables are the one yellow flag in the working-capital stack:** AR **+30.1%** vs revenue +18.2%, and the allowance rose from $2.4B to $2.8B (+16.7%). DSO on Q2 revenue ≈ **40 days**. Not alarming, but worth monitoring for collection quality at AWS/enterprise customers.
- **Inventory flat (−0.4%) on +18% revenue** is a genuine efficiency positive and argues the growth is not being stuffed into the channel.

### 4.3 Off-balance-sheet commitments — $650 billion

| Obligation (6/30/2026) | $M |
|---|---:|
| Total contractual obligations | **650,034** |
| Remainder of fiscal 2026 | 42,752 |
| Due in next 12 months | 78,084 |
| Due in year 2 | 53,406 |
| Due in year 3 | 46,767 |
| Due in year 4 | 42,219 |
| Operating lease payments (undiscounted) | 116,350 |
| Finance lease payments (undiscounted) | 16,660 |
| Other commitments, remainder of FY | 2,145 |

**$650B of contracted obligations** — the overwhelming majority being forward purchase commitments for compute, content, and infrastructure — is the single best proxy this dataset offers for **AI demand visibility**, but it is also the single largest **execution/flexibility risk**. It locks in spend regardless of demand inflection and is why debt is rising.

Note the front-loaded shape: **$78.1B due within 12 months** plus $42.8B in the remainder of FY2026 — i.e., **~$121B of near-term fixed claims**, roughly 1.5x the cash pile.

---

## 5. Cash flow — negative free cash flow, by design

All figures $ millions. "Capex" = `PaymentsToAcquireProductiveAssets`.

| | Q2 2026 | Q2 2025 | Q1 2026 | H1 2026 | H1 2025 | TTM (Jul-25→Jun-26) |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash flow | 45,387 | 32,515 | 26,032 | **71,419** | 49,530 | **161,403** |
| Capex (productive assets) | (54,208) | (32,183) | (44,203) | **(98,411)** | (57,202) | **(173,028)** |
| **Free cash flow** | **(8,821)** | 332 | **(18,171)** | **(26,992)** | (7,672) | **(11,625)** |
| Business acquisitions, net | (24,359) | (1,700) | (15,408) | **(39,767)** | (1,652) | (41,956) |
| Purchases of marketable securities | (26,006) | (17,797) | (23,256) | (49,262) | (31,130) | (72,902) |
| Proceeds from sale/maturity of securities | 24,196 | 11,441 | 17,686 | 41,882 | 19,178 | 67,090 |
| **Investing cash flow** | (79,245) | (39,424) | (64,212) | **(143,457)** | (69,227) | **(216,775)** |
| LT debt issued | 13,557 | 0 | 53,441 | **66,998** | 746 | **81,925** |
| ST debt issued, net | (205) | 701 | (1,847) | (296) | 434 | 1,164 |
| LT debt repaid | (2,752) | (2,751) | 0 | (2,752) | (2,751) | (5,022) |
| Finance lease principal | (395) | (411) | (468) | (863) | (821) | (1,599) |
| **Financing cash flow** | 10,146 | (2,539) | 52,767 | **62,913** | (2,586) | **75,160** |
| FX effect on cash | (53) | 1,008 | (1) | (54) | 1,424 | (314) |
| **Net change in cash** | **(23,765)** | (8,440) | (7,452) | **(9,179)** | (20,859) | +19,474 |

### Interpretation
1. **Capex is the entire story.** H1 2026 capex **+72% YoY**; Q2 alone $54.2B (+68%). Annualized Q2 run-rate ≈ **$217B**. Capex is now **1.36x operating cash flow** in H1 (vs 1.16x in H1 2025).
2. **OCF growth is strong (+44% H1)** and funded most of it — the shortfall is being closed with **debt (+$67.0B LT issuance in H1)**, not with equity. No buyback to speak of; APIC rose on SBC.
3. **M&A is a second, smaller drain:** $39.8B in H1 2026 vs $1.7B in H1 2025 — a step-change in inorganic spend that will add goodwill/intangibles and amortization.
4. **Q2 was the first materially negative FCF quarter** (−$8.8B). If capex holds at ~$54B/quarter and OCF stays ~$45B, FCF stays negative every quarter into 2027. **This is the crux of the debate:** the market must underwrite negative FCF today for AI capacity revenue tomorrow.
5. Cash fell $9.2B in H1 despite the $176B liquidity pool; the mix shifted from cash into AFS securities.

---

## 6. Returns, dilution, and per-share math

| Metric | H1 2026 (annualized) | H1 2025 (annualized) |
|---|---:|---:|
| Reported ROA (NI×2 / avg assets) | ~18.4% | ~8.9% |
| **Core ROA (ex-mark)** | **~8.8%** | ~8.9% |
| Reported ROE (NI×2 / est. equity) | ~33% | ~19% |
| **Core ROE (ex-mark)** | **~16%** | ~17% |
| Diluted share count | ~10,895M | ~10,793M |

- Stockholders' equity is **not directly tagged** in the extract. Deriving it (total assets less current liabilities, debt, and lease liabilities, less an estimated ~$55–65B of other noncurrent/deferred-tax liabilities implied by the $30.5B H1 deferred tax charge) gives **book value of roughly $550–570B, or ~$51–53/share**. Treat this as an **estimate**, not a reported figure.
- **Share count is drifting up ~0.5% per half-year** ($+52M) from SBC dilution. With **$24.8B of unrecognized SBC** still to run through the P&L, expect ~1% annual dilution to persist. No offsetting buyback is visible in this data.
- **Core ROE ~16% and core ROA ~8.8%** are both *flat to modestly down* YoY. That is the honest read: **the marginal dollar of 2026 investment has not yet earned its return** — this is a pure forward-earnings story, and the asset base grew 34% in six months while core earnings grew ~26%.

---

## 7. FX and other observations

- **Foreign-currency translation flipped negative:** −$1,563M in H1 2026 vs +$4,849M in H1 2025 — a reversal worth ~$6.4B of comprehensive income, and a headwind to reported International segment results.
- **FX transaction gains** were +$387M in H1 2026 vs +$68M in H1 2025.
- **Comprehensive income $130,959M vs net income $92,902M** — a $38.1B gap driven by AOCI (AFS bond marks and FX). Reported book value is rising faster than retained earnings, but that component is mark-to-market and reversible.
- **Equity FV-NI gains** of $1,300M in Q2 (vs $393M) suggest the liquid equity portfolio is also contributing.
- **Warrant fair-value adjustments** were a −$1,449M drag in Q2 2026 (vs −$590M), consistent with appreciation of counterparty share prices.
- **Deferred revenue is flat to down** ($26.0B → $24.9B) with $15.2B recognized in H1 — no evidence here of a bookings air-pocket, but also no acceleration on the balance sheet.

---

## 8. Insider transactions

**Not available.** The vendor explicitly reports: *"the B-project data package has no authorized, point-in-time insider-transactions archive for AMZN by 2026-09-24."*

I will not infer, estimate, or fabricate insider activity. For a trader, this means **one input to the mosaic is missing** — do not treat the absence of reported insider selling as a positive signal, and do not treat it as a negative. Substitute Form 4 data from EDGAR directly if this matters to your process.

---

## 9. Risks

**Bear / de-rating risks**
1. **Negative FCF with rising leverage.** FCF −$27.0B in H1, capex annualizing ~$217B, debt +90% in six months, working capital only $8.0B. Any capital-markets tightening or OCF wobble forces a capex deferral — which would hit the AI growth narrative directly.
2. **Earnings quality.** Over half of H1 pre-tax income is a single private-stake mark. A reversal of even 15–20% of the $122.3B carrying value removes ~$2/share in one quarter and could trigger a "growth-at-a-false-multiple" repricing. Reported P/E is not comparable to history.
3. **D&A ramp.** D&A is already 10.2% of revenue (+107 bp YoY). As $173B TTM of capex depreciates on 5–6 year lives, D&A could plausibly approach 12–13% of revenue by 2028 — a ~2–3 pt structural margin headwind that offsets operating leverage.
4. **$650B of contractual obligations**, $121B of it inside 12 months. Rigid cost base; a demand pause converts visibility into operating leverage in reverse.
5. **Interest expense trajectory**: +155% YoY in Q2. At the current debt pace, annualized interest expense could exceed $6B, eating ~$0.45–0.50 of EPS.
6. **Receivables +30% vs revenue +18%**, allowance +17% — early collection/credit signal to monitor.
7. **FX reversal** and International margin exposure.

**Bull risks (upside skew)**
1. Revenue re-accelerated to **+19.6%** on an ~$800B annualized base — rare for a company this size, and *before* the AI capacity comes online.
2. Operating margin **+226 bp YoY** with D&A rising 88 bp — the cleanest margin expansion in years, showing genuine mix shift toward AWS/advertising.
3. **Marketing +2.5%** on 19.6% revenue growth = pricing power and organic demand.
4. Leverage still only **~0.4x net debt/EBITDA** ex-leases; $176B of liquidity; investment-grade access clearly intact given $67B raised in H1.
5. **$650B obligation backlog** is an extraordinary forward revenue signal if you believe the AI demand curve.
6. Core EPS +25% YoY with reported EPS optically very low multiple.

---

## 10. Actionable takeaways

**For a fundamental trader, right now:**

1. **Normalize before you value.** Use **core EPS ~$4.09 for H1 2026** (vs. reported $8.53). Any screen or model keying off the $5.75 Q2 print is understating the multiple by roughly 2.5x. Rebuild estimates on: revenue growth 18–20%, operating margin 13.4–13.7%, interest expense ~$1.3B/quarter, tax rate 23%.
2. **The trade is a capex/FCF story, not an EPS story.** Watch, in order of importance: (a) quarterly capex vs ~$54B Q2 run-rate, (b) OCF growth vs ~44%, (c) LT debt issuance, (d) whether FCF turns less negative. **A capex guidance cut would likely be read as an AI-demand negative even though it's FCF-positive** — expect a negative initial reaction with a positive medium-term re-rating.
3. **Watch the private-stake line every quarter.** `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` (16.2 → 122.3B) and `...UpwardPriceAdjustmentAnnualAmount` (62.8B H1). This line alone can swing EPS by ±$2–4/quarter. Position sizing should account for that volatility regardless of operating performance.
4. **Balance-sheet tripwires to set alerts on:** current ratio below 1.00x (now 1.03x), total debt incl. leases above $275B (now $246B), net cash ex-leases turning negative (now +$26B), AR growth outpacing revenue by >10 pts.
5. **Margin durability check:** confirm D&A as % of revenue (now 10.19%) doesn't exceed ~11.5% while operating margin holds >13%. If both move adversely together, the leverage story is broken.
6. **Insider signal is blank** — do not let anyone tell you otherwise for this dataset. Pull Form 4s independently.
7. **Do not size a position off valuation multiples without a price feed** — I can't produce P/E or EV/EBITDA from this package, and I won't invent one.

**Net assessment:** operating momentum is the strongest it has been in this dataset (revenue +19.6%, margins +226 bp, core EPS +25%), but the company has simultaneously become **capital-hungry, levered, and dependent on non-cash marks for reported earnings**. Fundamentally this is a **high-quality operating story wrapped in a low-quality reported-earnings wrapper, funded by a large, deliberate balance-sheet expansion.** Traders should be long the operating trend and hedged against the earnings-quality and financing tail risks.

---

## 11. Key data summary table

| Category | Metric | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY | TTM |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **Scale** | Revenue (derived, $M) | 200,606 | 167,702 | +19.6% | 382,125 | 323,369 | +18.2% | n/a |
| **Profitability** | Gross margin | 52.3% | 51.8% | +50 bp | 52.0% | 51.2% | +82 bp | n/a |
| | Operating income ($M) | 27,461 | 19,171 | +43.2% | 51,313 | 37,576 | +36.6% | ~96,000e |
| | Operating margin | 13.69% | 11.43% | +226 bp | 13.43% | 11.62% | +181 bp | n/a |
| | Reported net income ($M) | 62,647 | 18,164 | +244.9% | 92,902 | 35,291 | +163.2% | 135,281 |
| | **Core net income ex-marks ($M)** | **23,520** | 18,098 | +30.0% | **44,535** | 35,225 | +26.4% | n/a |
| **Per share** | Diluted EPS — reported | $5.75 | $1.68 | +242% | $8.53 | $3.27 | +161% | n/a |
| | **Diluted EPS — core** | **$2.16** | $1.67 | +29% | **$4.09** | $3.26 | +25% | n/a |
| | Diluted shares | ~10,895M | ~10,811M | +0.8% | ~10,891M | ~10,793M | +0.9% | — |
| **Quality of earnings** | Non-operating income ($M) | 53,396 | 1,686 | n.m. | 69,378 | 4,960 | n.m. | — |
| | of which private-stake mark-up | 50,486 | 49 | n.m. | 62,814 | 86 | n.m. | — |
| | Mark-up as % of pre-tax income | 62.4% | 0.2% | — | 52.0% | 0.2% | — | — |
| | Carrying value of stake ($M) | 122,300 | — | — | 122,300 | — | — | — |
| | Deferred tax expense ($M) | 17,691 | 11 | n.m. | 30,489 | 518 | n.m. | 41,441 |
| | Cash taxes paid ($M) | 2,655 | 4,761 | −44.2% | 3,978 | 5,638 | −29.4% | 6,635 |
| **Cash flow** | Operating cash flow ($M) | 45,387 | 32,515 | +39.6% | 71,419 | 49,530 | +44.2% | 161,403 |
| | Capex ($M) | 54,208 | 32,183 | +68.4% | 98,411 | 57,202 | +72.0% | 173,028 |
| | **Free cash flow ($M)** | **(8,821)** | 332 | n.m. | **(26,992)** | (7,672) | n.m. | **(11,625)** |
| | Acquisitions, net ($M) | 24,359 | 1,700 | n.m. | 39,767 | 1,652 | n.m. | 41,956 |
| | LT debt issued ($M) | 13,557 | 0 | n.m. | 66,998 | 746 | n.m. | 81,925 |
| | Financing cash flow ($M) | 10,146 | (2,539) | n.m. | 62,913 | (2,586) | n.m. | 75,160 |
| **Balance sheet** | Cash + AFS securities ($M) | — | — | — | 176,113 | — | — | — |
| | Total debt incl. fin. leases ($M) | — | — | — | 149,779 | — | — | — |
| | Operating lease liabilities ($M) | — | — | — | 96,320 | — | — | — |
| | Net cash ex-op-leases ($M) | — | — | — | +26,334 | — | — | — |
| | Net debt incl. op leases ($M) | — | — | — | (69,986) | — | — | — |
| | Total assets ($M) | — | — | — | 1,095,689 | — | — | — |
| | Current ratio | — | — | — | 1.03x | — | — | — |
| | Inventory ($M) | — | — | — | 38,184 | — | — | — |
| | Accounts receivable ($M) | — | — | — | 88,092 | — | — | — |
| | Shares outstanding | — | — | — | 10,783M | — | — | — |
| | Book value / share (estimated) | — | — | — | ~$51–53 | — | — | — |
| **Commitments** | Total contractual obligations ($M) | — | — | — | 650,034 | — | — | — |
| | Due within 12 months ($M) | — | — | — | 78,084 | — | — | — |
| | Unrecognized SBC ($M) | — | — | — | 24,800 | — | — | — |
| **Segments** | Reportable operating segments | — | — | — | 3 | — | — | — |
| **Insider** | Insider transactions | **DATA UNAVAILABLE — no archive in vendor package** | | | | | | |
| **Valuation** | Price / market cap / P/E / EV-EBITDA | **NOT AVAILABLE — no price or estimate data in package** | | | | | | |

*Notes: Revenue derived as OperatingIncomeLoss + CostsAndExpenses (reconciles to reported comparatives). Core net income removes the pre-tax upward revaluation of non-marketable equity securities, tax-effected at the reported 23.0% H1 rate. TTM = 2025-07-01 to 2026-06-30. "e" = estimate derived from available tags. Book value/share is an estimate because stockholders' equity is not directly tagged in the extract.*