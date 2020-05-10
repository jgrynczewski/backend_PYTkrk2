import random

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", context="Hello")

@app.route("/goodbye")
def goodbye():
    text = "Goodbye"
    return render_template("index.html", context=text)

@app.route("/choice")
def choice():
    text = ["Hello", "Hi", "Goodbye", "Good morning", "Good evening"]
    return render_template("index.html", context=random.choice(text))