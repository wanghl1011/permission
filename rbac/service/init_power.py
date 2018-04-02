from django.conf import settings
from rbac.models import *
from django.db import transaction


def init_power(request, user):
    # with transaction.atomic():
    # 当前登录用户对应的角色id
    roles_id = User_Role.objects.filter(user_id=user.nid).values("role_id")
    role_id = [item.get("role_id") for item in roles_id]

    # 当前登录用户的角色名
    role_title = Role.objects.filter(nid__in=role_id).values("title")

    # 当前登录用户对应的权限id
    powers_id = Role_Power.objects.filter(role_id__in=role_id).values("power_id").distinct()
    power_id = [item.get("power_id") for item in powers_id]

    # 当前登录用户对应的权限对象
    power_list = Power.objects.filter(nid__in=power_id)

    permission_list = [
        {
            "power_id": power.nid,  # 权限id
            "power_title": power.title,  # 权限名称
            "power_code": power.code,  # 权限代号
            "power_group_id": power.group_id,  # 权限所属权限组id
            "power_url": power.power_url,  # 权限URL
            'parent_id': power.parent_id,  # 组内菜单id
            'menu_id': power.group.menu_id,  # 菜单id
            'menu__title': power.group.menu.name,  # 菜单标题
        }
        for power in power_list]

    # 用于生成动态菜单

    menu_list = [
        {
            'id': row['power_id'],
            'title': row['power_title'],
            'pid': row['parent_id'],
            'url': row['power_url'],
            'menu_id': row['menu_id'],
            'menu_title': row['menu__title'], }
        for row in permission_list
    ]
    # print(menu_list)
    s = [{'id': 4, 'title': '添加用户', 'pid': 11, 'url': '/qx/add/user/', 'menu_id': 1, 'menu_title': '用户管理'},
         {'id': 5, 'title': '编辑用户', 'pid': 11, 'url': '/qx/edit/user/(\\d+)/', 'menu_id': 1, 'menu_title': '用户管理'},
         {'id': 6, 'title': '删除用户', 'pid': 11, 'url': '/qx/del/user/(\\d+)/', 'menu_id': 1, 'menu_title': '用户管理'},
         {'id': 7, 'title': '添加订单', 'pid': 10, 'url': '/qx/add/order/', 'menu_id': 2, 'menu_title': '订单管理'},
         {'id': 10, 'title': '订单列表', 'pid': None, 'url': '/qx/orders/', 'menu_id': 2, 'menu_title': '订单管理'},
         {'id': 11, 'title': '用户列表', 'pid': None, 'url': '/qx/users/', 'menu_id': 1, 'menu_title': '用户管理'}]

    request.session[settings.MENU_SESSION_KEY] = menu_list
    # 用于按钮级别权限控制
    # print(permission_list)
    permission_dict = {}
    for item in permission_list:
        group_id = item.get("power_group_id")
        if group_id in permission_dict:
            permission_dict[group_id]["urls"].append(item.get("power_url"))
            permission_dict[group_id]["codes"].append(item.get("power_code"))
        else:
            permission_dict[group_id] = {
                "urls": [item.get("power_url"), ],
                "codes": [item.get("power_code"), ]
            }
    print("init",permission_dict)
    s = {2: {'urls': ['/qx/add/user/', '/qx/edit/user/(\\d+)/', '/qx/del/user/(\\d+)/', '/qx/users/'],
             'codes': ['add', 'edit', 'del', 'list']},
         1: {'urls': ['/qx/add/order/', '/qx/orders/'], 'codes': ['add', 'list']}}

    # 用于URL级别权限控制
    url_list = []
    for power in power_list:
        url_list.append(power.power_url)
    request.session[settings.POWER_SESSION_KEY] = permission_dict

    return (role_title, power_list)
