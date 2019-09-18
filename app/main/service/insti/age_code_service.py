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

    return page_obj.items
