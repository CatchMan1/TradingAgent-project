# AAPL (Apple Inc.) — Fundamental Research Report
**Point-in-time as of 2024-01-31 (market close)** | Data source: SEC facts cached in the fundamental vendor, filtered by actual EDGAR acceptance timestamp

---

## 1. Bottom Line Up Front

| Verdict element | Evidence |
|---|---|
| **Quality: Elite** | FY23 gross margin **44.1%** (record), operating margin **29.8%**, net margin **25.3%**, FCF **$99.6B** on $383.3B revenue (26.0% FCF margin) |
| **Growth: Stalled** | FY23 revenue **–2.8% YoY** ($383.3B vs $394.3B); op income **–4.3%**; net income **–2.8%**; diluted EPS **+0.3%** ($6.13 vs $6.11) — EPS growth now comes from buyback, not operations |
| **Balance sheet: Fortress** | **~$51.0B net cash** ($162.1B cash+securities vs $111.1B gross debt); debt laddered out to 5+ years; **–68 day cash conversion cycle** |
| **Capital return: The EPS engine** | $92.6B returned in FY23 (=$77.6B buyback + $15.0B dividends) = **95.5% of free cash flow** |
| **Insider signal: None available** | Vendor has **no authorized point-in-time insider archive for AAPL**; no inference made |
| **Critical caveat** | Latest filed financials are **FY2023 (10-K accepted 2023-11-03)**. The **Dec-2023 quarter (Q1 FY24) was NOT yet filed** as of 2024-01-31. Fundamentals are ~4 months stale and a major earnings release is imminent. |

---

## 2. Data Vintage & Disclosure Caveats (read before trading on this)

1. **Latest 10-K:** FY2023, period ended **2023-09-30**, accepted by EDGAR **2023-11-03 02:08 UTC** (`0000320193-23-000106`).
2. **Latest 10-Q in the dataset:** period ended **2023-07-01** (filed 2023-08-04). Apple does not file a Q4 10-Q, so the FY23 10-K is the terminal quarter.
3. **Q1 FY2024 (quarter ended ~2023-12-30) is absent** — it had not been accepted as of 2024-01-31. Any trade placed on this report is trading on **pre-holiday-quarter information** into an unresolved catalyst.
4. **Revenue is derived, not directly tagged.** The vendor did not return a `Revenues` tag. Revenue below = `GrossProfit + CostOfGoodsAndServicesSold` (both tool-sourced), which reconciles to Apple's reported figures (FY23: $169,148M + $214,137M = **$383,285M**).
5. **R&D vs SG&A split is not in the dataset** — only total `OperatingExpenses` ($54,847M) is available. Do not assume a line-item split from this report.
6. **Balance-sheet tag quirks:** the vendor's `AssetsNoncurrent` / `NoncurrentAssets` rows ($43,715M) actually carry PP&E-net values, *not* total noncurrent assets ($209,017M per the correctly-tagged `AssetsNoncurrent` row). I use $209,017M for total noncurrent assets and treat $43,715M as PP&E net.
7. **Insider transactions: DATA UNAVAILABLE.** No insider buy/sell activity is reported or estimated in this report.

---

## 3. Company Profile

**Apple Inc.** (NASDAQ: AAPL) — designer and marketer of smartphones (iPhone), personal computers (Mac), tablets (iPad), wearables/home/accessories, and a large and growing **Services** franchise (App Store, iCloud, Apple Music/TV+, advertising, AppleCare, payments). Vertically integrated hardware + silicon (Apple-designed SoCs) with an outsourced manufacturing model and an owned retail/online distribution footprint.

