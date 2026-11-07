# AMZN — Fundamental Research Report
**Company:** Amazon.com, Inc. (`AMZN`)
**Report date:** 2026-09-10
**Primary source:** Point-in-time SEC XBRL facts (latest filing: Form 10-Q for the quarter ended 2026-06-30, accepted 2026-07-31)
**Insider transactions:** ❌ **Not available.** The data package has no authorized point-in-time insider-transaction archive for `AMZN`. No inference or fabrication should be drawn from this report regarding insider buying/selling.

---

## 1. Executive summary — the six things that matter

1. **Core operations are accelerating.** Q2-2026 revenue ≈ **$200.6B (+19.6% y/y)**, operating income **$27.46B (+43.2% y/y)**, operating margin **13.7%** vs 11.4% a year ago. H1-2026 operating income **$51.31B (+36.6% y/y)** on revenue **$382.1B (+18.2%)**. Margin expansion is happening *despite* depreciation rising ~31% y/y — a genuinely strong operating result.
2. **Reported EPS is massively distorted by a non-cash mark-up.** Q2-2026 net income of **$62.65B / $5.75 diluted EPS** includes **$50.49B** of pre-tax upward fair-value adjustments on equity securities without a readily determinable fair value (H1-2026: **$62.81B**). This is almost certainly an AI-related private-equity stake revaluation. **Do not annualize $5.75.** On a tax-adjusted ex-mark basis, Q2 EPS is closer to **$2.16 (~+29% y/y)** and H1 closer to **$4.09 (~+25% y/y)**.
3. **Amazon is now free-cash-flow negative.** Trailing-twelve-month operating cash flow was a record **$161.4B (+33% y/y)**, but capex was **$173.0B (+61% y/y)**, producing **FCF of –$11.6B** (vs +$13.5B a year earlier). Q2 alone: OCF $45.4B vs capex $54.2B.
4. **The balance sheet is being levered up fast to fund the AI build-out.** Total debt rose from **$68.8B (12/31/25) to $133.0B (6/30/26), +93% in six months**, plus $13.5B finance leases. TTM debt issuance: **$81.9B long-term + $20.8B short-term**, against only ~$26B of repayments. Total assets grew **+34%** to **$1.097T**.
5. **Liquidity is still a strength, but the cushion is thinning.** Cash $78.2B + available-for-sale securities $97.9B = **$176.1B** vs debt + finance leases of **$146.4B** → still **~$29.7B net cash**. Current ratio 1.03.
6. **Off-balance-sheet commitments are enormous and under-appreciated.** Contractual obligations of **$650.0B** at 6/30/26, including **$78.1B due within 12 months**, plus **$116.4B** of undiscounted operating-lease payments. This is the fixed-cost tail risk if AI demand growth decelerates.

**Net stance:** Fundamentally **constructive on the operating business**, but the equity is now a **capex/leverage/AI-return story** rather than a free-cash-flow story. Reported earnings quality is low (mark-to-model gains), and headline EPS beats should be discounted. The next hard catalyst is the Q3-2026 report (~late October 2026).

---

## 2. Company profile and segment structure

Amazon.com, Inc. (Seattle, WA; incorporated 1994) is a global technology and logistics conglomerate. The 10-Q confirms **three operating segments**:
- **North America** — online and physical retail, third-party marketplace, Prime subscriptions, advertising, logistics/fulfillment services.
- **International** — the same retail/marketplace/advertising model outside North America.
- **Amazon Web Services (AWS)** — cloud compute, storage, database, AI/ML infrastructure and services, plus a fast-growing custom-silicon business.

Revenue mix is not disclosed in the extract available, but the cost and margin trajectory (gross margin ~52%, operating margin 13.7%) is consistent with a business increasingly driven by high-margin AWS, advertising, and third-party marketplace fees rather than first-party retail. Management does not pay a dividend; no share-repurchase cash outflow appears in the cash-flow data.

*Caveat: the fundamentals tool returned SEC fact data rather than a narrative company profile. The paragraph above combines the confirmed 3-segment disclosure with standard public-company description; no segment-level revenue/profit table was available in this dataset.*

