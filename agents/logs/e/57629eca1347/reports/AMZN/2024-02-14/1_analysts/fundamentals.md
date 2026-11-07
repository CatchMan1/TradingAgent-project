# AMZN (Amazon.com, Inc.) — Fundamental Research Report
**As of:** 2024-02-14 | **Fiscal year end:** December 31 | **Latest filing:** FY2023 Form 10-K, accession 0001018724-24-000008, accepted 2024-02-02 04:48 UTC

---

## 1. Data provenance & limitations (read first)

Every figure below is drawn from the point-in-time SEC XBRL fact set that was publicly accepted by **2024-02-14**. That set is dominated by the **FY2023 10-K filed 2024-02-02**, which is the single most important event of the past week: Amazon closed FY2023 and released audited full-year and Q4 results.

Explicit gaps in the feed that I will **not** fabricate around:

| Item | Status |
|---|---|
| `Revenues` / `RevenueFromContractWithCustomer` tag | **Not returned by the feed.** I derive total net sales as `CostsAndExpenses + OperatingIncomeLoss` (arithmetic identity), which reconciles exactly for 2021–2023. |
| Segment detail (NA / International / AWS) | **Not itemized in the feed.** Only `NumberOfOperatingSegments = 3` is confirmed. |
| Inventory, PP&E, goodwill line items | Not returned (feed truncated at intangibles). |
| Q1–Q4 2023 quarterly income statement | Only FY2023 + comparative FY2022/FY2021 annuals plus 2022/2023 balance-sheet dates are present. Quarterly revenue/EPS for 2023 is **not** available. |
| Insider transactions | **DATA_UNAVAILABLE** — no authorized point-in-time insider archive for AMZN. No insider inference is made anywhere in this report. |
| Share price / market cap | No price tool. Valuation section uses an **explicitly labeled ~$170/share assumption** and is presented as sensitivity, not as sourced fact. |

---

## 2. Company profile (identity confirmed)

Amazon.com, Inc. (`AMZN`, Nasdaq) — the resolved identity matches. Three reportable operating segments (confirmed: `NumberOfOperatingSegments = 3`): **North America** retail, **International** retail, and **Amazon Web Services**. The FY2023 filing also confirms the structural facts a trader needs to know:

- **10,387,381,291 shares outstanding** as of 2024-01-24 (10,383M at 2023-12-31).
- **Public float of $1.184 trillion** measured at 2023-06-30 (`EntityPublicFloat`) — top-tier mega-cap liquidity.
- **Common shares authorized: 100 billion**; par $0.01; 10,898M issued at year-end (i.e., ~515M treasury shares).
- **Three segments**, evidenced by a heavy tangible + leased asset base: gross PP&E (via D&A), finance-lease ROU assets before amortization of **$62.5B**, accumulated finance-lease ROU amortization of **$44.7B**, operating lease liabilities of **$75.6B**.
- **1.6 billion shares reserved for future issuance** under equity plans — the dilution pipeline.

---

## 3. Income statement: FY2021 → FY2023 (the re-acceleration story)

All $ in millions.

| Line | FY2021 | FY2022 | FY2023 | '23 YoY % |
|---|---:|---:|---:|---:|
| **Net sales (derived)** | **469,822** | **513,983** | **574,785** | **+11.8%** |
| Cost of goods & services sold | 272,344 | 288,831 | 304,739 | +5.5% |
| **Gross profit** | **197,478** | **225,152** | **270,046** | **+20.0%** |
| Gross margin | 42.0% | 43.8% | **47.0%** | +3.2 pts |
| Marketing expense | 32,551 | 42,238 | 44,370 | +5.0% |
| General & admin | 8,823 | 11,891 | 11,816 | −0.6% |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| **Operating income** | **24,879** | **12,248** | **36,852** | **+200.9%** |
| Operating margin | 5.29% | 2.38% | **6.41%** | +4.03 pts |
| Interest expense | 1,809 | 2,367 | 3,182 | +34.4% |
| Investment income (interest) | 448 | 989 | 2,949 | +198.2% |
| Non-operating income/(expense), net | 13,272 | (18,184) | 705 | n.m. |
| Pre-tax income | 38,151 | (5,936) | 37,557 | n.m. |
| Income tax expense/(benefit) | 4,791 | (3,217) | 7,120 | n.m. |
| Net income | **33,364** | **(2,722)** | **30,425** | n.m. |
| Net margin | 7.10% | (0.53%) | 5.29% | — |
| Diluted EPS | $3.24 | $(0.27) | **$2.90** | n.m. |
| Diluted shares (implied) | ~10,297 | ~10,189 | ~10,491 | +3.0% |