Structural characteristics visible directly in the FY23 statements:
- **Asset-light manufacturing but capital-heavy buybacks:** capex only **$10.96B** on $383.3B revenue (**2.9% of revenue**) — the hardware is not built on Apple's balance sheet.
- **Extreme supplier leverage:** accounts payable **$62.6B** vs inventory of only **$6.3B**.
- **Services-driven mix shift:** gross margin expanded ~235bp in a *declining-revenue* year, the signature of mix shifting toward higher-margin Services.
- **Entity scale:** public float was **$2.591 trillion** at 2023-03-31 (`EntityPublicFloat`), with **15,550,061,000** shares outstanding at 2023-09-30 and **15,552,752,000** as of 2023-10-20.

---

## 4. Income Statement — Three-Year History (FY2021–FY2023, fiscal years ending late September)

| $M unless noted | FY2021 | FY2022 | FY2023 | FY23 YoY |
|---|---:|---:|---:|---:|
| Revenue (derived) | 365,817 | 394,328 | **383,285** | **–2.8%** |
| Cost of goods & services sold | 212,981 | 223,546 | 214,137 | –4.2% |
| **Gross profit** | 152,836 | 170,782 | **169,148** | –1.0% |
| *Gross margin* | *41.8%* | *43.3%* | ***44.1%*** | *+82bp* |
| Operating expenses (total) | 43,887 | 51,345 | **54,847** | **+6.8%** |
| *Opex % of revenue* | *12.0%* | *13.0%* | *14.3%* | *+129bp* |
| **Operating income** | 108,949 | 119,437 | **114,301** | **–4.3%** |
| *Operating margin* | *29.8%* | *30.3%* | *29.8%* | *–45bp* |
| Investment income (interest & dividend) | 2,843 | 2,825 | 3,750 | +32.7% |
| Interest expense | 2,645 | 2,931 | 3,933 | +34.2% |
| Non-operating income/(expense) net | 258 | (334) | (565) | worse |
| Pretax income | 109,207 | 119,103 | 113,736 | –4.5% |
| Income tax expense | 14,527 | 19,300 | 16,741 | –13.3% |
| *Effective tax rate* | *13.3%* | *16.2%* | *14.7%* | *–150bp* |
| **Net income** | 94,680 | 99,803 | **96,995** | –2.8% |
| *Net margin* | *25.9%* | *25.3%* | *25.3%* | flat |
| Diluted EPS | $5.61 | $6.11 | **$6.13** | **+0.3%** |
| Basic EPS | $5.67 | $6.15 | $6.16 | +0.2% |
| Implied diluted shares (NI/EPS) | ~16,877M | ~16,334M | **~15,823M** | **–3.1%** |
| Comprehensive income | 95,249 | 88,531 | 96,652 | +9.2% |

### What the income statement is actually telling you
- **Margin expansion is doing all the work.** Gross margin rose 41.8% → 43.3% → **44.1%** over three years (+235bp) even as revenue fell. This is the Services-mix story and pricing power, and it is the single most important fundamental trendline in the file.
- **Negative operating leverage is now visible.** Opex grew **+17.0%** in FY22 and **+6.8%** in FY23 against revenue of +7.8% and **–2.8%**. Opex as a share of revenue has climbed from 12.0% to 14.3% in two years. If revenue is flat-to-down again, margin expansion alone will not carry op income growth.
- **EPS is being manufactured by the float, not the P&L.** Diluted shares fell ~3.1% (16,334M → 15,823M). That is what turned a 2.8% net-income decline into +0.3% EPS. **Every 1% of buyback ≈ +1% EPS with zero operational improvement.** This is the crux of the AAPL equity story at this data vintage.
- **Interest is now a two-way line.** Investment income rose to $3.75B (+32.7%) on higher yields, but interest expense rose to $3.93B (+34.2%) as older low-coupon debt was refinanced/rolled. Net interest flipped from +$0.20B (FY21) to roughly –$0.18B (FY23). Interest coverage remains enormous at **29.1x** (op income / interest expense), so this is an EPS headwind, not a solvency issue.
- **Tax rate is unsustainably low.** 14.7% effective vs a 21% statutory rate, driven by the foreign-derived rate differential (–$5.74B in FY23), R&D credits (+$1.21B), and share-based comp excess benefits (–$1.12B). A 200bp normalization to ~16.7% would cost roughly **$2.3B of net income ≈ $0.14–0.15 of EPS** (~2.4%). See §9 for the quantified Irish/state-aid exposure.

