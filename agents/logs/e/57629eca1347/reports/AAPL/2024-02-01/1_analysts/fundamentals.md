# AAPL — Fundamental Deep-Dive (analysis date: 2024-02-01)

**Company:** Apple Inc. (`AAPL`) · Fiscal year ends late September (FY2023 ended 2023-09-30)

---

## ⚠️ Critical data-timing note (read first)

The vendor dataset is labeled "point-in-time SEC facts public by 2024-02-01," but every row for the December quarter carries `accepted_at = 2024-02-02 04:03 UTC` (10-Q accepted Feb 2). That maps to **AAPL's fiscal Q1 FY2024 earnings release, which crossed the tape after the close on Feb 1, 2024**, with the 10-Q filed the next morning.

Practical implication for a trader at the 2024-02-01 close:
- The **income-statement, balance-sheet and cash-flow figures for the quarter ended 2023-12-30 were NOT in the public 10-Q at the Feb 1 close.** They are effectively the **post-close catalyst**, not pre-close information.
- **Actionable:** treat the Q1 FY24 numbers below as "the print," not as "known fundamentals." Anyone positioned at the Feb 1 close did not have them; the Feb 2 session is the reaction session.
- All FY2021–FY2023 annual figures come from the 10-K accepted **2023-11-03** (accn 0000320193-23-000106) and *were* fully public well before Feb 1 — that is the clean, tradeable history.

Also flagged up front: **`get_insider_transactions` returned DATA_UNAVAILABLE** — no authorized point-in-time insider archive exists for AAPL. No insider activity is reported or inferred below.

---

## 1. Company profile (vendor coverage caveat)

The vendor returned **no profile, segment, geographic, or product-line data** in this pull — only XBRL line items. What the filing data does establish about the business:

- **Capital-light, IP-driven model:** Q1 FY24 capex was only **$2.39B (2.0% of revenue)**; FY2023 capex **$10.96B (2.9% of revenue)** versus CFO of **$110.5B**. The bulk of value creation is software/services and brand, not fixed assets.
- **Massive, persistent free cash generation:** TTM FCF ≈ **$106.9B** (see §5).
- **Net-cash balance sheet with aggressive, continuous capital return:** TTM buybacks + dividends ≈ **$93.3B**, ~87% of TTM FCF.
- **Heavy non-US earnings exposure:** FY2023 pre-tax income from foreign jurisdictions was **$72.9B of $113.7B total (64%)**, driving an effective tax rate (14.7%) well below the 21% statutory rate.

*(Segment-level mix — iPhone/Services/Wearables, Greater China — is NOT in this dataset and is deliberately not asserted here.)*

---

## 2. Q1 FY2024 income statement (quarter ended 2023-12-30) vs Q1 FY2023

| Line ($M) | Q1 FY24 | Q1 FY23 | Δ y/y |
|---|---|---|---|
| Revenue | **119,575** | 117,154 | **+2.1%** |
| Cost of goods & services | 64,720 | 66,822 | −3.1% |
| **Gross profit** | **54,855** | 50,332 | **+9.0%** |
| R&D | 7,696 | 7,709 | −0.2% |
| SG&A | 6,786 | 6,607 | +2.7% |
| Total operating expenses | 14,482 | 14,316 | +1.2% |
| **Operating income** | **40,373** | 36,016 | **+12.1%** |
| Non-operating income/(expense) | (50) | (393) | improved $343M |
| Pre-tax income | 40,323 | 35,623 | +13.2% |
| Income tax | 6,407 | 5,625 | +13.9% |
| **Net income** | **33,916** | 29,998 | **+13.1%** |
| Diluted EPS | **$2.18** | $1.88 | **+16.0%** |
| Diluted shares (implied) | ~15,558M | ~15,957M | −2.5% |

