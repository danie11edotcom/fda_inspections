import pandas as pd
import numpy as np
import datetime as dt
import matplotlib as mp

#Create dataframe from inspection data xlsx file from FDA site
path = 'fda_inspections.xlsx'
inspections = pd.read_excel(path, sheetname='Final')

#Rename columns
columns = ['district', 'name', 'city', 'state', 'zip', 'country', 'date', 'center', 'area', 'rating']
inspections.columns = columns

#Add column to show year using inspection end date
inspections['year'] = inspections['date'].dt.year 
inspections['year'] = pd.to_datetime(inspections['year'], format='%Y')

#Add column named one to add a one to each record to use sum function to count
inspections['one'] = 1

#Remove partial years (2008 and 2015)
less_2008 = inspections[inspections.year != '2008']
full_years = less_2008[less_2008.year != '2015']

#Summarize by center
centers = ['CBER','CDER', 'CDRH', 'CVM','CFSAN']
cols = ['NAI', 'VAI', 'OAI' ]

#Add function to add sum and percentage for year
def add_percent(table):
		table['sum'] = (table['NAI']) + (table['VAI']) + (table['OAI'])
		table['NAIp'] = (table['NAI']) / (table['sum']) * 100
		table['VAIp'] = (table['VAI']) / (table['sum']) * 100
		table['OAIp'] = (table['OAI']) / (table['sum']) * 100

#CBER summary
#Create dataframe for cber inspections 
cber = full_years[full_years.center == 'CBER']

#Summarize ratings by year
cber_year = pd.pivot_table(cber, index='year', columns='rating', values='one', aggfunc=sum)
cber_year = cber_year[cols]
add_percent(cber_year)

#Summarize ratings by year and project area
cber_area = pd.pivot_table(cber, index=['year','area'], columns='rating', values='one', aggfunc=sum)
cber_area = cber_area[cols]
add_percent(cber_area)

#Summarize ratings by year, project area and district
cber_district = pd.pivot_table(cber, index=['year','area', 'district'], columns='rating', values='one', aggfunc=sum)
#fill blanks with 0
cber_district = cber_district.convert_objects(convert_numeric=True).fillna(0)
cber_district = cber_district[cols]
add_percent(cber_district)

#Create excel file with each center summary (not csv so that I can add multiple sheets to one workbook with excel writer)
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
cber.to_excel(writer, 'cber')
cber_year.to_excel(writer,'cber_year')
cber_area.to_excel(writer, 'cber_area')
cber_district.to_excel(writer, 'cber_district')
writer.save()

#TODO: write function(s) to repeat same summary for each of the 5 FDA centers without retyping the same code