### Recent interim trends (9M FY2023, from the 2023-08-04 10-Q)
| $M | 9M FY2022 | 9M FY2023 | Change |
|---|---:|---:|---:|
| Operating cash flow | 98,024 | 88,945 | **–9.3%** |
| Investing cash flow | (21,137) | +1,311 | swing |
| Financing cash flow | (83,955) | (85,335) | –1.6% |
| Share repurchases | 64,974 | 56,547 | **–13.0%** |
| Dividends paid | 11,138 | 11,267 | +1.2% |
| Capex | 7,419 | 8,796 | +18.6% |

**Read:** cash generation was decelerating through the first nine months of FY23 (–9.3% OCF) while capex accelerated (+18.6%). The FY23 full-year OCF decline of –9.5% ($122.2B → $110.5B) confirms this was a genuine, full-year cash-flow deceleration — not a timing artifact.

---

## 5. Balance Sheet — FY2023 (as of 2023-09-30) vs FY2022

### Assets
| $M | 2022-09-24 | 2023-09-30 | Change |
|---|---:|---:|---:|
| Cash & cash equivalents | 23,646 | 29,965 | +26.7% |
| Marketable securities, current (implied) | 24,658 | 31,590 | +28.1% |
| Accounts receivable, net | 28,184 | 29,508 | +4.7% |
| Nontrade receivables (current) | 32,748 | 31,477 | –3.9% |
| Inventory, net | 4,946 | 6,331 | **+28.0%** |
| Other current assets | 21,223 | 14,695 | –30.8% |
| **Total current assets** | **135,405** | **143,566** | **+6.0%** |
| Marketable securities, noncurrent | ~91,500 | 100,544 | +9.9% |
| PP&E, net | 42,117 | 43,715 | +3.8% |
| Other noncurrent assets | 39,053 | 64,758 | +65.8% |
| **Total noncurrent assets** | **217,350** | **209,017** | –3.8% |
| **TOTAL ASSETS** | **352,755** | **352,583** | **flat** |

**Implied total cash + investments: $29,965 + $31,590 + $100,544 = ~$162,099M** — effectively unchanged in scale but shifted out of "other current assets" into securities.

### Liabilities & Equity
| $M | 2022-09-24 | 2023-09-30 | Change |
|---|---:|---:|---:|
| Accounts payable | 64,115 | 62,611 | –2.3% |
| Other current liabilities | 60,845 | 58,829 | –3.3% |
| Other accrued liabilities (current) | 54,293 | 50,010 | –7.9% |
| Commercial paper | 9,982 | 5,985 | **–40.0%** |
| Current portion of LT debt | 11,128 | 9,822 | –11.7% |
| Deferred revenue (current) | 7,912 | 8,061 | +1.9% |
| **Total current liabilities** | **153,982** | **145,308** | **–5.6%** |
| Long-term debt, noncurrent | 98,959 | 95,281 | –3.7% |
| Deferred revenue (total) | 12,400 | 12,100 | –2.4% |
| Other noncurrent liabilities | 49,142 | 49,848 | — |
| **Total liabilities** | **302,083** | **290,437** | **–3.9%** |
| **Shareholders' equity** | **50,672** | **62,146** | **+22.6%** |
| Common stock + APIC | 64,849 | 73,812 | +13.8% |
| AOCI | (11,109) | (11,452) | –3.1% |
| Shares outstanding | 15,943,425,000 | 15,550,061,000 | **–2.5%** |

