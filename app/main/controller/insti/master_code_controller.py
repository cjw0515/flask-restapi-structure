from flask import request
from flask_restplus import Resource, marshal, fields
from app.main.util.decorator import token_required
from app.main.util.insti.master_code_dto import MasterCodeDto
from app.main.service.insti.master_code_service import get_codes, get_a_codes

api = MasterCodeDto.api
masterCode = MasterCodeDto.master_code


@api.route('/<code_number>')
@api.param('code_number', '키 코드')
@api.response(404, 'code not found.')
class MasterCodeList(Resource):
    @api.doc('MasterCodeList data')
    @api.marshal_list_with(masterCode)
    def get(self, code_number):
        result = get_a_codes(code_number)
        return result


@api.route('/childCodes/<parent_code>/depth/<depth>', endpoint='childCodes')
@api.param('parent_code', '부모 코드')
@api.param('depth', '깊이')
@api.response(404, 'code not found.')
class MasterCodeList2(Resource):
    @api.doc('MasterCodeList data')
    @api.marshal_list_with(masterCode)
    def get(self, parent_code, depth):
        res = get_codes(parent_code, depth)
        print(res)
        data = {'a': 100, 'b': 'foo', 'c': None}
        mfields = {'a': fields.Raw, 'c': fields.Raw, 'd': fields.Raw}
        print(marshal(res, masterCode))
        return res
