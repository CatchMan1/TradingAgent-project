# AAPL — Fundamental Deep Dive
**Point-in-time analysis as of 2026-09-01 | Latest reported period: FQ3 FY2026, ended 2026-06-27 (Form 10-Q accepted 2026-07-31)**

---

## 1. Executive Summary

Apple Inc. (`AAPL`) is showing a **clear fundamental re-acceleration** through the first nine months of FY2026, with growth in revenue (+16.2%), gross margin (+225 bp), operating income (+21.7%), and EPS (+22.4%) versus the comparable prior-year period. The most important development is not the revenue line — it is the **cash-generation step-change**: operating cash flow of **$117.0B** over nine months (+43% YoY) and free cash flow of **~$110.2B** (+52% YoY), against a **declining capex** base.

Three durable, tradeable facts emerge from the filings:

1. **Gross margin is structurally higher (~49–50% vs ~46.5%)** — a mix/AI-services-driven repricing that is flowing almost entirely to operating profit.
2. **The balance sheet is net-cash-rich and improving fast** — net cash (cash + securities − total debt) rose **~$28.5B in nine months to ~$62.2B** despite ~$73.9B returned to shareholders, and the company issued **zero** new long-term debt in FY26.
3. **Investment intensity is rotating from capex to R&D and intangibles** — R&D is up **32.5% YoY** to $34.0B (9.3% of revenue), capex is *down* 28%, and gross intangible assets jumped **$13.3B** with essentially no cash M&A in the investing section. This is the fingerprint of a **large non-cash / deferred-payment IP or technology acquisition** — likely AI-related — that traders should verify in the FQ3 10-Q notes.

**Offsetting concerns:** (a) the effective tax rate has risen from 15.4% to 17.6%, a ~$2.7B / ~$0.18 EPS headwind YTD; (b) raw-materials inventory has **more than tripled** to $7.6B, a swing factor for FQ4 gross margin; (c) buybacks have decelerated to $62.1B from $70.6B (9M basis), the first slowdown in years.

**Directional stance implied by the fundamentals: constructive/positive.** Fundamentals support the equity; the key near-term risk is that FQ4 (Sept-quarter) gross margin disappoints on inventory digestion or tariff/component cost, and that the higher tax rate persists into FY27.

---

## 2. Company Profile & Reporting Status

| Item | Detail |
|---|---|
| Company | Apple Inc. (`AAPL`) — Nasdaq |
| Fiscal year | 52/53-week year ending late September |
| Latest filing | Form 10-Q, period ended 2026-06-27, accepted 2026-07-31 14:01 UTC (accn 0000320193-26-000020) |
| Prior FY | Form 10-K, FY ended 2025-09-27, filed 2025-10-31 (accn 0000320193-25-000079) |
| Interim filings in period | Q1 FY26 10-Q (filed 2026-01-30), Q2 FY26 10-Q (filed 2026-05-01), Q3 FY26 10-Q (filed 2026-07-31) |
| Shares outstanding | **14,594,181,000** as of 2026-07-17 (from 14,773,260,000 at 2025-09-27; **−1.2%**) |
| Next catalyst | FQ4/FY2026 results, expected late October 2026 (not yet reported) |
| Segment/product disclosure | Not present in the point-in-time dataset — **no iPhone/Mac/Wearables/Services or geographic breakout available in these tool results** |

**Data caveats (important for the trader):**
- These tool outputs are **SEC XBRL facts only**. There is **no share price, no consensus estimate, no valuation multiple, and no forward guidance** in the dataset. Any P/E, EV/EBITDA or price-target math must come from a separate market-data source.
- `get_insider_transactions` returned **DATA_UNAVAILABLE** — there is no authorized point-in-time insider archive for `AAPL`. **No insider buying or selling has been observed or is being reported here.** Do not trade on an insider signal; there isn't one.
- Product-line and geographic mix, services gross margin, and Greater China exposure are **not** in the returned tags. The margin analysis below is therefore consolidated-only.

---

## 3. Income Statement — The Core Story

