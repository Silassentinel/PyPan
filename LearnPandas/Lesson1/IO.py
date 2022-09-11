#cheat sheet for input and output/ working with files and filesystems
#region imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import glob
import shutil
import zipfile
import tarfile
import gzip
import bz2
import lzma
import csv
import sqlite3
import pickle
import json
#endregion

#csv files
#region csv files
#read csv file
df = pd.read_csv('data.csv')
print(df)


#json
#region json
#read json file
df = pd.read_json('data.json')
print(df)

#excel
#region excel
#read excel file
df = pd.read_excel('data.xlsx')
print(df)

#html
#region html
#read html file
df = pd.read_html('data.html')
print(df)

#sql
#region sql
#read sql file
df = pd.read_sql('data.sql')
print(df)

#pickle
#region pickle
#read pickle file
df = pd.read_pickle('data.pickle')
print(df)

#to_csv
#region to_csv
#write to csv file
df.to_csv('data.csv')

#to_excel
#region to_excel
#write to excel file
df.to_excel('data.xlsx')

#to_html
#region to_html
#write to html file
df.to_html('data.html')

#to_json
#region to_json
#write to json file
df.to_json('data.json')

#to_sql
#region to_sql
#write to sql file
df.to_sql('data.sql')

#to_pickle
#region to_pickle
#write to pickle file
df.to_pickle('data.pickle')

#serialize class objects
#region serialize class objects
#writing to a file
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person({self.name}, {self.age})'

p = Person('John', 30)
df.to_csv(p)