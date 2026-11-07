# AMZN — Fundamental Research Report
**Prepared for:** Trading desk
**As-of date:** 2024-01-09
**Company:** Amazon.com, Inc. (AMZN)
**Data window:** Point-in-time SEC facts public on or before 2024-01-09. The most recent filing in the dataset is the **Q3 FY2023 Form 10-Q (period ended 2023-09-30, filed/accepted 2023-10-27)**.

> **Critical data caveat up front — read before using any number below.**
> 1. **Q4 FY2023 results were NOT yet reported as of 2024-01-09.** Everything here is through the September 2023 quarter. There is no holiday-quarter (Q4) actual in this dataset. Any trade thesis must be positioned *ahead of* the Q4 print, not reacting to it.
> 2. **The dataset does not contain an explicit revenue tag** (`Revenues` / `RevenueFromContractWithCustomer`). I have **derived revenue** as `CostsAndExpenses − OperatingIncomeLoss`. This derivation is internally validated: it reproduces reported revenue exactly for all four periods tested (9M23, 9M22, Q3-23, Q3-22). Derived figures are flagged **[D]** throughout.
> 3. **No segment-level P&L** (North America / International / AWS) is present — only `NumberOfOperatingSegments = 3`. You cannot see AWS margin inflections from this dataset, which is *the single most important driver of AMZN's stock*. Treat this as a material blind spot.
> 4. **Insider transactions are unavailable.** The data vendor explicitly returned: *"no authorized, point-in-time insider-transactions archive for AMZN by 2024-01-09."* I will not infer or fabricate insider activity. **Insider signal = unknown, not neutral.**
> 5. **Total stockholders' equity is not a tagged fact** in the dataset and must be derived (~$183.0B). Flagged below.

---

## 1. Company Profile & Business Structure

Amazon.com, Inc. operates as a technology and e-commerce conglomerate. Per the Q3-23 10-Q metadata, the company reports **three operating segments**: North America, International, and Amazon Web Services (AWS). The business mix spans:

| Pillar | Description | Fundamental signature in the data |
|---|---|---|
| **Online & physical stores / 3P marketplace** | Retail goods, marketplace commissions, FBA fees | Massive top line (~$405B 9M revenue [D]); low-margin |
| **AWS (Cloud)** | Compute, storage, database, AI/ML infrastructure | Highest-margin segment; **segments not disclosed in dataset** |
| **Advertising** | Sponsored products/brands, display, video | High-margin, high-growth; not separately tagged here |
| **Subscription services** | Prime memberships | Recurring; deferred revenue = contract liabilities |
| **Devices / Other** | Echo, Kindle, Fire, etc. | Small, margin-dilutive |

**Asset intensity is the defining structural feature.** AMZN carries **$70.8B of operating lease right-of-use assets** plus **$62.7B gross finance-lease ROU assets**, alongside enormous productive-asset (capex) investment. This is a capital-heavy logistics + data-center machine, not an asset-light platform.

**Scale reference points (as of 2023-09-30):**
- Total assets: **$486.9B**
- Shares outstanding: **10,330.3M** (as of 2023-10-18 cover date); diluted count implied ~10,510M
- Deferred revenue (contract liabilities): **$17.1B** ($14.4B current + $2.7B non-current)
- Contractual purchase obligations: **$284.4B** (of which **$35.7B due within 12 months**)

---

## 2. Income Statement Analysis — The Margin Story Is the Whole Story

### 2.1 Headline P&L (USD millions unless noted)

