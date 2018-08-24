from application import app
from flask import redirect, render_template


@app.route("/sites/taulu/")
def viikko_taulu():
    return render_template("sites/taulu.html")
