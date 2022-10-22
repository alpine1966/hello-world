"""
Correlation Machine
an attempt at making  a system for cross correlations in arbitrarily 
sampled time series

hmm.. if I am looking at drug deaths, I saw that unemployment is correlated
so that might be a thing to consider.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

#make sure in the data directory first please
os.chdir('C:\\Users\\Dave\\Dropbox\\Programming')

drug = pd.read_csv\
    ('NCHS_-_Drug_Poisoning_Mortality_by_State__United_States.csv',\
     index_col='Year')
weather =pd.read_csv('bigpghweather2.csv')
#Dow Jones industrialcd
dji = pd.read_csv('DJI.csv',index_col = 'Date')

#work unemployment data is 2d year/month table. should convert to a series
# https://data.bls.gov/pdq/SurveyOutputServlet
work=pd.read_excel('unemployment_data.xlsx',index_col =0)

work = pd.DataFrame.stack(work)

print (work.head())

#tmp = pd.to_datetime(dji['Date'])
#tmp2 = pd.to_datetime(drug['Year'], exact = 'False')
#tmp3 = pd.to_datetime(weather['DATE'])
#tmp3 = pd.to_datetime(work['Year'], exact = 'false')