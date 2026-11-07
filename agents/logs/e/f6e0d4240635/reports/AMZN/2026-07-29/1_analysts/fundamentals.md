# AMZN — Comprehensive Fundamental Research Report
### Amazon.com, Inc. (NASDAQ: AMZN)
**Data as of:** 2026-07-29 | **Latest public filing in dataset:** Form 10-Q for Q1 2026 (period ended 2026-03-31), accepted 2026-04-30 02:48 UTC | **FY2025 10-K:** accepted 2026-02-06

---

## 1. Dataset scope, limitations & data-integrity notes

Before the analysis, three things traders must know about the evidence base:

| Item | Status |
|---|---|
| Insider transactions | **DATA_UNAVAILABLE** — the vendor archive has no authorized point-in-time insider-transaction record for AMZN by 2026-07-29. **No insider signal can be asserted.** Any claim of insider buying/selling would be fabricated. |
| Q2 2026 results | **Not in dataset.** Latest XBRL facts are Q1 2026 (quarter ended 2026-03-31). AMZN historically reports Q2 in the last week of July — a **live earnings event is likely imminent/underway**. |
| Segment detail | Only the fact that AMZN reports **3 operating segments** (North America, International, AWS) is present. Segment revenue/margin splits are **not** in this dataset, so AWS-vs-retail mix cannot be quantified here. |
| Statement-level detail | The vendor returns the same cached SEC fact set for annual and quarterly requests; several tags are truncated. All figures below are derived **only** from reported XBRL tags, with derivations shown explicitly. |

---

## 2. Company profile (as reflected in the filings)

- **Entity:** Amazon.com, Inc., SEC CIK 0001018724, filer accession series `0001018724-26-0000xx`.
- **Scale:** Q1 2026 revenue **$181.5B** in a single quarter → ~**$726B** annualized run-rate.
- **Structure:** 3 reportable operating segments. Revenue is recognized under ASC 606 (`RevenueFromContractWithCustomerExcludingAssessedTax`).
- **Share count:** 11,269M shares **issued**, **10,754M outstanding** (2026-03-31); **10,757.1M** outstanding as of the 2026-04-22 cover date. ~515M shares held in treasury. Authorized: 100,000M shares.
- **Asset base:** Total assets **$916.6B** (2026-03-31), up from $818.0B at 2025-12-31 (+12.1% in one quarter).
- **Capital intensity:** This is now unambiguously an **AI/data-center infrastructure story** — Q1 2026 capex alone was **$44.2B** (24.4% of revenue).

---

## 3. Q1 2026 income statement (quarter ended 2026-03-31) — the headline quarter

All figures in USD millions unless noted. Derived from XBRL: COGS, CostsAndExpenses, OperatingIncomeLoss, NonoperatingIncomeExpense, IncomeTaxExpenseBenefit, NetIncomeLoss, EPS.

| Line item | Q1 2026 | Q1 2025 | Δ y/y |
|---|---:|---:|---:|
| Revenue | **181,519** | 155,667 | **+16.6%** |
| Cost of goods & services | 87,463 | 76,976 | +13.6% |
| **Gross profit** (derived) | **94,056** | 78,691 | **+19.5%** |
| **Gross margin** (derived) | **51.82%** | 50.55% | **+127 bp** |
| Marketing expense | 10,314 | 9,763 | +5.6% |
| G&A expense | 2,587 | 2,628 | −1.6% |
| Fulfillment + tech/infra (derived residual) | 57,303 | 47,895 | +19.6% |
| Other operating income (expense), net | (447) | (308) | worse |
| **Total costs & expenses** | **157,667** | 137,262 | +14.9% |
| **Operating income** | **23,852** | 18,405 | **+29.6%** |
| **Operating margin** | **13.14%** | 11.82% | **+132 bp** |
| Interest income | 1,135 | 1,066 | +6.5% |
| Interest expense | (800) | (541) | **+47.9%** |
| Other non-operating income | 15,647 | 2,749 | +469% |
| **Non-operating income, net** | **15,982** | 3,274 | +388% |
| Pre-tax income | **39,834** | 21,679 | +83.7% |
| Income tax expense | 9,560 | 4,553 | +110% |
| **Effective tax rate** (derived) | **24.0%** | 21.0% | **+300 bp** |
| Equity-method losses | (19) | +1 | — |
| **Net income** | **30,255** | 17,127 | **+76.7%** |
| **Diluted EPS** | **$2.78** | $1.59 | **+74.8%** |
| Basic EPS | $2.82 | $1.62 | +74.1% |
| Diluted shares (implied) | ~10,883M | ~10,772M | +1.0% |

