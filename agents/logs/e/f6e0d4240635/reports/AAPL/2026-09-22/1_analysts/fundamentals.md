# AAPL — Fundamental Deep Dive
**Analysis date:** 2026-09-22 · **Latest reported period:** fiscal Q3 FY2026, 13 weeks ended 2026-06-27 (10-Q accepted 2026-07-31) · **Currency:** USD

---

## 1. Data provenance and limitations (read first)

| Item | Status |
|---|---|
| Source | Point-in-time SEC facts, filtered by actual EDGAR acceptance timestamp ≤ 2026-09-22 |
| Latest filing in slice | 10-Q for period ended 2026-06-27, filed/accepted 2026-07-31 (`0000320193-26-000020`) |
| Prior FY26 filings in slice | Q2 FY26 10-Q (period end 2026-03-28, filed 2026-05-01); Q1 FY26 10-Q (period end 2025-12-27, filed 2026-01-30) |
| FY2025 10-K | Filed 2025-10-31 (`0000320193-25-000079`) — only the debt-maturity and cash-flow history from it are present in this slice |
| **Insider transactions** | **DATA_UNAVAILABLE** — no authorized point-in-time insider archive for AAPL exists at 2026-09-22. No inference is made below. |
| **Market price / market cap / consensus** | **Not provided by these tools.** All valuation work below is EPS- and cash-flow-based only. |
| Segment/product/geographic revenue | **Not present in the retrieved slice.** Margin conclusions are therefore consolidated-level. |

Because FY26 Q4 closes ~2026-09-26 and the FY26 10-K is not yet filed, we are in a **pre-earnings information vacuum with ~5 weeks to fiscal year-end** — the highest-value incremental disclosure will be the FY26 10-K (full-year P&L, goodwill/purchase accounting, segment mix).

---

## 2. Company profile

Apple Inc. (AAPL) designs, manufactures and markets smartphones, personal computers, tablets, wearables and accessories, and derives a growing share of gross profit from services (App Store, iCloud, advertising, AppleCare, payments, content subscriptions). The company reports on a **52/53-week fiscal year ending in late September**, sells through retail, carrier, reseller and direct online channels across the Americas, Europe, Greater China, Japan and Rest-of-Asia-Pacific, and is vertically integrated around its own silicon, operating systems and services stack. Balance-sheet structure is asset-light on manufacturing (outsourced assembly) but capital-intensive in silicon/R&D, with a long-standing policy of returning essentially all free cash flow via buybacks and dividends while carrying gross debt that is more than offset by cash and marketable securities.

---

## 3. Income statement — growth re-accelerated and margins expanded sharply

### 3.1 Quarterly (Q3 FY26 vs Q3 FY25)

| $M | Q3 FY26 (Mar 29–Jun 27, 2026) | Q3 FY25 (Mar 30–Jun 28, 2025) | Δ |
|---|---:|---:|---:|
| Revenue | 109,417 | 94,036 | **+16.4%** |
| Cost of goods & services | 54,647 | 50,318 | +8.6% |
| Gross profit | 54,770 | 43,718 | **+25.3%** |
| **Gross margin** | **50.06%** | **46.49%** | **+357 bp** |
| R&D | 11,729 | 8,866 | **+32.3%** |
| SG&A | 7,346 | 6,650 | +10.5% |
| Total opex | 19,075 | 15,516 | +22.9% |
| Operating income | 35,695 | 28,202 | **+26.6%** |
| **Operating margin** | **32.62%** | **29.99%** | **+263 bp** |
| Non-operating income/(expense) | +572 | (171) | +743 |
| Pretax income | 36,267 | 28,031 | +29.4% |
| Tax | 6,478 | 4,597 | +40.9% |
| **Effective tax rate** | **17.86%** | **16.40%** | **+146 bp** |
| Net income | 29,789 | 23,434 | **+27.1%** |
| **Net margin** | **27.22%** | **24.92%** | **+230 bp** |
| Diluted EPS | **$2.02** | **$1.57** | **+28.7%** |
| Diluted shares (implied) | ~14,748M | ~14,927M | −1.2% |

**The single most important fact in this report:** gross margin crossed **50%** in Q3, up 357 bp year over year, and 425 bp from the 9M FY26 average of 49.07%. That is a structural, not seasonal, improvement — COGS grew only 8.6% against 16.4% revenue growth. Whether ~50% GM is the new floor or a peak is the central debate for the next two quarters.

