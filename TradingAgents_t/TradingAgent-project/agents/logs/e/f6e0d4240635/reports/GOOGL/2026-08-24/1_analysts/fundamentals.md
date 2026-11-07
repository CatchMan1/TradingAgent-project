# GOOGL — Alphabet Inc. | Fundamental Deep-Dive
**Analysis date:** 2026-08-24 | **Latest filing in scope:** Form 10-Q for period ended 2026-06-30, accepted by EDGAR 2026-07-23 (accn 0001652044-26-000071); FY2025 Form 10-K accepted 2026-02-05 (accn 0001652044-26-000018)

---

## 0. Bottom Line Up Front

| # | Finding | Evidence | Trading implication |
|---|---|---|---|
| 1 | **Core operating momentum is exceptional and accelerating** — Q2'26 revenue +24.2% y/y with operating margin expanding to 34.0% (from 32.4%) | Revenue derived = OperatingIncomeLoss + CostsAndExpenses = $119,796M; op income $40,770M | The "AI capex destroys margins" bear case is not showing up in the P&L yet. Bullish for the core franchise. |
| 2 | **Headline EPS is ~70% non-operating** — $99.0B of Q2'26 pre-tax income was equity-security mark-ups | EquitySecuritiesFvNiGainLoss Q2 = $99,031M vs pretax $138,753M | Do **not** capitalize reported EPS. Reported $9.11 diluted vs ~$2.69 analyst-derived core. Big "quality of earnings" trap for screens. |
| 3 | **Free cash flow has effectively gone to zero** — H1'26 FCF $4.3B vs $24.3B (‑82%) | OCF $84,859M – PP&E purchases $80,598M; plus $29,113M capex incurred-but-unpaid | The single most important swing factor. Historically GOOGL was bought on FCF. That model is suspended. |
| 4 | **Capital allocation regime change** — buybacks = **$0** in H1'26 (vs $28.3B), share count **up** 1.2%, debt **doubled** | PaymentsForRepurchaseOfCommonStock $0; shares 12,088M→12,230M; debt $49.1B→$101.1B; +$19.1B convertible preferred; +$30.5B stock issuance | Loss of the EPS shrink-to-grow tailwind. New dilution/leverage variables. |
| 5 | **Balance sheet massively re-rated upward** — total assets +$326.7B in six months, book value roughly +$200B | Assets $595,281M → $921,983M; non-marketable equity $64,094M → $124,259M | Hidden asset value is real but marks are illiquid/private → high beta to AI private-market sentiment. |

---

## 1. Data Provenance & Explicit Limitations

I want to be transparent about what the tool layer did and did not give me, because several numbers below are **derived** rather than tagged:

1. **The vendor returned only an alphabetical prefix (A–D) of XBRL tags** for every statement call, in identical form regardless of `freq=quarterly` vs `annual`. Consequently:
   - The `Revenues` tag, segment revenues, R&D line, total liabilities, total stockholders' equity, and goodwill were **not returned**. I derive revenue from `OperatingIncomeLoss + CostsAndExpenses`; I cross-checked the derivation against known Q2'25/H1'25 figures ($96.4B / $186.7B) and it reconciles exactly to the cent, so I have high confidence in it.
   - Total equity below is an **estimate** built from the balance-sheet identity using the liability components that *were* disclosed (I flag it as estimated throughout).
2. **Full fiscal-year 2023/2024/2025 income statements and balance sheets were not retrievable.** Only a handful of 10-K cash-flow items came through. So "financial history" here is limited to (a) H1'25 vs H1'26, (b) Q2'25 vs Q2'26, and (c) three years of 10-K capex/financing data points.
3. **Insider transactions: `DATA_UNAVAILABLE`.** The vendor has no authorized point-in-time insider archive for GOOGL as of 2026-08-24. **I have not inferred, estimated, or fabricated any insider buying or selling.** Treat this as an open item requiring a different data source.
4. **No share price or market data was provided**, so I cannot compute P/E, EV/EBITDA, or P/B. I instead deliver **EPS and per-share run-rates** so the valuation agent can apply its own multiple.
5. Next scheduled catalyst: **Q3 2026 results (~late October 2026)**, i.e. one month of post-print drift already elapsed since the 2026-07-23 filing.

