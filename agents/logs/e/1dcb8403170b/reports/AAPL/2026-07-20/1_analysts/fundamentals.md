# AAPL — Fundamental Deep-Dive Report
**Valuation date:** 2026-07-20 | **Latest reported period:** Q2 FY2026 (quarter ended 2026-03-28), 10-Q filed 2026-05-01
**Data provenance:** Point-in-time SEC XBRL facts (10-K filed 2025-10-31; Q1 FY26 10-Q filed 2026-01-30; Q2 FY26 10-Q filed 2026-05-01). All figures USD. Insider-transaction archive: **unavailable** for AAPL as of 2026-07-20 (see caveats). Price/market-cap data is not served by these tools — no valuation multiples are computed or implied below.

---

## 1. Company Profile & Snapshot

**Apple Inc. (AAPL)** — designer/manufacturer of iPhone, Mac, iPad and Wearables/Home/Accessories, plus a large high-margin Services franchise (App Store, iCloud, Music, advertising, AppleCare, payments). Extreme vertical integration (silicon, OS, retail), heavily outsourced assembly, and a capital-return model historically funded by ~100%+ of free cash flow.

| Snapshot (as of 2026-03-28 unless noted) | Value |
|---|---|
| 6M FY26 revenue | $254.94B (+16.1% YoY) |
| 6M FY26 net income / diluted EPS | $71.68B / **$4.85** (+17.3% / +19.8%) |
| 6M FY26 operating cash flow / FCF | $82.63B / **$78.28B** (+53.3% / +63.5%) |
| Total assets / liabilities / equity | $371.08B / $264.59B / **$106.49B** |
| Cash + marketable securities | $146.60B |
| Total debt (LT + current + CP) | $84.71B → **net cash ≈ $61.9B** |
| Shares outstanding | 14.668B (14.687B at 2026-04-17) |
| Quarterly dividend | $0.26 (annualized $1.04, +4% YoY) |

**Structural note on the dataset:** the XBRL feed tags the *December* quarter's revenue indirectly. Reconstructing from period-over-period bridges (6M less March-quarter, and revenue − COGS = gross profit) gives a fully internally consistent picture: **Dec-2025 quarter revenue $143.76B** and **Mar-2026 quarter revenue $111.18B**. Every cross-check (GP, opex, pretax, tax, net income, EPS, COGS) ties out within $1–2M; I use the reconstructed values below.

---

## 2. Income Statement — Growth Re-Accelerated, Margins at Records

### 2.1 Quarterly reconstruction
| $B | Q1 FY25 (Dec-24) | Q2 FY25 (Mar-25) | Q1 FY26 (Dec-25) | Q2 FY26 (Mar-26) | Q1 YoY | Q2 YoY |
|---|---|---|---|---|---|---|
| Revenue | 124.30* | 95.36 | **143.76*** | **111.18** | **+15.7%** | **+16.6%** |
| Gross profit | 58.28* | 44.87 | 69.23* | 54.78 | +18.8% | +22.1% |
| Gross margin | 46.9% | 47.1% | **48.2%** | **49.3%** | +128bp | +224bp |
| R&D | 8.27* | 8.55 | 10.89* | 11.42 | +31.7% | +33.6% |
| SG&A | 6.73* | 6.73 | 7.49* | 7.48 | +11.4% | +11.1% |
| Operating income | 42.83* | 29.59 | 50.85* | 35.89 | +18.7% | +21.3% |
| Op. margin | 34.5% | 31.0% | 35.4% | 32.3% | +90bp | +130bp |
| Pre-tax income | 42.58* | 29.31 | 51.00* | 35.83 | +19.8% | +22.2% |
| Tax | 6.25* | 4.53 | 8.91* | 6.26 | +42.4% | +38.2% |
| Net income | 36.33 | 24.78 | 42.10 | 29.58 | +15.9% | +19.4% |
| Diluted EPS | 2.40 | 1.65 | **2.84** | **2.01** | +18.3% | **+21.8%** |

*\*derived from 6M-minus-quarter bridges; all derived lines reconcile to reported 6M totals.*

