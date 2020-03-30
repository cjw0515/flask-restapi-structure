from flask import request
from pprint import pprint as pp
from sqlalchemy import and_
import datetime
from app.main import db
from app.main.model.insti.models import Insti, InstiAddition, InstiDetail, CodeMast
from app.main.util.insti.academy_dto import AcademyDto
from flask_restplus import Resource, marshal
from app.main.service.auth_helper import Auth
from app.main.util.utils import filter_query

SUBJECT_CODE = ['OS', 'R1', 'R2', 'R3', 'R4', 'R5']


def get_academies():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))

    query = request.args.get('query')
    is_check = request.args.get('chkOption')

    # print(request.args)

    tmp_filters = []
    if request.args.get('queryType') and query:
        if request.args.get('queryType') == 'instiNumber':
            tmp_filters.append(Insti.insti_no == query)
        elif request.args.get('queryType') == 'instiName':
            tmp_filters.append(Insti.insti_name.like(
                '%{query}%'.format(query=query)))

    if is_check == '1':
        tmp_filters.append(Insti.confirm_yn == 1)
    elif is_check == '0':
        tmp_filters.append(Insti.confirm_yn == 0)

    filters = tuple(tmp_filters)
    page_obj = db.session.query(Insti).filter(*filters).order_by(Insti.insti_no.desc()).paginate(page=page,
                                                                                                 per_page=per_page)
    db.session.commit()

    return {'list': page_obj.items, 'total': page_obj.total, 'perPage': page_obj.per_page}


def get_a_academy_info(insti_no):
    insti = marshal(get_a_academy(insti_no), AcademyDto.academy)
    tmp_details = get_details(insti_no)
    additions = marshal(get_additions(insti_no), AcademyDto.academy_addition)
    details = []

    for o in tmp_details:
        tmp_obj = marshal(o[0], AcademyDto.academy_detail)
        tmp_obj['disp'] = o[1]
        details.append(tmp_obj)

    db.session.commit()

    return {
        'insti': insti,
        'details': details,
        'additions': additions
    }


def get_a_academy(insti_no):
    result = db.session.query(Insti) \
        .filter(Insti.insti_no == insti_no) \
        .first()

    db.session.commit()

    return result


def get_details(insti_no):
    """
    SELECT a.*, b.code_name
      FROM insti.insti_detail AS a
     left JOIN code_mast b ON a.code_no = b.code_no 
      AND a.gbn IN (
        'OS','R2'
     )
    """

    stmt = db.session \
        .query(CodeMast.code_name, CodeMast.code_no) \
        .subquery()

    result = db.session.query(InstiDetail, stmt.c.code_name) \
        .filter(InstiDetail.insti_no == insti_no) \
        .outerjoin(stmt, and_(InstiDetail.code_no == stmt.c.code_no, InstiDetail.gbn.in_(SUBJECT_CODE))) \
        .all()

    db.session.commit()

    # for o in result:
    #     print(o)

    return result


def get_additions(insti_no):
    result = db.session.query(InstiAddition) \
        .filter(InstiAddition.insti_no == insti_no) \
        .all()

    db.session.commit()

    return result


def insert_academy(data):
    new_insti = Insti(
        insti_id='inst_id',
        insti_name=data['insti']['instiName'],
        insti_kname=data['insti']['instiKname'],
        insti_type1=1,
        insti_type2=10,
        category1=100,
        category2=200,
        category3=300,
        area1=501,
        area2=521,
        area3=1006,
        address1=data['insti']['address1'],
        address2=data['insti']['address2'],
        address3=data['insti']['address3'],
        building=data['insti']['building'],
        zipcode=data['insti']['zipcode'],
        old_address=data['insti']['oldAddress'],
        old_zipcode=data['insti']['oldZipcode'],
        latitude=data['insti']['latitude'],
        longitude=data['insti']['longitude'],
        insti_img=data['insti']['instiImg'],
        opentime_flex_yn=None,
        entran_exam_yn=None,
        homework_amount=None,
        founder=data['insti']['founder'],
        num_teacher=None,
        num_limit=None,
        like_cnt=None,
        score=None,
        kakao_id=None,
        naver_id=None,
        reg_date=datetime.datetime.utcnow(),
        upd_date=None,
        upd_id=None,
        confirm_yn=None,
        confirm_date=None,
        use_yn=1,
    )
    save_changes(new_insti)
    new_insti_key = new_insti.insti_no
    if 'detailData' in data:
        chk_detail_data(data['detailData'], new_insti_key)
    if 'additionData' in data:
        chk_addition_data(data['additionData'], new_insti_key)

    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    db.session.commit()
    return response_object, 201


