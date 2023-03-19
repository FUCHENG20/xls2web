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
    num_rows, num_cols = mymodule.getsheetdimension(pagina, num_hoja)
    return jsonify({'Filas': num_rows, 'Columnas': num_cols})

if __name__ == '__main__':
    app.run()