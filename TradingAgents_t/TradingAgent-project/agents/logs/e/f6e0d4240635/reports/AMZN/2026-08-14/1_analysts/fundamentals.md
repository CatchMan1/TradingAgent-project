# AMZN — Fundamental Deep Dive
**Prepared 2026-08-14 | Data source: SEC point-in-time facts, latest filing = Q2 FY2026 Form 10-Q (acc. 0001018724-26-000026), filed/accepted 2026-07-31**

---

## 1. Data provenance & caveats (read first)

| Item | Status |
|---|---|
| Primary statement source | Q2 FY2026 10-Q filed 2026-07-31 (fresh — ~2 weeks old) |
| Comparative data | Q2 FY2025 / H1 FY2025 (from same 10-Q) + FY2025 year-end balance sheet |
| 10-K / annual period facts | **Not present** in the point-in-time cache — annual-frequency calls returned the same 10-Q dataset. No full-year FY2025 income statement or cash-flow statement was available. |
| Segment-level revenue | **Not in extract.** Only the segment *count* (3) is tagged. |
| Insider transactions | **DATA UNAVAILABLE** — no authorized insider archive for AMZN as of 2026-08-14. **No insider activity is inferred or fabricated in this report.** |
| Price / valuation multiples | Not available from tools; ratios below are statement-based only |
| Revenue derivation | Vendor does not tag `Revenues`; derived as `CostsAndExpenses + OperatingIncomeLoss` (reconciles exactly to reported operating income) |

---

## 2. Company profile

Amazon.com, Inc. (AMZN) is a global technology and logistics conglomerate operating **three reportable segments** (per the 10-Q segment tag): **North America**, **International**, and **Amazon Web Services (AWS)**. Business lines span online and physical retail, third-party marketplace services, Prime subscriptions, advertising, AWS cloud/compute/AI infrastructure, logistics and fulfillment, devices, and a large portfolio of equity investments in private and public technology companies.

**Scale markers from the filing:**
- Total assets: **$1,095.7B** (crossed $1T during H1 FY2026)
- Shares outstanding: **10,783M** (6/30/26); **10,786.3M** (7/22/26 cover date) — effectively flat, **no dilution**
- Shares issued 11,298M vs. outstanding 10,783M → ~515M treasury shares
- Authorized capital: 100B shares
- Headcount/segment revenue not disclosed in the returned facts

---

## 3. Income statement — the quarter was excellent, but headlines overstate it

### 3.1 Reported results

| $M | Q2 FY2026 | Q2 FY2025 | Δ YoY | H1 FY2026 | H1 FY2025 | Δ YoY |
|---|---|---|---|---|---|---|
| Revenue (derived) | **200,606** | 167,702 | **+19.6%** | **382,125** | 323,369 | **+18.2%** |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 183,241 | 157,785 | +16.1% |
| Gross profit | **104,828** | 86,893 | +20.6% | **198,884** | 165,584 | +20.1% |
| Gross margin | **52.26%** | 51.81% | +45bp | **52.05%** | 51.21% | +84bp |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 330,812 | 285,793 | +15.8% |
| Operating income | **27,461** | 19,171 | **+43.2%** | **51,313** | 37,576 | **+36.6%** |
| Operating margin | **13.69%** | 11.43% | **+226bp** | **13.43%** | 11.62% | **+181bp** |
| Non-operating income/(expense) | **53,396** | 1,686 | nm | **69,378** | 4,960 | nm |
| Pretax income | **80,857** | 20,857 | +288% | **120,691** | 42,536 | +184% |
| Income tax | 18,199 | 2,678 | — | 27,759 | 7,231 | — |
| Effective tax rate | 22.5% | 12.8% | +970bp | 23.0% | 17.0% | +600bp |
| Net income | **62,647** | 18,164 | **+245%** | **92,902** | 35,291 | +163% |
| Diluted EPS | **$5.75** | $1.68 | +242% | **$8.53** | $3.27 | +161% |
| Diluted shares (implied) | 10,895M | 10,812M | +0.8% | — | — | — |

