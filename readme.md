# Adult Census Income Data Analysis Pipeline

This project performs exploratory data analysis, data cleaning, and statistical aggregation on the classic **Adult Census Income dataset** (`adult.data.csv`) using **Python**, **Pandas**, and **NumPy**. It extracts key socio-economic demographic insights, calculates age distributions, evaluates income brackets ($>50K vs. $\le50K$), and analyzes working hours across various demographic groups.

## Project Features & Analysis Steps

1. **Data Ingestion & Preprocessing**:
   * Loads the dataset using `pandas`.
   * Cleans whitespace-padded missing values represented by `?` and drops rows with missing critical attributes (`workclass`, `occupation`, `native-country`).

2. **Demographic & Statistical Metrics**:
   * **Gender Distribution**: Counts the total representation of each gender in the dataset.
   * **Average Age of Women**: Computes the mean age of female respondents and breaks it down into exact years and months.
   * **Country Representation**: Calculates the percentage representation of individuals originating from Germany.

3. **Income & Education Analysis**:
   * **Age Statistics by Salary**: Aggregates mean and standard deviation of ages grouped by salary brackets.
   * **Higher Education Check**: Evaluates whether all individuals earning $>50K hold higher education degrees (such as Bachelors, Masters, Doctorate, etc.).

4. **Intersectional Demographics (Race & Gender)**:
   * Analyzes comprehensive descriptive age statistics grouped by race and sex.
   * Extracts specific metrics, such as the maximum age recorded for the `Amer-Indian-Eskimo` demographic.

5. **Marriage & Income Correlation**:
   * Evaluates the percentage of high-income earners ($>50K) among married versus unmarried males to determine which group holds a greater share of high earners.

6. **Work Intensity & Global Analysis**:
   * **Max Work Hours**: Determines the maximum weekly working hours recorded, the count of individuals working that exact maximum, and the percentage of high-income earners among them.
   * **Global Working Hours**: Computes average weekly working hours grouped by native country and salary tier.

## Requirements

Ensure you have Python 3.x installed along with the required dependencies:

```bash
pip install pandas numpy
```

## Dataset

This script expects the **`adult.data.csv`** dataset file to be located in the same working directory as the script. You can acquire it from standard repositories like the UCI Machine Learning Repository (Adult Dataset).

## Usage

Place the script and the dataset in your project folder, then run it via your terminal:

```bash
python script.py
```

The script will sequentially execute the data processing pipeline and output the calculated demographic and statistical insights to the console.