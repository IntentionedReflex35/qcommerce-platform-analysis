# Quick Commerce (Q-Commerce) Platform Analysis
### Competitive Intelligence Across 8 Indian Delivery Platforms

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=flat&logo=plotly&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-Statistical%20Testing-8CAAE6?style=flat&logo=scipy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)
![Status](https://img.shields.io/badge/Status-Complete-2E8B57?style=flat)

---

## Overview

This project delivers a structured competitive analysis of eight major Quick Commerce platforms operating in India, based on one million synthetic orders. The analysis spans the full analytical lifecycle — data auditing, cleaning, outlier treatment, exploratory analysis, statistical hypothesis testing and operational efficiency modelling — and concludes with six data-driven strategic recommendations.

Q-Commerce is one of the most operationally demanding segments in Indian e-commerce. Platforms like Blinkit, Zepto and Swiggy Instamart compete on three dimensions: **revenue**, **delivery speed**, and **customer satisfaction**. This analysis uses data to determine who is winning, why and where the next competitive battles will be fought.

---

## Business Questions

This analysis answers four core business questions:

| # | Question                                                       |
|---|----------------------------------------------------------------|
| 1 | Which platforms generate the most revenue and why?             |
| 2 | Who are the customers and what are they buying?                |
| 3 | Which platforms are operationally fastest and most consistent? |
| 4 | Does offering discounts actually increase order value?         |

---

## Key Findings

>  **Revenue — No dominant player.** The top 7 platforms sit within **~11%** of each other in total revenue. No platform holds a sustainable revenue moat — competition is decided on speed and experience, not scale.

>  **Demographics — The category defines the customer.** The **21–50 age band drives ~71%** of all orders, uniformly across every platform. Age distribution is a category-level trait, not a differentiator any single platform has developed.

>  **Delivery — Zepto leads on speed.** Zepto averages **9.6 minutes** delivery time and **0.839 km/min** — the fastest on both measures. Delivery time standard deviation is ~5 minutes across all platforms, indicating industry-wide infrastructure constraints rather than individual platform failures.

>  **Geography — Demand is nationwide.** The revenue gap between the #1 city (Gurgaon) and the #10 city (Pune) is only **~17%**. Metro concentration is not a viable long-term strategy.

>  **Discounts — Selection bias, not demand creation.** Discounted orders carry a **~42% higher average order value** (₹677 vs ₹477, Mann-Whitney U, p < 0.001) — but this reflects high-intent buyers seeking discounts, not discounts manufacturing demand. Blanket discount strategies leak margin without generating incremental basket growth.

>  **Bulk buyers — A distinct, underserved segment.** ~24,500 outlier orders represent a high-value cohort averaging **₹1,176 per order — 2.1× the standard customer**. 72.4% use discounts vs 39.3% in the main dataset. A formal B2B or subscription tier would capture this segment's revenue without eroding standard consumer pricing.

---

## Dataset

| Property   | Detail                                                                                                                                                                                                                                           |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Records    | 1,000,000 synthetic orders                                                                                                                                                                                                                       |
| Platforms  | Swiggy Instamart, Blinkit, Zepto, Big Basket, Flipkart Minutes, Amazon Now, Dunzo, Jio Mart                                                                                                                                                      |
| Cities     | 10 major Indian metros + unclassified                                                                                                                                                                                                            |
| Key Fields | Order ID, Company (Platform), City, Customer Age, Order Value (INR), Delivery Time (Minutes), Distance (Km), Items Count, Product Category, Payment Method, Customer Rating (1–5), Discount Applied (binary flag), Delivery Partner Rating (1–5) |
| Type       | Synthetic — generated to reflect realistic Q-Commerce distributions                                                                                                                                                                              |

> **Note on synthetic data:** This dataset was synthetically generated to reflect realistic Q-Commerce distributions. It was selected to allow demonstration of the complete analytical lifecycle — auditing, cleaning,
> outlier treatment, statistical testing, and strategic recommendation — without the access constraints of proprietary platform data. Findings
> are illustrative rather than operational claims about specific companies.

> Due to file size (~90MB), the raw dataset is not tracked by this repository.
> See [Reproducing This Analysis](#reproducing-this-analysis) for setup instructions.
 
---

## Methodology

### Data Quality and Cleaning

A systematic audit prior to analysis identified four categories of data quality issues. Each was resolved through a documented, analytically justified treatment:

| Issue                   | Scale         | Treatment                | Rationale                                                        |
|-------------------------|---------------|--------------------------|------------------------------------------------------------------|
| City — null values      | ~5.2% of rows | Filled with `'Other'`    | Rows otherwise complete; dropping would bias city-level analysis |
| Items Count — nulls     | Small subset  | Rows dropped             | Core metric; imputation would fabricate basket size data         |
| Customer Rating — nulls | Partial       | Group-median by platform | Medians differ by platform; global impute erases differentiation |
| Partner Rating — nulls  | Partial       | Group-mean by platform   | Missingness confirmed random via delivery time correlation check |


### Outlier Treatment

IQR detection was applied exclusively to four continuous business metrics: `Order_Value`, `Delivery_Time_Min`, `Distance_Km` and `Items_Count`. Rating columns and `Customer_Age` were explicitly excluded — ratings are bounded 1–5 by design (IQR fences on bounded scales are statistically meaningless) and age has no business rationale for exclusion within the plausible range.

Outlier rows were **not discarded**. They were retained in a separate dataset (~24,500 rows) and analysed independently as the **Bulk Order Segment** in Section 7 of the notebook — reflecting the principle that extreme values in transactional data frequently represent distinct customer archetypes rather than measurement errors.

### Statistical Methods

**Mann-Whitney U** was used for all order value comparisons (discount vs. no-discount groups). This non-parametric test was selected because order value distributions are right-skewed — the majority of orders are low-value with a long tail of high-value purchases. The standard t-test assumes normally distributed data and would produce unreliable results on such distributions. Mann-Whitney U operates on value ranks rather than raw numbers, making it robust to distributional skew.

**Pearson Correlation** for delivery time vs. partner rating analysis was restricted to originally non-null rating observations only, to avoid the artificial suppression introduced by group-mean imputation.

### Operational Efficiency Score

Platforms were ranked on a composite score combining **total order volume** and **average delivery speed (km/min)**. Both dimensions were Min-Max scaled to [0, 1] before combination — preventing unit dominance. Weights are equal by design as a methodologically neutral baseline; a parameterised variant would reflect business-specific priorities.

| Rank | Platform                     | Score Driver                       | Implication                                                         |
|------|------------------------------|------------------------------------|---------------------------------------------------------------------|
| 1    | Zepto                        | Highest delivery speed (km/min)    | Speed is the core differentiator; dark store density is likely high |
| 2–3  | Dunzo, Blinkit               | Short distances, fast times        | Strong hyperlocal infrastructure; volume is the limiting factor     |
| 4–6  | Swiggy, Big Basket, Flipkart | High volume, average speed         | Scale offsets moderate speed; revenue position is defensible        |
| 7    | Amazon Now                   | Mid-tier on both dimensions        | No operational differentiator; brand trust is the primary asset     |
| 8    | Jio Mart                     | Comparable distance, slow delivery | Logistics inefficiency — not a geography problem; correctable       |

---

## Strategic Recommendations

| #  | Recommendation                                                                                                                       | Anchored To |
|----|--------------------------------------------------------------------------------------------------------------------------------------|-------------|
| R1 | **Invest in dark store expansion** — speed gaps are the primary revenue differentiator, not brand or assortment                      | F1, F5      |
| R2 | **Replace blanket discounts with precision mechanics** — minimum-spend thresholds, cart-abandonment offers, and loyalty tiers        | F6          |
| R3 | **Formalise a B2B / bulk buyer subscription tier** — pre-negotiated pricing and dedicated SLA, protecting standard pricing integrity | F6, §7      |
| R4 | **Pursue hub-and-spoke geographic expansion** — secondary cities show near-equal demand density to top metros                        | F4          |
| R5 | **Invest in delivery partner training** — speed does not drive ratings; interpersonal quality and packaging care do                  | F5          |
| R6 | **Audit Jio Mart's routing and partner deployment** — delivery latency is an operations problem, not a geography problem             | F5, §6      |

---

## Project Structure

```
├── data/
│   ├── quick_commerce_data_raw.csv       # Raw dataset (not tracked — see note above)
│   ├── qcommerce_data_clean.csv          # Generated by notebook
│   ├── outlier_log_iqr.csv               # Generated by notebook
│   └── README.md
├── notebooks/
│   └── Analysis_Report.ipynb             # Main analysis — fully executed with outputs
├── plots/                                # All generated chart outputs
│   └── README.md                         
├── src/
│   └── config.py                         # Centralised path configuration
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Reproducing This Analysis

The notebook is committed with all outputs — executed cells, printed results and plots — so **no setup is required to review the analysis**. Simply open `notebooks/Analysis_Report.ipynb` directly on GitHub or view it on [nbviewer](https://nbviewer.org/) for full interactive rendering.

If you would like to run the notebook yourself:

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/qcommerce-platform-analysis.git
   cd qcommerce-platform-analysis
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add the raw dataset**
   Place `quick_commerce_data_raw.csv` inside the `data/` directory. The notebook will generate all cleaned and outlier datasets automatically on first run.
   Download `quick_commerce_data_raw.csv` data file [here](https://drive.google.com/file/d/1KT04J6Sy4sDrYZpHHfSX5WrUqC3PYyjW/view?usp=drive_link).

5. **Open and run the notebook**
   ```bash
   jupyter notebook notebooks/Analysis_Report.ipynb
   ```

---

## Limitations & Next Steps

- **No time dimension** — a timestamp column would enable seasonality, day-of-week demand patterns and cohort retention analysis, all critical for Q-Commerce operational planning.
- **Rating imputation suppresses signal** — future analyses should source ratings from a system where missingness is tracked at collection time (was the app closed? delivery refused?).
- **Equal-weight efficiency score** — a parameterised variant weighted by business-specific KPIs would produce a more actionable platform ranking.
- **Potential next project:** Build a delivery time prediction model (regression) using `Distance_Km`, `Company`, `City`, and `Items_Count` as features.

---

## Tools & Libraries

| Category                  | Library                 | Purpose                                    |
|---------------------------|-------------------------|--------------------------------------------|
| Data manipulation         | `pandas`, `numpy`       | Cleaning, aggregation, feature engineering |
| Visualisation             | `matplotlib`, `seaborn` | Static charts and heatmaps                 |
| Interactive visualisation | `plotly`                | Operational efficiency bubble chart        |
| Statistical testing       | `scipy`                 | Mann-Whitney U, Pearson correlation        |
| Preprocessing             | `scikit-learn`          | Min-Max scaling for efficiency score       |
| Path management           | `pathlib`               | Cross-platform file path resolution        |

---

## 📄 License

This project is open source under the [MIT License](LICENSE). Use it, fork it, learn from it, share it.

---

## Author

**Jeshurun Nana Kojo Ansah**
- GitHub: [Jeshurun Nana Kojo Ansah](https://github.com/IntentionedReflex35)
- LinkedIn: [linkedin.com/in/jeshurun-nana-kojo-ansah](https://www.linkedin.com/in/jeshurun-nana-kojo-ansah-08bbb9408)

---

*Dataset: 1,000,000 synthetic Q-Commerce orders | Clean dataset: ~940K orders | Bulk segment: ~24.5K orders analysed separately*
