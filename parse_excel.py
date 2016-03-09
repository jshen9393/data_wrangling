import os
from openpyxl import load_workbook

directory = "C:\\Users\\Jimmy\\Google Drive\\TSIP\\UK Unemployment\\"
filename = "neettablesaj15_tcm77-413803.xlsx"



wb = load_workbook(os.path.join(directory, filename), read_only=True)
ws = wb['People - SA'] # ws is now an IterableWorksheet

for row in ws.rows:
    print(row)

'''
for row in ws.rows:
    for cell in row:
        print(cell.value)
'''

