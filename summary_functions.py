"""
Author: Mister J
Date: 2025-08-26
Project: Summary Functions and Mapping in Python
Description:
    Demonstrates summary statistics and mapping in Pandas:
    - Using describe(), mean(), unique(), and value_counts()
    - Mapping functions across DataFrame columns
"""

import pandas as pd
import numpy as np

# Set display options
pd.set_option('display.max_rows', 5)

# Load dataset
reviews = pd.read_csv("./wine_reviews.csv", index_col=0)

# Summary statistics
print("Points summary:")
print(reviews.points.describe())

print("\nTaster name summary:")
print(reviews.taster_name.describe())

# Mean of points
mean_points = reviews.points.mean()
print("\nMean points:", mean_points)

# Unique taster names
print("\nUnique taster names:", reviews.taster_name.unique())

# Frequency of taster names
print("\nTaster name counts:")
print(reviews.taster_name.value_counts())

# Mapping: subtract the mean from each points value
print("\nPoints mapped to mean difference:")
print(reviews.points.map(lambda p: p - mean_points))

# Applying function across rows
def remean_points(row):
    row.points = row.points - mean_points
    return row

adjusted_reviews = reviews.apply(remean_points, axis='columns')
print("\nAdjusted points (first 5 rows):")
print(adjusted_reviews.head())