---

## 2. Company Profile (background only — not tool-confirmed)

Alphabet Inc. (ticker **GOOGL**, Class A) is the parent of Google. Its reporting structure is Google Services (Search & other, YouTube ads, Android/Chrome/Play, subscriptions-devices-tech, plus Google's first-party AI offerings), Google Cloud (infrastructure + Workspace + AI/enterprise platforms), and Other Bets (pre-revenue / early-revenue long-horizon ventures funded partly by outside capital). Alphabet has paid a quarterly dividend since 2024 and, until this year, ran one of the largest buyback programs in the market. I could not verify segment-level revenue or margins from the tool output — the segment tables did not return — so all quantitative analysis below is **consolidated**.

---

## 3. Q2 2026 Income Statement Scorecard (quarter ended 2026-06-30)

| $M | Q2 2026 | Q2 2025 | Δ y/y |
|---|---:|---:|---:|
| Revenue (derived) | **119,796** | 96,428 | **+24.2%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% |
| Gross profit | 73,853 | 57,389 | +28.7% |
| **Gross margin** | **61.6%** | 59.5% | +210 bps |
| Operating expenses (derived) | 33,083 | 26,118 | +26.7% |
| Opex % of revenue | 27.6% | 27.1% | +50 bps |
| **Operating income** | **40,770** | 31,271 | **+30.4%** |
| **Operating margin** | **34.0%** | 32.4% | **+160 bps** |
| Non-operating income | 97,983 | 2,662 | +3,581% |
| *of which equity-sec FV gains* | *99,031* | *1,286* | — |
| Pre-tax income | 138,753 | 33,933 | +309% |
| Tax | 26,560 | 5,737 | +363% |
| **Effective tax rate** | **19.1%** | 16.9% | +220 bps |
| Net income | 112,193 | 28,196 | +298% |
| NI to common (after $86M pref divs) | 112,107 | 28,196 | — |
| **Diluted EPS** | **$9.11** | $2.31 | +294% |
| **Analyst-derived core EPS (ex-marks)** | **≈$2.69** | ≈$2.18 | **+23.4%** |

**How I built core EPS** (an estimate, disclosed as such): take operating income, add net interest (interest income $1,430M less interest expense $1,278M), tax at the reported 19.1%/16.9%, divide by diluted shares (~12,306M / ~12,206M). This strips out the equity-security marks, which are non-cash and non-recurring in nature.

**Interpretation:** The quarter is a tale of two companies. The *operating* company grew revenue 24% and expanded operating margin 160bps at a ~$480B annualized revenue run-rate — superb operating leverage. The *investment* company contributed $99B of pre-tax gains from marking up equity stakes, tripling reported EPS. **A screen on reported EPS would value GOOGL at one-third of its true operating earnings power relative to history** — the correct anchor is the ~$2.69 core number.

---

## 4. First-Half 2026 Numbers & Trend

| $M | H1 2026 | H1 2025 | Δ y/y |
|---|---:|---:|---:|
| Revenue (derived) | **229,692** | 186,662 | **+23.0%** |
| Cost of revenue | 87,214 | 75,400 | +15.7% |
| Gross margin | 62.0% | 59.6% | +240 bps |
| Operating expenses | 62,012 | 49,385 | +25.6% |
| **Operating income** | **80,466** | 61,877 | **+30.0%** |
| **Operating margin** | **35.0%** | 33.2% | +180 bps |
| Non-operating income | 135,699 | 13,845 | +880% |
| Pre-tax income | 216,165 | 75,722 | +185% |
| Tax | 41,394 | 12,986 | +219% |
| **Net income** | **174,771** | 62,736 | +179% |
| **Diluted EPS** | **$14.24** | $5.12 | +178% |
| Diluted shares (implied) | ~12,270M | ~12,253M | +0.1% |
| SBC (included in opex) | **15,200** | 11,500 | **+32.2%** |
| SBC % of revenue | 6.6% | 6.2% | +40 bps |
| G&A | 10,752 | 8,748 | +22.9% |
| Depreciation | 13,586 | 9,485 | +43.2% |
| Amortization of intangibles | 545 | 246 | +122% |

**Quarterly decomposition (derived by subtraction):**

| $M | Q1'26 | Q2'26 | Q/Q |
|---|---:|---:|---:|
| Revenue | 109,896 | 119,796 | +9.0% |
| Operating income | 39,696 | 40,770 | +2.7% |
| Operating margin | 36.1% | 34.0% | −210 bps |
| Net income | 62,578 | 112,193 | +79% |
| Diluted EPS | ~$5.18 | $9.11 | — |

**Two important nuances:**
- **Revenue growth accelerated** from +21.8% in Q1'26 to +24.2% in Q2'26 — a genuine re-acceleration, not a decelerating comp.
- **But Q2 operating margin (34.0%) compressed 210bps sequentially from Q1 (36.1%).** Opex dollars rose from $28.9B to $33.1B q/q (+14.3%) on a 9.0% revenue increase. This is the first quantitative evidence of cost ramp (compute, AI R&D, and SBC +33% y/y) beginning to bite. Watch this line closely next quarter — if opex grows mid-teens again it caps the margin-expansion story.

**SBC quality-of-earnings flag:** SBC of $15.2B (+32.2% y/y, 6.6% of revenue) is growing meaningfully faster than revenue. SBC-adjusted H1 EBITDA = op income $80,466 + D&A $13,586 + intangible amortization $545 − SBC $15,200 = **$79,397M (34.6% margin)**, versus reported operating margin of 35.0%. The gap is widening.

---

## 5. The $136 Billion Question: Non-Operating Income

This is the most under-appreciated item in the release and deserves its own section.

| $M | H1 2026 | H1 2025 |
|---|---:|---:|
| Equity securities FV gain, total | **135,946** | 11,044 |
| — realized | 836 | 435 |
| — unrealized | 21,531 | 1,088 |
| — "impiled / remeasurement" balance (135,946 − 836 − 21,531) | **113,579** | 9,521 |
| Debt securities gain/(loss) | (143) | 367 |
| Interest income | 2,811 | 2,051 |
| Interest expense | (1,811) | (295) |
| FX loss | (14) | (175) |
| **Non-operating income total** | **135,699** | 13,845 |
| Non-op as % of pre-tax income | **62.8%** | 18.3% |

**What this looks like economically:** Alphabet holds large stakes in AI-era private companies. The carrying value of equity securities **without readily determinable fair value exploded from $64,094M (12/31/25) to $124,259M (6/30/26)** — a $60.2B increase — while **cumulative upward price adjustments jumped from $44,485M to $85,732M**. The ~$113.6B of "other" gain is consistent with re-measurement of positions that obtained observable prices (i.e., IPO/secondary events) and moved out of the non-marketable bucket into marketable equity securities, generating a one-time catch-up gain through the income statement.

**Three things a trader must do with this:**
1. **Exclude it from earnings multiples.** It is a mark, not an annuity. But *do not* ignore it either — it is real net worth and it proves Alphabet's venture portfolio is worth multiples of book.
2. **Recognize the reversal risk is symmetric.** These marks flow through the same line on the way down. A 30% drawdown in the AI private complex would create a ~$37B pre-tax hit with no operating impact but enormous headline-EPS optics. **Any long-vol / event structure around sentiment on private AI valuations is now a GOOGL trade.**
3. **Note the cash-tax shield:** DTL rose from $919M to $22,819M (+$21.9B) largely on these marks, and deferred tax assets net *fell* from $9,113M to $1,448M. The tax on the gains is deferred, not paid — but it is a real future claim, and it means the effective rate (19.1% vs 16.9%) is likely to stay structurally above 2025 levels.

---

## 6. Balance Sheet: A Balance Sheet That Doubled in Six Months

| $M | 2026-06-30 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| **Cash + short-term investments** | **242,474** | 126,843 | **+91.2%** |
| AFS debt securities (fair value) | 99,500 | n/a | — |
| Accounts receivable, net | 69,175 | 62,886 | +10.0% |
| Allowance / gross AR | 1.4% | 1.5% | — |
| Current assets | 343,524 | 206,038 | +66.7% |
| Equity securities w/o RDFV | **124,259** | 64,094 | **+93.9%** |
| Finite-lived intangibles, gross | 10,585 | 2,467 | +329% |
| **Total assets** | **921,983** | 595,281 | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| Employee-related liabilities | 15,086 | 17,546 | −14.0% |
| Contract liabilities (deferred revenue), total | **10,100** | 8,600 | **+17.4%** |
| Loss contingency accrual (current) | **17,356** | 15,594 | +11.3% |
| Debt, carrying amount | **101,085** | 49,085 | **+105.9%** |
| Operating lease liability | 18,037 | 15,954 | +13.1% |
| Finance lease liability | 2,590 | 2,500 | +3.6% |
| Deferred income tax liabilities, net | **22,819** | 919 | +2,383% |
| **Convertible preferred stock** | **18,023** | 0 | new |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| AOCI | (2,285) | (1,916) | — |
| **Est. total equity (derived, see caveat)** | **~$606,000** | ~$406,000 | **+~$200,000** |
| **Est. book value per share** | **~$49.6** | ~$33.6 | — |

*Total equity is derived as Total assets less the sum of all disclosed liability components (≈$297.7B at 6/30/26; ≈$189.0B at 12/31/25). Because some liability lines (current portion of long-term debt, current operating lease, other noncurrent liabilities) were not returned by the tool, treat the ~$606B / ~$49.6 BVPS as an estimate with maybe ±$15–25B of error. The directional change (+~$200B) reconciles well against NI $174.8B + SBC $15.2B + stock issued $30.5B + minority $3.8B − divs $5.3B.*

**What the balance sheet is telling you:**

- **Still a net-cash fortress.** Cash + ST investments $242.5B vs total debt $101.1B = **~$141B net cash**. Even after the debt binge, leverage is not a solvency issue. Interest coverage on operating income ($80.5B H1) against interest expense ($1.81B H1) is ~44x.
- **But the *velocity* of the change is the signal.** Debt +106% and interest expense +514% in six months. Annualizing Q2 interest expense ($1,278M × 4) gives a ~$5.1B/year run-rate versus ~$1.2B in FY2025 — a ~$3.9B headwind to future net income, or roughly $0.32/share. Still small, but it is now a line item people will model.
- **The $19.1B convertible preferred (issued 2026-06-05) is the newest and least-understood dilution vector.** Preferred dividends of $86M appear for the first time. Conversion terms were not in the returned data. **Action item: obtain the preferred's conversion price and reset features from the 10-Q notes** — if conversion is near-the-money, this is a permanent share-count overhang layered on top of the paused buyback.
- **$30.5B of common stock issued** (shares 12,088M → 12,230M, +1.2%) alongside finite-lived intangibles gross jumping from $2,467M to $10,585M and DTL +$21.9B is the classic fingerprint of a **large, largely stock-funded acquisition** (likely an AI/IP asset, given the intangible and deferred-tax pattern). **The tool data does not disclose goodwill or the acquired entity** — a material information gap. If a deal closed in Q2, check whether revenue contribution is organic or inorganic; the +24.2% might include a partial-period acquisition benefit.
- **Working capital is inflating:** AP +66% and accrued liabilities +31% alongside $29,113M of capex incurred-but-unpaid (vs $10,635M a year ago) means a meaningful chunk of the AI build is sitting in payables. That is flattering to reported H1 operating cash flow and **will reverse into a cash drag** in H2'26/Q1'27.
- **Deferred revenue +17.4% to $10.1B** (current portion $7.15B, up 8.8%) with $4.9B of the opening balance recognized in H1 — a healthy, if unspectacular, forward-demand indicator. Watch Cloud backlog commentary at Q3.
- **Loss contingency accrual $17.36B (+$1.76B in six months)**, plus $3.0B of actual payments disclosed in the FY2025 10-K for Q3'25. That is a very large legal/regulatory liability — consistent with major antitrust/ad-tech exposure. It is already provided for, so it is a cash-flow and headline item rather than a new balance-sheet shock, but a fresh adverse ruling above the accrual is a live tail risk.

---

## 7. Cash Flow: The Capex Shock Is the Whole Story

| $M | H1 2026 | H1 2025 | Δ |
|---|---:|---:|---:|
| **Operating cash flow** | **84,859** | 63,897 | **+32.8%** |
| Purchases of PP&E | **(80,598)** | (39,643) | **+103.3%** |
| **Free cash flow (OCF – capex)** | **4,261** | 24,254 | **−82.4%** |
| FCF margin | **1.9%** | 13.0% | −1,110 bps |
| Capex / revenue | **35.1%** | 21.2% | +1,390 bps |
| Capex / depreciation | **5.9x** | 4.2x | — |
| Purchases of marketable securities, net of maturities | (9,784) | +1,060 | — |
| Purchases of other (non-marketable) investments | (22,051) | (2,312) | **+853%** |
| **Investing cash flow** | **(145,822)** | (40,738) | +258% |
| Debt issued, net | +56,226 | +31,378 | +79% |
| Repayment of debt/lease obligations | (5,253) | (18,397) | −71% |
| **Common stock repurchases** | **0** | (28,306) | **−100%** |
| **Common stock issued** | **+30,499** | 0 | new |
| Convertible preferred issued | +19,063 | 0 | new |
| Minority interest proceeds (Other Bets) | +3,758 | 400 | +840% |
| Dividends paid | (5,231) | (4,977) | +5.1% |
| **Financing cash flow** | **+86,320** | (26,033) | — |
| Net change in cash | +25,203 | (2,430) | — |

**The three things that matter:**

1. **FCF at 1.9% of revenue is a regime shift, and it is deliberate.** Capex of $80.6B in six months (Q1 $35.7B, Q2 $44.9B — still *accelerating* quarter-over-quarter) plus $29.1B of unpaid accrued capex implies a **true H1 capex commitment near $110B, or ~48% of revenue**. Annualized, this points to a 2026 capex program plausibly in the **$190–210B** range. This is the entire investment case for the next 18 months: either this converts into revenue/margin in 2027–28, or GOOGL becomes a capital-intensive industrial with a permanently lower FCF multiple.
2. **The depreciation wave is the under-modeled risk.** Capex/depreciation of 5.9x, with depreciation already +43% y/y. Even with zero incremental capex, D&A must roughly triple over the next 8–12 quarters as this asset base turns on. On H1 revenue of $229.7B and D&A of $13.6B (5.9%), a move to 15% of revenue would be an **~$21B/year incremental operating-cost headwind** — roughly 400bps of operating margin. **This is why the opex line in Q2 (margin −210bps q/q) needs monitoring; it's the leading edge of the same problem.**
3. **The financing engine flipped from shrinking the float to raising capital.** Compare: financing outflows of −$72.1B (FY2023), −$79.7B (FY2024), −$37.4B (FY2025) versus **+$86.3B in H1'26 alone**. This is the single cleanest historical datapoint I could extract, and it tells the whole capital-allocation story: the buyback was sacrificed to fund the build, and then management went a step further and raised third-party capital (debt, convertible preferred, minority equity at the Other Bets level).

**Cash-quality scorecard:** OCF/GAAP net income = 0.49x (depressed purely by the $135.9B non-cash equity gains). **OCF / core net income ($65.9B) = 1.29x — healthy.** The earnings are cash-backed; it's the *capex* that ate the cash, not accrual games.

---

## 8. Financial History (limited by tool truncation)

The only true multi-year series the vendor surfaced was capex accruals and financing flows:

| $M | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 |
|---|---:|---:|---:|---:|---:|
| Capex incurred but not yet paid (period end) | 7,435 | 10,326 | 15,090 | 10,635 | **29,113** |
| Net cash from financing | (72,093) | (79,733) | (37,388) | (26,033) | **+86,320** |
| Finance lease principal payments | 705 | 405 | 1,988 | 302 | 840 |
| Operating lease payments | — | — | — | 1,661 | 1,817 |

**Reading:** capex accruals have grown ~4x since FY2023 and nearly tripled in six months. Financing has swung +$158B from FY2024's outflow to H1'26's inflow. Both lines confirm the same thesis independently. **Caveat: I could not retrieve FY2023/FY2024/FY2025 revenue, net income or EPS from the tool** — I recommend a follow-up call with a vendor that isn't truncating, because a proper 5-year ROIIC and ROE trend is essential to judge whether the capex program is earning its keep.

---

## 9. Profitability, Returns & Quality Metrics (Analyst-Derived)

| Metric | H1 2026 | H1 2025 | Comment |
|---|---:|---:|---|
| Gross margin | 62.0% | 59.6% | +240bps **despite** AI compute costs — strong AI monetization signal |
| Operating margin | 35.0% | 33.2% | +180bps |
| SBC-adjusted EBITDA margin | 34.6% | 32.1% | +250bps |
| R&D+opex intensity (derived) | 27.0% | 26.5% | Expense growth slightly outpacing revenue |
| Net margin (GAAP) | 76.1% | 33.6% | Distorted by marks |
| Core net margin (est.) | 28.7% | 28.3% | +40bps — the *real* profitability trend |
| Effective tax rate | 19.1% | 17.1% | +200bps structural headwind |
| Annualized core ROE (est.) | ~26% | ~26% | Solid, not spectacular, on the inflated equity base |
| Cash conversion (OCF/core NI) | 1.29x | 1.21x | Improving |
| FCF margin | 1.9% | 13.0% | **The problem** |
| Core EPS run-rate (Q2 × 4) | **≈$10.75** | ≈$8.73 | +23% |
| H1 core EPS × 2 (annualized) | **≈$10.74** | ≈$8.64 | +24% |

**Core EPS run-rate of ~$10.75 is the number to hand to the valuation model.** For reference, reported trailing GAAP will show something like $17–18 because of the $136B of marks — a screen on that basis would make GOOGL look 40% cheaper than it is. Reported Q2'26 diluted EPS: $9.11 (basic $9.23, so ~1.3% dilution from options/RSUs — a normal load).

---

## 10. Insider Transactions

**DATA_UNAVAILABLE.** The configured data vendor has no authorized, point-in-time insider-transactions archive for GOOGL as of 2026-08-24. Per instructions, **no inference or fabrication has been made**. This is a genuine information gap for the report: insider behavior is particularly informative right now given (a) a paused buyback, (b) first-ever common stock issuance in years, (c) a $19B convertible preferred issuance, and (d) reported EPS at an all-time high on mark-to-market gains. **Recommendation: source Form 4 data separately** and specifically scrutinize any accelerated/10b5-1 sales by the founders or the CFO in the June–August 2026 window, and any open-market purchases by directors around the 2026-06-05 preferred deal.

---

## 11. Actionable Insights for Traders

### Bullish setup (highest-conviction)
- **Revenue re-acceleration to +24.2% with +160bps operating margin expansion at a ~$480B run-rate** is the strongest fundamental datapoint in the file. Combined with gross margin +210bps *while* absorbing AI compute, it argues the AI investment is already revenue- and margin-accretive, not dilutive. **Core operating earnings power is compounding ~24%/year.**
- **$242.5B of cash and investments against $101.1B of debt** (~$141B net cash) funds the entire capex program internally for multiple years. There is no funding cliff.
- **Hidden asset value**: non-marketable equity $124.3B carrying value with $85.7B of cumulative upward adjustments — the portfolio (AI labs, space, frontier tech) is a call option on private AI valuations that is not in anyone's operating model. The 18-month evidence is that these marks go *up* in round lots.
- Deferred revenue +17.4% and healthy AR/DSO behavior (AR +10% vs revenue +23%) confirm no demand or collections deterioration.

### Bearish / risk setup (what to watch, and when)
1. **FCF is ~zero and capex is still accelerating sequentially ($35.7B → $44.9B).** If Q3 capex prints >$50B, the "spend now, earn later" narrative loses patience. **Target: any print above ~$55B quarterly capex is a sell-the-earnings event** on FCF-focused flows.
2. **Q2 operating margin compressed 210bps sequentially.** If Q3 shows a second consecutive sequential compression, the operating-leverage thesis breaks. **Doorway: opex growth above ~+14% q/q.**
3. **Mark-to-market reversal risk on the $136B gain.** A 25–30% drawdown in private AI valuations mechanically removes ~$31–37B of pre-tax income. Watch funding-round news at Anthropic/OpenAI-class names and any IPO postponements as the leading indicator; GOOGL's reported EPS is now a levered play on that sentiment.
4. **Buyback = $0, share count +1.2%, SBC +32%, plus an unquantified $19B convertible preferred.** Cumulative dilution is now a headwind, not a tailwind, for the first time in a decade. Get the conversion terms.
5. **The acquisition accounting is opaque.** +$8.1B of finite-lived intangibles, +$21.9B DTL, +$30.5B stock issued, goodwill not disclosed in the returned data. **Determine whether Q2's +24.2% includes inorganic revenue** — if a point or two is inorganic, the organic growth rate is lower than it appears.
6. **Legal/regulatory:** $17.36B accrued (+$1.76B in six months) with $3.0B of payments already made. Accrued-but-unresolved liability of this size means an adverse ruling above the provision is a genuine gap-risk event.

### Concrete levels/framework to trade against
- **Anchor valuation on ~$10.75 annualized core EPS**, not the ~$17–18 GAAP number. Assuming the market's historical ~25x multiple on core, the operating business alone justifies ~$269/share of value; the *incremental* question is whether the market will pay anything for the $124B private portfolio, the $141B net cash, and the AI capex optionality. If the stock is trading at or below ~22x core EPS, that is a compelling entry given +24% core growth (PEG < 1).
- **Depreciation is the sneaky 2027 story**: at capex/depreciation of 5.9x, D&A must roughly triple. A useful stress test: assume D&A reaches 15% of revenue by 2028. That is roughly −400bps of operating margin from here, or ~$6 of core EPS risk on today's revenue base. **Anyone modeling margin expansion to 40% is wrong on this math.**
- **Event calendar:** Q3'26 print (~late Oct 2026) — watch three lines only: (1) quarterly capex, (2) sequential opex growth, (3) the non-operating income line and any commentary on the private portfolio.
- **Relative-value/hedge idea:** GOOGL is now simultaneously a high-growth operating compounder *and* a long position in private AI equity. If an expression exists to be long the core operating business while short private AI sentiment (e.g., via a basket of listed AI-adjacent names that have already marked up 2–5x), the reported-EPS disconnect creates a structural mispricing around print dates.

### Open items requiring a different data source
1. Insider transactions (**DATA_UNAVAILABLE** — do not assume either way).
2. Segment revenue/margin (Google Services / Google Cloud / Other Bets) — the single biggest analytical hole; Cloud margin trend is the best proxy for whether the capex is monetizing.
3. Goodwill and the identity/timing/size of the Q2'26 acquisition.
4. Convertible preferred terms (conversion price, reset, dividend rate, call features).
5. FY2023–FY2025 income statements (vendor truncated to A–D tags) for a proper multi-year ROIC/ROE trend.
6. Share price and consensus — needed to convert the core EPS framework into a buy/sell decision.

---

## 12. Key Points Summary Table

| Category | Metric | Value | Change | Signal |
|---|---|---|---|---|
| **Growth** | Q2'26 revenue (derived) | $119,796M | +24.2% y/y | 🟢 Accelerating (Q1 was +21.8%) |
| | H1'26 revenue | $229,692M | +23.0% y/y | 🟢 |
| | Contract liabilities (deferred rev.) | $10,100M | +17.4% vs 12/31/25 | 🟢 Forward demand |
| **Margins** | Q2'26 gross margin | 61.6% | +210bps | 🟢 AI compute absorbed |
| | Q2'26 operating margin | 34.0% | +160bps y/y, **−210bps q/q** | 🟡 Watch opex ramp |
| | H1'26 operating margin | 35.0% | +180bps | 🟢 |
| | SBC-adjusted EBITDA margin | 34.6% | +250bps | 🟢 |
| **Earnings quality** | Reported Q2'26 diluted EPS | $9.11 | +294% | 🔴 70% from non-operating marks |
| | **Core EPS (ex-marks, est.)** | **≈$2.69** | **+23.4%** | 🟢 The real number |
| | Core EPS annualized run-rate | ≈$10.75 | +23% | → Use for valuation |
| | Non-op income / pre-tax income | 62.8% (H1) | vs 18.3% | 🔴 Symmetric reversal risk |
| | Equity securities FV gains (H1) | $135,946M | vs $11,044M | 🟡 Real but non-cash |
| | Effective tax rate | 19.1% | +200bps | 🔴 Structural headwind |
| **Cash flow** | Operating cash flow (H1) | $84,859M | +32.8% | 🟢 |
| | Capex (H1) | $80,598M | +103.3% | 🔴 35.1% of revenue |
| | **Free cash flow (H1)** | **$4,261M** | **−82.4%** | 🔴 FCF margin 1.9% |
| | Capex incurred but unpaid | $29,113M | vs $10,635M | 🔴 Flatters H1 OCF |
| | Capex / depreciation | 5.9x | vs 4.2x | 🔴 D&A wave coming |
| **Balance sheet** | Total assets | $921,983M | +54.9% in 6 months | 🟢 |
| | Cash + ST investments | $242,474M | +91.2% | 🟢 |
| | Total debt | $101,085M | **+105.9%** | 🟡 Doubled but still net cash |
| | Net cash position | **~$141,389M** | — | 🟢 Fortress |
| | Convertible preferred stock | $18,023M | new (issued 2026-06-05) | 🟡 Dilution unknown |
| | Non-marketable equity holdings | $124,259M | +93.9% | 🟢 Hidden value |
| | Est. book value / share (derived) | ~$49.6 | vs ~$33.6 | 🟢 |
| | Loss contingency accrual | $17,356M | +11.3% | 🔴 Legal/regulatory |
| | Deferred tax liabilities, net | $22,819M | vs $919M | 🟡 Tax on unrealized gains |
| **Capital allocation** | Buybacks (H1'26) | **$0** | vs $28,306M | 🔴 Regime change |
| | Common stock issued | $30,499M | vs $0 | 🔴 Shares +1.2% to 12,230M |
| | Debt issued, net | $56,226M | vs $31,378M | 🟡 |
| | Dividends paid | $5,231M ($0.22/qtr, $0.88 ann.) | +5.1% | 🟢 Minor |
| | Financing cash flow | **+$86,320M** | from −$26,033M | 🔴 Shift to capital raising |
| | FY23/24/25 financing | −$72.1B / −$79.7B / −$37.4B | — | Historical context |
| **Insider** | Insider transactions | **DATA_UNAVAILABLE** | — | ⚪ Gap — source separately |
| **Filings** | Latest 10-Q | Period 2026-06-30, filed 2026-07-23 | — | ⚪ ~1 month old |
| | Latest 10-K | FY2025, filed 2026-02-05 | — | ⚪ |

**One-sentence thesis:** GOOGL's operating business is compounding revenue at ~24% with expanding margins and a $141B net-cash fortress, but reported EPS is now dominated by $136B of private-equity marks, free cash flow has collapsed to ~2% of revenue on a >$190B annualized capex program, and the decade-long buyback tailwind has flipped to net dilution — making this a *core-operating-earnings* story (anchored on ~$10.75 of annualized core EPS) rather than the reported-EPS or FCF story the market has historically used to value it.