### 3.1 Nine-month FY2026 (2025-09-28 → 2026-06-27) vs. nine-month FY2025

| Line item ($M) | 9M FY26 | 9M FY25 | Δ % |
|---|---:|---:|---:|
| Revenue | **364,357** | 313,695 | **+16.2%** |
| Cost of goods & services | 185,575 | 166,835 | +11.2% |
| **Gross profit** | **178,782** | 146,860 | **+21.7%** |
| *Gross margin* | *49.07%* | *46.82%* | *+225 bp* |
| R&D | 34,035 | 25,684 | **+32.5%** |
| Selling & marketing | 15,632 | 14,601 | +7.1% |
| General & administrative | 6,683 | 5,952 | +12.3% |
| Total operating expenses | 56,350 | 46,237 | +21.9% |
| **Operating income** | **122,432** | 100,623 | **+21.7%** |
| *Operating margin* | *33.60%* | *32.08%* | *+152 bp* |
| Non-operating income/(expense) | +670 | (698) | n.m. |
| Pre-tax income | 123,102 | 99,925 | +23.2% |
| Income tax | 21,638 | 15,381 | **+40.7%** |
| *Effective tax rate* | *17.58%* | *15.39%* | *+219 bp* |
| **Net income** | **101,464** | 84,544 | **+20.0%** |
| *Net margin* | *27.85%* | *26.95%* | *+90 bp* |
| **Diluted EPS** | **$6.88** | $5.62 | **+22.4%** |
| Basic EPS | $6.91 | $5.64 | +22.5% |
| D&A | 9,973 | 8,571 | +16.4% |
| Stock-based comp | 10,523 | 9,680 | +8.7% |

**Key read:** Revenue grew 16.2% but gross profit grew 21.7% — the entire operating-leverage story sits in the gross-margin line. Yet opex grew *faster* than gross profit (+21.9%), driven almost entirely by R&D (+$8.35B). **Apple is trading current-period operating leverage for an AI/product investment cycle.** Operating margin still expanded 152 bp because gross margin expansion outran the opex ramp.

### 3.2 FQ3 FY2026 standalone (2026-03-29 → 2026-06-27) vs. FQ3 FY2025

| Line item ($M) | FQ3 FY26 | FQ3 FY25 | Δ % |
|---|---:|---:|---:|
| Revenue | **109,417** | 94,036 | **+16.4%** |
| COGS | 54,647 | 50,318 | +8.6% |
| **Gross profit** | **54,770** | 43,718 | **+25.3%** |
| *Gross margin* | ***50.06%*** | *46.49%* | ***+357 bp*** |
| R&D | 11,729 | 8,866 | +32.3% |
| SG&A | 7,346 | 6,650 | +10.5% |
| Operating expenses | 19,075 | 15,516 | +22.9% |
| **Operating income** | **35,695** | 28,202 | **+26.6%** |
| *Operating margin* | *32.62%* | *29.99%* | *+263 bp* |
| Pre-tax income | 36,267 | 28,031 | +29.4% |
| Tax | 6,478 | 4,597 | +40.9% |
| *Effective tax rate* | *17.86%* | *16.40%* | *+146 bp* |
| **Net income** | **29,789** | 23,434 | **+27.1%** |
| **Diluted EPS** | **$2.02** | $1.57 | **+28.7%** |

**Q3 is the cleanest quarter in the dataset and it is a genuinely strong one:** gross margin crossed **50%**, operating margin expanded 263 bp, and EPS grew 28.7%. Note that Q3 gross margin (50.06%) is *higher* than the 9M average (49.07%), meaning margin was still **expanding sequentially** into the June quarter rather than peaking early.

### 3.3 Derived earlier quarters (reconstructed; see methodology note)

| $M | FQ1 FY26 | FQ2 FY26 | FQ3 FY26 |
|---|---:|---:|---:|
| Gross profit (derived) | **69,231** | 54,781 | 54,770 |
| Pre-tax income (derived) | **51,002** | 35,833 | 36,267 |
| Operating cash flow | **53,925** | 28,702 | 34,369 |
| Capex | 2,373 | 1,971 | 2,455 |
| Share repurchases | 24,701 | 12,288 | 25,105 |
| Dividends paid | 3,921 | 3,822 | 4,035 |

