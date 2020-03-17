from flask.cli import FlaskGroup
from project import app, db, models, routes, scripts

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("fetch")
def fetch_currency():
    scripts.get_exchange_data()


if __name__ == "__main__":
    cli()
