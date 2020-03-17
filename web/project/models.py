from datetime import datetime
from . import db


class Converter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usd = db.Column(db.Numeric(10, 4), nullable=False)
    eur = db.Column(db.Numeric(10, 4), nullable=False)
    updated = db.Column(db.Date, nullable=False, default=datetime.now())

    def __repr__(self):
        return f'Updated at {self.updated}'
