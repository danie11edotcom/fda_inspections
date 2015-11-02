#Import libraries
import pandas as pd
import numpy as np

#Create dataframe from inspection data csv
path = 'fda_inspection_data.csv'
columns = ['district', 'name', 'city', 'state', 'zip', 'country', 'date', 'center', 'area', 'rating']
inspections = pd.read_csv(path, names=columns)