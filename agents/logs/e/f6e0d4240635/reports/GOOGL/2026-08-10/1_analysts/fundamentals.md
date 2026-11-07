# GOOGL — Alphabet Inc. Fundamental Research Report
**As-of date: 2026-08-10 | Latest filing in dataset: 10-Q for period ended 2026-06-30 (filed/accepted 2026-07-23, accn 0001652044-26-000071)**

---

## 0. Data Notes & Methodology (read first)

- All figures below are **point-in-time SEC XBRL facts** filtered by EDGAR acceptance time ≤ 2026-08-10. The most recent 10-Q (Q2 2026) is the anchor document; the FY2025 10-K (filed 2026-02-05) provides annual context and debt/lease maturity schedules.
- The vendor extract is **alphabetically truncated** (ends around tag "F"/"L"). Consequently the literal `Revenue` and `TotalLiabilities`/`RetainedEarnings` tags are not in the pull. **Revenue is therefore derived arithmetically** and is fully reliable because it ties on two independent lines:
  - `Revenue = CostsAndExpenses + OperatingIncomeLoss`
  - Cross-check: `Revenue − CostOfRevenue − G&A − R&D = OperatingIncomeLoss` (R&D is derived as the residual of `CostsAndExpenses − CostOfRevenue − G&A`).
- **Insider-transactions tool returned DATA_UNAVAILABLE** — no authorized point-in-time insider archive exists for GOOGL at 2026-08-10. **No insider activity is inferred or fabricated.** Similarly, no price/valuation data is available from these tools; all valuation commentary is left qualitative.
- Currency: USD millions unless noted.

---

## 1. Company Profile (as understood from the financial facts)

Alphabet Inc. (GOOGL) is the parent of Google — the dominant global digital-advertising, search, video (YouTube), Android/Chrome platform, cloud infrastructure (Google Cloud), and subscription hardware/services franchise, plus the "Other Bets" portfolio. The **2026 financials reveal a company in the middle of an aggressive, balance-sheet-financed AI infrastructure build-out**, plus a very large and rapidly appreciating private-investment portfolio. Three fingerprints in this dataset define the current profile:

1. **Revenue re-acceleration to ~+24% YoY** with operating leverage (op margin ~34–35%) — the strongest growth/margin combination visible in the comparative periods.
2. **A capital-intensity step-change**: H1 2026 capex of **$80.6bn** vs $39.6bn a year earlier, with a further **$29.1bn of capex incurred but unpaid** at 6/30/26 (vs $10.6bn a year earlier) — the accrual-basis spend rate is even higher than cash capex.
3. **A wholesale re-levering and equity-markup event**: total assets up **55% in six months** ($595.3bn → $922.0bn), debt carrying value roughly **doubled** ($49.1bn → $101.1bn), **$19.1bn of convertible preferred issued in June 2026**, **$30.5bn of common equity issued**, ~**$60bn of upward revaluation** on equity securities without readily determinable fair value, and **buybacks cut to zero**.

---

## 2. Income Statement Analysis

### 2.1 Quarterly bridge (derived)

| USD mn | Q2 2026 | Q2 2025 | YoY | Q1 2026 | QoQ |
|---|---|---|---|---|---|
| Revenue (derived) | **119,796** | 96,428 | **+24.2%** | 109,896 | +9.0% |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 41,271 | +11.3% |
| Gross profit | 73,853 | 57,389 | +28.7% | 68,625 | +7.6% |
| Gross margin | **61.7%** | 59.5% | +220 bps | 62.4% | −70 bps |
| R&D (residual) | ~26,622 | ~20,909 | +27.3% | ~24,638 | +8.1% |
| G&A | 6,461 | 5,209 | +24.0% | 4,291 | **+50.6%** |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 70,200 | +12.6% |
| **Operating income** | **40,770** | 31,271 | **+30.4%** | 39,696 | +2.7% |
| Operating margin | **34.0%** | 32.4% | +160 bps | 36.1% | **−210 bps** |
| Non-operating income | **97,983** | 2,662 | n/m | 37,716 | n/m |
| Pre-tax income | 138,753 | 33,933 | +309% | 77,412 | +79% |
| Tax | 26,560 | 5,737 | +363% | 15,834 | +68% |
| Effective tax rate | 19.1% | 16.9% | +220 bps | 20.5% | −140 bps |
| **Net income** | **112,193** | 28,196 | +298% | 62,578 | +79% |
| Diluted EPS | **$9.11** | $2.31 | +294% | $5.13 | +78% |
| SBC | 8,000 | 6,000 | +33% | 7,200 | +11% |
| SBC / revenue | 6.7% | 6.2% | +50 bps | 6.6% | +10 bps |

