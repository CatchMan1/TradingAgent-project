# AMZN — Fundamental Deep-Dive (Point-in-Time: 12-Jan-2024)

**Identity confirmed:** Amazon.com, Inc. — Nasdaq: **AMZN** (3 operating segments tagged in the latest filing: North America, International, AWS).
**Latest filed financials available at this date:** Q3 2023 10-Q (filed **2023-10-27**, accepted 02:36 UTC). **Q4/FY2023 results had not yet been reported** (Amazon reported them 1-Feb-2024, i.e., after today's analysis date). Everything below is therefore "as-known" on 12-Jan-2024 and reflects the twelve months ended **30-Sep-2023**.

---

## 0. Data-quality notes (read first)

Three vendor limitations matter for how much weight to put on individual lines:

1. **The income-statement revenue tag was not returned** (the payload is truncated alphabetically around "O"). I therefore **derived revenue as `CostsAndExpenses + OperatingIncomeLoss`**. This identity reproduces Amazon's publicly reported totals exactly in all four periods where both tags exist (Q3'23 $143,083M; 9M'23 $404,824M; Q3'22 $127,101M; 9M'22 $364,779M), so I treat the derived revenue line as reliable, but it is *derived*, not tagged.
2. **The annual calls returned the same 10-Q dataset** — no 10-K facts are cached. There is no FY2022 10-K income statement, no FY2021/FY2020 history, and no segment-level (NA / Int'l / AWS) revenue or operating-income disclosure in the payload. Multi-year history is limited to what is embedded as comparatives in the two 10-Q filings (Oct-2023 and Aug-2023).
3. **Insider transactions: DATA UNAVAILABLE.** The vendor returned: *"no authorized, point-in-time insider-transactions archive for AMZN by 2024-01-12. Do not infer or fabricate insider activity."* I will not speculate on Form 4 activity. Treat the absence of insider data as a genuine blind spot in this report, not as evidence of no activity.

Additionally, no price, market-cap, share-count-based valuation, consensus estimate, or guidance (8-K) data was returned, so this report contains **no valuation multiple or price target**. It is a business-quality and financial-statement report.

---

## 1. Company profile & business model (context)

Amazon operates a flywheel of three reportable segments: **North America** (1P retail, 3P marketplace commissions/FBA, Prime subscriptions, advertising, physical stores), **International** (same model, ex-US, historically lower-margin and periodically loss-making), and **AWS** (cloud infrastructure, database, AI/ML, plus a fast-growing ads and marketplace-adjacent software layer). The economic engine is not retail gross margin but **(a) high-margin services revenue — AWS, advertising, 3P seller fees, subscriptions — layered on a fixed-cost logistics and data-center base, and (b) the negative-working-capital model**, where customer receipts precede supplier payments (accounts payable and accrued liabilities have historically funded inventory and capex). As of this filing the balance sheet shows the company carrying **substantial operating-lease and finance-lease obligations** (warehouses, fulfillment centers, data centers), which is why reported debt understates true fixed obligations.

---

## 2. Q3 2023 (Jul–Sep): the margin inflection quarter

| Q3 2023 ($M) | Value | Q3 2022 ($M) | Value | Δ |
|---|---|---|---|---|
| Revenue (derived) | 143,083 | Revenue | 127,101 | **+12.6%** |
| Cost of goods & services | 75,022 | | 70,268 | +6.8% |
| **Gross profit** | **68,061** | | **56,833** | +19.8% |
| Gross margin | **47.57%** | | 44.71% | +286 bp |
| Total costs & expenses | 131,895 | | 124,576 | +5.9% |
| **Operating income** | **11,188** | | **2,525** | **+343%** |
| **Operating margin** | **7.82%** | | 1.99% | **+583 bp** |
| Interest expense | (806) | | (617) | +31% |
| Interest income | 776 | | 277 | +180% |
| Non-operating income | 1,001 | | 419 | +139% |
| Pre-tax income | 12,189 | | 2,944 | +314% |
| Tax | 2,306 | | 69 | — |
| **Net income** | **9,879** | | **2,872** | **+244%** |
| Diluted EPS | **$0.94** | | $0.28 | +236% |
| D&A | 12,131 | | 10,327 | +17.5% |
| Stock-based comp | 5,829 | | 5,556 | +4.9% |
| Capex (productive assets) | 12,479 | | 16,378 | **−23.8%** |
| Operating cash flow | 21,217 | | 11,404 | +86% |
| **Free cash flow** | **8,738** | | **(4,974)** | **swing +$13.7B** |

**The single most important fact in this dataset:** operating income grew 4.4× on 12.6% revenue growth. That is a pure cost-structure story, not a demand story. Mechanics:
- **Cost of sales grew only 6.8% vs revenue +12.6%**, worth ~$4.6B of incremental gross profit versus a constant-mix scenario (a 286 bp gross-margin expansion). Drivers consistent with Amazon's 2023 playbook: fulfillment-network regionalization (shorter routes, less cross-country freight), slower headcount growth, and a revenue mix shift toward AWS/ads/3P fees.
- **Total costs & expenses grew 5.9% while revenue grew 12.6%** → ~$9.0B of operating leverage dropped through to operating income.
- **Capex fell 24% y/y** while D&A rose 17.5% → cash conversion improved far faster than earnings.

**Quality-of-earnings caveat (important, and underappreciated):** Q3'23 non-operating income of $1,001M includes **$1,200M of equity-securities fair-value gains** (`EquitySecuritiesFvNiGainLoss`, i.e., mark-to-market on equity stakes) and $776M of interest income, partly offset by $806M of interest expense and $94M of FX losses. Stripping the ~$1.2B pre-tax mark (~$950M after tax), **Q3'23 EPS was closer to $0.85 than $0.94**, and ex-mark operating margin (7.82%) is the clean signal. Q3'22 was similarly flattered by a ~$1.0B gain. Do not model the equity-mark line as recurring.

---

## 3. Nine months to 30-Sep-2023 vs. 9M 2022 (the trend that matters)

| 9M 2023 ($M) | Value | 9M 2022 ($M) | Value | Δ |
|---|---|---|---|---|
| Revenue (derived) | 404,824 | | 364,779 | **+11.0%** |
| COGS | 212,186 | | 203,191 | +4.4% |
| Gross profit | **192,638** | | 161,588 | +19.2% |
| Gross margin | **47.59%** | | 44.30% | **+329 bp** |
| Marketing expense | 31,468 | | 29,420 | +7.0% |
| G&A expense | 8,806 | | 8,558 | +2.9% |
| Asset impairments | 420 | | 350 | +20% |
| Total costs & expenses | 381,181 | | 355,268 | +7.3% |
| **Operating income** | **23,643** | | **9,511** | **+149%** |
| Operating margin | **5.84%** | | 2.61% | **+323 bp** |
| Interest expense | (2,469) | | (1,673) | +48% |
| Interest income | 2,048 | | 544 | **+277%** |
| Equity-securities gains/(losses) | **+1,000** | | **(11,300)** | **+$12.3B** |
| Non-operating income/(expense) | 228 | | (14,485) | — |
| Pre-tax income | 23,871 | | (4,974) | +$28.8B |
| Tax | 4,058 | | (1,990) | — |
| **Net income** | **19,801** | | **(3,000)** | **+$22.8B** |
| Diluted EPS | **$1.89** | | ($0.29) | — |
| D&A | 34,843 | | 29,236 | +19.2% |
| SBC | 17,704 | | 14,015 | +26.3% |
| Capex | 38,141 | | 47,053 | **−18.9%** |
| Operating cash flow | **42,481** | | 17,579 | **+142%** |
| **Free cash flow** | **4,340** | | **(29,474)** | **+$33.8B** |
| Investing cash flow | (37,232) | | (26,780) | — |
| Financing cash flow | (9,133) | | +9,632 | — |
| Share repurchases | **0** | | 6,000 | — |

### The precise earnings bridge (fully reconciled from tool data)
The +$22.8B swing in 9M net income decomposes as follows — and this is the number a trader should internalize:

| Driver | Pre-tax Δ ($M) |
|---|---|
| Operating income improvement | **+14,132** |
| Equity-securities marks (Rivian-type stakes): −11,300 → +1,000 | **+12,300** |
| Net interest income (interest income +1,504, interest expense −796) | +708 |
| FX / other / warrants | +1,705 |
| **Total pre-tax Δ** | **+28,845** |
| Higher cash tax (from −1,990 to +4,058) | **−6,048** |
| **Net income Δ** | **+22,797** |

**Interpretation:** roughly **54% of the earnings improvement is operating**, ~43% is a non-recurring swing in equity marks, and the tax line took back $6.0B. Traders who read the headline "net income swung $22.8B" and extrapolate it will be wrong by roughly half. The **durable** number is operating income: **$14.1B of the improvement, with the margin at 5.84% for 9M'23 versus 2.61%**.

### Sub-margin metrics (9M)
| Metric | 9M 2023 | 9M 2022 |
|---|---|---|
| Gross margin | 47.59% | 44.30% |
| Operating margin | 5.84% | 2.61% |
| Net margin | 4.89% | (0.82%) |
| OCF margin | 10.49% | 4.82% |
| FCF margin | 1.07% | (8.08%) |
| SBC / revenue | 4.37% | 3.84% |
| D&A / revenue | 8.61% | 8.02% |
| Capex / revenue | 9.42% | 12.90% |
| Effective tax rate | 17.0% | n/a (loss) |
| EBIT / interest | 9.6× | 5.7× |

**Read:** operating margin expansion (+323 bp) is being *partly consumed* by rising depreciation (+59 bp of revenue) and SBC (+53 bp). That is the right kind of consumption — it's the amortization of prior AI/logistics investment coming online — but it means **the margin ceiling depends on capex continuing to decelerate relative to D&A**. If capex re-accelerates for AI infrastructure, the D&A drag grows again with a lag.

---

## 4. Trailing-twelve-month view (Oct-2022 → Sep-2023, directly tagged rolling periods)

| TTM metric | Value |
|---|---|
| Revenue (derived: FY22 $513.98B* − 9M22 $364.78B + 9M23 $404.82B) | **~$554.0B** |
| Net income (`NetIncomeLoss`, 12-mo tag) | **$20,079M** (3.6% margin) |
| Operating cash flow (12-mo tag) | **$71,654M** |
| Capex (12-mo tag) | **$54,733M** |
| **Free cash flow** | **$16,921M** (3.1% of revenue) |
| D&A (12-mo tag) | **$47,528M** |
| Cash taxes paid (12-mo tag) | $8,677M |
| Deferred tax benefit (12-mo tag) | ($7,779M) |

\*FY2022 total revenue is the widely reported figure; it is not in the returned payload but is required for the residual Q4'22 calc, so I flag it explicitly.

**The critical trajectory in capex:** TTM capex of $54.7B compares with **$58.6B for the TTM ended Jun-2023** and **$65.99B for the TTM ended Sep-2022**. Meanwhile TTM D&A rose from $39.1B (TTM Sep-2022) to **$47.5B**. The capex-to-D&A ratio has collapsed from **1.69× to 1.15×** in twelve months. **This ratio, not revenue growth, is what re-rated Amazon's free cash flow in 2023** — and it is the metric to monitor each quarter. At 1.15×, capex is still above D&A, so FCF is not yet structurally "clean," but the direction is unambiguous.

---

## 5. Balance sheet (30-Sep-2023 vs 31-Dec-2022)

| $M | 30-Sep-23 | 31-Dec-22 | Δ |
|---|---|---|---|
| Cash & equivalents | 49,605 | 53,888 | −7.9% |
| Marketable securities (AFS, fair value) | **49,871** | n/a in payload | — |
| **Cash + marketable securities** | **~99,476** | n/a | — |
| Accounts receivable (net) | 43,420 | 42,360 | +2.5% |
| Inventory (net) | 35,406 | 34,405 | **+2.9%** |
| Total current assets | 142,995 | 146,791 | −2.6% |
| **Total assets** | **486,883** | **462,675** | **+5.2%** |
| Accounts payable | **72,004** | **79,600** | **−9.5%** |
| Accrued liabilities | 58,812 | 62,566 | −6.0% |
| Total current liabilities | 145,214 | 155,393 | −6.6% |
| Long-term debt — current | 5,995 | 2,999 | +99.9% |
| Long-term debt — noncurrent | 61,098 | 67,150 | −9.0% |
| **Total long-term debt** | **67,472** | **70,542** | **−4.4%** |
| Finance lease liabilities | 12,466 | 15,783 | −21.0% |
| Operating lease liabilities | 73,902 | 69,040 | +7.0% |
| Deferred revenue (contract liabilities) | 17,098 | 16,127 | +6.0% |
| Additional paid-in capital | 92,711 | 75,066 | **+23.5%** |
| Accumulated OCI | (5,003) | (4,487) | worse |
| Shares outstanding | 10,330M | 10,242M | **+0.86%** |
| Shares issued | 10,845M | 10,757M | +0.82% |

### Derived leverage & liquidity
| Metric | 30-Sep-23 |
|---|---|
| Current ratio | **0.985** (0.945 at 12/31/22) |
| (Cash + securities) / current liabilities | **0.685** |
| Net debt (LT debt + finance leases − cash − securities) | **net CASH of ~$19.5B** |
| Net debt incl. operating leases | **~$54.4B ≈ 0.76× TTM OCF** |
| Total undiscounted obligations: purchase obligations | **$284,407M** (next 12 mo: $35,712M) |
| + operating lease payments due | $88,814M (next 12 mo: $9,977M) |
| + finance lease payments due | $14,574M (next 12 mo: $2,178M) |
| AFS unrealized position | amortized $50,377M vs FV $49,871M → **~$0.5B unrealized loss (1.0%)** |

**Three balance-sheet insights that are genuinely actionable:**

1. **Accounts payable fell $7.6B (−9.5%) while revenue rose 11%.** This is the supplier-payment normalization (Amazon shortened payables in 2023 as part of its cost-of-serve overhaul). It is a **cash headwind that flattered prior-year OCF and now reverses** — 9M'23 OCF of $42.5B was achieved *despite* this ~$7.6B payables drain plus a $9.0B drag from accrued liabilities. Underlying cash generation is therefore materially better than the $42.5B headline. Payables as a share of COGS: 72,004 / (TTM COGS ≈ $285B) ≈ 25% — still structurally high, so the negative-working-capital model is intact, just less aggressive.
2. **The company is in a net-cash position on a debt-plus-finance-lease basis (~$19.5B)** while carrying $73.9B of operating-lease liabilities. It issued **zero long-term debt in 2023** (vs $8.2B in the TTM to Sep-2022) and made **$3.4B of LT repayments**. Combined with $99.5B of cash and securities, this is a fortress position — Amazon has funded the entire 2023 capex program ($38.1B) and debt paydown out of operating cash flow. Financial risk is essentially nil; the risk here is *equity duration*, not solvency.
3. **Inventory grew 2.9% against revenue +11%** — inventory days falling, no obsolescence build (reserve actually declined $2.8B → $2.6B). This corroborates the "cost-to-serve" narrative from the income statement; it is not just accounting.

**Dilution:** shares out rose 0.86% in nine months with **$0 of buybacks** (vs $6.0B repurchased in 9M'22). APIC rose $17.6B, essentially matching 9M SBC of $17.7B. Annualized dilution is ~1.1–1.2%, and $23.3B of unrecognized SBC remains to be expensed. This is a real, persistent ~1% annual headwind to per-share value and a change from the 2022 posture.

---

## 6. Cash-flow anatomy (9M 2023) — why $42.5B is higher quality than it looks

| $M | 9M 2023 |
|---|---|
| Net income | 19,801 |
| + D&A | 34,843 |
| + SBC | 17,704 |
| − Deferred tax benefit | (4,412) |
| Sub-total (non-cash-adjusted earnings) | **67,936** |
| − Working capital & other (AR/other assets, accrued liabilities, payables, equity marks, impairments) | **(25,455)** |
| = **Operating cash flow** | **42,481** |
| − Capex | (38,141) |
| = **Free cash flow** | **4,340** |
| − Finance lease principal payments | (3,605) |
| = FCF after lease principal | **735** |

Cash conversion (OCF/NI) = **2.1×** — exceptionally high, but that is the arithmetic signature of a capital-intensive business mid-depreciation-cycle, not a sign of accounting aggression. The honest framing: **FCF of $4.3B is thin in absolute terms because $54.7B of trailing capex still exceeds $47.5B of D&A.** Net income of $19.8B understates cash earnings; FCF of $4.3B overstates the squeeze. The truth is a business generating roughly **$68B of pre-capex cash** and choosing to reinvest ~$55B of it.

Financing detail: 9M'23 proceeds from short-term debt $17.4B vs repayments $19.3B (net **−$1.9B**); LT repayments $3.4B; **no LT issuance**; **no buyback**; no dividends.

---

## 7. Risks, red flags, and what would break the thesis

| # | Risk / red flag | Evidence in the data | Why it matters for a trader |
|---|---|---|---|
| 1 | **~43% of the 9M earnings swing is non-operating** | Equity marks −$11,300M → +$1,000M; Q3 alone +$1,200M pre-tax | Mean-reverting. Consensus extrapolating EPS will over-earn. Watch the "other income" line each quarter. |
| 2 | **Tax normalization** | 9M'23 tax $4,058M (17.0% rate) vs a $1,990M *benefit* in 9M'22; $4.4B deferred benefit + $0.6B R&D credit helped 2023 | The 2022–23 tax holiday is ending. Forward EPS growth is taxed at a real ~17–20% rate. |
| 3 | **Payables reversal** | AP −$7.6B (−9.5%) in 9M despite revenue +11% | One-off cash headwind already absorbed, but limits further OCF "surprise" from working capital. |
| 4 | **Capex re-acceleration for AI** | Capex down 19% y/y, but $284.4B of purchase obligations (incl. AWS capacity/content) outstanding | The entire FCF re-rating rests on capex/D&A staying near 1.15×. A GenAI capex step-up resets the story. |
| 5 | **Persistent dilution, no buyback** | Shares +0.86% in 9M; $0 repurchased; $23.3B unrecognized SBC | ~1%+ annual per-share leakage with no offsetting capital return. |
| 6 | **No segment data in this payload** | Segments = 3, but NA/Int'l/AWS revenue and operating income absent | **AWS growth and AWS margin are the swing factors for the stock and cannot be assessed from this data.** Genuine gap. |
| 7 | **Balance-sheet opacity on equity** | Stockholders' equity line not tagged; only APIC/AOCI/assets available | Equity cannot be computed from the payload (needs total liabilities/retained earnings). Data gap, not a red flag. |
| 8 | **Q4/FY2023 print pending** | Latest filing 30-Sep-23; Q4 reported 1-Feb-2024 | Any position taken today is a bet on an unreported holiday quarter and on 2024 capex guidance. |
| 9 | **Negative AOCI, AFS in unrealized loss** | AOCI −$5,003M; AFS FV $49,871M vs cost $50,377M | Small (~1%), but duration risk if rates back up. |
| 10 | **Current ratio < 1.0** | 0.985 | Not a liquidity problem given $99.5B cash+securities and $71.7B TTM OCF — but it means the model depends on continuous supplier terms and rolling short-term paper ($17.4B drawn in 9M'23). |

---

## 8. Insider transactions

**Unavailable.** The vendor explicitly returned no authorized point-in-time insider-transactions archive for AMZN as of 2024-01-12, with an instruction not to infer or fabricate. I have **no** view on insider buying or selling for this date, and I would not treat a zero result as meaning "no insider activity." Anyone acting on this report should source Form 4 data independently before drawing any conclusion about management sentiment.

---

## 9. Actionable conclusions

**Bull case (strongly supported by this data):**
- The **operating-margin regime change is real and cash-backed**: operating margin 2.61% → 5.84% over nine months on 11% revenue growth, with COGS growing at less than half the rate of revenue (+4.4% vs +11.0%). This is cost-of-serve improvement, corroborated by inventory growth (+2.9%) decelerating well below revenue.
- **The FCF inflection is the trade**: FCF $4.3B in 9M'23 vs −$29.5B in 9M'22; Q3 alone $8.7B vs −$5.0B. TTM FCF $16.9B. The capex/D&A ratio moving from 1.69× to 1.15× is the mechanical driver and is observable every quarter.
- **Balance-sheet optionality**: ~$19.5B net cash (ex-operating leases), $99.5B liquidity, zero LT issuance, $3.4B LT repaid, 0.76× net-debt/OCF including leases. Interest income ($2.0B, +277%) now nearly offsets interest expense ($2.5B) — a structural tailwind that did not exist in 2021.
- **Positioning into the 1-Feb-2024 print**: the setup favors an expectation that Q4 operating margin holds at/above the high-6% range achieved in Q3, with the watch item being guidance on 2024 capex.

**Bear case / what to fade:**
- **Do not underwrite the $19.8B 9M net income as recurring.** Strip $1.0B of equity marks and the deferred-tax benefit and the "clean" earnings base is meaningfully lower; ~43% of the y/y improvement was a mark-to-market swing that cannot repeat from a $1B base.
- **Watch for FCF disappointment from capex guidance.** If AI infrastructure spending pushes 2024 capex back above D&A growth, the FCF re-rating that drove 2023 stalls, and the market will re-price the equity on a lower FCF yield. This is the highest-probability negative catalyst.
- **Dilution without buyback** is a slow tax; the 2022 $6B repurchase was not repeated.

**Specific monitoring checklist (next filing, 1-Feb-2024):**
1. Capex for Q4/FY23 and 2024 guidance → check capex/D&A against 1.15×.
2. AWS revenue growth and AWS operating margin (the payload cannot supply these; must be sourced externally).
3. Equity-securities fair-value line → quantify and strip from EPS.
4. Effective tax rate → confirm 17–20% normalized.
5. Accounts payable balance → has the payables drain stabilized near $72B?
6. Share count → is dilution still ~1%+ annualized with no repurchase authorization used?
7. Operating-lease liability ($73.9B) and purchase obligations ($284.4B) → growth signals for capacity commitments.

**Bottom line:** As of 12-Jan-2024, AMZN's fundamental data show a company that has completed a genuine, cash-flow-confirmed margin and capital-efficiency turnaround over the prior four quarters, funded entirely from internal cash flow, with an unlevered-quality balance sheet and one clear swing factor (capex discipline) that determines whether free cash flow compounds or stalls. The principal analytical trap is that roughly half the reported earnings improvement is non-operating and tax-mechanical. The principal data gaps in this report are insider activity, segment-level AWS/North America detail, and any price-based valuation.

---

## 10. Key points summary

| Category | Metric | Value / Detail | Read |
|---|---|---|---|
| **Identity** | Ticker / company | **AMZN** — Amazon.com, Inc. (Nasdaq) | 3 operating segments |
| **Filing basis** | Latest filing at 2024-01-12 | Q3 2023 10-Q, filed 2023-10-27 | Q4/FY23 not yet reported (1-Feb-24) |
| **Revenue** | Q3 2023 (derived) | $143,083M | +12.6% y/y |
| | 9M 2023 (derived) | $404,824M | +11.0% y/y |
| | TTM | ~$554.0B | Derivation flagged |
| **Profitability** | Q3'23 operating income / margin | $11,188M / **7.82%** | vs 1.99% in Q3'22 |
| | 9M'23 operating income / margin | $23,643M / **5.84%** | vs 2.61%; +$14.1B y/y |
| | 9M'23 gross margin | **47.59%** | +329 bp y/y |
| | Q3'23 net income / diluted EPS | $9,879M / **$0.94** | ~$0.85 ex-equity marks |
| | 9M'23 net income / diluted EPS | $19,801M / **$1.89** | vs −$3,000M / −$0.29 |
| | TTM net income | **$20,079M** | 3.6% margin |
| **Earnings quality** | Equity-securities marks 9M | **+$1,000M vs −$11,300M** | +$12.3B of the $22.8B swing |
| | Effective tax rate 9M'23 | **17.0%** | vs a $1,990M benefit in 9M'22 |
| | Bridge: operating vs other | +$14.1B operating; +$12.3B marks; −$6.0B tax | ~54% operating |
| **Cash flow** | Q3'23 OCF / FCF | $21,217M / **$8,738M** | FCF swing +$13.7B y/y |
| | 9M'23 OCF / FCF | $42,481M / **$4,340M** | vs $17,579M / −$29,474M |
| | TTM OCF / capex / FCF | $71,654M / $54,733M / **$16,921M** | 3.1% FCF margin |
| | TTM D&A | $47,528M | Capex/D&A **1.15×** (was 1.69×) |
| **Capex** | 9M'23 capex | $38,141M | **−18.9% y/y** |
| | Q3'23 capex | $12,479M | −23.8% y/y; 8.7% of sales |
| **Balance sheet** | Cash + marketable securities | **~$99,476M** | 49,605 cash + 49,871 AFS |
| | Total LT debt | $67,472M | −4.4% vs 12/31/22; **$0 new LT issuance** |
| | Finance leases | $12,466M | −21.0% |
| | Operating leases | **$73,902M** | +7.0% |
| | Net debt ex-operating leases | **net CASH ~$19.5B** | Fortress |
| | Net debt incl. operating leases | ~$54.4B ≈ 0.76× TTM OCF | Manageable |
| | Total assets | $486,883M | +5.2% |
| | Current ratio | 0.985 | vs 0.945 |
| | Accounts payable | $72,004M | **−9.5%** despite revenue +11% |
| | Inventory | $35,406M | +2.9% vs revenue +11% → efficiency gain |
| | Deferred revenue | $17,098M | +6.0% |
| | AOCI | −$5,003M | AFS ~$0.5B unrealized loss (1.0%) |
| | Purchase obligations | **$284,407M** | $35,712M due within 12 months |
| **Capital return** | Buybacks 9M'23 | **$0** | vs $6,000M in 9M'22; no dividend |
| | Dilution | shares **+0.86%** to 10,330M | ~1.1% annualized; $23.3B unrecognized SBC |
| **Coverage** | EBIT / interest 9M'23 | 9.6× | vs 5.7× |
| **Insiders** | Form 4 activity | **DATA UNAVAILABLE** | Not inferred or fabricated |
| **Data gaps** | Revenue tag, segment splits (NA/Int'l/AWS), equity line, FY history, price/valuation | Not returned by vendor | Derived revenue validated vs reported totals |
| **Primary catalyst** | Q4/FY2023 results | **1-Feb-2024** | Watch capex guide, AWS, equity marks, tax |