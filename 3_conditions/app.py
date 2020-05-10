import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/isitnewyear")
def index():
    now = datetime.datetime.now()
    is_new_year = now.month == 1 and now.day == 1

    return render_template("index.html", is_new_year=is_new_year)