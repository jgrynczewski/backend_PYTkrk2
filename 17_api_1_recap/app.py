from flask import Flask
from flask import render_template
from flask import request

import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")

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
        result = f"Wypłacam {round(float(amount) * converter, 2)} {currency}"
    else:
        result="Coś poszło nie tak"

    return render_template('index.html', result=result)
