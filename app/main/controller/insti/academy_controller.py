from flask import request
from flask_restplus import Resource, marshal
from app.main.util.insti.academy_dto import AcademyDto
from app.main.service.insti.academy_service import get_academies, update_academy, insert_academy


api = AcademyDto.api
academy = AcademyDto.academy


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

    # @token_required
    @api.doc('age 코드정보 수정')
    @api.response(201, '수정 성공.')
    @api.expect(academy)
    def put(self):
        data = request.json
        params = {
            'ageNo': request.args.get('ageNo'),
            'gbn': request.args.get('gbn'),
            'ageName': request.args.get('ageName'),
            'status': request.args.get('status')
        }
        return update_academy(data, params)