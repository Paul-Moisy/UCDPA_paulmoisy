# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 13:00:20 2021

@author: Paul.Moisy
"""
#Importing Pandas.
import pandas as pd

#Importing dataset from excel. 
df = pd.read_csv("Cell_Utilization_1.csv")

#Checking if data set is loaded.
print(df.head())

#looking at data set to determine if data is in the correct format.
#Also checking to see if there is any missing values.
df.info()

#Removing unwanted charicters from Column headings.
def run():
    lis = ['ubk', 'xaw', 'lml', 'jmo', 'lme']
    
    for i in lis:
        df.columns = df.columns.str.replace(i[0:3],'')                       
run()

df.columns = df.columns

#Checking if unwanted charicters are removed. 
df.info()

#Dropping any duplicates and rechecking dataset using "df.shape"
df.drop_duplicates(inplace=True)
df.shape

#Checking to see if there is any null values.
#Column: "GoodQuantity" containes 116 null values, "ActualEndTime" and "actualHoursOnTCard"
#both contain 3. The null values in "GoodQuantity can be replaced with 0.
#However the values for "ActualEndTime" and "actualHoursOnTCard" will need to be considered.
df.isna().sum()

#Replacing null values in column: "GoodQuantity" with "0" and checking the result. 
df = df.fillna({'GoodQuantity':'0'})
df.isna().sum()



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
#plt.plot(leo.directEarnedHours)
#plt.plot(shaun.directEarnedHours)
#plt.plot(murray.directEarnedHours)
#plt.plot(fernando.directEarnedHours)
plt.plot(cell_2.directEarnedHours)

import seaborn as sns

#sns.scatterplot(data=cell_2, x='weekDay', y='directEarnedHours' )












#cell_2.to_excel("123.xlsx")   
      


  


    
