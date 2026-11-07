# GOOGL — Alphabet Inc. Fundamental Deep Dive
**As of 2026-09-28 | Latest period: Q2 FY2026 (quarter ended 2026-06-30), 10-Q accepted 2026-07-23 | FY2025 10-K filed 2026-02-05**

---

## 1. Executive summary

Alphabet's Q2 FY2026 results show **genuinely accelerating core operations** — revenue up ~24% YoY, operating income up 30%, and operating margin expanding to 34% — but the headline numbers are **heavily distorted by an extraordinary $135.9B non-operating mark-to-market gain** on equity securities booked in H1 2026 ($99.0B of it in Q2 alone). Reported diluted EPS of **$9.11 in Q2 (+294% YoY)** and **$14.24 in H1** are not representative of earnings power. Stripping the mark, **"core" EPS is roughly $2.60 in Q2 (+17% YoY) and $5.29 in H1 (+22% YoY)**.

Simultaneously, the balance sheet has been **transformed in six months**: total assets +54.9% to **$922.0B**, gross debt more than doubled to **$101.1B**, **$30.5B of common stock** and **$19.0B of convertible preferred** were issued, a **$3.8B subsidiary-level minority raise** occurred, and the **buyback went to zero** (vs. $28.3B in H1 2025). Capital expenditure doubled to **$80.6B in H1 (35.1% of revenue)**, driving free cash flow down **82% to just $4.3B** — with Q2 free cash flow actually **negative (-$5.9B)**.

**Net assessment: bullish core operating trend, but materially degraded earnings quality and free-cash-flow optics versus 2025.** The stock should be valued on core EPS (~$10.40 annualized run-rate), not the inflated GAAP figure. Liquidity remains fortress-like ($242.5B cash + investments vs. $100.2B debt), so the leverage build is not a solvency issue — it is a capital-allocation and dilution issue.

---

## 2. Company profile

Alphabet Inc. (NASDAQ: GOOGL, Class A) is the parent of Google, organized around **Google Services** (Search, YouTube advertising, Android, Chrome, Play, hardware, subscriptions), **Google Cloud** (infrastructure, Workspace, AI platform), and **Other Bets** (early-stage ventures including autonomous driving and life sciences). The company's economic engine is advertising, with Cloud as the second profit pool; the current capital program is overwhelmingly directed at AI compute infrastructure (data centers, TPUs/GPUs, networking).

*Note: the vendor extract did not return segment-level revenue or operating income rows, so segment mix cannot be quantified in this report. All P&L figures below are consolidated.*

---

## 3. Income statement analysis

### 3.1 Reported vs. prior year

