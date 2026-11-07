# GOOGL — Alphabet Inc. | Fundamental Deep-Dive
**As of 2026-08-18 | Point-in-time SEC facts (latest 10-Q accepted 2026-07-23 for Q2-2026; latest 10-K accepted 2026-02-05 for FY2025)**

---

## 0. Data provenance & caveats (read first)

| Item | Status |
|---|---|
| Source | Vendor's point-in-time SEC XBRL fact cache, filtered by **actual EDGAR acceptance time** (no look-ahead) |
| Latest period | Q2-2026 (quarter ended 2026-06-30), 10-Q filed 2026-07-23 |
| Prior full year | FY2025 (10-K filed 2026-02-05) |
| **Revenue tag** | Not returned by the vendor (output truncated). Revenue below is **derived = CostsAndExpenses + OperatingIncomeLoss**, both of which *are* vendor-reported. Derived figures are labeled "d." |
| Not returned | R&D line, Sales & Marketing line, PP&E, Goodwill, Total equity, long-term investments, segment revenue |
| **Insider transactions** | `DATA_UNAVAILABLE` — no authorized point-in-time insider archive for GOOGL. **No insider activity is inferred or fabricated in this report.** |

---

## 1. Company profile

**Alphabet Inc. (GOOGL)** — the parent of Google. Operating structure (as reflected in the reported cost/expense geometry and contract-liability, backlog and lease disclosures): Google Services (Search/Ads, YouTube, Android, Chrome, Play, Maps, subscriptions/devices), Google Cloud (infrastructure + AI platforms + Workspace), and Other Bets (early-stage ventures). The balance sheet and cash-flow data show Alphabet in **an exceptionally capital-intensive build-out phase**: H1-2026 capex of $80.6B, operating-lease commitments of $21.3B, growing finance leases ($2.6B), and a large, appreciating portfolio of **non-marketable equity investments** ($124.3B at fair value).

---

## 2. Income statement — revenue re-acceleration and margin expansion

### 2.1 Derived revenue and profit (USD millions)

| Period | Revenue (d.) | Cost of revenue | Gross profit (d.) | Gross margin | Operating income | **Op. margin** | Pre-tax income | Net income | Diluted EPS |
|---|---|---|---|---|---|---|---|---|---|
| Q2-2024 | 88,268 | 36,474 | 51,794 | 58.7% | 28,521 | 32.3% | 31,706 | 26,301 | $2.12 |
| Q3-2024 | 88,268* | 36,474* | — | — | — | — | — | — | — |
| Q3-2025 | 102,346 | 41,369 | 60,977 | 59.6% | 31,228 | 30.5% | 43,987 | 34,979 | $2.87 |
| Q1-2025 | 90,234 | 36,361 | 53,873 | 59.7% | 30,606 | 33.9% | 41,735 | 34,540 | $2.81 |
| **Q2-2025** | 96,428 | 39,039 | 57,389 | 59.5% | 31,271 | 32.4% | 33,933 | 28,196 | $2.31 |
| **Q1-2026** | **109,896** | 41,271 | 68,625 | 62.4% | 39,696 | 36.1% | 77,412 | 62,578 | $5.13 |
| **Q2-2026** | **119,796** | 45,943 | 73,853 | **61.7%** | 40,770 | **34.0%** | 138,753 | 112,193 | **$9.11** |
| **H1-2025** | 186,662 | 75,400 | 111,262 | 59.6% | 61,877 | 33.1% | 75,722 | 62,736 | $5.12 |
| **H1-2026** | **229,692** | 87,214 | 142,478 | **62.0%** | 80,466 | **35.0%** | 216,165 | 174,771 | **$14.24** |
| 9M-2024 | 253,549 | 105,693 | 147,856 | 58.3% | 81,418 | 32.1% | 87,572 | 73,582 | $5.90 |
| 9M-2025 | 289,007 | 116,768 | 172,239 | 59.6% | 93,105 | 32.2% | 119,709 | 97,715 | $7.99 |

\*Q3-2024 shown as the same 3-month stub used for the 9M comparison; only the 9M figure is directly vendor-reported for 2024. All 2026 quarterly revenue figures are **derived**, not vendor line items.

