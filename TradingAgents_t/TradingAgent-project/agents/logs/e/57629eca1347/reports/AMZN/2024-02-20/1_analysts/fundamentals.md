# AMZN — Fundamental Research Report
**Prepared:** 2024-02-20 | **Instrument:** AMZN (Amazon.com, Inc.) | **Basis:** Point-in-time SEC/XBRL facts accepted by EDGAR on/before 2024-02-20 (latest filing: FY2023 Form 10-K, acc. 0001018724-24-000008, filed 2024-02-02 04:48 UTC)

---

## 1. Data Provenance & Method

- The most recent financial disclosure universe available is the **FY2023 10-K** (period ended 2023-12-31), accepted 2024-02-02. All annual figures below are **reported** unless marked *derived*.
- The vendor returned **annual (10-K) statements plus Q3-FY23 10-Q cash-flow items**; no quarterly income-statement/balance-sheet XBRL rows for 2023 interim periods were returned, so sequential (Q4-only) analysis is **not possible** from this dataset.
- **Revenue was not returned as its own tag**; it is *derived* from the identity `Revenue = CostsAndExpenses + OperatingIncomeLoss`. Cross-check: 2021 → 444,943 + 24,879 = **469,822**; 2022 → 501,735 + 12,248 = **513,983**; 2023 → 537,933 + 36,852 = **574,785**. These reconcile to Amazon's reported revenue in all three years, so the derivation is reliable.
- **Tags NOT returned (truncated extract):** revenue-by-segment/AWS, inventory, PP&E (gross/net), goodwill, total liabilities, and total stockholders' equity. I do **not** substitute estimates from memory for these; they are flagged as gaps in §9.
- **Insider transactions: DATA UNAVAILABLE.** The data package has no authorized, point-in-time insider-transaction archive for AMZN by 2024-02-20. No insider buying/selling assessment is possible and none is inferred.

---

## 2. Company Profile & Segment Frame

Amazon.com, Inc. reports **3 operating segments** (`NumberOfOperatingSegments = 3`): **North America**, **International**, and **Amazon Web Services (AWS)**. The business mix spans: (a) online and physical retail plus third-party seller services (1P/3P marketplace, fulfillment), (b) advertising (a high-margin line reported within segment results), (c) subscription services (Prime), and (d) AWS cloud compute/storage/database/AI infrastructure — the principal profit engine.

Structural read-through from the FY2023 statements:
- **Large-scale, low-margin, capital-intensive model:** revenue $574.8B against a cost base of $537.9B (93.6% of revenue). Nothing in the financials has changed that basic architecture.
- **Scale metrics:** total assets $527.9B; public float $1.184T as of 2023-06-30 (`EntityPublicFloat`); 10,387,381,291 shares outstanding as of 2024-01-24.
- **Three-segment disclosure makes segment margin data essential**: because AWS carries a structurally higher margin than retail, group margin expansion can come from mix shift rather than retail profitability. Segment revenue/margin tags were not returned (see §9) — this is the single biggest analytical gap for a trader.

---

## 3. Income Statement — Three-Year History (USD millions)

