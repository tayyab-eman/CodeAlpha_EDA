# CodeAlpha Data Analytics Internship — Task 2: Exploratory Data Analysis

## Objective

The objective of this task is to explore and analyze a structured population dataset using Exploratory Data Analysis (EDA) techniques.

## Dataset

The dataset contains population information collected from a publicly available population webpage.

The dataset contains the following columns:

- Country
- Population
- World Percentage
- Date
- Source

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn

## EDA Performed

The following analysis was performed:

- Dataset preview
- Dataset shape and structure
- Column names
- Data types
- Missing value analysis
- Descriptive statistics
- Identification of highly populated countries
- Population distribution analysis
- Data visualization

## Visualizations

Two visualizations were created:

1. Top 10 Most Populated Countries
2. Population Distribution

## Output

The analysis results and visualizations are stored in the `outputs` folder.

### Output Files

- `eda_summary.txt`
- `top10_population.png`
- `population_distribution.png`

## Conclusion

The exploratory data analysis helped identify population patterns, compare highly populated countries, examine the distribution of population values, and check the structure and quality of the dataset.

## Project Structure

```text
CodeAlpha_EDA/
│
├── task2_eda.py
├── README.md
├── REPORT.md
├── requirements.txt
│
├── data/
│   └── country_population.csv
│
└── outputs/
    ├── eda_summary.txt
    ├── top10_population.png
    └── population_distribution.png
