# cheatsheet to generate graphs from data

import pandas as pd
import matplotlib.pyplot as plt

# read data from csv file
df = pd.read_csv('data.csv')

# generate a line graph
df.plot(x='Date', y='Close', kind='line')
plt.show()

# generate a bar graph
df.plot(x='Date', y='Close', kind='bar')
plt.show()

# generate a scatter graph
df.plot(x='Date', y='Close', kind='scatter')
plt.show()

# generate a histogram
df.plot(x='Date', y='Close', kind='hist')
plt.show()

# generate a box plot
df.plot(x='Date', y='Close', kind='box')
plt.show()

# generate a pie chart
df.plot(x='Date', y='Close', kind='pie')
plt.show()

# generate a area graph
df.plot(x='Date', y='Close', kind='area')
plt.show()

# generate a hexbin graph
df.plot(x='Date', y='Close', kind='hexbin')
plt.show()

# generate a kde graph
df.plot(x='Date', y='Close', kind='kde')
plt.show()

# generate a density graph
df.plot(x='Date', y='Close', kind='density')
plt.show()
