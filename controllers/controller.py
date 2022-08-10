from app import app
from flask import render_template
from models.event_list import event1

@app.route("/")
def homepage():
    return render_template("index.html", event=event1)








