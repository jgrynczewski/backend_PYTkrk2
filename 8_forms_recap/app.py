from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form.get("imie")
        return render_template("hello.html", name=name)
    else:
        return render_template("hello.html", name="")

if __name__=="__main__":
    app.run(debug=True)