### 2.2 First-half comparison (the cleanest YoY read)

| USD mn | H1 2026 | H1 2025 | YoY |
|---|---|---|---|
| Revenue (derived) | **229,692** | 186,662 | **+23.1%** |
| Cost of revenue | 87,214 | 75,400 | +15.7% |
| R&D (residual) | ~51,260 | ~40,637 | +26.1% |
| G&A | 10,752 | 8,748 | +22.9% |
| Operating income | **80,466** | 61,877 | **+30.0%** |
| Operating margin | **35.0%** | 33.1% | +190 bps |
| Non-operating income | **135,699** | 13,845 | +880% |
| Pre-tax income | 216,165 | 75,722 | +185% |
| Tax (19.1% vs 17.1%) | 41,394 | 12,986 | +219% |
| Net income | **174,771** | 62,736 | +179% |
| Diluted EPS | **$14.24** | $5.12 | +178% |
| Diluted shares (implied) | ~12,267 | ~12,253 | +0.1% |

### 2.3 **Critical earnings-quality flag**

**79% of H1 2026 pre-tax income ($135.7bn of $216.2bn) came from non-operating income**, overwhelmingly mark-to-market gains on equity securities: `EquitySecuritiesFvNiGainLoss` = **$135.9bn** in H1 2026 (of which $99.0bn in Q2 alone), versus $11.0bn in H1 2025. These are **unrealized, non-cash, and non-recurring in nature**.

Stripping them out at the statutory rate:

| USD mn | H1 2026 | H1 2025 | YoY |
|---|---|---|---|
| Operating income | 80,466 | 61,877 | +30.0% |
| Tax @ reported ETR | (15,369) | (10,581) | |
| **"Core" net income** | **~65,097** | **~51,296** | **+26.9%** |
| **"Core" diluted EPS** | **~$5.31** | **~$4.19** | **+26.7%** |

**Actionable conclusion:** headline H1 EPS of $14.24 is *not* the earnings base to underwrite GOOGL on. The monetizable operating engine is growing ~27% on a core EPS basis — still exceptional for a company of this size, but roughly half the headline growth rate. Any model that capitalizes the $14.24 will drastically overvalue the franchise.

### 2.4 Cost-structure observations
- **Cost of revenue grew only +15.7% YoY vs revenue +23.1%** → gross margin *expanded* 240 bps to 62.0% in H1. This is a genuinely bullish signal: the AI compute/depreciation burden is being more than offset by mix (Cloud/technical infrastructure) and efficiency.
- **R&D +26.1%** — ahead of revenue growth. Alphabet is re-investing the operating leverage into the AI race.
- **G&A +22.9%**, but with an odd **+50.6% QoQ jump in Q2 ($4,291 → $6,461)**. Given the concurrent rise in `LossContingencyAccrualCarryingValueCurrent` ($15,594 → $17,356) and the accrual tax moves, a meaningful portion of Q2 G&A is plausibly **legal/regulatory charges** rather than run-rate overhead. Q2's 210 bps of sequential operating-margin compression should be attributed partly to this — i.e., it is more likely a one-off than the start of a margin downtrend. **This is a key item to verify in the 10-Q text.**
- **Effective tax rate rose to 19.1% from 17.1%** — a 200 bps headwind. Note the sensitivity: at $229.7bn of H1 revenue, each 100 bps of ETR ≈ $0.8–1.0bn of net income in a half.

---

## 3. Balance Sheet Analysis — the most important section