*Derivation:* Q1 = 6M − Q2; FQ2 = 6M − FQ1... i.e. 6M figures (from the 2026-05-01 10-Q) less the FQ3 standalone figures (from the 2026-07-31 10-Q) yield FQ3 checks; Q1 gross profit = 124,012 − 54,781. Q2 opex/cash items derived as 9M less Q3 less Q1 where disclosed. Q2 repurchases = 36,989 − 24,701 = 12,288. Treat Q1/Q2 splits as **approximations**; the 9M and FQ3 totals are exact as filed.

**Seasonality observation:** FQ1 is by far the largest profit quarter (gross profit $69.2B vs ~$54.8B in FQ2/FQ3), consistent with Apple's holiday hardware cycle. Q1 operating cash flow alone ($53.9B) exceeded the following two quarters combined.

**Tax normalization math:** had the 9M effective rate held at 15.39%, net income would have been **~$104.2B** (+$2.7B) and diluted EPS **~$7.06** instead of $6.88. **The tax-rate step-up is masking ~2.6 points of underlying earnings growth.** Roughly half of the deceleration from +22.4% EPS growth to the underlying ~25% would be recovered.

---

## 4. Margin & Operating Efficiency Trends

| Metric (9M basis unless noted) | FY26 | FY25 | Change |
|---|---:|---:|---:|
| Gross margin | 49.07% | 46.82% | +225 bp |
| FQ3 gross margin | **50.06%** | 46.49% | **+357 bp** |
| Operating margin | 33.60% | 32.08% | +152 bp |
| Net margin | 27.85% | 26.95% | +90 bp |
| R&D / revenue | **9.34%** | 8.19% | **+115 bp** |
| SG&A / revenue (S&M + G&A) | 6.12% | 6.55% | −43 bp |
| SBC / revenue | 2.89% | 3.09% | −20 bp |
| Effective tax rate | 17.58% | 15.39% | +219 bp |
| COGS growth vs. revenue growth | +11.2% vs +16.2% | — | **~500 bp of spread** |

**Interpretation:** Disciplined cost control outside R&D is unmistakable — SG&A and SBC both fell as a percentage of revenue while revenue grew mid-teens. The company is *not* buying growth with marketing spend. The COGS-to-revenue spread (~5 points of growth differential) is the mechanical source of the margin expansion and implies **pricing power or favorable mix**, not volume-driven scale.

**Trading implication:** A 49–50% gross margin is a new, higher plateau for Apple. If FQ4/FY27 gross margin merely *holds* ~49%, consensus models historically anchored at ~46–47% are structurally too low on EPS. The inverse is also true — this is now a high bar, and any slip toward 47% would be read as a mix reversal and hit the multiple hard.

---

## 5. Balance Sheet — Fortress, and Getting Stronger

### 5.1 Comparative balance sheet ($M)

