from flask import request
from app.main import db
from app.main.model.insti.models import CodeAge
from app.main.util.utils import filter_query


def get_codes():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))

    query = request.args.get('query')
    code = request.args.get('code')
    tmp_filters = []
    if code:
        tmp_filters.append(CodeAge.gbn == code)
    if request.args.get('queryType') and query:
        if request.args.get('queryType') == 'age':
            tmp_filters.append(CodeAge.age_no == query)
        elif request.args.get('queryType') == 'ageName':
            tmp_filters.append(CodeAge.age_name.like('%{query}%'.format(query=query)))

    filters = tuple(tmp_filters)
    page_obj = db.session.query(CodeAge).filter(*filters).paginate(page=page, per_page=per_page)

    # print('has_next : ', page_obj.has_next)
    # print('has_prev : ', page_obj.has_prev)
    # for page in page_obj.iter_pages():
    #     print('iter_pages : ', page)
    # print('next : ', page_obj.next())
    # print('next_num : ', page_obj.next_num)
    # print('page : ', page_obj.page)
    # print('pages : ', page_obj.pages)
    # print('per_page : ', page_obj.per_page)
    # print('prev : ', page_obj.prev())
    # print('prev_num : ', page_obj.prev_num)
    # print('query : ', page_obj.query)
    # print('total : ', page_obj.total)

    return {'list': page_obj.items, 'total': page_obj.total, 'perPage': page_obj.per_page}


def insert_agecode(data):
    new_age_code = CodeAge(
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


def update_code(data, code_keys: dict = {}):
    code = CodeAge.query.filter_by(age_no=code_keys['ageNo'],
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