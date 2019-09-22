from app.main import db
from app.main.model.insti.models import CodeAge


def get_codes(page=1, per_page=10):
    page_obj = CodeAge.query.paginate(page=page, per_page=per_page)
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


def update_code(data, code_keys: dict = {}):
    code = CodeAge.query.filter_by(age_no=code_keys['age_no'],
                                   gbn=code_keys['gbn'],
                                   age_name=code_keys['age_name'],
                                   use_yn=code_keys["use_yn"]).first()

    code.age_no = data['ageNo']
    code.gbn = data['gbn']
    code.age_name = data['ageName']
    code.use_yn = data['status']

    db.session.commit()

    return {
        'status': 'success',
        'message': 'Successfully updated.'
    }, 201