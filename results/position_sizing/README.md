# Position sizing experiments

Two separate experiments, evaluated with close-to-next-close simple returns and additive NAV. Initial position is cash, turnover costs 10 basis points per unit, cash earns no interest, and no extra terminal sale is imposed. Stocks are separate accounts, not a combined portfolio. API costs are excluded.

## Fixed 25-percentage-point execution

`fixed_25pp_full/`: June 30 close to October 9 close, 2026. AAPL, GOOGL, AMZN each have 71 intervals. Original archived five-tier ratings are held fixed. Buy sets 100%, Overweight adds 25 percentage points capped at 100%, Hold retains the target, Underweight subtracts 25 points floored at zero, Sell sets zero. Binary execution maps Buy/Overweight to 100% and Sell/Underweight to zero.

All 213 used ratings are Overweight, Underweight or Hold; Buy and Sell branches never activate. Returns change from +20.79% to +11.41% (AAPL), -3.61% to -9.17% (GOOGL), and +15.77% to -3.69% (AMZN). Maximum drawdown magnitudes increase from 2.07% to 2.40%, 8.20% to 13.09%, and 4.32% to 9.50%. Trading fees decline but do not offset unfavorable exposure timing. GOOGL's July 22 signal leaves 75% exposure before a 7.13% next-interval fall. AMZN's July 31 signal enters at 25% before a 4.58% rise.

## Manager-selected continuous targets

`manager_aapl_aug/`: AAPL only, July 31 close to August 31 close, 2026, 21 intervals. Source is the completed full-pipeline manager experiment (`full_pipeline_position_2026aug_sep`, group AAPL_08), not the later compact-risk rerun. `manager_decisions.csv` retains final rating, execution action and raw target, without model narrative. `replay_inputs.csv` carries targets forward on keep decisions, matching the previously reported standardized close-based comparison.

Net return is -0.23% versus the same-window binary baseline +0.65%. Drawdown is 0.36% versus 2.29%. Average exposure is 3.62% and maximum target 20%, versus binary average 28.57%. Targets shrink from 20% on August 5 to 0.25% on August 27. Lower exposure limits both losses and upside. The manager arm changes decisions and account context as well as sizing; it does not isolate numerical output format.

## Interpretation and limits

The two arms expose different problems: very low exposure in manager-selected weights, and slow entry/exit in fixed incremental execution. Neither supports a general performance improvement. Do not compare August manager totals directly with full-period fixed-step totals. Frozen signals were generated under their original execution/account assumptions; this replay does not establish how the model would respond to different positions. Historical input cutoff limitations remain. These are previously explored samples, not held-out validation.

## Reproduce

Run `python3 replay.py` from this folder (standard library only, no network or model calls). It rebuilds all daily returns, costs, NAV, drawdown and positions from `replay_inputs.csv` and checks them against the published ledgers. Original binary and buy-and-hold full-period ledgers were also reconciled against the main backtest archive before packaging. Daily CSVs, metrics and figures are included. No credentials, account records or private model reasoning are included.
