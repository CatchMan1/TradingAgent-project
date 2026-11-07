# GOOGL (Alphabet Inc.) — Fundamental Deep-Dive Report
**Point-in-time analysis as of 2026-07-15** | Primary filing: Q1 2026 Form 10-Q (period ended 2026-03-31, filed 2026-04-30, accn 0001652044-26-000048); FY2025 Form 10-K (filed 2026-02-05, accn 0001652044-26-000018)

---

## 0. Data Availability & Integrity Notes (read first)

| Item | Status |
|---|---|
| Q1 2026 (3mo to 3/31/26) income statement, balance sheet, cash flow | ✅ Full 10-Q detail |
| Q1 2025 comparatives | ✅ Full |
| FY2025 annual cash flow, capital returns, debt, leases, legal accruals (10-K) | ✅ Available |
| FY2023/FY2024 annual cash flow items | ✅ Available |
| Full annual **income statement** history (FY23–FY25 revenue/op income) | ⚠️ Not returned by vendor; Q1-only P&L available |
| Segment revenue / Cloud vs. Search breakout | ⚠️ Not in vendor feed — treated qualitatively |
| Insider transactions | ❌ **DATA_UNAVAILABLE** — no authorized point-in-time archive for GOOGL. No insider activity is inferred or fabricated below. |
| Share price / valuation multiples | ❌ Not in feed — no P/E, EV/EBITDA, or price-target math possible |

---

## 1. Company Profile

Alphabet Inc. is the parent of Google and the world's largest digital advertising business, complemented by cloud infrastructure, subscription/device revenue, and a portfolio of "Other Bets." Segments (qualitative, per company structure — no segment figures in the feed):

- **Google Services** — Search, YouTube ads, Google Network, subscriptions (YouTube Premium/One), Play, devices. Cash engine.
- **Google Cloud** — enterprise infrastructure (TPU/GPU compute), Workspace, AI platform. The growth/margin-inflection story.
- **Other Bets** — early-stage ventures (life sciences, autonomous-adjacent, etc.).
- **Balance-sheet "hidden asset":** non-marketable equity stakes, which revalue through the P&L (cross-referenced in §4) — increasingly material to reported earnings.

---

## 2. Q1 2026 Income Statement — Accelerating Core, Explosive "Other Income"

| $ millions | Q1 2026 | Q1 2025 | YoY |
|---|---:|---:|---:|
| **Revenues** | **109,896** | 90,234 | **+21.8%** |
| Cost of revenue | 41,271 | 36,361 | +13.5% |
| **Gross profit** | **68,625** | 53,873 | **+27.4%** |
| Gross margin | **62.5%** | 59.7% | +280 bps |
| R&D | 17,032 | 13,556 | +25.6% |
| Sales & marketing | 7,606 | 6,172 | +23.2% |
| G&A | 4,291 | 3,539 | +21.2% |
| Total costs & expenses | 70,200 | 59,628 | +17.7% |
| **Operating income** | **39,696** | 30,606 | **+29.7%** |
| Operating margin | **36.1%** | 33.9% | +220 bps |
| Non-operating income (net) | **37,716** | 11,183 | +237% |
| Pre-tax income | 77,412 | 41,789 | +85.2% |
| Tax | 14,834 | 7,249 | — |
| Effective tax rate | **19.2%** | 17.3% | +190 bps |
| **Net income** | **62,578** | 34,540 | **+81.2%** |
| Diluted EPS | **$5.11** | $2.81 | **+81.9%** |
| Diluted shares (implied) | ~12,246M | ~12,292M | −0.4% |
| SBC expense | 7,200 | 5,500 | +30.9% |
| D&A (dep. + amort. + fin-lease) | ~6,886 | ~4,705 | +46% |

**Key read-throughs:**
- **Revenue +21.8% YoY at ~$110B quarterly scale** is a genuine re-acceleration versus Alphabet's historical high-teens growth — the strongest structural bull data point in the file.
- **Gross margin expanded 280 bps** while cost of revenue grew only 13.5% vs. 21.8% revenue growth: infrastructure/TPU efficiency and mix (Cloud scaling) are leveraging. This is *despite* a doubling of capex.
- **Operating leverage on opex:** all three expense lines grew ~21–26%, slightly above revenue, yet operating margin still rose 220 bps because gross margin absorbed it.
- **Interest expense jumped to $533M from $34M** — the direct cost of the new debt program (§6).
- **Effective tax rate up 190 bps to 19.2%** — a headwind to forward EPS versus 2025's ~17% rate; monitor for permanence (OECD Pillar Two/global minimum tax is the likely driver).

