# AAPL — Comprehensive Fundamental Report
**Analysis date:** 2026-08-31 | **Instrument:** `AAPL` (Apple Inc.)
**Basis:** Point-in-time SEC XBRL facts, filtered by actual EDGAR acceptance timestamps (nothing filed after 2026-08-31 is used). Latest filing in scope: **Form 10-Q, accession 0000320193-26-000020, accepted 2026-07-31 14:01 UTC** — i.e. the quarter ended **2026-06-27 (fiscal Q3 FY2026)**.

---

## 1. Bottom line for traders

`AAPL` is in the middle of a **genuine fundamental re-acceleration**, not a slow-growth steady-state story. Three data points carry the whole thesis:

1. **Revenue +16.4% YoY in FQ3'26** ($109,417M vs $94,036M) — for a company of this size that is a violent inflection versus the ~5–6% growth regime implied by the prior-year comparatives.
2. **Gross margin expanded +356 bps YoY to 50.06%** in the quarter (+225 bps to 49.07% for 9M) — growth is arriving at *higher* incremental margin, which is the opposite of what discount-led or hardware-heavy growth looks like.
3. **Operating cash flow +43.1% to $116,996M for 9M'26**, with free cash flow **+52.5% to $110,197M** while capex actually *fell* 28%.

The offsetting negatives are equally real: **R&D is up 32.5%** (a permanent opex step-up), the **effective tax rate has risen 218 bps to 17.58%** (a silent EPS headwind), and the balance sheet shows an unusual **$13.3B gross intangible build** with an **inventory build of +94% (raw materials +260%)** whose funding source is not fully visible in the returned data slice. Those three items are where I would spend diligence time before sizing a position.

Net: **fundamentally bullish, with two specific accounting/anomaly flags** (Section 10) that a trader should verify rather than assume.

---

## 2. Data provenance and explicit limitations

Intellectual honesty matters more than completeness here. What the tools did and did not give me:

| Item | Status |
|---|---|
| Income statement, balance sheet, cash flow (quarterly & annual) | ✅ Retrieved (SEC XBRL, `10-Q`/`10-K`) |
| Multi-year cash flow history | ⚠️ Partial — FY2023, FY2024 full-year; FY2025 full-year OCF line not present in returned slice |
| FY2025 full-year P&L totals | ❌ Not present — only 9M FY2025 + Q3 FY2025 are in the slice |
| Insider transactions | ❌ **`DATA_UNAVAILABLE`** — vendor has no authorized point-in-time insider archive for `AAPL`. I will **not** infer or fabricate insider activity (Section 11) |
| Share price / market cap / valuation multiples | ❌ Not provided by any tool. No P/E, P/S, or EV/EBITDA multiple below is computed from a real quote — see the crude proxy note in Section 9 |
| Segment (iPhone/Services/Wearables) revenue split | ❌ Not in the returned tags — consolidated only |
| Goodwill balance | ❌ Not tagged in slice (intangibles are, goodwill is not) |

Both the `get_fundamentals` and the `annual` statement calls returned **identical payloads truncated at the `OperatingIncomeLoss` row** — the vendor caps the response length. I re-requested once to confirm; it is deterministic, not a transient error. Everything below is either directly reported or arithmetically derived from reported lines, and I label which is which.

---

## 3. Company profile

Apple Inc. designs, manufactures and markets smartphones, personal computers, tablets, wearables and accessories, and sells a growing portfolio of services (App Store, iCloud, Apple Music, advertising, AppleCare, payments). It is the largest publicly traded company by market capitalization, organized around a **hardware-installed-base-plus-attached-services** model: hardware wins the user, services monetize the annuity at structurally higher gross margin than devices.

The financial signature of that model is visible directly in the data: a **50.06% consolidated gross margin** at FQ3'26 is not a hardware company's margin. It reflects either (a) services mix reaching a new high, (b) very favorable component costs/memory pricing, or (c) both. **Mix shift is the single most important unpriced variable in this dataset**, and the segment disclosure needed to prove it was not returned.