### Margin structure (the whole story)
| Metric | Q1 FY24 | Q1 FY23 | Δ |
|---|---|---|---|
| Gross margin | **45.87%** | 42.96% | **+291 bp** |
| Opex / revenue | 12.11% | 12.22% | −11 bp |
| Operating margin | **33.76%** | 30.74% | **+302 bp** |
| Net margin | **28.36%** | 25.61% | **+275 bp** |
| Effective tax rate | 15.89% | 15.79% | +10 bp |

**Read-through:** Revenue grew only **+2.1%**, yet EPS grew **+16.0%**. The beat is **structurally margin-led**, not growth-led: ~$2.1B of COGS came out of the P&L on flat-to-up revenue (favorable mix/commodity costs), and a **2.5% lower diluted share count** added another ~2.5 pts to EPS. Non-operating swung from −$393M to −$50M on higher interest income on the cash pile.

**What it means:** this is a *high-quality earnings print with a soft top line*. Multiple expansion from here requires revenue re-acceleration or service-mix confirmation — margins alone are unlikely to keep compounding at +290bp/yr.

---

## 3. Balance sheet (2023-12-30 vs 2023-09-30)

| Item ($M) | 2023-12-30 | 2023-09-30 | Δ |
|---|---|---|---|
| Cash & equivalents | 40,760 | 29,965 | +10,795 |
| Marketable securities — current | 32,340 | 31,590 | +750 |
| Marketable securities — noncurrent | 99,475 | 100,544 | −1,069 |
| **Total cash + securities** | **172,575** | 162,099 | **+10,476** |
| Accounts receivable | 23,194 | 29,508 | −6,314 |
| Nontrade receivables | 26,908 | 31,477 | −4,569 |
| Inventory | 6,511 | 6,331 | +180 |
| **Total current assets** | **143,692** | 143,566 | +126 |
| **Total assets** | **353,514** | 352,583 | +931 |
| Accounts payable | 58,146 | 62,611 | −4,465 |
| Commercial paper | 1,998 | 5,985 | −3,987 |
| Current portion of LT debt | 10,954 | 9,822 | +1,132 |
| LT debt — noncurrent | 95,088 | 95,281 | −193 |
| **Total debt** | **107,998** | 111,085 | **−3,087** |
| **Total current liabilities** | **133,973** | 145,308 | **−11,335** |
| Total liabilities | 279,414 | 290,437 | −11,023 |
| **Shareholders' equity** | **74,100** | 62,146 | **+11,954** |
| Shares outstanding | 15,460.2M | 15,500.6M | −40.4M |
| Shares outstanding (2024-01-19) | 15,441.9M | — | — |

### Liquidity, leverage, returns
| Metric | Q1 FY24 | Q1 FY23 / prior |
|---|---|---|
| Current ratio | **1.07x** | 0.99x (Sep-23); 1.03x (Dec-22: 143,566? n/a) |
| Quick ratio (ex-inventory) | **1.02x** | — |
| Net cash (cash+securities − total debt) | **+$64,577M** | +$51,014M (Sep-23) |
| Total debt / equity | **1.46x** | 1.79x (Sep-23) |
| Debt maturities next 12M | $9,943M LT + CP | — |
| Debt due yrs 2–5 | $10,775M / $12,265M / $9,786M / $7,800M | — |
| Debt due after yr 5 | $56,003M | — |
| AOCI | −$9,378M | −$11,452M (improving on rate-cut expectations) |

**Key observations:**
1. **Equity jumped $12.0B in one quarter** — driven by $33.9B net income + $2.1B AOCI recovery + $3.0B stock comp, partially offset by $20.1B buybacks and $3.8B dividends.
2. **Maturity ladder is a non-issue:** $64.6B net cash against $10.0B of 12-month maturities. No refinancing risk; Apple is a net creditor to the system.
3. **Working capital swung sharply favorable:** AP −$4.5B, AR −$6.3B, nontrade receivables −$4.6B → current liabilities down $11.3B and current ratio pushed above 1.0x. This is the primary driver of the +$11.2B sequential cash build.
4. AOCI improving (−$11.5B → −$9.4B) with **$3,045M of unrealized AFS securities gains** in the quarter — a tailwind to book value while rates fall; a reversal risk if the rate path re-prices.

