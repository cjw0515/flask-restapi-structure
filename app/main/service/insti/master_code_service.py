from app.main import db
from app.main.model.insti.models import CodeMast


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
