from django.utils.deprecation import MiddlewareMixin
from django.middleware.csrf import CsrfViewMiddleware
from django.conf import settings
from django.shortcuts import HttpResponse,render,redirect
import re
class MyRbacMiddlewares(MiddlewareMixin):
    def process_request(self,request):
        # 不需要权限就可以访问的URL
        allow_url = settings.POWER_ALLOW_URL
        for url in allow_url:
            url_rule = "^%s$" % (url)
            if re.match(url_rule, request.path_info):
                # print("url_rule", url_rule)
                print(333333)
                return None
        print(444444)
        permission_dict=request.session.get(settings.POWER_SESSION_KEY)
        print("rbac",permission_dict)
        url_list=[]
        try:
            for value in permission_dict.values():
                for item in value.get("urls"):
                    url_list.append(item)
        except Exception as e:
            pass
        # 用户没有登录
        if not url_list:
            return HttpResponse("未查找到当前用户的权限信息，访问失败")

        # 需要验证权限的URL
        sign=0
        for url in url_list:
            url_rule="^%s$"%(url)
            if re.match(url_rule,request.path_info):
                sign=1
                break
        # print("sign",sign)
        request.permission_dict = request.session.get(settings.POWER_SESSION_KEY)
        if not sign:
            return HttpResponse("<h2>无权访问</h2>")