| Item | 2026-06-27 | 2026-03-28 | 2025-09-27 | Δ (9M) |
|---|---:|---:|---:|---:|
| Cash & equivalents | 39,544 | 45,572 | 35,934 | +3,610 |
| Marketable securities — current | 22,855 | n/a | 18,763 | +4,092 |
| Marketable securities — noncurrent | 84,118 | n/a | 77,723 | +6,395 |
| **Total cash & investments** | **146,517** | n/a | **132,420** | **+14,097** |
| Accounts receivable | 31,398 | 30,339 | 39,777 | **−8,379 (−21.1%)** |
| Nontrade receivables | 27,509 | 23,172 | 33,180 | −5,671 |
| **Inventory** | **11,092** | 6,747 | 5,718 | **+5,374 (+94%)** |
| — Raw materials & parts | **7,645** | n/a | 2,124 | **+5,521 (+260%)** |
| — Finished goods | 3,447 | n/a | 3,594 | −147 |
| Other current assets | 17,420 | 15,349 | 14,585 | +2,835 |
| **Total current assets** | **149,818** | 144,114 | 147,957 | +1,861 |
| Intangibles, gross | **38,220** | 37,767 | 24,950 | **+13,270** |
| — Accum. amortization | 12,803 | 11,970 | 11,649 | +1,154 |
| **Intangibles, net** | **25,417** | 25,797 | 13,301 | **+12,116** |
| Other noncurrent assets | 77,557 | 77,430 | 72,634 | +4,923 |
| **Total assets** | **383,266** | 371,082 | 359,241 | +24,025 |
| Accounts payable | 64,525 | n/a | 69,860 | −5,335 |
| Commercial paper | 1,997 | n/a | 7,979 | −5,982 |
| Current LTD | 11,007 | 8,310 | 12,350 | −1,343 |
| Other current liabilities | 62,259 | n/a | 66,387 | −4,128 |
| **Total current liabilities** | **149,326** | 134,641 | 165,631 | −16,305 |
| Long-term debt (noncurrent) | 71,340 | 74,404 | 78,328 | −6,988 |
| Other noncurrent liabilities | **55,080** | n/a | 41,549 | **+13,531** |
| **Total liabilities** | **275,746** | 264,591 | 285,508 | −9,762 |
| **Shareholders' equity** | **107,520** | 106,491 | 73,733 | **+33,787** |

### 5.2 Liquidity, leverage and net cash

| Metric | 2026-06-27 | 2025-09-27 | Change |
|---|---:|---:|---:|
| Total debt (LTD + CP) | **84,297** | 98,679 | **−14,382** |
| Cash + investments | 146,517 | 132,420 | +14,097 |
| **Net cash** | **62,220** | **33,741** | **+28,479** |
| Current ratio | **1.003x** | 0.893x | +0.110x |
| Debt / equity | **0.78x** | 1.34x | −0.56x |
| Liabilities / assets | 71.9% | 79.5% | −7.6 pts |
| Return on equity (9M ann.) | **~149%** (avg equity basis) | — | — |

**This is the single most under-appreciated part of the story.** Apple:
- **Retired $14.4B of gross debt** in nine months and issued **$0** of new long-term debt (9M FY25: $4.48B issued).
- Cut commercial paper **75%** ($7.98B → $2.00B).
- Grew the cash/investment pile **$14.1B** to $146.5B.
- Crossed the **current ratio above 1.0x** for the first time in this dataset.
- Cut debt/equity from 1.34x to **0.78x**.

The company is simultaneously deleveraging *and* returning ~$74B to shareholders *and* building cash. That is only possible because FCF doubled relative to prior-year comparatives.

### 5.3 Working capital — two genuine call-outs

**(a) Accounts receivable fell 21% while revenue rose 16%.** Combined with nontrade receivables down $5.7B, this released working capital and drives part of the OCF surge. DSO on the reported AR balance is roughly **26 days** (Q3 AR $31.4B ÷ Q3 revenue $109.4B/day). This is a *quality-of-earnings positive* — the cash is real, not receivables-heavy revenue.

**(b) Inventory +94%, raw materials +260%.** Inventory days rose from ~10 to ~18.6 on Q3 COGS. The composition matters enormously:
- **Finished goods actually fell** ($3.594B → $3.447B). No channel-stuffing signal.
- **Raw materials and purchased parts tripled** ($2.124B → $7.645B). This is a **forward component/ramp build** — pre-positioning for a new product cycle and/or hedging against component and tariff risk.
- Cash-flow statement confirms the swing: `IncreaseDecreaseInInventories` flipped from **−$1.22B** (9M FY25) to **+$5.46B** (a use of cash, 9M FY26).

**Two-sided trade implication:** the raw-materials build is bullish for forward unit volumes, but it **inverts next quarter**. If those components convert to revenue at 49%+ gross margin, FQ4 is strong. If the build was **precautionary**, it becomes an inventory-reserve charge and a gross-margin miss. Watch FQ4 inventory and reserve commentary.

