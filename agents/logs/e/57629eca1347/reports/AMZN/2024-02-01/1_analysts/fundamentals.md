# AMZN — Fundamental Deep Dive (as of 2024-02-01)

**Ticker:** AMZN · **Company:** Amazon.com, Inc. · **Fiscal year end:** Dec 31 · **Sector:** Consumer Discretionary / E-commerce + Cloud (AWS)

---

## 1. Data Provenance, Vintage & Gaps (read first)

**Vintage note — this is a "just-printed" dataset.** Every fact below comes from Amazon's FY2023 Form 10-K (accession `0001018724-24-000008`), with an EDGAR acceptance timestamp of **2024-02-02 04:48 UTC**. Amazon released Q4/FY2023 results after the close on **2024-02-01**. So the numbers I'm analyzing are the freshest possible print — but the formal 10-K text landed in EDGAR hours *after* the 2024-02-01 analysis date. Treat these as the "night-of-earnings" figures, not yet market-fully-digested.

**Coverage gaps I must flag (do not assume):**
- **No `Revenues` tag was returned.** I derive revenue from the identity `Revenue = CostsAndExpenses + OperatingIncomeLoss`. This reconstructs to $574.785B / $513.983B / $469.822B for FY2023/22/21 — internally consistent and matching the cost build-down. All revenue-based ratios therefore rest on a derived figure, though a robust one.
- **No segment-level detail** (North America / International / AWS revenue, AWS operating income, AWS backlog). Only `NumberOfOperatingSegments = 3` is available. This is the single biggest analytical hole for AMZN.
- **No quarterly granularity** was returned despite quarterly requests — the vendor served annual facts. I reconstructed *some* Q4-2023 cash flow from the 10-Q cumulative figures (shown below).
- **No inventory, no goodwill line, no headcount** in the fact set.
- **No price data** — I deliberately avoid quoting a share price or market cap. All valuation commentary is framed as sensitivity.

---

## 2. Company Profile

Amazon.com, Inc. reports **three operating segments** (`NumberOfOperatingSegments = 3`):

| Segment | Nature of business | Economics |
|---|---|---|
| **North America** | Online + physical retail, third-party marketplace, advertising, Prime subscriptions, devices | High volume, structurally thinner margins, improving with fulfillment regionalization |
| **International** | Same model outside US/Canada | Long-term loss-maker turning toward profitability |
| **AWS** | Cloud infrastructure, database, analytics, AI/ML services | Highest-margin, highest-ROIC engine; funds the retail build-out |

**Business model characteristics evidenced in the filings:**
- **Negative cash conversion cycle.** FY2023: accounts payable of $84,981M against COGS of $304,739M implies **~102 AP days**, versus receivables of $52,253M on $574,785M revenue (**~33 AR days**). Payables finance receivables and inventory — supplier float is a structural funding source, which is why Amazon can run negative free cash flow for years without distress.
- **Heavy fixed-asset intensity that is now decelerating.** Capex fell 17.2% in FY2023 to $52,729M, the first meaningful pullback after the 2021–22 logistics over-build.
- **Large, growing deferred-revenue base** (Prime + AWS prepayments): contract liabilities $20,600M (+28% YoY).
- **Scale:** 10,383M shares outstanding at 2023-12-31; 10,387,381,291 as of 2024-01-24; public float of **$1,183.7B** at 2023-06-30. Shareholder base is fully public — no controlling holder.

---

## 3. Income Statement — The Margin Inflection Is the Whole Story

| $ millions | FY2021 | FY2022 | FY2023 | YoY Δ |
|---|---:|---:|---:|---:|
| **Revenue (derived)** | 469,822 | 513,983 | **574,785** | **+11.8%** |
| Cost of goods & services | 272,344 | 288,831 | 304,739 | +5.5% |
| **Gross profit** | 197,478 | 225,152 | **270,046** | **+19.9%** |
| *Gross margin* | *42.03%* | *43.81%* | ***46.98%*** | *+317 bp* |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| **Operating income** | 24,879 | 12,248 | **36,852** | **+200.9%** |
| *Operating margin* | *5.29%* | *2.38%* | ***6.41%*** | *+403 bp* |
| Non-operating income/(expense) | 13,272 | (18,184) | 705 | n.m. |
| Pre-tax income | 38,151 | (5,936) | 37,557 | n.m. |
| Income tax expense/(benefit) | 4,791 | (3,217) | 7,120 | n.m. |
| **Net income** | 33,364 | (2,722) | **30,425** | n.m. |
| *Net margin* | *7.10%* | *-0.53%* | ***5.29%*** | |
| **Diluted EPS** | 3.24 | (0.27) | **2.90** | n.m. |
| Diluted shares (implied) | ~10,297 | ~10,189 | ~10,491 | +3.0% |

