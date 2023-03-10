from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "build test" #encrypt or secure the cookies

    #import the modules
    from .views import views

    app.register_blueprint(views, url_prefix = "/")

    return app

