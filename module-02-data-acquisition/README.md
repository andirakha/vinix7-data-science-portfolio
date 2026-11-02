# Module 2 - Data Acquisition

## Assignment context
Data acquisition is the foundation of any data project and maps to the Business Understanding and Data Understanding phases of CRISP-DM. The assignment had two goals: **find** a relevant public (secondary) structured dataset, and **design** a primary data collection plan for when the needed data is not available. The dataset chosen here is reused in Modules 3-6, 9, and 10.

## Dataset: Mall Visiting Customer Data
- **Source:** Kaggle - [Mall Visiting Customer Data](https://www.kaggle.com/datasets/krishnaraj30/mall-visiting-customer-data)
- **Type:** Structured / tabular
- **Size:** 200 rows (one per unique customer), 5 columns: customer ID, gender, age, annual income, spending score
- **Purpose:** Customer segmentation analysis

### Columns of interest
| Column | Meaning | Data type |
|---|---|---|
| Annual income (thousand USD) | Estimated annual income. A value of 15 means $15,000 | Numerical, continuous |
| Spending score | Score from 1 to 100 assigned by the mall from shopping behavior. Higher means more frequent / higher spending | Numerical, discrete |
| Age | Customer age in years | Numerical, discrete |

## Potential analyses (hypotheses)
1. **Income vs spending:** Is annual income related to spending score? Hypothesis: high-income customers also have high spending scores.
2. **Target segments:** Can customers be grouped (e.g., "frugal but high income", "big spender but low income") from income and spending score to find the most promising marketing targets?
3. **Age effect:** How does age correlate with spending score? Do certain age ranges spend more?
4. **Gender differences:** Is there a significant difference in mean spending score between male and female customers?

## Primary data collection design (survey)
**Replication questions** (to collect the same variables as the public dataset):
- Gender - "Please state your gender according to your identity."
- Age - "What is your current age in full years?"
- Annual income (thousand USD) - "What is your approximate average annual income? Answers are used for analysis only and kept confidential."

**New questions** (to enrich the analysis):
- Mall visit frequency in the last month: 1 time / 2-3 times / 4-5 times / more than 5 times
- Shopping preference (main purpose of a visit): fashion / food & beverage / electronics & gadgets / entertainment / other
- Typical time spent in the mall: under 1 hour / 1-2 hours / 3-4 hours / more than 4 hours
