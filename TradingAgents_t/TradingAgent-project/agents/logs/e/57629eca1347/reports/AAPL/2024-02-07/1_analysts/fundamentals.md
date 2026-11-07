# AAPL — Comprehensive Fundamental Report
**Analysis date: 2024-02-07 | Company: Apple Inc. (AAPL) | Most recent filing: 10-Q for fiscal Q1 2024, accepted 2024-02-02**

> **Data provenance note:** All figures below are pulled from point-in-time SEC XBRL facts filtered to those accepted by EDGAR on or before 2024-02-07. AAPL's fiscal Q1 2024 10-Q was accepted **2024-02-02**, only 5 calendar days before this analysis date — so the numbers are extremely fresh and represent the dominant near-term fundamental catalyst. The vendor's `get_fundamentals` endpoint returned SEC financial-statement facts only (no company profile text, no price/valuation snapshot, and no segment/geographic breakdown), and `get_insider_transactions` returned **DATA_UNAVAILABLE** — I will not infer insider activity. Where I derive a metric, I label it "(derived)".

---

## 1. Executive Summary — What the Tape Just Learned

AAPL delivered a **clear fundamental inflection** in fiscal Q1 2024 (quarter ended 2023-12-30):

| Metric | Q1 FY24 | Q1 FY23 | Y/Y |
|---|---|---|---|
| Revenue | $119,575M | $117,154M | **+2.1%** |
| Cost of goods & services sold | $64,720M | $66,822M | **−3.1%** |
| Gross profit | $54,855M | $50,332M | **+9.0%** |
| Gross margin | **45.9%** | 43.0% | **+290 bps** |
| R&D | $7,696M | $7,709M | −0.2% |
| SG&A | $6,786M | $6,607M | +2.7% |
| Total opex | $14,482M | $14,316M | +1.2% |
| Operating income | $40,373M | $36,016M | **+12.1%** |
| Operating margin | **33.8%** | 30.7% | **+310 bps** |
| Non-operating income/(expense) | −$50M | −$393M | +$343M swing |
| Pretax income | $40,323M | $35,623M | +13.2% |
| Tax expense | $6,407M | $5,625M | +13.9% |
| **Net income** | **$33,916M** | $29,998M | **+13.1%** |
| **Diluted EPS** | **$2.18** | $1.88 | **+16.0%** |
| Basic EPS | $2.19 | $1.89 | +15.9% |

**The core insight: revenue grew only 2.1%, but EPS grew 16.0%.** That 14-point gap is the entire investment case right now, and it decomposes into three engines (derived):
- **~290 bps of gross-margin expansion** → gross profit grew 9.0% on 2.1% revenue (cost of sales actually *fell* 3.1% absolute dollars).
- **~310 bps of operating-margin expansion** → operating income grew 12.1%; opex grew only 1.2% (R&D was flat y/y at $7.70B, SG&A +2.7%).
- **Share-count shrinkage of ~2.5% y/y** (diluted shares ≈15.56B vs ≈15.96B, derived from NI/EPS) → converts 13.1% net-income growth into 16.0% EPS growth.
- A smaller fourth kicker: non-operating drag shrank from −$393M to −$50M, i.e. **yield on the securities portfolio is now nearly fully offsetting interest on ~$108B of debt**.

This is a *margin-and-buyback* quarter, not a *volume* quarter. Traders should frame it that way.

---

## 2. Company Profile & Data Caveat

AAPL is resolved as **Apple Inc.** (Cupertino, CA; fiscal year ends late September). The vendor dataset for this analysis contained no profile/description field, no segment revenue (iPhone/Mac/iPad/Wearables/Services) and no geographic revenue split. I therefore **do not** make any segment-mix or China-demand claims — those are not supported by my tools. What the filings *do* let me say with certainty: this is a business running **$119.6B of quarterly revenue at a 45.9% gross margin**, with a hardware-plus-recurring-revenue structure evident from the balance sheet (see §5: $12.5B of deferred revenue/contract liabilities and $3.5B of contract liability recognized in the quarter, both rising).

**Point-in-time identity check:** All facts used are Apple Inc. CIK 0000320193 accessions (0000320193-24-000006, 0000320193-23-000106, 0000320193-23-000077, -000064). No identity substitution. ✔

---

## 3. Income Statement — Quarterly Bridge (Q1 FY24 vs Q1 FY23)

**Revenue +2.1% ($117.15B → $119.58B).** Modest, but the composition matters more than the level:

