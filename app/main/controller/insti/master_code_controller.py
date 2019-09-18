from flask import request
from flask_restplus import Resource, marshal, fields
from app.main.util.decorator import token_required
from app.main.util.insti.master_code_dto import MasterCodeDto
from app.main.service.insti.master_code_service import get_codes, get_a_codes, update_code

api = MasterCodeDto.api
master_code = MasterCodeDto.master_code
master_code_mod = MasterCodeDto.master_code_mod

@api.route('/<code_number>')
@api.param('code_number', '키 코드')
@api.response(404, 'code not found.')
class MasterCodeList(Resource):
    @api.doc('마스터 코드 get')
    @api.marshal_list_with(master_code)
    def get(self, code_number):
        result = get_a_codes(code_number)
        return result

    # @token_required
    @api.doc('코드정보 수정')
    @api.response(201, '수정 성공.')
    @api.expect(master_code_mod)
    def put(self, code_number):
        data = request.json
        return update_code(code_number, data)

@api.route('/childCodes/<parent_code>/depth/<depth>', endpoint='childCodes')
@api.param('parent_code', '부모 코드')
@api.param('depth', '깊이')
@api.response(404, 'code not found.')
class MasterCodeList2(Resource):
    @api.doc('MasterCodeList data')
    def get(self, parent_code, depth):
        res = get_codes(parent_code, depth)
        tmp_res = []
        for obj in res:
            tmp_obj = marshal(obj[0], master_code)
            tmp_obj['childCnt'] = obj[1] or 0
            tmp_res.append(tmp_obj)

        return tmp_res
