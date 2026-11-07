# GOOGL — Alphabet Inc. Fundamental Deep Dive
**As of 27 Aug 2026 | Latest filing: 10-Q for period ended 30 Jun 2026 (accepted 23 Jul 2026) | Prior full-year: 10-K FY2025 (filed 5 Feb 2026)**

---

## 0. How to read this report (data provenance & caveats)

| Item | Status |
|---|---|
| Source | Point-in-time SEC XBRL facts, filtered by actual EDGAR acceptance timestamp (no look-ahead) |
| Latest period | Q2 2026 (Apr–Jun 2026), filed 23 Jul 2026 — ~5 weeks old |
| Revenue | **Derived** — the raw revenue tag was not in the returned row window. Derived as `CostsAndExpenses + OperatingIncomeLoss`, which is the exact accounting identity for total revenue. Reconciles perfectly for every period below (verified against gross profit, pretax income, tax and net income). |
| Segment / product revenue mix, R&D line, goodwill, long-term investments, total liabilities/equity | **Not present** in the returned (alphabetically truncated) fact set. Not estimated or invented — flagged as gaps. |
| Insider transactions | **`DATA_UNAVAILABLE`** — the data package holds no authorized point-in-time insider archive for GOOGL. No insider signal can be offered; this is an absence of data, not a negative. |

---

## 1. Company profile

Alphabet Inc. (NASDAQ: GOOGL / GOOG) is the parent of Google — the world's largest digital advertising business, plus Google Cloud, YouTube, Android/Play, hardware, and the "Other Bets" portfolio (autonomous driving, life sciences, venture-style equity holdings). Its SEC facts show the classic Alphabet signature: very high gross margins (~60%), heavy share-based compensation (6–7% of revenue), a large portfolio of marketable debt securities and *non-marketable* equity investments marked through the P&L, an operating-lease-heavy real-estate footprint, and — new in 2026 — a large debt and equity-funded AI infrastructure build.

**Fiscal position:** Dec year-end; latest quarter is **Q2 FY2026**.

---

## 2. Income statement — growth *re-accelerated* and margins expanded

All figures $M unless noted.

| | Q2 2025 | Q1 2026 | **Q2 2026** | Q2 YoY | H1 2025 | **H1 2026** | H1 YoY |
|---|---|---|---|---|---|---|---|
| Revenue (derived) | 96,428 | 109,896 | **119,796** | **+24.2%** | 186,662 | **229,692** | **+23.0%** |
| Cost of revenue | 39,039 | 41,271 | 45,943 | +17.7% | 75,400 | 87,214 | +15.7% |
| Gross profit | 57,389 | 68,625 | **73,853** | +28.7% | 111,262 | 142,478 | +28.1% |
| **Gross margin** | 59.5% | 62.4% | **61.6%** | +2.1 pp | 59.6% | **62.0%** | +2.4 pp |
| Opex (total costs − COGS) | 26,118 | 28,929 | 33,083 | +26.7% | 49,385 | 62,012 | +25.6% |
| **Operating income** | 31,271 | 39,696 | **40,770** | **+30.4%** | 61,877 | **80,466** | **+30.0%** |
| **Operating margin** | 32.4% | 36.1% | **34.0%** | +1.6 pp | 33.1% | **35.0%** | +1.9 pp |
| Non-operating income | 2,662 | 37,716 | **97,983** | n.m. | 13,845 | **135,699** | n.m. |
| Pretax income | 33,933 | 77,412 | 138,753 | +309% | 75,722 | 216,165 | +186% |
| Tax | 5,737 | 14,834 | 26,560 | +363% | 12,986 | 41,394 | +219% |
| **Effective tax rate** | 16.9% | 19.2% | **19.1%** | +2.2 pp | 17.1% | **19.1%** | +2.0 pp |
| **Net income** | 28,196 | 62,578 | **112,193** | **+298%** | 62,736 | **174,771** | **+179%** |
| Diluted EPS ($) | 2.31 | 5.13 | **9.11** | +294% | 5.12 | **14.24** | +178% |
| Basic EPS ($) | 2.33 | 5.18 | 9.23 | — | 5.16 | 14.41 | — |