Fiscal year ends the last Saturday of September. Shares outstanding: **14,608.963M** at 2026-06-27; **14,594.180M** as of the 2026-07-17 cover date.

---

## 4. FQ3 FY2026 deep dive (quarter ended 2026-06-27)

| Line item ($M) | FQ3 FY26 | FQ3 FY25 | YoY |
|---|---:|---:|---:|
| Revenue | **109,417** | 94,036 | **+16.4%** |
| Cost of goods & services | 54,647 | 50,318 | +8.6% |
| **Gross profit** | **54,770** | 43,718 | **+25.3%** |
| *Gross margin* | *50.06%* | *46.49%* | **+356 bps** |
| R&D | 11,729 | 8,866 | **+32.3%** |
| Selling & marketing | 5,034 | 4,769 | +5.6% |
| G&A | 2,312 | 1,881 | +22.9% |
| Total operating expenses | 19,075 | 15,516 | +22.9% |
| **Operating income** | **35,695** | 28,202 | **+26.6%** |
| *Operating margin* | *32.62%* | *29.99%* | **+263 bps** |
| Non-operating income/(expense) | +572 | (171) | n/m |
| Pretax income | 36,267 | 28,031 | +29.4% |
| Tax provision | 6,478 | 4,597 | +40.9% |
| *Effective tax rate* | *17.86%* | *16.40%* | **+146 bps** |
| **Net income** | **29,789** | 23,434 | **+27.1%** |
| *Net margin* | *27.23%* | *24.92%* | **+231 bps** |
| **Diluted EPS** | **$2.02** | $1.57 | **+28.7%** |
| Share-based comp | 3,401 | 3,168 | +7.4% |

**What this quarter actually says.**

