
import xlsxwriter
from datetime import datetime

def write_excel (files:[]):
    workbook = xlsxwriter.Workbook("Data_Files.xlsx")

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
        fnameOnlyStr = str(f.name).removesuffix(f.suffix).split("-") 
        FnameCodeNumber= ''

        fnameCodeSuffix = fnameOnlyStr[0]
        if len(fnameOnlyStr) >1:
            FnameCodeNumber = fnameOnlyStr[1]

        fnameOnly = f"{fnameCodeSuffix}-{FnameCodeNumber.split('_')[0]}"

        fmod =  datetime.fromtimestamp(f.stat().st_mtime)

        column = 1
        worksheet.write_url (row,column,url=ruta, string=ruta)
        column +=1
        worksheet.write (row,column,fnameOnly)
        column +=1
        worksheet.write_url (row,column,url=str(f), string=str(f))
        column +=1
        worksheet.write_datetime (row,column,fmod,date_format)

        row +=1
    workbook.close()