### 3.2 Nine months FY26 vs nine months FY25

| $M | 9M FY26 (Sep 28, 2025–Jun 27, 2026) | 9M FY25 (Sep 29, 2024–Jun 28, 2025) | Δ |
|---|---:|---:|---:|
| Revenue | 364,357 | 313,695 | **+16.1%** |
| Gross profit | 178,782 | 146,860 | +21.7% |
| Gross margin | **49.07%** | **46.82%** | +225 bp |
| R&D | 34,035 | 25,684 | **+32.5%** |
| R&D % of revenue | **9.34%** | 8.19% | +115 bp |
| SG&A | 22,315 | 20,553 | +8.6% |
| SG&A % of revenue | 6.12% | 6.55% | −43 bp |
| Total opex | 56,350 | 46,237 | +21.9% |
| Operating income | 122,432 | 100,623 | **+21.7%** |
| Operating margin | **33.60%** | 32.08% | +152 bp |
| Pretax income | 123,102 | 99,925 | +23.2% |
| Tax | 21,638 | 15,381 | +40.7% |
| Effective tax rate | **17.58%** | 15.39% | **+219 bp** |
| Net income | 101,464 | 84,544 | +20.0% |
| Net margin | **27.85%** | 26.95% | +90 bp |
| Diluted EPS | **$6.88** | **$5.62** | **+22.4%** |

**Margin bridge (9M, +152 bp operating margin):**
- Gross margin **+225 bp** = +$7.94B of gross profit versus a flat-margin counterfactual.
- R&D **−115 bp** of revenue (investment step-up) and SG&A **+43 bp** of revenue (leverage) → net opex drag of ~72 bp.
- Net result: +152 bp operating margin. **Gross-margin expansion did all the work and funded a 32.5% R&D increase.**

**Quality-of-earnings observations:**
- EPS growth (+22.4%) exceeds net income growth (+20.0%) by ~240 bp, but **only ~1.1% of that comes from share count**; the rest is tax/rounding mix. Buyback is a modest tailwind, not the story — this is an operating-margin story.
- Revenue per diluted share rose from ~$21.0 to ~$24.8 (+18%), i.e., growth is genuinely per-share accretive even before buybacks.
- The tax rate rose 219 bp. If FY27 normalizes to ~19–20%, that alone is a **~2–3% EPS headwind** at constant pretax income — worth modeling explicitly.

### 3.3 Quarterly rhythm / seasonality
- 6M FY26 revenue = 364,357 − 109,417 = **$254,940M**; 6M gross profit = 124,012 (48.64%); 6M net income = **$71,675M**; 6M diluted EPS = **$4.85**.
- Q1 (December) remains the seasonal peak; Q3 is the trough. Q3's 50.06% GM versus a 48.64% first-half average indicates **sequential margin improvement through the year**, not a one-quarter fluke — the most constructive read in the dataset.
- 6M FY25 revenue was $219,659M, so first-half FY26 grew ~16.1% — consistent with the full 9M rate. Growth was stable, not front-loaded.

---

## 4. Balance sheet — fortress rebuilt, but inventory and intangibles are flashing

### 4.1 Position (2026-06-27 vs 2025-09-27)

| $M | 2026-06-27 | 2025-09-27 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 39,544 | 35,934 | +3,610 |
| Marketable securities — current | 22,855 | 18,763 | +4,092 |
| Marketable securities — noncurrent | 84,118 | 77,723 | +6,395 |
| **Total cash + securities** | **146,517** | **132,420** | **+14,097** |
| Accounts receivable | 31,398 | 39,777 | −8,379 |
| Nontrade receivables | 27,509 | 33,180 | −5,671 |
| **Inventory** | **11,092** | **5,718** | **+5,374 (+94%)** |
| — Raw materials & purchased parts | 7,645 | 2,124 | **+260%** |
| — Finished goods | 3,447 | 3,594 | −147 |
| Other current assets | 17,420 | 14,585 | +2,835 |
| Current assets | 149,818 | 147,957 | +1,861 |
| Noncurrent assets | 233,448 | 211,284 | +22,164 |
| — Intangibles, gross | 38,220 | 24,950 | **+13,270** |
| — Intangibles, net | 25,417 | 13,301 | **+12,116** |
| — Other noncurrent assets | 77,557 | 72,634 | +4,923 |
| **Total assets** | **383,266** | **359,241** | **+6.7%** |
| Accounts payable | 64,525 | 69,860 | −5,335 |
| Commercial paper | 1,997 | 7,979 | −5,982 |
| Current portion of LT debt | 11,007 | 12,350 | −1,343 |
| Other current liabilities | 62,259 | 66,387 | −4,128 |
| Current liabilities | 149,326 | 165,631 | −9.8% |
| Long-term debt (noncurrent) | 71,340 | 78,328 | −6,988 |
| **Total debt (CP + LTD)** | **84,297** | **98,679** | **−14,382** |
| Other noncurrent liabilities | 55,080 | 41,549 | **+13,531** |
| Total liabilities | 275,746 | 285,508 | −3.4% |
| **Shareholders' equity** | **107,520** | **73,733** | **+45.8%** |
| Deferred revenue (total / current) | 14,900 / 9,538 | 13,700 / 9,055 | +8.8% / +5.3% |

