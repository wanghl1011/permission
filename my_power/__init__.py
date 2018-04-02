from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception,request_finished

from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate

from django.test.signals import setting_changed
from django.test.signals import template_rendered

from django.db.backends.signals import connection_created


# def callback(sender, **kwargs):
#     print("pre_save_callback")
#     print(sender,kwargs)
#
# request_finished.connect(callback)      #该脚本代码需要写到app或者项目的初始化文件中，当项目启动时执行注册代码