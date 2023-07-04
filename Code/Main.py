import pathlib
from pathlib import Path
import xlsxwriter


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


for f in  files:

    print(str(f.parent))
    print(type(f))

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

# worksheet.write("A1", "Hello world")
			

workbook.close()

# print (files)