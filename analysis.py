#Import libraries
import pandas as pd
import numpy as np
import datetime as dt

#Create dataframe from inspection data csv
path = 'fda_inspections.xlsx'
inspections = pd.read_excel(path, sheetname='Final')

#Rename columns
inspections.columns = ['district', 'name', 'city', 'state', 'zip', 'country', 'date', 'center', 'area', 'rating']

#Add column to show year using inspection end date
inspections['year'] = inspections['date'].dt.year 

#Summarize ratings by year and center
p = pd.pivot_table(inspections, index=['year','center'], columns='rating' values=['name'],aggfunc=lambda x: len(x))
#http://stackoverflow.com/questions/12860421/python-pandas-pivot-table-with-aggfunc-count-unique-distinct

#Summarize ratings by year, center and project area
p2 = pd.pivot_table(inspections, index=['year','center','area'], columns='rating', values=['name'],aggfunc=lambda x: len(x))

#Plot summary