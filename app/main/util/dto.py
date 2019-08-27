from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
    user_info = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier'),
        'registered_on': fields.Date(description='user registered date'),
        'group_id': fields.Integer(description='user level')
    })
    user_info_permission = api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'group_name': fields.String(description='user level')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class TodoDto:
    api = Namespace('todo', description='todo related operations')
    todo = api.model('todo', {
        'todo': fields.String(required=True, description='todo'),
        'id': fields.Integer(description='id'),
    })


class UserGroup:
    api = Namespace('usergroup', description='usergroup')
    user_group = api.model('group', {
        'group_id': fields.Integer(required=True, description='group id'),
        'group_name': fields.String(description='group name'),
    })