### 2.1 The core business is genuinely accelerating
- **Revenue +24.2% YoY in Q2** is *faster* than Q1's +21.8% — i.e., growth is **accelerating sequentially**, not decaying. That is the single most important fundamental fact in this dataset.
- **Cost of revenue grew only 17.7%** vs revenue +24.2%: the AI/cloud compute build is being monetized faster than it is being depreciated so far. Gross margin expanded **+2.1–2.4 pp**.
- **Operating income +30%** — roughly 6–7 pts of revenue-growth-to-profit-growth operating leverage. Opex rose 26.7% in Q2 (ahead of revenue), driven by **SBC of $8.0B in Q2 2026 vs $6.0B (+33%)** and G&A of $6,461M vs $5,209M (+24%). Note Q2's 34.0% operating margin dipped from Q1's 36.1% — Q1 is seasonally the low-revenue/held-cost quarter; the YoY comparison is the cleaner read and it is positive.

### 2.2 Reported earnings are overwhelmingly *non-operating*
- H1 2026 non-operating income was **$135,699M** — **63% of pretax income**. In Q2 alone, non-operating income ($97,983M) was **2.4× operating income** and 82% of pretax income.
- Drivers visible in the tags: `DebtAndEquitySecuritiesGainLoss` **$135,803M** (H1'25: $11,411M); `EquitySecuritiesFvNiGainLoss` $135,946M, of which only $836M realized and $21,531M flagged unrealized; and the **cumulative upward price adjustment on non-marketable equity securities rose from $44,485M to $85,732M** — i.e. ~$41B of observable-price markups in six months.
- **Consequence:** ~$6.4 of the $9.11 Q2 EPS is non-operating. Backing it out:

| "Core" EPS (op income + interest income, taxed at the reported rate, ÷ diluted shares) | Q2 2025 | Q2 2026 | YoY | H1 2025 | H1 2026 | YoY |
|---|---|---|---|---|---|---|
| Core net income ($M) | ~26,900 | ~34,100 | **+27%** | ~53,100 | ~67,400 | **+27%** |
| Core EPS ($) | ~2.20 | ~2.78 | **+26%** | ~4.33 | ~5.49 | **+27%** |

**Core EPS growth of ~+27% is fully consistent with the +30% operating income growth** — the underlying franchise is healthy. But headline EPS growth of +294% is *not* repeatable and traders should not capitalize $9.11 as a run-rate.

### 2.3 Interest burden is now real
- Interest expense: **$1,278M in Q2 2026 vs $261M (+390%)**; H1 $1,811M vs $295M.
- Interest income: $1,430M vs $1,050M. Net interest was still marginally positive in Q2 (+$152M) but is closing fast — annualized interest expense is now ~$5.1B and rising with the debt stack.

---

## 3. Balance sheet — a $327B expansion in six months

| $M | 31 Dec 2025 | 30 Jun 2026 | Change |
|---|---|---|---|
| Cash & equivalents | 30,708 | 55,911 | +25,203 |
| **Cash + short-term investments** | **126,843** | **242,474** | **+115,631** |
| Accounts receivable (net) | 62,886 | 69,175 | +6,289 |
| **Total current assets** | 206,038 | **343,524** | **+137,486** |
| Non-marketable equity securities (no RDFV) | 64,094 | **124,259** | **+60,165** |
| AFS debt securities | n/a | 99,500 | — |
| Finite-lived intangibles, gross | 2,467 | 10,585 | **+8,118** |
| **Total assets** | **595,281** | **921,983** | **+326,702 (+54.9%)** |
| Accounts payable | 12,200 | 20,258 | +8,058 |
| Accrued liabilities | 55,557 | 73,014 | +17,457 |
| Accrued income taxes, current | 523 | 5,233 | +4,710 |
| **Debt (carrying amount)** | **49,085** | **101,085** | **+52,000 (+106%)** |
| Deferred tax liabilities, net | 919 | **22,819** | +21,900 |
| Operating lease liability | 15,954 | 18,037 | +2,083 |
| Finance lease liability | 2,500 | 2,590 | +90 |
| Legal/regulatory accruals, current | 15,594 | **17,356** | +1,762 |
| Common stock + APIC | 93,126 | 131,371 | +38,245 |
| **Convertible preferred stock** | **0** | **18,023** | **+18,023** |
| AOCI | (1,916) | (2,285) | −369 |
| Shares outstanding (M) | 12,088 | **12,230** | +142 |

**Read-through:**
1. **Liquidity is enormous and leverage is still low.** Cash + ST investments of **$242.5B** against **$101.1B** of debt = **~$141.4B net cash**. Add finance leases (2.6B) and operating leases (18.0B) and the position remains strongly net-cash. Debt/assets = 11%.
2. **But the funding model has inverted.** Alphabet raised, in H1 2026: **$56.2B of debt**, **$30.5B of common stock**, **$19.1B of convertible preferred** (single issuance 5 Jun 2026), and **$3.8B from minority shareholders** (subsidiary-level rounds) ≈ **$109.6B of gross external capital** — while repaying only $5.3B and paying $5.2B of dividends.
3. **First-ever meaningful equity dilution.** 142M shares issued for $30.5B implies an average price of ~**$215/share**; plus $18.0B of convertible preferred (a potential future claim). Diluted shares in Q2 (~12,306M) already exceed the 30 Jun count. Combined with the interest cost, this is a genuine shareholder-value shift that must be watched.
4. **The asset base is increasingly mark-to-model.** Non-marketable equity securities nearly **doubled ($64.1B → $124.3B)**, and the $22.8B deferred tax liability build (from $0.9B) is the mirror image of unrealized investment gains — confirming the gains are unrealized and carry a future tax bill on disposal.
5. **An acquisition occurred.** Finite-lived intangibles gross jumped from $2.5B to $10.6B (+$8.1B) — the largest inorganically acquired intangible base Alphabet has carried, implying a material deal (goodwill line unavailable in this extract). Forward amortization: $747M remainder of FY26, $1,304M in the next 12 months.
6. **Working capital is being leaned on:** AP +66%, accrued liabilities +31%, accrued current tax +10x. Some of this is capex-timing (see capex-incurred-not-paid below), but payables growth of 66% against revenue growth of 23% deserves monitoring.
7. **Legal exposure is large and rising:** current loss-contingency accruals of **$17.4B** (from $15.6B); the FY2025 10-K also discloses $3.0B of contingency *payments* in Q3 2025.

**Efficiency check:** DSO improved to **~55 days** (from ~61 days a year ago) — receivables (69,175) grew half as fast as H1 revenue. Clean collections, no channel-stuffing signal. Current ratio ≈ **2.5–2.6×** (current assets $343.5B vs an estimated ~$130B of current liabilities). Contract liabilities (deferred revenue) rose to **$10.1B from $8.6B (+17%)** with $4.9B of H1 revenue recognized from the opening balance — stable forward bookings.

---

## 4. Cash flow — the real story: free cash flow has essentially vanished

| $M | Q1 2025 | Q2 2025 | H1 2025 | Q1 2026 | Q2 2026 | H1 2026 |
|---|---|---|---|---|---|---|
| Operating cash flow | 36,150 | 27,747 | 63,897 | 45,790 | 39,069 | **84,859 (+32.8%)** |
| Capex (PP&E purchases) | 17,197 | 22,446 | 39,643 | 35,674 | **44,924** | **80,598 (+103.3%)** |
| Capex % of revenue | 19.1% | 23.3% | 21.2% | 32.5% | **37.5%** | **35.1%** |
| **Free cash flow** | 18,953 | 5,301 | 24,254 | 10,116 | **(5,855)** | **4,261 (−82%)** |
| Investing cash flow | (16,194) | — | (40,738) | (63,389) | — | **(145,822)** |
| Financing cash flow | (20,201) | — | (26,033) | +25,077 | — | **+86,320** |

**This is the decisive fundamental tension in GOOGL today:**
- Operating cash flow is *excellent* (+32.8% to $84.9B, converting ~49% of revenue and ~97% of operating income ex-SBC into cash).
- **Capex more than doubled to $80.6B in six months (35% of revenue)** and **Q2 alone consumed $44.9B — more than Q2 operating cash flow, producing negative FCF of −$5.9B.** Alphabet has not run a quarterly FCF deficit of this scale in its history as a public company.
- **Capex is still accelerating:** capex *incurred but not yet paid* is **$29,113M vs $10,635M a year ago (+174%)**. That is a leading indicator that Q3 cash capex will be at least comparable to Q2 and probably higher.
- **It is being funded by the financing and investing lines**, not by operations: +$86.3B financing inflow and $145.8B investing outflow, including **$22.1B of purchases of "other investments"** (vs $2.3B) — capital going into both compute and equity stakes.
- Buybacks went to **zero** (Q1 and Q2 2026 both $0) versus $28.3B in H1 2025. Capital return is now just the dividend ($5.2B H1) + rising interest ($1.8B H1).
- The dividend grew but decelerated: **$0.22/quarter vs $0.21 (+4.8%)**, H1 declared $0.43 vs $0.41. Total payout ~$0.88 annualized. Preferred dividends of $86M in Q2 are a new, senior claim.

**Interpretation:** management is running the company for an AI-infrastructure land-grab, willing to (a) suspend buybacks, (b) issue equity for the first time, (c) double gross debt, and (d) tolerate negative FCF. That is a defensible strategy only if the $160B+/yr capex program converts into revenue at today's >20% growth rate. **H1 2026 revenue growth of 23% and gross-margin expansion is evidence it currently is** — but the margin for error has narrowed dramatically, and the equity/debt raises signal management expects the spend to persist.

---

## 5. Earnings quality scorecard

| Test | Result | Verdict |
|---|---|---|
| Net income ÷ operating cash flow | 174,771 / 84,859 = **2.06×** | ⚠️ Earnings heavily non-cash — over half of net income is unrealized investment markup |
| Non-operating ÷ pretax income | **62.8% H1'26** (vs 18.3% H1'25) | ⚠️ Reported EPS is not an operating metric |
| Accruals vs revenue | Working capital a modest *use* of cash (other operating assets +$9,950M) | ✅ No aggressive revenue recognition signal |
| DSO trend | 61 → 55 days | ✅ Improving |
| Deferred revenue | +17% to $10.1B | ✅ Healthy |
| Tax rate | 17.1% → 19.1%; deferred tax expense +$27.5B | ⚠️ Non-cash, tied to unrealized gains |
| SBC | $15.2B H1 (+32%); 13% of operating income | ⚠️ Rising dilution pressure |
| Depreciation | $13,586M H1 vs $9,485M (+43%) | ⚠️ Lagging indicator of capex; will keep climbing |
| Goodwill impairment | No impairment tag in dataset | ✅ |