---

## 3. Earnings Quality — Strip Out the Investment Gains (critical for traders)

Reported EPS of **$5.11 includes a ~$36.9B pre-tax gain on equity securities** (DebtAndEquitySecuritiesGainLoss = $36,804M vs. $9,960M in Q1 2025; EquitySecuritiesFvNiGainLoss = $36,915M). This is mark-to-market on non-marketable/unlisted stakes — non-recurring in cash terms and highly volatile.

| Core estimate (own calculation) | Q1 2026 | Q1 2025 |
|---|---:|---:|
| Pre-tax income | 77,412 | 41,789 |
| Less: debt & equity securities gains | (36,804) | (9,960) |
| **Adjusted pre-tax income** | **40,608** | 31,829 |
| Tax @ effective rate | 7,797 | 5,508 |
| **Adjusted net income** | **~32,811** | ~26,321 |
| **Adjusted diluted EPS** | **~$2.68** | **~$2.14** |

**Conclusion:** core EPS grew ~**+25% YoY** ($2.14 → $2.68) — excellent, but roughly **half of headline EPS ($5.11) is mark-to-market investment gain, not operations.** Anyone annualizing $5.11 × 4 = $20.44 EPS is over-earning the business by ~2x on a core basis. Conversely, the core $2.68 is *supported by* 36% operating margins and 22% revenue growth, so the underlying trajectory is strong.

Supporting evidence for the "real" nature of the revaluation: **non-marketable equity securities carrying value rose from $64.1B (12/31/25) to $101.3B (3/31/26), +$37.2B in one quarter**, with cumulative upward adjustments jumping from $44.5B to **$80.8B**. This is a genuine, verifiable balance-sheet asset revaluation — AI-ecosystem stakes re-rating — but it is a **one-time step-up in book value, not recurring earnings power.**

---

## 4. Balance Sheet — Fortress, Now Being Levered for AI Capex

| $ millions | 3/31/2026 | 12/31/2025 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 38,063 | 30,708 | +7,355 |
| Cash + short-term investments | **126,840** | 126,843 | ~flat |
| Available-for-sale debt securities | 82,733 | — | — |
| Accounts receivable (net) | 62,999 | 62,886 | +0.2% |
| **Non-marketable equity securities** | **101,346** | 64,094 | **+37,252** |
| Intangibles (net, ex-goodwill) | 9,444 | 1,283 | +8,161 |
| Total current assets | 213,753 | 206,038 | +7,715 |
| **Total assets** | **703,919** | 595,281 | **+108,638 (+18.2%)** |
| Accounts payable | 16,852 | 12,200 | +4,652 |
| Accrued liabilities | 63,019 | 55,557 | +7,462 |
| Deferred revenue (current) | 7,162 | 6,578 | +584 |
| **Total liabilities** | **225,173** | 180,016 | **+45,157 (+25.1%)** |
| **Debt carrying amount** | **80,305** | 49,085 | **+31,220** |
| Finance lease liabilities | 2,214 | 2,500 | −286 |
| Operating lease liabilities | 16,161 | 15,954 | +207 |
| **Shareholders' equity (derived)** | **478,746** | 415,265 | **+63,481 (+15.3%)** |
| Shares outstanding | 12,116M | 12,088M | **+28M** |

**Interpretation:**
- **Net cash position ~$46.5B** (126.8B cash+ST inv − 80.3B debt). Still net-cash positive, but the cushion narrowed materially: debt rose $31.2B in a single quarter and $64.6B of new debt was issued over FY2025.
- **Receivables flat (+$113M) against revenue +21.8%** — exceptional working-capital discipline; implied DSO ≈ 52 days (down sharply). No channel-stuffing signal; allowance for doubtful accounts barely moved ($924M → $962M).
- **Equity +$63.5B in one quarter** = net income $62.6B + SBC $7.2B − dividends $2.5B − AOCI drift; ~$37B of that equity build is the investment revaluation, i.e., not cash.
- **Contingent legal liability:** current loss-contingency accrual **$15.55B** (was $15.59B at YE25; company paid $3.0B in Q3 2025). This is a large, real, near-term cash/accrual overhang tied to regulatory/antitrust matters — a persistent risk item, not a one-off.
- **Deferred tax assets net collapsed $9.1B → $2.0B** — consistent with the investment step-up creating offsetting deferred tax liabilities, and with $6.9B of deferred taxes flowing through the Q1 cash-tax line.