### Three findings that matter

**(a) Operating income tripled year-over-year — and this is durable, not a one-off.**
FY2023 operating income of $36,852M is **+200.9%** over FY2022's $12,248M. Critically, this is *pure operating* performance: non-operating income contributed only **$705M** in FY2023, versus **$13,272M** in FY2021. That distinction is essential —

**(b) FY2023 net income of $30,425M is far higher quality than FY2021's $33,364M.**
FY2021's headline was inflated by **$11,600M of unrealized equity-securities gains** (the Rivian mark-up) inside a $13,272M non-operating line. Strip that out and FY2021's operating profit was $24,879M. FY2023 delivered **$36,852M of operating profit — 48% above FY2021's real operating engine — while booking almost nothing non-operating.** Conversely, FY2022's $2,722M loss was as much a *mark-to-market* problem (−$13,600M equity losses) as an operating one; the genuine FY2022 problem was the collapse to a **2.38%** operating margin. That has now fully reversed and then some.

**(c) The margin recovery is roughly *half* gross margin, *half* operating leverage.**

| Component | FY2021 | FY2022 | FY2023 | Δ vs 2022 |
|---|---:|---:|---:|---:|
| Gross margin | 42.03% | 43.81% | 46.98% | +317 bp |
| Operating expense ratio | 36.74% | 41.42% | 40.57% | −85 bp |
| **Operating margin** | **5.29%** | **2.38%** | **6.41%** | **+403 bp** |

Gross margin expansion of 317bp reflects mix shift toward advertising/AWS/third-party services and a leaner cost-to-serve (regionalized fulfillment). The 85bp of opex leverage came from discipline across the P&L:

| Operating expense line | FY2021 | FY2022 | FY2023 | YoY Δ |
|---|---:|---:|---:|---:|
| Marketing | 32,551 | 42,238 | 44,370 | +5.0% |
| General & administrative | 8,823 | 11,891 | 11,816 | **−0.6%** |
| Advertising (traffic-driving) | 16,900 | 20,600 | 20,300 | **−1.5%** |
| Stock-based compensation | 12,757 | 19,621 | 24,023 | +22.4% |
| Depreciation, depletion & amortization | 34,433 | 41,921 | 48,663 | +16.1% |
| Operating lease cost | 7,199 | 8,847 | 10,550 | +19.2% |

**Actionable read:** G&A and advertising spend were *cut in absolute dollars* in FY2023 while revenue grew 11.8%. That is real cost extraction, not accounting. However, opex leverage was *partially offset* by SBC (+22.4%) and D&A (+16.1%) — both growing faster than revenue — and operating lease cost (+19.2%). This means **the FY2023 margin print is not fully "clean" operating leverage**; roughly a third of the improvement came from temporary restraint in discretionary spend that management can re-accelerate.

---

## 4. Cash Flow — The FCF Swing Is the Trade

| $ millions | FY2021 | FY2022 | FY2023 | Δ YoY |
|---|---:|---:|---:|---:|
| **Operating cash flow** | 46,327 | 46,752 | **84,946** | **+81.7%** |
| *OCF margin* | *9.86%* | *9.10%* | ***14.78%*** | *+568 bp* |
| Capex (productive assets) | (61,053) | (63,645) | **(52,729)** | **−17.2%** |
| **Free cash flow (OCF − capex)** | **(14,726)** | **(16,893)** | **+32,217** | **+49,110** |
| *FCF margin* | *−3.13%* | *−3.29%* | ***+5.60%*** | *+889 bp* |
| Investing cash flow | (58,154) | (37,601) | (49,833) | −32.5% |
| Financing cash flow | 6,291 | 9,718 | (15,879) | n.m. |
| D&A add-back | 34,433 | 41,921 | 48,663 | +16.1% |
| SBC add-back | 12,757 | 19,621 | 24,023 | +22.4% |
| Cash taxes paid | 3,688 | 6,035 | 11,179 | **+85.2%** |
| Δ unearned revenue | +2,314 | +2,216 | +4,578 | +107% |

