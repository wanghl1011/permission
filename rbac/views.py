from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.db import transaction
from rbac.models import *
from django.conf import settings
from rbac.service.init_power import init_power
import re
from rbac.permissopn import base

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username,password)
        # user=auth.authenticate(username=username,password=password)
        # if user:
        #     # for item in user.user_roles:
        #     #     print(item)
        #     # title_list=[]
        #     with transaction.atomic():
        #         roles_id=User_Role.objects.filter(user_id=user.nid).values("role_id")
        #         role_id=[item.get("role_id") for item in roles_id]
        #         print(role_id)
        #
        #         role_title=Role.objects.filter(nid__in=role_id).values("title")
        #
        #         powers_id=Role_Power.objects.filter(role_id__in=role_id).values("power_id")
        #         power_id=[item.get("power_id") for item in powers_id]
        #
        #         power_list=Power.objects.filter(nid__in=power_id)
        #         print(power_list)
        #     auth.login(request, user)
        #     url_list=[]
        #     for power in power_list:
        #         url_list.append(power.power_url)
        #     request.session["power_list"] = url_list
        #     title_list=[item.title for item in power_list]
        user = MyUserInfo.objects.filter(username=username, password=password).first()
        if user:
            # 初始化权限信息
            role_title, power_list = init_power(request, user)

            title_list = [item.title for item in power_list]
            return render(request, 'index.html',
                          {"power_list": power_list, "title_list": title_list, "role_title": role_title})
        else:
            return HttpResponse("登录失败")
    else:
        return render(request, 'login.html')


# def index(request):
#     if request.user.username:
#         power_list=request.session.get(settings.POWER_SESSION_KEY)
#         # print(power_list)
#         return  render(request,'index.html',{"power_list":power_list})
#
#     else:
#         return redirect('/qx/test')


def func1(request):
    return HttpResponse("添加用户")


def func2(request, id):
    return HttpResponse("编辑用户")


def func3(request, id):
    return HttpResponse("删除用户")





def user_list(request):
    permission_dict = request.permission_dict
    user_list = MyUserInfo.objects.all()
    power_group_id = str(PowerGroup.objects.get(gname="用户组").nid)
    # permissions = permission_dict[power_group_id]["codes"]
    print("view",permission_dict)
    per = base.Permission(permission_dict[power_group_id]["codes"])

    # 生成动态菜单
    # 用户访问的URL
    # url_info = request.path_info
    # 用于生成动态菜单的列表
    # menu_list = request.session[settings.MENU_SESSION_KEY]
    # print(menu_list)
    # s = [{'id': 4, 'title': '添加用户', 'pid': 11, 'url': '/qx/add/user/', 'menu_id': 1, 'menu_title': '用户管理'},
    #      {'id': 5, 'title': '编辑用户', 'pid': 11, 'url': '/qx/edit/user/(\\d+)/', 'menu_id': 1, 'menu_title': '用户管理'},
    #      {'id': 6, 'title': '删除用户', 'pid': 11, 'url': '/qx/del/user/(\\d+)/', 'menu_id': 1, 'menu_title': '用户管理'},
    #      {'id': 7, 'title': '添加订单', 'pid': 10, 'url': '/qx/add/order/', 'menu_id': 1, 'menu_title': '用户管理'},
    #      {'id': 10, 'title': '订单列表', 'pid': None, 'url': '/qx/orders/', 'menu_id': 1, 'menu_title': '用户管理'},
    #      {'id': 11, 'title': '用户列表', 'pid': None, 'url': '/qx/users/', 'menu_id': 1, 'menu_title': '用户管理'}]
    #
    # a = {10: {'id': 10, 'title': '订单列表', 'pid': None, 'url': '/qx/orders/', 'menu_id': 1, 'menu_title': '用户管理',
    #           'active': False},
    #      11: {'id': 11, 'title': '用户列表', 'pid': None, 'url': '/qx/users/', 'menu_id': 1, 'menu_title': '用户管理',
    #           'active': False}}


    # f = {10: {'id': 10, 'title': '订单列表', 'pid': None, 'url': '/qx/orders/', 'menu_id': 1, 'menu_title': '用户管理',
    #           'active': False},
    #      12: {'id': 10, 'title': '订单列表', 'pid': None, 'url': '/qx/orders/', 'menu_id': 2, 'menu_title': '用户管理',
    #           'active': True},
    #      13: {'id': 10, 'title': '订单列表', 'pid': None, 'url': '/qx/orders/', 'menu_id': 2, 'menu_title': '用户管理',
    #           'active': False},
    #      14: {'id': 10, 'title': '订单列表', 'pid': None, 'url': '/qx/orders/', 'menu_id': 2, 'menu_title': '用户管理',
    #           'active': False},
    #      15: {'id': 10, 'title': '订单列表', 'pid': None, 'url': '/qx/orders/', 'menu_id': 1, 'menu_title': '用户管理',
    #           'active': False},
    #      16: {'id': 10, 'title': '订单列表', 'pid': None, 'url': '/qx/orders/', 'menu_id': 1, 'menu_title': '用户管理',
    #           'active': False},
    #      11: {'id': 11, 'title': '用户列表', 'pid': None, 'url': '/qx/users/', 'menu_id': 1, 'menu_title': '用户管理',
    #           'active': True}}



    # g = {1: {'title': '用户管理',
    #          'active': True,
    #          'children':
    #              [
    #                  {'title': '订单列表', 'url': '/qx/orders/', 'active': False},
    #                 {'title': '用户列表', 'url': '/qx/users/', 'active': True}]}}

    return render(request, 'user_list.html', locals())

def orders(request):

    return render(request,'orders.html')
def menu(request):
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
            'active': True,
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
    return render(request, 'menu.html', {"menu_dict": menu_dict})