---

## 5. Cash Flow — The Single Most Important Chart in This File

| $ millions | Q1 2026 | Q1 2025 | YoY |
|---|---:|---:|---:|
| **Operating cash flow** | **45,790** | 36,150 | **+26.7%** |
| Capex (PP&E purchases) | **35,674** | 17,197 | **+107.5%** |
| **Free cash flow (OCF − capex)** | **10,116** | 18,953 | **−46.6%** |
| Capex / revenue | **32.5%** | 19.1% | +1,340 bps |
| Investing cash flow | −63,389 | −16,194 | — |
| Financing cash flow | **+25,077** | −20,201 | swing |
| Dividends paid | 2,542 | 2,434 | +4.4% |
| **Buybacks** | **0** | 15,068 | **−100%** |
| Debt issued (net of costs) | 31,379 | 4,532 | — |
| Minority proceeds | 3,200 | 400 | — |

**Multi-year annual (10-K facts):**

| $ millions | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Operating cash flow | 101,746 | 125,299 | **164,713** |
| Capex | 32,251 | 52,535 | **91,447** |
| **Free cash flow** | **69,495** | **72,764** | **73,266** |
| Buybacks | 61,504 | 62,222 | **45,709** |
| Dividends | 0 | 7,363 | **10,049** |
| Financing cash flow | −72,093 | −79,733 | −37,388 |
| Investing cash flow | −27,063 | −45,536 | −120,291 |
| Debt issued (net) | 10,790 | 13,589 | **64,564** |
| Debt repaid | 11,550 | 12,701 | 32,427 |

**The trade in one sentence:** Alphabet's **FCF has been essentially flat for three years ($69.5B → $72.8B → $73.3B)** while capex nearly **tripled** ($32.3B → $91.4B) and OCF grew **+62%** ($101.7B → $164.7B). Operating cash generation is superb and accelerating, but it is now almost entirely consumed by the AI datacenter build.

**Three signals that matter most:**
1. **Capex intensity is now a thesis-defining variable.** Q1 2026 capex/revenue of 32.5% implies a ~$140B+ annualized run-rate. Additionally, **capex incurred but not yet paid** ballooned to **$24.1B vs $11.4B a year ago** (FY25: $15.1B) — meaning reported capex *understates* the true near-term cash drain and will pressure Q2/Q3 FCF.
2. **Q1 FCF halved YoY to $10.1B.** If FY2026 maintains this pattern, full-year FCF could print **below** FY2025's $73.3B for the first time in the AI era — a genuine re-rating risk for a stock historically valued on FCF.
3. **Buybacks went to exactly zero in Q1 2026** (vs. $15.1B in Q1 2025; $45.7B FY2025, $62.2B FY2024). Combined with a **net +28M share count increase**, this is the clearest management signal in the dataset: **capital allocation has pivoted from shareholder returns to infrastructure + debt-funded buildout.** Expect buyback resumption to be the key "relief" catalyst; expect continued absence to be read as capex crowding out returns.

**Depreciation cross-check:** quarterly depreciation $6.48B (+44% YoY) against a ~$140B annualized capex run-rate implies D&A will compound aggressively for 4–8 quarters — a structural **margin headwind** in FY2027+ even if gross margin holds today.

---

## 6. Financing, Leases & Maturity Profile (from FY2025 10-K)

- **Debt maturities** (as of 12/31/25): $2.0B next 12M, $1.0B Y2, $2.68B Y3, $1.76B Y4, $5.5B Y5, **$36.1B after Y5** — a well-laddered profile with no refinancing cliff. Very low near-term rollover risk.
- **Operating lease payments due:** $18.8B total ($3.2B within 12M), discounted at 3.7% — modest relative to $478B equity.
- **Finance lease payments due:** $2.64B total — immaterial.
- **Interest expense trajectory:** $533M in Q1 2026 (~$2.1B annualized) vs. $34M in Q1 2025. Rising but still trivial versus $39.7B quarterly operating income (~1.3% of op income).
- **Contract liabilities / deferred revenue:** $9.8B total (current $7.2B), up 14% YoY — modest, reflecting that most ad revenue is billed in arrears; **$3.5B of Q1 revenue was recognized from prior-period deferred balances**, a slight quality-of-revenue watch item (4.5% of Q1 revenue from the backlog draw).

