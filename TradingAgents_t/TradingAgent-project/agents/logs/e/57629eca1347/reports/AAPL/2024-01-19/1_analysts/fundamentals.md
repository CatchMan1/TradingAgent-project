# AAPL — Fundamental Research Report
**Analysis date:** 2024-01-19 | **Instrument:** AAPL (Apple Inc., Nasdaq)
**Data basis:** Point-in-time SEC EDGAR facts (10-K FY2023 filed 2023-11-03; 10-Q filings through FY2023 Q3 filed 2023-08-04), filtered by actual EDGAR acceptance timestamp so nothing after 2024-01-19 leaks in.

---

## 0. Important data-scope caveat (read first)

- **The most recent fully reported period available to me is FY2023, ended 2023-09-30** (10-K accepted 2023-11-03). The latest 10-Q facts in the archive are cumulative 39-week figures through **2023-07-01**.
- **FQ1 2024 (quarter ended ~2013-12-30) had NOT yet been reported as of 2024-01-19.** Apple's December-quarter print landed 2024-02-01. I therefore have **no** holiday-quarter revenue, iPhone units, Greater China figures, or guidance for the current quarter. I will not estimate them.
- **Insider transactions: DATA UNAVAILABLE.** The vendor archive returned no authorized point-in-time insider-transactions data for AAPL as of 2024-01-19. **No insider buying or selling is inferred or fabricated in this report.** This is a genuine information gap, not evidence of absence of activity.
- Balance-sheet tags returned include cash and long-dated AFS securities but **do not itemize short-term marketable securities**; any "total cash" figure below is therefore a conservative floor, not the true liquidity figure.

---

## 1. Executive summary

1. **FY2023 was a modest "digestion" year, not a deterioration.** Revenue fell **−2.8%** to **$383.3B** and net income fell **−2.8%** to **$97.0B**, but **diluted EPS still rose +0.3% to $6.13** because the share count fell 2.8%. Buybacks fully offset the revenue decline at the EPS line.
2. **Gross margin expanded to a record 44.13%** (+82 bps y/y, +235 bps over two years) while opex grew to 14.31% of sales. The mix shift toward Services is visibly working: gross margin up while revenue is down is the single most important structural signal in this dataset.
3. **Operating margin is remarkably stable at ~29.8–30.3%** across three years — the opex step-up (54.8B, +6.8% y/y) was absorbed almost exactly by gross-margin expansion. FY2023 operating income: **$114.3B**.
4. **Cash generation remains elite but decelerating:** OCF **$110.5B (−9.5%)**, capex only **$11.0B**, **FCF $99.6B** (26.0% of revenue). FCF covers total shareholder returns of **$92.6B** by 1.08× — i.e., Apple funded buybacks + dividends from free cash flow with a small cushion, without adding net debt.
5. **Balance sheet was actively delevered:** total debt **$120.1B → $111.1B (−7.5%)**, cash **+26.7% to $30.0B**, **working capital swung from −$18.6B to −$1.7B**, current ratio **0.88 → 0.99**. Equity jumped **+22.6% to $62.1B**.
6. **Capital returns were trimmed, not abandoned:** buybacks **$77.6B (vs $89.4B)** and dividends **$15.0B (vs $14.8B)**. The buyback cut (−13.3%) is the tell that management was husbanding cash in a flattish revenue year.
7. **Valuation is full.** On FY2023 diluted EPS of $6.13, an illustrative ~$189 reference price implies **~30.8× trailing earnings** and a **~3.4% FCF yield**. This is a premium-quality, low-growth-price multiple — the stock needs a return to revenue growth (or a multiple-tolerant tape) to work from here.

---

## 2. Company profile (as of the analysis date)

Apple Inc. designs, manufactures and markets smartphones (iPhone), personal computers (Mac), tablets (iPad), wearables/home/accessories (Watch, AirPods, Vision Pro), and monetizes an installed base of ~2B+ active devices through **Services** (App Store, iCloud, Music, TV+, advertising, Apple Pay, licensing). The company is vertically integrated on silicon (Apple-designed SoCs), outsources assembly, sells direct (retail + online) and through carriers/retailers, and operates globally with the Americas, Europe and Greater China as its largest regions.