**This is a >$49B swing in free cash flow in twelve months.** Amazon went from burning $16.9B in FY2022 to generating $32.2B in FY2023. Decomposing the driver:

1. **+$38.2B from operations** (OCF $46.8B → $84.9B), of which roughly $6.7B is mechanically higher D&A add-back and $4.4B higher SBC add-back — i.e. **~$27B is genuine working-capital and profitability conversion** (mostly AP growth +$5.4B, unearned revenue +$4.6B, and the $48B earnings swing).
2. **+$10.9B from capex discipline** (−17.2%).

**Quarterly nuance from the Q3-2023 10-Q, reconstructed:** 9M-2023 OCF was $42,481M and capex $38,141M, implying **Q4-2023 alone delivered OCF of $42,465M and FCF of $27,877M.** A single quarter produced 87% of the full year's free cash flow. That is extreme seasonality and a reminder that **Q4 is the quarter that makes or breaks the year** — a Q4 miss would gut the FCF narrative.

**Two warnings embedded in the cash flow statement:**
- **Cash taxes jumped 85% to $11,179M** while book tax expense was only $7,120M. Cash taxes are running at **1.57× book**, an effective cash rate of ~29.8% vs an 18.96% book rate. As loss carryforwards exhaust (domestic NOL DTA only $610M; foreign $2,796M), the cash tax rate will converge toward the ~21%+ statutory level. **This is a structural headwind to future FCF growth that the FY2023 print flatters.**
- **Working capital flipped from a tailwind to a modest drag in liabilities:** accrued liabilities and other operating liabilities contributed **−$2,428M** in FY2023 and **−$1,558M** in FY2022, after a **+$2,123M** contribution in FY2021. The easy payables float expansion is behind us.

**Earnings quality check: OCF / Net income = 84,946 / 30,425 = 2.79×.** That is unusually high and is the direct signature of $48.7B of non-cash D&A and $24.0B of SBC. Net income converts to cash very well; the company is **not** an accrual-accounting story.

---

## 5. Balance Sheet — Fortress, With a Negative Cash Cycle

| $ millions | 2021-12-31 | 2022-12-31 | 2023-12-31 | YoY Δ |
|---|---:|---:|---:|---:|
| Cash & equivalents | 36,477* | 53,888 | **73,387** | +36.2% |
| Marketable securities (AFS, fair value) | n/a | n/a | **70,919** | — |
| **Total cash + securities** | — | — | **144,306** | — |
| Accounts receivable, net | — | 42,360 | 52,253 | +23.4% |
| **Total current assets** | — | 146,791 | **172,351** | +17.4% |
| Total assets | 420,549 | 462,675 | **527,854** | +14.1% |
| Accounts payable | — | 79,600 | 84,981 | +6.8% |
| Accrued liabilities | — | 62,566 | 64,709 | +3.4% |
| Contract liabilities (current) | — | 13,227 | 15,227 | +15.1% |
| Contract liabilities (non-current) | — | 2,900 | 5,700 | **+96.6%** |
| **Total current liabilities** | — | 142,266 | **164,917** | +15.9% |
| Long-term debt (carrying) | — | 67,150 | **58,314** | **−13.2%** |
| Finance lease liabilities | — | 15,783 | 12,109 | −23.3% |
| Operating lease liabilities | — | 69,040 | 75,639 | +9.6% |
| Total shareholders' equity | 138,245 | 146,043 | **201,875** | **+38.2%** |
| Total liabilities | — | 316,632 | 325,979 | +3.0% |

*\*2021 figure is cash + restricted cash per the cash-flow reconciliation; the AFS securities balance for 2021/2022 was not returned by the tool.*

### Liquidity & solvency metrics (FY2023)

