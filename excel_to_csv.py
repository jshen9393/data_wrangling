import os
import xlrd
import csv

excel_dir = "C:\\Users\\Jimmy\\Google Drive\\TSIP\\UK Unemployment\\"
excel_file = "neettablesaj15_tcm77-413803_2.xlsx"

wb = xlrd.open_workbook(os.path.join(excel_dir, excel_file), 'wb')
ws = wb.sheet_by_name('People - SA')


csv_dir = "C:\\Users\\Jimmy\\Google Drive\\TSIP\\UK Unemployment\\"
csv_filename = "neettablesaj15_tcm77-413803_people_sa.csv"

cf = open(os.path.join(csv_dir, csv_filename), 'wb')
cw = csv.writer(cf,quoting=csv.QUOTE_ALL)

for rownum in range(ws.nrows):
	cw.writerow(ws.row_values(rownum))
'''
Running into 'read only' error problem.
'''

cf.close()