### 3.2 The critical adjustment: ~$62.8B of the H1 profit is a non-cash mark-up

The single most important fact in this filing: **non-operating income of $53.4B in Q2 and $69.4B in H1 is almost entirely a revaluation of private equity holdings**, not operations.

| $M | Q2 FY2026 | H1 FY2026 | Q2 FY2025 | H1 FY2025 |
|---|---|---|---|---|
| Upward price adjustment, equity securities without readily determinable FV | **50,486** | **62,814** | 49 | 86 |
| Equity securities FV-NI gain/(loss) | 1,300 | 454 | 393 | 188 |
| Equity-method losses | (11) | (30) | (15) | (14) |
| Warrant fair-value adjustment | (1,449) | (1,051) | (590) | (212) |
| Interest income | 1,295 | 2,430 | 1,085 | 2,151 |
| Interest expense | (1,314) | (2,114) | (516) | (1,057) |

**Core (ex-mark-up, ex-FVNI) reconstruction:**

| | Q2 FY2026E | Q2 FY2025 | Δ | H1 FY2026E | H1 FY2025 | Δ |
|---|---|---|---|---|---|---|
| Pretax income as reported | 80,857 | 20,857 | | 120,691 | 42,536 | |
| less: RDFV upward adjustment | (50,486) | (49) | | (62,814) | (86) | |
| less: equity securities FV-NI gain | (1,300) | (393) | | (454) | (188) | |
| **Core pretax** | **29,071** | **20,415** | **+42.4%** | **57,423** | **42,262** | **+35.9%** |
| Core net income @ ~22.5%/23.0% tax | ~22,530 | ~17,780 | +26.7% | ~44,215 | ~35,078 | +26.0% |
| **Core diluted EPS (approx.)** | **~$2.07–2.16** | **~$1.64–1.68** | **+25–30%** | **~$4.05** | **~$3.25–3.27** | **~+24%** |

**Verdict:** the true operational story is **~+26–30% EPS growth with 226bp of operating-margin expansion on 19.6% revenue growth.** That is an outstanding quarter. But **the reported +242% EPS print is not repeatable** — roughly **52% of H1 pretax income ($62.8B) is a non-cash private-company valuation mark**. Any headline-driven screen will misprice this.

### 3.3 Why the mark matters for the balance sheet and the future

- "Equity securities without readily determinable fair value" ballooned from **$16.2B (12/31/25) → $122.3B (6/30/26)**, i.e., **11.2% of total assets**.
- Of the +$106.1B increase: **$62.8B is the valuation mark-up**, and **~$43.3B is additions** — consistent with the **$39.8B of cash business acquisitions in H1 FY2026** (Q2 alone: $24.4B). This is a step-change M&A pivot (H1 FY2025 acquisitions were only $1.65B).
- **Mark-to-market risk is now first-order:** a 20% haircut on this $122.3B book would be a ~$24B pre-tax charge, ~$2.25/share. Conversely, further upward rounds are pure EPS.

### 3.4 Margin bridge — genuine leverage *despite* a large depreciation headwind

| % of revenue | Q2 FY2026 | Q2 FY2025 | Δ bp | H1 FY2026 | H1 FY2025 | Δ bp |
|---|---|---|---|---|---|---|
| Gross margin | 52.26% | 51.81% | +45 | 52.05% | 51.21% | +84 |
| Opex ex-COGS | 38.57% | 40.38% | **−181** | 38.62% | 39.59% | −97 |
| — Marketing | 5.83% | 6.81% | −98 | 5.76% | 6.55% | −79 |
| — G&A | 1.39% | 1.77% | −38 | 1.41% | 1.73% | −32 |
| — Total D&A | **9.96%** | 9.08% | **+88 (headwind)** | **10.19%** | 9.12% | +107 (headwind) |
| — of which PP&E depreciation | 6.91% | 5.82% | +109 | 6.99% | 5.82% | +117 |
| — SBC | **3.01%** | 3.90% | **−89 (tailwind)** | **2.64%** | 3.16% | −52 |
| Operating margin | **13.69%** | 11.43% | +226 | 13.43% | 11.62% | +181 |