- **Cost of sales fell 3.1%** ($66.82B → $64.72B) while revenue rose. This is the single most important line in the quarter — it implies a favorable shift in revenue mix and/or component-cost relief. Every 100 bps of gross margin at this revenue base is worth ~$1.2B of quarterly gross profit.
- **Gross margin 45.9%** — a +290 bps y/y expansion, and a level that historically sits at the high end of Apple's range. This is the primary driver of the earnings surprise.
- **R&D flat at $7.70B (−0.2%)** — notable. R&D intensity fell to 6.4% of revenue from 6.6%. Flat R&D with growing revenue is a strong incremental-margin setup, but also a metric to monitor: sustained flat R&D would eventually raise questions about the product pipeline.
- **SG&A +2.7% to $6.79B** — essentially in line with revenue growth, i.e. no operating leverage there. All the leverage came from gross margin.
- **Tax rate 15.9%** of pretax ($6,407/$40,323) vs 15.8% y/y — stable, but see §7 for the *cash* tax anomaly.

**Sequential read (derived from the balance sheet and cash flow):** Shareholders' equity rose **$11.95B in one quarter** ($62,146M → $74,100M) *after* paying $20.1B of buybacks and $3.8B of dividends. That is a remarkable statement about the underlying cash generation.

---

## 4. Multi-Year Income Statement History (FY2021–FY2023, from 10-K)

| | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Gross profit | $152,836M | $170,782M | $169,148M |
| Pretax income | $109,207M | $119,103M | $113,736M |
| Tax expense | $14,527M | $19,300M | $16,741M |
| **Net income** (derived) | **$94,680M** | **$99,803M** | **$96,995M** |
| Diluted EPS | $5.61 | $6.11 | **$6.13** |
| Basic EPS | $5.67 | $6.15 | $6.16 |
| Effective tax rate | 13.3% | 16.2% | **14.7%** |
| SBC (allocated) | $7,906M | $9,038M | $10,833M |
| SBC tax benefit | $4,056M | $4,002M | $3,421M |

**Three-year read:**
1. **Net income has been flat-to-down for two years** ($99.8B → $97.0B) while **EPS has risen every year** ($5.61 → $6.11 → $6.13). The entire FY22→FY23 EPS advance came from the buyback, not from earnings. This is a mature-cash-cow pattern and it makes the *margin* recovery in Q1 FY24 important — without margin expansion, EPS growth stalls at the buyback rate (~2.5–3%).
2. **Effective tax rate is drifting up** (13.3% → 14.7%, and 15.9% in Q1 FY24). A 100 bps increase in the tax rate at FY23 pretax income costs ~$1.1B of net income. This is a slow structural headwind.
3. **SBC is compounding at ~9–10% annually** ($7.9B → $10.8B) even as the tax benefit shrinks. Buybacks are partly running to offset dilution from R&D-heavy equity comp, which is a real economic cost that GAAP EPS partially obscures.

---

## 5. Balance Sheet — The Big Improvement Story

| Balance sheet item | 2023-12-30 | 2023-09-30 | Δ |
|---|---|---|---|
| Cash & equivalents | $40,760M | $29,965M | **+$10,795M** |
| Marketable securities, current | $32,340M | $31,590M | +$750M |
| Marketable securities, non-current | $99,475M | $100,544M | −$1,069M |
| **Cash + securities (derived)** | **$172,575M** | $162,099M | **+$10,476M** |
| Accounts receivable, net | $23,194M | $29,508M | **−$6,314M** |
| Nontrade receivables | $26,908M | $31,477M | −$4,569M |
| Inventory | $6,511M | $6,331M | +$180M |
| Total current assets | $143,692M | $143,566M | +$126M |
| Total assets | $353,514M | $352,583M | +$931M |
| Accounts payable | $58,146M | $62,611M | −$4,465M |
| Commercial paper | $1,998M | $5,985M | **−$3,987M** |
| Current portion of term debt | $10,954M | $9,822M | +$1,132M |
| Total current liabilities | $133,973M | $145,308M | **−$11,335M** |
| Term debt, non-current | $95,088M | $95,281M | −$193M |
| **Total term debt + CP (derived)** | **$108,040M** | $111,088M | −$3,048M |
| Total liabilities | $279,414M | $290,437M | −$11,023M |
| AOCI | −$9,378M | −$11,452M | **+$2,074M** |
| **Shareholders' equity** | **$74,100M** | $62,146M | **+$11,954M** |
| Shares outstanding | 15,460.22M | 15,550.06M | −89.8M |

