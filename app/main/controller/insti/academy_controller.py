from flask import request
from flask_restplus import Resource, marshal
from app.main.util.insti.academy_dto import AcademyDto
from app.main.service.insti.academy_service import get_academies, update_academy, insert_academy, get_a_academy


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
class User(Resource):
    @api.doc('get a academy')
    def get(self, insti_no):
        """get a academy given its identifier"""
        result = get_a_academy(insti_no)
        tmp_data = marshal(result['insti'], academy)
        tmp_data.update(marshal(result['instiAddition'], academy_addition))

        data = {
            'data': tmp_data
        }

        if not data:
            api.abort(404)
        else:
            return data

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