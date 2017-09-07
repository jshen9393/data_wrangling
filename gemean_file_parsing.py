
import csv

'''
Export query in sql server:
    
select CL_PROG_NOTE_ID, NOTE_MEMO_CARETECH, NOTE_MEMO, SUBJECT
from [dbo].[CLAIM_PRG_NOTE]


select ENTRY_ID, ENTRY_NOTES, RESPONSE
from [dbo].[WPA_DIARY_ENTRY]
'''


#export file location
infile = 'C:\\Users\\gemean.GEM\\Documents\\'
outfile = 'C:\\Users\\gemean.GEM\\Documents\\files\\'

def rowid(id):
    zeros = 6-len(str(id))
    return '0'*zeros + id

def filename(tablename, rowid, columnname):
    return tablename + '_' + rowid + '_' + columnname +'.txt'
    

#CLAIM_PRG_NOTE table file creation
tablename = 'CLAIM_PRG_NOTE'
columnname = 'NOTE_MEMO_CARETECH'

with open(infile+'CLAIM_PRG_NOTE.txt',encoding="utf-8-sig") as f:  
    c = csv.reader(f,delimiter='\t', quotechar=None)
    for i in c: 
        try:        
            with open(outfile+filename(tablename,rowid(str(i[0])),columnname),'w') as of:
                w = csv.writer(of,delimiter='\t')
                w.writerow([i[1]])
                print(i[0],'done')
        except:
            with open(outfile+'errors.txt','a') as e:
                w = csv.writer(e,delimiter='\t')
                w.writerow([i[0],columnname])
                print('error detected',i[0],columnname)

tablename = 'CLAIM_PRG_NOTE'
columnname = 'NOTE_MEMO'


with open(infile+'CLAIM_PRG_NOTE.txt',encoding="utf-8-sig") as f:  
    c = csv.reader(f,delimiter='\t', quotechar=None)
    for i in c: 
        try:        
            with open(outfile+filename(tablename,rowid(str(i[0])),columnname),'w') as of:
                w = csv.writer(of,delimiter='\t')
                w.writerow([i[2]])
                print(i[0],'done')
        except:
            with open(outfile+'errors.txt','a') as e:
                w = csv.writer(e,delimiter='\t')
                w.writerow([i[0],columnname])
                print('error detected',i[0],columnname)


tablename = 'CLAIM_PRG_NOTE'
columnname = 'SUBJECT'

with open(infile+'CLAIM_PRG_NOTE.txt',encoding="utf-8-sig") as f:  
    c = csv.reader(f,delimiter='\t', quotechar=None)
    
    for i in c: 
        print(i[0])
        if int(i[0]) > 418341:
            try:        
                with open(outfile+filename(tablename,rowid(str(i[0])),columnname),'w') as of:
                    w = csv.writer(of,delimiter='\t')
                    w.writerow([i[3]])
                    print(i[0],'done')
            except:
                with open(outfile+'errors.txt','a') as e:
                    w = csv.writer(e,delimiter='\t')
                    w.writerow([i[0],columnname])
                    print('error detected',i[0],columnname)



#DIARY_ENTRY table file creation

tablename = 'WPA_DIARY_ENTRY'
columnname = 'ENTRY_NOTES'

with open(infile+'WPA_DIARY_ENTRY.txt',encoding="utf-8-sig") as f:  
    c = csv.reader(f,delimiter='\t')
    for i in c: 
        try:        
            with open(outfile+filename(tablename,rowid(str(i[0])),columnname),'w') as of:
                w = csv.writer(of,delimiter='\t')
                w.writerow([i[1]])
                print(i[0],'done')
        except:
            with open(outfile+'errors.txt','a') as e:
                w = csv.writer(e,delimiter='\t')
                w.writerow([i[0],columnname])
                print('error detected',i[0],columnname)

tablename = 'WPA_DIARY_ENTRY'
columnname = 'RESPONSE'

with open(infile+'WPA_DIARY_ENTRY.txt',encoding="utf-8-sig") as f:  
    c = csv.reader(f,delimiter='\t')
    for i in c: 
        try:        
            with open(outfile+filename(tablename,rowid(str(i[0])),columnname),'w') as of:
                w = csv.writer(of,delimiter='\t')
                w.writerow([i[2]])
                print(i[0],'done')
        except:
            with open(outfile+'errors.txt','a') as e:
                w = csv.writer(e,delimiter='\t')
                w.writerow([i[0],columnname])
                print('error detected',i[0],columnname)