### Derived balance-sheet metrics
| Metric | FY2022 | FY2023 | Interpretation |
|---|---:|---:|---|
| **Gross debt** (CP + current LTD + noncurrent LTD) | $119.7B | **$111.1B** | Deleveraging modestly |
| **Net cash** (cash+securities – gross debt) | ~$29.9B | **~$51.0B** | Improved $21B in one year |
| Current ratio | 0.88x | **0.99x** | Improving, still <1 |
| Quick ratio | 0.85x | **0.94x** | No liquidity stress |
| Working capital | –$18,577M | **–$1,742M** | Vastly improved |
| Debt / equity | 2.36x | **1.79x** | High but structurally normal for AAPL |
| Total liabilities / assets | 85.7% | **82.4%** | Deleveraging |
| Book value / share | $3.18 | **$4.00** | Thin equity base |
| ROE (NI / equity) | 197% | **156%** | Distorted by buybacks — not a quality metric here |
| ROA (NI / assets) | 28.3% | **27.5%** | Genuinely exceptional |
| ROIC (NOPAT $97.5B / equity+debt $173.2B) | ~62% | **~56%** | Best-in-class capital efficiency |

### Working-capital efficiency (FY2023, using derived revenue/COGS)
- Days sales outstanding: **28.1 days** (AR $29.5B / rev $383.3B)
- Days inventory outstanding: **10.8 days** (Inv $6.3B / COGS $214.1B)
- Days payable outstanding: **106.7 days** (AP $62.6B / COGS $214.1B)
- **Cash conversion cycle: –67.8 days** — suppliers fund 68 days of Apple's operations. This is why Apple can run a sub-1.0 current ratio with zero financial risk.

### Debt maturity ladder (as of 2023-09-30) — no refinancing wall
| Period | $M |
|---|---:|
| Next 12 months | 9,943 |
| Year 2 | 10,775 |
| Year 3 | 12,265 |
| Year 4 | 9,786 |
| Year 5 | 7,800 |
| After year 5 | **56,003** |
| **Total term debt** | **106,572** |

Plus operating lease liabilities **$11,818M** (current $1,410M / noncurrent $10,408M) and finance leases **$1,024M**. Roughly **53% of term debt matures beyond five years** — a highly favorable position if refinancing costs stay elevated. Only ~$9.9B must be termed out in the next year against $110.5B of annual OCF: **trivial rollover risk.**

### Balance-sheet watch items
1. **Inventory +28.0% YoY** ($4.95B → $6.33B) against a 2.8% revenue *decline* — the only notable working-capital warning sign in the file, though the absolute dollar amount is still immaterial to the P&L (inventory = 1.7% of revenue).
2. **Other noncurrent assets +65.8%** ($39.1B → $64.8B) — largely the noncurrent marketable securities restructuring; watch that this is duration, not opacity.
3. **AOCI still –$11.45B** — the residual mark-to-market drag from the 2022 rate shock. Improving: the FY23 AFS adjustment swung **+$1.82B positive** (vs –$11.90B in FY22), meaning the bond portfolio has stopped bleeding. A rate-cut cycle would be a direct, unrecognized book-value tailwind.
4. **Restricted AFS securities $13.8B** (up from $12.7B) — largely tied to Apple's U.S. manufacturing/Corning-type commitments held in restricted form.

---

## 6. Cash Flow Statement — FY2021–FY2023

