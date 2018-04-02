from django.contrib import admin
from django.conf.urls import url, include
from app01 import views
urlpatterns = [
    url('^users/',views.user_list),
]