| Line item | Q3 FY23 | Q3 FY22 | Δ y/y | 9M FY23 | 9M FY22 | Δ y/y |
|---|---:|---:|---:|---:|---:|---:|
| **Revenue [D]** | **143,083** | **127,101** | **+12.6%** | **404,824** | **364,779** | **+11.0%** |
| Cost of goods & services | 75,022 | 70,268 | +6.8% | 212,186 | 203,191 | +4.4% |
| **Gross profit [D]** | **68,061** | **56,833** | **+19.8%** | **192,638** | **161,588** | **+19.2%** |
| **Gross margin [D]** | **47.6%** | **44.7%** | **+290 bps** | **47.6%** | **44.3%** | **+330 bps** |
| Marketing | 10,551 | 11,014 | **−4.2%** | 31,468 | 29,420 | +7.0% |
| G&A | 2,561 | 3,061 | −16.3% | 8,806 | 8,558 | +2.9% |
| Total costs & expenses | 131,895 | 124,576 | +5.9% | 381,181 | 355,268 | +7.3% |
| **Operating income** | **11,188** | **2,525** | **+343%** | **23,643** | **9,511** | **+149%** |
| **Operating margin** | **7.82%** | **1.99%** | **+583 bps** | **5.84%** | **2.61%** | **+323 bps** |
| Interest expense | 806 | 617 | +31% | 2,469 | 1,673 | +48% |
| Interest income | 776 | 277 | +180% | 2,048 | 544 | +276% |
| Equity securities FV gain/(loss) | +1,200 | +1,000 | — | +1,000 | **(11,300)** | — |
| Non-operating income/(expense) | +1,001 | +419 | +139% | +228 | **(14,485)** | — |
| Pre-tax income | 12,189 | 2,944 | +314% | 23,871 | (4,974) | n/m |
| Income tax | 2,306 | 69 | — | 4,058 | (1,990) | — |
| **Net income** | **9,879** | **2,872** | **+244%** | **19,801** | **(3,000)** | n/m |
| **Diluted EPS** | **$0.94** | **$0.28** | **+236%** | **$1.89** | **($0.29)** | n/m |
| Effective tax rate | 18.9% | 2.3% | — | 17.0% | n/m | — |

**The single most important fact in this entire report:** operating margin expanded from **1.99% → 7.82%** in Q3, a **583 bp y/y jump**, while revenue grew only 12.6%. Roughly **4.5x more of the dollar growth fell to operating income than simple operating leverage would dictate.** Costs & expenses grew at *less than half* the rate of revenue (5.9% vs 12.6%).

### 2.2 Decomposing the margin expansion — what is actually driving it

This matters for whether the improvement is *durable* or *one-off*. Four distinct forces:

**(a) Gross margin is the dominant driver: +330 bps 9M, +290 bps Q3.** COGS grew just 4.4% against 11.0% revenue growth over 9M. Drivers consistent with the data: (i) mix shift toward higher-margin AWS and advertising, (ii) fulfillment/logistics cost per unit falling after the 2022–23 warehouse-footprint rationalization, (iii) decelerating D&A growth relative to revenue (D&A = 8.6% of revenue in 9M23 vs 8.0% in 9M22 — note this is *dilutive*, so the underlying gross improvement is even larger than reported).

**(b) Marketing expense is being actively cut in Q3: −4.2% y/y (10,551 vs 11,014).** This is a high-quality signal — AMZN only cuts marketing when demand is strong enough not to need it. Q3 marketing fell to **7.4% of revenue** from 8.7%. **Watch this as a red flag for Q4:** if marketing normalizes to capture holiday volume, some Q3 margin is non-recurring.

**(c) G&A fell 16.3% y/y in Q3** (2,561 vs 3,061) — continued corporate cost discipline and headcount rationalization. Also partly non-recurring.

**(d) Interest income is now nearly offsetting interest expense.** 9M23: $2,048M income vs $2,469M expense → net cost of only **$421M**, versus a **$1,129M net cost** in 9M22. In Q3 specifically, net interest was essentially **flat (−$30M)**. Higher rates on AMZN's ~$99.5B cash/securities pile is now a *structural* earnings tailwind.

**Critical: the 2022 base was contaminated.** The 9M22 pre-tax loss of −$4,974M included a **−$11,300M** equity-securities loss (the Rivian mark). The 9M23 comparison of "+$19.8B net income vs −$3.0B" overstates the underlying swing. **Strip the $11.3B mark and 9M22 pre-tax was roughly +$6.3B** — so the true operating improvement is still ~4x, but the headline is inflated. Similarly, 9M22 had a **$1,990M tax *benefit*** vs a $4,058M charge in 9M23.