---

## 7. Forward Visibility — RPO $467.6B

**Remaining performance obligations = $467.6B at 3/31/2026.** This is the largest forward-revenue indicator in the filing set — a multi-year contracted backlog (predominantly enterprise/Cloud commitments). It is roughly **4.3x annualized Q1 revenue** and represents an extremely strong multi-year revenue floor. However: (a) no prior-period comparison was returned, so we cannot measure RPO *growth*, and (b) the segment mix (Cloud vs. other) is not disclosed in the feed. Treat as a strong directional positive, unquantified on trend.

---

## 8. Insider Transactions

**DATA_UNAVAILABLE.** The vendor data package contains no authorized, point-in-time insider-transactions archive for GOOGL as of 2026-07-15. **No insider buying or selling is inferred, estimated, or fabricated.** Any prior reporting on Alphabet insider activity should be verified independently before use in a trading decision. This is a genuine information gap in this report and should be flagged as such when weighing sentiment.

---

## 9. Risk Register & Catalysts

**Structural positives**
1. Revenue re-accelerated to **+21.8% YoY** at $110B/quarter — AI monetization appears to be *adding* to, not cannibalizing, the core.
2. **Gross margin +280 bps to 62.5%** — the capex is generating efficiency, not just expense.
3. **Operating margin 36.1%**, up 220 bps despite triple-digit capex growth.
4. **$467.6B RPO** and **net cash ~$46.5B** — deep multi-year visibility and a still-unbroken balance sheet.
5. Core EPS **+25% YoY** ($2.14 → $2.68) even ex-investment gains.

**Risks to underwrite**
1. **FCF compression** — Q1 FCF −46.6% YoY; capex guide is the swing factor. Flat-to-down FY26 FCF is now a live scenario.
2. **Earnings quality** — ~48% of Q1 net income came from investment markups. A single down quarter in AI-ecosystem valuations could invert this to a *loss-making* other-income line.
3. **Buyback halt + rising share count** — removes the EPS tailwind and signals capex prioritization; watch Q2 10-Q repurchase line closely.
4. **Leverage ramp** — debt +$31.2B in one quarter to $80.3B; FY25 issuance $64.6B. Fine for now, but it is a directional change in capital structure.
5. **Legal/regulatory accrual of $15.55B** plus antitrust overhang — persistent cash calls.
6. **Tax rate 19.2% vs 17.3%** — a ~200 bps EPS headwind likely to persist.
7. **D&A cliff** — 44% YoY depreciation growth with $140B+ capex will compress margins in FY2027+.

**Catalyst calendar:** Q1 was filed 2026-04-30; **Q2 2026 results are due imminently (late July 2026)**, i.e., within days of this report's date. The two numbers that will decide the tape are **(1) capex guidance and (2) the Q2 buyback line**, followed by Cloud revenue growth and any further investment-gain marks.

---

## 10. Actionable Takeaways (evidence-linked)

1. **Anchor on core, not headline, EPS.** ~$2.68 of core EPS (Q1 2026) is the right annualization base; $5.11 overstates recurring earnings by ~2x. **Buy the core growth (+25%), fade anyone extrapolating the headline (+82%).**
2. **The FCF story is the swing factor for the multiple.** Watch whether OCF growth (+26.7%) can continue to outrun capex growth (+107%). If capex/revenue stabilizes below ~30%, FCF re-accelerates sharply in FY27. If it grinds above ~35%, expect multiple compression regardless of revenue strength.
3. **Treat the buyback halt as a medium-term negative for EPS per share, and a resumption as a positive catalyst.** Zero repurchases plus +28M shares = the per-share compounding machine is paused.
4. **The $15.55B legal accrual and 19.2% tax rate are persistent, quantifiable drags** — bake both into any FY26–FY27 model rather than treating them as one-offs.
5. **The $101.3B non-marketable equity book is a real, if lumpy, asset.** It adds $37.2B of value in a single quarter and is now ~14% of total assets — an upside option, but a source of earnings noise that will confuse headline comparisons quarterly.
6. **Pre-earnings positioning (late July):** fundamentals into the print are strong on revenue margin and weak on FCF/capex. Risk is asymmetric *if* capex guidance is raised again; reward is asymmetric if management signals capex plateau plus buyback resumption.

