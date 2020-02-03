from flask import request
from app.main import db
from app.main.model.insti.models import Insti, InstiAddition, InstiDetail
from app.main.util.insti.academy_dto import AcademyDto
from flask_restplus import Resource, marshal
from app.main.util.utils import filter_query


def get_academies():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))

    query = request.args.get('query')

    # print(request.args)

    tmp_filters = []
    if request.args.get('queryType') and query:
        if request.args.get('queryType') == 'instiNumber':
            tmp_filters.append(Insti.insti_no == query)
        elif request.args.get('queryType') == 'instiName':
            tmp_filters.append(Insti.insti_name.like('%{query}%'.format(query=query)))

    filters = tuple(tmp_filters)
    page_obj = db.session.query(Insti).filter(*filters).paginate(page=page, per_page=per_page)

    return {'list': page_obj.items, 'total': page_obj.total, 'perPage': page_obj.per_page}


def get_a_academy_info(insti_no):
    insti = marshal(get_a_academy(insti_no), AcademyDto.academy)
    details = marshal(get_details(insti_no), AcademyDto.academy_detail)
    additions = marshal(get_additions(insti_no), AcademyDto.academy_addition)

    return {
        'insti': insti,
        'details': details,
        'additions': additions
    }


def get_a_academy(insti_no):
    result = db.session.query(Insti)\
            .filter(Insti.insti_no == insti_no)\
            .first()

    return result


def get_details(insti_no):
    result = db.session.query(InstiDetail)\
            .filter(InstiDetail.insti_no == insti_no)\
            .all()

    return result


def get_additions(insti_no):
    result = db.session.query(InstiAddition)\
            .filter(InstiAddition.insti_no == insti_no)\
            .all()

    return result


def insert_academy(data):
    new_age_code = Insti(
        age_no=data['age'],
        gbn=data['gbn'],
        age_name=data['ageName'],
        use_yn=1
    )
    save_changes(new_age_code)

    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201


def update_academy(key, data):
    insti = Insti.query.filter_by(insti_no=key).first()
    print(data)

    # db.session.commit()

    return {
        'status': 'success',
        'message': 'Successfully updated.'
    }, 201


def save_changes(data):
    db.session.add(data)
    db.session.commit()