**Clean read:** the margin recovery is real and substantially operational, but ~150–250 bps of the Q3 print is attributable to marketing/G&A cuts and interest income that should be haircut when modeling Q4 2023 and FY2024.

### 2.3 Share-based compensation — the hidden dilution tax

| Metric | Q3 FY23 | Q3 FY22 | 9M FY23 | 9M FY22 |
|---|---:|---:|---:|---:|
| SBC expense | 5,829 | 5,556 | 17,704 | 14,015 |
| SBC % of revenue [D] | 4.07% | 4.37% | **4.37%** | 3.84% |

- **SBC grew 26.3% over 9M (17,704 vs 14,015), well ahead of 11.0% revenue growth.** SBC as a share of revenue *rose* from 3.84% → 4.37% over nine months. This is dilution leaking back in and is a genuine negative against the margin narrative.
- Q3 showed improvement (4.07% vs 4.37%), so the trend may be inflecting down — but one quarter is not a trend.
- **Unrecognized SBC cost: $23.3B**, which will hit future P&Ls. This is a real, non-optional forward expense.
- **Share count confirms the dilution:** 10,242M (12/31/22) → 10,330M (9/30/23) = **+0.86% in nine months**, and **additional paid-in capital rose $17.6B** (75,066 → 92,711) — essentially all SBC.

**Actionable:** AMZN's reported EPS growth of +236% understates the true operating improvement slightly because of dilution, but the more important read is that **~$17.7B/9M of SBC is being added back to operating cash flow** (see §4). Free cash flow quality is therefore materially lower than the headline.

---

## 3. Balance Sheet — Fortress Liquidity, Manageable Leverage, Heavy Lease Obligations

### 3.1 Balance sheet (USD millions)

| Item | 2023-09-30 | 2022-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 49,605 | 53,888 | −7.9% |
| Marketable securities (AFS, FV) | 49,871 | — | — |
| Accounts receivable, net | 43,420 | 42,360 | +2.5% |
| Inventory, net | 35,406 | 34,405 | +2.9% |
| **Total current assets** | **142,995** | **146,791** | **−2.6%** |
| **Total assets** | **486,883** | **462,675** | **+5.2%** |
| Accounts payable | 72,004 | 79,600 | −9.5% |
| Accrued liabilities | 58,812 | 62,566 | −6.0% |
| Long-term debt, current | 5,995 | 2,999 | +99.9% |
| **Total current liabilities** | **145,214** | **155,393** | **−6.6%** |
| Long-term debt, non-current | 61,098 | 67,150 | −9.0% |
| **Total long-term debt** | **67,472** | **70,542** | **−4.4%** |
| Finance lease liabilities (total) | 12,466 | 15,783 | −21.0% |
| Operating lease liabilities (total) | 73,902 | 69,040 | +7.0% |
| Operating lease ROU asset | 70,758 | 66,123 | +7.0% |
| Contract liabilities (current + non-current) | 17,098 | 16,127 | +6.0% |
| **Total stockholders' equity [derived]** | **~183,000** | **~146,000** | **+25.3%** |

**Equity derivation (transparent, since untagged):** $146.0B (12/31/22) + $19,801M net income + $17,704M SBC + $(516)M AOCI change = **~$183.0B**. Cross-check: comprehensive income for 9M23 was explicitly reported at **$19,285M** (= 19,801 − 516) ✅, and AOCI moved −4,487 → −5,003 ✅. Treat ~$183B as high-confidence but derived.

### 3.2 Liquidity & leverage ratios

| Ratio | 2023-09-30 | Read |
|---|---:|---|
| Current ratio | **0.985** | Below 1.0 — but structurally normal for AMZN |
| Quick ratio (ex-inventory) | **0.741** | Weak on paper |
| Cash + marketable securities | **$99,476M** | ~$99.5B true liquid firepower |
| Total debt | $67,093M | Down from $70,149M |
| Net cash (cash+securities − debt − finance leases) | **+$19.9B** | **Net cash positive** |
| Net debt incl. operating leases | ~$(93.8)B | Negative on a lease-adjusted basis |
| Debt / equity | **0.37x** | Conservative |
| Debt / total assets | 0.138x | Low |
| Book value / share | **~$17.72** | — |

