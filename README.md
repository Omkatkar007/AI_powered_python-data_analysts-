# Advanced Python for Data Analysis 📊🐍

## 🎯 Overview
This repository contains scripts, notes, and projects tracking my progress through the **Advanced Python for Data Analysis** curriculum. It transitions from core Python programming concepts directly into the industry-standard data stack, focusing on data manipulation, cleaning, and visualization.

## 🛠️ Technology Stack
- **Language:** Python 3.x
- **Data Manipulation:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **File Parsing:** openpyxl (Excel), csv

## 📚 Repository Contents

### 1. Advanced Python Mechanics
- **Iterables & Loops:** How Python iterates over data structures.
- **List Comprehensions:** Writing optimized, single-line data transformations.
- **Generators:** Managing memory efficiency when working with massive datasets.
- **Mutability & Copies:** Understanding references vs. explicit copies (Deep/Shallow) to prevent silent data corruption bugs.

### 2. Numerical Data Processing (NumPy)
- Transitioning from slow `for` loops to high-speed array **Vectorization**.

### 3. Data Wrangling (Pandas)
- **Core Structures:** Series (1D) and DataFrames (2D).
- **Data Auditing:** Utilizing `df.info()` and `df.describe()` for initial dataset exploration.
- **Data Cleaning:** Handling missing data (`NaN`), resolving incorrect data types, and using string vectorization (`.str`).
- **File I/O:** Reading, filtering, and writing to CSV and multi-sheet Excel files.

### 4. Data Visualization
- **Matplotlib:** Building foundational business charts.
  - *Line Charts:* Tracking continuous time series.
  - *Scatter Plots:* Identifying correlations and outliers.
  - *Bar Charts:* Categorical comparisons.
  - *Histograms & Boxplots:* Analyzing data distribution and extreme anomalies.
- **Seaborn:** Leveraging built-in datasets (e.g., `tips`, `titanic`) and generating aesthetically optimized statistical plots with minimal code.

### 5. Capstone Project
- **Gurgaon Real Estate Market Analysis:** An end-to-end data pipeline project involving raw data extraction, rigorous cleaning of inconsistent text formatting, outlier detection, and generating actionable visual insights for stakeholders.

## 🚀 Getting Started

Clone the repository and install the required dependencies to run the scripts locally:

```bash
# Clone the repository
git clone <your-repo-url>

# Install the required data analytics packages
pip install pandas numpy matplotlib seaborn openpyxl
```

## 📈 The Analyst's Mindset
- **The 80/20 Rule:** 80% of analytics is investigating business logic and cleaning data; 20% is the actual code execution.
- **Automation over Manual Entry:** Replacing manual spreadsheet tasks with robust, reproducible ETL (Extract, Transform, Load) pipelines.
