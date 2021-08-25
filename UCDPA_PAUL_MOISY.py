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

#updating the week day names.
df['weekDay'].replace([2, 3, 4, 5, 6, 7], ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], inplace = True)

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
#both contain 2. The null values in "GoodQuantity can be replaced with 0.
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
import numpy as np
import seaborn as sns


#Earned hours (Quoted time) vs actual hours (time spent on job) for leo.
plt.figure(figsize=(7,3))
plt.xlabel('Date')
plt.ylabel('Hrs')
plt.title('Earned Hours Vs actual Hours for Leo')
plt.plot(leo.directEarnedHours, label = 'directEarnedHours')
plt.plot(leo.actualHoursOnTCard, label ='actualHoursOnTCard')
plt.legend();

#Earned hours (Quoted time) vs actual hours (time spent on job) for shaun.
plt.figure(figsize=(7,3))
plt.xlabel('Date')
plt.ylabel('Hrs')
plt.title('Earned Hours Vs actual Hours for Shaun')
plt.plot(shaun.directEarnedHours, label = 'directEarnedHours')
plt.plot(shaun.actualHoursOnTCard, label ='actualHoursOnTCard')
plt.legend();

#Earned hours (Quoted time) vs actual hours (time spent on job) for murray.
plt.figure(figsize=(7,3))
plt.xlabel('Date')
plt.ylabel('Hrs')
plt.title('Earned Hours Vs actual Hours for Murray')
plt.plot(murray.directEarnedHours, label = 'directEarnedHours')
plt.plot(murray.actualHoursOnTCard, label ='actualHoursOnTCard')
plt.legend();

#Earned hours (Quoted time) vs actual hours (time spent on job) for Fernando.
plt.figure(figsize=(7,3))
plt.xlabel('Date')
plt.ylabel('Hrs')
plt.title('Earned Hours Vs actual Hours for Fernando')
plt.plot(fernando.directEarnedHours, label = 'directEarnedHours')
plt.plot(fernando.actualHoursOnTCard, label ='actualHoursOnTCard')
plt.legend();

#Earned hours (Quoted time) vs actual hours (time spent on job) for whole production cell.
plt.figure(figsize=(7,3))
plt.xlabel('Date')
plt.ylabel('Hrs')
plt.title('Earned Hours Vs actual Hours for Cell_2')
plt.plot(cell_2.directEarnedHours, label = 'directEarnedHours')
plt.plot(cell_2.actualHoursOnTCard, label ='actualHoursOnTCard')
plt.legend();

plt.figure(figsize=(7,3))
plt.title('Earned Hours Vs actual Hours for Cell_2')
plt.xlabel('Date')
plt.ylabel('Hrs')
sns.lineplot(data=cell_2, x='actionDate', y='directEarnedHours', label = 'directEarnedHours')
sns.lineplot(data=cell_2, x='actionDate', y='actualHoursOnTCard', label ='actualHoursOnTCard')
plt.legend();



#In this section i try to determine if the cell is clearing a profit based on the hours quoted for the job and hours worked. 
#It appers that there is roughly a 32% profit margin.
mean_earned = np.mean(cell_2.directEarnedHours)
mean_actual = np.mean(cell_2.actualHoursOnTCard)

profit_labels = np.array(['Earned Hours', 'Actual Hours'])
cell_2_means = np.array([mean_earned, mean_actual])

Profit_margin = (str((mean_earned/mean_actual * 100)-100) + "%")
print('Average Daily Profit margin = ' + Profit_margin)

#plt.title('Average Daily Earned Vs Actual Hours')
plt.ylabel('Hrs')
sns.barplot(profit_labels, cell_2_means) 



#This graph shouw how long operatives spend on operations by sector.
#The black lines indicate the distribution of teh data per sector. 
plt.title('Time on jobcard Vs Busness unit')
sns.barplot(data=cell_2, y='BusinessUnit', x='actualHoursOnTCard', order = ['Tooling', 'Production', 'Medical']);

#This graph showes the average amount of earned hours per sector. 
#Again the distribution is indicated by the black line.
plt.title('Earned Hours Vs Busness unit')
sns.barplot(data=cell_2, y='BusinessUnit', x='directEarnedHours', order = ['Production', 'Medical', 'Tooling']);

#this graph shows the average spread of earned hours over a week.
#The data set for saturday only contains one point and ths does not display a distribution. 
plt.title('Earned hours Vs Week day')
sns.barplot(data=cell_2, x = 'weekDay', y = 'directEarnedHours');



mean_leo = np.mean(leo.actualHoursOnTCard)
mean_Shaun = np.mean(shaun.actualHoursOnTCard)
mean_fernando = np.mean(fernando.actualHoursOnTCard)
mean_murray = np.mean(murray.actualHoursOnTCard)

operators = np.array(['Shaun', 'Fernando', 'Leo', 'Murray'])
Means = np.array([mean_Shaun, mean_fernando, mean_leo, mean_murray])

plt.title('Mean time clocked to operation')
plt.xlabel('Hours')
sns.barplot(Means, operators);

#cell_2.to_excel("123.xlsx")   
      


  


    
