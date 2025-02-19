import xlrd
book = xlrd.open_workbook('pagina.xls')
sheets = book.nsheets

def loadXLS():
    sheets = book.nsheets
    for hoja in range(sheets):
        print("----------hoja " + str(hoja))
        sheet = book.sheet_by_index(hoja)
        num_rows = sheet.nrows
        num_col = sheet.ncols
        for row in range(num_rows):
            print("")
            for col in range(num_col):
                cell = sheet.cell(row,col)
                #cell2 = sheet.cell(row,col+1)
                print(str(cell.value) + "\t",end="")

#esta funcion valida que la columna sea la de los ID y busca un id especifico
def find_page(id,page):
    sheet = book.sheet_by_index(page)
    num_rows = sheet.nrows
    num_col = sheet.ncols
    for col in range(num_col):
        cell = sheet.cell(0,col)
        if cell.value == "id":
            print("")
            for row in range(num_rows):
                cell = sheet.cell(row,col)
                rows_cell = sheet.row_values(row)
                #print(rows_cell)
                if id == rows_cell[0] and rows_cell[1] == 1:
                    print(rows_cell[0],"-",rows_cell[2],"-",rows_cell[3])
    #return cell.value

def getAboutImg():
    book = xlrd.open_workbook('pagina.xls')    
    sheet = book.sheet_by_index(0)
    cell = sheet.cell(1,1)
    return cell.value

def getAboutText():
    book = xlrd.open_workbook('pagina.xls')    
    sheet = book.sheet_by_index(0)
    cell = sheet.cell(2,1)
    return cell.value

loadXLS()
#print("Loading data for web")