from .. import db

class UserGroup(db.Model):
    __tablename__ = "user_group"

    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<UserGroup '{}'>".format(self.group_name)