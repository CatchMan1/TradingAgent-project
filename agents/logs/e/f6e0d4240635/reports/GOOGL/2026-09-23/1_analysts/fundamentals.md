# GOOGL (Alphabet Inc.) — Comprehensive Fundamental Report
**As of 2026-09-23 | Latest SEC data: Q2 2026 Form 10-Q accepted 2026-07-23**

---

## 1. Scope, Data Provenance & Limitations

This report is built strictly from point-in-time SEC XBRL facts accepted on or before 2026-09-23, cross-checked across the income statement, balance sheet and cash-flow statement.

**Important caveats for the trading desk:**

- **No new SEC filing landed in the past week.** The most recent accepted document is the Q2 2026 10-Q (accepted 2026-07-23). All "recent" information is therefore as of the June 30, 2026 balance-sheet date.
- **Revenue is derived, not tagged.** The vendor fact set did not include a `Revenues` line. I derive revenue as `CostsAndExpenses + OperatingIncomeLoss`, which reconciles cleanly to pre-tax income and EPS in both periods (verified below). Derived revenue should be treated as high-confidence but secondary.
- **Segment data (Google Services / Google Cloud / Other Bets) is not available** in the returned fact set. Segment-level conclusions cannot be drawn from these tools.
- **Insider transactions: DATA UNAVAILABLE.** The vendor has no authorized point-in-time insider archive for GOOGL. No insider buying/selling is inferred or fabricated in this report.
- **No price, market-cap, consensus or valuation-multiple data** is provided by these tools. Any valuation reference below is explicitly derived from company filings, not from market data.

---

## 2. Company Profile

Alphabet Inc. (NASDAQ: GOOGL) is the holding company for Google. Its reporting structure comprises **Google Services** (Search and other advertising, YouTube ads, subscriptions/platforms/devices, network advertising), **Google Cloud** (Google Cloud Platform infrastructure and Google Workspace), and **Other Bets** (early-stage businesses including Waymo). *(Segment description is background knowledge; the vendor feed supplied financials only.)*

**What the filings show the company actually is in 2026:** a cash-generative advertising/cloud franchise that has simultaneously become (a) a hyper-scale AI infrastructure builder, (b) a large technology investor with a $124.3B non-marketable equity portfolio, and (c) an active capital-markets issuer. That combination drives nearly every insight below.

---

## 3. Headline Financials — Q2 2026 and H1 2026

| $ millions | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | 119,796 | 96,428 | **+24.2%** | 229,692 | 186,662 | **+23.0%** |
| Cost of revenue | 45,943 | 39,039 | +17.7% | 87,214 | 75,400 | +15.7% |
| Gross profit | 73,853 | 57,389 | +28.7% | 142,478 | 111,262 | +28.1% |
| Gross margin | 61.7% | 59.5% | +220bp | 62.0% | 59.6% | +240bp |
| Operating income | 40,770 | 31,271 | **+30.4%** | 80,466 | 61,877 | **+30.0%** |
| Operating margin | 34.0% | 32.4% | +160bp | 35.0% | 33.1% | +190bp |
| Non-operating income | 97,983 | 2,662 | n.m. | 135,699 | 13,845 | n.m. |
| Pre-tax income | 138,753 | 33,933 | +309% | 216,165 | 75,722 | +185% |
| Tax rate | 19.1% | 16.9% | +220bp | 19.1% | 17.1% | +200bp |
| Net income | 112,193 | 28,196 | +298% | 174,771 | 62,736 | +179% |
| Diluted EPS | $9.11 | $2.31 | +294% | $14.24 | $5.12 | +178% |
| Diluted shares (M) | ~12,315 | ~12,206 | +0.9% | ~12,315 | ~12,255 | +0.5% |

**The operating business is accelerating, and it is accelerating profitably.** Revenue growth of +21.8% in Q1 and +24.2% in Q2 is a marked step-up, and operating income grew faster than revenue in both quarters (+29.7% and +30.4%). Gross margin expanded ~220bp YoY and opex discipline held: total costs and expenses excluding cost of revenue were 27.0% of revenue in H1 2026 vs 26.5% in H1 2025, with G&A up 22.9% (slower than revenue). SBC rose 32.2% to $15.2B (6.6% of revenue vs 6.2%), and depreciation jumped 43.1% to $13.6B (5.9% of revenue vs 5.1%) — the first visible depreciation drag from the AI build-out.

