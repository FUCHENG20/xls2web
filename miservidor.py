from flask import Flask
import mymodule

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/excel/columna1')
def columna():
    return "Columna 1 data"

@app.route("/mymodule")
def module():
    return(mymodule.saludo())

if __name__ =='__main__':
    print("main saludo")
    app.run()