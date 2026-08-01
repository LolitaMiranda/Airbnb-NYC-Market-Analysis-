# Airbnb NYC Market Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualization-4C72B0)
![SciPy](https://img.shields.io/badge/SciPy-Statistical%20Testing-8CAAE6)
![GeoPandas](https://img.shields.io/badge/GeoPandas-Geospatial%20Analysis-green)

**[📊 Full Presentation](presentation/Airbnb_NYC_Final_Presentation.pptx)** · **[📄 Reports](reports/)** · **[📓 Notebooks](notebooks/)** · **[👤 Recruiter Summary](docs/RECRUITER_PROJECT_SUMMARY.md)**

> **Headline result:** Analyzed **48,895 NYC Airbnb listings** and found Manhattan listings are priced significantly higher than Brooklyn's (confirmed via t-test), with entire-home listings commanding the largest premium across all five boroughs. Findings were translated into borough- and room-type-specific pricing recommendations.

![Average price by borough and room type](images/price_by_borough_roomtype.png)

## Contents

- [Project summary](#project-summary)
- [Business problem](#business-problem)
- [Business questions](#business-questions)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Visualizations](#visualizations)
- [Key findings](#key-findings)
- [Statistical analysis](#statistical-analysis)
- [Business recommendations](#business-recommendations)
- [Repository structure](#repository-structure)
- [How to run the project](#how-to-run-the-project)
- [Skills demonstrated](#skills-demonstrated)
- [Future improvements](#future-improvements)
- [Author](#author)

## Project summary

This project analyzes **48,895 Airbnb listings across New York City** to identify pricing patterns, customer preferences, host concentration, review activity, availability, and location-based trends.

The workflow follows a business-first structure: clear questions, reproducible analysis, statistical validation, and actionable recommendations — not just exploratory charts.

## Business problem

Airbnb hosts and marketplace teams need to understand which factors influence listing prices, demand, guest engagement, and availability. This project explores how room type, borough, host activity, reviews, minimum-night requirements, and location relate to listing performance.

## Business questions

- Which boroughs and room types command the highest prices?
- Are price differences statistically significant?
- Which areas and room types attract the most guest engagement?
- Which hosts manage the largest listing portfolios?
- Where are listings geographically concentrated?
- How do minimum nights, availability, reviews, and price relate to one another?

## Dataset

**Dataset:** Airbnb NYC Open Data, 2019  
**Records:** 48,895 listings  
**Geographic scope:** Manhattan, Brooklyn, Queens, Bronx, and Staten Island

Place the source file in:

```text
data/raw/AB_NYC_2019.csv
```

The raw dataset is not bundled in this repository because it was not included with the supplied project files.

## Workflow

<details>
<summary>View the analysis pipeline</summary>

```text
Raw data
   ↓
Data quality checks
   ↓
Cleaning and preprocessing
   ↓
Exploratory analysis
   ↓
Statistical testing
   ↓
Geospatial and correlation analysis
   ↓
Business insights and recommendations
```

</details>

## Visualizations

<table>
<tr>
<td width="50%">

**Average price by borough & room type**
![Average price by borough and room type](images/price_by_borough_roomtype.png)

</td>
<td width="50%">

**Price distribution by room type**
![Price distribution by room type](images/price_distribution.png)

</td>
</tr>
<tr>
<td width="50%">

**Geographic distribution of listings by borough**
![Geographic distribution of listings](images/geographic_distribution.png)

</td>
<td width="50%">

**Correlation matrix of key numerical variables**
![Correlation heatmap](images/correlation_heatmap.png)

</td>
</tr>
<tr>
<td width="50%">

**Total reviews by borough**
![Total reviews by borough](images/reviews_by_borough.png)

</td>
<td width="50%">

**Average availability (days/year) by borough**
![Average availability by borough](images/availability_by_borough.png)

</td>
</tr>
<tr>
<td width="50%">

**Room type mix across all listings**
![Proportion of room types](images/room_type_proportion.png)

</td>
<td width="50%">

**Top 10 hosts by listing count**
![Top hosts by listing count](images/top_hosts.png)

</td>
</tr>
</table>

## Key findings

- The mean listing price was approximately **$152.72**, while the median was **$106**, indicating a right-skewed price distribution.
- Manhattan had significantly higher average prices than Brooklyn.
- Average prices differed significantly across room types.
- Entire homes/apartments were the most expensive and among the most frequently listed room types.
- Brooklyn and Manhattan recorded the highest review activity.
- Shared rooms represented the least preferred accommodation category.
- Staten Island showed the highest average yearly availability.
- Listings were concentrated most heavily in Manhattan and Brooklyn.

## Statistical analysis

### One-way ANOVA

A one-way ANOVA was used to test whether mean prices differed across:

- Entire home/apartment
- Private room
- Shared room

The reported result showed a statistically significant difference among room types.

### Independent-samples t-test

An independent t-test compared listing prices in Brooklyn and Manhattan. The reported result indicated that Manhattan listings were significantly more expensive on average.

## Business recommendations

- Use borough- and room-type-specific pricing benchmarks rather than a single city-wide pricing rule.
- Prioritize premium positioning for entire-home listings in high-demand Manhattan and Brooklyn neighborhoods.
- Improve visibility and promotional support for value-oriented listings in lower-priced boroughs.
- Use availability and review activity together when evaluating listing performance.
- Encourage hosts to improve listing quality and guest experience rather than relying only on lower prices.

## Repository structure

<details>
<summary>View folder layout</summary>

```text
Airbnb-NYC-Market-Analysis/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   └── 03_Statistical_and_Spatial_Analysis.ipynb
├── src/
│   ├── data_cleaning.py
│   ├── visualizations.py
│   └── statistical_analysis.py
├── images/
├── presentation/
├── reports/
└── docs/
```

</details>

## How to run the project

> Note: `data/raw/` is empty in this repo — the source CSV isn't bundled (see [Dataset](#dataset)). Add it before running the notebooks.

1. Clone or download the repository.
2. Place `AB_NYC_2019.csv` inside `data/raw/`.
3. Create a virtual environment.
4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Run the notebooks in numerical order.

## Skills demonstrated

- Data cleaning and preprocessing
- Exploratory data analysis
- Descriptive statistics
- Data visualization
- Hypothesis testing
- Correlation analysis
- Geospatial analysis
- Business insight generation
- Analytical storytelling
- Reproducible Python workflows

## Future improvements

- Build an interactive Power BI or Tableau dashboard
- Develop a listing-price prediction model
- Create a Streamlit application
- Add neighborhood-level profitability analysis
- Introduce automated data validation tests
- Deploy an interactive geospatial dashboard

## Author

**Lolita Miranda**  
Data Analyst | Python | SQL | Power BI | Tableau

GitHub: `https://github.com/LolitaMiranda`
