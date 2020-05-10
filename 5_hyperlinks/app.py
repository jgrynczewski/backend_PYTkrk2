from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/pierwszy")
def first():
    return render_template("first_view.html")


@app.route("/drugi")
def second():
    return render_template("second_view.html")

