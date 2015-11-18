#Import libraries
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib as mp

#Create dataframe from inspection data csv
path = 'fda_inspections.xlsx'
inspections = pd.read_excel(path, sheetname='Final')

#Rename columns
inspections.columns = ['district', 'name', 'city', 'state', 'zip', 'country', 'date', 'center', 'area', 'rating']

#Add column to show year using inspection end date
inspections['year'] = inspections['date'].dt.year 

#Add column named one to add a one to each record to use sum function to count
inspections['one'] = 1

#Count total inspections by year
total_inspections = pd.pivot_table(inspections, index='year', values='one', aggfunc=sum)

#Summarize ratings by year and center
total_insp_center = pd.pivot_table(inspections, index=['year','center'], columns='rating', values='one', aggfunc=sum)
#http://stackoverflow.com/questions/12860421/python-pandas-pivot-table-with-aggfunc-count-unique-distinct

#Summarize ratings by year, center and project area
total_insp_area = pd.pivot_table(inspections, index=['year','center','area'], columns='rating', values='one', aggfunc=sum)

#Summarize ratings by year, center, project area and district
total_insp_district = pd.pivot_table(inspections, index=['year','center','area', 'district'], columns='rating', values='one', aggfunc=sum)

#Plot summary