| $M | FY2021 | FY2022 | FY2023 | FY23 YoY |
|---|---:|---:|---:|---:|
| **Operating cash flow** | 104,038 | **122,151** | **110,543** | **–9.5%** |
| Depreciation & amortization | 11,284 | 11,104 | 11,519 | +3.7% |
| Share-based compensation | 7,906 | 9,038 | **10,833** | **+19.9%** |
| Deferred taxes | — | — | (net deferred benefit across fed/state/foreign) | — |
| Increase in AR (use) | (10,125) | (1,823) | (1,688) | improving |
| Other receivables | (3,903) | (7,520) | +1,271 | swing |
| Other operating assets | (8,042) | (6,499) | (5,684) | improving |
| Other operating liabilities | +7,475 | +6,110 | +3,031 | deteriorating |
| Capex (PP&E) | (11,085) | (10,708) | (10,959) | +2.3% |
| **FREE CASH FLOW (OCF – capex)** | **92,953** | **111,443** | **99,584** | **–10.6%** |
| *FCF margin* | *25.4%* | *28.3%* | *26.0%* | –230bp |
| **Investing cash flow (net)** | (14,545) | (22,354) | **+3,705** | swing to inflow |
| — Purchases of AFS securities | (109,558) | (76,923) | (29,513) | **–61.6%** |
| — Proceeds from maturities | 59,023 | 29,917 | 39,686 | +32.7% |
| — Proceeds from sales | 47,460 | 37,446 | 5,828 | –84.4% |
| **Financing cash flow (net)** | (93,353) | (110,749) | **(108,488)** | –2.0% |
| — **Share repurchases** | (85,971) | (89,402) | **(77,550)** | **–13.3%** |
| — **Dividends paid** | (14,467) | (14,841) | **(15,025)** | +1.2% |
| — RSU tax withholding | (6,556) | (6,223) | (5,431) | –12.7% |
| — LT debt issued | 20,393 | 5,465 | 5,228 | — |
| — LT debt repaid | (8,750) | (9,543) | **(11,151)** | +16.9% |
| — Commercial paper, net | +1,022 | +3,955 | **(3,978)** | deleveraging |
| **Net change in cash (incl. FX)** | (3,860) | (10,952) | **+5,760** | swing |

### Cash-flow read-through
- **Cash quality remains excellent:** FCF of $99.6B = **90.1% of net income** ($96,995M), even after a 10.6% FCF decline. Declines were driven by working capital and lower net income, not accrual games.
- **The securities portfolio is being wound down, not built.** Purchases of AFS securities collapsed **–61.6%** to $29.5B while maturities brought in $39.7B. Apple converted its investment portfolio into buybacks. This is why investing swung to a **+$3.7B inflow** for the first time in three years.
- **Buybacks decelerated harder than the business.** Repurchases fell **–13.3%** ($89.4B → $77.6B), roughly 4x the rate of the revenue decline. Historically Apple has *increased* buybacks in downturns; the FY23 pullback signals either buyback-budget discipline or price sensitivity at higher share prices. **This is the key vulnerability in the EPS-manufacturing thesis** — if buybacks shrink further, the ~3% annual float reduction that has been masking net-income declines stops working.
- **SBC is inflating fast and being masked.** SBC rose **+19.9%** to $10.83B in a year with flat headcount economics, and **$18.6B of unrecognized SBC cost remains to be recognized**. Also note total capital returned ($92.6B) already includes $5.4B of RSU tax withholding — the *real* cost of comp is higher than the reported opex line.
- **Dividend is trivially covered but trivially sized.** $15.0B paid = **15.5% payout of net income**; FY23 DPS $0.94 (~$0.24/quarter). There is enormous room to raise, but management clearly prioritizes buybacks.

---

## 7. Capital Allocation Scorecard (FY2023)

| Use of cash | $M | % of FCF ($99,584M) |
|---|---:|---:|
| Share repurchases | 77,550 | **77.9%** |
| Dividends | 15,025 | 15.1% |
| **Total shareholder return** | **92,575** | **93.0%** |
| RSU tax withholding (comp-related) | 5,431 | 5.5% |
| Capex | 10,959 | 11.0% |
| Net debt repayment (CP + LTD net) | ~(9,901) | net source |
| **Total deployed on returns + capex + withholding** | **108,965** | **109.4%** |

Apple returned **93% of free cash flow** to shareholders and funded the balance with net debt reduction and portfolio drawdown. **There is no reinvestment engine being funded here** — capex is 2.9% of revenue. That is a deliberate, mature-cash-cow capital allocation model: the stock is a **capital-return instrument**, not a growth-reinvestment instrument, at this data vintage.

---

## 8. Insider Transactions

**DATA UNAVAILABLE.** The vendor explicitly reports no authorized, point-in-time insider-transactions archive for AAPL as of 2024-01-31. 

