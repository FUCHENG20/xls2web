import xlrd

##############################TAREA#####################################

# FUNCION #1 que regresa cuantas hojas hay en el archivo
def getnumsheets(pagina):
    book = xlrd.open_workbook(pagina)
    return book.nsheets

# FUNCION #2 que regresa cuantos renglones y columnas tiene una hoja
def getsheetdimension(pagina, num_hoja):
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_index(num_hoja)
    num_rows = sheet.nrows
    num_cols = sheet.ncols
    return (num_rows, num_cols)

# FUNCION #3 que regresa el contenido de una celda en una hoja especifica
def getcellcontent(pagina, num_hoja, num_row, num_col):
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_index(num_hoja)
    cell_value = sheet.cell_value(num_row, num_col)
    return cell_value

# FUNCION #4 que regresa el contenido de una columna completa
def getcolumnvalues(pagina, nom_hoja, num_col):
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_name(nom_hoja)
    values = []
    for row_index in range(sheet.nrows):
        cell_value = sheet.cell(row_index, int(num_col) - 1).value
        values.append(cell_value)
    return values

# FUNCION #5 que revisa la cabecera de la columna "para validar el nombre de la columna"
def checkcolumnheader(pagina, nom_hoja, num_col, cabecera_e):
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_name(nom_hoja)
    header = sheet.cell(0, int(num_col) - 1).value
    if header == cabecera_e:
        values = []
        for row_index in range(1, sheet.nrows):
            cell_value = sheet.cell(row_index, int(num_col) - 1).value
            values.append(cell_value)
        return True, values
    else:
        return False, None

# FUNCION #6 que regresa el contenido de N columnas en la hoja X, dame_columnas([2,4,5],hoja2)
def contentcolumns(pagina, cols, nom_hoja):
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_name(nom_hoja)
    values = []
    for col in cols:
        content = sheet.col_values(col)
        values.append(content)
    return values

# FUNCION #7 que me regresa toda la hoja en una matriz ordenada
