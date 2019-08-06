from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    # about flask config : https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    app.config.from_object(config_by_name[config_name])
    # about flask_sqlalchemy : https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/
    db.init_app(app)
    """
    This helper function wraps the eponymous method of Bcrypt. 
    It is intended to be used as a helper function at the expense of the configuration variable provided 
    when passing back the app object.
    """
    flask_bcrypt.init_app(app)

    return app
