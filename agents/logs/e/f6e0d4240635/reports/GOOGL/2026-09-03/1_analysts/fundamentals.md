# GOOGL — Alphabet Inc. Fundamental Research Report
**As-of date: 2026-09-03 | Latest available filing: Q2 FY2026 Form 10-Q (accepted 2026-07-23) | Prior: Q1 FY2026 10-Q (2026-04-30), FY2025 10-K (2026-02-05)**

---

## 0. Data Provenance & Caveats (read first)

| Item | Status |
|---|---|
| Income statement, balance sheet, cash flow | ✅ Retrieved from point-in-time SEC XBRL facts, filtered by EDGAR acceptance timestamp |
| Insider transactions | ❌ **DATA_UNAVAILABLE** — no authorized point-in-time insider archive. **No insider activity is inferred or fabricated in this report.** |
| Segment revenue (Search/Cloud/YouTube/Other Bets) | ❌ Not returned by the data pack — see gaps section |
| Share price / market cap / valuation multiples | ❌ Not in the pack — no price targets or P/E are stated |
| Revenue | ⚠️ **Derived** (= Total costs & expenses + Operating income). Formula validated: it reproduces Alphabet's Q1-2025 reported revenue of $90.234B exactly. |
| Balance sheet at 6/30/26 | ⚠️ Liabilities/equity tags truncated by the data vendor's row cap; figures **~$281B / ~$641B are estimates**, triangulated two independent ways (residual identity + bottom-up liability build). Flagged as such throughout. |

---

## 1. Company Profile

Alphabet Inc. is the parent of Google — the world's largest digital advertising business — plus Google Cloud, YouTube, Android, Chrome, Google Play, Pixel hardware, and the Gemini/DeepMind AI stack. Reporting structure: **Google Services** (Search, YouTube ads, subscriptions/devices, Play), **Google Cloud** (infrastructure + Workspace + AI/TPU rentals), and **Other Bets** (Waymo, Verily, Wing, etc.). Dual-class structure: GOOGL (Class A, 1 vote) and GOOG (Class C, no vote).

**What this data pack reveals about the current strategic posture:** Alphabet is in the middle of the most aggressive capital-deployment and balance-sheet transformation in its history — capex has more than doubled year-over-year, buybacks have gone to **zero**, and the company has simultaneously raised ~$110B of external capital in six months. That is a fundamental regime change from the 2019–2024 "fortress balance sheet + $70–80B/yr buyback" playbook, and it is the single most important fact for framing the stock.

---

## 2. Income Statement — H1 FY2026 vs H1 FY2025

All figures USD millions unless noted. Q1/Q2 split derived from H1 less Q2.

| Line | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|
| **Revenue** (derived) | **229,692** | **186,662** | **+23.1%** |
| Cost of revenue | 87,214 | 75,400 | +15.7% |
| Gross profit | 142,478 | 111,262 | +28.1% |
| *Gross margin* | *62.0%* | *59.6%* | *+240 bps* |
| Operating expenses (R&D + S&M + G&A) | 62,012 | 49,385 | +25.6% |
| **Operating income** | **80,466** | **61,877** | **+30.0%** |
| *Operating margin* | *35.0%* | *33.1%* | *+190 bps* |
| Non-operating income | 135,699 | 13,845 | +880% |
| Pre-tax income | 216,165 | 75,722 | +185% |
| Income tax | 41,394 | 12,986 | +219% |
| *Effective tax rate* | *19.1%* | *17.1%* | *+200 bps* |
| **Net income** | **174,771** | **62,736** | **+179%** |
| Net income to common | 174,685 | 62,736 | — |
| **Diluted EPS** | **$14.24** | **$5.12** | **+178%** |

**Quarterly cadence:**

| | Q1 2026 | Q1 2025 | YoY | Q2 2026 | Q2 2025 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Revenue | 109,896 | 90,234 | +21.8% | 119,796 | 96,428 | **+24.2%** |
| Gross margin | 62.4% | 59.7% | +270bp | 61.6% | 59.5% | +210bp |
| Operating income | 39,696 | 30,606 | +29.7% | 40,770 | 31,271 | +30.4% |
| **Operating margin** | **36.1%** | 33.9% | +220bp | **34.0%** | 32.4% | +160bp |
| Diluted EPS (GAAP) | $5.11 | $2.81 | +82% | $9.11 | $2.31 | +294% |

