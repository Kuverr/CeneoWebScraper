from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html",)

@app.route("/extract")
def extract():
    return render_template("extract.html",)

@app.route("/products")
def products():
    return render_template("products.html",)

@app.route("/author")
def author():
    return render_template("author.html",)

@app.route("/product/<product_id>")
def product():
    return render_template("product.html",)