### ⚠️ Critical quality-of-earnings adjustment — do not take the $2.78 at face value

Buried in "Other non-operating income" of **$15,647M** is a documented non-cash revaluation:

- `EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount` = **$12,328M** in Q1 2026 vs **$37M** in Q1 2025.
- Corroborated by `EquitySecuritiesFvNiGainLoss` of **−$883M** (loss on *marketable* equity) and `MarketableSecuritiesUnrealizedGainLoss` of −$889M.
- The carrying value of non-marketable equity securities jumped **$16,200M → $48,100M** in the quarter.

**Core (ex-revaluation) earnings bridge:**

| Metric | Q1 2026 reported | Less $12,328M pre-tax gain @ 24% tax | Q1 2026 "core" | Q1 2025 | Core Δ y/y |
|---|---:|---:|---:|---:|---:|
| Net income | 30,255 | (9,369) | **20,886** | 17,127 | **+21.9%** |
| Net margin | 16.67% | — | **11.51%** | 11.00% | +51 bp |
| Diluted EPS | $2.78 | ~($0.86) | **~$1.92** | $1.59 | **+20.8%** |

**Insight:** Headline EPS growth of **+75%** collapses to **~+21%** on a core basis. The stock's headline beat is ~31% non-cash mark-to-market on private AI/tech stakes. Still a strong quarter — core EPS +21% on +16.6% revenue with +132 bp operating margin expansion is genuinely good — but traders should not extrapolate $2.78.

---

## 4. Full-year history (FY2023 → FY2025) and trailing-twelve-month

Reported 10-K facts (fiscal year = calendar year):

| Metric ($M) | FY2023 | FY2024 | FY2025 | FY25 y/y | TTM (Apr'25–Mar'26) |
|---|---:|---:|---:|---:|---:|
| Total costs & expenses | 537,933 | 569,366 | **636,949** | +11.9% | n/a |
| Net income (derived for FY25*) | — | — | **77,670** | — | **90,798** |
| Comprehensive income | 31,872 | 62,254 | **105,934** | +70.2% | — |
| Share-based comp | 24,023 | 22,011 | **19,467** | **−11.6%** | — |
| Advertising expense | 20,300 | 21,400 | **23,500** | +9.8% | — |
| Capex (productive assets, cash) | 52,729 | 82,999 | **131,819** | **+58.8%** | **151,003** |
| Operating cash flow | 84,946 | 115,877 | **139,514** | +20.4% | **148,531** |
| **Free cash flow** (OCF − capex) | **32,217** | **32,878** | **7,695** | **−76.6%** | **(2,472)** |
| Financing cash flow | (15,879) | (11,812) | +9,661 | n/m | **+62,475** |
| Investing cash flow | (49,833) | (94,342) | (142,545) | worse | **(176,954)** |

\*FY2025 net income derived as: TTM(Apr'25–Mar'26) 90,798 − Q1'26 30,255 + Q1'25 17,127 = **77,670**. This reconciliation also independently ties out Q1 2026 OCF ($26,032) and capex ($44,203).

### The single most important fundamental trend in this dataset

> **Amazon's free cash flow has gone from $32.9B (FY2024) → $7.7B (FY2025) → NEGATIVE $2.5B (TTM to Q1 2026).**
> Q1 2026 FCF alone was **−$18,171M** vs −$8,004M in Q1 2025.

