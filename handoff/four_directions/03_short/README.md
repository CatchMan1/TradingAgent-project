# 03 做空

两种方案必须分别命名：

1. `overlay/experiments/short_only_month.py`：冻结原报告，在原 Underweight/Sell 日增加显式 `open_short` 判断。未获批准走原规则；原 Hold 不被当成允许继续持空，每天未获短仓许可则回补。它是节省 API 的审批叠加实验，不是原最终经理原生输出三分类。
2. `replay.py` / `overlay/experiments/plot_underweight_short.py`：不问模型，直接把 Underweight 映射为 Sell，调用 `simulate(..., short=True)`；Buy/Overweight→+1、Sell→−1、Hold保持股数（包括空头）。这是机械映射反事实实验，不应包装成模型的做空判断能力。

共享引擎：`shared/overlay/experiments/optimization_engine.py`。`short=False` 恢复原多头/现金路径。卖空卖出借来的股票、形成负股数；回补买入关闭负股数；逆转方向收取双边成交费用。默认单边10bps、借券年费3%，按日历日计借券费，空头支付股息。

显式审批路径有开盘保证金检查；机械映射路径没有该检查。两者都没有盘中强平、借券可得性/召回、滑点模型。不要声称已覆盖全部实盘约束。

`fixtures/` 保存三个股票的价格、评级和预期指标，支持完全离线复现。十月只有10月1—8日开仓/调仓，10月9日开盘结算；不是整月。独立月度账户与连续账户分别计算。所有价格输入仅用于成交/估值；历史最终评级作为冻结信号。

测试：`tests/test_short_only.py`、`tests/test_optimizations.py`。同学可增加独立 short 决策 schema 和借券/保证金模块，但需要保持原版关闭路径一致，不能把比例或情绪一起混入。