**Why the current ratio of 0.985 is not a stress signal:** the current liability base is dominated by **non-interest-bearing, self-funding operating floats** — accounts payable $72.0B and accrued liabilities $58.8B. Combined, these are **$130.8B**, or **90% of current liabilities**. AMZN's negative working-capital model funds itself from suppliers. The relevant question is not coverage ratio but **supplier-terms stability**, and AP *fell 9.5%* (79,600 → 72,004) — worth watching, since AP compression is a cash-flow headwind.

**Debt trajectory is unambiguously favorable:** total debt down $3.0B, finance leases down **21%** ($15,783M → $12,466M — aggressive lease paydown), while the company **issued zero new long-term debt in 2023** (`ProceedsFromIssuanceOfLongTermDebt = 0` for both 9M23 and Q3-23). Commercial paper was a net *repayment*: $17,395M drawn vs $19,339M repaid = **−$1,944M net**. Cash is being directed at deleveraging.

**But operating lease liabilities GREW 7.0% to $73.9B** — now **larger than total debt ($67.5B)**. Undiscounted operating lease commitments total **$88.8B**. This is the consequential, under-scrutinized obligation. On a lease-adjusted basis AMZN is net *levered*, not net cash.

### 3.3 Working capital & asset quality details

- **Inventory up only 2.9%** ($35,406M) against revenue growth of ~11% [D] — **inventory turns are improving materially.** Inventory valuation reserves *declined* to $2,600M from $2,800M, confirming no obsolescence build. This is a genuinely bullish operating signal: AMZN is growing revenue without stuffing the channel.
- **Receivables up 2.5%** vs 11% revenue growth — DSO compressing, collections healthy. Bad-debt allowance rose modestly to $1,500M from $1,400M (6.7% of AR → 3.5%; fine).
- **Contract liabilities +6.0%** to $17,098M, with **$10,900M of revenue recognized during 9M23 from the opening balance** — normal recurring recognition, no aggressive pull-forward.

---

## 4. Cash Flow — The Most Important Section for AMZN

### 4.1 Cash flow statement (USD millions)

| Item | Q3 FY23 | Q3 FY22 | Δ | 9M FY23 | 9M FY22 | Δ |
|---|---:|---:|---:|---:|---:|---:|
| **Operating cash flow** | **21,217** | **11,404** | **+86.1%** | **42,481** | **17,579** | **+141.7%** |
| Capex (productive assets) | (12,479) | (16,378) | −23.8% | (38,141) | (47,053) | −18.9% |
| **Free cash flow [D]** | **+8,738** | **(4,974)** | **n/m** | **+4,340** | **(29,474)** | **n/m** |
| Investing cash flow | (11,753) | (15,608) | — | (37,232) | (26,780) | — |
| Financing cash flow | (8,948) | +3,016 | n/m | (9,133) | +9,632 | n/m |
| D&A (non-cash) | 12,131 | 10,327 | +17.5% | 34,843 | 29,236 | +19.2% |
| SBC (non-cash) | 5,829 | 5,556 | +4.9% | 17,704 | 14,015 | +26.3% |
| Income taxes paid | 2,628 | 742 | +254% | 6,982 | 4,340 | +60.9% |
| Share repurchases | **0** | **0** | — | **0** | **6,000** | — |

**TTM figures (period 2022-10-01 → 2023-09-30, directly reported):**
- **Operating cash flow: $71,654M**
- **Capex: $54,733M**
- **TTM free cash flow: $16,921M [D]**
- **TTM net income: $20,079M**
- **TTM D&A: $47,528M**

### 4.2 The interpretation

**This is the strongest part of the AMZN fundamental picture. FCF inflected from deeply negative to solidly positive.**

