# Web application
import requests

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    base = request.form.get("base")
    symbol = request.form.get("symbol")

    res = requests.get("http://data.fixer.io/api/latest?access_key=032053b70cf616de08638aeaeb1cfd1d",
                       params={"base": base, "symbols": symbol})
    if res.status_code != 200:
        return f"Niepowodzenie. Kod HTTP {res.status_code}"

    data = res.json()
    if not data.get("success"):
        return f"Coś poszło nie tak w trakcie przetwarzania zapytania w api " \
               f"{data['error']['type']}"

    rate1 = None
    rates = data.get('rates')
    if rates:
        rate1 = rates.get(symbol)

    return f"1 {base} równa się {rate1} {symbol}"