| USD mn | 2026-06-30 | 2025-12-31 | Change |
|---|---|---|---|
| Cash & equivalents | 55,911 | 30,708 | +82% |
| **Cash + short-term investments** | **242,474** | 126,843 | **+91%** |
| Accounts receivable (net) | 69,175 | 62,886 | +10% |
| Current assets | 343,524 | 206,038 | +67% |
| **Total assets** | **921,983** | 595,281 | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66% |
| Accrued liabilities | 73,014 | 55,557 | +31% |
| Accrued income taxes, current | 5,233 | 523 | +900% |
| Employee-related liabilities | 15,086 | 17,546 | −14% |
| Deferred revenue, current | 7,154 | 6,578 | +9% |
| **Debt carrying amount** | **101,085** | 49,085 | **+106%** |
| Less: unamortized discount/costs | (921) | (542) | |
| Net debt carrying | ~100,164 | ~48,543 | +106% |
| Operating lease liability (total) | 18,037 | 15,954 | +13% |
| Finance lease liability | 2,590 | 2,500 | +4% |
| Deferred tax liabilities, net | **22,819** | 919 | +2,383% |
| Accrued income taxes, noncurrent | 11,306 | 9,531 | +19% |
| **Convertible preferred stock** | **18,023** | 0 | new |
| Common stock + APIC | 131,371 | 93,126 | +41% |
| AOCI | (2,285) | (1,916) | −$369 |
| Shares outstanding (mn) | **12,230** | 12,088 | +1.2% |
| Legal/contingency accrual (current) | 17,356 | 15,594 | +11% |
| Equity securities w/o determinable FV | **124,259** | 64,094 | **+94%** |
| — cumulative upward adjustment | 85,732 | 44,485 | +$41.2bn |
| — cumulative downward adjustment | 9,115 | 8,820 | +$295 |

### 3.1 What actually happened in H1 2026
This balance sheet did not evolve — it was **re-engineered**. In six months Alphabet:

1. **Doubled gross debt** (+$52.0bn) and issued **$19.1bn of convertible preferred** (all on 2026-06-05) — a security type Alphabet has never previously used at scale. The presence of a convertible preferred, plus $3.8bn of minority-interest proceeds, strongly implies **third-party co-investment into an infrastructure/AI entity** (data-center JV structure) rather than plain vanilla corporate funding.
2. **Issued $30.5bn of common equity** — extraordinary for a company that has repurchased ~$60–80bn/yr. This is the first material GOOGL equity issuance since the 2004 IPO era.
3. **Halted buybacks entirely**: `PaymentsForRepurchaseOfCommonStock` = **$0 in H1 2026** vs **$28,306M in H1 2025**. Share count rose from 12,088M to 12,230M.
4. **Marked up its private-AI portfolio by ~$60bn**, lifting non-marketable equity securities to $124.3bn. The $85.7bn cumulative upward revaluation (from $44.5bn at 12/31/25) is the mechanical source of both the $135.9bn P&L gain and a large chunk of the **$22.8bn deferred tax liability** newly on the books. Tax will eventually be owed on these marks — this is a real future cash obligation, not an accounting artifact.

### 3.2 Liquidity & solvency — still fortress, but consumption is rapid
- **Current ratio ≈ 2.7x** ($343.5bn current assets vs ~$125bn estimated current liabilities). Extremely comfortable.
- **Net cash position ≈ +$142bn** ($242.5bn cash+ST investments vs ~$100bn debt) — still net cash, even after the raise. Add $124.3bn of equity investments and the balance sheet remains a strategic asset.
- **But**: `CashCashEquivalentsAndShortTermInvestments` includes marketable securities. The AFS debt portfolio is now **$99.5bn with a $53.2bn unrealized-loss-position** ($416M accumulated loss) — i.e., **roughly half the new bond portfolio was bought above current market**. This is a modest but real interest-rate mark-to-market exposure that did not exist at 12/31/25 (only $13.2bn in loss positions then). At current rate levels it's immaterial to solvency; it is a reminder the cash pile is no longer pristine.
- **Debt maturity ladder (as of 12/31/25, pre-2026 issuance):** FY26 $2.0bn, FY27 $1.0bn, FY28 $2.7bn, FY29 $1.8bn, FY30 $5.5bn, thereafter $36.1bn. `RepaymentsOfDebtAndCapitalLeaseObligations` collapsed to **$5,253M in H1 2026 from $18,397M** — Alphabet has shifted from deleveraging to levering. Interest expense confirms the pivot: **$1,811M in H1 2026 vs $295M in H1 2025 (6.1x)**, with Q2 alone at $1,278M. Interest income of $2.81bn still covers it, but the trend line is now negative for the first time in a decade.