---

## 11. Key-Points Summary Table

| Category | Metric | Q1 2026 | Q1 2025 | Δ / Note |
|---|---|---:|---:|---|
| **Scale** | Revenue ($M) | 109,896 | 90,234 | **+21.8% YoY** |
| **Profitability** | Gross margin | 62.5% | 59.7% | +280 bps ✅ |
| | Operating income ($M) | 39,696 | 30,606 | +29.7% ✅ |
| | Operating margin | 36.1% | 33.9% | +220 bps ✅ |
| | Net income ($M) | 62,578 | 34,540 | +81.2% (inflated) |
| | Diluted EPS | $5.11 | $2.81 | +81.9% (inflated) |
| | **Core EPS (ex-investment gains, est.)** | **~$2.68** | **~$2.14** | **+25% — the real run-rate** |
| **Earnings quality** | Equity securities gain ($M) | 36,804 | 9,960 | ~48% of net income ⚠️ |
| | SBC ($M) | 7,200 | 5,500 | 6.6% of revenue ⚠️ |
| **Cash generation** | Operating cash flow ($M) | 45,790 | 36,150 | +26.7% ✅ |
| | Capex ($M) | 35,674 | 17,197 | **+107.5%** |
| | **Free cash flow ($M)** | **10,116** | **18,953** | **−46.6% ❌** |
| | Capex / revenue | 32.5% | 19.1% | +1,340 bps ⚠️ |
| | Capex incurred, unpaid ($M) | 24,131 | 11,388 | future FCF drag |
| **Balance sheet** | Cash + ST investments ($M) | 126,840 | — | ~flat vs YE25 |
| | Total debt ($M) | 80,305 | — | **+$31,220M in one quarter** |
| | Net cash ($M) | ~46,535 | — | still positive ✅ |
| | Non-marketable equities ($M) | 101,346 | — | +$37,252M vs YE25 |
| | Total assets ($M) | 703,919 | — | +18.2% vs YE25 |
| | Total liabilities ($M) | 225,173 | — | +25.1% vs YE25 |
| | Shareholders' equity ($M) | 478,746 | — | +15.3% vs YE25 |
| | Loss contingency (current, $M) | 15,551 | — | legal/regulatory overhang ⚠️ |
| | RPO ($M) | 467,600 | — | ~4.3x annualized revenue ✅ |
| **Capital returns** | Buybacks ($M) | **0** | 15,068 | **halted ❌** |
| | Dividends ($M) | 2,542 | 2,434 | $0.21/sh, +5% |
| | Shares outstanding | 12,116M | — | +28M vs YE25 ⚠️ |
| **FY2025 annual** | Operating cash flow | $164,713M | FY24: $125,299M | +31.5% |
| | Capex | $91,447M | FY24: $52,535M | +74% |
| | **Free cash flow** | **$73,266M** | FY24: $72,764M | **~flat 3 yrs** |
| | Buybacks / dividends | $45,709M / $10,049M | FY24: $62,222M / $7,363M | mix shift to dividends |
| **Rates/tax** | Effective tax rate | 19.2% | 17.3% | +190 bps headwind |
| | Interest expense ($M) | 533 | 34 | debt ramp cost |
| **Insider** | Insider transactions | — | — | **DATA_UNAVAILABLE — not inferable** |

**Bottom line:** GOOGL's Q1 2026 is a **two-sided print** — best-in-class revenue acceleration (+21.8%), expanding gross and operating margins, a fortress balance sheet with $46.5B net cash and $467.6B in contracted backlog — against **halved free cash flow, a doubling of capex, a $31B one-quarter debt raise, a suspended buyback, and roughly half of reported EPS coming from non-cash investment markups.** The core franchise is stronger than the headline suggests on quality-adjusted revenue/margin, and weaker than the headline suggests on cash. Trade the core (+25% EPS growth) and the capital-allocation pivot (zero buybacks), not the $5.11 headline.