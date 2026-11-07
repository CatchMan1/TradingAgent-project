# GOOGL — Alphabet Inc.: Comprehensive Fundamental Research Report
**As of 2026-07-27 | Primary source: SEC filings public through 2026-07-23 (latest 10-Q, accn 0001652044-26-000071) and FY2025 10-K (accn 0001652044-26-000018)**

---

## 0. Data provenance & caveats (read first)

- All figures are **point-in-time SEC XBRL facts** filed by Alphabet and accepted by EDGAR on or before 2026-07-27. The latest 10-Q was accepted **2026-07-23 01:15 UTC** — i.e., **four days before this report**, so this is a genuinely fresh reporting cycle.
- The vendor extract is a **partial tag list** (alphabetically truncated after ~"F" plus selected items). Consequently:
  - **Revenue is not directly tagged in the extract.** I derive it from the identity `Revenues = CostsAndExpenses + OperatingIncomeLoss`, which is the standard Alphabet income-statement structure. Derived revenue reconciles perfectly with the reported operating income, cost of revenue, tax, net income and diluted EPS for every period, which gives high confidence in the derivation.
  - **Not available in the extract:** PP&E, goodwill, retained earnings, total stockholders' equity, R&D expense, sales & marketing expense, share repurchase dollar amounts beyond cash-flow lines, segment detail. I flag where these gaps limit conclusions.
- **Insider transactions: DATA UNAVAILABLE.** The vendor has no authorized point-in-time insider-transactions archive for GOOGL as of 2026-07-27. I will not infer or fabricate insider activity. This is a genuine blank spot in this report and should be filled from Form 4 data before acting on any thesis.

---

## 1. Company profile

**Alphabet Inc. (GOOGL)** — the parent of Google. Core businesses: Google Search & other, YouTube ads, Google Network, Google Cloud (infrastructure + Workspace + AI platform), Google subscriptions/platforms/devices, and Other Bets (long-horizon ventures), plus an increasingly material **investment portfolio** (marketable equity securities and non-marketable/private equity stakes) run out of corporate.

What the filings make clear for the current period: Alphabet in 2026 is no longer a "net-cash-fortress, buyback-machine" story. It is in a **capital-intensive AI build-out phase funded with a historic mix of debt, common equity and convertible preferred**, while carrying a very large, rapidly appreciating private-investment book that has become the single largest swing factor in reported earnings.

Share class outstanding: **12,230M shares (Class A/B/C combined) at 2026-06-30**, up from 12,088M at 2025-12-31. Authorized: 300,000M shares; par $0.001.

---

## 2. Headline income statement — Q2 FY2026 and H1 FY2026

Alphabet's Q2 2026 (Apr–Jun 2026) and first half, versus prior year (USD millions, derived revenue):

| Metric | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---|---|---|---|---|---|
| Revenue (derived) | **119,796** | 96,428 | **+24.2%** | **229,692** | 186,662 | **+23.1%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| Gross profit | **73,853** | 57,389 | +28.7% | 142,478 | 111,262 | +28.1% |
| Gross margin | **61.6%** | 59.5% | +2.1 pt | **62.0%** | 59.6% | +2.4 pt |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 149,226 | 124,785 | +19.6% |
| Opex excl. cost of revenue | 33,083 | 26,118 | +26.7% | 62,012 | 49,385 | +25.6% |
| **Operating income** | **40,770** | 31,271 | **+30.4%** | **80,466** | 61,877 | **+30.1%** |
| Operating margin | **34.0%** | 32.4% | +1.6 pt | **35.0%** | 33.2% | +1.8 pt |
| Non-operating income | **97,983** | 2,662 | n.m. | **135,699** | 13,845 | n.m. |
| *of which: debt & equity securities gains* | *99,031* | *1,286* | *n.m.* | *135,803* | *11,411* | *n.m.* |
| *of which: net interest + FX + other* | *(1,048)* | *1,376* | | *(104)* | *2,434* | |
| Pre-tax income | **138,753** | 33,933 | +309% | **216,165** | 75,722 | +185% |
| Tax expense | 26,560 | 5,737 | +363% | 41,394 | 12,986 | +219% |
| Effective tax rate | **19.1%** | 16.9% | +2.2 pt | **19.1%** | 17.1% | +2.0 pt |
| Net income | **112,193** | 28,196 | +298% | **174,771** | 62,736 | +179% |
| Net income to common (basic) | 112,107 | 28,196 | | 174,685 | 62,736 | |
| **Diluted EPS** | **$9.11** | $2.31 | +294% | **$14.24** | $5.12 | +178% |
| Basic EPS | $9.23 | $2.33 | | $14.41 | $5.16 | |
| Diluted shares (implied) | ~12,306M | ~12,253M | +0.4% | ~12,267M | ~12,253M | |