| Metric | Value | Read |
|---|---:|---|
| Current ratio | **1.05×** | Thin on paper — but see below |
| Quick ratio (cash+securities+AR)/CL | **1.19×** | Comfortable |
| Cash & securities / total assets | **27.3%** | Very liquid |
| Total debt / equity | **0.29×** | Conservative |
| Net cash (cash+sec − debt − finance leases) | **+$73,883M** | Net cash, not net debt |
| Debt / EBITDA (EBIT + D&A = $85,515M) | **0.68×** | Under-levered |
| EBIT / interest expense | **11.6×** | Strong coverage |

**Why the 1.05× current ratio is not a red flag:** $84,981M of the $164,917M current liabilities is accounts payable — non-interest-bearing supplier float generated by the retail business itself, not a financing obligation. Excluding AP, the current ratio is a healthy **2.15×**.

**The liability that gets ignored: operating leases of $75,639M** (undiscounted payments $90,777M). Add that and gross obligations reach **~$146B against ~$144B of liquid assets** — essentially fully hedged, but it means Amazon is *not* sitting on a vast cash cushion once lease commitments are honestly counted. The $300,409M total contractual obligation figure (below) makes this more acute.

**Equity growth of 38.2% ($55.8B) breaks down as:** +$23,959M additional paid-in capital (SBC issuance), +$30,425M retained earnings (net income), +$1,447M AOCI improvement. Amazon is funding itself almost entirely through stock compensation and organic profit — no equity raise, no net new debt.

**Interest dynamics — a quiet positive:** interest expense rose to $3,182M (+34.4%) despite debt *falling* 13.2% (higher rates + mix), but **interest income surged to $2,949M (+198%)** on the larger securities book. Net interest cost collapsed from −$1,378M to **−$233M**. Higher-for-longer rates are now roughly neutral for Amazon, not a drag.

---

## 6. Capital Allocation & Leverage

| $ millions | FY2021 | FY2022 | FY2023 | Comment |
|---|---:|---:|---:|---|
| Capex | 61,053 | 63,645 | 52,729 | **−17.2%**; the FCF lever |
| Share repurchases | 0 | 6,000 | **0** | Buyback fully paused |
| LT debt issued | 19,003 | 21,166 | **0** | No new term debt |
| LT debt repaid | 1,590 | 1,258 | 3,676 | Deleveraging |
| ST debt issued | 7,956 | 41,553 | 18,129 | Commercial paper down |
| ST debt repaid | 7,753 | 37,554 | 25,677 | Net ST reduction −$7,548M |
| Finance lease principal payments | 11,163 | 7,941 | 4,384 | Shrinking rapidly |
| Operating lease payments | 6,722 | 8,633 | 10,453 | Growing (+21%) |

**Read:** Amazon spent FY2023 **paying down debt and generating cash rather than returning it.** $0 of buybacks and $0 of dividends in FY2023 (after a token $6.0B buyback in FY2022). With $32.2B of FCF, $144.3B of liquid assets and 0.29× debt/equity, the balance sheet has substantial **capacity to buy back stock or make an acquisition** — and $18,300M of unrecognized SBC plus a 4.2%-of-revenue annual SBC run rate means **a buyback would be the single most accretive signal management could send.** Its absence is a mild negative for per-share value.

**Debt maturity ladder (as of 2023-12-31) is well-laddered and easily covered:**

| Year | LT debt maturities |
|---|---:|
| Next 12 months | $8,500M |
| Year 2 | $5,286M |
| Year 3 | $3,146M |
| Year 4 | $8,750M |
| Year 5 | $2,250M |
| After year 5 | $39,250M |

Next-twelve-month maturities of $8,500M are covered **17× over** by cash alone.

---

## 7. Quality of Earnings — What to Discount

| Item | FY2023 | Assessment |
|---|---:|---|
| Non-operating income | $705M | **Minimal** — clean, in stark contrast to FY2021's $13,272M |
| Equity securities FV gains | $1,000M | ~3.3% of net income; modest tailwind |
| Foreign-currency transaction gain | $65M | Negligible |
| Book effective tax rate | **18.96%** | Below 21% statutory |
| — Tax credits recognized | $2,362M | Recurring but elevated (vs $1,006M FY2022) |
| — Deferred tax benefit | **−$5,876M** | Timing; non-cash benefit |
| Cash taxes paid | $11,179M (**29.8%** of pretax) | **The real number** — and it's rising |
| SBC expense | $24,023M (4.18% of rev) | **Real economic cost**; +22.4% YoY |
| Unrecognized SBC (future expense) | $18,300M | Will suppress future GAAP EPS |
| Diluted share count growth | +3.0% | SBC dilution; no buyback offset |

