import xlrd

##############################TAREA#####################################
# Funcion que regresa cuantas hojas hay en el archivo
def getnumsheets(pagina):
    book = xlrd.open_workbook(pagina)
    return book.nsheets

# Funcion que regresa cuantos renglones y columnas tiene una hoja
def getsheetdimension(pagina, num_hoja):
    # Obtener la hoja de cálculo especificada por el número de hoja
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_index(int(num_hoja))
    num_rows = sheet.nrows
    num_cols = sheet.ncols
    return (num_rows, num_cols)