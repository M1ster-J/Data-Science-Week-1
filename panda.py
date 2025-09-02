"""
Author: Mister J
Date: 2025-08-27
Project: Pandas DataFrame Examples
Description:
    Demonstrates creating and manipulating Pandas DataFrames and Series:
    - Creating DataFrames from dictionaries
    - Using custom indices
    - Iterating over DataFrame indices
    - Creating Series
    - Reading CSV files
    - Inspecting DataFrames
"""

import pandas as pd

# Example 1: DataFrame from dictionary
df_example = pd.DataFrame({'Yes': ['HI', 21], 'No': [131, 2]})
print("DataFrame example:\n", df_example)

# Example 2: DataFrame with custom index
users = pd.DataFrame({'Names': ['Alice', 'Bob', 'Charles'], 'Age': [24, 27, 22]}, index=['1', '2', '3'])
print("\nIterating over custom index:")
for i in users.index: 
    print(i)

# Example 3: DataFrame with string values
feedback = pd.DataFrame({
    'Bob': ['I liked it', 'It was okay'],
    'Sue': ['It was pretty good', 'It was bland']
})
print("\nFeedback DataFrame:\n", feedback)

# Example 4: Creating Series
s = pd.Series([1, 2, 3, 4, 5])
print("\nSeries s:\n", s)

t = pd.Series([30, 35, 40], index=['2015 sales', '2016 sales', '2017 sales'])
print("\nSeries t with custom index:\n", t)

# Example 5: Reading CSV file
wine_reviews = pd.read_csv('./wine_reviews.csv')
print("\nShape of wine_reviews DataFrame:", wine_reviews.shape)

# Viewing first five rows
print("\nFirst five rows of wine_reviews:")
print(wine_reviews.head())
