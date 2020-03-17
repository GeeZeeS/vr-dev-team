import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    TEMPLATES_FOLDER = f"{os.getenv('APP_FOLDER')}/project/templates"