Key reads:
- **D&A grew +31.3% YoY in Q2 ($19,988M vs $15,227M); PP&E depreciation alone +42%.** That is an 88bp drag that management absorbed *and still* expanded margins 226bp. This is the strongest possible evidence that the AI capex is beginning to generate returns.
- **SBC declined in absolute dollars** ($10,070M H1 FY26 vs $10,223M H1 FY25) and fell 52bp as a % of revenue. Combined with flat share count, **SBC discipline is a real, underappreciated positive** and directly supports per-share value.
- Marketing leverage (−98bp) and G&A leverage (−38bp) show cost control, not just mix.

### 3.5 Sequential & quarterly detail (this is an accelerating business)

| $M | Q1 FY2026 | Q2 FY2026 | Q1 FY2025 | Q2 FY2025 |
|---|---|---|---|---|
| Revenue | 181,519 | 200,606 | 155,667 | 167,702 |
| YoY growth | **+16.6%** | **+19.6%** | — | — |
| Gross margin | 51.82% | 52.26% | 50.5% | 51.81% |
| Operating income | 23,852 | 27,461 | 18,405 | 19,171 |
| Operating margin | 13.14% | 13.69% | 11.8% | 11.43% |
| RDFV upward adjustment | 12,328 | 50,486 | 37 | 49 |
| Net income | 30,255 | 62,647 | 17,127 | 18,164 |
| Diluted EPS | $2.78 | $5.75 | $1.59 | $1.68 |
| Core EPS (approx.) | ~$1.90–1.97 | ~$2.07–2.16 | ~$1.57 | ~$1.64–1.68 |

**Revenue is accelerating sequentially on a YoY basis (+16.6% → +19.6%)**, and the Q2/Q1 seasonal step-up was 1.105x vs. 1.077x a year ago — a stronger-than-normal sequential ramp. Given 3 segments and no segment disclosure in the extract, I cannot attribute the acceleration, but **19.6% consolidated growth alongside +32% D&A growth and 226bp of margin expansion is the signature of an accelerating AWS/AI infrastructure business** (inference, not disclosed).

---

## 4. Balance sheet — transformed in six months

| $M | 6/30/2026 | 12/31/2025 | Δ | Δ % |
|---|---|---|---|---|
| **ASSETS** | | | | |
| Cash & equivalents | 78,213 | 86,810 | −8,597 | −9.9% |
| Available-for-sale debt securities | **97,900** | 45,800 | +52,100 | **+113.8%** |
| **Cash + marketable securities** | **176,113** | **132,610** | +43,503 | +32.8% |
| Accounts receivable, net | 88,092 | 67,729 | +20,363 | **+30.1%** |
| Allowance for doubtful accounts | 2,800 | 2,400 | +400 | +16.7% |
| Inventories, net | 38,184 | 38,325 | −141 | −0.4% |
| Current assets | 249,264 | 229,083 | +20,181 | +8.8% |
| Equity securities w/o readily determinable FV | **122,300** | 16,200 | +106,100 | **+655%** |
| Operating lease ROU assets | 92,743 | 86,054 | +6,689 | +7.8% |
| **Total assets** | **1,095,689** | **818,042** | **+277,647** | **+33.9%** |
| **LIABILITIES** | | | | |
| Accounts payable | 147,440 | 121,909 | +25,531 | +20.9% |
| Accrued liabilities | 73,406 | 75,520 | −2,114 | −2.8% |
| Current portion of LTD | 3,330 | 2,748 | +582 | +21.2% |
| Current liabilities | 241,274 | 218,005 | +23,269 | +10.7% |
| **Long-term debt (total)** | **132,995** | **68,836** | **+64,159** | **+93.2%** |
| — noncurrent portion | 128,894 | 65,648 | +63,246 | +96.3% |
| Finance lease liabilities (total) | 13,451 | 12,286 | +1,165 | +9.5% |
| Operating lease liabilities (total) | 96,320 | 89,252 | +7,068 | +7.9% |
| Identified liabilities (current + noncurrent debt/leases) | **464,506** | **370,992** | +93,514 | +25.2% |
| **Stockholders' equity (derived, est.)** | **≈545,000–555,000** | ≈415,000–425,000 | ≈+135,000 | ≈+32% |
| Book value per share (est.) | **≈$51** | ≈$39 | | |

