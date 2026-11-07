# AMZN — Comprehensive Fundamental Report
**Analysis date: 2026-08-17 | Latest filing in cache: Form 10-Q for period ended 2026-06-30, EDGAR acceptance 2026-07-31 02:11 UTC (accn 0001018724-26-000026) | Prior 10-Q (period 2026-03-31) accepted 2026-04-30**

---

## 1. Executive summary — the six things that matter

1. **Revenue re-accelerated hard.** Q2 2026 (Apr–Jun) revenue was **$200.61B**, up **+19.6% YoY** from $167.70B, after **+16.6%** in Q1 2026. H1 2026 revenue **$382.13B, +18.2%**. (Revenue is derived as `CostsAndExpenses + OperatingIncomeLoss`, since the revenue tag is not in the cached fact set — see §11 caveat.)
2. **Operating margins expanded despite a large depreciation headwind.** Q2 2026 operating income **$27.46B (+43.2% YoY)**, margin **13.69% vs 11.43%** — a **+226bp** expansion *even though* D&A rose to **9.96% of revenue from 9.08%** (+130bp drag). H1 operating margin 13.43% vs 11.62%.
3. **Headline EPS is massively inflated by a non-cash private-stake markup.** H1 2026 pre-tax income of **$120.69B** includes **+$62.81B** of "upward price adjustments" on equity securities *without readily determinable fair value*, plus $1.30B FV gains and $1.32B marketable-security gains, less $1.45B warrant markdowns. That single line is **52% of H1 pre-tax income**. Reported Q2 diluted EPS **$5.75**; my **core (ex-markup) estimate is ~$2.16** (methodology in §5), still **+29% YoY**.
4. **Free cash flow is negative and worsening by design.** TTM (Jul-2025–Jun-2026) operating cash flow **$161.40B (+33% YoY)** against capex of **$173.03B (+61%)** → **FCF −$11.63B**, versus **+$13.48B** in the prior TTM period — a **$25.1B swing**. Q2 2026 alone: OCF $45.39B vs capex **$54.21B** → FCF −$8.82B; Q2 capex annualizes to ~$217B.
5. **The balance sheet changed character: debt nearly doubled.** Long-term debt **$132.995B vs $68.836B at 2025-12-31 (+93%)**; TTM LT debt issuance **$81.93B**. Interest expense **+155% YoY** in Q2 ($1.31B vs $0.52B). Total assets jumped **+33.9% to $1,095.7B** partly via **$39.77B of business acquisitions in H1 2026** (vs $1.65B in H1 2025).
6. **Leverage and liquidity are still comfortable.** Cash $78.21B + AFS debt securities $97.90B = **$176.11B** of liquid resources (vs $132.61B at YE25). Blended debt incl. leases ≈ **$242.8B** → **net debt ≈ $66.7B**, or roughly **0.4x TTM EBITDA (~$168B)**. Interest coverage >40x. Current ratio **1.03x** (thin, but structurally AP-funded).

**Bottom line:** AMZN's *operating* engine is accelerating (revenue +19.6%, core EPS +29%, margin +226bp, cash taxes nearly nil). The *reported* numbers are heavily flattered by a $62.8B non-cash private-asset revaluation, and the *cash* numbers are negative because of an unprecedented AI-infrastructure capex cycle funded increasingly with debt. This is a high-quality operating story wearing a low-quality earnings headline.

---

## 2. Company profile and reporting structure

- **Company:** Amazon.com, Inc. (ticker **AMZN**, US). Resolved identity confirmed against the cached SEC facts (CIK 0001018724 filings).
- **Segments:** `NumberOfOperatingSegments = 3` per the Q2 2026 10-Q (North America, International, Amazon Web Services).
- **Share structure:** $0.01 par; 100B shares authorized; **10,783M shares outstanding at 2026-06-30**; **10,786,313,572 as of 2026-07-22**; 11,298M issued (treasury method). APIC $149.62B; AOCI **+$66.29B** (up from $28.23B at YE25).
- **Dividends:** none — no dividend tags exist anywhere in the fact set. Capital return is zero; 100% of cash is reinvested.
- **Capital allocation:** capex (AI/datacenter/fulfillment) > M&A > debt service. No buyback evidence in the financing section (financing CF is dominated by debt issuance net of repayment).

---

## 3. Income statement — quarterly reconstruction

Because the "annual" and "quarterly" endpoints returned the same 10-Q-sourced fact set (no 10-K facts in cache), I reconstructed periods from the year-to-date and quarterly columns.