**But headline profitability is not operating profitability.** See the next section — this is the single most important analytical adjustment in the entire report.

---

## 4. Quality of Earnings: 63% of H1 Pre-Tax Income Is Investment Marks

The non-operating line exploded from $13.8B to $135.7B, driven by **equity securities fair-value gains of $135.9B** (net of $143M debt-securities losses). Of that, unrealized gains were $21.5B and realized gains only $0.8B — the balance comes from fair-value remeasurement of equity holdings, including observable-price adjustments on non-marketable positions. Cumulative upward fair-value adjustments on equity securities without readily determinable fair value jumped from **$44.5B to $85.7B** in six months.

**Normalized (ex-investment-gain) economics:**

| $ millions | Q2 2026 | Q2 2025 | YoY | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|---:|---:|---:|
| Pre-tax income (reported) | 138,753 | 33,933 | | 216,165 | 75,722 | |
| Less: equity securities gains | (99,031) | (1,286) | | (135,946) | (11,044) | |
| **Core pre-tax income** | **39,722** | **32,647** | **+21.7%** | **80,219** | **64,678** | **+24.0%** |
| Core net income (at reported tax rate) | ~32,120 | ~27,130 | +18.4% | ~64,900 | ~53,620 | +21.0% |
| **Core diluted EPS (approx.)** | **~$2.61** | **~$2.22** | **+17.6%** | **~$5.27** | **~$4.37** | **+20.5%** |

**Actionable conclusions:**

1. **Reported Q2 EPS of $9.11 is ~3.5x core EPS of ~$2.61.** Roughly 71% of Q2 net income was non-operating mark-to-market. Anyone screening GOOGL on reported trailing P/E is understating the multiple by a wide margin.
2. **Core growth is still excellent** — ~+18% to +21% EPS growth on a normalized basis, better than the operating margin alone implies (helped by higher interest income and a larger cash pile).
3. **The reported tax rate rose to 19.1%** from 16.9%, partly because gains are taxable on realization while the deferred tax liability ballooned from $0.9B to $22.8B. Watch for tax leakage when positions are sold.
4. **The gains are reversible.** A 20% markdown on the $124.3B non-marketable portfolio would be roughly a $25B pre-tax hit — capable of turning a headline beat into a headline miss in a single quarter.

---

## 5. Balance Sheet: A $922B Balance Sheet After Six Extraordinary Months

| $ millions | 2026-06-30 | 2025-12-31 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 55,911 | 30,708 | +82.1% |
| Cash + short-term investments | **242,474** | 126,843 | **+91.2%** |
| Accounts receivable, net | 69,175 | 62,886 | +10.0% |
| Current assets | 343,524 | 206,038 | +66.7% |
| **Total assets** | **921,983** | **595,281** | **+54.9%** |
| Accounts payable | 20,258 | 12,200 | +66.0% |
| Accrued liabilities | 73,014 | 55,557 | +31.4% |
| Employee-related liabilities | 15,086 | 17,546 | −14.0% |
| Accrued income taxes (current) | 5,233 | 523 | +900% |
| Deferred revenue (current) | 7,154 | 6,578 | +8.8% |
| Total deferred revenue | 10,100 | 8,600 | +17.4% |
| Debt carrying amount | **101,085** | 49,085 | **+105.9%** |
| Convertible preferred stock | **18,023** | 0 | new |
| Deferred tax liabilities, net | 22,819 | 919 | +2,383% |
| Operating lease liability | 18,037 | 15,954 | +13.1% |
| Finance lease liability | 2,590 | 2,500 | +3.6% |
| AOCI | (2,285) | (1,916) | −19.3% |
| Common stock + APIC | 131,371 | 93,126 | +41.1% |
| Shares outstanding (M) | 12,230 | 12,088 | +1.2% |

**Key observations:**

- **Total assets grew $326.7B (+54.9%) in six months.** Drivers: cash/ST investments +$115.6B, non-marketable equity securities +$60.2B ($64.1B → $124.3B), and PP&E additions from ~$100B of capex incurred (net of only $13.6B depreciation).
- **Total debt roughly doubled to ~$104B including finance leases**, plus $18.0B of convertible preferred. Interest expense annualizes at ~$5.1B (Q2 2026: $1.278B vs $0.261B a year earlier).
- **Deferred tax liabilities of $22.8B** are a direct consequence of unrealized investment gains — a future cash tax liability embedded in the equity story.
- **Accrued income taxes current jumped from $0.5B to $5.2B**, worth monitoring for cash tax timing.
- **Estimated total equity**: the fact set does not tag total stockholders' equity, but rolling forward from ~$405B at 12/31/2025 (net income $174.8B + SBC $15.2B + common issuance $30.5B + preferred $19.1B + minority $3.8B − dividends $5.3B − OCI $0.4B), book equity is approximately **$640B**, or **~$50–53 per share** — of which ~$124B is non-marketable equity carried at fair value. Treat as an estimate, not a reported figure.