**Key read-throughs**
- **Two consecutive mid-teens revenue growth quarters (15.7%, then 16.6%)** — an acceleration versus Apple's recent history. Growth is *not* decelerating into the March quarter, which is normally the seasonally softest.
- **Gross margin is the story**: 46.9% → 48.2% → 49.3% across four quarters. That is roughly **+240bp in two quarters**, an extremely large move for a hardware-anchored model and consistent with Services mix shift, favorable component costs, and pricing.
- **Operating leverage is positive but narrowing**: opex +21.3% vs revenue +16.1% in 1H FY26. The culprit is unambiguously **R&D (+32.6%, $22.31B vs $16.82B)** — a ~$5.5B step-up in six months. SG&A grew only +7.7%, i.e. disciplined. This reads as a deliberate AI/silicon platform investment cycle, not cost drift.
- **Tax is a real headwind**: effective rate **17.5% vs 15.0%** a year ago. Pre-tax income rose +20.8% but net income only +17.3% — 350bp of EPS growth was absorbed by tax. Model ~17–18% ETR going forward, not 15%.
- **EPS (+19.8%) > net income (+17.3%)** by ~2.5pt from buybacks — but see §4: that tailwind was materially reduced in the March quarter.

### 2.2 Half-year scorecard (6M FY26 vs 6M FY25)
| $B | 6M FY26 | 6M FY25 | Δ |
|---|---|---|---|
| Revenue | 254.94 | 219.66 | +16.1% |
| Gross profit / margin | 124.01 / **48.6%** | 103.14 / 47.0% | +20.2% / +167bp |
| Operating income / margin | 86.74 / **34.0%** | 72.42 / 33.0% | +19.8% / +104bp |
| Pre-tax income | 86.84 | 71.89 | +20.8% |
| Net income / margin | 71.68 / 28.1% | 61.11 / 27.8% | +17.3% |
| Diluted EPS | 4.85 | 4.05 | +19.8% |
| SBC expense | 7.12 | 6.51 | +9.4% |
| D&A | 6.65 | 5.74 | +15.9% |

Weighted diluted shares ≈ **14.72–14.82B** (implied from NI/EPS), down ~0.7% sequentially — confirms net share shrink despite buyback deceleration.

---

## 3. Balance Sheet — Fortress, Deleveraged, but a $12.8B Intangible Step-Up Needs Explaining

| $B | 2025-09-27 | 2026-03-28 | Change |
|---|---|---|---|
| Cash & equivalents | 35.93 | **45.57** | +9.64 |
| Marketable securities – current | 18.76 | 22.94 | +4.17 |
| Marketable securities – noncurrent | 77.72 | 78.09 | +0.37 |
| **Total cash & securities** | **132.42** | **146.60** | **+14.18** |
| Accounts receivable | 39.78 | 30.34 | **−23.7%** |
| Non-trade receivables | 33.18 | 23.17 | −30.2% |
| Inventory | 5.72 | 6.75 | **+17.9%** |
| Intangibles (net, ex-goodwill) | 13.30 | **25.80** | **+$12.50B (+94%)** |
| Intangibles (gross) | 24.95 | 37.77 | +12.82 |
| Total assets | 359.24 | 371.08 | +3.3% |
| Accounts payable | 69.86 | 57.35 | **−17.9%** |
| Commercial paper | 7.98 | 2.00 | −5.98 |
| Current portion LT debt | 12.35 | 8.31 | −4.04 |
| Long-term debt (noncurrent) | 78.33 | 74.40 | −3.93 |
| **Total debt (incl. CP)** | **98.66** | **84.71** | **−13.95** |
| Deferred revenue (total / current) | 13.70 / 9.06 | 14.70 / 9.33 | +7.3% |
| Total liabilities | 285.51 | 264.59 | **−7.3%** |
| Stockholders' equity | 73.73 | **106.49** | **+44.5%** |

**Observations**
1. **Net cash ≈ $61.9B** (146.60 − 84.71), up sharply. Debt/equity 0.80x; current ratio 1.07x (144.11 vs 134.64). Apple is deleveraging into a growth phase — a defensive, low-beta posture.
2. **Debt maturities are trivially covered** (10-K: $12.39B due <12M, then 10.08 / 9.30 / 5.24 / 4.97, and $49.30B beyond year five) against $146.6B liquidity.
3. **The intangibles jump (+$12.8B gross, +$12.5B net) is the single most important unexplained item.** It is *not* reflected in the retrieved investing-cash-flow lines (other investing activities were only $1.58B). Paired with noncurrent other assets +$4.8B and noncurrent other liabilities +$14.0B, this pattern is consistent with an acquisition / large licensing or content deal and related deferred tax. **Action for the trading desk: verify M&A in the Q2 FY26 10-Q footnotes before sizing any position — this is likely tied to the buyback cut in §4.**
4. **Working-capital reversal risk:** AP −$12.5B (−17.9%) while inventory +$4.0B points to tightening supplier terms/payables normalization. That is a future cash-flow headwind, and it flatters nothing in the current P&L — but it will be a drag on the *next* two quarters' OCF.
5. **Deferred revenue +$1.0B (+7.3%)** — Services backlog still compounding, consistent with the margin mix story.
6. **Equity +44.5%** is mechanically driven by retained earnings outrunning a slower buyback; AOCI improved to −$5.38B from −$5.57B.