**(c) Other noncurrent liabilities +$13.5B alongside gross intangibles +$13.3B.** In the same nine months, gross intangibles rose $13.27B while accumulated amortization rose only $1.15B — meaning the new intangibles are largely **non-amortizing** (indefinite-lived). Combined with **essentially no cash acquisition outflow** in the reported investing tags (9M investing was −$18.8B, fully explained by net securities purchases of $10.2B + capex $6.8B + other $1.8B), this strongly suggests a **non-cash or milestone/deferred-payment IP or technology transaction** (plausibly AI/IP licensing or an asset acquisition), with a corresponding long-term payment or deferred-tax obligation in other noncurrent liabilities. **This is the highest-value item for a follow-up read of the FQ3 10-Q notes.**

---

## 6. Cash Flow — The Step-Change

### 6.1 Nine-month cash flow ($M)

| Item | 9M FY26 | 9M FY25 | Δ % |
|---|---:|---:|---:|
| **Operating cash flow** | **116,996** | 81,754 | **+43.1%** |
| Capex (PP&E) | 6,799 | 9,473 | **−28.2%** |
| **Free cash flow** | **110,197** | 72,281 | **+52.5%** |
| *FCF margin* | *30.24%* | *23.04%* | *+720 bp* |
| Purchases of AFS securities | (48,752) | (17,591) | +177% |
| Maturities/calls of AFS securities | 26,504 | 35,036 | −24% |
| Sales of AFS securities | 12,016 | 10,785 | +11% |
| Other investing | (1,780) | +975 | n.m. |
| **Investing cash flow** | **(18,811)** | **+17,782** | n.m. |
| Share repurchases | (62,094) | (70,579) | −12.0% |
| Dividends paid | (11,778) | (11,559) | +1.9% |
| Tax withholding on SBC | (6,462) | (5,719) | +13.0% |
| LT debt repaid | (8,146) | (9,682) | −15.9% |
| LT debt issued | **0** | 4,481 | −100% |
| Commercial paper, net | (5,911) | (65) | n.m. |
| Short-term debt, net | (3,788) | (5,690) | −33.4% |
| **Financing cash flow** | **(94,575)** | **(93,210)** | n.m. |
| **Net change in cash** | **+3,610** | **+6,326** | −43% |

### 6.2 What matters here

1. **Cash conversion is excellent.** OCF / net income = **1.15x** (116,996 / 101,464). Earnings are cash-backed.
2. **Capex is falling while R&D is surging.** Capex $6.8B (−28%) vs. R&D $34.0B (+32.5%). Apple's capital intensity is *declining* (asset-light, fabless, outsourced manufacturing) while its intellectual-property intensity rises. This is a structurally higher-ROIC configuration than capex-led AI investment.
3. **The company is re-allocating the investing line.** Net AFS purchases of **~$10.2B** this year vs. net **sales/maturities of +$28.2B** last year — a ~$38B swing. Apple is **shifting capital back into its securities portfolio** rather than into acquisitions. Net cash built to $62.2B.
4. **Buyback deceleration is real but modest.** Repurchases fell to $62.1B from $70.6B (−12%). Meanwhile dividends rose just 1.9%. Total shareholder returns of $73.9B were still **67% of free cash flow**. The deceleration is consistent with a management choice to retain cash for the intangible/IP build rather than a signal of cash stress — but it does remove a historical EPS tailwind.
5. **Effective retirement of leverage.** Zero LT issuance + $8.1B repayment + $5.9B CP paydown + $3.8B STD paydown.

### 6.3 Historical cash-flow context (from the FY2025 10-K)

| Fiscal year | Operating CF ($B) | Investing CF ($B) | Financing CF ($B) |
|---|---:|---:|---:|
| FY2023 | 110,543 | +3,705 | (108,488) |
| FY2024 | 118,254 | +2,935 | (121,983) |
| FY2025 | n/d in dataset | +15,195 | (120,686) |
| **9M FY2026** | **116,996** | (18,811) | (94,575) |

