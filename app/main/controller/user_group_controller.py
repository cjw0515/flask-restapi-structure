# -- coding: utf-8 --
from flask import request
from flask_restplus import Resource

from ..util.dto import UserGroup
from ..service.user_group_service import save_new_group

api = UserGroup.api
user_group_dto = UserGroup.user_group

@api.route('/')
class UserList(Resource):
    # @api.doc('list_of_registered_users')
    # @api.marshal_list_with(user_group_dto, envelope='data')
    # def get(self):
    #     return get_all_group()

    @api.response(201, 'group successfully created.')
    @api.doc('create a new group')
    @api.expect(user_group_dto, validate=True)
    def post(self):
        """Creates a new User group """
        data = request.json
        return save_new_group(data=data)