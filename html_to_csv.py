# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 12:58:48 2016

@author: Jimmy
"""
import pandas as pd
from pandas import Series, DataFrame
from pandas import read_html
import os

os.chdir('c:\\in')

url = 'file:///C:/Users/Jimmy/AppData/Local/Temp/Temp1_eFACTS_Tables_And_Columns_List.zip/eFACTS_Tables_And_Columns_List.html'

dframe_list = pd.io.html.read_html(url)

df = dframe_list[0]

#df.set_index('TABLE_NAME', inplace=True)

df.to_csv('padep_schema.csv')