### 4.2 What matters here

**a) Net cash nearly doubled.** Net cash (cash + securities − total debt) = **$62,220M**, up from **$33,741M** nine months ago — a **+$28.5B** swing in three quarters. Total debt fell $14.4B with **zero new long-term debt issued in FY26** (proceeds from LT debt = $0). Net cash is now **$4.26/share**. That is firepower, not a problem.

**b) Inventory +94% and raw materials +260% — the one genuine yellow flag.** Inventory days (on Q3 COGS) rose to **~18.5 days from ~9.4 days** a year ago. Finished goods actually *fell* 4%, so the build is entirely upstream (components/raw materials). Two readings:
- **Bullish:** pre-buying ahead of a new product ramp and/or ahead of expected component (memory/advanced-node) cost inflation — this protects forward gross margin, which is exactly what Q3's 50% GM suggests is working.
- **Bearish:** a demand or supply-chain signal that reverses, leaving obsolescence exposure and a working-capital drag in Q4/FY27.

The evidence currently favors the bullish read (finished goods down, GM up, deferred revenue up 8.8% to $14.9B), but this is the metric to interrogate on the FY26 10-K and Q4 call. **A further large build with flat revenue would flip the interpretation.**

**c) ~$13B of intangibles appeared — Apple did M&A at scale.** Gross intangibles +$13.3B, net +$12.1B, while accumulated amortization rose only $1.15B. Simultaneously **other noncurrent liabilities rose $13.5B**, consistent with deferred-tax liabilities recognized in acquisition accounting. Combined with zero debt issuance and a $62B net cash pile, this looks like **cash-funded acquisitions of technology/IP**, not a balance-sheet stretch. Risks: amortization creep into COGS/opex and future impairment. Upside: acquired IP/AI capability. **The FY26 10-K purchase-price allocation is a must-read.**

**d) Working capital became a source of cash.** Receivables down $8.4B and nontrade receivables down $5.7B against a $5.3B payables decline and revenue up 16% — DSO compressed to **~26.1 days from ~38.5 days**. That is unusually strong collections and flatters 9M operating cash flow (see §5).

**e) Equity +$45.8B, almost entirely earned.** 9M net income $101.5B, less $62.1B buybacks and $11.8B dividends, plus $10.5B SBC and a $1.06B AOCI improvement reconciles the move. Book value is now **$7.36/share**; tangible book ~$5.62/share (no goodwill tag in this slice, so true tangible book is lower).

**f) Debt maturity ladder is a non-issue.** From the FY25 10-K: $12,393M due in 12 months, $10,078M yr 2, $9,300M yr 3, $5,235M yr 4, $4,972M yr 5, $49,303M beyond yr 5. Against $146.5B of liquid assets, refinancing risk is negligible. Operating leases total $14,725M; finance leases $1,579M.

---

## 5. Cash flow and capital allocation