*Equity is not directly tagged in the extract; estimated as total assets less identified liabilities plus inferred other long-term liabilities (~$75–80B at 6/30/26, up ~$46B, consistent with deferred taxes arising on the $62.8B mark). Two independent methods (asset-minus-liabilities and roll-forward of NI + OCI + APIC) converge within ~$10B, so BVPS ≈ $50–53 is a reasonable estimate.*

### 4.1 Leverage: debt roughly doubled — but still net cash

| $M | 6/30/2026 | 12/31/2025 | Change |
|---|---|---|---|
| Long-term debt | 132,995 | 68,836 | +64,159 |
| Finance lease liabilities | 13,451 | 12,286 | +1,165 |
| **Gross financial debt** | **146,446** | **81,122** | **+65,324 (+80.5%)** |
| Cash + AFS securities | 176,113 | 132,610 | +43,503 |
| **Net cash / (net debt)** | **+29,667** | **+51,488** | **−21,821** |
| Operating leases (off-ratio) | 96,320 | 89,252 | +7,068 |
| Net debt incl. operating leases | (66,653) | (37,764) | −28,889 |
| Gross financial debt / total assets | 13.4% | 9.9% | +350bp |

**Amazon is still in a net cash position on a financial-debt basis** ($29.7B net cash), even after nearly doubling gross debt. That materially softens the "leverage risk" narrative — but the cushion shrank $21.8B in six months and the trajectory is clearly toward funding the buildout with debt.

### 4.2 Liquidity and working capital

- Current ratio: **249,264 / 241,274 = 1.03x** (vs. 1.05x at 12/31/25) — thin but structurally normal for Amazon, which funds itself on supplier float.
- **Accounts payable grew +20.9%**, comfortably funding the +8.8% current-asset growth. Supplier financing remains the working-capital engine.
- **Inventory flat (−0.4%) against +19.6% revenue growth** — inventory turns improved sharply; inventory valuation reserves actually *fell* ($3.0B vs $3.3B). No demand-destruction signal here.
- **AR +30.1% vs revenue +19.6%**: DSO ≈ **40.0 days** vs **36.7 days** a year ago. Allowance up 17%, slower than AR — modest but worth monitoring into an advertising/3P-seller credit cycle.
- Contract liabilities (deferred revenue / gift cards): $20,428M current + $4,500M noncurrent — flat YoY. **$15.2B of prior deferred revenue was recognized in H1 FY2026.**

### 4.3 The elephant: $650B of contractual obligations

The 10-Q discloses **aggregate contractual obligations of $650,034M** at 6/30/2026 — **59% of total assets**.

| Maturity | $M |
|---|---|
| Remainder of FY2026 | 42,752 |
| Next 12 months (rolling) | 78,084 |
| Year 2 | 53,406 |
| Year 3 | 46,767 |
| Year 4 | 42,219 |
| **Sum through year 4** | **220,476** |
| **Implied beyond year 4** | **≈429,558** |

The disclosed ladder only accounts for ~$220B through year 4, implying **~$430B of commitments maturing beyond year 4**. For context, operating lease payments total $116.4B and debt $133.0B. This is consistent with **multi-year AI compute, chip, data-center and content commitments** — a powerful demand signal, but also a hard, largely non-cancellable fixed-cost layer that raises operating leverage in both directions.

---

