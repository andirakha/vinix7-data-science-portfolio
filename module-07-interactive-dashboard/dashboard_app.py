"""Interactive Auto MPG dashboard built with Panel and hvPlot.

Run from this folder:
    panel serve dashboard_app.py --show
"""
from pathlib import Path

import pandas as pd
import panel as pn
import hvplot.pandas  # noqa: F401  (registers the .hvplot accessor)

# ==============================================================================
# 1. SETUP & DATA LOADING
# ==============================================================================
pn.extension('tabulator', sizing_mode="stretch_width")

template = pn.template.FastListTemplate(
    title='Car Fuel Efficiency (MPG) Analysis Dashboard',
    sidebar_width=320,
    accent_base_color="#1F618D",
    header_background="#1F618D",
)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "auto-mpg.csv"

try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    pn.pane.Markdown(
        f"## Error: dataset not found\nExpected `auto-mpg.csv` at `{DATA_PATH}`."
    ).servable()
    raise SystemExit(1)

# Cleaning: 'horsepower' contains '?' placeholders -> numeric, fill with median
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].median())

origin_map = {1: 'USA', 2: 'Europe', 3: 'Japan'}
df['origin'] = df['origin'].map(origin_map)

# ==============================================================================
# 2. WIDGETS
# ==============================================================================
template.sidebar.append(
    pn.pane.Markdown("### Interactive Filters")
)

origin_select = pn.widgets.Select(
    name='Filter by Country of Origin',
    options=['All'] + list(df['origin'].unique())
)
year_slider = pn.widgets.RangeSlider(
    name='Model Year Range',
    start=int(df['model year'].min()),
    end=int(df['model year'].max()),
    value=(int(df['model year'].min()), int(df['model year'].max())),
    step=1
)
bins_slider = pn.widgets.IntSlider(
    name='Number of Bins for MPG Histogram',
    start=5,
    end=50,
    step=1,
    value=20
)
characteristic_select = pn.widgets.Select(
    name='Characteristic to Compare',
    options=['mpg', 'horsepower', 'weight', 'acceleration']
)

template.sidebar.append(origin_select)
template.sidebar.append(year_slider)
template.sidebar.append(bins_slider)
template.sidebar.append(characteristic_select)

# ==============================================================================
# 3. INTERACTIVE DATA PIPELINE
# ==============================================================================
@pn.depends(origin_select.param.value, year_slider.param.value)
def get_filtered_data(origin, year_range):
    filtered_df = df[(df['model year'] >= year_range[0]) & (df['model year'] <= year_range[1])].copy()
    if origin != 'All':
        filtered_df = filtered_df[filtered_df['origin'] == origin]
    return filtered_df

# ==============================================================================
# 4. PLOTTING FUNCTIONS (short titles)
# ==============================================================================

def plot_mpg_distribution(bins, filtered_data):
    return filtered_data['mpg'].hvplot.hist(
        bins=bins,
        title="MPG Distribution",
        xlabel="Miles Per Gallon (MPG)", ylabel="Number of Cars",
        height=350, responsive=True, color="#1F618D"
    )

def plot_mpg_vs_cylinders(filtered_data):
    avg_mpg = filtered_data.groupby('cylinders')['mpg'].mean().reset_index()
    return avg_mpg.hvplot.bar(
        x='cylinders', y='mpg',
        title="Average MPG by Cylinders",
        xlabel="Number of Cylinders", ylabel="Average MPG",
        height=350, responsive=True, color="#1F618D"
    ).opts(yformatter='%.1f')

def plot_weight_vs_mpg(filtered_data):
    origin_value = filtered_data['origin'].unique()

    color = '#1F618D'

    if len(origin_value) == 1:
        if origin_value[0] == 'USA':
            color = "#1FAAB4"
        elif origin_value[0] == 'Europe':
            color = '#2CA02C'
        elif origin_value[0] == 'Japan':
            color = '#D62728'

        return filtered_data.hvplot.scatter(
            x='weight',
            y='mpg',
            color=color,
            title=f"Car Weight vs MPG ({origin_value[0]})",
            xlabel="Car Weight (weight)",
            ylabel="Miles Per Gallon (MPG)",
            height=350,
            responsive=True
        )

    else:
        return filtered_data.hvplot.scatter(
            x='weight',
            y='mpg',
            by='origin',              # color by country of origin
            cmap='Category10',
            title='Relationship Between Weight and MPG',
            xlabel="Car Weight (weight)",
            ylabel="Miles Per Gallon (MPG)",
            height=350,
            responsive=True,
            legend='top_right'
        )

def plot_avg_mpg_trend(filtered_data):
    avg_mpg = filtered_data.groupby('model year')['mpg'].mean().reset_index()
    return avg_mpg.hvplot.line(
        x='model year',
        y='mpg',
        title='Average MPG Trend by Model Year',
        xlabel='Model Year',
        ylabel='Average MPG',
        line_width=3,
        color='#1F618D',
        height=350,
        responsive=True
    )

def plot_origin_characteristics(characteristic, filtered_data):
    return filtered_data.hvplot.box(
        y=characteristic, by='origin',
        title=f"'{characteristic.title()}' by Country of Origin",
        ylabel=characteristic.title(), xlabel="Country of Origin",
        height=350, responsive=True
    )

# ==============================================================================
# 5. DASHBOARD ASSEMBLY (pn.Card)
# ==============================================================================
# Bind widgets to the plotting functions
plot1 = pn.bind(plot_mpg_distribution, bins=bins_slider, filtered_data=get_filtered_data)
plot2 = pn.bind(plot_mpg_vs_cylinders, filtered_data=get_filtered_data)
plot3 = pn.bind(plot_weight_vs_mpg, filtered_data=get_filtered_data)
plot4 = pn.bind(plot_avg_mpg_trend, filtered_data=get_filtered_data)
plot5 = pn.bind(plot_origin_characteristics, characteristic=characteristic_select, filtered_data=get_filtered_data)

# Wrap each plot in a card with a clear header
card1 = pn.Card(plot1, title="1. What is the distribution of MPG values?", collapsible=False)
card2 = pn.Card(plot2, title="2. Does average MPG differ by number of cylinders?", collapsible=False)
card3 = pn.Card(plot3, title="3. How are car weight and MPG related?", collapsible=False)
card4 = pn.Card(plot4, title="4. How does average MPG change from year to year?", collapsible=False)
card5 = pn.Card(plot5, title="5. Do car characteristics differ by country of origin?", collapsible=False)

# Arrange the cards in the main layout
template.main.append(
    pn.Column(
        pn.pane.Markdown(
            """
            ### Interactive Analysis of the Auto MPG Dataset
            Use the controls in the **left sidebar** to filter the data and change the visualization parameters.
            """,
            max_width=900, align='center'
        ),
        pn.Tabs(
            ("Question 1", pn.Row(card1)),
            ("Question 2", pn.Row(card2)),
            ("Question 3", pn.Row(card3)),
            ("Question 4", pn.Row(card4)),
            ("Question 5", pn.Row(card5))
        )
    )
)

# ==============================================================================
# 6. MAKE IT SERVABLE
# ==============================================================================
template.servable()
