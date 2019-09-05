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
        return get_codes()