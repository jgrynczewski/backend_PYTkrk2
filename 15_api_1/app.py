from flask import Flask
from flask import render_template
from flask import request

import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    amount = request.form.get("amount")
    base = request.form.get("base")
    currency = request.form.get("currency")

    res = requests.get("http://data.fixer.io/api/latest",
                       params = {
                           "access_key" : "032053b70cf616de08638aeaeb1cfd1d",
                           "base": base,
                           "symbols": currency
                       })

    data = res.json()

    rates = data.get("rates")
    if rates:
        converter = rates.get(currency)
    else:
        return "Coś poszło nie tak"

    return f"Wypłacam {round(float(amount) * converter, 2)} {currency}"
