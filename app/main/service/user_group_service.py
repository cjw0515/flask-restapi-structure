from app.main import db
from app.main.model.user_group import UserGroup


def save_new_group(data):
    group = UserGroup.query.filter_by(group_id=data['group_id']).first()
    if not group:
        new_group = UserGroup(
            group_id=data['group_id'],
            group_name=data['group_name'],
        )
        save_changes(new_group)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def save_changes(data):
    db.session.add(data)
    db.session.commit()