| $M | 9M FY26 | 9M FY25 | Δ |
|---|---:|---:|---:|
| Net income | 101,464 | 84,544 | +20.0% |
| D&A | 9,973 | 8,571 | +16.4% |
| SBC (non-cash) | 10,523 | 9,680 | +8.7% |
| **Operating cash flow** | **116,996** | **81,754** | **+43.1%** |
| OCF margin | **32.11%** | 26.06% | +605 bp |
| Capex | 6,799 | 9,473 | −28.2% |
| Capex % of revenue | 1.87% | 3.02% | −115 bp |
| **Free cash flow** | **110,197** | **72,281** | **+52.5%** |
| FCF margin | **30.24%** | 23.04% | +720 bp |
| Buybacks | 62,094 | 70,579 | −12.0% |
| Dividends | 11,778 | 11,559 | +1.9% |
| **Total shareholder returns** | **73,872** | **82,138** | **−10.1%** |
| Returns / FCF | 67.0% | 113.6% | — |
| SBC tax withholding | 6,462 | 5,719 | +13.0% |
| Purchases of AFS securities | 48,752 | 17,591 | +177% |
| Proceeds from sales/maturities of AFS | 38,520 | 45,821 | −15.9% |
| Repayment of LT debt | 8,146 | 9,682 | −15.9% |
| Commercial paper, net | (5,911) | (65) | — |
| Investing cash flow | (18,811) | +17,782 | −$36.6B swing |
| Financing cash flow | (94,575) | (93,210) | −1.5% |

**Key reads:**

1. **Cash conversion is excellent and improving.** OCF/NI = **1.15x** vs **0.97x** a year ago. But note the driver is largely working capital (receivables down $8.4B, other operating liabilities +$10.0B vs −$15.2B last year), not just earnings. **Q4 will see some reversal** — do not extrapolate the 43% OCF growth rate.
2. **9M FY26 FCF of $110.2B already exceeds FY24's full-year FCF** (FY24 OCF $118.3B less 9M capex $9.5B implies ~$107–109B). A nine-month period is out-earning a full prior year in cash.
3. **Capex is falling, not rising** (−28%), to 1.87% of revenue. Apple is *not* in a capex super-cycle; the AI investment is running through **R&D (+32.5%)**, not PP&E. This is important: the expense is hitting the P&L now, but it is not capital-intensive.
4. **Buyback pace decelerated 12% over 9M but re-accelerated in Q3.** Q3 buybacks = 62,094 − 36,989 = **$25,105M vs $21,075M** a year ago (**+19.1%**). Q3 returns were **$29,140M = 91% of Q3 FCF ($31,914M)**. Management leaned back in once Q3 FCF inflected. That is a bullish tell.
5. **The $36.6B investing swing is portfolio rotation, not distress.** AFS purchases rose $31.2B while maturities fell; net securities purchases absorbed cash. Simultaneously the intangible jump implies ~$13B went to acquisitions inside "other investing." Neither shows up as capex.
6. **Dividend remains nominal:** $0.27/qtr (9M $0.79 vs $0.76, +3.9%); annualized **$1.08**, payout only **~11.6% of 9M net income**. Dividend policy is not a signal here — buybacks are.

---

## 6. Financial history (what the slice supports)

| Metric | FY2023 | FY2024 | FY2025 | 9M FY2026 |
|---|---:|---:|---:|---:|
| Operating cash flow ($M) | 110,543 | 118,254 | n/a in slice | **116,996** |
| Investing cash flow ($M) | +3,705 | +2,935 | +15,195 | (18,811) |
| Financing cash flow ($M) | (108,488) | (121,983) | (120,686) | (94,575) |
| Shareholders' equity, period end ($M) | — | 56,950 (9/28/24) | 73,733 (9/27/25) | **107,520** |
| Cash & equivalents, period end ($M) | — | 29,943 (9/28/24) | 35,934 (9/27/25) | **39,544** |
| Diluted EPS | — | — | — | **$6.88** |

**Trajectory:** financing outflows of $108B → $122B → $121B annually show a company that has returned more than $350B to shareholders over three years while *growing* its cash balance — the definition of a self-funding capital-return machine. FY26 breaks the pattern modestly: financing outflow is *lower* (−$94.6B in 9M) because buybacks slowed and debt was repaid, while investing turned negative for the first time (securities build + M&A). **The cash is being redeployed inward — into IP and acquisitions — rather than only outward.** That is a genuine strategic shift worth watching.

*Gap to note:* full-year FY2025 P&L and FY2023–FY25 revenue/net income are not present in this retrieved slice, so multi-year revenue CAGR cannot be computed from the tool output. Do not let any downstream model fabricate it.

---

## 7. Derived quality and efficiency metrics

