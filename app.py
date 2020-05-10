from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/adam")
def adam():
    return "Hello, Adam!"

@app.route("/ewa")
def ewa():
    return "Hello, Ewa!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"

@app.route("/test")
def test():
    return "<html><head></head><body><h2>Hello, world!</h2></body></html>"
