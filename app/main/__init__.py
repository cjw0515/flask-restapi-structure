# -- coding: utf-8 --
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from definitions import STATIC_PATH, TEMPLATE_FOLDER
from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
"""
    about flask config : https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    about flask_sqlalchemy : https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/
"""


def create_app(config_name):
    # print(config_name)
    app = Flask(__name__,
                static_folder=STATIC_PATH,
                template_folder=TEMPLATE_FOLDER)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    """
    This helper function wraps the eponymous method of Bcrypt.
    It is intended to be used as a helper function at the expense of the configuration variable provided
    when passing back the app object.
    """
    flask_bcrypt.init_app(app)

    @app.route('/')
    def catch_all():
        return render_template("index.html")

    return app
