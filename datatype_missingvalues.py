"""
Author: Mister J
Date: 2025-08-27
Project: Data Cleaning with Pandas
Description:
    Demonstrates how to:
    - Inspect and understand datatypes in a dataset
    - Convert columns between datatypes
    - Identify and handle missing values
    - Replace values in a DataFrame
"""

import pandas as pd
import numpy as np

# Load the dataset
reviews = pd.read_csv('./wine_reviews.csv', index_col=0)

# Display settings for pandas
pd.set_option('display.max_rows', 5)

# Inspect datatypes of a single column and the whole DataFrame
print("Datatype of 'price':", reviews.price.dtypes)
print("Datatypes for all columns:\n", reviews.dtypes)

# Convert 'price' column from int to float
print("\nPrice column converted to float:\n", reviews.price.astype('float64'))

# Inspect datatype of the index
print("\nIndex datatype:", reviews.index.dtype)

# Identify missing values in 'country'
print("\nRows with missing country values:\n", reviews[pd.isnull(reviews.country)])

# Replace missing country values with 'Unknown'
print("\nCountry column with missing values replaced:\n", reviews.country.fillna("Unknown"))

# Replace a specific value in 'taster_twitter_handle'
print("\nUpdated taster Twitter handles:\n",
      reviews.taster_twitter_handle.replace('@kerinokeefe', '@kerinrro'))