Capex trajectory: $52.7B → $83.0B → $131.8B → **$151.0B TTM**. Q1 2026 capex of **$44.2B** was **+76.7% y/y** and 24.4% of revenue, implying a **FY2026 cash capex run-rate well above $175B**. Additionally, `CapitalExpendituresIncurredButNotYetPaid` rose to **$27.0B** at FY2025 from $16.8B at FY2024 — meaning **cash capex understates true accrued capex by a widening margin.**

**Trading implication:** AMZN is in the deepest FCF-compression phase of its modern history. Historically the stock has de-rated on FCF-negative headlines even while EPS grows. This is the #1 bear narrative to respect into and after the upcoming Q2 print.

---

## 5. Balance sheet — a decisive shift toward leverage

### Assets (2026-03-31 vs 2025-12-31, $M)

| Item | 2026-03-31 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 101,816 | 86,810 | +15,006 |
| Marketable securities (AFS debt) | 42,200 | 45,800 | −3,600 |
| Accounts receivable, net | 75,532 | 67,729 | +7,803 |
| Inventory, net | 36,534 | 38,325 | −1,791 |
| Prepaid & other current | 7,200 | 6,900 | +300 |
| **Current assets** | **255,155** | 229,083 | **+26,072** |
| Operating lease ROU asset | 88,741 | 86,054 | +2,687 |
| Finance lease ROU asset (net) | 16,000 | 15,200 | +800 |
| Goodwill | 23,449 | 23,273 | +176 |
| **Other non-current assets** | **151,827** | 122,607 | **+29,220** |
| **Total assets** | **916,630** | 818,042 | **+98,588 (+12.1%)** |

Non-marketable equity securities (**$\mathbf{48.1B}** vs $16.2B) reside inside "other non-current assets" and explain most of the +$29.2B build, alongside $15.4B of acquisitions.

### Liabilities & equity ($M)

| Item | 2026-03-31 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| Accounts payable | 124,749 | 121,909 | +2,840 |
| Accrued liabilities | 71,120 | 75,520 | −4,400 |
| **Current liabilities** | **216,756** | 218,005 | −1,249 |
| Long-term debt — current portion | 2,832 | 2,748 | +84 |
| **Long-term debt — non-current** | **119,074** | 65,648 | **+53,426** |
| Operating lease liabilities — non-current | 79,067 | 76,597 | +2,470 |
| Finance lease liabilities — non-current | 11,747 | 10,742 | +1,005 |
| Other non-current liabilities | 48,072 | 35,985 | +12,087 |
| **Total liabilities (derived)** | **~474,716** | ~406,977 | **+67,739** |
| **Total equity (derived)** | **~441,914** | ~411,065 | **+30,849** |

### Debt — the story of the quarter

| Metric ($M) | Q1 2026 | FY2025 | TTM |
|---|---:|---:|---:|
| LT debt issued (cash proceeds) | **53,441** | 15,673 | **68,368** |
| LT debt repaid | 0 | 5,021 | 5,021 |
| Short-term debt issued | 6,018 | 9,320 | 13,523 |
| Short-term debt repaid | 6,109 | 8,426 | 12,453 |
| **Total long-term debt** | **121,906** | 68,836 | — |

- **Net cash position** (cash + AFS securities − total LT debt): **+$22.1B** at 2026-03-31 vs **+$63.8B** at 2025-12-31 — a **$41.7B deterioration in one quarter**. Amazon is actively releveraging to fund AI infrastructure.
- Interest expense +47.9% y/y ($541M → $800M). At ~4.5–5% on the new $53.4B, quarterly interest expense should step up materially toward **$1.2–1.5B** in coming quarters. Still ~30x covered by operating income — not a solvency issue, but an EPS drag.
- **Total fixed/lease obligations:** operating leases **$91.6B** + finance leases **$13.3B** + debt **$121.9B** ≈ **$226.8B**. Weighted-average discount rates rose modestly (operating 3.7% → 3.8%; finance 3.4% → 3.6%).