---

## 4. Cash Flow Analysis — the single largest red flag

| USD mn | H1 2026 | H1 2025 | YoY |
|---|---|---|---|
| **Operating cash flow** | **84,859** | 63,897 | **+32.8%** |
| CFO margin (% of revenue) | 36.9% | 34.2% | +270 bps |
| **Capex (PP&E purchases)** | **(80,598)** | (39,643) | **+103.3%** |
| Capex / revenue | **35.1%** | 21.2% | +1,390 bps |
| **Free cash flow (CFO − capex)** | **4,261** | **24,254** | **−82.4%** |
| FCF margin | **1.9%** | 13.0% | −1,110 bps |
| Capex incurred but unpaid (balance) | **29,113** | 10,635 | +174% |
| Depreciation | 13,586 | 9,485 | +43.2% |
| SBC | 15,200 | 11,500 | +32.2% |
| Purchases of marketable securities | (76,480) | (39,870) | +92% |
| Purchases of other investments | (22,051) | (2,312) | +854% |
| **Investing cash flow** | **(145,822)** | (40,738) | +258% |
| Debt issuance (net) | +56,226 | +31,378 | +79% |
| Common stock issued | +30,499 | 0 | new |
| Convertible preferred issued | +19,063 | 0 | new |
| Minority-interest proceeds | +3,758 | +400 | n/m |
| Dividends paid | (5,231) | (4,977) | +5% |
| Buybacks | **0** | (28,306) | −100% |
| Debt/lease repayments | (5,253) | (18,397) | −71% |
| **Financing cash flow** | **+86,320** | (26,033) | n/m |
| FX effect | (154) | +444 | |
| **Net change in cash** | **+25,203** | (2,430) | n/m |