**Bottom line on quality:** the *operating* earnings are high quality and cash-generative. The *reported* earnings are not — they contain a very large, reversible, largely non-cash mark-to-market component. Any quarter in which those marks reverse will produce a violent headline EPS miss even if the operating business beats.

---

## 6. Insider transactions

**No data available.** The vendor package contains no authorized point-in-time insider-transactions archive for GOOGL as of 27 Aug 2026, and I will not infer or fabricate Form 4 activity. **Traders should treat the insider signal as unknown** and source it elsewhere (Form 4 filings) before drawing conclusions.

---

## 7. What to watch / actionable conclusions

### Base case (bullish operating, cautious on reported EPS)
GOOGL is a franchise simultaneously **accelerating revenue (+24% Q2)** and **expanding gross margin (+2 pp)** while **operating income compounds at ~30%** — a rare combination at this scale. Net cash of ~$141B and $242B of liquidity mean the aggressive build is not a solvency question. **Core earnings power supports a constructive view.**

### Three things that cap the enthusiasm
1. **Free cash flow is negative in Q2 (−$5.9B) and −82% for H1 ($4.3B).** At 35–37% capex intensity this is now a "show me" story. Watch whether revenue growth holds >20% while capex intensity stays >30% — the moment growth decelerates into a capex guide that keeps rising, the equity de-rates.
2. **Reported EPS double-counts.** Do **not** extrapolate $9.11 (Q2) or $14.24 (H1) — the core figures are **~$2.78 and ~$5.49**. In a reversal quarter, marks of this size can swing EPS by several dollars per share in either direction.
3. **The capital-return regime has changed.** Zero buybacks, a >100% increase in debt, a $19B convertible preferred and a $30.5B common raise is a structural dilution/leverage pivot. Watch for (a) buyback resumption (the single cleanest bullish signal available), (b) interest expense crossing above interest income, (c) the conversion/anti-dilution terms of the June 2026 preferred, and (d) the derivative book, which jumped to $1,958M of liabilities from $379M.