### The single most important analytical point: earnings quality
Reported EPS is **massively inflated by non-operating, largely non-cash securities remeasurement gains.**

- H1 2026 pre-tax securities gains: **$135,803M** vs. total pre-tax income of $216,165M → **62.8% of pre-tax income is investment mark-up, not operations.**
- In Q2 alone: **$99,031M** of gains vs. $138,753M pre-tax → **71.4%.**
- Stripping gains out (same 19.1% / 16.9% tax rates):

| "Core" (ex-securities gains) | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---|---|---|---|---|---|
| Pre-tax income | 39,722 | 32,647 | +21.7% | 80,362 | 64,311 | +24.9% |
| Est. net income | ~32,135 | ~27,130 | +18.4% | ~65,013 | ~53,314 | +22.0% |
| Est. diluted EPS | **~$2.61** | ~$2.21 | **+18.1%** | **~$5.30** | ~$4.35 | **+21.8%** |

**Actionable read:** the *operating* engine is compounding EPS at **~18–22%**, an excellent but very different number from the **+294% headline Q2 EPS**. Any screen, valuation multiple or "beat/miss" comparison built on GAAP EPS this quarter is misleading. Traders should insist on ex-gains EPS ($2.61 Q2 / $5.30 H1) when assessing the operating trajectory, and should treat GAAP EPS as an *asset-value* event rather than an earnings event.

### Operating momentum: still accelerating
- Revenue growth accelerated sequentially: **Q1 2026 +21.8% YoY ($109,896M) → Q2 2026 +24.2% YoY**, and **+9.0% QoQ**. Sequential acceleration of this magnitude at ~$120B/quarter is the strongest operating datapoint in the release.
- **Gross margin expanded 2.4 pt to 62.0%** despite depreciation rising **+43%** (H1: $13,586M vs $9,485M) from the AI infrastructure build. Margin expansion *while* absorbing that depreciation implies unit economics on AI compute/Cloud are improving, not deteriorating.
- Opex ex-cost-of-revenue grew **+25.6%**, slightly faster than revenue. Opex intensity: 27.0% of revenue vs 26.5% — mild dilution. Q1 2026 G&A $4,291M, Q2 2026 G&A $6,461M (H1 $10,752M, +22.9% YoY). The Q2 G&A step-up is worth watching; it coincides with a $1,762M rise in the current legal/regulatory accrual (see §7).
- Margin path: Q1 2026 operating margin **36.1%** → Q2 2026 **34.0%**. Still +1.6 pt YoY, but two consecutive quarters of sequential compression means the marginal dollar of revenue is getting more expensive. Watch for this to persist as depreciation scales.

### Tax
Effective rate **19.1%** in both Q1 and Q2 2026, up from 16.9–17.3%. The rate on the mark-to-market gains is real cash tax deferred, not avoided — see the **$22,819M net deferred tax liability** (up from $919M) in §6. A structurally higher tax rate (~19%) should be modeled going forward; that alone is a ~2 pt drag on EPS growth versus 2025.

---

## 3. Cash flow and free cash flow — the story turns here

USD millions.

| | Q1 2026 | Q2 2026 | H1 2026 | H1 2025 | YoY |
|---|---|---|---|---|---|
| Cash from operations | 45,790 | **39,069** | **84,859** | 63,897 | **+32.8%** |
| Capex — PP&E purchases | 35,674 | **44,924** | **80,598** | 39,643 | **+103.3%** |
| **Free cash flow (CFO − capex)** | **+10,116** | **−5,855** | **+4,261** | **+24,254** | **−82.4%** |
| Capex incurred but unpaid (accrual capex) | 24,131 | 4,982 | 29,113 | 10,635 | +173.7% |
| *Cash-basis gross capex incl. accruals* | | | **~109,711** | ~50,278 | +118% |
| Cash from investing | −63,389 | −82,433 | **−145,822** | −40,738 | n.m. |
| Cash from financing | +25,077 | +61,243 | **+86,320** | −26,033 | n.m. |
| D&A proxy (depreciation + intangible amort.) | 6,334 | 7,987 | 14,131 | 9,731 | +45.2% |
| Stock-based comp (expense) | 7,200 | 8,000 | 15,200 | 11,500 | +32.2% |

