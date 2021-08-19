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
df.head(10)

#looking at data set to determine if data is in the correct format.
df.info()

#Some of the headings have unwanted index charicters from the export. 
#Removing unwanted charicters from Column headings.
def clean():
    lis = ['ubk', 'xaw', 'lml', 'jmo', 'lme']
    
    for i in lis:
        df.columns = df.columns.str.replace(i[0:3],'')                       
clean()

df.columns = df.columns

#Checking if unwanted charicters are removed. 
df.info()

#Dropping any duplicates and rechecking dataset using "df.shape"
df.drop_duplicates(inplace=True)
df.shape

#Checking to see if only cell operators are within the dataset.
#If there is aditional operators within the dataset it indicates that they logged on to the incorrect machine.
print(df['EmployeeName'])

#Cell_2_operatives = ['Shaun Murphy', 'Leo Cunniffe', 'Murray Pascall', 'Fernando Toni']

#Applying filter to dataset to only show the relevant operatives.
#Dataset was renamed "cell_2" as an analysis of incorrect loggin's is required on "df"
cell_2 = df[(df.EmployeeName == 'Leo Cunniffe') | (df.EmployeeName == 'Shaun Murphy') | 
        (df.EmployeeName == 'Murray Pascall') |  (df.EmployeeName == 'Fernando Toni')]

#Conferming that unwanted operators are removed.
print(cell_2['EmployeeName'])

#Checking to see if there is any null values.
#Column: "GoodQuantity" containes 86 null values, "ActualEndTime" and "actualHoursOnTCard"
#both contain 3. The null values in "GoodQuantity can be replaced with 0.
#However the values for "ActualEndTime" and "actualHoursOnTCard" will need to be considered.
print(cell_2.isna().sum())

#Replacing null values in column: "GoodQuantity" with "0" and checking the result. 
cell_2 = cell_2.fillna({'GoodQuantity':'0'})
print(cell_2.isna().sum() / len(cell_2)*100)

#The remaining two missing values equate to 0.43% of the total in that column.
#Thus deleting the rows will not significently alter the analysis results.
print(cell_2.dropna().info())

#Creating seperate datasets for each operative.
leo = cell_2[cell_2.EmployeeName == 'Leo Cunniffe']
shaun = cell_2[cell_2.EmployeeName == 'Shaun Murphy']
murray = cell_2[cell_2.EmployeeName == 'Murray Pascall']
fernando = cell_2[cell_2.EmployeeName == 'Fernando Toni']

#Playing around with graphs.
import matplotlib.pyplot as plt

plt.xlabel('Date')
plt.ylabel('Hrs')
plt.title('Earned Hours Trend Line')
#plt.plot(leo.directEarnedHours)
#plt.plot(leo.actualHoursOnTCard)
#plt.plot(shaun.directEarnedHours)
#plt.plot(murray.directEarnedHours)
#plt.plot(fernando.directEarnedHours)
#plt.plot(cell_2.directEarnedHours)

import seaborn as sns

#This scatter plot shows some interesting 
sns.lineplot(data=cell_2, x='actionDate', y='directEarnedHours')
sns.lineplot(data=cell_2, x='actionDate', y='actualHoursOnTCard')













#cell_2.to_excel("123.xlsx")   
      


  


    
