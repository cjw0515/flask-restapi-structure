from flask import request
from flask_restplus import Resource
from app.main.util.decorator import token_required
from app.main.util.insti.code_age_dto import CodeAgeDto
from app.main.service.insti.age_code_service import get_codes


api = CodeAgeDto.api
ageCode = CodeAgeDto.code_age


@api.route('/')
class AgeCodeList(Resource):
    @api.doc('ageCode data')
    @api.marshal_list_with(ageCode, envelope='data')
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        # result = get_codes(page=page, per_page=per_page)
        # print(result)

        return get_codes(page=page, per_page=per_page)