**Structural characteristics visible in the data:**
- **Capital-light:** capex is only 2.9% of revenue ($11.0B on $383.3B).
- **Asset-light balance sheet with heavy financial leverage:** liabilities are 82.4% of assets; equity is thin ($62.1B) by design due to buybacks. ROE is therefore extreme (**~156%**) and is a poor quality metric here — use ROA (**27.5%**) and FCF instead.
- **Public float ~$2.59T** (EntityPublicFloat at 2023-03-31), one of the largest in the world. Shares outstanding **15,500,061,000** at 2023-09-30 (**15,552,752,000** at 2023-10-20).

---

## 3. Income statement — three-year history

| $ in millions | FY2021 | FY2022 | FY2023 | FY23 y/y |
|---|---|---|---|---|
| Revenue (COGS + gross profit) | 365,817 | 394,328 | **383,285** | **−2.8%** |
| Cost of goods & services | 212,981 | 223,546 | 214,137 | −4.2% |
| **Gross profit** | 152,836 | 170,782 | **169,148** | −0.96% |
| *Gross margin* | *41.78%* | *43.31%* | ***44.13%*** | *+82 bps* |
| Operating expenses | 43,887 | 51,345 | **54,847** | +6.8% |
| *Opex % of revenue* | *12.00%* | *13.02%* | *14.31%* | *+129 bps* |
| **Operating income** | 108,949 | 119,437 | **114,301** | −4.3% |
| *Operating margin* | *29.78%* | *30.29%* | *29.82%* | *−47 bps* |
| Non-operating income/(expense) | +258 | (334) | **(565)** | worse |
| Pretax income | 109,207 | 119,103 | **113,736** | −4.5% |
| Income tax | 14,527 | 19,300 | 16,741 | −13.3% |
| *Effective tax rate* | *13.3%* | *16.2%* | ***14.7%*** | *−150 bps* |
| **Net income** | 94,680 | 99,803 | **96,995** | −2.8% |
| *Net margin* | *25.88%* | *25.31%* | *25.31%* | flat |
| **Diluted EPS** | $5.61 | $6.11 | **$6.13** | **+0.3%** |
| Basic EPS | $5.67 | $6.15 | $6.16 | +0.2% |
| Diluted shares (implied) | ~16,877M | ~16,335M | ~15,823M | −3.1% |

**Key reads from the income statement:**
- **The gross-margin line is the story.** +235 bps over two years while revenue *declined* is only possible with a favorable mix shift (Services/higher-margin hardware) plus commodity and freight relief. This is the highest-quality evidence in the dataset that Apple's margin flywheel is intact.
- **The opex line is the watch item.** Opex grew $3.5B (+6.8%) against a 2.8% revenue decline — operating leverage has turned *negative*. Opex intensity rose 129 bps in one year vs. only 102 bps over the entire prior year. Continuation of this trend in FY2024 would erase the gross-margin gains.
- **Non-operating swung against Apple:** interest expense rose to **$3,933M (+34.2% y/y, +48.7% over two years)** as the debt stack repriced, only partly offset by investment income of **$3,750M**. Net non-operating was **−$565M**. Higher-for-longer rates are a genuine, if small (~0.5% of revenue), earnings headwind.
- **Tax rate is a risk, not a tailwind.** FY2023's 14.7% benefited from a **$1.12B share-based-compensation excess tax benefit** and **$1.21B of R&D credits**, and it sat well below the 21% statutory rate. The 10-K also discloses a **possible ~$4.5B decrease in unrecognized tax benefits within 12 months** — a quantified downside/upside swing of roughly **$0.29/share**, ~4.7% of EPS.
- **SBC is compounding:** **$10,833M in FY2023 (+19.9% y/y, +37% over two years)** vs. net income that fell. SBC is now **2.83% of revenue and 11.2% of net income**, and **$18.6B of unrecognized SBC cost** remains to be expensed. Buybacks mask the dilution but the real economic cost is rising.
- **D&A is stable at $11.5B** — no ballooning of the asset base; the depreciation-to-capex ratio (~105%) says Apple is not under-investing in a way that flatters cash flow this year.

---

## 4. Balance sheet and liquidity

| $ in millions | 2022-09-24 | 2023-09-30 | Δ |
|---|---|---|---|
| Cash & cash equivalents | 23,646 | **29,965** | **+26.7%** |
| Long-dated AFS debt securities (fair value) | n/d | **100,544** | — |
| Accounts receivable, net | 28,184 | 29,508 | +4.7% |
| Inventories, net | 4,946 | 6,331 | **+28.0%** |
| Vendor non-trade receivables | 32,748 | 31,477 | −3.9% |
| Other current assets | 21,223 | 14,695 | −30.8% |
| **Current assets** | 135,405 | **143,566** | +6.0% |
| **Total assets** | 352,755 | 352,583 | flat |
| Accounts payable | 64,115 | 62,611 | −2.3% |
| Commercial paper | 9,982 | **5,985** | **−40.0%** |
| Current portion of long-term debt | 11,128 | 9,822 | −11.7% |
| Other current liabilities | 60,845 | 58,829 | −3.3% |
| **Current liabilities** | 153,982 | **145,308** | −5.6% |
| **Working capital** | **(18,577)** | **(1,742)** | **+$16.8B** |
| Long-term debt (noncurrent) | 98,959 | 95,281 | −3.7% |
| **Total debt (CP + LTD)** | **120,069** | **111,088** | **−7.5%** |
| Finance lease liabilities | 941 | 1,024 | +8.8% |
| Operating lease liabilities | 11,470 | 11,818 | +3.0% |
| Deferred revenue (total) | 12,400 | 12,100 | −2.4% |
| Deferred tax assets, net | 21,676 | 24,369 | +12.4% |
| **Total liabilities** | 302,083 | **290,437** | −3.9% |
| **Shareholders' equity** | 50,672 | **62,146** | **+22.6%** |

**Liquidity and leverage assessment:**
- **Current ratio improved from 0.879 to 0.988.** Apple still runs a current-liability-funded model (negative working capital in FY2022), but the gap nearly closed in FY2023 — a meaningful de-risking that few observers flag.
- **Gross debt fell $9.0B** while cash rose $6.3B. Adding the $100.5B of long-dated AFS securities, cash + long-dated securities of **$130.5B vs. $111.1B of debt = a ~$19.4B net cash position** — and that *understates* it because short-term marketable securities are not itemized in the returned data.
- **Debt servicing is not a concern but is getting more expensive:** FY2023 interest expense of $3.9B is covered **29×** by operating income, and the maturity ladder is smooth: **$9.9B (FY24), $10.8B (FY25), $12.3B (FY26), $9.8B (FY27), $7.8B (FY28), $56.0B thereafter**. No refinancing wall.
- **Working-capital items worth noting:** inventories **+28% to $6.3B** and AR **+4.7%** both grew faster than revenue (−2.8%). DSO deteriorated to **~28.1 days from ~26.1**. Both are small in absolute terms but they are the correct direction for concern, not comfort, and suggest the FY2023 cash-flow decline was partly working-capital-driven rather than purely demand-driven.
- **Deferred revenue fell slightly ($12.4B → $12.1B)** even as Services grew; $8.2B of prior-period deferred revenue was recognized in FY2023 (up from $7.5B). A flat deferred-revenue balance is a mild caution on forward Services visibility, though current deferred revenue did tick up to $8.06B.
- **Equity of $62.1B is the binding constraint on buyback capacity at the margin:** liabilities are 82% of the balance sheet. Apple can keep buying stock, but each dollar of buyback reduces an already thin equity base — leverage ratios (debt/equity **1.79×**) overstate risk precisely because equity is intentionally suppressed.

---

## 5. Cash flow and capital allocation

| $ in millions | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Net cash from operations | 104,038 | 122,151 | **110,543** |
| Capex (PP&E) | (11,085) | (10,708) | **(10,959)** |
| **Free cash flow** | **92,953** | **111,443** | **99,584** |
| *FCF margin* | *25.4%* | *28.3%* | *26.0%* |
| *OCF / net income* | *1.10×* | *1.22×* | ***1.14×*** |
| Purchases of AFS securities | (109,558) | (76,923) | (29,513) |
| Proceeds from AFS sales | 47,460 | 37,446 | 5,828 |
| Proceeds from AFS maturities | 59,023 | 29,917 | 39,686 |
| **Net investing cash flow** | (14,545) | (22,354) | **+3,705** |
| **Share repurchases** | (85,971) | (89,402) | **(77,550)** |
| **Dividends paid** | (14,467) | (14,841) | **(15,025)** |
| **Total shareholder returns** | **100,438** | **104,243** | **92,575** |
| Tax withholding on SBC | (6,556) | (6,223) | (5,431) |
| Net financing cash flow | (93,353) | (110,749) | **(108,488)** |
| Net change in cash | (3,860) | (10,952) | **+5,760** |

**Interpretation:**
- **FCF fell 10.6% to $99.6B** — the first sub-$100B FCF year in three. Still a 26% FCF margin, a level almost no large-cap company achieves.
- **Cash conversion (OCF/NI = 1.14×) is healthy** but down from 1.22× — consistent with the working-capital build noted above. Earnings quality remains high; there is no accrual red flag.
- **Apple shifted from a net buyer to a net seller of securities:** CFI went **positive $3.7B** in FY2023 (from −$22.4B) as it let $39.7B of AFS securities mature while buying only $29.5B. This, plus a lower commercial-paper balance (−$4.0B), is where the **+$5.8B cash build** came from — **not** from operations. Traders should note the cash increase is a portfolio and debt-management decision, not an operating inflection.
- **The capital-return engine was throttled:** total returns fell **$11.7B (−11.2%)** to $92.6B, entirely from the buyback line (−13.3%). Dividends grew just **+1.2%**. Total returns were covered **1.08×** by FCF (vs. 1.17× in FY2022) — still fully funded, but with meaningfully less headroom.
- **Dividend per share declared $0.94** (from $0.90), a **payout ratio of ~15.3%**. The dividend remains almost symbolic relative to FCF; the real return of capital is the buyback.
- **Cumulative 9M FY2023 (through 2023-07-01) confirms the trend persisted all year:** OCF **$88,945M vs. $98,024M (−9.3%)**; buybacks **$56,547M vs. $64,974M**; dividends **$11,267M vs. $11,138M**. The full-year numbers are not a Q4 anomaly.

---

## 6. Insider transactions

**Not available.** The point-in-time insider-transactions archive contains no authorized data for AAPL by 2024-01-19. I am explicitly declining to speculate; any specific insider-buying or insider-selling signal for AAPL in this report would be fabricated. Traders demanding an insider-flow input must source it separately (e.g., Form 4 filings on EDGAR directly). Treat the absence as a **blank field**, and note that for a company of AAPL's size, insider activity is a low-signal input in any case given executives' compensation is overwhelmingly equity-based.

---

## 7. Key risks (evidence-based, not generic)