**No insider buying or selling is asserted, implied, or estimated in this report.** Any downstream recommendation should treat insider sentiment as **unmeasured**, not neutral. Do not read a "no signal" into this — it is a data gap, not an observation.

---

## 9. Tax, Contingent, and Off-Balance-Sheet Items (quantified)

| Item | $M | Implication |
|---|---:|---|
| Effective tax rate FY23 | **14.7%** | vs 21% statutory; 630bp of benefit |
| Foreign rate differential benefit | (5,744) | Largest single driver; Pillar Two / global minimum tax directly attacks this |
| R&D tax credits | 1,212 | Recurring, stable |
| SBC excess tax benefit | (1,120) | Shrinks as SBC-driven |
| Cash taxes paid | **18,679** | vs $16,741 book expense — cash taxes run *above* book |
| **Unrecognized tax benefits — reasonably possible decrease** | **4,500** | **Direct quantified downside: ~$4.5B, ≈$0.28 EPS, ≈4.6% of FY23 net income** |
| Deferred tax assets, net | 24,369 | Includes $8,374 valuation allowance (up from $7,530) |
| Deferred tax assets, gross | 32,743 | Grew 12.1% YoY |
| Employee SBC not yet recognized | 18,600 | Future expense already committed |
| Operating lease liabilities | 11,818 | Off traditional debt; ~1.2x annual FCF coverage, immaterial |
| Finance lease liabilities | 1,024 | Immaterial |
| Purchase/contract liabilities (deferred revenue) | 12,100 | Services backlog proxy; +2.4% current portion |

**Actionable:** The **$4.5B "reasonably possible" unrecognized tax benefit decrease** is the single largest explicitly quantified downside item in the entire filing set. Combined with a 14.7% effective rate versus a 21% statutory rate, **tax normalization is a live 2–5% EPS risk** that the market routinely underweights in a 30x-multiple stock.

---

## 10. Key Debates, Catalysts, and Risks

### Catalysts (near-term, dated)
1. **Q1 FY2024 earnings — imminent.** The quarter ended ~2023-12-30 and had **not been filed** as of 2024-01-31. This is the dominant binary event for any position established on this report. Consensus figures are **not** available in this dataset and must be sourced separately before sizing.
2. **FY24 buyback authorization** — the FY23 deceleration (–13.3%) needs to reverse for the EPS bridge to hold.
3. **Gross margin sustainability above 44%** — the single most important number. Any Services deceleration or hardware promotions compresses the only growing line.

### Structural positives
- ~**$51B net cash** and a well-laddered debt stack → asymmetric ability to keep buying back stock through a downturn.
- **–68 day CCC** and 106.7 DPO → suppliers, not Apple, finance the working capital.
- **44.1% and rising gross margin** in a declining-revenue year → genuine pricing/mix power, not volume.
- **29.1x interest coverage**, ROA of **27.5%**, ROIC ~**56%**.
- AOCI improvement (+$1.82B AFS swing) means the 2022 bond-portfolio wound is healing; a rate-cut cycle is an unrecognized book-value tailwind.

### Structural negatives / risks
1. **Revenue contraction with negative operating leverage.** Revenue –2.8%, opex +6.8%. Two consecutive years of opex growing faster than revenue (FY22 +17.0%, FY23 +6.8%).
2. **Buyback dependence for EPS.** Strip out the –3.1% share count and FY23 was an **earnings decline**, not growth. Buyback *dollars* fell 13.3%; if that continues, EPS growth goes negative.
3. **Thin equity base distortion.** $62.1B equity on $352.6B assets (17.6% equity ratio) means ROE (156%) is uninformative and any large charge hits book value disproportionately. BVPS is only **$4.00** — there is no book-value floor supporting the price.
4. **Tax normalization risk:** 14.7% → 21% would cut EPS ~7%; the $4.5B unrecognized-benefit disclosure is a specific, quantified trigger.
5. **SBC inflation:** +19.9% to $10.8B, with $18.6B unrecognized — comp cost is rising faster than revenue, and RSU withholding ($5.4B) is a real cash cost not in opex.
6. **Data staleness:** you are trading 4-month-old financials into an unreported holiday quarter.

