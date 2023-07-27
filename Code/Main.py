
from pathlib import Path
from excel_file import write_excel
from datetime import datetime
import mysql.connector


rutas = []

rutas.append('Z:\\')
rutas.append('Y:\\')
rutas.append('X:\\smb1\\Descargas')

files = []

for r in rutas:
    p = Path(r).glob('**/*')
    # files = [x for x in p if x.is_file() and x.suffix in ('.mp4','.avi') ]
    for x in p:
        if x.is_file() and x.suffix in ('.mp4','.avi','.mkv','.wmv'):
            files.append(x)
    # break

# write_excel(files=files)


# print(files)

cnx = mysql.connector.connect(user='userdba', password='Grecia*456',
                              host='192.168.1.152',
                              database='data'
                              ,port='3307')

cursor = cnx.cursor()

file_insert = []

for f in files:
        
    ruta = str(f.parent)
    fname = str(f.name)
    fnameOnlyStr = str(f.name).removesuffix(f.suffix).split("-") 
    FnameCodeNumber= ''

    fnameCodeSuffix = fnameOnlyStr[0]
    if len(fnameOnlyStr) >1:
        FnameCodeNumber = fnameOnlyStr[1]

    fnameOnly = f"{fnameCodeSuffix}-{FnameCodeNumber.split('_')[0]}"

    fmod =  datetime.fromtimestamp(f.stat().st_mtime)

    # print(ruta,str(f),fnameOnly,fmod)

    file_insert.append( (fnameOnly,fname,str(f),fmod)  )




exit

sql_del = "DELETE FROM vid_files"

cursor.execute(sql_del)

sql = "INSERT INTO vid_files (file_vid_cod,file_name,file_uri,file_datemod) VALUES (%s, %s, %s,%s)"

cursor.executemany(sql, file_insert)
cnx.commit()

cnx.close()

# query = ("SELECT vid_id, vid_tittle FROM tb_videos "
#          "WHERE vid_id BETWEEN %s AND %s")

# hire_start = datetime.date(1999, 1, 1)
# hire_end = datetime.date(1999, 12, 31)

# id_init = 20
# id_end = 60

# cursor.execute(query, (id_init, id_end))


# for (vid_id, vid_tittle) in cursor:
#   print("{}, {} was hired on ".format(
#     vid_id, vid_tittle))

# cursor.close()


# cnx.close()


# for f in  files:

#     print(str(f.parent))
#     print(type(f))

# workbook = xlsxwriter.Workbook("Data_Files.xlsx")

# worksheet = workbook.add_worksheet("ListaMaster")

# row = 1
# column = 1

# worksheet.write (row,column,"Ruta")
# column +=1
# worksheet.write (row,column,"Archivo")
# column +=1
# worksheet.write (row,column,"Link")
# column +=1
# worksheet.write (row,column,"FechaMod")

# row +=1
# # worksheet.write("A1", "Hello world")
# date_format = workbook.add_format()
# date_format.set_num_format('dd/mm/yyyy hh:mm AM/PM')

# for f in files:
    
#     ruta = str(f.parent)
#     fname = str(f.name)
#     fnameOnlyStr = str(f.name).removesuffix(f.suffix).split("-") 
#     FnameCodeNumber= ''

#     fnameCodeSuffix = fnameOnlyStr[0]
#     if len(fnameOnlyStr) >1:
#         FnameCodeNumber = fnameOnlyStr[1]

#     fnameOnly = f"{fnameCodeSuffix}-{FnameCodeNumber.split('_')[0]}"

#     fmod =  datetime.fromtimestamp(f.stat().st_mtime)

#     column = 1
#     worksheet.write_url (row,column,url=ruta, string=ruta)
#     column +=1
#     worksheet.write (row,column,fnameOnly)
#     column +=1
#     worksheet.write_url (row,column,url=str(f), string=str(f))
#     column +=1
#     worksheet.write_datetime (row,column,fmod,date_format)

#     row +=1
# workbook.close()

# print (files)