## 5. Cash flow — the real battleground

| $M | Q2 FY2026 | Q2 FY2025 | Δ | H1 FY2026 | H1 FY2025 | Δ | TTM 6/30/26 | TTM 6/30/25 | Δ |
|---|---|---|---|---|---|---|---|---|---|
| Operating cash flow | **45,387** | 32,515 | **+39.6%** | **71,419** | 49,530 | **+44.2%** | **161,403** | 121,137 | **+33.2%** |
| Capex (productive assets) | **54,208** | 32,183 | **+68.4%** | **98,411** | 57,202 | **+72.0%** | **173,028** | 107,656 | **+60.7%** |
| **Free cash flow** | **(8,821)** | **+332** | nm | **(26,992)** | **(7,672)** | worse | **(11,625)** | **+13,481** | nm |
| Business acquisitions | 24,359 | 1,700 | +1,333% | **39,767** | 1,652 | +2,307% | 41,956 | 4,809 | +772% |
| **FCF after acquisitions** | **(33,180)** | (1,368) | nm | **(66,759)** | (9,324) | nm | (53,581) | (10,914) | nm |
| Investing cash flow | (79,245) | (39,424) | — | (143,457) | (69,227) | — | (216,775) | (123,569) | — |
| Financing cash flow | +10,146 | (2,539) | — | **+62,913** | (2,586) | — | **+75,160** | (8,652) | — |
| — LTD issuance | 13,557 | 0 | — | **66,998** | 746 | — | 81,925 | 746 | — |
| — ST debt proceeds | 9,368 | 2,093 | — | 15,386 | 3,908 | — | 20,798 | 8,187 | — |
| — LTD repayments | 2,752 | 2,751 | — | 2,752 | 2,751 | — | 5,022 | 7,434 | — |
| — ST debt repayments | 9,573 | 1,392 | — | 15,682 | 3,474 | — | 20,634 | 7,901 | — |
| Cash taxes paid | 2,655 | 4,761 | **−44%** | 3,978 | 5,638 | **−29%** | 6,635 | 11,788 | **−44%** |
| Operating lease payments | 3,489 | 3,758 | −7% | 7,804 | 7,320 | +7% | 15,522 | 13,485 | +15% |

### 5.1 The central tension

- **Operating cash flow is compounding beautifully:** +44% in H1, +33% TTM, and Q2 OCF reached **22.6% of Q2 revenue** (vs. 19.4% a year ago). OCF margin expansion is real.
- **Capex is compounding faster:** Q2 capex was **27.0% of revenue** (vs. 19.2%), H1 was 25.8% (vs. 17.7%), TTM was **$173.0B**.
- **Result: TTM free cash flow is NEGATIVE $11.6B**, a ~$25B swing from +$13.5B a year ago. Even H1 capex alone ($98.4B) exceeded TTM OCF a year ago.
- The gap is being closed with **debt ($82B LTD issued TTM) and acquisition-driven asset growth**, and it is why total assets jumped 34% in six months.

**Trader takeaway:** the equity story has shifted from "FCF machine" to "capital-deployment story with a multi-year negative-FCF hole." At 25%+ of revenue, capex must eventually produce either AWS revenue acceleration or it becomes a valuation de-rating event. **Capex guidance is now the single highest-beta disclosure in AMZN's earnings.**

### 5.2 Cash taxes: a quiet but powerful support

- H1 FY2026 cash taxes: **$3,978M on $120,691M pretax = 3.3% cash tax rate.**
- H1 FY2025: $5,638M on $42,536M = 13.3%.
- Deferred tax expense H1 FY2026: **$30,489M** (vs. $518M in H1 FY2025); TTM $41,441M.
- Q2 FY2026: deferred tax expense $17,691M vs. income tax expense $18,199M → essentially *all* of the P&L tax charge was non-cash.

