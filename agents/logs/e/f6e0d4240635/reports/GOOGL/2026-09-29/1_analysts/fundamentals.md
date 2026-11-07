# GOOGL — Alphabet Inc. | Fundamental Deep Dive
**As of 2026-09-29 | Latest filing: Form 10-Q for Q2 2026, filed 2026-07-23 (accn 0001652044-26-000071)**

---

## 1. Executive Summary

Alphabet's Q2 2026 report shows **two very different companies inside one P&L**:

1. **A strongly accelerating core business** — revenue +24.2% YoY in Q2 (+23.1% in H1), operating margin 34.0% (vs. 32.4%), and gross margin up ~220bp. On a *core* basis (excluding securities marks), H1 EPS rose ~22% YoY.
2. **A balance sheet in the middle of an unprecedented AI capital cycle** — H1 capex of **$80.6B** (+103% YoY), plus **$29.1B of capex incurred but unpaid**, negative Q2 free cash flow (**–$5.9B**), buybacks cut to **zero**, and **$105.8B of new capital raised** (debt + common + convertible preferred).

Headline earnings are heavily distorted by a **$135.9B net gain on equity securities** in H1 2026 (vs. $11.4B in H1 2025). Reported diluted EPS of **$14.24** overstates sustainable earning power by roughly 2.7x; **core EPS is ~$5.29**. Traders should anchor on operating income and cash flow, not the reported EPS line.

**Net stance implied by the data:** fundamentally strong demand and operating leverage, but sharply deteriorating free cash flow and earnings quality, rising leverage, and dilution. This is a "show-me" capex cycle where the equity hinges on AI monetization catching up to a ~$190B+ annualized capex run-rate.

---

## 2. Company Profile

**Alphabet Inc. (GOOGL)** is the parent of Google. Consolidated revenue is generated through:
- **Google Services** — Search and other advertising, YouTube ads, Google Network, subscriptions/platforms/devices (Android, Chrome, Play, hardware).
- **Google Cloud** — enterprise infrastructure, data/AI platforms (TPU/Gemini), and Workspace productivity apps.
- **Other Bets** — early-stage businesses (e.g., Waymo, Verily).

Dual-class structure: Class A (GOOGL, one vote), Class C (GOOG, no vote), Class B (super-voting, founder-controlled). This insulates management from short-term shareholder pressure — relevant given the aggressive capex and capital-structure decisions below.

*Note: the data package provides consolidated SEC XBRL facts only; no segment-level revenue/operating income breakdown was available in the extract.*

---

## 3. Income Statement — Quarterly Reconstruction

Revenue is not directly tagged in the returned extract (the tag list truncates alphabetically before `Revenues`). It is derived exactly as:

> **Revenue = OperatingIncomeLoss + CostsAndExpenses**

This reconciles to known H1 2025 figures and is used consistently throughout.

| $ millions | Q2 2025 | Q1 2026 | Q2 2026 | Q2 YoY | H1 2025 | H1 2026 | H1 YoY |
|---|---:|---:|---:|---:|---:|---:|---:|
| Revenue (derived) | 96,428 | 109,896 | 119,796 | **+24.2%** | 186,662 | 229,692 | **+23.1%** |
| Cost of revenue | 39,039 | 41,271 | 45,943 | +17.7% | 75,400 | 87,214 | +15.7% |
| **Gross profit** | 57,389 | 68,625 | 73,853 | +28.7% | 111,262 | 142,478 | +28.1% |
| Gross margin | 59.5% | 62.4% | 61.7% | +2.2pt | 59.6% | 62.0% | +2.4pt |
| Operating expenses | 26,118 | 28,929 | 33,083 | +26.7% | 49,385 | 62,012 | +25.6% |
| **Operating income** | 31,271 | 39,696 | 40,770 | **+30.4%** | 61,877 | 80,466 | **+30.0%** |
| Operating margin | 32.4% | 36.1% | 34.0% | +1.6pt | 33.1% | 35.0% | +1.9pt |
| Non-operating income | 2,662 | 37,716 | 97,983 | n.m. | 13,845 | 135,699 | n.m. |
| Pre-tax income | 33,933 | 77,412 | 138,753 | +309% | 75,722 | 216,165 | +185% |
| Income tax | 5,737 | 14,834 | 26,560 | | 12,986 | 41,394 | |
| Effective tax rate | 16.9% | 19.2% | 19.1% | +220bp | 17.1% | 19.1% | +200bp |
| **Net income** | 28,196 | 62,578 | 112,193 | +298% | 62,736 | 174,771 | +179% |
| Diluted EPS | $2.31 | ~$5.13 | **$9.11** | +294% | $5.12 | **$14.24** | +178% |

