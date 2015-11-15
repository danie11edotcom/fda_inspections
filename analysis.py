#Import libraries
import pandas as pd
import numpy as np
import datetime as dt

#Create dataframe from inspection data csv
path = 'fda_inspections.xlsx'
inspections = pd.read_excel(path, sheetname='Final')

#Rename columns
inspections.columns = ['district', 'name', 'city', 'state', 'zip', 'country', 'date', 'center', 'area', 'rating']

#Add column to show year using inpsection end date
inspections['year'] = inspections['date'].dt.year 

#Change year dtype to a datetime object


#Summarize findings by type and year (index= year, columns=center, values=rating, aggfunc=func to count o)
p = pd.pivot_table(inspections, index=['year','center'], columns='rating' values=['name'],aggfunc=lambda x: len(x)
#http://stackoverflow.com/questions/12860421/python-pandas-pivot-table-with-aggfunc-count-unique-distinct

#Plot summary