**Cash taxes fell 29% while pretax income nearly tripled.** That is the mechanical (DTL) result of the non-cash investment revaluation and heavy accelerated depreciation on capex, and it is what keeps OCF growth at +44%. **It is a genuine cash benefit, but it is also flattered by the non-cash mark and by bonus depreciation — do not extrapolate the 3% cash tax rate.**

### 5.3 Working-capital drag in H1 FY2026

| $M | H1 FY2026 | H1 FY2025 |
|---|---|---|
| AR & other operating assets | (13,954) | (122) |
| Accrued liabilities & other operating liabilities | (10,063) | (9,013) |
| Other noncurrent assets | (8,528) | (6,373) |
| Contract liabilities | +74 | +609 |

H1 FY2026 saw a **~$14.0B working-capital outflow from receivables/other assets vs. ~$0.1B a year ago** — a meaningful, and largely non-recurring-looking, drag. AP growth ($25.5B) offset most of it. Even so, H1 OCF still rose 44%, which makes the underlying cash generation look better than the raw footprint suggests.

---

## 6. Quality of earnings & accounting flags

| Observation | Assessment |
|---|---|
| $62.8B H1 non-cash private-investment mark-up = 52% of H1 pretax | **High — biggest adjustment item.** Reported EPS is not a proxy for earnings power. |
| Deferred tax expense $30.5B vs. cash taxes $4.0B in H1 | **High — explains the OCF/NI divergence and near-4% cash tax rate.** Unsustainable as a growth driver. |
| Total D&A +31% YoY (PP&E depreciation +42%) | **Structural, not a flag** — the bill for the AI buildout is arriving; margins still expanded. |
| AOCI +$38.1B in H1 (28,230 → 66,287); Q2 OCI alone +$41.4B vs. only ~$0.5B identified in FX + securities components | **Flagged.** Within this extract the Q2 OCI gain is largely *unattributed*. It inflates book equity by ~$38B, or ~$3.50/share, without touching income. Q2 comprehensive income $104.1B vs. net income $62.6B. Do not treat BVPS growth as tangible/operational. |
| `DebtSecuritiesAvailableForSaleUnrealizedGainLoss` tagged at $92.0B for H1 FY26 | **Discarded as unreliable.** Contradicted by gross unrealized gains of only $7M / losses $67M on the $97.9B AFS book. Probably a mis-tagged dimension. Not used anywhere in this report. |
| Inventory flat vs. +19.6% revenue; valuation reserves down | **Positive quality signal.** No channel-stuffing or obsolescence tell. |
| AR +30% vs. revenue +20%; allowance +17% | **Mild caution.** DSO 36.7 → 40.0 days. |
| Diluted shares +0.8% YoY; SBC down in absolute dollars | **Strong positive.** Real per-share accretion. |
| $650B contractual obligations, ~$430B beyond year four | **Flagged.** Massive fixed-commitment overhang — bullish on demand, bearish on flexibility. |

---

## 7. Insider activity

**No data available.** The vendor's point-in-time archive contains no authorized insider-transaction records for AMZN as of 2026-08-14. This report makes **no statement, estimate, or inference** about insider buying or selling. Anyone relying on insider flow for AMZN must source it from Forms 3/4/5 via EDGAR directly.

---

## 8. Actionable conclusions for traders

### The bull case (structurally supported by this filing)
1. **Revenue acceleration is genuine**: +16.6% (Q1) → +19.6% (Q2), with an unusually strong sequential step-up (1.105x vs. 1.077x). Growth *and* margin expansion simultaneously — the rarest combination at this scale.
2. **Operating leverage is beating a 31% D&A headwind.** 226bp of Q2 margin expansion *after* absorbing +88bp of depreciation. This is direct evidence the capex is converting.
3. **Core EPS ~+26–30% YoY**, driving ~+24–26% core EPS growth in H1 — a high-teens/low-20s P/E growth profile if the multiple has compressed.
4. **Balance sheet is still net cash** ($29.7B) despite gross debt +80%; interest coverage ~21x in Q2, ~24x in H1.
5. **Per-share discipline**: SBC down, share count flat, buyback-free but non-dilutive.
6. **Cash flow engine intact**: OCF +44% H1, +33% TTM; cash taxes only $4.0B on $120.7B pretax.