**Full-year anchors (vendor-reported where noted):**

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Cost of revenue | 133,332 | 146,306 | 162,535 |
| Total costs & expenses | 223,101 | 237,628 | 273,797 |
| SBC (expense) | 22,100 | 22,800 | **27,100** |
| Effective tax rate | 13.9% | 16.4% | 16.8% |
| Diluted EPS | $5.80 | $8.04 | **$10.81** |
| Comprehensive income | 76,996 | 99,720 | 135,054 |
| Equity FV-NI gains (net) | 392 | 3,714 | 24,080 |
| Debt & equity securities gains | (823) | 2,671 | 24,620 |
| SBC tax benefit | 4,500 | 4,600 | 5,000 |

### 2.2 What actually drove Q2/H1 2026

1. **Revenue growth accelerated sharply**: Q2-2026 +24.2% y/y (vs +9.3% in Q2-2025 and +16.0% in Q3-2025). H1-2026 +23.0% y/y. Two-year CAGR from Q2-2024 is ~16.5%/yr. This is the single most important fundamental datapoint in the file — Alphabet has re-accelerated, not decelerated.
2. **Gross-margin expansion is the operating story.** Cost of revenue grew only **+15.7% y/y** in H1-2026 ($87.2B vs $75.4B) against +23.0% revenue → gross margin 62.0% vs 59.6% (+240bp). Inference: traffic-acquisition/content/other cost-of-sales leverage more than offset AI compute depreciation in the period.
3. **Opex is growing faster than revenue.** Non-cost-of-revenue, non-G&A spend (R&D + S&M, derived residual) = **$51.3B in H1-2026 vs $40.6B H1-2025, +26.2%**. G&A rose +22.9% ($10.75B vs $8.75B). SBC rose **+32.2%** ($15.2B vs $11.5B; Q2 alone $8.0B). Trailing-12-month SBC ≈ **$30.8B** — a genuine, persistent dilution cost.
4. **Operating margin still expanded**: 35.0% H1-2026 vs 33.1% H1-2025. Ex-SBC operating margin = **41.6%** (H1-2026).
5. **Tax rate stepped up**: 19.1% in both Q1 and Q2-2026 vs 17.1% in H1-2025. Partly non-cash: the cash-flow statement shows a **$27.5B deferred-tax add-back**, implying cash taxes of only ~$13.9B on $216.2B pre-tax (≈6.4% cash rate) — the mark-to-market gains book a deferred tax liability (DTL rose to **$22.8B** from $0.9B) without a cash payment.

### 2.3 ⚠️ Earnings quality — the critical caveat

| H1-2026 | USD mn | % of pre-tax |
|---|---|---|
| Pre-tax income | 216,165 | 100% |
| **Operating income (core)** | **80,466** | **37.2%** |
| **Non-operating income** | **135,699** | **62.8%** |
| — of which equity securities FV-NI gain | 135,946 | 62.9% |
| — of which unrealized (mark-to-market) | 21,531 | 10.0%* |
| — interest income / (expense) | 2,811 / (1,811) | — |

Q2-2026 alone: non-operating income was **70.6% of pre-tax income** ($97,983 of $138,753).

**Read-through: ~63% of H1-2026 EPS is non-cash, mark-to-market appreciation on the investment portfolio, not operating profit.** Core (operating) EPS power is far lower than the $14.24 headline. Extrapolating the $9.11 Q2 headline EPS into a valuation multiple would badly misprice GOOGL. This is the #1 analytical trap in these filings.

---

## 3. Balance sheet — asset base up 55% in six months

