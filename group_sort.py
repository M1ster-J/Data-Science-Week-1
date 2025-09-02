"""
Author: Mister J
Date: 2025-08-27
Project: Grouping and Sorting with Pandas
Description:
    Demonstrates how to use Pandas for:
    - Grouping data with groupby()
    - Aggregating values with .agg()
    - Applying custom functions with apply()
    - Sorting grouped data
    - Resetting MultiIndex
"""

import pandas as pd
import numpy as np

# Load dataset
reviews = pd.read_csv('./wine_reviews.csv')

# Count number of reviews for each points value
print(reviews.groupby('points').points.count())

# Minimum price per points group
print(reviews.groupby('points').price.min())

# Apply a custom function to get the first title per winery
print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))

# Group by multiple columns and get the row with max points
print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))

# Use .agg() to run multiple aggregation functions at once
print(reviews.groupby('country').price.agg([len, min, max]))

# Multi-index example
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)

# Show the type of the index
mi = countries_reviewed.index
print(type(mi))

# Convert MultiIndex back to regular index
countries_reviewed = countries_reviewed.reset_index()
print(countries_reviewed)

# Sort by aggregation length ascending
print(countries_reviewed.sort_values(by='len'))

# Sort by aggregation length descending
print(countries_reviewed.sort_values(by='len', ascending=False))

# Sort by index values (alphabetical)
print(countries_reviewed.sort_index())

# Sort by multiple columns
print(countries_reviewed.sort_values(by=['country', 'len']))
