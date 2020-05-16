from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

tasks = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        tasks.append(task)
    return render_template("index.html", tasks=tasks)