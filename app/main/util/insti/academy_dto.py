from flask_restplus import Namespace, fields

class AcademyDto:
    api = Namespace('academy', description='학원 정보 리스트')

    academy = api.model('academy', {
        'instiNumber': fields.Integer(description='insti_no', attribute='insti_no'),
        'instiId': fields.String(description='insti_id', attribute='insti_id'),
        'instiName': fields.String(description='insti_name', attribute='insti_name'),
        'instiKname': fields.String(description='insti_kname', attribute='insti_kname'),
        'instiType1': fields.Integer(description='insti_type1', attribute='insti_type1'),
        'instiType2': fields.Integer(description='insti_type2', attribute='insti_type2'),
        'category1': fields.Integer(description='category1', attribute='category1'),
        'category2': fields.Integer(description='category2', attribute='category2'),
        'category3': fields.Integer(description='category3', attribute='category3'),
        'area1': fields.Integer(description='area1', attribute='area1'),
        'area2': fields.Integer(description='area2', attribute='area2'),
        'area3': fields.Integer(description='area3', attribute='area3'),
        'address1': fields.String(description='address1', attribute='address1'),
        'address2': fields.String(description='address2', attribute='address2'),
        'address3': fields.String(description='address3', attribute='address3'),
        'building': fields.String(description='building', attribute='building'),
        'zipcode': fields.String(description='zipcode', attribute='zipcode'),
        'oldAddress': fields.String(description='old_address', attribute='old_address'),
        'oldZipcode': fields.String(description='old_zipcode', attribute='old_zipcode'),
        'latitude': fields.String(description='latitude', attribute='latitude'),
        'longitude': fields.String(description='longitude', attribute='longitude'),
        'instiImg': fields.String(description='insti_img', attribute='insti_img'),
        'opentimeFlexYn': fields.Integer(description='opentime_flex_yn', attribute='opentime_flex_yn'),
        'entranExamYn': fields.Integer(description='entran_exam_yn', attribute='entran_exam_yn'),
        'homeworkAmount': fields.Integer(description='homework_amount', attribute='homework_amount'),
        'numLimit': fields.Integer(description='num_limit', attribute='num_limit'),
        'kakaoId': fields.Integer(description='kakao_id', attribute='kakao_id'),
        'naverId': fields.Integer(description='naver_id', attribute='naver_id'),
        'likeCnt': fields.Integer(description='like_cnt', attribute='like_cnt'),
        'founder': fields.String(description='founder', attribute='founder'),
        'numTeacher': fields.Integer(description='num_teacher', attribute='num_teacher'),
        'score': fields.Integer(description='score', attribute='score'),
        'updDate': fields.DateTime(description='upd_date', attribute='upd_date'),
        'updId': fields.String(description='upd_id', attribute='upd_id'),
        'status': fields.Integer(description='use_yn', attribute='use_yn'),
        'confirmYn': fields.String(description='use_yn', attribute='confirm_yn'),
        'regDate': fields.DateTime(description='reg_date', attribute='reg_date'),
        'confirmDate': fields.DateTime(description='confirm_date', attribute='confirm_date'),
    })
    academy_addition = api.model('academy_addition', {
        'instiNumber': fields.String(description='insti_no', attribute='insti_no'),
        'itemName': fields.String(description='item_name', attribute='item_name'),
        'seq': fields.String(description='seq', attribute='seq'),
        'itemValue': fields.String(description='item_value', attribute='item_value'),
        'itemProperty': fields.String(description='item_property', attribute='item_property'),
        'status': fields.String(description='use_yn', attribute='use_yn')
    })






