| Line item | FY2021 | FY2022 | FY2023 | FY23 YoY |
|---|---:|---:|---:|---:|
| Revenue (*derived*) | 469,822 | 513,983 | 574,785 | **+11.8%** |
| Cost of goods & services sold | 272,344 | 288,831 | 304,739 | +5.5% |
| **Gross profit** (*derived*) | 197,478 | 225,152 | 270,046 | +20.0% |
| **Gross margin** | 42.03% | 43.81% | **46.98%** | +317 bps |
| Marketing expense | 32,551 | 42,238 | 44,370 | +5.1% |
| G&A expense | 8,823 | 11,891 | 11,816 | -0.6% |
| Total costs & expenses | 444,943 | 501,735 | 537,933 | +7.2% |
| **Operating income** | 24,879 | 12,248 | **36,852** | +200.9% |
| **Operating margin** | 5.30% | 2.38% | **6.41%** | +403 bps |
| Interest expense | 1,809 | 2,367 | 3,182 | +34.4% |
| Interest income | 448 | 989 | 2,949 | +198.2% |
| Non-operating income/(expense), net | +13,272 | (18,184) | +705 | n.m. |
| Pre-tax income (incl. equity-method) | 38,151 | (5,936) | 37,557 | n.m. |
| Provision/(benefit) for income taxes | 4,791 | (3,217) | 7,120 | n.m. |
| **Net income** | 33,364 | **(2,722)** | **30,425** | n.m. |
| **Diluted EPS** | $3.24 | $(0.27) | **$2.90** | n.m. |
| Basic EPS | $3.30 | $(0.27) | $2.95 | n.m. |
| Effective tax rate (*derived*) | 12.6% | n.m. (benefit) | **19.0%** | +640 bps |

### 3.1 What actually drove the FY2023 inflection
1. **Cost-to-serve leverage is the whole story.** Revenue +11.8% while COGS rose only +5.5% → **gross margin +317 bps**. Total costs grew +7.2% vs revenue +11.8%, delivering **+403 bps of operating margin** and a **tripling of operating income** ($12.2B → $36.9B). This is the signature of fulfillment-network regionalization, headcount discipline, and AWS cost optimization cycling through.
2. **2022 was a genuine trough, not a trend.** FY2022 operating income collapsed to $12.2B (2.38%) and net income was **negative $(2.7)B**, driven by a **$(18.2)B non-operating loss** — of which **$(13.6)B was unrealized loss on equity securities at fair value** (`EquitySecuritiesFvNiUnrealizedGainLoss`). FY2021's +$11.6B equity gain was the mirror image (+$13.3B non-operating). **These mark-to-market swings are now essentially gone: FY2023 non-operating was only +$0.7B.**
3. **Earnings quality is materially better than the headline comparison suggests.** FY2021 net income of $33.4B (EPS $3.24) was inflated by ~$11.6B of pre-tax investment gains. FY2023 net income of $30.4B (EPS $2.90) is **almost entirely operating**, with operating income of $36.9B vs $24.9B in 2021. On an operating basis, FY2023 EPS is a higher-quality $2.90 than FY2021's $3.24.
4. **Marketing and G&A are being held flat** (+5.1% and -0.6% YoY) despite double-digit revenue growth — deliberate expense discipline, not revenue-driven.

### 3.2 Cost structure & cash-vs-non-cash expense detail

| Item | FY2021 | FY2022 | FY2023 | % of FY23 rev |
|---|---:|---:|---:|---:|
| Share-based compensation | 12,757 | 19,621 | **24,023** | **4.18%** |
| D&A (total) | 34,433 | 41,921 | **48,663** | 8.47% |
| — Depreciation (PP&E & other) | 22,909 | 24,924 | 30,225 | 5.26% |
| — Finance-lease ROU amortization | 9,857 | 6,097 | 5,899 | 1.03% |
| — Intangible amortization | 512 | 604 | 706 | 0.12% |
| Advertising expense | 16,900 | 20,600 | 20,300 | 3.53% |
| Operating lease cost | 7,199 | 8,847 | 10,550 | 1.84% |
| Finance lease interest | 473 | 361 | 304 | 0.05% |

- **SBC of $24.0B (+22.4% YoY, 4.18% of revenue) is the key "hidden" expense.** It is legitimately excluded from cash flow but is real dilution-economics cost. The mitigating fact: share count grew only **+1.38%** (10,242M → 10,383M), meaning buyback-free offsetting via issuance timing; still, **~1.4%/yr structural dilution** should be applied against per-share growth math.
- **$18.3B of SBC not yet recognized** (`EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized` = $18.3B at 2023-12-31) — a multi-year forward drag already contracted.
- **Interest income ($2.95B) now nearly cancels interest expense ($3.18B)** — net interest cost of only ~$233M vs ~$1.38B in 2022. Higher rates are, on net, no longer a P&L headwind for AMZN's cash-rich balance sheet.