**Key read-throughs:**
- Top-line acceleration is real and broad-based: **+21.8% → +24.2%** quarter-over-quarter. Revenue is annualizing at roughly **$459B** (Q2 × 4).
- Gross margin expansion of ~240bps despite a massive AI infrastructure build is the strongest single operating signal in the pack — it implies AI/cloud revenue is landing at attractive incremental margins, and/or deprecation has not yet fully caught up with capex (see §5).
- **But the sequential trend is deteriorating:** operating margin fell from 36.1% (Q1) to 34.0% (Q2), a 210bp compression. Total costs & expenses rose +12.6% q/q versus revenue +9.0%. Drivers visible in the data: cost of revenue +11.3% q/q ($41,271M → $45,943M), G&A +50.6% q/q ($4,291M → $6,461M), and legal accruals rising (see §6).

---

## 3. Earnings Quality — This Is the Most Important Section

**63% of H1 2026 pre-tax income came from investment revaluations, not operations.**

| Item | H1 2026 | H1 2025 |
|---|---:|---:|
| Debt & equity securities gains (pre-tax) | **135,803** | 11,411 |
| — of which equity securities FV-NI gains | 135,946 | 11,044 |
| — within that, *unrealized* | 21,531 | 1,088 |
| Pre-tax income **excluding** investment gains | **80,362** | **64,311** |
| Tax at reported rate | 19.1% / 17.1% | |
| **Normalized net income** | **~65,000** | **~53,300** |
| **Normalized diluted EPS** | **~$5.30** | **~$4.35** |
| *Normalized EPS growth* | ***+21.8%*** | |
| Reported diluted EPS | $14.24 | $5.12 |

**Interpretation:**
1. Headline EPS of **$14.24 is not a run-rate number** and should not be annualized. Roughly **two-thirds is mark-to-market** on the non-marketable equity portfolio.
2. The marks are corroborated on the balance sheet: cumulative *upward* price adjustments on equity securities without readily determinable fair value jumped from **$44.5B → $85.7B** (+$41.2B in six months), and the carrying value of those securities went **$64.1B → $124.3B**.
3. **The underlying business still grew normalized EPS +21.8%** — down only modestly from the +24% (Q1) to +18% (Q2) trajectory. So: decelerating, but a high-quality ~20% compounding engine.
4. **Compensation risk is severe.** Any sell-side model anchored on the $14.24 print will be materially wrong. Conversely, Q2's $9.11 print means the stock could "beat" on a GAAP basis even if operations disappoint — a divergence traders should exploit rather than trade blindly.

---

## 4. Balance Sheet

### 4a. Actual reported figures

| | 12/31/2025 | 3/31/2026 | 6/30/2026 | Δ H1 |
|---|---:|---:|---:|---:|
| **Total assets** | 595,281 | 703,919 | **921,983** | **+$326.7B (+54.9%)** |
| Current assets | 206,038 | 213,753 | 343,524 | +$137.5B |
| Cash & equivalents | 30,708 | 38,063 | 55,911 | +$25.2B |
| **Cash + short-term investments** | **126,843** | 126,840 | **242,474** | **+$115.6B** |
| Accounts receivable | 62,886 | 62,999 | 69,175 | +$6.3B |
| Non-marketable equity securities | 64,094 | 101,346 | 124,259 | +$60.2B |
| Available-for-sale debt securities | — | 82,733 | 99,500 | — |
| Finite-lived intangibles, gross | 2,467 | 10,626 | 10,585 | **+$8.1B** |
| **Total debt (carrying)** | **49,085** | **80,305** | **101,085** | **+$52.0B (+106%)** |
| Deferred tax liabilities, net | 919 | — | 22,819 | +$21.9B |
| **Total liabilities** | **180,016** | **225,173** | *~281,400 (est.)* | *+$101B* |
| **Total stockholders' equity** | **415,265** | **478,746** | *~640,600 (est.)* | *+$225B* |
| Convertible preferred stock | 0 | 0 | **18,023** | **new** |
| Common stock + APIC | 93,126 | 96,902 | 131,371 | +$38.2B |
| Shares outstanding | 12,088M | 12,116M | 12,230M | +1.2% |