---

## 4. Cash Flow & Capital Allocation — The Most Actionable Finding

### 4.1 Cash generation (6M FY26 vs 6M FY25, $B)
| | 6M FY26 | 6M FY25 | Δ |
|---|---|---|---|
| Operating cash flow | **82.63** | 53.89 | **+53.3%** |
| Capex | 4.34 | 6.01 | −27.7% |
| **Free cash flow** | **78.28** | 47.88 | **+63.5%** |
| Buybacks | **36.99** | 49.50 | **−25.3%** |
| Dividends | 7.74 | 7.61 | +1.7% |
| Debt repayments (LT + CP + ST) | 17.61 | 4.01 | +339% |
| Income taxes paid | 20.40 | 31.68 | −35.6% |

- **Cash conversion 115%** (OCF $82.63B vs net income $71.68B) vs an abnormally poor **88%** last year — earnings quality is high, aided by SBC (+$7.12B) and D&A (+$6.65B) add-backs and working-capital inflows ("other operating assets" swung +$14.33B vs +$4.37B LY).
- **Capex intensity collapsed to 1.7% of revenue** ($4.34B) from 2.7%. FCF margin 30.7%. Apple is monetizing an already-built asset base — supportive of continued heavy R&D without margin damage.
- **Buyback pace was cut hard mid-half**: Q1 FY26 $24.70B (+4.6% YoY) → **Q2 FY26 $12.29B (−52.5% YoY)**. Combined two-quarter payout to shareholders fell to **57% of FCF** (vs ~107% in FY2025, 110% in FY2024). Cash was redirected to debt paydown and the intangible investment in §3. **This removes a meaningful historical EPS-per-share floor; forward EPS growth must increasingly come from operations, not share count.**

### 4.2 Annual capital-allocation history ($B)
| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Operating cash flow | 110.54 | 118.25 | 111.48 |
| Capex | 10.96 | 9.45 | 12.72 |
| Free cash flow | 99.58 | 108.81 | 98.77 |
| Buybacks | 77.55 | 94.95 | 90.71 |
| Dividends | 15.03 | 15.23 | 15.42 |
| **Total return / FCF** | **93%** | **101%** | **107%** |
| LT debt issued / repaid | 5.23 / 11.15 | 0.00 / — | 4.48 / — |

FY2025 was peak-payout (>100% of FCF, partly debt/liquidity-funded). The 1H FY26 shift to 57% payout plus net debt reduction is a **regime change in capital allocation** that matters for both EPS modeling and the equity's income/quality profile.

---

## 5. Insider Transactions

**DATA_UNAVAILABLE.** The data package contains no authorized, point-in-time insider-transaction archive for AAPL as of 2026-07-20. I will not infer or fabricate insider buying/selling. Treat insider sentiment as **unknown** and do not weight it in the thesis; a second agent with a Form-4 feed should fill this gap.

---

## 6. Fundamental Assessment & Actionable Insights

**Thesis (constructive, with two watch items):**
1. **Buy growth quality, not just growth.** Revenue +16.1% with GM +167bp and cash conversion of 115% is a *rare* combination for a company of this size. Operating income grew ~20% on 16% revenue — genuine leverage, even after a 33% R&D ramp.
2. **Margin durability is the swing factor.** 49.3% gross margin is a record-class level off a hardware base. Do **not** extrapolate this as a permanent plateau: mix (Services), commodity costs and tariff/absorbed-cost dynamics can each move this 100bp+. A 100bp GM give-back ≈ $2.2B annualized gross profit.
3. **Reduce the buyback tailwind in your model.** Use **~17.5% ETR** (not 15%) and **~0.5–1.0% annual share shrink** (not the ~2–3% of FY2024–25). That is a 1–2pt haircut to forward EPS growth versus the trailing optics.
4. **Verify the intangible/M&A item before trading size.** A $12.8B gross intangible addition with no visible acquisition line in the retrieved cash flow is the highest-uncertainty datapoint in this report; it plausibly explains the 52% QoQ buyback cut. If it's an accretive platform/asset purchase, it's a positive optionality story; if it's a large capitalized licensing commitment, it's a future amortization drag (net intangibles already amortizing at ~$11.97B accumulated).
5. **Balance-sheet optionality is underappreciated.** $61.9B net cash, $146.6B total liquidity, debt down $13.95B in six months, capex at 1.7% of revenue. AAPL has maximum capacity to absorb a macro shock *and* fund the R&D ramp simultaneously. Low fundamental downside risk to the operating story.