**Verdict: high-quality earnings with two identifiable haircuts.** (1) The 18.96% book tax rate is *not* sustainable — cash taxes already run at ~30% of pretax, and the gap of $4,059M is a non-cash deferred benefit. Normalizing the tax rate to ~24% would reduce FY2023 net income by roughly **$1.9B** to ~$28.5B. (2) SBC of $24.0B is genuine compensation and dilution (shares +3.0%); an EV/NOPAT view must treat it as a cost. Even after both adjustments, the underlying operating story is intact.

**Red/yellow flags to monitor:**
- **Receivables +23.4% vs revenue +11.8%** — AR days stretched from 30.1 to 33.2. Ads and AWS billing mix explain some, but it is two quarters of receivables outrunning sales. Allowance for doubtful accounts rose only $1.4B→$1.7B, so credit quality is not the issue — collections timing is.
- **Accrued liabilities contributed a $2,428M cash *use*** — Amazon is paying down accruals, not stretching them.
- **Deferred tax liability on PP&E jumped $9,039M → $12,454M (+38%)** — consistent with aggressive depreciation timing/deregionalization of assets. Watch for a depreciation catch-up.
- **No goodwill line returned**, but finite-lived intangibles grew $7,135M → $8,935M gross with accumulated amortization only $2,395M — Amazon is still acquiring (this is unusual for a company generating this much cash) and amortization will build (+$706M in FY2023, with $715M scheduled for next year and $3,545M after year five). Amplitude is small relative to earnings.

---

## 8. Forward-Looking Indicators Buried in the Filing

These are the highest-signal, most-ignored data points in the 10-K:

| Indicator | 2022-12-31 | 2023-12-31 | Change | Interpretation |
|---|---:|---:|---:|---|
| Total contract liabilities (unearned revenue) | 16,100 | **20,600** | **+28.0%** | **Bullish.** Prime + AWS prepayments growing 2.4× faster than revenue. Forward demand visibility improving. |
| — Non-current portion | 2,900 | 5,700 | **+96.6%** | Multi-year AWS commitments lengthening — this is the leading edge of backlog. |
| Revenue recognized from prior-year deferred balance | — | 12,400 | — | 77% of opening deferred revenue converted to revenue within the year — high-quality, fast-converting bookings. |
| **Total contractual obligations** | — | **300,409** | — | **Critical.** Purchase + lease + debt commitments. $39,345M due within 12 months; **$157,824M due after year five.** Signals a **capex/infrastructure re-acceleration ahead** — likely AI/data-center build. If so, the FY2023 capex cut that powered the FCF beat is a **one-year phenomenon**. |
| SBC not yet recognized | — | 18,300 | — | Weighted-average ~3 years of future expense; a persistent EPS drag. |
| Investment tax credits | 1,006 | 2,362 | +135% | Likely semiconductor/clean-energy credits — a recurring, growing tax shield. |

**The single most important forward read:** the **$300.4B contractual obligation book with $157.8B beyond year five** is inconsistent with a permanently lower capex regime. Traders extrapolating FY2023's 9.2% capex/revenue ratio into FY2024–25 are likely to be disappointed. **The FCF inflection is real, but its magnitude may not repeat.**

---

## 9. Insider Transactions

**NOT AVAILABLE.** The data package returned: *"no authorized, point-in-time insider-transactions archive for AMZN by 2024-02-01."*

I will not infer, estimate, or fabricate insider activity. There is **zero** signal here — neither bullish nor bearish. A trader should obtain Form 4 data independently before assigning any weight to insider behavior, and should note that founder/executive selling at Amazon is routine 10b5-1 programmatic activity and carries limited information content regardless.

---

## 10. Actionable Insights & Trade Implications

