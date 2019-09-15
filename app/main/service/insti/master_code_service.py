from app.main import db
from app.main.model.insti.models import CodeAge

def get_codes():

    return CodeAge.query.all()