**Catalyst calendar (high urgency):** Q3 FY2026 (June quarter) results are expected in the **last week of July 2026 — i.e., within days of this report date**. Positioning is binary-event risk. The key checkpoints in that print: (a) does gross margin hold ≥48%, (b) does R&D growth remain ~30%+, (c) is the buyback re-accelerated or still throttled, (d) any disclosure of the intangible/M&A item, (e) ETR guidance.

**Bear-case tripwires to monitor:**
- Gross margin <47% in Q3 FY26 (mix reversal or tariff/component absorption).
- Buyback staying suppressed without a disclosed value-accretive use of cash → signals the intangible item is a recurring cash commitment.
- AP decline ($12.5B) plus inventory build (+18%) converting into negative working capital in Q3/Q4 and comping against an unusually strong 1H OCF.
- Effective tax rate drifting above 18%.

**What this report cannot support:** no price, market cap, P/E, EV/EBITDA, or yield can be derived from the available tool set — any valuation conclusion at this stage would be fabricated. Hand off to a pricing/market-data agent for multiple-based conclusions.

---

## 7. Key Points Summary

| Category | Metric | Latest | Comparison | Interpretation / Action |
|---|---|---|---|---|
| Scale | 6M FY26 revenue | $254.94B | +16.1% YoY | Growth re-accelerated; best pace in years |
| Growth | Q1 FY26 / Q2 FY26 revenue | $143.76B / $111.18B | +15.7% / +16.6% YoY | Sequentially *improving*, not decelerating |
| Profitability | Gross margin (Q2 FY26) | 49.3% | +224bp YoY | Record-class; do not extrapolate as permanent |
| Profitability | Operating margin (6M) | 34.0% | +104bp YoY | Leverage despite opex +21.3% |
| Investment | R&D (6M) | $22.31B | +32.6% YoY | AI/platform ramp; ~8.8% of revenue vs 7.7% |
| Expense control | SG&A (6M) | $14.97B | +7.7% YoY | Disciplined |
| Earnings | 6M diluted EPS | $4.85 | +19.8% YoY | Beat net income growth via buybacks |
| Tax | Effective tax rate | 17.5% | vs 15.0% LY | 350bp EPS headwind; model 17–18% forward |
| Cash generation | 6M operating cash flow | $82.63B | +53.3% YoY | 115% of net income — high quality |
| Cash generation | 6M free cash flow | $78.28B (30.7% margin) | +63.5% YoY | Capex only 1.7% of revenue |
| Capital return | Buybacks (Q2 FY26) | $12.29B | **−52.5% YoY** | Material EPS tailwind reduction — revise models |
| Capital return | Total return / FCF (6M) | 57% | vs 107% FY2025 | Regime change in capital allocation |
| Balance sheet | Net cash | ≈$61.9B | debt −$13.95B in 6M | Fortress; low fundamental downside |
| Balance sheet | Equity | $106.49B | +44.5% in 6M | Retained earnings > buybacks |
| Balance sheet | Intangibles (gross) | $37.77B | +$12.82B in 6M | **Unexplained — verify M&A/licensing; likely buyback link** |
| Working capital | Accounts payable | $57.35B | −17.9% in 6M | Future OCF headwind |
| Working capital | Inventory | $6.75B | +17.9% in 6M | Build ahead of launches; watch turns |
| Backlog | Deferred revenue | $14.70B | +7.3% in 6M | Services annuity intact |
| Leverage | Debt/equity | 0.80x | current ratio 1.07x | No solvency concern |
| Debt | LT maturities <12M | $12.39B | vs $146.6B liquidity | Fully covered |
| Insider | Form-4 activity | **DATA UNAVAILABLE** | — | Do not weight; fill gap separately |
| Catalyst | Q3 FY26 earnings | Late July 2026 | ~days away | Binary event; watch GM%, R&D, buyback, M&A disclosure |

**Bottom line on AAPL:** fundamentals are the strongest they have looked in this dataset — mid-teens revenue growth, ~49% gross margin, ~20% operating income growth, 115% cash conversion and a $62B net-cash balance sheet. The **two things a trader must adjust for** are (1) the intentional ~50% cut in buybacks that removes a historical EPS prop and plausibly signals a large investment/acquisition, and (2) a structurally higher 17.5% tax rate. Both argue for valuing AAPL on *operating* EPS growth (~17%) rather than the +19.8% headline, and for treating the imminent late-July print as the decisive near-term risk event — chiefly on gross-margin durability and disclosure of the $12.8B intangible addition.