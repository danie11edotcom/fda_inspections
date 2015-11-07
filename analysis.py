#Import libraries
import pandas as pd
import numpy as np

#Create dataframe from inspection data csv
path = 'fda_inspections.xlsx'
columns = ['district', 'name', 'city', 'state', 'zip', 'country', 'date', 'center', 'area', 'rating']
#http://stackoverflow.com/questions/31515626/pandas-reading-csv-files
inspections = pd.read_excel(path, sheetname='Final')

#Summarize findings by type and year


#Plot summary