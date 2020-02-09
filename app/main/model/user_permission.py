# -- coding: utf-8 --
from .. import db

class UserPermission(db.Model):
    __tablename__ = "user_permission"

    permission_id = db.Column(db.Integer, primary_key=True)
    permission_name = db.Column(db.String(20), nullable=False)
    create_date = db.Column(db.DateTime, default=db.func.now())
    update_date = db.Column(db.DateTime)

    def __repr__(self):
        return "<UserPermission '{}'>".format(self.permission_name)