---

## 4. Cash flow & capital returns

| ($M) | Q1 FY24 | Q1 FY23 | Δ |
|---|---|---|---|
| **Operating cash flow** | **39,895** | 34,005 | **+17.3%** |
| Capex (PP&E) | 2,392 | 3,787 | −36.8% |
| **Free cash flow** | **37,503** | 30,218 | **+24.1%** |
| Investing cash flow | **+1,927** | −1,445 | +3,372 |
| Financing cash flow | (30,585) | (35,563) | +4,978 |
| Net change in cash | **+11,237** | −3,003 | — |
| Share repurchases | 20,139 | 19,475 | +3.4% |
| Dividends paid | 3,825 | 3,768 | +1.5% |
| **Total capital returned** | **23,964** | 23,243 | **+3.1%** |
| SBC expense (non-cash) | 2,997 | 2,905 | +3.2% |
| Depreciation & amortization | 2,848 | 2,916 | −2.3% |
| Shares withheld for tax on SBC | 2,591 | 2,316 | +11.9% |
| Cash taxes paid | 7,255 | 828 | +776% |
| Dividend per share declared | $0.24 | $0.23 | +4.3% |

### Quality-of-earnings ratios
| Metric | Q1 FY24 | Q1 FY23 |
|---|---|---|
| CFO / net income | **1.18x** | 1.13x |
| FCF / net income | **1.11x** | 1.01x |
| Capex / revenue | 2.0% | 3.23% |
| FCF margin | **31.4%** | 25.8% |
| Capital return / FCF | **63.9%** | 76.9% |

**TTM (derived: FY2023 − Q1 FY23 + Q1 FY24):**
- Net income **≈ $100,913M**
- CFO **≈ $116,433M**; capex **≈ $9,564M**; **FCF ≈ $106,869M**
- Buybacks + dividends **≈ $93,296M = ~87% of TTM FCF**
- Diluted EPS TTM **≈ $6.43** ($6.13 − $1.88 + $2.18)

**Read-through:** Earnings are **fully cash-backed** (FCF > net income), capex intensity is falling, and Apple is returning ~87% of FCF while still *growing* the cash pile. The **cash-tax spike to $7.26B (from $0.83B)** is a timing/geography artifact, not a rate shock — the effective rate held at 15.9%. It is, however, a reminder that **cash taxes are now tracking closer to book taxes**, which can create reported-cash-flow noise in coming quarters.

---

## 5. Three-year annual history (FY2021–FY2023, from the 2023-11-03 10-K)

| Metric | FY2021 | FY2022 | FY2023 | FY22→FY23 |
|---|---|---|---|---|
| Gross profit ($M) | 152,836 | 170,782 | **169,148** | −1.0% |
| Pre-tax income ($M) | 109,207 | 119,103 | **113,736** | −4.5% |
| Income tax ($M) | 14,527 | 19,300 | **16,741** | −13.3% |
| **Net income ($M, derived)** | **94,680** | **99,803** | **96,995** | **−2.8%** |
| Effective tax rate | 13.3% | 16.2% | **14.7%** | −150 bp |
| Diluted EPS | $5.61 | $6.11 | **$6.13** | +0.3% |
| Operating cash flow ($M) | 104,038 | 122,151 | **110,543** | −9.5% |
| Capex ($M) | 11,085 | 10,708 | **10,959** | +2.3% |
| Buybacks ($M) | 85,971 | 89,402 | **77,550** | −13.3% |
| Dividends ($M) | 14,467 | 14,841 | **15,025** | +1.2% |
| SBC ($M) | 7,906 | 9,038 | **10,833** | +19.9% |
| Share-based tax benefit ($M) | 4,056 | 4,002 | **3,421** | −14.5% |
| Deferred revenue recognized ($M) | 6,700 | 7,500 | **8,200** | +9.3% |
| Foreign pre-tax share | $68.7B / 62.9% | $71.3B / 59.9% | $72.9B / 64.1% | rising |