**1. The thesis is an operating-margin and FCF inflection, and it is confirmed in hard numbers — not narrative.**
Operating income $12.2B → $36.9B (+201%); operating margin 2.38% → **6.41%**; FCF −$16.9B → **+$32.2B (+$49.1B)**. Gross margin expanded **317bp** to 46.98%. This is the cleanest fundamental turn in mega-cap tech for FY2023.

**2. But the market already knows — position for *durability*, not for the surprise.**
FY2023 diluted EPS is $2.90. Trailing earnings power of ~$30.4B net income and $32.2B FCF means the stock is priced on **forward** margin expansion, not the trailing print. Sensitivity: **every 100bp of sustained operating margin at FY2023's $574.8B revenue is worth ~$5.7B of pre-tax profit (~$4.4B after tax, ~$0.42/share).** The bull case requires margin to **hold at 6.4%+ and compound**, which in turn requires the opex restraint (G&A −0.6%, advertising −1.5%) to be structural rather than a one-year pause. **Watch the Q1-2024 opex lines for re-acceleration** — that is the first falsification test.

**3. The FCF beat is partly a capex holiday — fade the extrapolation.**
Capex fell 17.2% to $52,729M (9.2% of revenue from 12.4%). Meanwhile contractual obligations total **$300.4B** with **$157.8B beyond five years** and the PP&E deferred tax liability up 38%. **The next leg of capex (AI/infrastructure) is pre-committed.** Expect the FCF margin (currently 5.60%) to compress in FY2024 even if earnings grow.

**4. Cash taxes are the under-appreciated margin headwind.**
Book ETR 18.96%, cash rate **29.8%**, cash taxes +85% YoY to $11,179M. Domestic NOL DTAs are down to $610M. **Normalizing the tax rate to ~24% alone cuts ~$1.9B from net income.** FCF growth will lag EPS growth for this reason.

**5. Balance sheet gives optionality that is not priced.**
$144.3B cash + securities; net cash **+$73.9B** ex-operating-leases; debt/equity 0.29×; EBIT/interest 11.6×; zero LT debt issued and zero buybacks in FY2023. Combined with **4.18%-of-revenue SBC and +3.0% share count**, a **buyback announcement is the highest-probability positive catalyst** and would be highly accretive. Conversely, its continuation-absence is a drag on per-share value.

**6. Receivables and contract liabilities tell opposite stories — weight the latter.**
AR +23.4% vs revenue +11.8% (+3.1 AR days) is a mild working-capital yellow flag worth monitoring for one or two more quarters. But **contract liabilities +28% with the non-current portion +96.6%** is a genuine leading indicator of AWS/Prime demand and is the more informative signal. **Net-net: mildly bullish forward visibility.**

**7. Trade construction.** The fundamentals support a **long bias on operating leverage**, but the entry point matters given trailing EPS of $2.90 embeds a demanding multiple. Prefer:
- **Long AMZN vs. short a lower-margin retail peer** — isolates the margin-expansion thesis while hedging consumer-spending beta.
- **Options: cost-efficient upside** given the wide binary risk around Q4 seasonality (Q4-2023 alone produced $27.9B, or 87%, of full-year FCF — a single-quarter dependency that makes the name structurally volatile around the January print).
- **Avoid the "cheap on FCF" trap** — the 5.60% FCF margin is flattered by a one-year capex cut and an artificially low cash tax rate. Use **EBIT margin (6.41%)** as the anchor multiple instead.

**8. Hard catalysts to diarize:** (i) Q1-2024 opex lines — does G&A/advertising restraint persist? (ii) Capex guidance — does the $300B obligation book start converting? (iii) Any capital-return announcement (buyback/dividend). (iv) AWS segment margin, which this dataset cannot see.

---

## Summary Table

