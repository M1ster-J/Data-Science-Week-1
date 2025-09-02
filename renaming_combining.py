import pandas as pd
pd.set_option('display.max_rows',5)
reviews = pd.read_csv('./wine_reviews.csv', index_col=0)

# Renaming index or column names
print(reviews.rename(columns={'points': 'score'}))

# rename lets you rename index or columns by specifiying column
# numbers

print(reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'}))

# Rename_axis lets you change either row index or column index
print(reviews.rename_axis('wines', axis='rows').rename_axis('fields', axis='columns'))