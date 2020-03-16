from flask import Flask, render_template
from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Converter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usd = db.Column(db.Numeric(10, 4), nullable=False)
    eur = db.Column(db.Numeric(10, 4), nullable=False)
    updated = db.Column(db.Date, nullable=False, default=datetime.now())

    def __repr__(self):
        return f'Updated at {self.updated}'


@app.route("/")
def home():
    data = get_exchange_data()
    latest_data = get_latest_data()
    return render_template("index.html", data=data, latest_data=latest_data)


def get_latest_data():
    latest_data = Converter.query.order_by(Converter.id.desc()).limit(10)
    return latest_data


def get_exchange_data():
    recent_data = Converter.query.order_by(Converter.id.desc()).first()
    if recent_data is not None:
        if recent_data.updated == datetime.today().date():
            return recent_data
    else:
        create_obj()
        recent_data = Converter.query.order_by(Converter.id.desc()).first()
        return recent_data


def create_obj():
    r = requests.get('https://api.exchangeratesapi.io/latest?base=EUR').json()
    usd_value = r['rates']['USD']
    eur_value = 1.0
    value = Converter(usd=usd_value, eur=eur_value)
    db.session.add(value)
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
