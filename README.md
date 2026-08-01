Airbnb NYC Market Analysis

Python Pandas NumPy Matplotlib Seaborn SciPy GeoPandas

📊 Full Presentation · 📄 Reports · 📓 Notebooks · 👤 Recruiter Summary

Contents

Project summary
Business problem
Business questions
Dataset
Workflow
Visualizations
Key findings
Statistical analysis
Business recommendations
Repository structure
How to run the project
Skills demonstrated
Future improvements
Author
Project summary

This project analyzes 48,895 Airbnb listings across New York City to identify pricing patterns, customer preferences, host concentration, review activity, availability, and location-based trends.

The analysis was reframed from an academic submission into a recruiter-friendly portfolio project focused on business questions, clear methodology, reproducible analysis, and actionable recommendations.

Business problem

Airbnb hosts and marketplace teams need to understand which factors influence listing prices, demand, guest engagement, and availability. This project explores how room type, borough, host activity, reviews, minimum-night requirements, and location relate to listing performance.

Business questions

Which boroughs and room types command the highest prices?
Are price differences statistically significant?
Which areas and room types attract the most guest engagement?
Which hosts manage the largest listing portfolios?
Where are listings geographically concentrated?
How do minimum nights, availability, reviews, and price relate to one another?
Dataset

Dataset: Airbnb NYC Open Data, 2019
Records: 48,895 listings
Geographic scope: Manhattan, Brooklyn, Queens, Bronx, and Staten Island

Place the source file in:

data/raw/AB_NYC_2019.csv
 
The raw dataset is not bundled in this repository because it was not included with the supplied project files.

Workflow

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
 
Visualizations

Average price by borough & room type Average price by borough and room type

Price distribution (outliers excluded) Price distribution

Geographic distribution of listings Geographic distribution of listings

Correlation matrix of key variables Correlation heatmap

Key findings

The mean listing price was approximately $152.72, while the median was $106, indicating a right-skewed price distribution.
Manhattan had significantly higher average prices than Brooklyn.
Average prices differed significantly across room types.
Entire homes/apartments were the most expensive and among the most frequently listed room types.
Brooklyn and Manhattan recorded the highest review activity.
Shared rooms represented the least preferred accommodation category.
Staten Island showed the highest average yearly availability.
Listings were concentrated most heavily in Manhattan and Brooklyn.
Statistical analysis

One-way ANOVA

A one-way ANOVA was used to test whether mean prices differed across:

Entire home/apartment
Private room
Shared room
The reported result showed a statistically significant difference among room types.

Independent-samples t-test

An independent t-test compared listing prices in Brooklyn and Manhattan. The reported result indicated that Manhattan listings were significantly more expensive on average.

Business recommendations

Use borough- and room-type-specific pricing benchmarks rather than a single city-wide pricing rule.
Prioritize premium positioning for entire-home listings in high-demand Manhattan and Brooklyn neighborhoods.
Improve visibility and promotional support for value-oriented listings in lower-priced boroughs.
Use availability and review activity together when evaluating listing performance.
Encourage hosts to improve listing quality and guest experience rather than relying only on lower prices.
Repository structure

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
 
How to run the project

Clone or download the repository.
Place AB_NYC_2019.csv inside data/raw/.
Create a virtual environment.
Install the dependencies:
pip install -r requirements.txt
 
Run the notebooks in numerical order.
Skills demonstrated

Data cleaning and preprocessing
Exploratory data analysis
Descriptive statistics
Data visualization
Hypothesis testing
Correlation analysis
Geospatial analysis
Business insight generation
Analytical storytelling
Reproducible Python workflows
Future improvements

Build an interactive Power BI or Tableau dashboard
Develop a listing-price prediction model
Create a Streamlit application
Add neighborhood-level profitability analysis
Introduce automated data validation tests
Deploy an interactive geospatial dashboard
Author

Lolita Miranda
Data Analyst | Python | SQL | Power BI | Tableau

GitHub: https://github.com/LolitaMiranda

