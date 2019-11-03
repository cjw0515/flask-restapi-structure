from app.main import db
from app.main.model.backoffice.admin_menu import AdminMenu
from flask_restplus import marshal
from app.main.util.backoffice.admin_menu_dto import AdminMenuDto


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
        component=data['component']
    )

    save_changes(new_menu)

    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201


def get_admin_menus():
    """
    1. 최상위 메뉴 가져오기.
    2. 최상위 메뉴의 id값을 가진 자식메뉴 가져오기
    3. 상위메뉴의 children에 하위메뉴 집어넣기
    """
    result = get_children_menu(0)
    # print('ff', 'true' if get_children_menu(111) else 'false')
    # parsed_res = marshal(result, AdminMenuDto.admin_menu)

    tmp = generate_menus(result)
    return tmp


def generate_menus(menus: list):
    res = []
    parsed_menus = marshal(menus, AdminMenuDto.admin_menu)
    for menu in parsed_menus:
        tmp_children = get_children_menu(menu['id'])
        if tmp_children:
            menu['meta'] = {
                'roles': menu['roles'],          # control the page roles (you can set multiple roles)
                'title': menu['title'],          # the name show in sidebar and breadcrumb (recommend set)
                'icon': menu['icon'],          # the icon show in the sidebar
                'noCache': convert_bool(menu['noCache']),          # if set true, the page will no be cached(default is false)
                'affix': convert_bool(menu['affix']) ,          # if set true, the tag will affix in the tags-view
                'breadcrumb': convert_bool(menu['breadcrumb']),  # if set false, the item will hidden in breadcrumb(default is true)
                # 'activeMenu': parsed_menus['activeMenu']   # if set path, the sidebar will highlight the path you set
            }
            menu['children'] = generate_menus(tmp_children)
        res.append(menu)

    return res


def convert_bool(v):
    return True if int(v) == 1 else False

def get_children_menu(menu_id):
    result = db.session.query(AdminMenu)\
             .filter(AdminMenu.parent_id == menu_id, AdminMenu.status == 1)\
             .all()

    return result

def save_changes(data):
    db.session.add(data)
    db.session.commit()