### Committed obligations — the "hidden" $569B

| Contractual obligations, 2026-03-31 | $M |
|---|---:|
| Remainder of FY2026 | 46,489 |
| Next 12 months (total) | **57,065** |
| Year 2 | 48,945 |
| Year 3 | 40,355 |
| Year 4 | 38,566 |
| **Total contractual obligations** | **569,280** |

**$57.1B due within 12 months** — against $104.7B of cash + restricted cash. This is largely AWS compute/power/chip purchase commitments; it is both the **bull case** (contracted AI demand) and the **bear case** (fixed cost rigidity if AI demand disappoints).

### Liquidity & credit metrics

| Metric | 2026-03-31 | 2025-12-31 |
|---|---:|---:|
| Current ratio | **1.18x** | 1.05x |
| Cash + securities + A/R vs current liabilities | 219,548 / 216,756 = **1.01x** | 200,339 / 218,005 = 0.92x |
| Total debt + leases / total assets (derived) | ~24.7% | ~20.9% |
| ROE (TTM NI / avg equity) | **~21.4%** | — |

---

## 6. Cash flow statement deep dive

| $M | Q1 2026 | Q1 2025 | TTM Apr'25–Mar'26 | FY2025 | FY2024 |
|---|---:|---:|---:|---:|---:|
| Operating cash flow | **26,032** | 17,015 | **148,531** | 139,514 | 115,877 |
| Capex (productive assets) | **(44,203)** | (25,019) | **(151,003)** | (131,819) | (82,999) |
| **Free cash flow** | **(18,171)** | (8,004) | **(2,472)** | 7,695 | 32,878 |
| Purchases of marketable securities | (23,256) | (13,333) | (64,693) | (54,770) | (26,005) |
| Sales/maturities of securities | 17,686 | 7,737 | 54,335 | 44,386 | 16,403 |
| **Business acquisitions, net of cash** | **(15,408)** | (48) | **(19,297)** | n/a | 3,680 |
| Investing cash flow | (64,212) | (29,803) | (176,954) | (142,545) | (94,342) |
| LT debt issuance | 53,441 | 746 | 68,368 | 15,673 | 0 |
| Financing cash flow | **+52,767** | (47) | **+62,475** | +9,661 | (11,812) |
| D&A (non-cash) | **18,945** | 14,262 | **70,439** | — | — |
| SBC (non-cash) | 4,032 | 3,689 | — | 19,467 | 22,011 |
| Cash taxes paid | 1,323 | 877 | 8,741 | — | — |
| Deferred tax expense | **12,798** | 507 | 23,761 | — | — |

### Three critical cash-flow readings

**a) Cash conversion is deteriorating.** OCF/NI: FY2025 **180%**, TTM **164%**, Q1 2026 **86%**. The TTM OCF of $148.5B is now fully consumed by capex.

**b) D&A is the margin time bomb.** Q1 2026 D&A **$18,945M, +32.8% y/y** vs revenue +16.6%. TTM D&A **$70.4B**. As $151B of TTM capex is placed in service, D&A will grow well into the high-teens-to-20%+ range annually. Operating margin expansion of +132 bp in Q1 was achieved *despite* this — impressive, but the gap between D&A growth (33%) and revenue growth (17%) cannot persist indefinitely without margin pressure. **Watch Q3/Q4 2026 D&A as the leading indicator of the AI-capex margin payback debate.**

**c) The $12.8B deferred tax charge.** Q1 2026 deferred tax expense of **$12,798M** vs $507M a year ago (TTM $23,761M) is the book/tax timing consequence of the equity revaluations — non-cash, but it raises the Q1 effective rate to 24.0%. Expect elevated effective tax rates while mark-to-market gains accrue.

---

## 7. Capital allocation & M&A — the under-appreciated Q1 event