### The bear case (also supported by this filing)
1. **TTM FCF is negative $11.6B** and deteriorating ($13.5B → −$11.6B YoY). Q2 FCF −$8.8B; H1 −$27.0B; after acquisitions H1 −$66.8B.
2. **Capex at 25.8% of H1 revenue** and rising. Any further step-up pushes FCF further negative and reframes AMZN as a debt-funded infrastructure bet.
3. **Reported earnings are 52% non-cash mark-up.** Expect a messy "beat" headline; algorithms and fast money may chase a number that core operations didn't produce. **Sell-side will publish core EPS ~$2.10 vs. reported $5.75** — a ~63% haircut. Volatility around that reconciliation is a tradable event.
4. **$122.3B concentrated private-equity exposure (11.2% of assets)** with mark-to-market-through-earnings volatility. Down-round risk is now a real EPS risk.
5. **$650B of contractual obligations**, ~$430B beyond year 4 — a hard floor under future costs regardless of demand.
6. **D&A growth of +31% will persist and accelerate** as the buildout is placed in service; interest expense already +155% YoY in Q2 ($1,314M vs. $516M) and will keep climbing on $133B of debt.
7. **AOCI +$38.1B inflates book equity** — book value quality is weaker than the headline.

### Specific things to trade/watch into Q3 FY2026 (report ~late Oct 2026)
| Trigger | Why it matters |
|---|---|
| **Capex guidance / H2 capex run-rate** | Q2 alone was $54.2B. If H2 exceeds ~$120B, TTM FCF goes deeply negative and leverage rises further. Highest-impact variable. |
| **Whether revenue growth holds ≥19%** | The acceleration is the entire bull case; a deceleration to ~15% alongside rising D&A would compress margins. |
| **Reported vs. core EPS reconciliation** | Insiders/algos will react to the headline; the ~$2.10 core number is what matters. A stock pop on a mark-up-driven beat is a fade candidate; a sell-off on a core beat is a buy candidate. |
| **Any further RDFV upward adjustment, or a write-down** | $122.3B book. Another round = free EPS; a down-round = ~$2+/share hit. |
| **Gross debt trajectory** | $146.4B gross financial debt. Watch for further large issuance; net cash position ($29.7B) is the buffer being consumed. |
| **Deferred tax / cash tax rate normalization** | The 3% cash tax rate is unsustainable; normalization is an OCF headwind. |
| **AR/DSO and allowance** | 40.0 days and rising; early credit/customer-quality signal. |
| **Segment disclosure (AWS vs. NA vs. Intl.)** | Not in this dataset. If AWS growth re-accelerates past ~30%, the capex is justified; if it doesn't, the capex is a problem. |

### Opinionated stance
The **operational fundamentals in this filing are the best AMZN has printed in years** — accelerating revenue, expanding margins *through* a depreciation wall, no dilution, rising OCF. The **reported earnings are noisy and overstated**, and the **free-cash-flow profile is genuinely negative and worsening**. That combination argues for: **own the core operating trend, fade headline-EPS euphoria, and treat capex guidance as the binary event.** The balance sheet still has ~$29.7B of net cash and $176B of liquid assets, so there is no near-term solvency question — meaning the risk is duration of negative FCF and multiple compression, not financial distress.

---

## 9. Key metrics summary

