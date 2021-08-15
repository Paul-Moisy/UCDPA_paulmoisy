# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 13:00:20 2021

@author: Paul.Moisy
"""

import pandas as pd

df = pd.read_csv("Cell_Utilization_1.csv")

#Checking if data set is loaded.
print(df.head())

#looking at data set to determine if data is in the correct format.
df.info()

#Removing unwanted charicters from Column headings.
def run():
    lis = ['ubk', 'xaw', 'lml', 'jmo', 'lme']
    
    for i in lis:
        df.columns = df.columns.str.replace(i[0:3],'')                       
run()

df.columns = df.columns

df.info()

#df['actionDate'] = pd.to_datetime(df['actionDate'])
#df = df.set_index('actionDate')

#Checking to see if only cell operators are within the dataset.
#If there is aditional operators within the dataset it indicates that they logged on to the incorrect machine.
print(df['EmployeeName'])

Cell_2_operatives = ['Shaun Murphy', 'Leo Cunniffe', 'Murray Pascall', 'Fernando Toni']

#Applying filter to dataset to only show the relevant operatives.
#Dataset was renamed "cell_2" as an analysis of incorrect loggin's is required on "df"
cell_2 = df[(df.EmployeeName == 'Leo Cunniffe') | (df.EmployeeName == 'Shaun Murphy') | 
        (df.EmployeeName == 'Murray Pascall') |  (df.EmployeeName == 'Fernando Toni')]


leo = df[df.EmployeeName == 'Leo Cunniffe']
shaun = df[df.EmployeeName == 'Shaun Murphy']
murray = df[df.EmployeeName == 'Murray Pascall']
fernando = df[df.EmployeeName == 'Fernando Toni']


import matplotlib.pyplot as plt

plt.xlabel('Date')
plt.ylabel('Hrs')
plt.title('Earned Hours Trend Line')
plt.plot(leo.directEarnedHours)
plt.plot(shaun.directEarnedHours)
plt.plot(murray.directEarnedHours)
plt.plot(fernando.directEarnedHours)

#cell_2.to_excel("123.xlsx")   
      


  


    
