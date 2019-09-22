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
    # @api.marshal_list_with(ageCode, envelope='data')
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('perPage', 10))
        print('page : ', request.args.get('page'))
        result = get_codes(page=page, per_page=per_page)
        # {'list': page_obj.items, 'total': page_obj.total, 'perPage': page_obj.per_page}

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