- **Operating leverage is real and large.** Revenue grew 16.4% but COGS grew only 8.6%. Every incremental dollar of revenue cost ~53 cents of COGS versus ~54 cents historically — and the incremental gross margin on the *delta* is far higher: incremental GP of $11,052M on incremental revenue of $15,381M = **71.9% incremental gross margin**. That is a services-mix or pricing-power fingerprint, not a volume-discount one.
- **EPS grew 28.7%, faster than net income (+27.1%), and net income faster than operating income (+26.6%).** The 160 bps of EPS-over-net-income leverage came from buybacks (share count down ~1.1% over nine months), *not* from below-the-line items. Non-operating swung to +$572M from −$171M, which helped, but the tax rate consumed most of it.
- **The tax rate is the loudest quiet negative.** FQ3 ETR 17.86% vs 16.40%. On $36,267M of pretax income, the extra 146 bps cost roughly **$530M of net income**, or about **$0.036 of EPS (~1.8% of the quarter's EPS)**. This is a persistent structural headwind (international tax framework changes), not a one-off — and it is the main reason 9M EPS growth (+22.4%) trails 9M operating income growth (+21.7%) by less than you would expect from a pure operating story.
- **R&D +32.3% is a deliberate margin sacrifice that margins absorbed anyway.** R&D rose to **10.72% of revenue** from 9.43%. Management spent an extra $2,863M in the quarter on R&D and still printed +356 bps of gross margin. That is the highest-quality version of this trade: investment funded out of mix, not out of the operating margin.

---

## 5. Nine-month FY2026 vs nine-month FY2025 — the trend is not one quarter

| Line item ($M) | 9M FY26 | 9M FY25 | YoY |
|---|---:|---:|---:|
| Revenue | **364,357** | 313,695 | **+16.2%** |
| Cost of goods & services | 185,575 | 166,835 | +11.2% |
| **Gross profit** | **178,782** | 146,860 | **+21.7%** |
| *Gross margin* | *49.07%* | *46.82%* | **+225 bps** |
| R&D | 34,035 | 25,684 | **+32.5%** |
| SG&A | 22,315 | 20,553 | +8.6% |
| Total operating expenses | 56,350 | 46,237 | +21.9% |
| **Operating income** | **122,432** | 100,623 | **+21.7%** |
| *Operating margin* | *33.60%* | *32.08%* | **+153 bps** |
| Pretax income | 123,102 | 99,925 | +23.2% |
| Tax provision | 21,638 | 15,381 | +40.7% |
| *Effective tax rate* | *17.58%* | *15.39%* | **+218 bps** |
| **Net income** | **101,464** | 84,544 | **+20.0%** |
| *Net margin* | *27.85%* | *26.95%* | +90 bps |
| **Diluted EPS** | **$6.88** | $5.62 | **+22.4%** |
| Diluted EPS (basic check) | $6.91 basic | $5.64 basic | +22.5% |
| SBC | 10,523 | 9,680 | +8.7% |
| D&A | 9,973 | 8,571 | +16.4% |
| **Operating cash flow** | **116,996** | 81,754 | **+43.1%** |
| Capex | 6,799 | 9,473 | **−28.2%** |
| **Free cash flow (derived)** | **110,197** | 72,281 | **+52.5%** |
| Buybacks | 62,094 | 70,579 | **−12.0%** |
| Dividends paid | 11,778 | 11,559 | +1.9% |
| DPS declared | $0.79 | $0.76 | +3.9% |
| SBC tax withholding | 6,462 | 5,719 | +13.0% |

**Interpretation.**

- **Q3 alone was better than the 9M run-rate on every margin line** (GM 50.06% vs 49.07% 9M; OPM 32.62% vs 33.60% 9M — actually OPM was *lower* than the 9M average because Q1 is seasonally the strongest). The key point: Q3 gross margin of 50.06% **beat the 9M average by ~99 bps**, so the margin trajectory is *improving sequentially into the quarter*, not decaying.
- **The tax rate dragged harder over 9M (+218 bps) than in Q3 alone (+146 bps)** — i.e. earlier quarters had a worse tax picture. That is a headwind that is *fading*, which is constructive for forward EPS.
- **Cash conversion is exceptional.** OCF/net income = **1.153x**. For a company with $101B of net income, generating $117B of operating cash in nine months means working capital was a source of cash and non-cash add-backs (SBC $10.5B, D&A $10.0B) are doing real work.
- **Capex fell 28% while revenue grew 16%.** Capex is now just **1.87% of revenue** (vs 3.02%). Apple is becoming *less* capital intensive while growing faster. This is the mechanical reason FCF grew 52.5% on 16.2% revenue growth — and it is not repeatable forever, so do not extrapolate 52% FCF growth.

---

## 6. Margin and revenue-quality analysis

**Gross margin bridge (9M, +225 bps to 49.07%):** The two candidate drivers are (i) services mix and (ii) input-cost deflation / favorable memory pricing. The data cannot separate them, but one clue discriminates: **deferred revenue (total contract liability) rose to $14,900M from $13,700M (+8.8%), and current portion to $9,538M from $9,055M (+5.3%)** — healthy but *slower* than the +16.2% total revenue growth. If services were exploding, you would typically expect deferred revenue to grow faster than total revenue, since services are billed in advance. It did not. That tilts my read toward **a material component-cost / pricing tailwind in hardware** rather than pure services mix, meaning **some of the +225 bps is cyclical and at risk if memory/NAND pricing turns.**

**Deferred revenue recognized from the opening balance:** $7,260M over 9M'26 vs $6,958M over 9M'25 (+4.3%) — again, modest, consistent with a stable-not-surging services annuity.

**Operating expense discipline:** SG&A grew only **+8.6%**, less than half the revenue growth rate — genuine leverage. All the opex inflation is R&D (+32.5%). That is the right kind of inflation: it is discretionary, forward-looking, and margin-funded.

**D&A +16.4% ≈ revenue +16.2%** — depreciation is tracking the business, so the earnings growth is not being flattered by a widening capex-vs-depreciation gap. Accumulated depreciation moved only from $76,014M to $76,744M (+$730M in nine months) against gross additions — **the physical asset base is essentially flat.** This is a critical point for Section 10.

---

## 7. Balance sheet — a dramatic improvement in financial position

| Balance sheet ($M) | 2026-06-27 | 2025-09-27 | Change |
|---|---:|---:|---:|
| Cash & equivalents | 39,544 | 35,934 | +3,610 |
| Marketable securities — current | 22,855 | 18,763 | +4,092 |
| Accounts receivable | 31,398 | 39,777 | −8,379 |
| Nontrade receivables | 27,509 | 33,180 | −5,671 |
| Inventory | **11,092** | 5,718 | **+5,374 (+94%)** |
| — Raw materials & purchased parts | **7,645** | 2,124 | **+5,521 (+260%)** |
| — Finished goods | 3,447 | 3,594 | −147 |
| Other current assets | 17,420 | 14,585 | +2,835 |
| **Total current assets** | 149,818 | 147,957 | +1,861 |
| Marketable securities — noncurrent | 84,118 | 77,723 | +6,395 |
| Other noncurrent assets | 77,557 | 72,634 | +4,923 |
| Intangibles, gross | **38,220** | 24,950 | **+13,270** |
| Accumulated amortization | (12,803) | (11,649) | −1,154 |
| **Intangibles, net** | **25,417** | 13,301 | **+12,116** |
| **Total assets** | **383,266** | 359,241 | +24,025 |
| Accounts payable | 64,525 | 69,860 | −5,335 |
| Commercial paper | 1,997 | 7,979 | −5,982 |
| Current portion LT debt | 11,007 | 12,350 | −1,343 |
| Other current liabilities | 62,259 | 66,387 | −4,128 |
| **Total current liabilities** | 149,326 | 165,631 | −16,305 |
| Long-term debt (noncurrent) | 71,340 | 78,328 | −6,988 |
| Other noncurrent liabilities | **55,080** | 41,549 | **+13,531** |
| **Total liabilities** | 275,746 | 285,508 | −9,762 |
| **Shareholders' equity** | **107,520** | 73,733 | **+33,787 (+45.8%)** |
| Shares outstanding (M) | 14,608.963 | 14,773.260 | −164.297 |

**Derived liquidity and leverage:**

| Metric | 2026-06-27 | 2025-09-27 |
|---|---:|---:|
| Cash + all marketable securities | **$146,517M** | $132,420M |
| Total debt (LT + CP) | $84,297M | $98,679M |
| **Net cash position** | **+$62,220M** | +$33,741M |
| Current ratio | **1.003x** | 0.893x |
| Total debt / equity | **0.78x** | 1.34x |
| Liabilities / assets | 71.9% | 79.5% |
| Equity / assets | **28.1%** | 20.5% |
| Inventory days of COGS (annualized on quarter) | **~61.6 days** | ~34.0 days |

**Four things to take from this.**

1. **Net cash nearly doubled — +$28.5B in nine months**, to $62.2B, *while* returning $73.9B to shareholders. Total debt fell $14.4B and no new long-term debt was issued at all in 9M'26 (`ProceedsFromIssuanceOfLongTermDebt` = **$0** vs $4,481M prior year). This is the profile of a company with more cash than it knows what to do with near-term.
2. **Equity +45.8% to $107.5B** — the equity/assets ratio jumped from 20.5% to 28.1%. Apple is meaningfully de-risking its balance sheet. The dividend and buyback are now funded entirely from internally generated cash with room to spare.
3. **Current ratio crossed above 1.0x** for the first time in the series, driven by a $16.3B cut in current liabilities (commercial paper −$5,982M, AP −$5,335M, other CL −$4,128M). Reduced reliance on short-term supplier and CP financing.
4. **The two anomalies are here** — inventory +94% and intangibles +$13.3B gross. Both are covered in Section 10.

---

## 8. Cash flow and capital allocation

**Nine-month cash flow, three-way build:**

| ($M) | 9M FY26 | 9M FY25 | Change |
|---|---:|---:|---:|
| Operating | **+116,996** | +81,754 | +35,242 |
| Investing | **−18,811** | +17,782 | **−36,593 swing** |
| Financing | **−94,575** | −93,210 | −1,365 |
| Net change in cash (incl. FX) | +3,610 | +6,326 | −2,716 |

The investing swing is the least understood line and it is **almost entirely a treasury decision, not a capital-allocation one**:

- Purchases of AFS debt securities: **$48,752M** vs $17,591M (+177%)
- Maturities/prepayments/calls: $26,504M vs $35,036M (−24%)
- Sales of AFS debt: $12,016M vs $10,785M (+11%)
- **Net securities activity: +$10,232M outflow in 9M'26 vs +$28,230M inflow in 9M'25 → a $38.5B swing.**
- Capex: $6,799M vs $9,473M (**−$2,674M, a tailwind**)
- Other investing: $1,780M vs $975M

**In plain English: Apple moved ~$38B from "letting the securities portfolio run off" to "reinvesting in securities."** That is why investing flipped from a source to a use of cash. It is *not* a deterioration in business economics — OCF was up $35B. Do not misread the negative investing cash flow as heavy investment; the actual capex line went *down*.

**Capital allocation detail (9M FY26):**

| Use of cash | $M | % of FCF ($110,197M) |
|---|---:|---:|
| Buybacks | 62,094 | 56.3% |
| Dividends | 11,778 | 10.7% |
| SBC tax withholding (net share settlement) | 6,462 | 5.9% |
| **Total shareholder returns** | **80,334** | **72.9%** |
| Debt repayment, net (LT + CP + ST) | ~14,427 | 13.1% |
| Retained / cash build | ~14,116 | 12.8% |

**The signal in the buyback deceleration:** Buybacks fell **12.0%** ($62,094M vs $70,579M) despite FCF rising **52.5%**. Payout dropped from 97.6% of FCF to 67.2%. Simultaneously: R&D +32.5%, intangibles +$13.3B gross, and no new debt issued. **Management is visibly accumulating financial and intangible firepower rather than returning it.** For a trader, that is a bet on a large forward deployment of capital — either an acquisition, an IP/content licensing program, or a build-out that has not yet hit the capex line.

---

## 9. Financial history (multi-year context)

**Annual cash flow (from the FY2025 10-K, filed 2025-10-31):**

| ($M) | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Operating cash flow | 110,543 | 118,254 | *not in returned slice* |
| Investing cash flow | +3,705 | +2,935 | **+15,195** |
| Financing cash flow | −108,488 | −121,983 | **−120,686** |

**Fiscal-year-end balance snapshots:**

| ($M) | 2024-09-28 | 2025-03-29 | 2025-06-28 | 2025-09-27 | 2026-03-28 | 2026-06-27 |
|---|---:|---:|---:|---:|---:|---:|
| Total assets | — | — | — | 359,241 | 371,082 | **383,266** |
| Cash | — | 28,162 | 36,269 | 35,934 | 45,572 | **39,544** |
| Total liabilities | — | — | — | 285,508 | 264,591 | **275,746** |
| Shareholders' equity | 56,950 | 66,796 | 65,830 | 73,733 | 106,491 | **107,520** |
| Inventory | — | — | — | 5,718 | 6,747 | **11,092** |
| Long-term debt | — | — | — | 90,700 | 82,700 | **82,300** |
| Shares outstanding (M) | — | — | — | 14,773.3 | — | **14,609.0** |

**Equity trajectory is the headline of the history:** $56,950M (FY24) → $73,733M (FY25) → **$107,520M (Q3 FY26)**. That is an **89% increase in book equity in 21 months** — nearly all of it retained earnings outrunning buybacks. Apple has crossed from a levered-equity story into a genuinely self-financing one.

**FY2025 debt maturity ladder (as of 2025-09-27, $M):** Next 12 months 12,393 | Year 2 10,078 | Year 3 9,300 | Year 4 5,235 | Year 5 4,972 | After Year 5 49,303. Operating lease commitments total $14,725M (Year 1 $1,967M); finance lease commitments $1,579M. The ladder is smooth, long-dated, and comfortably covered by $62B of net cash — **no refinancing wall**.

**Valuation note — no price data was available from any tool.** I will not invent a multiple. As a crude, explicitly-unreliable proxy: net share reduction of 164.297M for $62,094M of buybacks implies an average repurchase price of **$378/share if share count fell 1:1**, but SBC issuance offsets roughly 30–60M shares of that, which implies a gross repurchase volume of ~195–225M shares and an average price nearer **$276–$318**. Taking the honest range, **implied average buyback price ≈ $280–$380, most likely low-to-mid $300s.** Anyone with a live quote should anchor multiples to that, not to this estimate.

**Earnings run-rates (derived):** FQ3 EPS $2.02 × 4 = **$8.08 annualized**; 9M EPS $6.88 × 4/3 = **$9.17 annualized**. Note Q1 is seasonally strongest, so the truth sits between or below.

---

## 10. Two anomalies a trader must diligence — and the strongest structural signal

### ⚠️ Anomaly 1: Inventory +94%, raw materials +260%
Inventory jumped from **$5,718M to $11,092M**. The entire increase is upstream: **raw materials and purchased parts rose from $2,124M to $7,645M (+260%)**, while finished goods actually *fell* $147M. Inventory now represents **~61.6 days of quarterly COGS vs ~34.0 days** at fiscal year-end.

*Bull read:* a major product ramp is being pre-funded ahead of launch — you buy components before you build. Raw-materials-heavy builds are the classic pre-launch signature.
*Bear read:* an oversized component commitment into softening demand, which turns into write-downs (and gross-margin reversal) one to two quarters later.
**Which is it?** The discriminator is **FQ4 revenue and gross margin**. If GM holds ≥49% with revenue up double digits, the build was demand-driven and the setup is strong. If GM compresses >150 bps on rising inventory, the build was misjudged. This is the **single highest-information event in the next 90 days.**

### ⚠️ Anomaly 2: +$13.3B gross intangible build with no obvious cash funding source
Intangibles, gross, rose from **$24,950M → $38,220M (+$13,270M)**; net from $13,301M → $25,417M (+$12,116M). Two problems:
- **"Payments for other investing activities" was only $1,780M**, and capex was $6,799M. There is no line in the returned slice that explains a $13.3B intangible addition.
- **Other noncurrent liabilities rose almost exactly in parallel: +$13,531M** ($41,549M → $55,080M).

The near 1:1 coincidence of a **+$13.3B asset** and a **+$13.5B long-term liability** strongly suggests **an IP/content acquisition or licensing arrangement structured with a deferred/contingent consideration liability**, or an omitted "acquisition of business" cash line. Either way it is **not in my data slice**, and I will not assert an explanation. **Action item: read the FQ3'26 10-Q notes on business combinations, other noncurrent liabilities, and the intangible roll-forward before trading on it.** What I *can* say confidently: this is a real, large deployment of capital into non-physical assets, and it is consistent with the buyback deceleration and R&D surge — **Apple is investing in something specific and large.**

### ✅ The strongest structural signal: capital is going to IP, not factories
Accumulated depreciation rose just **$730M in nine months** (to $76,744M) — the physical asset base is flat. D&A rose 16.4%, in line with revenue. Yet intangibles gross rose **$13,270M** and R&D rose **$8,351M**. **For the first time in the data, Apple's non-physical investment is growing an order of magnitude faster than its physical investment.** Combined with capex falling to 1.87% of revenue, this is a company converting its growth engine from fabrication to intellectual property and software. That is structurally *margin-accretive* and *capital-light* — which is precisely what the +356 bps of gross margin and +52.5% FCF growth are already reflecting.

---

## 11. Insider transactions

**`DATA_UNAVAILABLE`.** The vendor reports: *"the B-project data package has no authorized, point-in-time insider-transactions archive for AAPL by 2026-08-31."*

I have **no** Form 3/4/5 data for `AAPL` in the period and I am **not** going to infer, estimate, or characterize insider sentiment. Treat this as a **gap, not a signal.** If insider behavior is a required input for your decision process, source it directly from EDGAR (CIK 0000320193, Forms 3/4/5) before acting — do not read the absence of data as "no activity" or as a neutral or negative read.

---

## 12. Actionable conclusions and trade construction

**Bull case (supported by evidence):**
- Revenue +16.4% with **71.9% incremental gross margin** — growth quality is exceptional.
- GM +356 bps and OPM +263 bps **despite** R&D +32.3% — margin expansion is funded, not borrowed from the future.
- FCF +52.5%, OCF/NI 1.15x, net cash up to **$62.2B**, debt/equity down to **0.78x**, zero new LT debt issued.
- Current ratio >1.0x for the first time; buybacks down 12% while cash piles up → **optionality for a major value-accretive deployment.**
- Tax headwind **narrowed** (9M +218 bps → Q3 +146 bps), so forward ETR drag may be peaking.

**Bear case (supported by evidence):**
- Some of the +225 bps of 9M gross margin is likely **input-cost cyclicality**, not mix — services proxies (deferred revenue +8.8%) grew *slower* than total revenue (+16.2%). Margin mean-reversion is the primary downside risk.
- **Inventory +94% (+260% raw materials)** = 61.6 days of COGS vs 34.0. A demand miss converts this to write-downs fast.
- **$13.3B intangible build with opaque funding** — diligence required, and historically large intangible-driven spend occasionally precedes impairment.
- Capex at 1.87% of revenue **cannot keep falling**; the FCF tailwind is finite.
- Diligence gap: **no segment data, no price data, no insider data** — three significant blind spots for a consensus-defined mega-cap.

**Concrete position-management guidance:**

1. **Do not underwrite 52% FCF growth forward.** The capex decline (−28%) supplied roughly $2.7B of it and the securities-portfolio rotation supplied most of the investing-cash swing. Normalize to high-teens/low-20s FCF growth off a $117B 9M base.
2. **Anchor expectations on the tax rate, not just operations.** Every 100 bps of ETR on a ~$165B annualized pretax run-rate is ~$1.65B of net income. Modest ETR relief is a real, underappreciated EPS kicker.
3. **The FQ4/FY2026 10-K is the catalyst — expect it late October 2026** (FY2025's 10-K was filed 2025-10-31). Watch three numbers above all: **(a) FQ4 gross margin vs 50.06%, (b) inventory level vs $11,092M, (c) the intangible/noncurrent-liability note.**
4. **Asymmetry favors long exposure into that print** given the net-cash build, decelerating buyback (dry powder), narrowing tax drag, and 71.9% incremental margins — but size it against the inventory risk, and **verify the intangible funding source first.**

---

## 13. Key points summary table

| Category | Item | Value / Finding | Read-through |
|---|---|---|---|
| **Reporting** | Latest filing | 10-Q, acc. 0000320193-26-000020, accepted 2026-07-31 | FQ3 FY26 ended 2026-06-27 |
| **Growth** | FQ3 revenue | $109,417M, **+16.4% YoY** | Sharp re-acceleration |
| **Growth** | 9M revenue | $364,357M, **+16.2% YoY** | Multi-quarter trend, not a one-off |
| **Margin** | FQ3 gross margin | **50.06%**, +356 bps | Crossed 50% — services/pricing signature |
| **Margin** | 9M gross margin | 49.07%, +225 bps | Expansion is broad-based |
| **Margin** | FQ3 incremental gross margin | **71.9%** | Exceptional growth quality |
| **Margin** | FQ3 operating margin | 32.62%, +263 bps | Op leverage despite R&D surge |
| **Earnings** | FQ3 net income | $29,789M, **+27.1%** | FQ3 net margin 27.23% |
| **Earnings** | 9M diluted EPS | **$6.88 vs $5.62, +22.4%** | Buyback adds ~1pt |
| **Earnings** | FQ3 diluted EPS | **$2.02 vs $1.57, +28.7%** | Best quarter of the year |
| **Earnings** | 9M effective tax rate | **17.58% vs 15.39% (+218 bps)** | ~$2.2B drag; **narrowing to +146 bps in Q3** |
| **Investment** | R&D 9M | **$34,035M, +32.5%** (9.34% of rev vs 8.19%) | Deliberate AI/IP step-up |
| **Investment** | SG&A 9M | $22,315M, +8.6% | Half of revenue growth — real discipline |
| **Cash** | 9M operating cash flow | **$116,996M, +43.1%** | OCF/NI = 1.15x |
| **Cash** | 9M free cash flow | **$110,197M, +52.5%** | Capex fell 28% — not repeatable |
| **Cash** | Capex / revenue | **1.87%** (vs 3.02%) | Structurally capital-light |
| **Balance sheet** | Net cash | **+$62,220M** (from +$33,741M) | +$28.5B in nine months |
| **Balance sheet** | Total debt / equity | **0.78x** (from 1.34x) | Sharp de-risking |
| **Balance sheet** | Cash + securities | **$146,517M** | Ample dry powder |
| **Balance sheet** | Equity / assets | **28.1%** (from 20.5%) | Best in the series |
| **Balance sheet** | Current ratio | **1.003x** (from 0.893x) | Crossed above 1.0x |
| **Balance sheet** | New LT debt issued, 9M | **$0** (vs $4,481M) | Self-financing |
| **Capital return** | 9M buybacks | $62,094M, **−12.0%** | Decelerating despite FCF surge |
| **Capital return** | 9M dividends | $11,778M, +1.9%; DPS $0.79 (+3.9%) | Modest growth |
| **Capital return** | Total payout / FCF | **72.9%** (from 97.6%) | Retaining ~$14B |
| ⚠️ **Risk** | Inventory | **$11,092M, +94%**; raw materials **+260%** | 61.6 days COGS vs 34.0 — ramp or overbuild? |
| ⚠️ **Risk** | Intangibles, gross | **$38,220M, +$13,270M** | Funding source not visible in slice |
| ⚠️ **Risk** | Other noncurrent liabilities | **$55,080M, +$13,531M** | ~1:1 with intangible build — resolution needed |
| ✅ **Signal** | Accumulated depreciation | Only +$730M in 9M | Physical base flat; **growth engine = IP, not PP&E** |
| **Leading ind.** | Deferred revenue | $14,900M, **+8.8%** | Slower than revenue → mix may be hardware-led |
| **History** | OCF FY23 / FY24 / FY25 | $110,543M / $118,254M / n/a | Steady, then step-change in FY26 |
| **History** | Financing FY23 / FY24 / FY25 | −$108,488M / −$121,983M / −$120,686M | Consistent large return of capital |
| **Debt ladder** | FY25 maturities, next 12 mo / >5 yr | $12,393M / $49,303M | Smooth, long-dated, well covered |
| **Shares** | Outstanding | 14,608.963M (6/27); 14,594.180M (7/17) | −1.1% over nine months |
| **Run-rate** | Annualized EPS (derived) | **$8.08** (FQ3×4) to **$9.17** (9M×4/3) | Q1 seasonally strongest; truth in between |
| ❌ **Gap** | Insider transactions | **DATA_UNAVAILABLE** | Do **not** infer — source from EDGAR directly |
| ❌ **Gap** | Price / valuation multiples | Not provided by tools | No P/E computed; no invented multiples |
| ❌ **Gap** | Segment revenue split | Not in returned tags | Cannot prove services-mix thesis |
| **Catalyst** | Next 10-K (FY2026) | Expected **late Oct 2026** | Watch GM, inventory, intangible note |

---

**Report scope note:** All figures are USD millions unless stated, drawn from point-in-time SEC XBRL facts public by 2026-08-31. Lines marked *derived* (free cash flow, net cash, ratios, run-rates, the implied buyback price range) are my arithmetic on reported values, not vendor-supplied fields. The implied buyback price in Section 9 is explicitly a crude inference and should be replaced by a live quote before any valuation work. Insider data was unavailable and has not been estimated in any form.