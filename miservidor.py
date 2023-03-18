from flask import Flask, make_response
import mymodule
import xlrd

app = Flask(__name__)

@app.route('/')
def saludo():
    return 'Hola, Mundo'

@app.route('/mymodule')
def hello():
    book = xlrd.open_workbook('pagina.xls')
    num_sheets = mymodule.getnumsheets(book)
    print("El archivo tiene", num_sheets, "hojas")

    num_rows, num_cols = mymodule.getsheetdimension(book, 0)
    print("La primera hoja tiene", num_rows, "renglones y", num_cols, "columnas")

if __name__ == '__main__':
    app.run()