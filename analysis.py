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

#Function to add sum and percentage for year
def add_percent(table):
		table['SUM'] = (table['NAI']) + (table['VAI']) + (table['OAI'])
		table['NAIp'] = (table['NAI']) / (table['SUM']) * 100
		table['VAIp'] = (table['VAI']) / (table['SUM']) * 100
		table['OAIp'] = (table['OAI']) / (table['SUM']) * 100

###Summary Functions###
# def create_center_df(full_df, center):
# 	center_lower = center.lower()
# 	center_lower = full_df[full_df.center == center]


###CBER Summary###
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

###CDER Summary###
cder = full_years[full_years.center == 'CDER']
cder_year = pd.pivot_table(cder, index='year', columns='rating', values='one', aggfunc=sum)
cder_year = cber_year[cols]
add_percent(cder_year)
cder_area = pd.pivot_table(cder, index=['year','area'], columns='rating', values='one', aggfunc=sum)
cder_area = cder_area[cols]
add_percent(cder_area)
cder_district = pd.pivot_table(cder, index=['year','area', 'district'], columns='rating', values='one', aggfunc=sum)
cder_district = cder_district.convert_objects(convert_numeric=True).fillna(0)
cder_district = cder_district[cols]
add_percent(cder_district)

###CDRH Summary###
cdrh = full_years[full_years.center == 'CDRH']
cdrh_year = pd.pivot_table(cdrh, index='year', columns='rating', values='one', aggfunc=sum)
cdrh_year = cber_year[cols]
add_percent(cdrh_year)
cdrh_area = pd.pivot_table(cdrh, index=['year','area'], columns='rating', values='one', aggfunc=sum)
cdrh_area = cder_area[cols]
add_percent(cdrh_area)
cdrh_district = pd.pivot_table(cdrh, index=['year','area', 'district'], columns='rating', values='one', aggfunc=sum)
cdrh_district = cdrh_district.convert_objects(convert_numeric=True).fillna(0)
cdrh_district = cdrh_district[cols]
add_percent(cdrh_district)

###CVM Summary###
cvm = full_years[full_years.center == 'CVM']
cvm_year = pd.pivot_table(cvm, index='year', columns='rating', values='one', aggfunc=sum)
cvm_year = cvm_year[cols]
add_percent(cvm_year)
cvm_area = pd.pivot_table(cvm, index=['year','area'], columns='rating', values='one', aggfunc=sum)
cvm_area = cvm_area[cols]
add_percent(cvm_area)
cvm_district = pd.pivot_table(cvm, index=['year','area', 'district'], columns='rating', values='one', aggfunc=sum)
cvm_district = cvm_district.convert_objects(convert_numeric=True).fillna(0)
cvm_district = cvm_district[cols]
add_percent(cvm_district)

###CFSAN Summary###
cfsan = full_years[full_years.center == 'CFSAN']
cfsan_year = pd.pivot_table(cfsan, index='year', columns='rating', values='one', aggfunc=sum)
cfsan_year = cfsan_year[cols]
add_percent(cfsan_year)
cfsan_area = pd.pivot_table(cfsan, index=['year','area'], columns='rating', values='one', aggfunc=sum)
cfsan_area = cfsan_area[cols]
add_percent(cfsan_area)
cfsan_district = pd.pivot_table(cfsan, index=['year','area', 'district'], columns='rating', values='one', aggfunc=sum)
cfsan_district = cdrh_district.convert_objects(convert_numeric=True).fillna(0)
cfsan_district = cdrh_district[cols]
add_percent(cfsan_district)


#Create excel file with each center summary (not csv so that I can add multiple sheets to one workbook with excel writer)
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
cber.to_excel(writer, 'cber')
cber_year.to_excel(writer,'cber_year')
cber_area.to_excel(writer, 'cber_area')
cber_district.to_excel(writer, 'cber_district')
cder.to_excel(writer, 'cder')
cder_year.to_excel(writer,'cder_year')
cder_area.to_excel(writer, 'cder_area')
cder_district.to_excel(writer, 'cder_district')
cdrh.to_excel(writer, 'cdrh')
cdrh_year.to_excel(writer,'cdrh_year')
cdrh_area.to_excel(writer, 'cdrh_area')
cdrh_district.to_excel(writer, 'cdrh_district')
cvm.to_excel(writer, 'cvm')
cvm_year.to_excel(writer,'cvm_year')
cvm_area.to_excel(writer, 'cvm_area')
cvm_district.to_excel(writer, 'cvm_district')
cfsan.to_excel(writer, 'cfsan')
cfsan_year.to_excel(writer,'cfsan_year')
cfsan_area.to_excel(writer, 'cfsan_area')
cfsan_district.to_excel(writer, 'cfsan_district')
writer.save()

#TODO: write function(s) to repeat same summary for each of the 5 FDA centers without retyping the same code

#TODO: Research warning below for add_percent function def
# C:\Users\Network Admin 02\Desktop\fda_inspections\analysis.py:34: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead

# See the the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy