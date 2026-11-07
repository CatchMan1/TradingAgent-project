# GOOGL (Alphabet Inc.) — Fundamental Deep-Dive

**Pricing/reporting date:** 2026-07-01 | **Latest report on file:** Q1 2026 Form 10-Q (filed 2026-04-30) | **FY2025 Form 10-K** (filed 2026-02-05)

> **Data caveat:** Insider-transaction data was **not available** in the authorized archive as of 2026-07-01 — I have **not** inferred or fabricated any insider buying/selling. All figures below are drawn from SEC XBRL facts and are internally reconciled (revenue − costs, pretax → net income, cash flow identity all tie out). Dollar figures in USD.

---

## 1. Company Profile & Snapshot

- **Company:** Alphabet Inc. (parent of Google). Dual-class structure: **GOOGL** (Class A, voting) and GOOG (Class C).
- **Segments:** **Google Services** (Search, YouTube ads, Android, Chrome, Maps, Play, subscriptions/devices), **Google Cloud** (GCP + Workspace), **Other Bets** (Waymo, Verily, etc.).
- **Shares outstanding:** 12,116M (2026-03-31), up marginally from 12,088M at 2025-12-31 (SBC issuance; **no buyback** in Q1).
- **Dividend:** $0.21/share quarterly (Q1 2026), +5% vs $0.20 in Q1 2025 (~$0.84 annualized).
- **Capital-markets footprint:** ~$80B gross debt, ~$127B cash + marketable securities — still a large **net-cash** position (~$46B).

---

## 2. Q1 2026 Income Statement (three months ended 3/31/2026) vs Q1 2025

| Line item | Q1 2026 | Q1 2025 | YoY |
|---|---|---|---|
| **Revenue** | **$109,896M** | $90,234M | **+21.8%** |
| Cost of revenue | $41,271M | $36,361M | +13.5% |
| **Gross profit** | **$68,625M** | $53,873M | +27.4% |
| Gross margin | **62.4%** | 59.7% | +270 bps |
| R&D | $17,032M | $13,556M | +25.6% |
| Sales & marketing | $7,606M | $6,172M | +23.2% |
| G&A | $4,291M | $3,539M | +21.3% |
| **Operating income** | **$39,696M** | $30,606M | **+29.7%** |
| Operating margin | **36.1%** | 33.9% | +220 bps |
| Nonoperating income (net) | **$37,716M** | $11,183M | +237% |
| Pre-tax income | $77,412M | $41,789M | +85% |
| Income tax | $14,834M | $7,249M | — |
| Effective tax rate | 19.2% | 17.3% | +190 bps |
| **Net income** | **$62,578M** | $34,540M | +81% |
| **Diluted EPS** | **$5.11** | $2.81 | +82% |
| Diluted shares | ~12,250M | ~12,290M | — |

**Critical read — quality of earnings:** Operating results were strong (revenue +22%, operating margin expanding to 36.1%). But **~$37.7B of pretax income (≈49% of the total) came from nonoperating items**, dominated by a **~$36.9B mark-to-market gain on equity securities (EquitySecuritiesFvNiGainLoss)**. This is *not* recurring operating profit. Strip it out and after-tax operating EPS is roughly **~$2.6–2.7/share**, versus the reported $5.11. Traders should size GOOGL off the operating earnings power, not the headline EPS, which was flattered by an investment revaluation.

---

## 3. The Investment-Gain Story (Balance-Sheet Unrealized Gains)

The $36.9B gain is corroborated on the balance sheet — this is a **revaluation of non-marketable (private) equity holdings** (e.g., large stakes such as SpaceX/Anthropic-class positions):
- Non-marketable equity securities: **$64,094M → $101,346M** (Dec 2025 → Mar 2026), a **+$37.3B** jump.
- Cumulative *upward* price-adjustment on those holdings: **$44,485M → $80,792M** (+$36.3B) — matches the P&L gain.
- This is **unrealized, non-cash** and marks a step-up in reported book value; it is high-quality in the sense of mark-to-fair-value but volatile and non-repeatable quarter to quarter.

**Actionable takeaway:** The huge net income and EPS surge is largely a one-time valuation mark. Base-case operating momentum (search/cloud) is the durable driver; the investment book is a large, under-appreciated asset that can swing reported earnings sharply either direction.

---

## 4. Balance Sheet (2026-03-31 vs 2025-12-31)

