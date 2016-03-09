# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:33:48 2016

@author: Jimmy
"""
import pandas as pd
import numpy as np
import chardet as cd
import os

directory = 'c:\\in'

os.chdir(directory)

def file_encoding_validation(infile, encoding = 'UTF-8'):
    with open(infile,'rb') as file:
        file = file.read()    
        file_encoding = cd.detect(file)
        file_encoding = file_encoding['encoding']
    if encoding != file_encoding:
        print('converting file from',file_encoding,'to',encoding)
        data = file.decode(file_encoding)
        data = data.encode(encoding)
        data = data.decode(encoding)
        with open('conv_'+ infile,'w+b') as outfile:
            outfile.write(bytes(data,encoding))
    else:
        print('file is already in desired',encoding,'format')  

                
def remove_blank_columns():
    #it deletes everything in the dataframe in this function
    #the for statement works perfectly
    global df
    columns = df.columns.values
    for c in columns:
        values = pd.unique(df[c])   
        if len(values) == 1 and np.isnan(values).any():
            df = df.drop([c],axis=1)
            print(c,'was blank.  Column deleted.')
        else:
            print(c,'is a valid column')

def quick_export(dataframe):
    dataframe=dataframe
    with open('quickexport.csv','w') as file:
        dataframe.to_csv(file)
'''
#select columns with filters
df[(df['PassType']=='SHORT RIGHT')]['DataError']


Display column names

my_dataframe.columns.values

Get distinct values
pandas.unique(dataframe.['columnname'])

remove 

'''