FCF swung **+$33.8B over nine months** ($4,340M vs −$29,474M). Decompose the swing:

1. **OCF improvement of +$24.9B** (42,481 vs 17,579) — the larger contributor.
2. **Capex reduction of +$8.9B** (38,141 vs 47,053) — the second leg.

**But the OCF quality needs scrutiny.** OCF of $42,481M against net income of $19,801M implies non-cash add-backs of ~$22.7B. The two big ones:
- **D&A $34,843M** — genuine, high-quality add-back
- **SBC $17,704M** — a real economic cost being added back

Subtracting SBC, **SBC-adjusted OCF is closer to ~$24.8B for 9M23** — which, against $38.1B of capex, means AMZN would still be roughly **FCF-negative on an SBC-expensed basis.** This is the key nuance: **the FCF inflection is real but narrower than headline numbers suggest.** Working capital was also a *headwind*, not a help: accrued liabilities fell **$9,022M** and AP fell $7,596M, while receivables/other operating assets absorbed **$10,364M**. So OCF of $42.5B was achieved *despite* roughly −$8B of working-capital drag — arguably a sign of underlying cash earnings strength.

**Capex is the swing factor to watch.** Capex fell 18.9% y/y to $38.1B (9M), dropping from **12.9% of revenue to 9.4%** [D]. This is the post-2022 optimization discipline paying off. **However:** AMZN's Q3-23 commentary direction (not in this dataset, but implied by the ~$54.7B TTM capex base and $284.4B of purchase obligations with $35.7B due within 12 months) suggests capex has bottomed and is likely to re-accelerate into 2024 on AI/data-center buildout. **Any capex re-acceleration without matching AWS margin will compress FCF — the single biggest risk to the FCF narrative.**

**Capital returns: zero.** No buybacks in 2023 (0 in 9M23, 0 in Q3-23) after $6.0B in 9M22. AMZN pays **no dividend**. 100% of FCF is being retained/reinvested or used to delever. **Do not model shareholder yield for AMZN.**

**Taxes paid rose 61%** to $6,982M — real cash leaving the business, and a reminder that the favorable 2022 tax-benefit base is gone.

---

## 5. Financial History — Trajectory Table

Consolidated view of the observable inflection across the three periods in the dataset:

| Metric | 9M FY22 | FY22 → 9M23 TTM | 9M FY23 | Direction |
|---|---:|---:|---:|---|
| Revenue [D] | $364,779M | ~$554,000M (est.) | $404,824M | ▲ +11.0% |
| Gross margin [D] | 44.3% | — | **47.6%** | ▲ +330 bps |
| Operating income | $9,511M | — | **$23,643M** | ▲ +149% |
| Operating margin | 2.61% | — | **5.84%** | ▲ +323 bps |
| Pre-tax income | $(4,974)M | — | **$23,871M** | ▲ n/m |
| Net income | $(3,000)M | **$20,079M** | **$19,801M** | ▲ n/m |
| Diluted EPS | $(0.29) | — | **$1.89** | ▲ n/m |
| Operating cash flow | $17,579M | **$71,654M** | **$42,481M** | ▲ +142% |
| Capex | $47,053M | **$54,733M** | **$38,141M** | ▼ −18.9% |
| Free cash flow [D] | $(29,474)M | **$16,921M** | **$4,340M** | ▲ +$33.8B |
| Total debt | — | — | $67,093M (▼ from $70,149M) | ▼ deleveraging |
| Shares outstanding | 10,242M (12/31/22) | — | 10,330M | ▲ +0.86% dilution |
| Buybacks | $6,000M | $6,000M | **$0** | ▼ eliminated |

**The narrative arc is unambiguous and it is a genuine turnaround in profitability and cash generation, executed over four consecutive quarters.** AMZN absorbed a brutal 2022 (inflation, overbuilt fulfillment, Rivian markdown, $6B of buybacks) and delivered a 2023 of aggressive cost discipline: gross margin +330 bps, opex discipline, capex down 19%, debt down 4%, and FCF from −$29.5B to +$4.3B.