| $M | Q2 2025 | Q1 2026¹ | Q2 2026 | YoY (Q2) | H1 2025 | H1 2026 | YoY (H1) |
|---|---|---|---|---|---|---|---|
| Revenue (derived) | 167,702 | 181,519 | **200,606** | **+19.6%** | 323,369 | **382,125** | **+18.2%** |
| Cost of goods & services | 80,809 | 87,463 | 95,778 | +18.5% | 157,785 | 183,241 | +16.1% |
| COGS % of revenue | 48.19% | — | **47.74%** | −45bp | 48.79% | 47.95% | −84bp |
| Total costs & expenses | 148,531 | 157,667 | 173,145 | +16.6% | 285,793 | 330,812 | +15.8% |
| **Operating income** | **19,171** | **23,852** | **27,461** | **+43.2%** | **37,576** | **51,313** | **+36.6%** |
| Operating margin | 11.43% | 13.14% | **13.69%** | +226bp | 11.62% | 13.43% | +181bp |
| Non-operating income/(exp.) | 1,686 | 15,982 | **53,396** | nm | 4,960 | 69,378 | nm |
| Pre-tax income | 20,857 | 39,834 | **80,857** | +288% | 42,536 | 120,691 | +184% |
| Income tax | 2,678 | 9,560 | 18,199 | +580% | 7,231 | 27,759 | +284% |
| Effective tax rate | 12.84% | 24.0% | **22.51%** | +967bp | 17.00% | **23.00%** | +600bp |
| Equity-method loss | (15) | (19) | (11) | — | (14) | (30) | — |
| **Net income** | **18,164** | **30,255** | **62,647** | **+245%** | **35,291** | **92,902** | **+163%** |
| Diluted EPS | $1.68 | ~$2.78 | **$5.75** | **+242%** | $3.27 | $8.53 | +161% |
| Basic EPS | 1.71 | ~2.82 | 5.82 | +240% | 3.32 | 8.64 | +160% |
| Diluted shares (implied) | 10,812 | ~10,880 | ~10,895 | +0.8% | 10,793 | ~10,889 | +0.9% |

¹ Q1 2026 = H1 2026 minus Q2 2026. Q1 revenue = 157,667 + 23,852 = 181,519. Confirms Netflix-style clean arithmetic; all rows tie.

**Operating expense detail (H1, $M):**

| Line | H1 2025 | H1 2026 | Δ | % of rev H1'25 → H1'26 |
|---|---|---|---|---|
| COGS | 157,785 | 183,241 | +16.1% | 48.79% → 47.95% |
| Marketing | 21,179 | 22,012 | **+3.9%** | 6.55% → 5.76% |
| G&A | 5,593 | 5,375 | **−3.9%** | 1.73% → 1.41% |
| Share-based comp | 10,223 | 10,070 | **−1.5%** | 3.16% → 2.64% |
| D&A (total) | 29,489 | 38,933 | **+32.0%** | 9.12% → 10.19% |
| Operating lease cost | 6,666 | 8,035 | +20.5% | 2.06% → 2.10% |

**Read-through:** This is textbook operating leverage. Marketing grew 3.9%, G&A *shrank* 3.9%, and stock comp *shrank* 1.5% against 18.2% revenue growth — while the only inflation came from D&A (+32%) and lease cost (+20.5%), i.e., the capex bill arriving. The fact that margins still expanded 181bp tells you the revenue/mix improvement more than covered the depreciation ramp.

**Non-operating income bridge (Q2 2026, $M):**
- Upward price adjustment, equity securities without readily determinable FV: **+50,486**
- Equity securities FV-NI gains: +1,300
- Marketable securities unrealized gain: +1,319
- Interest income: +1,295
- Foreign currency gain: +227
- Interest expense: −1,314
- Warrant FV adjustment: −1,449
- (plus other, to reach) **= 53,396**

H1 2026 equivalent: non-marketable upward adjustment **+62,814** (Q1: +12,328, Q2: +50,486), equity FV +454, marketable +430, warrants −1,051, interest income +2,430, interest expense −2,114, FX +387.

---

## 4. Where the "growth" really comes from — segment/backlog proxies

The fact set does not carry segment revenue or AWS splits, so these are the best available proxies:

