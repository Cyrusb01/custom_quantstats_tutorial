import quantstats as qs


btc = qs.utils.download_returns("BTC-USD")
spy = qs.utils.download_returns("SPY")

# Quantstats custom_colors takes a list, this dictionary is just to show what each color means
colors = {
    "benchmark": "white",
    "strategy": "#FF9900",
    "rolling beta": "grey",
    "nothing": "orange",
    "nothing2": "blue",
    "dotted line": "red",
}

q_colors = list(colors.values())
logo = "new_logo.png"
b_color = "#13151E"

qs.reports.html(
    btc,
    benchmark=spy,
    strategy_name="Bitcoin",
    benchmark_name="SPY",
    custom_colors=q_colors,
    background_color=b_color,
    logo=logo,
    title="Bitcoin vs. SPY Tearsheet",
    company="Blockforce Capital",
    output="strat_tearsheet.html",
)
