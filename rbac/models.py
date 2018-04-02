from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserInfo(AbstractUser):
    """
    用户表
    和角色表是多对多的关系
    """
    nid=models.AutoField(primary_key=True)
    # username=models.CharField(verbose_name="用户名",max_length=32,null=True)

    # user_roles=models.ManyToManyField(
    #     to="Role",
    #     through='User_Role',
    #     through_fields=('user', 'role'),
    # )
    def __str__(self):
        return self.username

class MyUserInfo(models.Model):
    """
    用户表
    和角色表是多对多的关系
    """
    nid=models.AutoField(primary_key=True)
    username=models.CharField(verbose_name="用户名",max_length=32,null=True)
    password=models.CharField(verbose_name="密码",max_length=32,null=True)
    email=models.EmailField()
    user_roles=models.ManyToManyField(
        to="Role",
        through='User_Role',
        through_fields=('user', 'role'),
    )
    def __str__(self):
        return self.username

class Power(models.Model):
    """
    权限表
    和角色表是多对多的关系
    """
    nid = models.AutoField(primary_key=True)
    power_url = models.CharField(verbose_name="权限URL",max_length=32,null=True)
    title=models.CharField(verbose_name="权限名",max_length=32,null=True)

    code=models.CharField(verbose_name="权限代号",max_length=32,default="add")
    group=models.ForeignKey(verbose_name="权限组",to='PowerGroup',default=1, to_field='nid',on_delete=None)

    parent=models.ForeignKey(verbose_name="可以作为菜单显示的权限",to='Power',null=True, to_field='nid',on_delete=None)

    power_roles=models.ManyToManyField(
        to="Role",
        through='Role_Power',
        through_fields=('power', 'role'),
    )
    def __str__(self):
        return self.title

class PowerGroup(models.Model):
    """
    权限组表
    和权限表是一对多的关系，权限组是一，权限是多
    """
    nid = models.AutoField(primary_key=True)
    gname=models.CharField(max_length=32,null=True)

    menu=models.ForeignKey(verbose_name="菜单",to='Menu', to_field='nid',on_delete=None,default=1)


class Role(models.Model):
    """
    角色表
    和用户表是多对多的关系
    和权限表是多对多的关系
    """
    nid = models.AutoField(primary_key=True)
    title=models.CharField(verbose_name="角色名",max_length=32,null=True)
    def __str__(self):
        return self.title

class Menu(models.Model):
    """
    菜单表
    和权限组表是一对多的关系，菜单是一，权限组是多
    """
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

class Role_Power(models.Model):
    """
    角色权限关系表
    """
    nid = models.AutoField(primary_key=True)
    role=models.ForeignKey(verbose_name="角色",to='Role', to_field='nid',on_delete=None)
    power=models.ForeignKey(verbose_name="权限",to='Power', to_field='nid',on_delete=None)

class User_Role(models.Model):
    """
    用户角色关系表
    """
    nid = models.AutoField(primary_key=True)
    user=models.ForeignKey(verbose_name="用户",to='MyUserInfo', to_field='nid',on_delete=None)
    role=models.ForeignKey(verbose_name="角色",to='Role', to_field='nid',on_delete=None)