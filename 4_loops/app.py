from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    fruits = ['jabłko', 'banan', 'winogrona', 'manadarynki']
    return render_template("index.html", fruits=fruits)