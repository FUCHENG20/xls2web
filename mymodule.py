import xlrd
book = xlrd.open_workbook('pagina.xls')
sheets = book.nsheets
##############################TAREA#####################################
# Funcion que regresa cuantas hojas hay en el archivo
def getnumsheets(book):
    return len(book.sheet_names())

# Funcion que regresa cuantos renglones y columnas tiene una hoja
def getsheetdimension(book, sheet_index = 0):
    sheet = book.sheet_by_index(sheet_index)
    return sheet.max_row, sheet.max_column