**Derived liquidity & leverage ratios:**

| Ratio | 2023-12-30 | 2023-09-30 | Comment |
|---|---|---|---|
| Current ratio | **1.07x** | 0.99x | Back above 1.0 — first time in a year |
| Quick ratio (cash+ST sec+AR) | 0.72x | — | Chronically sub-1, structural for AAPL |
| Cash+securities / total debt | **1.60x** | 1.46x | Fortress |
| **Net cash position (derived)** | **+$64,535M** | +$51,011M | +$13.5B in one quarter |
| Debt / equity | 1.46x | 1.79x | Improving |
| Total liabilities / equity | 3.77x | 4.67x | Still high |
| Equity / total assets | **21.0%** | 17.6% | Thin, buyback-driven |
| Net cash per share (derived) | **~$4.18/sh** | — | 15,442M shares at 2024-01-19 |
| Book value per share (derived) | **~$4.80/sh** | — | Tangible book ≈ book (no goodwill of size) |

**Four things a trader must take away here:**

1. **Working capital was a massive cash source, but also a demand signal.** AR fell $6.3B (−21%) and nontrade receivables fell $4.6B (−15%) sequentially. The AR decline is a hugely favorable collections outcome in the seasonally strongest quarter — it flattered Q1 CFO by several billion and will *not* repeat. Meanwhile AP fell $4.5B, meaning Apple paid suppliers down rather than stretching them. Net: **do not extrapolate Q1's $39.9B CFO as a run-rate.**
2. **Net cash rebuilt to $64.5B** from $51.0B, with commercial paper cut 67% ($5.99B → $2.00B) and term debt essentially flat. The "net-cash-neutral-over-time" capital policy is currently running net-cash-*positive* — i.e. Apple is deleveraging into record buybacks. That is a bullish signal on management's read of its own cash flow durability.
3. **AOCI improved $2.07B** (from −$11.45B to −$9.38B), driven by **+$3,045M of unrealized gains on available-for-sale securities** in the quarter (vs +$900M a year ago), plus +$308M FX translation. The securities portfolio (≈$131.8B AFS) is recovering from its rate-shock mark-to-market hole. A continued decline in market yields is a *direct, mechanical* tailwind to both AOCI and book equity — and to the market's read on "hidden losses."
4. **Equity is thin (21% of assets) but rising fast.** $74.1B of book equity now supports $353.5B of assets. If buybacks continue at ~$20B/quarter while net income runs ~$34B/quarter, book equity compounds ~$14B/quarter — the deleveraging trend continues. The flip side: **nearly all EPS growth is buyback-dependent**, so any interruption in FCF (e.g. weaker demand, unfavorable mix) hits EPS with leverage.

**Debt maturity ladder (FY2023 10-K):** FY24 $9,943M | FY25 $10,775M | FY26 $12,265M | FY27 $9,786M | FY28 $7,800M | Beyond FY28 $56,003M. **Very well termed out** — no refinancing cliff, and the near-term maturities are <2x one quarter of free cash flow. Also on the books: $13,841M of operating-lease payments and $1,425M of finance-lease payments (immaterial).

---

## 6. Cash Flow — The Quarter That Paid for Itself Three Times

| Cash flow | Q1 FY24 | Q1 FY23 | Y/Y |
|---|---|---|---|
| **Operating cash flow** | **$39,895M** | $34,005M | **+17.3%** |
| Capex (PP&E) | $2,392M | $3,787M | **−36.8%** |
| **Free cash flow (derived)** | **$37,503M** | $30,218M | **+24.1%** |
| Investing cash flow (net) | **+$1,927M** | −$1,445M | net inflow |
| Financing cash flow (net) | −$30,585M | −$35,563M | less negative |
| Buybacks | $20,139M | $19,475M | +3.4% |
| Dividends | $3,825M | $3,768M | +1.5% |
| RSU tax withholding | $2,591M | $2,316M | +11.9% |
| Commercial paper, net | −$3,984M | −$8,214M | paydown |
| D&A | $2,848M | $2,916M | −2.3% |
| SBC (allocated) | $2,997M | $2,905M | +3.2% |
| Income taxes paid, net | **$7,255M** | $828M | **+776%** |
| Net change in cash | +$11,237M | −$3,003M | |

**Derived quality-of-earnings metrics:**

| Metric | Q1 FY24 | Q1 FY23 |
|---|---|---|
| CFO / net income | **1.18x** | 1.13x |
| CFO / revenue | **33.4%** | 29.0% |
| **FCF margin** | **31.4%** | 25.8% |
| Capex / revenue | **2.0%** | 3.2% |
| Total capital returned / FCF | **63.9%** | 76.8% |
| Dividends / FCF | 10.2% | 12.5% |

