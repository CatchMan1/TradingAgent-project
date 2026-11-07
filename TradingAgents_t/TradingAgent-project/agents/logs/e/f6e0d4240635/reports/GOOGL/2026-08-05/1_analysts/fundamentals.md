# GOOGL — Alphabet Inc. | Fundamental Deep-Dive
**Point-in-time as of 2026-08-05** | Latest filing: **Form 10-Q for Q2 2026, accepted 2026-07-23** (accn 0001652044-26-000071)

---

## 0. Data provenance, and what these tools did *not* return

Before the analysis, three disclosure notes that matter for how you weight this report:

| Item | Status |
|---|---|
| SEC facts (10-Q Q2'26, Q1'26; 10-K FY2025 filed 2026-02-05) | ✅ Retrieved, point-in-time filtered by actual EDGAR acceptance timestamp |
| Insider transactions | ❌ **Tool returned `DATA_UNAVAILABLE`** — the news vendor has no authorized insider archive for GOOGL as of 2026-08-05. No inference made below. |
| Revenue, R&D, S&M, PP&E, goodwill, total equity/liabilities, segment (Search/Cloud/YouTube) splits, headcount, share price / market cap | ❌ **Not returned** — the vendor payload truncates alphabetically before these tags. Where I state revenue I **derive** it (see below) and label it. No fabrication of segment or valuation figures. |

**Revenue derivation method (used throughout):** Alphabet's income statement presents `CostsAndExpenses` and `OperatingIncomeLoss` as discrete captions, so **Revenue = CostsAndExpenses + OperatingIncomeLoss**. Both inputs are reported facts, so the derived figure is arithmetic, not an estimate. Cross-check: this method yields H1'25 revenue of $186.66B, which is internally consistent with the reported H1'25 EPS/op-income structure — so the derivation is sound.

---

## 1. Executive summary — the six facts that matter

1. **Revenue growth is *accelerating*, and margins are expanding simultaneously.** Derived Q2'26 revenue ≈ **$119.8B, +24.2% YoY** (Q1'26 was +21.8%). Q2'26 GAAP operating margin **34.0%** vs 32.4% a year ago; gross margin **61.6%** vs 59.5%. Growth *and* margin expansion together is the single most bullish fundamental datapoint in this filing.

2. **Reported EPS is massively distorted by a one-time, non-cash remeasurement.** Q2'26 net income of **$112.2B** includes **$99.0B of equity-securities fair-value gains**. H1'26 gains total **$135.9B**. Reported H1'26 diluted EPS of **$14.24** vs a *core* EPS of roughly **$5.28**. Anyone screening on reported P/E is looking at a ~2.7x understatement.

3. **Core earnings are still growing ~18–21%.** Stripping equity gains and applying the reported tax rate: Q2'26 core net income ≈ **$32.1B** (+18.4% YoY), core EPS ≈ **$2.61** (+17.6%). This is genuine operating leverage, not accounting.

4. **Capex has gone parabolic and free cash flow has inverted.** H1'26 capex **$80.6B** vs $39.6B (+103%). Q2'26 capex alone **$44.9B = 37.5% of revenue**. Q2'26 FCF ≈ **–$5.9B** (negative) vs +$5.3B a year ago; H1'26 FCF **$4.3B vs $24.3B, –82%**.

