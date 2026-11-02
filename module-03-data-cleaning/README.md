# Module 3 - Data Cleaning

## Assignment context
Based on the principle "garbage in, garbage out", this module is about reporting data quality: inspecting the dataset chosen in Module 2, then identifying, handling, and documenting its problems. At least three of the four basic data issues (outliers, missing values, duplicates, wrong data types) had to be checked, using Python and pandas.

## Files
| File | Description |
|---|---|
| [`data_cleaning.ipynb`](data_cleaning.ipynb) | Full cleaning report with outputs. Reads `data/Mall_Customers.csv` and writes `data/processed/mall_customers_clean.csv`, which modules 4-6 use |

## 1. Initial data profiling
- 200 rows x 5 columns: `customer_id`, `gender`, `age`, `annual_income_k_usd`, `spending_score` (raw column names are standardized in the notebook).
- Gender split: 112 female, 88 male.
- Age 18-70 (mean 38.85); annual income 15-137k USD (mean 60.56k); spending score 1-99 (mean 50.20, median 50, so the distribution is roughly symmetric).

## 2. Cleaning process
| Issue | Finding | Action |
|---|---|---|
| **Outliers** | Box plots showed a potential outlier in annual income; the IQR method (Q1 = 41.5, Q3 = 78, IQR = 36.5, upper bound = 132.75) flagged **2 rows** (income 137) | **Capping** at the upper bound instead of deleting, to keep the rows while limiting distortion of means and models |
| **Missing values** | None in any column | No action |
| **Duplicates** | None (checked on customer ID) | No action |
| **Data types** | `gender` stored as a string column. Income became `float64` after capping | `gender` -> `category`, income -> `int64` |

After capping, mean income moved from 60.56k to about 60.52k and the standard deviation from 26.26 to 26.14.

## 3. Conclusion
The dataset is now clean, consistent, and ready for exploratory analysis (Module 4), segmentation, or predictive modeling. Two of the four checks required action (outliers, data types). The other two were already in good shape.

> **CSV vs Parquet:** CSV opens everywhere but does not preserve data types, whereas Parquet is more efficient and keeps the original types (e.g., `category`). The original assignment shared both formats. This repository saves the cleaned data as CSV.