**Analysis:**
- **FCF of $37.5B in a single quarter at a 31.4% margin is the headline.** Free cash flow grew 24% on 2% revenue growth. That is the cleanest proof that the margin story is real cash, not accounting.
- **Capex collapsed to $2.39B (−37% y/y), the lowest quarterly figure in years.** At 2.0% of revenue, Apple is spending almost nothing on PP&E relative to its scale. This inflates FCF optically and is a legitimate caution: infra/AI/datacenter investment is *not* showing up in Apple's capex line. If Apple must materially step up capex (e.g. for on-device or server-side AI), FCF growth decelerates. **Watch this line every quarter — it is the highest-signal forward indicator in the whole report.**
- **Cash taxes paid jumped to $7,255M from $828M.** The GAAP tax expense ($6,407M) was *lower* than the cash actually paid — the opposite of prior-year timing. This is a working-capital/timing item, not a rate change (rate held ~15.9%), but it means FY24 cash taxes will be a larger drag than FY23. Don't be alarmed, but don't model $828M-type quarters either.
- **Capital returns were $23.96B (buybacks $20.14B + dividends $3.83B), equal to 63.9% of FCF.** Payout to FCF fell y/y because FCF grew faster than the buyback — leaving **~$13.5B of quarterly FCF headroom** for further buyback increases, debt reduction, or M&A.
- **Dividend raised to $0.24/share/quarter** from $0.23 (+4.3%); annualized $0.96.

**Annual cash flow history (10-K):**

| | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| CFO | $104,038M | $122,151M | $110,543M |
| Capex | $11,085M | $10,708M | $10,959M |
| **FCF (derived)** | **$92,953M** | **$111,443M** | **$99,584M** |
| Buybacks | $85,971M | $89,402M | $77,550M |
| Dividends | $14,467M | $14,841M | $15,025M |
| RSU tax withholding | $6,556M | $6,223M | $5,431M |
| Total returned / FCF | **115.3%** | **99.1%** | **98.4%** |
| Financing cash flow | −$93,353M | −$110,749M | −$108,488M |
| Investing cash flow | −$14,545M | −$22,354M | +$3,705M |

**Critical historical observation:** In FY2021 and FY2022 Apple returned **115% and 99% of FCF** — it was paying out more than it generated, funding the excess with balance-sheet cash and debt. In FY2023 it pulled back to 98.4%. **In Q1 FY24 it is back down to 63.9%.** The company has deliberately throttled capital returns relative to cash generation. **That is dry powder.** Historically, AAPL has announced buyback authorization increases alongside its fiscal Q2 (April) results — a forward catalyst worth flagging, though the dataset contains no authorization-remaining figure.

---

## 7. Insider Transactions

**DATA_UNAVAILABLE.** The B-project data package contains no authorized, point-in-time insider-transaction archive for AAPL as of 2024-02-07. I am explicitly **not** inferring, estimating, or fabricating insider buying or selling. Traders should note this as an information gap in this report and source Form 4 data independently before attributing any signal to insider behavior.

---

## 8. Fundamental Scorecard

| Dimension | Assessment | Evidence |
|---|---|---|
| Revenue growth | **Weak / inflecting positive** | +2.1% y/y Q1 FY24; FY23 net income fell y/y |
| Gross margin | **Strong, expanding** | 45.9%, +290 bps y/y; COGS −3.1% absolute |
| Operating margin | **Strong, expanding** | 33.8%, +310 bps y/y; opex +1.2% vs rev +2.1% |
| EPS growth quality | **Mixed** | +16.0% EPS but +13.1% NI and only +2.1% rev; ~2.5% from buyback |
| Cash generation | **Excellent** | FCF $37.5B/qtr, 31.4% FCF margin, CFO/NI 1.18x |
| Balance sheet | **Very strong, improving** | Net cash +$64.5B; current ratio 1.07x; debt termed out to 2060s |
| Capital allocation | **Conservative pivot, i.e. dry powder** | Payout 63.9% of FCF (vs 98–115% in FY21–23) |
| Tax | **Slow headwind** | ETR 13.3% → 14.7% → 15.9%; cash taxes +776% y/y |
| Cyclicality / concentration | **Elevated risk** | Single-product-cycle dependence; no segment data available to quantify |
| Insider signal | **Not assessable** | Data unavailable — gap, not a red flag |