### 3.3 Tax
- Book tax $7.12B, **cash taxes paid $11.18B** (vs $6.04B in 2022, $3.69B in 2021) — cash taxes are rising faster than book tax.
- **Deferred tax expense was a $(5.88)B benefit**, meaning book income was *under*-taxed relative to cash. Sustainable ETR is drifting **up** (12.6% → ~19.0%), aided in FY2023 by $2.36B of tax credits and a $600M prior-year benefit. **Expect ETR normalization toward the low-20s to be an EPS headwind in FY2024** — a point traders frequently mis-model.
- Deferred tax assets gross rose to $50.6B, of which **IPR&D DTA jumped to $14.8B from $6.8B** — a marker of asset/intangible acquisitions rather than organic build.

---

## 4. Cash Flow — The Real Story of FY2023 (USD millions)

| Item | FY2021 | FY2022 | FY2023 |
|---|---:|---:|---:|
| **Operating cash flow** | 46,327 | 46,752 | **84,946** |
| Purchases of productive assets (capex) | (61,053) | (63,645) | **(52,729)** |
| **Free cash flow** (*derived*) | **(14,726)** | **(16,893)** | **+32,217** |
| Finance-lease principal payments | (11,163) | (7,941) | (4,384) |
| **Adj. FCF (incl. fin. lease principal)** (*derived*) | (25,889) | (24,834) | **+27,833** |
| Investing cash flow, net | (58,154) | (37,601) | (49,833) |
| Financing cash flow, net | +6,291 | +9,718 | **(15,879)** |
| FX effect on cash | (364) | (1,093) | +403 |
| **Net change in cash + restricted** | (5,900) | +17,776 | **+19,637** |
| Cash taxes paid | 3,688 | 6,035 | 11,179 |
| Operating lease payments | 6,722 | 8,633 | 10,453 |
| Share repurchases | 0 | 6,000 | **0** |

### 4.1 The single most important number in this dataset
**Free cash flow swung +$49.1B in one year** — from $(16.9)B to **+$32.2B** — through the *combination* of:
- **OCF +81.7%** ($46.8B → $84.9B), the operating-leverage effect, and
- **Capex -17.1%** ($63.6B → $52.7B), the investment cycle rolling off.

This is a **capital-allocation regime change**, not a one-line fluke. Two corroborating ratios:
- **Capex / D&A: 1.77x (2021) → 1.52x (2022) → 1.08x (2023).** Amazon is now investing ~in line with the depreciation of its existing asset base — the classic signature of a completed fulfillment overbuild.
- **Capex / revenue: 12.99% (2021) → 12.38% (2022) → 9.17% (2023).**
- **FCF / net income = 1.06x** — earnings are cash-backed, which was emphatically *not* true in 2021–22.

### 4.2 Financing behavior confirms the balance-sheet turn
- **Zero long-term debt issued in FY2023** (vs $21.2B in 2022, $19.0B in 2021).
- LT debt repaid $3.68B; net short-term debt **-$(7.55)B** (proceeds $18.1B vs repayments $25.7B).
- **Zero buybacks in FY2023** (vs $6.0B in 2022) — capacity is being rebuilt, not yet returned. This is the live catalyst for FY2024 capital-return optionality.
- Finance-lease principal payments down to $4.38B from $11.16B — less reliance on lease financing.

---

## 5. Balance Sheet — Position and Liquidity (USD millions)

