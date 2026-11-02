# Module 4 - Exploratory Data Analysis (EDA): Customer Behavior

## Assignment context
EDA is the early investigation of data to find patterns, detect anomalies, test hypotheses, and check assumptions using descriptive statistics and visualization. It sits in the Data Understanding phase. The task was to explore the cleaned dataset from Module 3 with basic statistics and charts, then document and narrate the patterns found. Tools: Python, pandas, matplotlib, seaborn.

## Files
| File | Description |
|---|---|
| [`eda_customer_behavior.ipynb`](eda_customer_behavior.ipynb) | Full EDA report with outputs. Reads `data/processed/mall_customers_clean.csv` (output of [Module 3](../module-03-data-cleaning/)) |

## Objective 1 - Descriptive statistics
| Variable | Key figures | Reading |
|---|---|---|
| Age | mean 38.85, median 36, range 18-70 | Fairly mature customer base that still includes many young adults |
| Annual income (k USD) | mean 60.51, std 26.12, range 15-132 | Wide income spread |
| Spending score | mean 50.2, median 50, range 1-99 | Roughly symmetric, covers very frugal to very free-spending customers |
| Gender | 112 female, 88 male | Slightly more female customers |

## Objective 2 - Visual analysis
**Q1. How is customer age distributed? Does an age group stand out?**
A histogram with a KDE curve shows a peak between 20 and 40 years, concentrated around 30-35. The count drops sharply after 40 and is smallest above 60.

**Q2. How does average spending score compare between male and female customers?**
Female 51.53 vs male 48.51. The gap is small, so there is no strong gender difference in shopping behavior, although women score slightly higher.

**Q3. Is annual income related to spending score?**
A scatter plot shows no simple linear relationship. High income does not imply a high spending score. Instead, five groups are visible:
1. Low income, high score - free spenders
2. Low income, low score - frugal, low income
3. Mid income, mid score - the large moderate group
4. High income, high score - the "ideal" customers
5. High income, low score - high income but very frugal

## Objective 3 - Findings and hypotheses
**Findings**
1. The core customer base is young adults (20-40).
2. Gender is not a main driver of shopping behavior. Gender-only marketing is likely ineffective.
3. Segmentation is more informative than simple correlation: five distinct segments emerge from income x spending score.

**Hypotheses**
1. Personalized marketing by segment (e.g., luxury promotions for "high income, high score", discounts for "low income, high score") will convert much better than mass campaigns.
2. The "high income, low score" group probably prioritizes saving or investing, making them a target for financial products or durable, high-quality goods rather than consumer goods.

These hypotheses are tested in [Module 6](../module-06-statistical-analysis/).