def update_academy(key, data):
    insti_key = key
    if not insti_key:
        return

    if 'insti' in data:
        update_insti(data['insti'], insti_key)
    if 'detailData' in data:
        chk_detail_data(data['detailData'], insti_key)
    if 'additionData' in data:
        chk_addition_data(data['additionData'], insti_key)

    db.session.commit()

    return {
        'status': 'success',
        'message': 'Successfully updated.'
    }, 201


def update_insti(data, insti_key):
    if not insti_key:
        return
    insti = Insti.query.filter_by(insti_no=insti_key).first()

    for key, val in data.items():
        insti.__setattr__(
            AcademyDto.academy._schema['properties'][key]['description'], val)

    insti.confirm_date = datetime.datetime.utcnow() if insti.confirm_yn == 1 else None
    insti.upd_id = Auth.get_logged_in_user(request)[0]['data']['name']
    insti.upd_date = datetime.datetime.utcnow()
    insti.use_yn = data['useYn'] if 'useYn' in data else 1

    db.session.commit()


def chk_detail_data(data, insti_key):
    if not data or not insti_key:
        return

    for o in SUBJECT_CODE:
        if next((item for item in data if item["gbn"] == o), None):
            delete_detail_data(o, insti_key)

    for o in data:
        # print(o)
        exists = InstiDetail.query.filter_by(
            insti_no=insti_key, gbn=o['gbn'], code_no=o['codeNo']).first()
        if not exists:
            insert_detail_data(o, insti_key)
        else:
            update_detail_data(o, insti_key)

    db.session.commit()


def delete_detail_data(gbn, insti_key):
    if not gbn or not insti_key:
        return

    db.session.query(InstiDetail).filter(InstiDetail.insti_no ==
                                         insti_key, InstiDetail.gbn == gbn).delete()
    db.session.commit()


def chk_addition_data(data, insti_key):
    if not data or not insti_key:
        return

    for o in data:
        # print(o)
        exists = InstiAddition.query.filter_by(insti_no=insti_key, item_name=o['itemName'],
                                               item_value=o['itemValue']).first()
        if not exists:
            insert_addition_data(o, insti_key)
        else:
            update_addition_data(o, insti_key)

    db.session.commit()


def insert_detail_data(data, insti_key):
    if not insti_key:
        return
    new_insti_detail = InstiDetail(
        insti_no=insti_key,
        gbn=data['gbn'],
        code_no=data['codeNo'],
        use_yn=data['useYn'],
    )
    save_changes(new_insti_detail)


def insert_addition_data(data, insti_key):
    if not insti_key:
        return
    new_insti_addition = InstiAddition(
        insti_no=insti_key,
        item_name=data['itemName'],
        seq=data['seq'],
        item_value=data['itemValue'],
        item_property=data['itemProperty'],
        use_yn=data['useYn'] or 1,
    )
    save_changes(new_insti_addition)


def update_addition_data(data, insti_key):
    if not insti_key:
        return
    addition_data = InstiAddition.query.filter_by(insti_no=insti_key, item_name=data['itemName'],
                                                  item_value=data['itemValue']).first()

    addition_data.item_name = data['itemName']
    addition_data.seq = data['seq']
    addition_data.item_value = data['itemValue']
    addition_data.item_property = data['itemProperty']
    addition_data.use_yn = data['useYn']
    db.session.commit()


def update_detail_data(data, insti_key):
    if not insti_key:
        return
    detail_data = InstiDetail.query.filter_by(
        insti_no=insti_key, gbn=data['gbn'], code_no=data['codeNo']).first()

    detail_data.insti_no = insti_key
    detail_data.gbn = data['gbn']
    detail_data.code_no = data['codeNo']
    detail_data.use_yn = data['useYn']
    db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
    db.session.refresh(data)
