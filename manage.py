import os
from dotenv import load_dotenv, find_dotenv
from app.main.config import get_db_uri
from definitions import INSTI
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app import blueprint
from flask_cors import CORS
from app.main.model.user_group import UserGroup
from app.main.model.todo import Todo
from app.main.model.blacklist import BlacklistToken
from app.main.model.user import User
from app.main.model.group_permission import GroupPermission
from app.main.model.user_permission import UserPermission
from app.main.model.user_job import UserJob
from app.main.model.backoffice.admin_menu import AdminMenu

"""
flask_script : https://flask-script.readthedocs.io/en/latest/
flask_migrate : https://flask-migrate.readthedocs.io/en/latest/
"""
load_dotenv(find_dotenv())
"""
    * 환경변수
        dev
        test
        prod
"""
app = create_app(os.getenv('ADMIN_APP_ENV') or 'dev')
CORS(app)
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(port=os.getenv('PORT'))


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    # print(get_db_uri(env="DEV", db_name=INSTI))
    # 모델 업데이트 스크립트
    # flask-sqlacodegen (주소) --flask > models.py
    manager.run()