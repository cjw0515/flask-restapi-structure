# -- coding: utf-8 --
from flask import request
from flask_restplus import Resource, fields
from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto, UserDto

api = AuthDto.api
user_auth = AuthDto.user_auth
user_info_permission = UserDto.user_info_permission

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)


@api.route('/user')
@api.response(404, 'User not found.')
class UserToken(Resource):
    @api.doc('get a user from token')
    @api.marshal_with(user_info_permission)
    def get(self):
        # get auth token
        auth_token = request.headers.get('Authorization')

        # print(auth_token)
        if auth_token:
            auth_token = auth_token.split(" ")[1]
        else:
            auth_token = ''

        user = Auth.get_user_from_token(auth_token)
        if not user:
            api.abort(404)
        else:
            return user
