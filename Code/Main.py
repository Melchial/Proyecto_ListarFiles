import pathlib
from pathlib import Path
import xlsxwriter
from datetime import datetime

rutas = []

rutas.append('Z:\\')
rutas.append('Y:\\')
rutas.append('X:\\smb1\\Descargas')

files = []

for r in rutas:
    p = Path(r).glob('**/*')
    # files = [x for x in p if x.is_file() and x.suffix in ('.mp4','.avi') ]
    for x in p:
        if x.is_file() and x.suffix in ('.mp4','.avi'):
            files.append(x)
    # break


# for f in  files:

#     print(str(f.parent))
#     print(type(f))

workbook = xlsxwriter.Workbook("Data_List.xlsx")

worksheet = workbook.add_worksheet("ListaMaster")

row = 1
column = 1

worksheet.write (row,column,"Ruta")
column +=1
worksheet.write (row,column,"Archivo")
column +=1
worksheet.write (row,column,"Link")
column +=1
worksheet.write (row,column,"FechaMod")

row +=1
# worksheet.write("A1", "Hello world")
date_format = workbook.add_format()
date_format.set_num_format('dd/mm/yyyy hh:mm AM/PM')

for f in files:
    
    ruta = str(f.parent)
    fname = str(f.name)
    fmod =  datetime.fromtimestamp(f.stat().st_mtime)

    column = 1
    worksheet.write_url (row,column,url=ruta, string=ruta)
    column +=1
    worksheet.write (row,column,fname)
    column +=1
    worksheet.write_url (row,column,url=str(f), string=fname)
    column +=1
    worksheet.write_datetime (row,column,fmod,date_format)

    row +=1
workbook.close()

# print (files)