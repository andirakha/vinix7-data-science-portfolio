# Module 7 - Interactive Dashboard (Auto MPG)

## Assignment context
Dashboards are a form of deployment in the data science life cycle: results are presented so stakeholders can explore them on their own. This module introduces Business Intelligence concepts and uses a new, shared dataset (**Auto MPG**) with no cleaning or EDA required. This repository holds **Option B: programmatic dashboard with Panel and hvPlot**.

## Features
- **Five analysis questions** answered with interactive charts (one tab each).
- **Global filters:** country of origin (USA, Europe, Japan) and model-year range.
- **Specific controls:** histogram bin slider and a dropdown to choose the characteristic to compare.
- **Organized layout** with `pn.Tabs` and `pn.Card`.

## Tech stack
Python 3.9+, [Panel](https://panel.holoviz.org/), [hvPlot](https://hvplot.holoviz.org/), pandas.

## Run locally
From the repository root:

```bash
cd module-07-interactive-dashboard
python -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
panel serve dashboard_app.py --show
```

The app reads the dataset from [`../data/auto-mpg.csv`](../data/auto-mpg.csv).

## Analysis questions, chart choice, and widgets
| # | Question | Chart | Interactive widget | Why |
|---|---|---|---|---|
| 1 | What is the distribution of MPG values? | Histogram | Bins slider | Best for the frequency distribution of a continuous variable. Bins control the level of detail |
| 2 | Does average MPG differ by number of cylinders? | Bar chart | Country-of-origin filter | Bar length maps directly to the mean. Filtering by origin gives deeper comparisons |
| 3 | How are weight and MPG related? | Scatter plot | Color by country of origin | Shows the direction and shape of the relationship and whether it differs by origin |
| 4 | How does average MPG trend by model year? | Line chart | Year-range slider | Standard choice for time series. The slider lets users focus on a period |
| 5 | Do car characteristics differ by origin? | Box plot | Characteristic dropdown (MPG, horsepower, weight, acceleration) | Compares medians, spread, and outliers across groups |

## Key insights
1. **Fuel efficiency improved over time.** Average MPG in the early 1980s is far higher than in the early 1970s, suggesting engine technology gains and an industry shift toward efficiency.
2. **Weight is a key factor.** There is a strong negative correlation between weight and MPG across all origins. American cars tend to be heavier with lower MPG, especially in the early years.
3. **Clear differences by origin.** Japanese cars consistently show the highest MPG and lowest weight. American cars tend to have more cylinders, more weight, and lower MPG. European cars fall in between.
4. **Most cars fall in the 15-25 MPG range.** A significant group exceeds 30 MPG, mostly Japanese cars from the later model years.

Overall, the dashboard shows the industry moving toward lighter, smaller-engine, much more fuel-efficient vehicles between 1970 and 1982.

## Interaction scenarios
- Filter to **Japan only** to analyze Japanese cars.
- Set the year range to **1975-1980** to look at the oil-crisis era.
- Switch the box plot to **horsepower** to compare power across origins.