**Three findings that matter more than the EPS headline:**

1. **Free cash flow went negative in Q2 2026 (−$5,855M)** — the first negative FCF quarter visible in this dataset. H1 FCF collapsed **−82%** to $4.26B on a $229.7B revenue base (FCF margin 1.9%). Capex **more than doubled** to $80.6B cash in six months, and accrued-but-unpaid capex of **$29.1B** means the *economic* H1 spend was closer to **$110B**. Annualizing Q2's $44.9B run-rate implies **~$180B of 2026 capex**. This is the core debate: if revenue growth (+24%) holds, the spend is growth investment; if growth decelerates, the market will re-rate GOOGL from "cash-machine" to "capital-intensive".
2. **Cash from operations growth (+32.8%) actually outpaced operating income growth (+30.1%)** — a positive quality signal, helped by $27,538M of deferred taxes (non-cash) and $15,200M of SBC.
3. **Q2 FCF negative + a $109.6B capital raise is the financing story of the year.** See §5.

**SBC is rising faster than I'd like:** +32.2% to $15.2B in H1, or **6.6% of revenue** (6.2% prior). Combined with a **zero buyback** (§5), per-share dilution is now real: shares +142M (+1.2%) in six months. Prior years used ~$28–60B of annual buybacks to neutralize SBC; that offset is gone.

---

## 4. Balance sheet — a $326.7B six-month expansion

| Balance sheet (USD M) | 2026-06-30 | 2025-12-31 | Change | % |
|---|---|---|---|---|
| Cash & equivalents | 55,911 | 30,708 | +25,203 | +82.1% |
| **Cash + short-term investments** | **242,474** | 126,843 | **+115,631** | +91.2% |
| Available-for-sale debt securities (fair value) | 99,500 | n/a | | |
| Accounts receivable, net | 69,175 | 62,886 | +6,289 | +10.0% |
| Total current assets | 343,524 | 206,038 | +137,486 | +66.7% |
| **Total assets** | **921,983** | **595,281** | **+326,702** | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +8,058 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +17,457 | +31.4% |
| Legal/regulatory accrual (current) | 17,356 | 15,594 | +1,762 | +11.3% |
| Accrued income taxes (current) | 5,233 | 523 | +4,710 | +900% |
| Employee-related liabilities | 15,086 | 17,546 | −2,460 | −14.0% |
| Contract liabilities (current / total) | 7,154 / 10,100 | 6,578 / 8,600 | +8.8% / +17.4% | |
| **Total debt (carrying)** | **101,085** | **49,085** | **+52,000** | **+105.9%** |
| Deferred tax assets, net | 1,448 | 9,113 | −7,665 | −84.1% |
| **Deferred tax liabilities, net** | **22,819** | 919 | **+21,900** | n.m. |
| **Convertible preferred (mezzanine)** | **18,023** | 0 | +18,023 | new |
| Common stock + APIC | 131,371 | 93,126 | +38,245 | +41.1% |
| Accumulated OCI | (2,285) | (1,916) | −369 | |
| Shares outstanding | 12,230M | 12,088M | +142M | +1.2% |
| Operating lease liability | 18,037 | 15,954 | +2,083 | +13.1% |
| Finance lease liability | 2,590 | 2,500 | +90 | +3.6% |

### Where did $326.7B of assets come from?
Itemizing the visible drivers: cash +$25.2B, short-term/AFS investments **+$90.4B**, non-marketable equity securities **+$60.2B** (see §5), AR +$6.3B, gross intangibles **+$8.1B** ($2,467M → $10,585M, implying an acquisition or asset purchase), plus roughly **+$70B of PP&E** implied by $80.6B of cash capex net of $14.1B D&A, plus derivative assets +$1.0B. *(PP&E and goodwill are not in the extract, so this decomposition is inferred, not read.)*

### Liquidity is still overwhelming
Even after levering: **cash + ST investments $242.5B vs. total debt $101.1B + preferred $18.0B = net cash ≈ +$123B.** Interest coverage remains trivially strong (H1 interest expense $1,811M vs operating income $80,466M = **44x**). This is not a credit-stress story — it's a **capital-allocation regime change**.

