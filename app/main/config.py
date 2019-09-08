import os
from definitions import INSTI, CJW0515_DB, BO
from dotenv import load_dotenv, find_dotenv
"""
    about flask config : https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    about flask_sqlalchemy : https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
    about flask config handling(Builtin Configuration Values) : https://flask.palletsprojects.com/en/1.1.x/config/
"""
load_dotenv(find_dotenv())


def get_db_uri(env="DEV", db_name="CJW0515_DB"):
    return "mysql+pymysql://{user}:{pwd}@{ip}/{db}?charset=utf8".format(
        user=os.getenv("{env}_USER".format(env=env)),
        pwd=os.getenv("{env}_PASSWORD".format(env=env)),
        ip=os.getenv("{env}_IP".format(env=env)),
        db=os.getenv("{db_name}".format(db_name=db_name)),
    )


class Config:
    SECRET_KEY = os.urandom(16)
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = get_db_uri(env="DEV", db_name=BO)
    SQLALCHEMY_BINDS = {
        # 'test': get_db_uri(env="TEST", db_name=CJW0515_DB),
        # 'bo': get_db_uri(env="TEST", db_name=BO),
        'insti': get_db_uri(env="TEST", db_name=INSTI),
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ""
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"
    SQLALCHEMY_DATABASE_URI = get_db_uri(db_name=INSTI)
    SQLALCHEMY_BINDS = {
        'test': get_db_uri(env="TEST", db_name=CJW0515_DB),
        'bo': get_db_uri(db_name=BO),
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

if __name__ == "__main__":
    print(os.urandom(16))