### Valuation framework (no price data in the vendor feed — use as sensitivity)
FY2023 diluted EPS = **$6.13**. Each **$10 of share price ≈ 1.63 turns of FY23 P/E.** On a normalized (21% tax) FY23 EPS of ~$5.65, each $10 of price ≈ 1.77 turns.

| If share price is… | P/E on FY23 EPS ($6.13) | P/E on tax-normalized EPS (~$5.65) | FCF yield ($99.6B / mkt cap @15.55B sh) |
|---|---:|---:|---:|
| $150 | 24.5x | 26.5x | 4.27% |
| $170 | 27.7x | 30.1x | 3.77% |
| $185 | 30.2x | 32.7x | 3.46% |
| $200 | 32.6x | 35.4x | 3.20% |
| $225 | 36.7x | 39.8x | 2.85% |

Dividend yield at $185 ≈ **0.51%** (FY23 DPS $0.94); at $150 ≈ **0.63%**. Dividend is not a support mechanism at any plausible price — payout is only 15.5% of earnings and management clearly prefers buybacks.

---

## 11. Actionable Trade Takeaways

1. **Do not treat this as a growth stock on these fundamentals.** Revenue –2.8%, op income –4.3%, net income –2.8%. The only positive line is EPS (+0.3%), and it is 100% attributable to a 3.1% share-count reduction. Position sizing should reflect a mature cash-return compounder, not a growth name.
2. **The bull case rests on exactly two numbers: 44.1% gross margin and buyback re-acceleration.** Both are at risk (margin from Services mix/promotions; buyback from the FY23 –13.3% decline). Any Q1 FY24 print that shows either breaking should be treated as thesis-invalidating for a long.
3. **The balance sheet is a genuine, sizeable put.** ~$51B net cash + $110.5B annual OCF + only $9.9B of near-term maturities + 53% of term debt beyond 5 years = no financing risk in any plausible rate scenario. This caps downside versus levered peers but does **not** provide valuation support at 30x earnings.
4. **Quantify the tax tail explicitly in your model.** 14.7% effective rate, $4.5B "reasonably possible" unrecognized benefit reduction (~$0.28 EPS), and a 21% statutory rate. A 200bp rate normalization = ~2.4% EPS; full normalization = ~7%. In a 30x stock, that is a 2-turn P/E expansion you are not being paid for.
5. **Trade the event, not the filing.** Q1 FY24 results are pending and unrepresented in this dataset. Consider expressing views **after** the print rather than into it, or size positions so the event risk is tolerable — the FY23 10-K gives you a high-confidence baseline (margins, cash return, net cash) but zero visibility on the holiday quarter.
6. **Watch cash taxes, not just book taxes.** Cash taxes paid ($18,679M) exceeded book tax expense ($16,741M) by $1.94B. Cash conversion of earnings is slightly worse than the headline suggests.
7. **Insider signal is a blank.** With no insider data available, do not let a presumed "quiet insider tape" add confidence to a long. It is unmeasured.
8. **The negative working capital is an asset, not a red flag.** CCC of –68 days with a 0.99x current ratio is a hallmark of unmatched supplier power — do not screen AAPL out on liquidity.

---

## 12. Key Points Summary Table

