# -- coding: utf-8 --
from flask_restplus import Namespace, fields


class MasterCodeDto:
    api = Namespace('masterCode', description='masterCode')

    master_code = api.model('master_code', {
        'codeNo': fields.Integer(discription='코드', attribute='code_no'),
        'parentCodeNo': fields.Integer(discription='부모 코드', attribute='parent_code_no'),
        'codeName': fields.String(discription='코드 명', attribute='code_name'),
        'status': fields.String(discription='사용 여부', attribute='use_yn'),
        'depth': fields.Integer(discription='depth', attribute='depth'),
        'regId': fields.String(discription='생성자', attribute='reg_id'),
        'regDate': fields.String(discription='생성 일자', attribute='reg_date'),
        'childCnt': fields.Integer(discription='자식 수', attribute='anon_1_cnt'),
    })

    master_code_mod = api.model('master_code', {
        'codeName': fields.String(discription='코드 명', attribute='code_name'),
        'status': fields.Integer(discription='사용 여부', attribute='use_yn'),
    })