# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:42:23 2015

@author: Jimmy
"""

import os
import pandas as pd
from pandas import Series, DataFrame
import re

folder = 'C:\\in'
os.chdir(folder)
outfile = 'karina1.csv'


file = '''
Karina results #1 files
Karina results #1 files
Karina results #1 files

1)
Name	BirthCert.doc
File Category	Document
File Type	Word Document
Is Deleted	
File Created	03/29/14 03:22:59PM
Last Written	08/18/08 01:20:48PM
Entry Modified	12/18/14 11:18:53AM
File Deleted	
File Acquired	04/28/15 01:54:45PM
Physical Size	32,768
Physical Location	546,930,589,696
Full Path	Karina Case files\D\Karina Results\Andrew Lexar 32gb\andrew.parise@promptcare.net\BirthCert.doc

2)
Name	Dr hatefi.DOC
File Category	Document
File Type	Word Document
Is Deleted	
File Created	03/29/14 03:22:59PM
Last Written	01/08/10 01:35:12PM
Entry Modified	12/18/14 11:18:53AM
File Deleted	
File Acquired	04/28/15 01:54:45PM
Physical Size	81,920
Physical Location	510,074,650,624
Full Path	Karina Case files\D\Karina Results\Andrew Lexar 32gb\andrew.parise@promptcare.net\Dr hatefi.DOC

'''

#location of files



'''
with open(file,'r') as open_file:
    data = open_file.read()
 '''    
'''
row_regex
raw_rows = row_regex.findall(file)
row_num = [r.strip('\)') for r in raw_rows]
'''
name_regex = re.compile(r'^Name\t.+$',re.M) ##re.M = multiline
raw_names = name_regex.findall(file)
name = [r.strip('Name\t') for r in raw_names]

file_cat_regex = re.compile(r'^File Category\t.*$',re.M) ##re.M = multiline
raw_file_cat = file_cat_regex.findall(file)
file_cat = [r.strip('File Category\t') for r in raw_file_cat]

file_type_regex = re.compile(r'^File Type\t.*$',re.M) ##re.M = multiline
raw_file_type = file_type_regex.findall(file)
file_type = [r.strip('File Type\t') for r in raw_file_type]

deleted_regex =re.compile(r'^Is Deleted\t.*$',re.M)
raw_deleted = deleted_regex.findall(file)
is_deleted = [r.strip('Is Deleted\t') for r in raw_deleted]

created_regex =re.compile(r'^File Created\t.*$',re.M)
raw_created = created_regex.findall(file)
file_created = [r.strip('File Created\t') for r in raw_created]

written_regex =re.compile(r'^Last Written\t.*$',re.M)
raw_written = written_regex.findall(file)
last_written = [r.strip('Last Written\t') for r in raw_written]

modified_regex =re.compile(r'^Entry Modified\t.*$',re.M)
raw_modified = modified_regex.findall(file)
entry_modified = [r.strip('Entry Modified\t') for r in raw_modified]

file_del_regex =re.compile(r'^File Deleted\t.*$',re.M)
raw_file_del = file_del_regex.findall(file)
file_deleted = [r.strip('File Deleted\t') for r in raw_file_del]


acq_regex =re.compile(r'^File Acquired\t.*$',re.M)
raw_acq = acq_regex.findall(file)
file_acquired = [r.strip('File Acquired\t') for r in raw_acq]

size_regex =re.compile(r'^Physical Size\t.*$',re.M)
raw_size = size_regex.findall(file)
physical_size = [r.strip('Physical Size\t') for r in raw_size]

location_regex =re.compile(r'^Physical Location\t.*$',re.M)
raw_location = location_regex.findall(file)
physical_location = [r.strip('Physical Location\t') for r in raw_location]

path_regex =re.compile(r'^Full Path\t.*$',re.M)
raw_path = path_regex.findall(file)
full_path = [r.strip('Full Path\t') for r in raw_path]

keyword_regex =re.compile(r'^Full Path\t.*$',re.M)
raw_keyword = str(keyword_regex.findall(file))
keyword_regex2 =re.compile(r'\w+$',re.M)
raw_keyword2 = keyword_regex2.findall(raw_keyword)


#row_num=DataFrame(row_num, columns=['row_num'])
name=DataFrame(name, columns=['name'])
file_cat=DataFrame(file_cat, columns=['file_cat'])
file_type=DataFrame(file_type, columns=['file_type'])
is_deleted=DataFrame(is_deleted, columns=['is_deleted'])
file_created=DataFrame(file_created, columns=['file_created'])
last_written=DataFrame(last_written, columns=['last_written'])
file_deleted=DataFrame(file_deleted, columns=['file_deleted'])
file_acquired=DataFrame(file_acquired, columns=['file_acquired'])
physical_size=DataFrame(physical_size, columns=['physical_size'])
physical_location=DataFrame(physical_location, columns=['physical_location'])
full_path=DataFrame(full_path,columns=['full_path'])


dataframe = pd.concat([name,file_cat,file_type,is_deleted,file_created,last_written,file_deleted,file_acquired,physical_size,physical_location,full_path], axis=1)



#dataframe.to_csv(outfile)
print(name)