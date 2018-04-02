from django.shortcuts import render
from rbac.models import *
# Create your views here.
def user_list(request):
    permission_dict=request.permission_dict
    user_list=MyUserInfo.objects.all()
    powergroup_id=str(PowerGroup.objects.get(gname="用户组").nid)
    permissions=permission_dict[powergroup_id]["codes"]


    return render(request,'user_list.html',locals())