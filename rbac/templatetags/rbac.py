import re
from django.conf import settings
from django.template import Library
register = Library()


@register.inclusion_tag("rbac_menu.html")
def menu(request):
    # 用户访问的URL
    url_info = request.path_info
    # 用于生成动态菜单的列表
    menu_list = request.session[settings.MENU_SESSION_KEY]
    menu_dict = {}
    for item in menu_list:
        pid = item['pid']
        if not pid:
            item['active'] = False
            menu_dict[item['id']] = item
    for item in menu_list:
        pid = item['pid']
        url = "^%s$" % item['url']
        if re.match(url, url_info):
            if pid:
                menu_dict[pid]['active'] = True
            else:
                item['active'] = True
    menu_result = {}
    for item in menu_dict.values():
        menu_id = item['menu_id']
        if menu_id in menu_result:
            temp = {'title': item['title'], 'url': item['url'], 'active': item['active']}
            menu_result[menu_id]['children'].append(temp)
            if item['active']:
                menu_result[menu_id]['active'] = True
        else:
            menu_result[menu_id] = {
                'title': item['menu_title'],
                'active': item['active'],
                'children': [
                    {'title': item['title'], 'url': item['url'], 'active': item['active']}
                ]
            }
    return {"menu_result":menu_result}