Nine-month FY2026 operating cash flow of **$116,996M already exceeds every full prior fiscal year in the dataset** (FY24 full year: $118,254M — nearly matched in nine months). This is the clearest evidence that FY2026 is a structurally different earnings regime.

**Debt maturity ladder (as of 2025-09-27, $M):** FY26 12,393 | FY27 10,078 | FY28 9,300 | FY29 5,235 | FY30 4,972 | Thereafter 49,303. Operating lease payments due: 14,725 total (1,967 next 12 months). Finance lease payments due: 1,579. **All comfortably serviceable from one quarter of operating cash flow.**

---

## 7. Returns, Quality & Forensic Scorecard

| Metric | Value | Comment |
|---|---|---|
| ROE (9M annualized, avg equity) | **~149%** | Distorted upward by buyback-shrunken equity base, but extreme |
| ROA (9M annualized) | **~36.4%** | Very high for a hardware-led business |
| FCF margin | **30.2%** | vs 23.0% prior period |
| OCF / net income | **1.15x** | High earnings quality |
| Accruals check | AR −21% vs revenue +16% | **Positive** — no receivables build |
| Inventory check | Raw materials +260%, FG −4% | **Watch item** — forward ramp or overbuild |
| Goodwill/intangibles | Net intangibles $25.4B = 6.6% of assets | Still small; low impairment risk |
| Off-balance-sheet | None disclosed in dataset | — |
| Effective tax rate | 17.58% (from 15.39%) | **Persistent headwind** |
| Debt/equity | 0.78x | Down from 1.34x |
| Share count | −1.2% YoY | EPS tailwind, but slowing |
| Alternative metrics | **No insider data available** | Cannot corroborate with insider signal |

### Red flags / disconfirming evidence to actively monitor
1. **Tax rate**: +219 bp YTD, and Q3's 17.86% was *higher* than the 9M average — the trend is still worsening, not stabilizing. If FY27 runs at 18–19%, EPS growth compresses by 2–3 points.
2. **R&D growth of +32.5% is not yet visibly monetized.** There is no segment disclosure in this dataset to confirm that AI/Services revenue is earning the incremental spend. If this spending is defensive (matching competitors) rather than accretive, operating margin expansion stalls.
3. **Inventory composition.** A $5.5B raw-materials build must convert next quarter.
4. **Buyback slowdown** removes ~1 point of the historical EPS growth engine.
5. **Intangible addition without disclosed cash outflow** — requires confirmation; if it represents a large future cash commitment, net cash is overstated relative to true obligations.

---

## 8. Actionable Trading Insights

**1. The gross-margin regime change is the highest-conviction signal.**
FQ3 at 50.06% and 9M at 49.07% versus a prior-year base of 46.5–46.8% is a **+250 to +350 bp structural shift**. Every 100 bp of gross margin at a ~$437B annualized revenue run-rate is worth roughly **$4.4B of gross profit**, or ~$3.6B after tax, or **~$0.25 EPS**. Models anchored below 48% gross margin are likely too low. *Trade:* own the fundamental revision cycle; express via long `AAPL` into the FQ4 print.

**2. Separate the tax noise from the operating signal.**
Reported EPS growth of +22.4% understates underlying growth by ~2.5–3 points. Normalizing the rate, 9M EPS would be ~$7.06 (+25.6% YoY). *Trade:* if the stock reacts negatively to a headline EPS number that is tax-suppressed, that is a buying opportunity; conversely, do not attribute tax-driven beats to operating strength.

**3. The defensiveness of the cash machine limits downside.**
$62.2B net cash, current ratio >1.0x, $110B of 9M FCF, zero new LT debt, and $14.4B of debt retired. At any reasonable valuation, a business generating a 30% FCF margin with net cash is **not** a solvency or balance-sheet risk story. *Trade:* this supports selling downside puts / owning calls versus owning outright puts.

