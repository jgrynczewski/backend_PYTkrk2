from flask import Flask
from flask import render_template

app = Flask(__name__)

text = [
    'To moja pierwsza strona',
    'To moja druga strona',
    'To moja trzecia strona'
    ]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/first")
def first():
    return text[0]


@app.route("/second")
def second():
    return text[1]


@app.route("/third")
def third():
    return text[2]