| USD mn | 2024-12-31 | 2025-12-31 | **2026-06-30** | Δ YTD |
|---|---|---|---|---|
| Cash & equivalents | 23,466 | 30,708 | **55,911** | +25,203 |
| Cash + short-term investments | 95,657 | 126,843 | **242,474** | **+115,631** |
| Accounts receivable, net | 52,340 | 62,886 | 69,175 | +6,289 |
| **Current assets** | 163,711 | 206,038 | **343,524** | **+137,486** |
| **Total assets** | **450,256** | **595,281** | **921,983** | **+326,702 (+54.9%)** |
| Accounts payable | 7,987 | 12,200 | 20,258 | +8,058 |
| Accrued liabilities | 51,228 | 55,557 | **73,014** | +17,457 |
| Employee-related liabilities | 15,069 | 17,546 | 15,086 | −2,460 |
| Accrued income taxes (current) | 2,905 | 523 | 5,233 | +4,710 |
| Contract liabilities (current) | 5,036 | 6,578 | 7,154 | +576 |
| **Legal / loss contingency accrual (current)** | 6,322 | 15,594 | **17,356** | +1,762 |
| Short/long-term debt (carrying) | 12,000 | 49,085 | **101,085** | **+52,000** |
| Finance lease liabilities | 1,677 | 2,500 | 2,590 | +90 |
| Operating lease liabilities | 14,578 | 15,954 | 18,037 | +2,083 |
| **Convertible preferred stock** | 0 | 0 | **18,023** | **+18,023** |
| Common stock + APIC | 84,800 | 93,126 | **131,371** | +38,245 |
| AOCI | (4,800) | (1,916) | (2,285) | −369 |
| Shares outstanding | 12.211 B | 12.088 B | **12.230 B** | **+142 M (+1.2%)** |

**Key balance-sheet observations**

- **The $327B asset increase is not capex alone.** It is driven by: (a) +$115.6B of cash & short-term investments, (b) a step-change in the private-mark portfolio, and (c) capitalized AI infrastructure (PP&E; the specific tag was truncated).
- **Equity securities without a readily determinable fair value: $124,259M, up from $64,094M at 2025-12-31 (+94%).** Cumulative *upward* adjustments on those holdings jumped to **$85,732M** (from $44,485M); cumulative downward adjustments only $9,115M. This is the source of the non-operating gain line — a seriously large, hard-to-verify, model-marked asset (≈13.5% of total assets). Cumulative upward marks of $85.7B vs a cost basis implying roughly $47.6B → the book is marked at ~2.6x cumulative cost.
- **Investing outflows exploded**: purchases of "other investments" (private/venture) **$22,051M in H1-2026 vs $2,312M in H1-2025 (9.5x)**; marketable securities purchases $76,480M vs $39,870M. Alphabet is both *marking up* and *adding to* the private book.
- **Leverage regime change**: debt carrying value **doubled to $101.1B** (from $49.1B; from just $12.0B at end-2024). H1-2026 gross debt issuance **$56,226M** vs $31,378M in all of H1-2025; only $5,253M repaid. Interest expense ran at **$1,278M in Q2-2026 vs $261M in Q2-2025 (~5x)** — annualizing ~$5B; that drag is only now ramping.
- **Dilution via three channels**: (i) +142M shares issued for **$30,499M** cash (≈$215/share implied) — buybacks were **$0** in H1-2026 vs $28,306M in H1-2025; (ii) **$19,063M of convertible preferred** issued in June-2026 ($19.0B on 2026-06-05, carrying $18,023M), with $86M of preferred dividends already paid in Q2; (iii) **$3,758M from minority shareholders** (JV/NCI structures — NCI now shares in subsidiary economics).
- **Liquidity is still overwhelming**: cash + short-term investments $242.5B vs total debt + leases of ~$121.7B → **net cash ≈ +$121B** before counting $99.5B of available-for-sale debt securities and the long-term equity book.
- **Available-for-sale debt portfolio** grew to $99,500M ($16.7B ≤1yr / $50.9B 1–5yr / $15.3B 5–10yr / $16.6B >10yr). Mild unrealized losses: $416M on $53.2B in a loss position — well contained; $150M of that is >12 months. No credit deterioration signal ($39M allowance provision).
- **Legal overhang is real**: current loss-contingency accruals of **$17.4B** (up from $6.3B at end-2024), and FY2025 cash flow shows a $3.0B contingency payment in Q3-2025 — consistent with major regulatory/antitrust settlements. Treat as a recurring, not one-time, cash drag.

---

## 4. Cash flow — the FCF inflection is the real story

