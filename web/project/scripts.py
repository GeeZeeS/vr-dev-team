import requests
from datetime import datetime
from .models import Converter
from . import db


def get_latest_data():
    latest_data = Converter.query.order_by(Converter.id.desc()).limit(10)
    return latest_data


def get_exchange_data():
    recent_data = Converter.query.order_by(Converter.id.desc()).first()
    if recent_data is not None:
        if recent_data.updated == datetime.today().date():
            print(f"Rates for today were already updated \n"
                  f"Rates for 1 EUR consists {recent_data.usd} USD for {recent_data.updated}")
            return recent_data
    fetch_data()
    recent_data = Converter.query.order_by(Converter.id.desc()).first()
    print(f"Successfully Updated \n"
          f"Rates for 1 EUR consists {recent_data.usd} USD for {recent_data.updated}")
    return recent_data


def fetch_data():
    r = requests.get('https://api.exchangeratesapi.io/latest?base=EUR').json()
    usd_value = r['rates']['USD']
    eur_value = 1.0
    value = Converter(usd=usd_value, eur=eur_value)
    db.session.add(value)
    db.session.commit()
