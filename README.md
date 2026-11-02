# VINIX7 Data Science Training Portfolio

A recap of the assignments from the **VINIX7** data science training program, a 10-module course covering the full workflow: data acquisition, cleaning, exploratory analysis, visualization, statistical testing, dashboards, machine learning, clustering, and data storytelling. The assignments were completed as part of a team. This repository consolidates and translates the work into English.

## Modules

| # | Module | Topic | Deliverable |
|---|---|---|---|
| 1 | [Data Diary](module-01-data-diary/) | Data sense and insight framework | Write-up |
| 2 | [Data Acquisition](module-02-data-acquisition/) | Dataset search, primary data design | Dataset profile, survey design |
| 3 | [Data Cleaning](module-03-data-cleaning/) | Outliers, missing values, duplicates, data types | Notebook + report |
| 4 | [Exploratory Data Analysis](module-04-eda/) | Descriptive stats, visual analysis, hypotheses | Notebook + report |
| 5 | [Data Visualization](module-05-data-visualization/) | Communicating insights with static charts | Notebook + report |
| 6 | [Statistical Analysis](module-06-statistical-analysis/) | t-tests, Pearson correlation | Notebook + report |
| 7 | [Interactive Dashboard](module-07-interactive-dashboard/) | Panel + hvPlot dashboard (Auto MPG) | Python app |
| 8 | [ML Regression](module-08-ml-regression/) | Random Forest regression (Auto MPG) | Notebook + report |
| 9 | [Clustering](module-09-clustering/) | K-Means customer segmentation | Notebook + report |
| 10 | [Data Storytelling](module-10-data-storytelling/) | From insight to actionable recommendations | Slides + poster (PDF) + summary |

## Repository structure

```
vinix7-data-science-portfolio/
├── README.md
├── requirements.txt              # shared dependencies for the notebooks
├── data/                         # datasets and download instructions
├── module-01-data-diary/
├── module-02-data-acquisition/
├── module-03-data-cleaning/      # notebook 
├── module-04-eda/                # notebook
├── module-05-data-visualization/ # notebook
├── module-06-statistical-analysis/
├── module-07-interactive-dashboard/  # dashboard_app.py (own requirements.txt)
├── module-08-ml-regression/      # notebook
├── module-09-clustering/         # notebook
└── module-10-data-storytelling/  # README + slides & poster PDF
```

Each module folder has its own `README.md` with the assignment context, approach, and results.

## Datasets

**Mall Customers** (modules 2-6, 9, 10) and **Auto MPG** (modules 7, 8) are included in [`data/`](data/), along with the cleaned Mall Customers file generated in module 3. See [`data/README.md`](data/README.md) for sources and schema.

## Quick start

```bash
git clone github.com/andirakha/vinix7-data-science-portfolio
cd vinix7-data-science-portfolio
python -m venv venv && source venv/bin/activate   # Windows: .\venv\Scripts\activate
pip install -r requirements.txt

jupyter notebook   # modules 3-6 and 9 read the datasets in data/
```

The dashboard has its own dependencies and run instructions: see [module 7](module-07-interactive-dashboard/README.md).

## Notes

- All notebooks are committed with their executed outputs (charts and tables are in English).
- `data/processed/mall_customers_clean.csv` is produced by `module-03-data-cleaning/data_cleaning.ipynb`. Re-run that notebook before modules 4-6 if you change the raw data.
- Results quoted in each module README come from the original assignment runs.

## Tech stack

Python, pandas, NumPy, matplotlib, seaborn, scikit-learn, SciPy, Panel, hvPlot, Jupyter.
