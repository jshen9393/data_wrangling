
import csv


with open(infile+'WPA_DIARY_ENTRY.txt',"r") as f:
    reader = csv.reader(f,delimiter = "\t")  
    data = list(reader)
    row_count = len(data)
print (row_count)