### 3.1 Earnings quality — reported vs. core

| $ millions | H1 2025 | H1 2026 | Change |
|---|---:|---:|---:|
| Pre-tax income | 75,722 | 216,165 | +185% |
| Less: gain on debt & equity securities | (11,411) | (135,803) | n.m. |
| **Core pre-tax income** | **64,311** | **80,362** | **+25.0%** |
| Core net income (at effective tax rate) | 53,282 | 64,971 | +21.9% |
| **Core diluted EPS** | **$4.35** | **$5.29** | **+21.7%** |
| Reported diluted EPS | $5.12 | $14.24 | +178% |
| *Reported / core EPS multiple* | *1.18x* | ***2.69x*** | |

- Of H1 2026 pre-tax income, **62.8% ($135.7B) came from non-operating items**, overwhelmingly equity-securities fair-value gains. Only **$0.84B** of the equity gain was realized — the rest is mark-to-market.
- **CFO / net income fell to 0.49x** (from 1.02x in H1 2025) — a classic signature of non-cash earnings.
- Core EPS growth (~+22%) is consistent with revenue growth and margin expansion. **That is the number to model.**

### 3.2 Cost structure signals
- **SBC:** $15.2B in H1 2026 vs. $11.5B (+32%), or **6.6% of revenue** (vs. 6.2%). Q2 alone $8.0B. This is now growing faster than revenue.
- **Depreciation:** $13.6B vs. $9.5B (+43%); D&A including intangibles $14.1B (+45%).
- **Interest expense:** $1.81B vs. $0.30B (**+514%**) as debt doubled; interest income $2.81B (+37%) still exceeds interest expense.
- **G&A:** $10.75B vs. $8.75B (+23%) — in line with revenue.

---

## 4. Balance Sheet — A Structural Transformation

| $ millions | 2025-12-31 | 2026-06-30 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 30,708 | 55,911 | +82.1% |
| Cash + short-term investments | 126,843 | **242,474** | **+91.1%** |
| Accounts receivable, net | 62,886 | 69,175 | +10.0% |
| **Total current assets** | 206,038 | 343,524 | +66.7% |
| **Total assets** | 595,281 | **921,983** | **+54.9%** |
| Accounts payable | 12,200 | 20,258 | +66.0% |
| Accrued liabilities | 55,557 | 73,014 | +31.4% |
| Accrued income taxes, current | 523 | 5,233 | +900% |
| Contract liabilities (deferred revenue) | 8,600 | 10,100 | +17.4% |
| Operating lease liability | 15,954 | 18,037 | +13.1% |
| Finance lease liability | 2,500 | 2,590 | +3.6% |
| **Debt (carrying amount)** | 49,085 | **101,085** | **+106.0%** |
| Convertible preferred stock | 0 | **18,023** | new |
| Common stock + APIC | 93,126 | 131,371 | +41.1% |
| AOCI | (1,916) | (2,285) | wider loss |
| Non-marketable equity securities | 64,094 | **124,259** | **+93.9%** |
| Deferred tax assets, net | 9,113 | 1,448 | –84.1% |
| **Deferred tax liabilities, net** | 919 | **22,819** | +2,383% |
| Finite-lived intangibles, gross | 2,467 | 10,585 | +329% |
| Shares outstanding (millions) | 12,088 | 12,230 | +1.2% |

**Key observations**