### 4b. What actually happened on this balance sheet
- **Total assets grew 55% in six months.** That is not organic. The inflation comes from (i) ~$41B of private-company marks, (ii) ~$22B of new "other investments," (iii) ~$8B of acquired intangibles, and (iv) a tripling of short-term investment holdings funded by debt and equity issuance.
- **Debt more than doubled to $101.1B**, and **$19.0B of convertible preferred** was issued on **2026-06-05** (carrying $18.0B; H1 preferred dividends only $86M → implied coupon ≈ **1.8–1.9%**, i.e. very cheap conversion-linked capital).
- **Finite-lived intangibles gross went from $2.5B → $10.6B**, with a new amortization ramp scheduled: **$1,304M (next 12 mo)**, then $1,142M, $1,096M, $1,055M. Together with the "Other Investments" step-up, this is strong evidence of **a significant acquisition and/or strategic stake purchase closing in Q1–Q2 2026.** The tools do not identify the counterparty; treat the specific target as unconfirmed.
- **Deferred tax liabilities went from $919M → $22,819M** — the tax bill crystallizing on the unrealized investment gains. This is a real future cash consideration, not cosmetic.

### 4c. Liquidity & leverage — still pristine, but no longer fortress-like
- Net cash position: **$242.5B liquid − $101.1B debt = +$141.4B** (preferred excluded). Even treating the $18.0B preferred as debt: **+$123.4B net cash.**
- Net debt / equity: **negative**. Gross debt / equity ≈ **16%**. Leverage is not a solvency risk at these levels.
- Current ratio: **343,524 / ~127,500 (est. current liabilities) ≈ 2.7x** — comfortable.
- **The relevance is not solvency, it is capital allocation.** Alphabet has swapped a shrinking, buyback-supported share count for an expanding one. See §7.

---

## 5. Cash Flow — The Most Actionable Signal in This Report

| | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|
| **Operating cash flow** | **84,859** | 63,897 | **+32.8%** |
| *Less: deferred-tax non-cash add-back* | *(27,538)* | *(−1,596)* | |
| **OCF ex deferred taxes** | **57,321** | **65,493** | **−12.5%** |
| Capital expenditures (cash) | **80,598** | 39,643 | **+103.3%** |
| **Free cash flow (reported basis)** | **+4,261** | **+24,254** | **−82.4%** |
| **FCF (ex deferred-tax add-back)** | **(23,277)** | **+25,850** | **swing of ~$49B** |
| Capex / revenue | **35.1%** | 21.2% | +1,390 bps |
| Capex / operating cash flow | **95.0%** | 62.0% | — |
| Depreciation | 13,586 | 9,485 | +43.2% |
| Stock-based compensation | 15,200 | 11,500 | +32.2% |
| Capex incurred but **not yet paid** (BS) | **29,113** | 10,635 | +174% |

**Quarterly breakdown — the standout datapoint:**

| | Q1 2026 | Q2 2026 |
|---|---:|---:|
| Operating cash flow | 45,790 | 39,069 |
| Capex | 35,674 | **44,924** |
| **Free cash flow** | **+10,116** | **−5,855** |

**Q2 2026 produced negative free cash flow — the first in Alphabet's modern history.** Three points compound the concern:

1. **Capex is still accelerating**, not plateauing: $35.7B → $44.9B sequential quarter.
2. **$29.1B of capex is incurred but unpaid** on the balance sheet. Q3 cash capex will therefore be *higher* than the cash-flow capex line implies — a hidden Q3 FCF trap.
3. **The +33% headline OCF growth overstates cash generation.** $27.5B of it is a non-cash deferred-tax add-back tied to the investment marks. Strip that out and underlying operating cash flow *fell 12.5% year-over-year*. Both adjustments (gain and tax) net to roughly zero on the income statement, but on the cash flow statement the TAX add-back is a genuine cash benefit that flatters OCF.

