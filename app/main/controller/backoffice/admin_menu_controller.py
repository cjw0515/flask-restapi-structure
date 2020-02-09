# -- coding: utf-8 --
from flask import request
from flask_restplus import Resource
from app.main.util.decorator import token_required
from app.main.util.backoffice.admin_menu_dto import AdminMenuDto
from app.main.service.backoffice.admin_menu_service import insert_admin_menu, get_admin_menus,update_menu_status
from app.main.service.auth_helper import Auth

api = AdminMenuDto.api
admin_menu = AdminMenuDto.admin_menu
menu_status = AdminMenuDto.menu_status

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

@api.route('/<id>')
@api.param('id', '메뉴 아이디')
@api.response(404, 'not found')
class AdminMenu(Resource):
    @token_required
    @api.doc('메뉴 수정')
    @api.response(201, 'User successfully updated.')
    @api.expect(menu_status)
    def put(self, id):
        data = request.json
        print(data)

        return update_menu_status(id, data)