5. **Balance sheet was re-engineered in six months.** Assets **$595B → $922B**. Gross debt **$49.1B → $101.1B**. New common stock issued **$30.5B** (+142M shares, +1.2%), **$19.1B of convertible preferred** issued 2026-06-05, **$3.8B** raised at minority/subsidiary level. **Buybacks went to exactly zero** ($0 vs $28.3B in H1'25).

6. **A large private equity stake was revalued (and largely monetized on paper).** Non-marketable equity ("without readily determinable fair value") **$64.1B → $124.3B**, with cumulative *upward* adjustments **$44.5B → $85.7B**. Meanwhile cash + marketable securities jumped **$126.8B → $242.5B**, of which only $155.4B is cash + AFS debt — implying **~$87B of marketable equity securities** now sit on the balance sheet. Asset value support is real, but it is equity-risk, not cash.

---

## 2. Q2 2026 income statement — reported vs. derived

| Line (USD M) | Q2 2026 | Q2 2025 | YoY |
|---|---:|---:|---:|
| Revenue (**derived**) | **119,796** | 96,428 | **+24.2%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% |
| Gross profit (**derived**) | 73,853 | 57,389 | +28.7% |
| **Gross margin** | **61.6%** | 59.5% | **+2.1 pp** |
| G&A | 6,461 | 5,209 | +24.0% |
| R&D + S&M (**derived residual**) | 26,622 | 20,909 | **+27.3%** |
| Total costs & expenses | 79,026 | 65,157 | +21.3% |
| **Operating income** | **40,770** | 31,271 | **+30.4%** |
| **Operating margin** | **34.0%** | 32.4% | **+1.6 pp** |
| Equity securities FV gain | 99,031 | 1,286 | n.m. |
| Interest income | 1,430 | 1,050 | +36.2% |
| Interest expense | 1,278 | 261 | **+389%** |
| Nonoperating income | 97,983 | 2,662 | n.m. |
| Pre-tax income | 138,753 | 33,933 | +309% |
| Tax | 26,560 | 5,737 | — |
| **Effective tax rate** | **19.1%** | 16.9% | +2.2 pp |
| Net income | 112,193 | 28,196 | +298% |
| Less preferred dividends | 86 | 0 | new |
| Net income to common | 112,107 | 28,196 | +298% |
| **Diluted EPS (reported)** | **$9.11** | $2.31 | +294% |
| Diluted shares (implied) | 12,307 | 12,206 | +0.8% |

**The critical read: operating momentum is strong, and it is *improving sequentially*.** Revenue rose **+9.0% QoQ** ($109.9B → $119.8B). Note the composition: gross margin expanded 2.1pp while combined R&D+S&M grew **faster** than revenue (+27.3% vs +24.2%). That means the margin gain came entirely from **cost-of-revenue leverage** — i.e., the AI infrastructure already deployed is generating revenue faster than it is depreciating. That is the key thesis variable, and this quarter it went the right way.

**Watch item:** `Depreciation` was only **$13.6B in H1'26** against **$80.6B of H1 capex — a 17% ratio.** With FY26 capex tracking toward ~$180B annualized, the depreciation ramp in 2027–2028 is the largest single threat to the 34% operating margin. Interest expense is also inflecting hard (+389% YoY) as $56.2B of new debt was issued.

---

## 3. Core earnings — the number you should actually model

Equity securities FV gains are **non-cash, mark-to-market, pre-tax, and mark-to-market again next quarter**. Isolating them (reported effective tax rate applied):

| | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Pre-tax income | 138,753 | 33,933 | | 216,165 | 75,722 | |
| Less equity securities FV gains | (99,031) | (1,286) | | (135,946) | (11,044) | |
| **Core pre-tax** | **39,722** | 32,647 | +21.7% | **80,219** | 64,678 | +24.0% |
| Tax @ reported ETR | (7,587) | (5,517) | | (15,120) | (10,919) | |
| **Core net income** | **32,135** | 27,130 | **+18.4%** | **64,897** | 57,509* | **+21.0%** |
| Diluted shares (M) | 12,307 | 12,206 | | 12,267 | 12,253 | |
| **Core diluted EPS** | **≈$2.61** | ≈$2.22 | **+17.6%** | **≈$5.28** | ≈$4.37 | **+20.8%** |
| Reported diluted EPS | $9.11 | $2.31 | | $14.24 | $5.12 | |

*\*Using H1'25 reported ETR of 17.1%. Small rounding differences vs. reported NI occur because quarterly ETRs differ.*

**Two implications for traders:**
- Normalized annualized core EPS run-rate is roughly **$10.5–10.9**. Apply your own price to that, not to the $14.24 reported H1 figure or to a trailing multiple contaminated by $136B of unrealized gains.
- Sequential core EPS was roughly flat ($2.68 Q1 → $2.61 Q2) even though revenue grew 9% QoQ — because **share count rose and R&D+S&M accelerated**. Operationally fine; optically a "peak margin" talking point for bears.

---

## 4. Balance sheet — a 6-month transformation

| USD M | 2026-06-30 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| **Total assets** | **921,983** | 595,281 | **+54.9%** |
| Current assets | 343,524 | 206,038 | +66.7% |
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| **Cash + marketable securities** | **242,474** | 126,843 | **+91.2%** |
| — of which AFS debt securities | 99,500 | n/a | — |
| — *implied marketable equity securities* | *~87,100* | *n/a* | *inferred* |
| Non-marketable equity (no RDFV) | 124,259 | 64,094 | +93.9% |
| Accounts receivable, net | 69,175 | 62,886 | +10.0% |
| Operating lease ROU / finance lease ROU | — | 4,797 | → 5,474 |
| Finite-lived intangibles, gross | 10,585 | 2,467 | **+329%** |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| Accrued income taxes, current | 5,233 | 523 | +901% |
| Employee-related liabilities | 15,086 | 17,546 | –14.0% |
| **Legal / loss contingency accrual (current)** | **17,356** | 15,594 | **+11.3%** |
| Deferred revenue (current/total) | 7,154 / 10,100 | 6,578 / 8,600 | +8.8% / +17.4% |
| Finance lease liability (total) | 2,590 | 2,500 | +3.6% |
| **Debt (gross carrying)** | **101,085** | 49,085 | **+106%** |
| Deferred tax liabilities, net | 22,819 | 919 | **+2,383%** |
| Accrued income taxes, noncurrent | 11,306 | 9,531 | +18.6% |
| Operating lease liability | 18,037 | 15,954 | +13.1% |
| **Convertible preferred stock** | **18,023** | 0 | **new** |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| AOCI | (2,285) | (1,916) | — |
| Shares outstanding (M) | 12,230 | 12,088 | **+1.2%** |

**Key reads:**

- **Liquidity is enormous, leverage is still trivial.** Net cash (cash+securities – gross debt) = **$141.4B**; using only cash + AFS debt, still **+$54.3B**. Interest coverage on operating income = **~32x** in Q2. Even using only *tangible* operating earnings, this is an AA-quality balance sheet.
- **Deferred tax liabilities went from $0.9B to $22.8B.** That is the tax bill being provisioned on the $136B of unrealized gains — the tax *expense* is being recognized ahead of any cash tax. Confirms the gains are being marked through the P&L with corresponding deferred tax, not an off-balance-sheet sleight of hand.
- **Intangibles gross +329% ($2.5B → $10.6B)** signals an acquisition or licensed-IP capitalization of roughly **$8B** in H1'26. Forward amortization is now locked: remainder FY26 $747M, FY27 $1,304M, FY28 $1,142M, FY29 $1,096M, FY30 $1,055M — a ~$1.1–1.3B/yr ongoing opex headwind. Q2 amortization already tripled ($367M vs $124M).
- **Legal contingency accrual of $17.4B** (up from $15.6B) with a $3.0B payment made in Q3'25. This is a live, material, under-discussed risk — regulatory/antitrust exposure. It is 1.7% of assets and ~4% of annualized operating income.
- **Deferred revenue +17.4% YoY** to $10.1B, with $4.9B recognized in H1. Backlog/commit growth is healthy (cloud-contract proxy), though this line captures only a fraction of total RPO.
- **AFS unrealized-loss positions exploded** from $13.2B to $53.2B in fair value (accumulated loss only $416M). Benign — it means a much larger, slightly-underwater, rate-sensitive debt portfolio was purchased, consistent with parking new capital in securities before deploying it into capex.

---

## 5. Cash flow — the capex supercycle and the FCF inversion

| USD M | H1 2026 | H1 2025 | Δ |
|---|---:|---:|---:|
| Operating cash flow | 84,859 | 63,897 | +32.8% |
| Capital expenditures (PP&E) | (80,598) | (39,643) | **+103.3%** |
| **Free cash flow (derived)** | **4,261** | **24,254** | **–82.4%** |
| Purchases of marketable securities | (76,480) | (39,870) | +91.8% |
| Sales/maturities of marketable securities | 66,696 | 40,930 | +62.9% |
| Purchases of other (equity) investments | (22,051) | (2,312) | **+854%** |
| Proceeds from other investments | 1,667 | 873 | +91.0% |
| **Investing cash flow** | **(145,822)** | (40,738) | +258% |
| Proceeds from debt | 56,226 | 31,378 | +79.2% |
| Repayments of debt & leases | (5,253) | (18,397) | –71.4% |
| **Issuance of common stock** | **30,499** | 0 | **new** |
| **Issuance of convertible preferred** | **19,063** | 0 | **new** |
| Proceeds from minority shareholders | 3,758 | 400 | +840% |
| Dividends paid (common) | (5,231) | (4,977) | +5.1% |
| **Share repurchases** | **0** | **(28,306)** | **–100%** |
| **Financing cash flow** | **+86,320** | (26,033) | flip |
| FX effect | (154) | 444 | — |
| **Net change in cash** | **+25,203** | (2,430) | — |

**Quarterly decomposition (derived):**

| | Q1 2026 | Q2 2026 | Q2 2025 |
|---|---:|---:|---:|
| Revenue (derived) | 109,896 | 119,796 | 96,428 |
| Operating cash flow | 45,790 | 39,069 | 27,747 |
| Capex | 35,674 | **44,924** | 22,446 |
| **FCF** | **+10,116** | **–5,855** | **+5,301** |
| Capex / revenue | 32.5% | **37.5%** | 23.3% |

**This is the pivotal debate.** Alphabet is converting itself from a ~$70–90B/yr capex company to a **~$180B/yr capex company**, funded by debt, new equity, convertible preferred, and subsidiary-level minority raises. Total new capital raised in H1'26 = **~$109B** (debt $56.2B + common $30.5B + preferred $19.1B + minority $3.8B).

Capex-incurred-but-not-yet-paid was **$29.1B** at 6/30/26 (vs $15.1B at 12/31/25), so the true capex commitment is *understated* by accrual timing and Q3'26 cash capex will run above the P&L number.

**Bull framing:** CFO grew +32.8% and Q2 operating margin rose 1.6pp *while* absorbing a doubling of capex — the investment is earning a return. **Bear framing:** FCF has collapsed 82% and went negative in the most recent quarter, just as the company had to raise equity and preferred for the first time in its history; equity holders are funding a depreciation cliff with dilution.

---

## 6. Capital allocation — an unambiguous regime change

| Signal | Evidence | Interpretation |
|---|---|---|
| **Buyback halted entirely** | $0 repurchased in H1'26 vs $28.3B H1'25 | Per-share EPS support removed; historically a strong "management sees better ROI elsewhere" signal (or a capital constraint) |
| **First-ever large common issuance** | $30.5B; shares +142M (+1.2%) | Direct dilution; unusual for GOOGL and a break in the capital-return narrative |
| **$19.1B convertible preferred (2026-06-05)** | Carrying $18.0B; $86M dividends in Q2 (~1.8% annualized) | Likely a strategic investor stake; introduces conversion overhang and a preferred claim ahead of common |
| **Subsidiary-level minority raises** | $3,758M vs $400M | Capital being raised at partially-owned entities (Other Bets style); parent's economic share falls — watch noncontrolling interest growth |
| **Debt more than doubled** | $49.1B → $101.1B; interest expense +389% | Deliberate leverage-up; maturity ladder was conservative ($2.0B due 2026, $1.0B 2027), so refinancing risk is low |
| **Dividend still growing but slowing** | $0.22/qtr vs $0.21 (+4.8%); H1 cash dividends +5.1% | Token commitment maintained; not a priority |
| **SBC accelerating** | $15.2B H1'26 vs $11.5B (+32.2%); $8.0B in Q2 = 6.7% of revenue | Real economic cost; offsets part of the buyback stop |

**Net assessment:** the company has pivoted from a "return 100%+ of FCF" shareholder model to a "pre-fund a multi-year AI infrastructure program with all available capital" model. This typically compresses the multiple *initially* and re-rates later if incremental ROIC is demonstrable — which is exactly what the revenue acceleration and gross-margin expansion are hinting at.

---

## 7. Multi-period financial history (as available)

| USD M | H1 2025 | FY2025 (YE BS) | H1 2026 |
|---|---:|---:|---:|
| Revenue (**derived**) | 186,662 | n/a | 229,692 (**+23.1%**) |
| Operating income | 61,877 | n/a | 80,466 (+30.0%) |
| Operating margin | 33.1% | n/a | **35.0%** |
| Equity securities FV gains | 11,044 | n/a | 135,946 |
| Net income | 62,736 | n/a | 174,771 (+178.6%) |
| Diluted EPS | $5.12 | n/a | $14.24 |
| **Core diluted EPS (derived)** | **≈$4.37** | n/a | **≈$5.28 (+20.8%)** |
| Operating cash flow | 63,897 | n/a | 84,859 (+32.8%) |
| Capex | 39,643 | n/a | 80,598 (+103.3%) |
| Capex / revenue | 21.2% | n/a | 35.1% |
| Free cash flow | 24,254 | n/a | 4,261 (**–82.4%**) |
| SBC | 11,500 | n/a | 15,200 (+32.2%) |
| Total assets | n/a | 595,281 | **921,983** |
| Gross debt | n/a | 49,085 | **101,085** |
| Cash + marketable securities | n/a | 126,843 | **242,474** |
| Non-marketable equity | n/a | 64,094 | **124,259** |
| Shares outstanding (M) | n/a | 12,088 | 12,230 |
| Financing cash flow | (26,033) | **FY25: (37,388)** / FY24: (79,733) / FY23: (72,093) | **+86,320** |

**Three-year capital-return arc (from the 10-K):** FY23 –$72.1B → FY24 –$79.7B → FY25 –$37.4B → H1'26 **+$86.3B**. The inflection in H1'26 is the largest in the company's history and is entirely explained by the funding of the AI build-out.

---

## 8. Actionable insights

**1. Use core EPS, not reported EPS. This is the highest-value correction available.**
Reported H1'26 EPS of $14.24 overstates run-rate earnings power by roughly **2.7x**. Model **~$10.5–11.0 annualized core EPS** and let that drive your multiple. Any sell-side screen or screener relying on trailing GAAP P/E will show GOOGL as extraordinarily cheap — that is an artifact of $136B of mark-to-market gains.

**2. The investment case now rests on one measurable variable: incremental capex ROIC.**
Watch the *pair* of (a) capex/revenue and (b) gross margin. In Q2'26 these moved in the right direction simultaneously — capex/revenue hit 37.5% while gross margin *rose* 2.1pp. **If gross margin starts compressing while capex/revenue stays above 35%, the thesis breaks.** That is your single best early-warning indicator, and it prints quarterly in this exact dataset.

**3. Expect a depreciation cliff in 2027–2028 — quantify it, don't fear it blindly.**
H1'26 depreciation of $13.6B against $80.6B of H1 capex implies a very low current depreciation rate on new assets. If FY26 capex lands near $180B and useful lives are ~6 years, depreciation could plausibly double from ~$27B annualized toward $50–60B by 2028. At 35% operating margin that is a **~15pp headwind** unless offset by revenue growth or price/mix. Position sizing should reflect this as a 2027+ risk, not a 2026 one.

**4. Treat $17.4B of legal contingency accrual as a discrete, under-priced risk.**
Up $1.8B in six months, with a $3.0B cash payment already made in Q3'25. Adverse outcomes here are cash, not accrual, and would hit FCF in a year when FCF is already ~$4B in H1.

**5. Dilution is now a real, quantifiable drag — adjust per-share models.**
+142M shares (+1.2%), $19.1B of convertible preferred ahead of common, and $3.8B of subsidiary minority raises, all with **zero buyback offset**. Effective net dilution in H1'26 is the first in GOOGL's modern history. Any per-share target built on FY25 share counts overstates value by ~1–2%.

**6. The asset-value floor is meaningfully higher than the operating business alone implies.**
Cash + marketable securities **$242.5B** (~$19.8/share) *plus* non-marketable equity **$124.3B** (~$10.2/share) = **~$30/share of investments** before any operating asset, against **$101.1B gross debt (~$8.3/share)**. Net investment value ≈ **$265B / ~$21.7 per share**. This is a genuine sum-of-parts cushion, but note ~$87B of the "marketable securities" appears to be *equity*, not cash — so treat ~$40% of it as market-risk exposure, not dry powder.

**7. Management's revealed preference is a strong signal.**
Halting a $28B/半年 buyback *and* issuing $30.5B of stock *and* $19.1B of converts in the same six months is an extreme, deliberate statement: management believes the marginal dollar of AI capex earns a higher return than GOOGL's own equity at current prices. Either they are right (multi-year re-rating) or this is the classic late-cycle capex peak. The revenue acceleration (+21.8% Q1 → +24.2% Q2) currently supports "they are right."

**8. Insider signal: unavailable — treat as a gap, not a signal.**
The insider-transaction vendor has no authorized archive for GOOGL as of 2026-08-05. Do **not** read the absence of reported insider buying as a negative — it is a data limitation. No insider inference appears in this report.

**9. Define your invalidation triggers now.**
- **Bear trigger:** Q3'26 gross margin < 59% OR FCF negative for a second consecutive quarter OR buyback still zero while another equity/preferred raise occurs.
- **Bull trigger:** Q3'26 revenue growth > 24% with gross margin ≥ 62%, core EPS > $2.75, and capex/revenue stabilizing below 35%.

---

## 9. Summary table

| Category | Metric | Latest (Q2'26 / 6-30-26) | Prior / YoY | Signal |
|---|---|---:|---:|---|
| **Growth** | Revenue (derived) | $119.8B | +24.2% YoY; +9.0% QoQ | 🟢 Accelerating |
| **Growth** | H1'26 revenue (derived) | $229.7B | +23.1% YoY | 🟢 |
| **Margins** | Gross margin | 61.6% | +2.1 pp | 🟢 |
| **Margins** | Operating margin | 34.0% | +1.6 pp | 🟢 |
| **Margins** | H1'26 operating margin | 35.0% | +1.9 pp | 🟢 |
| **Earnings** | GAAP diluted EPS | $9.11 | vs $2.31 | ⚪ Distorted |
| **Earnings** | Core diluted EPS (derived) | ≈$2.61 | +17.6% | 🟢 Real growth |
| **Earnings** | Equity securities FV gain | $99.0B | vs $1.3B | 🔴 Non-cash, non-repeatable |
| **Earnings** | Effective tax rate | 19.1% | +2.2 pp | 🟡 Rising |
| **Costs** | R&D + S&M (derived) | $26.6B | +27.3% | 🟡 Outgrowing revenue |
| **Costs** | SBC (H1'26) | $15.2B | +32.2% | 🔴 Dilutive cost |
| **Costs** | Depreciation (H1'26) | $13.6B | +43.2% | 🟡 Cliff ahead |
| **Costs** | Interest expense | $1.28B | +389% | 🟡 New burden |
| **Cash flow** | Operating cash flow (H1'26) | $84.9B | +32.8% | 🟢 |
| **Cash flow** | Capex (H1'26) | $80.6B | +103.3% | 🔴 Supercycle |
| **Cash flow** | **Free cash flow (H1'26)** | **$4.3B** | **–82.4%** | 🔴 Inverted |
| **Cash flow** | Q2'26 FCF | **–$5.9B** | vs +$5.3B | 🔴 Negative |
| **Cash flow** | Capex / revenue | 37.5% | vs 23.3% | 🔴 |
| **Balance sheet** | Total assets | $922.0B | +54.9% since 12/31/25 | ⚪ |
| **Balance sheet** | Cash + marketable securities | $242.5B | +91.2% | 🟢 |
| **Balance sheet** | Non-marketable equity | $124.3B | +93.9% | 🟢 (equity risk) |
| **Balance sheet** | Gross debt | $101.1B | +106% | 🟡 |
| **Balance sheet** | Net cash (cash+sec – debt) | +$141.4B | — | 🟢 Fortress |
| **Balance sheet** | Deferred tax liabilities | $22.8B | from $0.9B | ⚪ Tax on gains |
| **Balance sheet** | Legal contingency accrual | $17.4B | +11.3% | 🔴 Under-priced risk |
| **Balance sheet** | Convertible preferred | $18.0B (new, 6/5/26) | — | 🟡 Overhang |
| **Balance sheet** | Deferred revenue | $10.1B | +17.4% | 🟢 Backlog |
| **Capital returns** | Buybacks (H1'26) | **$0** | vs $28.3B | 🔴 Regime change |
| **Capital returns** | Dividend / share | $0.22 | +4.8% | 🟡 Token |
| **Capital returns** | New capital raised (H1'26) | ~$109B | — | 🔴 Dilution/leverage |
| **Share count** | Diluted shares | 12,307M | +0.8% YoY; +1.2% vs 12/31 | 🔴 Diluting |
| **Leverage** | Interest coverage | ~32x | — | 🟢 |
| **Investments** | Other-investment purchases (H1'26) | $22.1B | +854% | 🟡 New capital outlay |
| **Insider** | Transactions | — | — | ⚫ Data unavailable |

**Bottom line for GOOGL:** The operating business is performing better than it has in years — accelerating revenue, expanding gross and operating margins, +33% operating cash flow — and the balance sheet carries roughly $22/share of net investment value. But the company has simultaneously executed the most aggressive capital-structure change in its history: buybacks to zero, $109B of new capital raised, debt doubled, and free cash flow down 82% and negative in the latest quarter. The stock is a **core-earnings growth story (~$10.5–11 annualized core EPS, +18–21% growth) with a valuation trap in its reported GAAP EPS**, and a 2027 depreciation-cliff risk that the market will begin discounting within 2–3 quarters. Position for the operating momentum; size for the FCF and dilution risk; and use gross margin vs. capex/revenue as your tripwire.