### Two balance-sheet warning flags
1. **Inventory of unrealized bond losses ballooned:** AFS securities in an unrealized-loss position **$53,239M** (from $13,160M); accumulated unrealized loss **$416M** (from $178M); losses <12 months $49,351M / $266M. Mark-to-market duration/rate risk on the $99.5B bond book has risen sharply — a rate shock now has a visible (if small, ~0.4%) AOCI channel.
2. **Derivative liabilities $1,958M vs. $379M and derivative assets $1,702M vs. $732M** — gross FX/hedging exposure up ~4–5x, consistent with a much larger, more internationally-funded balance sheet. Also $614M of FX cash-flow hedge losses to be reclassified into earnings over the next 12 months (vs. a −$60M benefit at 12/31/25) — a small, near-certain **headwind to reported margins** for the next four quarters.

---

## 5. Capital structure transformation — the most under-appreciated item in the filings

H1 2026 financing cash flows (USD M):

| Source | H1 2026 | H1 2025 |
|---|---|---|
| Proceeds from debt, net of issuance costs | **+56,226** | +31,378 |
| Proceeds from issuance of **common stock** | **+30,499** | 0 |
| Proceeds from issuance of **convertible preferred stock** | **+19,063** (June 5, 2026: $19,000M) | 0 |
| Proceeds from minority shareholders | +3,758 | +400 |
| Dividends paid (ordinary) | −5,231 | −4,977 |
| Dividends paid (preferred) | −86 | 0 |
| Debt/lease repayments | −5,253 | −18,397 |
| **Share repurchases** | **$0** | **−28,306** |
| Other financing | −686 | −400 |
| **Net financing cash flow** | **+86,320** | −26,033 |

**Interpretation and the actionable angle:**

- **Buyback went to zero.** Alphabet repurchased $28.3B in H1 2025 and **$0 in H1 2026**. With SBC running $15.2B/H1 for a full year of ~$31B, share count rose **+1.2%**. The multi-year per-share shrink engine has stopped. Any thesis that relied on "buyback + EPS growth" must be revised: **all EPS growth from here is organic.**
- **Alphabet issued equity for the first time in its modern history — twice.** $30.5B of common stock and $19.0B of **convertible preferred** (issued 2026-06-05, carried at $18,023M). The preferred adds a small $86M/quarter dividend claim *ahead of* common and introduces potential dilution overhang. **Note the share-count arithmetic:** shares rose by 142M while $30,499M was raised → **implied average issuance price ≈ $215/share** if the increase is entirely attributable to the offering (SBC vesting would modestly distort this). Treat $215 as an approximate capital-raise reference price — a level management was willing to sell equity at.
- **Debt roughly doubled** ($49.1B → $101.1B), including the June quarter. FY2025 10-K maturity ladder was conservative ($2.0B due within 12 months; $36.1B beyond year 5). Even doubled, maturities remain well-laddered. But the **$52B single-half increase is the largest in company history** and the interest expense run-rate has already gone from $295M (H1 2025) to $1,811M (H1 2026) — a ~$3.6B annualized drag that will keep building.
- **Where's the money going?** $80.6B cash capex (AI infrastructure), **$22,051M of "other investments" purchases** (vs. $2,312M a year ago — a **9.5x** increase, i.e. private AI/strategic stakes), $76.5B of marketable securities purchases, $8.1B of new intangibles.

**Bottom line for traders:** Alphabet has converted from a self-funding cash generator to a **capital-raising, front-loaded AI investor**. That mechanically compresses FCF, raises the tax rate, adds an interest burden, and halts buybacks — three of the four pillars of the old bull case. The offset is that revenue growth *accelerated* to +24% and gross margins *expanded*, which is the only evidence that would justify the spend. **The stock's sensitivity to Cloud/AI revenue disclosure has therefore increased materially.**

---

## 6. The investment book — $124B of private assets driving $135.8B of "earnings"

| Metric | 2026-06-30 | 2025-12-31 | Change |
|---|---|---|---|
| **Non-marketable equity securities (no readily determinable FV)** | **124,259** | 64,094 | **+60,165 (+93.9%)** |
| Cumulative *upward* price adjustment recognized | **85,732** | 44,485 | **+41,247** |
| Cumulative *downward* price adjustment recognized | 9,115 | 8,820 | +295 |
| Equity securities FV-NI gain, in earnings (H1) | **135,946** | 11,044 (H1 2025) | +1,131% |
| Equity securities FV-NI unrealized gain (H1) | 21,531 | 1,088 | +1,879% |
| Equity securities FV-NI realized gain (H1) | 836 | 435 | +92% |
| Debt & equity securities gain (income statement, H1) | **135,803** | 11,411 | +1,090% |

