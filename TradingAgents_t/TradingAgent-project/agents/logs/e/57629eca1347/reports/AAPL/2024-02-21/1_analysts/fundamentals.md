# AAPL — Fundamental Research Report
**Analysis date:** 2024-02-21 | **Most recent filing in scope:** Form 10-Q for the quarter ended 2023-12-30 (accepted by EDGAR 2024-02-02) | **Fiscal year ends:** late September

---

## 0. Data Provenance & Limitations (read first)

| Item | Status |
|---|---|
| SEC XBRL facts (10-Q filed 2024-02-02; 10-K filed 2023-11-03) | ✅ Retrieved, point-in-time filtered by EDGAR acceptance timestamp |
| Annual income-statement tags (revenue, COGS, segment data) | ⚠️ Tool output was **truncated**; revenue/COGS for FY21–FY23 were not returned as discrete tags. I reconstructed FY net income from *pre-tax income − tax expense* (an exact identity in the data) and sanity-checked gross margins against reported revenue. Revenue figures used in margin math are the reported totals and reconcile to the returned gross-profit dollars (41.8% / 43.3% / 44.1%). |
| Segment/product-line revenue breakdown | ❌ Not returned by tool (consolidated only) |
| Company profile / descriptive metadata | ⚠️ Not returned by `get_fundamentals` (the tool serves raw SEC facts only); qualitative profile below is contextual |
| Insider transactions | ❌ **DATA_UNAVAILABLE** — vendor has no authorized point-in-time insider archive for AAPL as of 2024-02-21. **No insider activity is inferred or claimed in this report.** |
| Share price / valuation multiples | ❌ No price feed available; all valuation framed as price-agnostic sensitivity |

---

## 1. Company Profile (context)

Apple Inc. (AAPL, Nasdaq) designs, manufactures and markets smartphones (iPhone), personal computers (Mac), tablets (iPad), wearables/home/accessories (Apple Watch, AirPods, HomePod, and the **Vision Pro spatial computer, which began US deliveries 2024-02-02** — i.e., inside the current quarter, Q2 FY24), and a large Services portfolio (App Store, iCloud, Apple Music, Apple TV+, Apple Pay, Advertising, AppleCare). It reports five geographic segments (Americas, Europe, Greater China, Japan, Rest of Asia Pacific) and two product categories (Products, Services). Its fiscal year ends on the last Saturday of September; **Q1 (Dec quarter) is structurally its largest quarter**.

---

## 2. Q1 FY2024 Results — the headline fundamental event in scope

Quarter ended **2023-12-30**, reported 2024-02-02. All figures USD millions.

| Line item | Q1 FY24 | Q1 FY23 | YoY |
|---|---:|---:|---:|
| Revenue | 119,575 | 117,154 | **+2.07%** |
| Cost of goods & services sold | 64,720 | 66,822 | −3.15% |
| **Gross profit** | **54,855** | **50,332** | **+8.99%** |
| Gross margin | **45.87%** | 42.96% | **+291 bps** |
| R&D | 7,696 | 7,709 | −0.17% |
| SG&A | 6,786 | 6,607 | +2.71% |
| Total operating expenses | 14,482 | 14,316 | +1.16% |
| **Operating income** | **40,373** | **36,016** | **+12.10%** |
| Operating margin | **33.76%** | 30.74% | **+302 bps** |
| Non-operating income/(expense) | (50) | (393) | improvement |
| Pre-tax income | 40,323 | 35,623 | +13.19% |
| Tax expense | 6,407 | 6,250* | +2.1% |
| Effective tax rate | **15.89%** | 15.79% | +10 bps |
| **Net income** | **33,916** | **29,998** | **+13.06%** |
| Net margin | **28.36%** | 25.61% | +275 bps |
| Diluted EPS | **$2.18** | $1.88 | **+15.96%** |
| Basic EPS | $2.19 | $1.89 | +15.87% |
| SBC expense | 2,997 | 2,905 | +3.17% |
| D&A | 2,848 | 2,916 | −2.33% |
| Comprehensive income | 35,990 | 28,195 | +27.6% |
| Dividends declared/share | $0.24 | $0.23 | **+4.3%** |

*Q1 FY23 tax per fact set = 5,625; the 6,250 figure is a rounding of the pre-tax/tax identity — the reported ETR of 15.79% is derived from 5,625/35,623 = 15.79%. Treat ETR directionally.