---

## 3. Income statement analysis

Revenue is derived as `CostsAndExpenses + OperatingIncomeLoss` (the raw Revenue tag was not returned by the feed); this is an exact accounting identity and reconciles cleanly.

### Q2-2026 vs Q2-2025

| Line ($M) | Q2-2026 | Q2-2025 | Δ |
|---|---:|---:|---:|
| Revenue | 200,606 | 167,702 | **+19.6%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% |
| Gross profit | 104,828 | 86,893 | +20.6% |
| Gross margin | **52.3%** | 51.8% | +0.5 pp |
| Marketing | 11,698 | 11,416 | +2.5% |
| G&A | 2,788 | 2,965 | –6.0% |
| D&A | 19,988 | 15,227 | **+31.3%** |
| SBC | 6,038 | 6,534 | –7.6% |
| Total costs & expenses | 173,145 | 148,531 | +16.6% |
| **Operating income** | **27,461** | **19,171** | **+43.2%** |
| Operating margin | **13.7%** | 11.4% | +2.3 pp |
| Interest expense | 1,314 | 516 | +154.7% |
| Interest income | 1,295 | 1,085 | +19.4% |
| Other/non-operating, net | 53,396 | 1,686 | n.m. |
| Pre-tax income | 80,857 | 20,857 | +287.7% |
| Tax | 18,199 | 2,678 | +579.6% |
| Effective tax rate | 22.5% | 12.8% | +9.7 pp |
| **Net income** | **62,647** | **18,164** | **+244.9%** |
| Diluted EPS | **$5.75** | $1.68 | +242.3% |
| Diluted shares | 10.895B | 10.812B | +0.8% |

### H1-2026 vs H1-2025

| Line ($M) | H1-2026 | H1-2025 | Δ |
|---|---:|---:|---:|
| Revenue | 382,125 | 323,369 | **+18.2%** |
| Gross profit | 198,884 | 165,584 | +20.1% |
| Gross margin | 52.0% | 51.2% | +0.8 pp |
| D&A | 38,933 | 29,489 | +32.0% |
| SBC | 10,070 | 10,223 | –1.5% |
| **Operating income** | **51,313** | **37,576** | **+36.6%** |
| Operating margin | **13.4%** | 11.6% | +1.8 pp |
| Interest expense | 2,114 | 1,057 | +100.0% |
| Non-operating income | 69,378 | 4,960 | n.m. |
| Pre-tax income | 120,691 | 42,536 | +183.7% |
| Tax (effective rate) | 27,759 (23.0%) | 7,231 (17.0%) | |
| **Net income** | **92,902** | **35,291** | **+163.2%** |
| Diluted EPS | **$8.53** | $3.27 | +160.9% |

**Q1-2026 (derived):** revenue $181.5B (+16.6% y/y), operating income $23.85B (13.1% margin). **Q2 accelerated sequentially and year-over-year** — the strongest operating print in the dataset.

### Key read-throughs
- **Operating leverage is real.** Revenue +19.6% against total cost growth of +16.6% in Q2. Marketing fell to 5.8% of revenue (from 6.8%) and G&A to 1.4% (from 1.8%); SBC fell in absolute dollars. Amazon is getting more efficient on opex even as it spends aggressively on infrastructure.
- **Depreciation is the swing factor.** D&A reached **10.0% of revenue** in Q2 (vs 9.1%), +31% y/y, and TTM D&A is **$75.2B (+28%)**. This is the P&L cost of the AI build. Operating margin still expanded, which implies gross profit/AWS mix is absorbing it — but the depreciation curve steepens every quarter as prior capex enters service. **This is the single most important line to watch in 2027.**
- **Tax rate normalization is a headwind.** Effective rate 23.0% in H1-2026 vs 17.0%, partly due to tax on the fair-value gains. Even on ordinary income, a low-20s rate is the right assumption versus high-teens historically.
- **Interest expense doubled** to $2.11B in H1 as debt doubled; still only ~4% of operating income (21x coverage in Q2) — not a solvency issue, but it is now a visible EPS drag and will keep growing.

---

## 4. Earnings quality: the $62.8B non-cash mark