| Metric | Latest (Q3 FY26 / 6-27-26) | Prior-year comparable | Comment |
|---|---:|---:|---|
| Gross margin | 50.06% | 46.49% | +357 bp; the core bull case |
| Operating margin | 32.62% | 29.99% | +263 bp |
| Net margin | 27.22% | 24.92% | +230 bp |
| R&D / revenue | 10.72% (Q3) · 9.34% (9M) | 9.43% · 8.19% | Investment step-up |
| Effective tax rate | 17.86% (Q3) · 17.58% (9M) | 16.40% · 15.39% | Normalizing — EPS headwind |
| Current ratio | 1.00x | 0.89x | Improving but still thin by design |
| Total debt | $84.3B | $98.7B (9/27/25) | −$14.4B |
| Net cash | **$62.2B** | $33.7B (9/27/25) | +$28.5B |
| Debt / equity | 0.78x | 1.34x (9/27/25) | Deleveraging fast |
| Net debt / annualized EBITDA | **net cash** | net cash | No leverage concern |
| Inventory days (on Q3 COGS) | ~18.5 | ~9.4 | ⚠️ Watch item |
| DSO | ~26.1 | ~38.5 | Strong collections |
| DPO | ~107.5 | ~113 (est.) | Slight vendor-payment tightening |
| ROE (annualized, avg equity) | **~149%** | — | Distorted by thin equity base |
| ROA (annualized, avg assets) | **~36.4%** | — | Genuinely exceptional |
| FCF margin (9M) | 30.24% | 23.04% | +720 bp |
| FCF per share (9M) | ~$7.52 | ~$4.84 | +55% |
| Buyback yield proxy (shares retired) | 1.11% in 9M | — | Modest vs history |
| Shares outstanding | 14,608.963M | 14,773.260M (9/27/25) | −1.1%; 14,594.180M as of 7/17/26 |

*ROE/ROIC are not economically meaningful here in the traditional sense because Apple operates with net cash and negative working capital; ROA and FCF margin are the better efficiency gauges.*

---

## 8. Insider transactions

**DATA_UNAVAILABLE.** The data package contains **no authorized, point-in-time insider-transactions archive for AAPL as of 2026-09-22.** No purchases, sales, exercises, gifts, or 10b5-1 plan activity can be reported, and **none should be inferred**. The absence of records here is a data-availability fact, not evidence that insiders were inactive. Traders should source Form 4 filings directly from EDGAR before drawing any insider signal; this report makes no insider-based recommendation.

---

## 9. Actionable insights for traders

**1. Own the margin thesis, not the growth thesis.**
Revenue +16.4% is strong, but the P&L delta is margin: gross margin +357 bp drove +25.3% gross profit on +16.4% revenue, and operating income grew +26.6% — 10 points faster than sales. If you are long AAPL, your actual bet is that **~50% gross margin is durable**. Define the invalidation level: **two consecutive quarters below ~48.5% GM** would break the thesis and compress EPS meaningfully.

**2. Model FY26 EPS at roughly $8.90–9.00, then apply your own multiple.**
9M diluted EPS is $6.88. Q3 alone was $2.02. If Q4 lands in the $2.00–2.10 range (consistent with Q3, with Q4 typically modestly above Q3), **FY26 diluted EPS ≈ $8.88–8.98.** At those levels, illustrative price outcomes are **~$222 at 25x, ~$267 at 30x, ~$311 at 35x.** With 9M FCF/share of $7.52 (annualizing to ~$10), the cash-flow support at 25x FCF is roughly $250. These are arithmetic scenarios, **not** valuation conclusions — the tools provide no market price, so no P/E or FCF yield can be asserted.

**3. Treat the tax rate as a real, underappreciated headwind.**
Effective rate went from 15.39% to 17.58% (9M) and 16.40% to 17.86% (Q3). Each +100 bp of tax rate is roughly **$0.10–0.11 of EPS** at current pretax run-rate. A move toward 19–20% would shave ~2–3% off FY27 EPS with no operational cause. Ask management to quantify the sustainable rate.

**4. Watch inventory as the leading indicator, both ways.**
Inventory +94% with raw materials +260% and finished goods *down* 4% is a pre-build, not a demand problem — yet. **Signal to monitor:** if Q4/FY26 inventory rises again while revenue growth decelerates below ~10%, that flips from "protecting margin" to "channel stuffing/obsolescence," and GM is the first thing to break. Conversely, if the pre-buy converts into a strong December quarter, GM could hold above 50% into FY27 — the upside case.

**5. Respect the Q3 buyback re-acceleration.**
Q3 buybacks of $25.1B (+19.1% y/y) after a slower first half, at 91% of Q3 FCF, is a real capital-allocation signal. With $62.2B net cash and $110.2B 9M FCF, Apple has room to sustain or increase this. **Buybacks are ~$1.08 of annual EPS support per 1% of shares retired** at current earnings — modest, but it is a floor under the stock on weakness.