---

## 9. Actionable Insights for Traders

**Bull case — what the numbers actually support:**
1. **The margin story is the trade.** COGS fell 3.1% while revenue rose 2.1%. If gross margin simply *holds* at 45.9% for the remaining three quarters, the y/y EPS comparison gets very easy. The market was positioned for a revenue-decline narrative; the 10-Q delivered margin expansion instead, filed 2024-02-02 — a fresh, under-absorbed catalyst.
2. **Cash-flow optionality is underappreciated.** $37.5B FCF in one quarter, only 63.9% returned. The company is building net cash ($51.0B → $64.5B) *while* running $20B/quarter buybacks. Either buybacks accelerate or the dividend growth rate (+4.3%) accelerates — both are EPS-supportive.
3. **AOCI recovery is a quiet re-rating driver.** Unrealized gains of $3.0B on the $131.8B AFS portfolio turned AOCI from −$11.5B to −$9.4B in one quarter. Falling yields mechanically repair book equity; this is a persistent tailwind to "hidden loss" narratives.
4. **The buyback lever is intact:** 15,550.1M → 15,460.2M → 15,441.9M shares (Sep → Dec → Jan 19). ~2.8% annualized shrink, and it is being executed *without* incremental debt (CP down $4.0B, term debt flat).

**Bear case — what the numbers also support:**
1. **Organic growth is only 2.1%.** Strip out margin expansion and this is a low-growth industrial. Any gross-margin give-back (component costs, mix, FX) removes the entire EPS beat. Model gross margin, don't model revenue.
2. **Quality-of-earnings flags in CFO.** Q1 CFO of $39.9B benefited from a $6.3B AR release and a $4.6B nontrade-receivables release — combined ~$10.9B of one-time working-capital tailwind, partly offset by a $4.5B AP paydown. **Normalize Q1 CFO toward ~$30–33B** before extrapolating FY24 FCF.
3. **Capex is abnormally low at 2.0% of revenue.** FCF margin of 31.4% contains a structural subsidy. A capex normalization toward 3% of revenue would cut annual FCF by ~$4–5B.
4. **EPS growth depends on the buyback.** FY23 proved it: net income fell $2.8B, EPS still rose $0.02. That is a fragile mechanism, and it means a *single* bad margin quarter hits EPS twice (earnings down + the market de-rating the repurchase-funded growth).
5. **Leverage optics.** Liabilities/equity of 3.77x and equity/assets of 21.0% mean book equity is a very thin cushion. Fine for a AAA-like cash generator, but it removes any "asset-backed floor" from valuation.

**Concrete monitoring triggers for the next 90 days:**
- **Gross margin below ~44%** in the fiscal Q2 (March-quarter) 10-Q → the margin trade is broken; expect EPS re-rating down.
- **Capex > $4B in a quarter** → FCF-margin compression narrative begins; cut FCF-based valuation.
- **Repurchase dollars > $25B in a quarter** → management signaling confidence in margin durability; add.
- **AOCI turning positive** (from −$9.4B) → hidden-loss overhang fully clears; multiple-supportive.
- **Effective tax rate >16.5%** → EPS estimates need trimming on a mechanical basis.
- **Cash & securities falling below $150B** → capital-return policy has turned more aggressive than cash generation; watch credit posture.
- **Insider Form 4s** — must be sourced externally; the signal is unknown, not neutral.

**Recommended framing (not a price target — no price data was available to my tools):** Treat AAPL as a **cash-flow-and-margin compounder with ~2% organic growth and a ~2.8% annual share shrink**, i.e. a low-double-digit EPS compounder if margins hold. On that basis, the relevant valuation anchors from this dataset are **~$4.18/share of net cash**, **~$4.80/share of book value**, and a **FY23 diluted EPS base of $6.13 growing at double digits** — traders should apply current-market multiples themselves.

---

## 10. Key Points Summary Table

