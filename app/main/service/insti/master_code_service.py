from app.main import db
from app.main.model.insti.models import CodeMast
from flask_restplus import marshal
from app.main.util.insti.master_code_dto import MasterCodeDto

def get_a_codes(code):
    return CodeMast.query.filter_by(code_no=code).first()


def update_code(code_number, data):
    code = CodeMast.query.filter_by(code_no=code_number).first()
    code.code_name = data['codeName']
    code.use_yn = data['status']

    db.session.commit()

    return {
        'status': 'success',
        'message': 'Successfully updated.'
    }, 201


def get_codes(parent_code, depth):
    """
    SELECT a.* 	  
          , b.cnt
        FROM code_mast AS a
      left JOIN (
          SELECT parent_code_no
                , COUNT(*) AS cnt
            FROM code_mast
          GROUP BY parent_code_no  
      ) AS b ON b.parent_code_no = a.code_no   
      WHERE a.parent_code_no = 10
    """
    stmt = db.session\
        .query(CodeMast.parent_code_no, db.func.count('*').label('cnt')).\
        group_by(CodeMast.parent_code_no)\
        .subquery()

    result = db.session.query(CodeMast, stmt.c.cnt)\
        .filter(CodeMast.parent_code_no == parent_code, CodeMast.depth == depth)\
        .outerjoin(stmt, CodeMast.code_no == stmt.c.parent_code_no).all()

    tmp_list = []
    for obj in result:
        tmp_list.append(obj)

    return tmp_list

# 마스터 코드 가져오기


def get_mast_code_tree(code_no):

    result = get_children_code(code_no)

    tmp = generate_menus(result)
    return tmp


def get_children_code(parent_code_no):
    result = db.session.query(CodeMast)\
             .filter(CodeMast.parent_code_no == parent_code_no, CodeMast.use_yn == 1, CodeMast.code_no != parent_code_no)\
             .all()

    return result


def generate_menus(codes: list):
    res = []
    parsed_codes = marshal(codes, MasterCodeDto.master_code)
    for code in parsed_codes:
        tmp_children = get_children_code(code['codeNo'])

        if tmp_children:
            code['children'] = generate_menus(tmp_children)
        res.append(code)

    return res