| Category | Metric | Value | YoY / Prior-period context | Signal |
|---|---|---|---|---|
| **Scale** | Q2 FY2026 revenue (derived) | $200.61B | +19.6% YoY | 🟢 Accelerating |
| | H1 FY2026 revenue | $382.13B | +18.2% YoY | 🟢 |
| | Total assets (6/30/26) | $1,095.69B | +33.9% in 6 months | 🟡 Balance-sheet expansion |
| | Shares outstanding | 10,783M | +0.8% diluted YoY | 🟢 Non-dilutive |
| **Profitability** | Q2 gross margin | 52.26% | +45bp | 🟢 |
| | Q2 operating income | $27.46B | +43.2% | 🟢 |
| | Q2 operating margin | 13.69% | +226bp | 🟢 Best-in-class leverage |
| | H1 operating margin | 13.43% | +181bp | 🟢 |
| | Q2 total D&A | $19.99B (9.96% of rev) | +31.3% | 🔴 Structural headwind |
| | Q2 SBC | $6.04B (3.01% of rev) | −7.6%; −89bp of rev | 🟢 Discipline |
| **Earnings** | Q2 reported diluted EPS | $5.75 | +242% | 🟡 52% is non-cash mark |
| | H1 reported diluted EPS | $8.53 | +161% | 🟡 |
| | **Q2 core EPS (est.)** | **~$2.07–2.16** | **+25–30%** | 🟢 True earnings power |
| | **H1 core EPS (est.)** | **~$4.05** | **~+24%** | 🟢 |
| | H1 RDFV upward revaluation | $62.81B | vs. $0.09B LY | 🔴 Non-cash, non-recurring |
| | H1 effective tax rate | 23.0% | +600bp | 🟡 Normalizing |
| **Cash flow** | H1 operating cash flow | $71.42B | +44.2% | 🟢 |
| | TTM operating cash flow | $161.40B | +33.2% | 🟢 |
| | Q2 capex | $54.21B (27.0% of rev) | +68.4% | 🔴 Massive buildout |
| | H1 capex | $98.41B (25.8% of rev) | +72.0% | 🔴 |
| | TTM capex | $173.03B | +60.7% | 🔴 |
| | **TTM free cash flow** | **−$11.63B** | vs. +$13.48B LY | 🔴 Key bear point |
| | H1 FCF after acquisitions | −$66.76B | vs. −$9.32B LY | 🔴 |
| | H1 cash taxes paid | $3.98B (3.3% of pretax) | −29% | 🟡 Flattered, not repeatable |
| **Balance sheet** | Cash + AFS securities | $176.11B | +32.8% | 🟢 |
| | Long-term debt (total) | $132.99B | +93.2% | 🔴 Levering up |
| | Gross financial debt | $146.45B | +80.5% | 🔴 |
| | **Net cash (ex-op leases)** | **+$29.67B** | vs. +$51.49B | 🟡 Still net cash |
| | Operating lease liabilities | $96.32B | +7.9% | 🟡 |
| | Current ratio | 1.03x | vs. 1.05x | 🟡 Thin |
| | Est. stockholders' equity | ~$545–555B | ~+32% | 🟡 Incl. $38B AOCI |
| | Est. book value/share | ~$51 | vs. ~$39 | 🟡 Incl. non-cash gains |
| | Contractual obligations | $650.03B (59% of assets) | ~$430B beyond yr 4 | 🔴 Fixed-cost overhang |
| **Earnings quality** | Private equity w/o RDFV | $122.30B (11.2% of assets) | +655% | 🔴 MTM volatility |
| | AR / DSO | $88.09B / ~40.0 days | +30.1% / +3.3 days | 🟡 Watch |
| | Inventories | $38.18B | −0.4% vs. +19.6% rev | 🟢 Turns improving |
| | Accounts payable | $147.44B | +20.9% | 🟢 Funds WC |
| | AOCI | $66.29B | +$38.06B in 6 mo | 🟡 Partly unattributed |
| **Other** | Reportable segments | 3 (NA, International, AWS) | — | — |
| | H1 business acquisitions | $39.77B | vs. $1.65B LY | 🟡 M&A pivot |
| | Interest expense Q2 | $1.31B | +155% | 🔴 Rising |
| | Q2 interest coverage | ~20.9x | vs. 37x LY | 🟡 Still ample |
| **Insider** | Insider transactions | **DATA UNAVAILABLE** | — | ⚪ Not assessable |