#Import libraries
import pandas as pd
import numpy as np

#Create dataframe from inspection data csv
path = 'fda_inspection_data.txt'
columns = ['district', 'name', 'city', 'state', 'zip', 'country', 'date', 'center', 'area', 'rating']
#http://stackoverflow.com/questions/31515626/pandas-reading-csv-files
inspections = pd.read_csv(path, names=columns, encoding='cp1252')
#TODO: troubleshoot utf-8 char error

#Summarize findings by type and year


#Plot summary