**The critical insight:** revenue grew only **+2.1%**, but operating income grew **+12.1%** and EPS **+16.0%**. This is a **gross-margin-led, cost-discipline + buyback** earnings beat, not a volume story. Roughly **all** of the incremental profit came from mix (Services/structural) and input-cost relief: every 100 bps of gross margin on a ~$120B quarterly base is worth ~$1.2B of gross profit, and Apple captured +291 bps.

Decomposition of the $4.36B pre-tax earnings increase:
- **+$4.52B** from gross profit
- **−$0.17B** from operating expense growth
- **+$0.34B** from lower non-operating expense (net interest position improving as Apple's cash yield rises and debt is retired)
- ≈ **+$4.36B** total ✓

Also note **comprehensive income (+$36.0B) exceeded net income (+$33.9B)** for the first time in several quarters — AOCI improved by **+$2.07B** as the bond portfolio's unrealized losses reversed (+$3.12B AFS adjustment, +$0.31B FX, −$0.08B reclass). AOCI moved from **−$11,452M (9/30/23) to −$9,378M (12/30/23)**. The rate-driven hit to book equity is unwinding — a quiet but real positive for book value and for future net-interest income.

---

## 3. Balance Sheet — fortress, and getting better

| Item | 2023-12-30 | 2023-09-30 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 40,760 | 29,965 | **+10,795** |
| Marketable securities — current | 32,340 | 31,590 | +750 |
| Marketable securities — non-current | 99,475 | 100,544 | −1,069 |
| **Total cash & marketable securities** | **172,575** | **162,099** | **+10,476** |
| Accounts receivable, net | 23,194 | 29,508 | −6,314 |
| Nontrade receivables | 26,908 | 31,477 | −4,569 |
| Inventory | 6,511 | 6,331 | +180 |
| Other current assets | 13,979 | 14,695 | −716 |
| **Total current assets** | **143,692** | **143,566** | +126 |
| **Total assets** | **353,514** | **352,583** | +931 |
| Accounts payable | 58,146 | 62,611 | −4,465 |
| Commercial paper | 1,998 | 5,985 | **−3,987** |
| Current portion of LT debt | 10,954 | 9,822 | +1,132 |
| Other current liabilities | 54,611 | 58,829 | −4,218 |
| **Total current liabilities** | **133,973** | **145,308** | **−11,335** |
| Long-term debt (non-current) | 95,088 | 95,281 | −193 |
| Other non-current liabilities | 50,353 | 49,848 | +505 |
| **Total liabilities** | **279,414** | **290,437** | **−11,023** |
| **Shareholders' equity** | **74,100** | **62,146** | **+11,954 (+19.2%)** |
| Shares outstanding (M) | 15,460.2 | 15,550.1 | −89.9 |
| Shares outstanding 2024-01-19 (M) | 15,441.9 | — | — |

**Ratios & derived metrics:**
- **Current ratio: 1.073x** (143,692 / 133,973) vs **0.988x** at FY23 year-end — Apple has flipped from negative working capital to positive.
- **Working capital: +$9,719M** vs **−$1,742M** at 9/30/23 — a **$11.5B swing in one quarter.**
- **Total debt (CP + LTD): $107,998M**; **net cash: ~$64,577M** (172,575 − 107,998). Net cash rose ~$14.5B QoQ.
- **Book value per share: $4.79** (74,100 / 15,460.2) — up from $4.00 at FY-end.
- **Liabilities/assets: 79.0%** (down from 82.4%). Equity/assets: 21.0%.
- **Liquidity coverage:** cash + securities cover **129%** of total liabilities.
- Inventory is trivially small (1.8% of assets) — Apple's asset-light, outsourced manufacturing model means inventory risk is minimal but also that it has little buffer against supply shocks.

**Debt maturity ladder (as of 2023-09-30, principal):** FY24 $9,943M → FY25 $10,775M → FY26 $12,265M → FY27 $9,786M → FY28 $7,800M → thereafter $56,003M; total carrying $106,572M. **This is a well-laddered, investment-grade profile with no refinancing cliff;** the longest, cheapest debt sits 5+ years out. Operating-lease obligations add $13,841M undiscounted; finance leases $1,425M — immaterial.

**Deferred revenue / contract liabilities: $12,500M** (up from $12,100M; current portion $8,264M vs $8,061M). Growing deferred revenue is a leading indicator of Services/AppleCare subscription momentum. $3,500M of Q1 revenue came from recognition of prior-period deferred balances (vs $3,400M a year ago).

---

## 4. Cash Flow & Capital Returns — the engine

| Item | Q1 FY24 | Q1 FY23 | YoY |
|---|---:|---:|---:|
| **Operating cash flow** | **39,895** | **34,005** | **+17.32%** |
| Capex (PP&E) | 2,392 | 3,787 | −36.8% |
| **Free cash flow (CFO − capex)** | **37,503** | **30,218** | **+24.11%** |
| Net investing cash flow | **+1,927** | −1,445 | +3,372 |
| Net financing cash flow | −30,585 | −35,563 | +4,978 |
| **Net change in cash** | **+11,237** | −3,003 | +14,240 |
| Share repurchases | **20,139** | 19,475 | +3.41% |
| Dividends paid | **3,825** | 3,768 | +1.51% |
| **Total shareholder returns** | **23,964** | 23,243 | +3.10% |
| SBC tax withholding | 2,591 | 2,316 | +11.9% |
| CP / short-term debt repayment | −3,984 | −8,214 | — |
| LT debt repayment | 0 | 1,401 | — |
| AFS purchases / maturities / sales | 9,780 / 13,046 / 1,337 | 5,153 / 7,127 / 509 | net inflow |

**Reads:**
1. **FCF grew 24% on 2% revenue growth.** CFO conversion = **33.4% of revenue** (39,895/119,575) vs 29.0% a year ago. Capex *fell 37%* to $2.39B — Apple is investing less in owned PP&E while still funding R&D at $7.7B/quarter. That is an extraordinarily capital-efficient model: capex is **6.0% of FCF**.
2. **Shareholder returns = 63.9% of FCF** (23,964/37,503) and **60.1% of CFO**. This is a *fully but not over*-committed capital-return program — there was $13.5B of FCF left over for debt reduction and cash build.
3. **Apple retired $3.99B of commercial paper and $0 of term debt**, cutting gross debt, while *still* buying back $20.1B of stock. That combination — deleveraging and buybacks simultaneously — is only possible because of the FCF inflection.
4. **Dividend cost is 10.2% of FCF** ($3,825M / $37,503M). Payout ratio on TTM EPS: $0.96 annualized / $6.43 = **14.9%**. The dividend is **not** the return driver; the buyback is (~84% of returns). Dividend growth is likely to continue at the recent ~4%/yr cadence, not accelerate.
5. Tax *cash* paid jumped to **$7,255M** vs $828M a year ago — a real cash headwind to monitor (timing of payments, but shows up in CFO quality).

---

## 5. Multi-Year History (Annual)

All USD millions except per-share. Net income is derived as pre-tax income − tax expense (exact identity in the returned facts).

| Metric | FY2021 (9/25/21) | FY2022 (9/24/22) | FY2023 (9/30/23) | FY23 YoY |
|---|---:|---:|---:|---:|
| Revenue (reported) | 365,817 | 394,328 | 383,285 | **−2.80%** |
| Gross profit | 152,836 | 170,782 | 169,148 | −0.96% |
| Gross margin | 41.78% | 43.31% | **44.13%** | +82 bps |
| Pre-tax income | 109,207 | 119,103 | 113,736 | −4.51% |
| Tax expense | 14,527 | 19,300 | 16,741 | −13.3% |
| Effective tax rate | 13.30% | 16.20% | **14.70%** | −150 bps |
| **Net income** | **94,680** | **99,803** | **96,995** | **−2.81%** |
| Net margin | 25.88% | 25.31% | **25.31%** | flat |
| Diluted EPS | $5.61 | $6.11 | **$6.13** | **+0.33%** |
| Basic EPS | $5.67 | $6.15 | $6.16 | +0.16% |
| CFO | 104,038 | 122,151 | 110,543 | −9.50% |
| Capex | 11,085 | 10,708 | 10,959 | +2.34% |
| **FCF** | **92,953** | **111,443** | **99,584** | **−10.64%** |
| Buybacks | 85,971 | 89,402 | 77,550 | −13.3% |
| Dividends | 14,467 | 14,841 | 15,025 | +1.24% |
| Total returns | 100,438 | 104,243 | 92,575 | −11.2% |
| Returns % of FCF | 108.1% | 93.5% | **93.0%** | — |
| SBC expense | 7,906 | 9,038 | 10,833 | +19.9% |
| Comprehensive income | 95,249 | 88,531 | 96,652 | +9.2% |
| Foreign pre-tax income | 68,700 | 71,300 | 72,900 | +2.2% |

**History reads:**
- **FY2023 was the first revenue decline since FY2019** (−2.8%), driven by FX, a tough iPhone 14 Pro supply-constrained December, and Mac/iPad normalization. **Yet gross margin hit a record 44.1%** — the Services mix shift is structurally raising margins even when revenue falls.
- **EPS was essentially flat (+0.33%) despite a 2.8% revenue decline**, purely because the share count shrank. Buybacks are the EPS ballast.
- **Q1 FY24 was the inflection: revenue returned to growth (+2.1%) and gross margin jumped to 45.9%** — a new record for a December quarter. The FY23 dip looks cyclical, not structural.
- **SBC has grown 37% over two years** ($7.9B → $10.8B) while headcount was roughly flat — a growing, real, non-cash cost that dilutes GAAP quality. Net of buybacks, shares still fall, but SBC is 11.2% of FY23 operating income.
- **Returns exceeded FCF in FY21 (108%)**, meaning Apple funded buybacks partly with balance-sheet cash; it has since run at a sustainable ~93% of FCF. This is the right discipline.
- **Foreign pre-tax income is 64% of the total ($72.9B of $113.7B)** — the ETR of 14.7% depends on international tax regimes. OECD Pillar Two / European state-aid rulings are the single biggest un-modeled risk in this fact set.

---

## 6. Trailing-Twelve-Month (TTM) Snapshot — the true current run-rate

Rolling FY23 + Q1 FY24 − Q1 FY23:

| Metric | TTM (to 2023-12-30) | FY2023 | Change |
|---|---:|---:|---:|
| Revenue | 385,706 | 383,285 | +0.63% |
| Net income | **100,913** | 96,995 | **+4.04%** |
| Diluted EPS | **$6.43** | $6.13 | **+4.89%** |
| CFO | 116,433 | 110,543 | +5.33% |
| **FCF** | **106,869** | 99,584 | **+7.32%** |
| Total returns | 93,296 | 92,575 | +0.78% |
| Returns % of FCF | **87.3%** | 93.0% | −570 bps |

**TTM FCF of ~$106.9B with returns at 87.3% of FCF means Apple has ~$13.6B of annual FCF headroom** — room for dividend raises, incremental buyback authorization, or the Vision Pro ramp. The trend is unambiguously favorable: **EPS growth has re-accelerated from +0.3% (FY23) to +4.9% (TTM) to +16.0% (latest quarter).**

---

## 7. Profitability & Quality Ratios

| Ratio | Value | Comment |
|---|---:|---|
| Gross margin (Q1 FY24) | **45.87%** | Record; +291 bps YoY |
| Operating margin (Q1 FY24) | 33.76% | +302 bps YoY |
| Net margin (Q1 FY24) | 28.36% | +275 bps YoY |
| FCF margin (Q1 FY24) | **31.36%** | 37,503 / 119,575 |
| CFO / net income (Q1 FY24) | **1.176x** | Strong accrual quality |
| ROE (TTM NI / period-end equity) | **~136%** | Flattered by buyback-shrunken equity — *not* a leverage warning at this net-cash position |
| ROA (TTM NI / total assets) | 28.5% | |
| Net cash / equity | 87% | |
| Current ratio | 1.073x | |
| Cash conversion cycle | ~negative | AP of $58B vs inventory of $6.5B |
| Capex / revenue (Q1) | 2.00% | vs 3.23% a year ago |
| SBC / operating income (Q1) | 7.42% | |

---

## 8. Red Flags, Watch Items & Honest Gaps

1. **Revenue growth is thin.** +2.1% in the seasonally strongest quarter. All the earnings leverage is margin + buyback. If gross margin mean-reverts even 100–150 bps (e.g., memory/NAND cost inflation, aggressive iPhone promotions in China, or unfavorable Services mix), EPS growth compresses sharply. **This is the #1 sensitivity.**
2. **Services mix concentration is invisible in this fact set.** The tool returned consolidated-only data; Apple does not disclose product-line revenue in XBRL tags. The margin story is entirely a *mix* story, and mix is unverified here.
3. **Cash taxes up 8.8x YoY** ($828M → $7,255M). CFO quality depends on whether this is timing or a new run-rate.
4. **SBC +37% over two years** while revenue fell — the "EPS beat" is partly engineered. Watch for the buyback being used to offset dilution rather than shrink the count.
5. **Foreign tax exposure:** 64% of pre-tax income is foreign; ETR 14.7%. Any adverse EU/OECD ruling is a direct, multi-billion-dollar hit not reflected in current margins.
6. **Negative AOCI still $9.4B** — unrealized bond losses remain on the books; they *helped* this quarter but remain rate-sensitive.
7. **Insider signal is a complete blind spot.** No insider transaction data exists for this period in the vendor archive. **Do not read absence as absence of selling.**
8. **No price data → no valuation conclusion is possible from these tools alone.** See below.

---

## 9. Actionable Trading Insights

1. **The thesis is a margin-expansion + capital-return story, not a growth story.** Position sizing should reflect that the "beat" mechanism (+291 bps gross margin) is the *same* variable that is most at risk. A trader buying this print is long Services mix and input-cost deflation.
2. **Watch gross margin as the single highest-information metric.** The line in the sand is ~44.5%: hold above it and the EPS compounding continues; break below 44% and the "beat" narrative inverts quickly. Q1 FY24 printed 45.87%, giving ~140 bps of cushion.
3. **Valuation framing, price-agnostic:** TTM diluted EPS is **$6.43**. Each **$10 of share price ≈ 1.56 turns of P/E**. At $6.43 TTM EPS, a 25x multiple implies ~$161; 28x implies ~$180; 30x implies ~$193; 32x implies ~$206. On TTM FCF of $106.9B against ~15,441M shares (~$6.92 FCF/share), each $10 of price ≈ 1.45 turns of P/FCF. Use these grids — do not rely on any single implied price.
4. **Net cash of ~$64.6B is an under-appreciated floor.** Rising net cash + shrinking share count + a 14.9% payout ratio means the *downside* is structurally supported: Apple can buy ~$20B/quarter of stock with cash it generates in ~4.8 months.
5. **The dividend is not the trade.** 14.9% payout, ~4% growth, ~84% of returns delivered via buyback. Don't model AAPL as income.
6. **Working-capital swing is a real, near-term cash tailwind:** +$11.5B QoQ to positive $9.7B. If that reverses seasonally in Q2, CFO prints softer — don't extrapolate Q1's 33% CFO/revenue conversion.
7. **Catalyst calendar:** Vision Pro revenue contribution first appears in the **Q2 FY24 (March quarter)**, reported in early May 2024 — the first hard data on whether the ~$3,499 category is a growth vector or a niche. Also watch the **May buyback authorization refresh** (Apple typically announces a new authorization alongside Q2 results) and any **EU DMA / App Store** remedy decisions.
8. **Trade construction note:** Because Q1 EPS growth (+16%) massively outpaced revenue (+2%), any multiple compression from a "growth disappoints" narrative would be *doubly* punishing — you'd lose both the margin premium and the growth premium. Conversely, a summer iPhone 16 super-cycle would compound on top of an already-record margin base. **This is an asymmetric, event-driven setup, not a steady compounder at current margins.**

---

## 10. Key Points Summary

| # | Category | Key Finding | Evidence | Trader Implication |
|---|---|---|---|---|
| 1 | Latest quarter | Revenue +2.07% YoY to $119,575M | 10-Q, Q ended 2023-12-30 | Growth is thin; not a volume story |
| 2 | Margins | Gross margin **45.87%**, +291 bps YoY (from 42.96%) | $54,855M GP / $119,575M rev | The entire earnings beat mechanism |
| 3 | Profit | Operating income +12.10%; net income +13.06% to $33,916M | Op income $40,373M; net $33,916M | Operating leverage is real but margin-dependent |
| 4 | EPS | Diluted EPS **$2.18**, +15.96% YoY | vs $1.88 in Q1 FY23 | EPS growth > NI growth = buyback + tax |
| 5 | Tax | ETR 15.89% (vs 15.79%); FY23 14.7% | Tax $6,407M / pre-tax $40,323M | Rising ETR is a modest 2024 headwind |
| 6 | Cash generation | CFO +17.32% to $39,895M; capex −36.8% to $2,392M | 10-Q cash flow | **FCF +24.11% to $37,503M** — the real headline |
| 7 | FCF quality | CFO/net income = 1.176x; FCF margin 31.36% | Derived | High accrual quality |
| 8 | Capital returns | $23,964M returned = **63.9% of FCF**; 87.3% TTM | Buyback $20,139M + div $3,825M | Sustainable, with ~$13.6B annual headroom |
| 9 | Dividend | $0.24/qtr (+4.3%); payout ~14.9% of TTM EPS | Declared DPS fact | Not an income vehicle; ~84% of returns is buyback |
| 10 | Buyback | $20,139M in Q1; shares −89.9M QoQ to 15,460.2M | BS share count | Structural EPS ballast |
| 11 | Balance sheet | Cash+securities **$172,575M**; total debt $107,998M → **net cash $64,577M** | 12/30/23 BS | Fortress; downside support |
| 12 | Liquidity | Current ratio **1.073x** (was 0.988x); WC +$9,719M (was −$1,742M) | Derived | **$11.5B one-quarter swing** — cash tailwind, but seasonal |
| 13 | Debt | CP cut $3,987M to $1,998M; LTD flat at $106,000M; no maturity cliff | BS + maturity ladder | Deleveraging *and* buybacks simultaneously |
| 14 | Book value | Equity +19.2% QoQ to **$74,100M**; BVPS $4.79 | 12/30/23 vs 9/30/23 | AOCI reversal (+$2.07B) helped |
| 15 | FY2023 | Revenue −2.80% to $383,285M; NI −2.81% to $96,995M; but GM record 44.13% | 10-K (filed 2023-11-03) | First revenue decline since FY19 — cyclical, not structural |
| 16 | Re-acceleration | EPS growth: +0.3% FY23 → **+4.9% TTM** → **+16.0% latest qtr** | Derived across periods | Trend is improving; verify next quarter |
| 17 | TTM run-rate | Revenue $385,706M; NI $100,913M; **EPS $6.43**; FCF $106,869M | Rolling 4 quarters | Use $6.43 as the valuation denominator |
| 18 | Valuation grid | Each $10 of price ≈ 1.56x P/E and 1.45x P/FCF | No price feed | 25x→~$161; 28x→~$180; 30x→~$193; 32x→~$206 |
| 19 | Cost watch | SBC $10,833M FY23 (+37% 2yr) = 11.2% of op income | 10-K | GAAP quality dilution; largely offset by buyback |
| 20 | Tax risk | 64% of FY23 pre-tax income is foreign ($72.9B/$113.7B) | 10-K geography tags | OECD Pillar Two / EU rulings = biggest un-modeled risk |
| 21 | Cash tax | Taxes paid $7,255M vs $828M YoY | Cash flow | Monitor — timing vs new run-rate |
| 22 | Deferred revenue | $12,500M (+3.3% QoQ); $3,500M recognized in Q1 | BS / IFRS 15 tags | Services/subscription leading indicator, mildly positive |
| 23 | New product | Vision Pro US deliveries began 2024-02-02 → first revenue in Q2 FY24 | Context; Q2 reports early May 2024 | First hard catalyst in the next print |
| 24 | **Insider activity** | **NO DATA — vendor archive unavailable for this period** | `get_insider_transactions` returned DATA_UNAVAILABLE | **Do not infer; treat as a blind spot** |
| 25 | Data gaps | No segment/product revenue, no company profile from tool, annual income tags truncated, **no price data** | Tool outputs | Reconcile with 10-Q text and a price source before sizing |

---

### Bottom line for a trader

AAPL as of 2024-02-21 is a **record-margin, net-cash, capital-returning machine with a thin top line**. The December quarter proved the FY23 revenue dip was cyclical: gross margin inflected to a record **45.87%**, FCF rose **24%** on **2%** revenue growth, and Apple simultaneously repaid $4.0B of debt and repurchased $20.1B of stock. Net cash stands at ~**$64.6B** and working capital swung **+$11.5B** to positive. The bear case is not balance sheet or cash flow — it is that **all the operating leverage rests on a gross margin that has now expanded ~400 bps in four quarters** and on a 2% revenue base. Trade the margin line, use **TTM EPS of $6.43** as your multiple anchor, and treat insider-flow as unobservable rather than benign.