from flask import Flask, jsonify
import mymodule

app = Flask(__name__)

@app.route('/')
def saludo():
    return 'Hola, Mundo'

#route #1
@app.route('/num_pag/<pagina>')
def num_pag(pagina):
    ruta = mymodule.getnumsheets(pagina)
    return jsonify({'Archivo ': pagina, 'Hojas ' : ruta})

#route #2
@app.route('/dimension/<pagina>/<num_hoja>')
def dimension(pagina, num_hoja):
    num_rows, num_cols = mymodule.getsheetdimension(pagina, int(num_hoja))
    return jsonify({'Archivo' : pagina, 'Numero de Hoja' : num_hoja, 'Filas': num_rows, 'Columnas': num_cols})

#route #3
@app.route('/contenidocelda/<pagina>/<num_hoja>/<num_row>/<num_col>')
def contenidocelda(pagina, num_hoja, num_row, num_col):
    content = mymodule.getcellcontent(pagina, int(num_hoja), int(num_row), int(num_col))
    return jsonify({'Archivo' : pagina, 'Numero de Hoja' : num_hoja,'Contenido': content ,'Fila': num_row, 'Columna': num_col})

#route #4
@app.route('/columna/<pagina>/<nom_hoja>/<num_col>')
def columna(pagina, nom_hoja, num_col):
    content = mymodule.getcolumnvalues(pagina, str(nom_hoja), num_col)
    return jsonify({'contenido': content})

if __name__ == '__main__':
    app.run()