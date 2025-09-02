"""
Author: Mister J
Date: 2025-08-27
Project: Pandas Indexing Examples
Description:
    Demonstrates different ways to select data in a Pandas DataFrame using:
    - Label-based selection
    - Index-based selection (.iloc)
    - Slicing and negative indexing
"""

import pandas as pd

# Load dataset
reviews = pd.read_csv('./wine_reviews.csv')

# Access a single value using column label
print("First country:", reviews['country'][0])

# Access the first row
print("First row (as Series):", reviews.iloc[0])

# Index-based selection examples
print("First row using iloc:", reviews.iloc[0])
print("First column using iloc:", reviews.iloc[:, 0])

# Select second and third entries of the first column
print("Second and third entries of first column:", reviews.iloc[1:3, 0])

# Select specific rows by passing a list
print("First three rows of first column:", reviews.iloc[[0, 1, 2], 0])

# Negative indexing: select last five entries of first column
print("Last five rows of first column:", reviews.iloc[-5:, 0])