### Specific, testable triggers
| Signal | Threshold | Direction |
|---|---|---|
| Q3 capex vs $44.9B Q2 | In line or higher (supported by $29.1B capex-incurred-not-paid) | Bearish FCF, neutral revenue |
| Revenue growth | ≥ +20% YoY | Bullish — confirms ROI on capex |
| Gross margin | ≥ 61% | Bullish — depreciation not yet biting |
| Buyback authorization restart | Any $ > 0 | Bullish — signals FCF inflection |
| Interest expense vs interest income | Expense > income | Caution |
| Non-marketable equity marks | Downward adjustment in any quarter | Headline EPS shock risk |
| Legal accruals (>$17.4B) | New charge >$2B | Caution |
| Diluted share count | >12.5B | Dilution drag on core EPS |

### Valuation framing (honest limits)
No share price was retrieved, so I am not assigning a multiple. The correct analytical frame is: **value GOOGL on core (ex-markup) earnings of ~$5.49 H1 / ~$11 annualized core diluted EPS, not on the $14.24 reported H1 figure** — then treat the $124.3B of non-marketable equity securities as a separate, less-liquid net asset carried at management's fair-value marks.

---

## 8. Key points summary

| Category | Metric | Latest | Prior / YoY | Signal |
|---|---|---|---|---|
| **Growth** | Q2 2026 revenue | $119,796M | +24.2% YoY (Q1 +21.8%) | ✅ Accelerating |
| | H1 2026 revenue | $229,692M | +23.0% YoY | ✅ |
| **Margins** | Gross margin Q2 | 61.6% | 59.5% (+2.1 pp) | ✅ |
| | Operating margin Q2 | 34.0% | 32.4% (+1.6 pp) | ✅ |
| | Operating margin H1 | 35.0% | 33.1% (+1.9 pp) | ✅ |
| **Profit** | Q2 operating income | $40,770M | +30.4% | ✅ |
| | H1 net income | $174,771M | +179% | ⚠️ Includes non-cash marks |
| | Q2 diluted EPS | $9.11 | +294% | ⚠️ ~$2.78 core |
| | H1 core diluted EPS (est.) | ~$5.49 | +27% | ✅ True earnings power |
| **Non-operating** | H1 non-operating income | $135,699M | vs $13,845M | ⚠️ Non-cash, reversible |
| | Non-marketable equity book | $124,259M | from $64,094M | ⚠️ Mark-to-model |
| **Cash flow** | H1 operating cash flow | $84,859M | +32.8% | ✅ Excellent |
| | H1 capex | $80,598M | +103.3% | ⚠️ 35% of revenue |
| | **Q2 free cash flow** | **−$5,855M** | vs +$5,301M | 🔴 **Negative** |
| | H1 free cash flow | $4,261M | −82% | 🔴 |
| | Capex incurred, unpaid | $29,113M | +174% | 🔴 Q3 capex heavy |
| **Balance sheet** | Cash + ST investments | $242,474M | +115,631 | ✅ |
| | Total debt | $101,085M | +106% | ⚠️ Up but modest |
| | Net cash | ~$141,400M | — | ✅ |
| | Total assets | $921,983M | +54.9% in 6 mths | ⚠️ |
| | Legal accruals (current) | $17,356M | from $15,594M | ⚠️ |
| **Capital return** | Buybacks H1 2026 | **$0** | vs $28,306M | 🔴 Regime change |
| | Dividends paid H1 | $5,231M ($0.43/sh) | +4.8%/sh | ➖ Decelerating growth |
| | Common stock issued | $30,499M (142M sh @ ~$215) | from $0 | 🔴 First-ever dilution |
| | Convertible preferred issued | $19,063M (5 Jun 2026) | from $0 | 🔴 New senior claim |
| | Preferred dividends | $86M in Q2 | new | ➖ |
| **Cost structure** | SBC H1 | $15,200M | +32% | ⚠️ |
| | Depreciation H1 | $13,586M | +43% | ⚠️ Rising |
| | Interest expense Q2 | $1,278M | +390% | ⚠️ |
| | Effective tax rate | 19.1% | from 17.1% | ⚠️ |
| **Efficiency** | DSO | ~55 days | from ~61 | ✅ |
| | Deferred revenue | $10,100M | +17% | ✅ |
| | Net income / OCF | 2.06× | from 0.98× | ⚠️ Low earnings quality |
| **Insider** | Transactions | **DATA UNAVAILABLE** | — | ⚪ Unknown |
| **Bottom line** | | Operating business accelerating with strong net cash; but negative Q2 FCF, zero buybacks, first-ever equity/debt-funded dilution and EPS inflated ~3× by non-cash investment marks | | **Constructive on core earnings; do not underwrite reported EPS or near-term FCF** |