import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(login_name=data['login_name']).first()
    if not user:
        new_user = User(
            employee_no=data['employee_no'],
            login_name=data['login_name'],
            name=data['name'],
            email=data['email'],
            # user_password=data['user_password'],
            password=data['user_password'],
            public_id=str(uuid.uuid4()),
            phone_number=data['phone_number'],
            cell_number=data['cell_number'],
            gender=True if data['gender'] == '1' else False,
            date_of_birth=None if data['date_of_birth'] == '' else data['date_of_birth'],
            department_id=data['department_id'],
            job_id=data['job_id'],
            group_id=data['group_id'],
            hired_date=None if data['hired_date'] == '' else data['hired_date'],
            retire_date=None if data['retire_date'] == '' else data['retire_date'],
            create_date=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        # response_object = {
        #     'status': 'success',
        #     'message': 'Successfully registered.'
        # }
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.public_id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def save_changes(data):
    db.session.add(data)
    db.session.commit()