The most important analytical adjustment in this report:

- **H1-2026 upward price adjustments on equity securities without readily determinable fair value: $62.814B** (Q2 alone: **$50.486B**; Q1: ~$12.3B).
- This sits inside `NonoperatingIncomeExpense` of **$69.4B** — i.e., **~90% of H1 "other income" is a mark-to-model revaluation of a private stake**, not cash, not operating, and not repeatable on demand.
- The balance-sheet counterpart: `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` exploded from **$16.2B at 12/31/25 to $122.3B at 6/30/26 (+$106B)**. A large part is the mark-up plus new investment. This is a concentrated, illiquid asset whose value is set by financing rounds, not markets.
- **Adjusted earnings (excluding the pre-tax mark, taxed at the 23% effective rate):**

| | Reported | Less mark (after tax) | Adjusted | Adj. y/y |
|---|---:|---:|---:|---:|
| Q2-2026 net income | $62.65B | –$38.87B | **~$23.8B** | +31% |
| Q2-2026 diluted EPS | $5.75 | –$3.57 | **~$2.18** | +30% |
| H1-2026 net income | $92.90B | –$48.37B | **~$44.5B** | +26% |
| H1-2026 diluted EPS | $8.53 | –$4.44 | **~$4.09** | +25% |

*(Using the prior-year ~13–17% tax rate instead would give Q2 EPS ~$2.40 and H1 ~$4.40; the range $2.16–2.40 / $4.09–4.40 brackets the true underlying figure.)*

**Implication for traders:** Any headline like "AMZN EPS triples" is an accounting artifact. On ~$2.18 of Q2 adjusted EPS annualized (~$8.7) with normal Q4 seasonality, a full-year 2026 adjusted EPS in the **$9–10.5** range is a reasonable working estimate (illustrative, not guidance). Also note the reverse risk: **a future down-round or valuation reset on that private stake would produce a multi-billion-dollar non-cash charge** — asymmetric headline-EPS volatility in both directions.

---

## 5. Cash flow: record operating cash, negative free cash flow

### Trailing twelve months (2025-07-01 → 2026-06-30)

| Metric ($M) | TTM Jun-2026 | TTM Jun-2025 | Δ |
|---|---:|---:|---:|
| Operating cash flow | **161,403** | 121,137 | **+33.2%** |
| Capex (productive assets) | **173,028** | 107,656 | **+60.7%** |
| **Free cash flow** | **–11,625** | **+13,481** | n.m. |
| Finance-lease principal | 1,599 | 1,556 | +2.8% |
| FCF after finance leases | –13,224 | +11,925 | n.m. |
| Business acquisitions | **41,956** | 4,809 | +772% |
| Purchases of marketable securities | 72,902 | 46,731 | +56% |
| LT debt issued | **81,925** | 746 | n.m. |
| ST debt issued | 20,798 | 8,187 | +154% |
| LT + ST repayments | 25,656 | 15,335 | +67% |

### Quarterly cadence

| ($M) | Q1-2026 | Q2-2026 | Q2-2025 |
|---|---:|---:|---:|
| Operating cash flow | 26,032 | 45,387 | 32,515 |
| Capex | 44,203 | 54,208 | 32,183 |
| **FCF** | **–18,171** | **–8,821** | **+332** |
| Acquisitions | 15,408 | 24,359 | 1,700 |
| Investing cash flow | –64,212 | –79,245 | –39,424 |
| Financing cash flow | +52,767 | +10,146 | –2,539 |

**Interpretation:**
- **Capex is running at ~26–27% of revenue** (Q2: $54.2B on $200.6B). That is hyperscale-AI-utility territory, not retail. It is being funded by operating cash plus debt.
- **Cash OCF quality needs a caveat:** TTM OCF includes a **$41.4B deferred-tax add-back** (largely the deferred tax liability booked against the non-cash equity marks) and $75.2B of D&A. Strip deferred taxes and D&A and the underlying cash conversion is far less dramatic than the +33% headline. OCF growth is real, but flattered.
- **$42.0B of acquisitions in twelve months ($39.8B in H1-2026 alone, $24.4B in Q2)** is a major, under-discussed capital-allocation shift. Combined with announced AI investments, Amazon is deploying cash into inorganic growth at scale.
- Amazon has **no dividend and no buyback** in the data — 100% of capital is being reinvested.