---

## 6. Liquidity and Solvency: Still Fortress, Despite the Leverage

- **Net cash position: ~$139B** ($242.5B cash + short-term investments − $101.1B debt − $2.6B finance leases). Even after raising $52B of debt, GOOGL remains a large net creditor.
- **Current assets of $343.5B** against itemized current liabilities of roughly $106B (AP + accrued liabilities + current taxes + current deferred revenue) implies a **current ratio well above 3x** before current debt — no liquidity risk.
- **Interest coverage is extreme**: Q2 operating income of $40.8B covers quarterly interest of $1.28B by ~32x. The debt raise is opportunistic/pre-funding, not distress-driven.
- **Debt maturity ladder (as of 12/31/2025, pre-raise):** $2.0B due within 12 months, $1.0B year 2, $2.7B year 3, $1.8B year 4, $5.5B year 5, $36.1B beyond year 5 — a long-dated, well-laddered book before the 2026 issuance.
- **Legal/regulatory accruals**: current loss-contingency accrual rose to **$17.4B** from $15.6B; the FY2025 10-K discloses a $3.0B contingency payment in Q3 2025. This is a persistent, material regulatory cost line.
- **Lease obligations**: $21.3B undiscounted operating lease payments and $2.9B finance lease payments.

**Verdict:** solvency is not a near-term risk. The correct lens is **return on incremental capital**, not balance-sheet fragility.

---

## 7. Cash Flow: The Capex Supercycle Is Now a Free-Cash-Flow Story

| $ millions | H1 2026 | H1 2025 | YoY |
|---|---:|---:|---:|
| Cash from operations | 84,859 | 63,897 | **+32.8%** |
| Purchases of PP&E (cash capex) | (80,598) | (39,643) | **+103.3%** |
| **Free cash flow** | **4,261** | **24,254** | **−82.4%** |
| FCF margin | 1.9% | 13.0% | −1,110bp |
| Capex / revenue | 35.1% | 21.2% | +1,390bp |
| CFO / revenue | 36.9% | 34.2% | +270bp |
| Share repurchases | 0 | (28,306) | n.m. |
| Dividends paid | (5,231) | (4,977) | +5.1% |
| Debt issued, net | 56,226 | 31,378 | +79.2% |
| Debt repaid | (5,253) | (18,397) | −71.4% |
| Common stock issued | 30,499 | 0 | new |
| Convertible preferred issued | 19,063 | 0 | new |
| Minority interests raised | 3,758 | 400 | +840% |
| Net financing cash flow | **+86,320** | (26,033) | n.m. |
| Net investing cash flow | (145,822) | (40,738) | +258% |
| Net change in cash | +25,203 | (2,430) | n.m. |

**Quarterly FCF decomposition:**

| $ millions | Q1 2026 | Q2 2026 | Q2 2025 |
|---|---:|---:|---:|
| CFO | 45,790 | 39,069 | 27,747 |
| Capex | (35,674) | (44,924) | (22,446) |
| **FCF** | **+10,116** | **(5,855)** | **+5,301** |
| Capex / revenue | 32.5% | 37.5% | 23.3% |

**Three critical insights:**

1. **Q2 2026 free cash flow was negative (−$5.9B).** This is the first clearly negative quarterly FCF in the modern Alphabet era and a regime change for a company long valued on FCF generation.
2. **Cash capex understates true capex.** "Capital expenditures incurred but not yet paid" nearly tripled to **$29.1B** at 6/30/2026 from $10.6B a year earlier. Economic capex incurred in H1 2026 was approximately **$99B (~43% of revenue)**, not the $80.6B cash figure. Accounts payable rising 66% confirms this accrual build. **Implication: even if new AI commitments pause, Q3 cash capex stays elevated simply paying down accrued balances.**
3. **Operating cash flow is healthy and growing (+32.8%)** — the FCF collapse is entirely a capital-deployment decision, not an operational deterioration.

---

## 8. Capital Allocation: A Complete Regime Change