| Item | 2021-12-31 | 2022-12-31 | 2023-12-31 | YoY |
|---|---:|---:|---:|---:|
| Total assets | 420,549 | 462,675 | **527,854** | +14.1% |
| Current assets | n/r | 146,791 | **172,351** | +17.4% |
| Cash & cash equivalents | n/r | 53,888 | **73,387** | +36.2% |
| Accounts receivable, net | n/r | 42,360 | **52,253** | +23.4% |
| Accounts payable | n/r | 79,600 | **84,981** | +6.8% |
| Accrued liabilities | n/r | 62,566 | **64,709** | +3.4% |
| Deferred revenue (total) | n/r | 16,100 | **20,606** | **+28.0%** |
| — current / non-current | n/r | 13,227 / 2,900 | 15,227 / 5,700 | +15.1% / +96.6% |
| Long-term debt | n/r | 67,150 | **58,314** | **-13.2%** |
| Operating lease liability | n/r | 69,040 | **75,639** | +9.6% |
| Finance lease liability | n/r | 15,783 | **12,109** | -23.3% |
| Additional paid-in capital | n/r | 75,066 | **99,025** | +31.9% |
| Accumulated OCI | n/r | (4,487) | **(3,040)** | improving |
| Shares outstanding (M) | n/r | 10,242 | **10,383** | +1.38% |
| Shares issued (M) | n/r | 10,757 | 10,898 | +1.31% |

**Key balance-sheet reads:**

1. **Liquidity is ample and improving.** Cash & equivalents **$73.4B (+36%)** against **$58.3B of long-term debt** → **net cash position**. Cash also grew faster than total assets. The vendor returned an available-for-sale debt-securities fair value of **$70.9B** (amortized cost $71.3B; $65.2B maturing within one year), but **this tag does not reconcile with reported current assets** ($172.4B = cash $73.4B + AR $52.3B + inventory + short-term investments, leaving only ~$46.7B for the latter two combined), nor with FY2023 securities purchases of only $1.49B. **Treat the $70.9B securities figure as a data-integrity caveat and underwrite liquidity on the $73.4B cash figure plus non-current investments.** Even on the conservative reading, AMZN is net cash.
2. **Deferred revenue +28% to $20.6B** — the closest available proxy to contracted forward demand (AWS commitments, Prime subscriptions). **$12.4B of FY2023 revenue was recognized from the prior-year deferred balance**, confirming a genuine, large backlog flowing into the P&L. This is a leading indicator that the revenue base is contractually supported, not purely transactional.
3. **Working capital remains a structural funder.** AP $85.0B and accrued liabilities $64.7B against AR of $52.3B → **supplier float continues to finance the model**.
   - **DSO (derived): 30.1 days (2022) → 33.2 days (2023)** — receivables +23.4% vs revenue +11.8%. A mild collection deceleration; watch, but the allowance for doubtful accounts rose only modestly ($1.4B → $1.7B, write-offs $1.3B → $1.6B), and AR growth is partly advertising/AWS receivables growing into a more profitable mix — not a red flag yet.
   - **DPO (derived): 100.6 days (2022) → 101.8 days (2023)** — stable, no stretching of suppliers.
4. **Lease obligations are the real leverage.** Operating leases ($75.6B) plus finance leases ($12.1B) = **$87.7B** — larger than reported debt. **Adjusted gross obligations ≈ $146B** (debt $58.3B + finance leases $12.1B + operating leases $75.6B). Any peer comparison on leverage must adjust for this.
5. **Dilution is contained but persistent:** shares outstanding +1.38%, funded through $24.0B of APIC build.

---

## 6. Contractual Obligations & Maturity Wall (as of 2023-12-31, USD millions)

| Obligation | Due ≤12m | Yr 2 | Yr 3 | Yr 4 | Yr 5 | >5 yr | **Total** |
|---|---:|---:|---:|---:|---:|---:|---:|
| Long-term debt principal | 8,500 | 5,286 | 3,146 | 8,750 | 2,250 | 39,250 | **67,182** |
| Finance lease payments | 2,292 | 1,471 | 1,369 | 1,123 | 1,022 | 6,829 | **14,106** |
| Operating lease payments | 11,229 | 9,922 | 9,156 | 8,321 | 7,546 | 44,603 | **90,777** |
| **Total contractual obligations** | **39,345** (all-in, incl. purchase/other) | 30,863 | 25,713 | 28,398 | 18,266 | 157,824 | **300,409** |

