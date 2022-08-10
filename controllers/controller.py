from app import app
from flask import render_template
from models.order_list import orders

@app.route("/")
def homepage():
    return render_template("index.html", orders=orders)

@app.route("/orders/<int:index>/")
def order(index):
    return render_template("order.html", order=orders[index])







