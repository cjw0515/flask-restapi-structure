from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'employee_no': fields.String(required=True, description='employee_no'),
        'login_name': fields.String(required=True, description='login_name'),
        'name': fields.String(description='name'),
        'email': fields.String(description='email'),
        'user_password': fields.String(required=True, description='user_password'),
        'public_id': fields.String(description='public_id'),
        'phone_number': fields.String(description='phone_number'),
        'cell_number': fields.String(description='cell_number'),
        'gender': fields.String(description='gender'),
        'date_of_birth': fields.String(description='date_of_birth'),
        'department_id': fields.String(description='department_id'),
        'job_id': fields.String(description='job_id'),
        'group_id': fields.String(description='group_id'),
        'hired_date': fields.String(description='hired_date'),
        'retire_date': fields.String(description='retire_date'),
    })
    user_info = api.model('user_info', {
        'email': fields.String(required=True, description='user email address'),
        'login_name': fields.String(required=True, description='login_name'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier'),
        'create_date': fields.Date(description='user registered date'),
        'group_id': fields.Integer(description='user level')
    })
    user_info_permission = api.model('user_permissions', {
        'login_name': fields.String(required=True, description='user username'),
        'group_name': fields.String(description='user group_name')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='The login id'),
        'password': fields.String(required=True, description='The user password '),
    })


class TodoDto:
    api = Namespace('todo', description='todo related operations')
    todo = api.model('todo', {
        'todo': fields.String(required=True, description='todo'),
        'id': fields.Integer(description='id'),
    })


class UserGroup:
    api = Namespace('group', description='group')
    user_group = api.model('group', {
        'group_id': fields.Integer(required=True, description='group id'),
        'group_name': fields.String(description='group_name'),
    })