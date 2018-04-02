from django.contrib import admin
from rbac.models import *
# Register your models here.
admin.site.register(MyUserInfo)
admin.site.register(Role)
admin.site.register(Power)
admin.site.register(User_Role)
admin.site.register(Role_Power)
admin.site.register(PowerGroup)
