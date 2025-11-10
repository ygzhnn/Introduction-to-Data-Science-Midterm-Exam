# Introduction to Data Science - Midterm Exam Project

This repository contains a Python script (`data_wrangling.py`) that demonstrates a data cleaning and preparation process on a sample student dataset.

## Description

The script performs the following data wrangling steps in order:

1.  **Duplicate Handling**: Identifies and removes any duplicate rows from the dataset.
2.  **Standardization**: Converts the 'Major' column to a consistent lowercase format and removes any leading/trailing whitespace.
3.  **Missing Data Imputation**: Fills missing `NaN` values in the 'Course_Grade' column using the median of the existing non-missing values.
4.  **Casting**: Converts the 'Date_Enrolled' column from a string type to a proper Pandas datetime object.
5.  **Final Check**: Calculates and prints the final mean of the cleaned 'Course_Grade' column.

## How to Run the Script

1.  Ensure you have Python and the `pandas` library installed. If not, you can install pandas using pip:
    ```bash
    pip install pandas numpy
    ```
2.  Navigate to the directory containing the script.
3.  Run the script from your terminal:
    ```bash
    python data_wrangling.py
    ```

The script will print the state of the data at each step of the cleaning process.