**6. Price in the M&A/intangibles shift.**
~$13B of gross intangibles appeared in nine months with $0 new debt. This is cash-funded IP acquisition. Two implications: (a) amortization will creep higher, a modest ongoing opex/COGS headwind; (b) Apple may be buying AI/technology capability rather than building it. **The FY26 10-K purchase-price allocation is the highest-value non-earnings disclosure you will get this cycle** — check goodwill vs. amortizable intangibles and whether any revenue comes with the deals.

**7. Position for the pre-earnings window.**
Fiscal year-end is ~2026-09-26; FY26 results and 10-K typically follow in late October. Between now and then there is **no new company financial disclosure in this dataset** — the next 5 weeks are headline/flow-driven, not fundamental. The fundamentals you can act on today are: accelerating margins, $62B net cash, 30% FCF margin, and a decelerating-but-still-present buyback. That is an asymmetric setup *if* the multiple is reasonable — which requires a price check this tool cannot provide.

**8. Reduce exposure to the "services mix" narrative until segment data is available.**
The 50% gross margin is consistent with services mix, but this dataset contains **no product/geographic revenue split**. Do not attribute the margin gain to Services without the 10-K segment table. The COGS line (only +8.6%) is the hard evidence; the *cause* is unverified.

---

## 10. Key risks (ranked by likely impact on EPS)

| # | Risk | Evidence | Sensitivity |
|---|---|---|---|
| 1 | Gross margin mean-reverts | Q3 50.06% vs 9M 49.07%; Q3 is the seasonally easiest compare | −200 bp GM ≈ −$2.2B/qtr gross profit ≈ −$0.11–0.12 EPS/qtr |
| 2 | Component cost inflation / inventory write-down | Raw materials +260%, inventory +94%, inventory days 9.4 → 18.5 | Direct COGS hit; could erase the 357 bp gain |
| 3 | Tax rate normalization | 15.39% → 17.58% (9M); +219 bp | Each +100 bp ≈ −$0.10 EPS |
| 4 | R&D growth outrunning revenue | R&D +32.5% vs revenue +16.1%; 8.19% → 9.34% of sales | If revenue slows to <8%, opex leverage reverses |
| 5 | OCF quality (working-capital-driven) | OCF +43% vs NI +20%; receivables −$8.4B | Q4 reversal risk; FCF growth is not repeatable at this rate |
| 6 | M&A integration / impairment | +$13.3B gross intangibles, +$13.5B noncurrent liabilities | Amortization creep; potential write-down |
| 7 | Buyback slowdown limits EPS support | 9M buybacks −12.0%; shares only −1.1% | Each 1% fewer shares retired ≈ −$0.09 EPS |
| 8 | Thin current ratio | 1.00x; current liabilities $149.3B | Structural, but a liquidity-event amplifier |
| 9 | Concentration/regulatory (unquantified) | Not in dataset | Not modeled — flag only |

---

## 11. Bottom line

AAPL's fundamentals **strengthened materially** over the last three reported quarters. Nine-month revenue grew **16.1%** to $364.4B, gross margin expanded **225 bp to 49.07%** (and **357 bp to 50.06%** in Q3), operating income rose **21.7%**, diluted EPS rose **22.4% to $6.88**, and free cash flow surged **52.5% to $110.2B** — a 30.2% FCF margin. The balance sheet added **$28.5B of net cash in nine months** to reach **$62.2B net cash**, cut total debt $14.4B with no new long-term issuance, and grew equity **45.8%**. Buybacks re-accelerated **19% y/y in Q3**, and 91% of Q3 FCF was returned to shareholders.

Against that, three things demand discipline: **inventory is up 94%** (raw materials +260%), the **tax rate has risen 219 bp**, and **R&D is growing at twice the rate of revenue**. None is yet a thesis-breaker; the first is the one that could become one.

**Fundamental stance: constructive/positive.** The operating momentum, cash generation and balance-sheet capacity are unambiguous. **Valuation stance: undetermined** — this tool set contains no price data, so no P/E, FCF yield, or target multiple can be asserted. Traders should combine the ~$8.90–9.00 FY26 EPS estimate and ~$10 FCF/share run-rate above with a live quote before sizing a position. Insider activity **cannot be assessed** — the archive is unavailable and no inference should be drawn.