The feed did not expose the `Revenues` tag within its returned window; revenue is **derived as `CostsAndExpenses` + `OperatingIncomeLoss`** (validated because the derivation exactly reproduces Alphabet's reported Q1-25 $90.2B and Q2-25 $96.4B).

| $ millions | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | 119,796 | 96,428 | **+24.2%** | 229,692 | 186,662 | **+23.0%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| Gross profit | 73,853 | 57,389 | +28.7% | 142,478 | 111,262 | +28.1% |
| Gross margin | 61.6% | 59.5% | +2.1 pts | 62.0% | 59.6% | +2.4 pts |
| Total costs & expenses | 79,026 | 65,157 | +21.3% | 149,226 | 124,785 | +19.6% |
| **Operating income** | **40,770** | **31,271** | **+30.4%** | **80,466** | **61,877** | **+30.0%** |
| Operating margin | 34.0% | 32.4% | +1.6 pts | 35.0% | 33.1% | +1.9 pts |
| Non-operating income | 97,983 | 2,662 | n.m. | 135,699 | 13,845 | n.m. |
| Pre-tax income | 138,753 | 33,933 | +309% | 216,165 | 75,722 | +185% |
| Tax | 26,560 | 5,737 | — | 41,394 | 12,986 | — |
| Effective tax rate | 19.1% | 16.9% | +2.2 pts | 19.1% | 17.1% | +2.0 pts |
| **Net income** | **112,193** | **28,196** | **+298%** | **174,771** | **62,736** | **+179%** |
| Diluted EPS | $9.11 | $2.31 | +294% | $14.24 | $5.12 | +178% |
| Diluted shares (M) | 12,316 | 12,206 | +0.9% | 12,273 | 12,253 | +0.2% |

**Key operating reads:**
- **Incremental operating margin of 43%** in H1 ($18.6B of incremental operating income on $43.0B of incremental revenue) — evidence of real operating leverage, not just cost deferral.
- Gross margin expanded 210–240 bps despite an aggressive AI infrastructure build, implying either favorable revenue mix (Cloud/enterprise) or disciplined depreciation timing. This is the single most important bullish data point.
- Q1 2026 standalone (derived): revenue $109.9B (+21.8%), operating income $39.7B, **36.1% margin**; Q2 margin of 34.0% is a sequential step down — worth monitoring, as it may reflect the first wave of AI depreciation and higher cloud serving costs.
- **G&A rose 24% YoY in Q2** ($6.46B vs $5.21B) and 23% in H1 — faster than the 19.6% total cost growth; consistent with scaling, legal, and AI-related spend.

### 3.2 Earnings quality — the critical adjustment

H1 2026 non-operating income of **$135.7B** is composed almost entirely of **`EquitySecuritiesFvNiGainLoss` = $135.9B** (realized $0.8B + unrealized $21.5B on marketable names), net of interest expense ($1.81B), plus interest income ($2.81B). This is a **non-cash, non-recurring fair-value remeasurement**, likely an upward "observable price change" on a large strategic stake, partly tied to a capital event.

| $ millions | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---:|---:|---:|---:|
| Reported net income | 112,193 | 28,196 | 174,771 | 62,736 |
| Less: equity securities FVNI gain (after 19.1%/17.1% tax) | (80,116) | (1,069) | (109,865) | (9,468) |
| **Core net income** | **32,077** | **27,127** | **64,906** | **53,268** |
| **Core diluted EPS** | **$2.60** | **$2.22** | **$5.29** | **$4.35** |
| Core EPS growth | **+17.1%** | — | **+21.6%** | — |
| Core net margin | 26.8% | 28.1% | 28.3% | 28.5% |

**Implications for traders:**
1. **~63% of H1 2026 net income is mark-to-market, not operations.** Any screen using trailing GAAP P/E is understating the multiple by roughly 2.7x.
2. A **full reversal** of the gain would be ~$110B after tax, or **~$8.93/share** — three-plus quarters of core earnings. A 25% reversal is ~$2.23/share.
3. Core net margin *compressed* slightly (28.3% vs 28.5%) despite operating margin expansion, because of **6x higher interest expense** ($1.81B vs $0.30B) and a **200 bp higher tax rate**.
4. The **deferred tax liability jumped from $0.92B to $22.82B** — the tax on unrealized appreciation is being deferred, not paid. If the asset is sold or the mark reverses, this unwinds with P&L and cash consequences.

---

## 4. Balance sheet — a six-month transformation

| $ millions | 2026-06-30 | 2025-12-31 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 55,911 | 30,708 | +82% |
| Cash + short-term investments | **242,474** | 126,843 | **+91%** |
| Available-for-sale debt securities | 99,500 | n/a | — |
| Accounts receivable, net | 69,175 | 62,886 | +10% |
| Current assets | 343,524 | 206,038 | +66.7% |
| Equity securities w/o readily determinable FV | **124,259** | 64,094 | **+94%** |
| Finite-lived intangibles, gross | 10,585 | 2,467 | +329% |
| **Total assets** | **921,983** | **595,281** | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66% |
| Accrued liabilities | 73,014 | 55,557 | +31% |
| Accrued income taxes, current | 5,233 | 523 | +900% |
| Legal/loss contingency accrual (current) | 17,356 | 15,594 | +11% |
| Contract liabilities, current | 7,154 | 6,578 | +9% |
| **Debt, gross carrying** | **101,085** | 49,085 | **+106%** |
| Operating lease liabilities | 18,037 | 15,954 | +13% |
| Finance lease liabilities | 2,590 | 2,500 | +4% |
| **Deferred tax liabilities** | **22,819** | 919 | **+2,383%** |
| Accrued income taxes, noncurrent | 11,306 | 9,531 | +19% |
| **Convertible preferred stock** | **18,023** | 0 | new |
| Common stock + APIC | 131,371 | 93,126 | +41% |
| Shares outstanding (M) | 12,230 | 12,088 | +1.2% |

**Analysis:**
- **Liquidity is still exceptional.** Cash + investments of $242.5B less gross debt of $101.1B = **~$142.3B net cash**; including $20.6B of lease liabilities it is **~$120.8B**, and after the $18.0B preferred claim **~$124.3B**. Interest coverage on H1 operating income is **~44x**.
- **But leverage is rising fast.** Gross debt +$52.0B in six months; interest expense run-rate has gone from ~$0.6B/yr to ~$3.6B/yr. A further $56.2B of debt was issued in H1 alone.
- **The preferred is a new senior claim.** $19.0B raised on 2026-06-05; $86M of preferred dividends paid in Q2 alone implies a high-single-digit coupon. Preferred holders rank ahead of common and the instrument carries conversion potential — a future dilution overhang.
- **Share count is rising, not falling.** 12.088B → 12.230B (+1.2%) from $30.5B of common stock issuance plus SBC. This is the **first dilution regime since before 2023** and removes a multi-year EPS tailwind.
- **Receivables quality is fine:** AR +10% versus H1 revenue +23% implies DSO improved to ~52 days; allowance is only 1.4% of gross AR.
- **Legal exposure is large and creeping:** $17.4B of current loss-contingency accruals (vs. $15.6B), after $3.0B of payments in Q3 2025.
- **Total equity could not be computed** — retained earnings and stockholders' equity rows fall outside the vendor's returned window, so ROE/ROIC and book value per share are not calculable from this extract.

---

## 5. Cash flow — the real story of the quarter

| $ millions | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|---:|---:|
| Operating cash flow | 39,069 | 27,747 | **84,859** | 63,897 | **+32.8%** |
| Capital expenditures | 44,924 | 22,446 | **80,598** | 39,643 | **+103.3%** |
| **Free cash flow** | **(5,855)** | **5,301** | **4,261** | **24,254** | **-82.4%** |
| Capex / revenue | 37.5% | 23.3% | 35.1% | 21.2% | +13.9 pts |
| CFO / revenue | 32.6% | 28.8% | 36.9% | 34.2% | +2.7 pts |
| Share repurchases | 0 | n/a | **0** | 28,306 | -100% |
| Dividends paid | ~2,689 | ~2,579 | 5,231 | 4,977 | +5.1% |
| Dividends per share (declared) | $0.22 | $0.21 | $0.43 | $0.41 | +4.9% |
| Debt issued, net | — | — | 56,226 | 31,378 | +79% |
| Common stock issued | — | — | 30,499 | 0 | new |
| Convertible preferred issued | — | — | 19,063 | 0 | new |
| Minority interest proceeds | — | — | 3,758 | 400 | +840% |
| Other investment purchases | — | — | 22,051 | 2,312 | +854% |

**What this tells us:**
1. **Operating cash generation is accelerating (+33%)** — the core business is funding more of the build than the headline FCF suggests.
2. **Capex has doubled and is running at 35–37% of revenue.** Critically, **$29.1B of capex was incurred but unpaid at 6/30** (vs. $10.6B a year earlier), meaning reported capex *understates* true economic spend and H2 cash capex will carry this backlog. Annualized capex is on a ~$170–180B trajectory.
3. **Q2 FCF was negative.** Even at $120B quarterly revenue, the company is now outspending its operating cash flow at the margin. This is the single biggest change in the Alphabet investment case versus 2023–2025.
4. **Capital returns were cut to fund the build:** buybacks went from $28.3B to **zero**, while dividends grew only 5%. The ~$28B/yr of buyback support for EPS is gone, replaced by dilution.
5. **The raise was pre-funded and multi-channel:** ~$109.5B of gross financing (debt + common + preferred + minority) in six months, plus $22.1B deployed into "other investments." The strategic-investment program is now large enough to move the consolidated balance sheet.

---

## 6. Insider transactions

**DATA UNAVAILABLE.** The vendor's point-in-time archive contains no authorized insider-transaction records for GOOGL as of 2026-09-28. No insider buying or selling should be inferred, assumed, or fabricated. Traders should source Form 4 data separately before drawing conclusions about management conviction.

---

## 7. Risks and red flags

| Risk | Evidence | Severity |
|---|---|---|
| **Mark-to-market reversal** | $135.9B FVNI gain = 63% of H1 net income; non-cash | **High** — optical EPS collapse risk |
| **Negative/compressed FCF** | Q2 FCF -$5.9B; H1 FCF $4.3B vs $24.3B | **High** — changes the "cash machine" narrative |
| **Capex escalation** | Capex +103%; $29.1B accrued unpaid; 35% of revenue | **High** — depreciation cliff ahead |
| **Dilution** | +$30.5B common, +$19.0B convertible preferred, shares +1.2% | **Medium-High** |
| **Leverage/interest** | Debt +106% to $101.1B; interest expense 6x YoY | **Medium** (44x coverage) |
| **Tax rate** | 17.1% → 19.1%; DTL $22.8B | **Medium** |
| **Depreciation lag** | D&A +43% YoY vs revenue +23%; still ramping | **Medium** — margin headwind in 2027 |
| **SBC** | $15.2B H1, +32% YoY (6.6% of revenue) | **Medium** |
| **Legal/regulatory** | $17.4B current loss accruals; $3.0B paid in Q3-25 | **Medium** |
| **Concentration in AI capex cycle** | ~$80B/H1 with no disclosed segment ROI | **Medium** |

**Notable disconnect to flag:** the $135.9B FVNI gain cannot be fully reconciled to the $60.2B increase in non-marketable equity ($64.1B → $124.3B, with $85.7B cumulative upward and $9.1B downward adjustments). Part of the gain likely relates to securities classified elsewhere or to a remeasurement/reclassification event. Treat the precise composition as uncertain; treat the *magnitude and non-cash nature* as certain.

---

## 8. Actionable framework for traders

**What is working (buy-side evidence):**
- Revenue re-accelerated to **+24% YoY**, the strongest in years, with **43% incremental operating margins**.
- Gross margin *expanded* through an infrastructure build — a strong signal on pricing/mix.
- **$142B net cash** and 44x interest coverage mean the capex program is fully self-fundable, even with negative FCF.
- Dividend continues to grow (~$0.88 annualized).

**What is deteriorating (sell/hedge-side evidence):**
- **Earnings quality:** strip out $136B of marks and core EPS grows ~17–22%, not 178%.
- **FCF inflected negative** in Q2; the buyback is switched off; shares are being issued.
- **Depreciation (+43%) and interest (+514%) are both lagging indicators that get worse** before they get better as H1 capex enters service.

**Concrete positioning considerations:**
1. **Value GOOGL on ~$10.40–10.60 of annualized core EPS** (Q2 $2.60 × 4 = $10.40; H1 $5.29 × 2 = $10.58). Each turn of P/E on that base is worth ~$10.40/share. Any screen showing a mid-teens multiple is using inflated GAAP EPS and is wrong — the true core multiple is roughly **2.7x higher** than the headline.
2. **Do not extrapolate Q2 GAAP EPS.** Expect a dramatic optical YoY EPS decline in any quarter where the mark is stable or reverses, even with perfect operations.
3. **Watch the Q3 FY2026 report (late October 2026, ~4 weeks out).** Specific checkpoints:
   - Revenue growth ≥20% and operating margin ≥33% (below that, the Q1 36% margin was a peak).
   - **FY2026 capex guidance** — H1 was $80.6B plus $29.1B accrued; a guide above ~$175B would pressure FCF further.
   - Whether **buybacks resume** — a restart would be a strong signal management sees the shares as undervalued and is comfortable with FCF.
   - **Any partial reversal of the FVNI gain** and the associated deferred-tax unwind.
   - Cloud/segment disclosure and any update on the $22.1B of strategic investments.
4. **Credit/liquidity trade:** with $142B net cash and 44x coverage, credit risk is low; the equity risk is *multiple* risk and *FCF* risk, not solvency risk.
5. **Key falsification tests for the bull case:** (a) operating margin falls below 30% for two consecutive quarters; (b) capex/revenue stays above 35% into 2027 without commensurate revenue acceleration; (c) buybacks remain at zero while share count keeps rising; (d) the FVNI gain reverses by more than 25% without an offsetting operating beat.

---

## 9. Data caveats

- **Revenue is derived** (`CostsAndExpenses` + `OperatingIncomeLoss`) because the vendor's returned window cut off before the `Revenues` tag. The derivation reproduces reported Q1-25 ($90.2B) and Q2-25 ($96.4B) exactly, giving high confidence.
- **`annual` frequency returned identical interim 10-Q data** — no FY2023/FY2024/FY2025 full-year income statement, cash flow, or segment rows were exposed. Multi-year history could not be independently reconstructed beyond the disclosed FY financing outflows (-$72.1B in 2023, -$79.7B in 2024, -$37.4B in 2025) and capex-incurred-but-unpaid ($7.4B / $10.3B / $15.1B).
- **Stockholders' equity, retained earnings, goodwill, R&D and S&M expense, and segment results** fell outside the returned window; ROE, ROIC, book value, and segment margins are therefore not computable.
- **No price or market-cap data** was available from this toolset, so no P/E, P/S, or EV multiples are presented; the framework above is expressed per-share in EPS terms.
- **Insider transactions: unavailable** (see Section 6).

---

## 10. Key points summary

| Category | Metric | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | Signal |
|---|---|---:|---:|---:|---:|---|
| Growth | Revenue ($M, derived) | 119,796 | 96,428 | 229,692 | 186,662 | **Bullish** (+24.2% / +23.0%) |
| Growth | Operating income ($M) | 40,770 | 31,271 | 80,466 | 61,877 | **Bullish** (+30.4% / +30.0%) |
| Margins | Operating margin | 34.0% | 32.4% | 35.0% | 33.1% | **Bullish** (+160/+190 bps) |
| Margins | Gross margin | 61.6% | 59.5% | 62.0% | 59.6% | **Bullish** (+210/+240 bps) |
| Margins | Core net margin | 26.8% | 28.1% | 28.3% | 28.5% | **Neutral/negative** (interest + tax) |
| Earnings | Reported diluted EPS | $9.11 | $2.31 | $14.24 | $5.12 | **Distorted** (+294%) |
| Earnings | **Core diluted EPS** | **$2.60** | **$2.22** | **$5.29** | **$4.35** | **Bullish** (+17.1% / +21.6%) |
| Earnings | Non-operating income ($M) | 97,983 | 2,662 | 135,699 | 13,845 | **Warning** — 63% of H1 NI is marks |
| Earnings | Effective tax rate | 19.1% | 16.9% | 19.1% | 17.1% | **Negative** (+200 bps) |
| Earnings | SBC ($M) | 8,000 | 6,000 | 15,200 | 11,500 | **Negative** (+32%) |
| Earnings | Depreciation ($M) | n/a | n/a | 13,586 | 9,485 | **Negative** (+43%) |
| Cash flow | Operating cash flow ($M) | 39,069 | 27,747 | 84,859 | 63,897 | **Bullish** (+32.8%) |
| Cash flow | Capex ($M) | 44,924 | 22,446 | 80,598 | 39,643 | **Negative** (+103%) |
| Cash flow | **Free cash flow ($M)** | **(5,855)** | **5,301** | **4,261** | **24,254** | **Bearish** (-82%) |
| Cash flow | Capex / revenue | 37.5% | 23.3% | 35.1% | 21.2% | **Bearish** (+1,390 bps) |
| Cash flow | Capex incurred, unpaid ($M) | — | — | 29,113 | 10,635 | **Bearish** (forward spend) |
| Capital returns | Buybacks ($M) | 0 | — | **0** | 28,306 | **Bearish** — suspended |
| Capital returns | Dividends ($M) | ~2,689 | ~2,579 | 5,231 | 4,977 | Neutral (+5.1%) |
| Capital returns | Dividends/share (H1) | — | — | $0.43 | $0.41 | Neutral (+4.9%) |
| Balance sheet | Total assets ($M) | 921,983 | — | — | — | **Transformed** (+54.9% in 6M) |
| Balance sheet | Cash + ST investments ($M) | 242,474 | — | — | — | **Bullish** (vs. $126,843 at 12/31/25) |
| Balance sheet | Gross debt ($M) | 101,085 | — | — | — | **Negative** (+106% in 6M) |
| Balance sheet | **Net cash ($M)** | **~142,300** | — | — | — | **Bullish** (still fortress) |
| Balance sheet | Convertible preferred ($M) | 18,023 | 0 | — | — | **Warning** — new senior claim |
| Balance sheet | Deferred tax liabilities ($M) | 22,819 | — | — | — | **Warning** (vs. $919 at 12/31/25) |
| Balance sheet | Shares outstanding (M) | 12,230 | — | — | — | **Negative** (+1.2% in 6M) |
| Balance sheet | Legal/loss accruals ($M) | 17,356 | — | — | — | **Watch** (+11% in 6M) |
| Leverage | Interest expense ($M) | 1,278 | 261 | 1,811 | 295 | **Negative** (+514%) |
| Leverage | Interest coverage (H1 op. income) | — | — | ~44x | ~210x | Still very strong |
| Insider | Transactions | — | — | — | — | **Data unavailable** |

**Bottom line for GOOGL:** the operating business is performing better than at any point in the last several years — 24% revenue growth with 43% incremental margins is a rare combination at this scale. But the 2026 story is now a **capital-intensity story**: negative Q2 FCF, a doubled debt load, no buyback, new preferred and common equity, and a GAAP P&L dominated by a $136B non-cash mark. **Trade the core EPS trajectory (~$10.40 run-rate, ~20% growth), demand evidence that capex converts to revenue by Q3–Q4 2026, and treat any headline P/E as meaningless until the mark either laps or reverses.**