| Item | Q1 2026 | TTM | FY2025 | FY2024 |
|---|---:|---:|---:|---:|
| Business acquisitions, net of cash | **15,408** | 19,297 | ~0 | 3,680 |
| Goodwill balance | 23,449 | — | 23,273 | — |

**$15.4B of acquisitions in a single quarter** — the largest M&A outlay in years — yet goodwill increased only **$176M**. Two conclusions:

1. The consideration was largely allocated to **identifiable intangibles and/or equity interests**, not residual goodwill. This is consistent with **strategic minority stakes in AI/silicon companies** rather than outright consolidation.
2. Combined with the **$12.3B upward revaluation** of existing non-marketable stakes, AMZN is now carrying **$48.1B of private-company equity** — a genuinely new, largely invisible, and mark-to-model earnings driver. This creates **earnings volatility risk in both directions**: the same line item that added $9.4B after-tax to Q1 could subtract meaningfully in a risk-off quarter.

Other capital-allocation positives: **SBC falling** ($24.0B → $22.0B → $19.5B annual; $3.69B → $4.03B quarterly, +9.3%) — genuine expense discipline. Unrecognized SBC cost is $14.4B (≈3.6 years of runway at current pace). **Inventory down 4.7% q/q on +16.6% revenue growth** — improving turns and working-capital efficiency. **Cash taxes paid actually fell to $1.3B from $877M... i.e., remain very low relative to $9.6B book tax expense** — a real cash advantage.

---

## 8. Evidence-based bull case vs bear case

### 🟢 Bull case (supported by the filings)
1. **Operating leverage is real and accelerating:** Q1 2026 operating income **+29.6%** on revenue **+16.6%**; operating margin **13.14%** vs 11.82% (+132 bp); gross margin **51.82%** vs 50.55% (+127 bp). Residual "fulfillment + tech/infra" grew 19.6%, slower than the gross-profit dollar growth of 19.5%... i.e. the mix is working.
2. **Core EPS growth ~+21%** with **net margin ex-revaluation at 11.51%** — a genuine record-class Q1 profitability level for Amazon.
3. **SBC discipline:** −11.6% y/y in FY2025 on top of −8.4% in FY2024 — a structural boost to GAAP margins vs history.
4. **Operating cash flow still compounding:** TTM **$148.5B**, +30% vs FY2024's $115.9B.
5. **Contracted demand signal:** $569.3B of contractual obligations, $57.1B due within a year — this is *committed* capacity spend, implying a visibility book for AWS/AI that most mega-caps lack.
6. **Free option on private equity:** $48.1B of non-marketable stakes with demonstrated revaluation upside (+$12.3B in one quarter).
7. Investment grade balance sheet intact: current ratio improved to **1.18x**, interest coverage ~30x.

### 🔴 Bear case (supported by the filings)
1. **FCF is now negative:** −$2.5B TTM; −$18.2B in Q1 2026 alone. FY2025 FCF of $7.7B was **76.6% below** FY2024's $32.9B.
2. **Releveraging at scale:** LT debt nearly **doubled** ($68.8B → $121.9B) in one quarter; net cash position fell from **+$63.8B to +$22.1B**. Interest expense +48% y/y and set to rise further.
3. **Earnings quality:** ~31% of Q1 2026 net income was non-cash private-markup. The Q1 "beat" was largely not operational. Repeatability is low and the line is symmetric.
4. **D&A inflecting:** +33% y/y, TTM $70.4B, against TTM capex of $151.0B not yet fully in service. Depreciation is a **lagged but certain** drag.
5. **Fixed-cost rigidity:** $569.3B committed obligations convert from advantage to liability if AI/cloud demand growth decelerates.
6. **Tax rate normalization:** 24.0% vs 21.0% — a ~300 bp headwind to net income growth relative to prior years.
7. **Forward-quarter visibility is zero in this dataset** and a major binary event (Q2 2026) is imminent.

---

## 9. Actionable takeaways for traders

