# Does a Four-Analyst LLM Trading Workflow Outperform a Single Agent?

**MSBD 5018 Group Project Proposal (Fall 2026)**  
**Topic:** Multi-Agent Collaboration  
**Team:** Zhou Xiaoyang (coordination and analysis), Zhou Runyu (system), Li Ziqi (data and evaluation), Zhao Tianyu (experiments)  
**Date:** October 15, 2026

## 1. Task Introduction

We study whether a staged organization of LLM agents improves trading decisions relative to a single agent receiving the same historical evidence. Starting from TradingAgents (Xiao et al., 2025), we retain four analysts (market, fundamentals, news, sentiment), bull/bear research, a trader, risk discussion, and a final manager. The system uses an LLM API, role-specific prompts, and workflow orchestration; it does not train new models. News and sentiment roles will analyze a shared historical news corpus from different perspectives. This preserves four-role organization while explicitly treating sentiment as news-derived rather than claiming a reproduction of historical social-media inputs.

## 2. Why This Task Is Important

Role specialization and debate may expose weak evidence, but additional stages also increase computation and can reinforce shared mistakes. A same-evidence single-agent comparison measures whether this organization offers a useful performance-cost trade-off. It does not, by itself, isolate collaboration from additional inference budget. Trading provides measurable downstream decisions, while also making information timing, execution rules, model changes, and reproducibility central to the study. We therefore evaluate both financial outcomes and operational cost, report negative findings, and distinguish historical input filtering from protection against pretrained knowledge of past events.

## 3. Proposed Methodology

**Controlled systems and data.** We pin the upstream code and our adapter, and use the same DeepSeek Flash model and verified thinking configuration across conditions. We record served model IDs, request settings, prompts, outputs, data hashes, and actual calls/tokens; temperature zero is not treated as a determinism guarantee. AAPL, GOOGL, and AMZN receive matched bundles of cached Yahoo prices/corporate actions, SEC facts, and timestamped historical news. News acquisition, coverage checks, and point-in-time validation are prerequisites, not completed work. Both news roles and the single-agent control receive the same frozen news texts. Cross-date learning memory and automatic reflection are excluded to avoid unequal histories and uncontrolled retrieval.

**Experiments.** A protocol-adapted reproduction targets January-March 2024, subject to news coverage and budget validation. The main study covers July-August 2026: the first 25 trading days (July 1-August 5) are used for development, and the last 18 (August 6-31) are reserved for final evaluation. We compare the four-analyst workflow with a same-evidence single agent; Buy and Hold, SMA(20/50), and MACD(12/26/9) provide free baselines. A development-set no-debate ablation examines bull/bear exchange. On November 3, development evidence selects exactly one workflow change, frozen before the final held-out comparison.

**Evaluation and feasibility.** Final ratings map to long-only binary positions: Buy/Overweight to invested, Underweight/Sell to cash, and Hold to the previous position. Decisions execute at the next session's open, with a total 10-bps cost per unit turnover. We report compounded net return, annualized Sharpe, maximum drawdown, and paired differences by stock, alongside API cost, tokens, latency, and failures. A staged pilot, up to 20 four-analyst decisions, checks feasibility within an $80 total API budget. Optional ablations and extended reproduction have lower priority than the main comparison. Historical-input limitations, a short holdout, and mutable API models limit generalization; negative results will be reported.

**Deliverables.** The proposal is due October 17; main results November 17; an ACL-format report of at most eight pages, reproducible code, data references, prompts, and experiment manifests December 9. Zhou Runyu implements the systems; Li Ziqi owns evidence and backtesting; Zhao Tianyu runs experiments and cost accounting; Zhou Xiaoyang coordinates protocol decisions, analysis, and the final report.

**References:** Xiao et al. (2025), TradingAgents, arXiv:2412.20138. Du et al. (2023), Improving Factuality and Reasoning in Language Models through Multiagent Debate, arXiv:2305.14325. DeepSeek API documentation, models/pricing and thinking mode (accessed October 15, 2026).
