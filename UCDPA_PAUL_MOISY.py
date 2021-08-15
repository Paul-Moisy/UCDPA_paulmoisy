# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 13:00:20 2021

@author: Paul.Moisy
"""

import pandas as pd

df = pd.read_csv("Cell_Utilization_1.csv")

df.info()

def run():
    lis = ['ubk', 'xaw', 'lml', 'jmo', 'lme']
    
    for i in lis:
        
        df.columns = df.columns.str.replace(i[0:3],'')                       
run()

df.columns = [df.columns]

df.info()

