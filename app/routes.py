from app import app
from flask import render_template
import xlsdata

@app.route("/")
@app.route("/index")
def index():
    return "<p>Hello, World!</p>"