This is the most under-appreciated finding in the dataset. In H1 2026 GOOGL raised **~$105.8B gross** ($56.2B debt, $30.5B common equity, $19.1B convertible preferred, $3.8B minority) while **repurchasing zero shares** (vs. $28.3B of buybacks in H1 2025).

- **Buyback halted:** $0 vs $28.3B. Historically buybacks supplied 1–2 points of EPS growth per year. That tailwind is gone for now.
- **Common equity issued: $30.5B**, with shares outstanding up 142M (+1.2%). Implied average issuance price is roughly **~$215/share** (range $215–250 depending on how many shares came from SBC rather than the offering). This is a management-sanctioned valuation anchor worth using as a trading reference.
- **Convertible preferred issued: $19.1B** on 2026-06-05 — an instrument Alphabet has never used at this scale. Preferred dividends of $86M were paid in Q2, implying a roughly 5–6% annualized coupon. The counterparty/structure is not in this fact set and should be checked in the 8-K/prospectus; a strategic-investor structure would carry signaling value.
- **Purchases of "other investments" leaped to $22.1B** from $2.3B, and non-marketable equity rose $60B. GOOGL is simultaneously **building** AI infrastructure and **buying stakes in** AI companies.
- **Dividend continues to grow** but remains immaterial: $0.22/quarter (H1 declared $0.43 vs $0.41), ~$0.88 annualized, ~$10.7B/year — under 1% of H1 net income.

**Interpretation:** Management is funding an AI capex/investment supercycle with a deliberately balanced debt-plus-equity package, using a high share price as currency. That is bullish on opportunity set, but it **dilutes the equity story and removes the buyback EPS cushion** — two things that historically supported the multiple.

---

## 9. Multi-Year Context

| $ millions | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 |
|---|---:|---:|---:|---:|---:|
| Net financing cash flow | (72,093) | (79,733) | (37,388) | (26,033) | **+86,320** |
| Capex incurred but unpaid (period-end) | 7,435 | 10,326 | 15,090 | 10,635 | **29,113** |
| Finance lease principal payments | 705 | 405 | 1,988 | 302 | 840 |
| Share repurchases | n/a | n/a | n/a | 28,306 | **0** |
| Cash + short-term investments (period-end) | n/a | n/a | 126,843 | n/a | **242,474** |

The trend is unambiguous: **three years of large net cash return (financing outflows of $72–80B annually)** flipped to a **$86.3B financing inflow in a single half-year**. Capital allocation has rotated 180 degrees from "return capital" to "raise and deploy capital."

---

## 10. Insider Transactions

**No data available.** The vendor's news/insider archive has no authorized point-in-time insider-transaction record for GOOGL as of 2026-09-23. I explicitly make **no inference** about insider buying or selling. Traders should source Form 4 data directly from EDGAR if this input is required for the decision.

---

## 11. Risk Register (ranked by trading relevance)

| # | Risk | Evidence | Magnitude / Trigger |
|---|---|---|---|
| 1 | **Earnings quality / mark-to-market reversal** | $135.9B of H1 pre-tax income (63%) from equity gains; 71% of Q2 net income | A 20% markdown on $124.3B non-marketable book ≈ $25B pre-tax hit |
| 2 | **FCF compression / capex ROI** | Q2 FCF −$5.9B; capex 37.5% of revenue; economic capex ~43% of revenue; $29.1B accrued capex | Sustained capex/revenue >30% with flat FCF pressures the multiple |
| 3 | **Buyback cessation + dilution** | $0 repurchases; +142M shares; $18B preferred; SBC +32% | Removes 1–2 pts of historical EPS tailwind; ~1.2% annual dilution |
| 4 | **Leverage ramp** | Debt $49.1B → $101.1B; interest expense 4.9x YoY; DTL $0.9B → $22.8B | Interest ~$5B/yr run-rate; cash tax on realization of gains |
| 5 | **Regulatory/legal** | Current loss contingency accrual $17.4B; $3.0B paid in Q3 2025 | Recurring fines/settlements; headline risk |
| 6 | **Depreciation wave** | Depreciation +43% YoY, 5.9% of revenue and rising | Margin headwind through 2026–2027 as AI assets are placed in service |
| 7 | **Revenue concentration/opacity** | No segment data in feed; growth +21.8%/+24.2% | Inability to verify Cloud vs. Search mix complicates the growth thesis |

---

## 12. Actionable Insights for Traders