---

## 6. Balance sheet and liquidity

| Item ($M) | 2026-06-30 | 2025-12-31 | Δ |
|---|---:|---:|---:|
| Cash & equivalents | 78,213 | 86,810 | –9.9% |
| Available-for-sale debt securities | 97,900 | 45,800 | +113.8% |
| Accounts receivable, net | 88,092 | 67,729 | **+30.1%** |
| Inventory, net | 38,184 | 38,325 | –0.4% |
| Current assets | 249,264 | 229,083 | +8.8% |
| **Total assets** | **1,096,889** | **818,042** | **+34.1%** |
| Accounts payable | 147,440 | 121,909 | +20.9% |
| Accrued liabilities | 73,406 | 75,520 | –2.8% |
| Current liabilities | 241,274 | 218,005 | +10.7% |
| Long-term debt (total, incl. current) | **132,995** | **68,836** | **+93.2%** |
| Finance lease liabilities | 13,451 | 12,286 | +9.5% |
| Operating lease liabilities | 96,320 | 89,252 | +7.9% |
| Non-marketable equity securities | **122,300** | 16,200 | **+655%** |
| AOCI | 66,287 | 28,230 | +134.8% |

**Liquidity/leverage math:**
- Cash + AFS = **$176.1B**; debt + finance leases = **$146.4B** → **net cash ≈ $29.7B**.
- Current ratio **1.03x** — thin, typical of Amazon's negative-working-capital retail model.
- Interest coverage (Q2): operating income $27.5B / interest $1.31B = **~21x**. Comfortable.
- **The trend is the story:** net debt capacity fell by roughly $90B in six months (debt +$64B, cash –$9B, partly offset by AFS +$52B). If the capex run-rate persists at $200B+ annualized, further debt issuance is likely.

**Working-capital observations:**
- **Receivables +30% vs revenue +18%** — receivables are growing ~1.6x faster than sales. This is plausibly mix-driven (AWS/ads/third-party sellers carry different collection profiles), but it deserves monitoring; it consumed ~$20B of cash. Allowance for doubtful accounts rose to $2.8B (3.2% of gross AR) from $2.4B (3.5%), so credit quality is stable.
- **Inventory flat at $38.2B while revenue grew 18%** — a clear efficiency positive; inventory valuation reserves fell to $3.0B from $3.3B.
- **Accounts payable +21%**, roughly in line with cost of goods — no stretching of payables (a quality positive).
- **AOCI +$38.1B in six months is anomalous** relative to the disclosed FX translation loss (–$1.6B H1) and negligible AFS unrealized gains ($7M). This line, and the `DebtSecuritiesAvailableForSaleUnrealizedGainLoss` figure of $92B for H1-2026, are **internally inconsistent with other tags in the same filing**. Flag as a data-quality item to verify against the actual 10-Q before relying on it.

---

## 7. Commitments and off-balance-sheet risk

At 6/30/2026:
- **Total contractual obligations: $650.0B**
- Due within 12 months: **$78.1B**
- Due year 2: $53.4B; year 3: $46.8B; year 4: $42.2B
- Remainder of FY2026: $42.8B
- **Undiscounted operating lease payments: $116.4B** (finance leases: $16.7B)

These are largely purchase commitments for cloud/compute capacity, content, energy, and logistics. **$650B is ~60% of total assets and ~4x annualized operating income.** In a demand shock, these become operating leverage in reverse. Conversely, they are also evidence of contracted forward demand — the market will read them as bullish while AI capacity remains scarce.

Other items: unrecognized SBC of **$24.8B** (~2.5 years of grant expense at the current run-rate); contract liabilities (deferred revenue) $20.4B current + $4.5B non-current.

---

## 8. Fundamental scorecard

