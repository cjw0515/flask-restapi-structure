import os
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


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
CORS(app)
app.register_blueprint(blueprint)
app.app_context().push()

# flask_script : https://flask-script.readthedocs.io/en/latest/
manager = Manager(app)
# flask_migrate : https://flask-migrate.readthedocs.io/en/latest/
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