**Forward margin math that the market may be under-pricing:** H1 depreciation of $13.6B is only **16.9% of H1 capex of $80.6B**. As the AI datacenter base is placed in service, depreciation must converge toward capex. If annualized capex runs ~$180B and useful lives are ~6 years, steady-state depreciation alone approaches **~$30B/quarter** versus **~$7B/quarter** today. That is a multi-year, multi-hundred-basis-point structural headwind to operating margin that has *not yet* appeared in the P&L. It is the central debate in the stock.

---

## 6. Legal, Contingency & Other Charges

- **Loss contingency accrual (current): $15,594M → $17,356M** (+$1,762M in Q2 alone). This is a very large legal/regulatory reserve — consistent with ongoing antitrust, ad-tech, and privacy exposure.
- FY2025 10-K discloses **$3.0B of loss-contingency payments** in Q3 FY2025 — legal settlements are already a recurring cash drag.
- Accrued liabilities jumped **$55,557M → $73,014M (+31.4%)** in six months, far faster than revenue (+23%). G&A rose +50.6% quarter-over-quarter. Some of this is AI-related spend, but the legal line is a meaningful contributor.
- **Accrued income taxes current rose $523M → $5,233M (10x)** and noncurrent $9,531M → $11,306M — cash tax payments step up materially in H2 2026.

---

## 7. Capital Allocation — A Regime Change

| Financing / Investing activity (H1) | 2026 | 2025 |
|---|---:|---:|
| Proceeds from debt issuance, net | **+56,226** | 31,378 |
| Proceeds from **common stock issuance** | **+30,499** | 0 |
| Proceeds from **convertible preferred** | **+19,063** | 0 |
| Proceeds from minority shareholders | **+3,758** | 400 |
| Debt repayments | (5,253) | (18,397) |
| **Share repurchases** | **0** | **(28,306)** |
| Dividends paid | (5,231) | (4,977) |
| Purchases of other (non-marketable) investments | **(22,051)** | (2,312) |
| **Net financing cash flow** | **+86,320** | **(26,033)** |
| **Net investing cash flow** | **(145,822)** | (40,738) |

**Alphabet raised ~$109.5B of external capital in six months and bought back zero stock.**

- **$30.5B of common equity issued.** For a company generating $85B of operating cash flow, issuing equity is a strong signal — either management believes the shares are richly valued, or the capital is earmarked for something strategic and time-sensitive (the intangibles/investments data points toward an acquisition or a large AI partnership stake).
- **Share count rose 1.2% YTD** (12,088M → 12,230M), the first sustained dilution in years, plus $18.0B of convertible preferred sitting ahead of common. Combined dilution overhang on a fully converted basis is meaningful.
- **Dividend remains token:** $0.21 (Q1) → $0.22 (Q2) per share, $5.23B in H1, growing ~5%. Not an income instrument.
- **$22.1B into "other investments"** (9.5x last year) — Alphabet is now behaving partly like a sovereign AI/tech fund. This is *not* operating capex; it is strategic equity. Important distinction: it consumes FCF but does not generate depreciation.

---

## 8. Trend Data Across Years (where the pack provides it)

| Metric | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Net financing cash flow | (72,093) | (79,733) | (37,388) |
| Capex incurred but unpaid (YE) | 7,435 | 10,326 | 15,090 |
| Finance lease principal payments | 705 | 405 | 1,988 |
| Filing | 10-K | 10-K | 10-K |

The FY2023→FY2024→FY2025 reduction in net financing outflow (−72.1 → −79.7 → −37.4) shows buybacks already decelerating into 2025 before the full stop in 2026 — a gradual, not abrupt, capital-allocation pivot. The accrued-but-unpaid capex series (7.4 → 10.3 → 15.1 → **29.1** at 6/30/26) is the cleanest available proxy for the accelerating buildout.

---

## 9. Insider Transactions