- **Total assets rose $326.7B in six months.** The largest identifiable drivers: +$115.6B cash/investments, +$60.2B non-marketable equity securities, +$52.0B debt-funded liquidity, and ~$9.5B of acquired intangibles (M&A).
- **Non-marketable equity securities are now 13.5% of total assets.** Cumulative upward fair-value adjustments rose from $44.5B to **$85.7B** in six months. This is the single largest source of book-value and earnings volatility.
- **A $22.8B deferred tax liability** was created, consistent with the unrealized marks — a future cash tax claim if gains are realized.
- **Liquidity remains exceptional:** $242.5B cash + short-term investments against $101.1B debt = **~$141.4B net cash** (~$123.4B after the $18.0B preferred). Estimated current ratio ~2.8–3.1x (current liabilities ~$110–125B based on visible components). **No credit stress**, despite the leverage step-up.
- **Working capital flattered cash flow:** AP +66% and accrued liabilities +31% provided a cash tailwind. AR grew only 10% against 23% revenue growth — receivables quality is good, collection is tight.
- **Dilution:** +142M shares (+1.2%) in six months, plus a new $19B convertible preferred instrument. Common issuance generated **$30.5B** of proceeds — implying an average issuance price around **$215/share** (inference, not disclosed).

---

## 5. Cash Flow — The Critical Fault Line

| $ millions | Q1 2025 | Q2 2025 | H1 2025 | Q1 2026 | Q2 2026 | H1 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash flow | 36,150 | 27,747 | 63,897 | 45,790 | 39,069 | **84,859** |
| Capital expenditures | 17,197 | 22,446 | 39,643 | 35,674 | 44,924 | **80,598** |
| **Free cash flow** | **18,953** | **5,301** | **24,254** | **10,116** | **(5,855)** | **4,261** |
| FCF margin | 21.0% | 5.5% | 13.0% | 9.2% | **–4.9%** | **1.9%** |
| SBC (non-cash) | — | 6,000 | 11,500 | — | 8,000 | 15,200 |
| Dividends paid | 2,434 | 2,543 | 4,977 | 2,542 | 2,689 | 5,231 |

- **H1 FCF collapsed 82% YoY to $4.3B**; Q2 was **negative $5.9B** — the first negative FCF quarter in the visible data.
- **Capex/revenue reached 35.1%** in H1 2026 (21.2% in H1 2025).
- **Capex incurred but not yet paid** jumped from $15.1B at 12/31/25 to **$29.1B at 6/30/26**. Adjusting for the $14.0B accrual build, **capex actually incurred in H1 2026 was ~$94.6B vs. ~$40.0B in H1 2025 (+137%)**. This is the true run-rate to model (~$190B annualized).
- **Dividends ($5.23B) now exceed free cash flow ($4.26B)**. FCF less SBC is **–$10.9B**.
- FY2023–FY2025 financing cash flow was **–$72.1B, –$79.7B, –$37.4B** — a consistent repurchaser. In H1 2026 financing swung to **+$86.3B**. The company has flipped from returning capital to raising it.

### Financing raised in H1 2026
| Item | $ millions |
|---|---:|
| Debt proceeds, net of issuance costs | 56,226 |
| Repayments of debt/lease obligations | (5,253) |
| Common stock issuance | 30,499 |
| Convertible preferred issuance (2026-06-05) | 19,063 |
| Minority interests (project/JV capital) | 3,758 |
| Dividends | (5,231) |
| Share repurchases | **0** |
| **Net financing cash flow** | **+86,320** |

The **$28.3B buyback in H1 2025 going to zero**, combined with a first-time $19B convertible preferred and $30B of common stock, is the clearest signal in the dataset: management is prioritizing AI infrastructure and strategic investments over per-share returns.

---

## 6. Investment Portfolio and Mark-to-Market Risk

- Non-marketable equity securities: **$124.3B** (from $64.1B).
- Cumulative upward adjustments: **$85.7B** (from $44.5B); cumulative downward adjustments: $9.1B.
- Only **$0.84B** of the $135.9B H1 equity gain was realized.
- **Sensitivity:** a 10% markdown of the $124.3B portfolio = **–$12.4B pre-tax ≈ –$1.01 EPS**; a 20% markdown ≈ **–$2.02 EPS**. A broad markdown could swing reported EPS negative in a single quarter even with a healthy core business.
- The **$22.8B deferred tax liability** represents a future cash claim if and when gains are monetized.

**Actionable read:** Reported EPS and book value now carry meaningful "private-AI-valuation beta." Screen any valuation multiple against core EPS, and treat reported book value as a marked-to-model figure.

---

## 7. Multi-Year Context (10-K data points)

| Metric | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Financing cash flow | –$72.1B | –$79.7B | –$37.4B |
| Capex incurred but not yet paid (year-end) | $7.4B | $10.3B | $15.1B |
| Finance lease principal payments | $0.71B | $0.41B | $1.99B |

