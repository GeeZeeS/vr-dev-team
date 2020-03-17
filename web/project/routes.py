from . import app
from flask import render_template
from .scripts import get_exchange_data, get_latest_data


@app.route("/")
def home():
    data = get_exchange_data()
    latest_data = get_latest_data()
    return render_template("index.html", data=data, latest_data=latest_data)
