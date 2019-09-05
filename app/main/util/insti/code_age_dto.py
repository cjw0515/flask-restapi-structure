from flask_restplus import Namespace, fields

class CodeAgeDto:
    api = Namespace('codeAge', description='code_age')

    code_age = api.model('code_age', {
        'age_no': fields.Integer(description='나이'),
        'gbn': fields.String(description='구분. C=그룹. A=별칭'),
        'age_name': fields.String(description='나이 명칭'),
        'use_yn': fields.String(description='사용여부')
    })