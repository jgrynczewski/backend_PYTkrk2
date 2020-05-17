from flask import Flask
from flask import render_template
from flask import request
from flask import session

from flask_session import Session

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():

    if session.get('tasks') is None:
        session['tasks'] = []

    if request.method == "POST":
        task = request.form.get("task")
        session['tasks'].append(task)

    return render_template("index.html", tasks=session['tasks'])