Even before 2026, the capex pipeline was building (accrued capex +46% in 2025) and capital returns were already slowing (financing outflow halved in 2025). **2026 is an acceleration of an existing trend, not a one-quarter anomaly.**

Long-term debt maturities as of 12/31/25 were laddered: $2.0B (2026), $1.0B (2027), $2.7B (2028), $1.8B (2029), $5.5B (2030), $36.1B thereafter — no near-term refinancing wall.

---

## 8. Insider Transactions

**DATA_UNAVAILABLE.** The data vendor has no authorized, point-in-time insider-transactions archive for GOOGL as of 2026-09-29. No insider buying/selling should be inferred or assumed. Monitor Form 4 filings directly; the founder Class B bloc remains the dominant governance factor.

---

## 9. Risks

| Risk | Evidence | Potential impact |
|---|---|---|
| **Earnings-quality reversal** | 62.8% of H1 pre-tax income from non-operating marks; only $0.84B realized | 10–20% portfolio markdown = $1.0–2.0 EPS hit; headline EPS could turn negative |
| **FCF compression / capex super-cycle** | H1 capex $80.6B cash, $94.6B incurred; Q2 FCF –$5.9B | Sustained negative FCF removes buyback support and may force more capital raises |
| **D&A cliff** | Depreciation $13.6B vs. $94.6B incurred capex (≈7x) | D&A could triple over 2–3 years; each +$10B D&A ≈ –$0.66 EPS |
| **Rising leverage / interest cost** | Debt $101.1B (+106%); interest expense +514% | Further issuance likely; credit metrics normalize from "fortress" |
| **Dilution** | Shares +1.2% in 6 months; $30.5B common + $19.1B preferred; buybacks zero | Per-share growth lags net-income growth |
| **Legal/regulatory accruals** | Current loss-contingency accrual $17.4B (from $15.6B) | Potential cash settlements; ongoing antitrust/ad-tech exposure |
| **AI capex ROI skepticism** | Capex 35% of revenue and rising | Multiple compression if revenue acceleration stalls below ~20% |
| **Concentration in marked private assets** | $124.3B non-marketable = 13.5% of assets | Valuation resets are lumpy and opaque |

**Mitigants:** $242.5B liquidity, ~$141B net cash, 35% operating margins, revenue accelerating, deferred revenue +17%, and a tax rate that remains moderate at 19.1%.

---

## 10. Actionable Trading Insights

1. **Trade core EPS, not headline EPS.** Model H1 core EPS of **$5.29** (annualized ~**$10.60**; Q2 annualized ~$10.44). Reported $14.24 annualizes to $28.48 and is not a sustainable earnings base. If consensus or screens use GAAP EPS, GOOGL looks far cheaper than it is.
2. **Valuation framing:** each 5 turns of P/E applied to ~$10.60 of annualized core EPS equals roughly **$53/share**. Use this to calibrate where the market is pricing the core franchise versus the marked investment portfolio.
3. **Watch Q3 (late Oct 2026) for four numbers:** (a) revenue growth ≥20%; (b) operating margin ≥33%; (c) capex guide — any figure at or below the H1 run-rate is a positive surprise; (d) Q3 FCF — should be positive on seasonal CFO strength; a second negative quarter would be a material negative catalyst.
4. **Negative FCF is the bear thesis' cleanest evidence.** H1 FCF $4.3B vs. $24.3B, dividends > FCF, buybacks at zero. If capex guidance rises again without a matching acceleration in Cloud/AI revenue, expect multiple compression.
5. **The $124B private portfolio is an unhedged earnings option.** Expect large swings in the non-operating line each quarter. If implied volatility around earnings does not reflect this, long-straddle structures are structurally attractive; conversely, avoid directional bets anchored on GAAP EPS.
6. **Buyback resumption would be a strong positive signal** — it would imply management sees FCF inflection and believes the shares are undervalued. None is currently signaled.
7. **D&A is the 2027 margin story.** Depreciation growth (+43%) is already outpacing revenue; the gap to capex implies years of elevated D&A. Fade any thesis that assumes operating margins expand linearly from 35%.
8. **Balance-sheet risk is low, but governance signal is negative.** Net cash of ~$141B means no solvency concern, but the pivot to $56B of debt, $30B of stock, and $19B of preferred in six months — while halting buybacks — is a meaningful change in capital-allocation discipline.
9. **Key data gap to fill:** segment-level revenue and Cloud backlog/margin (not in this extract). Cloud growth and AI monetization are the swing factors for whether this capex cycle earns its cost of capital.