| Category | Metric | Value | Trend / Read |
|---|---|---|---|
| **Data** | Latest filing | FY23 10-K, accepted 2023-11-03 | Q1 FY24 **not yet filed** as of 2024-01-31 |
| **Data** | Insider transactions | **UNAVAILABLE** | No signal measured — do not infer |
| **Scale** | Revenue (FY23) | $383,285M | **–2.8% YoY** |
| **Scale** | Net income (FY23) | $96,995M | –2.8% YoY |
| **Scale** | Diluted EPS (FY23) | $6.13 | **+0.3%** — only via buyback |
| **Profitability** | Gross margin | **44.1%** | +82bp YoY; +235bp over 2 yrs — record, expanding |
| **Profitability** | Operating margin | 29.8% | –45bp YoY |
| **Profitability** | Net margin | 25.3% | flat |
| **Profitability** | ROA | 27.5% | –80bp YoY |
| **Profitability** | ROE | 156% | Distorted by buybacks; not a quality read |
| **Profitability** | ROIC (equity+debt) | ~56% | Best-in-class |
| **Efficiency** | Opex growth | +6.8% | **vs revenue –2.8% → negative leverage** |
| **Efficiency** | Cash conversion cycle | **–67.8 days** | DPO 106.7 / DSO 28.1 / DIO 10.8 |
| **Efficiency** | Capex / revenue | 2.9% ($10,959M) | Asset-light |
| **Cash Flow** | Operating cash flow | $110,543M | **–9.5% YoY** |
| **Cash Flow** | Free cash flow | **$99,584M** | –10.6% YoY; 26.0% margin |
| **Cash Flow** | FCF / net income | 90.1% | Strong earnings quality |
| **Balance Sheet** | Total assets | $352,583M | Flat YoY |
| **Balance Sheet** | Cash + investments | ~$162,099M | +~$21B net cash to ~$51.0B |
| **Balance Sheet** | Gross debt | $111,088M | CP cut –40.0% (deleveraging) |
| **Balance Sheet** | Net cash | **~$51,010M** | Improving ~$21B YoY |
| **Balance Sheet** | Current ratio | 0.99x | Up from 0.88x; structurally fine |
| **Balance Sheet** | Debt / equity | 1.79x | Down from 2.36x |
| **Balance Sheet** | Equity ratio | 17.6% | Thin; BVPS $4.00 — no book floor |
| **Balance Sheet** | Debt due next 12M | $9,943M | vs $110.5B OCF — trivial |
| **Balance Sheet** | Debt due >5 years | $56,003M | 53% of term debt — no wall |
| **Capital Return** | Buybacks (FY23) | $77,550M | **–13.3% YoY — key vulnerability** |
| **Capital Return** | Dividends (FY23) | $15,025M | +1.2%; DPS $0.94; payout 15.5% |
| **Capital Return** | Total returned | **$92,575M** | **= 93.0% of FCF** |
| **Capital Return** | Diluted shares | ~15,823M | **–3.1% YoY** — the EPS engine |
| **Tax** | Effective rate | 14.7% | vs 21% statutory; ~7% EPS risk at full normalization |
| **Tax** | Unrecognized benefit, possible decrease | **$4,500M** | **≈$0.28 EPS headwind** |
| **Equity** | Shares outstanding | 15,550,061,000 (9/30/23) | 15,552,752,000 (10/20/23) |
| **Equity** | Public float (2023-03-31) | $2.591T | Mega-cap, deep liquidity |
| **Valuation** | Rule of thumb | Each $10 of price ≈ 1.63x FY23 P/E | At $185 → ~30.2x FY23 EPS |
| **Verdict** | Profile | Elite-margin, fortress-balance-sheet, **ex-growth** cash-return compounder | Long thesis = margin + buyback; not revenue |
| **Verdict** | Principal risk | EPS growth is manufactured by float reduction that is decelerating | Monitor buyback dollars and gross margin |

---

**Report prepared for AAPL on 2024-01-31.** All financial figures are sourced from SEC filings accepted on or before that date. Revenue is derived as Gross Profit + Cost of Goods and Services Sold because the vendor did not return a direct revenue tag. All ratios, growth rates, and derived metrics are calculated from the tool-supplied line items. Insider activity is unavailable from the vendor and is **not** estimated. No share price was supplied by the data vendor; valuation figures are presented as pure price sensitivity, not as market-derived multiples.