| Category | Metric | Value | YoY / Trend | Signal |
|---|---|---:|---|---|
| **Scale** | Revenue (derived) | $574,785M | +11.8% | ✅ Reaccelerating (from +9.4%) |
| | Total assets | $527,854M | +14.1% | ✅ |
| | Shares outstanding | 10,383M | +1.4% (diluting) | ⚠️ |
| **Profitability** | Gross profit | $270,046M | +19.9% | ✅ Margin 46.98% (+317bp) |
| | Operating income | $36,852M | **+200.9%** | ✅✅ Margin 6.41% (+403bp) |
| | Net income | $30,425M | n.m. (from −$2,722M) | ✅ Margin 5.29% |
| | Diluted EPS | $2.90 | n.m. (from −$0.27) | ✅ |
| | EBIT margin | 6.41% | +403 bp | ✅✅ Core thesis |
| **Cash generation** | Operating cash flow | $84,946M | **+81.7%** | ✅✅ |
| | Capex | $52,729M | **−17.2%** | ⚠️ One-year holiday |
| | **Free cash flow** | **+$32,217M** | **+$49,110M swing** | ✅✅ FCF margin +5.60% |
| | OCF / Net income | 2.79× | — | ✅ High earnings quality |
| **Balance sheet** | Cash + securities | $144,306M | +36.2% (cash) | ✅✅ |
| | Total debt (carrying) | $58,314M | −13.2% | ✅ Deleveraging |
| | Net cash (ex-op-leases) | +$73,883M | Improving | ✅✅ |
| | Current ratio | 1.05× (2.15× ex-AP) | Flat | ✅ |
| | Debt / EBITDA | 0.68× | Falling | ✅ Under-levered |
| | EBIT / interest | 11.6× | Improving | ✅ |
| | Operating lease liabilities | $75,639M | +9.6% | ⚠️ Under-appreciated |
| **Returns** | ROE | 17.5% | Recovering | ✅ |
| | ROIC (NOPAT/invested capital) | ~23.3% | Recovering | ✅✅ |
| | Asset turnover | 1.16× | +0.03 | ✅ |
| **Capital allocation** | Buybacks FY2023 | $0 | vs $6,000M FY2022 | ⚠️ Paused |
| | LT debt issued FY2023 | $0 | — | ✅ |
| | Finance lease principal paid | $4,384M | −44.8% | ✅ |
| **Earnings quality** | Non-operating income | $705M | vs $13,272M FY2021 | ✅ Clean |
| | Book ETR | 18.96% | — | ⚠️ Unsustainable |
| | **Cash taxes / pretax** | **29.8%** | Cash taxes +85% | ⚠️⚠️ FCF headwind |
| | SBC expense | $24,023M (4.18% rev) | +22.4% | ⚠️ Real cost |
| | Unrecognized SBC | $18,300M | — | ⚠️ Future EPS drag |
| **Forward indicators** | Contract liabilities | $20,600M | **+28.0%** | ✅✅ Demand visibility |
| | Non-current contract liab. | $5,700M | **+96.6%** | ✅✅ Multi-year commitments |
| | Total contractual obligations | $300,409M | ($157,824M >5yr) | ⚠️ Capex re-acceleration |
| | AR days | 33.2 | +3.1 days | ⚠️ Monitor |
| | AP days | ~101.8 | +1.2 days | ✅ Supplier float |
| **Segment** | Operating segments | 3 (NA / Intl / AWS) | — | ⛔ No segment detail available |
| **Insider activity** | Form 4 archive | **UNAVAILABLE** | — | ⛔ No signal — do not infer |
| **Data caveats** | 10-K accepted | 2024-02-02 04:48 UTC | After 2024-02-01 | ⚠️ Fresh, un-digested print |
| | Revenue tag | Not provided — derived | COGS + Op. income | ⚠️ Derived figure |

---

### Bottom line for traders
AMZN printed a **genuine, cash-backed operating inflection** in FY2023: operating income tripled to $36.9B, operating margin reached 6.41%, and free cash flow swung positive by $49.1B on a fortress balance sheet with $144.3B of liquidity and net cash of $73.9B. The earnings are **high quality** — only $705M of non-operating help, and OCF covers net income 2.79×. **The risks are that the FCF beat rests on a one-year capex holiday and an artificially low cash tax rate (29.8% cash vs 18.96% book), that $300.4B of contractual obligations foretell a capex re-acceleration, and that SBC of $24.0B dilutes shareholders at 3% a year with zero buyback offset.** Net stance: **constructively long on the operating-margin and FCF trajectory, but sized for a capex-driven FCF giveback in FY2024 rather than extrapolating FY2023's 5.60% FCF margin.** The insider-transaction channel is unavailable and should be treated as no-signal.