### 4.1 The three numbers that matter
1. **FCF of $4.3bn on $229.7bn of revenue (1.9% margin)** — an 82% YoY collapse in free cash generation despite 23% revenue growth and 33% CFO growth. **Every dollar of incremental CFO is being consumed by capex.**
2. **Capex of $80.6bn in six months** plus **$29.1bn incurred-but-unpaid**. Accrual-basis capex intensity is therefore higher than the cash figure suggests. Annualized, FY2026 capex is tracking toward **$160–180bn+**, versus ~$91bn in 2025 (extrapolating H1 2025's $39.6bn). If H2 capex matches H1, **FY2026 FCF could be near zero or negative for the first time in Alphabet's public history.**
3. **The funding gap was closed with capital markets, not cash flow**: $56.2bn debt + $30.5bn equity + $19.1bn preferred + $3.8bn minority = **~$109.6bn raised in six months**, against $5.2bn of dividends and $5.3bn of debt repaid. Net financing inflow of **+$86.3bn** versus an outflow of $26.0bn a year earlier — a **$112bn swing in financing direction in twelve months.**

### 4.2 Depreciation is the coming P&L wave
`Depreciation` rose **+43.2% YoY** to $13.6bn in H1, far below the +103% capex growth. Since capex is capitalized and depreciated over 4–6 years (server/storage-heavy mix), the **D&A ramp is only ~20% complete**. Expect depreciation to keep compounding at 30–50%/yr into 2027–2028, which mechanically pressures operating margin even if gross margin holds. **The 2026 margin expansion should be treated as the peak of the cycle, not the trend.**

### 4.3 Historical cash-flow trend (from FY2025 10-K)
| USD mn | FY2023 | FY2024 | FY2025 | H1 2026 (ann.) |
|---|---|---|---|---|
| Financing cash flow | (72,093) | (79,733) | (37,388) | +172,600 (annualized) |
| Finance lease principal payments | 705 | 405 | 1,988 | 1,680 |
| Capex incurred but unpaid (YE) | 7,435 | 10,326 | 15,090 | 29,113 (6/30/26) |

The trend is unambiguous: a decade of shareholder returns (−$150bn of buybacks+dividends in FY23–24) has been replaced by a decade-of-capex commitment funded with other people's capital.

---

## 5. Capital Returns & Shareholder Yield

- **Dividend:** $0.22/share declared in Q2 2026 (vs $0.21 Q2 2025); $0.43 for H1 2026 (vs $0.41 H1 2025) — a **~4.9% raise**. Paid $5,231M in H1. Annualized ~$0.87–0.88/share. At a typical GOOGL price this is a **sub-0.5% yield** — not an income story.
- **Buybacks: zero in 2026.** This is the most consequential change for per-share math. Combined with 12,088M → 12,230M shares (+1.2%), **the share count is now expanding for the first time in years**, and the $19.1bn convertible preferred adds contingent future dilution. **The buyback-driven EPS tailwind of 2023–2025 has become a headwind of ~1–2% per year.**
- **Preferred dividends** of $86M paid in H1 2026 (new line item) — a small but permanent senior claim.
- **Net shareholder return in H1 2026 was negative** (~−$5.1bn of dividends+preferred against +$49.6bn of equity/preferred issuance).

---

## 6. Segment / Business-Mix Inference

The dataset does not include segment tags, but several line items allow directional inference:
- **Cloud/technical infrastructure is scaling**: gross-margin expansion to 62% alongside +23% revenue is consistent with Google Cloud's margin ramp plus advertising resilience; a pure ad business would not deliver 240 bps of gross-margin gain while R&D grows 26%.
- **AI capex is being co-funded**: $19.1bn convertible preferred + $3.8bn minority interests + $30.5bn common equity point to **external capital partners inside Alphabet's AI/data-center perimeter**, meaning some of the capex burden (and future upside) is being shared/ceded. Traders should watch for any disclosure of NCI attribution — consolidated revenue growth may overstate the equity-holder capture.
- **Private AI holdings are now a material P&L driver**: $124.3bn of non-marketable equity securities, marked up $60bn in six months. This makes GOOGL's reported earnings **partially a proxy for private-AI valuations**. A private-market markdown would hit reported EPS hard even if Google's operations were unchanged. Conversely the $22.8bn DTL means future cash taxes on the gains.

---

## 7. Risk Register

| Risk | Evidence | Magnitude / Read-through |
|---|---|---|
| **FCF compression** | H1 FCF $4.3bn vs $24.3bn; capex 35% of revenue | Highest-priority risk. Threatens the DCF denominator; any capex guide-up is a direct equity risk |
| **Leverage inflection** | Debt $49.1bn → $101.1bn; interest expense 6.1x YoY; repayments down 71% | Still net cash, but the direction is now a negative catalyst; rating/credit narrative shifts |
| **Dilution / capital-raise dependency** | 0 buybacks, +142M shares, $19.1bn preferred, $30.5bn equity | ~1–2%/yr EPS headwind + overhang; signals capex > internally fundable |
| **Earnings quality** | 79% of H1 pretax from unrealized gains; $22.8bn DTL | Headline EPS ($14.24 H1) not repeatable; comps will be brutal in a flat private-market year |
| **Depreciation wave** | Dep +43% on capex +103% | Margin compression likely in 2027–28; 2026 margin is likely the cycle peak |
| **Margin mix in Q2** | G&A +50.6% QoQ; legal accrual $17.4bn | Verify whether Q2 G&A spike is litigation vs run-rate |
| **Tax rate** | ETR 17.1% → 19.1% | ~$0.8–1.0bn/half headwind at current scale |
| **AFS securities marks** | $53.2bn in unrealized-loss positions vs $13.2bn at YE25 | Minor, but the "cash" is less pristine than headline suggests |
| **D&A/asset-life assumption risk** | Server-heavy capex with 4–6yr lives in a fast-obsolescing AI hardware cycle | Under-depreciation risk → future impairment/step-up |
| **Insider signal** | **Data unavailable** | Cannot confirm or deny management conviction; treat as unknown, not as neutral |

---

## 8. Actionable Conclusions for Traders

**Bull case (supported by the data):**
1. **Revenue growth of +24% YoY with gross-margin expansion and +30% operating-income growth is best-in-class at this scale.** Core (ex-mark) EPS growth of ~+27% is real and cash-generative at the operating line (CFO +32.8%, CFO margin 36.9%).
2. The balance sheet remains a **net-cash fortress (~$142bn)** with $242bn of liquid assets and 2.7x current ratio. Alphabet *can* fund this build.
3. The company accessed **$110bn of capital in six months** with a convertible preferred and a common equity raise — evidence of strong institutional demand and strategic-partner validation of the AI build. Private holdings marked up ~$60bn in half a year.
4. Q2's 210 bps of sequential margin compression is plausibly a **one-off legal/G&A item**, not a structural break — a potential "buy the dip on a noisy quarter" setup.

**Bear case (supported by the data):**
1. **Free cash flow has effectively gone to zero** (1.9% margin, −82% YoY). For a mega-cap whose multiple historically rested on FCF conversion, this is a **regime change, not a blip**, and it is being papered over by $109bn of new capital.
2. **Headline EPS is inflated by unrealized private-market marks** (79% of pretax). The market may be capitalizing an earnings stream that cannot be sustained; the $22.8bn DTL is a claim on future cash.
3. **Buybacks have stopped, shares are growing, and preferred+debt are up** — the per-share compounding machine has been temporarily switched into a capex machine.
4. **Depreciation is only ~20% ramped** relative to capex — the margin headwind is ahead, not behind.

**Concrete positioning guidance:**

| Signal to monitor | Where in the data | Action |
|---|---|---|
| **H2 2026 capex guide / accrual** | `CapitalExpendituresIncurredButNotYetPaid` ($29.1bn — up from $10.6bn) | The single best leading indicator. Continued accrual growth ⇒ FCF stays ~0 ⇒ de-rate risk. Stabilization ⇒ FCF inflection trade |
| **Q3 2026 G&A** | `GeneralAndAdministrativeExpense` ($6,461M in Q2) | If it reverts toward ~$4.3–4.5bn, Q2 margin dip was one-off → constructive. If sticky, margin peak is in |
| **Buyback resumption** | `PaymentsForRepurchaseOfCommonStock` ($0 in 2026) | A restart is the cleanest management signal that the capex cycle is peaking — high-conviction long trigger |
| **Depreciation trajectory** | $13,586M H1; +43% YoY | Watch for step-ups >50% YoY ⇒ margin compression confirmed |
| **Private-mark cadence** | `EquitySecuritiesFvNiGainLoss` ($135.9bn H1) | Any deceleration makes 2027 comps ugly; do not extrapolate Q2's $99bn |
| **Total debt & interest expense** | $101.1bn carrying; $1,811M H1 interest | A second consecutive doubling, or interest expense > interest income, is the leverage red line |
| **Deferred tax liability** | $22,819M | Growing DTL = growing future cash tax on unrealized gains |

**Net assessment:** GOOGL's *operating* business is executing at an elite level — accelerating growth, expanding gross margin, 34–35% operating margins, and 37% CFO margins. But the **financial-engineering layer has inverted**: FCF is gone, buybacks are gone, leverage has doubled, the share count is rising, and reported EPS is ~4–5x "core" earnings because of private-AI markups. Traders should **underwrite GOOGL on core operating income growth (+27–30%) and on the capex trajectory — not on headline EPS or historical FCF multiples.** The most attractive risk/reward is likely on the *confirmation* of a capex plateau (visible first in the accrued-capex line and any buyback restart); the biggest avoidable error is capitalizing H1's $14.24 EPS.

---

## 9. Key Metrics Summary Table

| Category | Metric | Latest (2026-06-30 / H1 2026) | Prior (2025-06-30 / H1 2025) | YoY Change | Interpretation |
|---|---|---|---|---|---|
| **Growth** | Revenue (derived) | $229,692M | $186,662M | **+23.1%** | Re-acceleration; best-in-class at scale |
| | Q2 revenue | $119,796M | $96,428M | +24.2% | Sequential +9.0% QoQ |
| **Profitability** | Operating income | $80,466M | $61,877M | +30.0% | Operating leverage intact |
| | Operating margin | 35.0% | 33.1% | +190 bps | Q2 alone 34.0% (−210 bps QoQ) |
| | Gross margin | 62.0% | 59.6% | +240 bps | Cost of revenue +15.7% < revenue +23.1% ✅ |
| | R&D | ~$51,260M | ~$40,637M | +26.1% | Ahead of revenue — AI reinvestment |
| | G&A | $10,752M | $8,748M | +22.9% | Q2 +50.6% QoQ — possible legal charge |
| **Earnings Quality** | Net income | $174,771M | $62,736M | +179% | ⚠️ 79% from non-operating gains |
| | Non-operating income | $135,699M | $13,845M | +880% | Unrealized equity marks ($135.9bn) |
| | Diluted EPS (reported) | $14.24 | $5.12 | +178% | ⚠️ Not a repeatable base |
| | **"Core" diluted EPS (ex-marks)** | **~$5.31** | **~$4.19** | **+26.7%** | The true operating earnings trend |
| | Effective tax rate | 19.1% | 17.1% | +200 bps | Headwind |
| **Cash Flow** | Operating cash flow | $84,859M | $63,897M | +32.8% | CFO margin 36.9% |
| | Capex | $(80,598)M | $(39,643)M | +103.3% | 35.1% of revenue |
| | **Free cash flow** | **$4,261M** | **$24,254M** | **−82.4%** | 🚩 FCF margin 1.9% |
| | Capex incurred, unpaid | $29,113M | $10,635M | +174% | 🚩 Accrual capex even higher |
| | Depreciation | $13,586M | $9,485M | +43.2% | Ramp only ~20% complete |
| | SBC | $15,200M | $11,500M | +32.2% | 6.6% of revenue |
| **Balance Sheet** | Total assets | $921,983M | $595,281M (12/31/25) | **+54.9%** | Transformation, not drift |
| | Cash + ST investments | $242,474M | $126,843M | +91.2% | Liquidity fortress |
| | Total debt (carrying) | $101,085M | $49,085M | +106.0% | 🚩 Leverage inflection |
| | Net cash position | ~+$142bn | ~+$78bn | +$64bn | Still net cash |
| | Deferred tax liabilities | $22,819M | $919M | +2,383% | Future cash tax on marks |
| | Convertible preferred | $18,023M | $0 | new | Issued 2026-06-05 ($19.0bn) |
| | Equity securities (non-marketable) | $124,259M | $64,094M | +93.9% | $85.7bn cumulative upward reval |
| | Legal/contingency accrual | $17,356M | $15,594M | +11.3% | Regulatory overhang |
| | Shares outstanding | 12,230M | 12,088M | +1.2% | 🚩 Dilution resumed |
| | Current ratio (est.) | ~2.7x | — | — | Very strong |
| **Capital Returns** | Buybacks | **$0** | $(28,306)M | −100% | 🚩 Program halted |
| | Dividends paid | $(5,231)M | $(4,977)M | +5.1% | $0.22/qtr (+4.9%) |
| | Equity issued | $30,499M | $0 | new | First major raise in decades |
| | Minority interest proceeds | $3,758M | $400M | +840% | Co-investment partners |
| | Financing cash flow | **+$86,320M** | $(26,033)M | n/m | $112bn directional swing |
| **Other** | Interest expense | $1,811M | $295M | +514% | Consequence of re-levering |
| | Interest income | $2,811M | $2,051M | +37% | Still covers interest expense |
| **Insider Activity** | Transactions | **DATA UNAVAILABLE** | — | — | No archive at 2026-08-10; not inferred |

---

*Data provenance: SEC XBRL facts via B-project cached SEC archive, filtered by EDGAR `accepted_at` ≤ 2026-08-10. Primary source documents: 10-Q period ended 2026-06-30 (accn 0001652044-26-000071, accepted 2026-07-23 01:15:54 UTC); 10-Q period ended 2026-03-31 (accn 0001652044-26-000048, accepted 2026-04-30); 10-K FY2025 (accn 0001652044-26-000018, accepted 2026-02-05). Revenue, R&D, core earnings, ratios and prior-period quarters marked "derived" are computed from reported XBRL tags as described in Section 0. Insider-transaction data could not be retrieved and no insider activity is asserted.*