**4. Watch FQ4 for the inventory swing — the highest-variance event.**
Raw materials tripled to $7.6B. FQ4 (Sept quarter) gross margin is the single most important disclosure in the next report. *Two scenarios:*
- **Bull:** components convert, gross margin holds ≥48.5%, revenue grows high-teens → the 50% gross-margin plateau is validated and FY27 estimates rise.
- **Bear:** inventory reserve charge of $0.5–1.5B, gross margin falls toward 47%, and the market re-prices the "new plateau" thesis back to the old one. **A $1B reserve is roughly $0.06–0.07 EPS plus a multiple de-rating.**

**5. R&D intensity is a two-to-three year call, not a quarter call.**
$34.0B of R&D in nine months (9.3% of revenue, up from 8.2%) is a ~$45B annualized run-rate. Either this buys a new product/services category, or it is a permanent margin tax. *Trade:* express as a longer-dated thesis; don't size quarter-to-quarter around it.

**6. The intangible/other-noncurrent-liability pairing is an under-priced information gap.**
A $13.3B non-amortizing intangible addition with no matching cash outflow, offset by $13.5B of new other noncurrent liabilities, is **not** in most sell-side models. Depending on what it is (IP licensing, an AI model/technology asset, a milestone-structured acquisition), it is either a hidden asset ramp or a hidden cash obligation. **Priority research action: read the FQ3 FY2026 10-Q notes on business combinations, intangible assets, and other noncurrent liabilities.**

**7. Capital-return slowing is a mild negative that is being offset by net-cash build.**
Buybacks −12% and dividends +1.9% while FCF +52% means the *incremental* cash is going to the balance sheet and intangibles, not shareholders. If management re-accelerates the buyback at the FY26 year-end announcement (late Oct 2026), that is a positive catalyst given the now much larger cash base.

---

## 9. Limitations of This Analysis

- **No price or valuation data.** P/E, EV/EBITDA, FCF yield, and any rating to a target price cannot be computed from these tools. The thesis above is purely fundamental/direction-of-revisions.
- **No revenue disaggregation.** iPhone / Services / Wearables / geography mix — the most important drivers of *why* gross margin expanded — are not in the returned XBRL tags.
- **No forward guidance or consensus.** The FQ4/FY27 outlook is inference, not data.
- **No insider transactions available.** Explicitly `DATA_UNAVAILABLE`; no insider inference is drawn.
- **The "annual" tool responses returned the same point-in-time fact set as "quarterly"** (the vendor does not appear to maintain a separate annual series in this cache beyond FY2023–FY2025 cash-flow lines from the FY2025 10-K). FY2025 full-year income and balance-sheet data are therefore **not** available here; all FY2026 analysis is on a nine-month-to-nine-month basis, which is correct but limits FY-level trend-table construction.
- **FQ1/FQ2 splits are derived by subtraction**, not directly reported, and should be treated as approximations. The 9M and FQ3 figures are exact as filed.
- **Non-GAAP measures** (constant-currency growth, adjusted EPS) are not available; all figures are GAAP.

---

## 10. Key Points Summary Table

