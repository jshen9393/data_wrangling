from openpyxl import load_workbook
import csv
import os

excel_dir = "C:\\Users\\Jimmy\\Google Drive\\TSIP\\UK Unemployment\\"
excel_file = "neettablesaj15_tcm77-413803.xlsx"

wb = load_workbook(os.path.join(excel_dir, excel_file), read_only=True)
ws = wb['People - SA']

csv_dir = "C:\\Users\\Jimmy\\Google Drive\\TSIP\\UK Unemployment\\"
csv_file = "neettablesaj15_tcm77-413803_people_sa.csv"

with open(os.path.join(csv_dir, csv_file), 'wb') as f:
    c = csv.writer(f)
    for r in ws.rows:
    	c.writerow(str([cell.value for cell in r]).strip('[]'))
       