from app.main import db

from app.main.model.insti.models import CodeMast


def get_a_codes(code):
    return CodeMast.query.filter_by(code_no=code).first()


def get_codes(parent_code, depth):
    return CodeMast.query.filter_by(parent_code_no=parent_code, depth=depth).all()
