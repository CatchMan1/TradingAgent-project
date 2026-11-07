# AMZN — Fundamental Research Report (as of 2026-08-04)

**Instrument:** AMZN (Amazon.com, Inc. — Nasdaq)
**Primary source:** Form 10-Q for the quarter ended **2026-06-30**, filed/accepted **2026-07-31** (accn 0001018724-26-000026), plus the prior 10-Q (Q1 2026, accepted 2026-04-30) for the Q1 detail bridge.
**Data note / limits:** The vendor returned a *point-in-time SEC facts* archive containing only the **latest 10-Q with prior-year comparatives** — multi-year annual statements (FY2022–FY2025) were **not** returned, and `get_insider_transactions` explicitly returned **DATA_UNAVAILABLE**. Insider activity is therefore **not** characterized here rather than guessed. Revenue is not a standalone line in the returned tag set; I derive it as *Total costs & expenses + Operating income* (this reconciles exactly and matches Amazon's known Q2 2025 revenue of $167.7B, validating the method).

---

## 1. Headline: a blowout quarter on the surface — but the quality split matters enormously

Q2 2026 (Apr–Jun) delivered **$200.6B of revenue (+19.6% y/y)** and **$27.5B of operating income (+43.2% y/y, 13.7% margin)** — the strongest combination of growth *and* margin in this dataset. But reported **diluted EPS of $5.75 vs $1.68** is *not* an operating story: **$50.5B of Q2 non-operating income came from upward revaluation of equity securities without readily determinable fair value** (private/illiquid stakes, re-measured to model marks). That single non-cash item is **62% of Q2 pretax income**.

- Reported Q2 net income: **$62.65B** (+245% y/y)
- Ex-that revaluation (tax-effected at the 22.5% Q2 rate): **≈$23.5B**, or **≈$2.16/sh — still +29% y/y**
- H1 2026 cumulative revaluation gain: **$62.81B** (vs just $0.09B in H1 2025)

**Actionable:** Treat GAAP EPS momentum as ~40% accounting, ~60% operating. Any screen or consensus built on reported EPS is overstating run-rate earnings power by roughly 55–60%.

---

## 2. Income statement — quarterly and year-to-date

### Q2 2026 vs Q2 2025 ($M)

| Line | Q2 2026 | Q2 2025 | Δ y/y | % of rev '26 |
|---|---|---|---|---|
| Revenue (derived) | **200,606** | 167,702 | **+19.6%** | 100.0% |
| Cost of goods & services | 95,778 | 80,809 | +18.5% | 47.7% |
| Gross profit | **104,828** | 86,893 | +20.6% | **52.3%** (vs 51.8%) |
| Marketing | 11,698 | 11,416 | +2.5% | 5.8% (vs 6.8%) |
| G&A | 2,788 | 2,965 | **−6.0%** | 1.4% (vs 1.8%) |
| D&A (total) | 19,988 | 15,227 | **+31.3%** | 10.0% (vs 9.1%) |
| SBC (allocated) | 6,038 | 6,534 | **−7.6%** | 3.0% |
| Total costs & expenses | 173,145 | 148,531 | +16.6% | 86.3% |
| **Operating income** | **27,461** | 19,171 | **+43.2%** | **13.7%** (vs 11.4%) |
| Interest income | 1,295 | 1,085 | +19.4% | |
| Interest expense | (1,314) | (516) | **+155%** | |
| Non-operating income, net | **53,396** | 1,686 | n.m. | |
| — *of which private-equity up-marks* | *50,486* | *49* | n.m. | |
| — *of which warrant FV loss* | *(1,449)* | *(590)* | | |
| — *of which marketable sec. gains* | *1,319* | *388* | | |
| Pretax income | **80,857** | 20,857 | +288% | |
| Tax | 18,199 | 2,678 | | **22.5%** eff. (vs 12.8%) |
| **Net income** | **62,647** | 18,164 | **+245%** | 31.2% |
| **Diluted EPS** | **$5.75** | $1.68 | +242% | |
| *Adj. EPS ex-private marks* | *≈$2.16* | *≈$1.68* | *≈+29%* | |

### H1 2026 vs H1 2025 ($M)

| Line | H1 2026 | H1 2025 | Δ |
|---|---|---|---|
| Revenue (derived) | **382,125** | 323,369 | **+18.2%** |
| COGS | 183,241 | 157,785 | +16.1% (GM 52.05% vs 51.21%) |
| Operating income | **51,313** | 37,576 | **+36.6%** |
| Operating margin | **13.4%** | 11.6% | +1.8 pt |
| Non-operating income | **69,378** | 4,960 | +1,299% |
| Pretax income | 120,691 | 42,536 | +183.8% |
| Income tax | 27,759 | 7,231 | eff. 23.0% vs 17.0% |
| Net income | **92,902** | 35,291 | +163.2% |
| Diluted EPS | **$8.53** | $3.27 | +161% |
| *Adj. EPS ex-marks* | *≈$4.06* | *≈$3.27* | *≈+24%* |

### Quarter-by-quarter bridge (implied Q1)

| Metric | Q1 2025 | Q1 2026 | Q2 2025 | Q2 2026 |
|---|---|---|---|---|
| Revenue | 155,667 | **181,519 (+16.6%)** | 167,702 | **200,606 (+19.6%)** |
| Operating income | 18,405 | 23,852 | 19,171 | 27,461 |
| Operating margin | 11.8% | 13.1% | 11.4% | **13.7%** |
| Net income | 17,127 | 30,255 | 18,164 | 62,647 |
| Private-stake up-mark (pretax) | ~0.04 | 12,328 | 0.05 | **50,486** |

**Read-through:** revenue growth is *accelerating* (16.6% → 19.6%) while margins *expand* — genuine operating leverage. Simultaneously, G&A and SBC are shrinking in absolute dollars and marketing is nearly flat — an unusual and highly favorable cost backdrop. Offsetting: **D&A grew 31% y/y, roughly 1.6x revenue growth** — the depreciation wave from the capex boom is arriving and is the main structural margin headwind into 2027.

---

## 3. Cash flow — record operating cash, but free cash flow has turned negative

### TTM (2025-07-01 → 2026-06-30) vs prior TTM

| Item ($M) | TTM Jun-26 | TTM Jun-25 | Δ |
|---|---|---|---|
| **Operating cash flow** | **161,403** | 121,137 | **+33.2%** |
| Purchases of productive assets (capex) | **(173,028)** | (107,656) | **+60.7%** |
| **Free cash flow (OCF − capex)** | **(11,625)** | **+13,481** | **negative swing** |
| Acquisitions, net of cash | (41,956) | (4,809) | +772% |
| Purchase of marketable securities | (72,902) | (46,731) | |
| Proceeds from sale/maturity of securities | 67,090 | 30,924 | |
| **Investing cash flow** | **(216,775)** | (123,569) | |
| LT debt issued | **81,925** | 746 | n.m. |
| ST debt issued, net of repay | 1,640 | 286 | |
| LT debt repaid | (5,022) | (7,434) | |
| **Financing cash flow** | **+75,160** | (8,652) | n.m. |
| D&A | **75,200** | 58,562 | +28.4% |
| SBC | 20,700 (H1'26 10,070 + H1'25 10,223 ≈ 20.3) | | |
| Cash taxes paid | 6,635 | 11,788 | **−44%** |
| Net change in cash | +19,474 | (10,220) | |

### Recent-run quarterly detail ($M)

| Item | Q2 2025 | Q1 2026 | Q2 2026 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|
| OCF | 32,515 | 26,032 | **45,387** | 49,530 | 71,419 |
| Capex | (32,183) | (44,203) | **(54,208)** | (57,202) | (98,411) |
| **FCF** | **+332** | **(18,171)** | **(8,821)** | **(7,672)** | **(26,992)** |
| Acquisitions | (1,700) | (15,408) | **(24,359)** | (1,652) | **(39,767)** |

**Insights:**
1. **OCF is running at a ~$161B TTM / ~$180B annualized pace and Q2 was a record $45.4B** (+40% y/y) — the core franchise is a cash machine.
2. **Capex is annualizing at ~$200B+** (Q2 alone $54.2B; H1 $98.4B, +72% y/y). Capex is now **~22% of revenue** vs ~15% a year ago. FCF is **structurally negative** for as long as this persists.
3. **The deficit is being debt-funded**, not equity-funded: **$81.9B of LT debt + $20.8B of ST debt issued in 12 months**, the largest borrowing program in company history. This is the single most important change in AMZN's capital structure.
4. **Cash taxes fell 44% y/y to $6.6B** while tax *expense* rose — deferred tax expense was **+$41.4B TTM / +$30.5B in H1 2026**. Reported earnings are increasingly tax-deferred; cash tax rate (~4% of pretax H1) is very low and likely to normalize upward.
5. Working capital became a drag: AR/other operating assets **−$21.4B** TTM, other non-current assets **−$17.8B**, accrued liabilities **−$6.1B**.

---

## 4. Balance sheet — bigger, more levered, more illiquid-asset-heavy

| Item ($M) | 2025-12-31 | 2026-06-30 | Δ |
|---|---|---|---|
| Cash & equivalents | 86,810 | 78,213 | −9.9% |
| AFS debt securities | 45,800 | **97,900** | +113.8% |
| **Cash + marketable securities** | **132,610** | **176,113** | **+32.8%** |
| Accounts receivable, net | 67,729 | 88,092 | **+30.1%** |
| Inventory, net | 38,325 | 38,184 | −0.4% |
| Current assets | 229,083 | 249,264 | +8.8% |
| **Equity securities w/o readily determinable FV** | **16,200** | **122,300** | **+655%** |
| **Total assets** | **818,042** | **1,095,689** | **+33.9%** |
| Accounts payable | 121,909 | 147,440 | +21.0% |
| Accrued liabilities | 75,520 | 73,406 | −2.8% |
| Current liabilities | 218,005 | 241,274 | +10.7% |
| LT debt — current | 2,748 | 3,330 | +21.2% |
| **LT debt — noncurrent** | **65,648** | **128,894** | **+96.3%** |
| **Total debt** | **68,396** | **132,224** | **+93.3%** |
| Operating lease liability | 89,252 | 96,320 | +7.9% |
| Finance lease liability | 12,286 | 13,451 | +9.5% |
| AOCI | +28,230 | **+66,287** | **+38,057** |
| Additional paid-in capital | 140,024 | 149,619 | +6.9% |
| Shares outstanding | 10,731 | **10,783** | +0.5% (dilution, no buyback) |
| Shares outstanding (7/22/26) | — | 10,786,313,572 | — |

### Derived balance-sheet metrics

| Metric | 2025-12-31 | 2026-06-30 |
|---|---|---|
| Current ratio | 1.051x | **1.033x** |
| Total debt / (cash + securities) | 0.52x | **0.75x** |
| Net debt / (net cash) | **net cash $64.2B** | **net cash $43.9B** |
| DSO (Q2 revenue basis) | n/a | **~40 days** (AR +30% vs rev +18.2% H1) |
| Total contractual obligations | — | **$650.0B** ($78.1B due <12 mo; $53.4B yr2; $46.8B yr3; $42.2B yr4) |
| Unrecognized SBC cost | — | $24.8B |
| Operating lease discount rate | 3.7% | 3.9% |

**Three balance-sheet signals a trader must not miss:**

1. **The $106B jump in "equity securities without readily determinable fair value" ($16.2B → $122.3B) is the source of the earnings story.** Part is new capital deployed, part is up-marking (+$62.8B in H1 charged through the income statement; +$50.5B in Q2 alone). These are **model-marked private assets** — they can be marked *down* just as easily, and they are the least liquid asset on the sheet.
2. **$38.1B of other comprehensive income in H1 2026** (vs $2.5B in H1 2025) drove AOCI from +$28.2B to +$66.3B. Note the return set shows only **$7M** of gross unrealized gain on AFS *debt* securities at 6/30/26 — so this OCI swing does **not** come from the bond portfolio and its precise source requires footnote verification. **Until verified, treat reported book-value growth as low-quality.**
3. **No buyback.** Shares outstanding *rose* 52M in six months despite $62.6B of quarterly net income — capital is being recycled into capex, M&A ($42.0B TTM) and private investments instead. Also note the $3.3B of debt maturing inside 12 months is trivial versus $176B of liquidity, so there is **no refinancing cliff**, only a rising interest burden (Q2 interest expense $1.31B, +155% y/y, annualizing ~$5.3B).

*Note: total stockholders' equity is not directly derivable from the returned line items (retained earnings is absent). Illustratively, H1 2026 comprehensive income of $131.0B plus $10.1B SBC, net of repurchases, implies a very large sequential increase in book value — flag as an estimate, not a filing figure.*

---

## 5. Profitability, leverage and quality scorecard

| Metric | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 | TTM Jun-26 |
|---|---|---|---|---|---|
| Revenue growth | — | **+19.6%** | — | **+18.2%** | — |
| Gross margin | 51.8% | **52.3%** | 51.2% | **52.1%** | — |
| Operating margin | 11.4% | **13.7%** | 11.6% | **13.4%** | — |
| Operating income growth | — | **+43.2%** | — | **+36.6%** | — |
| Net margin (reported) | 10.8% | **31.2%** | 10.9% | 24.3% | — |
| Net margin (ex-private marks) | ~10.8% | **~11.7%** | ~10.9% | **~11.6%** | — |
| Effective tax rate | 12.8% | **22.5%** | 17.0% | 23.0% | — |
| D&A / revenue | 9.1% | **10.0%** | 9.1% | 10.2% | — |
| Capex / revenue | 19.2% | **27.0%** | 17.7% | **25.8%** | ~22% |
| OCF / net income | 1.79x | 0.72x | 1.40x | 0.77x | 1.19x |
| OCF / adj. net income | — | **1.93x** | — | **1.62x** | 1.86x |
| Interest coverage (op income / interest exp.) | 37x | **21x** | 36x | 24x | — |
| Reported TTM diluted EPS | — | — | — | — | **≈$12.44** |
| **Adjusted TTM diluted EPS** | — | — | — | — | **≈$7.97** |

The OCF/NI collapse (1.79x → 0.72x) is *not* deteriorating cash conversion — it is the non-cash revaluation inflating the denominator. Against **adjusted** net income, cash conversion actually **improved to 1.93x**. That's the correct lens.

---

## 6. What a trader should do with this

**Bull case (evidence-based):**
- Revenue growth accelerating to +19.6% *with* 13.7% operating margins and G&A/SBC outright declining — this is the highest-quality operating quarter in the dataset.
- Q2 OCF $45.4B (+40%) and TTM OCF $161.4B (+33%) prove the core businesses (retail + AWS/AI) are compounding cash faster than ever.
- $176B of cash + securities and only 0.75x gross-debt coverage: ample firepower; the debt raise is opportunistic, not distress-driven.
- Adjusted EPS +29% y/y with a 23% tax rate — core earnings power is intact and under-appreciated by headline-focused screens.

**Bear case (evidence-based):**
- **FCF is negative: −$11.6B TTM, −$27.0B in H1.** Capex is running ~27% of Q2 revenue and rising. If AI-demand monetization slips, this becomes a de-rating catalyst rather than a growth investment.
- **Debt up 93% in six months (+$64B).** Net cash cushion has halved ($64B → $44B) in two quarters; at this pace net debt turns positive within ~2–3 quarters — a psychological regime change for a name that has been net-cash for years.
- **Earnings quality:** 57% of H1 pretax income and 66% of Q2 pretax income came from non-cash private-stake marks. Those marks are one-directional in the model until they aren't — reversal risk is asymmetric and unhedged.
- **Depreciation is compounding at ~1.6x revenue.** D&A/revenue moved 9.1% → 10.0% in a year; on $200B+ of annualized capex, that ratio likely keeps climbing — a mechanical drag on 2027 margins.
- **$650B of contractual obligations** ($78.1B inside 12 months) locks in the spend even if demand softens.
- **No capital returns**: share count is rising, so per-share compounding relies entirely on operating growth.

**Specific, actionable positioning insights:**
1. **Never trade AMZN off GAAP EPS this cycle.** Use **operating income (+43% y/y, 13.7% margin)** and **adjusted EPS (~$2.16 Q2, ~$4.06 H1)** as the anchors. If a beat is driven by revaluation again, fade the knee-jerk reaction; if it's driven by operating margin >13.5%, that's the durable signal.
2. **Watch FCF inflection as the swing factor.** The single most bullish datapoint would be capex growth decelerating below revenue growth. The single most bearish would be another quarter of $54B+ capex with negative FCF and another $15B+ of bond issuance.
3. **Monitor net debt.** Crossing from net cash to net debt is a concrete, checkable catalyst for multiple compression. Currently $43.9B net cash → ~3 quarters at the current burn.
4. **Scrutinize the AOCI/OCI line in the next 10-Q.** $38.1B of OCI in H1 2026 is unexplained by the disclosed AFS bond portfolio (only $7M gross unrealized gain). If that OCI is a fair-value mark on an equity stake routed through OCI, book value is materially mark-dependent.
5. **Interest expense trajectory** ($516M → $1,314M, +155%) is the tell on how much more debt is coming. Next print: any quarterly interest expense above ~$1.6B implies an acceleration of borrowing.
6. **Insider signal: unavailable.** Do not read management conviction into this report; the archive had no point-in-time insider data for AMZN as of 2026-08-04.

**Next catalysts:** Q3 2026 10-Q/earnings (expected late October 2026) — key debates will be (a) capex guidance, (b) AWS/AI revenue mix and margin, (c) D&A ramp, (d) any mark-down in private equity stakes, (e) further debt issuance. Also note the 3-reportable-segment structure (North America / International / AWS) disclosed for H1 2026 — segment disclosure detail was not included in the returned data.

---

## 7. Key points summary

| # | Category | Key finding | Value / evidence | Direction for AMZN | Trader implication |
|---|---|---|---|---|---|
| 1 | Growth | Revenue growth accelerated | Q2 2026 rev **$200.6B, +19.6% y/y** (Q1 +16.6%, H1 +18.2%) | **Bullish** | Strongest top-line print in dataset |
| 2 | Margins | Operating leverage intact | Op income **$27.46B, +43.2%**; margin **13.7%** vs 11.4% | **Bullish** | The real earnings driver |
| 3 | Cost control | G&A & SBC shrinking outright | G&A −6.0% y/y, SBC −7.6% y/y, marketing +2.5% | **Bullish** | Margin expansion is structural, not one-off |
| 4 | Earnings quality | GAAP EPS inflated by private-stake marks | **$50.5B Q2 / $62.8B H1** up-marks = 66% of Q2 pretax | **Bearish (quality)** | Reported EPS ≈$5.75 vs core ≈$2.16 |
| 5 | Cash generation | Operating cash flow at record | TTM OCF **$161.4B (+33%)**; Q2 $45.4B (+40%) | **Bullish** | Core franchise is a cash machine |
| 6 | Capex | Hyper-investment cycle | Capex TTM **$173.0B (+61%)**; Q2 $54.2B = 27% of rev | **Mixed→Bearish near term** | Explains margin/D&A risk |
| 7 | Free cash flow | FCF has turned negative | TTM **−$11.6B**; H1 **−$27.0B**; Q2 −$8.8B | **Bearish** | Key de-rating risk if persistent |
| 8 | Leverage | Debt nearly doubled in 6 months | Total debt **$68.4B → $132.2B (+93%)**; $81.9B LT issued TTM | **Bearish** | Net cash cushion halved to $43.9B |
| 9 | Liquidity | Still ample | Cash + securities **$176.1B** (+33%); current ratio 1.03x | **Bullish** | No refinancing cliff ($3.3B due <12mo) |
| 10 | Interest | Net interest tailwind gone | Interest exp. $1,314M (+155% y/y) ≈ interest income $1,295M | **Bearish (mild)** | Watch >$1.6B/qtr as borrowing tell |
| 11 | Depreciation | Capex depreciation wave arriving | D&A $19,988M **+31.3%** y/y; 10.0% of rev vs 9.1% | **Bearish (2027)** | Mechanical margin drag |
| 12 | M&A | Largest acquisition program ever | **$42.0B TTM**, incl. $24.4B in Q2, $39.8B H1 | **Mixed** | Integration + goodwill risk |
| 13 | Investments | Illiquid private book exploded | Equity sec. w/o RDFV **$16.2B → $122.3B** | **Bearish (opacity)** | Mark-down risk is asymmetric |
| 14 | Book value | Unexplained OCI surge | OCI **+$38.1B** H1'26 vs +$2.5B; AOCI $28.2B → **$66.3B** | **Verify** | Only $7M AFS bond gain disclosed — source unclear |
| 15 | Taxes | Cash tax rate unsustainably low | Cash taxes $6.6B TTM (−44%); deferred tax exp. +$41.4B TTM | **Bearish (mild)** | Normalization = EPS headwind |
| 16 | Capital returns | No buyback; dilution instead | Shares out 10,731M → **10,783M**; APIC +$9.6B | **Neutral** | Per-share compounding relies on ops |
| 17 | Obligations | Massive locked-in commitments | Contractual obligations **$650.0B** ($78.1B <12mo) | **Bearish (flexibility)** | Limits downside response options |
| 18 | Coverage | Interest coverage compressing | 37x → **21x** (Q2); 36x → 24x (H1) | **Neutral** | Still comfortable, trending the wrong way |
| 19 | Structure | 3 reportable segments | North America / International / AWS (H1 2026) | **Neutral** | Segment detail not in data pull |
| 20 | Insider data | **Unavailable** | Vendor: no point-in-time archive for AMZN by 2026-08-04 | **n/a** | Do not infer insider sentiment |
| 21 | Filing | Fresh, on-time disclosure | 10-Q accepted **2026-07-31 02:11 UTC** for period 6/30/26 | **Neutral** | All figures are point-in-time clean |
| 22 | **Net stance** | **Operating bull / accounting-and-capital-structure bear** | Op. income +43% & margins 13.7%, but FCF −$11.6B, debt +93%, 66% of Q2 pretax from non-cash marks | **Constructive on core, cautious on quality** | Anchor on operating income & adjusted EPS (~$2.16/qtr); treat revaluation-driven beats as fadeable; make capex deceleration the bull trigger and net-debt crossover the risk trigger |