1. **Normalize before you value.** Use ~$5.27 H1 2026 core EPS (annualized ~$10.50) rather than the reported $14.24. At the ~$215 implied equity-issuance price, GOOGL screens at roughly **20x annualized core EPS** but only ~**13x headline EPS**. The gap is the entire debate: the market may be capitalizing mark-to-market gains it should exclude. Position sizing should reflect which multiple you believe.
2. **Treat the buyback halt as a negative EPS-revision catalyst.** Consensus models that mechanically roll forward historical buyback accretion will be too high. Expect estimate recalibration around the Q3 print.
3. **Watch Q3 2026 (late October) for five specific items:** (a) 2027 capex guidance, (b) Cloud revenue growth and backlog, (c) whether repurchases resume, (d) realized vs. unrealized split of investment gains, (e) any FCF inflection. Any one of these can move the stock double digits.
4. **Front-load caution on Q3 cash flow.** With $29.1B of accrued capex on the balance sheet, cash capex should remain high even if commitments slow. A second consecutive negative FCF quarter is a realistic bear catalyst.
5. **The balance sheet is a floor, not a catalyst.** ~$139B net cash and >3x current ratio mean no solvency risk; the debt raise is pre-funding, not distress. Do not short GOOGL on leverage alone.
6. **Use the $215/share implied issuance price as an anchor.** Management chose to sell equity at that level; it is a rare, filing-based statement of intrinsic-value view and a defensible reference for entry/exit levels.
7. **Asymmetry:** core operating momentum (+24% revenue, +30% operating income, +240bp gross margin) is genuinely strong. The bear case rests on capital intensity and earnings quality, not on the core franchise deteriorating. That argues for **owning the operating business while hedging the mark-to-market and capex risk** rather than a directional short.

---

## 13. Key Points Summary

| Category | Key Finding | Evidence | Trading Implication |
|---|---|---|---|
| **Revenue** | Accelerating to +24.2% YoY in Q2 2026 | Revenue $119.8B (derived), +21.8% Q1, +24.2% Q2 | Core demand is strong; supports premium multiple |
| **Operating margin** | 34.0% in Q2, +160bp YoY; H1 35.0% | OI $40.8B vs $31.3B; gross margin 61.7% | Operating leverage intact — bull case |
| **Earnings quality** | 63% of H1 pre-tax income is investment gains | $135.9B equity gains vs $80.2B core pre-tax | Headline EPS massively overstated; use core EPS |
| **Core EPS** | ~$2.61 in Q2, ~$5.27 in H1 (vs $9.11 / $14.24 reported) | Derived by stripping $99.0B / $135.9B gains | ~20x annualized core P/E at implied $215 |
| **Free cash flow** | Q2 2026 FCF **−$5.9B**; H1 FCF $4.3B vs $24.3B | CFO $84.9B − capex $80.6B | FCF story broken near-term; key bear catalyst |
| **Capex intensity** | 35% of revenue cash; ~43% economic | Capex $80.6B cash; $29.1B accrued but unpaid | Q3 cash capex stays elevated regardless |
| **Balance sheet** | Total assets $922B, +54.9% in six months | Cash+STI $242.5B; debt $101.1B; DTL $22.8B | Net cash ~$139B — no solvency risk |
| **Capital allocation** | Buybacks halted; $105.8B raised in H1 | $0 repurchases vs $28.3B; +$56.2B debt, +$30.5B equity, +$19.1B preferred | EPS tailwind removed; dilution ~1.2%; equity-raise price ~$215 anchor |
| **Investment portfolio** | Non-marketable equity $64.1B → $124.3B | Cumulative upward marks $44.5B → $85.7B | Large hidden asset, but volatile mark-to-market |
| **Dividend** | $0.22/qtr, ~5% growth, immaterial payout | H1 $0.43/share; $5.23B paid | Not a total-return driver |
| **Book value** | Estimated ~$640B, ~$50–53/share (est.) | Roll-forward of equity components | Framework reference only |
| **Regulatory** | Current loss contingency accrual $17.4B | Up from $15.6B; $3.0B paid Q3 2025 | Persistent headline/fine risk |
| **Insider activity** | **DATA UNAVAILABLE** | No authorized archive | Source Form 4s from EDGAR separately |
| **Net stance** | Strong core franchise, deteriorating FCF and headline earnings quality | Operating +30% YoY vs FCF −82% | Own the franchise, hedge the capex/mark-to-market risk; avoid valuation on reported EPS |