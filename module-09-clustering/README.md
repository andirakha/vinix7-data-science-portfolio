# Module 9 - Clustering (Customer Segmentation)

## Assignment context
This module covers unsupervised learning. Unlike Module 8 (supervised regression with a target column), clustering works on unlabeled data to find natural groups, with uses such as customer segmentation, document grouping, and anomaly detection. This repository holds **Option A1: customer segmentation on structured data** using K-Means, the elbow method, and silhouette score.

## Files
| File | Description |
|---|---|
| `customer_segmentation_clustering.ipynb` | EDA, preprocessing, K selection, final model, and cluster plot |

**Data:** reads [`data/Mall_Customers.csv`](../data/Mall_Customers.csv) (see [`data/README.md`](../data/README.md)). The notebook is committed with its outputs.

## Dataset
Mall Customer Segmentation Data: 200 customers, 5 columns: `CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, `Spending Score (1-100)` (1 = frugal, 100 = big spender).

## Data checking and preparation
- No missing values and no duplicates.
- **Feature selection:** only `Annual Income (k$)` and `Spending Score (1-100)` are used. age, gender, and ID are excluded.
- **Standardization:** `StandardScaler`, because K-Means is distance-based and sensitive to scale.

## Exploratory analysis
- Most customers are 30-40 years old. Most incomes are between 40k and 80k USD. Spending scores concentrate around 40-60.
- 112 female and 88 male customers.
- The income vs spending scatter plot visually suggests **5 clear clusters**. The pair plot confirms income x spending score is the most useful pair.
- Median and IQR of spending score are very similar for male and female customers: no meaningful gender difference.

## Modeling
- **Algorithm:** K-Means (`init='k-means++'`, `n_init=10`, `random_state=42`) - efficient, widely used, and suited to the roughly spherical clusters seen in the EDA.
- **Choosing k (elbow method):** WCSS drops sharply from K=1 to K=4 and flattens after K=5, a clear elbow at **K=5**.

## Evaluation (silhouette score)
| K | 2 | 3 | 4 | **5** | 6 |
|---|---|---|---|---|---|
| Silhouette | 0.3213 | 0.4666 | 0.4939 | **0.5547** | 0.5399 |

The highest score is at K=5, confirming the elbow method.

## Cluster interpretation
| Profile | Characteristics | Interpretation |
|---|---|---|
| Low income, high spending | Spends a lot despite lower income | Target for promotions and loyalty programs |
| Mid income, mid spending | Middle of the plot | Standard / average customers |
| High income, low spending | Wealthy but careful | Cautious spenders |
| High income, high spending | High purchasing power and willingness to spend | Ideal / VIP customers - top priority |
| Low income, low spending | Frugal with limited income | Lower priority |
