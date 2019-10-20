from app.main import db
from app.main.model.backoffice.admin_menu import AdminMenu


def insert_admin_menu(data):
    new_menu = AdminMenu(
        parent_id=data['parentId'],
        name=data['name'],
        path=data['path'],
        hidden=data['hidden'],
        redirect=data['redirect'],
        roles=data['roles'],
        title=data['title'],
        icon=data['icon'],
        no_chashe=data['noChashe'],
        affix=data['affix'],
        breadcrumb=data['breadcrumb'],
        regdate=data['regDate'],
        last_mod_user=data['lastModUser'],
    )

    save_changes(new_menu)

    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201


def get_admin_menus():
    return AdminMenu.query.all()



def save_changes(data):
    db.session.add(data)
    db.session.commit()