---

## 12. Key points summary

| Category | Metric | Value | Read-through |
|---|---|---|---|
| **Period** | Latest report | Q3 FY26, ended 2026-06-27 (10-Q filed 2026-07-31) | Point-in-time, pre-FY26 10-K |
| **Growth** | Q3 revenue | $109,417M, **+16.4% y/y** | Stable mid-teens growth |
| **Growth** | 9M revenue | $364,357M, **+16.1% y/y** | Not front-loaded |
| **Profitability** | Q3 gross margin | **50.06%** (+357 bp) | Crossed 50%; core bull case |
| **Profitability** | 9M gross margin | 49.07% (+225 bp) | Sequential improvement through year |
| **Profitability** | Q3 operating margin | **32.62%** (+263 bp) | Gross margin funded opex |
| **Profitability** | 9M operating margin | 33.60% (+152 bp) | +$21.8B incremental op income |
| **Earnings** | Q3 diluted EPS | **$2.02, +28.7%** | Fastest line-item growth |
| **Earnings** | 9M diluted EPS | **$6.88, +22.4%** | FY26E ≈ $8.90–9.00 |
| **Earnings** | 9M net income | $101,464M (+20.0%); 27.85% margin | +90 bp net margin |
| **Investment** | 9M R&D | $34,035M, **+32.5%**; 9.34% of revenue | AI/IP step-up; margin risk if revenue slows |
| **Investment** | 9M capex | $6,799M, −28.2%; 1.87% of revenue | Not a capex cycle — expense-led |
| **Tax** | 9M effective rate | **17.58% vs 15.39%** | +219 bp EPS headwind |
| **Cash flow** | 9M operating cash flow | **$116,996M, +43.1%** | 1.15x net income; WC-assisted |
| **Cash flow** | 9M free cash flow | **$110,197M, +52.5%**; 30.24% margin | Exceeds FY24 full-year FCF |
| **Cash flow** | Q3 FCF | $31,914M (+30.8%) | Inflection quarter |
| **Balance sheet** | Cash + securities | **$146,517M** | +$14.1B in 9 months |
| **Balance sheet** | Total debt | $84,297M (−$14.4B); no new LT debt | Deleveraging |
| **Balance sheet** | **Net cash** | **$62,220M vs $33,741M** | +$28.5B; ~$4.26/share |
| **Balance sheet** | Debt/equity | **0.78x vs 1.34x** | Fortress rebuilt |
| **Balance sheet** | Shareholders' equity | **$107,520M, +45.8%** | $7.36 BVPS |
| **Balance sheet** | Inventory | **$11,092M, +94%**; raw materials +260% | ⚠️ #1 watch item |
| **Balance sheet** | Inventory days / DSO | ~18.5 (vs 9.4) / ~26.1 (vs 38.5) | Upstream build; strong collections |
| **Balance sheet** | Net intangibles | **$25,417M vs $13,301M (+91%)** | ~$13B cash-funded M&A/IP |
| **Balance sheet** | Deferred revenue | $14,900M (+8.8%) | Forward demand indicator positive |
| **Capital return** | 9M buybacks / dividends | $62,094M / $11,778M | Returns = 67% of FCF (vs 114%) |
| **Capital return** | Q3 buybacks | $25,105M, **+19.1% y/y** | Re-acceleration = bullish tell |
| **Capital return** | Dividend | $0.27/qtr, $1.08 annualized; ~11.6% payout | Nominal; buyback is the lever |
| **Shares** | Outstanding | 14,608.963M (−1.1% in 9M); 14,594.180M at 7/17/26 | Modest EPS tailwind |
| **Returns** | Annualized ROE / ROA | ~149% / ~36.4% | Exceptional; ROE distorted by thin equity |
| **Efficiency** | FCF/share (9M) | ~$7.52 vs ~$4.84 | +55% |
| **Insider** | Transactions | **DATA_UNAVAILABLE — no authorized archive; no inference made** | Must source Form 4s directly |
| **Valuation** | Price / P/E / yield | **Not provided by tools** | Use $8.90–9.00 FY26E EPS + live quote |
| **Catalyst** | Next disclosure | FY26 Q4 + 10-K, likely late Oct 2026 | Watch GM ~50%, inventory, tax rate, goodwill |
| **Stance** | Fundamentals / Valuation | **Constructive** / **Undetermined** | Long thesis = margin durability, not growth |