| USD mn | H1-2025 | **H1-2026** | Δ |
|---|---|---|---|
| Operating cash flow | 63,897 | **84,859** | +32.8% |
| Capex (cash, PP&E) | (39,643) | **(80,598)** | **+103.3%** |
| **Free cash flow (d.)** | **24,254** | **4,261** | **−82.4%** |
| Capex / OCF | 62% | **95%** | — |
| Capex / revenue (d.) | 21.2% | **35.1%** | +1,390bp |
| Purchases of marketable securities | (39,870) | (76,480) | +91.8% |
| Purchases of other investments | (2,312) | **(22,051)** | +853% |
| Acquisitions/other investing (net) | +363 | +1,359 | — |
| **Investing cash flow** | (40,738) | **(145,822)** | — |
| Debt issued (net of costs) | 31,378 | **56,226** | +79% |
| Debt repaid | (18,397) | (5,253) | — |
| Common stock issued | 0 | **30,499** | ∞ |
| Convertible preferred issued | 0 | **19,063** | ∞ |
| Minority interest proceeds | 400 | 3,758 | +840% |
| **Buybacks** | **(28,306)** | **0** | **halted** |
| Dividends paid | (4,977) | (5,231) | +5.1% |
| **Financing cash flow** | **(26,033)** | **+86,320** | swing of +$112.4B |
| D&A: depreciation | 9,485 | 13,586 | +43.2% |
| SBC | 11,500 | 15,200 | +32.2% |
| Deferred taxes (non-cash) | (1,596) | +27,538 | — |
| Capex incurred but **unpaid** (balance) | 10,635 | **29,113** | +174% |

**Quarterly split (derived):**

| | Q1-2025 | Q2-2025 | Q1-2026 | **Q2-2026** |
|---|---|---|---|---|
| OCF | 36,150 | 27,747 | 45,790 | **39,069** |
| Capex | (17,197) | (22,446) | (35,674) | **(44,924)** |
| **FCF (d.)** | **18,953** | **5,301** | **10,116** | **(5,855)** |

**The single most important flow-of-funds fact: Q2-2026 free cash flow was NEGATIVE (~−$5.9B), the first negative quarter in the dataset.** Annualized capex run-rate ≈ $161B (and *true* capex is higher still: $29.1B of capex was incurred but unpaid at 6/30/26, vs $10.6B a year earlier). The entire financing story follows mechanically: **buybacks to zero → $56B of debt → $30.5B of equity → $19.1B of convertible preferred → $3.8B of minority capital.** Alphabet has flipped from a net returner of capital to a net raiser.

**Depreciation lag risk**: depreciation is only **+43% y/y** while capex is +103%. Depreciation/revenue is 5.9% today. As the ~$80B+/half-year of AI infrastructure enters service, D&A will climb materially for several quarters — a structural headwind to the currently expanding operating margin, independent of revenue.

---

## 5. Insider transactions

**Unavailable.** The vendor's insider-transactions archive has no authorized, point-in-time coverage for GOOGL as of 2026-08-18. I am explicitly **not** inferring insider buying or selling from the share-count, SBC, or preferred-issuance data, and no directional insider signal should be assumed in any trade decision from this report. (Note only, from the cap table itself: shares outstanding *rose* 1.2% in H1-2026, the opposite of the FY2023–FY2025 pattern of net shrinkage — an objective dilution fact, not an insider view.)

---

## 6. Fundamental scorecard

**Strengths**
1. Revenue growth inflected to **+23–24% y/y** (Q2-2026 +24.2%) — the fastest in the dataset.
2. **Gross margin 62.0%** (+240bp y/y) and **operating margin 35.0%** (+190bp y/y) despite an aggressive AI spend cycle; ex-SBC operating margin 41.6%.
3. Net cash ~**+$121B** plus $99.5B of AFS securities — no solvency or refinancing risk whatsoever; funded the entire build-out while still paying dividends.
4. **$124.3B** of private equity holdings marked at 2.6x cumulative cost — a large, under-appreciated (but model-dependent) asset-value cushion.
5. OCF +32.8% y/y — the core franchise is generating more cash than ever.

**Weaknesses / risks**
1. **Earnings quality**: ~63% of H1-2026 pre-tax income is mark-to-market investment gains. Core operating EPS power is a fraction of the $14.24 headline. Any private-market or AI-valuation reset hits reported EPS directly.
2. **FCF compression**: H1 FCF −82% y/y; **Q2-2026 FCF negative**. Capex at 35% of revenue and rising, plus $29.1B of accrued-but-unpaid capex.
3. **Capital-structure reversal**: debt doubled to $101B, $19.1B preferred with a dividend, +142M shares, $3.8B NCI, buyback to zero — while the company also spent $22.1B on new private investments. Three-way demands on capital simultaneously.
4. **Depreciation step-up** still ahead of the P&L; interest expense up ~5x y/y.
5. **DTL of $22.8B** on unrealized gains: the low (6.4%) cash tax rate is a deferral, not a permanent benefit.
6. **Legal**: $17.4B of current contingency accruals (rising).

