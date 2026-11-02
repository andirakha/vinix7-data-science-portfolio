# Module 8 - Machine Learning Modeling (Regression)

## Assignment context
Modeling applies AI algorithms to build models that predict from existing data. The module offered two options. This repository holds **Option A: regression model on a structured dataset**, covering the workflow from data understanding to evaluation.

## Files
| File | Description |
|---|---|
| `ml_regression_auto_mpg.ipynb` | Full workflow with outputs (data: [`../data/auto-mpg.csv`](../data/auto-mpg.csv)) |

## Dataset: Auto MPG
Fuel consumption (miles per gallon) of cars from the late 1970s to the early 1980s.

| Variable | Description | Type |
|---|---|---|
| `mpg` | Fuel efficiency (**target**) | Continuous |
| `cylinders` | Number of engine cylinders | Discrete |
| `displacement` | Engine displacement | Continuous |
| `horsepower` | Engine horsepower (initially text because of `?` values) | Continuous |
| `weight` | Car weight | Continuous |
| `acceleration` | Acceleration time | Continuous |
| `model year` | Model year | Ordinal |
| `origin` | Country of origin (1 = USA, 2 = Europe, 3 = Japan) | Categorical |
| `car name` | Car name (unique) | Categorical |

**Goal:** predict `mpg` from technical attributes.

## Preprocessing
1. **Missing values (`horsepower`):** `?` replaced with `NaN`, column cast to float, 6 missing values filled with the **median** (the histogram is right-skewed, so the median is more robust than the mean).
2. **`origin`:** mapped from codes to `USA` / `Europe` / `Japan` for EDA, then label-encoded before modeling.
3. **`car name`:** dropped, since a unique identifier is not a useful predictor.

## EDA and feature selection
- `mpg` is right-skewed. `displacement`, `horsepower`, and `weight` are right-skewed or bimodal; `acceleration` is close to normal.
- Strongest correlations with `mpg`: `weight` (-0.83), `displacement` (-0.80), `cylinders` (-0.78), `horsepower` (-0.77); `model year` is moderately positive (0.58). `acceleration` is the weakest (0.42).
- `cylinders`, `displacement`, `horsepower`, and `weight` are highly multicollinear, which a Random Forest tolerates.
- USA cars have clearly lower `mpg` than European and Japanese cars, so `origin` is relevant.

**Selected features:** `weight`, `horsepower`, `model year`, `origin`. `displacement` and `cylinders` overlap with `weight` / `horsepower`. `acceleration` has the weakest correlation.

## Modeling
- **Algorithm:** `RandomForestRegressor` (`n_estimators=100`, `max_depth=None`, `random_state=42`, `n_jobs=-1`). It is robust, needs no feature scaling, handles non-linear relationships, and is insensitive to multicollinearity.
- **Split:** 80 / 20 (`random_state=42`): 318 training rows, 80 test rows.

## Results (test set)
| Metric | Value | Meaning |
|---|---|---|
| MAE | 1.70 | Predictions are off by about 1.70 MPG on average |
| MSE | 4.67 | Mean squared error (penalizes large errors) |
| RMSE | 2.16 | Typical prediction deviation of about 2.16 MPG |
| R² | 0.91 | The features explain about 91% of the variance in MPG |

The high R² with low MAE and RMSE indicates the model predicts MPG very well on this dataset.
