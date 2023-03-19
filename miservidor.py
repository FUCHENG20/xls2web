from flask import Flask, jsonify
import mymodule

app = Flask(__name__)

@app.route('/')
def saludo():
    return 'Hola, Mundo'

#route #1 - http://localhost:5000/num_pag/pagina.xls
@app.route('/num_pag/<pagina>')
def num_pag(pagina):
    ruta = mymodule.getnumsheets(pagina)
    return jsonify({'Archivo' : pagina, 'Hojas' : ruta})

#route #2 - http://localhost:5000/dimension/pagina.xls/3
@app.route('/dimension/<pagina>/<num_hoja>')
def dimension(pagina, num_hoja):
    num_rows, num_cols = mymodule.getsheetdimension(pagina, int(num_hoja))
    return jsonify({'Archivo' : pagina, 'Numero_de_Hoja' : num_hoja, 
    'Filas': num_rows, 'Columnas': num_cols})

#route #3 - http://localhost:5000/contenidocelda/pagina.xls/1/1/2
@app.route('/contenidocelda/<pagina>/<num_hoja>/<num_row>/<num_col>')
def contenidocelda(pagina, num_hoja, num_row, num_col):
    content = mymodule.getcellcontent(pagina, int(num_hoja), int(num_row), int(num_col))
    return jsonify({'Archivo' : pagina, 'Numero_de_Hoja' : num_hoja,
    'Contenido': content ,'Fila': num_row, 'Columna': num_col})

#route #4 - http://localhost:5000/columna/pagina.xls/Hoja2/4
@app.route('/columna/<pagina>/<nom_hoja>/<num_col>')
def columna(pagina, nom_hoja, num_col):
    content = mymodule.getcolumnvalues(pagina, str(nom_hoja), num_col)
    return jsonify({'Archivo' : pagina, 'Contenido': content, 'Numero_Columna': num_col})

#route #5 - http://localhost:5000/verificarcabecera/pagina.xls/Hoja2/2/Nombre
@app.route('/verificarcabecera/<pagina>/<nom_hoja>/<num_col>/<cabecera_e>')
def verificarcabecera(pagina, nom_hoja, num_col, cabecera_e):
    is_valid, content = mymodule.checkcolumnheader(pagina, nom_hoja, num_col, cabecera_e)
    if is_valid:
        return jsonify({'Archivo': pagina, 'Numero_de_Hoja': nom_hoja,
        'Cabecera_de_Columna': cabecera_e, 'Contenido': content, 'Numero_Columna': num_col})
    else:
        return jsonify({'Archivo': pagina, 'Numero_de_Hoja': nom_hoja,
        'Cabecera_de_Columna': cabecera_e, 'Error': content , 'Numero_Columna': num_col})

#route #6 - http://localhost:5000/excel/contenidocolumnas/pagina.xls/1,2,3/Hoja2
@app.route('/excel/contenidocolumnas/<pagina>/<cols>/<nom_hoja>')
def contenidocolumnas(pagina, cols, nom_hoja):
    index = []
    for col in cols.split(','):
        index.append(int(col))
    content = mymodule.contentcolumns(pagina, index, nom_hoja)
    return jsonify({'Archivo': pagina, 'Numero_de_Hoja': nom_hoja, 'Contenido': content,
    'Columnas': cols})

#route #7

if __name__ == '__main__':
    app.run()