---

## 11. Data Notes & Limitations

- **Revenue is derived**, not directly reported in the returned extract: Revenue = Operating income + Total costs and expenses. This method reconciles exactly to H1 2025 figures.
- The vendor's fact set **truncates alphabetically**; tags after ~`FiniteLivedIntangibleAssetsGross` (including `Revenues`, `ResearchAndDevelopmentExpense`, goodwill, retained earnings, total liabilities/equity) were unavailable. Segment data, geographic mix, and Cloud backlog are therefore not covered.
- "Annual" and "quarterly" requests returned the same point-in-time fact set; multi-year comparison is limited to the FY2023–FY2025 10-K tags shown.
- Core EPS uses the reported effective tax rate applied to pre-tax income excluding securities gains; it is an approximation, not a company-defined non-GAAP measure.
- Common-share issuance price (~$215) is inferred from proceeds divided by share count change and should not be treated as a market quote.

---

## 12. Key Points Summary Table

| Category | Key Data (H1 2026 vs. H1 2025) | Interpretation | Trading Implication |
|---|---|---|---|
| **Revenue** | $229.7B vs. $186.7B, **+23.1%** (Q2 +24.2%) | Demand accelerating, not decelerating | Supports core multiple; watch for ≥20% in Q3 |
| **Operating income** | $80.5B vs. $61.9B, **+30.0%**; margin 35.0% vs. 33.1% | Genuine operating leverage | Core earnings power intact; margin floor ~33% |
| **Reported EPS** | **$14.24** vs. $5.12 (+178%) | Distorted by $135.9B equity marks | Do **not** use for valuation |
| **Core EPS** | **~$5.29** vs. ~$4.35 (+22%) | Clean growth in line with revenue | Annualized ~$10.60; anchor multiples here |
| **Earnings quality** | CFO/NI 0.49x (vs. 1.02x); only $0.84B of gains realized | Low-quality headline earnings | Expect EPS volatility; avoid GAAP-anchored models |
| **Free cash flow** | **$4.3B vs. $24.3B (–82%)**; Q2 **–$5.9B** | Capex super-cycle consuming cash | Cleanest bear evidence; watch Q3 FCF |
| **Capex** | $80.6B cash / **$94.6B incurred**, 35% of revenue | Unprecedented AI build | Any capex guide cut/plateau = bullish |
| **Capital raised** | Debt $56.2B, common $30.5B, preferred $19.1B | Pivot from returning to raising capital | Dilution/leverage overhang |
| **Buybacks** | **$0 vs. $28.3B** | Support removed | Resumption would be a strong buy signal |
| **Dividend** | $0.22/qtr (+4.8%); H1 $5.23B > FCF | Return now debt/cash-funded | Low yield, low risk of cut, but no cushion |
| **Balance sheet** | Cash+ST inv **$242.5B**; debt **$101.1B**; net cash ~$141B | Still fortress-like | Credit risk low; leverage trend negative |
| **Private assets** | Non-marketable equity **$124.3B** (+94%); up-marks $85.7B | Hidden earnings/book volatility | 10% markdown ≈ –$1.01 EPS |
| **Deferred taxes** | DTL **$22.8B** (from $0.9B) | Future cash tax claim on marks | Monitor if gains are monetized |
| **SBC** | $15.2B (+32%), 6.6% of revenue | Rising dilution cost | FCF less SBC is negative (–$10.9B) |
| **D&A** | $14.1B (+45%) vs. $94.6B capex incurred | Multi-year D&A cliff | Margin headwind into 2027 |
| **Interest** | Expense $1.81B (+514%); income $2.81B | Net interest still positive | Watch as debt grows |
| **Tax rate** | 19.1% vs. 17.1% | +200bp headwind | ~2pt EPS drag |
| **Insider activity** | **Data unavailable** | No authorized archive | Do not infer; monitor Form 4s |
| **Overall** | Core accelerating, FCF collapsing, balance sheet releveraging | High-quality franchise in a low-FCF investment phase | Own the core, hedge the GAAP-EPS noise; Q3 capex/FCF is the binary catalyst |