**Not available.** The data vendor explicitly returned `DATA_UNAVAILABLE` for GOOGL insider transactions, with instruction not to infer or fabricate. No conclusion about insider sentiment should be drawn from this report. This is a genuine gap in the evidence base and should be sourced separately before acting.

---

## 10. Risk Register (ranked by materiality to a trading decision)

| # | Risk | Evidence | Direction |
|---|---|---|---|
| 1 | **FCF compression / capex escalation** | Q2 FCF **−$5.9B**; capex/revenue 35.1%; $29.1B accrued unpaid capex | High — supports de-rating vs. historical FCF multiples |
| 2 | **Earnings-quality misread** | 63% of H1 pre-tax is investment marks; GAAP EPS $14.24 vs. normalized ~$5.30 | High — source of violent comp-driven volatility |
| 3 | **Depreciation catch-up** | Depreciation only 16.9% of capex; D&A must ramp toward ~$120B+/yr at current spend | High — structural margin headwind not yet in P&L |
| 4 | **Mark-to-market reversal** | $85.7B cumulative upward adjustments on private holdings are **illiquid and reversible** | Medium-High — non-cash, but hits GAAP EPS hard in a drawdown |
| 5 | **Dilution + leverage shift** | +1.2% shares, $19.0B convertible preferred, debt doubled to $101.1B | Medium — erodes per-share compounding |
| 6 | **Tax step-up** | Deferred tax liabilities $0.9B → $22.8B; accrued income tax +$6.0B; rate 17.1% → 19.1% | Medium — real cash drag in H2 |
| 7 | **Legal/antitrust** | Accrual $17.4B, +$1.8B in Q2; $3.0B paid in Q3 FY2025 | Medium — binary headline risk |
| 8 | **Margin deceleration** | Op margin 36.1% → 34.0% q/q; G&A +50.6% q/q | Medium — most recent data is the weakest |
| 9 | **SBC creep** | $15.2B H1 (+32%), 6.6% of revenue | Low-Medium |

**Mitigants:** $242.5B of liquid assets vs. $101.1B debt; gross margin *expanding* (+240bps); revenue *accelerating* (+21.8% → +24.2%); normalized EPS +21.8%; operating income +30%. The operating business is not deteriorating — the *quality and cash conversion* of the reported result is.

---

## 11. Actionable Framing for Traders

1. **Separate the two GOOGL narratives.** The GAAP story ("EPS up 178%, $14.24") and the cash story ("FCF −82%, Q2 FCF negative") are both true. Position sizing should reflect which one you are trading. GAAP beats are likely for 2–3 more quarters because of the private-mark tailwind; FCF misses are also likely.
2. **Watch the Q3 2026 print for three specific items:** (a) cash capex — must account for the $29.1B accrued-unpaid overhang; (b) whether operating margin stabilizes above ~34% or breaks lower; (c) the split between "Google Services" and "Cloud" — unavailable here and essential to validating that +24% growth is durable.
3. **The buyback halt is the under-discussed catalyst.** Resumption of repurchases (or an explicit statement that capex has peaked) would be a powerful positive re-rating signal. Continued zero buybacks alongside further equity/preferred issuance would be a negative signal about management's view of intrinsic value.
4. **The $30.5B common issuance at ~$267/share is an implicit management price signal.** Management sold equity at that level. Historically, that has not marked a top — but it does set an anchor and reveals financing preference.
5. **The AI investment thesis is intact but is being funded with balance sheet capacity, not internal cash.** Net cash of $141B gives enormous runway — roughly 3+ years at the current capex trajectory before external funding is needed again. That materially reduces the tail risk of a financing shock, even as FCF optics deteriorate.
6. **Normalized EPS of ~$5.30 for H1 2026 (~$10.60 annualized run-rate, growing ~20%) is the correct anchor for any multiple-based work.** Do not use $14.24.
7. **Insider flow is unknown — do not assume it is neutral.** Source it independently; it is a genuine information gap in this analysis.

---

## 12. Summary Table — Key Points

