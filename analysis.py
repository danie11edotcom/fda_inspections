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
inspections['year'] = pd.to_datetime(inspections['year'], format='%Y')

#Add column named one to add a one to each record to use sum function to count
inspections['one'] = 1

#Remove partial years (2008 and 2015)
less_2008 = inspections[inspections.year != '2008']
full_years = less_2008[less_2008.year != '2015']

#Count total inspections by year
total_insp = pd.pivot_table(full_years, index='year', values='one', aggfunc=sum)

#Count total ratings by year
total_insp_rating = pd.pivot_table(full_years, index='year', columns='rating', values='one', aggfunc=sum)

#Summarize ratings by year and center
total_insp_center = pd.pivot_table(full_years, index=['year','center'], columns='rating', values='one', aggfunc=sum)

#Summarize ratings by year, center and project area
total_insp_area = pd.pivot_table(full_years, index=['year','center','area'], columns='rating', values='one', aggfunc=sum)

#Summarize ratings by year, center, project area and district
total_insp_district = pd.pivot_table(full_years, index=['year','center','area', 'district'], columns='rating', values='one', aggfunc=sum)

#Plot summary of individual center ratings by year
centers = ['CBER','CDER', 'CDRH', 'CVM','CFSAN']
# for each item in list subsitite center_name with list
# 		total_insp_center.query('center == ["CVM"]').plot()

#CBER summary
#create dataframe for cber inspections 
cber = full_years[full_years.center == 'CBER']
#summarize ratings by year
cber_year = pd.pivot_table(cber, index='year', columns='rating', values='one', aggfunc=sum)

#plot and save image
#cber_year.plot()
#cber_year.to_json(date_format='iso', date_unit='s')

#summarize ratings by year and project area
cber_area = pd.pivot_table(cber, index=['year','area'], columns='rating', values='one', aggfunc=sum)
#summarize ratings by year, project area and district
cber_district = pd.pivot_table(cber, index=['year','area', 'district'], columns='rating', values='one', aggfunc=sum)

#Write functions and loop to summarize each center

#def center_df(center):
		#center = inspections[inspections.center == "'" + center + "'"]

#def center_pivot(center)
		#center_pivot = pd.pivot_table(center, index='year', columns='rating', values='one', aggfunc=sum)