| Item | 3/31/2026 | 12/31/2025 | Change |
|---|---|---|---|
| Cash & equivalents | $38,063M | $30,708M | +$7.4B |
| Cash + ST investments | **$126,840M** | $126,843M | flat |
| Accounts receivable | $62,999M | $62,886M | flat |
| **Total current assets** | $213,753M | $206,038M | +$7.7B |
| **Total assets** | **$703,919M** | $595,281M | **+$108.6B (+18%)** |
| **Total liabilities** | $225,173M | $180,016M | +$45.2B (+25%) |
| Long-term debt (carrying) | **$80,305M** | $49,085M | **+$31.2B** |
| Finance lease liability | $2,214M | $2,500M | −$0.3B |
| **Shareholders' equity (implied)** | **~$478,746M** | ~$415,265M | +$63.5B |

**Key balance-sheet observations:**
1. **Debt ramp:** Long-term debt jumped **+$31.2B in a single quarter** — Alphabet is now funding AI capex and the investment book partly with debt. Debt maturities per the FY2025 10-K: $2.0B (next 12m), $1.0B (yr2), $2.7B (yr3), $1.8B (yr4), $5.5B (yr5), $36.1B (after yr5) — a long, well-laddered profile. Even after the ramp, the company retains ~$46B **net cash**.
2. **New intangibles → an acquisition:** Gross intangibles ex-goodwill jumped **$2,662M → $10,821M** (net $1,088M → $9,249M) in Q1 2026. This strongly implies Alphabet closed a **large acquisition (~$8B of finite-lived intangibles)** in the quarter. Worth watching for consolidation impact and amortization step-up.
3. **Deferred tax assets collapsed** $9,113M → $1,995M — consistent with utilization/revaluation tied to the equity gain.
4. Total assets +18% in one quarter is driven by the equity revaluation (+$37B) and the acquisition intangibles — not organic cash build.

---

## 5. Cash Flow & Free Cash Flow (the real story)

| Metric | Q1 2026 | Q1 2025 |
|---|---|---|
| **Operating cash flow** | $45,790M | $36,150M |
| **CapEx (PP&E purchases)** | **$35,674M** | $17,197M |
| **Free cash flow (OCF − CapEx)** | **$10,116M** | $18,953M |
| Investing cash flow | −$63,389M | −$16,194M |
| Financing cash flow | **+$25,077M** | −$20,201M |
| Debt raised (net of costs) | **$31,379M** | $4,532M |
| Debt repaid | $1,477M | $4,521M |
| Dividends paid | $2,542M | $2,434M |
| **Share repurchases** | **$0** | $15,068M |

**This is the single most important fundamental tension in the quarter:**
- **FCF collapsed ~47% YoY to $10.1B despite +22% revenue** — because **capex more than doubled to $35.7B in one quarter** (annualized run-rate ~$140B+ of AI/data-center spend). CapEx still ramping: FY2025 was $91.4B vs FY2024 $52.5B vs FY2023 $32.3B.
- **Buybacks were paused ($0)** and the company **issued $31.4B of new debt** to help fund the capex + investment build. This is a notable capital-allocation pivot: from return-of-capital (historically $45–62B/yr buybacks) toward **reinvestment + debt-financed infrastructure**.

**Annual cash-flow trajectory (from FY2025 10-K / comparisons):**

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Operating cash flow | $101,746M | $125,299M | **$164,713M** |
| CapEx (PP&E) | $32,251M | $52,535M | **$91,447M** |
| Implied FCF | ~$69,495M | ~$72,764M | **~$73,266M** |
| Buybacks | $61,504M | $62,222M | $45,709M |
| Dividends | $0 | $7,363M | $10,049M |
| Debt raised | $10,790M | $13,589M | **$64,564M** |

OCF is compounding impressively (+31% in FY2025), but **capex has grown faster than OCF**, flattening FCF two years running — the "AI tax" on cash generation. FY2025 debt issuance of $64.6B confirms management is leaning on the balance sheet to fund the build-out.

---

## 6. Profitability, Returns & Financial Health

- **Gross margin:** 62.4% (Q1 2026) vs 59.7% — improving (AI/cloud mix and search efficiency).
- **Operating margin:** 36.1% — best-in-class for a mega-cap, still expanding.
- **Net margin:** 56.9% reported — *flattered* by the investment gain; underlying net margin ~30%.
- **ROE (annualized, reported):** very high but distorted by the one-time gain and rising equity base; core ROE remains robust.
- **Liquidity:** $126.8B cash + securities vs $80.3B debt → strong **net cash (~$46B)**; interest coverage enormous (interest expense only $533M in Q1 vs $39.7B operating income).
- **Leverage:** Liabilities/Assets ~32% — still conservative despite the debt ramp.

---

## 7. Insider Transactions
**Not available.** The authorized point-in-time archive has no insider-transaction record for GOOGL as of 2026-07-01. No insider buying or selling is reported here — figures must not be inferred. (Recommend sourcing Form 4s separately before making an insider-flow-based decision.)

---

