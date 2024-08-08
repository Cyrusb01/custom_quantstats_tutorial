import quantstats as qs

btc = qs.utils.download_returns("AAPL")
spy = qs.utils.download_returns("SPY")

btc.index = btc.index.tz_localize(None)
spy.index = spy.index.tz_localize(None)

btc = btc[btc.index > "2012-01-01"]
spy = spy[spy.index > "2012-01-01"]

print(btc)
# Quantstats custom_colors takes a list, this dictionary is just to show what each color means
colors = {
    "benchmark": "white",
    "strategy": "#FF9900",
    "rolling beta": "grey",
    "axis font": "white",
    "nothing2": "blue",
    "dotted line": "red",
    "graph titles": "white",
}

q_colors = list(colors.values())
logo = "new_logo.png"
alpha = (
    1  # 1 is not transparent, 0 is transparent. This is for the graph background color
)
graph_background_color = "#191E2B"
font_path = "Be_Vietnam_Pro/"
fontname = "Be Vietnam Pro"

qs.reports.html(
    btc,
    benchmark=spy,
    strategy_name="Apple",
    benchmark_name="SPY",
    custom_colors=q_colors,
    bg_graph=graph_background_color,
    alpha=alpha,
    stylesheet="style.css",
    logo=logo,
    fontname=fontname,
    font_path=font_path,
    title="Apple vs. S&P 500 Tearsheet",
    company="Blockforce Capital",
    output="strat_tearsheet.html",
)