- **Deferred revenue (contract liabilities):** $25.00B total at 2025-12-31 ($20.576B current + $4.400B non-current) vs **$24.93B at 2026-06-30** ($20.428B + $4.500B) — **flat**. H1 2026 recognized **$15.2B** of revenue that was previously deferred. Flat deferred revenue alongside +18% revenue suggests backlog conversion is running at/above bookings pace rather than ballooning — a *strong* demand read for AWS-type contracts.
- **Remaining performance obligations / contractual obligations: $650.03B** at 2026-06-30. Maturity ladder: remainder of FY26 **$42.75B**; next 12 months **$78.08B**; year 2 **$53.41B**; year 3 **$46.77B**; year 4 **$42.22B**. This is a very long-dated commitment book (largely purchased capacity/content/energy) — supportive of future revenue but a hard obligation if demand softens.
- **Operating lease payments due: $116.35B** undiscounted ($9.34B remainder FY26; $14.77B next 12m; $13.92B yr2; $12.60B yr3; $11.27B yr4), carrying value **$96.32B** (discount rate 3.9%, up from 3.7% at YE25).
- **M&A:** H1 2026 business acquisitions **$39.77B** (Q1 $15.41B, Q2 **$24.36B**) vs $1.65B in H1 2025. Some of the +19.6% Q2 revenue growth and part of the +30% AR growth is inorganic — traders should not extrapolate the ~20% organic rate without checking the 10-Q business-combination footnote.

---

## 5. Earnings quality — the single most important analytical point

**Equity securities without readily determinable fair value:** **$16.2B at 2025-12-31 → $122.3B at 2026-06-30** (+$106.1B, +655%). Upward price adjustments booked to income: **$62.81B in H1 2026 ($50.49B in Q2 alone)** versus **$86M in H1 2025**.

This is a private-company stake (or stakes) being marked up 6.5x in six months. Consequences:

| | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 |
|---|---|---|---|---|
| Reported diluted EPS | $1.68 | $5.75 | $3.27 | $8.53 |
| Less non-marketable FV uplift (pre-tax, $M) | (49) | (50,486) | (86) | (62,814) |
| Non-operating income ex-uplift ($M) | 1,637 | 2,910 | 4,874 | 6,564 |
| **Core pre-tax income ($M)** | 20,808 | **30,371** | 42,450 | **57,877** |
| Core tax at period ETR → **core net income** | 18,136 | **23,537** | 35,219 | **44,558** |
| **Core diluted EPS (est.)** | **$1.68** | **$2.16** | **$3.26** | **$4.09** |
| **Core EPS growth** | — | **+28.6%** | — | **+25.4%** |

**Interpretation:** Roughly **62% of Q2 2026 reported EPS and 52% of H1 EPS is a non-cash private-asset revaluation**. The *operating* momentum is nonetheless genuinely excellent: core EPS +26–29% YoY is still an outstanding print for a company this size. But:

