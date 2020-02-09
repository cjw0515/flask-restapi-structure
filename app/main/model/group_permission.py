# -- coding: utf-8 --
from .. import db

class GroupPermission(db.Model):
    __tablename__ = "group_permission"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_id = db.Column(db.Integer)
    permission_id = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, default=db.func.now())
    update_date = db.Column(db.DateTime)

    def __repr__(self):
        return "<GroupPermission '{}'>".format(self.group_id)