**Interpretation:** The maturity profile is **well-laddered and back-loaded** — only **$8.5B of debt matures in the next 12 months**, comfortably covered by $73.4B of cash and $84.9B of annual operating cash flow. The **heaviest single-year obligations are lease payments**, not debt principal. **$157.8B of the $300.4B total falls after year 5** — a long-dated, inflation-sensitive lease tail (data centers, fulfillment, offices, physical stores) rather than a refinancing cliff. **Refinancing risk is negligible; lease-cost inflation and renewal terms are the real long-tail liability.**

---

## 7. Quality-of-Earnings Scorecard

| Test | Result | Read |
|---|---|---|
| FCF / Net income | **1.06x** | Strong — earnings are cash-backed |
| OCF vs Net income gap | +$54.5B | Explained by D&A $48.7B + SBC $24.0B − deferred tax benefit $5.9B − WC drag |
| Non-operating share of pretax income | **1.9%** ($0.7B / $37.6B) | **Excellent** — vs 2021 (34.8%) and 2022 (loss-maker). Mark-to-market dependency eliminated |
| SBC / revenue | 4.18% (rising) | Negative but offset by low dilution (1.4%) |
| Capex / D&A | **1.08x** | Capital intensity normalizing — genuine FCF durability |
| Cash taxes vs book taxes | $11.2B vs $7.1B | Conservative; cash tax burden rising |
| Deferred revenue growth | +28% | Positive forward-demand signal |
| AR growth vs revenue growth | 23.4% vs 11.8% | Mild caution flag — watch collections |
| Goodwill/intangible impairment | **$0** (Q2-FY23) | No impairment overhang |

**Verdict: FY2023 earnings are of materially higher quality than FY2021's headline record.** The $30.4B net income / $2.90 diluted EPS is operating-derived; the FY2021 $33.4B / $3.24 EPS was ~$11.6B of Rivian-era equity gains. A trader comparing EPS across years without this adjustment will materially misjudge the improvement.

---

## 8. Actionable Insights for Traders

**Bullish evidence (all from reported figures):**
1. **Operating margin inflected +403 bps to 6.41%** — the highest in this three-year window and achieved on cost discipline (COGS +5.5%, G&A flat) rather than revenue mix alone.
2. **FCF turned positive at $32.2B from $(16.9)B — a +$49.1B annual swing.** FCF is the metric AMZN's multiple has historically been most sensitive to; this is the strongest single fundamental datapoint in the set.
3. **Capex/D&A fell to 1.08x** — the multi-year overbuild is over. Unless FY2024 capex re-accelerates for AI (not verifiable from this dataset — see §9), FCF has structural support.
4. **Net cash balance sheet:** $73.4B cash vs $58.3B LT debt; no LT debt issued in FY2023; $8.5B next-12m maturities immaterial.
5. **Net interest is now neutral** (−$0.23B vs −$1.38B), removing a rate-driven earnings drag.
6. **Deferred revenue +28%, with $12.4B recognized from backlog** — contracted revenue visibility improving.
7. **Buyback optionality:** $0 repurchased in FY2023 with $6.0B repurchased in 2022 — a $32B-FCF business with net cash and no repurchase program is a live capital-return catalyst.

