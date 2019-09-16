from app.main import db
from app.main.model.insti.models import CodeMast


def get_a_codes(code):
    return CodeMast.query.filter_by(code_no=code).first()


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
        tmp_list.append(obj[0])
        # print(obj[0].parent_code_no)

    # [(< CodeMast 100 >, 2), (< CodeMast 101 >, 2), (< CodeMast 102 >, 1), (< CodeMast 106 >, 1), (< CodeMast 108 >, 1),
    #  (< CodeMast 110 >, 1)]


    return tmp_list