| Risk | Evidence in the dataset | Magnitude |
|---|---|---|
| **Revenue stagnation becomes structural** | Revenue −2.8% y/y; 9M OCF −9.3% | High — a 30× multiple on shrinking revenue is fragile |
| **Negative operating leverage** | Opex +6.8% on revenue −2.8%; opex ratio +129 bps | Medium-High — would unwind the gross-margin story |
| **Tax rate normalization** | 14.7% vs 21% statutory; $4.5B probable change in unrecognized benefits | Medium — ~$0.29/share (~4.7% of EPS) |
| **Rising interest cost** | Interest expense +48.7% over two years to $3.9B | Medium-Low — 29× covered |
| **Thin equity / buyback capacity** | Liabilities 82% of assets; equity $62.1B; D/E 1.79× | Medium — limits aggressive buyback upside |
| **SBC creep** | SBC $10.8B, +19.9% y/y; $18.6B unrecognized; opex pressure | Medium |
| **Working-capital build** | Inventory +28%, AR +4.7%, DSO +2 days | Low-Medium — early warning, small absolute |
| **Slight forward-visibility softening** | Deferred revenue $12.4B → $12.1B; contract liabilities −2.4% | Low-Medium |
| **Data/latency risk for the trader** | No FQ1-24 data available at 2024-01-19 | High for near-term positioning decisions |

---

## 8. Actionable takeaways for traders

**Bull case (what the data supports):**
- Gross margin at a **record 44.13%** with a still-normalizing Services mix means the FY2024 earnings base is more resilient than a −2.8% revenue print implies. **Model gross-margin expansion, not revenue growth, as the near-term EPS driver.**
- **$99.6B FCF, $19B+ net cash, and 29× interest coverage** mean there is no balance-sheet scenario that impairs this franchise. Apple is a defensive holding with a quality floor.
- **Buyback authorization is under-utilized relative to cash generation** ($92.6B returned vs. $99.6B FCF). If revenue re-accelerates even modestly, the capital-returns line has room to re-expand and mechanically lift EPS.
- **Working capital improved $16.8B** and the CP balance was cut 40% — a cleaner, better-hedged balance sheet entering FY2024 than entering FY2023.

**Bear case (what the data supports):**
- **You are paying ~30–31× trailing EPS for a company that shrank revenue and net income.** Every forward-return scenario from here requires either revenue growth to reappear or multiple expansion. Multiple expansion on a $2.9T base is hard.
- **The EPS "growth" was entirely financial engineering.** Diluted EPS +0.3% on a 3.1% share-count reduction and a 2.8% net-income decline. This is the most important numbers-check in the report.
- **Negative operating leverage (+129 bps opex ratio) plus a rising tax rate is a two-front margin squeeze in FY2024.**
- **Capital returns are contracting** (−11.2% y/y). Historically, decelerating buybacks at Apple have coincided with periods of muted stock performance; the reduction is a signal management does not see a compelling use of cash at current prices.

**Positioning framework (evidence-based):**
- **Event risk is imminent and un-quantified in this dataset.** The December quarter prints on **2024-02-01**. Everything in this report is a *pre-print* prior. A trader should size positions with knowledge of that binary event and obtain FQ1-24 expectations from a source outside this dataset.
- **What to check the moment the 10-Q lands:** (1) gross margin vs. the 44.13% FY2023 base; (2) opex as % of revenue vs. 14.31%; (3) FCF vs. the $99.6B run-rate; (4) buyback dollars vs. the $77.6B FY2023 base; (5) deferred revenue as a forward-demand proxy. Those five line items are where this dataset has real predictive signal.
- **Valuation sensitivity for entry discipline** (illustrative, using an approximate $189 reference price and FY2023 diluted EPS of $6.13 — price is *not* from the fundamental dataset):

| Reference price | Trailing P/E (FY23 EPS $6.13) | FCF yield (FCF $99.58B) | Dividend yield ($0.94) |
|---|---|---|---|
| $170 | 27.7× | 3.78% | 0.55% |
| $180 | 29.4× | 3.57% | 0.52% |
| $189 | 30.8× | 3.40% | 0.50% |
| $200 | 32.6× | 3.21% | 0.47% |
| $210 | 34.3× | 3.06% | 0.45% |

*Market cap at ~$189 ≈ $2.93T on 15.50B shares.*

- **Best risk-adjusted use of this report:** treat AAPL as a **high-quality, fully-valued, cash-return compounder with no balance-sheet risk and no visible fundamental catalyst inside the dataset.** The asymmetry from here is modestly negative until either (a) Services mix drives gross margin sustainably above 45%, or (b) the multiple compresses toward the high-20s.

