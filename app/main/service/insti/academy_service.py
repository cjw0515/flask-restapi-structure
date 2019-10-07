from flask import request
from app.main import db
from app.main.model.insti.models import Insti, InstiAddition
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


def get_a_academy(insti_no):

    # result = db.session.query(Insti, InstiAddition)\
    #     .filter(Insti.insti_no == insti_no)\
    #     .filter(Insti.insti_no == InstiAddition.insti_no)\
    #     .first()

    result = db.session.query(Insti, InstiAddition)\
            .join(InstiAddition)\
            .filter(Insti.insti_no == insti_no)\
            .first()

    return {'insti': result[0], 'instiAddition': result[1]}


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


def update_academy(data, code_keys: dict = {}):
    code = Insti.query.filter_by(age_no=code_keys['ageNo'],
                                   gbn=code_keys['gbn'],
                                   age_name=code_keys['ageName']).first()
    code.age_no = data['ageNo']
    code.gbn = data['gbn']
    code.age_name = data['ageName']
    code.use_yn = data['status']

    db.session.commit()

    return {
        'status': 'success',
        'message': 'Successfully updated.'
    }, 201


def save_changes(data):
    db.session.add(data)
    db.session.commit()