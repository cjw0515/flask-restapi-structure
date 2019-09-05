import os
from dotenv import load_dotenv, find_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# about flask config : https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# about flask_sqlalchemy : https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

load_dotenv(find_dotenv())
db_options1 = "mysql+pymysql://{user}:{pwd}@{ip}/{db}?charset=utf8".format(
    user=os.getenv("TESTUSER"),
    pwd=os.getenv("TESTPASSWORD"),
    ip=os.getenv("TESTIP"),
    db=os.getenv("TESTDB"),
)
db_options2 = "mysql+pymysql://{user}:{pwd}@{ip}/{db}?charset=utf8".format(
    user=os.getenv("DEVUSER"),
    pwd=os.getenv("DEVPASSWORD"),
    ip=os.getenv("DEVIP"),
    db=os.getenv("DEVDB"),
)


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = db_options2
    SQLALCHEMY_BINDS = {
        'test': db_options1,
        'dev': db_options2
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = {
        db_options1,
        db_options2
    }
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

if __name__ == "__main__":
    print(db_options2)