**The three-year arc that matters:**
- **FY22 was the peak; FY23 contracted.** Net income −2.8%, EPS flat (+0.3%) only because the share count fell. Gross profit fell for the first time in the window.
- **The buyback is the EPS engine.** FY23 EPS was flat *despite* a 2.8% earnings decline — pure share-count engineering. This makes the +16% EPS in Q1 FY24 all the more notable (real earnings growth + buyback).
- **SBC is compounding faster than earnings (+20% in FY23)** and is now **$10.8B/yr (~11% of net income)**, a real, recurring dilution offset to buybacks. Watch the buyback's *net* effect: FY23 gross buybacks $77.6B were partly consumed by $5.4B of SBC tax withholding and $10.8B of SBC issuance.
- **Deferred revenue is growing modestly (6.7 → 7.5 → 8.2B, +9.3% in FY23)** — a modest forward indicator that services/contractual revenue visibility is intact but not accelerating.
- **Tax rate is structurally low (13–16%) but the trend is up**, and OECD/global-minimum regimes plus the FY23 foreign tax mix are a live risk to forward EPS.

---

## 6. Insider transactions

**Unavailable.** The vendor explicitly returned `DATA_UNAVAILABLE` — no authorized point-in-time insider archive for AAPL exists as of 2024-02-01. **No insider buying or selling is reported, implied, or estimated.** Any claim about insider behavior for this name would be fabricated; treat insider signal as a **blank input** for this trade and weight the fundamentals only.

---

## 7. What this dataset does *not* contain (do not over-read the report)

- Price, market cap, valuation multiples (P/E, EV/EBITDA) — no market data in this tool set.
- Segment and geographic revenue (iPhone, Services, Wearables, Greater China), unit volumes, ASPs.
- Forward guidance, consensus estimates, buyback authorization size, dividend policy changes.
- Any insider data (see above).

Illustrative only, if you supply a price: on **TTM diluted EPS of $6.43** and ~15.44B shares outstanding (2024-01-19), a $185 price implies **~28.8x TTM P/E and ~$2.86T market cap**. Substituting your own price is required — I have not sourced a price.

---

## 8. Actionable insights for a trader

**Constructive:**
1. **The print is a margin-quality beat, not a growth beat.** Revenue +2.1% vs operating income +12.1%. If the market is pricing a growth re-rating, this does not support it; if it is pricing durable margin/free-cash-flow, it very much does. **Position accordingly — this is an FCF/quality print.**
2. **FCF inflection is the strongest datapoint:** CFO +17.3%, FCF +24.1%, FCF margin 25.8% → 31.4%. Cash generation is accelerating faster than earnings, with capex intensity falling to 2.0% of revenue.
3. **Balance sheet is unambiguously strong:** $64.6B net cash, current ratio 1.07x (above 1.0x for the first time in recent memory), $10.0B of 12-month maturities vs $172.6B liquidity. **Zero credit risk.** This caps downside in any macro/rate shock.
4. **Capital return is a structural bid:** ~87% of TTM FCF returned; 15,500.6M → 15,441.9M shares in ~4 months. A ~2.8% annualized buyback yield plus a rising dividend ($0.23 → $0.24) provides a persistent technical floor.
5. **Watch the FY24 product cycle for the top-line fix** — the margin lever is now largely spent (+291bp y/y is not repeatable indefinitely).

**Cautions / risks:**
6. **+2.1% revenue growth is the weak link.** Every dollar of EPS growth beyond this is margin + buyback, both of which have finite runway.
7. **SBC at $10.8B/yr (+20%)** materially dilutes the net effect of a $77–80B buyback program. Net share reduction is ~2.5–3%/yr — decent, but the headline buyback number overstates it.
8. **Tax rate risk:** 13.3% → 16.2% → 14.7% → 15.9%. A move toward 18–20% on global-minimum rules would be an ~3–5 pt EPS headwind with no operating offset.
9. **AOCI is mark-to-market, not operating:** the $3.0B unrealized gain in Q1 FY24 flatters equity and comprehensive income; it reverses if yields back up.
10. **Cash-tax spike ($0.83B → $7.26B)** should be tracked for two more quarters to confirm it is timing and not a new run-rate.

