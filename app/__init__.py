from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.todo_controller import api as todo_ns
from .main.controller.user_group_controller import api as user_group_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='admin web service',
          version='1.0',
          dApiescription='admin web service WITH JWT',
          doc='/doc/'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(todo_ns, path='/todo')
api.add_namespace(auth_ns)
api.add_namespace(user_group_ns)