**Bearish/caution evidence:**
1. **Revenue growth is decelerating on a two-year arc (+9.4% in FY2022, +11.8% in FY2023):** respectable, but well below the FY2021 pace — margin expansion, not growth, is doing the work. Multiple re-rating on margin alone has a ceiling.
2. **ETR normalization from 12.6% → 19.0% (likely low-20s) is an unmodeled EPS headwind** of roughly several percentage points to net income growth.
3. **SBC +22.4% to $24.0B (4.18% of revenue), with $18.3B unrecognized** — the "quality-adjusted" margin is ~217 bps lower than reported figure suggests, and SBC growth outpaces revenue growth.
4. **AR growing 23.4% vs revenue 11.8%** — DSO up to 33.2 days. Mild, but the first sign of channel/collection friction in this dataset.
5. **$87.7B of lease obligations**, with $157.8B of total obligations beyond year 5 — long-dated cost inflation exposure that does not appear on the debt line.
6. **2022's $(2.7)B net loss and $(13.6)B equity-mark loss demonstrate earnings volatility from the investment portfolio is not fully retired** — non-operating swings can still distort any given quarter.
7. **No buyback executed and no dividend** — capital return remains a promise, not a fact.

**What to monitor next (ranked by information value):**
1. **Capex trajectory in FY2024** — if capex/D&A pushes back above ~1.3x, the FCF inflection thesis weakens materially. This is the #1 swing factor.
2. **AWS segment revenue growth and operating margin** (not in this extract) — with group gross margin up 317 bps, confirmation that AWS (not just retail cost cuts) is driving it would validate durability.
3. **ETR in FY2024 filings** — a step-up beyond 20% is a direct EPS cut.
4. **Deferred revenue / backlog growth** — leading indicator of contracted demand; a deceleration below ~15% would flag that the +28% was a one-off.
5. **Any announcement of share repurchase authorization** — the clearest near-term per-share catalyst given $32.2B FCF and net cash.

**Positioning synthesis:** The fundamental setup as of 2024-02-20 is a **margin-and-cash-flow inflection story with a fortress balance sheet, priced off FY2023 results released 2024-02-02** (fully public and digested for ~3 weeks). The evidence supports a constructive fundamental stance, with the two genuine derailers being (a) capex re-acceleration for AI infrastructure and (b) tax-rate normalization — both of which are *cost* risks, not *demand* risks. Note: no valuation, price, or consensus data is available in this dataset, so no price-target or multiple-based conclusion can be drawn here.

---

## 9. Explicit Data Gaps (do not assume)

| Gap | Impact |
|---|---|
| **Insider transactions** — vendor returned DATA_UNAVAILABLE | No insider signal; absent, not neutral |
| **Quarterly P&L / balance sheet** (only annual 10-K facts returned; Q3-FY23 cash-flow items only) | No Q4-23 seasonality, no sequential margin trend, no holiday-quarter read |
| **Revenue-by-segment / AWS revenue & operating income** | Cannot decompose margin expansion into AWS mix vs retail cost cuts — the key analytical question |
| **Inventory, PP&E gross/net, goodwill, total liabilities, total stockholders' equity** (tags beyond extract truncation) | Cannot compute ROE, ROIC, inventory turns, or book value; asset-turnover (derived 1.09x) is a partial substitute |
| **Available-for-sale securities $70.9B tag** | Fails to reconcile with current assets and investing cash flow — treated as unreliable, liquidity underwritten on $73.4B cash |
| **Valuation / price / consensus** | No multiple, target, or sentiment analysis possible |

---

## 10. Key Points Summary

