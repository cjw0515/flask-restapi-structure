from flask_restplus import Namespace, fields


class AdminMenuDto:
    api = Namespace('adminMenu', description='어드민 메뉴')

    admin_menu = api.model('admin_menu', {
        'id': fields.Integer(description='id', attribute='id'),
        'parentId': fields.Integer(description='parent_id', attribute='parent_id'),
        'component': fields.String(description='component', attribute='component'),
        'name': fields.String(description='name', attribute='name'),
        'path': fields.String(description='path', attribute='path'),
        'hidden': fields.Boolean(description='hidden', attribute='hidden'),
        'redirect': fields.Boolean(description='redirect', attribute='redirect'),
        'roles': fields.String(description='roles', attribute='roles'),
        'title': fields.String(description='title', attribute='title'),
        'icon': fields.String(description='icon', attribute='icon'),
        'noCache': fields.Boolean(description='no_cache', attribute='no_cache'),
        'affix': fields.Boolean(description='affix', attribute='affix'),
        'breadcrumb': fields.Boolean(description='breadcrumb', attribute='breadcrumb'),
        'regDate': fields.DateTime(description='regdate', attribute='regdate'),
        'lastModUser': fields.String(description='last_mod_user', attribute='last_mod_user'),
        'status': fields.Boolean(description='status', attribute='status'),
    })






















