import openpyxl as xls
import pymongo

wb = xls.load_workbook('finishe(8).xlsm')
ws = wb['Лист1']
con = pymongo.MongoClient(host='localhost', port=27017)
db = con.db
collection = db.trashers
r = []
for row in ws.iter_rows(min_row=2):
    d = {'coords': row[1].value}
    c = []
    for i in range(3, 16):
        if row[i].value == 1:
            c.append(i - 2)
    d['types'] = c
    r.append(pymongo.InsertOne(d))

res = collection.bulk_write(r)
con.close()