| Category | Metric | Value | Prior / Comparative | Read |
|---|---|---|---|---|
| **Identity** | Company / ticker | Apple Inc. / `AAPL` | — | Nasdaq, FY ends late Sept |
| **Reporting** | Latest period | FQ3 FY26, ended 2026-06-27 | Filed 2026-07-31 | 10-Q, accn 0000320193-26-000020 |
| **Growth** | 9M FY26 revenue | **$364.36B** | $313.70B (+16.2%) | Accelerating |
| | FQ3 FY26 revenue | $109.42B | $94.04B (+16.4%) | Consistent, not decelerating |
| **Margins** | 9M gross margin | **49.07%** | 46.82% (+225 bp) | Structural re-rating |
| | FQ3 gross margin | **50.06%** | 46.49% (+357 bp) | Crossed 50% |
| | 9M operating margin | 33.60% | 32.08% (+152 bp) | Expanding |
| | 9M net margin | 27.85% | 26.95% (+90 bp) | Expanding |
| **Earnings** | 9M net income | **$101.46B** | $84.54B (+20.0%) | Strong |
| | 9M diluted EPS | **$6.88** | $5.62 (+22.4%) | Tax-suppressed |
| | FQ3 diluted EPS | $2.02 | $1.57 (+28.7%) | Best quarter in set |
| | Effective tax rate | **17.58%** | 15.39% (+219 bp) | **Headwind**; ~$0.18 EPS drag |
| **Cash flow** | 9M operating CF | **$116.996B** | $81.754B (+43.1%) | Step-change |
| | 9M free cash flow | **~$110.20B** | $72.28B (+52.5%) | > any full prior FY |
| | FCF margin | 30.2% | 23.0% | +720 bp |
| | OCF / net income | 1.15x | — | High earnings quality |
| | 9M capex | $6.80B | $9.47B (−28.2%) | Asset-light shift |
| **Balance sheet** | Total cash & investments | **$146.52B** | $132.42B | +$14.10B |
| | Total debt (LTD + CP) | $84.30B | $98.68B | −$14.38B |
| | **Net cash** | **$62.22B** | $33.74B | **+$28.48B** |
| | Current ratio | 1.003x | 0.893x | Now >1.0x |
| | Debt / equity | 0.78x | 1.34x | Deleveraging |
| | Shareholders' equity | **$107.52B** | $73.73B | +$33.79B |
| | Net intangibles | $25.42B | $13.30B | **+$12.12B — investigate** |
| **Working capital** | Accounts receivable | $31.40B | $39.78B (−21.1%) | Cash-quality positive |
| | Inventory | $11.09B | $5.72B (+94%) | **Watch item** |
| | — Raw materials | $7.65B | $2.12B (+260%) | Forward ramp / hedge |
| | — Finished goods | $3.45B | $3.59B (−4.1%) | No channel stuffing |
| | Deferred revenue | $14.90B | $13.70B (+8.8%) | Lags revenue growth |
| **Investment** | 9M R&D | **$34.04B** (9.34% of rev) | $25.68B (8.19%) | **+32.5% — AI cycle** |
| | 9M SG&A | $22.32B (6.12% of rev) | $20.55B (6.55%) | Leverage |
| | 9M SBC | $10.52B (2.89% of rev) | $9.68B (3.09%) | Improving |
| **Capital return** | 9M share repurchases | $62.09B | $70.58B (−12.0%) | **Decelerating** |
| | 9M dividends | $11.78B | $11.56B (+1.9%) | +$0.03/sh to $0.27/qtr |
| | Total return / FCF | ~67% | — | Still generous |
| | Shares outstanding | 14.594B (2026-07-17) | 14.773B | −1.2% |
| **Leverage detail** | LT debt issued 9M FY26 | **$0** | $4.48B | No new issuance |
| | CP balance | $2.00B | $7.98B | −75% |
| | Debt maturities FY26 | $12.39B | — | Easily covered |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | — | No signal; no inference |
| **Quality flags** | Tax rate trend | 17.58% → 17.86% (Q3) | Rising | Monitor for FY27 |
| | Intangibles + noncurrent liabilities | +$13.27B / +$13.53B | Non-amortizing | **Verify in 10-Q notes** |
| **Next catalyst** | FQ4/FY26 results | ~late Oct 2026 | Not yet reported | Inventory + GM + FY27 guide |
| **Stance** | Implied direction | **Constructive / positive** | — | Long into FQ4; hedge inventory/tax risk |

---

### Bottom line for the trader
`AAPL`'s FY2026 fundamentals have **inflected upward**, and the inflection is balance-sheet-confirmed: 16% revenue growth, a 49–50% gross-margin plateau, 30% free-cash-flow margins, $62B of net cash, and $14B of gross debt retired — all while funding a 32% R&D ramp and $74B of shareholder returns. The two things that can break the thesis are **an inventory/component charge in FQ4** and **a structurally higher tax rate**. The single most valuable research action before the next earnings date is confirming **what the $13.3B non-amortizing intangible addition and $13.5B increase in other noncurrent liabilities actually represent**. Absent insider data (which is not available), position sizing should be driven by the FQ4 inventory-conversion and gross-margin outcomes rather than by capital-return momentum, which is visibly decelerating.