**What we can say with confidence:**
- The private-equity book nearly **doubled to $124.3B (13.5% of total assets)** through $22.1B of new purchases plus **$41.2B of upward marks** (observable-price remeasurements on private holdings).
- Reported H1 2026 earnings therefore include **$135.8B of securities gains**, of which only $21.5B is disclosed as "unrealized" on marketable securities and $0.8B as realized.

**What I cannot fully reconcile — and neither should you ignore it:** the $135.8B total gain materially exceeds the sum of the disclosed components ($21.5B unrealized + $0.8B realized + $41.2B incremental upward adjustment ≈ $63.5B). Roughly **$72B of the H1 gain is not explained by the visible tags.** Plausible explanations include realized gains on non-marketable securities upon IPO/transfer, a step-up on a stake that became marketable, dilution gains on a portfolio company raising capital, or a gain recognized on an acquisition. **This is the #1 item to verify in the 10-Q MD&A/notes before sizing any position.** The point is not that the gain is fictitious — the $22.8B deferred tax liability and $85.7B cumulative upward adjustment are hard corroborating evidence of real value creation — but that its **sustainability and cash-convertibility are unknown**.

**Trader takeaway:** the market will likely capitalize *operating* earnings and treat the ~$136B of gains as a **net-asset-value add-on, not a multiple-bearing earnings stream**. If those marks reverse (private AI valuations are the most volatile asset class on the planet), the earnings optics cut both ways — a −20% markdown on the $124B book is a ~$25B pre-tax hit, roughly **14% of a single year's operating income**. Expect elevated realized/unrealized volatility in reported EPS for years, and expect sell-side to publish "ex-gains" EPS alongside GAAP.

---

## 7. Other items worth flagging

- **Legal/regulatory accruals still building:** current loss-contingency accrual **$17,356M** (from $15,594M). The FY2025 10-K discloses a **$3,000M payment made in Q3 2025** tied to a loss contingency. Regulated-industry liability is a persistent, growing, un-modeled drag and a candidate explanation for the Q2 G&A step-up (+$2,170M YoY).
- **Revenue visibility improving:** total contract liabilities **$10,100M (+17.4%)**, with $4,900M of H1 revenue recognized from the opening balance — consistent with a growing Cloud backlog. New intangibles of $8,118M gross (accumulated amortization only $1,691M) suggest acquired technology/customer relationships; amortization steps up modestly: $747M remainder of FY26, then $1.30B / $1.14B / $1.10B / $1.06B annually.
- **Working capital quality:** AR +10.0% against revenue +23.1% → **DSO improved to ~52.5 days from ~59.3 days.** Collections are strong; AP +66% and accrued liabilities +31% show suppliers are financing part of the build (a favorable sign, not deterioration).
- **Leases:** operating lease liability $18,037M (+13.1%), total undiscounted operating lease commitments $21,333M, $3,498M due within 12 months — modest, data-center/office related.
- **Share count / dilution:** 12,230M shares; authorized 300,000M (effectively unlimited), so buyback re-authorization, if it returns, will not be capacity-constrained.
- **Dividend:** quarterly declared **$0.22** in Q2 2026 (from $0.21, **+4.8%**); H1 declared $0.43 vs $0.41. Payout remains a token ~$0.1B/quarter versus $112B of quarterly net income — management is signaling growth investment over shareholder return.
- **OCI is clean:** comprehensive income $174,402M vs. net income $174,771M (H1) — essentially no AOCI distortion; AOCI of −$2,285M is de minimis.

---

## 8. Insider transactions

**NOT AVAILABLE.** The vendor's point-in-time archive contains no authorized Form 4 / insider-transaction data for GOOGL as of 2026-07-27. I explicitly decline to infer or fabricate insider activity. Given the extraordinary capital-markets actions in Q2 2026 (a $30.5B common raise, a $19B convertible preferred, and a doubling of debt), **insider filings become unusually informative** — purchases/sales around the ~$215 implied offering price and any 10b5-1 plan changes should be checked directly in EDGAR before trading.

---

## 9. Synthesis: bull case vs. bear case

