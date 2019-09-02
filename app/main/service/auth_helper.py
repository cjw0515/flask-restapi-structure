from app.main.model.user import User
from app.main.model.user_group import UserGroup
from ..service.blacklist_service import save_token


class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(login_name=data.get('username')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.employee_no)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'login name or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            auth_token = auth_token.split(" ")[1]
        else:
            auth_token = ''
        # print(auth_token)
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if resp:
                user = User.query.filter_by(employee_no=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.employee_no,
                        'email': user.email,
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

    @staticmethod
    def get_user_from_token(token):
        # get the auth token
        # auth_token = token
        # if auth_token:
        #     auth_token = auth_token
        # else:
        #     auth_token = ''
        if token:
            resp = User.decode_auth_token(token)
            if resp:
                # user = User.query.filter_by(id=resp).first()
                user = User.query\
                    .join(UserGroup, User.group_id == UserGroup.group_id)\
                    .add_columns(User.login_name, UserGroup.group_name)\
                    .filter(User.employee_no == resp).first()
                print(user)
                return {'login_name': user.login_name, 'group_name': user.group_name}, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401