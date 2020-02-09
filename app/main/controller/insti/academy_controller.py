# -- coding: utf-8 --
from flask import request
from flask_restplus import Resource, marshal
from app.main.util.insti.academy_dto import AcademyDto
from app.main.service.insti.academy_service import get_academies, update_academy, insert_academy, get_a_academy, get_a_academy_info
from ...util.decorator import token_required

api = AcademyDto.api
academy = AcademyDto.academy
academy_addition = AcademyDto.academy_addition


@api.route('/')
class AcademyList(Resource):
    @api.doc('academy data')
    def get(self):
        result = get_academies()
        list = marshal(result['list'], academy)
        data = {
            'data': {
                'list': list,
                'total': result['total'],
                'perPage': result['perPage']
            }
        }
        return data

    @api.response(201, 'academy successfully created.')
    @api.doc('create a new academy')
    @api.expect(academy)
    def post(self):
        data = request.json
        return insert_academy(data=data)


@api.route('/<insti_no>')
@api.param('insti_no', '학원 키')
@api.response(404, 'academy not found.')
class Academy(Resource):
    @api.doc('get a academy')
    def get(self, insti_no):
        """get a academy given its identifier"""
        data = {
            'data': get_a_academy_info(insti_no)
        }
        # for o in data['data']['details']:
        #     print(o)

        if not data:
            api.abort(404)
        else:
            return data

    @token_required
    @api.doc('학원 정보 수정')
    @api.response(201, '수정 성공.')
    def put(self, insti_no):
        data = request.json
        return update_academy(insti_no, data)