from flask_restplus import Namespace, fields

class CodeAgeDto:
    api = Namespace('codeAge', description='code_age')

    code_age = api.model('code_age', {
        'age': fields.Integer(description='나이', attribute='age_no'),
        'gbn': fields.String(description='구분. C=그룹. A=별칭', attribute='gbn'),
        'ageName': fields.String(description='나이 명칭', attribute='age_name'),
        'status': fields.String(description='사용여부', attribute='use_yn'),
    })