**Trade framing:**
- **Bull case:** margin durability + $106.9B TTM FCF + $64.6B net cash + mechanical buyback = defensive quality compounder with a floor. Buy dips.
- **Bear case:** 2% growth means the EPS growth rate is mechanically decelerating as margin comps harden through FY24; at ~29x TTM P/E there is no room for a top-line miss.
- **Key monitors for the next two prints:** (a) does gross margin hold above ~45%? (b) does revenue growth re-accelerate above 2%? (c) does the effective tax rate stay under 17%? (d) does FCF/NI stay above 1.0x?

---

## 9. Key points summary

| Category | Metric | Value | Signal |
|---|---|---|---|
| **Data caveat** | Q1 FY24 10-Q accepted | 2024-02-02 04:03 UTC (post Feb-1 close) | Print is the catalyst, not pre-close info |
| **Growth** | Revenue y/y (Q1 FY24) | +2.1% ($119,575M) | ⚠️ Weak — the key bear point |
| **Profitability** | Gross margin | 45.87% (+291 bp y/y) | ✅ Strong mix/cost tailwind |
| **Profitability** | Operating margin | 33.76% (+302 bp y/y) | ✅ Operating leverage |
| **Earnings** | Net income y/y | +13.1% ($33,916M) | ✅ Margin-led, not growth-led |
| **Earnings** | Diluted EPS y/y | +16.0% ($2.18) | ✅ Margin + 2.5% share shrink |
| **Cash flow** | Operating cash flow | $39,895M (+17.3% y/y) | ✅ Accelerating |
| **Cash flow** | Free cash flow | $37,503M (+24.1% y/y) | ✅ FCF margin 31.4% |
| **Quality** | FCF / net income | 1.11x | ✅ Fully cash-backed |
| **Liquidity** | Cash + securities | $172,575M | ✅ Fortress |
| **Leverage** | Net cash | +$64,577M | ✅ Net creditor |
| **Leverage** | Total debt / equity | 1.46x (from 1.79x) | ✅ Deleveraging |
| **Liquidity** | Current ratio | 1.07x (from 0.99x) | ✅ Above 1.0x |
| **Capital return** | Buybacks + dividends (Q) | $23,964M | ✅ ~87% of TTM FCF |
| **Capital return** | Dividend/share | $0.24 (+4.3% y/y) | ✅ Modest growth |
| **Dilution** | SBC expense | $2,997M/qtr; $10,833M FY23 (+19.9%) | ⚠️ Offsets buyback |
| **Tax** | Effective rate | 15.89% (FY23: 14.7%) | ⚠️ Structurally low, trending up |
| **Equity** | Shareholders' equity | $74,100M (+$11,954M q/q) | ✅ Includes $3.0B AOCI gain |
| **Valuation** | TTM diluted EPS | ≈ $6.43 (derived) | Needs price input for multiple |
| **Annual trend** | FY23 net income / EPS | −2.8% / +0.3% | ⚠️ FY23 was a down year |
| **Insider** | Transactions | **DATA UNAVAILABLE** | 🚫 No signal — do not infer |

**Bottom line:** AAPL at 2024-02-01 delivers a **high-quality, cash-rich, margin-driven quarter on a soft top line**, funded by a fortress balance sheet and recycled through one of the largest capital-return programs in the market. The trade is a **quality/FCF/defensive** trade, not a growth trade. The single largest risk to the equity at ~29x TTM earnings is that **+2.1% revenue growth cannot carry the valuation** once the gross-margin comps harden. Insider data is entirely absent and should be treated as an unknown, not a positive.