**Bull (evidence-backed):**
1. Revenue growth **accelerated** to **+24.2% YoY** in Q2; **+9.0% QoQ** on a $120B base.
2. Gross margin **+2.4 pt to 62.0%** *despite* +43% depreciation — AI/infra unit economics are working.
3. Operating income **+30.4% YoY** — operating leverage still positive.
4. CFO **+32.8%** to $84.9B; cash conversion healthy.
5. Net cash still **≈ +$123B**; interest coverage 44x; the capital raise was opportunistic, not distress.
6. Private-investment book **+$60.2B to $124.3B** with $85.7B of cumulative upward marks — genuine, verifiable balance-sheet value creation.
7. "Core" ex-gains EPS growth of **~18–22%** is a strong, sustainable operating story.

**Bear (evidence-backed):**
1. **Q2 FCF negative (−$5.9B)**; H1 FCF −82% to $4.3B; implied FY26 capex ~$180B. The cash machine has stalled.
2. **Headline EPS is 63–71% investment mark-up** — a low-quality, non-repeatable earnings mix, with a ~$72B unexplained component.
3. **Buyback = $0** and share count **+1.2%**; SBC at 6.6% of revenue and +32% YoY. Per-share math is now dilutive.
4. **Debt doubled (+$52B)**; interest expense **6x'd**; effective tax rate **+2 pt** structurally.
5. Sequential operating margin compression (36.1% → 34.0%) and opex growing faster than revenue (27.0% vs 26.5% intensity).
6. **Convertible preferred** adds a senior claim and future dilution.
7. Deferred tax liability of **$22.8B** is a real future cash obligation attached to the investment marks; a valuation reversal would hit earnings without a matching cash benefit.
8. Rising legal accruals ($17.4B) and $614M of FX hedge losses poised to hit the next four quarters.

---

## 10. Actionable recommendations for traders

1. **Rebase every model on "ex-securities-gains" EPS: $2.61 (Q2) / $5.30 (H1).** Discounting GAAP EPS of $9.11 will produce wildly wrong multiples. Model FY2026 core EPS off ~$2.6/quarter growing ~15–20%.
2. **Trade the FCF narrative, not the EPS line.** The most likely near-term catalyst is a debate over capex/FCF. Watch: (a) whether Q3 capex again exceeds ~$45B, (b) whether accrued capex ($29.1B) converts to cash outflow, (c) whether FCF stays negative. A second consecutive negative FCF quarter is a plausible de-rating trigger; a reacceleration of Cloud revenue alongside stable capex is the melt-up scenario.
3. **Monitor the buyback restart as a discrete event.** With $242B of cash/ST investments and $0 repurchased, a re-authorization announcement is a clean positive catalyst; continued zero plus rising SBC is a slow per-share headwind.
4. **Verify the ~$72B unexplained investment gain in the 10-Q notes before sizing.** If it's a one-time realization/IPO/step-up → ignore it and value the operating business. If it's a recurring observable-price methodology → the earnings stream becomes structurally more volatile and deserves a lower multiple.
5. **Watch private-AI valuation marks as the swing factor.** $124.3B of Level-3-ish assets = ~13.5% of total assets. Any broad private-AI valuation reset is a direct, immediate EPS hit. Conversely, further upward rounds are a hidden call option.
6. **Position for the "capital-intensive AI utility" re-rating.** The combination of (i) a $215-equivalent equity issuance price, (ii) doubling debt, (iii) zero buyback, and (iv) ~$180B capex run-rate says management sees an investable opportunity far larger than FCF can fund. That is either extraordinary capital allocation or peak-cycle overspend — the answer will be determined by Cloud/AI revenue disclosure over the next 2–4 quarters, not by the Q2 print.
7. **Fill the insider-data gap manually** (EDGAR Form 4s post-June) given the $49.5B of equity issuance in Q2.

---

## 11. Key data summary table