---

## 7. Actionable trading implications

**Bias: constructive on the operating business, neutral-to-negative on headline EPS optics. Trade the operating franchise; discount the investment marks.**

1. **Do not value GOOGL on the $14.24 H1 / $9.11 Q2 EPS.** Use core operating EPS: H1-2026 operating income $80.47B, after-tax at the 19.1% rate ≈ **$65.1B**, or ≈ **$5.30/share** for H1 (vs $2.58 in H1-2025, **+105% y/y**). Even ex-marks, core earnings roughly doubled — that is the real, defensible growth number and it supports a structurally higher multiple than the FY2025 $10.81 reported EPS implies.
2. **The quarterly EPS print is now hostage to private-market marks.** Expect ±$4–6 of quarterly EPS noise purely from revaluation of the $124B non-marketable book and the $99.5B AFS portfolio. Consequence: **elevated realized volatility around earnings dates, high dispersion vs consensus** (consensus models cannot see the private marks). Options sellers are structurally advantaged on elevated implied vol; but be aware of gap risk in either direction.
3. **Watch the FCF trajectory as the primary bear catalyst.** If Q3-2026 FCF is again negative, expect the market to re-rate the "AI capex supercycle" narrative and to pressure the multiple on diminishing buyback support (buyback = $0 removes a persistent bid). Concrete triggers to monitor in the Q3-2026 10-Q (expected ~late Oct 2026): capex ≥$45B/quarter, capex-incurred-but-unpaid >$29B, further equity/preferred issuance, or NCI proceeds.
4. **Conversely, resumption of buybacks is the cleanest bullish tell.** Buybacks were $15.1B (Q1-2025) and $13.2B (Q2-2025) before going to zero. Any re-authorization/re-start, alongside capex plateauing below ~$40B/quarter, would signal management believes the infra build is peaking — historically a strong positive inflection for the stock.
5. **Asymmetry from the investment book cuts both ways, but with a floor.** Downside: the $85.7B of cumulative upward marks are the mark-to-market cushion — a 30% haircut on the $124B book would cost ~$37B pre-tax (~$2.6/share, one-off). Upside: continued private-AI revaluations have already delivered $136B of H1 gains; another strong revaluation quarter could produce another double-digit EPS beat. Position sizing should reflect that you are long a **levered option on private AI valuations** in addition to the ad/cloud franchise.
6. **Credit is not a concern but is now a factor.** Gross debt $101B + preferred $19B vs $242B cash + $99.5B AFS. Net cash remains ~$121B+; the company can fund capex internally *and* pay the preferred dividend. No credit-driven thesis. But note interest expense run-rate ~$5B/yr rising — a small, growing EPS headwind (≈$0.30–0.40/share annually).
7. **Dividend**: $0.22/quarter (from $0.21), i.e. ~$0.88 annualized, +4.8% y/y. Yield is immaterial (~0.4% at the ~$215 implied issuance price); it is a signaling device, not an income vehicle. Dividend growth is safe (only $5.2B/half vs $84.9B OCF).
8. **Asymmetry check / falsifiers.** The bull case breaks if (a) revenue growth decelerates back below ~15% while capex stays >30% of revenue, or (b) the private book is written down materially. The bear case breaks if gross margin holds >60% and operating margin stays >34% for two more quarters — which is exactly what H1-2026 shows.

---

## 8. Key metrics summary table

