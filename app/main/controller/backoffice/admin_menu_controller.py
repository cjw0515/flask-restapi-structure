from flask import request
from flask_restplus import Resource
from app.main.util.decorator import token_required
from app.main.util.backoffice.admin_menu_dto import AdminMenuDto
from app.main.service.backoffice.admin_menu_service import insert_admin_menu, get_admin_menus
from app.main.service.auth_helper import Auth

api = AdminMenuDto.api
admin_menu = AdminMenuDto.admin_menu

"""
flask-restplus examples : https://flask-restplus.readthedocs.io/en/stable/example.html
"""


@api.route('/')
class AdminMenus(Resource):
    @api.doc('어드민 메뉴')
    def get(self):
        return {'data': get_admin_menus()}

    @api.response(201, 'menu successfully created.')
    @api.doc('어드민 메뉴 추가')
    @api.expect(admin_menu)
    def post(self):
        data = request.json
        return insert_admin_menu(data=data)
#
# @api.route('/<id>')
# @api.param('id', 'The todo identifier')
# @api.response(404, 'todo found.')
# class Todo(Resource):
#     @token_required
#     @api.doc('get a todo')
#     @api.marshal_with(_todo)
#     def get(self, id):
#         todo = get_a_todo(id)
#         if not todo:
#             api.abort(404)
#         else:
#             return todo
#
#     @token_required
#     @api.doc('delete a user')
#     @api.response(204, 'User successfully deleted.')
#     def delete(self, id):
#         delete_todo(id)
#         return {
#         'status': 'success',
#         'message': 'Successfully deleted.'
#         }, 204
#
#     @token_required
#     @api.doc('modify todo')
#     @api.response(201, 'User successfully updated.')
#     @api.expect(_todo, validate=True)
#     def put(self, id):
#         data = request.json
#
#         return update_todo(id, data)