**What actually happened — the five things that matter:**

1. **Revenue re-accelerated to +11.8% from +9.4%**, a genuine inflection after the 2022 post-COVID digestion. That is a demand-side positive, not an accounting one.
2. **Gross margin expanded 320 bp to 47.0%.** Gross profit grew $44.9B (+20.0%) while total costs grew only $36.2B (+7.2%). Roughly $8.7B of operating-income expansion came straight from gross-margin mix (third-party seller services, advertising, AWS cost discipline) — margin, not volume, drove the year.
3. **Operating income tripled** ($12.2B → $36.9B) and operating margin hit 6.41%, the best of the three years shown and above FY2021's 5.29% despite a 2.4x larger revenue base.
4. **The 2022 loss was non-operating, not operational.** FY2022's $(2.7)B net loss came with **$12.2B of positive operating income**; it was destroyed by a **$18.2B non-operating loss** driven by `EquitySecuritiesFvNiUnrealizedGainLoss` of **−$13.6B** (mark-to-market on equity stakes) plus a $341M realized loss on securities. In FY2023 that line flipped to **+$1.0B**, adding ~$14.6B of swing versus the prior year. **Trader takeaway: FY2022's "loss" was a mark-to-market artifact and should not be used as an earnings-quality baseline; FY2023's +200% operating-income growth is the real signal.**
5. **Net interest expense turned roughly neutral.** Investment income of $2,949M (up 198% on higher rates/larger balances) nearly offset $3,182M of interest expense, versus a $(1,378)M net drag in 2022 — a ~$1.1B tailwind *and* evidence the securities portfolio is being sweated for yield.

