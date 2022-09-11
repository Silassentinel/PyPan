# cheatsheet to convert data

import pandas as pd

# convert a csv file to a json file
df = pd.read_csv('data.csv')
df.to_json('data.json')

# convert a csv file to a html file
df = pd.read_csv('data.csv')
df.to_html('data.html')

# convert a csv file to a excel file
df = pd.read_csv('data.csv')
df.to_excel('data.xlsx')

# convert a csv file to a sql file
df = pd.read_csv('data.csv')
df.to_sql('data', con)

# convert a csv file to a clipboard
df = pd.read_csv('data.csv')
df.to_clipboard()

# convert a csv file to a hdf5 file
df = pd.read_csv('data.csv')
df.to_hdf('data.h5', key='df', mode='w')

# convert a csv file to a feather file
df = pd.read_csv('data.csv')
df.to_feather('data.feather')

# convert a csv file to a parquet file
df = pd.read_csv('data.csv')
df.to_parquet('data.parquet')

# convert a csv file to a msgpack file
df = pd.read_csv('data.csv')
df.to_msgpack('data.msgpack')

# convert a csv file to a stata file
df = pd.read_csv('data.csv')
df.to_stata('data.dta')

# convert a csv file to a sas file
df = pd.read_csv('data.csv')
df.to_sas('data.sas7bdat')

# convert a csv file to a pickle file
df = pd.read_csv('data.csv')
df.to_pickle('data.pkl')

# convert a csv file to a python file
df = pd.read_csv('data.csv')
df.to_pickle('data.py')

# string to datetime
df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# csv to DataTransferObject
df = pd.read_csv('data.csv')
df.to_dict('records')

# array to list
df = pd.read_csv('data.csv')
df.values.tolist()

# int to datetime
df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'], unit='s')


# int to string
df = pd.read_csv('data.csv')
df['Date'] = df['Date'].astype(str)

# int to float
df = pd.read_csv('data.csv')
df['Date'] = df['Date'].astype(float)

# int to bool
df = pd.read_csv('data.csv')
df['Date'] = df['Date'].astype(bool)

# int to complex
df = pd.read_csv('data.csv')
df['Date'] = df['Date'].astype(complex)