| Category | Metric | H1 FY2026 | H1 FY2025 | YoY / Δ | Signal |
|---|---|---:|---:|---|---|
| **Growth** | Revenue (derived) | $229.7B | $186.7B | **+23.1%** | 🟢 Accelerating (Q1 +21.8% → Q2 +24.2%) |
| | Operating income | $80.5B | $61.9B | +30.0% | 🟢 |
| | Diluted EPS (GAAP) | $14.24 | $5.12 | +178% | 🟡 Distorted by marks |
| **Margins** | Gross margin | 62.0% | 59.6% | +240 bps | 🟢 |
| | Operating margin | 35.0% | 33.1% | +190 bps | 🟢 Y/Y, 🔴 Q/Q (36.1%→34.0%) |
| | Effective tax rate | 19.1% | 17.1% | +200 bps | 🔴 |
| **Quality of earnings** | Investment gains (pre-tax) | $135.8B | $11.4B | 12x | 🔴 63% of pre-tax income |
| | **Normalized EPS (ex-gains)** | **~$5.30** | **~$4.35** | **+21.8%** | 🟢 True run-rate |
| **Cash flow** | Operating cash flow | $84.9B | $63.9B | +32.8% | 🟡 $27.5B is deferred-tax add-back |
| | OCF ex-deferred tax | $57.3B | $65.5B | **−12.5%** | 🔴 |
| | Capital expenditures | $80.6B | $39.6B | **+103%** | 🔴 Capex/revenue 35.1% |
| | **Free cash flow** | **+$4.3B** | **+$24.3B** | **−82%** | 🔴 **Q2 FCF = −$5.9B** |
| | Accrued but unpaid capex | $29.1B | $10.6B | +174% | 🔴 Q3 FCF risk |
| **Balance sheet** | Total assets | $922.0B | $595.3B* | +54.9% | 🟡 Mark inflation |
| | Cash + ST investments | $242.5B | $126.8B* | +91% | 🟢 |
| | Total debt | $101.1B | $49.1B* | **+106%** | 🟡 Still net cash |
| | Net cash | +$141.4B | +$77.8B* | +$63.6B | 🟢 |
| | Total liabilities (6/30) | *~$281B (est.)* | $180.0B* | +$101B | 🟡 |
| | Stockholders' equity (6/30) | *~$641B (est.)* | $415.3B* | +$225B | 🟡 |
| **Capital allocation** | Share repurchases | **$0** | $28.3B | −100% | 🔴 Regime change |
| | Common stock issued | +$30.5B | $0 | new | 🔴 Dilution (+1.2% shares) |
| | Convertible preferred issued | +$19.1B | $0 | new (2026-06-05) | 🟡 ~1.8% coupon |
| | Debt issued, net | +$56.2B | +$31.4B | +79% | 🟡 |
| | Dividends paid | $5.2B | $5.0B | +5.1% | 🟡 Token ($0.43/sh H1) |
| **Strategic** | Non-marketable equity holdings | $124.3B | $64.1B* | +94% | 🟡 Illiquid, marked up $85.7B cumulative |
| | Intangibles, gross | $10.6B | $2.5B* | +329% | 🟡 Implies material M&A |
| **Risk** | Legal loss contingency accrual | $17.4B | $15.6B* | +11.3% | 🔴 |
| **Data gap** | Insider transactions | — | — | — | ⚪ **UNAVAILABLE — not inferred** |

\* *Prior-period comparative refers to 12/31/2025 balance sheet, not H1 2025, since balance-sheet tags are point-in-time.*

---

**Bottom line:** GOOGL's *operating* engine is accelerating — revenue +23%, gross margin +240bps, normalized EPS +22%, and an expanding $141B net cash buffer. But the *reported* numbers are heavily flattered by $135.8B of largely non-cash private-company marks, while the cash-flow engine has inverted: capex has doubled, buybacks have stopped, $109.5B of external capital was raised, and Q2 2026 delivered **negative free cash flow for the first time**. The durable debate is not growth — it is whether a 35%-of-revenue AI capex program converts into returns before depreciation catches up. Traders should anchor on ~$5.30 H1 normalized EPS, treat the $29.1B accrued capex as a Q3 FCF landmine, and watch for a buyback resumption as the cleanest positive catalyst. Insider data was unavailable and must be sourced independently.