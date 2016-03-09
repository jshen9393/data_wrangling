# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:54:42 2016

@author: Jimmy
"""
import pandas as pd
import os

os.chdir('c:\\in')

df = pd.read_csv('FBI-CRIME11.csv')

#df = df.set_index('Year')

df.set_index('Year', inplace = True)

df['Violent Crime Rate'].to_csv('newcsv2.csv')



df = pd.read_csv('newcsv2.csv',index_col=0)

df = pd.read_csv('newcsv2.csv',names = ['Date','Violent Crime Rate'], index_col=0)

df.to_csv('newcsv3.csv')
df.to_csv('newcsv4.csv',header=False)