---

## 9. Key figures at a glance

| Metric | Value | Period | Read-through |
|---|---|---|---|
| Revenue | $383.29B | FY2023 (ended 2023-09-30) | −2.8% y/y |
| Gross profit / margin | $169.15B / **44.13%** | FY2023 | Record margin, +82 bps y/y |
| Operating income / margin | $114.30B / **29.82%** | FY2023 | −47 bps y/y; −4.3% absolute |
| Net income / margin | $96.995B / **25.31%** | FY2023 | −2.8% y/y; margin flat |
| Diluted EPS | **$6.13** | FY2023 | +0.3% y/y (buyback-driven) |
| Diluted share count (implied) | ~15.82B | FY2023 | −3.1% y/y |
| Operating cash flow | $110.54B | FY2023 | −9.5% y/y |
| Capex | $10.96B (2.9% of revenue) | FY2023 | Capital-light model confirmed |
| **Free cash flow** | **$99.58B (26.0% of revenue)** | FY2023 | −10.6% y/y |
| OCF / net income | 1.14× | FY2023 | Solid earnings quality (was 1.22×) |
| Cash & equivalents | $29.97B | 2023-09-30 | +26.7% y/y |
| Long-dated AFS securities | $100.54B | 2023-09-30 | Cash + LTD securities ≈ $130.5B |
| Total debt (CP + LTD) | $111.09B | 2023-09-30 | **−7.5% y/y** (deleveraging) |
| Net cash (cash + LTD securities − debt) | **≈ +$19.4B** | 2023-09-30 | Conservative floor; excludes short-term securities |
| Working capital | **−$1.74B** | 2023-09-30 | Improved from −$18.58B |
| Current ratio | 0.988 | 2023-09-30 | Up from 0.879 |
| Total assets / liabilities | $352.58B / $290.44B | 2023-09-30 | Liabilities = 82.4% of assets |
| Shareholders' equity | $62.15B | 2023-09-30 | +22.6% y/y |
| ROE | ~156% | FY2023 | Distorted by buyback-thin equity |
| ROA | **~27.5%** | FY2023 | The better quality metric |
| Debt / equity | 1.79× | 2023-09-30 | Structurally high by design |
| Interest expense | $3.93B | FY2023 | +34.2% y/y; 29× covered by EBIT |
| SBC expense | $10.83B | FY2023 | +19.9% y/y; $18.6B unrecognized |
| Effective tax rate | 14.7% | FY2023 | vs. 21% statutory; $4.5B UTB risk |
| Buybacks | $77.55B | FY2023 | **−13.3% y/y** |
| Dividends paid / per share | $15.03B / $0.94 | FY2023 | Payout ~15.3% |
| Total shareholder returns | $92.58B | FY2023 | **−11.2% y/y**; 1.08× covered by FCF |
| Shares outstanding | 15.50B (15.55B at 2023-10-20) | 2023-09-30 | −2.8% y/y |
| 9M FY2023 OCF (thru 2023-07-01) | $88.95B vs $98.02B | 9M FY23 | −9.3% — trend confirmed all year |
| Insider transactions | **DATA UNAVAILABLE** | as of 2024-01-19 | No signal; not inferred |
| Next reporting catalyst | FQ1 2024, ~2024-02-01 | post-analysis-date | Not reflected in any figure above |

**Bottom line for the desk:** AAPL at 2024-01-19 is a **cash machine with a flat top line and a full multiple**. The FY2023 10-K shows a *margin story* (record 44.13% gross margin, stable ~30% operating margin) masking a *growth problem* (−2.8% revenue, −2.8% net income, EPS propped up by a 3.1% share-count cut) and a *capital-return slowdown* (−11.2%). Balance-sheet risk is essentially nil. The decisive unknown — holiday-quarter demand — is **outside this dataset** and lands on 2024-02-01. Own it for quality and cash return, not for growth at 30× trailing earnings.