from flask import request
from flask_restplus import Resource, marshal
from app.main.util.decorator import token_required
from app.main.util.insti.code_age_dto import CodeAgeDto
from app.main.service.insti.age_code_service import get_codes, update_code


api = CodeAgeDto.api
ageCode = CodeAgeDto.code_age


@api.route('/')
class AgeCodeList(Resource):
    @api.doc('ageCode data')
    def get(self):
        result = get_codes()
        list = marshal(result['list'], ageCode)
        data = {
            'data': {
                'list': list,
                'total': result['total'],
                'perPage': result['perPage']
            }
        }

        return data

    # @token_required
    @api.doc('age 코드정보 수정')
    @api.response(201, '수정 성공.')
    @api.expect(ageCode)
    def put(self):
        data = request.json
        params = {
            'ageNo': request.args.get('ageNo'),
            'gbn': request.args.get('gbn'),
            'ageName': request.args.get('ageName'),
            'status': request.args.get('status')
        }
        return update_code(data, params)