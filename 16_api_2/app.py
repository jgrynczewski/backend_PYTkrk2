import xml.etree.ElementTree as ET

import requests
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    q = request.form.get("q")

    res = requests.get("https://www.goodreads.com/search.xml",
                       params={
                           "key": "c0xhe8onKJvo7agFJSwAkw",
                           "q": q
                       })

    root = ET.fromstring(res.content)

    elements = root.findall("./search/results/work/best_book/image_url")
    image_urls = [item.text for item in elements]

    elements = root.findall("./search/results/work/best_book/title")
    titles = [item.text for item in elements]

    content = {"image_urls": image_urls, "titles": titles}

    return render_template("search.html", content=content)