| Category | Metric | FY2021 | FY2022 | FY2023 | Signal |
|---|---|---:|---:|---:|---|
| **Scale** | Revenue (USD M, *derived*) | 469,822 | 513,983 | 574,785 | +11.8% YoY; growth solid but below FY21 pace |
| **Scale** | Revenue growth | — | +9.4% | +11.8% | Re-accelerating modestly |
| **Profitability** | Gross margin | 42.03% | 43.81% | **46.98%** | **+317 bps — cost-to-serve leverage** |
| **Profitability** | Operating income (USD M) | 24,879 | 12,248 | **36,852** | **Tripled off the FY22 trough** |
| **Profitability** | Operating margin | 5.30% | 2.38% | **6.41%** | **+403 bps — core thesis** |
| **Profitability** | Net income (USD M) | 33,364 | (2,722) | 30,425 | Recovered; now operating-driven |
| **Per share** | Diluted EPS | $3.24 | $(0.27) | $2.90 | Higher *quality* than FY21's $3.24 |
| **Per share** | Shares outstanding (M) | n/r | 10,242 | 10,383 | +1.38% dilution (SBC $24.0B) |
| **Cash generation** | Operating cash flow (USD M) | 46,327 | 46,752 | **84,946** | **+81.7%** |
| **Cash generation** | Capex (USD M) | (61,053) | (63,645) | (52,729) | **-17.1% — cycle rolling off** |
| **Cash generation** | **Free cash flow (USD M, *derived*)** | (14,726) | (16,893) | **+32,217** | **+$49.1B swing — single best datapoint** |
| **Cash generation** | Capex / D&A | 1.77x | 1.52x | **1.08x** | Capital intensity normalizing |
| **Cash generation** | FCF / Net income | n.m. | n.m. | **1.06x** | Earnings cash-backed |
| **Balance sheet** | Total assets (USD M) | 420,549 | 462,675 | 527,854 | +14.1% |
| **Balance sheet** | Cash & equivalents (USD M) | n/r | 53,888 | **73,387** | **+36.2%** |
| **Balance sheet** | Long-term debt (USD M) | n/r | 67,150 | **58,314** | **-13.2%; net cash position** |
| **Balance sheet** | Lease obligations (op. + fin., USD M) | n/r | 84,823 | **87,748** | Larger than reported debt |
| **Balance sheet** | Deferred revenue (USD M) | n/r | 16,100 | **20,606** | **+28% — backlog proxy** |
| **Working capital** | DSO (*derived*) | n/r | 30.1d | 33.2d | Mild caution |
| **Working capital** | DPO (*derived*) | n/r | 100.6d | 101.8d | Stable supplier float |
| **Obligations** | Debt due ≤12m (USD M) | — | — | 8,500 | Trivial vs $73.4B cash |
| **Obligations** | Total obligations (USD M) | — | — | 300,409 | $157.8B beyond year 5 |
| **Costs** | SBC (USD M / % rev) | 12,757 / 2.72% | 19,621 / 3.82% | **24,023 / 4.18%** | Rising; $18.3B unrecognized |
| **Costs** | Cash taxes paid (USD M) | 3,688 | 6,035 | 11,179 | Rising faster than book tax |
| **Costs** | Effective tax rate | 12.6% | n.m. | **19.0%** | **FY24 EPS headwind** |
| **Quality** | Non-operating income (USD M) | +13,272 | (18,184) | +705 | **Mark-to-market noise cleared** |
| **Capital return** | Share repurchases (USD M) | 0 | 6,000 | **0** | Buyback optionality unexercised |
| **Insider activity** | — | — | — | **UNAVAILABLE** | No signal; not neutral |
| **Segments** | Operating segments | 3 | 3 | 3 | NA / Int'l / AWS — segment detail not returned |

**Bottom line:** AMZN's FY2023 10-K documents a **confirmed fundamental inflection** — operating margin +403 bps, operating income tripled, OCF +82%, and FCF swinging from $(16.9)B to **+$32.2B** on a net-cash balance sheet with no refinancing cliff — while simultaneously revealing that the FY2021 profit record was inflated by investment marks and that FY2024 carries two identifiable cost headwinds (tax-rate normalization, $24.0B and rising SBC). The dataset's binding constraints for decision-making are the **absence of segment/AWS detail, the absence of quarterly P&L data, and the unavailability of insider transactions**; conclusions here should be treated as strongly evidenced on group-level cash generation and capital structure, and unverified on mix.