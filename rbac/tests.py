# from django.test import TestCase
#
# # Create your tests here.
# permission_list = [
#     {'permissions__title': '用户列表', 'permissions__group_id': 1, 'permissions__code': 'list',
#      'permissions__url': '/users/'},
#     {'permissions__title': '添加用户', 'permissions__group_id': 1, 'permissions__code': 'add',
#      'permissions__url': '/users/add/'},
#
#     {'permissions__title': '订单列表', 'permissions__group_id': 2, 'permissions__code': 'list',
#      'permissions__url': '/orders/'},
#
#     {'permissions__title': '删除订单', 'permissions__group_id': 2, 'permissions__code': 'del',
#      'permissions__url': '/orders/del/(\d+)/'},
#     {'permissions__title': '编辑订单', 'permissions__group_id': 2, 'permissions__code': 'edit',
#      'permissions__url': '/orders/edit/(\d+)/'},
# ]
# permission_dict = {}
# for item in permission_list:
#     group_id = item.get("permissions__group_id")
#     if group_id in permission_dict:
#         permission_dict[group_id]["urls"].append(item.get("permissions__url"))
#         permission_dict[group_id]["codes"].append(item.get("permissions__code"))
#     else:
#         permission_dict[group_id] = {
#             "urls": [item.get("permissions__url"), ],
#             "codes": [item.get("permissions__code"), ]
#         }
# print(permission_dict)
#
# re = {
#     1:
#         {
#             'urls': ['/users/', '/users/add/'],
#             'codes': ['list', 'add']
#         },
#     2:
#         {
#             'urls': ['/orders/', '/orders/del/(\d+)/', '/orders/edit/(\d+)/'],
#             'codes': ['list', 'del', 'edit']
#         }
#       }


menu_dict = {
    1: {
        'title': '菜单一',
        'active': True,
        'children': [
            {'title': '权限一', 'url': '/xxxxx/', 'active': False},
            {'title': '权限二', 'url': '/xxxxx/', 'active': True},
        ]
    },
    2: {
        'title': '菜单二',
        'active': False,
        'children': [
            {'title': '权限三', 'url': '/xxxxx/', 'active': False},
            {'title': '权限四', 'url': '/xxxxx/', 'active': False},
        ]
    },
    3: {
        'title': '菜单三',
        'active': False,
        'children': [
            {'title': '权限五', 'url': '/xxxxx/', 'active': False},
            {'title': '权限六', 'url': '/xxxxx/', 'active': False},
        ]
    }
}

test_dict = {}
# user=MyUserInfo.objects.get(nid=1)
# 当前登录用户对应的角色id
# roles_id = User_Role.objects.filter(user_id=user.nid).values("role_id")
# role_id = [item.get("role_id") for item in roles_id]

# 当前登录用户的角色名
# role_title = Role.objects.filter(nid__in=role_id).values("title")

# 当前登录用户对应的权限id
# powers_id = Role_Power.objects.filter(role_id__in=role_id).values("power_id").distinct()
# power_id = [item.get("power_id") for item in powers_id]

# 当前登录用户对应的权限对象
# power_list = Power.objects.filter(nid__in=power_id)

# permission_list=[{"group_title":powaaer.group.gname,"power_title": power.title, "power_group_id":power.group_id,"power_url":power.power_url} for power in power_list]
permission_list = [{'group_title': '用户组', 'power_title': '添加用户', 'power_code': 'add', 'power_group_id': 2,
                    'power_url': '/qx/add/user/'},
                   {'group_title': '用户组', 'power_title': '编辑用户', 'power_code': 'edit', 'power_group_id': 2,
                    'power_url': '/qx/edit/user/(\d+)/'},
                   {'group_title': '用户组', 'power_title': '删除用户', 'power_code': 'del', 'power_group_id': 2,
                    'power_url': '/qx/del/user/(\d+)/'},
                   {'group_title': '用户组', 'power_title': '用户列表', 'power_code': 'list', 'power_group_id': 2,
                    'power_url': '/qx/users/'}]

for item in permission_list:
    group_id = item.get("power_group_id")
    if group_id in test_dict:
        test_dict.get(group_id).get("children").append(
            {"title": item.get("power_title"), "url": item.get("power_url"), "active": "active"})
    else:
        test_dict[group_id] = {
            "title": item.get("group_title"),
            "active": "fffff",
            "children": [
                {"title": item.get("power_title"), "url": item.get("power_url"), "active": "active"}
            ]
        }

print(test_dict)
s = {
    2:
        {
            'title': '用户组',
            'active': 'fffff',
            'children': [
                { 'title': '添加用户','url': '/qx/add/user/', 'active': 'active'},
                {'title': '编辑用户', 'url': '/qx/edit/user/(\d+)/', 'active': 'active'},
                {'title': '删除用户', 'url': '/qx/del/user/(\d+)/', 'active': 'active'},
                {'title': '用户列表', 'url': '/qx/users/', 'active': 'active'}
            ]
        }
}