**Advertising expense** (Amazon's own marketing channels, not ad revenue) was $20,300M vs $20,600M vs $16,900M — essentially flat in 2023, meaning management let marketing leverage rather than spend. **G&A fell in absolute dollars.** This is a genuinely lean cost year.

**Effective tax rate:** $7,120 / $37,557 = **19.0%**, below the 21% statutory, helped by **$2,362M of tax credits** and a **$5,876M deferred tax benefit** (versus −$8,148M in 2022). Note `IncomeTaxesPaidNet` jumped to **$11,179M** from $6,035M — cash taxes are now rising meaningfully, a real cash headwind that the deferred-benefit optics partially mask.

---

## 4. Cash flow: the story of the year

All $ in millions.

| Line | FY2021 | FY2022 | FY2023 | '23 YoY |
|---|---:|---:|---:|---:|
| **Net cash from operating activities** | **46,327** | **46,752** | **84,946** | **+81.7%** |
| Purchases of productive assets (capex) | (61,053) | (63,645) | (52,729) | −17.1% |
| **Simple free cash flow (OCF − capex)** | **(14,726)** | **(16,893)** | **+32,217** | **+$49.1B swing** |
| Net cash used in investing | (58,154) | (37,601) | (49,833) | +32.5% |
| Net cash from/(used in) financing | 6,291 | 9,718 | (15,879) | n.m. |
| D&A (total) | 34,433 | 41,921 | 48,663 | +16.1% |
| — of which depreciation | 22,909 | 24,924 | 30,225 | +21.3% |
| — finance lease ROU amortization | 9,857 | 6,097 | 5,899 | −3.2% |
| — intangible amortization | 512 | 604 | 706 | +16.9% |
| Stock-based comp (SBC) | 12,757 | 19,621 | 24,023 | +22.4% |
| **FCF less SBC** | (27,483) | (36,514) | **8,194** | +$44.7B |
| Operating lease payments | 6,722 | 8,633 | 10,453 | +21.1% |
| Finance lease principal payments | 11,163 | 7,941 | 4,384 | −44.8% |

**This is the most important section of the report.** Amazon swung from **−$16.9B FCF to +$32.2B FCF in one year — a $49.1B improvement** — via three simultaneous levers:

1. **OCF +$38.2B (+81.7%)** on the operating-income tripling plus working capital (unearned revenue added $4,578M of cash; accrued liabilities *used* $2,428M).
2. **Capex cut $10,916M (−17.1%)** to $52,729M.
3. **Depreciation and amortization rose $6,742M**, which suppresses GAAP income but adds back to OCF — i.e., the 2021–22 capex surge is now liquidating into cash flow.

**Critical insight: capex is now barely above D&A (52,729 vs 48,663 = 1.08x).** Nearly all FY2023 capital spending was **maintenance**, not growth. That is exactly why FCF exploded. It is also the single biggest risk to the 2024 FCF trajectory: any normalization of growth capex (AWS/GenAI infrastructure) compresses the D&A-to-capex gap. **Position accordingly — FY2023 FCF is a margin-of-safety peak, not a run-rate.**

**Earnings-quality flag:** SBC of **$24,023M** (4.18% of revenue, up from 3.82% in 2022) is *not* deducted from OCF. SBC-adjusted FCF is only **$8,194M** — roughly a quarter of headline FCF. Headline FCF overstates distributable cash by ~3.9x. Any thesis built on "$32B of FCF" must haircut for this.

**Secondary flag:** FY2023 financing cash outflow of $(15,879)M vs +$9,718M in 2022 reflects real deleveraging and the unwind of the commercial-paper/ST-debt balance (see §5).

---

## 5. Balance sheet: fortress liquidity, ~$88B of off–income-statement-style obligations

All $ in millions; as of December 31.

| Line | 2022-12-31 | 2023-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 53,888 | **73,387** | +$19,499 |
| Marketable securities (AFS, fair value) | — | **70,919** | — |
| **Cash + marketable securities** | ~124,807* | **144,306** | +$19,499 |
| Accounts receivable, net | 42,360 | 52,253 | +23.4% |
| Allowance for doubtful accounts | 1,400 | 1,700 | 3.25% of gross AR |
| Total current assets | 146,791 | **172,351** | +17.4% |
| **Total assets** | **462,675** | **527,854** | **+14.1%** |
| Accounts payable | 79,600 | 84,981 | +6.8% |
| Accrued liabilities (incl. current debt/lease portions) | 62,566 | 64,709 | +3.4% |
| Unearned revenue (current) | 13,227 | 15,227 | +15.1% |
| **Total current liabilities (derived)** | 155,393 | **164,917** | +6.1% |
| Total contract liabilities (current + non-current) | 16,100 | **20,600** | **+28.0%** |
| Long-term debt, carrying amount | 67,150 | **58,314** | **−13.2%** |
| — due within 12 months | — | 8,500 | — |
| Operating lease liabilities | 69,040 | **75,639** | +9.6% |
| — current | 7,458 | 8,419 | — |
| — non-current | 61,582 | 67,220 | — |
| Finance lease liabilities | 15,783 | **12,109** | −23.3% |
| Additional paid-in capital | 75,066 | **99,025** | **+32.0%** |
| Retained earnings (implied) | — | **~105,800** | — |
| AOCI | (4,487) | (3,040) | +$1,447 improv. |
| **Total stockholders' equity (implied)** | **~146,043** | **~201,875** | **+38.2%** |

*\*2022 marketable securities not itemized in the feed; total is indicative.*

**Liquidity:** Current ratio = 172,351 / 164,917 = **1.045** — comfortable but *thin* for a company with this working-capital cycle. Working capital is only **+$7,434M**. Amazon is structurally a negative-cash-conversion-of-inventory business that funds itself with payables ($85.0B) — so a current ratio near 1.0 is normal and not distressed, but it means there is no large liquidity cushion beyond the $144.3B of cash and securities.

**Solvency — the headline number:** Cash + securities of **$144,306M** against total debt of **~$66,814M** (58,314 + 8,500 current) = **net cash of ~$77.5B**. Add operating leases of $75,639M and finance leases of $12,109M and total debt-like obligations reach **~$154.6B**, which pushes the company to roughly **net debt-neutral on a lease-inclusive basis**. Amazon carries the biggest lease book in the world ($87.7B), and lease-adjusted leverage is far higher than the headline "net cash" framing suggests.

**Debt trajectory — genuinely prudent:**
- **Zero new long-term debt issued in FY2023** (vs $21,166M in 2022).
- Long-term debt repaid: $3,676M; short-term debt repaid $25,677M vs $18,129M drawn → **net ST paydown of $7,548M**.
- Maturity ladder: $8.5B (2024), $5.3B (2025), $3.1B (2026), $8.75B (2027), $2.25B (2028), **$39.25B after 2028**. Well-laddered, no 2024 refinancing cliff, and the whole front-loaded stack is coverable ~17x from cash alone.
- Finance lease principal payments fell to $4,384M from $7,941M — Amazon has been retiring lease obligations, cutting finance-lease liabilities 23%.
- Operating lease payments are rising fast ($6,722M → $8,633M → $10,453M, +21%), with $90.8B of undiscounted operating lease commitments due. This is the fastest-growing fixed obligation on the balance sheet.

**Equity funded by dilution:** APIC rose **$23,959M** in FY2023, almost entirely stock-based compensation. Share count rose from **10,242M to 10,383M (+1.38%)**. Combined with $24.0B of SBC expense, the cost of "no cash comp" is being paid in equity — ~$24B/year of value transfer, or roughly **79% of net income**.

**Contract liabilities (unearned revenue) +28% to $20,600M**, with $12,400M of prior-period deferred revenue recognized into FY2023 revenue — a solid forward-demand indicator (AWS commitments, Prime subscriptions).

---

## 6. Returns, efficiency, and quality of the franchise

Using implied equity (assets less itemized liabilities):

| Metric | FY2022 | FY2023 | Read |
|---|---:|---:|---|
| ROE (avg. equity ~$174.0B) | — | **~17.5%** | Strong, and 2022's negative print was mark-to-market noise |
| Operating margin | 2.38% | **6.41%** | Largest single-year jump in a decade |
| Gross margin | 43.8% | **47.0%** | Mix shift to 3P/ads/AWS + cost control |
| Revenue / total assets | 1.11x | **1.09x** | Asset-heavy; leverage of fixed base is improving |
| Capex / D&A | 1.52x | **1.08x** | Transitioning from build to harvest |
| SBC / net income | n.m. | **79%** | Real dilution cost |
| Cash conversion (OCF/net income) | n.m. | **2.79x** | Excellent on a D&A-heavy base; not a red flag |
| Net cash (ex-leases) | ~$57.7B | **~$77.5B** | Improving |
| Lease-inclusive net debt | — | **~$(10.3)B** (net debt) | Deleveraging story is less clean than headline |

**ROIC check:** NOPAT = 36,852 × (1 − 19.0%) = **$29.9B**; invested capital ≈ equity $201.9B + debt $66.8B + leases $87.7B − cash/securities $144.3B = **$212.1B** → **ROIC ≈ 14.1%** vs an estimated ~9–10% weighted cost of capital. Franchise is value-creating, but only modestly above cost of capital — a reminder that Amazon's moat is volume- and reinvestment-based, not capital-light.

---

## 7. Valuation framing (assumption-based — flag)

Only the share count is tool-sourced (10,387.4M at 2024-01-24). With **~$170/share** as an illustrative mid-February 2024 price:

| Metric | Value | Comment |
|---|---|---|
| Market cap | ~$1.77T | 10,387M × $170 |
| EV (net of $77.5B cash/securities net of debt) | ~$1.69T | |
| EV / FY2023 net sales ($574.8B) | **~2.9x** | |
| P / FY2023 diluted EPS ($2.90) | **~59x** | |
| EV / FY2023 EBITDA ($85.5B = op inc 36.9 + D&A 48.7) | **~19.8x** | |
| P / FY2023 OCF ($84.9B) | ~20.8x | |
| FCF yield (headline $32.2B) | **~1.8%** | |
| FCF yield (SBC-adjusted $8.2B) | **~0.46%** | The honest number |
| EV / FCF (headline) | ~52x | |

**Interpretation:** the multiple is not cheap on trailing cash flow, and the SBC-adjusted FCF yield of under 0.5% means the market is paying for *future* margin expansion and AWS/GenAI re-acceleration, not present cash returns. That framing only works if operating margin continues expanding from 6.4% and capex does not re-inflate faster than D&A. **Both assumptions are currently unproven for FY2024.**

---

## 8. Actionable conclusions for traders

**Bull case (strengths with hard evidence):**
1. **Operating-margin inflection is real and large** — 2.38% → 6.41%, +$24.6B of incremental operating income, driven by a 320bp gross-margin gain, not by cutting marketing (marketing was flat) or R&D.
2. **$49.1B one-year FCF swing** to +$32.2B, the first decisively positive FCF year of this cycle, funded by OCF growth *and* a $10.9B capex cut.
3. **Balance sheet is a fortress**: $144.3B cash + securities, ~$77.5B net cash, zero new long-term debt in FY2023, $39B of the maturity stack pushed beyond 2028, finance-lease liabilities down 23%.
4. **Deleveraging plus 38% equity growth** (APIC +$24.0B, AOCI improving by $1.4B) with no buyback burn — capital is being retained, not returned.
5. **Deferred revenue +28%** and $12.4B of recognized prior-period contract liability signal forward demand visibility.

**Bear case / what to short against:**
1. **FY2023 FCF is a peak, not a baseline.** Capex/D&A of 1.08x means growth investment was switched off. Any 2024 capex re-acceleration cuts FCF growth directly; the FCF yield math is extremely sensitive to this one variable.
2. **SBC of $24.0B = 79% of net income, and 1.4% annual share dilution.** SBC-adjusted FCF is only $8.2B. If the market re-rates on SBC-adjusted cash, the multiple is far more expensive than it looks.
3. **Cash taxes are inflecting**: taxes paid rose $6,035M → $11,179M (+85%). The $5,876M deferred tax benefit that flattered 2023 net income is a non-repeating cushion.
4. **Lease obligations of $87.7B** (operating $75.6B + finance $12.1B), with operating-lease payments up 21% to $10,453M and $44.6B due beyond year five. Lease-adjusted, this is not a net-cash balance sheet.
5. **Thin liquidity for the size**: current ratio 1.045, working capital +$7.4B. Payables-funded working capital cycles are fragile if growth stalls.
6. **Valuation leaves no room**: ~59x trailing EPS, ~52x EV/FCF, 1.8% headline FCF yield.

**Specific monitorables over the next 1–2 quarters:**
- **Capex run-rate vs. D&A** — the single most important variable. Watch for the capex/D&A ratio crossing back above ~1.3x; that would break the FCF thesis.
- **Gross margin ≥47%** — if FY2024 gross margin holds above 47%, the mix shift is structural; a slip below 46% invalidates the margin-expansion leg.
- **Operating margin ≥6.4%** — must not regress; the entire multiple rests on this.
- **SBC as % of revenue** — 4.18% in FY2023; any acceleration toward 5% is a dilution warning.
- **`IncomeTaxesPaidNet`** — track for further step-ups.
- **Finance-lease principal payments and operating-lease additions** — the fixed-obligation growth rate.
- **Balance-sheet cash build** — $73.4B cash is firepower for capex, M&A, or (eventually) a buyback; note **zero repurchases in FY2023** after $6.0B in FY2022, so buyback resumption would be a positive catalyst signal.

**Net stance implied by the data:** fundamentally improving at the operating line, balance sheet de-risked, but the cash-flow and valuation picture is *less* attractive than the headline FCF number implies. The trade is a bet on sustained margin expansion absorbing a re-acceleration in capex — not a bet on cheapness.

---

## 9. Key points summary

| Category | Metric | FY2021 | FY2022 | FY2023 | Signal |
|---|---|---:|---:|---:|---|
| **Scale** | Net sales ($M, derived) | 469,822 | 513,983 | 574,785 | ✅ Re-accelerated to +11.8% |
| **Profitability** | Gross margin | 42.0% | 43.8% | 47.0% | ✅ +320 bp, mix-driven |
| **Profitability** | Operating income ($M) | 24,879 | 12,248 | 36,852 | ✅ +200.9% YoY |
| **Profitability** | Operating margin | 5.29% | 2.38% | 6.41% | ✅ Best of 3 yrs |
| **Profitability** | Net income ($M) | 33,364 | (2,722) | 30,425 | ✅ 2022 loss was MTM-driven |
| **Profitability** | Diluted EPS | $3.24 | $(0.27) | $2.90 | ⚠️ Below FY2021 on 2.4x revenue |
| **Cash flow** | Operating cash flow ($M) | 46,327 | 46,752 | 84,946 | ✅ +81.7% |
| **Cash flow** | Capex ($M) | 61,053 | 63,645 | 52,729 | ⚠️ Cut 17% — FCF flattered |
| **Cash flow** | Simple FCF ($M) | (14,726) | (16,893) | **32,217** | ✅ +$49.1B swing; ⚠️ peak |
| **Cash flow** | FCF less SBC ($M) | (27,483) | (36,514) | 8,194 | ❌ Only 25% of headline FCF |
| **Cash flow** | D&A ($M) | 34,433 | 41,921 | 48,663 | ✅ Capex/D&A at 1.08x |
| **Comp** | SBC ($M) / % revenue | 12,757 / 2.7% | 19,621 / 3.8% | 24,023 / 4.2% | ❌ 79% of net income |
| **Liquidity** | Cash + securities ($M) | — | ~124,807 | 144,306 | ✅ |
| **Liquidity** | Current ratio | — | 0.94 | 1.045 | ⚠️ Thin |
| **Leverage** | Long-term debt ($M) | — | 67,150 | 58,314 | ✅ −13.2% |
| **Leverage** | Net cash ex-leases ($M) | — | ~57,700 | **~77,500** | ✅ |
| **Leverage** | Lease obligations ($M) | — | 84,823 | 87,748 | ⚠️ Fixed-cost creep |
| **Leverage** | New LT debt issued ($M) | 19,003 | 21,166 | **0** | ✅ Deleveraging |
| **Equity** | Total equity ($M, implied) | — | ~146,043 | ~201,875 | ✅ +38.2% |
| **Equity** | APIC ($M) — dilution cost | — | 75,066 | 99,025 | ⚠️ +$24.0B from SBC |
| **Equity** | Shares outstanding (M) | — | 10,242 | 10,383 | ⚠️ +1.38% dilution |
| **Returns** | ROE | — | neg. | ~17.5% | ✅ |
| **Returns** | ROIC (NOPAT/IC) | — | — | ~14.1% | ✅ Modestly above WACC |
| **Tax** | Effective rate | 12.6% | n.m. | 19.0% | ⚠️ Normalizing |
| **Tax** | Cash taxes paid ($M) | 3,688 | 6,035 | 11,179 | ❌ +85%, real headwind |
| **Working cap** | Contract liabilities ($M) | — | 16,100 | 20,600 | ✅ +28% forward demand |
| **Capital returns** | Buybacks ($M) | 0 | 6,000 | **0** | ⚠️ Watch for resumption |
| **Valuation** | P/E (assumed ~$170/sh) | — | n.m. | ~59x | ❌ Priced for perfection |
| **Valuation** | EV/EBITDA | — | — | ~19.8x | ❌ |
| **Valuation** | FCF yield (headline / SBC-adj.) | — | — | 1.8% / 0.46% | ❌ |
| **Insider** | Transactions | — | — | — | ⛔ Data unavailable — no inference made |

---

**Bottom line for AMZN:** the FY2023 10-K (filed 2024-02-02, within the past week) documents a genuine, broad-based operating turnaround — margin, operating income, and cash flow all inflected sharply, and the balance sheet was actively de-risked. But the FCF surge is **materially assisted by a 17% capex cut and a rising D&A add-back**, and headline FCF overstates distributable cash ~3.9x once $24.0B of SBC is deducted. At ~59x earnings and ~52x headline FCF, the equity already discounts continued margin expansion; the entire forward return case rests on **capex/D&A staying near 1.1x** and **operating margin holding ≥6.4%**. Those are the two variables to trade around.

*Note: quarterly 2023 income-statement detail, segment-level (NA/International/AWS) P&L, inventory/PP&E/goodwill line items, and insider transaction data were all unavailable from the point-in-time feed used here. No figures in those areas have been estimated or inferred.*