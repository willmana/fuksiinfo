from flask import render_template
from application import app

@app.route("/tapahtumat")
def index():
    return render_template("index.html")

@app.route("/")
def viikko_taulu():
    return render_template("taulu.html")
