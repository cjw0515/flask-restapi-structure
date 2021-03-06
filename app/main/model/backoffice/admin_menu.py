# -- coding: utf-8 --
from app.main import db


class AdminMenu(db.Model):
    __tablename__ = "admin_menu"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_id = db.Column(db.Integer)
    name = db.Column(db.String(50), nullable=False)
    path = db.Column(db.String(50), nullable=False)
    hidden = db.Column(db.Boolean, nullable=False, default=False)
    redirect = db.Column(db.String(100), nullable=True)
    component = db.Column(db.String(150), nullable=True)

    # meta
    roles = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(50))
    no_cache = db.Column(db.Boolean, nullable=False, default=False)
    affix = db.Column(db.Boolean, nullable=False, default=False)
    breadcrumb = db.Column(db.Boolean, nullable=False, default=True)

    status = db.Column(db.Boolean, nullable=False, default=True)
    regdate = db.Column(db.DateTime, nullable=False, default=db.func.now())
    reg_user = db.Column(db.String(50), nullable=False)
    update_date = db.Column(db.DateTime)
    last_mod_user = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<adminMenu '{}'>".format(self.name)