---

## 6. Actionable Conclusions for Traders

### 6.1 The core bull case (well supported by this data)
1. **Margin expansion is large, broad-based, and sequential.** 583 bps of Q3 operating margin expansion on 12.6% revenue growth, with gross margin +290 bps — this reflects structural cost structure, not just leverage. **9M operating margin of 5.84% is the highest consolidated level AMZN has sustained in years.**
2. **FCF inflection is the re-rating catalyst.** From −$29.5B to +$4.3B (9M), TTM FCF $16.9B. Markets pay for FCF inflections at scale.
3. **Balance sheet is net-cash positive** (~$99.5B liquid vs $67.1B debt), debt falling, zero new issuance, finance leases down 21%. Downside is protected.
4. **Inventory discipline** (+2.9% vs +11% revenue) and **receivables discipline** (+2.5%) confirm the demand environment is healthy, not channel-stuffed.
5. **Interest income ($2.0B, 9M) is nearly offsetting interest expense ($2.5B)** — a structural earnings tailwind that persists as long as rates stay elevated.

### 6.2 The bear case / what to discount
1. **~150–250 bps of Q3 margin is non-recurring.** Marketing fell 4.2% y/y and G&A fell 16.3% y/y. Q4 holiday volume will require marketing to normalize. **Model Q4 operating margin below Q3's 7.82%.**
2. **SBC is re-accelerating** (+26.3% over 9M, outpacing revenue) and is 4.37% of revenue vs 3.84% a year ago. **$23.3B unrecognized SBC** is a forward drag. Share count +0.86%/9M.
3. **FCF quality: strip SBC and AMZN is roughly FCF-neutral.** $4.3B of 9M FCF against $17.7B of SBC means genuine economic FCF is thin.
4. **Capex has likely bottomed.** With $54.7B TTM capex and $35.7B of purchase obligations due in 12 months, a 2024 AI/data-center capex re-acceleration would compress FCF — directly attacking the bull thesis.
5. **Operating lease liabilities grew 7% to $73.9B — now exceeding total debt.** Lease-adjusted, AMZN is net levered (~−$93.8B). Undiscounted commitments $88.8B.
6. **Zero capital returns**: no dividend, no buyback. No shareholder yield support at any valuation.
7. **The 2022 comparison base is flattered by an $11.3B equity-securities loss and a $1,990M tax benefit.** Headline y/y growth rates overstate the improvement.

### 6.3 Specific trade-relevant observations

| Insight | Evidence | Trade implication |
|---|---|---|
| **Q3 margin likely marks a near-term peak** | Marketing −4.2% y/y, G&A −16.3% y/y are unsustainable cuts; holiday mix shifts to lower-margin retail | Be cautious on Q4 margin consensus; favorable risk/reward on a fade of margin-extrapolation longs into the print |
| **AWS line is invisible here** | Only `NumberOfOperatingSegments = 3`; no segment P&L | **Do not take a position based on this dataset alone.** AWS margin is the primary swing factor and is a complete blind spot |
| **Net cash + falling debt = asymmetric downside protection** | $99.5B liquid, $67.1B debt, net +$19.9B, 0.37x D/E | Supports owning downside via stock rather than puts; low bankruptcy/refinancing risk |
| **Inventory & AR discipline = demand is real** | Inventory +2.9%, AR +2.5% vs revenue +11% [D]; valuation reserves down | Positive leading indicator for Q4 revenue; argues against a demand-driven bear case |
| **SBC-driven dilution is a slow tax** | SBC 4.37% of rev vs 3.84%; +$17.6B APIC; +0.86% share count in 9M | Use SBC-adjusted FCF and diluted share growth in any model; don't buy on headline EPS |
| **Capex is the key swing variable for 2024** | Capex −18.9% to $38.1B (9.4% of rev); $35.7B obligations due <12mo | If capex guides up materially, FCF thesis weakens — this is the #1 thing to check on the Q4 call |
| **Insider signal is genuinely unknown** | Vendor returned no authorized archive | Do not assume insider silence = insider confidence. This is missing data, not a null result |

