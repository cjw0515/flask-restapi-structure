from .. import db

class UserGroup(db.Model):
    __tablename__ = "user_group"

    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(20), nullable=False)
    create_date = db.Column(db.DateTime, default=db.func.now())
    update_date = db.Column(db.DateTime)

    def __repr__(self):
        return "<UserGroup '{}'>".format(self.group_name)