| Category | Metric | Value | Period | Signal |
|---|---|---|---|---|
| **Growth** | Revenue (derived) | $229.69B | H1-2026 | +23.0% y/y |
| | Revenue (derived) | $119.80B | Q2-2026 | **+24.2% y/y** (vs +9.3% Q2-2025) — acceleration |
| | Cost of revenue | $87.21B | H1-2026 | +15.7% y/y → COGS leverage |
| **Margins** | Gross margin | 62.0% | H1-2026 | +240bp y/y |
| | Operating margin | 35.0% | H1-2026 | +190bp y/y |
| | Ex-SBC operating margin | 41.6% | H1-2026 | — |
| | G&A | $10.75B | H1-2026 | +22.9% y/y |
| | SBC | $15.2B (Q2 $8.0B) | H1-2026 | **+32.2% y/y**; TTM ≈$30.8B |
| **Earnings** | Operating income | $80.47B | H1-2026 | +30.0% y/y (core) |
| | Non-operating income | $135.70B | H1-2026 | **62.8% of pre-tax — marks** |
| | Equity FV-NI gain | $135.95B | H1-2026 | non-cash |
| | Pre-tax income | $216.17B | H1-2026 | +185% y/y |
| | Net income | $174.77B | H1-2026 | +178% y/y |
| | Diluted EPS | $14.24 (Q2 $9.11) | H1-2026 | vs $5.12 (Q2 $2.31) |
| | Core EPS est. (ex-marks) | ≈$5.30 | H1-2026 | vs ≈$2.58 → **+105% y/y** |
| | Effective tax rate | 19.1% | Q1/Q2-2026 | up from 17.1% |
| | Cash tax rate implied | ≈6.4% | H1-2026 | DTL-driven, non-permanent |
| **Cash flow** | Operating cash flow | $84.86B | H1-2026 | +32.8% y/y |
| | Capex | $80.60B | H1-2026 | **+103% y/y; 35.1% of revenue** |
| | Free cash flow (derived) | $4.26B | H1-2026 | **−82.4% y/y** |
| | Free cash flow (derived) | **−$5.86B** | Q2-2026 | **first negative quarter** |
| | Capex incurred but unpaid | $29.11B | 2026-06-30 | vs $10.64B — true capex higher |
| | Depreciation | $13.59B | H1-2026 | +43% (lags +103% capex) |
| **Balance sheet** | Total assets | $921.98B | 2026-06-30 | **+54.9% in 6 months** |
| | Cash + ST investments | $242.47B | 2026-06-30 | +$115.6B YTD |
| | AFS debt securities | $99.50B | 2026-06-30 | unrealized loss only $416M |
| | Equity sec. w/o RDFV (private book) | $124.26B | 2026-06-30 | **+94% YTD**; cumulative +$85.7B marks |
| | Total debt + leases | ≈$121.7B | 2026-06-30 | debt carrying **$101.1B (+$52.0B YTD)** |
| | Convertible preferred | $18.02B | 2026-06-30 | issued 2026-06-05 ($19.0B) |
| | Net cash (cash+ST inv − debt/leases) | ≈**+$121B** | 2026-06-30 | fortress |
| | Shares outstanding | 12.230B | 2026-06-30 | **+1.2% YTD (dilution)** |
| | Legal contingency accrual (current) | $17.36B | 2026-06-30 | rising legal drag |
| **Capital allocation** | Buybacks | **$0** | H1-2026 | vs $28.31B H1-2025 — **halted** |
| | Common stock issued | $30.50B | H1-2026 | ~$215/sh implied |
| | Debt issued / repaid | $56.23B / $5.25B | H1-2026 | leverage regime change |
| | Private/other investments | $22.05B | H1-2026 | 9.5x y/y |
| | Dividends per share | $0.22/qtr ($0.43 H1) | Q2-2026 | +4.8% y/y |
| | Financing cash flow | **+$86.32B** | H1-2026 | vs −$26.03B — $112B swing |
| **History** | Diluted EPS | $5.80 → $8.04 → $10.81 | FY23→FY25 | ~37% CAGR |
| | SBC | $22.1B → $22.8B → $27.1B | FY23→FY25 | accelerating |
| | Effective tax rate | 13.9% → 16.4% → 16.8% | FY23→FY25 | rising |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | — | no signal; not inferred |

---

### Bottom line for traders
GOOGL's **operating** engine is the strongest it has been in the dataset: 24% revenue growth, 62% gross margin, 35% operating margin, +30% core operating income, and $85B of half-year operating cash flow against a $121B net-cash balance sheet. But the **reported** numbers are now dominated by non-cash private-market marks (63% of pre-tax income), **free cash flow has collapsed to zero (−$5.9B in Q2-2026)**, and the company has flipped from buying back $28B of stock per half-year to raising $56B of debt, $30B of equity and $19B of convertible preferred in a single half-year. Trade the core franchise on operating income; treat the investment marks as an embedded, high-variance option; and make Q3-2026 capex and any buyback restart the two decision triggers.