| Dimension | Assessment | Evidence |
|---|---|---|
| Revenue growth | **Strong / accelerating** | Q2 +19.6% y/y, H1 +18.2%; Q1 was +16.6% |
| Operating margin | **Strong / expanding** | Q2 13.7% vs 11.4%; H1 13.4% vs 11.6% |
| Gross margin | Stable/improving | 52.3% Q2 vs 51.8% |
| Opex discipline | **Good** | Marketing –0.9pp, G&A –0.4pp, SBC –$0.5B y/y in Q2 |
| Earnings quality | **Poor (this period)** | $62.8B H1 non-cash equity marks = ~90% of other income |
| Cash generation | Strong operating, **negative FCF** | OCF $161.4B TTM; FCF –$11.6B |
| Capex intensity | **Extreme** | 27% of Q2 revenue; TTM capex +61% |
| Balance sheet | **Adequate, deteriorating** | Net cash ~$29.7B; debt +93% in 6 months |
| Liquidity | Adequate | $176.1B cash+AFS; current ratio 1.03 |
| Off-balance-sheet risk | **Elevated** | $650B contractual obligations |
| Capital returns | None | No dividend, no buyback |
| Insider signal | **Unknown** | Data unavailable |
| Accounting/data flags | Several | AOCI and AFS unrealized-gain tags inconsistent |

---

## 9. Actionable trading insights

**Bull case (operating):**
- Operating income compounding >35% with margins at record levels is the cleanest evidence that AWS/AI and advertising monetization are outweighing the depreciation drag. If Q3 shows another ~40% operating-income increase, the "AI capex is destroying returns" bear thesis weakens materially.
- Inventory discipline and falling SBC as a % of revenue show cost control is genuine, not just revenue leverage.
- $176B of liquid assets plus 21x interest coverage means Amazon can fund the build-out without distress — the balance sheet is a competitive weapon against smaller AI competitors.

**Bear case / risks:**
- **Free cash flow is negative and worsening.** With capex at 27% of revenue, any deceleration in AI demand hits both the P&L (depreciation) and the balance sheet (debt) simultaneously.
- **Reported EPS is not cash.** Traders who anchor on $5.75 quarterly EPS will overpay; a mark-down of the $122B private-equity book would create an equally dramatic negative headline.
- **Leverage inflection.** Total debt +$64B in six months. Another two quarters at this pace pushes gross debt toward $200B+ and removes the net-cash cushion.
- **$650B of contractual obligations** is the most under-priced risk in the disclosure set.
- Tax rate now ~23% vs ~17% historically — a structural ~5–7% EPS headwind versus prior modeling.

**What to watch in the next print (~late Oct 2026, Q3-2026 10-Q):**
1. **AWS revenue growth and AWS operating margin** — the single biggest driver of the multiple.
2. **Capex guide / actual Q3 capex vs the $54B Q2 run-rate.** A further step-up is bearish for FCF; a plateau is bullish.
3. **Depreciation as % of revenue** — currently 10.0%; watch for acceleration above 10.5%.
4. **Non-operating income ex-marks** — isolate the fair-value adjustment line so you can compute a clean EPS.
5. **Debt issuance and revolver usage**, plus any change in the AFS securities balance (a drawdown would signal liquidity stress).
6. **Receivables growth vs revenue growth** — a widening gap would be an early warning.
7. **Any valuation event around the private AI stake** (financing round, markdown, or IPO) — this will dominate reported EPS.

**Positioning framework (given no price data was supplied by the tools — valuation multiples cannot be computed here):**
- On **adjusted** earnings power (~$8.7 annualized Q2 run-rate; ~$9–10.5 illustrative FY26), `AMZN` should be valued as a **high-teens-to-low-20s-growth compounder with negative FCF**, not as a cash-flow yield story. Justified multiple therefore rests on the durability of 13%+ operating margins into 2027–28 as depreciation peaks.
- **Asymmetry:** upside from continued 40%+ operating-income growth and AI monetization; downside from a capex guide-up combined with slowing AWS growth — that combination is the scenario that compresses the multiple.
- **Event risk is elevated around earnings** because reported EPS will swing violently with private-stake marks, creating gap risk in both directions independent of operations.
- **Insider signal: unavailable — treat as neutral/unknown, not as confirmation.**