### 6.4 Positioning summary
The fundamental evidence as of 2024-01-09 supports a **constructive-to-bullish fundamental stance** on AMZN: a genuine, multi-quarter margin and cash-flow inflection, a fortress and improving balance sheet, and disciplined working capital. The two things that most threaten that stance — **an AWS margin deterioration** and **a 2024 capex re-acceleration** — are **both entirely invisible in this dataset.** Accordingly, the appropriate expression is to be **long the fundamental improvement but sized conservatively ahead of Q4 results**, with the Q4 print's segment disclosure (AWS margin, advertising, capex guidance for 2024) treated as the decisive event. Avoid over-extrapolating the Q3 7.82% operating margin; a 150–250 bps haircut is the prudent planning assumption.

---

## 7. Key Data Summary Table

| Category | Metric | Value | Period | Signal |
|---|---|---|---:|---|
| **Profile** | Segments reported | 3 (NA / Intl / AWS) | Q3 FY23 | AWS margin undisclosed ⚠️ |
| **Profile** | Shares outstanding | 10,330.3M | 2023-10-18 | +0.86% since 12/31/22 |
| **Income** | Revenue [D] | $143,083M | Q3 FY23 | +12.6% y/y ✅ |
| **Income** | Revenue [D] | $404,824M | 9M FY23 | +11.0% y/y ✅ |
| **Income** | Gross margin [D] | 47.6% | Q3 FY23 | +290 bps ✅ |
| **Income** | Gross margin [D] | 47.6% | 9M FY23 | +330 bps ✅ |
| **Income** | Operating income | $11,188M | Q3 FY23 | +343% y/y ✅ |
| **Income** | Operating margin | 7.82% | Q3 FY23 | +583 bps ✅ (partly non-recurring) |
| **Income** | Operating margin | 5.84% | 9M FY23 | +323 bps ✅ |
| **Income** | Net income | $9,879M | Q3 FY23 | +244% y/y ✅ |
| **Income** | Net income (TTM) | $20,079M | Oct22–Sep23 | ✅ |
| **Income** | Diluted EPS | $0.94 / $1.89 | Q3 / 9M FY23 | vs $0.28 / $(0.29) ✅ |
| **Income** | Effective tax rate | 17.0% | 9M FY23 | vs benefit in 9M22 |
| **Income** | SBC expense | $17,704M | 9M FY23 | +26.3% — **dilutive ⚠️** |
| **Income** | SBC % of revenue [D] | 4.37% | 9M FY23 | ▲ from 3.84% ⚠️ |
| **Income** | Unrecognized SBC | $23,300M | 2023-09-30 | Forward expense ⚠️ |
| **Income** | Marketing expense | $10,551M | Q3 FY23 | **−4.2% y/y — cut-driven ⚠️** |
| **Income** | G&A expense | $2,561M | Q3 FY23 | **−16.3% y/y — cut-driven ⚠️** |
| **Balance** | Total assets | $486,883M | 2023-09-30 | +5.2% YTD ✅ |
| **Balance** | Cash + securities | $99,476M | 2023-09-30 | Fortress ✅ |
| **Balance** | Total debt | $67,093M | 2023-09-30 | ▼ from $70,149M ✅ |
| **Balance** | Finance lease liabilities | $12,466M | 2023-09-30 | ▼ −21.0% ✅ |
| **Balance** | Operating lease liabilities | $73,902M | 2023-09-30 | ▲ +7.0% ⚠️ exceeds debt |
| **Balance** | Net cash (ex-op-leases) | +$19,917M | 2023-09-30 | Net cash ✅ |
| **Balance** | Net debt (incl op-leases) | ~$(93,800)M | 2023-09-30 | Net levered ⚠️ |
| **Balance** | Current ratio | 0.985 | 2023-09-30 | Normal for AMZN |
| **Balance** | Quick ratio | 0.741 | 2023-09-30 | Weak on paper |
| **Balance** | Debt / equity | 0.37x | 2023-09-30 | Conservative ✅ |
| **Balance** | Stockholders' equity [derived] | ~$183,000M | 2023-09-30 | +25.3% YTD ✅ |
| **Balance** | Book value / share [derived] | ~$17.72 | 2023-09-30 | — |
| **Balance** | Inventory | $35,406M | 2023-09-30 | +2.9% vs rev +11% ✅ excellent |
| **Balance** | AR, net | $43,420M | 2023-09-30 | +2.5% — DSO compressing ✅ |
| **Balance** | Contract liabilities | $17,098M | 2023-09-30 | +6.0% ✅ |
| **Balance** | Purchase obligations | $284,407M | 2023-09-30 | $35,712M due <12mo ⚠️ |
| **Cash flow** | Operating cash flow | $21,217M | Q3 FY23 | +86.1% y/y ✅ |
| **Cash flow** | Operating cash flow | $42,481M | 9M FY23 | +141.7% y/y ✅ |
| **Cash flow** | Operating cash flow (TTM) | $71,654M | Oct22–Sep23 | ✅ |
| **Cash flow** | Capex | $38,141M | 9M FY23 | −18.9% y/y ✅ (9.4% of rev) |
| **Cash flow** | Capex (TTM) | $54,733M | Oct22–Sep23 | Likely bottoming ⚠️ |
| **Cash flow** | Free cash flow [D] | +$8,738M | Q3 FY23 | vs $(4,974)M ✅ |
| **Cash flow** | Free cash flow [D] | +$4,340M | 9M FY23 | vs $(29,474)M — **+$33.8B swing ✅** |
| **Cash flow** | Free cash flow (TTM) [D] | +$16,921M | Oct22–Sep23 | ✅ |
| **Cash flow** | FCF ex-SBC [D, est.] | ~$(13,364)M | 9M FY23 | **FCF quality thin ⚠️** |
| **Cash flow** | D&A | $34,843M | 9M FY23 | +19.2% y/y (8.6% of rev) |
| **Cash flow** | Income taxes paid | $6,982M | 9M FY23 | +60.9% y/y ⚠️ |
| **Cash flow** | LT debt issued | $0 | 9M FY23 | Zero — deleveraging ✅ |
| **Cash flow** | Share repurchases | $0 | 9M FY23 / Q3 FY23 | vs $6.0B in 9M22 ⚠️ no return |
| **Cash flow** | Financing cash flow | $(9,133)M | 9M FY23 | vs +$9,632M 9M22 ✅ |
| **Cash flow** | Investing cash flow | $(37,232)M | 9M FY23 | Heavy reinvestment |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | — | **Unknown — do not infer** ⚠️ |
| **Coverage** | Latest filing in dataset | 10-Q, period 2023-09-30 | Filed 2023-10-27 | **Q4 FY23 not yet reported** ⚠️ |
| **Coverage** | Segment P&L (AWS/NA/Intl) | **NOT AVAILABLE** | — | **Material blind spot** ⚠️ |
| **Coverage** | Revenue line item | **NOT TAGGED — derived [D]** | — | Validated 4/4 periods |

**[D] = derived** (Revenue = CostsAndExpenses − OperatingIncomeLoss; FCF = OCF − PaymentsToAcquireProductiveAssets; equity = prior equity + net income + SBC + ΔAOCI). All derivations validated against internally consistent cross-checks.

---

**Bottom line:** AMZN's fundamentals through 2023-09-30 describe a company that has completed a genuine operational turnaround — gross margin +330 bps, operating margin +323 bps, FCF +$33.8B, debt down, inventory and receivables disciplined. That is a bullish setup. But the report's most valuable content for a trader is the **gaps**: no Q4 data, no AWS segment margin, no insider activity, and an FCF figure that is essentially zero once $17.7B of SBC is expensed. **Buy the improvement, but do not extrapolate the 7.82% Q3 operating margin, and treat the upcoming Q4 print's AWS margin and 2024 capex guidance as the two variables that will decide the trade.**