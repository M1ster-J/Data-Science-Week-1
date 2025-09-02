# Mister J
# 08/29/2025
# Verses Python

import numpy as np
import pandas as pd

pd.set_option('display.max_rows', 5)
bible = pd.read_csv('asv.csv')

print(bible.points.describe())