---

## 10. Key points summary

| Category | Metric / Point | Value | Signal |
|---|---|---|---|
| **Latest filing** | Form 10-Q, quarter ended 2026-06-30 (accepted 2026-07-31) | — | 6 weeks old; no new SEC data this week |
| **Revenue** | Q2-2026 | $200.6B, +19.6% y/y | 🟢 Accelerating |
| | H1-2026 | $382.1B, +18.2% y/y | 🟢 |
| **Operating income** | Q2-2026 | $27.46B, +43.2% y/y | 🟢 Strong |
| | H1-2026 | $51.31B, +36.6% y/y | 🟢 |
| **Operating margin** | Q2-2026 | 13.7% (vs 11.4%) | 🟢 +230 bp |
| **Gross margin** | Q2-2026 | 52.3% (vs 51.8%) | 🟢 |
| **D&A** | Q2-2026 / TTM | $20.0B (+31%) / $75.2B (+28%) | 🟡 Capex digestion |
| **Reported EPS** | Q2-2026 diluted | $5.75 (+242%) | 🔴 Distorted by marks |
| **Adjusted EPS** | Q2-2026 (ex $50.5B mark) | ~$2.16–2.40, +29–43% y/y | 🟢 Underlying growth solid |
| **Non-cash equity mark** | H1-2026 upward adjustment | $62.8B pre-tax (Q2: $50.5B) | 🔴 Earnings-quality issue |
| **Private equity book** | Non-marketable equity securities | $122.3B (from $16.2B at 12/31/25) | 🟡 Concentration/valuation risk |
| **Operating cash flow** | TTM Jun-2026 | $161.4B, +33.2% y/y | 🟢 |
| **Capex** | TTM / Q2 | $173.0B (+61%) / $54.2B (27% of revenue) | 🔴 Extreme |
| **Free cash flow** | TTM Jun-2026 | **–$11.6B** (vs +$13.5B) | 🔴 Negative |
| **Acquisitions** | TTM / H1-2026 | $42.0B / $39.8B | 🟡 Capital allocation shift |
| **Total debt** | 6/30/26 | $133.0B (+93% vs 12/31/25) | 🔴 Rapid leveraging |
| **Net cash** | Cash+AFS minus debt+fin. leases | ~+$29.7B | 🟡 Still positive, shrinking |
| **Liquidity** | Cash + AFS | $176.1B | 🟢 |
| **Current ratio** | 6/30/26 | 1.03x | 🟡 Thin |
| **Interest coverage** | Q2-2026 | ~21x | 🟢 |
| **Receivables** | 6/30/26 | $88.1B, +30.1% vs revenue +18.2% | 🟡 Monitor |
| **Inventory** | 6/30/26 | $38.2B, –0.4% | 🟢 Efficiency |
| **Contractual obligations** | 6/30/26 | $650.0B ($78.1B due <12m) | 🔴 Under-priced commitment risk |
| **Operating leases** | Undiscounted | $116.4B | 🟡 |
| **SBC** | H1-2026 | $10.07B (–1.5% y/y); $24.8B unrecognized | 🟢 Disciplined |
| **Tax rate** | H1-2026 | 23.0% (vs 17.0%) | 🔴 EPS headwind |
| **Capital returns** | Dividend / buyback | None / None | 🟡 Full reinvestment |
| **Insider transactions** | — | **Data unavailable** | ⚪ No signal |
| **Next catalyst** | Q3-2026 results | ~late Oct 2026 | Watch AWS, capex, D&A |
| **Data-quality flags** | AOCI +$38.1B and $92B AFS unrealized-gain tag inconsistent with other disclosures | — | ⚠️ Verify vs 10-Q |

**Bottom line for `AMZN`:** a fundamentally strong, accelerating operating business wearing a misleadingly spectacular reported-EPS headline, funded by a historically aggressive capex program that has pushed free cash flow negative and debt up 93% in six months. Trade the operating momentum, but model the earnings off adjusted figures (~$2.2/quarter core), respect the $650B commitment tail, and treat private-stake marks as a volatility source rather than value creation.