| Category | Metric | Value | Read |
|---|---|---|---|
| **Latest filing** | 10-Q Q1 FY24 | Accepted 2024-02-02 | Fresh catalyst, 5 days old |
| **Revenue** | Q1 FY24 | $119,575M (+2.1% y/y) | Return to modest growth |
| **Gross profit** | Q1 FY24 | $54,855M (+9.0% y/y) | Beat vs 2.1% rev growth |
| **Gross margin** | Q1 FY24 | **45.9% (+290 bps y/y)** | ★ Primary bull driver |
| **COGS** | Q1 FY24 | $64,720M (−3.1% y/y) | Declining while revenue grows |
| **R&D** | Q1 FY24 | $7,696M (−0.2% y/y) | Flat — margin lever + pipeline watch |
| **SG&A** | Q1 FY24 | $6,786M (+2.7% y/y) | In line with revenue |
| **Operating income** | Q1 FY24 | $40,373M (+12.1% y/y) | 33.8% margin, +310 bps |
| **Net income** | Q1 FY24 | $33,916M (+13.1% y/y) | |
| **Diluted EPS** | Q1 FY24 | **$2.18 (+16.0% y/y)** | Buyback adds ~2.5 pts |
| **Effective tax rate** | Q1 FY24 | 15.9% (vs 15.8%) | Slow uptrend since 13.3% FY21 |
| **CFO** | Q1 FY24 | $39,895M (+17.3% y/y) | Incl. ~$10.9B WC release — not repeatable |
| **Capex** | Q1 FY24 | $2,392M (−36.8% y/y) | ★ 2.0% of rev — abnormally low |
| **Free cash flow** | Q1 FY24 | **$37,503M (+24.1% y/y)** | 31.4% FCF margin |
| **CFO / Net income** | Q1 FY24 | 1.18x | High earnings quality (with WC caveat) |
| **Buybacks** | Q1 FY24 | $20,139M | ~0.7% of shares/qtr |
| **Dividends** | Q1 FY24 | $3,825M ($0.24/sh) | +4.3% rate raise |
| **Payout / FCF** | Q1 FY24 | 63.9% | ↓ from 98–115% FY21–23 = dry powder |
| **Cash + securities** | 2023-12-30 | $172,575M | +$10.5B sequentially |
| **Total debt** | 2023-12-30 | $108,040M | CP cut 67% to $2.0B |
| **Net cash** | 2023-12-30 | **+$64,535M** | +$13.5B sequentially |
| **Net cash / share** | Derived | ~$4.18 | On 15,441.9M shares (2024-01-19) |
| **Current ratio** | 2023-12-30 | 1.07x (from 0.99x) | Back above 1.0 |
| **Quick ratio** | 2023-12-30 | 0.72x | Structural, sub-1 |
| **Debt / equity** | 2023-12-30 | 1.46x (from 1.79x) | Deleveraging |
| **Equity / assets** | 2023-12-30 | 21.0% (from 17.6%) | Thin but improving fast |
| **AOCI** | 2023-12-30 | −$9,378M (from −$11,452M) | Repairing on $3.0B unrealized gains |
| **Shareholders' equity** | 2023-12-30 | $74,100M (+$11,954M q/q) | +$17.4B y/y |
| **Shares outstanding** | 2023-12-30 | 15,460.22M | −89.8M q/q; ~2.8% annual shrink |
| **Debt maturity ladder** | FY24–28 | $9.9B / $10.8B / $12.3B / $9.8B / $7.8B | No refinancing cliff |
| **Deferred revenue** | 2023-12-30 | $12,500M (from $12,100M) | Recurring-revenue base growing |
| **FY23 net income** | Full year | $96,995M (derived) | Down from $99,803M FY22 |
| **FY23 diluted EPS** | Full year | $6.13 (from $6.11) | Growth entirely from buyback |
| **FY23 FCF** | Full year | $99,584M (derived) | From $111,443M FY22 |
| **Insider transactions** | — | **DATA UNAVAILABLE** | Do not infer; source externally |
| **Segment/geo detail** | — | **Not in dataset** | No China/mix claims made |
| **Price / valuation multiples** | — | **Not in dataset** | Apply market data externally |

---

### Bottom line
AAPL's fundamental picture as of 2024-02-07 is **"low growth, high quality, expanding margins, fortress balance sheet, deliberately under-distributed cash."** The fiscal Q1 2024 10-Q (filed five days ago) shows a company that grew revenue 2.1% but earnings 13.1% and EPS 16.0% by cutting cost of sales, holding opex flat, and shrinking its share count — while cutting commercial paper 67%, lifting net cash to $64.5B, and reducing its payout ratio to 63.9% of free cash flow. The bear rebuttal is entirely mechanical: revenue growth is thin, ~$10.9B of Q1's $39.9B operating cash flow was a non-repeatable working-capital release, capex is unsustainably low at 2.0% of revenue, and the tax rate is drifting higher. **The single variable that matters for the next two quarters is gross margin (~44% is the line in the sand); the single variable that matters for the next two years is capex.** Insider activity is unknown and must be sourced outside this toolset.