**1. Reframe the Q1 2026 "beat" before you trade the memory of it.**
Reported diluted EPS $2.78 (+75%) is distorted. Core EPS ≈ **$1.92 (+21%)**. Anyone anchoring on $2.78 as a run-rate base is overstating forward earnings power by roughly **45%**.

**2. The setup into the imminent Q2 2026 print is asymmetric on FCF, not EPS.**
With TTM FCF at **−$2.5B** and FY2026 capex run-rate tracking above **$175B**, the market's reaction function has shifted from "did EPS beat" to "what is the capex guide and when does FCF inflect." A beat on operating income paired with a capex raise has historically been a **sell-the-print** combination. Position sizing should respect that.

**3. Set hard monitoring levels:**
| Metric | Current reading | Trigger to watch |
|---|---|---|
| Operating margin | 13.14% (Q1'26) | Any quarter < 12.0% ⇒ capex cost absorption problem |
| D&A y/y growth | +32.8% | > 30% while revenue growth < 17% ⇒ margin compression imminent |
| Capex / revenue | 24.4% (Q1'26) | > 27% ⇒ FY2026 FCF stays negative; de-rating risk |
| LT debt | $121.9B | New issuance while FCF < 0 ⇒ leverage narrative takes over |
| Contractual obligations | $569.3B | A flat/down total ⇒ AI demand deceleration signal |
| Private equity stake value | $48.1B | A downward revaluation ⇒ EPS miss from non-operating line |

**4. The leverage story is the under-owned risk.** Amazon has added **$68.4B of long-term debt over twelve months** and **$53.4B in a single quarter** — while simultaneously running negative FCF. A current ratio of 1.18x and 30x interest coverage mean no near-term solvency concern, but the *direction of travel* matters: the FY2023–FY2025 story was "cash machine deleveraging," and the Q1 2026 story is "leveraging up to fund AI." Multiple-compression risk is concentrated in that transition being re-rated.

**5. Positive divergence worth owning on weakness:** SBC −11.6% y/y, inventory turns improving, G&A down 1.6% y/y, gross margin at a record 51.8%, and operating income growing ~1.8x faster than revenue. If the capex cycle peaks in 2027, the operating leverage already demonstrated in Q1 2026 implies an **extremely powerful FCF snap-back**. That is the multi-year bull thesis; it is a **2027–2028 story, not a next-quarter story.**

**6. No insider signal available.** Insider transactions are **DATA_UNAVAILABLE** for AMZN in this dataset. Do not treat the absence of insider data as either bullish or bearish — it is simply missing. Any decision must rest on the reported fundamentals above.

**7. Earnings-date risk management:** Given the point-in-time cutoff at the Q1 2026 10-Q (filed 2026-04-30) and today's date of 2026-07-29, **Q2 2026 results are almost certainly being released around now**. This is the highest-variance event in the near term. The dataset provides zero Q2 2026 information, so any Q2 view must be treated as an estimate, not a fact.

---

## 10. Summary table — key points at a glance

| Category | Metric | Value | Δ / Context | Signal |
|---|---|---|---:|---|
| **Latest quarter** | Q1 2026 revenue | $181.5B | +16.6% y/y | 🟢 Strong |
| | Q1 2026 operating income | $23.9B | +29.6% y/y | 🟢 Strong |
| | Q1 2026 operating margin | 13.14% | +132 bp y/y | 🟢 Record-class |
| | Q1 2026 gross margin | 51.82% | +127 bp y/y | 🟢 Record-class |
| | Q1 2026 diluted EPS | $2.78 | +74.8% y/y | 🟡 Distorted |
| | **Q1 2026 core EPS (ex-reval)** | **~$1.92** | **+20.8% y/y** | 🟢 Solid, not spectacular |
| | Q1 2026 net margin (core) | 11.51% | +51 bp y/y | 🟢 |
| **Earnings quality** | Non-marketable equity reval gain | $12.3B pre-tax / ~$9.4B after-tax | vs $37M in Q1'25 | 🔴 31% of net income |
| | Effective tax rate | 24.0% | +300 bp y/y | 🔴 Headwind |
| | Deferred tax expense | $12.8B (Q1) / $23.8B TTM | non-cash | 🟡 |
| **Cash generation** | TTM operating cash flow | $148.5B | +30% vs FY2024 | 🟢 |
| | TTM capex | $151.0B | FY23: $52.7B → FY25: $131.8B | 🔴 2.9x in 2 yrs |
| | **TTM free cash flow** | **−$2.5B** | FY24: +$32.9B | 🔴 **Negative** |
| | FY2025 FCF | $7.7B | −76.6% y/y | 🔴 |
| | Q1 2026 capex / revenue | 24.4% | +77% y/y in dollars | 🔴 |
| | Capex accrued but unpaid | $27.0B (FY25) | vs $16.8B FY24 | 🔴 Understated |
| **Balance sheet** | Total assets | $916.6B | +12.1% q/q | 🟢 |
| | Cash + AFS securities | $144.0B | — | 🟢 |
| | Long-term debt | $121.9B | +$53.4B q/q (from $68.8B) | 🔴 |
| | TTM LT debt issued | $68.4B | vs $15.7B FY2025 | 🔴 |
| | Net cash (cash+sec−debt) | +$22.1B | −$41.7B q/q | 🔴 Releveraging |
| | Total debt + leases | ~$226.8B | — | 🟡 |
| | Current ratio | 1.18x | from 1.05x | 🟢 |
| | Interest expense | $800M (Q1) | +47.9% y/y | 🟡 Watch |
| | Total equity (derived) | ~$441.9B | +$30.8B q/q | 🟢 |
| | ROE (TTM) | ~21.4% | — | 🟢 |
| **Committed spend** | Total contractual obligations | $569.3B | $57.1B due <12mo | 🟡 2-sided |
| **Cost structure** | D&A | $18.9B (Q1) / $70.4B TTM | +32.8% y/y | 🔴 Lagged margin drag |
| | SBC | $19.5B FY2025 | −11.6% y/y | 🟢 Discipline |
| | SBC unrecognized | $14.4B | ~3.6 yr runway | 🟢 |
| | Advertising expense | $23.5B FY2025 | +9.8% y/y | 🟡 |
| | Inventory | $36.5B | −4.7% q/q on +16.6% rev | 🟢 Turns improving |
| | Allowance for doubtful A/R | $2.6B | 3.4% of gross A/R | 🟢 |
| **M&A / investments** | Q1 2026 acquisitions | $15.4B | TTM $19.3B | 🟡 New driver |
| | Private (non-marketable) equity | $48.1B | from $16.2B | 🟡 Volatile marks |
| | Goodwill | $23.4B | +$0.2B only | 🟢 Low impairment risk |
| **Shares** | Diluted shares (implied) | ~10,883M | +1.0% y/y | 🟢 Low dilution |
| | Shares outstanding | 10,754M (10,757.1M @ 4/22) | — | — |
| **Insider activity** | All insider transactions | **DATA UNAVAILABLE** | no archive | ⚪ No signal |
| **Event risk** | Q2 2026 earnings | Not in dataset | due ~late July 2026 | 🔴 Binary |
| **Overall** | **Operating momentum vs. cash-flow/leverage deterioration** | — | — | 🟡 **Constructive on operations, cautious on FCF & leverage into the print** |

---

*Prepared 2026-07-29 strictly from point-in-time SEC XBRL facts for AMZN (10-Q acc. 0001018724-26-000014, filed 2026-04-30; 10-K acc. 0001018724-26-000004, filed 2026-02-06). Derived figures are labeled "(derived)"; all derivations are shown so they can be independently verified. Insider transaction data is unavailable in this dataset and no inference is made. No price or valuation-multiple data was supplied, so P/E, EV/EBITDA or similar multiples cannot be computed from this evidence base.*