from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

from models import Task

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        t = Task(text=task)
        db.session.add(t)
        db.session.commit()

    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)