- **Reversal risk is real and asymmetric.** A $122.3B private mark now equals roughly **21% of implied book equity** (see §6). A 20% haircut would be a ~$24B pre-tax charge — larger than a full quarter of operating income.
- **The uplift is non-cash and untaxed-currently.** H1 2026 deferred income tax expense was **+$30.49B** (TTM $41.44B) — i.e., the tax on the markups is being deferred, creating a growing DTL. Cash taxes paid were only **$6.64B TTM** on TTM net income of $135.28B.
- **Cash-tax cliff.** Cash taxes have been running at ~5% of GAAP tax expense because of depreciation shields on the capex boom plus the mark-to-market deferral. As capex growth slows (it won't shrink) and the private marks eventually reverse or monetize, the cash tax rate normalizes toward the 22–24% GAAP rate. That is a multi-year headwind to EPS and FCF.
- **Data-quality flag:** `DebtSecuritiesAvailableForSaleUnrealizedGainLoss = $92.0B` for H1 2026 in the cache is **inconsistent** with the same filing's own maturity schedule showing only **$7M gross unrealized gains and $67M gross unrealized losses** at 6/30/26. Treat the $92B as a mis-scaled/mis-tagged value (probably ~$92M) and ignore it. AFS securities are marked essentially at par ($106.578B amortized vs $106.518B fair value).

---

## 6. Balance sheet — 2025-12-31 → 2026-06-30

| $M | 2025-12-31 | 2026-06-30 | Δ % |
|---|---|---|---|
| Cash & equivalents | 86,810 | 78,213 | −9.9% |
| AFS debt securities (fair value) | 45,800 | **97,900** | **+113.8%** |
| **Cash + securities** | **132,610** | **176,113** | **+32.8%** |
| Accounts receivable, net | 67,729 | 88,092 | **+30.1%** |
| — allowance for doubtful accounts | 2,400 | 2,800 | +16.7% (coverage 3.54% → 3.18%) |
| Inventory, net | 38,325 | 38,184 | −0.4% |
| — inventory valuation reserves | 3,300 | 3,000 | −9.1% |
| **Current assets** | 229,083 | 249,264 | +8.8% |
| Equity securities w/o readily det. FV | 16,200 | **122,300** | **+655%** |
| Operating lease ROU asset | 86,054 | 92,743 | +7.8% |
| Finance lease ROU asset, gross | 55,600 | 55,600 | 0.0% |
| **Total assets** | **818,042** | **1,095,689** | **+33.9%** |
| Accounts payable | 121,909 | 147,440 | +21.0% |
| Accrued liabilities | 75,520 | 73,406 | −2.8% |
| **Current liabilities** | 218,005 | 241,274 | +10.7% |
| Long-term debt — current | 2,748 | 3,330 | +21.2% |
| Long-term debt — non-current | 65,648 | 128,894 | **+96.4%** |
| **Total long-term debt** | **68,836** | **132,995** | **+93.2%** |
| Operating lease liabilities (total) | 89,252 | 96,320 | +7.9% |
| Finance lease liabilities (total) | 12,286 | 13,451 | +9.5% |
| AOCI | +28,230 | +66,287 | +134.8% |
| Additional paid-in capital | 140,024 | 149,619 | +6.8% |
| Shares outstanding (M) | 10,731 | 10,783 | +0.5% |

**Derived credit/liquidity metrics (2026-06-30):**

| Metric | Value | Comment |
|---|---|---|
| Current ratio | 249,264 / 241,274 = **1.03x** | Thin, but structurally funded by AP (≈$147B) |
| Tangible-ish funding vs obligations | Cash+AFS $176.1B | Covers current portion of all debt + finance leases comfortably |
| Total debt incl. leases | 132,995 + 96,320 + 13,451 = **$242.77B** | vs $170.37B at YE25 (+42.5%) |
| Net debt (debt incl. leases − cash & AFS) | **≈ $66.7B** | vs ≈$37.8B at YE25 |
| TTM EBITDA (op. inc. ~$92.7B est. + D&A $75.2B) | **≈ $167.9B** | Net debt/EBITDA ≈ **0.4x** |
| Net debt / TTM OCF ($161.4B) | **≈ 0.41x** | Comfortable |
| Implied book equity (assets − current liab − LT debt − non-current lease liabs − est. other non-current liab) | **≈ $570B** (estimate) | Book value/share ≈ **$53** |
| Private-stake mark as % of implied equity | **≈ 21%** | Concentration risk in book value |
| AR days (Q2 revenue basis) | ≈ 40 days (vs ≈37 on YE25/Q2 revenue basis) | AR +30% vs revenue +18% — mild watch item |
| Inventory vs revenue | Inventory flat, revenue +18% | Healthy turns/destocking |
| Debt / implied equity | ≈ 23% (43% incl. leases) | Still conservative for the asset base |
| Dilution | +0.5% in six months (~1%/yr) | Well contained vs 2.6% SBC/revenue |

**Interpretation:** Amazon traded a pristine, near-zero-net-debt balance sheet for a still-conservative but materially levered one, in order to fund AI capex and $40B of acquisitions. Leverage metrics remain unthreatening (0.4x net), but the *direction of travel* — debt +93%, interest expense +155% — is a genuine change in financial philosophy and deserves monitoring each quarter.

---

## 7. Cash flow statement — the capex story

| $M | TTM Jul'24–Jun'25 | TTM Jul'25–Jun'26 | Δ | H1 2025 | H1 2026 | Q2 2025 | Q2 2026 |
|---|---|---|---|---|---|---|---|
| **Operating cash flow** | 121,137 | **161,403** | **+33.3%** | 49,530 | 71,419 | 32,515 | 45,387 |
| Capex (productive assets) | 107,656 | **173,028** | **+60.7%** | 57,202 | 98,411 | 32,183 | **54,208** |
| **Free cash flow (OCF − capex)** | **+13,481** | **−11,625** | **−$25.1B** | −7,672 | **−26,992** | **+332** | **−8,821** |
| Capex % of revenue | — | ~high-20s | — | 17.7% | **25.8%** | 19.2% | **27.0%** |
| Business acquisitions, net | 4,809 | **41,956** | +772% | 1,652 | 39,767 | 1,700 | 24,359 |
| Purchases of marketable securities | 46,731 | 72,902 | +56% | 31,130 | 49,262 | 17,797 | 26,006 |
| Proceeds from sale/maturity of securities | 30,924 | 67,090 | +117% | 19,178 | 41,882 | 11,441 | 24,196 |
| **Investing cash flow** | −123,569 | **−216,775** | — | −69,227 | −143,457 | −39,424 | −79,245 |
| LT debt issued | 746 | **81,925** | nm | 746 | 66,998 | 0 | 13,557 |
| LT debt repaid | 7,434 | 5,022 | — | 2,751 | 2,752 | 2,751 | 2,752 |
| ST debt issued / (repaid) | 8,187 / (7,901) | 20,798 / (20,634) | — | 3,908 / (3,474) | 15,386 / (15,682) | 2,093 / (1,392) | 9,368 / (9,573) |
| **Financing cash flow** | −8,652 | **+75,160** | — | −2,586 | +62,913 | −2,539 | +10,146 |
| D&A (non-cash) | 58,562 | **75,200** | +28.4% | 29,489 | 38,933 | 15,227 | 19,988 |
| Deferred income tax expense | (2,407) | **+41,441** | nm | +518 | +30,489 | +11 | +17,691 |
| Income taxes paid, net | 11,788 | **6,635** | **−43.7%** | 5,638 | 3,978 | 4,761 | 2,655 |
| Operating lease payments | 13,485 | 15,522 | +15.1% | 7,320 | 7,804 | 3,758 | 3,489 |
| Finance lease principal | 1,556 | 1,599 | +2.8% | 821 | 863 | 411 | 395 |
| Finance lease interest | 284 | 339 | +19.4% | 143 | 187 | 72 | 85 |
| FX effect on cash | +864 | −314 | — | +1,424 | −54 | +1,008 | −53 |
| **Net change in cash** | −10,220 | **+19,474** | — | −20,859 | −9,179 | −8,440 | −23,765 |

**Cash-flow quality checks:**
- **OCF is real, but flattered by working capital.** Q2 2026 OCF $45.39B vs net income $62.65B: the gap is *entirely* the $50.49B non-cash markup, partially offset by $19.99B D&A and working-capital inflow. Adjusting net income for the markup gives ~$11–12B of "cash-ish" earnings + $19.99B D&A + $6.04B SBC ≈ $37B, consistent with the reported $45.4B once working capital is added. **Q2 OCF quality is good.**
- **Cash taxes are near zero relative to accounting taxes:** TTM $6.64B paid vs $48.1B total tax expense (TTM: 27,759 + ~20.3B from prior quarters). H1 2026 cash taxes *fell 29%* while pre-tax income tripled. This is a large, temporary, and reversible contributor to FCF and EPS.
- **Working capital was a net source in H1 2026:** AR/other operating assets −$13.95B (a use), accrued liabilities −$10.06B (a use), other non-current assets −$8.53B (a use), offset by AP growth (+$25.5B, implied by balance sheet). AP is doing the funding.
- **Q2 2026 cash fell $23.77B** despite +$10.15B financing inflow, because investing consumed $79.25B (incl. $54.21B capex and $24.36B M&A) and the securities portfolio was shifted ($97.9B AFS now sits outside "cash").

**The FCF inflection math:** TTM capex $173.0B against TTM D&A $75.2B means the asset base is growing ~$98B/yr. Depreciation is compounding at +32% YoY. If capex merely *stops growing* (flat ~$200–217B annualized), FCF stays negative; FCF turns positive only when capex/revenue declines toward the high-teens. **Do not model positive FCF for AMZN until capex growth decelerates below OCF growth.**

---

## 8. Capital structure, commitments and coverage

- **Debt raised with intent:** $81.93B of LT debt issued in TTM, $66.998B in H1 2026 alone. Against $5.02B repaid. This is the first genuine levering-up episode in Amazon's history at this scale.
- **Interest burden is tripling off a tiny base:** Q2 2026 interest expense $1,314M vs $516M (+155%); H1 $2,114M vs $1,057M (+100%). Net interest turned **negative (−$19M) in Q2 2026** for the first time, from +$569M a year ago. Coverage remains enormous (TTM EBITDA ≈ $167.9B / annualized interest ≈ $5.3B ≈ **32x**), but the trend line matters for the P&L.
- **Fixed obligations stack:** $650.0B total contractual obligations + $116.4B undiscounted operating leases + $16.7B undiscounted finance leases. Near-term (next 12 months) call on cash: **$78.1B of contractual obligations** + $14.8B operating lease + $1.8B finance lease ≈ **$94.7B** — comfortably covered by ~$161B TTM OCF, but it leaves little room for an OCF stumble while capex is running at $54B/quarter.
- **Off-balance-sheet exposure to watch:** the purchase commitments inside the $650B figure are largely take-or-pay style capacity/content/energy contracts. In a demand air-pocket, these convert from growth enablers to margin drags.
- **Energy/hedging:** derivative assets jumped to $705M from $112M; derivative liabilities $133M. The 10-Q discloses **270 million MWh** of non-monetary energy derivative notional for H1 2026 — a direct read on how central power procurement is to the AI buildout.

---

## 9. Insider transactions, governance, capital return

**Insider transaction data is unavailable.** The news-data vendor returned: *"the B-project data package has no authorized, point-in-time insider-transactions archive for AMZN by 2026-08-17."* I will not infer or fabricate insider activity. Traders should source Form 4s directly.

What the filings *do* tell us about insider-adjacent capital behavior:
- **Dilution is modest and decelerating:** shares outstanding 10,731M → 10,783M (+0.5% in six months, ~1.0%/yr), while SBC *fell* to 2.64% of revenue from 3.16%. Unrecognized SBC on the books: **$24.8B** (≈2.5 years of runway at current pace). This is genuinely shareholder-friendly relative to mega-cap tech peers.
- **No buyback, no dividend.** 100% of capital is being reinvested into capex and M&A. Shareholder return is entirely deferred and entirely dependent on the AI/cloud bet paying off.
- **AOCI is a swing factor:** +$66.29B at 6/30/26 from +$28.23B at YE25 — H1 comprehensive income of $130.96B vs net income of $92.90B, so **$38.1B of the equity build is non-income OCI** (partly FX: −$1.56B H1, but the bulk is unrealized securities/other). Book equity is therefore more volatile than the income statement alone implies.

---

## 10. What to trade on — catalysts, confirmations and risks

### Constructive evidence (bull case support)
1. **Growth is accelerating, not decelerating:** +16.6% (Q1) → **+19.6% (Q2)**. For a $800B+ revenue base, that is a rare re-acceleration.
2. **Margin expansion is broad-based and beats the depreciation drag:** COGS −84bp, marketing −79bp, G&A −32bp, SBC −52bp; net +181bp H1 despite D&A +107bp.
3. **Operating cash flow +33% TTM to $161.4B** and Q2 OCF $45.4B (+39.6% YoY) — the capex is being funded from genuine cash generation plus modest leverage, not from balance-sheet depletion.
4. **Liquidity up $43.5B in six months** (cash + AFS $132.6B → $176.1B) even after $54B of Q2 capex and $24B of M&A.
5. **Deferred revenue flat at $25.0B with +18% revenue** implies backlog is converting faster than it's accumulating — a positive demand signal.
6. **Zero dividend/buyback obligations** and only ~1% dilution means no capital-return constraint on the reinvestment thesis.
7. **Optionality on a $122.3B private-equity book:** if the underlying holding(s) IPO, the markup converts to real, monetizable value — a hard catalyst, not just an accounting entry. (The cached facts do not name the issuer; confirm in the 10-Q investments footnote.)

### Risk evidence (bear case support)
1. **Negative FCF is worsening:** −$11.6B TTM vs +$13.5B a year ago; H1 alone −$27.0B. Q2 annualized capex ≈ $217B. Any capex guide-up at the next print is an FCF-negative event.
2. **Earnings quality:** ~62% of Q2 EPS is a non-cash private valuation markup that can reverse. Mark-to-market reversals flow straight to EPS with no operating offset.
3. **Debt +93% and interest expense +155% in one year.** Net interest flipped negative. If rates stay high and the capex cycle extends, financing costs compound against a shrinking cash-tax shield.
4. **Cash-tax normalization:** TTM cash taxes of $6.6B on $135B of net income (≈4.9%) is unsustainable. Each 10pp step up toward the 22–24% GAAP rate costs roughly **$25–30B/yr of FCF**.
5. **AR +30% vs revenue +18%, with allowance coverage down 3.54% → 3.18%.** Mild collections/credit-quality warning.
6. **Current ratio 1.03x with $241B of current liabilities** — very little cushion if AP terms tighten or a supply shock hits.
7. **$650B of contractual obligations** are a fixed cost in a downturn, not a variable one.
8. **Concentration risk in book value:** the $122.3B private mark ≈ 21% of implied equity.

### Actionable setups
- **For fundamental longs:** the thesis is intact and arguably *strengthening* — own it for the operating leverage (margin +226bp, core EPS +29%), but size for the possibility of a markdown quarter. A "clean" quarter would be: revenue +18–20%, operating margin ≥13%, *and* capex growth decelerating. That combination is the single best long trigger.
- **For event/short-term traders:** the reported-vs-core EPS spread ($5.75 vs ~$2.16) is a **consensus-quality trap**. If the street's whisper number is built off headline EPS, an in-line-or-better headline with *no further* markup (i.e., the private stake simply holds flat) could read as a "miss" on any core-metric scrutiny, and vice versa. Trade the *core* number.
- **For credit/rates-oriented traders:** watch quarterly interest expense and total debt. Crossing ~$150–160B of LT debt or net debt/EBITDA above ~1.0x would mark a genuine regime change from "AWS-funded" to "levered-capex" Amazon.
- **What would flip me negative:** (a) capex guided *up* again while OCF growth decelerates below ~20%; (b) any write-down of the $122.3B equity-securities line; (c) cash taxes stepping up faster than revenue; (d) revenue growth reverting back below 15% with margins flat. None of these are in the Q2 data.
- **Next data points:** Q3 2026 10-Q (expected ~late October 2026). Focus on four lines: capex, interest expense, the equity-securities-without-FV balance, and cash taxes paid.

---

## 11. Methodology, provenance and data-quality caveats (read before trading)

1. **Vintage:** All facts are point-in-time SEC EDGAR facts by acceptance timestamp. The newest facts are from the **2026-07-31 02:11:13 UTC** 10-Q (Q2 2026). No post-quarter guidance, transcript, or price data is in this package.
2. **No 10-K / no full fiscal-year facts in cache.** Requesting `annual` frequency returned the same 10-Q fact set. Consequently I used the filing's own **TTM (2025-07-01 → 2026-06-30)** columns, which the 10-Q provides directly, for annualized/rolling metrics. Full FY2025 revenue and operating income are **not** directly available and are not asserted here.
3. **Revenue is derived,** not tagged: `Revenue = CostsAndExpenses + OperatingIncomeLoss`. This ties exactly to the reported operating income, pre-tax income and net income lines for every period, so I regard it as reliable — but it is a derived figure.
4. **No share price, market cap, P/E, EV/EBITDA or valuation multiples are computed** — there is no price data in the tool set. Any valuation work must be layered on separately (using the implied diluted share count of ~10,895M and implied book value/share of ~$53).
5. **No segment revenue, AWS margin, headcount, or geographic splits** are present in the cached facts; §4 uses contract-liability and contractual-obligation proxies instead. `NumberOfOperatingSegments = 3` is the only structural disclosure.
6. **Data anomaly flagged and excluded:** `DebtSecuritiesAvailableForSaleUnrealizedGainLoss` = $92.0B (H1 2026) contradicts the same filing's AFS maturity table ($7M gains / $67M losses at 6/30/26). Treated as a mis-scaled tag (~$92M) and excluded from all analysis in §5.
7. **Insider transactions: DATA_UNAVAILABLE** from the configured vendor. No inference made, none fabricated.
8. **Implied book equity (~$570B) is an estimate** — total liabilities are not a single tagged fact. It is computed as total assets less current liabilities, long-term debt, and non-current operating and finance lease liabilities, less an estimated ~$50B of other non-current liabilities calibrated to the 12/31/2025 balance-sheet structure. Treat book value per share (~$53) and ROE (~24% TTM) as approximations (±10%).

---

## 12. Key points at a glance

| Category | Metric | Latest value | Reference | Change | Signal |
|---|---|---|---|---|---|
| **Scale** | Revenue, Q2 2026 | $200.61B | $167.70B (Q2'25) | **+19.6%** | 🟢 Accelerating |
| | Revenue, Q1 2026 | $181.52B | $155.67B (Q1'25) | +16.6% | 🟢 |
| | Revenue, H1 2026 | $382.13B | $323.37B | +18.2% | 🟢 |
| **Profitability** | Operating income, Q2 2026 | $27.46B | $19.17B | +43.2% | 🟢 |
| | Operating margin, Q2 2026 | 13.69% | 11.43% | **+226bp** | 🟢 Strong |
| | Operating margin, H1 2026 | 13.43% | 11.62% | +181bp | 🟢 |
| | COGS % of revenue, H1 | 47.95% | 48.79% | −84bp | 🟢 |
| | D&A % of revenue, H1 | 10.19% | 9.12% | +107bp | 🟡 Capex drag |
| | Marketing growth (H1) | +3.9% | vs rev +18.2% | — | 🟢 Leverage |
| | G&A growth (H1) | −3.9% | vs rev +18.2% | — | 🟢 Leverage |
| | SBC % of revenue, H1 | 2.64% | 3.16% | −52bp | 🟢 Disciplined |
| **Earnings quality** | Reported diluted EPS, Q2 2026 | $5.75 | $1.68 | +242% | 🟡 Inflated |
| | **Core diluted EPS, Q2 2026 (est.)** | **$2.16** | $1.68 | **+28.6%** | 🟢 But real |
| | Core diluted EPS, H1 2026 (est.) | $4.09 | $3.26 | +25.4% | 🟢 |
| | Non-cash FV uplift, H1 2026 | **$62.81B** | $0.086B (H1'25) | nm | 🔴 52% of pre-tax |
| | Equity sec. w/o readily det. FV | **$122.3B** | $16.2B (YE25) | **+655%** | 🔴 Concentration |
| | Effective tax rate, H1 2026 | 23.00% | 17.00% | +600bp | 🟡 Normalizing |
| | Cash taxes paid, TTM | **$6.64B** | $11.79B (prior TTM) | −43.7% | 🔴 Unsustainable |
| | Deferred tax expense, TTM | $41.44B | −$2.41B (prior) | nm | 🔴 DTL build |
| **Cash generation** | Operating cash flow, TTM | **$161.40B** | $121.14B | **+33.3%** | 🟢 |
| | Operating cash flow, Q2 2026 | $45.39B | $32.52B | +39.6% | 🟢 |
| | Capex, TTM | **$173.03B** | $107.66B | **+60.7%** | 🟡 |
| | Capex, Q2 2026 | **$54.21B** (≈$217B annualized) | $32.18B | +68.4% | 🟡 |
| | **Free cash flow, TTM** | **−$11.63B** | +$13.48B | **−$25.1B** | 🔴 Negative |
| | Free cash flow, H1 2026 | −$26.99B | −$7.67B | −$19.3B | 🔴 |
| | Capex % of revenue, H1 | 25.8% | 17.7% | +810bp | 🔴 |
| | Business acquisitions, H1 2026 | $39.77B | $1.65B | +2,307% | 🟡 Inorganic mix |
| **Balance sheet** | Total assets | **$1,095.69B** | $818.04B (YE25) | **+33.9%** | 🟢 |
| | Cash + AFS securities | $176.11B | $132.61B | +32.8% | 🟢 |
| | Total long-term debt | **$133.00B** | $68.84B | **+93.2%** | 🔴 Rapid |
| | LT debt issued, TTM | $81.93B | $0.75B | nm | 🔴 New regime |
| | Operating + finance leases | $109.77B | $101.54B | +8.1% | 🟡 |
| | Total debt incl. leases | $242.77B | $170.37B | +42.5% | 🟡 |
| | Net debt (incl. leases) | ≈$66.7B | ≈$37.8B | +76% | 🟢 Still low |
| | Net debt / TTM EBITDA | **≈0.4x** | — | — | 🟢 Comfortable |
| | Interest expense, Q2 2026 | $1,314M | $516M | **+155%** | 🔴 Trending |
| | Net interest income, Q2 2026 | **−$19M** | +$569M | flip to negative | 🔴 Milestone |
| | Current ratio | 1.03x | 1.05x | −2bp | 🟡 Thin |
| | AR growth vs revenue growth | +30.1% vs +18.2% | — | — | 🟡 Watch |
| | AR allowance coverage | 3.18% | 3.54% | −36bp | 🟡 |
| | Inventory change | −0.4% | vs rev +18.2% | — | 🟢 Efficient |
| | Dilution, 6 months | +0.5% | — | ~1%/yr | 🟢 Contained |
| | Unrecognized SBC | $24.8B | — | — | 🟢 ~2.5yr runway |
| **Obligations** | Total contractual obligations | **$650.03B** | — | — | 🟡 Long-dated lock-in |
| | Contractual obligations, next 12m | $78.08B | — | — | 🟢 Covered by OCF |
| | Operating lease payments due | $116.35B | $106.91B (YE25) | +8.8% | 🟡 |
| | Deferred revenue (contract liab.) | $24.93B | $25.00B | −0.3% | 🟢 Converting fast |
| | Deferred revenue recognized in H1 | $15.20B | — | — | 🟢 |
| | Energy derivative notional, H1 | 270 million MWh | — | — | 🟡 Power intensity |
| **Capital return** | Dividend | **None** | None | — | 🟡 Zero |
| | Buyback | **None observed** | None | — | 🟡 Zero |
| **Governance** | Insider transactions | **DATA UNAVAILABLE** | — | — | ⚪ Not assessable |
| **Segments** | Operating segments | 3 | 3 | — | ⚪ No detail |
| **Valuation** | Price / multiples | **Not computable** (no price data) | — | — | ⚪ Out of scope |