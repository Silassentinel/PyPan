# comment to init the directory
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the data
df = pd.read_csv('data.csv')
# print(df)

# print the first 5 rows
print(df.head())

# print the last 5 rows
print(df.tail())

# print the first 10 rows
print(df.head(10))

# print the last 10 rows
print(df.tail(10))

# print the shape of the data
print(df.shape)

# print the columns of the data
print(df.columns)

# print the index of the data
print(df.index)

# print the data types of the data
print(df.dtypes)

# print the data types of the data
print(df.info())
