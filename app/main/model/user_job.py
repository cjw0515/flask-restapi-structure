from .. import db

class UserJob(db.Model):
    __tablename__ = "user_job"
    __bind_key__ = "test"

    job_id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(20), nullable=False)
    create_date = db.Column(db.DateTime, default=db.func.now())
    update_date = db.Column(db.DateTime)

    def __repr__(self):
        return "<UserJob '{}'>".format(self.job_name)