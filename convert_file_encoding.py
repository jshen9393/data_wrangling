# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:42:23 2015

@author: Jimmy

How to convert file encoding
"""


with open(ff_name, 'rb') as source_file:
  with open(target_file_name, 'w+b') as dest_file:
    contents = source_file.read()
    dest_file.write(contents.decode('utf-16').encode('utf-8'))
    
    