# Quick Commerce (Q-Commerce) Platform Analysis

## Dataset Overview
The dataset comprises one million order records across eight platforms, covering transaction lifecycle from order placement to delivery completion. Key fields/columns include: **Order ID**, **Company(Platform)**, **City**, **Customer Age**, **Order Value(INR)**,    **Delivery Time(Minuites)**, **Distance(Km)**, **Items Count**, **Product Category**, **Payment Method**, **Customer Rating(1-5)**, **Discount Applied(binary flag)** and **Delivery Partner Rating(1-5)**

## Business Context
This analysis answers four core business questions:
1. Which platform generates the most revenue and why?
2. Who are the customers and what are they buying?
3. Which platforms are operationally the fastest and most consistent?
4. Does offering discounts actually increase order value?

## Methodology
### Data Quality and Cleaning
A systematic audit prior to analysis identified four categories of data quality issues. Each was resolved through a documented analytically justified treatment.

|Issue|Scale|Treatment|Rationale|
|-----|-----|---------|---------|
|City — null values|  ~5.2% of rows  |  Filled with 'Other'  |  Rows otherwise complete; dropping would bias city-level analysis  |
|Items Count — nulls|  Small subset  |  Rows dropped  |  Core metric;imputation would fabricate basket size data  |
|Customer rating — nulls|  Partial  |  Group-median by platform  |  Median differ by platform; global impute erases differentiation  |
|Partner rating — nulls|  Partial  |  Group-mean by platform  |  Missingness confirmed random via delivery time correlation check  |


#### Outlier Treatment
Outlier detection used the Interquartile Range (IQR) method on four continuous business metrics: Order Value, Delivery Time, Distance and Items Count.
Outlier rows were not discarded but rather retained in a separate dataset(~24,500 rows) and analysed independently as the Bulk Order Segment.

### Statistical Methods
The **Mann-Whitney U** test was used for all order value comparisons(discount vs. no-discount groups). This non-parametric test was selected because order value distribution are right-skewed — the majority of orders are low-value with a long tail of high-value purchases. The standard t-test, which assumes normally distributed data, would produce unreliable results on such distributions. Mann-Whitney U operates on value ranks rather than raw numbers, making it robust to distributional skew.

**Pearson's Correlation** for delivery time vs. partner rating analysis was restricted to original non-null ratings only to avoid the artificial suppression introduced by group-mean imputation.


## Key Insights 












## Data Access
Due to the file size(91MB), the raw dataset is not included in this repository. To replicate this analysis, please place the source CSV in the /data folder.