# -- coding: utf-8 --
from .. import db, flask_bcrypt
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key

class User(db.Model):
    __tablename__ = "user"

    employee_no = db.Column(db.String(20), primary_key=True)
    login_name = db.Column(db.String(40), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(40))
    user_password = db.Column(db.String(255))
    public_id = db.Column(db.String(255), unique=True)
    phone_number = db.Column(db.String(20))
    cell_number = db.Column(db.String(20))
    gender = db.Column(db.Boolean, nullable=False)
    date_of_birth = db.Column(db.DateTime)
    department_id = db.Column(db.String(3), nullable=False)
    job_id = db.Column(db.String(3), nullable=False)
    group_id = db.Column(db.Integer, nullable=False)
    hired_date = db.Column(db.DateTime)
    retire_date = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, default=db.func.now())
    update_date = db.Column(db.DateTime)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.user_password = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.user_password, password)

    def __repr__(self):
        return "<User '{}'>".format(self.login_name)

    """
    pyJWT doc : https://pyjwt.readthedocs.io/en/latest/usage.html
    rfc 표준 JSON web token spec :  https://tools.ietf.org/html/rfc7519#section-4.1.4
    """
    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key, algorithm='HS256')
            # print('payload : ', payload)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return {'res': False, 'msg': '블랙리스트된 토큰입니다. 다시 로그인해 주세요.'}
            else:
                return {'res': True, 'msg': payload['sub']}
        except jwt.ExpiredSignatureError:
            return {'res': False, 'msg': '인증이 만료되었습니다. 다시 로그인해 주세요.'}
        except jwt.InvalidTokenError:
            return {'res': False, 'msg': '인증이 만료되었습니다. 다시 로그인해 주세요.'}