| Category | Metric | Value | Period | Signal |
|---|---|---|---|---|
| **Scale** | Total assets | $921,983M | 2026-06-30 | +54.9% in 6 months |
| | Shares outstanding | 12,230M | 2026-06-30 | +1.2% H1 (no buyback) |
| **Growth** | Revenue (derived) | $119,796M | Q2 2026 | +24.2% YoY, +9.0% QoQ |
| | Revenue | $229,692M | H1 2026 | +23.1% YoY |
| | Operating income | $40,770M | Q2 2026 | +30.4% YoY |
| | Operating income | $80,466M | H1 2026 | +30.1% YoY |
| **Margins** | Gross margin | 61.6% / 62.0% | Q2 / H1 2026 | +2.1 / +2.4 pt YoY |
| | Operating margin | 34.0% / 35.0% | Q2 / H1 2026 | +1.6 / +1.8 pt YoY; Q1 36.1% |
| | Opex ex-CoR / revenue | 27.6% / 27.0% | Q2 / H1 2026 | vs 27.1% / 26.5% — mild dilution |
| **Earnings quality** | GAAP diluted EPS | $9.11 / $14.24 | Q2 / H1 2026 | +294% / +178% YoY |
| | **Ex-gains diluted EPS (est.)** | **$2.61 / $5.30** | Q2 / H1 2026 | **+18.1% / +21.8% YoY** |
| | Securities gains in pre-tax income | $99,031M / $135,803M | Q2 / H1 2026 | 71.4% / 62.8% of pre-tax |
| | Effective tax rate | 19.1% | Q2 & H1 2026 | +2.2 pt YoY |
| **Cash flow** | Cash from operations | $84,859M | H1 2026 | +32.8% YoY |
| | Capex (PP&E, cash) | $80,598M | H1 2026 | +103.3% YoY |
| | **Free cash flow** | **+$4,261M (H1); −$5,855M (Q2)** | 2026 | **−82.4% YoY; Q2 negative** |
| | Accrued capex incurred, unpaid | $29,113M | H1 2026 | +173.7% YoY |
| | Stock-based comp | $15,200M | H1 2026 | +32.2%; 6.6% of revenue |
| **Balance sheet** | Cash + short-term investments | $242,474M | 2026-06-30 | +91.2% H1 |
| | Total debt (carrying) | $101,085M | 2026-06-30 | +105.9% H1 (+$52.0B) |
| | Convertible preferred (mezzanine) | $18,023M | 2026-06-30 | New (issued 2026-06-05) |
| | Net cash position (approx.) | **≈ +$123B** | 2026-06-30 | Still a fortress, but shrinking |
| | Non-marketable equity securities | $124,259M | 2026-06-30 | +93.9% H1 (13.5% of assets) |
| | Cumulative upward price adjustment | $85,732M | 2026-06-30 | +$41,247M in H1 |
| | Net deferred tax liability | $22,819M | 2026-06-30 | from $919M — tax on the marks |
| | Legal/regulatory accrual (current) | $17,356M | 2026-06-30 | +$1,762M H1 |
| | Contract liabilities (total) | $10,100M | 2026-06-30 | +17.4% — backlog proxy |
| **Capital allocation** | Share repurchases | **$0** | H1 2026 | vs −$28,306M H1 2025 |
| | Common stock issued | +$30,499M | H1 2026 | Implied ≈$215/sh if 142M shares |
| | Convertible preferred issued | +$19,063M | H1 2026 | First-ever; senior claim + dilution |
| | Debt issued, net | +$56,226M | H1 2026 | 1.8x prior year |
| | Dividends paid | $5,231M (+$86M pref) | H1 2026 | $0.22/qtr declared, +4.8% YoY |
| **Risks** | AFS securities in loss position | $53,239M (acc. loss $416M) | 2026-06-30 | Rate/duration risk rising |
| | Derivative liabilities | $1,958M | 2026-06-30 | from $379M |
| | FX hedge losses to reclassify (12m) | $614M | 2026-06-30 | Near-term margin headwind |
| | Interest expense | $1,811M | H1 2026 | from $295M (+514%) |
| **Not available** | Insider transactions | **DATA UNAVAILABLE** | — | Must source Form 4s directly |
| | Revenue tag, R&D, S&M, PP&E, goodwill, equity | **Not in vendor extract** | — | Revenue derived; others inferred |

**Verdict:** GOOGL's *operating* business is accelerating (+24% revenue, +30% operating income, expanding gross margin) and remains overwhelmingly solvent (≈+$123B net cash). But H1 2026 marks a **regime change**: free cash flow has been spent to near-zero (negative in Q2), buybacks are off, debt has doubled, preferred stock has been issued, and **~63% of reported pre-tax income is investment mark-up**. The correct posture is to underwrite the operating business at ~$5.30 H1 core EPS growing high-teens-to-20%, treat the $124B investment book as a volatile NAV kicker worth verifying line-by-line, and watch Q3 capex and FCF as the decisive variables.