## 8. Key Insights for Traders (Actionable)

1. **Don't be fooled by the EPS explosion.** Headline EPS $5.11 (+82%) is inflated by a **~$2.5/share non-cash equity revaluation gain**. The durable, operating EPS is roughly **$2.6–2.7**. Value GOOGL on operating earnings; expect the investment mark to create a **tough comparable** in the next few quarters and potential volatility if those private marks reverse.
2. **Operating momentum is genuinely excellent:** revenue +22%, gross and operating margins expanding 220–270 bps. Core demand (search, cloud) is accelerating — a bullish underpinning.
3. **Free-cash-flow compression is the key risk to watch.** FCF fell ~47% YoY as capex more than doubled. If AI capex keeps outrunning OCF, buyback-funded EPS accretion (a historical pillar of the GOOGL bull case) stalls. **FY2026 capex guidance and the pace of buyback resumption are the two catalysts to monitor.**
4. **Capital-allocation pivot:** buybacks paused to **$0** and **$31.4B of debt raised in one quarter**. A debt-funded AI build is a meaningful change — confirm it's temporary (timing around earnings/blackout) vs. a strategic shift.
5. **Hidden asset value:** the non-marketable equity book nearly doubled to **$101B** (+$37B in one quarter). This is a large, under-modeled value cushion (e.g., AI/space stakes) but adds reported-earnings volatility.
6. **Possible acquisition:** ~$8B jump in finite-lived intangibles implies a sizable M&A deal closed in Q1 — watch for amortization drag and strategic rationale.
7. **Balance sheet remains fortress-grade:** ~$46B net cash even after the debt ramp; $0.84 annualized dividend (+5%) still growing. Ample capacity to fund capex without solvency risk.

**Net stance from fundamentals:** Strong underlying operating acceleration and a fortress balance sheet support a constructive view — but the reported-profit optics are distorted by a one-time investment gain, and the **capex-driven FCF squeeze plus debt-financed build and paused buybacks** are the main things that could test the multiple. A trader should treat headline EPS with caution and focus on **operating margin trajectory, FY2026 capex guidance, and FCF inflection.**

---

## 9. Key Data Summary Table

| Category | Metric | Value | Comment |
|---|---|---|---|
| **Scale** | Q1'26 Revenue | $109.90B | +21.8% YoY (vs $90.23B) |
| | Shares outstanding | 12,116M | +28M QoQ (no buyback) |
| **Profitability** | Gross margin | 62.4% | +270 bps YoY |
| | Operating margin | 36.1% | +220 bps YoY |
| | Operating income | $39.70B | +29.7% YoY |
| | Reported net income | $62.58B | Inflated by investment gains |
| | Reported diluted EPS | $5.11 | +82% YoY |
| | **~Operating EPS (adj.)** | **~$2.6–2.7** | Excl. ~$36.9B equity gain |
| | Effective tax rate | 19.2% | vs 17.3% YoY |
| **Non-op / Quality** | Nonoperating income | $37.72B | ~49% of pretax income |
| | Equity securities FV gain | $36.92B | Non-cash mark-to-market |
| | Non-marketable equity value | $101.35B | +$37.3B QoQ |
| **Balance Sheet** | Total assets | $703.92B | +$108.6B QoQ |
| | Total liabilities | $225.17B | +$45.2B QoQ |
| | LTD (carrying) | $80.31B | +$31.2B QoQ (debt raise) |
| | Cash + ST investments | $126.84B | Net cash ~$46B |
| | New finite intangibles (net) | $9.25B | Implies ~$8B acquisition |
| **Cash Flow** | Operating cash flow | $45.79B | +26.7% YoY |
| | CapEx (PP&E) | $35.67B | ~2.1x YoY (AI build) |
| | **Free cash flow** | **$10.12B** | **−47% YoY** |
| | Buybacks | $0 | Paused vs $15.07B Q1'25 |
| | Debt raised (net) | $31.38B | Funds capex/investments |
| | Dividends paid | $2.54B | $0.21/sh (+5%) |
| **Multi-yr Trend** | FY25 OCF | $164.71B | vs $125.30B FY24, $101.75B FY23 |
| | FY25 CapEx | $91.45B | vs $52.54B FY24, $32.25B FY23 |
| | FY25 FCF | ~$73.27B | Flat despite OCF growth (capex drag) |
| **Governance** | Insider transactions | N/A | Data unavailable — not inferred |

*All figures from SEC XBRL filings (Q1 2026 10-Q filed 2026-04-30; FY2025 10-K filed 2026-02-05). Adjusted operating EPS is an analyst approximation (reported pretax minus the ~$36.9B equity gain, taxed at 19.2%, divided by ~12.25B diluted shares).*